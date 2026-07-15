## Problem background

Rechargeable lithium-ion and sodium-ion batteries require anode materials with high capacity and fast rate capability. Two-dimensional (2D) materials with large surface area and potentially fast ion diffusion are promising candidates. This task investigates a hexagonal Ti2B2 monolayer, a predicted stable 2D transition metal boride, as an anode material for both Li-ion and Na-ion batteries. The goal is to compute its theoretical specific capacity, average open-circuit voltage, and ion diffusion barriers using first-principles methods, which together determine its suitability as a battery electrode.

## Approach

The reproduction follows a computational workflow based on density functional theory (DFT). First, the hexagonal Ti2B2 monolayer unit cell (space group P6/mmm) – consisting of a central honeycomb boron layer sandwiched between two hexagonal planes of Ti atoms – is structurally optimized to obtain the equilibrium lattice constant and atomic positions. Secondly, the bulk phases of Li and Na (bcc) are optimized to extract the total energy per atom, which serves as the chemical potential reference for adsorption calculations.

With the optimized monolayer and bulk metal energies in hand, the agent builds a 2×2 supercell and determines the maximum stable coverage of Li and Na adatoms by iteratively adding atomic layers on both sides of the monolayer. For each coverage level, the average adsorption energy is computed; a stable configuration requires negative (favorable) average adsorption energies. From the saturated metal-loaded configurations, the theoretical specific capacity (in mAh/g) and the average open-circuit voltage (in eV) are calculated using standard electrochemical formulas that relate the energy of the lithiated/sodiated monolayer, the energy of the bare monolayer, and the bulk metal energy per atom, together with Faraday's constant.

Ion diffusion barriers are obtained with the climbing-image nudged elastic band (CI-NEB) method. A single Li (respectively Na) atom is placed on the most favorable adsorption site (S1, above the center of a hexagon) and a minimum energy path connecting adjacent S1 sites via a bridging S3 site is constructed. The energy profile along this S1–S3–S1 path yields the diffusion barrier. Both Li and Na barriers are computed in this way.

## Reproduction target

Produce the following six numeric properties for the hexagonal Ti2B2 monolayer:
- Theoretical specific capacity for Li (in mAh/g)
- Average open-circuit voltage for Li (in eV)
- Li-ion diffusion barrier (in eV)
- Theoretical specific capacity for Na (in mAh/g)
- Average open-circuit voltage for Na (in eV)
- Na-ion diffusion barrier (in eV)
The results must be based on DFT calculations as described; the final values will be written to a JSON file and independently scored by a hidden verifier against reference thresholds.

## Assets

The following open-source tools and resources are required. The solving agent must obtain them at runtime.

- **Quantum ESPRESSO** – plane-wave DFT code (open-source alternative to VASP).  
  Access: https://www.quantum-espresso.org/
- **ASE (Atomic Simulation Environment)** – Python library for building structures, managing DFT calculations, and running workflows.  
  Access: https://wiki.fysik.dtu.dk/ase/
- **SSSP pseudopotentials (efficiency set)** – standard solid-state pseudopotentials for accurate DFT with Quantum ESPRESSO.  
  Access: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Optimize Ti2B2 monolayer structure
- Role: process
- Action: Construct the hexagonal Ti2B2 monolayer unit cell (space group P6/mmm) with a central honeycomb boron layer and outer hexagonal Ti layers. Perform a DFT variable-cell relaxation to optimize the lattice constant and atomic positions.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Compute bulk Li and Na total energies
- Role: process
- Action: Optimize the ground-state structures of bulk bcc Li and bulk bcc Na using DFT and extract the total energy per atom. These energies serve as the anode reaction reference.
- Evidence: `/app/outputs/bulk_energies.json`

### Step 3: Compute anode properties: capacity, voltage, and diffusion barriers
- Role: scored (load-bearing)
- Action: Using the optimized Ti2B2 monolayer (Step 1) and bulk metal energies (Step 2), build a 2×2 supercell. Determine the maximum stable Li and Na coverage by iteratively adding adatom layers on both sides and computing average adsorption energies. From the stable saturated configurations, compute the theoretical specific capacity (mAh/g) and average open-circuit voltage (eV) using the standard electrochemical formulas. For diffusion barriers, place a single Li (resp. Na) atom on the S1 site and perform CI-NEB along the S1–S3–S1 pathway; extract the energy barrier. Collect all six quantities into a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: `Li_diffusion_barrier` (eV, number), `Na_diffusion_barrier` (eV, number), `Li_capacity` (mAh/g, number), `Na_capacity` (mAh/g, number), `Li_open_circuit_voltage` (eV, number), `Na_open_circuit_voltage` (eV, number). All values are numbers.
- Scoring: scored by hidden verifier

## Output files

The following files must be placed under `/app/outputs`:
- `relaxed_structure.cif` – optimized Ti2B2 monolayer structure
- `bulk_energies.json` – bulk Li and Na total energies per atom
- `results.json` – final scored results (six numeric properties)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Final scored battery performance results. Each field is compared directionally: lower diffusion barriers and higher capacities are better; voltages are compared within a tolerance. Better-than-reference values earn full credit.
- schema:
  - `type`: object
  - `required`:
    - `Li_diffusion_barrier`: number (eV)
    - `Na_diffusion_barrier`: number (eV)
    - `Li_capacity`: number (mAh/g)
    - `Na_capacity`: number (mAh/g)
    - `Li_open_circuit_voltage`: number (eV)
    - `Na_open_circuit_voltage`: number (eV)

Notes: Only results.json is scored. The process-step evidence files (relaxed_structure.cif and bulk_energies.json) are not scored but their presence is checked to ensure the workflow was executed.

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
        "required": {
          "Li_diffusion_barrier": "number (eV)",
          "Na_diffusion_barrier": "number (eV)",
          "Li_capacity": "number (mAh/g)",
          "Na_capacity": "number (mAh/g)",
          "Li_open_circuit_voltage": "number (eV)",
          "Na_open_circuit_voltage": "number (eV)"
        }
      },
      "description": "Final scored battery performance results. Each field is compared directionally: lower diffusion barriers and higher capacities are better; voltages are compared within a tolerance. Better-than-reference values earn full credit."
    }
  ],
  "notes": "Only results.json is scored. The process-step evidence files (relaxed_structure.cif and bulk_energies.json) are not scored but their presence is checked to ensure the workflow was executed."
}
```

## How you are scored

A hidden verifier reads `results.json` and independently compares each of the six numeric values against reference thresholds. For each quantity, full credit is awarded if the computed value is at least as good as the reference threshold (higher capacity, lower diffusion barrier, voltage within tolerance); worse values receive partial or zero credit. The process steps (1 and 2) are checked for existence of the evidence files but do not carry direct score weight; the scored step (3) determines the entire reward.

Note: The solving agent may use appropriate external/remote compute resources to run the DFT and NEB calculations, then place the required final artifacts under `/app/outputs`.
