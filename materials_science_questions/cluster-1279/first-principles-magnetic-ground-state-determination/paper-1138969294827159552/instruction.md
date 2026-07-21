# Magnetic Ground State Determination of RhY₂O₄ Spinel via First-Principles DFT

## Problem background
RhY₂O₄ is an oxide spinel material with a cubic crystal structure (space group Fd-3m) that exhibits semiconducting character, making it a candidate for semiconductor and spintronic applications. Assessing its potential requires detailed knowledge of its magnetic ground state, structural parameters, electronic band gaps, elastic stability, and magnetic moments. This task uses first-principles density functional theory (DFT) to compute these physical properties and to determine whether the ferromagnetic or non-magnetic arrangement of spins is energetically preferred.

## Approach
The computational workflow starts from the experimentally reported cubic crystal structure with known Wyckoff positions. Spin-polarized DFT calculations are performed for both ferromagnetic (FM) and non-magnetic (NM) configurations using the GGA-PBE exchange-correlation functional. For each magnetic phase, the total energy is calculated at several volumes and fitted to the Murnaghan equation of state, yielding the equilibrium lattice constant, bulk modulus, and equilibrium total energy. The FM and NM results are compared to identify the ground-state magnetic order. The same protocol is applied under GGA+U with on-site Coulomb corrections of U = 1, 2, 3, and 4 eV to study how the lattice parameters, bulk moduli, and total energies evolve. Electronic band structures are then computed for the FM phase using GGA, GGA+mBJ, and GGA+U; from these, the valence-band maximum, conduction-band minimum, and band gap are extracted for both majority and minority spin channels. Elastic constants C₁₁, C₁₂, C₄₄ are obtained at zero pressure by applying small distortions to the equilibrium FM structure, and the bulk modulus, shear modulus, Young's modulus, B/G ratio, Poisson's ratio, Cauchy pressure, and Debye temperature are derived through standard elasticity formulas. Finally, the total magnetic moment per formula unit and the partial moments on each atomic species are extracted from the spin-polarized charge density.

**All calculations must be performed with a full-potential linearized augmented plane-wave (FP-LAPW) DFT code (e.g., Elk) using the essential computational parameters listed below. Pseudopotential calculations are not suitable for this task because the reference (gold) values were obtained with the full-potential WIEN2k code, and pseudopotential methods yield absolute total energies and band gaps that are inconsistent with the full-potential results.** Post-processing is done with standard scientific Python libraries for equation-of-state fitting and data aggregation.

## Essential computational parameters
To reproduce the paper’s reference values, you must use exactly the following parameters that correspond to the WIEN2k setup reported in the paper:

- **Exchange-correlation functional**: GGA-PBE (Perdew–Burke–Ernzerhof).
- **Energy cutoff**: –6 Ry (separation energy between core and valence states; states below –6 Ry are treated as core).
- **k-point mesh**: 10 × 10 × 10 (Γ-centered or Monkhorst–Pack mesh; the paper uses 10×10×10 in the full Brillouin zone).
- **Muffin-tin radii (RMT)**: Rh = 2.15 a.u., Y = 2.32 a.u., O = 1.61 a.u. (these values must be imposed in the input; do not rely on automatic determination).

If using the Elk full-potential code, you can enforce these settings by fixing the muffin-tin radii to the above values, using `rgkmax` ≈ 7.0–8.0, and setting the core-valence energy to –6 Ry (the exact syntax depends on the code version; consult the Elk manual). Any other full-potential code that permits the same fixed muffin-tin radii and uses the same functional, energy cutoff, and k-point grid is also acceptable.

## Reproduction target
Execute the computational protocol described above and write the resulting physical quantities—equilibrium lattice constants, bulk moduli, total energies, band gaps for all functionals and spin channels, elastic constants and derived mechanical properties, Debye temperature, magnetic moments, and a confirmation of the magnetic ground state—into the single scored file /app/outputs/properties.json, following the field definitions and units given in the output contract. The objective is to obtain these numbers by re-running the DFT workflow; the hidden verifier will compare each field against an expected reference. Additionally, write the intermediate evidence files listed in the Output files section.

## Assets

- **Open-source full-potential DFT code** (e.g., Elk): https://elk.sourceforge.io/ (Elk is a full-potential FP-LAPW code that can reproduce WIEN2k results when the same parameters are used). **Do not use pseudopotential codes (e.g., Quantum ESPRESSO) for this task.**
- **Python with scipy** (and optionally numpy, matplotlib): scipy

## Workflow steps

### Step 1: Prepare crystal structure
- Role: process
- Action: Construct the cubic crystal structure of RhY2O4 in space group Fd-3m (No. 227) with Rh at Wyckoff position 8a (0.125,0.125,0.125), Y at 16d (0.5,0.5,0.5), and O at 32e (0.25,0.25,0.25). Set the computational parameters as given in the “Essential computational parameters” section and produce a DFT input file.
- Evidence: `/app/outputs/structure_input.txt`

### Step 2: GGA optimization and magnetic ground state determination
- Role: process
- Action: Run spin-polarized (FM) and non-spin-polarized (NM) DFT calculations using GGA-PBE at several volumes, employing the mandated energy cutoff, k‑point grid, and muffin‑tin radii. Fit the total energy versus volume data to the Murnaghan equation of state for each magnetic phase. Extract equilibrium lattice parameter, bulk modulus, and equilibrium total energy. Confirm that FM has lower energy than NM.
- Evidence: `/app/outputs/gga_eos_fit.log`

### Step 3: GGA+U calculations
- Role: process
- Action: Perform spin-polarized DFT calculations on the FM phase using GGA+U with U = 1, 2, 3, and 4 eV, using the same essential parameters. For each U, compute total energy at multiple volumes, fit to Murnaghan equation of state, and extract equilibrium lattice parameter, bulk modulus, and equilibrium total energy.
- Evidence: `/app/outputs/gga_u_eos_fit.log`

### Step 4: Electronic structure calculations
- Role: process
- Action: Using the optimized FM structure from step_02, compute the band structure and density of states under GGA, GGA+mBJ, and GGA+U (with U=1,2,3,4 eV), keeping all computational parameters unchanged. Extract the valence band maximum (VBM), conduction band minimum (CBM), and band gap for majority and minority spins for each approximation. Determine the nature (direct/indirect) of each gap.
- Evidence: `/app/outputs/band_gaps.csv`

### Step 5: Elastic constant calculations
- Role: process
- Action: Using the optimized FM structure from step_02, compute the elastic constants C11, C12, C44 at zero pressure by applying small strains and evaluating stress or total energy changes. The same DFT settings (including muffin‑tin radii, energy cutoff, and k‑point mesh) must be used. Derive bulk modulus B, shear modulus G, B/G ratio, Poisson's ratio ν, Cauchy pressure C12−C44, and Debye temperature ΘD using standard formulas. Determine ductility: according to the Pugh criterion (B/G > 1.75) and the Frantsevich criterion (ν > 0.26), the material is classified as ductile if **both** conditions are satisfied; otherwise it is considered brittle. Set the boolean field `is_ductile` to `true` only when both thresholds are met.
- Evidence: `/app/outputs/elastic_constants.csv`

### Step 6: Magnetic moment extraction
- Role: process
- Action: From the spin-polarized GGA charge/spin density, extract the total magnetic moment per formula unit and the partial magnetic moments on Rh, Y, and O atoms.
- Evidence: `/app/outputs/magnetic_moments.txt`

### Step 7: Aggregate all computed properties into a single scored JSON
- Role: scored (load-bearing)
- Action: Collect every value computed in the previous steps and assemble them into the structured JSON file properties.json according to the contract below.
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: JSON object with the following fields: gga_fm_equilibrium_lattice_constant (number, Å), gga_fm_bulk_modulus (number, GPa), gga_nm_equilibrium_lattice_constant (number, Å), gga_nm_bulk_modulus (number, GPa), gga_fm_total_energy (number, Ry), gga_nm_total_energy (number, Ry), gga_u_lattice_constants (array of 4 numbers for U=1..4 eV in order, unit Å), gga_u_bulk_moduli (array of 4 numbers, unit GPa), gga_u_total_energies (array of 4 numbers, unit Ry), band_gap_majority_gga (number, eV), band_gap_minority_gga (number, eV), band_gap_majority_mbj (number, eV), band_gap_minority_mbj (number, eV), band_gap_majority_u1 (number, eV), band_gap_minority_u1 (number, eV), band_gap_majority_u2 (number, eV), band_gap_minority_u2 (number, eV), band_gap_majority_u3 (number, eV), band_gap_minority_u3 (number, eV), band_gap_majority_u4 (number, eV), band_gap_minority_u4 (number, eV), elastic_constants_C11 (number, GPa), elastic_constants_C12 (number, GPa), elastic_constants_C44 (number, GPa), bulk_modulus_elastic (number, GPa), shear_modulus (number, GPa), B_G_ratio (number, dimensionless), poisson_ratio (number, dimensionless), cauchy_pressure (number, GPa), debye_temperature (number, K), total_magnetic_moment (number, μB/f.u.), partial_magnetic_moments (object with keys Rh, Y, O, each a number in μB), is_ductile (boolean), fm_ground_state_confirmed (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json` (scored)
- `/app/outputs/structure_input.txt`
- `/app/outputs/gga_eos_fit.log`
- `/app/outputs/gga_u_eos_fit.log`
- `/app/outputs/band_gaps.csv`
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/magnetic_moments.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated file containing all computed physical quantities from the DFT workflow. The hidden checker compares each numeric value to the paper's reported reference with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `gga_fm_equilibrium_lattice_constant`, `gga_fm_bulk_modulus`, `gga_nm_equilibrium_lattice_constant`, `gga_nm_bulk_modulus`, `gga_fm_total_energy`, `gga_nm_total_energy`, `gga_u_lattice_constants`, `gga_u_bulk_moduli`, `gga_u_total_energies`, `band_gap_majority_gga`, `band_gap_minority_gga`, `band_gap_majority_mbj`, `band_gap_minority_mbj`, `band_gap_majority_u1`, `band_gap_minority_u1`, `band_gap_majority_u2`, `band_gap_minority_u2`, `band_gap_majority_u3`, `band_gap_minority_u3`, `band_gap_majority_u4`, `band_gap_minority_u4`, `elastic_constants_C11`, `elastic_constants_C12`, `elastic_constants_C44`, `bulk_modulus_elastic`, `shear_modulus`, `B_G_ratio`, `poisson_ratio`, `cauchy_pressure`, `debye_temperature`, `total_magnetic_moment`, `partial_magnetic_moments`, `is_ductile`, `fm_ground_state_confirmed`
  - `properties`:
    - `gga_fm_equilibrium_lattice_constant`:
      - `type`: number
      - `unit`: Å
    - `gga_fm_bulk_modulus`:
      - `type`: number
      - `unit`: GPa
    - `gga_nm_equilibrium_lattice_constant`:
      - `type`: number
      - `unit`: Å
    - `gga_nm_bulk_modulus`:
      - `type`: number
      - `unit`: GPa
    - `gga_fm_total_energy`:
      - `type`: number
      - `unit`: Ry
    - `gga_nm_total_energy`:
      - `type`: number
      - `unit`: Ry
    - `gga_u_lattice_constants`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: Å
      - `maxItems`: 4
      - `minItems`: 4
    - `gga_u_bulk_moduli`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: GPa
      - `maxItems`: 4
      - `minItems`: 4
    - `gga_u_total_energies`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: Ry
      - `maxItems`: 4
      - `minItems`: 4
    - `band_gap_majority_gga`:
      - `type`: number
      - `unit`: eV
    - `band_gap_minority_gga`:
      - `type`: number
      - `unit`: eV
    - `band_gap_majority_mbj`:
      - `type`: number
      - `unit`: eV
    - `band_gap_minority_mbj`:
      - `type`: number
      - `unit`: eV
    - `band_gap_majority_u1`:
      - `type`: number
      - `unit`: eV
    - `band_gap_minority_u1`:
      - `type`: number
      - `unit`: eV
    - `band_gap_majority_u2`:
      - `type`: number
      - `unit`: eV
    - `band_gap_minority_u2`:
      - `type`: number
      - `unit`: eV
    - `band_gap_majority_u3`:
      - `type`: number
      - `unit`: eV
    - `band_gap_minority_u3`:
      - `type`: number
      - `unit`: eV
    - `band_gap_majority_u4`:
      - `type`: number
      - `unit`: eV
    - `band_gap_minority_u4`:
      - `type`: number
      - `unit`: eV
    - `elastic_constants_C11`:
      - `type`: number
      - `unit`: GPa
    - `elastic_constants_C12`:
      - `type`: number
      - `unit`: GPa
    - `elastic_constants_C44`:
      - `type`: number
      - `unit`: GPa
    - `bulk_modulus_elastic`:
      - `type`: number
      - `unit`: GPa
    - `shear_modulus`:
      - `type`: number
      - `unit`: GPa
    - `B_G_ratio`:
      - `type`: number
    - `poisson_ratio`:
      - `type`: number
    - `cauchy_pressure`:
      - `type`: number
      - `unit`: GPa
    - `debye_temperature`:
      - `type`: number
      - `unit`: K
    - `total_magnetic_moment`:
      - `type`: number
      - `unit`: μB/f.u.
    - `partial_magnetic_moments`:
      - `type`: object
      - `properties`:
        - `Rh`:
          - `type`: number
          - `unit`: μB
        - `Y`:
          - `type`: number
          - `unit`: μB
        - `O`:
          - `type`: number
          - `unit`: μB
      - `required`: `Rh`, `Y`, `O`
    - `is_ductile`:
      - `type`: boolean
      - `description`: `true` if the material is ductile (B/G > 1.75 and ν > 0.26), `false` otherwise.
    - `fm_ground_state_confirmed`:
      - `type`: boolean

Notes: The solver must run the full DFT pipeline. The checker compares the submitted properties.json to the paper's reported values (the hidden gold) with tolerances that account for typical code/pseudopotential differences. All quantities are required; missing fields score zero.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gga_fm_equilibrium_lattice_constant",
          "gga_fm_bulk_modulus",
          "gga_nm_equilibrium_lattice_constant",
          "gga_nm_bulk_modulus",
          "gga_fm_total_energy",
          "gga_nm_total_energy",
          "gga_u_lattice_constants",
          "gga_u_bulk_moduli",
          "gga_u_total_energies",
          "band_gap_majority_gga",
          "band_gap_minority_gga",
          "band_gap_majority_mbj",
          "band_gap_minority_mbj",
          "band_gap_majority_u1",
          "band_gap_minority_u1",
          "band_gap_majority_u2",
          "band_gap_minority_u2",
          "band_gap_majority_u3",
          "band_gap_minority_u3",
          "band_gap_majority_u4",
          "band_gap_minority_u4",
          "elastic_constants_C11",
          "elastic_constants_C12",
          "elastic_constants_C44",
          "bulk_modulus_elastic",
          "shear_modulus",
          "B_G_ratio",
          "poisson_ratio",
          "cauchy_pressure",
          "debye_temperature",
          "total_magnetic_moment",
          "partial_magnetic_moments",
          "is_ductile",
          "fm_ground_state_confirmed"
        ],
        "properties": {
          "gga_fm_equilibrium_lattice_constant": {
            "type": "number",
            "unit": "Å"
          },
          "gga_fm_bulk_modulus": {
            "type": "number",
            "unit": "GPa"
          },
          "gga_nm_equilibrium_lattice_constant": {
            "type": "number",
            "unit": "Å"
          },
          "gga_nm_bulk_modulus": {
            "type": "number",
            "unit": "GPa"
          },
          "gga_fm_total_energy": {
            "type": "number",
            "unit": "Ry"
          },
          "gga_nm_total_energy": {
            "type": "number",
            "unit": "Ry"
          },
          "gga_u_lattice_constants": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "Å"
            },
            "maxItems": 4,
            "minItems": 4
          },
          "gga_u_bulk_moduli": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "GPa"
            },
            "maxItems": 4,
            "minItems": 4
          },
          "gga_u_total_energies": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "Ry"
            },
            "maxItems": 4,
            "minItems": 4
          },
          "band_gap_majority_gga": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_minority_gga": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_majority_mbj": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_minority_mbj": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_majority_u1": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_minority_u1": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_majority_u2": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_minority_u2": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_majority_u3": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_minority_u3": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_majority_u4": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_minority_u4": {
            "type": "number",
            "unit": "eV"
          },
          "elastic_constants_C11": {
            "type": "number",
            "unit": "GPa"
          },
          "elastic_constants_C12": {
            "type": "number",
            "unit": "GPa"
          },
          "elastic_constants_C44": {
            "type": "number",
            "unit": "GPa"
          },
          "bulk_modulus_elastic": {
            "type": "number",
            "unit": "GPa"
          },
          "shear_modulus": {
            "type": "number",
            "unit": "GPa"
          },
          "B_G_ratio": {
            "type": "number"
          },
          "poisson_ratio": {
            "type": "number"
          },
          "cauchy_pressure": {
            "type": "number",
            "unit": "GPa"
          },
          "debye_temperature": {
            "type": "number",
            "unit": "K"
          },
          "total_magnetic_moment": {
            "type": "number",
            "unit": "μB/f.u."
          },
          "partial_magnetic_moments": {
            "type": "object",
            "properties": {
              "Rh": {
                "type": "number",
                "unit": "μB"
              },
              "Y": {
                "type": "number",
                "unit": "μB"
              },
              "O": {
                "type": "number",
                "unit": "μB"
              }
            },
            "required": [
              "Rh",
              "Y",
              "O"
            ]
          },
          "is_ductile": {
            "type": "boolean"
          },
          "fm_ground_state_confirmed": {
            "type": "boolean"
          }
        }
      },
      "description": "Aggregated file containing all computed physical quantities from the DFT workflow. The hidden checker compares each numeric value to the paper's reported reference with appropriate tolerances."
    },
    {
      "file": "structure_input.txt",
      "format": "txt",
      "purpose": "unscored"
    },
    {
      "file": "gga_eos_fit.log",
      "format": "txt",
      "purpose": "unscored"
    },
    {
      "file": "gga_u_eos_fit.log",
      "format": "txt",
      "purpose": "unscored"
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "unscored"
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "unscored"
    },
    {
      "file": "magnetic_moments.txt",
      "format": "txt",
      "purpose": "unscored"
    }
  ],
  "notes": "The solver must run the full DFT pipeline. The checker compares the submitted properties.json to the paper's reported values (the hidden gold) with tolerances that account for typical code/pseudopotential differences. All quantities are required; missing fields score zero."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/properties.json and independently compares every required field to a reference value. Each quantity is scored with an appropriate tolerance; the final reward is a weighted combination of the individual field scores. Merely quoting known values without genuinely executing the computational pipeline and producing the required intermediate evidence files (structure_input.txt, gga_eos_fit.log, gga_u_eos_fit.log, band_gaps.csv, elastic_constants.csv, magnetic_moments.txt) will not satisfy the scoring criteria—the verifier checks that every evidence file contains reasonable content (non‑empty, minimum size, CSV with at least a header and one data row). The verifier does not have access to your raw DFT data and relies solely on the structured file you submit.