# Computing thermoelectric figure of merit ZT for GeS/GeSe monolayers and heterostructures using DFT and Boltzmann transport equation

## Problem background
Thermoelectric materials convert heat directly into electricity via the Seebeck effect, and their efficiency is quantified by the dimensionless figure of merit ZT. Achieving high ZT requires balancing a high Seebeck coefficient, high electrical conductivity, and low thermal conductivity. Two-dimensional van der Waals heterostructures, such as those formed by stacking germanium sulfide (GeS) and germanium selenide (GeSe) monolayers, are promising because their thermoelectric properties can be tuned by the stacking configuration. First-principles density functional theory (DFT) combined with the Boltzmann transport equation enables computational prediction of these properties, accelerating material design.

## Approach
This task computes the thermoelectric figure of merit ZT from first principles. The workflow proceeds through several stages: (1) structural relaxation of the four target systems—GeS monolayer, GeSe monolayer, and the two stacking variants GeS/GeSe XX and GeS/GeSe XY—using DFT with the PBE functional; (2) electronic band structure calculations to obtain PBE band gaps and effective masses; (3) deformation potential theory to derive carrier relaxation times; (4) harmonic and anharmonic phonon calculations with finite-displacement supercells to determine lattice thermal conductivity; (5) semi-classical Boltzmann transport calculations (via BoltzTraP2) to obtain the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as functions of chemical potential; and (6) combining all contributions to compute ZT at 300 K and 800 K. All calculations use open-source packages: Quantum Espresso for DFT, Phonopy and Phono3py for phonons, HiPhive for rotational invariance enforcement on harmonic force constants, and BoltzTraP2 for transport coefficients.

## Reproduction target
The target is to compute, for the four systems (GeS monolayer, GeSe monolayer, GeS/GeSe XX heterostructure, and GeS/GeSe XY heterostructure): (a) the indirect PBE band gap in eV, output as band_gaps.json; (b) the lattice thermal conductivity at 300 K in W/mK, output as lattice_thermal_conductivity.json; and (c) the maximum ZT value at 300 K and at 800 K, output as zt_values.json. All outputs must follow the exact JSON schema specified in the output contract.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org
- BoltzTraP2: https://github.com/tgacek/boltztrap2
- Phono3py: https://github.com/phonopy/phono3py
- Phonopy: https://github.com/phonopy/phonopy
- HiPhive: https://github.com/ttadano/hiphive
- Standard solid-state pseudopotentials (SSSP): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Perform DFT structural relaxation for GeS monolayer, GeSe monolayer, GeS/GeSe XX, and GeS/GeSe XY vdW heterostructures using Quantum Espresso with PBE functional. Obtain relaxed atomic coordinates and lattice parameters.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: PBE band structure calculation
- Role: process
- Action: Compute PBE Kohn-Sham band energies on dense k-point grids for all four relaxed structures using Quantum Espresso. Extract effective masses via parabolic fitting at band edges.
- Evidence: `/app/outputs/bands.log`

### Step 3: Compute PBE band gaps
- Role: scored
- Action: Extract the indirect band gap (eV) for each material from the PBE band structure.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"GeS_ML": "float eV", "GeSe_ML": "float eV", "XX": "float eV", "XY": "float eV"}
- Scoring: scored by hidden verifier

### Step 4: Deformation potential and relaxation time
- Role: process
- Action: Apply uniaxial strain to monolayers and heterostructures, compute band-edge shifts and vacuum energies with DFT. Extract deformation potential constants and elastic moduli. Calculate 2D carrier mobilities and relaxation times for electrons and holes.
- Evidence: `/app/outputs/relaxation_times.json`

### Step 5: Harmonic phonon dispersion
- Role: process
- Action: Compute second-order interatomic force constants using finite displacement method (Phonopy) on supercells with DFT forces. Enforce rotational invariance constraints (HiPhive). Generate phonon dispersion to confirm dynamic stability.
- Evidence: `/app/outputs/phonon_dispersion.png`

### Step 6: Lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Using harmonic force constants from step 05, compute third-order anharmonic force constants via finite displacement supercells (Phono3py). Solve the linearized phonon Boltzmann transport equation to obtain lattice thermal conductivity as a function of temperature. Report values at 300 K.
- Output file: `/app/outputs/lattice_thermal_conductivity.json`
- Format: json
- Contract: {"GeS_ML": "float W/mK", "GeSe_ML": "float W/mK", "XX": "float W/mK", "XY": "float W/mK"}
- Scoring: scored by hidden verifier

### Step 7: BoltzTraP2 transport calculation
- Role: process
- Action: Use the PBE band energies to run BoltzTraP2 and compute the transport distribution function. Derive Seebeck coefficient S, electrical conductivity per relaxation time (σ/τ), and electronic thermal conductivity per relaxation time (κ_e/τ) as functions of chemical potential and temperature (300–800 K).
- Evidence: `/app/outputs/transport_coefficients.h5`

### Step 8: Figure of merit ZT
- Role: scored (load-bearing)
- Action: Combine the Seebeck coefficient S (from step 07), scaled absolute electrical conductivity σ and electronic thermal conductivity κ_e (using τ from step 04), lattice thermal conductivity κ_l (step 06), and temperature T to compute ZT via ZT = S^2 σ T / (κ_e + κ_l). Evaluate ZT at 300 K and 800 K for each material and report the maximum ZT value at each temperature.
- Output file: `/app/outputs/zt_values.json`
- Format: json
- Contract: {"GeS_ML": {"300K": "float", "800K": "float"}, "GeSe_ML": {"300K": "float", "800K": "float"}, "XX": {"300K": "float", "800K": "float"}, "XY": {"300K": "float", "800K": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/lattice_thermal_conductivity.json`
- `/app/outputs/zt_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: PBE indirect band gaps for GeS monolayer, GeSe monolayer, GeS/GeSe XX, and GeS/GeSe XY heterostructure.
- schema:
  - `type`: object
  - `required`:
    - `GeS_ML`: float, eV
    - `GeSe_ML`: float, eV
    - `XX`: float, eV
    - `XY`: float, eV

### lattice_thermal_conductivity.json
- path: `/app/outputs/lattice_thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivity at 300 K for the four systems.
- schema:
  - `type`: object
  - `required`:
    - `GeS_ML`: float, W/mK
    - `GeSe_ML`: float, W/mK
    - `XX`: float, W/mK
    - `XY`: float, W/mK

### zt_values.json
- path: `/app/outputs/zt_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum ZT at 300 K and 800 K for all four materials.
- schema:
  - `type`: object
  - `required`:
    - `GeS_ML`:
      - `300K`: float
      - `800K`: float
    - `GeSe_ML`:
      - `300K`: float
      - `800K`: float
    - `XX`:
      - `300K`: float
      - `800K`: float
    - `XY`:
      - `300K`: float
      - `800K`: float

Notes: All values are compared to the corresponding paper-reported numbers with appropriate tolerances. Relative trends (ZT increase with temperature, heterostructure ZT lower than monolayer ZT at 300 K) are also assessed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "GeS_ML": "float, eV",
          "GeSe_ML": "float, eV",
          "XX": "float, eV",
          "XY": "float, eV"
        }
      },
      "description": "PBE indirect band gaps for GeS monolayer, GeSe monolayer, GeS/GeSe XX, and GeS/GeSe XY heterostructure."
    },
    {
      "file": "lattice_thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "GeS_ML": "float, W/mK",
          "GeSe_ML": "float, W/mK",
          "XX": "float, W/mK",
          "XY": "float, W/mK"
        }
      },
      "description": "Lattice thermal conductivity at 300 K for the four systems."
    },
    {
      "file": "zt_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "GeS_ML": {
            "300K": "float",
            "800K": "float"
          },
          "GeSe_ML": {
            "300K": "float",
            "800K": "float"
          },
          "XX": {
            "300K": "float",
            "800K": "float"
          },
          "XY": {
            "300K": "float",
            "800K": "float"
          }
        }
      },
      "description": "Maximum ZT at 300 K and 800 K for all four materials."
    }
  ],
  "notes": "All values are compared to the corresponding paper-reported numbers with appropriate tolerances. Relative trends (ZT increase with temperature, heterostructure ZT lower than monolayer ZT at 300 K) are also assessed."
}
```

## How you are scored
After you submit your result artifacts, a hidden verifier will score each output independently by comparing your values against reference benchmarks and, for the ZT output, by checking that ZT increases with temperature and that the heterostructure ZT at 300 K is lower than that of the corresponding monolayers. The final reward is a weighted combination of these per‑artifact scores. Reporting the paper's numbers without running the pipeline is not sufficient — you must execute all workflow steps and produce the required output files.
