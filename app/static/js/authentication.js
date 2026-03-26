function showPass(element) {
    /* checkbox switch password type (password or text) */

    const targetID = element.dataset.target; // get id from checkbox
    console.log(targetID);

    // toggle password type
    if (document.getElementById(targetID).type == 'password'){
        document.getElementById(targetID).type = 'text';
    } else {
        document.getElementById(targetID).type = 'password';
    };
}

async function checkConf(pass, conf) {
    /* check confirmation password & password */

    // show error message if not the same
    if (pass == conf) {
        return true;
    } else{
        document.getElementById('conf-error').innerText = "Passwords Don't Match!" 
        await new Promise(r => setTimeout(r, 2000));
        document.getElementById('conf-error').innerText = ""
        return false;

    }
}

async function fetchPost(data){
    /* send data to validate endpoint */

    // validation endpoint
    const apiUrl = 'http://127.0.0.1:5000/api/auth/validate';

    try {

        // send data to endpoint
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });        

        // get response
        const response_result = await response.json();


        // reset errors
        document.querySelectorAll('.error').forEach(element => {
            element.innerText = "";
        });


        // check status
        if (response.ok) {
            console.log(response_result.message);
        } else {
            console.log('Validation failed:', response_result.errors)


            for (const [field, messages] of Object.entries(response_result.errors)) {
                const errorEl = document.getElementById(`${field}-error`);
                if (errorEl){
                    errorEl.innerText = messages.join(', ');
                }
            }
        }

    
        return response_result;

    } catch (error) {
        console.error('Network Error:', error);
        return {success: false, error: error.message};
    }
}




document.addEventListener('DOMContentLoaded', () => { // wait for content to load

    /* retrieve register form data */
    document.getElementById('register-form').addEventListener('submit', async (event) => { // wait for submit clicked
        event.preventDefault() // stop page reload

        // register data
        const data = {
            'email' : event.target.email.value,
            'name'  : event.target.name.value,
            'password'  : event.target.pass.value,
            'conf'  : event.target.conf.value,
            'phone' : event.target.phone.value,
            'type'  : event.target.querySelector('input[name="acc-type"]:checked')?.value
        };

        // check password & confirmation password
        if (await checkConf(data['password'], data['conf'])) {
            const result = await fetchPost(data);
            console.log(result);
        }
        
    });

});



