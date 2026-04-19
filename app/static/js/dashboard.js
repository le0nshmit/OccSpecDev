import { createOptions } from './utils.js';


async function main(){
    createOptions('http://127.0.0.1:5000/api/admin/dashboard-nav-options', false);
    createOptions('http://127.0.0.1:5000/api/admin/dashboard-nav-options', true);
}

function viewImage(element) {
    const fullImage = element.nextElementSibling;

    fullImage.style.display = 'block';
}

function closeImage(element) {
    const fullImage = element.parentElement;

    fullImage.style.display = 'none';
}

function initialiseCarousel(){
    const track = document.getElementById('analytics-statistics-carousel-track');
    const leftBtn = document.querySelector('.analytics-carousel-button-left');
    const rightBtn = document.querySelector('.analytics-carousel-button-right');
    
    console.log('Initialising carousel - checking buttons:', {
        leftBtnCount: document.querySelectorAll('.analytics-carousel-button-left').length,
        rightBtnCount: document.querySelectorAll('.analytics-carousel-button-right').length,
        leftBtn: leftBtn?.className,
        rightBtn: rightBtn?.className
    });
    
    let index = 0;
    const total = track.children.length;

    function updateCarousel() {
        const transform = `translateX(-${index * 115}%)`;
        track.style.transform = transform;
        console.log('Carousel index:', index, 'Transform:', transform, 'Total:', total);
    }

    leftBtn.addEventListener('click', () => {
        index = (index - 1 + total) % total;
        console.log('Left clicked, new index:', index);
        updateCarousel();
    });

    rightBtn.addEventListener('click', () => {
        index = (index + 1) % total;
        console.log('Right clicked, new index:', index);
        updateCarousel();
    });
}



/* Build Order Table */
async function fetchOrders(){
    const url = 'http://127.0.0.1:5000/admin/dashboard/orders'
}



document.addEventListener('DOMContentLoaded', () => {
    // Product Image View
    const images = document.querySelectorAll('.produce-table-row-image');
    const exit_buttons = document.querySelectorAll('.produce-table-row-image-full-exit');

    images.forEach(img => {
        img.addEventListener('click', () => viewImage(img));
    });

    exit_buttons.forEach(img => {
        img.addEventListener('click', () => closeImage(img));
    });

    
    // Content Redirect
    


    initialiseCarousel()    
});

    
main() 