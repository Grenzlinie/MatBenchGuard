# Lattice thermal conductivity model incorporating optical phonon decay into acoustic phonons

## Problem background
Accurate prediction of lattice thermal conductivity in semiconductors is essential for thermal management in electronics. The standard modified Callaway theory (MCT) describes heat conduction by acoustic phonons using scattering rates from boundaries, point defects, normal three-phonon, and umklapp processes. However, for materials such as AlN and Ge, the standard MCT often produces significant deviations from experimental data near the thermal conductivity maximum, suggesting that a missing phonon mechanism may be important. One proposed mechanism is the anharmonic decay of optical phonons into acoustic phonons, which can act as a generation channel that modifies the acoustic phonon population and thus affects heat transport. In this task, you will implement a thermal conductivity model that incorporates this optical‑phonon decay process and compute the resulting k(T) curves for several conditions; the agreement with experimental measurements will be evaluated.

## Approach
The modeling framework is the relaxation‑time approximation of the Callaway theory. You will implement the standard MCT, where the total phonon scattering rate is the sum of boundary scattering (constant rate), point‑defect scattering (∝ ω⁴), normal three‑phonon scattering (different power‑law forms for longitudinal and transverse branches), and umklapp scattering (containing an exponential Debye‑temperature factor). Thermal conductivity is obtained by the usual integration over phonon frequencies and branches.

To that baseline you will add a generation term that originates from the anharmonic decay of optical phonons into two acoustic phonons (the Klemens channel). The generation rate is derived from cubic anharmonicity; it depends on the optical‑phonon velocity, the Grüneisen parameters, and the temperature, and it partially counteracts the resistive scattering processes. The effect is applied only in the frequency window where optical‑phonon decay is energetically allowed, as indicated by the phonon dispersion of the material.

You will fit the adjustable parameters—the mass‑fluctuation scattering parameter Γ for AlN and the generation strength coefficients B^{L,T}—to the provided experimental thermal‑conductivity datasets for AlN (two crystal directions) and for isotopically purified Ge. After obtaining the best‑fit parameters, you will compute the final k(T) curves for the specified conditions and write them to a JSON file. A baseline standard MCT fit is also required to provide a reference for the magnitude of the improvement brought by the generation term.

## Reproduction target
Produce a JSON file `/app/outputs/thermal_conductivity.json` that contains the computed lattice thermal conductivity k as a function of temperature for the following seven conditions:
- AlN along the ΓA direction with mass‑fluctuation parameters Γ = 0.03, 0.13, and 0.42.
- AlN along the ΓK direction with the same three Γ values.
- Isotopically purified germanium (Ge).
For each condition the output must be an array of {T, k} objects, where T is in kelvin and k in W m⁻¹ K⁻¹. The temperature points should correspond to those in the bundled experimental data files so that the computed curves can be compared with measurements. In addition, you must provide evidence of the fitting process (log and parameter files) for both the baseline MCT and the proposed model, as detailed in the workflow steps below. Your curves will be checked against hidden reference experimental data to evaluate the accuracy of the implemented model.

## Assets

- Experimental thermal conductivity data for AlN (digitized from Figure 1)
- Experimental thermal conductivity data for isotopically purified Ge
- Davydov et al., PRB 58, 12899 (1998) – AlN phonon dispersion and Debye temperatures: 10.1103/PhysRevB.58.12899
- Kazan et al., Diamond Relat. Mater. 15, 1525 (2006) – AlN acoustic velocities: 10.1016/j.diamond.2005.10.017
- Perlin et al., PRB 47, 2874 (1993) – Grüneisen parameters of AlN: 10.1103/PhysRevB.47.2874
- Morelli et al., PRB 66, 195304 (2002) – Ge material parameters: 10.1103/PhysRevB.66.195304

## Workflow steps

### Step 1: Standard MCT baseline fitting to AlN data
- Role: process
- Action: Implement the standard modified Callaway model (boundary, impurity, normal, umklapp scattering rates) and fit the mass-fluctuation parameter Γ to the provided experimental AlN thermal conductivity data by minimizing error. This step establishes the baseline and demonstrates the systematic underestimation near the peak.
- Evidence: `/app/outputs/standard_mct_fit_log.txt`

### Step 2: Proposed model fitting to AlN data
- Role: process
- Action: Implement the proposed model that adds the anharmonic optical-phonon decay into two acoustic phonons (Klemens channel) and the generation term. Fit the parameters B^{L,T} (and possibly revise Γ) to the experimental AlN data to obtain the best-fit curves.
- Evidence: `/app/outputs/aln_proposed_fit_params.json`

### Step 3: Proposed model fitting to Ge data
- Role: process
- Action: Using the same proposed model, fit the parameters B^{L,T} to the provided experimental Ge thermal conductivity data (with the analytically known isotopic Γ for Ge).
- Evidence: `/app/outputs/ge_proposed_fit_params.json`

### Step 4: Compute and output final thermal conductivity curves
- Role: scored (load-bearing)
- Action: Using the fitted parameters from steps 2 and 3, compute k(T) at the experimental temperature points for the following conditions: AlN along ΓA and ΓK directions with mass-fluctuation parameters Γ = 0.03, 0.13, 0.42; isotopically purified Ge. Write the results to /app/outputs/thermal_conductivity.json.
- Output file: `/app/outputs/thermal_conductivity.json`
- Format: json
- Contract: JSON object with keys for each sample/direction: 'AlN_GammaA_Gamma0.03', 'AlN_GammaA_Gamma0.13', 'AlN_GammaA_Gamma0.42', 'AlN_GammaK_Gamma0.03', 'AlN_GammaK_Gamma0.13', 'AlN_GammaK_Gamma0.42', 'Ge_isotropic'. Each value is an array of {T: float, k: float} objects.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.json
- path: `/app/outputs/thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed lattice thermal conductivity curves incorporating optical phonon decay. The checker recomputes the mean absolute error between the submitted curves and hidden gold experimental data to verify model accuracy.
- schema:
  - `type`: object
  - `required`: `AlN_GammaA_Gamma0.03`, `AlN_GammaA_Gamma0.13`, `AlN_GammaA_Gamma0.42`, `AlN_GammaK_Gamma0.03`, `AlN_GammaK_Gamma0.13`, `AlN_GammaK_Gamma0.42`, `Ge_isotropic`
  - `additionalProperties`: False
  - `properties`:
    - `AlN_GammaA_Gamma0.03`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`
    - `AlN_GammaA_Gamma0.13`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`
    - `AlN_GammaA_Gamma0.42`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`
    - `AlN_GammaK_Gamma0.03`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`
    - `AlN_GammaK_Gamma0.13`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`
    - `AlN_GammaK_Gamma0.42`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`
    - `Ge_isotropic`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
          - `k`:
            - `type`: number
        - `required`: `T`, `k`

Notes: The experimental data to which the curves are compared are bundled in the task as hidden gold; the agent must not access them directly. All material parameters needed for the model are available from the listed public references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "AlN_GammaA_Gamma0.03",
          "AlN_GammaA_Gamma0.13",
          "AlN_GammaA_Gamma0.42",
          "AlN_GammaK_Gamma0.03",
          "AlN_GammaK_Gamma0.13",
          "AlN_GammaK_Gamma0.42",
          "Ge_isotropic"
        ],
        "additionalProperties": false,
        "properties": {
          "AlN_GammaA_Gamma0.03": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          },
          "AlN_GammaA_Gamma0.13": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          },
          "AlN_GammaA_Gamma0.42": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          },
          "AlN_GammaK_Gamma0.03": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          },
          "AlN_GammaK_Gamma0.13": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          },
          "AlN_GammaK_Gamma0.42": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          },
          "Ge_isotropic": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number"
                },
                "k": {
                  "type": "number"
                }
              },
              "required": [
                "T",
                "k"
              ]
            }
          }
        }
      },
      "description": "Computed lattice thermal conductivity curves incorporating optical phonon decay. The checker recomputes the mean absolute error between the submitted curves and hidden gold experimental data to verify model accuracy."
    }
  ],
  "notes": "The experimental data to which the curves are compared are bundled in the task as hidden gold; the agent must not access them directly. All material parameters needed for the model are available from the listed public references."
}
```

## How you are scored
An automated verifier evaluates your solution by inspecting the output files and assigning a final reward between 0 and 1.

- **Scored artifact (`thermal_conductivity.json`):** The verifier checks that the file is valid JSON, contains all seven required condition keys, and that each array holds well‑formed {T, k} objects. It then recomputes the mean absolute error between your submitted k(T) curves and hidden gold experimental data points (digitized from published measurements). Your reward for this stage is based on the average MAE across all conditions: the closer your curves are to the measurements, the higher the score.
- **Process steps:** The existence of `standard_mct_fit_log.txt`, `aln_proposed_fit_params.json`, and `ge_proposed_fit_params.json` is verified to confirm that the fitting pipeline was executed. These files are not directly scored for accuracy but are required to pass structural checks.
- The stages are weighted to reflect their importance, with the final thermal conductivity curves carrying the bulk of the reward.

Simply reporting expected numbers without producing the underlying computations will not satisfy the verifier.
