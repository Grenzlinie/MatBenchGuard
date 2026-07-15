# He migration energy and clustering in bcc W via DFT

## Problem background
Helium (He) can be introduced into tungsten (W) plasma-facing components in fusion reactors via transmutation and plasma irradiation. Understanding the migration properties and clustering tendency of He in body-centered-cubic (bcc) W is important for predicting phenomena such as He embrittlement and bubble formation. This task investigates, through first-principles density functional theory (DFT) calculations, the relative stability of He interstitial sites, the energy barrier for He diffusion, and the strength of He–He attractive interactions.

## Approach
The method uses periodic DFT to compute total energies of W supercells containing He atoms. By comparing the energies of a single He atom placed at different high-symmetry interstitial sites (tetrahedral and octahedral) with reference energies of perfect bulk W and an isolated He atom, formation energies are obtained. The diffusion barrier is estimated as the energy difference between the He atom at the saddle point (located on the bisector of two first-neighbour tetrahedral sites) and the He atom at the tetrahedral site. The binding energy of two He atoms is computed from the energy of a supercell containing the He pair in a specific near-neighbour configuration (configuration C, initial separation 0.612a) and the energies of separate single-He supercells. All calculations are to be carried out using an open-source plane-wave DFT code and GGA-PBE pseudopotentials, with a 54-atom bcc W supercell at the lattice constant 3.1741 Å.

## Reproduction target
Using your own DFT calculations, determine the formation energies (in eV) for He at the tetrahedral and octahedral interstitial sites in bcc W and report which site is more stable. Estimate the He migration energy by computing the energy difference between the saddle point and the tetrahedral site, and verify that it is below 0.10 eV. Compute the He–He binding energy for a pair initially placed in configuration C (initial separation 0.612a) and confirm that the binding is strong (at least 0.5 eV). Provide the results in the required JSON files (step_01_formation_energies.json, step_02_migration_energy.json, step_03_binding_energy.json).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT reference calculations for bulk W and isolated He
- Role: process
- Action: Compute the total energy per atom of bulk bcc W at lattice constant 3.1741 Å and the total energy of an isolated He atom in a large periodic cell using Quantum ESPRESSO with SSSP efficiency pseudopotentials.
- Evidence: `/app/outputs/ref_energies.json`

### Step 2: DFT He interstitial defect calculations
- Role: process
- Action: Construct a 54‑atom bcc W supercell at a=3.1741 Å, insert one He atom at the tetrahedral and octahedral interstitial sites, and run DFT total‑energy calculations with full atomic relaxation (lattice fixed) using Quantum ESPRESSO.
- Evidence: `/app/outputs/defect_energies.json`

### Step 3: Formation energy analysis
- Role: scored (load-bearing)
- Action: Calculate the formation energies ΔH_f = E(NW+He) – N·E(W) – E(He_isolated) using the reference energies from step s0 and the defect total energies from step s1. Write a JSON object with keys 'tetrahedral' and 'octahedral' (energies in eV).
- Output file: `/app/outputs/step_01_formation_energies.json`
- Format: json
- Contract: { "tetrahedral": <float in eV>, "octahedral": <float in eV> }
- Scoring: scored by hidden verifier

### Step 4: DFT saddle‑point calculation
- Role: process
- Action: Place a single He atom at the approximate saddle point (on the right bisector of two first‑neighbour tetrahedral sites, 0.504 lattice parameter from the octahedral site) in the 54‑atom supercell and compute the total energy with ionic relaxation.
- Evidence: `/app/outputs/saddle_energy.json`

### Step 5: Migration energy analysis
- Role: scored
- Action: Compute the He migration energy as E_saddle – E(tetrahedral), where E(tetrahedral) is the total energy of the He tetrahedral configuration from step s1. Write a JSON object with key 'migration_energy' (in eV).
- Output file: `/app/outputs/step_02_migration_energy.json`
- Format: json
- Contract: { "migration_energy": <float in eV> }
- Scoring: scored by hidden verifier

### Step 6: DFT He‑He pair calculation (configuration C)
- Role: process
- Action: In the same 54‑atom bcc W supercell, place two He atoms initially at tetrahedral sites corresponding to configuration C (initial separation 0.612a) and run a DFT total‑energy calculation with full ionic relaxation.
- Evidence: `/app/outputs/He_pair_C_energy.json`

### Step 7: He‑He binding energy analysis
- Role: scored
- Action: Calculate the He‑He binding energy using E_b = E(A1) + E(A2) – E(A1+A2) – E_ref, where E(A1) and E(A2) are the single‑He tetrahedral energies from step s1, E(A1+A2) is the pair energy from step s5, and E_ref is N·E(W) from step s0. Write a JSON object with key 'binding_energy_config_C' (in eV).
- Output file: `/app/outputs/step_03_binding_energy.json`
- Format: json
- Contract: { "binding_energy_config_C": <float in eV> }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.json`
- `/app/outputs/step_02_migration_energy.json`
- `/app/outputs/step_03_binding_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.json
- path: `/app/outputs/step_01_formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of He in tetrahedral and octahedral interstitial sites; the relative ordering (tetrahedral < octahedral) is the primary claim.
- schema:
  - `type`: object
  - `required`:
    - `tetrahedral`: float (eV)
    - `octahedral`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `tetrahedral`: eV
    - `octahedral`: eV

### step_02_migration_energy.json
- path: `/app/outputs/step_02_migration_energy.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: He migration energy; must be positive and not exceed the very low threshold claimed in the paper.
- schema:
  - `type`: object
  - `required`:
    - `migration_energy`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `migration_energy`: eV

### step_03_binding_energy.json
- path: `/app/outputs/step_03_binding_energy.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: He‑He binding energy for configuration C; must exceed the large‑binding threshold that supports strong clustering.
- schema:
  - `type`: object
  - `required`:
    - `binding_energy_config_C`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `binding_energy_config_C`: eV

Notes: The task uses Quantum ESPRESSO (open‑source) with SSSP PBE pseudopotentials as a replacement for the originally used VASP. Tolerances are set to accommodate differences due to code and pseudopotential variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "tetrahedral": "float (eV)",
          "octahedral": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "tetrahedral": "eV",
          "octahedral": "eV"
        }
      },
      "description": "Formation energies of He in tetrahedral and octahedral interstitial sites; the relative ordering (tetrahedral < octahedral) is the primary claim."
    },
    {
      "file": "step_02_migration_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "migration_energy": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "migration_energy": "eV"
        }
      },
      "description": "He migration energy; must be positive and not exceed the very low threshold claimed in the paper."
    },
    {
      "file": "step_03_binding_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "binding_energy_config_C": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "binding_energy_config_C": "eV"
        }
      },
      "description": "He‑He binding energy for configuration C; must exceed the large‑binding threshold that supports strong clustering."
    }
  ],
  "notes": "The task uses Quantum ESPRESSO (open‑source) with SSSP PBE pseudopotentials as a replacement for the originally used VASP. Tolerances are set to accommodate differences due to code and pseudopotential variations."
}
```

## How you are scored
Each scored artifact is independently checked by a hidden verifier. The verifier first inspects the structural format of each JSON file, then evaluates the computed values against predefined tolerances and criteria (e.g., ordering, threshold crossing). The three scored files carry weights that are combined into a final reward between 0 and 1. Simply reporting the paper’s numeric results is not sufficient; the verifier expects values that are consistent with a correctly executed DFT workflow using the specified setup.
