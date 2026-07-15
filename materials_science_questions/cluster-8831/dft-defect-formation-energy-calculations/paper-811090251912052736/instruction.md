# Vacancy Formation Energies in BiCuSeO from Density Functional Theory

## Problem background
The layered oxyselenide BiCuSeO is a promising oxide thermoelectric material that can operate at high temperatures, largely because its intrinsically low thermal conductivity arises from the unique alternating Cu₂Se₂ and Bi₂O₂ layers. To optimize its thermoelectric performance, controlling crystal defects — particularly Bi and Cu vacancies — is crucial. This work investigates how high-pressure synthesis alters the defect landscape, using first-principles density functional theory (DFT) to quantify the energetic costs of forming these vacancies. The key computational claim is that vacancy formation energies can be computed from DFT total-energy calculations and that these energies are sensitive to pressure. The task here is to compute the ambient-pressure formation energies of a Bi vacancy and a Cu vacancy in BiCuSeO using the supercell approach and standard DFT methodology.

## Approach
We employ plane-wave density functional theory (DFT) with the generalized gradient approximation (GGA-PBE) and projector-augmented-wave (PAW) pseudopotentials. A 2×2×1 supercell of the tetragonal P4/nmm BiCuSeO structure (containing 32 atoms) is constructed. Three structures are relaxed: (i) the perfect supercell, (ii) a supercell with one Bi atom removed (V_Bi vacancy), and (iii) a supercell with one Cu atom removed (V_Cu vacancy). The elemental chemical potentials μ_Bi and μ_Cu are obtained from separate DFT calculations on bulk rhombohedral Bi and face‑centered cubic Cu, extracting the total energy per atom. The vacancy formation energy is then computed via the standard formula  E_f = E_defect − E_perfect + μ_removed, where E_defect and E_perfect are the total energies of the defective and perfect supercells, and μ_removed is the per‑atom energy of the removed element from its bulk elemental phase. This procedure yields the two formation energies E_f(Bi) and E_f(Cu) that characterize the propensity for vacancy creation.

## Reproduction target
Produce a JSON file at /app/outputs/results.json containing the total energies (in eV) of the perfect supercell, the Bi‑vacancy supercell, the Cu‑vacancy supercell, the per‑atom total energies of bulk Bi and bulk Cu, and the computed vacancy formation energies E_f(Bi) and E_f(Cu). The formation energies must be derived from the intermediate total energies using the E_f = E_defect − E_perfect + μ_removed formula. The hidden verifier will recompute the formation energies from the intermediates you report and compare the recomputed values against the paper’s reference results.

## Assets

- BiCuSeO crystal structure (tetragonal, P4/nmm): https://materialsproject.org/materials/mp-1009800/
- Bulk Bi structure (rhombohedral): https://materialsproject.org/materials/mp-10625/
- Bulk Cu structure (fcc): https://materialsproject.org/materials/mp-30/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP efficiency library, GGA-PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare supercell structures
- Role: process
- Action: Build 2×2×1 supercells of BiCuSeO from the tetragonal unit cell (space group P4/nmm) with lattice parameters a≈3.93 Å, c≈8.93 Å. Create three structures: a perfect supercell, a supercell with one Bi atom removed (V_Bi), and a supercell with one Cu atom removed (V_Cu). Save the structures in a format suitable for the DFT code.
- Evidence: none

### Step 2: DFT calculation of bulk chemical potentials
- Role: process
- Action: Perform DFT total energy calculations for bulk metallic Bi (rhombohedral) and bulk Cu (fcc) using plane-wave DFT with the GGA-PBE functional. Use pseudopotentials from the SSSP efficiency library. Extract the total energy per atom for each element (μ_Bi, μ_Cu). Optionally record the total energies in a reference file.
- Evidence: `/app/outputs/bulk_energies.json`

### Step 3: DFT relaxation of perfect and defective supercells
- Role: process
- Action: Perform DFT structural relaxation (allowing atomic positions to optimize) for the perfect supercell and each defective supercell (V_Bi and V_Cu) using the same functional and pseudopotential set. Obtain the final total energies E_perfect, E_bi_vac, and E_cu_vac. Optionally save these energies.
- Evidence: `/app/outputs/supercell_energies.json`

### Step 4: Compute vacancy formation energies
- Role: scored (load-bearing)
- Action: Compute the formation energies E_f(Bi) and E_f(Cu) using the standard vacancy formation energy formula: E_f = E_defect - E_perfect + μ_removed, where E_defect and E_perfect are the total energies from step 03 and μ_removed is the elemental chemical potential from step 02. Collect all intermediate values (E_perfect, E_bi_vac, E_cu_vac, μ_Bi, μ_Cu) and the final formation energies into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"perfect_total_energy": float (eV), "Bi_vacancy_total_energy": float, "Cu_vacancy_total_energy": float, "bulk_Bi_total_energy_per_atom": float, "bulk_Cu_total_energy_per_atom": float, "Ef_Bi_vacancy": float, "Ef_Cu_vacancy": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The scored artifact containing total energies, chemical potentials, and the computed vacancy formation energies. The checker will recompute the formation energies from the intermediate total energies and chemical potentials, then compare them to reference values within a tolerance.
- schema:
  - `type`: object
  - `required`: `perfect_total_energy`, `Bi_vacancy_total_energy`, `Cu_vacancy_total_energy`, `bulk_Bi_total_energy_per_atom`, `bulk_Cu_total_energy_per_atom`, `Ef_Bi_vacancy`, `Ef_Cu_vacancy`
  - `properties`:
    - `perfect_total_energy`:
      - `type`: number
      - `units`: eV
    - `Bi_vacancy_total_energy`:
      - `type`: number
      - `units`: eV
    - `Cu_vacancy_total_energy`:
      - `type`: number
      - `units`: eV
    - `bulk_Bi_total_energy_per_atom`:
      - `type`: number
      - `units`: eV
    - `bulk_Cu_total_energy_per_atom`:
      - `type`: number
      - `units`: eV
    - `Ef_Bi_vacancy`:
      - `type`: number
      - `units`: eV
    - `Ef_Cu_vacancy`:
      - `type`: number
      - `units`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "perfect_total_energy",
          "Bi_vacancy_total_energy",
          "Cu_vacancy_total_energy",
          "bulk_Bi_total_energy_per_atom",
          "bulk_Cu_total_energy_per_atom",
          "Ef_Bi_vacancy",
          "Ef_Cu_vacancy"
        ],
        "properties": {
          "perfect_total_energy": {
            "type": "number",
            "units": "eV"
          },
          "Bi_vacancy_total_energy": {
            "type": "number",
            "units": "eV"
          },
          "Cu_vacancy_total_energy": {
            "type": "number",
            "units": "eV"
          },
          "bulk_Bi_total_energy_per_atom": {
            "type": "number",
            "units": "eV"
          },
          "bulk_Cu_total_energy_per_atom": {
            "type": "number",
            "units": "eV"
          },
          "Ef_Bi_vacancy": {
            "type": "number",
            "units": "eV"
          },
          "Ef_Cu_vacancy": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "The scored artifact containing total energies, chemical potentials, and the computed vacancy formation energies. The checker will recompute the formation energies from the intermediate total energies and chemical potentials, then compare them to reference values within a tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json, recomputes the vacancy formation energies from the intermediate total energies and chemical potentials you supply, and compares these recomputed values to the paper’s reported formation energies. Your score is based on how closely your computed formation energies match the expected reference. The exact comparison criteria and tolerances are hidden. No other output files contribute to the score.
