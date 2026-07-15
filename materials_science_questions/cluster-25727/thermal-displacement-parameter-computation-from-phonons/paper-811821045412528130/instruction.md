# Computation of double-well barrier and Curie temperature from electronic potential in SbSI-type ferroelectric crystals

## Problem background
SbSI-type crystals undergo ferroelectric phase transitions driven by a soft B1u normal mode. The potential energy surface of this mode, obtained from the electronic potential of all atoms in the unit cell, can exhibit a double-well shape as a function of the soft-mode amplitude. The height of the barrier between the two wells is directly linked to the Curie temperature via the thermal energy scale. The goal of the present work is to understand how the double-well barrier height and the resulting Curie temperature vary with temperature, hydrostatic pressure, and Bi substitution in mixed Bi<sub>x</sub>Sb<sub>1−x</sub>SI crystals. By computing the electronic potential from crystallographic data, atomic form factors, and Debye‑Waller attenuation, one can trace the evolution of the soft‑mode potential and determine whether and at what temperature a ferroelectric phase transition occurs.

## Approach
The electronic potential at any point in the unit cell is expressed as a sum over reciprocal‑lattice vectors, weighted by atomic form factors and by a Debye‑Waller factor that accounts for the thermal motion of the atoms. For the soft B1u mode, the atoms are displaced along the crystallographic c‑axis according to the mode eigenvector, resulting in a one‑dimensional average potential energy per atom as a function of the displacement amplitude z. At each set of conditions (temperature, pressure, composition) this average potential curve is evaluated numerically for a series of z values. A quartic polynomial V(z) = V₀ + a·z + b·z² + d·z³ + c·z⁴ is fitted to each curve. In regimes where the potential is a symmetric double well (a ≈ 0, d ≈ 0, b < 0, c > 0), the barrier height between the wells is ΔV = b²/(4c). Varying temperature changes the Debye‑Waller factors; varying pressure changes the unit‑cell volume; varying Bi composition changes the average atomic form factor of the mixed sites. The Curie temperature T<sub>C</sub> for each pressure and composition is obtained by scanning the temperature‑dependent barrier heights and locating the temperature at which the barrier first reaches a critical height ΔV<sub>C</sub>. The critical height is calibrated from the known Curie temperature of pure SbSI at ambient pressure (T = 293 K). The calculations are fully specified in the literature and only require publicly available crystallographic data and atomic form factors.

## Reproduction target
Compute the double‑well barrier height ΔV of the B1u soft mode for SbSI and Bi<sub>x</sub>Sb<sub>1−x</sub>SI (with x = 0, 0.06, 0.1, 0.18, 0.2, 0.3, 0.45, 0.6, 0.8) as a function of temperature T (covering the range 0–400 K) and pressure p (0 to 0.8 arbitrary units, where 1 arb. unit = 6.4 kbar). From these data, determine the ferroelectric Curie temperature T<sub>C</sub> for each composition and pressure. The critical barrier ΔV<sub>C</sub> is defined as the barrier height computed for pure SbSI at room temperature (293 K) and zero pressure. For each (x, p) condition, T<sub>C</sub> is the temperature at which ΔV first reaches ΔV<sub>C</sub> when cooling from high temperature; if the barrier never reaches ΔV<sub>C</sub> down to T = 0 K, report that there is no phase transition (e.g., by setting T<sub>C</sub> to −1). The main quantitative outputs are a table of barrier heights for all (T, p, x) conditions, a record of the full quartic coefficients, and a table of the derived Curie temperatures. The results should be fully internally consistent: the barrier heights must follow from the fitted quartic coefficients, and the Curie temperatures must be correctly interpolated from those barrier heights.

## Assets

- SbSI crystal structure data (Voutsas & Rentzeperis 1982): 10.1524/zkri.1982.161.1-2.111
- BiSI crystal structure data (Lukaszewicz et al. 1997)
- Atomic form factors for Bi, Sb, S, I (Audzijonis et al. 1996): 10.1080/01411599608220051

## Workflow steps

### Step 1: Data preparation and grid generation
- Role: process
- Action: Assemble crystallographic data (unit-cell parameters a,b,c, atomic positions R0α, temperature factors b_ij) for SbSI and BiSI from published sources, atomic form factors f_α(s) for Bi, Sb, S, I, and the B1u soft-mode eigenvector. Generate a set of reciprocal-lattice vectors s (about 5000 vectors). Compute Debye-Waller factors exp[-M(s)] for each temperature using the Debye-Waller formula with temperature factors. Create arrays of displaced atomic positions Rα(z) by varying the soft-mode amplitude z along the c-axis from -z_max to +z_max in small steps.
- Evidence: none

### Step 2: Compute average potential energy curves
- Role: process
- Action: For each required combination of temperature T (covering the range 0–400 K to reproduce Tables 1 and 2), pressure p (0 to 0.8 arb. units), and composition x (0, 0.06, 0.1, 0.18, 0.2, 0.3, 0.45, 0.6, 0.8), evaluate the electronic potential V_P(r) at the relevant atomic sites using the reciprocal-lattice sum (Eq. 4) including Debye-Waller attenuation, and average over symmetry‑equivalent atoms (Eq. 5) to obtain V̄_p(z) curves as a function of soft-mode amplitude z. Store the numerical V̄_p(z) curves for each condition for the subsequent fitting step.
- Evidence: none

### Step 3: Fit quartic polynomials and extract barrier heights
- Role: scored (load-bearing)
- Action: For each V̄_p(z) curve, perform a least‑squares fit to the quartic polynomial V(z)=V0 + a·z + b·z² + d·z³ + c·z⁴. Identify symmetric double‑well regimes (a≈0, d≈0, b<0, c>0) and compute the barrier height ΔV = b²/(4c). Write a CSV containing temperature, pressure, composition, and the resulting barrier height ΔV (in atomic units).
- Output file: `/app/outputs/step_02_barrier_heights.csv`
- Format: csv
- Contract: Columns: temperature_K (float), pressure_arb (float), composition_x (float), barrier_V (float in atomic units).
- Scoring: scored by hidden verifier

### Step 4: Output quartic coefficients
- Role: scored
- Action: For every condition (T, p, x), store the full set of fitted quartic coefficients a, b, c, d in a JSON file for consistency auditing.
- Output file: `/app/outputs/step_03_quartic_coefficients.json`
- Format: json
- Contract: Array of objects: {temperature_K: number, pressure_arb: number, composition_x: number, a: number, b: number, c: number, d: number}.
- Scoring: scored by hidden verifier

### Step 5: Determine Curie temperatures T_C
- Role: scored (load-bearing)
- Action: Using the ΔV vs T data for each composition and pressure, locate the temperature at which ΔV first reaches the critical barrier ΔV_C ≈ 0.007 a.u. and report it as the Curie temperature T_C. For conditions where ΔV never reaches 0.007 a.u. (including all x > 0.7), set T_C to a sentinel value (e.g., -1) indicating no transition. Write the results to a CSV.
- Output file: `/app/outputs/step_04_Tc_values.csv`
- Format: csv
- Contract: Columns: composition_x (float), pressure_arb (float), Tc_K (float; -1 if no transition).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_barrier_heights.csv`
- `/app/outputs/step_03_quartic_coefficients.json`
- `/app/outputs/step_04_Tc_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_barrier_heights.csv
- path: `/app/outputs/step_02_barrier_heights.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Barrier heights ΔV of the B1u soft mode double-well potential for varying temperature, pressure, and Bi composition. The checker compares these to the paper's reported values with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_arb`, `composition_x`, `barrier_V`
  - `units`:
    - `barrier_V`: atomic units (a.u.)

### step_03_quartic_coefficients.json
- path: `/app/outputs/step_03_quartic_coefficients.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fitted quartic coefficients for each condition. Checked for consistency (e.g., a≈0, d≈0 in symmetric regimes) with low weight.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `temperature_K`, `pressure_arb`, `composition_x`, `a`, `b`, `c`, `d`
    - `properties`:
      - `temperature_K`:
        - `type`: number
      - `pressure_arb`:
        - `type`: number
      - `composition_x`:
        - `type`: number
      - `a`:
        - `type`: number
      - `b`:
        - `type`: number
      - `c`:
        - `type`: number
      - `d`:
        - `type`: number

### step_04_Tc_values.csv
- path: `/app/outputs/step_04_Tc_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Curie temperatures T_C (in K) for each composition and pressure; -1 indicates no transition. The checker compares to paper values within ±10 K.
- schema:
  - `type`: table
  - `required_columns`: `composition_x`, `pressure_arb`, `Tc_K`
  - `units`:
    - `Tc_K`: Kelvin

Notes: All scored quantities are compared to the paper's hidden gold values with appropriate tolerances (barrier heights ±0.001 a.u., Tc ±10 K).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_barrier_heights.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_arb",
          "composition_x",
          "barrier_V"
        ],
        "units": {
          "barrier_V": "atomic units (a.u.)"
        }
      },
      "description": "Barrier heights ΔV of the B1u soft mode double-well potential for varying temperature, pressure, and Bi composition. The checker compares these to the paper's reported values with a tolerance."
    },
    {
      "file": "step_03_quartic_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "temperature_K",
            "pressure_arb",
            "composition_x",
            "a",
            "b",
            "c",
            "d"
          ],
          "properties": {
            "temperature_K": {
              "type": "number"
            },
            "pressure_arb": {
              "type": "number"
            },
            "composition_x": {
              "type": "number"
            },
            "a": {
              "type": "number"
            },
            "b": {
              "type": "number"
            },
            "c": {
              "type": "number"
            },
            "d": {
              "type": "number"
            }
          }
        }
      },
      "description": "Fitted quartic coefficients for each condition. Checked for consistency (e.g., a≈0, d≈0 in symmetric regimes) with low weight."
    },
    {
      "file": "step_04_Tc_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_x",
          "pressure_arb",
          "Tc_K"
        ],
        "units": {
          "Tc_K": "Kelvin"
        }
      },
      "description": "Curie temperatures T_C (in K) for each composition and pressure; -1 indicates no transition. The checker compares to paper values within ±10 K."
    }
  ],
  "notes": "All scored quantities are compared to the paper's hidden gold values with appropriate tolerances (barrier heights ±0.001 a.u., Tc ±10 K)."
}
```

## How you are scored
A hidden verifier examines the three output files you produce: the barrier heights table, the quartic coefficients file, and the Curie temperatures table. It checks that your reported barrier heights are consistent with your own quartic coefficients (i.e., that ΔV = b²/(4c) for symmetric‑well conditions) and that the Curie temperatures are correctly derived from the barrier‑height data. It also compares your computed barrier heights and Curie temperatures against reference results obtained from an independent re‑implementation of the same procedure. The final score is a weighted combination of the accuracy of each artifact. Fabricating numbers that do not arise from the actual potential‑energy computation will lead to a low score because the verifier cross‑checks internal consistency and does not rely solely on self‑reported values. You must therefore implement the full workflow as described; shortcuts will be detected and penalised.
