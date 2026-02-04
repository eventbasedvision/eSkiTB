# Updates

<!-- syntax for updating -->
<!-- - [6 August 2025] Tool for Manual Annotation Release -->

# _eSkiTB_: Event-based Ski Tracking Benchmark

<!-- for adding link to paper and image -->
<div>
<a href="https://arxiv.org/abs/2601.06647">Paper</a> | 
<a href="https://www.dropbox.com/scl/fi/1fbsjthks57e3mucxrsz5/E-Ski_v2e.zip?rlkey=8hn6umsbo406eygoy7s81kg1d&st=0fntvbfr&dl=0">Dataset</a> | 
<a href="https://eventbasedvision.github.io/eskitb/">Website</a>
</div>

<hr>

<div style="text-align: center;">
<img src="docs/media/images/Teaser_image.png"/>
</div>

<p align="justify">
Tracking skiers in RGB broadcast footage is challenging due to motion blur, static overlays, and clutter that obscure the fast-moving athlete. Event cameras, with their asynchronous contrast sensing, offer natural robustness to such artifacts, yet a controlled benchmark for winter-sport tracking has been missing. We introduce event SkiTB (eSkiTB), a synthetic event-based ski tracking dataset generated from SkiTB using direct video-to-event conversion without neural interpolation, enabling an iso-informational comparison between RGB and event modalities. Benchmarking SDTrack (spiking transformer) against STARK (RGB transformer), we find that event-based tracking is substantially resilient to broadcast clutter in scenes dominated by static overlays, achieving 0.685 IoU, outperforming RGB by +20.0 points. Across the dataset, SDTrack attains a mean IoU of 0.711, demonstrating that temporal contrast is a reliable cue for tracking ballistic motion in visually congested environments. eSkiTB establishes the first controlled setting for event-based tracking in winter sports and highlights the promise of event cameras for ski tracking.
</p>

# Dataset Overview

<p align="justify">
The eSkiTB dataset comprises 300 high-resolution broadcast sequences (1280x720) spanning Alpine Skiing (AL), Freestyle Skiing (FS), and Ski Jumping (JP). Generated via the v2e simulator under a strict iso-informational constraint (no neural interpolation), the dataset provides event streams in HDF5 format with per-frame bounding box annotations and 1 ms spline-interpolated dense labels. The dataset is split into Train/Val/Test with 240/30/30 sequences respectively, and includes 10 visual attribute annotations (occlusion, fast motion, illumination variation, background clutter, etc.).
</p>

# Dataset

The Dataset is available <a href="https://www.dropbox.com/scl/fi/1fbsjthks57e3mucxrsz5/E-Ski_v2e.zip?rlkey=8hn6umsbo406eygoy7s81kg1d&st=0fntvbfr&dl=0">here</a>

### Dataset Statistics

- **Total Sequences:** 300 (AL/FS/JP)
- **Duration:** ~235 minutes
- **Resolution:** 1280 x 720
- **Splits:** Train (240), Val (30), Test (30)
- **Format:** HDF5 events `(t, x, y, p)` in microseconds; JSON boxes `[x, y, w, h]`

### Repository Structure

```bash
eskitb-repo/
├── README.md
├── LICENSE
├── data/
│   ├── README.md
│   ├── splits/
│   └── annotations/
├── code/
│   ├── evaluation/
│   ├── visualization/
│   └── generation/
├── examples/
└── docs/
```

# Getting Started

Download the dataset and unpack under `data/raw`. Ensure paths align with `data/splits/*`.

Install dependencies:

```bash
git clone https://github.com/eventbasedvision/eskitb.git
cd eskitb
pip install -r requirements.txt  # add h5py, numpy, opencv-python, etc.
```

# Usage

Run evaluation on validation split:

```bash
python code/evaluation/evaluate.py \
  --split data/splits/val.txt \
  --annotations data/annotations/example.json \
  --data-root data/raw
```

Visualize events with bounding boxes:

```bash
python code/visualization/visualize_events.py \
  --events examples/sample_events.npy \
  --annotation data/annotations/example.json \
  --out vis.png
```

# License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

Code is released under the MIT License.

# Citation

If you use our dataset or code, please cite our paper and the original SkiTB and v2e works:

```bash
@article{eskitb2026,
  title     = {eSkiTB: Event-based Ski Tracking Benchmark},
  author    = {Vinod, Krishna and Vishal, Joseph Raj and Chanda, Kaustav and Ramesh, Prithvi Jai and Yang, Yezhou and Chakravarthi, Bharatesh},
  journal   = {arXiv preprint arXiv:2601.06647},
  year      = {2026}
}
```

```bash
@inproceedings{hu2021v2e,
  title     = {v2e: From video frames to realistic DVS events},
  author    = {Hu, Yuhuang and Liu, Shih-Chii and Delbruck, Tobi},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages     = {1312--1321},
  year      = {2021}
}
```
