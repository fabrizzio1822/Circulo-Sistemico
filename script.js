document.addEventListener('DOMContentLoaded', function() {
    const videoListItems = document.querySelectorAll('#videoList li');
    const videoPlayer = document.getElementById('videoPlayer');

    videoListItems.forEach(item => {
        item.addEventListener('click', function() {
            const time = parseInt(item.getAttribute('data-time')) / 10; // Dividimos entre 10 para obtener los segundos con decimales
            videoPlayer.currentTime = time;
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const carouselImages = document.querySelectorAll('.carousel-images img');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    let currentIndex = 0;

    function showImage(index) {
        carouselImages.forEach((image, idx) => {
            if (idx === index) {
                image.style.display = 'block';
            } else {
                image.style.display = 'none';
            }
        });
    }

    function nextImage() {
        currentIndex++;
        if (currentIndex >= carouselImages.length) {
            currentIndex = 0;
        }
        showImage(currentIndex);
    }

    function prevImage() {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = carouselImages.length - 1;
        }
        showImage(currentIndex);
    }

    prevButton.addEventListener('click', prevImage);
    nextButton.addEventListener('click', nextImage);

    showImage(currentIndex);
});



