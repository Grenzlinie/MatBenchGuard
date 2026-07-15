# DFT Study of SrVO₃ Work Function and Ba Doping Effects

## Problem background
Perovskite oxides are promising materials for electron emission applications, but their surface work functions and the compositional trends that control them have not been systematically quantified. This task uses density functional theory (DFT) to compute the work function of the AO-terminated (001) surface of SrVO₃, the effect of Ba surface doping on the work function, the energetic driving force for Ba segregation to the surface, and the adsorption stability of Ba-O dipoles on SrVO₃, Sc₂O₃, and W. The goal is to obtain physically consistent numerical values for these quantities, which together indicate the potential of SrVO₃ as a stable, low-work-function electron emitter.

## Approach
Use an open-source DFT code (e.g., Quantum ESPRESSO, GPAW, ABINIT) that supports the HSE hybrid functional and the PBE functional. Relax the bulk structures of SrVO₃ (cubic Pm-3m) with HSE at an appropriate Hartree-Fock exchange fraction, and of rocksalt SrO and BaO with PBE to obtain reference total energies. From the relaxed bulk, build AO-terminated (001) slabs of SrVO₃ with sufficient vacuum; compute the work functions of the pristine surface and of the surface with the top SrO layer replaced by BaO using HSE. Calculate substitution energies for Ba at a surface and a bulk-like interior position using the slab and rocksalt reference energies to obtain the segregation energy. For the adsorption energies, construct W(001) and Sc₂O₃(011) slabs with Ba-O adsorbates at known coverages, compute total energies of the clean and adsorbate-covered slabs with PBE, and calculate the adsorption energy per Ba atom relative to rocksalt BaO. All structures are built from public crystal structure databases (e.g., the Materials Project) or from literature data; pseudopotentials compatible with the chosen functional must be acquired. The workflow is divided into three ordered steps: relax SrVO₃, relax SrO and BaO, and then compute and collect the six target quantities into a structured JSON file.

## Reproduction target
Compute and report the following six quantities in the file /app/outputs/results.json:

- φ_AO_pristine: work function (eV) of the AO-terminated (001) SrVO₃ slab without doping.
- φ_AO_Ba_surface: work function (eV) of the same slab with the top SrO layer replaced by a full BaO layer.
- segregation_energy: the Ba segregation energy (eV/Ba atom), defined as the difference between the Ba substitution energy at the surface and the Ba substitution energy in a bulk-like interior layer.
- adsorption_energy_SrVO3: adsorption energy (eV/Ba atom) of Ba-O on SrVO₃(001) relative to rocksalt BaO.
- adsorption_energy_Sc2O3: adsorption energy (eV/Ba atom) of Ba-O on Sc₂O₃(011) relative to rocksalt BaO.
- adsorption_energy_W: adsorption energy (eV/Ba atom) of Ba-O on W(001) relative to rocksalt BaO.

All values must be reported as numbers (floats) using the exact keys and units specified in the output contract. The computed values should be physically reasonable but their exact magnitude is determined by your DFT calculation.

## Assets

- Quantum ESPRESSO or equivalent open-source DFT code supporting HSE: https://www.quantum-espresso.org/
- Pseudopotentials for Sr, V, O, Ba, Sc, W: http://www.physics.rutgers.edu/gbrv/
- Crystal structures for SrVO3 (cubic Pm-3m), SrO (rocksalt), BaO (rocksalt), Sc2O3 (bixbyite), W (bcc): https://materialsproject.org/

## Workflow steps

### Step 1: Relax bulk SrVO₃ using HSE
- Role: process
- Action: Obtain or construct the cubic SrVO₃ unit cell (Pm-3m) and relax the cell shape and ionic positions using the HSE functional with a Hartree-Fock exchange fraction appropriate for SrVO₃ (the paper uses 0.125). This yields the equilibrium bulk structure.
- Evidence: `/app/outputs/relax_srvo3.log`

### Step 2: Relax rocksalt SrO and BaO using PBE
- Role: process
- Action: Build rocksalt SrO and BaO unit cells and relax their lattice constants and ionic positions using the PBE functional. These total energies serve as reference states in the substitution/adsorption energy formulas.
- Evidence: `/app/outputs/relax_references.log`

### Step 3: Compute work functions, segregation energy, and adsorption energies
- Role: scored (load-bearing)
- Action: Using the relaxed structures, build AO-terminated (001) SrVO₃ slabs with and without a BaO surface layer, and compute their work functions (HSE). Build a slab with Ba substituted at a bulk-like interior position to compute the bulk substitution energy, and use the surface-substituted and rocksalt reference energies to derive the segregation energy (difference between surface and bulk substitution energies). Construct W(001) and Sc₂O₃(011) slabs with Ba-O adsorbates at the coverages described in the paper (1/4 ML on W, 7/8 ML on Sc₂O₃) using GGA-PBE, compute total energies of clean and adsorbate-covered slabs, and combine with the rocksalt BaO energy to calculate adsorption energies per Ba atom relative to BaO. Write all six final values into a JSON file at /app/outputs/results.json with keys phi_AO_pristine (eV), phi_AO_Ba_surface (eV), segregation_energy (eV/Ba), adsorption_energy_SrVO3 (eV/Ba), adsorption_energy_Sc2O3 (eV/Ba), adsorption_energy_W (eV/Ba).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"phi_AO_pristine": float (eV), "phi_AO_Ba_surface": float (eV), "segregation_energy": float (eV/Ba), "adsorption_energy_SrVO3": float (eV/Ba), "adsorption_energy_Sc2O3": float (eV/Ba), "adsorption_energy_W": float (eV/Ba)}
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
- target_policy: reference_match
- description: JSON file containing the six target quantities: two work functions, the Ba segregation energy, and three adsorption energies. The checker compares each value to the paper's reference using hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `phi_AO_pristine`: number (eV)
    - `phi_AO_Ba_surface`: number (eV)
    - `segregation_energy`: number (eV/Ba)
    - `adsorption_energy_SrVO3`: number (eV/Ba)
    - `adsorption_energy_Sc2O3`: number (eV/Ba)
    - `adsorption_energy_W`: number (eV/Ba)

Notes: This task reproduces the key elements of the paper’s SrVO₃/Ba doping study: the AO‑terminated work functions, the Ba surface‑segregation driving force, and the relative stability of Ba–O dipoles on SrVO₃ vs conventional substrates. The workflow requires running HSE and PBE slab calculations, which are computationally demanding but feasible with appropriate hardware.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phi_AO_pristine": "number (eV)",
          "phi_AO_Ba_surface": "number (eV)",
          "segregation_energy": "number (eV/Ba)",
          "adsorption_energy_SrVO3": "number (eV/Ba)",
          "adsorption_energy_Sc2O3": "number (eV/Ba)",
          "adsorption_energy_W": "number (eV/Ba)"
        }
      },
      "description": "JSON file containing the six target quantities: two work functions, the Ba segregation energy, and three adsorption energies. The checker compares each value to the paper's reference using hidden tolerances."
    }
  ],
  "notes": "This task reproduces the key elements of the paper’s SrVO₃/Ba doping study: the AO‑terminated work functions, the Ba surface‑segregation driving force, and the relative stability of Ba–O dipoles on SrVO₃ vs conventional substrates. The workflow requires running HSE and PBE slab calculations, which are computationally demanding but feasible with appropriate hardware."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/results.json and compare each reported value against a set of hidden reference values obtained from peer-reviewed work. The verifier uses tolerances that absorb legitimate differences between DFT implementations and pseudopotential choices, but reject values that are physically implausible or that could be guessed without performing the calculations. In addition, the verifier will check that the ordering of the three adsorption energies is physically consistent. Your final reward is a weighted sum of the per-field scores. Simply writing down approximate numbers is not sufficient; you must genuinely execute the DFT pipeline and report the values that it produces.
