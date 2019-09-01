browser.runtime.onMessage.addListener(receivedUrl);
var receivedUrl = ""
var receivedUrlLast = "lasturl";
function receivedUrl(message) {
  console.log("Received: "+message.url);
  receivedUrl = message.url;
  console.log ("Listener Started..");
  browser.webRequest.onBeforeRequest.addListener(
        sendToServer,
        {urls: ["<all_urls>"]},
        ["blocking"]
    );
}

var lastDomain = "";
var extensions = ["jpg", "css", "png", "js", "woff", "gif", "svg", "ico"];
function sendToServer(requestDetails) {
    var url = requestDetails.url;
    console.log("Intercepted: "+url);
    if(receivedUrl == receivedUrlLast)
    {
        console.log("receivedUrl==receivedUrlLast probably same site: "+receivedUrl);
        return url;
    }
    else
    {
        console.log("Not same analyzing..");
        receivedUrlLast = receivedUrl;
        url = receivedUrl;
    }
    var urlSplit = url.split("/");
    console.log(urlSplit);
    var lastElement = urlSplit[urlSplit.length-1];
    var lastElementSplit = lastElement.split(".");
    console.log("Last element: "+lastElementSplit);
    var skip=0;
    if(extensions.indexOf(lastElementSplit[lastElementSplit.length-1]) != -1)
    {
        skip = 1;
        console.log("*********Skipped************");
    }
    console.log("lastDomain: "+lastDomain);
    if(urlSplit[2].split(".")[1] == "google")
    {
        console.log("Letting google go");
        return receivedUrl;
    }
    else if(urlSplit[2] != "127.0.0.1:8000" && lastDomain != urlSplit[2] && skip == 0)
    {
        console.log("Stopping Listener..");
        browser.webRequest.onBeforeRequest.removeListener(
        sendToServer,
        );
        lastDomain = urlSplit[2];
        var redirectToUrl = {redirectUrl : "http://127.0.0.1:8000/runmodel?link="+url};
        console.log("Sent: "+receivedUrl);
        return redirectToUrl;
    }
    else
    {
        return url;
    }
}

browser.webRequest.onBeforeRequest.addListener(
    sendToServer,
    {urls: ["<all_urls>"]},
    ["blocking"]
  );
/*
browser.webRequest.onCompleted.addListener(
    myFunction,
    {urls: ["<all_urls>"]},
  );
function myFunction(x) {
  console.log ("Request completed");
  browser.webRequest.onBeforeRequest.addListener(
        sendToServer,
        {urls: ["<all_urls>"]},
        ["blocking"]
    );
}
*/
