# Periodic DFT study of hydrogenated rutile TiO2(110): adsorption energies, spin localization, and NH3 acidity

## Problem background
Rutile titanium dioxide (TiO2) is a widely used reducible oxide in catalysis and photovoltaics. Its (110) surface is the most stable and reactive surface. Understanding how atomic hydrogen adsorbs on this surface is key to controlling surface chemistry, protonation, and catalytic activity. Two distinct adsorption modes are possible: (1) proton-type adsorption where H binds to surface oxygen atoms, potentially reducing Ti(IV) to Ti(III); (2) heterolytic adsorption where H⁺ binds to O and H⁻ binds to a surface Ti. The goal of this task is to computationally determine the relative stability of these modes, the electronic nature of the reduction (i.e., whether it manifests as spin localization on Ti rather than large charge transfer), and how hydrogenation affects the Lewis acidity of the surface using NH3 as a probe molecule. Your calculations must provide the adsorption energies, spin populations, and NH3 adsorption energies; the hidden verifier will then assess whether the results exhibit the expected physical trends.

## Approach
This task uses periodic density functional theory (DFT) with the Perdew-Wang 1991 (PW91) generalized gradient approximation (GGA) functional. The TiO2(110) surface is modeled by periodic slabs of 3, 6, and 9 atomic layers constructed from bulk rutile lattice constants. The top three layers of the clean slabs are first relaxed. Three hydrogen adsorption configurations are investigated: the R mode (both H atoms adsorbed on bridging surface oxygen atoms), the H1 mode (one H on an oxygen and one H on a titanium), and the H2 mode (a different arrangement of H on O and H on Ti). For each configuration and slab thickness, geometry optimization is performed to obtain total energies; the adsorption energy per two H atoms is computed using the energy of an isolated H atom as reference. For the R mode, Mulliken (or Bader) atomic spin populations are extracted to characterize the spin localization. Finally, NH3 co-adsorption is studied on clean and R-hydrogenated surfaces for the 3L and 6L slabs to assess the change in Lewis acidity. All calculations are performed with a periodic DFT code such as Quantum ESPRESSO using pseudopotentials. The comparison of interest is the relative ordering of the adsorption modes, the extent of spin on Ti vs. H in the R mode, and the direction of the NH3 adsorption energy shift upon hydrogenation.

## Reproduction target
The primary deliverables are three CSV files produced by performing the DFT calculations described in the workflow steps. Specifically:
- adsorption_energies.csv: for each slab thickness (3, 6, 9) and each configuration (R, H1, H2), report the computed adsorption energy per two H atoms.
- spin_analysis.csv: for the R configuration on 3L and 6L slabs, report the maximum absolute spin population (in e) on any Ti atom and on any H atom.
- nh3_adsorption.csv: for the 3L and 6L slabs, report the NH3 adsorption energy on the clean surface and on the H-covered (R model) surface.
Your calculations must accurately reflect the physical chemistry of the system. The hidden verifier will check whether your computed values satisfy certain structural and threshold relationships that follow from the underlying physics (e.g., which adsorption mode is most stable, the magnitude of spin localization on Ti, and how NH3 binding changes with hydrogenation). The objective is to produce DFT results that are consistent with the expected behavior of this system; you are not required to guess any target value.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PW91 ultrasoft pseudopotentials for Ti, O, H (SSSP efficiency v1.1): https://archive.materialscloud.org/record/2019.0028/v2

## Workflow steps

### Step 1: Slab model construction
- Role: process
- Action: Build periodic slab models of rutile TiO2(110) with 3, 6, and 9 atomic layers using bulk lattice parameters a=6.4312 Å, c=3.0065 Å. Create primitive and double cells and initial atomic positions for clean slabs and the three H adsorption configurations (R, H1, H2) with one H per surface bridging O.
- Evidence: `/app/outputs/initial_slabs.xyz`

### Step 2: Clean slab relaxation
- Role: process
- Action: For each slab thickness (3L, 6L, 9L), relax the top three layers of the clean slab using Quantum ESPRESSO pw.x with PW91 GGA and ultrasoft pseudopotentials. Use a vacuum gap >15 Å and a suitable k-grid. Obtain relaxed geometries and total energies.
- Evidence: `/app/outputs/relaxed_slabs.xyz`

### Step 3: H adsorption energy calculation
- Role: scored
- Action: For each slab thickness and each adsorption model (R, H1, H2), perform geometry optimization (relax H positions and surface atoms) and final SCF to obtain total energy of the hydrogenated slab. Compute adsorption energy per two H atoms as E_ads = 2*E(H) + E(slab) - E(2H/slab). Output a CSV with columns: slab, model, E_ads.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: slab:int, model:string, E_ads:float
- Scoring: scored by hidden verifier

### Step 4: Spin polarization analysis for R model
- Role: scored (load-bearing)
- Action: For the relaxed R model on 3L and 6L slabs, compute Mulliken (or Bader) atomic spin populations (α-β). Extract the maximum absolute spin on any Ti atom and the maximum absolute spin on any H atom. Output a CSV with columns: slab, max_abs_spin_Ti, max_abs_spin_H.
- Output file: `/app/outputs/spin_analysis.csv`
- Format: csv
- Contract: slab:int, max_abs_spin_Ti:float, max_abs_spin_H:float
- Scoring: scored by hidden verifier

### Step 5: NH3 co-adsorption acidity test
- Role: scored (load-bearing)
- Action: For 3L and 6L slabs, compute the adsorption energy of NH3 on the clean TiO2 surface (NH3 on undercoordinated Ti) and on the R-model hydrogenated surface (coverage 1 NH3 and 1 H). Relax geometries and obtain total energies. Compute E_ads_NH3 relative to isolated NH3 and the corresponding slab. Output a CSV with columns: slab, system (clean or H_covered), E_ads_NH3.
- Output file: `/app/outputs/nh3_adsorption.csv`
- Format: csv
- Contract: slab:int, system:string, E_ads_NH3:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/spin_analysis.csv`
- `/app/outputs/nh3_adsorption.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hydrogen adsorption energies per two H atoms for each slab thickness and adsorption model. Checker compares ordering (R > H1, R > H2) and values to hidden paper reference within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `slab`, `model`, `E_ads`
  - `units`:
    - `E_ads`: eV

### spin_analysis.csv
- path: `/app/outputs/spin_analysis.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum absolute Mulliken (or Bader) spin populations on Ti and H atoms for the R model on selected slabs. Checker verifies that for at least one slab, max_abs_spin_Ti > 0.5 e and max_abs_spin_H < 0.1 e.
- schema:
  - `type`: table
  - `required_columns`: `slab`, `max_abs_spin_Ti`, `max_abs_spin_H`
  - `units`:
    - `max_abs_spin_Ti`: e
    - `max_abs_spin_H`: e

### nh3_adsorption.csv
- path: `/app/outputs/nh3_adsorption.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: NH3 adsorption energies on clean and hydrogenated TiO2(110) slabs. Checker verifies that for each slab, E_ads_NH3(clean) - E_ads_NH3(H_covered) > 0.3 eV.
- schema:
  - `type`: table
  - `required_columns`: `slab`, `system`, `E_ads_NH3`
  - `units`:
    - `E_ads_NH3`: eV

Notes: All checks are performed at the result level (T0) against the paper's VASP PW91 reference values, with tolerances absorbing code-to-code spread. Process steps must be executed to reach the scored artifacts; the spin and NH3 steps are load-bearing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "slab",
          "model",
          "E_ads"
        ],
        "units": {
          "E_ads": "eV"
        }
      },
      "description": "Hydrogen adsorption energies per two H atoms for each slab thickness and adsorption model. Checker compares ordering (R > H1, R > H2) and values to hidden paper reference within tolerance."
    },
    {
      "file": "spin_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "slab",
          "max_abs_spin_Ti",
          "max_abs_spin_H"
        ],
        "units": {
          "max_abs_spin_Ti": "e",
          "max_abs_spin_H": "e"
        }
      },
      "description": "Maximum absolute Mulliken (or Bader) spin populations on Ti and H atoms for the R model on selected slabs. Checker verifies that for at least one slab, max_abs_spin_Ti > 0.5 e and max_abs_spin_H < 0.1 e."
    },
    {
      "file": "nh3_adsorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "slab",
          "system",
          "E_ads_NH3"
        ],
        "units": {
          "E_ads_NH3": "eV"
        }
      },
      "description": "NH3 adsorption energies on clean and hydrogenated TiO2(110) slabs. Checker verifies that for each slab, E_ads_NH3(clean) - E_ads_NH3(H_covered) > 0.3 eV."
    }
  ],
  "notes": "All checks are performed at the result level (T0) against the paper's VASP PW91 reference values, with tolerances absorbing code-to-code spread. Process steps must be executed to reach the scored artifacts; the spin and NH3 steps are load-bearing."
}
```

## How you are scored
The hidden verifier reads your three CSV files. It first validates that each file contains the required columns, data types, and the correct number of rows. Then it scores each artifact independently against hidden criteria. For adsorption_energies.csv, it checks that the relative ordering of the adsorption energies across configurations follows the pattern that the physics predicts; a correct relative ordering earns high credit, while incorrect ordering results in partial or no credit. For spin_analysis.csv, it verifies that the spin populations on Ti and H exceed certain hidden thresholds that indicate the expected spin localization behavior. For nh3_adsorption.csv, it checks that the NH3 adsorption energy changes in the expected direction upon hydrogenation. Each scored artifact carries a pre-assigned weight, with the adsorption energy ordering and spin localization receiving the most weight. The final reward is a weighted average of the scores. Merely copying numbers from any source (including the published article) will not pass, as the verifier tests the internal consistency of the computed values against the physical requirements. The only way to score well is to perform accurate DFT calculations that capture the correct chemical trends.
