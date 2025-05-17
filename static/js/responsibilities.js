document.addEventListener('DOMContentLoaded', function() {
    console.log('Responsibilities page loaded');
    
    // Store original content to restore later
    const originalContents = new Map();
    document.querySelectorAll('.responsibility-item').forEach(item => {
        const roleElement = item.querySelector('.role');
        const instituteElement = item.querySelector('.institute');
        originalContents.set(item, {
            role: roleElement.innerHTML,
            institute: instituteElement.innerHTML
        });
    });

    // Search functionality
    const searchInput = document.getElementById('responsibilitySearch');
    const responsibilityItems = document.querySelectorAll('.responsibility-item');
    const noResultsMessage = document.createElement('div');
    noResultsMessage.className = 'no-results';
    noResultsMessage.textContent = 'No responsibilities found matching your search.';
    document.getElementById('responsibilitiesContainer').appendChild(noResultsMessage);
    
    function performSearch() {
        const searchTerm = searchInput.value.trim().toLowerCase();
        let hasResults = false;
        
        // Reset all items first
        responsibilityItems.forEach(item => {
            const original = originalContents.get(item);
            item.querySelector('.role').innerHTML = original.role;
            item.querySelector('.institute').innerHTML = original.institute;
            item.style.display = 'flex';
            item.classList.remove('highlight');
        });

        // If search is empty, show everything
        if (searchTerm === '') {
            document.querySelectorAll('.category').forEach(category => {
                category.style.display = 'block';
            });
            noResultsMessage.style.display = 'none';
            return;
        }

        // Filter and highlight
        responsibilityItems.forEach(item => {
            const role = item.dataset.role;
            const institute = item.dataset.institute;
            const from = item.dataset.from;
            const to = item.dataset.to;
            
            if (role.includes(searchTerm) || 
                institute.includes(searchTerm) || 
                from.includes(searchTerm) || 
                to.includes(searchTerm)) {
                hasResults = true;
                item.classList.add('highlight');
                
                // Highlight matching text
                if (role.includes(searchTerm)) {
                    const roleElement = item.querySelector('.role');
                    roleElement.innerHTML = roleElement.textContent.replace(
                        new RegExp(searchTerm, 'gi'), 
                        match => `<span class="highlight-text">${match}</span>`
                    );
                }
                if (institute.includes(searchTerm)) {
                    const instituteElement = item.querySelector('.institute');
                    instituteElement.innerHTML = instituteElement.textContent.replace(
                        new RegExp(searchTerm, 'gi'), 
                        match => `<span class="highlight-text">${match}</span>`
                    );
                }
            } else {
                item.style.display = 'none';
            }
        });
        
        // Show/hide categories
        document.querySelectorAll('.category').forEach(category => {
            const visibleItems = category.querySelectorAll('.responsibility-item[style!="display: none;"]');
            category.style.display = visibleItems.length > 0 ? 'block' : 'none';
        });
        
        noResultsMessage.style.display = hasResults ? 'none' : 'block';
    }
    
    // Perform search as user types with slight debounce
    let searchTimeout;
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(performSearch, 300);
    });
    
    // Also trigger search immediately on keydown for faster response
    searchInput.addEventListener('keydown', function() {
        clearTimeout(searchTimeout);
        performSearch();
    });
});