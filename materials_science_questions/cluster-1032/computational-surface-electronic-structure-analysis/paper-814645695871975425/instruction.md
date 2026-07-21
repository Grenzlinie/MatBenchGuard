# Electronic surface states in triple-constituent semiconductor superlattices

## Problem background
Semiconductor superlattices exhibit electronic surface states whose dispersion and localization can influence device behavior. In a triple-constituent GaSb/AlSb/InAs superlattice, the energies of surface states and their dependence on the constituent layer thicknesses are of interest. Understanding how the surface-state energies evolve relative to the superlattice bulk subband edges, and whether a transition occurs at a particular thickness, is important for potential applications in high-speed electronics.

## Approach
This task uses a two-band tight-binding model to describe the electronic structure of each constituent material (GaSb, AlSb, InAs) and of the superlattice. The necessary tight-binding parameters (orbital self-energies and hopping integrals) are taken from the publicly available paper by Rahmani et al. (J. Phys. C 21, 4761, 1988).

The superlattice is built by coupling finite slabs of the three materials using an interface response formalism. For the semi-infinite case with a surface, the theory yields a surface-secular equation D(E)=0 whose solutions give the energies of possible electronic surface states. An additional decay factor t(E) must satisfy |t|<1 for a true surface-localized state.

The workflow proceeds by first computing the superlattice bulk subbands (in particular the heavy-hole edge HH_1) as functions of layer thickness L. Then, for the InAs-terminated surface with an In top plane, the surface-secular equation is solved for layer thicknesses L = 2 to 6, yielding the surface-state energy, the corresponding HH_1 energy, and the decay factor. In a separate step, for L=2 the surface-state energy is computed as a function of the in-plane wave-vector parameter Q (defined as Q = 1 - cos(k1 a0/2) cos(k2 a0/2)) for Q from 0 to 1.

## Reproduction target
Compute, for the InAs-terminated (In top plane) semi-infinite GaSb/AlSb/InAs superlattice:

1. The surface-state energy E_surface, the heavy-hole subband edge HH_1, and the decay factor t_decay for integer layer thickness L from 2 to 6. Determine whether and at what L the surface-state energy crosses the HH_1 level (i.e., E_surface becomes lower than HH_1).

2. For L=2, the surface-state energy E_surface as a function of the dimensionless wave-vector parameter Q, with Q = 0.0, 0.1, ..., 1.0. Confirm that the decay factor satisfies |t|<1 for all computed states.

## Assets

- Tight-binding parameters for GaSb, AlSb, InAs (two-band model): 10.1088/0022-3719/21/26/012

## Workflow steps

### Step 1: Surface state energies vs layer thickness
- Role: scored (load-bearing)
- Action: Using the tight-binding parameters from Rahmani et al., construct the two-band model for the InAs-terminated semi-infinite GaSb/AlSb/InAs superlattice. For each layer thickness L from 2 to 6, compute the heavy-hole band edge HH_1 and solve the surface secular equation D(E)=0 to find the surface state energy E_surface and the localization decay factor t (enforcing |t|<1). Record results.
- Output file: `/app/outputs/surface_vs_L.csv`
- Format: csv
- Contract: columns: L (int), E_surface (float), E_HH1 (float), t_decay (float)
- Scoring: scored by hidden verifier

### Step 2: Surface state dispersion vs Q for L=2
- Role: scored
- Action: For L=2 and the same InAs-terminated surface, compute the surface state energy as a function of the dimensionless parameter Q (defined in terms of in-plane wave-vectors) for Q from 0 to 1 in steps of 0.1. Record results.
- Output file: `/app/outputs/dispersion_Q.csv`
- Format: csv
- Contract: columns: Q (float), E_surface (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_vs_L.csv`
- `/app/outputs/dispersion_Q.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_vs_L.csv
- path: `/app/outputs/surface_vs_L.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Scored artifact: surface state energy and localization factor versus layer thickness L. The checker verifies agreement with reference values within tolerance and checks t_decay < 1.
- schema:
  - `type`: table
  - `required_columns`: `L`, `E_surface`, `E_HH1`, `t_decay`
  - `units`:
    - `E_surface`: eV
    - `E_HH1`: eV
    - `t_decay`: dimensionless

### dispersion_Q.csv
- path: `/app/outputs/dispersion_Q.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Scored artifact: surface state energy as a function of Q for L=2. The checker verifies agreement with the reference dispersion within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Q`, `E_surface`
  - `units`:
    - `E_surface`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_vs_L.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "E_surface",
          "E_HH1",
          "t_decay"
        ],
        "units": {
          "E_surface": "eV",
          "E_HH1": "eV",
          "t_decay": "dimensionless"
        }
      },
      "description": "Scored artifact: surface state energy and localization factor versus layer thickness L. The checker verifies agreement with reference values within tolerance and checks t_decay < 1."
    },
    {
      "file": "dispersion_Q.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Q",
          "E_surface"
        ],
        "units": {
          "E_surface": "eV"
        }
      },
      "description": "Scored artifact: surface state energy as a function of Q for L=2. The checker verifies agreement with the reference dispersion within tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently examine your two output CSV files. For surface_vs_L.csv it will check that the computed energies and decay factors are physically reasonable and that the critical crossing thickness (where E_surface falls below HH_1) is correctly identified. For dispersion_Q.csv it will compare the surface-state energies versus Q to expected reference values, verifying consistency and localization. Each scored artifact contributes a portion of the final reward; simply reporting a number that matches expectation is not sufficient — your computed data must demonstrate genuine reproduction of the underlying physics.
