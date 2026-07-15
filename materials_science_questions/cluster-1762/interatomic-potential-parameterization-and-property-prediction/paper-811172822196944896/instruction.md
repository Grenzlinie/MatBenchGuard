# Computation of Cs atom dispersion coefficients and retardation functions for various surfaces

## Problem background
Accurate knowledge of atom–surface van der Waals interactions is critical for applications such as atom chips, Bose-Einstein condensates, and precision spectroscopy. The interaction strength is quantified by dispersion coefficients (C3), which depend on the dynamic electric-dipole polarizability of the atom and the frequency-dependent dielectric function of the surface material. For ground-state cesium (Cs), earlier theoretical predictions often relied on approximate polarizabilities or simplified dielectric models, limiting their accuracy. This task computes high-accuracy dynamic polarizabilities of Cs using relativistic coupled-cluster theory, augmented with experimental transition data, and combines them with optical constants to derive C3 coefficients and retardation functions for several technologically important surfaces: perfect conductor, Au, Si, SiO2, SiNx, ordinary sapphire, extraordinary sapphire, birefringent sapphire, and YAG.

## Approach
The dynamic electric-dipole polarizability α(iω) of the Cs ground state at imaginary frequencies is computed within relativistic coupled-cluster theory (CCSD(T) in a Fock-space formalism). The valence contribution is evaluated using a sum-over-states expression, with E1 matrix elements for the dominant 6s–6p transitions replaced by precise experimental values to reduce uncertainty. The core contribution is obtained via relativistic random-phase approximation (RRPA), core-valence correlation is estimated separately, and the tail (high-lying excited states and continuum) is approximated using Dirac-Fock orbitals. The static limit yields the total scalar polarizability and its decomposition. 

For each surface material, the frequency-dependent dielectric function ε(iω) along the imaginary axis is derived from optical data (real and imaginary refractive indices compiled in the Palik handbook). For Au, Im[ε(ω)] is constructed from n and κ, followed by a Kramers-Kronig transform to obtain ε(iω); below 0.1 eV the Drude model (ωp = 9.0 eV, γ = 0.035 eV) is used to extrapolate. For Si, SiO2, sapphire variants, and YAG, ε(iω) is obtained directly from Palik data via Kramers-Kronig. For SiNx, the Tauc-Lorentz model is employed. The material response function S(iω) = (ε(iω)-1)/(ε(iω)+1) is then formed. 

Using the dynamic polarizability and S(iω), the C3 coefficient is computed for each material by numerical integration of the Lifshitz expression. For the perfect conductor, S is taken as 1. Each C3 integral is decomposed into core, valence, core-valence, and tail components. 

Finally, the full interaction potential V(z) is evaluated, and the retardation function f3(z) = -V(z) z³ / C3 is computed over a grid of separation distances z. The function is fitted to the rational form: f3(z) = (1 + A₁ α_fs z + A₂ (α_fs z)²) / (1 + A₁ α_fs z + B₂ (α_fs z)² + B₃ (α_fs z)³), yielding the four dimensionless parameters for each surface.

## Reproduction target
Produce three scored output files: 
1. Static scalar polarizability of ground-state Cs in atomic units, broken down into valence, core, core-valence, and tail contributions, along with an estimated total uncertainty. 
2. C3 dispersion coefficients (in atomic units) for Cs interacting with each of the following surfaces: perfect conductor, Au, Si, SiO2, SiNx, ordinary sapphire, extraordinary sapphire, birefringent sapphire, and YAG. Each coefficient must be split into core, valence, core-valence, tail, and total components. 
3. The four fitting parameters (A₁, A₂, B₂, B₃) for the rational-function representation of the retardation function f3(z) for each surface (Au, Si, SiO2, SiNx, ordinary sapphire, extraordinary sapphire, birefringent sapphire, YAG). Parameters are dimensionless. 

All values must be derived by re-running the full computational pipeline (relativistic coupled-cluster, Kramers-Kronig, lifshitz integration, and fitting); simply quoting known numbers is insufficient.

## Assets

- DIRAC relativistic quantum chemistry program (or equivalent open-source relativistic CC package): https://www.diracprogram.org
- Cs experimental E1 amplitudes and energies for 6s-6p transitions (Rafac et al., 1999): 10.1103/PhysRevA.60.3648
- Optical constants (n, k) from E.D. Palik, Handbook of Optical Constants of Solids: 10.1016/C2009-0-20913-4
- Python packages for numerical integration and fitting (scipy, numpy): scipy numpy

## Workflow steps

### Step 1: Compute Cs dynamic polarizability and static decomposition
- Role: scored
- Action: Compute the dynamic electric-dipole polarizability α(iω) of the ground-state Cs atom at imaginary frequencies using a relativistic coupled-cluster approach (CCSD(T) within Fock-space RCC). Employ a sum-over-states expression for the valence contribution, with experimental E1 amplitudes and energies for the 6s–6p transitions replacing calculated values. Compute core contribution via relativistic random-phase approximation (RRPA), estimate core-valence, and estimate tail contributions from Dirac-Fock orbitals. Decompose the static limit α(0) into core, valence, core-valence, and tail components. Report the total static polarizability and its decomposition in atomic units.
- Output file: `/app/outputs/step_01_static_polarizability.json`
- Format: json
- Contract: Keys: alpha_total (float), alpha_valence (float), alpha_core (float), alpha_core_valence (float), alpha_tail (float), uncertainty_total (float). All values in atomic units.
- Scoring: scored by hidden verifier

### Step 2: Prepare material dielectric functions ε(iω)
- Role: process
- Action: For each surface material (Au, Si, SiO₂, SiNₓ, ordinary sapphire, extraordinary sapphire, birefringent sapphire, YAG), obtain the frequency-dependent dielectric constant ε(iω) along the imaginary axis. Use optical data from the Palik handbook: for Au, compute Im[ε(ω)] = 2nκ, apply Kramers-Kronig to obtain ε(iω), and extrapolate below 0.1 eV with the Drude model (ωp = 9.0 eV, γ = 0.035 eV). For Si, SiO₂, sapphire, YAG, use Palik n,κ data over the available energy range and derive ε(iω) via Kramers-Kronig. For SiNₓ, employ the Tauc-Lorentz model. Save the dielectric functions for all materials for subsequent integration steps.
- Evidence: `/app/outputs/dielectric_functions.npz`

### Step 3: Compute C3 dispersion coefficients
- Role: scored (load-bearing)
- Action: Using the dynamic polarizability α(iω) from step 'compute_polarizability' and the material dielectric functions ε(iω) from step 'prepare_dielectric', numerically integrate the Lifshitz expression to obtain the C3 coefficient for each medium. For the perfect conductor, set S = 1. Decompose each integral into core, valence, core-valence, and tail contributions. Output a CSV table with one row per material (perfect_conductor, Au, Si, SiO2, SiNx, ordinary_sapphire, extraordinary_sapphire, birefringent_sapphire, YAG) and columns for each component and total, all in atomic units.
- Output file: `/app/outputs/step_02_C3_coefficients.csv`
- Format: csv
- Contract: Columns: material (string, one of: perfect_conductor, Au, Si, SiO2, SiNx, ordinary_sapphire, extraordinary_sapphire, birefringent_sapphire, YAG), C3_core (float), C3_valence (float), C3_core_valence (float), C3_tail (float), C3_total (float). All C3 values in atomic units.
- Scoring: scored by hidden verifier

### Step 4: Compute retardation functions and obtain fitting parameters
- Role: scored
- Action: For each surface (Au, Si, SiO₂, SiNₓ, ordinary_sapphire, extraordinary_sapphire, birefringent_sapphire, YAG), evaluate the full interaction potential V(z) from the atom-surface formula using the dynamic polarizability and dielectric functions. Derive the retardation function f₃(z) = -V(z) z³ / C₃ over a dense grid of separation distances z. Fit the computed f₃(z) to the rational functional form f₃(z) = (1 + A₁ α_fs z + A₂ (α_fs z)²) / (1 + A₁ α_fs z + B₂ (α_fs z)² + B₃ (α_fs z)³). Output a CSV with the best-fit parameters A₁, A₂, B₂, B₃ for each surface.
- Output file: `/app/outputs/step_03_f3_fitting_parameters.csv`
- Format: csv
- Contract: Columns: surface (string), A1 (float), A2 (float), B2 (float), B3 (float). Parameters are dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_static_polarizability.json`
- `/app/outputs/step_02_C3_coefficients.csv`
- `/app/outputs/step_03_f3_fitting_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_static_polarizability.json
- path: `/app/outputs/step_01_static_polarizability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static scalar polarizability of ground-state Cs and its decomposition into core, valence, core-valence, and tail contributions.
- schema:
  - `type`: object
  - `required`:
    - `alpha_total`: float (a.u.)
    - `alpha_valence`: float (a.u.)
    - `alpha_core`: float (a.u.)
    - `alpha_core_valence`: float (a.u.)
    - `alpha_tail`: float (a.u.)
    - `uncertainty_total`: float (a.u.)

### step_02_C3_coefficients.csv
- path: `/app/outputs/step_02_C3_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: C3 dispersion coefficients for the interaction of ground-state Cs with a perfect conductor, Au, Si, SiO2, SiNx, ordinary sapphire, extraordinary sapphire, birefringent sapphire, and YAG, with contribution breakdown.
- schema:
  - `type`: table
  - `required_columns`: `material`, `C3_core`, `C3_valence`, `C3_core_valence`, `C3_tail`, `C3_total`
  - `units`:
    - `C3_core`: a.u.
    - `C3_valence`: a.u.
    - `C3_core_valence`: a.u.
    - `C3_tail`: a.u.
    - `C3_total`: a.u.

### step_03_f3_fitting_parameters.csv
- path: `/app/outputs/step_03_f3_fitting_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fitting parameters (A1, A2, B2, B3) for the rational-function representation of the retardation function f3(z) for each surface.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `A1`, `A2`, `B2`, `B3`

Notes: All numerical values are compared to hidden gold from the source paper with tolerances that absorb legitimate toolchain variance. The perfect_conductor row uses S=1 in the integral.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_static_polarizability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_total": "float (a.u.)",
          "alpha_valence": "float (a.u.)",
          "alpha_core": "float (a.u.)",
          "alpha_core_valence": "float (a.u.)",
          "alpha_tail": "float (a.u.)",
          "uncertainty_total": "float (a.u.)"
        }
      },
      "description": "Static scalar polarizability of ground-state Cs and its decomposition into core, valence, core-valence, and tail contributions."
    },
    {
      "file": "step_02_C3_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "C3_core",
          "C3_valence",
          "C3_core_valence",
          "C3_tail",
          "C3_total"
        ],
        "units": {
          "C3_core": "a.u.",
          "C3_valence": "a.u.",
          "C3_core_valence": "a.u.",
          "C3_tail": "a.u.",
          "C3_total": "a.u."
        }
      },
      "description": "C3 dispersion coefficients for the interaction of ground-state Cs with a perfect conductor, Au, Si, SiO2, SiNx, ordinary sapphire, extraordinary sapphire, birefringent sapphire, and YAG, with contribution breakdown."
    },
    {
      "file": "step_03_f3_fitting_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "A1",
          "A2",
          "B2",
          "B3"
        ]
      },
      "description": "Fitting parameters (A1, A2, B2, B3) for the rational-function representation of the retardation function f3(z) for each surface."
    }
  ],
  "notes": "All numerical values are compared to hidden gold from the source paper with tolerances that absorb legitimate toolchain variance. The perfect_conductor row uses S=1 in the integral."
}
```

## How you are scored
A hidden verifier will load your three output files and compare the computed quantities to reference benchmarks. Each artifact is scored independently: the static polarizability and its components, the C3 coefficients, and the fitting parameters are each evaluated against a hidden ground truth. The comparison tolerances are chosen to absorb legitimate implementation differences while still requiring meaningful agreement. In addition, certain structural relations (e.g., the expected ordering of C3 coefficients across materials) may be checked. The final reward is a weighted combination of the per-artifact scores, so a faithful reproduction earns full credit while partial or inaccurate work yields a proportionally lower score.
