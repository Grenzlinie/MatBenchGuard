# APB Energy Calculation in Ni3Al Alloy using Cluster Expansion and Monte Carlo

## Problem background
Antiphase boundaries (APBs) are planar defects in ordered intermetallic alloys that form during dislocation slip. The APB energy quantifies the resistance to shearing along a given slip plane and is a key factor in alloy strengthening. Impurity atoms can alter the APB energy, but predicting this effect from first principles is challenging because the impurities are not confined to a specific layer and many configurations across thousands of atoms must be sampled. Cluster expansion (CE) combined with Monte Carlo (MC) provides a tractable approach: a surrogate energy model is trained on density-functional theory (DFT) data, and then MC simulations are used to sample configurations at finite temperature to compute the unequilibrated APB energy. This task reproduces the computational pipeline for the L1₂ ordered Ni₃Al system with Ti additions, using open-source tools, to compute APB energies and the influence of Ti impurities.

## Approach
The method proceeds in four stages. First, DFT total-energy calculations (using the PBE functional) are performed on a set of enumerated Ni-Al and Ni-Al-Ti structures to generate a training set. Second, a cluster expansion is fitted to these energies, producing effective cluster interactions (ECIs) that can rapidly evaluate the energy of any atomic configuration on the L1₂ lattice. Third, canonical Metropolis Monte Carlo simulations (with at least 1000 atoms) are run for pure Ni₃Al and for Ni₃Al with 1% Ti substitution, using the cluster expansion for energy evaluation, at selected temperatures. The supercell is oriented such that the first two translation vectors lie in the (111) slip plane and the slip vector is [0 0.5 0.5], ensuring correct APB geometry under periodic boundaries. Finally, for each MC snapshot the unequilibrated APB energy is obtained by duplicating the configuration along the third translation vector, shifting one half by the slip vector, and computing the energy difference per unit area. The pure APB energy is also computed directly from the cluster expansion without MC. All steps use open-source software: Quantum ESPRESSO for DFT, and the Alloy Theoretic Automated Toolkit (ATAT) for structure enumeration, cluster expansion fitting, Monte Carlo, and APB handling.

## Reproduction target
Produce two scored artifacts. First, compute the unequilibrated APB energy of pure Ni₃Al using the cluster expansion alone (no Monte Carlo) and write that single number (in mJ/m²) to pure_apb_energy.txt. Second, from the MC simulations at 400 K and 1600 K, compute the mean APB energy for pure Ni₃Al and for Ni₃Al with 1% Ti at each temperature, and calculate the impurity-induced change Δ = γ(Ti) – γ(pure). Write a CSV file dopant_apb_energies.csv with columns: concentration (at%), temperature (K), APB_energy (mJ/m²), delta_APB_energy (mJ/m²). Include at least two rows: one for 1% Ti at 400 K and one for 1% Ti at 1600 K. The CSV must be well-formed, with accurate column headers and consistent units.

## Assets

- Alloy Theoretic Automated Toolkit (ATAT): https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP PBE): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Generate oriented supercell
- Role: process
- Action: Using ATAT tools (cellcvrt), generate a supercell of L12 Ni3Al with at least 1000 atoms, oriented such that the (111) plane is defined by the first two translation vectors and the slip vector is [0 0.5 0.5]. Write the lattice and structure files.
- Evidence: `/app/outputs/lat.in, str.out`

### Step 2: DFT total-energy calculations for cluster expansion training
- Role: process
- Action: Enumerate Ni-Al binary and Ni-Al-Ti ternary structures using ATAT's mmaps. Perform DFT calculations with Quantum ESPRESSO (PBE functional) to obtain total energies for each structure. Save the energies in a format readable by ATAT's fit.
- Evidence: `/app/outputs/energies.dat`

### Step 3: Cluster expansion fitting
- Role: process
- Action: Fit a cluster expansion using ATAT's mmaps (or corrdump and fit) to obtain effective cluster interactions (eci.out). Report the cross-validation score.
- Evidence: `/app/outputs/eci.out`

### Step 4: Compute pure Ni3Al APB energy from cluster expansion
- Role: scored
- Action: Using the cluster expansion from step 03, create a defect-free and a defective APB structure with the (111)[0 0.5 0.5] slip. Compute the APB energy via evaluating the energy difference. Write the pure APB energy in mJ/m² to pure_apb_energy.txt.
- Output file: `/app/outputs/pure_apb_energy.txt`
- Format: txt
- Contract: A single floating-point number in mJ/m².
- Scoring: scored by hidden verifier

### Step 5: Monte Carlo simulations for pure and doped systems
- Role: process
- Action: For pure Ni3Al and for Ni3Al with 1% Ti substitution, run canonical Monte Carlo (memc2) at 400 K and 1600 K using the ECIs from step 03, with sufficient equilibration and averaging passes. Use the apb code to compute APB energy for each snapshot, recording per-snapshot energies for later averaging.
- Evidence: `/app/outputs/gamma_apb_pure_400.out, gamma_apb_ti_400.out, gamma_apb_pure_1600.out, gamma_apb_ti_1600.out`

### Step 6: Extract mean APB energy and enhancement for doped case
- Role: scored (load-bearing)
- Action: From the MC outputs, compute the mean APB energy for the 1% Ti case at each temperature and the corresponding pure Ni3Al mean APB energy (using pure MC results at the same temperature). Calculate the change Δ = γ(Ti) - γ(pure). Write a CSV with columns: concentration (at%), temperature (K), APB_energy (mJ/m²), delta_APB_energy (mJ/m²). Include rows for 1% Ti at 400 K and 1600 K.
- Output file: `/app/outputs/dopant_apb_energies.csv`
- Format: csv
- Contract: CSV with columns: concentration, temperature, APB_energy, delta_APB_energy. At least two data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_apb_energy.txt`
- `/app/outputs/dopant_apb_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_apb_energy.txt
- path: `/app/outputs/pure_apb_energy.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: APB energy of pure Ni3Al evaluated from the cluster expansion without Monte Carlo.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the APB energy in mJ/m².

### dopant_apb_energies.csv
- path: `/app/outputs/dopant_apb_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Mean APB energy and the enhancement due to 1% Ti at 400 K and 1600 K, derived from Monte Carlo sampling.
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `temperature`, `APB_energy`, `delta_APB_energy`
  - `units`:
    - `concentration`: at%
    - `temperature`: K
    - `APB_energy`: mJ/m^2
    - `delta_APB_energy`: mJ/m^2

Notes: Scoring is structural: the pure APB energy must be within a reasonable range for Ni3Al, and the dopant file must show a positive APB energy enhancement that decreases with temperature. Exact numeric agreement with the paper is not required because the DFT code (Quantum ESPRESSO) differs from the original VASP.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_apb_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the APB energy in mJ/m²."
      },
      "description": "APB energy of pure Ni3Al evaluated from the cluster expansion without Monte Carlo."
    },
    {
      "file": "dopant_apb_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "temperature",
          "APB_energy",
          "delta_APB_energy"
        ],
        "units": {
          "concentration": "at%",
          "temperature": "K",
          "APB_energy": "mJ/m^2",
          "delta_APB_energy": "mJ/m^2"
        }
      },
      "description": "Mean APB energy and the enhancement due to 1% Ti at 400 K and 1600 K, derived from Monte Carlo sampling."
    }
  ],
  "notes": "Scoring is structural: the pure APB energy must be within a reasonable range for Ni3Al, and the dopant file must show a positive APB energy enhancement that decreases with temperature. Exact numeric agreement with the paper is not required because the DFT code (Quantum ESPRESSO) differs from the original VASP."
}
```

## How you are scored
A hidden verifier independently scores each output and combines them into a final reward. For pure_apb_energy.txt, the verifier checks that the reported APB energy is a valid floating-point number within a physically plausible range for Ni₃Al. For dopant_apb_energies.csv, the verifier validates the CSV structure, the required columns, and then examines the numerical consistency. This includes checking that the energy differences are physically reasonable and that the data exhibit the expected relationship between temperature and the effect of titanium. Do not attempt to match the paper’s exact numbers; the scoring rewards correct physical trends and plausible magnitudes derived from your own computation, not exact numeric agreement. Reporting a number without executing the full workflow is not sufficient to pass.
