# Surface Adsorption Energetics and Electronic Structure from DFT

## Problem background
Palladium ditelluride (PdTe₂) is a layered transition-metal dichalcogenide that crystallizes in the trigonal CdI₂-type structure with a Te-terminated surface. Understanding the chemical reactivity of this surface toward ambient gases is essential to assess its long-term stability for electronic applications. In particular, the adsorption and possible decomposition of O₂, H₂O, and CO determine whether the material resists oxidation and water contamination. Density functional theory (DFT) provides a quantitative framework to compute the associated thermodynamic quantities (adsorption enthalpies, Gibbs free energies, and decomposition enthalpies) and to characterize changes in the electronic structure upon oxidation.

## Approach
The computational approach uses first-principles DFT within the GGA-PBE approximation, augmented by a van der Waals dispersion correction (vdW). All calculations are performed with the QUANTUM-ESPRESSO plane-wave code, using standard PBE pseudopotentials for Pd and Te.

Slab models are built from the bulk PdTe₂ crystal structure (space group P-3m1, three-layer slabs in a vacuum cell) to represent both the pristine surface and a surface containing one Te vacancy in the outermost layer (stoichiometry PdTe₁.₈₈). For each surface, the total energies of the bare slab and of the slab with a physisorbed molecule (O₂, H₂O, CO) are computed after full relaxation. In addition, the energies after dissociation of the molecule on the surface, and — for O₂ — the energies of the fully oxygenated Te surface and of a TeO₂-like surface layer are obtained. The energy of the isolated molecule in the gas phase is calculated in a separate cell.

From these total energies, the differential physisorption enthalpy ΔH_phys and the Gibbs free energy ΔG_phys at room temperature are derived, where the entropy change of the adsorbed molecule is estimated from the experimental enthalpy of vaporization (ΔS = ΔH_vap / T). The decomposition enthalpy ΔH_decomp is obtained as the energy difference between the adsorbed state and the dissociated state. For O₂, the additional enthalpies of full surface oxygenation and of TeO₂ formation are also evaluated.

To characterise the electronic structure, the total density of states (DOS) is computed for four specific configurations: the pristine slab, the slab after dissociative adsorption of O₂, the slab after full oxygenation of the surface Te layer, and the slab with the TeO₂-like overlayer. All DOS calculations are performed on the corresponding relaxed geometries.

As an auxiliary analysis, free-energy diagrams for the hydrogen evolution reaction (HER) and the oxygen evolution reaction (OER) are constructed using the computational hydrogen electrode model, providing a qualitative picture of the catalytic activity of the various surfaces.

## Reproduction target
The objective is to produce two scored output files that contain the computed thermodynamic and electronic-structure results:

1. `step_01_energetics.json` – a structured JSON file reporting the differential physisorption enthalpy (ΔH_phys), Gibbs free energy (ΔG_phys), and decomposition enthalpy (ΔH_decomp) for O₂, H₂O, and CO on both the pristine PdTe₂ surface and the Te-deficient PdTe₁.₈₈ surface. For O₂, the file must additionally contain the enthalpy of total surface oxygenation and the enthalpy of formation of the TeO₂-like surface layer.

2. `step_02_dos.csv` – a single CSV table with the total density of states of the pristine slab, the slab after O₂ decomposition, the slab after full oxygenation, and the slab with the TeO₂-like layer. Each row provides a configuration label, an energy (in eV), and a DOS value (arbitrary units).

## Assets

- QUANTUM-ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for Pd and Te: https://www.quantum-espresso.org/pseudopotentials/
- PdTe2 crystal structure (CdI2 type, P-3m1)

## Workflow steps

### Step 1: Construct surface slab models
- Role: process
- Action: Build three-layer slab models for pristine PdTe2, PdTe1.88 (one Te vacancy), and configurations with adsorbed/decomposed O2, H2O, CO, as well as oxygenated and TeO2-like layers, using the bulk crystal structure.
- Evidence: `/app/outputs/slab_structures.log`

### Step 2: Compute adsorption energetics
- Role: scored (load-bearing)
- Action: Perform DFT calculations (GGA-PBE+vdW) with QUANTUM-ESPRESSO to obtain total energies for each slab configuration and isolated molecules. Calculate physisorption enthalpy, Gibbs free energy (using ΔS = ΔH_vap/T), and decomposition enthalpy for O2, H2O, CO on pristine and defected surfaces. For O2 also compute the enthalpy of total surface oxygenation and of TeO2-like layer formation.
- Output file: `/app/outputs/step_01_energetics.json`
- Format: json
- Contract: JSON object with keys 'pristine' and 'defect'. Each key maps to an object with keys 'O2','H2O','CO'. For each species, fields: physisorption_Delta_H_kJmol (float), physisorption_Delta_G_kJmol (float), decomposition_Delta_H_kJmol (float). For O2 only, additional fields: oxygenation_Delta_H_kJmol (float), TeO2_formation_Delta_H_kJmol (float).
- Scoring: scored by hidden verifier

### Step 3: Compute density of states (DOS)
- Role: scored
- Action: From the optimized geometries, compute total density of states for the pristine slab, after O2 decomposition, after full oxygenation, and after TeO2 layer formation. Output a combined CSV file with columns: Configuration, Energy_eV, DOS_arb_units.
- Output file: `/app/outputs/step_02_dos.csv`
- Format: csv
- Contract: CSV with header: Configuration,Energy_eV,DOS_arb_units. Configuration values: 'pristine','O2_decomp','full_oxygenation','TeO2_layer'. Energy_eV in eV, DOS_arb_units as float.
- Scoring: scored by hidden verifier

### Step 4: HER/OER free energy calculations
- Role: process
- Action: Compute free energy diagrams for hydrogen evolution reaction (HER) and oxygen evolution reaction (OER) on pristine, defected, and oxidized PdTe2 surfaces using the computational hydrogen electrode model. Save step intermediate formation energies as evidence.
- Evidence: `/app/outputs/heroer_free_energies.json`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energetics.json`
- `/app/outputs/step_02_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energetics.json
- path: `/app/outputs/step_01_energetics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic quantities for O2, H2O, CO on pristine and Te-defected PdTe2 surfaces. Nested per surface and species with fields for physisorption ΔH, ΔG, and decomposition ΔH; for O2 additionally oxygenation ΔH and TeO2 formation ΔH. All values in kJ mol⁻¹.
- schema:
  - `type`: object
  - `required`:
    - `pristine`: object
    - `defect`: object
  - `items`: object
  - `required_columns`:
  - `units`: object

### step_02_dos.csv
- path: `/app/outputs/step_02_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states (DOS) for pristine, O2 decomposed, fully oxygenated, and TeO2-covered surfaces. The structural audit verifies the presence/absence of the O-2s peak near -18 eV.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `Configuration`, `Energy_eV`, `DOS_arb_units`
  - `units`: object

Notes: HER/OER free energy diagrams (step_3) are process-only and not scored because precise numeric gold values are not available. The main scored targets are the adsorption/decomposition energetics and the DOS features supporting the electronic structure interpretation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energetics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine": "object",
          "defect": "object"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Computed thermodynamic quantities for O2, H2O, CO on pristine and Te-defected PdTe2 surfaces. Nested per surface and species with fields for physisorption ΔH, ΔG, and decomposition ΔH; for O2 additionally oxygenation ΔH and TeO2 formation ΔH. All values in kJ mol⁻¹."
    },
    {
      "file": "step_02_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "Configuration",
          "Energy_eV",
          "DOS_arb_units"
        ],
        "units": {}
      },
      "description": "Total density of states (DOS) for pristine, O2 decomposed, fully oxygenated, and TeO2-covered surfaces. The structural audit verifies the presence/absence of the O-2s peak near -18 eV."
    }
  ],
  "notes": "HER/OER free energy diagrams (step_3) are process-only and not scored because precise numeric gold values are not available. The main scored targets are the adsorption/decomposition energetics and the DOS features supporting the electronic structure interpretation."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact and combines the results into a final reward between 0 and 1.

- The energetics file is compared to a hidden reference set. The comparison accounts for the typical quantitative spread that can arise from different DFT implementations, convergence settings, and pseudopotential choices; only physically unreasonable deviations are penalised.
- The DOS file is examined for the presence (or absence) of the expected characteristic features that reflect the formation of oxygen-derived electronic states upon oxidation.

Merely returning plausible numbers without having genuinely performed the DFT workflow described in the approach will not satisfy the verification, because the quantitative picture relies on the physical trends produced by the slab calculations.
