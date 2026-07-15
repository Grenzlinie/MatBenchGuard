# Phonon-based stability and thermoelectric ZT of CaS/CaSe heterobilayer

## Problem background
Thermoelectric materials convert waste heat directly into electricity, offering a route to improve energy efficiency. Calcium chalcogenide monolayers, particularly CaS and CaSe in a hexagonal honeycomb structure, have recently been identified as promising thermoelectric candidates. Stacking these layers to form a hybrid CaS/CaSe bilayer may alter the structural, vibrational, electronic, and transport properties, potentially yielding a material that maintains a high thermoelectric figure of merit over a wide temperature range. This task investigates that possibility by producing the key quantities that characterize the thermoelectric performance of the heterostructure.

## Approach
The investigation uses first‑principles density functional theory (DFT) combined with semiclassical Boltzmann transport theory. The DFT calculations are performed with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and Grimme’s D2 dispersion correction, as implemented in Quantum ESPRESSO. After relaxing the hybrid CaS/CaSe bilayer (AB‑stacked, with initial lattice constant 4.7860 Å and interlayer spacing 2.77 Å), the phonon dispersion is computed to assess dynamical stability. The electronic band structure is obtained on a dense k‑mesh and used to determine the indirect band gap. The band eigenvalues are then fed into BoltzTraP, which solves the Boltzmann transport equation under the constant scattering time approximation (CSTA) and rigid band approximation (RBA), yielding the Seebeck coefficient, electrical and thermal conductivities, and the figure of merit ZT over the temperature range 50–1200 K. The workflow yields three independently verifiable results: (i) a stability verdict, (ii) the indirect band gap, and (iii) the ZT values at selected temperatures.

## Reproduction target
Reproduce the dynamical stability, indirect band gap, and temperature‑dependent figure of merit ZT for the hybrid CaS/CaSe bilayer. Specifically: (1) determine whether the structure is dynamically stable (no imaginary phonon frequencies) and write the verdict; (2) compute the indirect band gap in eV; (3) compute ZT at 300, 600, 900, and 1200 K and report the values in a CSV file. The verifier will check that the ZT values are consistent with stable performance across the wide temperature range and will validate the trend over the four temperatures.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP: https://www.boltzstrap.org/
- PBE ultrasoft pseudopotentials for Ca, S, Se (GBRV library or equivalent): https://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: DFT geometry relaxation for hybrid CaS/CaSe bilayer
- Role: process
- Action: Using Quantum ESPRESSO, perform a DFT-D2 (PBE + Grimme D2) geometry relaxation of the hybrid CaS/CaSe bilayer. The initial structure has lattice constant a=4.7860 Å, interlayer spacing d=2.77 Å, AB stacking, and sufficient vacuum. The relaxed atomic positions and cell parameters are the foundation for all later steps.
- Evidence: `/app/outputs/relaxed_structure.txt`

### Step 2: Phonon dispersion calculation
- Role: process
- Action: On the relaxed structure, compute the phonon dispersion along the high-symmetry path using density functional perturbation theory (or finite differences) in Quantum ESPRESSO to obtain phonon frequencies.
- Evidence: `/app/outputs/phonon_freq.txt`

### Step 3: Phonon stability assessment
- Role: scored
- Action: From the phonon dispersion data, determine whether the structure is dynamically stable (no imaginary frequencies, within a small numerical tolerance). Write the verdict to phonon_stability.txt.
- Output file: `/app/outputs/phonon_stability.txt`
- Format: txt
- Contract: A single line containing either the string 'stable' or the string 'unstable'.
- Scoring: scored by hidden verifier

### Step 4: Electronic band structure calculation
- Role: process
- Action: Using the relaxed structure, perform a self-consistent field (SCF) calculation and then compute the electronic band structure along the high-symmetry path (K‑Γ‑M‑K) with Quantum ESPRESSO. Output the eigenvalues needed for the band gap and for BoltzTraP.
- Evidence: `/app/outputs/band_eigenvalues.dat`

### Step 5: Report indirect band gap
- Role: scored
- Action: From the band structure, identify the valence band maximum (VBM) and conduction band minimum (CBM) and write the indirect band gap in eV to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single number representing the indirect band gap in eV.
- Scoring: scored by hidden verifier

### Step 6: BoltzTraP transport calculation
- Role: process
- Action: Feed the SCF band structure eigenvalues into BoltzTraP and run it under the constant scattering time approximation (CSTA) and rigid band approximation (RBA) for the temperature range 50–1200 K. Produce temperature-dependent electrical conductivity, thermal conductivity, Seebeck coefficient, and ZT.
- Evidence: `/app/outputs/boltz_output.txt`

### Step 7: Report ZT values
- Role: scored (load-bearing)
- Action: Extract the figure of merit ZT at 300, 600, 900, and 1200 K from the BoltzTraP output and write them to zt_vs_temperature.csv.
- Output file: `/app/outputs/zt_vs_temperature.csv`
- Format: csv
- Contract: CSV with two columns: Temperature(K) (integer) and ZT (float). At least the rows 300,600,900,1200 must be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_stability.txt`
- `/app/outputs/band_gap.txt`
- `/app/outputs/zt_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_stability.txt
- path: `/app/outputs/phonon_stability.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Verdict of dynamical stability: 'stable' if no imaginary phonon frequencies, otherwise 'unstable'.
- schema:
  - `type`: text
  - `description`: A single line containing either the string 'stable' or 'unstable'.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The indirect band gap of the hybrid CaS/CaSe bilayer.
- schema:
  - `type`: text
  - `units`: eV
  - `description`: A single number representing the indirect band gap in eV.

### zt_vs_temperature.csv
- path: `/app/outputs/zt_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature-dependent figure of merit ZT at 300, 600, 900, and 1200 K; checked for range [0.8,1.0] and non-decreasing trend within noise.
- schema:
  - `type`: table
  - `required_columns`: `Temperature(K)`, `ZT`
  - `units`:
    - `Temperature(K)`: K
    - `ZT`: dimensionless

Notes: The phonon stability and band gap are computed directly from DFT results. The ZT check relies on the expected stable performance over a wide temperature range; a correct reproduction should show ZT values within the specified range and a flat or gently increasing trend, consistent with the paper's claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_stability.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line containing either the string 'stable' or 'unstable'."
      },
      "description": "Verdict of dynamical stability: 'stable' if no imaginary phonon frequencies, otherwise 'unstable'."
    },
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "eV",
        "description": "A single number representing the indirect band gap in eV."
      },
      "description": "The indirect band gap of the hybrid CaS/CaSe bilayer."
    },
    {
      "file": "zt_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature(K)",
          "ZT"
        ],
        "units": {
          "Temperature(K)": "K",
          "ZT": "dimensionless"
        }
      },
      "description": "Temperature-dependent figure of merit ZT at 300, 600, 900, and 1200 K; checked for range [0.8,1.0] and non-decreasing trend within noise."
    }
  ],
  "notes": "The phonon stability and band gap are computed directly from DFT results. The ZT check relies on the expected stable performance over a wide temperature range; a correct reproduction should show ZT values within the specified range and a flat or gently increasing trend, consistent with the paper's claim."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that examines the output files you write under /app/outputs. Each scored artifact (phonon_stability.txt, band_gap.txt, zt_vs_temperature.csv) is checked independently: the stability verdict is compared against the expected answer, the band gap is compared to a hidden reference value (with a tolerance that accounts for legitimate implementation differences), and the ZT file is validated for shape, required rows, and consistency with expected range and trend. The verifier then combines the scores from each artifact, weighted according to their importance, into a single reward between 0 and 1. You do not need to guess any hidden thresholds; simply follow the computational protocol as described.
