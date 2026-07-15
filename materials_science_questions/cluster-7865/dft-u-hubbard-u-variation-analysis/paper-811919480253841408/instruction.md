# DFT+U Investigation of Intermediate Band and Half-Metallicity in Cr-Doped ZnTe

## Problem background
Cr-doped II–VI semiconductors are investigated as candidates for half-metallic ferromagnets and intermediate-band materials with potential applications in spintronics, optoelectronics, and high-efficiency solar cells. In these materials, the interplay between the Cr 3d states and the host semiconductor bands determines whether a partially filled intermediate band forms within the gap. Density-functional theory calculations using the local spin density approximation (LSDA) often underestimate correlation effects in narrow d bands, which can lead to an inaccurate description of the intermediate band occupation and its stability. The LSDA+U approach adds a Hubbard U term to correct self-interaction and improve the description of the Cr d orbitals. Understanding how the Hubbard U parameter affects the electronic structure at low Cr concentrations is essential for predicting the behavior of such materials, yet the magnitude of these correlation effects and their dependence on the host semiconductor remain open questions.

## Approach
The investigation uses spin-polarized first-principles calculations based on the local spin density approximation (LSDA) and its extension with a Hubbard U correction (LSDA+U). Starting from the zinc-blende ZnTe host, 64-atom supercells are constructed with Cr substitutions at Zn sites to represent two dilute concentrations, x=1/32 and 2/32, and a ferromagnetic spin alignment is imposed. The atomic positions are first relaxed within LSDA to obtain the equilibrium geometry. From the relaxed structures, self-consistent field calculations are carried out for each concentration at three values of the Hubbard U parameter (0, 3, and 6 eV) to sample the range of correlation effects. Norm-conserving pseudopotentials and a double-zeta polarized basis are employed, with a k-point grid sufficient to converge the electronic structure. After each self-consistent run, band structures and density-of-states (DOS) data are computed. The resulting electronic structure is analyzed to identify the intermediate band in the majority-spin channel and to extract the characteristic energy gaps (between valence band and intermediate band, the intermediate band width, and the gaps to the conduction band) as well as the integrated DOS that measures the occupation of the intermediate band below and above the Fermi level. This workflow directly probes whether a well-defined intermediate band exists, how its width and occupation change with Cr concentration, and how sensitive these quantities are to the Hubbard U correction.

## Reproduction target
For both Cr concentrations (x=1/32 and 2/32) and for each Hubbard U value (0, 3, and 6 eV), compute and report the following quantities from the spin-polarized band structures and DOS:

1. The majority-spin band gaps: the gap between the valence-band maximum and the intermediate-band minimum (ΔE_VI⁺), the intermediate-band width (ΔE_I⁺), and the gap between the intermediate-band maximum and the conduction-band minimum (ΔE_IC⁺). Also compute the minority-spin gap between the valence-band maximum and the conduction-band minimum (ΔE_VC⁻). Write these values to `/app/outputs/band_gaps.csv` with the schema described in the step contract.

2. The integrated majority-spin DOS of the intermediate band: integrate the DOS from the intermediate-band bottom to the Fermi level (DOS_below_Ef, electrons per 64-atom cell) and from the Fermi level to the intermediate-band top (DOS_above_Ef). Write the results to `/app/outputs/integrated_dos_IB.csv` using the schema below.

The band gaps and integrated DOS jointly characterize the formation of the intermediate band and its partial occupancy. The evaluation examines whether the obtained gaps and integrated DOS reproduce the values predicted by the original study within appropriate numerical tolerances.

## Assets

- SIESTA open-source DFT package: https://departments.icmab.es/leem/siesta/
- Troullier-Martins pseudopotentials for Zn, Te, Cr: https://departments.icmab.es/leem/siesta/Databases/

## Workflow steps

### Step 1: Supercell construction and input preparation
- Role: process
- Action: Construct 64-atom zinc-blende ZnTe supercells with Cr substitution at Zn sites to obtain concentrations x=1/32 and 2/32. Set ferromagnetic spin configuration. Prepare SIESTA input files using DZP basis, Troullier-Martins pseudopotentials, and an 18-special-k-point grid.
- Evidence: `/app/outputs/supercell_inputs.tar.gz`

### Step 2: LSDA atomic relaxation
- Role: process
- Action: Perform spin-polarised LSDA relaxation for both x=1/32 and x=2/32, allowing Cr and nearest-neighbour atoms to relax until forces fall below 0.004 eV/Å.
- Evidence: `/app/outputs/relaxed_coordinates.xyz`

### Step 3: SCF and band structure / DOS calculations
- Role: process
- Action: For each relaxed supercell, run spin-polarised LSDA (U=0) and LSDA+U (U=3, 6 eV) self-consistent field calculations, followed by band-structure and density-of-states post-processing. Save raw .bands and .DOS outputs.
- Evidence: `/app/outputs/raw_dft_outputs.tar.gz`

### Step 4: Band gaps extraction
- Role: scored (load-bearing)
- Action: From the band-structure outputs, determine the majority-spin VB maximum, IB minimum, IB maximum, CB minimum and the minority-spin VB–CB gap. For every (concentration, U) combination, compute ΔE_VI⁺, ΔE_I⁺, ΔE_IC⁺, ΔE_VC⁻ and write them to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: Columns: concentration (string, e.g. '1/32'), U (integer eV), Delta_E_VI_plus (float eV), Delta_E_I_plus (float eV), Delta_E_IC_plus (float eV), Delta_E_VC_minus (float eV). One row per (concentration, U) combination.
- Scoring: scored by hidden verifier

### Step 5: Intermediate band integrated DOS
- Role: scored (load-bearing)
- Action: From the DOS outputs, integrate the majority-spin DOS from the IB bottom to E_F and from E_F to the IB top, obtaining electrons per 64-atom cell. Write the results for all U values to integrated_dos_IB.csv.
- Output file: `/app/outputs/integrated_dos_IB.csv`
- Format: csv
- Contract: Columns: concentration (string), U (integer eV), DOS_below_Ef (float electrons/cell), DOS_above_Ef (float electrons/cell). One row per (concentration, U) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/integrated_dos_IB.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gaps extracted from DFT calculations for each Cr concentration and Hubbard U value. Compared against paper Table 1 with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `U`, `Delta_E_VI_plus`, `Delta_E_I_plus`, `Delta_E_IC_plus`, `Delta_E_VC_minus`
  - `units`:
    - `Delta_E_VI_plus`: eV
    - `Delta_E_I_plus`: eV
    - `Delta_E_IC_plus`: eV
    - `Delta_E_VC_minus`: eV

### integrated_dos_IB.csv
- path: `/app/outputs/integrated_dos_IB.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Integrated DOS of the intermediate band below and above the Fermi level, confirming partial occupation and U insensitivity. Compared against paper-reported values and U=0 baseline.
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `U`, `DOS_below_Ef`, `DOS_above_Ef`
  - `units`:
    - `DOS_below_Ef`: electrons per 64-atom cell
    - `DOS_above_Ef`: electrons per 64-atom cell

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "U",
          "Delta_E_VI_plus",
          "Delta_E_I_plus",
          "Delta_E_IC_plus",
          "Delta_E_VC_minus"
        ],
        "units": {
          "Delta_E_VI_plus": "eV",
          "Delta_E_I_plus": "eV",
          "Delta_E_IC_plus": "eV",
          "Delta_E_VC_minus": "eV"
        }
      },
      "description": "Band gaps extracted from DFT calculations for each Cr concentration and Hubbard U value. Compared against paper Table 1 with tolerances."
    },
    {
      "file": "integrated_dos_IB.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "U",
          "DOS_below_Ef",
          "DOS_above_Ef"
        ],
        "units": {
          "DOS_below_Ef": "electrons per 64-atom cell",
          "DOS_above_Ef": "electrons per 64-atom cell"
        }
      },
      "description": "Integrated DOS of the intermediate band below and above the Fermi level, confirming partial occupation and U insensitivity. Compared against paper-reported values and U=0 baseline."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects the two scored artifact files (`band_gaps.csv` and `integrated_dos_IB.csv`). The verifier compares each reported quantity against reference values derived from the original investigation, using tolerances that account for the spread introduced by different code implementations, pseudopotential flavors, and basis set choices. The band gaps (step 4) contribute 70% of the total score, and the integrated DOS of the intermediate band (step 5) contributes 30%. To receive full credit, you must genuinely execute the entire DFT workflow; simply fabricating numbers that look plausible will not pass the hidden checks, which include consistency tests across concentration and U values. No specific tolerance or reference value is disclosed here, so your best strategy is to faithfully run the described protocol and extract the quantities from your computed results.
