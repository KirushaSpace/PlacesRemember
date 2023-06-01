let center = [56.838010, 60.597465];

function init() {
	let map = new ymaps.Map('map-test', {
		center: center,
		zoom: 17
	},{
		balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search'
	});
	map.events.add('click', function (e) {
        if (!map.balloon.isOpen()) {
            var coords = e.get('coords');
            map.balloon.open(coords, {
                contentHeader:'Событие',
                contentBody:'произошло в этом месте',
                contentFooter:'<sup>Щелкните еще раз</sup>'
            });
            document.getElementById("id_lat").value = coords[0]
            document.getElementById("id_lon").value = coords[1]
        }
        else {
            map.balloon.close();
        }
    });
    // Скрываем хинт при открытии балуна.
    map.events.add('balloonopen', function (e) {
        map.hint.close();
    });
}

ymaps.ready(init);