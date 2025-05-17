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


/* ================================
   DOM Ready Logic:
   - Initialize Swiper for News
   - Expandable "Read More" Cards
================================== */
document.addEventListener('DOMContentLoaded', function () {

    // Check if the news swiper exists, then initialize Swiper.js
    if (document.querySelector('.news-swiper')) {
        new Swiper('.news-swiper', {
            loop: true, // Infinite loop
            autoplay: { delay: 5000 }, // Slide every 5 seconds
            slidesPerView: 1, // Show 1 slide at a time by default
            spaceBetween: 20, // Space between slides
            pagination: { el: '.swiper-pagination' }, // Dots navigation
            navigation: {
                nextEl: '.swiper-button-next', // Next button
                prevEl: '.swiper-button-prev'  // Previous button
            },
            // Responsive breakpoints
            breakpoints: {
                768: { slidesPerView: 2 },   // 2 slides for tablets
                1024: { slidesPerView: 3 }   // 3 slides for desktops
            }
        });
    }

    // Handle expanding/collapsing "Read More" text in news cards
    document.addEventListener('click', function (e) {
        // If clicked element is a "Read More" button
        if (e.target.classList.contains('read-more')) {
            const excerpt = e.target.closest('.news-content').querySelector('.news-excerpt');
            excerpt.classList.toggle('expanded'); // Toggle full text
            // Change button text accordingly
            e.target.textContent = excerpt.classList.contains('expanded') ? 'Read Less' : 'Read More';
        }
    });
});
