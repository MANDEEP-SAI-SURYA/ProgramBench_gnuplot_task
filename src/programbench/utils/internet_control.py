"""Run compile.sh without network access (upstream blackholes DNS inside the container).

Locally we use an unprivileged network namespace (`unshare -rn`) when the kernel allows it.
"""
import shutil
import subprocess


def no_network_prefix() -> list[str]:
    if shutil.which("unshare") and subprocess.run(["unshare", "-rn", "true"], capture_output=True).returncode == 0:
        return ["unshare", "-rn"]
    return []
