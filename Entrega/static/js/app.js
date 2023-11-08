const app = new Vue({
    el: '#app',
    data: {
        descuentos: []
    },
    methods: {
        fetchDescuentos() {
            fetch('/api/descuentos')
                .then(response => response.json())
                .then(data => {
                    this.descuentos = data;
                });
        }
    }
});

var appVue2 = new Vue ({
    el: '#app',
    data:{
        miHTML:'<h1>Hola</h1>'
    }
})

