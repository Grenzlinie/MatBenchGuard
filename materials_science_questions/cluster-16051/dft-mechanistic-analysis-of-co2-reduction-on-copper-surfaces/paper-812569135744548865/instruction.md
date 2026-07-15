# DFT Barriers for CO Oxidation on CuO(111)

## Problem background
Copper-based oxygen carriers are attractive for chemical looping combustion and CO catalytic oxidation because of their high reactivity and low cost. The CuO(111) surface is the most stable termination of cupric oxide and is therefore a key model surface for understanding surface reactivity. However, the dominant CO oxidation mechanism on this surface—whether it proceeds via the Mars–van‑Krevelen (MvK) path (CO reacting with lattice oxygen), the Eley‑Rideal (ER) path (CO reacting with a pre‑adsorbed oxygen atom), or the Langmuir‑Hinshelwood (LH) path (co‑adsorbed CO and O)—is not fully settled. This task addresses that question by computing the 0 K electronic activation energy barriers for all three pathways using dispersion‑corrected density functional theory, providing a direct kinetic comparison to determine the most feasible mechanism.

## Approach
We use plane‑wave density functional theory with the Perdew‑Burke‑Ernzerhof (PBE) exchange‑correlation functional and Grimme’s D3 dispersion correction, as implemented in an open‑source DFT code (e.g., Quantum ESPRESSO). A periodic slab model of the perfect CuO(111) surface is built from the monoclinic CuO bulk structure (C2/c symmetry, lattice constants a=4.669 Å, b=3.553 Å, c=5.220 Å, β=93.8°), containing nine atomic layers and 12 Å of vacuum to separate periodic images. After optimising the slab geometry, we determine the most stable adsorption structures for CO and atomic O on the surface by evaluating several plausible binding sites (Cu CUS , O CUS , and bridge sites). These optimised structures serve as initial and final states for the MvK, ER, and LH mechanisms. For each mechanism we locate the transition state using the climbing‑image nudged elastic band (NEB) method or a combination of linear and quadratic synchronous transit (LST/QST), and confirm the transition state by vibrational analysis (exactly one imaginary frequency). The activation barrier is taken as the zero‑point‑uncorrected electronic energy difference between the transition state and the corresponding initial state. The three barriers are then compared to establish which pathway is kinetically most favourable.

## Reproduction target
Your goal is to produce a JSON file, `barriers.json`, containing the 0 K electronic activation energy barriers (in eV) for the three CO oxidation mechanisms on the perfect CuO(111) surface: `MvK_barrier_0K` (CO + lattice O), `ER_barrier_0K` (CO + pre‑adsorbed O), and `LH_barrier_0K` (co‑adsorbed CO and O). The values must be obtained by running the complete DFT workflow described below: build and optimise the slab, locate the stable adsorption configurations, and compute the transition‑state barriers for each mechanism using an open‑source plane‑wave code with the PBE functional and Grimme D3 dispersion correction. The final output should permit a clear ordering of the three mechanisms by their barrier height.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for Cu and O: https://materialscloud.org/sssp/

## Workflow steps

### Step 1: Prepare CuO(111) surface slab model
- Role: process
- Action: Construct a periodic slab model of the CuO(111) surface from the monoclinic bulk CuO (C2/c) with lattice constants a=4.669 Å, b=3.553 Å, c=5.220 Å, β=93.8°, containing nine atomic layers and 12 Å vacuum. Optimize the slab geometry using DFT-D/PBE.
- Evidence: `/app/outputs/surface_model.log`

### Step 2: Determine adsorption configurations for CO and atomic O
- Role: process
- Action: Place CO and atomic O at plausible surface sites (CuCUS, OCUS, bridges) on the optimized CuO(111) slab and optimize the geometries to find the most stable adsorption structures. These serve as initial and final states for the ER and LH mechanisms.
- Evidence: `/app/outputs/adsorption.log`

### Step 3: Compute CO oxidation reaction barriers
- Role: scored (load-bearing)
- Action: For each mechanism (MvK: CO + lattice O; ER: CO + pre-adsorbed O; LH: co-adsorbed CO and O), define initial state (IS) and final state (FS), locate the transition state (TS) using LST/QST or NEB, verify with vibrational analysis (one imaginary frequency), and calculate the 0 K electronic energy barrier (E_TS - E_IS). Report the three barriers in eV.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: {"MvK_barrier_0K": float, "ER_barrier_0K": float, "LH_barrier_0K": float} (all in eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed 0 K electronic energy barriers for the three CO oxidation mechanisms on the perfect CuO(111) surface. The hidden checker compares each barrier to the paper-reported reference within a tolerance and verifies that ER_barrier < LH_barrier and ER_barrier < MvK_barrier.
- schema:
  - `type`: object
  - `required`:
    - `MvK_barrier_0K`: number (eV)
    - `ER_barrier_0K`: number (eV)
    - `LH_barrier_0K`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `MvK_barrier_0K`: eV
    - `ER_barrier_0K`: eV
    - `LH_barrier_0K`: eV

Notes: The paper used DMol3 with a DNP basis set; the task allows any open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with PBE functional and Grimme D3 dispersion correction. Differences in basis set and pseudopotentials may cause small variations; scoring uses an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "MvK_barrier_0K": "number (eV)",
          "ER_barrier_0K": "number (eV)",
          "LH_barrier_0K": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "MvK_barrier_0K": "eV",
          "ER_barrier_0K": "eV",
          "LH_barrier_0K": "eV"
        }
      },
      "description": "Computed 0 K electronic energy barriers for the three CO oxidation mechanisms on the perfect CuO(111) surface. The hidden checker compares each barrier to the paper-reported reference within a tolerance and verifies that ER_barrier < LH_barrier and ER_barrier < MvK_barrier."
    }
  ],
  "notes": "The paper used DMol3 with a DNP basis set; the task allows any open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with PBE functional and Grimme D3 dispersion correction. Differences in basis set and pseudopotentials may cause small variations; scoring uses an appropriate tolerance."
}
```

## How you are scored
A hidden verifier reads your `barriers.json` and scores each of the three reported barriers against a reference (the paper’s own computed values) using a tolerance that accounts for legitimate differences between DFT implementations (basis set, pseudopotentials, numerical settings). In addition, the verifier checks a structural condition: the ordering of the three barriers (i.e., which mechanism has the lowest barrier) must match the paper’s finding. The three barrier values carry equal weight, and the ordering check adds a small additional weight. To succeed, you must genuinely run the DFT calculations; simply copying literature values will not reproduce the reference within the required tolerance for an independently re‑run computation.
