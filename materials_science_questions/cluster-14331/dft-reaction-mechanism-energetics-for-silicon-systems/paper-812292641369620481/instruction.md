# DFT Reaction Mechanism Energetics for Silicon Systems

## Problem background
Kinetic experiments have shown that ground‑state silicon atoms (³P) react with ethylene and acetylene at rates approaching unit collisional efficiency, which implies that the collisions form one or more stable complexes with little or no activation barrier. To rationalize this fast chemistry, it is necessary to explore the triplet potential energy surfaces of SiC₂H₄ and SiC₂H₂ and identify which geometric isomers are the lowest in energy. Understanding the relative stabilities of the possible triplet structures, and the ordering of their energies with respect to the separated fragments, explains why the reactions proceed so efficiently and provides insight into the preferred bonding motifs in organosilicon intermediates.

## Approach
The calculations employ spin‑unrestricted Møller‑Plesset second‑order perturbation theory (UMP2) together with spin projection that removes the two largest spin contaminants (PUMP2). Geometries of candidate triplet isomers and the dissociation fragments (Si(³P) + C₂H₄ / C₂H₂) are optimized with a double‑ζ plus polarization (DZP) basis set. For selected low‑lying isomers, single‑point PUMP2 energies are also computed with a larger triple‑ζ plus double‑polarization (TZ2P) basis set, using the DZP‑optimized geometries. The target quantities are total electronic energies in hartrees and relative enthalpies in kcal/mol, always referenced to the separated ground‑state fragments. The method workflow therefore steps from initial structure generation, through cheap pre‑screening, geometry optimization, and finally energy evaluation at two levels of theory.

## Reproduction target
The task is to produce two JSON files that contain the computed PUMP2 energies for a set of triplet isomers of SiC₂H₄ and SiC₂H₂.
- For SiC₂H₄: compute PUMP2/DZP energies for isomers 1a, 1b, 2, 3, 4b, 6, and for the reference fragments Si(³P) and C₂H₄. Additionally, for isomers 1a, 2, and 3 compute PUMP2/TZ2P energies.
- For SiC₂H₂: compute PUMP2/DZP energies for isomers 19, 20, 21, 22, and for Si(³P) and C₂H₂. For isomers 19 and 20 also compute PUMP2/TZ2P energies.
For every entry report the total energy (in hartree) and the relative energy (kcal/mol) with respect to the appropriate dissociation limit. The two output files must be written to `/app/outputs/sic2h4_energies.json` and `/app/outputs/sic2h2_energies.json` following the schema described in the Output Contract. The relative ordering of the isomer energies—which structure is most stable and how the others rank—must be determined solely from your computed numbers.

## Assets

- Psi4 (or PySCF) open-source quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: Build initial molecular geometries
- Role: process
- Action: Generate initial Cartesian coordinates for all triplet SiC2H4 and SiC2H2 isomers and the dissociation fragments (Si(3P), C2H4, C2H2) based on the structural formulas given in the paper.
- Evidence: none

### Step 2: RHF/STO-3G pre-screening
- Role: process
- Action: Perform restricted Hartree-Fock (RHF) geometry optimizations and harmonic frequency calculations at the STO-3G level to identify true minima among candidate structures.
- Evidence: none

### Step 3: UMP2/DZP geometry optimization
- Role: process
- Action: Optimize the geometries of all verified minima at the unrestricted MP2 level with a DZP basis set (C: Dunning 4s2p + d(0.8); H: p(1.0); Si: Dunning 6s4p + d(0.4)).
- Evidence: none

### Step 4: Compute SiC2H4 isomer energies
- Role: scored (load-bearing)
- Action: At the UMP2/DZP optimized geometries, compute single-point PUMP2/DZP energies for the SiC2H4 triplet isomers (1a,1b,2,3,4b,6) and the fragments Si(3P) and C2H4. For isomers 1a,2,3 additionally compute PUMP2/TZ2P single-point energies (TZ2P: Si 12s9p/9s6p + d(1.86,0.59,0.20); C 10s6p/5s4p + d(1.2,0.4)). Calculate relative energies (kcal/mol) with respect to Si(3P)+C2H4. Write results to /app/outputs/sic2h4_energies.json.
- Output file: `/app/outputs/sic2h4_energies.json`
- Format: json
- Contract: A JSON array of objects, each with string fields "isomer", "symmetry", "basis" (either "DZP" or "TZ2P"), and numeric fields "total_energy_hartree" (hartree) and "relative_energy_kcal_per_mol" (kcal/mol). The array must include entries for the specified isomers and the reference fragments Si and C2H4 at each basis level. No concrete numeric values are provided; compute them from your own calculations.
- Scoring: scored by hidden verifier

### Step 5: Compute SiC2H2 isomer energies
- Role: scored (load-bearing)
- Action: Compute single-point PUMP2/DZP energies for the SiC2H2 triplet isomers (19,20,21,22) and fragments Si(3P) and C2H2. For isomers 19 and 20 also compute PUMP2/TZ2P energies. Calculate relative energies with respect to Si(3P)+C2H2. Write results to /app/outputs/sic2h2_energies.json.
- Output file: `/app/outputs/sic2h2_energies.json`
- Format: json
- Contract: A JSON array of objects, each with string fields "isomer", "symmetry", "basis" (either "DZP" or "TZ2P"), and numeric fields "total_energy_hartree" (hartree) and "relative_energy_kcal_per_mol" (kcal/mol). The array must include entries for the specified isomers and the reference fragments Si and C2H2 at each basis level. No concrete numeric values are provided; compute them from your own calculations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sic2h4_energies.json`
- `/app/outputs/sic2h2_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sic2h4_energies.json
- path: `/app/outputs/sic2h4_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: PUMP2 computed total and relative energies for SiC2H4 triplet isomers
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `isomer`, `symmetry`, `basis`, `total_energy_hartree`, `relative_energy_kcal_per_mol`
    - `properties`:
      - `isomer`:
        - `type`: string
      - `symmetry`:
        - `type`: string
      - `basis`:
        - `type`: string
        - `enum`: `DZP`, `TZ2P`
      - `total_energy_hartree`:
        - `type`: number
      - `relative_energy_kcal_per_mol`:
        - `type`: number
  - `description`: Array of objects for each computed isomer/fragment at each basis level.

### sic2h2_energies.json
- path: `/app/outputs/sic2h2_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: PUMP2 computed total and relative energies for SiC2H2 triplet isomers
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `isomer`, `symmetry`, `basis`, `total_energy_hartree`, `relative_energy_kcal_per_mol`
    - `properties`:
      - `isomer`:
        - `type`: string
      - `symmetry`:
        - `type`: string
      - `basis`:
        - `type`: string
        - `enum`: `DZP`, `TZ2P`
      - `total_energy_hartree`:
        - `type`: number
      - `relative_energy_kcal_per_mol`:
        - `type`: number
  - `description`: Array of objects for each computed isomer/fragment at each basis level.

Notes: The checker compares total_energy_hartree and relative_energy_kcal_per_mol to hidden gold values from the paper's Tables I–IV within tolerances (±0.001 hartree for total energies, relaxed for spin-contaminated structures). Ordering of relative energies (e.g., 1a lowest) is also verified. The TZ2P entries are required only for the specified isomers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sic2h4_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "isomer",
            "symmetry",
            "basis",
            "total_energy_hartree",
            "relative_energy_kcal_per_mol"
          ],
          "properties": {
            "isomer": {
              "type": "string"
            },
            "symmetry": {
              "type": "string"
            },
            "basis": {
              "type": "string",
              "enum": [
                "DZP",
                "TZ2P"
              ]
            },
            "total_energy_hartree": {
              "type": "number"
            },
            "relative_energy_kcal_per_mol": {
              "type": "number"
            }
          }
        },
        "description": "Array of objects for each computed isomer/fragment at each basis level."
      },
      "description": "PUMP2 computed total and relative energies for SiC2H4 triplet isomers"
    },
    {
      "file": "sic2h2_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "isomer",
            "symmetry",
            "basis",
            "total_energy_hartree",
            "relative_energy_kcal_per_mol"
          ],
          "properties": {
            "isomer": {
              "type": "string"
            },
            "symmetry": {
              "type": "string"
            },
            "basis": {
              "type": "string",
              "enum": [
                "DZP",
                "TZ2P"
              ]
            },
            "total_energy_hartree": {
              "type": "number"
            },
            "relative_energy_kcal_per_mol": {
              "type": "number"
            }
          }
        },
        "description": "Array of objects for each computed isomer/fragment at each basis level."
      },
      "description": "PUMP2 computed total and relative energies for SiC2H2 triplet isomers"
    }
  ],
  "notes": "The checker compares total_energy_hartree and relative_energy_kcal_per_mol to hidden gold values from the paper's Tables I–IV within tolerances (±0.001 hartree for total energies, relaxed for spin-contaminated structures). Ordering of relative energies (e.g., 1a lowest) is also verified. The TZ2P entries are required only for the specified isomers."
}
```

## How you are scored
A hidden verifier will read your JSON output files. It compares your reported total energies and relative energies against a reference set of correct values (obtained from the same method and basis sets). For each entry, the reward depends on how close your computed number is to the reference; the closer the match, the higher the score, up to full credit when within the acceptable numerical agreement expected for this methodology. Additionally, the verifier checks that the energy ordering of the isomers (lowest to highest) matches the correct physical ordering; getting the order right contributes further to the reward. The final score is a weighted combination of the accuracies on the DZP and TZ2P data for both molecules. Simply reporting the paper’s published numbers without performing the calculations will not produce the required agreement, because the verifier expects numbers that reflect your own computed run.
