import platform, sys, json, pathlib, subprocess

out = {
    "os": platform.platform(),
    "python": sys.version.split()[0],
    "machine": platform.machine(),
    "processor": platform.processor(),
}

# Optional: Torch/CUDA info
try:
    import torch
    out["torch"] = torch.__version__
    out["cuda_available"] = torch.cuda.is_available()
    if torch.cuda.is_available():
        out["cuda_device"] = torch.cuda.get_device_name(0)
except Exception:
    pass

def git(cmd):
    try:
        return subprocess.check_output(["git"] + cmd, text=True).strip()
    except Exception:
        return None

out["git_branch"] = git(["rev-parse", "--abbrev-ref", "HEAD"])
out["git_commit"] = git(["rev-parse", "HEAD"])
out["git_remote"] = git(["config", "--get", "remote.origin.url"])

pathlib.Path("env_manifest.txt").write_text(
    "\n".join(f"{k}: {v}" for k, v in out.items() if v is not None)
)
print("Wrote env_manifest.txt")
