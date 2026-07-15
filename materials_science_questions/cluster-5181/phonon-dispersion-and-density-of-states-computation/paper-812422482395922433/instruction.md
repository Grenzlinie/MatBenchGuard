# Electron-phonon coupling and Tc in MgB2 and NbB2

## Problem background
The discovery of superconductivity at 39 K in MgB₂ renewed interest in the diboride family. Among them, NbB₂ is a closely related compound that also displays superconductivity, but with widely varying reported transition temperatures. Understanding the differences in the electron–phonon interaction that underlies superconductivity in these two materials is important for clarifying the mechanisms at play. This work computes the key electron–phonon coupling parameters for both MgB₂ and NbB₂ using first‑principles methods, and asks: what are the average electron‑phonon coupling constants λ, and what are the corresponding superconducting critical temperatures Tc (evaluated at a Coulomb pseudopotential μ*=0.1), for these two diborides?

## Approach
The approach uses density‑functional theory (DFT) and density‑functional perturbation theory (linear response) to obtain the electron‑phonon properties from first principles. For each material, the hexagonal P6/mmm crystal structure is relaxed to determine equilibrium lattice constants. A self‑consistent field calculation is then performed, followed by a linear‑response computation of dynamical matrices on a grid of q‑points. From these, the phonon density of states, the Eliashberg function α²F(ω), and the average electron‑phonon coupling constant λ are derived. Finally, the isotropic Eliashberg gap equation is solved numerically for a range of Coulomb pseudopotential μ* values (0.1–0.2) to obtain the Tc(μ*) curves. The two materials are processed identically, and their resulting λ and Tc values are directly compared.

## Reproduction target
Compute the average electron–phonon coupling constant λ for both MgB₂ and NbB₂, and the superconducting critical temperature Tc at a Coulomb pseudopotential μ*=0.1. Produce a CSV file `tc_vs_mustar.csv` containing Tc as a function of μ* (from 0.1 to 0.2) for both materials, and a JSON file `results.json` that records the λ and Tc(μ*=0.1) values for each material. All outputs must be derived from the first‑principles workflow described in the steps below, using an open‑source DFT code (e.g., Quantum ESPRESSO).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Optimize the lattice constants a and c for MgB2 and NbB2 in the P6/mmm crystal structure using a DFT plane-wave pseudopotential code (e.g., Quantum ESPRESSO). Choose appropriate pseudopotentials and convergence parameters to obtain relaxed structures.
- Evidence: `/app/outputs/relaxation.json`

### Step 2: Phonon and electron-phonon coupling calculation
- Role: process
- Action: Using the relaxed structures, perform a self-consistent field calculation followed by a density-functional perturbation theory (linear response) calculation to obtain dynamical matrices on a grid of q-points. From these, compute the phonon density of states, the Eliashberg function α²F(ω), and the average electron–phonon coupling constant λ for both MgB2 and NbB2. Save the α²F(ω) data and λ values to a structured file.
- Evidence: `/app/outputs/phonon_results.json`

### Step 3: Compute Tc vs μ* curves
- Role: scored (load-bearing)
- Action: Read the computed α²F(ω) for each material from the previous step. Solve the isotropic Eliashberg gap equation numerically for Coulomb pseudopotential values μ* in the range 0.1–0.2 (e.g., step size 0.01). For each material and each μ*, output the superconducting critical temperature Tc (in K). Write the full Tc vs μ* dataset to tc_vs_mustar.csv.
- Output file: `/app/outputs/tc_vs_mustar.csv`
- Format: csv
- Contract: material (str), mu_star (float), Tc (float, in K)
- Scoring: scored by hidden verifier

### Step 4: Compile final results
- Role: scored
- Action: Extract the average electron–phonon coupling constant λ for each material from the intermediate phonon results (step_phonon) and the Tc at μ*=0.1 from tc_vs_mustar.csv (step_tc_curves). Write a JSON file results.json containing the keys "MgB2" and "NbB2", each with sub‑keys "lambda" (float) and "Tc_mu0_1" (float).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"MgB2": {"lambda": number, "Tc_mu0_1": number}, "NbB2": {"lambda": number, "Tc_mu0_1": number}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_vs_mustar.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_vs_mustar.csv
- path: `/app/outputs/tc_vs_mustar.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Tc(μ*) curves showing decreasing trend with increasing μ* for each material, and cross-checking Tc at μ*=0.1 against results.json.
- schema:
  - `type`: table
  - `required_columns`: `material`, `mu_star`, `Tc`
  - `units`:
    - `Tc`: K

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline average electron-phonon coupling constant λ and superconducting transition temperature at μ*=0.1 for MgB2 and NbB2. Compared to paper-reported values with tolerances; ordering MgB2 λ > NbB2 λ and MgB2 Tc > NbB2 Tc is also checked.
- schema:
  - `type`: object
  - `required_keys`: `MgB2`, `NbB2`
  - `value_schema`:
    - `lambda`:
      - `type`: number
      - `unit`: dimensionless
    - `Tc_mu0_1`:
      - `type`: number
      - `unit`: K

Notes: The tolerances (hidden) absorb differences from using an open-source DFT code (Quantum ESPRESSO) instead of the original full-potential LMTO. The Tc vs μ* curves are also verified for monotonicity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_vs_mustar.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "mu_star",
          "Tc"
        ],
        "units": {
          "Tc": "K"
        }
      },
      "description": "Tc(μ*) curves showing decreasing trend with increasing μ* for each material, and cross-checking Tc at μ*=0.1 against results.json."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "MgB2",
          "NbB2"
        ],
        "value_schema": {
          "lambda": {
            "type": "number",
            "unit": "dimensionless"
          },
          "Tc_mu0_1": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Headline average electron-phonon coupling constant λ and superconducting transition temperature at μ*=0.1 for MgB2 and NbB2. Compared to paper-reported values with tolerances; ordering MgB2 λ > NbB2 λ and MgB2 Tc > NbB2 Tc is also checked."
    }
  ],
  "notes": "The tolerances (hidden) absorb differences from using an open-source DFT code (Quantum ESPRESSO) instead of the original full-potential LMTO. The Tc vs μ* curves are also verified for monotonicity."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently inspects the artifacts:

- `results.json`: the verifier compares your reported λ and Tc(μ*=0.1) values to reference values (with tolerances) and checks that the ordering MgB₂ λ > NbB₂ λ and MgB₂ Tc > NbB₂ Tc holds.
- `tc_vs_mustar.csv`: the verifier confirms that Tc decreases monotonically with increasing μ* for each material, and cross‑checks that the Tc(μ*=0.1) entry matches the corresponding value in `results.json` within tolerance.

The final reward is a weighted combination of these checks. Simply reporting numbers from the literature without executing the first‑principles calculations will not satisfy all criteria.
