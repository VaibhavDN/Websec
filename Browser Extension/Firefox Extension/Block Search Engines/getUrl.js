var searchEngine = ["google", "bing", "dogpile", "yippy", "webopedia", "yahoo", "baidu", "ask", "wolframalpha", "yandex", "excite", "webcrawler", "search", "info", "startpage"];

function getDomain(requestDetails){
  var url = requestDetails.url;
  var urlSplit = url.split("/");
  console.log(requestDetails);
  console.log(urlSplit);
  var hostName = urlSplit[2];
  console.log(hostName);
  var hostNameSplit = hostName.split(".");
  if(hostNameSplit[0] == "www" || hostNameSplit[0] == "in") //For host names starting with www
  {
    var domainName = hostNameSplit[1];
  }
  else
  {
    var domainName = hostNameSplit[0];
  }
  
  console.log(domainName);
  return domainName;
}

function redirectToMySite(requestDetails) {
    //console.log("Redirecting: " + requestDetails.url);
    var domainName = getDomain(requestDetails);
    var redirectToUrl = {redirectUrl : "http://localhost/dummySite.html"};
    if(requestDetails.url != "http://localhost/dummySite.html" && searchEngine.indexOf(domainName) > -1)  //Returns -1 in domain is not in array
    {
      console.log(redirectToUrl);
      return redirectToUrl;
    }
    else
    {
      return requestDetails.url;
    }
    
}

browser.webRequest.onBeforeRequest.addListener(
    redirectToMySite,
    {urls: ["<all_urls>"]},
    ["blocking"]
  );