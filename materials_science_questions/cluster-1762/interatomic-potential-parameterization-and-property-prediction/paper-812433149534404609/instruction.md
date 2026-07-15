# Reproduce Fe Bond-Order Potential and Computed Properties

## Problem background
Fe is a technologically important transition metal, and accurate interatomic potentials that capture directional bonding are critical for large-scale atomistic simulations. Traditional many-body potentials often fail to reproduce key properties such as the elastic constant C44, the relative energies of different crystal phases, and the pressure-induced BCC-to-HCP transformation. This task evaluates a bond-order potential that explicitly incorporates angular-dependent bonding through an environmental parameter, similar in spirit to potentials originally developed for tetrahedrally bonded semiconductors. The potential is designed to reproduce a set of experimental reference properties and a universal scaling energy curve, and its ability to predict a suite of physical quantities—including elastic moduli, phase energetics, surface energy, and transformation pressure—is the central result to be reproduced.

## Approach
The bond-order potential expresses the total energy as a sum over atom pairs of a repulsive and an attractive contribution, both modulated by a smooth cut-off function acting between the second and third neighbor shells. The repulsive term is an exponential that can include a strong short-range stiffening at very small separations. The attractive term is an exponential multiplied by a bond-order function that depends on the local environment of the bond. This bond-order function is a polynomial in a local coordination-like variable ζ, raised to a power f, where ζ is constructed as a sum over all other atoms of the cut-off function, an exponential distance factor, and an angular function g(θ). The angular function depends on the cosine of the bond angle and includes several adjustable parameters. The potential is fitted by a multi-variate optimization that minimizes deviations from experimental reference data (the BCC lattice constant, cohesive energy, elastic constants C44 and C′, the (111) surface energy, and the cohesive energies of FCC and HCP Fe at specified volumes) while also matching a universal scaling equation-of-state curve for BCC Fe. Once the parameters are determined, the fitted potential is used to compute the equilibrium BCC properties (lattice constant, atomic volume, cohesive energy, and the full set of elastic constants C11, C12, C44, C′ and bulk modulus K) by energy minimization and finite strain. The (111) surface energy is obtained from a slab calculation. Cohesive energies of FCC and HCP Fe are computed at the volumes corresponding to the experimental polymorphic transformations. Finally, the BCC-HCP phase transformation pressure is found by calculating enthalpies H(P)=E+PV for both phases as a function of pressure and identifying the crossing point.

## Reproduction target
After fitting the potential to the provided experimental reference data and universal scaling constraints, compute the following physical properties for Fe and write them to `/app/outputs/computed_properties.json` as a single JSON object:

- BCC equilibrium lattice constant a0 (Å)
- BCC equilibrium atomic volume Ω0 (Å³)
- BCC cohesive energy E_coh (eV)
- Elastic constants C11, C12, C44, C′ (in units of 10² GPa)
- Bulk modulus K (in units of 10² GPa)
- (111) surface energy per atom (eV/atom)
- Cohesive energy of FCC Fe at atomic volume 11.152 Å³ (eV)
- Cohesive energy of HCP Fe at atomic volume 10.398 Å³ (eV)
- BCC-to-HCP phase transformation pressure (kbar)

## Assets

- Fe experimental reference data for fitting
- Python with numpy and scipy: numpy, scipy

## Workflow steps

### Step 1: Implement bond-order potential functional form
- Role: process
- Action: Implement the bond-order potential energy function for Fe as defined in the paper. This includes the cut-off function, repulsive term, attractive bond-order term, bond-order function b, environmental coordinator ζ, and angular function g(θ). The potential takes atomic positions and a set of parameters as input and returns the total energy.
- Evidence: none

### Step 2: Fit potential parameters to experimental data
- Role: process
- Action: Optimize the potential parameters (A, B, β1, β2, β3, β4, α, f, γ1…γ6, c, d, β, h, δ, nz, cut-off radii) to reproduce the experimental reference properties (lattice parameter, cohesive energy, elastic moduli C44 and C′, (111) surface energy, FCC and HCP cohesive energies) and to match the universal scaling energy curve for BCC Fe. Use a multi-variate minimizer. Record the optimized parameters in fitted_parameters.json.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 3: Compute target physical properties
- Role: scored (load-bearing)
- Action: Using the fitted potential, compute (a) BCC equilibrium lattice constant a0, atomic volume Ω0, cohesive energy E_coh, and elastic constants C11, C12, C44, C′, bulk modulus K; (b) (111) surface energy via a slab calculation; (c) cohesive energies of FCC and HCP Fe at the specified experimental volumes; (d) the BCC-HCP phase transformation pressure by calculating enthalpies H(P)=E+PV for both phases as a function of pressure and locating the crossing point. Write all results to computed_properties.json.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {
  "a_bcc": float,   // lattice constant in Å
  "Omega0_bcc": float,   // atomic volume in Å³
  "E_coh_bcc": float,    // cohesive energy in eV
  "C11": float,          // elastic constant in 10² GPa
  "C12": float,
  "C44": float,
  "C_prime": float,
  "K": float,            // bulk modulus in 10² GPa
  "E_surf_111": float,   // surface energy in eV/atom
  "E_coh_fcc": float,    // cohesive energy of FCC in eV
  "E_coh_hcp": float,    // cohesive energy of HCP in eV
  "phase_transition_pressure": float   // transition pressure in kbar
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All computed physical properties of Fe as reported in the paper's Table 1 and Figure 3. Values must be derived from the fitted bond-order potential.
- schema:
  - `type`: object
  - `required`: `a_bcc`, `Omega0_bcc`, `E_coh_bcc`, `C11`, `C12`, `C44`, `C_prime`, `K`, `E_surf_111`, `E_coh_fcc`, `E_coh_hcp`, `phase_transition_pressure`
  - `properties`:
    - `a_bcc`:
      - `type`: number
      - `unit`: Angstrom
    - `Omega0_bcc`:
      - `type`: number
      - `unit`: Angstrom^3
    - `E_coh_bcc`:
      - `type`: number
      - `unit`: eV
    - `C11`:
      - `type`: number
      - `unit`: 10^2 GPa
    - `C12`:
      - `type`: number
      - `unit`: 10^2 GPa
    - `C44`:
      - `type`: number
      - `unit`: 10^2 GPa
    - `C_prime`:
      - `type`: number
      - `unit`: 10^2 GPa
    - `K`:
      - `type`: number
      - `unit`: 10^2 GPa
    - `E_surf_111`:
      - `type`: number
      - `unit`: eV/atom
    - `E_coh_fcc`:
      - `type`: number
      - `unit`: eV
    - `E_coh_hcp`:
      - `type`: number
      - `unit`: eV
    - `phase_transition_pressure`:
      - `type`: number
      - `unit`: kbar

Notes: The checker will compare each numeric value to paper-reported reference values using absolute tolerances. The exact tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a_bcc",
          "Omega0_bcc",
          "E_coh_bcc",
          "C11",
          "C12",
          "C44",
          "C_prime",
          "K",
          "E_surf_111",
          "E_coh_fcc",
          "E_coh_hcp",
          "phase_transition_pressure"
        ],
        "properties": {
          "a_bcc": {
            "type": "number",
            "unit": "Angstrom"
          },
          "Omega0_bcc": {
            "type": "number",
            "unit": "Angstrom^3"
          },
          "E_coh_bcc": {
            "type": "number",
            "unit": "eV"
          },
          "C11": {
            "type": "number",
            "unit": "10^2 GPa"
          },
          "C12": {
            "type": "number",
            "unit": "10^2 GPa"
          },
          "C44": {
            "type": "number",
            "unit": "10^2 GPa"
          },
          "C_prime": {
            "type": "number",
            "unit": "10^2 GPa"
          },
          "K": {
            "type": "number",
            "unit": "10^2 GPa"
          },
          "E_surf_111": {
            "type": "number",
            "unit": "eV/atom"
          },
          "E_coh_fcc": {
            "type": "number",
            "unit": "eV"
          },
          "E_coh_hcp": {
            "type": "number",
            "unit": "eV"
          },
          "phase_transition_pressure": {
            "type": "number",
            "unit": "kbar"
          }
        }
      },
      "description": "All computed physical properties of Fe as reported in the paper's Table 1 and Figure 3. Values must be derived from the fitted bond-order potential."
    }
  ],
  "notes": "The checker will compare each numeric value to paper-reported reference values using absolute tolerances. The exact tolerances are hidden."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/computed_properties.json` and compare each numeric value against reference values that a correct implementation of the described potential and fitting protocol is expected to produce. The comparison uses absolute tolerances appropriate for independent re-implementations; the exact tolerances are not disclosed. The score is the fraction of the reported properties whose absolute difference from the hidden reference falls within the tolerance. The intermediate fitting artifact (`fitted_parameters.json`) is not scored, but you must perform the fitting yourself because the physical properties to be reported can only be obtained reliably from a correctly fitted potential. The final reward is a single float in [0,1].
