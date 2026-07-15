# DFT Study of Strain-Tunable Electronic and Optical Properties of 2D Tetragonal MgS and MgSe Monolayers

## Problem background
Two-dimensional materials with wide band gaps are sought for ultraviolet optoelectronics and shielding. The tetragonal monolayer phases of MgS and MgSe are candidates, but their precise structural parameters, cohesive energy, electronic band gaps, strain-dependent band-gap tuning, and optical dielectric response must be determined from first principles to assess their suitability.

## Approach
The study uses density functional theory (DFT) with the PBE functional for geometry optimization and band structures, and the HSE06 hybrid functional for corrected band gaps. The workflow consists of: constructing the buckled tetragonal unit cells; relaxing the geometries to obtain equilibrium lattice constants, buckling distances, and bond lengths; computing isolated-atom energies to extract cohesive energies; computing PBE and HSE06 band structures at zero strain; applying biaxial strain from -8% to +8% and recalculating PBE band gaps to map the strain dependence; and computing the frequency-dependent complex dielectric function (out-of-plane polarization) together with derived absorption and reflectivity spectra.

## Reproduction target
Produce the equilibrium structural parameters and cohesive energy for both MgS and MgSe; report the PBE and HSE06 band gaps at zero strain; produce a table of PBE band gaps as a function of biaxial strain for both materials; compute the complex dielectric function (real and imaginary parts) for out-of-plane polarization over 0–15+ eV; and derive the absorption coefficient and reflectivity spectra. All results must be placed in the specified output files under /app/outputs according to the output contract.

## Assets

- Quantum ESPRESSO (QE): https://www.quantum-espresso.org/download
- SSSP Efficiency Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate initial structures
- Role: process
- Action: Create the buckled tetragonal unit cells of MgS and MgSe monolayers based on the geometry described in the paper (two Mg atoms and two X atoms per cell, Mg in the middle plane and X atoms buckled outward).
- Evidence: none

### Step 2: Geometry optimization and total energy (PBE)
- Role: process
- Action: Perform DFT relaxation of the unit cells with PBE functional to obtain the fully optimized lattice constants, atomic positions (buckling distance, bond lengths, bond angles), and the ground-state total energy of each unit cell.
- Evidence: `/app/outputs/geo_opt.log`

### Step 3: Isolated atom energy calculations
- Role: process
- Action: Compute the total energy of isolated Mg, S, and Se atoms using the same DFT functional (PBE) and a large enough supercell to avoid interactions.
- Evidence: `/app/outputs/atom_energies.json`

### Step 4: PBE band structure calculation
- Role: process
- Action: On the optimized equilibrium structures, compute the electronic band structure with the PBE functional to obtain the indirect band gap and band-edge character.
- Evidence: `/app/outputs/pbe_bands.dat`

### Step 5: HSE06 band structure calculation
- Role: process
- Action: Recalculate the band structure on the optimized structures using the Heyd–Scuseria–Ernzerhof screened hybrid functional (HSE06) to obtain the more accurate band gap.
- Evidence: `/app/outputs/hse06_bands.dat`

### Step 6: Structural and cohesive energy summary
- Role: scored (load-bearing)
- Action: Collect the optimized structural parameters, compute the cohesive energy from the unit-cell and isolated-atom total energies, and report together with the HSE06 band gap.
- Output file: `/app/outputs/step_01_summary_table.csv`
- Format: csv
- Contract: Columns: Material, Lattice_constant_a(Angstrom), Buckling_delta(Angstrom), Bond_length_MgX(Angstrom), Cohesive_energy(eV/atom), HSE06_band_gap(eV). Rows: MgS, MgSe.
- Scoring: scored by hidden verifier

### Step 7: Zero‑strain band gap report
- Role: scored
- Action: Report the PBE and HSE06 band gaps for MgS and MgSe in a JSON file.
- Output file: `/app/outputs/step_02_band_gaps_zero_strain.json`
- Format: json
- Contract: Example: {"MgS": {"PBE_gap": 3.69, "HSE06_gap": 4.70}, "MgSe": {"PBE_gap": 4.01, "HSE06_gap": 4.51}}
- Scoring: scored by hidden verifier

### Step 8: Strain‑dependent DFT calculations (PBE)
- Role: process
- Action: For each biaxial strain value from -8% to +8% in steps of 2%, modify the lattice constant accordingly and re‑compute the total energy and PBE band structure for both materials.
- Evidence: `/app/outputs/strain_energies.log`

### Step 9: Strain‑dependent band gap table
- Role: scored
- Action: Extract the PBE band gap for each strain and each material into a CSV table.
- Output file: `/app/outputs/step_03_strain_band_gap_PBE.csv`
- Format: csv
- Contract: Columns: Material, Strain_percent, PBE_band_gap(eV). Rows for all strain values.
- Scoring: scored by hidden verifier

### Step 10: Optical properties calculation (dielectric function)
- Role: process
- Action: On the unstrained equilibrium structures, compute the momentum‑matrix‑element‑based imaginary dielectric function and then obtain the real part via Kramers‑Kronig transformation. Derive absorption coefficient and reflectivity spectra.
- Evidence: `/app/outputs/optical_calculations.done`

### Step 11: Dielectric function of MgS
- Role: scored
- Action: Export the real and imaginary parts of the dielectric function for MgS as a function of energy.
- Output file: `/app/outputs/step_04_dielectric_function_MgS.csv`
- Format: csv
- Contract: Columns: Energy_eV, real_eps_ZZ, imag_eps_ZZ.
- Scoring: scored by hidden verifier

### Step 12: Dielectric function of MgSe
- Role: scored
- Action: Same as step_11 but for MgSe.
- Output file: `/app/outputs/step_05_dielectric_function_MgSe.csv`
- Format: csv
- Contract: Columns: Energy_eV, real_eps_ZZ, imag_eps_ZZ.
- Scoring: scored by hidden verifier

### Step 13: Absorption and reflectivity of MgS
- Role: scored
- Action: From the MgS dielectric function, derive the optical absorption coefficient and reflectivity spectrum and save to CSV.
- Output file: `/app/outputs/step_06_absorption_reflectivity_MgS.csv`
- Format: csv
- Contract: Columns: Energy_eV, absorption_coeff_cm-1, reflectivity_fraction.
- Scoring: scored by hidden verifier

### Step 14: Absorption and reflectivity of MgSe
- Role: scored
- Action: Same as step_13 but for MgSe.
- Output file: `/app/outputs/step_07_absorption_reflectivity_MgSe.csv`
- Format: csv
- Contract: Columns: Energy_eV, absorption_coeff_cm-1, reflectivity_fraction.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_summary_table.csv`
- `/app/outputs/step_02_band_gaps_zero_strain.json`
- `/app/outputs/step_03_strain_band_gap_PBE.csv`
- `/app/outputs/step_04_dielectric_function_MgS.csv`
- `/app/outputs/step_05_dielectric_function_MgSe.csv`
- `/app/outputs/step_06_absorption_reflectivity_MgS.csv`
- `/app/outputs/step_07_absorption_reflectivity_MgSe.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_summary_table.csv
- path: `/app/outputs/step_01_summary_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium structural parameters, cohesive energy, and HSE06 band gap for MgS and MgSe monolayers.
- schema:
  - `type`: table
  - `required_columns`: `Material`, `Lattice_constant_a(Angstrom)`, `Buckling_delta(Angstrom)`, `Bond_length_MgX(Angstrom)`, `Cohesive_energy(eV/atom)`, `HSE06_band_gap(eV)`
  - `units`:
    - `Lattice_constant_a(Angstrom)`: Angstrom
    - `Buckling_delta(Angstrom)`: Angstrom
    - `Bond_length_MgX(Angstrom)`: Angstrom
    - `Cohesive_energy(eV/atom)`: eV/atom
    - `HSE06_band_gap(eV)`: eV

### step_02_band_gaps_zero_strain.json
- path: `/app/outputs/step_02_band_gaps_zero_strain.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: PBE and HSE06 band gaps at zero strain for MgS and MgSe.
- schema:
  - `type`: object
  - `required`:
    - `MgS`:
      - `type`: object
      - `required`:
        - `PBE_gap`:
          - `type`: number
        - `HSE06_gap`:
          - `type`: number
    - `MgSe`:
      - `type`: object
      - `required`:
        - `PBE_gap`:
          - `type`: number
        - `HSE06_gap`:
          - `type`: number

### step_03_strain_band_gap_PBE.csv
- path: `/app/outputs/step_03_strain_band_gap_PBE.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: PBE band gap as a function of biaxial strain (-8% to +8%) for both materials. The checker verifies the presence and trend of the strain dependence (monotonic decrease for MgS under compression; increase up to -6% for MgSe).
- schema:
  - `type`: table
  - `required_columns`: `Material`, `Strain_percent`, `PBE_band_gap(eV)`
  - `units`:
    - `Strain_percent`: %
    - `PBE_band_gap(eV)`: eV

### step_04_dielectric_function_MgS.csv
- path: `/app/outputs/step_04_dielectric_function_MgS.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Complex dielectric function (out-of-plane) for MgS. The checker will compute the static dielectric constant from real part at zero energy and locate first two absorption peaks in imaginary part.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `real_eps_ZZ`, `imag_eps_ZZ`
  - `units`:
    - `Energy_eV`: eV
    - `real_eps_ZZ`: dimensionless
    - `imag_eps_ZZ`: dimensionless

### step_05_dielectric_function_MgSe.csv
- path: `/app/outputs/step_05_dielectric_function_MgSe.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Complex dielectric function (out-of-plane) for MgSe. Same checks as MgS.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `real_eps_ZZ`, `imag_eps_ZZ`
  - `units`:
    - `Energy_eV`: eV
    - `real_eps_ZZ`: dimensionless
    - `imag_eps_ZZ`: dimensionless

### step_06_absorption_reflectivity_MgS.csv
- path: `/app/outputs/step_06_absorption_reflectivity_MgS.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Absorption coefficient and reflectivity spectrum for MgS. Checker verifies near-zero absorption in visible region and peak positions.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `absorption_coeff_cm-1`, `reflectivity_fraction`
  - `units`:
    - `Energy_eV`: eV
    - `absorption_coeff_cm-1`: cm^-1
    - `reflectivity_fraction`: fraction

### step_07_absorption_reflectivity_MgSe.csv
- path: `/app/outputs/step_07_absorption_reflectivity_MgSe.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Absorption coefficient and reflectivity spectrum for MgSe.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `absorption_coeff_cm-1`, `reflectivity_fraction`
  - `units`:
    - `Energy_eV`: eV
    - `absorption_coeff_cm-1`: cm^-1
    - `reflectivity_fraction`: fraction

Notes: All values are compared to hidden paper‑reported values or verified for structural trends/tolerances. The summary table (step_01_summary_table.csv) is load‑bearing: it cannot be produced without running the preceding geometry optimization, isolated atom, and HSE06 calculations. The strain band gap table is scored via trend verification; the dielectric function and optical spectra via derived features (static constant, peak positions, relative heights). Near‑zero visible absorption is also checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_summary_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "Lattice_constant_a(Angstrom)",
          "Buckling_delta(Angstrom)",
          "Bond_length_MgX(Angstrom)",
          "Cohesive_energy(eV/atom)",
          "HSE06_band_gap(eV)"
        ],
        "units": {
          "Lattice_constant_a(Angstrom)": "Angstrom",
          "Buckling_delta(Angstrom)": "Angstrom",
          "Bond_length_MgX(Angstrom)": "Angstrom",
          "Cohesive_energy(eV/atom)": "eV/atom",
          "HSE06_band_gap(eV)": "eV"
        }
      },
      "description": "Equilibrium structural parameters, cohesive energy, and HSE06 band gap for MgS and MgSe monolayers."
    },
    {
      "file": "step_02_band_gaps_zero_strain.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "MgS": {
            "type": "object",
            "required": {
              "PBE_gap": {
                "type": "number"
              },
              "HSE06_gap": {
                "type": "number"
              }
            }
          },
          "MgSe": {
            "type": "object",
            "required": {
              "PBE_gap": {
                "type": "number"
              },
              "HSE06_gap": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "PBE and HSE06 band gaps at zero strain for MgS and MgSe."
    },
    {
      "file": "step_03_strain_band_gap_PBE.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "Strain_percent",
          "PBE_band_gap(eV)"
        ],
        "units": {
          "Strain_percent": "%",
          "PBE_band_gap(eV)": "eV"
        }
      },
      "description": "PBE band gap as a function of biaxial strain (-8% to +8%) for both materials. The checker verifies the presence and trend of the strain dependence (monotonic decrease for MgS under compression; increase up to -6% for MgSe)."
    },
    {
      "file": "step_04_dielectric_function_MgS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "real_eps_ZZ",
          "imag_eps_ZZ"
        ],
        "units": {
          "Energy_eV": "eV",
          "real_eps_ZZ": "dimensionless",
          "imag_eps_ZZ": "dimensionless"
        }
      },
      "description": "Complex dielectric function (out-of-plane) for MgS. The checker will compute the static dielectric constant from real part at zero energy and locate first two absorption peaks in imaginary part."
    },
    {
      "file": "step_05_dielectric_function_MgSe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "real_eps_ZZ",
          "imag_eps_ZZ"
        ],
        "units": {
          "Energy_eV": "eV",
          "real_eps_ZZ": "dimensionless",
          "imag_eps_ZZ": "dimensionless"
        }
      },
      "description": "Complex dielectric function (out-of-plane) for MgSe. Same checks as MgS."
    },
    {
      "file": "step_06_absorption_reflectivity_MgS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "absorption_coeff_cm-1",
          "reflectivity_fraction"
        ],
        "units": {
          "Energy_eV": "eV",
          "absorption_coeff_cm-1": "cm^-1",
          "reflectivity_fraction": "fraction"
        }
      },
      "description": "Absorption coefficient and reflectivity spectrum for MgS. Checker verifies near-zero absorption in visible region and peak positions."
    },
    {
      "file": "step_07_absorption_reflectivity_MgSe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "absorption_coeff_cm-1",
          "reflectivity_fraction"
        ],
        "units": {
          "Energy_eV": "eV",
          "absorption_coeff_cm-1": "cm^-1",
          "reflectivity_fraction": "fraction"
        }
      },
      "description": "Absorption coefficient and reflectivity spectrum for MgSe."
    }
  ],
  "notes": "All values are compared to hidden paper‑reported values or verified for structural trends/tolerances. The summary table (step_01_summary_table.csv) is load‑bearing: it cannot be produced without running the preceding geometry optimization, isolated atom, and HSE06 calculations. The strain band gap table is scored via trend verification; the dielectric function and optical spectra via derived features (static constant, peak positions, relative heights). Near‑zero visible absorption is also checked."
}
```

## How you are scored
Each scored artifact is checked by a hidden verifier program. For structural parameters, cohesive energy, and band gaps, the verifier compares your computed values to reference values with appropriate tolerances (values not disclosed here). For the strain-dependent band gaps, the verifier checks that the reported band gaps follow the expected monotonicity trends under strain (no exact values required). For the dielectric functions, the verifier computes the static dielectric constant and locates absorption peaks, comparing positions and relative heights to hidden reference features. For absorption and reflectivity, it verifies near-zero absorption in the visible region and consistency with the dielectric function. The final reward is a weighted combination of scores from all scored artifacts; reporting numbers that match the paper without genuine DFT computation will not pass because the verifier checks structural consistency and derived features, not mere self-reported scalars.
