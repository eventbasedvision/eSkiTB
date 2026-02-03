# eSkiTB: Event-based Ski Tracking Benchmark

Camera-ready release scaffold for the eSkiTB paper. This repo is GitHub/Pages-friendly: metadata, splits, schema docs, tiny examples, and code pointers—no heavyweight data blobs.

## Project snapshot
- Paper: TODO (arXiv link)
- Website: docs/index.html (serve with GitHub Pages)
- Dataset links: TODO (Dropbox/Drive + MD5/SHA256)
- Videos: TODO (YouTube playlist)
- Code: evaluation + visualization hooks included here

## What is eSkiTB?
- 300 broadcast sequences (AL/FS/JP) at 1280x720; 235 minutes total.
- Train/val/test = 240/30/30 sequences.
- Synthetic events from SkiTB via v2e under an **iso-informational** constraint (no neural interpolation or SuperSloMo).
- Event tuples `(t, x, y, p)` in HDF5; bounding boxes for `Skier` with 1 ms spline-interpolated dense labels.
- Attributes: 10 visual conditions (occlusion, fast motion, illumination variation, etc.).

## Key findings (paper)
- STARK (RGB transformer, fine-tuned): 0.795 IoU; ski-specific: 0.829 IoU.
- SDTrack (spiking transformer) fine-tuned on eSkiTB: **0.711 IoU**, +0.399 over its pretrained baseline.
- High-clutter split: SDTrack hits **0.685 IoU**, +20.0 IoU over generic STARK, confirming robustness to broadcast overlays and banners.

## Repository layout
```
eskitb-repo/
├── README.md              # You are here
├── LICENSE                # Code MIT; dataset CC BY-NC recommended
├── data/
│   ├── README.md          # Download + integrity instructions
│   ├── splits/            # Train/val/test lists (placeholders)
│   └── annotations/       # Schema docs + example
├── code/
│   ├── evaluation/        # Eval stub
│   ├── visualization/     # Event + box overlay helper
│   └── generation/        # Conversion configs/notes
├── examples/              # Tiny sample for smoke tests
└── docs/                  # Static site for GitHub Pages
```

## Getting started
1) Clone
```
git clone https://github.com/eventbasedvision/eskitb.git
cd eskitb
```
2) Download dataset archives to `data/raw` (links + checksums coming). Keep paths consistent with `data/splits/*`.
3) (Optional) Create env
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # to be added with actual deps
```
4) Smoke test paths (after data is in place)
```
python code/evaluation/evaluate.py \
  --split data/splits/val.txt \
  --annotations data/annotations/example.json \
  --data-root data/raw
```

## Data access (summary)
- Full dataset hosted externally; see [data/README.md](data/README.md) for links + integrity checks.
- Splits in [data/splits](data/splits); annotations/schema in [data/annotations](data/annotations).
- Tiny sample expected under `examples/` (add a few-MB clip + annotation).

## License
- Code: MIT (see [LICENSE](LICENSE)).
- Dataset: CC BY-NC 4.0 recommended; restate terms next to download links.
