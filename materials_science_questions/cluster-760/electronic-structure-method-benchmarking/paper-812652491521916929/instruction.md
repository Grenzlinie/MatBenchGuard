# Antioxidant Activity Evaluation of Polyaniline-Fullerene Hybrids via Density Functional Theory

## Problem background
Polyaniline-fullerene hybrid nanomaterials are being explored for their antioxidant activity. Radical scavenging can proceed via hydrogen atom transfer (HAT), characterized by N-H bond dissociation enthalpy (BDE), or via single electron transfer (SET), characterized by ionization energy (IE) and electron affinity (EA). Frontier orbital energies (HOMO/LUMO) and a full-electron donor-acceptor map (FEDAM) based on normalized IE and EA indices (RIE and REA) can further classify antioxidant power. This task evaluates the antioxidant activity of six polyaniline and polyaniline-fullerene compounds (PANI-L, PANI-E, C60-L1, C60-L2, C60-E1, C60-E2) through density functional theory calculations to determine which compound is the most effective antioxidant.

## Approach
The computational approach uses density functional theory with the hybrid B3LYP functional and Grimme's D3 dispersion correction (GD3). First, initial molecular geometries for each compound in neutral, radical, cation, and anion forms are constructed. Geometry optimization and harmonic vibrational frequency calculations are performed at the B3LYP-GD3/6-31G(d) level to obtain minimum-energy structures, total energies, and zero-point energy corrections. Then, single-point energy calculations are carried out on the optimized geometries at the B3LYP-GD3/6-311++G(d,p) level to obtain accurate electronic energies and frontier orbital energies (HOMO and LUMO in eV). From these energies, N-H bond dissociation enthalpies (BDE) at 298 K, adiabatic ionization energies (IE), and adiabatic electron affinities (EA) are computed. Finally, the FEDAM indices are calculated: RIE = IE_compound / IE_Na and REA = EA_compound / EA_F, using standard reference values for sodium (IE_Na) and fluorine (EA_F). The compound lying in the sector with RIE < 1 and REA > 1 is identified as the best antioxidant.

## Reproduction target
Produce the antioxidant thermochemical properties (BDE, IE, EA, HOMO, LUMO) for the six compounds PANI-L, PANI-E, C60-L1, C60-L2, C60-E1, and C60-E2 computed at the B3LYP-GD3/6-311++G(d,p)//B3LYP-GD3/6-31G(d) level. Then construct the FEDAM by calculating the electron-donor index (RIE) and electron-acceptor index (REA) for each compound using the reference values IE_Na and EA_F. Identify and report which compound satisfies both RIE < 1 and REA > 1.

## Assets

- ORCA quantum chemistry package (or any open-source DFT code capable of B3LYP/6-31G(d) and B3LYP/6-311++G(d,p) with GD3): https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Build initial molecular geometries
- Role: process
- Action: Generate initial Cartesian coordinates for PANI‑L, PANI‑E, and the four polyaniline‑fullerene adducts (C60‑L1, C60‑L2, C60‑E1, C60‑E2) in their neutral, cationic, and anionic forms from known chemical structures. The structures must be chemically reasonable starting points for DFT optimization.
- Evidence: `/app/outputs/initial_geometries.json`

### Step 2: Geometry optimization and frequency calculation
- Role: process
- Action: For each of the six compounds (neutral, cation, and anion) perform DFT geometry optimization and vibrational frequency calculation at the B3LYP‑GD3/6‑31G(d) level using an open‑source quantum chemistry package. Extract the optimized total energies and zero‑point corrections.
- Evidence: `/app/outputs/opt_freq_logs.txt`

### Step 3: Single‑point energies and orbital analysis
- Role: process
- Action: Run single‑point energy calculations at the B3LYP‑GD3/6‑311++G(d,p) level on the geometries optimized in step 02 to obtain accurate total energies, as well as HOMO and LUMO eigenvalues (in eV).
- Evidence: `/app/outputs/sp_energies.txt`

### Step 4: Compute antioxidant properties (BDE, IE, EA, orbital energies)
- Role: scored (load-bearing)
- Action: From the energies and zero‑point corrections of the parent, radical, cation, and anion species (step 02 and step 03) compute for each compound: all N‑H bond dissociation enthalpies (BDE in kcal/mol at 298 K), adiabatic ionization energy (IE in kcal/mol), adiabatic electron affinity (EA in kcal/mol), HOMO energy (eV), and LUMO energy (eV). Write the results to a JSON file.
- Output file: `/app/outputs/antioxidant_properties.json`
- Format: json
- Contract: { "<compound_name>": {"bde": [float, ...], "adiabatic_IE": float, "adiabatic_EA": float, "HOMO_energy": float, "LUMO_energy": float}, ... }
- Scoring: scored by hidden verifier

### Step 5: Construct FEDAM and identify best antioxidant
- Role: scored
- Action: Using the adiabatic IE and EA from step 04 and the public reference values IE_Na = 118.5 kcal/mol, EA_F = 78.4 kcal/mol, compute the electron‑donor index RIE = IE_compound / IE_Na and electron‑acceptor index REA = EA_compound / EA_F for every compound. Identify the one compound that simultaneously satisfies RIE < 1 and REA > 1 (the best antioxidant sector). Write the results to a JSON file.
- Output file: `/app/outputs/fedor_analysis.json`
- Format: json
- Contract: { "compounds": {"<compound>": {"RIE": float, "REA": float}, ...}, "best_antioxidant": "<compound_name>" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/antioxidant_properties.json`
- `/app/outputs/fedor_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### antioxidant_properties.json
- path: `/app/outputs/antioxidant_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Antioxidant thermochemical properties and frontier orbital energies computed at B3LYP/6-311++G(d,p)//B3LYP/6-31G(d) level for six polyaniline and polyaniline-fullerene compounds.
- schema:
  - `type`: object
  - `required`: `PANI-L`, `PANI-E`, `C60-L1`, `C60-L2`, `C60-E1`, `C60-E2`
  - `description`: Each key is a compound name. Value is an object with: 'bde' (list of floats; kcal/mol), 'adiabatic_IE' (float; kcal/mol), 'adiabatic_EA' (float; kcal/mol), 'HOMO_energy' (float; eV), 'LUMO_energy' (float; eV).

### fedor_analysis.json
- path: `/app/outputs/fedor_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Full‑electron donor–acceptor map indices derived from IE/EA, plus identification of the best antioxidant compound.
- schema:
  - `type`: object
  - `required`: `compounds`, `best_antioxidant`
  - `description`: 'compounds' is an object with compound name keys, each containing 'RIE' (float) and 'REA' (float). 'best_antioxidant' is a string naming the compound in the best antioxidant sector.

Notes: The hidden checker compares the reported BDE, IE, EA, HOMO, LUMO, RIE, REA, and best_antioxidant against the paper's reported values with appropriate tolerances. Only typical chemical accuracy is expected; differences arising from the choice of open‑source DFT implementation are absorbed by the tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "antioxidant_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "PANI-L",
          "PANI-E",
          "C60-L1",
          "C60-L2",
          "C60-E1",
          "C60-E2"
        ],
        "description": "Each key is a compound name. Value is an object with: 'bde' (list of floats; kcal/mol), 'adiabatic_IE' (float; kcal/mol), 'adiabatic_EA' (float; kcal/mol), 'HOMO_energy' (float; eV), 'LUMO_energy' (float; eV)."
      },
      "description": "Antioxidant thermochemical properties and frontier orbital energies computed at B3LYP/6-311++G(d,p)//B3LYP/6-31G(d) level for six polyaniline and polyaniline-fullerene compounds."
    },
    {
      "file": "fedor_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "compounds",
          "best_antioxidant"
        ],
        "description": "'compounds' is an object with compound name keys, each containing 'RIE' (float) and 'REA' (float). 'best_antioxidant' is a string naming the compound in the best antioxidant sector."
      },
      "description": "Full‑electron donor–acceptor map indices derived from IE/EA, plus identification of the best antioxidant compound."
    }
  ],
  "notes": "The hidden checker compares the reported BDE, IE, EA, HOMO, LUMO, RIE, REA, and best_antioxidant against the paper's reported values with appropriate tolerances. Only typical chemical accuracy is expected; differences arising from the choice of open‑source DFT implementation are absorbed by the tolerances."
}
```

## How you are scored
A hidden verifier will compare your computed properties (BDE, IE, EA, HOMO, LUMO) and your FEDAM indices (RIE, REA) against expected reference values. The verifier also checks that the identified best antioxidant compound matches the expected one. The overall score is a weighted combination of the accuracy of each stage; simply reporting the correct conclusion is not sufficient — the numerical properties must be reasonably close to the expected results.
