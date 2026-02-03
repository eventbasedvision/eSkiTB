# eSkiTB data guide

This repo ships metadata and tiny samples; the full dataset is hosted externally.

## Download (links you will add)
- Train split (240 seq): TODO link (size, MD5/SHA256)
- Val split (30 seq): TODO link (size, MD5/SHA256)
- Test split (30 seq): TODO link (size, MD5/SHA256)
- Optional RGB/diagnostics: TODO link (size, MD5/SHA256)

Place archives under `data/raw` and keep relative paths consistent with `data/splits/*`.

## Expected layout
```
data/
├── raw/
│   ├── train/
│   ├── val/
│   └── test/
├── splits/
│   ├── train.txt
│   ├── val.txt
│   └── test.txt
└── annotations/
    ├── format.md
    └── example.json
```

## Format recap (from the paper)
- Resolution: 1280×720
- Events: HDF5 dataset `events` with rows `(t, x, y, p)` where `t` is microseconds, `p∈{0,1}`.
- Boxes: JSON with `[x, y, w, h]` pixels (top-left origin), class = `Skier`.
- Dense labels: 1 ms cubic-spline interpolation between frame annotations.
- Attributes: 10 visual conditions (occlusion, fast motion, illumination variation, background clutter, etc.).

## Iso-informational conversion
Events are generated directly from broadcast RGB via v2e **without** neural frame interpolation (no SuperSloMo). Every event corresponds to observed photometric change—no hallucinated temporal cues.

## Integrity checks
Publish checksums alongside download links. Recommended:
```
md5sum train.tar.gz
sha256sum train.tar.gz
```
Users should verify before unpacking.

## Tiny sample
Add a small clip + annotation under `examples/` so users can sanity-check loaders without pulling the full dataset (<10 MB).
