# Ab initio electronic and magnetic structure of RE5Ge3 intermetallic compounds

## Problem background
Rare-earth intermetallic compounds $RE_5Ge_3$ ($RE = La, Ce, Pr, Nd$) adopt the hexagonal $Mn_5Si_3$ structure and are known for complex magnetic behaviour including multiple transitions at low temperature. First-principles calculations within density functional theory can provide insight into the electronic and magnetic ground state, but accurate description of the strongly correlated $4f$ electrons (and $5d$ for La) requires treatment of on-site Coulomb interactions and spin–orbit coupling. This task reproduces a *ab initio* study of these materials by computing self‑consistent Hubbard $U$ parameters, equilibrium lattice constants, and magnetic moments from open‑source DFT.

## Approach
Use the local spin density approximation (LSDA) as the base density functional. First, obtain a relaxed LSDA electronic structure for each of the four compounds. From this, compute the effective on‑site Coulomb interaction $U_{\mathrm{eff}}$ for the rare‑earth localized orbitals ($La$‑$5d$, $Ce$‑$4f$, $Pr$‑$4f$, $Nd$‑$4f$) via the Madsen–Novák linear‑response method. Second, apply these $U$ values in LSDA+$U$ calculations to relax the crystal structures and determine the equilibrium lattice parameters $a$ and $c$. Third, perform spin‑polarised LSDA+$U$ including spin–orbit coupling (LSDA+$U$+SO) at the relaxed geometries to extract total and site‑projected spin magnetic moments on the two inequivalent $RE$ sites and on the $Ge$ site. The original work used the full‑potential linearised augmented‑plane‑wave code WIEN2K; reproduce the same methodological sequence with an open‑source alternative such as Quantum ESPRESSO, which implements LSDA, LSDA+$U$, spin–orbit coupling, and the Madsen–Novák $U$ determination.

## Reproduction target
For the four hexagonal $RE_5Ge_3$ compounds ($La_5Ge_3$, $Ce_5Ge_3$, $Pr_5Ge_3$, $Nd_5Ge_3$), using the LSDA, Madsen–Novák linear‑response, LSDA+$U$, and LSDA+$U$+SO protocols described above:
- Determine the on‑site Hubbard $U$ parameter for the rare‑earth $4f$ (or $5d$ for $La$) orbitals.
- Obtain the LSDA+$U$ equilibrium lattice constants $a$, $c$, and the unit cell volume.
- Compute the total spin magnetic moment and the site‑resolved moments on the two $RE$ positions and the $Ge$ position within LSDA+$U$+SO.
Report the results in the three CSV files specified in the workflow steps.

## Assets

- Quantum ESPRESSO: quantum-espresso

## Crystal structure data

All compounds adopt the hexagonal Mn₅Si₃‑type structure with space group P6₃/mcm (No. 193). There are two inequivalent rare‑earth sites and one Ge site:

- RE1: 4d Wyckoff position (1/3, 2/3, 0)
- RE2: 6g (x_RE, 0, 1/4)
- Ge: 6g (x_Ge, 0, 1/4)

The following table gives the initial lattice parameters (from experimental data) and the internal coordinates x_RE, x_Ge (from the paper’s LSDA‑optimized geometry) to be used as starting guesses for the DFT relaxation.

| Compound | a (Å) | c (Å) | x_RE  | x_Ge   |
|----------|-------|-------|-------|--------|
| La₅Ge₃   | 8.95  | 6.90  | 0.2427| 0.6086 |
| Ce₅Ge₃   | 8.84  | 6.72  | 0.2627| 0.6171 |
| Pr₅Ge₃   | 8.79  | 6.66  | 0.2324| 0.5966 |
| Nd₅Ge₃   | 8.74  | 6.60  | 0.2499| 0.6073 |

## Workflow steps

### Step 1: LSDA Structure Relaxation
- Role: process
- Action: Perform LSDA geometry optimization for each of the four compounds (La5Ge3, Ce5Ge3, Pr5Ge3, Nd5Ge3) to obtain converged electronic ground states and initial structural parameters. These calculations are a prerequisite for the Hubbard U calculation.
- Evidence: none

### Step 2: Hubbard U via Madsen–Novák method
- Role: scored (load-bearing)
- Action: For each compound, compute the effective on-site Coulomb interaction U_eff for the localized orbitals (La-5d, Ce-4f, Pr-4f, Nd-4f) using the Madsen–Novák linear-response approach on the LSDA electronic structure.
- Output file: `/app/outputs/step_01_U_values.csv`
- Format: csv
- Contract: Columns: compound (string), U_type (string, one of 'd' or 'f'), U_value (float, eV). Rows for La, Ce, Pr, Nd.
- Scoring: scored by hidden verifier

### Step 3: LSDA+U Structural Optimization
- Role: scored
- Action: For each compound, perform LSDA+U structural optimization using the Hubbard U values computed in Step 1 to determine the equilibrium lattice parameters a, c, and the unit cell volume.
- Output file: `/app/outputs/step_02_lattice_constants.csv`
- Format: csv
- Contract: Columns: compound (string), method (string, e.g. 'LSDA+U'), a (float, angstrom), c (float, angstrom), volume (float, angstrom^3).
- Scoring: scored by hidden verifier

### Step 4: LSDA+U+SO Magnetic Moment Calculation
- Role: scored
- Action: For the magnetic compounds Ce5Ge3, Pr5Ge3, Nd5Ge3 (and optionally La5Ge3 with zero moments), perform a spin-polarized LSDA+U+SO calculation at the optimized geometry to obtain the total magnetic moment and site-resolved spin moments on the two inequivalent RE sites and the Ge site.
- Output file: `/app/outputs/step_03_magnetic_moments.csv`
- Format: csv
- Contract: Columns: compound (string), method (string, e.g. 'LSDA+U+SO'), total_moment (float, mu_B), RE1_moment (float, mu_B), RE2_moment (float, mu_B), Ge_moment (float, mu_B).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_U_values.csv`
- `/app/outputs/step_02_lattice_constants.csv`
- `/app/outputs/step_03_magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_U_values.csv
- path: `/app/outputs/step_01_U_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed on-site Hubbard U parameters for the RE localized orbitals. Columns: compound (La, Ce, Pr, Nd), U_type ('d' or 'f'), U_value (float in eV).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `U_type`, `U_value`
  - `units`:
    - `U_value`: eV

### step_02_lattice_constants.csv
- path: `/app/outputs/step_02_lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: LSDA+U equilibrium lattice constants. Columns: compound (La, Ce, Pr, Nd), method (e.g. LSDA+U), a (float Å), c (float Å), volume (float Å^3).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `method`, `a`, `c`, `volume`
  - `units`:
    - `a`: angstrom
    - `c`: angstrom
    - `volume`: angstrom^3

### step_03_magnetic_moments.csv
- path: `/app/outputs/step_03_magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Spin magnetic moments from LSDA+U+SO calculations. Columns: compound (Ce, Pr, Nd; La optional), method, total_moment (float μ_B), RE1_moment (float μ_B), RE2_moment (float μ_B), Ge_moment (float μ_B).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `method`, `total_moment`, `RE1_moment`, `RE2_moment`, `Ge_moment`
  - `units`:
    - `total_moment`: mu_B
    - `RE1_moment`: mu_B
    - `RE2_moment`: mu_B
    - `Ge_moment`: mu_B

Notes: The agent must perform DFT calculations using an open-source code (e.g., Quantum ESPRESSO) capable of LSDA, LSDA+U, spin-orbit coupling, and the Madsen–Novák linear-response Hubbard U method. Crystal structures are provided in the instruction. The checker compares submitted CSV values against paper-reported results within appropriate tolerances to account for code-to-code spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_U_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "U_type",
          "U_value"
        ],
        "units": {
          "U_value": "eV"
        }
      },
      "description": "Computed on-site Hubbard U parameters for the RE localized orbitals. Columns: compound (La, Ce, Pr, Nd), U_type ('d' or 'f'), U_value (float in eV)."
    },
    {
      "file": "step_02_lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "method",
          "a",
          "c",
          "volume"
        ],
        "units": {
          "a": "angstrom",
          "c": "angstrom",
          "volume": "angstrom^3"
        }
      },
      "description": "LSDA+U equilibrium lattice constants. Columns: compound (La, Ce, Pr, Nd), method (e.g. LSDA+U), a (float Å), c (float Å), volume (float Å^3)."
    },
    {
      "file": "step_03_magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "method",
          "total_moment",
          "RE1_moment",
          "RE2_moment",
          "Ge_moment"
        ],
        "units": {
          "total_moment": "mu_B",
          "RE1_moment": "mu_B",
          "RE2_moment": "mu_B",
          "Ge_moment": "mu_B"
        }
      },
      "description": "Spin magnetic moments from LSDA+U+SO calculations. Columns: compound (Ce, Pr, Nd; La optional), method, total_moment (float μ_B), RE1_moment (float μ_B), RE2_moment (float μ_B), Ge_moment (float μ_B)."
    }
  ],
  "notes": "The agent must perform DFT calculations using an open-source code (e.g., Quantum ESPRESSO) capable of LSDA, LSDA+U, spin-orbit coupling, and the Madsen–Novák linear-response Hubbard U method. Crystal structures are provided in the instruction. The checker compares submitted CSV values against paper-reported results within appropriate tolerances to account for code-to-code spread."
}
```

## How you are scored
A hidden verifier independently scores each of the three scored output artefacts: the $U$ values, the lattice constants, and the magnetic moments. The verifier compares your submitted CSV files to a set of reference results (not disclosed to you) using appropriate numerical tolerances that account for the use of a different DFT code and small methodological variations. Each component is assigned a weight, and the final reward is the weighted sum of the component scores. Merely writing numbers that match the reference is not sufficient—the verifier expects the CSV files to be produced by a genuine computational workflow, but it does not re‑run the heavy DFT calculations. Only the files placed under `/app/outputs` are evaluated.
