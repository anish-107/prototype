document.addEventListener('DOMContentLoaded', function() {
    // Initialize Swiper
    const newsSwiper = new Swiper('.news-swiper', {
        loop: true,
        autoplay: { 
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 1,
        spaceBetween: 20,
        pagination: { 
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        },
        breakpoints: {
            640: { slidesPerView: 2 },
            1024: { slidesPerView: 3 }
        }
    });

    // Read More/Less functionality
    document.querySelectorAll('.read-more').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.news-card');
            const excerpt = card.querySelector('.news-excerpt');
            const fullText = card.querySelector('.news-full-text');
            const icon = this.querySelector('i');
            
            if (excerpt.style.display === 'none') {
                excerpt.style.display = 'block';
                fullText.style.display = 'none';
                this.innerHTML = 'Read More <i class="fas fa-chevron-down"></i>';
            } else {
                excerpt.style.display = 'none';
                fullText.style.display = 'block';
                this.innerHTML = 'Read Less <i class="fas fa-chevron-up"></i>';
            }
        });
    });

    // Search functionality
    const newsSearch = document.getElementById('newsSearch');
    if (newsSearch) {
        const newsSlides = document.querySelectorAll('.swiper-slide');
        const noResultsMessage = document.createElement('div');
        noResultsMessage.className = 'no-results-message';
        noResultsMessage.innerHTML = `
            <i class="fas fa-newspaper"></i>
            <h3>No news found matching your search</h3>
            <p>Try different keywords or check back later for updates</p>
        `;
        noResultsMessage.style.display = 'none';
        document.querySelector('.news-swiper').parentNode.appendChild(noResultsMessage);

        newsSearch.addEventListener('input', function() {
            const searchTerm = this.value.trim().toLowerCase();
            let hasResults = false;

            newsSlides.forEach(slide => {
                const title = slide.querySelector('h3').textContent.toLowerCase();
                const excerpt = slide.querySelector('.news-excerpt').textContent.toLowerCase();
                const fullText = slide.querySelector('.news-full-text').textContent.toLowerCase();
                const combinedContent = title + ' ' + excerpt + ' ' + fullText;

                if (searchTerm === '' || combinedContent.includes(searchTerm)) {
                    slide.style.display = '';
                    hasResults = true;
                    
                    // Highlight matching text
                    const highlight = (element) => {
                        element.innerHTML = element.textContent.replace(
                            new RegExp(searchTerm, 'gi'),
                            match => `<span class="highlight-text">${match}</span>`
                        );
                    };

                    if (searchTerm !== '') {
                        highlight(slide.querySelector('h3'));
                        highlight(slide.querySelector('.news-excerpt'));
                        highlight(slide.querySelector('.news-full-text'));
                        slide.classList.add('highlight');
                    } else {
                        slide.querySelector('h3').innerHTML = slide.querySelector('h3').textContent;
                        slide.querySelector('.news-excerpt').innerHTML = slide.querySelector('.news-excerpt').textContent;
                        slide.querySelector('.news-full-text').innerHTML = slide.querySelector('.news-full-text').textContent;
                        slide.classList.remove('highlight');
                    }
                } else {
                    slide.style.display = 'none';
                }
            });

            noResultsMessage.style.display = hasResults ? 'none' : 'block';
            newsSwiper.update();
        });
    }
});