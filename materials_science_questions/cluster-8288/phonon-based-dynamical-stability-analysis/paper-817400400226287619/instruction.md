## Problem background

The crystal structure and dynamical stability of two‑dimensional (2D) metals are key to understanding their potential as building blocks for 2D materials and ordered alloys. While many elemental 2D materials have been proposed, a systematic assessment of their dynamical stability from first‑principles phonon calculations is lacking. This task reproduces the dynamical stability evaluation for a representative set of 2D metals in three common monolayer structures: planar hexagonal (HX), buckled honeycomb (bHC), and buckled square (bSQ). A structure is considered dynamically stable if its phonon spectrum contains no imaginary frequencies over the whole Brillouin zone.

## Approach

The computational workflow combines density‑functional theory (DFT) total‑energy calculations and density‑functional perturbation theory (DFPT) phonon calculations using the open‑source code Quantum ESPRESSO with the GGA‑PBE exchange‑correlation functional and ultrasoft pseudopotentials from pslibrary 1.0.0. The key quantities to be produced are the optimized lattice constant a, buckling height δ, cohesive energy per atom, and a dynamical stability flag (stable/unstable) for each element–structure combination. The main steps are:

1. **Isolated‑atom reference energy** – Compute the total energy of a single atom of each element in a large periodic box, to serve as the reference εₐₜₒₘ needed for cohesive energies.
2. **Geometry optimization** – For each element and each of the three monolayer structures, perform a full DFT relaxation to obtain the optimized lattice constant a, buckling height δ (zero for HX), and total energy per atom εⱼ.
3. **DFPT phonon calculation** – On each relaxed structure, compute the phonon dispersion and extract the phonon frequencies.
4. **Stability analysis** – Calculate the cohesive energy per atom as Eⱼ = εₐₜₒₘ − εⱼ, then determine dynamical stability by checking for imaginary phonon frequencies (ω² < 0). A structure without imaginary modes is flagged as stable.

The target is a single summary table containing all quantities for the five elements Li, Be, Sc, Cu, Al in the HX, bHC, and bSQ structures (15 combinations). Because the required DFT and DFPT calculations are computationally heavy, you are expected to acquire appropriate external computing resources (e.g., a cluster or cloud instances) and run them there. The final verifiable artifact must be placed under `/app/outputs`.

## Reproduction target

Produce a JSON file `/app/outputs/results_summary.json` containing an array of 15 objects (one per element‑structure combination). Each object must include:
- `element` (string): one of "Li", "Be", "Sc", "Cu", "Al"
- `structure` (string): one of "HX", "bHC", "bSQ"
- `a` (number): optimized lattice constant in Å
- `delta` (number): buckling height in Å (0 for HX)
- `cohesive_energy_per_atom` (number): cohesive energy per atom in eV
- `stable` (boolean): true if dynamically stable, false otherwise

All 15 combinations must be present. The values must be obtained from a complete first‑principles workflow as described below; simply reporting numbers without running the calculations will not satisfy the task.

## Assets

- **Quantum ESPRESSO** (version ≥ 6.6) – open‑source plane‑wave DFT code, available at https://www.quantum-espresso.org/ or via `conda install -c conda-forge qe`.
- **pslibrary 1.0.0** – ultrasoft pseudopotentials for GGA‑PBE, available at https://dalcorso.github.io/pslibrary/.  Required for all five elements.
- **Nearest‑neighbour distances d₃ᴅ** – Used as initial lattice constant guesses for geometry optimization. Standard tabulated values from solid‑state physics references (e.g., Kittel) are provided below:
  - Li: 3.04 Å
  - Be: 2.22 Å
  - Sc: 3.26 Å
  - Cu: 2.56 Å
  - Al: 2.86 Å

You may retrieve these assets in whichever way you find most convenient; the access hints above are suggestions.

## Workflow steps

### Step 1: Isolated atom reference energies
- Role: process
- Action: For each element (Li, Be, Sc, Cu, Al), perform a spin‑unpolarized DFT total‑energy calculation of a single atom in a 15 × 15 × 15  Å³ periodic box using the GGA‑PBE functional and the corresponding pslibrary 1.0.0 ultrasoft pseudopotential. Save the total energy for each element.
- Evidence: `/app/outputs/atom_energies.json`

### Step 2: Geometry optimization of HX, bHC, bSQ structures
- Role: process
- Action: For each of the five elements, set up the unit cells for the three monolayer structures:
  - HX: planar hexagonal (no buckling)
  - bHC: buckled honeycomb, two atoms at (0, 0, +δ) and (0, a/√3, −δ)
  - bSQ: buckled square, two atoms at (0, 0, +δ) and (a/2, a/2, −δ)
  Use an initial lattice constant equal to the d₃ᴅ value listed above and, for bHC and bSQ, an initial buckling of 0.3 × d₃ᴅ. Run a full DFT geometry optimization (GGA‑PBE, pslibrary 1.0.0 pseudopotentials) with tight convergence criteria (energy convergence ≤ 10⁻⁵ Ry, force convergence ≤ 10⁻⁴ a.u.), a 30 × 30 × 1 k‑point grid, wave‑function/charge‑density cutoffs that are well converged (the paper’s reference values are 80 Ry / 800 Ry), Marzari‑Vanderbilt smearing with σ = 0.02 Ry, and a vacuum spacing of 14 Å in the out‑of‑plane direction. For each relaxed structure record the final lattice constant a, buckling height δ, and the total energy per atom εⱼ.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 3: DFPT phonon calculations
- Role: process
- Action: For each relaxed structure obtained in Step 2, perform a DFPT phonon calculation using the same QE setup. Use q‑point grids of 8 × 8 × 1 for HX and bHC structures, and 6 × 6 × 1 for bSQ structures. Extract the phonon frequencies along the high‑symmetry directions; the key output is a list of frequencies (or a binary flag indicating presence of imaginary modes) that will enable the stability decision in the next step.
- Evidence: `/app/outputs/phonon_bands.json`

### Step 4: Stability summary and results table  *(load‑bearing)*
- Role: scored (load‑bearing)
- Action: Using the results from Steps 1–3, compute for each (element, structure) the cohesive energy per atom as Eⱼ = εₐₜₒₘ − εⱼ (in eV). Determine dynamical stability: if the phonon spectrum contains no imaginary frequencies (i.e., all ω² ≥ 0 or equivalent), set `stable` to true; otherwise set it to false. Collect all quantities into a single JSON array, one object per combination, and write it to the output file.
- Output file: `/app/outputs/results_summary.json`
- Format: JSON
- Contract: An array of objects, each with the keys: `element` (string), `structure` (string, one of "HX","bHC","bSQ"), `a` (float, Å), `delta` (float, Å, 0 for HX), `cohesive_energy_per_atom` (float, eV), `stable` (boolean). All 15 combinations must be present.
- Scoring: This artifact carries the entire task reward. It is load‑bearing because the values can only be obtained by genuinely running the preceding DFT/DFPT steps.

## Output files

- `/app/outputs/results_summary.json` (scored)
- Supporting evidence: `/app/outputs/atom_energies.json`, `/app/outputs/relaxed_structures.json`, `/app/outputs/phonon_bands.json` (not directly scored but must be produced as proof of execution).

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored table of dynamical stability assessment: lattice parameter, buckling, cohesive energy and stability flag for each of the 15 element‑structure combinations.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `element`, `structure`, `a`, `delta`, `cohesive_energy_per_atom`, `stable`
    - `properties`:
      - `element`:
        - `type`: string
        - `enum`: `Li`, `Be`, `Sc`, `Cu`, `Al`
      - `structure`:
        - `type`: string
        - `enum`: `HX`, `bHC`, `bSQ`
      - `a`:
        - `type`: number
        - `unit`: Å
      - `delta`:
        - `type`: number
        - `unit`: Å
        - `description`: 0 for HX
      - `cohesive_energy_per_atom`:
        - `type`: number
        - `unit`: eV
      - `stable`:
        - `type`: boolean

Notes: The verifier compares each reported a, delta, cohesive_energy_per_atom to reference values with domain‑appropriate tolerances, and checks the stable flag against the expected classification.  All tolerance values are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "element",
            "structure",
            "a",
            "delta",
            "cohesive_energy_per_atom",
            "stable"
          ],
          "properties": {
            "element": {
              "type": "string",
              "enum": [
                "Li",
                "Be",
                "Sc",
                "Cu",
                "Al"
              ]
            },
            "structure": {
              "type": "string",
              "enum": [
                "HX",
                "bHC",
                "bSQ"
              ]
            },
            "a": {
              "type": "number",
              "unit": "Å"
            },
            "delta": {
              "type": "number",
              "unit": "Å",
              "description": "0 for HX"
            },
            "cohesive_energy_per_atom": {
              "type": "number",
              "unit": "eV"
            },
            "stable": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Scored table of dynamical stability assessment: lattice parameter, buckling, cohesive energy and stability flag for each of the 15 element‑structure combinations."
    }
  ],
  "notes": "The verifier compares each reported a, delta, cohesive_energy_per_atom to reference values with domain‑appropriate tolerances, and checks the stable flag against the expected classification.  All tolerance values are hidden."
}
```

## How you are scored

A hidden verifier reads your `/app/outputs/results_summary.json` and compares each reported lattice constant, buckling height, and cohesive energy to reference values (with generous tolerances that absorb legitimate tool‑chain differences), and also validates the `stable` flag against the expected stability classification.  The final reward is a weighted score in [0,1].  Simply reporting numbers that match a known table is insufficient; the verifier expects the numbers to result from a correctly executed first‑principles workflow.  The load‑bearing nature of this step means that ignoring the intermediate calculations and fabricating values would likely produce inconsistencies that are detectable.
