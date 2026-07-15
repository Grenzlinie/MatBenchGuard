# CO2 Electroreduction Mechanism on Au Single-Atom Catalyst

## Problem background
Electrochemical CO2 reduction (CO2RR) can convert the greenhouse gas CO2 into valuable fuels and chemicals. Single-atom catalysts (SACs) maximize atom utilization and offer tunable selectivity. This task studies the reaction mechanism of CO2RR on a single Au atom supported on a 2D graphitic carbon nitride monolayer (Au1@g-C3N4) using density functional theory (DFT) and the computational hydrogen electrode (CHE) method. The investigation aims to compute the Gibbs free energy profile at zero applied potential, identify the lowest-energy pathway, find the potential-limiting step and its limiting potential, predict the main reaction product, and determine whether CO* desorption is thermodynamically favorable.

## Approach
The approach uses periodic DFT with the PBE functional, a D3 dispersion correction, and PAW pseudopotentials, implemented in Quantum ESPRESSO. A corrugated 2×2 supercell of the g-C3N4 monolayer (001) surface is built from the Materials Project structure. One Au atom is placed in the cavity to form the catalyst. The CHE method is employed: the chemical potential of a proton–electron pair is referenced to half the Gibbs free energy of gas-phase H2. Gibbs free energies are computed as G = E_DFT + ZPE − TS, with ZPE and entropy corrections from vibrational frequency analyses. For each elementary proton-coupled electron transfer step, the reaction free energy ΔG at 0 V is calculated from the relative Gibbs energies of intermediates. From the full network, the minimum-energy pathway is determined, and the potential-limiting step is identified as the step with the largest positive ΔG at 0 V; its limiting potential is −ΔG_max. The main product is the terminal species of that pathway. The 'beyond CO' classification is based on whether the desorption free energy of CO* is positive.

## Reproduction target
Compute the following from first principles (DFT+CHE) and report them as specified:

- A CSV table (`gibbs_energies.csv`) listing every reaction intermediate and gas-phase species with its Gibbs free energy at 0 V vs SHE relative to CO2(g) and the clean Au1@g-C3N4 surface.
- A CSV table (`reaction_free_energies.csv`) containing the ΔG at 0 V for each elementary proton-coupled electron transfer step in the full reaction network.
- A JSON summary (`summary.json`) giving the lowest-energy pathway (sequence of intermediates from CO2(g) to the final product), the limiting potential (in eV), the identity of the rate-determining (potential-limiting) step, the predicted main product, and a boolean indicating whether CO* desorption is endergonic (`true` for 'beyond CO').

All calculations are performed with Quantum ESPRESSO (PBE+D3) using the provided pseudopotentials and structural model. The computational hydrogen electrode method is used throughout.

## Assets

- Quantum ESPRESSO (DFT package): https://www.quantum-espresso.org/
- g-C3N4 monolayer structure (001) from Materials Project: https://next-gen.materialsproject.org/
- Grimme D3 dispersion correction (dftd3): https://github.com/andrewwillis/dftd3
- PBE PAW pseudopotentials (PSlibrary 1.0.0): https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library

## Workflow steps

### Step 1: Geometry optimization of catalyst and all adsorbates/gas-phase species
- Role: process
- Action: Build the Au1@g-C3N4 monolayer slab (corrugated) from the Materials Project g-C3N4 structure. Perform periodic DFT (PBE+D3) geometry optimization for the clean slab, the slab with Au atom, and all CO2RR adsorbed intermediates (COOH*, HCOO*, CO*, HCO*, COH*, HCOH*, CH2O*, CH2OH*, CH3O*, CH2*, CH3*, CH*, O*, OH*). Also optimize gas-phase molecules: CO2, CO, CH4, CH3OH, H2O, H2, HCOOH, CH2O. Record the final total energies and optimized atomic coordinates.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Vibrational frequency analysis and thermodynamic corrections
- Role: process
- Action: For each optimized species (adsorbates and gas-phase molecules), compute vibrational frequencies via finite displacements. Extract zero-point energy (ZPE) and entropic (TS) corrections at standard temperature and pressure.
- Evidence: `/app/outputs/frequency_analysis.log`

### Step 3: Compute Gibbs free energies at 0 V and write gibbs_energies.csv
- Role: scored (load-bearing)
- Action: Calculate the Gibbs free energy of each species at 0 V vs SHE by combining the DFT total energy, ZPE, and -TS. Use the computational hydrogen electrode: reference H+ + e- to 1/2 G(H2). Express all Gibbs energies relative to CO2(g) and the clean catalyst surface. Write the result to /app/outputs/gibbs_energies.csv.
- Output file: `/app/outputs/gibbs_energies.csv`
- Format: csv
- Contract: species (string), G_0V (float, eV) relative to CO2(g) and clean surface
- Scoring: scored by hidden verifier

### Step 4: Compute elementary reaction free energies and write reaction_free_energies.csv
- Role: scored
- Action: From the Gibbs energies in gibbs_energies.csv, compute the reaction Gibbs free energy change (ΔG, in eV) at 0 V for each elementary proton-coupled electron transfer step in the full reaction network (R2a, R2b, R3a, R3b, R4a, R4b, R5a, R5b, R5c, R6a, R6b, R6c, R7a, R7b, R7cd, R8a, R9a, etc., and include CO* desorption). Write the table to /app/outputs/reaction_free_energies.csv.
- Output file: `/app/outputs/reaction_free_energies.csv`
- Format: csv
- Contract: step (string), delta_G (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Determine lowest energy pathway and key descriptors, output summary.json
- Role: scored
- Action: Using the Gibbs energy data, identify the sequence of intermediates with the minimum Gibbs energy barriers, forming the lowest-energy pathway. Find the potential-limiting step (the elementary step with the largest positive ΔG at 0 V) and compute its limiting potential. State the main product and evaluate whether CO* desorption is endergonic (ΔG > 0, indicating 'beyond CO'). Write the pathway, limiting potential, rate-determining step, main product, and beyond_CO boolean to /app/outputs/summary.json.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: {'lowest_energy_pathway': [list of strings from CO2(g) to CH4(g)], 'limiting_potential': float (eV), 'rate_determining_step': string, 'main_product': string, 'beyond_CO': boolean}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gibbs_energies.csv`
- `/app/outputs/reaction_free_energies.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gibbs_energies.csv
- path: `/app/outputs/gibbs_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gibbs free energies at 0 V vs SHE for every reaction intermediate and gas-phase species, referenced to CO2(g) and the clean Au1@g-C3N4 surface.
- schema:
  - `type`: table
  - `required_columns`: `species`, `G_0V`
  - `units`:
    - `G_0V`: eV

### reaction_free_energies.csv
- path: `/app/outputs/reaction_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reaction Gibbs free energy changes (ΔG) at 0 V for every elementary proton-coupled electron transfer step in the network.
- schema:
  - `type`: table
  - `required_columns`: `step`, `delta_G`
  - `units`:
    - `delta_G`: eV

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived mechanistic conclusion: the minimum-energy pathway, limiting potential (eV), rate-determining step, main product, and beyond-CO classification.
- schema:
  - `type`: object
  - `required`: `lowest_energy_pathway`, `limiting_potential`, `rate_determining_step`, `main_product`, `beyond_CO`
  - `properties`:
    - `lowest_energy_pathway`:
      - `type`: array
      - `items`: string
    - `limiting_potential`:
      - `type`: number
      - `unit`: eV
    - `rate_determining_step`: string
    - `main_product`: string
    - `beyond_CO`: boolean

Notes: All Gibbs energies are referenced to CO2(g) and the clean corrugated Au1@g-C3N4 surface. The computational hydrogen electrode method is used for H+/e−. The reaction_free_energies.csv is checked for internal consistency with gibbs_energies.csv; summary.json is validated against both the checked energies and the hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gibbs_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "G_0V"
        ],
        "units": {
          "G_0V": "eV"
        }
      },
      "description": "Gibbs free energies at 0 V vs SHE for every reaction intermediate and gas-phase species, referenced to CO2(g) and the clean Au1@g-C3N4 surface."
    },
    {
      "file": "reaction_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "delta_G"
        ],
        "units": {
          "delta_G": "eV"
        }
      },
      "description": "Reaction Gibbs free energy changes (ΔG) at 0 V for every elementary proton-coupled electron transfer step in the network."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "lowest_energy_pathway",
          "limiting_potential",
          "rate_determining_step",
          "main_product",
          "beyond_CO"
        ],
        "properties": {
          "lowest_energy_pathway": {
            "type": "array",
            "items": "string"
          },
          "limiting_potential": {
            "type": "number",
            "unit": "eV"
          },
          "rate_determining_step": "string",
          "main_product": "string",
          "beyond_CO": "boolean"
        }
      },
      "description": "Derived mechanistic conclusion: the minimum-energy pathway, limiting potential (eV), rate-determining step, main product, and beyond-CO classification."
    }
  ],
  "notes": "All Gibbs energies are referenced to CO2(g) and the clean corrugated Au1@g-C3N4 surface. The computational hydrogen electrode method is used for H+/e−. The reaction_free_energies.csv is checked for internal consistency with gibbs_energies.csv; summary.json is validated against both the checked energies and the hidden reference."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently reads your output files (`/app/outputs/gibbs_energies.csv`, `/app/outputs/reaction_free_energies.csv`, `/app/outputs/summary.json`). The verifier:

1. Recomputes the reaction free energies from your `gibbs_energies.csv` and checks them against your `reaction_free_energies.csv` for internal consistency.
2. Derives the lowest-energy pathway, the potential-limiting step, and the limiting potential from your Gibbs energies and compares them to the values you reported in `summary.json`.
3. Compares your computed Gibbs energies per species and your predicted limiting potential and beyond-CO classification to paper-derived hidden references (with appropriate tolerances for differences in DFT implementation).
4. Validates that your reported pathway and main product are consistent with the computed energy landscape.

Each scored component (Step 3, Step 4, Step 5) carries a weight. The verifier produces a reward between 0 and 1, where a higher reward means closer agreement with the expected results. Merely reporting plausible numbers without a genuine DFT calculation will not pass the consistency and reference checks.
