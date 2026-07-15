# DFT Analysis of PMS Adsorption on Oxygen-Vacancy-Modified NiO/ZnO Surfaces

## Problem background
Peroxymonosulfate (PMS) can be activated by a NiO-ZnO heterojunction catalyst containing oxygen vacancies to degrade organic pollutants such as bisphenol A. The activity is thought to arise from a surface-bound radical mechanism, but the atomistic origin – how charge redistribution at the NiO/ZnO interface and strong PMS adsorption facilitate radical generation – is not fully clear. Density functional theory (DFT) calculations are used to quantify the adsorption strength, the structural perturbation of the PMS molecule, and the interfacial electron transfer, providing insight into the catalyst's PMS activation ability.

## Approach
Use open-source DFT software (Quantum ESPRESSO or CP2K) with the GGA-PBE functional, spin polarization, and a Hubbard U correction on Ni 3d states to model the catalyst and PMS adsorption. Build a slab model of the heterojunction by placing a NiO(200) supercell on a ZnO(101) supercell and introduce one surface oxygen vacancy on ZnO. Optimize the bare slab geometry, then analyze the charge density difference and perform Bader charge analysis to quantify electron redistribution at the interface. Separately optimize an isolated PMS molecule, create an adsorption complex on the slab, and optimize that complex. From the optimized geometries, compute the adsorption energy, the O–O bond length change upon adsorption, and the Bader charge transferred to PMS.

## Reproduction target
Produce DFT results that characterize PMS activation by the oxygen-vacancy-modified NiO/ZnO heterojunction:
1. The adsorption energy of PMS on the slab (eV).
2. The peroxide O–O bond length before and after adsorption (Å), showing whether the bond elongates.
3. A qualitative charge density difference description and a Bader charge summary for the bare slab, indicating the direction of interfacial electron transfer.

## Assets

- Crystal structures of wurtzite ZnO and rocksalt NiO: https://materialsproject.org/
- Peroxymonosulfate (PMS) molecular structure
- Open-source DFT code (Quantum ESPRESSO or CP2K): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for Ni, Zn, O, H, S, C: https://pseudopotentials.quantum-espresso.org/
- Bader charge analysis program: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build and optimize bare NiO/ZnO slab with oxygen vacancy
- Role: process
- Action: Construct a slab model by placing a 1×1×2 supercell of NiO(200) on a 3×5×2 supercell of ZnO(101). Remove one surface oxygen atom from the ZnO layer to create an oxygen vacancy. Perform DFT geometry optimization of the entire bare slab using GGA-PBE with spin polarization, a Hubbard U correction on Ni 3d, and a plane-wave cutoff of at least 400 eV. Relax all atomic positions until forces converge. Save the optimized geometry.
- Evidence: `/app/outputs/slab_optimization.log`

### Step 2: Charge density difference and Bader analysis for bare slab
- Role: scored
- Action: Using the optimized bare slab, compute the charge density difference Δρ = ρ(NiO/ZnO) - ρ(NiO) - ρ(ZnO) by performing separate single-point calculations for the isolated NiO layer, isolated ZnO slab (with vacancy), and the full heterojunction. Run Bader charge analysis on the full slab to obtain net charges. Summarize the qualitative picture of electron accumulation/depletion and report the net electron gain/loss of the NiO layer.
- Output file: `/app/outputs/step_02_charge_density_analysis.json`
- Format: json
- Contract: {"type":"object","properties":{"charge_density_difference_description":{"type":"string"},"bader_charges_summary":{"type":"string"}},"required":["charge_density_difference_description","bader_charges_summary"]}
- Scoring: scored by hidden verifier

### Step 3: PMS adsorption on NiO/ZnO slab
- Role: scored (load-bearing)
- Action: Construct a PMS molecule and optimize it in a vacuum cell. Place it on the optimized slab in a plausible adsorption geometry (e.g., O atoms of the peroxide group near Ni). Perform DFT geometry optimization of the adsorption complex using the same DFT settings. Calculate the adsorption energy Eads = E(total) - E(slab) - E(PMS). Extract the O–O bond length before and after adsorption. Perform Bader analysis on the adsorbed complex to obtain the net charge transferred to the PMS molecule.
- Output file: `/app/outputs/step_01_geometry_optimization_results.json`
- Format: json
- Contract: {"type":"object","properties":{"adsorption_energy_PMS":{"type":"number","unit":"eV"},"O_O_bond_length_before_adsorption":{"type":"number","unit":"Å"},"O_O_bond_length_after_adsorption":{"type":"number","unit":"Å"},"bader_charge_transfer_to_PMS":{"type":"number"}},"required":["adsorption_energy_PMS","O_O_bond_length_before_adsorption","O_O_bond_length_after_adsorption"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_charge_density_analysis.json`
- `/app/outputs/step_01_geometry_optimization_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_charge_density_analysis.json
- path: `/app/outputs/step_02_charge_density_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Qualitative charge redistribution evidence from the bare heterojunction. Verified for non-empty, internally consistent description.
- schema:
  - `type`: object
  - `required`:
    - `charge_density_difference_description`: string
    - `bader_charges_summary`: string

### step_01_geometry_optimization_results.json
- path: `/app/outputs/step_01_geometry_optimization_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Quantitative adsorption results: adsorption energy and O–O bond length change, compared to paper-reported values.
- schema:
  - `type`: object
  - `required`:
    - `adsorption_energy_PMS`: number (eV)
    - `O_O_bond_length_before_adsorption`: number (Å)
    - `O_O_bond_length_after_adsorption`: number (Å)
  - `properties`:
    - `bader_charge_transfer_to_PMS`: number

Notes: The slab optimization (step_1) is a required process step and not scored. The charge analysis is structural; the adsorption values are compared to paper gold with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_charge_density_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "charge_density_difference_description": "string",
          "bader_charges_summary": "string"
        }
      },
      "description": "Qualitative charge redistribution evidence from the bare heterojunction. Verified for non-empty, internally consistent description."
    },
    {
      "file": "step_01_geometry_optimization_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "adsorption_energy_PMS": "number (eV)",
          "O_O_bond_length_before_adsorption": "number (Å)",
          "O_O_bond_length_after_adsorption": "number (Å)"
        },
        "properties": {
          "bader_charge_transfer_to_PMS": "number"
        }
      },
      "description": "Quantitative adsorption results: adsorption energy and O–O bond length change, compared to paper-reported values."
    }
  ],
  "notes": "The slab optimization (step_1) is a required process step and not scored. The charge analysis is structural; the adsorption values are compared to paper gold with tolerances."
}
```

## How you are scored
A hidden verifier independently scores each of your two output artifacts (charge analysis and PMS adsorption) according to the output contract below. The adsorption energy and O–O bond lengths are compared against reference values with tolerances that absorb legitimate computational spread; the bond length increase upon adsorption is also verified. The charge analysis is checked for non-empty, internally consistent descriptions of electron redistribution. The two stages are combined by weight into a final reward. Reporting the paper's numbers without executing the computational workflow is not sufficient; the artifacts must be produced by running the DFT calculations and subsequent analysis as described.
