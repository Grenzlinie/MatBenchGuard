# Spin-polarized DFT calculation of magnetic moments in Al-doped 4H-SiC with vacancies

## Problem background
Dilute magnetic semiconductors (DMS) based on non-magnetic dopants are attractive for spintronics because they avoid the clustering of magnetic transition-metal impurities. In Al-doped 4H-SiC, the origin of the observed ferromagnetism is not fully understood: it may be tied to the local magnetic moments of atoms that are themselves non-magnetic. First-principles calculations can be used to compute the distribution of magnetic moments in such systems, revealing which atomic species carry the spin polarization when defects (vacancies) are present. This task computes the magnetic moments in Al-doped 4H-SiC supercells with and without Si or C vacancies to investigate the role of carbon in the magnetic response.

## Approach
The method relies on spin-polarized density functional theory (DFT) calculations using a plane-wave pseudopotential approach. The exchange-correlation functional is the generalized gradient approximation in the Perdew-Burke-Ernzerhof (PBE) form. Three 192-atom supercell models of 4H-SiC are constructed to represent different doping scenarios:

- Al-only: one Si atom replaced by an Al atom.
- Al+V_Si: one Al substitution and one Si vacancy.
- Al+V_C: one Al substitution and one C vacancy.

For each supercell, a full geometry optimization (atomic positions and cell volume) is performed with spin polarization enabled. From the relaxed structures, the total magnetic moment per supercell and the sum of the magnetic moments on all carbon atoms are extracted. These values quantify the net magnetization and the carbon contribution, allowing a comparison of how vacancies influence the magnetic moments.

## Reproduction target
Using the DFT workflow, compute the following for each of the three doping configurations (Al-only, Al+V_Si, Al+V_C):

- Total magnetic moment per supercell (in μB)
- Carbon magnetic moment: the sum of absolute magnetic moments on all carbon atoms in the supercell (in μB)

Save the results as a JSON array in `/app/outputs/results.json`, with each entry containing the system name and the two magnetic moment values. This output is the sole scored artifact.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- 4H-SiC crystal structure (pristine): https://materialsproject.org/materials/mp-8062

## Workflow steps

### Step 1: Construct supercell models for three doping configurations
- Role: process
- Action: Build three 4×3×2 supercell (192 atoms) models of 4H‑SiC: (a) one Al atom substituting a Si atom (Al‑only), (b) one Al + one Si vacancy (Al+V_Si), (c) one Al + one C vacancy (Al+V_C). Generate the necessary DFT input files (e.g., Quantum ESPRESSO pw.x input) for each.
- Evidence: `/app/outputs/supercell_inputs.zip`

### Step 2: Spin-polarized DFT geometry optimization
- Role: process
- Action: For each of the three supercells, perform a spin-polarized DFT geometry optimization using the GGA-PBE exchange-correlation functional. Relax both atomic positions and cell volume to convergence. Save the relaxed structure files and relaxation logs.
- Evidence: `/app/outputs/relaxation_outputs.tar.gz`

### Step 3: Extract magnetic moments and write results.json
- Role: scored (load-bearing)
- Action: From the relaxed DFT output of each system, compute the total magnetic moment per supercell (in μB) and the sum of absolute magnetic moments on all carbon atoms (in μB). Write these values to results.json as a JSON array of objects, one per system.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "type": "array",
  "items": {
    "type": "object",
    "required": ["name", "total_magnetic_moment_per_supercell", "carbon_magnetic_moment"],
    "properties": {
      "name": {
        "type": "string",
        "enum": ["Al-doped_4H-SiC", "Al+V_Si_4H-SiC", "Al+V_C_4H-SiC"]
      },
      "total_magnetic_moment_per_supercell": {"type": "number", "unit": "μB"},
      "carbon_magnetic_moment": {"type": "number", "unit": "μB"}
    }
  }
}
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
- target_policy: threshold_or_better
- description: Magnetic moments per supercell and carbon atom contribution for the three doping configurations.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `name`, `total_magnetic_moment_per_supercell`, `carbon_magnetic_moment`
    - `properties`:
      - `name`:
        - `type`: string
        - `enum`: `Al-doped_4H-SiC`, `Al+V_Si_4H-SiC`, `Al+V_C_4H-SiC`
      - `total_magnetic_moment_per_supercell`:
        - `type`: number
        - `unit`: μB
      - `carbon_magnetic_moment`:
        - `type`: number
        - `unit`: μB

Notes: The hidden checker will compare the reported values to paper-referenced thresholds. The agent must compute the moments from the relaxed DFT outputs; the values are not provided in the public instruction.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "name",
            "total_magnetic_moment_per_supercell",
            "carbon_magnetic_moment"
          ],
          "properties": {
            "name": {
              "type": "string",
              "enum": [
                "Al-doped_4H-SiC",
                "Al+V_Si_4H-SiC",
                "Al+V_C_4H-SiC"
              ]
            },
            "total_magnetic_moment_per_supercell": {
              "type": "number",
              "unit": "μB"
            },
            "carbon_magnetic_moment": {
              "type": "number",
              "unit": "μB"
            }
          }
        }
      },
      "description": "Magnetic moments per supercell and carbon atom contribution for the three doping configurations."
    }
  ],
  "notes": "The hidden checker will compare the reported values to paper-referenced thresholds. The agent must compute the moments from the relaxed DFT outputs; the values are not provided in the public instruction."
}
```

## How you are scored
After you produce `/app/outputs/results.json`, a hidden verifier will read the file and compare the reported total magnetic moment and carbon magnetic moment for each system against reference thresholds that reflect the expected physical behavior. The verifier computes a per-configuration sub-reward and combines them into a final reward between 0 and 1. The exact tolerances and the weighting of each system are not disclosed. Only the content of `results.json` is scored; intermediate evidence files are not evaluated.
