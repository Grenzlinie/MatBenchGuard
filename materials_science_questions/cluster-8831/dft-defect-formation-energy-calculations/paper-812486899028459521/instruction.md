# Ab Initio Defect Formation and Partitioning of Hf in MgSiO3 Bridgmanite

## Problem background
Recent geochemical studies reveal a wide range of ¹⁸²W isotopic anomalies in mantle-derived rocks, with both positive and negative deviations from the bulk silicate Earth value. One hypothesis is that these anomalies arise from deep silicate fractionation during the crystallization of a basal magma ocean while the short-lived parent ¹⁸²Hf (half-life 8.9 Myr) was still alive. In this scenario, Hf is partitioned between solid bridgmanite and silicate melt at high pressure, leading to ¹⁸²W heterogeneities that depend on the partition coefficient D_Hf and on the timing and extent of crystallization. However, the substitution mechanism of Hf in bridgmanite and the pressure dependence of D_Hf at lower-mantle conditions are unknown. This task uses first-principles calculations to determine the energetically preferred substitution site for Hf in MgSiO₃ bridgmanite, compute D_Hf as a function of pressure and temperature, and model the resulting tungsten isotopic evolution during basal magma ocean solidification.

## Approach
The approach combines three computational stages. (1) Density functional theory (DFT) calculations for MgSiO₃ bridgmanite supercells with Hf defects, using static relaxations, quasi-harmonic phonon free-energy corrections, and density functional perturbation theory (DFPT) to compute defect formation Gibbs free energies and the macroscopic dielectric constant. By comparing the formation energies of Hf on the Mg site versus the Si site, the preferred substitution mechanism is identified at lower-mantle pressures. (2) First-principles molecular dynamics (FPMD) simulations for pure and Hf-bearing (using the substitution mechanism found to be favorable from the defect formation energy analysis) solid bridgmanite and MgSiO₃ melt at several lower-mantle pressure–temperature conditions. Helmholtz free energy differences are obtained via thermodynamic integration, yielding the Gibbs free energy of the exchange reaction and the Hf partition coefficient D_Hf. (3) A geochemical model of basal magma ocean crystallization that uses the computed D_Hf to solve for the time evolution of Hf and W concentrations and the resulting μ¹⁸²W anomalies in both solid and liquid reservoirs.

## Reproduction target
The reproduction target is to compute and output three artifacts:
(a) The difference in defect formation energies ΔG = ΔG_f(Hf_Mg··) – ΔG_f(Hf_Si×) in MgSiO₃ bridgmanite at T = 2000 K for pressures from 25 to 140 GPa at two Hf concentrations (283 ppb and 732 ppm).
(b) The partition coefficient of Hf between bridgmanite and silicate melt, D_Hf, at multiple pressure–temperature conditions: 3000 K (31, 50, 93, 129 GPa), 4000 K (31, 58, 101, 140 GPa), and 5000 K (66, 109, 144 GPa).
(c) The evolution of the tungsten isotopic anomaly μ¹⁸²W (in ppm deviations) over 0–4.5 Gyr in solid and liquid reservoirs produced by a basal magma ocean crystallization model that uses the computed D_Hf, with batch melt formation at 50 Myr, initial thickness 850 km, melt fraction 0.8, cooling timescale 887 Myr, and D_W/D_Hf = 0.43.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- SSSP PBEsol efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/pbesol/efficiency
- MgSiO3 bridgmanite crystal structure
- CP2K: https://www.cp2k.org/

## Workflow steps

### Step 1: Gibbs free energies of pure and defect bridgmanite supercells
- Role: process
- Action: Set up supercells (e.g., 32 formula units) for pure MgSiO3 bridgmanite and Hf-substituted systems (Hf on Mg site and Hf on Si site). Perform DFT static relaxations at target pressures to obtain static enthalpies. Compute phonon free energies via quasi-harmonic approximation to obtain Gibbs free energies G(P,T) for solid phases at 2000 K.
- Evidence: `/app/outputs/energy_phonon_output.txt`

### Step 2: Macroscopic dielectric constant of bridgmanite
- Role: process
- Action: Compute the static macroscopic dielectric constant (electronic and ionic contributions) of MgSiO3 bridgmanite using density functional perturbation theory (DFPT).
- Evidence: `/app/outputs/dielectric_constant.txt`

### Step 3: Defect formation energy difference ΔG
- Role: scored (load-bearing)
- Action: Using the Gibbs free energies from previous steps, chemical potentials from charge neutrality and Hf concentration equations (283 ppb and 732 ppm), and finite-size corrections (Makov–Payne with the dielectric constant), compute the defect formation energy difference ΔG = ΔG_f(Hf_Mg··) − ΔG_f(Hf_Si×) at T = 2000 K for pressures from 25 to 140 GPa. Output a CSV with columns: pressure_GPa, concentration, delta_G_eV.
- Output file: `/app/outputs/defect_formation_energy_difference.csv`
- Format: csv
- Contract: columns: pressure_GPa (float), concentration (string: '283_ppb' or '732_ppm'), delta_G_eV (float)
- Scoring: scored by hidden verifier

### Step 4: First-principles molecular dynamics and thermodynamic integration
- Role: process
- Action: Set up pure and Hf-bearing (using the favorable substitution mechanism determined in Step 3) supercells for solid bridgmanite and MgSiO3 melt. Run first-principles molecular dynamics at the following P,T conditions: 3000 K: 31, 50, 93, 129 GPa; 4000 K: 31, 58, 101, 140 GPa; 5000 K: 66, 109, 144 GPa. Collect time-averaged potential energies for undoped and doped systems. Perform thermodynamic integration (linear or cubic method) to obtain the Helmholtz free energy difference ΔF for the exchange reaction.
- Evidence: `/app/outputs/thermo_integration_raw.csv`

### Step 5: Hf partition coefficient D_Hf compilation
- Role: scored (load-bearing)
- Action: From the free energy differences obtained in the previous step, compute the Hf partition coefficient D_Hf = exp(-ΔG_R/(k_B T)) for each P,T condition. Output a CSV with columns: pressure_GPa, temperature_K, D_Hf.
- Output file: `/app/outputs/hafnium_partition_coefficient.csv`
- Format: csv
- Contract: columns: pressure_GPa (float), temperature_K (float), D_Hf (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 6: Geochemical model of tungsten isotopic evolution
- Role: scored
- Action: Implement the basal magma ocean crystallization model: batch melt at t_i = 50 Myr, initial thickness 850 km, melt fraction F = 0.8, cooling timescale τ = 887 Myr, D_W/D_Hf = 0.43, using the computed D_Hf from step4 at representative basal magma ocean conditions (~100 GPa, 4000 K). Solve the differential equations for Hf and W evolution and compute μ¹⁸²W (ppm) for solid and liquid reservoirs over 0–4.5 Gyr. Output a CSV with columns: time_Myr, mu182W_solid_ppm, mu182W_liquid_ppm.
- Output file: `/app/outputs/tungsten_anomaly_evolution.csv`
- Format: csv
- Contract: columns: time_Myr (float), mu182W_solid_ppm (float), mu182W_liquid_ppm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_formation_energy_difference.csv`
- `/app/outputs/hafnium_partition_coefficient.csv`
- `/app/outputs/tungsten_anomaly_evolution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_formation_energy_difference.csv
- path: `/app/outputs/defect_formation_energy_difference.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Difference in defect formation energies between Hf on Mg site and Si site in bridgmanite at 2000 K.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `concentration`, `delta_G_eV`
  - `units`:
    - `pressure_GPa`: GPa
    - `delta_G_eV`: eV

### hafnium_partition_coefficient.csv
- path: `/app/outputs/hafnium_partition_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hf partition coefficient between bridgmanite and silicate melt at multiple P,T conditions.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `temperature_K`, `D_Hf`
  - `units`:
    - `pressure_GPa`: GPa
    - `temperature_K`: K
    - `D_Hf`: dimensionless

### tungsten_anomaly_evolution.csv
- path: `/app/outputs/tungsten_anomaly_evolution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tungsten isotopic anomaly evolution for solid and liquid reservoirs.
- schema:
  - `type`: table
  - `required_columns`: `time_Myr`, `mu182W_solid_ppm`, `mu182W_liquid_ppm`
  - `units`:
    - `time_Myr`: Myr
    - `mu182W_solid_ppm`: ppm
    - `mu182W_liquid_ppm`: ppm

Notes: Hidden scoring will compare submitted values to paper-reported references with tolerances (e.g., ±0.2 eV for ΔG, factor-of-2 for D_Hf, 30% relative for μ¹⁸²W) and also check internal consistency (e.g., D_Hf increases with pressure).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_formation_energy_difference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "concentration",
          "delta_G_eV"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "delta_G_eV": "eV"
        }
      },
      "description": "Difference in defect formation energies between Hf on Mg site and Si site in bridgmanite at 2000 K."
    },
    {
      "file": "hafnium_partition_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "temperature_K",
          "D_Hf"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "temperature_K": "K",
          "D_Hf": "dimensionless"
        }
      },
      "description": "Hf partition coefficient between bridgmanite and silicate melt at multiple P,T conditions."
    },
    {
      "file": "tungsten_anomaly_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_Myr",
          "mu182W_solid_ppm",
          "mu182W_liquid_ppm"
        ],
        "units": {
          "time_Myr": "Myr",
          "mu182W_solid_ppm": "ppm",
          "mu182W_liquid_ppm": "ppm"
        }
      },
      "description": "Tungsten isotopic anomaly evolution for solid and liquid reservoirs."
    }
  ],
  "notes": "Hidden scoring will compare submitted values to paper-reported references with tolerances (e.g., ±0.2 eV for ΔG, factor-of-2 for D_Hf, 30% relative for μ¹⁸²W) and also check internal consistency (e.g., D_Hf increases with pressure)."
}
```

## How you are scored
Your solution will be scored by a hidden verifier that examines each scored output file. The verifier holds reference values for the defect formation energy difference ΔG, the partition coefficient D_Hf, and the μ¹⁸²W evolution curves, and compares your submitted numbers against those references with tolerances that account for the use of different DFT codes, implementations, and numerical settings. In addition to value-based comparisons, the verifier checks internal consistency requirements — for example, that D_Hf increases monotonically with pressure at each temperature. The overall reward is a weighted combination of the scores from the three scored artifacts. Reporting the paper's published numbers without performing the required computations is not sufficient; your artifacts must be the product of the workflow steps described in this instruction.
