# DFT Free Energy Profiles and Charge Transfer for OER on CoP and Co-PBA Complex

## Problem background
Electrochemical water splitting for renewable hydrogen production is limited by the sluggish kinetics of the oxygen evolution reaction (OER). Transition metal phosphides, combined with porous Prussian blue analogue (PBA) frameworks containing cyano groups, are promising OER catalysts, but the atomic-level origin of their activity – in particular the role of the cyano groups and the PBA substrate in tuning the OER free energy landscape – is not fully understood. This computational task addresses the OER mechanism on both a pristine CoP surface and a CoP/Co-PBA interface, using density functional theory (DFT) to compute the Gibbs free energy profiles of the elementary steps and to quantify charge transfer between the metal phosphide cluster and the PBA substrate.

## Approach
You will perform spin-polarised DFT calculations using an open-source plane-wave / pseudopotential code (e.g. Quantum ESPRESSO) and the standardised SSSP pseudopotential library. Starting from public crystal structures for CoP and Co3[Fe(CN)6]2·H2O, construct slab models exposing the (001) surface of each material, and build an interface model by placing a CoP cluster on the PBA slab. Optimise geometries for clean surfaces and for the three adsorbed OER intermediates (*OH, *O, *OOH) on both the pristine CoP(001) surface and the CoP/Co-PBA interface. Apply zero-point energy, entropy, and solvation corrections to obtain Gibbs free energies. From those energies, construct the OER free energy diagrams at zero electrode potential, identify the potential-determining step (PDS) on each system, and compare the free energy changes between the two systems. Finally, perform Bader charge analysis on the CoP/Co-PBA interface to determine the net electron transfer from the CoP cluster to the PBA substrate. Your choices of slab thickness, vacuum gap, k‑point mesh, and energy cutoff should follow standard DFT convergence practices; specific convergence parameters are not prescribed.

## Reproduction target
Produce two scored artifacts under /app/outputs:

1. **oer_free_energies.csv** – a CSV file with four rows and three columns: `Step` (one of OH*, O*, OOH*, O2*), `dG_CoP` (Gibbs free energy in eV for the pristine CoP surface), and `dG_complex` (Gibbs free energy in eV for the CoP/Co-PBA interface). This file should contain the free energy profile at zero electrode potential for both systems and reflect the identification of the potential-determining step.

2. **bader_charge.txt** – a plain-text file containing a single floating-point number: the net Bader charge on the CoP cluster in the CoP/Co-PBA interface model, in units of |e|, with a positive value indicating electron loss from the cluster to the substrate.

## Assets

- CoP crystal structure: https://materialsproject.org/materials/mp-52/
- Co3[Fe(CN)6]2·H2O crystal structure: https://www.crystallography.net/cod/2010000.html
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Standard DFT pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp
- Bader charge analysis tool: https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build DFT slab models
- Role: process
- Action: From the CoP and Co3[Fe(CN)6]2·H2O crystal structures, construct slab models exposing the (001) surface for each material. Build a CoP/Co-PBA interface model by placing a CoP cluster on the PBA slab. Determine slab thickness, vacuum gap, k-point mesh, and energy cutoff following standard DFT convergence practices.
- Evidence: `/app/outputs/slab_models.geom`

### Step 2: DFT energy calculations of OER intermediates
- Role: process
- Action: Perform spin-polarized DFT calculations to optimize geometries and compute total energies of clean surfaces and adsorbed *OH, *O, *OOH intermediates on both CoP(001) and the CoP/Co-PBA interface model. Apply zero-point energy, entropy, and solvation corrections to obtain Gibbs free energies. Save the computed free energies for each system to an intermediate file for downstream use.
- Evidence: `/app/outputs/dft_free_energies.json`

### Step 3: Construct Gibbs free energy diagram
- Role: scored (load-bearing)
- Action: Using the free energies from the previous DFT calculations, compute the OER Gibbs free energy profiles at zero electrode potential for both the CoP(001) surface and the CoP/Co-PBA interface. Identify the potential-determining step (PDS) and its free-energy change for each system. Output a CSV file with columns: Step (one of OH*, O*, OOH*, O2*), dG_CoP (eV), dG_complex (eV).
- Output file: `/app/outputs/oer_free_energies.csv`
- Format: csv
- Contract: columns: Step (string), dG_CoP (float, eV), dG_complex (float, eV). Four rows, one per OER step.
- Scoring: scored by hidden verifier

### Step 4: Bader charge analysis
- Role: scored
- Action: From the optimized charge density of the CoP/Co-PBA interface model, perform Bader charge analysis to compute the net electron transfer from the CoP cluster to the PBA substrate. Output a single text file containing the net Bader charge (in |e|, positive for electron loss from the cluster).
- Output file: `/app/outputs/bader_charge.txt`
- Format: txt
- Contract: A single line with a float value (e.g., +3.44).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/oer_free_energies.csv`
- `/app/outputs/bader_charge.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### oer_free_energies.csv
- path: `/app/outputs/oer_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gibbs free energy steps for OER on CoP and on CoP/Co-PBA complex.
- schema:
  - `type`: table
  - `required_columns`: `Step`, `dG_CoP`, `dG_complex`
  - `units`:
    - `dG_CoP`: eV
    - `dG_complex`: eV

### bader_charge.txt
- path: `/app/outputs/bader_charge.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Net electron transfer from CoP to PBA substrate via Bader charge analysis.
- schema:
  - `type`: text
  - `content`: a single float value, the net Bader charge on the CoP cluster in the CoP/Co-PBA complex (units: |e|, positive = electron loss from CoP)

Notes: The checker compares the Gibbs free energy changes of the potential-determining step for the complex to paper-reported values and enforces the trend that *O->*OOH ΔG on complex is lower than on pristine CoP. For Bader charge, it checks the sign is positive and the magnitude within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "oer_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Step",
          "dG_CoP",
          "dG_complex"
        ],
        "units": {
          "dG_CoP": "eV",
          "dG_complex": "eV"
        }
      },
      "description": "Gibbs free energy steps for OER on CoP and on CoP/Co-PBA complex."
    },
    {
      "file": "bader_charge.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "a single float value, the net Bader charge on the CoP cluster in the CoP/Co-PBA complex (units: |e|, positive = electron loss from CoP)"
      },
      "description": "Net electron transfer from CoP to PBA substrate via Bader charge analysis."
    }
  ],
  "notes": "The checker compares the Gibbs free energy changes of the potential-determining step for the complex to paper-reported values and enforces the trend that *O->*OOH ΔG on complex is lower than on pristine CoP. For Bader charge, it checks the sign is positive and the magnitude within tolerance."
}
```

## How you are scored
Your submitted files are evaluated by an automated verifier that compares your reported numbers to hidden reference values (derived from the original paper) and checks required relative trends. For `oer_free_energies.csv`, the verifier checks the free energy of the potential-determining step on both systems and verifies that the free energy change from *O to *OOH on the complex is lower than on pristine CoP. For `bader_charge.txt`, it checks that the sign of the charge is positive (electron loss from CoP) and that the magnitude lies within an acceptable range. The verifier does not re‑run any DFT calculations; it scores solely based on your reported values. Final reward is a weighted combination of the scores for the two artifacts. Reporting arbitrary numbers without performing the task will typically result in scores outside the hidden tolerance windows and will not earn credit.
