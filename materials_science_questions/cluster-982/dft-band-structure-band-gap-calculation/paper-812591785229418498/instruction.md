# DFT and Boltzmann transport calculation of thermoelectric properties for a half-Heusler compound

## Problem background
Half-Heusler compounds are promising thermoelectric materials that can convert heat into electricity, but many suffer from high lattice thermal conductivity that limits their thermoelectric figure of merit ZT. The half-Heusler compound BiBaK has a crystal structure in which the light K atom resides inside a cage formed by heavy Bi and Ba atoms. This structural motif may cause the K atom to "rattle" and scatter phonons strongly, potentially giving BiBaK an intrinsically low lattice thermal conductivity. The goal of this task is to use density functional theory and Boltzmann transport theory to compute the lattice thermal conductivity, electronic band structure, and thermoelectric performance of BiBaK, and thereby determine its ZT and the optimal doping conditions.

## Approach
The reproduction follows a computational workflow based on first-principles methods and semi-classical transport theory. The crystal structure of BiBaK (space group F-43m) is first relaxed using density functional theory (DFT) to obtain its equilibrium lattice constant and atomic positions. From this optimized structure, second- and third-order interatomic force constants are obtained via the finite-displacement method. The force constants are used to solve the linearized phonon Boltzmann transport equation, yielding the temperature-dependent lattice thermal conductivity κ_l. Separately, the electronic band structure is computed with a hybrid exchange-correlation functional that includes spin-orbit coupling, giving the indirect band gap and band dispersions. Carrier relaxation times are estimated using deformation potential theory. These relaxation times, together with the band structure, are supplied to the semi-classical Boltzmann transport code BoltzTraP2 to calculate the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity for both n- and p-type doping as functions of temperature and carrier concentration. Finally, the figure of merit ZT = S²σT/(κ_l + κ_e) is evaluated, and the maximum ZT values at 900 K together with the corresponding optimal carrier concentrations are extracted.

## Reproduction target
Compute the following quantities for half-Heusler BiBaK and write them to `/app/outputs/results.json`:  
- lattice thermal conductivity κ_l at 300 K and 900 K (in W/mK),  
- the indirect band gap (in eV),  
- the maximum n-type ZT at 900 K and the carrier concentration that achieves it (in cm⁻³),  
- the maximum p-type ZT at 900 K and the carrier concentration that achieves it (in cm⁻³).  
These must be obtained by running the full computational pipeline described in the workflow steps; reporting numbers alone is not sufficient.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- ShengBTE: https://www.shengbte.org/
- BoltzTraP2: https://gitlab.com/sousaw/BoltzTraP2
- Spglib: https://spglib.github.io/spglib/

## Workflow steps

### Step 1: Structure optimization
- Role: process
- Action: Optimize the crystal structure of half-Heusler BiBaK (space group F-43m, starting lattice constant approximately 8.45 Å) using density functional theory. Determine the fully relaxed lattice constant and atomic positions that will serve as the equilibrium structure for all subsequent calculations.
- Evidence: `/app/outputs/relax.log`

### Step 2: Second-order interatomic force constants
- Role: process
- Action: Compute the harmonic (second-order) interatomic force constants of the relaxed BiBaK structure using the finite displacement method on a supercell. Generate the phonon dispersion and group velocities as intermediate results.
- Evidence: `/app/outputs/FORCE_CONSTANTS_2ND`

### Step 3: Third-order interatomic force constants
- Role: process
- Action: Compute the anharmonic (third-order) interatomic force constants using a larger supercell with a cutoff radius of 7.7 Å. This step is computationally demanding; parallel execution is expected.
- Evidence: `/app/outputs/FORCE_CONSTANTS_3RD`

### Step 4: Lattice thermal conductivity
- Role: process
- Action: Solve the phonon Boltzmann transport equation using ShengBTE with the second- and third-order force constants on a dense q-mesh to obtain the temperature-dependent lattice thermal conductivity. Output the κ_l values at 300 K and 900 K, which will be used in the final results assembly.
- Evidence: `/app/outputs/kappa_300K_900K.json`

### Step 5: Electronic band structure (HSE+SOC)
- Role: process
- Action: Compute the electronic band structure of the relaxed BiBaK using a hybrid functional (e.g. HSE06) with spin-orbit coupling. Determine the indirect band gap (VBM at X, CBM at Γ) and output its value.
- Evidence: `/app/outputs/band_gap.json`

### Step 6: Deformation potential parameters
- Role: process
- Action: Calculate the elastic constant, deformation potential constant, and carrier relaxation times for electrons and holes using deformation potential theory. Output the required parameters.
- Evidence: `/app/outputs/dp_params.json`

### Step 7: Electronic transport coefficients
- Role: process
- Action: Feed the band structure (step4) and carrier relaxation times (step5) into BoltzTraP2 to compute the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as functions of temperature and carrier concentration for both n- and p-type doping. Output the transport data in a format suitable for the final ZT calculation.
- Evidence: `/app/outputs/transport_data.json`

### Step 8: Figure-of-merit ZT and final results
- Role: scored (load-bearing)
- Action: Combine the lattice thermal conductivity (from step3) with the electronic transport coefficients (step6) to compute ZT = S²σT/(κ_l+κ_e) for n- and p-type doping as functions of carrier concentration and temperature. Identify the maximum ZT values at 900 K and the corresponding optimal carrier concentrations. Gather also the lattice thermal conductivity at 300 K and 900 K and the indirect band gap. Write all these quantities into /app/outputs/results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: kappa_300K (W/mK), kappa_900K (W/mK), band_gap (eV), n_type_ZT_max (dimensionless), n_type_carrier_concentration_optimal (cm^-3), p_type_ZT_max (dimensionless), p_type_carrier_concentration_optimal (cm^-3). All values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the reproduced lattice thermal conductivity at 300 K and 900 K, indirect band gap, maximum n-type and p-type ZT values and their optimal carrier concentrations.
- schema:
  - `type`: object
  - `required`:
    - `kappa_300K`: float (W/mK)
    - `kappa_900K`: float (W/mK)
    - `band_gap`: float (eV)
    - `n_type_ZT_max`: float (dimensionless)
    - `n_type_carrier_concentration_optimal`: float (cm^-3)
    - `p_type_ZT_max`: float (dimensionless)
    - `p_type_carrier_concentration_optimal`: float (cm^-3)

Notes: All values are compared against a hidden reference (paper-reported results) with appropriate tolerances. The ZT values are directional; the scoring accounts for genuine reproduction accuracy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "kappa_300K": "float (W/mK)",
          "kappa_900K": "float (W/mK)",
          "band_gap": "float (eV)",
          "n_type_ZT_max": "float (dimensionless)",
          "n_type_carrier_concentration_optimal": "float (cm^-3)",
          "p_type_ZT_max": "float (dimensionless)",
          "p_type_carrier_concentration_optimal": "float (cm^-3)"
        }
      },
      "description": "JSON file containing the reproduced lattice thermal conductivity at 300 K and 900 K, indirect band gap, maximum n-type and p-type ZT values and their optimal carrier concentrations."
    }
  ],
  "notes": "All values are compared against a hidden reference (paper-reported results) with appropriate tolerances. The ZT values are directional; the scoring accounts for genuine reproduction accuracy."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and compares each reported value against a scientific reference using appropriate tolerances. The overall reward is a weighted sum over the quantities, with higher weight placed on the ZT values because they represent the main thermoelectric figure of merit. You must genuinely execute all the process steps; the verifier may also inspect intermediate evidence files for consistency. Simply writing plausible numbers without performing the required computations will not yield a passing score.
