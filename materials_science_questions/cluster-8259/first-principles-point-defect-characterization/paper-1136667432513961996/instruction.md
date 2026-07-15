# Defect-induced switchable polarization in non-ferroelectric perovskite

## Problem background
Perovskite SrTiO3 is non-ferroelectric at room temperature, yet recent experiments on Ti-rich/Sr-poor thin films have observed ferroelectric-like polarization switching. First‑principles density‑functional theory (DFT) is used to investigate whether intrinsic point defects — specifically the Ti antisite (Ti_Sr) and its complex with a Sr vacancy (Ti_Sr+V_Sr) — can generate a spontaneous polarization comparable to conventional ferroelectrics, and whether the polarization is switchable. Revealing the underlying defect-driven mechanism is crucial for defect‑engineered memory and sensing applications.

## Approach
The investigation employs spin‑polarized DFT with the HSE06 hybrid functional (α=25% for pristine bulk, α=20% for defect calculations) and the modern theory of polarization (Berry phase). The workflow first characterizes a pristine 2×2×2 SrTiO3 supercell in the anti‑ferrodistortive (AFD) P1 phase (a⁻a⁻a⁻ octahedral tilt) to establish a reference polarization and electronic band gap. Then, defect supercells containing either a neutral Ti_Sr antisite or a compensated Ti_Sr+V_Sr defect complex are constructed and fully relaxed. From the relaxed structures, the electronic band structure and magnetic moment of neutral Ti_Sr are computed to determine whether localized mid‑gap states appear. The net defect‑induced polarization of the compensated complex is obtained by subtracting the pristine reference from its Berry‑phase polarization. Finally, energy barriers for switching the Ti_Sr defect from its equilibrium site to symmetry‑equivalent sites (A–B and A–C pathways) are computed by linearly interpolating atomic positions and performing constrained relaxations along each path. All steps are carried out with HSE(20) and spin polarization for defect calculations.

## Reproduction target
Execute the DFT workflow described in the steps below and produce a final JSON file `results.json` that contains the following computed quantities:
- Polarization of the compensated Ti_Sr+V_Sr complex (μC/cm²)
- Energy barrier for switching neutral Ti_Sr along the A–B path (eV)
- Energy barrier for switching the compensated Ti_Sr+V_Sr complex along the A–B path (eV)
- Magnetic moment of neutral Ti_Sr (μB)
- Boolean indicating whether two localized mid‑gap states are present in neutral Ti_Sr
- Pristine AFD P1 band gap (eV, reported for information but not scored)

## Assets

- DFT code with HSE06 hybrid functional and Berry phase polarization calculation: quantum-espresso (or equivalent via pip/conda)
- Pseudopotential library for Sr, Ti, O: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Pristine AFD P1 reference
- Role: process
- Action: Relax the 2×2×2 SrTiO₃ supercell in the AFD P1 phase (a⁻a⁻a⁻ tilt) using HSE06 with α=20% and spin polarization. Compute the electronic band gap (eV) and the Berry phase spontaneous polarization vector (μC/cm²). Save both to pristine.json.
- Evidence: `/app/outputs/pristine.json`

### Step 2: Defect supercell construction and relaxation
- Role: process
- Action: Construct 2×2×2 supercells containing (a) one Ti_Sr antisite defect (neutral) and (b) one Ti_Sr+V_Sr defect complex (compensated). Relax both supercells fully (atomic positions + lattice parameters) with HSE06 (α=20%) and spin polarization. Save the relaxed structures for subsequent analysis.
- Evidence: `/app/outputs/relaxed_defects.out`

### Step 3: Neutral Ti_Sr electronic structure analysis
- Role: process
- Action: Compute the electronic band structure and total magnetic moment of the relaxed neutral Ti_Sr supercell. Determine whether two localized mid‑gap states appear (occupied defect states inside the band gap). Save the magnetic moment (μB) and a boolean (true if two localized mid‑gap states exist) to neutral_analysis.json.
- Evidence: `/app/outputs/neutral_analysis.json`

### Step 4: Polarization of compensated Ti_Sr+V_Sr complex
- Role: process
- Action: Compute the spontaneous polarization of the relaxed compensated Ti_Sr+V_Sr supercell via Berry phase, then subtract the pristine reference polarization (from step‑1) to obtain the net defect‑induced polarization magnitude. Save the net polarization (μC/cm²) to polarization.json.
- Evidence: `/app/outputs/polarization.json`

### Step 5: Energy barrier A–B for neutral Ti_Sr
- Role: process
- Action: Set up the A→B switching path for the neutral Ti_Sr defect. Generate intermediate images by linear interpolation of atomic positions between sites A and B, then relax all atomic coordinates and lattice parameters while constraining the Ti_Sr position and a reference Sr atom. Record the total energy for each image; extract the barrier as max energy minus initial energy (eV). Save to barrier_neutral.json.
- Evidence: `/app/outputs/barrier_neutral.json`

### Step 6: Energy barrier A–B for compensated Ti_Sr+V_Sr
- Role: process
- Action: Similarly, compute the energy barrier for the A→B switching path of the compensated Ti_Sr+V_Sr complex using the same protocol (linear interpolation + constrained relaxation). Save the barrier (eV) to barrier_compensated.json.
- Evidence: `/app/outputs/barrier_compensated.json`

### Step 7: Compile final scored results
- Role: scored (load-bearing)
- Action: Gather the computed values: polarization from polarization.json, barrier for neutral Ti_Sr from barrier_neutral.json, barrier for compensated complex from barrier_compensated.json, magnetic moment and mid‑gap boolean from neutral_analysis.json. Also read the pristine band gap from pristine.json (informational). Assemble results.json containing the required fields and submit it.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "polarization_TiSr_VSr_compensated_muC_per_cm2": "float",
  "barrier_A_B_neutral_TiSr_eV": "float",
  "barrier_A_B_compensated_eV": "float",
  "magnetic_moment_neutral_TiSr_muB": "float",
  "has_localized_midgap_states_neutral_TiSr": "bool",
  "pristine_band_gap_eV": "float"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final scored artifact containing the headline quantities: polarization of compensated complex, switching barriers, magnetic moment, presence of localized mid-gap states, and the pristine band gap (informational, not scored).
- schema:
  - `type`: object
  - `required`: `polarization_TiSr_VSr_compensated_muC_per_cm2`, `barrier_A_B_neutral_TiSr_eV`, `barrier_A_B_compensated_eV`, `magnetic_moment_neutral_TiSr_muB`, `has_localized_midgap_states_neutral_TiSr`, `pristine_band_gap_eV`
  - `properties`:
    - `polarization_TiSr_VSr_compensated_muC_per_cm2`:
      - `type`: number
    - `barrier_A_B_neutral_TiSr_eV`:
      - `type`: number
    - `barrier_A_B_compensated_eV`:
      - `type`: number
    - `magnetic_moment_neutral_TiSr_muB`:
      - `type`: number
    - `has_localized_midgap_states_neutral_TiSr`:
      - `type`: boolean
    - `pristine_band_gap_eV`:
      - `type`: number

Notes: Only results.json is scored. The process-step evidence files (pristine.json, relaxed_defects.out, neutral_analysis.json, polarization.json, barrier_neutral.json, barrier_compensated.json) are not directly scored but are required to produce the final values. The hidden gold values and tolerances are defined in grading_spec.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "polarization_TiSr_VSr_compensated_muC_per_cm2",
          "barrier_A_B_neutral_TiSr_eV",
          "barrier_A_B_compensated_eV",
          "magnetic_moment_neutral_TiSr_muB",
          "has_localized_midgap_states_neutral_TiSr",
          "pristine_band_gap_eV"
        ],
        "properties": {
          "polarization_TiSr_VSr_compensated_muC_per_cm2": {
            "type": "number"
          },
          "barrier_A_B_neutral_TiSr_eV": {
            "type": "number"
          },
          "barrier_A_B_compensated_eV": {
            "type": "number"
          },
          "magnetic_moment_neutral_TiSr_muB": {
            "type": "number"
          },
          "has_localized_midgap_states_neutral_TiSr": {
            "type": "boolean"
          },
          "pristine_band_gap_eV": {
            "type": "number"
          }
        }
      },
      "description": "Final scored artifact containing the headline quantities: polarization of compensated complex, switching barriers, magnetic moment, presence of localized mid-gap states, and the pristine band gap (informational, not scored)."
    }
  ],
  "notes": "Only results.json is scored. The process-step evidence files (pristine.json, relaxed_defects.out, neutral_analysis.json, polarization.json, barrier_neutral.json, barrier_compensated.json) are not directly scored but are required to produce the final values. The hidden gold values and tolerances are defined in grading_spec.json."
}
```

## How you are scored
A hidden verifier reads your submitted `results.json` and compares each field against a set of hidden reference values with predetermined tolerances. The scored quantities are the net polarization of the compensated complex, the two switching barriers, the magnetic moment, and the presence of two localized mid‑gap states (boolean). The pristine band gap is reported for information but does not affect the final score. Per‑field agreements are combined into an overall reward in the range [0,1]; meeting the expected range yields full credit, while increasing deviations reduce the score. You must produce only the required fields in the exact format specified in the output contract; do not include extra data or attempt to guess the hidden reference values.
