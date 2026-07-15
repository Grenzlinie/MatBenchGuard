# Phonon-based phase boundary prediction for MgGeO3

## Problem background
MgGeO3 is a low‑pressure analog for key Earth‑forming silicate minerals. Predicting its high‑pressure, high‑temperature phase transitions among the ilmenite, perovskite, and postperovskite structures provides crucial constraints for mineral physics models. First‑principles phonon calculations within the local density approximation (LDA) and the quasiharmonic approximation offer a route to compute finite‑temperature phase boundaries and Clapeyron slopes, and to test whether the LiNbO3 structure appears as a stable intermediate.

## Approach
The computational approach uses density functional theory (LDA) with density functional perturbation theory (DFPT) to obtain phonon dispersions and vibrational densities of states for the four MgGeO3 polymorphs: ilmenite, perovskite, postperovskite, and LiNbO3. Quasiharmonic free energy calculations combine static total energies with vibrational free energy contributions to yield Helmholtz free energy F(V,T) for each phase. Gibbs free energies G(P,T) are then constructed, and phase boundaries are located by the condition ΔG = 0 between competing phases. Clapeyron slopes dP/dT are derived from the temperature dependence of the transition pressures or from the ratio ΔS/ΔV. The thermodynamic stability of LiNbO3 relative to ilmenite is assessed by comparing their Gibbs free energies over a wide pressure‑temperature range.

## Reproduction target
Perform the DFT+DFPT+QHA workflow to produce three scored artifacts:
- `transition_pressures_300K.json`: the ilmenite→perovskite and perovskite→postperovskite transition pressures in GPa at T = 300 K.
- `clapeyron_slopes_1000K.json`: the Clapeyron slopes dP/dT in MPa/K at T = 1000 K for both transitions.
- `linbo3_metastability_verification.txt`: a one‑line statement summarizing whether LiNbO3 has any thermodynamic stability field over the range 0–60 GPa and 0–2000 K.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP LDA ultrasoft pseudopotentials for Mg, Ge, O: https://www.materialscloud.org/discover/sssp/
- Python scientific stack: numpy scipy matplotlib ase

## Workflow steps

### Step 1: DFT static energy-volume calculations
- Role: process
- Action: Perform LDA DFT static calculations for ilmenite, LiNbO3, perovskite, and postperovskite phases of MgGeO3 at several volumes. For each phase, relax the structure and compute total energy at each volume.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 2: DFPT phonon dispersion and VDOS
- Role: process
- Action: Using the relaxed structures from Step 1, perform density functional perturbation theory (DFPT) calculations to obtain phonon dispersions and vibrational densities of states (VDOS) for each phase at each volume.
- Evidence: `/app/outputs/phonon_dispersion.log`

### Step 3: Quasiharmonic Helmholtz free energy
- Role: process
- Action: Combine the static energies and VDOS to compute Helmholtz free energy F(V,T) for each phase in the quasiharmonic approximation (QHA) for a range of temperatures.
- Evidence: `/app/outputs/qha_free_energy.log`

### Step 4: LDA transition pressures at 300 K
- Role: scored (load-bearing)
- Action: From the Gibbs free energies G(P,T) = F(V,T) + P(V,T)V, determine the ilmenite→perovskite and perovskite→postperovskite transition pressures at T = 300 K by locating the pressures where ΔG between the phases equals zero. Write the two pressures (in GPa) to a JSON file.
- Output file: `/app/outputs/transition_pressures_300K.json`
- Format: json
- Contract: {"type":"object","required":{"ilmenite_perovskite_Pt_GPa":"number","perovskite_postperovskite_Pt_GPa":"number"}}
- Scoring: scored by hidden verifier

### Step 5: Clapeyron slopes at 1000 K
- Role: scored (load-bearing)
- Action: Compute the Clapeyron slopes dP/dT for both phase boundaries at T = 1000 K using either dΔG/dT or ΔS/ΔV derived from the QHA data. Write the slopes (in MPa/K) to a JSON file.
- Output file: `/app/outputs/clapeyron_slopes_1000K.json`
- Format: json
- Contract: {"type":"object","required":{"ilmenite_perovskite_dPdT_MPa_K":"number","perovskite_postperovskite_dPdT_MPa_K":"number"}}
- Scoring: scored by hidden verifier

### Step 6: LiNbO3 metastability verification
- Role: scored
- Action: Compare the Gibbs free energy of LiNbO3 with that of ilmenite over the pressure range 0–60 GPa and temperature range 0–2000 K. Determine whether LiNbO3 has a thermodynamic stability field (i.e., any P,T where its G is lower than ilmenite's). Write a single‑line statement summarizing your findings.
- Output file: `/app/outputs/linbo3_metastability_verification.txt`
- Format: txt
- Contract: {"type":"text"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_pressures_300K.json`
- `/app/outputs/clapeyron_slopes_1000K.json`
- `/app/outputs/linbo3_metastability_verification.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_pressures_300K.json
- path: `/app/outputs/transition_pressures_300K.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Transition pressures at 300 K for ilmenite→perovskite and perovskite→postperovskite.
- schema:
  - `type`: object
  - `required`:
    - `ilmenite_perovskite_Pt_GPa`: number
    - `perovskite_postperovskite_Pt_GPa`: number

### clapeyron_slopes_1000K.json
- path: `/app/outputs/clapeyron_slopes_1000K.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Clapeyron slopes at 1000 K for the two phase boundaries.
- schema:
  - `type`: object
  - `required`:
    - `ilmenite_perovskite_dPdT_MPa_K`: number
    - `perovskite_postperovskite_dPdT_MPa_K`: number

### linbo3_metastability_verification.txt
- path: `/app/outputs/linbo3_metastability_verification.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Statement confirming LiNbO3 is metastable over 0-60 GPa and 0-2000 K.
- schema:
  - `type`: text

Notes: The checker compares reported pressures and slopes against reference values within tolerances, and verifies the metastability statement indicates a positive ΔG between LiNbO3 and ilmenite.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_pressures_300K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ilmenite_perovskite_Pt_GPa": "number",
          "perovskite_postperovskite_Pt_GPa": "number"
        }
      },
      "description": "Transition pressures at 300 K for ilmenite→perovskite and perovskite→postperovskite."
    },
    {
      "file": "clapeyron_slopes_1000K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ilmenite_perovskite_dPdT_MPa_K": "number",
          "perovskite_postperovskite_dPdT_MPa_K": "number"
        }
      },
      "description": "Clapeyron slopes at 1000 K for the two phase boundaries."
    },
    {
      "file": "linbo3_metastability_verification.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Statement confirming LiNbO3 is metastable over 0-60 GPa and 0-2000 K."
    }
  ],
  "notes": "The checker compares reported pressures and slopes against reference values within tolerances, and verifies the metastability statement indicates a positive ΔG between LiNbO3 and ilmenite."
}
```

## How you are scored
A hidden verifier inspects your three output files independently. Transition pressures and Clapeyron slopes are compared to reference values with predetermined tolerances; meeting or exceeding the threshold earns full credit for those components. The metastability verification is checked for a positive ΔG(LiNbO3−ilmenite) statement over the specified range. Each scored artifact contributes to the final reward (transition pressures weight 0.4, Clapeyron slopes 0.4, metastability verification 0.2). The total reward is a float in [0,1]. Completing the DFT+DFPT+QHA workflow is required; simply reporting numbers from an external source will not satisfy the verifier.
