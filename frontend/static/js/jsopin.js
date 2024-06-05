function mostrarPopup() {
    document.getElementById('popup_overlay').style.display = 'block';
    document.getElementById('success_message').style.display = 'block';
}

function cerrarPopup() {
    document.getElementById('popup_overlay').style.display = 'none';
    document.getElementById('success_message').style.display = 'none';
}

document.getElementById('form_opinion').addEventListener('submit', function(event) {
    event.preventDefault();

    mostrarPopup();
});
