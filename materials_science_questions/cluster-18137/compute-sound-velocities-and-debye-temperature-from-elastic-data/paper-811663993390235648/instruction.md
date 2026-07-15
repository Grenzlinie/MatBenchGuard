# Compute Properties of Cubic Zr₃N₄ and Hf₃N₄ via DFT

## Problem background
Transition metal nitrides such as Zr₃N₄ and Hf₃N₄ are candidate materials for ultra‑hard and refractory applications. The cubic Th₃P₄‑type phase is of practical interest, but experimental data for many of its fundamental properties remain limited. First‑principles calculations based on density functional theory (DFT) can predict structural, elastic, mechanical, and optical behaviour and provide quantitative benchmarks where measurements are sparse or absent. In this task, we use DFT to compute the ground‑state properties of these two compounds.

## Approach
The workflow proceeds in three DFT calculation stages followed by post‑processing. First, the cubic crystal structure is relaxed at zero pressure, and a series of static relaxations under hydrostatic pressures up to 30 GPa is performed to obtain a pressure–volume curve; a third‑order Birch–Murnaghan equation of state is then fitted to the P(V) data to extract the zero‑pressure bulk modulus and its pressure derivative. Second, the single‑crystal elastic constants (C₁₁, C₁₂, C₄₄) are obtained via the static finite‑strain method, and polycrystalline moduli (bulk, shear, Young’s modulus, Poisson’s ratio) are computed by the Voigt–Reuss–Hill averaging scheme. Third, the imaginary part of the dielectric function is calculated from the momentum matrix elements, and the real part is obtained via Kramers–Kronig transformation; the static limits yield the dielectric constant and refractive index. Finally, mass density, sound velocities, and Debye temperature are derived from the lattice constant and polycrystalline moduli using standard relations. All calculations are performed with a plane‑wave pseudopotential DFT code using the GGA‑PBE exchange‑correlation functional and appropriate pseudopotentials. The required outputs are four JSON files capturing these quantities for both Zr₃N₄ and Hf₃N₄.

## Reproduction target
Compute the following quantities for the cubic (I‑43d) phases of Zr₃N₄ and Hf₃N₄:

1. Equilibrium lattice constant a₀ (Å).
2. Zero‑pressure bulk modulus B₀ (GPa) and its pressure derivative B′ (dimensionless) from a Birch–Murnaghan fit to the P(V) data over 0–30 GPa.
3. Single‑crystal elastic constants C₁₁, C₁₂, C₄₄ (GPa).
4. Polycrystalline bulk modulus B, shear modulus G, Young’s modulus E (GPa), and Poisson’s ratio ν (dimensionless) from Voigt–Reuss–Hill averaging.
5. Mass density ρ (g/cm³).
6. Transverse, longitudinal, and average sound velocities vₜ, vₗ, vₘ (km/s).
7. Debye temperature θ_D (K).
8. Static dielectric constant ε₁(0) and refractive index n(0) (dimensionless).

All values must be written to the four JSON output files exactly as specified in the workflow steps. The computed numbers should reflect a fully converged DFT setup; you may use any open‑source plane‑wave DFT code and public pseudopotentials. The target is to reproduce the physical trends and magnitudes that emerge from the GGA‑PBE description of these materials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python numerical libraries: numpy scipy

## Workflow steps

### Step 1: DFT geometry optimization and P‑V curve
- Role: process
- Action: Build the cubic Th₃P₄‑type unit cell (space group I‑43d, atomic positions as described in the method) for Zr₃N₄ and Hf₃N₄. Use a plane‑wave DFT code with GGA‑PBE exchange‑correlation and appropriate pseudopotentials. First perform full geometry relaxation at zero pressure to obtain equilibrium lattice constant a₀ and volume V₀. Then run a series of static relaxations at fixed hydrostatic pressures spanning 0–30 GPa to generate a P(V) table for each compound.
- Evidence: `/app/outputs/dft_relax.log`

### Step 2: DFT elastic constants via finite strain
- Role: process
- Action: For the zero‑pressure equilibrium structures of Zr₃N₄ and Hf₃N₄, apply the static finite‑strain approach within DFT: deform the lattice according to the symmetry‑adapted strain patterns that give the cubic elastic constants C₁₁, C₁₂, and C₄₄. Fit the change in total energy versus strain magnitude to extract the three independent elastic constants.
- Evidence: `/app/outputs/elastic.log`

### Step 3: DFT dielectric function
- Role: process
- Action: Using the relaxed ground‑state electronic structure, compute the imaginary part of the dielectric function ϵ₂(ω) from momentum matrix elements. Apply a Kramers‑Kronig transformation to obtain the real part ϵ₁(ω) and extract the static limits ϵ₁(0) and n(0) = √(ϵ₁(0)).
- Evidence: `/app/outputs/optical.log`

### Step 4: Structural parameters and equation‑of‑state fit
- Role: scored (load-bearing)
- Action: From the zero‑pressure DFT relaxation, record the equilibrium lattice constant a₀. Fit the P(V) data (0–30 GPa) to the third‑order Birch–Murnaghan equation of state, keeping V₀ fixed at the zero‑pressure value, to obtain the zero‑pressure bulk modulus B₀ and its pressure derivative B′. Write the results for both Zr₃N₄ and Hf₃N₄ to the specified JSON file.
- Output file: `/app/outputs/step_01_structural_params.json`
- Format: json
- Contract: {"Zr3N4": {"a0": "float (Å)", "B0": "float (GPa)", "Bprime": "float (dimensionless)"}, "Hf3N4": {"a0": "float (Å)", "B0": "float (GPa)", "Bprime": "float (dimensionless)"}}
- Scoring: scored by hidden verifier

### Step 5: Elastic constants and polycrystalline moduli
- Role: scored
- Action: From the finite‑strain DFT calculations, obtain the single‑crystal elastic constants C₁₁, C₁₂, C₄₄. Apply the Voigt–Reuss–Hill averaging scheme to compute the isotropic polycrystalline bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio ν. Write all values for both compounds to the specified JSON file.
- Output file: `/app/outputs/step_02_elastic_constants.json`
- Format: json
- Contract: {"Zr3N4": {"C11": "float (GPa)", "C12": "float (GPa)", "C44": "float (GPa)", "B": "float (GPa)", "G": "float (GPa)", "E": "float (GPa)", "nu": "float (dimensionless)"}, "Hf3N4": {…}}
- Scoring: scored by hidden verifier

### Step 6: Sound velocities and Debye temperature
- Role: scored
- Action: From the equilibrium lattice constant and formula‑unit mass compute the mass density ρ. Using the polycrystalline B and G from the previous step, apply Navier's equations to obtain longitudinal vₗ and transverse vₜ sound velocities, then compute the average sound velocity vₘ and the Debye temperature θ_D using standard formulas (Anderson/Wachter). Write the results to the specified JSON file.
- Output file: `/app/outputs/step_03_sound_velocities_debye.json`
- Format: json
- Contract: {"Zr3N4": {"rho": "float (g/cm³)", "vt": "float (km/s)", "vl": "float (km/s)", "vm": "float (km/s)", "theta_D": "float (K)"}, "Hf3N4": {…}}
- Scoring: scored by hidden verifier

### Step 7: Static optical constants
- Role: scored
- Action: From the Kramers‑Kronig analysis of the dielectric function, extract the zero‑frequency limits: the static dielectric constant ε₁(0) and the static refractive index n(0) = √(ε₁(0)). Write these values for both compounds to the specified JSON file.
- Output file: `/app/outputs/step_04_optical_constants.json`
- Format: json
- Contract: {"Zr3N4": {"epsilon0": "float (dimensionless)", "n0": "float (dimensionless)"}, "Hf3N4": {…}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_params.json`
- `/app/outputs/step_02_elastic_constants.json`
- `/app/outputs/step_03_sound_velocities_debye.json`
- `/app/outputs/step_04_optical_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_params.json
- path: `/app/outputs/step_01_structural_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant, bulk modulus and pressure derivative for the two compounds, extracted from DFT relaxation and Birch‑Murnaghan equation‑of‑state fitting.
- schema:
  - `type`: object
  - `required`: `Zr3N4`, `Hf3N4`
  - `properties`:
    - `Zr3N4`:
      - `type`: object
      - `required`: `a0`, `B0`, `Bprime`
      - `properties`:
        - `a0`:
          - `type`: number
          - `unit`: Å
        - `B0`:
          - `type`: number
          - `unit`: GPa
        - `Bprime`:
          - `type`: number
          - `unit`: dimensionless
    - `Hf3N4`:
      - `type`: object
      - `required`: `a0`, `B0`, `Bprime`
      - `properties`:
        - `a0`:
          - `type`: number
          - `unit`: Å
        - `B0`:
          - `type`: number
          - `unit`: GPa
        - `Bprime`:
          - `type`: number
          - `unit`: dimensionless

### step_02_elastic_constants.json
- path: `/app/outputs/step_02_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single‑crystal elastic constants and Voigt–Reuss–Hill polycrystalline moduli (bulk, shear, Young’s moduli and Poisson’s ratio) for the two compounds.
- schema:
  - `type`: object
  - `required`: `Zr3N4`, `Hf3N4`
  - `properties`:
    - `Zr3N4`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `B`, `G`, `E`, `nu`
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `B`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `nu`:
          - `type`: number
          - `unit`: dimensionless
    - `Hf3N4`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `B`, `G`, `E`, `nu`
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `B`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `nu`:
          - `type`: number
          - `unit`: dimensionless

### step_03_sound_velocities_debye.json
- path: `/app/outputs/step_03_sound_velocities_debye.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mass density, transverse/longitudinal/average sound velocities, and Debye temperature computed from polycrystalline moduli and lattice constant.
- schema:
  - `type`: object
  - `required`: `Zr3N4`, `Hf3N4`
  - `properties`:
    - `Zr3N4`:
      - `type`: object
      - `required`: `rho`, `vt`, `vl`, `vm`, `theta_D`
      - `properties`:
        - `rho`:
          - `type`: number
          - `unit`: g/cm³
        - `vt`:
          - `type`: number
          - `unit`: km/s
        - `vl`:
          - `type`: number
          - `unit`: km/s
        - `vm`:
          - `type`: number
          - `unit`: km/s
        - `theta_D`:
          - `type`: number
          - `unit`: K
    - `Hf3N4`:
      - `type`: object
      - `required`: `rho`, `vt`, `vl`, `vm`, `theta_D`
      - `properties`:
        - `rho`:
          - `type`: number
          - `unit`: g/cm³
        - `vt`:
          - `type`: number
          - `unit`: km/s
        - `vl`:
          - `type`: number
          - `unit`: km/s
        - `vm`:
          - `type`: number
          - `unit`: km/s
        - `theta_D`:
          - `type`: number
          - `unit`: K

### step_04_optical_constants.json
- path: `/app/outputs/step_04_optical_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constant and refractive index extracted from the DFT dielectric function.
- schema:
  - `type`: object
  - `required`: `Zr3N4`, `Hf3N4`
  - `properties`:
    - `Zr3N4`:
      - `type`: object
      - `required`: `epsilon0`, `n0`
      - `properties`:
        - `epsilon0`:
          - `type`: number
          - `unit`: dimensionless
        - `n0`:
          - `type`: number
          - `unit`: dimensionless
    - `Hf3N4`:
      - `type`: object
      - `required`: `epsilon0`, `n0`
      - `properties`:
        - `epsilon0`:
          - `type`: number
          - `unit`: dimensionless
        - `n0`:
          - `type`: number
          - `unit`: dimensionless

Notes: All values are to be computed from first‑principles DFT using the specified crystal structures, pseudopotentials, and numerical protocols. The hidden checker compares each field against the corresponding paper‑reported value using tolerances that account for code‑to‑code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Zr3N4",
          "Hf3N4"
        ],
        "properties": {
          "Zr3N4": {
            "type": "object",
            "required": [
              "a0",
              "B0",
              "Bprime"
            ],
            "properties": {
              "a0": {
                "type": "number",
                "unit": "Å"
              },
              "B0": {
                "type": "number",
                "unit": "GPa"
              },
              "Bprime": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          },
          "Hf3N4": {
            "type": "object",
            "required": [
              "a0",
              "B0",
              "Bprime"
            ],
            "properties": {
              "a0": {
                "type": "number",
                "unit": "Å"
              },
              "B0": {
                "type": "number",
                "unit": "GPa"
              },
              "Bprime": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          }
        }
      },
      "description": "Equilibrium lattice constant, bulk modulus and pressure derivative for the two compounds, extracted from DFT relaxation and Birch‑Murnaghan equation‑of‑state fitting."
    },
    {
      "file": "step_02_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Zr3N4",
          "Hf3N4"
        ],
        "properties": {
          "Zr3N4": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "B",
              "G",
              "E",
              "nu"
            ],
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "B": {
                "type": "number",
                "unit": "GPa"
              },
              "G": {
                "type": "number",
                "unit": "GPa"
              },
              "E": {
                "type": "number",
                "unit": "GPa"
              },
              "nu": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          },
          "Hf3N4": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "B",
              "G",
              "E",
              "nu"
            ],
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "B": {
                "type": "number",
                "unit": "GPa"
              },
              "G": {
                "type": "number",
                "unit": "GPa"
              },
              "E": {
                "type": "number",
                "unit": "GPa"
              },
              "nu": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          }
        }
      },
      "description": "Single‑crystal elastic constants and Voigt–Reuss–Hill polycrystalline moduli (bulk, shear, Young’s moduli and Poisson’s ratio) for the two compounds."
    },
    {
      "file": "step_03_sound_velocities_debye.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Zr3N4",
          "Hf3N4"
        ],
        "properties": {
          "Zr3N4": {
            "type": "object",
            "required": [
              "rho",
              "vt",
              "vl",
              "vm",
              "theta_D"
            ],
            "properties": {
              "rho": {
                "type": "number",
                "unit": "g/cm³"
              },
              "vt": {
                "type": "number",
                "unit": "km/s"
              },
              "vl": {
                "type": "number",
                "unit": "km/s"
              },
              "vm": {
                "type": "number",
                "unit": "km/s"
              },
              "theta_D": {
                "type": "number",
                "unit": "K"
              }
            }
          },
          "Hf3N4": {
            "type": "object",
            "required": [
              "rho",
              "vt",
              "vl",
              "vm",
              "theta_D"
            ],
            "properties": {
              "rho": {
                "type": "number",
                "unit": "g/cm³"
              },
              "vt": {
                "type": "number",
                "unit": "km/s"
              },
              "vl": {
                "type": "number",
                "unit": "km/s"
              },
              "vm": {
                "type": "number",
                "unit": "km/s"
              },
              "theta_D": {
                "type": "number",
                "unit": "K"
              }
            }
          }
        }
      },
      "description": "Mass density, transverse/longitudinal/average sound velocities, and Debye temperature computed from polycrystalline moduli and lattice constant."
    },
    {
      "file": "step_04_optical_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Zr3N4",
          "Hf3N4"
        ],
        "properties": {
          "Zr3N4": {
            "type": "object",
            "required": [
              "epsilon0",
              "n0"
            ],
            "properties": {
              "epsilon0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "n0": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          },
          "Hf3N4": {
            "type": "object",
            "required": [
              "epsilon0",
              "n0"
            ],
            "properties": {
              "epsilon0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "n0": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          }
        }
      },
      "description": "Static dielectric constant and refractive index extracted from the DFT dielectric function."
    }
  ],
  "notes": "All values are to be computed from first‑principles DFT using the specified crystal structures, pseudopotentials, and numerical protocols. The hidden checker compares each field against the corresponding paper‑reported value using tolerances that account for code‑to‑code differences."
}
```

## How you are scored
Each JSON output file is scored by a hidden verifier that compares your computed numeric fields to independent reference values derived from the original study. The comparison is performed field by field with relative tolerances that account for the normal spread between different DFT implementations and pseudopotential libraries. For each field the verifier computes the relative absolute error and maps it to a score via a piecewise linear ramp: full credit when the error is below the tolerance, zero credit when it exceeds twice the tolerance, and a linear decrease in between. The final reward is a weighted sum of the per‑field scores across all four artifacts. The tolerances are chosen so that a correct, well‑converged DFT calculation with a mainstream GGA‑PBE pseudopotential set will receive a high score, while simple guesses or physically unreasonable results will not. You do not need to match any particular reference value exactly — only to stay within the expected accuracy of the method.
