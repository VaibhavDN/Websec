package com.atootbal.websec

import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import org.jsoup.Connection
import java.util.*
import org.jsoup.Jsoup
import java.lang.Exception

class Login : AsyncTask<String,Void,String>(){
    override fun doInBackground(vararg input: String?): String {
        var stringInput = Arrays.toString(input)
        stringInput = stringInput.replace("[","")
        stringInput = stringInput.replace("]","")
        var splitString = stringInput.split(",")
        var username = splitString[0]
        var password = splitString[1]
        var re = ""
        try{
            var login = Jsoup.connect("https://webwebsec.serveo.net/login/phone/")
                .ignoreContentType(true)
                .data("loginType", "adminlogin")
                .data("username", username)
                .data("password", password)
                .post()
            var html = login.html()
            var parsedHtml = Jsoup.parse(html).body().text()
            re = parsedHtml
        }
        catch(e:Exception){
            return e.toString()
        }

        return re
    }
}

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
            var x = asyncTask.execute(combinedString).get()
            Toast.makeText(this, x, Toast.LENGTH_LONG).show()
            submitBtn.text = x
        }
    }
}
