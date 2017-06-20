window.addEventListener('load', function () {
  var select = document.getElementById('version-selector');
  
  if (select == undefined) {
    document.location.href = "/2.0";
  } else {
    console.log(document.location.href)
    select.selectedIndex = document.location.href.endsWith("1.0/") ? 1 : 2;

    function onSelectChanged() {
        document.location.href = "/" + select.value;
    }

    if (select.addEventListener) {
        select.addEventListener('change', onSelectChanged, false);
    }
    else {
        // !@#$ing IE support, of course
        select.attachEvent('onchange', onSelectChanged, false);
    }
    
  }
}, false );
