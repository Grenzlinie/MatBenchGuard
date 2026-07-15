# Strain Effects on Electronic and Photocatalytic Properties of a vdW Heterostructure

## Problem background
Two‑dimensional van der Waals heterostructures offer a route to combine the advantages of individual monolayers for photocatalytic water splitting. Tungsten disulfide (WS₂) exhibits strong visible‑light absorption but limited redox capability, while blue phosphorus (BlueP) provides favourable carrier mobility and redox potentials but poor visible‑light absorption and stability. Stacking WS₂ and BlueP into a heterostructure and applying in‑plane uniaxial or biaxial strain can tune the band alignment, band gap, and electrochemical driving forces, potentially converting a type‑I heterostructure into type‑II or Z‑scheme configurations that effectively separate photogenerated carriers. The goal is to compute the key electronic and photocatalytic properties of strained WS₂/BlueP heterostructures and assess their thermodynamic feasibility for full water splitting.

## Approach
Use first‑principles density functional theory (DFT) with the screened hybrid functional HSE06 and a van der Waals correction (optB88‑vdW) to simulate WS₂, BlueP, and their heterostructures. Reconstruct the most stable stacking model (Model III, with phosphorus atoms atop tungsten and sulfur sites) from relaxed monolayer unit cells. Apply a set of in‑plane uniaxial (−2%, −4%) and biaxial (−2%, −6%, −8%) strains within the elastic limit. For each strained heterostructure, relax the atomic positions, then compute the electronic band structure, density of states, charge density difference, and Bader charges to extract band alignment, interlayer distance, charge transfer, effective masses of electrons and holes, and the reduction and oxidation centre energies on the normal hydrogen electrode scale. Additionally, compute the adsorption energies of the oxygen evolution reaction (OER) intermediates (*H₂O, *OH, *O, *OOH) to obtain the Gibbs free energy profiles at pH=0 and pH=7. From these profiles, determine the potential‑determining step (PDS) and the electrochemical driving force (EDF), and thus the thermodynamic feasibility of water splitting. The entire workflow is executed with the open‑source plane‑wave code Quantum ESPRESSO, the Bader charge analysis code, and Python post‑processing.

## Reproduction target
Produce a single JSON file `/app/outputs/results.json` that reports, for each of the five strain conditions (labelled `uni_-2`, `uni_-4`, `bi_-2`, `bi_-6`, `bi_-8`), the following computed quantities:

- `Bader_charge` (net charge transferred across the interface, in e)
- `interlayer_distance` (equilibrium interlayer spacing, in Å)
- `Re_center` (reduction centre energy, in eV)
- `Ox_center` (oxidation centre energy, in eV)
- `PDS_ph0` and `EDF_ph0` (potential‑determining step and electrochemical driving force at pH = 0, in eV)
- `PDS_ph7` and `EDF_ph7` (same quantities at pH = 7, in eV)
- `m_e/m0` (effective electron mass, dimensionless)
- `m_h/m0` (effective hole mass, dimensionless)
- `band_type` (string, either `"Z-scheme"` or `"type-II"`)
- `feasible_ph0` and `feasible_ph7` (boolean, whether EDF ≥ PDS at the respective pH).

These numbers must be extracted from the raw DFT outputs of the preceding workflow steps. The JSON schema is provided in the output contract.

## Assets

- Crystal structures of WS₂ and BlueP monolayers
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Bader charge analysis code (Henkelman group): https://theory.cm.utexas.edu/henkelman/code/bader/
- Python analysis packages: numpy, scipy, ase, matplotlib

## Workflow steps

### Step 1: DFT relaxation of WS₂ and BlueP monolayers
- Role: process
- Action: Set up and relax the unit cells of WS₂ and BlueP monolayers using Quantum ESPRESSO with HSE06 and optB88‑vdW. Converge total energy and forces. Obtain optimized lattice constants and atomic positions.
- Evidence: `/app/outputs/monolayer_relax.log`

### Step 2: Construction of WS₂/BlueP stacking models
- Role: process
- Action: Using the relaxed monolayer structures, construct 3×3 supercell heterostructures for the four stacking configurations (Model I–IV). Add vacuum layer along z.
- Evidence: none

### Step 3: DFT relaxation and stability selection of Model III
- Role: process
- Action: Relax each of the four heterostructure models, compute formation and binding energies, and identify Model III as the most stable. Extract the relaxed geometry of Model III.
- Evidence: `/app/outputs/formation_energies.json`

### Step 4: Relaxation of ideal WS₂/BlueP (Model III)
- Role: process
- Action: Fully relax the chosen Model III heterostructure with HSE06 and van der Waals correction. Monitor interlayer distance and total energy.
- Evidence: `/app/outputs/ideal_relax.log`

### Step 5: Electronic properties of ideal heterostructure (optional evidence)
- Role: process
- Action: Compute band structure, density of states, work function, and Bader charge for the relaxed ideal heterostructure. (Not scored, but verifies the base system.)
- Evidence: `/app/outputs/ideal_bands.gnu`

### Step 6: DFT calculations of strained heterostructures
- Role: process
- Action: Apply the specified uniaxial (−2%, −4%) and biaxial (−2%, −6%, −8%) in‑plane strains to the relaxed Model III. For each strain, relax atomic positions (keeping in‑plane cell fixed), then compute band structure, projected density of states, and charge density difference. Also compute Bader charges.
- Evidence: `/app/outputs/strain_bands.json`

### Step 7: DFT calculation of OER intermediate adsorption energies
- Role: process
- Action: On the five strained heterostructure surfaces, compute adsorption energies for the OER intermediates *H₂O, *OH, *O, and *OOH. Use the same functional and van der Waals correction.
- Evidence: `/app/outputs/adsorption_energies.json`

### Step 8: Extract quantities and build scored results.json
- Role: scored (load-bearing)
- Action: From the raw DFT outputs compute for each of the five strain configurations: (i) Bader charge transfer, (ii) interlayer distance, (iii) Re and Ox center energies using absolute electronegativity and the computed band gap, (iv) band type (Z‑scheme or type‑II) from the relative positions of CBM/VBM of the constituents, (v) effective electron/hole masses from band curvatures, (vi) OER potential‑determining step (PDS) and electrochemical driving force (EDF) at pH=0 and pH=7 following the four‑step mechanism and free‑energy relations, (vii) thermodynamic feasibility booleans (EDF ≥ PDS). Write all values into /app/outputs/results.json according to the provided JSON schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys "uni_-2", "uni_-4", "bi_-2", "bi_-6", "bi_-8". Each key maps to an object with fields: Bader_charge (float, e), interlayer_distance (float, Å), Re_center (float, eV), Ox_center (float, eV), PDS_ph0 (float, eV), EDF_ph0 (float, eV), PDS_ph7 (float, eV), EDF_ph7 (float, eV), m_e/m0 (float), m_h/m0 (float), band_type (string, "Z-scheme" or "type-II"), feasible_ph0 (boolean), feasible_ph7 (boolean).
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
- target_policy: exact_match
- description: Aggregated reproduction target containing Bader charge, interlayer distance, redox center energies, OER PDS and EDF at pH=0 and pH=7, effective masses, band type, and thermodynamic feasibility for five strained WS₂/BlueP heterostructures.
- schema:
  - `type`: object
  - `required_keys`: `uni_-2`, `uni_-4`, `bi_-2`, `bi_-6`, `bi_-8`
  - `item_schema`:
    - `type`: object
    - `required_fields`: `Bader_charge`, `interlayer_distance`, `Re_center`, `Ox_center`, `PDS_ph0`, `EDF_ph0`, `PDS_ph7`, `EDF_ph7`, `m_e/m0`, `m_h/m0`, `band_type`, `feasible_ph0`, `feasible_ph7`
    - `field_types`:
      - `Bader_charge`: number (unit: e)
      - `interlayer_distance`: number (unit: Å)
      - `Re_center`: number (unit: eV)
      - `Ox_center`: number (unit: eV)
      - `PDS_ph0`: number (unit: eV)
      - `EDF_ph0`: number (unit: eV)
      - `PDS_ph7`: number (unit: eV)
      - `EDF_ph7`: number (unit: eV)
      - `m_e/m0`: number (dimensionless)
      - `m_h/m0`: number (dimensionless)
      - `band_type`: string ("Z-scheme" or "type-II")
      - `feasible_ph0`: boolean
      - `feasible_ph7`: boolean

Notes: The checker compares each numeric field to hidden gold values from the paper using per-field absolute tolerances. Boolean and string fields are compared for exact match. Meeting or exceeding a tolerance is not defined for these physical quantities; only exact match within tolerance counts.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "uni_-2",
          "uni_-4",
          "bi_-2",
          "bi_-6",
          "bi_-8"
        ],
        "item_schema": {
          "type": "object",
          "required_fields": [
            "Bader_charge",
            "interlayer_distance",
            "Re_center",
            "Ox_center",
            "PDS_ph0",
            "EDF_ph0",
            "PDS_ph7",
            "EDF_ph7",
            "m_e/m0",
            "m_h/m0",
            "band_type",
            "feasible_ph0",
            "feasible_ph7"
          ],
          "field_types": {
            "Bader_charge": "number (unit: e)",
            "interlayer_distance": "number (unit: Å)",
            "Re_center": "number (unit: eV)",
            "Ox_center": "number (unit: eV)",
            "PDS_ph0": "number (unit: eV)",
            "EDF_ph0": "number (unit: eV)",
            "PDS_ph7": "number (unit: eV)",
            "EDF_ph7": "number (unit: eV)",
            "m_e/m0": "number (dimensionless)",
            "m_h/m0": "number (dimensionless)",
            "band_type": "string (\"Z-scheme\" or \"type-II\")",
            "feasible_ph0": "boolean",
            "feasible_ph7": "boolean"
          }
        }
      },
      "description": "Aggregated reproduction target containing Bader charge, interlayer distance, redox center energies, OER PDS and EDF at pH=0 and pH=7, effective masses, band type, and thermodynamic feasibility for five strained WS₂/BlueP heterostructures."
    }
  ],
  "notes": "The checker compares each numeric field to hidden gold values from the paper using per-field absolute tolerances. Boolean and string fields are compared for exact match. Meeting or exceeding a tolerance is not defined for these physical quantities; only exact match within tolerance counts."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results.json` and compares each numeric field for each strain label against independently determined reference values. The comparison allows small tolerances that reflect legitimate variations between DFT implementations while excluding trivial guesses. String fields (`band_type`) are checked for exact match; boolean feasibility fields are evaluated against the computed EDF and PDS. Partial credit is awarded per field, with higher weight given to the thermodynamic feasibility and band‑type assignments. The final reward is a weighted sum normalised to the range [0, 1]. Merely reporting numbers without executing the required DFT workflow is detectable and does not receive credit.
