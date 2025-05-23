// index.js => Handles the carousel logic and scripts for home page

/* ================================
   Navbar Toggle Functionality
================================== */
// Toggles the 'active' class on the navbar for responsive menu (mobile)
function toggleMenu() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active');
}


/* ================================
   Hero Image Carousel
   - Auto-play every 4 seconds
   - Manual navigation support
================================== */
let currentSlide = 0; // Track the currently visible slide
const slides = document.querySelectorAll(".carousel-image"); // All slide images
const dots = document.querySelectorAll(".dot"); // Navigation dots

// Display the slide with the given index and activate the corresponding dot
function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.toggle("active", i === index); // Show current slide
        dots[i].classList.toggle("active", i === index); // Highlight corresponding dot
    });
    currentSlide = index;
}

// Move to the next slide, wrapping back to the first if at the end
function nextSlide() {
    showSlide((currentSlide + 1) % slides.length);
}

// Move to the previous slide, wrapping to the last if at the beginning
function prevSlide() {
    showSlide((currentSlide - 1 + slides.length) % slides.length);
}

// Manually set the slide, e.g., on dot click
function setSlide(index) {
    showSlide(index);
}

// Automatically switch to the next slide every 4 seconds
setInterval(nextSlide, 4000);
