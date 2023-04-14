
function closeNav() {
    document.querySelector('.navbar-collapse').classList.remove('show');
  }
  
$(document).ready(function(){
    $('[data-bs-toggle="tooltip"]').tooltip();  // ativa o tooltip
    $(".abre-sidebar").hover(function(){     // exibe a sidebar quando passar o mouse sobre o elemento que contém a classe "abre-sidebar"
      $("#exampleModal").modal("show");
    });
  });
