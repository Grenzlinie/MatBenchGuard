# Cohesive law for parallel graphene sheets from Lennard-Jones potential

## Problem background
Carbon nanotubes (CNTs) possess outstanding mechanical properties and often appear as multi-wall structures where adjacent walls interact via van der Waals forces. Accurately modelling these wall-to-wall interactions is essential for continuum simulations of CNT assemblies. The goal of this task is to derive from first principles a cohesive law – i.e., explicit expressions for the cohesive energy, tensile cohesive stress, and shear cohesive stress – by starting from the Lennard-Jones potential that describes van der Waals forces between carbon atoms. The task considers graphene-based approximations: infinitely extended parallel graphene sheets for tensile behaviour, and finite overlapping graphene sheets that capture edge effects in shear. All needed physical constants (Lennard‑Jones parameters and the carbon–carbon equilibrium bond length) are provided.

## Approach
The approach homogenises carbon atoms on each graphene layer into a continuous area density derived from the graphene lattice (using the given equilibrium bond length). For two infinite parallel sheets, the integration of the Lennard‑Jones potential over the whole plane yields analytical forms for the cohesive energy per unit area and the tensile cohesive stress as functions of the opening displacement. Minimising the energy gives the equilibrium inter‑wall separation. For two sheets that overlap over a finite length, the same homogenisation is applied, but the integration now accounts for the free edges. This produces a line energy (energy per unit length along the edge) that depends on both opening and sliding displacements, from which average tensile and shear cohesive stresses are derived. The computation uses the fixed Lennard‑Jones parameters (ε = 0.00239 eV, σ = 0.3415 nm) and the equilibrium bond length l₀ = 0.142 nm. The implementation must perform the required analytical integrations and evaluate the resulting formulas to obtain the requested numerical values and curves.

## Reproduction target
1. From the given Lennard‑Jones parameters and bond length, compute the carbon area density and then the total cohesive energy Φ_total (J/m²), the tensile cohesive strength σ_max (GPa), and the critical separation δ₀ (nm) for infinite parallel graphene. Store these together with the input ε and σ in cohesive_parameters.json.
2. For the same infinite-graphene system, compute the tensile cohesive stress σ_cohesive (GPa) at opening displacements v from 0.00 to 0.50 nm in steps of 0.01 nm. For a finite overlap with current overlap length L–u = 10 nm and sliding displacement u = 0 nm, compute the average shear cohesive stress τ_cohesive (GPa) at the same v values. Write the three columns (v_nm, sigma_cohesive_GPa, tau_cohesive_GPa) to stress_displacement_data.csv.
3. Derive and document the key analytical expressions: the cohesive energy per unit area and tensile cohesive stress for the infinite case, and the line energy and average shear cohesive stress for the finite‑overlap case. Use the notation from the cohesive‑law literature (e.g., Φ, σ_cohesive, τ_cohesive) and save the expressions as plain text in cohesive_law_expressions.txt.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy

## Workflow steps

### Step 1: Compute cohesive parameters
- Role: scored
- Action: Compute the area density of carbon atoms on graphene, the total cohesive energy Phi_total, the tensile cohesive strength sigma_max, and the critical separation delta_0 from the Lennard-Jones potential for infinite graphene sheets. Use the given LJ parameters (epsilon=0.00239 eV, sigma=0.3415 nm) and equilibrium bond length (l0=0.142 nm). Write the computed values to the output file.
- Output file: `/app/outputs/cohesive_parameters.json`
- Format: json
- Contract: JSON object with keys: Phi_total (float, J/m^2), sigma_max (float, GPa), delta_0 (float, nm), epsilon (float, eV), sigma (float, nm).
- Scoring: scored by hidden verifier

### Step 2: Compute stress-displacement data
- Role: scored (load-bearing)
- Action: Compute the tensile cohesive stress sigma_cohesive as a function of opening displacement v for infinite graphene, and the average shear cohesive stress tau_cohesive for a finite overlap of L-u=10 nm and sliding displacement u=0. Evaluate at v from 0 to 0.5 nm in steps of 0.01 nm. Write the results to the output CSV file.
- Output file: `/app/outputs/stress_displacement_data.csv`
- Format: csv
- Contract: CSV with columns: v_nm (float), sigma_cohesive_GPa (float), tau_cohesive_GPa (float).
- Scoring: scored by hidden verifier

### Step 3: Write cohesive law expressions
- Role: scored
- Action: Formulate and write the derived analytical expressions for the cohesive energy per unit area and tensile cohesive stress for infinite graphene, and for the line energy and average shear cohesive stress for finite overlap, using the notation from the paper. Save these expressions in plain text.
- Output file: `/app/outputs/cohesive_law_expressions.txt`
- Format: txt
- Contract: Plain text file with the derived mathematical expressions (e.g., Phi = ..., sigma_cohesive = ..., tau_cohesive = ...).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cohesive_parameters.json`
- `/app/outputs/stress_displacement_data.csv`
- `/app/outputs/cohesive_law_expressions.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cohesive_parameters.json
- path: `/app/outputs/cohesive_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived cohesive parameters from the infinite graphene Lennard‑Jones cohesive law.
- schema:
  - `type`: object
  - `required`:
    - `Phi_total`: number (J/m^2)
    - `sigma_max`: number (GPa)
    - `delta_0`: number (nm)
    - `epsilon`: number (eV)
    - `sigma`: number (nm)

### stress_displacement_data.csv
- path: `/app/outputs/stress_displacement_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Tensile and shear cohesive stresses vs. opening displacement for infinite graphene and a finite overlap of 10 nm.
- schema:
  - `type`: table
  - `required_columns`: `v_nm`, `sigma_cohesive_GPa`, `tau_cohesive_GPa`
  - `units`:
    - `v_nm`: nm
    - `sigma_cohesive_GPa`: GPa
    - `tau_cohesive_GPa`: GPa

### cohesive_law_expressions.txt
- path: `/app/outputs/cohesive_law_expressions.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Plain-text rendering of the derived analytical cohesive law expressions.
- schema:
  - `type`: text

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cohesive_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Phi_total": "number (J/m^2)",
          "sigma_max": "number (GPa)",
          "delta_0": "number (nm)",
          "epsilon": "number (eV)",
          "sigma": "number (nm)"
        }
      },
      "description": "Derived cohesive parameters from the infinite graphene Lennard‑Jones cohesive law."
    },
    {
      "file": "stress_displacement_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "v_nm",
          "sigma_cohesive_GPa",
          "tau_cohesive_GPa"
        ],
        "units": {
          "v_nm": "nm",
          "sigma_cohesive_GPa": "GPa",
          "tau_cohesive_GPa": "GPa"
        }
      },
      "description": "Tensile and shear cohesive stresses vs. opening displacement for infinite graphene and a finite overlap of 10 nm."
    },
    {
      "file": "cohesive_law_expressions.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Plain-text rendering of the derived analytical cohesive law expressions."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each of the three artefacts. For cohesive_parameters.json, the verifier recomputes Φ_total, σ_max, and δ₀ from the given input constants and compares them against the submitted values within a tolerance. For stress_displacement_data.csv, the verifier recomputes σ_cohesive and τ_cohesive from the analytical formulas at every v point and compares row‑by‑row, also verifying that τ_cohesive decreases monotonically with v. For cohesive_law_expressions.txt, the verifier performs a structural audit to confirm that the text contains the correct functional forms. The three checks are combined with weights (≈40 % for the parameter file, ≈60 % for the stress-displacement table, and a small share for the expression file) to produce a single reward between 0 and 1. Simply copying numbers from a memory source will not suffice because the verifier recomputes the stress curves from the public analytical forms, and the hidden reference values are not disclosed in these instructions.
