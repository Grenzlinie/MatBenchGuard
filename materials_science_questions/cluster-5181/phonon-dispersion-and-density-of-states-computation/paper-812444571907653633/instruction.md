# Phonon Spectrum and Impurity Local Mode Calculation for Indium Phosphide

## Problem background
Accurate lattice dynamics models for III-V semiconductors are essential for understanding impurity vibrational modes. InP possesses a wide phonon gap, making it an ideal host for studying substitutional impurity modes. This work fits a rigid-ion model with 11 parameters (RIM 11) to experimental phonon data for InP and applies a Green's function method to predict the local and gap mode frequencies of substitutional impurities. The task is to implement the model, compute the elastic constants and phonon frequencies at high-symmetry points, compute the two-phonon summation density of states, and determine the local mode frequency for a boron impurity substituting for indium.

## Approach
Use a rigid-ion model (RIM 11) for InP that includes general interactions between nearest and next-nearest neighbours together with long-range Coulomb forces. Construct the dynamical matrix for the sphalerite structure using the published 11-parameter set. Solve the eigenvalue problem at the high-symmetry points Γ, X, L to obtain phonon frequencies and derive the three independent elastic constants C11, C12, C44 from the long-wavelength limit of the dynamical matrix.

Next, compute the one-phonon frequency spectrum on a fine mesh of k-points covering the Brillouin zone, then histogram the summed frequencies ω_i(k)+ω_j(k) over all pairs of phonon branches to obtain the two-phonon summation density of states g+(ω).

Finally, implement the Green's function method for an isolated substitutional impurity. Use the host InP dynamical matrix, set up a 15×15 defect space for the F₂ symmetry block, and consider a boron impurity (mass 11 u) at the indium site with a nearest-neighbour force-constant defect parameter t = -0.25 (equivalent to Δf/f = +0.25). Solve for bound states in the phonon gap and above the maximum phonon frequency, extracting the local mode frequency and any gap mode frequency.

## Reproduction target
Compute the following:
1. Elastic constants C11, C12, C44 (in 10^11 dyn/cm^2) and phonon frequencies at Γ, X, L points (in 10^12 Hz) for InP, written to phonon_results.csv.
2. The two-phonon summation density of states g+(ω) as a histogram covering 0–700 cm⁻¹, written to gplus_dos.json.
3. The F₂ local mode frequency (in cm⁻¹) and any gap mode frequency for a boron atom substituting for indium, computed with the nearest-neighbour force-constant defect t = -0.25, written to impurity_modes.json.

## Assets
The rigid-ion model (RIM 11) parameters for InP are:

- Lattice constant a0 = 2.9343 Å
- Atomic masses: M1 (P) = 30.93 u, M2 (In) = 114.82 u
- Effective charge Z = 0.82
- Force constants (in units of 10^5 dyn·cm⁻¹):
  A = -0.365, B = -0.100, C1 = -0.017, D1 = -0.003, E1 = +0.05, F1 = -0.071,
  C2 = -0.043, D2 = -0.120, E2 = +0.110, F2 = +0.177

No external datasets or tools beyond standard Python numerical libraries (NumPy, SciPy) are required.

## Workflow steps

### Step 1: Compute RIM 11 phonon properties for InP
- Role: scored (load-bearing)
- Action: Implement the rigid-ion model RIM 11 for InP using the published 11-parameter set. Construct the dynamical matrix D(k) for the sphalerite structure, solve the eigenvalue problem at high-symmetry points Γ, X, L to obtain phonon frequencies, and derive the three independent elastic constants C11, C12, C44 from the long-wavelength limit of the dynamical matrix.
- Output file: `/app/outputs/phonon_results.csv`
- Format: csv
- Contract: CSV with header: quantity, computed_value, unit. The quantity column contains string identifiers: C11, C12, C44 (elastic constants in 10^11 dyn/cm^2), ω_LO(Γ), ω_TO(Γ), ω_LA(X), ω_LO(X), ω_TA(X), ω_TO(X), ω_LO(L), ω_LA(L), ω_TA(L), ω_TO(L) (frequencies in 10^12 Hz).
- Scoring: scored by hidden verifier

### Step 2: Compute two-phonon summation density of states g+(ω)
- Role: scored
- Action: Using the RIM 11 model, compute the one-phonon frequency spectrum on a fine mesh of k-points covering the Brillouin zone (e.g., 27,791 points as in the paper). Compute the two-phonon summation density of states g+(ω) by histogramming the summed frequencies ω_i(k) + ω_j(k) over all pairs of phonon branches i, j.
- Output file: `/app/outputs/gplus_dos.json`
- Format: json
- Contract: JSON object with keys: omega_cm1 (array of frequency bin centers in cm-1), gplus (array of corresponding density values). Arrays of equal length covering 0 to roughly 700 cm-1, bin width approximately 6.93 cm-1.
- Scoring: scored by hidden verifier

### Step 3: Compute F₂ local mode frequency for B impurity on In site
- Role: scored
- Action: Implement the Green's function method for an isolated substitutional impurity in the sphalerite lattice. Use the host InP dynamical matrix from the RIM 11 model. Set up the 15×15 defect space for the F₂ symmetry block. Assume the impurity is a boron atom (mass 11 u) substituting for indium, and use a nearest-neighbour force-constant defect parameter t = -0.25 (i.e., Δf/f = +0.25). Solve for the bound state(s) in the phonon gap and above the maximum phonon frequency. Extract the local mode frequency (if any) and the gap mode frequency (if any).
- Output file: `/app/outputs/impurity_modes.json`
- Format: json
- Contract: JSON object with keys: local_mode_cm1 (float, frequency of the local mode above the maximum phonon frequency, in cm-1), gap_mode_cm1 (float or null, frequency of any gap mode in the phonon gap, in cm-1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_results.csv`
- `/app/outputs/gplus_dos.json`
- `/app/outputs/impurity_modes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_results.csv
- path: `/app/outputs/phonon_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of computed elastic constants and phonon frequencies at high-symmetry points. Rows with quantity='C11','C12','C44' give elastic constants; rows with ω_LO(Γ), ω_TO(Γ), ω_LA(X), ω_LO(X), ω_TA(X), ω_TO(X), ω_LO(L), ω_LA(L), ω_TA(L), ω_TO(L) give phonon frequencies.
- schema:
  - `type`: table
  - `required_columns`: `quantity`, `computed_value`, `unit`
  - `units`:
    - `computed_value`: 10^11 dyn/cm^2 for elastic constants; 10^12 Hz for frequencies

### gplus_dos.json
- path: `/app/outputs/gplus_dos.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Histogram of the two-phonon summation density of states g+(ω). Arrays are of equal length and cover 0–700 cm-1.
- schema:
  - `type`: object
  - `required`:
    - `omega_cm1`: array of floats
    - `gplus`: array of floats
  - `items`:
    - `omega_cm1`: frequency bin center in cm-1
    - `gplus`: density value (unitless)

### impurity_modes.json
- path: `/app/outputs/impurity_modes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Local mode and gap mode frequencies for a B impurity on the In site, computed with t = -0.25.
- schema:
  - `type`: object
  - `required`:
    - `local_mode_cm1`: float (or null if none)
    - `gap_mode_cm1`: float or null

Notes: All scored artifacts derive from the published RIM 11 parameter set; the fitting procedure is not required. The checker compares computed values to paper-reported experimental references within suitable tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "quantity",
          "computed_value",
          "unit"
        ],
        "units": {
          "computed_value": "10^11 dyn/cm^2 for elastic constants; 10^12 Hz for frequencies"
        }
      },
      "description": "Table of computed elastic constants and phonon frequencies at high-symmetry points. Rows with quantity='C11','C12','C44' give elastic constants; rows with ω_LO(Γ), ω_TO(Γ), ω_LA(X), ω_LO(X), ω_TA(X), ω_TO(X), ω_LO(L), ω_LA(L), ω_TA(L), ω_TO(L) give phonon frequencies."
    },
    {
      "file": "gplus_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "omega_cm1": "array of floats",
          "gplus": "array of floats"
        },
        "items": {
          "omega_cm1": "frequency bin center in cm-1",
          "gplus": "density value (unitless)"
        }
      },
      "description": "Histogram of the two-phonon summation density of states g+(ω). Arrays are of equal length and cover 0–700 cm-1."
    },
    {
      "file": "impurity_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "local_mode_cm1": "float (or null if none)",
          "gap_mode_cm1": "float or null"
        }
      },
      "description": "Local mode and gap mode frequencies for a B impurity on the In site, computed with t = -0.25."
    }
  ],
  "notes": "All scored artifacts derive from the published RIM 11 parameter set; the fitting procedure is not required. The checker compares computed values to paper-reported experimental references within suitable tolerances."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage's output artifact. The verifier reads your submitted CSV/JSON files, extracts the required quantities, and compares them against reference values derived from the original experimental data. Structural checks (e.g., peak locations) may also be applied. Reporting a number alone is insufficient; the verifier uses the full data in your files. The stages are weighted: Stage 1 (phonon results) contributes 40% of the total reward, Stage 2 (g+ DOS) 30%, and Stage 3 (impurity modes) 30%. The final score is the weighted sum.
