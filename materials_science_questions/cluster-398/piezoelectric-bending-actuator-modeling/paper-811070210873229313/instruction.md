# Effect of a polythene membrane on physiotherapy ultrasound probe power output

## Problem background
Physiotherapy ultrasound probes (1–3 MHz) are often tested with radiation force balances that measure emitted acoustic power. Many balances use a thin coupling membrane to seal the water tank, separating the probe face from the water. Because these probes are highly resonant, the membrane can alter the acoustic load and shift the effective resonant frequency, thereby changing the output power delivered to the water. Understanding and quantifying this effect is essential for reliable power calibration of clinical physiotherapy devices.

## Approach
A one-dimensional, plane-wave model is used to represent the physiotherapy probe as a stack of five layers: air backing, a piezoelectric (PC4) ceramic disk, a stainless steel matching layer, an optional polythene membrane, and a water load. The piezoelectric constitutive equations relate mechanical stress, strain, and electric displacement in the disk. By enforcing continuity of particle displacement and normal stress at each interface and applying the electrical boundary conditions (sinusoidal drive voltage across the disk), the complex electrical impedance Z(f) of the assembly can be derived as a function of frequency. The emitted acoustic power into water is then computed as P(f) = V²·Re(Z) / (2·|Z|²) for a constant drive voltage V = 1 V.

You must implement this model using the material parameters below. Compute impedance and power over a frequency range of 1.0 MHz to 1.2 MHz with at least 100 points, once for the case without the membrane (polythene thickness = 0 µm) and once with a 100 µm membrane.

Material parameters:
- PC4 disk: speed of sound 3802 m/s, density 7500 kg/m³, thickness 1.60 mm, diameter 0.025 m, permittivity K = 4.703 × 10⁻⁹ F/m, piezoelectric constant h = 3.402 × 10⁹ V/m, stiffness α = 1.084 × 10¹¹ N/m².
- Stainless steel: speed of sound 6000 m/s, density 7800 kg/m³, thickness 2.52 mm.
- Polythene: speed of sound 2000 m/s, density 930 kg/m³, thickness either 0 µm or 100 µm.
- Air: speed of sound 330 m/s, density 1.3 kg/m³.
- Water: speed of sound 1480 m/s, density 1000 kg/m³.

All layers are assumed laterally infinite and lossless; the model handles only thickness-mode resonances.

## Reproduction target
Your task is to compute the ultrasonic power output of the five-layer probe as a function of frequency, both with and without a 100 µm polythene membrane. From these power curves, the verifier will determine the maximum percentage increase and maximum percentage decrease in power caused by the membrane. You are expected to provide the raw power-vs.-frequency data in the specified CSV format; the verifier will use that data to compute the percentage change values and compare them to the expected results of the model.

## Assets
This task requires no external datasets, models, or specialized tools. All material constants and geometry are provided in the Approach section. The solver may use standard scientific Python libraries (e.g., numpy, scipy) for computation.

## Workflow steps

### Step 1: Compute power output with and without membrane
- Role: scored (load-bearing)
- Action: Implement the five-layer piezoelectric transducer model (air-backed PC4 disk, stainless-steel face, optional polythene membrane, water load) using the piezoelectric constitutive equations and acoustic boundary-matching method. For a frequency range of 1.0–1.2 MHz with at least 100 points, compute the electrical impedance and then the emitted power at a constant voltage drive (e.g., V=1 V). Repeat for the case with a 100-µm membrane and for the case without membrane (thickness = 0). Write the resulting power curves to the output file.
- Output file: `/app/outputs/step_01_power_output.csv`
- Format: csv
- Contract: Header: frequency_Hz, power_without_membrane_W, power_with_membrane_W. Frequency in Hz, power in watts. At least 100 frequency points covering 1.0 MHz to 1.2 MHz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_power_output.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_power_output.csv
- path: `/app/outputs/step_01_power_output.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Power output curves for the five-layer probe model; the checker recomputes the maximum percentage increase and decrease due to the membrane and compares to the paper’s reference values.
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `power_without_membrane_W`, `power_with_membrane_W`
  - `units`:
    - `frequency_Hz`: Hz
    - `power_without_membrane_W`: W
    - `power_with_membrane_W`: W

Notes: The model parameters (from Table 1: PC4 piezoelectric disk, stainless steel, polythene, air, water) are specified in the instruction. The solver must handle all layer boundary matching internally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_power_output.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "power_without_membrane_W",
          "power_with_membrane_W"
        ],
        "units": {
          "frequency_Hz": "Hz",
          "power_without_membrane_W": "W",
          "power_with_membrane_W": "W"
        }
      },
      "description": "Power output curves for the five-layer probe model; the checker recomputes the maximum percentage increase and decrease due to the membrane and compares to the paper’s reference values."
    }
  ],
  "notes": "The model parameters (from Table 1: PC4 piezoelectric disk, stainless steel, polythene, air, water) are specified in the instruction. The solver must handle all layer boundary matching internally."
}
```

## How you are scored
Your submission will be scored by an automated verifier. It will read your CSV file, compute the percentage change in power at each frequency, and extract the maximum increase and maximum decrease. These two values are compared to hidden reference values (the correct results of the theoretical model). Full credit is awarded if both values are within a predefined tolerance; partial credit is proportional to the number of values within tolerance. No other artifacts are examined.
