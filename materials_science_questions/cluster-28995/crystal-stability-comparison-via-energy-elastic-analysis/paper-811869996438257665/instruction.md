# Helium-4 Ground-State Energies on Graphene and Graphite via Diffusion Monte Carlo

## Problem background
The zero-temperature phase diagram of the first 4He layer adsorbed on a single graphene sheet is still an open question. The binding of helium atoms to a single carbon layer differs from binding to bulk graphite (many stacked layers), and the relative stability of liquid, commensurate solid, and incommensurate solid phases on these two substrates is not fully settled. Computing accurate ground-state energies via diffusion Monte Carlo (DMC) allows a direct comparison of the phase diagram on graphene versus graphite, which in turn tells us whether a metastable liquid film can exist on graphene. We reproduce the key ground-state energies for the liquid, the √3×√3 commensurate solid, and an incommensurate triangular solid on both a single graphene sheet (n=1) and an eight-layer graphite model (n=8), as well as the infinite-dilution binding energies that define the substrate offset.

## Approach
We use diffusion Monte Carlo, a stochastic projection method that yields the exact ground-state energy for bosonic systems given a sufficiently accurate trial wave function. The trial wave function consists of a Jastrow factor with a fixed He–He correlation parameter and a one-body factor Ψ(z) obtained by solving the 1D Schrödinger equation for a single 4He atom moving in the laterally-averaged C–He potential of the graphene planes. For solid phases the trial wave function is multiplied by Gaussian localization terms. The interatomic interactions are a high-quality He–He pair potential and a Lennard-Jones C–He potential with literature parameters. Simulations are performed in rectangular cells for a range of surface densities on both graphene (n=1) and graphite (n=8, A-B stacked layers). Liquid-phase energies at very low densities are fitted to extract the infinite-dilution limit. The method is applied without adjustable parameters beyond the published forms of the potentials and the one-body wave function, providing an independent computational reproduction.

## Reproduction target
Compute and report the ground-state energy per 4He atom (in kelvin) for the following six physical situations: liquid at equilibrium density (≈0.044 Å⁻²) on a single graphene sheet (n=1) and on eight-layer graphite (n=8); the √3×√3 commensurate solid on n=1 and n=8; and the incommensurate triangular solid at ≈0.08 Å⁻² on n=1 and n=8. Also compute the infinite-dilution binding energy for both substrates from a polynomial fit to low-density liquid data, and derive the binding-energy offset between graphene and graphite as well as the liquid–commensurate energy difference on graphite. All results (energy and statistical error for each phase, plus the derived quantities) must be collected in a single JSON file `/app/outputs/reproduced_energies.json` following the specified schema.

## Assets

- Aziz He–He pair potential: 10.1080/00268978700101491
- C–He Lennard-Jones parameters: 10.1016/S0039-6028(97)01029-7
- Quantum Monte Carlo code (optional): https://github.com/QMCPACK/qmcpack

## Workflow steps

### Step 1: One-body wave function Ψ(z)
- Role: process
- Action: Solve the 1D Schrödinger equation for a single ^4He atom under an averaged, non-corrugated C–He potential (constructed from the Lennard-Jones parameters laterally averaged over the graphene plane(s)). Obtain the ground-state wave function Ψ(z) that will be used in the many-body trial wave function.
- Evidence: none

### Step 2: Liquid-phase DMC simulations
- Role: process
- Action: Perform diffusion Monte Carlo simulations of liquid ^4He on graphene (n=1 layer) and graphite (n=8 stacked graphene layers) at a series of surface densities, including low densities (ρ < 0.02 Å⁻²) for infinite-dilution extraction and the equilibrium density 0.044 Å⁻². Use the trial wave function with the Jastrow factor (b_He‑He = 3.07 Å) and Ψ(z) from step_01, rectangular cell of 34.43 × 34.08 Å², varying the number of ^4He atoms. Record the energy per atom and statistical error for each density.
- Evidence: none

### Step 3: Commensurate √3×√3 solid DMC simulation
- Role: process
- Action: Perform DMC simulation of the √3×√3 commensurate solid phase for n=1 (graphene) and n=8 (graphite), using 120 atoms in a 44.27 × 42.60 Å² cell. Multiply the trial wave function by localization Gaussians with a = 0.31 Å⁻². Record the energy per atom and statistical error.
- Evidence: none

### Step 4: Incommensurate triangular solid DMC simulations
- Role: process
- Action: Perform DMC simulations of an incommensurate triangular solid phase at density ~0.08 Å⁻² on graphene (n=1) and graphite (n=8). Optimize the localization parameter a for each density. Average over several lateral displacements of the helium lattice with respect to the substrate to account for incommensurability. Record the averaged energy per atom and error.
- Evidence: none

### Step 5: Infinite-dilution energy extraction
- Role: process
- Action: Fit the low-density (ρ < 0.02 Å⁻²) liquid DMC energies from step_02 to a third-degree polynomial in density for each layer number (n=1 and n=8). Extract the infinite-dilution binding energy per atom (the intercept at ρ=0).
- Evidence: none

### Step 6: Compile final energies JSON
- Role: scored
- Action: Collect the computed DMC energies: liquid equilibrium energy, √3×√3 commensurate solid energy, incommensurate solid energy (at ~0.08 Å⁻²) for both n=1 and n=8, the infinite-dilution energies for graphene and graphite, the offset between them (graphene infinite dilution minus graphite infinite dilution), and the energy difference between liquid and commensurate solid on graphite. Write these values into a single JSON file with the required structure.
- Output file: `/app/outputs/reproduced_energies.json`
- Format: json
- Contract: {"type": "object", "required": ["liquid_graphene", "commensurate_graphene", "incommensurate_graphene", "liquid_graphite", "commensurate_graphite", "incommensurate_graphite", "infinite_dilution_graphene", "infinite_dilution_graphite", "offset_K", "diff_liquid_commensurate_graphite_K"], "properties": {"liquid_graphene": {"type": "object", "required": ["energy_K", "error_K"], "properties": {"energy_K": {"type": "number"}, "error_K": {"type": "number"}}}, "commensurate_graphene": {"type": "object", "required": ["energy_K", "error_K"], "properties": {"energy_K": {"type": "number"}, "error_K": {"type": "number"}}}, "incommensurate_graphene": {"type": "object", "required": ["energy_K", "error_K"], "properties": {"energy_K": {"type": "number"}, "error_K": {"type": "number"}}}, "liquid_graphite": {"type": "object", "required": ["energy_K", "error_K"], "properties": {"energy_K": {"type": "number"}, "error_K": {"type": "number"}}}, "commensurate_graphite": {"type": "object", "required": ["energy_K", "error_K"], "properties": {"energy_K": {"type": "number"}, "error_K": {"type": "number"}}}, "incommensurate_graphite": {"type": "object", "required": ["energy_K", "error_K"], "properties": {"energy_K": {"type": "number"}, "error_K": {"type": "number"}}}, "infinite_dilution_graphene": {"type": "number"}, "infinite_dilution_graphite": {"type": "number"}, "offset_K": {"type": "number"}, "diff_liquid_commensurate_graphite_K": {"type": "number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_energies.json
- path: `/app/outputs/reproduced_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the ground-state energy per ^4He atom (in K) for each phase on graphene (n=1) and graphite (n=8), the infinite-dilution energies, the binding energy offset, and the liquid-commensurate difference on graphite. The checker compares these values to the paper's reported results within tolerances (±0.2 K for absolute energies, ±0.05 K for differences/offsets) and verifies stability ordering.
- schema:
  - `type`: object
  - `required`: `liquid_graphene`, `commensurate_graphene`, `incommensurate_graphene`, `liquid_graphite`, `commensurate_graphite`, `incommensurate_graphite`, `infinite_dilution_graphene`, `infinite_dilution_graphite`, `offset_K`, `diff_liquid_commensurate_graphite_K`
  - `properties`:
    - `liquid_graphene`:
      - `type`: object
      - `required`: `energy_K`, `error_K`
      - `properties`:
        - `energy_K`:
          - `type`: number
        - `error_K`:
          - `type`: number
    - `commensurate_graphene`:
      - `type`: object
      - `required`: `energy_K`, `error_K`
      - `properties`:
        - `energy_K`:
          - `type`: number
        - `error_K`:
          - `type`: number
    - `incommensurate_graphene`:
      - `type`: object
      - `required`: `energy_K`, `error_K`
      - `properties`:
        - `energy_K`:
          - `type`: number
        - `error_K`:
          - `type`: number
    - `liquid_graphite`:
      - `type`: object
      - `required`: `energy_K`, `error_K`
      - `properties`:
        - `energy_K`:
          - `type`: number
        - `error_K`:
          - `type`: number
    - `commensurate_graphite`:
      - `type`: object
      - `required`: `energy_K`, `error_K`
      - `properties`:
        - `energy_K`:
          - `type`: number
        - `error_K`:
          - `type`: number
    - `incommensurate_graphite`:
      - `type`: object
      - `required`: `energy_K`, `error_K`
      - `properties`:
        - `energy_K`:
          - `type`: number
        - `error_K`:
          - `type`: number
    - `infinite_dilution_graphene`:
      - `type`: number
    - `infinite_dilution_graphite`:
      - `type`: number
    - `offset_K`:
      - `type`: number
    - `diff_liquid_commensurate_graphite_K`:
      - `type`: number

Notes: The agent must generate this file from the DMC simulations and polynomial fit. The hidden gold is the paper's Table I values; the checker enforces an exact-match of structure and compares numeric values with tolerances. No implementation hyperparameters are mandated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "liquid_graphene",
          "commensurate_graphene",
          "incommensurate_graphene",
          "liquid_graphite",
          "commensurate_graphite",
          "incommensurate_graphite",
          "infinite_dilution_graphene",
          "infinite_dilution_graphite",
          "offset_K",
          "diff_liquid_commensurate_graphite_K"
        ],
        "properties": {
          "liquid_graphene": {
            "type": "object",
            "required": [
              "energy_K",
              "error_K"
            ],
            "properties": {
              "energy_K": {
                "type": "number"
              },
              "error_K": {
                "type": "number"
              }
            }
          },
          "commensurate_graphene": {
            "type": "object",
            "required": [
              "energy_K",
              "error_K"
            ],
            "properties": {
              "energy_K": {
                "type": "number"
              },
              "error_K": {
                "type": "number"
              }
            }
          },
          "incommensurate_graphene": {
            "type": "object",
            "required": [
              "energy_K",
              "error_K"
            ],
            "properties": {
              "energy_K": {
                "type": "number"
              },
              "error_K": {
                "type": "number"
              }
            }
          },
          "liquid_graphite": {
            "type": "object",
            "required": [
              "energy_K",
              "error_K"
            ],
            "properties": {
              "energy_K": {
                "type": "number"
              },
              "error_K": {
                "type": "number"
              }
            }
          },
          "commensurate_graphite": {
            "type": "object",
            "required": [
              "energy_K",
              "error_K"
            ],
            "properties": {
              "energy_K": {
                "type": "number"
              },
              "error_K": {
                "type": "number"
              }
            }
          },
          "incommensurate_graphite": {
            "type": "object",
            "required": [
              "energy_K",
              "error_K"
            ],
            "properties": {
              "energy_K": {
                "type": "number"
              },
              "error_K": {
                "type": "number"
              }
            }
          },
          "infinite_dilution_graphene": {
            "type": "number"
          },
          "infinite_dilution_graphite": {
            "type": "number"
          },
          "offset_K": {
            "type": "number"
          },
          "diff_liquid_commensurate_graphite_K": {
            "type": "number"
          }
        }
      },
      "description": "Contains the ground-state energy per ^4He atom (in K) for each phase on graphene (n=1) and graphite (n=8), the infinite-dilution energies, the binding energy offset, and the liquid-commensurate difference on graphite. The checker compares these values to the paper's reported results within tolerances (±0.2 K for absolute energies, ±0.05 K for differences/offsets) and verifies stability ordering."
    }
  ],
  "notes": "The agent must generate this file from the DMC simulations and polynomial fit. The hidden gold is the paper's Table I values; the checker enforces an exact-match of structure and compares numeric values with tolerances. No implementation hyperparameters are mandated."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow artifact. The verifier reads `/app/outputs/reproduced_energies.json` and compares the reported energies and derived quantities to independently held reference values. Simply stating the paper's numbers is not sufficient — you must perform the computational workflow described in the steps to obtain your results. The final reward is a weighted combination of the per-artifact scores; each correct energy and correct derived quantity contributes to the total reward. The verifier checks numeric agreement within a hidden tolerance, verifies the required output structure, and may also check that the stability ordering among phases is correctly reproduced.
