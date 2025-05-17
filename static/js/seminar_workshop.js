document.addEventListener('DOMContentLoaded', () => {
    // Initialize the page with all entries shown
    filterEntries('all');
    
    // Dynamic search on input - no button needed
    document.getElementById('searchInput').addEventListener('input', function() {
        const activeButton = document.querySelector('.filter-buttons button.active');
        const currentFilter = activeButton ? 
            getButtonType(activeButton.textContent) : 'all';
        filterEntries(currentFilter);
    });
});

/**
 * Filters entries based on type and search term
 * @param {string} type - The type of entries to show ('all', 'seminar', 'workshop', 'visit')
 */
function filterEntries(type) {
    const entries = document.querySelectorAll('.entry-item');
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();

    entries.forEach(entry => {
        const matchesType = type === 'all' || entry.classList.contains(type);
        const matchesSearch = searchTerm === '' || 
            entry.textContent.toLowerCase().includes(searchTerm);
        
        entry.style.display = (matchesType && matchesSearch) ? 'block' : 'none';
    });

    updateActiveButton(type);
}

/**
 * Updates the active state of filter buttons
 * @param {string} activeType - The currently active filter type
 */
function updateActiveButton(activeType) {
    const buttons = document.querySelectorAll('.filter-buttons button');
    buttons.forEach(button => {
        button.classList.remove('active');
        if (getButtonType(button.textContent) === activeType) {
            button.classList.add('active');
        }
    });
}

/**
 * Determines the filter type based on button text
 * @param {string} buttonText - The text content of the button
 * @returns {string} - The corresponding filter type
 */
function getButtonType(buttonText) {
    const text = buttonText.toLowerCase();
    if (text.includes('all')) return 'all';
    if (text.includes('seminar')) return 'seminar';
    if (text.includes('workshop')) return 'workshop';
    if (text.includes('visit')) return 'visit';
    return 'all';
}

