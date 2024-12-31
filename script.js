const pickupLineDisplay = document.getElementById('pickupLine');
const generateButton = document.getElementById('generateButton');

async function generatePickupLine() {
    pickupLineDisplay.textContent = "Loading...";
    try {
        const response = await fetch('https://api.example.com/pickup-line'); // Replace with your API endpoint
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        pickupLineDisplay.textContent = data.pickupLine; // Assuming the API returns an object with a 'pickupLine' property
    } catch (error) {
        console.error("Failed to fetch pickup line:", error);
        pickupLineDisplay.textContent = "Failed to load pickup line.";
    }
}

generateButton.addEventListener('click', generatePickupLine);
