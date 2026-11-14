# Lab Task 04 – Geometric Transformations with Custom Inputs

**Course:** Digital Image Processing Lab, Department of Software Engineering, The University of Azad Jammu and Kashmir
**Instructor:** Engr. Fahad Nisar | **Semester:** Fifth | **Session:** 2024-28 (SE)
**Name:** Sheikh Haseeb-ur-Rehman
**Roll No:** 2024-SE-31

## Objective
Build one reusable `transform` function that takes an image, an operation name and that operation's custom
parameters, validates all input, and returns the correctly transformed image.

## Files
| Path | Description |
|---|---|
| `2024-SE-31-LAB04.ipynb` | Completed notebook, run from a restarted kernel; code, outputs, validation examples, checks and observations are visible |
| `input_image.jpg` | Input image (2400 x 1792 px) loaded by the notebook |
| `results/` | Saved transformed images (23 files) |
| `requirements.txt` | Packages needed to run the notebook |
| `2024-SE-31-LAB04.docx` | Written lab report (same content as the notebook, with figures) |
| `README.md` | This file |
| `.gitignore` | Excludes virtual environments and caches |

All code is inside the notebook; there are no separate helper source files.

## Notebook sections
1. Setup and declared limits (max output 10,000 px per side and 25 megapixels; black fill for exposed background)
2. Image loading and validation (file exists, decodes, non-zero size); original kept unchanged; RGB colour handling
3. `transform(image, operation, **params)` with `scale`, `crop`, `flip`, `translate`, `rotate`
4. Prompt-driven input: a recorded session (operation selection and parameter entry, with error messages and re-entry) and a live `ipywidgets` control panel
5. Demonstrations with labelled figures: enlargement and reduction, proportional and non-proportional scaling, crop, three flips, opposite translations, positive and negative rotations; the 2 x 3 affine matrices behind translation and rotation, verified against `cv2.warpAffine`
6. Interpolation comparison (nearest, bilinear, bicubic, Lanczos) on one 6x enlarged patch, with a measured timing table and observations
7. Rejected inputs (30 cases, at least one per operation) and accepted boundary inputs
8. Identity checks table (zero translation, scale 1, zero rotation): expected, actual, Pass/Fail
9. Observations: image coordinates vs array indexing, aspect-ratio distortion, rotation canvas expansion, translation clipping
10. Final check that the original image is unchanged, and list of saved results

## Operations and rules
| Operation | Inputs | Validation |
|---|---|---|
| Scale | `fx`, `fy`, `interpolation` | finite and > 0; output at least 1 x 1 px; supported interpolation; size limit |
| Crop | `left`, `top`, `right`, `bottom` | integers; 0 <= left < right <= width, 0 <= top < bottom <= height (right/bottom exclusive) |
| Flip | `direction` | `horizontal`, `vertical` or `both` only |
| Translate | `tx`, `ty` | finite numbers (positive, negative, zero); canvas size kept |
| Rotate | `angle`, `expand` | any finite angle (0 and negative allowed); `expand` must be a bool; positive = counter-clockwise, about the image centre |

## Saved results (`results/`)
- `01`-`03`: scaling (enlarge 1.5 x 1.5, reduce 0.4 x 0.4, non-proportional 1.5 x 0.6)
- `04`: crop
- `05`-`07`: horizontal, vertical and both flips
- `08`-`09`: translation (+300, +150) and (-250, -200)
- `10`-`13`: rotation +30 and -45 degrees, with and without canvas expansion
- `14`-`15`: interpolation patch (original and four 6x versions)
- `interactive_01`-`interactive_05`: one result per operation from the prompt session

## Run
```bash
pip install -r requirements.txt
jupyter notebook 2024-SE-31-LAB04.ipynb    # Kernel > Restart & Run All
```
Keep `input_image.jpg` in the same folder as the notebook. To type your own values, use the live control panel in
section 4.2 (needs `ipywidgets` and a Jupyter front end such as JupyterLab, Jupyter Notebook or VS Code), or set
`LIVE_INPUT = True` in section 4 and run `interactive_session(original, input)`.
