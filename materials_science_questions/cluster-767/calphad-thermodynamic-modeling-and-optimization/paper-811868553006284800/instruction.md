# Reproducing Variational-Parameter Model Parameters and Alloy Properties of Al-Li Melts

## Problem background
Liquid aluminum–lithium alloys are important for both technology and fundamental science. Their thermodynamic, kinetic, and dynamic properties depend sensitively on how electrons correlate with the ionic configuration. A variational-parameter (VP) approach incorporates electron correlation effects into interionic potentials, making it possible to compute model parameters for pure metals and then predict concentration‑dependent properties of the alloy. This task focuses on determining these VP model parameters for pure Al and Li at 1023 K and, using an additive atomic volume (Ω₀) approximation, computing the corresponding alloy properties across the full composition range.

## Approach
The method is based on a self‑consistent variational procedure that treats the conduction‑electron subsystem within a Landau Fermi‑liquid framework and the ion subsystem as a hard‑sphere mixture. For each pure metal the workflow computes:
- exchange–correlation parameter A_v,
- Ashcroft model potential radius r_c,
- hard‑sphere packing coefficient η and diameter d,
- density of states at the Fermi level N(E_F) (via a Green’s‑function approach),
- Landau parameter F₁ˢ and electronic correlation energy E_cor.
These are obtained by minimizing the free energy under the Mansoori–Canfield hard‑sphere approximation at 1023 K.

For the alloy, additive mixing rules are used for A_v and for the average atomic volume (derived from the pure‑metal densities). The Mansoori–Canfield variational procedure for binary hard‑sphere mixtures is then solved to obtain partial packing coefficients η₁ and η₂. Finally, the electrical resistivity is calculated within the Faber–Ziman approximation. The entire calculation is restricted to the additive atomic volume (Ω₀) case; no experimental excess‑entropy correction is applied.

## Reproduction target
1. Compute the self‑consistent VP model parameters for pure Al and Li at 1023 K: A_v, r_c (au), η, d (au), N(E_F), −F₁ˢ, and −E_cor (au). Report these in `pure_metal_parameters.csv`.
2. Using the pure‑metal results and the additive atomic volume (Ω₀) approximation, compute for Li concentrations 0, 20, 40, 60, 80, and 100 at%:
   - exchange–correlation parameter A_v,
   - additive atomic volume Ω₀ (au³),
   - partial packing coefficients η₁ and η₂,
   - electrical resistivity ρₑₗ (μΩ·cm).
   Report the results in `alloy_properties.csv`.

All outputs must be placed under `/app/outputs`.

## Assets

- Python scientific stack (numpy, scipy): numpy scipy matplotlib

## Workflow steps

### Step 1: Compute pure Al and Li VP model parameters at 1023 K
- Role: scored
- Action: Implement the self-consistent variational-parameter procedure for pure Al and Li at 1023 K to determine the exchange–correlation parameter A_v, Ashcroft pseudopotential radius r_c (au), hard‑sphere packing coefficient η, solid‑sphere diameter d (au), density of states at the Fermi level N(E_F), Landau parameter F₁ˢ, and electronic correlation energy E_cor (au), using a Green’s-function approach for N(E_F) and the Mansoori–Canfield hard‑sphere free‑energy minimisation. Report the results in a CSV.
- Output file: `/app/outputs/pure_metal_parameters.csv`
- Format: csv
- Contract: element (text), Av (float), rc_au (float), eta (float), d_au (float), N_EF (float), minus_F1s (float), minus_Ecor_au (float). Two rows: 'Al' and 'Li'.
- Scoring: scored by hidden verifier

### Step 2: Compute concentration‑dependent alloy properties (Ω₀ case)
- Role: scored (load-bearing)
- Action: Using the pure‑component parameters from step 0, additive rules for A_v and atomic volume (alloy density from pure metal densities), and the Mansoori–Canfield variational procedure for binary hard‑sphere mixtures, compute concentration‑dependent properties for Li concentrations 0, 20, 40, 60, 80, 100 at%: exchange–correlation parameter A_v, additive atomic volume Ω₀ (in au³), partial packing coefficients η₁ and η₂, and electrical resistivity ρₑₗ (in μΩ·cm) using the Faber–Ziman approximation. Report the results in a CSV.
- Output file: `/app/outputs/alloy_properties.csv`
- Format: csv
- Contract: Li_at_percent (integer), Av (float), Omega0_au (float), eta1 (float), eta2 (float), resistivity_uohm_cm (float). Rows for 0, 20, 40, 60, 80, 100 at% Li.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_metal_parameters.csv`
- `/app/outputs/alloy_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_metal_parameters.csv
- path: `/app/outputs/pure_metal_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Self-consistent VP model parameters for pure Al and Li melts at 1023 K. Each row corresponds to one element.
- schema:
  - `required_columns`: `element`, `Av`, `rc_au`, `eta`, `d_au`, `N_EF`, `minus_F1s`, `minus_Ecor_au`
  - `units`:
    - `Av`: unitless
    - `rc_au`: atomic units (au)
    - `eta`: unitless
    - `d_au`: atomic units (au)
    - `N_EF`: states/(energy·unit cell) (as defined by authors)
    - `minus_F1s`: unitless
    - `minus_Ecor_au`: atomic units (au)

### alloy_properties.csv
- path: `/app/outputs/alloy_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Concentration-dependent alloy properties under the additive atomic volume (Ω₀) approximation for Al–Li melts at 1023 K, including sound velocity and compressibility.
- schema:
  - `required_columns`: `Li_at_percent`, `Av`, `Omega0_au`, `eta1`, `eta2`, `resistivity_uohm_cm`, `c_m_s`, `beta_inv_Pa`
  - `units`:
    - `Li_at_percent`: at%
    - `Av`: unitless
    - `Omega0_au`: atomic units³ (au³)
    - `eta1`: unitless
    - `eta2`: unitless
    - `resistivity_uohm_cm`: μΩ·cm
    - `c_m_s`: m/s
    - `beta_inv_Pa`: 1/Pa

Notes: The task is limited to the additive atomic volume (Ω₀) case. The checker compares reported values against hidden gold values from the paper using relative tolerances, and additionally scores the sound velocity c and compressibility β derived from the Einstein‑phonon model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_metal_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "element",
          "Av",
          "rc_au",
          "eta",
          "d_au",
          "N_EF",
          "minus_F1s",
          "minus_Ecor_au"
        ],
        "units": {
          "Av": "unitless",
          "rc_au": "atomic units (au)",
          "eta": "unitless",
          "d_au": "atomic units (au)",
          "N_EF": "states/(energy·unit cell) (as defined by authors)",
          "minus_F1s": "unitless",
          "minus_Ecor_au": "atomic units (au)"
        }
      },
      "description": "Self-consistent VP model parameters for pure Al and Li melts at 1023 K. Each row corresponds to one element."
    },
    {
      "file": "alloy_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "Li_at_percent",
          "Av",
          "Omega0_au",
          "eta1",
          "eta2",
          "resistivity_uohm_cm",
          "c_m_s",
          "beta_inv_Pa"
        ],
        "units": {
          "Li_at_percent": "at%",
          "Av": "unitless",
          "Omega0_au": "atomic units³ (au³)",
          "eta1": "unitless",
          "eta2": "unitless",
          "resistivity_uohm_cm": "μΩ·cm",
          "c_m_s": "m/s",
          "beta_inv_Pa": "1/Pa"
        }
      },
      "description": "Concentration-dependent alloy properties under the additive atomic volume (Ω₀) approximation for Al–Li melts at 1023 K, including sound velocity and compressibility."
    }
  ],
  "notes": "The task is limited to the additive atomic volume (Ω₀) case. The checker compares reported values against hidden gold values from the paper using relative tolerances, and additionally scores the sound velocity c and compressibility β derived from the Einstein‑phonon model."
}
```

## How you are scored
A hidden verifier will read your two CSV files and compare each quantity against reference values that account for the variability of independent numerical implementations. In addition, the verifier will check the qualitative requirement that the electrical resistivity at 80 at% Li is at least twice the resistivity at 0 at% Li. Each scored part contributes a portion of the total reward; you are not required to reproduce the reference values exactly, but closer agreement yields a higher score.
