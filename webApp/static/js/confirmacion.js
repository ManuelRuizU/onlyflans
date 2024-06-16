
  // Obtener el modal
  var modal = document.getElementById('confirmationModal');

  // Mostrar el modal si se ha establecido un mensaje de confirmación en la sesión del usuario
  {% if messages %}
    var messages = "{{ messages }}";
    if (messages.includes("¡Gracias por tu contacto!")) {
      modal.style.display = "block";
      // Cerrar el modal después de 5 segundos
      setTimeout(function(){
        modal.style.display = "none";
      }, 5000); // Cambia 5000 a la cantidad de milisegundos que desees que el modal permanezca abierto
    }
  {% endif %}

  // Cerrar el modal cuando se haga clic en el botón de cerrar
  var closeButton = document.getElementsByClassName("close")[0];
  closeButton.onclick = function() {
    modal.style.display = "none";
  }

  // Cerrar el modal cuando se haga clic fuera del modal
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }

