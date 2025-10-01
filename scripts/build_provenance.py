import csv

# Seed with what we know now. Update commit_shas once you pin them.
code_rows = [
    {"component":"transformer/runner.py","provenance":"Adapted",
     "source_repo":"oliverguhr/transformer-time-series-prediction",
     "commit_sha":"","license":"MIT"},
    {"component":"lstm/trainer.py","provenance":"Adapted",
     "source_repo":"jinglescode/time-series-forecasting-pytorch",
     "commit_sha":"","license":"Apache-2.0"},
]

with open("code_provenance.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=["component","provenance","source_repo","commit_sha","license"])
    w.writeheader(); w.writerows(code_rows)

with open("dataset_provenance.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=["artifact","source","time_window","notes"])
    w.writeheader()
    w.writerow({
        "artifact":"data/final_inputs/TSLA_input.csv",
        "source":"internal pipeline",
        "time_window":"2021-01-01→2023-12-31",
        "notes":"engineered technicals + sentiment; Target = Close.shift(-1)"
    })

print("Wrote code_provenance.csv and dataset_provenance.csv")
