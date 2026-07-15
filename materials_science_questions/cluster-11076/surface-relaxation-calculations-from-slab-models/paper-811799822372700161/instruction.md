# Surface stress estimation via DFT strain calculations on a slab model

## Problem background
Surface stress influences surface reconstruction, self‑organization, and nanoscale pattern formation. A prototypical system to study temperature‑dependent surface stress is the p(1×2) oxygen adlayer on W(110), which undergoes an order‑disorder transition at elevated temperature. Experimental low‑energy electron diffraction measurements provide the strain relaxations of the oxygen lattice as a function of temperature, and these can be combined with first‑principles calculations to estimate the surface stress in both the ordered and the disordered phases. In this task you will perform the computational part: you will use density‑functional theory (DFT) to compute the surface formation energy of the O/W(110) slab under uniaxial strain, and from that derive the surface stress across the transition.

## Approach
The approach uses a slab supercell model of the p(1×2) O/W(110) surface. You will construct a symmetric 11‑layer tungsten slab with an oxygen overlayer and vacuum, and carry out DFT total‑energy calculations for several homogeneous uniaxial strains applied separately along the [1‑10] and [001] crystallographic directions. From the computed energies, you obtain the surface formation energy γ and its product with the surface area A. Fitting a polynomial (quadratic for [1‑10], cubic for [001]) to γA versus strain, and differentiating, yields the surface stress τ = (1/A) ∂(Aγ)/∂ε. The stress at zero strain corresponds to the ordered (low‑temperature) phase; the stress at the experimentally reported high‑temperature strains, ε = 0.027 along [1‑10] and ε = −0.053 along [001], corresponds to the disordered phase. All necessary input parameters (slab geometry, pseudopotentials, computational parameters) are specified in the workflow steps below; the relaxed strain values are provided as fixed problem parameters.

## Reproduction target
Your objective is to produce two artifacts that will be scored:
1. `/app/outputs/surf_formation_energy_fit.json` – contains the strain values, the γA values, the polynomial fit type and coefficients, and the derived surface stress at zero strain and at the relaxed strain for each direction.
2. `/app/outputs/surface_stress_summary.json` – lists the four final surface stress quantities (in N/m): ordered phase (zero strain) along [1‑10] and [001], and disordered phase (at relaxed strain) along [1‑10] and [001].

Follow the workflow steps exactly and write these files as specified. The detailed output schemas are given in the workflow steps and output contract.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/
- Vanderbilt ultrasoft pseudopotentials for O and W: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT total energy calculations of strained slab
- Role: process
- Action: Construct a symmetric 11-layer slab of p(1×2) O on W(110) with 9 vacuum layers. Perform DFT total-energy calculations (LDA, Vanderbilt ultrasoft pseudopotentials) for a set of uniaxial strains along [1-10] and [001] directions, covering at least five strain points per direction including the reported relaxed strains ε=0.027 ([1-10]) and ε=-0.053 ([001]). Compute bulk W reference energy for each strain. Collect slab total energies, unit cell areas, and bulk energies.
- Evidence: `/app/outputs/dft_raw_energies.json`

### Step 2: Surface formation energy fit and stress evaluation
- Role: scored
- Action: From the DFT total energies, compute surface formation energy γ multiplied by area A for each strain. For each direction, fit a polynomial (quadratic for [1-10], cubic for [001]) to γA vs strain and record fitted coefficients. Compute surface stress at zero strain and at the relaxed strains (0.027 and -0.053) via τ = (1/A) ∂(Aγ)/∂ε.
- Output file: `/app/outputs/surf_formation_energy_fit.json`
- Format: json
- Contract: Object with keys 'dir_1bar1_0' and 'dir_001'. Each contains: 'strain_values' (array of numbers), 'gammaA_values' (array of numbers), 'fit_type' (string), 'fit_coefficients' (array of numbers), 'stress_at_zero_strain' (number, N/m), 'stress_at_relaxed_strain' (number, N/m).
- Scoring: scored by hidden verifier

### Step 3: Surface stress summary
- Role: scored (load-bearing)
- Action: Using the fitted polynomials, compute and output the four surface stress values: ordered phase (zero strain) along [1-10] and [001], and disordered phase (at relaxed strain) along [1-10] and [001].
- Output file: `/app/outputs/surface_stress_summary.json`
- Format: json
- Contract: Object with keys 'tau_O_1x2_gamma_1bar1_0', 'tau_O_1x2_gamma_001', 'tau_disO_1x2_gamma_1bar1_0', 'tau_disO_1x2_gamma_001' (all numbers in N/m).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surf_formation_energy_fit.json`
- `/app/outputs/surface_stress_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surf_formation_energy_fit.json
- path: `/app/outputs/surf_formation_energy_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Strain-energy data points, polynomial fits, and stress values derived from DFT calculations. The checker recomputes stress from fit coefficients and compares against reference values.
- schema:
  - `type`: object
  - `required`: `dir_1bar1_0`, `dir_001`
  - `dir_1bar1_0`:
    - `type`: object
    - `required`: `strain_values`, `gammaA_values`, `fit_type`, `fit_coefficients`, `stress_at_zero_strain`, `stress_at_relaxed_strain`
    - `strain_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `gammaA_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `fit_type`:
      - `type`: string
    - `fit_coefficients`:
      - `type`: array
      - `items`:
        - `type`: number
    - `stress_at_zero_strain`:
      - `type`: number
      - `unit`: N/m
    - `stress_at_relaxed_strain`:
      - `type`: number
      - `unit`: N/m
  - `dir_001`:
    - `type`: object
    - `required`: `strain_values`, `gammaA_values`, `fit_type`, `fit_coefficients`, `stress_at_zero_strain`, `stress_at_relaxed_strain`
    - `strain_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `gammaA_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `fit_type`:
      - `type`: string
    - `fit_coefficients`:
      - `type`: array
      - `items`:
        - `type`: number
    - `stress_at_zero_strain`:
      - `type`: number
      - `unit`: N/m
    - `stress_at_relaxed_strain`:
      - `type`: number
      - `unit`: N/m

### surface_stress_summary.json
- path: `/app/outputs/surface_stress_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final surface stress quantities for ordered and disordered phases. The checker verifies consistency with the recomputed stress values from the previous artifact.
- schema:
  - `type`: object
  - `required`: `tau_O_1x2_gamma_1bar1_0`, `tau_O_1x2_gamma_001`, `tau_disO_1x2_gamma_1bar1_0`, `tau_disO_1x2_gamma_001`
  - `tau_O_1x2_gamma_1bar1_0`:
    - `type`: number
    - `unit`: N/m
  - `tau_O_1x2_gamma_001`:
    - `type`: number
    - `unit`: N/m
  - `tau_disO_1x2_gamma_1bar1_0`:
    - `type`: number
    - `unit`: N/m
  - `tau_disO_1x2_gamma_001`:
    - `type`: number
    - `unit`: N/m

Notes: The relaxed strains (ε=0.027 along [1-10] and ε=-0.053 along [001]) are provided in the task instruction as problem parameters. No experimental data need to be fetched. The domain-wall energy analysis (stage 1 of the paper) is omitted as a minor supporting calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surf_formation_energy_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "dir_1bar1_0",
          "dir_001"
        ],
        "dir_1bar1_0": {
          "type": "object",
          "required": [
            "strain_values",
            "gammaA_values",
            "fit_type",
            "fit_coefficients",
            "stress_at_zero_strain",
            "stress_at_relaxed_strain"
          ],
          "strain_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "gammaA_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "fit_type": {
            "type": "string"
          },
          "fit_coefficients": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "stress_at_zero_strain": {
            "type": "number",
            "unit": "N/m"
          },
          "stress_at_relaxed_strain": {
            "type": "number",
            "unit": "N/m"
          }
        },
        "dir_001": {
          "type": "object",
          "required": [
            "strain_values",
            "gammaA_values",
            "fit_type",
            "fit_coefficients",
            "stress_at_zero_strain",
            "stress_at_relaxed_strain"
          ],
          "strain_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "gammaA_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "fit_type": {
            "type": "string"
          },
          "fit_coefficients": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "stress_at_zero_strain": {
            "type": "number",
            "unit": "N/m"
          },
          "stress_at_relaxed_strain": {
            "type": "number",
            "unit": "N/m"
          }
        }
      },
      "description": "Strain-energy data points, polynomial fits, and stress values derived from DFT calculations. The checker recomputes stress from fit coefficients and compares against reference values."
    },
    {
      "file": "surface_stress_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "tau_O_1x2_gamma_1bar1_0",
          "tau_O_1x2_gamma_001",
          "tau_disO_1x2_gamma_1bar1_0",
          "tau_disO_1x2_gamma_001"
        ],
        "tau_O_1x2_gamma_1bar1_0": {
          "type": "number",
          "unit": "N/m"
        },
        "tau_O_1x2_gamma_001": {
          "type": "number",
          "unit": "N/m"
        },
        "tau_disO_1x2_gamma_1bar1_0": {
          "type": "number",
          "unit": "N/m"
        },
        "tau_disO_1x2_gamma_001": {
          "type": "number",
          "unit": "N/m"
        }
      },
      "description": "Final surface stress quantities for ordered and disordered phases. The checker verifies consistency with the recomputed stress values from the previous artifact."
    }
  ],
  "notes": "The relaxed strains (ε=0.027 along [1-10] and ε=-0.053 along [001]) are provided in the task instruction as problem parameters. No experimental data need to be fetched. The domain-wall energy analysis (stage 1 of the paper) is omitted as a minor supporting calculation."
}
```

## How you are scored
A hidden verifier will score your submitted artifacts independently for each step. For `surf_formation_energy_fit.json`, it will read your fitted polynomial coefficients, recompute the stress at the specified strains from your fit, and compare the recomputed values to hidden reference values with a suitable tolerance. It also cross‑checks the stress values you explicitly reported against the recomputed stresses. For `surface_stress_summary.json`, it verifies consistency with the recomputed stresses from the first artifact. The two scores are combined by weight into a single reward; meeting or exceeding the hidden reference quality earns full credit, while increasing deviation reduces the score. No amount of guessing or supplying expected numbers without the actual DFT strain‑energy data will pass—the verifier relies on your fit coefficients and the consistency between your outputs.
