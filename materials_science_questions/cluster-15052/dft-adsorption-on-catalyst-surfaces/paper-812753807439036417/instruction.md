# DFT Study of NH₃ Adsorption and Decomposition on Mo₂C(001) Surface

## Problem background
Ammonia (NH₃) decomposition on transition metal carbides is a promising route for COₓ‑free hydrogen production and catalysis. Understanding the adsorption and sequential dissociation of NH₃ at the atomic level is critical for designing efficient catalysts. This task investigates the adsorption of NH₃ and its stepwise dehydrogenation on the metallic Mo₂C(001) surface. The goal is to determine the preferred binding sites, the energy barriers and reaction energies for each NH₃ dehydrogenation step, and the maximum surface coverage (saturation) achievable with NH₃ as the nitridation agent.

## Approach
The study uses periodic density functional theory (DFT) at the GGA‑PBE level with van der Waals dispersion correction (DFT‑D3). The core‑electron interaction is described by the projector‑augmented wave (PAW) method. The workflow proceeds as follows:

- Optimize the hexagonal bulk Mo₂C unit cell to obtain equilibrium lattice parameters.
- Build a six‑layer p(2×2) slab of the Mo₂C(001) surface; the bottom three layers are fixed in bulk positions while the top three are relaxed.
- Place single NH₃, NH₂, NH, and N adsorbates on all candidate surface sites (top, bridge, hollow) and relax the geometries to obtain adsorption energies and identify the most stable site for each species.
- Using the most stable configurations, locate transition states via the climbing‑image nudged elastic band (CI‑NEB) method for the three sequential decomposition steps: NH₃ → NH₂ + H, NH₂ + H → NH + 2H, NH + 2H → N + 3H. Zero‑point energy (ZPE) corrections are included.
- Determine saturation coverages by computing stepwise adsorption energies for increasing numbers of NHₓ (x = 3,2,1,0) on the surface, using gaseous NH₃ as the nitrogen source and H₂ desorption as the energy reference. The saturation coverage is the highest coverage for which the stepwise adsorption remains exothermic.

## Reproduction target
Compute the following quantities using the DFT protocol described:

1. Single‑adsorbate adsorption energies (eV) for NH₃, NH₂, NH, and N on Mo₂C(001) at their most stable surface sites, reported in `step_01_adsorption_energies.csv`.
2. Energy barriers (Eₐ) and reaction energies (ΔEᵣ) for the three sequential NH₃ dehydrogenation steps, including zero‑point energy correction, reported in `step_02_decomposition_barriers.csv`.
3. Saturation coverages (in monolayers, ML) of NH₃, NH₂, NH, and N on the surface when NH₃ is the sole nitrogen source, reported in `step_03_saturation_coverages.csv`.

The results should be obtained by the computational procedure described; they are not provided and must be derived from first‑principles calculations.

## Assets

- Open-source periodic DFT code with PAW and D3 support (e.g., Quantum ESPRESSO, ABINIT)
- PAW pseudopotential library for Mo, C, N, H
- Hexagonal Mo2C bulk crystal structure parameters

## Workflow steps

### Step 1: Bulk Mo2C optimization
- Role: process
- Action: Perform DFT geometry optimization of the hexagonal Mo2C unit cell (GGA-PBE + D3, PAW) to obtain accurate lattice parameters.
- Evidence: `/app/outputs/bulk_opt.log`

### Step 2: Slab model construction and relaxation
- Role: process
- Action: Build a periodic p(2×2) slab of Mo2C(001) from the optimized bulk, using six atomic layers. Fix the bottom three layers in bulk positions, relax the top three layers, and obtain the clean-surface total energy.
- Evidence: `/app/outputs/slab_relax.log`

### Step 3: Single-adsorbate adsorption energies
- Role: scored
- Action: Place a single NH3, NH2, NH, and N on all candidate surface sites (top t1/t2, bridge, hollow) of the relaxed slab; optimize geometry and compute adsorption energy E_ads = E(species/slab) − (E(species) + E(slab)). Report the most stable site and its adsorption energy for each species.
- Output file: `/app/outputs/step_01_adsorption_energies.csv`
- Format: csv
- Contract: species,site,E_ads(eV)
- Scoring: scored by hidden verifier

### Step 4: NH3 decomposition barriers and reaction energies
- Role: scored (load-bearing)
- Action: Using the most stable adsorbate configurations as initial and final states, locate the transition states (CI-NEB) for the three sequential steps: NH3* → NH2* + H*, NH2* + H* → NH* + 2H*, NH* + 2H* → N* + 3H*. Compute energy barriers E_a, reaction energies ΔE_r including zero-point energy correction.
- Output file: `/app/outputs/step_02_decomposition_barriers.csv`
- Format: csv
- Contract: step,E_a(eV),ΔE_r(eV),ZPE_included(bool)
- Scoring: scored by hidden verifier

### Step 5: Saturation coverages from NH3 nitridation
- Role: scored
- Action: For each NHx species (x=3,2,1,0), compute stepwise adsorption energies ΔE(NHx) = E[(NHx)n/slab] – E[(NHx)n-1/slab] – (E[NH3] – (3-x)/2 E[H2]) for increasing coverage n. Determine saturation coverage as the highest n for which the stepwise energy remains negative (or the coverage where it becomes positive), and express it in monolayers (ML).
- Output file: `/app/outputs/step_03_saturation_coverages.csv`
- Format: csv
- Contract: species,saturation_coverage_ML
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_adsorption_energies.csv`
- `/app/outputs/step_02_decomposition_barriers.csv`
- `/app/outputs/step_03_saturation_coverages.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_energies.csv
- path: `/app/outputs/step_01_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adsorption energies of single NH3, NH2, NH, N on Mo2C(001) at their most stable sites.
- schema:
  - `type`: table
  - `required_columns`: `species`, `site`, `E_ads(eV)`
  - `units`:
    - `E_ads(eV)`: eV

### step_02_decomposition_barriers.csv
- path: `/app/outputs/step_02_decomposition_barriers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Barriers and reaction energies (ZPE-corrected) for three NH3 decomposition steps.
- schema:
  - `type`: table
  - `required_columns`: `step`, `E_a(eV)`, `ΔE_r(eV)`, `ZPE_included(bool)`
  - `units`:
    - `E_a(eV)`: eV
    - `ΔE_r(eV)`: eV

### step_03_saturation_coverages.csv
- path: `/app/outputs/step_03_saturation_coverages.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Saturation coverages (in monolayers) of NH3, NH2, NH, N using NH3 as nitridation agent.
- schema:
  - `type`: table
  - `required_columns`: `species`, `saturation_coverage_ML`
  - `units`:
    - `saturation_coverage_ML`: ML

Notes: Scoring compares the reported values against paper-reported reference within absolute tolerances (±0.05 eV for energies, ±0.05 ML for coverages). A T3 structural check verifies that all three ΔE_r in step_02 are negative (full decomposition).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "site",
          "E_ads(eV)"
        ],
        "units": {
          "E_ads(eV)": "eV"
        }
      },
      "description": "Adsorption energies of single NH3, NH2, NH, N on Mo2C(001) at their most stable sites."
    },
    {
      "file": "step_02_decomposition_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "E_a(eV)",
          "ΔE_r(eV)",
          "ZPE_included(bool)"
        ],
        "units": {
          "E_a(eV)": "eV",
          "ΔE_r(eV)": "eV"
        }
      },
      "description": "Barriers and reaction energies (ZPE-corrected) for three NH3 decomposition steps."
    },
    {
      "file": "step_03_saturation_coverages.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "saturation_coverage_ML"
        ],
        "units": {
          "saturation_coverage_ML": "ML"
        }
      },
      "description": "Saturation coverages (in monolayers) of NH3, NH2, NH, N using NH3 as nitridation agent."
    }
  ],
  "notes": "Scoring compares the reported values against paper-reported reference within absolute tolerances (±0.05 eV for energies, ±0.05 ML for coverages). A T3 structural check verifies that all three ΔE_r in step_02 are negative (full decomposition)."
}
```

## How you are scored
After you finish, a hidden verifier will inspect your CSV artifacts under `/app/outputs`. The verifier compares your computed adsorption energies, barriers, reaction energies, and saturation coverages against reference values — not by matching a single known number, but by evaluating whether each quantity falls within a tolerance window derived from typical code‑to‑code variations for this level of theory. Zero‑point correction inclusion is also checked. The verifier further verifies structural properties (e.g., that all three decomposition reaction energies are negative). Each of the three scored steps contributes a portion of the final reward; the final score is the weighted combination of the individual stage scores. Simply writing the reference numbers without performing the calculations will not pass the verification.
