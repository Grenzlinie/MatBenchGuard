# DFT Activation Barriers for Ethylene Hydrogenation on Supported Ni4 Catalysts

## Problem background
Supported transition metal nanoparticles are widely employed as hydrogenation catalysts. Anchoring the metal particles on a support material not only prevents sintering but also alters the electronic state of the metal through the electronic metal‑support interaction (EMSI). Understanding how different supports tune the electron density of a metal cluster and thereby its catalytic activity is essential for rational catalyst design. In this task we study the ethylene hydrogenation activity of a tetrahedral Ni₄ cluster deposited on three chemically distinct substrates: CeO₂(111), TiO₂(101), and a monolayer of oxygen‑doped hexagonal boron nitride (BNO). The key quantity is the activation barrier for the Langmuir–Hinshelwood step in which two co‑adsorbed hydrogen atoms migrate from the Ni cluster to an adsorbed ethylene molecule. Because the support is expected to withdraw different amounts of electron density from the Ni cluster, the computed barriers are a direct probe of the EMSI effect. Determining the barriers for all three supports, at both low and high hydrogen coverage, allows one to quantify how strongly the support influences the catalytic activity.

## Approach
The computational framework is periodic density functional theory (DFT) with the PBE exchange‑correlation functional and a plane‑wave basis set. Slab models of the three support surfaces are built from their standard bulk crystal structures and relaxed. A tetrahedral Ni₄ cluster is placed on each clean surface and the combined Ni₄/support system is geometry‑optimized. Hydrogen adsorption is then built up: one H₂ molecule dissociates on the Ni₄ cluster to give a low‑coverage state with two H atoms on Ni₄; further sequential H₂ dissociation leads to a high‑coverage state with six H atoms on Ni₄. For each catalyst and each coverage, ethylene (C₂H₄) is co‑adsorbed on the Ni₄Hₓ cluster and the geometry is optimized to create the reactant complex. The activation barrier for the hydrogenation reaction — the simultaneous migration of two H atoms from Ni to ethylene to form ethane — is computed with the nudged elastic band (NEB) method. The procedure is repeated for the three supports at low and high coverage, yielding six activation barriers whose relative values and ordering reflect how the support identity controls the catalytic activity.

## Reproduction target
Using an open‑source DFT code capable of NEB (e.g., Quantum ESPRESSO), compute the activation barriers for the Langmuir–Hinshelwood ethylene hydrogenation step on three supported Ni₄ catalysts:

- Ni₄/CeO₂(111)
- Ni₄/TiO₂(101)
- Ni₄/BNO (oxygen‑doped BN monolayer)

Carry out the computation at two hydrogen coverages:
- low coverage: 2 H atoms pre‑adsorbed on the Ni₄ cluster
- high coverage: 6 H atoms pre‑adsorbed on the Ni₄ cluster

For each of the six combinations (3 supports × 2 coverages) report the activation barrier in eV. The relative ordering of the barriers among the three supports is an integral part of the evaluation; therefore all six barriers must be determined with the same computational protocol and written into a single JSON file at `/app/outputs/activation_barriers.json`.

## Assets

- Bulk CeO2 crystal structure: https://materialsproject.org/materials/mp-20194
- Bulk TiO2 anatase crystal structure: https://materialsproject.org/materials/mp-390
- O-doped BN monolayer reference: 10.1021/acs.jpcc.9b00324
- Open‑source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials (SSSP or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Substrate model preparation and relaxation
- Role: process
- Action: Build slab models of CeO2(111), TiO2(101), and the BNO monolayer (O‑doped BN) from the provided crystal structures. Relax atomic positions using DFT with PBE functional.
- Evidence: `/app/outputs/step_0_optimized_geometries.log`

### Step 2: Ni4 cluster adsorption
- Role: process
- Action: Adsorb a tetrahedral Ni4 cluster on each relaxed substrate and optimize the geometry of the Ni4/support system using DFT.
- Evidence: `/app/outputs/step_1_ni4_adsorption.log`

### Step 3: H2 dissociative chemisorption to obtain Ni4H2
- Role: process
- Action: For each Ni4/support, perform an NEB calculation for H2 dissociation on the Ni4 cluster to produce a stable structure with two adsorbed H atoms (Ni4H2).
- Evidence: `/app/outputs/step_2_h2_dissociation.log`

### Step 4: Sequential H adsorption to high coverage (Ni4H6)
- Role: process
- Action: Sequentially adsorb additional H atoms onto the Ni4/support structures up to a total of 6 H atoms (three H2 molecules dissociated). Optimize the geometry at each intermediate coverage (2, 4, 6 H) to obtain the final Ni4H6 configurations.
- Evidence: `/app/outputs/step_3_sequential_h_adsorption.log`

### Step 5: Reactant preparation for hydrogenation NEB
- Role: process
- Action: For each catalyst, create the reactant complexes by adsorbing ethylene (C2H4) onto the Ni4H2 structure (low coverage) and onto the Ni4H6 structure (high coverage). Optimize the co‑adsorbed configurations to serve as initial states for the NEB calculations.
- Evidence: `/app/outputs/step_4_reactant_preparation.log`

### Step 6: Ethylene hydrogenation activation barriers
- Role: scored (load-bearing)
- Action: For each catalyst and each coverage, perform an NEB calculation for the Langmuir–Hinshelwood hydrogenation step where two H atoms migrate from Ni to ethylene to form ethane. Extract the activation barrier as the energy difference between the transition state and the reactant complex. Gather all six barriers and write them to the output JSON file.
- Output file: `/app/outputs/activation_barriers.json`
- Format: json
- Contract: {"low_coverage": {"Ni4/TiO2": number, "Ni4/CeO2": number, "Ni4/BNO": number}, "high_coverage": {"Ni4/TiO2": number, "Ni4/CeO2": number, "Ni4/BNO": number}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_barriers.json
- path: `/app/outputs/activation_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Activation barriers for the Langmuir-Hinshelwood ethylene hydrogenation step under low H coverage (2 H) and high H coverage (6 H) on three supported Ni4 catalysts. Lower values indicate better catalytic performance.
- schema:
  - `type`: object
  - `properties`:
    - `low_coverage`:
      - `type`: object
      - `units`:
        - `*`: eV
      - `required_keys`: `Ni4/TiO2`, `Ni4/CeO2`, `Ni4/BNO`
    - `high_coverage`:
      - `type`: object
      - `units`:
        - `*`: eV
      - `required_keys`: `Ni4/TiO2`, `Ni4/CeO2`, `Ni4/BNO`
  - `required`: `low_coverage`, `high_coverage`

Notes: The barriers must be positive numbers in eV. The ordering Ni4/BNO < Ni4/CeO2 < Ni4/TiO2 must hold at each coverage.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "low_coverage": {
            "type": "object",
            "units": {
              "*": "eV"
            },
            "required_keys": [
              "Ni4/TiO2",
              "Ni4/CeO2",
              "Ni4/BNO"
            ]
          },
          "high_coverage": {
            "type": "object",
            "units": {
              "*": "eV"
            },
            "required_keys": [
              "Ni4/TiO2",
              "Ni4/CeO2",
              "Ni4/BNO"
            ]
          }
        },
        "required": [
          "low_coverage",
          "high_coverage"
        ]
      },
      "description": "Activation barriers for the Langmuir-Hinshelwood ethylene hydrogenation step under low H coverage (2 H) and high H coverage (6 H) on three supported Ni4 catalysts. Lower values indicate better catalytic performance."
    }
  ],
  "notes": "The barriers must be positive numbers in eV. The ordering Ni4/BNO < Ni4/CeO2 < Ni4/TiO2 must hold at each coverage."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/activation_barriers.json` and evaluates the six reported activation barriers. The verifier compares each value to a reference derived from independent DFT calculations that follow the same protocol. The comparison uses a tolerance that accommodates the expected variation between different DFT codes and pseudopotentials, so faithfully re‑running the workflow with reasonable settings is sufficient to score well. In addition, the verifier checks that the relative ordering of the barriers across the three supports is physically consistent at both low and high hydrogen coverage. The final score is a weighted combination of absolute‑value agreement and correct ordering; no single barrier dominates the reward. The intermediate process artifacts (geometry optimizations, NEB convergence, etc.) are not directly scored, but they must be produced because the final barriers depend on them.
