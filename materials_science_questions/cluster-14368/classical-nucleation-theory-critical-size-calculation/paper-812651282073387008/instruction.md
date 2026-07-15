# Classical Nucleation Theory Critical Size Calculation

## Problem background
Classical nucleation theory (CNT) provides a framework for understanding phase transformations, describing the critical nucleus size and the energy barrier required for nucleation to proceed. In typical implementations, the monomer concentration is assumed constant, corresponding to an effectively infinite reservoir. However, during colloidal nanocrystal synthesis, growing particles consume monomers from a finite precursor pool, which gradually lowers the supersaturation and eventually arrests growth. This problem explores a modified free energy formulation that couples the growth of spherical nanocrystals to the remaining monomer concentration, enabling the prediction of an equilibrium nanoparticle radius that the system reaches under a given set of synthesis conditions. The model demonstrates how final particle size is determined by a balance between surface tension and the volume free energy gain from the remaining precursor, offering a quantitative route to size control at maximum yield.

## Approach
The central idea is to consider the free energy change accompanying the formation of a spherical nucleus of radius r, taking into account that the precursor monomer concentration in solution is not fixed but declines as nuclei grow. This leads to a modified free energy expression: a positive surface term (proportional to r²γ) and a negative volume term that depends on temperature, the instantaneous supersaturation, and the amount of monomer already consumed by existing nanoparticles. The equilibrium radius corresponds to the minimum of this free energy function for r > 0. For each set of synthesis parameters (initial monomer concentration, nanoparticle concentration, temperature, surface tension, and solubility limit), the equilibrium radius can be computed numerically by minimizing the free energy function. This approach reproduces the methodology of solving the modified CNT equation for the steady-state nanoparticle size.

## Reproduction target
Your task is to compute the equilibrium nanoparticle radius for each system entry in the provided input parameter file. The input file contains the necessary parameters: SystemID, nanoparticle concentration C_np (μM), initial precursor concentration C₀ (mM), solubility limit C_sol (nM), surface tension γ (J/m²), and temperature T (K). For every entry with all required parameters, implement the modified free energy expression and numerically find the radius r > 0 that minimizes it. Convert all concentrations to consistent SI units (mol/m³) and use standard physical constants (R = 8.314 J/(mol·K), Nₐ = 6.022×10²³ mol⁻¹, the molar volume of CdSe v = 2.27×10⁻⁵ m³/mol). Omit the entry that lacks a C_np value. Produce a CSV file at /app/outputs/simulated_radii.csv with two columns: SystemID (string) and R_sim_computed (float, nm). The rows must appear in the same order as the input file, skipping the excluded entry. Your computed radii will be compared to a hidden reference to assess the accuracy of your reproduction.

## Assets

- Input parameters for CNT simulation (Table S1)

## Workflow steps

### Step 1: Compute equilibrium radii
- Role: scored (load-bearing)
- Action: Read the provided input parameters (concentrations in µM, mM, nM; surface tension in J/m²; temperature in K). Convert all concentrations to mol/m³. Use physical constants R = 8.314 J/(mol·K), N_A = 6.022e23 mol⁻¹, and the molar volume of CdSe v = 2.27e-5 m³/mol. For each system entry, compute the equilibrium nanoparticle radius r_eq (in nm) that minimizes the modified free energy function: G(r) = 4πr²γ − (4πr³/3)(RT/v) ln( S₀ − (4πr³/3)(Nₐ C_np)/(v C_s) ), where S₀ = C₀ / C_s. Use a numerical minimizer for r > 0. Skip any row with missing C_np. Output a CSV file with columns: SystemID (string), R_sim_computed (float, nm). Ensure the row order matches the input order, omitting the OA5 at 508 K row.
- Output file: `/app/outputs/simulated_radii.csv`
- Format: csv
- Contract: Header: SystemID (string), R_sim_computed (float, nm). Rows in the same order as the provided input CSV, excluding the entry with missing C_np.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulated_radii.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulated_radii.csv
- path: `/app/outputs/simulated_radii.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Equilibrium nanocrystal radii computed via numerical minimization of the modified CNT free energy function, for all system IDs with available input parameters.
- schema:
  - `type`: table
  - `required_columns`: `SystemID`, `R_sim_computed`
  - `units`:
    - `R_sim_computed`: nm

Notes: The scored output is the computed radius. The verifier compares each value to the paper's hidden gold using tolerance: absolute difference ≤ max(0.05 nm, 0.05 × |gold|). A directionally correct reproduction (meeting or beating the tolerance) earns full credit per row.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulated_radii.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "SystemID",
          "R_sim_computed"
        ],
        "units": {
          "R_sim_computed": "nm"
        }
      },
      "description": "Equilibrium nanocrystal radii computed via numerical minimization of the modified CNT free energy function, for all system IDs with available input parameters."
    }
  ],
  "notes": "The scored output is the computed radius. The verifier compares each value to the paper's hidden gold using tolerance: absolute difference ≤ max(0.05 nm, 0.05 × |gold|). A directionally correct reproduction (meeting or beating the tolerance) earns full credit per row."
}
```

## How you are scored
A hidden automated verifier will read your simulated_radii.csv output and compare each computed radius (R_sim_computed) against a hidden reference value. For each row, the verifier determines whether your value meets an accuracy threshold; rows that meet or exceed the threshold receive full credit, while less accurate rows receive partial or no credit. The final reward is the fraction of rows that pass the accuracy check. The verifier also checks that the output file contains all expected entries in the correct order. To maximize your score, ensure your numerical minimization accurately solves the free energy equation and your unit conversions are correct.
