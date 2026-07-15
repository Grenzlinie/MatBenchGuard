# DFT-Computed Spin-State and Isomer Energies with OCO Stretching Frequencies for EDTA–Metal Complexes

## Problem background
Transition-metal dications chelated by EDTA exhibit vibrational signatures in the OCO stretching region that depend on the metal's spin state and coordination number. The underlying computational sub‑result consists of the relative energies of different spin states (high‑spin vs low‑spin) and of different coordination isomers (hexa‑, penta‑, tetra‑coordinated) for several first‑row transition metals, together with the associated antisymmetric OCO stretching frequencies. Reproducing these quantities provides a spectroscopic ruler for the metal‑ion environment and tests the predictive power of the chosen DFT protocol.

## Approach
The reproduction follows a compute‑driven DFT pipeline. All calculations are performed at the ωB97X‑D/Def2‑TZVPP level using an open‑source quantum chemistry package (e.g., Psi4). For each metal, initial geometries of the EDTA complex are constructed in the relevant spin states and coordination numbers. Geometry optimization is followed by a harmonic frequency calculation. The raw harmonic frequencies are scaled uniformly by 0.950, a factor calibrated to align the main antisymmetric OCO feature of the Ca‑EDTA reference complex. The total energies and scaled vibrational frequencies are then post‑processed to extract relative energies (in cm⁻¹) and the antisymmetric OCO stretching frequency in the 1600–1700 cm⁻¹ window.

## Reproduction target
Compute and report:
1) The relative energies (in cm⁻¹) of different spin states for hexa‑coordinated [M(II)‑EDTA]²⁻ (M = Mn, Co, Ni).
2) The relative energies (in cm⁻¹) of hexa‑, penta‑, and tetra‑coordinated isomers (most stable spin state) for M = Co, Cu, Zn.
3) The scaled antisymmetric OCO stretching frequency (in cm⁻¹) for each coordination isomer of Co, Cu, Zn.
The results should reveal the ground spin state for Mn, Co, Ni, the most stable coordination number for Co, Cu, Zn, and the trend in OCO stretching frequency as a function of coordination number.

## Assets

- Psi4 quantum chemistry package: https://psicode.org/
- Def2-TZVPP basis set library: https://www.basissetexchange.org/
- ωB97X-D exchange-correlation functional

## Workflow steps

### Step 1: DFT geometry optimization and harmonic frequency calculations
- Role: process
- Action: Construct initial geometries for [M(II)-EDTA]²⁻ complexes (M = Mn, Co, Ni, Cu, Zn). For Mn, Co, Ni set up hexa-coordinated structures in high-spin and low-spin states. For Co, Cu, Zn build hexa-, penta-, and tetra-coordinated isomers at the most stable spin state. Perform geometry optimization followed by harmonic frequency calculation at the ωB97X-D/Def2-TZVPP level using an open-source package (e.g., Psi4). Apply a uniform frequency scaling factor of 0.950 to the harmonic frequencies. Record total energies and scaled vibrational frequencies for every system.
- Evidence: `/app/outputs/dft_outputs.log`

### Step 2: Spin-state relative energies
- Role: scored (load-bearing)
- Action: Using the total DFT energies of the hexa-coordinated complexes for M = Mn, Co, Ni, compute the relative energy (in cm⁻¹) of each spin state, setting the lowest spin state to zero. Report the results as a JSON array.
- Output file: `/app/outputs/step_01_spin_state_energies.json`
- Format: json
- Contract: Array of objects: [{"metal": "Mn|Co|Ni", "spin_state": "string", "relative_energy_cm1": float}]
- Scoring: scored by hidden verifier

### Step 3: Isomer relative energies
- Role: scored
- Action: Using the total DFT energies of the most stable spin state for each coordination isomer of M = Co, Cu, Zn, compute the relative energy (in cm⁻¹) with the lowest isomer set to zero. Report as a JSON array.
- Output file: `/app/outputs/step_02_isomer_energies.json`
- Format: json
- Contract: Array of objects: [{"metal": "Co|Cu|Zn", "coordination": 4|5|6, "relative_energy_cm1": float}]
- Scoring: scored by hidden verifier

### Step 4: Antisymmetric OCO stretching frequencies
- Role: scored
- Action: For each coordination isomer of Co, Cu, Zn, after scaling harmonic frequencies by 0.950, locate the highest-frequency normal mode in the 1600–1700 cm⁻¹ window dominated by antisymmetric OCO stretching. Report that frequency in cm⁻¹.
- Output file: `/app/outputs/step_03_frequencies.json`
- Format: json
- Contract: Array of objects: [{"metal": "Co|Cu|Zn", "coordination": 4|5|6, "frequency_cm1": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_spin_state_energies.json`
- `/app/outputs/step_02_isomer_energies.json`
- `/app/outputs/step_03_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_spin_state_energies.json
- path: `/app/outputs/step_01_spin_state_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed relative spin-state energies for Mn, Co, Ni EDTA complexes. Compared against reference values derived from the computational protocol to validate ground-state spin ordering.
- schema:
  - `type`: array
  - `items`:
    - `metal`: string (Mn, Co, or Ni)
    - `spin_state`: string (descriptive, e.g., sextet, doublet)
    - `relative_energy_cm1`: float (energy difference in cm⁻¹)

### step_02_isomer_energies.json
- path: `/app/outputs/step_02_isomer_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed relative energies of hexa-, penta-, and tetra-coordinated EDTA isomers for Co, Cu, Zn. Compared against reference isomer energy ordering and values.
- schema:
  - `type`: array
  - `items`:
    - `metal`: string (Co, Cu, or Zn)
    - `coordination`: integer (4, 5, or 6)
    - `relative_energy_cm1`: float (energy difference in cm⁻¹)

### step_03_frequencies.json
- path: `/app/outputs/step_03_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed antisymmetric OCO stretching frequencies for each isomer, verifying the monotonic trend with coordination number and agreement with reference values.
- schema:
  - `type`: array
  - `items`:
    - `metal`: string (Co, Cu, or Zn)
    - `coordination`: integer (4, 5, or 6)
    - `frequency_cm1`: float (scaled antisymmetric OCO stretching frequency in cm⁻¹)

Notes: The agent must run DFT calculations at the ωB97X‑D/Def2‑TZVPP level with a 0.950 frequency scaling factor. Scored outputs are JSON arrays; the checker compares computed values against reference values derived from the same computational protocol and verifies required qualitative trends (high‑spin lowest, penta‑coordinated lowest, OCO frequency ordering). Absolute tolerances absorb legitimate method‑dependent shifts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_spin_state_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string (Mn, Co, or Ni)",
          "spin_state": "string (descriptive, e.g., sextet, doublet)",
          "relative_energy_cm1": "float (energy difference in cm⁻¹)"
        }
      },
      "description": "Computed relative spin-state energies for Mn, Co, Ni EDTA complexes. Compared against reference values derived from the computational protocol to validate ground-state spin ordering."
    },
    {
      "file": "step_02_isomer_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string (Co, Cu, or Zn)",
          "coordination": "integer (4, 5, or 6)",
          "relative_energy_cm1": "float (energy difference in cm⁻¹)"
        }
      },
      "description": "Computed relative energies of hexa-, penta-, and tetra-coordinated EDTA isomers for Co, Cu, Zn. Compared against reference isomer energy ordering and values."
    },
    {
      "file": "step_03_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string (Co, Cu, or Zn)",
          "coordination": "integer (4, 5, or 6)",
          "frequency_cm1": "float (scaled antisymmetric OCO stretching frequency in cm⁻¹)"
        }
      },
      "description": "Computed antisymmetric OCO stretching frequencies for each isomer, verifying the monotonic trend with coordination number and agreement with reference values."
    }
  ],
  "notes": "The agent must run DFT calculations at the ωB97X‑D/Def2‑TZVPP level with a 0.950 frequency scaling factor. Scored outputs are JSON arrays; the checker compares computed values against reference values derived from the same computational protocol and verifies required qualitative trends (high‑spin lowest, penta‑coordinated lowest, OCO frequency ordering). Absolute tolerances absorb legitimate method‑dependent shifts."
}
```

## How you are scored
Your submitted JSON files are evaluated by an automated verifier that compares them against reference results obtained from the same computational protocol. Scoring is based on qualitative trends and orderings:
- Step 2 (spin‑state energies): the high‑spin state must be the lowest for each metal, and the energetic ordering of spin states must be consistent.
- Step 3 (isomer energies): for each of Co, Cu, Zn the pentacoordinated isomer must be the lowest in energy and the hexacoordinated isomer must be the second lowest.
- Step 4 (frequencies): for each metal, the antisymmetric OCO stretching frequency must increase with decreasing coordination number (hexa < penta < tetra).
Exact numerical values are allowed generous tolerances to absorb legitimate method‑dependent shifts. The verifier combines the outcomes of the three scored stages to produce a final reward between 0 and 1; the spin‑state and isomer stages carry the largest weight.
