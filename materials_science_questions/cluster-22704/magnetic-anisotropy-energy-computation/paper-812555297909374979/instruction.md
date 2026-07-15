# Magnetic Anisotropy Imprinting in FeRh/CoFeB Heterostructures: Computational Reproduction

## Problem background
Magnetic anisotropy is a fundamental property that dictates the performance of magnetic materials, from permanent magnets to soft magnets. In crystalline materials, magnetocrystalline anisotropy arises from spin-orbit coupling and reflects the symmetry of the crystal lattice. Amorphous materials lack long-range order and therefore normally exhibit negligible magnetocrystalline anisotropy. However, when an amorphous ferromagnetic layer is grown on an epitaxial antiferromagnet or ferromagnet, interfacial exchange coupling can imprint a magnetic anisotropy onto the amorphous layer. This task computationally investigates such an effect in an FeRh/CoFeB heterostructure. The study consists of two parts: (1) first-principles density-functional theory (DFT) calculations of the magnetocrystalline anisotropy energy (MAE) of FeRh in antiferromagnetic (AF) and ferromagnetic (FM) phases, both in the cubic bulk and when epitaxially strained to match a MgO substrate; and (2) Monte Carlo simulations of the angular dependence of coercivity in a soft-magnet/hard-magnet bilayer, where the hard magnet has in-plane fourfold anisotropy. The goal is to determine the MAE signs and easy axes for FeRh, and to observe how the coercivity angular dependence changes when the hard magnet's easy axes are rotated between the AF and FM configurations.

## Approach
The computational approach combines two complementary methods. First, DFT calculations with spin-orbit coupling are performed using an open-source plane-wave code (Quantum ESPRESSO) with the GGA-PBE exchange-correlation functional. Total energies are computed for FeRh in the CsCl structure with magnetic moments aligned along the <100> and <110> crystal directions. The MAE per unit volume is obtained as the energy difference between the two orientations. This is carried out for the cubic lattice parameters obtained from geometry optimization, as well as for tetragonally distorted cells that mimic the epitaxial strain induced by a MgO substrate. The sign of MAE determines whether the easy axis is <100> or <110>. Second, a Monte Carlo simulation is implemented for a bilayer of classical spins in a two-dimensional square lattice. The soft magnet (SM) layer has a uniaxial in-plane anisotropy, while the hard magnet (HM) layer has an in-plane fourfold anisotropy. The spin Hamiltonian includes intralayer exchange, interlayer (interfacial) exchange, anisotropy terms, and a Zeeman term for an external magnetic field. Magnetization hysteresis loops are simulated at low temperature as a function of the in-plane field angle. Coercivity is extracted from these loops for a single SM layer and for two bilayer configurations where the HM layer represents an AF-like state and an FM-like state (different anisotropy strengths and exchange sign). The angular dependence of coercivity is then analyzed to identify symmetry (e.g., fourfold periodicity) and any phase shift between the two bilayer cases.

## Reproduction target
Produce two final artifacts. 1) mae_results.json: a JSON object containing the computed MAE values (in J/m³ or meV/unit cell) and easy-axis assignments for four FeRh configurations: cubic AF, cubic FM, epitaxially strained AF, and epitaxially strained FM. The object must have keys cubic_AF_MAE, cubic_FM_MAE, strained_AF_MAE, strained_FM_MAE (float) and cubic_AF_easy_axis, cubic_FM_easy_axis, strained_AF_easy_axis, strained_FM_easy_axis (string). 2) mc_coercivity.csv: a CSV file with columns phi_deg (integer), Hc_single_SM (float), Hc_SM_AF_bilayer (float), Hc_SM_FM_bilayer (float), containing the coercivity as a function of in-plane field angle φ (0° to 360°) for the three simulated systems. The artifacts must be obtained by executing the corresponding workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials for Fe and Rh (GGA-PBE): https://www.materialscloud.org/discover/sssp/table
- numpy: numpy

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for bulk FeRh in CsCl structure for both AF and FM spin arrangements using Quantum ESPRESSO with GGA-PBE functional and appropriate pseudopotentials. Record optimized lattice parameters.
- Evidence: `/app/outputs/optimization_log.json`

### Step 2: MAE calculation
- Role: scored (load-bearing)
- Action: Using the optimized structures from step 1, set up non-collinear DFT calculations with spin-orbit coupling in Quantum ESPRESSO to compute total energies with magnetization along <100> and <110> directions for both cubic and epitaxially strained (tetragonally distorted to match MgO lattice) FeRh. Compute MAE = E_<100> - E_<110> for each case (cubic AF, cubic FM, strained AF, strained FM) and determine the easy axis. Output results to 'mae_results.json'.
- Output file: `/app/outputs/mae_results.json`
- Format: json
- Contract: JSON object with keys: cubic_AF_MAE (float), cubic_FM_MAE (float), strained_AF_MAE (float), strained_FM_MAE (float), cubic_AF_easy_axis (string), cubic_FM_easy_axis (string), strained_AF_easy_axis (string), strained_FM_easy_axis (string).
- Scoring: scored by hidden verifier

### Step 3: Monte Carlo simulation of bilayer coercivity
- Role: scored
- Action: Write a Monte Carlo simulation for a bilayer of soft magnet (SM) and hard magnet (HM) with in-plane spins. Use the parameters: K_SM = 0.0375 J_SM, K_HM = 1.0 J_SM (AF-like HM), K_HM = -0.2 J_SM (FM-like HM), J_SM = 1.0, J_HM = ±0.1, J_IF = 1.0. Simulate coercivity Hc as a function of in-plane field angle φ (0–360°). Output 'mc_coercivity.csv' with columns phi_deg, Hc_single_SM, Hc_SM_AF_bilayer, Hc_SM_FM_bilayer.
- Output file: `/app/outputs/mc_coercivity.csv`
- Format: csv
- Contract: CSV columns: phi_deg (int), Hc_single_SM (float), Hc_SM_AF_bilayer (float), Hc_SM_FM_bilayer (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mae_results.json`
- `/app/outputs/mc_coercivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mae_results.json
- path: `/app/outputs/mae_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed MAE values and easy-axis assignments for FeRh.
- schema:
  - `type`: object
  - `required`:
    - `cubic_AF_MAE`: float
    - `cubic_FM_MAE`: float
    - `strained_AF_MAE`: float
    - `strained_FM_MAE`: float
    - `cubic_AF_easy_axis`: string
    - `cubic_FM_easy_axis`: string
    - `strained_AF_easy_axis`: string
    - `strained_FM_easy_axis`: string

### mc_coercivity.csv
- path: `/app/outputs/mc_coercivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Monte Carlo simulated coercivity angular dependence.
- schema:
  - `type`: table
  - `required_columns`: `phi_deg`, `Hc_single_SM`, `Hc_SM_AF_bilayer`, `Hc_SM_FM_bilayer`

Notes: Scoring verifies MAE sign and relative ordering (T3) and checks that the Monte Carlo curves show fourfold periodicity and a 45° phase shift. Absolute numerical tolerance is not applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mae_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "cubic_AF_MAE": "float",
          "cubic_FM_MAE": "float",
          "strained_AF_MAE": "float",
          "strained_FM_MAE": "float",
          "cubic_AF_easy_axis": "string",
          "cubic_FM_easy_axis": "string",
          "strained_AF_easy_axis": "string",
          "strained_FM_easy_axis": "string"
        }
      },
      "description": "Computed MAE values and easy-axis assignments for FeRh."
    },
    {
      "file": "mc_coercivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_deg",
          "Hc_single_SM",
          "Hc_SM_AF_bilayer",
          "Hc_SM_FM_bilayer"
        ]
      },
      "description": "Monte Carlo simulated coercivity angular dependence."
    }
  ],
  "notes": "Scoring verifies MAE sign and relative ordering (T3) and checks that the Monte Carlo curves show fourfold periodicity and a 45° phase shift. Absolute numerical tolerance is not applied."
}
```

## How you are scored
A hidden verifier independently scores each artifact and computes a final weighted reward between 0 and 1. For mae_results.json, the verifier performs a structural audit: it checks the sign of each MAE (positive => easy axis <110>, negative => easy axis <100>) and verifies that the relative ordering of MAE magnitudes across the four configurations is physically consistent (e.g., the strained-AF MAE magnitude should be larger than the cubic-AF magnitude, the strained-FM magnitude smaller than the cubic-FM magnitude). For mc_coercivity.csv, the verifier fits a fourfold cosine model to each coercivity–angle curve and checks that the curves exhibit the correct periodicity (approximately 90°) and that the phase difference between the two bilayer curves matches the physical expectation (i.e., reflects the rotation of the hard magnet's easy axes between the AF-like and FM-like cases). Exact numerical agreement is not required; implementation-dependent variations are tolerated within generous bounds. Both output files must be present in the specified format and locations to be evaluated.
