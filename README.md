# Websec
*****************************************
Namaste, welcome to WebSec!

Format for adding changes:

Name of Contributor, Date Added, Changes Made
******************************************

Please start writinng from here

Aug 18 2019

Vaibhav:

Added: Firefox Browser extension

Working: Extension redirects user to "dummySite.html" whenever he trys to go to or attempt a 
search request using a search engine.

Changes in directory: Browser Extension/Firefox Extension/

******************************************

Aug 20, 2019

Anubhav:

Added: The GUI/FrontEnd Part for the project

Working: As of now, only working HTML/CSS site. Not Connected to Database. Once Django Server is setup(by Parth), database connection would be established. Parth, is also, supposed to edit the necessary changes in the website, keeping the basic structure same.

**********************************************

Aug 20, 2019

Vaibhav:

Added: Scraper + HTML Parser

Working: Scrapper uses selenium and Beautiful Soup is used for HTML Parsing. This script reads all the links in TrainSites.txt / TestSites.txt then performs scraping and parsing and then makes a folder for each site it scraps. 

Made folder contains following files: 

1. Raw Body Content 

2. Body Content without html / scripts / style elements

3. Links in body 

4. Scripts in html

5. Sites Link

**********************************************

Aug 25,2019

Anubhav

Added: Scraped Content of 20 Tech Blog Websites for Classification.
Numberwise,scraped content is less, but there is enough news within each column to particularly cover every aspect. Also, ignore tags like <n> or <t> as they would be removed during pre-processing.
  On may way to make final csv file to perform machine learning but before that need to scrap some other categories of blog to so that model is not overfitted.
  
  *********************************************
  
  Aug 26,2019
  
  Vaibhav
  
  Added:
  
  1. Model to classify game sites (XGBoost). [/Models/Gaming Sites/]
  
  2. Django server to handle captured links from websites and run models on them. [/Server/WebsecServer/]
  
  3. Dataset made from scraped gaming sites. [/Gaming Dataset/]
  
  4. Firefox browser extension to capture and send links to server. [/Browser Extension/Firefox Extension/Send Links to Server/]
  
  Improvement:
  
  1. HTMLParser now first uses requests to fetch HTML and switches to selenium if websites detect the first approach as bot. [/HTML Parser/]
  
  *********************************************

Aug 26, 2019

Milind
LV 0.01

Added scrapped data of movie sites alongwith its designated scrapper in folder 'Movie_site_scrapper'.
Extract/Clone into C drive for flawless compaitability.

Data addition :-
  1. Movie_site_scrapper/mv_db -> Contains scrapped text data from user interactive tags of movie sites
  2. Movie_site_scrapper/mv_db_keywords -> Contains processed token keywords extracted from 'mv_db' data
  3. Movie_site_scrapper/mvdb.txt -> Contains all active url to movie sites used by the code
  4. Movie_site_scrapper/mvdb_o.txt -> Contains all url to movie sites regardless of their accesibility , superset of mvdb.txt
  
Code addition :-
  1. Movie_site_scrapper/site_scrapper.py -> Scraps sites and keeps mvdb.txt error free. Uses 'requests' amd 'BS4'
  2. Movie_site_scrapper/tknz.py -> Processes and tokenizes data from mv_db folder 
  3. Movie_site_scrapper/link_copy.py -> Copies link from mvdb_o.txt to mvdb.txt to be reloaded
  
 (PS:- Manual link hunting is cumbersome , somebody should automate it)
 
   *********************************************
 Aug 28, 2019
 
 Milind
 LV 0.02
 
 Added inital prototype of Layer 1 , games and movie sites incorporated.
 Starting results are encouraging.
 
 To test:-
 1. Download Chrome
 2. Enter 'chrome://extensions' in address bar of browser
 3. Enable developer mode
 4. Click on load unpacked and select the folder 'chrome_extension'(after getting cloned from repo) from your filesystem.
 5. Start testing.
 
   ***********************************************
   September 1,2019
   
   
   Parth
   
   1)Scraped social media sites using BeautifulSoup and Resquests.
   2)Only text data related to the socialmedia website is scraped.
   3)All scraped data is stored in different files so that they can used for applying models.
   
***********************************************

Sep 1,2019

Vaibhav:

1. Added shopping sites dataset and trained model.

2. Major changes to extension's getUrl_v2 (V1 is stable).

3. Minor changes to HTMLParser.

***********************************************

Sep 1,2019

Anubhav:

1. Scraped webpges of Adult Websites, Bollywood Blogs.

2. A Corresponding Model using Tfidf approach and Logistic Regression was created.

3. The Model was deployed on to the flask server.

*****************************************

Sep 21,2019

Vaibhav:

1. Connected webpages for login and signup. (COOKIE based login - Login expires after 10 min of inactivity)

2. Connected database for login and signup funstionality. Use first name as username and last name as password (all in lowercase)

*****************************************

Sept 25,2019:

Anubhav:

1. Made a GUI Title Analyser for the Website. It scrapes the title of the web page for primary analysis.
2. A model based on this was prepared using Count Vectorizer and Tfidf Approach. On testing set, gave a good enough accuracy.

Models uploaded to folder Models/Tech Blog Models

**********************************************

Sept 30,2019

Vaibhav:

1. Improvements to Gaming and Shopping models. Switched Gaming model from XGBoost to Naive Bayes.

2. Improvements to server.

3. Merged Payment/Bank model. [/Compiled/Models/]

**********************************************

Sept 30,2019

Milind
LV 0.03

1. All 10 categories incorporated in Layer 1.

2. Chrome extension implemented.

3. Layer ready for model merge.

**********************************************

Oct 3,2019

Vaibhav:

1. Merged Gaming, Shopping, Movie, VideoStreaming, Banking/Payment, Tech, Entertainment and Adult models.

2. Integration testing successful.

3. Fixed bug which led to server crash.

4. Changed folder structure for better clarity

NOTE: Final working project can be found in [/compiled/] folder. 

To run clone the repo. Make sure django is installed. Change directory to WebsecServer [found in compiled].

Run in terminal:

`
python manage.py runserver
`

Load the browser extension and start surfing.

Change blocking categories in [/compiled/Models/HTMLParser.py] (Bottom of the function)

**********************************************

Oct 4, 2019

Vaibhav:

Design changes to login page.

**********************************************

Nov 1, 2019

Vaibhav:

1. Added active models database.

2. Added admin login functionality.

3. Added admin control functionality.

**********************************************

Nov 2, 2019

Vaibhav:

Completed implementation of Model control system. Admin can login and change the user settings 

and the settings will be instantly applied.

**********************************************

Nov 7, 2019

Vaibhav:

1. Implemented REST API

2. Added Android app


**********************************************

Nov 10, 2019

Vaibhav:

1. Android App: Admin: Change user settings functionality complete.

2. Server: Changes to allow admin to save new model settings sent by admin using android app.


**********************************************

Nov 12, 2019

Vaibhav:

1. Log database created and api created.

2. Fixed browser extension bugs.

**********************************************

Nov 13, 2019

Vaibhav:

1. Added "View history functionality" in android app.

2. Fixed android UI freeze issues.

**********************************************

Nov 17,2019

Anubhav:

Added the all new User Friendly Website Design and Control Panel.
It is located in the folder anubhav_website.

*************************************************

Nov 18,2019

Anubhav

Uploaded the flutter app. The App is fully functional with users being authenticated for firebase real time database. Logs can also be fetched but the script has to be added somewhere. Only downside is not the functional settings panel but that will be made as a dummy only to show evaluators. OK?

*************************************************

Nov 23,2019

Vaibhav

1. Completed load distribution functionality using socket programming. Place ModelHelper and Model_Helper_Server

   folders in another device and run p2p_server.py.

2. Small changes to browser extension to incorporate load distribution functionality.

*************************************************
