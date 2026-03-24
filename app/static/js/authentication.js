function showPass() {
    if (document.q('pass').type == 'password') {
        document.getElementById('pass').type = 'text';
    } else {
        document.getElementById('pass').type = 'password';
    }
}

async function checkConf(pass, conf) {
    if (pass == conf) {
        return true;
    } else{
        document.getElementById('register-error').innerText = "Passwords Don't Match!"
        await new Promise(r => setTimeout(r, 2000));
        document.getElementById('register-error').innerText = ""
        return false;

    }
}

document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('register-form').addEventListener('submit', async (event) => {
        event.preventDefault()

        const data = {
            'email' : event.target.email.value,
            'name'  : event.target.name.value,
            'pass'  : event.target.pass.value,
            'conf'  : event.target.conf.value,
            'phone' : event.target.phone.value,
            'type'  : event.target.querySelector('input[name="acc-type"]:checked')?.value
        };

        if (checkConf(data['pass'], data['conf'])) {


        }
        

        

    });

});