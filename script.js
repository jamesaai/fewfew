// Sample JavaScript functionality for dynamic updates

// Update battery progress dynamically
const batteryProgress = document.getElementById('battery-progress');
const batteryLife = document.getElementById('battery-life');

function updateBatteryProgress() {
    const batteryPercentage = 85; // Simulating the battery life percentage
    batteryProgress.style.width = batteryPercentage + '%';
    batteryLife.innerText = batteryPercentage + '%';
}

// Location and Map Simulation (could use an API like Google Maps for real implementation)
function updateLocation() {
    const mapContainer = document.getElementById('map');
    mapContainer.innerHTML = '<p>Pet’s current location will be shown here (using Google Maps API)</p>';
}

// Simulate updating health data
function updateHealthStats() {
    document.getElementById('heart-rate').innerText = '95 bpm';
    document.getElementById('body-temp').innerText = '38°C';
    document.getElementById('weight').innerText = '30 kg';
}

// Simulate activity data
function updateActivityStats() {
    document.getElementById('steps').innerText = '500';
    document.getElementById('distance').innerText = '1.2 km';
    document.getElementById('calories').innerText = '80 kcal';
}

// Initializing functions on page load
window.onload = function () {
    updateBatteryProgress();
    updateLocation();
    updateHealthStats();
    updateActivityStats();
};
