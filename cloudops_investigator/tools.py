"""Read-only tools for loading CloudOps investigation data.

The first version reads local mock files. Later, these same function names can
be backed by AWS, Kubernetes, Prometheus, or log platform integrations.
"""

from __future__ import annotations

import json
from pathlib import Path


DEFAULT_DATA_DIR = Path("mock_data")


def _safe_data_path(data_dir: Path, *parts: str) -> Path:
    """Build a path inside the configured data directory."""
    base = data_dir.resolve()
    target = base.joinpath(*parts).resolve()
    if base != target and base not in target.parents:
        raise ValueError(f"Refusing to read outside data directory: {target}")
    return target


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def get_incident(incident_id: str, data_dir: Path | str = DEFAULT_DATA_DIR) -> dict:
    """Read one incident description by incident file name."""
    data_path = Path(data_dir)
    path = _safe_data_path(data_path, "incidents", f"{incident_id}.json")
    return _read_json(path)


def get_logs(service_name: str, data_dir: Path | str = DEFAULT_DATA_DIR) -> list[str]:
    """Read log lines for a service."""
    data_path = Path(data_dir)
    path = _safe_data_path(data_path, "logs", f"{service_name}.log")
    return [line for line in _read_text(path).splitlines() if line.strip()]


def get_metrics(service_name: str, data_dir: Path | str = DEFAULT_DATA_DIR) -> dict:
    """Read metrics for a service."""
    data_path = Path(data_dir)
    path = _safe_data_path(data_path, "metrics", f"{service_name}.json")
    return _read_json(path)


def get_kubernetes_events(
    service_name: str, data_dir: Path | str = DEFAULT_DATA_DIR
) -> dict:
    """Read Kubernetes workload and event data for a service."""
    data_path = Path(data_dir)
    path = _safe_data_path(data_path, "kubernetes", f"{service_name}-events.json")
    return _read_json(path)


def search_runbooks(query: str, data_dir: Path | str = DEFAULT_DATA_DIR) -> list[dict]:
    """Search runbook files using simple keyword matching."""
    data_path = Path(data_dir)
    runbooks_dir = _safe_data_path(data_path, "runbooks")
    query_terms = [term.lower() for term in query.split() if len(term) > 2]
    matches: list[dict] = []

    for path in sorted(runbooks_dir.glob("*.md")):
        content = _read_text(path)
        lower_content = content.lower()
        score = sum(1 for term in query_terms if term in lower_content)
        if score > 0:
            matches.append(
                {
                    "title": _extract_title(content, path.stem),
                    "path": str(path),
                    "score": score,
                    "content": content,
                }
            )

    return sorted(matches, key=lambda item: item["score"], reverse=True)


def _extract_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return fallback
