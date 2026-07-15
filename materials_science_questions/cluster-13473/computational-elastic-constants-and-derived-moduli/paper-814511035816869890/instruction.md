# Elastic Properties of Hard Sphere Crystals with Orthogonal Nanochannel Inclusions

## Problem background
Negative Poisson's ratio (auxetic) materials exhibit the counter‑intuitive property of expanding transversely when stretched. Understanding how structural modifications like nano‑scale inclusions alter the elastic response of crystalline solids is crucial for designing materials with tailored auxeticity. In this task, we study a model system of face‑centered cubic (f.c.c.) hard sphere crystals containing a periodic array of three mutually orthogonal nanochannels. The channels are filled with hard spheres of a possibly different diameter, creating an inclusion. The goal is to investigate, by Monte Carlo simulation, how the layout of the channels (whether they cross or remain separate), the channel diameter, and the ratio of inclusion‑ to‑matrix sphere diameters affect the effective elastic symmetry, Poisson’s ratios in the main crystallographic directions, and the overall isotropy of the material.

## Approach
The elastic properties are computed from isothermal‑isobaric (NpT) Monte Carlo simulations that allow the shape of the simulation box to fluctuate (Parrinello–Rahman method). For each combination of channel type (D‑type with diameter 2σ, S‑type with diameter 2√2σ), channel layout (crossing, separate), and inclusion‑to‑matrix sphere diameter ratio σ’/σ (from 1.0 to 1.1 in steps of 0.025), a periodic f.c.c. supercell of N=864 hard spheres is constructed. All simulations are performed at a single reduced pressure p*=250. From the recorded trajectories of the symmetric box matrix h, one first computes the equilibrium reference box h_p and the Lagrangian strain tensor. The full elastic compliance matrix S (Voigt notation) is obtained from strain fluctuations, and the stiffness matrix B is obtained by inversion. Finally, the Poisson’s ratios for loading along [100], [110] and [111] are calculated from B using the standard formulas for cubic elasticity; the global minimum and maximum Poisson’s ratio are estimated by sampling many loading directions; and a relative isotropy criterion is evaluated. The workflow tests whether the effective elastic symmetry remains cubic (S11=S22=S33, S44=S55=S66, S12=S13=S23, other S elements zero) and how the inclusion parameters modulate the Poisson’s ratios and anisotropy.

## Reproduction target
Re‑compute the elastic compliance and stiffness matrices for all 20 systems (2 channel sizes × 2 layouts × 5 inclusion ratios). For each system, verify whether the compliance matrix satisfies the cubic symmetry relations. Using the stiffness matrix elements, compute the Poisson’s ratios for the [100], [110] (with measurement directions [1‑10] and [001]), and [111] crystallographic directions, as well as the global minimum and maximum Poisson’s ratio and the relative isotropy parameter. The central empirical question is to determine, from these simulation results, the conditions (inclusion layout, channel type, inclusion sphere size) under which the minimum Poisson’s ratio becomes non‑negative (i.e., auxeticity is removed), and to characterize how the elastic anisotropy changes.

## Assets

- Open‑source Monte Carlo simulation package supporting hard‑sphere interactions and Parrinello–Rahman box fluctuations (e.g., HOOMD‑blue hpmc): https://hoomd-blue.readthedocs.io

## Workflow steps

### Step 1: Generate initial supercell configurations
- Role: process
- Action: For each combination of channel type (D, S), layout (crossing, separate), and inclusion diameter ratio σ′/σ from 1.0 to 1.1 (step 0.025), build an f.c.c. supercell of N=864 particles with periodic boundaries. Assign matrix spheres diameter σ and inclusion spheres diameter σ′. Place nanochannels according to the described orthogonal layouts. Write the initial particle positions, types, sizes, and box vectors.
- Evidence: `/app/outputs/config_summary.txt`

### Step 2: Run Monte Carlo NpT simulations
- Role: process
- Action: For each generated system, perform isobaric‑isothermal Monte Carlo simulations at reduced pressure p*=250 using the Parrinello–Rahman method to sample box matrix fluctuations. Save the trajectory of the symmetric box matrix h at regular intervals using appropriate equilibration and production cycles.
- Evidence: `/app/outputs/run_log.txt`

### Step 3: Compute elastic compliance and stiffness matrices
- Role: scored (load-bearing)
- Action: From each saved box matrix trajectory, compute the equilibrium reference box matrix h_p, the volume V_p, and the Lagrangian strain tensor using the standard strain–box relation. Then calculate the full elastic compliance tensor (Voigt matrix S) via strain fluctuations and obtain the stiffness matrix B by matrix inversion. For each system, output the independent S and B elements, the maximum absolute off‑diagonal element outside the cubic set, and a Boolean indicating whether the matrix satisfies cubic symmetry relations to within a tolerance.
- Output file: `/app/outputs/s_matrix_results.json`
- Format: json
- Contract: {"type":"object","required":["results"],"items":{"required":["system","S11","S22","S33","S44","S55","S66","S12","S13","S23","other_S_max_abs","B11","B12","B44","cubic_symmetry_satisfied"]}}
- Scoring: scored by hidden verifier

### Step 4: Compute Poisson's ratios and anisotropy
- Role: scored
- Action: Using the elastic stiffness constants B11, B12, B44 from the previous step, compute the Poisson's ratio for loading in [100], [110] (both [1-10] and [001] measurement directions), and [111] crystallographic directions using the standard formulas for cubic symmetry. Determine the global minimum and maximum Poisson's ratio by sampling many loading and measurement directions. Compute the relative isotropy criterion B44 / (0.5*(B11-B12)).
- Output file: `/app/outputs/pr_results.json`
- Format: json
- Contract: {"type":"object","required":["results"],"items":{"required":["system","PR_100","PR_110_1m10","PR_110_001","PR_111","PR_min","PR_max","isotropy_ratio"]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/s_matrix_results.json`
- `/app/outputs/pr_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### s_matrix_results.json
- path: `/app/outputs/s_matrix_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Elastic compliance and stiffness matrix elements and cubic symmetry flag for each simulated system.
- schema:
  - `type`: object
  - `required`:
    - `results`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `S11`, `S22`, `S33`, `S44`, `S55`, `S66`, `S12`, `S13`, `S23`, `other_S_max_abs`, `B11`, `B12`, `B44`, `cubic_symmetry_satisfied`

### pr_results.json
- path: `/app/outputs/pr_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Directional and extreme Poisson's ratios and isotropy ratio for each system, used to verify removal of auxetic properties and anisotropy trends.
- schema:
  - `type`: object
  - `required`:
    - `results`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `PR_100`, `PR_110_1m10`, `PR_110_001`, `PR_111`, `PR_min`, `PR_max`, `isotropy_ratio`

Notes: The checker validates cubic symmetry of the reported compliance matrices and checks internal consistency between the reported Poisson's ratios and the stiffness matrix elements. The auxeticity condition (PR_min ≥ 0 for separate‑channel systems) is verified against expected behaviour.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "s_matrix_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "results": "array"
        },
        "items": {
          "type": "object",
          "required": [
            "system",
            "S11",
            "S22",
            "S33",
            "S44",
            "S55",
            "S66",
            "S12",
            "S13",
            "S23",
            "other_S_max_abs",
            "B11",
            "B12",
            "B44",
            "cubic_symmetry_satisfied"
          ]
        }
      },
      "description": "Elastic compliance and stiffness matrix elements and cubic symmetry flag for each simulated system."
    },
    {
      "file": "pr_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "results": "array"
        },
        "items": {
          "type": "object",
          "required": [
            "system",
            "PR_100",
            "PR_110_1m10",
            "PR_110_001",
            "PR_111",
            "PR_min",
            "PR_max",
            "isotropy_ratio"
          ]
        }
      },
      "description": "Directional and extreme Poisson's ratios and isotropy ratio for each system, used to verify removal of auxetic properties and anisotropy trends."
    }
  ],
  "notes": "The checker validates cubic symmetry of the reported compliance matrices and checks internal consistency between the reported Poisson's ratios and the stiffness matrix elements. The auxeticity condition (PR_min ≥ 0 for separate‑channel systems) is verified against expected behaviour."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts you write to /app/outputs. For the elastic matrices (s_matrix_results.json) the verifier checks the cubic symmetry equalities on the compliance elements and, for each system, recomputes the directional Poisson’s ratios from the stiffness constants B11, B12, B44 you provided. Those recomputed values are compared against your reported PR_100, PR_110_1m10, PR_110_001 and PR_111. This cross‑check ensures internal consistency. For the auxeticity question, the verifier evaluates the minimum Poisson’s ratio you obtained against the known physical behavior derived from the published study (e.g., whether, for a given layout and inclusion size, the material is expected to be auxetic or non‑auxetic). The isotropy ratio is compared qualitatively to the trend reported in the literature. Each stage carries a pre‑defined weight, and the final reward is a weighted sum of the scores from the matrix symmetry check, the Poisson’s ratio consistency check, and the auxeticity/anisotropy comparison. Your solution is judged on the correctness of the computed physical quantities, not on replicating exact table values from any publication.
