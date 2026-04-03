function showPass(element) {
    /* checkbox switch password type (password or text) */
    
    const targetID = element.dataset.target; // get target id from checkbox activated

    // toggle type
    if (document.getElementById(targetID).type == 'password'){
        document.getElementById(targetID).type = 'text';
    } else{
        document.getElementById(targetID).type = 'password';
    }
}

async function checkConf(pass, conf) {
    /* check confirmation password & password */
    
    // show error message if not the same value
    if (pass == conf) {
        return true;
    } else{
        document.getElementById('conf-error').innerText = "Passwords Don't Match!"

        return false;

    }
}

async function fetchValidation(data){
    /* send data to validate endpoint */

    // validation endpoint url
    const apiUrl = 'http://127.0.0.1:5000/api/auth/validate-input'

    try{
        // send data to endpoint
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });


        // recieve validation response
        const response_result = await response.json();


        // reset any validation errors
        document.querySelectorAll('.error').forEach(element => {
            element.innerText = "";
        });


        // check status
        if (response_result.ok){
            console.log(response_result.message);
        } else{
            
            if (response_result.errors){
                // loop through error message
                for (const [field, message] of Object.entries(response_result.errors)) {

                // allocate message with correct element
                const errorEl = document.getElementById(`${field}-error`);
                if (errorEl){

                    // display error
                    errorEl.innerText = message.join(' ');
                }
            }
            }
        }

        return response_result;

    } catch (error) {
        console.error('Network Error:', error);
        return {succes: false, error: error.message};
    }
}


async function fetchUser(data) {
    /* send data to be queried */

    // login endpoint url
    const apiUrl = 'http://127.0.0.1:5000/api/auth/login'


    try{
        // send data to endpoint
        const response = await fetch(apiUrl, {
            method: 'POST',
            credentials: 'include',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });

        // recieve validation response
        const response_result = await response.json();

        if (response_result.success){
            window.location.href = response_result.redirect;
        }else{
            document.getElementById('error').innerText = response_result.message;
        }

    } catch (error) {
        console.error('Network Error:', error);
        return {success: false, error: error.message};
    }
}



document.addEventListener('DOMContentLoaded', () => { // wait for DOM content

    document.getElementById('register-form').addEventListener('submit', async (event) => { // wait for submit
        event.preventDefault() // stop page reload

        // retrieve register form data
        const data = {
            'email' : event.target.email.value,
            'name'  : event.target.name.value,
            'password'  : event.target.pass.value,
            'conf'  : event.target.conf.value,
            'phone' : event.target.phone.value,
            'type'  : event.target.querySelector('input[name="acc-type"]:checked')?.value
        };

        // if confirmation password & password equal then
        if (await checkConf(data['password'], data['conf'])) {
            // fetch validation result
            const result = await fetchValidation(data);
            console.log(result);
        }
        
    });

    document.getElementById('login-form').addEventListener('submit', async (event) => { // wait for submit
        event.preventDefault() // stop page reload

        // retrieve login form data
        const data = {
            'email' : event.target.email.value,
            'password'  : event.target.pass.value,
        };

        // fetch login result
        const result = await fetchUser(data);
        console.log(result);
    });
});