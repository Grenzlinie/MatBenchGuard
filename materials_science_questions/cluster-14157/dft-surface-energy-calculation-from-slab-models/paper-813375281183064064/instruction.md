# Surface alloy atomic arrangements via Monte Carlo with cluster expansion Hamiltonians

## Problem background
Bimetallic surface alloys often exhibit catalytic properties that differ from their pure constituents, partly because the arrangement of atoms at the surface determines which active sites are available. Two important model systems are AuPd/Pd(100) and AuPt/Pt(100), where a monolayer of Au is mixed with a small fraction of Pd or Pt, respectively. The interatomic interactions in these alloys can be either heteronuclear (favoring unlike-atom pairs) or homonuclear (favoring like-atom pairs), and this tendency strongly influences whether the minority component atoms disperse as isolated monomers or aggregate into larger clusters. Understanding and quantifying these atomic arrangements is essential for rational catalyst design. The present computational reproduction task is to determine, via Monte Carlo simulation, the equilibrium distribution of monomers and dimers and the short-range order in these two alloy surfaces at selected coverages and temperatures, including a special case of c(2×2) ordering in AuPd.

## Approach
The energy of a surface alloy configuration is described by a cluster expansion Hamiltonian that expresses the total energy as a sum of effective cluster interactions (ECIs) over point, pair, and multibody clusters up to the third nearest‑neighbour shell. The ECIs for AuPd/Pd(100) and AuPt/Pt(100) have been obtained from first-principles calculations and are provided in a supporting resource file. Using these Hamiltonians, a canonical (NVT) Monte Carlo simulation is performed on a 30×30 fcc(100) lattice with periodic boundary conditions. Swaps between unlike atoms are attempted, and the difference in cluster-expansion energy determines the acceptance probability via the Metropolis criterion. After equilibration, ensemble-averaged quantities are collected: (i) the fraction of minority atoms (Pd or Pt) that exist as monomers (four nearest neighbours of opposite species) and as dimers (two contiguous monomers), and (ii) the probability of finding a minority atom at specified neighbour distances, from which the short-range order parameter α is computed. As a reference, the same quantities for a completely random, non-interacting alloy are computed analytically from the lattice topology and coverage, providing a baseline for comparison.

## Reproduction target
Produce a single JSON file `simulation_results.json` containing the following ten numeric fields derived from the Monte Carlo simulations and the analytical random baseline:

- `AuPd_monomer_fraction_theta015_T300`: monomer fraction for AuPd at Pd coverage θ = 0.15 and T = 300 K.
- `AuPd_dimer_fraction_theta015_T300`: dimer fraction for AuPd at θ = 0.15 and T = 300 K.
- `AuPt_monomer_fraction_theta015_T300`: monomer fraction for AuPt at Pt coverage θ = 0.15 and T = 300 K.
- `AuPt_dimer_fraction_theta015_T300`: dimer fraction for AuPt at θ = 0.15 and T = 300 K.
- `AuPd_short_range_order_1NN_theta01_T300`: short-range order parameter α at the 1st nearest‑neighbour distance for AuPd at θ = 0.10 and T = 300 K.
- `AuPd_short_range_order_2NN_theta01_T300`: α at the 2nd nearest‑neighbour distance for AuPd at θ = 0.10 and T = 300 K.
- `AuPd_short_range_order_3NN_theta01_T300`: α at the 3rd nearest‑neighbour distance for AuPd at θ = 0.10 and T = 300 K.
- `AuPd_c2x2_alpha_1NN_theta05_T100`: α at the 1st nearest‑neighbour distance for AuPd at θ = 0.50 (50 % Pd) and T = 100 K, representing the tendency toward c(2×2) ordering.
- `random_monomer_fraction_theta015`: analytically computed monomer fraction for a random fcc(100) alloy at θ = 0.15.
- `random_dimer_fraction_theta015`: analytically computed dimer fraction for a random fcc(100) alloy at θ = 0.15.

All quantities must lie within physically meaningful ranges (monomer/dimer fractions between 0 and 1, α between −1 and 1).

## Assets

- Cluster expansion coefficients for AuPd/Pd(100) and AuPt/Pt(100) are provided as a supporting resource (see resource file `ce_coefficients`). The coefficients include effective cluster interactions up to the third nearest-neighbour distance for both alloy systems.

## Workflow steps

### Step 1: Compute random alloy baseline monomer and dimer fractions
- Role: process
- Action: Analytically compute the expected monomer fraction (1−θ)^4 and dimer fraction 4θ(1−θ)^6 for a non-interacting fcc(100) surface alloy at θ = 0.15. Store these values for inclusion in the final output.

### Step 2: Run Monte Carlo simulations for AuPd and AuPt surface alloys
- Role: process
- Action: Implement canonical (NVT) Monte Carlo simulation on a 30×30 fcc(100) lattice with periodic boundary conditions. Use the cluster expansion Hamiltonians (effective cluster interactions up to third nearest neighbour) for AuPd/Pd(100) and AuPt/Pt(100) from the supporting resource to evaluate configuration energies every trial swap. Run simulations for the following condition sets:
  - (i) AuPd at θ = 0.15, T = 300 K
  - (ii) AuPt at θ = 0.15, T = 300 K
  - (iii) AuPd at θ = 0.10, T = 300 K
  - (iv) AuPd at θ = 0.50, T = 100 K
  After equilibration, collect ensemble‑averaged statistics for each simulation: monomer and dimer counts per configuration, and the probability of finding a minority atom at 1st, 2nd, and 3rd nearest‑neighbour distances from a minority atom (i.e. the conditional probability p_AB(r) that a given neighbour shell r around a minority atom contains the opposite species). For condition (iv) only the 1st nearest‑neighbour statistics are needed.

### Step 3: Extract monomer/dimer fractions, short-range order parameters, and output final scored JSON
- Role: scored (load-bearing)
- Action: From the MC statistics compute the ensemble-averaged monomer fraction and dimer fraction for each alloy. For the AuPd simulations at θ = 0.10 and at θ = 0.50, compute the short-range order parameter
  α(r) = 1 − p_AB(r)/x_B,
  where x_B = θ is the minority coverage. At θ = 0.10, compute α for 1st, 2nd, and 3rd nearest‑neighbour distances; at θ = 0.50 (c(2×2) condition) compute α only for the 1st nearest‑neighbour distance. Combine all values with the random baseline from Step 1 into a single JSON file `simulation_results.json` containing all ten required fields.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: {"type":"object","required":["AuPd_monomer_fraction_theta015_T300","AuPd_dimer_fraction_theta015_T300","AuPt_monomer_fraction_theta015_T300","AuPt_dimer_fraction_theta015_T300","AuPd_short_range_order_1NN_theta01_T300","AuPd_short_range_order_2NN_theta01_T300","AuPd_short_range_order_3NN_theta01_T300","AuPd_c2x2_alpha_1NN_theta05_T100","random_monomer_fraction_theta015","random_dimer_fraction_theta015"],"properties":{"AuPd_monomer_fraction_theta015_T300":{"type":"number","minimum":0,"maximum":1},"AuPd_dimer_fraction_theta015_T300":{"type":"number","minimum":0,"maximum":1},"AuPt_monomer_fraction_theta015_T300":{"type":"number","minimum":0,"maximum":1},"AuPt_dimer_fraction_theta015_T300":{"type":"number","minimum":0,"maximum":1},"AuPd_short_range_order_1NN_theta01_T300":{"type":"number","minimum":-1,"maximum":1},"AuPd_short_range_order_2NN_theta01_T300":{"type":"number","minimum":-1,"maximum":1},"AuPd_short_range_order_3NN_theta01_T300":{"type":"number","minimum":-1,"maximum":1},"AuPd_c2x2_alpha_1NN_theta05_T100":{"type":"number","minimum":-1,"maximum":1},"random_monomer_fraction_theta015":{"type":"number","minimum":0,"maximum":1},"random_dimer_fraction_theta015":{"type":"number","minimum":0,"maximum":1}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Final scored JSON containing ten numeric fields: monomer and dimer fractions for AuPd and AuPt at θ=0.15, T=300 K, short-range order parameters for AuPd at θ=0.1, T=300 K, the c(2×2) α(1NN) for AuPd at θ=0.5, T=100 K, and the analytically computed random alloy baseline.
- schema:
  - `type`: object
  - `required`: `AuPd_monomer_fraction_theta015_T300`, `AuPd_dimer_fraction_theta015_T300`, `AuPt_monomer_fraction_theta015_T300`, `AuPt_dimer_fraction_theta015_T300`, `AuPd_short_range_order_1NN_theta01_T300`, `AuPd_short_range_order_2NN_theta01_T300`, `AuPd_short_range_order_3NN_theta01_T300`, `AuPd_c2x2_alpha_1NN_theta05_T100`, `random_monomer_fraction_theta015`, `random_dimer_fraction_theta015`
  - `properties`:
    - `AuPd_monomer_fraction_theta015_T300`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `AuPd_dimer_fraction_theta015_T300`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `AuPt_monomer_fraction_theta015_T300`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `AuPt_dimer_fraction_theta015_T300`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `AuPd_short_range_order_1NN_theta01_T300`:
      - `type`: number
      - `minimum`: -1
      - `maximum`: 1
    - `AuPd_short_range_order_2NN_theta01_T300`:
      - `type`: number
      - `minimum`: -1
      - `maximum`: 1
    - `AuPd_short_range_order_3NN_theta01_T300`:
      - `type`: number
      - `minimum`: -1
      - `maximum`: 1
    - `AuPd_c2x2_alpha_1NN_theta05_T100`:
      - `type`: number
      - `minimum`: -1
      - `maximum`: 1
    - `random_monomer_fraction_theta015`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `random_dimer_fraction_theta015`:
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "AuPd_monomer_fraction_theta015_T300",
          "AuPd_dimer_fraction_theta015_T300",
          "AuPt_monomer_fraction_theta015_T300",
          "AuPt_dimer_fraction_theta015_T300",
          "AuPd_short_range_order_1NN_theta01_T300",
          "AuPd_short_range_order_2NN_theta01_T300",
          "AuPd_short_range_order_3NN_theta01_T300",
          "AuPd_c2x2_alpha_1NN_theta05_T100",
          "random_monomer_fraction_theta015",
          "random_dimer_fraction_theta015"
        ],
        "properties": {
          "AuPd_monomer_fraction_theta015_T300": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "AuPd_dimer_fraction_theta015_T300": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "AuPt_monomer_fraction_theta015_T300": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "AuPt_dimer_fraction_theta015_T300": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "AuPd_short_range_order_1NN_theta01_T300": {
            "type": "number",
            "minimum": -1,
            "maximum": 1
          },
          "AuPd_short_range_order_2NN_theta01_T300": {
            "type": "number",
            "minimum": -1,
            "maximum": 1
          },
          "AuPd_short_range_order_3NN_theta01_T300": {
            "type": "number",
            "minimum": -1,
            "maximum": 1
          },
          "AuPd_c2x2_alpha_1NN_theta05_T100": {
            "type": "number",
            "minimum": -1,
            "maximum": 1
          },
          "random_monomer_fraction_theta015": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "random_dimer_fraction_theta015": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          }
        }
      },
      "description": "Final scored JSON containing ten numeric fields: monomer and dimer fractions for AuPd and AuPt at θ=0.15, T=300 K, short-range order parameters for AuPd at θ=0.1, T=300 K, the c(2×2) α(1NN) for AuPd at θ=0.5, T=100 K, and the analytically computed random alloy baseline."
    }
  ]
}
```

## How you are scored
A hidden verifier performs a structural audit of your `simulation_results.json`. It checks the following properties without requiring an exact match to any published numeric values:

- For AuPd at θ = 0.15, T = 300 K: the monomer fraction must be larger than the random monomer fraction, and the dimer fraction must be smaller than the random dimer fraction.
- For AuPt at θ = 0.15, T = 300 K: the monomer fraction must be smaller than the random monomer fraction, and the dimer fraction must also be smaller than the random dimer fraction.
- For AuPd at θ = 0.10, T = 300 K: the short‑range order parameter must satisfy α(1NN) < 0, α(2NN) > 0, and α(3NN) within ±0.05 of zero.
- The random baseline entries `random_monomer_fraction_theta015` and `random_dimer_fraction_theta015` must equal the exact analytical expressions (1−θ)^4 and 4θ(1−θ)^6 evaluated at θ = 0.15, within a tight tolerance.
- The field `AuPd_c2x2_alpha_1NN_theta05_T100` must be present in the output (enforced by the output contract); its value is not further constrained by the structural audit beyond the allowed range.

All submitted fractions must be between 0 and 1, and α values between −1 and 1. The verifier combines these checks into a single reward score in the range [0,1]; the main scored artifact carries the majority of the weight.