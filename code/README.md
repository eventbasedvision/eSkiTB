# Code layout

This folder mirrors the minimal hooks used in the paper. Add your actual scripts/configs here.

- evaluation/: entry point to compute metrics on event tracking sequences.
- visualization/: quick plots and overlays for events + boxes.
- generation/: configs or wrappers for converting RGB to events (e.g., v2e settings).

## Suggested quickstart
```
python evaluation/evaluate.py \
  --split ../../data/splits/val.txt \
  --annotations ../../data/annotations/example.json \
  --data-root ../../data/raw
```

## Dependencies
List your exact runtime dependencies in `requirements.txt` at the repo root (to be added). Typical stack: numpy, torch, opencv-python, h5py, matplotlib.
