# Li-ion migration barriers in VS2 from DFT-NEB calculations

## Problem background
Transition metal dichalcogenides (TMDs) such as VS₂ are attractive anode materials for lithium-ion batteries due to their layered structure and high theoretical capacity. The interlayer spacing of VS₂ strongly influences the kinetics of Li-ion diffusion, which is a key factor for rate capability. This task reproduces density functional theory (DFT) and climbing-image nudged elastic band (CI-NEB) calculations that investigate Li-ion migration energy barriers in VS₂ at different interlayer spacings. Understanding these barriers helps assess the potential of expanded interlayer structures for fast Li-ion transport.

## Approach
The calculations are performed using spin-polarized DFT with the generalized gradient approximation (GGA) in the Perdew-Burke-Ernzerhof (PBE) form and the DFT-D2 van der Waals correction. Two model systems are used: a 3×3×2 supercell of VS₂ (trigonal P-3m1, lattice parameters a=b=3.221 Å, c=5.755 Å) to represent the bulk-like interlayer spacing (~5.736 Å), and a 3×3×1 monolayer with a vacuum layer of 20 Å to model the expanded interlayer limit. The workflow consists of geometry optimization of the host structures, identification of stable Li adsorption sites by computing binding energies, and finally CI-NEB calculations of Li migration barriers along several diffusion paths (O–T and O–O′ in the supercell; T–H, T–T′, and H–H′ on the monolayer). The rate-determining activation energy is extracted for each system.

## Reproduction target
Compute the rate-determining Li-ion migration activation energy (in eV) for the VS₂ supercell and for the VS₂ monolayer. Report the results in a JSON file named `activation_energies.json` with keys `supercell_barrier_eV` and `monolayer_barrier_eV`.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP efficiency): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: VS2 structure optimization
- Role: process
- Action: Construct a 3×3×2 supercell of VS₂ (trigonal Pm1, lattice a=b=3.221 Å, c=5.755 Å) and a 3×3×1 monolayer with 20 Å vacuum. Perform spin-polarized DFT geometry optimization using GGA-PBE functional with DFT-D2 van der Waals correction until forces are converged.
- Evidence: none

### Step 2: Li adsorption site identification
- Role: process
- Action: Place a Li atom at candidate interstitial sites: octahedral (O) and tetrahedral (T) sites in the supercell; on top of V (T_V) and hollow center of S (H_center) sites on the monolayer. Compute binding energies using single-point DFT to determine the most stable adsorption positions.
- Evidence: none

### Step 3: NEB diffusion barrier calculation
- Role: scored (load-bearing)
- Action: Using the optimized structures and identified Li sites, compute Li migration barriers with climbing-image nudged elastic band (CI-NEB). Evaluate paths: O–T and O–O′ in the supercell; T–H, T–T′, and H–H′ on the monolayer. Extract the rate-determining activation energies (highest barrier along each complete path) and write them to activation_energies.json as floats with keys 'supercell_barrier_eV' and 'monolayer_barrier_eV'.
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: {"supercell_barrier_eV": "float", "monolayer_barrier_eV": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Li-ion migration activation energies (eV) for VS₂ supercell (interlayer ~5.736 Å) and VS₂ monolayer (expanded interlayer limit).
- schema:
  - `type`: object
  - `required`:
    - `supercell_barrier_eV`: number
    - `monolayer_barrier_eV`: number
  - `description`: Key-value pairs of the migration energy barrier in eV.

Notes: The agent must perform the full DFT-NEB pipeline. The reported values are compared to paper gold within a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "supercell_barrier_eV": "number",
          "monolayer_barrier_eV": "number"
        },
        "description": "Key-value pairs of the migration energy barrier in eV."
      },
      "description": "Computed Li-ion migration activation energies (eV) for VS₂ supercell (interlayer ~5.736 Å) and VS₂ monolayer (expanded interlayer limit)."
    }
  ],
  "notes": "The agent must perform the full DFT-NEB pipeline. The reported values are compared to paper gold within a hidden tolerance."
}
```

## How you are scored
A hidden verifier reads your `activation_energies.json` and extracts the two barrier values. Each barrier is compared to the expected value for that system. Full credit is awarded if both values fall within a hidden tolerance of the correct results. The final score is the average of the two individual scores (equal weight). No other artifacts are scored.
