# Ripplocation–Vacancy Coupling in 2D WSe₂

## Problem background
Two-dimensional WSe₂ layers can develop structural deformations known as ripplocations when subjected to mechanical loading. Simultaneously, point defects such as Se vacancies are common in these materials and can influence their mechanical and electronic properties. Understanding how curvature and vacancy formation energies interact is important for defect engineering and for controlling growth of high-quality 2D WSe₂. The target of this task is to compute, using a reactive empirical potential (ReaxFF), the formation energies of pristine and Se-vacancy-containing ripplocations as a function of buckling height, and to determine whether a mechanochemical coupling exists between monolayer bending and vacancy formation.

## Approach
We use the published W/Se/H ReaxFF force field parameters to perform energy minimisations of various atomic models of a WSe₂ bilayer. The workflow constructs: (i) a flat, pristine bilayer (R0); (ii) four compressed ripplocation models (R1–R4) with increasing buckling heights; (iii) the corresponding defective models in which a Se vacancy is introduced on each layer (R0‑vac and R1‑vac to R4‑vac); and (iv) a flat monolayer with two isolated Se vacancies to study the two‑vacancy ripple energy. After relaxing all structures with LAMMPS (or an equivalent ReaxFF‑capable code), the bulk chemical potentials of bcc‑W and α‑Se are computed. From the relaxed total energies and these chemical potentials, formation energies are derived: the pristine ripplocation formation energy relative to R0, the vacancy formation energy in each defective ripplocation, and the defective‑ripplocation formation energy relative to R0‑vac. Finally, the buckling height Δh is extracted and the observed trends are summarised.

## Reproduction target
Produce two scored artifacts:
- `ripplocation_energies.json`: Contains the total energies and derived formation energies for all models, the chemical potentials used, and the two‑vacancy ripple energy. This file must follow the exact schema declared in the output contract.
- `trend_summary.txt`: A plain‑text table of buckling height vs. pristine ripplocation formation energy and vacancy formation energy, together with the computed two‑vacancy ripple energy and explicit statements describing the observed trends. The checker will verify that the reported energies and trends are internally consistent and conform to the expected behavior of the force field.

## Assets

- W/Se/H ReaxFF force field parameter file: 10.1021/acs.jpcc.0c09155
- LAMMPS: lammps
- Bulk α-Se crystal structure: https://materialsproject.org/materials/mp-443
- Bulk bcc-W crystal structure: https://materialsproject.org/materials/mp-91

## Workflow steps

### Step 1: Generate ripplocation and defect models
- Role: process
- Action: Construct all required atomic models: (a) flat pristine AB‑stacked WSe₂ bilayer R0 (24×1 unit cells, 15 Å vacuum); (b) four compressed ripplocation models R1–R4 by laterally compressing R0 along the zigzag direction by 21.9%, 33.6%, 40.1%, and 45.3%; (c) flat defective model R0‑vac with one Se vacancy on each layer; (d) defective ripplocations R1‑vac to R4‑vac by removing a pair of Se atoms from the concave region of highest curvature; (e) a flat monolayer with two isolated Se vacancies (one on top, one on bottom) for the two‑vacancy coupling case. Models must be ready for ReaxFF energy minimisation with periodic boundary conditions and vacuum.
- Evidence: `/app/outputs/model_generation.log`

### Step 2: ReaxFF energy minimisation of all models
- Role: process
- Action: For each model generated in step_01 (R0, R1–R4, R0‑vac, R1‑vac to R4‑vac, flat two‑vacancy monolayer), run geometry optimisation with the ReaxFF force field using LAMMPS (or an equivalent ReaxFF‑capable code). Converge forces to a stringent threshold and record the final total energy of each relaxed structure.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Compute bulk chemical potentials
- Role: process
- Action: Run a ReaxFF energy minimisation for bulk bcc‑W and bulk α‑Se to obtain the total energy per atom, μ_W and μ_Se. These will be used in the formation‑energy formulas.
- Evidence: `/app/outputs/chemical_potentials.log`

### Step 4: Compute formation energies and output results
- Role: scored (load-bearing)
- Action: From the relaxed total energies and the chemical potentials, compute the following quantities and write them to `ripplocation_energies.json`: (a) the energy of the flat monolayer with two isolated Se vacancies relative to the pristine flat monolayer; (b) for each pristine ripplocation R1–R4, the formation energy E_ripp^f relative to R0; (c) for each defective ripplocation R1‑vac to R4‑vac, the vacancy formation energy E_vac and the defective‑ripplocation formation energy E_ripp‑vac^f, both referenced to the flat defective R0‑vac; (d) the buckling height Δh of each ripplocation model. Include the chemical potentials used. The output must be a JSON object with keys `two_vacancy_ripple_energy`, `chemical_potentials`, and `models` containing the prescribed fields and units.
- Output file: `/app/outputs/ripplocation_energies.json`
- Format: json
- Contract: Object with: 'two_vacancy_ripple_energy' (float, eV); 'chemical_potentials' (object with 'mu_W' and 'mu_Se' in eV); 'models' (array of objects). Each model object: 'name' (string), 'type' ('pristine' or 'defective'), 'buckling_height' (float, Å, 0 for flat), 'total_energy' (float, eV), 'formation_energy_pristine' (float, eV, only for pristine models, reference R0), 'formation_energy_vacancy' (float, eV, only for defective models, reference R0‑vac), 'formation_energy_defective_ripplocation' (float, eV, only for defective models, reference R0‑vac).
- Scoring: scored by hidden verifier

### Step 5: Summarise mechanochemical coupling trends
- Role: scored
- Action: Write a plain‑text file `trend_summary.txt` that lists the buckling heights and the corresponding pristine ripplocation formation energies E_ripp^f and vacancy formation energies E_vac. Explicitly state the observed trends: (i) E_ripp^f increases monotonically with Δh, (ii) E_vac decreases monotonically with Δh, (iii) E_vac becomes negative at the highest Δh, (iv) the defective ripplocation total energy becomes lower than the pristine ripplocation total energy at large Δh. Also include the computed two‑vacancy ripple energy.
- Output file: `/app/outputs/trend_summary.txt`
- Format: txt
- Contract: Plain text. Should contain a table of Δh vs E_ripp^f and E_vac, the two‑vacancy ripple energy, and explicit statements that the trends specified above are reproduced.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ripplocation_energies.json`
- `/app/outputs/trend_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ripplocation_energies.json
- path: `/app/outputs/ripplocation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The computed raw total energies, derived formation energies for all ripplocation models, and the two‑vacancy ripple energy. The checker verifies that the formation energies follow the required monotonic trends and that the two‑vacancy ripple energy matches a hidden reference value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `two_vacancy_ripple_energy`: float (eV)
    - `chemical_potentials`: object with mu_W and mu_Se (eV)
    - `models`: array of objects {name, type, buckling_height (Å), total_energy (eV), formation_energy_pristine (eV) (pristine only), formation_energy_vacancy (eV) (defective only), formation_energy_defective_ripplocation (eV) (defective only)}

### trend_summary.txt
- path: `/app/outputs/trend_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A human‑readable summary that the checker audits to confirm the reported trends and consistency with the numerical JSON output.
- schema:
  - `type`: text
  - `required_content`: A table of buckling heights vs E_ripp^f and E_vac, the two‑vacancy ripple energy, and explicit statements that the four mechanochemical coupling trends hold.

Notes: The JSON file is the load‑bearing scored artifact; the checker will verify the monotonic trends and compare the two‑vacancy ripple energy to a hidden gold value (exact_match with tolerance). The plain‑text summary is scored structurally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ripplocation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "two_vacancy_ripple_energy": "float (eV)",
          "chemical_potentials": "object with mu_W and mu_Se (eV)",
          "models": "array of objects {name, type, buckling_height (Å), total_energy (eV), formation_energy_pristine (eV) (pristine only), formation_energy_vacancy (eV) (defective only), formation_energy_defective_ripplocation (eV) (defective only)}"
        }
      },
      "description": "The computed raw total energies, derived formation energies for all ripplocation models, and the two‑vacancy ripple energy. The checker verifies that the formation energies follow the required monotonic trends and that the two‑vacancy ripple energy matches a hidden reference value within a tolerance."
    },
    {
      "file": "trend_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required_content": "A table of buckling heights vs E_ripp^f and E_vac, the two‑vacancy ripple energy, and explicit statements that the four mechanochemical coupling trends hold."
      },
      "description": "A human‑readable summary that the checker audits to confirm the reported trends and consistency with the numerical JSON output."
    }
  ],
  "notes": "The JSON file is the load‑bearing scored artifact; the checker will verify the monotonic trends and compare the two‑vacancy ripple energy to a hidden gold value (exact_match with tolerance). The plain‑text summary is scored structurally."
}
```

## How you are scored
Each scored artifact is independently evaluated by a hidden verifier. For `ripplocation_energies.json`, the checker recomputes formation energies from the provided total energies and chemical potentials, then assesses whether the reported trends satisfy required structural relationships. The two‑vacancy ripple energy is compared to a hidden reference value within a tolerance. For `trend_summary.txt`, the checker confirms that the numerical values match those in the JSON file and that the stated trend observations are correct. Successful reproduction requires that the workflow steps are genuinely executed in order; merely reporting numbers, even if correct, is not sufficient. The final reward is a weighted combination of the scores from the individual stages.
