# Layer-Resolved Magnetic Moments in Palladium Slabs from Self-Consistent Tight-Binding

## Problem background
Bulk palladium is paramagnetic, but thin films and slabs can exhibit magnetism due to reduced coordination and changes in the electronic density of states near the Fermi level. Understanding the thickness-dependent magnetic behavior of Pd is important for magnetic thin-film applications. This task addresses the onset of magnetism in Pd(001) slabs: you will compute the layer-resolved magnetic moments for slabs of 2, 3, 4, and 5 atomic layers within a self-consistent tight-binding model, using the unrestricted Hartree-Fock approximation and a specified exchange parameter.

## Approach
Use the real-space self-consistent tight-binding recursion method for a Hubbard Hamiltonian of d-electrons. The intra-atomic Coulomb and exchange interactions are treated in the unrestricted Hartree-Fock approximation with an exchange parameter J = 0.65 eV. The hopping integrals are taken from canonical d-band theory (Pettifor). The local spin-polarized density of states is obtained via the recursion method with eight levels of the continued fraction. The d-electron occupation is 9.4 e⁻/atom. The calculations are performed for Pd(001) slabs with 2, 3, 4, and 5 atomic layers; for each thickness, iterate to self-consistency and compute the magnetic moment (spin polarization) layer by layer.

## Reproduction target
Produce a CSV file containing the layer-resolved magnetic moments for Pd(001) slabs of 2, 3, 4, and 5 atomic layers, computed with the above method and parameters. The CSV must have columns: slab_layers (integer 2–5), layer_index (integer, 1-indexed from one surface to the other), and moment (float, in μB/atom). The file must contain complete sets of moments for all four slab thicknesses. The hidden verifier will compare your computed moments to a reference and verify that the moment profiles satisfy structural and symmetry constraints.

## Assets

- NumPy: pip install numpy
- SciPy: pip install scipy
- Canonical d-band hopping integrals (Pettifor)

## Workflow steps

### Step 1: Layer-resolved magnetic moments for Pd slabs
- Role: scored (load-bearing)
- Action: Implement the self-consistent tight-binding recursion method for a Hubbard Hamiltonian of d-electrons on Pd(001) slabs with 2, 3, 4, and 5 atomic layers. Use unrestricted Hartree–Fock approximation, exchange parameter J=0.65 eV, canonical d-band hopping integrals, d-electron count 9.4 e⁻/atom, and 8 levels of continued fraction. Compute layer-resolved magnetic moments (μB per atom) for each slab. Save results to magnetic_moments.csv.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: CSV with columns: slab_layers (int, 2-5), layer_index (int, 1-indexed from one surface to the other), moment (float, μB/atom). Four blocks, one per slab, each with as many rows as layers. Example: slab_layers=3, layer_index=1,2,3; moment values as computed.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Layer-resolved magnetic moments predicted by the agent for Pd slabs. The hidden checker compares each moment against the paper’s reported values with absolute tolerance and checks structural trends (e.g., center moment larger than surface for 3 layers, decreasing profile for 5 layers).
- schema:
  - `type`: table
  - `required_columns`: `slab_layers`, `layer_index`, `moment`
  - `units`:
    - `moment`: μB/atom

Notes: The checker performs T0 result‑level comparison: absolute deviation from the paper’s Table 1 within a tolerance, plus structural consistency checks. No external holdout labels are needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "slab_layers",
          "layer_index",
          "moment"
        ],
        "units": {
          "moment": "μB/atom"
        }
      },
      "description": "Layer-resolved magnetic moments predicted by the agent for Pd slabs. The hidden checker compares each moment against the paper’s reported values with absolute tolerance and checks structural trends (e.g., center moment larger than surface for 3 layers, decreasing profile for 5 layers)."
    }
  ],
  "notes": "The checker performs T0 result‑level comparison: absolute deviation from the paper’s Table 1 within a tolerance, plus structural consistency checks. No external holdout labels are needed."
}
```

## How you are scored
A hidden verifier independently scores your output artifact. It reads `magnetic_moments.csv` and compares each layer moment to a hidden reference value within an allowed tolerance. It also checks that the magnetic moment distribution across layers obeys expected physical trends (e.g., symmetry and thickness dependence). Full credit is awarded when all values meet the tolerance and all structural checks pass; partial credit may be granted for partial agreement. The final reward combines these checks into a single score in [0,1]. You do not need to match an exact table from any publication; the verifier uses its own reference.
