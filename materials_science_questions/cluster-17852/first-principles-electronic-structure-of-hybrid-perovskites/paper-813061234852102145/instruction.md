# CH3NH3SnI3/TiO2 Interface Stability and Potential Drop from DFT

## Problem background
Perovskite solar cells have achieved high power conversion efficiency, but the toxicity of lead hinders commercialization. Tin-based perovskites like CH3NH3SnI3 are promising lead-free alternatives. The interface between the perovskite absorber and the electron-transport layer (TiO2) plays a crucial role in charge separation and overall device performance. This study uses density functional theory to investigate the structural stability and charge separation capabilities of four different CH3NH3SnI3/TiO2 interfaces, comparing two TiO2 phases (anatase and rutile) and two perovskite surface terminations (MAI and SnI2). The goal is to determine which interface configuration provides the strongest adhesion and the best driving force for electron-hole pair separation.

## Approach
The conceptual approach employs first-principles density functional theory (DFT) with plane-wave basis and pseudopotentials. The workflow begins by optimizing the bulk crystal structures of tetragonal CH3NH3SnI3, anatase TiO2, and rutile TiO2. Using the optimized bulk structures, slab models are constructed for the perovskite (001) surface with two terminations (MAI-rich and SnI2-rich) and for anatase (001) and rutile (001) substrates. Four interface supercells are created: MAI/rutile, MAI/anatase, SnI2/rutile, and SnI2/anatase. All interface models are relaxed using DFT including van der Waals corrections. The binding energy for each interface is computed as Eb = E_total - E_substrate - E_perovskite_slab, where E_total is the total energy of the relaxed interface, and E_substrate and E_perovskite_slab are single-point energies of the separated slabs kept at the interface geometry. Additionally, the plane-averaged electrostatic potential along the direction perpendicular to the interface is calculated, and the potential drop across the interface is extracted as the difference between the average potential in the perovskite region far from the interface and that in the TiO2 region. The four binding energies and potential drops are then compared to identify the most favorable interface for adhesion and charge separation.

## Reproduction target
Produce two JSON output files: `binding_energies.json` containing four floating-point numbers (keys: `MAI/R`, `MAI/A`, `SnI2/R`, `SnI2/A`) for the binding energies in eV, and `potential_drops.json` containing the corresponding potential drops in eV. The target is to correctly compute the relative ordering among the four interfaces: identify which interface has the most negative binding energy (strongest adhesion) and which has the largest potential drop (strongest driving force for charge separation).

## Assets

- CH3NH3SnI3 bulk structure
- Anatase TiO2 bulk structure
- Rutile TiO2 bulk structure
- DFT code (open-source): quantum-espresso
- PAW pseudopotentials (GGA-PBE): https://pseudopotentials.quantum-espresso.org/upf_files/

## Workflow steps

### Step 1: Bulk relaxation of CH3NH3SnI3
- Role: process
- Action: Perform DFT relaxation of the tetragonal bulk CH3NH3SnI3 unit cell to obtain optimized lattice constants. Optionally verify the band gap for validation (not scored).
- Evidence: `/app/outputs/perovskite_relax.log`

### Step 2: Bulk relaxation of anatase TiO2
- Role: process
- Action: Perform DFT relaxation of the anatase TiO2 unit cell to obtain optimized lattice constants.
- Evidence: `/app/outputs/anatase_relax.log`

### Step 3: Bulk relaxation of rutile TiO2
- Role: process
- Action: Perform DFT relaxation of the rutile TiO2 unit cell to obtain optimized lattice constants.
- Evidence: `/app/outputs/rutile_relax.log`

### Step 4: Interface model construction
- Role: process
- Action: Using the relaxed bulk structures, generate slab models for the perovskite (001) surface with MAI termination (4 MAI, 3 SnI2 layers) and SnI2 termination (4 SnI2, 3 MAI layers), and for anatase (001) with five layers and rutile (001) with four layers. Combine to create four interface supercells: MAI/R, MAI/A, SnI2/R, SnI2/A. Apply 20 Å vacuum. Ensure minimal lateral strain as dictated by the lattice match (about 5.78% for rutile, −2.80% for anatase).
- Evidence: `/app/outputs/interface_models.pkl`

### Step 5: Interface structure relaxation
- Role: process
- Action: Fully relax all four interface models using DFT (PAW-PBE+vdW-DF). Record the total energy for each configuration.
- Evidence: `/app/outputs/relaxed_energies.json`

### Step 6: Single-point energy of isolated slabs
- Role: process
- Action: For each relaxed interface, perform single-point energy calculations on the separated TiO2 substrate and perovskite slab (atom positions kept as in the interface) to obtain E_sub and E_p.
- Evidence: `/app/outputs/reference_energies.json`

### Step 7: Compute binding energies
- Role: scored (load-bearing)
- Action: Calculate Eb = E_total − E_sub − E_p for each of the four interfaces and write the results.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"MAI/R": <float>, "MAI/A": <float>, "SnI2/R": <float>, "SnI2/A": <float>} (all values in eV)
- Scoring: scored by hidden verifier

### Step 8: Plane-averaged electrostatic potential calculation
- Role: process
- Action: For each relaxed interface, compute the plane-averaged electrostatic potential along the z‑direction using post‑processing tools.
- Evidence: `/app/outputs/potential_profiles.dat`

### Step 9: Extract potential drops
- Role: scored
- Action: From the plane‑averaged potential profiles, determine the average potential in the TiO2 region and in the perovskite slab far from the interface, compute the drop ΔV = V_perovskite − V_TiO2, and write the results.
- Output file: `/app/outputs/potential_drops.json`
- Format: json
- Contract: {"MAI/R": <float>, "MAI/A": <float>, "SnI2/R": <float>, "SnI2/A": <float>} (all values in eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`
- `/app/outputs/potential_drops.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Binding energies (Eb) for the four CH3NH3SnI3/TiO2 interface configurations. The scoring verifies that SnI2/A has the most negative value (strongest binding).
- schema:
  - `type`: object
  - `required`:
    - `MAI/R`: float (eV)
    - `MAI/A`: float (eV)
    - `SnI2/R`: float (eV)
    - `SnI2/A`: float (eV)

### potential_drops.json
- path: `/app/outputs/potential_drops.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electrostatic potential drops (ΔV) across each interface. The scoring verifies that SnI2/A has the largest value (best charge separation).
- schema:
  - `type`: object
  - `required`:
    - `MAI/R`: float (eV)
    - `MAI/A`: float (eV)
    - `SnI2/R`: float (eV)
    - `SnI2/A`: float (eV)

Notes: Scoring checks the relative ordering among the four interfaces: SnI2/A must show the most negative binding energy and the largest potential drop. Absolute values may vary due to code choice; the trends are the verified targets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "MAI/R": "float (eV)",
          "MAI/A": "float (eV)",
          "SnI2/R": "float (eV)",
          "SnI2/A": "float (eV)"
        }
      },
      "description": "Binding energies (Eb) for the four CH3NH3SnI3/TiO2 interface configurations. The scoring verifies that SnI2/A has the most negative value (strongest binding)."
    },
    {
      "file": "potential_drops.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "MAI/R": "float (eV)",
          "MAI/A": "float (eV)",
          "SnI2/R": "float (eV)",
          "SnI2/A": "float (eV)"
        }
      },
      "description": "Electrostatic potential drops (ΔV) across each interface. The scoring verifies that SnI2/A has the largest value (best charge separation)."
    }
  ],
  "notes": "Scoring checks the relative ordering among the four interfaces: SnI2/A must show the most negative binding energy and the largest potential drop. Absolute values may vary due to code choice; the trends are the verified targets."
}
```

## How you are scored
A hidden verifier will independently inspect your output files. For `binding_energies.json`, it will verify that all four values are negative and that the ordering among the interfaces matches the expected result from the reference DFT calculations: one particular interface must have the most negative value (strongest binding). For `potential_drops.json`, it will verify that all values are positive and that the same interface has the largest value. The final reward is a weighted combination of these two checks. The verifier does not compare absolute values, only the relative trends, because numerical magnitudes can vary with the choice of DFT code and parameters.
