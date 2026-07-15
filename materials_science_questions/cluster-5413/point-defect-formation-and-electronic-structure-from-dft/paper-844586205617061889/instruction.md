# DFT formation energies of Cd defects in α-MoO3

## Problem background
The layered semiconductor α-MoO3 (orthorhombic, space group Pbnm) consists of Mo-O6 octahedra forming sheets held together by weak van der Waals forces. It has three distinct oxygen sites: singly coordinated O1, doubly coordinated O2, and triply coordinated O3. The van der Waals gap can host intercalated impurities, while oxygen vacancies, particularly at the O2 sites, are the most common native point defects. When Cd is implanted into α-MoO3, a variety of defect configurations involving Cd substitutional, interstitial, and Cd-oxygen-vacancy complexes may form, and their relative stability influences the material's electronic properties. Understanding which configurations are most stable is a key step in interpreting experimental hyperfine measurements and polaron effects.

## Approach
We will use density functional theory (DFT) with a plane-wave PAW code that supports DFT+U and van der Waals corrections (e.g., Quantum ESPRESSO or CP2K). The functional is PBE+U with an effective Hubbard U of 6 eV on the Mo 4d states, combined with the DFT-D3(BJ) dispersion correction to account for interlayer interactions. A 3×1×2 supercell of α-MoO3 is built using the experimental lattice constants (a=3.96 Å, b=13.86 Å, c=3.69 Å). Four defect configurations are considered: substitutional Cd (replacing one Mo), interstitial Cd placed in the van der Waals gap, interstitial Cd with one O2 vacancy adjacent to it, and interstitial Cd with two O2 vacancies in different planes. Total energies are computed for the pristine supercell, the defective supercells, as well as for reference bulk phases (Mo bcc, Cd hcp) and the O2 molecule (spin-polarized). Formation energies are then derived from these total energies using standard chemical-potential formulas that account for the number of added/removed atoms. The result is a relative stability comparison among the four configurations.

## Reproduction target
Compute and report the DFT formation energies for the four Cd defect configurations (substitutional Cd, interstitial Cd, interstitial Cd with one O2 vacancy, interstitial Cd with two O2 vacancies in different planes) in α-MoO3. The energies must be written to a CSV file with columns 'configuration' and 'formation_energy_eV'. The hidden verifier will assess the relative stability ordering among these configurations.

## Assets

- DFT code with PAW, DFT+U and van der Waals correction (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- PAW pseudopotentials for Mo, O, Cd (PBE): https://www.physics.rutgers.edu/gbrv/
- α-MoO3 crystal structure (orthorhombic, Pbnm, a=3.96 Å, b=13.86 Å, c=3.69 Å): COD ID 2100808 or ICSD 84370
- Reference total energies for bulk Mo (bcc), Cd (hcp), and O2 molecule

## Workflow steps

### Step 1: Prepare supercells for pristine and defect configurations
- Role: process
- Action: Construct 3x1x2 supercells for pristine alpha-MoO3 and for the Cd defect configurations: substitutional Cd (Cd_s), interstitial Cd at vdW gap (Cd_I), Cd_I with one O2 vacancy (Cd_I^{VO2}), Cd_I with two O2 vacancies in different planes (^{VO2}Cd_I^{VO2}), using the experimental lattice constants.
- Evidence: `/app/outputs/supercell_structures.txt`

### Step 2: Compute reference total energies for Mo, Cd, and O2
- Role: process
- Action: Using the selected DFT functional (PBE+U=6 eV on Mo, D3(BJ) dispersion), compute total energies for bulk Mo (bcc), bulk Cd (hcp), and O2 molecule (spin-polarized).
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Relax defect supercells and compute total energies
- Role: process
- Action: Perform ionic relaxation (forces < 0.01 eV/Å) for the pristine supercell and the four defect supercells from Step 1 with the same DFT settings, then compute final total energies.
- Evidence: `/app/outputs/total_energies.json`

### Step 4: Calculate defect formation energies and verify stability ordering
- Role: scored (load-bearing)
- Action: Use the total energies from Step 3 and the reference energies from Step 2 to compute formation energies using the standard defect formation formulas (for substitutional: E_F = E(Mo1-xCds_xO3) - E(MoO3) - x*E_Cd + (1-x)*E_Mo; for interstitial: E_F = E(MoCdI_nO3) - E(MoO3) - n*E_Cd; for vacancy complexes: E_F = E(defect) - E(MoCdI_nO3) + (N_vac/2)*E(O2) + E_F(Cd_I)). Report results in formation_energies.csv with columns configuration and formation_energy_eV.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: configuration (string), formation_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies for Cd substitutional, interstitial, and Cd+O2 vacancy complexes. The checker will verify the relative ordering: formation_energy(Cd_s) > formation_energy(Cd_I) > formation_energy(Cd_I^{VO2}) > formation_energy(^{VO2}Cd_I^{VO2}) (strict ordering required).
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

Notes: Only the formation energy ordering is scored; absolute values may differ due to code/pseudopotential differences. The agent must compute all four configurations; missing entries or a wrong ordering results in zero credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energies for Cd substitutional, interstitial, and Cd+O2 vacancy complexes. The checker will verify the relative ordering: formation_energy(Cd_s) > formation_energy(Cd_I) > formation_energy(Cd_I^{VO2}) > formation_energy(^{VO2}Cd_I^{VO2}) (strict ordering required)."
    }
  ],
  "notes": "Only the formation energy ordering is scored; absolute values may differ due to code/pseudopotential differences. The agent must compute all four configurations; missing entries or a wrong ordering results in zero credit."
}
```

## How you are scored
After you write the required output files under `/app/outputs`, a hidden verifier reads your `formation_energies.csv` and checks that all four configurations are present and that the formation energies follow the correct relative ordering. Because the absolute formation energies depend on your chosen DFT code, pseudopotentials, and convergence settings, the verifier does NOT require an exact match to a specific numeric value; instead it verifies the ORDER of formation energies (e.g., which configuration is most stable, which is least stable) and that the required four entries exist. Only the formation energy ordering is scored; other intermediate files are not graded. You must compute all four configurations—missing any entry will result in zero credit for the ordering check.
