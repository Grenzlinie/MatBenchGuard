# Strain-Induced Band Shifts from Subsurface Point Stressor in GaN

## Problem background
Subsurface point stressors such as quantum dots or strain centres in wurtzite GaN generate non‑uniform strain fields that locally modify the conduction and valence band edges. Quantifying the resulting band‑edge shifts is critical for understanding lateral carrier confinement in strain‑engineered devices. This task investigates the strain field from a single subsurface In0.5Ga0.5N point stressor (modelled as a point dilatation) and applies Bir–Pikus k·p perturbation theory to compute the induced shifts of the band edges. Two open quantities characterise the effect: the lateral conduction‑band localisation depth near the free surface, and the depth along the symmetry axis at which the top two valence bands cross.

## Approach
The strain field is obtained from the analytical solution for a point dilatation in an isotropic elastic half‑space. The stressor is located at depth h below the (0001) surface and has effective strength S = f V, where f is the average lattice misfit of the In0.5Ga0.5N island and V = 200π nm³ is the island volume. All strain components εij are computed on a (r,z) grid within the valid point‑source region (r > ℓc ≈ 8 nm, 0 < z < h) and in the far field, using Poisson’s ratio ν = 0.234.

At each grid point the strain tensor enters a 6×6 Bir–Pikus k·p Hamiltonian for wurtzite GaN with the deformation potentials given in the workflow steps. Diagonalising the Hamiltonian yields the conduction‑band edge shift and three valence‑band eigenvalues. From these results two headline quantities are extracted:
- The minimum conduction‑band shift near the surface (r = 0, small z) relative to the far‑field value – the lateral electron localisation depth.
- The depth z along the r = 0 axis where the top and middle valence‑band energies become equal – the valence‑band crossing depth.
Both values are saved in the final output file.

## Reproduction target
Using the supplied stressor parameters (depth h = 41 nm, Poisson ratio ν = 0.234, effective strength S = f V with f = 0.0507 and V = 200π nm³) and the GaN deformation potentials listed in Step 2, compute the strain tensor grid for the point‑stressor model and then perform the 6×6 k·p diagonalisation on that grid. Extract the two quantities described above and write them as numbers with units meV and nm into the file /app/outputs/step_01_results.json under the keys cb_localization_depth_mev and vb_crossing_depth_nm. The task is self‑contained; all necessary physical constants and formulas are specified in the workflow steps and should be implemented by the solver.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute point-stressor strain tensor field
- Role: process
- Action: On a 2D grid of (r,z) spanning the region r>ℓ_c≈8 nm and 0<z<h (and extending into the far-field), compute all strain tensor components ε_{ij} induced by a subsurface point dilatation in an isotropic half-space. Use Poisson ratio ν=0.234, stressor depth h=41 nm, effective strength S=fV with f=0.0507 and V=200π nm³. Save the grid coordinates and at least the hydrostatic strain component to a file (strain_field.npz) for later validation.
- Evidence: `/app/outputs/strain_field.npz`

### Step 2: k·p band-edge shift calculation and quantity extraction
- Role: scored (load-bearing)
- Action: Load the strain field from the previous step. At each point, assemble the 6×6 Bir–Pikus k·p Hamiltonian for wurtzite GaN using the deformation potentials α_∥=α_⊥=-44.5 eV, Δ₁=0.022 eV, Δ₂=Δ₃=0.005 eV, D₁=-41.4 eV, D₂=-33.3 eV, D₃=8.2 eV, D₄=-4.1 eV, D₅=-4.7 eV, D₆=(D₃+4D₅)/√2. Diagonalise to obtain the conduction band edge shift and the three top valence band eigenvalues. Extract (a) the minimum CB shift near the surface (r=0) relative to the far-field value – cb_localization_depth_mev – and (b) the depth z where the top two VB eigenvalues cross along r=0 – vb_crossing_depth_nm. Write both values to step_01_results.json.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: {"cb_localization_depth_mev": <number>, "vb_crossing_depth_nm": <number>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Two key band-structure quantities derived from the strain field: conduction band localization depth (meV) and valence band crossing depth (nm). These values are compared against the paper's hidden reported gold with appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `cb_localization_depth_mev`: number
    - `vb_crossing_depth_nm`: number
  - `units`:
    - `cb_localization_depth_mev`: meV
    - `vb_crossing_depth_nm`: nm

Notes: The checker compares the agent's submitted numbers to the hidden paper gold using an exact-match tolerance (both must be within tolerance for full reward). The agent must compute these from the strain field and k·p diagonalisation; copying from any source will not pass because the hidden gold is not publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "cb_localization_depth_mev": "number",
          "vb_crossing_depth_nm": "number"
        },
        "units": {
          "cb_localization_depth_mev": "meV",
          "vb_crossing_depth_nm": "nm"
        }
      },
      "description": "Two key band-structure quantities derived from the strain field: conduction band localization depth (meV) and valence band crossing depth (nm). These values are compared against the paper's hidden reported gold with appropriate tolerance."
    }
  ],
  "notes": "The checker compares the agent's submitted numbers to the hidden paper gold using an exact-match tolerance (both must be within tolerance for full reward). The agent must compute these from the strain field and k·p diagonalisation; copying from any source will not pass because the hidden gold is not publicly available."
}
```

## How you are scored
A hidden verifier checks your /app/outputs/step_01_results.json and compares the two reported numbers against expected values that follow from a faithful implementation of the described strain and k·p pipeline, using appropriate tolerances. It also performs a structural audit of /app/outputs/strain_field.npz to confirm that a genuine strain computation was carried out. The final reward is a weighted combination of these checks, so simply reporting a number without actually running the calculation will fail the structural validation and/or the tolerance‑based comparisons.
