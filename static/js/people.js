document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('people-search');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const personCards = document.querySelectorAll('.person-card');
    const noResultsMsg = document.getElementById('no-results-message');
    
    // Combined filter function
    function filterPeople() {
        const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
        const searchTerm = searchInput.value.toLowerCase().trim();
        
        let visibleCount = 0;
        
        personCards.forEach(card => {
            const degree = card.dataset.degree;
            const name = card.dataset.name;
            const interests = card.dataset.interests;
            
            // Check filter match
            const filterMatch = activeFilter === 'all' || 
                              (activeFilter === 'phd' && degree.includes('ph')) || 
                              (activeFilter === 'mtech' && degree.includes('m.tech')) || 
                              (activeFilter === 'btech' && degree.includes('b.tech'));
            
            // Check search match
            const searchMatch = searchTerm === '' || 
                               name.includes(searchTerm) || 
                               degree.includes(searchTerm) || 
                               interests.includes(searchTerm);
            
            // Show/hide based on matches
            if (filterMatch && searchMatch) {
                card.style.display = 'flex';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });
        
        // Show/hide no results message
        noResultsMsg.style.display = visibleCount > 0 ? 'none' : 'flex';
    }
    
    // Filter button event listeners
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterPeople();
        });
    });
    
    // Search input event listener with debounce
    let searchTimeout;
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(filterPeople, 300);
    });
    
    // Initialize with all people shown
    filterPeople();
});