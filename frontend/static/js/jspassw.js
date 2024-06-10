const passwordField = document.querySelector('input[name="contra"]');
const toggleButton = document.getElementById('togglePassword');

toggleButton.addEventListener('click', function() {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.textContent = type === 'password' ? 'Mostrar' : 'Ocultar';
});