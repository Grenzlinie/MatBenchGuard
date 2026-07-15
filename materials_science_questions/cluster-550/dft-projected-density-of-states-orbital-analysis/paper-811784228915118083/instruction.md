# DFT Elastic and Hardness Properties of 5d Transition Metal Monocarbides

## Problem background
5d transition metal monocarbides crystallizing in the hexagonal tungsten carbide structure (space group P-6m2) are candidate hard materials. Understanding their mechanical and electronic properties requires systematic first-principles prediction of equilibrium lattice parameters, elastic constants, polycrystalline moduli, and Vickers hardness. The hardness is influenced by the degree of covalent bonding and metallicity, which can be quantified via the density of states and Mulliken population analysis. A key open question is how hardness varies across the 5d series and which monocarbide exhibits the highest hardness, and what electronic-structure features govern it.

## Approach
The properties are computed from first principles using density functional theory (DFT) with both the PBE generalized-gradient approximation (GGA) and the local-density approximation (LDA, Perdew-Zunger parameterization). For each of the nine compounds (LaC, HfC, TaC, WC, ReC, OsC, IrC, PtC, AuC) in the WC structure (TM at (0,0,0), C at (1/3,2/3,1/2)), the workflow proceeds in two stages: (1) variable-cell geometry optimization for each functional, yielding relaxed lattice parameters a0, c0; (2) elastic constant calculation via strain-stress analysis to obtain the five independent constants C11, C12, C13, C33, C44. The Voigt-Reuss-Hill averaging scheme for hexagonal crystals is then applied to derive bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio nu. Mechanical stability is assessed; compounds with a negative C44 are unstable and their derived moduli are not computed. Electronic structure analysis (total and projected density of states, Mulliken population) is performed at both functional levels to extract: the pseudogap energy Ep (identified from the C-2p PDOS where it becomes negligible), the effective number of free electrons n_free by integrating the total DOS from Ep to the Fermi energy, the bond volume vb = V/6, and the Mulliken bond population P. A semi-empirical model combines these quantities to calculate Vickers hardness Hv, and the metallicity fm = (n_free/V)/P is reported. The arithmetic mean of GGA and LDA results is taken as the final predicted value for each quantity.

## Reproduction target
Compute the averaged (GGA + LDA) lattice parameters a0, c0, the five elastic constants C11, C12, C13, C33, C44, the Voigt-Reuss-Hill bulk, shear, Young's moduli, Poisson's ratio, metallicity, and Vickers hardness for all nine 5d TM monocarbides. Output the results as a CSV file with one row per compound. For any compound that is mechanically unstable (as indicated by the elastic stability criteria, e.g. negative C44), leave the derived moduli (B, G, E, nu) and the metallicity and hardness (fm, Hv) cells empty, while still reporting its lattice parameters and elastic constants.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP pseudopotentials (PBE and LDA): https://www.materialscloud.org/discover/sssp/table
- Atomic Simulation Environment (ASE): ase
- Python with numpy: numpy

## Workflow steps

### Step 1: Structure preparation
- Role: process
- Action: Create initial unit cells for each of the nine 5d TM monocarbides (LaC, HfC, TaC, WC, ReC, OsC, IrC, PtC, AuC) in the hexagonal WC structure (space group P-6m2), with TM at (0,0,0) and C at (1/3,2/3,1/2). Save structures in a format readable by Quantum ESPRESSO.
- Evidence: none

### Step 2: DFT geometry optimization (GGA-PBE)
- Role: process
- Action: For each compound, perform variable-cell geometry relaxation using Quantum ESPRESSO with the PBE exchange-correlation functional, ultrasoft pseudopotentials, a dense Monkhorst-Pack k-point grid, and a high plane-wave cutoff. Relax both lattice parameters and atomic positions until tight convergence criteria are met.
- Evidence: none

### Step 3: DFT geometry optimization (LDA)
- Role: process
- Action: Repeat the geometry optimization for each compound using the LDA (Perdew-Zunger parameterization) exchange-correlation functional, keeping all other computational parameters the same.
- Evidence: none

### Step 4: DFT elastic constant calculation (GGA-PBE)
- Role: process
- Action: Using the PBE-relaxed structures, compute the five independent elastic constants C11, C12, C13, C33, C44 for each compound via strain-stress analysis. Mark compounds with negative C44 as mechanically unstable.
- Evidence: none

### Step 5: DFT elastic constant calculation (LDA)
- Role: process
- Action: Repeat the elastic constant calculation using the LDA-relaxed structures.
- Evidence: none

### Step 6: DFT electronic structure and DOS (GGA-PBE)
- Role: process
- Action: For each compound, perform a self-consistent SCF calculation, then a non-self-consistent calculation on a denser k-mesh to compute total and projected density of states (DOS) and Mulliken population analysis. Determine the pseudogap energy Ep from the C-2p PDOS.
- Evidence: none

### Step 7: DFT electronic structure and DOS (LDA)
- Role: process
- Action: Repeat the electronic structure calculation and DOS analysis using the LDA functional.
- Evidence: none

### Step 8: Post-processing and averaged properties table
- Role: scored (load-bearing)
- Action: For each compound, average the GGA and LDA results for lattice parameters a0, c0 and elastic constants C11, C12, C13, C33, C44. Apply the Voigt-Reuss-Hill averaging formulas for hexagonal crystals to compute bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio nu. From electronic structure data, estimate pseudogap energy, integrate total DOS to obtain effective free electron number n_free, compute metallicity fm, and calculate Vickers hardness Hv using the semiempirical formula involving Mulliken bond population P, bond volume vb, and metallicity. For compounds with negative C44, leave derived columns B through Hv empty. Write all results to results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: compound, a0, c0, C11, C12, C13, C33, C44, B, G, E, nu, fm, Hv. Each row one compound. For mechanically unstable compounds, columns B through Hv are empty.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Averaged structural, elastic, and hardness properties for each 5d TM monocarbide. Mechanically unstable compounds have empty derived columns. The verifier compares against hidden paper reference values using tolerances appropriate for a different DFT code.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a0`, `c0`, `C11`, `C12`, `C13`, `C33`, `C44`, `B`, `G`, `E`, `nu`, `fm`, `Hv`

Notes: The CSV must contain one row per compound (9 compounds). Compounds with negative C44 must have empty cells in columns B, G, E, nu, fm, Hv, while still reporting their elastic constants and lattice parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
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
          "nu",
          "fm",
          "Hv"
        ]
      },
      "description": "Averaged structural, elastic, and hardness properties for each 5d TM monocarbide. Mechanically unstable compounds have empty derived columns. The verifier compares against hidden paper reference values using tolerances appropriate for a different DFT code."
    }
  ],
  "notes": "The CSV must contain one row per compound (9 compounds). Compounds with negative C44 must have empty cells in columns B, G, E, nu, fm, Hv, while still reporting their elastic constants and lattice parameters."
}
```

## How you are scored
A hidden verifier scores your final results.csv by comparing the reported averaged lattice parameters, elastic constants, derived moduli, metallicity, and hardness for each compound against a set of hidden reference values, using appropriate tolerances and structural checks (e.g. correct ordering of hardness among stable compounds, correct identification of unstable compounds). The verifier also checks that the CSV follows the required columns and that base quantities are reported for all nine compounds. The scores for different components are combined into a single reward between 0 and 1. Submitting the paper's reported numbers without a genuine DFT workflow will not meet the tolerance and structural checks.
