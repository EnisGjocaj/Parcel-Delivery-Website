console.log("Zooming")

const zoomContainer = document.getElementById('zoomContainer');
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        zoomContainer.classList.add('zoom-in', 'active');
      } else {
        zoomContainer.classList.remove('zoom-in', 'active');
      }
    });
  });

observer.observe(zoomContainer);

