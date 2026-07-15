# CO Oxidation on 2D Transition-Metal Phthalocyanine Sheets: Poisoning Resistance Study

## Problem background
Two-dimensional transition-metal phthalocyanine (TMPc) sheets are structurally well-defined organometallic frameworks that expose a single TM cation per unit cell, making them attractive candidates for heterogeneous catalysis. For low-temperature CO oxidation, a good catalyst must bind and activate O2 while avoiding irreversible poisoning by CO. This study investigates the catalytic potential of 2D TMPc sheets with central 3d metals Cr, Mn, and Fe. By computing adsorption energies of CO and O2, coadsorption energies, and energy barriers for the full catalytic cycle, the work aims to identify whether any of these materials can serve as a poison-resistant CO oxidation catalyst and to determine the associated reaction barriers.

## Approach
The investigation employs spin-polarized density functional theory (DFT) with the GGA-PBE exchange-correlation functional. Periodic two-dimensional unit cells are built for TMPc (TM = Cr, Mn, Fe) from standard phthalocyanine geometry. Adsorption energies E_ads are obtained from total-energy differences: E_ads = E(TMPc+adsorbate) - E(TMPc) - E(adsorbate), after full geometry optimization of the isolated sheet, the free molecule, and the combined system. CO poisoning resistance is quantified by the coadsorption energy E_coad = E(TMPc+CO+O2) - E(TMPc+CO) - E(O2); a negative value indicates that O2 can bind to a CO-precovered sheet, thereby displacing CO. For systems that pass this test, the catalytic cycle is examined: a Langmuir-Hinshelwood (LH) step (CO + O2 → OOCO intermediate → CO2 + O) followed by an Eley-Rideal (ER) step (CO + O → CO2). Transition states for each elementary step are located using LST/QST and nudged-elastic-band (NEB) methods; each transition state is verified to have exactly one imaginary frequency. All DFT calculations are to be performed with an open-source plane-wave / pseudopotential code such as Quantum ESPRESSO, using standard PBE pseudopotentials (e.g., the SSSP efficiency library). The final comparison is between the three metals Cr, Mn, and Fe to see which, if any, can function as a poison-resistant low-temperature CO oxidation catalyst.

## Reproduction target
Compute the following energetic quantities (all in eV) by running the DFT workflow described above and write them to a single JSON file `/app/outputs/results.json`:
- `Eads_CO_CrPc`, `Eads_O2_CrPc`: adsorption energies of CO and O2 on 2D CrPc
- `Eads_CO_MnPc`, `Eads_O2_MnPc`: adsorption energies of CO and O2 on 2D MnPc
- `Eads_CO_FePc`, `Eads_O2_FePc`: adsorption energies of CO and O2 on 2D FePc
- `E_coad_CrPc`: coadsorption energy of CO + O2 on 2D CrPc (as defined above)
- `Ea_LH_TS1`, `Ea_LH_TS2`: energy barriers (relative to the coadsorbed initial state) for the two transition states of the Langmuir-Hinshelwood step on CrPc
- `Ea_ER_TS`: energy barrier for the Eley-Rideal step on CrPc (relative to the CO + O coadsorbed state)
The JSON file must contain exactly these ten numeric fields. No additional keys are required. All values are to be reported in electronvolts (eV), rounded to reasonable precision (e.g., 0.001 eV). The hidden verifier will compare your computed numbers against reference values derived from the original study; no prior knowledge of the paper's reported numbers is available in this instruction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build structural models
- Role: process
- Action: Construct periodic unit cells for 2D CrPc, MnPc, FePc sheets using standard phthalocyanine geometry and create structures for CO and O2 molecules. Prepare atomic coordinates and lattice vectors.
- Evidence: `/app/outputs/structures.json`

### Step 2: Optimize clean sheets and gas molecules
- Role: process
- Action: Perform spin-polarized DFT geometry optimization (GGA-PBE functional, appropriate k-point grid and energy cutoff) for isolated CrPc, MnPc, FePc sheets and free CO, O2 molecules. Obtain total energies and relaxed geometries.
- Evidence: `/app/outputs/opt_energies.json`

### Step 3: Compute adsorption energies of CO and O2 on TMPc sheets
- Role: process
- Action: Place CO and O2 on each optimized TMPc sheet (CrPc, MnPc, FePc) at the TM site, optimize the adsorbed geometries, and record total energies of the complexes.
- Evidence: `/app/outputs/ads_complex_energies.json`

### Step 4: Coadsorption and transition state searches on CrPc
- Role: process
- Action: For CrPc: (a) compute coadsorbed CO+O2 geometry and total energy; (b) locate transition states TS1 and TS2 for the Langmuir-Hinshelwood step (CO+O2→OOCO→CO2+O) and TS for the Eley-Rideal step (CO+O→CO2) using LST/QST and NEB methods; verify each TS has exactly one imaginary frequency. Record all energies.
- Evidence: `/app/outputs/ts_energies.json`

### Step 5: Compile key results
- Role: scored (load-bearing)
- Action: Compute adsorption energies Eads = E_TMPc+mol - E_TMPc - E_mol for CO and O2 on CrPc, MnPc, FePc. Compute coadsorption energy E_coad = E_TMPc+CO+O2 - E_TMPc+CO - E_O2 for CrPc. Extract energy barriers from TS searches. Write all values to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"Eads_CO_CrPc": float, "Eads_O2_CrPc": float, "Eads_CO_MnPc": float, "Eads_O2_MnPc": float, "Eads_CO_FePc": float, "Eads_O2_FePc": float, "E_coad_CrPc": float, "Ea_LH_TS1": float, "Ea_LH_TS2": float, "Ea_ER_TS": float}
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
- description: JSON file containing computed adsorption energies (Eads), coadsorption energy (E_coad), and energy barriers (Ea) for CO oxidation on 2D TMPc sheets. All values are in eV.
- schema:
  - `type`: object
  - `required`:
    - `Eads_CO_CrPc`: float
    - `Eads_O2_CrPc`: float
    - `Eads_CO_MnPc`: float
    - `Eads_O2_MnPc`: float
    - `Eads_CO_FePc`: float
    - `Eads_O2_FePc`: float
    - `E_coad_CrPc`: float
    - `Ea_LH_TS1`: float
    - `Ea_LH_TS2`: float
    - `Ea_ER_TS`: float

Notes: The values are compared against paper-reported references with tolerances of 0.15 eV for adsorption/coadsorption energies and 0.10 eV for energy barriers. The coadsorption energy for CrPc must be negative.

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
          "Eads_CO_CrPc": "float",
          "Eads_O2_CrPc": "float",
          "Eads_CO_MnPc": "float",
          "Eads_O2_MnPc": "float",
          "Eads_CO_FePc": "float",
          "Eads_O2_FePc": "float",
          "E_coad_CrPc": "float",
          "Ea_LH_TS1": "float",
          "Ea_LH_TS2": "float",
          "Ea_ER_TS": "float"
        }
      },
      "description": "JSON file containing computed adsorption energies (Eads), coadsorption energy (E_coad), and energy barriers (Ea) for CO oxidation on 2D TMPc sheets. All values are in eV."
    }
  ],
  "notes": "The values are compared against paper-reported references with tolerances of 0.15 eV for adsorption/coadsorption energies and 0.10 eV for energy barriers. The coadsorption energy for CrPc must be negative."
}
```

## How you are scored
A hidden verifier inspects all artifacts you produce under `/app/outputs`. The final reward (a number between 0 and 1) is built from several weighted components:
1. **Presence and shape checks** (low weight): The verifier confirms that every required intermediate file (structures.json, opt_energies.json, ads_complex_energies.json, ts_energies.json) and the final results.json exist and have the correct format. Missing or malformed files incur a penalty.
2. **Process consistency checks** (moderate weight): The verifier cross-checks that the reported intermediate energies are internally consistent (e.g., that the complex energies and reference energies are compatible with the adsorption formulas you apply in step 5). Evidence of fabrication (e.g., total energies that don’t add up) lowers your score.
3. **Quantitative comparison of results.json** (highest weight): Each of the ten numerical values in results.json is compared against a hidden reference (derived from the original study) using a tolerance appropriate for DFT re-implementations (the tolerance is **not** disclosed to you). You receive full credit for a value that falls within the tolerance band; the reward for that field decreases gradually if the deviation exceeds the tolerance. The coadsorption energy `E_coad_CrPc` and the highest energy barrier among `Ea_LH_TS1`, `Ea_LH_TS2`, and `Ea_ER_TS` carry extra weight because they directly address the poisoning resistance and catalytic activity.
4. **Additional constraint**: The verifier checks that `E_coad_CrPc` is negative; a non-negative value yields zero credit for that field regardless of how close it is to the reference.
*Important*: You must actually run the DFT calculations and produce all the intermediate evidence. Simply guessing or hardcoding the required numbers from prior knowledge (if any) will be detected by the consistency checks and will result in a low score even if the final numbers happen to be close to the hidden reference. The only path to a high reward is an honest computational workflow.
