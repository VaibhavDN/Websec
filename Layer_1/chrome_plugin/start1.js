chrome.webRequest.onBeforeRequest.addListener(
  function (details) {
    /* var element = document.createElement('a')
    /* element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(details.url))
    element.setAttribute('download', 'url.txt')

    element.style.display = 'none'
    document.body.appendChild(element)

    element.click()

    document.body.removeChild(element) */
    var txt = ''
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
      if (xmlhttp.status === 200 && xmlhttp.readyState === 4) {
        txt = xmlhttp.responseText
      }
    }
    console.log(details.url)
    if (details.url.length < 100 && !/api|css|.jpg|.js|google|.svg|.wof|.gif|no-rj-mo|.png|icon/.test(details.url)) {
      xmlhttp.open("GET", details.url, false);
      xmlhttp.send()
    }
    
    console.log(txt)
    if (/game|games/.test(txt)) {
      return { cancel: /download|play/.test(txt)}
    }
    console.log(txt)
    if (/movie|movies/.test(txt)) {
      return { cancel: /download|watch/.test(txt)}
    }
    /* return { cancel: details.url.indexOf('://www.google.com/') !== -1 } */
  },
  { urls: ['<all_urls>'] },
  ['blocking'])
