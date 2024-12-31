const pickupLines = [
    "Are you a parking ticket? Because you've got 'fine' written all over you.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Is your name Google? Because you have everything I've been searching for.",
    "Are you a magician? Because whenever I look at you, everyone else disappears!",
    "I'm not a photographer, but I can picture us together.",
    "Do you have a map? I keep getting lost in your eyes.",
    "If being sexy was a crime, you'd be guilty as charged.",
    "Are you from Tennessee? Because you're the only ten I see!",
    "I'm learning about important dates in history. Wanna be one of them?",
    "Aside from being sexy, what do you do for a living?"
];

const pickupLineDisplay = document.getElementById('pickupLine');
const generateButton = document.getElementById('generateButton');

function generatePickupLine() {
    const randomIndex = Math.floor(Math.random() * pickupLines.length);
    pickupLineDisplay.textContent = pickupLines[randomIndex];
}

generateButton.addEventListener('click', generatePickupLine);
