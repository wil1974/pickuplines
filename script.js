const pickupLineDisplay = document.getElementById('pickupLine');
const generateButton = document.getElementById('generateButton');

async function generatePickupLine() {
    pickupLineDisplay.textContent = "Loading...";
    try {
        const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-goog-api-key': document.querySelector('meta[name="gemini-api-key"]').getAttribute('content')
            },
            body: JSON.stringify({
                prompt: "Generate a short, funny pickup line."
            }),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        // Assuming the API returns a structure like:
        // { candidates: [{ content: { parts: [{ text: "pickup line" }] } }] }
        const pickupLine = data.candidates[0].content.parts[0].text;
        pickupLineDisplay.textContent = pickupLine;
    } catch (error) {
        console.error("Failed to fetch pickup line:", error);
        pickupLineDisplay.textContent = "Failed to load pickup line.";
    }
}

generateButton.addEventListener('click', generatePickupLine);
