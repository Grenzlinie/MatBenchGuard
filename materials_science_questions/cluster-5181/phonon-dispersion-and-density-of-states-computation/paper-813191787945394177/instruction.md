# Structural optimization and phonon mode stabilization in La2CuO4 with covalent overlap term

## Problem background
The work addresses the role of covalency in shaping the structural parameters and phonon spectrum of the high-temperature superconductor La2CuO4 in its tetragonal phase. An ionic reference model based on pairwise potentials derived from ab initio ion charge densities can describe many features, but it tends to overestimate the planar lattice constant and leaves certain phonon modes unstable. The goal is to determine how adding a simple covalent overlap term to the pair potentials changes the equilibrium structure and the frequencies of specific phonon modes, and whether those modes become stable.

## Approach
Construct an ionic model for tetragonal La2CuO4 using pairwise potentials computed via the Gordon‑Kim overlap method from atomic DFT charge densities of isolated ions. Fit each short‑range potential to a two‑exponential form. For the nearest‑neighbour Cu–O planar interaction, add an attractive covalent term of the form −α exp(−β R) with α = 2.114 a.u. and β = 0.796 a.u. Replace nominal charges with effective ionic charges: Cu +1.6, O_xy −1.8, O_z −2, La +3. Minimize the total ionic energy with respect to the tetragonal structural parameters a, c/a, z(O_z), z(La) to obtain the equilibrium structure. From the same pair potentials, construct the dynamical matrix and compute phonon frequencies at the Γ and X points; extract the frequencies of the two E_u modes at Γ and the E_g mode at X. Compare these results to those obtained from the pure ionic model to assess the effect of covalency.

## Reproduction target
Produce two JSON artifacts under `/app/outputs`:

1. `structural_params.json` — the minimized structural parameters **a** (Å), **c/a**, **z(O_z)**, and **z(La)** for the covalence‑including model described above.
2. `mode_stabilities.json` — the frequencies (in THz) of the two E_u modes at the Γ point and the E_g mode at the X point, obtained from the phonon calculation for the same covalence‑including structure.

The parameters and frequencies must be computed by the workflow steps; simply copying reported values is not sufficient.

## Assets

- PySCF (atomic DFT code): pyscf
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate ionic charge densities
- Role: process
- Action: Use an atomic DFT code (e.g., PySCF) to compute the valence charge densities of isolated La3+, Cu2+, and O2- ions applying a Watson sphere stabilization for O2-. Produce spherically averaged densities rho_alpha(r) for each ion.
- Evidence: none

### Step 2: Compute and fit short-range pair potentials
- Role: process
- Action: From the ionic densities, calculate the short-range pair potentials Phi_alpha_beta(R) between all ion pairs using the Gordon-Kim method (overlap model). Fit each short-range potential to a two-exponential form (alpha+ * exp(-beta+ * R) - alpha- * exp(-beta- * R)). Use nominal charges for the Coulomb part initially.
- Evidence: none

### Step 3: Add covalent term and set effective charges
- Role: process
- Action: For the Cu–O_xy nearest-neighbour interaction, add the fitted covalent exponential term -α exp(-β R) with parameters α=2.114 a.u. and β=0.796 a.u. Use effective ionic charges: Cu+1.6, O_xy-1.8, O_z-2, La+3. The modified pair potentials become the input for the subsequent energy minimization and phonon calculation.
- Evidence: none

### Step 4: Energy minimization and structural parameter extraction
- Role: scored (load-bearing)
- Action: Using the augmented pair potentials from the previous step, minimize the total ionic energy E = (1/2) Σ' Φ_αβ(|R_β^b - R_α^0|) with respect to the tetragonal structural parameters a, c/a, z(Oz), z(La). Record the optimized parameters as the Ecov≠0 model structure.
- Output file: `/app/outputs/structural_params.json`
- Format: json
- Contract: JSON object with keys: a (float, in Angstrom), c_over_a (float), z_Oz (float), z_La (float). Example: {"a": 3.69, "c_over_a": 3.38, "z_Oz": 0.189, "z_La": 0.362}
- Scoring: scored by hidden verifier

### Step 5: Phonon calculation and stability verification
- Role: scored (load-bearing)
- Action: Construct the dynamical matrix from the same augmented pair potentials for the Ecov≠0 structure. Compute phonon frequencies at high-symmetry points (Γ and X). Extract the frequencies of the two Eu modes at Γ and the Eg mode at X. Record the frequencies (in THz); all three must be positive, indicating that these previously unstable modes are now stabilized.
- Output file: `/app/outputs/mode_stabilities.json`
- Format: json
- Contract: JSON object with keys: E_u_mode_1_frequency_THz (float), E_u_mode_2_frequency_THz (float), E_g_mode_frequency_THz (float). Example: {"E_u_mode_1_frequency_THz": 1.5, "E_u_mode_2_frequency_THz": 3.2, "E_g_mode_frequency_THz": 0.8}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_params.json`
- `/app/outputs/mode_stabilities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_params.json
- path: `/app/outputs/structural_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized structural parameters for the Ecov≠0 model.
- schema:
  - `type`: object
  - `required`: `a`, `c_over_a`, `z_Oz`, `z_La`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
    - `c_over_a`:
      - `type`: number
    - `z_Oz`:
      - `type`: number
    - `z_La`:
      - `type`: number

### mode_stabilities.json
- path: `/app/outputs/mode_stabilities.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Frequencies of the two Eu modes at Γ and the Eg mode at X; must be positive to demonstrate stabilization.
- schema:
  - `type`: object
  - `required`: `E_u_mode_1_frequency_THz`, `E_u_mode_2_frequency_THz`, `E_g_mode_frequency_THz`
  - `properties`:
    - `E_u_mode_1_frequency_THz`:
      - `type`: number
      - `unit`: THz
    - `E_u_mode_2_frequency_THz`:
      - `type`: number
      - `unit`: THz
    - `E_g_mode_frequency_THz`:
      - `type`: number
      - `unit`: THz

## Scope and omitted results

This task is scoped to the tetragonal covalence model (Ecov≠0) as the paper's primary quantitative result for structural parameters and mode stabilisation.  Several other topics discussed in the paper are NOT scored here, for the following concrete reasons (doctrine D7):

- **Reduced band dispersion and polarizability**: The paper investigates the effect of narrowing the antibonding band on the Cu–Cu polarizability and the phonon dispersion.  This requires a specific two‑dimensional 11‑band tight‑binding model (Ref. 3) whose parameters are not tabulated in the paper; they are only described qualitatively.  Without those exact parameters a unique polarizability cannot be reconstructed, so there is no verifiable gold.

- **Ferroelectric mode softening under axial dipolar fluctuations**: This is a hypothetical investigation without a reported numerical target; the paper only discusses that dipolar fluctuations could soften the mode, but no specific frequency or threshold is given.  Hence no hidden gold exists and the topic cannot be scored.

- **Orthorhombic phase (structural parameters and phonon dispersion)**: The orthorhombic calculations use different ionic configurations (rigid‑ion, soft‑ion) without a covalence term.  There is no single “paper‑reported” orthorhombic covalence model; the paper only gives results for ionic models, and those results are not the same as the covalence model that is the central reproduction target.  Including the orthorhombic phase would require a separate, full structural relaxation in a lower‑symmetry space, constituting a distinct task beyond the present scope.

- **Charge fluctuation amplitudes and Tc–hole‑content relation**: Table IV’s charge‑fluctuation amplitudes are model‑dependent outputs of the polarizability calculation that require the tight‑binding model (see first point).  The Tc–hole‑content relation is a theoretical interpretation, not a quantitative artifact that can be recomputed from the ionic model workflow.

These omissions are intentional and do not affect the coverage of the paper’s main covalence‑driven structural reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "c_over_a",
          "z_Oz",
          "z_La"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å"
          },
          "c_over_a": {
            "type": "number"
          },
          "z_Oz": {
            "type": "number"
          },
          "z_La": {
            "type": "number"
          }
        }
      },
      "description": "Optimized structural parameters for the Ecov≠0 model."
    },
    {
      "file": "mode_stabilities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "E_u_mode_1_frequency_THz",
          "E_u_mode_2_frequency_THz",
          "E_g_mode_frequency_THz"
        ],
        "properties": {
          "E_u_mode_1_frequency_THz": {
            "type": "number",
            "unit": "THz"
          },
          "E_u_mode_2_frequency_THz": {
            "type": "number",
            "unit": "THz"
          },
          "E_g_mode_frequency_THz": {
            "type": "number",
            "unit": "THz"
          }
        }
      },
      "description": "Frequencies of the two Eu modes at Γ and the Eg mode at X; must be positive to demonstrate stabilization."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted `structural_params.json` and `mode_stabilities.json`. It compares your structural parameters to reference values (derived from the paper's covalence‑including model) with appropriate absolute tolerances. It checks that all three phonon frequencies are positive, indicating stabilization. It may also perform a consistency check that the lattice constant a is smaller than the pure ionic model value. These checks are combined into a final reward between 0 and 1. Simply reporting the correct numbers without executing the described workflow will not satisfy the verifier's consistency requirements.
