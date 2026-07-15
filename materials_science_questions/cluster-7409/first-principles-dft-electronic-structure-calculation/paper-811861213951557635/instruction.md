# Formation energies, band gaps, and Bader charges of N/W-doped anatase TiO2 from DFT

## Problem background
Anatase TiO₂ is a wide-bandgap photocatalyst, but its absorption is limited to the UV region. Doping with nitrogen (N) and tungsten (W) has been explored to narrow the band gap and improve visible-light activity. This task reproduces the first-principles calculations that underpin the paper’s analysis: formation energies of N-, W-, and N/W-codoped anatase under different growth conditions, electronic band gap changes, and Bader charge distributions. Understanding these quantities is essential for rationalizing the synergistic effects of codoping on the material’s electronic structure and thermodynamic stability.

## Approach
We use spin-polarized density functional theory (DFT) with the generalized gradient approximation (GGA-PBE). The anatase crystal structure is modeled as a 2×2×1 supercell of 48 atoms. Substitutional doping is introduced: N replaces an O atom, W replaces a Ti atom, and for codoping an adjacent Ti–O pair is replaced by W and N respectively. The workflow includes: bulk lattice-parameter optimization, geometry relaxation of pure and doped supercells, reference total energies for O₂, N₂, bulk Ti, and bulk W to define chemical potentials under Ti-rich and O-rich conditions, calculation of formation energies via the standard defect formation formula, band gap extraction from the electronic density of states, and Bader charge decomposition. Comparison across pure, N-doped, W-doped, and N/W-codoped systems reveals the impact of doping on stability and band structure.

## Reproduction target
Produce three scored CSV files:
- formation_energies.csv: formation energies (eV) for N-, W-, and N/W-codoping under Ti-rich and O-rich growth conditions, plus the energetic preference of the adjacent N–W pair over other configurations.
- band_gaps.csv: band gaps (eV) and band gap reductions (relative to pure anatase) for pure TiO₂, N-doped, W-doped, and N/W-codoped systems.
- bader_charges.csv: Bader charges (|e|) on dopant atoms and their specified neighbors for N-doped, W-doped, and N/W-codoped systems.
These outputs correspond to the key quantitative predictions of the paper and must be derived from your own DFT calculations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader charge analysis code (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/
- SSSP Efficiency Pseudopotentials (PBE PAW): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk anatase lattice-parameter optimization
- Role: process
- Action: Perform spin-polarized DFT geometry optimization of anatase TiO2 (space group I41/amd) using GGA-PBE and a suitable plane-wave cutoff and k-point mesh to obtain optimized lattice parameters a and c.
- Evidence: `/app/outputs/step01_bulk_optimization.log`

### Step 2: Pure 2×2×1 supercell relaxation
- Role: process
- Action: Construct a 2×2×1 anatase supercell (48 atoms) using the optimized bulk lattice parameters. Relax atomic positions while keeping the cell fixed and compute the total energy E(pure).
- Evidence: `/app/outputs/step02_pure_relaxation.log`

### Step 3: N-doped supercell relaxation
- Role: process
- Action: Substitute one O atom by N in the relaxed pure supercell. Relax atomic positions and compute the total energy E(N-doped).
- Evidence: `/app/outputs/step03_Ndoped_relaxation.log`

### Step 4: W-doped supercell relaxation
- Role: process
- Action: Substitute one Ti atom by W in the relaxed pure supercell. Relax atomic positions and compute the total energy E(W-doped).
- Evidence: `/app/outputs/step04_Wdoped_relaxation.log`

### Step 5: N/W adjacent pair codoped supercell relaxation
- Role: process
- Action: Create a supercell with both N substituted for an O atom and W substituted for an adjacent Ti atom. Relax atomic positions and compute the total energy E(N/W-adjacent).
- Evidence: `/app/outputs/step05_NWcodoped_relaxation.log`

### Step 6: N–W configuration search
- Role: process
- Action: Generate several N–W substitutional arrangements with different pair distances. Relax each and compute total energies. Identify the most stable configuration (adjacent pair) and record the energy difference between it and the next best configuration.
- Evidence: `/app/outputs/step06_configuration_search.log`

### Step 7: Reference calculations for chemical potentials
- Role: process
- Action: Perform DFT calculations for O2 and N2 molecules (isolated) and for bulk Ti and bulk W metals to obtain total energies. Use these to define chemical potentials μ_O, μ_Ti, μ_N, μ_W under O-rich and Ti-rich growth conditions as described in the method.
- Evidence: `/app/outputs/step07_reference_calculations.log`

### Step 8: Formation energy analysis
- Role: scored (load-bearing)
- Action: Using the total energies from steps 02–05 and the chemical potentials from step 07, compute the formation energies for N-doped, W-doped, and N/W-codoped (adjacent pair) systems under Ti-rich and O-rich conditions using the formula E_form = E(doped) - E(pure) - μ_N - μ_W + μ_O + μ_Ti. Also report the energetic preference of the adjacent N–W pair over other configurations (energy difference from step 06). Write the results to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: doping_type (string, values: 'N', 'W', 'NW', 'NW_adjacent_preference'), condition (string, values: 'Ti-rich', 'O-rich', 'general'), formation_energy_eV (float). Contains six rows for N/W/NW under Ti-rich/O-rich, plus a row for the adjacent-pair preference.
- Scoring: scored by hidden verifier

### Step 9: Band gap analysis
- Role: scored
- Action: For pure TiO2 and the N-doped, W-doped, and N/W-codoped relaxed supercells, compute the electronic band gap as the difference between the valence band maximum and conduction band minimum. Report the band gap in eV and the reduction relative to pure TiO2. Write to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: system (string, values: 'pure', 'N-doped', 'W-doped', 'NW-doped'), band_gap_eV (float), band_gap_reduction_eV (float). The reduction is defined as pure band gap minus doped band gap.
- Scoring: scored by hidden verifier

### Step 10: Bader charge analysis
- Role: scored
- Action: Perform Bader charge decomposition on the relaxed N-doped, W-doped, and N/W-codoped supercells. Report charges on the dopant atoms and their specified neighbors (N, W, and adjacent O and Ti atoms) as listed in the published table. Write to bader_charges.csv.
- Output file: `/app/outputs/bader_charges.csv`
- Format: csv
- Contract: CSV with columns: system (string, values: 'N-doped', 'W-doped', 'NW-doped'), atom (string, e.g., 'N', 'W', 'O1', 'Ti1'), bader_charge_e (float). Includes all atoms for which values are reported.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/band_gaps.csv`
- `/app/outputs/bader_charges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies of N, W, and N/W doping in anatase under Ti-rich and O-rich conditions, plus the adjacent pair preference energy.
- schema:
  - `type`: table
  - `required_columns`: `doping_type`, `condition`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gaps and band-gap reductions for pure, N-doped, W-doped, and NW-doped anatase.
- schema:
  - `type`: table
  - `required_columns`: `system`, `band_gap_eV`, `band_gap_reduction_eV`
  - `units`:
    - `band_gap_eV`: eV
    - `band_gap_reduction_eV`: eV

### bader_charges.csv
- path: `/app/outputs/bader_charges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bader charges on dopant and neighboring atoms for N-doped, W-doped, and NW-doped anatase.
- schema:
  - `type`: table
  - `required_columns`: `system`, `atom`, `bader_charge_e`
  - `units`:
    - `bader_charge_e`: e

Notes: All output values are numerical and compared to reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_type",
          "condition",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energies of N, W, and N/W doping in anatase under Ti-rich and O-rich conditions, plus the adjacent pair preference energy."
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "band_gap_eV",
          "band_gap_reduction_eV"
        ],
        "units": {
          "band_gap_eV": "eV",
          "band_gap_reduction_eV": "eV"
        }
      },
      "description": "Band gaps and band-gap reductions for pure, N-doped, W-doped, and NW-doped anatase."
    },
    {
      "file": "bader_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "atom",
          "bader_charge_e"
        ],
        "units": {
          "bader_charge_e": "e"
        }
      },
      "description": "Bader charges on dopant and neighboring atoms for N-doped, W-doped, and NW-doped anatase."
    }
  ],
  "notes": "All output values are numerical and compared to reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each of your three output files by comparing your reported values to hidden reference values. The verifier checks structural properties (correct columns and row labels) and numerical accuracy within domain-appropriate tolerances. Each artifact carries a weight, and the final reward is the weighted combination of per-artifact scores. Reporting accurate numbers requires genuinely executing the DFT workflow; no pre-computed data or answers are provided in the task. The verifier will not re-run DFT itself.
