from ..domain.models import Element, ElementState, Result, Rule

class RuleEngine:
    def evaluate(self, rule: Rule, elements: dict[str, Element]) -> Result:
        missing = []
        disputed = []
        partial = []
        used = []
        for element_id in rule.required_elements:
            element = elements.get(element_id)
            if not element:
                missing.append(element_id)
                continue
            used.append(element_id)
            if element.state == ElementState.SATISFIED:
                continue
            if element.state == ElementState.DISPUTED:
                disputed.append(element_id)
            elif element.state == ElementState.PARTIAL:
                partial.append(element_id)
            else:
                missing.append(element_id)

        if not missing and not disputed and not partial:
            status = "compatible"
            conclusion = rule.consequence
        else:
            status = "no_concluyente"
            conclusion = "No procede una conclusión jurídica definitiva con los elementos actualmente acreditados."

        uncertainties = [f"Elemento pendiente: {x}" for x in missing]
        uncertainties += [f"Elemento controvertido: {x}" for x in disputed]
        uncertainties += [f"Elemento parcialmente acreditado: {x}" for x in partial]
        return Result(
            conclusion=conclusion,
            fundamentals=used,
            rules_executed=[rule.id],
            uncertainties=uncertainties,
            status=status,
          )
      
