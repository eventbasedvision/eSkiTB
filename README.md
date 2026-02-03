# eSkiTB: Event-based Ski Tracking Benchmark

Event-based ski tracking benchmark derived from SkiTB. Public links and a SEBVS-style landing page are below.

## Quick links
- Paper: https://arxiv.org/abs/2601.06647
- Dataset: https://www.dropbox.com/scl/fi/1fbsjthks57e3mucxrsz5/E-Ski_v2e.zip?rlkey=8hn6umsbo406eygoy7s81kg1d&st=0fntvbfr&dl=0
- Code: https://github.com/eventbasedvision/eskitb
- Website: docs/index.html (serve via GitHub Pages)

## Snapshot
- Scale: 300 broadcast sequences (AL/FS/JP), 235 minutes, 1280x720.
- Splits: Train/Val/Test = 240/30/30 sequences.
- Conversion: v2e with **iso-informational** constraint (no SuperSloMo or neural interpolation).
- Format: HDF5 events `(t, x, y, p)` in microseconds; boxes `[x, y, w, h]` with 1 ms spline interpolation.
- Attributes: 10 visual conditions (occlusion, fast motion, illumination variation, background clutter, etc.).

## Headline results (from the paper)
- STARK (RGB, fine-tuned): 0.795 IoU; ski-specific: 0.829 IoU.
- SDTrack (spiking, fine-tuned on eSkiTB): **0.711 IoU**, +0.399 over its pretrained baseline.
- High-clutter split: SDTrack **0.685 IoU**, +20.0 IoU over generic STARK.

## Visuals
- Teaser: docs/media/images/Teaser_image.png
- Stats: docs/media/images/eSkiTB Statistics.png
- RGB vs event clutter: docs/media/images/rgb_artifacts.png
- Pipeline: docs/media/images/v2e pipeline without slowmo.png

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
└── docs/                  # Static site (GitHub Pages)
```

## Getting started
1) Clone
```
git clone https://github.com/eventbasedvision/eskitb.git
cd eskitb
```
2) Download the dataset zip and unpack under `data/raw` (align paths with `data/splits/*`).
3) (Optional) Create env
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # add your deps here
```
4) Smoke test paths (after data is in place)
```
python code/evaluation/evaluate.py \
  --split data/splits/val.txt \
  --annotations data/annotations/example.json \
  --data-root data/raw
```

## License
- Code: MIT (see LICENSE).
- Dataset: CC BY-NC 4.0 recommended; restate terms next to download links.
