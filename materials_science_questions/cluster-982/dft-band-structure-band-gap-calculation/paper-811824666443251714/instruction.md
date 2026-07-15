# Equilibrium properties and phonon softening in zincblende HgSe and HgTe from LDA DFT

## Problem background
The mercury chalcogenides HgSe and HgTe crystallize in the zincblende structure at ambient conditions. Under moderate compression they exhibit a unique "hidden" phase transition to an orthorhombic $C222_1$ structure not observed in other II-VI compounds. The transition is believed to be driven by a pressure-induced softening of the transverse-acoustic (TA) phonon mode at the Brillouin zone boundary $X$ point. Reproducing the equilibrium properties and phonon frequencies can validate this mechanism.

## Approach
Use first-principles density functional theory (DFT) with the local density approximation (LDA) and a plane-wave pseudopotential code. Compute total energies for zincblende HgSe and HgTe over a range of unit-cell volumes. Fit a Murnaghan-type equation of state to obtain zero-pressure equilibrium volume $V_0$ and bulk modulus $B_0$. Then compute phonon frequencies using the finite-displacement method in a supercell at two volumes: the zero-pressure equilibrium volume and a smaller volume corresponding to approximately 3 GPa of compression. Extract the transverse-optic (TO) mode at $\Gamma$ and the TA mode at $X$; comparing them between the two conditions reveals whether the TA branch softens as pressure is applied.

## Reproduction target
Produce two comma-separated value (CSV) files in `/app/outputs`:

- `equilibrium_properties.csv` with columns `compound`, `V0_pfu_AA3` (Å³ per formula unit), `B0_GPa` (GPa) for HgSe and HgTe.
- `phonon_frequencies.csv` with columns `compound`, `pressure_condition` (e.g., `0_GPa` or `3_GPa`), `frequency_TO_Gamma_THz` (THz), `frequency_TA_X_THz` (THz) for both compounds at each pressure condition.

The goal is to compute these quantities from the DFT workflow. The verifier will check that the equilibrium parameters and the phonon frequencies are consistent with the expected softening trend.

## Assets

- Open-source plane-wave DFT code (Quantum ESPRESSO): https://www.quantum-espresso.org/
- LDA pseudopotentials (e.g., SSSP precision library or GBRV): https://www.materialscloud.org/discover/sssp/table/precision
- Phonopy package: phonopy
- Zincblende crystal structures for HgSe and HgTe

## Workflow steps

### Step 1: DFT parameter convergence
- Role: process
- Action: Determine a plane-wave kinetic-energy cutoff and Monkorst-Pack k-point grid that achieve total-energy convergence of about 1 meV per atom for zincblende HgSe and HgTe. Record the chosen parameters.
- Evidence: `/app/outputs/convergence_report.txt`

### Step 2: LDA total-energy vs volume calculations
- Role: process
- Action: For zincblende HgSe and HgTe, compute the total energy per formula unit at a set of volumes spanning the equilibrium region using the converged LDA parameters. Save the volume–energy pairs to CSV files.
- Evidence: `/app/outputs/ev_data_HgSe.csv, ev_data_HgTe.csv`

### Step 3: Equilibrium properties from Murnaghan EOS fit
- Role: scored
- Action: Fit a Murnaghan-type equation of state to the energy-volume data for each compound. Save the extracted zero-pressure equilibrium volume V0 (Å³ per formula unit) and bulk modulus B0 (GPa) to equilibrium_properties.csv.
- Output file: `/app/outputs/equilibrium_properties.csv`
- Format: csv
- Contract: Columns: compound (string), V0_pfu_AA3 (float), B0_GPa (float)
- Scoring: scored by hidden verifier

### Step 4: Phonon supercell calculations
- Role: process
- Action: For zincblende HgSe and HgTe, at the zero-pressure equilibrium volume and at a compressed volume corresponding to ~3 GPa, compute force constants using the finite-displacement method in a supercell (e.g., 4×4×4). Use the converged LDA parameters. Output the resulting phonon data (e.g., band.yaml or force constants).
- Evidence: `/app/outputs/phonon_HgSe_0GPa.yaml, phonon_HgSe_3GPa.yaml, phonon_HgTe_0GPa.yaml, phonon_HgTe_3GPa.yaml`

### Step 5: Phonon frequencies at Γ and X points
- Role: scored (load-bearing)
- Action: From the computed phonon data, extract the transverse-optic (TO) frequency at the Γ point and the transverse-acoustic (TA) frequency at the X point for each compound and pressure condition. Save to phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: compound (string), pressure_condition (string), frequency_TO_Gamma_THz (float), frequency_TA_X_THz (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_properties.csv`
- `/app/outputs/phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_properties.csv
- path: `/app/outputs/equilibrium_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Zero-pressure equilibrium volumes and bulk moduli for zincblende HgSe and HgTe obtained from a Murnaghan EOS fit to LDA total-energy data.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `V0_pfu_AA3`, `B0_GPa`
  - `units`:
    - `V0_pfu_AA3`: Å³ per formula unit
    - `B0_GPa`: GPa

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Selected phonon frequencies for zincblende HgSe and HgTe at zero pressure and at a compressed volume (~3 GPa), extracted from finite-displacement supercell calculations.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `pressure_condition`, `frequency_TO_Gamma_THz`, `frequency_TA_X_THz`
  - `units`:
    - `frequency_TO_Gamma_THz`: THz
    - `frequency_TA_X_THz`: THz

Notes: The pressure_condition in phonon_frequencies.csv should use the labels '0_GPa' and '3_GPa' (or equivalent). The TA(X) frequency at the compressed condition is expected to show softening (i.e., be significantly lower than the zero-pressure value).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "V0_pfu_AA3",
          "B0_GPa"
        ],
        "units": {
          "V0_pfu_AA3": "Å³ per formula unit",
          "B0_GPa": "GPa"
        }
      },
      "description": "Zero-pressure equilibrium volumes and bulk moduli for zincblende HgSe and HgTe obtained from a Murnaghan EOS fit to LDA total-energy data."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "pressure_condition",
          "frequency_TO_Gamma_THz",
          "frequency_TA_X_THz"
        ],
        "units": {
          "frequency_TO_Gamma_THz": "THz",
          "frequency_TA_X_THz": "THz"
        }
      },
      "description": "Selected phonon frequencies for zincblende HgSe and HgTe at zero pressure and at a compressed volume (~3 GPa), extracted from finite-displacement supercell calculations."
    }
  ],
  "notes": "The pressure_condition in phonon_frequencies.csv should use the labels '0_GPa' and '3_GPa' (or equivalent). The TA(X) frequency at the compressed condition is expected to show softening (i.e., be significantly lower than the zero-pressure value)."
}
```

## How you are scored
A hidden verifier reads your output files and compares the values against hidden reference data. For `equilibrium_properties.csv`, the verifier checks that $V_0$ and $B_0$ are physically reasonable. For `phonon_frequencies.csv`, it examines the TA($X$) frequency at the compressed condition relative to the zero-pressure value to assess whether softening occurs. Each file receives a partial score, and the weighted sum yields the final reward in [0,1]. The verifier does not require exact reproduction of any particular code or pseudopotential; it evaluates the correctness of the trend and magnitude within tolerances appropriate for the computational approach.
