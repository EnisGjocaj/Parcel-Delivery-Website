// Add this in your existing JavaScript file or create a new one

console.log("Scroll btn")

// Function to show or hide the scroll-to-top button based on scroll position
function handleScrollToTopButton() {
    const scrollToTopButton = document.getElementById('scrollToTopButton');
    if (window.scrollY > 300) {
        scrollToTopButton.classList.remove('hidden');
    } else {
        scrollToTopButton.classList.add('hidden');
    }
}

// Function to smoothly scroll to the top when the button is clicked
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Event listener for scroll events to show or hide the button
window.addEventListener('scroll', handleScrollToTopButton);

// Event listener for the button click to scroll to the top
document.getElementById('scrollToTopButton').addEventListener('click', scrollToTop);
