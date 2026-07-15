# DFT calculation of structural and optical properties of KB6 hexaboride

## Problem background
Potassium hexaboride (KB6) is a cubic hexaboride with potential for solar radiation shielding applications. This task uses first-principles density functional theory (DFT) to predict its structural and optical properties — including the dielectric function, reflectivity, absorption spectrum, and electron energy‑loss spectrum — in order to evaluate its performance as a near‑infrared absorber and visible‑light transmitter. The target is to compute the key quantitative descriptors that underpin such an assessment.

## Approach
The core approach is a plane‑wave DFT calculation using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) functional. Starting from the known cubic crystal structure (space group Pm‑3m), geometry optimization is performed to obtain the equilibrium lattice parameter and the internal coordinate of the boron atoms. A self‑consistent field (SCF) calculation then yields the Kohn–Sham eigenstates. From these, the frequency‑dependent complex dielectric function is computed within the independent‑particle approximation via the momentum matrix elements. The dielectric function is subsequently transformed into the reflectivity, absorption coefficient, and electron energy‑loss function. Characteristic features — such as the static dielectric constant, the plasma frequency, the maximum near‑infrared absorption, and the position of a sharp reflectivity dip — are extracted to quantify the optical response.

## Reproduction target
Perform a plane‑wave DFT calculation for cubic KB6 (space group Pm‑3m) and report the following six numbers in the output file results.json:

1. Optimized lattice parameter a₀ (Å).
2. Internal coordinate z (dimensionless).
3. Static dielectric constant ε₁(0).
4. Plasma frequency (eV), taken as the energy of the maximum in the electron energy‑loss function.
5. Maximum absorption coefficient (cm⁻¹) in the near‑infrared (NIR) region.
6. Energy (eV) of the sharp dip in the visible‑light reflectivity curve.

All values must be computed from the output of the simulation; the three process‑step evidence logs (relaxation.log, scf.log, optical_properties.log) must also be produced and placed in /app/outputs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for K and B: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of bulk KB6 (cubic, space group Pm-3m) using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with PBE functional and standard pseudopotentials. Optimize atomic positions and cell parameters to obtain equilibrium lattice parameter and internal coordinate.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Self-consistent field calculation
- Role: process
- Action: Run a self-consistent field calculation on the optimized structure to obtain Kohn-Sham eigenvalues and wavefunctions, using the same DFT code, functional, and an appropriate k-point mesh.
- Evidence: `/app/outputs/scf.log`

### Step 3: Optical properties computation
- Role: process
- Action: Compute the frequency-dependent complex dielectric function from the momentum matrix elements using the independent-particle approximation. Derive reflectivity, absorption coefficient, and electron energy-loss function.
- Evidence: `/app/outputs/optical_properties.log`

### Step 4: Report key results
- Role: scored (load-bearing)
- Action: Extract the following quantities from the computed data: (1) optimized lattice parameter a0 (Å); (2) internal coordinate z; (3) static dielectric constant ε₁(0); (4) plasma frequency (eV), identified as the energy of the maximum in the electron energy-loss function; (5) maximum absorption coefficient (cm⁻¹) in the NIR region; (6) energy (eV) of the sharp reflectivity dip in the visible range. Write these six values into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": {"a0": "number (Å)", "z": "number", "static_epsilon1_0": "number", "plasma_frequency_eV": "number (eV)", "max_absorption_coeff_NIR_cm1": "number (cm⁻¹)", "reflectivity_dip_energy_eV": "number (eV)"}}
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
- target_policy: exact_match
- description: Six numerical values from DFT calculations: lattice parameter, internal coordinate, static dielectric constant, plasma frequency, maximum NIR absorption coefficient, and reflectivity dip energy.
- schema:
  - `type`: object
  - `required`:
    - `a0`: number (Å)
    - `z`: number
    - `static_epsilon1_0`: number
    - `plasma_frequency_eV`: number (eV)
    - `max_absorption_coeff_NIR_cm1`: number (cm⁻¹)
    - `reflectivity_dip_energy_eV`: number (eV)

Notes: All six fields must be present. The checker compares each field to the paper-reported gold within domain-appropriate tolerances; fields carry equal weight.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a0": "number (Å)",
          "z": "number",
          "static_epsilon1_0": "number",
          "plasma_frequency_eV": "number (eV)",
          "max_absorption_coeff_NIR_cm1": "number (cm⁻¹)",
          "reflectivity_dip_energy_eV": "number (eV)"
        }
      },
      "description": "Six numerical values from DFT calculations: lattice parameter, internal coordinate, static dielectric constant, plasma frequency, maximum NIR absorption coefficient, and reflectivity dip energy."
    }
  ],
  "notes": "All six fields must be present. The checker compares each field to the paper-reported gold within domain-appropriate tolerances; fields carry equal weight."
}
```

## How you are scored
A hidden verifier reads your submitted results.json and compares each of the six numeric fields to a hidden reference. Every field carries equal weight. The verifier also checks that the three intermediate evidence logs (relaxation.log, scf.log, optical_properties.log) exist and are not empty; however, the bulk of the score comes from the accuracy of the six extracted quantities. Reporting numbers that match the reference is not sufficient — the entire computational pipeline described in the workflow steps must be executed, as evidenced by the logs. The final reward is the weighted combination of these checks.
