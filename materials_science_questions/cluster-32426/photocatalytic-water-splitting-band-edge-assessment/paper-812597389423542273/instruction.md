# Computational Reproduction of Electronic, Optical and Thermoelectric Properties of Janus-like TiMoCO2 MXene

## Problem background
Two-dimensional MXene alloys are emerging materials for sustainable energy applications, offering tunable compositions that can be tailored for photocatalytic water-splitting and thermoelectric conversion. A fully O-terminated Janus-like MXene alloy with asymmetric stacking (O(fcc)-Ti-C-Mo-O(hcp)) has been proposed as a candidate structure that may combine suitable band edge alignment, strong visible-infrared optical absorption, and competitive thermoelectric performance. The task is to compute the key electronic, optical, and thermoelectric properties of this alloy using an open-source first-principles workflow, to verify whether its predicted performance metrics meet the requirements for high-efficiency photocatalysis and thermoelectricity.

## Approach
The reproduction follows a first-principles computational pipeline: (1) construct the Janus-like TiMoCO2 crystal structure and relax it using density functional theory (DFT) with the PBE exchange–correlation functional; (2) recalculate the electronic band structure with the hybrid HSE06 functional to obtain an accurate band gap; (3) compute the frequency-dependent dielectric function and the optical absorption coefficient, then integrate with the AM1.5G solar spectrum to derive the maximum short-circuit current density; (4) perform density-functional perturbation theory (DFPT) to obtain phonon dispersions and electron–phonon matrix elements; (5) use the self-energy relaxation time approximation (SERTA) within EPW to compute intrinsic electron and hole mobilities; and (6) within the rigid-band approximation, shift the Fermi level to simulate n- and p-type doping and evaluate the thermoelectric power factor as a function of carrier concentration. The entire workflow is to be executed with open-source codes (Quantum ESPRESSO and EPW) and publicly available ONCV pseudopotentials.

## Reproduction target
Compute the following quantities for the Janus-like TiMoCO2 MXene alloy using the workflow described above: (1) the HSE06 fundamental band gap (in eV), written to band_gap.txt; (2) the maximum short-circuit current density (in mA cm⁻²) under AM1.5G illumination, written to short_circuit_current.txt; (3) the room-temperature intrinsic drift mobilities (in cm² V⁻¹ s⁻¹) for electrons and holes along the in-plane x and y directions, written to mobility.csv; and (4) the thermoelectric power factor (in μW cm⁻¹ K⁻²) as a function of carrier concentration (cm⁻³) at 300 K for both n-type and p-type doping, covering at least 50 logarithmically spaced concentrations from 1×10¹⁸ to 1×10²¹ cm⁻³, written to power_factor_vs_N.csv.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW code (Electron-Phonon Wannier): https://epw-code.org/
- ONCV pseudopotentials (PseudoDojo): http://www.pseudo-dojo.org/
- AM1.5G solar spectrum (ASTM G173-03): https://www.nrel.gov/grid/solar-resource/spectra-am1.5.html

## Workflow steps

### Step 1: Build and relax TiMoCO₂ Janus-like structure
- Role: process
- Action: Construct the Janus-like TiMoCO₂ MXene alloy with space group P3m1 (no.156) and stacking O(fcc)-Ti-C-Mo-O(hcp). Perform full DFT structural relaxation using the PBE functional until forces are converged. Produce the relaxed crystal structure.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 2: HSE06 band gap calculation
- Role: scored
- Action: Using the relaxed structure, perform a hybrid functional (HSE06) calculation to obtain the electronic band structure and density of states, and determine the fundamental band gap. Write the value to a text file.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single line containing the band gap in eV as a floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Optical absorption and maximum short-circuit current
- Role: scored
- Action: Calculate the frequency-dependent dielectric function using HSE06 eigenvalues, derive the in-plane optical absorption coefficient, and integrate it with the AM1.5G solar spectrum to obtain the maximum short-circuit current density. Write the value to a text file.
- Output file: `/app/outputs/short_circuit_current.txt`
- Format: txt
- Contract: A single line containing the short-circuit current density in mA/cm² as a floating-point number.
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion and electron-phonon Wannierization
- Role: process
- Action: Perform DFPT phonon calculation on a coarse q-grid, then compute maximally localized Wannier functions and interpolate phonon dispersions and electron-phonon matrix elements to fine k and q grids using EPW, preparing inputs for transport calculations.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 5: Intrinsic carrier mobility computation
- Role: scored
- Action: Using the self-energy relaxation time approximation (SERTA) within EPW, compute the room-temperature intrinsic electron and hole drift mobilities along the in-plane x and y directions. Output the mobilities to a CSV file with columns type, direction, and mobility.
- Output file: `/app/outputs/mobility.csv`
- Format: csv
- Contract: CSV with header: type, direction, mobility. type is 'electron' or 'hole'; direction is 'x' or 'y'; mobility is a floating-point number in cm² V⁻¹ s⁻¹. Exactly four data rows (electron/x, electron/y, hole/x, hole/y).
- Scoring: scored by hidden verifier

### Step 6: Thermoelectric power factor vs doping
- Role: scored (load-bearing)
- Action: Within the rigid-band approximation, shift the Fermi level to simulate n-type and p-type doping, and compute the Seebeck coefficient, electrical conductivity, and power factor S²σ as functions of carrier concentration at 300 K. Output the power factor data to a CSV file with at least 50 logarithmically spaced concentration points from 1×10¹⁸ to 1×10²¹ cm⁻³.
- Output file: `/app/outputs/power_factor_vs_N.csv`
- Format: csv
- Contract: CSV with header: doping_type, carrier_concentration, power_factor_x, power_factor_y. doping_type is 'n' or 'p'; carrier_concentration is a floating-point number in cm⁻³; power_factor_x and power_factor_y are floating-point numbers in μW cm⁻¹ K⁻² (for p-type they are identical). The file must contain at least 50 rows for each doping type, with logarithmically spaced concentrations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/short_circuit_current.txt`
- `/app/outputs/mobility.csv`
- `/app/outputs/power_factor_vs_N.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: HSE06 fundamental band gap

### short_circuit_current.txt
- path: `/app/outputs/short_circuit_current.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum short-circuit current density

### mobility.csv
- path: `/app/outputs/mobility.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electron and hole mobilities

### power_factor_vs_N.csv
- path: `/app/outputs/power_factor_vs_N.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Thermoelectric power factor vs carrier concentration

Notes: All outputs generated by the agent must be placed in /app/outputs. The verifier reads them directly from that directory.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {},
      "description": "HSE06 fundamental band gap"
    },
    {
      "file": "short_circuit_current.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {},
      "description": "Maximum short-circuit current density"
    },
    {
      "file": "mobility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {},
      "description": "Electron and hole mobilities"
    },
    {
      "file": "power_factor_vs_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {},
      "description": "Thermoelectric power factor vs carrier concentration"
    }
  ],
  "notes": "All outputs generated by the agent must be placed in /app/outputs. The verifier reads them directly from that directory."
}
```

## How you are scored
Each output file is independently evaluated by a hidden automated verifier. The verifier reads your submitted files, extracts the required numbers or curves, and compares them against a hidden set of expected values and tolerances. For scalar outputs (band gap, short-circuit current), closeness to the reference within a tolerance contributes to the score. For the mobility CSV, the verifier checks the presence of four rows with correct labels and verifies that the mobility values fall within a reference range. For power_factor_vs_N.csv, the verifier extracts the peak power factor and the corresponding optimal carrier concentration for each doping type and compares them to the expected values; it may also evaluate the power factor at randomly selected hidden carrier concentrations. Your final score is a weighted sum of the scores from all scored stages, with the power factor stage carrying the largest weight. Importing the values directly from the literature without performing the actual calculations will result in a low or zero score.
