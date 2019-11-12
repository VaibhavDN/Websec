package com.atootbal.websec

import android.content.Intent
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Layout
import android.util.Log
import android.view.Gravity
import android.view.View
import android.widget.*
import androidx.core.content.ContextCompat
import androidx.core.view.marginLeft
import kotlinx.android.synthetic.main.activity_dashboard.*
import org.json.JSONArray
import org.jsoup.Jsoup
import java.lang.Exception
import java.util.*

class Dashboard : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dashboard)
        val getExtras = intent.extras
        var jsonString = getExtras!!.getString("json")
        var adminUsername = getExtras.getString("username")
        var adminPassword = getExtras.getString("password")
        Toast.makeText(this, "Welcome: "+adminUsername, Toast.LENGTH_SHORT).show()
        var json = JSONArray(jsonString)
        //Toast.makeText(this, json.getJSONObject(0).getString("username").toString(), Toast.LENGTH_LONG).show()
        var buttonSave = Button(this)
        var buttonLogs = Button(this)
        var initTextView = TextView(this)
        var textView = Array<TextView>(json.length()){initTextView}
        var initCheckBox = CheckBox(this)
        var checkbox = Array<CheckBox>(json.getJSONObject(0).getString("statusString").length){initCheckBox}

        //****Dropdown****
        var usernameArray = Array<String>(json.length()){""}
        for(i in 0 until(json.length()) step 1){
            usernameArray[i] = json.getJSONObject(i).getString("username").toString().capitalize()
        }
        var adapter = ArrayAdapter(this, R.layout.spinner, usernameArray)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        var spinner = Spinner(this)
        spinner.setPadding(20, 20 , 20 ,20)
        spinner.setBackgroundColor(Color.argb(20, 0, 0, 200))
        spinner.setPopupBackgroundDrawable(ColorDrawable(ContextCompat.getColor(this, R.color.spinnerPopUpBackground)))
        spinner.adapter = adapter
        var lastPosition = 1234
        spinner.onItemSelectedListener = object:AdapterView.OnItemSelectedListener{
            override fun onNothingSelected(parent: AdapterView<*>?) {
                //pass
            }

            override fun onItemSelected(
                parent: AdapterView<*>?,
                view: View?,
                position: Int,
                id: Long
            ) {
                if(lastPosition!=1234)
                {
                    textView[lastPosition].visibility = View.GONE
                    for(j in 0 until(json.getJSONObject(0).getString("statusString").length) step 1){
                        checkbox[j].visibility = View.GONE
                    }
                }
                Toast.makeText(applicationContext, "Selected: "+usernameArray[position], Toast.LENGTH_SHORT).show()
                var i=position
                lastPosition = position
                textView[i] = TextView(applicationContext)
                textView[i].id = i
                textView[i].textSize = 20f
                textView[i].text = "Select the categories to block for: " + usernameArray[i]
                textView[i].setTextColor(Color.rgb(102,0,153))
                textView[i].setPadding(40,40,20,20)
                dashboard_llayout.addView(textView[i])
                try {
                    val models = arrayOf("Game", "Shopping", "Payment", "Movie", "Video", "Tech", "Entertainment")
                    for(j in 0 until(json.getJSONObject(0).getString("statusString").length) step 1){
                        checkbox[j] = CheckBox(applicationContext)
                        var param = LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT) //LinearLayout.LayoutParams.WRAP_CONTENT are width and height respectively
                        param.setMargins(40,20,20,20)
                        checkbox[j].layoutParams = param
                        checkbox[j].text = models[j]
                        checkbox[j].setPadding(20,20,20,20)
                        if(json.getJSONObject(i).getString("statusString").toString()[j] == '1'){
                            checkbox[j].isChecked = true
                        }
                        dashboard_llayout.addView(checkbox[j])
                    }

                    //****Buttons****
                    buttonSave.visibility = View.GONE
                    buttonSave = Button(applicationContext)
                    buttonSave.text = "Save settings"
                    //buttonSave.layoutParams = LinearLayout.LayoutParams(500,200)
                    buttonSave.setPadding(50,50,50,50)
                    var params = LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.WRAP_CONTENT
                    )
                    params.setMargins(40, 50, 40, 10)
                    buttonSave.layoutParams = params
                    buttonSave.setOnClickListener {
                        var saveStatusString=""
                        Toast.makeText(applicationContext, "Saving user settings..", Toast.LENGTH_LONG).show()
                        saveStatusString+=adminUsername+","+adminPassword+","+usernameArray[i].toLowerCase()+","
                        for(j in 0 until(json.getJSONObject(0).getString("statusString").length) step 1){
                            if(checkbox[j].isChecked){
                                saveStatusString+="1"
                            }
                            else{
                                saveStatusString+="0"
                            }
                        }
                        var save = SaveStatusString()
                        var result = save.execute(saveStatusString)
                    }
                    dashboard_llayout.addView(buttonSave)

                    buttonLogs.visibility = View.GONE
                    buttonLogs = Button(applicationContext)
                    buttonLogs.text = "View Logs"

                    buttonLogs.setPadding(50,50,50,50)
                    params = LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.WRAP_CONTENT
                    )
                    params.setMargins(40, 20, 40, 10)
                    buttonLogs.layoutParams = params
                    buttonLogs.setOnClickListener {
                        var intent = Intent(applicationContext, LogActivity::class.java)
                        intent.putExtra("username", adminUsername)
                        intent.putExtra("password", adminPassword)
                        intent.putExtra("user", usernameArray[i].toLowerCase())
                        startActivity(intent)
                    }
                    dashboard_llayout.addView(buttonLogs)

                }catch (e:Exception){
                    Toast.makeText(applicationContext, e.toString(), Toast.LENGTH_LONG).show()
                }
            }
        }
        dashboard_llayout.addView(spinner)

        supportActionBar!!.setDisplayHomeAsUpEnabled(true)
        supportActionBar!!.title = "Dashboard"
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed()
        return true
    }

    inner class SaveStatusString : AsyncTask<String, Void, String>(){
        override fun doInBackground(vararg saveString: String?): String {
            var saveStatusString = Arrays.toString(saveString)
            var stringSplit = saveStatusString.toString().replace("[","")
            stringSplit = stringSplit.replace("]","")
            var stringArr = stringSplit.split(",")
            Log.d("saveString: ",stringArr.toString())
            Log.d("saveString: ",stringArr[2])
            var response = Jsoup.connect("https://webwebsec.localtunnel.me/login/phone/")
                .ignoreContentType(true)
                .data("username", stringArr[0])
                .data("password", stringArr[1])
                .data("user", stringArr[2])
                .data("loginType", "adminlogin")
                .data("device", "phone")
                .data("statusString", stringArr[3])
                .post()
            var bodyText = Jsoup.parse(response.html()).body().text()
            runOnUiThread {
                Toast.makeText(applicationContext, bodyText.capitalize(), Toast.LENGTH_LONG).show()
            }
            return bodyText
        }
    }
}
