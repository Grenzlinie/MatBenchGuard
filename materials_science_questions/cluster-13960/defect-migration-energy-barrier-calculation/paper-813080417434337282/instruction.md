# First-principles voltage profile and Mg migration barriers in spinel MgxCr2O4

## Problem background
Magnesium batteries hold the promise of higher energy density than lithium-ion systems, but their practical realisation is hindered by the scarcity of cathodes that can reversibly intercalate divalent Mg ions with a high voltage and fast diffusion. The spinel oxide family has emerged as a candidate because the tetrahedral coordination environment of the Mg site may facilitate Mg mobility while the oxide lattice can deliver high intercalation voltages. This task investigates Mg intercalation into spinel Mg_x Cr_2 O_4 using first-principles methods. The goal is to determine, purely from computation, the room-temperature voltage–composition profile and the Mg migration barriers at several key compositions, thereby assessing the material’s viability as a cathode.

## Approach
In this computational study, the voltage profile is obtained by coupling density functional theory (DFT) with statistical mechanics. First, a training set of total energies is generated with DFT+U (generalized gradient approximation plus a Hubbard U correction on Cr, U = 3.5 eV) for a large number of Mg–vacancy configurations on the tetrahedral sites of the spinel host. These energies are used to fit a cluster expansion (CE) Hamiltonian, which is then employed in grand-canonical Monte Carlo (GCMC) simulations at 293 K. The GCMC output yields the Mg chemical potential in the cathode as a function of Mg concentration x. The intercalation voltage V(x) is obtained from the difference between this cathode chemical potential and the chemical potential of bulk Mg metal (the anode). Migrating Mg ions are studied with nudged elastic band (NEB) calculations, also at the DFT+U level, for six distinct scenarios: the dilute-Mg and dilute-vacancy limits, and the x=0.33 and x=0.50 ground-state orderings with either an added vacancy or an added Mg. The entire workflow is executed with the open‑source tools Quantum ESPRESSO (DFT and NEB), CASM (cluster expansion and Monte Carlo), and pymatgen (structure enumeration).

## Reproduction target
Reproduce the room-temperature (293 K) voltage–composition curve V(x) for Mg intercalation into the spinel Cr₂O₄ host, where x = Mg content per formula unit (0 ≤ x ≤ 1). The curve must be a two‑column file with at least 100 (x, V in volts) points. The quality of the curve will be assessed by recomputing the average voltage over the whole composition range and the voltage‑step magnitudes at x ≈ 0.33 and x ≈ 0.50, with comparison to hidden reference values. Separately, compute the Mg migration barriers (GGA+U, Hubbard U on Cr) for the following six cases using nudged elastic band: dilute Mg (single Mg in the empty host), dilute vacancy (single vacancy in the fully magnesiated host), the 33 % Mg ground state with an added vacancy (+Va), the 33 % Mg ground state with an added Mg (+Mg), the 50 % Mg ground state with an added vacancy (+Va), and the 50 % Mg ground state with an added Mg (+Mg). Report the barriers (meV) in a table with columns ‘case’ and ‘barrier_GGA+U’. The verifier will compare each barrier to hidden expected values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- CASM (Cluster Approach to Statistical Mechanics): https://github.com/prisms-center/CASMcode
- pymatgen: pymatgen
- Bulk Mg metal reference structure: https://materialsproject.org/materials/mp-153
- Spinel Cr2O4 host structure: https://materialsproject.org/
- PAW pseudopotential library: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: DFT total-energy training set for cluster expansion
- Role: process
- Action: Perform DFT total energy calculations for ~249 Mg-Va configurations in MgxCr2O4 up to 64‑oxygen supercells using Quantum ESPRESSO with PBE+U (U=3.5 eV on Cr). Compute formation energies referenced to empty Cr2O4 and fully magnesiated MgCr2O4.
- Evidence: `/app/outputs/dft_training_set_energies.json`

### Step 2: Cluster expansion model fitting
- Role: process
- Action: Fit a cluster expansion Hamiltonian to the DFT formation energies using split‑Bregman algorithm (as in CASM or custom implementation). Select effective cluster interactions, validate with RMSE and LOOCV. Identify ground state configurations, particularly at x=0.33 and x=0.50.
- Evidence: `/app/outputs/ce_hamiltonian.json`

### Step 3: Grand‑canonical Monte Carlo simulations
- Role: process
- Action: Run GCMC simulations using the CE Hamiltonian on a 12×12×12 supercell of the primitive rhombohedral spinel cell at 293 K. Equilibrate for 40 000 steps and sample for 100 000 steps. Perform thermodynamic free‑energy integration between 0%–100% Mg and 25%–50% Mg to correct for hysteresis. Obtain the Mg chemical potential μ_cathode(x) as a function of composition.
- Evidence: `/app/outputs/mu_vs_x.json`

### Step 4: Voltage–composition curve computation
- Role: scored (load-bearing)
- Action: From the GCMC μ_cathode(x) data, compute the intercalation voltage V(x) = −(μ_cathode(x) − μ_Mg_anode)/(2e), where μ_Mg_anode is the chemical potential of bulk Mg metal obtained via a separate DFT calculation. Produce a full voltage–composition curve V(x) for x_Mg in [0,1] at 293 K. Write the curve as a two‑column table with x_Mg and V (in volts).
- Output file: `/app/outputs/voltage_curve_293K.txt`
- Format: txt
- Contract: Two‑column space‑ or tab‑separated text: column 1 'x_Mg' (float 0–1), column 2 'V' (float, volts). At least 100 points covering the full range.
- Scoring: scored by hidden verifier

### Step 5: Mg migration barrier calculations
- Role: scored
- Action: Compute Mg migration barriers using DFT‑based nudged elastic band (NEB) with Quantum ESPRESSO, employing GGA+U (U=3.5 eV on Cr). For each case—dilute Mg (single Mg in empty Cr2O4), dilute vacancy (single vacancy in fully magnesiated MgCr2O4), 33% Mg ground state with an added vacancy (+Va), 33% Mg ground state with an added Mg (+Mg), 50% Mg ground state with an added vacancy (+Va), and 50% Mg ground state with an added Mg (+Mg)—run NEB with 7 images and force convergence 50 meV/Å. Extract the GGA+U migration barrier (maximum energy along the path minus initial state energy). Write a table with columns 'case' and 'barrier_GGA+U'.
- Output file: `/app/outputs/migration_barriers.txt`
- Format: tsv
- Contract: Tab‑ or space‑separated text with two columns: 'case' (string; one of dilute_Mg, dilute_Va, 33%_+Va, 33%_+Mg, 50%_+Va, 50%_+Mg) and 'barrier_GGA+U' (float, meV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/voltage_curve_293K.txt`
- `/app/outputs/migration_barriers.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### voltage_curve_293K.txt
- path: `/app/outputs/voltage_curve_293K.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Room‑temperature voltage–composition curve V(x) for MgxCr2O4. The checker recomputes the average voltage and voltage‑step magnitudes at x≈0.33 and x≈0.50 from this curve.
- schema:
  - `type`: table
  - `required_columns`: `x_Mg`, `V`
  - `units`:
    - `x_Mg`: dimensionless
    - `V`: V

### migration_barriers.txt
- path: `/app/outputs/migration_barriers.txt`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Table of Mg migration barriers for six specified configurations. The checker compares each barrier to a hidden reference value.
- schema:
  - `type`: table
  - `required_columns`: `case`, `barrier_GGA+U`
  - `units`:
    - `barrier_GGA+U`: meV

Notes: The voltage curve artifact enables recomputation of average voltage and voltage steps; the migration barriers are compared directly to paper‑reported values. Both artifacts must be produced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "voltage_curve_293K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Mg",
          "V"
        ],
        "units": {
          "x_Mg": "dimensionless",
          "V": "V"
        }
      },
      "description": "Room‑temperature voltage–composition curve V(x) for MgxCr2O4. The checker recomputes the average voltage and voltage‑step magnitudes at x≈0.33 and x≈0.50 from this curve."
    },
    {
      "file": "migration_barriers.txt",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "barrier_GGA+U"
        ],
        "units": {
          "barrier_GGA+U": "meV"
        }
      },
      "description": "Table of Mg migration barriers for six specified configurations. The checker compares each barrier to a hidden reference value."
    }
  ],
  "notes": "The voltage curve artifact enables recomputation of average voltage and voltage steps; the migration barriers are compared directly to paper‑reported values. Both artifacts must be produced."
}
```

## How you are scored
Your submission consists of two scored artifacts: voltage_curve_293K.txt and migration_barriers.txt. A hidden verifier independently recomputes the required metrics from your voltage curve (average voltage over the full range and voltage‑step sizes at the two specified compositions) and reads each migration barrier from your table. Each artifact is scored according to how close its derived or read quantities are to the hidden expected results. The final reward, a number between 0 and 1, is a weighted combination of the two scores: the voltage‑curve metrics carry a higher weight because the curve depends on the entire preceding pipeline and is the primary result, while the migration barriers contribute a substantial but lower weight. Simply reporting the paper's numbers without producing the correct file content will not pass; the verifier checks the artifact files directly.
