# Thermoelectric Transport Modeling and Vibrational Properties of Antifluorite Carbides

## Problem background
Antifluorite carbides (Be2C, Mg2C, and the mixed crystal BeMgC) are candidate materials for thermoelectric applications. First-principles density functional theory (DFT) combined with Boltzmann transport theory can predict the Seebeck coefficient, electrical conductivity, and power factor, enabling the identification of promising p-type thermoelectrics before synthesis. This task computes the optimum thermoelectric transport coefficients for the three carbides under constant relaxation time, and also calculates the zone-centre phonon frequencies of Mg2C to assess vibrational stability, thereby determining which compound exhibits the highest power factor and whether Mg2C is suitable for near-room-temperature thermoelectric use.

## Approach
The workflow uses first-principles DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional. The electronic band structure is calculated for the optimized antifluorite crystal structures. Within the constant relaxation-time approximation (τ fixed) and rigid-band approximation (band structure independent of doping and temperature), the Boltzmann transport equation is solved using the BoltzTraP code to obtain the Seebeck coefficient S, electrical conductivity σ, and power factor PF = S²σ as functions of chemical potential at several temperatures. The optimum PF and the corresponding quantities at the optimum p-type doping are extracted at 300, 500, and 800 K for each material. Separately, density-functional perturbation theory (DFPT) is applied to the optimized Mg2C structure to compute the Hessian and zone-centre phonon frequencies, from which the optical mode frequencies (TO, Raman, LO) and the LO-TO splitting are obtained. The pipeline proceeds through geometry optimization, non-self-consistent band structure on a dense k‑mesh, interface to BoltzTraP, transport simulation, and post-processing, plus the DFPT phonon calculation.

## Reproduction target
Produce two scored artifacts:
- optimum_transport.csv: For each compound (Be2C, BeMgC, Mg2C) and at each temperature (300, 500, 800 K), report the maximum (optimum) power factor PF_max, the corresponding Seebeck coefficient S_max, the electrical conductivity σ at that optimum, and the carrier concentration at that optimum, all evaluated under p-type conditions with a constant relaxation time τ = 4×10⁻¹⁴ s. The CSV must contain the columns: compound, temperature, PF_max, S_max, sigma_at_max, carrier_concentration.
- mg2c_phonon.json: For Mg2C, report the zone-centre optical phonon frequencies: the TO mode(s) (list of floats), Raman frequency (float), LO frequency (float), and the LO-TO splitting (float). The JSON must have keys TO, Raman, LO, LO-TO_split.
These artifacts will be compared against independent reference targets to assess the correctness of the computed values and, for the transport data, the relative ordering of the compounds.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/download
- BoltzTraP (Boltzmann transport code): https://bitbucket.org/sousaw/boltztrap
- PBE pseudopotentials for Be, Mg, C: https://www.quantum-espresso.org/pseudopotentials
- Crystal structures of Be2C, Mg2C, BeMgC

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Optimize the unit-cell lattice constants and atomic positions of Be2C, Mg2C, and BeMgC using DFT with the PBE functional.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: DFT band structure on dense k-mesh
- Role: process
- Action: Perform a non-self-consistent DFT calculation on a dense Monkhorst-Pack k-point grid (sufficiently dense, ~10^4 points in the irreducible wedge) using the optimized structures to obtain eigen-energies.
- Evidence: `/app/outputs/nscf_bands.log`

### Step 3: Convert DFT energies to BoltzTraP input
- Role: process
- Action: Extract the eigen-energies and generate the case.energy, case.struct, and case.intrans files required by BoltzTraP, using a constant relaxation time τ = 4×10⁻¹⁴ s and the lattice parameters from optimization.
- Evidence: `/app/outputs/boltztrap_input_files`

### Step 4: Run BoltzTraP transport simulations
- Role: process
- Action: Run BoltzTraP to compute the Seebeck coefficient S, electrical conductivity σ, and power factor PF = S²σ as functions of chemical potential at temperatures 300, 500, 800 K for each compound.
- Evidence: `/app/outputs/boltztrap_output.log`

### Step 5: Extract optimum transport quantities
- Role: scored (load-bearing)
- Action: Parse the BoltzTraP output to find the maximum PF and the corresponding S, σ, and carrier concentration at 300, 500, and 800 K for each compound. Write the results to optimum_transport.csv.
- Output file: `/app/outputs/optimum_transport.csv`
- Format: csv
- Contract: compound: string, temperature: int K, PF_max: float W/mK^2, S_max: float V/K, sigma_at_max: float S/m, carrier_concentration: float cm^-3
- Scoring: scored by hidden verifier

### Step 6: DFPT phonon calculation for Mg2C
- Role: process
- Action: Perform a density-functional perturbation theory (DFPT) calculation on the optimized Mg2C structure to obtain the Hessian and compute phonon frequencies at the Γ point.
- Evidence: `/app/outputs/mg2c_phonon.log`

### Step 7: Write Mg2C phonon frequencies
- Role: scored
- Action: Extract the TO, Raman, LO frequencies and the LO-TO splitting from the DFPT output and write them to mg2c_phonon.json.
- Output file: `/app/outputs/mg2c_phonon.json`
- Format: json
- Contract: {"TO": [float] cm^-1, "Raman": float cm^-1, "LO": float cm^-1, "LO-TO_split": float cm^-1}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimum_transport.csv`
- `/app/outputs/mg2c_phonon.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimum_transport.csv
- path: `/app/outputs/optimum_transport.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimum power factor, Seebeck coefficient, electrical conductivity, and carrier concentration for Be2C, BeMgC, Mg2C at 300, 500, 800 K under constant relaxation time τ = 4×10⁻¹⁴ s.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature`, `PF_max`, `S_max`, `sigma_at_max`, `carrier_concentration`
  - `units`:
    - `temperature`: K
    - `PF_max`: W/mK^2
    - `S_max`: V/K
    - `sigma_at_max`: S/m
    - `carrier_concentration`: cm^-3

### mg2c_phonon.json
- path: `/app/outputs/mg2c_phonon.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zone-centre phonon frequencies (TO, Raman, LO) and LO-TO splitting for Mg2C.
- schema:
  - `type`: object
  - `required`:
    - `TO`: array of floats (cm⁻¹)
    - `Raman`: float (cm⁻¹)
    - `LO`: float (cm⁻¹)
    - `LO-TO_split`: float (cm⁻¹)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimum_transport.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature",
          "PF_max",
          "S_max",
          "sigma_at_max",
          "carrier_concentration"
        ],
        "units": {
          "temperature": "K",
          "PF_max": "W/mK^2",
          "S_max": "V/K",
          "sigma_at_max": "S/m",
          "carrier_concentration": "cm^-3"
        }
      },
      "description": "Optimum power factor, Seebeck coefficient, electrical conductivity, and carrier concentration for Be2C, BeMgC, Mg2C at 300, 500, 800 K under constant relaxation time τ = 4×10⁻¹⁴ s."
    },
    {
      "file": "mg2c_phonon.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "TO": "array of floats (cm⁻¹)",
          "Raman": "float (cm⁻¹)",
          "LO": "float (cm⁻¹)",
          "LO-TO_split": "float (cm⁻¹)"
        }
      },
      "description": "Zone-centre phonon frequencies (TO, Raman, LO) and LO-TO splitting for Mg2C."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier reads your two scored output files and compares them against reference values (and the required trend among compounds) that are not disclosed to you. Scoring is a weighted combination: the transport artifact (optimum_transport.csv) carries the majority of the weight, and the phonon artifact (mg2c_phonon.json) carries a smaller but meaningful weight. The verifier checks the presence and format of the files, and then assesses the accuracy of the reported numbers within predefined tolerances and the consistency of the ordering trend. You must produce both artifacts exactly as specified, with correct column names, units, and JSON keys, to receive credit. Simply stating the paper’s published numbers does not guarantee a high score; the verifier evaluates your actual computed output.
