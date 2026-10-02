from pathlib import Path

from programbench.constants import BLOB_DIR


def get_blob_dir(instance_id: str) -> Path | None:
    """Local layout identical to the HF dataset: <BLOB_DIR>/<instance_id>/tests/<branch>.tar.gz."""
    d = BLOB_DIR / instance_id
    return d if d.exists() else None
