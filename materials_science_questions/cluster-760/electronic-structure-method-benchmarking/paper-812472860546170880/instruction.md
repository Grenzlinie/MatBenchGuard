# DFT Benchmarking of PEDOT:PSS Ground-State Properties

## Problem background
Poly(3,4-ethylenedioxythiophene) polystyrene sulfonate (PEDOT:PSS) is a key conductive polymer complex for flexible electronics. Density functional theory (DFT) is widely used to probe its molecular-scale properties, yet no systematic validation of density functionals has been performed for this system. This task benchmarks 17 density functionals on ground-state properties (geometries, vibrational spectra, polarizabilities, interaction energies, delocalization error, exciton stability, torsional barriers) against the double-hybrid DSD-PBEP86 reference, producing a set of error metrics that quantify each functional’s accuracy. The goal is to determine which functionals faithfully reproduce the properties of PEDOT:PSS-related molecules, enabling more reliable computational design of conductive polymer devices.

## Approach
The approach follows a reference-based benchmarking workflow. First, initial 3D geometries of all benchmarked molecules and complexes (PEDOT oligomers, EDOT, Tos-H, EMIM⁺, TFSI⁻, and their non-covalent complexes) are constructed. A high-accuracy reference is computed using the double-hybrid functional DSD-PBEP86 with appropriate basis sets, yielding reference geometries, vibrational frequencies, polarizabilities, interaction energies, delocalization error curves, singlet‑triplet energy gap for PEDOT₆²⁺, and torsion barrier heights. Then, each of 17 density functionals spanning GGA, meta-GGA, global-hybrid, and range-separated LC classes is evaluated on the same property set. For every property, the deviation of each functional from the DSD-PBEP86 reference is quantified (mean absolute errors, signed errors, percent errors). All results are aggregated into a single JSON artifact whose schema is defined in the output contract. The comparison is made on a per-functional basis, covering the full set of properties that influence the morphology and electronic behavior of PEDOT:PSS films.

## Reproduction target
Produce a file `/app/outputs/benchmark_results.json` containing, for each of the 17 density functionals, the error metrics against the DSD-PBEP86 reference for the following properties: intramolecular geometry (MAE in pm), vibrational spectrum (MAE in cm⁻¹), polarizability (MAE in percent), ion‑exchange energy (signed error in kcal/mol), non‑covalent interaction energy (MAE in kcal/mol), delocalization error (extremal deviation in kcal/mol), torsional barrier height (signed error in kcal/mol), and singlet‑triplet energy gap ΔEₛₜ (in kcal/mol). The JSON must be an array of objects, each with a `functional` field and numeric keys for the metrics listed above; missing or inapplicable quantities should be stored as `null`. The artifact must follow the schema defined in the output contract exactly. This artifact serves as the scored reproduction of the benchmark study.

## Assets

- Psi4: https://psicode.org/

## Workflow steps

### Step 1: Prepare molecular structures
- Role: process
- Action: Build initial 3D geometries for all molecules and complexes used in the benchmark: PEDOT3 (neutral and cation), PEDOT6^2+ (bipolaronic and pair-polaronic), EDOT monomer, Tos-H, EMIM^+, TFSI^-, and their non-covalent complexes (EDOT...EDOT, Tos-H...Tos-H, PD3^+...Tos^-, EMIM^+...TFSI^-, PD3^+...TFSI^-, EMIM^+...Tos^-). Use standard chemical knowledge; perform initial low-level optimization if needed.
- Evidence: `/app/outputs/initial_geometries.json`

### Step 2: Generate DSD-PBEP86 reference data
- Role: process
- Action: Perform all reference calculations with the double-hybrid DSD-PBEP86 functional as implemented in Psi4: (a) geometry optimizations at DSD-PBEP86/aug-cc-pVDZ for small molecules; (b) harmonic vibrational frequencies and static polarizabilities at the same level; (c) single-point energies at DF-DSD-PBEP86/jun-cc-pV(T+d)Z on complex geometries to obtain reference interaction energies, ion-exchange energy, and singlet-triplet energy gap for PEDOT6^2+; (d) fractional electron calculations on PEDOT3 to obtain the delocalization error curve; (e) relaxed torsion scan energies for bipolaronic PEDOT6^2+ to extract the torsion barrier height.
- Evidence: `/app/outputs/reference_calculations.log`

### Step 3: Evaluate all 17 density functionals and compute error metrics
- Role: scored (load-bearing)
- Action: For each of the 17 density functionals (APFD, B3LYP, B3LYP-D3, B97-D, B97-D3, HSE06, M06-2X, M06-HF, M06-L, MN15, PBE0, CAM-B3LYP, CAM-B3LYP-D3, LC-BLYP, LC-ωHPBE, LC-ωPBE-D3, ωB97x-D) using the jun-cc-pVDZ basis set: perform geometry optimizations, vibrational frequency calculations, static polarizability calculations, single-point energy evaluations for all noncovalent complexes, fractional electron runs, singlet-triplet energy calculations for PEDOT6^2+, and relaxed torsion scans for bipolaronic PEDOT6^2+. Compute the mean absolute errors, signed errors, and percent errors relative to the DSD-PBEP86 reference values. Aggregate all results into benchmark_results.json: a list of objects, each with keys 'functional', 'geometry_mae_pm', 'vibrational_mae_cm1', 'polarizability_mae_percent', 'ion_exchange_signed_error_kcalmol', 'interaction_energy_mae_kcalmol', 'delocalization_error_extremum_kcalmol', 'torsion_barrier_signed_error_kcalmol', 'exciton_stability_delta_EST_kcalmol'. Values are floating-point numbers or null if not computed.
- Output file: `/app/outputs/benchmark_results.json`
- Format: json
- Contract: JSON array of objects; each object has string key 'functional' and numeric keys for each property metric (null if not computed).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/benchmark_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### benchmark_results.json
- path: `/app/outputs/benchmark_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated error metrics for all 17 functionals against DSD-PBEP86 reference. Checker compares each metric to paper-reported gold with appropriate tolerances and directionality.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `functional`
    - `properties`:
      - `functional`:
        - `type`: string
      - `geometry_mae_pm`:
        - `type`: `number`, `null`
      - `vibrational_mae_cm1`:
        - `type`: `number`, `null`
      - `polarizability_mae_percent`:
        - `type`: `number`, `null`
      - `ion_exchange_signed_error_kcalmol`:
        - `type`: `number`, `null`
      - `interaction_energy_mae_kcalmol`:
        - `type`: `number`, `null`
      - `delocalization_error_extremum_kcalmol`:
        - `type`: `number`, `null`
      - `torsion_barrier_signed_error_kcalmol`:
        - `type`: `number`, `null`
      - `exciton_stability_delta_EST_kcalmol`:
        - `type`: `number`, `null`

Notes: Error metrics are compared to the hidden gold values from the paper's Table 2 and text-reported ΔE_ST. Tolerances and score direction are handled by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "benchmark_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "functional"
          ],
          "properties": {
            "functional": {
              "type": "string"
            },
            "geometry_mae_pm": {
              "type": [
                "number",
                "null"
              ]
            },
            "vibrational_mae_cm1": {
              "type": [
                "number",
                "null"
              ]
            },
            "polarizability_mae_percent": {
              "type": [
                "number",
                "null"
              ]
            },
            "ion_exchange_signed_error_kcalmol": {
              "type": [
                "number",
                "null"
              ]
            },
            "interaction_energy_mae_kcalmol": {
              "type": [
                "number",
                "null"
              ]
            },
            "delocalization_error_extremum_kcalmol": {
              "type": [
                "number",
                "null"
              ]
            },
            "torsion_barrier_signed_error_kcalmol": {
              "type": [
                "number",
                "null"
              ]
            },
            "exciton_stability_delta_EST_kcalmol": {
              "type": [
                "number",
                "null"
              ]
            }
          }
        }
      },
      "description": "Aggregated error metrics for all 17 functionals against DSD-PBEP86 reference. Checker compares each metric to paper-reported gold with appropriate tolerances and directionality."
    }
  ],
  "notes": "Error metrics are compared to the hidden gold values from the paper's Table 2 and text-reported ΔE_ST. Tolerances and score direction are handled by the checker."
}
```

## How you are scored
After submission, a hidden verifier reads `/app/outputs/benchmark_results.json` and independently scores each metric per functional against a hidden gold reference derived from the paper’s reported values. Scoring is metric‑aware and directional: for error metrics, meeting or exceeding (i.e., lower error) the reference earns full credit, while worse results receive partial to zero credit; for signed error and singlet‑triple gap, both sign and magnitude are checked within appropriate tolerances. The overall reward is a weighted sum of the scores for all metrics and functionals. Simply copying the paper’s reported numbers is insufficient – the verifier expects the output to arise from genuine DFT calculations consistent with the pipeline described in the workflow steps. No gold values or tolerances are disclosed to the agent.
