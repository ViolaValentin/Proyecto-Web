function inicializarBusquedaPalabrasClave(){
    const palabrasClave = [
        { nombre: "GRIDO", url: "http://127.0.0.1:5000/descuentos/1"},
        { nombre: "GRIDO HELADOS", url: "http://127.0.0.1:5000/descuentos/1"},
        { nombre: "GARBARINO", url: "http://127.0.0.1:5000/descuentos/2"},
        { nombre: "NIKE", url: "http://127.0.0.1:5000/descuentos/3"},
        { nombre: "CINE HOYTS", url: "http://127.0.0.1:5000/descuentos/4"},
        { nombre: "DESPEGAR", url: "http://127.0.0.1:5000/descuentos/5"},
        { nombre: "PRO PLAN", url: "http://127.0.0.1:5000/descuentos/6"},
        { nombre: "JBL", url: "http://127.0.0.1:5000/descuentos/7"},
        { nombre: "McDonalds", url: "http://127.0.0.1:5000/descuentos/8"},            
        {nombre: "SONY", url:"http://127.0.0.1:5000/descuentos/9"},
        { nombre: "ADIDAS", url: "http://127.0.0.1:5000/descuentos/10"},
        { nombre: "APPLE TV", url: "http://127.0.0.1:5000/descuentos/11"},
        { nombre: "BOOKING", url: "http://127.0.0.1:5000/descuentos/12"},
        { nombre: "DogChow", url: "http://127.0.0.1:5000/descuentos/13"},
        { nombre: "BOSE", url: "http://127.0.0.1:5000/descuentos/14"},
    ];
    
    function buscarPalabraClave(palabra) {
        for (const keyword of palabrasClave) {
            if (palabra.toLowerCase() === keyword.nombre.toLowerCase()) {
                window.location.href = keyword.url;
                return;
            }
        }
        alert("No se han encontrado resultados para tu búsqueda");
    }
    
    const inputSearch = document.getElementById("inputSearch");
    const searchIcon = document.getElementById("searchIcon");
    
    searchIcon.addEventListener("click", function() {
        const searchText = inputSearch.value.trim();
    
        if (searchText !== "") {
            buscarPalabraClave(searchText);
        }
    });
    
    inputSearch.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            const searchText = inputSearch.value.trim();
    
            if (searchText !== "") {
                buscarPalabraClave(searchText);
            }
        }
    });
}
