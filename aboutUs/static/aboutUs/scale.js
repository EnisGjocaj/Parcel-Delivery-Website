const imageContainer = document.getElementById('image-container');
const scalingImage = document.getElementById('scaling-image');

window.addEventListener('scroll', function() {
  const scrollTop = window.scrollY;
  const containerTop = imageContainer.offsetTop;
  const containerHeight = imageContainer.offsetHeight;
  const containerBottom = containerTop + containerHeight;
  const windowHeight = window.innerHeight;

  if (scrollTop >= containerTop - windowHeight && scrollTop <= containerBottom) {
    
    const scale = 1 + (scrollTop - containerTop + windowHeight) / (containerHeight + windowHeight);
    scalingImage.style.transform = `scale(${scale})`;
  }
});
