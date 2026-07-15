# Silicon Vacancy Excitation Properties in SiC — DFT and TD‑DFT Study

## Problem background
Isolated point defects in semiconductors that combine a high-spin ground state with near-infrared luminescence are promising candidates for solid-state quantum bits. The silicon vacancy (V_Si) in silicon carbide (SiC) exhibits these features, making it a compelling system for quantum optics, magnetometry, and quantum information applications. However, the charge state responsible for the main photoluminescence (PL) centers observed experimentally in SiC (commonly denoted V1 and V1') has remained debated. Clarifying the correct charge state and its optical properties is essential for advancing the use of this defect in quantum technologies.

## Approach
This reproduction uses density functional theory (DFT) and time-dependent density functional theory (TD-DFT) to study the silicon vacancy. Both the neutral and negatively charged vacancy are modeled in a nano cubic 3C-SiC cluster. The PBE0 hybrid functional is employed to obtain accurate electronic structures. For each charge state, the ground-state geometry is optimized with the appropriate spin configuration (S=1 for neutral, S=3/2 for negative), after which TD-DFT with a PBE0 kernel computes the lowest-lying optical excitation energies and the symmetries of the many-electron excited states. Polarization selection rules for the optical transitions follow from the symmetries. For the negatively charged vacancy, a constrained DFT relaxation in an excited-state geometry is performed to extract the relaxation energy; this is used to estimate the zero-phonon line (ZPL) of the luminescence. The computed properties (excitation energies, ZPL, polarization rules) for both charge states are then compared against the experimental V1/V1' PL signatures: a ZPL near 1.44 eV and distinct parallel and perpendicular polarization components. The assignment is based on which charge state's computed properties are consistent with the experiments.

## Reproduction target
Reproduce the computational assessment by constructing a ≈1.4 nm 3C-SiC cluster with a silicon vacancy, optimizing geometries, and running TD-DFT calculations to obtain excitation energies, symmetries, and polarization rules for both charge states. Compute the relaxation energy for the negative vacancy and derive its estimated ZPL. Collect all results in a single JSON file (`computed_properties.json`) and include a statement that compares the computed properties with the experimental V1/V1' data to determine whether the neutral or negatively charged vacancy best explains the observed signals.

## Assets

- 3C-SiC crystal structure (zinc blende): Materials Project (mp-8062) or ICSD (60387); lattice constant ~4.36 Å, space group F-43m
- CP2K open-source DFT package: https://www.cp2k.org/download (version 8.2 or later recommended; any DFT code supporting PBE0, spin polarisation, and TD-DFT is acceptable)

## Workflow steps

### Step 1: Construct nano 3C-SiC cluster with silicon vacancy
- Role: process
- Action: From the public 3C-SiC zinc blende structure, construct a nano cubic cluster of approximately 1.4 nm diameter centred at an interstitial site, then remove one silicon atom to create a vacancy, ensuring a near-Td symmetry.
- Evidence: `/app/outputs/cluster.xyz`

### Step 2: DFT ground-state calculation for nano cluster
- Role: process
- Action: Perform spin-polarised DFT geometry optimisation and ground-state electronic structure calculations for the neutral (charge=0, S=1) and negatively charged (charge=-1, S=3/2) silicon vacancy using the PBE0 hybrid functional.
- Evidence: `/app/outputs/dft_gs.log`

### Step 3: TD-DFT excitation calculation
- Role: process
- Action: Using TD-DFT with the PBE0 hybrid kernel, compute the lowest excitation energies and the many-electron symmetry labels for the neutral vacancy (lowest excitation, e.g. ^3E from ^3A_2) and for the negatively charged vacancy (two lowest excitations, ^4A_2 and ^4E).
- Evidence: `/app/outputs/tddft.out`

### Step 4: Constrained DFT relaxation for the negatively charged vacancy
- Role: process
- Action: For the negatively charged vacancy, perform a geometry optimisation under an occupation constraint that mimics the excited state (e.g. the ^4A_2 occupation) to obtain the relaxed excited-state geometry; compute the relaxation energy as the difference between the vertical excitation energy and the relaxed excitation energy.
- Evidence: `/app/outputs/relax_energy.txt`

### Step 5: Compile computed properties and compare with experiment
- Role: scored (load-bearing)
- Action: Collect all computed quantities: for the neutral vacancy, ground-state symmetry, lowest excitation energy, excited-state symmetry, and polarisation rules; for the negatively charged vacancy, ground-state symmetry, first and second excitation energies and their symmetries, relaxation energy, estimated zero-phonon line (vertical excitation minus relaxation energy), and polarisation rules. Write the complete results into computed_properties.json. Include a comparison statement that honestly assesses, based on the computed values, whether the properties of the neutral and negatively charged silicon vacancy agree or disagree with the experimental V1/V1' photoluminescence data (ZPL ~1.44 eV, parallel and perpendicular polarisation components).
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {
  "neutral_vacancy": {
    "ground_state_symmetry": "string (e.g., ^3A_2)",
    "lowest_excitation_energy_eV": "number",
    "lowest_excited_state_symmetry": "string (e.g., ^3E)",
    "polarization_rules": "string (e.g., perpendicular only)"
  },
  "negative_vacancy": {
    "ground_state_symmetry": "string (e.g., ^4A_2)",
    "first_excitation_energy_eV": "number",
    "first_excited_state_symmetry": "string (e.g., ^4A_2)",
    "second_excitation_energy_eV": "number",
    "second_excited_state_symmetry": "string (e.g., ^4E)",
    "relaxation_energy_eV": "number",
    "estimated_zero_phonon_line_eV": "number",
    "polarization_rules": "string (e.g., E||c for ^4A_2, E_perp_c for ^4E)"
  },
  "comparison_experiment": "string (statement describing agreement/mismatch with experimental V1/V1' data)"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON artifact containing the computed excitation energies, symmetries, polarisation rules, relaxation energy, estimated zero‑phonon line, and a comparison statement against experimental V1/V1' photoluminescence data.
- schema:
  - `type`: object
  - `required`: `neutral_vacancy`, `negative_vacancy`, `comparison_experiment`
  - `neutral_vacancy`:
    - `ground_state_symmetry`: string
    - `lowest_excitation_energy_eV`: number
    - `lowest_excited_state_symmetry`: string
    - `polarization_rules`: string
  - `negative_vacancy`:
    - `ground_state_symmetry`: string
    - `first_excitation_energy_eV`: number
    - `first_excited_state_symmetry`: string
    - `second_excitation_energy_eV`: number
    - `second_excited_state_symmetry`: string
    - `relaxation_energy_eV`: number
    - `estimated_zero_phonon_line_eV`: number
    - `polarization_rules`: string
  - `comparison_experiment`: string

Notes: All numeric energies are in eV. Polarisation strings indicate optical selection rules relative to the defect symmetry axis. The comparison statement must honestly evaluate, based on the computed numbers, whether the properties of the neutral and negatively charged vacancies are consistent with the experimental V1/V1' PL data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "neutral_vacancy",
          "negative_vacancy",
          "comparison_experiment"
        ],
        "neutral_vacancy": {
          "ground_state_symmetry": "string",
          "lowest_excitation_energy_eV": "number",
          "lowest_excited_state_symmetry": "string",
          "polarization_rules": "string"
        },
        "negative_vacancy": {
          "ground_state_symmetry": "string",
          "first_excitation_energy_eV": "number",
          "first_excited_state_symmetry": "string",
          "second_excitation_energy_eV": "number",
          "second_excited_state_symmetry": "string",
          "relaxation_energy_eV": "number",
          "estimated_zero_phonon_line_eV": "number",
          "polarization_rules": "string"
        },
        "comparison_experiment": "string"
      },
      "description": "JSON artifact containing the computed excitation energies, symmetries, polarisation rules, relaxation energy, estimated zero‑phonon line, and a comparison statement against experimental V1/V1' photoluminescence data."
    }
  ],
  "notes": "All numeric energies are in eV. Polarisation strings indicate optical selection rules relative to the defect symmetry axis. The comparison statement must honestly evaluate, based on the computed numbers, whether the properties of the neutral and negatively charged vacancies are consistent with the experimental V1/V1' PL data."
}
```

## How you are scored
A hidden verifier independently evaluates your `computed_properties.json` artifact. It checks each numeric field (excitation energies, relaxation energy, estimated ZPL) against a hidden reference with an appropriate tolerance. It also verifies that the reported symmetry labels and polarization selection rules are correct. The comparison statement is checked for factual consistency with the computed numbers. The overall reward is the weighted sum of these individual checks, rewarding accurate computation rather than merely reporting preconceived numbers. No single missing or wrong field fails the task, but a high-quality reproduction must accurately capture the physics of both charge states.
