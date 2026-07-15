# Surface state energies and localization on MgB2(0001) surfaces

## Problem background
Magnesium diboride (MgB2) is a layered superconductor whose electronic structure features distinct boron σ and π bands. The (0001) surface of MgB2 supports surface states whose energies and spatial localization depend on the chemical termination (boron, magnesium, or lithium) and on the charge state of the surface layer. Understanding how these surface states behave and how they can be tuned is important for interpreting experiments and for potential applications in plasmonics and superconductivity. In this task, you will reproduce the first-principles identification and characterization of the surface electronic states on MgB2(0001) using density functional theory (DFT).

## Approach
The calculations are carried out with the projector-augmented wave (PAW) method as implemented in the GPAW code, using the local density approximation (LDA) for exchange-correlation. Slab models for three terminations — B-, Mg-, and Li-terminated — are built from the experimental bulk hexagonal lattice constants. After constructing the initial geometries, the atomic positions are relaxed until forces are small. Self-consistent field calculations then yield Kohn-Sham wavefunctions and eigenvalues on a k-point mesh that samples the surface Brillouin zone high-symmetry points Γ, K, and M.

Surface states are identified by computing the projected charge density along the direction normal to the surface and evaluating the surface weight, defined as the integral of that density over the region extending from two bulk unit cells below the surface layer to one unit cell of vacuum above it. Bands whose surface weight exceeds 0.66 are classified as surface states. The energies of the B σ1, sp_z, B σ2, and B σ3 surface bands are then extracted for all three terminations, together with additional localization metrics (surface weight and fraction of the density within the topmost B layer) for the B-terminated case.

## Reproduction target
For each termination (B, Mg, Li), build the periodic slab, relax the geometry, perform the self-consistent DFT calculation, and post-process the wavefunctions to compute the surface weight and identify the surface states. Produce a JSON file (surface_states.json) that contains, for every termination, the energies (in eV relative to the Fermi level) of the B σ1, sp_z, B σ2, and B σ3 surface bands at the Γ, K, and M points. For the B-terminated σ1 band, also report the surface weight at Γ, K, and M. For the B-terminated σ2 and σ3 bands, include the fraction of the wavefunction weight lying in the topmost boron layer at Γ. The output file must adhere to the schema specified in the output contract.

## Assets

- GPAW: https://wiki.fysik.dtu.dk/gpaw/download.html
- ASE: https://wiki.fysik.dtu.dk/ase/
- GPAW LDA pseudopotential setups

## Workflow steps

### Step 1: Construction of slab models
- Role: process
- Action: Construct periodic slab models for three terminations: (a) B-terminated: supercell of 9 Mg and 10 B alternating layers with 4c vacuum; (b) Mg-terminated: add Mg layers on top of each surface of the B-terminated slab; (c) Li-terminated: replace the two surface Mg layers with two Li layers. Use experimental bulk lattice constants a=3.086 Å, c=3.504 Å. Ensure the slab has two surfaces and sufficient vacuum to isolate them.
- Evidence: `/app/outputs/initial_slabs.xyz`

### Step 2: Structural relaxation
- Role: process
- Action: Perform structural relaxation for each termination using GPAW with LDA exchange-correlation. Relax until the maximum force on any atom is below a tight threshold. Save the relaxed geometries.
- Evidence: `/app/outputs/relaxed_slabs.xyz`

### Step 3: Electronic structure calculation
- Role: process
- Action: For each relaxed geometry, perform a self-consistent field DFT calculation with GPAW and LDA to obtain Kohn-Sham wavefunctions and eigenvalues. Use a dense Monkhorst-Pack k-point grid that samples the high-symmetry points Γ, K, and M of the surface Brillouin zone. Save the wavefunction data.
- Evidence: `/app/outputs/wavefunctions.gpw`

### Step 4: Identification of surface states and computation of energies/localization
- Role: scored (load-bearing)
- Action: From the wavefunctions of each termination, compute the projected density in the z-direction ϱ_{n,k}(z) and the surface weight s_{n,k} using the definition: integrate ϱ_{n,k}(z) over the surface region (z0−2c to z0+c plus L−z0−c to L−z0+2c) where z0 is the surface layer coordinate, c the bulk unit-cell height, and L the slab length. Classify bands with s_{n,k} > 0.66 as surface states. For each termination, identify the B σ1, sp_z, B σ2, and B σ3 surface bands (if present). For each such band, record the Kohn-Sham eigenvalue (relative to the Fermi level) at the Γ, K, and M points. For the B-terminated σ1 band, additionally record the surface weight at Γ, K, M. For the B-terminated σ2 and σ3 bands, record the fraction of the wavefunction weight residing in the topmost B layer at the Γ point. Output all results into a single file surface_states.json following the schema described below.
- Output file: `/app/outputs/surface_states.json`
- Format: json
- Contract: JSON object with top-level keys 'B', 'Mg', 'Li'. Each key maps to a list of surface state records. Each record is a dict with keys: 'label' (string, e.g. 'sigma1', 'sp_z', 'sigma2', 'sigma3'), 'energy_gamma' (float), 'energy_k' (float), 'energy_m' (float). For the B-terminated 'sigma1' record, additionally include 'surface_weight_gamma', 'surface_weight_k', 'surface_weight_m' (float). For the B-terminated 'sigma2' and 'sigma3' records, include 'topmost_layer_fraction_gamma' (float). All energies in eV relative to the Fermi level.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_states.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_states.json
- path: `/app/outputs/surface_states.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file with surface state energies in eV relative to the Fermi level and, for B termination, surface weights and topmost-layer fractions.
- schema:
  - `type`: object
  - `required`: `B`, `Mg`, `Li`
  - `properties`:
    - `B`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `label`, `energy_gamma`, `energy_k`, `energy_m`
        - `properties`:
          - `label`:
            - `type`: string
          - `energy_gamma`:
            - `type`: number
          - `energy_k`:
            - `type`: number
          - `energy_m`:
            - `type`: number
          - `surface_weight_gamma`:
            - `type`: number
          - `surface_weight_k`:
            - `type`: number
          - `surface_weight_m`:
            - `type`: number
          - `topmost_layer_fraction_gamma`:
            - `type`: number
    - `Mg`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `label`, `energy_gamma`, `energy_k`, `energy_m`
        - `properties`:
          - `label`:
            - `type`: string
          - `energy_gamma`:
            - `type`: number
          - `energy_k`:
            - `type`: number
          - `energy_m`:
            - `type`: number
    - `Li`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `label`, `energy_gamma`, `energy_k`, `energy_m`
        - `properties`:
          - `label`:
            - `type`: string
          - `energy_gamma`:
            - `type`: number
          - `energy_k`:
            - `type`: number
          - `energy_m`:
            - `type`: number

Notes: The checker compares reported energies to digitized reference values from the paper (hidden) with a tolerance, and verifies that B-terminated sigma1 surface weights are ≥ 0.66 and sigma2/sigma3 topmost layer fractions are ≥ 0.90. Weighting: 60% energy accuracy, 20% surface weight threshold, 20% topmost layer fraction threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "B",
          "Mg",
          "Li"
        ],
        "properties": {
          "B": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "label",
                "energy_gamma",
                "energy_k",
                "energy_m"
              ],
              "properties": {
                "label": {
                  "type": "string"
                },
                "energy_gamma": {
                  "type": "number"
                },
                "energy_k": {
                  "type": "number"
                },
                "energy_m": {
                  "type": "number"
                },
                "surface_weight_gamma": {
                  "type": "number"
                },
                "surface_weight_k": {
                  "type": "number"
                },
                "surface_weight_m": {
                  "type": "number"
                },
                "topmost_layer_fraction_gamma": {
                  "type": "number"
                }
              }
            }
          },
          "Mg": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "label",
                "energy_gamma",
                "energy_k",
                "energy_m"
              ],
              "properties": {
                "label": {
                  "type": "string"
                },
                "energy_gamma": {
                  "type": "number"
                },
                "energy_k": {
                  "type": "number"
                },
                "energy_m": {
                  "type": "number"
                }
              }
            }
          },
          "Li": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "label",
                "energy_gamma",
                "energy_k",
                "energy_m"
              ],
              "properties": {
                "label": {
                  "type": "string"
                },
                "energy_gamma": {
                  "type": "number"
                },
                "energy_k": {
                  "type": "number"
                },
                "energy_m": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "JSON file with surface state energies in eV relative to the Fermi level and, for B termination, surface weights and topmost-layer fractions."
    }
  ],
  "notes": "The checker compares reported energies to digitized reference values from the paper (hidden) with a tolerance, and verifies that B-terminated sigma1 surface weights are ≥ 0.66 and sigma2/sigma3 topmost layer fractions are ≥ 0.90. Weighting: 60% energy accuracy, 20% surface weight threshold, 20% topmost layer fraction threshold."
}
```

## How you are scored
A hidden verifier running independently will read your surface_states.json. It will compare the energies you report against reference values (derived from the paper’s published band structure) within a tolerance that accounts for typical differences between DFT implementations. It will check that the surface weights for the B-terminated σ1 band are at least 0.66 at all three k‑points, and that the topmost‑layer fractions for σ2 and σ3 are at least 0.9 at Γ. The final reward is a weighted combination of these energy accuracy and localization checks. Simply inserting numbers from the literature without performing the required calculations will not yield a passing score, because the verifier expects physically reasonable results consistent with a genuine DFT run.
