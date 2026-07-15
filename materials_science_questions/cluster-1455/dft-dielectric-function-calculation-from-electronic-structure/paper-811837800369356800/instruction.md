## Problem background

Cubic spinel double nitrides, particularly c‑SiGe₂N₄, are candidate materials for optoelectronic applications because of their predicted wide direct band gaps, large bulk moduli, and interesting dielectric properties. First‑principles density functional theory (DFT) studies provide reliable predictions of these properties, which are essential for assessing technological potential when experimental data are scarce.

This task requires computing a consistent set of ground‑state physical properties of the cubic spinel compound SiGe₂N₄ at zero external pressure (and room temperature, 300 K, for thermal properties) using plane‑wave pseudopotential DFT within the generalized gradient approximation (GGA). The computed quantities serve as a benchmark for theoretical predictions and future experiments.

## Approach

Use a plane‑wave pseudopotential total‑energy method with an open‑source DFT code (e.g., Quantum ESPRESSO). Employ Vanderbilt‑type ultrasoft pseudopotentials for Si, Ge and N, and treat exchange‑correlation with the GGA functional of Perdew, Burke and Ernzerhof.

First, perform a full geometry optimization of the cubic spinel structure (space group Fd‑3m, origin at ‑3m) to determine the equilibrium lattice constant a₀ and the internal anion parameter u. From this equilibrium geometry, generate an energy‑volume (E–V) dataset by carrying out fixed‑pressure structural relaxations at a set of hydrostatic pressures up to 40 GPa; fit the (V,E) points to the third‑order Birch–Murnaghan equation of state to extract the zero‑pressure bulk modulus B₀ and its pressure derivative B′.

Using the relaxed equilibrium structure, compute the three independent elastic stiffness coefficients C₁₁, C₁₂, C₄₄ by applying finite strain patterns, calculating the resulting stresses, and fitting the stress–strain relations.

For the electronic properties, calculate the band structure along high‑symmetry lines of the Brillouin zone, identify the direct band gap at the Γ point, and record that value.

For optical properties, compute the momentum matrix elements from the equilibrium wavefunctions on a dense k‑point mesh, evaluate the complex dielectric function, and extract the static (ω→0) dielectric constant ε(0) and refractive index n(0).

Finally, use the quasi‑harmonic Debye model (e.g., the Gibbs program) on the previously obtained E–V data to predict thermal properties at T = 300 K and zero pressure: the bulk modulus, the heat capacity at constant volume Cᵥ, and the Debye temperature θD.

All computations are purely dry and require only publicly available codes and pseudopotentials.

## Reproduction target

Compute and write to disk the following five JSON artifacts, each containing well‑defined scalar properties obtained from the DFT workflow described above:

- `structural_properties.json` – equilibrium lattice constant a₀ (Å), internal anion parameter u, bulk modulus B₀ (GPa) from EOS fit, and its pressure derivative B′.
- `elastic_constants.json` – the three independent elastic constants C₁₁, C₁₂, C₄₄ (GPa) for the cubic phase.
- `electronic_properties.json` – the direct band gap at Γ (eV).
- `optical_properties.json` – static dielectric constant ε(0) and static refractive index n(0).
- `thermal_properties_300K.json` – bulk modulus (GPa), heat capacity Cᵥ (J mol⁻¹ K⁻¹), and Debye temperature (K) evaluated at T = 300 K and zero pressure.

All properties must be obtained at the equilibrium structure at zero pressure (except the thermal properties, which additionally require the E–V dataset).

## Assets

- **Quantum ESPRESSO** – open‑source plane‑wave pseudopotential DFT code.
  URL: https://www.quantum-espresso.org/
- **Ultrasoft pseudopotentials for Si, Ge, N** – taken from the Standard Solid‑State Pseudopotentials (SSSP) efficiency library or equivalent.
  URL: https://www.materialscloud.org/discover/sssp/table/efficiency
- **Gibbs program** – quasi‑harmonic Debye model (Blanco et al., Comput. Phys. Commun. 158, 57 (2004)) used for thermal properties. An equivalent implementation is acceptable.
  URL: (no single direct link; the program is publicly available and can be obtained from the authors’ site or equivalent repositories).

No other assets are required. The paper’s crystal structure information and computational protocol are described in the Approach section.

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform a plane‑wave pseudopotential DFT geometry optimization of cubic spinel SiGe₂N₄ using GGA and ultrasoft pseudopotentials to find the equilibrium lattice constant a₀ and the internal anion parameter u.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: Energy–volume data generation
- Role: process
- Action: Carry out a series of fixed‑pressure (or fixed‑volume) structural relaxations for the same system at several hydrostatic pressures (e.g., 0, 10, 20, 30, 40 GPa) to obtain a set of (volume, total energy) data points. Use the same DFT settings as in Step 1.
- Evidence: `/app/outputs/ev_data.csv`

### Step 3: Assemble structural properties (load‑bearing)
- Role: scored (load‑bearing)
- Action: From the geometry optimization, extract a₀ and u. Fit the E–V data to the third‑order Birch–Murnaghan equation of state to obtain the zero‑pressure bulk modulus B₀ and its pressure derivative B′. Write the results to `/app/outputs/structural_properties.json`.
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: A JSON object with keys `a0` (float, Å), `u` (float, dimensionless), `B0_EOS` (float, GPa), `Bprime_EOS` (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Compute elastic constants
- Role: scored
- Action: Using the equilibrium geometry from Step 1, apply finite strain patterns, compute the resulting stresses, and extract the three independent elastic stiffness coefficients C₁₁, C₁₂, C₄₄. Write to `/app/outputs/elastic_constants.json`.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: A JSON object with keys `C11` (float, GPa), `C12` (float, GPa), `C44` (float, GPa).
- Scoring: scored by hidden verifier

### Step 5: Compute direct band gap
- Role: scored
- Action: Calculate the electronic band structure along high‑symmetry paths. Identify the direct optical band gap at the Γ point (Γ→Γ transition) and write the value to `/app/outputs/electronic_properties.json`.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: A JSON object with key `direct_band_gap_Gamma_Gamma` (float, eV).
- Scoring: scored by hidden verifier

### Step 6: Compute static optical constants
- Role: scored
- Action: From the equilibrium wavefunctions, compute the momentum matrix elements, evaluate the dielectric function on a dense k‑mesh, perform Kramers‑Kronig transformation if needed, and extract the static dielectric constant ε(0) and refractive index n(0). Write to `/app/outputs/optical_properties.json`.
- Output file: `/app/outputs/optical_properties.json`
- Format: json
- Contract: A JSON object with keys `static_dielectric_constant_epsilon0` (float, dimensionless) and `static_refractive_index_n0` (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 7: Thermal properties at 300 K
- Role: scored
- Action: Using the E–V data from Step 2 and the quasi‑harmonic Debye model (e.g., Gibbs program), compute the bulk modulus, heat capacity at constant volume Cᵥ, and Debye temperature at T = 300 K and zero pressure. Write to `/app/outputs/thermal_properties_300K.json`.
- Output file: `/app/outputs/thermal_properties_300K.json`
- Format: json
- Contract: A JSON object with keys `bulk_modulus_300K` (float, GPa), `heat_capacity_300K` (float, J mol⁻¹ K⁻¹), `debye_temperature_300K` (float, K).
- Scoring: scored by hidden verifier

## Output files

The agent must create the following files under `/app/outputs`:
- `geom_opt.log` (evidence from Step 1)
- `ev_data.csv` (evidence from Step 2)
- `structural_properties.json` (scored)
- `elastic_constants.json` (scored)
- `electronic_properties.json` (scored)
- `optical_properties.json` (scored)
- `thermal_properties_300K.json` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Ground‑state lattice constant a₀, internal anion parameter u, bulk modulus B₀ from Birch‑Murnaghan EOS fit, and pressure derivative B′.
- schema:
  - `type`: object
  - `required`:
    - `a0`: float (Å)
    - `u`: float (dimensionless)
    - `B0_EOS`: float (GPa)
    - `Bprime_EOS`: float (dimensionless)
  - `units`:
    - `a0`: Å
    - `B0_EOS`: GPa

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Independent elastic stiffness coefficients for the cubic phase.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C44`: float (GPa)
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Direct electronic band gap at the Brillouin zone centre (Γ point).
- schema:
  - `type`: object
  - `required`:
    - `direct_band_gap_Gamma_Gamma`: float (eV)
  - `units`:
    - `direct_band_gap_Gamma_Gamma`: eV

### optical_properties.json
- path: `/app/outputs/optical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static (ω→0) dielectric constant and refractive index.
- schema:
  - `type`: object
  - `required`:
    - `static_dielectric_constant_epsilon0`: float (dimensionless)
    - `static_refractive_index_n0`: float (dimensionless)
  - `units`: object

### thermal_properties_300K.json
- path: `/app/outputs/thermal_properties_300K.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk modulus, heat capacity at constant volume, and Debye temperature evaluated at 300 K and zero pressure from the quasi‑harmonic Debye model.
- schema:
  - `type`: object
  - `required`:
    - `bulk_modulus_300K`: float (GPa)
    - `heat_capacity_300K`: float (J mol⁻¹ K⁻¹)
    - `debye_temperature_300K`: float (K)
  - `units`:
    - `bulk_modulus_300K`: GPa
    - `heat_capacity_300K`: J mol⁻¹ K⁻¹
    - `debye_temperature_300K`: K

Notes: All properties correspond to the equilibrium cubic spinel structure of SiGe₂N₄ at zero pressure (and 300 K for the thermal entry). The verifier compares each scalar within a tolerance that accounts for legitimate differences between DFT implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a0": "float (Å)",
          "u": "float (dimensionless)",
          "B0_EOS": "float (GPa)",
          "Bprime_EOS": "float (dimensionless)"
        },
        "units": {
          "a0": "Å",
          "B0_EOS": "GPa"
        }
      },
      "description": "Ground‑state lattice constant a₀, internal anion parameter u, bulk modulus B₀ from Birch‑Murnaghan EOS fit, and pressure derivative B′."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C44": "float (GPa)"
        },
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Independent elastic stiffness coefficients for the cubic phase."
    },
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "direct_band_gap_Gamma_Gamma": "float (eV)"
        },
        "units": {
          "direct_band_gap_Gamma_Gamma": "eV"
        }
      },
      "description": "Direct electronic band gap at the Brillouin zone centre (Γ point)."
    },
    {
      "file": "optical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "static_dielectric_constant_epsilon0": "float (dimensionless)",
          "static_refractive_index_n0": "float (dimensionless)"
        },
        "units": {}
      },
      "description": "Static (ω→0) dielectric constant and refractive index."
    },
    {
      "file": "thermal_properties_300K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_modulus_300K": "float (GPa)",
          "heat_capacity_300K": "float (J mol⁻¹ K⁻¹)",
          "debye_temperature_300K": "float (K)"
        },
        "units": {
          "bulk_modulus_300K": "GPa",
          "heat_capacity_300K": "J mol⁻¹ K⁻¹",
          "debye_temperature_300K": "K"
        }
      },
      "description": "Bulk modulus, heat capacity at constant volume, and Debye temperature evaluated at 300 K and zero pressure from the quasi‑harmonic Debye model."
    }
  ],
  "notes": "All properties correspond to the equilibrium cubic spinel structure of SiGe₂N₄ at zero pressure (and 300 K for the thermal entry). The verifier compares each scalar within a tolerance that accounts for legitimate differences between DFT implementations."
}
```

## How you are scored

A hidden verifier reads the five scored JSON files from `/app/outputs` and compares each scalar quantity to reference values derived independently from the published work. The final reward is the weighted average of the step‑wise scores. Submitting the published numbers without performing the DFT workflow is not sufficient; the computed values must originate from a genuine computational reproduction.
