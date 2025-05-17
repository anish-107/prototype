document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map
    initMap();
    
    // Setup form submission handler
    setupContactForm();
});

function initMap() {
    // Coordinates for NIT Jalandhar (example)
    const nitCoords = [31.39700816912175, 75.53407399561769];
    
    // Initialize map
    const map = L.map('map').setView(nitCoords, 16);
    
    // Add tile layer (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // Add custom marker
    const customIcon = L.icon({
        iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34]
    });
    
    // Add marker to map
    L.marker(nitCoords, {icon: customIcon})
        .addTo(map)
        .bindPopup(`
            <b>NIT Jalandhar</b><br>
            Department of Information Technology<br>
            Dr. Ranjeet Kumar Rout
        `)
        .openPopup();
}

function setupContactForm() {
    const form = document.getElementById('contactForm');
    const responseDiv = document.getElementById('formResponse');
    const submitBtn = form.querySelector('button[type="submit"]');
    const btnText = submitBtn.querySelector('.btn-text');
    const btnLoader = submitBtn.querySelector('.btn-loader');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state
        btnText.style.display = 'none';
        btnLoader.style.display = 'inline-block';
        submitBtn.disabled = true;
        
        // Get form data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        try {
            // Send data to server
            const response = await fetch('/submit_contact_form', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (response.ok) {
                // Success
                showResponse(result.message || 'Message sent successfully!', 'success');
                form.reset();
            } else {
                // Error from server
                showResponse(result.message || 'Error sending message', 'error');
            }
        } catch (error) {
            // Network error
            console.error('Error:', error);
            showResponse('Network error. Please try again later.', 'error');
        } finally {
            // Reset button state
            btnText.style.display = 'inline-block';
            btnLoader.style.display = 'none';
            submitBtn.disabled = false;
        }
    });
}

function showResponse(message, type) {
    const responseDiv = document.getElementById('formResponse');
    responseDiv.textContent = message;
    responseDiv.className = `form-response ${type}`;
    responseDiv.style.display = 'block';
    
    // Hide after 5 seconds
    setTimeout(() => {
        responseDiv.style.display = 'none';
    }, 5000);
}