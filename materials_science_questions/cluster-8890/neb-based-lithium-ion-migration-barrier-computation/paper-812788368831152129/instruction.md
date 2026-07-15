# Lithium-ion migration barrier and storage properties of 2D carbon haeckelites

## Problem background
Lithium-ion batteries (LIBs) power most portable electronics and electric vehicles, but the anode material limits energy density and charge/discharge rates. Graphite is the standard anode with a theoretical capacity of 372 mAh/g, yet its low capacity and moderate Li-ion diffusion motivate the search for alternative carbon-based materials. Two-dimensional (2D) carbon allotropes containing topological defects—five- and seven-membered rings in addition to the usual six-membered rings—have been proposed as candidates because the non-hexagonal rings can create stronger Li binding sites and open faster diffusion channels. Among these, planar carbon haeckelites (denoted h567, r57, and o567) are a family of structures composed of mixed 5-, 6-, and 7-membered rings. This work investigates, through first-principles density functional theory (DFT), whether these haeckelites can serve as high-capacity, fast-diffusion anode materials for LIBs. The goal is to compute their Li binding strengths, migration barriers, maximum storage capacity, and average operating voltage to assess their promise relative to graphite.

## Approach
The evaluation is performed with first-principles DFT simulations. The workflow begins by constructing the unit cells of the three haeckelites—h567, r57, and o567—from their known crystal structures (mixed 5-, 6-, and 7-membered carbon rings). The pristine structures are fully relaxed to their equilibrium geometries using the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional with van der Waals corrections. On these relaxed structures, a single Li atom is placed in each distinct hollow ring site (pentagon, hexagon when present, heptagon) to calculate the Li binding energy as the difference between the total energies of the lithiated and pristine systems and the energy of an isolated Li atom. Next, migration energy barriers are computed with the climbing-image nudged elastic band (CI-NEB) method along the lowest-barrier paths connecting adjacent hollow sites, considering the high state-of-charge regime (Li placed in the unit cell). Additionally, for haeckelite h567, the maximum Li storage capacity is determined by sequentially lithiating both sides of the unit cell until the binding energy of the last added Li turns positive. The specific capacity (mAh/g) is derived from the corresponding LiₓC₆ stoichiometry. Finally, the average open-circuit voltage (OCV) of the fully lithiated h567 is computed from the formation energies of intermediate Li concentrations relative to pristine h567 and bulk Li metal. All calculations use a plane-wave basis with a kinetic-energy cutoff of at least 500 eV and a 3×3×1 k-point grid; atomic positions are relaxed until forces fall below 0.01 eV/Å. The code can be any mainstream DFT package (VASP or an open-source equivalent such as Quantum ESPRESSO) in conjunction with standard PAW/PBE pseudopotentials.

## Reproduction target
Your task is to compute the following quantities and write them to the specified output files.

1. **Li binding energies** – For each haeckelite (h567, r57, o567), report the binding energy (in eV) of a single Li atom at the hollow site of a pentagon, a hexagon (where present), and a heptagon. Write these to `/app/outputs/binding_energies.json` following the schema described in the step.

2. **Li migration energy barriers** – For each haeckelite, run CI-NEB to obtain the minimum energy barrier (in eV) on the following paths at high state-of-charge:
   - h567: Ea(6→5) and Ea(5→6)
   - r57: Ea(5→5), Ea(5→7), Ea(7→5)
   - o567: Ea(5→5), Ea(5→7), Ea(7→5)
   Write to `/app/outputs/diffusion_barriers.json`.

3. **Maximum specific capacity of h567** – For h567 only, sequentially lithiate both sides of the unit cell and determine the maximum number of Li atoms that remain stably bound (negative binding energy). Convert this composition to a specific capacity (mAh/g) and report it together with the lithiation condition ("both sides lithiation") in `/app/outputs/specific_capacity.json`.

4. **Average open-circuit voltage of h567** – Using the total energies of the intermediate lithiated configurations, compute the formation energies relative to pristine h567 and bulk Li, construct the convex hull, and calculate the average OCV (in V) over the full lithiation range. Write the value to `/app/outputs/average_ocv.json`.

## Assets

- Quantum ESPRESSO (or VASP): https://www.quantum-espresso.org
- Atomic Simulation Environment (ASE): ase
- PBE pseudopotentials (SSSP or similar): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Geometry optimization of pristine haeckelite unit cells
- Role: process
- Action: Construct the unit cells of haeckelites h567, r57, and o567 using the known carbon ring arrangements and lattice parameters from the literature. Perform DFT structure relaxation to obtain equilibrium lattice constants and atomic positions. Use the PBE functional with van der Waals corrections, and converge forces.
- Evidence: `/app/outputs/pristine_relaxation.log`

### Step 2: Compute Li binding energies
- Role: scored
- Action: For each relaxed haeckelite, place a single Li atom in the hollow site of each distinct ring type (pentagon, hexagon where present, heptagon). Compute total energies and calculate the binding energy as E_b = E(Li+hae) - E(hae) - E(Li). Report binding energies for all ring sites.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: JSON object: keys 'h567', 'r57', 'o567'. Each value is an object mapping ring type ('pentagon', 'hexagon', 'heptagon') to binding energy in eV (float). Hexagon is only present when applicable.
- Scoring: scored by hidden verifier

### Step 3: Compute Li migration energy barriers via CI-NEB
- Role: scored (load-bearing)
- Action: Identify characteristic Li migration paths between adjacent hollow sites for each haeckelite. For the high state-of-charge condition (using the unit cell), run climbing-image nudged elastic band calculations to determine minimum energy barriers. Compute the following: h567: E_a(6→5) and E_a(5→6); r57: E_a(5→5), E_a(5→7), E_a(7→5); o567: E_a(5→5), E_a(5→7), E_a(7→5). Report the energy barriers in eV.
- Output file: `/app/outputs/diffusion_barriers.json`
- Format: json
- Contract: JSON object: keys 'h567', 'r57', 'o567'. Each value is an object mapping path identifier (e.g., 'Ea_6-5', 'Ea_5-6', 'Ea_5-5', 'Ea_5-7', 'Ea_7-5') to barrier in eV (float).
- Scoring: scored by hidden verifier

### Step 4: Determine maximum Li storage capacity of h567
- Role: scored
- Action: For haeckelite h567, sequentially add Li atoms to hollow sites on both sides of the unit cell, relaxing the structure at each composition. Continue until the binding energy of the last added Li atom becomes positive. From the maximum stable Li content, compute the specific capacity using the standard formula for Li_xC6. Report the capacity and the lithiation condition.
- Output file: `/app/outputs/specific_capacity.json`
- Format: json
- Contract: JSON object with key 'h567', value an object with 'capacity_mAh_per_g' (float) and 'condition' (string, e.g., 'both sides lithiation').
- Scoring: scored by hidden verifier

### Step 5: Compute average open-circuit voltage
- Role: scored
- Action: Using total energies of lithiated h567 configurations at intermediate Li concentrations, compute formation energies relative to pristine h567 and bulk Li metal. Construct the convex hull to identify stable intermediate phases and calculate voltage plateaus. Compute the average open-circuit voltage over the full lithiation range and report it in volts.
- Output file: `/app/outputs/average_ocv.json`
- Format: json
- Contract: JSON object with key 'h567', value is the average OCV in V (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`
- `/app/outputs/diffusion_barriers.json`
- `/app/outputs/specific_capacity.json`
- `/app/outputs/average_ocv.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Binding energies of a single Li atom on hollow ring sites of haeckelites. Checker compares each site's binding energy to the paper reference within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `h567`: object
    - `r57`: object
    - `o567`: object
  - `items`:
    - `h567`: object containing keys 'pentagon', 'hexagon', 'heptagon' each a float in eV
    - `r57`: object containing keys 'pentagon', 'heptagon' each a float in eV
    - `o567`: object containing keys 'pentagon', 'hexagon', 'heptagon' each a float in eV
  - `units`: eV

### diffusion_barriers.json
- path: `/app/outputs/diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: CI-NEB migration energy barriers for characteristic low-barrier paths. Lower barriers are better; checker scores threshold_or_better using the paper's reported barriers as the threshold.
- schema:
  - `type`: object
  - `required`:
    - `h567`: object
    - `r57`: object
    - `o567`: object
  - `items`:
    - `h567`: object containing keys 'Ea_6-5', 'Ea_5-6' each a float in eV
    - `r57`: object containing keys 'Ea_5-5', 'Ea_5-7', 'Ea_7-5' each a float in eV
    - `o567`: object containing keys 'Ea_5-5', 'Ea_5-7', 'Ea_7-5' each a float in eV
  - `units`: eV

### specific_capacity.json
- path: `/app/outputs/specific_capacity.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum theoretical specific capacity of h567. Higher capacity is better; checker applies threshold_or_better with a relative tolerance.
- schema:
  - `type`: object
  - `required`:
    - `h567`: object
  - `items`:
    - `h567`: object containing 'capacity_mAh_per_g' (float) and 'condition' (string)

### average_ocv.json
- path: `/app/outputs/average_ocv.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Average open-circuit voltage of h567. Lower OCV is better; checker scores threshold_or_better with the paper's OCV as the threshold.
- schema:
  - `type`: object
  - `required`:
    - `h567`: float
  - `units`: V

Notes: All scored outputs are numerical values derived from DFT and NEB calculations. The checker compares them to the paper's reported values with appropriate tolerances. Directional quantities (barrier, capacity, OCV) use threshold_or_better; binding energies use reference_match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "h567": "object",
          "r57": "object",
          "o567": "object"
        },
        "items": {
          "h567": "object containing keys 'pentagon', 'hexagon', 'heptagon' each a float in eV",
          "r57": "object containing keys 'pentagon', 'heptagon' each a float in eV",
          "o567": "object containing keys 'pentagon', 'hexagon', 'heptagon' each a float in eV"
        },
        "units": "eV"
      },
      "description": "Binding energies of a single Li atom on hollow ring sites of haeckelites. Checker compares each site's binding energy to the paper reference within a tolerance."
    },
    {
      "file": "diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "h567": "object",
          "r57": "object",
          "o567": "object"
        },
        "items": {
          "h567": "object containing keys 'Ea_6-5', 'Ea_5-6' each a float in eV",
          "r57": "object containing keys 'Ea_5-5', 'Ea_5-7', 'Ea_7-5' each a float in eV",
          "o567": "object containing keys 'Ea_5-5', 'Ea_5-7', 'Ea_7-5' each a float in eV"
        },
        "units": "eV"
      },
      "description": "CI-NEB migration energy barriers for characteristic low-barrier paths. Lower barriers are better; checker scores threshold_or_better using the paper's reported barriers as the threshold."
    },
    {
      "file": "specific_capacity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "h567": "object"
        },
        "items": {
          "h567": "object containing 'capacity_mAh_per_g' (float) and 'condition' (string)"
        }
      },
      "description": "Maximum theoretical specific capacity of h567. Higher capacity is better; checker applies threshold_or_better with a relative tolerance."
    },
    {
      "file": "average_ocv.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "h567": "float"
        },
        "units": "V"
      },
      "description": "Average open-circuit voltage of h567. Lower OCV is better; checker scores threshold_or_better with the paper's OCV as the threshold."
    }
  ],
  "notes": "All scored outputs are numerical values derived from DFT and NEB calculations. The checker compares them to the paper's reported values with appropriate tolerances. Directional quantities (barrier, capacity, OCV) use threshold_or_better; binding energies use reference_match."
}
```

## How you are scored
A hidden verifier independently inspects each output file you produce in `/app/outputs`. Every scored artifact is compared to a hidden reference gold using a policy appropriate to the quantity:

- Binding energies are evaluated by **reference_match** (numeric comparison against the expected values).
- Diffusion barriers, specific capacity, and average OCV are evaluated with **threshold_or_better**: your result earns full credit if it meets or exceeds (i.e., lower barrier, higher capacity, or lower OCV) the hidden threshold; credit degrades only when your value is worse than the reference.

The verifier weights the four scored stages and combines them into a final reward. You are not required to match any particular reported number, but you must perform the compute workflow honestly—the verifier's hidden gold corresponds to results obtainable by a correct re-run of the described procedure. The verifier does **not** re-run any heavy simulations; it only reads your submitted JSON artifacts.
