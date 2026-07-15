# Thermoelectric figure of merit of Janus gamma-Pb2SeTe monolayer from first principles

## Problem background
Thermoelectric materials can directly convert heat into electricity, with efficiency quantified by the dimensionless figure of merit ZT = (σ S² T) / (κ_e + κ_l), where σ is electrical conductivity, S the Seebeck coefficient, T temperature, κ_e and κ_l the electronic and lattice thermal conductivities. Two-dimensional (2D) Janus monolayers, which break structural symmetry by having different chalcogen atoms on opposite sides, are promising candidates for high-temperature thermoelectric applications. In this task, you will computationally determine the thermoelectric performance of the Janus gamma-Pb2SeTe monolayer: calculate its lattice thermal conductivity, electronic transport coefficients, and ZT at 800 K for p-type doping.

## Approach
The computational workflow proceeds in several stages. First, construct the atomic structure of the Janus gamma-Pb2SeTe monolayer (buckled honeycomb, Pb sandwiched between Se and Te) and optimize its geometry using density functional theory (DFT) with the PBE functional and a plane-wave basis set. Next, compute the harmonic and third-order interatomic force constants (IFCs) using finite-displacement supercell calculations; the harmonic IFCs are corrected to enforce rotational invariance, ensuring a quadratic ZA acoustic mode. Use the harmonic and anharmonic IFCs to solve the linearized phonon Boltzmann transport equation on a fine Q-grid and obtain the lattice thermal conductivity, applying a scaling factor (cross-plane height) to account for the 2D geometry. Separately, compute the electronic band structure; extract hole effective masses; apply uniaxial strains to determine deformation potentials; and combine these with elastic constants to compute the carrier mobility and relaxation time τ for holes using deformation potential theory. Then, using BoltzTraP2 under the constant relaxation time approximation, compute the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as functions of p-type carrier concentration at 800 K, scaling the outputs by the previously obtained τ. Finally, combine the lattice and electronic transport data to calculate ZT as a function of carrier concentration and identify the maximum ZT and the corresponding optimal hole concentration.

## Reproduction target
Produce the following three output files under /app/outputs: (i) step_01_lattice_thermal_conductivity.json containing the lattice thermal conductivity κ_l at 300 K and 800 K (units W m⁻¹ K⁻¹); (ii) step_02_electronic_transport.json containing an array of objects with Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as a function of p-type carrier concentration (cm⁻²) at 800 K; (iii) step_03_ZT_results.json containing the maximum dimensionless figure of merit ZT and the corresponding optimal carrier concentration for p-type gamma-Pb2SeTe at 800 K. All quantities should be derived from the DFT+BTE workflow described in the Workflow steps.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Phonopy: https://phonopy.github.io/phonopy/
- Phono3py: https://phonopy.github.io/phono3py/
- HiPhive: https://hiphive.materialsmodeling.org/
- BoltzTraP2: https://www.boltztrap2.org/

## Workflow steps

### Step 1: Generate initial Janus gamma-Pb2SeTe structure
- Role: process
- Action: Construct the atomic positions and lattice vectors of a Janus gamma-Pb2SeTe monolayer. Use the known buckled honeycomb structure with Pb in the middle, Se on one side and Te on the other. Start from lattice constants and atomic positions of parent gamma-PbX monolayers. The unit cell includes 4 atoms. Build the initial input file for Quantum Espresso.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: DFT structural optimization
- Role: process
- Action: Using Quantum Espresso with the PBE functional and SSSP pseudopotentials, relax the atomic positions and cell parameters of the Janus monolayer. Apply a vacuum layer of ~30 Å along the c-axis to isolate the layer. Converge forces to below 1e-3 Ry/Bohr.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 3: Harmonic phonon calculation
- Role: process
- Action: Build a supercell of the optimized structure. Use Phonopy with finite displacements and HiPhive to enforce rotational invariance and obtain quadratic ZA acoustic mode. Compute harmonic interatomic force constants and the phonon dispersion.
- Evidence: `/app/outputs/harmonic_IFCs.hdf5`

### Step 4: Third-order interatomic force constants
- Role: process
- Action: Use Phono3py on a supercell of the optimized structure to compute the third-order anharmonic interatomic force constants.
- Evidence: `/app/outputs/fc3.hdf5`

### Step 5: Elastic constants from strain DFT
- Role: process
- Action: Apply uniaxial (x and y) and biaxial strains to the optimized rectangular unit cell within a small strain range. For each strain, relax atomic positions with QE. Fit the strain-energy curves to obtain the 2D elastic stiffness constants C11 and C12.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 6: Band structure and effective masses
- Role: process
- Action: Compute the PBE band structure of the optimized monolayer along a standard high-symmetry path including Gamma, M, K points. Extract the hole effective masses at the valence band maximum along the transport directions by fitting a parabola to the band edges.
- Evidence: `/app/outputs/effective_masses.json`

### Step 7: Deformation potentials and relaxation time
- Role: process
- Action: Apply uniaxial strains along x and y directions to the optimized unit cell. For each strain, run a QE SCF calculation to obtain the VBM energy relative to the vacuum level. Fit the energy shifts vs. strain to obtain the deformation potential constants. Combine with effective masses, elastic constants, and temperature (300 K) using deformation potential theory to compute the hole mobility and the relaxation time τ.
- Evidence: `/app/outputs/relaxation_times.json`

### Step 8: Lattice thermal conductivity
- Role: scored
- Action: Using the harmonic IFCs (from Phonopy/HiPhive) and the third-order IFCs (from Phono3py), solve the linearized Boltzmann transport equation with a fine Q-grid. Apply the scaling factor Lz/h to account for the 2D cross-plane geometry. Compute the in-plane lattice thermal conductivity κl at 300 K and at 800 K.
- Output file: `/app/outputs/step_01_lattice_thermal_conductivity.json`
- Format: json
- Contract: {"kappa_l_300K": float, "kappa_l_800K": float} (units W m^{-1} K^{-1})
- Scoring: scored by hidden verifier

### Step 9: Electronic transport properties from BoltzTraP2
- Role: scored
- Action: Using the PBE band structure and the deformation-potential relaxation time for holes, run BoltzTraP2 in constant relaxation time approximation at 800 K. Scale the computed transport coefficients by τ. Scan the p-type carrier concentration over a range that includes the optimal doping. Output Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as a function of carrier concentration.
- Output file: `/app/outputs/step_02_electronic_transport.json`
- Format: json
- Contract: [{"carrier_concentration": float (cm^{-2}), "seebeck": float (µV/K), "electrical_conductivity": float (Ω^{-1}m^{-1}), "electronic_thermal_conductivity": float (W m^{-1} K^{-1})}, ...]
- Scoring: scored by hidden verifier

### Step 10: Figure of merit ZT calculation
- Role: scored (load-bearing)
- Action: Load the electronic transport data and the lattice thermal conductivity at 800 K. Compute the power factor PF = σ S^2, then ZT = (σ S^2 T)/(κ_e + κ_l) for each carrier concentration. Identify the maximum ZT and the carrier concentration at which it occurs. Write these to the output file.
- Output file: `/app/outputs/step_03_ZT_results.json`
- Format: json
- Contract: {"max_ZT_800K_p_type": float (dimensionless), "optimal_carrier_concentration_800K_p_type": float (cm^{-2})}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_thermal_conductivity.json`
- `/app/outputs/step_02_electronic_transport.json`
- `/app/outputs/step_03_ZT_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_thermal_conductivity.json
- path: `/app/outputs/step_01_lattice_thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice thermal conductivity at 300 K and 800 K for gamma-Pb2SeTe.
- schema:
  - `type`: object
  - `required`:
    - `kappa_l_300K`: float (W/mK)
    - `kappa_l_800K`: float (W/mK)

### step_02_electronic_transport.json
- path: `/app/outputs/step_02_electronic_transport.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic transport coefficients vs. carrier concentration at 800 K for p-type doping.
- schema:
  - `type`: array
  - `items`:
    - `carrier_concentration`: float
    - `seebeck`: float
    - `electrical_conductivity`: float
    - `electronic_thermal_conductivity`: float

### step_03_ZT_results.json
- path: `/app/outputs/step_03_ZT_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum ZT and the corresponding carrier concentration for p-type gamma-Pb2SeTe at 800 K.
- schema:
  - `type`: object
  - `required`:
    - `max_ZT_800K_p_type`: float
    - `optimal_carrier_concentration_800K_p_type`: float (cm^{-2})

Notes: The lattice thermal conductivity is a fixed computed quantity (comparable within tolerance). The optimal ZT is a performance metric; meeting or exceeding the paper's value earns full credit. The electronic transport array provides the raw data from which ZT can be recomputed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "kappa_l_300K": "float (W/mK)",
          "kappa_l_800K": "float (W/mK)"
        }
      },
      "description": "Lattice thermal conductivity at 300 K and 800 K for gamma-Pb2SeTe."
    },
    {
      "file": "step_02_electronic_transport.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "carrier_concentration": "float",
          "seebeck": "float",
          "electrical_conductivity": "float",
          "electronic_thermal_conductivity": "float"
        }
      },
      "description": "Electronic transport coefficients vs. carrier concentration at 800 K for p-type doping."
    },
    {
      "file": "step_03_ZT_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "max_ZT_800K_p_type": "float",
          "optimal_carrier_concentration_800K_p_type": "float (cm^{-2})"
        }
      },
      "description": "Maximum ZT and the corresponding carrier concentration for p-type gamma-Pb2SeTe at 800 K."
    }
  ],
  "notes": "The lattice thermal conductivity is a fixed computed quantity (comparable within tolerance). The optimal ZT is a performance metric; meeting or exceeding the paper's value earns full credit. The electronic transport array provides the raw data from which ZT can be recomputed."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that inspects each of the three output files. The verifier reads the lattice thermal conductivity values and compares them to hidden reference values using appropriate tolerances. It examines the electronic transport array, either recomputing ZT from the raw data or checking that the reported coefficients are physically consistent, and compares selected quantities to hidden references. Finally, it compares the reported maximum ZT and optimal carrier concentration to hidden reference values. Each stage contributes a fraction to the total reward (in the range 0–1). To succeed, you must faithfully execute the computational pipeline and produce physically correct results; merely reporting a number without running the required calculations will not pass the verification.
