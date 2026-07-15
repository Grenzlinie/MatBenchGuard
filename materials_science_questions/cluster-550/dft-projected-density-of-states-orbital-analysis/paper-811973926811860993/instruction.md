# Layer-Resolved Density of States Analysis of Thiolate on Pt(111) by DFT

## Problem background
When thiols chemisorb on Pt(111), the sulfur 3p states hybridize with the platinum 5d bands, forming interface states that can be metallic near the S–Pt bond and insulating farther away along the alkyl chain. Understanding how the local density of states (LDOS) varies with distance from the surface—including the existence of empty acceptor states just above the Fermi level—is important for interpreting charge transport in molecule–metal junctions. This task targets a first-principles calculation that reveals that spatial electronic structure.

## Approach
Use density functional theory (DFT) with the generalized gradient approximation (PBE functional) as implemented in an open-source plane‑wave code. Model a six‑layer Pt(111) slab with a (√3×√3)R30° in‑plane supercell and sufficient vacuum. Place a methanethiolate (CH3S) adsorbate on a bridge site and relax the top three Pt layers together with the thiolate. On the relaxed geometry, perform a self‑consistent field calculation to obtain the Kohn–Sham eigenvalues and wavefunctions, then project the density of states onto the Pt, S, and outermost C atomic layers. The resulting layer‑resolved LDOS as a function of energy provides the desired spatial electronic profile.

## Reproduction target
Compute the layer‑resolved density of states (LDOS) for methanethiolate (CH3S) on Pt(111) in the energy range –5 to +5 eV relative to the Fermi level. Use DFT to relax the adsorption geometry and project the DOS onto atomic layers. The verifier will evaluate the resulting LDOS and geometry against a set of hidden checks; no expected site, tilt angle, or layer-character assignments are stated here.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE for Pt, S, C, H): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Slab model construction
- Role: process
- Action: Build a Pt(111) slab with six atomic layers, a (√3×√3)R30° in-plane supercell, and a vacuum of 14.4 Å. Place methanethiolate (CH3S) on the bridge site with initial S–C bond tilted ~50° from the surface normal. Output the initial structure.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: DFT geometry optimization
- Role: scored
- Action: Relax the atomic positions of the top three Pt layers and the thiolate using DFT (PBE functional, appropriate pseudopotentials) until forces converge. Extract the final adsorption site, S–C tilt angle, and total energy.
- Output file: `/app/outputs/geometry_summary.json`
- Format: json
- Contract: {"adsorption_site": "string", "sc_tilt_angle_deg": "number", "total_energy_eV": "number"}
- Scoring: scored by hidden verifier

### Step 3: DFT electronic structure SCF
- Role: process
- Action: Perform a self-consistent field calculation on the optimized geometry using the same DFT functional and pseudopotentials to obtain the Kohn–Sham eigenvalues and wavefunctions.
- Evidence: none

### Step 4: Layer-resolved DOS analysis
- Role: scored (load-bearing)
- Action: Project the density of states onto Pt, S, and C atomic layers using the wavefunctions. Integrate over -5 to +5 eV relative to the Fermi level and output a CSV file with layer-resolved LDOS (states/eV).
- Output file: `/app/outputs/ldos_CH3S.csv`
- Format: csv
- Contract: Columns: energy (eV, Fermi level at 0), LDOS_Pt (states/eV), LDOS_S (states/eV), LDOS_C (states/eV). One row per energy grid point with step ≤ 0.05 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometry_summary.json`
- `/app/outputs/ldos_CH3S.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometry_summary.json
- path: `/app/outputs/geometry_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Geometric properties of the relaxed adsorption structure.
- schema:
  - `type`: object
  - `required`:
    - `adsorption_site`: string
    - `sc_tilt_angle_deg`: number
    - `total_energy_eV`: number
  - `description`: Final adsorption site, S–C tilt angle relative to surface normal, and total energy

### ldos_CH3S.csv
- path: `/app/outputs/ldos_CH3S.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Layer-resolved density of states around the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `LDOS_Pt`, `LDOS_S`, `LDOS_C`
  - `units`:
    - `energy`: eV
    - `LDOS_Pt`: states/eV
    - `LDOS_S`: states/eV
    - `LDOS_C`: states/eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometry_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "adsorption_site": "string",
          "sc_tilt_angle_deg": "number",
          "total_energy_eV": "number"
        },
        "description": "Final adsorption site, S–C tilt angle relative to surface normal, and total energy"
      },
      "description": "Geometric properties of the relaxed adsorption structure."
    },
    {
      "file": "ldos_CH3S.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "LDOS_Pt",
          "LDOS_S",
          "LDOS_C"
        ],
        "units": {
          "energy": "eV",
          "LDOS_Pt": "states/eV",
          "LDOS_S": "states/eV",
          "LDOS_C": "states/eV"
        }
      },
      "description": "Layer-resolved density of states around the Fermi level."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently inspect your scored artifacts—the geometry summary (`geometry_summary.json`) and the LDOS table (`ldos_CH3S.csv`). The verifier checks geometric properties (adsorption site, tilt angle) and electronic characteristics (LDOS around the Fermi level, presence of empty states) against internal criteria that are not disclosed. Each check carries a weight, and the verifier combines them into a final reward between 0 and 1. Merely reporting plausible numbers is not sufficient; your generated files must pass these hidden checks.
