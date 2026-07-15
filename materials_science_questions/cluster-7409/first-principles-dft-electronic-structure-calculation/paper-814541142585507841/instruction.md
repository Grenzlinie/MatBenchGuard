# Band Gap Engineering of KTaO3 via Anionic Codoping: DFT Study

## Problem background
KTaO3 is a perovskite oxide with a wide band gap (~3.6 eV) that limits its visible-light photocatalytic activity for water splitting. Anionic doping, particularly with nitrogen, can narrow the band gap but often introduces localized defect states that harm photoconversion efficiency. Codoping with halogen elements (F, Cl, Br, I) may compensate these defects and restore a clean band structure. This study investigates whether specific (N, halogen) codoping pairs can achieve significant band gap reduction while maintaining suitable band edge alignment for overall water splitting.

## Approach
The computational approach uses density functional theory (DFT) with the Heyd–Scuseria–Ernzerhof (HSE) hybrid functional. A cubic KTaO3 supercell (2×2×2) is built as the host model. Doping is performed substitutionally at oxygen sites with N, F, Cl, Br, I individually (monodoping) and with (N, halogen) pairs in two spatial configurations (codoping). The workflow includes: (i) geometry optimization of all systems using the PBE functional; (ii) calibration of the HSE mixing fraction to reproduce the experimental undoped band gap; (iii) HSE band structure calculations to obtain band gaps and band edge positions; (iv) defect formation energy calculations under oxygen-rich and oxygen-poor conditions using the thermodynamic constraints for KTaO3 growth; (v) optical absorption edge determination from the dielectric function; and (vi) alignment of valence and conduction band edges with water redox potentials. The results for all undoped, monodoped, and codoped configurations are compared to identify the most promising dopant combination.

## Reproduction target
Produce the following quantitative results for the undoped, all five monodoped, and all five codoped systems: (1) band gaps (eV) from HSE; (2) defect formation energies (eV) under oxygen-rich and oxygen-poor conditions; (3) optical absorption edge wavelengths (nm) where the absorption coefficient exceeds 10^4 cm^{-1}; (4) absolute valence band maximum (VBM) and conduction band minimum (CBM) energies (eV vs. vacuum). The computational parameters (PBE functional for relaxations, HSE with calibrated mixing and screening 0.2 Å^{-1}, 500 eV plane-wave cutoff, 8×8×8 k-point mesh, and the KTaO3 chemical potential domain) are fixed across all systems. The objective is to determine, from these outputs, which codoping pair achieves the largest band gap narrowing and most favorable formation energy while retaining band edges straddling the water redox levels for overall water splitting.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency
- KTaO3 cubic crystal structure: https://materialsproject.org/materials/mp-3614/
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Undoped supercell geometry optimization
- Role: process
- Action: Build a 2x2x2 supercell of cubic KTaO3 and perform DFT geometry optimization (cell parameters and atomic positions) using the PBE functional. Record the relaxed structure and total energy.
- Evidence: `/app/outputs/relaxed_undoped.cif`

### Step 2: HSE mixing calibration
- Role: process
- Action: Using the relaxed undoped supercell, compute band gaps with the HSE hybrid functional at Hartree-Fock mixing fractions of 25%, 30%, and 35% (screening parameter 0.2 Å⁻¹). Identify the fraction that best reproduces the experimental band gap of 3.6 eV. Record the chosen fraction.
- Evidence: `/app/outputs/hse_calibration.json`

### Step 3: Geometry optimization of doped/codoped supercells
- Role: process
- Action: For each doping configuration (N, F, Cl, Br, I monodoped; (N,F) str.I and str.II; (N,Cl); (N,Br); (N,I) codoped; substitutional at oxygen sites), build the corresponding 2x2x2 supercell. Perform full geometry relaxation (PBE) and record the relaxed structures and total energies.
- Evidence: `/app/outputs/doped_structures.tar.gz`

### Step 4: Band gap calculation
- Role: scored (load-bearing)
- Action: Using the HSE hybrid functional (mixing fraction from step 1, screening 0.2 Å⁻¹) and the relaxed supercells, compute the electronic band gaps for undoped, each monodoped, and each codoped system. Report the band gap values.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: System (string), BandGap (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Defect formation energy calculation
- Role: scored
- Action: Using total energies from PBE relaxations and chemical potentials of K, Ta (from bulk metals), O (from O2 molecule), and N (from N2 molecule) with the same PBE functional, apply thermodynamic constraints and calculate defect formation energies for oxygen-rich and oxygen-poor conditions for all monodoped and codoped systems.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: System (string), FormationEnergy_OxygenRich (float, eV), FormationEnergy_OxygenPoor (float, eV)
- Scoring: scored by hidden verifier

### Step 6: Optical absorption edge calculation
- Role: scored
- Action: For undoped and each codoped system, compute the frequency-dependent absorption coefficient using HSE and determine the absorption edge wavelength where the absorption coefficient exceeds 10^4 cm^{-1}.
- Output file: `/app/outputs/absorption_edge.csv`
- Format: csv
- Contract: System (string), AbsorptionEdgeWavelength (float, nm)
- Scoring: scored by hidden verifier

### Step 7: Band edge alignment
- Role: scored
- Action: Extract VBM and CBM positions relative to vacuum from HSE calculations. Align these with experimental absolute band edge positions of undoped KTaO3 and the water redox potentials (H+/H2 at -4.44 eV, H2O/O2 at -5.67 eV vs. vacuum). Report VBM and CBM for all codoped systems.
- Output file: `/app/outputs/band_edge_alignment.csv`
- Format: csv
- Contract: System (string), VBM_vs_vacuum (float, eV), CBM_vs_vacuum (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/formation_energies.csv`
- `/app/outputs/absorption_edge.csv`
- `/app/outputs/band_edge_alignment.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed band gaps (eV) for undoped, monodoped, and codoped systems.
- schema:
  - `type`: table
  - `required_columns`: `System`, `BandGap`
  - `units`:
    - `BandGap`: eV

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Defect formation energies (eV) under oxygen-rich and oxygen-poor conditions.
- schema:
  - `type`: table
  - `required_columns`: `System`, `FormationEnergy_OxygenRich`, `FormationEnergy_OxygenPoor`
  - `units`:
    - `FormationEnergy_OxygenRich`: eV
    - `FormationEnergy_OxygenPoor`: eV

### absorption_edge.csv
- path: `/app/outputs/absorption_edge.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optical absorption edge wavelengths (nm) where absorption coefficient > 10^4 cm^{-1}.
- schema:
  - `type`: table
  - `required_columns`: `System`, `AbsorptionEdgeWavelength`
  - `units`:
    - `AbsorptionEdgeWavelength`: nm

### band_edge_alignment.csv
- path: `/app/outputs/band_edge_alignment.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Absolute VBM and CBM positions (eV) relative to vacuum. The VBM must be below the H2O/O2 potential (-5.67 eV) and the CBM must be above the H+/H2 potential (-4.44 eV).
- schema:
  - `type`: table
  - `required_columns`: `System`, `VBM_vs_vacuum`, `CBM_vs_vacuum`
  - `units`:
    - `VBM_vs_vacuum`: eV
    - `CBM_vs_vacuum`: eV

Notes: All columns must be present and values must be numeric. The band edge alignment is verified by threshold conditions: CBM > H+/H2 (-4.44 eV) and VBM < H2O/O2 (-5.67 eV).

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
          "System",
          "BandGap"
        ],
        "units": {
          "BandGap": "eV"
        }
      },
      "description": "Computed band gaps (eV) for undoped, monodoped, and codoped systems."
    },
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "FormationEnergy_OxygenRich",
          "FormationEnergy_OxygenPoor"
        ],
        "units": {
          "FormationEnergy_OxygenRich": "eV",
          "FormationEnergy_OxygenPoor": "eV"
        }
      },
      "description": "Defect formation energies (eV) under oxygen-rich and oxygen-poor conditions."
    },
    {
      "file": "absorption_edge.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "AbsorptionEdgeWavelength"
        ],
        "units": {
          "AbsorptionEdgeWavelength": "nm"
        }
      },
      "description": "Optical absorption edge wavelengths (nm) where absorption coefficient > 10^4 cm^{-1}."
    },
    {
      "file": "band_edge_alignment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "VBM_vs_vacuum",
          "CBM_vs_vacuum"
        ],
        "units": {
          "VBM_vs_vacuum": "eV",
          "CBM_vs_vacuum": "eV"
        }
      },
      "description": "Absolute VBM and CBM positions (eV) relative to vacuum. The VBM must be below the H2O/O2 potential (-5.67 eV) and the CBM must be above the H+/H2 potential (-4.44 eV)."
    }
  ],
  "notes": "All columns must be present and values must be numeric. The band edge alignment is verified by threshold conditions: CBM > H+/H2 (-4.44 eV) and VBM < H2O/O2 (-5.67 eV)."
}
```

## How you are scored
A hidden verifier evaluates each scored CSV file independently. Each of the four scored stages (band gaps, formation energies, absorption edges, band edge alignment) carries a weighted portion of the total reward. The verifier checks that your computed values obey the expected quantitative trends, structural orders, and threshold conditions (e.g. band gap values within a tolerance of reference values, correct ordering of formation energies across dopant types, absorption edge ranking, and band edge alignment with water redox potentials). The exact weights and tolerances are hidden; only the public output contract describes the required file format and columns. Producing the required files with plausible, self-consistent numbers that reflect a genuine DFT calculation is essential.
