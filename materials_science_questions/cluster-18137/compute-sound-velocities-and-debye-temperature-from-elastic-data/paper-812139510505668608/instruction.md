# DFT Determination of Elastic and Thermal Properties of Hexagonal Fe2Mo

## Problem background
Laves phase Fe₂Mo is a hardening precipitate that forms in ferritic steels during long-term high-temperature service. Its structural, elastic and thermal properties directly affect alloy design and phase stability, yet experimental measurement is challenging because the phase exists in the low-temperature region of the Fe–Mo phase diagram where diffusion is slow and other intermetallic phases coexist. First-principles computations of the equilibrium structure, elastic constants, polycrystalline moduli, Debye temperature and anisotropic sound velocities provide access to these quantities and underpin thermodynamic modelling.

## Approach
All quantities are obtained from spin-polarized density functional theory (DFT) calculations using the generalized gradient approximation (GGA) of Perdew, Burke and Ernzerhof (PBE). The workflow uses the open-source Quantum ESPRESSO code with publicly available PBE pseudopotentials for Fe and Mo.

First, the hexagonal C14 unit cell (space group P6₃/mmc, 12 atoms) is fully relaxed to obtain the equilibrium lattice constants a, c, atomic positions and total magnetic moment. Reference total energies for the elemental ground states (bcc Fe, bcc Mo) are computed under the same settings; the formation enthalpy ΔH is then evaluated from the total energy of Fe₂Mo relative to the elemental references at the known composition (x_Mo = 1/3).

Elastic constants are extracted by applying five symmetric strain distortion matrices to the equilibrium lattice at a series of strain amplitudes δ, performing DFT total-energy calculations, and fitting the resulting ΔE(δ) curves to quadratic polynomials. The five independent elastic constants C11, C12, C13, C33, C44 and the dependent constant C66 are obtained by solving the resulting linear system. Polycrystalline elastic moduli (bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio ν) are computed from the single-crystal constants via the Voigt–Reuss–Hill (VRH) averaging scheme, together with shear anisotropy factors, directional linear bulk moduli and percentage anisotropy indices. Finally, the density is derived from the relaxed volume and formula mass, and the Debye temperature θD along with the polycrystalline and directional sound velocities along [001] and [100] are calculated using standard relations.

## Reproduction target
Using Quantum ESPRESSO with GGA‑PBE and the provided pseudopotentials, perform spin‑polarized DFT calculations to produce the following scored artifacts for hexagonal Fe₂Mo:

- `step_01_structure.json`: the optimized lattice parameters a, c, equilibrium volume V, the internal coordinate x of the 6h Fe site, the internal coordinate z of the 4f Mo site, and the total magnetic moment of the unit cell.
- `step_00_formation_enthalpy.json`: the formation enthalpy ΔH in kJ per mole of atoms.
- `step_02_elastic_constants.json`: the six elastic constants (C11, C12, C13, C33, C44, C66) in GPa.
- `step_03_polycrystalline_moduli.json`: the Voigt–Reuss–Hill bulk and shear moduli, Young's modulus, Poisson's ratio, B/G ratio, shear anisotropy factors A₁₀₀ and A₀₀₁, linear bulk moduli Bₐ and Bc, and the percentage anisotropies AB and AG together with the universal anisotropy index AU.
- `step_04_debye_sound_velocities.json`: the Debye temperature θD, the polycrystalline sound velocities (shear vₛ, longitudinal vₗ, average Vₘ), and the single‑crystal directional velocities for longitudinal and shear waves along [001] and [100].

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Fe PBE pseudopotential: https://www.quantum-espresso.org/pseudopotentials/
- Mo PBE pseudopotential: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: DFT geometry optimization of Fe2Mo
- Role: process
- Action: Perform spin-polarized DFT relaxation of the hexagonal Fe2Mo unit cell (space group P6_3/mmc, 12 atoms) using GGA-PBE, starting from the literature Wyckoff positions. Converge forces and stress below tight thresholds.
- Evidence: `/app/outputs/geometry_opt.log`

### Step 2: Report optimized structure and magnetic moments
- Role: scored
- Action: Extract the optimized lattice constants a, c, volume V, the 6h Fe x-coordinate, the 4f Mo z-coordinate, and the total cell magnetic moment from the geometry optimization and write them to step_01_structure.json.
- Output file: `/app/outputs/step_01_structure.json`
- Format: json
- Contract: {"a_angstrom": float, "c_angstrom": float, "V_angstrom3": float, "Fe_6h_x": float, "Mo_4f_z": float, "total_magnetic_moment_muB": float}
- Scoring: scored by hidden verifier

### Step 3: Reference total energies of bcc Fe and bcc Mo
- Role: process
- Action: Perform spin-polarized DFT total-energy calculations for bcc Fe and bcc Mo using the same pseudopotentials and computational settings. Obtain total energies per atom.
- Evidence: `/app/outputs/ref_energies.log`

### Step 4: Compute formation enthalpy
- Role: scored
- Action: Calculate the formation enthalpy ΔH of Fe2Mo from the total energy of the relaxed Fe2Mo cell and the per-atom energies of bcc Fe and bcc Mo, using the known Mo concentration (x_Mo = 1/3). Write the result to step_00_formation_enthalpy.json.
- Output file: `/app/outputs/step_00_formation_enthalpy.json`
- Format: json
- Contract: {"delta_H_kJ_per_mol": float}
- Scoring: scored by hidden verifier

### Step 5: DFT total-energy calculations for strained Fe2Mo cells
- Role: process
- Action: Apply the five symmetric strain distortion matrices D1–D5 to the equilibrium lattice vectors. For each distortion type, perform spin-polarized DFT total-energy calculations at a set of strain amplitudes δ. Store the total energies and strain values.
- Evidence: `/app/outputs/strain_energies.csv`

### Step 6: Extract single-crystal elastic constants
- Role: scored (load-bearing)
- Action: For each distortion, fit the strain energy ΔE(δ) to a quadratic polynomial to obtain the corresponding second-order coefficient. Solve the resulting linear system to obtain the five independent elastic constants C11, C12, C13, C33, C44 and the dependent constant C66. Write the values to step_02_elastic_constants.json.
- Output file: `/app/outputs/step_02_elastic_constants.json`
- Format: json
- Contract: {"C11_GPa": float, "C12_GPa": float, "C13_GPa": float, "C33_GPa": float, "C44_GPa": float, "C66_GPa": float}
- Scoring: scored by hidden verifier

### Step 7: Compute polycrystalline elastic moduli and anisotropy
- Role: scored
- Action: From the elastic constants, compute the Voigt, Reuss, and Hill bulk modulus B and shear modulus G, Young's modulus E, Poisson's ratio ν, B/G ratio, shear anisotropy factors A100 and A001, linear bulk moduli Ba and Bc, percentage anisotropies AB and AG, and the universal anisotropy index AU. Output all quantities to step_03_polycrystalline_moduli.json.
- Output file: `/app/outputs/step_03_polycrystalline_moduli.json`
- Format: json
- Contract: {"B_GPa": float, "G_GPa": float, "E_GPa": float, "nu": float, "B_G_ratio": float, "A_100": float, "A_001": float, "B_a_GPa": float, "B_c_GPa": float, "A_B_percent": float, "A_G_percent": float, "A_U": float}
- Scoring: scored by hidden verifier

### Step 8: Compute Debye temperature and sound velocities
- Role: scored
- Action: Calculate the density ρ from the equilibrium volume and formula mass. Using the polycrystalline moduli B and G, compute the average, shear, and longitudinal sound velocities Vm, vs, vl and the Debye temperature θD. Also compute directional sound velocities along [001] and [100] from the single-crystal elastic constants. Write the results to step_04_debye_sound_velocities.json.
- Output file: `/app/outputs/step_04_debye_sound_velocities.json`
- Format: json
- Contract: {"theta_D_K": float, "v_s_m_per_s": float, "v_l_m_per_s": float, "V_m_m_per_s": float, "v_l_001_m_per_s": float, "v_s_001_m_per_s": float, "v_l_100_m_per_s": float, "v_s1_100_m_per_s": float, "v_s2_100_m_per_s": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structure.json`
- `/app/outputs/step_00_formation_enthalpy.json`
- `/app/outputs/step_02_elastic_constants.json`
- `/app/outputs/step_03_polycrystalline_moduli.json`
- `/app/outputs/step_04_debye_sound_velocities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structure.json
- path: `/app/outputs/step_01_structure.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameters, atomic coordinate, and total magnetic moment from DFT relaxation.
- schema:
  - `type`: object
  - `required`:
    - `a_angstrom`: float
    - `c_angstrom`: float
    - `V_angstrom3`: float
    - `Fe_6h_x`: float
    - `Mo_4f_z`: float
    - `total_magnetic_moment_muB`: float

### step_00_formation_enthalpy.json
- path: `/app/outputs/step_00_formation_enthalpy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation enthalpy of Fe2Mo computed from total energies.
- schema:
  - `type`: object
  - `required`:
    - `delta_H_kJ_per_mol`: float

### step_02_elastic_constants.json
- path: `/app/outputs/step_02_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single-crystal elastic constants extracted from strain-energy fits.
- schema:
  - `type`: object
  - `required`:
    - `C11_GPa`: float
    - `C12_GPa`: float
    - `C13_GPa`: float
    - `C33_GPa`: float
    - `C44_GPa`: float
    - `C66_GPa`: float

### step_03_polycrystalline_moduli.json
- path: `/app/outputs/step_03_polycrystalline_moduli.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Polycrystalline elastic moduli and anisotropy indices derived from the single-crystal elastic constants.
- schema:
  - `type`: object
  - `required`:
    - `B_GPa`: float
    - `G_GPa`: float
    - `E_GPa`: float
    - `nu`: float
    - `B_G_ratio`: float
    - `A_100`: float
    - `A_001`: float
    - `B_a_GPa`: float
    - `B_c_GPa`: float
    - `A_B_percent`: float
    - `A_G_percent`: float
    - `A_U`: float

### step_04_debye_sound_velocities.json
- path: `/app/outputs/step_04_debye_sound_velocities.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Debye temperature, polycrystalline sound velocities, and directional sound velocities along [001] and [100].
- schema:
  - `type`: object
  - `required`:
    - `theta_D_K`: float
    - `v_s_m_per_s`: float
    - `v_l_m_per_s`: float
    - `V_m_m_per_s`: float
    - `v_l_001_m_per_s`: float
    - `v_s_001_m_per_s`: float
    - `v_l_100_m_per_s`: float
    - `v_s1_100_m_per_s`: float
    - `v_s2_100_m_per_s`: float

Notes: The checker compares the agent’s reported values against the paper’s DFT results with tolerances appropriate for a different code (Quantum ESPRESSO instead of WIEN2k). For polycrystalline moduli and sound velocities it recomputes the values from the agent’s Cij and lattice parameters, then compares to the paper’s reported polycrystalline properties. Mechanical stability criteria on Cij are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a_angstrom": "float",
          "c_angstrom": "float",
          "V_angstrom3": "float",
          "Fe_6h_x": "float",
          "Mo_4f_z": "float",
          "total_magnetic_moment_muB": "float"
        }
      },
      "description": "Optimized lattice parameters, atomic coordinate, and total magnetic moment from DFT relaxation."
    },
    {
      "file": "step_00_formation_enthalpy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_H_kJ_per_mol": "float"
        }
      },
      "description": "Formation enthalpy of Fe2Mo computed from total energies."
    },
    {
      "file": "step_02_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11_GPa": "float",
          "C12_GPa": "float",
          "C13_GPa": "float",
          "C33_GPa": "float",
          "C44_GPa": "float",
          "C66_GPa": "float"
        }
      },
      "description": "Single-crystal elastic constants extracted from strain-energy fits."
    },
    {
      "file": "step_03_polycrystalline_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "B_GPa": "float",
          "G_GPa": "float",
          "E_GPa": "float",
          "nu": "float",
          "B_G_ratio": "float",
          "A_100": "float",
          "A_001": "float",
          "B_a_GPa": "float",
          "B_c_GPa": "float",
          "A_B_percent": "float",
          "A_G_percent": "float",
          "A_U": "float"
        }
      },
      "description": "Polycrystalline elastic moduli and anisotropy indices derived from the single-crystal elastic constants."
    },
    {
      "file": "step_04_debye_sound_velocities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "theta_D_K": "float",
          "v_s_m_per_s": "float",
          "v_l_m_per_s": "float",
          "V_m_m_per_s": "float",
          "v_l_001_m_per_s": "float",
          "v_s_001_m_per_s": "float",
          "v_l_100_m_per_s": "float",
          "v_s1_100_m_per_s": "float",
          "v_s2_100_m_per_s": "float"
        }
      },
      "description": "Debye temperature, polycrystalline sound velocities, and directional sound velocities along [001] and [100]."
    }
  ],
  "notes": "The checker compares the agent’s reported values against the paper’s DFT results with tolerances appropriate for a different code (Quantum ESPRESSO instead of WIEN2k). For polycrystalline moduli and sound velocities it recomputes the values from the agent’s Cij and lattice parameters, then compares to the paper’s reported polycrystalline properties. Mechanical stability criteria on Cij are also verified."
}
```

## How you are scored
A hidden verifier reads each JSON output file and scores it against the paper's reference values using tolerances appropriate for a different DFT implementation (Quantum ESPRESSO instead of the original WIEN2k). Mechanical stability criteria (C11>0, C11−|C12|>0, (C11+C12)C33 − 2C13² > 0, C44>0) are checked automatically. For the polycrystalline moduli and the sound velocities, the verifier recomputes the quantities directly from your own submitted elastic constants and lattice parameters and then compares the recomputed values to the paper's polycrystalline results. The final score is a weighted combination across all scored artifacts; reporting a numeric value without executing the required DFT calculations will not satisfy the verifier.
