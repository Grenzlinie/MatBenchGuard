# First-Principles Charge Transport in Li2S2

## Problem background
In lithium–sulfur (Li–S) batteries, solid discharge products such as Li2S and Li2S2 deposit on the cathode during discharge, potentially passivating the active surface and raising impedance. While Li2S is known to be an electronic insulator, the charge-transport properties of the intermediate solid Li2S2 remain poorly understood. Crystalline Li2S2 can exist in a p1 structure, but it is not clear whether this phase can support free-electron conduction or whether native defects and polarons enable charge transport. Understanding the dominant charge carriers and their mobility is critical for designing cathodes that mitigate passivation and improve battery rate capability.

## Approach
Use first-principles density functional theory (DFT) to investigate the electronic structure and defect properties of p1 Li2S2. Compute the electronic band gap with both PBE and HSE06 functionals to determine whether the material is a semiconductor. Then model four native charged defects: negatively charged lithium vacancies (VLi−), positively charged S2 dimer vacancies (VS22+), electron polarons (p−), and hole polarons (p+). Relax each defect in a supercell at the HSE06 level and evaluate their formation energies using appropriate chemical potentials. Next, calculate diffusion barriers for each defect along the three principal crystallographic directions ([100], [010], [001]) via the climbing-image nudged elastic band method. From the lowest barrier hops, estimate mobilities using the Einstein relation (D = ν d² exp(−ΔE/kT) with ν = 10¹³ s⁻¹) and combine with defect concentrations derived from formation energies to estimate the ionic conductivity (from VLi− diffusion) and electronic conductivity (from p+ diffusion) at 300 K. Compare the two conductivities to infer which carrier mechanism dominates charge transport in Li2S2.

## Reproduction target
Obtain the p1 Li2S2 crystal structure from public sources. Build a (3×3×2) supercell. Perform the following computations and write the specified output files:

1. Band gaps: Report PBE and HSE06 band gaps in band_gaps.txt.
2. Defect formation energies: For VLi−, VS22+, p−, and p+, output a CSV with defect_type and formation_energy_eV.
3. Diffusion barriers: For each defect and each orientation [100], [010], [001], output a CSV with defect_type, orientation, barrier_eV.
4. Conductivity summary: At T = 300 K, report mobility and conductivity for p+ and VLi− in conductivity_summary.csv.

You must run the complete workflow using the open-source DFT code Quantum ESPRESSO and publicly available pseudopotentials. The goal is to produce a self-consistent set of computed properties that allow identifying the dominant charge transport mechanism in Li2S2.

## Assets

- p1 Li2S2 crystal structure: From the supporting information of Feng et al., J. Power Sources 2014, DOI 10.1016/j.jpowsour.2014.08.118
- Quantum ESPRESSO: Open-source DFT code, https://www.quantum-espresso.org/
- SSSP efficiency PAW pseudopotentials: PBE- and HSE-compatible pseudopotential files from the SSSP library, https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare crystal structure and supercell
- Role: process
- Action: Obtain the p1 Li2S2 crystal structure (atomic positions and lattice vectors) from the public source (Feng et al., J. Power Sources 2014). Construct a (3×3×2) supercell for defect calculations. Prepare the necessary input files for Quantum ESPRESSO (primitive cell and supercell).
- Evidence: none

### Step 2: Compute band gaps (PBE and HSE06)
- Role: scored
- Action: Perform DFT electronic-structure calculations on the pristine Li2S2 primitive cell using Quantum ESPRESSO with the PBE and HSE06 exchange-correlation functionals. Extract the band gap values (conduction band minimum minus valence band maximum). Write the results to band_gaps.txt with two lines: PBE_bandgap_eV = <float> and HSE06_bandgap_eV = <float>.
- Output file: `/app/outputs/band_gaps.txt`
- Format: txt
- Contract: Two lines formatted as '<functional>_bandgap_eV = <float>'. Example: PBE_bandgap_eV = 1.5  (value not revealed).
- Scoring: scored by hidden verifier

### Step 3: Relax charged defect and polaron supercells
- Role: process
- Action: Construct supercells for the four charged species: VLi− (remove one Li, charge −1), VS22+ (remove one S2 dimer, charge +2), electron polaron p− (add one electron), hole polaron p+ (remove one electron). Relax the geometry of each defect supercell using HSE06 (or equivalent hybrid) DFT in Quantum ESPRESSO. Record the final total energies.
- Evidence: none

### Step 4: Calculate formation energies
- Role: scored
- Action: From the relaxed total energies of pristine and defect supercells, and using appropriate chemical potentials (e.g., bulk Li metal and α-S reference energies), compute the formation energies of VLi−, VS22+, p−, and p+ with a charge-neutrality Fermi level. Write a CSV file defect_formation_energies.csv with columns defect_type (string) and formation_energy_eV (float). Include at least the four charged defects.
- Output file: `/app/outputs/defect_formation_energies.csv`
- Format: csv
- Contract: CSV with header: defect_type,formation_energy_eV. Each row gives the defect name and its formation energy in eV.
- Scoring: scored by hidden verifier

### Step 5: Compute diffusion barriers via CI-NEB
- Role: process
- Action: For each defect (VLi−, VS22+, p−, p+) and each crystallographic direction [100], [010], [001], set up initial and final configurations for the migration path and run climbing-image nudged-elastic-band (CI-NEB) calculations in Quantum ESPRESSO. Extract the energy barrier (activation energy) for each path.
- Evidence: none

### Step 6: Write diffusion barriers
- Role: scored
- Action: Collect the computed diffusion barriers. Write a CSV file diffusion_barriers.csv with columns defect_type (string), orientation (string, e.g., [100], [010], [001]), barrier_eV (float). Include all four defect species for at least the three orientations mentioned in the paper.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: CSV with header: defect_type,orientation,barrier_eV. Example row: V_Li-,[001],0.148
- Scoring: scored by hidden verifier

### Step 7: Compute mobilities and conductivities
- Role: scored (load-bearing)
- Action: Use the diffusion barriers from step04b and the Einstein relation (D = ν d² exp(−ΔE/kT) with ν = 10¹³ s⁻¹, hopping distance d derived from crystal structure) to estimate the mobility μ = eD/(kT). For VLi− and p+, estimate the concentration c = c₀ exp(−Ef/kT) from the formation energies (step03b) and compute the conductivity σ = c e μ at T = 300 K. Write a CSV file conductivity_summary.csv with columns charge_carrier (string), mobility_cm2_Vs (float), conductivity_S_cm (float), temperature_K (float). Include at least entries for p+ and VLi−.
- Output file: `/app/outputs/conductivity_summary.csv`
- Format: csv
- Contract: CSV with header: charge_carrier,mobility_cm2_Vs,conductivity_S_cm,temperature_K. Example row: p+,1.0e-01,1.0e-12,300
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.txt`
- `/app/outputs/defect_formation_energies.csv`
- `/app/outputs/diffusion_barriers.csv`
- `/app/outputs/conductivity_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.txt
- path: `/app/outputs/band_gaps.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Semiconductor band gap values from PBE and HSE06 functionals.
- schema:
  - `type`: text
  - `description`: Two lines with keys 'PBE_bandgap_eV' and 'HSE06_bandgap_eV' followed by ' = ' and a float value.

### defect_formation_energies.csv
- path: `/app/outputs/defect_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of charged native defects and polarons.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Diffusion barrier energies for defects and polarons along different crystallographic directions.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `orientation`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

### conductivity_summary.csv
- path: `/app/outputs/conductivity_summary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Mobility and conductivity estimates for the main charge carriers at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `charge_carrier`, `mobility_cm2_Vs`, `conductivity_S_cm`, `temperature_K`
  - `units`:
    - `mobility_cm2_Vs`: cm²/(V·s)
    - `conductivity_S_cm`: S/cm
    - `temperature_K`: K

Notes: Scoring is based on structural trends (T3): PBE band gap < HSE06 band gap and both > 1.0 eV; VLi− and p+ have lowest formation energies (≤1.5 eV) and neutral vacancies are higher; p+ barriers ≤0.1 eV, VLi− barriers <1 eV, VS22+ barriers >0.4 eV, and p+ is the smallest; p+ mobility >> VLi− mobility (factor ≥10⁸) and electronic conductivity >> ionic conductivity at 300 K. Exact values are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Two lines with keys 'PBE_bandgap_eV' and 'HSE06_bandgap_eV' followed by ' = ' and a float value."
      },
      "description": "Semiconductor band gap values from PBE and HSE06 functionals."
    },
    {
      "file": "defect_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energies of charged native defects and polarons."
    },
    {
      "file": "diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "orientation",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Diffusion barrier energies for defects and polarons along different crystallographic directions."
    },
    {
      "file": "conductivity_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "charge_carrier",
          "mobility_cm2_Vs",
          "conductivity_S_cm",
          "temperature_K"
        ],
        "units": {
          "mobility_cm2_Vs": "cm²/(V·s)",
          "conductivity_S_cm": "S/cm",
          "temperature_K": "K"
        }
      },
      "description": "Mobility and conductivity estimates for the main charge carriers at 300 K."
    }
  ],
  "notes": "Scoring is based on structural trends (T3): PBE band gap < HSE06 band gap and both > 1.0 eV; VLi− and p+ have lowest formation energies (≤1.5 eV) and neutral vacancies are higher; p+ barriers ≤0.1 eV, VLi− barriers <1 eV, VS22+ barriers >0.4 eV, and p+ is the smallest; p+ mobility >> VLi− mobility (factor ≥10⁸) and electronic conductivity >> ionic conductivity at 300 K. Exact values are not required."
}
```

## How you are scored
A hidden verifier will independently inspect each of the four scored artifacts. It will apply structural and trend-based checks (T3 scoring) that verify physically expected relationships – for example, that the band gap is consistent with a semiconductor, that certain defects have the lowest formation energies, that the diffusion barriers exhibit a plausible ordering, and that the estimated mobilities and conductivities follow the expected trends. The verifier does not expect exact numerical coincidence with any specific code; it checks that your results are physically reasonable and capture the key relative features that establish the dominant charge carrier. Each artifact contributes a weighted portion of the final reward (0–1). Simply reporting known numbers from the literature without executing the workflow will not satisfy the verifier.
