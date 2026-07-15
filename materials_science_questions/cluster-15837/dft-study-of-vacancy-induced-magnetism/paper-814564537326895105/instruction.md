# DFT study of structural and magnetic properties of AlₓV₁₋ₓN compounds

## Problem background
Wurtzite AlN is a wide-band-gap semiconductor with applications in ultraviolet optoelectronics and high-power electronics. Substituting Al with transition metals such as vanadium can introduce magnetic properties, potentially yielding half-metallic ferromagnetism — a desirable feature for spintronic devices and spin injectors. This work computationally investigates the structural, electronic, and magnetic properties of wurtzite AlxV1-xN compounds (x=0.25, 0.50, 0.75) using first-principles density functional theory. The central questions are: what are the equilibrium lattice constants, total energies, formation energies, and magnetic moments of these ternary compounds, and do they exhibit half-metallic or metallic character?

## Approach
We use spin-polarized density functional theory (DFT) within the generalized gradient approximation of Perdew, Burke, and Ernzerhof (GGA-PBE). Electron-ion interactions are described by ultrasoft pseudopotentials for Al, V, and N, and the calculations are performed with Quantum ESPRESSO.

The workflow proceeds as follows:
- Construct wurtzite supercells for the ternary compounds AlxV1-xN (x=0.25, 0.50, 0.75) by substituting V atoms into appropriate AlN supercells. Also prepare unit cells for the binary reference compounds: AlN in the wurtzite structure, and VN in both the wurtzite and rock-salt (NaCl) structures.
- For each binary reference, perform a series of spin-polarized total energy versus volume calculations, fit the results to the Murnaghan equation of state, and extract the ground-state total energy E0 and, for the wurtzite phases, the equilibrium lattice constant a0.
- For each ternary composition, carry out spin-polarized total energy versus volume calculations in both ferromagnetic (FM) and antiferromagnetic (AFM) spin configurations. Relax the structures, fit to the Murnaghan equation of state, identify whether the FM or AFM configuration is the ground state, and from the FM ground state extract E0, a0, and the magnetic moment per V atom.
- From the self-consistent FM charge density of each ternary compound, compute the total and projected density of states (DOS) and band structures. Use the DOS to classify each composition as half-metallic (one spin channel metallic, the other insulating) or metallic (both spin channels conducting).
- Finally, compute the formation energy Ef of a ternary compound as the difference between its ground-state total energy and the weighted sum of the reference total energies of wurtzite AlN and NaCl VN.

## Reproduction target
The goal is to produce a single structured output file, `/app/outputs/computed_properties.json`, containing the following computed ground-state properties:

**Binary compounds** (AlN wurtzite, VN wurtzite, VN NaCl):
- Equilibrium lattice constant a0 (Å)
- Ground-state total energy E0 (eV)

**Ternary compounds** (Al0.25V0.75N, Al0.50V0.50N, Al0.75V0.25N):
- Al fraction x
- Equilibrium lattice constant a0 (Å)
- Ground-state total energy E0 (eV)
- Formation energy Ef (eV), computed using the reference energies of AlN wurtzite and VN NaCl
- Magnetic moment per V atom (μB)
- Electronic class: one of "half-metallic" or "metallic"

All values must be derived from the spin-polarized DFT calculations described in the workflow steps; no precomputed results should be used.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials for Al, V, N: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct wurtzite supercells for AlₓV₁₋ₓN (x=0.25,0.50,0.75) by substituting V atoms into AlN supercells, and create unit cells for pure AlN (wurtzite), VN (wurtzite), and VN (rock‑salt NaCl structure).
- Evidence: `/app/outputs/supercell_construction.log`

### Step 2: DFT reference calculations for binary compounds
- Role: process
- Action: Perform spin‑polarized DFT total‑energy vs volume calculations for AlN wurtzite, VN wurtzite, and VN NaCl. Fit each to the Murnaghan equation of state to obtain ground‑state total energy E₀. For AlN and VN wurtzite also extract equilibrium lattice constant a₀.
- Evidence: `/app/outputs/binary_dft.log`

### Step 3: Spin‑polarized DFT for AlₓV₁₋ₓN ternary compounds
- Role: process
- Action: For each ternary composition (x=0.25,0.50,0.75), run spin‑polarized DFT total‑energy vs volume in both FM and AFM magnetic configurations. Relax structures, fit to Murnaghan equation of state, identify the FM ground state, and extract total energy E₀, lattice constant a₀, and magnetic moment per V atom from the FM ground state.
- Evidence: `/app/outputs/ternary_dft.log`

### Step 4: Electronic structure and half‑metallicity classification
- Role: process
- Action: From the self‑consistent FM charge densities of each ternary compound, compute total and projected density of states (DOS) and band structures. Use these to classify each composition as half‑metallic or metallic.
- Evidence: `/app/outputs/dos_analysis.log`

### Step 5: Compilation of computed properties and formation energies
- Role: scored (load-bearing)
- Action: Aggregate all computed properties into a single JSON file. For binary compounds include name, a₀, E₀. For ternary compounds compute formation energy Ef using the ground‑state total energy of the ternary and the reference energies of AlN wurtzite and VN NaCl, then report x, a₀, E₀, Ef, magnetic moment per V atom, and class (half‑metallic or metallic).
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: JSON object with two keys: "binary_compounds" (list of objects with fields "name" (string), "a0" (float, Å), "E0" (float, eV)) and "ternary_compounds" (list of objects with fields "x" (float, one of 0.25/0.50/0.75), "a0" (float, Å), "E0" (float, eV), "Ef" (float, eV), "magnetic_moment" (float, μB), "class" (string, "half-metallic" or "metallic")).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final aggregated results containing lattice constants, total energies, formation energies, magnetic moments, and electronic classification for all compounds.
- schema:
  - `type`: object
  - `required`:
    - `binary_compounds`: array of objects with name, a0, E0
    - `ternary_compounds`: array of objects with x, a0, E0, Ef, magnetic_moment, class
  - `items`: object
  - `required_columns`:
  - `units`:
    - `a0`: Å
    - `E0`: eV
    - `Ef`: eV
    - `magnetic_moment`: μB

Notes: The checker recomputes relative/absolute deviations of numerical quantities against hidden paper‑reported values using threshold_or_better scoring, while the class field is compared exactly. The checker only validates the declared schema before scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "binary_compounds": "array of objects with name, a0, E0",
          "ternary_compounds": "array of objects with x, a0, E0, Ef, magnetic_moment, class"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "a0": "Å",
          "E0": "eV",
          "Ef": "eV",
          "magnetic_moment": "μB"
        }
      },
      "description": "Final aggregated results containing lattice constants, total energies, formation energies, magnetic moments, and electronic classification for all compounds."
    }
  ],
  "notes": "The checker recomputes relative/absolute deviations of numerical quantities against hidden paper‑reported values using threshold_or_better scoring, while the class field is compared exactly. The checker only validates the declared schema before scoring."
}
```

## How you are scored
A hidden verifier will independently check your submitted artifacts. It will:
1. Confirm that each required intermediate step has produced its expected evidence log.
2. Validate the structure and units of `computed_properties.json`.
3. Compare the numerical properties you report against independently known reference values, using appropriate tolerances for the DFT methodology.
4. Verify that the electronic classification matches the expected outcome based on the density-of-states analysis.

The verifier combines the per-stage scores (with the main weight on the computed properties) into a final reward between 0 and 1. Merely reporting numbers without performing the underlying DFT calculations will yield low or zero credit.
