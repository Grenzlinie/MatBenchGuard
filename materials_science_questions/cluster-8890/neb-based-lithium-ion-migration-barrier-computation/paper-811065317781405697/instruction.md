# DFT Calculations of Li Storage Properties in 2D SQ-COPs

## Problem background
Developing high-capacity and environmentally friendly anode materials is a central challenge for lithium-ion batteries. Two-dimensional covalent organic frameworks (2D COFs) with large surface areas, open porous channels, and tunable chemistry are attractive candidates. The present work concerns three squaraine-linked COFs (SQ-COP-1, SQ-COP-2, SQ-COP-3) that differ in the heterocyclic node (B3O3, H3B3N3, and C3N3, respectively). The key material properties governing anode performance are the electronic conductivity (quantified by the band gap), the degree of charge transfer from intercalated Li to the framework (indicating lithiation strength), and the mobility of Li ions (the diffusion barrier). Computing these quantities across the three framework variants provides a comparative assessment that guides electrode design.

## Approach
The electronic structure is obtained from first-principles density functional theory (DFT) band structure calculations using a plane-wave implementation. The charge transfer upon lithiation is extracted by relaxing structures with lithium atoms placed in the pores and performing Bader charge analysis on the converged charge density. The Li diffusion kinetics are studied with the climbing-image nudged elastic band (CI-NEB) method, which yields the minimum energy barrier along a predefined migration path. All calculations can be carried out with open-source scientific codes and publicly available crystal structure coordinates.

## Reproduction target
Construct the periodic unit cells for SQ-COP-1, SQ-COP-2, and SQ-COP-3 from the atomic coordinates provided in the supporting information of the design study that introduced these frameworks (DOI: 10.1002/slct.201600533). Perform DFT band structure calculations for each pristine framework and extract the band gap values. Model lithiated systems by placing 26 Li atoms in the pores of SQ-COP-1 and SQ-COP-2, relax the structures, and compute the total Bader charge transferred from Li to the framework. Set up an NEB calculation for Li diffusion along the pore-center path (DP2) in SQ-COP-1 and determine the energy barrier. Finally, assemble the six numerical results (three band gaps in eV, two charge transfers in elementary charge e, one barrier in eV) into `/app/outputs/reproduced_quantities.json` following the exact JSON schema defined in the Workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- Atomic Simulation Environment (ASE): ase
- SQ-COP initial atomic structures: 10.1002/slct.201600533
- DFT pseudopotentials: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Prepare SQ-COP unit cells
- Role: process
- Action: Obtain the atomic coordinates / CIF files for SQ-COP-1, SQ-COP-2, SQ-COP-3 from the supporting information of the design paper (DOI: 10.1002/slct.201600533) and set up the periodic unit cells for DFT calculations.
- Evidence: `/app/outputs/structures_prepared.txt`

### Step 2: Run DFT band structure calculations
- Role: process
- Action: Perform self-consistent and band structure calculations for pristine SQ-COP-1, SQ-COP-2, SQ-COP-3 using an open-source DFT code (e.g., Quantum ESPRESSO). Retain the computed band gaps and raw output files.
- Evidence: `/app/outputs/band_output.log`

### Step 3: Optimize lithiated SQ-COP-1 and SQ-COP-2 with 26 Li atoms
- Role: process
- Action: Build systems with 26 Li atoms placed in the pores of SQ-COP-1 and SQ-COP-2. Perform geometry optimization using DFT to obtain relaxed structures.
- Evidence: `/app/outputs/lithiated_structures.optimized`

### Step 4: Bader charge analysis
- Role: process
- Action: Run the Bader charge partitioning code on the optimized charge densities of Li26@SQ-COP-1 and Li26@SQ-COP-2 to obtain the total charge transferred from Li atoms to the frameworks.
- Evidence: `/app/outputs/bader_results.log`

### Step 5: NEB diffusion barrier calculation for SQ-COP-1
- Role: process
- Action: Set up and run a nudged elastic band (NEB) calculation for Li diffusion along the pore-center path (DP2) in SQ-COP-1 using an open-source code (e.g., ASE interfaced with Quantum ESPRESSO). Obtain the energy barrier along the path.
- Evidence: `/app/outputs/neb_profile.dat`

### Step 6: Compile final reproduction quantities
- Role: scored (load-bearing)
- Action: Collect the band gap values (in eV) for the three frameworks from the band structure calculations, the total charge transfer (in e) for the Li26 systems from the Bader analysis, and the diffusion barrier (in eV) from the NEB calculation. Assemble these quantities into a single JSON file.
- Output file: `/app/outputs/reproduced_quantities.json`
- Format: json
- Contract: JSON object with keys: 'SQ-COP-1_band_gap_ev' (float), 'SQ-COP-2_band_gap_ev' (float), 'SQ-COP-3_band_gap_ev' (float), 'SQ-COP-1_charge_transfer_n26_e' (float), 'SQ-COP-2_charge_transfer_n26_e' (float), 'SQ-COP-1_diffusion_barrier_DP2_ev' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_quantities.json
- path: `/app/outputs/reproduced_quantities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Collection of reproduced quantities for numerical comparison with hidden paper-reported values.
- schema:
  - `type`: object
  - `required`: `SQ-COP-1_band_gap_ev`, `SQ-COP-2_band_gap_ev`, `SQ-COP-3_band_gap_ev`, `SQ-COP-1_charge_transfer_n26_e`, `SQ-COP-2_charge_transfer_n26_e`, `SQ-COP-1_diffusion_barrier_DP2_ev`
  - `properties`:
    - `SQ-COP-1_band_gap_ev`:
      - `type`: number
      - `unit`: eV
    - `SQ-COP-2_band_gap_ev`:
      - `type`: number
      - `unit`: eV
    - `SQ-COP-3_band_gap_ev`:
      - `type`: number
      - `unit`: eV
    - `SQ-COP-1_charge_transfer_n26_e`:
      - `type`: number
      - `unit`: e
    - `SQ-COP-2_charge_transfer_n26_e`:
      - `type`: number
      - `unit`: e
    - `SQ-COP-1_diffusion_barrier_DP2_ev`:
      - `type`: number
      - `unit`: eV

Notes: All quantities are absolute values derived from the DFT/NEB calculations. The checker compares them to the paper's reported numbers within tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "SQ-COP-1_band_gap_ev",
          "SQ-COP-2_band_gap_ev",
          "SQ-COP-3_band_gap_ev",
          "SQ-COP-1_charge_transfer_n26_e",
          "SQ-COP-2_charge_transfer_n26_e",
          "SQ-COP-1_diffusion_barrier_DP2_ev"
        ],
        "properties": {
          "SQ-COP-1_band_gap_ev": {
            "type": "number",
            "unit": "eV"
          },
          "SQ-COP-2_band_gap_ev": {
            "type": "number",
            "unit": "eV"
          },
          "SQ-COP-3_band_gap_ev": {
            "type": "number",
            "unit": "eV"
          },
          "SQ-COP-1_charge_transfer_n26_e": {
            "type": "number",
            "unit": "e"
          },
          "SQ-COP-2_charge_transfer_n26_e": {
            "type": "number",
            "unit": "e"
          },
          "SQ-COP-1_diffusion_barrier_DP2_ev": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Collection of reproduced quantities for numerical comparison with hidden paper-reported values."
    }
  ],
  "notes": "All quantities are absolute values derived from the DFT/NEB calculations. The checker compares them to the paper's reported numbers within tolerances."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts produced by each workflow stage and combines them into a final reward. The verifier reads `/app/outputs/reproduced_quantities.json` and compares each of the six reported numbers to expected reference values derived from the original study. Comparisons are made with tolerances that accommodate the legitimate spread arising from different DFT implementations, pseudopotentials, and numerical settings. The reward reflects how closely your reproduced quantities agree with the hidden reference; merely reporting numbers without executing the required computations will not receive credit.
