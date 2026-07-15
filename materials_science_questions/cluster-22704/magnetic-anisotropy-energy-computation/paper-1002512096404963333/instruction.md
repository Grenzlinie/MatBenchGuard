# Tunable magnetism in Nitride MXenes via stacking control

## Problem background
Two-dimensional Nitride MXenes of the form M₂NT₂ (M = Sc, Ti, V, Cr, Mn; T = O, F) can adopt two distinct atomic layer stackings: the conventional ABC stacking and the alternative ABA stacking. Changing the stacking pattern is expected to modify the magnetic and electronic ground states as well as the magnetic anisotropy. This task investigates these stacking-dependent properties by computing magnetic ground states, atomic magnetic moments, electronic ground state classifications, and magnetic anisotropy energies for the eight dynamically stable MXenes in both stacking configurations.

## Approach
The approach uses spin-polarized density functional theory with an on-site Coulomb correction (DFT+U) and spin-orbit coupling where needed. For each compound and stacking pattern, a 2×2×1 supercell is constructed and four magnetic arrangements (ferromagnetic FM, and antiferromagnetic AFM1, AFM2, AFM3) are compared. The total energy, site-projected magnetic moments, and spin-resolved density of states are computed from self-consistent DFT+U relaxations. The lowest-energy magnetic configuration is identified as the magnetic ground state. The electronic ground state is classified from the total density of states into metal, semiconductor, half-metal, or spin-gapless semiconductor. For each magnetic ground state, the magnetic anisotropy energy is obtained as the difference between in-plane and out-of-plane spin orientations from two additional DFT calculations including spin-orbit coupling. All calculations are performed with the PBE exchange-correlation functional, standard DFT+U parameters for each transition metal, and a van der Waals correction.

## Reproduction target
For each of the eight M₂NT₂ compounds (Sc₂NF₂, Sc₂NO₂, Ti₂NF₂, V₂NF₂, V₂NO₂, Cr₂NF₂, Cr₂NO₂, Mn₂NF₂) in both ABC and ABA stacking, determine and report the magnetic ground state among the four configurations FM, AFM1, AFM2, AFM3, the site-projected atomic magnetic moments on the two inequivalent transition metal sites (M^I, M^II) and on the nitrogen atom (N) in that ground state, the electronic ground state classification (metal, semiconductor, half-metal, spin-gapless_semiconductor), and the magnetic anisotropy energy per unit cell. Produce three CSV files summarizing these results for all compound–stacking combinations.

## Assets

- Open-source plane-wave DFT code (e.g. Quantum ESPRESSO): https://www.quantum-espresso.org/
- PAW pseudopotentials for PBE functional (PSlibrary or equivalent): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Prepare atomic structures and magnetic configurations
- Role: process
- Action: Construct the eight dynamically stable M2NT2 compounds (Sc2NF2, Sc2NO2, Ti2NF2, V2NF2, V2NO2, Cr2NF2, Cr2NO2, Mn2NF2) in both ABC stacking (HH functionalization) and ABA stacking (HH functionalization for Cr2NF2, Sc2NO2, Mn2NF2, Sc2NF2; CC functionalization for Cr2NO2, V2NO2, Ti2NF2, V2NF2 as per the known functionalization models). For each compound/stacking, create a 2×2×1 supercell and set up the four magnetic configurations FM, AFM1, AFM2, AFM3. Write input files for a plane-wave DFT code (e.g. Quantum ESPRESSO) ready for spin-polarized DFT+U calculations.
- Evidence: none

### Step 2: DFT+U calculations for ABC stacking
- Role: process
- Action: Run spin-polarized DFT+U calculations for all eight compounds in ABC stacking, for each of the four magnetic configurations (32 calculations in total). Use PBE functional, DFT+U with U values from the literature (Sc 3.0, Ti 4.0, V 3.0, Cr 4.0, Mn 4.0 eV), D3 van der Waals correction, a plane-wave cutoff of 600 eV, and a k-mesh sufficient for accurate total energies (e.g. 8×8×1 for relaxation, 18×18×1 for electronic structure). Optimize the atomic positions until forces are below 0.01 eV/Å and the total energy converges to 10⁻⁶ eV. Collect total energies, site-projected magnetic moments, and spin-resolved total densities of states (DOS).
- Evidence: none

### Step 3: DFT+U calculations for ABA stacking
- Role: process
- Action: Run the same DFT+U calculations as in step 2 (identical parameters) for the ABA stacking compounds (eight compounds, four magnetic configurations each, total 32 calculations). Collect total energies, site-projected magnetic moments, and spin-resolved total DOS.
- Evidence: none

### Step 4: Determine magnetic ground states and atomic moments
- Role: scored
- Action: From the total energies computed in steps 2 and 3, identify the magnetic ground state (the configuration with the lowest total energy) for each compound and stacking. Extract the site-projected magnetic moments (M^I, M^II, and N) in that ground state. Write the results to magnetic_ground_states.csv.
- Output file: `/app/outputs/magnetic_ground_states.csv`
- Format: csv
- Contract: compound (str), stacking (str: ABC/ABA), ground_state (str: FM/AFM1/AFM2/AFM3 or NM), M_I_moment (float, μ_B), M_II_moment (float, μ_B), N_moment (float, μ_B)
- Scoring: scored by hidden verifier

### Step 5: Classify electronic ground states from DOS
- Role: scored
- Action: For each compound and stacking, inspect the spin-resolved total DOS obtained from steps 2 and 3. Classify the electronic ground state as one of: metal, semiconductor, half-metal, spin-gapless_semiconductor. Write the results to electronic_ground_states.csv.
- Output file: `/app/outputs/electronic_ground_states.csv`
- Format: csv
- Contract: compound (str), stacking (str: ABC/ABA), electronic_state (str: metal/semiconductor/half-metal/spin-gapless_semiconductor)
- Scoring: scored by hidden verifier

### Step 6: Compute magnetic anisotropy energy (MAE)
- Role: scored (load-bearing)
- Action: For each compound/stacking in its magnetic ground state (excluding nonmagnetic cases), perform two additional DFT calculations with spin-orbit coupling (SOC): one with spins aligned in-plane and one with spins aligned out-of-plane, using the same PBE+U parameters and a dense k-mesh. Calculate the magnetic anisotropy energy as E(∥) − E(⊥) and report it in micro-eV per unit cell. Write the results to magnetic_anisotropy_energies.csv.
- Output file: `/app/outputs/magnetic_anisotropy_energies.csv`
- Format: csv
- Contract: compound (str), stacking (str: ABC/ABA), MAE_microeV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_ground_states.csv`
- `/app/outputs/electronic_ground_states.csv`
- `/app/outputs/magnetic_anisotropy_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_ground_states.csv
- path: `/app/outputs/magnetic_ground_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Magnetic ground state configuration and atomic magnetic moments for each compound and stacking. The hidden checker compares ground_state by exact match (FM/AFM1/AFM2/AFM3/NM) and the moments within an absolute tolerance of 0.1 μ_B.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `stacking`, `ground_state`, `M_I_moment`, `M_II_moment`, `N_moment`
  - `units`:
    - `M_I_moment`: μ_B
    - `M_II_moment`: μ_B
    - `N_moment`: μ_B

### electronic_ground_states.csv
- path: `/app/outputs/electronic_ground_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electronic ground state classification (metal, semiconductor, half-metal, spin-gapless_semiconductor) for each compound and stacking. Checked by exact match after string normalization.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `stacking`, `electronic_state`

### magnetic_anisotropy_energies.csv
- path: `/app/outputs/magnetic_anisotropy_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Magnetic anisotropy energy (in μeV) for each magnetic ground state. Checked against paper values with an absolute tolerance of 20 μeV.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `stacking`, `MAE_microeV`
  - `units`:
    - `MAE_microeV`: μeV per unit cell

Notes: All public outputs come from the agent's DFT+U and SOC calculations. The hidden checker uses the paper's Table II as the gold standard. The MAE step is load-bearing; a correct MAE can only be obtained by genuinely running the full workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_ground_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "stacking",
          "ground_state",
          "M_I_moment",
          "M_II_moment",
          "N_moment"
        ],
        "units": {
          "M_I_moment": "μ_B",
          "M_II_moment": "μ_B",
          "N_moment": "μ_B"
        }
      },
      "description": "Magnetic ground state configuration and atomic magnetic moments for each compound and stacking. The hidden checker compares ground_state by exact match (FM/AFM1/AFM2/AFM3/NM) and the moments within an absolute tolerance of 0.1 μ_B."
    },
    {
      "file": "electronic_ground_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "stacking",
          "electronic_state"
        ]
      },
      "description": "Electronic ground state classification (metal, semiconductor, half-metal, spin-gapless_semiconductor) for each compound and stacking. Checked by exact match after string normalization."
    },
    {
      "file": "magnetic_anisotropy_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "stacking",
          "MAE_microeV"
        ],
        "units": {
          "MAE_microeV": "μeV per unit cell"
        }
      },
      "description": "Magnetic anisotropy energy (in μeV) for each magnetic ground state. Checked against paper values with an absolute tolerance of 20 μeV."
    }
  ],
  "notes": "All public outputs come from the agent's DFT+U and SOC calculations. The hidden checker uses the paper's Table II as the gold standard. The MAE step is load-bearing; a correct MAE can only be obtained by genuinely running the full workflow."
}
```

## How you are scored
A hidden verifier will independently compare each entry in your output files to the expected values. For magnetic_ground_states.csv, the magnetic ground state label is compared exactly, and the atomic moments are compared with a small absolute tolerance. For electronic_ground_states.csv, the electronic state label is compared exactly after canonical normalization. For magnetic_anisotropy_energies.csv, each MAE value is compared with an absolute tolerance. The overall reward is a weighted combination of the fractional correctness across all compound–stacking rows. Missing, unreadable, or malformed output files will receive a reward of zero. The verifier does not reveal the expected values or specific tolerances; the best outcome is achieved by accurate computation.
