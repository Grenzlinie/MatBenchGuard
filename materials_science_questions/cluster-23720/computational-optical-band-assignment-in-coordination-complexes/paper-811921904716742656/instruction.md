# Group IV Metallocene Dichlorides Covalency from DFT and TD-DFT

## Problem background
Group IV metallocene dichlorides (C5H5)2MCl2 (M = Ti, Zr, Hf) are classic organometallic complexes whose reactivity is linked to the covalent character of the metal–chlorine bonds. Chlorine K-edge X-ray absorption spectroscopy (XAS) provides a direct experimental probe of ligand-to-metal orbital mixing, but the underlying electronic structure and the role of each virtual orbital in determining bond covalency require computational analysis. This task reproduces the quantum-chemical calculation of %Cl 3p character per M–Cl bond and the simulation of the Cl K-edge pre-edge spectral features, enabling a quantitative understanding of how the metal’s principal quantum number influences covalent bonding.

## Approach
The computational work uses density functional theory (DFT) with the B3LYP hybrid functional. For metals, the Stuttgart RSC 1997 relativistic effective core potential (ECP) is employed together with its associated basis sets; carbon, hydrogen, and chlorine are described by the 6‑31G* basis set. Ground-state geometry optimizations are performed for each complex, followed by Mulliken population analysis on the five lowest unoccupied metal‑d‑based molecular orbitals (labelled 1a1, 1b2, 1b1, 1a2, 2a1) to extract the percent Cl 3p character. Core-excited states are then simulated using linear-response time-dependent DFT (TD‑DFT) from the chlorine 1s orbitals into the virtual manifold. A uniform energy shift of +64.9 eV is applied to the computed transition energies to bring them onto the experimental energy scale. The analysis yields per‑orbital and total per‑bond Cl 3p contributions, as well as pre‑edge transition energies, oscillator strengths, and associated Cl 3p characters.

## Reproduction target
For the three complexes (M = Ti, Zr, Hf), compute and report:

1. The percent Cl 3p character in each of the five metal‑d‑based virtual orbitals (1a1, 1b2, 1b1, 1a2, 2a1) and the total percent Cl 3p character per M–Cl bond (obtained as half the sum of the five orbital contributions), written to a CSV file.

2. The simulated Cl K-edge pre-edge features from TD‑DFT: two pre-edge peaks per complex, each with its transition energy (eV), oscillator strength, and percent Cl 3p character, written to a second CSV file. The peaks should be labelled as peak1 and peak2.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Stuttgart RSC 1997 ECP and 6-31G* basis sets: https://www.basissetexchange.org/
- Molecular connectivity of (C5H5)2MCl2

## Workflow steps

### Step 1: Prepare initial molecular geometries
- Role: process
- Action: Build initial Cartesian coordinates for (C5H5)2MCl2 (M = Ti, Zr, Hf) reflecting the bent metallocene motif with approximate symmetry. Save each geometry as a separate coordinate file.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: Ground-state DFT optimisation and electronic structure analysis
- Role: process
- Action: Run B3LYP geometry optimization on each complex using the Stuttgart RSC 1997 ECP for metals and 6-31G* for C, H, Cl. Compute molecular orbital energies and perform Mulliken population analysis to extract %Cl 3p character for the five metal-d-based virtual orbitals (1a1, 1b2, 1b1, 1a2, 2a1).
- Evidence: `/app/outputs/dft_populations.log`

### Step 3: Report ground-state %Cl 3p character
- Role: scored (load-bearing)
- Action: From the Mulliken populations, output a CSV containing, for each compound, the %Cl 3p character in each of the five relevant orbitals and the sum of these percentages divided by two (to give %Cl 3p per M-Cl bond).
- Output file: `/app/outputs/computed_percent_Cl3p.csv`
- Format: csv
- Contract: compound: str, orbital: str, percent_Cl3p: float. For each compound there are six rows (five orbitals + total).
- Scoring: scored by hidden verifier

### Step 4: TD-DFT core-excitation simulation
- Role: process
- Action: Using the optimised geometries, run linear-response TD-DFT from the Cl 1s orbitals to the virtual MO manifold. Apply a uniform energy shift of +64.9 eV to the computed transition energies to align with the experimental energy scale. Extract transition energies, oscillator strengths, and %Cl 3p character for each pre-edge peak via Mulliken analysis of the core-excited state.
- Evidence: `/app/outputs/tddft_spectrum.log`

### Step 5: Report simulated XAS features
- Role: scored
- Action: From the TD-DFT calculation, produce a CSV listing the two pre-edge peaks for each complex: peak label, energy (eV), oscillator strength, and the computed %Cl 3p character per peak.
- Output file: `/app/outputs/simulated_XAS_features.csv`
- Format: csv
- Contract: compound: str, peak_label: str, peak_energy_eV: float, oscillator_strength: float, percent_Cl3p: float. Two rows per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_percent_Cl3p.csv`
- `/app/outputs/simulated_XAS_features.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_percent_Cl3p.csv
- path: `/app/outputs/computed_percent_Cl3p.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed percent Cl 3p character for each metal-d-based virtual orbital and the total per M-Cl bond (as the 'total' row).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `orbital`, `percent_Cl3p`
  - `units`:
    - `percent_Cl3p`: percent

### simulated_XAS_features.csv
- path: `/app/outputs/simulated_XAS_features.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated Cl K-edge pre-edge transition energies, oscillator strengths, and per-peak %Cl 3p character from TD-DFT.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `peak_label`, `peak_energy_eV`, `oscillator_strength`, `percent_Cl3p`
  - `units`:
    - `peak_energy_eV`: eV
    - `oscillator_strength`: dimensionless
    - `percent_Cl3p`: percent

Notes: The reference check compares the total %Cl 3p per M-Cl bond and the peak energy splittings to the paper's calculated values with a tolerance, and verifies the Ti > Zr > Hf trend and that two peaks are present with peak2 intensity > peak1 intensity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_percent_Cl3p.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "orbital",
          "percent_Cl3p"
        ],
        "units": {
          "percent_Cl3p": "percent"
        }
      },
      "description": "Computed percent Cl 3p character for each metal-d-based virtual orbital and the total per M-Cl bond (as the 'total' row)."
    },
    {
      "file": "simulated_XAS_features.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "peak_label",
          "peak_energy_eV",
          "oscillator_strength",
          "percent_Cl3p"
        ],
        "units": {
          "peak_energy_eV": "eV",
          "oscillator_strength": "dimensionless",
          "percent_Cl3p": "percent"
        }
      },
      "description": "Simulated Cl K-edge pre-edge transition energies, oscillator strengths, and per-peak %Cl 3p character from TD-DFT."
    }
  ],
  "notes": "The reference check compares the total %Cl 3p per M-Cl bond and the peak energy splittings to the paper's calculated values with a tolerance, and verifies the Ti > Zr > Hf trend and that two peaks are present with peak2 intensity > peak1 intensity."
}
```

## How you are scored
A hidden verifier independently inspects both CSV files that you output. For the ground‑state CSV, it checks that the per‑bond %Cl 3p values for Ti, Zr, and Hf are close to expected reference values (within a hidden tolerance) and that the trend among them is correct. For the XAS CSV, it verifies that exactly two pre-edge peaks are present per compound, that the second peak’s intensity is larger than the first, and that the energy splittings and total Cl 3p character are consistent with reference calculations. Each CSV contributes a weighted portion to the final reward. Reporting a number without genuinely running the required calculations is detectable by the verifier and will not receive full credit.
