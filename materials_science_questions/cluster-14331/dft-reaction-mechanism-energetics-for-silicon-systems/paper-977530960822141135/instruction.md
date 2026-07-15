# DFT Thermodynamic Profile for Fe-Catalyzed H/D Exchange in Hydrosilanes

## Problem background
Transition-metal-catalysed H/D exchange in hydrosilanes is an atom-efficient route to deuterated silanes, which are valuable reagents and mechanistic probes. Iron-based catalysts are attractive because of the metal’s abundance and low toxicity. The present work investigates iron(I) and iron(II) complexes supported by an amido-imidazolin-2-imine ligand as precatalysts for this transformation. Experimental studies point to two possible catalytic cycles: one proceeding via iron deuteride/hydride intermediates (pathway I), and an alternative via iron-silyl intermediates (pathway II). To assess which cycle is thermodynamically more feasible, the mechanism was studied computationally using density functional theory (DFT). Your task is to reproduce the DFT-derived thermodynamic profile of the key catalytic steps and, from the computed Gibbs free energies, determine whether pathway I or II is the more viable route under the conditions studied.

## Approach
The approach employs quantum-chemical calculations to build and evaluate the reaction energy landscape. Starting from crystallographic coordinates of related complexes, you will construct molecular models of the critical intermediates along both pathways: the iron deuteride catalyst (FeD), its adduct with diphenylsilane (FeD·S), a cyclic activated complex (AC), the iron hydride (FeH), the iron-silyl species (FeSi), the FeSi·HD adduct, and the ACD2 complex. All species are treated as neutral, quintet-spin (S=2) systems. Geometry optimizations and vibrational frequency calculations will be performed with the ORCA package using the B3LYP functional, the def2-SVP basis set, and the D3BJ dispersion correction. The resulting Gibbs free energies at 298.15 K will be referenced to the separated reactants (FeD + Ph₂SiH₂) to obtain a relative free energy profile. By comparing the ΔG values for the FeD→FeH transformation (pathway I) and the FeD→FeSi transformation (pathway II), the thermodynamic viability of the two catalytic routes can be assessed.

## Reproduction target
Your objective is to deliver three scored artefacts: (1) an XYZ file `optimized_structures.xyz` containing the final optimized Cartesian coordinates of all key intermediates (FeD, FeD·S, AC, FeH, FeSi, FeSi·HD, ACD2); (2) a CSV file `gibbs_free_energies.csv` reporting the absolute total Gibbs free energy (in Hartree) and the relative ΔG (in kcal/mol) for each species; (3) a plain-text file `conclusion.txt` that states, based on your computed energies, which catalytic pathway (I or II) is thermodynamically more favorable, and reports the computed ΔG values for the FeD→FeH and FeD→FeSi steps. All outputs must be written to `/app/outputs`.

## Assets

- Crystallographic CIF files for complexes 3–11
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/app.php/portal
- Def2-SVP basis set: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Build molecular models from crystal structures
- Role: process
- Action: Use the provided CIF files for complexes 3–11 to construct initial geometries of the catalytic intermediates (FeD, FeD·S, AC, FeH, FeSi, FeSi·HD, ACD2) with the AmIm-iron fragment. Replace/add hydrogens/deuterium where needed and set correct charge/multiplicity (all species are neutral, quintet spin state S=2). Prepare ORCA input files for geometry optimization and vibrational frequency analysis.
- Evidence: `/app/outputs/orca_input_files.tar.gz`

### Step 2: DFT geometry optimization and frequency calculations
- Role: scored (load-bearing)
- Action: Perform geometry optimization and vibrational frequency calculations for all catalytic intermediates (FeD, FeD·S, AC, FeH, FeSi, FeSi·HD, ACD2) using ORCA at the B3LYP/def2-SVP level with D3BJ dispersion correction (all species in the quintet spin state S=2). Save the final optimized Cartesian coordinates of each species in XYZ format to `optimized_structures.xyz`.
- Output file: `/app/outputs/optimized_structures.xyz`
- Format: other
- Contract: Standard XYZ format: first line number of atoms, second line comment (species name, charge, spin multiplicity), then lines with element symbol and x y z coordinates in Å.
- Scoring: scored by hidden verifier

### Step 3: Potential energy surface scan for activated complex
- Role: process
- Action: Perform linear-transit and quadratic-transit PES scans using the optimized structures of FeD·S and AC to determine the energy profile for formation of the activated complex. Calculate the barrier height for AC formation and confirm that AC is a local minimum via vibrational analysis.
- Evidence: `/app/outputs/pes_scan_summary.txt`

### Step 4: Compile Gibbs free energies and relative profile
- Role: scored
- Action: Extract the total Gibbs free energy (electronic energy + thermal correction) at 298.15 K for each intermediate from the ORCA output files of step 02. Compute the relative ΔG (in kcal/mol) with respect to the reactant state FeD + Ph2SiH2 (set to 0.0). Write a CSV file containing the absolute total Gibbs free energy (in Hartree) and the relative ΔG (in kcal/mol) for each species.
- Output file: `/app/outputs/gibbs_free_energies.csv`
- Format: csv
- Contract: species (string), total_gibbs_free_energy_Hartree (float), relative_gibbs_free_energy_kcal_mol (float)
- Scoring: scored by hidden verifier

### Step 5: State pathway viability conclusion
- Role: scored
- Action: Based on the computed relative free energies, write a plain text file stating which catalytic pathway is more viable. Specifically, report the ΔG for FeD→FeH (pathway I) and FeD→FeSi (pathway II), and state whether pathway I or II is thermodynamically favored.
- Output file: `/app/outputs/conclusion.txt`
- Format: txt
- Contract: Plain text; expected to contain the phrases 'Pathway I' or 'Pathway II', the computed ΔG values in kcal/mol, and a clear statement of which pathway is more viable.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structures.xyz`
- `/app/outputs/gibbs_free_energies.csv`
- `/app/outputs/conclusion.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structures.xyz
- path: `/app/outputs/optimized_structures.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Optimized Cartesian coordinates of all catalytic intermediates; used by the checker to recompute energies.
- schema:
  - `type`: text
  - `description`: Standard XYZ format: first line number of atoms, second line comment (species name, charge, spin multiplicity), then lines with element symbol and x y z coordinates in Å. Multiple species are concatenated.

### gibbs_free_energies.csv
- path: `/app/outputs/gibbs_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Absolute and relative Gibbs free energies for the intermediates; the checker will independently recompute ΔG from the submitted structures.
- schema:
  - `type`: table
  - `required_columns`: `species`, `total_gibbs_free_energy_Hartree`, `relative_gibbs_free_energy_kcal_mol`
  - `units`:
    - `total_gibbs_free_energy_Hartree`: Hartree
    - `relative_gibbs_free_energy_kcal_mol`: kcal/mol

### conclusion.txt
- path: `/app/outputs/conclusion.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Conclusion stating the more viable pathway (I or II) and the computed ΔG values; checked against the recomputed energies and paper-derived gold.
- schema:
  - `type`: text

Notes: Scoring is based on the recomputed relative Gibbs free energies (ΔG) from the optimized structures, not on self-reported numbers alone. The verifier will run single-point energy + frequency calculations on the submitted XYZ files using ORCA to derive the reference energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structures.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Standard XYZ format: first line number of atoms, second line comment (species name, charge, spin multiplicity), then lines with element symbol and x y z coordinates in Å. Multiple species are concatenated."
      },
      "description": "Optimized Cartesian coordinates of all catalytic intermediates; used by the checker to recompute energies."
    },
    {
      "file": "gibbs_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "total_gibbs_free_energy_Hartree",
          "relative_gibbs_free_energy_kcal_mol"
        ],
        "units": {
          "total_gibbs_free_energy_Hartree": "Hartree",
          "relative_gibbs_free_energy_kcal_mol": "kcal/mol"
        }
      },
      "description": "Absolute and relative Gibbs free energies for the intermediates; the checker will independently recompute ΔG from the submitted structures."
    },
    {
      "file": "conclusion.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Conclusion stating the more viable pathway (I or II) and the computed ΔG values; checked against the recomputed energies and paper-derived gold."
    }
  ],
  "notes": "Scoring is based on the recomputed relative Gibbs free energies (ΔG) from the optimized structures, not on self-reported numbers alone. The verifier will run single-point energy + frequency calculations on the submitted XYZ files using ORCA to derive the reference energies."
}
```

## How you are scored
A hidden verifier evaluates each scored output separately and combines the scores into a final reward. For the optimized structures, the verifier recomputes single-point energies and vibrational frequencies at the same DFT level, then calculates relative Gibbs free energies for the FeD→FeH and FeD→FeSi transformations. Your submitted `gibbs_free_energies.csv` is compared to these recomputed values and to hidden reference data for self-consistency. The verifier also checks that your `conclusion.txt` correctly identifies the more viable pathway based on the recomputed energies. Meeting or exceeding the reference agreement yields full credit; larger deviations result in proportionally lower rewards. Reporting a number without performing the calculations is not sufficient—the verifier independently re-derives the key quantities from your submitted structures.
