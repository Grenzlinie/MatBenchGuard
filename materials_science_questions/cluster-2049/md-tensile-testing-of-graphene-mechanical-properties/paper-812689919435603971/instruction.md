# DFT simulations of graphene moiré corrugation and stepped-terrace geometry on Ni(100)

## Problem background
Graphene growth on Ni(100) surfaces under chemical vapor deposition conditions involves a competition between strong carbon‑nickel bonding and in‑plane stress accumulation in the carbon layer. This interplay leads to several characteristic behaviors that have been studied with density functional theory (DFT). First, as a graphene ribbon grows across a flat Ni(100) terrace, it initially stays flat and strongly chemisorbed; beyond a certain width, the accumulated tensile stress becomes too large to sustain, and the ribbon undergoes a flat‑to‑corrugated transition, developing a regular moiré‑like out‑of‑plane modulation. Second, the stress that can be accommodated by the interface has a maximum magnitude – beyond this threshold, the graphene network relaxes through corrugation. Third, when graphene encounters high step bunches on the Ni surface, it does not simply drape across them; instead, the step bunch opens into a staircase of equally‑sized monoatomic terraces whose width is optimised by the balance between C‑Ni bond formation and stress relief. Understanding these phenomena quantitatively is important for controlling graphene quality on polycrystalline substrates.

## Approach
The task reproduces the DFT protocol used to calculate the above quantities. All simulations are performed with the open‑source Quantum ESPRESSO code, using the Generalized Gradient Approximation in the Perdew‑Burke‑Ernzerhof (GGA‑PBE) parametrization, augmented with the DFT‑D van der Waals correction. The Ni(100) surface is modeled as a slab three Ni layers thick, with a vacuum gap of about 15 Å between periodic images. Standard PBE pseudopotentials for Ni and C are employed.

The computational workflow consists of three parts:
1. **Graphene ribbons of varying width**: an orthorhombic slab periodic along the moiré‑stripe direction is prepared. Graphene ribbons of increasing width (number of carbon rows) are placed on one side of the slab, with one zigzag edge fixed at a moiré valley position. For each width, the atomic positions (except the fixed edge) are relaxed. This series of calculations simulates progressive carbon addition and reveals the critical width at which corrugation sets in, as well as the maximum tensile excess stress.
2. **Infinite graphene overlayer on flat Ni(100)**: a slab fully covered by a periodic infinite graphene layer is relaxed to obtain the equilibrium striped moiré pattern. From this relaxed structure the moiré beating period and the maximum compressive excess stress are determined.
3. **Stepped Ni(100) terrace with graphene**: a stepped slab containing two equal monoatomic terraces, each of width 9.5 a_Ni (a_Ni = 2.49 Å), is built, and a graphene overlayer is placed on top with a carbon‑to‑nickel row ratio of about 2.35 (±0.05). After relaxation, the geometry is used to compute the ratio of the terrace width to the flat‑surface moiré period.

## Reproduction target
Produce the following three quantities from the DFT simulations:
1. **Critical ribbon width** (integer, in number of carbon rows): the smallest graphene‑ribbon width at which the relaxed ribbon develops a corrugated (moiré‑like) out‑of‑plane modulation. Write this integer to `critical_width.txt`.
2. **Excess stress thresholds** (kbar): the maximum tensile excess stress (negative) and maximum compressive excess stress (positive) found in the relaxed infinite graphene overlayer, derived from the ribbon and infinite‑layer simulations. Write a JSON object with keys `"tensile_max"` and `"compressive_max"` to `stress_threshold.json`.
3. **Terrace‑width to moiré‑period ratio** (dimensionless float): the ratio of the staircase terrace width (9.5 a_Ni) to the moiré beating period obtained from the infinite‑layer simulation. Write the ratio to `terrace_ratio.txt`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PBE pseudopotentials for Ni and C: https://pseudo-dojo.org

## Workflow steps

### Step 1: DFT relaxations of graphene ribbons on Ni(100) of varying width
- Role: process
- Action: Build Ni(100) slab models (3 Ni layers, vacuum ~15 Å) with periodic dimension along the moiré-stripe direction and varying graphene ribbon widths on one side. For each width, fix one zigzag edge at a moiré valley position and relax the remaining atomic positions using DFT (GGA-PBE with DFT-D van der Waals correction). Increase ribbon width stepwise to simulate carbon addition.
- Evidence: `/app/outputs/ribbon_outputs.log`

### Step 2: DFT relaxation of infinite graphene overlayer on flat Ni(100)
- Role: process
- Action: Build a periodic Ni(100) slab fully covered by an infinite graphene layer. Relax atomic positions with the same DFT settings to obtain the equilibrium striped moiré structure, its period, and the maximum compressive excess stress.
- Evidence: `/app/outputs/infinite_layer_outputs.log`

### Step 3: Extract critical ribbon width for flat-to-corrugated transition
- Role: scored (load-bearing)
- Action: From the ribbon simulations, identify the smallest graphene-ribbon width (in number of carbon rows) at which the relaxed ribbon becomes corrugated (develops a moiré-like out-of-plane modulation). Write this single integer to /app/outputs/critical_width.txt.
- Output file: `/app/outputs/critical_width.txt`
- Format: txt
- Contract: single integer
- Scoring: scored by hidden verifier

### Step 4: Report maximum tensile and compressive excess stress thresholds
- Role: scored (load-bearing)
- Action: From the ribbon and infinite-layer simulations, extract the maximum tensile excess stress (negative value, in kbar) and the maximum compressive excess stress (positive value, in kbar). Write a JSON object with keys "tensile_max" and "compressive_max" to /app/outputs/stress_threshold.json.
- Output file: `/app/outputs/stress_threshold.json`
- Format: json
- Contract: {"tensile_max": float, "compressive_max": float}
- Scoring: scored by hidden verifier

### Step 5: DFT relaxation of graphene on a stepped Ni(100) terrace
- Role: process
- Action: Build a stepped Ni(100) slab model with two equal monoatomic terraces of width 9.5 a_Ni (a_Ni=2.49 Å) and a number of carbon rows maintaining a C:Ni row ratio ~2.35±0.05. Relax the atomic positions of graphene and topmost Ni layers with the same DFT settings.
- Evidence: `/app/outputs/stepped_outputs.log`

### Step 6: Compute terrace-width to moiré-period ratio
- Role: scored (load-bearing)
- Action: Using the terrace width (9.5 a_Ni) from the stepped simulation and the moiré beating period obtained from the infinite-layer simulation (step_02), compute the ratio (terrace width / moiré period). Write this single float to /app/outputs/terrace_ratio.txt.
- Output file: `/app/outputs/terrace_ratio.txt`
- Format: txt
- Contract: single float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_width.txt`
- `/app/outputs/stress_threshold.json`
- `/app/outputs/terrace_ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_width.txt
- path: `/app/outputs/critical_width.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The critical graphene-ribbon width (carbon rows) for the flat-to-corrugated transition, read as a plain number.
- schema:
  - `type`: text
  - `required`: A single integer or float, without additional characters or whitespace, representing the number of carbon rows.

### stress_threshold.json
- path: `/app/outputs/stress_threshold.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Maximum tensile and compressive excess stress (in kbar) in the optimized graphene overlayer, from the ribbon and infinite-layer simulations.
- schema:
  - `type`: object
  - `required`:
    - `tensile_max`: float (negative value, units kbar)
    - `compressive_max`: float (positive value, units kbar)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `tensile_max`: kbar
    - `compressive_max`: kbar

### terrace_ratio.txt
- path: `/app/outputs/terrace_ratio.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The dimensionless ratio of the optimal stepped‑terrace width (9.5 a_Ni) to the moiré beating period on flat Ni(100), derived from the stepped‑surface DFT simulation.
- schema:
  - `type`: text
  - `required`: A single float, without additional characters or whitespace, representing the ratio of staircase terrace width to moiré period.

Notes: All scored artifacts are extracted from DFT simulations. The hidden checker compares the agent’s numbers to the paper’s reported DFT values with appropriate per‑artifact tolerances; no gold values are disclosed here. Structural sanity checks are also performed (tensile_max negative, compressive_max positive, ratio > 1.0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_width.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": "A single integer or float, without additional characters or whitespace, representing the number of carbon rows."
      },
      "description": "The critical graphene-ribbon width (carbon rows) for the flat-to-corrugated transition, read as a plain number."
    },
    {
      "file": "stress_threshold.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "tensile_max": "float (negative value, units kbar)",
          "compressive_max": "float (positive value, units kbar)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "tensile_max": "kbar",
          "compressive_max": "kbar"
        }
      },
      "description": "Maximum tensile and compressive excess stress (in kbar) in the optimized graphene overlayer, from the ribbon and infinite-layer simulations."
    },
    {
      "file": "terrace_ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": "A single float, without additional characters or whitespace, representing the ratio of staircase terrace width to moiré period."
      },
      "description": "The dimensionless ratio of the optimal stepped‑terrace width (9.5 a_Ni) to the moiré beating period on flat Ni(100), derived from the stepped‑surface DFT simulation."
    }
  ],
  "notes": "All scored artifacts are extracted from DFT simulations. The hidden checker compares the agent’s numbers to the paper’s reported DFT values with appropriate per‑artifact tolerances; no gold values are disclosed here. Structural sanity checks are also performed (tensile_max negative, compressive_max positive, ratio > 1.0)."
}
```

## How you are scored
A hidden verifier independently inspects each scored output file and compares your reported numbers to reference values derived from the original DFT study. The comparison accounts for the expected numerical scatter that arises from using a different code version, pseudopotential library, or convergence settings, so small deviations within hidden tolerances are accepted. Additionally, the verifier checks structural constraints: the tensile stress must be negative, the compressive stress positive, and the terrace ratio must be greater than 1.0. Each scored artifact is converted to a per‑artifact score, and the final reward is a weighted sum of these scores. The exact tolerances and weights are not disclosed; your job is to faithfully execute the described DFT protocol and report the computed quantities.
