# Monte Carlo Simulation of TMAO Hydration Structure and Dipole Alignment

## Problem background
Trimethylamine N-oxide (TMAO) is a highly polarized polyhedral osmolyte that stabilizes proteins, but the molecular details of its hydration structure—especially around the methyl groups—have been controversial. Canonical Monte Carlo simulations can map the three-dimensional distribution and average alignment of surrounding water molecules, providing quantitative signatures of TMAO's influence. Key open questions are: how many water molecules occupy the first hydration shell, how they partition between the oxide and methyl regions, and what is the sign of the average dipole orientation parameter D in each region (i.e., whether water dipoles point toward or away from TMAO).

## Approach
We simulate a single rigid TMAO molecule fixed at the origin, solvated by 500 TIP3P water molecules in a spherical droplet of radius 15.3 Å at 300 K and a density of 1 g cm⁻³. The atomic partial charges (NPA) and Lennard‑Jones parameters for TMAO are provided. A canonical Metropolis–Hastings Monte Carlo algorithm generates configurations. After a long equilibration, production configurations are sampled; every time all water molecules have been moved, the oxygen coordinates and dipole moment vectors are recorded. From these trajectories, one computes the number density of water oxygens as a function of distance from the TMAO nitrogen. The first hydration shell is defined by oxygen atoms within 6 Å of the nitrogen. Within that shell, the oxide region is defined by oxygens within 3.5 Å of the TMAO oxygen, and the methyl region by oxygens within 3.5 Å of any TMAO carbon. The average dipole orientation parameter D measures the alignment of water dipoles relative to the radial direction; its sign indicates whether the dipoles point towards (positive) or away from (negative) TMAO.

## Reproduction target
Run the NVT Monte Carlo simulation as described above. From the production trajectory, analyze the water oxygen positions and dipole moments to compute the following and write them to `/app/outputs/results.json`:
- `total_hydration_number`: the average number of water oxygen atoms within 6.0 Å of the TMAO nitrogen.
- `oxide_region_count`: the average number of water oxygen atoms within 3.5 Å of the TMAO oxygen.
- `methyl_region_count`: the average number of water oxygen atoms within 3.5 Å of any TMAO carbon.
- `oxide_D_sign`: a string, either `"positive"` or `"negative"`, indicating the sign of the average dipole orientation parameter D in the oxide region.
- `methyl_D_sign`: a string, either `"positive"` or `"negative"`, indicating the sign of D in the methyl region.

## Assets

- TIP3P water model: 10.1063/1.445869
- TMAO NPA charges and Lennard-Jones parameters

## Workflow steps

### Step 1: Run NVT Monte Carlo simulation
- Role: process
- Action: Set up a system with one rigid TMAO molecule (fixed at origin, N–O bond along z, one N–C bond in xz plane) and 500 TIP3P water molecules randomly placed in a sphere of radius 15.3 Å. Perform a canonical Metropolis–Hastings simulation at 300 K with the provided TMAO charges and LJ parameters. Run a long equilibration followed by a long production run, recording oxygen coordinates and dipole moment vectors of all water molecules whenever every molecule has moved.
- Evidence: `/app/outputs/mc_trajectory.log`

### Step 2: Compute hydration numbers and D sign
- Role: scored (load-bearing)
- Action: From the recorded water molecule positions and dipole moments, compute the following and write them to results.json: total_hydration_number (number of water oxygen atoms within 6.0 Å of TMAO nitrogen), oxide_region_count (oxygen atoms within 3.5 Å of TMAO oxygen), methyl_region_count (oxygen atoms within 3.5 Å of any TMAO carbon), oxide_D_sign and methyl_D_sign (sign of the average dipole orientation parameter D in the oxide and methyl regions, 'positive' or 'negative'). Use a spatial bin size comparable to the paper’s analysis and average over the production simulation.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"total_hydration_number": float, "oxide_region_count": float, "methyl_region_count": float, "oxide_D_sign": string, "methyl_D_sign": string}
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
- target_policy: threshold_or_better
- description: Hydration numbers and dipole orientation signs around TMAO. Counts are checked within a tolerance band; D signs are checked for exact match against expected strings.
- schema:
  - `type`: object
  - `required`: `total_hydration_number`, `oxide_region_count`, `methyl_region_count`, `oxide_D_sign`, `methyl_D_sign`
  - `properties`:
    - `total_hydration_number`:
      - `type`: number
    - `oxide_region_count`:
      - `type`: number
    - `methyl_region_count`:
      - `type`: number
    - `oxide_D_sign`:
      - `type`: string
      - `enum`: `positive`, `negative`
    - `methyl_D_sign`:
      - `type`: string
      - `enum`: `positive`, `negative`

Notes: The hydration numbers are compared to hidden paper reference values using a threshold_or_better policy (value within tolerance band accepted). D signs are checked with exact_match.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "total_hydration_number",
          "oxide_region_count",
          "methyl_region_count",
          "oxide_D_sign",
          "methyl_D_sign"
        ],
        "properties": {
          "total_hydration_number": {
            "type": "number"
          },
          "oxide_region_count": {
            "type": "number"
          },
          "methyl_region_count": {
            "type": "number"
          },
          "oxide_D_sign": {
            "type": "string",
            "enum": [
              "positive",
              "negative"
            ]
          },
          "methyl_D_sign": {
            "type": "string",
            "enum": [
              "positive",
              "negative"
            ]
          }
        }
      },
      "description": "Hydration numbers and dipole orientation signs around TMAO. Counts are checked within a tolerance band; D signs are checked for exact match against expected strings."
    }
  ],
  "notes": "The hydration numbers are compared to hidden paper reference values using a threshold_or_better policy (value within tolerance band accepted). D signs are checked with exact_match."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results.json` and independently evaluates each reported quantity. The three hydration counts (`total_hydration_number`, `oxide_region_count`, `methyl_region_count`) are compared to reference values using tolerance bands with a threshold‑or‑better policy: meeting or exceeding the hidden expected range earns full credit, and credit degrades for results that deviate too far. The two dipole orientation signs (`oxide_D_sign`, `methyl_D_sign`) are checked by exact match against the expected strings. The final reward is a weighted combination of these checks, emphasizing the hydration counts. The simulation must be executed honestly; simply reporting a target value without running the full MC workflow will not satisfy the procedural verification.
