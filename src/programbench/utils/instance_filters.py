import re


def filter_instances(ids: list[str], filter_spec: str = "", slice_spec: str = "") -> list[str]:
    if filter_spec:
        ids = [i for i in ids if re.match(filter_spec, i)]
    if slice_spec:
        parts = [int(p) if p else None for p in slice_spec.split(":")]
        ids = ids[slice(*parts)]
    return ids
