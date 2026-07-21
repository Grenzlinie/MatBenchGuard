# Double-layer ice relative enthalpies at confinement width 9.5 Å

## Problem background
Two-dimensional ice confined between graphene sheets exhibits rich polymorphism. Several candidate crystal structures—hexagonal, hexagonal-close-packed (HCP), square-tube, square, and buckled-rhombic—have been proposed for double-layer ice. First-principles density functional theory (DFT) calculations can determine the relative stability of these phases at 0 K by comparing their enthalpies as functions of lateral pressure and confinement width. This task asks you to compute those relative enthalpies for a confinement width of 9.5 Å, using a plane-wave DFT code that includes a van der Waals functional and a confining Morse potential that models the interaction with the confining walls. The resulting data allow one to infer which solid phases are thermodynamically stable under which pressure conditions.

## Approach
You will perform DFT geometry optimisations for five double-layer ice structures (hexagonal, HCP, square-tube, square, buckled-rhombic) at a fixed confinement width w = 9.5 Å. The confining effect of the walls is described by a Morse potential V(z) = D ((1 − e^{−a (z − z₀)})² − 1) applied to each oxygen atom, with parameters D = 57.8 meV, a = 0.92 Å⁻¹, z₀ = 3.85 Å. For each structure you will optimise the in-plane cell at lateral pressures P = 0, 1, 2, 3, 4, 5 GPa, keeping the out-of-plane lattice vector fixed. Choose an open-source plane-wave DFT code that supports a van der Waals inclusive exchange‑correlation functional (e.g. the vdW‑DF2 / rPW86‑vdW2 family). For each converged optimization, compute the enthalpy H = E_ice^tot + E_confinement + P × A × h, where E_confinement is the energy from the Morse potential, A is the lateral area, and h = w = 9.5 Å (the layer height equals the confinement width). Finally, for every pressure, calculate the enthalpy of each structure relative to the square‑tube structure at the same pressure. Structures that become mechanically unstable at higher pressures (as indicated by imaginary phonon modes or very large distortions) may be omitted. The workflow must be repeated for all four non‑tube structures (hexagonal, HCP, square, buckled‑rhombic) so that the output contains the relative enthalpies at each feasible pressure.

## Reproduction target
Produce a CSV file named relative_enthalpies.csv with the following columns: pressure_GPa (float), structure (string: one of hexagonal, HCP, square, buckled‑rhombic), and relative_enthalpy_meV_per_H2O (float). The relative enthalpy is the difference between the enthalpy of the listed structure and the enthalpy of the square‑tube structure at the same pressure, expressed in meV per H₂O molecule. Include rows for at least pressures 0, 1, 2, 3, 4, 5 GPa for each of the four non‑tube structures, omitting any combination that proved mechanically unstable (e.g., hexagonal and square are expected to become unstable above roughly 1 GPa; such rows may be absent). The square‑tube structure is the reference and must not appear in the file. Row order does not matter.

## Assets

- Double-layer ice initial structure files (from paper's supplemental material): https://arxiv.org/abs/1703.03670
- Plane-wave DFT code with van der Waals functional (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org
- Pseudopotential library (e.g., SSSP efficiency for Quantum ESPRESSO): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Compute relative enthalpies of double-layer ice structures
- Role: scored (load-bearing)
- Action: For each double-layer ice structure (hexagonal, HCP, square, buckled-rhombic) at confinement width w = 9.5 Å, perform DFT geometry optimisations at lateral pressures P = 0, 1, 2, 3, 4, 5 GPa using a plane-wave code with a van der Waals functional. Apply the confining Morse potential V(z)=D((1-e^{-a(z-z₀)})²-1) with D=57.8 meV, a=0.92 Å⁻¹, z₀=3.85 Å. Compute enthalpy H = E_ice^tot + E_confinement + P×A×h, with h=w=9.5 Å. For each pressure, calculate the relative enthalpy of every structure with respect to square-tube. Write the results to relative_enthalpies.csv. Omit rows for structures that become mechanically unstable (e.g., hexagonal and square above ~1 GPa).
- Output file: `/app/outputs/relative_enthalpies.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), structure (string: hexagonal, HCP, square, buckled-rhombic), relative_enthalpy_meV_per_H2O (float). Excludes square-tube (reference with relative enthalpy 0). Row order does not matter.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_enthalpies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_enthalpies.csv
- path: `/app/outputs/relative_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Relative enthalpies of double‑layer ice structures with respect to square‑tube at confinement width 9.5 Å and lateral pressures 0, 1, 2, 3, 4, 5 GPa. The hidden verifier checks thermodynamic stability trends and a key energy difference.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `structure`, `relative_enthalpy_meV_per_H2O`
  - `column_types`:
    - `pressure_GPa`: float
    - `structure`: string
    - `relative_enthalpy_meV_per_H2O`: float

Notes: Scored by a hidden verifier that checks thermodynamic stability trends and a key energy difference. Tolerances accommodate legitimate implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "structure",
          "relative_enthalpy_meV_per_H2O"
        ],
        "column_types": {
          "pressure_GPa": "float",
          "structure": "string",
          "relative_enthalpy_meV_per_H2O": "float"
        }
      },
      "description": "Relative enthalpies of double‑layer ice structures with respect to square‑tube at confinement width 9.5 Å and lateral pressures 0, 1, 2, 3, 4, 5 GPa. The hidden verifier checks thermodynamic stability trends and a key energy difference."
    }
  ],
  "notes": "Scored by a hidden verifier that checks thermodynamic stability trends and a key energy difference. Tolerances accommodate legitimate implementation spread."
}
```

## How you are scored
A hidden verifier will load relative_enthalpies.csv and perform two independent checks: (1) It compares the pattern of relative enthalpies at each pressure to the expected thermodynamic stability ordering — i.e., it verifies whether the structure with the lowest enthalpy at a given pressure matches the correct stable phase according to the published first‑principles phase diagram. (2) It applies a threshold condition on the enthalpy difference between the square and square‑tube structures at a pressure of 1 GPa. The verifier tolerates small absolute shifts in enthalpy that arise from different DFT implementations; the primary weight is on the correct ordering of phases (trend) and the threshold comparison. Your final reward is a weighted combination of these two evaluations.
