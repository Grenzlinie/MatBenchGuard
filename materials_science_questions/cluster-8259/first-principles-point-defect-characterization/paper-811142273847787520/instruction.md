# Compute helium-like donor energies and orbital radii for oxygen donors in Si and SiO2

## Problem background
Point defects such as oxygen donors in silicon (Si) and silicon dioxide (SiO₂) introduce localized energy levels inside the band gap. These double-donor centers can be modeled as a helium-like system: two electrons bound to an effective positive charge, embedded in a host material whose response is captured by an effective mass m* and a relative permittivity ε/ε₀. The helium-like variational model provides closed-form expressions for the two successive ionization energies (E₁, E₂) and for the corresponding effective orbital radii (a₁, a₂) as functions of material parameters and an effective nuclear charge Z_eff. This task computes those energies and radii for oxygen donors in both Si and SiO₂ using the published model.

## Approach
The helium-like model treats the two-electron ground state with a variational wavefunction; the total energy is minimized to obtain an expression in terms of Z_eff. The first ionization energy E₁ (removal of the first electron) and the second ionization energy E₂ (removal of the second electron) are then written in effective atomic units. Applying effective-medium theory replaces the free‑electron Rydberg constant with an effective Rydberg constant Reff that depends on the host’s effective mass ratio (m*/m) and relative permittivity (ε/ε₀):

Reff = (m*/m) / (ε/ε₀)² × (R₀ / 2)   with   R₀ = 2 × 13.6 eV.

The closed‑form ionization energies are:

E₁ = [Z_eff² – (5/4) Z_eff + 25/128] × Reff,
E₂ = Z_eff² × Reff.

The effective orbital radii follow from the Bohr‑radius scaling:

a₁ = (ε/ε₀) × (m / m*) × 0.291 Å,
a₂ = (ε/ε₀) × (m / m*) × 0.529 Å.

The necessary host parameters and the pre‑determined Z_eff values (derived from experimental data) are provided in the workflow step. No other inputs are required.

## Reproduction target
Compute the first and second donor ionization energies (E₁, E₂) and the effective orbital radii (a₁, a₂) for oxygen donors in Si and in SiO₂ using the helium‑like closed‑form formulas. Use the specific material parameters and effective nuclear charges supplied in the workflow step. Output all eight quantities in a single JSON file (“results.json”) as specified in the output contract.

## Assets
Python 3.8 or later (standard library only; no external packages needed). All calculations use elementary arithmetic and the built‑in math module.

## Workflow steps

### Step 1: Compute helium-like donor energies and radii
- Role: scored
- Action: Implement the helium-like closed-form expressions for the first and second ionization energies (E1, E2) and effective orbital radii (a1, a2) as described in the paper’s method. Use the provided host parameters and effective nuclear charges: for Si, m*/m = 0.26, ε/ε₀ = 12, Z_eff = 2.42; for SiO₂, m*/m = 0.50, ε/ε₀ = 3.9, Z_eff = 2.13. Compute all eight quantities and write them to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'Si_E1' (float, eV), 'Si_E2' (float, eV), 'Si_a1' (float, Å), 'Si_a2' (float, Å), 'SiO2_E1' (float, eV), 'SiO2_E2' (float, eV), 'SiO2_a1' (float, Å), 'SiO2_a2' (float, Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed helium-like donor ionization energies and effective orbital radii for Si and SiO2.
- schema:
  - `type`: object
  - `required_keys`: `Si_E1`, `Si_E2`, `Si_a1`, `Si_a2`, `SiO2_E1`, `SiO2_E2`, `SiO2_a1`, `SiO2_a2`
  - `properties`:
    - `Si_E1`:
      - `type`: number
      - `units`: eV
    - `Si_E2`:
      - `type`: number
      - `units`: eV
    - `Si_a1`:
      - `type`: number
      - `units`: Å
    - `Si_a2`:
      - `type`: number
      - `units`: Å
    - `SiO2_E1`:
      - `type`: number
      - `units`: eV
    - `SiO2_E2`:
      - `type`: number
      - `units`: eV
    - `SiO2_a1`:
      - `type`: number
      - `units`: Å
    - `SiO2_a2`:
      - `type`: number
      - `units`: Å

Notes: The checker compares the reported energies and radii to reference values and verifies that the ratios E2/E1 and a2/a1 are approximately 2.0 for both materials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "Si_E1",
          "Si_E2",
          "Si_a1",
          "Si_a2",
          "SiO2_E1",
          "SiO2_E2",
          "SiO2_a1",
          "SiO2_a2"
        ],
        "properties": {
          "Si_E1": {
            "type": "number",
            "units": "eV"
          },
          "Si_E2": {
            "type": "number",
            "units": "eV"
          },
          "Si_a1": {
            "type": "number",
            "units": "Å"
          },
          "Si_a2": {
            "type": "number",
            "units": "Å"
          },
          "SiO2_E1": {
            "type": "number",
            "units": "eV"
          },
          "SiO2_E2": {
            "type": "number",
            "units": "eV"
          },
          "SiO2_a1": {
            "type": "number",
            "units": "Å"
          },
          "SiO2_a2": {
            "type": "number",
            "units": "Å"
          }
        }
      },
      "description": "The computed helium-like donor ionization energies and effective orbital radii for Si and SiO2."
    }
  ],
  "notes": "The checker compares the reported energies and radii to reference values and verifies that the ratios E2/E1 and a2/a1 are approximately 2.0 for both materials."
}
```

## How you are scored
A hidden verifier reads your “results.json” file. It checks each of the eight reported values against the expected results that follow from the model and the given parameters. In addition, the verifier checks that for both materials the ratios E₂/E₁ and a₂/a₁ are consistent with the structural predictions of the helium‑like model (each ratio should be approximately 2.0). Your reward is a weighted sum over all checks, with each check carrying equal weight; a perfect score requires all values and ratios to fall within acceptable tolerances. The verifier does not require you to match any specific published table; it only evaluates the correctness of your computed outputs.
