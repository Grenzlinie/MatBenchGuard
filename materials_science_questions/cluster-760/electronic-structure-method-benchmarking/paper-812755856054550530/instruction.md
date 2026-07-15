# CH3OH potential energy surface stationary points via CASSCF and CCI

## Problem background
The CH3+OH reaction is a key step in combustion chemistry, with multiple possible product channels including 1CH2+H2O, H2+HCOH, and H2+H2CO. This study characterizes the potential energy surface (PES) for these channels using multiconfigurational electronic structure methods. The goal is to determine the relative energies (including zero-point corrections) of the stationary points along these channels and to ascertain whether the 1CH2+H2O insertion channel possesses an intrinsic reaction barrier. The results provide insight into the accessibility of these channels from the CH3+OH asymptote and help resolve discrepancies in earlier kinetic models.

## Approach
The computational protocol proceeds in three stages:

1. **Geometry and frequency calculation (CASSCF/DZP)** — Complete-active-space self-consistent-field (CASSCF) gradient optimizations and harmonic vibrational frequency calculations are carried out for all stationary points using a polarized double-zeta basis set (cc-pVDZ). Active spaces are chosen to include the electrons in the bonds being made or broken: six electrons in six orbitals for the CH2O+H2 and 1CH2+H2O channels, and four electrons in four orbitals for the HCOH+H2 channel.

2. **Energetic refinement (CCI+Davidson / cc-pVTZ)** — Using the CASSCF-optimized geometries, internally contracted multireference configuration interaction (CCI) single-point calculations with the multireference Davidson correction are performed with the larger correlation-consistent triple-zeta basis set (cc-pVTZ) to obtain refined electronic energies.

3. **Relative energy construction** — Total energies for each stationary point are formed by adding the zero-point energy (from CASSCF harmonic frequencies) to the CCI+Davidson electronic energy. These total energies are then referenced to CH3OH (set to zero) to obtain relative energies. The experimental C–O bond strength of 90.2 kcal/mol is used as a fixed reference to place the CH3+OH asymptote.

## Reproduction target
Produce a JSON file `raw_energies.json` containing the CCI+Davidson electronic energy and the CASSCF zero-point energy (both in hartree) for each of the following stationary points:

- CH3OH
- CH2O-H2 (saddle point)
- CH2O+H2 (separated asymptote)
- CH2-H2O (dative complex / minimum)
- 1CH2+H2O (separated asymptote)
- HCOH-H2 (saddle point)
- HCOH+H2 (separated asymptote)

From these raw values the relative energies (including zero-point correction) with respect to CH3OH = 0.0 kcal/mol are computed. In addition, the ordering of the relative energies for the 1CH2+H2O channel is examined to determine whether the CH2-H2O saddle point lies below the 1CH2+H2O asymptote (indicating no intrinsic barrier) or above it (indicating a barrier).

## Assets

- Quantum chemistry package supporting CASSCF gradients and internally contracted MRCI (e.g., PySCF or ORCA): pyscf (pip install pyscf) or ORCA (free download for academic use)
- Correlation-consistent polarized valence double-zeta basis set (cc-pVDZ): https://www.basissetexchange.org
- Correlation-consistent polarized valence triple-zeta basis set (cc-pVTZ): https://www.basissetexchange.org

## Workflow steps

### Step 1: Build initial molecular geometries
- Role: process
- Action: Construct initial guess geometries for CH3OH, CH2O, HCOH, 1CH2, H2O, H2, and the transition state / dative complex structures (CH2O-H2 saddle point, HCOH-H2 saddle point, CH2-H2O dative complex, and CH2-H2O saddle point) using standard bond lengths and angles.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: CASSCF geometry optimizations and frequency calculations
- Role: process
- Action: Perform CASSCF gradient calculations to optimize geometries and compute harmonic vibrational frequencies for all stationary points using the cc-pVDZ basis set. Use active spaces as specified: six electrons in six orbitals for the CH2O+H2 and 1CH2+H2O channels, and four electrons in four orbitals for the HCOH+H2 channel. Include only the electrons in bonds being made or broken in the active space.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 3: CCI+Davidson electronic energy refinements
- Role: process
- Action: Using the CASSCF-optimized geometries, carry out internally contracted MRCI (CCI) single-point calculations with the multireference Davidson correction and the cc-pVTZ basis set for each stationary point to obtain refined electronic energies.
- Evidence: `/app/outputs/cci_raw_energies.txt`

### Step 4: Collect raw energies and zero-point corrections
- Role: scored (load-bearing)
- Action: Compile the CCI+Davidson energies and zero-point energies from the CASSCF harmonic frequencies for all stationary points into a single JSON artifact.
- Output file: `/app/outputs/raw_energies.json`
- Format: json
- Contract: Object with keys for each species: "CH3OH", "CH2O-H2", "CH2O+H2", "CH2-H2O", "1CH2+H2O", "HCOH-H2", "HCOH+H2". Each value is an object with fields: "cci_plus_davidson_hartree" (float, in hartree), "zero_point_energy_hartree" (float, in hartree).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raw_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raw_energies.json
- path: `/app/outputs/raw_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw CCI+Davidson electronic energies and CASSCF zero-point energies for each stationary point. The hidden checker computes relative energies (E_total = cci_plus_davidson_hartree + zero_point_energy_hartree) with respect to CH3OH, converts to kcal/mol, and compares the resulting values and the CH2-H2O vs 1CH2+H2O ordering to the paper's reported results.
- schema:
  - `type`: object
  - `required`: `CH3OH`, `CH2O-H2`, `CH2O+H2`, `CH2-H2O`, `1CH2+H2O`, `HCOH-H2`, `HCOH+H2`
  - `properties`:
    - `*`:
      - `type`: object
      - `required`: `cci_plus_davidson_hartree`, `zero_point_energy_hartree`
      - `properties`:
        - `cci_plus_davidson_hartree`:
          - `type`: number
          - `unit`: hartree
        - `zero_point_energy_hartree`:
          - `type`: number
          - `unit`: hartree

Notes: All energies are in hartree. The agent must compute CCI+Davidson energies and ZPE for all seven species; the checker then derives relative energies and verifies the barrier claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raw_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "CH3OH",
          "CH2O-H2",
          "CH2O+H2",
          "CH2-H2O",
          "1CH2+H2O",
          "HCOH-H2",
          "HCOH+H2"
        ],
        "properties": {
          "*": {
            "type": "object",
            "required": [
              "cci_plus_davidson_hartree",
              "zero_point_energy_hartree"
            ],
            "properties": {
              "cci_plus_davidson_hartree": {
                "type": "number",
                "unit": "hartree"
              },
              "zero_point_energy_hartree": {
                "type": "number",
                "unit": "hartree"
              }
            }
          }
        }
      },
      "description": "Raw CCI+Davidson electronic energies and CASSCF zero-point energies for each stationary point. The hidden checker computes relative energies (E_total = cci_plus_davidson_hartree + zero_point_energy_hartree) with respect to CH3OH, converts to kcal/mol, and compares the resulting values and the CH2-H2O vs 1CH2+H2O ordering to the paper's reported results."
    }
  ],
  "notes": "All energies are in hartree. The agent must compute CCI+Davidson energies and ZPE for all seven species; the checker then derives relative energies and verifies the barrier claim."
}
```

## How you are scored
Scoring is performed by a hidden verifier that reads your submitted `raw_energies.json`. The verifier independently recomputes relative energies from the raw CCI+Davidson and zero-point energies and compares them against reference values derived from the original study. Each relative energy is evaluated against an allowed tolerance; the verifier also checks whether the computed ordering of the CH2-H2O saddle point and the 1CH2+H2O asymptote is consistent with the absence of a barrier. The final score is a weighted combination: 80% from the accuracy of the individual relative energies and 20% from the barrier/no-barrier structural check. Simply reporting numbers — even correct ones — is not sufficient; the raw energies must be the output of the required electronic structure workflow.
