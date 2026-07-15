# Point defect formation energy under biaxial strain in LaAlO3 using DFT

## Problem background
Perovskite‑structure oxides like LaAlO₃ are widely studied for thin‑film applications because their properties can be tuned by epitaxial strain. When a film is grown coherently on a substrate with a different lattice constant, the in‑plane biaxial strain alters the crystal structure and may also affect the concentration of point defects such as oxygen vacancies. Understanding this interplay is important because oxygen vacancies can drastically change the electronic and structural behavior of the oxide.

This task investigates the relationship between biaxial strain and oxygen vacancy formation in LaAlO₃ using first‑principles density functional theory (DFT). The goal is to compute the change in oxygen vacancy formation energy for ±2% biaxial strain relative to the unstrained bulk, providing a quantitative measure of whether strain alone can significantly alter the intrinsic defect formation energy.

## Approach
We use DFT within the GGA+U approximation (PBE functional, Hubbard U = 10.32 eV on La 4f states, Dudarev method, fully localized limit) to compute total energies of bulk LaAlO₃ and of supercells containing a single neutral oxygen vacancy.

The workflow consists of:
- Determining the equilibrium pseudocubic lattice constant a₀ of bulk LaAlO₃ from a cell relaxation.
- Computing the reference total energy of an isolated O₂ molecule to define the oxygen chemical potential μ₀ = ½ E(O₂).
- Building a 2×2×2 supercell (40 atoms) and calculating the total energy of the pristine (defect‑free) supercell under three biaxial strain states: unstrained (ε = 0%), compressive (ε = −2%), and tensile (ε = +2%). For each strain, the in‑plane lattice parameters are fixed according to ε, and the out‑of‑plane parameter and atomic positions are relaxed.
- Introducing one neutral oxygen vacancy at the axial position (perpendicular to the strain plane) and repeating the total energy calculations for the same three strain states.
- Finally, computing the oxygen vacancy formation energy Ω(ε) = E_tot(V_O, ε) − E_tot(bulk, ε) + μ₀ and evaluating the strain‑induced changes ΔΩ_comp = Ω(−2%) − Ω(0) and ΔΩ_tens = Ω(+2%) − Ω(0), both expressed in meV.

The entire pipeline is executed with a DFT code that supports GGA+U and the Dudarev correction (e.g., Quantum ESPRESSO or GPAW). All results are derived solely from the computed total energies.

## Reproduction target
Produce the following two numerical quantities, both in units of meV, and write them as a JSON object to `/app/outputs/strain_effect.json`:

- `compressive_strain_2pct_delta_meV` – the change in oxygen vacancy formation energy between 2% compressive biaxial strain (ε = −2%) and the unstrained case (ε = 0%).
- `tensile_strain_2pct_delta_meV` – the change in oxygen vacancy formation energy between 2% tensile biaxial strain (ε = +2%) and the unstrained case.

The formation energy itself is computed from the total energies of the defective and pristine supercells and the O₂ reference energy as described in the Approach and the workflow steps.

## Assets

- DFT code with GGA+U capability and Dudarev method support (e.g., Quantum ESPRESSO, GPAW): https://www.quantum-espresso.org/
- Bulk LaAlO3 rhombohedral R‑3c crystal structure

## Workflow steps

### Step 1: Calculate equilibrium lattice constant of bulk LaAlO3
- Role: process
- Action: Perform DFT structural relaxation of the 10‑atom rhombohedral unit cell of LaAlO₃ using the GGA+U settings (PBE functional, Hubbard U=10.32 eV on La 4f, Dudarev method, fully localized limit) to obtain the equilibrium pseudocubic lattice constant a0.
- Evidence: `/app/outputs/bulk_eq_info.json`

### Step 2: Compute total energy of an isolated O2 molecule
- Role: process
- Action: Compute the total energy of an oxygen molecule (spin‑polarized, placed in a large periodic box) using the same DFT functional, pseudopotentials, and plane‑wave cutoff as for LaAlO₃, to provide the reference chemical potential μ_O = ½ E(O₂).
- Evidence: `/app/outputs/o2_energy.txt`

### Step 3: Compute total energies of pristine LaAlO3 supercells under biaxial strain
- Role: process
- Action: Construct a 2×2×2 supercell (40 atoms) from the relaxed rhombohedral cell. For each biaxial strain state (ε = −2%, 0%, +2%): set the in‑plane lattice parameters to a = a0(1+ε), relax the out‑of‑plane lattice parameter and atomic positions while keeping in‑plane dimensions fixed, and record the final total energy of the defect‑free supercell.
- Evidence: `/app/outputs/pristine_energies.json`

### Step 4: Compute total energies of oxygen‑vacancy supercells under biaxial strain
- Role: process
- Action: Using the 2×2×2 supercell, introduce one neutral oxygen vacancy at the axial position (position 1, perpendicular to the strain plane). For the same strain states (ε = −2%, 0%, +2%), relax the cell and ions (keeping in‑plane dimensions fixed) and record the total energy of the neutral vacancy supercell.
- Evidence: `/app/outputs/defective_energies.json`

### Step 5: Compute formation energies and strain dependence
- Role: scored
- Action: Using the energies from previous steps, compute for each strain the oxygen vacancy formation energy: Ω(ε) = E_tot(V_O, ε) − E_tot(bulk, ε) + μ_O, with μ_O taken from step_02. Then compute ΔΩ_comp = Ω(ε=−2%) − Ω(ε=0) and ΔΩ_tens = Ω(ε=+2%) − Ω(ε=0), both in meV. Write these two values to strain_effect.json.
- Output file: `/app/outputs/strain_effect.json`
- Format: json
- Contract: {"compressive_strain_2pct_delta_meV": number, "tensile_strain_2pct_delta_meV": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strain_effect.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strain_effect.json
- path: `/app/outputs/strain_effect.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Strain‑induced change in oxygen vacancy formation energy (ΔΩ) for ±2% biaxial strain, extracted from total‑energy differences.
- schema:
  - `type`: object
  - `required`: `compressive_strain_2pct_delta_meV`, `tensile_strain_2pct_delta_meV`
  - `properties`:
    - `compressive_strain_2pct_delta_meV`:
      - `type`: number
      - `units`: meV
    - `tensile_strain_2pct_delta_meV`:
      - `type`: number
      - `units`: meV

Notes: Only the relative changes ΔΩ are scored. The checker verifies the reported values against the paper‑reported result with empirical tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strain_effect.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "compressive_strain_2pct_delta_meV",
          "tensile_strain_2pct_delta_meV"
        ],
        "properties": {
          "compressive_strain_2pct_delta_meV": {
            "type": "number",
            "units": "meV"
          },
          "tensile_strain_2pct_delta_meV": {
            "type": "number",
            "units": "meV"
          }
        }
      },
      "description": "Strain‑induced change in oxygen vacancy formation energy (ΔΩ) for ±2% biaxial strain, extracted from total‑energy differences."
    }
  ],
  "notes": "Only the relative changes ΔΩ are scored. The checker verifies the reported values against the paper‑reported result with empirical tolerances."
}
```

## How you are scored
A hidden verifier reads the `strain_effect.json` file and compares the two delta values against reference results obtained from the original study. The comparison uses pre‑defined tolerances that account for the legitimate numerical spread arising from different DFT implementations, pseudopotentials, and plane‑wave cutoffs.

Your reward is proportional to the number of deltas that fall within their respective tolerance ranges. The verifier does not require an exact match to the reference; it expects values that are consistent with the calculations, within the allowed margins. The final reward is a float between 0 and 1, where 1 indicates both deltas are within tolerance. The verifier does not accept a simple reporting of expected numbers; it checks that the submitted values are realistic and consistent with the computational pipeline described.
