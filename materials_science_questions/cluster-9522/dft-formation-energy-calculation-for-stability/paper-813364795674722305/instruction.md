# DFT Screening of B2 Stabilizers in Cu-Pd-M Alloys

## Problem background
Hydrogen separation membranes require alloy materials that combine high hydrogen permeability with resistance to embrittlement and poisoning. Cu-Pd alloys with an ordered B2 (bcc) structure are among the most promising candidates because the open bcc lattice facilitates faster hydrogen diffusion compared to the fcc phase. However, the binary B2 phase is stable only over a limited composition and temperature range. Alloying with a third element M can stabilize the B2 structure, potentially expanding the phase field to lower Pd contents and higher temperatures. The challenge is to identify which alloying elements are effective B2 stabilizers. This task uses first‑principles density functional theory (DFT) to compute the formation enthalpy of hypothetical B2 Cu₈Pd₈₋ₓMₓ compositions for a set of candidate elements M. The computed formation enthalpy will indicate whether a given element energetically favours the B2 phase relative to the constituent pure elements.

## Approach
The screening procedure is based on the idea that a negative formation enthalpy (ΔHf < 0) implies thermodynamic stabilisation of the compound with respect to the pure elements. The approach uses plane‑wave DFT to compute the total energies of 2×2×2 B2 supercells. Starting from the ordered CuPd B2 structure, a supercell of 16 atoms (Cu₈Pd₈) is built. For each candidate alloying element M, one Pd atom is replaced to obtain a ternary Cu₈Pd₇M₁ supercell. Total energies per atom are obtained after full relaxation of atomic positions and cell volume at zero pressure. Cohesive energies of the pure elements (Cu, Pd, and each M) in their ground‑state reference structures are computed with the same DFT settings. The formation enthalpy per atom for each compound is then calculated as ΔHf = E_coh(compound) − Σ cᵢ·E_coh(elementᵢ), where cᵢ are the atomic fractions. A negative value for the ternary composition indicates that the B2 phase is stabilised by that alloying element under the purely energetic (zero‑temperature, no configurational entropy) assumptions. The calculation uses open‑source plane‑wave DFT with PAW pseudopotentials and the PBE exchange‑correlation functional, with a plane‑wave cutoff and k‑point sampling sufficient for convergence to ~1 meV/atom.

## Reproduction target
Produce a CSV file, `formation_enthalpies.csv`, that contains the formation enthalpy per atom (in eV/atom) for each composition. The file must include a row for the binary Cu₈Pd₈ (with M = 'None' and x = 0) and one row for each ternary composition Cu₈Pd₇M₁ (with M = Sc, Ti, Zn, Y, Zr, Hf, La, Al, Mg and x = 1). The columns are: `M_element` (string), `x` (integer, 0 or 1), and `Delta_Hf` (float, eV/atom). The computed enthalpies will be used to judge which alloying elements, if any, yield a negative formation enthalpy, thereby identifying strong B2 stabilizers.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase

## Workflow steps

### Step 1: Generate B2 supercell structures
- Role: process
- Action: Construct a 2×2×2 B2 supercell of CuPd to obtain Cu8Pd8. For each alloying element M in [Sc, Ti, Zn, Y, Zr, Hf, La, Al, Mg], substitute one Pd atom with M to create Cu8Pd7M1 structures. Save structure files for subsequent DFT calculations.
- Evidence: none

### Step 2: Compute elemental reference cohesive energies
- Role: process
- Action: For pure Cu, Pd, and each M (Sc, Ti, Zn, Y, Zr, Hf, La, Al, Mg), set up the ground-state bulk crystal structure and perform a DFT total-energy calculation using a plane-wave pseudopotential code (Quantum ESPRESSO with SSSP PBE pseudopotentials). Converge with respect to plane-wave cutoff and k-point mesh to ~1 meV/atom, fully relax atomic positions and cell volume at zero pressure. Extract the cohesive energy per atom for each element.
- Evidence: `/app/outputs/elemental_energies.csv`

### Step 3: Compute alloy supercell total energies
- Role: process
- Action: For each supercell (Cu8Pd8 and the nine Cu8Pd7M1 structures), perform full relaxation (atomic positions, cell parameters, volume) using the same DFT settings as the elemental calculations. Extract the total energy per atom after relaxation.
- Evidence: `/app/outputs/alloy_energies.csv`

### Step 4: Calculate formation enthalpies
- Role: scored (load-bearing)
- Action: Calculate the formation enthalpy per atom ΔHf = E_coh(compound) − Σc_i·E_coh(element_i) using the computed cohesive energies of the pure elements and the total energies per atom of the alloy supercells. For Cu8Pd8, c_Cu=0.5, c_Pd=0.5; for Cu8Pd7M1, c_Cu=0.5, c_Pd=7/16, c_M=1/16. Write a CSV file with columns M_element, x, Delta_Hf. Include a row for the binary (M='None', x=0) and one row per M at x=1.
- Output file: `/app/outputs/formation_enthalpies.csv`
- Format: csv
- Contract: columns: M_element (string), x (integer, 0 or 1), Delta_Hf (float, eV/atom)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_enthalpies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_enthalpies.csv
- path: `/app/outputs/formation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Formation enthalpy per atom for each B2 composition. The hidden checker will use the sign of Delta_Hf to assess which alloying elements stabilize the B2 phase.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `M_element`, `x`, `Delta_Hf`
  - `units`:
    - `Delta_Hf`: eV/atom

Notes: The scorer will verify that the listed alloying elements produce a negative formation enthalpy, in agreement with the paper's identification of B2 stabilizers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "M_element",
          "x",
          "Delta_Hf"
        ],
        "units": {
          "Delta_Hf": "eV/atom"
        }
      },
      "description": "Formation enthalpy per atom for each B2 composition. The hidden checker will use the sign of Delta_Hf to assess which alloying elements stabilize the B2 phase."
    }
  ],
  "notes": "The scorer will verify that the listed alloying elements produce a negative formation enthalpy, in agreement with the paper's identification of B2 stabilizers."
}
```

## How you are scored
A hidden verifier will read your output files and independently score them. For `formation_enthalpies.csv`, the verifier checks that the formation enthalpy for the binary and for each alloying element at x = 1 has the correct sign, and optionally verifies that the absolute values fall within a physically reasonable range. The final reward is the fraction of these checks that pass. The verifier uses its own hidden reference derived from the paper's reported results; it does not rely on you reporting a particular number. The numerical values must be the outcome of a genuine DFT workflow — fabrication will not match the hidden expectations.
