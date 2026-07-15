# Thermoelectric Properties of Filled Skutterudite CeRu4Sb12

## Problem background
Filled skutterudite CeRu4Sb12 is a candidate thermoelectric material. Its thermoelectric efficiency depends on the electronic structure near the Fermi level, the elastic properties of the crystal lattice, and the transport of charge carriers. First-principles density functional theory (DFT) can predict the equilibrium structure, elastic constants, and band structure, while semiclassical Boltzmann transport theory can translate the electronic states into the Seebeck coefficient and thermoelectric figure of merit ZT. This task asks you to compute these quantities for CeRu4Sb12 using an open‑source DFT package and Boltztrap, thereby exploring how the material's electronic and mechanical features give rise to its thermoelectric performance.

## Approach
Use DFT to relax the CeRu4Sb12 crystal structure with the GGA (PBE) exchange‑correlation functional and fit the energy‑volume data to the Murnaghan equation of state to obtain the equilibrium lattice constant. Apply volume‑conserving strains to compute the three independent elastic constants (C11, C12, C44) of the cubic lattice, then derive isotropic mechanical parameters (bulk, shear, Young’s moduli, sound velocities, Debye temperature, Poisson’s ratio, anisotropy). Switch to the LDA functional for a self‑consistent electronic structure calculation; compute the band structure along high‑symmetry lines and the total/partial density of states to extract the indirect band gap. Feed the DFT band energies into Boltztrap under the constant relaxation time approximation to obtain the Seebeck coefficient S(T) from 0 to 300 K and the figure of merit ZT at 300 K. All steps build on the same relaxed crystal structure, forming an end‑to‑end computational pipeline from structure to thermoelectric response.

## Reproduction target
Using an open‑source DFT code (Quantum ESPRESSO, Elk, or similar) and Boltztrap, perform the following for cubic CeRu4Sb12 (space group Im-3, atomic positions: Ce at (0,0,0), Ru at (0.25,0.25,0.25), Sb at (0,0.35,0.16)).

1. **Structural and elastic properties**: Determine the equilibrium lattice constant a0 (Å) and the elastic constants C11, C12, C44 (GPa). Compute the derived isotropic parameters: bulk modulus B (GPa), shear modulus G (GPa), Young’s modulus Y (GPa), mean sound velocity V (m/s), Debye temperature θ_D (K), Poisson’s ratio ν (dimensionless), and anisotropy factor A (dimensionless). Write everything to `structural_properties.json` as a JSON object with numeric fields.
2. **Indirect band gap**: Extract the energy difference (eV) between the valence band maximum and conduction band minimum from the LDA band structure and write it as a single floating‑point number to `bandgap.txt`.
3. **Seebeck coefficient curve**: From the Boltztrap output, produce a two‑column CSV file `seebeck_curve.csv` with header `T(K),S(µV/K)` and at least 30 data points covering 0–300 K that capture the low‑temperature peak.
4. **Figure of merit at 300 K**: Write the computed ZT at 300 K as a single floating‑point number to `zt_300k.txt`.

All files must conform to the format specifications in the Output contract section.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Boltztrap: https://bitbucket.org/sousaw/boltztrap
- Crystal structure of CeRu4Sb12

## Workflow steps

### Step 1: DFT structural relaxation (GGA/PBE)
- Role: process
- Action: Perform DFT structural optimization of CeRu4Sb12 using the GGA (PBE) exchange-correlation functional. For a series of unit‑cell volumes, compute total energy and fit the energy–volume data to the Murnaghan equation of state to obtain the equilibrium lattice constant a0 and the optimized atomic positions.
- Evidence: `/app/outputs/relax_evidence.log`

### Step 2: Elastic constants calculation
- Role: process
- Action: Using the relaxed structure, apply volume-conserving strain patterns to compute the total energy changes; fit the strain‑energy data to the linear‑elastic relations for a cubic lattice to extract the three independent elastic constants C11, C12, and C44 (in GPa).
- Evidence: `/app/outputs/elastic_evidence.log`

### Step 3: Derive isotropic mechanical parameters
- Role: process
- Action: From C11, C12, C44, compute the isotropic moduli and other mechanical parameters using the standard formulas for cubic crystals: bulk modulus B, shear modulus G, Young’s modulus Y, mean sound velocity V, Debye temperature θ_D, Poisson’s ratio ν, and anisotropy factor A.
- Evidence: none

### Step 4: Structural and elastic properties report
- Role: scored
- Action: Write structural_properties.json containing the equilibrium lattice constant a0 (Å), the independent elastic constants C11, C12, C44, and the derived isotropic parameters B, G, Y (all in GPa), mean sound velocity V (m/s), Debye temperature θ_D (K), Poisson’s ratio ν (dimensionless), and anisotropy factor A (dimensionless).
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: JSON object with numeric fields: a0 (float, Å), C11 (float, GPa), C12 (float, GPa), C44 (float, GPa), B (float, GPa), G (float, GPa), Y (float, GPa), V (float, m/s), θ_D (float, K), ν (float, dimensionless), A (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: LDA electronic structure calculation
- Role: process
- Action: Perform a self‑consistent DFT calculation using the LDA exchange‑correlation functional on the relaxed structure. Compute the band structure along high‑symmetry directions and the total/partial density of states.
- Evidence: `/app/outputs/electronic_evidence.log`

### Step 6: Indirect band gap extraction
- Role: scored
- Action: Extract the indirect band gap (energy difference between the top of the valence band and the bottom of the conduction band) from the computed band structure and write it as a single floating‑point number (in eV) to bandgap.txt.
- Output file: `/app/outputs/bandgap.txt`
- Format: txt
- Contract: Text file containing a single floating‑point number (eV).
- Scoring: scored by hidden verifier

### Step 7: Boltzmann transport simulation
- Role: process
- Action: Using the DFT band structure (eigenvalues) as input, run the Boltztrap code under the constant relaxation time approximation to compute the Seebeck coefficient S(T) for temperatures 0–300 K and the thermoelectric figure of merit ZT at 300 K.
- Evidence: `/app/outputs/transport_evidence.log`

### Step 8: Seebeck coefficient curve
- Role: scored (load-bearing)
- Action: From the Boltztrap output, produce a CSV file seebeck_curve.csv with header "T(K),S(µV/K)" and rows covering at least the temperature range 0–300 K with sufficient density to capture the low‑temperature peak. The Seebeck coefficient is in µV/K.
- Output file: `/app/outputs/seebeck_curve.csv`
- Format: csv
- Contract: Two‑column CSV with header. First column: T(K) (numeric, K); second column: S(µV/K) (numeric, µV/K). At least 30 data points covering 0–300 K.
- Scoring: scored by hidden verifier

### Step 9: Thermoelectric figure of merit at 300 K
- Role: scored (load-bearing)
- Action: Extract the computed ZT at 300 K from the Boltztrap output and write it as a single floating‑point number to zt_300k.txt.
- Output file: `/app/outputs/zt_300k.txt`
- Format: txt
- Contract: Text file containing a single floating‑point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.json`
- `/app/outputs/bandgap.txt`
- `/app/outputs/seebeck_curve.csv`
- `/app/outputs/zt_300k.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constant, independent elastic constants, and derived isotropic mechanical parameters. Each value is compared to a hidden paper‑reported gold with a tolerance window.
- schema:
  - `type`: object
  - `required`: `a0`, `C11`, `C12`, `C44`, `B`, `G`, `Y`, `V`, `θ_D`, `ν`, `A`
  - `units`:
    - `a0`: Å
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `B`: GPa
    - `G`: GPa
    - `Y`: GPa
    - `V`: m/s
    - `θ_D`: K
    - `ν`: dimensionless
    - `A`: dimensionless

### bandgap.txt
- path: `/app/outputs/bandgap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Indirect band gap extracted from the LDA band structure. Compared to a hidden reference value ± 0.02 eV.
- schema:
  - `type`: text
  - `description`: A single floating‑point number representing the indirect band gap in eV.

### seebeck_curve.csv
- path: `/app/outputs/seebeck_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature‑dependent Seebeck coefficient S(T) from 0 to 300 K. The checker recomputes S at 80 K and 300 K, locates the peak, and verifies the curve shape; tolerances are applied to the extracted values.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `S(µV/K)`
  - `units`:
    - `T(K)`: K
    - `S(µV/K)`: µV/K

### zt_300k.txt
- path: `/app/outputs/zt_300k.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Thermoelectric figure of merit at room temperature. Compared to a hidden reference value ± 0.02.
- schema:
  - `type`: text
  - `description`: A single floating‑point number representing ZT at 300 K.

Notes: All scored outputs are compared to hidden reference values (paper‑reported gold) with tolerances. The Seebeck curve and ZT are load‑bearing, forcing honest execution of the electronic structure and transport calculations. Structural sanity checks (positive moduli, C11 > C12 > 0, C44 > 0, 0 < ν < 0.5, A positive) act as gating criteria in the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a0",
          "C11",
          "C12",
          "C44",
          "B",
          "G",
          "Y",
          "V",
          "θ_D",
          "ν",
          "A"
        ],
        "units": {
          "a0": "Å",
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "B": "GPa",
          "G": "GPa",
          "Y": "GPa",
          "V": "m/s",
          "θ_D": "K",
          "ν": "dimensionless",
          "A": "dimensionless"
        }
      },
      "description": "Equilibrium lattice constant, independent elastic constants, and derived isotropic mechanical parameters. Each value is compared to a hidden paper‑reported gold with a tolerance window."
    },
    {
      "file": "bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating‑point number representing the indirect band gap in eV."
      },
      "description": "Indirect band gap extracted from the LDA band structure. Compared to a hidden reference value ± 0.02 eV."
    },
    {
      "file": "seebeck_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "S(µV/K)"
        ],
        "units": {
          "T(K)": "K",
          "S(µV/K)": "µV/K"
        }
      },
      "description": "Temperature‑dependent Seebeck coefficient S(T) from 0 to 300 K. The checker recomputes S at 80 K and 300 K, locates the peak, and verifies the curve shape; tolerances are applied to the extracted values."
    },
    {
      "file": "zt_300k.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating‑point number representing ZT at 300 K."
      },
      "description": "Thermoelectric figure of merit at room temperature. Compared to a hidden reference value ± 0.02."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference values (paper‑reported gold) with tolerances. The Seebeck curve and ZT are load‑bearing, forcing honest execution of the electronic structure and transport calculations. Structural sanity checks (positive moduli, C11 > C12 > 0, C44 > 0, 0 < ν < 0.5, A positive) act as gating criteria in the checker."
}
```

## How you are scored
A hidden verifier independently scores each of the four output files (structural_properties.json, bandgap.txt, seebeck_curve.csv, zt_300k.txt) against undisclosed reference benchmarks and tolerances. Each file contributes equally (0.25) to the total reward, which is 1.0 for a perfect reproduction. The reward is monotonic in quality: a result that equals or surpasses the reference target earns full credit, and credit decreases only if your result is worse. Structural sanity checks (positive moduli, C11 > C12 > 0, C44 > 0, 0 < ν < 0.5, A > 0) are gating; if any fails, the total reward is zero. The Seebeck curve is evaluated not only at specific temperatures but also for the correct overall shape and peak location. Because the exact tolerances and reference values are hidden, you must perform the complete DFT + Boltztrap pipeline honestly — simply copying plausible numbers will not reproduce the required quantitative behavior.
