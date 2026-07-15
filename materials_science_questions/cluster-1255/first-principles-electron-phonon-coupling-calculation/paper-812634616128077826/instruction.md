# Temperature-dependent properties of V3Si from a microscopic two-band tight-binding model

## Problem background
A-15 intermetallic compounds such as V3Si display a structural martensitic transition from a cubic to a tetragonal phase at low temperature. This transition is accompanied by strongly temperature-dependent anomalies in the shear elastic modulus, magnetic susceptibility, and electronic specific heat. A successful microscopic model must explain all these phenomena from the underlying electronic band structure. Here we implement a three-dimensional two-band tight-binding model based on the transition-metal δ1 orbitals that captures both Peierls-like and Jahn-Teller effects, with the goal of computing the temperature variation of the key observables.

## Approach
A 6×6 tight-binding Hamiltonian is constructed on the six transition-metal sites per unit cell, using the δ1 (x²−y²) orbitals. The matrix includes nearest-neighbour (intrachain) hopping β, next-nearest-neighbour (interchain) hopping γ, and an electron-phonon coupling of the form M(d)=M(0)(1−gd) that depends linearly on interatomic distance changes due to a collective distortion coordinate Δ. For a given set of parameters (Case I: α=0, β=−0.165 eV, γ=0.014 eV, g=3.8 Å⁻¹) and a bare elastic constant K, the two lowest band energies E_k^n(Δ) are obtained by diagonalisation on a uniform k‑mesh covering the Brillouin zone (edges at ±π). The density of states N(E) and its first two energy derivatives are computed via the Gilat–Raubenheimer linear-interpolation scheme. The thermodynamic potential Ω(T,Δ,μ) combines the electronic grand potential with the elastic energy ½KΔ². The electron number is fixed near the peak of the density of states. The bare elastic constant K is calibrated by requiring that the martensitic transition temperature Tm matches the known experimental value of approximately 21 K for V3Si. For each temperature from 0 to 50 K, the chemical potential μ(Δ,T) is solved from the electron number constraint and the free energy is minimised to find the equilibrium distortion Δ_eq(T). The bulk of the Brillouin zone is treated with low-temperature series expansions, while fine integration is used in the flat regions near the Fermi energy. From the equilibrium state the tetragonal distortion ε = |c/a−1|, the magnetic susceptibility χ(T) (density of states weighted by the Fermi-function derivative, plus an adjustable temperature-independent background), and the electronic specific heat C(T) (from the temperature derivative of the entropy) are computed.

## Reproduction target
Using the tight-binding model and the self-consistently determined elastic constant K, produce the temperature-dependent curves and key scalar quantities for V3Si Case I. Output a CSV file (step_01_thermodynamic_curves.csv) with columns T (K), epsilon (dimensionless), chi (emu/g), and C (J/mol·K), covering at least 20 temperatures from 0 to 50 K, densely sampled near the transition. Also output a JSON file (step_02_derived_values.json) containing the zero-temperature tetragonal distortion epsilon_0 (dimensionless), the martensitic transition temperature Tm (K), the slope of the magnetic susceptibility at Tm dchi_dT_at_Tm (in units of 10⁻⁶ emu/g·K), and the specific heat jump Delta_Cv (J/mol·K). The solver must determine the bare elastic constant K and the electron number such that the model yields a realistic transition temperature and charge balance.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Build tight-binding Hamiltonian and compute band energies
- Role: process
- Action: Construct the 6×6 tight-binding Hamiltonian matrix for the two relevant bands as a function of the collective distortion coordinate Δ and wavevector k, using the V3Si Case I parameters: α=0, β=−0.165 eV, γ=0.014 eV, g=3.8 Å⁻¹. The matrix elements follow the model's distance-dependent linear variation (M_{ij}(d)=M_{ij}(0)(1−gd)), with the relations between d₀, d_T and Δ as given in the paper. Diagonalize the Hamiltonian on a uniform mesh of k‑points covering the Brillouin zone (zone edges at ±π) to obtain the two lowest band energies E_k^n(Δ).
- Evidence: `/app/outputs/step_1_band_energies.npy`

### Step 2: Compute density of states and its derivatives
- Role: process
- Action: Compute the electronic density of states N(E) and its first two energy derivatives N'(E), N''(E) using the Gilat–Raubenheimer linear interpolation scheme. Subdivide each small cube of the k‑mesh, calculate the energy gradient at the cube center, and accumulate contributions from constant‑energy plane intersections following the formulas in the paper's Appendix. Produce N(E), N'(E) and N''(E) as functions of E and the distortion Δ.
- Evidence: `/app/outputs/step_2_dos.npz`

### Step 3: Determine equilibrium distortion and chemical potential, including fitting of bare elastic constant K
- Role: process
- Action: Set up the thermodynamic potential Ω(T,Δ,μ) as the sum of the electronic part (sum of band contributions) and the elastic energy ½KΔ². Fix an electron number such that the Fermi level lies near the density‑of‑states peak. Determine the bare elastic constant K by requiring that the resulting martensitic transition temperature Tm matches the experimental value of ≈21 K for V3Si. For each temperature from 0 K to well above Tm (e.g., 0–50 K), solve for the chemical potential μ(Δ,T) from the electron‑number constraint and minimize the free energy to find the equilibrium distortion Δ_eq(T). Use low‑temperature series expansions for the bulk of the Brillouin zone and fine integration in the flat critical regions near the Fermi energy.
- Evidence: `/app/outputs/step_3_equilibrium_data.json`

### Step 4: Compute observable curves and save thermodynamic curves
- Role: scored (load-bearing)
- Action: From the equilibrium distortion and chemical potential obtained in the previous step, compute the following physical observables as functions of temperature: (a) tetragonal distortion ε(T) = |c/a−1| derived from Δ_eq; (b) magnetic susceptibility χ(T) using the electronic density of states and the temperature derivative of the Fermi function, including a constant background term adjusted to match the absolute level at high temperatures, with the electron‑phonon enhancement factor (1+λ) set to 1 for V3Si; (c) electronic specific heat C(T) from the temperature derivative of the electronic entropy. Output a CSV file with columns T, epsilon, chi, C for at least 20 temperatures covering 0–50 K with dense sampling near Tm.
- Output file: `/app/outputs/step_01_thermodynamic_curves.csv`
- Format: csv
- Contract: CSV with columns: T (K, float), epsilon (dimensionless, float), chi (emu/g, float), C (J/mol·K, float). At least 20 rows covering T from 0 to 50 K, with dense sampling near Tm.
- Scoring: scored by hidden verifier

### Step 5: Extract derived quantities
- Role: scored
- Action: From the temperature arrays in step_01_thermodynamic_curves.csv, determine the following derived quantities: the zero‑temperature tetragonal distortion ε(0) (value at the lowest temperature), the martensitic transition temperature Tm (where ε drops to zero or the free energies cross), the slope of the magnetic susceptibility at Tm (dχ/dT in the cubic phase just above Tm), and the specific heat jump ΔCv at Tm (difference between the specific heat in the tetragonal and cubic phases at Tm). Save these as a JSON file.
- Output file: `/app/outputs/step_02_derived_values.json`
- Format: json
- Contract: JSON object with keys: Tm (K, float), epsilon_0 (dimensionless, float), dchi_dT_at_Tm (10^-6 emu/g·K, float), Delta_Cv (J/mol·K, float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermodynamic_curves.csv`
- `/app/outputs/step_02_derived_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermodynamic_curves.csv
- path: `/app/outputs/step_01_thermodynamic_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent tetragonal distortion ε(T), magnetic susceptibility χ(T) and electronic specific heat C(T) computed from the tight-binding model. The checker compares these curves against hidden reference curves using tolerance bands.
- schema:
  - `type`: table
  - `required_columns`: `T`, `epsilon`, `chi`, `C`
  - `units`:
    - `T`: K
    - `epsilon`: dimensionless
    - `chi`: emu/g
    - `C`: J/mol·K

### step_02_derived_values.json
- path: `/app/outputs/step_02_derived_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived scalar values (zero‑temperature distortion, transition temperature, susceptibility slope, specific heat jump) extracted from the thermodynamic curves. The checker compares each value to hidden reference scalar values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Tm`: K
    - `epsilon_0`: dimensionless
    - `dchi_dT_at_Tm`: 10^-6 emu/g·K
    - `Delta_Cv`: J/mol·K

Notes: The bare elastic constant K is not given analytically; the agent must determine it by fitting Tm to the experimental value (~21 K) as described. The magnetic susceptibility includes a constant background term adjusted to match absolute levels. The checker uses hidden reference data and scalar values with tolerances that allow for numerical discretisation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermodynamic_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "epsilon",
          "chi",
          "C"
        ],
        "units": {
          "T": "K",
          "epsilon": "dimensionless",
          "chi": "emu/g",
          "C": "J/mol·K"
        }
      },
      "description": "Temperature-dependent tetragonal distortion ε(T), magnetic susceptibility χ(T) and electronic specific heat C(T) computed from the tight-binding model. The checker compares these curves against hidden reference curves using tolerance bands."
    },
    {
      "file": "step_02_derived_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Tm": "K",
          "epsilon_0": "dimensionless",
          "dchi_dT_at_Tm": "10^-6 emu/g·K",
          "Delta_Cv": "J/mol·K"
        }
      },
      "description": "Derived scalar values (zero‑temperature distortion, transition temperature, susceptibility slope, specific heat jump) extracted from the thermodynamic curves. The checker compares each value to hidden reference scalar values with appropriate tolerances."
    }
  ],
  "notes": "The bare elastic constant K is not given analytically; the agent must determine it by fitting Tm to the experimental value (~21 K) as described. The magnetic susceptibility includes a constant background term adjusted to match absolute levels. The checker uses hidden reference data and scalar values with tolerances that allow for numerical discretisation differences."
}
```

## How you are scored
Each output file is independently assessed by a hidden verifier. The verifier reads the CSV, checks that the T range and row count meet the specification, and compares the numerical columns against reference data within tolerance bands. The JSON-derived values are compared against expected scalars. The final reward is a weighted combination of the scores from the curve-fitting step (primary weight) and the derived-values step; the reward degrades monotonically as deviations increase. Reporting a number without executing the required thermodynamic equilibrium calculations will not pass the verifier, because the hidden checks evaluate the shape, consistency, and quantitative accuracy of the full temperature-dependent profiles.
