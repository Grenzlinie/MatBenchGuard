# Vibronic fine structure of local states in naphthalene crystals with benzselenophene impurity

## Problem background
Resonance hybridization between impurity electronic states and local exciton states in molecular crystals can lead to anomalous fine structure in vibronic absorption and luminescence spectra. In the system naphthalene with benzselenophene impurity, the impurity 0–0 transition lies close to the exciton band, suggesting that impurity–crystal mixing may significantly alter the observed vibronic bands. The task is to test whether the dynamic theory of vibronic states, with provided impurity resonance matrix elements and a standard naphthalene crystal model, reproduces the computed fine-structure energies, intensities, and polarization ratios for both non-totally symmetric (NTS) and totally symmetric (TS) vibrons. The outcome will determine whether the calculated spectra can account for the experimentally observed fine-structure features and their polarizations.

## Approach
The reproduction uses a two-stage diagonalization of a vibronic Hamiltonian that includes electronic exciton transfer, intramolecular vibrations, linear electron–phonon coupling, and interactions that mix impurity and crystal excitations. In the first stage, the local-state eigenvalue problem is solved for the NTS vibron case (where electron–phonon coupling of type H^(2) is absent) by constructing the vibronic basis from the impurity resonance parameters and the naphthalene crystal Green's functions, yielding wavefunctions |nα> and energies E_nα. In the second stage, the full Hamiltonian, now including the coupling terms that mix exciton, phonon, and impurity degrees of freedom, is diagonalized on this basis to obtain the fine-structure levels, transition intensities (I_a, I_b) and polarization ratios p(a/b). The model uses fixed impurity–crystal resonance matrix elements M_l^imp (M1=60 cm⁻¹, M2=50 cm⁻¹, M3=49 cm⁻¹, M4=50 cm⁻¹) and standard naphthalene exciton band parameters obtained from the literature; all other needed parameters (vibration frequencies, frequency shifts, transition moment ratios) are stated alongside the target quantities.

## Reproduction target
Your task is to compute the vibronic fine structure and write the results to `/app/outputs/vibronic_fine_structure.json`. Specifically:

- For the **NTS vibron** (ν₀ = 509 cm⁻¹, Δν = –89 cm⁻¹): compute, for each impurity site l = 1..4, the excitation defocus (ED) and exciton–phonon (EP) energies (cm⁻¹, relative to the bottom of the two-particle band) and their non‑polarized intensities.
- For the **TS vibron** (ν₀ = 764 cm⁻¹, Δ₄ = –57 cm⁻¹, |p₀|²/|p_A₂|² = 542.5): compute, for each l = 1..4, the EDP bands (bound exciton–defect–phonon combination) with energies E_l, intensities I_a and I_b, and polarization ratios p(a/b); and also compute the ED and EP fine‑structure levels with their individual energies, I_a, I_b, and p(a/b).

Use the provided impurity resonance matrix elements M_l^imp (60, 50, 49, 50 cm⁻¹) and obtain the naphthalene crystal exciton band parameters (nearest‑neighbour interactions, dispersion, Green's functions) from the standard reference: Broude, V.L., Rashba, E.I., Sheka, E.F., 'Spektroskopiya molekulyarnykh eksitonov', Energoizdat, Moscow (1981). All energies are to be reported relative to the bottom of the two-particle band; intensities are in relative units.

## Assets

- Naphthalene exciton band parameters and Green's functions

## Workflow steps

### Step 1: Vibronic basis calculation (first-stage diagonalization)
- Role: process
- Action: Construct the vibronic basis by solving the local-state eigenvalue problem for the non-totally symmetric vibron case using the provided impurity resonance parameters and the naphthalene crystal model. This yields the wavefunctions |nα> and energies E_nα.
- Evidence: none

### Step 2: Compute vibronic fine structure
- Role: scored (load-bearing)
- Action: Using the basis from Step 1, compute the NTS vibronic fine structure (ED and EP energies and intensities for l=1..4) with ν₀=509 cm⁻¹, Δν=-89 cm⁻¹, and the TS vibronic spectrum (EDP bands and ED/EP fine levels) with ν₀=764 cm⁻¹, Δ₄=-57 cm⁻¹, and |p₀|²/|p_A₂|²=542.5. Implement the two-stage diagonalization scheme and solve for energies, intensities, and polarization ratios. Write the results to vibronic_fine_structure.json.
- Output file: `/app/outputs/vibronic_fine_structure.json`
- Format: json
- Contract: {
  "nts": [
    {
      "l": int,
      "ed": [{"energy": float, "intensity": float}],
      "ep": [{"energy": float, "intensity": float}]
    }
  ],
  "ts": {
    "edp_bands": [
      {
        "l": int,
        "M_imp": float,
        "E": float,
        "I_a": float,
        "I_b": float,
        "p_ab": float
      }
    ],
    "ed_ep_fine": [
      {
        "l": int,
        "type": "ED" or "EP",
        "E_j": float,
        "I_a": float,
        "I_b": float,
        "p_ab": float
      }
    ]
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vibronic_fine_structure.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vibronic_fine_structure.json
- path: `/app/outputs/vibronic_fine_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The single scored artifact containing all computed vibronic fine-structure energies, intensities and polarization ratios. The checker compares each reported value against the paper's truth within allowed tolerances.
- schema:
  - `type`: object
  - `required`: `nts`, `ts`
  - `nts`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `l`, `ed`, `ep`
      - `l`: integer
      - `ed`:
        - `type`: array
        - `items`:
          - `type`: object
          - `required`: `energy`, `intensity`
          - `energy`: float (cm⁻¹)
          - `intensity`: float
      - `ep`:
        - `type`: array
        - `items`:
          - `type`: object
          - `required`: `energy`, `intensity`
          - `energy`: float (cm⁻¹)
          - `intensity`: float
  - `ts`:
    - `type`: object
    - `required`: `edp_bands`, `ed_ep_fine`
    - `edp_bands`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `l`, `M_imp`, `E`, `I_a`, `I_b`, `p_ab`
        - `l`: integer
        - `M_imp`: float (cm⁻¹)
        - `E`: float (cm⁻¹)
        - `I_a`: float
        - `I_b`: float
        - `p_ab`: float
    - `ed_ep_fine`:
      - `type`: array
      - `items`:
        - `type`: string ("ED" or "EP")
        - `required`: `l`, `type`, `E_j`, `I_a`, `I_b`, `p_ab`
        - `l`: integer
        - `E_j`: float (cm⁻¹)
        - `I_a`: float
        - `I_b`: float
        - `p_ab`: float

Notes: The provided M_l^imp values are: M1=60 cm⁻¹, M2=50 cm⁻¹, M3=49 cm⁻¹, M4=50 cm⁻¹. The naphthalene crystal parameters are to be obtained from the cited literature. All energies are relative to the bottom of the two-particle band.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vibronic_fine_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "nts",
          "ts"
        ],
        "nts": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "l",
              "ed",
              "ep"
            ],
            "l": "integer",
            "ed": {
              "type": "array",
              "items": {
                "type": "object",
                "required": [
                  "energy",
                  "intensity"
                ],
                "energy": "float (cm⁻¹)",
                "intensity": "float"
              }
            },
            "ep": {
              "type": "array",
              "items": {
                "type": "object",
                "required": [
                  "energy",
                  "intensity"
                ],
                "energy": "float (cm⁻¹)",
                "intensity": "float"
              }
            }
          }
        },
        "ts": {
          "type": "object",
          "required": [
            "edp_bands",
            "ed_ep_fine"
          ],
          "edp_bands": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "l",
                "M_imp",
                "E",
                "I_a",
                "I_b",
                "p_ab"
              ],
              "l": "integer",
              "M_imp": "float (cm⁻¹)",
              "E": "float (cm⁻¹)",
              "I_a": "float",
              "I_b": "float",
              "p_ab": "float"
            }
          },
          "ed_ep_fine": {
            "type": "array",
            "items": {
              "type": "string (\"ED\" or \"EP\")",
              "required": [
                "l",
                "type",
                "E_j",
                "I_a",
                "I_b",
                "p_ab"
              ],
              "l": "integer",
              "E_j": "float (cm⁻¹)",
              "I_a": "float",
              "I_b": "float",
              "p_ab": "float"
            }
          }
        }
      },
      "description": "The single scored artifact containing all computed vibronic fine-structure energies, intensities and polarization ratios. The checker compares each reported value against the paper's truth within allowed tolerances."
    }
  ],
  "notes": "The provided M_l^imp values are: M1=60 cm⁻¹, M2=50 cm⁻¹, M3=49 cm⁻¹, M4=50 cm⁻¹. The naphthalene crystal parameters are to be obtained from the cited literature. All energies are relative to the bottom of the two-particle band."
}
```

## How you are scored
A hidden verifier reads your `vibronic_fine_structure.json` and independently scores the NTS and TS fine-structure outputs. For each reported entry (energies, intensities, and polarization ratios), your computed values are compared against a set of hidden reference numbers that were obtained from the original work. The comparison uses tolerances that account for legitimate implementation differences. Your final reward is the fraction of reference entries that are matched within tolerance, combined across the NTS and TS sections with the TS fine-structure section carrying the larger weight. The verifier checks the structure of the output file (that all required fields exist and have the correct types) but only a tiny fraction of the reward comes from mere structure; the bulk of the reward comes from the accuracy of the computed physical quantities.
