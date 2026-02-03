# Annotation schema (proposed)

This schema follows a per-sequence JSON with frame-level bounding boxes for each tracked athlete/object.

## Top-level fields
- `sequence_id` (string): unique clip identifier (e.g., "AL0006").
- `fps` (number): nominal frame rate of rendered event frames (if applicable).
- `resolution` (array[int, int]): `[width, height]` of frames/events.
- `frames` (array): list of frame entries (ordered by time).

## Frame entry
- `frame_id` (int): zero-based frame index.
- `timestamp` (float): seconds since sequence start (optional but recommended).
- `objects` (array): list of tracked objects for this frame. Empty array if no visible targets.

## Object entry
- `track_id` (int): persistent ID for the object across frames.
- `category` (string): class label (e.g., "athlete").
- `bbox` (array[float, float, float, float]): `[x, y, w, h]` in pixels (top-left origin).
- `confidence` (float, optional): 0–1 for pseudo-labels or detector outputs.

## Minimal example
```json
{
  "sequence_id": "AL0006",
  "fps": 20,
  "resolution": [1280, 720],
  "frames": [
    {
      "frame_id": 0,
      "timestamp": 0.000,
      "objects": [
        {"track_id": 1, "category": "athlete", "bbox": [430.5, 220.0, 120.0, 260.0], "confidence": 1.0}
      ]
    },
    {
      "frame_id": 1,
      "timestamp": 0.050,
      "objects": []
    }
  ]
}
```

If your internal format differs (e.g., polygon masks, multiple classes, or sparse events keyed by timestamps instead of frames), update this file and the example accordingly so downstream users have a single source of truth.
