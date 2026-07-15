# Mechanical and Thermal Properties of Hf/Nb/Zr-Doped MAX Phases via DFT

## Problem background
MAX phases are a class of layered ternary ceramics that combine metallic and ceramic properties. Doping with transition metals can modify their mechanical and thermal behavior. This task investigates, using density functional theory (DFT), how Hf, Nb, or Zr doping at either substitutional (Ti1 site) or interstitial (c-ATi2 site) positions affects the structural, elastic, mechanical, and thermal properties of Ti3AlC2 and Ti3SiC2, and whether interstitial doping can induce magnetism.

## Approach
The approach is a standard first-principles DFT computation. For each of the 14 systems (pristine and doped), a 2×2×1 supercell is constructed, relaxed using spin-polarized DFT with a GGA-PBE functional, and elastic constants are obtained by applying finite strains. From the relaxed structures and elastic constants, the polycrystalline moduli (bulk, shear, Young’s), Poisson’s ratio, sound velocities, and Debye temperature are computed via the Voigt-Reuss-Hill approximation and standard thermodynamic formulas. For interstitial-doped systems, the total magnetic moment is extracted from the DFT output.

## Reproduction target
The goal is to produce a single CSV file `computed_properties.csv` containing, for each of the 14 systems (pristine Ti3AlC2, pristine Ti3SiC2, and their substitutional- and interstitial-doped variants with Hf, Nb, and Zr at the specified sites), the lattice constants, independent elastic constants, bulk, shear, and Young’s moduli, Poisson’s ratio, G/B ratio, sound velocities (transverse, longitudinal, average), Debye temperature, and magnetic moment. The CSV must have exactly the columns: system, host, doping_type, dopant, a0_A, c0_A, C11_GPa, C33_GPa, C44_GPa, C12_GPa, C13_GPa, B_GPa, G_GPa, E_GPa, sigma, G_B_ratio, vt_ms, vl_ms, vm_ms, ThetaD_K, Mag_muB. The output will be evaluated based on how well the computed numeric values agree with reference data and whether the relative changes between pristine, substitutionally doped, and interstitially doped systems follow the expected trends.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials (efficiency version): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct 2×2×1 supercells for pristine Ti3AlC2 and Ti3SiC2, and for Hf/Nb/Zr-doped configurations: substitutional doping at the Ti1 site (replacing one Ti1) and interstitial doping at the c-ATi2 site (dopant placed between A layer and Ti2 layer). Use known hexagonal lattice parameters and Wyckoff positions.
- Evidence: `/app/outputs/supercell_structures.txt`

### Step 2: DFT structural relaxation
- Role: process
- Action: For each of the 14 systems, perform spin-polarized DFT structural relaxation using Quantum ESPRESSO with GGA-PBE functional, plane-wave energy cutoff 600 eV, k-point mesh 6×6×2, and force convergence below 1e-3 eV/Å. Relax atomic positions and cell shape.
- Evidence: `/app/outputs/relaxation_summary.log`

### Step 3: DFT elastic constant calculation
- Role: process
- Action: For each relaxed structure, compute the five independent elastic constants (C11, C33, C44, C12, C13) of the hexagonal lattice using the finite-strain method.
- Evidence: `/app/outputs/elastic_constants.log`

### Step 4: Compute mechanical and thermal properties
- Role: scored (load-bearing)
- Action: From relaxed lattice parameters and stoichiometry, compute mass density ρ. Using the elastic constants, calculate bulk modulus B and shear modulus G via the Voigt-Reuss-Hill (VRH) approximation, then compute Young's modulus E and Poisson's ratio σ. Compute transverse (vt), longitudinal (vl), and average (vm) sound velocities, and Debye temperature ΘD using standard formulas with fundamental constants and atomic masses. For interstitial-doped systems, extract the total magnetic moment from DFT output. Assemble all results into a single CSV file with exactly 14 rows (one per system).
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: Columns: system (str), host (str), doping_type (str), dopant (str), a0_A (float), c0_A (float), C11_GPa (float), C33_GPa (float), C44_GPa (float), C12_GPa (float), C13_GPa (float), B_GPa (float), G_GPa (float), E_GPa (float), sigma (float), G_B_ratio (float), vt_ms (float), vl_ms (float), vm_ms (float), ThetaD_K (float), Mag_muB (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing computed mechanical and thermal properties for all 14 pristine and doped MAX-phase systems.
- schema:
  - `type`: table
  - `required_columns`: `system`, `host`, `doping_type`, `dopant`, `a0_A`, `c0_A`, `C11_GPa`, `C33_GPa`, `C44_GPa`, `C12_GPa`, `C13_GPa`, `B_GPa`, `G_GPa`, `E_GPa`, `sigma`, `G_B_ratio`, `vt_ms`, `vl_ms`, `vm_ms`, `ThetaD_K`, `Mag_muB`

Notes: Values are compared to hidden paper reported values with appropriate tolerances. Trend checks (substitutional within 10% of pristine, interstitial at least 20% lower moduli, magnetic moment thresholds) are also evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "host",
          "doping_type",
          "dopant",
          "a0_A",
          "c0_A",
          "C11_GPa",
          "C33_GPa",
          "C44_GPa",
          "C12_GPa",
          "C13_GPa",
          "B_GPa",
          "G_GPa",
          "E_GPa",
          "sigma",
          "G_B_ratio",
          "vt_ms",
          "vl_ms",
          "vm_ms",
          "ThetaD_K",
          "Mag_muB"
        ]
      },
      "description": "CSV containing computed mechanical and thermal properties for all 14 pristine and doped MAX-phase systems."
    }
  ],
  "notes": "Values are compared to hidden paper reported values with appropriate tolerances. Trend checks (substitutional within 10% of pristine, interstitial at least 20% lower moduli, magnetic moment thresholds) are also evaluated."
}
```

## How you are scored
Your submission is scored by a hidden verifier. The verifier reads `computed_properties.csv` and compares each numeric value to a set of reference values derived from the original study, using appropriate tolerances. Additionally, the verifier checks that the relative ranking of moduli and the presence of magnetic moments across the 14 systems are consistent with the underlying physics (e.g., that substitutional doping causes only small changes relative to pristine, while interstitial doping leads to a substantial reduction, and that magnetism appears only in certain interstitial cases). Checks carry different weights, and the final reward is the weighted sum of passed checks. Producing the file exactly in the specified format is mandatory; missing columns or malformed data may result in a score of zero.
