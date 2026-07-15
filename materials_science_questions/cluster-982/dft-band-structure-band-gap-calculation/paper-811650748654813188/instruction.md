# DFT study of Al-doped α-Si3N4: formation energies and electronic band gaps

## Problem background
α-Si3N4 is a wide-band-gap ceramic material with potential applications in optoelectronics and photocatalysis. Al doping is a strategy to modify its electronic structure and possibly reduce the band gap, making it active under visible light. This task investigates how Al incorporation at different sites (substitutional, interstitial, and complexes) affects the thermodynamic stability and the electronic band gap of α-Si3N4 by means of first-principles density functional theory (DFT) calculations. The target is to compute the formation heats of various Al configurations and the resulting band gaps, quantifying the doping-induced changes.

## Approach
The workflow uses plane-wave DFT within the generalized gradient approximation of Perdew, Burke, and Ernzerhof (GGA-PBE) as implemented in the open-source code Quantum ESPRESSO. An 84-atom supercell of hexagonal α-Si3N4 (space group P31c, experimental lattice constants a=7.753 Å, c=5.618 Å) is constructed. Al is placed at inequivalent substitutional and interstitial sites, as well as in multi-atom complexes comprising both substitutional and interstitial Al. For each configuration, the geometry is optimized with fixed lattice constants, and the total energy is computed. Formation heats are then calculated by comparing the energy of the doped system to that of pure α-Si3N4 and the elemental reference states of Al (fcc) and Si (diamond). The electronic band gap is extracted from the self-consistent calculations for the pristine supercell and for the most stable (1+1) Al-doped configuration.

## Reproduction target
The goal is to produce two JSON files: (1) formation_heats.json, containing the formation heats (in eV) of nine Al configurations: single substitutional at the two inequivalent Si sites (sub1, sub2), single interstitial, two substitutional Al far apart and neighboring, the interaction energy between substitutional Al (difference between the two), and the per-Al formation heats of the (1+1), (2+1), and (3+1) complexes; (2) band_gaps.json, giving the band gaps (in eV) for pure α-Si3N4 and for the most stable (1+1) Al-doped configuration. All values must be derived from the DFT calculations described in the workflow steps.

## Assets

- α-Si3N4 crystal structure: https://materialsproject.org/materials/mp-1242
- GGA-PBE pseudopotentials (PAW) for Si, N, Al: https://www.materialscloud.org/discover/sssp
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build supercell and doping configurations
- Role: process
- Action: Construct an 84-atom supercell of α-Si3N4 (a=7.753 Å, c=5.618 Å, space group P31c) from the experimental crystal structure. Generate input files for Quantum ESPRESSO for the pristine system, elemental references (fcc Al, diamond Si), and all required Al-doped configurations: single substitutional at each inequivalent site (sub-1, sub-2), single interstitial, two substitutional far apart and neighboring, one substitutional plus one interstitial (1+1 complex), two substitutional plus one interstitial (2+1 complex), and three substitutional plus one interstitial (3+1 complex). Identify and label the inequivalent sites.
- Evidence: `/app/outputs/supercell_configurations.log`

### Step 2: Run DFT total energy and geometry optimization
- Role: process
- Action: Perform GGA-PBE total energy and geometry optimization calculations using Quantum ESPRESSO for the pristine supercell, elemental Al and Si, and every Al-doped configuration listed in step 1. Relax internal coordinates (lattice constants fixed at experimental values) and obtain self-consistent total energies and optimized geometries needed for the formation heat and band gap analysis.
- Evidence: `/app/outputs/dft_output.log`

### Step 3: Calculate formation heats
- Role: scored (load-bearing)
- Action: Compute the formation heats of all Al configurations from the DFT total energies (pristine, elemental references, and doped systems) using the definition referenced to pure α-Si3N4, elemental Al and Si. Write the results to /app/outputs/formation_heats.json.
- Output file: `/app/outputs/formation_heats.json`
- Format: json
- Contract: JSON object: keys are configuration names (strings "sub1", "sub2", "interstitial", "two_sub_far", "two_sub_near", "interaction_energy", "complex_1+1_per_Al", "complex_2+1_per_Al", "complex_3+1_per_Al"); values are formation heats in eV (float). The interaction_energy is two_sub_far minus two_sub_near. The complex per‑Al values are the total formation heat divided by the number of Al atoms in the complex.
- Scoring: scored by hidden verifier

### Step 4: Extract band gaps
- Role: scored (load-bearing)
- Action: Extract the electronic band gap from the DFT calculations for pristine α-Si3N4 and for the most stable (1+1) Al‑doped configuration. For metallic systems report 0. Write the results to /app/outputs/band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON object: keys "pure" and "complex_1+1"; values are band gaps in eV (float). A metallic system yields 0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_heats.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_heats.json
- path: `/app/outputs/formation_heats.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation heat values for each Al configuration, computed from DFT total energies and referenced to pure α-Si3N4 and elemental Al and Si.
- schema:
  - `type`: object
  - `required`:
    - `sub1`: float (eV)
    - `sub2`: float (eV)
    - `interstitial`: float (eV)
    - `two_sub_far`: float (eV)
    - `two_sub_near`: float (eV)
    - `interaction_energy`: float (eV)
    - `complex_1+1_per_Al`: float (eV)
    - `complex_2+1_per_Al`: float (eV)
    - `complex_3+1_per_Al`: float (eV)

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic band gaps for pristine and (1+1) Al‑doped α-Si3N4 from DFT calculations.
- schema:
  - `type`: object
  - `required`:
    - `pure`: float (eV)
    - `complex_1+1`: float (eV)

Notes: All values are in electronvolts (eV). The (1+1) complex refers to the most stable configuration found in the DFT calculations. Formulation of formation heats follows the standard definition referenced to pure α-Si3N4 and elemental crystals of Al and Si.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_heats.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "sub1": "float (eV)",
          "sub2": "float (eV)",
          "interstitial": "float (eV)",
          "two_sub_far": "float (eV)",
          "two_sub_near": "float (eV)",
          "interaction_energy": "float (eV)",
          "complex_1+1_per_Al": "float (eV)",
          "complex_2+1_per_Al": "float (eV)",
          "complex_3+1_per_Al": "float (eV)"
        }
      },
      "description": "Formation heat values for each Al configuration, computed from DFT total energies and referenced to pure α-Si3N4 and elemental Al and Si."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pure": "float (eV)",
          "complex_1+1": "float (eV)"
        }
      },
      "description": "Electronic band gaps for pristine and (1+1) Al‑doped α-Si3N4 from DFT calculations."
    }
  ],
  "notes": "All values are in electronvolts (eV). The (1+1) complex refers to the most stable configuration found in the DFT calculations. Formulation of formation heats follows the standard definition referenced to pure α-Si3N4 and elemental crystals of Al and Si."
}
```

## How you are scored
A hidden verifier reads your submitted JSON files and compares each reported value to hidden reference values using tolerances that absorb legitimate implementation spread. Each scored artifact carries a share of the total reward; the reward is the fraction of values that fall within the acceptable tolerance or, for complex per-Al values, within a specified range. The verifier does not inspect your intermediate DFT output—it only checks the final reported numbers. Reporting values without genuinely running the DFT workflow will produce results that are unlikely to match the hidden references.
