// ایجاد نقشه
const map = L.map('map').setView([38.075, 46.305], 14);

// نقشه پایه
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// داده‌های نمونه
const binsData = [
    { bin_id: "B001", lat: 38.074124, lon: 46.305969, cap: 660, fill: 90, status: "active" },
    { bin_id: "B002", lat: 38.078400, lon: 46.310200, cap: 660, fill: 45, status: "active" },
    { bin_id: "B003", lat: 38.071500, lon: 46.299800, cap: 1100, fill: 75, status: "active" },
    { bin_id: "B004", lat: 38.080100, lon: 46.315000, cap: 660, fill: 25, status: "active" },
    { bin_id: "B005", lat: 38.072000, lon: 46.301000, cap: 800, fill: 85, status: "active" },
    { bin_id: "B006", lat: 38.075000, lon: 46.308000, cap: 500, fill: 10, status: "inactive" },
    { bin_id: "B007", lat: 38.076000, lon: 46.305000, cap: 750, fill: 60, status: "active" }
];

let markersLayer = L.layerGroup().addTo(map);

// تعیین رنگ نشانگر بر اساس پرشدگی
function getColor(fill) {
    if (fill >= 80) return "red";
    if (fill >= 50) return "orange";
    return "green";
}

// رسم نشانگرها
function drawMarkers(filterStatus) {
    markersLayer.clearLayers();

    binsData.forEach(bin => {
        if (filterStatus !== "all" && bin.status !== filterStatus) return;

        const circle = L.circleMarker([bin.lat, bin.lon], {
            radius: 12,
            fillColor: getColor(bin.fill),
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        });

        const popupContent = `
            <div style="font-family: Tahoma; text-align: right;">
                <b>شناسه:</b> ${bin.bin_id}<br>
                <b>ظرفیت:</b> ${bin.cap} لیتر<br>
                <b>درصد پرشدگی:</b> ${bin.fill}%<br>
                <b>وضعیت:</b> ${bin.status === 'active' ? 'فعال' : 'غیرفعال'}
            </div>
        `;
        circle.bindPopup(popupContent);
        markersLayer.addLayer(circle);
    });
}

// رسم اولیه
drawMarkers("all");

// رویداد فیلتر
document.getElementById("statusFilter").addEventListener("change", (e) => {
    drawMarkers(e.target.value);
});