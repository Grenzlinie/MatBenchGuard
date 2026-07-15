# Quantum thermochemistry of metal hydroxide vapors

## Problem background
Accurate thermodynamic data for high-temperature metal hydroxide vapor species are essential for predicting material stability in combustion and turbine environments. The gaseous hydroxides and oxyhydroxides of aluminum, zirconium, and yttrium are formed when the refractory oxides react with water vapor, but experimental measurements for many of these species are limited or extremely challenging. This work addresses the need for reliable standard entropy, enthalpy of formation, and heat capacity for the dominant Al–OH, Zr–OH, and Y–OH vapor species using quantum chemistry methods. The task is to compute the missing thermodynamic quantities via a well-defined computational protocol, yielding a complete set of thermochemical data for 14 gas-phase species.

## Approach
The computational strategy uses a two-tier hierarchical approach. First, density functional theory (B3LYP) optimizations provide geometries, harmonic vibrational frequencies, and one-dimensional potential energy scans for the M–O–H bending angles and for the full 360° rotation of each –OH group. The bending potentials are treated anharmonically by solving the 1D Schrödinger equation; the torsional modes are corrected using the hindered rotor Pitzer–Gwinn approximation. Second, single-point coupled-cluster (CCSD(T)) calculations at the optimized geometries are performed with a series of correlation-consistent basis sets and extrapolated to the complete basis set (CBS) limit via the X⁻³ formula. Core-correlation effects are included: for Al species all electrons except Al 1s are correlated; for Zr and Y, the metal 4s4p are correlated while the deeper semicore (1s–3d) and O 1s are frozen. For the heavy metals, an all-electron Douglas–Kroll calculation is performed to obtain an AE–ECP correction that adjusts the effective core potential results. The final enthalpy of formation is derived from appropriate isodesmic or atomization-based reaction energies, with additional corrections for zero-point energy, spin–orbit coupling (element-specific constants), and known systematic errors in the computed atomization energies of H₂ and H₂O. The heat capacity at constant pressure is fitted to the polynomial form A + B·T + C·T² + D/T + E/T² over the relevant temperature range.

## Reproduction target
Produce a single JSON file, `thermo_data.json`, containing the computed thermodynamic data for all 14 target species: AlOH, AlO(OH), Al(OH)₂, Al(OH)₃, ZrOH, ZrOOH, Zr(OH)₂, Zr(OH)₃, ZrO(OH)₂, Zr(OH)₄, YOH, YO(OH), Y(OH)₂, Y(OH)₃. For each species, report: (i) the standard molar entropy at 298 K, S°(298), in J/(mol·K); (ii) the standard enthalpy of formation at 298 K, ΔfH°(298), in kJ/mol; and (iii) the heat capacity polynomial coefficients (A, B, C, D, E) for the fit Cp(T) = A + B·T + C·T² + D/T + E/T². The file must be a JSON array of 14 objects, each with the keys `species`, `S298`, `delta_f_H298`, and `Cp_polynomial` (an object containing `A`, `B`, `C`, `D`, `E` as numbers).

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Basis sets from EMSL Basis Set Exchange: https://www.basissetexchange.org/
- cclib: cclib
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: B3LYP geometry optimization, frequencies, and potential scans
- Role: process
- Action: For each of the 14 target species (AlOH, AlO(OH), Al(OH)2, Al(OH)3, ZrOH, ZrOOH, Zr(OH)2, Zr(OH)3, ZrO(OH)2, Zr(OH)4, YOH, YO(OH), Y(OH)2, Y(OH)3), perform B3LYP geometry optimization and harmonic frequency calculation using the basis sets prescribed in the computational protocol (aug-cc-pVTZ for Al; cc-pwCVTZ-PP for Y and Zr). Additionally, compute the M-O-H bending potential energy curve by fixing the angle and optimizing all other coordinates, and compute the full 360° torsional rotational potential of each -OH group. Collect the optimized geometries, harmonic frequencies, bending potential curves, and torsional rotational potential curves.
- Evidence: `/app/outputs/b3lyp_summary.json`

### Step 2: CCSD(T) reaction energies and CBS extrapolation
- Role: process
- Action: Using the B3LYP-optimized geometries, run CCSD(T) single-point energy calculations for each species with the basis set series (TZ, QZ, 5Z) as specified in the protocol. Extrapolate to the complete basis set (CBS) limit using the X^-3 formula. Apply the core-correlation treatments: for Al species, correlate all electrons except Al 1s; for Y and Zr species, correlate metal 4s and 4p but freeze metal 1s-3d and O 1s. For Y and Zr, also perform an all-electron (Douglas–Kroll) CCSD(T)/TZ calculation to compute the AE–ECP correction. Collect the final CBS reaction energies and the AE vs ECP corrections.
- Evidence: `/app/outputs/cc_energies.csv`

### Step 3: Compute thermodynamic functions and generate final table
- Role: scored (load-bearing)
- Action: From the B3LYP outputs: apply the hindered rotor Pitzer–Gwinn treatment to the torsional potentials; solve the 1D vibrational levels for the bending potentials to obtain anharmonic corrections; combine with harmonic frequencies to compute standard entropy at 298 K (S°(298)) and heat capacity (Cp) as a function of temperature. Using the CCSD(T) CBS reaction energies: add B3LYP zero-point energy corrections, spin-orbit corrections (0.9 kJ/mol for Al, 8.6 kJ/mol for Zr, 3.8 kJ/mol for Y), and the known systematic error corrections for H₂/H₂O atomization to obtain standard enthalpy of formation at 298 K (ΔfH°(298)). For Y and Zr species, correct the ECP-based reaction energy by the AE–ECP difference before deriving ΔfH°. Fit Cp(T) to the polynomial form A + B·T + C·T² + D/T + E/T². Write the final thermodynamic data for all 14 species to a JSON file.
- Output file: `/app/outputs/thermo_data.json`
- Format: json
- Contract: A JSON array of 14 objects. Each object has keys: species (string), S298 (number, unit J/(mol·K)), delta_f_H298 (number, unit kJ/mol), Cp_polynomial (object with numeric fields A, B, C, D, E representing the polynomial A + B*T + C*T^2 + D/T + E/T^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_data.json
- path: `/app/outputs/thermo_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic data for the 14 gas-phase hydroxide/oxyhydroxide species as computed by the full quantum chemistry protocol.
- schema:
  - `type`: array
  - `items`:
    - `species`: string
    - `S298`: number (J/(mol·K))
    - `delta_f_H298`: number (kJ/mol)
    - `Cp_polynomial`:
      - `A`: number
      - `B`: number
      - `C`: number
      - `D`: number
      - `E`: number

Notes: The hidden checker compares each species' S298, delta_f_H298, and the Cp polynomial coefficients to the paper-reported values in Table VI, using domain-appropriate tolerances. Only the species and numeric fields are checked; the ordering of array elements may differ.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "species": "string",
          "S298": "number (J/(mol·K))",
          "delta_f_H298": "number (kJ/mol)",
          "Cp_polynomial": {
            "A": "number",
            "B": "number",
            "C": "number",
            "D": "number",
            "E": "number"
          }
        }
      },
      "description": "Thermodynamic data for the 14 gas-phase hydroxide/oxyhydroxide species as computed by the full quantum chemistry protocol."
    }
  ],
  "notes": "The hidden checker compares each species' S298, delta_f_H298, and the Cp polynomial coefficients to the paper-reported values in Table VI, using domain-appropriate tolerances. Only the species and numeric fields are checked; the ordering of array elements may differ."
}
```

## How you are scored
A hidden verifier reads your `thermo_data.json` and independently compares each species' S298, delta_f_H298, and Cp polynomial coefficients (A, B, C, D, E) against trusted reference values derived from the original study's published results. Your overall reward is the fraction of the 14 species for which all three metric groups (entropy, enthalpy, and the five Cp coefficients) simultaneously fall within the verifier's predetermined tolerances. A species receives credit only when every one of its numbers is acceptable; no partial credit is given for a species where some values pass and others do not. To earn any positive score, you must successfully provide entries for at least 12 of the 14 species. The verifier does not reveal the reference numbers or tolerance bounds; they are based solely on the quantitative data reported in the primary literature. Reporting arbitrary numbers is insufficient—only genuine computational reproduction of the described pipeline will produce values that satisfy the hidden criteria.
