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

