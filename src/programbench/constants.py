import os
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent.parent
TASKS_DIR = PACKAGE_ROOT / "data" / "tasks"
TEST_RUNS_DIR = PACKAGE_ROOT / "data" / "test_runs"
IMAGES_DIR = REPO_ROOT / "images"
SOURCES_DIR = REPO_ROOT / "sources"

# Local stand-in for the HuggingFace dataset programbench/ProgramBench-Tests
# (<instance_id>/tests/<branch>.tar.gz). Same env var as upstream.
BLOB_DIR = Path(os.environ.get("PROGRAMBENCH_BLOB_DIR") or REPO_ROOT / "blobs")

TASK_YAML = "task.yaml"
TESTS_JSON = "tests.json"
WORKSPACE_DIR = "/workspace"

DOCKER_EXECUTABLE = os.environ.get("PROGRAMBENCH_DOCKER_EXECUTABLE", "docker")
DOCKER_ORG = os.environ.get("PROGRAMBENCH_DOCKER_ORG", "programbench")
CLEANROOM_TAG = "task_cleanroom_v6"
TASK_TAG = "task_v6"

COMPILE_TIMEOUT = int(os.environ.get("PROGRAMBENCH_COMPILE_TIMEOUT", "1800"))
BRANCH_TIMEOUT = int(os.environ.get("PROGRAMBENCH_BRANCH_TIMEOUT", "3600"))


def image_name_from_instance_id(instance_id: str) -> str:
    return f"{DOCKER_ORG}/{instance_id.replace('__', '_1776_')}"
