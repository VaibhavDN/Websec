import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:async/async.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/services.dart';

Map zz;

void main() => runApp(MyApp());
var _data = Firestore.instance;
var _newdata = FirebaseDatabase.instance.reference();

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  @override
  _LoginPage createState() => _LoginPage();
}

class _LoginPage extends State<LoginPage> {
  TextEditingController ucontroller = new TextEditingController();
  TextEditingController pcontroller = new TextEditingController();
  var _auth = FirebaseAuth.instance;
  var _data = Firestore.instance;
  void getdata() async {
    final ll = await _data.collection('links').getDocuments();
    for (var i in ll.documents) {
      i.data;
    }
  }

  void clickme() {}
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            'Websec',
            style: TextStyle(fontSize: 28, color: Colors.white),
          ),
          backgroundColor: Colors.grey[600],
          centerTitle: true,
        ),
        body: SafeArea(
          child: Column(
            children: <Widget>[
              SizedBox(
                height: 20,
              ),
              Center(
                child: Container(
                  child: CircleAvatar(
                    backgroundImage: AssetImage('images/admin.jpeg'),
                    radius: 90,
                  ),
                ),
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                'Admin Login',
                style: TextStyle(
                    fontSize: 28,
                    color: Colors.grey[400],
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 10,
              ),
              TextField(
                controller: ucontroller,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 24, color: Colors.red[500]),
                keyboardType: TextInputType.emailAddress,
                decoration: InputDecoration(
                    hintText: 'Username',
                    hintStyle:
                        TextStyle(color: Colors.blue[600], fontSize: 20)),
              ),
              SizedBox(
                height: 10,
              ),
              TextField(
                controller: pcontroller,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 24, color: Colors.red[500]),
                obscureText: true,
                keyboardType: TextInputType.text,
                decoration: InputDecoration(
                    hintText: 'Password',
                    hintStyle:
                        TextStyle(color: Colors.blue[600], fontSize: 20)),
              ),
              SizedBox(
                height: 10,
              ),
              Center(
                child: Container(
                  width: 200,
                  child: FlatButton(
                    onPressed: () async {
                      String a;
                      String b;
                      a = ucontroller.text;
                      b = pcontroller.text;
                      print(a);
                      print(b);
                      final _user = await _auth.signInWithEmailAndPassword(
                          email: a, password: b);
                      try {
                        if (_user != null) {
                          final _u = await _auth.currentUser();
                          return Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => SecondPage()),
                          );
                        }
                      } on PlatformException catch (e) {
                        String a = e.toString();
                        print(a);
                      }
                    },
                    color: Colors.grey[400],
                    child: Text(
                      'SUBMIT',
                      style: TextStyle(fontSize: 22, color: Colors.black),
                    ),
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}

class SecondPage extends StatefulWidget {
  @override
  __SecondpageState createState() => __SecondpageState();
}

class __SecondpageState extends State<SecondPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Welcome Admin',
          style: TextStyle(color: Colors.white, fontSize: 26),
        ),
        backgroundColor: Colors.grey,
        centerTitle: true,
      ),
      body: SafeArea(
        child: Column(
          children: <Widget>[
            SizedBox(
              height: 80,
            ),
            Container(
              width: double.infinity,
              height: 200,
              padding: EdgeInsets.fromLTRB(15, 15, 0, 0),
              color: Colors.green[600],
              child: FlatButton(
                onPressed: () {},
                child: Text(
                  'Change your Settings',
                  style: TextStyle(fontSize: 28, color: Colors.white),
                ),
              ),
            ),
            SizedBox(
              height: 30,
            ),
            Container(
              width: double.infinity,
              height: 200,
              padding: EdgeInsets.fromLTRB(15, 15, 0, 0),
              color: Colors.red[600],
              child: FlatButton(
                onPressed: () async {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => Thirdpage()));

                  _newdata.once().then((DataSnapshot snapshot) {
                    zz = snapshot.value;

                    print(zz['links']);
                  });
                },
                child: Text(
                  'View Log History',
                  style: TextStyle(fontSize: 28, color: Colors.white),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

//child: Text(
//'Change your Settings',
//style: TextStyle(fontSize: 32, color: Colors.white),
//textAlign: TextAlign.center,
//),
class Thirdpage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            'Websec',
            style: TextStyle(fontSize: 28, color: Colors.white),
          ),
          backgroundColor: Colors.grey,
        ),
        body: SafeArea(
          child: Column(
            children: <Widget>[
              Center(
                child: Image(
                  image: AssetImage('images/sad.png'),
                  height: 50,
                ),
              ),
              Text(
                '${zz["links"][1]['link']}',
                style: TextStyle(fontSize: 26, color: Colors.orange),
              ),
              Text(
                '${zz["links"][1]['result']}',
                style: TextStyle(fontSize: 26, color: Colors.red),
              ),
              Text(
                '${zz["links"][2]['link']}',
                style: TextStyle(fontSize: 26, color: Colors.orange),
              ),
              Text(
                '${zz["links"][2]['result']}',
                style: TextStyle(fontSize: 26, color: Colors.red),
              ),
              Text(
                '${zz["links"][3]['link']}',
                style: TextStyle(fontSize: 26, color: Colors.orange),
              ),
              Text(
                '${zz["links"][3]['result']}',
                style: TextStyle(fontSize: 26, color: Colors.red),
              ),
              Text(
                '${zz["links"][4]['link']}',
                style: TextStyle(fontSize: 26, color: Colors.orange),
              ),
              Text(
                '${zz["links"][4]['result']}',
                style: TextStyle(fontSize: 26, color: Colors.red),
              ),
              Text(
                '${zz["links"][5]['link']}',
                style: TextStyle(fontSize: 26, color: Colors.orange),
              ),
              Text(
                '${zz["links"][5]['result']}',
                style: TextStyle(fontSize: 26, color: Colors.red),
              ),
              Text(
                '${zz["links"][6]['link']}',
                style: TextStyle(fontSize: 26, color: Colors.orange),
              ),
              Text(
                '${zz["links"][6]['result']}',
                style: TextStyle(fontSize: 26, color: Colors.red),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
