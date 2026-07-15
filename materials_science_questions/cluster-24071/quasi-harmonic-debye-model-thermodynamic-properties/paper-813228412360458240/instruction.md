## Problem background

The cubic antiperovskite compound InNCe₃ (space group Pm-3m) is a ternary nitride with potential for interesting mechanical and thermal properties. Determining its elastic constants, sound velocities, Debye temperature, and finite‑temperature thermodynamic behaviour provides reference data where experimental measurements are scarce. First‑principles calculations together with the quasi‑harmonic Debye model allow these quantities to be predicted from the crystal structure alone.

## Approach

The task follows a computational workflow that combines first‑principles density‑functional‑theory (DFT) total‑energy calculations with numerical post‑processing:

1. **DFT energy–volume (E–V) curve**: For the given cubic crystal structure, compute total energies at a range of lattice constants to produce a set of (V, E) points.
2. **Equation of state (EOS) fit**: Fit the E(V) data to the Birch–Murnaghan EOS to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative.
3. **Elastic constants**: At the equilibrium volume, apply volume‑conserving strains (orthorhombic/monoclinic) and recompute energies; extract the three independent elastic constants C₁₁, C₁₂, C₄₄ from the strain–energy relations.
4. **Polycrystalline sound velocities and Debye temperature**: From the elastic constants and the crystal density, compute the isotropic bulk and shear moduli (Voigt–Reuss–Hill), then the longitudinal (vₗ), transverse (vₜ), and average (vₘ) sound velocities. Derive the Debye temperature from the average sound velocity using the standard formula.
5. **Quasi‑harmonic Debye model**: Using the E(V) data and Poisson’s ratio (from the elastic constants), implement the quasi‑harmonic Debye model. Minimise the non‑equilibrium Gibbs function G*(V;P,T) at zero pressure to obtain the thermal equation of state, and evaluate the heat capacity at constant volume C_V at 1000 K, the Debye temperature at 300 K, and the volume thermal expansion coefficient α at 300 K.

The work is purely computational. The required DFT functional is the local density approximation (LSDA, Perdew–Wang). The agent may use any open‑source DFT code capable of total‑energy calculations (e.g., Quantum ESPRESSO, Elk) and implement the Debye model in Python.

## Reproduction target

- Compute the **zero‑pressure elastic constants** C₁₁, C₁₂, C₄₄ (in GPa).
- Compute the **polycrystalline longitudinal, transverse, and average sound velocities** (vₗ, vₜ, vₘ, in m s⁻¹) and the **Debye temperature from elastic constants** θ_D,el (in K).
- From the **quasi‑harmonic Debye model at zero pressure**, compute:
  - C_V at 1000 K (J mol⁻¹ K⁻¹)
  - Debye temperature at 300 K (K)
  - thermal expansion coefficient α at 300 K (K⁻¹)

These quantities correspond to the main mechanical and thermodynamic predictions for cubic InNCe₃. The hidden grader will compare the submitted numerical values against the paper’s reference results within appropriate tolerances.

## Assets

The following non‑paper resources are required. Obtain them at runtime:

- **Open‑source DFT code** (e.g., Elk  – https://elk.sourceforge.io, Quantum ESPRESSO – https://www.quantum-espresso.org). The code must support LSDA total‑energy calculations.
- **Python 3** with `numpy` and `scipy` for fitting, elastic‑constant extraction, sound‑velocity calculation, and implementation of the quasi‑harmonic Debye model.

NO external datasets, pretrained models, or proprietary software are needed.

## Workflow steps

### Step 1: DFT energy–volume curve
- Role: process
- Action: Perform DFT total‑energy calculations for the cubic InNCe₃ structure (space group Pm‑3m, Wyckoff positions: In 1a (0,0,0), N 1b (0.5,0.5,0.5), Ce 3c (0,0.5,0.5)) at a range of lattice constants. Use the local density approximation (LSDA) functional. Output a file containing the computed energy vs. volume data points.
- Evidence: `/app/outputs/E_V_data.json`

### Step 2: Birch–Murnaghan EOS fit
- Role: process
- Action: Fit the E(V) data from Step 1 to the Birch–Murnaghan equation of state to obtain the equilibrium lattice constant a₀, the zero‑pressure bulk modulus B₀, and its pressure derivative B′. Save these equilibrium properties.
- Evidence: `/app/outputs/equilibrium_props.json`

### Step 3: Elastic constants calculation
- Role: scored
- Action: At the equilibrium volume from Step 2, apply volume‑conserving orthorhombic and monoclinic strains, recompute the DFT total energies, and extract the three independent elastic constants C₁₁, C₁₂, C₄₄ from the strain–energy relations. Write the results in GPa.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: top‑level keys `C11`, `C12`, `C44` (each a float, unit GPa)
- Scoring: scored by hidden verifier

### Step 4: Polycrystalline sound velocities
- Role: scored
- Action: From the elastic constants and the crystal density (derived from the equilibrium lattice constant and the atomic masses), compute the polycrystalline bulk and shear moduli using the Voigt–Reuss–Hill approximation. Then calculate the longitudinal (vₗ), transverse (vₜ), and average (vₘ) sound velocities. Write the velocities in m s⁻¹.
- Output file: `/app/outputs/polycrystalline_sound_velocities.json`
- Format: json
- Contract: top‑level keys `v_l`, `v_t`, `v_m` (each a float, unit m s⁻¹)
- Scoring: scored by hidden verifier

### Step 5: Debye temperature from elastic constants
- Role: scored
- Action: Using the average sound velocity vₘ, the molecular mass, and the number of atoms per formula unit, compute the Debye temperature θ_D,el through the standard formula. Write the result in K.
- Output file: `/app/outputs/debye_temp_from_elastic.json`
- Format: json
- Contract: top‑level key `theta_D_el` (float, unit K)
- Scoring: scored by hidden verifier

### Step 6: Quasi‑harmonic Debye model thermodynamic properties
- Role: scored (load‑bearing)
- Action: Implement the quasi‑harmonic Debye model using the E(V) data from Step 1 and Poisson’s ratio derived from the elastic constants. Minimise the non‑equilibrium Gibbs function G*(V;P=0,T) to obtain the thermal equation of state. Extract the heat capacity at constant volume C_V at 1000 K, the Debye temperature at 300 K, and the volume thermal expansion coefficient α at 300 K (all at zero pressure). Write the results in J mol⁻¹ K⁻¹, K, and K⁻¹ respectively.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: top‑level keys `CV_1000K_0GPa` (float, J mol⁻¹ K⁻¹), `Debye_temp_300K_0GPa` (float, K), `alpha_300K_0GPa` (float, K⁻¹)
- Scoring: scored by hidden verifier

## Output files

The agent must place the following files under `/app/outputs`:
- `E_V_data.json` (evidence, not scored)
- `equilibrium_props.json` (evidence, not scored)
- `elastic_constants.json`
- `polycrystalline_sound_velocities.json`
- `debye_temp_from_elastic.json`
- `thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zero‑pressure elastic constants of cubic InNCe₃.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C44`: float (GPa)

### polycrystalline_sound_velocities.json
- path: `/app/outputs/polycrystalline_sound_velocities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline sound velocities derived from elastic constants.
- schema:
  - `type`: object
  - `required`:
    - `v_l`: float (m/s)
    - `v_t`: float (m/s)
    - `v_m`: float (m/s)

### debye_temp_from_elastic.json
- path: `/app/outputs/debye_temp_from_elastic.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Debye temperature derived from elastic constants.
- schema:
  - `type`: object
  - `required`:
    - `theta_D_el`: float (K)

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Quasi‑harmonic Debye model thermodynamic properties at 0 GPa.
- schema:
  - `type`: object
  - `required`:
    - `CV_1000K_0GPa`: float (J/(mol·K))
    - `Debye_temp_300K_0GPa`: float (K)
    - `alpha_300K_0GPa`: float (1/K)

Notes: All scored outputs are compared to the paper’s reported values with tolerances that allow for legitimate implementation differences (functional, code, pseudopotential). Evidence files (E_V_data.json, equilibrium_props.json) are not scored but must exist to demonstrate the workflow was followed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C44": "float (GPa)"
        }
      },
      "description": "Zero‑pressure elastic constants of cubic InNCe₃."
    },
    {
      "file": "polycrystalline_sound_velocities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "v_l": "float (m/s)",
          "v_t": "float (m/s)",
          "v_m": "float (m/s)"
        }
      },
      "description": "Polycrystalline sound velocities derived from elastic constants."
    },
    {
      "file": "debye_temp_from_elastic.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "theta_D_el": "float (K)"
        }
      },
      "description": "Debye temperature derived from elastic constants."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CV_1000K_0GPa": "float (J/(mol·K))",
          "Debye_temp_300K_0GPa": "float (K)",
          "alpha_300K_0GPa": "float (1/K)"
        }
      },
      "description": "Quasi‑harmonic Debye model thermodynamic properties at 0 GPa."
    }
  ],
  "notes": "All scored outputs are compared to the paper’s reported values with tolerances that allow for legitimate implementation differences (functional, code, pseudopotential). Evidence files (E_V_data.json, equilibrium_props.json) are not scored but must exist to demonstrate the workflow was followed."
}
```

## How you are scored

A hidden verifier independently reads the scored artifact files (`elastic_constants.json`, `polycrystalline_sound_velocities.json`, `debye_temp_from_elastic.json`, `thermodynamic_properties.json`) and compares each numerical value against a hidden reference (the paper’s reported result) with tolerances that account for legitimate implementation differences. The reward is a weighted combination of the per‑quantity agreement. Reporting a number without the supporting computational pipeline is not sufficient; the hidden verifier will only accept correctly formatted artifacts placed at the required paths.
