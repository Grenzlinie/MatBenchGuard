# Estimation of Surface Free Energies and Equilibrium Vapor Pressure of Quaterthiophene for Nucleation Analysis

## Problem background
Molecular organic thin films, such as quaterthiophene (4T), are often grown by vapor deposition in ultra-high vacuum. The growth process is typically modeled by surface diffusion and aggregation of adsorbed molecules, assuming complete condensation (no re-evaporation). However, observations of 4T film morphology—such as saturation of island density at high deposition rates—suggest that desorption (re-evaporation) of molecules from the substrate may play an important role. Quantifying this effect requires knowledge of the surface free energies of the 4T crystal and the equilibrium vapor pressure of the solid at room temperature, which can be obtained through molecular mechanics simulations and classical nucleation theory. In this task, you will compute these quantities and use them to predict critical nucleus dimensions under typical deposition conditions.

## Approach
The approach combines atomistic simulations with classical nucleation theory. First, the deposition rates and substrate beam pressures are calculated for several source temperatures using the Knudsen effusion equations and published vapor pressure data. Second, molecular mechanics minimizations of slab models of the α-4T/LT crystal are performed with a modified MM3 force field to obtain surface energies for the main crystal faces, as a function of the van der Waals cutoff. Third, using the converged surface energies and a given adhesion energy, the equilibrium vapor pressure of 4T at 298 K is derived by requiring the predicted critical nucleus height to match an experimentally observed value. Finally, the same model yields the critical nucleus dimensions and the thermodynamic supersaturation for each deposition condition. The entire workflow must be executed; all intermediate quantities (e.g., beam pressures) are needed for the final steps.

## Reproduction target
Your objective is to produce three output files that capture the computational pipeline:

1.  **surface_energies.csv**: a table of surface free energies (in meV/Å²) for the (001), (100), (110), and (010) faces of the α-4T/LT crystal, computed with cutoff radii of 9.0, 12.0, 15.0, 17.5, and 19.9 Å. The slab models must be built from the published unit cell and minimized using the modified MM3 force field as specified.

2.  **vapor_pressure_298K.txt**: a single line containing the derived equilibrium vapor pressure of 4T at 298 K, in the format `p_eq = <value> Torr`. You must obtain this value by combining the surface energy of the (001) face at a 19.9 Å cutoff, the adhesion energy σ = 4 meV/Å², the beam pressure for a source temperature of 160°C, and the experimental critical nucleus height n_c* = 9.5.

3.  **critical_dimensions.csv**: a table with the critical nucleus dimensions (n_a*, n_b*, n_c*, n_d*) and the thermodynamic supersaturation Δμ (in eV) for source temperatures 160°C, 170°C, and 180°C, using the converged surface energies (19.9 Å cutoff), the derived p_eq, and the beam pressures.

All files must be placed in `/app/outputs` and conform to the specifications given in the **Output contract** section.

## Assets

- Crystal structure of α-4T/LT (Siegrist et al., Adv. Mater. 1998): 10.1002/(SICI)1521-4095(199803)10:5<379::AID-ADMA379>3.0.CO;2-W
- TINKER molecular modeling package (version 4.1 or later): https://dasher.wustl.edu/tinker/
- Modified MM3 force field for 4T
- Vapor pressure data of 4T (Kloc & Laudise, J. Cryst. Growth 1998): 10.1016/S0022-0248(98)00537-5

## Workflow steps

### Step 1: Compute deposition rates and beam pressures
- Role: process
- Action: Using the Knudsen effusion equations (eqs 2 and 3 in the literature) with the given Knudsen cell parameters (orifice area 7.9e-3 cm², transmission factor 0.6, source–substrate distance 14 cm) and the vapor pressure data of 4T at 160°C, 170°C, and 180°C from Kloc & Laudise, calculate the deposition rates I_A (Å/min) and the substrate beam pressures p_C (Torr) for those three source temperatures.
- Evidence: `/app/outputs/beam_pressures.csv`

### Step 2: Calculate surface free energies
- Role: scored (load-bearing)
- Action: Using the crystal structure of α-4T/LT, build bulklike and surfacelike slabs for the (001), (100), (110), and (010) faces. Perform molecular mechanics minimizations with the modified MM3 force field using TINKER, employing cutoffs of 9.0, 12.0, 15.0, 17.5, and 19.9 Å. Compute the surface energy γ for each face and cutoff using the formula γ = (2E_s - E_b)/(2A).
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: CSV with columns: cutoff (float, Å), face (string, one of 001|100|110|010), surface_energy (float, meV/Å²). One row per combination of cutoff and face.
- Scoring: scored by hidden verifier

### Step 3: Derive room-temperature vapor pressure of 4T
- Role: scored (load-bearing)
- Action: Using the computed surface energy γ001 (at 19.9 Å cutoff), the adhesion energy σ = 4 meV/Å², and the beam pressure p_C for the source temperature 160°C (from step_0), together with the experimental critical nucleus height n_c* = 9.5, apply the relation for critical nucleus dimension and the definition of supersaturation (Δμ = k_B T_c ln(p_c/p_eq)) to solve for the equilibrium vapor pressure p_eq at room temperature (298 K).
- Output file: `/app/outputs/vapor_pressure_298K.txt`
- Format: txt
- Contract: Single line of text: 'p_eq = <value> Torr' where value is a positive number.
- Scoring: scored by hidden verifier

### Step 4: Compute critical nucleus dimensions
- Role: scored (load-bearing)
- Action: With the converged surface energies (19.9 Å cutoff), the derived p_eq, the beam pressures p_C for source temperatures 160°C, 170°C, and 180°C, and the adhesion energy σ = 4 meV/Å², compute the supersaturation Δμ and the critical nucleus dimensions n_a*, n_b*, n_c*, n_d* for each source temperature using the classical nucleation theory equations.
- Output file: `/app/outputs/critical_dimensions.csv`
- Format: csv
- Contract: CSV with columns: source_temp_C (int), n_a_star (float), n_b_star (float), n_c_star (float), n_d_star (float), supersaturation_eV (float, eV). One row per source temperature (160, 170, 180).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energies.csv`
- `/app/outputs/vapor_pressure_298K.txt`
- `/app/outputs/critical_dimensions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed surface free energies for each crystal face and cutoff distance.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `cutoff`, `face`, `surface_energy`
  - `units`:
    - `cutoff`: Å
    - `surface_energy`: meV/Å²

### vapor_pressure_298K.txt
- path: `/app/outputs/vapor_pressure_298K.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium vapor pressure of 4T at 298 K derived from surface energy and critical nucleus height.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `pattern`: p_eq = <float> Torr

### critical_dimensions.csv
- path: `/app/outputs/critical_dimensions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical nucleus dimensions and thermodynamic supersaturation for three source temperatures.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `source_temp_C`, `n_a_star`, `n_b_star`, `n_c_star`, `n_d_star`, `supersaturation_eV`
  - `units`:
    - `source_temp_C`: °C
    - `supersaturation_eV`: eV

Notes: Surface energies must be computed using the modified MM3 force field as described. The derived vapor pressure and critical dimensions depend on the computed surface energies; the checker will verify consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "cutoff",
          "face",
          "surface_energy"
        ],
        "units": {
          "cutoff": "Å",
          "surface_energy": "meV/Å²"
        }
      },
      "description": "Computed surface free energies for each crystal face and cutoff distance."
    },
    {
      "file": "vapor_pressure_298K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "pattern": "p_eq = <float> Torr"
      },
      "description": "Equilibrium vapor pressure of 4T at 298 K derived from surface energy and critical nucleus height."
    },
    {
      "file": "critical_dimensions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "source_temp_C",
          "n_a_star",
          "n_b_star",
          "n_c_star",
          "n_d_star",
          "supersaturation_eV"
        ],
        "units": {
          "source_temp_C": "°C",
          "supersaturation_eV": "eV"
        }
      },
      "description": "Critical nucleus dimensions and thermodynamic supersaturation for three source temperatures."
    }
  ],
  "notes": "Surface energies must be computed using the modified MM3 force field as described. The derived vapor pressure and critical dimensions depend on the computed surface energies; the checker will verify consistency."
}
```

## How you are scored
Each of the three output files (`surface_energies.csv`, `vapor_pressure_298K.txt`, `critical_dimensions.csv`) is scored independently by a hidden automated verifier. The verifier compares your computed values against reference values that are based on the same theoretical model and experimental inputs. The scoring weights are allocated such that the surface energies carry the largest share, followed by the vapor pressure and the critical dimensions. Simply reporting any numbers is not sufficient; the verifier will check that the derived quantities are internally consistent and that the reported supersaturation and critical dimensions can be re-derived from your own surface energies, beam pressures, and vapor pressure. To achieve a high score, you must execute the complete computational procedure accurately—approximate or guessed values will not pass the hidden checks.
