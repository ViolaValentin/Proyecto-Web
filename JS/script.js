window.onload = init;
function init (){
    var planet = document.getElementById ("greenplanet")
    planet.innerHTML="Red Alert: hit by..."
var botonTxto = document.getElementById("botonCambiarTexto")
botonTxto.addEventListener("click", modificarRePlanet)
}

function modificarRePlanet(){
    var planet = document.getElementById ("greenplanet")
    planet.innerHTML="Red Alert: hit by..."
}

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
