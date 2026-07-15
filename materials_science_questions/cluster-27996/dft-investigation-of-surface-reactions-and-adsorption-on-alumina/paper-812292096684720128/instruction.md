# Ab initio Interaction Energies of Amides with Alumina Model Surface Sites

## Problem background
This study investigates the adsorption of two amides, N-ethylacetamide (linear) and 2-pyrrolidinone (cyclic), on γ-alumina. Experimentally, the cyclic molecule adsorbs more strongly and can displace the linear one, but the microscopic origin is not obvious from wet-lab data alone. To rationalize the observed selectivity, the work includes ab initio SCF calculations that model adsorption complexes between the amides and simple aluminium hydroxide surface sites. The computational component aims to quantify the relative strengths of single- and dual-site hydrogen bonding and to measure the conformational energetics of the linear amide. Your task is to reproduce these theoretical interaction energies, energy differences, and key geometric parameters by re-running a comparable quantum chemistry workflow.

## Approach
Use Hartree–Fock SCF theory with the 6-31G basis set augmented by a d-function (exponent 0.325) on aluminium. Perform full geometry optimizations without symmetry constraints for the isolated amides (trans and cis N-ethylacetamide, 2-pyrrolidinone), the Al(OH)H₂ model cluster, and a series of adsorption complexes formed by these molecules with one or two surface sites. The complexes include both single-site binding modes (via carbonyl only, amine only) and dual-site binding. The isomerization barrier for trans→cis rotation of N-ethylacetamide is obtained through a transition state search or a relaxed potential energy scan along the N–C bond dihedral angle. From the optimized total energies compute interaction energies (complex energy minus sum of isolated fragment energies) and extract the shortest O···H hydrogen-bond distance in each complex. All calculations should be run with an open-source quantum chemistry package such as ORCA.

## Reproduction target
Produce a single JSON file, `computed_results.json`, that reports for every molecular species and complex: its total Hartree–Fock energy (Hartree), the derived interaction energy (kJ/mol, null where not applicable), and the shortest O···H distance (nm, null where not applicable). Additionally report two global scalars: the cis–trans energy difference of N-ethylacetamide (kJ/mol) and the activation energy for the trans→cis isomerization (kJ/mol). The relative ordering among interaction energies (cyclic vs. cis linear, carbonyl-only vs. amine-only, single-site vs. two-site) must be internally consistent and will be checked against the paper's reported trends.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Build molecular geometries
- Role: process
- Action: Construct initial 3D structures for trans and cis N-ethylacetamide, 2-pyrrolidinone, the Al(OH)H₂ model cluster, and all required adsorption complexes (cis N-ethylacetamide + Al(OH)H₂, 2-pyrrolidinone + Al(OH)H₂, trans N-ethylacetamide bound to Al(OH)H₂ via carbonyl only, trans N-ethylacetamide bound via amine only, and trans N-ethylacetamide bound to two Al(OH)H₂ units). Output the structures in a format suitable for the quantum chemistry package.
- Evidence: `/app/outputs/initial_geometries.log`

### Step 2: Hartree-Fock geometry optimization
- Role: process
- Action: Perform Hartree-Fock geometry optimizations using the 6-31G basis set with an additional d-orbital (exponent 0.325) on aluminium for all isolated molecules and complexes. Run without symmetry constraints. Save the optimized geometries and total electronic energies.
- Evidence: `/app/outputs/geometry_optimizations.log`

### Step 3: Transition state or rotation scan for trans-cis isomerization
- Role: process
- Action: For trans N-ethylacetamide, locate the transition state or perform a relaxed potential energy scan for rotation about the N-C bond at the same HF/6-31G(d) level to obtain the activation energy for trans→cis isomerization. Save the resulting energy.
- Evidence: `/app/outputs/ts_search.log`

### Step 4: Compute interaction energies and geometric parameters
- Role: scored (load-bearing)
- Action: From the optimized total energies and the isomerization barrier result, compute: (a) the cis-trans energy difference of N-ethylacetamide in kJ/mol; (b) the activation energy for trans→cis isomerization in kJ/mol; (c) interaction energies for each complex (E_complex – sum_of_fragment_energies) in kJ/mol; (d) the shortest O···H hydrogen-bond distance for each complex in nm. Compile all results into a JSON file.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: object with top-level keys: 'systems' (array of objects, each with 'name' (string), 'total_energy_hartree' (float), 'interaction_energy_kJmol' (float or null), 'oh_distance_nm' (float or null)); 'cis_trans_energy_diff_kJmol' (float); 'activation_energy_kJmol' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The artifact reports total energies and derived interaction energies, O···H distances, and conformational energetics. The verifier recomputes derived quantities from total energies and checks them against hidden paper gold values within tolerances; it also validates relative trends (e.g., interaction energy differences, bonding strength ratios).
- schema:
  - `type`: object
  - `required`:
    - `systems`: array
    - `cis_trans_energy_diff_kJmol`: float
    - `activation_energy_kJmol`: float
  - `items`:
    - `name`: string
    - `total_energy_hartree`: float
    - `interaction_energy_kJmol`: float or null
    - `oh_distance_nm`: float or null
  - `units`:
    - `total_energy_hartree`: Hartree
    - `interaction_energy_kJmol`: kJ/mol
    - `oh_distance_nm`: nm
    - `cis_trans_energy_diff_kJmol`: kJ/mol
    - `activation_energy_kJmol`: kJ/mol

Notes: The hidden checker uses tolerances appropriate for independent code implementations (energies ≤ 2 kJ/mol, distances ≤ 0.01 nm) and verifies relative ordering constraints.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "systems": "array",
          "cis_trans_energy_diff_kJmol": "float",
          "activation_energy_kJmol": "float"
        },
        "items": {
          "name": "string",
          "total_energy_hartree": "float",
          "interaction_energy_kJmol": "float or null",
          "oh_distance_nm": "float or null"
        },
        "units": {
          "total_energy_hartree": "Hartree",
          "interaction_energy_kJmol": "kJ/mol",
          "oh_distance_nm": "nm",
          "cis_trans_energy_diff_kJmol": "kJ/mol",
          "activation_energy_kJmol": "kJ/mol"
        }
      },
      "description": "The artifact reports total energies and derived interaction energies, O···H distances, and conformational energetics. The verifier recomputes derived quantities from total energies and checks them against hidden paper gold values within tolerances; it also validates relative trends (e.g., interaction energy differences, bonding strength ratios)."
    }
  ],
  "notes": "The hidden checker uses tolerances appropriate for independent code implementations (energies ≤ 2 kJ/mol, distances ≤ 0.01 nm) and verifies relative ordering constraints."
}
```

## How you are scored
A hidden verifier reads your submitted artifacts and scores each workflow stage independently, then combines the stage scores (weighted) into a final reward between 0 and 1. The verifier recomputes derived quantities (interaction energies, energy differences) from the raw total energies you report, and compares all key values and relative trends against the paper's hidden gold values using appropriate tolerances that allow for legitimate toolchain variation. The verifier also validates that the required structural relationships (e.g., ordering and approximate ratios among interaction energies) hold. Submitting the paper’s numerical results without evidence of genuine computation will not earn full credit; all required intermediate log files and output artifacts must demonstrate that the calculations were actually executed.
