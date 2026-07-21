# Self-consistent charge ordering and critical coverage in Cs/Si(001)

## Problem background
Alkali-metal adsorption on Si(001) induces metal–semiconductor transitions as the coverage changes. One proposed mechanism invokes indirect exchange (substrate-mediated) and dipole–dipole repulsion among adatoms, which together can open and then collapse an energy gap in the surface-state band without requiring strong intra-atomic Coulomb repulsion (the Hubbard U). For Cs/Si(001) at large coverage, this model predicts a charge-ordered state and a coverage-dependent gap collapse. Reproducing the self-consistent calculation for this system tests whether the simple indirect-exchange plus dipole–dipole picture can indeed produce charge ordering and gap closure under physically motivated assumptions.

## Approach
The theoretical model treats the substrate surface-state band as a narrow quasi-two-dimensional band of half-width D, with density of states modelled as a rectangle of height 1/(2D) for |ω| ≤ D in the two-dimensional limit (γ → 0). The band is coupled to adatom levels via hybridization V (indirect exchange). Dipole–dipole interactions split the adatom level into two sublattice levels ε_a⁺ = +δ and ε_a⁻ = –δ, where δ = c v ξ θ^{3/2} Z, with coverage θ, adatom charge Z, geometry factor v, and dipole parameter ξ. The self-consistent charge order parameter c is determined by the occupation difference between the two sublattices.

In the two-dimensional limit, the positions of the band edges for each sublattice (±) are (setting V = D):
ω₂⁺ = ω₂⁻ = –D – θ D
ω₄⁺ = ω₄⁻ = D + θ D
and the band widths of the lower subbands are
W̃₃₂⁺ = D + δ,   W̃₃₂⁻ = D – δ   (assuming D > δ).

The Fermi level ε_F is fixed by the conservation of the total number of electrons per surface atom:
n_s + n_a = 1, where n_s = (ε_F – ω₂⁺)/W̃₃₂⁺ + (ε_F – ω₂⁻)/W̃₃₂⁻   (Eq. 18)
and the mean adatom occupation is n_a = 0.77, giving n_s = 0.23.

The adatom occupations for the two sublattices are given by (Eq. 16, with V = D):
n_a⁺ = (D/π) · (ε_F – ω₂⁺) / [ (ε_F – δ)·(ω₂⁺ – δ) ]
n_a⁻ = (D/π) · (ε_F – ω₂⁻) / [ (ε_F + δ)·(ω₂⁻ + δ) ]

The charge order parameter c is found from the self-consistency condition (Eq. 19):
2 c Z = (D/π) [ (ε_F – ω₂⁻) / ((ε_F + δ)(ω₂⁻ + δ)) – (ε_F – ω₂⁺) / ((ε_F – δ)(ω₂⁺ – δ)) ]

The three-dimensional critical coverage θ_C for gap collapse is obtained from the spectral overlap condition ε_a⁺ = Ω₂⁻ and ε_a⁻ = Ω₁⁺, which yields (Eq. 13):
θ_C = (V √2) / (c v ξ Z)
with V = D.

The following parameter values are adopted for Cs/Si(001) at large coverage:
- Band half-width D = 0.17 eV
- Hybridization V = D = 0.17 eV
- Coverage used in the self-consistent calculation: θ = 0.5
- Adatom charge Z = 0.2 (extracted from work-function data at this coverage)
- Geometry factor v = 0.5
- Dipole shift parameter ξ = 22.97 eV (from ξ = 2e² l² N_ML^{3/2} A₀ with l = 2.24 Å, N_ML = 6.78×10¹⁴ cm⁻², A₀ = 9)

The coupled equations are solved for ε_F, δ, and c. Then θ_C is computed from the above formula.

## Reproduction target
Compute the self-consistent level splitting δ (in eV), the charge-order parameter c (dimensionless), and the three-dimensional critical coverage θ_C (dimensionless) for Cs/Si(001) under the assumptions V=D, symmetric adatom levels ε_a^±=±δ, and mean adatom/substrate occupations n_a=0.77, n_s=0.23. Output the three values in a JSON file with keys 'delta_eV', 'c', and 'theta_C'.

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: Self-consistent charge ordering solution
- Role: scored (load-bearing)
- Action: Implement the self-consistent equations described in the Approach. With the parameter values D = 0.17 eV, V = D, θ = 0.5, Z = 0.2, v = 0.5, ξ = 22.97 eV, and mean occupations n_a=0.77, n_s=0.23, solve for the Fermi level ε_F, the level splitting δ (eV), the charge-order parameter c (dimensionless). Then compute the three-dimensional critical coverage θ_C using θ_C = (V√2)/(c v ξ Z). Write the final values delta_eV, c, theta_C to a JSON file.
- Output file: `/app/outputs/self_consistent_results.json`
- Format: json
- Contract: {"delta_eV": number, "c": number, "theta_C": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/self_consistent_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### self_consistent_results.json
- path: `/app/outputs/self_consistent_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Self-consistently determined level splitting δ, charge-order parameter c, and critical coverage θ_C for Cs/Si(001) under the assumptions V=D, ε_a^±=±δ, n_a=0.77, n_s=0.23. Tolerances: δ ±0.05 eV, c ±0.05, θ_C ±0.1.
- schema:
  - `type`: object
  - `required`:
    - `delta_eV`: number (eV)
    - `c`: number (dimensionless)
    - `theta_C`: number (dimensionless)

Notes: The verifier compares each value to paper-reported gold values with the listed tolerances. Full credit requires all three within tolerance; partial credit is proportional to the number of values passing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "self_consistent_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "delta_eV": "number (eV)",
          "c": "number (dimensionless)",
          "theta_C": "number (dimensionless)"
        }
      },
      "description": "Self-consistently determined level splitting δ, charge-order parameter c, and critical coverage θ_C for Cs/Si(001) under the assumptions V=D, ε_a^±=±δ, n_a=0.77, n_s=0.23. Tolerances: δ ±0.05 eV, c ±0.05, θ_C ±0.1."
    }
  ],
  "notes": "The verifier compares each value to paper-reported gold values with the listed tolerances. Full credit requires all three within tolerance; partial credit is proportional to the number of values passing."
}
```

## How you are scored
A hidden verifier reads your `self_consistent_results.json` and compares each of the three values (delta_eV, c, theta_C) to the corresponding reference values derived from the paper's self-consistent calculation. Credit is awarded for each value that falls within a predefined tolerance; the total reward is the fraction of values that pass. Reporting something that is not a valid number or missing a key results in zero reward for that value. The verifier's tolerances are set to accommodate minor numerical differences from different solver implementations.
