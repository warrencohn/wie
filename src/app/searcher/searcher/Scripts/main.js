var map;
var infoWindow;

function getLatLngFromString(str) {
    var temp = str.split(',');
    var pos = new google.maps.LatLng(temp[0], temp[1]);
    return pos;
};

function initialize() {
    var myOptions = {
        center: new google.maps.LatLng(10.772308, 106.657812),
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map_canvas'),
            myOptions);
    //alert("X");
    
    infowindow = new google.maps.InfoWindow();

    var pos = drawAllMarker();

    map.setCenter(pos);
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

    $(".container").height(mainh + 'px');
    //$(".container").attr('left', '');
    //$(".resultBox").height(mh + 'px');
}

function drawAllMarker() {
    var counter = 0;
    var pos;

    var markers = [];
    $('.result').each(function () {
        var latLng = $(this).find('.rLocation').html();
        counter++;
        pos = getLatLngFromString(latLng);

        marker = new google.maps.Marker({
            position: pos,
            map: map,
            icon: "Styles/images/markers/number_" + counter + ".png"
        });

        markers.push(marker);
    });

    console.log(markers);

    for (var i = 0; i < markers.length; i++) {
        for (var j = 0; j < i; j++) {
            if (markers[i].getPosition().equals(markers[j].getPosition())) {
                var lat = markers[i].getPosition().lat() + 0.0003;
                var lng = markers[i].getPosition().lng() + 0.0003;
                markers[i].setPosition(new google.maps.LatLng(lat,lng));
            }
        }
    }

    return pos;
}
var isClosed = false;

$(document).ready(function () {

    //    alert('123');
    setWindowSize();
    initialize();

    $(window).resize(setWindowSize);

    $("#txtsName").click(function () {
        if ($(this).val() == "Nhập thông tin tìm kiếm..") {
            $(this).val('');
        }
    });

    $(".result").click(function () {

        $(".result").removeClass('active');
        $(this).addClass('active');

        var $span = $('span');
        var latLng = $(this).find('.rLocation').html();
        //alert(latLng);
        var pos = getLatLngFromString(latLng);

        // Replace our Info Window's content and position

        //        var $info1 = $;
        var iw = $(this).find('.infowindow1');

        console.log(iw);

        iw.find('rName').html($(this).find('rName'));
        iw.find('rAddr').html($(this).find('rAddr'));
        iw.find('rPhone').html($(this).find('rPhone'));
        iw.find('rEmail').html($(this).find('rEmail'));
        iw.find('rFax').html($(this).find('rFax'));
        iw.find('rWebsite').html($(this).find('rWebsite'));
        iw.find('rBiz').html($(this).find('rBiz'));

        console.log(iw);

        infowindow.setContent(iw.html());
        infowindow.setPosition(pos);

        infowindow.open(map);

        map.panTo(pos);


    });

    $(".toolbox").click(function () {
        if (!isClosed) {
            $(".sidebar").hide();
            $(this).css('left', '20px');
            var w = $(".map").width() + 380;
            $(".map").width(w + 'px');
            isClosed = true;
            $(this).html('Hiện sidebar');
        }
        else {
            $(".sidebar").show();
            $(this).css('left', '390px');
            var w = $(".map").width() - 380;
            $(".map").width(w + 'px');
            isClosed = false;
            $(this).html('Xem toàn màn hình');
        }
    });

    $(".loginDisplay a img").hover(function () {
        $(this).attr('src', 'Styles/images/ads_hover.jpg');
    }, function () {
        $(this).attr('src', 'Styles/images/ads.jpg');
    });
});

//google.maps.event.addDomListener(window, 'load', initialize);