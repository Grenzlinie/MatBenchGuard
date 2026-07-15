# Graphite (0001) surface electronic structure: corrugation and symmetry analysis from DFT slab calculations

## Problem background
The (0001) surface of graphite, when imaged with a scanning tunneling microscope (STM), displays an unexpectedly large corrugation—height variations of several ångströms across the surface lattice—and a striking absence of the three-fold trigonal symmetry expected from the atomic arrangement. The origin of these observations is not explained by simple considerations of the surface atomic structure alone. Electronic structure effects and the stacking registry of the topmost layers may play a crucial role. This task investigates whether the stacking configuration of the top graphite layer can account for the observed corrugation and the breaking of trigonal symmetry by comparing the electronic properties of two competing slab models through first-principles calculations.

## Approach
The approach is to perform density-functional theory (DFT) calculations on two three-layer graphite slab models: one with the ideal AB (Bernal) stacking and another in which the topmost carbon layer is slipped by half the in-plane lattice vector, yielding a local AA-like stacking at the surface. From the self-consistent charge density and the local density of states at the Fermi level, we simulate constant-current STM images using the Tersoff-Hamann approximation. For each configuration we then quantify (i) the corrugation amplitude—the peak-to-peak height variation in the simulated STM image—and (ii) a metric of trigonal symmetry, derived from the relative strength of the three-fold symmetric Fourier components compared to the one-fold component. The comparison between the two slab models reveals whether a slipped top layer can simultaneously produce larger corrugation and a weaker three-fold symmetry.

## Reproduction target
Construct the two slab models, run self-consistent DFT electronic-structure calculations, and post-process the resulting charge density and local density of states (LDOS) to simulate constant-current STM images. For each slab configuration compute:
- **corrugation_angstrom**: the corrugation amplitude (in Å),
- **trigonal_symmetry_metric**: a metric that quantifies the degree of three-fold trigonal symmetry (for example, the ratio of the amplitude of the three-fold Fourier component to that of the one-fold component; lower values indicate weaker trigonal symmetry).
Write the results to the file `corrugation_results.csv` with the columns `slab_type`, `configuration`, `corrugation_angstrom`, and `trigonal_symmetry_metric`. The two rows should correspond to the ideal AB-stacked slab and the slipped slab.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Pseudopotentials for carbon (e.g., C.pbe-rrkjus.UPF): https://www.quantum-espresso.org/pseudopotentials
- Python post-processing packages (numpy, scipy, matplotlib, ase): numpy scipy matplotlib ase

## Workflow steps

### Step 1: Slab model construction
- Role: process
- Action: Construct 3-layer graphite slab models with ideal (AB) stacking and a slipped configuration (top layer shifted by half the in-plane lattice vector) for DFT calculations. Output atomic positions in Quantum ESPRESSO input format.
- Evidence: `/app/outputs/slab_models.xyz`

### Step 2: Self-consistent electronic structure calculation
- Role: process
- Action: Run DFT self-consistent field calculations with Quantum ESPRESSO on both slab models to obtain the self-consistent charge density and local density of states (LDOS) at the Fermi level.
- Evidence: `/app/outputs/scf_output.tar.gz`

### Step 3: Corrugation and symmetry analysis
- Role: scored (load-bearing)
- Action: From the computed charge density and LDOS, simulate STM constant-current corrugation using the Tersoff-Hamann approximation. Compute the corrugation amplitude (in Å) and a metric quantifying the degree of trigonal symmetry (e.g., ratio of 3-fold to 1-fold Fourier component amplitudes) for both the ideal and slipped configurations. Save the results to corrugation_results.csv.
- Output file: `/app/outputs/corrugation_results.csv`
- Format: csv
- Contract: slab_type (string), configuration (string, 'ideal' or 'slipped'), corrugation_angstrom (float), trigonal_symmetry_metric (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/corrugation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### corrugation_results.csv
- path: `/app/outputs/corrugation_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV containing corrugation amplitude and trigonal symmetry metric for each slab configuration.
- schema:
  - `type`: table
  - `required_columns`: `slab_type`, `configuration`, `corrugation_angstrom`, `trigonal_symmetry_metric`
  - `units`:
    - `corrugation_angstrom`: Angstrom

Notes: The checker will derive the ratio of corrugation amplitudes (slipped/ideal) and the ratio of trigonal symmetry metrics (slipped/ideal) and verify structural trends (larger corrugation and broken symmetry for the slipped configuration).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "corrugation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "slab_type",
          "configuration",
          "corrugation_angstrom",
          "trigonal_symmetry_metric"
        ],
        "units": {
          "corrugation_angstrom": "Angstrom"
        }
      },
      "description": "CSV containing corrugation amplitude and trigonal symmetry metric for each slab configuration."
    }
  ],
  "notes": "The checker will derive the ratio of corrugation amplitudes (slipped/ideal) and the ratio of trigonal symmetry metrics (slipped/ideal) and verify structural trends (larger corrugation and broken symmetry for the slipped configuration)."
}
```

## How you are scored
A hidden verifier will read your `corrugation_results.csv` and independently evaluate each scored workflow stage. It will compute the ratio of corrugation amplitudes (slipped / ideal) and the ratio of trigonal symmetry metrics (slipped / ideal) and check whether they satisfy prescribed structural conditions (for example, the corrugation is larger and the symmetry is reduced for the slipped configuration). Additionally, the verifier checks the format, presence, and integrity of all required artifacts. Reporting a number that matches the gold is not sufficient—your entire pipeline must produce the required outputs in the correct format, and the hidden checker computes its own reward from the submitted artifacts. The final reward is a weighted combination of the scores from the scored artifact(s).
