#!/usr/bin/env python3
"""Calculate weighted manuscript scorecards from dimension scores."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple


DEFAULT_WEIGHTS = {
    "problem_formulation": 0.15,
    "literature_review": 0.15,
    "methodology": 0.20,
    "data_collection": 0.10,
    "analysis": 0.15,
    "results": 0.10,
    "writing": 0.10,
    "citations": 0.05,
}

QUALITY_LEVELS = {
    (4.5, 5.0): ("Exceptional", "Close to top-tier submission readiness"),
    (4.0, 4.49): ("Strong", "Minor revisions likely sufficient"),
    (3.5, 3.99): ("Good", "Promising, but major revisions remain"),
    (3.0, 3.49): ("Acceptable", "Significant revision required"),
    (2.0, 2.99): ("Weak", "Major rework needed"),
    (0.0, 1.99): ("Poor", "Not ready for submission"),
}


def load_json(path: Path) -> Dict[str, float]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    for key, value in data.items():
        if not 1 <= float(value) <= 5:
            raise ValueError(f"Score for {key} must be between 1 and 5, got {value}")
    return {str(k): float(v) for k, v in data.items()}


def weighted_average(scores: Dict[str, float], weights: Dict[str, float]) -> float:
    total_score = 0.0
    total_weight = 0.0
    for dimension, score in scores.items():
        norm = dimension.replace("-", "_").lower()
        weight = weights.get(norm, 0.0)
        total_score += score * weight
        total_weight += weight
    if total_weight == 0:
        return 0.0
    return total_score / total_weight


def quality_level(score: float) -> Tuple[str, str]:
    for (low, high), label in QUALITY_LEVELS.items():
        if low <= score <= high:
            return label
    return ("Unknown", "Score out of range")


def strengths_and_weaknesses(scores: Dict[str, float]) -> Tuple[list[str], list[str]]:
    ordered = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    strengths = [dim for dim, score in ordered[:3] if score >= 4.0]
    weaknesses = [dim for dim, score in ordered[-3:] if score < 3.5]
    return strengths, weaknesses


def bar_chart(scores: Dict[str, float], width: int = 40) -> str:
    max_name = max(len(name) for name in scores)
    lines = []
    for dimension, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        size = int((score / 5.0) * width)
        lines.append(f"{dimension:<{max_name}} | {'#' * size} {score:.2f}")
    return "\n".join(lines)


def render_report(scores: Dict[str, float], weights: Dict[str, float]) -> str:
    overall = weighted_average(scores, weights)
    level, desc = quality_level(overall)
    strengths, weaknesses = strengths_and_weaknesses(scores)

    lines = [
        "=" * 68,
        "MANUSCRIPT SCORECARD",
        "=" * 68,
        "",
        f"Overall Score: {overall:.2f} / 5.00",
        f"Quality Level: {level}",
        f"Assessment: {desc}",
        "",
        "Dimension Scores",
        "-" * 68,
        bar_chart(scores),
        "",
        "Weighted Breakdown",
        "-" * 68,
    ]

    for dimension, score in sorted(scores.items()):
        weight = weights.get(dimension.replace("-", "_").lower(), 0.0)
        lines.append(f"{dimension:22s} {score:.2f}/5.00  weight={weight * 100:4.1f}%")

    if strengths:
        lines.extend(["", "Top Strengths"])
        lines.extend([f"- {name}: {scores[name]:.2f}" for name in strengths])

    if weaknesses:
        lines.extend(["", "Priority Weaknesses"])
        lines.extend([f"- {name}: {scores[name]:.2f}" for name in weaknesses])

    lines.extend(["", "=" * 68])
    return "\n".join(lines)


def interactive_scores() -> Dict[str, float]:
    scores: Dict[str, float] = {}
    for dimension in DEFAULT_WEIGHTS:
        while True:
            raw = input(f"{dimension.replace('_', ' ').title()} (1-5, blank to skip): ").strip()
            if not raw:
                break
            try:
                value = float(raw)
            except ValueError:
                print("Enter a number between 1 and 5.")
                continue
            if not 1 <= value <= 5:
                print("Enter a number between 1 and 5.")
                continue
            scores[dimension] = value
            break
    return scores


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate a weighted manuscript scorecard.")
    parser.add_argument("--scores", type=Path, help="JSON file containing dimension scores")
    parser.add_argument("--weights", type=Path, help="Optional JSON file with custom weights")
    parser.add_argument("--output", type=Path, help="Optional output report path")
    parser.add_argument("--interactive", action="store_true", help="Enter scores interactively")
    args = parser.parse_args()

    try:
        if args.interactive:
            scores = interactive_scores()
            if not scores:
                print("No scores entered.")
                return
        else:
            if not args.scores:
                parser.error("--scores is required unless --interactive is used")
            scores = load_json(args.scores)

        weights = load_json(args.weights) if args.weights else DEFAULT_WEIGHTS
        report = render_report(scores, weights)

        if args.output:
            args.output.write_text(report, encoding="utf-8")
        else:
            print(report)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
