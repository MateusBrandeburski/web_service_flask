from flask import Blueprint, request, render_template
from classes.formula_pitagoras import TeoremaDePitagoras


calcularora_query = Blueprint('calculadora_query', __name__, template_folder='templates')


@calcularora_query.route("/teorema_de_pitagoras", methods=["GET"])  # type: ignore
def query_teorema():
    """Como funciona essa rota:
    O aplicativo está sendo desenvolvido usando POO, por isso, os parâmetros são passado na instância da classe TeoremaDePitagoras. 

    O round, dentro do return, serve para limitar o número de casa decimais. Sendo que 2, correponde == 2.22. Se tivesse 3, correponderia == 3.333
    """     
    hipotenusa = request.args.get("hipotenusa")
    catetoA = request.args.get("catetoA")
    catetoO = request.args.get("catetoO") 
     
    try:
        
        if (catetoA and hipotenusa) or (catetoO and hipotenusa): 
            teorema = TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO, hipotenusa=hipotenusa)  # type: ignore
            return render_template('resposta_query.html', name=teorema.strings_teorema(name="cateto"), resposta=teorema.calcular_catetos())
        
        elif catetoA and catetoO:      
            teorema = TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO)    # type: ignore
                
            return render_template('resposta_query.html', name=teorema.strings_teorema(name="hipotenusa"), resposta=teorema.calcular_hipotenusa())  
                
    except TypeError:
      return {"204":"no_content", "query":"faltam_parametros"}
  
    except ValueError:
        return {"400":"bod_request", "number":"apenas_float_e_int_suportados"}