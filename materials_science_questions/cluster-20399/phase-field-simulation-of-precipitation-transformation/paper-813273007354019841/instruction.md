# Sequential multiscale simulation of Cu precipitate coarsening in α-Fe using KMC and grand-potential phase-field method

## Problem background
Cu precipitation in α-Fe is used to strengthen the material, but at elevated temperatures (above 700 °C) the precipitates undergo coarsening, which degrades mechanical properties. Accurately predicting the coarsening kinetics requires bridging atomistic nucleation and growth, interface energetics, and continuum Ostwald ripening over length scales from nanometers to tens of nanometers. This reproduction package implements a sequential multiscale simulation framework that connects these scales and yields quantitative information on coarsening rates and precipitate size distributions.

## Approach
The workflow begins with vacancy-mediated kinetic Monte Carlo (KMC) simulations on a rigid bcc lattice to capture early-stage clustering and produce realistic spatial arrangements of Cu-rich precipitates. The {110} interface energy between the Fe matrix and Cu precipitates is obtained from a broken-bond model using the same pair interaction parameters as in KMC. An optional molecular dynamics relaxation step with a published EAM potential checks whether precipitates remain coherent in the bcc lattice for the sizes that appear in the later coarsening stages; if coherency holds, elastic strain fields are neglected in the subsequent continuum model. These results are then fed into a grand-potential phase-field model (PFM) that is thermodynamically calibrated with a polynomial fit to CALPHAD free energies. After validating the model against the Gibbs-Thomson effect, coarsening simulations are run for Fe-5 at.% Cu and Fe-10 at.% Cu at 1100 K, starting from the KMC-generated precipitate configurations. From the evolving microstructure, the mean precipitate radius, particle number, and particle size distributions are extracted, and the Lifshitz–Slyozov–Wagner (LSW) coarsening rate constant is determined by fitting the cube of the mean radius versus time.

## Reproduction target
Carry out the full sequential multiscale pipeline and produce a single scored artifact, `/app/outputs/simulation_results.json`, containing:

- **Gibbs-Thomson validation**: for a single spherical Fe precipitate of several different radii, report the equilibrium composition shift Δcᵖ on the precipitate side and the corresponding curvature (1 / radius).
- **Coarsening kinetics for 5 at.% Cu and 10 at.% Cu**: time series of mean precipitate radius (nm) and number of particles at 1100 K.
- **Particle size distributions (PSDs)**: binned counts versus radius at t = 0 s and t = 175 s for each composition.
- **Fitted LSW coarsening rate constants K** (nm³/s) for the 5 at.% Cu and 10 at.% Cu systems, obtained by a cubic fit to the mean radius³ vs. time data.

The results must be written according to the output contract: a JSON object with keys `gibbs_thomson`, `coarsening_5at`, `coarsening_10at`, `K_5at`, `K_10at`, `PSD_5at_start`, `PSD_5at_end`, `PSD_10at_start`, and `PSD_10at_end`.

## Assets

- Bonny EAM potential for Fe-Cu: https://www.ctcms.nist.gov/potentials/Fe-Cu.html
- KMC pair interaction parameters
- Molecular dynamics engine supporting EAM

## Workflow steps

### Step 1: KMC simulation and cluster extraction
- Role: process
- Action: Run vacancy-mediated kinetic Monte Carlo simulations for Fe-5 at.% Cu and Fe-10 at.% Cu at 973 K on a 128×128×128 bcc lattice using the published first- and second-nearest neighbour pair interaction parameters. Extract the final atomic configurations, identify Cu precipitates, and output their positions and radii.
- Evidence: `/app/outputs/kmc_clusters.json`

### Step 2: Break-bond model interface energy calculation
- Role: process
- Action: Using the same pair interaction parameters as in the KMC step, compute the {110} Fe-Cu interface energy via the broken-bond model: first compute the energy change per interface atom for the [110] orientation, then divide by the orientation-dependent area per atom to obtain the interface energy γ in J/m².
- Evidence: `/app/outputs/interface_energy.txt`

### Step 3: Molecular dynamics coherency assessment (optional)
- Role: process
- Action: Perform molecular dynamics relaxation of Cu precipitates of various radii (≈0.5–4 nm) using the Bonny EAM potential for Fe-Cu. Analyse local coordination numbers to determine whether precipitates remain coherent bcc for the sizes present in the KMC end states. This step justifies the omission of elastic strain fields in the PFM; it can be omitted if the solver explicitly states that the paper found precipitates coherent for these sizes and the PFM will neglect elastic strains.
- Evidence: `/app/outputs/md_coherency.json`

### Step 4: Grand-potential phase-field model calibration and setup
- Role: process
- Action: Calibrate the grand-potential phase-field model for a two-phase binary Fe-Cu system using the published free-energy polynomial coefficients: A_alpha=1.71×10¹¹ J/m³, B_alpha=-3.33×10¹¹ J/m³, E_alpha=1.13×10¹¹ J/m³, A_beta=1.39×10¹¹ J/m³, B_beta=-6.43×10⁹ J/m³, E_beta=-5.04×10¹⁰ J/m³. Set the interface energy γ to the value from step_02_bbm (0.41 J/m² if consistent), diffusion coefficient D=10⁻¹⁶ m²/s, interface width ε=7.0×10⁻¹⁰ m, and grid spacing Δx=2.8665×10⁻¹⁰ m. Set up a 128³ grid with periodic boundary conditions.
- Evidence: `/app/outputs/pfm_params.json`

### Step 5: Phase-field Gibbs-Thomson validation simulations
- Role: process
- Action: Run PFM simulations of a single spherical Fe precipitate of several different radii in a 3D domain at 1100 K. For each size, record the steady-state precipitate composition shift Δc^p relative to the flat-interface equilibrium and the corresponding curvature 1/R. Output these raw data points.
- Evidence: `/app/outputs/gibbs_thomson_raw.json`

### Step 6: Phase-field coarsening simulations with KMC initial configurations
- Role: process
- Action: Starting from the KMC-derived precipitate configurations (step_01_kmc), run PFM coarsening simulations for the 5 at.% Cu and 10 at.% Cu systems at 1100 K for at least 175 s physical time. Save the time evolution of the order parameter or concentration fields sufficiently often to enable subsequent particle analysis.
- Evidence: `/app/outputs/coarsening_fields.h5`

### Step 7: Coarsening kinetics analysis and results assembly
- Role: scored (load-bearing)
- Action: From the outputs of steps 05 and 06, compute: (i) the linear relation between curvature (1/R) and Δc^p (Gibbs‑Thomson); (ii) the time evolution of mean precipitate radius and number of particles for 5 at.% and 10 at.% Cu; (iii) the particle size distributions (PSDs) at t=0 s and t=175 s for each composition; (iv) the LSW coarsening rate constants K by fitting mean radius³ vs time. Write all results to /app/outputs/simulation_results.json according to the output contract.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: JSON object with keys: gibbs_thomson (list of {curvature_1_nm, delta_cp}), coarsening_5at (list of {time_s, mean_radius_nm, num_particles}), coarsening_10at (similar), K_5at (float), K_10at (float), PSD_5at_start (list of {radius_nm, count}), PSD_5at_end (similar), PSD_10at_start (similar), PSD_10at_end (similar).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the Gibbs-Thomson validation data, coarsening kinetics time series, fitted LSW rate constants, and particle size distributions for 5 and 10 at.% Cu. The hidden checker will recompute the Gibbs-Thomson linear slope and the cubic LSW fits to extract K, and compare against reference values derived from the paper.
- schema:
  - `type`: object
  - `required`: `gibbs_thomson`, `coarsening_5at`, `coarsening_10at`, `K_5at`, `K_10at`, `PSD_5at_start`, `PSD_5at_end`, `PSD_10at_start`, `PSD_10at_end`
  - `properties`:
    - `gibbs_thomson`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `curvature_1_nm`, `delta_cp`
        - `properties`:
          - `curvature_1_nm`:
            - `type`: number
            - `unit`: 1/nm
          - `delta_cp`:
            - `type`: number
            - `unit`: dimensionless
    - `coarsening_5at`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `time_s`, `mean_radius_nm`, `num_particles`
        - `properties`:
          - `time_s`:
            - `type`: number
            - `unit`: s
          - `mean_radius_nm`:
            - `type`: number
            - `unit`: nm
          - `num_particles`:
            - `type`: integer
    - `coarsening_10at`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `time_s`, `mean_radius_nm`, `num_particles`
        - `properties`:
          - `time_s`:
            - `type`: number
            - `unit`: s
          - `mean_radius_nm`:
            - `type`: number
            - `unit`: nm
          - `num_particles`:
            - `type`: integer
    - `K_5at`:
      - `type`: number
      - `unit`: nm^3/s
    - `K_10at`:
      - `type`: number
      - `unit`: nm^3/s
    - `PSD_5at_start`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `radius_nm`, `count`
        - `properties`:
          - `radius_nm`:
            - `type`: number
            - `unit`: nm
          - `count`:
            - `type`: integer
    - `PSD_5at_end`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `radius_nm`, `count`
        - `properties`:
          - `radius_nm`:
            - `type`: number
            - `unit`: nm
          - `count`:
            - `type`: integer
    - `PSD_10at_start`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `radius_nm`, `count`
        - `properties`:
          - `radius_nm`:
            - `type`: number
            - `unit`: nm
          - `count`:
            - `type`: integer
    - `PSD_10at_end`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `radius_nm`, `count`
        - `properties`:
          - `radius_nm`:
            - `type`: number
            - `unit`: nm
          - `count`:
            - `type`: integer

Notes: The checker will recompute the Gibbs-Thomson slope via linear regression on the (curvature_1_nm, delta_cp) pairs, and the LSW rate constants K by fitting a cubic polynomial to mean_radius_nm^3 vs time_s for each composition. No tolerances or gold values are given here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gibbs_thomson",
          "coarsening_5at",
          "coarsening_10at",
          "K_5at",
          "K_10at",
          "PSD_5at_start",
          "PSD_5at_end",
          "PSD_10at_start",
          "PSD_10at_end"
        ],
        "properties": {
          "gibbs_thomson": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "curvature_1_nm",
                "delta_cp"
              ],
              "properties": {
                "curvature_1_nm": {
                  "type": "number",
                  "unit": "1/nm"
                },
                "delta_cp": {
                  "type": "number",
                  "unit": "dimensionless"
                }
              }
            }
          },
          "coarsening_5at": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "time_s",
                "mean_radius_nm",
                "num_particles"
              ],
              "properties": {
                "time_s": {
                  "type": "number",
                  "unit": "s"
                },
                "mean_radius_nm": {
                  "type": "number",
                  "unit": "nm"
                },
                "num_particles": {
                  "type": "integer"
                }
              }
            }
          },
          "coarsening_10at": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "time_s",
                "mean_radius_nm",
                "num_particles"
              ],
              "properties": {
                "time_s": {
                  "type": "number",
                  "unit": "s"
                },
                "mean_radius_nm": {
                  "type": "number",
                  "unit": "nm"
                },
                "num_particles": {
                  "type": "integer"
                }
              }
            }
          },
          "K_5at": {
            "type": "number",
            "unit": "nm^3/s"
          },
          "K_10at": {
            "type": "number",
            "unit": "nm^3/s"
          },
          "PSD_5at_start": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "radius_nm",
                "count"
              ],
              "properties": {
                "radius_nm": {
                  "type": "number",
                  "unit": "nm"
                },
                "count": {
                  "type": "integer"
                }
              }
            }
          },
          "PSD_5at_end": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "radius_nm",
                "count"
              ],
              "properties": {
                "radius_nm": {
                  "type": "number",
                  "unit": "nm"
                },
                "count": {
                  "type": "integer"
                }
              }
            }
          },
          "PSD_10at_start": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "radius_nm",
                "count"
              ],
              "properties": {
                "radius_nm": {
                  "type": "number",
                  "unit": "nm"
                },
                "count": {
                  "type": "integer"
                }
              }
            }
          },
          "PSD_10at_end": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "radius_nm",
                "count"
              ],
              "properties": {
                "radius_nm": {
                  "type": "number",
                  "unit": "nm"
                },
                "count": {
                  "type": "integer"
                }
              }
            }
          }
        }
      },
      "description": "Contains the Gibbs-Thomson validation data, coarsening kinetics time series, fitted LSW rate constants, and particle size distributions for 5 and 10 at.% Cu. The hidden checker will recompute the Gibbs-Thomson linear slope and the cubic LSW fits to extract K, and compare against reference values derived from the paper."
    }
  ],
  "notes": "The checker will recompute the Gibbs-Thomson slope via linear regression on the (curvature_1_nm, delta_cp) pairs, and the LSW rate constants K by fitting a cubic polynomial to mean_radius_nm^3 vs time_s for each composition. No tolerances or gold values are given here."
}
```

## How you are scored
A hidden verifier parses your `/app/outputs/simulation_results.json`. It independently recomputes the Gibbs-Thomson linear slope from your (`curvature_1_nm`, `delta_cp`) pairs and fits the LSW coarsening rate constants from your reported mean‑radius‑cubed versus time data. It also checks the shape consistency of the particle size distributions. The verifier compares these recomputed quantities against hidden reference values derived from the original study and combines the individual scores into a final reward:

- Coarsening rate constant K for 5 at.% Cu — 30%
- Coarsening rate constant K for 10 at.% Cu — 30%
- Gibbs-Thomson linear slope — 20%
- Particle size distribution shape consistency (peak location and width) — 20%

Only the contents of your JSON file are examined; simply reporting the target numbers from the literature without producing the correct physical relationships will yield low or zero credit.
