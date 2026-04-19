export async function fetchNav(endpoint_url){
    /* fetch nav bar data from endpoint */

    
    // nav bar options endpoint
    const apiUrl = endpoint_url

    try{
        // fetch data from endpoint
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
        });

        // recieve data from endpont
        const response_result = await response.json();

        // check status
        if (response_result.ok){
            console.log(response_result.options);
        } else{
            console.log(response_result.success)
        }

        return response_result.options;

    // catch error and return message
    } catch (error) {
        console.error('Network Error:', error);
        return {succes: false, error: error.message};
    }
}


// creates nav options dynamically using API endpoint
export async function createOptions(endpoint_url, side){

    // fetch nav options from endpoint to iterate 
    const options = await fetchNav(endpoint_url);

    // for name in options
    for (var name of Object.entries(options)){

        // create a list element
        const list_item = document.createElement('li');
        list_item.classList.add('list-item');
        list_item.classList.add('page-redirect')


        // create an image element
        const list_img = document.createElement('img');
        list_img.classList.add('list-img');
        list_img.src = `../../static/images/icons/dashboard/sidebar/${name[1]['name'].toLowerCase()}-light.png`;

        // create an anchor element
        const list_link = document.createElement('a');
        list_link.classList.add('item');
        list_link.classList.add('category');
        list_link.classList.add('page-redirect')
        list_link.innerText = name[1]['name'];

        // if sidebar then
        if (side) {

            // append to sidebar-list as child 
            var nav_list = document.getElementById('sidebar-list');
            list_item.classList.add('sidebar-item')
            list_item.appendChild(list_img);

        } else {
            // append to list
            var nav_list = document.getElementById('list');

        } 


        list_item.appendChild(list_link);

        nav_list.appendChild(list_item);
    }
}



