package com.atootbal.websec

import android.content.Intent
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import org.json.JSONArray
import org.json.JSONObject
import java.util.*
import org.jsoup.Jsoup
import java.lang.Exception
import androidx.core.app.ComponentActivity.ExtraData
import androidx.core.content.ContextCompat.getSystemService
import android.icu.lang.UCharacter.GraphemeClusterBreak.T
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val submitBtn = findViewById<Button>(R.id.login_button_submit)
        val usernameEditText = findViewById<EditText>(R.id.login_editText_username)
        val passwordEditText = findViewById<EditText>(R.id.login_editText_password)
        submitBtn.setOnClickListener {
            val username = usernameEditText.text
            val password = passwordEditText.text
            val combinedString = username.toString()+","+password.toString()
            Toast.makeText(this,"Logging in", Toast.LENGTH_LONG).show()
            var asyncTask = Login()
            var jsonString = asyncTask.execute(combinedString).get()
            if(jsonString != "failed")
            {
                var json = JSONArray(jsonString)
                var intent = Intent(this, Dashboard::class.java)
                intent.putExtra("json", jsonString)
                intent.putExtra( "username", username.toString())
                intent.putExtra( "password", password.toString())
                startActivity(intent)

            }
            else{
                val loginButton = findViewById<Button>(R.id.login_button_submit)
                loginButton.text = "Incorrect username or password"
                Toast.makeText(this,"Login failed", Toast.LENGTH_LONG).show()
                progressBar.visibility = View.GONE
            }
        }
    }
    inner class Login : AsyncTask<String,Void,String>() {
        override fun doInBackground(vararg input: String?): String {
            var re = ""
            try {
                var stringInput = Arrays.toString(input)
                stringInput = stringInput.replace("[", "")
                stringInput = stringInput.replace("]", "")
                var splitString = stringInput.split(",")
                var username = splitString[0]
                var password = splitString[1]

                var login = Jsoup.connect("https://webwebsec.localtunnel.me/login/phone/")
                    .ignoreContentType(true)
                    .data("loginType", "adminlogin")
                    .data("username", username)
                    .data("password", password)
                    .post()
                var html = login.html()
                var parsedHtml = Jsoup.parse(html).body().text()
                re = parsedHtml
            } catch (e: Exception) {
                return "failed"
            }
            return re
        }

        override fun onPreExecute() {
            super.onPreExecute()
            progressBar.visibility = View.VISIBLE
        }

        override fun onProgressUpdate(vararg values: Void?) {
            super.onProgressUpdate(*values)
        }

        override fun onPostExecute(result: String?) {
            super.onPostExecute(result)
            //progressBar.visibility = View.GONE
        }
    }
}
