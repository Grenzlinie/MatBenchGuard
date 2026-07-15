# DFT-based intercalation site preference, bulk moduli, and diffusion barriers for black phosphorus anodes

## Problem background
Black phosphorus is a layered material with a corrugated structure similar to graphite but with a larger interlayer spacing, making it a candidate anode for Li-ion, Na-ion, and Mg-ion batteries. The atomic-scale insertion mechanisms, the mechanical response (softening vs. hardening) upon ion uptake, and the diffusion kinetics are critical for battery performance but differ among the three ion species. This task addresses the problem of quantifying those differences from first principles.

## Approach
For each metal (Li, Na, Mg), the computational approach uses density functional theory (DFT) with a GGA-PBE exchange-correlation functional, a projector-augmented-wave (PAW) representation, and a van der Waals correction (e.g., Grimme D2) to model the black phosphorus host. Starting from the experimental orthorhombic crystal structure, a 2×2×2 supercell (64 P atoms) is fully relaxed. Intercalation site preference is determined by placing two adatoms either in the same interlayer gap or in adjacent gaps, relaxing both configurations, and comparing total energies. Mechanical properties are assessed by computing bulk moduli of pristine BP and the M₂P phases via fitting energy–volume data to the Birch–Murnaghan equation of state. Diffusion barriers are calculated with the nudged elastic band (NEB) method for single-atom hops along the zigzag and armchair directions within a phosphorene layer. All results are to be derived from re-running these calculations; pre-packaged output files from the original study must not be used.

## Reproduction target
Compute and report three sets of quantities. (1) Intercalation site preference: for Li, Na, Mg, identify whether two guest atoms in a 2×2×2 BP supercell prefer the same layer or different layers (the lower-energy configuration), and record the interlayer spacing. Results go to `site_preference.json`. (2) Bulk moduli: determine the bulk moduli (GPa) of pristine BP, Li₂P, Na₂P, and Mg₂P by fitting DFT energy–volume curves. Results go to `bulk_moduli.json`. (3) Diffusion barriers: compute NEB energy barriers (eV) for single Li, Na, Mg diffusing along zigzag and armchair channels. Results go to `diffusion_barriers.json`. Each JSON file must follow the schema detailed in the workflow steps and output contract.

## Assets

- Black phosphorus crystal structure: https://materialsproject.org/materials/mp-2450/
- DFT simulation package: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Relax pristine black phosphorus supercell
- Role: process
- Action: Construct a 2×2×2 supercell (64 P atoms) using the experimental lattice parameters, and fully relax the geometry with DFT (GGA-PBE, vdW correction) until forces fall below 0.001 eV/Å. Save the relaxed structure for subsequent steps.
- Evidence: `/app/outputs/relaxed_BP_structure.xyz`

### Step 2: Determine intercalation site preference
- Role: scored (load-bearing)
- Action: For each metal (Li, Na, Mg), place two adatoms in the relaxed supercell: (i) in the same interlayer gap and (ii) in adjacent interlayer gaps. Fully relax each configuration. Compare total energies to decide the preferred site (lower energy). Record the preference and the interlayer distance after intercalation.
- Output file: `/app/outputs/site_preference.json`
- Format: json
- Contract: Array of objects, each with keys: "metal" (one of "Li","Na","Mg"), "preferred_site" (one of "same_layer" or "different_layers"), "interlayer_distance_A" (number, in Å). Three objects total.
- Scoring: scored by hidden verifier

### Step 3: Compute bulk moduli of pristine BP and M2P
- Role: scored (load-bearing)
- Action: For pristine black phosphorus and for M2P (M=Li,Na,Mg) compositions, construct the appropriate supercell with metal atoms arranged according to the known intercalation mechanism (columnar for Li/Mg, planar for Na). Perform DFT calculations at several cell volumes around equilibrium, fit the energy-volume data to the Birch-Murnaghan equation of state, and extract the bulk modulus. Report the bulk moduli in GPa.
- Output file: `/app/outputs/bulk_moduli.json`
- Format: json
- Contract: Array of objects, each with keys: "system" (one of "pristine_BP","Li2P","Na2P","Mg2P"), "bulk_modulus_GPa" (number, in GPa). Four objects total.
- Scoring: scored by hidden verifier

### Step 4: Compute Li, Na, Mg diffusion barriers
- Role: scored (load-bearing)
- Action: For each metal (Li, Na, Mg), set up initial and final positions for the diffusion hop inside a phosphorene layer along the zigzag channel and along the armchair direction. Use the nudged elastic band (NEB) method with at least 5 images to compute the minimum energy path and extract the energy barrier. Report the barriers in eV.
- Output file: `/app/outputs/diffusion_barriers.json`
- Format: json
- Contract: Array of objects, each with keys: "metal" (one of "Li","Na","Mg"), "path" (one of "zigzag","armchair"), "barrier_eV" (number, in eV). Six objects total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/site_preference.json`
- `/app/outputs/bulk_moduli.json`
- `/app/outputs/diffusion_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### site_preference.json
- path: `/app/outputs/site_preference.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Intercalation site preference and interlayer distance for Li, Na, Mg in black phosphorus. Verified with tolerances: preferred_site exact match, interlayer_distance ±0.2 Å.
- schema:
  - `type`: array
  - `items`:
    - `metal`: string (one of 'Li','Na','Mg')
    - `preferred_site`: string (one of 'same_layer' or 'different_layers')
    - `interlayer_distance_A`: number

### bulk_moduli.json
- path: `/app/outputs/bulk_moduli.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Bulk moduli of pristine BP and M2P. Tolerances: ±5 GPa.
- schema:
  - `type`: array
  - `items`:
    - `system`: string (one of 'pristine_BP', 'Li2P', 'Na2P', 'Mg2P')
    - `bulk_modulus_GPa`: number

### diffusion_barriers.json
- path: `/app/outputs/diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Diffusion barriers for single atoms along zigzag and armchair channels. Tolerances: ±0.05 eV for barriers ≤0.2 eV, ±0.2 eV for higher. Also check Li zigzag < 0.5 eV.
- schema:
  - `type`: array
  - `items`:
    - `metal`: string (one of 'Li', 'Na', 'Mg')
    - `path`: string (one of 'zigzag', 'armchair')
    - `barrier_eV`: number

Notes: All values compared against published DFT results with tolerances as described. Site preference exact match for the preferred_site field; interlayer distance, bulk moduli, and barriers use thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "site_preference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string (one of 'Li','Na','Mg')",
          "preferred_site": "string (one of 'same_layer' or 'different_layers')",
          "interlayer_distance_A": "number"
        }
      },
      "description": "Intercalation site preference and interlayer distance for Li, Na, Mg in black phosphorus. Verified with tolerances: preferred_site exact match, interlayer_distance ±0.2 Å."
    },
    {
      "file": "bulk_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "system": "string (one of 'pristine_BP', 'Li2P', 'Na2P', 'Mg2P')",
          "bulk_modulus_GPa": "number"
        }
      },
      "description": "Bulk moduli of pristine BP and M2P. Tolerances: ±5 GPa."
    },
    {
      "file": "diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string (one of 'Li', 'Na', 'Mg')",
          "path": "string (one of 'zigzag', 'armchair')",
          "barrier_eV": "number"
        }
      },
      "description": "Diffusion barriers for single atoms along zigzag and armchair channels. Tolerances: ±0.05 eV for barriers ≤0.2 eV, ±0.2 eV for higher. Also check Li zigzag < 0.5 eV."
    }
  ],
  "notes": "All values compared against published DFT results with tolerances as described. Site preference exact match for the preferred_site field; interlayer distance, bulk moduli, and barriers use thresholds."
}
```

## How you are scored
A hidden verifier checks your output files against independently determined reference values. Each of the three scored artifacts (`site_preference.json`, `bulk_moduli.json`, `diffusion_barriers.json`) carries part of the total reward. The verifier will compare your reported site preference, interlayer distance, bulk moduli, and diffusion barriers to the corresponding expected values, using tolerance margins that account for legitimate differences arising from different DFT codes, pseudopotentials, or convergence settings. Reporting the paper’s numbers without actually performing the calculations is not sufficient; the verifier expects values consistent with a genuine re-run of the described workflow. The final reward is a weighted combination of the per-artifact scores.
