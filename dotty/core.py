from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Optional
from .config import DottyConfig

CITATION_PATTERN = re.compile(r"\b(C\.R\.S\.|C\.R\.C\.P\.|D\.C\.COLO\.LCivR|U\.S\.C\.)\b.*?\d")

EMOTIONAL_MARKERS = [
    "unfair", "hurt", "lied", "betrayed", "cruel", "disrespected", "angry", "devastated",
    "gaslit", "traumatized", "abusive", "harassed"
]

@dataclass
class DottyResult:
    status: str
    message: str
    suggestion: Optional[str] = None

class Dotty:
    def __init__(self, config: Optional[DottyConfig] = None):
        self.config = config or DottyConfig()

    def _has_citation(self, text: str) -> bool:
        return bool(CITATION_PATTERN.search(text))

    def _has_emotional_language(self, text: str) -> bool:
        t = text.lower()
        return any(marker in t for marker in EMOTIONAL_MARKERS)

    def analyze(self, text: str) -> DottyResult:
        text = text.strip()
        if not text:
            return DottyResult(
                status="invalid",
                message="Input is empty.",
                suggestion="State the legally relevant facts or question."
            )

        if self._has_citation(text):
            return DottyResult(
                status="citation_provided",
                message="Citation detected. Validate against approved sources.",
                suggestion="Confirm text and updates using the Colorado Revised Statutes or applicable court rules."
            )

        if self._has_emotional_language(text):
            return DottyResult(
                status="emotional",
                message="Emotional language detected. Reframe into fact- and pattern-based statements.",
                suggestion="Identify dates, actors, actions, and attach exhibits. Then connect to a statute or rule."
            )

        return DottyResult(
            status="unsupported",
            message="No statute, rule, or evidence detected.",
            suggestion="Add a controlling statute or rule (e.g., C.R.S. § [title-article-section]) or attach admissible evidence."
        )

    def format_response(self, result: DottyResult) -> str:
        # Output style: relevance -> reference -> next step; concise; no emotional validation.
        lines: list[str] = []
        if result.status == "citation_provided":
            lines.append("Status: Citation detected; proceed to validation.")
        elif result.status == "emotional":
            lines.append("Status: Emotional phrasing present; convert to fact pattern.")
        elif result.status == "unsupported":
            lines.append("Status: Unsupported assertion; add legal authority or evidence.")
        else:
            lines.append(f"Status: {result.status}.")

        if result.message:
            lines.append(f"Analysis: {result.message}")

        if result.suggestion:
            lines.append(f"Next step: {result.suggestion}")

        return "\n".join(lines)
