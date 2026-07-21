# Kinetic Monte Carlo Simulation of Hg Incorporation Site Selectivity in HgCdTe MBE Growth

## Problem background
In molecular-beam epitaxy (MBE) of HgCdTe, the large difference in Hg–Te and Cd–Te bond strengths forces growth conditions where Hg incorporation is very small and primarily controlled by Te₂ overpressure and the density of kink sites on the growing surface. Understanding the atomistic mechanism—whether Hg atoms incorporate predominantly at high-coordination kink/step sites versus low-coordination terrace sites—is critical for controlling composition uniformity in HgCdTe heterostructures and superlattices. This work uses a simple thermodynamic model to quantify the site selectivity of Hg incorporation. The aim is to compute the Hg occupation probability for different surface bonding configurations and to evaluate how strongly it depends on the site type, in particular to compare the probabilities at kink/step sites to those at terrace sites.

## Approach
We use a hybrid approach: the growth of CdTe (100) would be simulated explicitly via kinetic Monte Carlo (KMC) using Cd migration and evaporation rates, but the Hg incorporation is treated through a thermodynamic occupation probability that depends on the binding energy of each surface site. For scoring, only the thermodynamic computation is required.

The surface sites are classified by (α,β), where α is the number of nearest-neighbor bonds and β the number of second-neighbor bonds on the (100) surface. Representative site types are the terrace site (2,4) and the kink/step configurations (2,6) and (2,7). For a given site with total binding energy E_tot, the steady-state Hg occupation probability is given by

P_Hg(E_tot) = J_Hg / R_v(E_tot),

where J_Hg is the incident Hg flux per surface site and R_v(E_tot) is the site-dependent Hg evaporation rate.

**Required input rates** (to be used in the simulations):

*Hg evaporation rates at 450 K (R_v in atoms/s):*
- (2,4): 1.8 × 10^4
- (2,6): 7.62 × 10^2
- (2,7): 1.5 × 10^2

*Hg flux:*  The total incident Hg flux is J_Hg_total = 1 × 10^5 atoms/s. The simulation surface is a 30×30 array of adsorption sites (N_sites = 900). The per‑site flux used in the probability formula is therefore J_Hg = J_Hg_total / N_sites ≈ 111.111 atoms/s per site.

*Cd migration (R_d, hops/s) and evaporation (R_e, atoms/s) rates at 450 K (for reference, not required for the scored computation):*
- (2,4):  R_e = 6 × 10^{-3},  R_d = 312
- (2,5):  R_e = 4.2 × 10^{-4},  R_d = 21
- (2,6):  R_e = 2.9 × 10^{-3},  R_d = 1.5
- (2,7):  R_e = 2 × 10^{-6},  R_d = 0.1

The CdTe simulation would run with a Cd flux of 1 monolayer per second (ML/s) and evolve the surface bonding configurations; however, for this task only the Hg incorporation probabilities and their ratios need to be computed directly from the Hg evaporation rates and the per‑site flux.

## Reproduction target
Compute the Hg occupation probabilities P_Hg for the (2,4), (2,6), and (2,7) site types using the provided Hg evaporation rates and the per‑site flux J_Hg = J_Hg_total / 900. Then calculate the ratios:

- ratio_26_24 = P_Hg(2,6) / P_Hg(2,4)
- ratio_27_24 = P_Hg(2,7) / P_Hg(2,4)

Write the results to `/app/outputs/incorporation_ratios.json` as a JSON object with keys:
`p_Hg_24`, `p_Hg_26`, `p_Hg_27`, `ratio_26_24`, `ratio_27_24`.

## Assets

- Python 3 with numpy and random: standard library; install via apt or pip

## Workflow steps

### Step 1: (Optional) Kinetic Monte Carlo simulation of CdTe growth
- Role: informational (not scored)
- Action: Optionally run a kinetic Monte Carlo simulation of CdTe (100) growth at 450 K with a Cd flux of 1 ML/s, using the Cd migration and evaporation rates listed above, to evolve the surface bonding configurations. This step is not required for the scored output.

### Step 2: Compute site‑specific Hg incorporation probabilities and enhancement ratios
- Role: scored (load-bearing)
- Action: Using the provided Hg evaporation rates at 450 K and the per‑site Hg flux J_Hg = J_Hg_total / 900, compute the occupation probability P_Hg for the (2,4), (2,6), and (2,7) site types via P_Hg = J_Hg / R_v(E_tot). Then calculate the ratios P_Hg(2,6)/P_Hg(2,4) and P_Hg(2,7)/P_Hg(2,4). Write the results as a JSON file with keys p_Hg_24, p_Hg_26, p_Hg_27, ratio_26_24, ratio_27_24.
- Output file: `/app/outputs/incorporation_ratios.json`
- Format: json
- Contract: {"p_Hg_24": <float>, "p_Hg_26": <float>, "p_Hg_27": <float>, "ratio_26_24": <float>, "ratio_27_24": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/incorporation_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### incorporation_ratios.json
- path: `/app/outputs/incorporation_ratios.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file with site-specific Hg incorporation probabilities and the enhancement ratios at kink/step sites relative to terrace sites.
- schema:
  - `type`: object
  - `required`: `p_Hg_24`, `p_Hg_26`, `p_Hg_27`, `ratio_26_24`, `ratio_27_24`
  - `properties`:
    - `p_Hg_24`:
      - `description`: Hg occupation probability at the terrace (2,4) site
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `p_Hg_26`:
      - `description`: Hg occupation probability at the kink/step (2,6) site
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `p_Hg_27`:
      - `description`: Hg occupation probability at the kink/step (2,7) site
      - `type`: number
      - `minimum`: 0
      - `maximum`: 1
    - `ratio_26_24`:
      - `description`: Ratio P_Hg(2,6) / P_Hg(2,4)
      - `type`: number
      - `minimum`: 0
    - `ratio_27_24`:
      - `description`: Ratio P_Hg(2,7) / P_Hg(2,4)
      - `type`: number
      - `minimum`: 0

Notes: The kinetic Monte Carlo simulation step (step_01) is included for workflow completeness but is not required to obtain the scored ratios; those can be computed directly from the published evaporation rates. The step_02 artifact is the scored target.

## How you are scored
A hidden verifier will read your `/app/outputs/incorporation_ratios.json` and compare the reported probabilities and ratios to a hidden reference. It will also check that the occupation probabilities satisfy certain expected structural relations (e.g., ordering among site types) that a correct simulation should exhibit. Your final reward is based on the correctness of the ratios and the structural checks. The computation must follow the described approach using the given per‑site flux and evaporation rates.