// Enhanced Project Filtering with Search
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const searchInput = document.getElementById('project-search');
    const projectCards = document.querySelectorAll('.project-card');
    
    // Combined filter function
    function filterProjects() {
        const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
        const searchTerm = searchInput.value.toLowerCase();
        
        projectCards.forEach(project => {
            const status = project.dataset.status;
            const type = project.dataset.type;
            const title = project.querySelector('h2').textContent.toLowerCase();
            const description = project.querySelector('p').textContent.toLowerCase();
            const tags = Array.from(project.querySelectorAll('.project-tag')).map(tag => tag.textContent.toLowerCase());
            
            // Check filter match
            const filterMatch = activeFilter === 'all' || 
                               status === activeFilter || 
                               type.includes(activeFilter);
            
            // Check search match
            const searchMatch = searchTerm === '' || 
                               title.includes(searchTerm) || 
                               description.includes(searchTerm) || 
                               tags.some(tag => tag.includes(searchTerm));
            
            // Show/hide based on matches
            if (filterMatch && searchMatch) {
                project.style.display = 'block';
                setTimeout(() => {
                    project.style.opacity = '1';
                    project.style.transform = 'translateY(0)';
                }, 50);
            } else {
                project.style.opacity = '0';
                project.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    project.style.display = 'none';
                }, 300);
            }
        });
    }
    
    // Filter button event listeners
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterProjects();
        });
    });
    
    // Search input event listener with debounce
    let searchTimeout;
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(filterProjects, 300);
    });
    
    // Initialize with all projects shown
    filterProjects();
});