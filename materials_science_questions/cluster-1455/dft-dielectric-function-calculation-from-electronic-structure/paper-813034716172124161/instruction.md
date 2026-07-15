# Compute absorption spectra of C60 aggregates from real-frequency polarizability via Clausius-Mossotti and Kramers-Kronig

## Problem background
C60 fullerenes and their derivatives are widely used as electron acceptors and transport layers in organic and perovskite solar cells. The optical absorption of C60 in its molecular and aggregated (solid) states is important for understanding light harvesting and charge generation, but computing it accurately is challenging. Standard computational methods like time-dependent density functional theory (TD-DFT) and the dipole approximation (using the imaginary part of the dielectric function) are known to be highly sensitive to the choice of exchange-correlation functional and can predict unrealistically large spectral shifts when molecules aggregate. There is a need for alternative computational approaches that can model aggregation effects more reliably and with less dependence on the underlying functional.

## Approach
This task reproduces an alternative computational pipeline that bypasses TD-DFT and the direct dipole approximation. The key idea is to first compute the frequency-dependent real molecular polarizability α(ω) for C60 molecules using density functional theory (DFT). Two different exchange-correlation functionals (PBE and B3LYP) will be used to examine the method’s sensitivity. The real polarizability is then inserted into the Clausius-Mossotti relation (which relates the macroscopic dielectric constant to the molecular polarizability and number density) to obtain the real part of the dielectric function ε_r(ω). The imaginary part ε_i(ω) is obtained from ε_r(ω) via the Kramers-Kronig transform, and the molar absorptivity spectrum is calculated from both ε_r and ε_i using a standard relation. The approach is applied to an isolated C60 molecule (monomer) and to a dimer (two molecules at the distance of nearest neighbours in the crystal) to study how aggregation alters the spectrum. By comparing spectra computed with PBE and B3LYP for the monomer, one can assess the functional sensitivity of this polarizability-based route.

## Reproduction target
The goal is to produce the following four scored artifacts:
1. Absorption spectrum of the C60 monomer computed from PBE polarizability, covering the energy range 1–6 eV.
2. Absorption spectrum of the C60 monomer computed from B3LYP polarizability, in the same format.
3. Absorption spectrum of the C60 dimer computed from PBE polarizability.
4. A summary file containing the first major absorption peak energy for each of the three spectra, whether a shoulder feature (a secondary peak) appears in the dimer spectrum and at what energy, and the percentage difference between the two monomer peak energies (a measure of functional sensitivity).
The spectra should be derived by the polarizability → Clausius-Mossotti → Kramers-Kronig pipeline, and the resulting peak positions and spectral shape are the primary subjects of reproduction.

## Assets

- C60 crystal structure coordinates: 10.1038/353147a0
- NWChem: https://github.com/nwchemgit/nwchem
- Atomic Simulation Environment (ASE): ase
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare C60 monomer geometry
- Role: process
- Action: Obtain a C60 monomer geometry: either from a public molecular database or built from the known icosahedral structure; optionally optimize geometry at the DFT/PBE level using NWChem to match the paper's approach.
- Evidence: `/app/outputs/monomer.xyz`

### Step 2: Construct C60 dimer geometry
- Role: process
- Action: Construct a C60 dimer: take two copies of the monomer geometry and place them with a centre-of-mass separation of approximately 13.8 Å and relative orientation matching the nearest-neighbour packing in the fcc C60 crystal.
- Evidence: `/app/outputs/dimer.xyz`

### Step 3: Compute frequency-dependent polarizability α(ω)
- Role: process
- Action: Using NWChem, compute the real part of the frequency-dependent molecular polarizability α(ω) for: (a) C60 monomer with PBE, (b) C60 monomer with B3LYP, (c) C60 dimer with PBE. Perform calculations at frequencies covering 1–6 eV with a fine grid. Save α values to CSV files.
- Evidence: `/app/outputs/alpha_monomer_pbe.csv`

### Step 4: Compute absorption spectrum for monomer (PBE)
- Role: scored (load-bearing)
- Action: From the α(ω) data for monomer (PBE), compute the real dielectric function ε_r(ω) via the Clausius-Mossotti relation using the C60 crystal number density. Apply Kramers-Kronig transform to obtain ε_i(ω). Compute molar absorptivity Mμ(ω) using Eq. (7) of the paper. Output a JSON array of objects (each with energy_ev, epsilon_r, epsilon_i, absorption) for energies from 1.0 to 6.0 eV in steps of at most 0.1 eV.
- Output file: `/app/outputs/monomer_pbe_spectrum.json`
- Format: json
- Contract: array of objects: { energy_ev: float, epsilon_r: float, epsilon_i: float, absorption: float }
- Scoring: scored by hidden verifier

### Step 5: Compute absorption spectrum for monomer (B3LYP)
- Role: scored (load-bearing)
- Action: From the α(ω) data for monomer (B3LYP), repeat the same procedure as in step3 to obtain the absorption spectrum. Output the same JSON format.
- Output file: `/app/outputs/monomer_b3lyp_spectrum.json`
- Format: json
- Contract: array of objects: { energy_ev: float, epsilon_r: float, epsilon_i: float, absorption: float }
- Scoring: scored by hidden verifier

### Step 6: Compute absorption spectrum for dimer (PBE)
- Role: scored (load-bearing)
- Action: From the α(ω) data for dimer (PBE), repeat the procedure to obtain the absorption spectrum. Output JSON.
- Output file: `/app/outputs/dimer_pbe_spectrum.json`
- Format: json
- Contract: array of objects: { energy_ev: float, epsilon_r: float, epsilon_i: float, absorption: float }
- Scoring: scored by hidden verifier

### Step 7: Extract peak positions and compute functional sensitivity
- Role: scored (load-bearing)
- Action: From the three absorption spectra, identify the first major absorption peak (local maximum of absorption above 2 eV) for each system. For the dimer spectrum, check for a shoulder (local maximum between 2.55 and 2.95 eV with absorption ≥ 10% of the main peak). Compute functional sensitivity percentage = 100 * |E_peak(PBE) – E_peak(B3LYP)| / average of the two peak energies. Output a JSON object with keys: monomer_pbe_peak1_ev, monomer_b3lyp_peak1_ev, dimer_pbe_peak1_ev, shoulder_energy_ev (or null), functional_sensitivity_percent.
- Output file: `/app/outputs/results_summary.json`
- Format: json
- Contract: object: { monomer_pbe_peak1_ev: float, monomer_b3lyp_peak1_ev: float, dimer_pbe_peak1_ev: float, shoulder_energy_ev: float|null, functional_sensitivity_percent: float }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monomer_pbe_spectrum.json`
- `/app/outputs/monomer_b3lyp_spectrum.json`
- `/app/outputs/dimer_pbe_spectrum.json`
- `/app/outputs/results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monomer_pbe_spectrum.json
- path: `/app/outputs/monomer_pbe_spectrum.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Absorption spectrum of C60 monomer computed from PBE polarizability; array of points covering 1–6 eV with ≤0.1 eV spacing.
- schema:
  - `type`: array
  - `items`:
    - `energy_ev`: float
    - `epsilon_r`: float
    - `epsilon_i`: float
    - `absorption`: float
  - `required`: `energy_ev`, `epsilon_r`, `epsilon_i`, `absorption`

### monomer_b3lyp_spectrum.json
- path: `/app/outputs/monomer_b3lyp_spectrum.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Absorption spectrum of C60 monomer computed from B3LYP polarizability; same format as monomer_pbe_spectrum.json.
- schema:
  - `type`: array
  - `items`:
    - `energy_ev`: float
    - `epsilon_r`: float
    - `epsilon_i`: float
    - `absorption`: float
  - `required`: `energy_ev`, `epsilon_r`, `epsilon_i`, `absorption`

### dimer_pbe_spectrum.json
- path: `/app/outputs/dimer_pbe_spectrum.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Absorption spectrum of C60 dimer computed from PBE polarizability; used for aggregation effect analysis.
- schema:
  - `type`: array
  - `items`:
    - `energy_ev`: float
    - `epsilon_r`: float
    - `epsilon_i`: float
    - `absorption`: float
  - `required`: `energy_ev`, `epsilon_r`, `epsilon_i`, `absorption`

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Summary of extracted peak energies, shoulder detection, and functional sensitivity; cross-validated against raw spectra by the checker.
- schema:
  - `type`: object
  - `required`: `monomer_pbe_peak1_ev`, `monomer_b3lyp_peak1_ev`, `dimer_pbe_peak1_ev`, `shoulder_energy_ev`, `functional_sensitivity_percent`
  - `properties`:
    - `monomer_pbe_peak1_ev`: float
    - `monomer_b3lyp_peak1_ev`: float
    - `dimer_pbe_peak1_ev`: float
    - `shoulder_energy_ev`: float|null
    - `functional_sensitivity_percent`: float

Notes: The raw spectra are the primary scored artifacts; the checker will extract peak positions and compute functional sensitivity from them. The summary file is provided for convenience and will be cross-checked against the recomputed values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monomer_pbe_spectrum.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "energy_ev": "float",
          "epsilon_r": "float",
          "epsilon_i": "float",
          "absorption": "float"
        },
        "required": [
          "energy_ev",
          "epsilon_r",
          "epsilon_i",
          "absorption"
        ]
      },
      "description": "Absorption spectrum of C60 monomer computed from PBE polarizability; array of points covering 1–6 eV with ≤0.1 eV spacing."
    },
    {
      "file": "monomer_b3lyp_spectrum.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "energy_ev": "float",
          "epsilon_r": "float",
          "epsilon_i": "float",
          "absorption": "float"
        },
        "required": [
          "energy_ev",
          "epsilon_r",
          "epsilon_i",
          "absorption"
        ]
      },
      "description": "Absorption spectrum of C60 monomer computed from B3LYP polarizability; same format as monomer_pbe_spectrum.json."
    },
    {
      "file": "dimer_pbe_spectrum.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "energy_ev": "float",
          "epsilon_r": "float",
          "epsilon_i": "float",
          "absorption": "float"
        },
        "required": [
          "energy_ev",
          "epsilon_r",
          "epsilon_i",
          "absorption"
        ]
      },
      "description": "Absorption spectrum of C60 dimer computed from PBE polarizability; used for aggregation effect analysis."
    },
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "monomer_pbe_peak1_ev",
          "monomer_b3lyp_peak1_ev",
          "dimer_pbe_peak1_ev",
          "shoulder_energy_ev",
          "functional_sensitivity_percent"
        ],
        "properties": {
          "monomer_pbe_peak1_ev": "float",
          "monomer_b3lyp_peak1_ev": "float",
          "dimer_pbe_peak1_ev": "float",
          "shoulder_energy_ev": "float|null",
          "functional_sensitivity_percent": "float"
        }
      },
      "description": "Summary of extracted peak energies, shoulder detection, and functional sensitivity; cross-validated against raw spectra by the checker."
    }
  ],
  "notes": "The raw spectra are the primary scored artifacts; the checker will extract peak positions and compute functional sensitivity from them. The summary file is provided for convenience and will be cross-checked against the recomputed values."
}
```

## How you are scored
Each of the four scored output files will be inspected by a hidden verifier. The verifier reads the raw spectrum JSON arrays, identifies the first dominant absorption peak in each, scans the dimer spectrum for a shoulder feature within a specified energy window, and computes the functional sensitivity from the monomer peak energies. These extracted quantities are compared against hidden reference values (obtained from the original study) with appropriate tolerances. The summary file is cross-checked against the values derived directly from the spectra. The overall reward is a weighted combination of the per-artifact scores: the three spectrum files and the summary each contribute a share, with the monomer and dimer PBE spectra carrying the largest weight. Simply reporting numbers that match the reference without genuine computation of the polarizability and dielectric function will not suffice; the verifier’s recomputation from the raw spectral data ensures that the reported artifacts must be internally consistent.
