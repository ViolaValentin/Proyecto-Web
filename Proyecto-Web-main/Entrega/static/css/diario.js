document.addEventListener('DOMContentLoaded', function() {
    const card = document.getElementById('card');
    const imageContainer = document.getElementById('image-container');
    const image = document.getElementById('image');
    const nombre = document.getElementById('nombre');
    const descuento = document.getElementById('descuento');
    const link = document.getElementById('link');

    const imagenes = [
        {"idDescuento": 1, "imagen": "https://th.bing.com/th/id/R.7aa2ed0bc6e8caec4559150bdded9f1d?rik=qgPckyM1RzxCFA&riu=http%3a%2f%2fturronessirvent.com%2fwp-content%2fuploads%2f2016%2f01%2fhelados.jpg&ehk=Gl%2bXdl1SP9UiQ1bcL9smnn6GHgKijfbC%2fYFyc4vrCFs%3d&risl=&pid=ImgRaw&r=0", "nombre": "Grido helados", "Descuento": "El descuento es del 25%", "categoria":"comida", "link":"https://chilepedidos.gridohelado.com/pedir/65WceKrkoGW5GuKfP/1-kilo-helado"},
        {"idDescuento": 2, "imagen": "https://www.totalmedios.com/img/noticias/2019/07/5d3848bf676c0__838x390.jpg", "nombre": "GARBARINO", "Descuento": "Ahorra un 30% con este descuento", "categoria":"tecnologia","link":"https://www.nike.com.ar/"},
        {"idDescuento": 3, "imagen": "https://c.static-nike.com/a/images/w_1920,c_limit/bzl2wmsfh7kgdkufrrjq/image.jpg", "nombre": "NIKE", "Descuento": "Obtén un 10% de descuento", "categoria":"deportes","link":"https://www.garbarino.com/"},
        {"idDescuento": 4, "imagen": "https://staticclvf5a.lavozdelinterior.com.ar/files/promociones/miniatura_270x160_-_hoyts.jpg", "nombre": "CINE HOYTS", "Descuento": "¡Compra ahora y ahorra un 15%", "categoria":"multimedia","link":"https://www.cinemarkhoyts.com.ar/"},
        {"idDescuento": 6, "imagen": "https://traviesospetshop.com.ar/wp-content/uploads/2020/10/Purina-proplan-logo-transparente.png", "nombre": "PRO PLAN", "Descuento": "Aprovecha el 20% de descuento", "categoria":"mascotas","link":"https://www.purina.com.ar/proplan"},
        {"idDescuento": 7, "imagen": "https://www.comeros.com.ar/wp-content/uploads/2021/11/jbl-logo-6-1.png", "nombre": "JBL", "Descuento": "Consigue un descuento del 12%", "categoria":"musica","link":"https://www.jbl.com/"},
    ];

    card.addEventListener('click', () => {
        const imagenAleatoria = obtenerImagenAleatoria(imagenes);
        image.src = imagenAleatoria.imagen;
        nombre.textContent = imagenAleatoria.nombre;
        descuento.textContent = imagenAleatoria.Descuento;
        link.textContent = imagenAleatoria.link;
        imageContainer.style.display = 'block';
    });

    imageContainer.addEventListener('click', () => {
        imageContainer.style.display = 'none';
    });

    function obtenerImagenAleatoria(imagenesArray) {
        const indiceAleatorio = Math.floor(Math.random() * imagenesArray.length);
        return imagenesArray[indiceAleatorio];
    }
});

