# Molecular Statics Dislocation Core Critical Stress and Compliance

## Problem background
Body-centred cubic (bcc) metals and alloys, including the ordered DO3 intermetallic Fe3Al, deviate from Schmid’s law: the critical resolved shear stress (CRSS) depends on loading orientation and sense due to two effects — (i) twin-antitwin (TA) slip asymmetry and (ii) non-glide shear (NGS) stress components that couple with the non-planar core of screw dislocations. Understanding how NGS components alter the dislocation core structure and consequently the critical glide shear stress is central to predicting the orientation-dependent yield behaviour of DO3-Fe3Al. In this task you will investigate this behaviour by performing molecular statics simulations of dissociated 1/4<111> superpartial dislocations under uniaxial compression along three different crystallographic directions.

## Approach
You will build a simulation cell containing a DO3-Fe3Al crystal oriented such that the coordinate axes x1, x2, x3 lie along [1̅ 2 1], [1 0 1], and [1̅ 1 1], respectively. A superdislocation dissociated into four 1/4[1̅ 1 1] screw superpartials will be introduced using the anisotropic elasticity displacement fields from the Stroh‑Eshelby formalism, with initial separations that reflect the nearest‑ and next‑nearest‑neighbour anti‑phase boundary (APB) distances. After relaxing the cell to equilibrium, you will incrementally apply homogeneous strains corresponding to uniaxial compression along [1 5 11], [0 0 1], and [20 31 36]. For each orientation the strain is proportional to a single loading coefficient (η, λ, or ω) and is derived from the orientation‑specific uniaxial stress tensor expressed in the simulation frame. At each increment you will relax the cell and detect when the leading partial begins to glide. From the coefficient at glide onset you will compute the critical glide shear stress component σ′23 on the active (1 0 1) [1̅ 1 1] slip system. You will also evaluate the elastic compliance coupling components S′2321 and S′2323 from the given DO3 elastic constants and the rotation matrix from the crystal frame to the simulation frame.

## Reproduction target
Produce a JSON file `/app/outputs/critical_coefficients.json` containing:
- For each orientation identified by the keys `"203136"`, `"1511"`, and `"001"`: the loading coefficient at which the leading partial started to move, and the corresponding critical sigma′23 (in MPa) derived from that coefficient and the stress tensor expression for that orientation.
- The elastic compliance components S′2321 and S′2323 (both in GPa⁻¹) computed from the DO3 elastic constants C1111=165 GPa, C1122=125 GPa, C1212=142 GPa and the appropriate coordinate rotation.
The file must follow the schema: an object with exactly those five top‑level keys; each orientation key maps to an object containing `"coefficient"` (number) and `"critical_sigma_23_MPa"` (number); `"S_prime_2321"` and `"S_prime_2323"` are numbers. No other external information is needed.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- Fe-Al EAM potential (Mendelev et al., 2005): https://www.ctcms.nist.gov/potentials/Fe-Al.html
- Elastic constants of DO3-Fe3Al

## Workflow steps

### Step 1: Build and relax the dislocated simulation cell
- Role: process
- Action: Create a rectangular parallelpiped simulation box with DO3-Fe3Al crystal oriented such that x1∥[1̅ 2 1], x2∥[1 0 1], x3∥[1̅ 1 1]. Insert four 1/4[1̅ 1 1] screw superpartials at initial separations d1=d3=20 nm (NNAPB) and d2=30 nm (NNNAPB). Impose anisotropic screw dislocation displacement fields using the Stroh-Eshelby formalism. Fix atoms on (1̅ 2 1) and (1 0 1) boundaries; apply periodic boundaries along x3. Relax with the Fe-Al EAM potential until max force < 0.015 eV/Å.
- Evidence: `/app/outputs/unstressed_relax.log`

### Step 2: Compute critical glide shear stress for three orientations
- Role: scored (load-bearing)
- Action: For each compression orientation [1 5 11], [0 0 1], [20 31 36] (referred to in the output as '1511', '001', '203136'), increment the proportional loading coefficient (η, λ, ω) starting from zero. At each increment apply the homogeneous strain corresponding to the uniaxial stress tensors expressed in the x1-x2-x3 simulation frame. The stress tensors (in MPa) are:
  - [1 5 11]: σ = η [[0, 0, 0], [0, -0.49, -0.50], [0, -0.50, -0.51]]
  - [0 0 1]: σ = λ [[-0.16, -0.29, -0.23], [-0.29, -0.50, -0.41], [-0.23, -0.41, -0.33]]
  - [20 31 36]: σ = ω [[-0.13, 0.28, 0.19], [0.28, -0.59, -0.40], [0.19, -0.40, -0.28]]
  Relax the cell and check if the leading partial has moved (centre displacement exceeding a threshold). Record the coefficient at the onset of glide. Compute the critical sigma'_23 (in MPa) from the recorded coefficient and the stress tensor expressions. Also calculate the elastic compliance components S'_2321 and S'_2323 (in GPa⁻¹) from the given DO3 elastic constants Cij and the rotation matrix from the DO3 crystal frame to the x1-x2-x3 frame.
- Output file: `/app/outputs/critical_coefficients.json`
- Format: json
- Contract: type=object; required=['203136', '1511', '001', 'S_prime_2321', 'S_prime_2323']; properties={'203136': {'type': 'object', 'required': ['coefficient', 'critical_sigma_23_MPa'], 'properties': {'coefficient': {'type': 'number'}, 'critical_sigma_23_MPa': {'type': 'number', 'units': 'MPa'}}}, '1511': {'type': 'object', 'required': ['coefficient', 'critical_sigma_23_MPa'], 'properties': {'coefficient': {'type': 'number'}, 'critical_sigma_23_MPa': {'type': 'number', 'units': 'MPa'}}}, '001': {'type': 'object', 'required': ['coefficient', 'critical_sigma_23_MPa'], 'properties': {'coefficient': {'type': 'number'}, 'critical_sigma_23_MPa': {'type': 'number', 'units': 'MPa'}}}, 'S_prime_2321': {'type': 'number', 'units': 'GPa^-1'}, 'S_prime_2323': {'type': 'number', 'units': 'GPa^-1'}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_coefficients.json
- path: `/app/outputs/critical_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical loading coefficients, derived glide shear stresses, and elastic compliance components from MS core-structure simulations for three orientations. The checker compares reported values to hidden paper-reported gold within tolerances and verifies the CRSS ordering trend.
- schema:
  - `type`: object
  - `required`: `203136`, `1511`, `001`, `S_prime_2321`, `S_prime_2323`
  - `properties`:
    - `203136`:
      - `type`: object
      - `required`: `coefficient`, `critical_sigma_23_MPa`
      - `properties`:
        - `coefficient`:
          - `type`: number
        - `critical_sigma_23_MPa`:
          - `type`: number
          - `units`: MPa
    - `1511`:
      - `type`: object
      - `required`: `coefficient`, `critical_sigma_23_MPa`
      - `properties`:
        - `coefficient`:
          - `type`: number
        - `critical_sigma_23_MPa`:
          - `type`: number
          - `units`: MPa
    - `001`:
      - `type`: object
      - `required`: `coefficient`, `critical_sigma_23_MPa`
      - `properties`:
        - `coefficient`:
          - `type`: number
        - `critical_sigma_23_MPa`:
          - `type`: number
          - `units`: MPa
    - `S_prime_2321`:
      - `type`: number
      - `units`: GPa^-1
    - `S_prime_2323`:
      - `type`: number
      - `units`: GPa^-1

Notes: The agent must implement the Stroh-Eshelby anisotropic displacement fields and the incremental loading protocol from the given setup. The stress tensor expressions for each orientation are derived from uniaxial loading in the simulation frame and are proportional to a single coefficient; the agent should construct them from the orientation-specific matrices provided in the task background.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "203136",
          "1511",
          "001",
          "S_prime_2321",
          "S_prime_2323"
        ],
        "properties": {
          "203136": {
            "type": "object",
            "required": [
              "coefficient",
              "critical_sigma_23_MPa"
            ],
            "properties": {
              "coefficient": {
                "type": "number"
              },
              "critical_sigma_23_MPa": {
                "type": "number",
                "units": "MPa"
              }
            }
          },
          "1511": {
            "type": "object",
            "required": [
              "coefficient",
              "critical_sigma_23_MPa"
            ],
            "properties": {
              "coefficient": {
                "type": "number"
              },
              "critical_sigma_23_MPa": {
                "type": "number",
                "units": "MPa"
              }
            }
          },
          "001": {
            "type": "object",
            "required": [
              "coefficient",
              "critical_sigma_23_MPa"
            ],
            "properties": {
              "coefficient": {
                "type": "number"
              },
              "critical_sigma_23_MPa": {
                "type": "number",
                "units": "MPa"
              }
            }
          },
          "S_prime_2321": {
            "type": "number",
            "units": "GPa^-1"
          },
          "S_prime_2323": {
            "type": "number",
            "units": "GPa^-1"
          }
        }
      },
      "description": "Critical loading coefficients, derived glide shear stresses, and elastic compliance components from MS core-structure simulations for three orientations. The checker compares reported values to hidden paper-reported gold within tolerances and verifies the CRSS ordering trend."
    }
  ],
  "notes": "The agent must implement the Stroh-Eshelby anisotropic displacement fields and the incremental loading protocol from the given setup. The stress tensor expressions for each orientation are derived from uniaxial loading in the simulation frame and are proportional to a single coefficient; the agent should construct them from the orientation-specific matrices provided in the task background."
}
```

## How you are scored
A hidden verifier will automatically score your submission. It reads `/app/outputs/critical_coefficients.json` and compares the critical sigma′23 values you derived for the three orientations against hidden reference values determined from the paper’s own results, within an allowed tolerance. It also checks whether the ordering of the critical sigma′23 magnitudes among the three orientations matches the expected trend. In addition, the verifier compares your reported S′2321 and S′2323 compliance components to hidden reference values within a tolerance. The critical stress values carry a combined weight of 0.8, and the two compliance components carry a weight of 0.2. The final reward is a number between 0 and 1 reflecting the aggregate agreement. You must write the artifact exactly as specified; merely reporting the paper’s numbers is not sufficient—the verifier expects values that are consistent with having genuinely executed the described workflow.
