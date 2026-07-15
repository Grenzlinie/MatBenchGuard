# Monte Carlo Surface Tension Calculation via Free Energy Method

## Problem background
Surface tension of liquids is a fundamental thermodynamic property. A computational method that directly computes the Helmholtz free energy required to create a surface can yield lower statistical uncertainty than mechanical stress calculations. The method is demonstrated for the Lennard‑Jones 6:12 fluid at temperature and density conditions close to the argon triple point.

## Approach
The free energy of surface creation is computed by reversibly converting a bulk liquid with periodic boundary conditions into a slab of liquid held together by its own cohesion. This is accomplished in five stages:

1. **Bulk tail correction** – numerically integrate the Lennard‑Jones potential tail beyond the truncation radius (2.5 σ) for a uniform bulk liquid.
2. **Slab separation** – using Monte Carlo simulations and Bennett's acceptance ratio method, gradually increase the slab separation parameter Δ from 0 to beyond the interaction cut‑off, recording the cumulative free energy change.
3. **Cut‑off distance increase** – using Bennett's method, compute the free energy difference between the slab system with a cut‑off of 2.5 σ and one with a cut‑off of 5.0 σ.
4. **Surface relaxation** – relax the hard walls outward symmetrically while sampling the density at the walls via Monte Carlo; integrate the force (kT × density) along the wall position to obtain the relaxation free energy.
5. **Free surface tail correction** – compute the long‑range correction for the potential tail beyond 5.0 σ for the final free‑surface slab.

The total free energy of surface creation is the sum of these five contributions. The macroscopic surface tension and excess internal energy are then obtained by dividing by the total surface area and converting to cgs units using the argon parameters (ε / k = 119.8 K, σ = 3.405 Å).

## Reproduction target
Implement the five‑stage free‑energy calculation for a system of N = 216 Lennard‑Jones 12:6 particles at reduced temperature T* = 0.7 and reduced density ρ* = 0.85. Perform the required Monte Carlo runs with the specified cut‑off distances (2.5 σ and 5.0 σ) and Bennett’s acceptance ratio method. Compute all five free‑energy differences (Fb−Fa, Fc−Fb, Fd−Fc, Fe−Fd, Ff−Fe). From the total free energy of surface creation, calculate the surface tension γ in dyn/cm and the excess internal energy U_s in erg/cm². Write all intermediate and final results to `/app/outputs/results.json` according to the output contract. The objective is to produce a correct reproduction of the surface properties; a hidden verifier will compare your numbers to reference values that would be obtained from a faithful implementation of the described procedure.

## Assets
This task requires only public knowledge:
- Lennard‑Jones 12:6 pair potential (standard analytic form)
- Bennett acceptance ratio algorithm
- Argon parameters: ε / k = 119.8 K, σ = 3.405 Å (these are fixed physical constants for the conversion to macroscopic units).
No external datasets, models, or proprietary software are needed.

## Workflow steps

### Step 1: Bulk liquid tail correction
- Role: process
- Action: Compute the free energy difference between the full Lennard-Jones potential and the truncated potential (cut-off 2.5σ) for the uniform bulk liquid using numerical integration of the potential tail, assuming uniform radial distribution function.
- Evidence: `/app/outputs/evidence_bulk_tail.txt`

### Step 2: Monte Carlo slab separation free energy
- Role: process
- Action: Using Monte Carlo simulations and Bennett's acceptance ratio method, gradually separate the bulk liquid into slabs with hard walls by increasing the slab separation parameter Δ from 0 to beyond the cut-off distance. Record the cumulative free energy change Fc - Fb.
- Evidence: `/app/outputs/evidence_slab_separation.json`

### Step 3: Cut-off distance increase free energy
- Role: process
- Action: Using Bennett's method, compute the free energy difference between the slab system with potential cut-off 2.5σ and with cut-off 5.0σ.
- Evidence: `/app/outputs/evidence_cutoff_increase.txt`

### Step 4: Surface relaxation free energy
- Role: process
- Action: Relax the hard walls by moving them outward symmetrically, sample the density at the walls via Monte Carlo, and integrate the force (kT times density) to obtain the relaxation free energy Fe - Fd.
- Evidence: `/app/outputs/evidence_relaxation.json`

### Step 5: Free surface tail correction
- Role: process
- Action: Compute the free energy correction from the potential tail beyond 5.0σ to infinity for the free-surface slab, assuming uniform density.
- Evidence: `/app/outputs/evidence_surface_tail.txt`

### Step 6: Surface tension and excess internal energy
- Role: scored (load-bearing)
- Action: Sum all free energy contributions (Fb-Fa, Fc-Fb, Fd-Fc, Fe-Fd, Ff-Fe) to obtain total free energy of surface creation. Compute the total surface area. Calculate surface tension γ = ΔF_total / (2 * Lx * Ly) and convert to dyn/cm using argon parameters (ε/k = 119.8 K, σ = 3.405 Å). Compute excess internal energy Us from the average potential energies of the bulk and free-surface states and convert to erg/cm². Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: total_free_energy (float, units of ε), surface_tension (float, dyn/cm), excess_internal_energy (float, erg/cm²), stages : { Fb_minus_Fa: float, Fc_minus_Fb: float, Fd_minus_Fc: float, Fe_minus_Fd: float, Ff_minus_Fe: float }.
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
- target_policy: reference_match
- description: Final aggregated results: total free energy of surface creation, surface tension, excess internal energy, and the five stage free energy differences. The checker compares these to the paper's reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `total_free_energy`: number (units of ε)
    - `surface_tension`: number (dyn/cm)
    - `excess_internal_energy`: number (erg/cm²)
    - `stages`:
      - `type`: object
      - `required`:
        - `Fb_minus_Fa`: number (units of ε)
        - `Fc_minus_Fb`: number (units of ε)
        - `Fd_minus_Fc`: number (units of ε)
        - `Fe_minus_Fd`: number (units of ε)
        - `Ff_minus_Fe`: number (units of ε)

Notes: The perturbation theory correction (BFW+ATM) is not required for this core reproduction.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_free_energy": "number (units of ε)",
          "surface_tension": "number (dyn/cm)",
          "excess_internal_energy": "number (erg/cm²)",
          "stages": {
            "type": "object",
            "required": {
              "Fb_minus_Fa": "number (units of ε)",
              "Fc_minus_Fb": "number (units of ε)",
              "Fd_minus_Fc": "number (units of ε)",
              "Fe_minus_Fd": "number (units of ε)",
              "Ff_minus_Fe": "number (units of ε)"
            }
          }
        }
      },
      "description": "Final aggregated results: total free energy of surface creation, surface tension, excess internal energy, and the five stage free energy differences. The checker compares these to the paper's reported values with appropriate tolerances."
    }
  ],
  "notes": "The perturbation theory correction (BFW+ATM) is not required for this core reproduction."
}
```

## How you are scored
A hidden verifier reads your `results.json` and independently checks each reported free‑energy difference and the final surface tension and excess internal energy against reference values derived from a faithful implementation. The score is a weighted combination of the closeness of each stage and the final macroscopic properties; meeting or exceeding the reference quality within expected reproduction tolerances earns full credit. Simply printing the paper’s numbers is not sufficient – the workflow must be executed and the evidence of intermediate computations must be consistent with the final results.
