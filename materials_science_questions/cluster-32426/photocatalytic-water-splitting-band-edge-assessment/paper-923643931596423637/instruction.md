# Bi2Se3 Surface Doping by Adsorption: DFT Analysis

## Problem background
Bi₂Se₃ is a three-dimensional topological insulator whose surface hosts spin-momentum-locked Dirac cone states. In practice, as-grown crystals are intrinsically n-doped by selenium vacancies, which shift the Fermi level into the bulk conduction band and destroy the topological protection of the surface states. Compensating this n-doping to restore a clean Dirac cone is a key challenge for device applications. Recent experiments have shown that exposing the surface to water vapour followed by UV or soft X-ray irradiation can induce a stable p-doping effect, but the atomistic mechanism remains unclear. This task investigates how different chemical species—water (H₂O), hydroxyl (OH), atomic oxygen (O), atomic carbon (C), and CH—interact with both the pristine and Se‑defective Bi₂Se₃(0001) surfaces, and whether water splitting at a selenium vacancy can supply the oxygen atoms needed to passivate the vacancies and reverse the intrinsic n-doping.

## Approach
The study uses density functional theory (DFT) with a plane‑wave code and the PBE exchange‑correlation functional, plus a van der Waals correction (Grimme D2). Spin‑orbit coupling is taken into account for electronic properties (total energy, Fermi energy) but may be omitted during structural optimisation for efficiency. The bulk Bi₂Se₃ crystal (R‑3m) is first optimised to obtain the equilibrium lattice constants. A slab of four quintuple layers (4 QL) with a 2×2 surface supercell and 15 Å of vacuum is constructed. A surface selenium vacancy is created by removing one Se atom from the topmost Se layer. For each adsorbate (H₂O, OH, O, C, CH) on both the pristine and defective slabs, geometry relaxation is performed followed by a single‑point SOC calculation to obtain the total energy and Fermi energy. Gas‑phase references (H₂O, O₂, H₂, atomic C) are computed in the same unit cell. The adsorption energy is defined as E_ads = E(X/slab) – E(slab) – E(X_gas). The Fermi‑level shift is obtained by aligning the deep valence bands of the adsorbate system to those of a clean 6‑QL slab used as the energy reference. Using the total energies, formation energies are tabulated, and from them reaction energies are calculated for the elementary water‑splitting steps at the selenium vacancy.

## Reproduction target
Compute, using the DFT methodology described above, the adsorption energy (in eV) and Fermi‑level shift (in eV) for each of the five adsorbates (H₂O, OH, O, C, CH) on both the pristine Bi₂Se₃ surface and the Se‑vacancy surface. Also compute the reaction energy ΔE (in eV) for the three elementary steps: (1) H₂O/V → OH/V + H/S, (2) OH/V → O/V + H/S, and the overall reaction (3) H₂O/V → O/V + H₂. Report the adsorption and Fermi‑level data in a CSV file `computed_data.csv` and the reaction energies in a second CSV file `reaction_energies.csv`, following the exact schemas given in the workflow steps. The target is to obtain physically plausible values whose relative ordering, sign, and relative magnitudes are consistent with the expected doping and reaction behaviour—you do not need to match any particular set of published numbers.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- PBE pseudopotentials for Bi, Se, H, O, C: https://www.quantum-espresso.org/pseudopotentials (or SSSP efficiency library)
- Bi2Se3 crystal structure (space group R-3m): 10.1007/s10853-004-8267-2

## Workflow steps

### Step 1: Bulk geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of bulk Bi2Se3 (R-3m) using PBE functional to obtain equilibrium lattice constants a and c.
- Evidence: `/app/outputs/optimized_lattice.txt`

### Step 2: Slab construction and clean surface reference
- Role: process
- Action: Build a 4-QL Bi2Se3(0001) slab with 15 Å vacuum and a 2×2 surface supercell. Compute the total energy and Fermi energy of the clean slab to establish the zero reference. Also compute the band alignment of a 6-QL slab to set the deep-valence alignment reference.
- Evidence: `/app/outputs/clean_slab_ref.txt`

### Step 3: Adsorption on pristine surface
- Role: process
- Action: For each adsorbate (H2O, OH, O, C, CH) on the pristine 2×2 slab, perform geometry relaxation (PBE + D2) and a single-point calculation with spin-orbit coupling to obtain total energy and Fermi energy. Also compute total energies of gas-phase H2O, O2, H2, and atomic C references.
- Evidence: `/app/outputs/pristine_energies.csv`

### Step 4: Adsorption on Se-defective surface
- Role: process
- Action: For the slab with one surface Se vacancy, repeat geometry relaxations and single-point SOC calculations for the five adsorbates. Also compute the total energy of the clean defective slab.
- Evidence: `/app/outputs/defective_energies.csv`

### Step 5: Scored: Adsorption energies and Fermi-level shifts
- Role: scored (load-bearing)
- Action: Post-process the total energies and Fermi energies from the adsorption simulations to compute, for each adsorbate on each surface, the adsorption energy (E_ads = E(X/surface) - E(surface) - E(X_gas)) and the Fermi-level shift relative to the clean surface (for pristine) or clean vacancy surface (for vacancy). Write all results to computed_data.csv.
- Output file: `/app/outputs/computed_data.csv`
- Format: csv
- Contract: species (string), surface_type (string, pristine or vacancy), adsorption_energy (float, eV), fermi_level_shift (float, eV)
- Scoring: scored by hidden verifier

### Step 6: Scored: Reaction energies for water splitting
- Role: scored
- Action: Using the formation energies derived from the total energies, calculate the reaction energies for (1) H2O/V → OH/V + H/S, (2) OH/V → O/V + H/S, and (3) H2O/V → O/V + H2. Write the results to reaction_energies.csv.
- Output file: `/app/outputs/reaction_energies.csv`
- Format: csv
- Contract: reaction (string, one of 'H2O/V -> OH/V + H/S', 'OH/V -> O/V + H/S', 'H2O/V -> O/V + H2'), delta_E (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_data.csv`
- `/app/outputs/reaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_data.csv
- path: `/app/outputs/computed_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of adsorption energies and Fermi-level shifts for H2O, OH, O, C, CH on pristine and Se-defective Bi2Se3 surfaces.
- schema:
  - `type`: table
  - `required_columns`: `species`, `surface_type`, `adsorption_energy`, `fermi_level_shift`
  - `units`:
    - `adsorption_energy`: eV
    - `fermi_level_shift`: eV

### reaction_energies.csv
- path: `/app/outputs/reaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of reaction energies for the three water-splitting steps at a Se vacancy.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `delta_E`
  - `units`:
    - `delta_E`: eV

Notes: The scored artifacts are checked for structural trends: adsorption energy ranking, Fermi-level sign/near-zero for O/V, endothermicity, and reaction energy ordering. No exact reproduction of VASP numbers is required; tolerances account for code/functional differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "surface_type",
          "adsorption_energy",
          "fermi_level_shift"
        ],
        "units": {
          "adsorption_energy": "eV",
          "fermi_level_shift": "eV"
        }
      },
      "description": "Table of adsorption energies and Fermi-level shifts for H2O, OH, O, C, CH on pristine and Se-defective Bi2Se3 surfaces."
    },
    {
      "file": "reaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "delta_E"
        ],
        "units": {
          "delta_E": "eV"
        }
      },
      "description": "Table of reaction energies for the three water-splitting steps at a Se vacancy."
    }
  ],
  "notes": "The scored artifacts are checked for structural trends: adsorption energy ranking, Fermi-level sign/near-zero for O/V, endothermicity, and reaction energy ordering. No exact reproduction of VASP numbers is required; tolerances account for code/functional differences."
}
```

## How you are scored
An automated verifier reads your two CSV files and checks them against hidden reference trends. It evaluates (i) the ranking of adsorption energies on each surface, (ii) whether the Fermi‑level shifts indicate the correct doping character (n‑type, p‑type, or near‑zero) for the different adsorbates, (iii) that all three reaction energies are positive (endothermic) and that step 1 is less endothermic than step 2, and (iv) that the overall reaction energy falls within a physically reasonable window. The checks are weighted: adsorption ranking contributes 0.5, Fermi‑level trends 0.3, and reaction energy trends 0.2, combined into a final reward between 0 and 1. You are not required to reproduce exact numbers; the scoring rewards properly capturing the key physical trends.
