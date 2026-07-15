# DFT Optical Spectra of Zn-Doped Au20 Nanoclusters

## Problem background
Gold nanoclusters are promising for photothermal therapy due to their biocompatibility. However, the optical absorption of the stable tetrahedral Au20 cluster lies primarily in the visible range, limiting in vivo therapeutic applications where near-infrared (NIR) light penetrates tissue more effectively. This task reproduces first‑principles DFT calculations that investigate how substituting Au atoms with Zn atoms in Au20 modifies the electronic structure and optical spectra, with the goal of understanding whether Zn doping can shift the optical absorption into the NIR.

## Approach
Use density functional theory (DFT) within the generalized gradient approximation (PBE functional) and the plane‑wave pseudopotential method. For the neutral clusters Au20, Au19Zn1, Au18Zn2, Au17Zn3, and Au16Zn4, the workflow comprises: (i) building initial atomic coordinates from the known tetrahedral Au20 structure with Zn substituted at vertex sites; (ii) geometry relaxation to obtain the ground‑state structures; (iii) a self‑consistent field calculation to obtain Kohn–Sham eigenvalues and wavefunctions; (iv) computation of the frequency‑dependent dielectric function within the independent‑particle approximation, averaged over polarization directions, to obtain the imaginary part ε₂(ω) and the optical absorption coefficient α(ω). The resulting spectra are then analyzed to extract the principal peak positions.

## Reproduction target
For each of the five compositions — Au20, Au19Zn1, Au18Zn2, Au17Zn3, and Au16Zn4 — compute and report the three main peak energies (E1, E2, E3 in eV) of the imaginary dielectric function ε₂(ω). Additionally, for Au20 and Au17Zn3, report the wavelength (in nm) of the dominant peak in the optical absorption spectrum. Store all results in the structured JSON file optical_peaks.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard Solid-State Pseudopotentials (SSSP) library – PBE norm-conserving: https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/
- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Generate cluster models
- Role: process
- Action: Create initial atomic coordinates for Au20 and the Zn-substituted clusters Au19Zn1, Au18Zn2, Au17Zn3, Au16Zn4 using the known tetrahedral Au20 structure, substituting Zn at vertex sites as described in the paper's method. Write structures in a format suitable for DFT input.
- Evidence: none

### Step 2: Geometry optimization via DFT
- Role: process
- Action: For each cluster, relax atomic positions using DFT-PBE with norm-conserving pseudopotentials, a plane-wave cutoff of 720 eV, and a 20x20x20 Å supercell, until forces converge. Save optimized structures.
- Evidence: none

### Step 3: Self-consistent field (SCF) calculation
- Role: process
- Action: Run a self-consistent field calculation on the optimized geometries to obtain Kohn-Sham eigenvalues and wavefunctions for each cluster.
- Evidence: none

### Step 4: Optical spectrum calculation
- Role: process
- Action: From the SCF wavefunctions, compute the imaginary part of the dielectric function ε₂(ω) within the independent-particle approximation, averaging polarization. Derive the optical absorption coefficient α(ω). Store ε₂(ω) and absorption spectra as text files.
- Evidence: none

### Step 5: Extract optical peaks
- Role: scored (load-bearing)
- Action: Analyze the computed ε₂(ω) spectra to identify the three principal peaks (E1, E2, E3) in eV for each composition. From the optical absorption spectrum extract the wavelength (nm) of the dominant absorption band for Au20 and Au17Zn3. Write the results to optical_peaks.json.
- Output file: `/app/outputs/optical_peaks.json`
- Format: json
- Contract: Object with keys for each composition: 'Au20', 'Au19Zn1', 'Au18Zn2', 'Au17Zn3', 'Au16Zn4'. Each value is an object with numeric fields 'E1', 'E2', 'E3' (float, in eV). For Au20 and Au17Zn3 the object additionally contains 'absorption_peak_nm' (float, in nm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_peaks.json
- path: `/app/outputs/optical_peaks.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the extracted ε₂ peak energies and optical absorption peak wavelengths for Zn-doped Au20 clusters.
- schema:
  - `type`: object
  - `required`:
    - `Au20`: object with fields E1, E2, E3 (eV) and absorption_peak_nm (nm)
    - `Au19Zn1`: object with fields E1, E2, E3 (eV)
    - `Au18Zn2`: object with fields E1, E2, E3 (eV)
    - `Au17Zn3`: object with fields E1, E2, E3 (eV) and absorption_peak_nm (nm)
    - `Au16Zn4`: object with fields E1, E2, E3 (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `E1`: eV
    - `E2`: eV
    - `E3`: eV
    - `absorption_peak_nm`: nm

Notes: The checker compares the agent's reported peak energies and absorption wavelengths to the paper-reported values within hidden tolerances and enforces monotonic trends (E1 decreases, E2 decreases, E3 non-decreasing with Zn concentration).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Au20": "object with fields E1, E2, E3 (eV) and absorption_peak_nm (nm)",
          "Au19Zn1": "object with fields E1, E2, E3 (eV)",
          "Au18Zn2": "object with fields E1, E2, E3 (eV)",
          "Au17Zn3": "object with fields E1, E2, E3 (eV) and absorption_peak_nm (nm)",
          "Au16Zn4": "object with fields E1, E2, E3 (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "E1": "eV",
          "E2": "eV",
          "E3": "eV",
          "absorption_peak_nm": "nm"
        }
      },
      "description": "JSON file containing the extracted ε₂ peak energies and optical absorption peak wavelengths for Zn-doped Au20 clusters."
    }
  ],
  "notes": "The checker compares the agent's reported peak energies and absorption wavelengths to the paper-reported values within hidden tolerances and enforces monotonic trends (E1 decreases, E2 decreases, E3 non-decreasing with Zn concentration)."
}
```

## How you are scored
A hidden verifier will independently score the contents of optical_peaks.json. It checks that the reported peak energies and absorption wavelengths lie within allowed tolerances and that they obey certain expected relationships among the compositions (for example, monotonic trends with Zn concentration). The verifier does not re‑run the DFT calculations but assumes that the numbers were obtained from an honest execution of the workflow. The final reward is a weighted combination of the scores for the submitted optical_peaks.json artifact.
