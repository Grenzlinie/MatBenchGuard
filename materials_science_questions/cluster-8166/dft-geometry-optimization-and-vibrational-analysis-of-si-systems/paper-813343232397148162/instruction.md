# DFT Geometry and Vibrational Frequencies of Si Impurity in GaAs Supercell

## Problem background
The DX center in GaAs exhibits bistability between shallow and deep donor levels. The broken-bond model explains the deep state by a large off-center displacement of the donor atom (C3v symmetry). However, EXAFS measurements report nearly identical bond lengths for both the shallow and deep levels, and FTIR absorption shows close vibrational frequencies, raising doubts whether the broken-bond geometry is correct. This task tests the broken-bond model for the Si donor in GaAs by computing optimized geometries and local vibrational frequencies from first-principles DFT, to determine which large-relaxation structure is energetically preferred and whether the resulting structural and vibrational properties are compatible with the experimental constraints.

## Approach
The workflow uses supercell density-functional theory (DFT) within the local-density approximation (LDA), employing norm-conserving pseudopotentials and a plane-wave basis. A 32-atom GaAs supercell containing a Si impurity is constructed. Atomic geometries are optimized for several distinct configurations: the substitutional site (Td, representing the shallow donor), the broken-bond geometry (C3v, the candidate deep state), the Si-As exchange geometry, and three Ga-interstitial–vacancy pair distortions. Total energies are compared to identify the most stable configuration among the large-lattice-relaxation candidates. Subsequently, local vibrational mode frequencies for the Si–As bond-stretching motions are computed for the optimized Td and C3v structures by displacing the Si and nearest As atoms and evaluating forces via finite differences; the relevant t₂, e, and a₁ modes are extracted. All calculations are performed with open-source software and public pseudopotentials, allowing the entire pipeline to be executed by the agent.

## Reproduction target
The agent must produce two scored JSON files. The first (`step_01_geometries.json`) contains optimized bond lengths, Si displacement, bond angle, and total energies for the substitutional (Td) and broken-bond (C3v) geometries, plus a determination of the most stable configuration among the large-relaxation candidates and the energy difference to the next most stable. The second (`step_02_frequencies.json`) reports the Si-As local vibrational mode frequencies: the t₂ mode for the Td geometry, the e and a₁ modes for the C3v geometry, and the ratio v(Td)/v(C3v). The computed numbers are the target; the agent does not need to report any experimental comparisons or auxiliary analysis.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA norm-conserving pseudopotentials for Ga, As, Si: https://www.materialscloud.org/discover/sssp/table/efficiency
- GaAs zincblende crystal structure

## Workflow steps

### Step 1: DFT geometry optimizations for Si impurity configurations
- Role: scored
- Action: Set up a 32-atom GaAs supercell with a Si impurity. Using LDA and norm-conserving pseudopotentials, optimize the following geometries: (a) substitutional (Td) with a +1 charge state; (b) broken-bond (C3v) with a -1 charge state; (c) the metastable Si_AsAs_Ga exchange configuration; (d) three Ga_I V_Ga variants. Relax all atoms until forces are negligible. Report structural parameters and total energies.
- Output file: `/app/outputs/step_01_geometries.json`
- Format: json
- Contract: {"substitutional_Td":{"Si_As_bond_length_A":"float","total_energy_eV":"float"},"broken_bond_C3v":{"Si_As_bond_length_A":"float","Si_displacement_A":"float","bond_angle_deg":"float","total_energy_eV":"float"},"most_stable_among_large_relaxation":"string","energy_difference_compared_to_next_metastable_eV":"float"}
- Scoring: scored by hidden verifier

### Step 2: Local vibrational mode frequency calculation
- Role: scored
- Action: Using the optimized substitutional (Td) and broken-bond (C3v) geometries from step_01, compute the Si–As bond-stretching local vibrational mode frequencies via finite-difference DFT forces with a plane-wave cutoff of 12 Ry. Displace Si and nearest As atoms. Extract the t2 mode for Td and e and a1 modes for C3v.
- Output file: `/app/outputs/step_02_frequencies.json`
- Format: json
- Contract: {"v_Td_t2_mode_cm-1":"float","v_C3v_e_mode_cm-1":"float","v_C3v_a1_mode_cm-1":"float","ratio_vTd_vC3v":"float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_geometries.json`
- `/app/outputs/step_02_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_geometries.json
- path: `/app/outputs/step_01_geometries.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized geometries and energies for Si impurity configurations in GaAs.
- schema:
  - `type`: object
  - `required`: `substitutional_Td`, `broken_bond_C3v`, `most_stable_among_large_relaxation`, `energy_difference_compared_to_next_metastable_eV`
  - `properties`:
    - `substitutional_Td`:
      - `type`: object
      - `required`: `Si_As_bond_length_A`, `total_energy_eV`
    - `broken_bond_C3v`:
      - `type`: object
      - `required`: `Si_As_bond_length_A`, `Si_displacement_A`, `bond_angle_deg`, `total_energy_eV`
    - `most_stable_among_large_relaxation`:
      - `type`: string
    - `energy_difference_compared_to_next_metastable_eV`:
      - `type`: number

### step_02_frequencies.json
- path: `/app/outputs/step_02_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Local vibrational mode frequencies for Si in GaAs and frequency ratio.
- schema:
  - `type`: object
  - `required`: `v_Td_t2_mode_cm-1`, `v_C3v_e_mode_cm-1`, `v_C3v_a1_mode_cm-1`, `ratio_vTd_vC3v`
  - `properties`:
    - `v_Td_t2_mode_cm-1`:
      - `type`: number
    - `v_C3v_e_mode_cm-1`:
      - `type`: number
    - `v_C3v_a1_mode_cm-1`:
      - `type`: number
    - `ratio_vTd_vC3v`:
      - `type`: number

Notes: Task covers only Si impurity. Ge and Sn donors, VFF model, and experimental comparison are not required. The agent must use open-source Quantum ESPRESSO and public LDA pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_geometries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "substitutional_Td",
          "broken_bond_C3v",
          "most_stable_among_large_relaxation",
          "energy_difference_compared_to_next_metastable_eV"
        ],
        "properties": {
          "substitutional_Td": {
            "type": "object",
            "required": [
              "Si_As_bond_length_A",
              "total_energy_eV"
            ]
          },
          "broken_bond_C3v": {
            "type": "object",
            "required": [
              "Si_As_bond_length_A",
              "Si_displacement_A",
              "bond_angle_deg",
              "total_energy_eV"
            ]
          },
          "most_stable_among_large_relaxation": {
            "type": "string"
          },
          "energy_difference_compared_to_next_metastable_eV": {
            "type": "number"
          }
        }
      },
      "description": "Optimized geometries and energies for Si impurity configurations in GaAs."
    },
    {
      "file": "step_02_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "v_Td_t2_mode_cm-1",
          "v_C3v_e_mode_cm-1",
          "v_C3v_a1_mode_cm-1",
          "ratio_vTd_vC3v"
        ],
        "properties": {
          "v_Td_t2_mode_cm-1": {
            "type": "number"
          },
          "v_C3v_e_mode_cm-1": {
            "type": "number"
          },
          "v_C3v_a1_mode_cm-1": {
            "type": "number"
          },
          "ratio_vTd_vC3v": {
            "type": "number"
          }
        }
      },
      "description": "Local vibrational mode frequencies for Si in GaAs and frequency ratio."
    }
  ],
  "notes": "Task covers only Si impurity. Ge and Sn donors, VFF model, and experimental comparison are not required. The agent must use open-source Quantum ESPRESSO and public LDA pseudopotentials."
}
```

## How you are scored
A hidden verifier will independently evaluate each output file. For step_01, it checks the reported structural parameters, total energies, and the identification of the most stable large-relaxation structure against a set of reference values with appropriate tolerances. For step_02, it checks the vibrational frequencies and the frequency ratio against reference values. Both stages contribute weighted fractions to the final score (range 0 to 1). Merely writing approximate numbers is not sufficient; the verifier expects results that are within a tolerance window derived from the known computational uncertainty of this protocol. The exact tolerances are not disclosed, but a correct implementation of the described DFT workflow is expected to pass. No other artifacts are scored.
