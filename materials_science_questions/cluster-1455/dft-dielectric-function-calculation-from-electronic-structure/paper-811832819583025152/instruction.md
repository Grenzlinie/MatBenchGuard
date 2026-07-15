# DFT property reproduction for chalcogenide phase-change materials

## Problem background
Chalcogenide phase-change materials based on pseudobinary compounds of GeTe and Sb2Te3 are central to rewritable optical storage and emerging non-volatile memory technologies. A key to device optimization is understanding how the electronic band structure and optical properties vary across composition and crystalline phase. Density functional theory (DFT) can predict band gaps, dielectric constants, and critical-point energies—quantities that directly affect optical contrast and electronic transport. This task focuses on the DFT-calculated properties of five compositions: GeTe, Ge2Sb2Te5, Ge1Sb2Te4, Ge1Sb4Te7, and Sb2Te3, in their metastable rocksalt-like and stable hexagonal/rhombohedral crystalline phases. The goal is to compute the indirect band gap, minimum direct band gap, static dielectric constant, and (for GeTe) the critical-point energies, providing a systematic picture of the electronic and optical properties of these materials.

## Approach
The computational approach uses planewave density functional theory within the generalized gradient approximation (GGA-PBE). You will build crystal structures for each composition and phase using publicly reported lattice parameters and atomic positions, and optionally relax the geometries to minimize forces and stresses. Starting from the relaxed structures, perform self-consistent DFT calculations, then band-structure calculations along high-symmetry directions, and compute the frequency-dependent dielectric function. The imaginary part of the dielectric function is obtained from momentum matrix elements between occupied and empty bands; the real part is derived via the Kramers‑Kronig relation. From these outputs, extract (i) the indirect band gap—the smallest energy difference between the valence band maximum and conduction band minimum when they occur at different k-points, (ii) the minimum direct band gap (same‑k‑point smallest energy difference), and (iii) the static dielectric constant ε∞, defined as the zero-energy limit of the real part of the dielectric function. For GeTe, additionally identify the critical-point energies from the band structure, i.e., energies where the joint density of states shows Van Hove singularities. All calculations can be carried out with open‑source DFT codes such as Quantum ESPRESSO, using pseudopotentials from standard libraries.

## Reproduction target
For each of the five compositions (GeTe, Ge2Sb2Te5, Ge1Sb2Te4, Ge1Sb4Te7, Sb2Te3) and for both the metastable rock-salt crystalline phase and the stable hexagonal/rhombohedral crystalline phase (where that phase exists), compute and record the following quantities in a single JSON file named dft_results.json:

- indirect band gap (eV)
- minimum direct band gap (eV)
- static dielectric constant (dimensionless)
- for GeTe only, a list of critical-point energies (eV) derived from the band structure

All values must be reported as numbers (float for scalar quantities, array of floats for critical-point energies). The file schema must exactly match the output contract specified below: a top‑level "compositions" array containing objects with fields "name", "phase" ("stable" or "metastable"), "band_gap_indirect", "band_gap_direct_min", "static_dielectric_constant", and "critical_point_energies".

## Assets

- Crystal structures for GST compounds (metastable and stable phases): 10.1103/PhysRevB.78.224111
- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org
- Pseudopotentials for Ge, Sb, Te (PBE): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Run DFT calculations for crystalline GST phases
- Role: process
- Action: Using the obtained crystal structures for the five compositions (GeTe, Ge2Sb2Te5, Ge1Sb2Te4, Ge1Sb4Te7, Sb2Te3) and their metastable rock-salt (where applicable) and stable hexagonal/rhombohedral crystalline phases, perform planewave DFT calculations (e.g., with Quantum ESPRESSO or another open-source code) to compute electronic band structures and frequency-dependent dielectric functions. Compute the imaginary part of the dielectric function from momentum matrix elements and derive the real part via Kramers-Kronig relations.
- Evidence: `/app/outputs/dft_run.log`

### Step 2: Extract target quantities from DFT outputs
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract for every composition and phase: the indirect band gap (eV), the minimum direct band gap (eV), and the static dielectric constant (ε∞, zero-energy limit of the real part of the dielectric function). For GeTe, additionally extract the critical-point energies (list of eV, derived from the band structure). Write all results into dft_results.json following the declared output schema.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"compositions": [{"name": "string", "phase": "stable"|"metastable", "band_gap_indirect": float, "band_gap_direct_min": float, "static_dielectric_constant": float, "critical_point_energies": [float]}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compilation of DFT-computed electronic and optical properties for GST compounds. The checker will verify band gaps within 0.1 eV, dielectric constants within 10% relative, and critical-point energies within 0.2 eV against the paper's reported DFT results.
- schema:
  - `type`: object
  - `required`:
    - `compositions`: array of objects
  - `items`:
    - `name`: string (compound identifier)
    - `phase`: string (stable or metastable)
    - `band_gap_indirect`: float (eV)
    - `band_gap_direct_min`: float (eV)
    - `static_dielectric_constant`: float (dimensionless)
    - `critical_point_energies`: array of float (eV; may be empty for compositions where not required)

Notes: The DFT runs are resource-intensive and may require GPU or cluster resources. The agent is expected to run the calculations and produce the output file; the hidden grader compares it to the paper's tabulated values with defined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compositions": "array of objects"
        },
        "items": {
          "name": "string (compound identifier)",
          "phase": "string (stable or metastable)",
          "band_gap_indirect": "float (eV)",
          "band_gap_direct_min": "float (eV)",
          "static_dielectric_constant": "float (dimensionless)",
          "critical_point_energies": "array of float (eV; may be empty for compositions where not required)"
        }
      },
      "description": "Compilation of DFT-computed electronic and optical properties for GST compounds. The checker will verify band gaps within 0.1 eV, dielectric constants within 10% relative, and critical-point energies within 0.2 eV against the paper's reported DFT results."
    }
  ],
  "notes": "The DFT runs are resource-intensive and may require GPU or cluster resources. The agent is expected to run the calculations and produce the output file; the hidden grader compares it to the paper's tabulated values with defined tolerances."
}
```

## How you are scored
A hidden verifier will independently read your dft_results.json file and compare each reported quantity against a set of reference values derived from the original DFT calculations. The verifier checks that you have provided entries for all required composition‑phase pairs and that every numeric field is present. Each quantity is then evaluated for agreement with the reference; partial credit is assigned according to a predefined rubric. The verifier also verifies that the file is well‑formed according to the output schema. All partial scores are combined into a final reward between 0 and 1. Simply reporting numbers without carrying out the required computational steps is not sufficient; the verifier may also examine the evidence of the DFT run (e.g., log file) to confirm that the full workflow was executed.
