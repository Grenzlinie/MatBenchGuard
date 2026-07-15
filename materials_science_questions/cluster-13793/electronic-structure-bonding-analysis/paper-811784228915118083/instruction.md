# DFT-based elastic properties and hardness predictions of WC-type 5d transition metal monocarbides

## Problem background
5d transition metal monocarbides that adopt the tungsten carbide (WC) hexagonal structure are candidate hard materials. Understanding how their elastic properties and hardness vary across the series can illuminate relationships between electronic structure and mechanical behavior. Density functional theory (DFT) can compute lattice constants, elastic constants, and derived polycrystalline moduli; combining these with a semiempirical hardness model yields Vickers hardness predictions. This task explores those predictions for the mechanically stable compounds in the series.

## Approach
The work uses plane-wave DFT with two exchange-correlation functionals, the generalized gradient approximation (GGA-PBE) and the local density approximation (LDA), to relax the crystal structures and obtain elastic constants via the stress–strain method. From the relaxed structures, electronic-structure analyses yield Mulliken bond populations and density-of-states (DOS) profiles. A semiempirical hardness model then combines these quantities: Vickers hardness is expressed in terms of the Mulliken population, a metallic population derived from the number of effective free electrons (obtained by integrating the total DOS from the pseudogap to the Fermi level), and the bond volume. Because GGA and LDA typically give opposite systematic errors, the arithmetic average of the two functionals is also reported. The workflow is applied to six 5d transition metal monocarbides (TaC, WC, ReC, OsC, IrC, PtC) in the WC-type hexagonal structure (space group P-6m2). An open-source plane-wave DFT code (e.g., Quantum ESPRESSO) is used as an equivalent to the original proprietary code.

## Reproduction target
Compute the equilibrium lattice parameters a0, c0, the five independent elastic constants C11, C12, C13, C33, C44, the derived Voigt–Reuss–Hill polycrystalline moduli (bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio ν), and the Vickers hardness Hv for the six monocarbides TaC, WC, ReC, OsC, IrC, and PtC. Perform all calculations with both the GGA-PBE and LDA functionals, and report the arithmetic average of the two as a third set. Tabulate the lattice parameters, elastic constants, and moduli in one CSV file, and the electronic-structure descriptors together with the predicted hardness in a second CSV file, following the provided schemas.

## Assets

- Quantum ESPRESSO (plane-wave DFT code): https://www.quantum-espresso.org/
- Pseudopotential library (PBE and LDA): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Crystal structure setup
- Role: process
- Action: Create the initial crystal structures for the six mechanically stable 5d transition metal monocarbides (TaC, WC, ReC, OsC, IrC, PtC) in the WC-type hexagonal structure (space group P-6m2, No. 187) with the transition metal atom at Wyckoff position 1a (0,0,0) and carbon at 1d (1/3,2/3,1/2).
- Evidence: `/app/outputs/structure_setup_done.txt`

### Step 2: DFT geometry optimization and elastic constants
- Role: process
- Action: For each compound, perform DFT calculations with both GGA-PBE and LDA functionals to relax the unit cell (optimize lattice parameters a, c and atomic positions) until forces and stresses are below convergence thresholds. From the relaxed structures, compute the five independent elastic constants (C11, C12, C13, C33, C44) using the stress–strain method. Record the relaxed lattice parameters a0, c0 and the elastic constants for each functional.
- Evidence: `/app/outputs/dft_calculation_log.txt`

### Step 3: Electronic structure analysis
- Role: process
- Action: For each relaxed structure from step 2, perform single-point DFT calculations (GGA and LDA) to obtain the total and orbital-projected density of states (DOS), Mulliken bond populations, and identify the pseudogap energy from the C-2p PDOS. Integrate the total DOS from the pseudogap to the Fermi level to obtain the effective free-electron count n_free. Record the bond distance d, cell volume V, Mulliken population P, pseudogap energy Ep, Fermi-level DOS N(EF), and n_free for each functional.
- Evidence: `/app/outputs/electronic_analysis_log.txt`

### Step 4: Compile lattice parameters, elastic constants, and derived moduli
- Role: scored (load-bearing)
- Action: Collect the GGA and LDA lattice parameters and elastic constants from step 2. Compute the arithmetic average for each quantity. From the averaged elastic constants, calculate the Voigt–Reuss–Hill bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio ν using standard formulas for hexagonal crystals. Output the results to lattice_and_elastic_constants.csv, containing one row per compound per functional (GGA, LDA, Ave) with all quantities.
- Output file: `/app/outputs/lattice_and_elastic_constants.csv`
- Format: csv
- Contract: Columns: compound (string), xc (string, one of GGA/LDA/Ave), a0 (float, Å), c0 (float, Å), C11 (float, GPa), C12 (float, GPa), C13 (float, GPa), C33 (float, GPa), C44 (float, GPa), B (float, GPa), G (float, GPa), E (float, GPa), nu (float, dimensionless). One row per xc level per compound.
- Scoring: scored by hidden verifier

### Step 5: Hardness calculation
- Role: scored (load-bearing)
- Action: From the relaxed structures (bond distances d, cell volume V), the Mulliken populations P, and the electronic structure quantities (Ep, n_free) obtained in steps 2 and 3, compute the Vickers hardness Hv using the Gao semiempirical model: Hv = 740 * (P - P') * (v_b)^(-5/3), where P' = n_free/V, v_b = V/6, and metallicity f_m = P'/P. Compute these for GGA, LDA, and the arithmetic average. Output all intermediate quantities and final hardness to hardness_data.csv.
- Output file: `/app/outputs/hardness_data.csv`
- Format: csv
- Contract: Columns: compound (string), xc (string, one of GGA/LDA/Ave), d (float, Å), V (float, Å³), P (float, dimensionless Mulliken population), v_b (float, Å³), Ep (float, eV), N(E_f) (float, states/eV), n_free (float, dimensionless), P' (float, dimensionless), f_m (float, dimensionless), H_v (float, GPa). One row per xc level per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_and_elastic_constants.csv`
- `/app/outputs/hardness_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_and_elastic_constants.csv
- path: `/app/outputs/lattice_and_elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice parameters, elastic constants, and Voigt‑Reuss‑Hill polycrystalline moduli for the six mechanically stable compounds. The checker compares these values against hidden reference data from the paper with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `xc`, `a0`, `c0`, `C11`, `C12`, `C13`, `C33`, `C44`, `B`, `G`, `E`, `nu`
  - `units`:
    - `a0`: Å
    - `c0`: Å
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `B`: GPa
    - `G`: GPa
    - `E`: GPa
    - `nu`: dimensionless

### hardness_data.csv
- path: `/app/outputs/hardness_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Intermediate quantities from electronic structure analysis and the predicted Vickers hardness. The checker compares these values against hidden reference data from the paper with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `xc`, `d`, `V`, `P`, `v_b`, `Ep`, `N(E_f)`, `n_free`, `P'`, `f_m`, `H_v`
  - `units`:
    - `d`: Å
    - `V`: Å³
    - `P`: dimensionless
    - `v_b`: Å³
    - `Ep`: eV
    - `N(E_f)`: states/eV
    - `n_free`: dimensionless
    - `P'`: dimensionless
    - `f_m`: dimensionless
    - `H_v`: GPa

Notes: All required calculations are publicly reproducible using open-source plane-wave DFT code and standard pseudopotentials. The solver is expected to use convergence parameters (cutoff, k-point mesh) that give accuracy comparable to the paper's settings, but specific numerical tolerances are hidden. Only the six mechanically stable compounds (TaC, WC, ReC, OsC, IrC, PtC) are required; LaC, HfC, and AuC are excluded because the paper reports them as mechanically unstable.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_and_elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "xc",
          "a0",
          "c0",
          "C11",
          "C12",
          "C13",
          "C33",
          "C44",
          "B",
          "G",
          "E",
          "nu"
        ],
        "units": {
          "a0": "Å",
          "c0": "Å",
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "B": "GPa",
          "G": "GPa",
          "E": "GPa",
          "nu": "dimensionless"
        }
      },
      "description": "Lattice parameters, elastic constants, and Voigt‑Reuss‑Hill polycrystalline moduli for the six mechanically stable compounds. The checker compares these values against hidden reference data from the paper with appropriate tolerances."
    },
    {
      "file": "hardness_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "xc",
          "d",
          "V",
          "P",
          "v_b",
          "Ep",
          "N(E_f)",
          "n_free",
          "P'",
          "f_m",
          "H_v"
        ],
        "units": {
          "d": "Å",
          "V": "Å³",
          "P": "dimensionless",
          "v_b": "Å³",
          "Ep": "eV",
          "N(E_f)": "states/eV",
          "n_free": "dimensionless",
          "P'": "dimensionless",
          "f_m": "dimensionless",
          "H_v": "GPa"
        }
      },
      "description": "Intermediate quantities from electronic structure analysis and the predicted Vickers hardness. The checker compares these values against hidden reference data from the paper with appropriate tolerances."
    }
  ],
  "notes": "All required calculations are publicly reproducible using open-source plane-wave DFT code and standard pseudopotentials. The solver is expected to use convergence parameters (cutoff, k-point mesh) that give accuracy comparable to the paper's settings, but specific numerical tolerances are hidden. Only the six mechanically stable compounds (TaC, WC, ReC, OsC, IrC, PtC) are required; LaC, HfC, and AuC are excluded because the paper reports them as mechanically unstable."
}
```

## How you are scored
A hidden verifier compares the values in the two scored CSV files (lattice_and_elastic_constants.csv and hardness_data.csv) against hidden reference values derived from published data. The verifier checks both the absolute numbers (with appropriate tolerances for each quantity) and the relative trends across compounds. The total reward is a weighted combination of the scores from these two stages. Reporting the paper's numbers without executing the described DFT workflow will not earn full credit; the checker expects values obtained through the required computational pipeline.
