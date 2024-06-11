function mostrarPopup() {
    document.getElementById('popup_overlay').style.display = 'block';
    document.getElementById('success_message').style.display = 'block';
}

function cerrarPopup() {
    document.getElementById('popup_overlay').style.display = 'none';
    document.getElementById('success_message').style.display = 'none';
}

window.addEventListener('load', function() {
    mostrarPopup();
});

function openModal() {
    var modal = document.getElementById("authModal");
    modal.style.display = "block";
}

function closeModal() {
    var modal = document.getElementById("authModal");
    modal.style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById("authModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
