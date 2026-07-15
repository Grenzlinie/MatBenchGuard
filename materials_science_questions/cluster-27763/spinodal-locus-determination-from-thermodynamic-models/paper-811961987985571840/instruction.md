# SCFT Phase Diagram of Reversibly Bonding Triblock Blends

## Problem background
A melt blend of monofunctional A and difunctional B homopolymers that can reversibly bond only between dissimilar groups forms supramolecular AB diblock and ABA triblock copolymers. The architecture of these copolymers depends on the ratio of the homopolymer chain lengths. Using self-consistent field theory (SCFT), one can explore how this architectural control, together with the bonding strength and the segmental incompatibility, determines the stability of ordered mesophases (lamellar, hexagonal, inverted hexagonal) versus the disordered homogeneous phase. The task is to compute the order–disorder melting envelope (the boundary at which the ordered phases give way to disorder) and identify which mesophase is stable at each composition and temperature for a particular set of parameters where symmetric triblocks and asymmetric diblocks are formed. The expected structure of the phase diagram is an interesting open question.

## Approach
The system is treated within a grand-canonical SCFT framework that accounts for four species (A and B homopolymers, AB diblocks, and ABA triblocks) whose concentrations are linked by mass-action constraints for the reversible bonding reactions. The free energy per chain is expressed in terms of segmental density fields and conjugate chemical potential fields, with incompressibility enforced by a pressure field. For a given total A-segment composition and inverse temperature, modified diffusion equations are solved pseudo-spectrally for candidate phases (disordered, lamellar, hexagonal, inverted hexagonal) in a unit cell. The unit cell size and shape are optimized to minimize the grand potential via a variable-cell-shape method. The phase with the lowest grand potential per chain at each thermodynamic condition is the equilibrium phase. By repeating this calculation over a grid of compositions and temperatures, the complete order–disorder envelope and the sequence of stable mesophases are obtained.

## Reproduction target
For the supramolecular triblock blend with total polymerization N=300, normalized bond strength h/(χN)=0.627086, and homopolymer length ratio such that the B homopolymer is twice as long as the A homopolymer (α_Ah=1/4), determine the stable mesophase at each point on a grid of total A-segment volume fractions φ_A,tot ∈ [0.15, 0.85] (step 0.05) and inverse temperatures χN ∈ [12, 20] (step fine enough to capture transitions). For every (φ_A,tot, χN) point, solve the SCFT equations for the four candidate phases (Dis, Lam, Hex, Hex_II), compute their grand potential per chain, and identify the equilibrium phase as the one with the lowest grand potential. Produce two scored outputs: a CSV table listing the stable phase at each grid point, and a JSON file containing the grand potential values for all four phases at every point. From these, the order–disorder boundary can be extracted.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run SCFT grand potential sweeps
- Role: process
- Action: Implement the grand-canonical SCFT model for the supramolecular triblock blend with reference polymerization N=300, normalized bond strength h/(χN)=0.627086, and homopolymer length ratio α_Ah=1/4. Set up a grid of total A-segment volume fractions φ_A,tot from 0.15 to 0.85 with step 0.05 and inverse temperatures χN from 12 to 20 with a step fine enough to resolve order-disorder transitions. For each (φ_A,tot, χN) point, solve the SCFT equations for the four candidate phases: disordered, lamellar, hexagonal, and inverted hexagonal. Use a pseudo-spectral operator-splitting scheme to solve the modified diffusion equations; optimize the unit cell size and shape via the variable-cell-shape method to minimize the grand potential. Compute the final grand potential per chain for each phase. Save the complete raw data to grand_potentials_raw.json.
- Evidence: `/app/outputs/grand_potentials_raw.json`

### Step 2: Compile stable phases
- Role: scored
- Action: From the raw grand potentials file, determine for each grid point the phase with the lowest grand potential. In case of ties, prefer an ordered phase over disordered. Save the stable phase for every grid point as step_01_stable_phases.csv.
- Output file: `/app/outputs/step_01_stable_phases.csv`
- Format: csv
- Contract: Columns: phi_A_tot (float, total A volume fraction), chiN (float, inverse temperature), phase (string one of Dis, Lam, Hex, Hex_II). The row list covers all (phi_A_tot, chiN) grid points.
- Scoring: scored by hidden verifier

### Step 3: Export grand potential data for checker
- Role: scored (load-bearing)
- Action: Reformat the raw grand potentials into a JSON object: keys are stringified (φ_A,tot, χN) pairs (e.g., "(0.3,15.0)") and values are objects with keys 'Dis', 'Lam', 'Hex', 'Hex_II' mapping to the computed grand potential value. Save as step_02_grand_potentials.json.
- Output file: `/app/outputs/step_02_grand_potentials.json`
- Format: json
- Contract: JSON object. Each key is a string like "(0.3,15.0)"; the corresponding value is an object with keys "Dis", "Lam", "Hex", "Hex_II" and float values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stable_phases.csv`
- `/app/outputs/step_02_grand_potentials.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stable_phases.csv
- path: `/app/outputs/step_01_stable_phases.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Equilibrium phase at each grid point; checked for internal consistency with the recomputed phases from the grand potential data.
- schema:
  - `type`: table
  - `required_columns`: `phi_A_tot`, `chiN`, `phase`
  - `columns`:
    - `phi_A_tot`: float
    - `chiN`: float
    - `phase`: string

### step_02_grand_potentials.json
- path: `/app/outputs/step_02_grand_potentials.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Grand potential per chain for each phase at each grid point. The checker recomputes the stable phase and compares the resulting order-disorder envelope shape with a hidden digitized reference from the paper.
- schema:
  - `type`: object
  - `keys`: stringified (phi_A_tot, chiN)
  - `values`:
    - `type`: object
    - `required_keys`: `Dis`, `Lam`, `Hex`, `Hex_II`
    - `value_type`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stable_phases.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_A_tot",
          "chiN",
          "phase"
        ],
        "columns": {
          "phi_A_tot": "float",
          "chiN": "float",
          "phase": "string"
        }
      },
      "description": "Equilibrium phase at each grid point; checked for internal consistency with the recomputed phases from the grand potential data."
    },
    {
      "file": "step_02_grand_potentials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "keys": "stringified (phi_A_tot, chiN)",
        "values": {
          "type": "object",
          "required_keys": [
            "Dis",
            "Lam",
            "Hex",
            "Hex_II"
          ],
          "value_type": "float"
        }
      },
      "description": "Grand potential per chain for each phase at each grid point. The checker recomputes the stable phase and compares the resulting order-disorder envelope shape with a hidden digitized reference from the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads the JSON file with grand potentials, recomputes the stable phase at each grid point by picking the phase with the lowest grand potential (preferring any ordered phase over disordered in ties), and compares the resulting order–disorder envelope to a reference derived from published results. The reward is based mainly on how well the envelope shape agrees with the reference, including the number and locations of lobes, the position of the eutectic minimum, and the dominant ordered phases in each lobe. The verifier also checks that the CSV file is consistent with the recomputed phases. Because a re‑implementation may differ in numerical details, the comparison uses tolerances that account for legitimate spread; a correct physical solution should score well.
