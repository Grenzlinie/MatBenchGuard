# MD Simulation of Liquid Water and SFG Spectrum using Flexible Polarizable Water Model

## Problem background
Sum frequency generation (SFG) spectroscopy is a powerful surface-specific nonlinear optical technique used to probe the structure and dynamics of interfacial water. Accurate interpretation of SFG spectra requires reliable molecular models that capture vibrational response and polarization effects. This task centers on a new flexible and polarizable water model based on charge response kernel (CRK) theory, which explicitly includes the conformational dependence of partial charges and electronic polarization. The model is used to simulate a liquid water slab and compute key bulk liquid properties as well as the imaginary part of the ssp-polarized SFG susceptibility of the water surface. The simulation aims to provide insights into the anisotropic local field effects at the interface.

## Approach
The water molecule is modeled as a five-site object: O, two H, and two fictitious X sites allowing out-of-plane polarization. The total potential energy consists of an anharmonic intramolecular potential (with parameters distinguishing positive and negative bond displacements), Lennard-Jones interactions (only on the oxygen site), and Coulomb interactions among self-consistent site charges. The charge response kernel (CRK) relates each site's charge to the local electrostatic potential, and the charges are solved iteratively. Conformational dependencies of the equilibrium charges and response kernels are expressed via first-order expansions in internal coordinates, with derivative parameters determined from DFT calculations.

Short-range Coulomb interactions are damped with a Gaussian charge distribution to prevent polarization catastrophe. Long-range electrostatics are handled by Ewald summation. The simulation uses a slab geometry of 500 water molecules in a rectangular cell (30×30×150 Å³) with gas-liquid interfaces normal to z. The system is initially randomized, equilibrated for 30 ps with a Berendsen thermostat (NVT), and then sampled for 60 ns under NVE conditions with a small time step (~0.61 fs). Trajectory snapshots store site coordinates, induced charges, and electrostatic potentials.

Post-processing: Bulk properties (density, enthalpy of vaporization, average dipole moment, equilibrium OH bond length and HOH angle) are computed by averaging over the liquid region away from the interfaces. The ssp-polarized second-order nonlinear susceptibility χ_ssp is obtained via the time correlation function of the system polarizability and dipole. For the transition dipole calculation, the damping function is omitted (f=1, point-charge approximation) to better capture the strong hydrogen-bonding effects, as found in the original study. The imaginary part of χ_ssp is extracted over the OH stretching region (2800–3800 cm⁻¹).

## Reproduction target
The goal is to produce two scored artifacts:

1. **`/app/outputs/bulk_properties.json`**: A JSON file containing the computed bulk liquid water density, enthalpy of vaporization, average dipole moment, equilibrium O-H bond length, and equilibrium H-O-H angle.

2. **`/app/outputs/sfg_spectrum.csv`**: A CSV file with columns 'wavenumber_cm1' and 'Im_chi_ssp' covering wavenumbers from 2800 to 3800 cm⁻¹ at regular intervals. The hidden verifier will evaluate these quantities against established criteria for bulk water properties and for the structural features of the SFG spectrum (including sign pattern and peak location).

## Assets
No external datasets or pre-trained models are required. The agent must provide its own implementation of the CRK water model, molecular dynamics simulation, and analysis codes. The necessary force-field parameters (intramolecular coefficients, Lennard-Jones parameters, Gaussian width, equilibrium charges and response kernels with their derivatives) are listed in the workflow steps. Standard open-source scientific computing libraries (e.g., Python with NumPy, SciPy) and optionally a molecular dynamics engine (such as LAMMPS or a custom code) are assumed available.

## Workflow steps

### Step 1: Model implementation and MD setup
- Role: process
- Action: Implement the CRK water model with the given intramolecular, Lennard-Jones, Gaussian damping, and CRK parameters (charges, response kernels, and internal-coordinate derivatives). Set up a slab geometry of 500 water molecules in a 30x30x150 Å³ periodic cell with gas-liquid interfaces normal to z. Prepare initial random positions and orientations.
- Evidence: `/app/outputs/model_code.py`

### Step 2: Run MD simulation
- Role: process
- Action: Perform molecular dynamics simulation of the water slab at 298 K using velocity Verlet integrator with a small time step, Ewald summation for long-range electrostatics, and the Gaussian damping function for forces. Equilibrate for 30 ps in NVT (Berendsen thermostat, coupling 0.4 ps), then sample for a total of 60 ns in NVE. Save trajectories, site coordinates, induced charges, and electrostatic potentials at regular intervals for subsequent analysis.
- Evidence: `/app/outputs/simulation_checkpoint.nc`

### Step 3: Calculate bulk water properties
- Role: scored
- Action: From the liquid bulk region of the slab simulation (away from interfaces), compute density, enthalpy of vaporization, average dipole moment, and the equilibrium O-H bond length and H-O-H angle. Output these properties as a JSON file.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: {"density": float, "enthalpy_vaporization": float, "dipole_moment": float, "equilibrium_OH_length": float, "equilibrium_HOH_angle": float}
- Scoring: scored by hidden verifier

### Step 4: Calculate SFG susceptibility
- Role: scored (load-bearing)
- Action: Using the same trajectory, compute the time correlation function of the system polarizability and dipole according to the CRK model with f=1 (point-charge approximation) for the transition dipole. Calculate the imaginary part of χ_ssp as a function of IR wavenumber from 2800 to 3800 cm⁻¹. Output the spectrum to a CSV file.
- Output file: `/app/outputs/sfg_spectrum.csv`
- Format: csv
- Contract: columns: wavenumber_cm1 (int), Im_chi_ssp (float). Rows covering wavenumbers from 2800 to 3800 cm⁻¹ at regular intervals.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/sfg_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk liquid water properties computed from MD simulation. Checker compares values against paper-reported values within hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `density`: number (g/cm^3)
    - `enthalpy_vaporization`: number (kcal/mol)
    - `dipole_moment`: number (D)
    - `equilibrium_OH_length`: number (Angstrom)
    - `equilibrium_HOH_angle`: number (deg)

### sfg_spectrum.csv
- path: `/app/outputs/sfg_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Imaginary part of the ssp-polarized SFG susceptibility. Checker will verify sign pattern in three frequency bands (3000-3200 cm⁻¹ positive, 3200-3600 cm⁻¹ negative, 3650-3750 cm⁻¹ positive) and a peak in the negative band.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber_cm1`, `Im_chi_ssp`
  - `units`:
    - `wavenumber_cm1`: int
    - `Im_chi_ssp`: float

Notes: Only the two headline artifacts from the paper's main experiment (bulk properties and SFG spectrum) are scored. The underlying MD simulation and model implementation are required process steps but not scored directly. DFT parameter derivation, dimer assessment, and PD model comparison are omitted per taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "density": "number (g/cm^3)",
          "enthalpy_vaporization": "number (kcal/mol)",
          "dipole_moment": "number (D)",
          "equilibrium_OH_length": "number (Angstrom)",
          "equilibrium_HOH_angle": "number (deg)"
        }
      },
      "description": "Bulk liquid water properties computed from MD simulation. Checker compares values against paper-reported values within hidden tolerances."
    },
    {
      "file": "sfg_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber_cm1",
          "Im_chi_ssp"
        ],
        "units": {
          "wavenumber_cm1": "int",
          "Im_chi_ssp": "float"
        }
      },
      "description": "Imaginary part of the ssp-polarized SFG susceptibility. Checker will verify sign pattern in three frequency bands (3000-3200 cm⁻¹ positive, 3200-3600 cm⁻¹ negative, 3650-3750 cm⁻¹ positive) and a peak in the negative band."
    }
  ],
  "notes": "Only the two headline artifacts from the paper's main experiment (bulk properties and SFG spectrum) are scored. The underlying MD simulation and model implementation are required process steps but not scored directly. DFT parameter derivation, dimer assessment, and PD model comparison are omitted per taskability scope."
}
```

## How you are scored
A hidden verifier checks each scored artifact independently. For bulk_properties.json, the verifier compares the reported values to reference values within certain tolerances. For sfg_spectrum.csv, the verifier inspects the sign of the imaginary part of χ_ssp averaged over three predefined frequency windows (3000–3200 cm⁻¹, 3200–3600 cm⁻¹, 3650–3750 cm⁻¹) and verifies that a peak exists in one of the windows, as expected from the model. The final reward is a weighted combination of the scores for these two artifacts. The verifier does not require the agent to match the paper's precise numerical results; instead, it assesses physical consistency and reproduction of qualitative features.
