# First-principles effective pair interactions and metastable phase boundaries for an ordered intermetallic phase from a disordered solid solution

## Problem background
The Al-Li alloy system exhibits precipitation of the metastable L1₂ ordered δ′ phase from a disordered fcc solid solution. Understanding the thermodynamic driving forces for ordering and the metastable phase boundaries requires knowledge of the effective pair interactions (EPIs) between Al and Li atoms. These interactions can be obtained from first-principles total energy calculations on fcc-based ordered superstructures via the Connolly-Williams cluster expansion. The derived EPIs are then used in a static concentration wave (SCW) free energy model to compute quantitative measures of ordering instability and phase equilibria. The task is to reproduce these calculations and obtain the key thermodynamic quantities that characterize the ordering transition and metastable two-phase region.

## Approach
The computational pipeline consists of three main stages. First, density-functional theory (DFT) total energy calculations are performed for eleven fcc-based Al-Li superstructures at a fixed unit-cell volume of 107.0 a.u.³, using the TB-LMTO method as implemented in the Questaal code. Cohesive energies are derived by subtracting the atomic ground-state energies of the constituents. Second, the cohesive energies are used in a Connolly-Williams inversion with the correlation functions of the tetrahedron-octahedron (TO) cluster approximation to extract the effective pair interactions J₂⁽¹⁾ (first-nearest-neighbour) and J₂⁽²⁾ (second-nearest-neighbour). The EPIs are then Fourier-transformed to the special points [000]* and [100]* of the fcc lattice using the known cell-function matrix. Third, these Fourier-transformed interactions are fed into the static concentration wave free energy expressions. The free energy of the disordered α phase depends only on composition and J(000)/k_B, while the free energy of the L1₂ ordered δ′ phase depends additionally on order parameter η and J(100)/k_B, with configurational entropy treated in the Bragg-Williams approximation. The equilibrium order parameter at a given composition and temperature is found by minimizing the ordered-phase free energy, respecting the maximum attainable order parameter. Metastable phase boundaries are determined by constructing the free-energy-versus-composition curves for both phases and finding the common tangent. The ordering instability temperature T_i⁻ is obtained directly from J(100)/k_B and the composition via a known closed-form expression.

## Reproduction target
Compute the effective pair interactions J₂⁽¹⁾ and J₂⁽²⁾ at a unit-cell volume of 107.0 a.u.³, their Fourier transforms J(000)/k_B and J(100)/k_B, the ordering instability temperature T_i⁻ at solute concentrations c=0.10 and 0.25, the equilibrium order parameter η_eq of the L1₂ phase at T=1000 K and stoichiometric composition (c=0.25), and the metastable α-phase solubility limit and δ′ composition at T=1000 K. All results must be written in the specified JSON output files.

## Assets

- TB-LMTO (Questeal): https://www.questaal.org/
- Python environment: python>=3.8,numpy,scipy

## Workflow steps

### Step 1: DFT total energy calculations for f.c.c.-based Al–Li superstructures
- Role: process
- Action: Compute the cohesive energies of the following f.c.c.-based Al–Li superstructures at a fixed unit‑cell volume of 107.0 a.u.³ using the TB‑LMTO method (Questeal): Al (f.c.c.), Al₃Li (L1₂), Al₃Li (DO₂₂), Al₂Li, AlLi (L1₀), Al₂Li₂, AlLi (L1₁), AlLi₂, AlLi₃ (L1₂), AlLi₃ (DO₂₂), Li (f.c.c.). Cohesive energy is total energy minus the sum of atomic ground‑state energies of the constituents.
- Evidence: `/app/outputs/dft_energies.json`

### Step 2: Connolly–Williams inversion for effective pair interactions
- Role: scored (load-bearing)
- Action: Using the cohesive energies from step_0_dft and the cluster correlation functions of the tetrahedron–octahedron (TO) cluster expansion (standard values for the listed superstructures), perform the Connolly–Williams inversion (solve the linear system) to obtain the effective pair interactions J₂⁽¹⁾ (first-nearest neighbour) and J₂⁽²⁾ (second-nearest neighbour) at volume 107.0 a.u.³. Output the values in Rydberg.
- Output file: `/app/outputs/step_01_epis.json`
- Format: json
- Contract: {"J2_1": <float in Ry>, "J2_2": <float in Ry>, "volume": 107.0}
- Scoring: scored by hidden verifier

### Step 3: Fourier transform of EPIs
- Role: scored
- Action: Compute the Fourier‑transformed pair interactions J(000)/k_B and J(100)/k_B from J₂⁽¹⁾ and J₂⁽²⁾ using the known cell‑function matrix for the f.c.c. lattice: [[-4.0, 6.0], [12.0, 6.0]]. Output the results in Kelvin.
- Output file: `/app/outputs/step_02_fourier.json`
- Format: json
- Contract: {"J000_over_kB": <float in K>, "J100_over_kB": <float in K>}
- Scoring: scored by hidden verifier

### Step 4: Ordering instability temperatures
- Role: scored
- Action: Calculate the ordering instability temperature T_i⁻ at compositions c=0.10 and c=0.25 using the formula T_i⁻ = (J(100)/k_B) · c(1−c). Output the temperatures in Kelvin.
- Output file: `/app/outputs/step_03_t_i_minus.json`
- Format: json
- Contract: {"c_0.10": <float in K>, "c_0.25": <float in K>}
- Scoring: scored by hidden verifier

### Step 5: Equilibrium order parameter at stoichiometric composition
- Role: scored (load-bearing)
- Action: For composition c=0.25 (stoichiometric Al₃Li) and temperature T=1000 K, minimize the static concentration wave free energy of the L1₂ ordered phase with respect to the order parameter η, using the Bragg–Williams configurational entropy and the interactions J(000)/k_B and J(100)/k_B from step_2_fourier. The minimization must respect the maximum attainable order parameter at this composition. Output the optimal value η_eq.
- Output file: `/app/outputs/step_04_eta_eq.json`
- Format: json
- Contract: {"eta_eq": <float>, "temperature": 1000, "composition": 0.25}
- Scoring: scored by hidden verifier

### Step 6: Metastable phase boundaries at 1000 K
- Role: scored (load-bearing)
- Action: Construct the free energy versus composition curves for the disordered α phase and the fully ordered L1₂ (δ′) phase at T=1000 K using the static concentration wave free energy expressions with J(000)/k_B and J(100)/k_B from step_2_fourier. Determine the common tangent to these curves to obtain the compositions of the two coexisting phases: the α solubility limit (Li concentration in the disordered phase) and the δ′ composition. Output both as atomic fractions of Li.
- Output file: `/app/outputs/step_05_phase_boundaries.json`
- Format: json
- Contract: {"alpha_solubility_limit": <float>, "delta_prime_composition": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_epis.json`
- `/app/outputs/step_02_fourier.json`
- `/app/outputs/step_03_t_i_minus.json`
- `/app/outputs/step_04_eta_eq.json`
- `/app/outputs/step_05_phase_boundaries.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_epis.json
- path: `/app/outputs/step_01_epis.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Effective pair interactions J₂⁽¹⁾ and J₂⁽²⁾ from Connolly‑Williams inversion of DFT cohesive energies.
- schema:
  - `type`: object
  - `required`:
    - `J2_1`: float
    - `J2_2`: float
    - `volume`: float
  - `units`:
    - `J2_1`: Ry
    - `J2_2`: Ry
    - `volume`: a.u.^3

### step_02_fourier.json
- path: `/app/outputs/step_02_fourier.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fourier‑transformed pair interactions at special points for the f.c.c. lattice.
- schema:
  - `type`: object
  - `required`:
    - `J000_over_kB`: float
    - `J100_over_kB`: float
  - `units`:
    - `J000_over_kB`: K
    - `J100_over_kB`: K

### step_03_t_i_minus.json
- path: `/app/outputs/step_03_t_i_minus.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ordering instability temperatures T_i⁻ at compositions c=0.10 and c=0.25.
- schema:
  - `type`: object
  - `required`:
    - `c_0.10`: float
    - `c_0.25`: float
  - `units`:
    - `c_0.10`: K
    - `c_0.25`: K

### step_04_eta_eq.json
- path: `/app/outputs/step_04_eta_eq.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium order parameter of the L1₂ phase at T=1000 K and stoichiometric composition.
- schema:
  - `type`: object
  - `required`:
    - `eta_eq`: float
    - `temperature`: number
    - `composition`: number
  - `units`:
    - `eta_eq`: dimensionless
    - `temperature`: K
    - `composition`: atomic fraction Li

### step_05_phase_boundaries.json
- path: `/app/outputs/step_05_phase_boundaries.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: α/δ′ metastable phase boundary compositions at T=1000 K.
- schema:
  - `type`: object
  - `required`:
    - `alpha_solubility_limit`: float
    - `delta_prime_composition`: float
  - `units`:
    - `alpha_solubility_limit`: atomic fraction Li
    - `delta_prime_composition`: atomic fraction Li

Notes: All numeric outputs are compared to hidden paper‑reported reference values using predefined tolerances that absorb method‑spread (different DFT functional/basis) but exclude random guesses. The checker does not require exact agreement; a correct re‑run within tolerance passes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_epis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "J2_1": "float",
          "J2_2": "float",
          "volume": "float"
        },
        "units": {
          "J2_1": "Ry",
          "J2_2": "Ry",
          "volume": "a.u.^3"
        }
      },
      "description": "Effective pair interactions J₂⁽¹⁾ and J₂⁽²⁾ from Connolly‑Williams inversion of DFT cohesive energies."
    },
    {
      "file": "step_02_fourier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "J000_over_kB": "float",
          "J100_over_kB": "float"
        },
        "units": {
          "J000_over_kB": "K",
          "J100_over_kB": "K"
        }
      },
      "description": "Fourier‑transformed pair interactions at special points for the f.c.c. lattice."
    },
    {
      "file": "step_03_t_i_minus.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c_0.10": "float",
          "c_0.25": "float"
        },
        "units": {
          "c_0.10": "K",
          "c_0.25": "K"
        }
      },
      "description": "Ordering instability temperatures T_i⁻ at compositions c=0.10 and c=0.25."
    },
    {
      "file": "step_04_eta_eq.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "eta_eq": "float",
          "temperature": "number",
          "composition": "number"
        },
        "units": {
          "eta_eq": "dimensionless",
          "temperature": "K",
          "composition": "atomic fraction Li"
        }
      },
      "description": "Equilibrium order parameter of the L1₂ phase at T=1000 K and stoichiometric composition."
    },
    {
      "file": "step_05_phase_boundaries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_solubility_limit": "float",
          "delta_prime_composition": "float"
        },
        "units": {
          "alpha_solubility_limit": "atomic fraction Li",
          "delta_prime_composition": "atomic fraction Li"
        }
      },
      "description": "α/δ′ metastable phase boundary compositions at T=1000 K."
    }
  ],
  "notes": "All numeric outputs are compared to hidden paper‑reported reference values using predefined tolerances that absorb method‑spread (different DFT functional/basis) but exclude random guesses. The checker does not require exact agreement; a correct re‑run within tolerance passes."
}
```

## How you are scored
Each of the five scored output files is independently evaluated by a hidden verifier. The verifier compares the numerical values in each file against reference values with appropriate tolerances. The partial scores are weighted and combined to yield an overall reward between 0 and 1. To achieve a high score, you must perform the full computational workflow; simply reporting values, whether correct or not, without executing the steps is unlikely to pass the verification. Note that the verifier does not inspect intermediate files or logs; only the specified JSON outputs are checked.
