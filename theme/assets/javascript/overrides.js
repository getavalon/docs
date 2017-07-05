window.addEventListener("load", function () {

  var OSName = "Windows";
  if (window.navigator.userAgent.indexOf("Windows")   != -1) OSName = "cmd";
  if (window.navigator.userAgent.indexOf("Mac")  != -1) OSName = "bash";
  if (window.navigator.userAgent.indexOf("X11")  != -1) OSName = "bash";
  if (window.navigator.userAgent.indexOf("Linux")   != -1) OSName = "bash";

  // Per default, display tab most relevant to the current OS
  var defaultTab = document.getElementsByClassName("tab " + OSName);
  for (i = 0; i < defaultTab.length; i++){
    defaultTab[i].click();
    break;
  }

  var select = document.getElementById("version-selector");
  
  if (select != undefined) {
    console.log(document.location.href)
    select.selectedIndex = document.location.href.endsWith("1.0/") ? 1 : 2;

    function onSelectChanged() {
        document.location.href = "/" + select.value;
    }

    if (select.addEventListener) {
        select.addEventListener("change", onSelectChanged, false);
    }
    else {
        // !@#$ing IE support, of course
        select.attachEvent("onchange", onSelectChanged, false);
    }
  }
}, false );

function hasClass(element, cls) {
    return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
}

function setTab(event, tabName) {
    var i, tabcontent, tabs;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = hasClass(tabcontent[i], tabName) ? "block" : "none";
    }

    // Get all elements with class="tabs" and remove the class "active"
    tabs = document.getElementsByClassName("tab");
    for (i = 0; i < tabs.length; i++) {
        tabs[i].className = tabs[i].className.replace(" active", "");
        tabs[i].className += hasClass(tabs[i], tabName) ? " active" : ""
    }
}