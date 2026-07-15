# Tight-binding optimization and electronic property analysis of Si45 cluster isomers

## Problem background
Silicon clusters have attracted attention because their reactivity with molecules such as ammonia and methanol varies dramatically with cluster size; certain sizes, including Si45, appear comparatively unreactive. The geometric and electronic structure of the Si45 cluster is expected to provide an explanation. The paper compares several candidate isomers for Si45 and presents two new tetrahedral-symmetry structures, labeled T1 and T2. Using a tight‑binding (TB) model, it computes optimized geometries and electronic properties (cohesion energy, HOMO‑LUMO gap, bond topology) for these isomers at two different bond cutoff distances (3.1 Å and 3.3 Å). An open question addressed in the paper is whether the T2 isomer undergoes a Jahn–Teller distortion when the larger cutoff is used; such a distortion would alter the electronic structure and bond topology. This task requires you to reproduce the TB‑computed properties of the T1 and T2 isomers by implementing the model, performing geometry optimizations, and assessing whether a distortion occurs.

## Approach
Implement the Tománek–Schlüter tight‑binding model as described in the reference paper (Phys. Rev. B 36, 1208, 1987). The model uses a non‑orthogonal s‑p basis with parameters fitted to bulk silicon. It consists of a band‑structure energy term (including on‑site energies, hopping integrals, and an intra‑cluster Coulombic repulsion term), a diatomic repulsion term E_d(R) fitted to ab initio dimer data, and a coordination‑number‑dependent repulsive correction that accounts for the cluster environment. The total cohesion energy per cluster is obtained by summing these contributions and is reported relative to 45 isolated atoms.

Geometry optimization is performed by first using Hellmann‑Feynman forces to approach equilibrium, followed by a large number of variational steps. For cases where tetrahedral (Td) symmetry is required, the optimization is constrained to preserve that symmetry. For asymmetrical (unconstrained) optimizations, the structure is allowed to fully relax. The procedure is repeated for two bond cutoff distances, 3.1 Å and 3.3 Å, because the appropriate cutoff for clusters is ambiguous.

After optimization, for each structure the following quantities are computed: (i) total cohesion energy, (ii) HOMO‑LUMO gap, (iii) the number of bonds within the given cutoff distance, (iv) the bond margin (the difference between the longest bond and the shortest non‑bonded interatomic distance), and (v) the longest bond length. The combination of symmetrical and unconstrained optimizations at two cutoffs probes the stability and electronic structure of the T1 and T2 isomers, including the possible Jahn–Teller distortion in T2.

## Reproduction target
Your goal is to produce a single JSON file that contains the computed cluster properties for the five cases listed below. For each case you must report the structure identifier, the bond cutoff used, the cohesion energy (eV), the HOMO‑LUMO gap (eV), the number of bonds, the bond margin (Å), and the longest bond length (Å). The five required cases are:

- T1_sym_3.3: T1 optimized with Td symmetry and a 3.3 Å cutoff.
- T2_sym_3.1: T2 optimized with Td symmetry and a 3.1 Å cutoff.
- T2_sym_3.3: T2 optimized with Td symmetry and a 3.3 Å cutoff.
- T2_asym_3.1: T2 optimized without symmetry constraints (unconstrained) at 3.1 Å.
- T2_asym_3.3: T2 optimized without symmetry constraints at 3.3 Å.

Save the results in `/app/outputs/properties.json` following exactly the output schema described in the output contract.

## Assets

- Tománek-Schlüter tight-binding model paper: 10.1103/PhysRevB.36.1208

## Workflow steps

### Step 1: Prepare initial T1 and T2 structures
- Role: process
- Action: Construct initial atomic coordinates for T1 from the explicit Cartesian coordinates given in the instruction (extracted from the paper's Table II). Build T2 by taking T1 and moving each of the four cap atoms (type IV) inward along the line from the cluster center toward each cap so that the cap-central distance becomes approximately 3.2 Å (ensuring bonding at the 3.3 Å cutoff) while maintaining Td symmetry. Save the coordinates as initial_T1.xyz and initial_T2.xyz.
- Evidence: `/app/outputs/initial_T1.xyz, initial_T2.xyz`

### Step 2: Tight-binding geometry optimization
- Role: process
- Action: Implement the Tománek‑Schlüter tight‑binding model using the parameterization from Phys. Rev. B 36, 1208 (1987). Perform global geometry optimization for each required case: (1) T1 symmetrical at 3.3 Å cutoff, (2) T2 symmetrical at 3.1 Å cutoff, (3) T2 symmetrical at 3.3 Å cutoff, (4) T2 asymmetrical (unconstrained) at 3.1 Å cutoff, (5) T2 asymmetrical at 3.3 Å cutoff. For symmetrical cases, enforce Td symmetry during optimization. Use Hellmann‑Feynman forces and iterative variational steps (the agent may choose the number of steps, at least 1800) following the protocol described in the paper. Save the final optimized geometries for each case as separate XYZ files.
- Evidence: `/app/outputs/opt_T1_sym_3.3.xyz, opt_T2_sym_3.1.xyz, opt_T2_sym_3.3.xyz, opt_T2_asym_3.1.xyz, opt_T2_asym_3.3.xyz`

### Step 3: Compute cluster properties
- Role: scored (load-bearing)
- Action: For each of the five optimized structures, compute: (i) cohesion energy (eV) relative to the energy of 45 isolated atoms, (ii) HOMO‑LUMO gap (eV), (iii) number of bonds using the corresponding cutoff distance, (iv) bond margin (Å) defined as the difference between the longest bond and the shortest non‑bonded interatomic distance, and (v) longest bond length (Å). Collect all results into a single JSON file.
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: An array of five objects. Each object has keys: structure (string, one of 'T1_sym_3.3', 'T2_sym_3.1', 'T2_sym_3.3', 'T2_asym_3.1', 'T2_asym_3.3'), cutoff (float, Å), energy (float, eV), band_gap (float, eV), num_bonds (int), margin (float, Å), long_bond (float, Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed properties of the five Si45 cluster cases. Each entry contains the structure identifier, bond cutoff, cohesion energy, HOMO‑LUMO gap, number of bonds, bond margin, and longest bond length.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `structure`, `cutoff`, `energy`, `band_gap`, `num_bonds`, `margin`, `long_bond`
    - `properties`:
      - `structure`:
        - `type`: string
      - `cutoff`:
        - `type`: number
        - `unit`: Å
      - `energy`:
        - `type`: number
        - `unit`: eV
      - `band_gap`:
        - `type`: number
        - `unit`: eV
      - `num_bonds`:
        - `type`: integer
      - `margin`:
        - `type`: number
        - `unit`: Å
      - `long_bond`:
        - `type`: number
        - `unit`: Å

Notes: The agent’s computed values will be compared to hidden reference values from the original study. Tolerances are not disclosed. The Jahn‑Teller distortion of T2 at 3.3 Å is implicitly verified through the reported properties (gap, number of bonds).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "structure",
            "cutoff",
            "energy",
            "band_gap",
            "num_bonds",
            "margin",
            "long_bond"
          ],
          "properties": {
            "structure": {
              "type": "string"
            },
            "cutoff": {
              "type": "number",
              "unit": "Å"
            },
            "energy": {
              "type": "number",
              "unit": "eV"
            },
            "band_gap": {
              "type": "number",
              "unit": "eV"
            },
            "num_bonds": {
              "type": "integer"
            },
            "margin": {
              "type": "number",
              "unit": "Å"
            },
            "long_bond": {
              "type": "number",
              "unit": "Å"
            }
          }
        }
      },
      "description": "Computed properties of the five Si45 cluster cases. Each entry contains the structure identifier, bond cutoff, cohesion energy, HOMO‑LUMO gap, number of bonds, bond margin, and longest bond length."
    }
  ],
  "notes": "The agent’s computed values will be compared to hidden reference values from the original study. Tolerances are not disclosed. The Jahn‑Teller distortion of T2 at 3.3 Å is implicitly verified through the reported properties (gap, number of bonds)."
}
```

## How you are scored
A hidden verifier will read your `properties.json`. For each reported numeric quantity (cohesion energy, HOMO‑LUMO gap, number of bonds, bond margin, longest bond length) the verifier compares your value to a hidden reference value derived from the paper’s original calculations, using pre‑set tolerances. It also checks whether the computed properties satisfy structural‑consistency criteria derived from the expected Jahn–Teller distortion behavior (for example, changes in band gap and bond count between symmetry‑constrained and unconstrained optimizations). The overall score is a weighted fraction of the required quantities that fall within the allowed tolerances and consistency criteria; the closer your values are to the references (or the better they satisfy the structural criteria), the higher your score. Reporting numbers without performing the genuine TB optimization and property extraction will result in a low score.
