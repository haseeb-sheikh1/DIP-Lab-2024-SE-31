# Lab Task 05 - Spatial Filtering and Convolution

**Name:** Sheikh Haseeb-ur-Rehman  
**Roll No.:** 2024-SE-31  
**Course:** Digital Image Processing Lab - Department of Software Engineering, The University of Azad Jammu and Kashmir  
**Instructor:** Engr. Fahad Nisar

## Contents

| File | Purpose |
|---|---|
| `2024-SE-31-LAB05.ipynb` | The completed notebook: code, outputs, dry-run calculations, observations and viva answers |
| `requirements.txt` | Python packages needed to run it |
| `.gitignore` | Keeps virtual environments and caches out of the repository |

## How to run

```bash
python -m venv .venv            # the .venv folder is ignored by git
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook 2024-SE-31-LAB05.ipynb
```

In Jupyter choose **Kernel -> Restart & Run All**. The whole notebook runs in well under a minute. The `camera`, `coins` and `chelsea` test images come bundled with scikit-image, so no download is needed.

## Decisions where the lab text is open (details in section 0 of the notebook)

- `amount=0.05` in salt-and-pepper means 5 % of all pixels in total (half 0, half 255).
- Noise uses `np.random.default_rng(seed)` created inside each function, with `seed=5`.
- `cv2.medianBlur` always replicates the border, so the image is reflect-padded first to satisfy R1.
- "Noisiest image" means the one with the lowest PSNR against its clean original.
