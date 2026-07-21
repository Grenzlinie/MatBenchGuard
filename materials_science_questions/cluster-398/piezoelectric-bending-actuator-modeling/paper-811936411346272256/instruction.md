# Contact behavior of functionally graded piezoelectric layered half-plane under a rigid punch

## Problem background
Functionally graded piezoelectric materials (FGPMs) are inhomogeneous composites with graded electro-elastic properties that can improve the resistance of smart structures to contact damage. This task reproduces the two-dimensional frictionless contact problem of an FGPM layer perfectly bonded to a homogeneous piezoelectric half-plane under the action of a rigid conducting punch (flat or cylindrical). The FGPM layer's elastic, piezoelectric, and dielectric constants vary exponentially in the thickness direction. Under combined mechanical line load and electric charge, the contact pressure, electric charge distribution, and related intensity factors (for flat punch) or contact half-width and relative indentation (for cylindrical punch) need to be determined for different material gradient indices and punch geometries.

## Approach
The electro-mechanical contact problem is treated as a mixed boundary-value problem. Fourier integral transform is applied to the governing equations of the FGPM layer and homogeneous half-plane, leading to a characteristic polynomial whose roots give the modal exponents. Transfer matrices relate the transformed displacements, electric potential, stresses, and electric displacements across the layer. The surface response at the top of the layer is expressed in terms of the unknown contact pressure and electric charge, yielding coupled Cauchy singular integral equations after applying the boundary and interface conditions. The Fredholm kernels are regularized using the asymptotic behaviour of the response matrix. The integral equations are discretized via collocation methods. For the flat punch, the unknowns are decomposed into singular parts, and the resulting linear system includes the global equilibrium conditions. For the cylindrical punch, the smooth contact pressure is expressed with a square-root edge behaviour, and the electric charge is split into a smooth part and a singular part; the contact half-width is determined as part of the solution by enforcing the consistency condition. The intensity factors, relative indentation depth, and relative electric potential are computed from the solved surface distributions. The entire numerical pipeline uses the PZT-4 material constants at the interface and recomputes the response for five values of the gradient index βh covering both negative and positive gradients.

## Reproduction target
Compute the following for an FGPM layer of thickness h = 0.01 m perfectly bonded to a piezoelectric PZT-4 half-plane, using the material constants of PZT-4 at the interface.

1. **Flat punch contact** (half-width a = 0.01 m, normal line force P = 1 kN/m, applied electric charge Q = 1×10⁻⁶ C/m). For each gradient index βh ∈ {−0.8, −0.4, 0, 0.4, 0.8}, compute:
   - The surface contact pressure distribution p(x) and surface electric charge distribution q(x) at the collocation points.
   - The normalized stress intensity factor K_σ / (σ_a √a) and normalized electric displacement intensity factor K_D / (σ_b √a), where σ_a = P/a and σ_b = Q/a.
   Output as specified in Step 4.

2. **Cylindrical punch contact** (radius R = 0.08 m, same loads P and Q). For the same five gradient indices, compute:
   - The surface contact pressure p(x) and electric charge q(x) (split into q1 and q2 components) at the collocation points.
   - The converged contact half-width a.
   Output as specified in Step 5.

3. **Relative indentation and electric potential** from the cylindrical punch solution. Using the obtained pressure and charge distributions, evaluate the relative vertical displacement Δδ₀ and relative electric potential Δφ₀ at points x₀ = 0.0 m, 0.005 m, 0.010 m, relative to the reference point at x = 0.02 m. Aggregate the flat punch intensity factors and the cylindrical indentation/potential in a single file as specified in Step 6.

## Assets

- numpy: numpy
- scipy: scipy
- PZT-4 material constants

## Workflow steps

### Step 1: Define material constants of PZT-4
- Role: process
- Action: Hardcode the electro-mechanical constants c_ij0, e_ij0, ε_ij0 for PZT-4 from the paper's Table 1 into the solver code.
- Evidence: none

### Step 2: Compute fundamental solution matrix and asymptotic constants
- Role: process
- Action: Construct the governing equations in Fourier domain. Derive the characteristic equation (bi-cubic) for modal exponents n_j. For each required transform variable s, find the six roots, compute modal ratios a_j, b_j, assemble transfer matrices [T1], [T2], [V], [Vn], and extract asymptotic limits f^∞_ij of the surface response matrix F(s,h) as s→∞.
- Evidence: `/app/outputs/asymptotic_constants.txt`

### Step 3: Compute integral kernel functions
- Role: process
- Action: For a given gradient index βh and layer thickness h, evaluate the regularized Fredholm kernels K_1 through K_6 on the collocation grids by integrating the difference between the full transformed matrix F(s,h) and its asymptotic form over the transform variable s.
- Evidence: `/app/outputs/kernel_tables.npy`

### Step 4: Solve flat punch contact and compute intensity factors
- Role: scored (load-bearing)
- Action: For each βh ∈ [-0.8, -0.4, 0, 0.4, 0.8], set up the discretized singular integral equations for a conducting rigid flat punch with half-width a=0.01 m, normal line force P=1 kN/m, and electric charge Q=1e-6 C/m. Solve the collocation linear system to obtain contact pressure p(η_i) and electric charge distribution q(η_i) at N collocation points. Extract normalized stress intensity factor K_σ/(σ_a√a) and electric displacement intensity factor K_D/(σ_b√a). Write all results.
- Output file: `/app/outputs/flat_punch_results.json`
- Format: json
- Contract: JSON object with keys 'beta_h_values' (array of 5 floats) and 'results' (array of 5 objects, each containing 'beta_h', 'p_points' (list of {x (m), p (Pa)}), 'q_points' (list of {x (m), q (C/m^2)}), 'K_sigma_normalized', 'K_D_normalized').
- Scoring: scored by hidden verifier

### Step 5: Solve cylindrical punch contact and compute contact half-width
- Role: scored (load-bearing)
- Action: For the same set of βh values, solve the cylindrical punch problem with radius R=0.08 m, same loads. Treat the contact half-width a as an unknown determined by consistency. Use the appropriate collocation scheme to obtain smooth contact pressure p(η_i), electric charge distribution q(η_i) (split into q1 and q2), and the converged half-width a. Write the results.
- Output file: `/app/outputs/cylindrical_punch_results.json`
- Format: json
- Contract: JSON object with keys 'beta_h_values' (array of 5 floats) and 'results' (array of 5 objects, each containing 'beta_h', 'p_points' (list of {x (m), p (Pa)}), 'q_points' (list of {x (m), q (C/m^2)}), 'a_half_width' (meters)).
- Scoring: scored by hidden verifier

### Step 6: Compute relative indentation depth and electric potential
- Role: scored
- Action: Using the solved surface traction distributions from the cylindrical punch step, evaluate the surface displacement integrals and logarithmic singular terms, and compute the relative vertical displacement Δδ₀ and relative electric potential Δφ₀ at points x₀ = 0.0, 0.005, 0.01 m relative to a reference point at x = 0.02 m. Also aggregate the flat punch intensity factors already computed.
- Output file: `/app/outputs/intensity_and_indentation.json`
- Format: json
- Contract: JSON object with keys 'flat_intensity' (list of {beta_h, K_sigma_normalized, K_D_normalized}) and 'cylindrical_indentation' (list of {beta_h, x0 (m), delta0_m (m), phi0_V (V)} for x0 = 0.0, 0.005, 0.01 m).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/flat_punch_results.json`
- `/app/outputs/cylindrical_punch_results.json`
- `/app/outputs/intensity_and_indentation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### flat_punch_results.json
- path: `/app/outputs/flat_punch_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contact pressure distribution, electric charge distribution, stress intensity factor and electric displacement intensity factor for a flat punch on the FGPM layered half-plane for various gradient indices βh.
- schema:
  - `type`: object
  - `required`: `beta_h_values`, `results`
  - `properties`:
    - `beta_h_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `results`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `beta_h`, `p_points`, `q_points`, `K_sigma_normalized`, `K_D_normalized`
        - `properties`:
          - `beta_h`:
            - `type`: number
          - `p_points`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `x`, `p`
              - `properties`:
                - `x`:
                  - `type`: number
                  - `unit`: m
                - `p`:
                  - `type`: number
                  - `unit`: Pa
          - `q_points`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `x`, `q`
              - `properties`:
                - `x`:
                  - `type`: number
                  - `unit`: m
                - `q`:
                  - `type`: number
                  - `unit`: C/m^2
          - `K_sigma_normalized`:
            - `type`: number
          - `K_D_normalized`:
            - `type`: number

### cylindrical_punch_results.json
- path: `/app/outputs/cylindrical_punch_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contact pressure distribution, electric charge distribution and contact half-width for a cylindrical punch on the FGPM layered half-plane for various gradient indices βh.
- schema:
  - `type`: object
  - `required`: `beta_h_values`, `results`
  - `properties`:
    - `beta_h_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `results`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `beta_h`, `p_points`, `q_points`, `a_half_width`
        - `properties`:
          - `beta_h`:
            - `type`: number
          - `p_points`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `x`, `p`
              - `properties`:
                - `x`:
                  - `type`: number
                  - `unit`: m
                - `p`:
                  - `type`: number
                  - `unit`: Pa
          - `q_points`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `x`, `q`
              - `properties`:
                - `x`:
                  - `type`: number
                  - `unit`: m
                - `q`:
                  - `type`: number
                  - `unit`: C/m^2
          - `a_half_width`:
            - `type`: number
            - `unit`: m

### intensity_and_indentation.json
- path: `/app/outputs/intensity_and_indentation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated flat punch intensity factors and cylindrical punch relative indentation depth Δδ₀ and relative electric potential Δφ₀ at x₀ = 0.0, 0.005, 0.01 m.
- schema:
  - `type`: object
  - `required`: `flat_intensity`, `cylindrical_indentation`
  - `properties`:
    - `flat_intensity`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `beta_h`, `K_sigma_normalized`, `K_D_normalized`
        - `properties`:
          - `beta_h`:
            - `type`: number
          - `K_sigma_normalized`:
            - `type`: number
          - `K_D_normalized`:
            - `type`: number
    - `cylindrical_indentation`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `beta_h`, `x0`, `delta0_m`, `phi0_V`
        - `properties`:
          - `beta_h`:
            - `type`: number
          - `x0`:
            - `type`: number
            - `unit`: m
          - `delta0_m`:
            - `type`: number
            - `unit`: m
          - `phi0_V`:
            - `type`: number
            - `unit`: V

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "flat_punch_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "beta_h_values",
          "results"
        ],
        "properties": {
          "beta_h_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "beta_h",
                "p_points",
                "q_points",
                "K_sigma_normalized",
                "K_D_normalized"
              ],
              "properties": {
                "beta_h": {
                  "type": "number"
                },
                "p_points": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "x",
                      "p"
                    ],
                    "properties": {
                      "x": {
                        "type": "number",
                        "unit": "m"
                      },
                      "p": {
                        "type": "number",
                        "unit": "Pa"
                      }
                    }
                  }
                },
                "q_points": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "x",
                      "q"
                    ],
                    "properties": {
                      "x": {
                        "type": "number",
                        "unit": "m"
                      },
                      "q": {
                        "type": "number",
                        "unit": "C/m^2"
                      }
                    }
                  }
                },
                "K_sigma_normalized": {
                  "type": "number"
                },
                "K_D_normalized": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Contact pressure distribution, electric charge distribution, stress intensity factor and electric displacement intensity factor for a flat punch on the FGPM layered half-plane for various gradient indices βh."
    },
    {
      "file": "cylindrical_punch_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "beta_h_values",
          "results"
        ],
        "properties": {
          "beta_h_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "beta_h",
                "p_points",
                "q_points",
                "a_half_width"
              ],
              "properties": {
                "beta_h": {
                  "type": "number"
                },
                "p_points": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "x",
                      "p"
                    ],
                    "properties": {
                      "x": {
                        "type": "number",
                        "unit": "m"
                      },
                      "p": {
                        "type": "number",
                        "unit": "Pa"
                      }
                    }
                  }
                },
                "q_points": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "x",
                      "q"
                    ],
                    "properties": {
                      "x": {
                        "type": "number",
                        "unit": "m"
                      },
                      "q": {
                        "type": "number",
                        "unit": "C/m^2"
                      }
                    }
                  }
                },
                "a_half_width": {
                  "type": "number",
                  "unit": "m"
                }
              }
            }
          }
        }
      },
      "description": "Contact pressure distribution, electric charge distribution and contact half-width for a cylindrical punch on the FGPM layered half-plane for various gradient indices βh."
    },
    {
      "file": "intensity_and_indentation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "flat_intensity",
          "cylindrical_indentation"
        ],
        "properties": {
          "flat_intensity": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "beta_h",
                "K_sigma_normalized",
                "K_D_normalized"
              ],
              "properties": {
                "beta_h": {
                  "type": "number"
                },
                "K_sigma_normalized": {
                  "type": "number"
                },
                "K_D_normalized": {
                  "type": "number"
                }
              }
            }
          },
          "cylindrical_indentation": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "beta_h",
                "x0",
                "delta0_m",
                "phi0_V"
              ],
              "properties": {
                "beta_h": {
                  "type": "number"
                },
                "x0": {
                  "type": "number",
                  "unit": "m"
                },
                "delta0_m": {
                  "type": "number",
                  "unit": "m"
                },
                "phi0_V": {
                  "type": "number",
                  "unit": "V"
                }
              }
            }
          }
        }
      },
      "description": "Aggregated flat punch intensity factors and cylindrical punch relative indentation depth Δδ₀ and relative electric potential Δφ₀ at x₀ = 0.0, 0.005, 0.01 m."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted artifacts will be checked by a hidden verifier. The verifier independently evaluates each scored output file. It compares your computed contact pressure and electric charge distributions, intensity factors, contact half-width, and relative indentation/potential against a hidden reference that encodes the correct electro-mechanical response under the specified conditions. The scoring accounts for legitimate numerical differences introduced by different implementations of the Fourier-transform method, root-finding, integration, and collocation solver, using appropriate tolerances. Each artifact contributes a fraction of the total reward; they are combined into a single final score between 0 and 1. Producing the correct physical response through a faithful execution of the described method is essential; reporting numbers without the underlying computation will not satisfy the verifier.
