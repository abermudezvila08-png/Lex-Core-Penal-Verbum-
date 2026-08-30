from ...domain.models import Element, ElementState, Fact, FactState, Norm, Rule

def demo_case():
    norm = Norm(
        id="DL91-2024-A12-H",
        norm_type="Decreto-Ley",
        issuer="Estado cubano",
        date="2024",
        validity="vigente-a-verificar",
        version="2024",
        jurisdiction="Cuba",
        text="Conducta laboral referida en el Archivo Maestro de Continuidad.",
        articles=("12-H",),
    )
    facts = {
        "F1": Fact("F1", "Se afirma que una persona fue empleada sin contrato de trabajo.", "sujeto-01", state=FactState.AFFIRMED, source_id="E1")
    }
    elements = {
        "EL1": Element("EL1", "Existencia de relación de trabajo.", "sujeto/relación", norm.id, ElementState.SATISFIED, ("F1",), ("E1",)),
        "EL2": Element("EL2", "Ausencia de contrato conforme a la legislación laboral vigente.", "conducta", norm.id, ElementState.PARTIAL, ("F1",), ("E1",)),
    }
    rule = Rule(
        id="R-DL91-12H",
        name="Correspondencia de conducta laboral",
        description="Evalúa los elementos declarados por el supuesto normativo.",
        required_elements=("EL1", "EL2"),
        consequence="La conducta es jurídicamente compatible con la hipótesis normativa, sujeta a validación de todos los elementos y vigencia.",
    )
    return {norm.id: norm}, facts, elements, rule
  
