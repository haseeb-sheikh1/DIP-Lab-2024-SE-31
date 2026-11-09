# Lab Task #03 — Image Enhancement and Intensity Transformations

**Course:** Digital Image Processing Lab
**Department:** Software Engineering, University of Azad Jammu and Kashmir

| | |
|---|---|
| **Student** | Sheikh Haseeb-ur-Rehman |
| **Roll No.** | 2024-SE-31 |
| **Instructor** | Engr. Fahad Nisar |
| **Semester** | Fifth |
| **Session** | 2024-28 (SE) |
| **Date** | November 09, 2026 |

---

## Overview

This lab implements and compares grayscale intensity transformations, histogram-based enhancement and thresholding techniques using **Python, NumPy and OpenCV**, while preventing 8-bit overflow and interpreting the effect of each operation.

Every operation follows the same two-part method:

1. **Dry run** — a typed hand calculation on a small pixel array, then verified in Python with a `verify()` helper (the notebook asserts that hand and computed values match).
2. **Image task** — the same operation applied to a personally selected 2048 × 2048 image, followed by brief observations backed by measured statistics.

All images are displayed with `cmap="gray", vmin=0, vmax=255` so Matplotlib never silently rescales intensities.

## Repository Contents

| File | Description |
|---|---|
| `2024-SE-31-LAB03.ipynb` | Jupyter notebook with all code, dry runs and outputs |
| `2024-SE-31-LAB03.docx` | Lab report (Word) |
| `2024-SE-31-LAB03.pdf` | Lab report (PDF) |
| `input_image.jpg` | Input image (2048 × 2048, generated with Google Gemini) |
| `README.md` | This file |

## Requirements

- Python 3
- `opencv-python` (tested with OpenCV 5.0.0)
- `numpy` (tested with NumPy 2.5.4)
- `matplotlib`
- `ipykernel` (to run the notebook in VS Code / Jupyter)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (PowerShell: .venv\Scripts\Activate.ps1)
pip install numpy opencv-python matplotlib ipykernel
```

## How to Run

1. Keep `input_image.jpg` in the **same folder** as the notebook (the notebook raises a `FileNotFoundError` otherwise).
2. Open `2024-SE-31-LAB03.ipynb` in VS Code or Jupyter and select the `.venv` kernel.
3. Run all cells from top to bottom. Every dry run ends with `✔ MATCH` lines; a `✘ MISMATCH` stops execution through an assertion.

## Safe 8-bit Arithmetic

A `uint8` pixel only stores 0–255, so arithmetic done inside `uint8` wraps around (e.g. `240 + 50 → 34`). The recipe used throughout the lab:

1. Convert to a wider type (`int16` for integer maths, `float64` for fractional maths)
2. Compute the transformation
3. `np.clip(..., 0, 255)`
4. Convert back with `.astype(np.uint8)` (truncates fractions)

The input image is read with `cv2.IMREAD_GRAYSCALE`, validated (2-D, `uint8`, at least 300 × 300) and locked read-only, so every operation creates a new array.

## Operations Implemented

| # | Operation | Rule / Settings | Key result on the input image |
|---|---|---|---|
| 1 | Brightness | `s = r + β`, β = ±40 (NumPy and nested loops) | Mean 107.27 → 145.01 / 71.57; 7.96 % clipped to 255, 19.09 % clipped to 0 |
| 2 | Linear contrast from zero | `s = 1.5·r + 0` | Mean 149.87, std-dev 81.95; 15.91 % of pixels saturate |
| 3 | Contrast centered at 128 | `s = (r − 128)·α + 128`, α = 1.5 and 0.5 | α = 1.5: std-dev 82.61; α = 0.5: range compressed to 64–191 |
| 4 | Image negative | `s = 255 − r` | Mean 147.73 (= 255 − 107.27); lossless and reversible |
| 5 | Gamma correction | `s = 255·(r/255)^γ`, γ = 0.5 and 2.0 | Dark-region mean 29.48 → 80.41 (γ = 0.5) / 4.44 (γ = 2.0) |
| 6 | Grayscale histogram | 256 bins, probabilities | 38.9 % dark, 45.2 % medium, 15.9 % bright pixels |
| 7 | Global histogram equalization | `cv2.equalizeHist` | Mean 107.3 → 128.1; Laplacian variance in dark arch 449.6 → 753.6 (noise amplified) |
| 8 | CLAHE | `clipLimit=2.0`, `tileGridSize=(8, 8)` | Dark arch std-dev 37.7 vs 31.6 (global); bright wall contrast preserved |
| 9 | Fixed binary threshold | `T = 127`, `r > T → 255` | 38.00 % white, 62.00 % black |
| 10 | Otsu thresholding | `THRESH_BINARY + THRESH_OTSU` | T = 106; 50.58 % white; 87.42 % agreement with fixed mask |
| 11 | Adaptive Gaussian threshold | `blockSize=11`, `C=2` | 57.23 % white; behaves like an edge / local-contrast map |

Operation 12 is a **technical summary and integrity check**: statistics for every result image, plus a check that the original array is identical to a fresh read of the file and still read-only.

## Dry Runs

| Dry run | Input | Verified result |
|---|---|---|
| 1 Brightness | `[30, 80, 128, 180, 240]` | +40 → `[70, 120, 168, 220, 255]`; −40 → `[0, 40, 88, 140, 200]` |
| 2 Linear contrast | same | `[45, 120, 192, 255, 255]` (180 and 240 saturate) |
| 3 Centered contrast | same | α = 1.5 → `[0, 56, 128, 206, 255]`; α = 0.5 → `[79, 104, 128, 154, 184]` |
| 4 Negative | same | `[225, 175, 127, 75, 15]`; applying it twice returns the original |
| 5 Gamma | `[0, 64, 128, 192, 255]` | γ = 0.5 → `[0, 127, 180, 221, 255]`; γ = 2.0 → `[0, 16, 64, 144, 255]` |
| 6 Histogram | 2 × 4 matrix `A` | Probabilities sum to 1; matrix `B` (same values, different positions) has an identical histogram |
| 7 Equalization | `[50, 50, 100, 150]` | CDFmin-corrected mapping → `[0, 0, 128, 255]`, identical to OpenCV |
| 8 CLAHE | histogram `[6, 2, 0, 0]`, cap 4 | Clipped `[4, 2, 0, 0]`, redistributed `[4.5, 2.5, 0.5, 0.5]` |
| 9 Fixed threshold | `[0, 80, 127, 128, 180, 255]` | T = 127 → 3 white pixels; T = 180 → 1 white pixel |
| 10 Otsu | `[0, 1, 4, 5]` | Max variance 4.0 at T = 1, 2, 3; smallest T = 1 chosen, matches OpenCV |
| 11 Adaptive | 3 × 3 neighbourhood | Weighted mean 120, T = 118; a pixel equal to T becomes 0 |

## Main Conclusions

- **Brightness vs contrast:** brightness shifts the whole histogram; contrast scales its spread. Centering contrast at 128 changes contrast without also changing overall brightness.
- **Clipping is irreversible:** values lost to saturation cannot be recovered, while the negative is fully reversible.
- **Gamma** lifts shadows (γ < 1) or crushes them (γ > 1) without needing clipping; 0 and 255 never change.
- **Global vs local:** global equalization and fixed or Otsu thresholds are simple and fast but struggle with uneven lighting. CLAHE and adaptive thresholding cope better with unevenly lit scenes, at the cost of more noise amplification or edge-only output.
- **Gamma convention used:** `s = 255·(r/255)^γ`, so γ < 1 brightens. Some libraries use the inverse convention.

## Notes

- The dry-run results for gamma use truncation at the final step only, so values differ by one level from a rounded slide example (127 vs 128 and 180 vs 181 for r = 64 and r = 128).
- The CLAHE dry run is a simplified model; OpenCV redistributes integer counts and its `clipLimit` is not the same as the absolute cap used in the hand calculation.
