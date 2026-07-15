# Molecular Dynamics Simulation of Graphene under Hydrostatic Compression: Bulk Modulus and Grüneisen Parameter

## Problem background
Graphene, a single layer of carbon atoms arranged in a honeycomb lattice, possesses exceptional in-plane stiffness and strength. Understanding its response to hydrostatic compression is crucial for strain engineering and for interpreting high-pressure Raman spectroscopy experiments. Atomistic simulations can directly probe the mechanical behavior by computing the force required to compress a free-standing graphene sheet, from which one can extract the 2D bulk modulus, the effective 3D bulk modulus, and the mode Grüneisen parameter. In this task, you will perform such simulations and compute these quantities from the resulting force–strain data.

## Approach
The mechanical response of graphene is modelled using an empirical interatomic potential that includes a two-body Morse-type bond stretching term and a three-body angle bending term with quadratic plus cubic contributions. This potential, described in the literature for graphene, will be implemented by you (using any molecular dynamics engine or custom code). You will construct a rectangular graphene lattice containing approximately 7482 atoms. Hydrostatic compression is simulated by applying forces of equal magnitude per unit length on the boundary atoms, perpendicular to the edges, and allowing the lattice to relax to an equilibrium area. For each applied force, you will record the resulting relative surface change ΔS_R = (S – S₀)/S₀, where S₀ is the initial surface area and S is the relaxed surface area. You will sample a range of compressive (and optionally tensile) forces to capture both the linear small-strain regime and the asymmetric response at larger strains.

From this force–strain curve, the 2D bulk modulus B₂D is obtained as the slope of the linear region at small strains (force per unit length vs. ΔS_R). Using the interlayer spacing of graphite (0.335 nm) as the effective thickness of graphene, the effective 3D bulk modulus is B_eff = B₂D / 0.335 nm, expressed in GPa. Finally, the Grüneisen parameter γ_G of the E₂g mode (G band) is computed using the relation γ_G = (B_eff / ω_G) · (dω_G/dP), where ω_G is the mode frequency at ambient pressure and dω_G/dP is its pressure derivative for unsupported graphene. You are given ω_G = 1588 cm⁻¹ and dω_G/dP = 5.6 cm⁻¹/GPa. The derived quantities will be stored in a summary JSON file.

## Reproduction target
Your goal is to produce two output files:

1. `/app/outputs/force_surface_curve.csv` – a CSV table with columns `force` (float, in N/m) and `delta_SR` (float, dimensionless). The data must span a range that includes the linear small-strain regime (negative ΔS_R values) and, optionally, a larger compressive range to show asymmetry. The curve should be smooth and physically plausible.

2. `/app/outputs/md_results_summary.json` – a JSON object with the following keys:
   - `B_2D`: the 2D bulk modulus (float, units of N/m),
   - `B_eff`: the effective 3D bulk modulus (float, units of GPa),
   - `gamma_G`: the Grüneisen parameter (float, dimensionless).

These values must be derived from the linear region of the force–strain curve and the supplied physical constants (interlayer spacing 0.335 nm, ω_G = 1588 cm⁻¹, dω_G/dP = 5.6 cm⁻¹/GPa).

## Assets

- Graphene interatomic potential parameters and functional forms from Kalosakas et al. (2013): 10.1063/1.4795528
- Molecular dynamics simulation engine (e.g., LAMMPS, ASE, or custom implementation): https://www.lammps.org/

## Workflow steps

### Step 1: MD simulation of graphene under hydrostatic compression
- Role: scored
- Action: Implement the interatomic potential for graphene (bond stretching Morse-type and angle bending with quadratic+cubic terms) from Kalosakas et al. (2013). Set up a rectangular graphene lattice containing approximately 7482 atoms. Simulate hydrostatic compression by applying same-magnitude forces per unit length on boundary atoms, record the relative surface change ΔS_R at equilibrium, and produce a CSV of force per unit length versus ΔS_R for a range covering both linear small-strain regime and larger asymmetric response.
- Output file: `/app/outputs/force_surface_curve.csv`
- Format: csv
- Contract: CSV with columns: force (float, N/m), delta_SR (float, unitless).
- Scoring: scored by hidden verifier

### Step 2: Extract bulk moduli and Grüneisen parameter from force–strain curve
- Role: scored (load-bearing)
- Action: Read force_surface_curve.csv, identify the linear regime at small strains, and compute the 2D bulk modulus B_2D as the slope (N/m). Then calculate the effective 3D bulk modulus B_eff = B_2D / 0.335e-9 m, converted to GPa. Compute the Grüneisen parameter γ_G using γ_G = B_eff / ω_G · (dω_G/dP) with ω_G = 1588 cm⁻¹ and dω_G/dP = 5.6 cm⁻¹/GPa for unsupported graphene. Save the three values to a JSON file.
- Output file: `/app/outputs/md_results_summary.json`
- Format: json
- Contract: JSON object with keys: B_2D (float, N/m), B_eff (float, GPa), gamma_G (float, unitless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_surface_curve.csv`
- `/app/outputs/md_results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_surface_curve.csv
- path: `/app/outputs/force_surface_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw force per unit length vs relative surface change data; the checker will fit the linear small-strain region to recompute the 2D bulk modulus.
- schema:
  - `type`: table
  - `required_columns`: `force`, `delta_SR`
  - `units`:
    - `force`: N/m
    - `delta_SR`: unitless

### md_results_summary.json
- path: `/app/outputs/md_results_summary.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reported 2D bulk modulus, effective 3D bulk modulus, and Grüneisen parameter derived from the simulation.
- schema:
  - `type`: object
  - `required`:
    - `B_2D`: float (N/m)
    - `B_eff`: float (GPa)
    - `gamma_G`: float (unitless)

Notes: The checker will internally recompute B_2D from the force_surface_curve.csv linear fit and verify it against the paper's reported value, and will also read md_results_summary.json to compare all three quantities to reference values with hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_surface_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "force",
          "delta_SR"
        ],
        "units": {
          "force": "N/m",
          "delta_SR": "unitless"
        }
      },
      "description": "Raw force per unit length vs relative surface change data; the checker will fit the linear small-strain region to recompute the 2D bulk modulus."
    },
    {
      "file": "md_results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "B_2D": "float (N/m)",
          "B_eff": "float (GPa)",
          "gamma_G": "float (unitless)"
        }
      },
      "description": "Reported 2D bulk modulus, effective 3D bulk modulus, and Grüneisen parameter derived from the simulation."
    }
  ],
  "notes": "The checker will internally recompute B_2D from the force_surface_curve.csv linear fit and verify it against the paper's reported value, and will also read md_results_summary.json to compare all three quantities to reference values with hidden tolerances."
}
```

## How you are scored
A hidden verifier will score your outputs automatically. The verifier will:

- Read your `force_surface_curve.csv` and perform a linear least-squares fit on the small-strain region to recompute the 2D bulk modulus. This recomputed value is compared to a hidden reference to assess the quality of your simulation curve.
- Read your `md_results_summary.json` and compare each of the three reported quantities (`B_2D`, `B_eff`, `gamma_G`) against hidden target values, with appropriate hidden tolerances.

The total reward is a weighted combination of the scores from these two stages. The force–strain curve stage contributes score, and the summary JSON stage (which carries the main load-bearing quantities) contributes the remaining weight. To obtain a high score, you must faithfully implement the potential and run the simulation; simply guessing or hard-coding values will not pass the verifier's checks. The verifier does not inspect your code, only the final artifacts.
