# Charge carrier dynamics from DFT and NAMD in cobalt-doped graphitic carbon nitride

## Problem background
Single-atom catalysts on graphitic carbon nitride (GCN) have shown enhanced photocatalytic performance. Cobalt doping is reported to introduce occupied midgap states that act as hole traps and oxidation centers, affecting charge carrier dynamics. Understanding the balance between charge separation and recombination is critical for photocatalytic efficiency. This task investigates the electronic structure and nonadiabatic carrier dynamics of a Co-doped GCN system to quantify the time scales of hole trapping (charge separation) and electron-hole recombination, and to determine whether separation outpaces recombination.

## Approach
The computational approach combines first-principles density functional theory (DFT) with nonadiabatic molecular dynamics (NAMD). A structural model of Co-doped GCN is first optimized using spin-polarized DFT with a Hubbard U correction on Co 3d states and a van der Waals functional appropriate for layered materials. The DFT electronic structure is obtained with both a semilocal functional (PBE+U) and a hybrid functional (HSE06) to correct the well-known band gap underestimation. Adiabatic molecular dynamics is then run to sample the vibrational motion, from which energy gaps and nonadiabatic couplings between band-edge and defect states are extracted. These couplings are scaled using the HSE06/PBE+U gap ratio to approximate the hybrid-functional values. Finally, NAMD simulations are performed using the decoherence-induced surface hopping (DISH) algorithm to model photoexcited charge carrier relaxation. The populations of excited, trapped, and ground states are tracked, and exponential fits yield the characteristic time scales for charge separation (hole trapping) and recombination, including statistical uncertainties.

## Reproduction target
Produce the following scored outputs for the Co-GCN system: (1) an electronic structure summary containing the PBE+U and HSE-scaled band gaps, and a list of midgap defect states with their energies relative to the valence band maximum and occupation status for both spin channels; (2) a table of canonically averaged energy gaps and absolute nonadiabatic couplings (raw and scaled) between the key orbital pairs in the spin-down channel; (3) a table of charge carrier dynamics time scales (excited-state decay, trapped-hole rise, ground-state rise) and their uncertainties for both spin-up and spin-down channels. The outputs must be written as described in the workflow steps and adhere to the declared file formats and schemas.

## Assets

- DFT code with spin-polarized PBE+U, vdW correction, and MD (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PYXAID: https://github.com/Quantum-Dynamics-Hub/PYXAID
- CA-NAC: https://github.com/Quantum-Dynamics-Hub/CA-NAC
- GCN lattice parameters from literature (Gao et al., J. Phys. Chem. C 2020): 10.1021/acs.jpcc.9b11639

## Workflow steps

### Step 1: Geometry optimization of Co-GCN
- Role: process
- Action: Build a 2×2 supercell of heptazine-based graphitic carbon nitride (GCN) with a single Co atom at the cavity center coordinated to two hydroxy groups. Perform spin-polarized DFT geometry optimization using PBE+U (U_eff=3.0 eV on Co 3d) with optB86b-vdW correction and plane-wave basis. Relax atomic positions until forces are below the convergence threshold. Save the relaxed structure for subsequent steps.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Electronic structure summary and midgap states
- Role: scored (load-bearing)
- Action: Using the optimized geometry, compute spin-polarized electronic structure (PDOS, orbital energies) with PBE+U and HSE06 (or scale the PBE+U gap using an HSE06 reference). Identify the band gap and the energies of all midgap defect states relative to the valence band maximum for the spin-up and spin-down channels. Determine whether each midgap state is occupied. Output a structured JSON file containing the band gaps and the list of midgap states with their properties.
- Output file: `/app/outputs/electronic_summary.json`
- Format: json
- Contract: {"type": "object", "required": ["bandgap_PBEpU", "bandgap_HSEscaled", "midgap_states"], "properties": {"bandgap_PBEpU": {"type": "number", "units": "eV"}, "bandgap_HSEscaled": {"type": "number", "units": "eV"}, "midgap_states": {"type": "array", "items": {"type": "object", "required": ["spin", "state_label", "energy_rel_VBM", "occupied"], "properties": {"spin": {"type": "string"}, "state_label": {"type": "string"}, "energy_rel_VBM": {"type": "number", "units": "eV"}, "occupied": {"type": "boolean"}}}}}}
- Scoring: scored by hidden verifier

### Step 3: Canonically averaged energy gaps and nonadiabatic couplings
- Role: scored
- Action: Run adiabatic molecular dynamics at 300 K for 5 ps on the optimized geometry using spin-polarized PBE+U DFT. For the spin-down channel, extract the energy gaps and nonadiabatic couplings (NAC) between VBM, defect states d1, d2, d3, and CBM at each MD step. Compute canonically averaged raw (PBE+U) energies and NAC, then scale them using the HSE06/PBE+U gap ratio to obtain the final scaled values. Output a CSV with the averaged raw and scaled energies and NAC for each orbital pair as required.
- Output file: `/app/outputs/table1_energy_nac.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["orbitals", "energy", "scaled_energy", "NAC", "scaled_NAC"], "units": {"energy": "eV", "scaled_energy": "eV", "NAC": "meV", "scaled_NAC": "meV"}}
- Scoring: scored by hidden verifier

### Step 4: Charge carrier dynamics time scales from NAMD
- Role: scored
- Action: Perform nonadiabatic molecular dynamics (NAMD) using the DISH algorithm as implemented in PYXAID with the scaled NA Hamiltonian from the previous step. Simulate charge carrier dynamics for both spin-up and spin-down channels independently, using 100 random initial configurations and 100 stochastic DISH trajectories per configuration (effective ~1 ns total). Track excited state (ES), trapped hole, and ground state (GS) populations. Fit the relevant portions of the population curves to exponential functions to extract time scales for ES decay, trapped hole rise, and GS rise, including uncertainties estimated from trajectory sub-sets. Report the fitted time constants and their uncertainties in a CSV.
- Output file: `/app/outputs/table2_timescales.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["spin", "process", "timescale_ps", "uncertainty_ps"], "units": {"timescale_ps": "ps", "uncertainty_ps": "ps"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_summary.json`
- `/app/outputs/table1_energy_nac.csv`
- `/app/outputs/table2_timescales.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_summary.json
- path: `/app/outputs/electronic_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic structure summary containing the band gap values and a list of midgap defect states with their energies relative to VBM and occupation status, required to verify the existence of occupied hole-trap states.
- schema:
  - `type`: object
  - `required`: `bandgap_PBEpU`, `bandgap_HSEscaled`, `midgap_states`
  - `properties`:
    - `bandgap_PBEpU`:
      - `type`: number
      - `units`: eV
    - `bandgap_HSEscaled`:
      - `type`: number
      - `units`: eV
    - `midgap_states`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `spin`, `state_label`, `energy_rel_VBM`, `occupied`
        - `properties`:
          - `spin`:
            - `type`: string
          - `state_label`:
            - `type`: string
          - `energy_rel_VBM`:
            - `type`: number
            - `units`: eV
          - `occupied`:
            - `type`: boolean

### table1_energy_nac.csv
- path: `/app/outputs/table1_energy_nac.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Canonically averaged energy gaps and nonadiabatic couplings for spin-down channel state pairs, used to validate the raw and scaled electronic coupling inputs for the dynamics.
- schema:
  - `type`: table
  - `required_columns`: `orbitals`, `energy`, `scaled_energy`, `NAC`, `scaled_NAC`
  - `units`:
    - `energy`: eV
    - `scaled_energy`: eV
    - `NAC`: meV
    - `scaled_NAC`: meV

### table2_timescales.csv
- path: `/app/outputs/table2_timescales.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted time scales for charge separation (hole trapping) and recombination from NAMD simulations for both spin channels, including statistical uncertainties, to verify the claim that charge separation is significantly faster than recombination.
- schema:
  - `type`: table
  - `required_columns`: `spin`, `process`, `timescale_ps`, `uncertainty_ps`
  - `units`:
    - `timescale_ps`: ps
    - `uncertainty_ps`: ps

Notes: The verifier compares the submitted numeric values against hidden reference values derived from the paper’s reported results, applying appropriate tolerances for the chosen functional and basis set. The electronic_summary must contain at least one occupied midgap state in each spin channel. The time scales must show τ_separation << τ_recombination.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bandgap_PBEpU",
          "bandgap_HSEscaled",
          "midgap_states"
        ],
        "properties": {
          "bandgap_PBEpU": {
            "type": "number",
            "units": "eV"
          },
          "bandgap_HSEscaled": {
            "type": "number",
            "units": "eV"
          },
          "midgap_states": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "spin",
                "state_label",
                "energy_rel_VBM",
                "occupied"
              ],
              "properties": {
                "spin": {
                  "type": "string"
                },
                "state_label": {
                  "type": "string"
                },
                "energy_rel_VBM": {
                  "type": "number",
                  "units": "eV"
                },
                "occupied": {
                  "type": "boolean"
                }
              }
            }
          }
        }
      },
      "description": "Electronic structure summary containing the band gap values and a list of midgap defect states with their energies relative to VBM and occupation status, required to verify the existence of occupied hole-trap states."
    },
    {
      "file": "table1_energy_nac.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "orbitals",
          "energy",
          "scaled_energy",
          "NAC",
          "scaled_NAC"
        ],
        "units": {
          "energy": "eV",
          "scaled_energy": "eV",
          "NAC": "meV",
          "scaled_NAC": "meV"
        }
      },
      "description": "Canonically averaged energy gaps and nonadiabatic couplings for spin-down channel state pairs, used to validate the raw and scaled electronic coupling inputs for the dynamics."
    },
    {
      "file": "table2_timescales.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "spin",
          "process",
          "timescale_ps",
          "uncertainty_ps"
        ],
        "units": {
          "timescale_ps": "ps",
          "uncertainty_ps": "ps"
        }
      },
      "description": "Fitted time scales for charge separation (hole trapping) and recombination from NAMD simulations for both spin channels, including statistical uncertainties, to verify the claim that charge separation is significantly faster than recombination."
    }
  ],
  "notes": "The verifier compares the submitted numeric values against hidden reference values derived from the paper’s reported results, applying appropriate tolerances for the chosen functional and basis set. The electronic_summary must contain at least one occupied midgap state in each spin channel. The time scales must show τ_separation << τ_recombination."
}
```

## How you are scored
A hidden verifier independently scores each of the three required output artifacts. The electronic summary is checked for consistency: band gaps, midgap state energies, and occupation status are compared against reference values with appropriate tolerances. The energy/NAC table is evaluated by comparing the reported averaged and scaled values to known references. The time-scale table is assessed by comparing the fitted time constants and uncertainties to reference values and by verifying expected qualitative trends, such as whether charge separation is faster than recombination. Each stage contributes a weighted portion to the final reward; reporting the correct quantities alone is not sufficient—the values must be within the allowed margins to earn full credit.
