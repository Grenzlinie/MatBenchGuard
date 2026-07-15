# Curvature-corrected phonon dispersion and symmetry analysis of carbon nanotubes

## Problem background
A single-wall carbon nanotube (SWCNT) can be formed by rolling a graphene sheet into a cylinder. Its vibrational properties are important for experimental characterisation, in particular the radial breathing mode (RBM) whose frequency–diameter relationship is used to identify tube diameter. However, the phonon dispersion relations cannot be obtained by simple zone‑folding from 2D graphite because the curvature of the tube modifies the atomic force constants. A proper calculation requires adapting the flat‑graphite force‑constant tensor to the curved cylindrical surface. Additionally, the symmetry classification of the vibrational modes at the Brillouin zone centre determines which modes are Raman‑active and infrared‑active, yet earlier symmetry assignments for armchair and zigzag tubes (using point groups Dₙₕ or Dₙₔ) may not capture the full space‑group symmetry. This work addresses both challenges by computing curvature‑corrected phonon frequencies and performing a consistent group‑theory analysis.

## Approach
The calculation starts from the 2D graphite force‑constant parameters of Jishi et al. (Chem. Phys. Lett. 209, 77, 1993), which describe interactions up to the 18 nearest neighbours. For each armchair (n,n) and zigzag (n,0) nanotube, the Cartesian atomic positions are generated from the chiral indices and the graphene lattice constant (~0.246 nm). To account for curvature, the 3×3 force‑constant tensor of each interacting atom pair is rotated five successive times into a local cylindrical coordinate frame, yielding curvature‑adapted force constants. Using these tensors, the dynamical matrix at the Γ point (k=0) is constructed and diagonalised, giving phonon eigenfrequencies (in cm⁻¹) and the corresponding displacement eigenvectors. Each eigenvector is then assigned to an irreducible representation of the D₂ₙₕ point group (the factor group of the non‑symmorphic space group of these tubes), and the Raman and infrared activity is decided according to the group selection rules. The lowest‑frequency mode with A₁₉ symmetry is identified as the radial breathing mode.

## Reproduction target
For armchair nanotubes with n = m = 4 through 19 and zigzag nanotubes with m = 0, n = 5 through 19, compute the Γ‑point phonon frequencies and symmetry labels. The required output is a single JSON file (step_01_phonon_results.json) that for each tube lists: the (n,m) indices, diameter, the frequency of the identified RBM, all Γ‑point modes with their frequency, irreducible representation label, and Raman/IR activity flags, together with the total counts of Raman‑active and IR‑active modes. The underlying verification goals are: (i) the relationship between the RBM frequency ω and the tube diameter d — specifically, for tubes with d > 1.0 nm the product ω·d should approach a constant value; (ii) the absolute frequencies of the low‑energy and high‑energy A₁₉ modes for the (12,12) armchair tube and the (12,0) zigzag tube; (iii) the total numbers of Raman‑active and IR‑active modes obtained from the symmetry analysis under D₂ₙₕ.

## Assets

- Jishi et al. 2D graphite force constants (1993): 10.1016/0009-2614(93)87057-5

## Workflow steps

### Step 1: Generate nanotube geometries
- Role: process
- Action: For armchair nanotubes (n=m, n=4..19) and zigzag nanotubes (m=0, n=5..19), compute the chiral vector and lattice vectors, construct the cylindrical unit cell, and generate the Cartesian atomic positions of all carbon atoms in the unit cell using the graphene lattice constant (≈0.246 nm).
- Evidence: `/app/outputs/geometry_check.txt`

### Step 2: Apply curvature correction to force constants
- Role: process
- Action: Obtain the 2D graphite force-constant tensor parameters from Jishi et al. (1993). For each tube, for each pair of interacting atoms (18 nearest neighbours), determine the local cylindrical coordinate frame and apply the sequence of five rotations to the 3×3 force-constant tensor to adapt it to the curved surface.
- Evidence: `/app/outputs/rotated_force_constants.pkl`

### Step 3: Build dynamical matrix and diagonalize
- Role: process
- Action: For each tube, construct the dynamical matrix at the Γ point (wavevector k=0) using the curvature-corrected force constants and the atomic masses. Diagonalize the matrix to obtain the phonon eigenfrequencies (in cm⁻¹) and the corresponding eigenvectors (displacement patterns).
- Evidence: `/app/outputs/raw_eigensolutions.json`

### Step 4: Classify modes by symmetry and write scored output
- Role: scored (load-bearing)
- Action: For each tube, classify every Γ‑point mode into an irreducible representation of the D₂ₙₕ point group using the computed eigenvectors and the character table of D₂ₙₕ; determine whether each mode is Raman‑active, IR‑active, or silent; identify the radial breathing mode as the lowest‑frequency A₁₉ mode; compute the tube diameter from the chiral indices. Write the complete structured results to step_01_phonon_results.json.
- Output file: `/app/outputs/step_01_phonon_results.json`
- Format: json
- Contract: {"armchair": [{"n": int, "m": int, "diameter_nm": float, "rbm_frequency_cm-1": float, "gamma_modes": [{"frequency_cm-1": float, "irrep": string, "raman_active": bool, "ir_active": bool}], "raman_active_total": int, "ir_active_total": int}], "zigzag": [same structure]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_results.json
- path: `/app/outputs/step_01_phonon_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Phonon frequencies at Γ point for armchair (n=4..19) and zigzag (n=5..19) nanotubes, along with symmetry classification, Raman/IR activity, and radial breathing mode identification.
- schema:
  - `type`: object
  - `required`:
    - `armchair`: array
    - `zigzag`: array
  - `items`:
    - `armchair_item`:
      - `n`: int
      - `m`: int
      - `diameter_nm`: float
      - `rbm_frequency_cm-1`: float
      - `gamma_modes`: array of objects with keys: frequency_cm-1 (float), irrep (string), raman_active (bool), ir_active (bool)
      - `raman_active_total`: int
      - `ir_active_total`: int
    - `zigzag_item`: same structure as armchair_item
  - `required_columns`:
  - `units`:
    - `diameter_nm`: nm
    - `frequency_cm-1`: cm⁻¹

Notes: The checker will recompute the ω·d product for the radial breathing mode and verify constancy, compare specific A₁₉ mode frequencies within tolerances, and count Raman‑active (8) and IR‑active (3) modes; it will also verify that all irreducible representation labels belong to the D₂ₙₕ point group.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "armchair": "array",
          "zigzag": "array"
        },
        "items": {
          "armchair_item": {
            "n": "int",
            "m": "int",
            "diameter_nm": "float",
            "rbm_frequency_cm-1": "float",
            "gamma_modes": "array of objects with keys: frequency_cm-1 (float), irrep (string), raman_active (bool), ir_active (bool)",
            "raman_active_total": "int",
            "ir_active_total": "int"
          },
          "zigzag_item": "same structure as armchair_item"
        },
        "required_columns": [],
        "units": {
          "diameter_nm": "nm",
          "frequency_cm-1": "cm⁻¹"
        }
      },
      "description": "Phonon frequencies at Γ point for armchair (n=4..19) and zigzag (n=5..19) nanotubes, along with symmetry classification, Raman/IR activity, and radial breathing mode identification."
    }
  ],
  "notes": "The checker will recompute the ω·d product for the radial breathing mode and verify constancy, compare specific A₁₉ mode frequencies within tolerances, and count Raman‑active (8) and IR‑active (3) modes; it will also verify that all irreducible representation labels belong to the D₂ₙₕ point group."
}
```

## How you are scored
A hidden verifier inspects your submitted `step_01_phonon_results.json`. It independently recomputes ω·d from your RBM frequencies and diameters to assess whether the product is approximately constant for d > 1.0 nm; it compares your reported A₁₉ mode frequencies for (12,12) and (12,0) to reference values with hidden tolerances; and it verifies the total counts of Raman‑active and IR‑active modes. The verifier also checks that every irreducible representation label belongs to D₂ₙₕ and that the activity flags are consistent with the selection rules. Each check contributes a weighted reward; the main weight is on the ω·d relationship and the specific A₁₉ frequencies. The final reward is a single float between 0 (no valid reproduction) and 1 (full reproduction). Simply reporting a number that matches a literature value is not sufficient — the verifier evaluates the quantitative consistency of the output you produce from the full computational pipeline.
