# Na Adsorption and Electrochemical Properties of MoSSe Monolayer from DFT

## Problem background
This task investigates the Janus MoSSe monolayer as a flexible anode material for sodium-ion batteries using density functional theory (DFT). The paper computes structural, electronic, and mechanical properties, Na adsorption thermodynamics, ion diffusion barriers, and electrode performance metrics to assess MoSSe as a high-capacity, low-voltage, mechanically robust anode. You will reproduce the key computed electrochemical and mechanical properties.

## Approach
The computational approach uses plane-wave DFT with the PBE functional and Grimme D2 van der Waals correction. A 3×3×1 supercell of the Janus MoSSe monolayer is first geometry-optimized. The adsorption of a single Na atom is computed on several candidate sites on both the S and Se sides to identify the preferred adsorption positions. Migrating Na atoms between neighboring sites is studied with the climbing-image nudged elastic band (CI-NEB) method, yielding diffusion barriers on each surface. Electrode performance is evaluated by adding Na atoms sequentially in layers up to Na₈MoSSe; after full ionic relaxation, total energies, lattice parameters, and thickness are recorded. From these, average and layer adsorption energies, the anode voltage profile, the theoretical specific capacity, and volume expansion are derived. Mechanical flexibility is probed by applying uniaxial (x, y) and biaxial (xy) tensile strains to the pristine monolayer; strain energy and stress‑strain curves are computed, and Young’s moduli, ultimate strains, and breaking strengths are extracted. All calculations use consistent settings (plane-wave cutoff ≥ 400 eV, adequate k‑point mesh for the 3×3 supercell, vacuum > 30 Å). The workflow can be implemented with an open‑source DFT code such as Quantum ESPRESSO.

## Reproduction target
Produce three JSON files under `/app/outputs`:

1. `mechanical_properties.json` — Young's modulus (GPa), ultimate strain (dimensionless), and breaking strength (GPa) for uniaxial tension along x and y, and for biaxial tension along xy.
2. `diffusion_barriers.json` — Na diffusion barriers (eV) on the Se surface and on the S surface along Path I (the minimum‑energy migration route between neighboring top‑of‑Mo sites).
3. `adsorption_energies.json` — for each Na concentration x = 1 through 8 in NaₓMoSSe, report the theoretical specific capacity (mAh/g), average adsorption energy (eV), layer adsorption energy (eV), anode voltage (V), and volume expansion (%).

These quantities must be derived from the DFT procedures described in the workflow steps; simply looking up or fabricating numbers will not pass the hidden structural checks.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency library: https://www.materialscloud.org/discover/sssp/table/efficiency
- CI-NEB implementation (Quantum ESPRESSO neb.x): https://www.quantum-espresso.org/
- Python (numpy, scipy, matplotlib): python3

## Workflow steps

### Step 1: Relax MoSSe monolayer structure
- Role: process
- Action: Perform geometry optimization of a 3x3x1 supercell of Janus MoSSe monolayer using DFT (PBE functional with Grimme D2 dispersion correction, vacuum >30 Angstrom, adequate k-mesh). Converge forces to <0.02 eV/Angstrom and total energy to 10^-5 eV. Save the relaxed structure for all subsequent calculations.
- Evidence: `/app/outputs/mosse_relaxed.json`

### Step 2: Compute mechanical properties under strain
- Role: scored
- Action: Apply uniaxial tensile strains along x and y directions and biaxial tension along xy to the relaxed MoSSe monolayer. Calculate strain energy as a function of strain, and from it derive stress-strain curves. Extract Young's modulus, ultimate strain, and breaking strength for each direction. Write the results to mechanical_properties.json.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: JSON object with keys 'x', 'y', 'xy'. Each value is an object with fields: Young_modulus_GPa (float), ultimate_strain (float), breaking_strength_GPa (float).
- Scoring: scored by hidden verifier

### Step 3: Single Na adsorption site determination
- Role: process
- Action: Compute adsorption energies of a single Na atom on Tm (top of Mo) and H (top of hexagon) sites on both the Se side and S side of the MoSSe monolayer. Identify the most stable site on each side (lowest adsorption energy) to be used as the preferred site for subsequent multilayer adsorption.
- Evidence: `/app/outputs/single_na_sites.json`

### Step 4: Na diffusion barriers via NEB
- Role: scored
- Action: Using the climbing-image nudged elastic band (CI-NEB) method, calculate the minimum energy path for Na migration between neighboring Tm sites on the Se surface (Path I) and on the S surface (Path I). Determine the diffusion barriers. Write the results to diffusion_barriers.json.
- Output file: `/app/outputs/diffusion_barriers.json`
- Format: json
- Contract: JSON object with keys: Se_side_pathI_barrier_eV (float), S_side_pathI_barrier_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Layer-by-layer Na adsorption and electrode properties
- Role: scored (load-bearing)
- Action: Sequentially add up to 8 Na layers on MoSSe according to the preferred adsorption sites identified in step3. For each composition Na_xMoSSe (x=1..8), perform full ionic relaxation, compute total energy, lattice parameters, and thickness. From these, calculate the average adsorption energy E_avg, layer adsorption energy E_layer, anode voltage for each intermediate composition, theoretical specific capacity at x=8, and volume expansion. Write all results to adsorption_energies.json.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with keys '1' through '8' (strings). Each value is an object with fields: capacity_mAh_g (float), E_avg_eV (float), E_layer_eV (float), voltage_V (float), volume_expansion_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_properties.json`
- `/app/outputs/diffusion_barriers.json`
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anisotropic Young's moduli, ultimate strains, and breaking strengths of MoSSe monolayer under uniaxial and biaxial tension.
- schema:
  - `type`: object
  - `required`: `x`, `y`, `xy`
  - `items`:
    - `x`:
      - `type`: object
      - `required`: `Young_modulus_GPa`, `ultimate_strain`, `breaking_strength_GPa`
      - `units`:
        - `Young_modulus_GPa`: GPa
        - `ultimate_strain`: dimensionless
        - `breaking_strength_GPa`: GPa
    - `y`:
      - `type`: object
      - `required`: `Young_modulus_GPa`, `ultimate_strain`, `breaking_strength_GPa`
      - `units`:
        - `Young_modulus_GPa`: GPa
        - `ultimate_strain`: dimensionless
        - `breaking_strength_GPa`: GPa
    - `xy`:
      - `type`: object
      - `required`: `Young_modulus_GPa`, `ultimate_strain`, `breaking_strength_GPa`
      - `units`:
        - `Young_modulus_GPa`: GPa
        - `ultimate_strain`: dimensionless
        - `breaking_strength_GPa`: GPa

### diffusion_barriers.json
- path: `/app/outputs/diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Sodium diffusion barriers on Se and S surfaces along Path I.
- schema:
  - `type`: object
  - `required`: `Se_side_pathI_barrier_eV`, `S_side_pathI_barrier_eV`
  - `items`:
    - `Se_side_pathI_barrier_eV`:
      - `type`: number
      - `unit`: eV
    - `S_side_pathI_barrier_eV`:
      - `type`: number
      - `unit`: eV

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Average and layer adsorption energies, voltage, specific capacity, and volume expansion for Na_xMoSSe (x=1..8).
- schema:
  - `type`: object
  - `required`: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`
  - `items`:
    - `1`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `2`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `3`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `4`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `5`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `6`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `7`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent
    - `8`:
      - `type`: object
      - `required`: `capacity_mAh_g`, `E_avg_eV`, `E_layer_eV`, `voltage_V`, `volume_expansion_percent`
      - `units`:
        - `capacity_mAh_g`: mAh/g
        - `E_avg_eV`: eV
        - `E_layer_eV`: eV
        - `voltage_V`: V
        - `volume_expansion_percent`: percent

Notes: All numerical comparisons will use appropriate tolerances. The checker expects a JSON object with keys '1' through '8', each containing the required fields.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "x",
          "y",
          "xy"
        ],
        "items": {
          "x": {
            "type": "object",
            "required": [
              "Young_modulus_GPa",
              "ultimate_strain",
              "breaking_strength_GPa"
            ],
            "units": {
              "Young_modulus_GPa": "GPa",
              "ultimate_strain": "dimensionless",
              "breaking_strength_GPa": "GPa"
            }
          },
          "y": {
            "type": "object",
            "required": [
              "Young_modulus_GPa",
              "ultimate_strain",
              "breaking_strength_GPa"
            ],
            "units": {
              "Young_modulus_GPa": "GPa",
              "ultimate_strain": "dimensionless",
              "breaking_strength_GPa": "GPa"
            }
          },
          "xy": {
            "type": "object",
            "required": [
              "Young_modulus_GPa",
              "ultimate_strain",
              "breaking_strength_GPa"
            ],
            "units": {
              "Young_modulus_GPa": "GPa",
              "ultimate_strain": "dimensionless",
              "breaking_strength_GPa": "GPa"
            }
          }
        }
      },
      "description": "Anisotropic Young's moduli, ultimate strains, and breaking strengths of MoSSe monolayer under uniaxial and biaxial tension."
    },
    {
      "file": "diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Se_side_pathI_barrier_eV",
          "S_side_pathI_barrier_eV"
        ],
        "items": {
          "Se_side_pathI_barrier_eV": {
            "type": "number",
            "unit": "eV"
          },
          "S_side_pathI_barrier_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Sodium diffusion barriers on Se and S surfaces along Path I."
    },
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8"
        ],
        "items": {
          "1": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "2": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "3": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "4": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "5": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "6": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "7": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          },
          "8": {
            "type": "object",
            "required": [
              "capacity_mAh_g",
              "E_avg_eV",
              "E_layer_eV",
              "voltage_V",
              "volume_expansion_percent"
            ],
            "units": {
              "capacity_mAh_g": "mAh/g",
              "E_avg_eV": "eV",
              "E_layer_eV": "eV",
              "voltage_V": "V",
              "volume_expansion_percent": "percent"
            }
          }
        }
      },
      "description": "Average and layer adsorption energies, voltage, specific capacity, and volume expansion for Na_xMoSSe (x=1..8)."
    }
  ],
  "notes": "All numerical comparisons will use appropriate tolerances. The checker expects a JSON object with keys '1' through '8', each containing the required fields."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads only the three output files. The verifier first validates that each file matches its specified schema (correct keys, numeric types). It then compares each reported value to a hidden reference with appropriate tolerances. In addition, it applies several structural consistency checks that a genuine DFT run would satisfy:
- The average adsorption energy (`E_avg_eV`) should decrease monotonically with increasing Na concentration.
- All layer adsorption energies (`E_layer_eV`) must be negative (indicating exothermic adsorption).
- The voltage should exhibit a low plateau at high Na concentrations.
- The diffusion barrier on the Se side should be lower than on the S side.
- The biaxial Young’s modulus should exceed the uniaxial moduli, and the mechanical properties should be roughly isotropic.
- The theoretical specific capacity at x=8 should lie near the value expected for full sodiation of the monolayer.

The final reward (a number between 0 and 1) is a weighted combination of the scores from all three artifacts, with `adsorption_energies.json` carrying the largest weight. Simple reporting of paper numbers without actual computation is unlikely to satisfy these consistency checks.
