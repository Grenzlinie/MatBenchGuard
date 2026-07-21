# DFT Binding Energies of Li-S Species on Functionalized Carbon Models

## Problem background
Lithium-sulfur (Li-S) batteries suffer from low utilization of the sulfur cathode, partly because the non-polar carbon hosts commonly used to provide conductivity bind poorly to the polar lithium polysulfide (Li₂Sₙ, 1 ≤ n ≤ 8) discharge intermediates and the final lithium sulfide (Li₂S). A strategy to improve retention of these species is to introduce polar functional groups onto the carbon surface. This task investigates the effect of amine and amide surface groups on the interaction strength between a mesoporous carbon model and a range of sulfur species through density functional theory (DFT) calculations. You will quantify the binding energy (BE) between sulfur species and functionalized carbon surfaces and compare the results across different functional groups and bonding arrangements.

## Approach
Model the carbon surface as a C₅₄H₂₀ graphene fragment. Functionalize this fragment with three types of polar groups: ethylenediamine (EN), N,N-dimethylacetamide (DMA), and N,N,N',N'-tetramethylmalonamide (TMMA). For each functional group, prepare two bonding motifs to the carbon—face-bonded and edge-bonded—giving eight distinct surface models. For every combination of surface (4 variants × 2 motifs) and each of six sulfur species (S₈, Li₂S, Li₂S₂, Li₂S₄, Li₂S₆, Li₂S₈), place the sulfur species in multiple initial orientations and perform geometry optimizations at the DFT level using the M06-2X functional with Grimme D3 dispersion correction. Refine all structures with a larger basis set. Compute the binding energy for each complex as the difference between the total energy of the optimized complex and the sum of the separately optimized surface and sulfur species energies, applying a correction for basis set superposition error (BSSE). The final result set consists of 48 binding energies covering all surface–sulfur combinations.

## Reproduction target
Produce a CSV file that contains the final BSSE‑corrected binding energy (in eV) for each of the 48 surface–sulfur combinations: four carbon surfaces (pristine CMK3, EN‑CMK3, DMA‑CMK3, TMMA‑CMK3), each in two bonding motifs (face and edge), for each of six sulfur species (S8, Li2S, Li2S2, Li2S4, Li2S6, Li2S8). The file must have columns `surface`, `bonding_motif`, `sulfur_species`, and `binding_energy_eV`, with one row per combination and a CSV header.

## Assets

- Quantum chemistry software (ORCA, Psi4, or PySCF)

## Workflow steps

### Step 1: Construct initial atomic geometries
- Role: process
- Action: Build the C54H20 carbon fragment and functionalize its surface with EN, DMA, TMMA for both face-bonded and edge-bonded motifs as described in the main text. Prepare starting conformers for each isolated sulfur species (S8, Li2S, Li2S2, Li2S4, Li2S6, Li2S8).
- Evidence: `/app/outputs/models_manifest.json`

### Step 2: DFT geometry optimization and total energy calculation
- Role: process
- Action: For each isolated surface, each isolated sulfur species, and each of the 48 carbon–sulfur complexes (4 surfaces × 2 bonding motifs × 6 sulfur species), place the sulfur species in at least 5 distinct starting orientations and perform geometry optimization using M06-2X functional with D3 dispersion correction. Pre-optimize with 6-31G(d) basis set, then refine with 6-311++G(d,p). Record total electronic energies for all optimized structures.
- Evidence: `/app/outputs/dft_energy_summary.json`

### Step 3: Compute binding energies and compile results
- Role: scored (load-bearing)
- Action: Calculate binding energies as BE = E_total_complex − E_surface − E_sulfur (each optimized separately), apply BSSE correction, and write a CSV with one row per combination. Columns: surface, bonding_motif, sulfur_species, binding_energy_eV (float).
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Header row: surface, bonding_motif, sulfur_species, binding_energy_eV. Data rows: surface (one of CMK3, EN-CMK3, DMA-CMK3, TMMA-CMK3), bonding_motif (face or edge), sulfur_species (one of S8, Li2S, Li2S2, Li2S4, Li2S6, Li2S8), binding_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing calculated binding energies for all 48 surface-sulfur combinations. The binding energies will be numerically compared to reference values derived from the original DFT study, with tolerance that accounts for implementation differences. The ordering trend across surfaces will also be verified.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `bonding_motif`, `sulfur_species`, `binding_energy_eV`
  - `units`:
    - `binding_energy_eV`: eV

Notes: The hidden gold comprises the binding energies reported in the paper's supplementary tables and the ordering trend described in the main text. The solver is expected to use an open-source quantum chemistry code supporting M06-2X/D3 and BSSE correction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "bonding_motif",
          "sulfur_species",
          "binding_energy_eV"
        ],
        "units": {
          "binding_energy_eV": "eV"
        }
      },
      "description": "CSV file containing calculated binding energies for all 48 surface-sulfur combinations. The binding energies will be numerically compared to reference values derived from the original DFT study, with tolerance that accounts for implementation differences. The ordering trend across surfaces will also be verified."
    }
  ],
  "notes": "The hidden gold comprises the binding energies reported in the paper's supplementary tables and the ordering trend described in the main text. The solver is expected to use an open-source quantum chemistry code supporting M06-2X/D3 and BSSE correction."
}
```

## How you are scored
A hidden verifier will read your submitted `binding_energies.csv` and independently score the result. First, the verifier confirms the file shape and column names. Then it compares each binding energy value to a hidden reference dataset. It also checks whether the average ordering of the binding energies among the four surface types (averaged across the sulfur species) matches the expected trend observed in the original DFT study. Numerical agreement with the reference (within a hidden tolerance) and preservation of the ordering both contribute to your score. The final reward is a weighted combination of these checks; reporting a number alone is not sufficient—the workflow steps must be executed to arrive at the submitted values.
