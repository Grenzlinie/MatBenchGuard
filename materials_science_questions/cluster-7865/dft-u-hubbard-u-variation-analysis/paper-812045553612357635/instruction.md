# DFT+U Electronic Structure and Magnetism of CeRu2Si2

## Problem background
CeRu2Si2 is a heavy fermion compound that exhibits a nonmagnetic ground state and a metamagnetic transition under an applied magnetic field. Standard density‑functional calculations in the local‑density approximation (LDA) fail to capture the strong orbital polarization of the 4f electrons. The LDA+U method, which adds a Hubbard U correction to treat strong electron‑electron correlations, combined with spin‑orbit coupling, is a more advanced approach that can be applied to investigate the electronic structure of this material, including the density of states near the Fermi level and the magnetic response.

## Approach
Perform first‑principles DFT calculations using the LDA+U framework with spin‑orbit coupling. Two self‑consistent calculations are required:
- A nonmagnetic calculation to obtain the ground‑state electronic structure and density of states.
- A spin‑polarized calculation with an external magnetic field of 5 T applied along the crystallographic c‑axis, to obtain the field‑induced 4f magnetic moment.

The Hubbard U parameter is set to 0.4 Ry. The initial density matrix is chosen to be occupied in the |j=5/2, j_z=±5/2> state; the density matrix is then determined self‑consistently together with the charge density. The crystal structure is body‑centered tetragonal (space group I4/mmm) with experimental lattice parameters from Boucherle et al. (2001) or from the ICSD. Any open‑source DFT code that supports LDA+U and spin‑orbit coupling (e.g., Elk, Quantum ESPRESSO) may be used.

## Reproduction target
Produce three outputs:
1. A JSON file (`nonmagnetic_4f_weights.json`) containing the projected occupation weights of the Ce 4f orbitals for the three Kramers doublets (j_z=±5/2, ±3/2, ±1/2) obtained from the nonmagnetic LDA+U calculation.
2. A CSV file (`dos_data.csv`) with the total density of states in the energy range –1.0 eV to +1.0 eV relative to the Fermi level, at a resolution sufficient to resolve peak structures.
3. A plain‑text file (`magnetic_moment_5T.txt`) containing the total 4f magnetic moment (in μ_B) per Ce atom from the magnetic calculation at H=5 T.

The computed quantities are to be obtained by following the described workflow and will be evaluated by a hidden verifier against reference values that represent a correct implementation of the approach.

Note: The paper also reports Fermi surfaces and angular dependence of de Haas–van Alphen (dHvA) frequencies as co-headline results. These are omitted from the scored targets because the exact numerical frequency values are not stated in the source paper (the data are presented only as angular dependence figures), making it impossible to define objective hidden gold values for verification.

## Assets

- Crystal structure of CeRu2Si2: 10.1088/0953-8984/13/48/307
- Open-source DFT code with LDA+U and spin-orbit coupling: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Crystal structure preparation
- Role: process
- Action: Obtain the crystal structure of CeRu2Si2 (space group I4/mmm) from the experimental data (Boucherle et al. 2001 or ICSD) and prepare a geometry input file for the DFT code.
- Evidence: none

### Step 2: LDA+U nonmagnetic self-consistent calculation
- Role: process
- Action: Perform a self-consistent LDA+U calculation for nonmagnetic CeRu2Si2 with spin-orbit coupling, using Hubbard U=0.4 Ry, initial density matrix occupied in the |j=5/2, j_z=±5/2> state, and the prepared crystal structure. Run until charge/spin density convergence.
- Evidence: `/app/outputs/convergence_nonmag.log`

### Step 3: Extract 4f occupation weights
- Role: scored (load-bearing)
- Action: From the self-consistent LDA+U nonmagnetic density matrix, extract the projected occupation weights of the 4f orbitals for the three Kramers doublets: j_z=±5/2, ±3/2, ±1/2. Output the values as a JSON file.
- Output file: `/app/outputs/nonmagnetic_4f_weights.json`
- Format: json
- Contract: JSON object with keys 'jz_5_2', 'jz_3_2', 'jz_1_2' containing floating-point numbers.
- Scoring: scored by hidden verifier

### Step 4: Compute total density of states (nonmagnetic)
- Role: scored
- Action: Using the converged LDA+U nonmagnetic eigenvalues and Fermi level, compute the total density of states (DOS) in the energy range -1.0 to +1.0 eV relative to E_F. Output a CSV file with columns 'Energy_eV' and 'Total_DOS'.
- Output file: `/app/outputs/dos_data.csv`
- Format: csv
- Contract: CSV with columns 'Energy_eV' (float) and 'Total_DOS' (float, arbitrary units). At least 200 data points covering [-1.0, 1.0] eV.
- Scoring: scored by hidden verifier

### Step 5: LDA+U magnetic calculation under H=5 T
- Role: process
- Action: Perform a spin-polarized LDA+U calculation for CeRu2Si2 with an applied magnetic field H=5 T along the crystallographic c-axis, including spin-orbit coupling. Start from the nonmagnetic converged charge density or a suitable restart, and converge to a self-consistent magnetic solution.
- Evidence: `/app/outputs/convergence_mag_5T.log`

### Step 6: Extract 4f magnetic moment
- Role: scored (load-bearing)
- Action: From the magnetic LDA+U self-consistent calculation, extract the total 4f magnetic moment (in μ_B) per Ce atom. Write the value to a plain text file.
- Output file: `/app/outputs/magnetic_moment_5T.txt`
- Format: txt
- Contract: A single floating-point number (in μ_B) representing the total 4f magnetic moment of Ce at H=5 T.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nonmagnetic_4f_weights.json`
- `/app/outputs/dos_data.csv`
- `/app/outputs/magnetic_moment_5T.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nonmagnetic_4f_weights.json
- path: `/app/outputs/nonmagnetic_4f_weights.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Occupied weights for the three Kramers doublets of the j=5/2 manifold.
- schema:
  - `type`: object
  - `required`:
    - `jz_5_2`: number
    - `jz_3_2`: number
    - `jz_1_2`: number

### dos_data.csv
- path: `/app/outputs/dos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states near the Fermi level, used to verify the double-peak anomaly.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `Total_DOS`
  - `units`:
    - `Energy_eV`: eV
    - `Total_DOS`: arbitrary units

### magnetic_moment_5T.txt
- path: `/app/outputs/magnetic_moment_5T.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Total 4f magnetic moment per Ce atom under H=5 T.
- schema:
  - `type`: text
  - `description`: Single floating-point number in μB.

Notes: The exact_match outputs (4f weights, magnetic moment) are compared to hidden paper-reported values with appropriate tolerance. The DOS output is audited for the Fermi-level double-peak feature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nonmagnetic_4f_weights.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "jz_5_2": "number",
          "jz_3_2": "number",
          "jz_1_2": "number"
        }
      },
      "description": "Occupied weights for the three Kramers doublets of the j=5/2 manifold."
    },
    {
      "file": "dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "Total_DOS"
        ],
        "units": {
          "Energy_eV": "eV",
          "Total_DOS": "arbitrary units"
        }
      },
      "description": "Total density of states near the Fermi level, used to verify the double-peak anomaly."
    },
    {
      "file": "magnetic_moment_5T.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number in μB."
      },
      "description": "Total 4f magnetic moment per Ce atom under H=5 T."
    }
  ],
  "notes": "The exact_match outputs (4f weights, magnetic moment) are compared to hidden paper-reported values with appropriate tolerance. The DOS output is audited for the Fermi-level double-peak feature."
}
```

## How you are scored
Your submitted artifacts are evaluated independently by a hidden verifier. For the 4f weights file, each reported occupation number is compared to a hidden gold value with an allowed tolerance. For the density‑of‑states file, the verifier performs a structural audit to check that the Fermi level lies between two peaks with a local minimum. For the magnetic moment file, the reported value is compared to a hidden reference value with an allowed tolerance. Each artifact carries a specific weight, and the final score is a weighted combination. All checks must pass for full credit. The exact gold values, tolerances, and audit criteria are not disclosed; the goal is to reward an accurate reproduction of the target electronic structure.
