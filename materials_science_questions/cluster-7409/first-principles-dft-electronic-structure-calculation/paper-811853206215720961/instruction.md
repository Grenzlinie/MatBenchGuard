# Electronic structure of Sr2MgSi2O7:Eu2+ via DFT

## Problem background
Sr2MgSi2O7:Eu2+ is a persistent luminescence material. Understanding its electronic structure — particularly the host band gap and the energy position of the Eu2+ 4f ground state relative to the valence and conduction band edges — is essential for explaining the luminescence mechanism. Density functional theory (DFT) can provide these quantities, but the calculated position of the strongly correlated 4f electrons depends sensitively on the treatment of Coulomb interactions. The goal is to compute the band gap of the pure host and to determine how the Eu2+ 4f energy shifts with the Hubbard U correction.

## Approach
The electronic structure is studied using periodic DFT. First, a pure Sr2MgSi2O7 unit cell is modelled, and a generalized gradient approximation (PBE) calculation is performed to obtain the density of states and extract the band gap (conduction band minimum minus valence band maximum). Second, a doped supercell is constructed by substituting one Sr by Eu. Because Eu 4f electrons are strongly correlated, a GGA+U approach with spin-orbit coupling is applied. The Hubbard U parameter is varied over the range 4.35–7.62 eV while keeping the exchange parameter J fixed at 0.68 eV. For each U value, the projected density of states is computed, and the energy of the occupied majority-spin Eu 4f peak is identified and measured relative to the host valence band maximum (VBM) and conduction band minimum (CBM). The results are then collected to characterise the trend in the 4f level position as a function of U.

## Reproduction target
Calculate the band gap of pure Sr2MgSi2O7 using GGA (PBE) and write the value to `/app/outputs/band_gap.txt`. For the Eu-doped supercell, run GGA+U calculations with spin-orbit coupling for the set of Hubbard U values provided in `assets/u_values.txt` (J = 0.68 eV). For each U, determine the energy of the occupied majority-spin Eu 4f ground state relative to the host VBM and CBM, and output the results as a CSV table at `/app/outputs/ef_vs_U.csv` with columns `U`, `Energy_to_VBM`, `Energy_to_CBM` (all in eV).

## Assets

- Sr2MgSi2O7 crystal structure reference (Kimata 1983): 10.1524/zkri.1983.163.3-4.295
- `assets/u_values.txt`: list of Hubbard U values (one per line) to be used in Step 3.

## Workflow steps

### Step 1: Build crystal structure models
- Role: process
- Action: Construct unit cell of pure Sr2MgSi2O7 (tetragonal, P-42_1m, a=7.996 Å, c=5.152 Å) and a 1×1×1 supercell with one Sr substituted by Eu. Generate DFT input files.
- Evidence: none

### Step 2: Compute pure host band gap
- Role: scored
- Action: Perform a GGA (PBE) calculation on the pure Sr2MgSi2O7 unit cell. Determine the band gap (VBM to CBM) from the density of states and record the value.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: Single floating-point number in eV.
- Scoring: scored by hidden verifier

### Step 3: Eu 4f energy position vs Hubbard U
- Role: scored (load-bearing)
- Action: For the Eu-doped supercell, run GGA+U calculations with spin-orbit coupling for the Hubbard U values listed in `assets/u_values.txt` (J=0.68 eV). For each U, extract the occupied Eu2+ 4f peak in the majority-spin channel and compute its energy relative to the host VBM and CBM.
- Output file: `/app/outputs/ef_vs_U.csv`
- Format: csv
- Contract: CSV with columns: U (float, eV), Energy_to_VBM (float, eV), Energy_to_CBM (float, eV). One row per U value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/ef_vs_U.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: The GGA-computed band gap of pure Sr2MgSi2O7. Compared to a hidden reference value with tolerance.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the calculated band gap in eV.

### ef_vs_U.csv
- path: `/app/outputs/ef_vs_U.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file mapping Hubbard U to the energy of the occupied Eu2+ 4f ground state relative to the valence band maximum (VBM) and conduction band minimum (CBM). The linear trend and slope are recomputed and compared to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `U`, `Energy_to_VBM`, `Energy_to_CBM`
  - `units`:
    - `U`: eV
    - `Energy_to_VBM`: eV
    - `Energy_to_CBM`: eV

Notes: Band gap compared to a hidden reference value; CSV checked for monotonic trend of Energy_to_VBM with U and slope compared to hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the calculated band gap in eV."
      },
      "description": "The GGA-computed band gap of pure Sr2MgSi2O7. Compared to a hidden reference value with tolerance."
    },
    {
      "file": "ef_vs_U.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "Energy_to_VBM",
          "Energy_to_CBM"
        ],
        "units": {
          "U": "eV",
          "Energy_to_VBM": "eV",
          "Energy_to_CBM": "eV"
        }
      },
      "description": "CSV file mapping Hubbard U to the energy of the occupied Eu2+ 4f ground state relative to the valence band maximum (VBM) and conduction band minimum (CBM). The linear trend and slope are recomputed and compared to a hidden reference."
    }
  ],
  "notes": "Band gap compared to a hidden reference value; CSV checked for monotonic trend of Energy_to_VBM with U and slope compared to hidden reference."
}
```

## How you are scored
A hidden verifier will independently inspect every output file you produce under `/app/outputs`. The band gap value you report in `band_gap.txt` will be compared to a hidden reference, and the CSV table `ef_vs_U.csv` will be checked for correct format and for the physical trend in the data (for instance, how the Eu 4f energy changes with U). Your final score is a weighted combination of these checks; a solution that performs the required calculations and captures the essential behaviour will earn high marks. Simply writing the paper's reported numbers without performing the calculations is not sufficient to pass the hidden checks.
