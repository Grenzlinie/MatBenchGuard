# Ab initio low-density amorphous carbon model and properties

## Problem background
Low-density amorphous carbon is a disordered solid consisting primarily of carbon atoms with mixed sp, sp², and sp³ bonding. Understanding its atomic-scale microstructure and how bonding preferences change with density is important for interpreting its experimentally measured properties. This task focuses on generating a realistic amorphous carbon model and computing its structural, vibrational, and electronic properties from first principles. The results illustrate how different hybridizations contribute to the overall behavior of the material.

## Approach
The simulation procedure follows a melt-quench approach using plane-wave density functional theory (DFT) with a local-density approximation (LDA) and projector augmented-wave (PAW) pseudopotential. A cubic cell containing 120 carbon atoms at a target mass density of 1.50 g/cm³ is prepared with random initial coordinates. The system is heated to a high temperature, equilibrated, then cooled to 300 K over a prescribed time while maintaining constant volume. After cooling, the structure is relaxed via conjugate-gradient minimization. From the relaxed structure we compute the radial distribution function g(r), the vibrational eigenfrequencies by constructing and diagonalizing the dynamical matrix through small atomic displacements, and the electronic density of states (total and p-orbital projected) from a single-point DFT calculation. All steps use open‑source tools.

## Reproduction target
Generate a 120-atom amorphous carbon model at density 1.50 g/cm³ using the melt-quench and relaxation protocol described in the workflow steps. From the resulting structure, produce:
- the radial distribution function g(r) up to at least 6 Å,
- a list of vibrational eigenfrequencies derived from the dynamical matrix,
- the total and p-projected electronic density of states in the range −10 to +10 eV relative to the Fermi level.

The submitted artifacts will be evaluated against expected physical signatures: realistic bonding statistics, peak positions in the radial distribution function, the shape of the vibrational density of states and the high-temperature harmonic specific heat trend, and the presence of a pseudogap and orbital character in the electronic density of states.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- C LDA PAW pseudopotential: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Melt-quench AIMD simulation and structure relaxation
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO with an LDA PAW pseudopotential for carbon, perform constant-volume ab initio molecular dynamics for a system of 120 carbon atoms at a target mass density of 1.50 g/cm³. Start from random coordinates, heat to 8000 K, equilibrate, melt-quench to 300 K over 15 ps, and finally perform conjugate-gradient relaxation. Output the fully relaxed atomic structure.
- Output file: `/app/outputs/step_01_structure.xyz`
- Format: txt
- Contract: XYZ format text: first line = number of atoms N; second line = a comment string (e.g., cell vectors); next N lines each contain symbol 'C' followed by three space-separated Cartesian coordinates in Angstrom.
- Scoring: scored by hidden verifier

### Step 2: Vibrational eigenfrequency calculation
- Role: scored
- Action: Using the relaxed structure from step_01, perform single-point force calculations with Quantum ESPRESSO for each atom displaced by ±0.015 Å along x, y, and z directions to construct the force constant matrix. Diagonalize the matrix to obtain vibrational eigenfrequencies. Output the non-zero frequencies.
- Output file: `/app/outputs/step_02_eigenfrequencies.txt`
- Format: txt
- Contract: One eigenfrequency per line, in cm⁻¹, as a floating-point number. Sorted ascending. First three zero-frequency translation modes may be omitted; total lines = 3N-3 where N is the number of atoms.
- Scoring: scored by hidden verifier

### Step 3: Radial distribution function computation
- Role: scored
- Action: From the relaxed atomic structure in step_01, compute the radial distribution function g(r) up to at least 6 Å with fine spacing. Output the g(r) data.
- Output file: `/app/outputs/step_03_rdf_data.csv`
- Format: csv
- Contract: Two comma-separated columns: r (Angstrom) and g(r) (dimensionless). No header row. At least 300 rows covering r from 0 to 6 Å.
- Scoring: scored by hidden verifier

### Step 4: Electronic density of states calculation
- Role: scored
- Action: Perform a single-point electronic-structure calculation on the relaxed structure from step_01 to obtain the total and p-orbital projected density of states. Align the energy scale to the Fermi level, and output the data covering at least the range -10 eV to +10 eV.
- Output file: `/app/outputs/step_04_edos_data.csv`
- Format: csv
- Contract: Three comma-separated columns: energy (eV, relative to Fermi level), total DOS (arbitrary normalized), p-orbital projected DOS (same normalization). No header or header optional. At least 200 rows covering -10 to +10 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structure.xyz`
- `/app/outputs/step_02_eigenfrequencies.txt`
- `/app/outputs/step_03_rdf_data.csv`
- `/app/outputs/step_04_edos_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structure.xyz
- path: `/app/outputs/step_01_structure.xyz`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Relaxed atomic structure of the 120-atom amorphous carbon model at 1.50 g/cm³. Checker recomputes coordination and hybridization fractions.
- schema:
  - `type`: text
  - `description`: XYZ format: first line N; second line comment (cell vectors); next N lines each 'C x y z' in Angstrom.

### step_02_eigenfrequencies.txt
- path: `/app/outputs/step_02_eigenfrequencies.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Vibrational eigenfrequencies used to compute VDOS and harmonic specific heat; checker checks shape and Dulong-Petit limit.
- schema:
  - `type`: text
  - `description`: One floating-point eigenfrequency per line in cm⁻¹, sorted ascending, 3N-3 lines.

### step_03_rdf_data.csv
- path: `/app/outputs/step_03_rdf_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Radial distribution function g(r) table; checker verifies first and second peak positions within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `r`, `g(r)`
  - `units`:
    - `r`: Angstrom
    - `g(r)`: dimensionless

### step_04_edos_data.csv
- path: `/app/outputs/step_04_edos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electronic density of states; checker inspects Fermi-level pseudogap and p-orbital dominance.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_dos`, `p_dos`
  - `units`:
    - `energy_eV`: eV
    - `total_dos`: arbitrary
    - `p_dos`: arbitrary

Notes: All outputs are derived from the same ab initio melt-quench simulation of step_01. The agent is free to choose any open-source plane-wave DFT implementation and specific run parameters (timestep, thermostat, k-point sampling, etc.), provided the overall 15 ps cooling from 8000 K to 300 K and final relaxation are achieved. No gold values or tolerances are public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structure.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "XYZ format: first line N; second line comment (cell vectors); next N lines each 'C x y z' in Angstrom."
      },
      "description": "Relaxed atomic structure of the 120-atom amorphous carbon model at 1.50 g/cm³. Checker recomputes coordination and hybridization fractions."
    },
    {
      "file": "step_02_eigenfrequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "One floating-point eigenfrequency per line in cm⁻¹, sorted ascending, 3N-3 lines."
      },
      "description": "Vibrational eigenfrequencies used to compute VDOS and harmonic specific heat; checker checks shape and Dulong-Petit limit."
    },
    {
      "file": "step_03_rdf_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "g(r)"
        ],
        "units": {
          "r": "Angstrom",
          "g(r)": "dimensionless"
        }
      },
      "description": "Radial distribution function g(r) table; checker verifies first and second peak positions within tolerance."
    },
    {
      "file": "step_04_edos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_dos",
          "p_dos"
        ],
        "units": {
          "energy_eV": "eV",
          "total_dos": "arbitrary",
          "p_dos": "arbitrary"
        }
      },
      "description": "Electronic density of states; checker inspects Fermi-level pseudogap and p-orbital dominance."
    }
  ],
  "notes": "All outputs are derived from the same ab initio melt-quench simulation of step_01. The agent is free to choose any open-source plane-wave DFT implementation and specific run parameters (timestep, thermostat, k-point sampling, etc.), provided the overall 15 ps cooling from 8000 K to 300 K and final relaxation are achieved. No gold values or tolerances are public."
}
```

## How you are scored
Each scored workflow step produces a single output file. A hidden verifier processes these artifacts independently:
- From the relaxed structure, it recomputes coordination and bonding fractions.
- From the eigenfrequency list, it computes the vibrational density of states and the harmonic specific heat, then checks that the results exhibit the expected physical characteristics.
- From the radial distribution data, it locates the first two peak positions and compares them to reference values.
- From the electronic density of states, it examines the total and p‑projected density of states near the Fermi energy for the required features.

Each step is assigned a weight, and the final reward (0–1) is the weighted sum of the individual step scores. The solver must produce the specified artifact files exactly as described; reporting a number is not sufficient.
