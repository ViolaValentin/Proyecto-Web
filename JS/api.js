import fetch from "fetch";
const url = "https://dolarapi.com/v1/dolares/blue";
const response = await fetch(url);
const body = await response.json();
const venta = body["venta"];
console.log(venta);

var precioCupon = 0.3 * venta;

let button = document.getElementById("boton-descuento-individual1");

button.innerHTML = precio