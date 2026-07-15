# Compute ZT for ordered flat DNA ladder at 400 K

## Problem background
Thermoelectric energy conversion in molecular junctions offers a route to waste-heat harvesting at the nanoscale. This work models a flat DNA segment as a two-stranded tight-binding ladder and investigates its thermoelectric performance, quantified by the electronic figure of merit ZT. The central challenge is to compute ZT for a given molecular configuration as a function of the Fermi energy, and to determine whether this DNA-based junction can achieve efficient energy conversion.

## Approach
The system is described by a nearest-neighbor tight-binding Hamiltonian for a flat DNA ladder with two strands and inter-strand coupling. The molecule is taken as an ordered alternating sequence of two base-pair types (A and B) with 50 base pairs. Electronic transmission T(E) is computed using the transfer-matrix method together with Oseledec's theorem: the transfer matrices are built from the site energies and hoppings, and the smallest Lyapunov exponent gives the localization length, from which T(E) follows. At a fixed temperature of 400 K, the Landauer integrals L0, L1, L2 are evaluated numerically from T(E) for a dense grid of equilibrium Fermi energies Ef ∈ [−2.0, 2.0] eV. The figure of merit ZT is then obtained as ZT = 1/(L0 L2 / L1^2 − 1). The result is a curve of ZT versus Ef that captures the thermoelectric response of the ordered DNA junction.

## Reproduction target
Implement the tight-binding Hamiltonian and the transfer-matrix transmission calculation as described for an ordered alternating DNA ladder (sequence A B A B ...) with 50 base pairs at 400 K, using the on-site energies and hopping parameters listed in the Workflow steps. Compute the ZT curve over the Fermi energy interval [−2.0, 2.0] eV with a step size no larger than 0.01 eV and write it to a CSV file (ZT_vs_Ef.csv). From this curve extract the maximum ZT and the Ef at which it occurs and write them to a JSON file (summary.json). The task is to produce a physically correct ZT curve that follows from the stated model and parameters; the hidden scorer will verify the shape and peak of the curve as well as self-consistency between the two files.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute ZT vs Ef for ordered DNA ladder at T=400 K
- Role: scored (load-bearing)
- Action: Implement the tight-binding Hamiltonian for a two-stranded flat DNA ladder with alternating A-B sequence (N=50) using the following on-site energies: E_A=0.26 eV, E_T=-0.93 eV, E_G=1.14 eV, E_C=-1.06 eV, and homogeneous inter-site and inter-strand hoppings λ=2.8 eV, molecule-lead coupling v_ML=2.8 eV. Compute electronic transmission T(E) via the transfer-matrix method together with Oseledec's theorem (find the smallest Lyapunov exponent, localization length, and T(E)=exp(-2N/Λ(E))). At T=400 K, evaluate Landauer integrals L_n as functions of Fermi energy E_f over [-2.0, 2.0] eV, then compute figure of merit ZT = 1/(L_0 L_2 / L_1^2 − 1). Write the ZT vs E_f table to the output CSV.
- Output file: `/app/outputs/ZT_vs_Ef.csv`
- Format: csv
- Contract: Two columns: column 1 is Ef (float, eV), column 2 is ZT (float, dimensionless). May include header row with column names 'Ef' and 'ZT'.
- Scoring: scored by hidden verifier

### Step 2: Extract maximum ZT and corresponding Ef
- Role: scored
- Action: Read ZT_vs_Ef.csv, find the row with the maximum ZT value, and write the max ZT and the Ef at which it occurs to a JSON file.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: {"max_ZT": <float>, "Ef_at_max_ZT": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ZT_vs_Ef.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ZT_vs_Ef.csv
- path: `/app/outputs/ZT_vs_Ef.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV table of Fermi energy vs. figure of merit ZT for the ordered DNA ladder at T=400 K. The checker recomputes the maximum ZT from this table and scores it against a hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `Ef`, `ZT`
  - `units`:
    - `Ef`: eV
    - `ZT`: dimensionless

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Extracted maximum ZT and the Fermi energy where it occurs. The checker will verify that these values are consistent with the ZT_vs_Ef.csv table.
- schema:
  - `type`: object
  - `required`:
    - `max_ZT`: float
    - `Ef_at_max_ZT`: float
  - `units`:
    - `max_ZT`: dimensionless
    - `Ef_at_max_ZT`: eV

Notes: The hidden checker recomputes the maximum ZT and its associated Ef directly from ZT_vs_Ef.csv and compares them against a paper-derived gold threshold and energy window. The summary.json is additionally verified for self-consistency. The reward is determined solely by the checker's recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ZT_vs_Ef.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ef",
          "ZT"
        ],
        "units": {
          "Ef": "eV",
          "ZT": "dimensionless"
        }
      },
      "description": "CSV table of Fermi energy vs. figure of merit ZT for the ordered DNA ladder at T=400 K. The checker recomputes the maximum ZT from this table and scores it against a hidden threshold."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "max_ZT": "float",
          "Ef_at_max_ZT": "float"
        },
        "units": {
          "max_ZT": "dimensionless",
          "Ef_at_max_ZT": "eV"
        }
      },
      "description": "Extracted maximum ZT and the Fermi energy where it occurs. The checker will verify that these values are consistent with the ZT_vs_Ef.csv table."
    }
  ],
  "notes": "The hidden checker recomputes the maximum ZT and its associated Ef directly from ZT_vs_Ef.csv and compares them against a paper-derived gold threshold and energy window. The summary.json is additionally verified for self-consistency. The reward is determined solely by the checker's recomputation."
}
```

## How you are scored
A hidden automated verifier inspects the artifacts you write. It recomputes the maximum ZT and its corresponding Ef directly from your ZT_vs_Ef.csv, checks that your summary.json reports the same values, and assesses whether your computed ZT curve faithfully reflects the physics of the model (e.g., correct peak location, smoothness, and finite positive values). The reward is a weighted combination of these checks, with the majority of credit coming from the ZT-vs-Ef data rather than from shape-only validation. Submitting fabricated numbers that match a guessed target will not receive credit — the verifier uses reference computations and consistency checks that only a correct implementation passes.
