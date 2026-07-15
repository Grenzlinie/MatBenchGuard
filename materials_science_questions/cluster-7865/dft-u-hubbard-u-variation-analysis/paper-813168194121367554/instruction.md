# Spin-Polarized DFT Optimization and Electronic Structure of RFeAsO in the Cmma Phase

## Problem background
Iron-based pnictides RFeAsO (R = Pr, Nd, Sm, Gd) undergo a crystallographic phase transition from the tetragonal phase to the orthorhombic Cmma phase at low temperatures, accompanied by antiferromagnetic ordering of Fe and R ions. Density functional theory (DFT) calculations can be used to investigate how magnetic ordering influences structural parameters and how on-site Coulomb interactions (Hubbard U) affect electronic properties: the magnetic moments of Fe and R atoms, and the opening of a band gap at the Fermi level. In this task, you will compute these quantities for all four compounds using spin-polarized DFT with the GGA (PBE) functional and GGA+U approaches.

## Approach
The core idea is to perform first-principles DFT calculations on the orthorhombic Cmma magnetic cell (16 atoms) for each rare-earth compound using the projector augmented wave (PAW) method as implemented in QUANTUM ESPRESSO. First, you will construct the magnetic cell with stripe-like antiferromagnetic order on Fe and zigzag antiferromagnetic order on the rare-earth, using the known Wyckoff positions. Then, you will run a spin-polarized GGA structural optimization to obtain the equilibrium lattice parameters and atomic positions. On the optimized structures, you will compute the magnetic moments with pure GGA and with two GGA+U settings: U_R=5 eV with U_Fe=2 eV, and U_R=5 eV with U_Fe=3 eV. Finally, using the GGA+U scheme with U_R=5 eV and U_Fe=3 eV, you will compute the electronic band structure and/or density of states to determine the band gap at the Fermi level for each compound.

## Reproduction target
For each compound R = Pr, Nd, Sm, Gd, you must:
1. Optimize the orthorhombic Cmma magnetic cell within spin-polarized GGA and report the lattice constants a, b, c, the internal coordinates z_R and z_As, and the two distinct Fe-As bond lengths. Save these as step_01_structural_parameters.csv.
2. Using the optimized structures, compute the magnetic moments (in μ_B) of the R and Fe atoms under three schemes: pure GGA, GGA+U with U_R=5 eV and U_Fe=2 eV, and GGA+U with U_R=5 eV and U_Fe=3 eV. Save these as step_02_magnetic_moments.csv.
3. Using GGA+U with U_R=5 eV and U_Fe=3 eV, compute the electronic band gap at the Fermi level for each compound; if no gap opens, report “metallic”. Save these as step_03_dos_gap.csv.
The hidden verifier will check your results against reference values.

## Assets

- QUANTUM ESPRESSO: https://www.quantum-espresso.org/
- ATOMPAW: https://github.com/rcb008/atompaw
- Rare-earth PAW pseudopotentials (Pr, Nd, Sm, Gd): http://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Construct magnetic Cmma supercell
- Role: process
- Action: Construct the 16-atom orthorhombic Cmma magnetic cell with stripe-like antiferromagnetic order on Fe ions and zigzag-like antiferromagnetic order on rare-earth ions, using the experimental Wyckoff positions (R at 2b, Fe at 4b, As at 4g, O at 4a) and internal coordinates from literature.
- Evidence: `/app/outputs/magnetic_cell.txt`

### Step 2: Spin-polarized GGA structural optimization
- Role: scored
- Action: Perform spin-polarized GGA (PBE) structural optimization of the magnetic Cmma cell for each compound (R=Pr,Nd,Sm,Gd) using QUANTUM ESPRESSO. Extract lattice constants a, b, c, internal coordinates z_R, z_As, and the two Fe-As bond lengths.
- Output file: `/app/outputs/step_01_structural_parameters.csv`
- Format: csv
- Contract: compound, a (Å), b (Å), c (Å), z_R, z_As, Fe_As_1 (Å), Fe_As_2 (Å)
- Scoring: scored by hidden verifier

### Step 3: Compute magnetic moments (GGA and GGA+U)
- Role: scored (load-bearing)
- Action: On the optimized magnetic structure, perform spin-polarized calculations using GGA and GGA+U (U_R=5 eV, U_Fe=2 eV; U_R=5 eV, U_Fe=3 eV) and extract magnetic moments of R and Fe atoms.
- Output file: `/app/outputs/step_02_magnetic_moments.csv`
- Format: csv
- Contract: compound, method, R_moment (μ_B), Fe_moment (μ_B)
- Scoring: scored by hidden verifier

### Step 4: Determine band gap under GGA+U
- Role: scored
- Action: Compute electronic band structure or density of states for each compound using GGA+U (U_R=5 eV, U_Fe=3 eV) and extract the band gap at the Fermi level. Report the gap value in eV or state 'metallic' if no gap opens.
- Output file: `/app/outputs/step_03_dos_gap.csv`
- Format: csv
- Contract: compound, U_Fe (eV), gap (eV or 'metallic')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_parameters.csv`
- `/app/outputs/step_02_magnetic_moments.csv`
- `/app/outputs/step_03_dos_gap.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_parameters.csv
- path: `/app/outputs/step_01_structural_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized structural parameters for the magnetic cell.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a (Å)`, `b (Å)`, `c (Å)`, `z_R`, `z_As`, `Fe_As_1 (Å)`, `Fe_As_2 (Å)`
  - `units`:
    - `a (Å)`: Å
    - `b (Å)`: Å
    - `c (Å)`: Å
    - `z_R`: dimensionless
    - `z_As`: dimensionless
    - `Fe_As_1 (Å)`: Å
    - `Fe_As_2 (Å)`: Å

### step_02_magnetic_moments.csv
- path: `/app/outputs/step_02_magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetic moments of rare-earth and iron atoms for different Hubbard U values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `method`, `R_moment (μ_B)`, `Fe_moment (μ_B)`
  - `columns`:
    - `compound`:
      - `type`: string
    - `method`:
      - `type`: string
      - `enum`: `GGA`, `GGA+U (U_Fe=2)`, `GGA+U (U_Fe=3)`
    - `R_moment (μ_B)`:
      - `type`: number
    - `Fe_moment (μ_B)`:
      - `type`: number
  - `units`:
    - `R_moment (μ_B)`: μ_B
    - `Fe_moment (μ_B)`: μ_B

### step_03_dos_gap.csv
- path: `/app/outputs/step_03_dos_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap value under GGA+U (U_R=5, U_Fe=3) for each compound.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `U_Fe (eV)`, `gap`
  - `units`:
    - `U_Fe (eV)`: eV
    - `gap`: eV or 'metallic'

Notes: All quantities must be derived from the DFT calculations; the checker will compare the reported values against hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a (Å)",
          "b (Å)",
          "c (Å)",
          "z_R",
          "z_As",
          "Fe_As_1 (Å)",
          "Fe_As_2 (Å)"
        ],
        "units": {
          "a (Å)": "Å",
          "b (Å)": "Å",
          "c (Å)": "Å",
          "z_R": "dimensionless",
          "z_As": "dimensionless",
          "Fe_As_1 (Å)": "Å",
          "Fe_As_2 (Å)": "Å"
        }
      },
      "description": "Optimized structural parameters for the magnetic cell."
    },
    {
      "file": "step_02_magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "method",
          "R_moment (μ_B)",
          "Fe_moment (μ_B)"
        ],
        "columns": {
          "compound": {
            "type": "string"
          },
          "method": {
            "type": "string",
            "enum": [
              "GGA",
              "GGA+U (U_Fe=2)",
              "GGA+U (U_Fe=3)"
            ]
          },
          "R_moment (μ_B)": {
            "type": "number"
          },
          "Fe_moment (μ_B)": {
            "type": "number"
          }
        },
        "units": {
          "R_moment (μ_B)": "μ_B",
          "Fe_moment (μ_B)": "μ_B"
        }
      },
      "description": "Magnetic moments of rare-earth and iron atoms for different Hubbard U values."
    },
    {
      "file": "step_03_dos_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "U_Fe (eV)",
          "gap"
        ],
        "units": {
          "U_Fe (eV)": "eV",
          "gap": "eV or 'metallic'"
        }
      },
      "description": "Band gap value under GGA+U (U_R=5, U_Fe=3) for each compound."
    }
  ],
  "notes": "All quantities must be derived from the DFT calculations; the checker will compare the reported values against hidden reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three scored artifacts you produce. For each artifact, it will compare your submitted values to hidden reference values using appropriate tolerances and assign a score. The final reward is a weighted combination: structural parameters contribute the largest share (about 50% of the total reward), magnetic moments about 40%, and the band gap check about 10%. The verifier does not inspect your workflow steps or intermediate logs; only the final CSV files are read. You must follow the described approach and report the quantities exactly as specified in each output file’s contract. Simply copying known numbers will be detected because the verifier checks for internal consistency and plausible derivation from the actual computational procedure.
