# DFT Band Gap and Anisotropic Charge Mobilities of a Biphenyl Organic Crystal

## Problem background
Organic semiconductors based on biphenyl derivatives show promise for optoelectronic devices due to their wide band gaps and tunable charge transport. This task investigates the electronic band gap, effective electronic couplings, and anisotropic charge mobilities of one such compound, BPVB, using density functional theory (DFT) and Marcus theory. The goal is to compute these properties from first-principles and compare them against established reference results.

## Approach
We adopt a combined DFT and Marcus-theory workflow. First, the crystal structure of BPVB (obtained from the Cambridge Crystallographic Data Centre) is used to define the molecular packing. The monomer geometry is optimized in neutral, cationic, and anionic states at the B3LYP/6-311++G(d,p) level in CHCl₃ solvent, yielding hole and electron reorganization energies. Next, periodic DFT with the GGA-PBE functional on the experimental unit cell computes the electronic band gap as the energy difference between the valence band maximum and conduction band minimum. From the BPVB crystal packing, the nearest-neighbor dimers (P, T1, and T2 channels) are identified; single-point DFT calculations provide the Kohn-Sham Hamiltonian and monomer frontier orbitals, from which effective hole and electron transfer integrals are calculated using the fragment orbital approach. Finally, Marcus hopping rates are combined with the effective couplings, reorganization energies, intermolecular distances, and an anisotropic mobility orientation function to produce the angular-dependent hole and electron mobilities, from which the maximum values are extracted.

## Reproduction target
Produce the following quantitative results for the BPVB crystal:
1. The electronic band gap Eg (eV).
2. The effective hole (V_eff^h) and electron (V_eff^e) transfer integrals (meV) for the P, T1, and T2 dimer channels.
3. The maximum anisotropic hole mobility μ_h_max and maximum electron mobility μ_e_max (cm²/Vs).
These values must be computed through the prescribed workflow and written to the designated JSON output files.

## Assets

- BPVB crystal structure (CCDC 628422): CCDC 628422
- Quantum chemistry / DFT software (ORCA, Quantum ESPRESSO)
- Python scientific stack: python (numpy, scipy)

## Workflow steps

### Step 1: Retrieve BPVB crystal structure
- Role: process
- Action: Download the CIF file of BPVB from the Cambridge Crystallographic Data Centre using deposition number CCDC 628422.
- Evidence: `/app/outputs/BPVB.cif`

### Step 2: Compute monomer properties and reorganization energies
- Role: process
- Action: Optimize the geometry of the BPVB monomer in neutral, cationic, and anionic states at the B3LYP/6-311++G(d,p) level in CHCl₃ solvent. From the total energies compute adiabatic and vertical ionization potentials, electron affinities, HOMO/LUMO energies, and hole/electron reorganization energies.
- Evidence: `/app/outputs/reorganization_energies.json`

### Step 3: Compute electronic band gap
- Role: scored
- Action: Using the experimental BPVB unit cell from the CIF, perform a periodic DFT calculation with the GGA-PBE functional on the reported k-point mesh (2×3×1). Extract the band gap Eg as the energy difference between the valence band maximum and conduction band minimum.
- Output file: `/app/outputs/step_01_band_gap.json`
- Format: json
- Contract: {"Eg": {"type": "float", "unit": "eV"}}
- Scoring: scored by hidden verifier

### Step 4: Compute effective transfer integrals
- Role: scored
- Action: Extract the nearest-neighbor dimers (P, T1, T2 channels) from the BPVB crystal packing. For each dimer, perform a single-point DFT calculation to obtain the Kohn-Sham Hamiltonian and monomer HOMO/LUMO orbitals. Compute the effective hole and electron transfer integrals V_eff^h and V_eff^e using the fragment orbital approach. Report the values in meV.
- Output file: `/app/outputs/step_02_effective_couplings.json`
- Format: json
- Contract: [{"channel": "string", "V_eff_h": {"type": "float", "unit": "meV"}, "V_eff_e": {"type": "float", "unit": "meV"}}]
- Scoring: scored by hidden verifier

### Step 5: Compute anisotropic charge mobilities
- Role: scored (load-bearing)
- Action: Combine the effective couplings, reorganization energies, intermolecular distances and angles from the crystal packing, and apply Marcus theory and the anisotropic mobility orientation function to compute the maximum hole mobility μ_h_max and maximum electron mobility μ_e_max.
- Output file: `/app/outputs/step_03_anisotropic_mobilities.json`
- Format: json
- Contract: {"mu_h_max": {"type": "float", "unit": "cm2/Vs"}, "mu_e_max": {"type": "float", "unit": "cm2/Vs"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gap.json`
- `/app/outputs/step_02_effective_couplings.json`
- `/app/outputs/step_03_anisotropic_mobilities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gap.json
- path: `/app/outputs/step_01_band_gap.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic band gap Eg (VBM − CBM) of the BPVB crystal. Compare to paper gold with tolerance; lower is better.
- schema:
  - `type`: object
  - `required`:
    - `Eg`: number
  - `units`:
    - `Eg`: eV

### step_02_effective_couplings.json
- path: `/app/outputs/step_02_effective_couplings.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Effective hole and electron transfer integrals for P, T1, T2 dimers. Compare each component to paper gold within tolerance.
- schema:
  - `type`: array
  - `items`:
    - `channel`: string
    - `V_eff_h`: number (meV)
    - `V_eff_e`: number (meV)

### step_03_anisotropic_mobilities.json
- path: `/app/outputs/step_03_anisotropic_mobilities.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum anisotropic hole and electron mobilities. Compare to paper gold with relative tolerance; meeting or exceeding the reference earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `mu_h_max`: number
    - `mu_e_max`: number
  - `units`:
    - `mu_h_max`: cm²/Vs
    - `mu_e_max`: cm²/Vs

Notes: Only the BPVB crystal is reproduced. Absorption spectra (TDDFT) and Hirshfeld surface analysis are omitted as per the scoped taskability scope. All outputs are compared to the hidden paper-reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Eg": "number"
        },
        "units": {
          "Eg": "eV"
        }
      },
      "description": "Electronic band gap Eg (VBM − CBM) of the BPVB crystal. Compare to paper gold with tolerance; lower is better."
    },
    {
      "file": "step_02_effective_couplings.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "channel": "string",
          "V_eff_h": "number (meV)",
          "V_eff_e": "number (meV)"
        }
      },
      "description": "Effective hole and electron transfer integrals for P, T1, T2 dimers. Compare each component to paper gold within tolerance."
    },
    {
      "file": "step_03_anisotropic_mobilities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "mu_h_max": "number",
          "mu_e_max": "number"
        },
        "units": {
          "mu_h_max": "cm²/Vs",
          "mu_e_max": "cm²/Vs"
        }
      },
      "description": "Maximum anisotropic hole and electron mobilities. Compare to paper gold with relative tolerance; meeting or exceeding the reference earns full credit."
    }
  ],
  "notes": "Only the BPVB crystal is reproduced. Absorption spectra (TDDFT) and Hirshfeld surface analysis are omitted as per the scoped taskability scope. All outputs are compared to the hidden paper-reported values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently inspects each output JSON file. It extracts the reported quantities and compares them against verified reference values using appropriate tolerances (band gap and coupling values are compared with tight absolute tolerances, while mobilities are compared with a relative margin). Each stage carries a predefined weight; the final reward is a weighted combination of the stage scores, ranging from 0 to 1. You must faithfully execute the workflow and produce the required artifacts; simply guessing or fabricating numbers is not a valid strategy.
