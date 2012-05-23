function initialize() {
    var myOptions = {
        center: new google.maps.LatLng(-34.397, 150.644),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById('map_canvas'),
            myOptions);
    //alert("X");
}

function setWindowSize() {
    var w = $(window).width();
    var h = $(window).height();
    var mw = w - 420;
    var mainh = h - 110;
    var mh = h - 120;
    var rh = h - 120;
    
    $(".map").width(mw + 'px');
    $(".map").height(mh + 'px');
    $(".main").height(mainh + 'px');
    //$(".resultBox").height(mh + 'px');
}
$(document).ready(function () {
    setWindowSize();
    initialize();

    $(window).resize(setWindowSize);
});

//google.maps.event.addDomListener(window, 'load', initialize);