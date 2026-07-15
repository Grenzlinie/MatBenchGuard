# DFT Band Structure and Optical Properties of TGS Crystal

## Problem background
Triglycine sulphate (TGS) is a ferroelectric material below 322 K, crystallizing in the monoclinic space group P2₁. Its unit cell contains 74 atoms arranged in glycine complexes, sulphate anions, and hydrogen bonds. Despite broad application as a detector material, the electronic band structure and ultraviolet optical properties of TGS have not been thoroughly characterized from first principles. This task addresses the theoretical determination of the electronic structure and dielectric response of the ferroelectric phase using density-functional theory (DFT), with the aim of clarifying the nature of the band gap and the origin of spectral features in the 4–10 eV range.

## Approach
The electronic structure and optical properties are computed via first-principles DFT within the generalized gradient approximation (GGA). An open-source plane-wave code (Quantum ESPRESSO) is used with ultrasoft pseudopotentials to describe the ionic cores. The workflow begins by obtaining the crystal structure from a public database and performing a geometry relaxation to reach the ground-state configuration. A self-consistent field (SCF) calculation is then carried out, followed by a non-self-consistent band structure computation along a high-symmetry path in the Brillouin zone. The imaginary part of the dielectric function ε''(E) is calculated within the independent-particle approximation; to improve agreement with experiment, a rigid scissor shift of 0.9 eV is applied to the conduction bands when computing the dielectric function. The key outcomes are the band gap (its magnitude and whether it is direct or indirect) and the ε''(E) spectrum for light polarized along the crystal a‑axis, over the photon energy range 0–12 eV.

## Reproduction target
Using the open-source DFT code, compute the electronic band structure and the imaginary dielectric function for TGS in the ferroelectric phase. Specifically, produce two scored artifacts: (1) a text file `band_gap.txt` that reports the computed band gap energy (in eV) and whether the gap is direct or indirect; and (2) a CSV file `epsilon_im.csv` that lists the ε''(E) spectrum for the X‑direction (a‑axis) after applying the 0.9 eV scissor shift, covering energies from 0 to 12 eV with at least 100 data points. The goal is to reproduce these quantities, which characterize the fundamental electronic and optical response of the material.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- TGS crystal structure (CIF file for ferroelectric P2₁ phase): https://www.crystallography.net/cod/9008320.cif
- Ultrasoft pseudopotentials (SSSP library or equivalent): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Obtain TGS crystal structure
- Role: process
- Action: Retrieve the crystal structure CIF file for ferroelectric TGS (P2₁ phase) from a public crystallographic database (e.g., COD entry 9008320).
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Using an open-source plane-wave DFT code (Quantum ESPRESSO), relax the atomic positions and cell of TGS. Use a GGA exchange-correlation functional (e.g., PBE), ultrasoft pseudopotentials, a plane-wave cutoff around 340 eV, and a k‑point mesh with at least 23 k‑points in the full Brillouin zone. Write the optimized structure to a file for later use.
- Evidence: `/app/outputs/tgs_opt.out`

### Step 3: SCF, band structure and dielectric function calculation
- Role: process
- Action: Starting from the optimized structure, run a self-consistent field (SCF) calculation, then a non‑self‑consistent band structure computation along the high‑symmetry path Γ–Y–Z–Γ–D–B–E, and compute the imaginary part of the dielectric function ε''(E) within the independent‑particle approximation. A rigid scissor shift of 0.9 eV must be applied to the conduction bands for the dielectric function calculation. Save the raw band structure data and the epsilon output.
- Evidence: `/app/outputs/bands.out, epsilon.out`

### Step 4: Extract band gap
- Role: scored (load-bearing)
- Action: From the computed band structure, identify the valence band maximum and conduction band minimum, determine the band gap value (in eV) and whether it is direct or indirect. Write the result to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: Three lines: first line 'Band gap = <value> eV', second line 'Type: <Direct or Indirect>', third line optionally 'VBM at <kpoint> and CBM at <kpoint>'.
- Scoring: scored by hidden verifier

### Step 5: Generate ε''(E) spectrum
- Role: scored (load-bearing)
- Action: Extract the imaginary part of the dielectric function ε''(E) for the polarization along the crystal a‑axis (X‑direction). Write the spectrum as a two‑column CSV (Energy_eV, Epsilon_im) covering at least 0–12 eV with at least 100 points. Ensure the 0.9 eV scissor shift has been applied.
- Output file: `/app/outputs/epsilon_im.csv`
- Format: csv
- Contract: CSV with two columns: Energy_eV (float), Epsilon_im (float). Energy range 0‑12 eV, at least 100 points.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/epsilon_im.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: The computed band gap energy and whether it is direct or indirect, extracted from the DFT band structure. The hidden checker compares the reported gap and type to the paper’s values.
- schema:
  - `type`: text
  - `pattern`: Line1: 'Band gap = <value> eV', Line2: 'Type: <Direct or Indirect>', optional Line3 with k-point positions.

### epsilon_im.csv
- path: `/app/outputs/epsilon_im.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The imaginary part of the dielectric function ε''(E) along the X‑direction after a 0.9 eV scissor shift. The hidden checker recomputes the position of the main peak in the 6–8 eV range from this spectrum and compares it to the paper‑reported peak position.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `Epsilon_im`
  - `units`:
    - `Energy_eV`: eV
    - `Epsilon_im`: dimensionless

Notes: The DFT calculations use the independent‑particle approximation with a GGA functional and ultrasoft pseudopotentials. The scissor shift of 0.9 eV is to be applied as described. The checker does not evaluate the absolute intensity of ε''(E), only the peak location.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "pattern": "Line1: 'Band gap = <value> eV', Line2: 'Type: <Direct or Indirect>', optional Line3 with k-point positions."
      },
      "description": "The computed band gap energy and whether it is direct or indirect, extracted from the DFT band structure. The hidden checker compares the reported gap and type to the paper’s values."
    },
    {
      "file": "epsilon_im.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "Epsilon_im"
        ],
        "units": {
          "Energy_eV": "eV",
          "Epsilon_im": "dimensionless"
        }
      },
      "description": "The imaginary part of the dielectric function ε''(E) along the X‑direction after a 0.9 eV scissor shift. The hidden checker recomputes the position of the main peak in the 6–8 eV range from this spectrum and compares it to the paper‑reported peak position."
    }
  ],
  "notes": "The DFT calculations use the independent‑particle approximation with a GGA functional and ultrasoft pseudopotentials. The scissor shift of 0.9 eV is to be applied as described. The checker does not evaluate the absolute intensity of ε''(E), only the peak location."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted artifacts against reference values derived from the original study. For `band_gap.txt`, the verifier reads the reported band gap and its direct/indirect classification, comparing them to a hidden reference within a tolerance. For `epsilon_im.csv`, the verifier reads the spectrum, locates the position of the main absorption peak in the 6–8 eV range, and compares it to the expected position. The two items contribute equally to the final reward (a float between 0 and 1). The verifier does not grade the absolute intensity of ε''(E), only the peak location, provided the spectrum meets the required energy range and point count. Reporting the paper’s numbers is not sufficient; the verifier scores the accuracy of your computed results.
