# DFT Defect Formation Energy Calculations in D03-Fe3Al

## Problem background
The intermetallic compound D03-Fe3Al exhibits a complex defect chemistry that controls thermal vacancy concentrations, sublattice preference, and diffusion mechanisms at high temperatures. Understanding which crystallographic sublattice hosts the lowest-energy vacancies and whether structural (athermal) vacancies exist is crucial for predicting the material's behavior. This task computes the effective formation energies of atomic point defects in D03-Fe3Al using ab-initio density functional theory (DFT) combined with a grand-canonical statistical formalism. The energies determine the equilibrium defect populations and reveal the dominant defect types near the stoichiometric composition.

## Approach
The approach combines first-principles DFT calculations with a grand-canonical statistical treatment of defects. First, construct a 16-atom supercell representing the ordered D03 structure and create supercells containing a single defect of each type (Fe vacancy on the α sublattice, Fe vacancy on the γ sublattice, Al vacancy, Fe antisite on Al, Al antisite on Fe γ, Al antisite on Fe α). Perform DFT structural relaxations (ionic positions only) to obtain the total energy of each configuration. Then compute the bare defect formation energies from the relaxed total energies. Next, apply the grand-canonical formalism: define grand-canonical excitations for each defect, write the grand-canonical potential J as a function of defect concentrations and chemical potentials, minimize J at fixed temperature and volume, and determine the chemical potentials from the conditions J=0 and the stoichiometric composition x=75. Neglect defect formation entropies and volume changes. The formalism yields temperature-independent effective formation energies for each defect type, which are the final output quantities. The DFT engine is an open-source plane-wave pseudopotential code such as Quantum ESPRESSO; spin polarization is neglected, consistent with the small magnetic effects reported for similar systems.

## Reproduction target
Produce a CSV file containing the effective formation energies (in eV) for the six defect types in D03-Fe3Al at the stoichiometric composition x=75, derived from DFT relaxations of a 16-atom supercell via the grand-canonical formalism. The file must have columns 'defect' and 'E_eff'. The defect names are: Fe_vac_alpha, Fe_vac_gamma, Al_vac, Fe_anti_Al, Al_anti_gamma, Al_anti_alpha. The energies are the temperature-independent effective formation energies after minimizing J and enforcing the composition constraint.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Fe and Al (e.g., PBE family from SSSP): https://www.materialscloud.org/discover/sssp/table
- D03-Fe3Al crystal structure (16-atom supercell geometry)

## Workflow steps

### Step 1: DFT structural relaxation of defect supercells
- Role: process
- Action: Construct the 16-atom D03-Fe3Al supercell for the perfect crystal and for six defect configurations: Fe vacancy on α sublattice, Fe vacancy on γ sublattice, Al vacancy, Fe antisite on Al site, Al antisite on Fe γ site, Al antisite on Fe α site. Perform DFT structural relaxation (ionic positions) to obtain the relaxed total energy for each configuration. Record the relaxed energies and geometries.
- Evidence: `/app/outputs/relaxation_output.log`

### Step 2: Derive effective formation energies via grand-canonical formalism
- Role: scored (load-bearing)
- Action: From the relaxed total energies of the perfect and defect supercells, compute defect formation energies. Then apply the grand-canonical statistical method (neglecting entropies and relaxing the chemical potentials to satisfy J=0 and the stoichiometric composition) to obtain the temperature-independent effective formation energies for the six defects. Output a CSV with columns 'defect' (name) and 'E_eff' (eV).
- Output file: `/app/outputs/effective_formation_energies.csv`
- Format: csv
- Contract: Header: defect, E_eff. defect values: Fe_vac_alpha, Fe_vac_gamma, Al_vac, Fe_anti_Al, Al_anti_gamma, Al_anti_alpha. E_eff is a floating-point number in electronvolts.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_formation_energies.csv
- path: `/app/outputs/effective_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective formation energies for six defect types in D03-Fe3Al at stoichiometric composition x=75, computed from the relaxed N=16 supercell via the grand-canonical formalism. Contains rows for Fe_vac_alpha, Fe_vac_gamma, Al_vac, Fe_anti_Al, Al_anti_gamma, Al_anti_alpha.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `E_eff`
  - `units`:
    - `E_eff`: eV

Notes: The scored artifact is the CSV of effective formation energies. The checker will compare each defect's E_eff value to the paper-reported gold within a tolerance and verify the ordering Fe_vac_alpha < Al_vac < Fe_vac_gamma.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "E_eff"
        ],
        "units": {
          "E_eff": "eV"
        }
      },
      "description": "Effective formation energies for six defect types in D03-Fe3Al at stoichiometric composition x=75, computed from the relaxed N=16 supercell via the grand-canonical formalism. Contains rows for Fe_vac_alpha, Fe_vac_gamma, Al_vac, Fe_anti_Al, Al_anti_gamma, Al_anti_alpha."
    }
  ],
  "notes": "The scored artifact is the CSV of effective formation energies. The checker will compare each defect's E_eff value to the paper-reported gold within a tolerance and verify the ordering Fe_vac_alpha < Al_vac < Fe_vac_gamma."
}
```

## How you are scored
A hidden verifier reads your effective_formation_energies.csv. It compares each defect's E_eff value to a hidden gold reference using an appropriate tolerance and verifies a required ordering among the three vacancy defects (Fe vacancy on the α sublattice, Al vacancy, and Fe vacancy on the γ sublattice). Full credit is awarded if all values fall within the tolerance and the ordering is satisfied. Partial credit may be given for partially correct matches. Reproducing the exact steps and submitting the resulting energies is essential; reporting numbers without the underlying computation will not suffice.
