# Compute Clustering Fractions in a Variational Cell Model for fcc Solids

## Problem background
In a system of penetrable spheres, particles can overlap at a finite energy cost. At high densities, the solid phase can lower its free energy by allowing multiple particles to occupy the same lattice site — a phenomenon called clustering. A variational cell model for fcc crystals expresses the per‑particle free energy as a function of the fractions of sites occupied by pairs (z) and by triplets (w). The model depends on the hard‑sphere reference free energy of an fcc crystal, which is provided as a table. The goal is to compute the equilibrium cluster composition (z, w) and the resulting minimized free energy for given thermodynamic conditions.

## Approach
The variational free energy per particle is a function of the packing fraction η, reduced temperature t, and site fractions (z,w), involving the hard‑sphere reference free energy f0 evaluated at an effective packing fraction γ = η/(1+z+2w), plus energetic and entropic terms. The reference data f0(γ) is provided as a CSV file (fcc_hs_free_energy.csv); you should interpolate it as needed. For each (η,t) condition, construct the free energy surface over the triangular domain z ≥ 0, w ≥ 0, z + w ≤ 1, and numerically minimize it to find the optimal (z,w). The minimized free energy per particle (in units of k_B T) is then recorded together with the optimal fractions. The exact functional form is given in the workflow step; you must implement it and perform the minimization.

## Reproduction target
Compute the optimal z, w, and minimized free energy per particle for a clustered fcc solid at the following (η,t) conditions:  
- a scan of η values from 0.5 to 2.0 at constant t = 0.05, and  
- a single point η = 0.8, t = 0.1.  
Write the results to /app/outputs/clustering_results.csv with columns: eta, t, z, w, free_energy_per_particle. Each row corresponds to one (η,t) point; the free energy is the minimum value obtained from the minimization over z and w.

## Assets

- fcc_hs_free_energy.csv

## Workflow steps

### Step 1: Compute clustered solid fractions and free energy
- Role: scored (load-bearing)
- Action: Implement the variational free-energy expression for clustered fcc solids: f = f0(η/(1+z+2w)) + (z+3w)/(1+z+2w)*(1/t) + (z*ln2 + w*ln6)/(1+z+2w) + [z*ln z + w*ln w + (1-z-w)*ln(1-z-w)]/(1+z+2w). Load the hard-sphere reference free energy f0(γ) from the provided CSV (interpolating as needed). For each (η,t) condition specified in the task instructions, construct the free energy function in terms of site fractions (z,w) within the triangular domain (z≥0, w≥0, z+w≤1), and perform a minimization to find the optimal z and w. Write the optimal z, w, and the minimized free energy per particle to the output CSV.
- Output file: `/app/outputs/clustering_results.csv`
- Format: csv
- Contract: eta (float), t (float), z (float), w (float), free_energy_per_particle (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/clustering_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### clustering_results.csv
- path: `/app/outputs/clustering_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV with optimal site fractions and minimized free energy per particle for each evaluated condition. The free energy is in units of k_B T.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `t`, `z`, `w`, `free_energy_per_particle`
  - `units`: object

Notes: The checker will compare the reported z, w, and free_energy_per_particle for each condition to hidden gold values derived from the paper's results, using absolute tolerances. The hard-sphere reference free energy data is provided as a bundled resource (fcc_hs_free_energy.csv).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "clustering_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "t",
          "z",
          "w",
          "free_energy_per_particle"
        ],
        "units": {}
      },
      "description": "CSV with optimal site fractions and minimized free energy per particle for each evaluated condition. The free energy is in units of k_B T."
    }
  ],
  "notes": "The checker will compare the reported z, w, and free_energy_per_particle for each condition to hidden gold values derived from the paper's results, using absolute tolerances. The hard-sphere reference free energy data is provided as a bundled resource (fcc_hs_free_energy.csv)."
}
```

## How you are scored
A hidden verifier will evaluate your /app/outputs/clustering_results.csv. For each (η,t) condition, it will compare your reported z, w, and free_energy_per_particle to hidden gold values derived from the paper's results, using absolute tolerances. A structural trend (e.g., monotonic increase of z with η at fixed t) may also be checked. The final reward is a weighted combination across the conditions. Simply reporting the paper's numbers without performing the minimization is not sufficient; you must implement the variational model and compute the quantities.
