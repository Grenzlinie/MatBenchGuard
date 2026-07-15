# Band structure and transport validation for square planar thermoelectrics

## Problem background
Designing crystalline solids with a tailored electronic band structure is a fundamental challenge in materials science. For thermoelectric energy conversion, a so-called “pudding‑mold” band structure – one that contains both flat and dispersive regions – can lead to a high power factor. An inverse design strategy that combines materials database screening with structural and chemical attributes has been proposed to identify candidate compounds with this band shape. Two palladium oxide compounds, Ba<sub>2</sub>PdO<sub>3</sub> and La<sub>4</sub>PdO<sub>7</sub>, were highlighted through this approach. The goal of this task is to computationally validate whether these two compounds indeed possess the targeted pudding‑mold band structure and to evaluate their thermoelectric transport behavior.

## Approach
First‑principles electronic structure calculations are combined with semiclassical transport theory. Density functional theory (DFT) within the generalized gradient approximation is used to compute the band eigenvalues along high‑symmetry k‑paths for each compound. The thermoelectric power factor σS²/τ is then evaluated at 700 K using the constant relaxation‑time approximation as implemented in BoltzTraP2. To isolate the effect of band shape from the magnitude of the band gap, the computed band edges are rigidly shifted to the gap of a known reference compound, Bi<sub>2</sub>PdO<sub>4</sub> (1.41 eV). The resulting power factor curves are compared with those of Bi<sub>2</sub>PdO<sub>4</sub> to assess whether the new compounds exhibit competitive thermoelectric performance.

## Reproduction target
Produce electronic band structures along high‑symmetry paths for Ba<sub>2</sub>PdO<sub>3</sub> and La<sub>4</sub>PdO<sub>7</sub>, and compute their thermoelectric power factor (σS²/τ) as a function of carrier concentration at 700 K for both n‑type and p‑type doping. The primary questions to answer are: (1) do the band edges exhibit the pudding‑mold character, i.e., strong dispersion in one direction and flatness in perpendicular directions? (2) does the n‑type power factor reach values comparable to or exceeding that of the reference compound Bi<sub>2</sub>PdO<sub>4</sub> under comparable doping conditions? The required artifacts are band‑structure JSON files and a CSV file detailing the power factor for each compound and doping type.

## Assets

- Open Quantum Materials Database (OQMD): https://oqmd.org
- Quantum ESPRESSO: https://www.quantum-espresso.org
- BoltzTraP2: https://gitlab.com/sousaw/BoltzTraP2
- Python packages (pymatgen, ase, numpy, etc.): pymatgen, ase, numpy, matplotlib

## Workflow steps

### Step 1: Obtain crystal structures
- Role: process
- Action: Retrieve the crystal structures of Ba2PdO3 and La4PdO7 from the OQMD. Fetch atomic positions, lattice vectors, and space group information for each compound.
- Evidence: `/app/outputs/log_structure_retrieval.txt`

### Step 2: DFT band structure for Ba2PdO3
- Role: scored
- Action: Perform a GGA-DFT calculation for Ba2PdO3 using an open-source code. Converge a self-consistent field calculation, then compute the electronic band structure along a high-symmetry k-path. Output the band eigenvalues (eV) along the path as a JSON file, including the highest valence and lowest conduction bands.
- Output file: `/app/outputs/band_structure_Ba2PdO3.json`
- Format: json
- Contract: {
  "kpath": [{"label": "G", "k": [0,0,0]}, ...],
  "bands": [
    {
      "band_index": 0,
      "eigenvalues": [ ... ]  // energies in eV for each k-point
    },
    ...
  ]
}
- Scoring: scored by hidden verifier

### Step 3: DFT band structure for La4PdO7
- Role: scored
- Action: Perform the same GGA-DFT calculation as in step 2 for La4PdO7. Output the band eigenvalues as a JSON file.
- Output file: `/app/outputs/band_structure_La4PdO7.json`
- Format: json
- Contract: Same structure as band_structure_Ba2PdO3.json but for La4PdO7.
- Scoring: scored by hidden verifier

### Step 4: Electronic transport calculations
- Role: scored (load-bearing)
- Action: Using the constant relaxation time approximation as implemented in BoltzTraP2, compute the thermoelectric power factor sigma*S^2/tau at 700 K for n-type and p-type doping. Use the band structures from steps 2 and 3 and shift the band gap to 1.41 eV to isolate band-shape effects. Output a CSV file with columns: compound, doping_type, carrier_concentration_cm3, and sigmaS2_tau_W_mK2s, covering log-spaced concentrations from 1e19 to 1e22 cm^{-3}.
- Output file: `/app/outputs/pf_vs_doping.csv`
- Format: csv
- Contract: compound (string: Ba2PdO3 or La4PdO7),
  doping_type (string: n or p),
  carrier_concentration_cm3 (float),
  sigmaS2_tau_W_mK2s (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure_Ba2PdO3.json`
- `/app/outputs/band_structure_La4PdO7.json`
- `/app/outputs/pf_vs_doping.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure_Ba2PdO3.json
- path: `/app/outputs/band_structure_Ba2PdO3.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electronic band structure for Ba2PdO3. The checker verifies the presence of flat and dispersive regions consistent with a pudding-mold band.
- schema:
  - `type`: object
  - `required`:
    - `kpath`: array of objects (label, k [x,y,z])
    - `bands`: array of objects (band_index, eigenvalues array of floats in eV)

### band_structure_La4PdO7.json
- path: `/app/outputs/band_structure_La4PdO7.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electronic band structure for La4PdO7. The checker verifies the pudding-mold band shape.
- schema:
  - `type`: object
  - `required`:
    - `kpath`: array of objects (label, k [x,y,z])
    - `bands`: array of objects (band_index, eigenvalues array of floats in eV)

### pf_vs_doping.csv
- path: `/app/outputs/pf_vs_doping.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Thermoelectric power factor sigma*S^2/tau at 700 K as a function of carrier concentration. The checker extracts the maximum n-type value and compares to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `doping_type`, `carrier_concentration_cm3`, `sigmaS2_tau_W_mK2s`
  - `units`:
    - `carrier_concentration_cm3`: cm^{-3}
    - `sigmaS2_tau_W_mK2s`: W/(m·K^2·s)

Notes: The screener filters that identified Ba2PdO3 and La4PdO7 are assumed as given; only the band structure and transport validation of these two compounds is reproduced. All scored artifacts must be produced under /app/outputs. The band structure JSON must include k-path points and eigenvalues; the CSV must contain the specified columns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure_Ba2PdO3.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "kpath": "array of objects (label, k [x,y,z])",
          "bands": "array of objects (band_index, eigenvalues array of floats in eV)"
        }
      },
      "description": "Electronic band structure for Ba2PdO3. The checker verifies the presence of flat and dispersive regions consistent with a pudding-mold band."
    },
    {
      "file": "band_structure_La4PdO7.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "kpath": "array of objects (label, k [x,y,z])",
          "bands": "array of objects (band_index, eigenvalues array of floats in eV)"
        }
      },
      "description": "Electronic band structure for La4PdO7. The checker verifies the pudding-mold band shape."
    },
    {
      "file": "pf_vs_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "doping_type",
          "carrier_concentration_cm3",
          "sigmaS2_tau_W_mK2s"
        ],
        "units": {
          "carrier_concentration_cm3": "cm^{-3}",
          "sigmaS2_tau_W_mK2s": "W/(m·K^2·s)"
        }
      },
      "description": "Thermoelectric power factor sigma*S^2/tau at 700 K as a function of carrier concentration. The checker extracts the maximum n-type value and compares to hidden reference values."
    }
  ],
  "notes": "The screener filters that identified Ba2PdO3 and La4PdO7 are assumed as given; only the band structure and transport validation of these two compounds is reproduced. All scored artifacts must be produced under /app/outputs. The band structure JSON must include k-path points and eigenvalues; the CSV must contain the specified columns."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that inspects each scored artifact. The band‑structure JSON files will be checked for the presence of flat and dispersive regions using a structural‑audit procedure. The power‑factor CSV file will be analyzed to extract the maximum n‑type σS²/τ for each compound at 700 K; this value will be compared against hidden reference data derived from published results, with tolerances that account for differences in computational setup (pseudopotential, k‑point sampling, etc.). The final score is a weighted combination of the outcomes of these checks. Reporting the paper’s numbers without performing the actual calculations will not yield credit – the verifier assesses the data you produce, not the text you write.
