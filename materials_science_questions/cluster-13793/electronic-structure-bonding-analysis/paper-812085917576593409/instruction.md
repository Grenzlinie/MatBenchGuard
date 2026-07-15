# Re Site Preference and Interfacial Rupture Strength in Ni/Ni3Al from First-Principles DFT

## Problem background
Ni‑based single‑crystal superalloys used in turbine blades derive their high‑temperature strength from coherent γ/γ′ interfaces. Alloying with Re significantly improves creep resistance, but the atomic‑scale strengthening mechanism is not fully understood. A first‑principles DFT study can determine which sites Re occupies at the Ni/Ni₃Al interface and how Re substitution affects the interfacial rupture strength.

## Approach
Construct a 64‑atom periodic Ni/Ni₃Al (002) coherent interface supercell and create five substitution models: a Re‑free reference (no‑add); Re at a Ni site in the γ‑Ni block (Ni(1)); Re at a Ni site at the coherent interfacial layer (Ni(2)); Re at a Ni site in the γ′‑Ni₃Al block (Ni(3)); and Re replacing an Al site adjacent to the interface in the γ′ block (Al(4)). Perform DFT structure optimization for each model and compute the total energy. Also compute per‑atom reference energies for elemental fcc Ni, fcc Al, and hcp Re using the same functional and pseudopotentials. From these, calculate the heat of formation per atom for each model, and order the models by their heat of formation to determine the site preference of Re. Then, for the no‑add, Ni(1), Ni(2), and Ni(3) models, cleave the optimized interface along two possible fracture regions (region‑1 and region‑2) to create surface slabs, compute their single‑point energies, and calculate the Griffith rupture work for each model and region. This workflow tests the effect of Re substitution on interfacial rupture strength using open‑source plane‑wave DFT (e.g., Quantum ESPRESSO) and pseudopotentials from a standard library (e.g., SSSP PBE).

## Reproduction target
Produce the site preference ordering of Re at the Ni/Ni₃Al interface based on the heat of formation: a list of model names ordered by decreasing stability, together with the corresponding heat‑of‑formation per atom (eV). Also produce a table of Griffith rupture work values (J/m²) for the no‑add, Ni(1), Ni(2), and Ni(3) models at both region‑1 and region‑2. From these results, it should be possible to check whether substitution at the coherent interfacial layer (Ni(2)) alters the rupture strength relative to the Re‑free interface.

## Assets

- Quantum ESPRESSO (or other open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP PBE efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build interface supercell models
- Role: process
- Action: Construct 64‑atom periodic Ni/Ni3Al (002) coherent interface supercells for five substitution models: no‑add (Re‑free), Ni(1) (Re substitutes Ni in γ‑Ni block), Ni(2) (Re substitutes Ni at the coherent interfacial layer), Ni(3) (Re substitutes Ni in γ′‑Ni3Al block), and Al(4) (Re substitutes Al adjacent to the interface in the γ′ block). Generate initial atomic positions and lattice vectors based on fcc Ni and L12 Ni3Al crystal structures.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: Compute reference elemental per‑atom energies
- Role: process
- Action: Perform DFT total energy calculations for the elemental crystals fcc Ni, fcc Al, and hcp Re using the same exchange‑correlation functional and pseudopotential library as the interface calculations. Extract per‑atom energies E_c(Ni), E_c(Al), and E_c(Re).
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Geometry optimization of all interface models
- Role: process
- Action: Run DFT structure relaxation (atomic positions and cell parameters) for each of the five interface models. Converge forces and stress to obtain equilibrium lattice constants and total energies E_i for each model.
- Evidence: `/app/outputs/optimized_energies.json`

### Step 4: Calculate heat of formation and determine site preference ordering
- Role: scored
- Action: For each interface model, compute the heat of formation per atom H = (E_i − n·E_c(Ni) − m·E_c(Al) − l·E_c(Re)) / (n+m+l) using the DFT total energies E_i and the reference per‑atom energies. Produce the list of model names ordered by decreasing stability (most negative H first) and the corresponding heat of formation values.
- Output file: `/app/outputs/site_preference_ordering.json`
- Format: json
- Contract: {"models": ["string", ...], "heat_per_atom": {"model_name": float}}
- Scoring: scored by hidden verifier

### Step 5: Construct and compute surface slab energies
- Role: process
- Action: For the no‑add, Ni(1), Ni(2), and Ni(3) models, create surface slab models by cleaving the optimized interface supercell along region‑1 (between (002)γ/γ′ and (001)γ′ layers) and region‑2 (between (001)γ and (002)γ/γ′ layers). Perform single‑point DFT calculations on each slab with vacuum to obtain the total energies E_s^γ and E_s^γ′ for each model and cleavage region.
- Evidence: `/app/outputs/surface_energies.json`

### Step 6: Compute Griffith rupture work
- Role: scored (load-bearing)
- Action: For each of the four models (no‑add, Ni(1), Ni(2), Ni(3)) and each region (region‑1, region‑2), calculate the Griffith rupture work W = (−1/(2·S_i))·(E_i − E_s^γ − E_s^γ′), where S_i = a·b is the lateral area of the optimized interface supercell. Compile all results into a CSV table.
- Output file: `/app/outputs/griffith_work_results.csv`
- Format: csv
- Contract: model (string), region (string, e.g., region‑1 or region‑2), Griffith_work_J_m2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/site_preference_ordering.json`
- `/app/outputs/griffith_work_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### site_preference_ordering.json
- path: `/app/outputs/site_preference_ordering.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Site preference ordering of Re at the Ni/Ni3Al interface based on heat of formation. The 'models' array must list the model names in the correct stability order, which is checked against the hidden gold. The 'heat_per_atom' object provides the computed H values for each model.
- schema:
  - `type`: object
  - `required`:
    - `models`: ordered array of strings
    - `heat_per_atom`: object mapping model name to float (eV)

### griffith_work_results.csv
- path: `/app/outputs/griffith_work_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Griffith rupture work for the no‑add, Ni(1), Ni(2), and Ni(3) interface models evaluated at region‑1 and region‑2. Values are compared to the paper's reported rupture work with a tolerance of ±0.3 J/m²; the region‑1 trend W(Ni(2)) > W(no‑add) > W(Ni(1)) must also hold.
- schema:
  - `type`: table
  - `required_columns`: `model`, `region`, `Griffith_work_J_m2`
  - `units`:
    - `Griffith_work_J_m2`: J/m^2

Notes: The task uses an open‑source DFT code (e.g., Quantum ESPRESSO) with SSSP PBE pseudopotentials. All intermediate DFT parameters (k‑point samplings, energy cutoffs, convergence thresholds) are left to the solver. The Mulliken population analysis and charge density contour plots are excluded as non‑verifiable and sensitive to the DFT implementation. The heat‑of‑formation ordering and Griffith work values form a complete test of the paper's core energetic conclusions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "site_preference_ordering.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "models": "ordered array of strings",
          "heat_per_atom": "object mapping model name to float (eV)"
        }
      },
      "description": "Site preference ordering of Re at the Ni/Ni3Al interface based on heat of formation. The 'models' array must list the model names in the correct stability order, which is checked against the hidden gold. The 'heat_per_atom' object provides the computed H values for each model."
    },
    {
      "file": "griffith_work_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "region",
          "Griffith_work_J_m2"
        ],
        "units": {
          "Griffith_work_J_m2": "J/m^2"
        }
      },
      "description": "Griffith rupture work for the no‑add, Ni(1), Ni(2), and Ni(3) interface models evaluated at region‑1 and region‑2. Values are compared to the paper's reported rupture work with a tolerance of ±0.3 J/m²; the region‑1 trend W(Ni(2)) > W(no‑add) > W(Ni(1)) must also hold."
    }
  ],
  "notes": "The task uses an open‑source DFT code (e.g., Quantum ESPRESSO) with SSSP PBE pseudopotentials. All intermediate DFT parameters (k‑point samplings, energy cutoffs, convergence thresholds) are left to the solver. The Mulliken population analysis and charge density contour plots are excluded as non‑verifiable and sensitive to the DFT implementation. The heat‑of‑formation ordering and Griffith work values form a complete test of the paper's core energetic conclusions."
}
```

## How you are scored
Your outputs are scored by a hidden verifier that you do not have access to. The verifier checks the submitted site preference ordering (model sequence) against its own reference ordering. For the Griffith work results, it compares your computed values to hidden reference values with an allowed tolerance, and also verifies a required trend among the Griffith work results for region‑1. Each scored artifact carries a weight, and the final reward (a number between 0 and 1) is the weighted sum. You must produce these values from your own DFT calculations; merely reporting numbers that are not self‑consistently computed will not satisfy the verifier.
