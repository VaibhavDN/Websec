package com.atootbal.websec

import android.graphics.Color
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Layout
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.ProgressBar
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.widget.LinearLayoutCompat
import kotlinx.android.synthetic.main.activity_log.*
import org.json.JSONArray
import org.json.JSONObject
import org.jsoup.Jsoup
import java.lang.Exception
import java.util.*

class LogActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_log)
        var getExtras = intent.extras
        var username = getExtras!!.getString("username")
        var password = getExtras.getString("password")
        var user = getExtras.getString("user")

        val getLogs = GetLogs()
        var output = getLogs.execute(username+","+password+","+user)
        Toast.makeText(this, "Fetching history..", Toast.LENGTH_LONG).show()

        supportActionBar!!.setDisplayHomeAsUpEnabled(true)
        supportActionBar!!.title = "User history"
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed()
        return true
    }

    inner class GetLogs : AsyncTask<String, Int, String>(){
        override fun doInBackground(vararg params: String?): String {
            var paramString = Arrays.toString(params)

            runOnUiThread {
                val progressBar = findViewById<ProgressBar>(R.id.log_progressBar)
                progressBar.visibility = View.VISIBLE
            }

            paramString = paramString.replace("[","")
            paramString = paramString.replace("]","")
            var receivedData = paramString.split(",")
            var connect = Jsoup.connect("https://webwebsec.localtunnel.me/login/logs/")
                .ignoreContentType(true)
                .data("username", receivedData[0])
                .data("password", receivedData[1])
                .post()
            var jsonString = Jsoup.parse(connect.html()).body().text()
            var json = JSONArray(jsonString)
            var history = ""

            try {
                for (i in 0..json.length()-1 step 1) {
                    if (json.getJSONObject(i).getString("username") == receivedData[2]) {
                        history += json.getJSONObject(i).getString("site") + ": "
                        history += json.getJSONObject(i).getString("status").capitalize() + "\n\n"
                    }
                }
            }catch (e:Exception){
                history = "Error"
            }
            runOnUiThread {
                log_progressBar.visibility = View.GONE
                var param = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT)
                param.setMargins(40, 10, 40, 10)
                val heading = TextView(applicationContext)
                heading.textSize = 22f
                heading.layoutParams = param
                heading.setTextColor(Color.rgb(102,0,153))
                heading.text = "History for user: "+receivedData[2].capitalize()+"\n"
                log_llayout.addView(heading)

                val textView = TextView(applicationContext)
                textView.layoutParams = param
                textView.text = history
                textView.textSize = 17f
                log_llayout.addView(textView)
            }

            return history
        }

    }
}
