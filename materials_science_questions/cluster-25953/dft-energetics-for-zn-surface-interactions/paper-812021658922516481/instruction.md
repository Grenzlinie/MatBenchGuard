# DFT energetics for Zn-surface interactions

## Problem background
The nucleation and initial growth of ZnO films on Si substrates with Au nanocrystallites influence the polarity and defect distribution of the resulting films. First-principles density functional theory (DFT) can be used to model the adsorption of Zn and O atoms on an Au(111) surface and to compare the energies of different ZnO/Au(111) slab configurations, shedding light on the preferred atomic arrangements during early growth. Reproducing these DFT energetic orderings is a step toward understanding the role of Au nanocrystallites in controlling ZnO film polarity.

## Approach
The approach is to employ density functional theory (DFT) to model a seven-layer Au(111) slab. First, the slab is fully relaxed to obtain the equilibrium lattice constant and surface geometry. Then, two series of calculations are performed: (1) For each of the four high-symmetry adsorption sites (on-top, hcp, bridge, fcc), a monolayer of Zn atoms is placed on the Au surface and the total energy is computed after relaxing the adsorbate layer; the same process is repeated for a monolayer of O atoms. The resulting energies are sorted to obtain the adsorption site energy ordering. (2) Four ZnO/Au(111) slab configurations are constructed, corresponding to O-polar Zn-terminated (I), Zn-polar Zn-terminated (II), Zn-polar O-terminated (III), and O-polar O-terminated (IV) surfaces. After geometry relaxation, their total energies are computed and sorted to obtain the configuration energy ordering.

## Reproduction target
Compute, using first-principles DFT calculations, the relative energy ordering of Zn and O adsorption sites on Au(111) among the four candidate sites (on-top, hcp, bridge, fcc) and the relative total energy ordering of the four initial ZnO/Au(111) film configurations (I, II, III, IV). Report the two ordered lists in a JSON file.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP or GBRV): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Optimize Au(111) slab
- Role: process
- Action: Construct a seven-layer Au(111) slab and perform DFT geometry optimization to obtain the equilibrium lattice constant and relaxed surface structure. This slab serves as the substrate for all subsequent adsorption and configuration calculations.
- Evidence: `/app/outputs/slab_optimization.log`

### Step 2: Compute energy orderings
- Role: scored (load-bearing)
- Action: Using the optimized Au(111) slab, perform DFT calculations for two sets: (1) Place a monolayer of Zn atoms and, separately, a monolayer of O atoms on the four high-symmetry sites (on-top, hcp, bridge, fcc) and compute total energies; after relaxing the adsorbate layer, sort the site labels by increasing energy to produce the adsorption site energy ordering. (2) Construct four slab models with Zn and O layers arranged as configurations I (O-polar Zn-terminated), II (Zn-polar Zn-terminated), III (Zn-polar O-terminated), and IV (O-polar O-terminated) and compute total energies; after relaxation, sort the configuration labels by increasing energy to produce the configuration energy ordering. Write both orderings to dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: JSON object with keys: 'adsorption_site_energy_order' (array of strings, one of 'hcp','fcc','bridge','on-top'; sorted by increasing energy) and 'configuration_energy_order' (array of strings, 'I','II','III','IV'; sorted by increasing energy).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reproduces the paper's DFT energy ordering results: the most stable adsorption site for Zn/O on Au(111) (hcp) and the most stable initial ZnO configuration (Zn-polar O-terminated, configuration III).
- schema:
  - `type`: object
  - `required`:
    - `adsorption_site_energy_order`: array[string]
    - `configuration_energy_order`: array[string]
  - `items`:
    - `adsorption_site_energy_order`: string
    - `configuration_energy_order`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "adsorption_site_energy_order": "array[string]",
          "configuration_energy_order": "array[string]"
        },
        "items": {
          "adsorption_site_energy_order": "string",
          "configuration_energy_order": "string"
        }
      },
      "description": "Reproduces the paper's DFT energy ordering results: the most stable adsorption site for Zn/O on Au(111) (hcp) and the most stable initial ZnO configuration (Zn-polar O-terminated, configuration III)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your dft_results.json and compare the arrays 'adsorption_site_energy_order' and 'configuration_energy_order' against the reference orderings derived from the original DFT study. The scoring is exact match: full credit (1.0) is awarded if and only if both arrays match the hidden gold orderings; otherwise zero. The orderings reflect the paper-reported DFT energetic preferences; only the relative order matters, not the absolute energy values. Each workflow stage must be executed and the final scored file must be present at /app/outputs/dft_results.json.
