from dataclasses import dataclass, field
from enum import Enum
from typing import Any

class FactState(str, Enum):
    AFFIRMED = "afirmado"
    PROVEN = "probado"
    DISPUTED = "controvertido"
    UNKNOWN = "desconocido"

class ElementState(str, Enum):
    SATISFIED = "satisfecho"
    NOT_SATISFIED = "no_satisfecho"
    PARTIAL = "parcialmente_acreditado"
    DISPUTED = "controvertido"
    UNKNOWN = "desconocido"

@dataclass(frozen=True)
class Norm:
    id: str
    norm_type: str
    issuer: str
    date: str
    validity: str
    version: str
    jurisdiction: str
    text: str
    articles: tuple[str, ...] = ()
    relations: tuple[str, ...] = ()

@dataclass(frozen=True)
class Fact:
    id: str
    description: str
    subject: str
    date: str | None = None
    place: str | None = None
    state: FactState = FactState.AFFIRMED
    source_id: str | None = None

@dataclass(frozen=True)
class Evidence:
    id: str
    kind: str
    origin: str
    description: str
    validation: str = "pendiente"
    strength: str = "no_determinada"

@dataclass(frozen=True)
class Element:
    id: str
    description: str
    category: str
    required_by: str
    state: ElementState = ElementState.UNKNOWN
    supporting_facts: tuple[str, ...] = ()
    supporting_evidence: tuple[str, ...] = ()

@dataclass(frozen=True)
class Rule:
    id: str
    name: str
    description: str
    required_elements: tuple[str, ...]
    consequence: str

@dataclass
class Result:
    conclusion: str
    fundamentals: list[str] = field(default_factory=list)
    evidence_used: list[str] = field(default_factory=list)
    norms_used: list[str] = field(default_factory=list)
    rules_executed: list[str] = field(default_factory=list)
    uncertainties: list[str] = field(default_factory=list)
    trace: list[dict[str, Any]] = field(default_factory=list)
    status: str = "no_concluyente"

