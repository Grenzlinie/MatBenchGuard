# First‑Principles Determination of Elastic and Thermodynamic Properties for Two Tetragonal 122 Intermetallics

## Problem background
The two intermetallics LaNi₂P₂ and LaNi₂Ge₂ crystallise in the tetragonal ThCr₂Si₂‑type structure (space group I4/mmm). Understanding their elastic and thermodynamic properties is important for assessing mechanical stability, chemical bonding, and potential applications. This task requires you to determine those properties from first principles: you will compute the complete set of elastic constants, polycrystalline moduli, sound velocities, Debye temperature, and low-temperature heat capacity for both compounds.

## Approach
You will use density functional theory (DFT) with the GGA‑PBE exchange‑correlation functional. First, fully relax the crystal structures of LaNi₂P₂ and LaNi₂Ge₂. On the relaxed geometries, apply a series of small volume‑conserving strains and calculate the resulting stress tensors to extract the six independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆ for the tetragonal lattice. Perform a separate density‑of‑states calculation on the relaxed structures to obtain the electronic density of states at the Fermi level and the corresponding Sommerfeld coefficient γ. From the elastic constants and the crystallographic density, you will derive the polycrystalline bulk modulus B and shear modulus G in the Voigt, Reuss, and Voigt‑Reuss‑Hill averaging schemes, as well as Young's modulus, Poisson's ratio, and the Pugh ratio G/B. Using the polycrystalline moduli and density, compute the longitudinal, transverse, and mean sound velocities and the Debye temperature θD. Finally, combine γ with the lattice heat‑capacity coefficient β (obtained from θD) to evaluate the low‑temperature heat capacity Cp(T) = γT + βT³ at several low temperatures. An open‑source DFT code (e.g., Quantum ESPRESSO) and standard GGA‑PBE pseudopotentials are required.

## Reproduction target
Produce a JSON file, elastic_and_moduli.json, that contains for each compound the six elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆ (in GPa), the Voigt, Reuss, and Voigt‑Reuss‑Hill averaged bulk and shear moduli, Young's modulus, Poisson's ratio, the G/B ratio, the crystallographic density, and the molar mass. Produce a second JSON file, thermophysical.json, that contains for each compound the longitudinal, transverse, and mean sound velocities (in m/s), the Debye temperature (in K), and the low‑temperature heat capacity Cp at 10, 20, 50, 100, and 150 K (in J mol⁻¹ K⁻¹). All quantities must be computed from the relaxed structures, the DFT‑derived elastic constants, and the electronic density of states.

## Assets

- Open‑source DFT code (e.g., Quantum ESPRESSO or ABINIT): https://www.quantum-espresso.org
- GGA‑PBE pseudopotentials (e.g., SSSP efficiency or GBRV library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python packages (numpy, scipy, json): numpy scipy
- Initial crystal structures of LaNi₂P₂ and LaNi₂Ge₂

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for LaNi₂P₂ and LaNi₂Ge₂ using GGA‑PBE to obtain equilibrium lattice parameters, cell volume, and internal coordinate z. Record the optimized structures.
- Evidence: `/app/outputs/geometry_opt.log`

### Step 2: Elastic constants calculation
- Role: process
- Action: Using the optimized structures, compute the six independent elastic constants C11, C12, C13, C33, C44, C66 via the volume‑conserving strain‑stress method. Output the raw Cij values.
- Evidence: `/app/outputs/Cij_values.json`

### Step 3: Electronic DOS calculation
- Role: process
- Action: Perform a DFT density‑of‑states calculation on the optimized structures to obtain the total DOS at the Fermi level N(E_F) and the Sommerfeld coefficient γ = (π²/3)k_B² N(E_F) per formula unit.
- Evidence: `/app/outputs/dos_data.json`

### Step 4: Polycrystalline moduli and elastic properties
- Role: scored
- Action: From the elastic constants, density, and molar mass, compute the Voigt, Reuss, and Voigt‑Reuss‑Hill bulk modulus B and shear modulus G, Young's modulus Y, Poisson's ratio ν, and the G/B ratio. Include the original Cij values. Write the results to elastic_and_moduli.json.
- Output file: `/app/outputs/elastic_and_moduli.json`
- Format: json
- Contract: Object with keys "LaNi2P2" and "LaNi2Ge2", each containing numeric fields: C11, C12, C13, C33, C44, C66 (all in GPa), B_V, B_R, B_VRH, G_V, G_R, G_VRH, Y, nu, G_over_B, density_gcm3, molar_mass_gmol.
- Scoring: scored by hidden verifier

### Step 5: Sound velocities, Debye temperature and heat capacity
- Role: scored (load-bearing)
- Action: Using the polycrystalline moduli (e.g., B_V, G_V), density, and γ, compute longitudinal, transverse, and average sound velocities, the Debye temperature θ_D, and the low‑temperature heat capacity C_p(T) = γT + βT³ for T = 10, 20, 50, 100, 150 K. Write the results to thermophysical.json.
- Output file: `/app/outputs/thermophysical.json`
- Format: json
- Contract: Object with keys "LaNi2P2" and "LaNi2Ge2", each containing: v_l (m/s), v_t (m/s), v_m (m/s), theta_D (K), and "heat_capacity": array of {"T": float (K), "Cp": float (J/(mol·K))} for temperatures 10, 20, 50, 100, 150 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_and_moduli.json`
- `/app/outputs/thermophysical.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_and_moduli.json
- path: `/app/outputs/elastic_and_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constants, polycrystalline moduli, and derived engineering properties for both intermetallics.
- schema:
  - `type`: object
  - `required`:
    - `LaNi2P2`:
      - `C11`: float (GPa)
      - `C12`: float (GPa)
      - `C13`: float (GPa)
      - `C33`: float (GPa)
      - `C44`: float (GPa)
      - `C66`: float (GPa)
      - `B_V`: float (GPa)
      - `B_R`: float (GPa)
      - `B_VRH`: float (GPa)
      - `G_V`: float (GPa)
      - `G_R`: float (GPa)
      - `G_VRH`: float (GPa)
      - `Y`: float (GPa)
      - `nu`: float
      - `G_over_B`: float
      - `density_gcm3`: float (g/cm³)
      - `molar_mass_gmol`: float (g/mol)
    - `LaNi2Ge2`:
      - `C11`: float (GPa)
      - `C12`: float (GPa)
      - `C13`: float (GPa)
      - `C33`: float (GPa)
      - `C44`: float (GPa)
      - `C66`: float (GPa)
      - `B_V`: float (GPa)
      - `B_R`: float (GPa)
      - `B_VRH`: float (GPa)
      - `G_V`: float (GPa)
      - `G_R`: float (GPa)
      - `G_VRH`: float (GPa)
      - `Y`: float (GPa)
      - `nu`: float
      - `G_over_B`: float
      - `density_gcm3`: float (g/cm³)
      - `molar_mass_gmol`: float (g/mol)

### thermophysical.json
- path: `/app/outputs/thermophysical.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Sound velocities, Debye temperature, and low‑temperature heat capacity for both intermetallics.
- schema:
  - `type`: object
  - `required`:
    - `LaNi2P2`:
      - `v_l`: float (m/s)
      - `v_t`: float (m/s)
      - `v_m`: float (m/s)
      - `theta_D`: float (K)
      - `heat_capacity`: array of {"T": float (K), "Cp": float (J/(mol·K))}
    - `LaNi2Ge2`:
      - `v_l`: float (m/s)
      - `v_t`: float (m/s)
      - `v_m`: float (m/s)
      - `theta_D`: float (K)
      - `heat_capacity`: array of {"T": float (K), "Cp": float (J/(mol·K))}

Notes: The hidden checker will compare the reported elastic constants, moduli, sound velocities, and Debye temperature against paper‑derived reference values with appropriate tolerances, and will verify that the heat capacity satisfies the expected trend (C_p(LaNi₂Ge₂) > C_p(LaNi₂P₂) at each temperature).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_and_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LaNi2P2": {
            "C11": "float (GPa)",
            "C12": "float (GPa)",
            "C13": "float (GPa)",
            "C33": "float (GPa)",
            "C44": "float (GPa)",
            "C66": "float (GPa)",
            "B_V": "float (GPa)",
            "B_R": "float (GPa)",
            "B_VRH": "float (GPa)",
            "G_V": "float (GPa)",
            "G_R": "float (GPa)",
            "G_VRH": "float (GPa)",
            "Y": "float (GPa)",
            "nu": "float",
            "G_over_B": "float",
            "density_gcm3": "float (g/cm³)",
            "molar_mass_gmol": "float (g/mol)"
          },
          "LaNi2Ge2": {
            "C11": "float (GPa)",
            "C12": "float (GPa)",
            "C13": "float (GPa)",
            "C33": "float (GPa)",
            "C44": "float (GPa)",
            "C66": "float (GPa)",
            "B_V": "float (GPa)",
            "B_R": "float (GPa)",
            "B_VRH": "float (GPa)",
            "G_V": "float (GPa)",
            "G_R": "float (GPa)",
            "G_VRH": "float (GPa)",
            "Y": "float (GPa)",
            "nu": "float",
            "G_over_B": "float",
            "density_gcm3": "float (g/cm³)",
            "molar_mass_gmol": "float (g/mol)"
          }
        }
      },
      "description": "Elastic constants, polycrystalline moduli, and derived engineering properties for both intermetallics."
    },
    {
      "file": "thermophysical.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LaNi2P2": {
            "v_l": "float (m/s)",
            "v_t": "float (m/s)",
            "v_m": "float (m/s)",
            "theta_D": "float (K)",
            "heat_capacity": "array of {\"T\": float (K), \"Cp\": float (J/(mol·K))}"
          },
          "LaNi2Ge2": {
            "v_l": "float (m/s)",
            "v_t": "float (m/s)",
            "v_m": "float (m/s)",
            "theta_D": "float (K)",
            "heat_capacity": "array of {\"T\": float (K), \"Cp\": float (J/(mol·K))}"
          }
        }
      },
      "description": "Sound velocities, Debye temperature, and low‑temperature heat capacity for both intermetallics."
    }
  ],
  "notes": "The hidden checker will compare the reported elastic constants, moduli, sound velocities, and Debye temperature against paper‑derived reference values with appropriate tolerances, and will verify that the heat capacity satisfies the expected trend (C_p(LaNi₂Ge₂) > C_p(LaNi₂P₂) at each temperature)."
}
```

## How you are scored
A hidden, automated verifier will independently examine your two output files. For each pipeline stage it will compare the values you report against reference data that were derived from the same computational protocol. The verifier will verify that your elastic constants and moduli lie within expected physical ranges, that the derived quantities are internally consistent, and that the correct trends between the two compounds are observed. The overall reward is a weighted combination of the per‑stage scores, with the thermophysical properties carrying the highest weight. Simply quoting a number without actually executing the DFT workflow will not satisfy the check.
