window.addEventListener("load", function () {
  var select = document.getElementById("version-selector");
  
  if (select != undefined) {
    console.log(document.location.href)
    select.selectedIndex = document.location.href.endsWith("1.0/") ? 1 : 2;

    function onSelectChanged() {
        document.location.href = "/docs/" + select.value;
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
