# Static Transferred Hyperfine Constants in PbF2:Mn2+

## Problem background
When a transition metal ion is embedded in an insulating crystal, its magnetic electrons can polarize the spin density at the nuclei of surrounding ligand ions. This transferred hyperfine interaction is particularly interesting in superionic conductors like PbF2, where the Mn2+–F– distance is unusually large compared with typical fluorides. Computing the isotropic and anisotropic hyperfine constants at the 19F site adjacent to a Mn2+ ion from first principles tests the theory of long-range charge transfer and is essential for interpreting the electron paramagnetic resonance spectra observed in this system.

## Approach
The static transferred hyperfine interaction is modeled using a two-center three-electron configuration-interaction approach. The starting point is the Hartree-Fock atomic wavefunctions for F– (1s, 2s, 2p) and Mn2+ (3d) from standard tables. Two-center one- and two-electron integrals are computed at the known interatomic distance. These integrals, together with a configurational energy separation, determine electron-transfer amplitudes (γ) for the s, σ, and π channels. From the transfer amplitudes and overlap integrals, ligand admixture amplitudes (λ) are obtained, which yield spin densities at the fluorine nucleus. The isotropic (Fermi-contact) constant A_s is derived from the 2s spin density, including a 1s–2s cross-term correction, while the anisotropic dipolar contributions A_σ and A_π are obtained from the 2pσ and 2pπ spin densities. The total anisotropic constant A_p is the sum A_σ + A_π. Only the static part of the interaction is considered.

## Reproduction target
Compute the isotropic transferred hyperfine constant A_s and the total anisotropic constant A_p (the sum of the σ and π dipolar contributions) for a Mn2+–F– pair at the interatomic distance R = 2.58 Å, using the static two-center three-electron configuration-interaction method described above. Express both constants in MHz and write them to the JSON file `/app/outputs/hyperfine_constants.json` with keys `A_s` and `A_p`.

## Assets

- Clementi and Roetti, At. Data Nucl. Data Tables 14, 177 (1974) – Hartree-Fock wavefunctions for F and Mn

## Workflow steps

### Step 1: Acquire Hartree-Fock atomic wavefunctions
- Role: process
- Action: Obtain the radial Hartree-Fock wavefunctions for F⁻ (1s, 2s, 2p) and Mn²⁺ (3d) from the Clementi-Roetti tables or an equivalent public source.
- Evidence: none

### Step 2: Compute two-center one- and two-electron integrals
- Role: process
- Action: Use the acquired wavefunctions to compute all required overlap, kinetic, Coulomb, and exchange integrals between F⁻ orbitals (1s, 2s, 2pσ, 2pπ) and Mn²⁺ d orbitals (d_{z²} for σ, d_t for π) at the interatomic distance R = 2.58 Å, and compute the radial expectation values ⟨r⁻³⟩ for the 2p F⁻ orbital.
- Evidence: none

### Step 3: Construct transfer coefficients γ_s, γ_σ, γ_π
- Role: process
- Action: Combine the computed integrals with the configurational energy difference Δ_B = −1.0 a.u. according to the two-center three-electron configuration-interaction formula to obtain the electron-transfer amplitudes for the s, σ, and π channels.
- Evidence: none

### Step 4: Calculate ligand amplitudes λ and spin densities f_s, f_σ, f_π
- Role: process
- Action: From the transfer coefficients and the overlap integrals, compute the ligand admixture amplitudes λ_s, λ_σ, λ_π; then obtain the isotropic spin density f_s (applying the 1s–2s cross-term correction) and the anisotropic spin densities f_σ and f_π by squaring the λ amplitudes.
- Evidence: none

### Step 5: Evaluate transferred hyperfine constants A_s and A_p
- Role: scored (load-bearing)
- Action: Insert the spin densities together with the known atomic parameters (|χ_s(0)|² for 2s, ⟨r⁻³⟩ for 2p, g = 2.0, μ_B, g_N for ¹⁹F, μ_N) into the isotropic and anisotropic hyperfine formulas to compute A_s and the total anisotropic constant A_p = A_σ + A_π (both in MHz). Write the results to the output file.
- Output file: `/app/outputs/hyperfine_constants.json`
- Format: json
- Contract: {"A_s": number (MHz), "A_p": number (MHz)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hyperfine_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hyperfine_constants.json
- path: `/app/outputs/hyperfine_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed isotropic hyperfine constant A_s and the total anisotropic hyperfine constant A_p. The checker compares these values against a hidden reference with an appropriate tolerance.
- schema:
  - `type`: object
  - `required`: `A_s`, `A_p`
  - `additionalProperties`: False
  - `properties`:
    - `A_s`:
      - `type`: number
      - `unit`: MHz
      - `description`: Isotropic (Fermi‑contact) transferred hyperfine constant
    - `A_p`:
      - `type`: number
      - `unit`: MHz
      - `description`: Total anisotropic transferred hyperfine constant (sum of σ and π dipolar contributions)
  - `description`: Hyperfine constants computed by the static two‑center three‑electron model for the Mn²⁺–F⁻ pair at R=2.58 Å.

Notes: Only the static part of the theory is reproduced; the soft‑phonon contribution is excluded because it requires an experimentally deduced matrix element that is not derivable from the published first‑principles workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hyperfine_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "A_s",
          "A_p"
        ],
        "additionalProperties": false,
        "properties": {
          "A_s": {
            "type": "number",
            "unit": "MHz",
            "description": "Isotropic (Fermi‑contact) transferred hyperfine constant"
          },
          "A_p": {
            "type": "number",
            "unit": "MHz",
            "description": "Total anisotropic transferred hyperfine constant (sum of σ and π dipolar contributions)"
          }
        },
        "description": "Hyperfine constants computed by the static two‑center three‑electron model for the Mn²⁺–F⁻ pair at R=2.58 Å."
      },
      "description": "Contains the computed isotropic hyperfine constant A_s and the total anisotropic hyperfine constant A_p. The checker compares these values against a hidden reference with an appropriate tolerance."
    }
  ],
  "notes": "Only the static part of the theory is reproduced; the soft‑phonon contribution is excluded because it requires an experimentally deduced matrix element that is not derivable from the published first‑principles workflow."
}
```

## How you are scored
A hidden verifier reads your output file and compares the reported `A_s` and `A_p` values to a hidden reference. Credit is based on how closely your computed constants match the expected result; the verifier does not reveal the reference values or tolerances. All intermediate process steps are required to reach the final constants, but only the final output file is scored. Producing plausible numbers without genuinely executing the integral and spin-density computations will not earn full credit.
