let player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        videoId: 'LgijD2Cwj5s', // Reemplaza 'VIDEO_ID' con el ID de tu video de YouTube
        playerVars: {
            'autoplay': 0,
            'controls': 1,
            'rel': 0,
            'showinfo': 0
        },
        events: {
            'onReady': videoPlayerReady
        }
    });
}

function videoPlayerReady(event) {
    const videoListItems = document.querySelectorAll('#videoList li');
    videoListItems.forEach(item => {
        item.addEventListener('click', function() {
            const time = parseInt(item.getAttribute('data-time'));
            event.target.seekTo(time);
        });
    });
}
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
document.querySelector(".bars__menu").addEventListener("click",animateBars);

const barraDesplegable = document.querySelector(".barra-desplegable");
const line1__bars = document.querySelector(".line1__bars-menu");
const line2__bars = document.querySelector(".line2__bars-menu");
const line3__bars = document.querySelector(".line3__bars-menu");
function animateBars(){
    line1__bars.classList.toggle('activeline1__bars-menu');
    line2__bars.classList.toggle('activeline2__bars-menu');
    line3__bars.classList.toggle('activeline3__bars-menu');
    barraDesplegable.classList.toggle('show')
}