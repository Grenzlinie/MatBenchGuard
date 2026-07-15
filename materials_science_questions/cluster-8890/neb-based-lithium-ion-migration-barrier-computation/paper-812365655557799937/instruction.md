# Lithium Adsorption and Diffusion on Graphene Monoxide Monolayer: DFT Reproduction

## Problem background
Two-dimensional graphene monoxide (GmO) has been proposed as a potential anode material for lithium‑ion batteries. Unlike graphene, which does not bind lithium atoms, GmO contains periodically arranged oxygen atoms that could introduce strong covalent Li–O bonds. Understanding the thermodynamics of Li adsorption, the surface diffusion barriers, and the theoretical gravimetric capacity is essential to assess whether GmO is a viable high‑capacity, fast‑charging anode candidate.

## Approach
The reproduction uses plane‑wave density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional, as implemented in Quantum ESPRESSO, together with projector augmented‑wave pseudopotentials. The workflow begins with a variable‑cell relaxation of a pristine GmO monolayer unit cell to determine its equilibrium lattice parameters. A single Li atom is then placed at the hollow (H) adsorption site on a 4 × 4 supercell and the combined system is relaxed; the Li adsorption energy is computed from the total energies using the formation energy relative to bulk bcc lithium. For the fully lithiated structure (Li₂C₂O₂, where Li atoms occupy both sides of every hollow site), the formation energy per Li and the theoretical gravimetric capacity are derived after a variable‑cell relaxation. Surface diffusion is investigated by the nudged elastic band (NEB) method along the H–S–B–S–H path between adjacent hollow sites; the minimum‑energy pathway yields the migration barrier. All supercell calculations use a vacuum gap of 20 Å to minimise periodic‑image interactions.

## Reproduction target
Compute the following quantities from first‑principles DFT:
(1) The adsorption energy per Li atom at the hollow (H) site on a 4 × 4 GmO supercell, obtained from variable‑cell relaxation with a 20 Å vacuum gap.
(2) The energy barrier for Li surface diffusion between adjacent H‑sites along the H–S–B–S–H route, determined by nudged elastic band (NEB) calculations on the same 4 × 4 supercell with identical computational parameters.
(3) The formation energy per Li and the theoretical gravimetric capacity of the fully lithiated Li₂C₂O₂ structure (Li atoms placed on both sides of every hollow site), obtained after variable‑cell relaxation with a 20 Å vacuum gap.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- PSlibrary pseudopotentials (v1.0.0): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Relax pristine GmO monolayer unit cell
- Role: process
- Action: Perform DFT variable-cell relaxation of the GmO monolayer unit cell (initial lattice constant ~3.13 Å, opening angle ~130°) using Quantum ESPRESSO with PBE PAW pseudopotentials to obtain equilibrium lattice parameter a_lat, opening angle α, and relaxed atomic coordinates.
- Evidence: `/app/outputs/gmo_relaxed.json`

### Step 2: Single Li adsorption energy on GmO
- Role: scored (load-bearing)
- Action: Build a 4x4 supercell from the relaxed GmO unit cell, place one Li atom at the hollow (H) site, perform variable-cell relaxation (with 20 Å vacuum gap). Compute total energies for pristine GmO supercell, bulk bcc Li, and the GmO+Li system, then calculate the adsorption energy per Li, ΔE_Li, using the formation energy formula (ΔE_Li = (E_GmO+Li - (E_GmO + E_Li * N_Li)) / N_Li).
- Output file: `/app/outputs/single_li_adsorption.json`
- Format: json
- Contract: {"E_GmO": float (eV), "E_bcc_Li_per_atom": float (eV), "E_GmOplusLi": float (eV), "DeltaE_Li": float (eV)}
- Scoring: scored by hidden verifier

### Step 3: Li2C2O2 formation energy and capacity
- Role: scored
- Action: Construct the fully lithiated Li2C2O2 unit cell (Li on both sides of every hollow site) and perform variable-cell relaxation (with 20 Å vacuum gap). Compute total energies for the pristine GmO per formula unit, bulk bcc Li, and the Li2C2O2 system, then derive the formation energy per Li and the theoretical gravimetric capacity (mAh/g) using the formula: capacity = (x * e) / (y * (m_C + m_O)).
- Output file: `/app/outputs/li2c2o2_properties.json`
- Format: json
- Contract: {"E_GmO_per_formula": float (eV), "E_bcc_Li_per_atom": float (eV), "E_total_Li2C2O2": float (eV), "DeltaE_Li": float (eV), "capacity_mAh_per_g": float}
- Scoring: scored by hidden verifier

### Step 4: NEB surface migration barrier for Li
- Role: scored
- Action: Using the relaxed 4x4 GmO supercell with Li at the H-site, set up a nudged elastic band path between two adjacent H-sites traversing the H-S-B-S-H route. Run NEB calculations with the same computational parameters (PBE PAW, 4x4x1 k-points, 20 Å vacuum) and extract the energy barrier.
- Output file: `/app/outputs/neb_barrier.json`
- Format: json
- Contract: {"barrier_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_li_adsorption.json`
- `/app/outputs/li2c2o2_properties.json`
- `/app/outputs/neb_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_li_adsorption.json
- path: `/app/outputs/single_li_adsorption.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Adsorption energy of a single Li atom at the GmO H-site. DeltaE_Li should be negative; more negative is better. Contains supporting total energies.
- schema:
  - `type`: object
  - `required`:
    - `E_GmO`: number
    - `E_bcc_Li_per_atom`: number
    - `E_GmOplusLi`: number
    - `DeltaE_Li`: number

### li2c2o2_properties.json
- path: `/app/outputs/li2c2o2_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Formation energy per Li and theoretical capacity of the fully lithiated Li2C2O2 structure. Lower DeltaE_Li is better; higher capacity is better.
- schema:
  - `type`: object
  - `required`:
    - `E_GmO_per_formula`: number
    - `E_bcc_Li_per_atom`: number
    - `E_total_Li2C2O2`: number
    - `DeltaE_Li`: number
    - `capacity_mAh_per_g`: number

### neb_barrier.json
- path: `/app/outputs/neb_barrier.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: NEB energy barrier for Li surface diffusion between adjacent H-sites. Lower barrier is better.
- schema:
  - `type`: object
  - `required`:
    - `barrier_eV`: number

Notes: All scored artifacts are compared against hidden paper-reported gold values using threshold-or-better scoring. Exact tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_li_adsorption.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "E_GmO": "number",
          "E_bcc_Li_per_atom": "number",
          "E_GmOplusLi": "number",
          "DeltaE_Li": "number"
        }
      },
      "description": "Adsorption energy of a single Li atom at the GmO H-site. DeltaE_Li should be negative; more negative is better. Contains supporting total energies."
    },
    {
      "file": "li2c2o2_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "E_GmO_per_formula": "number",
          "E_bcc_Li_per_atom": "number",
          "E_total_Li2C2O2": "number",
          "DeltaE_Li": "number",
          "capacity_mAh_per_g": "number"
        }
      },
      "description": "Formation energy per Li and theoretical capacity of the fully lithiated Li2C2O2 structure. Lower DeltaE_Li is better; higher capacity is better."
    },
    {
      "file": "neb_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "barrier_eV": "number"
        }
      },
      "description": "NEB energy barrier for Li surface diffusion between adjacent H-sites. Lower barrier is better."
    }
  ],
  "notes": "All scored artifacts are compared against hidden paper-reported gold values using threshold-or-better scoring. Exact tolerances are hidden."
}
```

## How you are scored
A hidden verifier reads the JSON artifacts you write under `/app/outputs` and scores each artifact independently. For every scored step, the verifier compares your reported numeric value to a confidential expected result using a direction‑aware tolerance: more negative adsorption energy, lower diffusion barrier, and higher theoretical capacity are better, and full credit is awarded when your computed value meets or exceeds the expected performance within an allowed tolerance range. Partial credit is given proportionally for values that fall within the tolerance band. The verifier combines the step‑level scores into a single overall reward between 0.0 and 1.0. Because the verifier also inspects the total energies you must report, it can detect artifacts that are inconsistent with the proper computational protocol. You must therefore run the complete DFT workflow honestly; simply guessing or copying the original publication's reported numbers will not yield a high score.
