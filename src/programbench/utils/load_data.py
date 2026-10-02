import json
from pathlib import Path

from programbench.constants import TASK_YAML, TASKS_DIR, TESTS_JSON, image_name_from_instance_id


def _read_yaml(path: Path) -> dict:
    try:
        import yaml

        return yaml.safe_load(path.read_text())
    except ImportError:  # tiny fallback for the flat task.yaml schema (scalars and lists of scalars)
        data: dict = {}
        key = None
        for raw in path.read_text().splitlines():
            line = raw.split(" #")[0].rstrip()
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.startswith("- ") or line.startswith("  - "):
                data[key].append(line.split("- ", 1)[1].strip())
            elif ":" in line:
                key, val = (s.strip() for s in line.split(":", 1))
                data[key] = val if val else []
        return data


def load_instance(instance_id: str, tasks_dir: Path = TASKS_DIR) -> dict:
    task_dir = tasks_dir / instance_id
    inst = {**_read_yaml(task_dir / TASK_YAML), "instance_id": instance_id,
            "image_name": image_name_from_instance_id(instance_id)}
    tests = task_dir / TESTS_JSON
    inst.update(json.loads(tests.read_text()) if tests.exists() else {"branches": {}})
    return inst


def load_all_instances(tasks_dir: Path = TASKS_DIR) -> dict[str, dict]:
    return {d.name: load_instance(d.name, tasks_dir) for d in sorted(tasks_dir.iterdir()) if (d / TASK_YAML).exists()}


def get_active_branches(inst: dict) -> list[str]:
    return [b for b, info in inst["branches"].items() if not info.get("ignored")]


def get_ignored_tests(inst: dict) -> set[str]:
    return {f"{b}/{t['name']}" for b, info in inst["branches"].items() for t in info.get("ignored_tests") or []}
