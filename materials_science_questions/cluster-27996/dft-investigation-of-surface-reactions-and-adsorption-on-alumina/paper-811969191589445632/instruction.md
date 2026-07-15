# Quantum Chemical Study of Surface Hydroxyl and Lewis Acid Effects on Perfluoroethers

## Problem background
Perfluoropolyalkylethers (PFPEs) are high‑performance lubricants used in aerospace and industrial applications, but they can decompose on metal oxide surfaces under tribological conditions. The decomposition mechanism has been debated: some studies attribute it to Lewis acid surface sites (e.g., Al³⁺ sites on alumina), while others implicate surface hydroxyl groups. This work uses quantum chemical calculations to investigate the interaction of perfluorodimethylether (PDME) and perfluorodiethylether (PDEE) with a model Lewis acid (BF₃) and with different hydroxyl species (OH, OH⁺, OH⁻) to gain insight into the reactivity of these surfaces. The key question is whether Lewis acid sites or hydroxyl groups are primarily responsible for perfluoroether decomposition.

## Approach
The study employs the AM1 semiempirical self‑consistent field molecular orbital method, as implemented in the open‑source program MOPAC. All calculations are performed using the unrestricted Hartree–Fock (UHF) option with the lowest spin multiplicity. Geometry optimization is carried out for each isolated molecule and for each interacting pair (complex). The following molecules are studied in isolation: PDME, DEE, PDEE, OH, OH⁺, OH⁻, BF₃, and NH₃ (the latter used as a validation case). Complexes are formed by bringing the two components together and optimizing: BF₃ with DEE (BF₃ approaching the ether oxygen), BF₃ with PDEE (BF₃ approaching the ether oxygen), OH with PDME (neutral OH approaching the ether oxygen), OH⁺ with PDME (approaching the ether oxygen), and OH⁻ with PDME (OH⁻ approaching a perfluoromethyl carbon). Additionally, the BF₃+NH₃ adduct is computed for validation. For each system, the total energy is obtained after optimization, and critical interatomic distances are extracted. Interaction energies are defined as the difference between the total energy of the complex and the sum of the total energies of the isolated fragments.

## Reproduction target
Produce a single JSON file, `results.json`, containing the total energy (in kJ/mol) and the specified key interatomic distances (in Å) for all 15 systems: the nine isolated molecules and the six complexes listed in the workflow steps. The key distances to report are: B–N in BF₃+NH₃, B–O in BF₃+DEE, B–O in BF₃+PDEE, O(ether)–H in OH+PDME, H–O(ether) and H–O(hydroxyl) in OH⁺+PDME, and O(hydroxyl)–C(ether) in OH⁻+PDME. The results will be evaluated by a hidden verifier that recomputes interaction energies and checks the agreement of these energies and distances against reference values, as well as the correct relative ordering of interaction strengths among the different systems.

## Assets

- MOPAC: http://openmopac.net/

## Workflow steps

### Step 1: Prepare molecular geometries for AM1 calculations
- Role: process
- Action: Build initial molecular geometries for all required isolated molecules (PDME, DEE, PDEE, OH, OH+, OH-, BF3, NH3) and for the complex starting structures (BF3+NH3, BF3+DEE, BF3+PDEE, OH+PDME at O site, OH++PDME at O site, OH-+PDME at C site). Write the geometries in a format readable by MOPAC (e.g., XYZ or Z-matrix) and produce a summary log file confirming the prepared input files.
- Evidence: `/app/outputs/step_01_input_preparation.log`

### Step 2: Run AM1 optimizations and collect energies and distances
- Role: scored (load-bearing)
- Action: For each system listed below, perform an AM1 UHF geometry optimization (lowest spin multiplicity) using MOPAC. Record the optimized total energy in kJ/mol and the specified key interatomic distances. Systems: isolated PDME, OH, OH+, OH-, BF3, DEE, PDEE, NH3; complexes: BF3+NH3, BF3+DEE (BF3 approaching O), BF3+PDEE (BF3 approaching O), OH+PDME (neutral OH approaching ether O), OH++PDME (OH+ approaching ether O), OH-+PDME (OH- approaching a perfluoromethyl carbon). Key distances to extract: BF3-NH3 – B‑N distance; BF3-DEE – B‑O distance; BF3-PDEE – B‑O distance; OH-PDME – O(ether)–H(OH); OH+-PDME – H–O(ether) and H–O(hydroxyl); OH--PDME – O(hydroxyl)–C(ether). Write all results into a single JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with a top-level key 'systems' (array). Each element has keys: 'system' (string, e.g. 'PDME_isolated'), 'total_energy_kjmol' (number), 'key_distances' (object whose keys are distance names. For the complex systems, the keys MUST be exactly (case-sensitive): 'B_N' for BF3_NH3; 'B_O' for BF3_DEE and BF3_PDEE; 'O_ether_H_OH' for OH_PDME; 'H_O_ether' and 'H_O_hydroxyl' for OH+_PDME; 'O_OH_C_ether' for OH-_PDME). All values are numbers in Angstrom.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The agent's computed AM1 total energies and key intermolecular distances. The checker will recompute interaction energies as E(complex) minus the sum of the corresponding isolated fragment energies, then compare to paper reference values, using the exact distance key names specified.
- schema:
  - `type`: object
  - `required`: `systems`
  - `properties`:
    - `systems`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `system`, `total_energy_kjmol`, `key_distances`
        - `properties`:
          - `system`:
            - `type`: string
          - `total_energy_kjmol`:
            - `type`: number
          - `key_distances`:
            - `type`: object
  - `key_requirements`: For complex systems, key_distances must contain the exact keys (case-sensitive): BF3_NH3 -> B_N; BF3_DEE, BF3_PDEE -> B_O; OH_PDME -> O_ether_H_OH; OH+_PDME -> H_O_ether, H_O_hydroxyl; OH-_PDME -> O_OH_C_ether.

Notes: The scored artifact covers both the BF3/perfluoroether Lewis acid test and the OH/PDME interaction pathways. The BF3+NH3 validation system is included for completeness but is not required for the paper's main conclusions; its absence would not be penalized.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "systems"
        ],
        "properties": {
          "systems": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "system",
                "total_energy_kjmol",
                "key_distances"
              ],
              "properties": {
                "system": {
                  "type": "string"
                },
                "total_energy_kjmol": {
                  "type": "number"
                },
                "key_distances": {
                  "type": "object"
                }
              }
            }
          }
        },
        "key_requirements": "For complex systems, key_distances must contain the exact keys (case-sensitive): BF3_NH3 -> B_N; BF3_DEE, BF3_PDEE -> B_O; OH_PDME -> O_ether_H_OH; OH+_PDME -> H_O_ether, H_O_hydroxyl; OH-_PDME -> O_OH_C_ether."
      },
      "description": "The agent's computed AM1 total energies and key intermolecular distances. The checker will recompute interaction energies as E(complex) minus the sum of the corresponding isolated fragment energies, then compare to paper reference values, using the exact distance key names specified."
    }
  ],
  "notes": "The scored artifact covers both the BF3/perfluoroether Lewis acid test and the OH/PDME interaction pathways. The BF3+NH3 validation system is included for completeness but is not required for the paper's main conclusions; its absence would not be penalized."
}
```

## How you are scored
A hidden verifier reads your `results.json`, extracts the reported total energies and distances, and independently recalculates each interaction energy as E(complex) – Σ E(isolated fragments). It then compares these interaction energies and the key distances to concealed reference values derived from the published study. Scoring is based on the accuracy of these computed quantities within allowed tolerances, and on whether the relative ordering of interaction strengths among the different systems matches the hidden reference trends. Each system contributes a weighted share to the total reward, with the main interaction systems carrying the greatest weight. Simply reporting numbers identical to the published paper is not sufficient; your submitted results must be the output of genuine AM1 computations.
