# Digital Image Processing: Lab Task 02

**Digital Images, Pixels, Color, and Basic Transformations**

| | |
|---|---|
| **Name** | Sheikh Haseeb-ur-Rehman |
| **Roll No.** | 2024-SE-31 |
| **Instructor** | Engr. Fahad Nisar |
| **Department** | Software Engineering, University of Azad Jammu and Kashmir |
| **Semester / Session** | Fifth / 2024-28 (SE) |

---

## Objective

Use **NumPy**, **OpenCV**, and **Matplotlib** to load, inspect, display, analyze, transform, and save a digital image, while correctly handling pixel coordinates, color channels, histograms, resolution, and bit depth.

## What This Lab Covers

| Step | Topic | What was done |
|------|-------|---------------|
| 1 | Environment | Created `dip-lab-02`, a `.venv` virtual environment, installed `numpy`, `opencv-python`, `matplotlib` (plus `ipykernel` for the notebook), and added `.venv/` to `.gitignore` |
| 2 | Load image | Loaded the image with `cv.imread()`, raised `FileNotFoundError` if missing, printed shape and dtype |
| 3 | Inspect | Printed height, width, channels, top-left and center pixels (`[row, col]`), global and per-channel min/max |
| 4 | Color and channels | BGR to RGB, grayscale, separate R/G/B channels, 2 x 3 figure, center pixel converted to HEX |
| 5 | Crop, resize, save | Exact 100 x 100 crop, resized to 200 x 200, side-by-side display, saved `resized_crop.png` |
| 6 | Histogram | 256-bin grayscale histogram over 0-256, saved `grayscale_histogram.png`, with written interpretation |
| 7 | Bit depth | 8-bit gradient quantized to 1-, 2-, and 4-bit, with unique-value counts |
| 8 | Final check | Verified all required output files exist and are valid |

## Key Results

| Property | Value |
|----------|-------|
| Image size (H x W x C) | 1792 x 2400 x 3 |
| Data type | `uint8` |
| Top-left pixel `[0, 0]` (B, G, R) | `[35 23 43]` |
| Center pixel `[896, 1200]` (B, G, R) | `[4 139 183]` |
| Center pixel RGB / HEX | `(183, 139, 4)` / `#B78B04` |
| Global min / max | 0 / 255 |
| Crop region | rows 846:946, columns 1150:1250 |
| Crop / resized shape | (100, 100, 3) / (200, 200, 3) |
| Mean grayscale intensity | 61.7 / 255 |
| Dark / mid / bright pixels | 73.1% / 17.7% / 9.2% |
| Unique values (8, 1, 2, 4-bit) | 256, 2, 4, 16 |

## Short Concept Notes

- **BGR vs RGB:** OpenCV loads and saves color images in Blue-Green-Red order, while Matplotlib expects Red-Green-Blue. Displaying a BGR array directly swaps red and blue, so it must be converted with `cv.COLOR_BGR2RGB` first (and back with `cv.COLOR_RGB2BGR` before `cv.imwrite()`).
- **Resolution vs bit depth:** Resolution is the number of pixels (width x height) and controls spatial detail. Bit depth is the number of bits per pixel and controls how many intensity levels are possible (1-bit = 2, 2-bit = 4, 4-bit = 16, 8-bit = 256).
- **Histogram:** Shows how many pixels have each intensity value (brightness, contrast, clipping). It does **not** show where pixels are located, what objects are present, or color information.

## Repository Structure

```
dip-lab-02/
├── lab02.py                    # Main script (all steps)
├── lab02.ipynb                 # Notebook version with results and explanations
├── photo.jpg                   # Input image (personally selected, 2400 x 1792)
├── resized_crop.png            # Output: 200 x 200 resized crop
├── grayscale_histogram.png     # Output: grayscale histogram
├── evidence/                   # Extra figures saved for the report (optional)
│   ├── channels_figure.png
│   ├── crop_resize_figure.png
│   └── bit_depth_figure.png
├── 2024-SE-31-LAB02.docx       # Lab report
├── .gitignore                  # Contains .venv/
└── README.md
```

> The `.venv/` folder is intentionally **not** included in the repository.

## How to Run

1. Clone the repository and open the folder in VS Code.

   ```bash
   git clone <your-repository-url>
   cd dip-lab-02
   ```

2. Create and activate a virtual environment.

   ```bash
   python -m venv .venv

   # PowerShell
   .venv\Scripts\Activate.ps1
   # Command Prompt
   .venv\Scripts\activate.bat
   ```

3. Install the dependencies.

   ```bash
   pip install numpy opencv-python matplotlib ipykernel
   ```

4. Run the script (or open `lab02.ipynb` and select the `.venv` kernel).

   ```bash
   python lab02.py
   ```

5. When finished:

   ```bash
   deactivate
   ```

## Requirements

- Python 3
- numpy
- opencv-python
- matplotlib
- ipykernel (only needed for the notebook)

## Academic Integrity

This is my own work for Lab Task 02. The input image was personally selected and is not the instructor's demonstration image.
