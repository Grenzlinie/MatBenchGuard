# Electronic Structure Bonding Analysis

## Problem background
Platinum-based catalysts are widely used for alkane dehydrogenation, but they suffer rapid deactivation due to the formation of carbonaceous deposits (coking). Doping with germanium has been found experimentally to improve catalyst selectivity and stability, yet the electronic origin of this improvement is not fully understood. This work uses density functional theory to investigate how a minimal coke unit (two carbon atoms, C2) attached to a Pt4 cluster on an Al2O3 support affects the electronic structure and catalytic activity for ethane C–H activation, and to examine whether Ge doping can counteract the deactivating effect of coke. The key quantities to compute are the kinetic barriers for the first C–H bond scission of ethane and the distribution of electronic charge among the cluster atoms.

## Approach
All calculations are performed using periodic plane-wave density functional theory with the PBE exchange-correlation functional. An open-source plane-wave code (Quantum ESPRESSO) and standard PAW pseudopotentials are used throughout. The model consists of a Pt4, Pt4C2, or Pt4GeC2 cluster supported on a 5‑layer 3×3 α‑Al2O3 supercell with a 15 Å vacuum gap. For each composition, global optimization is carried out to explore the potential energy surface of the supported cluster, identifying the lowest‑energy isomers. For Pt4GeC2, the isomer featuring a bonded C–C dimer (which lies slightly above the global minimum) is also of interest. From the low‑energy isomers, the most reactive ones are selected, and ethane adsorption configurations are located using DFT. For each active isomer, the first C–H activation transition state is found with the climbing‑image nudged elastic band (CI‑NEB) method, and the barrier is computed as the energy of the transition state relative to the global minimum isomer of that composition (in eV). Finally, Bader charge analysis (QTAIM) is performed on the active isomers of Pt4C2 and Pt4GeC2, and the sum of Pt atomic charges (ΣqPt) is evaluated. The overall comparison probes the effect of coke (C2) and Ge doping on catalytic activity and charge distribution.

## Reproduction target
Produce a JSON file, `results.json`, containing the following quantities:
- `Pt4`: the lowest ethane C–H activation barrier in eV.
- `Pt4C2`: the lowest ethane C–H activation barrier in eV and the sum of Pt Bader charges in units of elementary charge (e).
- `Pt4GeC2`: the lowest ethane C–H activation barrier in eV and the sum of Pt Bader charges in e.
All barriers must be reported as positive numbers, and charge sums must be reported with their sign (negative). The relative ordering of the barriers is expected to reveal the deactivating effect of coking and the mitigating effect of Ge doping: the barrier for Pt4 should be lower than that for Pt4C2, and the barrier for Pt4GeC2 should be lower than that for Pt4C2. The calculations must be performed using the workflow described above, relying on the publicly available α‑Al2O3 structure (Materials Project mp‑1143) and the open‑source tools Quantum ESPRESSO, VTST tools, and the Bader charge analysis code.

## Assets

- α-Al2O3 crystal structure: https://next-gen.materialsproject.org/materials/mp-1143
- Quantum ESPRESSO: https://www.quantum-espresso.org
- VTST tools (climbing-image NEB): http://theory.cm.utexas.edu/vtsttools/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Global optimization of cluster ensembles on α-Al2O3
- Role: process
- Action: Perform global optimization of Pt4, Pt4C2, and Pt4GeC2 clusters on a 5-layer 3×3 α-Al2O3 supercell with 15 Å vacuum using plane-wave DFT (PBE functional). Identify low-energy isomers for each composition; for Pt4GeC2, identify the C–C bonded isomer that lies approximately 0.06 eV above the global minimum.
- Evidence: `/app/outputs/global_optimization.log`

### Step 2: Ethane adsorption configurations
- Role: process
- Action: For the active isomer(s) of each composition (Pt4, Pt4C2, Pt4GeC2) find low-energy adsorption configurations of ethane (C2H6) on the cluster.
- Evidence: none

### Step 3: C–H activation transition state search
- Role: process
- Action: Using low-energy ethane adsorption structures as initial reactants, perform climbing-image nudged elastic band (CI-NEB) calculations to locate the transition state for the first C–H bond scission. Compute the energy of the transition state relative to the global minimum isomer of each composition (units: eV).
- Evidence: `/app/outputs/neb_barriers.json`

### Step 4: QTAIM charge analysis on active isomers
- Role: process
- Action: For the active isomers of Pt4C2 and Pt4GeC2 used in the NEB calculation, perform Bader charge analysis to obtain atomic charges. Compute the sum of Pt atomic charges (ΣqPt) in the supported cluster.
- Evidence: `/app/outputs/qtaim_charges.json`

### Step 5: Compile scored results
- Role: scored (load-bearing)
- Action: Compile the computed lowest ethane C–H activation barriers for Pt4, Pt4C2, and Pt4GeC2, and the Pt charge sums for Pt4C2 and Pt4GeC2, into a JSON file results.json. Barriers are in eV (positive), charge sums in e (negative).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"Pt4": {"ethane_barrier": <float>}, "Pt4C2": {"ethane_barrier": <float>, "Pt_charge_sum": <float>}, "Pt4GeC2": {"ethane_barrier": <float>, "Pt_charge_sum": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reproduced ethane C–H activation barriers and Pt charge sums. The checker compares each numeric field against the paper‑reported values within hidden tolerances and verifies the ordering Pt4.ethane_barrier < Pt4C2.ethane_barrier and Pt4GeC2.ethane_barrier < Pt4C2.ethane_barrier.
- schema:
  - `type`: object
  - `required`:
    - `Pt4`: object with key ethane_barrier (eV)
    - `Pt4C2`: object with keys ethane_barrier (eV) and Pt_charge_sum (e)
    - `Pt4GeC2`: object with keys ethane_barrier (eV) and Pt_charge_sum (e)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `ethane_barrier`: eV
    - `Pt_charge_sum`: e

Notes: The checker will also enforce the monotonic trend constraints. No gold values or tolerances are disclosed publicly.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Pt4": "object with key ethane_barrier (eV)",
          "Pt4C2": "object with keys ethane_barrier (eV) and Pt_charge_sum (e)",
          "Pt4GeC2": "object with keys ethane_barrier (eV) and Pt_charge_sum (e)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "ethane_barrier": "eV",
          "Pt_charge_sum": "e"
        }
      },
      "description": "Reproduced ethane C–H activation barriers and Pt charge sums. The checker compares each numeric field against the paper‑reported values within hidden tolerances and verifies the ordering Pt4.ethane_barrier < Pt4C2.ethane_barrier and Pt4GeC2.ethane_barrier < Pt4C2.ethane_barrier."
    }
  ],
  "notes": "The checker will also enforce the monotonic trend constraints. No gold values or tolerances are disclosed publicly."
}
```

## How you are scored
A hidden verifier will read your `results.json` and evaluate it against reference values (derived from the original paper) with appropriate tolerances that account for the spread expected when using an open‑source DFT code and different computational settings. It will check that each numeric field falls within the tolerance of its reference, and it will verify the barrier ordering: `Pt4.ethane_barrier < Pt4C2.ethane_barrier` and `Pt4GeC2.ethane_barrier < Pt4C2.ethane_barrier`. The final reward is a weighted combination of these checks; meeting all criteria yields the maximum score (1.0). Partial credit may be awarded if the barrier trends are correct and/or the charge values are within tolerance. The verifier may also inspect auxiliary evidence files to confirm that the required process steps (global optimization, CI‑NEB, Bader analysis) were genuinely executed; reporting the expected outcome without performing the calculations will not satisfy the scoring.
