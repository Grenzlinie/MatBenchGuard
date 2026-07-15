# Monte Carlo electron transport and electron emission from carbon foils under heavy-ion impact

## Problem background
Energetic heavy ions traversing thin solid foils produce intense secondary electron emission, relevant to radiotherapy, space electronics, and heavy-ion fusion. Predicting the absolute doubly-differential electron yields, total yields, and the time evolution of the emission requires coupling an accurate single-collision ionization model with a detailed electron transport treatment through the amorphous solid. This task reproduces a numerical simulation framework that computes these quantities for multiply-charged uranium ions incident on amorphous carbon foils of various thicknesses.

## Approach
The reproduction implements a two-step numerical model. First, for every ion–carbon collision the n-body classical trajectory Monte Carlo (nCTMC) method is used to generate the initial burst of liberated electrons: the method includes the six target electrons and uses a Hartree–Fock-based screening potential for the partially-stripped projectile. Second, each electron is transported through the amorphous carbon foil until it either exits or its energy drops below a termination threshold. The transport incorporates continuous energy loss via the Bethe–Bloch formula, normalized to published experimental stopping data for carbon, and angular scattering via quantal partial-wave elastic differential cross sections evaluated for a static Hartree–Fock carbon potential. The transport code is benchmarked against observed electron straggling data before being used for the ion-induced emission. The simulation is repeated for several foil areal densities, and the exit events are accumulated to obtain doubly-differential and total yields, to locate any binary peaks in the energy spectrum, and to track the cumulative forward/backward emission as a function of the ion’s position within the foil.

## Reproduction target
Produce the following quantitative results from the complete simulation:

- Total electron yields per incident ion (forward and backward components) for foil thicknesses: 1, 10, 20, 44, 100, 1000 µg/cm².
- Absolute doubly-differential electron yields (energy vs. angle) for the 44 µg/cm² foil.
- Energies of the two most prominent peaks in the 40° energy spectrum for the 44 µg/cm² foil.
- Cumulative forward and backward emission percentages as a function of projectile position fraction (0 to 1) for foil thicknesses 1, 10, and 100 µg/cm².

All results must be computed from scratch using the described simulation procedure; no pre‑computed outputs are provided.

## Assets

- Electron stopping and straggling data for carbon foils (Lencinas et al 1990): 10.1103/PhysRevA.41.1435

## Workflow steps

### Step 1: Simulation parameter definition
- Role: process
- Action: Define simulation configuration: projectile (U³⁸⁺, 3.5 MeV/u), foil areal densities (1, 10, 20, 44, 100, 1000 µg/cm²), number of projectile ions (20000), collision frequency (~20 per µg/cm²), and electron termination energy (100 eV).
- Evidence: `/app/outputs/simulation_config.json`

### Step 2: nCTMC single-collision ionization
- Role: process
- Action: Implement and run the n-body classical trajectory Monte Carlo (nCTMC) method for every projectile–carbon collision to generate the initial burst of liberated electrons. Use a Hartree–Fock-based model potential for projectile screening and include all six target electrons. Record the initial positions and velocities of the ionized electrons.
- Evidence: `/app/outputs/nctmc_summary.json`

### Step 3: Electron transport through amorphous carbon foils
- Role: process
- Action: Transport each liberated electron through the foil. Apply continuous energy loss using the Bethe–Bloch formula normalised to experimental stopping data (Lencinas et al 1990), and angular scattering via quantal partial-wave elastic differential cross sections assuming a static Hartree-Fock carbon potential, with random azimuthal scattering. Follow each electron until it exits the foil or its energy drops below 100 eV, and log exit energies, angles, and termination status.
- Evidence: `/app/outputs/transport_log.csv`

### Step 4: Transport model benchmark
- Role: process
- Action: Validate the electron transport model by simulating monoenergetic electrons incident on carbon foils and comparing the resulting angular and energy straggling to the experimental data of Lencinas et al (1990). Produce a brief validation report with summary statistics.
- Evidence: `/app/outputs/benchmark_report.txt`

### Step 5: Total electron yields per ion
- Role: scored (load-bearing)
- Action: From the exit events accumulated in step 3, compute for each foil thickness the total number of electrons emitted per incident ion, separately for forward (θ < 90°) and backward (θ ≥ 90°) directions.
- Output file: `/app/outputs/total_yields.csv`
- Format: csv
- Contract: thickness (float, µg/cm²), total_yield (float), forward_yield (float), backward_yield (float)
- Scoring: scored by hidden verifier

### Step 6: Doubly-differential yields for 44 µg/cm² foil
- Role: scored
- Action: Accumulate the absolute doubly-differential electron yield as a function of exit energy and emission angle for the 44 µg/cm² foil. Bin exit events in energy (e.g. 0.5 keV bins) and angle (e.g. 10° bins) and output the yield in electrons per eV per steradian.
- Output file: `/app/outputs/yields_44_ugcm2.csv`
- Format: csv
- Contract: energy_eV (float), angle_deg (float), yield (float)
- Scoring: scored by hidden verifier

### Step 7: Double binary peak identification
- Role: scored
- Action: From the 44 µg/cm² doubly-differential yields at the 40° observation angle, identify the two prominent peaks in the energy spectrum and report their energies.
- Output file: `/app/outputs/binary_peaks.json`
- Format: json
- Contract: {"foil_thickness_ugcm2": 44, "angle_deg": 40, "peak_energies_eV": [float, float]}
- Scoring: scored by hidden verifier

### Step 8: Time-resolved emission fractions
- Role: scored
- Action: For foil thicknesses 1, 10 and 100 µg/cm², compute the cumulative percentage of forward and backward emitted electrons as a function of the projectile's position fraction (from 0 to 1 relative to foil thickness). Sample the position fraction at intervals ≤ 0.1.
- Output file: `/app/outputs/time_resolved.csv`
- Format: csv
- Contract: thickness (float, µg/cm²), position_fraction (float), forward_percent (float), backward_percent (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_yields.csv`
- `/app/outputs/yields_44_ugcm2.csv`
- `/app/outputs/binary_peaks.json`
- `/app/outputs/time_resolved.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_yields.csv
- path: `/app/outputs/total_yields.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total electron yields per incident ion for foil thicknesses 1, 10, 20, 44, 100, 1000 µg/cm², with forward/backward breakdown.
- schema:
  - `type`: table
  - `required_columns`: `thickness`, `total_yield`, `forward_yield`, `backward_yield`
  - `units`:
    - `thickness`: µg/cm²
    - `total_yield`: electrons/ion
    - `forward_yield`: electrons/ion
    - `backward_yield`: electrons/ion

### yields_44_ugcm2.csv
- path: `/app/outputs/yields_44_ugcm2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Absolute doubly-differential electron yield for the 44 µg/cm² foil, binned in energy and angle.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `angle_deg`, `yield`
  - `units`:
    - `energy_eV`: eV
    - `angle_deg`: degrees
    - `yield`: electrons / (eV·sr)

### binary_peaks.json
- path: `/app/outputs/binary_peaks.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Energies of the double binary peaks at 40° for the 44 µg/cm² foil.
- schema:
  - `type`: object
  - `required`:
    - `foil_thickness_ugcm2`: integer
    - `angle_deg`: number
    - `peak_energies_eV`: array of two numbers

### time_resolved.csv
- path: `/app/outputs/time_resolved.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cumulative forward/backward emission percentages as a function of projectile position for 1, 10, 100 µg/cm² foils.
- schema:
  - `type`: table
  - `required_columns`: `thickness`, `position_fraction`, `forward_percent`, `backward_percent`
  - `units`:
    - `thickness`: µg/cm²
    - `position_fraction`: dimensionless
    - `forward_percent`: %
    - `backward_percent`: %

Notes: All scored outputs are derived from the full Monte Carlo simulation. The checker compares total yields, doubly-differential yields, binary peak energies, and time-resolved fractions against reference values from the paper, with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_yields.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness",
          "total_yield",
          "forward_yield",
          "backward_yield"
        ],
        "units": {
          "thickness": "µg/cm²",
          "total_yield": "electrons/ion",
          "forward_yield": "electrons/ion",
          "backward_yield": "electrons/ion"
        }
      },
      "description": "Total electron yields per incident ion for foil thicknesses 1, 10, 20, 44, 100, 1000 µg/cm², with forward/backward breakdown."
    },
    {
      "file": "yields_44_ugcm2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "angle_deg",
          "yield"
        ],
        "units": {
          "energy_eV": "eV",
          "angle_deg": "degrees",
          "yield": "electrons / (eV·sr)"
        }
      },
      "description": "Absolute doubly-differential electron yield for the 44 µg/cm² foil, binned in energy and angle."
    },
    {
      "file": "binary_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "foil_thickness_ugcm2": "integer",
          "angle_deg": "number",
          "peak_energies_eV": "array of two numbers"
        }
      },
      "description": "Energies of the double binary peaks at 40° for the 44 µg/cm² foil."
    },
    {
      "file": "time_resolved.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness",
          "position_fraction",
          "forward_percent",
          "backward_percent"
        ],
        "units": {
          "thickness": "µg/cm²",
          "position_fraction": "dimensionless",
          "forward_percent": "%",
          "backward_percent": "%"
        }
      },
      "description": "Cumulative forward/backward emission percentages as a function of projectile position for 1, 10, 100 µg/cm² foils."
    }
  ],
  "notes": "All scored outputs are derived from the full Monte Carlo simulation. The checker compares total yields, doubly-differential yields, binary peak energies, and time-resolved fractions against reference values from the paper, with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently inspects each of the four scored output files after your run. It checks that the reported total yields, doubly‑differential spectra, peak energies, and time‑resolved fractions are physically consistent and are of a magnitude and exhibit trends that can only arise from a faithful execution of the described simulation. The verifier does not require the outputs to exactly match any particular published figure; instead it assesses whether the submitted values are characteristic of a correct implementation. Each artifact is scored separately, and the final reward is a weighted combination of these scores. Simply printing the paper’s table or a constant string is not sufficient—the artifacts must be generated by running the numerical workflow.
