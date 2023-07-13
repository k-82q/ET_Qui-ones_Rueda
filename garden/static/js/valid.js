const nombre =document.getElementById("nom");
const apellido =document.getElementById("ape");
const email =document.getElementById("mail");
const telefono =document.getElementById("fono");
const region =document.getElementById("region");
const form = document.getElementById("form");
const parrafo = document.getElementById("warnings");

form.addEventListener("submit", e => {
    e.preventDefault();
    let entrar=false;
    let warnings = ""
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    if(nombre.value.length<6){
       warnings += 'El nombre debe tener al menos 6 caracteres <br>'
       entrar=true;

    }
    if(apellido.value.length<6){
        warnings += 'El apellido debe tener al menos 6 caracteres <br>'
        entrar=true;
    }
    
    if(!regexEmail.test(email.value)){
        warnings += 'El email no es valido <br>'    
        entrar=true;
    }
    if(telefono.value.length<9){
        warnings += 'El telefono debe tener al menos 9 caracteres <br>'
        entrar=true;
    }
    if(region.value.length<5){
        warnings += 'El region debe tener al menos 5 caracteres <br>'
        entrar=true;
    }

    if(entrar){
            parrafo.inertHTML = warnings;
    }
    else{
        parrafo.inertHTML = "enviado";
    }
})

