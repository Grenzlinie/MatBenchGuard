# DFT+U defect energetics and magnetic coupling in a transition-metal doped oxide

## Problem background
Diluted magnetic semiconductors (DMS) such as Co-doped TiO₂ promise spintronic devices that exploit both charge and spin. A key obstacle is distinguishing intrinsic carrier-mediated ferromagnetism from extrinsic effects caused by dopant clustering. Understanding the defect chemistry and magnetic coupling in anatase Co:TiO₂ is essential to identify growth conditions that yield uniform, intrinsic ferromagnetism. First-principles DFT+U calculations can reveal the relative stability of different defect configurations, their charge states, magnetic moments, and the energetic preference for ferromagnetic versus antiferromagnetic ordering, thereby explaining why low oxygen partial pressure during growth promotes intrinsic magnetism.

## Approach
Perform spin-polarized GGA+U density functional theory (DFT) calculations on anatase TiO₂ supercells. Build a pristine bulk supercell and relax it to obtain a reference total energy. Then introduce individual point defects: Co substitutional (Co_Ti), Co interstitial (Co_int), oxygen vacancy (V_O), Ti interstitial (Ti_int), and a Co_Ti+V_O complex. For each defect type, consider several charge states. After relaxing each defect supercell, record the total energy and spin magnetic moment. Next, construct supercells containing pairs of Co_Ti atoms and Co_Ti+V_O complexes at several separation distances. For each pair configuration, compute total energies for both ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments. Finally, use the computed total energies to derive defect formation energies as a function of the Fermi energy, identify the stable charge states, and extract the magnetic moments. Compute the relative interaction energies of the pairs and complexes as a function of separation, and determine the energy difference between FM and AFM ordering for the nearest-neighbor neutral Co_Ti pair. All final quantities are compared with the trends and values reported in the computational study.

## Reproduction target
Using DFT+U calculations on anatase TiO₂ supercells, compute the following and write the results to a JSON file: (i) defect formation energies for Co_int, V_O, Ti_int, Co_Ti, and Co_Ti+V_O as a function of the Fermi level; (ii) spin magnetic moments of the stable charge states of each defect; (iii) relative total energies (interaction energies) of neutral and charged Co_Ti pairs and Co_Ti+V_O complexes as a function of the separation distance; (iv) the energy difference between ferromagnetic and antiferromagnetic spin ordering for the nearest-neighbor neutral Co_Ti pair. A hidden verifier will evaluate the submitted results using reference values and structural consistency checks. The exact scoring criteria are not disclosed.

## Assets

- Open-source DFT code with DFT+U support (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- Anatase TiO2 crystal structure

## Workflow steps

### Step 1: Bulk anatase reference DFT calculation
- Role: process
- Action: Set up a supercell of anatase TiO2 and perform spin-polarized GGA+U DFT relaxation to obtain the reference total energy and relaxed structure.
- Evidence: `/app/outputs/bulk_ref.log`

### Step 2: Single-defect DFT simulations
- Role: process
- Action: Using the relaxed bulk structure, create supercells with individual defects: Co substitutional (Co_Ti), Co interstitial (Co_int), oxygen vacancy (V_O), Ti interstitial (Ti_int), and Co_Ti+V_O complex. For each defect type, set up relevant charge states as described in the paper and perform spin-polarized GGA+U DFT relaxation, recording total energy and spin magnetic moments.
- Evidence: `/app/outputs/single_defect_raw.json`

### Step 3: Defect pair and cluster DFT simulations
- Role: process
- Action: Construct supercells with neutral and charged Co_Ti pairs at varying separation distances and with Co_Ti+V_O complexes at varying separations. For each pair configuration, compute total energies for both ferromagnetic and antiferromagnetic spin alignments using spin-polarized GGA+U DFT.
- Evidence: `/app/outputs/pair_energies_raw.json`

### Step 4: Defect formation energy and magnetic analysis
- Role: scored (load-bearing)
- Action: From the raw total energies of all previous calculations, compute defect formation energies as a function of Fermi energy using the standard formalism. Determine stable charge states, extract spin magnetic moments for each defect configuration, compute relative interaction energies for pairs and complexes as a function of separation, and calculate the energy difference between ferromagnetic and antiferromagnetic ordering for the nearest-neighbor neutral Co_Ti pair. Output all computed quantities in a single JSON file.
- Output file: `/app/outputs/defect_results.json`
- Format: json
- Contract: {"type": "object", "properties": {"formation_energies": {"type": "object", "description": "Mapping from defect label (e.g. 'Co_Ti', 'V_O', ...) to an object mapping charge state to formation energy in eV."}, "magnetic_moments": {"type": "object", "description": "Mapping from defect label to an object mapping charge state to spin magnetic moment in μB."}, "pair_energies": {"type": "object", "description": "Mapping from pair type label (e.g. 'Co_Ti-Co_Ti_neutral') to an object mapping separation distance (in Å) to relative total energy in eV."}, "FM_AFM_difference": {"type": "object", "description": "Object with pair type as key and energy difference (FM minus AFM) in eV."}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_results.json
- path: `/app/outputs/defect_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the reproduced defect formation energies, magnetic moments, pair interaction energies, and FM-AFM energy differences for Co-doped TiO2, as computed by the agent's DFT+U workflow.
- schema:
  - `type`: object
  - `required`: `formation_energies`, `magnetic_moments`, `pair_energies`, `FM_AFM_difference`
  - `properties`:
    - `formation_energies`:
      - `type`: object
      - `description`: Keys: defect labels (e.g. Co_Ti, Co_int, V_O, Ti_int, Co_Ti+V_O). Values: objects mapping charge state (e.g. 0, +2, -2) to formation energy in eV.
    - `magnetic_moments`:
      - `type`: object
      - `description`: Keys: defect labels. Values: objects mapping charge state to spin magnetic moment in μB.
    - `pair_energies`:
      - `type`: object
      - `description`: Keys: pair type labels (e.g. Co_Ti-Co_Ti_neutral, Co_Ti-Co_Ti_charged). Values: objects mapping separation distance (in Å) to relative total energy in eV.
    - `FM_AFM_difference`:
      - `type`: object
      - `description`: Keys: pair type labels. Values: energy difference (E_FM - E_AFM) in eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "formation_energies",
          "magnetic_moments",
          "pair_energies",
          "FM_AFM_difference"
        ],
        "properties": {
          "formation_energies": {
            "type": "object",
            "description": "Keys: defect labels (e.g. Co_Ti, Co_int, V_O, Ti_int, Co_Ti+V_O). Values: objects mapping charge state (e.g. 0, +2, -2) to formation energy in eV."
          },
          "magnetic_moments": {
            "type": "object",
            "description": "Keys: defect labels. Values: objects mapping charge state to spin magnetic moment in μB."
          },
          "pair_energies": {
            "type": "object",
            "description": "Keys: pair type labels (e.g. Co_Ti-Co_Ti_neutral, Co_Ti-Co_Ti_charged). Values: objects mapping separation distance (in Å) to relative total energy in eV."
          },
          "FM_AFM_difference": {
            "type": "object",
            "description": "Keys: pair type labels. Values: energy difference (E_FM - E_AFM) in eV."
          }
        }
      },
      "description": "Contains the reproduced defect formation energies, magnetic moments, pair interaction energies, and FM-AFM energy differences for Co-doped TiO2, as computed by the agent's DFT+U workflow."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read the output JSON file `defect_results.json` and compare the submitted formation energies, magnetic moments, pair energies, and FM-AFM energy difference against reference values and structural trends. The scoring criteria are based on consistency with DFT-computed quantities and are not disclosed in detail. Full credit is awarded if all checks pass; partial credit may be given otherwise. Reporting numbers that are not supported by actual DFT runs will be detectable by the verifier's consistency checks.
