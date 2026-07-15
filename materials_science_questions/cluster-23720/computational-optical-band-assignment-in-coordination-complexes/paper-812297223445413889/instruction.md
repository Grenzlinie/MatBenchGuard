# Computational Prediction of Photolabile Ligands in Chromium(III) Ammine Complexes

## Problem background
Chromium(III) ammine complexes undergo photochemical ligand substitution when irradiated in the lowest quartet absorption band. The reaction is thought to proceed via a dissociative mechanism: (1) selective loss of a ligand from the complex in its first excited quartet state, (2) rearrangement of the resulting pentacoordinated fragment, and (3) capture of a solvent ligand. The central challenges are to predict which ligand is labilized (the leaving ligand) and from which excited electronic state (the photoactive state), and to rationalize the stereochemical outcome of the reaction. This task uses ab initio ligand-field CI calculations to compute the quartet excited states, the Mulliken population changes upon vertical excitation (Δp = p* − p), and the energies of the intermediate pentacoordinated isomers. The goal is to obtain qualitative predictions: the identity of the photoactive state, the ligand with the largest positive Δp (indicating weakened metal–ligand bonding), and the relative state ordering of square-pyramidal and trigonal-bipyramidal fragments that determines stereomobility.

## Approach
The approach adopts a dissociative model. Idealized molecular geometries are built for the four hexacoordinated complexes (Cr(NH3)5F2+, trans‑Cr(NH3)4F2+, trans‑Cr(NH3)4Cl2+, cis‑Cr(NH3)4F2+) and for the pentacoordinated fragments (Cr(NH3)4F2+ and Cr(NH3)4Cl2+) in the four relevant isomers: square-pyramidal with heteroligand apical (SP_ap) or basal (SP_bas), and trigonal-bipyramidal with heteroligand axial (TBP_ax) or equatorial (TBP_eq). Bond lengths are: Cr–N 2.07 Å, Cr–F 1.891 Å, Cr–Cl 2.33 Å, N–H 1.02 Å, with ∠H–N–H = 106.6° and all bond angles 90° (or 90°/120° for TBP). Point-group symmetries (C4v, C3v, C2v, Cs) are enforced as described.

An open-source quantum chemistry package (e.g., PySCF) is used to perform multi-configuration CI calculations within the d³ manifold, employing averaged d-orbitals (Av(d³)) from a restricted Hartree‑Fock calculation. For each hexacoordinated complex, the ground and lowest excited quartet states are computed. From these, one extracts vertical excitation energies (in cm⁻¹), the composition (% d_z² and % d_x²−y²) of the photoactive state (⁴E or ⁴B₂), and Mulliken gross populations for the ground and photoactive states. The Δp values (σ, π, and total) are obtained for each ligand; the ligand with the largest positive total Δp is taken as the predicted leaving ligand. For each pentacoordinated fragment, analogous CI calculations yield the energies of the relevant quartet states, allowing their relative ordering to be determined. Because exact numerical agreement is not expected due to differences in code and basis sets, the focus is on categorical predictions: photoactive state identity, leaving ligand identity, and the relative energy ordering of fragment states.

## Reproduction target
Produce a single JSON file at /app/outputs/results.json containing:

- "hexacoordinated": an array of objects, one per complex, each with:
  - "complex_id" (string, e.g., "Cr(NH3)5F2+", "trans-Cr(NH3)4F2+", ...),
  - "photoactive_state" (string: "4E" or "4B2"),
  - "excitation_energies" (object mapping each computed quartet state label to its energy in cm⁻¹),
  - "composition" (object with numeric keys "d_z2" and "d_x2_y2" giving percentages),
  - "delta_p" (object with per‑ligand Δp values; keys should identify ligand and component, e.g., "X_sigma", "X_pi", "X_total", "Nax_sigma", "Nax_total", "Neq_sigma", "Neq_total", etc.),
  - "predicted_leaving_ligand" (string naming the ligand with the largest positive total Δp).

- "pentacoordinated": an array of objects, one per fragment/structure, each with:
  - "fragment_id" (string, e.g., "Cr(NH3)4F2+" or "Cr(NH3)4Cl2+"),
  - "structure" (string: one of "SP_ap", "SP_bas", "TBP_ax", "TBP_eq"),
  - "relative_energies" (list of objects with keys "state" (string, e.g., "4B1", "4A1'", "4B2", "4A'") and "energy" (numeric, in arbitrary units but consistent for each fragment)).

Exact numerical reproduction of the paper's reported values is not required; the output must contain the requested quantities. The checked qualitative predictions (photoactive state, leaving ligand, fragment-state ordering) are the primary targets.

## Assets

- PySCF: https://github.com/pyscf/pyscf
- Basis sets (Cr 15s11p6d/11s8p4d; F,N 9s5p/5s3p; H 4s/3s; Cl Veillard-Dunning): https://www.basissetexchange.org/
- Idealized molecular geometries and symmetries

## Workflow steps

### Step 1: Prepare molecular geometries
- Role: process
- Action: Build idealized molecular geometries for all four hexacoordinated complexes (Cr(NH3)5F2+, trans‑Cr(NH3)4F2+, trans‑Cr(NH3)4Cl2+, cis‑Cr(NH3)4F2+) and the pentacoordinated fragments (SP_ap, SP_bas, TBP_ax, TBP_eq of Cr(NH3)4F2+ and Cr(NH3)4Cl2+) using the bond lengths and symmetry constraints given in the problem description (Cr‑N 2.07 Å, Cr‑F 1.891 Å, Cr‑Cl 2.33 Å, N‑H 1.02 Å, ∠H‑N‑H 106.6°, right angles, specified point groups).
- Evidence: none

### Step 2: Calculate excited quartet states for hexacoordinated complexes
- Role: process
- Action: Perform multi-configuration CI calculations (e.g., CASCI within the d³ manifold using averaged d-orbitals) for each hexacoordinated complex to obtain ground and lowest excited quartet state energies and wavefunctions. Extract vertical excitation energies (cm⁻¹), state compositions (% d_z², % d_x²-y²), and Mulliken gross populations for the ground and photoactive states.
- Evidence: none

### Step 3: Calculate quartet states for pentacoordinated fragments
- Role: process
- Action: Perform analogous CI calculations for the square‑pyramidal and trigonal‑bipyramidal isomers of Cr(NH3)4F2+ and Cr(NH3)4Cl2+ (SP_ap, SP_bas, TBP_ax, TBP_eq) to obtain the energies of the relevant quartet states.
- Evidence: none

### Step 4: Assemble and report computed results
- Role: scored (load-bearing)
- Action: Compile the computed values into /app/outputs/results.json. For each hexacoordinated complex: list the photoactive state (⁴E or ⁴B₂), excitation energies of the lowest quartet states, d‑orbital composition percentages, Mulliken population changes Δp (σ, π, and total per ligand), and the predicted leaving ligand (the ligand with the largest positive total Δp). For each pentacoordinated fragment: list the structure label (SP_ap, SP_bas, TBP_ax, TBP_eq) and the energies of the lowest quartet states as relative energies. No exact numeric reproduction is required; the file must contain the requested quantities.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys 'hexacoordinated' (array) and 'pentacoordinated' (array). Each hexacoordinated object has fields: complex_id (string), photoactive_state (string), excitation_energies (object with state labels as keys and numeric energies in cm⁻¹), composition (object with d_z2 and d_x2_y2 as numbers), delta_p (object with per-ligand breakdown, e.g., X_sigma, X_pi, X_total, Nax_sigma, Nax_total, Neq_sigma, Neq_total), predicted_leaving_ligand (string). Each pentacoordinated object has fields: fragment_id (string), structure (string, one of SP_ap, SP_bas, TBP_ax, TBP_eq), relative_energies (list of objects each with state (string) and energy (number)).
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
- target_policy: structural_audit
- description: Aggregated results from ab initio ligand-field CI calculations: photoactive state, excitation energies, d-orbital compositions, Mulliken population changes, leaving ligand predictions, and pentacoordinated fragment state energies.
- schema:
  - `type`: object
  - `required`:
    - `hexacoordinated`: array of objects
    - `pentacoordinated`: array of objects
  - `items`:
    - `hexacoordinated.element`: object with fields: complex_id (string), photoactive_state (string), excitation_energies (object mapping state label to numeric energy in cm⁻¹), composition (object with d_z2, d_x2_y2 as numbers), delta_p (object with per-ligand Δp values), predicted_leaving_ligand (string)
    - `pentacoordinated.element`: object with fields: fragment_id (string), structure (string), relative_energies (list of objects with state (string) and energy (number))

Notes: Scoring focuses on qualitative correctness: the photoactive state and leaving ligand must match the experimental consensus (categorical match) and the relative ordering of the pentacoordinated fragment states must reproduce the paper's Figure 3 pattern. No numeric tolerance is applied.

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "hexacoordinated": "array of objects",
          "pentacoordinated": "array of objects"
        },
        "items": {
          "hexacoordinated.element": "object with fields: complex_id (string), photoactive_state (string), excitation_energies (object mapping state label to numeric energy in cm⁻¹), composition (object with d_z2, d_x2_y2 as numbers), delta_p (object with per-ligand Δp values), predicted_leaving_ligand (string)",
          "pentacoordinated.element": "object with fields: fragment_id (string), structure (string), relative_energies (list of objects with state (string) and energy (number))"
        }
      },
      "description": "Aggregated results from ab initio ligand-field CI calculations: photoactive state, excitation energies, d-orbital compositions, Mulliken population changes, leaving ligand predictions, and pentacoordinated fragment state energies."
    }
  ],
  "notes": "Scoring focuses on qualitative correctness: the photoactive state and leaving ligand must match the experimental consensus (categorical match) and the relative ordering of the pentacoordinated fragment states must reproduce the paper's Figure 3 pattern. No numeric tolerance is applied."
}
```

## How you are scored
A hidden verifier independently scores your submitted /app/outputs/results.json against known experimental consensus and qualitative trends. The scoring is based on categorical correctness, not on numeric tolerance.

For each hexacoordinated complex:
- The photoactive state (⁴E or ⁴B₂) is compared to the experimentally identified photoreactive state; it must match exactly.
- The predicted leaving ligand (the ligand with the largest positive total Δp) is compared to the experimentally observed leaving ligand; it must match.

For the pentacoordinated fragments:
- The relative ordering of the lowest quartet states across the four structures (SP_ap, SP_bas, TBP_ax, TBP_eq) is checked against the pattern expected from stereomobility analysis. The ordering must be correct.

Each scored stage contributes a portion of the total reward. Reporting the required quantities in the specified JSON structure is necessary but not sufficient; the verifier confirms that the qualitative conclusions align with the experimental findings embedded in the hidden gold. The gold values are the established experimental results, and the check is binary (correct match or not).
