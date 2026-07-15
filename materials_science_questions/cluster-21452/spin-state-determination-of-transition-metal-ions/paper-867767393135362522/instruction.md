# Intermediate-Coupling Single-Ion Model Fit for 5d³ Oxides

## Problem background
5d³ transition‑metal oxides such as Ca₃LiOsO₆ and Ba₂YOsO₆ exhibit magnetic properties that cannot be explained by a pure S=3/2 ground state, indicating that spin‑orbit coupling (SOC) and electron‑electron interactions must be treated on an equal footing. Resonant inelastic x‑ray scattering (RIXS) measurements reveal a set of intra‑t₂g excitation peaks below 2 eV, whose energies and multiplicity encode the underlying single‑ion Hamiltonian. The key open question is: what quantitative single‑ion parameters (spin‑orbit coupling strength, Racah B and C, and effective Hund’s coupling) and what ground‑state wavefunction describe these compounds within an intermediate‑coupling model that includes cubic crystal field, Coulomb exchange, and SOC simultaneously?

## Approach
We adopt the intermediate‑coupling framework for a 5d³ ion in an octahedral crystal field. The full Hamiltonian is split into three contributions: (i) a cubic crystal‑field term that lifts the degeneracy of the d orbitals, quantified by 10Dq; (ii) Coulomb and exchange interactions parameterized by the Racah parameters B and C; (iii) spin‑orbit coupling ζ_SO. Following the explicit matrix forms given in Eisenstein (1961), we construct the 21×21 Γ₈ and the 9×9 Γ₆ and Γ₇ Hamiltonian matrices in the O double group basis, where the basis states describe all ways three electrons can occupy the t₂g and e_g levels. For each compound the crystal‑field splitting 10Dq is fixed to the energy of the t₂g→e_g RIXS peak, and the experimental intra‑t₂g peak energies a, b, c, d are used as target observables. A nonlinear least‑squares fit varies ζ_SO, B, and C to minimize the difference between the computed first four excited eigenvalues of the Hamiltonian and the measured peak energies. From the best‑fit parameters we derive J_h = 3B + C, the fitted excitation energies, and the normalized eigenvector coefficients of the Γ₈ ground state.

## Reproduction target
Implement the Hamiltonian matrices as parametrized by B, C, and ζ_SO, then perform the fitting procedure for both Ca₃LiOsO₆ and Ba₂YOsO₆. For each compound, output a JSON file containing the optimized ζ_SO (eV), B (eV), C (eV), J_h (eV), the four fitted excitation energies (eV, in increasing order), and the full normalized eigenvector coefficients (21 components) of the Γ₈ ground state. The separate steps define the required inputs (crystal-field splittings and experimental peak energies) and the exact naming of the output files.

## Assets

- Eisenstein, J. Chem. Phys. 34, 1628 (1961) – Interaction matrices for d³ in octahedral field: https://doi.org/10.1063/1.4732310
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Assemble intermediate-coupling Hamiltonian matrices
- Role: process
- Action: Implement the single-ion Hamiltonian for the 5d³ configuration in an octahedral crystal field, following the matrix forms given by Eisenstein (1961). Incorporate cubic crystal-field splitting 10Dq (to be fixed per compound), Racah Coulomb/exchange parameters B and C, and spin-orbit coupling ζ_SO. Construct the 21×21 Γ8 matrix and the 9×9 Γ6 and Γ7 matrices in the O double group basis. Do not hardcode numerical values for B, C, or ζ_SO; the matrices must accept these as variables for later fitting.
- Evidence: `/app/outputs/matrix_assembly.log`

### Step 2: Fit Ca₃LiOsO₆ single-ion parameters and extract ground state
- Role: scored (load-bearing)
- Action: For Ca₃LiOsO₆, load the fixed crystal-field splitting 10Dq and the experimental intra‑t₂g RIXS peak energies from the input file `/app/inputs/ca3lioso6_input.json`. Perform a nonlinear least‑squares fit of the first four excited eigenvalues of the Hamiltonian to these four target energies by optimizing ζ_SO, B, C. Diagonalize the matrices at each iteration. From the best‑fit parameters, compute J_h = 3B + C, the four fitted excitation energies, and the full normalized eigenvector coefficients of the Γ8 ground state (all 21 components, ordered consistently with the Eisenstein basis). Output these quantities in a JSON file.
- Output file: `/app/outputs/ca3lioso6_results.json`
- Format: json
- Contract: JSON object with keys: zeta_SO (float, eV), B (float, eV), C (float, eV), Jh (float, eV), excitation_energies (array of 4 floats, eV), ground_state_eigenvector (array of 21 floats).
- Scoring: scored by hidden verifier

### Step 3: Fit Ba₂YOsO₆ single-ion parameters and extract ground state
- Role: scored (load-bearing)
- Action: For Ba₂YOsO₆, load the fixed crystal-field splitting 10Dq and the experimental intra‑t₂g RIXS peak energies from the input file `/app/inputs/ba2yoso6_input.json`. Repeat the same fitting procedure as for Ca₃LiOsO₆. Output the best‑fit ζ_SO, B, C, J_h, the fitted excitation energies, and the ground‑state eigenvector.
- Output file: `/app/outputs/ba2yoso6_results.json`
- Format: json
- Contract: JSON object with keys: zeta_SO (float, eV), B (float, eV), C (float, eV), Jh (float, eV), excitation_energies (array of 4 floats, eV), ground_state_eigenvector (array of 21 floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ca3lioso6_results.json`
- `/app/outputs/ba2yoso6_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ca3lioso6_results.json
- path: `/app/outputs/ca3lioso6_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted single-ion parameters, computed excitation energies, and ground-state eigenvector coefficients for Ca₃LiOsO₆. The checker will compare the fitted parameters to reference values within tolerances and verify that the ground state eigenvector has the expected dominant components.
- schema:
  - `type`: object
  - `required`: `zeta_SO`, `B`, `C`, `Jh`, `excitation_energies`, `ground_state_eigenvector`
  - `properties`:
    - `zeta_SO`:
      - `type`: number
      - `unit`: eV
    - `B`:
      - `type`: number
      - `unit`: eV
    - `C`:
      - `type`: number
      - `unit`: eV
    - `Jh`:
      - `type`: number
      - `unit`: eV
    - `excitation_energies`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: eV
      - `minItems`: 4
      - `maxItems`: 4
    - `ground_state_eigenvector`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 21
      - `maxItems`: 21

### ba2yoso6_results.json
- path: `/app/outputs/ba2yoso6_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted single-ion parameters, computed excitation energies, and ground-state eigenvector coefficients for Ba₂YOsO₆. The checker will compare the fitted parameters to reference values within tolerances and verify that the ground state eigenvector has the expected dominant components.
- schema:
  - `type`: object
  - `required`: `zeta_SO`, `B`, `C`, `Jh`, `excitation_energies`, `ground_state_eigenvector`
  - `properties`:
    - `zeta_SO`:
      - `type`: number
      - `unit`: eV
    - `B`:
      - `type`: number
      - `unit`: eV
    - `C`:
      - `type`: number
      - `unit`: eV
    - `Jh`:
      - `type`: number
      - `unit`: eV
    - `excitation_energies`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: eV
      - `minItems`: 4
      - `maxItems`: 4
    - `ground_state_eigenvector`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 21
      - `maxItems`: 21

Notes: The experimental peak energies and 10Dq values are provided as input JSON files, not hardcoded in the instruction. The checker uses hidden reference values (from the paper) to score the fitted parameters and eigenvector components.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ca3lioso6_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "zeta_SO",
          "B",
          "C",
          "Jh",
          "excitation_energies",
          "ground_state_eigenvector"
        ],
        "properties": {
          "zeta_SO": {
            "type": "number",
            "unit": "eV"
          },
          "B": {
            "type": "number",
            "unit": "eV"
          },
          "C": {
            "type": "number",
            "unit": "eV"
          },
          "Jh": {
            "type": "number",
            "unit": "eV"
          },
          "excitation_energies": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "eV"
            },
            "minItems": 4,
            "maxItems": 4
          },
          "ground_state_eigenvector": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 21,
            "maxItems": 21
          }
        }
      },
      "description": "Fitted single-ion parameters, computed excitation energies, and ground-state eigenvector coefficients for Ca₃LiOsO₆. The checker will compare the fitted parameters to reference values within tolerances and verify that the ground state eigenvector has the expected dominant components."
    },
    {
      "file": "ba2yoso6_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "zeta_SO",
          "B",
          "C",
          "Jh",
          "excitation_energies",
          "ground_state_eigenvector"
        ],
        "properties": {
          "zeta_SO": {
            "type": "number",
            "unit": "eV"
          },
          "B": {
            "type": "number",
            "unit": "eV"
          },
          "C": {
            "type": "number",
            "unit": "eV"
          },
          "Jh": {
            "type": "number",
            "unit": "eV"
          },
          "excitation_energies": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "eV"
            },
            "minItems": 4,
            "maxItems": 4
          },
          "ground_state_eigenvector": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 21,
            "maxItems": 21
          }
        }
      },
      "description": "Fitted single-ion parameters, computed excitation energies, and ground-state eigenvector coefficients for Ba₂YOsO₆. The checker will compare the fitted parameters to reference values within tolerances and verify that the ground state eigenvector has the expected dominant components."
    }
  ],
  "notes": "The experimental peak energies and 10Dq values are provided as input JSON files, not hardcoded in the instruction. The checker uses hidden reference values (from the paper) to score the fitted parameters and eigenvector components."
}
```

## How you are scored
A hidden verifier independently scores each scored output file. For each compound the verifier compares your reported parameters (ζ_SO, B, C, J_h) and excitation energies against reference values derived from the original study. It also checks internal self‑consistency by recomputing the eigenvalues from your submitted parameters and comparing them to your reported excitation energies. The ground‑state eigenvector is inspected to verify normalization and that the expected symmetry‑adapted basis states appear with physically plausible magnitudes, consistent with the cubic intermediate‑coupling scenario. The final reward is a weighted combination of these checks; merely reporting numbers without a genuine fitting process will not suffice.
