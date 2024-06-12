const carousel = document.querySelector('.carousel-inner');
const images = carousel.querySelectorAll('img');
const totalImages = images.length;
const imageWidth = images[0].clientWidth;

const carouselItems = document.querySelectorAll('.carousel-item');

let currentIndex = 0;

console.log("Helloooo")


function showSlide(index) {
    carouselItems.forEach((item, i) => {
        if (i === index) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
}

function slide() {
    currentIndex = (currentIndex + 1) % totalImages;
    carousel.style.transform = `translateX(-${currentIndex * imageWidth}px)`;
}

setInterval(slide, 9000);