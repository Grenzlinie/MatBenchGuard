# DFT-LSDA magnetic ground state of the UTAl compound series

## Problem background
The UTAl intermetallic compounds (T = Fe, Co, Ni, Ru, Rh, Ir, Pt) crystallize in the hexagonal ZrNiAl structure and exhibit a progression from paramagnetic to magnetically ordered behavior. Understanding the origin of this magnetic transition in terms of the electronic band filling and the Stoner criterion is a key question in actinide magnetism. This task aims to determine, from first-principles scalar-relativistic DFT calculations, which of these compounds have a magnetic ground state and to quantify the spin magnetic moment of the ferromagnetic state.

## Approach
The magnetic ground state is investigated using density-functional theory in the local spin-density approximation (LSDA) with scalar-relativistic effects. For each of the seven compounds, two self-consistent total-energy calculations are performed: a non-spin-polarized (non-magnetic) calculation, and a spin-polarized (ferromagnetic) calculation where the spin-up and spin-down densities are allowed to differ. Comparing the total energies of these two configurations reveals which one is more stable; a lower energy for the spin-polarized state indicates a magnetic ground state. Additionally, the total spin magnetic moment from the spin-polarized calculation provides a complementary measure of magnetism. The calculations cover the entire isostructural series so that the trend of magnetic stability across the transition-metal series can be assessed. Spin-orbit coupling and orbital polarization calculations are not included because the paper's orbital moments were obtained with a Racah parameter E3 orbital-polarization term that is not implemented in standard open-source DFT codes (Quantum ESPRESSO, ELK, ABINIT). Furthermore, the paper provides quantitative orbital moment values only for URhAl, making it impossible to construct a reliable scored metric for the entire compound series. Consequently, this reproduction focuses on the scalar-relativistic spin moments and magnetic ground-state classification, which are the paper's primary quantitative findings.

## Reproduction target
Perform scalar-relativistic LSDA calculations for all seven UTAl compounds. For each compound, run a non-spin-polarized SCF calculation and a spin-polarized (ferromagnetic) SCF calculation. Extract the total energy per formula unit (in eV) for each state and the total spin magnetic moment (in μB per formula unit) from the spin-polarized calculation. Collect the results into a CSV file named magnetic_results.csv with exactly four columns: compound (string), E_nonmag (float), E_spin (float), total_spin_moment (float). The hidden verifier will recompute the energy difference ΔE = E_spin - E_nonmag and use it together with the spin moment to decide whether each compound is correctly classified as magnetic or non-magnetic, according to pre-defined criteria based on the known physical behaviour.

## Assets

- UTAl crystal structures (hexagonal ZrNiAl type): Obtain from literature (e.g., Sechovský and Havela, 'Ferromagnetic Materials' vol. 4, 1988) or from public crystallographic databases (ICSD, COD).
- Open-source DFT code with LSDA: Quantum ESPRESSO (https://www.quantum-espresso.org/), ELK (http://elk.sourceforge.net/), or ABINIT.

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Obtain the hexagonal ZrNiAl crystal structures for all seven UTAl compounds (UFeAl, UCoAl, UNiAl, URuAl, URhAl, UIrAl, UPtAl) from public databases or literature, and prepare input files for scalar-relativistic DFT-LSDA calculations (non-spin-polarized and spin-polarized).
- Evidence: none

### Step 2: Run DFT-LSDA calculations and collect magnetic properties
- Role: scored (load-bearing)
- Action: For each compound, run a non-spin-polarized SCF calculation and a spin-polarized (ferromagnetic) SCF calculation using an open-source DFT code. Extract the total energy per formula unit (in eV) for each state and the total spin magnetic moment (in μB per formula unit) from the spin-polarized calculation. Combine results into a CSV file.
- Output file: `/app/outputs/magnetic_results.csv`
- Format: csv
- Contract: Columns: compound (string), E_nonmag (float, eV per formula unit), E_spin (float, eV per formula unit), total_spin_moment (float, μB per formula unit).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_results.csv
- path: `/app/outputs/magnetic_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw total energies and spin magnetic moment from DFT-LSDA calculations; the checker recomputes ΔE = E_spin - E_nonmag and classifies the magnetic ground state.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `E_nonmag`, `E_spin`, `total_spin_moment`
  - `units`:
    - `E_nonmag`: eV per f.u.
    - `E_spin`: eV per f.u.
    - `total_spin_moment`: μB per f.u.

Notes: Spin-orbit coupling, orbital polarization, and metamagnetic state search are excluded from this reproduction scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "E_nonmag",
          "E_spin",
          "total_spin_moment"
        ],
        "units": {
          "E_nonmag": "eV per f.u.",
          "E_spin": "eV per f.u.",
          "total_spin_moment": "μB per f.u."
        }
      },
      "description": "Raw total energies and spin magnetic moment from DFT-LSDA calculations; the checker recomputes ΔE = E_spin - E_nonmag and classifies the magnetic ground state."
    }
  ],
  "notes": "Spin-orbit coupling, orbital polarization, and metamagnetic state search are excluded from this reproduction scope."
}
```

## How you are scored
A hidden verifier reads your submitted magnetic_results.csv. It computes ΔE = E_spin - E_nonmag for every compound and applies internal threshold conditions on ΔE and total_spin_moment to classify each compound as magnetic or non-magnetic. Your score is the fraction of the seven compounds that are classified correctly according to those hidden criteria. The reward is monotonic: meeting or exceeding the expected trend yields full credit, and credit only decreases if the predicted magnetic/non-magnetic behaviour deviates further from the expected physical outcome. Reporting a number from memory without running the DFT calculations is unlikely to satisfy the thresholds, which are tailored to genuine LSDA results.
