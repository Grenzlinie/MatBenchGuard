# Cu-Nb amorphous phase formation range from MD simulation with TB-SMA potential

## Problem background
The immiscible Cu-Nb system has a positive heat of formation and no equilibrium compounds. Nevertheless, under far-from-equilibrium conditions, amorphous phases may form. Molecular dynamics (MD) simulations can predict the composition range over which crystal-to-amorphous transitions occur in this alloy. This task addresses the construction of an interatomic potential for Cu-Nb and the use of MD to determine the Nb concentration window that leads to amorphization at 300 K, thereby identifying the glass-forming ability range in this binary system.

## Approach
An n-body interatomic potential based on the tight-binding second-moment approximation (TB-SMA) is built. The total energy has a repulsive pairwise term and a many-body band-structure term. Different functional forms are adopted for different pair types: for Cu–Cu and Cu–Nb, piecewise exponential functions with polynomial cutoff modifications are used; for Nb–Nb, a polynomial repulsive term and a cutoff-modulated exponential many-body term are employed. The potential parameters are determined by fitting to reference properties: for pure Cu and Nb, experimental cohesive energy, lattice constant, elastic constants C11, C12, C44, and bulk modulus; for the cross interactions, ab initio calculated properties of hypothetical Cu ₃Nb (L1₂), CuNb (B2), and CuNb₃ (L1₂) compounds. After fitting, the pure-element potentials are validated by checking that the correct ground-state crystal structures are the most stable. Using the combined potential, MD simulations are carried out at 300 K and zero pressure on fcc Cu-based and bcc Nb-based solid solution models spanning a range of solute concentrations. From the final atomic configurations, pair-correlation functions g(r) are computed and Zallen’s criterion (absence of discernible peaks beyond the third-nearest neighbor) is applied to classify each composition as crystalline or amorphous. The composition interval where amorphization occurs is then extracted from the per-composition classifications.

## Reproduction target
Run the entire workflow: fit the TB-SMA potential parameters, validate the pure-element ground states, perform MD simulations for all specified compositions, analyze the pair-correlation functions, and output the final composition bounds as lower and upper at.% Nb together with a list of all compositions and their amorphous/crystalline flags. The scored artifact is `amorphization_range.json`, which must be produced from scratch by the described methodology and reference data and must be internally consistent with the intermediate g(r) analysis.

## Reference data for potential fitting

The following reference properties (experimental for Cu and Nb; ab initio for the three hypothetical Cu-Nb compounds) are to be used for fitting the TB-SMA potential.

| Property | Cu (exp.) | Nb (exp.) | L1₂ Cu₃Nb (ab initio) | B2 CuNb (ab initio) | L1₂ CuNb₃ (ab initio) |
|----------|-----------|-----------|------------------------|---------------------|------------------------|
| Lattice constant a (Å) | 3.62 | 3.30 | 3.81 | 3.12 | 4.05 |
| Cohesive energy E_c (eV) | 3.49 | 7.57 | 4.18 | 5.35 | 6.40 |
| C11 (Mbar) | 1.68 | 2.47 | 1.49 | 1.69 | 0.94 |
| C12 (Mbar) | 1.22 | 1.35 | 1.54 | 1.70 | 1.92 |
| C44 (Mbar) | 0.76 | 0.29 | 0.48 | 0.48 | 0.44 |
| Bulk modulus B0 (Mbar) | 1.37 | 1.70 | 1.48 | 1.68 | 1.59 |

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- Python scientific stack: pip install scipy numpy ase

## Workflow steps

### Step 1: Fit pure Cu potential
- Role: process
- Action: Determine the parameters of the modified TB-SMA potential for Cu-Cu interactions (repulsive and many-body terms, using piecewise exponential and cutoff-polynomial forms) by fitting to the provided experimental reference properties for fcc Cu: cohesive energy, lattice constant, elastic constants C11, C12, C44, and bulk modulus. Save the fitted parameter set as cu_potential.json.
- Evidence: `/app/outputs/cu_potential.json`

### Step 2: Fit pure Nb potential
- Role: process
- Action: Determine the parameters of the modified TB-SMA potential for Nb-Nb interactions (using cutoff-polynomial repulsive term and cutoff-modulated exponential many-body term) by fitting to the provided experimental reference properties for bcc Nb: cohesive energy, lattice constant, elastic constants C11, C12, C44, and bulk modulus. Save the fitted parameter set as nb_potential.json.
- Evidence: `/app/outputs/nb_potential.json`

### Step 3: Fit Cu-Nb cross potential
- Role: process
- Action: Determine the cross-interaction parameters for Cu-Nb pairs (using the same functional forms as Cu-Cu) by fitting to the provided ab initio reference properties for the three hypothetical compounds L1₂ Cu₃Nb, B2 CuNb, and L1₂ CuNb₃: lattice constants, cohesive energies, elastic constants, and bulk moduli. Save the fitted cross parameter set as cross_potential.json.
- Evidence: `/app/outputs/cross_potential.json`

### Step 4: Validate pure-element ground states
- Role: process
- Action: Using the fitted pure potentials, compute the cohesive energies of fcc, hcp, and bcc polymorphs for Cu and for Nb. Verify that fcc Cu has the lowest energy among its polymorphs and bcc Nb has the lowest among its polymorphs. Write the computed energies to polymorph_energies.json.
- Evidence: `/app/outputs/polymorph_energies.json`

### Step 5: Run MD simulations and analyze g(r)
- Role: process
- Action: Build fcc Cu-based solid solution models (8x8x8 unit cells, 2048 atoms) with Nb concentrations from 0 to 50 at.% Nb, and bcc Nb-based solid solution models (10x10x10 unit cells, 2000 atoms) with Cu concentrations from 0 to 50 at.% Cu. Run MD at 300 K and 0 Pa for 50,000 time steps (dt=5 fs) using the full Cu-Nb potential. For each final configuration, calculate the pair-correlation function g(r) and apply Zallen's criterion (no discernible peaks beyond third-nearest neighbor) to classify each composition as crystalline or amorphous. Save the per-composition analysis (composition at.% Nb, list of g(r) peak distances, and amorphous flag) to md_g_of_r_analysis.json.
- Evidence: `/app/outputs/md_g_of_r_analysis.json`

### Step 6: Determine amorphous formation range
- Role: scored (load-bearing)
- Action: From the g(r) analysis data, identify the composition bounds of the amorphous region. For Cu-rich solid solutions, find the lowest Nb concentration where the structure becomes amorphous (lower bound). For Nb-rich solutions, find the highest Nb concentration where the structure is still amorphous (upper bound). Ensure monotonicity: once amorphous at a given composition, all compositions inside the interval should also be amorphous. Combine the two ends to report the overall composition range in at.% Nb. Output the bounds and the full list of compositions with their amorphous flags.
- Output file: `/app/outputs/amorphization_range.json`
- Format: json
- Contract: {"lower_bound_at_percent_Nb": <float>, "upper_bound_at_percent_Nb": <float>, "critical_compositions": [{"composition_at_percent_Nb": <float>, "amorphous": <bool>}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/amorphization_range.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### amorphization_range.json
- path: `/app/outputs/amorphization_range.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lower and upper bounds of the composition range (at.% Nb) where amorphous phase forms, and the per-composition crystalline/amorphous flags determined from g(r) analysis.
- schema:
  - `type`: object
  - `required`:
    - `lower_bound_at_percent_Nb`: float (at.% Nb)
    - `upper_bound_at_percent_Nb`: float (at.% Nb)
    - `critical_compositions`: array
  - `items`:
    - `composition_at_percent_Nb`: float
    - `amorphous`: boolean
  - `required_columns`: None
  - `units`: None

Notes: The bounds are compared to the paper's reported values (15 and 72 at.% Nb) with a tolerance of ±5 at% absolute. Internal consistency with md_g_of_r_analysis.json is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "amorphization_range.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lower_bound_at_percent_Nb": "float (at.% Nb)",
          "upper_bound_at_percent_Nb": "float (at.% Nb)",
          "critical_compositions": "array"
        },
        "items": {
          "composition_at_percent_Nb": "float",
          "amorphous": "boolean"
        },
        "required_columns": null,
        "units": null
      },
      "description": "Lower and upper bounds of the composition range (at.% Nb) where amorphous phase forms, and the per-composition crystalline/amorphous flags determined from g(r) analysis."
    }
  ],
  "notes": "The bounds are compared to the paper's reported values (15 and 72 at.% Nb) with a tolerance of ±5 at% absolute. Internal consistency with md_g_of_r_analysis.json is also verified."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. For each workflow stage, the verifier inspects the corresponding output artifacts for structural correctness (e.g., valid JSON format, monotonicity of amorphous flags with composition). For the final scored artifact, the verifier compares your derived composition bounds to a hidden reference. The overall reward is a weighted combination of the per‑stage scores. Reporting the paper’s numbers without proper execution of the described methodology will not earn credit. You should faithfully implement the described potential fitting, MD protocol, and g(r) analysis; exact tolerances are hidden, but the verifier expects physically consistent results.
