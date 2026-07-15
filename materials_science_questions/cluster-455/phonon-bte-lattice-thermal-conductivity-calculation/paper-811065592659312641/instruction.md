# Multiscale NEMD-FE modeling of thermal conductivity in MoS2 heterostructures

## Problem background
Single-layer molybdenum disulfide (MoS₂) can exist in semiconducting (2H) and metallic (1T) phases, and in-plane heterostructures that stitch these phases together have been fabricated. These all-MoS₂ heterostructures offer tunable electronic properties for nanoelectronics, but their thermal transport characteristics are critical for thermal management and thermoelectric applications. Understanding how the domain size and phase concentration influence the effective in-plane thermal conductivity of such heterostructures is an open challenge. This task requires computing the intrinsic thermal conductivity of the pristine phases and the interfacial thermal resistances, and using these to predict the overall effective conductivity of macroscopic heterostructure samples.

## Approach
The computational strategy combines non-equilibrium molecular dynamics (NEMD) and continuum finite-element (FE) modeling. First, NEMD simulations with the REBO potential for MoS₂ are used to obtain the thermal conductivity of pristine 2H and 1T films and the thermal contact conductances of the α, β, and γ grain boundaries between the phases. The finite-size NEMD conductivities are extrapolated to infinite length via a 1/k vs. 1/L regression. Next, continuum FE models of heterostructures are constructed: random triangular tessellations in a square domain, with each triangle assigned a phase (2H or 1T) according to a prescribed volume fraction. The phase conductivities and interface conductances from the NEMD step are assigned. Steady-state heat conduction is solved under an applied heat flux, and the effective thermal conductivity is extracted and normalized by the pristine 2H value. This multiscale workflow is repeated for domain sizes ranging from 1 nm to 1000 nm and for secondary-phase concentrations of 5% and 20% in both 1T-in-2H and 2H-in-1T configurations.

## Reproduction target
Produce three scored artifacts:
1) pristine_conductivities.csv – the infinite-length thermal conductivity of defect-free 2H and 1T MoS₂ (in W/mK).
2) interface_conductances.csv – the thermal contact conductances of the α, β, and γ 1T/2H interfaces (in GW/m²K).
3) keff_curves.csv – the normalized effective thermal conductivity (keff divided by the pristine 2H conductivity) as a function of domain size for heterostructures with 5% and 20% secondary phase in both compositional directions (e.g., 1T triangles in a 2H matrix and 2H triangles in a 1T matrix).

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- REBO potential for MoS₂ (Liang et al. 2009): 10.1103/PhysRevB.79.245110
- FEniCS finite-element solver: https://fenicsproject.org/

## Workflow steps

### Step 1: Generate atomistic models
- Role: process
- Action: Create LAMMPS input data files for pristine 2H and 1T MoS₂ films with lengths in the range 10–80 nm, and for the three 1T/2H grain boundary interface geometries (α, β, γ) at a fixed length (e.g., 20 nm). Use known crystal structure parameters and interface atomic configurations from the literature.
- Evidence: `/app/outputs/model_files_generated.txt`

### Step 2: Run NEMD simulations for pristine films
- Role: process
- Action: Perform non-equilibrium molecular dynamics (NEMD) simulations in LAMMPS with the REBO potential for each pristine film length and phase (2H and 1T). Apply a temperature gradient, record slab temperatures and energy addition/removal, and compute the heat flux and finite-length thermal conductivity k(L).
- Evidence: `/app/outputs/nemd_pristine.log`

### Step 3: Extrapolate infinite-length pristine conductivity
- Role: scored
- Action: From the NEMD finite-length results, extrapolate the thermal conductivity to infinite length via linear regression of 1/k vs 1/L. Output the infinite-length thermal conductivity for both 2H and 1T phases.
- Output file: `/app/outputs/pristine_conductivities.csv`
- Format: csv
- Contract: phase: string (2H or 1T), k_inf: float (W/mK)
- Scoring: scored by hidden verifier

### Step 4: Run NEMD simulations for grain boundary interfaces
- Role: process
- Action: Perform NEMD simulations on the α, β, and γ 1T/2H interface models to obtain steady-state temperature profiles. Measure the temperature jump ΔT across each interface and compute the applied heat flux.
- Evidence: `/app/outputs/nemd_interface.log`

### Step 5: Compute interface thermal conductances
- Role: scored
- Action: From the NEMD interface results, compute the thermal contact conductances C_i = q_x / ΔT for the α, β, and γ grain boundaries and output the values.
- Output file: `/app/outputs/interface_conductances.csv`
- Format: csv
- Contract: interface: string (alpha, beta, gamma), C: float (GW/m²K)
- Scoring: scored by hidden verifier

### Step 6: Compute FE effective thermal conductivity of heterostructures
- Role: scored (load-bearing)
- Action: Construct continuum finite-element models of MoS₂ heterostructures using random triangular tessellation in a square domain. Assign thermal conductivities from step 3 and interface conductances from step 5. Apply heat flux boundary conditions and solve the steady-state heat equation for a range of domain sizes (1–1000 nm) and phase concentrations of 5% and 20% secondary phase (both 1T in 2H and 2H in 1T). Compute the effective thermal conductivity keff and normalize by the 2H pristine conductivity. Output the normalized values as a function of domain size for each composition.
- Output file: `/app/outputs/keff_curves.csv`
- Format: csv
- Contract: domain_size_nm: float, composition: string (e.g., '20_1T_in_2H'), keff_norm: float (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_conductivities.csv`
- `/app/outputs/interface_conductances.csv`
- `/app/outputs/keff_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_conductivities.csv
- path: `/app/outputs/pristine_conductivities.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Infinite-length thermal conductivity of pristine 2H and 1T MoS₂. Two rows: phase=2H and phase=1T.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `k_inf`
  - `units`:
    - `k_inf`: W/mK

### interface_conductances.csv
- path: `/app/outputs/interface_conductances.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermal contact conductances of the three 1T/2H grain boundaries. One row each for interface=alpha, beta, gamma.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `C`
  - `units`:
    - `C`: GW/m²K

### keff_curves.csv
- path: `/app/outputs/keff_curves.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized effective thermal conductivity (keff/k₂H) as a function of domain size for several heterostructure compositions. Composition values like '5_1T_in_2H', '20_1T_in_2H', '5_2H_in_1T', '20_2H_in_1T'.
- schema:
  - `type`: table
  - `required_columns`: `domain_size_nm`, `composition`, `keff_norm`
  - `units`:
    - `keff_norm`: dimensionless

Notes: The paper's phonon density of states analysis is omitted as it is not essential for the main computational claims. Only the NEMD-derived properties and FE effective conductivity curves are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_conductivities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "k_inf"
        ],
        "units": {
          "k_inf": "W/mK"
        }
      },
      "description": "Infinite-length thermal conductivity of pristine 2H and 1T MoS₂. Two rows: phase=2H and phase=1T."
    },
    {
      "file": "interface_conductances.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "C"
        ],
        "units": {
          "C": "GW/m²K"
        }
      },
      "description": "Thermal contact conductances of the three 1T/2H grain boundaries. One row each for interface=alpha, beta, gamma."
    },
    {
      "file": "keff_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "domain_size_nm",
          "composition",
          "keff_norm"
        ],
        "units": {
          "keff_norm": "dimensionless"
        }
      },
      "description": "Normalized effective thermal conductivity (keff/k₂H) as a function of domain size for several heterostructure compositions. Composition values like '5_1T_in_2H', '20_1T_in_2H', '5_2H_in_1T', '20_2H_in_1T'."
    }
  ],
  "notes": "The paper's phonon density of states analysis is omitted as it is not essential for the main computational claims. Only the NEMD-derived properties and FE effective conductivity curves are scored."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three output artifacts by comparing your computed values against the expected reference results derived from the original study. The verifier assigns a numerical score for each artifact and combines them using predefined weights to compute the final reward. Merely reporting known numbers without executing the workflow will not earn a high score; the verifier expects results that match the physics of the described multiscale model within the natural uncertainties of re‑implementation.
