const mapElement = document.getElementById("map");
const isen = [Number(mapElement.dataset.lat), Number(mapElement.dataset.lng)];

const map = L.map(mapElement).setView(isen, 16);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

L.marker(isen).addTo(map).bindPopup("ISEN Toulon").openPopup();
