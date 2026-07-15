# Quadrupole ordering in DySb: molecular-field model with given parameters

## Problem background
Rare-earth pnictides (group‑V intermetallic compounds with the rock‑salt structure) exhibit an unusual sequence of phase transitions: they undergo a cubic‑to‑tetragonal lattice distortion at a temperature T* that is a few degrees above the Néel temperature T_N where antiferromagnetic magnetic order sets in. This challenges the conventional picture in which the lattice distortion is directly driven by the magnetic ordering. The present model proposes that the distortion is instead driven by a quadrupole phase transition: the electric quadrupole moments of the rare‑earth 4f electrons order at a higher temperature than the magnetic dipoles, owing to strong biquadratic interactions that dominate over bilinear exchange in these face‑centered cubic antiferromagnets. The lattice strain couples linearly to the quadrupole moment, so when the quadrupoles align the lattice distorts to accommodate the ordered array. Applying this idea to DySb, a molecular‑field Hamiltonian with crystal‑field terms, a biquadratic interaction that couples to the quadrupole operator, and a bilinear exchange that couples to the magnetic moment can be solved self‑consistently to predict a first‑order quadrupole transition and an enhanced magnetic ordering temperature. Your task is to carry out this self‑consistent calculation using the provided parameters and to extract the key quantitative predictions: the quadrupole ordering temperature T* and the size of the quadrupole moment discontinuity at the transition, as well as the hypothetical Néel temperature that would result from bilinear exchange alone.

## Approach
The theory is formulated as a mean‑field Hamiltonian acting on a truncated basis that includes only the ground doublet Γ6 and the first excited quartet Γ8⁽¹⁾ (located at 20 K). The Hamiltonian contains three contributions:

1. **Crystal field** – parameterised by B₄ and B₆ operators that capture the electrostatic environment of the Dy³⁺ ion in the cubic lattice.
2. **Biquadratic interaction** – a term of the form −I₂₀ ⟨O₀²⟩ O₀², where O₀² = 3J_z² − J(J+1) is the quadrupole operator (with J = 15/2 for Dy³⁺) and I₂₀ is the biquadratic coupling constant. This term drives the quadrupole ordering.
3. **Bilinear exchange** – a standard Heisenberg‑like term −I_z ⟨J_z⟩ J_z that couples the magnetic moments.

The procedure is a self‑consistent mean‑field calculation:
- For a given temperature, initialise the mean fields ⟨O₀²⟩ and ⟨J_z⟩ (e.g. to zero).
- Construct the Hamiltonian matrix using these mean fields, diagonalise it, and compute the thermal expectation values ⟨O₀²⟩ and ⟨J_z⟩ from the resulting eigenvalues and eigenvectors.
- Update the mean fields and repeat until convergence.
- Sweep temperature from 0 K to about 15 K, recording the converged expectation values at each step.

The quadrupole transition is first‑order, so ⟨O₀²⟩ jumps discontinuously at T*. You will identify T* as the temperature where this jump occurs and compute the ratio ⟨O₀²⟩(T*)/⟨O₀²⟩(0).

To quantify the enhancement of magnetic ordering by the biquadratic coupling, you will repeat the calculation with I₂₀ set to zero and find the temperature T_N_bilinear below which ⟨J_z⟩ becomes non‑zero. All numerical work can be done with standard Python libraries (numpy, scipy).

## Reproduction target
Implement the molecular‑field model described above to produce two output files:

1. **`/app/outputs/quadrupole_transition_results.json`** – a JSON object containing:
   - `T_star_K` (float): the quadrupole ordering temperature T* in Kelvin, i.e. the temperature at which ⟨O₀²⟩ jumps discontinuously.
   - `discontinuity_ratio` (float): the dimensionless ratio ⟨O₀²⟩(T*)/⟨O₀²⟩(0).

2. **`/app/outputs/spin_only_ordering_temperature.json`** – a JSON object containing:
   - `T_N_bilinear_K` (float): the Néel temperature (in Kelvin) obtained when the biquadratic coupling is turned off (I₂₀ = 0), i.e. the temperature below which ⟨J_z⟩ first becomes non‑zero from bilinear exchange alone.

The parameters to use are fixed: B₄ = −8.88×10⁻³ K, B₆ = 4.27×10⁻⁶ K, I₂₀ = 2.36×10⁻³ K, I_z = 0.217 K, and the basis is the Γ₆ doublet plus the Γ₈⁽¹⁾ quartet at 20 K.

## Assets

- Python scientific computing stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Compute quadrupole transition properties
- Role: scored (load-bearing)
- Action: Implement the molecular-field Hamiltonian for DySb with crystal-field parameters B4 = -8.88e-3 K, B6 = 4.27e-6 K, biquadratic interaction I20 = 2.36e-3 K, and bilinear interaction Iz = 0.217 K, using a truncated basis of the ground doublet Gamma6 and first excited quartet Gamma8^(1) at 20 K. Perform a self-consistent mean-field calculation to obtain the temperature-dependent quadrupole moment <O0^(2)>(T) from 0 K to ~15 K. Identify the first-order transition temperature T* and compute the ratio <O0^(2)>(T*)/<O0^(2)>(0). Write T* in K and the discontinuity ratio (dimensionless) to quadrupole_transition_results.json.
- Output file: `/app/outputs/quadrupole_transition_results.json`
- Format: json
- Contract: JSON object with keys: T_star_K (float, K) and discontinuity_ratio (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 2: Compute spin-only Néel temperature
- Role: scored
- Action: Re-run the same molecular-field calculation with the biquadratic coupling I20 set to zero. Determine the Néel temperature T_N_bilinear (temperature below which average spin <Jz> becomes non-zero). Write T_N_bilinear in K to spin_only_ordering_temperature.json.
- Output file: `/app/outputs/spin_only_ordering_temperature.json`
- Format: json
- Contract: JSON object with key: T_N_bilinear_K (float, K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quadrupole_transition_results.json`
- `/app/outputs/spin_only_ordering_temperature.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quadrupole_transition_results.json
- path: `/app/outputs/quadrupole_transition_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed quadrupole ordering temperature and discontinuity ratio from the self-consistent model.
- schema:
  - `type`: object
  - `required`:
    - `T_star_K`: float
    - `discontinuity_ratio`: float
  - `units`:
    - `T_star_K`: K
    - `discontinuity_ratio`: dimensionless

### spin_only_ordering_temperature.json
- path: `/app/outputs/spin_only_ordering_temperature.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Hypothetical Néel temperature from bilinear exchange only.
- schema:
  - `type`: object
  - `required`:
    - `T_N_bilinear_K`: float
  - `units`:
    - `T_N_bilinear_K`: K

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quadrupole_transition_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_star_K": "float",
          "discontinuity_ratio": "float"
        },
        "units": {
          "T_star_K": "K",
          "discontinuity_ratio": "dimensionless"
        }
      },
      "description": "Computed quadrupole ordering temperature and discontinuity ratio from the self-consistent model."
    },
    {
      "file": "spin_only_ordering_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_N_bilinear_K": "float"
        },
        "units": {
          "T_N_bilinear_K": "K"
        }
      },
      "description": "Hypothetical Néel temperature from bilinear exchange only."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads the two JSON files. The verifier checks that the files exist and contain the required keys, then compares your reported values against hidden reference values that correspond to the correct results of the self‑consistent calculation. Each output is scored individually, and the final reward is a weighted combination of the scores from the two stages.

Scoring uses tolerances that absorb the legitimate spread coming from numerical implementation details (e.g. convergence criteria, temperature step size, linear‑algebra routines) while still rejecting values that are far from the physics. Full credit is given when your results fall within the prescribed tolerance; beyond that, the reward decreases gradually with increasing deviation. The verifier operates entirely offline and does not fetch any external data.
