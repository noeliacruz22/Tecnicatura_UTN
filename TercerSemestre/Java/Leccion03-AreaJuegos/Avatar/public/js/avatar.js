function seleccionarPersonajeJugador() {
    let mensaje = "No seleccionaste ningún personaje";

    if (document.getElementById("zuko").checked) {
        mensaje = "Seleccionaste a Zuko 🔥";
    } else if (document.getElementById("katara").checked) {
        mensaje = "Seleccionaste a Katara 💧";
    } else if (document.getElementById("aang").checked) {
        mensaje = "Seleccionaste a Aang 💨";
    } else if (document.getElementById("toph").checked) {
        mensaje = "Seleccionaste a Toph 🌱";
    }

    alert(mensaje);
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
