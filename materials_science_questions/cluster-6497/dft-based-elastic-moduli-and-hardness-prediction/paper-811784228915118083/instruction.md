# DFT elastic moduli and hardness prediction of 5d transition metal monocarbides in WC structure

## Problem background
Transition metal monocarbides in the tungsten carbide (WC) structure are candidate materials for extreme hardness, combining metallic, covalent, and ionic bonding. Understanding how the choice of 5d metal influences lattice parameters, elastic constants, polycrystalline moduli, and intrinsic hardness is essential for identifying the most promising compounds. This task reproduces the first-principles prediction of these properties across the whole 5d series (La to Au) using density-functional theory (DFT) to produce a systematic, self-consistent dataset of mechanical and hardness characteristics.

## Approach
The reproduction follows a first-principles computational workflow. For each compound, a starting hexagonal crystal structure (space group P-6m2) is constructed with the transition metal at (0,0,0) and carbon at (1/3,2/3,1/2). Full geometry optimizations are performed with two exchange-correlation functionals (GGA-PBE and LDA) using a plane-wave pseudopotential code. From the relaxed cells, the five independent elastic constants of the hexagonal system are obtained via stress-strain calculations. Electronic structure analysis yields the density of states, Mulliken bond populations, the pseudogap, and the number of free carriers. The geometry and elastic constants are then averaged over the two functionals. Voigt-Reuss-Hill averaging formulas are applied to compute the isotropic bulk modulus, shear modulus, Young's modulus, and Poisson's ratio. For the hardness prediction, Chen's semi-empirical model is employed: Hv = 740 * (P - P') * vb^(-5/3), where P is the Mulliken bond population, P' = n_free/V is the metallic population, vb = V/6 is the bond volume, and n_free is the free-electron count integrated from the pseudogap to the Fermi level. Compounds that are mechanically unstable (negative C44) are flagged and their shear-related moduli are left undefined.

## Reproduction target
Produce two CSV tables for the nine 5d transition metal monocarbides LaC, HfC, TaC, WC, ReC, OsC, IrC, PtC, and AuC, all in the hexagonal WC (P-6m2) structure. For each compound, compute the GGA and LDA relaxed lattice parameters a0 and c0, the elastic constants C11, C12, C13, C33, and C44, and then average the GGA and LDA results. Apply Voigt-Reuss-Hill averaging to obtain the bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio nu. For any compound whose averaged C44 is negative, leave G, E, and nu empty. Report these results in mechanical_properties.csv. Separately, compute the bond distance, unit-cell volume, bond volume, Mulliken bond population, pseudogap energy, density of states at the Fermi level, free-electron count, metallic population, metallicity, and Vickers hardness Hv for each compound using the same averaged quantities and the semi-empirical hardness formula. Provide the GGA, LDA, and averaged rows (at least the averaged row) in hardness_properties.csv. The task is to deliver the correct physical values and the correct stability assignments.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard pseudopotentials (SSSP library or similar): https://www.quantum-espresso.org/pseudopotentials
- Python with NumPy, SciPy, pandas: pip install numpy scipy pandas

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Define the hexagonal WC prototype (space group P-6m2) with fractional coordinates TM(0,0,0) and C(1/3,2/3,1/2). Generate input files for all 5d TM monocarbides: LaC, HfC, TaC, WC, ReC, OsC, IrC, PtC, AuC.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: For each compound, run full geometry optimization using a plane-wave pseudopotential code (e.g., Quantum ESPRESSO) at GGA-PBE and LDA levels. Use Vanderbilt ultrasoft pseudopotentials and standard tight convergence criteria for energy, forces, and stresses.
- Evidence: none

### Step 3: Elastic constants calculation
- Role: process
- Action: For each compound and each functional (GGA/LDA), apply finite strains to the relaxed cell, compute the stress tensors, and extract the five independent hexagonal elastic constants C11, C12, C13, C33, C44 using standard stress-strain methods.
- Evidence: none

### Step 4: Electronic structure and population analysis
- Role: process
- Action: Perform single-point DFT calculations on the relaxed structures (GGA and LDA) to obtain total and partial density of states (DOS), Mulliken bond population P, the pseudogap energy Ep, and the number of free electrons n_free by integrating DOS from Ep to the Fermi energy EF.
- Evidence: none

### Step 5: Mechanical properties compilation
- Role: scored (load-bearing)
- Action: For each compound, compute the arithmetic average of the GGA and LDA lattice parameters (a0, c0) and elastic constants C11, C12, C13, C33, C44. Apply the Voigt–Reuss–Hill formulas (bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio nu) to the averaged elastic constants. For compounds with a negative C44 (mechanically unstable), set G, E, nu to empty values. Write the results to 'mechanical_properties.csv'.
- Output file: `/app/outputs/mechanical_properties.csv`
- Format: csv
- Contract: Columns: compound, a0_avg, c0_avg, C11_avg, C33_avg, C44_avg, C12_avg, C13_avg, B, G, E, nu. Include one row per compound (9 total). Use empty strings for G, E, nu when C44_avg < 0.
- Scoring: scored by hidden verifier

### Step 6: Hardness prediction
- Role: scored (load-bearing)
- Action: For each compound, compute bond distance d from the averaged lattice parameters, cell volume V, bond volume vb = V/6, Mulliken population P (average of GGA/LDA), metallic population P' = n_free / V, metallicity fm = P'/P, and Vickers hardness Hv = 740 * (P - P') * vb^(-5/3). Compute these quantities separately for the GGA and LDA results, then report their arithmetic average. Write all intermediate quantities and the final Hv to 'hardness_properties.csv'.
- Output file: `/app/outputs/hardness_properties.csv`
- Format: csv
- Contract: Columns: compound, d_avg, V_avg, P, vb, Ep, N_Ef, n_free, P_prime, fm, Hv_calc. Include one row per compound for the averaged result (the GGA and LDA rows are optional).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_properties.csv`
- `/app/outputs/hardness_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_properties.csv
- path: `/app/outputs/mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Averaged lattice parameters, elastic constants, and derived Voigt–Reuss–Hill polycrystalline moduli for 5d transition metal monocarbides. Mechanically unstable compounds (C44_avg < 0) must have empty G, E, nu.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a0_avg`, `c0_avg`, `C11_avg`, `C33_avg`, `C44_avg`, `C12_avg`, `C13_avg`, `B`, `G`, `E`, `nu`
  - `units`:
    - `a0_avg`: Å
    - `c0_avg`: Å
    - `C11_avg`: GPa
    - `C33_avg`: GPa
    - `C44_avg`: GPa
    - `C12_avg`: GPa
    - `C13_avg`: GPa
    - `B`: GPa
    - `G`: GPa
    - `E`: GPa
    - `nu`: dimensionless

### hardness_properties.csv
- path: `/app/outputs/hardness_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Semi-empirical Vickers hardness and intermediate electronic quantities averaged over GGA and LDA for each compound.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `d_avg`, `V_avg`, `P`, `vb`, `Ep`, `N_Ef`, `n_free`, `P_prime`, `fm`, `Hv_calc`
  - `units`:
    - `d_avg`: Å
    - `V_avg`: Å³
    - `P`: electrons
    - `vb`: Å³
    - `Ep`: eV
    - `N_Ef`: states/eV/cell
    - `n_free`: electrons/cell
    - `P_prime`: electrons/Å³
    - `fm`: dimensionless
    - `Hv_calc`: GPa

Notes: The task requires a full DFT pipeline for nine compounds, each at two functionals, including geometry optimizations, elastic constant calculations, and DOS analysis. The verifier uses a lightweight CSV comparison (result-level, T0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a0_avg",
          "c0_avg",
          "C11_avg",
          "C33_avg",
          "C44_avg",
          "C12_avg",
          "C13_avg",
          "B",
          "G",
          "E",
          "nu"
        ],
        "units": {
          "a0_avg": "Å",
          "c0_avg": "Å",
          "C11_avg": "GPa",
          "C33_avg": "GPa",
          "C44_avg": "GPa",
          "C12_avg": "GPa",
          "C13_avg": "GPa",
          "B": "GPa",
          "G": "GPa",
          "E": "GPa",
          "nu": "dimensionless"
        }
      },
      "description": "Averaged lattice parameters, elastic constants, and derived Voigt–Reuss–Hill polycrystalline moduli for 5d transition metal monocarbides. Mechanically unstable compounds (C44_avg < 0) must have empty G, E, nu."
    },
    {
      "file": "hardness_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "d_avg",
          "V_avg",
          "P",
          "vb",
          "Ep",
          "N_Ef",
          "n_free",
          "P_prime",
          "fm",
          "Hv_calc"
        ],
        "units": {
          "d_avg": "Å",
          "V_avg": "Å³",
          "P": "electrons",
          "vb": "Å³",
          "Ep": "eV",
          "N_Ef": "states/eV/cell",
          "n_free": "electrons/cell",
          "P_prime": "electrons/Å³",
          "fm": "dimensionless",
          "Hv_calc": "GPa"
        }
      },
      "description": "Semi-empirical Vickers hardness and intermediate electronic quantities averaged over GGA and LDA for each compound."
    }
  ],
  "notes": "The task requires a full DFT pipeline for nine compounds, each at two functionals, including geometry optimizations, elastic constant calculations, and DOS analysis. The verifier uses a lightweight CSV comparison (result-level, T0)."
}
```

## How you are scored
A hidden verifier reads your mechanical_properties.csv and hardness_properties.csv and compares the reported values for each compound against hidden reference targets with tolerances that reflect typical spread between different plane-wave implementations. It checks that lattice parameters, elastic constants, bulk, shear, Young's moduli, Poisson's ratio, and Vickers hardness agree within those tolerances, and that mechanically unstable compounds (C44<0) correctly have empty G, E, nu. Intermediate quantities such as bond population, free-electron count, and metallicity are also checked for consistency. The final reward is a weighted sum of the successes across both files; you must produce the correct averaged numbers and correctly identify stable and unstable compounds.
