{"filter":false,"title":"script.js","tooltip":"/static/script.js","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":23,"column":3},"action":"insert","lines":["var open = document.getElementById('hamburger');","var changeIcon = true;","","open.addEventListener(\"click\", function(){","","    var overlay = document.querySelector('.overlay');","    var nav = document.querySelector('nav');","    var icon = document.querySelector('.menu-toggle i');","","    overlay.classList.toggle(\"menu-open\");","    nav.classList.toggle(\"menu-open\");","","    if (changeIcon) {","        icon.classList.remove(\"fa-bars\");","        icon.classList.add(\"fa-times\");","","        changeIcon = false;","    }","    else {","        icon.classList.remove(\"fa-times\");","        icon.classList.add(\"fa-bars\");","        changeIcon = true;","    }","});"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":3},"action":"remove","lines":["var open = document.getElementById('hamburger');","var changeIcon = true;","","open.addEventListener(\"click\", function(){","","    var overlay = document.querySelector('.overlay');","    var nav = document.querySelector('nav');","    var icon = document.querySelector('.menu-toggle i');","","    overlay.classList.toggle(\"menu-open\");","    nav.classList.toggle(\"menu-open\");","","    if (changeIcon) {","        icon.classList.remove(\"fa-bars\");","        icon.classList.add(\"fa-times\");","","        changeIcon = false;","    }","    else {","        icon.classList.remove(\"fa-times\");","        icon.classList.add(\"fa-bars\");","        changeIcon = true;","    }","});"],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566319801476,"hash":"da39a3ee5e6b4b0d3255bfef95601890afd80709"}