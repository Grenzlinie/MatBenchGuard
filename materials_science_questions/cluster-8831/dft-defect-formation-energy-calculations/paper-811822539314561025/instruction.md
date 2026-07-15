# DFT Optical Response of Spinel SiGe₂N₄ with Ga and As Substitution

## Problem background
Spinel-phase nitrides of group IV elements, such as γ‑Si₃N₄ and γ‑Ge₃N₄, are known for their wide direct electronic band gaps, but their optical absorption strength, as measured by the imaginary part of the dielectric function ε₂, is relatively modest compared to established optoelectronic semiconductors. One compound of interest is the derivative γ‑SiGe₂N₄, which has a direct band gap and a stable spinel structure. Prior work has suggested that this material's optical response could be improved by introducing dopants that alter the electronic band structure near the gap, particularly by modifying the character and energetics of the interband transitions that dominate the absorption peak. The present work aims to quantify the effect of cation substitution at the tetrahedral Si sites on the dielectric function of γ‑SiGe₂N₄, computing the static dielectric constant and the energy and intensity of the main absorption peak.

## Approach
The reproducibility strategy is to perform first-principles density-functional theory (DFT) calculations using the generalized gradient approximation (Perdew–Burke–Ernzerhof, GGA‑PBE) to obtain the ground-state electronic structure of three model systems: undoped γ‑SiGe₂N₄, and two cation‑substituted variants in which 50% of the tetrahedral Si atoms are replaced by Ga or As. For each system we build a 56‑atom spinel supercell, relax the atomic positions (and optionally the lattice parameter), and then compute the frequency‑dependent dielectric function ε(ω) = ε₁(ω) + i ε₂(ω) within the independent‑particle approximation (RPA‑like, neglecting local‑field and excitonic effects). A phenomenological broadening of 0.2 eV is applied. From the resulting spectra we extract three headline quantities for each composition: the maximum value of ε₂, the photon energy where it occurs, and the static dielectric constant ε₁(0). These nine numbers are then written to a structured JSON file for subsequent verification.

## Reproduction target
Deliver a single JSON file, `/app/outputs/dielectric_results.json`, containing the extracted optical quantities for three systems:

- `undoped`: pure γ‑SiGe₂N₄ (the parent compound)
- `Ga_substitution`: (Si₀.₅Ga₀.₅)Ge₂N₄
- `As_substitution`: (Si₀.₅As₀.₅)Ge₂N₄

The JSON object must have the structure:
```
{
  "undoped": {"epsilon2_peak": float, "peak_position_eV": float, "epsilon1_0": float},
  "Ga_substitution": {...},
  "As_substitution": {...}
}
```
All values must be finite positive floats. The verifier will check that the output file is syntactically valid, contains all required keys, and that the numerical values meet physical reasonableness criteria (e.g., lie within expected energy ranges for this class of materials). The reproduction is considered successful if your computed quantities, taken together, demonstrate the effect of the substitution on the optical response without needing to match exact literature numbers.

## Assets

- DFT code (Quantum ESPRESSO, GPAW, ABINIT, or equivalent open-source)
- GGA-PBE pseudopotentials (e.g., SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of γ-SiGe₂N₄ (spinel, Fd-3m)

## Workflow steps

### Step 1: DFT for pristine γ-SiGe₂N₄
- Role: process
- Action: Build the 56-atom spinel unit cell of γ-SiGe₂N₄, relax atomic positions (and optionally the lattice constant), then compute the frequency-dependent dielectric function ε₂(ω) and ε₁(ω) using the independent-particle approximation (RPA-like) as implemented in the chosen DFT code. Use a broadening of 0.2 eV. Save the raw ε₂ and ε₁ data as a two-column file (energy vs. ε₂, and optionally energy vs. ε₁).
- Evidence: `/app/outputs/pristine_epsilon.dat`

### Step 2: DFT for (Si₀.₅Ga₀.₅)Ge₂N₄
- Role: process
- Action: Construct a supercell of γ-SiGe₂N₄ where 50% of the tetrahedral Si atoms are replaced by Ga (two Ga atoms in the 56-atom cell). Relax atomic positions keeping the symmetry cubic, then compute the frequency-dependent dielectric function ε₂(ω) and ε₁(ω) with the same DFT settings as step 1. Save the raw data as a two-column file.
- Evidence: `/app/outputs/ga_epsilon.dat`

### Step 3: DFT for (Si₀.₅As₀.₅)Ge₂N₄
- Role: process
- Action: Construct a supercell of γ-SiGe₂N₄ where 50% of the tetrahedral Si atoms are replaced by As (two As atoms in the 56-atom cell). Relax atomic positions keeping the symmetry cubic, then compute the frequency-dependent dielectric function ε₂(ω) and ε₁(ω) with the same DFT settings as step 1. Save the raw data as a two-column file.
- Evidence: `/app/outputs/as_epsilon.dat`

### Step 4: Extract headline optical quantities
- Role: scored (load-bearing)
- Action: From the dielectric functions computed in steps 1–3, extract for each system: (i) the maximum value of ε₂ (epsilon2_peak), (ii) the photon energy at which that maximum occurs (peak_position_eV), and (iii) the static dielectric constant ε₁(0). Write these nine numbers to a JSON file.
- Output file: `/app/outputs/dielectric_results.json`
- Format: json
- Contract: {"undoped": {"epsilon2_peak": float, "peak_position_eV": float, "epsilon1_0": float}, "Ga_substitution": {"epsilon2_peak": float, "peak_position_eV": float, "epsilon1_0": float}, "As_substitution": {"epsilon2_peak": float, "peak_position_eV": float, "epsilon1_0": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_results.json
- path: `/app/outputs/dielectric_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Extracted peak ε₂ values, their photon energies, and static dielectric constants for undoped γ-SiGe₂N₄, (Si₀.₅Ga₀.₅)Ge₂N₄, and (Si₀.₅As₀.₅)Ge₂N₄.
- schema:
  - `type`: object
  - `required`:
    - `undoped`: object with epsilon2_peak (float), peak_position_eV (float), epsilon1_0 (float)
    - `Ga_substitution`: object with epsilon2_peak (float), peak_position_eV (float), epsilon1_0 (float)
    - `As_substitution`: object with epsilon2_peak (float), peak_position_eV (float), epsilon1_0 (float)

Notes: The checker verifies structural ordering (ε2_peak and ε1_0: Ga > As > undoped) and that peak positions fall within broad acceptable ranges; no exact numeric match required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "undoped": "object with epsilon2_peak (float), peak_position_eV (float), epsilon1_0 (float)",
          "Ga_substitution": "object with epsilon2_peak (float), peak_position_eV (float), epsilon1_0 (float)",
          "As_substitution": "object with epsilon2_peak (float), peak_position_eV (float), epsilon1_0 (float)"
        }
      },
      "description": "Extracted peak ε₂ values, their photon energies, and static dielectric constants for undoped γ-SiGe₂N₄, (Si₀.₅Ga₀.₅)Ge₂N₄, and (Si₀.₅As₀.₅)Ge₂N₄."
    }
  ],
  "notes": "The checker verifies structural ordering (ε2_peak and ε1_0: Ga > As > undoped) and that peak positions fall within broad acceptable ranges; no exact numeric match required."
}
```

## How you are scored
A hidden verifier program will read the file `/app/outputs/dielectric_results.json` that your workflow writes. It will first confirm that the file format is correct and that all nine fields are present and contain positive numbers. It will then compare your reported values against hidden reference criteria that encode the expected structural relationship between the three systems and approximate magnitude windows. Your final score is a weighted sum of the verifier's checks: the structural checks on the three quantities carry the most weight, while syntactic checks carry a small weight. The verifier does not require exact numeric agreement with the original paper; it tests whether your DFT calculations correctly capture the relative optical response of the doped compared to the undoped spinel. No credit is given for simply reporting numbers that happen to match a published table; the workflow must perform the DFT steps and extract the quantities from the computed spectra.
