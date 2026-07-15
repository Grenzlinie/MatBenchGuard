# Surface exchange interactions in Fe, Co, and Gd from ab initio calculations

## Problem background
Ferromagnetic transition metals Fe and Co and rare-earth Gd exhibit interesting surface magnetic properties. Understanding how magnetic exchange interactions at surfaces differ from those in the bulk is essential for explaining finite‑temperature behavior and for applications like thin‑film spintronics. This study addresses two key aspects: (1) effective interlayer exchange couplings, quantified as the total‑energy difference between a ferromagnetic and an antiferromagnetic alignment of adjacent atomic layers; (2) layer‑resolved on‑site exchange parameters derived from a classical Heisenberg model. The goal is to determine these quantities for several low‑index surfaces and to examine the change of the interlayer coupling and on‑site exchange parameters at the surface relative to the bulk.

## Approach
The workflow combines ab initio electronic‑structure calculations within the local spin‑density approximation (LSDA) with a post‑processing step based on the magnetic force theorem. Slab models are constructed for bcc Fe(110), Fe(001), hcp Co(0001), and hcp Gd(0001) surfaces using experimental lattice constants. Each slab contains seven atomic layers and three vacuum layers; for Gd(0001), an additional slab with a 3% inward relaxation of the top interlayer distance is created. Self‑consistent total energies are computed for both ferromagnetic (FM) and layer‑wise antiferromagnetic (AFM) spin configurations. From the total energies, the effective interlayer exchange coupling is obtained as the energy difference per atom between the AFM and FM states. Separately, layer‑resolved on‑site exchange parameters J_R^0 are evaluated via an energy integration involving site‑diagonal Green’s functions and potential‑function differences. The calculations are performed with a publicly available all‑electron FLAPW code (FLEUR) or an equivalent LSDA implementation. For Gd, 4f states are treated as core electrons.

## Reproduction target
As the end result, the agent must produce two CSV files under `/app/outputs`:

1. `delta_E_results.csv`: computed total‑energy differences ΔE^bulk and ΔE^surf (in mRy/atom) for every surface – Fe(110), Fe(001), Co(0001), Gd(0001) ideal, and Gd(0001) relaxed.

2. `J0_results.csv`: layer‑resolved on‑site exchange parameters J_R^0 (in mRy) for each surface layer of the same systems, with layer index 0 denoting the topmost surface layer.

The numerical values themselves are the target; the agent is not required to interpret or comment on them. The computed values should reflect the chosen physical models and computational settings described in the approach.

## Assets

- FLEUR (FLAPW code): https://www.flapw.de/
- Standard crystal structures of bcc Fe, hcp Co, hcp Gd

## Workflow steps

### Step 1: Construct bulk and slab models
- Role: process
- Action: Set up atomic coordinates and lattice vectors for bcc Fe(110) and (001), hcp Co(0001), and hcp Gd(0001) using experimental lattice constants. For each surface, build a slab with 7 atomic layers and 3 layers of empty spheres. For Gd(0001), create both an ideal slab and a slab with a 3% inward relaxation of the top interlayer spacing. Prepare input files suitable for the FLAPW code (FLEUR).
- Evidence: `/app/outputs/slab_setup_summary.txt`

### Step 2: Run DFT self-consistent calculations
- Role: process
- Action: Using the all-electron FLAPW code FLEUR (or an equivalent LSDA implementation), perform self-consistent calculations for each system in ferromagnetic (FM) and antiferromagnetic (AFM) configurations: FM bulk, AFM bulk with layer-by-layer antiferromagnetic coupling, FM surface, and AFM surface with the top layer flipped. For Gd, treat 4f states as core. Save total energies and, if supported by the chosen code, the Green's function data needed for exchange parameter evaluation.
- Evidence: `/app/outputs/dft_run_summary.log`

### Step 3: Calculate ΔE values
- Role: scored (load-bearing)
- Action: From the total energies obtained in step_2, compute ΔE^bulk = (E_AFM_bulk - E_FM_bulk) per bulk atom and ΔE^surf = (E_AFM_surf - E_FM_surf) per surface atom for each system. Write the results to delta_E_results.csv.
- Output file: `/app/outputs/delta_E_results.csv`
- Format: csv
- Contract: Columns: system (string), surface_type (string: 'ideal' or 'relaxed'), Delta_E_bulk (float, mRy/atom), Delta_E_surf (float, mRy/atom).
- Scoring: scored by hidden verifier

### Step 4: Calculate on-site exchange parameters J_R^0
- Role: scored (load-bearing)
- Action: Using the magnetic force theorem implemented in the FLAPW code (or a post-processing tool) applied to the DFT output of step_2, compute the layer-resolved on-site exchange parameters J_R^0 for each surface layer. For Gd(0001) include both ideal and relaxed slabs. Write results to J0_results.csv.
- Output file: `/app/outputs/J0_results.csv`
- Format: csv
- Contract: Columns: system (string), surface_type (string), layer_index (integer, 0=top layer), J_R0 (float, mRy).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_E_results.csv`
- `/app/outputs/J0_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_E_results.csv
- path: `/app/outputs/delta_E_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed total-energy differences ΔE^bulk and ΔE^surf for all Fe, Co, and Gd surfaces, including ideal and relaxed geometries for Gd(0001).
- schema:
  - `type`: table
  - `required_columns`: `system`, `surface_type`, `Delta_E_bulk`, `Delta_E_surf`
  - `units`:
    - `Delta_E_bulk`: mRy/atom
    - `Delta_E_surf`: mRy/atom

### J0_results.csv
- path: `/app/outputs/J0_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Layer-resolved on-site exchange parameters J_R^0 for each surface layer of Fe, Co, and Gd surfaces.
- schema:
  - `type`: table
  - `required_columns`: `system`, `surface_type`, `layer_index`, `J_R0`
  - `units`:
    - `J_R0`: mRy

Notes: The hidden checker compares the computed values to reference data from the paper, verifying consistency and the expected trend ΔE_surf > ΔE_bulk for all entries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_E_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "surface_type",
          "Delta_E_bulk",
          "Delta_E_surf"
        ],
        "units": {
          "Delta_E_bulk": "mRy/atom",
          "Delta_E_surf": "mRy/atom"
        }
      },
      "description": "Computed total-energy differences ΔE^bulk and ΔE^surf for all Fe, Co, and Gd surfaces, including ideal and relaxed geometries for Gd(0001)."
    },
    {
      "file": "J0_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "surface_type",
          "layer_index",
          "J_R0"
        ],
        "units": {
          "J_R0": "mRy"
        }
      },
      "description": "Layer-resolved on-site exchange parameters J_R^0 for each surface layer of Fe, Co, and Gd surfaces."
    }
  ],
  "notes": "The hidden checker compares the computed values to reference data from the paper, verifying consistency and the expected trend ΔE_surf > ΔE_bulk for all entries."
}
```

## How you are scored
After you submit your results, a hidden verifier reads the two CSV files. It compares each ΔE value and each J_R^0 value against a hidden reference set and assigns a score based on how closely they match (tolerances are applied, chosen to accommodate legitimate implementation variations). Additionally, the verifier confirms that the computed values satisfy certain required structural relationships (e.g., between surface and bulk entries, and across layers). Each scored artifact contributes a weight to the overall reward; a perfect agreement yields a reward of 1.0. Submitting correctly formatted but inaccurate numbers earns little or no reward.
