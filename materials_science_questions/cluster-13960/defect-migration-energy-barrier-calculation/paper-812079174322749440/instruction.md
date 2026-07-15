# DFT and NEB evaluation of Mg storage capacity, open-circuit voltage, and diffusion barrier in functionalized GYCTF monolayers

## Problem background
Rechargeable magnesium-ion batteries (MIBs) are promising alternatives to lithium-ion systems due to magnesium's high abundance, low cost, and large volumetric capacity. Developing high-capacity anode materials is a critical challenge. Two-dimensional graphyne-analogue covalent triazine frameworks (GYCTF) are a recently synthesised class of porous carbon-nitride networks with tunable structure. Evaluating their potential as MIB anodes requires computing several key properties: the maximum magnesium loading that a monolayer can stably accommodate, the resulting theoretical specific capacity, the average open-circuit voltage (OCV) during magnesiation, and the energy barrier for Mg-ion migration on the surface. These quantities determine whether a material can deliver high energy density and fast charge–discharge kinetics.

## Approach
This task reproduces the computational screening of pristine GYCTF and three chemically functionalised variants (GYCTF-CH₃, GYCTF-F, GYCTF-SH) using first-principles density-functional theory (DFT) with dispersion corrections. The methodological idea is:

- Use the B3LYP hybrid functional with the 6-31G(d) basis set and the Grimme D3 dispersion correction to obtain reliable total energies and equilibrium geometries.
- Build the unit cell of each bare monolayer from the known crystal structure of GYCTF. Substitute the terminating hydrogen atoms by –CH₃, –F, or –SH groups to obtain the functionalised sheets.
- Perform a coverage scan by adsorbing an increasing number of Mg atoms (one by one) onto each monolayer, fully relaxing the geometry at each coverage, and compute the adsorption energy. The exothermicity of adsorption determines the maximum stable magnesium loading.
- For the GYCTF-SH variant, run climbing-image nudged elastic band (CI‑NEB) calculations to determine the minimum-energy pathway for a single Mg atom diffusing between the most favourable binding sites.
- Post-process the total energies: compute the theoretical gravimetric capacity from the number of adsorbed Mg atoms and the molecular weight of the fully magnesiated unit cell, derive the open-circuit voltage profiles using the Nernst-based energy difference formula, and average the voltage steps to obtain the mean OCV for each functionalised sheet.

The workflow contrasts the four surfaces to reveal how chemical functionalisation tunes the coverage, capacity, voltage, and ion mobility.

## Reproduction target
Produce a single JSON file (`/app/outputs/reproduction_results.json`) that contains:

- The maximum number of Mg atoms stably adsorbed per unit cell for pristine GYCTF, GYCTF-CH₃, GYCTF-F, and GYCTF-SH.
- The theoretical gravimetric capacity (mAh g⁻¹) for each of the four variants.
- The average open-circuit voltage (V) for each functionalised monolayer (GYCTF-CH₃, GYCTF-F, GYCTF-SH).
- The four stepwise OCV values (V) for pristine GYCTF, ordered from the first to the fourth magnesiation step.
- The lowest Mg-ion diffusion barrier (eV) on the GYCTF-SH monolayer, as obtained from the CI‑NEB calculation.

All entries must be numerical values formatted according to the output contract. No other file is accepted for scoring.

## Assets

- GYCTF unit cell geometry: 10.1002/chem.201904651
- Quantum chemistry package (GAMESS, ORCA, or equivalent): https://www.msg.chem.iastate.edu/gamess/ (GAMESS) or https://orcaforum.kofo.mpg.de/app.php/portal (ORCA)
- 6-31G(d) basis set: bundled with most quantum chemistry packages
- Grimme D3 dispersion correction: built into many DFT programs (e.g., ORCA keyword D3); also standalone from https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3
- NEB implementation: available in GAMESS, ORCA, etc.

## Workflow steps

### Step 1: Geometry optimization of host GYCTF and functionalized monolayers
- Role: process
- Action: Perform DFT geometry optimization (B3LYP/6-31G(d) with Grimme D3 dispersion) for pristine GYCTF, GYCTF-CH3, GYCTF-F, and GYCTF-SH unit cells. Obtain relaxed geometries and total energies of each bare sheet.
- Evidence: `/app/outputs/host_optimization.log`

### Step 2: Mg adsorption on pristine GYCTF (coverage scan)
- Role: process
- Action: For pristine GYCTF, add Mg atoms sequentially at the centre of carbon six-membered rings until newly added Mg can no longer be adsorbed exothermically; optimize each nMg/GYCTF structure and compute total energies. Determine the maximum stable coverage and record the total energies of all stable magnesiated configurations.
- Evidence: `/app/outputs/bare_Mg_adsorption.log`

### Step 3: Mg adsorption on functionalized GYCTF (-CH3, -F, -SH)
- Role: process
- Action: For GYCTF-CH3, GYCTF-F, and GYCTF-SH, place Mg atoms incrementally starting from the most favourable sites identified in the paper (e.g., atop C-C bond for -CH3, bridging F atoms for -F, near triazine N for -SH) and optimize each structure. Compute total energies for every stable nMg@GYCTF-X configuration. Identify the maximum coverage for each variant.
- Evidence: `/app/outputs/func_Mg_adsorption.log`

### Step 4: NEB Mg diffusion barrier on GYCTF-SH
- Role: process
- Action: Run climbing-image nudged elastic band (CI-NEB) calculations for a single Mg atom moving between the most stable adsorption sites on the GYCTF-SH monolayer. Determine the minimum energy path and extract the lowest diffusion barrier height.
- Evidence: `/app/outputs/neb_diffusion.log`

### Step 5: Post-process: compute capacities, OCVs, and barrier
- Role: scored (load-bearing)
- Action: From the total energies of all nMg@GYCTF-X configurations obtained in previous steps, compute:
- maximum coverage (x) for each variant (pristine, -CH3, -F, -SH);
- theoretical gravimetric capacity C = 2*x*F / MW, where F = 96500 C/mol and MW is the molecular weight of the fully magnesiated unit cell;
- average OCV for each functionalized variant using the Nernst-based approximation;
- stepwise OCV values for pristine GYCTF;
- the lowest NEB diffusion barrier for Mg on GYCTF-SH.
Write all results to reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: {
  "max_coverage": {"pristine": int, "-CH3": int, "-F": int, "-SH": int},
  "capacity_mAh_g": {"pristine": float, "-CH3": float, "-F": float, "-SH": float},
  "average_OCV_V": {"-CH3": float, "-F": float, "-SH": float},
  "pristine_stepwise_OCV_V": [float, float, float, float],
  "GYCTF_SH_diffusion_barrier_eV": float
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the reproduced maximum Mg coverage, theoretical gravimetric capacities, average OCVs, stepwise OCV for pristine GYCTF, and Mg diffusion barrier on GYCTF-SH. Each quantity will be compared to the paper's reported value with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `max_coverage`:
      - `pristine`: int
      - `-CH3`: int
      - `-F`: int
      - `-SH`: int
    - `capacity_mAh_g`:
      - `pristine`: float
      - `-CH3`: float
      - `-F`: float
      - `-SH`: float
    - `average_OCV_V`:
      - `-CH3`: float
      - `-F`: float
      - `-SH`: float
    - `pristine_stepwise_OCV_V`: array of 4 floats
    - `GYCTF_SH_diffusion_barrier_eV`: float

Notes: The hidden checker uses result-level comparison (T0) with tolerances: ±2% for capacity, ±0.05 V for OCV, ±0.05 eV for diffusion barrier, ±1 for coverage counts. Additionally, ordering conditions are enforced for capacities and diffusion barriers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "max_coverage": {
            "pristine": "int",
            "-CH3": "int",
            "-F": "int",
            "-SH": "int"
          },
          "capacity_mAh_g": {
            "pristine": "float",
            "-CH3": "float",
            "-F": "float",
            "-SH": "float"
          },
          "average_OCV_V": {
            "-CH3": "float",
            "-F": "float",
            "-SH": "float"
          },
          "pristine_stepwise_OCV_V": "array of 4 floats",
          "GYCTF_SH_diffusion_barrier_eV": "float"
        }
      },
      "description": "JSON file containing the reproduced maximum Mg coverage, theoretical gravimetric capacities, average OCVs, stepwise OCV for pristine GYCTF, and Mg diffusion barrier on GYCTF-SH. Each quantity will be compared to the paper's reported value with appropriate tolerances."
    }
  ],
  "notes": "The hidden checker uses result-level comparison (T0) with tolerances: ±2% for capacity, ±0.05 V for OCV, ±0.05 eV for diffusion barrier, ±1 for coverage counts. Additionally, ordering conditions are enforced for capacities and diffusion barriers."
}
```

## How you are scored
After you submit `reproduction_results.json`, a hidden verifier reads the file and compares each numeric entry against a set of expected reference values. The comparison uses per-quantity tolerances that account for legitimate differences between DFT implementations. Each correctly matched field contributes to the overall score. Additionally, the verifier checks that the capacities of the four variants follow the known qualitative ordering induced by the different functional groups, and that the diffusion barriers obey the expected ranking as well. The final reward is a weighted sum of the individual scores; shape errors or missing fields receive zero credit for the affected entries.
