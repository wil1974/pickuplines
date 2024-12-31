const pickupLineDisplay = document.getElementById('pickupLine');
const generateButton = document.getElementById('generateButton');

const pickupLineDescriptionInput = document.getElementById('pickupLineDescription');

async function generatePickupLine() {
    pickupLineDisplay.textContent = "Loading...";
    const description = pickupLineDescriptionInput.value;
    try {
        const response = await fetch('/generate_pickup_line', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description: description })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        const pickupLine = data.pickupLine;
        pickupLineDisplay.textContent = pickupLine;
    } catch (error) {
        console.error("Failed to fetch pickup line:", error);
        pickupLineDisplay.textContent = "Failed to load pickup line.";
    }
}

generateButton.addEventListener('click', generatePickupLine);
