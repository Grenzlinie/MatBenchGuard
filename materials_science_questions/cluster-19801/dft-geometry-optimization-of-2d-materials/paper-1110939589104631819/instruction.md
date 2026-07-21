# Tight-binding analysis of surface relaxation effects on topological surface states

## Problem background
Bismuth (Bi) and its alloys are debated topological materials. The surface states at the \u0305M point of Bi(111) are crucial for topological characterization, yet experimental evidence is contradictory. Surface relaxation — an expansion of inter‑bilayer distances near the surface — may alter the local topology and thereby affect the emergence of these surface states. This task explores how such inter‑bilayer expansion modifies the wavefunction distribution and spectral intensity of surface states in thick Bi(111) films, with the goal of quantifying potential suppression effects.

## Approach
Re‑implement the Liu–Allen relativistic empirical tight‑binding model for Bi. For bulk calculations, scale the hopping integrals as V \u221d d\u207b\u00b2 and compute the eigenenergies at the L point under uniform inter‑bilayer expansion to find the critical expansion where the band gap closes and reopens with opposite character. For slab calculations, construct the Hamiltonian for a 100‑bilayer Bi(111) film with a 10‑bilayer surface relaxation layer on one side, applying the surface potential of Saito et al. Perform slab diagonalization at the \u0305M point (k\u2016 corresponding to the bulk L point) for two different expansion magnitudes. Identify the surface states S1 and S2 by energy proximity to the Fermi level and high surface localization, and extract their probability distribution |\u03c8(z)|\u00b2 across bilayers. Finally, compute the spatial one‑particle spectral function A(k\u2016,z,\u03b5) via the retarded Green’s function with a Lorentzian broadening, and compare the spectral weight at the surface bilayer between a relaxed slab and an unrelaxed slab to obtain a blocking ratio.

## Reproduction target
Produce three scored artifacts from tight‑binding calculations:
(1) `critical_expansion.json` – the critical normalized inter‑bilayer expansion and the corresponding fractional hopping change at which the bulk L‑point band inversion occurs.
(2) `wavefunction_distribution.csv` – the probability distribution |\u03c8(z)|\u00b2 of the surface states S1 and S2 for a 100‑bilayer slab with a 10‑bilayer relaxation layer, evaluated at two chosen expansion ratios (one below and one above the typical relaxation magnitude).
(3) `spatial_spectrum.json` – the blocking ratio, defined as the ratio of the surface‑layer spectral weight at the \u0305M point with relaxation to that without relaxation, and the underlying peak weights.

## Assets

- Liu–Allen relativistic tight-binding model parameters for bulk Bi: 10.1103/PhysRevB.52.1566
- Saito et al. surface potential for Bi(111) thin films: 10.1103/PhysRevB.93.041301
- Bulk Bi crystal structure (inter-bilayer distance and lattice constants)

## Workflow steps

### Step 1: Critical inter-bilayer expansion from bulk band inversion
- Role: scored
- Action: Implement the Liu-Allen tight-binding model for bulk Bi. Compute the eigenenergies at the L point as a function of uniform inter-bilayer expansion Δd/d0, scaling the hopping integrals with V ∝ d⁻². Identify the critical expansion Δd_c/d0 where the conduction and valence bands invert (band gap closes and reopens with opposite character) and compute the corresponding fractional hopping change ΔV_c/V0. Write these critical values to the output file.
- Output file: `/app/outputs/critical_expansion.json`
- Format: json
- Contract: {"critical_delta_d_d0": float, "critical_delta_V_V0": float}
- Scoring: scored by hidden verifier

### Step 2: Surface state probability distribution in Bi(111) slab with relaxation
- Role: scored
- Action: Construct the Liu-Allen slab Hamiltonian for a 100-bilayer Bi(111) film with a 10-bilayer surface relaxation layer on one side. Set the inter-bilayer expansion to Δd/d0 = 0.2% and 3% in separate calculations. Diagonalize at the M point (k∥ corresponding to the bulk L point). Identify the surface states S1 and S2 (e.g., by energy proximity to the Fermi level and high surface localization). For each surface state, compute |ψ(z)|² for each bilayer index z = 1…100. Write a CSV with columns z_BL, state, delta_d_d0, prob.
- Output file: `/app/outputs/wavefunction_distribution.csv`
- Format: csv
- Contract: Header: z_BL,state,delta_d_d0,prob
- Scoring: scored by hidden verifier

### Step 3: Spatial one-particle spectrum and blocking ratio
- Role: scored (load-bearing)
- Action: Using the slab Hamiltonian from the previous step, compute the spatial one-particle spectral function A(k∥,z,ε) at the M point via the retarded Green's function with Lorentzian broadening Σ'' = 0.03 eV. Produce spectra for the slab with relaxation (Δd/d0 = 3%) and for an unrelaxed slab (Δd = 0). For each, extract the total spectral weight at the surface bilayer (z=1) over the energy window of the surface states. Calculate the blocking ratio = (surface peak weight with relaxation) / (surface peak weight without relaxation). Write the ratio and the two peak weights to the output file.
- Output file: `/app/outputs/spatial_spectrum.json`
- Format: json
- Contract: {"blocking_ratio_100BL": float, "surface_peak_weight_relaxed": float, "surface_peak_weight_unrelaxed": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_expansion.json`
- `/app/outputs/wavefunction_distribution.csv`
- `/app/outputs/spatial_spectrum.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_expansion.json
- path: `/app/outputs/critical_expansion.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical normalized expansion and corresponding fractional hopping change at L-point band inversion.
- schema:
  - `type`: object
  - `required`: `critical_delta_d_d0`, `critical_delta_V_V0`
  - `items`: object
  - `units`:
    - `critical_delta_d_d0`: dimensionless
    - `critical_delta_V_V0`: dimensionless

### wavefunction_distribution.csv
- path: `/app/outputs/wavefunction_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Probability distribution of surface states for two expansion values, showing migration away from the relaxed surface for Δd > Δd_c.
- schema:
  - `type`: table
  - `required_columns`: `z_BL`, `state`, `delta_d_d0`, `prob`
  - `units`:
    - `z_BL`: bilayer index (1–100)
    - `state`: string: S1 or S2
    - `delta_d_d0`: dimensionless (0.002 or 0.03)
    - `prob`: normalized probability

### spatial_spectrum.json
- path: `/app/outputs/spatial_spectrum.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Blocking ratio and surface spectral weights quantifying the suppression of surface-state intensity by the relaxation layer.
- schema:
  - `type`: object
  - `required`: `blocking_ratio_100BL`, `surface_peak_weight_relaxed`, `surface_peak_weight_unrelaxed`
  - `items`: object
  - `units`:
    - `blocking_ratio_100BL`: dimensionless
    - `surface_peak_weight_relaxed`: arbitrary spectral weight
    - `surface_peak_weight_unrelaxed`: arbitrary spectral weight

Notes: All three artifacts are produced by tight-binding calculations using public parameters. The DFT structural optimization stage is omitted (proprietary code) and the task focuses exclusively on the tight-binding part that demonstrates the topological blocking effect.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_expansion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "critical_delta_d_d0",
          "critical_delta_V_V0"
        ],
        "items": {},
        "units": {
          "critical_delta_d_d0": "dimensionless",
          "critical_delta_V_V0": "dimensionless"
        }
      },
      "description": "Critical normalized expansion and corresponding fractional hopping change at L-point band inversion."
    },
    {
      "file": "wavefunction_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_BL",
          "state",
          "delta_d_d0",
          "prob"
        ],
        "units": {
          "z_BL": "bilayer index (1–100)",
          "state": "string: S1 or S2",
          "delta_d_d0": "dimensionless (0.002 or 0.03)",
          "prob": "normalized probability"
        }
      },
      "description": "Probability distribution of surface states for two expansion values, showing migration away from the relaxed surface for Δd > Δd_c."
    },
    {
      "file": "spatial_spectrum.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "blocking_ratio_100BL",
          "surface_peak_weight_relaxed",
          "surface_peak_weight_unrelaxed"
        ],
        "items": {},
        "units": {
          "blocking_ratio_100BL": "dimensionless",
          "surface_peak_weight_relaxed": "arbitrary spectral weight",
          "surface_peak_weight_unrelaxed": "arbitrary spectral weight"
        }
      },
      "description": "Blocking ratio and surface spectral weights quantifying the suppression of surface-state intensity by the relaxation layer."
    }
  ],
  "notes": "All three artifacts are produced by tight-binding calculations using public parameters. The DFT structural optimization stage is omitted (proprietary code) and the task focuses exclusively on the tight-binding part that demonstrates the topological blocking effect."
}
```

## How you are scored
A hidden verifier independently checks each output file against reference values derived from the experimental protocol. `critical_expansion.json` is scored by comparing the reported critical expansion and hopping change to the expected values within appropriate tolerances. `wavefunction_distribution.csv` is checked for structural consistency: the surface‑state probability is expected to concentrate differently on the relaxed vs. opposite side depending on the expansion ratio. `spatial_spectrum.json` is scored by comparing the blocking ratio and peak weights to the expected values. The final reward is a weighted combination of these individual stage scores; simply reporting numbers without correct underlying computation will receive low credit.
