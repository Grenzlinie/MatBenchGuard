# DFT+U Study of Ceria Stepped Surface Electronic Structure

## Problem background
Cerium oxide (ceria) surfaces play a central role in catalysis, energy storage, and sensing, largely because of the facile Ce⁴⁺ ↔ Ce³⁺ redox interconversion that accompanies oxygen release or uptake. Stepped surfaces are especially interesting because the reduced coordination of atoms at step edges may stabilize Ce³⁺, yet the electronic structure of these sites remains debated: whether Ce³⁺ can exist in stoichiometric extended samples, and how oxygen vacancies on stepped surfaces influence the oxidation state of Ce atoms, are open questions. This task addresses those questions by determining the atomic and electronic structure of a series of CeO₂(111) slab models representing perfect terraces, reduced terraces, stepped surfaces, and stepped surfaces with oxygen vacancies. The electronic descriptors—Bader charges (a spatial partitioning of the charge density), atomic magnetic moments, and electron localization function (ELF) maps—are used to assign oxidation states and to reveal how coordination number and local stoichiometry affect the Ce redox state.

## Approach
The study employs periodic density functional theory (DFT) with the Dudarev DFT+U approach to treat the strong localization of Ce 4f electrons. Geometry optimizations are performed using the local density approximation plus U (LDA+U, with the VWN exchange-correlation functional and an effective Hubbard U_eff=5 eV), while the final electronic structure analysis (total energies, magnetic moments, charge density) is carried out with the generalized gradient approximation plus U (GGA+U, with the PW91 functional and U_eff=3 eV). This two-step protocol—LDA+U for structure, GGA+U for electronic properties—provides a balanced description of both oxidized Ce⁴⁺ and reduced Ce³⁺ ions.

All calculations are performed on periodic slab models of the CeO₂(111) surface, built from the bulk fluorite structure. The models include:
- Terrace models: a perfect stoichiometric (111) surface (T1), a fully reduced Ce-terminated surface (T2), and a missing-row partially reduced surface (T3).
- Stepped models: four different step geometries (S1–S4) that preserve overall CeO₂ stoichiometry but introduce low-coordinated Ce sites.
- Step+vacancy models: three models (SV1–SV3) combining a step with oxygen vacancies of varying concentration; SV1 is formally stoichiometric while SV2 and SV3 are nonstoichiometric.

For each model, the Bader charge analysis and atomic magnetic moments are extracted from the self-consistent GGA+U charge density and wavefunctions, enabling a quantitative assignment of Ce oxidation states. ELF maps are generated as supporting visualization. Total energies are used to compute formation energies per Ce atom, taking isolated Ce and O₂ as references.

## Reproduction target
Your goal is to execute the described DFT+U workflow on all ten slab models (T1, T2, T3; S1, S2, S3, S4; SV1, SV2, SV3) and to deliver the following scored artifacts:

1. A JSON file (`/app/outputs/results.json`) containing, for every slab model:
   - The total energy per CeO₂ unit (for stoichiometric models) and the formation energy per Ce atom.
   - For all atoms in the simulation cell, the element, Bader charge (in units of e), and atomic magnetic moment (in μ_B).
   The file structure and keys are specified in the output contract below.

2. A tar.gz archive (`/app/outputs/elf_cube_files.tar.gz`) containing an ELF cube file for each slab model, named `<model>.cube` (e.g., `T1.cube`, `S4.cube`, `SV2.cube`).

The computed values must be derived from the LDA+U relaxed geometries and the GGA+U single-point charge densities, as described in the workflow steps. The reference energies for Ce and O₂ needed for formation energies are to be computed with the same GGA+U settings.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Henkelman Bader charge analysis code: https://theory.cm.utexas.edu/henkelman/code/bader/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Bulk CeO2 lattice constant optimization with LDA+U
- Role: process
- Action: Perform LDA+U (VWN, Ueff=5 eV) geometry optimization of bulk cubic CeO2 (fluorite structure) using Quantum ESPRESSO to determine the equilibrium lattice constant a0.
- Evidence: `/app/outputs/bulk_opt.log`

### Step 2: Construction of slab surface models
- Role: process
- Action: Generate initial atomic coordinates for all terrace (T1, T2, T3), stepped (S1, S2, S3, S4) and step+vacancy (SV1, SV2, SV3) slab models using the optimized lattice constant a0, appropriate supercell dimensions, and a vacuum gap of about 12 Å.
- Evidence: `/app/outputs/slab_coords.tar.gz`

### Step 3: LDA+U geometry relaxation of all slab models
- Role: process
- Action: Relax atomic positions of all slab models using LDA+U (VWN, Ueff=5 eV), spin-restricted, until forces and energies converge; save the final optimized geometries.
- Evidence: `/app/outputs/relaxed_geometries.tar.gz`

### Step 4: Reference energy calculations for Ce and O2
- Role: process
- Action: Compute the total energy of an isolated Ce atom (spin-polarized) and an O2 molecule (triplet) using GGA+U (PW91, Ueff=3 eV) with the same pseudopotentials as the slab calculations; these energies serve as references for formation energies.
- Evidence: `/app/outputs/ref_energies.log`

### Step 5: GGA+U single-point evaluation of energies, magnetic moments and charge density
- Role: process
- Action: For all slab models, perform spin-polarized GGA+U (PW91, Ueff=3 eV) single-point calculations on the LDA+U relaxed geometries; save total energies, atomic magnetic moments, and the self-consistent charge density in cube format for Bader and ELF post-processing.
- Evidence: `/app/outputs/gga_u_outputs.tar.gz`

### Step 6: Post-process: Bader charges, formation energies and results assembly
- Role: scored (load-bearing)
- Action: For each slab model: (a) run the Henkelman Bader code on the GGA+U charge density to obtain per-atom Bader charges; (b) compute total energy per CeO2 unit (where stoichiometric) and formation energy per Ce atom using the Ce and O2 reference energies; (c) collect atomic magnetic moments from the DFT output. Assemble all data into a single JSON file (results.json) with per-atom details for every model.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level key 'models' (list). Each model object has keys: 'name' (string, e.g. 'T1', 'S4', 'SV2'), 'energy_per_CeO2' (float or null, units eV), 'formation_energy_per_Ce' (float, eV), and 'atoms' (list of per-atom objects). Each atom object has keys: 'element' (string), 'bader_charge' (float, units e), 'magnetic_moment' (float, units μ_B). The 'atoms' list must contain every atom in the simulation cell for all models. 'energy_per_CeO2' can be null for nonstoichiometric models.
- Scoring: scored by hidden verifier

### Step 7: Generate ELF maps as supporting evidence
- Role: scored
- Action: Compute the electron localization function (ELF) from the GGA+U charge density for each slab model using Quantum ESPRESSO's pp.x, and export the results as cube files. Bundle all cube files into a tar.gz archive named elf_cube_files.tar.gz, with one .cube file per model named after the model (e.g., T1.cube).
- Output file: `/app/outputs/elf_cube_files.tar.gz`
- Format: other
- Contract: tar.gz archive containing at least one .cube file per model, named <model>.cube (e.g., T1.cube, S4.cube, SV2.cube). The archive is checked for validity and presence of cube files.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/elf_cube_files.tar.gz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Reproduced Bader charges, magnetic moments, and formation energies for all ceria slab models.
- schema:
  - `type`: object
  - `required`:
    - `models`: list of model objects (see description)
  - `description`: Each model object: { 'name': string, 'energy_per_CeO2': float or null (eV), 'formation_energy_per_Ce': float (eV), 'atoms': [ { 'element': string, 'bader_charge': float (e), 'magnetic_moment': float (μ_B) } ] }. The 'atoms' array must contain all atoms in the simulation cell for every model.

### elf_cube_files.tar.gz
- path: `/app/outputs/elf_cube_files.tar.gz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Electron localization function cube files for all slab models, bundled as a tar.gz archive.
- schema:
  - `type`: archive
  - `required`:
    - `archive`: valid tar.gz file
  - `items`: `T1.cube`, `T2.cube`, `T3.cube`, `S1.cube`, `S2.cube`, `S3.cube`, `S4.cube`, `SV1.cube`, `SV2.cube`, `SV3.cube`
  - `notes`: List of expected cube files; all must be present inside the archive.

Notes: All reported quantities must be derived from the specified DFT+U workflow using Quantum ESPRESSO and the Henkelman Bader code. The checker will recompute deviations from hidden reference values and verify formation energy trends across models.

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
        "required": {
          "models": "list of model objects (see description)"
        },
        "description": "Each model object: { 'name': string, 'energy_per_CeO2': float or null (eV), 'formation_energy_per_Ce': float (eV), 'atoms': [ { 'element': string, 'bader_charge': float (e), 'magnetic_moment': float (μ_B) } ] }. The 'atoms' array must contain all atoms in the simulation cell for every model."
      },
      "description": "Reproduced Bader charges, magnetic moments, and formation energies for all ceria slab models."
    },
    {
      "file": "elf_cube_files.tar.gz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "archive",
        "required": {
          "archive": "valid tar.gz file"
        },
        "items": [
          "T1.cube",
          "T2.cube",
          "T3.cube",
          "S1.cube",
          "S2.cube",
          "S3.cube",
          "S4.cube",
          "SV1.cube",
          "SV2.cube",
          "SV3.cube"
        ],
        "notes": "List of expected cube files; all must be present inside the archive."
      },
      "description": "Electron localization function cube files for all slab models, bundled as a tar.gz archive."
    }
  ],
  "notes": "All reported quantities must be derived from the specified DFT+U workflow using Quantum ESPRESSO and the Henkelman Bader code. The checker will recompute deviations from hidden reference values and verify formation energy trends across models."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects your output files and compares them against predetermined expectations. The verifier carries out several independent checks, each assigned a weight that contributes to the final reward (a number between 0 and 1). The key checks are:

- **Bader charges and magnetic moments**: For selected key slab models, the verifier compares the atomic Bader charges and magnetic moments you report for Ce atoms against hidden reference values (derived from the same DFT+U protocol). The comparison allows for typical numerical spread between independent implementations.
- **Formation energy trends**: The verifier checks the relative ordering of formation energies across all models. Even if absolute values differ, a correct reproduction preserves the trend found in the original study.
- **ELF cube files**: The verifier confirms that the `elf_cube_files.tar.gz` archive exists, is a valid tar.gz, and contains the required cube files.
- **Structural consistency**: The verifier cross-checks that nonzero magnetic moments appear only on atoms with Bader charges below a certain threshold, reflecting the physical expectation that only Ce atoms with significant 3+ character carry a local moment.

Simply writing numbers that match a published table without executing the DFT workflow will not satisfy the structural and trend checks, because the verifier looks at per-atom values, the internal consistency of your data, and the overall quality of the computed electronic structure. The final score is a weighted combination of all checks.
