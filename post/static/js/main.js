var mapContainer = document.getElementById('map'),
    mapOption = {
        center: new kakao.maps.LatLng(36.819516, 127.156586),
        level: 3
    };

var map = new kakao.maps.Map(mapContainer, mapOption);

var positions = [
    {
        content: '<div>신세계백화점 아라리오점</div>',
        latlng: new kakao.maps.LatLng(36.819435, 127.156568)
    },
    {
        content: '<div>올리브영 천안점</div>',
        latlng: new kakao.maps.LatLng(36.819246, 127.157727)
    },
    {
        content: '<div>복자여자고등학교</div>',
        latlng: new kakao.maps.LatLng(36.815699, 127.151622)
    }
];

for (var i = 0; i < positions.length; i++) {

    var marker = new kakao.maps.Marker({
        map: map,
        position: positions[i].latlng
    });

    var infowindow = new kakao.maps.InfoWindow({
        content: positions[i].content
    });

    kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
    kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
}

function makeOverListener(map, marker, infowindow) {
    return function() {
        infowindow.open(map, marker);
    };
}

function makeOutListener(infowindow) {
    return function() {
        infowindow.close();
    };
}

/*
var content = '<div class="wrap">' + 
            '    <div class="info">' + 
            '        <div class="title">' + 
            '            신세계백화점 아라리오점' + 
            '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' + 
            '        </div>' + 
            '        <div class="body">' + 
            '            <div class="img">' +
            '                <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F421%2F2020%2F12%2F30%2F0005079158_001_20201230152823148.jpg&type=a340" width="73" height="70">' +
            '           </div>' + 
            '            <div class="desc">' + 
            '                <div class="ellipsis">충남 천안시 동남구 만남로 43</div>' + 
            '                <div class="jibun ellipsis">(우) 31120 (지번) 신부동 354-1</div>' + 
            '                <div><a href="https://www.shinsegae.com/store/main.do?storeCd=SC00009" target="_blank" class="link">홈페이지</a></div>' + 
            '            </div>' + 
            '        </div>' + 
            '    </div>' +    
            '</div>';

var overlay = new kakao.maps.CustomOverlay({
    content: content,
    map: map,
    position: marker.getPosition()
})


kakao.maps.event.addListener(map, 'click', function() {
    overlay.setMap(map);
});

function closeOverlay() {
    overlay.setMap(null);
}
*/