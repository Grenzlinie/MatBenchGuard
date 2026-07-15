# Vibrational analysis of SiGa- defect geometries in GaAs using LDF cluster method

## Problem background
The DX center in Si-doped GaAs is believed to involve a large lattice distortion when a shallow donor captures an extra electron, but its exact atomic geometry remains controversial. Local-vibrational-mode infrared spectroscopy under hydrostatic pressure has tentatively assigned a DX-related mode at 376 cm⁻¹ (inferred zero‑pressure value), providing an experimental signature that candidate structures can be tested against. Two main candidates have been proposed for the negatively charged SiGa⁻ defect: the off‑site Chadi–Chang distortion, in which the Si atom moves along ⟨111⟩ breaking one Si–As bond, and a breathing distortion where the As neighbors move outward while Si stays on‑site. First‑principles calculations that predict vibrational frequencies and infrared intensities for these geometries can independently evaluate which structure agrees with the experimental local mode.

## Approach
The approach uses local‑density‑functional (LDF) cluster calculations to model the SiGa⁻ defect in a 71‑atom, H‑terminated cluster that represents a Si atom substituting a Ga site in GaAs. The negatively charged cluster is relaxed in two configurations: (i) the off‑site distortion where Si is displaced along ⟨111⟩ away from one As neighbour, and (ii) the breathing distortion where one As neighbour is initially pulled outward while Si stays on‑site, leading to four equal lengthened Si–As bonds. For each relaxed geometry, the second derivatives of the energy are computed to obtain the dynamical matrix and extract the localized vibrational mode frequencies, and the Born effective charge is evaluated to gauge infrared activity. The results are then compared with the experimentally inferred DX local mode at 376 cm⁻¹ to assess which structure, if either, is consistent with experiment. A preliminary benchmark calculation on the positively charged donor SiGa⁺ is performed to validate the cluster model against the known shallow‑donor triplet frequency.

## Reproduction target
Compute, using the LDF cluster method, the localized vibrational mode frequencies and Born effective charges for the two negative‑charge defect geometries described above. Specifically, for the off‑site Chadi–Chang geometry report the high‑frequency doublet E‑mode frequency and its effective charge; for the breathing geometry report the triplet mode frequencies (with their mean) and its effective charge. In addition, record the total‑energy difference between the two relaxed structures. Then produce a short plain‑text report that compares the computed frequencies with the experimental DX local mode at 376 cm⁻¹ and states which structure, if any, is consistent with that frequency, along with a qualitative note on the relative infrared activities. The required output files are: `chadi_chang_frequencies.json`, `breathing_frequencies.json`, and `comparison_report.txt`.

## Assets

- Density functional theory (DFT) code with LDA capability (e.g., CP2K): https://www.cp2k.org/
- Pseudopotentials or basis sets for Ga, As, Si, H (LDA): CP2K or other DFT package included basis/pseudopotential libraries
- GaAs crystal structure (lattice constant and atomic positions): https://next-gen.materialsproject.org/materials/mp-2534

## Workflow steps

### Step 1: Cluster model setup
- Role: process
- Action: Construct the 71-atom H-terminated cluster SiAs16Ga18H36 with Si substituted at a Ga site, suitable for LDF cluster calculations. Assign appropriate number of extra electrons for the negatively charged defect (for SiGa-) and for the positively charged donor (for SiGa+). Use the zinc-blende GaAs lattice constant from standard crystallographic data.
- Evidence: none

### Step 2: Donor Si+ vibrational benchmark
- Role: process
- Action: Using the same cluster model with appropriate charge (positively charged shallow donor SiGa+), relax the geometry and compute the second derivatives of the energy to obtain the triplet vibrational mode frequencies. Verify the mean frequency is close to the known experimental value to validate the cluster methodology. Write the computed triplet frequencies and mean to an evidence file.
- Evidence: `/app/outputs/donor_benchmark_frequencies.json`

### Step 3: Chadi-Chang off-site distortion of SiGa-: relaxation, vibrational and charge analysis
- Role: scored
- Action: Starting from the negatively charged cluster model, displace the Si atom along <111> away from one As neighbour to break one Si-As bond as in the Chadi-Chang model. Relax the inner atoms. Compute the dynamical matrix and extract the localized vibrational mode frequencies. Report the high-frequency doublet (E) localized vibrational mode frequency (the singlet is not a distinct LVM). Compute the Born effective charge governing infrared intensity. Write the E-mode frequency, effective charge, and a note to the output file.
- Output file: `/app/outputs/chadi_chang_frequencies.json`
- Format: json
- Contract: {"e_mode_frequency_cm1": <float>, "effective_charge_e": <float>, "note": "string indicating singlet is not a distinct high-frequency LVM"}
- Scoring: scored by hidden verifier

### Step 4: Breathing distortion of SiGa-: relaxation, vibrational analysis and energy relative to Chadi-Chang
- Role: scored (load-bearing)
- Action: Starting from the same negatively charged cluster model, keep Si on-site and displace one As neighbour 1 Å outward from Si. Relax the inner atoms; the relaxation should yield four equal, longer Si-As bonds. Compute the triplet vibrational mode frequencies and their mean. Compute the Born effective charge. Also compute the total energy difference between this breathing structure and the previously relaxed Chadi-Chang structure. Write the triplet frequencies, mean, effective charge, and energy difference to the output file.
- Output file: `/app/outputs/breathing_frequencies.json`
- Format: json
- Contract: {"triplet_frequencies_cm1": [<float>, <float>, <float>], "mean_frequency_cm1": <float>, "effective_charge_e": <float>, "energy_difference_eV": <float>}
- Scoring: scored by hidden verifier

### Step 5: Comparison with experimental DX local mode
- Role: scored
- Action: Using the computed frequencies and charges from steps 2 and 3, compare them with the experimentally inferred DX local mode at 376 cm^-1 (from Wolk et al.). State whether the breathing or the Chadi-Chang structure is consistent with the experimental frequency, and discuss the relative infrared activities. Write a plain-text report.
- Output file: `/app/outputs/comparison_report.txt`
- Format: txt
- Contract: Plain text; must mention both the Chadi-Chang and breathing structures and reference the experimental frequency of 376 cm^-1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chadi_chang_frequencies.json`
- `/app/outputs/breathing_frequencies.json`
- `/app/outputs/comparison_report.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chadi_chang_frequencies.json
- path: `/app/outputs/chadi_chang_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the E-mode frequency (in cm^-1) and Born effective charge (in elementary charge e) for the Chadi-Chang off-site SiGa- geometry.
- schema:
  - `type`: object
  - `required`: `e_mode_frequency_cm1`, `effective_charge_e`, `note`
  - `properties`:
    - `e_mode_frequency_cm1`:
      - `type`: number
      - `description`: E-mode doublet frequency in cm^-1
    - `effective_charge_e`:
      - `type`: number
      - `description`: Born effective charge in elementary charge e
    - `note`:
      - `type`: string
      - `description`: Statement that singlet is not a distinct high-frequency LVM

### breathing_frequencies.json
- path: `/app/outputs/breathing_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the three triplet frequencies (cm^-1), their mean, the Born effective charge, and the energy difference (eV) relative to the Chadi-Chang structure.
- schema:
  - `type`: object
  - `required`: `triplet_frequencies_cm1`, `mean_frequency_cm1`, `effective_charge_e`, `energy_difference_eV`
  - `properties`:
    - `triplet_frequencies_cm1`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Three triplet mode frequencies in cm^-1
    - `mean_frequency_cm1`:
      - `type`: number
      - `description`: Mean of the triplet frequencies in cm^-1
    - `effective_charge_e`:
      - `type`: number
      - `description`: Born effective charge in elementary charge e
    - `energy_difference_eV`:
      - `type`: number
      - `description`: Total energy difference relative to Chadi-Chang structure in eV

### comparison_report.txt
- path: `/app/outputs/comparison_report.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A brief report that states which computed vibrational mode matches the experimental 376 cm^-1 and gives a qualitative assessment of infrared activity; must mention both the Chadi-Chang and breathing structures and reference the experimental frequency of 376 cm^-1.
- schema:
  - `type`: text
  - `description`: Plain text report.

Notes: The scored artifacts record computed vibrational frequencies and effective charges. The comparison report is a qualitative structural audit. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chadi_chang_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "e_mode_frequency_cm1",
          "effective_charge_e",
          "note"
        ],
        "properties": {
          "e_mode_frequency_cm1": {
            "type": "number",
            "description": "E-mode doublet frequency in cm^-1"
          },
          "effective_charge_e": {
            "type": "number",
            "description": "Born effective charge in elementary charge e"
          },
          "note": {
            "type": "string",
            "description": "Statement that singlet is not a distinct high-frequency LVM"
          }
        }
      },
      "description": "Scored artifact containing the E-mode frequency (in cm^-1) and Born effective charge (in elementary charge e) for the Chadi-Chang off-site SiGa- geometry."
    },
    {
      "file": "breathing_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "triplet_frequencies_cm1",
          "mean_frequency_cm1",
          "effective_charge_e",
          "energy_difference_eV"
        ],
        "properties": {
          "triplet_frequencies_cm1": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Three triplet mode frequencies in cm^-1"
          },
          "mean_frequency_cm1": {
            "type": "number",
            "description": "Mean of the triplet frequencies in cm^-1"
          },
          "effective_charge_e": {
            "type": "number",
            "description": "Born effective charge in elementary charge e"
          },
          "energy_difference_eV": {
            "type": "number",
            "description": "Total energy difference relative to Chadi-Chang structure in eV"
          }
        }
      },
      "description": "Scored artifact containing the three triplet frequencies (cm^-1), their mean, the Born effective charge, and the energy difference (eV) relative to the Chadi-Chang structure."
    },
    {
      "file": "comparison_report.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Plain text report."
      },
      "description": "A brief report that states which computed vibrational mode matches the experimental 376 cm^-1 and gives a qualitative assessment of infrared activity; must mention both the Chadi-Chang and breathing structures and reference the experimental frequency of 376 cm^-1."
    }
  ],
  "notes": "The scored artifacts record computed vibrational frequencies and effective charges. The comparison report is a qualitative structural audit. No gold values or tolerances are revealed here."
}
```

## How you are scored
A hidden verifier independently examines each scored artifact (the two JSON frequency files and the comparison report) and assigns a reward based on agreement with reference values derived from the paper, using tolerances appropriate for re‑runs with a different DFT implementation and cluster setup. The scores for the individual artifacts are combined by weight into a single overall reward between 0 and 1. The earlier donor‑benchmark validation step is not directly scored but ensures the cluster methodology is sound. The verifier does not reveal the reference numbers or tolerances; your job is to faithfully execute the described workflow and report the computed quantities.
