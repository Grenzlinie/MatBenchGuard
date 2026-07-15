# Retrieval of effective permittivity and ENZ wavelength in Ag-Ge multilayer metamaterials

## Problem background
Near-infrared epsilon-near-zero (ENZ) metamaterials based on silver-germanium (Ag-Ge) multilayers exhibit unique electromagnetic properties, such as near-zero permittivity enabling anomalous wave manipulation. Determining the effective complex refractive index, effective transverse permittivity, and the ENZ wavelength at which the real part of permittivity vanishes is essential for verifying the metamaterial response and for applications like phase front shaping and spontaneous emission control. The task is to compute these quantities for a specific Ag-Ge multilayer slab using two independent computational routes.

## Approach
The computational approach consists of two independent pipelines. First, a rigorous electromagnetic simulation of the multilayer slab yields transmission and reflection spectra. The amplitude‑only inversion formulas (which require only the simulated T and R and the known slab thickness) are then applied to retrieve the complex refractive index (n, k) without needing phase information. From n and k, the effective transverse permittivity is obtained. Second, an analytical nonlocal dispersion model, derived from the transfer‑matrix method, provides an effective permittivity directly from the individual layer properties (Ag Drude model and Ge optical constants). The ENZ wavelength is identified where the real part of the effective permittivity vanishes, and the condition n = k at that point is verified. Both pipelines are evaluated over the same wavelength range and should yield consistent results.

## Reproduction target
Compute for a 5‑pair Ag‑Ge multilayer slab (15 nm Ag, 85 nm Ge, with 42.5 nm Ge half‑layers top and bottom) the following:

1. The complex refractive index (n, k) and effective transverse permittivity from amplitude‑only inversion of simulated transmission and reflection spectra.
2. The ENZ wavelength where the real part of the effective permittivity crosses zero, and verify the n = k condition at that wavelength.
3. The effective permittivity computed from the nonlocal analytical dispersion model.

All calculations are performed over the near‑infrared wavelength range 1.4 μm to 1.9 μm using publicly available material constants and an open‑source electromagnetic solver.

## Assets

- Silver Drude model parameters
- Germanium optical constants: https://refractiveindex.info
- Open-source electromagnetic solver: https://github.com/victorliu/S4

## Workflow steps

### Step 1: Simulate multilayer transmission and reflection spectra
- Role: scored
- Action: Construct the Ag-Ge multilayer slab: 5 periods of 15 nm Ag / 85 nm Ge, with 42.5 nm Ge capping layers on top and bottom. Use an open-source EM solver (e.g., transfer-matrix method, RCWA, or FDTD) to compute the normal-incidence TM-polarized transmission T and reflection R as power fractions for wavelengths from 1.4 μm to 1.9 μm, with a sufficiently fine wavelength step. Output the spectra.
- Output file: `/app/outputs/step_01_simulated_spectra.csv`
- Format: csv
- Contract: Columns: wavelength_micron (float), transmission (float, 0–1), reflection (float, 0–1).
- Scoring: scored by hidden verifier

### Step 2: Retrieve complex refractive index from T and R
- Role: scored
- Action: Using the simulated T(λ) and R(λ) and the known total slab thickness t = 5*(15+85)+2*42.5 nm = 585 nm, compute the extinction coefficient k(λ) = -(λ/(4π t)) * ln( X ) where X = [ (T^2 - (1-R)^2) + sqrt( (T^2 - (1-R)^2)^2 + 4 T^2 ) ] / (2 T). Then compute the surface reflectance Ras = R / (1 + X). Then compute the refractive index n via the formula n = (1+Ras)/(1-Ras) ± sqrt( 4 Ras/(1-Ras)^2 - k^2 ), selecting the plus branch when n ≥ 1 and the minus branch when n < 1. Output n(λ) and k(λ).
- Output file: `/app/outputs/step_02_retrieved_nk.csv`
- Format: csv
- Contract: Columns: wavelength_micron (float), n (float), k (float).
- Scoring: scored by hidden verifier

### Step 3: Compute effective permittivity from n, k
- Role: scored
- Action: Calculate the effective transverse permittivity as ε_y^eff = (n + i k)^2, giving real and imaginary parts.
- Output file: `/app/outputs/step_03_retrieved_epsilon.csv`
- Format: csv
- Contract: Columns: wavelength_micron (float), real_epsilon (float), imag_epsilon (float).
- Scoring: scored by hidden verifier

### Step 4: Determine ENZ wavelength and n=k condition (amplitude-only route)
- Role: scored (load-bearing)
- Action: From the retrieved ε_y^eff(λ), locate the wavelength where the real part of ε_y^eff crosses zero; report that wavelength. At that ENZ wavelength, check whether the absolute difference |n – k| is ≤ 0.02; report a boolean. Output the result.
- Output file: `/app/outputs/step_04_enz_result.json`
- Format: json
- Contract: {"enz_wavelength_micron": float, "n_equals_k_at_enz": boolean}
- Scoring: scored by hidden verifier

### Step 5: Compute effective permittivity via nonlocal dispersion (Method 3)
- Role: scored
- Action: Using the Ag Drude parameters (ε∞=5.0, ωp=1.38×10^16 rad/s, γp=6.4×5.07×10^13 rad/s) and the Ge optical constants, evaluate the nonlocal dispersion relation for the effective transverse permittivity: ε_y^eff = (arc cos^2[ cos(√ε1 k0 d1) cos(√ε2 k0 d2) - 0.5 (√(ε1/ε2)+√(ε2/ε1)) sin(√ε1 k0 d1) sin(√ε2 k0 d2) ]) / [k0^2 (d1+d2)^2], where k0 = 2π/λ, ε1, ε2 are the complex permittivities of Ag and Ge, d1=15 nm, d2=85 nm. Treat the arc cos branch to yield a continuous function matching the paper's convention. Output the real and imaginary parts of ε_y^eff(λ) over the same wavelength range.
- Output file: `/app/outputs/nonlocal_epsilon.csv`
- Format: csv
- Contract: Columns: wavelength_micron (float), real_epsilon (float), imag_epsilon (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_simulated_spectra.csv`
- `/app/outputs/step_02_retrieved_nk.csv`
- `/app/outputs/step_03_retrieved_epsilon.csv`
- `/app/outputs/step_04_enz_result.json`
- `/app/outputs/nonlocal_epsilon.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_simulated_spectra.csv
- path: `/app/outputs/step_01_simulated_spectra.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated TM-polarized normal-incidence transmission and reflection spectra of the multilayer slab. Checked for physical plausibility (values in [0,1], T+R ≤ 1).
- schema:
  - `type`: table
  - `required_columns`: `wavelength_micron`, `transmission`, `reflection`
  - `units`:
    - `wavelength_micron`: micrometer
    - `transmission`: fraction (0-1)
    - `reflection`: fraction (0-1)

### step_02_retrieved_nk.csv
- path: `/app/outputs/step_02_retrieved_nk.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Retrieved real and imaginary parts of the complex refractive index from amplitude-only inversion. Verified by recomputing from the submitted T,R spectra.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_micron`, `n`, `k`
  - `units`:
    - `wavelength_micron`: micrometer
    - `n`: dimensionless
    - `k`: dimensionless

### step_03_retrieved_epsilon.csv
- path: `/app/outputs/step_03_retrieved_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Effective permittivity derived from the inverted n,k. Verified by recomputing from submitted n,k.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_micron`, `real_epsilon`, `imag_epsilon`
  - `units`:
    - `wavelength_micron`: micrometer
    - `real_epsilon`: dimensionless
    - `imag_epsilon`: dimensionless

### step_04_enz_result.json
- path: `/app/outputs/step_04_enz_result.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: ENZ wavelength and n=k condition from the amplitude-only pipeline. Compared against hidden paper reference (wavelength tolerance ±0.003 μm; boolean expected true).
- schema:
  - `type`: object
  - `required`:
    - `enz_wavelength_micron`: float
    - `n_equals_k_at_enz`: boolean

### nonlocal_epsilon.csv
- path: `/app/outputs/nonlocal_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Effective permittivity computed from the nonlocal dispersion relation. Verified by independent recomputation using the same material parameters.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_micron`, `real_epsilon`, `imag_epsilon`
  - `units`:
    - `wavelength_micron`: micrometer
    - `real_epsilon`: dimensionless
    - `imag_epsilon`: dimensionless

Notes: The amplitude-only inversion uses the formulas from the paper (based on incoherent interference, requiring only T and R). The nonlocal dispersion is the analytical formula from the multilayer transfer-matrix method. Both pipelines independently yield an ENZ wavelength and must be consistent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_simulated_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_micron",
          "transmission",
          "reflection"
        ],
        "units": {
          "wavelength_micron": "micrometer",
          "transmission": "fraction (0-1)",
          "reflection": "fraction (0-1)"
        }
      },
      "description": "Simulated TM-polarized normal-incidence transmission and reflection spectra of the multilayer slab. Checked for physical plausibility (values in [0,1], T+R ≤ 1)."
    },
    {
      "file": "step_02_retrieved_nk.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_micron",
          "n",
          "k"
        ],
        "units": {
          "wavelength_micron": "micrometer",
          "n": "dimensionless",
          "k": "dimensionless"
        }
      },
      "description": "Retrieved real and imaginary parts of the complex refractive index from amplitude-only inversion. Verified by recomputing from the submitted T,R spectra."
    },
    {
      "file": "step_03_retrieved_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_micron",
          "real_epsilon",
          "imag_epsilon"
        ],
        "units": {
          "wavelength_micron": "micrometer",
          "real_epsilon": "dimensionless",
          "imag_epsilon": "dimensionless"
        }
      },
      "description": "Effective permittivity derived from the inverted n,k. Verified by recomputing from submitted n,k."
    },
    {
      "file": "step_04_enz_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "enz_wavelength_micron": "float",
          "n_equals_k_at_enz": "boolean"
        }
      },
      "description": "ENZ wavelength and n=k condition from the amplitude-only pipeline. Compared against hidden paper reference (wavelength tolerance ±0.003 μm; boolean expected true)."
    },
    {
      "file": "nonlocal_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_micron",
          "real_epsilon",
          "imag_epsilon"
        ],
        "units": {
          "wavelength_micron": "micrometer",
          "real_epsilon": "dimensionless",
          "imag_epsilon": "dimensionless"
        }
      },
      "description": "Effective permittivity computed from the nonlocal dispersion relation. Verified by independent recomputation using the same material parameters."
    }
  ],
  "notes": "The amplitude-only inversion uses the formulas from the paper (based on incoherent interference, requiring only T and R). The nonlocal dispersion is the analytical formula from the multilayer transfer-matrix method. Both pipelines independently yield an ENZ wavelength and must be consistent."
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact and combines them by weight into the final reward.

- **Simulated spectra (step 1):** Physical plausibility is checked.
- **Retrieved n,k (step 2):** The verifier recomputes the amplitude‑only inversion from your submitted spectra and compares.
- **Retrieved permittivity (step 3):** Re‑computed from your n,k and compared.
- **ENZ result (step 4):** Compared against a hidden reference.
- **Nonlocal permittivity (step 5):** The verifier recomputes the nonlocal dispersion formula independently and compares.

Reporting a number is not enough; the artifacts must be consistent with the underlying physics and pipeline. Only the hidden verifier knows the exact tolerances and reference values.
