
// scripts_modal2.js
document.addEventListener("DOMContentLoaded", function() {
  var modal = document.getElementById("myModal_2");
  
  if (modal) {
      var closeButton = modal.querySelector(".close");
      
      if (closeButton) {
          closeButton.onclick = function() {
              modal.style.display = "none";
          };

          window.onclick = function(event) {
              if (event.target == modal) {
                  modal.style.display = "none";
              }
          };
      }

      window.showModal2 = function(title, content, publicPrice, loggedPrice, stock) {
          var modalTitle = modal.querySelector("#modal-title-2");
          var modalContent = modal.querySelector("#modal-content-2");
          var modalPublicPrice = modal.querySelector("#modal-preciop-2");
          var modalLoggedPrice = modal.querySelector("#modal-preciolog-2");
          var modalStock = modal.querySelector("#modal-stock-2");

          if (modalTitle && modalContent && modalPublicPrice && modalLoggedPrice && modalStock) {
              modalTitle.textContent = title;
              modalContent.textContent = content;
              modalPublicPrice.textContent = "Precio público: $" + publicPrice;
              modalLoggedPrice.textContent = "Precio logueado: $" + loggedPrice;
              modalStock.textContent = "Stock: " + stock;
          }

          modal.style.display = "block";
      }
  }
});

