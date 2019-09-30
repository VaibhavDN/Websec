chrome.webRequest.onBeforeRequest.addListener(
  function (details) {
    /* var element = document.createElement('a')
    /* element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(details.url))
    element.setAttribute('download', 'url.txt')

    element.style.display = 'none'
    document.body.appendChild(element)

    element.click()

    document.body.removeChild(element) */

    /* code for category selection
    goes
    in
    here */

    var mode = [0,1,2,3,4,5,6,7,8]          // mode is array returned by category selection 0-movies, 1-games, 2-adult, 3-stream, 4-sports, 5-paymenr, 6-shopping, 7-news, 8-travel, 9-edu blog
    var txt = ''
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
      if (xmlhttp.status === 200 && xmlhttp.readyState === 4) {
        txt = xmlhttp.responseText
      }
    }
    console.log(details.url)
    if (details.url.length < 120 && !/api|css|.jpg|.js|google|.svg|.wof|.gif|no-rj-mo|.png|icon/.test(details.url)) {
      xmlhttp.open("GET", details.url, false);
      xmlhttp.send()
    }

    var el = document.createElement( 'html' );
    el.innerHTML = txt

    var zt = el.getElementsByTagName( 'title' );      // title tag extracted
    var at = el.getElementsByTagName( 'a' );          // a tag extracted
    var bt = el.getElementsByTagName('button')        // button tag extracted
    console.log(at)
    console.log(bt)


    var tx,ax,bx                                      // tx is title text , ax is anchor text, bx is button text

      /***************************************************************************************************************************************************************** movies*/
    if( mode.indexOf(0) !== -1) {

      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/movie|movies/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/download|watch|brrip|1080p|dubbed/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/download|watch|brrip|1080p|dubbed/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                             // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/movie|hollywood|bollywood|movies/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/movie|hollywood|bollywood|movies/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
    /********************************************************************************************************************************************************************* games*/
    if( mode.indexOf(1) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/game|games/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/download|play|platformer|shooter|simulation|strategy|torrent|utorrent|arcade|cheats/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/download|play|platformer|shooter|simulation|strategy|torrent|utorrent|arcade|cheats/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/download|play|platformer|shooter|simulation|strategy|torrent|utorrent|arcade|cheats/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/download|play|platformer|shooter|simulation|strategy|torrent|utorrent|arcade|cheats/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
      
    }
/******************************************************************************************************************************************************** adult*/
    if( mode.indexOf(2) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/porn|adult|nude|naked|booty/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/download|hd|ass|milf|boobs|hardcore|arab|mallu|pussy|bbc|cum/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/download|hd|ass|milf|boobs|hardcore|arab|mallu|pussy|bbc|cum/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/porn|adult|hd|ass|milf|boobs|hardcore|arab|mallu|pussy|bbc|cum/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/porn|adult|hd|ass|milf|boobs|hardcore|arab|mallu|pussy|bbc|cum/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
  /************************************************************************************************************************************************************************************* stream*/
    if( mode.indexOf(3) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/video|streaming|watch|shows|movie|youtube/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/1080p|hd|openload|trial|prime|720p|bollywood|hollywood|youtube/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/1080p|hd|openload|trial|prime|720p|bollywood|hollywood|youtube/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/1080p|hd|openload|trial|prime|720p|bollywood|hollywood|stream|originals/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/1080p|hd|openload|trial|prime|720p|bollywood|hollywood|stream|originals/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
/**************************************************************************************************************************************************************** sports*/
    if( mode.indexOf(4) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/sport|match|lose|loss|win|draw|play/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/cricket|football|gp|prix|hockey|kabaddi|olympics|tennis|badminton|wrestling|boxing|golf|wimbledon/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/cricket|football|gp|prix|hockey|kabaddi|olympics|tennis|badminton|wrestling|boxing|golf|wimbledon/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/cricket|football|gp|prix|hockey|kabaddi|olympics|tennis|badminton|wrestling|boxing|golf|wimbledon|medal|sport|match|win|loss/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/cricket|football|gp|prix|hockey|kabaddi|olympics|tennis|badminton|wrestling|boxing|golf|wimbledon|medal|sport|match|win|loss/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
  /************************************************************************************************************************************************************** payment*/
    if( mode.indexOf(5) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/online payment|payment|paypal|payment processing|make payments|accept payments/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/service|fraud|protection|checkout|solutions|resources|commerece|paypal|visa|mastercard/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/service|fraud|protection|checkout|solutions|resources|commerece|paypal|visa|mastercard/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/service|fraud|protection|checkout|solutions|resources|commerece|paypal|visa|mastercard|cart/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/service|fraud|protection|checkout|solutions|resources|commerece|paypal|visa|mastercard|cart/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
/*************************************************************************************************************************************************************************** shopping*/
    if( mode.indexOf(6) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/shopping|menswear|% off|accessories/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/cart|signup|offers|exchange|prime|account|bollywood|deals|sale/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/cart|signup|offers|exchange|prime|account|bollywood|deals|sale/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/cart|signup|offers|exchange|prime|account|bollywood|deals|sale|shopping|menswear|% off|accessories/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/cart|signup|offers|exchange|prime|account|bollywood|deals|sale|shopping|menswear|% off|accessories/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
  /********************************************************************************************************************************************************* news*/
    if( mode.indexOf(7) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/news|headlines|breaking|times of|world news/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/world|sport|culture|latest|breaking|business|politics|economy|video/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/world|sport|culture|latest|breaking|business|politics|economy|video/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/world|sport|culture|latest|breaking|business|politics|economy|video|news|headlines|breaking|times of|world news/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/world|sport|culture|latest|breaking|business|politics|economy|video|news|headlines|breaking|times of|world news/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
/********************************************************************************************************************************************************************* travel*/
    if( mode.indexOf(8) !== -1) {
      tx = zt[0].outerText.toLowerCase()
      console.log(tx)
      if (/booking|hotel|flight|train|bus|vacation|trip/.test(tx)){

        for(i = 0;i < at.length; i++) {
          ax = at[i].innerText.toLowerCase()

          console.log(ax)
          if(/destinations|domestic|international|tourist|package|flight|train|irctc|holiday/.test(ax)) {
            return {cancel:true}
          }
        }

        for(i = 0;i < bt.length; i++) {
          bx = bt[i].innerText.toLowerCase()
  
          console.log(bx)
          if(/destinations|domestic|international|tourist|package|flight|train|irctc|holiday/.test(bx)) {
            return {cancel:true}
          }
         }

        return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
        
        }
        else {

          for(i = 0;i < at.length; i++) {
            ax = at[i].innerText.toLowerCase()
  
            if(/destinations|domestic|international|tourist|package|flight|train|irctc|holiday|booking|hotel|flight|train|bus|vacation|trip/.test(ax)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
  
          for(i = 0;i < bt.length; i++) {
            bx = bt[i].innerText.toLowerCase()
    
            if(/destinations|domestic|international|tourist|package|flight|train|irctc|holiday|booking|hotel|flight|train|bus|vacation|trip/.test(bx)) {
              return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
            }
          }
          
        }
    }
/******************************************************************************************************************************************************************** edu blog*/
    if( mode.indexOf(9) !== -1) {
      return {redirectUrl:"https://www.google.com"}                          // replace with server request to run model and add conditional to block request if site is flagged red by model
    }

    /* return { cancel: details.url.indexOf('://www.google.com/') !== -1 } */
  },
  { urls: ['<all_urls>'] },
  ['blocking'])
