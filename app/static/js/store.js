import { createOptions } from './utils.js';


async function main(){
    createOptions('http://127.0.0.1:5000/api/store/dashboard-nav-options', false);
   
    // list
    const list = document.getElementById('list');

    // list item
    const list_item = document.createElement('li');
    list_item.classList.add('list-item');

    // item
    const item = document.createElement('a');
    item.classList.add('item');
    item.id = 'view';
    item.href = '#';
    item.innerText = 'View More →';

    // append item to list item
    list_item.appendChild(item);

    // append list item to list
    list.appendChild(list_item);

    // create a list element
    const cartItem = document.createElement('li');
    cartItem.classList.add('list-item');
    
    // create a div element
    const list_div = document.createElement('div');
    list_div.id = 'cart-button';

    // create an image element
    const list_img = document.createElement('img');
    list_img.id = 'cart-logo';
    list_img.src = '/static/images/icons/trolley-light.png'; 
    list_img.alt = 'Cart';

    // create header element
    const cartPrice = document.createElement('h3');
    cartPrice.id = 'cart-price';
    cartPrice.innerText = '£14.50'

    // append elements
    list_div.appendChild(list_img);
    list_div.appendChild(cartPrice);
    cartItem.appendChild(list_div);
    list.appendChild(cartItem);
}

await main();