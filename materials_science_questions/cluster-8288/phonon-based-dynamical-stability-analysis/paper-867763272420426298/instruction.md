# Phonon stability, Peierls distortion, and electronic gaps of Te extreme nanowires in carbon nanotubes

## Problem background
Extreme nanowires (ENs) of tellurium encapsulated inside ultra-narrow single-walled carbon nanotubes (SWCNTs) with diameters between 0.7 and 1.1 nm present a fascinating example of low‑dimensional structural selectivity and electronic transitions. Under nanoconfinement, Te atoms can arrange as linear chains (LC), zigzag chains (ZZ), or 3‑fold helical coils (3H), and the preferred form depends on the encapsulating diameter. The mechanical stability of these structures and their possible Peierls distortion require quantitative computational assessment. The present task aims to computationally investigate the structural selectivity, mechanical stability, and electronic properties of these Te ENs across a range of encapsulating diameters, using a DFT workflow with Quantum ESPRESSO, an open‑source code.

## Approach
The reproduction is performed entirely with open‑source tools. SWCNT unit cells for the (5,5), (8,3), and (7,7) chiralities are constructed to represent the diameter range of interest. Initial atomic positions for the Te extreme nanowires are set up according to the linear chain, zigzag chain, and 3‑fold helix motifs, and both bare nanowire (vacuum) and encapsulated systems are built. All structures are relaxed using DFT with a Perdew–Burke–Ernzerhof (PBE) functional and standard pseudopotentials from the SSSP library. Phonon frequencies are evaluated via the finite‑displacement method to probe mechanical stability; the calculations are performed for the bare chains and for the encapsulated chains in the three representative SWCNTs. For the linear chain, a Peierls distortion scan is carried out by fixing the unit cell length while varying the bond‑length alternation, and the total energy is mapped as a function of the distortion. Electronic band gaps are extracted from the ground‑state electronic structure for the three encapsulated configurations. The workflow concludes by collecting all computed numbers into a structured JSON report.

## Reproduction target
Produce a single JSON file, `stability_results.json`, containing:
- Lists of phonon frequencies (in cm⁻¹ or THz) for LC in vacuum, LC encapsulated, ZZ in vacuum, ZZ encapsulated, and 3H encapsulated.
- The Peierls distortion curve for the LC: a set of bond‑length alternation (BLA) values (nm) and the corresponding total energy per Te atom (meV), as well as the equilibrium BLA and the associated energy gain.
- The electronic band gaps (in eV) for the encapsulated LC, ZZ, and 3H systems.
The file must follow the exact JSON schema provided in the structured output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE) v1.3.0: https://www.materialscloud.org/discover/sssp/table/efficiency
- TubeGen/GenCNT for CNT coordinates: https://tubenet.tec.nagoya-u.ac.jp/tubegen/tubeGen.cgi

## Workflow steps

### Step 1: Generate initial atomic structures
- Role: process
- Action: Generate unit cells for (5,5), (8,3), and (7,7) SWCNTs and construct initial Te atomic positions for linear chain (LC), zigzag chain (ZZ), and 3-fold helical coil (3H) motifs. Build both bare extreme nanowire (vacuum) and encapsulated systems, saving them in a suitable format for DFT input.
- Evidence: none

### Step 2: Relax all structures
- Role: process
- Action: For each system (LC in vacuum, LC encapsulated, ZZ in vacuum, ZZ encapsulated, 3H encapsulated), perform DFT geometry optimization using Quantum ESPRESSO pw.x. Relax atomic positions while keeping unit cell dimensions fixed for the encapsulated systems. Save output logs and relaxed structures.
- Evidence: none

### Step 3: Compute phonon frequencies
- Role: process
- Action: For each relaxed structure, compute phonon frequencies at the Gamma point (or along a high-symmetry path) using the finite-displacement method with Quantum ESPRESSO ph.x. Record all phonon frequencies for each system.
- Evidence: `/app/outputs/phonon_freqs_raw.dat`

### Step 4: Compute Peierls distortion curve for LC
- Role: process
- Action: For the linear chain in vacuum and inside a (5,5) SWCNT, construct a series of unit cells with varying bond-length alternation (BLA). For each BLA, fix the unit cell length and compute the DFT total energy with pw.x. Record the energy vs BLA data.
- Evidence: `/app/outputs/peierls_energy_vs_bla.dat`

### Step 5: Compute electronic band gaps
- Role: process
- Action: For the encapsulated LC, ZZ, and 3H structures, perform a DFT calculation (scf or nscf) to obtain the electronic density of states or band structure, and extract the fundamental band gap (in eV) for each system.
- Evidence: `/app/outputs/band_gaps.dat`

### Step 6: Compile final report
- Role: scored (load-bearing)
- Action: Collect all computed results: the phonon frequency lists for each system, the Peierls distortion curve data, and the extracted band gaps. Write a single JSON file containing all numerical results in the required format.
- Output file: `/app/outputs/stability_results.json`
- Format: json
- Contract: {"type":"object","required":["LC_vac_phonon_freqs","LC_enc_phonon_freqs","ZZ_vac_phonon_freqs","ZZ_enc_phonon_freqs","3H_enc_phonon_freqs","LC_PD_curve","LC_PD_equilibrium_BLA_nm","LC_PD_energy_gain_meV","band_gap_LC_eV","band_gap_ZZ_eV","band_gap_3H_eV"],"properties":{"LC_vac_phonon_freqs":{"type":"array","items":{"type":"number"}},"LC_enc_phonon_freqs":{"type":"array","items":{"type":"number"}},"ZZ_vac_phonon_freqs":{"type":"array","items":{"type":"number"}},"ZZ_enc_phonon_freqs":{"type":"array","items":{"type":"number"}},"3H_enc_phonon_freqs":{"type":"array","items":{"type":"number"}},"LC_PD_curve":{"type":"object","required":["BLA_nm","energy_meV_per_Te"],"properties":{"BLA_nm":{"type":"array","items":{"type":"number"}},"energy_meV_per_Te":{"type":"array","items":{"type":"number"}}}},"LC_PD_equilibrium_BLA_nm":{"type":"number"},"LC_PD_energy_gain_meV":{"type":"number"},"band_gap_LC_eV":{"type":"number"},"band_gap_ZZ_eV":{"type":"number"},"band_gap_3H_eV":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stability_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stability_results.json
- path: `/app/outputs/stability_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Consolidated results for phonon stability, Peierls distortion, and electronic band gaps.
- schema:
  - `type`: object
  - `required`: `LC_vac_phonon_freqs`, `LC_enc_phonon_freqs`, `ZZ_vac_phonon_freqs`, `ZZ_enc_phonon_freqs`, `3H_enc_phonon_freqs`, `LC_PD_curve`, `LC_PD_equilibrium_BLA_nm`, `LC_PD_energy_gain_meV`, `band_gap_LC_eV`, `band_gap_ZZ_eV`, `band_gap_3H_eV`
  - `properties`:
    - `LC_vac_phonon_freqs`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Phonon frequencies (cm⁻¹ or THz) for LC in vacuum
    - `LC_enc_phonon_freqs`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Phonon frequencies for encapsulated LC
    - `ZZ_vac_phonon_freqs`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Phonon frequencies for ZZ in vacuum
    - `ZZ_enc_phonon_freqs`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Phonon frequencies for encapsulated ZZ
    - `3H_enc_phonon_freqs`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Phonon frequencies for encapsulated 3H
    - `LC_PD_curve`:
      - `type`: object
      - `required`: `BLA_nm`, `energy_meV_per_Te`
      - `properties`:
        - `BLA_nm`:
          - `type`: array
          - `items`:
            - `type`: number
          - `description`: Bond-length alternation values in nm
        - `energy_meV_per_Te`:
          - `type`: array
          - `items`:
            - `type`: number
          - `description`: Total energy per Te atom (meV) for each BLA
    - `LC_PD_equilibrium_BLA_nm`:
      - `type`: number
      - `description`: Equilibrium BLA from the Peierls curve
    - `LC_PD_energy_gain_meV`:
      - `type`: number
      - `description`: Energy gain per Te atom due to Peierls distortion (meV)
    - `band_gap_LC_eV`:
      - `type`: number
      - `description`: Electronic band gap of encapsulated LC (eV)
    - `band_gap_ZZ_eV`:
      - `type`: number
      - `description`: Electronic band gap of encapsulated ZZ (eV)
    - `band_gap_3H_eV`:
      - `type`: number
      - `description`: Electronic band gap of encapsulated 3H (eV)

Notes: All frequency lists are numeric arrays; units may be cm⁻¹ or THz, but must be consistent within each list. The Peierls curve object must have equal-length arrays for BLA_nm and energy_meV_per_Te. The equilibrium BLA and energy gain are single numeric values. Band gaps are floats in eV. The checker will apply tolerance-based comparisons and will not require exact numerical agreement with a specific reference; results that satisfy the qualitative physical criteria will score fully.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stability_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "LC_vac_phonon_freqs",
          "LC_enc_phonon_freqs",
          "ZZ_vac_phonon_freqs",
          "ZZ_enc_phonon_freqs",
          "3H_enc_phonon_freqs",
          "LC_PD_curve",
          "LC_PD_equilibrium_BLA_nm",
          "LC_PD_energy_gain_meV",
          "band_gap_LC_eV",
          "band_gap_ZZ_eV",
          "band_gap_3H_eV"
        ],
        "properties": {
          "LC_vac_phonon_freqs": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Phonon frequencies (cm⁻¹ or THz) for LC in vacuum"
          },
          "LC_enc_phonon_freqs": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Phonon frequencies for encapsulated LC"
          },
          "ZZ_vac_phonon_freqs": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Phonon frequencies for ZZ in vacuum"
          },
          "ZZ_enc_phonon_freqs": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Phonon frequencies for encapsulated ZZ"
          },
          "3H_enc_phonon_freqs": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Phonon frequencies for encapsulated 3H"
          },
          "LC_PD_curve": {
            "type": "object",
            "required": [
              "BLA_nm",
              "energy_meV_per_Te"
            ],
            "properties": {
              "BLA_nm": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "description": "Bond-length alternation values in nm"
              },
              "energy_meV_per_Te": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "description": "Total energy per Te atom (meV) for each BLA"
              }
            }
          },
          "LC_PD_equilibrium_BLA_nm": {
            "type": "number",
            "description": "Equilibrium BLA from the Peierls curve"
          },
          "LC_PD_energy_gain_meV": {
            "type": "number",
            "description": "Energy gain per Te atom due to Peierls distortion (meV)"
          },
          "band_gap_LC_eV": {
            "type": "number",
            "description": "Electronic band gap of encapsulated LC (eV)"
          },
          "band_gap_ZZ_eV": {
            "type": "number",
            "description": "Electronic band gap of encapsulated ZZ (eV)"
          },
          "band_gap_3H_eV": {
            "type": "number",
            "description": "Electronic band gap of encapsulated 3H (eV)"
          }
        }
      },
      "description": "Consolidated results for phonon stability, Peierls distortion, and electronic band gaps."
    }
  ],
  "notes": "All frequency lists are numeric arrays; units may be cm⁻¹ or THz, but must be consistent within each list. The Peierls curve object must have equal-length arrays for BLA_nm and energy_meV_per_Te. The equilibrium BLA and energy gain are single numeric values. Band gaps are floats in eV. The checker will apply tolerance-based comparisons and will not require exact numerical agreement with a specific reference; results that satisfy the qualitative physical criteria will score fully."
}
```

## How you are scored
The verifier inspects the submitted `stability_results.json` and assigns a reward based on three separate checks:
1. Phonon stability: the phonon frequency lists are evaluated against hidden criteria to assess whether each structure is mechanically stable.
2. Peierls distortion: the reported Peierls curve is analysed to determine whether it describes a physically plausible Peierls‑distorted linear chain.
3. Electronic gaps: the band gap values are compared against hidden thresholds to capture the electronic character of each structure.
Each check contributes a fraction of the total reward; the exact thresholds and reference values are hidden, and the reward is monotonic in the quality of the reproduction. A structurally correct JSON file that passes all shape checks is a prerequisite, but the score is determined solely by the numerical agreement with the expected physical picture.
