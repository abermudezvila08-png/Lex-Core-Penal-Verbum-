from dataclasses import dataclass, field
from uuid import uuid4
from ..domain.models import Element, Norm, Rule, Result
from ..reasoning.engine import RuleEngine
from ..validation.validator import Validator

@dataclass
class Execution:
    task_id: str
    correlation_id: str
    events: list[dict] = field(default_factory=list)

class LegalPipeline:
    def __init__(self):
        self.engine = RuleEngine()
        self.validator = Validator()

    def run(self, task: str, rule: Rule, elements: dict[str, Element], norms: dict[str, Norm], norm_ids: list[str]) -> tuple[Execution, Result]:
        correlation = str(uuid4())
        execution = Execution(str(uuid4()), correlation)
        execution.events.append({"type": "TASK", "task": task})
        execution.events.append({"type": "CLASSIFY", "domain": "juridico"})
        execution.events.append({"type": "REASON", "rule": rule.id})
        result = self.engine.evaluate(rule, elements)
        result.norms_used = norm_ids
        result.trace = execution.events.copy()
        execution.events.append({"type": "VALIDATE"})
        result = self.validator.validate(result, norms, elements)
        execution.events.append({"type": "RESULT", "status": result.status})
        result.trace = execution.events.copy()
        return execution, result

