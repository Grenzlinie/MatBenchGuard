# Magnetoelastic coupling and equilibrium oxygen displacement in UO2 via crystal-field theory

## Problem background
Uranium dioxide (UO₂) undergoes a first-order antiferromagnetic transition that coincides with a structural distortion of the oxygen sublattice known as the transverse internal rearrangement (TIR). In the TIR, the oxygen planes shear relative to one another while the uranium sublattice remains fcc. The physical question is what microscopic mechanism selects the TIR over competing distortions, such as a homogeneous internal strain (the Allen mode). The leading hypothesis is a competition between two energy contributions: a crystal-field energy that is lowered by the distortion and an elastic energy that increases with the distortion. Understanding which mode wins at low temperature requires a quantitative energy comparison using a microscopic model that includes crystal-field, magnetic exchange, and lattice elasticity.

## Approach
The magnetoelastic coupling is modelled by a single-site Hamiltonian for the U⁴⁺ ion in the cubic Γ₅ crystal-field ground-state manifold. The Hamiltonian includes three terms: (1) a cubic crystal-field operator that provides a Γ₅ triplet, (2) a molecular-field exchange term that drives antiferromagnetic ordering along ⟨110⟩, and (3) a distortion-dependent crystal-field operator whose strength is proportional to the relative oxygen displacement δ. The effective coupling between the distortion and the electronic degrees of freedom is characterised by a charge-like parameter that is derived from experimental constraints on the Néel temperature and the magnetisation discontinuity.

Elastic energies for the TIR and Allen modes are computed microscopically within a rigid-ion model. The model uses a given set of short-range repulsive parameters and an ionic charge, combined with the lattice constant a = 5.468 Å. The elastic constant κ for each mode is obtained from a combination of Coulomb (Ewald) sums and repulsive contributions; the resulting κδ² term adds a harmonic penalty that competes with the crystal-field energy lowering.

At zero temperature, the ground state is found by self-consistently diagonalising the Hamiltonian to obtain the thermal averages of the dipole ⟨J_z⟩ and the quadrupole ⟨O₂⁰−O₂²⟩. The equilibrium distortion δ is the value that minimises the total energy (crystal‑field + exchange + elastic). The TIR and Allen modes are then compared by evaluating their total energies over a range of δ values, using the same exchange and elastic parameters, to determine which mode yields the lower ground-state energy.

## Reproduction target
Reproduce the following two results:

1. The zero-temperature equilibrium relative oxygen shift δ (dimensionless) for the TIR mode, computed with the rigid-ion parameter set labelled "soft set, column 5 of Table II" (Z_C = 2.142, A₁ = 21.0, B₁ = 3.9, A₂ = 8.8, B₂ = −1.1, A₃ = 13.5, B₃ = −3.8) and the constraints Q/λ = 0.033, λ = 7.04 K. Convert δ to a physical oxygen displacement in Å using a = 5.468 Å and write the results to `equilibrium_delta.json`.

2. A comparison of the total ground-state energies (in K) of the TIR and Allen modes for a range of δ values, using the same parameters and the effective charge ρ derived from the TIR elastic constant. Write the table to `mode_energy_comparison.csv`. The comparison should span a sufficiently wide range of δ to capture the minima of both modes and must include a row at (or very near) the equilibrium δ obtained in part 1.

## Assets

- numpy: numpy
- scipy: scipy
- Standard crystal-field data for U4+ (Stevens factors, radial integrals)
- Rigid-ion model parameters for UO₂ (soft set, column 5 of Table II)
- UO₂ lattice constant (a = 5.468 Å)

## Workflow steps

### Step 1: Compute crystal-field coefficients and elastic constants for TIR and Allen modes
- Role: process
- Action: Using the given rigid-ion parameters (column 5 of Table II) and lattice constant a=5.468 Å, compute the effective elastic constants κ for the TIR and Allen modes via Ewald summation and the rigid-ion model. Compute crystal-field distortion coefficients C_TIR and C_Allen from the point-charge model and Stevens operators using the radial integrals and Stevens factors for U⁴⁺. Derive the effective charge ρ from the constraints Q/λ=0.033, λ=7.04 K, and κ_TIR. The derived parameters (κ, C, ρ) are used in subsequent steps; no scored output here.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 2: Compute zero-temperature equilibrium TIR distortion
- Role: scored (load-bearing)
- Action: Construct the Γ₅ Hamiltonian for the TIR mode with quantization axis along ⟨110⟩, including the cubic crystal-field term, the magnetic exchange term with λ=7.04 K, and the quadrupolar term with Q=0.23232 K. At T=0, self-consistently solve for ⟨J_z⟩ and ⟨O₂⁰−O₂²⟩ by diagonalizing the Hamiltonian and iterating until convergence. Compute the equilibrium relative oxygen shift δ from δ = sqrt(Q/(2κ_TIR)) * |⟨O₂⁰−O₂²⟩|. Convert δ to physical oxygen displacement in Å using the lattice constant a=5.468 Å. Write the results to equilibrium_delta.json.
- Output file: `/app/outputs/equilibrium_delta.json`
- Format: json
- Contract: JSON with keys: 'delta' (float, unitless), 'oxygen_displacement_A' (float, Å), 'parameter_set' (string, e.g., 'soft set column 5 Table II'), 'mode' (string, 'TIR').
- Scoring: scored by hidden verifier

### Step 3: Compare ground-state energies of TIR and Allen modes
- Role: scored
- Action: For a range of δ values (e.g., 0 to 0.006), compute the total ground-state energy at T=0 for both TIR and Allen modes. Total energy = (crystal-field + exchange) ground-state eigenvalue + elastic energy κδ², using the same λ=7.04 K and effective charge ρ derived in step_01. Self-consistently determine ⟨J_z⟩ at each δ. Write a CSV file with columns delta, energy_TIR, energy_Allen. Include rows spanning the range and in particular at the equilibrium δ of the TIR.
- Output file: `/app/outputs/mode_energy_comparison.csv`
- Format: csv
- Contract: CSV with header: delta, energy_TIR, energy_Allen. All values are floats. Must contain multiple rows including a row at the equilibrium δ of the TIR.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_delta.json`
- `/app/outputs/mode_energy_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_delta.json
- path: `/app/outputs/equilibrium_delta.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium TIR distortion; scored by comparing the reported dimensionless delta to the paper-reported value within a tolerance and checking the oxygen displacement conversion.
- schema:
  - `type`: object
  - `required`:
    - `delta`: float (unitless)
    - `oxygen_displacement_A`: float (Å)
    - `parameter_set`: string
    - `mode`: string

### mode_energy_comparison.csv
- path: `/app/outputs/mode_energy_comparison.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Ground-state energy comparison between TIR and Allen modes; scored by recomputing the equilibrium delta from the CSV data, comparing it to a reference value, and verifying that the energy ordering is correct across the scanned range.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `energy_TIR`, `energy_Allen`
  - `column_types`:
    - `delta`: float
    - `energy_TIR`: float
    - `energy_Allen`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_delta.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta": "float (unitless)",
          "oxygen_displacement_A": "float (Å)",
          "parameter_set": "string",
          "mode": "string"
        }
      },
      "description": "Equilibrium TIR distortion; scored by comparing the reported dimensionless delta to the paper-reported value within a tolerance and checking the oxygen displacement conversion."
    },
    {
      "file": "mode_energy_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "energy_TIR",
          "energy_Allen"
        ],
        "column_types": {
          "delta": "float",
          "energy_TIR": "float",
          "energy_Allen": "float"
        }
      },
      "description": "Ground-state energy comparison between TIR and Allen modes; scored by recomputing the equilibrium delta from the CSV data, comparing it to a reference value, and verifying that the energy ordering is correct across the scanned range."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently reads your output files and rewards each scored artifact. For `equilibrium_delta.json`, the verifier compares your reported δ and oxygen displacement to a hidden reference (with an appropriate tolerance) and checks that the mode name and parameter-set description are sensible. For `mode_energy_comparison.csv`, the verifier checks that the file contains the required columns, that it includes a row at the equilibrium δ from the first artifact, and that the energy ordering at that δ (and over the scanned range) satisfies the condition expected from the physics: the mode with the lower total energy at equilibrium should be the one that is energetically preferred. The final reward is a weighted combination of the two scores. Reporting a number alone is not sufficient — the reconstruction of the physical reasoning through self-consistent computation and elastic-constant derivation must be evidenced by the artifacts.
