# Phonon-based thermodynamic functions of Na3ClO supercell via DFT and molecular dynamics

## Problem background
Solid-state electrolytes with relaxor ferroelectric properties are promising candidates for energy harvesting and storage devices. Understanding their thermal stability, phase transitions, and the energetic landscape that underpins their electrochemical performance requires a detailed characterization of their thermodynamic functions—heat capacity, entropy, enthalpy, and free energy—as a function of temperature. First-principles simulations can predict these properties from the material's crystal structure. This task focuses on computationally determining the temperature-dependent thermodynamic functions of a Na₃ClO supercell, a representative composition for a class of Na⁺-ion conductors that exhibit complex, glass-like disorder.

## Approach
The computational workflow uses density functional theory (DFT) in three stages. First, the ideal crystal structure of Na₃ClO (space group Pm-3m) is relaxed by optimizing cell parameters and atomic positions. Next, an ab initio molecular dynamics (AIMD) simulation is run at 56 °C to generate a disordered, glass-like configuration, after which the structure is quenched to freeze in the disorder. Finally, the phonon frequencies and eigenvectors are computed for the disordered supercell (e.g., via the finite-displacement method using Phonopy). From the phonon density of states, standard statistical mechanics integration yields the molar heat capacity at constant volume (C_V), entropy (S), enthalpy (H), and Gibbs free energy (F) over the temperature range 0–600 K. All DFT steps may be performed with open-source codes such as Quantum ESPRESSO or CP2K, using appropriate pseudopotentials. The agent is free to choose numerical convergence parameters (energy cutoff, k‑mesh, time step, etc.) and must manage the computational cost of the 135‑atom supercell.

## Reproduction target
Execute the entire DFT/AIMD/phonon pipeline and produce a single scored output file: `thermodynamic_functions.csv`. The CSV must contain columns for Temperature (K), C_V (J/mol/K), S (J/mol/K), H (J/mol), and F (J/mol). Provide at least 100 equally spaced rows covering the interval from 0 K to 600 K. Values must be floating‑point numbers. The hidden verifier will compare the submitted table to a set of reference thermodynamic functions (obtained from an independent computational characterization of the same system) at multiple temperature points, using tolerance criteria that reflect the expected variability due to different DFT implementations and algorithmic choices.

## Assets

- Quantum ESPRESSO (open‑source DFT code): https://www.quantum-espresso.org/
- PAW‑GGA pseudopotentials (e.g., SSSP precision or PseudoDojo): https://www.materialscloud.org/discover/sssp/
- Phonopy: https://phonopy.github.io/phonopy/
- Na3ClO crystal structure (space group Pm‑3m, a ≈ 4.5 Å)

## Workflow steps

### Step 1: Prepare and relax the Na3ClO supercell
- Role: process
- Action: Construct the Na3ClO crystal (space group Pm‑3m, a ≈ 4.5 Å) and create a 3×3×3 supercell (Na81Cl27O27). Perform DFT geometry optimisation (cell parameters and atomic positions) using an open‑source DFT code with PAW‑GGA pseudopotentials. Save the optimised structure.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 2: Ab initio molecular dynamics at 56 °C
- Role: process
- Action: Run an NVT ab initio molecular dynamics simulation on the relaxed supercell at 329 K (56 °C) using the same DFT setup. Equilibrate the structure and then quench/relax to a low‑temperature configuration to freeze in the disorder, generating a glass‑like structure.
- Evidence: `/app/outputs/disordered_structure.cif`

### Step 3: Phonon calculations and thermodynamic functions
- Role: scored (load-bearing)
- Action: Using the disordered supercell from Step 2, compute the phonon frequencies and eigenvectors via finite‑displacement method (e.g., with Phonopy). Calculate the phonon density of states and integrate over q‑points to obtain the temperature‑dependent molar heat capacity at constant volume (C_V), entropy (S), enthalpy (H), and Gibbs free energy (F) from 0 K to 600 K. Write the results to thermodynamic_functions.csv.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: Temperature (K), C_V (J/mol/K), S (J/mol/K), H (J/mol), F (J/mol). At least 100 equally spaced rows covering 0–600 K. Values as floating‑point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Temperature‑dependent molar thermodynamic functions computed from phonon simulations, compared against reference values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `C_V (J/mol/K)`, `S (J/mol/K)`, `H (J/mol)`, `F (J/mol)`
  - `units`:
    - `Temperature (K)`: K
    - `C_V (J/mol/K)`: J/mol/K
    - `S (J/mol/K)`: J/mol/K
    - `H (J/mol)`: J/mol
    - `F (J/mol)`: J/mol

Notes: The agent must produce the CSV using the disordered supercell from the AIMD step. The checker will compare the computed C_V, S, H, F at multiple temperatures against hidden reference data with a tolerance that accounts for DFT code and pseudopotential differences. No gold values or tolerances are provided here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "C_V (J/mol/K)",
          "S (J/mol/K)",
          "H (J/mol)",
          "F (J/mol)"
        ],
        "units": {
          "Temperature (K)": "K",
          "C_V (J/mol/K)": "J/mol/K",
          "S (J/mol/K)": "J/mol/K",
          "H (J/mol)": "J/mol",
          "F (J/mol)": "J/mol"
        }
      },
      "description": "Temperature‑dependent molar thermodynamic functions computed from phonon simulations, compared against reference values with tolerance."
    }
  ],
  "notes": "The agent must produce the CSV using the disordered supercell from the AIMD step. The checker will compare the computed C_V, S, H, F at multiple temperatures against hidden reference data with a tolerance that accounts for DFT code and pseudopotential differences. No gold values or tolerances are provided here."
}
```

## How you are scored
A hidden verifier scores the submission in two stages. First, it validates that `thermodynamic_functions.csv` exists, is correctly formatted, and contains the required columns and at least 100 rows. Then it compares the agent's computed C_V, S, H, and F at a set of reference temperatures against hidden target values, applying per‑quantity tolerance windows. The final reward (a float between 0 and 1) is a weighted combination of the structural format check and the quantitative agreement scores. The intermediate process artifacts (the optimized and disordered supercell structures) are not scored individually, but they are essential to produce the final thermodynamic functions; a submission that does not genuinely reflect the full DFT+AIMD+phonon pipeline will not pass the verification.
