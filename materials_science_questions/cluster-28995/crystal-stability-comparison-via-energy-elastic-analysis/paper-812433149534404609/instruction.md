# Iron bond-order potential: lattice stability, elastic moduli, and phase transformation pressure

## Problem background
Accurate interatomic potentials are essential for large-scale atomistic simulations, but capturing directional bonding in transition metals like iron is challenging. A bond-order potential has been proposed for iron that extends the Tersoff formalism with a more flexible bond-order function and an angular-dependent environmental term. The potential was calibrated to reproduce experimental properties of BCC iron, including its cohesive energy, lattice constant, and elastic moduli. This task asks you to implement that potential and compute a comprehensive set of structural, elastic, and energetic properties for BCC, FCC, and HCP iron, as well as the pressure at which the BCC and HCP phases transform, to evaluate its predictive performance.

## Approach
The total potential energy is written as a sum over atom pairs of a repulsive term and an attractive bond-order term, both modulated by a smooth cutoff function that restricts interactions to neighbours within a given distance. The repulsive term is a simple exponential with optional short-range stiffening. The attractive term is an exponential multiplied by a bond-order function that depends on the local atomic environment. This bond-order function is a polynomial expansion in an environmental variable ζ, which is computed for each atom pair by summing over neighbouring atoms an angular function g(θ) weighted by a distance-dependent factor. The angular function contains parameters that control the directional character of bonding. All potential parameters (A, B, β1, β2, β3, β4, f, γ1–γ6, nz, c, d, β_ang, δ, h, cutoff radii r_c1 and r_c2, and nearest-neighbor distance R0) are provided in the task description. You will implement this functional form in a computational module that handles periodic boundary conditions and neighbour lists. Using this implementation, you will then construct BCC, FCC, and HCP crystals, compute their cohesive energies, elastic constants via finite strain distortions, surface energy via slab construction, and the enthalpy-pressure curves that yield the BCC-HCP transformation pressure.

## Reproduction target
Construct perfect BCC, FCC, and HCP crystals at the following atomic volumes: Ω_BCC = 11.6833 Å³, Ω_FCC = 11.152 Å³, Ω_HCP = 10.398 Å³. For each structure, compute the cohesive energy per atom (Ecoh). For BCC iron, additionally compute the equilibrium lattice constant a (Å), the elastic constants C11, C12, C44, and C′ (in 10² GPa), the bulk modulus K (10² GPa), and the (111) surface energy (eV per surface atom). Finally, compute the enthalpies of BCC and HCP phases as a function of pressure and determine the pressure (kbar) at which the two enthalpies cross, indicating the BCC-HCP phase transformation. Write all results to the file `/app/outputs/computed_properties.json` using the exact schema defined in the output contract.

## Assets

- Python 3 runtime
- NumPy package: numpy

## Potential parameters

The bond-order potential uses the following numeric parameter values (taken from Table 2 of the source):

- A = 0.2346154E+04
- beta1 = 0.3465077E+01
- beta4 = 0.0, alpha = 0.0
- B = 0.1580257E-04
- beta2 = 0.1117197E+01
- f = 0.4534376E+00
- gamma1 = 0.3718635E+03
- gamma2 = 0.1664427E+04
- gamma3 = -0.6539821E+02
- gamma4 = 0.9013512E+00
- gamma5 = -0.1142012E-01
- gamma6 = 0.1385744E-03
- nz = 6
- beta3 = 0.6034363E+00
- c = 0.4199031E+01
- d = 0.3752465E+02
- h = 0.6915982E+00
- beta_ang = 0.9433671E+00 (angular function parameter β in Eq. 7a)
- delta = 0.9870393E+00
- cutoff radii: r_c1 = 3.70, r_c2 = 3.60 (Å)
- nearest-neighbor distance R0 = (sqrt(3)/2) * a_BCC, where a_BCC = 2.8589 Å (R0 ≈ 2.476 Å)

## Workflow steps

### Step 1: Implement the bond-order potential for Fe
- Role: process
- Action: Write a computational module (e.g., Python function) that evaluates the total energy of an Fe atom configuration using the bond-order potential functional form described in the method. The form includes a repulsive pair term V_rep, an attractive bond-order term V_bo with a bond-order function b, an environmental variable ζ, and an angular function g. Use the published parameters: A, B, β1, β2, β3, β4, f, γ1, γ2, γ3, γ4, γ5, γ6, nz, c, d, β_ang, δ, h, cutoff radii r_c1, r_c2, and nearest-neighbor distance R0. The potential must properly handle periodic boundary conditions and sum over neighbors within the cutoff distance.
- Evidence: none

### Step 2: Compute physical properties of Fe phases and phase transformation pressure
- Role: scored (load-bearing)
- Action: Using the implemented potential: (1) construct BCC, FCC, and HCP crystals at the specified atomic volumes (Ω0_BCC = 11.6833 Å³, Ω0_FCC = 11.152 Å³, Ω0_HCP = 10.398 Å³) and compute their cohesive energy per atom (Ecoh). (2) For BCC, compute the equilibrium lattice constant a, the elastic constants C11, C12, C44, and C′ via finite differences of energy with respect to small strain distortions, the bulk modulus K, and the (111) surface energy by constructing a slab and subtracting the bulk energy. (3) Compute the enthalpies of BCC and HCP as a function of pressure and determine the pressure where they become equal (phase transformation pressure). Output all results in a structured JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {
  "BCC": {
    "a": "float (Å)",
    "Omega0": "float (Å³)",
    "Ecoh": "float (eV/atom)",
    "C11": "float (10² GPa)",
    "C12": "float (10² GPa)",
    "C44": "float (10² GPa)",
    "Cprime": "float (10² GPa)",
    "K": "float (10² GPa)",
    "E_surf_111": "float (eV/surface atom)"
  },
  "FCC": {
    "Omega0": "float (Å³)",
    "Ecoh": "float (eV/atom)"
  },
  "HCP": {
    "Omega0": "float (Å³)",
    "Ecoh": "float (eV/atom)"
  },
  "phase_transformation": {
    "pressure_BCC_HCP": "float (kbar)"
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural, elastic, and energetic properties of iron phases (BCC, FCC, HCP) and the BCC-HCP phase transformation pressure, computed from the bond-order potential.
- schema:
  - `type`: object
  - `required`: `BCC`, `FCC`, `HCP`, `phase_transformation`
  - `properties`:
    - `BCC`:
      - `type`: object
      - `required`: `a`, `Omega0`, `Ecoh`, `C11`, `C12`, `C44`, `Cprime`, `K`, `E_surf_111`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Å
        - `Omega0`:
          - `type`: number
          - `unit`: Å³
        - `Ecoh`:
          - `type`: number
          - `unit`: eV/atom
        - `C11`:
          - `type`: number
          - `unit`: 10² GPa
        - `C12`:
          - `type`: number
          - `unit`: 10² GPa
        - `C44`:
          - `type`: number
          - `unit`: 10² GPa
        - `Cprime`:
          - `type`: number
          - `unit`: 10² GPa
        - `K`:
          - `type`: number
          - `unit`: 10² GPa
        - `E_surf_111`:
          - `type`: number
          - `unit`: eV/surface atom
    - `FCC`:
      - `type`: object
      - `required`: `Omega0`, `Ecoh`
      - `properties`:
        - `Omega0`:
          - `type`: number
          - `unit`: Å³
        - `Ecoh`:
          - `type`: number
          - `unit`: eV/atom
    - `HCP`:
      - `type`: object
      - `required`: `Omega0`, `Ecoh`
      - `properties`:
        - `Omega0`:
          - `type`: number
          - `unit`: Å³
        - `Ecoh`:
          - `type`: number
          - `unit`: eV/atom
    - `phase_transformation`:
      - `type`: object
      - `required`: `pressure_BCC_HCP`
      - `properties`:
        - `pressure_BCC_HCP`:
          - `type`: number
          - `unit`: kbar

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "BCC",
          "FCC",
          "HCP",
          "phase_transformation"
        ],
        "properties": {
          "BCC": {
            "type": "object",
            "required": [
              "a",
              "Omega0",
              "Ecoh",
              "C11",
              "C12",
              "C44",
              "Cprime",
              "K",
              "E_surf_111"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Å"
              },
              "Omega0": {
                "type": "number",
                "unit": "Å³"
              },
              "Ecoh": {
                "type": "number",
                "unit": "eV/atom"
              },
              "C11": {
                "type": "number",
                "unit": "10² GPa"
              },
              "C12": {
                "type": "number",
                "unit": "10² GPa"
              },
              "C44": {
                "type": "number",
                "unit": "10² GPa"
              },
              "Cprime": {
                "type": "number",
                "unit": "10² GPa"
              },
              "K": {
                "type": "number",
                "unit": "10² GPa"
              },
              "E_surf_111": {
                "type": "number",
                "unit": "eV/surface atom"
              }
            }
          },
          "FCC": {
            "type": "object",
            "required": [
              "Omega0",
              "Ecoh"
            ],
            "properties": {
              "Omega0": {
                "type": "number",
                "unit": "Å³"
              },
              "Ecoh": {
                "type": "number",
                "unit": "eV/atom"
              }
            }
          },
          "HCP": {
            "type": "object",
            "required": [
              "Omega0",
              "Ecoh"
            ],
            "properties": {
              "Omega0": {
                "type": "number",
                "unit": "Å³"
              },
              "Ecoh": {
                "type": "number",
                "unit": "eV/atom"
              }
            }
          },
          "phase_transformation": {
            "type": "object",
            "required": [
              "pressure_BCC_HCP"
            ],
            "properties": {
              "pressure_BCC_HCP": {
                "type": "number",
                "unit": "kbar"
              }
            }
          }
        }
      },
      "description": "Structural, elastic, and energetic properties of iron phases (BCC, FCC, HCP) and the BCC-HCP phase transformation pressure, computed from the bond-order potential."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads only the file `/app/outputs/computed_properties.json`. The verifier compares each numeric field in the JSON to a hidden reference value using relative tolerances. Each field contributes a predefined weight toward the total score; fields that are missing or not formatted correctly receive zero credit. The verifier does not re-execute any computation—it simply validates the reported numbers. Therefore, it is essential that you implement the potential correctly, perform all property calculations accurately, and format your output exactly as specified in the output contract.
