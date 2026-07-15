# Actinide Ionization Potentials and Excitation Energies from QR Pseudopotential and Four-Component DFT Computations

## Problem background
The actinide series (Ac–Lr) presents complex electronic structure due to open 5f, 6d, and 7s shells and strong relativistic effects, making accurate experimental determination of ionization potentials and excitation energies challenging. Experimental data are sparse, especially for higher ionization states. First-principles computational predictions can provide reliable values where experiments are missing and guide future measurements. This task reproduces a comprehensive dataset of ionization potentials and excitation energies for the complete actinide series using two independent theoretical approaches.

## Approach
The task employs two independent levels of theory.

1. **Quasirelativistic energy-consistent small-core pseudopotential (QR PP) method:** State-averaged complete active space self-consistent field (CASSCF) calculations with dynamic correlation via the averaged coupled-pair functional (ACPF). The active space includes 5f, 6d, and 7s orbitals; excitations from semicore 6p (and optionally 6s and 5d) are allowed. Spin‑orbit corrections are obtained from configuration interaction within the open‑shell orbitals and added to the scalar‑relativistic energies.

2. **Fully relativistic four‑component Dirac–Kohn–Sham (DKS) DFT:** All‑electron Dirac–Kohn–Sham calculations using the local‑density approximation with a self‑interaction correction (LDASIC), the Becke gradient exchange correction (B), and the Becke–Perdew exchange‑correlation functional (BP). Open shells are treated with moment‑polarized fractional occupancies and a frozen core [1s²–5d¹⁰].

For each method, total energies are computed for all required neutral and ionic configurations (up to the fourth charge state) and for the configurations relevant to the Δdf and Δfd excitation energies. From these total energies, the first through fourth ionization potentials (IP1–IP4) and the excitation energies Δdf and Δfd are derived as energy differences. The results from the two approaches are collected and can be compared to assess agreement and systematic variations across the actinide series.

## Reproduction target
Compute the first through fourth ionization potentials (IP1–IP4) and the Δdf and Δfd excitation energies (defined as the energy differences between specific configurations) for every actinide atom from Ac to Lr (atomic numbers 89–103). Perform the calculations using both the quasirelativistic pseudopotential (QR_PP) method and the four‑component Dirac–Kohn–Sham DFT method with each of the three functionals: LDASIC, Becke exchange (B), and Becke–Perdew (BP). Collect all results in electronvolts (eV) in the CSV file `actinide_properties.csv` with the following columns:
- Element (string, e.g., 'Ac'),
- Z (integer atomic number),
- Method (one of 'QR_PP', 'BDF_LDASIC', 'BDF_B', 'BDF_BP'),
- Property (one of 'IP1', 'IP2', 'IP3', 'IP4', 'Delta_df', 'Delta_fd'),
- Value (float, in eV).
Include rows for every applicable combination of element, method, and property. The resulting dataset provides a systematic picture of these fundamental quantities for the actinide series.

## Assets

- Stuttgart energy-consistent small-core pseudopotentials for Ac–Lr: https://www.tc.uni-koeln.de/PP/
- Valence basis sets (12s11p10d8f4g)/[8s7p6d4f4g] for actinides: https://www.basissetexchange.org/
- Open-source quantum chemistry code (PySCF): pyscf
- Fully relativistic four-component Dirac–Kohn–Sham DFT code (DIRAC): http://diracprogram.org/

## Workflow steps

### Step 1: QR PP scalar-relativistic CASSCF/ACPF energy calculations
- Role: process
- Action: For each actinide atom Ac–Lr, perform state‑averaged CASSCF/ACPF calculations for all required neutral and ionic configurations using the small‑core pseudopotentials and valence basis sets. Active space: 5f, 6d, 7s; allow excitations from semicore 6p (and optionally 6s,5d) in ACPF. Obtain scalar‑relativistic total energies for every configuration.
- Evidence: `/app/outputs/qrpp_scalar_energies.csv`

### Step 2: QR PP spin‑orbit correction calculations
- Role: process
- Action: For each configuration, perform complete CI within the open‑shell orbitals including the spin‑orbit operator provided by the pseudopotential, obtain spin‑orbit corrections, and add them to the scalar‑relativistic energies to yield the final QR PP total energies.
- Evidence: `/app/outputs/qrpp_final_energies.csv`

### Step 3: Fully relativistic DFT total energy calculations
- Role: process
- Action: For the same electronic configurations, run four‑component Dirac–Kohn–Sham DFT using the LDASIC, Becke exchange (B), and Becke–Perdew (BP) functionals. Use moment‑polarized fractional occupancies for open shells, a frozen core [1s²–5d¹⁰], and the numerical‑atomic‑spinor plus double‑ζ Slater‑type valence basis. Obtain total energies for each functional.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 4: Derivation of ionization potentials and excitation energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in the previous steps, compute the first through fourth ionization potentials (IP1–IP4) and the Δdf and Δfd excitation energies for all actinide elements according to the energy‑difference definitions. Collect all values in a structured CSV file.
- Output file: `/app/outputs/actinide_properties.csv`
- Format: csv
- Contract: CSV with columns: Element (string, e.g., 'Ac'), Z (integer), Method (one of 'QR_PP','BDF_LDASIC','BDF_B','BDF_BP'), Property (one of 'IP1','IP2','IP3','IP4','Delta_df','Delta_fd'), Value (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/actinide_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### actinide_properties.csv
- path: `/app/outputs/actinide_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed ionization potentials and excitation energies for the actinide series. The checker compares each (Element,Method,Property) row to the paper‑reported reference values (hidden gold) within per‑property tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Element`, `Z`, `Method`, `Property`, `Value`
  - `units`:
    - `Value`: eV

Notes: The DV‑Xα calculations for Es and No are excluded as they are a minor diagnostic comparison not part of the core dataset.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "actinide_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Element",
          "Z",
          "Method",
          "Property",
          "Value"
        ],
        "units": {
          "Value": "eV"
        }
      },
      "description": "Computed ionization potentials and excitation energies for the actinide series. The checker compares each (Element,Method,Property) row to the paper‑reported reference values (hidden gold) within per‑property tolerances."
    }
  ],
  "notes": "The DV‑Xα calculations for Es and No are excluded as they are a minor diagnostic comparison not part of the core dataset."
}
```

## How you are scored
A hidden verifier reads your final output file `actinide_properties.csv`. For each row (a specific element, method, and property) the verifier compares your reported Value to a hidden reference value. The comparison uses a per‑property tolerance that accounts for legitimate differences due to implementation, basis sets, and convergence choices; the closer your result, the higher the credit. The overall reward is a weighted combination over all rows, with full credit awarded when your values fall within the acceptable error margin.

The intermediate process evidence files (`qrpp_scalar_energies.csv`, `qrpp_final_energies.csv`, `dft_energies.csv`) are required to demonstrate that the workflow steps were executed, but they are not individually scored. Missing or incomplete intermediate files may reduce the reward.
