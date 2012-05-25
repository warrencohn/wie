var map;

function getLatLngFromString(str) {
    var temp = str.split(',');
    var pos = new google.maps.LatLng(temp[0], temp[1]);
    return pos;
};

function initialize() {
    var myOptions = {
        center: new google.maps.LatLng(10.772308, 106.657812),
        zoom: 18,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map_canvas'),
            myOptions);
    //alert("X");

    drawAllMarker();
}

function setWindowSize() {
    var w = $(window).width();
    var h = $(window).height();
    var mw = w - 420;
    var mainh = h - 100;
    var mh = mainh - 24;
    var rh = mh - 40;

    
    $(".map").width(mw + 'px');
    $(".map").height(mh + 'px');
    $(".sidebar").height(mh + 'px');
    $(".resultBox").height(rh + 'px'); 
    $(".main").height(mainh + 'px');
    
    //$(".resultBox").height(mh + 'px');
}

function drawAllMarker() {
    var counter = 0;
    $('.result').each(function () {
        var latLng = $(this).find('.rLocation').html();
        counter++;
        var pos = getLatLngFromString(latLng);

        marker = new google.maps.Marker({
            position: pos,
            map: map,
            icon: "Styles/images/markers/number_" + counter + ".png"
        });


    });
}

$(document).ready(function () {
    setWindowSize();
    initialize();

    $(window).resize(setWindowSize);

    $("#MainContent_sName").click(function () {
        if ($(this).val() == "Nhập thông tin tìm kiếm..") {
            $(this).val('');
        }
    });

    $(".result").click(function () {
        $(".result").removeClass('active');
        $(this).addClass('active');

        var latLng = $(this).find('.rLocation').html();
        //alert(latLng);
        map.panTo(getLatLngFromString(latLng));
    });
});

//google.maps.event.addDomListener(window, 'load', initialize);