# DFT spin-state & electronic structure analysis of Fe complexes

## Problem background
In the trinuclear oxo-centred iron(III) complex with S=5/2 ions on a triangle, antiferromagnetic exchange on a threefold-symmetric framework creates spin frustration that cannot be accommodated without a structural distortion. Low-temperature inelastic incoherent neutron scattering (IINS) reveals eight magnetic transitions, which are assigned to two non-equivalent sets of molecules: one set is described by a static "isosceles" coupling model with two distinct exchange constants (J and J_ab), while the other set is described by a dynamic "scalene" model in which the three coupling constants are equally spaced, characterised by an average ⟨J⟩ and a distortion parameter D. From the observed IINS transition energies and infrared (IR) data, the exchange coupling constants and the displacement of the central oxygen atom from the centre of the metal triangle can be derived.

## Approach
A spin-only Heisenberg Hamiltonian for three S=5/2 spins is used. For the isosceles (set A) model, the Hamiltonian depends on two coupling constants J (for the two equivalent Fe–Fe pairs) and J_ab (for the unique pair). Diagonalising this Hamiltonian yields transition energies that are compared with the set‑A band energies from the provided data. For the scalene (set B) extreme limit, the three coupling constants are taken to be equally spaced as ⟨J⟩−9D, ⟨J⟩, and ⟨J⟩+9D. In this limit the allowed transition energies are 9D, −3⟨J⟩−9D, −3⟨J⟩, and −3⟨J⟩+9D. A least‑squares fit of these model energies to the observed set‑B bands gives ⟨J⟩ and D. Separately, the central oxygen displacement x is estimated by equating the elastic strain energy of the O–Fe₃ asymmetric stretch to the electronic ground‑state splitting. This uses the IR asymmetric stretch frequency, the oxygen mass, and the lowest observed IINS transition energy, together with the relation between the force constant, frequency, mass, and displacement.

## Reproduction target
You are given two CSV resource files: `observed_energies.csv` (columns: band_label, energy_meV, set, assignment) containing the IINS transitions from the literature, and `ir_data.csv` (columns: ν_asym, bandwidth, ΔE) containing the IR data for the complex. Write a program that:
1. reads these datasets;
2. for the set‑A bands, diagonalises the isosceles spin Hamiltonian and performs a least‑squares fit to obtain J and J_ab;
3. for the set‑B bands, uses the scalene extreme‑limit model to fit ⟨J⟩ and D;
4. computes the central oxygen displacement x (in Å) from the IR data and the lowest IINS transition energy using the elastic strain energy relation;
5. outputs the results as a single JSON file at `/app/outputs/fitted_parameters.json` with the exact structure described in the workflow step.

## Assets

- observed_energies.csv
- ir_data.csv
- Python 3 with scientific libraries: python3, numpy, scipy

## Workflow steps

### Step 1: Fit exchange models and compute displacement
- Role: scored (load-bearing)
- Action: Read observed_energies.csv and ir_data.csv. Diagonalize the spin-only Heisenberg Hamiltonian for three S=5/2 spins with two coupling constants (isosceles) to fit J, J_ab to the set-A band energies. Diagonalize the same Hamiltonian with three equally spaced coupling constants (scalene extreme limit) to fit ⟨J⟩, D to the set-B band energies. Using the IR data and the elastic strain energy relation, compute the central oxygen displacement x (Å).
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {
  "set_A": {
    "J": <float>,
    "J_ab": <float>
  },
  "set_B": {
    "langle_J_rangle": <float>,
    "D": <float>
  },
  "distortion": {
    "x_angstrom": <float>
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted exchange coupling constants for the isosceles (set A) and scalene (set B) models, and the central oxygen displacement derived from IR data.
- schema:
  - `type`: object
  - `required`: `set_A`, `set_B`, `distortion`
  - `items`:
    - `set_A`:
      - `type`: object
      - `required`: `J`, `J_ab`
      - `properties`:
        - `J`:
          - `type`: number
          - `unit`: meV
        - `J_ab`:
          - `type`: number
          - `unit`: meV
    - `set_B`:
      - `type`: object
      - `required`: `langle_J_rangle`, `D`
      - `properties`:
        - `langle_J_rangle`:
          - `type`: number
          - `unit`: meV
        - `D`:
          - `type`: number
          - `unit`: meV
    - `distortion`:
      - `type`: object
      - `required`: `x_angstrom`
      - `properties`:
        - `x_angstrom`:
          - `type`: number
          - `unit`: angstrom

Notes: The scored quantities are the fitted J, J_ab, ⟨J⟩, D, and the displacement x. The solver must produce a single JSON file with the exact keys shown. The checker will compare each numeric field to hidden reference values (paper-reported) with absolute tolerances (not disclosed to the solver).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "set_A",
          "set_B",
          "distortion"
        ],
        "items": {
          "set_A": {
            "type": "object",
            "required": [
              "J",
              "J_ab"
            ],
            "properties": {
              "J": {
                "type": "number",
                "unit": "meV"
              },
              "J_ab": {
                "type": "number",
                "unit": "meV"
              }
            }
          },
          "set_B": {
            "type": "object",
            "required": [
              "langle_J_rangle",
              "D"
            ],
            "properties": {
              "langle_J_rangle": {
                "type": "number",
                "unit": "meV"
              },
              "D": {
                "type": "number",
                "unit": "meV"
              }
            }
          },
          "distortion": {
            "type": "object",
            "required": [
              "x_angstrom"
            ],
            "properties": {
              "x_angstrom": {
                "type": "number",
                "unit": "angstrom"
              }
            }
          }
        }
      },
      "description": "Fitted exchange coupling constants for the isosceles (set A) and scalene (set B) models, and the central oxygen displacement derived from IR data."
    }
  ],
  "notes": "The scored quantities are the fitted J, J_ab, ⟨J⟩, D, and the displacement x. The solver must produce a single JSON file with the exact keys shown. The checker will compare each numeric field to hidden reference values (paper-reported) with absolute tolerances (not disclosed to the solver)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/fitted_parameters.json` and compares each numeric field (J, J_ab, ⟨J⟩, D, x) to reference values derived from the published study. The comparison uses appropriate tolerances that account for legitimate numerical and implementation variations. Each quantity contributes to a weighted overall score between 0 and 1. The exact tolerances and weights are not disclosed; your goal is to produce results that are as accurate as possible given the described methodology and the provided data.
