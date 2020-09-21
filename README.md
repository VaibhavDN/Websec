## Websec - A website classification system

****

<img width="100%" src="https://github.com/VaibhavDN/Websec/blob/master/Flow/WebSecWorking.jpg">

****

### How does it work?
1. User login to their account and start surfing
2. User clicks on the link
3. Browser extension intercepts the request and redirects it to the websec server
4. Server receives the link and runs the web scraper on the website
5. Scraped content is tokenized and cleaned
6. Frequencies of words are calculated and CSV file is formed
7. Users settings are retrieved to identify the blocked categories
8. Machine learning models classify the website
9. If website is classified under the blocked category, a blocked message is displayed to the user
10. Else the original requested website is opened

****

### Technologies used
1. Django server: Python
2. Android app: Java
3. Machine learning models: Decision Tree, XGBoost, Naive bayes
4. Selenium WebDriver: Python bindings
5. Login/Signup website: HTML, CSS
6. Browser extensions: Javascript
