# Reproduction of Optimal Thermoelectric Figure-of-Merit ZT for Janus γ-Pb₂XY Monolayers

## Problem background
Thermoelectric materials can directly convert heat into electricity and vice versa, but their widespread use is limited by the need to simultaneously achieve a high Seebeck coefficient, high electrical conductivity, and low thermal conductivity. Two-dimensional (2D) materials offer a promising route to enhance thermoelectric performance through band engineering and phonon manipulation. In particular, Janus monolayers—where the top and bottom atomic layers consist of different chalcogen atoms—break structural symmetry and can reduce lattice thermal conductivity while maintaining favorable electrical transport. This task focuses on Janus gamma-phase Pb₂XY monolayers (X = S, Se; Y = Se, Te; X ≠ Y), exploring their potential as high-temperature thermoelectric materials. The key quantity to compute is the thermoelectric figure of merit ZT, which determines the efficiency of heat-to-electricity conversion, along with the underlying transport properties that define it.

## Approach
The computational protocol combines first-principles density functional theory (DFT) with the semiclassical Boltzmann transport equation. We use the PBE exchange-correlation functional and projector-augmented wave (PAW) pseudopotentials within Quantum ESPRESSO. The approach proceeds in three main stages:
1. **Structural and vibrational properties**: Relax the atomic positions of each Janus monolayer. Compute harmonic interatomic force constants via finite displacements and apply rotational invariance corrections to ensure a strictly quadratic out-of-plane acoustic mode. Then compute third-order anharmonic force constants on supercells and solve the phonon Boltzmann transport equation to obtain the lattice thermal conductivity κ_l as a function of temperature.
2. **Electronic transport**: Perform a dense k-point self-consistent field calculation to obtain the electronic band structure. Using deformation potential theory, extract effective masses, 2D elastic stiffness, and deformation potential constants from strained DFT runs to derive carrier relaxation times. Interpolate the band structure with BoltzTraP2 under the constant relaxation time approximation to generate the Seebeck coefficient S, electrical conductivity σ/τ, and electronic thermal conductivity κ_e/τ as functions of carrier concentration and temperature; then scale by the relaxation times to obtain absolute σ and κ_e.
3. **Figure of merit ZT**: For both n-type and p-type doping, combine the electronic transport coefficients with the lattice thermal conductivity and compute ZT = (σ S² T) / (κ_e + κ_l) as a function of carrier concentration at temperatures from 300 K to 800 K. Finally, identify the optimal (maximum) ZT and the corresponding transport properties at 300 K and 800 K for each of the three Janus monolayers.

## Reproduction target
Compute the optimal thermoelectric figure of merit ZT and the associated Seebeck coefficient, electrical conductivity, power factor, electronic thermal conductivity, and lattice thermal conductivity for n-type and p-type carriers at 300 K and 800 K for the three Janus monolayers gamma-Pb₂SSe, gamma-Pb₂STe, and gamma-Pb₂SeTe. Write the results to a single JSON file `optimized_zt_results.json` following the specified contract. The computed values should come from the DFT+phonon+Boltzmann transport protocol described above, not from lookup or pre‑computed tables.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP2: https://bitbucket.org/sousaw/boltzTraP2/
- Phonopy: https://phonopy.github.io/phonopy/
- Phono3py: https://phonopy.github.io/phono3py/
- HiPhive: https://hiphive.materialsmodeling.org/
- PBE PAW pseudopotentials: SSSP/PSlibrary

## Workflow steps

### Step 1: Structural optimization
- Role: process
- Action: Perform DFT structural relaxation for each Janus monolayer (gamma-Pb2SSe, gamma-Pb2STe, gamma-Pb2SeTe) using Quantum ESPRESSO with PBE functional and PAW pseudopotentials. Obtain equilibrium lattice constants, atomic positions, and cohesive energies. Include a vacuum layer along the z direction.
- Evidence: `/app/outputs/relaxation_details.log`

### Step 2: Harmonic phonon calculation
- Role: process
- Action: Using the relaxed structures, compute harmonic interatomic force constants (IFCs) via finite displacement method with Phonopy. Apply rotational invariance corrections using HiPhive to ensure a strictly quadratic ZA mode. Verify the absence of imaginary phonon frequencies.
- Evidence: `/app/outputs/harmonic_IFCs_output.hdf5`

### Step 3: Lattice thermal conductivity from anharmonic phonons
- Role: process
- Action: Compute third-order anharmonic IFCs with Phono3py on supercells. Solve the linearized Boltzmann transport equation (LBTE) to obtain lattice thermal conductivity κ_l(T) for temperatures 300–800 K. Apply the thickness scaling factor to obtain in-plane values.
- Evidence: `/app/outputs/kappa_l_results.txt`

### Step 4: Electronic band structure (PBE)
- Role: process
- Action: Perform a self-consistent DFT calculation for each monolayer with a dense k-point mesh using the PBE functional. Extract the band energies (eigenvalues) for use in BoltzTraP2.
- Evidence: `/app/outputs/bands.dat`

### Step 5: Carrier mobility and relaxation time (deformation potential theory)
- Role: process
- Action: Calculate effective masses (electron and hole) from band edge curvatures. Perform strained DFT runs to extract the 2D elastic stiffness and deformation potential constants. Apply Bardeen-Shockley deformation potential theory to obtain carrier mobilities and relaxation times at 300 K.
- Evidence: `/app/outputs/mobility_relaxation_times.txt`

### Step 6: Electronic transport coefficients (BoltzTraP2)
- Role: process
- Action: Interpolate the PBE band structure with BoltzTraP2 under the constant relaxation time approximation (CRTA). Generate the Seebeck coefficient S, electrical conductivity σ/τ, and electronic thermal conductivity κ_e/τ as functions of carrier concentration and temperature. Multiply by the DP relaxation times to obtain absolute σ and κ_e, and compute the power factor PF = σ S².
- Evidence: `/app/outputs/transport_coefficients.npz`

### Step 7: ZT optimization and final results
- Role: scored (load-bearing)
- Action: For each monolayer, combine the lattice thermal conductivity κ_l(T) with the electronic transport coefficients. Compute ZT(T, carrier concentration) = PF·T/(κ_e + κ_l). For both n-type and p-type carriers, find the optimal ZT and the corresponding transport properties at 300 K and 800 K. Write the optimal values to optimized_zt_results.json.
- Output file: `/app/outputs/optimized_zt_results.json`
- Format: json
- Contract: Object with keys 'gamma-Pb2SSe', 'gamma-Pb2STe', 'gamma-Pb2SeTe'. Each value is an object with keys 'n-type' and 'p-type'. Each doping type object has keys '300K' and '800K'. Each temperature entry contains: ZT (float), Seebeck_coeff_muV_K (float), electrical_cond_Ohm_m (float), power_factor_W_mK2_e-3 (float), electronic_thermal_cond_W_mK (float), lattice_thermal_cond_W_mK (float), carrier_concentration_cm2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_zt_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_zt_results.json
- path: `/app/outputs/optimized_zt_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the optimal ZT and corresponding Seebeck coefficient, electrical conductivity, power factor, electronic and lattice thermal conductivities, and carrier concentration for each monolayer, doping type (n, p), at 300 K and 800 K.
- schema:
  - `type`: object
  - `required`:
    - `gamma-Pb2SSe`:
      - `n-type`:
        - `300K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
        - `800K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
      - `p-type`:
        - `300K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
        - `800K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
    - `gamma-Pb2STe`:
      - `n-type`:
        - `300K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
        - `800K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
      - `p-type`:
        - `300K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
        - `800K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
    - `gamma-Pb2SeTe`:
      - `n-type`:
        - `300K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
        - `800K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
      - `p-type`:
        - `300K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float
        - `800K`:
          - `ZT`: float
          - `Seebeck_coeff_muV_K`: float
          - `electrical_cond_Ohm_m`: float
          - `power_factor_W_mK2_e-3`: float
          - `electronic_thermal_cond_W_mK`: float
          - `lattice_thermal_cond_W_mK`: float
          - `carrier_concentration_cm2`: float

Notes: The hidden verifier will compare the reported values against the paper's published optima with appropriate tolerances. The lattice thermal conductivity input κ_l is produced from the simulation, not extracted from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_zt_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma-Pb2SSe": {
            "n-type": {
              "300K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              },
              "800K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              }
            },
            "p-type": {
              "300K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              },
              "800K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              }
            }
          },
          "gamma-Pb2STe": {
            "n-type": {
              "300K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              },
              "800K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              }
            },
            "p-type": {
              "300K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              },
              "800K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              }
            }
          },
          "gamma-Pb2SeTe": {
            "n-type": {
              "300K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              },
              "800K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              }
            },
            "p-type": {
              "300K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              },
              "800K": {
                "ZT": "float",
                "Seebeck_coeff_muV_K": "float",
                "electrical_cond_Ohm_m": "float",
                "power_factor_W_mK2_e-3": "float",
                "electronic_thermal_cond_W_mK": "float",
                "lattice_thermal_cond_W_mK": "float",
                "carrier_concentration_cm2": "float"
              }
            }
          }
        }
      },
      "description": "Contains the optimal ZT and corresponding Seebeck coefficient, electrical conductivity, power factor, electronic and lattice thermal conductivities, and carrier concentration for each monolayer, doping type (n, p), at 300 K and 800 K."
    }
  ],
  "notes": "The hidden verifier will compare the reported values against the paper's published optima with appropriate tolerances. The lattice thermal conductivity input κ_l is produced from the simulation, not extracted from the paper."
}
```

## How you are scored
A hidden verifier reads your `optimized_zt_results.json` and independently scores each stage's contribution. Scoring is based on how well your computed optimal values agree with a set of hidden reference values derived from the literature. Because different implementations can yield slightly different numbers, the verifier applies tolerances that account for legitimate DFT and transport code variations. Additionally, structural relationships are checked: for example, at the same temperature p‑type ZT should exceed n‑type ZT, and ZT should increase with temperature for a given doping type. The final reward is a weighted sum over all quantities, with the ZT values carrying the largest weight.
