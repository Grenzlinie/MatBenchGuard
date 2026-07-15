# Computational Molecular Dipole Moment Calculation

## Problem background
Dissociative electron attachment (DEA) to biological metabolites such as oxaloacetic acid (OAA) and citric acid (CA) can lead to fragmentation upon capture of low-energy electrons, producing reactive species that may cause cellular damage. Reliable theoretical estimates of the thermochemistry and electron-accepting properties of these molecules are essential for understanding their behaviour under irradiation. This reproduction task isolates the computational determination of vertical electron affinities and the Gibbs free energies of two key fragmentation channels using density functional theory (DFT).

## Approach
The computational approach employs the long-range-corrected hybrid functional ωB97x with the aug-cc-pVTZ basis set to model the neutral molecules and their anionic fragments. The vertical electron affinity (VEA) is obtained as the difference between single-point energies of the anion and the neutral, both computed at the optimized geometry of the neutral molecule. For the fragmentation channels corresponding to dehydrogenation (loss of a hydrogen atom) and loss of a formic acid unit (HCOOH), reaction Gibbs free energies are calculated at 400 K. These values are derived from harmonic vibrational frequency calculations using the rigid-rotor harmonic-oscillator approximation. The target species are the cis-enol tautomer of oxaloacetic acid and the most stable conformer of citric acid; all computations are performed with an open-source quantum chemistry package supporting the required functional and basis set.

## Reproduction target
Compute the vertical electron affinity (VEA) and the Gibbs free energies (at 400 K) for the two dissociation reactions, M + e⁻ → [M-H]⁻ + H and M + e⁻ → [M-HCOOH]⁻ + HCOOH, where M stands for cis-enol oxaloacetic acid and citric acid. All calculations must be performed at the ωB97x/aug-cc-pVTZ level of theory (with neutral geometry optimizations optionally at ωB97x/cc-pVTZ). Report the six resulting values in electronvolts (eV) in a JSON file at `/app/outputs/df_results.json` with the following keys: `VEA_OAA`, `VEA_CA`, `Gibbs_M_H_OAA`, `Gibbs_M_H_CA`, `Gibbs_M_HCOOH_OAA`, `Gibbs_M_HCOOH_CA`.

## Assets

- ORCA quantum chemistry package (or equivalent): https://orcaforum.kofo.mpg.de
- Molecular structures of oxaloacetic acid (cis-enol) and citric acid

## Workflow steps

### Step 1: Neutral geometry optimization
- Role: process
- Action: Optimize the molecular geometries of cis-enol oxaloacetic acid and citric acid at the ωB97x/cc-pVTZ level of theory. Save the optimized coordinates.
- Evidence: `/app/outputs/neutrals_opt.log`

### Step 2: Vertical electron affinity (VEA) calculation
- Role: process
- Action: Perform single-point energy calculations for the neutral and anionic forms at the optimized neutral geometries using ωB97x/aug-cc-pVTZ. Compute VEA = E(anion) − E(neutral) for each molecule.
- Evidence: `/app/outputs/vea_computation.log`

### Step 3: Fragment optimization and thermochemistry
- Role: process
- Action: Optimize geometries of fragmentation products: [M-H]⁻ and [M-HCOOH]⁻ anions for both OAA and CA, as well as HCOOH and H atom if needed. Perform harmonic vibrational frequency calculations at ωB97x/aug-cc-pVTZ. Obtain Gibbs free energies at 400 K using rigid-rotor harmonic-oscillator approximation. Store total Gibbs free energies of each species.
- Evidence: `/app/outputs/fragment_opt_freq.log`

### Step 4: Report VEA and Gibbs free energies
- Role: scored (load-bearing)
- Action: Assemble the computed quantities into a JSON file: VEA_OAA, VEA_CA, Gibbs_M_H_OAA, Gibbs_M_H_CA, Gibbs_M_HCOOH_OAA, Gibbs_M_HCOOH_CA. All values in eV. Write to /app/outputs/df_results.json.
- Output file: `/app/outputs/df_results.json`
- Format: json
- Contract: {"VEA_OAA": <float eV>, "VEA_CA": <float eV>, "Gibbs_M_H_OAA": <float eV>, "Gibbs_M_H_CA": <float eV>, "Gibbs_M_HCOOH_OAA": <float eV>, "Gibbs_M_HCOOH_CA": <float eV>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/df_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### df_results.json
- path: `/app/outputs/df_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed vertical electron affinities and Gibbs free energies (400 K) for the dehydrogenation and formic acid loss channels of oxaloacetic and citric acids.
- schema:
  - `type`: object
  - `required`:
    - `VEA_OAA`: float (eV)
    - `VEA_CA`: float (eV)
    - `Gibbs_M_H_OAA`: float (eV)
    - `Gibbs_M_H_CA`: float (eV)
    - `Gibbs_M_HCOOH_OAA`: float (eV)
    - `Gibbs_M_HCOOH_CA`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `VEA_OAA`: eV
    - `VEA_CA`: eV
    - `Gibbs_M_H_OAA`: eV
    - `Gibbs_M_H_CA`: eV
    - `Gibbs_M_HCOOH_OAA`: eV
    - `Gibbs_M_HCOOH_CA`: eV

Notes: All values are in eV. The Gibbs free energies correspond to the reactions M + e⁻ → [M-H]⁻ + H and M + e⁻ → [M-HCOOH]⁻ + HCOOH at 400 K. The agent must compute these using the specified density functional and basis set.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "df_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "VEA_OAA": "float (eV)",
          "VEA_CA": "float (eV)",
          "Gibbs_M_H_OAA": "float (eV)",
          "Gibbs_M_H_CA": "float (eV)",
          "Gibbs_M_HCOOH_OAA": "float (eV)",
          "Gibbs_M_HCOOH_CA": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "VEA_OAA": "eV",
          "VEA_CA": "eV",
          "Gibbs_M_H_OAA": "eV",
          "Gibbs_M_H_CA": "eV",
          "Gibbs_M_HCOOH_OAA": "eV",
          "Gibbs_M_HCOOH_CA": "eV"
        }
      },
      "description": "Computed vertical electron affinities and Gibbs free energies (400 K) for the dehydrogenation and formic acid loss channels of oxaloacetic and citric acids."
    }
  ],
  "notes": "All values are in eV. The Gibbs free energies correspond to the reactions M + e⁻ → [M-H]⁻ + H and M + e⁻ → [M-HCOOH]⁻ + HCOOH at 400 K. The agent must compute these using the specified density functional and basis set."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/df_results.json` and compares each of the six reported values against a set of hidden reference values that are consistent with the protocol described in this instruction. Your final reward is proportional to the number of values that fall within an undisclosed tolerance of the reference; a value that is completely wrong (or missing) contributes nothing. Simply printing numbers from the literature without genuinely executing the required DFT steps will not earn credit. The verifier does not reveal the reference values or the tolerance thresholds.
