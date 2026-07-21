# Time-Dependent Monte Carlo Simulation of Catalytic Hydrogenation with Steric Hindrance and Metal Dispersion

## Problem background
The catalytic hydrogenation of 2,4‑dinitro‑toluene (2,4DNT) to 2,4‑diamino‑toluene (2,4DAT) over palladium‑on‑carbon (Pd/C) catalysts is an industrially important three‑phase reaction conducted in an ethanol solvent under hydrogen pressure. The reaction proceeds through a complex network of hydroxylamino and amino intermediates, and the resulting product distribution is known to depend on the morphology of the catalyst — in particular, on the metal dispersion (Dx), which reflects the fraction of palladium atoms exposed on the crystallite surface. Earlier modelling efforts using ordinary differential equation systems produced contradictory mechanistic interpretations and could not simultaneously account for the experimentally observed activity and selectivity trends at different dispersions and temperatures. A molecular‑level picture that resolves how different adsorption configurations of the reacting species, their mutual steric hindrance, and the fraction of accessible surface sites jointly shape the macroscopic catalytic behaviour is therefore needed. This task investigates the open relationship between metal dispersion, temperature, and the resulting catalyst relative activity, product selectivity, and turnover frequency in this system.

## Approach
The core of this task is a time‑dependent Monte Carlo (tdMC) simulation on a 100×100 square lattice representing a mixed ensemble of palladium surface sites. Each lattice site can be occupied by a surface species, left vacant, or blocked by an inert gap (a site permanently excluded from participating in any event).

Three adsorption configurations are distinguished for every toluene‑derived surface species, differing in the number of occupied sites and steric footprint:
- **FC (fat constellation)**: the aromatic ring lies parallel to the surface, occupying 12 sites.
- **HFC (hindered‑flag constellation)**: the ring is perpendicular to the surface with the nitrogen‑containing substituent oriented toward the surface in the ortho position; 4 sites occupied.
- **FFC (free‑flag constellation)**: the ring is perpendicular with the nitrogen‑containing substituent toward the surface in the para position; 3 sites occupied.

Metal dispersion Dx is simulated by randomly introducing gaps on the lattice in proportions matching the desired Dx value (0 ≤ Dx < 1), where Dx = 0 corresponds to a continuous metal surface with no gaps.

The chemical model includes nine toluene derivatives in the solution phase (2,4DNT; the hydroxylamino‑nitro isomers 4HA2NT and 2HA4NT; the amino‑nitro isomers 4A2NT and 2A4NT; 2,4‑dihydroxylamino‑toluene, 2,4DHAT; the hydroxylamino‑amino isomers 2HA4AT and 4HA2AT; and the final product 2,4DAT) and 27 surface species (each solution species in three adsorption configurations). Surface events comprise:
- **Adsorption**: a solution species attaches to a suitable vacant region of the lattice in one of the three configurations.
- **Desorption**: an adsorbed species leaves the surface.
- **Diffusion**: a surface species moves to a neighbouring vacant region.
- **Hydrogenation reactions**: on the surface, a –NO₂ group can be reduced to –NHOH, and an –NHOH group can be reduced to –NH₂.

Event occurrence probabilities are derived from activation energies (Ea) via transition‑state theory (TST), normalised by the number of sites the configuration occupies. The reference time step is calibrated against the diffusion‑limited hitting rate of solvated species in ethanol, yielding macroscopic rates per surface metal site per second.

The simulation uses the following set of averaged activation energies for surface events (the corresponding approximate occurrence probability per site per picosecond at 323.15 K follows from TST):
- Hydrogenation of surface –NO₂ (r‑NO₂): Ea ≈ 79 kJ mol⁻¹ (P ~ 7.8×10⁻¹³)
- Hydrogenation of surface –NHOH (r‑NHOH): Ea ≈ 76 kJ mol⁻¹ (P ~ 2.4×10⁻¹²)
- Desorption of flag species via –NO₂ (d‑NO₂): Ea ≈ 79 kJ mol⁻¹ (P ~ 1.1×10⁻¹²)
- Desorption of flag species via –NHOH (d‑NHOH): Ea ≈ 73 kJ mol⁻¹ (P ~ 1.0×10⁻¹¹)
- Desorption of flag species via –NH₂ (d‑NH₂): Ea ≈ 42 kJ mol⁻¹ (P ~ 1.0×10⁻⁶)
- Desorption of FC (fat) species via the aromatic ring (d‑Φ): Ea ≈ 79 kJ mol⁻¹ (P ~ 1.1×10⁻¹²)

When a solution molecule strikes the surface, the probabilities of forming FC, HFC, or FFC are 0.10, 0.45, and 0.45, respectively. The relative amount of 4HA2NT versus 2HA4NT in solution is governed by the parameter κ = 0.50, which multiplies the known 4A2NT / 2A4NT molar ratio.

The reaction is simulated under isothermal, isobaric conditions (H₂ pressure 1 atm) with the liquid phase initially containing 0.1 M 2,4DNT in ethanol. Starting from a fresh, clean catalyst surface at t = 0 s, the simulation tracks surface populations and computes macroscopic appearance and disappearance rates of each species. By varying Dx and temperature while keeping all other parameters fixed, the model predicts how catalyst relative activity, product selectivity, and turnover frequency respond to these variables.

## Reproduction target
Implement the tdMC algorithm as described above using the activation energies and occurrence probabilities provided. Because the algorithm is stochastic, employ suitable averaging (e.g. running multiple independent random seeds per condition) to obtain stable macroscopic rate estimates. Then run simulations under the following conditions and produce three tab‑separated output files:

1. At T = 323.15 K, run simulations for metal dispersion values Dx = 0.0, 0.3, 0.6, and 0.9. At t = 0 s (the fresh‑catalyst instant), compute the **catalyst relative activity (c.r.a.)** as the initial 2,4DNT disappearance rate per surface metal site, normalised by the rate obtained at Dx = 0. Write one row per Dx value to `catalyst_relative_activity_vs_dispersion.tsv` (columns: Dx, catalyst_relative_activity).

2. From the same or equivalent simulation runs at T = 323.15 K and the same Dx values, compute the **selectivity** to three product groups at t = 0 s: HANT (the combined 4HA2NT + 2HA4NT isomers), 4A2NT, and 2A4NT. Selectivity to a given product is its appearance rate at t = 0 divided by the sum of appearance rates of all products (HANT + 4A2NT + 2A4NT) at that instant. Write one row per Dx value to `selectivity_vs_dispersion.tsv` (columns: Dx, selectivity_HANT, selectivity_4A2NT, selectivity_2A4NT).

3. At fixed Dx = 0.3, run simulations at three temperatures (e.g. 313.15 K, 323.15 K, 333.15 K). At t = 0 s, record the **turnover frequency (TOF)** of 2,4DNT disappearance per surface metal site (units of s⁻¹). Write one row per temperature to `arrhenius_data.tsv` (columns: temperature_K, TOF_2_4DNT).

All output files must be placed under `/app/outputs/` and follow the column schemas and formats declared in the individual workflow steps below.

## Assets
This is a compute‑driven task; no external datasets, pre‑trained models, or data files need to be fetched. All simulation parameters — the activation energies (or occurrence probabilities), the hitting configuration probabilities (FC=0.10, HFC=0.45, FFC=0.45), the parameter κ=0.50, the lattice size (100×100), the solution composition (0.1 M 2,4DNT in ethanol), the H₂ pressure (1 atm), and the reaction network — are specified in the Approach section above and in the workflow steps. You may implement the tdMC algorithm in any programming language. Standard numerical and scientific computing libraries for random number generation, array operations, and (optionally) linear regression are sufficient; no specialised simulation package is required.

## Workflow steps

### Step 1: Implement the time‑dependent Monte Carlo algorithm
- Role: process
- Action: Implement the tdMC algorithm for a 100×100 square lattice with three adsorption constellations (FC, HFC, FFC), the 9‑species solution network, 27 surface species, steric‑blocking rules, random‑gap generation for metal dispersion Dx, and event probabilities calculated from the paper’s Table 2 via transition‑state theory. The algorithm must simulate adsorption, desorption, diffusion, and reaction events and produce time‑resolved surface population snapshots as well as macroscopic rates.
- Evidence: none

### Step 2: Simulate at varied Dx and compute catalyst relative activity
- Role: scored (load-bearing)
- Action: Using the tdMC algorithm with the best‑fit activation energies and occurrence probabilities from Table 2 of the paper, run simulations for Dx = 0.0, 0.3, 0.6, 0.9 at T = 323.15 K. At t = 0 s (fresh‑catalyst limit), compute the catalyst relative activity (c.r.a.) as the initial 2,4‑DNT disappearance rate per surface metal site, normalised to the Dx = 0 value. Write the results to a tab‑separated file.
- Output file: `/app/outputs/catalyst_relative_activity_vs_dispersion.tsv`
- Format: tsv
- Contract: columns: Dx (real, 0.0–0.9), catalyst_relative_activity (dimensionless). One row per simulated Dx value.
- Scoring: scored by hidden verifier

### Step 3: Simulate at varied Dx and compute selectivity
- Role: scored
- Action: Using the same simulation runs (or comparable fresh runs) at T = 323.15 K, compute at t = 0 s the selectivity to HANT, 4A2NT, and 2A4NT, defined as the appearance rate of each species divided by the sum of appearance rates of all products at that instant. Write the results to a tab‑separated file.
- Output file: `/app/outputs/selectivity_vs_dispersion.tsv`
- Format: tsv
- Contract: columns: Dx (real), selectivity_HANT (real), selectivity_4A2NT (real), selectivity_2A4NT (real). One row per Dx value.
- Scoring: scored by hidden verifier

### Step 4: Simulate at varied temperatures and extract Arrhenius data
- Role: scored
- Action: Run the tdMC algorithm with Dx = 0.3 and the Table 2 parameters at three temperatures (e.g., 313.15 K, 323.15 K, 333.15 K). At t = 0 s, record the turnover frequency (TOF) of 2,4‑DNT disappearance per surface metal site (s⁻¹). Write the results to a tab‑separated file.
- Output file: `/app/outputs/arrhenius_data.tsv`
- Format: tsv
- Contract: columns: temperature_K (real), TOF_2_4DNT (real, s⁻¹ per site). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/catalyst_relative_activity_vs_dispersion.tsv`
- `/app/outputs/selectivity_vs_dispersion.tsv`
- `/app/outputs/arrhenius_data.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### catalyst_relative_activity_vs_dispersion.tsv
- path: `/app/outputs/catalyst_relative_activity_vs_dispersion.tsv`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Catalyst relative activity (c.r.a.) vs metal dispersion Dx at 323.15 K, t=0 s.
- schema:
  - `type`: table
  - `required_columns`: `Dx`, `catalyst_relative_activity`

### selectivity_vs_dispersion.tsv
- path: `/app/outputs/selectivity_vs_dispersion.tsv`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Selectivity to HANT, 4A2NT, 2A4NT at t=0 s vs Dx.
- schema:
  - `type`: table
  - `required_columns`: `Dx`, `selectivity_HANT`, `selectivity_4A2NT`, `selectivity_2A4NT`

### arrhenius_data.tsv
- path: `/app/outputs/arrhenius_data.tsv`
- format: tsv
- purpose: scored
- target_policy: metric_recompute
- description: TOF of 2,4‑DNT disappearance at t=0 s for Dx=0.3 at three temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `TOF_2_4DNT`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "catalyst_relative_activity_vs_dispersion.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Dx",
          "catalyst_relative_activity"
        ]
      },
      "description": "Catalyst relative activity (c.r.a.) vs metal dispersion Dx at 323.15 K, t=0 s."
    },
    {
      "file": "selectivity_vs_dispersion.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Dx",
          "selectivity_HANT",
          "selectivity_4A2NT",
          "selectivity_2A4NT"
        ]
      },
      "description": "Selectivity to HANT, 4A2NT, 2A4NT at t=0 s vs Dx."
    },
    {
      "file": "arrhenius_data.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "TOF_2_4DNT"
        ]
      },
      "description": "TOF of 2,4‑DNT disappearance at t=0 s for Dx=0.3 at three temperatures."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier separately inspects and scores each of the three output files.

For `catalyst_relative_activity_vs_dispersion.tsv`, the verifier checks whether the reported catalyst relative activity values follow the expected trend as Dx increases (specifically, whether they are monotonic in Dx).

For `selectivity_vs_dispersion.tsv`, the verifier checks whether one of the three selectivities is monotonic in Dx and whether the ordering among the three selectivity values at each Dx conforms to the pattern characteristic of this reaction system.

For `arrhenius_data.tsv`, the verifier performs a linear regression of ln(TOF_2_4DNT) against 1/T (in K⁻¹), extracts an apparent activation energy from the slope, and verifies that this activation energy falls within a physically plausible range for this catalytic hydrogenation. The verifier also checks that the TOF magnitudes themselves are of a reasonable order.

Each file is scored independently, and the three scores are combined by weight to produce the final reward. Reporting values that violate the required structural relationships (e.g. non‑monotonic behaviour, an incorrect ordering, or an extracted activation energy far outside the expected range) will result in a low or zero score.
