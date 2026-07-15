# Determination of EFG orientations and cation distribution in olivine from single-crystal Mössbauer data

## Problem background
Mössbauer spectroscopy on a single crystal of olivine (Mg,Fe)₂SiO₄ can be used to determine the orientation of the electric field gradient (EFG) principal axes at the iron nucleus, the asymmetry parameter η, the sign of the EFG (q), and the distribution of Fe²⁺ ions between the two crystallographically distinct octahedral sites, M(1) and M(2). The intensity ratio of the two quadrupole-split absorption lines, A_H/A_L, depends on the angle between the incident γ‑ray and the EFG principal axes. By measuring this ratio for a set of crystal orientations and fitting the data with a theoretical model that accounts for the crystal symmetry and the angular dependence of the transition probabilities, one can extract the EFG parameters and the site occupancies. In this task, you are given experimental A_H/A_L values for 17 combinations of Θ (polar) and Φ (azimuthal) angles relative to the crystallographic axes a, b, c, and the unit cell dimensions and atomic coordinates of the olivine structure. Your goal is to compute the EFG parameters and cation distribution that best reproduce the observed ratios.

## Approach
The theoretical model for the Mössbauer absorption area ratio is based on the magnetic-dipole transition probabilities derived by Zory (1965). For a single site, the probabilities of the high- and low-energy transitions depend on the polar (θ) and azimuthal (ϕ) angles of the incident γ‑ray relative to the EFG principal axes (x, y, z) and on the asymmetry parameter η. The room-temperature Mössbauer fraction f′ can be taken as isotropic. The overall A_H/A_L for the crystal is obtained by summing the probabilities over all inequivalent EFG orientations contributed by the four M(1) and four M(2) sites, weighted by the Fe²⁺ occupancy fractions. The angles (θ,ϕ) for each site are related to the experimental angles (Θ,Φ) through the direction cosines between the crystallographic axes and the EFG axes, using the known crystal structure and symmetry operations (reflections and rotations) that generate the four equivalent sites of each type. The fitting procedure is iterative: start with an initial guess for the EFG axis directions and η values for both sites, compute the theoretical A_H/A_L for all 17 orientations, compare with experiment, and refine the parameters until a self-consistent best fit is achieved. Because the oxygen coordination polyhedra have approximate axial symmetry, physically reasonable initial orientations can be inferred from the crystal structure, for example, aligning the major EFG axis of M(1) with the O(3b)–M(1)–O(3) bond direction. The fitting must simultaneously determine the Fe²⁺ fraction on each site, subject to the constraint that the total Fe per formula unit is 0.163.

## Reproduction target
Produce two output files:
1. `derived_parameters.json`: An object containing the best-fit EFG principal axis directions (given as axis labels and direction cosines relative to a, b, c), the asymmetry parameter η, and the sign of q for both M(1) and M(2) sites, as well as the Fe²⁺ occupation fractions for each site and the total Fe per formula unit (0.163).
2. `theoretical_area_ratios.csv`: A table of the theoretical A_H/A_L values computed from the fitted parameters for the same 17 (Θ,Φ) orientations that were used in the fit, with columns theta, phi, AH_AL_combined.

The experimental A_H/A_L values and the list of 17 orientations are provided in the table below. The goal is to obtain EFG parameters and site occupancies such that the computed ratios closely match the experimental values, as judged by the hidden verifier.

| Θ (deg) | Φ (deg) | (A_H/A_L)_E (±0.02) |
|---------|---------|----------------------|
| 90.0    | 40.5    | 1.05                 |
| 90.0    | 30.0    | 1.03                 |
| 90.0    | 15.0    | 1.05                 |
| 90.0    | 8.0     | 1.07                 |
| 90.0    | 0.0     | 1.05                 |
| 78.0    | 0.0     | 1.04                 |
| 66.0    | 0.0     | 1.03                 |
| 57.0    | 0.0     | 1.03                 |
| 52.0    | 90.0    | 1.10                 |
| 45.0    | 0.0     | 1.02                 |
| 38.5    | 94.6    | 1.02                 |
| 38.5    | 59.6    | 1.04                 |
| 35.0    | 90.0    | 1.05                 |
| 30.0    | 0.0     | 1.00                 |
| 18.0    | 90.0    | 1.01                 |
| 15.0    | 0.0     | 0.99                 |
| 0.0     | 0.0     | 0.98                 |

## Assets

- Olivine crystal structure (forsterite, Birle et al. 1968): https://www.crystallography.net/cod/1000031.cif
- The unit cell dimensions for the olivine sample are a=4.78 Å, b=10.22 Å, c=5.96 Å. Scale the forsterite coordinates from the CIF file to these dimensions.

## Workflow steps

### Step 1: Fit EFG parameters and cation distribution
- Role: scored
- Action: Implement the theoretical model relating Mössbauer absorption area ratios A_H/A_L to the principal electric field gradient (EFG) axes orientations and asymmetry parameters, based on the angular-dependent transition probabilities and crystallographic symmetry relations. Using the provided experimental area ratios for 17 (Θ, Φ) orientations and the olivine crystal structure, perform an iterative self-consistent fit to determine the EFG principal axis directions, asymmetry parameters η, sign of the EFG parameter q, and the Fe²⁺ occupancy fractions on the M(1) and M(2) sites. Write the optimized parameters to derived_parameters.json.
- Output file: `/app/outputs/derived_parameters.json`
- Format: json
- Contract: JSON object with keys: M1 (eta: float, sign_q: str, Vzz_direction: {axis: str, direction_cosines: {cx, cy, cz}: float}, Vxx_direction: {axis: str, direction_cosines: {cx, cy, cz}}, Vyy_direction: {axis: str, direction_cosines: {cx, cy, cz}}), M2 (similar), site_distribution (M1_fraction: float, M2_fraction: float), total_Fe_per_formula: float, Fe_per_site (M1: float, M2: float).
- Scoring: scored by hidden verifier

### Step 2: Compute theoretical area ratios
- Role: scored (load-bearing)
- Action: Using the fitted parameters from the previous step and the same theoretical model, calculate the theoretical A_H/A_L values for all 17 experimental (Θ, Φ) orientations. Output a CSV file with columns theta, phi, AH_AL_combined.
- Output file: `/app/outputs/theoretical_area_ratios.csv`
- Format: csv
- Contract: Columns: theta (float, degrees), phi (float, degrees), AH_AL_combined (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/derived_parameters.json`
- `/app/outputs/theoretical_area_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### derived_parameters.json
- path: `/app/outputs/derived_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived EFG parameters and cation distribution obtained from the fit.
- schema:
  - `type`: object
  - `required`:
    - `M1`:
      - `eta`: float
      - `sign_q`: string
      - `Vzz_direction`:
        - `axis`: string
        - `direction_cosines`:
          - `cx`: float
          - `cy`: float
          - `cz`: float
      - `Vxx_direction`:
        - `axis`: string
        - `direction_cosines`:
          - `cx`: float
          - `cy`: float
          - `cz`: float
      - `Vyy_direction`:
        - `axis`: string
        - `direction_cosines`:
          - `cx`: float
          - `cy`: float
          - `cz`: float
    - `M2`:
      - `eta`: float
      - `sign_q`: string
      - `Vzz_direction`:
        - `axis`: string
        - `direction_cosines`:
          - `cx`: float
          - `cy`: float
          - `cz`: float
      - `Vxx_direction`:
        - `axis`: string
        - `direction_cosines`:
          - `cx`: float
          - `cy`: float
          - `cz`: float
      - `Vyy_direction`:
        - `axis`: string
        - `direction_cosines`:
          - `cx`: float
          - `cy`: float
          - `cz`: float
    - `site_distribution`:
      - `M1_fraction`: float
      - `M2_fraction`: float
    - `total_Fe_per_formula`: float
    - `Fe_per_site`:
      - `M1`: float
      - `M2`: float

### theoretical_area_ratios.csv
- path: `/app/outputs/theoretical_area_ratios.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Theoretical Mössbauer absorption area ratios for the 17 experimental orientations.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `phi`, `AH_AL_combined`
  - `items`:
    - `theta`: float
    - `phi`: float
    - `AH_AL_combined`: float

Notes: The experimental A_H/A_L values and the 17 (Θ, Φ) orientations are provided in the task instructions. The crystal structure should be approximated using the forsterite coordinates from the Crystallography Open Database, scaled to the paper's unit cell dimensions (a=4.78 Å, b=10.22 Å, c=5.96 Å).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "derived_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "M1": {
            "eta": "float",
            "sign_q": "string",
            "Vzz_direction": {
              "axis": "string",
              "direction_cosines": {
                "cx": "float",
                "cy": "float",
                "cz": "float"
              }
            },
            "Vxx_direction": {
              "axis": "string",
              "direction_cosines": {
                "cx": "float",
                "cy": "float",
                "cz": "float"
              }
            },
            "Vyy_direction": {
              "axis": "string",
              "direction_cosines": {
                "cx": "float",
                "cy": "float",
                "cz": "float"
              }
            }
          },
          "M2": {
            "eta": "float",
            "sign_q": "string",
            "Vzz_direction": {
              "axis": "string",
              "direction_cosines": {
                "cx": "float",
                "cy": "float",
                "cz": "float"
              }
            },
            "Vxx_direction": {
              "axis": "string",
              "direction_cosines": {
                "cx": "float",
                "cy": "float",
                "cz": "float"
              }
            },
            "Vyy_direction": {
              "axis": "string",
              "direction_cosines": {
                "cx": "float",
                "cy": "float",
                "cz": "float"
              }
            }
          },
          "site_distribution": {
            "M1_fraction": "float",
            "M2_fraction": "float"
          },
          "total_Fe_per_formula": "float",
          "Fe_per_site": {
            "M1": "float",
            "M2": "float"
          }
        }
      },
      "description": "Derived EFG parameters and cation distribution obtained from the fit."
    },
    {
      "file": "theoretical_area_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "phi",
          "AH_AL_combined"
        ],
        "items": {
          "theta": "float",
          "phi": "float",
          "AH_AL_combined": "float"
        }
      },
      "description": "Theoretical Mössbauer absorption area ratios for the 17 experimental orientations."
    }
  ],
  "notes": "The experimental A_H/A_L values and the 17 (Θ, Φ) orientations are provided in the task instructions. The crystal structure should be approximated using the forsterite coordinates from the Crystallography Open Database, scaled to the paper's unit cell dimensions (a=4.78 Å, b=10.22 Å, c=5.96 Å)."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that checks both output files.
- For `derived_parameters.json`, the verifier will compare your reported η values, the sign of q, and the direction cosines of the principal axes against reference values permitted by the crystal symmetry. The site occupation fractions will also be compared. Symmetry-equivalent representations are accepted.
- For `theoretical_area_ratios.csv`, the verifier will compute the overall deviation (e.g., root-mean-square difference) between your theoretical ratios and the true experimental ratios. A close match will earn a higher score.

The final reward is a weighted combination of the two artifact scores. Reporting only the paper's published numbers without a correct implementation of the underlying model will not pass, because the verifier re-derives intermediate quantities and checks the internal consistency of your submitted parameters with the calculated ratios.
