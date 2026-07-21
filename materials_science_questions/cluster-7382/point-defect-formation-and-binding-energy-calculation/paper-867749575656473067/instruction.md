# Hydrogen defect energies in iron from a tight-binding model

## Problem background
Hydrogen embrittlement of iron-based alloys is a critical issue in materials science, limiting the structural integrity of steel. To understand and predict the behaviour of hydrogen in iron, accurate quantum-mechanical methods are needed. Tight-binding (TB) models provide a computationally efficient yet physically grounded description of electronic structure, magnetism, and interatomic forces, balancing speed and accuracy. This task focuses on reproducing the energetics of hydrogen defects in body-centered cubic (bcc) iron using a non-orthogonal sd TB model. By computing dissolution, surface binding, and vacancy segregation energies, one can validate the model's ability to capture the interaction of hydrogen with iron at the atomic scale.

## Approach
The task requires implementing a non-orthogonal tight-binding Hamiltonian with s and d orbitals for iron, and an s orbital for hydrogen. The model includes explicit Slater–Koster hopping and overlap integrals, exponential distance scaling, smooth cutoff functions, a Stoner term for spin polarization, Hubbard‑U corrections, and a repulsive pair-potential. Using the provided Fe–Fe, Fe–H, and H on-site parameters (listed in this document), you will construct total-energy and force calculations.

To evaluate the model, you will perform ionic relaxations in several configurations: (i) a bulk bcc Fe supercell with a single H atom at a tetrahedral or octahedral interstitial site, (ii) a (001) surface slab with H adsorbed at three different sites (quasi‑threefold, hollow, bridge), and (iii) a bcc supercell containing a vacancy, to which H atoms are added sequentially up to seven. From the relaxed total energies, you will calculate the dissolution energies, surface binding energies, and vacancy segregation energies as defined in the workflow steps.

## Reproduction target
Your goal is to produce a JSON file containing the following computed hydrogen defect energies, all in eV:
- Dissolution energy of H at the tetrahedral (TET) and octahedral (OCT) interstitial sites in bulk bcc Fe.
- Binding energy of H to the Fe(001) surface at the quasi‑threefold (QT), hollow (H), and bridge (B) adsorption sites.
- Segregation energy of H to a monovacancy in bcc Fe for n = 1 to 7 H atoms trapped, i.e., the energy gained by moving a H atom from a bulk tetrahedral site to a vacancy already containing n‑1 H atoms.

These energies must be computed by running the tight-binding relaxations and applying the appropriate energy differences. The H₂ molecular reference energy is taken as −4.75 eV. The output file must conform to the JSON schema specified in the workflow step 5 and the output contract.

## Assets

- Python 3: python3
- numpy: numpy
- scipy: scipy
- Tight-binding model parameters for Fe and Fe–H (described in detail below)

## Tight-binding model parameters

The tight-binding model uses an exponential distance scaling h(r)=h0 exp(-q r) and s(r)=s0 exp(-q r) (in atomic Rydberg units: 1 Ry = 13.61 eV, 1 bohr = 0.529 Å). All hopping and overlap integrals are smoothly cut off between distances r1 and rc using a fifth-degree polynomial that matches value, slope, and curvature at both ends.

### Fe–Fe interactions (from Table I of the paper)

| parameter | h0 (Ry) | q (bohr⁻¹) |
|-----------|---------|------------|
| h_ddσ     | -3.84   | 1.0        |
| h_ddπ     |  2.56   | 1.0        |
| h_ddδ     | -0.66   | 1.0        |
| h_ssσ     | -0.35   | 1.0        |
| h_sdσ     | -0.14   | 1.0        |
| s_ssσ     |  0.27   | 1.0        |
| s_sdσ     |  0.22   | 1.0        |

Stoner parameter I = 0.07 Ry. Hubbard U values: U_Fe = 1.0 Ry, U_H = 1.2 Ry. The repulsive pair potential is φ(r)=B1 e^{-p1 r} - B2 e^{-p2 r} with B1=200, B2=100, p1=3.279, p2=1.626 (all in Ry, bohr⁻¹). Cutoffs for hopping and overlap integrals: r1 = 1.1 a, rc = 1.4 a, where a=2.87 Å (5.423 bohr) is the bcc lattice constant. For the pair potential, the same cutoffs r1=1.1 a, rc=1.4 a apply.

### Fe–H and H on-site parameters (from Table V of the paper)

| parameter | value (Ry) | q (bohr⁻¹) |
|-----------|------------|------------|
| ε_s - ε_d (H on-site relative to Fe d) | -0.085 | -          |
| h_ss (Fe–H) | -0.35    | 1.0        |
| h_sd (Fe–H) | -0.14    | 1.0        |
| s_ss (Fe–H) |  0.27    | 1.0        |
| s_sd (Fe–H) |  0.22    | 1.0        |
| Fe–H pair potential: B=299.6 Ry·bohr, p=2.6922 bohr⁻¹, φ(r)=B/r e^{-p r} | | |
| Cutoffs: for hopping/overlap r1=0.8 a, rc=2.0 a; for pair potential r1=0.8 a, rc=0.95 a. | | |

The H₂ reference energy (bond energy) is taken as -4.75 eV.

## Workflow steps

### Step 1: Implement the non-orthogonal sd tight-binding model for Fe–H
- Role: process
- Action: Write the computational engine that constructs the Hamiltonian and overlap matrices for Fe and Fe–H systems using the two-center Slater–Koster formalism, exponential distance scaling, smooth polynomial cutoffs, a Stoner model for magnetism, Hubbard‑U terms, and pair potentials. Use the Fe–Fe and Fe–H parameters exactly as provided.
- Evidence: `/app/outputs/tb_model_check.log`

### Step 2: Compute hydrogen dissolution energies in bulk iron
- Role: process
- Action: Build a bcc Fe supercell (e.g., 54 atoms), place a single H atom at a tetrahedral and an octahedral interstitial site, relax ionic positions using Hellmann–Feynman forces from the TB model while keeping the supercell volume fixed, and record the relaxed total energies.
- Evidence: `/app/outputs/dissolution_raw_energies.json`

### Step 3: Compute hydrogen surface binding energies
- Role: process
- Action: Construct a (001) slab of bcc Fe (e.g., 2×2×5 with vacuum), relax the clean slab, then place one H atom at each of the quasi‑threefold, hollow, and bridge adsorption sites and relax all atomic coordinates. Record the total energies.
- Evidence: `/app/outputs/surface_raw_energies.json`

### Step 4: Compute hydrogen‑vacancy segregation energies
- Role: process
- Action: Introduce a vacancy in a bcc Fe supercell (e.g., 53 atoms), then sequentially add 1 to 7 H atoms at the six {001} face‑centered octahedral sites adjacent to the vacancy (and finally at the vacancy center). After each addition, relax all atomic positions and record the total energy.
- Evidence: `/app/outputs/vacancy_raw_energies.json`

### Step 5: Compile hydrogen defect energies
- Role: scored (load-bearing)
- Action: Using the total energies obtained in the previous steps and the H₂ reference energy (given in the task instruction), calculate: dissolution energies at tetrahedral and octahedral sites as E(Fe54H) - E(Fe54) - ½ E(H₂); surface binding energies using the tetrahedral dissolution energy minus the adsorption energy for each surface site; and vacancy segregation energies for n=1..7 via the sequential energy difference formula. Write all values in eV to /app/outputs/h_fe_defect_energies.json.
- Output file: `/app/outputs/h_fe_defect_energies.json`
- Format: json
- Contract: {"dissolution_energy_TET": float, "dissolution_energy_OCT": float, "surface_binding_QT": float, "surface_binding_H": float, "surface_binding_B": float, "vacancy_segregation_n1": float, "vacancy_segregation_n2": float, "vacancy_segregation_n3": float, "vacancy_segregation_n4": float, "vacancy_segregation_n5": float, "vacancy_segregation_n6": float, "vacancy_segregation_n7": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/h_fe_defect_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### h_fe_defect_energies.json
- path: `/app/outputs/h_fe_defect_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed hydrogen defect energies in bcc iron from the non-orthogonal sd tight-binding model.
- schema:
  - `type`: object
  - `properties`:
    - `dissolution_energy_TET`:
      - `type`: number
      - `unit`: eV
    - `dissolution_energy_OCT`:
      - `type`: number
      - `unit`: eV
    - `surface_binding_QT`:
      - `type`: number
      - `unit`: eV
    - `surface_binding_H`:
      - `type`: number
      - `unit`: eV
    - `surface_binding_B`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n1`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n2`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n3`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n4`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n5`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n6`:
      - `type`: number
      - `unit`: eV
    - `vacancy_segregation_n7`:
      - `type`: number
      - `unit`: eV
  - `required`: `dissolution_energy_TET`, `dissolution_energy_OCT`, `surface_binding_QT`, `surface_binding_H`, `surface_binding_B`, `vacancy_segregation_n1`, `vacancy_segregation_n2`, `vacancy_segregation_n3`, `vacancy_segregation_n4`, `vacancy_segregation_n5`, `vacancy_segregation_n6`, `vacancy_segregation_n7`

Notes: The H₂ reference energy (bond energy) is provided in the task instruction. All energies are total-energy differences as described in the public workflow steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "h_fe_defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "dissolution_energy_TET": {
            "type": "number",
            "unit": "eV"
          },
          "dissolution_energy_OCT": {
            "type": "number",
            "unit": "eV"
          },
          "surface_binding_QT": {
            "type": "number",
            "unit": "eV"
          },
          "surface_binding_H": {
            "type": "number",
            "unit": "eV"
          },
          "surface_binding_B": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n1": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n2": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n3": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n4": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n5": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n6": {
            "type": "number",
            "unit": "eV"
          },
          "vacancy_segregation_n7": {
            "type": "number",
            "unit": "eV"
          }
        },
        "required": [
          "dissolution_energy_TET",
          "dissolution_energy_OCT",
          "surface_binding_QT",
          "surface_binding_H",
          "surface_binding_B",
          "vacancy_segregation_n1",
          "vacancy_segregation_n2",
          "vacancy_segregation_n3",
          "vacancy_segregation_n4",
          "vacancy_segregation_n5",
          "vacancy_segregation_n6",
          "vacancy_segregation_n7"
        ]
      },
      "description": "Computed hydrogen defect energies in bcc iron from the non-orthogonal sd tight-binding model."
    }
  ],
  "notes": "The H₂ reference energy (bond energy) is provided in the task instruction. All energies are total-energy differences as described in the public workflow steps."
}
```

## How you are scored
A hidden verifier evaluates your submission by reading the `/app/outputs/h_fe_defect_energies.json` file. The verifier compares each energy value against a set of reference values with numerical tolerances appropriate for computational reproducibility. The score is a weighted combination of the accuracy of all twelve energies, with emphasis on the dissolution and vacancy segregation results. Consistency checks (e.g., the sign of certain segregation energies) may also be applied. Note that only the final defect energies are scored; intermediate raw energy files are not directly graded. Therefore, you must implement the full tight-binding model and perform the calculations honestly: simply guessing or hard‑coding the expected numbers will not match the required accuracy and will result in a low score.
