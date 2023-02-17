from flask import Blueprint, request
from classes.formula_pitagoras import TeoremaDePitagoras


calcularora_query = Blueprint('calculadora_query', __name__)


@calcularora_query.route("/teorema_de_pitagoras", methods=["GET"])
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
            teorema = TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO,hipotenusa=hipotenusa)
            return { "Cateto": round(teorema.calcular_catetos(), 2) }
        
        elif catetoA and catetoO:      
            teorema = TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO)       
            return { "Hipotenusa": round(teorema.calcular_hipotenusa(), 2)}
      
    except TypeError:
      return {"204":"no_content", "query":"faltam_parametros"}
  
    except ValueError:
        return {"400":"bod_request", "number":"apenas_float_e_int_suportados"}