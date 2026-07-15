# OER overpotential increase with surface N-substitution in SrTaO2N

## Problem background
Perovskite oxynitride photocatalysts such as SrTaO2N lose surface nitrogen during operation, which correlates with a progressive drop in oxygen evolution reaction (OER) activity. The atomic-scale mechanism behind this loss of activity is not fully understood. In this task, we use density functional theory to investigate anion vacancies at the TaON-terminated (001) surface of SrTaO2N. The goal is to compute the thermodynamic OER overpotential as a function of the number of surface nitrogen ions replaced by oxygen, and to determine how the surface stress tensor changes accordingly, thus linking nitrogen loss to catalytic performance.

## Approach
The method is based on first-principles DFT calculations using the PBE functional with ultrasoft pseudopotentials. A slab model of the TaON-terminated SrTaO2N(001) surface is constructed with a 2×2 surface cell and vacuum. Defective surfaces with oxygen and nitrogen vacancies at specific sites are created to compute vacancy formation energies. The tendency of vacancies to be healed by OER intermediates is examined by placing an *O adsorbate near a surface nitrogen vacancy and relaxing the geometry. To evaluate the OER activity, the computational hydrogen electrode approach is used: the binding energies of *OH, *O, and *OOH adsorbates are computed on surfaces with different degrees of nitrogen substitution (x = 0,1,2,3,4). Gibbs free energies of the four proton-coupled electron transfer steps are obtained using zero-point energy and entropy corrections from prior work. The thermodynamic overpotential η is then derived as η = max(ΔG_i)/e − 1.23 V. Additionally, diagonal stress tensor components σ_xx and σ_yy are extracted from the relaxed slabs to assess the strain state. The workflow compares surfaces with different x and, for x=1, compares the two inequivalent Ta sites.

## Reproduction target
Compute the following quantities using the DFT setup described:
- Vacancy formation energies for V_O1, V_O3, V_N1, V_N3 on the SrTaO2N(001) surface (in eV).
- The geometry after placing an *O adsorbate near V_N1 and relaxing, demonstrating self-healing (the O atom occupying the vacancy site).
- The thermodynamic OER overpotential η (in V) for surfaces with x = 0,1,2,3,4 substituted surface N atoms. For x=1, compute η at the two inequivalent Ta sites (Ta2 and Ta3).
- The diagonal stress tensor components σ_xx and σ_yy (in GPa) for each x.

The primary objective is to determine how the overpotential and stress depend on x, and whether the overpotential for x=1 differs between the Ta2 and Ta3 sites. The output artifacts will be evaluated against expected structural and energetic relationships.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Ultrasoft pseudopotentials for Sr, Ta, O, N
- Zero-point energy and entropy corrections for OER adsorbates

## Workflow steps

### Step 1: Construct SrTaO2N slab models
- Role: process
- Action: Build the TaON-terminated (001) slab of SrTaO2N with lateral dimensions 8.182 Å × 8.182 Å (2×2 surface cell), 8 TaON/SrO layers, bottom two layers fixed, 15 Å vacuum, dipole correction. Set up models with oxygen vacancies V_O1, V_O3 and nitrogen vacancies V_N1, V_N3, as well as surfaces with x = 0,1,2,3,4 substituted surface N atoms.
- Evidence: none

### Step 2: Compute vacancy formation energies
- Role: scored
- Action: Calculate total energies of stoichiometric and defective slabs using Quantum ESPRESSO (PBE). Compute formation energies E_f(V_O1), E_f(V_O3), E_f(V_N1), E_f(V_N3) using the formation energy formula with mu_O = ½E(O₂) and mu_N = ½E(N₂) from separate DFT calculations. Store the results in JSON.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {"V_O1": float (eV), "V_O3": float (eV), "V_N1": float (eV), "V_N3": float (eV)}
- Scoring: scored by hidden verifier

### Step 3: Self-healing of V_N1 by *O adsorbate
- Role: scored
- Action: Place a single *O adsorbate on the surface near the V_N1 vacancy, relax the geometry to convergence, and verify that the oxygen atom occupies the vacancy site. Export the final atomic coordinates in XYZ format.
- Output file: `/app/outputs/self_healing_final.xyz`
- Format: txt
- Contract: XYZ file: first line number of atoms, second line comment, then element x y z (Å) per line.
- Scoring: scored by hidden verifier

### Step 4: OER overpotential vs surface N substitution
- Role: scored (load-bearing)
- Action: For surfaces with x = 0,1,2,3,4 substituted N atoms, compute DFT energies of the bare slab and with *OH, *O, *OOH adsorbates. Use free-energy corrections (ZPE, entropy) from prior work and the computational hydrogen electrode model to obtain Gibbs free energies of each PCET step. Compute thermodynamic overpotential η = max(ΔG_i)/e − 1.23 V. For x=1, compute separately on the inequivalent Ta2 and Ta3 sites. Report results in CSV.
- Output file: `/app/outputs/overpotentials.csv`
- Format: csv
- Contract: CSV columns: x (int), site (string), overpotential [V] (float). For x=0 one row site='Ta1'; x=1 rows for 'Ta2','Ta3'; x=2..4 one row per composition (site='average' or similar).
- Scoring: scored by hidden verifier

### Step 5: Stress tensor analysis
- Role: scored
- Action: Extract diagonal stress tensor components σ_xx and σ_yy from the DFT output of the relaxed slabs with x=0,1,2,3,4 substituted N atoms. Convert to GPa and write to CSV.
- Output file: `/app/outputs/stress_tensor.csv`
- Format: csv
- Contract: CSV columns: x (int), sigma_xx [GPa] (float), sigma_yy [GPa] (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/self_healing_final.xyz`
- `/app/outputs/overpotentials.csv`
- `/app/outputs/stress_tensor.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Vacancy formation energies. The checker verifies ordering (V_O1 < V_O3 and V_N1 < V_N3) and numeric values within hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `V_O1`: number (eV)
    - `V_O3`: number (eV)
    - `V_N1`: number (eV)
    - `V_N3`: number (eV)

### self_healing_final.xyz
- path: `/app/outputs/self_healing_final.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: XYZ file showing final positions after placing *O near V_N1. The checker will measure the distance from the placed O to the original N vacancy site; it must be < 2.0 Å.
- schema:
  - `type`: text
  - `required`: object

### overpotentials.csv
- path: `/app/outputs/overpotentials.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: OER overpotential as a function of x and site. The checker verifies monotonic increase with x and, for x=1, that Ta2 overpotential > Ta3 overpotential by a required margin.
- schema:
  - `type`: table
  - `required_columns`: `x`, `site`, `overpotential [V]`
  - `units`:
    - `overpotential [V]`: V

### stress_tensor.csv
- path: `/app/outputs/stress_tensor.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Diagonal stress tensor components. The checker verifies that σ_xx and σ_yy become more negative (decrease) as x increases.
- schema:
  - `type`: table
  - `required_columns`: `x`, `sigma_xx [GPa]`, `sigma_yy [GPa]`
  - `units`:
    - `sigma_xx [GPa]`: GPa
    - `sigma_yy [GPa]`: GPa

Notes: The workflow reproduces the paper's main OER activity and stress analysis without the NEB migration barrier calculations, which are computationally heavy and not required for the headline quantitative trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "V_O1": "number (eV)",
          "V_O3": "number (eV)",
          "V_N1": "number (eV)",
          "V_N3": "number (eV)"
        }
      },
      "description": "Vacancy formation energies. The checker verifies ordering (V_O1 < V_O3 and V_N1 < V_N3) and numeric values within hidden tolerance."
    },
    {
      "file": "self_healing_final.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {}
      },
      "description": "XYZ file showing final positions after placing *O near V_N1. The checker will measure the distance from the placed O to the original N vacancy site; it must be < 2.0 Å."
    },
    {
      "file": "overpotentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "site",
          "overpotential [V]"
        ],
        "units": {
          "overpotential [V]": "V"
        }
      },
      "description": "OER overpotential as a function of x and site. The checker verifies monotonic increase with x and, for x=1, that Ta2 overpotential > Ta3 overpotential by a required margin."
    },
    {
      "file": "stress_tensor.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "sigma_xx [GPa]",
          "sigma_yy [GPa]"
        ],
        "units": {
          "sigma_xx [GPa]": "GPa",
          "sigma_yy [GPa]": "GPa"
        }
      },
      "description": "Diagonal stress tensor components. The checker verifies that σ_xx and σ_yy become more negative (decrease) as x increases."
    }
  ],
  "notes": "The workflow reproduces the paper's main OER activity and stress analysis without the NEB migration barrier calculations, which are computationally heavy and not required for the headline quantitative trends."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored output artifact. The vacancy formation energies will be checked for the correct ordering between surface and subsurface vacancies and numerical agreement with expected values within a tolerance. The self-healing XYZ geometry will be inspected to confirm the O atom is located at the original nitrogen vacancy position. The overpotential CSV will be verified for the expected trend with x and, for x=1, the required site-dependent difference. The stress tensor will be checked for the expected dependence on x. Each stage is assigned a weight, and the final reward is a weighted combination of the stage scores. Reporting a single number that matches a known value is not sufficient; the artifacts must be produced by the described workflow and contain the required structure.
