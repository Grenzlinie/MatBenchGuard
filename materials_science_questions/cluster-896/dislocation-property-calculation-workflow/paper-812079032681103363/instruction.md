# First‑Principles Calculation of Elastic Constants and Dislocation Properties in GaAs

## Problem background
GaAs is a technologically important III‑V semiconductor with high electron mobility, widely used in optoelectronics and high‑frequency devices. Its mechanical reliability and plastic deformation behaviour are governed by dislocation motion, yet the Peierls stress—the intrinsic lattice resistance to dislocation glide—is not well established for the 30° partial dislocation that controls plasticity. Experimental estimates of the Peierls stress exist only as rough extrapolations, and classical Peierls‑Nabarro (P‑N) theory, which treats the crystal as an elastic continuum, predicts values that disagree with experiments by an order of magnitude. An improved P‑N theory that incorporates the discrete lattice correction is expected to give more accurate predictions, but first‑principles predictions of the core width and Peierls stress for GaAs using this improved theory are still needed. This task computes the second‑ and third‑order elastic constants, the generalized stacking fault energy (GSFE), and from them the dislocation core half‑widths and Peierls stresses, thereby providing a first‑principles assessment of the dislocation properties of GaAs.

## Approach
The approach follows a three‑stage computational workflow. First, density functional theory (DFT) total‑energy calculations are performed under the local density approximation (LDA) on bulk GaAs using six independent Lagrangian strain tensors (variants A–F) at multiple strain amplitudes. By fitting third‑order polynomials to the energy‑vs‑strain data, the equilibrium lattice constant and the second‑ and third‑order elastic constants of the cubic crystal are extracted via the appropriate symmetry relations.

Second, a DFT slab model of the {111} glide set (12 atomic layers, 15 Å vacuum) is used to compute the GSFE along the (1/2)⟨112⟩ direction. Rigid relative shifts of the upper slab are applied, and energies are collected for two sets of calculations: one without relaxation (unrelaxed) and one in which the atoms are allowed to relax only in the ⟨111⟩ direction (relaxed). The resulting GSFE curves are then fitted to the functional form

γ(u) = γ cos²(π u / b) · [1 + Δ₁ cos²(π u / b) + Δ₂ cos⁴(π u / b)],

where b is the Burgers vector, yielding the dimensionless parameters γ, Δ₁, and Δ₂ for both the relaxed and unrelaxed cases.

Finally, the elastic constants and GSFE parameters are fed into the improved Peierls‑Nabarro integro‑differential equation, which includes a discrete crystal correction term proportional to a parameter β derived from the elastic constants. The equation is solved numerically for a 30° partial dislocation using the Wang truncation method. The core half‑width is obtained from the dislocation density profile, and the Peierls stress is determined from the maximum slope of the dislocation energy as an applied stress is varied. Solutions are obtained both with the full discrete correction (β≠0) and in the continuum limit (β=0), for both the relaxed and unrelaxed GSFE inputs, allowing the discrete effect and the role of structural relaxation to be assessed.

## Reproduction target
Compute the following quantities for GaAs, using LDA‑DFT and the improved Peierls‑Nabarro model:

1. Equilibrium lattice constant a0 (Å) and second‑order elastic constants C₁₁, C₁₂, C₄₄ (GPa), together with the six third‑order elastic constants C₁₁₁, C₁₁₂, C₁₂₃, C₁₄₄, C₁₅₅, C₄₅₆ (GPa).
2. GSFE fitting parameters γ, Δ₁, Δ₂ for both the relaxed and unrelaxed stacking faults (dimensionless).
3. For the 30° partial dislocation:
   - from the relaxed GSFE: core half‑width ξ₀ and Peierls stress σᴾ⁰ (continuum limit, β=0); core half‑width ξ and Peierls stress σᴾ (with discrete correction, β≠0).
   - from the unrelaxed GSFE: core half‑width ξ and Peierls stress σᴾ (with discrete correction).

The results are to be written into the three scored output files specified in the workflow.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GaAs LDA pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python 3 with numpy, scipy, matplotlib: numpy, scipy, matplotlib

## Workflow steps

### Step 1: DFT total‑energy calculations for elastic constants
- Role: process
- Action: Perform DFT total‑energy calculations (LDA functional, plane‑wave basis, Quantum ESPRESSO) on GaAs using six Lagrangian strain tensors (variants A–F) at multiple strain values. Collect energy‑vs‑strain data for each strain type.
- Evidence: none

### Step 2: Extract elastic constants
- Role: scored
- Action: Fit third‑order polynomials to the energy‑strain data from Step 1 and derive the SOECs and TOECs using the cubic‑symmetry relations. Write the equilibrium lattice constant a0 (Å) and all elastic constants (C11, C12, C44, C111, C112, C123, C144, C155, C456, in GPa) to the output file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with numeric keys: a0 (float, Å), C11, C12, C44, C111, C112, C123, C144, C155, C456 (all float, GPa).
- Scoring: scored by hidden verifier

### Step 3: DFT slab calculations of generalized stacking fault energy
- Role: process
- Action: Perform DFT slab calculations for the {111} glide set of GaAs using a slab of 12 atomic layers and 15 Å vacuum. Apply rigid shifts of the upper slab along (1/2)⟨112⟩. Compute energies for each shift without relaxation (unrelaxed) and with relaxation of atoms in the ⟨111⟩ direction (relaxed). Collect GSFE data (energy vs. displacement).
- Evidence: none

### Step 4: Fit GSFE and extract parameters
- Role: scored
- Action: Fit the computed GSFE data from Step 3 to the functional form γ(u)=γ cos²(π u / b) * (1 + Δ₁ cos²(π u / b) + Δ₂ cos⁴(π u / b)) for both relaxed and unrelaxed cases. Write the fitting parameters to the output file.
- Output file: `/app/outputs/gsfe_fit_params.json`
- Format: json
- Contract: JSON object with keys: relaxed → {gamma, Delta1, Delta2}, nonrelaxed → {gamma, Delta1, Delta2}. All values dimensionless.
- Scoring: scored by hidden verifier

### Step 5: Solve improved Peierls‑Nabarro equation for 30° partial dislocation
- Role: scored (load-bearing)
- Action: Using the elastic constants from Step 2 and GSFE parameters from Step 4, solve the improved Peierls‑Nabarro integro‑differential equation (including the discrete correction term β) for a 30° partial dislocation via the Wang truncation method. Compute the core half‑widths (ξ, ξ₀) and Peierls stresses (σ_P, σ_P⁰) for both relaxed and unrelaxed GSFE, and write the results to the output file.
- Output file: `/app/outputs/dislocation_properties.json`
- Format: json
- Contract: JSON object with keys: relaxed_xi0 (float, units of b), relaxed_xi (float, units of b), relaxed_sigmaP0 (float, GPa), relaxed_sigmaP (float, GPa), nonrelaxed_xi (float, units of b), nonrelaxed_sigmaP (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/gsfe_fit_params.json`
- `/app/outputs/dislocation_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium lattice constant and second‑ and third‑order elastic constants of GaAs, validated against the paper’s LDA results.
- schema:
  - `type`: object
  - `required`:
    - `a0`: number (Å)
    - `C11`: number (GPa)
    - `C12`: number (GPa)
    - `C44`: number (GPa)
    - `C111`: number (GPa)
    - `C112`: number (GPa)
    - `C123`: number (GPa)
    - `C144`: number (GPa)
    - `C155`: number (GPa)
    - `C456`: number (GPa)

### gsfe_fit_params.json
- path: `/app/outputs/gsfe_fit_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters of the generalized stacking fault energy for relaxed and unrelaxed cases, used to define the restoring force in the P–N equation.
- schema:
  - `type`: object
  - `required`:
    - `relaxed`:
      - `gamma`: number
      - `Delta1`: number
      - `Delta2`: number
    - `nonrelaxed`:
      - `gamma`: number
      - `Delta1`: number
      - `Delta2`: number

### dislocation_properties.json
- path: `/app/outputs/dislocation_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Core half‑widths and Peierls stresses of the 30° partial dislocation in GaAs, obtained from the improved P–N equation with discrete correction.
- schema:
  - `type`: object
  - `required`:
    - `relaxed_xi0`: number (units of b)
    - `relaxed_xi`: number (units of b)
    - `relaxed_sigmaP0`: number (GPa)
    - `relaxed_sigmaP`: number (GPa)
    - `nonrelaxed_xi`: number (units of b)
    - `nonrelaxed_sigmaP`: number (GPa)

Notes: All outputs are scored against the paper's reported LDA values using appropriate tolerances. The dislocation properties step is load‑bearing to ensure the DFT stages are genuinely executed.

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
        "type": "object",
        "required": {
          "a0": "number (Å)",
          "C11": "number (GPa)",
          "C12": "number (GPa)",
          "C44": "number (GPa)",
          "C111": "number (GPa)",
          "C112": "number (GPa)",
          "C123": "number (GPa)",
          "C144": "number (GPa)",
          "C155": "number (GPa)",
          "C456": "number (GPa)"
        }
      },
      "description": "Computed equilibrium lattice constant and second‑ and third‑order elastic constants of GaAs, validated against the paper’s LDA results."
    },
    {
      "file": "gsfe_fit_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "relaxed": {
            "gamma": "number",
            "Delta1": "number",
            "Delta2": "number"
          },
          "nonrelaxed": {
            "gamma": "number",
            "Delta1": "number",
            "Delta2": "number"
          }
        }
      },
      "description": "Fitted parameters of the generalized stacking fault energy for relaxed and unrelaxed cases, used to define the restoring force in the P–N equation."
    },
    {
      "file": "dislocation_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "relaxed_xi0": "number (units of b)",
          "relaxed_xi": "number (units of b)",
          "relaxed_sigmaP0": "number (GPa)",
          "relaxed_sigmaP": "number (GPa)",
          "nonrelaxed_xi": "number (units of b)",
          "nonrelaxed_sigmaP": "number (GPa)"
        }
      },
      "description": "Core half‑widths and Peierls stresses of the 30° partial dislocation in GaAs, obtained from the improved P–N equation with discrete correction."
    }
  ],
  "notes": "All outputs are scored against the paper's reported LDA values using appropriate tolerances. The dislocation properties step is load‑bearing to ensure the DFT stages are genuinely executed."
}
```

## How you are scored
A hidden verifier reads your three output JSON files from `/app/outputs`. Each scored step is evaluated independently against a set of expected reference values (the gold) that are kept secret. The verifier checks that your computed elastic constants, GSFE fit parameters, and dislocation core half‑widths and Peierls stresses fall within acceptable agreement windows, and that key structural relationships hold across the different physical regimes—for example, that the relaxed dislocation is wider and has a lower Peierls stress than the unrelaxed one, and that including the discrete crystal correction widens the core and reduces the stress relative to the continuum limit. The per‑step scores are combined by weight to produce the final reward. Simply reporting a set of numbers without genuinely performing the DFT and solver steps will not pass; the verifier may also inspect that the overall workflow was executed by looking for evidence of intermediate calculations.
