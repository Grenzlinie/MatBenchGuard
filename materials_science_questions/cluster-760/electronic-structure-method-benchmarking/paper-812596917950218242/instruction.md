# Reproduce B3LYP/6-311++G(d,p) properties and vibrational analysis of the cyclopropane–ClF charge-transfer complex

## Problem background
The pseudo-π…σ charge-transfer complex formed by cyclopropane (C₃H₆) and chlorine monofluoride (ClF) has been characterized by rotational spectroscopy, yielding precise experimental rotational constants and an intermolecular distance. Density functional theory, in particular the B3LYP hybrid functional with the 6‑311++G(d,p) basis set, is able to reproduce these geometrical parameters and thereby provides access to quantities that have not been measured directly: the dissociation energy of the complex, the shape of the intermolecular stretching potential, and the number and energies of the vibrational states this potential supports. This task computes those B3LYP properties from first principles and compares them against the published experimental and theoretical reference.

## Approach
All calculations use the B3LYP hybrid density functional in its standard formulation and the 6‑311++G(d,p) basis set. The geometry of the cyclopropane···ClF complex is optimized under C₂ᵥ symmetry and confirmed to be a true minimum by a harmonic frequency calculation. From this optimized structure the rotational constants A, B, C are derived. The dissociation energy is obtained via the counterpoise procedure: the total energies of the isolated monomers (each at its own optimized geometry) and of the complex are calculated at the same level, the basis set superposition error is subtracted, and the zero‑point vibrational energy correction is applied.

To map the intermolecular coordinate, the potential energy is scanned by performing single‑point calculations at many distances between the ClF and cyclopropane fragments, keeping the internal geometries of the monomers frozen at their optimized values. The resulting curve is fit to a Morse potential V(x) = V₀{[1 – exp(–γ (x – x_min))]² – 1}. With the fitted Morse curve and a reduced mass of 7.3938 u for the intermolecular stretch, the WKB quantization integral is solved numerically to locate all bound vibrational states. From the bound‑state energies the fundamental (1←0) and first overtone (2←0) excitation wavenumbers and the zero‑point vibrational energy are computed.

## Reproduction target
Produce the following outputs in the exact files and formats listed under “## Workflow steps” and “## Output contract”: (1) optimized Cartesian geometry of the C₃H₆···ClF complex, (2) the three rotational constants A, B, C (MHz), (3) the BSSE‑ and ZPVE‑corrected dissociation energy D₀ (kcal mol⁻¹), (4) a 35‑point table of intermolecular distance r(*···Cl) and total energy, (5) the fitted Morse parameters V₀, γ, x_min and the rms deviation of the fit, and (6) the number of bound states, their energies (au), the fundamental and first overtone (cm⁻¹), and the zero‑point vibrational energy (kcal mol⁻¹ relative to the potential minimum).

## Assets

- B3LYP hybrid density functional (standard formulation)
- 6-311++G(d,p) basis set
- Quantum chemistry package (e.g., ORCA, Psi4, PySCF): https://orcaforum.kofo.mpg.de
- Python with SciPy stack: scipy

## Workflow steps

### Step 1: Geometry optimization and frequency check
- Role: process
- Action: Optimize the geometry of the cyclopropane···ClF complex at the B3LYP/6‑311++G(d,p) level, enforcing C₂ᵥ symmetry, and run a harmonic frequency calculation to confirm the structure is a minimum (no imaginary frequencies). Output the final Cartesian coordinates as /app/outputs/step_01_optimized_geometry.xyz for use in subsequent steps.
- Evidence: `/app/outputs/step_01_optimized_geometry.xyz`

### Step 2: Extract rotational constants
- Role: scored
- Action: From the optimized geometry of the complex (step_01) and the molecular mass distribution, calculate the rotational constants A, B, C (in MHz). Write the three values to /app/outputs/step_02_rotational_constants.json.
- Output file: `/app/outputs/step_02_rotational_constants.json`
- Format: json
- Contract: {"A_MHz": float, "B_MHz": float, "C_MHz": float}
- Scoring: scored by hidden verifier

### Step 3: Compute BSSE‑corrected dissociation energy
- Role: scored
- Action: Calculate the total energies of the isolated cyclopropane and ClF monomers at their B3LYP/6‑311++G(d,p) optimized geometries, and the energy of the complex. Apply the counterpoise correction to obtain the basis set superposition error (BSSE). Using the zero‑point vibrational energy from the harmonic frequency calculation (step_01), compute the ZPVE‑ and BSSE‑corrected dissociation energy D₀ in kcal/mol. Write the result to /app/outputs/step_03_interaction_energy.json.
- Output file: `/app/outputs/step_03_interaction_energy.json`
- Format: json
- Contract: {"D0_kcal_mol": float}
- Scoring: scored by hidden verifier

### Step 4: Rigid‑monomer intermolecular potential scan
- Role: scored (load-bearing)
- Action: Using the B3LYP/6‑311++G(d,p) optimized fragment geometries, perform single‑point energy calculations at 35 values of the intermolecular distance r(*···Cl) covering approximately 2.8 Å to 4.5 Å, keeping both ClF and cyclopropane monomers rigid. Record the distance and total energy for each point in /app/outputs/step_04_potential_curve.csv.
- Output file: `/app/outputs/step_04_potential_curve.csv`
- Format: csv
- Contract: CSV with header: r_A,energy_au. Exactly 35 rows covering the intermolecular coordinate.
- Scoring: scored by hidden verifier

### Step 5: Morse‑potential fitting
- Role: scored (load-bearing)
- Action: Fit the 35 energy points from step_04 to the Morse function V(x) = V₀ { [1 − exp(−γ (x − x_min))]² − 1 } using a least‑squares procedure. Extract the well depth V₀ (au), shape parameter γ, equilibrium distance x_min (Å), and the root‑mean‑square deviation between the data and the fit. Write these four values to /app/outputs/step_05_morse_fit_params.json.
- Output file: `/app/outputs/step_05_morse_fit_params.json`
- Format: json
- Contract: {"V0_au": float, "gamma": float, "x_min_A": float, "rms_deviation_au": float}
- Scoring: scored by hidden verifier

### Step 6: WKB vibrational analysis
- Role: scored (load-bearing)
- Action: Using the fitted Morse potential from step_05 and the reduced mass μ = 7.3938 u for the intermolecular stretch, solve the WKB quantization integral numerically (e.g., via Newton–Raphson) to find all bound vibrational states. Output the number of bound states, the energy of each state (au), the fundamental excitation energy (1←0, cm⁻¹), the first overtone (2←0, cm⁻¹), and the zero‑point vibrational energy (ZPVE, kcal/mol relative to the potential minimum) to /app/outputs/step_06_wkb_energies.json.
- Output file: `/app/outputs/step_06_wkb_energies.json`
- Format: json
- Contract: {"n_bound_states": int, "energies_au": [float], "fundamental_cm-1": float, "first_overtone_cm-1": float, "zpve_kcal_mol": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_rotational_constants.json`
- `/app/outputs/step_03_interaction_energy.json`
- `/app/outputs/step_04_potential_curve.csv`
- `/app/outputs/step_05_morse_fit_params.json`
- `/app/outputs/step_06_wkb_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_rotational_constants.json
- path: `/app/outputs/step_02_rotational_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Rotational constants A, B, C in MHz computed from the optimized B3LYP geometry. The checker compares each to a hidden reference within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `A_MHz`: float
    - `B_MHz`: float
    - `C_MHz`: float

### step_03_interaction_energy.json
- path: `/app/outputs/step_03_interaction_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: BSSE‑ and ZPVE‑corrected dissociation energy D₀ in kcal/mol. The checker compares to the paper‑reported value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `D0_kcal_mol`: float

### step_04_potential_curve.csv
- path: `/app/outputs/step_04_potential_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Discrete intermolecular potential energy points (35 rows). The checker independently fits a Morse function from this data and compares the obtained parameters to a hidden standard.
- schema:
  - `type`: table
  - `required_columns`: `r_A`, `energy_au`
  - `units`:
    - `r_A`: Angstrom
    - `energy_au`: Hartree

### step_05_morse_fit_params.json
- path: `/app/outputs/step_05_morse_fit_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Morse potential parameters obtained by fitting the 35 DFT points. The checker either compares these directly to hidden references or refits independently from step_04.
- schema:
  - `type`: object
  - `required`:
    - `V0_au`: float
    - `gamma`: float
    - `x_min_A`: float
    - `rms_deviation_au`: float

### step_06_wkb_energies.json
- path: `/app/outputs/step_06_wkb_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: WKB bound vibrational states and excitation energies. The checker re‑solves the WKB integral from the agent‑submitted potential (step_04 or step_05) and compares the derived quantities against paper‑reported values.
- schema:
  - `type`: object
  - `required`:
    - `n_bound_states`: int
    - `energies_au`: list of float
    - `fundamental_cm-1`: float
    - `first_overtone_cm-1`: float
    - `zpve_kcal_mol`: float

Notes: All DFT calculations use standard B3LYP/6‑311++G(d,p); tolerances absorb the spread from using the standard functional instead of the paper's slightly modified Becke exchange. The reduced mass μ = 7.3938 u is a fixed input for the WKB step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_rotational_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A_MHz": "float",
          "B_MHz": "float",
          "C_MHz": "float"
        }
      },
      "description": "Rotational constants A, B, C in MHz computed from the optimized B3LYP geometry. The checker compares each to a hidden reference within a tolerance."
    },
    {
      "file": "step_03_interaction_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "D0_kcal_mol": "float"
        }
      },
      "description": "BSSE‑ and ZPVE‑corrected dissociation energy D₀ in kcal/mol. The checker compares to the paper‑reported value within a tolerance."
    },
    {
      "file": "step_04_potential_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_A",
          "energy_au"
        ],
        "units": {
          "r_A": "Angstrom",
          "energy_au": "Hartree"
        }
      },
      "description": "Discrete intermolecular potential energy points (35 rows). The checker independently fits a Morse function from this data and compares the obtained parameters to a hidden standard."
    },
    {
      "file": "step_05_morse_fit_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V0_au": "float",
          "gamma": "float",
          "x_min_A": "float",
          "rms_deviation_au": "float"
        }
      },
      "description": "Morse potential parameters obtained by fitting the 35 DFT points. The checker either compares these directly to hidden references or refits independently from step_04."
    },
    {
      "file": "step_06_wkb_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "n_bound_states": "int",
          "energies_au": "list of float",
          "fundamental_cm-1": "float",
          "first_overtone_cm-1": "float",
          "zpve_kcal_mol": "float"
        }
      },
      "description": "WKB bound vibrational states and excitation energies. The checker re‑solves the WKB integral from the agent‑submitted potential (step_04 or step_05) and compares the derived quantities against paper‑reported values."
    }
  ],
  "notes": "All DFT calculations use standard B3LYP/6‑311++G(d,p); tolerances absorb the spread from using the standard functional instead of the paper's slightly modified Becke exchange. The reduced mass μ = 7.3938 u is a fixed input for the WKB step."
}
```

## How you are scored
A hidden verifier reads each scored output file. For the rotational constants, interaction energy, and Morse parameters the verifier compares your numbers to independently obtained reference values using tolerances that account for the use of the standard B3LYP functional. The potential curve (step_04) is re‑fit to a Morse function and the resulting parameters and rms deviation are cross‑checked. From the same curve the verifier re‑solves the WKB integral and compares the number of bound states, excitation energies, and ZPVE to reference figures. Consistency checks (e.g., that the potential curve contains 35 points, that energies increase with vibrational quantum number, and that the fitted rms deviation is small) are also weighed. The final reward is a weighted combination of the per‑step scores.
