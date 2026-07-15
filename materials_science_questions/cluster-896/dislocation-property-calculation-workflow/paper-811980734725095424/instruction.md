# Tight-Binding Dislocation Core and Peierls Stress Calculation for bcc Metals

## Problem background
Plastic deformation of body-centred cubic (b.c.c.) transition metals shows a pronounced orientation dependence of the Peierls stress, and this orientation dependence is known to differ between metals like α-Fe (type‑A) and those like W and Nb (type‑B). Earlier models based on pair potentials could not capture the effect of d‑band filling. This task investigates the motion of an (a/2)⟨111⟩ screw dislocation by directly computing the dimensionless Peierls stress τ_p/μ for three shear orientations and the dislocation core energy at zero stress, using a tight‑binding‑type electronic theory as described below.

## Approach
The d‑electron contribution to cohesion is treated with a second‑moment tight‑binding approximation. The local density of states on each atom is represented by a Gaussian fitted to the second moment μ_{2i} = Σ_j β_{ij}², where the effective resonance integral β_{ij} decays exponentially with distance: β_{ij} = β₀ exp(−q r_{ij}) with q r₀ ≈ 3. The band‑structure energy is obtained by integrating over occupied states up to the Fermi energy. Short‑range repulsive core‑core interactions are added via a Born‑Mayer potential for Fe and a power‑law potential for W and Nb. The model parameters β₀ and the repulsive‑potential parameters for each metal are fitted to experimental values of the cohesive energy, bulk modulus, and elastic constant C₄₄.

A cylindrical crystallite of 102 ⟨111⟩ atomic rows is constructed with periodic boundary conditions along the dislocation line. An (a/2)⟨111⟩ screw dislocation is introduced using the isotropic linear‑elasticity displacement field. Homogeneous shear stresses corresponding to three orientations (χ = 0°, −30°, 30°) are applied, and the atomic positions along the dislocation line are relaxed iteratively until the energy change per iteration becomes negligible. The Peierls stress is identified as the minimum applied shear stress at which the dislocation moves to the next low‑energy position; the zero‑stress core energy is obtained from the relaxed configuration under no applied stress.

## Reproduction target
Compute the dimensionless Peierls stress τ_p/μ for α‑Fe, W, and Nb under shear on the (110) plane (χ = 0°), on the (112) plane in the twinning direction (χ = −30°), and on the (112) plane in the anti‑twinning direction (χ = 30°). Also compute the dislocation core energy per 102 atomic rows of length b (in eV) at zero applied stress for each of the three metals. Write the Peierls stresses to /app/outputs/peierls_stresses.json and the core energies to /app/outputs/core_energies.json, exactly following the output contract below.

## Assets

- Experimental cohesive energies, bulk moduli, and elastic constants C44 for α-Fe, W, Nb
- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Fit tight-binding model parameters
- Role: process
- Action: Using the analytical formulas for cohesive energy, bulk modulus, and C44 with second-nearest neighbors, fit the electronic parameter β₀ and repulsive potential parameters (C₀, p or n) for α‑Fe, W, and Nb to the experimental values. Use Born-Mayer repulsion for Fe and power-law repulsion for W and Nb with qr₀=3.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 2: Run screw dislocation relaxation simulations
- Role: process
- Action: For each metal (Fe, W, Nb) and each shear orientation (χ=0°, -30°, 30°), construct a cylindrical crystallite of 102 ⟨111⟩ atomic rows with periodic boundary conditions along the dislocation line. Introduce an (a/2)⟨111⟩ screw dislocation using isotropic linear elasticity, apply homogeneous shear stress, and relax atomic positions (z-component only) iteratively until the energy change per iteration falls below convergence. For each metal, also relax at zero stress.
- Evidence: `/app/outputs/relaxation_data.npz`

### Step 3: Extract Peierls stresses
- Role: scored (load-bearing)
- Action: From the relaxation outputs of step 2, determine the Peierls stress τ_p/μ for each metal and orientation as the minimum applied shear stress at which the dislocation moves to the next low-energy position. Write τ_p/μ values for χ=0°, -30°, and 30° to /app/outputs/peierls_stresses.json.
- Output file: `/app/outputs/peierls_stresses.json`
- Format: json
- Contract: JSON object with keys 'Fe', 'Nb', 'W'. Each value is an object with keys 'chi0', 'chi_neg30', 'chi_pos30' mapping to floats (τ_p/μ).
- Scoring: scored by hidden verifier

### Step 4: Extract zero-stress core energies
- Role: scored
- Action: From the zero-stress relaxation outputs of step 2, extract the dislocation core energy per 102 atomic rows of length b (in eV) for each metal. Write the values to /app/outputs/core_energies.json.
- Output file: `/app/outputs/core_energies.json`
- Format: json
- Contract: JSON object with keys 'Fe', 'Nb', 'W' mapping to floats (eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/peierls_stresses.json`
- `/app/outputs/core_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### peierls_stresses.json
- path: `/app/outputs/peierls_stresses.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dimensionless Peierls stresses τ_p/μ for each metal and shear orientation.
- schema:
  - `type`: object
  - `required`:
    - `Fe`: object
    - `Nb`: object
    - `W`: object
  - `items`:
    - `chi0`: float (τ_p/μ)
    - `chi_neg30`: float (τ_p/μ)
    - `chi_pos30`: float (τ_p/μ)
  - `units`:
    - `chi0`: dimensionless
    - `chi_neg30`: dimensionless
    - `chi_pos30`: dimensionless

### core_energies.json
- path: `/app/outputs/core_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zero-stress dislocation core energy in eV for each metal.
- schema:
  - `type`: object
  - `required`:
    - `Fe`: float
    - `Nb`: float
    - `W`: float
  - `items`: object
  - `units`:
    - `Fe`: eV
    - `Nb`: eV
    - `W`: eV

Notes: The hidden checker compares agent-reported values to paper-reported references with absolute tolerances and also verifies the relative ordering: for Fe, τ_p(χ=0°) < τ_p(χ=-30°) < τ_p(χ=30°); for W and Nb, τ_p(χ=-30°) < τ_p(χ=0°) < τ_p(χ=30°).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "peierls_stresses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe": "object",
          "Nb": "object",
          "W": "object"
        },
        "items": {
          "chi0": "float (τ_p/μ)",
          "chi_neg30": "float (τ_p/μ)",
          "chi_pos30": "float (τ_p/μ)"
        },
        "units": {
          "chi0": "dimensionless",
          "chi_neg30": "dimensionless",
          "chi_pos30": "dimensionless"
        }
      },
      "description": "Dimensionless Peierls stresses τ_p/μ for each metal and shear orientation."
    },
    {
      "file": "core_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe": "float",
          "Nb": "float",
          "W": "float"
        },
        "items": {},
        "units": {
          "Fe": "eV",
          "Nb": "eV",
          "W": "eV"
        }
      },
      "description": "Zero-stress dislocation core energy in eV for each metal."
    }
  ],
  "notes": "The hidden checker compares agent-reported values to paper-reported references with absolute tolerances and also verifies the relative ordering: for Fe, τ_p(χ=0°) < τ_p(χ=-30°) < τ_p(χ=30°); for W and Nb, τ_p(χ=-30°) < τ_p(χ=0°) < τ_p(χ=30°)."
}
```

## How you are scored
A hidden verifier reads your peierls_stresses.json and core_energies.json and independently scores them. It compares each computed τ_p/μ value and core energy against hidden reference values with appropriate tolerances. It also verifies that the relative ordering of τ_p/μ across the three shear orientations is consistent with the expected pattern for each metal. The final reward is a weighted combination of these checks. Simply reporting numbers without executing the required simulation pipeline is unlikely to satisfy both the absolute‑value tolerances and the ordering requirement.
