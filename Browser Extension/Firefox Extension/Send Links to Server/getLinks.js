//console.log(window.location.href);
window.addEventListener("click", clickFunction);

function clickFunction(e) {
    /*if (e.target.tagName.toLowerCase() != "a") {
        return;
    }*/
    browser.runtime.sendMessage({"url": e.target.href});
}
