class List extends HTMLElement {
    constructor(){
        super();

        let shadow = this.attachShadow({mode:"open"})
        this.divHeader = document.createElement ("div")
        this.divHeader.innerHTML= "Hola";

        shadow.appendChild (this.divHeader)
    }
}

customElements.define ("menu",List);