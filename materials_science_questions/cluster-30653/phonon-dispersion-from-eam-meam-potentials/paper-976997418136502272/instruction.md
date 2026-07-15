# ACE potential fitting and binary Al-Li phase diagram validation

## Problem background
The development of machine learning interatomic potentials (MLPs) requires automated, reproducible workflows that span from reference data generation to fitting and thorough validation. A robust validation must go beyond energy/force errors and include physical properties such as elastic constants, phonon spectra, and thermodynamic phase diagrams. This task addresses the challenge of constructing such a workflow for a binary alloy system (Al-Li) and evaluating the predictive power of an atomic cluster expansion (ACE) potential for the binary phase diagram. The ultimate goal is to demonstrate that a fitted MLP can reproduce key features of the phase diagram—namely the eutectic point and solubility limits—derived entirely from first principles without fitting to experimental thermodynamic data.

## Approach
An ACE interatomic potential is fitted to a provided public density-functional theory (DFT) training dataset for Al-Li. The fitting employs a two-stage optimization with energy-based weighting to place higher emphasis on low-energy configurations. The fitted potential is then validated by computing phonon density-of-states (DOS) peak frequencies for fcc Al, bcc Li, AlLi, and Al₃Li using phonopy, and elastic constants (C₁₁, C₁₂, C₄₄) for fcc Al and bcc Li using LAMMPS. Subsequently, free energies of solid (fcc, B32 AlLi) and liquid phases are computed over a range of compositions (0 ≤ x_Li ≤ 0.5) and temperatures (600–1000 K) with the calphy package, which interfaces with LAMMPS for thermodynamic integration. Ideal mixing entropy is added to the solid phases, and common tangent constructions are performed on the free-energy curves to delineate phase boundaries. From these constructions, the eutectic temperature, the eutectic liquid composition (Li fraction), and the solubility of Li in fcc Al at the eutectic temperature are extracted.

## Reproduction target
Starting from the public Al-Li DFT training dataset, fit an ACE potential, then produce the following scored artifacts:

1. `validation_results.json`: phonon DOS main peak frequencies (in THz) for fcc Al, bcc Li, AlLi, and Al₃Li, and elastic constants C₁₁, C₁₂, C₄₄ (in GPa) for fcc Al and bcc Li.
2. `phase_diagram_features.json`: the eutectic temperature (in K), the eutectic liquid composition (Li atomic fraction), and the solubility of Li in fcc Al (atomic fraction) at the eutectic temperature.

The required output files, their formats, and the expected JSON schemas are specified in the workflow steps below.

## Assets

- pyiron: https://github.com/pyiron/pyiron
- pacemaker: https://github.com/ICAMS/python-ace
- calphy: https://github.com/ICAMS/calphy
- LAMMPS: https://github.com/lammps/lammps
- phonopy: https://github.com/phonopy/phonopy
- Al-Li DFT training dataset

## Workflow steps

### Step 1: ACE potential fitting
- Role: process
- Action: Using pyiron and pacemaker, fit an ACE potential to the provided Al-Li DFT training dataset following a two-stage optimization with energy-based weighting. Save the fitted potential file as ace_potential.yaml.
- Evidence: `/app/outputs/ace_potential.yaml`

### Step 2: Phonon DOS and elastic constant validation
- Role: scored (load-bearing)
- Action: With the fitted ACE potential, use LAMMPS to compute elastic constants C11, C12, C44 for fcc Al and bcc Li. Use phonopy to compute phonon density of states for fcc Al, bcc Li, AlLi, and Al3Li and extract main peak positions. Write results to validation_results.json.
- Output file: `/app/outputs/validation_results.json`
- Format: json
- Contract: {"phonon_peaks": {"fcc_Al": ["list of numbers"], "bcc_Li": ["list"], "AlLi": ["list"], "Al3Li": ["list"]}, "elastic_constants": {"Al_fcc": {"C11": "number", "C12": "number", "C44": "number"}, "Li_bcc": {"C11": "number", "C12": "number", "C44": "number"}}}
- Scoring: scored by hidden verifier

### Step 3: Free energy simulations for phase diagram
- Role: process
- Action: Using calphy with LAMMPS and the fitted ACE potential, run non-equilibrium thermodynamic integration and reversible scaling to compute free energies for fcc, liquid, and B32 AlLi phases at multiple compositions (0≤xLi≤0.5) and temperatures 600–1000 K. Store the computed free-energy data in free_energies.csv.
- Evidence: `/app/outputs/free_energies.csv`

### Step 4: Phase diagram feature extraction
- Role: scored (load-bearing)
- Action: From the free-energy data, add ideal mixing entropy for solid phases, perform common tangent constructions to determine phase boundaries, and extract the eutectic temperature, eutectic composition, and Li solubility in fcc Al at the eutectic. Write phase_diagram_features.json.
- Output file: `/app/outputs/phase_diagram_features.json`
- Format: json
- Contract: {"eutectic_temperature_K": "number", "eutectic_composition_Li_fraction": "number", "Li_solubility_in_fcc_Al_fraction": "number"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/validation_results.json`
- `/app/outputs/phase_diagram_features.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### validation_results.json
- path: `/app/outputs/validation_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phonon DOS peak positions (THz) and elastic constants (GPa) computed from the fitted ACE potential.
- schema:
  - `type`: object
  - `required`: `phonon_peaks`, `elastic_constants`
  - `properties`:
    - `phonon_peaks`:
      - `fcc_Al`: array
      - `bcc_Li`: array
      - `AlLi`: array
      - `Al3Li`: array
    - `elastic_constants`:
      - `Al_fcc`:
        - `C11`: number
        - `C12`: number
        - `C44`: number
      - `Li_bcc`:
        - `C11`: number
        - `C12`: number
        - `C44`: number

### phase_diagram_features.json
- path: `/app/outputs/phase_diagram_features.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Eutectic temperature (K), eutectic liquid Li fraction, and Li solubility in fcc Al at the eutectic temperature, extracted from common tangent constructions on the free-energy data.
- schema:
  - `type`: object
  - `required`: `eutectic_temperature_K`, `eutectic_composition_Li_fraction`, `Li_solubility_in_fcc_Al_fraction`
  - `properties`:
    - `eutectic_temperature_K`: number
    - `eutectic_composition_Li_fraction`: number
    - `Li_solubility_in_fcc_Al_fraction`: number

Notes: Scoring uses exact_match with tolerances against the paper's reference values. The hidden checker compares the reported numbers to the gold values within tolerances (elastic constants 20%, peak positions 1 THz, eutectic temperature 50 K, composition/solubility 0.05 fraction).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "validation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "phonon_peaks",
          "elastic_constants"
        ],
        "properties": {
          "phonon_peaks": {
            "fcc_Al": "array",
            "bcc_Li": "array",
            "AlLi": "array",
            "Al3Li": "array"
          },
          "elastic_constants": {
            "Al_fcc": {
              "C11": "number",
              "C12": "number",
              "C44": "number"
            },
            "Li_bcc": {
              "C11": "number",
              "C12": "number",
              "C44": "number"
            }
          }
        }
      },
      "description": "Phonon DOS peak positions (THz) and elastic constants (GPa) computed from the fitted ACE potential."
    },
    {
      "file": "phase_diagram_features.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "eutectic_temperature_K",
          "eutectic_composition_Li_fraction",
          "Li_solubility_in_fcc_Al_fraction"
        ],
        "properties": {
          "eutectic_temperature_K": "number",
          "eutectic_composition_Li_fraction": "number",
          "Li_solubility_in_fcc_Al_fraction": "number"
        }
      },
      "description": "Eutectic temperature (K), eutectic liquid Li fraction, and Li solubility in fcc Al at the eutectic temperature, extracted from common tangent constructions on the free-energy data."
    }
  ],
  "notes": "Scoring uses exact_match with tolerances against the paper's reference values. The hidden checker compares the reported numbers to the gold values within tolerances (elastic constants 20%, peak positions 1 THz, eutectic temperature 50 K, composition/solubility 0.05 fraction)."
}
```

## How you are scored
A hidden verifier will read `validation_results.json` and `phase_diagram_features.json` and compare the reported numerical values to hidden reference targets. Each scored artifact is evaluated independently, and a weighted combination yields your final reward. Reporting numbers that merely match the reference without genuinely executing the pipeline will not be sufficient—the verifier expects the values to be the result of a correct computational workflow. The verifier does not reveal the reference values or the exact tolerances ahead of time, but rewards accuracy: the closer your computed quantities are to the expected values, the higher your score, provided they fall within acceptable margins.
