# DFT-based CO2 binding energy ordering for Zn/Metal clusters

## Problem background
Metal-organic frameworks (MOFs) containing nucleophilic M–OH functional groups can capture CO₂ via a chemisorption mechanism analogous to carbonic anhydrase. This investigation focuses on how the identity of the transition metal (Zn, Co, Ni) at the Kuratowski-type nodes of CFA-1 influences the strength of CO₂ binding. In this task, you will use density functional theory (DFT) calculations on truncated model clusters to compute the first CO₂ binding energies and determine the relative ordering of binding strength across different metal compositions.

## Approach
The computation employs the B3PW91 hybrid functional with a mixed basis set: LANL2DZ effective core potentials for all metal atoms (Zn, Co, Ni), 6-311G(d) for C and H, and 6-311+G(d) for N and O. Model clusters are constructed by truncating the CFA-1 crystal structure to retain the pentanuclear Kuratowski-type nodes with benzotriazolate ligands. For each metal composition (Zn₅, Co₄Zn, NiZn₄, Ni₄Zn), the hydroxide (M-OH) and bicarbonate (M-HCO₃) forms are optimized and vibrational frequencies computed to obtain thermally corrected electronic energies. The first CO₂ binding energy is then calculated as `E_bind = E[M-HCO₃] – E[M-OH] – E[CO₂]`, with the CO₂ reference molecule treated at the same level of theory. The bicarbonate binds in the thermodynamically preferred distal geometry, as determined by a preliminary isomer screening on the Zn₅ cluster. The resulting binding energies are ranked to reveal the dependence of CO₂ affinity on metal identity and cluster composition.

## Reproduction target
Compute the first CO₂ binding energies for four model clusters: Zn₅, Co₄Zn, NiZn₄, and Ni₄Zn, using DFT at the B3PW91 level with LANL2DZ effective core potentials and the specified mixed basis sets. For each cluster, output the binding energy in kJ/mol and the bicarbonate isomer. Provide the results in a JSON file that records all four clusters and their binding energies. The relative ranking of these binding energies will be evaluated.

## Assets

- CFA-1 crystal structure (CCDC entry): https://www.ccdc.cam.ac.uk/structures/
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Screen bicarbonate linkage isomers for Zn5 cluster
- Role: process
- Action: Construct the Zn5 model cluster from the CFA-1 crystal structure. Perform DFT geometry optimizations and frequency calculations at the BP86 level with LANL2DZ for Zn and 6-311G(d)/6-311+G(d) for light atoms to compare the energies of proximal and distal bicarbonate binding isomers. Identify the more stable distal isomer as the starting geometry for subsequent calculations.
- Evidence: `/app/outputs/isomer_energies.txt`

### Step 2: Compute reference CO2 energy
- Role: process
- Action: Perform a DFT geometry optimization and frequency calculation on an isolated CO2 molecule using B3PW91 with the mixed basis set (6-311G(d) for C, 6-311+G(d) for O). Extract the thermally corrected electronic energy for use in binding energy formulas.
- Evidence: `/app/outputs/co2_energy.txt`

### Step 3: Optimize MxZny-OH and MxZny-HCO3 clusters
- Role: process
- Action: Construct hydroxide (M-OH) and bicarbonate (M-HCO3) models for Zn5, Co4Zn, NiZn4, and Ni4Zn clusters using the CFA-1 structure and the distal bicarbonate configuration from step1. Perform geometry optimizations and frequency calculations with B3PW91, LANL2DZ effective core potentials for metals, and 6-311G(d)/6-311+G(d) for light atoms. Use the highest spin state for Co and Ni complexes. Record thermally corrected electronic energies of all eight species.
- Evidence: `/app/outputs/cluster_energies.json`

### Step 4: Compute CO2 binding energies and ranking
- Role: scored (load-bearing)
- Action: For each cluster composition, compute the first CO2 binding energy as E_bind = E[M-HCO3] - E[M-OH] - E[CO2] using the thermally corrected energies from steps 2 and 3. Output the results in JSON format with cluster name, binding energy (kJ/mol), and bicarbonate isomer.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: [{"cluster": "string (one of Ni4Zn, NiZn4, Zn5, Co4Zn)", "binding_energy_kj_per_mol": "number", "bicarbonate_isomer": "string (distal)"}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: First CO2 binding energies for the four metal-exchanged clusters. The checker verifies the presence of all four clusters with 'distal' isomer and the exact relative ordering: Ni4Zn > NiZn4 > Zn5 > Co4Zn.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `cluster`, `binding_energy_kj_per_mol`, `bicarbonate_isomer`
    - `properties`:
      - `cluster`:
        - `type`: string
        - `enum`: `Ni4Zn`, `NiZn4`, `Zn5`, `Co4Zn`
      - `binding_energy_kj_per_mol`:
        - `type`: number
      - `bicarbonate_isomer`:
        - `type`: string
        - `const`: distal
  - `minItems`: 4
  - `maxItems`: 4

Notes: Only the relative ordering of binding energies is scored; absolute values are not compared. The output must contain exactly four entries with the specified cluster names and 'distal' isomer.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "cluster",
            "binding_energy_kj_per_mol",
            "bicarbonate_isomer"
          ],
          "properties": {
            "cluster": {
              "type": "string",
              "enum": [
                "Ni4Zn",
                "NiZn4",
                "Zn5",
                "Co4Zn"
              ]
            },
            "binding_energy_kj_per_mol": {
              "type": "number"
            },
            "bicarbonate_isomer": {
              "type": "string",
              "const": "distal"
            }
          }
        },
        "minItems": 4,
        "maxItems": 4
      },
      "description": "First CO2 binding energies for the four metal-exchanged clusters. The checker verifies the presence of all four clusters with 'distal' isomer and the exact relative ordering: Ni4Zn > NiZn4 > Zn5 > Co4Zn."
    }
  ],
  "notes": "Only the relative ordering of binding energies is scored; absolute values are not compared. The output must contain exactly four entries with the specified cluster names and 'distal' isomer."
}
```

## How you are scored
A hidden verifier inspects your `binding_energies.json`. It first confirms that all four required clusters are present and that each entry reports the 'distal' bicarbonate isomer. It then checks that the binding energies are ranked in the correct relative order, as determined by the physics of the metal-exchanged clusters. The reward is 1.0 if the ordering matches the expected trend; otherwise the reward is 0.0. Absolute binding energy values are not compared, only the order matters.
