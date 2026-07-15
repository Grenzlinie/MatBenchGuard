# DFT+U simulations of charge-ordered metastable state in La0.25Sr0.75TiO3 bulk and thin films

## Problem background
Charge ordering (CO) in transition metal oxides involves periodic modulation of electron density and lattice distortion, often competing with superconductivity or colossal magnetoresistance. This work addresses the question of whether a charge-ordered phase can exist in electron-doped SrTiO₃ at the lowest d-electron occupancy, specifically in La₀.₂₅Sr₀.₇₅TiO₃ (LSTO). Density functional theory (DFT) calculations have been used to examine a metastable insulating CO state that exhibits alternating expanded and contracted TiO₆ octahedra, antiferromagnetic ordering, and a characteristic distortion pattern. The stabilization of this state in thin films is proposed to be triggered by surface distortion. Your task is to reproduce the key computational predictions for this CO state in both bulk and thin-film geometries.

## Approach
You will perform spin-polarized DFT+U calculations using an open-source plane-wave code (e.g., Quantum ESPRESSO) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the rotationally invariant Hubbard correction. The reported Hubbard U parameters are (U-J) = 5 – 0.64 eV for Ti 3d orbitals and (U-J) = 11 – 0.68 eV for La 4f orbitals. Two systems must be studied:
- Bulk: a 2×2×2 periodic supercell of La₀.₂₅Sr₀.₇₅TiO₃, initialized with an antiferromagnetic spin ordering. The structure is relaxed to locate the metastable charge-ordered state, after which the octahedral lattice modulation is decomposed into four distortion modes (inter‑layer breathing d1, intra‑layer breathing d2, Jahn‑Teller d3, and antiferrodistortive rotation θz).
- Thin film: a slab model consisting of 6 unit cells of LSTO on a TiO₂-terminated SrTiO₃(001) substrate, with a vacuum layer and fixed bottom substrate layers. After relaxation, the per‑layer apical‑oxygen‑to‑apical‑oxygen distance is extracted to reveal the octahedral breathing pattern.
For both systems, the electronic band gap and total magnetic moment are computed to characterise the insulating and magnetic properties.

## Reproduction target
Produce the following scored artifacts under /app/outputs:
1. `bulk_distortion_modes.json` – the four distortion amplitudes (d1, d2, d3 in picometers; θz in degrees) for the relaxed bulk CO state.
2. `bulk_band_gap_moment.json` – the band gap (eV) and total magnetic moment (μB) of the bulk CO state.
3. `slab_layer_heights.csv` – a table of layer indices (starting at -1 for the topmost layer) and the corresponding apical oxygen-to-oxygen distance (pm) for each non-fixed layer in the relaxed slab.
4. `slab_band_gap_moment.json` – the band gap (eV) and total magnetic moment (μB) of the slab.
All calculations must be carried out with the specified DFT+U protocol and the listed public structural references; the outputs must conform to the described formats.

## Assets

- Quantum ESPRESSO (DFT package): https://www.quantum-espresso.org/
- PSLibrary pseudopotentials for Sr, Ti, La, O: https://www.quantum-espresso.org/pseudopotentials/ps-library/
- Crystal structure of SrTiO3: https://materialsproject.org/materials/mp-4651
- Crystal structure of LaTiO3: https://materialsproject.org/materials/mp-21159

## Workflow steps

### Step 1: Construct bulk LSTO supercell
- Role: process
- Action: Build a 2×2×2 periodic supercell of La0.25Sr0.75TiO3 with a specific La/Sr arrangement on the A-sites and Ti on the B-sites. Set up an initial antiferromagnetic spin ordering consistent with the expected charge-ordered phase (alternating spin sublattice).
- Evidence: `/app/outputs/bulk_supercell_input.cif`

### Step 2: Perform bulk DFT+U relaxation
- Role: process
- Action: Run spin-polarized DFT+U geometry optimization of the bulk supercell using an open-source DFT code with the PBE functional and a rotationally invariant Hubbard U correction (U-J = 5 - 0.64 eV for Ti 3d and U-J = 11 - 0.68 eV for La 4f). Converge Hellmann-Feynman forces to 0.01 eV/Å using a Γ-centered k‑point mesh appropriate for the supercell (e.g., 8×8×4). Obtain the relaxed atomic positions of the metastable charge-ordered insulating state.
- Evidence: `/app/outputs/relaxed_bulk_structure.cif`

### Step 3: Compute bulk distortion amplitudes
- Role: scored (load-bearing)
- Action: From the relaxed bulk charge-ordered structure, decompose the octahedral lattice modulation into the four distortion modes: inter-layer breathing (d1), intra-layer breathing (d2), Jahn-Teller (d3), and antiferrodistortive rotation (θz). Output the amplitudes in picometers and degrees.
- Output file: `/app/outputs/bulk_distortion_modes.json`
- Format: json
- Contract: { 'd1_pm': number, 'd2_pm': number, 'd3_pm': number, 'theta_z_deg': number }
- Scoring: scored by hidden verifier

### Step 4: Report bulk electronic properties
- Role: scored
- Action: Compute the electronic band gap (eV) and the total magnetic moment (μB) for the bulk charge-ordered state. Write a JSON file with band_gap_eV and total_magnetization_muB.
- Output file: `/app/outputs/bulk_band_gap_moment.json`
- Format: json
- Contract: { 'band_gap_eV': number, 'total_magnetization_muB': number }
- Scoring: scored by hidden verifier

### Step 5: Build LSTO/STO slab model
- Role: process
- Action: Construct a periodic slab consisting of 6 unit cells of La0.25Sr0.75TiO3 on a SrTiO3(001) substrate with TiO2 termination. Include a vacuum layer. Fix several bottom substrate layers and set the in-plane lattice constant to that of STO.
- Evidence: `/app/outputs/slab_input.cif`

### Step 6: Perform slab DFT+U relaxation
- Role: process
- Action: Run spin-polarized DFT+U relaxation on the slab model with the same functional and Hubbard U corrections as the bulk. Allow all atoms to relax except the fixed bottom STO layers, until forces converge to 0.01 eV/Å. Use a Γ-centered k‑point mesh appropriate for the slab (e.g., 4×4×1). Obtain the relaxed geometry of the charge-ordered state.
- Evidence: `/app/outputs/relaxed_slab_structure.cif`

### Step 7: Extract slab layer-resolved octahedral heights
- Role: scored
- Action: For each non-fixed TiO6 layer in the relaxed slab, compute the apical oxygen-to-oxygen distance (TiO6 octahedron height) in picometers. Output a CSV with columns layer_index (integer, starting from -1 for the topmost layer) and Oap_Oap_distance_pm (float).
- Output file: `/app/outputs/slab_layer_heights.csv`
- Format: csv
- Contract: layer_index (int), Oap_Oap_distance_pm (float)
- Scoring: scored by hidden verifier

### Step 8: Report slab electronic properties
- Role: scored
- Action: Compute the electronic band gap (eV) and total magnetic moment (μB) for the relaxed slab. Output a JSON file with band_gap_eV and total_magnetization_muB.
- Output file: `/app/outputs/slab_band_gap_moment.json`
- Format: json
- Contract: { 'band_gap_eV': number, 'total_magnetization_muB': number }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_distortion_modes.json`
- `/app/outputs/bulk_band_gap_moment.json`
- `/app/outputs/slab_layer_heights.csv`
- `/app/outputs/slab_band_gap_moment.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_distortion_modes.json
- path: `/app/outputs/bulk_distortion_modes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Distortion mode amplitudes of the bulk charge-ordered state. The checker compares each value to the paper's reported numbers with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `d1_pm`: number (pm)
    - `d2_pm`: number (pm)
    - `d3_pm`: number (pm)
    - `theta_z_deg`: number (degrees)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `d1_pm`: picometers
    - `d2_pm`: picometers
    - `d3_pm`: picometers
    - `theta_z_deg`: degrees

### bulk_band_gap_moment.json
- path: `/app/outputs/bulk_band_gap_moment.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic band gap (must exceed 0.1 eV) and total magnetic moment (absolute value must be less than 1 μB) to confirm insulating antiferromagnetic character.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number (eV)
    - `total_magnetization_muB`: number (μB)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `band_gap_eV`: electronvolts
    - `total_magnetization_muB`: Bohr magnetons

### slab_layer_heights.csv
- path: `/app/outputs/slab_layer_heights.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Layer-resolved apical oxygen to oxygen distance (TiO6 octahedron height) for each non-fixed layer in the slab. The checker verifies that consecutive layers show an alternating expanded/contracted pattern (consecutive height difference >2 pm for at least three adjacent pairs in the top six layers).
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `layer_index`, `Oap_Oap_distance_pm`
  - `units`:
    - `Oap_Oap_distance_pm`: picometers

### slab_band_gap_moment.json
- path: `/app/outputs/slab_band_gap_moment.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic band gap (>0.1 eV) and total magnetic moment (|moment| < 1 μB) for the slab, confirming insulating antiferromagnetic nature.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number (eV)
    - `total_magnetization_muB`: number (μB)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `band_gap_eV`: electronvolts
    - `total_magnetization_muB`: Bohr magnetons

Notes: The scoring tiers are: reference_match (tolerance-based comparison to hidden paper gold) for bulk distortion amplitudes; threshold_or_better for band gaps and magnetic moments (insulating/AFM criteria); structural_audit for slab layer-height pattern. All process steps are required to reach the scored load-bearing artifact bulk_distortion_modes.json and the other scored outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_distortion_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "d1_pm": "number (pm)",
          "d2_pm": "number (pm)",
          "d3_pm": "number (pm)",
          "theta_z_deg": "number (degrees)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "d1_pm": "picometers",
          "d2_pm": "picometers",
          "d3_pm": "picometers",
          "theta_z_deg": "degrees"
        }
      },
      "description": "Distortion mode amplitudes of the bulk charge-ordered state. The checker compares each value to the paper's reported numbers with appropriate tolerances."
    },
    {
      "file": "bulk_band_gap_moment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number (eV)",
          "total_magnetization_muB": "number (μB)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "band_gap_eV": "electronvolts",
          "total_magnetization_muB": "Bohr magnetons"
        }
      },
      "description": "Electronic band gap (must exceed 0.1 eV) and total magnetic moment (absolute value must be less than 1 μB) to confirm insulating antiferromagnetic character."
    },
    {
      "file": "slab_layer_heights.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "layer_index",
          "Oap_Oap_distance_pm"
        ],
        "units": {
          "Oap_Oap_distance_pm": "picometers"
        }
      },
      "description": "Layer-resolved apical oxygen to oxygen distance (TiO6 octahedron height) for each non-fixed layer in the slab. The checker verifies that consecutive layers show an alternating expanded/contracted pattern (consecutive height difference >2 pm for at least three adjacent pairs in the top six layers)."
    },
    {
      "file": "slab_band_gap_moment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number (eV)",
          "total_magnetization_muB": "number (μB)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "band_gap_eV": "electronvolts",
          "total_magnetization_muB": "Bohr magnetons"
        }
      },
      "description": "Electronic band gap (>0.1 eV) and total magnetic moment (|moment| < 1 μB) for the slab, confirming insulating antiferromagnetic nature."
    }
  ],
  "notes": "The scoring tiers are: reference_match (tolerance-based comparison to hidden paper gold) for bulk distortion amplitudes; threshold_or_better for band gaps and magnetic moments (insulating/AFM criteria); structural_audit for slab layer-height pattern. All process steps are required to reach the scored load-bearing artifact bulk_distortion_modes.json and the other scored outputs."
}
```

## How you are scored
A hidden verifier independently examines each submitted artifact. For the bulk distortion modes, your computed values are compared against hidden reference values with absolute tolerances; better agreement earns higher credit. For the band gaps and magnetic moments, a threshold check is applied: the band gap must exceed a minimum value (confirming insulating behaviour), and the total magnetization must be consistent with antiferromagnetism. For the slab layer heights, the verifier audits the pattern—consecutive layers should alternate between larger and smaller distances, forming the expected expanded/contracted sequence. The final reward is a weighted sum of the scores from all four artifacts. Simply reporting the paper’s final numbers without running the full computational workflow will not pass these checks, because the tolerances, thresholds, and pattern requirements are stringent and require actual simulation results.
