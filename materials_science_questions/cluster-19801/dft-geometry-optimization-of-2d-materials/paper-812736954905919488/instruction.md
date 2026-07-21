# Mechanical and thermodynamic properties of 2D monoclinic Ga2O3 from first principles

## Problem background
Beta-gallium oxide (β-Ga2O3) is an ultra-wide-bandgap semiconductor attractive for high-power electronics and deep-UV detection. Recently, two-dimensional (2D) forms of Ga2O3 have been fabricated, opening new possibilities for flexible, high-performance devices. The mechanical and thermodynamic properties of these 2D layers—elastic constants, sound velocities, Debye temperature, thermal conductivity, and heat capacity—are critical for device design and thermal management but remain largely unexplored from first principles. This task uses density functional theory (DFT) to determine how these properties evolve when bulk β-Ga2O3 is thinned down to monolayer, bilayer, and trilayer slabs, providing the quantitative data needed to assess the material's suitability for nanoscale devices.

## Approach
The core idea is a computational pipeline that starts from the atomic structure of monoclinic Ga2O3 and ends with its thermodynamic figures of merit. First, construct four structural models: bulk β-Ga2O3 (C2/m symmetry) and hydrogen-passivated slabs of one, two, and three Ga2O3 layers obtained by cleaving the bulk along the (100) surface. Then, perform DFT geometry optimization for each system to relax atomic positions and lattice parameters. On the relaxed structures, compute the complete elastic constant matrix (13 independent constants for monoclinic symmetry) via stress-strain methodology within DFT. From these elastic constants, apply Voigt–Reuss–Hill averaging to extract polycrystalline elastic moduli (bulk, shear, Young's), Poisson's ratio, and compressive/shear anisotropy indices. Finally, using the derived Young's modulus, Poisson's ratio, and structural parameters (mass density, unit‑cell mass, number of atoms, atomic area), evaluate analytical formulas from the literature to obtain the longitudinal, transverse, and average sound velocities, the Debye temperature, the minimum thermal conductivity, and the saturated high‑temperature limit of the isochoric specific heat capacity. Each stage feeds its outputs into the next; the entire workflow is ordered to produce the final thermodynamic quantities.

## Reproduction target
Compute and report the following quantities for bulk β-Ga2O3, hydrogen-passivated monolayer Ga2O3, bilayer Ga2O3, and trilayer Ga2O3: (1) the thirteen independent elastic constants C11, C22, C33, C44, C55, C66, C12, C13, C15, C23, C25, C35, C46, with values in GPa for bulk and N/m for slabs; (2) the polycrystalline elastic moduli—bulk modulus, shear modulus, Young's modulus, Poisson's ratio—and the anisotropy indices A_B and A_G; (3) the longitudinal (v_l), transverse (v_t), and average (v_m) sound velocities, the Debye temperature (Θ_D), the minimum thermal conductivity (k_min), and the saturated high‑temperature specific heat capacity (saturated_C_V). All results must be written to the three output JSON files specified in the workflow steps. The target is to derive these quantities entirely from the DFT calculations and subsequent analytical post‑processing without relying on pre‑computed results.

## Assets

- Open-source DFT package (e.g., Quantum ESPRESSO): quantum-espresso
- LDA pseudopotentials for Ga and O (standard libraries, e.g., SSSP efficiency): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Construct structural models
- Role: process
- Action: Construct initial atomic structures for bulk β-Ga2O3 (C2/m symmetry) and hydrogen-passivated monolayer, bilayer, and trilayer Ga2O3 slabs by slicing the bulk along the (100) surface and adding vacuum.
- Evidence: `/app/outputs/initial_models.log`

### Step 2: DFT geometry optimization
- Role: process
- Action: For each system (bulk, monolayer, bilayer, trilayer), perform DFT geometry optimization to relax atomic positions and cell parameters. Choose appropriate exchange‑correlation functional and pseudopotentials, and converge forces and total energy to suitable thresholds.
- Evidence: `/app/outputs/geo_optimization.log`

### Step 3: Compute elastic constants
- Role: scored
- Action: Calculate the complete elastic constant matrix for each optimized structure using DFT. Output all 13 independent elastic constants for bulk (in GPa) and for each slab (in N/m).
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: Array of objects. Each object contains keys: system (one of 'bulk', 'monolayer', 'bilayer', 'trilayer'), C11, C22, C33, C44, C55, C66, C12, C13, C15, C23, C25, C35, C46 (all numeric).
- Scoring: scored by hidden verifier

### Step 4: Derive elastic moduli and anisotropy
- Role: scored
- Action: From the elastic constants, use averaging methods to compute for each system: bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and anisotropy indices.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: Array of objects. Each object contains keys: system ('bulk', 'monolayer', 'bilayer', 'trilayer'), bulk_modulus (float, GPa for bulk, N/m for slabs), shear_modulus (float, same units), Youngs_modulus (float, same units), Poisson_ratio (float, dimensionless), anisotropy_index_B (float, dimensionless), anisotropy_index_G (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Compute thermal properties
- Role: scored (load-bearing)
- Action: Using the derived moduli, structural parameters, and analytical formulas from the literature, compute the longitudinal, transverse, and average sound velocities, the Debye temperature, the minimum thermal conductivity, and the saturated high-temperature specific heat capacity for each system.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: Array of objects. Each object contains keys: system ('bulk', 'monolayer', 'bilayer', 'trilayer'), k_min (float, W cm⁻¹ K⁻¹), Theta_D (float, K), v_m (float, m s⁻¹), v_l (float, m s⁻¹), v_t (float, m s⁻¹), saturated_C_V (float, J mol⁻¹ K⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/mechanical_properties.json`
- `/app/outputs/thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Full set of 13 independent elastic constants for bulk β-Ga2O3 and the three 2D thicknesses.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `C11`, `C22`, `C33`, `C44`, `C55`, `C66`, `C12`, `C13`, `C15`, `C23`, `C25`, `C35`, `C46`
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `bulk`, `monolayer`, `bilayer`, `trilayer`
      - `C11`: number (GPa for bulk, N/m for slabs)
      - `C22`: number
      - `C33`: number
      - `C44`: number
      - `C55`: number
      - `C66`: number
      - `C12`: number
      - `C13`: number
      - `C15`: number
      - `C23`: number
      - `C25`: number
      - `C35`: number
      - `C46`: number

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline elastic moduli and anisotropy indices derived from elastic constants.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `bulk_modulus`, `shear_modulus`, `Youngs_modulus`, `Poisson_ratio`, `anisotropy_index_B`, `anisotropy_index_G`
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `bulk`, `monolayer`, `bilayer`, `trilayer`
      - `bulk_modulus`: number (GPa for bulk, N/m for slabs)
      - `shear_modulus`: number (same units as bulk_modulus)
      - `Youngs_modulus`: number (same units)
      - `Poisson_ratio`: number (dimensionless)
      - `anisotropy_index_B`: number (dimensionless)
      - `anisotropy_index_G`: number (dimensionless)

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic quantities: sound velocities, Debye temperature, minimum thermal conductivity, and saturated heat capacity.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `k_min`, `Theta_D`, `v_m`, `v_l`, `v_t`, `saturated_C_V`
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `bulk`, `monolayer`, `bilayer`, `trilayer`
      - `k_min`: number (W·cm⁻¹·K⁻¹)
      - `Theta_D`: number (K)
      - `v_m`: number (m s⁻¹)
      - `v_l`: number (m s⁻¹)
      - `v_t`: number (m s⁻¹)
      - `saturated_C_V`: number (J·mol⁻¹·K⁻¹)

Notes: All values must be computed from the DFT results and analytical formulas; the solver should use open-source DFT software and standard pseudopotentials. The checker will compare the reported numbers to the paper's reference values with tolerances that account for differences in DFT implementations.

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
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "C11",
            "C22",
            "C33",
            "C44",
            "C55",
            "C66",
            "C12",
            "C13",
            "C15",
            "C23",
            "C25",
            "C35",
            "C46"
          ],
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "bulk",
                "monolayer",
                "bilayer",
                "trilayer"
              ]
            },
            "C11": "number (GPa for bulk, N/m for slabs)",
            "C22": "number",
            "C33": "number",
            "C44": "number",
            "C55": "number",
            "C66": "number",
            "C12": "number",
            "C13": "number",
            "C15": "number",
            "C23": "number",
            "C25": "number",
            "C35": "number",
            "C46": "number"
          }
        }
      },
      "description": "Full set of 13 independent elastic constants for bulk β-Ga2O3 and the three 2D thicknesses."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "bulk_modulus",
            "shear_modulus",
            "Youngs_modulus",
            "Poisson_ratio",
            "anisotropy_index_B",
            "anisotropy_index_G"
          ],
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "bulk",
                "monolayer",
                "bilayer",
                "trilayer"
              ]
            },
            "bulk_modulus": "number (GPa for bulk, N/m for slabs)",
            "shear_modulus": "number (same units as bulk_modulus)",
            "Youngs_modulus": "number (same units)",
            "Poisson_ratio": "number (dimensionless)",
            "anisotropy_index_B": "number (dimensionless)",
            "anisotropy_index_G": "number (dimensionless)"
          }
        }
      },
      "description": "Polycrystalline elastic moduli and anisotropy indices derived from elastic constants."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "k_min",
            "Theta_D",
            "v_m",
            "v_l",
            "v_t",
            "saturated_C_V"
          ],
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "bulk",
                "monolayer",
                "bilayer",
                "trilayer"
              ]
            },
            "k_min": "number (W·cm⁻¹·K⁻¹)",
            "Theta_D": "number (K)",
            "v_m": "number (m s⁻¹)",
            "v_l": "number (m s⁻¹)",
            "v_t": "number (m s⁻¹)",
            "saturated_C_V": "number (J·mol⁻¹·K⁻¹)"
          }
        }
      },
      "description": "Thermodynamic quantities: sound velocities, Debye temperature, minimum thermal conductivity, and saturated heat capacity."
    }
  ],
  "notes": "All values must be computed from the DFT results and analytical formulas; the solver should use open-source DFT software and standard pseudopotentials. The checker will compare the reported numbers to the paper's reference values with tolerances that account for differences in DFT implementations."
}
```

## How you are scored
A hidden verifier evaluates each output artifact (elastic constants, mechanical properties, thermodynamic properties) independently. For every reported quantity, the verifier compares your value against a reference value that reflects a correct re‑run of the procedure. The comparison uses tolerances that account for legitimate differences between DFT codes and pseudopotentials, so an accurate reproduction will score well. Additionally, the verifier checks that the thickness‑dependent trends are physically meaningful (e.g., certain quantities should increase or decrease monotonically as the number of layers changes). Each artifact contributes a weighted share to the final reward, which is a single float in [0,1]. Reporting numbers alone is not enough; the verifier expects the values to originate from a genuine execution of the DFT pipeline as described in the workflow.
