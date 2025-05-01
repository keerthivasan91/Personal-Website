// Select all navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        // Prevent default anchor jump
        e.preventDefault();
        
        // Get the target section
        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        // Smooth scroll to section
        if (targetSection) {
            targetSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.nav-toggle');
    const menu  = document.querySelector('.nav-menu');
  
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('open');
      menu.classList.toggle('open');
    });
  });
  