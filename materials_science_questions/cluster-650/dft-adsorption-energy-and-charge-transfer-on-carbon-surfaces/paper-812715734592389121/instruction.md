# DFT Calculations of Li Decoration and Hydrogen Storage on Reduced Graphene Oxides

## Problem background
Hydrogen is a promising clean energy carrier, but on-board reversible storage at ambient temperature remains challenging. Carbon nanomaterials offer lightweight scaffolds; however, pristine carbon binds H₂ too weakly for practical use. Introducing oxygen functional groups and decorating with light alkali metals can enhance H₂ adsorption. This task investigates the hydrogen storage properties of Li-decorated reduced graphene oxides (RGO) containing epoxy (-O) and hydroxyl (-OH) groups. The objective is to compute, using density functional theory (DFT), the binding energies of Li atoms and Li-containing clusters on graphene, the corresponding structural parameters, and the adsorption energies and capacities of H₂ on the decorated surfaces at different oxidation degrees. The computed quantities will determine whether such systems can achieve high gravimetric storage capacity with moderate adsorption energies suitable for reversible ambient-temperature hydrogen storage.

## Approach
The reproduction uses an open-source plane-wave DFT code that supports the PBE functional, PAW pseudopotentials, and the Grimme D2 van der Waals dispersion correction. Models are built as 4×4 graphene supercells with varying numbers of epoxy or hydroxyl groups. Geometry optimizations are performed for isolated graphene and functional-group systems, then Li atoms are placed near the O-containing groups to form clusters. Total energies and relaxed geometries are extracted, from which average binding energies of Li atoms and clusters are computed following standard energy difference definitions. To assess hydrogen storage, H₂ molecules are added near the decorated Li clusters and the systems are re-optimized; the average adsorption energy per H₂ and the gravimetric hydrogen storage capacity (wt%) are calculated. The workflow spans a sequence of configurations: a single Li on pristine graphene; LiₙO (n=1–4) on a single-epoxy supercell; LiₘOH (m=1–3) on a single-hydroxyl supercell; multi-cluster decorations at O/C ratios 1/16 and 1/8; and H₂ adsorption on Li₄O, Li₃OH, and the multi-cluster arrangements. All calculations are carried out with the same level of theory, and results are collected in the final artifact.

## Reproduction target
Using DFT calculations as described, compute the following quantities and write them to a single JSON file (`results.json`):

- Binding energy of a single Li atom on a pristine 4×4 graphene supercell.
- For graphene with a single epoxy O (O/C = 1/32): optimized vertical distances of O and Li from the graphene plane, O–Li bond lengths, average Li binding energy, and cluster binding energy for LiₙO clusters with n = 1, 2, 3, 4.
- For graphene with a single hydroxyl group (O/C = 1/32): analogous quantities for LiₘOH clusters with m = 1, 2, 3.
- Average H₂ adsorption energy per H₂ on a Li₄O-decorated supercell for 3, 6, and 9 H₂ molecules, and on a Li₃OH-decorated supercell for 3 and 6 H₂ molecules.
- Average binding energies of Li atoms and clusters in multi-cluster configurations: C1 (one Li₄O + one Li₃OH at O/C = 1/16), C2 (two Li₄O + two Li₃OH at O/C = 1/8), and C3 (four Li₄O at O/C = 1/8).
- Average H₂ adsorption energy and gravimetric hydrogen storage capacity (wt%) for each multi-cluster system when loaded with the maximum number of H₂ molecules (15 for C1, 26 for C2, 32 for C3).

All values must be obtained from the DFT optimizations and structured according to the output contract.

## Assets

- Open-source DFT code with PAW method (e.g., GPAW): https://wiki.fysik.dtu.dk/gpaw/

## Workflow steps

### Step 1: Construct structural models
- Role: process
- Action: Build 4×4 supercells of pristine graphene, graphene with a single epoxy O (O/C=1/32), graphene with a single hydroxyl OH (O/C=1/32), and multi-cluster RGO models at O/C=1/16 (configuration C1) and O/C=1/8 (configurations C2, C3) as described. Generate input files for DFT calculations.
- Evidence: `/app/outputs/structures.json`

### Step 2: Single Li on pure graphene
- Role: process
- Action: Perform DFT geometry optimization of a single Li atom on the pristine 4×4 graphene supercell. Compute the binding energy relative to isolated Li and graphene.
- Evidence: `/app/outputs/Li_pure_graphene.log`

### Step 3: Li_nO clusters on epoxy-graphene
- Role: process
- Action: For the supercell with one epoxy O, place n Li atoms (n=1,2,3,4) near the O atom and optimize geometries. Record vertical distances of O and Li from graphene, O-Li bond lengths, and compute the average binding energy per Li and the cluster binding energy.
- Evidence: `/app/outputs/Li_nO_optimizations.log`

### Step 4: Li_mOH clusters on hydroxyl-graphene
- Role: process
- Action: For the supercell with one OH group, place m Li atoms (m=1,2,3) and optimize geometries. Record vertical distances, O-Li bond lengths, and compute average Li binding energy and cluster binding energy.
- Evidence: `/app/outputs/Li_mOH_optimizations.log`

### Step 5: H₂ adsorption on Li₄O cluster
- Role: process
- Action: Using the optimized Li₄O-decorated graphene, adsorb 3, 6, and 9 H₂ molecules and optimize geometries. Compute the average adsorption energy per H₂ for each coverage.
- Evidence: `/app/outputs/H2_Li4O.log`

### Step 6: H₂ adsorption on Li₃OH cluster
- Role: process
- Action: Using the optimized Li₃OH-decorated graphene, adsorb 3 and 6 H₂ molecules and optimize geometries. Compute the average adsorption energy per H₂.
- Evidence: `/app/outputs/H2_Li3OH.log`

### Step 7: Multi-cluster Li decoration at O/C=1/16 and 1/8
- Role: process
- Action: Build and optimize the configurations C1 (Li₄O+Li₃OH, O/C=1/16), C2 (2 Li₄O+2 Li₃OH, O/C=1/8), and C3 (4 Li₄O, O/C=1/8) as described. Compute average binding energy of Li atoms and clusters for each.
- Evidence: `/app/outputs/multi_cluster_decorations.log`

### Step 8: H₂ adsorption on multi-cluster systems
- Role: process
- Action: Adsorb the maximum number of H₂ molecules on the optimized C1, C2, C3 configurations (15, 26, 32 H₂ respectively) and optimize. Compute the average H₂ adsorption energy and gravimetric hydrogen storage capacity (wt%) for each.
- Evidence: `/app/outputs/H2_multi_cluster.log`

### Step 9: Compile numerical results
- Role: scored (load-bearing)
- Action: Collect all computed quantities from steps 02–08 and write them into results.json following the schema: binding energy of Li on pure graphene; structural parameters (vertical distances, O-Li bond lengths) and binding energies for Li_nO (n=1-4) and Li_mOH (m=1-3); H₂ adsorption energies for Li₄O and Li₃OH; multi-cluster binding energies; H₂ adsorption energies and storage capacities for C1, C2, C3.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: See output_contract.
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
- target_policy: reference_match
- description: All main numerical quantities computed by the DFT workflow. The hidden checker compares each value to paper-reported reference values within tolerances (energies: ±0.2 eV, distances: ±0.2 Å, HSC: ±0.5 wt%).
- schema:
  - `type`: object
  - `required`:
    - `binding_energy_Li_on_pure_graphene`: float (eV)
    - `Li_nO`: array of objects
    - `Li_mOH`: array of objects
    - `binding_energies_O_C_ratios`: array of objects
    - `H2_adsorption_Li4O`: array of objects
    - `H2_adsorption_Li3OH`: array of objects
    - `HSC_adsorption`: array of objects
  - `items`:
    - `Li_nO_item`:
      - `n`: int
      - `d_O_graphene`: float (Å)
      - `d_Li_graphene`: float or [float,float] (Å) for n=4
      - `d_O_Li`: float or [float,float] (Å) for n=4
      - `E_b_Li`: float (eV)
      - `E_b_cluster`: float (eV)
    - `Li_mOH_item`:
      - `m`: int
      - `d_O_graphene`: float (Å)
      - `d_Li_graphene`: float (Å)
      - `d_O_Li`: float (Å)
      - `E_b_Li`: float (eV)
      - `E_b_cluster`: float (eV)
    - `binding_energies_O_C_ratios_item`:
      - `config`: str (e.g., C1, C2, C3)
      - `E_b_Li`: float (eV)
      - `E_b_cluster`: float (eV)
    - `H2_adsorption_item`:
      - `n_H2`: int
      - `E_ad`: float (eV/H2)
    - `HSC_adsorption_item`:
      - `system`: str (C1, C2, C3)
      - `E_ad`: float (eV/H2)
      - `HSC_wt`: float (wt%)

Notes: The agent must compute all values using an open-source DFT implementation that matches the paper's level of theory (PBE functional, PAW method, D2 dispersion correction, 500 eV plane-wave cutoff, 5×5×1 k-point mesh, 20 Å vacuum). Structural parameters and energies are obtained from geometry optimizations with forces converged below 0.01 eV/Å. The results.json must contain the listed fields populated from the computations.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "binding_energy_Li_on_pure_graphene": "float (eV)",
          "Li_nO": "array of objects",
          "Li_mOH": "array of objects",
          "binding_energies_O_C_ratios": "array of objects",
          "H2_adsorption_Li4O": "array of objects",
          "H2_adsorption_Li3OH": "array of objects",
          "HSC_adsorption": "array of objects"
        },
        "items": {
          "Li_nO_item": {
            "n": "int",
            "d_O_graphene": "float (Å)",
            "d_Li_graphene": "float or [float,float] (Å) for n=4",
            "d_O_Li": "float or [float,float] (Å) for n=4",
            "E_b_Li": "float (eV)",
            "E_b_cluster": "float (eV)"
          },
          "Li_mOH_item": {
            "m": "int",
            "d_O_graphene": "float (Å)",
            "d_Li_graphene": "float (Å)",
            "d_O_Li": "float (Å)",
            "E_b_Li": "float (eV)",
            "E_b_cluster": "float (eV)"
          },
          "binding_energies_O_C_ratios_item": {
            "config": "str (e.g., C1, C2, C3)",
            "E_b_Li": "float (eV)",
            "E_b_cluster": "float (eV)"
          },
          "H2_adsorption_item": {
            "n_H2": "int",
            "E_ad": "float (eV/H2)"
          },
          "HSC_adsorption_item": {
            "system": "str (C1, C2, C3)",
            "E_ad": "float (eV/H2)",
            "HSC_wt": "float (wt%)"
          }
        }
      },
      "description": "All main numerical quantities computed by the DFT workflow. The hidden checker compares each value to paper-reported reference values within tolerances (energies: ±0.2 eV, distances: ±0.2 Å, HSC: ±0.5 wt%)."
    }
  ],
  "notes": "The agent must compute all values using an open-source DFT implementation that matches the paper's level of theory (PBE functional, PAW method, D2 dispersion correction, 500 eV plane-wave cutoff, 5×5×1 k-point mesh, 20 Å vacuum). Structural parameters and energies are obtained from geometry optimizations with forces converged below 0.01 eV/Å. The results.json must contain the listed fields populated from the computations."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json`. For each numerical field required by the output contract, it compares your computed value to a hidden reference value using predefined tolerances. The reward is the fraction of individual comparisons that pass—i.e., the proportion of fields whose difference from the reference falls within the allowed tolerance. Structural and energy fields are checked separately, each contributing to the total score. The verifier also confirms that the file contains all required keys and types. Intermediate process-step evidence files (structures and log files) are not directly scored but must be produced to document that the workflow steps were executed. The final reward is a float between 0 and 1.
