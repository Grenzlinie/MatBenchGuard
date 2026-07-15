## Problem background

Thermoelectric (TE) materials convert heat directly into electricity, offering a route to waste-heat recovery and solid-state cooling. Their efficiency is quantified by the dimensionless figure of merit

ZT = (σ S² T) / (κ_e + κ_l) = (PF / (κ_e + κ_l)) × T,

where σ is electrical conductivity, S is Seebeck coefficient, PF = σ S² is power factor, κ_e is electronic thermal conductivity, κ_l is lattice thermal conductivity, and T is temperature. A high ZT requires simultaneous high power factor and low total thermal conductivity, which are often counteracting properties.

Two-dimensional (2D) Janus monolayers – nanosheets with different chalcogen atoms on opposite surfaces – can break structural symmetry and enhance thermoelectric performance. This study investigates three Janus γ-Pb₂XY monolayers (X=S, Se; Y=Se, Te; X≠Y): γ-Pb₂SSe, γ-Pb₂STe, and γ-Pb₂SeTe. They combine the intrinsically low lattice thermal conductivity of γ-phase Pb-chalcogenides with favorable electronic transport, promising high ZT values.

## Approach

We use density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) functional, combined with the semi-classical Boltzmann transport equation, to compute the complete set of thermoelectric properties from first principles. The workflow consists of:

- **DFT geometry optimization** for each Janus monolayer, including van der Waals corrections.
- **Electronic structure calculations** to obtain PBE band structures, Kohn-Sham eigenvalues on dense k-meshes, and effective masses of electrons and holes from parabolic fitting around the band edges.
- **Harmonic phonon calculations** using the finite-displacement method to verify dynamic stability and obtain second-order interatomic force constants (IFCs). The out-of-plane acoustic mode is enforced to be quadratic near Γ by applying rotational invariance conditions.
- **Mechanical properties and deformation potentials**: uniaxial strains are applied to extract the 2D elastic modulus and the deformation potential constants for the conduction band minimum (CBM) and valence band maximum (VBM) relative to the vacuum level.
- **Carrier relaxation time** derived via the deformation potential (DP) theory (Bardeen–Shockley formula) using effective masses, 2D elastic modulus, and deformation potentials.
- **Lattice thermal conductivity** computed by solving the linearized Boltzmann transport equation (LBTE) for phonons using third-order anharmonic IFCs. Temperature-dependent κ_l is obtained at 300 K and 800 K with appropriate 2D thickness scaling.
- **Electronic transport coefficients**: Seebeck coefficient S, electrical conductivity σ (scaled by the DP relaxation time), power factor PF, and electronic thermal conductivity κ_e as functions of carrier concentration are obtained from the PBE band structure using BoltzTraP2 in the rigid-band approximation.
- **Thermoelectric figure of merit ZT**: PF and κ_e are combined with κ_l to compute ZT(n,T) for p-type carriers. For each monolayer and the two temperatures (300 K, 800 K), the optimal carrier concentration that maximizes ZT is identified, and the corresponding transport parameters are collected.

## Reproduction target

Compute the optimal p-type dimensionless figure of merit ZT and the corresponding Seebeck coefficient, electrical conductivity, power factor, electronic thermal conductivity, and optimal carrier concentration for the three Janus γ-Pb₂SSe, γ-Pb₂STe, and γ-Pb₂SeTe monolayers at temperatures 300 K and 800 K from first-principles DFT and semi-classical Boltzmann transport simulations, and store the results in a single CSV file.

## Assets

- **Quantum ESPRESSO** – plane-wave DFT code. Open-source; website: https://www.quantum-espresso.org, installable via conda or from source.
- **Phonopy** – harmonic phonon and supercell finite-displacement engine. Install via pip; package name `phonopy`.
- **Phono3py** – third-order anharmonic interatomic force constants and lattice thermal conductivity via LBTE. Install via pip; package name `phono3py`.
- **BoltzTraP2** – electronic transport coefficients under constant relaxation time approximation. Install via pip; package name `BoltzTraP2`.
- **HiPhive** – enforces rotational invariance conditions for harmonic IFCs. Install via pip; package name `hiphive`.
- **PAW pseudopotentials** – PBE projector-augmented-wave pseudopotentials for Pb, S, Se, Te. Obtainable from standard sources such as SSSP or PSLibrary (https://www.quantum-espresso.org/pseudopotentials).

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for each Janus monolayer (γ-Pb₂SSe, γ-Pb₂STe, γ-Pb₂SeTe) using Quantum ESPRESSO with PBE PAW pseudopotentials and van der Waals corrections. Optimize until forces are below 1×10⁻³ Ry/Bohr. Include a sufficient vacuum layer along the out-of-plane direction.
- Evidence: none

### Step 2: Electronic structure and effective mass
- Role: process
- Action: Using the optimized structures, run a self-consistent DFT calculation (PBE) followed by a non-self-consistent band structure calculation. Compute the PBE band structure and extract the effective masses of electrons (CBM) and holes (VBM) along the in-plane transport directions by parabolic fitting. Also obtain Kohn–Sham eigenvalues on a dense k-mesh for later use by BoltzTraP2.
- Evidence: none

### Step 3: Harmonic phonon calculation
- Role: process
- Action: Compute second-order interatomic force constants using Phonopy with finite displacements on a sufficiently large supercell. Use HiPhive to enforce rotational invariance so that the out-of-plane acoustic mode is quadratic near Γ. Obtain harmonic phonon frequencies and IFCs.
- Evidence: none

### Step 4: Mechanical and deformation potential calculations
- Role: process
- Action: Apply uniaxial strains (compressive and tensile) along the in-plane directions to the rectangular unit cell, relaxing atomic positions at each strain. Extract the 2D elastic stiffness modulus from strain–energy fits, and obtain the deformation potential constants for the CBM and VBM from the energy shifts of the band edges relative to the vacuum level.
- Evidence: none

### Step 5: Carrier relaxation time from deformation potential theory
- Role: process
- Action: Using the effective masses, 2D elastic modulus, and deformation potentials, compute the carrier mobility and relaxation time τ for electrons and holes via the Bardeen–Shockley formula. Average over transport directions to obtain an isotropic relaxation time for each carrier type.
- Evidence: none

### Step 6: Lattice thermal conductivity by anharmonic phonon LBTE
- Role: process
- Action: Compute third-order interatomic force constants using Phono3py on a moderate supercell with finite displacements. Solve the linearized Boltzmann transport equation for phonons on a fine q-grid to obtain the lattice thermal conductivity κ_l along the in-plane plane at 300 K and 800 K, applying the appropriate thickness scaling.
- Evidence: none

### Step 7: Electronic transport coefficients (BoltzTraP2 with DP τ)
- Role: process
- Action: Run BoltzTraP2 on the PBE band structure with the previously computed relaxation time τ to obtain the Seebeck coefficient S, electrical conductivity σ, power factor PF = σS², and electronic thermal conductivity κ_e as functions of carrier concentration (p-type, rigid-band approximation) and temperature (300–800 K).
- Evidence: none

### Step 8: Optimal p-type ZT extraction
- Role: scored (load-bearing)
- Action: For each monolayer, combine the power factor PF and electronic thermal conductivity κ_e (from step 7) with the lattice thermal conductivity κ_l (from step 6) to compute ZT = (PF / (κ_e + κ_l)) × T as a function of carrier concentration. For the p-type branch, locate the concentration that maximizes ZT at 300 K and at 800 K. Collect the optimal ZT and the corresponding Seebeck coefficient, electrical conductivity, power factor, electronic thermal conductivity, and carrier concentration. Write a CSV file with exactly 6 rows (3 monolayers × 2 temperatures, all carrier_type='p').
- Output file: `/app/outputs/optimal_zt_summary.csv`
- Format: csv
- Contract: CSV with header: monolayer,temperature_K,carrier_type,optimal_carrier_concentration_cm2,Seebeck_uVK,electrical_conductivity_Ohm-1m-1,power_factor_Wm-1K-2,electronic_thermal_conductivity_Wm-1K-1,ZT. 6 data rows.
- Scoring: scored by hidden verifier.

## Output files

- `/app/outputs/optimal_zt_summary.csv` — the final aggregated thermoelectric results (scored).

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_zt_summary.csv
- path: `/app/outputs/optimal_zt_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimal p-type figure of merit ZT and the corresponding transport parameters for the three Janus monolayers at 300 K and 800 K.
- schema:
  - `type`: table
  - `required_columns`: `monolayer`, `temperature_K`, `carrier_type`, `optimal_carrier_concentration_cm2`, `Seebeck_uVK`, `electrical_conductivity_Ohm-1m-1`, `power_factor_Wm-1K-2`, `electronic_thermal_conductivity_Wm-1K-1`, `ZT`
  - `units`:
    - `optimal_carrier_concentration_cm2`: cm⁻²
    - `Seebeck_uVK`: μV/K
    - `electrical_conductivity_Ohm-1m-1`: Ω⁻¹ m⁻¹
    - `power_factor_Wm-1K-2`: W m⁻¹ K⁻²
    - `electronic_thermal_conductivity_Wm-1K-1`: W m⁻¹ K⁻¹
    - `ZT`: dimensionless

Notes: Carrier_type must be 'p' for all rows. The CSV must contain exactly 6 rows (γ-Pb₂SSe, γ-Pb₂STe, γ-Pb₂SeTe each at 300 K and 800 K). The hidden verifier compares each numeric column against paper-reported values within a relative error tolerance and checks that ZT(800 K) > ZT(300 K) for each monolayer.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_zt_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "monolayer",
          "temperature_K",
          "carrier_type",
          "optimal_carrier_concentration_cm2",
          "Seebeck_uVK",
          "electrical_conductivity_Ohm-1m-1",
          "power_factor_Wm-1K-2",
          "electronic_thermal_conductivity_Wm-1K-1",
          "ZT"
        ],
        "units": {
          "optimal_carrier_concentration_cm2": "cm⁻²",
          "Seebeck_uVK": "μV/K",
          "electrical_conductivity_Ohm-1m-1": "Ω⁻¹ m⁻¹",
          "power_factor_Wm-1K-2": "W m⁻¹ K⁻²",
          "electronic_thermal_conductivity_Wm-1K-1": "W m⁻¹ K⁻¹",
          "ZT": "dimensionless"
        }
      },
      "description": "Optimal p-type figure of merit ZT and the corresponding transport parameters for the three Janus monolayers at 300 K and 800 K."
    }
  ],
  "notes": "Carrier_type must be 'p' for all rows. The CSV must contain exactly 6 rows (γ-Pb₂SSe, γ-Pb₂STe, γ-Pb₂SeTe each at 300 K and 800 K). The hidden verifier compares each numeric column against paper-reported values within a relative error tolerance and checks that ZT(800 K) > ZT(300 K) for each monolayer."
}
```

## How you are scored

The hidden verifier reads your output CSV and compares each row's ZT, Seebeck coefficient, electrical conductivity, power factor, electronic thermal conductivity, and optimal carrier concentration against hidden gold values derived from the reference publication. For each numeric quantity, the relative error is computed; all relative errors must be within a predetermined tolerance. Additionally, monotonicity (ZT at 800 K > ZT at 300 K for each monolayer) is checked. Each scored row contributes equally to the final reward. Simply reporting the paper's numbers without performing the genuine first-principles workflow will not satisfy the verifier because the scoring is based on a reference_match with a tight tolerance that reflects a correct re-run of the DFT+BTE pipeline.
