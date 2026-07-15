# Phonon-Driven Topological Phase Transition in ZrTe5 from DFT

## Problem background
ZrTe5 is a layered van der Waals material that sits near the topological phase boundary between a strong topological insulator (STI) and a weak topological insulator (WTI). Small lattice distortions that preserve the crystal symmetry can switch the system between these two topological phases. In particular, atomic displacements along certain A_g Raman-active phonon modes may drive a STI–WTI transition, which is marked by the closing and reopening of the band gap at the Γ point and a change in the Z2 topological invariant. This task computes the equilibrium spin‑orbit coupling (SOC) band gap of ZrTe5 and then follows how the band gap and topological phase evolve when the crystal is displaced along the normal coordinates of six specific A_g phonon modes. The goal is to determine which of these symmetry‑preserving modes can trigger a topological phase transition, and to map the resulting phase diagram in the space of two selected modes.

## Approach
The calculations use density functional theory (DFT) with spin‑orbit coupling, implemented through the open‑source Quantum ESPRESSO package. The workflow proceeds in several stages. First, the crystal structure of ZrTe5 (space group Cmcm) is relaxed to obtain the equilibrium geometry. Next, phonon frequencies and eigenvectors are computed at the Γ point to identify the six A_g Raman‑active modes; these modes preserve the space‑group symmetry and involve specific displacement patterns of the Zr and Te atoms. Using the normal‑mode eigenvectors, a series of distorted structures is generated: for each A_g mode, atomic positions are displaced along the mode’s normal coordinate Q over the range −0.6 to 0.3 (dimensionless units, step size ≤ 0.1); additionally, a two‑dimensional grid of structures is created in which the A_g‑27 and A_g‑31 modes are varied simultaneously. For every structure (equilibrium and distorted) a DFT+SOC electronic‑structure calculation is performed, from which the fundamental band gap at the Γ point is extracted and the topological phase (STI or WTI) is determined via the Z2 invariant or the presence of a band inversion. All required inputs—crystal structure (CIF), pseudopotentials (SSSP PBEsol), and the DFT code—are publicly available.

## Reproduction target
The objective is to produce three numerical artifacts from first‑principles DFT+SOC calculations. No pre‑computed models or fitted parameters are provided.

1. `equilibrium_gap.txt`: a single floating‑point number (in eV) giving the SOC band gap at the Γ point for the fully relaxed ZrTe5 structure.
2. `band_gap_vs_Q.csv`: a CSV table covering all six A_g modes (labelled Ag6, Ag22, Ag25, Ag27, Ag29, Ag36). Each row lists the mode name, the normal coordinate Q (float), the band gap (meV), and the topological phase (string "STI" or "WTI"). The Q range must span at least −0.6 to 0.3 with steps no larger than 0.1; finer sampling is encouraged near any gap closure.
3. `phase_diagram_2D.csv`: a CSV table for a two‑dimensional grid of (Q27, Q31) values, with columns Q27 (float), Q31 (float), gap_meV (float), and topological_phase (string "STI" or "WTI"). Each coordinate is sampled over the same range as above with at least 7×7 distinct points.

## Assets

- Quantum ESPRESSO (pw.x, ph.x): https://www.quantum-espresso.org/
- ZrTe5 crystal structure (CIF): https://www.crystallography.net/cod/
- Pseudopotentials for Zr and Te (SSSP PBEsol): https://www.materialscloud.org/discover/sssp/table/efficiency
- Z2Pack or parity-based Z2 routine: https://z2pack.github.io/

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Relax the crystal structure of ZrTe5 (space group Cmcm) using DFT to obtain equilibrium lattice parameters and atomic positions.
- Evidence: `/app/outputs/relax.out`

### Step 2: Phonon calculation at Γ
- Role: process
- Action: Using DFPT or finite displacements on the relaxed structure, compute phonon frequencies and eigenvectors at the Γ point, identifying the six Ag Raman-active modes and their atomic displacement vectors.
- Evidence: `/app/outputs/phonon.txt`

### Step 3: Generate distorted structures along Ag normal coordinates
- Role: process
- Action: For each of the six Ag modes, generate atomic geometries with displacements along the normal coordinate Q in the range -0.6 to 0.3 (step no larger than 0.1). Also produce a 2D grid of structures for combinations of Q27 and Q31 covering the same range (at least 7x7 points).
- Evidence: none

### Step 4: Equilibrium SOC band gap
- Role: scored
- Action: Perform a DFT electronic structure calculation with spin-orbit coupling on the relaxed equilibrium structure; extract the fundamental band gap at the Γ point and write it to equilibrium_gap.txt.
- Output file: `/app/outputs/equilibrium_gap.txt`
- Format: txt
- Contract: A text file containing a single floating-point number on the first line (unit: eV).
- Scoring: scored by hidden verifier

### Step 5: Band gap and topological phase vs Q for all Ag modes
- Role: scored (load-bearing)
- Action: For every distorted structure generated in step3 (all six Ag modes, full Q range), run a DFT+SOC band calculation; extract the Γ-point band gap and determine the topological phase (STI or WTI) using the Z2 invariant or a clear band inversion indicator. Output the results as a CSV.
- Output file: `/app/outputs/band_gap_vs_Q.csv`
- Format: csv
- Contract: CSV with columns: mode_name (string, e.g. Ag6, Ag22, Ag25, Ag27, Ag29, Ag36), Q (float, dimensionless normal coordinate), gap_meV (float, positive number, meV), topological_phase (string, either 'STI' or 'WTI').
- Scoring: scored by hidden verifier

### Step 6: 2D phase diagram for A_g-27 and A_g-31
- Role: scored
- Action: For the 2D grid of (Q27, Q31) structures from step3, compute the Γ-point band gap and topological phase; output a CSV.
- Output file: `/app/outputs/phase_diagram_2D.csv`
- Format: csv
- Contract: CSV with columns: Q27 (float), Q31 (float), gap_meV (float), topological_phase (string, 'STI' or 'WTI').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_gap.txt`
- `/app/outputs/band_gap_vs_Q.csv`
- `/app/outputs/phase_diagram_2D.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_gap.txt
- path: `/app/outputs/equilibrium_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium SOC band gap at the Γ point of ZrTe5.
- schema:
  - `type`: text
  - `required`:
    - `value`: float in eV

### band_gap_vs_Q.csv
- path: `/app/outputs/band_gap_vs_Q.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Evolution of the Γ-point band gap and topological phase as a function of the normal coordinate Q for each of the six Ag phonon modes.
- schema:
  - `type`: table
  - `required_columns`: `mode_name`, `Q`, `gap_meV`, `topological_phase`
  - `units`:
    - `gap_meV`: meV

### phase_diagram_2D.csv
- path: `/app/outputs/phase_diagram_2D.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Two-dimensional phase diagram (gap and topological phase) on a grid of (A_g-27, A_g-31) normal coordinate values.
- schema:
  - `type`: table
  - `required_columns`: `Q27`, `Q31`, `gap_meV`, `topological_phase`
  - `units`:
    - `gap_meV`: meV

Notes: All outputs are computed from first-principles DFT with spin-orbit coupling. The checker compares the submitted results to hidden gold references derived from the paper's reported quantities, with tolerances appropriate for DFT code-to-code variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "value": "float in eV"
        }
      },
      "description": "Equilibrium SOC band gap at the Γ point of ZrTe5."
    },
    {
      "file": "band_gap_vs_Q.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_name",
          "Q",
          "gap_meV",
          "topological_phase"
        ],
        "units": {
          "gap_meV": "meV"
        }
      },
      "description": "Evolution of the Γ-point band gap and topological phase as a function of the normal coordinate Q for each of the six Ag phonon modes."
    },
    {
      "file": "phase_diagram_2D.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Q27",
          "Q31",
          "gap_meV",
          "topological_phase"
        ],
        "units": {
          "gap_meV": "meV"
        }
      },
      "description": "Two-dimensional phase diagram (gap and topological phase) on a grid of (A_g-27, A_g-31) normal coordinate values."
    }
  ],
  "notes": "All outputs are computed from first-principles DFT with spin-orbit coupling. The checker compares the submitted results to hidden gold references derived from the paper's reported quantities, with tolerances appropriate for DFT code-to-code variation."
}
```

## How you are scored
A hidden verifier inspects each output artefact against the required schema and a set of hidden reference criteria derived from the underlying physical behavior (the checker holds the expected results but does not reveal them).

- For `equilibrium_gap.txt`, the verifier compares the reported value with the expected equilibrium SOC gap; a value within a reasonable margin earns full credit.
- For `band_gap_vs_Q.csv`, the verifier examines whether the gap‑versus‑Q curve for each mode shows gap closing (the gap drops to a very small value at some Q) and whether the topological phase changes between STI and WTI at the closing point. It also checks that the mode(s) that do not close the gap are correctly identified. The reward depends on matching the observed pattern of gap closures and phase flips, and on the approximate location of any gap minimum.
- For `phase_diagram_2D.csv`, the verifier evaluates the shape of the boundary line separating STI and WTI regions and compares the zero‑gap line to a hidden linear reference.
- Structural requirements: the output files must have the exact columns, units (gap in meV), and phase labels specified in the contract. Missing or malformed columns reduce credit.
The final reward is a weighted combination of these checks, with `band_gap_vs_Q.csv` carrying the largest weight because it directly tests the main scientific claim. You must execute the DFT calculations yourself; merely reporting numbers without running the simulations will not satisfy the hidden checks (e.g., gap‑closing positions and phase flips are verified against undisclosed patterns).
