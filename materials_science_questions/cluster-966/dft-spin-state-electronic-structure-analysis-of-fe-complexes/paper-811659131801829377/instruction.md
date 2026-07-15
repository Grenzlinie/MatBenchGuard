# Spin Density Distribution in Free Dithiolate Radicals: DFT and CASSCF Analysis

## Problem background
The active site of [FeFe]-hydrogenase, the H-cluster, contains a [2Fe]-subcluster bridged by a dithiolate ligand. The identity of the bridgehead atom (X = CH₂, NH, or O) and the extent to which unpaired spin density delocalizes from the sulfur atoms onto the bridgehead are important for interpreting paramagnetic spectroscopic signatures. This task investigates the spin density distribution in the one-electron-oxidized free dithiolate radicals [SCH₂XCH₂S]¹⁻. This task aims to compute the atomic spin densities to quantify how much spin resides on the bridgehead and sulfur atoms, and to assess the effect of geometric constraint, an open question in the context of the H-cluster.

## Approach
The approach combines density functional theory (DFT), Bader's Quantum Theory of Atoms in Molecules (QTAIM), and complete active space self-consistent field (CASSCF) calculations. For three free dithiolate radicals (pdt, dtma, dtme) in two geometries each (gas-phase optimized 'relaxed' and 'fixed' to the chelating conformation from crystal structures of their [2Fe] complexes), we first perform DFT geometry optimizations for the relaxed forms. Single-point DFT calculations (BP86/TZVP or equivalent) then provide electron densities and spin densities for all six ligand/geometry combinations. QTAIM basin integration extracts atomic spin densities on the bridgehead atom (C, N, or O) and the two sulfur atoms. To validate the single-reference DFT picture, a CASSCF(13,17) calculation is performed for the dtma radical in both relaxed and fixed geometries, using an active space composed of four S–C bonding/antibonding, four C–N bonding/antibonding, four S lone pairs, and one N lone pair. From the natural orbital occupations, the maximum occupied–virtual mixing is derived.

## Reproduction target
Produce two scored artifacts. (1) free_ligand_spin_densities.csv: a CSV table with one row per ligand/geometry combination (six rows). Columns must be 'ligand' (pdt, dtma, dtme), 'geometry' (relaxed, fixed), 'bridgehead_spin_density_e' (the QTAIM atomic spin density on the bridgehead atom in electrons), and 'sulfur_spin_density_e' (the sum of spin densities on the two sulfur atoms in electrons). (2) casdtma_mixing.json: a JSON object containing 'relaxed_max_mixing' and 'fixed_max_mixing', each the maximum deviation from an integer occupation (2 or 0) among the active orbitals in the CASSCF(13,17) for the dtma radical, in electrons.

## Assets

- Quantum chemistry code (ORCA or NWChem): https://orcaforum.kofo.mpg.de/
- QTAIM analysis tool (Multiwfn or AIMAll): http://sobereva.com/multiwfn/
- Crystal structure of [Fe2(CO)6(μ-SCH2CH2CH2S)] (pdt complex): 10.1002/(SICI)1521-3773(19991115)38:22<3373::AID-ANIE3373>3.0.CO;2-4
- Crystal structure of [Fe2(CO)6(μ-SCH2NHCH2S)] (dtma complex): 10.1021/om7007983
- Crystal structure of [Fe2(CO)6(μ-SCH2OCH2S)] (dtme complex): 10.1021/om0504798

## Workflow steps

### Step 1: Prepare molecular models
- Role: process
- Action: Build initial Cartesian coordinates for the three one-electron-oxidized dithiolate radicals [SCH2XCH2S]1- (X=CH2 (pdt), NH (dtma), O (dtme)) in two geometries: (i) relaxed – starting from standard bond lengths for gas-phase optimization; (ii) fixed – geometries extracted from the crystal structures of the corresponding [2Fe] biomimetic complexes (res_03, res_04, res_05) by removing the iron and carbonyl groups and adding the missing hydrogen atoms, then fixing all non-hydrogen atoms at the crystallographic positions.
- Evidence: none

### Step 2: DFT geometry optimization of relaxed free radicals
- Role: process
- Action: Perform gas-phase geometry optimization of each free dithiolate radical (pdt, dtma, dtme) using DFT with BP86/TZVP or an equivalent functional (e.g., PBE/def2-TZVP) to obtain fully relaxed structures.
- Evidence: `/app/outputs/relaxed_geometries.log`

### Step 3: Single-point DFT calculations for all six ligand/geometry combinations
- Role: process
- Action: Run single-point DFT calculations (BP86/TZVP or equivalent) for each of the six ligand/geometry combinations (pdt relaxed, pdt fixed, dtma relaxed, dtma fixed, dtme relaxed, dtme fixed). Use the optimized relaxed coordinates from step_02 and the fixed coordinates from step_01. The calculations must produce wavefunction or electron density files suitable for QTAIM analysis.
- Evidence: `/app/outputs/single_point_energies.txt`

### Step 4: QTAIM atomic spin density integration
- Role: process
- Action: For each of the six conditions, use a QTAIM tool (Multiwfn or AIMAll) to perform basin integration of the total electron density from step_03. Obtain the integrated atomic spin density (in electrons) on the bridgehead atom (C, N, O) and the sum of spin densities on the two sulfur atoms.
- Evidence: `/app/outputs/aim_integration.log`

### Step 5: Write free ligand spin densities CSV
- Role: scored (load-bearing)
- Action: Compile the integrated spin densities from step_04 into a CSV file. Each row must contain the ligand identifier (pdt, dtma, or dtme), the geometry type (relaxed or fixed), the bridgehead atomic spin density (in e), and the total sulfur atomic spin density (in e).
- Output file: `/app/outputs/free_ligand_spin_densities.csv`
- Format: csv
- Contract: Header: ligand, geometry, bridgehead_spin_density_e, sulfur_spin_density_e. Each row corresponds to one ligand/geometry combination.
- Scoring: scored by hidden verifier

### Step 6: CASSCF(13,17) calculation for dtma radical
- Role: process
- Action: For the dtma radical ([SCH2NHCH2S]1-) in both relaxed and fixed geometries, run CASSCF with an active space of 13 orbitals (four S–C σ/σ*, four C–N σ/σ*, four S lone pairs, one N lone pair) containing 17 electrons. Use the geometries obtained in step_02 (relaxed) and step_01 (fixed). Converge the calculation and obtain the natural orbital occupation numbers.
- Evidence: `/app/outputs/casscf_occupation.log`

### Step 7: Write CASSCF mixing values JSON
- Role: scored
- Action: From the CASSCF one-electron density matrix of step_06, compute the maximum deviation from integer occupation (2 or 0) for any active orbital (the largest occupied–virtual mixing). Report this value for the relaxed and for the fixed geometry in a JSON file.
- Output file: `/app/outputs/casdtma_mixing.json`
- Format: json
- Contract: Keys: "relaxed_max_mixing" (float, e), "fixed_max_mixing" (float, e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_ligand_spin_densities.csv`
- `/app/outputs/casdtma_mixing.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_ligand_spin_densities.csv
- path: `/app/outputs/free_ligand_spin_densities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: AIM-integrated atomic spin densities on the bridgehead and sulfur atoms for the three free ligands in relaxed and chelation-constrained geometries.
- schema:
  - `type`: table
  - `required_columns`: `ligand`, `geometry`, `bridgehead_spin_density_e`, `sulfur_spin_density_e`
  - `units`:
    - `bridgehead_spin_density_e`: e
    - `sulfur_spin_density_e`: e

### casdtma_mixing.json
- path: `/app/outputs/casdtma_mixing.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum deviation from integer occupation (occupied–virtual mixing) from CASSCF(13,17) for the dtma radical in relaxed and fixed geometries.
- schema:
  - `type`: object
  - `required`:
    - `relaxed_max_mixing`: number
    - `fixed_max_mixing`: number
  - `units`:
    - `relaxed_max_mixing`: e
    - `fixed_max_mixing`: e

Notes: The hidden checker will compare the reported spin densities and CASSCF mixing values to paper gold values with suitable tolerances (±0.02 e for bridgehead, ±0.05 e for S, ±0.01 e for CASSCF mixing). The agent must execute the full DFT+QTAIM+CASSCF pipeline; the scored outputs cannot be obtained by guesswork alone.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_ligand_spin_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ligand",
          "geometry",
          "bridgehead_spin_density_e",
          "sulfur_spin_density_e"
        ],
        "units": {
          "bridgehead_spin_density_e": "e",
          "sulfur_spin_density_e": "e"
        }
      },
      "description": "AIM-integrated atomic spin densities on the bridgehead and sulfur atoms for the three free ligands in relaxed and chelation-constrained geometries."
    },
    {
      "file": "casdtma_mixing.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "relaxed_max_mixing": "number",
          "fixed_max_mixing": "number"
        },
        "units": {
          "relaxed_max_mixing": "e",
          "fixed_max_mixing": "e"
        }
      },
      "description": "Maximum deviation from integer occupation (occupied–virtual mixing) from CASSCF(13,17) for the dtma radical in relaxed and fixed geometries."
    }
  ],
  "notes": "The hidden checker will compare the reported spin densities and CASSCF mixing values to paper gold values with suitable tolerances (±0.02 e for bridgehead, ±0.05 e for S, ±0.01 e for CASSCF mixing). The agent must execute the full DFT+QTAIM+CASSCF pipeline; the scored outputs cannot be obtained by guesswork alone."
}
```

## How you are scored
A hidden verifier will independently inspect your free_ligand_spin_densities.csv and casdtma_mixing.json. It compares the bridgehead and sulfur spin densities, and the maximum CASSCF mixing values, against reference values obtained from the same computational protocol. The verifier applies predetermined tolerances and awards credit according to how close your results match. Simply reporting numbers without performing the required DFT, QTAIM, and CASSCF calculations will not produce valid artifacts and will not receive credit.
