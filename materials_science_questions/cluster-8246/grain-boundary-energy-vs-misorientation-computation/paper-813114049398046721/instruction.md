# Femtosecond-laser microstructural evolution in copper grain boundaries via TTM-MD simulation

## Problem background
When an ultrashort femtosecond laser pulse strikes a metal, energy is first absorbed by the conduction electrons, creating a strong non-equilibrium between hot electrons and the cooler lattice. This triggers rapid heating, phase changes, and stress-wave generation, which can lead to void nucleation and dislocation activity—especially near microstructural features like grain boundaries. Understanding and predicting these coupled responses is essential for advancing laser-based manufacturing and surface engineering. The present task focuses on the interaction of a femtosecond laser pulse with a copper bicrystal containing a high-angle grain boundary, using a multiscale simulation that couples a continuum description of the electrons to an atomistic description of the lattice.

## Approach
The core of the reproduction is a coupled two-temperature model–molecular dynamics (TTM-MD) simulation. The electrons are treated as a continuum with a temperature-dependent thermal conductivity, a linear heat capacity, and a constant electron–phonon coupling factor. The atoms are described by an embedded-atom method (EAM) potential for copper. The two domains exchange energy through electron–phonon coupling. The simulation cell contains a Σ13 (510) symmetric tilt grain boundary, with a free surface at the top where a Gaussian laser pulse is applied, and a non-reflective force applied at the bottom to absorb the transmitted stress wave without reflection. The laser is characterized by its pulse duration (full width at half maximum), penetration depth, and peak absorbed intensity. Separate simulations are run for three different absorbed intensities, each for at least 200 ps, and the atomic trajectories with per-atom stress tensors are recorded. Post-processing of these trajectories yields the volume-averaged pressure history and, for the highest intensity, the final void population statistics.

## Reproduction target
The primary goal is to compute, from the TTM-MD simulations, the peak volumetric pressure reached in the copper sample for each of the three laser intensities, and to quantify the void characteristics that develop by the end of the 200 ps run at the highest intensity. Specifically:
- For each of the three absorbed laser intensities, extract the maximum volume-averaged pressure (defined as the negative third of the trace of the stress tensor) that occurs during the entire simulation. Output the results as a JSON file mapping intensities to their respective peak pressures.
- For the highest-intensity case only, identify all voids at the final simulation time using a cutoff distance equal to the bulk copper lattice constant. Compute the total number of voids, the maximum void diameter, and the total void volume fraction (total void volume divided by the total sample volume). Report these three quantities in a second JSON file.
The correctness of these computed quantities is what will be evaluated.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Copper EAM potential (Mishin et al. 2001): https://www.ctcms.nist.gov/potentials/Cu.html

## Workflow steps

### Step 1: Generate initial Cu Σ13 (510) grain boundary structure
- Role: process
- Action: Construct a bicrystal atomic configuration of copper with a Σ13 (510) symmetric tilt grain boundary using a lattice constant of 3.615 Å, misorientation angle 22.6°, periodic boundary conditions in X and Z, and a free surface in Y. Create a LAMMPS data file with the initial coordinates and velocities corresponding to 300 K.
- Evidence: `/app/outputs/initial_structure.dat`

### Step 2: Run TTM-MD femtosecond-laser simulation on the grain boundary
- Role: process
- Action: Using LAMMPS with fix ttm/mod, set up a coupled two-temperature model (TTM) and molecular dynamics (MD) simulation for the grain boundary structure, incorporating the Fermi-temperature-dependent electron thermal conductivity (Eq. 11), linear electron heat capacity (γ=96.8 J/m³/K²), constant electron–phonon coupling (G=1×10¹⁷ W/m³/K), a non-reflective terminating force at the bottom interface (Eq. 9), and a Gaussian laser source (τ=200 fs, penetration depth h=12 nm). Run separate simulations for absorbed laser intensities I₀ = 597, 797, 996 GW/cm², each for at least 200 ps. Output atomic trajectories with per-atom stress tensor data.
- Evidence: `/app/outputs/simulation.dump`

### Step 3: Extract peak pressures for three laser intensities
- Role: scored (load-bearing)
- Action: From the atomic stress tensors in the simulation dump files for each intensity, compute the volume-averaged pressure history as P = –(σ_xx+σ_yy+σ_zz)/3, identify the maximum pressure value for each intensity, and output a JSON file mapping each intensity to its peak pressure.
- Output file: `/app/outputs/peak_pressures.json`
- Format: json
- Contract: {"type":"object","required":{"intensities":"array[float]","peak_pressures":"array[float]"},"units":{"intensities":"GW/cm^2","peak_pressures":"GPa"}}
- Scoring: scored by hidden verifier

### Step 4: Compute void statistics at the highest intensity
- Role: scored (load-bearing)
- Action: For the simulation with I₀ = 996 GW/cm² at the final simulation time (200 ps), identify all voids using the paper’s neighbor criterion (no atoms within 3.615 Å cutoff). Compute the total number of voids, the maximum void diameter, and the total void volume fraction (void volume / total volume). Write the results to a JSON file.
- Output file: `/app/outputs/void_statistics.json`
- Format: json
- Contract: {"type":"object","required":{"number_of_voids":"integer","max_diameter_nm":"float","total_void_volume_fraction":"float"},"units":{"max_diameter_nm":"nm","total_void_volume_fraction":"dimensionless"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/peak_pressures.json`
- `/app/outputs/void_statistics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### peak_pressures.json
- path: `/app/outputs/peak_pressures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Peak volumetric pressures under 597, 797, and 996 GW/cm² intensities.
- schema:
  - `type`: object
  - `required`:
    - `intensities`: array[float]
    - `peak_pressures`: array[float]
  - `units`:
    - `intensities`: GW/cm^2
    - `peak_pressures`: GPa

### void_statistics.json
- path: `/app/outputs/void_statistics.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Number of large voids (diameter ≥ 10 nm), maximum diameter, and void volume fraction at 200 ps for the 996 GW/cm² case.
- schema:
  - `type`: object
  - `required`:
    - `number_of_large_voids`: integer
    - `max_diameter_nm`: float
    - `total_void_volume_fraction`: float
  - `units`:
    - `max_diameter_nm`: nm
    - `total_void_volume_fraction`: dimensionless

Notes: The hidden verifier compares the reported peak pressures and void statistics against the paper's published values, using permissive tolerances that reflect legitimate implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "peak_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "intensities": "array[float]",
          "peak_pressures": "array[float]"
        },
        "units": {
          "intensities": "GW/cm^2",
          "peak_pressures": "GPa"
        }
      },
      "description": "Peak volumetric pressures under 597, 797, and 996 GW/cm² intensities."
    },
    {
      "file": "void_statistics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "number_of_large_voids": "integer",
          "max_diameter_nm": "float",
          "total_void_volume_fraction": "float"
        },
        "units": {
          "max_diameter_nm": "nm",
          "total_void_volume_fraction": "dimensionless"
        }
      },
      "description": "Number of large voids (diameter ≥ 10 nm), maximum diameter, and void volume fraction at 200 ps for the 996 GW/cm² case."
    }
  ],
  "notes": "The hidden verifier compares the reported peak pressures and void statistics against the paper's published values, using permissive tolerances that reflect legitimate implementation spread."
}
```

## How you are scored
A hidden verifier will independently inspect your output files (`peak_pressures.json` and `void_statistics.json`). It compares the values you report against expected reference values derived from the original study. The verifier computes a reward between 0 and 1 that reflects how closely your results match the expected physical outcomes. The two scored artifacts carry substantial weight, and the overall reward is a weighted combination of their individual scores. The intermediate process steps (creating the initial grain boundary structure and running the TTM-MD simulations) are required to produce the final outputs, but they are not directly scored by the verifier—completing them correctly is the only way to obtain the correct scored numbers.
