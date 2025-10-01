import json, hashlib, pathlib

root = pathlib.Path(".")
targets = []
targets += list(root.glob("models/**/predictions_*.csv"))
targets += list(root.glob("models/**/metrics_*.json"))
targets += list(root.glob("models/**/run_config_*.json"))

out = {}
for fp in sorted(set(targets)):
    h = hashlib.sha256(fp.read_bytes()).hexdigest()
    out[str(fp)] = {"sha256": h, "bytes": fp.stat().st_size}

pathlib.Path("file_hashes.json").write_text(json.dumps(out, indent=2))
print(f"Wrote file_hashes.json with {len(out)} entries")
