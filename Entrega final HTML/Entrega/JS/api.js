document.addEventListener("DOMContentLoaded", function () {
    let dolarElement = document.getElementById("boton-descuento-individual1");
    let resultadoElement = document.getElementById("resultado");

    let precioEnPesos = parseFloat(dolarElement.textContent.replace("$", ""));
    
    fetch("https://dolarapi.com/v1/dolares/blue")
        .then(response => response.json())
        .then(data => {
            let precioDolarBlue = data.venta;
            let resultado = 0.3 * precioDolarBlue;
            resultadoElement.textContent = `$${resultado.toFixed(2)}`;
        })
        .catch(error => {
            console.error("Error al obtener el precio del dólar:", error);
            resultadoElement.textContent = "Error al obtener el precio del dólar";
        });
});