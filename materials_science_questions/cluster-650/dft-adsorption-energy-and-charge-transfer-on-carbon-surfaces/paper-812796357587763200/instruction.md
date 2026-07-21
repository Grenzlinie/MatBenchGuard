# DFT Adsorption Energies of Potassium on Pristine and N-Doped Graphene Models

## Problem background
Potassium-ion batteries (PIBs) have emerged as promising low-cost alternatives to lithium-ion batteries due to the abundance and low redox potential of potassium. However, the large ionic radius of K⁺ (1.38 Å) hinders intercalation into electrode materials, leading to poor capacity and cycling stability. Carbon-based anodes, especially nitrogen-doped carbon, have shown enhanced performance, but the underlying mechanism is not fully understood. Density functional theory (DFT) calculations can quantify the adsorption strength of a single K atom on carbon surfaces and reveal how different nitrogen doping configurations affect K-ion storage. This task focuses on computing the adsorption energies of a K atom on pristine graphene and on graphene doped with three common nitrogen types: pyrrolic (N5), pyridinic (N6), and graphitic (NQ). The goal is to determine which doping configurations exhibit stronger (more negative) adsorption energies, providing insight into why certain N-doping types are beneficial for PIB anodes.

## Approach
The computational approach uses first-principles plane-wave DFT with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) functional. Structural models of a graphene supercell are built for four cases: pristine graphene and graphene with a single substitutional nitrogen atom in the pyrrolic (N5), pyridinic (N6), or graphitic (NQ) configuration. A single K atom is placed on each surface. For each adsorption configuration, the geometry is fully relaxed and the total energy of the combined K+surface system is computed. Separately, the total energy of the clean surface (without K) and the energy of an isolated K atom (in a large cell with spin polarization if needed) are computed. The adsorption energy ΔE_a is then obtained as the difference: ΔE_a = E(K+surface) − E(surface) − E(K_isolated). Negative values indicate exothermic binding. The final step compares the computed adsorption energies across the four doping types to assess the relative K-ion affinity of each site.

## Reproduction target
Perform DFT calculations as described and produce a CSV file (`/app/outputs/adsorption_energies.csv`) containing the computed adsorption energies (in eV) for the four doping types: pristine, N5, N6, NQ. The energies should be self-consistent and reflect a converged geometry optimization. The hidden verifier will check both the absolute values and the relative ordering among the doping types.

## Assets

- Plane-wave DFT code (Quantum ESPRESSO or VASP): https://www.quantum-espresso.org/
- Standard PBE pseudopotential library (SSSP Efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization and total energy calculations
- Role: process
- Action: Perform DFT geometry optimization and total energy calculations for a single K atom adsorbed on pristine graphene and on three N-doped graphene models: pyrrolic (N5), pyridinic (N6), and graphitic (NQ). Use a plane-wave DFT code with the PBE-GGA functional. For each configuration, optimize atomic positions and compute the total energy of the combined K+surface system. Separately compute the total energy of the corresponding pristine/doped slab without K and of an isolated K atom. Use a graphene supercell with vacuum and appropriate k-point sampling.
- Evidence: none

### Step 2: Compute and report adsorption energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in the DFT calculations, compute the adsorption energy ΔE_a for each model as: ΔE_a = E(K+surface) - E(surface) - E(K_isolated). Write the results to a CSV file.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: CSV with header: doping_type, adsorption_energy_eV. Four rows with doping_type values pristine, N5, N6, NQ. adsorption_energy_eV is a float in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed adsorption energies of a single K atom on pristine graphene and on N5, N6, NQ doped graphene.
- schema:
  - `type`: table
  - `required_columns`: `doping_type`, `adsorption_energy_eV`
  - `units`:
    - `adsorption_energy_eV`: eV

Notes: The hidden checker will compare the reported adsorption energies to the paper's DFT values with appropriate tolerance and also verify the relative trend (N6 more negative than N5, both more negative than pristine and NQ).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_type",
          "adsorption_energy_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "Computed adsorption energies of a single K atom on pristine graphene and on N5, N6, NQ doped graphene."
    }
  ],
  "notes": "The hidden checker will compare the reported adsorption energies to the paper's DFT values with appropriate tolerance and also verify the relative trend (N6 more negative than N5, both more negative than pristine and NQ)."
}
```

## How you are scored
Each workflow stage is evaluated by a hidden verifier. For this task, the scored artifact is the CSV file. The verifier will compare your reported adsorption energies to a hidden reference derived from the literature. In addition, it will verify that the relative trend of adsorption strengths across the four doping types is physically correct (i.e., a certain ordering must hold). The final reward is a weighted combination of these checks. Simply reporting values copied from a known source is insufficient; you must execute the DFT computations and produce consistent results from your own calculations.
