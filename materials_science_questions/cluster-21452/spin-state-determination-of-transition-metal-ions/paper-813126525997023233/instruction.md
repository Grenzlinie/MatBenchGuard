# Compute Uniaxial Rotational Strengths for Mn²⁺ Spin-Forbidden Transitions

## Problem background
Spin-forbidden d–d transitions of Mn²⁺ ions in certain host crystals can exhibit circular dichroism (CD). Interpreting the CD requires calculating uniaxial rotational strengths from ligand-field theory, combining the effects of an asymmetric odd‑parity crystal field and spin‑orbit coupling. This task computes those strengths for three specific transitions within the d⁵ manifold of Mn²⁺, providing theoretical predictions to compare with experimental CD measurements.

## Approach
The calculation uses a perturbative Hamiltonian H = H₀ + V_u + V_so, where H₀ includes the octahedral crystal field for a d⁵ ion, V_u is an odd‑parity ligand‑field operator (a sum of one‑electron spherical harmonics of rank 3), and V_so is the spin‑orbit coupling. The wavefunctions are taken from the Koide–Pryce formalism. Electric‑dipole transition moments between the ground ⁶A₁ and the excited states (⁴A₁, ⁴E_u, ⁴E_v) are evaluated via second‑order perturbation theory, mixing states through V_u and V_so. The uniaxial rotational strength for each transition is computed with the Buckingham–Dunn formula, which involves the imaginary part of the product of electric‑dipole and magnetic‑dipole/electric‑quadrupole moments. The relative results are then converted to absolute strengths using a supplied odd‑field scale factor. The workflow implements this computation from the given parameters and formulas.

## Reproduction target
Produce the JSON file `/app/outputs/rotational_strengths.json` containing the absolute uniaxial rotational strengths (in units of 10⁻⁴⁴ c.g.s.) for the transitions ⁶A₁ → ⁴A₁, ⁶A₁ → a⁴E_u, and ⁶A₁ → a⁴E_v. The computation must use the provided crystal‑field parameters (Dq=800 cm⁻¹, B=800 cm⁻¹, C=3200 cm⁻¹), spin‑orbit coupling constants (ζ = ζ′ = 270 cm⁻¹), odd‑field scale parameter (P₁β = 2.0 × 10⁻⁴⁰ c.g.s.), and the Koide–Pryce wavefunctions. The output file must be a JSON object with keys "R(6A1->4A1)", "R(6A1->a4Eu)", and "R(6A1->a4Ev)", each mapping to a float.

## Assets

- Koide-Pryce wavefunctions for Mn2+ d5 octahedral: 10.1080/14786435808237076
- Buckingham-Dunn uniaxial rotational strength formula: 10.1039/J19710001988

## Workflow steps

### Step 1: Compute uniaxial rotational strengths
- Role: scored (load-bearing)
- Action: Implement the perturbative Hamiltonian H = H0 + Vu + Vso using Koide-Pryce wavefunctions for the d5 manifold, with crystal-field parameter Dq=800 cm⁻¹, Racah parameters B=800 cm⁻¹ and C=3200 cm⁻¹, and spin-orbit coupling constant ζ=ζ'=270 cm⁻¹. Compute electric-dipole transition matrix elements for the spin-forbidden transitions ⁶A₁→⁴A₁, ⁶A₁→ₐ⁴E_u, and ⁶A₁→ₐ⁴E_v using second-order perturbation theory with the odd-parity ligand-field operator Vu = ∑ B₁ r³ t_{(3)}_{2ζ}(θ,φ) and spin-orbit coupling. Apply the Buckingham–Dunn uniaxial rotational strength formula. Convert the relative rotational strengths to absolute values in units of 10^{-44} c.g.s. using the odd-field scale parameter P₁β = 2.0×10^{-40} c.g.s. Output the three absolute strengths to /app/outputs/rotational_strengths.json.
- Output file: `/app/outputs/rotational_strengths.json`
- Format: json
- Contract: JSON object with keys "R(6A1->4A1)", "R(6A1->a4Eu)", "R(6A1->a4Ev)", each mapping to a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rotational_strengths.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rotational_strengths.json
- path: `/app/outputs/rotational_strengths.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Absolute uniaxial rotational strengths in units of 10^{-44} c.g.s. for the three spin-forbidden transitions. The hidden checker compares each value to the paper-reported reference within a relative tolerance.
- schema:
  - `type`: object
  - `required`:
    - `R(6A1->4A1)`: float
    - `R(6A1->a4Eu)`: float
    - `R(6A1->a4Ev)`: float
  - `items`: object
  - `units`: object

Notes: The agent must implement the ligand-field perturbation theory as described. No external data download is needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rotational_strengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "R(6A1->4A1)": "float",
          "R(6A1->a4Eu)": "float",
          "R(6A1->a4Ev)": "float"
        },
        "items": {},
        "units": {}
      },
      "description": "Absolute uniaxial rotational strengths in units of 10^{-44} c.g.s. for the three spin-forbidden transitions. The hidden checker compares each value to the paper-reported reference within a relative tolerance."
    }
  ],
  "notes": "The agent must implement the ligand-field perturbation theory as described. No external data download is needed."
}
```

## How you are scored
A hidden verifier will load your `/app/outputs/rotational_strengths.json` and compare each of the three values against a hidden reference. Each transition contributes to the overall score, and the final reward is the weighted combination of the per‑value scores. Full credit requires that all three computed strengths fall within the allowed tolerance of the reference. The verifier does not check whether you looked up the answer; successful reproduction depends on a correct reimplementation of the physics‑based computation as described in the workflow.
