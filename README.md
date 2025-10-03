# Deep Learning and Financial Sentiment Forecasting (MSc 2025)

Private research repository for my Kingston University MSc dissertation.  
Scope: Benchmark ARIMA, ARIMAX, LSTM (price-only), LSTM (Sentiment-Enhanced), Transformer (Sentiment-Enhanced), and a Hybrid model on five tickers (AAPL, AMZN, MSFT, TSLA, AMD).  
All models share fixed splits, identical inputs where applicable, and a leakage-safe protocol.

## Data windows and target
- Train: 2021-02-03 → 2022-12-30
- Val:   2023-01-03 → 2023-05-31
- Test:  2023-06-01 → 2023-12-28 (n = 146)
- Target: next-day Close (Close.shift(-1)) created after features

## Reproducibility
See `env_manifest.txt`, `file_hashes.json`, `code_provenance.csv`, `dataset_provenance.csv`, and `third_party_licenses/`.  
Deep models use train-only scaling and record seeds, parameter counts, and monthly refit cadence.

## Structure
See the top-level tree in this README. Notebooks are under `notebooks/`, reusable code under `src/`, and per-model outputs under `models/`.

## Licence
See `LICENSE`. Third-party licences are mirrored under `third_party_licenses/`.

## Quick start

1) Create a Python 3.12 virtual environment:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2) Install dependencies:
   pip install -r requirements.txt

3) Snapshot the environment and provenance:
   python scripts\capture_env.py
   python scripts\build_provenance.py
   python scripts\hash_artifacts.py

4) Run models (examples):
   python src\arima\runner.py
   python src\arimax\runner.py
   python src\transformer\runner.py
   # (see notebooks/ and src/ for full usage)
