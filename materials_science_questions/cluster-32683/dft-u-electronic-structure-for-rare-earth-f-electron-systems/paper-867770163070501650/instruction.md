# LDA+DMFT total energy vs volume for cerium and energy difference at 400 K

## Problem background
Cerium metal undergoes a first‑order isostructural transition between a low‑volume α phase and a high‑volume γ phase, ending at a critical point around 600 K. The mechanism driving the transition has been heavily debated: one view attributes it to an energy‑driven electronic collapse (Mott or Kondo volume collapse), while another argues that the large spin‑fluctuation entropy of the γ phase dominates the free‑energy balance. Clarifying these contributions requires a reliable determination of the total internal energy as a function of unit‑cell volume and temperature. This task provides such data by performing LDA+DMFT calculations that focus on the electronic energy landscape of fcc cerium.

## Approach
The workflow employs a combination of density‑functional theory in the local‑density approximation (LDA) and dynamical mean‑field theory (DMFT). The LDA part is handled by the open‑source Quantum ESPRESSO package, while DMFT is implemented with the TRIQS library and the DFTTools interface. A Hirsch‑Fye quantum Monte Carlo impurity solver is used to solve the many‑body problem on the correlated f‑orbitals. The valence states include the semicore orbitals 5s, 5p, 6s, 6p, 5d and the correlated 4f orbitals; a Hubbard U parameter of 6 eV is applied and spin‑orbit coupling is neglected. For a set of fixed unit‑cell volumes (28.0–33.0 Å³) and three temperatures (400 K, 800 K, 1600 K), fully self‑consistent DMFT calculations are performed. The total internal energy per formula unit is extracted from the DMFT total‑energy expression, which corrects the DFT energy for double‑counted interaction contributions. The resulting energy‑volume curves are then compiled to enable analysis of the temperature‑dependent changes in curvature and the energy separation between the two characteristic volumes that approximately correspond to the α and γ phases at 400 K. The experimental thermodynamic analysis (e.g. use of the Clausius‑Clapeyron relation) is outside the scope of this computational reproduction.

## Reproduction target
Produce two output files. The first, `E_vs_V_all_T.csv`, is a comma‑separated table with columns `Temperature_K` (integer), `Volume_ang3` (floating point), and `TotalEnergy_eV` (floating point). It must contain one row for every combination of the three temperatures (400, 800, 1600 K) and the eleven volumes (28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0 Å³). No index or extra columns. The second, `Delta_E_400K.txt`, is a plain‑text file with a single line giving the energy difference ΔE = E(V=32.0 Å³) − E(V=28.5 Å³) at 400 K, expressed in eV (e.g. `0.0135`). These artifacts allow independent verification of the electronic energy differences that underlie the thermodynamic competition between the two phases.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- TRIQS library: https://triqs.github.io/triqs/latest/install.html
- DFTTools interface: https://triqs.github.io/dft_tools/latest/
- Cerium PAW pseudopotential (PSL 1.0.0): https://pseudopotentials.quantum-espresso.org/upf_files/Ce.pbe-n-kjpaw_psl.1.0.0.UPF

## Workflow steps

### Step 1: LDA+DMFT total energy calculations
- Role: process
- Action: For each volume V = 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0 Å³ and each temperature T = 400 K, 800 K, 1600 K, perform a self‑consistent LDA+DMFT calculation using Quantum ESPRESSO + TRIQS/DFTTools with a Hirsch‑Fye quantum Monte Carlo impurity solver. Use Hubbard U = 6 eV, neglect spin‑orbit coupling, and retain valence states 5s,5p,6s,6p,5d,4f. Compute the total internal energy per formula unit using the DMFT energy expression (removing double‑counted contributions). Store the energies temporarily.
- Evidence: `/app/outputs/dmft_runs.log`

### Step 2: Compile energy vs volume data
- Role: scored
- Action: Collect the computed total energies from all (volume, temperature) runs and write a CSV file with one row per data point.
- Output file: `/app/outputs/E_vs_V_all_T.csv`
- Format: csv
- Contract: CSV with exactly three columns: Temperature_K (int, one of 400,800,1600), Volume_ang3 (float, one of the listed volumes), TotalEnergy_eV (float, total energy in eV). No index, no extra columns.
- Scoring: scored by hidden verifier

### Step 3: Extract ΔE at 400 K
- Role: scored (load-bearing)
- Action: From the compiled energy data, compute the energy difference ΔE = E(V=32.0 Å³) – E(V=28.5 Å³) at T=400 K. Write this single number to a text file.
- Output file: `/app/outputs/Delta_E_400K.txt`
- Format: txt
- Contract: A single line containing a float value in eV, e.g., 0.0135.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/E_vs_V_all_T.csv`
- `/app/outputs/Delta_E_400K.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### E_vs_V_all_T.csv
- path: `/app/outputs/E_vs_V_all_T.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Tabulated LDA+DMFT total energies for cerium at multiple volumes and temperatures; checked for decreasing curvature as temperature is lowered.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Volume_ang3`, `TotalEnergy_eV`
  - `units`:
    - `Temperature_K`: K
    - `Volume_ang3`: angstrom^3
    - `TotalEnergy_eV`: eV

### Delta_E_400K.txt
- path: `/app/outputs/Delta_E_400K.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy difference ΔE = E(γ)−E(α) at 400 K, compared to the paper‑reported value within a small tolerance.
- schema:
  - `type`: text
  - `required`: `numeric value in eV`
  - `units`: eV

Notes: The DMFT calculations are computationally heavy; the solving agent may need external compute resources. Only the final aggregated data and ΔE are scored; intermediate DMFT outputs are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "E_vs_V_all_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Volume_ang3",
          "TotalEnergy_eV"
        ],
        "units": {
          "Temperature_K": "K",
          "Volume_ang3": "angstrom^3",
          "TotalEnergy_eV": "eV"
        }
      },
      "description": "Tabulated LDA+DMFT total energies for cerium at multiple volumes and temperatures; checked for decreasing curvature as temperature is lowered."
    },
    {
      "file": "Delta_E_400K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": [
          "numeric value in eV"
        ],
        "units": "eV"
      },
      "description": "Energy difference ΔE = E(γ)−E(α) at 400 K, compared to the paper‑reported value within a small tolerance."
    }
  ],
  "notes": "The DMFT calculations are computationally heavy; the solving agent may need external compute resources. Only the final aggregated data and ΔE are scored; intermediate DMFT outputs are not required."
}
```

## How you are scored
A hidden verifier reads `E_vs_V_all_T.csv` and `Delta_E_400K.txt`. It first extracts the energy‑volume data and checks that the curvature of the total energy versus volume curves decreases as temperature is lowered (the curve at 400 K appears flatter than at 1600 K) without developing a region of negative curvature. It then reads the ΔE value from `Delta_E_400K.txt` and compares it to an independent reference determination within a tolerance. The overall reward (a float between 0 and 1) is a weighted combination of these checks, with the structural trend and the energy difference carrying the largest weights. The files must reflect genuine LDA+DMFT calculations; merely quoting a known value will not pass the structural audit.
