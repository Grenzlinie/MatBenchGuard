# First-Principles Prediction of Structural and Optoelectronic Properties of BTlGaN Quaternary Alloys

## Problem background
The development of III-nitride semiconductors has enabled ultraviolet, blue, and green light-emitting devices. To extend the spectral range into the infrared, thallium-containing III-nitride alloys have been proposed because the large atomic radius of thallium reduces the band gap significantly. However, TlGaN alloys grown on GaN substrates suffer from lattice mismatch that introduces strain and dislocations, degrading device performance. One strategy to mitigate the mismatch is to substitute small amounts of boron (which has a smaller covalent radius) into the TlGaN lattice, forming quaternary B_xTl_yGa_{1-x-y}N alloys. First-principles calculations can predict the structural, electronic, and optical properties of such alloys and identify compositions that achieve both lattice matching to GaN and infrared band gaps. This task aims to compute these properties from density functional theory and assess whether a particular composition can provide strain-free active layers for infrared optoelectronics.

## Approach
The computational workflow uses density functional theory (DFT) within the full-potential linearized augmented plane wave (FP-LAPW) framework. The open-source Elk code, which implements FP-LAPW, is employed as a substitute for proprietary tools. Structural properties (equilibrium lattice constants and bulk moduli) are obtained by calculating total energy as a function of unit-cell volume and fitting to the Murnaghan equation of state, using the Wu–Cohen generalized gradient approximation (GGA-WC) for exchange-correlation. Electronic band structures are then computed self-consistently with the Tran–Blaha modified Becke–Johnson (TB-mBJ) exchange potential, which yields band gaps much closer to experiment than standard GGA. Optical properties, in particular the dielectric function in the long-wavelength limit, are calculated within the TB-mBJ framework and relate to the static refractive index and dielectric constant via Kramers–Kronig relations. The approach first validates the computational protocol by computing structural and electronic properties of the parent zinc blende binary compounds GaN, BN, and TlN, and comparing against known experimental benchmarks (which are not provided here). Then a 32-atom supercell representing the quaternary alloy B_0.125Tl_0.187Ga_0.688N is constructed and fully relaxed. From the relaxed structure, the equilibrium lattice constant, direct band gap at the Γ point, static dielectric constant ε₁(0), and static refractive index n(0) are extracted.

## Reproduction target
Produce the following quantities, each in the specified output file:

- Equilibrium lattice constants a₀ (Å) and bulk moduli B₀ (GPa) for zinc blende GaN, BN, and TlN (`binary_lattice_constants_bulk_moduli.csv`).
- Direct band gap E_Γ-Γ of GaN and TlN, and indirect band gap E_Γ-X of BN, all in eV (`binary_band_gaps.csv`).
- Equilibrium cubic lattice constant (Å) of the quaternary alloy B₀.₁₂₅Tl₀.₁₈₇Ga₀.₆₈₈N (`quaternary_lattice_constant.txt`).
- Direct band gap (eV) at the Γ point of the same quaternary alloy (`quaternary_bandgap.txt`).
- Static dielectric constant ε₁(0) and static refractive index n(0) = √ε₁(0) of the quaternary alloy (`quaternary_optical_constants.csv`).

All quantities are computed from first principles using the FP-LAPW method with the GGA-WC functional for structure and the TB-mBJ functional for electronic and optical properties, as described in the workflow steps.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Binary structural relaxation and equation-of-state fitting
- Role: process
- Action: Set up and run DFT calculations for zinc blende GaN, BN, and TlN using an open-source FP-LAPW code (e.g., Elk) with the GGA-WC functional. For each compound, compute total energy for a range of lattice volumes, fit the energy-volume data to the Murnaghan equation of state, and determine the equilibrium lattice constant a0 and bulk modulus B0. Retain optimized structural parameters for later steps.
- Evidence: `/app/outputs/binary_eos_data.json`

### Step 2: Extract binary lattice constants and bulk moduli
- Role: scored
- Action: From the equation-of-state fits, extract the equilibrium lattice constant (in ångströms) and bulk modulus (in GPa) for GaN, BN, and TlN. Write them to a CSV file.
- Output file: `/app/outputs/binary_lattice_constants_bulk_moduli.csv`
- Format: csv
- Contract: CSV with columns: binary (string), a0_angstrom (float), B0_GPa (float). One row per binary compound.
- Scoring: scored by hidden verifier

### Step 3: Binary band structure calculation
- Role: process
- Action: Using the equilibrium lattice constants from the binary relaxation, perform self-consistent field and band-structure calculations with the TB-mBJ exchange potential for GaN, BN, and TlN. Obtain band energies at the Γ and X points. Save the raw band structure data as evidence.
- Evidence: `/app/outputs/binary_band_structures.npy`

### Step 4: Extract binary band gaps
- Role: scored
- Action: From the band-structure data, extract the required band gaps: for GaN the direct gap E_Γ-Γ; for TlN the direct gap E_Γ-Γ; for BN the indirect gap E_Γ-X. Write the values (in eV) to a CSV file.
- Output file: `/app/outputs/binary_band_gaps.csv`
- Format: csv
- Contract: CSV with columns: binary (string), gap_type (string, either 'E_Γ-Γ' or 'E_Γ-X'), energy_eV (float). One row per gap.
- Scoring: scored by hidden verifier

### Step 5: Quaternary alloy structural relaxation
- Role: process
- Action: Construct a 32-atom zinc blende supercell (2×2×1) corresponding to composition B0.125Tl0.187Ga0.688N. Using the GGA-WC functional, perform full structural relaxation (atomic positions and optionally cell volume) to obtain the equilibrium structure. Save the relaxation log as evidence.
- Evidence: `/app/outputs/quaternary_relaxation.log`

### Step 6: Extract quaternary lattice constant
- Role: scored (load-bearing)
- Action: From the relaxed quaternary supercell, compute the equilibrium cubic lattice constant (in ångströms) and write it as a single number to a text file.
- Output file: `/app/outputs/quaternary_lattice_constant.txt`
- Format: txt
- Contract: A single line with the lattice constant in ångströms as a floating-point value.
- Scoring: scored by hidden verifier

### Step 7: Quaternary band structure calculation
- Role: process
- Action: Using the relaxed quaternary structure, run self-consistent and band-structure calculations with the TB-mBJ functional. Save the band structure data as evidence.
- Evidence: `/app/outputs/quaternary_band_structure.npy`

### Step 8: Extract quaternary band gap
- Role: scored (load-bearing)
- Action: Extract the direct band gap at the Γ point (in eV) from the band structure and write it as a single number to a text file.
- Output file: `/app/outputs/quaternary_bandgap.txt`
- Format: txt
- Contract: A single line with the band gap in eV as a floating-point value.
- Scoring: scored by hidden verifier

### Step 9: Quaternary optical properties calculation
- Role: process
- Action: Using the relaxed quaternary structure and the TB-mBJ functional, compute the frequency-dependent dielectric function in the long-wavelength limit. Obtain the real part ε1(ω) to extract the static limit. Save the dielectric function data as evidence.
- Evidence: `/app/outputs/quaternary_dielectric_function.txt`

### Step 10: Extract quaternary optical constants
- Role: scored (load-bearing)
- Action: From the dielectric function, extract the static dielectric constant ε1(0) and the static refractive index n(0) = √ε1(0). Write them to a CSV file with two rows.
- Output file: `/app/outputs/quaternary_optical_constants.csv`
- Format: csv
- Contract: CSV with columns: property (string), value (float). Rows: 'static_dielectric_constant' and 'static_refractive_index'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binary_lattice_constants_bulk_moduli.csv`
- `/app/outputs/binary_band_gaps.csv`
- `/app/outputs/quaternary_lattice_constant.txt`
- `/app/outputs/quaternary_bandgap.txt`
- `/app/outputs/quaternary_optical_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binary_lattice_constants_bulk_moduli.csv
- path: `/app/outputs/binary_lattice_constants_bulk_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constants and bulk moduli of GaN, BN, and TlN compared to paper Table 1.
- schema:
  - `type`: table
  - `required_columns`: `binary`, `a0_angstrom`, `B0_GPa`
  - `description`: Binary structural properties.

### binary_band_gaps.csv
- path: `/app/outputs/binary_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct and indirect band gaps of GaN, TlN, and BN computed with TB-mBJ, compared to paper Table 2.
- schema:
  - `type`: table
  - `required_columns`: `binary`, `gap_type`, `energy_eV`
  - `description`: Binary band gaps.

### quaternary_lattice_constant.txt
- path: `/app/outputs/quaternary_lattice_constant.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant of B0.125Tl0.187Ga0.688N.
- schema:
  - `type`: text
  - `description`: Single floating‑point value for the quaternary lattice constant in Å.

### quaternary_bandgap.txt
- path: `/app/outputs/quaternary_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Direct band gap at Γ of B0.125Tl0.187Ga0.688N.
- schema:
  - `type`: text
  - `description`: Single floating‑point value for the quaternary direct band gap in eV.

### quaternary_optical_constants.csv
- path: `/app/outputs/quaternary_optical_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constant ε1(0) and static refractive index n(0) of B0.125Tl0.187Ga0.688N.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`
  - `description`: Static optical constants.

Notes: All scored quantities are compared to hidden reference values extracted from the paper. The agent must perform the full DFT workflow; the last three scored steps are load-bearing to ensure genuine execution.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binary_lattice_constants_bulk_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "binary",
          "a0_angstrom",
          "B0_GPa"
        ],
        "description": "Binary structural properties."
      },
      "description": "Equilibrium lattice constants and bulk moduli of GaN, BN, and TlN compared to paper Table 1."
    },
    {
      "file": "binary_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "binary",
          "gap_type",
          "energy_eV"
        ],
        "description": "Binary band gaps."
      },
      "description": "Direct and indirect band gaps of GaN, TlN, and BN computed with TB-mBJ, compared to paper Table 2."
    },
    {
      "file": "quaternary_lattice_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating‑point value for the quaternary lattice constant in Å."
      },
      "description": "Equilibrium lattice constant of B0.125Tl0.187Ga0.688N."
    },
    {
      "file": "quaternary_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating‑point value for the quaternary direct band gap in eV."
      },
      "description": "Direct band gap at Γ of B0.125Tl0.187Ga0.688N."
    },
    {
      "file": "quaternary_optical_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ],
        "description": "Static optical constants."
      },
      "description": "Static dielectric constant ε1(0) and static refractive index n(0) of B0.125Tl0.187Ga0.688N."
    }
  ],
  "notes": "All scored quantities are compared to hidden reference values extracted from the paper. The agent must perform the full DFT workflow; the last three scored steps are load-bearing to ensure genuine execution."
}
```

## How you are scored
A hidden automated verifier will evaluate each scored artifact independently by comparing your computed values to reference values stored in the grading system. The reference values are derived from the same computational protocol and units; they are not disclosed to you. Each artifact is scored using a tolerance that accounts for the expected spread between different DFT implementations, and the verifier awards partial credit as your results deviate from the reference. The final reward is a weighted sum of the scores from all scored artifacts. The quaternary lattice constant, band gap, and optical constants are load-bearing, meaning they require genuine execution of the computationally heavy DFT workflow; you cannot obtain them by trivial guessing. The verifier will not reward you for simply printing a pre-known number; you must demonstrate the sequence of calculations and write the results as specified.
