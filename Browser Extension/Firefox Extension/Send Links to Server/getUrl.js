var lastDomain = ""
var extensions = ["jpg", "css", "png", "js", "woff", "gif", "svg", "ico"]
function sendToServer(requestDetails) {
    var url = requestDetails.url;
    var urlSplit = url.split("/");
    console.log(urlSplit);
    var lastElement = urlSplit[urlSplit.length-1];
    var lastElementSplit = lastElement.split(".");
    console.log("Last element: "+lastElementSplit);
    var skip=0;
    if(extensions.indexOf(lastElementSplit[lastElementSplit.length-1]) != -1 || url.length > 100)
    {
        skip = 1;
        console.log("*********Skipped************");
    }
    
    if(urlSplit[2].split(".")[1] == "google")
    {
        console.log("Letting google go");
        return requestDetails.url;
    }
    else if(urlSplit[2] != "127.0.0.1:8000" && lastDomain != urlSplit[2] && skip == 0)
    {
        browser.webRequest.onBeforeRequest.removeListener(
        sendToServer,
        );
        lastDomain = urlSplit[2];
        var redirectToUrl = {redirectUrl : "http://127.0.0.1:8000/runmodel?link="+requestDetails.url};
        //console.log("Sent: "+redirectToUrl)
        return redirectToUrl;
    }
    else
    {
        return requestDetails.url;
    }
}

browser.webRequest.onBeforeRequest.addListener(
    sendToServer,
    {urls: ["<all_urls>"]},
    ["blocking"]
  );

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


