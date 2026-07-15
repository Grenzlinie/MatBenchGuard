# Monte Carlo Simulation of Multisubband Charge Transport in GaAs Quantum Wires

## Problem background
Quasi-one-dimensional quantum wires made of GaAs-AlGaAs exhibit dramatically altered transport properties due to extreme transverse confinement. In such structures, the electron motion is restricted to a single longitudinal direction, and the energy states form discrete subbands. The interplay between confinement, electron-phonon scattering (polar optical and acoustic), and the occupation of multiple subbands determines the drift velocity and subband populations. This task explores how varying the transverse confinement changes the electron distribution and velocity, including conditions where the energy separation between the lowest subbands matches the polar-optical-phonon energy, leading to a resonance effect analogous to the magnetophonon effect. The target is to compute the steady-state drift velocity and the fraction of electrons in each subband under specified temperature, electric field, and confinement geometries.

## Approach
The work is reproduced using a multisubband Monte Carlo simulation. The electron states are obtained by solving the Schrödinger equation for the transverse confinement: an infinite square-well potential along one direction (y) and a triangular potential along the other (z), approximated by a variational damped-polynomial method. The resulting transverse wavefunctions and subband energies are combined with a parabolic longitudinal dispersion to form the electronic structure. Electron-phonon scattering is treated by projecting bulk three-dimensional polar-optical-phonon and acoustic-phonon matrix elements onto the one-dimensional subband states. Scattering rates are computed over a wide energy range using Fermi's golden rule with Gaussian energy broadening to avoid density-of-states singularities. Transport is simulated with a steady-state single-particle Monte Carlo code that uses a direct-integration algorithm for free-flight determination and before-scattering renormalization to obtain the correct electron distribution. The workflow runs for several confinement configurations (different well widths and gate fields) and two lattice temperatures. For comparison, the wire's drift velocity is benchmarked against the known bulk GaAs drift velocity under identical conditions.

## Reproduction target
You must produce two scored output files. First, `velocity_results.json` must contain the drift velocity of electrons in a GaAs quantum wire with optimal confinement (well width Ly = 135 Å, gate field Fz = 120 kV/cm) at a longitudinal electric field of 500 V/cm for both 300 K and 77 K, together with the corresponding bulk GaAs drift velocity at the same conditions. Second, `distribution_results.json` must report the electron population fractions in the three lowest subbands for three different confinement sets that result in first-to-second subband energy separations of about 28 meV (off-resonance), 36 meV (resonance), and 44 meV (above-resonance), all at 300 K and a field of 500 V/cm. The exact formats and schemas are specified in the workflow steps. You must implement the full computational pipeline (subband solver, rate tabulator, and Monte Carlo simulator) from scratch; no pre-computed data or code is provided. All reported results must derive from your own simulations.

## Assets

- GaAs material parameters
- Bulk GaAs drift velocity vs. field: 10.1063/1.335733
- Python 3: python3
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Subband structure computation
- Role: process
- Action: Compute the transverse subband energies and wavefunction parameters for GaAs quantum wire structures using the infinite-square-well approximation in the y-direction and the variational damped-polynomial method in the z-direction, for all required confinement sets: the optimal set (Ly=135 Å, Fz=120 kV/cm), and at least three other sets that yield first-to-second subband energy separations of approximately 28, 36, and 44 meV. Use the electron effective mass m*=0.067 m0 and elementary charge. Order the subbands by increasing energy and assign a single index v=1..7. Save the computed subband energies, ordering, and variational parameters for each confinement set to subband_data.json.
- Evidence: `/app/outputs/subband_data.json`

### Step 2: Scattering rate computation
- Role: process
- Action: For each confinement set and for the required temperatures (300 K and 77 K for the optimal set; 300 K for the resonance sets), compute intersubband scattering rates for polar optical phonons and acoustic phonons. Project bulk 3D electron-phonon matrix elements onto the 1D transverse wave functions, apply Fermi's golden rule, use Gaussian energy broadening (with appropriate POP broadening time) to remove density-of-states singularities, and tabulate the total scattering rates on a 400-point energy mesh from 100 to 400 meV above the well bottom for each subband and for all four possible final states (forward/backward emission/absorption). Save the rate tables to rate_tables.npz.
- Evidence: `/app/outputs/rate_tables.npz`

### Step 3: Monte Carlo simulation for drift velocity
- Role: scored (load-bearing)
- Action: Using the precomputed scattering rate tables for the optimal confinement (Ly=135 Å, Fz=120 kV/cm), run a steady-state single-particle Monte Carlo simulation at T=300 K and T=77 K with a longitudinal electric field of Fx=500 V/cm. Implement the direct-integration free-flight algorithm and before-scattering renormalization. For each temperature, compute the average drift velocity of the electron. Also determine the bulk GaAs drift velocity under the same conditions using known mobility data (e.g., from Haase et al., J. Appl. Phys. 57, 2295 (1985)) or a simple analytical model. Write the results to velocity_results.json according to the specified schema.
- Output file: `/app/outputs/velocity_results.json`
- Format: json
- Contract: {
  "optimal_confinement": {"Ly": 135, "Fz": 120, "units": "Å, kV/cm"},
  "velocities": [
    {"T": 300, "Fx": 500, "velocity_cm_s": <float>, "bulk_velocity_cm_s": <float>},
    {"T": 77, "Fx": 500, "velocity_cm_s": <float>, "bulk_velocity_cm_s": <float>}
  ]
}
- Scoring: scored by hidden verifier

### Step 4: Monte Carlo simulation for subband populations
- Role: scored
- Action: For each of the three resonance-condition confinement sets (subband separation ≈ 28, 36, 44 meV), run the steady-state single-particle Monte Carlo simulation at T=300 K and Fx=500 V/cm, using the corresponding precomputed rate tables. Compute the electron population fractions in the three lowest subbands after reaching steady state. Write the results to distribution_results.json according to the specified schema.
- Output file: `/app/outputs/distribution_results.json`
- Format: json
- Contract: {
  "resonance_data": [
    {"case": "off_resonance", "delta_E_meV": 28, "fraction_subband_1": <float>, "fraction_subband_2": <float>, "fraction_subband_3": <float>},
    {"case": "resonance", "delta_E_meV": 36, "fraction_subband_1": <float>, "fraction_subband_2": <float>, "fraction_subband_3": <float>},
    {"case": "above_resonance", "delta_E_meV": 44, "fraction_subband_1": <float>, "fraction_subband_2": <float>, "fraction_subband_3": <float>}
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/velocity_results.json`
- `/app/outputs/distribution_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### velocity_results.json
- path: `/app/outputs/velocity_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Drift velocity results for the optimal confinement condition at two temperatures. Compared to the paper's reported values within tolerance.
- schema:
  - `type`: object
  - `properties`:
    - `optimal_confinement`:
      - `type`: object
      - `properties`:
        - `Ly`:
          - `type`: number
          - `description`: well width in Å
        - `Fz`:
          - `type`: number
          - `description`: gate field in kV/cm
        - `units`:
          - `type`: string
          - `description`: units
    - `velocities`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `T`:
            - `type`: number
            - `description`: temperature in K
          - `Fx`:
            - `type`: number
            - `description`: longitudinal field in V/cm
          - `velocity_cm_s`:
            - `type`: number
            - `description`: 1D drift velocity in cm/s
          - `bulk_velocity_cm_s`:
            - `type`: number
            - `description`: bulk GaAs drift velocity in cm/s

### distribution_results.json
- path: `/app/outputs/distribution_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Subband population fractions for three confinement cases near the POP resonance. Compared to the paper's reported values within tolerance.
- schema:
  - `type`: object
  - `properties`:
    - `resonance_data`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `case`:
            - `type`: string
            - `description`: off_resonance, resonance, or above_resonance
          - `delta_E_meV`:
            - `type`: number
            - `description`: subband separation in meV
          - `fraction_subband_1`:
            - `type`: number
            - `description`: population fraction in subband 1
          - `fraction_subband_2`:
            - `type`: number
            - `description`: population fraction in subband 2
          - `fraction_subband_3`:
            - `type`: number
            - `description`: population fraction in subband 3

Notes: The drift velocity and subband population fractions are the main scored outputs of the simulation reproduction. The hidden checker compares the agent's computed values to the paper's reported reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "velocity_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "optimal_confinement": {
            "type": "object",
            "properties": {
              "Ly": {
                "type": "number",
                "description": "well width in Å"
              },
              "Fz": {
                "type": "number",
                "description": "gate field in kV/cm"
              },
              "units": {
                "type": "string",
                "description": "units"
              }
            }
          },
          "velocities": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "T": {
                  "type": "number",
                  "description": "temperature in K"
                },
                "Fx": {
                  "type": "number",
                  "description": "longitudinal field in V/cm"
                },
                "velocity_cm_s": {
                  "type": "number",
                  "description": "1D drift velocity in cm/s"
                },
                "bulk_velocity_cm_s": {
                  "type": "number",
                  "description": "bulk GaAs drift velocity in cm/s"
                }
              }
            }
          }
        }
      },
      "description": "Drift velocity results for the optimal confinement condition at two temperatures. Compared to the paper's reported values within tolerance."
    },
    {
      "file": "distribution_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "resonance_data": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "case": {
                  "type": "string",
                  "description": "off_resonance, resonance, or above_resonance"
                },
                "delta_E_meV": {
                  "type": "number",
                  "description": "subband separation in meV"
                },
                "fraction_subband_1": {
                  "type": "number",
                  "description": "population fraction in subband 1"
                },
                "fraction_subband_2": {
                  "type": "number",
                  "description": "population fraction in subband 2"
                },
                "fraction_subband_3": {
                  "type": "number",
                  "description": "population fraction in subband 3"
                }
              }
            }
          }
        }
      },
      "description": "Subband population fractions for three confinement cases near the POP resonance. Compared to the paper's reported values within tolerance."
    }
  ],
  "notes": "The drift velocity and subband population fractions are the main scored outputs of the simulation reproduction. The hidden checker compares the agent's computed values to the paper's reported reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will run automatically after your submission. It reads `velocity_results.json` and `distribution_results.json` and compares the numbers you report against expected reference values that were obtained from the original study. The comparison uses a tolerance that accounts for the natural spread introduced by different implementations, numerical discretizations, and random seeds, so a correct simulation will score highly. The verifier also checks that the trend across the three resonance cases (the relative population changes) follows the expected physical behaviour. Each scored artifact contributes a weight to the final reward (`velocity_results.json` carries the larger share). You do not need to know the reference values; they are secret. Because the tolerance is set to separate a genuine simulation from a wild guess, simply copying publicly available numbers is unlikely to give a high score.
