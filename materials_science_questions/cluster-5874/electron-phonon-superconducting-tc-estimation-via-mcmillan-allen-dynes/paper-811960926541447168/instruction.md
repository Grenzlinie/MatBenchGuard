# DFT Study of Superconducting Properties in Cu-Intercalated TiSe2

## Problem background
Layered TiSe₂ undergoes a charge‑density‑wave (CDW) transition, and intercalation with copper suppresses this CDW while inducing superconductivity. Understanding how copper doping modifies the electronic density of states near the Fermi energy is crucial for explaining the doping‑dependent CDW–superconductivity phase diagram. This task investigates the electronic structure of undoped TiSe₂ and of a Cu‑intercalated supercell CuTi₁₂Se₂₄ at several lattice constants by computing the density of states (DOS) and from it a set of derived properties (electron‑phonon coupling, superconducting critical temperature, Stoner factor, electronic specific heat).

## Approach
Use density‑functional theory (DFT) to perform self‑consistent electronic‑structure calculations for the primitive cell of TiSe₂ and for a 2×2×3 supercell of CuTi₁₂Se₂₄ (48 sites, one intercalated Cu). Compute the total density of states on a fine energy grid relative to the Fermi level for each system at the required lattice constants. From the supercell calculations extract the site‑projected density of states at the Fermi energy for Cu‑d, Ti near Cu, and Ti far from Cu.

Post‑process the results: obtain the total N(E_F) for each volume, then estimate the electron‑phonon coupling λ using the rigid‑ion approximation together with Debye temperatures that scale with volume, compute the superconducting critical temperature T_c via the McMillan–Allen–Dynes equation (effective Coulomb repulsion μ* = 0.13), evaluate the Stoner factor from the paramagnetic density of states, and calculate the electronic specific‑heat coefficient γ (including the λ enhancement). Carry out this procedure for the three lattice constants specified in the workflow steps.

## Reproduction target
The goal is to produce the total DOS curves for undoped TiSe₂ and for CuTi₁₂Se₂₄ at the three lattice constants (a = 6.70, 6.67, 6.53 a.u., with c scaled proportionally), to tabulate the site‑projected N(E_F) from the supercells, and to report a table of derived properties (λ, T_c, Stoner factor S, γ, and total N(E_F)) for each lattice constant. The quantities must be obtained from first‑principles calculations and the post‑processing protocol described, and the results should reflect the expected volume dependence of the electronic structure.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, Elk): https://www.quantum-espresso.org
- Crystal structure of TiSe2 (CdI2 type, space group P-3m1)
- Debye temperature values for λ estimation
- McMillan-Allen-Dynes equation for Tc
- Exchange integral parameter for Stoner factor

## Workflow steps

### Step 1: Compute total DOS of undoped TiSe2
- Role: scored
- Action: Perform a self-consistent DFT calculation for the primitive unit cell of TiSe2 (space group P-3m1) at a lattice constant of about 6.67 a.u. (or 6.7 a.u.). Compute the total density of states on a fine energy grid relative to the Fermi energy. The result should exhibit a low density of states at the Fermi energy and a sharply rising shoulder just above it. Save the data as two columns: energy (Ry, relative to EF) and total DOS (states/Ry/cell).
- Output file: `/app/outputs/total_dos_undoped.csv`
- Format: csv
- Contract: Columns: Energy_Ry (float, energy relative to E_F in Ry), Total_DOS_states_per_Ry_cell (float).
- Scoring: scored by hidden verifier

### Step 2: Compute total DOS of CuTi12Se24 at a=6.7 a.u.
- Role: scored
- Action: Set up a 2×2×3 supercell of CuTi12Se24 (one Cu intercalated) with lattice constants a = 6.7 a.u., c = 11.35 a.u.. Perform a self-consistent DFT calculation and compute the total DOS on a fine energy grid relative to EF. Save the data as energy (Ry) and total DOS (states/Ry/cell).
- Output file: `/app/outputs/total_dos_doped_a670.csv`
- Format: csv
- Contract: Columns: Energy_Ry (float), Total_DOS_states_per_Ry_cell (float).
- Scoring: scored by hidden verifier

### Step 3: Compute total DOS of CuTi12Se24 at a=6.67 a.u.
- Role: scored
- Action: Repeat the supercell calculation with lattice constant a = 6.67 a.u. (c scaled proportionally from the a=6.7 a.u. value). Compute the total DOS and save as before.
- Output file: `/app/outputs/total_dos_doped_a667.csv`
- Format: csv
- Contract: Columns: Energy_Ry (float), Total_DOS_states_per_Ry_cell (float).
- Scoring: scored by hidden verifier

### Step 4: Compute total DOS of CuTi12Se24 at a=6.53 a.u.
- Role: scored
- Action: Repeat the supercell calculation with lattice constant a = 6.53 a.u. (c scaled proportionally). Compute the total DOS and save as before.
- Output file: `/app/outputs/total_dos_doped_a653.csv`
- Format: csv
- Contract: Columns: Energy_Ry (float), Total_DOS_states_per_Ry_cell (float).
- Scoring: scored by hidden verifier

### Step 5: Extract site-projected DOS at EF and compile table
- Role: scored
- Action: From the three supercell DFT calculations, extract the site-projected density of states at EF for Cu d, Ti_Cu (Ti near Cu), and Ti (Ti far from Cu). Compile the results as a table with lattice constant, site label, and N(EF) in states/(Ry·atom).
- Output file: `/app/outputs/projected_dos_table.csv`
- Format: csv
- Contract: Columns: a0 (float, lattice constant in a.u.), site (string, one of 'Cu_d', 'Ti_Cu_d', 'Ti_d'), N_EF_states_per_Ry_atom (float).
- Scoring: scored by hidden verifier

### Step 6: Compute superconducting and magnetic properties
- Role: scored (load-bearing)
- Action: For each of the three lattice constants: (1) obtain the total N(EF) in states/(Ry·cell) from the total DOS curves; (2) compute the electron-phonon coupling λ using the rigid-ion approximation with the given Debye temperatures (240, 250, 290 K) and the experimental phonon moment scaling; (3) compute superconducting Tc from λ via the McMillan-Allen-Dynes equation with μ* = 0.13; (4) compute the Stoner factor S from the paramagnetic N(EF) using the exchange integral for Ti d; (5) compute the electronic specific heat coefficient γ (including λ enhancement). Save one row per lattice constant in a table.
- Output file: `/app/outputs/derived_properties_table.csv`
- Format: csv
- Contract: Columns: a0 (float, lattice constant in a.u.), lambda (float), Tc_K (float, superconducting critical temperature in K), Stoner_S (float, Stoner factor), gamma_mJ_per_mol_K2 (float, electronic specific heat coefficient in mJ/(mol·K²)), N_EF_total_states_per_Ry_cell (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_dos_undoped.csv`
- `/app/outputs/total_dos_doped_a670.csv`
- `/app/outputs/total_dos_doped_a667.csv`
- `/app/outputs/total_dos_doped_a653.csv`
- `/app/outputs/projected_dos_table.csv`
- `/app/outputs/derived_properties_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_dos_undoped.csv
- path: `/app/outputs/total_dos_undoped.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total density of states for undoped TiSe2. The checker will extract N(EF) at E=0 and verify the low value and the sharp rising shoulder above EF.
- schema:
  - `type`: table
  - `required_columns`: `Energy_Ry`, `Total_DOS_states_per_Ry_cell`
  - `units`:
    - `Energy_Ry`: Ry (relative to EF)
    - `Total_DOS_states_per_Ry_cell`: states/(Ry·cell)

### total_dos_doped_a670.csv
- path: `/app/outputs/total_dos_doped_a670.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total DOS for doped CuTi12Se24 at a=6.7 a.u.
- schema:
  - `type`: table
  - `required_columns`: `Energy_Ry`, `Total_DOS_states_per_Ry_cell`
  - `units`:
    - `Energy_Ry`: Ry (relative to EF)
    - `Total_DOS_states_per_Ry_cell`: states/(Ry·cell)

### total_dos_doped_a667.csv
- path: `/app/outputs/total_dos_doped_a667.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total DOS at a=6.67 a.u.
- schema:
  - `type`: table
  - `required_columns`: `Energy_Ry`, `Total_DOS_states_per_Ry_cell`
  - `units`:
    - `Energy_Ry`: Ry (relative to EF)
    - `Total_DOS_states_per_Ry_cell`: states/(Ry·cell)

### total_dos_doped_a653.csv
- path: `/app/outputs/total_dos_doped_a653.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total DOS at a=6.53 a.u.
- schema:
  - `type`: table
  - `required_columns`: `Energy_Ry`, `Total_DOS_states_per_Ry_cell`
  - `units`:
    - `Energy_Ry`: Ry (relative to EF)
    - `Total_DOS_states_per_Ry_cell`: states/(Ry·cell)

### projected_dos_table.csv
- path: `/app/outputs/projected_dos_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Site-projected density of states at EF from the supercell calculations. The checker compares the values to the paper's Table II.
- schema:
  - `type`: table
  - `required_columns`: `a0`, `site`, `N_EF_states_per_Ry_atom`
  - `units`:
    - `a0`: a.u.
    - `site`: string
    - `N_EF_states_per_Ry_atom`: states/(Ry·atom)

### derived_properties_table.csv
- path: `/app/outputs/derived_properties_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived superconducting and magnetic properties. The checker recomputes Tc from λ and Debye temperature, then compares all quantities to the paper's reported values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `a0`, `lambda`, `Tc_K`, `Stoner_S`, `gamma_mJ_per_mol_K2`, `N_EF_total_states_per_Ry_cell`
  - `units`:
    - `a0`: a.u.
    - `lambda`: dimensionless
    - `Tc_K`: K
    - `Stoner_S`: dimensionless
    - `gamma_mJ_per_mol_K2`: mJ/(mol·K²)
    - `N_EF_total_states_per_Ry_cell`: states/(Ry·cell)

Notes: All quantities are obtained from first-principles DFT calculations and post-processing using the rigid-ion approximation, McMillan-Allen-Dynes equation, and Stoner model. The scoring tolerances are chosen to account for differences in DFT implementation, exchange-correlation functional, and basis sets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_dos_undoped.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_Ry",
          "Total_DOS_states_per_Ry_cell"
        ],
        "units": {
          "Energy_Ry": "Ry (relative to EF)",
          "Total_DOS_states_per_Ry_cell": "states/(Ry·cell)"
        }
      },
      "description": "Total density of states for undoped TiSe2. The checker will extract N(EF) at E=0 and verify the low value and the sharp rising shoulder above EF."
    },
    {
      "file": "total_dos_doped_a670.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_Ry",
          "Total_DOS_states_per_Ry_cell"
        ],
        "units": {
          "Energy_Ry": "Ry (relative to EF)",
          "Total_DOS_states_per_Ry_cell": "states/(Ry·cell)"
        }
      },
      "description": "Total DOS for doped CuTi12Se24 at a=6.7 a.u."
    },
    {
      "file": "total_dos_doped_a667.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_Ry",
          "Total_DOS_states_per_Ry_cell"
        ],
        "units": {
          "Energy_Ry": "Ry (relative to EF)",
          "Total_DOS_states_per_Ry_cell": "states/(Ry·cell)"
        }
      },
      "description": "Total DOS at a=6.67 a.u."
    },
    {
      "file": "total_dos_doped_a653.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_Ry",
          "Total_DOS_states_per_Ry_cell"
        ],
        "units": {
          "Energy_Ry": "Ry (relative to EF)",
          "Total_DOS_states_per_Ry_cell": "states/(Ry·cell)"
        }
      },
      "description": "Total DOS at a=6.53 a.u."
    },
    {
      "file": "projected_dos_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0",
          "site",
          "N_EF_states_per_Ry_atom"
        ],
        "units": {
          "a0": "a.u.",
          "site": "string",
          "N_EF_states_per_Ry_atom": "states/(Ry·atom)"
        }
      },
      "description": "Site-projected density of states at EF from the supercell calculations. The checker compares the values to the paper's Table II."
    },
    {
      "file": "derived_properties_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0",
          "lambda",
          "Tc_K",
          "Stoner_S",
          "gamma_mJ_per_mol_K2",
          "N_EF_total_states_per_Ry_cell"
        ],
        "units": {
          "a0": "a.u.",
          "lambda": "dimensionless",
          "Tc_K": "K",
          "Stoner_S": "dimensionless",
          "gamma_mJ_per_mol_K2": "mJ/(mol·K²)",
          "N_EF_total_states_per_Ry_cell": "states/(Ry·cell)"
        }
      },
      "description": "Derived superconducting and magnetic properties. The checker recomputes Tc from λ and Debye temperature, then compares all quantities to the paper's reported values with appropriate tolerances."
    }
  ],
  "notes": "All quantities are obtained from first-principles DFT calculations and post-processing using the rigid-ion approximation, McMillan-Allen-Dynes equation, and Stoner model. The scoring tolerances are chosen to account for differences in DFT implementation, exchange-correlation functional, and basis sets."
}
```

## How you are scored
After submission, a hidden verifier independently inspects each scored artifact. It checks the DOS curves for characteristic structural features, reads the tabulated N(E_F) values and derived properties, and compares them against reference results obtained through a faithful implementation of the same protocol. The verifier may also recompute T_c from the submitted λ and Debye temperature to test internal consistency, and it examines the trend of the properties as the lattice constant changes. The final reward is a weighted combination of the scores from the individual artifacts, so simply reporting numeric values without performing the required calculations will not yield a high score.
