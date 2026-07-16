# Problem Brief: CUMCM 2021 E

Title: 中药材的鉴别

Purpose of this note: provide a clean, human-readable task brief for the calibration run. The raw extraction files remain in this run directory for audit, but the PDF text extraction contains font-map mojibake, so this note is based on rendered-page inspection plus attachment schema extraction.

## Problem Context

Different Chinese medicinal materials and different origins of the same material can show different near-infrared and mid-infrared spectral features. Category identification is easier because different materials can have visibly different spectra. Origin identification is harder because spectra from the same material but different origins can be close in the same band.

The problem asks the team to build mathematical models using spectral absorbance data.

Field meanings:

- `No`: sample identifier.
- `Class`: material category.
- `OP`: origin/place label.
- spectral columns: wave numbers in `cm^-1`.
- cell values after the first row: absorbance after instrument correction; negative values may appear.

## Subquestions

### Q1: Category Identification From Mid-Infrared Spectra

Attachment 1 gives mid-infrared spectra for several medicinal-material categories.

Task:

- study the features and differences of different material categories;
- identify the category of the materials.

### Q2: Origin Identification From Mid-Infrared Spectra

Attachment 2 gives mid-infrared spectra for one medicinal material from different origins.

Task:

- analyze features and differences among origins;
- identify the origin of samples whose `OP` is missing;
- fill the origin results for:

```text
No 3, 14, 38, 48, 58, 71, 79, 86, 89, 110, 134, 152, 227, 331, 618
```

### Q3: Origin Identification From Near-Infrared And Mid-Infrared Spectra

Attachment 3 gives near-infrared and mid-infrared spectra for one medicinal material.

Task:

- identify the origin by combining the two spectral bands;
- fill the origin results for:

```text
No 4, 15, 22, 30, 34, 45, 74, 114, 170, 209
```

### Q4: Category And Origin Identification From Near-Infrared Spectra

Attachment 4 gives near-infrared spectra for several medicinal-material categories.

Task:

- identify both material category and origin;
- fill the category and origin results for:

```text
No 94, 109, 140, 278, 308, 330, 347
```

## Calibration Meaning

This is a good classification-recognition pressure test because it has four increasing difficulty levels:

```text
category recognition
-> single-band origin recognition
-> two-band origin recognition
-> category and origin recognition with missing labels
```

The route should not stop at one classifier score. It must show:

- spectral preprocessing;
- feature or band interpretation;
- same-split classifier comparison;
- class/origin-level error diagnosis;
- final answer tables with claim boundaries.
