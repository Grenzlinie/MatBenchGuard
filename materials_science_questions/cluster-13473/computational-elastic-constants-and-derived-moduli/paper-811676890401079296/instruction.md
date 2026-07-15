# Hexatic-like Phase Window in 2D Lennard-Jones Binary Arrays

## Problem background
The transition from a crystal to a glass in two-dimensional systems can proceed through a sequence of distinct structural regimes. In binary arrays of atoms with different sizes, the competition between translational and orientational order as solute concentration increases may give rise to an intermediate phase that retains orientational symmetry while losing positional regularity. This task investigates whether such a hexatic-like regime exists in a model system of Lennard-Jones particles with atomic size mismatch, and if so, over what composition window it appears.

## Approach
The reproduction follows a two‑part approach: first, molecular dynamics simulations of a two‑dimensional binary Lennard‑Jones system under constant temperature and pressure are performed at several solute concentrations. The initial configurations are random placements on a hexagonal lattice, and the system is evolved until equilibrium. Second, for each equilibrated configuration, two order correlation functions are computed: the translational order correlation (measuring positional periodicity) and the bond‑orientational correlation (measuring angular order of nearest‑neighbor bonds). By comparing the decay of these correlation functions across compositions, one can identify concentration ranges where translational order becomes short‑ranged while orientational order persists quasi‑long‑ranged. This analysis directly yields the lower and upper bounds of the hexatic‑like window.

## Reproduction target
Run molecular dynamics simulations of a 2D binary Lennard‑Jones system with atomic size ratio α = 0.75, temperature T = 0.25 (reduced LJ units), pressure P = 0.0, and a total of 256 atoms on a hexagonal lattice. Set equal well depths for all pair interactions (ε<sub>AA</sub> = ε<sub>AB</sub> = ε<sub>BB</sub>). Perform simulations at four solute concentrations X<sub>B</sub>: 0.10, 0.148, 0.172, and 0.25. For each concentration, compute the translational order correlation function ρ<sub>G</sub>(r) and the bond‑orientational correlation function Ψ(r) and save them as CSV files. From the four sets of correlation curves, determine the compositional window in which ρ<sub>G</sub>(r) decays to near zero over the sample while Ψ(r) remains significantly above zero at large distances. Output this window as a JSON file with lower and upper bounds.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Setup system and run MD simulations
- Role: process
- Action: Set up a 2D hexagonal lattice of 256 atoms with Lennard-Jones potential (σ_A=1, atomic size ratio α=0.75, ε_AA=ε_AB=ε_BB) at temperature T=0.25 (reduced units) and pressure P=0.0. For each solute concentration X_B in {0.10, 0.148, 0.172, 0.25}, generate random initial configurations and perform constant-T, constant-P molecular dynamics until equilibrium. Output the trajectories or final configurations needed for correlation analysis.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute correlation functions for X_B=0.10
- Role: scored
- Action: From the MD trajectory for X_B=0.10, compute the translational order correlation function ρ_G(r) and bond-orientational correlation function Ψ(r). Write the results as a CSV file with columns: r, rho_G, Psi.
- Output file: `/app/outputs/correlation_functions_XB_0.100.csv`
- Format: csv
- Contract: CSV with three numeric columns: r (reduced distance), rho_G (translational correlation, dimensionless), Psi (orientational correlation, dimensionless). No header.
- Scoring: scored by hidden verifier

### Step 3: Compute correlation functions for X_B=0.148
- Role: scored
- Action: From the MD trajectory for X_B=0.148, compute the translational order correlation function ρ_G(r) and bond-orientational correlation function Ψ(r). Write the results as a CSV file with columns: r, rho_G, Psi.
- Output file: `/app/outputs/correlation_functions_XB_0.148.csv`
- Format: csv
- Contract: CSV with three numeric columns: r (reduced distance), rho_G (translational correlation, dimensionless), Psi (orientational correlation, dimensionless). No header.
- Scoring: scored by hidden verifier

### Step 4: Compute correlation functions for X_B=0.172
- Role: scored (load-bearing)
- Action: From the MD trajectory for X_B=0.172, compute the translational order correlation function ρ_G(r) and bond-orientational correlation function Ψ(r). Write the results as a CSV file with columns: r, rho_G, Psi.
- Output file: `/app/outputs/correlation_functions_XB_0.172.csv`
- Format: csv
- Contract: CSV with three numeric columns: r (reduced distance), rho_G (translational correlation, dimensionless), Psi (orientational correlation, dimensionless). No header.
- Scoring: scored by hidden verifier

### Step 5: Compute correlation functions for X_B=0.25
- Role: scored
- Action: From the MD trajectory for X_B=0.25, compute the translational order correlation function ρ_G(r) and bond-orientational correlation function Ψ(r). Write the results as a CSV file with columns: r, rho_G, Psi.
- Output file: `/app/outputs/correlation_functions_XB_0.250.csv`
- Format: csv
- Contract: CSV with three numeric columns: r (reduced distance), rho_G (translational correlation, dimensionless), Psi (orientational correlation, dimensionless). No header.
- Scoring: scored by hidden verifier

### Step 6: Determine compositional window of hexatic-like phase
- Role: scored
- Action: From the computed correlation functions for all four compositions, identify the compositional range where translational order is short-ranged (ρ_G decays to near zero over the sample) while orientational order remains quasi-long-ranged. Output a JSON file with the lower and upper bounds.
- Output file: `/app/outputs/compositional_window.json`
- Format: json
- Contract: JSON object with numeric keys: "lower_bound" (float) and "upper_bound" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_functions_XB_0.100.csv`
- `/app/outputs/correlation_functions_XB_0.148.csv`
- `/app/outputs/correlation_functions_XB_0.172.csv`
- `/app/outputs/correlation_functions_XB_0.250.csv`
- `/app/outputs/compositional_window.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_functions_XB_0.100.csv
- path: `/app/outputs/correlation_functions_XB_0.100.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Translational and bond-orientational correlation functions for X_B=0.10. At long distances both ρ_G and Ψ should remain significantly above zero.
- schema:
  - `type`: table
  - `required_columns`: `r`, `rho_G`, `Psi`
  - `units`:
    - `r`: reduced distance
    - `rho_G`: dimensionless
    - `Psi`: dimensionless

### correlation_functions_XB_0.148.csv
- path: `/app/outputs/correlation_functions_XB_0.148.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Correlation functions for X_B=0.148. ρ_G is expected to become short-ranged, while Ψ remains quasi-long-ranged.
- schema:
  - `type`: table
  - `required_columns`: `r`, `rho_G`, `Psi`
  - `units`:
    - `r`: reduced distance
    - `rho_G`: dimensionless
    - `Psi`: dimensionless

### correlation_functions_XB_0.172.csv
- path: `/app/outputs/correlation_functions_XB_0.172.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Correlation functions at the representative hexatic-like composition X_B=0.172. ρ_G should decay to near zero over the sample, while Ψ persists quasi-long-ranged.
- schema:
  - `type`: table
  - `required_columns`: `r`, `rho_G`, `Psi`
  - `units`:
    - `r`: reduced distance
    - `rho_G`: dimensionless
    - `Psi`: dimensionless

### correlation_functions_XB_0.250.csv
- path: `/app/outputs/correlation_functions_XB_0.250.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Correlation functions for X_B=0.25 in the amorphous regime. Both ρ_G and Ψ should decay exponentially at short distances.
- schema:
  - `type`: table
  - `required_columns`: `r`, `rho_G`, `Psi`
  - `units`:
    - `r`: reduced distance
    - `rho_G`: dimensionless
    - `Psi`: dimensionless

### compositional_window.json
- path: `/app/outputs/compositional_window.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The compositional range of the hexatic-like intermediate phase determined from the correlation function analysis.
- schema:
  - `type`: object
  - `required`:
    - `lower_bound`: number
    - `upper_bound`: number

Notes: The correlation function CSVs are scored by structural trends (T3): the checker verifies that at large r, the curves satisfy specific inequality criteria that characterise the ordered, hexatic, and amorphous regimes. The compositional window is scored by result-level comparison (T0) against the paper's reported bounds with a tolerance that accounts for finite-size and sampling variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_functions_XB_0.100.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "rho_G",
          "Psi"
        ],
        "units": {
          "r": "reduced distance",
          "rho_G": "dimensionless",
          "Psi": "dimensionless"
        }
      },
      "description": "Translational and bond-orientational correlation functions for X_B=0.10. At long distances both ρ_G and Ψ should remain significantly above zero."
    },
    {
      "file": "correlation_functions_XB_0.148.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "rho_G",
          "Psi"
        ],
        "units": {
          "r": "reduced distance",
          "rho_G": "dimensionless",
          "Psi": "dimensionless"
        }
      },
      "description": "Correlation functions for X_B=0.148. ρ_G is expected to become short-ranged, while Ψ remains quasi-long-ranged."
    },
    {
      "file": "correlation_functions_XB_0.172.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "rho_G",
          "Psi"
        ],
        "units": {
          "r": "reduced distance",
          "rho_G": "dimensionless",
          "Psi": "dimensionless"
        }
      },
      "description": "Correlation functions at the representative hexatic-like composition X_B=0.172. ρ_G should decay to near zero over the sample, while Ψ persists quasi-long-ranged."
    },
    {
      "file": "correlation_functions_XB_0.250.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "rho_G",
          "Psi"
        ],
        "units": {
          "r": "reduced distance",
          "rho_G": "dimensionless",
          "Psi": "dimensionless"
        }
      },
      "description": "Correlation functions for X_B=0.25 in the amorphous regime. Both ρ_G and Ψ should decay exponentially at short distances."
    },
    {
      "file": "compositional_window.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lower_bound": "number",
          "upper_bound": "number"
        }
      },
      "description": "The compositional range of the hexatic-like intermediate phase determined from the correlation function analysis."
    }
  ],
  "notes": "The correlation function CSVs are scored by structural trends (T3): the checker verifies that at large r, the curves satisfy specific inequality criteria that characterise the ordered, hexatic, and amorphous regimes. The compositional window is scored by result-level comparison (T0) against the paper's reported bounds with a tolerance that accounts for finite-size and sampling variability."
}
```

## How you are scored
A hidden verifier will examine the artifacts you write. For each correlation CSV file, the verifier checks that the file exists and that the numerical curves satisfy structural expectations that characterise ordered, intermediate, and amorphous regimes (e.g., whether correlations are long‑ranged or short‑ranged). Your `compositional_window.json` is compared against exact reference bounds. The final reward is a weighted combination: the accuracy of the compositional window carries most of the weight, and the structural sanity checks of the correlation curves account for the remainder. Simply reporting plausible numbers without genuinely running the simulations and obtaining data from the specified MD procedure will not yield a high score.
