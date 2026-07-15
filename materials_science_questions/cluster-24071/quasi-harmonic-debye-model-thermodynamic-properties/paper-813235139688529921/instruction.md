# DFT calculation of elastic constants and band gap of cubic KTaO3

## Problem background
The perovskite KTaO3 adopts a cubic structure at room temperature and exhibits interesting elastic and electronic characteristics. First-principles computational methods can predict structural, elastic, and electronic properties that are difficult to measure directly. Reproducing such calculations with open-source density functional theory (DFT) tools validates the methodology and provides robust predictions of material properties.

## Approach
The approach employs plane-wave pseudopotential density functional theory (DFT) with the generalized gradient approximation. Structural and elastic calculations use the Perdew-Burke-Ernzerhof (PBE) functional. The electronic band structure uses the Engel-Vosko (EV) GGA functional, which improves band gap predictions. The workflow comprises three main stages: (1) Determine the equilibrium lattice constant and bulk modulus by computing total energies for a set of unit cell volumes and fitting the energy–volume data to the Murnaghan equation of state. (2) Compute the three independent cubic elastic constants C11, C12, and C44 by applying volume-conserving orthorhombic and monoclinic strain tensors to the equilibrium unit cell and fitting the quadratic energy–strain relations; the bulk modulus from stage 1 combines with the fitted coefficients to yield individual C11 and C12. (3) Compute the electronic band structure at the equilibrium volume to obtain the indirect band gap from the valence band maximum at the R point to the conduction band minimum at the Γ point.

## Reproduction target
Compute the elastic constants C11, C12, C44 (in GPa) and the indirect electronic band gap (in eV) of cubic KTaO3 using the DFT workflow described above. Report the results in two JSON files: `elastic_constants.json` containing the equilibrium lattice constant, bulk modulus, and the three elastic constants, and `band_gap.json` containing the band gap value and the transition type.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Pseudopotentials for K, Ta, O (PBE): https://www.quantum-espresso.org/pseudopotentials
- Python packages (numpy, scipy, matplotlib): pip

## Workflow steps

### Step 1: Equilibrium structure and Murnaghan EOS fitting
- Role: process
- Action: Perform DFT total-energy calculations for cubic KTaO3 at a set of volumes around the experimental lattice constant using the GGA-PBE functional. Fit the energy-volume data to the Murnaghan equation of state to obtain the equilibrium lattice constant, bulk modulus, and its pressure derivative. Save the energy-volume pairs to energy_volume.csv.
- Evidence: `/app/outputs/energy_volume.csv`

### Step 2: Compute elastic constants C11, C12, C44
- Role: scored (load-bearing)
- Action: Using the equilibrium lattice constant from the previous step, apply volume-conserving orthorhombic and monoclinic strain tensors to the cubic unit cell. Perform DFT energy calculations for strain amplitudes δ = 0.01, 0.03, 0.05 for each strain type. Fit the quadratic energy-strain relations to extract C11−C12 and C44, then combine with the bulk modulus B0 to obtain individual C11 and C12. Report the elastic constants and the structural parameters (equilibrium lattice constant, bulk modulus) in GPa and Å.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"lattice_constant_A": "number", "bulk_modulus_GPa": "number", "C11_GPa": "number", "C12_GPa": "number", "C44_GPa": "number"}
- Scoring: scored by hidden verifier

### Step 3: Compute electronic band gap
- Role: scored
- Action: Using the equilibrium lattice constant from step 1, perform a band structure calculation with the Engel-Vosko GGA functional. Identify the indirect band gap (R→Γ) and report the value in eV along with the transition type.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"band_gap_eV": "number", "transition": "string"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant, bulk modulus, and the three independent cubic elastic constants computed by the volume-conserving strain method.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: number
    - `bulk_modulus_GPa`: number
    - `C11_GPa`: number
    - `C12_GPa`: number
    - `C44_GPa`: number

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic band gap of cubic KTaO3 and the type of indirect transition (R→Γ).
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `transition`: string

Notes: The checker compares the reported quantities to the paper's computed results and verifies the cubic mechanical stability conditions (C11−C12>0, C11+2C12>0, C44>0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "number",
          "bulk_modulus_GPa": "number",
          "C11_GPa": "number",
          "C12_GPa": "number",
          "C44_GPa": "number"
        }
      },
      "description": "Equilibrium lattice constant, bulk modulus, and the three independent cubic elastic constants computed by the volume-conserving strain method."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "transition": "string"
        }
      },
      "description": "Electronic band gap of cubic KTaO3 and the type of indirect transition (R→Γ)."
    }
  ],
  "notes": "The checker compares the reported quantities to the paper's computed results and verifies the cubic mechanical stability conditions (C11−C12>0, C11+2C12>0, C44>0)."
}
```

## How you are scored
A hidden verifier reads your submitted artifacts under `/app/outputs` and independently scores each required output. For `elastic_constants.json`, the verifier compares your reported values against hidden reference results and checks the cubic mechanical stability conditions: C11 − C12 > 0, C11 + 2C12 > 0, C44 > 0. For `band_gap.json`, the verifier checks the band gap value and confirms the transition type. The final reward combines these checks; meeting the required tolerances and stability conditions yields full credit.
