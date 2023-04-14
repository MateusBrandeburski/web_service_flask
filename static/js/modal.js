
$(document).ready(function(){
    $('[data-bs-toggle="tooltip"]').tooltip();  // ativa o tooltip
    $(".abre-sidebar").hover(function(){     // exibe a sidebar quando passar o mouse sobre o elemento que contém a classe "abre-sidebar"
      $("#exampleModal").modal("show");
    });
    
    $("body").click(function(event){    // fecha a sidebar quando clicar em qualquer lugar da página
        var target = $(event.target);
        if(!target.closest("#exampleModal").length && !target.hasClass("abre-sidebar")) {
          $("#exampleModal").modal("hide");
        }
      });
  });
