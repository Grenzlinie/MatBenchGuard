# DFT‑based prediction of mechanical and lattice dynamic properties of a cubic dihydride

## Problem background
Lutetium dihydride (LuH₂) with the cubic fluorite (CaF₂) structure is a candidate for hydrogen storage applications. Its mechanical strength, elastic behaviour under load, lattice stability, and thermal properties are not fully characterised by first-principles theory. A systematic computational prediction of the structural, elastic, tensile, phonon, and thermodynamic properties at ambient pressure can fill this gap and provide reference data for future studies. This task requires a first-principles density functional theory (DFT) investigation of these properties.

## Approach
Use plane-wave density functional theory with the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional and the projector augmented-wave (PAW) method to treat electron–ion interactions. First, build the fluorite LuH₂ unit cell and relax the structure with variable-cell optimisation to obtain the equilibrium lattice parameter. Then, apply the strain–energy method to compute the three independent single‑crystal elastic constants (C₁₁, C₁₂, C₄₄) for the cubic phase. From these, derive the Voigt–Reuss–Hill polycrystalline moduli (bulk, shear, Young’s) and the Pugh ratio G/B and Poisson’s ratio, and compute derived quantities: density, sound velocities, Debye temperature, and Vickers hardness. Next, simulate uniaxial tension along the [100] direction by incrementally increasing strain and calculating stress via the energy derivative to extract the ideal tensile strength and failure strain. For lattice dynamics, construct a 2 × 2 × 2 supercell and compute the phonon dispersion and density of states using both density functional perturbation theory (DFPT) and the finite‑displacement method. From these, determine the zone‑center optical mode frequencies: the infrared‑active T₁ᵤ mode and the Raman‑active T₂₉ mode. Finally, use the phonon density of states and the quasi‑harmonic approximation (QHA) to compute the lattice entropy and constant‑volume heat capacity as functions of temperature up to 1500 K. A suitable open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) with the PBE PAW pseudopotentials, together with the phonopy package for finite‑displacement phonon calculations, can be used.

## Reproduction target
Compute the following properties for LuH₂ in the fluorite structure using density functional theory with the PBE functional:
- Equilibrium lattice parameter (a₀) after variable‑cell structure relaxation.
- Single‑crystal elastic constants C₁₁, C₁₂, C₄₄ via the strain–energy method.
- Polycrystalline moduli (Voigt–Reuss–Hill bulk, shear, Young’s moduli, Poisson’s ratio, and G/B ratio).
- Derived sound velocities, Debye temperature, and Vickers hardness.
- Ideal tensile strength and failure strain along the [100] direction from a DFT tensile test.
- Zone‑center optical phonon frequencies (T₁ᵤ and T₂₉) from both DFPT and finite‑displacement calculations.
- Lattice entropy and constant‑volume heat capacity as functions of temperature (0–1500 K) obtained from the quasi‑harmonic approximation.
All results must be provided in the specified output files with the declared schemas.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Standard Solid-State Pseudopotentials (SSSP) library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT structure optimization and lattice parameter
- Role: scored (load-bearing)
- Action: Build the fluorite LuH₂ unit cell (space group Fm‑3m) and perform variable‑cell relaxation using DFT‑PBE. Extract the equilibrium lattice parameter.
- Output file: `/app/outputs/step_01_lattice_parameter.txt`
- Format: txt
- Contract: Single line: lattice_parameter_angstrom = <float>
- Scoring: scored by hidden verifier

### Step 2: Elastic constants calculation
- Role: scored (load-bearing)
- Action: Using the relaxed structure, apply the strain‑energy method to compute the single‑crystal elastic constants C₁₁, C₁₂ and C₄₄.
- Output file: `/app/outputs/step_02_elastic_constants.json`
- Format: json
- Contract: {"C11_GPa": <number>, "C12_GPa": <number>, "C44_GPa": <number>}
- Scoring: scored by hidden verifier

### Step 3: Polycrystalline moduli and mechanical indicators
- Role: scored
- Action: From the elastic constants and lattice parameter, compute Voigt‑Reuss‑Hill averaged bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio, and the G/B (Pugh) ratio.
- Output file: `/app/outputs/step_03_polycrystalline_moduli.json`
- Format: json
- Contract: {"B_VRH_GPa":<number>, "G_VRH_GPa":<number>, "E_VRH_GPa":<number>, "Poisson_ratio":<number>, "G_B_ratio":<number>}
- Scoring: scored by hidden verifier

### Step 4: Derived sound velocities, Debye temperature, and hardness
- Role: scored
- Action: Using the elastic moduli and density, compute shear, compressional and average sound velocities, Debye temperature via the average velocity, and Vickers hardness using Chen’s model.
- Output file: `/app/outputs/step_07_derived_properties.json`
- Format: json
- Contract: {"Vs_km_s":<number>, "Vp_km_s":<number>, "Vm_km_s":<number>, "Debye_temperature_K":<number>, "Hardness_Hv_GPa":<number>}
- Scoring: scored by hidden verifier

### Step 5: Ideal tensile strength along [100]
- Role: scored (load-bearing)
- Action: Perform a uniaxial tensile test along the [100] direction using DFT by incrementally increasing strain and computing stress from the energy derivative. Obtain the ideal tensile strength and failure strain.
- Output file: `/app/outputs/step_04_tensile_strength.json`
- Format: json
- Contract: {"direction":"[100]", "ideal_tensile_strength_GPa":<number>, "failure_strain_percent":<number>}
- Scoring: scored by hidden verifier

### Step 6: Phonon dispersion and density of states (DFPT + finite displacement)
- Role: process
- Action: Build a 2×2×2 supercell and compute phonon dispersion and partial density of states using both DFPT (Quantum ESPRESSO ph.x) and the finite displacement method with phonopy. Save the generated phonon density of states.
- Evidence: `/app/outputs/phonon_DOS.dat`

### Step 7: Zone‑center phonon frequencies
- Role: scored (load-bearing)
- Action: From the phonon results, extract the frequencies of the Infrared‑active (T₁ᵤ) and Raman‑active (T₂₉) modes at the Γ point for both DFPT and finite displacement methods.
- Output file: `/app/outputs/step_05_phonon_frequencies.json`
- Format: json
- Contract: {"T1u_DFPT_THz":<number>, "T1u_finite_displacement_THz":<number>, "T2g_DFPT_THz":<number>, "T2g_finite_displacement_THz":<number>}
- Scoring: scored by hidden verifier

### Step 8: Lattice thermodynamic properties (QHA)
- Role: scored (load-bearing)
- Action: From the phonon density of states, compute the lattice entropy and constant‑volume heat capacity as functions of temperature up to 1500 K using the quasi‑harmonic approximation. Output a CSV with at least 30 points.
- Output file: `/app/outputs/step_06_thermodynamic_properties.csv`
- Format: csv
- Contract: columns: temperature_K, entropy_J_per_mol_K, heat_capacity_Cv_J_per_mol_K; rows from 0 K to 1500 K, at least 30 points
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_parameter.txt`
- `/app/outputs/step_02_elastic_constants.json`
- `/app/outputs/step_03_polycrystalline_moduli.json`
- `/app/outputs/step_07_derived_properties.json`
- `/app/outputs/step_04_tensile_strength.json`
- `/app/outputs/step_05_phonon_frequencies.json`
- `/app/outputs/step_06_thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_parameter.txt
- path: `/app/outputs/step_01_lattice_parameter.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice parameter a₀ (Å) from DFT variable‑cell relaxation.
- schema:
  - `type`: text
  - `required`: lattice_parameter_angstrom

### step_02_elastic_constants.json
- path: `/app/outputs/step_02_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single‑crystal elastic constants C₁₁, C₁₂, C₄₄ in GPa.
- schema:
  - `type`: object
  - `required`:
    - `C11_GPa`: number
    - `C12_GPa`: number
    - `C44_GPa`: number

### step_03_polycrystalline_moduli.json
- path: `/app/outputs/step_03_polycrystalline_moduli.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Voigt‑Reuss‑Hill polycrystalline moduli, brittleness indicators, and directional Young's modulus values along [100], [110], [111]. The checker recomputes all quantities from the submitted elastic constants and verifies consistency.
- schema:
  - `type`: object
  - `required`:
    - `B_VRH_GPa`: number
    - `G_VRH_GPa`: number
    - `E_VRH_GPa`: number
    - `Poisson_ratio`: number
    - `G_B_ratio`: number
    - `E_100_GPa`: number
    - `E_110_GPa`: number
    - `E_111_GPa`: number

### step_07_derived_properties.json
- path: `/app/outputs/step_07_derived_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Sound velocities, Debye temperature, and Vickers hardness derived from elastic moduli.
- schema:
  - `type`: object
  - `required`:
    - `Vs_km_s`: number
    - `Vp_km_s`: number
    - `Vm_km_s`: number
    - `Debye_temperature_K`: number
    - `Hardness_Hv_GPa`: number

### step_04_tensile_strength.json
- path: `/app/outputs/step_04_tensile_strength.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ideal tensile strength and strain at failure for the [100] direction from DFT stress‑strain simulation.
- schema:
  - `type`: object
  - `required`:
    - `direction`: string
    - `ideal_tensile_strength_GPa`: number
    - `failure_strain_percent`: number

### step_05_phonon_frequencies.json
- path: `/app/outputs/step_05_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Γ‑point optical phonon frequencies (T₁ᵤ and T₂₉) from DFPT and finite‑displacement methods.
- schema:
  - `type`: object
  - `required`:
    - `T1u_DFPT_THz`: number
    - `T1u_finite_displacement_THz`: number
    - `T2g_DFPT_THz`: number
    - `T2g_finite_displacement_THz`: number

### step_06_thermodynamic_properties.csv
- path: `/app/outputs/step_06_thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Lattice entropy and constant‑volume heat capacity vs temperature up to 1500 K. Checked for monotonic increase and approach to the Dulong‑Petit limit.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `entropy_J_per_mol_K`, `heat_capacity_Cv_J_per_mol_K`
  - `min_rows`: 30

Notes: All quantities correspond to the cubic fluorite phase of the dihydride. The phonon DOS generated in the process step is required for the phonon frequency and thermodynamic steps. The checker applies appropriate tolerances for DFT code variations and validates internal consistency of polycrystalline moduli and directional Young's modulus values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_parameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": "lattice_parameter_angstrom"
      },
      "description": "Equilibrium lattice parameter a₀ (Å) from DFT variable‑cell relaxation."
    },
    {
      "file": "step_02_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11_GPa": "number",
          "C12_GPa": "number",
          "C44_GPa": "number"
        }
      },
      "description": "Single‑crystal elastic constants C₁₁, C₁₂, C₄₄ in GPa."
    },
    {
      "file": "step_03_polycrystalline_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "B_VRH_GPa": "number",
          "G_VRH_GPa": "number",
          "E_VRH_GPa": "number",
          "Poisson_ratio": "number",
          "G_B_ratio": "number",
          "E_100_GPa": "number",
          "E_110_GPa": "number",
          "E_111_GPa": "number"
        }
      },
      "description": "Voigt‑Reuss‑Hill polycrystalline moduli, brittleness indicators, and directional Young's modulus values along [100], [110], [111]. The checker recomputes all quantities from the submitted elastic constants and verifies consistency."
    },
    {
      "file": "step_07_derived_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Vs_km_s": "number",
          "Vp_km_s": "number",
          "Vm_km_s": "number",
          "Debye_temperature_K": "number",
          "Hardness_Hv_GPa": "number"
        }
      },
      "description": "Sound velocities, Debye temperature, and Vickers hardness derived from elastic moduli."
    },
    {
      "file": "step_04_tensile_strength.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "direction": "string",
          "ideal_tensile_strength_GPa": "number",
          "failure_strain_percent": "number"
        }
      },
      "description": "Ideal tensile strength and strain at failure for the [100] direction from DFT stress‑strain simulation."
    },
    {
      "file": "step_05_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T1u_DFPT_THz": "number",
          "T1u_finite_displacement_THz": "number",
          "T2g_DFPT_THz": "number",
          "T2g_finite_displacement_THz": "number"
        }
      },
      "description": "Γ‑point optical phonon frequencies (T₁ᵤ and T₂₉) from DFPT and finite‑displacement methods."
    },
    {
      "file": "step_06_thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "entropy_J_per_mol_K",
          "heat_capacity_Cv_J_per_mol_K"
        ],
        "min_rows": 30
      },
      "description": "Lattice entropy and constant‑volume heat capacity vs temperature up to 1500 K. Checked for monotonic increase and approach to the Dulong‑Petit limit."
    }
  ],
  "notes": "All quantities correspond to the cubic fluorite phase of the dihydride. The phonon DOS generated in the process step is required for the phonon frequency and thermodynamic steps. The checker applies appropriate tolerances for DFT code variations and validates internal consistency of polycrystalline moduli and directional Young's modulus values."
}
```

## How you are scored
Each scored output file in the workflow is evaluated independently by a hidden verifier. The verifier checks your submitted numbers against reference values derived from the original paper, consistency relations between artifacts (e.g., bulk modulus recomputed from elastic constants), and physical constraints (e.g., monotonic heat capacity, the correct ordering of phonon frequencies). For thermodynamic curves, the verifier inspects the shape, monotonicity, and approach to the Dulong–Petit limit. Each stage carries a weight, and your final reward is the weighted sum of stage scores, all in the range [0,1]. The verifier does not accept the paper’s reported numbers alone; it verifies that you have actually performed the required calculations and produced consistent, physically plausible results.
