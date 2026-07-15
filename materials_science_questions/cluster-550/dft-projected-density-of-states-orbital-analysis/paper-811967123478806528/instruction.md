# DFT Electronic and Optical Properties of A‑Site Substituted PZT: Band Gaps, Bond Angles, and Oxygen Vacancy Formation Energies

## Problem background
Lead zirconate titanate (PZT) is a high-performance ferroelectric perovskite used in actuators, sensors, and nonvolatile memories. Its fatigue under repeated switching is linked to oxygen vacancies that pin domain walls and degrade ferroelectric response. Doping with donor cations is known to mitigate fatigue and tune electronic and optical properties, but a systematic comparison of different A‑site trivalent substitutes is lacking. This task computes the electronic band gaps, optical band gaps, Ti–O–Ti bond angles, and oxygen vacancy formation energies for PZT doped with group IIIA (Sc, Y, La) and group VB (Sb, Bi) elements, and investigates how these properties depend on the dopant's atomic number and ionic size.

## Approach
Use first‑principles density functional theory (DFT) to model undoped and A‑site substituted PZT. Build 2×2×4 supercells of Pb(Zr₀.₂₅Ti₀.₇₅)O₃ with one Pb vacancy and two Pb atoms replaced by the trivalent dopant (Sc, Y, La, Sb, Bi) to maintain charge neutrality; use experimental lattice constants. Relax the ionic positions with a GGA functional (e.g., PBE), then recompute the electronic structure with a meta‑GGA functional (e.g., TPSS) to obtain the density of states (DOS) and optical absorption spectra. Compute the oxygen chemical potential μ_O from an isolated O₂ molecule and calculate total energies of perfect and oxygen‑deficient supercells to extract neutral oxygen vacancy formation energies. From the relaxed structures and the computed DOS/optical curves, determine the energy band gaps (from VBM–CBM in the DOS), optical band gaps (via Tauc's direct‑gap formula applied to the absorption coefficient), average Ti–O–Ti bond angles, and formation energies. Compare the results across all systems to establish how the dopant's atomic number and ionic radius influence these properties.

## Reproduction target
Produce a single scored file `results.json` containing, for each system (undoped PZT, and the A‑site substituted systems with Sc, Y, La, Sb, Bi), the energy band gap (eV), optical band gap (eV), average Ti–O–Ti bond angle (deg), and oxygen vacancy formation energy (eV) under oxygen‑rich conditions. Additionally, include the formation energy for a Pb‑deficient (no dopant) case. The hidden verifier will check the accuracy of each quantity against reference values and also verify that the computed set of values exhibits the systematic trends with dopant atomic number and ionic radius expected from the physics of Ti‑3d bandwidth and the character of the band gap.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific stack (numpy, scipy, matplotlib)

## Workflow steps

### Step 1: Geometry optimization of supercells
- Role: process
- Action: For each system (undoped PZT and A‑site substituted PZT with Sc, Y, La, Sb, Bi), build a 2×2×4 supercell of Pb(Zr0.25Ti0.75)O3 with one Pb vacancy at the cell centre and two Pb atoms replaced by the respective dopant to maintain electroneutrality. Use experimental lattice constants a=b=7.892 Å, c/a=2.094. Relax atomic positions using DFT‑GGA (PBE) with Quantum ESPRESSO until forces converge. Save the final relaxed atomic coordinates for all systems in a single structured file.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 2: Oxygen chemical potential from isolated O₂ molecule
- Role: process
- Action: Compute the total energy of an isolated O₂ molecule (bond length ~1.21 Å) using the same GGA‑PBE functional. Extract the oxygen chemical potential μ_O = E(O₂)/2 and save the value.
- Evidence: `/app/outputs/mu_O.json`

### Step 3: Electronic structure and DOS calculation
- Role: process
- Action: On the relaxed structures, run a self‑consistent field (SCF) calculation followed by a non‑SCF density of states (DOS) calculation using a meta‑GGA functional (TPSS) with a dense k‑mesh. Save the total DOS for each system as a two‑column CSV file (Energy in eV, DOS in states/eV).
- Evidence: `/app/outputs/dos_{dopant}.csv`

### Step 4: Optical absorption spectrum calculation
- Role: process
- Action: Using the same meta‑GGA electronic structure, compute the frequency‑dependent dielectric function and derive the absorption coefficient α(E). Save the absorption spectrum for each system as a two‑column CSV file (Energy in eV, α in cm⁻¹).
- Evidence: `/app/outputs/absorption_{dopant}.csv`

### Step 5: Oxygen vacancy total energy calculations
- Role: process
- Action: For each system (undoped perfect, Pb‑deficient, and all doped systems), create a neutral oxygen vacancy defect supercell (remove one O atom). Perform a static GGA‑PBE energy calculation on the relaxed geometry (keeping ionic positions fixed). Collect the total energies of all perfect and defective supercells in a structured JSON file.
- Evidence: `/app/outputs/vacancy_total_energies.json`

### Step 6: Extract energy, optical, structural, and defect properties
- Role: scored (load-bearing)
- Action: Read the DOS CSV files and locate the valence band maximum (VBM) and conduction band minimum (CBM) to determine energy band gaps. Read the absorption spectra, apply Tauc’s formula for a direct allowed transition, and extract optical band gaps. Compute the average Ti‑O‑Ti bond angle from the relaxed atomic coordinates. Compute oxygen vacancy formation energies using the formula E_f = E_defect − E_perfect + μ_O. Assemble all quantities per system into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"systems": [{"dopant": "none"|"Pb-deficient"|"Sc"|"Y"|"La"|"Sb"|"Bi", "energy_band_gap": <float|null>, "optical_band_gap": <float|null>, "Ti-O-Ti_bond_angle": <float|null>, "oxygen_vacancy_formation_energy": <float|null>}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scored summary of the paper’s headline quantities: energy and optical band gaps, Ti‑O‑Ti bond angle, and oxygen vacancy formation energy for all systems. The checker will recompute gaps from the supplied DOS and absorption CSVs, bond angles from the relaxed structures, and formation energies from the total energy data, then compare against hidden gold values with tolerances and verify monotonic trends.
- schema:
  - `type`: object
  - `required`:
    - `systems`: array
  - `items`:
    - `dopant`: string (one of: none, Pb-deficient, Sc, Y, La, Sb, Bi)
    - `energy_band_gap`: float (eV) or null for Pb-deficient
    - `optical_band_gap`: float (eV) or null for Pb-deficient
    - `Ti-O-Ti_bond_angle`: float (degrees) or null for Pb-deficient
    - `oxygen_vacancy_formation_energy`: float (eV)

Notes: The checker also reads the intermediate evidence files (dos_*.csv, absorption_*.csv, relaxed_structures.json, vacancy_total_energies.json, mu_O.json) that the agent must produce. These are not scored directly but are required for recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "systems": "array"
        },
        "items": {
          "dopant": "string (one of: none, Pb-deficient, Sc, Y, La, Sb, Bi)",
          "energy_band_gap": "float (eV) or null for Pb-deficient",
          "optical_band_gap": "float (eV) or null for Pb-deficient",
          "Ti-O-Ti_bond_angle": "float (degrees) or null for Pb-deficient",
          "oxygen_vacancy_formation_energy": "float (eV)"
        }
      },
      "description": "Scored summary of the paper’s headline quantities: energy and optical band gaps, Ti‑O‑Ti bond angle, and oxygen vacancy formation energy for all systems. The checker will recompute gaps from the supplied DOS and absorption CSVs, bond angles from the relaxed structures, and formation energies from the total energy data, then compare against hidden gold values with tolerances and verify monotonic trends."
    }
  ],
  "notes": "The checker also reads the intermediate evidence files (dos_*.csv, absorption_*.csv, relaxed_structures.json, vacancy_total_energies.json, mu_O.json) that the agent must produce. These are not scored directly but are required for recomputation."
}
```

## How you are scored
A hidden verifier recomputes each headline quantity from the raw intermediate artifacts you produce (DOS CSV files, absorption CSV files, relaxed structure coordinates, total energy data, and μ_O). It checks the extracted band gaps, bond angles, and formation energies against reference values and also audits the series for mandatory systematic trends (monotonic ordering across the group IIIA and group VB series). Each verification stage carries a weight; the final reward (0–1) is the weighted sum of all checks. Reporting approximate paper‑reported numbers without proper intermediate evidence will not yield a high score — the verifier relies on your raw computed data.
