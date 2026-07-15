# DFT fixed-spin-moment study of magnetic ground states in B2 FeAl and FeV

## Problem background
Ordered B2 (CsCl-type) compounds FeAl and FeV are of fundamental interest because their simple two‑atom unit cell allows reliable electronic‑structure calculations, yet they exhibit a rich competition between nonmagnetic (NM), ferromagnetic (FM), and antiferromagnetic (AF) spin configurations. Understanding which magnetic state is the ground state, how the lattice constant and bulk modulus change with magnetism, and how close competing AF states lie in energy is central to interpreting experimental observations and to assessing the role of chemical disorder. This task uses first‑principles DFT calculations to map out the magnetic phase volumes, determine the equilibrium lattice constant and bulk modulus from the FM equation of state, extract the rigid‑lattice energy difference between the FM and the type‑I AF zero‑field solutions, and record the iron local moments at those special points.

## Approach
The method relies on total‑energy band‑structure calculations within the atomic‑sphere approximation, using a fixed‑spin‑moment (FSM) procedure. For each compound (FeAl and FeV) in the B2 structure, you will perform self‑consistent DFT runs on increasingly large magnetic cells (two‑atom cells for NM/FM configurations and four‑atom cells for type‑I AF configurations) at a series of volumes near equilibrium. In these runs the total magnetic moment M of the cell is constrained to a chosen value, and the total energy E(M) and local (site‑projected) magnetic moments are obtained. From the resulting E(M) curves you will identify zero‑field solutions (points where dE/dM=0) and classify them as stable, metastable, or unstable. Separately, the FM zero‑field energies at different volumes are fitted to an equation of state to extract the equilibrium lattice constant and bulk modulus. Finally, for each system you will report the equilibrium lattice constant, bulk modulus, the energy difference E_AF − E_FM at the equilibrium volume, and the iron magnetic moments for the FM and AF ground states.

## Reproduction target
For both FeAl and FeV, perform the DFT fixed‑spin‑moment workflow described above and produce two JSON files (`results_FeAl.json` and `results_FeV.json`) containing the following quantities, each expressed in the indicated units:

- `equilibrium_lattice_constant_a`: equilibrium lattice constant in atomic units (a.u.)
- `bulk_modulus_B`: bulk modulus in kbar
- `E_AF_minus_E_FM`: rigid‑lattice energy difference between the type‑I AF zero‑field solution and the FM zero‑field solution, as millirydberg per atom (mRy/atom)
- `FM_iron_moment`: iron local magnetic moment in the FM zero‑field state, in Bohr magnetons (μ_B)
- `AF_iron_moment`: iron local magnetic moment in the type‑I AF zero‑field state, in Bohr magnetons (μ_B)

The task is to compute these values independently using the protocol outlined above; the numeric results obtained are the scored artifacts.

## Assets

- Elk all-electron DFT code (or equivalent open-source DFT code supporting fixed-spin-moment calculations): https://elk.sourceforge.io/
- B2 FeAl crystal structure
- B2 FeV crystal structure

## Workflow steps

### Step 1: Perform fixed-spin-moment DFT calculations for FeAl and FeV
- Role: process
- Action: Set up and run DFT fixed-spin-moment calculations for FeAl and FeV using their B2 structures. For each system, perform calculations at a series of volumes (effective Wigner-Seitz radii spanning approximately ±5% around equilibrium) using 2-atom (FM/NM) and 4-atom (type-I AF) magnetic cells. Constrain the total magnetic moment M and compute total energy E(M) and local magnetic moments for each volume, producing sufficient data to construct E(M) curves and identify zero-field solutions.
- Evidence: `/app/outputs/dft_summary.txt`

### Step 2: Extract FeAl equilibrium properties and magnetic quantities
- Role: scored (load-bearing)
- Action: Using the computed DFT data for FeAl: (a) fit the total energies of the FM zero-field solutions to an equation of state to obtain equilibrium lattice constant a (a.u.) and bulk modulus B (kbar); (b) from the E(M) curves at the equilibrium volume, identify the FM and type-I AF zero-field solutions and compute E_AF_minus_E_FM (mRy/atom); (c) record the Fe local magnetic moments for the FM and AF zero-field states (μ_B). Write all values to results_FeAl.json.
- Output file: `/app/outputs/results_FeAl.json`
- Format: json
- Contract: {"equilibrium_lattice_constant_a": float (a.u.), "bulk_modulus_B": float (kbar), "E_AF_minus_E_FM": float (mRy/atom), "FM_iron_moment": float (μ_B), "AF_iron_moment": float (μ_B)}
- Scoring: scored by hidden verifier

### Step 3: Extract FeV equilibrium properties and magnetic quantities
- Role: scored
- Action: Using the computed DFT data for FeV: (a) fit the total energies of the FM zero-field solutions to an equation of state to obtain equilibrium lattice constant a (a.u.) and bulk modulus B (kbar); (b) from the E(M) curves at the equilibrium volume, identify the FM and type-I AF1 zero-field solutions and compute E_AF1_minus_E_FM (mRy/atom); (c) record the Fe local magnetic moments for the FM and AF1 states (μ_B). Write all values to results_FeV.json.
- Output file: `/app/outputs/results_FeV.json`
- Format: json
- Contract: {"equilibrium_lattice_constant_a": float (a.u.), "bulk_modulus_B": float (kbar), "E_AF_minus_E_FM": float (mRy/atom), "FM_iron_moment": float (μ_B), "AF_iron_moment": float (μ_B)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_FeAl.json`
- `/app/outputs/results_FeV.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_FeAl.json
- path: `/app/outputs/results_FeAl.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored FeAl equilibrium and magnetic properties.
- schema:
  - `type`: object
  - `required`:
    - `equilibrium_lattice_constant_a`: number
    - `bulk_modulus_B`: number
    - `E_AF_minus_E_FM`: number
    - `FM_iron_moment`: number
    - `AF_iron_moment`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `equilibrium_lattice_constant_a`: a.u.
    - `bulk_modulus_B`: kbar
    - `E_AF_minus_E_FM`: mRy/atom
    - `FM_iron_moment`: μ_B
    - `AF_iron_moment`: μ_B

### results_FeV.json
- path: `/app/outputs/results_FeV.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored FeV equilibrium and magnetic properties.
- schema:
  - `type`: object
  - `required`:
    - `equilibrium_lattice_constant_a`: number
    - `bulk_modulus_B`: number
    - `E_AF_minus_E_FM`: number
    - `FM_iron_moment`: number
    - `AF_iron_moment`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `equilibrium_lattice_constant_a`: a.u.
    - `bulk_modulus_B`: kbar
    - `E_AF_minus_E_FM`: mRy/atom
    - `FM_iron_moment`: μ_B
    - `AF_iron_moment`: μ_B

Notes: Values are compared to the paper-reported results with appropriate hidden tolerances (lattice constant ±3%, bulk modulus ±20%, energy difference ±1 mRy/atom, iron moments ±0.2 μ_B).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_FeAl.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "equilibrium_lattice_constant_a": "number",
          "bulk_modulus_B": "number",
          "E_AF_minus_E_FM": "number",
          "FM_iron_moment": "number",
          "AF_iron_moment": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "equilibrium_lattice_constant_a": "a.u.",
          "bulk_modulus_B": "kbar",
          "E_AF_minus_E_FM": "mRy/atom",
          "FM_iron_moment": "μ_B",
          "AF_iron_moment": "μ_B"
        }
      },
      "description": "Scored FeAl equilibrium and magnetic properties."
    },
    {
      "file": "results_FeV.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "equilibrium_lattice_constant_a": "number",
          "bulk_modulus_B": "number",
          "E_AF_minus_E_FM": "number",
          "FM_iron_moment": "number",
          "AF_iron_moment": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "equilibrium_lattice_constant_a": "a.u.",
          "bulk_modulus_B": "kbar",
          "E_AF_minus_E_FM": "mRy/atom",
          "FM_iron_moment": "μ_B",
          "AF_iron_moment": "μ_B"
        }
      },
      "description": "Scored FeV equilibrium and magnetic properties."
    }
  ],
  "notes": "Values are compared to the paper-reported results with appropriate hidden tolerances (lattice constant ±3%, bulk modulus ±20%, energy difference ±1 mRy/atom, iron moments ±0.2 μ_B)."
}
```

## How you are scored
A hidden verifier reads your submitted `results_FeAl.json` and `results_FeV.json` and compares each numeric field against reference values using pre‑set tolerance bands. For each scalar, full credit is awarded when the value falls within its tolerance; credit decays as the deviation increases or becomes zero beyond a cutoff. The final reward is the weighted average of all individual scalar scores across both systems, normalized to the [0, 1] range. The verifier's tolerances and reference values are unknown to you; your objective is to obtain accurate values by faithfully executing the DFT workflow described in the steps.
