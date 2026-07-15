# Gibbs Free Energy of Hydrogen Adsorption on Halogenated Benzothiadiazole Models

## Problem background
Covalent organic frameworks (COFs) featuring benzothiadiazole (BT) units are investigated as photocatalysts for water splitting. The introduction of halogen atoms (fluorine, chlorine) onto the BT moiety may alter the electronic structure and influence the energy required to form the hydrogen intermediate (H*) on the framework surface, a key descriptor for photocatalytic H₂ evolution activity. Density functional theory (DFT) calculations can be used to evaluate the Gibbs free energy change (ΔG) for H* adsorption on the BT unit, providing insight into this reaction barrier.

## Approach
Construct three molecular models of the benzothiadiazole unit, each with a different substituent at the carbon site directly attached to the halogen (or the equivalent position for the non-halogenated case): hydrogen (H), fluorine (F), and chlorine (Cl). For each model, perform DFT geometry optimization and vibrational frequency analysis using a dispersion-corrected exchange-correlation functional (e.g., PBE-D3 or B3LYP-D3) and an implicit solvation model (e.g., SMD or PCM) to mimic the aqueous environment. Obtain the Gibbs free energies of the clean fragment and the fragment with an adsorbed hydrogen atom (H*) placed at that same carbon. Calculate the adsorption free energy as ΔG = G(fragment+H*) − G(fragment) − ½ G(H₂) at 0 V vs. RHE. The resulting ΔG values for the three substituents capture the energetics of the H* intermediate formation.

## Reproduction target
For molecular models of the benzothiadiazole unit with substituents H, F, and Cl, compute the Gibbs free energy change (ΔG) for H* adsorption on the carbon atom directly attached to the halogen (site 4) using dispersion-corrected DFT with implicit solvation. Report the three ΔG values in eV in the file `/app/outputs/deltaG_values.json` according to the output contract. The correctness of the obtained values will be evaluated by their relative ordering and by the requirement that all values are positive.

## Assets

- Open-source DFT package (e.g., ORCA, PySCF): pyscf or orca

## Workflow steps

### Step 1: Prepare molecular models of BT units
- Role: process
- Action: Construct 3D molecular models of the benzothiadiazole (BT) unit with substituents H, F, Cl. For each, place a hydrogen atom (H*) at the carbon site directly attached to the halogen (site 4), and also prepare clean models without H*. Save initial coordinates in XYZ format.
- Evidence: `/app/outputs/initial_models.xyz`

### Step 2: DFT calculation and extraction of ΔG values
- Role: scored (load-bearing)
- Action: For each of the three models (H, F, Cl substituent), perform DFT geometry optimization with dispersion correction (e.g., PBE-D3 or B3LYP-D3) and implicit solvation (e.g., SMD water). Compute Gibbs free energies of the clean fragment and fragment+H* using vibrational frequency analysis. Calculate ΔG = G(fragment+H*) - G(fragment) - 1/2 G(H₂) at 0 V vs. RHE. Report the three ΔG values in eV in deltaG_values.json.
- Output file: `/app/outputs/deltaG_values.json`
- Format: json
- Contract: JSON object with keys 'Py-HTP-BT-COF', 'Py-FTP-BT-COF', 'Py-CITP-BT-COF', each mapping to a float representing ΔG in eV. Example: {'Py-HTP-BT-COF': 0.5, 'Py-FTP-BT-COF': 0.3, 'Py-CITP-BT-COF': 0.1}
- Scoring: scored by hidden verifier

### Step 3: Output optimized structures
- Role: scored
- Action: Collect the optimized geometries of each fragment+H* complex (H, F, Cl) from the DFT calculations and write them to optimized_structures.xyz, separated by comment lines starting with '#'.
- Output file: `/app/outputs/optimized_structures.xyz`
- Format: txt
- Contract: Concatenated XYZ files; each molecular geometry preceded by a comment line '# Py-XTP-BT-COF' with X=H,F,Cl.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deltaG_values.json`
- `/app/outputs/optimized_structures.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deltaG_values.json
- path: `/app/outputs/deltaG_values.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Gibbs free energy changes for H* adsorption on the halogenated BT unit site 4, in eV, for the three COF variants.
- schema:
  - `type`: object
  - `required`:
    - `Py-HTP-BT-COF`: float
    - `Py-FTP-BT-COF`: float
    - `Py-CITP-BT-COF`: float
  - `units`:
    - `Py-HTP-BT-COF`: eV
    - `Py-FTP-BT-COF`: eV
    - `Py-CITP-BT-COF`: eV

### optimized_structures.xyz
- path: `/app/outputs/optimized_structures.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized Cartesian coordinates of the three fragment+H* complexes.
- schema:
  - `type`: text
  - `description`: Concatenated XYZ files; each molecular geometry preceded by a comment line '# Py-XTP-BT-COF' with X=H,F,Cl.

Notes: The primary scored target is the relative ordering of ΔG values: ΔG(Py-CITP-BT-COF) < ΔG(Py-FTP-BT-COF) < ΔG(Py-HTP-BT-COF) and all must be positive. The optimized structures are checked for existence and basic format.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deltaG_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Py-HTP-BT-COF": "float",
          "Py-FTP-BT-COF": "float",
          "Py-CITP-BT-COF": "float"
        },
        "units": {
          "Py-HTP-BT-COF": "eV",
          "Py-FTP-BT-COF": "eV",
          "Py-CITP-BT-COF": "eV"
        }
      },
      "description": "Gibbs free energy changes for H* adsorption on the halogenated BT unit site 4, in eV, for the three COF variants."
    },
    {
      "file": "optimized_structures.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Concatenated XYZ files; each molecular geometry preceded by a comment line '# Py-XTP-BT-COF' with X=H,F,Cl."
      },
      "description": "Optimized Cartesian coordinates of the three fragment+H* complexes."
    }
  ],
  "notes": "The primary scored target is the relative ordering of ΔG values: ΔG(Py-CITP-BT-COF) < ΔG(Py-FTP-BT-COF) < ΔG(Py-HTP-BT-COF) and all must be positive. The optimized structures are checked for existence and basic format."
}
```

## How you are scored
A hidden verifier reads your submitted `/app/outputs/deltaG_values.json` and checks that it contains the required three entries with positive floating-point values. It then compares the relative ordering of the three ΔG values against the expected trend (which is known to the verifier but not to you). The verifier also confirms that the file `/app/outputs/optimized_structures.xyz` exists and follows the required XYZ format. The final reward is a weighted combination of the scores from these checks; merely reporting plausible numbers is not sufficient—the computed values must be obtained from the required DFT calculations and must satisfy the implicit trend and positivity constraints.
