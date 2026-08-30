from ..domain.models import Element, Norm, Result

class Validator:
    def validate(self, result: Result, norms: dict[str, Norm], elements: dict[str, Element]) -> Result:
        if not result.norms_used:
            result.uncertainties.append("No se registraron normas utilizadas en el resultado.")
        for norm_id in result.norms_used:
            norm = norms.get(norm_id)
            if not norm:
                result.uncertainties.append(f"Norma no recuperable: {norm_id}")
            elif norm.validity.lower() not in {"vigente", "active", "activa"}:
                result.uncertainties.append(f"Vigencia a revisar: {norm_id}")
        for element_id in result.fundamentals:
            if element_id not in elements:
                result.uncertainties.append(f"Elemento no recuperable: {element_id}")
        if result.uncertainties:
            result.status = "requiere_validacion"
        return result
      
