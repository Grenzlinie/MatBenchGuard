# DFT Defect Formation Energy and Band Structure Calculation for Monolayer WTe2

## Problem background
Monolayer WTe2 is a two‑dimensional topological insulator in which band inversion stems from chemical bonding and crystal symmetry rather than atomic relativistic effects. Point defects—such as Te vacancies and Te adatoms—can disrupt the local bonding environment and potentially reverse band inversion, driving the system into a topologically trivial state. This task investigates the influence of Te vacancies and Te adatoms on the electronic structure of monolayer WTe2 by computing defect formation energies and supercell band structures without spin–orbit coupling. The target quantities are the formation energies of a single Te vacancy and a single Te adatom under Te‑rich conditions, and the band gaps along Γ‑X for the pristine, vacancy, and adatom supercells, which together indicate whether band inversion has been reversed.

## Approach
The computational approach builds a monolayer WTe2 slab in the 1T′ phase and constructs a 5 × 3 supercell. Three configurations are prepared: pristine (no defect), one Te vacancy (a single Te atom removed), and one Te adatom (an extra Te atom placed above the layer). Each configuration is relaxed with spin‑unpolarised DFT using the GGA‑PBE functional and pseudopotentials, without spin–orbit coupling. After relaxation, the band structure along the Γ‑X path is computed. An additional DFT calculation on bulk hexagonal Te provides the Te chemical potential μ_Te (total energy per Te atom) in the Te‑rich limit. Defect formation energies are computed from the total energies of the pristine, vacancy, and adatom supercells combined with μ_Te using the standard formulas: E_f(vacancy) = E_total(vacancy) − E_total(pristine) + μ_Te and E_f(adatom) = E_total(adatom) − E_total(pristine) − μ_Te. Band gaps along Γ‑X are determined as the minimum energy separation between the highest occupied and lowest unoccupied states at the Fermi level for each configuration. All DFT calculations are performed with the open‑source Quantum ESPRESSO package.

## Reproduction target
Produce two JSON files in `/app/outputs`. `formation_energies.json` must contain the defect formation energies (in eV) for a Te vacancy and a Te adatom in monolayer WTe2 under Te‑rich conditions, derived from the DFT total energies. `band_gaps.json` must contain the band gaps (in eV) along Γ‑X for the pristine, Te‑vacancy, and Te‑adatom supercells, extracted from the computed band structures without spin–orbit coupling. Together these results quantify how the defects affect the electronic structure, as assessed by the verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library (GGA-PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): ase
- pymatgen: pymatgen
- Monolayer WTe2 1T′ crystal structure
- Bulk Te hexagonal crystal structure

## Workflow steps

### Step 1: Bulk Te reference DFT calculation
- Role: process
- Action: Perform DFT calculation for bulk Te (hexagonal structure) using GGA-PBE functional to obtain the total energy per Te atom (μ_Te). Save the total energy to a file.
- Evidence: `/app/outputs/bulk_Te_energy.txt`

### Step 2: Pristine WTe2 supercell DFT calculation
- Role: process
- Action: Build a 5×3 supercell of monolayer WTe2 in the 1T′ phase, relax the atomic positions using DFT (GGA-PBE, no SOC), and compute the band structure along the Γ-X path. Save the total energy and the Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/pristine_total_energy.txt`

### Step 3: Te vacancy supercell DFT calculation
- Role: process
- Action: Build the 5×3 supercell with one Te vacancy (remove a Te atom), relax the geometry using DFT (GGA-PBE, no SOC), and compute the band structure along Γ-X. Save total energy and eigenvalues.
- Evidence: `/app/outputs/vacancy_total_energy.txt`

### Step 4: Te adatom supercell DFT calculation
- Role: process
- Action: Build the 5×3 supercell with one Te adatom placed on the monolayer, relax the geometry, and compute the band structure along Γ-X (GGA-PBE, no SOC). Save total energy and eigenvalues.
- Evidence: `/app/outputs/adatom_total_energy.txt`

### Step 5: Compute defect formation energies
- Role: scored (load-bearing)
- Action: Calculate the defect formation energies for the Te vacancy and Te adatom using the formula: E_f(vacancy) = E_total(vacancy) - E_total(pristine) + μ_Te, E_f(adatom) = E_total(adatom) - E_total(pristine) - μ_Te, where μ_Te is the total energy per atom of bulk Te from step_01. Output the results as a JSON file.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {"vacancy_formation_energy_eV": number, "adatom_formation_energy_eV": number}
- Scoring: scored by hidden verifier

### Step 6: Extract band gaps along Γ-X
- Role: scored (load-bearing)
- Action: From the band structures computed in steps 02–04, determine the minimum energy gap between the highest occupied and lowest unoccupied states along the Γ-X path at the Fermi level for the pristine, vacancy, and adatom supercells. Output the three gap values as a JSON file.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"pristine_gap_eV": number, "vacancy_gap_eV": number, "adatom_gap_eV": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Defect formation energies (in eV) for a Te vacancy and a Te adatom in monolayer WTe2 under Te-rich conditions, derived from DFT total energies.
- schema:
  - `type`: object
  - `required`:
    - `vacancy_formation_energy_eV`: number
    - `adatom_formation_energy_eV`: number

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Band gaps (in eV) along Γ‑X for pristine, Te‑vacancy, and Te‑adatom supercells. The verifier will evaluate these against reference thresholds to assess the paper's topological claims.
- schema:
  - `type`: object
  - `required`:
    - `pristine_gap_eV`: number
    - `vacancy_gap_eV`: number
    - `adatom_gap_eV`: number

Notes: Formation energies compared to paper values with tolerance 0.3 eV. Band gaps audited by threshold; the exact thresholds are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "vacancy_formation_energy_eV": "number",
          "adatom_formation_energy_eV": "number"
        }
      },
      "description": "Defect formation energies (in eV) for a Te vacancy and a Te adatom in monolayer WTe2 under Te-rich conditions, derived from DFT total energies."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "pristine_gap_eV": "number",
          "vacancy_gap_eV": "number",
          "adatom_gap_eV": "number"
        }
      },
      "description": "Band gaps (in eV) along Γ‑X for pristine, Te‑vacancy, and Te‑adatom supercells. The verifier will evaluate these against reference thresholds to assess the paper's topological claims."
    }
  ],
  "notes": "Formation energies compared to paper values with tolerance 0.3 eV. Band gaps audited by threshold; the exact thresholds are not disclosed to the agent."
}
```

## How you are scored
A hidden verifier reads your two output files and compares the reported values against reference criteria derived from the same computational protocol (GGA‑PBE, no SOC, Te‑rich limit, 5 × 3 supercell). Formation energies are checked numerically: they are compared to reference values obtained from the paper’s DFT workflow, and scoring rewards values that lie within a tolerance that accounts for toolchain and implementation differences. Band gaps are compared against reference thresholds; the exact criteria are not disclosed. The final reward is a weighted combination of the scores from both output files. Reporting a number without running the required DFT calculations will not satisfy the checks.
