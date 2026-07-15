# Oxygen Vacancy Formation Energy Calculation in SrFeO2.875 via GGA+U DFT

## Problem background
SrFeO3-δ is a prototypical perovskite oxide that easily accommodates oxygen vacancies, making it a candidate material for solid oxide fuel cell electrodes, oxygen separation membranes, and catalytic applications. Understanding how a single oxygen vacancy redistributes charge among the surrounding metal and oxygen atoms, and how much energy is required to create that vacancy, is essential for rational design of such oxygen-ion conductors. Density functional theory (DFT) provides a first-principles route to quantify these properties. This task targets the oxygen-deficient composition SrFeO2.875 (i.e., δ = 0.125) and asks: (i) Which atoms gain or lose electron density when a vacancy is introduced, and in what relative order? (ii) What is the oxygen vacancy formation energy, both uncorrected and corrected for the well-known O2 overbinding error?

## Approach
The procedure follows a plane-wave pseudopotential DFT approach. First, construct the (SrFeO3)8 and (SrFeO2.875)8 supercells: a 2×2×2 repetition of the cubic unit cell, with the central oxygen removed in the defective cell and the lattice constant adjusted appropriately. Two levels of exchange‑correlation are used: pure PBE GGA for the uncorrected formation energy, and PBE GGA+U (with a Hubbard U on Fe) for the corrected formation energy and for the Löwdin population analysis. All calculations are performed in the nonmagnetic configuration (NM2). Atomic positions in the defective supercell are relaxed until forces are below a tight threshold. Löwdin populations are extracted for the stoichiometric SrFeO3 reference and for every symmetry‑inequivalent atom in SrFeO2.875 (Fe1, Fe2, Fe3, Sr1, Sr2, O1‑O7). Separately, the total energy of an isolated triplet O2 molecule is computed at the GGA level. The uncorrected vacancy formation energy E_vf1 is obtained from the GGA total energies of SrFeO3, SrFeO2.875, and half the O2 energy. The corrected formation energy E_vf2 replaces the solid‑phase GGA energies with their GGA+U counterparts and adds a constant per‑oxygen correction of 0.68 eV to account for the systematic overbinding of O2 in GGA. The comparison reveals whether charge transfers principally to the nearest Fe atom and provides two formation energies that can be benchmarked against literature expectations.

## Reproduction target
For the nonmagnetic (NM2) case only, produce two scored artifacts:

1. `step_01_lowdin_populations.csv` – a CSV containing the Löwdin total atomic populations (in electrons). The file must have one block for stoichiometric SrFeO3 (rows Fe, Sr, O) and one block for SrFeO2.875 (rows Fe1, Fe2, Fe3, Sr1, Sr2, O1, O2, O3, O4, O5, O6, O7). The populations should reflect the vacancy‑induced charge redistribution and must exhibit the correct ordering among the atoms closest to the vacancy.

2. `step_02_vacancy_formation_energy.txt` – a plain text file with two lines giving the oxygen vacancy formation energies (in eV). The first line reports E_vf1, computed as E(SrFeO2.875)GGA + 0.5·E(O2)GGA – 8·E(SrFeO3)GGA. The second line reports E_vf2, computed as E(SrFeO2.875)GGA+U + 0.5·E(O2)GGA – 8·E(SrFeO3)GGA+U + 0.68 eV.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PBE ultrasoft pseudopotentials for Fe, Sr, O (SSSP efficiency v1.3): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Build the (SrFeO3)8 and (SrFeO2.875)8 supercells from the cubic unit cell (a=3.869 Å) as described: a 2×2×2 supercell, then for SrFeO2.875 remove the central oxygen and shrink the lattice constant to a_p=3.864 Å per supercell side (2a_p). Generate Quantum ESPRESSO input files with atomic positions and appropriate k‑point grid.
- Evidence: `/app/outputs/supercell_inputs.tar.gz`

### Step 2: GGA+U structural relaxation of SrFeO2.875
- Role: process
- Action: Using Quantum ESPRESSO with PBE GGA+U (U=4.3 eV on Fe), cold smearing 0.01 Ry, kinetic energy cutoffs 40/500 Ry, Monkhorst-Pack 4×4×4 k‑point grid, relax all atomic positions of (SrFeO2.875)8 until all forces < 0.026 eV/Å. Save the final charge density and wavefunction for subsequent population analysis.
- Evidence: `/app/outputs/srfeo2875_relax_ggau.out`

### Step 3: GGA+U reference calculation of SrFeO3
- Role: process
- Action: Using the same GGA+U setup, perform a single-point calculation on the (SrFeO3)8 supercell (nonmagnetic configuration, experimental lattice constant, ideal positions) to obtain the total energy and charge density for subsequent population analysis and formation energy.
- Evidence: `/app/outputs/srfeo3_scf_ggau.out`

### Step 4: Extract Löwdin populations
- Role: scored
- Action: Post-process the outputs from the GGA+U runs to extract Löwdin total atomic populations. For SrFeO3: extract values for Fe, Sr, O. For SrFeO2.875: extract the populations for Fe1, Fe2, Fe3, Sr1, Sr2, O1–O7 (NM2 column of Table 2). Write step_01_lowdin_populations.csv.
- Output file: `/app/outputs/step_01_lowdin_populations.csv`
- Format: csv
- Contract: Table with columns: configuration (string), atom_type (string), population (float, electrons).
- Scoring: scored by hidden verifier

### Step 5: GGA calculation of isolated O2 molecule
- Role: process
- Action: Run a spin-polarized GGA (PBE) calculation for the triplet O2 molecule in a 10×10×10 Å³ cell, relaxing the bond length. Use kinetic energy cutoffs 80 Ry (wavefunctions) and 500 Ry (charge density), Gamma‑point only. Store the relaxed total energy (in Ry).
- Evidence: `/app/outputs/o2_gga.out`

### Step 6: GGA relaxation of SrFeO2.875
- Role: process
- Action: Using PBE GGA (no +U), relax atomic positions of the (SrFeO2.875)8 supercell (starting from a_p=3.864 Å) with the same k‑mesh, cutoffs, and force threshold as the GGA+U run. Save the total energy.
- Evidence: `/app/outputs/srfeo2875_relax_gga.out`

### Step 7: GGA reference total energy of SrFeO3
- Role: process
- Action: Perform a single-point GGA calculation on the (SrFeO3)8 supercell (nonmagnetic, experimental lattice constant) to obtain the total energy. Use identical cutoffs and k‑mesh as for the GGA+U reference.
- Evidence: `/app/outputs/srfeo3_scf_gga.out`

### Step 8: Compute oxygen vacancy formation energies
- Role: scored (load-bearing)
- Action: From the total energies extracted in the previous steps, compute the uncorrected formation energy E_vf1 = E(SrFeO2.875)GGA + 0.5*E(O2)GGA – 8*E(SrFeO3)GGA, and the corrected formation energy E_vf2 = E(SrFeO2.875)GGA+U + 0.5*E(O2)GGA – 8*E(SrFeO3)GGA+U + 0.68 eV. Write both values to step_02_vacancy_formation_energy.txt.
- Output file: `/app/outputs/step_02_vacancy_formation_energy.txt`
- Format: txt
- Contract: Two lines, each starting with 'E_vf1 = ' or 'E_vf2 = ', followed by a floating-point number and ' eV'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lowdin_populations.csv`
- `/app/outputs/step_02_vacancy_formation_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lowdin_populations.csv
- path: `/app/outputs/step_01_lowdin_populations.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Löwdin total atomic populations (in electrons) for the nonmagnetic (NM2) case of SrFeO3 and SrFeO2.875. The file contains a block for SrFeO3 with rows Fe, Sr, O, and a block for SrFeO2.875 with rows Fe1, Fe2, Fe3, Sr1, Sr2, O1–O7.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `atom_type`, `population`

### step_02_vacancy_formation_energy.txt
- path: `/app/outputs/step_02_vacancy_formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Oxygen vacancy formation energies E_vf1 (uncorrected GGA) and E_vf2 (corrected GGA+U) for the nonmagnetic (NM2) case, both in eV.
- schema:
  - `type`: text
  - `required`:
    - `lines`: two lines

Notes: All DFT calculations use the nonmagnetic configuration (NM2). The agent must perform the full pipeline to obtain the required total energies; no pre-computed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lowdin_populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "atom_type",
          "population"
        ]
      },
      "description": "Löwdin total atomic populations (in electrons) for the nonmagnetic (NM2) case of SrFeO3 and SrFeO2.875. The file contains a block for SrFeO3 with rows Fe, Sr, O, and a block for SrFeO2.875 with rows Fe1, Fe2, Fe3, Sr1, Sr2, O1–O7."
    },
    {
      "file": "step_02_vacancy_formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "lines": "two lines"
        }
      },
      "description": "Oxygen vacancy formation energies E_vf1 (uncorrected GGA) and E_vf2 (corrected GGA+U) for the nonmagnetic (NM2) case, both in eV."
    }
  ],
  "notes": "All DFT calculations use the nonmagnetic configuration (NM2). The agent must perform the full pipeline to obtain the required total energies; no pre-computed data is provided."
}
```

## How you are scored
A hidden verifier reads your submitted artifacts and compares them against gold values extracted from the literature. For the populations CSV, it checks the numerical values for key atoms and verifies that the relative ordering among them (e.g., which atom receives the most charge) matches the reference. For the formation energy text file, it compares E_vf1 and E_vf2 to expected values within a tolerance that accounts for typical code‑to‑code variation in DFT. Each scored step carries a weight, and the final reward is a weighted sum. Reporting numbers that lie outside the tolerance, or that violate the required ordering, results in a reduced score. Simply printing a number, without genuinely running the DFT pipeline, will not produce values that fall within the acceptance windows, so honest execution is essential to receive full credit.
