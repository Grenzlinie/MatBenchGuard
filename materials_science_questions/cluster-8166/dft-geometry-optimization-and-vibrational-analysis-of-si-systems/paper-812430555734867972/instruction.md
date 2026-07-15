# DFT Energy and Geometry of ansa-Niobocene Ethylene Hydride Model Systems

## Problem background
The effect of single and double ansa‑bridges on the olefin insertion mechanism in group 5 metallocene ethylene hydride complexes is not fully understood. This task uses density functional theory (DFT) to investigate model niobocene systems and compute the reaction pathway for hydrogen exchange, including identification of a β‑agostic ethyl intermediate. The goal is to quantify how bridging influences the relative stabilities of intermediates and transition states, and to extract key geometric parameters that characterize each structure.

## Approach
Three model complexes are constructed: the unbridged niobocene **6** [Cp₂Nb(C₂H₄)H], the singly SiH₂‑bridged ansa‑niobocene **7** [H₂Si(η⁵‑C₅H₄)₂Nb(C₂H₄)H], and the doubly SiH₂‑bridged ansa‑niobocene **8** [(H₂Si)₂(η⁵‑C₅H₃)₂Nb(C₂H₄)H]. For each model, four stationary points that define the hydrogen exchange surface are located: (a) the ethylene hydride minimum, (b) the transition state for ethylene insertion, (c) the β‑agostic ethyl minimum, and (d) the transition state for C–C bond rotation. DFT calculations are performed at the GGA level with the Becke exchange and Perdew correlation (BP86), a triple‑zeta valence basis set with polarization, frozen cores for heavy atoms (1s for C, 2p for Si, 3d for Nb), and scalar relativistic corrections via the ZORA approximation. Full geometry optimizations are followed by harmonic vibrational frequency calculations to confirm minima (all real frequencies) and transition states (one imaginary frequency). Relative energies are computed with respect to the corresponding ethylene hydride minimum **a**, and the optimized bond lengths (Nb–H, Cendo–H, C–C, Nb–Cexo) and inter‑ring angle are extracted.

## Reproduction target
Perform DFT geometry optimization and frequency analysis for the four stationary points (a, b, c, d) of each model (6, 7, 8) using the BP86 functional, triple‑zeta basis with polarization, frozen cores, and ZORA relativistic treatment. Compute the relative electronic energy (kcal/mol) of each stationary point with respect to its corresponding ethylene hydride minimum **a**. Extract the optimized geometric parameters: Nb–H bond length (Å), Cendo–H bond length (Å), C–C bond length (Å), Nb–Cexo bond length (Å), and inter‑ring angle (degrees). Output all results to `/app/outputs/dft_results.csv` in the format specified in the workflow steps.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Prepare initial molecular geometries
- Role: process
- Action: Construct initial 3D molecular geometries for the unbridged niobocene (model 6), singly SiH₂-bridged ansa-niobocene (model 7), and doubly SiH₂-bridged ansa-niobocene (model 8) ethylene hydride complexes as described in the publication. Each contains niobium, cyclopentadienyl or substituted rings, silicon bridges, ethylene and hydride ligands.
- Evidence: `/app/outputs/initial_structures.xyz`

### Step 2: Locate approximate stationary points
- Role: process
- Action: Perform relaxed potential energy surface scans along chosen reaction coordinates (e.g., Nb–H distance, C–C torsion) using DFT at a modest level to identify approximate geometries for the four stationary points per model: a (ethylene hydride), b (insertion TS), c (β‑agostic ethyl minimum), d (rotation TS).
- Evidence: `/app/outputs/scan_paths.log`

### Step 3: DFT geometry optimization and frequency analysis
- Role: scored (load-bearing)
- Action: For each model (6,7,8) and each approximate stationary point (a,b,c,d), perform full DFT geometry optimization using the GGA BP86 functional, triple‑zeta valence basis set with polarization, frozen cores (1s for C, 2p for Si, 3d for Nb), and scalar relativistic corrections (ZORA). Confirm minima (all real frequencies) and transition states (one imaginary frequency) via harmonic vibrational frequency calculations. Compute the total electronic energy relative to the corresponding ethylene hydride minimum (a) in kcal/mol. Extract optimized geometric parameters: Nb–H bond length, Cendo–H bond length, C–C bond length, Nb–Cexo bond length, and inter‑ring angle. Write all results to dft_results.csv.
- Output file: `/app/outputs/dft_results.csv`
- Format: csv
- Contract: CSV with columns: model (int, 6/7/8), state (str, a/b/c/d), relative_energy_kcal_mol (float), Nb_H_A (float), Cendo_H_A (float), C_C_A (float), Nb_Cexo_A (float), inter_ring_angle_deg (float). One row per state per model.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.csv
- path: `/app/outputs/dft_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed relative electronic energies and key bond lengths/angles for stationary points a–d of model niobocene complexes 6, 7, and 8.
- schema:
  - `type`: table
  - `required_columns`: `model`, `state`, `relative_energy_kcal_mol`, `Nb_H_A`, `Cendo_H_A`, `C_C_A`, `Nb_Cexo_A`, `inter_ring_angle_deg`
  - `units`:
    - `relative_energy_kcal_mol`: kcal/mol
    - `Nb_H_A`: Å
    - `Cendo_H_A`: Å
    - `C_C_A`: Å
    - `Nb_Cexo_A`: Å
    - `inter_ring_angle_deg`: degrees

Notes: The agent must construct molecular structures from the paper's description (Cp, SiH₂ bridges, ethylene, hydride). Any open-source DFT implementation of BP86/ZORA/triple‑zeta is acceptable; numerical spread is absorbed by the checker tolerances. The checker compares each row's values to hidden reference values and also validates energetic ordering between models.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "state",
          "relative_energy_kcal_mol",
          "Nb_H_A",
          "Cendo_H_A",
          "C_C_A",
          "Nb_Cexo_A",
          "inter_ring_angle_deg"
        ],
        "units": {
          "relative_energy_kcal_mol": "kcal/mol",
          "Nb_H_A": "Å",
          "Cendo_H_A": "Å",
          "C_C_A": "Å",
          "Nb_Cexo_A": "Å",
          "inter_ring_angle_deg": "degrees"
        }
      },
      "description": "Computed relative electronic energies and key bond lengths/angles for stationary points a–d of model niobocene complexes 6, 7, and 8."
    }
  ],
  "notes": "The agent must construct molecular structures from the paper's description (Cp, SiH₂ bridges, ethylene, hydride). Any open-source DFT implementation of BP86/ZORA/triple‑zeta is acceptable; numerical spread is absorbed by the checker tolerances. The checker compares each row's values to hidden reference values and also validates energetic ordering between models."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/dft_results.csv`. The verifier compares your computed relative energies and geometric parameters against a set of reference values, checking each entry within appropriate tolerances. It also verifies that the energetic ordering among the three model complexes follows the expected trend (e.g., the insertion barrier and the energy of the agostic intermediate differ systematically between unbridged, singly bridged, and doubly bridged systems). The final score is a weighted combination of the per‑entry agreement and the ordering check.
