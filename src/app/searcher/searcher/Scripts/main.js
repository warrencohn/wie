var map;
var infoWindow;
var markers = [];
function getLatLngFromString(str) {
    var temp = str.split(',');
    var x = Number(temp[0]);
    var y = Number(temp[1]);
    //console.log("x = " + x + ", y = " + y);
    var pos = new google.maps.LatLng(x, y);
    return pos;
};

function getMarkerByPos(pos) {
    for (i = 0; i < markers.length; i++) {
        if (markers[i].getPosition().equals(pos)) {
            return i;
        }
    }
    return -1;
}

function initialize() {
    var myOptions = {
        center: new google.maps.LatLng(10.772308, 106.657812),
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map_canvas'),
            myOptions);
    //alert("X");
    google.maps.event.trigger(map, 'resize');

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

    //console.log(markers);

    for (var i = 0; i < markers.length; i++) {
        for (var j = 0; j < i; j++) {
            if (markers[i].getPosition().equals(markers[j].getPosition())) {
                var lat = markers[i].getPosition().lat() + 0.0001; //0.00035
                var lng = markers[i].getPosition().lng() + 0.0001;
                markers[i].setPosition(new google.maps.LatLng(lat, lng));
                markers[i].setZIndex(1);
                console.log("changed i = " + i + " same j = " + j);
            }
        }
    }

    return pos;
}
var isClosed = false;


function resultLoad() {
    var returnStr = document.getElementById("MainContent_lblTest").innerHTML;
    var availableTags = returnStr.split('|');
    //alert(availableTags);

    function split(val) {
        return val.split(/,*\s+/);
    }
    function extractLast(term) {
        return split(term).pop();
    }
    $("#MainContent_txtsName")
    // don't navigate away from the field on tab when selecting an item
			.bind("keydown", function (event) {
			    if (event.keyCode === $.ui.keyCode.TAB &&
						$(this).data("autocomplete").menu.active) {
			        event.preventDefault();
			    }
			})
			.autocomplete({
			    minLength: 2,
			    source: function (request, response) {
			        // delegate back to autocomplete, but extract the last term
			        response($.ui.autocomplete.filter(
						availableTags, extractLast(request.term)));
			    },
			    focus: function () {
			        // prevent value inserted on focus
			        return false;
			    },
			    select: function (event, ui) {
			        var terms = split(this.value);
			        // remove the current input
			        terms.pop();
			        // add the selected item
			        terms.push(ui.item.value);
			        // add placeholder to get the comma-and-space at the end
			        terms.push("");
			        this.value = terms.join(", ");
			        return false;
			    }
			});

    setWindowSize();
    initialize();
    $(window).resize(setWindowSize);

    $("#MainContent_txtsName").click(function () {
        if ($(this).val() == "Nhập thông tin tìm kiếm..") {
            $(this).val('');
        }
    });

    $(".result").click(function () {
        //console.log('result clicked');
        $(".result").removeClass('active');
        $(this).addClass('active');

        var $span = $('span');
        var latLng = $(this).find('.rLocation').html();
        //alert(latLng);
        var pos = getLatLngFromString(latLng);

        // Replace our Info Window's content and position

        //        var $info1 = $;
        var iw = $(this).find('.infowindow1');

        //console.log(iw);
        /*
        var name = $(this).find('rName');
        iw.find('rName').html(name);
        iw.find('rAddr').html($(this).find('rAddr'));
        iw.find('rPhone').html($(this).find('rPhone'));
        iw.find('rEmail').html($(this).find('rEmail'));
        iw.find('rFax').html($(this).find('rFax'));
        iw.find('rWebsite').html($(this).find('rWebsite'));
        iw.find('rBiz').html($(this).find('rBiz'));
        */
        //console.log(iw);

        infowindow.setContent(iw.html());
        infowindow.setPosition(pos);

        for (i = 0; i < markers.length; i++)
            markers[i].setZIndex(1);

        //var i = getMarkerByPos(pos);
        var index = $(this).find('.rName:first').html().split(".")[0];

        console.log(index);

        markers[index-1].setZIndex(100);

        infowindow.open(map);

        map.panTo(pos);


    });

    $(".toolbox").click(function () {
        //console.log("toolbox clicked " + isClosed);
        var cent = map.getCenter();
        if (!isClosed) {
            $(".sidebar").hide();
            $(this).css('left', '20px');
            var w = $(".map").width() + 390;
            $(".map").width(w + 'px');
            isClosed = true;
            $(this).html('Hiện sidebar');
        }
        else {
            $(".sidebar").show();
            $(this).css('left', '390px');
            var w = $(".map").width() - 390;
            $(".map").width(w + 'px');
            isClosed = false;
            $(this).html('Xem toàn màn hình');
        }
        google.maps.event.trigger(map, "resize");
        map.setCenter(cent);
    });

    $(".loginDisplay a img").hover(function () {
        $(this).attr('src', 'Styles/images/ads_hover.jpg');
    }, function () {
        $(this).attr('src', 'Styles/images/ads.jpg');
    });
}

$(document).ready(function () {
    resultLoad();
    (function () {
        // remove layerX and layerY
        var all = $.event.props,
        len = all.length,
        res = [];
        while (len--) {
            var el = all[len];
            if (el != 'layerX' && el != 'layerY') res.push(el);
        }
        $.event.props = res;
    } ());


});

//google.maps.event.addDomListener(window, 'load', initialize);
//Sys.WebForms.PageRequestManager.getInstance().add_endRequest(resultLoad)