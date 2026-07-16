# DFT energetics of oxygen transfer from graphene oxide to Zn and ZnO

## Problem background
A crucial step in understanding the spontaneous formation of a ZnO monolayer on graphene oxide is quantifying the energetics of oxygen transfer from oxygen-containing functional groups on graphene oxide to metallic zinc and to ZnO surface oxygen vacancies. The paper uses first-principles density functional theory (DFT) to compute the reaction energies and energy barriers for these processes, which are proposed to drive the oxidation of Zn and the deoxygenation of graphene oxide. This task reproduces those DFT calculations to obtain the key thermodynamic and kinetic quantities that underpin the proposed redox mechanism.

## Approach
The computational approach employs plane-wave DFT with the Perdew–Burke–Ernzerhof (PBE) functional and Grimme’s D3 dispersion correction, using an open‑source code such as Quantum ESPRESSO. Slab models are constructed for a clean Zn(0001) surface, a ZnO(0001) surface containing an oxygen vacancy, and a graphene oxide layer functionalised with epoxide and hydroxyl groups. Total energy calculations and relaxation of atomic positions are performed for initial, final, and transition‑state configurations. Reaction energies are obtained from the differences between the total energies of the relevant reactant and product configurations. Energy barriers for oxygen migration are computed via climbing‑image nudged elastic band (NEB) calculations. The calculations yield four quantities: the reaction energy of bulk Zn oxidation per oxygen atom, the energy change when an epoxide oxygen moves from graphene oxide to a Zn metal surface, the energy barrier for oxygen transfer from an oxygen‑containing group on graphene oxide to a ZnO surface oxygen vacancy, and the energy change when a hydroxyl group oxygen is transferred to metallic Zn.

## Reproduction target
Your goal is to compute the following four energetic quantities using the DFT methodology described above:
1. Reaction energy of bulk Zn oxidation (Zn + O → ZnO) in eV per oxygen atom.
2. Energy change (ΔE) when an epoxide oxygen atom migrates from graphene oxide to a Zn metal surface (negative values indicate exothermicity).
3. Energy barrier for oxygen transfer from an oxygen‑containing functional group on graphene oxide (epoxide or hydroxyl) to a ZnO surface oxygen vacancy.
4. Energy change (ΔE) when a hydroxyl group oxygen is transferred to a metallic Zn surface (negative values indicate exothermicity).

Extract these four values and write them to a JSON file at `/app/outputs/dft_energetics.json` with the keys: `reaction_energy_bulk_Zn_oxidation_eV_per_O`, `exothermicity_epoxide_migration_Zn_eV`, `energy_barrier_O_transfer_vacancy_eV`, and `exothermicity_hydroxyl_transfer_Zn_eV`. All values are in eV.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): ase
- Materials Project crystal structures: https://materialsproject.org/
- Crystallography Open Database (COD): https://www.crystallography.net/cod/

## Workflow steps

### Step 1: Run DFT calculations for oxygen transfer energetics
- Role: process
- Action: Construct slab models of a clean Zn(0001) surface, a ZnO(0001) surface with an oxygen vacancy, and graphene oxide with epoxide and hydroxyl functional groups. Perform DFT relaxations and, for the oxygen migration barrier to the ZnO surface vacancy, a nudged elastic band (NEB) calculation to obtain total energies of initial, final, and transition states. Writing of intermediate energies or logs is performed but no scored artifact is produced here.
- Evidence: `/app/outputs/dft_run.log`

### Step 2: Report computed DFT reaction energies and barrier
- Role: scored (load-bearing)
- Action: Extract the required energetic quantities from the completed DFT calculations and write them to dft_energetics.json.
- Output file: `/app/outputs/dft_energetics.json`
- Format: json
- Contract: {"type": "object", "properties": {"reaction_energy_bulk_Zn_oxidation_eV_per_O": {"type": "number", "description": "Reaction energy of Zn + O -> ZnO in eV per oxygen atom, computed with DFT+dispersion"}, "exothermicity_epoxide_migration_Zn_eV": {"type": "number", "description": "Exothermicity of an epoxide oxygen migrating from graphene oxide to a Zn metal surface, in eV"}, "energy_barrier_O_transfer_vacancy_eV": {"type": "number", "description": "Energy barrier for oxygen transfer from graphene oxide (epoxide/hydroxyl) to a ZnO surface oxygen vacancy, in eV"}, "exothermicity_hydroxyl_transfer_Zn_eV": {"type": "number", "description": "Exothermicity of hydroxyl group oxygen transfer to metallic Zn, in eV"}}, "required": ["reaction_energy_bulk_Zn_oxidation_eV_per_O", "exothermicity_epoxide_migration_Zn_eV", "energy_barrier_O_transfer_vacancy_eV", "exothermicity_hydroxyl_transfer_Zn_eV"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_energetics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_energetics.json
- path: `/app/outputs/dft_energetics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed reaction energies and migration barrier for oxygen transfer from graphene oxide functional groups to metallic Zn and to ZnO surface oxygen vacancies. The checker compares each numeric value against the hidden paper-reported reference values with field-specific tolerances.
- schema:
  - `type`: object
  - `required`:
    - `reaction_energy_bulk_Zn_oxidation_eV_per_O`: number (eV per O atom)
    - `exothermicity_epoxide_migration_Zn_eV`: number (eV)
    - `energy_barrier_O_transfer_vacancy_eV`: number (eV)
    - `exothermicity_hydroxyl_transfer_Zn_eV`: number (eV)

Notes: Only the listed fields are scored. Additional details may be present but are not checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_energetics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "reaction_energy_bulk_Zn_oxidation_eV_per_O": "number (eV per O atom)",
          "exothermicity_epoxide_migration_Zn_eV": "number (eV)",
          "energy_barrier_O_transfer_vacancy_eV": "number (eV)",
          "exothermicity_hydroxyl_transfer_Zn_eV": "number (eV)"
        }
      },
      "description": "DFT-computed reaction energies and migration barrier for oxygen transfer from graphene oxide functional groups to metallic Zn and to ZnO surface oxygen vacancies. The checker compares each numeric value against the hidden paper-reported reference values with field-specific tolerances."
    }
  ],
  "notes": "Only the listed fields are scored. Additional details may be present but are not checked."
}
```

## How you are scored
The submitted `dft_energetics.json` file is evaluated by a hidden verifier that compares each of the four numeric fields against reference values derived from the original DFT study. For each field, a score is awarded if the computed value lies within a pre‑defined tolerance range. The final reward is proportional to the number of fields that meet their respective tolerance criteria. The scoring is based solely on the accuracy of your computed energies; merely reporting values that match expected literature results is not sufficient — you must genuinely execute the DFT workflow.
