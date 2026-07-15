# Vacancy-vacancy binding energy in copper using Morse potential

## Problem background
Point defects such as vacancies govern many solid‑state processes, including diffusion, annealing, and radiation damage. The interaction between vacancies can lead to bound pairs (divacancies), and the binding energy as a function of separation determines the stability of these configurations. An accurate calculation of the binding energy in copper is essential for understanding vacancy‑mediated phenomena. This task reproduces the static‑lattice computation of the vacancy‑vacancy binding energy using a Morse potential, as originally studied to assess the relative stability of different vacancy‑pair separations.

## Approach
The calculation uses a Morse pair potential with parameters derived from bulk copper: α = 1.3588 Å⁻¹, β = 49.11, D = 0.3429 eV. We model the lattice as a 20×20×20 face‑centred‑cubic crystal. Four vacancy separations are considered: first‑, second‑, fourth‑, and eighth‑nearest neighbours. For each separation, the direct pair interaction energy E_NN is obtained by evaluating the Morse potential at the corresponding interatomic distance. The relaxation energy E_DR is computed by grouping the atoms nearest the vacancy pair into symmetry‑based sets and iteratively displacing each set radially toward/away from each vacancy. The lattice energy is evaluated using a translated Morse summation at each iteration; convergence yields the relaxed configuration. E_DR is the energy difference between the unrelaxed and relaxed lattices. The isolated‑vacancy relaxation energy E_VR = 0.56 eV is provided. The binding energy then follows from E_B = E_NN + E_DR − 2·E_VR. This procedure is repeated for all four separations, and the resulting binding energies are written to a CSV file.

## Reproduction target
Reproduce the binding energy E_B for each of the four vacancy‑pair separations using the Morse potential model and the iterative relaxation procedure described above. Implement the lattice construction, the relaxation, and the energy calculation. Write the output file `/app/outputs/binding_energies.csv` containing two columns: `separation_rank` (integer 1, 2, 4, or 8) and `binding_energy_ev` (float, in eV). The verifier will check the quantitative accuracy of the first‑nearest‑neighbour binding energy as well as a required trend across the separations.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Lattice setup and neighbour grouping
- Role: process
- Action: Construct a 20×20×20 FCC copper lattice and select four vacancy-pair separations (first-, second-, fourth-, eighth-nearest neighbours). For each separation, group the first- and second-nearest-neighbour atoms into symmetry-based sets for later relaxation.
- Evidence: `/app/outputs/lattice_setup_summary.json`

### Step 2: Compute pair interaction energy E_NN
- Role: process
- Action: For each vacancy-pair separation, evaluate the Morse pair potential between two atoms at the same separation to obtain E_NN, using the Morse parameters α=1.3588 Å⁻¹, β=49.11, D=0.3429 eV.
- Evidence: none

### Step 3: Iterative relaxation and E_DR calculation
- Role: process
- Action: For each separation, perform the iterative grouped-set displacement relaxation: displace atom sets radially toward/away from each vacancy, evaluate the lattice energy using the translated Morse summation, and converge to the relaxed configuration. Compute the relaxation energy E_DR as the energy difference between the unrelaxed and relaxed configurations.
- Evidence: `/app/outputs/relaxed_coordinates.csv`

### Step 4: Binding energy calculation and output
- Role: scored (load-bearing)
- Action: Combine E_NN, E_DR, and the known isolated-vacancy relaxation energy E_VR = 0.56 eV using E_B = E_NN + E_DR – 2·E_VR for each of the four separations. Write a CSV file with separation_rank (1,2,4,8) and the corresponding binding energy (in eV).
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with two columns: separation_rank (int, allowed values 1,2,4,8) and binding_energy_ev (float, positive).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Binding energy for each separation. The verifier will compare the binding_energy_ev for separation_rank=1 against a hidden reference value using a specified absolute tolerance, and verify a required trend across the four separations.
- schema:
  - `type`: table
  - `required_columns`: `separation_rank`, `binding_energy_ev`
  - `units`:
    - `binding_energy_ev`: eV

Notes: The hidden checker compares the binding_energy_ev for separation_rank=1 to a paper-reported gold value using an absolute tolerance and verifies a required trend across the separations. No public gold value is given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "separation_rank",
          "binding_energy_ev"
        ],
        "units": {
          "binding_energy_ev": "eV"
        }
      },
      "description": "Binding energy for each separation. The verifier will compare the binding_energy_ev for separation_rank=1 against a hidden reference value using a specified absolute tolerance, and verify a required trend across the four separations."
    }
  ],
  "notes": "The hidden checker compares the binding_energy_ev for separation_rank=1 to a paper-reported gold value using an absolute tolerance and verifies a required trend across the separations. No public gold value is given."
}
```

## How you are scored
The hidden verifier reads your `binding_energies.csv`. It performs two checks: (1) a point‑value check that compares the `binding_energy_ev` for `separation_rank=1` against a hidden reference value with an absolute tolerance; (2) a trend check that verifies the relative ordering of the binding energies across the four separations. The majority of the reward is tied to the point‑value match; the remainder comes from correct trend ordering. The verifier outputs a single score between 0 and 1.
