# Oxygen defect formation energies in AlSb via first-principles DFT

## Problem background
InAs/AlSb high-electron mobility transistors (HEMTs) can exhibit a recoverable degradation under electrical stress, observed as a negative shift in threshold voltage. Prior work has hypothesized that oxygen contamination introduces point defects in the AlSb barrier layer that, upon hole injection, can convert from negatively charged acceptor states to more positively charged metastable states, increasing net positive charge. To evaluate this mechanism, it is necessary to compute the formation energies of substitutional oxygen (O_Sb) and interstitial oxygen (O_i) in AlSb for their relevant charge states and atomic configurations, and to see how their relative stability changes with the Fermi level.

## Approach
Density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional is used to perform first-principles calculations. First, a perfect zincblende AlSb host cell is computed to obtain reference total energies, the valence band maximum (VBM), and chemical potentials under Al-rich conditions. Then, supercells containing individual oxygen defects (O_Sb and O_i) in various atomic configurations and charge states are structurally relaxed, and their total energies are extracted. Formation energies are calculated using the standard expression E^f = E_tot + q(E_F - E_V) - Σ n_i μ_i, with potential alignment and image charge corrections for charged defects. Formation energies are evaluated at two Fermi levels: at the VBM and 0.25 eV above the VBM. By comparing the formation energies of different charge states and configurations, one can determine which configurations are thermodynamically preferred under each condition and assess whether hole capture can induce a transition to a more positive charge state.

## Reproduction target
Produce a CSV file, `formation_energies.csv`, containing the formation energies (in eV) for the following defect types, configurations, and charge states at Fermi levels 0.0 eV and 0.25 eV relative to the VBM.
- Substitutional oxygen (O_Sb): configurations alpha-CCB-DX, beta-CCB-DX, OBB-DX, C3V, each in charge states -1, 0, +1.
- Interstitial oxygen (O_i): configurations C3V, bb, (O-Sb)sp, each in charge states -2 and 0.
The CSV must have columns: defect, configuration, charge, Fermi_level, formation_energy.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- AlSb zincblende crystal structure
- PseudoDojo pseudopotentials for Al, Sb, O: http://www.pseudo-dojo.org/

## Workflow steps

### Step 1: Host AlSb reference calculation
- Role: process
- Action: Set up AlSb zincblende primitive cell with experimental lattice constant 6.1355 Å. Perform DFT self-consistent field calculation with PBE functional using Quantum ESPRESSO to obtain total energy per atom, valence band maximum (VBM) using average over k-points, and derive chemical potentials for Al and Sb under Al-rich conditions. Write the reference values to host_reference.json.
- Evidence: `/app/outputs/host_reference.json`

### Step 2: Defect supercell DFT relaxations
- Role: process
- Action: For oxygen defects O_Sb and O_i, construct a 64-atom AlSb supercell with the defect. For each configuration (O_Sb: alpha-CCB-DX, beta-CCB-DX, OBB-DX, C3V; O_i: C3V, bb, (O-Sb)sp) and each required charge state (O_Sb: -1, 0, +1; O_i: -2, 0) perform ionic relaxation and compute total energy using Quantum ESPRESSO. Use consistent k-point sampling and plane-wave cutoff. Write a summary of total energies to defect_total_energies.json.
- Evidence: `/app/outputs/defect_total_energies.json`

### Step 3: Formation energy calculation and scored CSV
- Role: scored (load-bearing)
- Action: Using the host reference VBM and chemical potentials from host_reference.json and the total energies from defect_total_energies.json, compute formation energies for each defect, configuration, and charge state at Fermi levels 0.0 eV and 0.25 eV above VBM. Apply a potential alignment correction and image charge correction for charged defects (e.g., the scheme of Lany and Zunger, or equivalent). Write results to formation_energies.csv with columns: defect, configuration, charge, Fermi_level, formation_energy.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: defect (string), configuration (string), charge (integer), Fermi_level (float, eV), formation_energy (float, eV). Rows for all combinations of defect, configuration, charge, and Fermi_level=0.0,0.25.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies for oxygen defect configurations and charge states at two Fermi levels. The verifier checks relative formation energy ordering between charge states at the two specified Fermi levels and verifies that the charge-state transition levels fall within the expected range.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `configuration`, `charge`, `Fermi_level`, `formation_energy`
  - `columns`:
    - `defect`: string
    - `configuration`: string
    - `charge`: integer
    - `Fermi_level`: float, eV
    - `formation_energy`: float, eV

Notes: The verifier applies structural checks (charge ordering and transition level) to formation_energies.csv. The evidence files host_reference.json and defect_total_energies.json are required intermediate artifacts but are not scored directly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "configuration",
          "charge",
          "Fermi_level",
          "formation_energy"
        ],
        "columns": {
          "defect": "string",
          "configuration": "string",
          "charge": "integer",
          "Fermi_level": "float, eV",
          "formation_energy": "float, eV"
        }
      },
      "description": "Formation energies for oxygen defect configurations and charge states at two Fermi levels. The verifier checks relative formation energy ordering between charge states at the two specified Fermi levels and verifies that the charge-state transition levels fall within the expected range."
    }
  ],
  "notes": "The verifier applies structural checks (charge ordering and transition level) to formation_energies.csv. The evidence files host_reference.json and defect_total_energies.json are required intermediate artifacts but are not scored directly."
}
```

## How you are scored
An automated hidden verifier evaluates your submission by reading your output artifacts. The verifier independently reconstructs formation energies from your intermediate host and defect total energy files (`host_reference.json` and `defect_total_energies.json`) and checks the consistency with the values reported in `formation_energies.csv`. It then verifies that certain relative ordering relationships among the formation energies of different charge states hold at the specified Fermi levels, and that the Fermi level at which the formation energies of relevant charge states cross lies within a target interval. Each scored stage is assigned a weight, and the overall reward is a weighted combination of the stage scores. The verifier never reveals the target values or tolerances; it only returns a final score between 0 and 1. To succeed, you must faithfully execute the workflow, produce all intermediate artifacts, and ensure the final CSV is physically reasonable.
