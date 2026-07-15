# DFT Computed Gibbs Free Energies for H2O2 Decomposition on Doped Graphene

## Problem background
Carbon-based nanozymes such as reduced graphene oxide (rGO) offer low-cost alternatives to natural peroxidases but suffer from low catalytic activity. Heteroatom doping can increase activity, and N- and B-codoping yields particularly enhanced peroxidase-like activity. Density functional theory (DFT) calculations can provide a microscopic understanding by computing Gibbs free energy changes during the H₂O₂ decomposition reaction and identifying the rate-determining step's energy barrier. Reproducing these DFT-computed ΔG values for the key reaction step on different doped graphene models will shed light on the origin of the activity improvement.

## Approach
Construct atomic cluster models representing the active regions of graphene with specific doping configurations: pristine rGO (basal plane carbon), B-doped rGO with a single boron atom in a BC₃ motif on the basal plane, N-doped rGO with a single quaternary (graphitic) nitrogen on the basal plane, and N,B-codoped rGO with a boron atom adjacent to a pyridinic nitrogen at the edge. For each model, perform spin-polarized DFT calculations using a generalized gradient approximation (e.g., PBE functional) with van der Waals corrections and an implicit solvent model (COSMO) representing aqueous conditions (dielectric constant 78.54). Compute the Gibbs free energy change for the reaction step H₂O₂(aq) → 2 OH* adsorbed on the identified active site of each model (carbon for rGO, boron for B-rGO, carbon adjacent to quaternary N for N(q)-rGO, and boron adjacent to pyridinic N for NB-rGO). The resulting ΔG values quantify the thermodynamic driving force for this rate-determining step; comparing them across the four systems reveals how doping modifies the activity.

## Reproduction target
Compute the Gibbs free energy change ΔG (in eV) for the formation of two adsorbed OH* from H₂O₂ on the basal-plane active sites of the four doped graphene models listed. Report the four values in a JSON file `/app/outputs/dft_results.json` with keys `rGO_basal`, `B_rGO_basal`, `Nq_rGO_basal`, and `NB_rGO_B_atom`. The computed ΔG values and their relative ordering will be evaluated against hidden reference data.

## Assets

- Quantum ESPRESSO (or other open-source DFT code, e.g., GPAW, ABINIT; VASP if licensed): https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
- Python 3: python3

## Workflow steps

### Step 1: Build graphene cluster models
- Role: process
- Action: Construct atomic cluster models for pristine rGO (basal plane), B-rGO (single B atom in BC3 site on basal plane), N(q)-rGO (single quaternary N on basal plane), and NB-rGO (single B atom adjacent to a pyridinic N at the edge). The models should reflect the doping states described in the paper: B in a BC3 motif, N as quaternary (graphitic) on the basal plane, and pyridinic at the edge.
- Evidence: `/app/outputs/models_structures.xyz`

### Step 2: DFT calculations for reaction intermediates
- Role: process
- Action: For each model, perform spin-polarized DFT calculations to obtain electronic ground-state energies and vibrational frequencies/thermal corrections for the initial state (H2O2 in solution + pristine surface) and the final state (two adsorbed OH* on the surface). Use an appropriate exchange-correlation functional (e.g., PBE), van der Waals correction, and an implicit aqueous solvent model (e.g., COSMO) with water dielectric constant 78.54. Include temperature and pH conditions (25 °C, pH 4) as needed for Gibbs free energy corrections.
- Evidence: `/app/outputs/dft_raw_energies.json`

### Step 3: Compute Gibbs free energy changes
- Role: scored (load-bearing)
- Action: Using the DFT total energies and thermal corrections from step 2, calculate the Gibbs free energy change ΔG for the reaction step H2O2(aq) → 2OH* on the basal-plane active site of each model (C atom for rGO, B atom for B-rGO, C adjacent to quaternary N for N(q)-rGO, B atom adjacent to pyridinic N for NB-rGO). Report the ΔG values in eV.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"rGO_basal": <float, ΔG in eV>, "B_rGO_basal": <float>, "Nq_rGO_basal": <float>, "NB_rGO_B_atom": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gibbs free energy change ΔG for the rate-determining step (formation of two adsorbed OH*) on the basal-plane active sites of four models: pristine rGO, B-doped rGO, N-doped rGO (quaternary N), and N,B-codoped rGO (B adjacent to pyridinic N).
- schema:
  - `type`: object
  - `required`:
    - `rGO_basal`: number (ΔG in eV)
    - `B_rGO_basal`: number (ΔG in eV)
    - `Nq_rGO_basal`: number (ΔG in eV)
    - `NB_rGO_B_atom`: number (ΔG in eV)
  - `additionalProperties`: False

Notes: The values correspond to the paper's Figure 3 and associated text. The checker compares to hidden reference values within a tolerance appropriate for DFT code/functional differences, and also verifies the relative trend (NB_rGO_B_atom ≤ B_rGO_basal ≤ Nq_rGO_basal ≤ rGO_basal).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "rGO_basal": "number (ΔG in eV)",
          "B_rGO_basal": "number (ΔG in eV)",
          "Nq_rGO_basal": "number (ΔG in eV)",
          "NB_rGO_B_atom": "number (ΔG in eV)"
        },
        "additionalProperties": false
      },
      "description": "Gibbs free energy change ΔG for the rate-determining step (formation of two adsorbed OH*) on the basal-plane active sites of four models: pristine rGO, B-doped rGO, N-doped rGO (quaternary N), and N,B-codoped rGO (B adjacent to pyridinic N)."
    }
  ],
  "notes": "The values correspond to the paper's Figure 3 and associated text. The checker compares to hidden reference values within a tolerance appropriate for DFT code/functional differences, and also verifies the relative trend (NB_rGO_B_atom ≤ B_rGO_basal ≤ Nq_rGO_basal ≤ rGO_basal)."
}
```

## How you are scored
A hidden verifier will read your submitted `dft_results.json` and compare each of the four ΔG values to independently known reference numbers (the paper's own computed values, unknown to you). Each number is compared within a tolerance that accounts for legitimate differences between DFT codes and functionals; exact reproduction of the reference values is not required. In addition, the verifier checks that the relative ordering of the four ΔG values (i.e., which system is most or least favorable) matches the expected trend. Each of the four values carries equal weight in the final score (total of 1.0). If a value is missing or far outside the tolerance, that weight is lost. The reward reflects how many values lie within tolerance and whether the ordering is correct; no single number needs to be hit exactly.
