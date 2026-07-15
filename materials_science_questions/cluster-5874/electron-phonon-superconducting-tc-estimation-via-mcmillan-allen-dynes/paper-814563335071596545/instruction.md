# Phonon Softening Enhanced Superconducting Tc in 2D Geometries via Spring-Network Model

## Problem background
Superconductivity in reduced-dimensional systems is strongly influenced by finite-size effects and phonon softening, which can modify the electron-phonon coupling and shift the superconducting transition temperature (Tc). In a two-dimensional (2D) superconductor with a thickness of one coherence length, the local vibrational stiffness and the resulting electron-phonon interaction vary across the sample, especially near edges and corners, and when the film is curved into a hollow cylinder or sphere. A quantitative model that captures these effects is needed to understand how much the onset temperature can increase relative to the bulk value under different geometries. This task asks you to compute the Tc enhancement ratios for a flat rectangular sheet, a hollow sphere, and a hollow cylinder, as well as the broadening of the specific-heat anomaly caused by edge effects.

## Approach
The method discretizes the superconductor into a grid of coherence volumes connected by classical springs with unit coupling, representing collective lattice vibrations. For a flat 800×800 grid, the effective spring constant at each point is computed from series/parallel rules and compared to a 3D reference block (800×800×400) to obtain a stiffness ratio R(x,y) that quantifies phonon softening. This ratio is then linked to the electron-phonon coupling enhancement via (R)^0.25, and the local Tc ratio follows from BCS gap proportionality. Curved geometries (hollow sphere and cylinder) reuse the same spring-network logic, but with spring components restricted to tangential directions and with the ionic charge number corrected for Coulomb potential differences between curved and flat surfaces. From the distribution of local Tc ratios on the flat sheet, the specific heat anomaly is constructed as a sum over grid points, and the temperature at which the anomaly deviates from the bulk gives an onset broadening ratio.

## Reproduction target
Produce a single JSON file, results.json, that contains the following computed ratios (all relative to bulk): the average Tc ratio for the entire flat 800×800 film, for its four edges, and for its four corners; the average Tc ratio for a hollow sphere (radius 127, thickness 1) and for a hollow cylinder (length 800, radius 127, thickness 1); and the specific-heat onset temperature ratio due to edge-effect broadening on the flat film.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute flat sheet stiffness ratio R(x,y)
- Role: process
- Action: Implement a classical spring network on an 800×800 grid with unit spring constants and nearest-neighbour connectivity. Compute the effective spring constant at each grid point using series/parallel rules. Also compute the 3D reference stiffness on an 800×800×400 grid. Then calculate the local stiffness ratio R(x,y) = k_3D/k_2D.
- Evidence: none

### Step 2: Compute local Tc ratio map for flat sheet
- Role: process
- Action: From the R(x,y) map compute the electron–phonon coupling enhancement ratio as (R)^0.25, then map to local Tc ratio using BCS gap proportionality (Tc/Tc_bulk = He-ph/He-ph_bulk).
- Evidence: none

### Step 3: Compute curvature correction for hollow sphere
- Role: process
- Action: Compute the Coulomb potential energy of an electron at a distance L/4 from the surface for a hollow sphere (radius 127, thickness 1) and a flat surface, using three nearest-neighbour grid points. Obtain the corrected ionic charge number Z_corrected = Z * (U_sphere/U_flat).
- Evidence: none

### Step 4: Compute hollow sphere average Tc ratio
- Role: process
- Action: Apply the spring-network model to the spherical surface using tangential components only and the corrected Z. Compute effective spring constants, electron–phonon coupling, and then the average Tc enhancement ratio for the entire hollow sphere.
- Evidence: none

### Step 5: Compute curvature correction for hollow cylinder
- Role: process
- Action: Compute the Coulomb potential energy for a hollow cylinder (length 800, radius 127, thickness 1) and compare with the flat case to obtain Z_corrected = Z * (U_cylinder/U_flat).
- Evidence: none

### Step 6: Compute hollow cylinder average Tc ratio
- Role: process
- Action: Apply the spring-network model to the cylindrical surface, treating axial and angular components separately with the cylinder's Z_corrected. Compute effective spring constants, electron–phonon coupling, and the average Tc enhancement ratio for the cylinder.
- Evidence: none

### Step 7: Compute specific heat broadening and onset ratio
- Role: process
- Action: Using the Tc ratio distribution from the flat sheet, compute the specific heat anomaly C(T) = Σ A * T^{-1.5} * exp(-3.52 * Tc_point / T) over all grid points. Determine the onset temperature ratio (T_onset / T_c^bulk) where the anomaly begins to deviate from the bulk onset.
- Evidence: none

### Step 8: Compile all Tc enhancement and onset ratios
- Role: scored (load-bearing)
- Action: Compile all computed ratios into a JSON file: average Tc ratios for the flat sheet (entire film, edges, corners), hollow sphere, hollow cylinder, and the specific heat onset ratio.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"flat_sheet": {"entire_film_ratio": "number", "edges_ratio": "number", "corners_ratio": "number"}, "hollow_sphere": {"ratio": "number"}, "hollow_cylinder": {"ratio": "number"}, "specific_heat_onset_ratio": "number"}
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
- description: JSON file containing Tc enhancement ratios for the flat sheet (entire film, edges, corners), hollow sphere, hollow cylinder, and the specific heat onset broadening ratio.
- schema:
  - `type`: object
  - `required`: `flat_sheet`, `hollow_sphere`, `hollow_cylinder`, `specific_heat_onset_ratio`
  - `properties`:
    - `flat_sheet`:
      - `type`: object
      - `required`: `entire_film_ratio`, `edges_ratio`, `corners_ratio`
      - `properties`:
        - `entire_film_ratio`:
          - `type`: number
        - `edges_ratio`:
          - `type`: number
        - `corners_ratio`:
          - `type`: number
    - `hollow_sphere`:
      - `type`: object
      - `required`: `ratio`
      - `properties`:
        - `ratio`:
          - `type`: number
    - `hollow_cylinder`:
      - `type`: object
      - `required`: `ratio`
      - `properties`:
        - `ratio`:
          - `type`: number
    - `specific_heat_onset_ratio`:
      - `type`: number

Notes: All ratios are relative to bulk Tc. The checker compares each ratio to the paper's reported values with a tolerance that accounts for discretisation sensitivity (e.g., 10% for aggregate ratios, 20% for corner ratio).

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
        "required": [
          "flat_sheet",
          "hollow_sphere",
          "hollow_cylinder",
          "specific_heat_onset_ratio"
        ],
        "properties": {
          "flat_sheet": {
            "type": "object",
            "required": [
              "entire_film_ratio",
              "edges_ratio",
              "corners_ratio"
            ],
            "properties": {
              "entire_film_ratio": {
                "type": "number"
              },
              "edges_ratio": {
                "type": "number"
              },
              "corners_ratio": {
                "type": "number"
              }
            }
          },
          "hollow_sphere": {
            "type": "object",
            "required": [
              "ratio"
            ],
            "properties": {
              "ratio": {
                "type": "number"
              }
            }
          },
          "hollow_cylinder": {
            "type": "object",
            "required": [
              "ratio"
            ],
            "properties": {
              "ratio": {
                "type": "number"
              }
            }
          },
          "specific_heat_onset_ratio": {
            "type": "number"
          }
        }
      },
      "description": "JSON file containing Tc enhancement ratios for the flat sheet (entire film, edges, corners), hollow sphere, hollow cylinder, and the specific heat onset broadening ratio."
    }
  ],
  "notes": "All ratios are relative to bulk Tc. The checker compares each ratio to the paper's reported values with a tolerance that accounts for discretisation sensitivity (e.g., 10% for aggregate ratios, 20% for corner ratio)."
}
```

## How you are scored
A hidden verifier will read your results.json and compare each numeric ratio against an expected value using an exact-match policy with a relative tolerance that accounts for discretisation and implementation differences. Meeting the tolerance on a ratio earns full credit for that component; deviations beyond the tolerance reduce the score. The final reward is a weighted combination of all scored components.
