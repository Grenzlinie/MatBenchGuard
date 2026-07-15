# DFT band gaps and Fe-N-O angle for NO on iron tape-porphyrin

## Problem background
Molecular wires are a key component of envisioned molecular electronic devices. Among the candidates, tape-shaped porphyrin molecules (linked macrocycles via three C–C bonds) are promising because of their extended conjugation and potentially very small HOMO-LUMO gaps. Incorporating a transition metal such as iron (FeTP) may further tailor the electronic properties, and the interaction with diatomic molecules like NO is of interest for sensing applications. This task investigates the electronic structure of iron tape-porphyrin (FeTP) and the structural and electronic changes induced by adsorption of a nitric oxide (NO) molecule.

## Approach
Density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation is used throughout. Spin-polarized calculations are performed in a periodic supercell with the tape axis along x and vacuum regions in y and z to isolate the tape. The geometry is first relaxed until forces are sufficiently converged, and then the band structure is computed along the tape direction. The same protocol is applied to the bare FeTP and to the FeTP-NO complex, where NO is placed in an end-on configuration above the Fe atom. The calculations may be carried out with any plane-wave DFT code capable of GGA-PBE (e.g., Quantum ESPRESSO) together with standard pseudopotentials. The raw band energies are processed into structured CSV files for analysis.

## Reproduction target
From the raw band structure data, extract the fundamental band gap (the minimum energy difference between the highest occupied and lowest unoccupied band, with the Fermi level set to zero) for FeTP and for FeTP-NO. Based on the computed gaps, determine whether FeTP is metallic or insulating, and whether adsorption of NO opens an insulating gap. From the optimized geometry of FeTP-NO, extract the Fe-N-O bond angle and report it in degrees. The three scored outputs are feTP_band.csv, feTPNO_band.csv, and angle.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PseudoDojo pseudopotentials: https://www.pseudo-dojo.org/
- Atomic Simulation Environment: ase

## Workflow steps

### Step 1: Build FeTP geometry
- Role: process
- Action: Construct the periodic unit cell of iron tape-porphyrin (FeTP) with the tape axis along x and a vacuum of at least 8 Å in y and z. Use standard porphyrin bond lengths and angles, link macrocycles with three C-C bonds, place Fe at the centre and add H terminations.
- Evidence: `/app/outputs/feTP_initial_structure.xyz`

### Step 2: DFT relaxation and band structure of FeTP
- Role: process
- Action: Perform spin-polarized DFT calculation with the GGA-PBE functional. Relax the FeTP geometry until forces are < 0.05 eV/Å, then compute the band structure along the tape axis. Use a plane-wave code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials, a k-point mesh of at least 30×1×1, and the vacuum defined in step 1. Output raw band energies (files for later conversion).
- Evidence: `/app/outputs/feTP_scf.log`

### Step 3: DFT geometry optimization of FeTP-NO
- Role: process
- Action: Add an NO molecule in an end-on configuration above the Fe atom of the relaxed FeTP. Perform spin-polarized DFT geometry optimization with the same functional and settings to obtain the stable adsorption geometry.
- Evidence: `/app/outputs/feTPNO_relax.log`

### Step 4: DFT band structure of FeTP-NO
- Role: process
- Action: Using the optimized FeTP-NO geometry, compute the spin-polarized electronic band structure along the tape axis with the same DFT parameters as before. Output raw band energies.
- Evidence: `/app/outputs/feTPNO_scf.log`

### Step 5: Extract FeTP band structure to CSV
- Role: scored (load-bearing)
- Action: Convert the raw band structure output from step 2 into a standardised CSV file. The file must contain a k_coord column (reciprocal coordinate, 1/Å) and energy columns for all bands within at least 5 eV of the Fermi level (Fermi level set to zero). Spin channels can be interleaved or in separate columns.
- Output file: `/app/outputs/feTP_band.csv`
- Format: csv
- Contract: Columns: k_coord (float, 1/Å), then one or more energy columns (float, eV) representing the spin-polarised band energies. Fermi level at zero.
- Scoring: scored by hidden verifier

### Step 6: Extract FeTP-NO band structure to CSV
- Role: scored (load-bearing)
- Action: Convert the raw band structure output from step 4 into a standardised CSV file, following the same format as step 5.
- Output file: `/app/outputs/feTPNO_band.csv`
- Format: csv
- Contract: Columns: k_coord (float, 1/Å), then energy columns (float, eV) for the spin-polarised bands. Fermi level at zero.
- Scoring: scored by hidden verifier

### Step 7: Extract Fe-N-O angle
- Role: scored (load-bearing)
- Action: From the optimized geometry of step 3, extract the Fe-N-O bond angle and write it to a JSON file.
- Output file: `/app/outputs/angle.json`
- Format: json
- Contract: {"fe_NO_angle_deg": float (unit: degrees)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/feTP_band.csv`
- `/app/outputs/feTPNO_band.csv`
- `/app/outputs/angle.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### feTP_band.csv
- path: `/app/outputs/feTP_band.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw band structure of bare FeTP. The checker recomputes the band gap from this file.
- schema:
  - `type`: table
  - `required_columns`: `k_coord`
  - `description`: CSV file with column 'k_coord' (float, units 1/Å) and additional columns for band energies (float, eV), one per band/spin channel. Fermi level is at zero.

### feTPNO_band.csv
- path: `/app/outputs/feTPNO_band.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw band structure of FeTP-NO. The checker recomputes the band gap.
- schema:
  - `type`: table
  - `required_columns`: `k_coord`
  - `description`: Same format as feTP_band.csv, but for the FeTP-NO system.

### angle.json
- path: `/app/outputs/angle.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fe-N-O bond angle from the optimized FeTP-NO geometry.
- schema:
  - `type`: object
  - `required`: `fe_NO_angle_deg`
  - `properties`:
    - `fe_NO_angle_deg`:
      - `type`: number
      - `unit`: degrees

Notes: All band energies assume the Fermi level set to zero. The checker computes the smallest gap between conduction and valence bands for each system. The Fe-N-O angle is compared against a hidden tolerance window.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "feTP_band.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_coord"
        ],
        "description": "CSV file with column 'k_coord' (float, units 1/Å) and additional columns for band energies (float, eV), one per band/spin channel. Fermi level is at zero."
      },
      "description": "Raw band structure of bare FeTP. The checker recomputes the band gap from this file."
    },
    {
      "file": "feTPNO_band.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_coord"
        ],
        "description": "Same format as feTP_band.csv, but for the FeTP-NO system."
      },
      "description": "Raw band structure of FeTP-NO. The checker recomputes the band gap."
    },
    {
      "file": "angle.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "fe_NO_angle_deg"
        ],
        "properties": {
          "fe_NO_angle_deg": {
            "type": "number",
            "unit": "degrees"
          }
        }
      },
      "description": "Fe-N-O bond angle from the optimized FeTP-NO geometry."
    }
  ],
  "notes": "All band energies assume the Fermi level set to zero. The checker computes the smallest gap between conduction and valence bands for each system. The Fe-N-O angle is compared against a hidden tolerance window."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the three output files. For each CSV file, it locates the valence band maximum and conduction band minimum (with the Fermi level set to zero) and computes the band gap. The gap values and the angle from angle.json are compared against hidden targets derived from the published reference study, using thresholds appropriate for the method. The verifier combines the results into a single reward score. Reporting a plausible value without producing the underlying data files will not yield credit.
