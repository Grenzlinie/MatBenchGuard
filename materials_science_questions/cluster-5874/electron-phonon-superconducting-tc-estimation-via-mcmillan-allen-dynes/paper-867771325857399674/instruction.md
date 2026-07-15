# Electron-Phonon Coupling and Superconducting Tc for δ-Ti at 140 GPa via DFT/DFPT

## Problem background
Superconductivity in elemental metals under high pressure provides a clean testbed for the Bardeen-Cooper-Schrieffer (BCS) theory and the electron-phonon coupling (EPC) mechanism. Titanium (Ti) undergoes a structural phase sequence α → ω → γ → δ → β under compression, with the δ phase (Cmcm) stable above ~140 GPa. Experimental measurements show that δ-Ti exhibits superconductivity, and first-principles calculations can reveal the underlying EPC strength and the resulting critical temperature (Tc). In particular, the δ-Ti phase at 140 GPa is a prime candidate for studying strong electron-phonon coupling driven by Fermi surface nesting and phonon softening, which can be quantified by the EPC constant λ, the logarithmic average phonon frequency ω_log, and the acoustic phonon contribution fraction.

## Approach
Use density functional theory (DFT) and density-functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO, with a GGA-PBE PAW pseudopotential for Ti. The crystal structure of Cmcm δ-Ti at 140 GPa is taken from published literature. Perform a self-consistent field (SCF) calculation to obtain the electronic ground state, then compute phonon dispersions and the dynamical matrix on a uniform q-point grid. From the phonon data, calculate the Eliashberg spectral function α²F(ω) and the cumulative frequency-dependent EPC parameter λ(ω). Extract the total λ and ω_log, then compute the superconducting critical temperature Tc using the McMillan-Allen-Dynes formula with a Coulomb pseudopotential μ* = 0.19. Additionally, compute the fraction of λ contributed by phonon modes with frequency ≤ 120 cm⁻¹ (the acoustic fraction). All intermediate steps produce supporting output files; the four target quantities are written to a single JSON file.

## Reproduction target
Produce a file `delta_Ti_140GPa_results.json` containing four float values computed solely from the DFT/DFPT workflow: (1) the electron-phonon coupling constant `lambda` (dimensionless), (2) the logarithmic average phonon frequency `omega_log` (in K), (3) the superconducting critical temperature `Tc` (in K) obtained via the McMillan-Allen-Dynes formula with μ* = 0.19, and (4) the acoustic fraction `acoustic_fraction` (dimensionless, between 0 and 1) defined as the ratio λ(120 cm⁻¹) / λ, i.e., the fraction of the total EPC due to phonon modes with frequency ≤ 120 cm⁻¹. The JSON object must use these exact keys. The target is to obtain these values from a faithful reproduction of the DFT/DFPT workflow; the gold reference values are not provided.

## Assets

- δ-Ti crystal structure (Cmcm) at 140 GPa: 10.1103/PhysRevLett.87.275503
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ti PAW pseudopotential (GGA-PBE): https://www.materialscloud.org/discover/sssp/package/efficiency

## Workflow steps

### Step 1: Prepare crystal structure input
- Role: process
- Action: Construct the Quantum ESPRESSO input file for δ-Ti (Cmcm) at 140 GPa using lattice parameters and atomic positions from the published literature (Akahama et al. or Vohra & Spencer).
- Evidence: `/app/outputs/delta_ti.scf.in`

### Step 2: SCF ground state calculation
- Role: process
- Action: Run pw.x to obtain the self-consistent charge density and wavefunctions for δ-Ti.
- Evidence: `/app/outputs/delta_ti.scf.out`

### Step 3: DFPT phonon calculation
- Role: process
- Action: Run ph.x on a q-point grid, followed by q2r.x and matdyn.x to obtain phonon frequencies and eigenvectors across the Brillouin zone.
- Evidence: `/app/outputs/delta_ti.ph.out`

### Step 4: Electron-phonon coupling calculation
- Role: process
- Action: Run lambda.x (or equivalent) using the phonon data to produce the Eliashberg spectral function α²F(ω) and cumulative EPC λ(ω).
- Evidence: `/app/outputs/delta_ti.elph.out`

### Step 5: Scored EPC and Tc results
- Role: scored (load-bearing)
- Action: From the λ(ω) data compute: (1) total λ = λ(∞); (2) ω_log from the α²F(ω) integration; (3) Tc via the McMillan-Allen-Dynes formula with μ*=0.19; (4) acoustic fraction = λ(120 cm⁻¹) / λ (contribution from modes ≤ 120 cm⁻¹). Write all four quantities to delta_Ti_140GPa_results.json.
- Output file: `/app/outputs/delta_Ti_140GPa_results.json`
- Format: json
- Contract: JSON object with keys: lambda (float), omega_log (float, in K), Tc (float, in K), acoustic_fraction (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_Ti_140GPa_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_Ti_140GPa_results.json
- path: `/app/outputs/delta_Ti_140GPa_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed electron-phonon coupling constant λ, logarithmic average phonon frequency ω_log, superconducting critical temperature Tc from the McMillan-Allen-Dynes formula with μ*=0.19, and the fractional contribution of acoustic phonons (below 120 cm⁻¹) to λ.
- schema:
  - `type`: object
  - `required`:
    - `lambda`: float (dimensionless)
    - `omega_log`: float (K)
    - `Tc`: float (K)
    - `acoustic_fraction`: float (dimensionless, between 0 and 1)

Notes: The agent must run the full DFT/DFPT workflow to obtain λ(ω) and α²F(ω), then compute the four quantities. The hidden checker compares each value to the paper-reported gold within absolute tolerances. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_Ti_140GPa_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lambda": "float (dimensionless)",
          "omega_log": "float (K)",
          "Tc": "float (K)",
          "acoustic_fraction": "float (dimensionless, between 0 and 1)"
        }
      },
      "description": "The computed electron-phonon coupling constant λ, logarithmic average phonon frequency ω_log, superconducting critical temperature Tc from the McMillan-Allen-Dynes formula with μ*=0.19, and the fractional contribution of acoustic phonons (below 120 cm⁻¹) to λ."
    }
  ],
  "notes": "The agent must run the full DFT/DFPT workflow to obtain λ(ω) and α²F(ω), then compute the four quantities. The hidden checker compares each value to the paper-reported gold within absolute tolerances. No gold values or tolerances are revealed here."
}
```

## How you are scored
A hidden verifier reads your `delta_Ti_140GPa_results.json` and compares each of the four quantities to a hidden reference value (derived from the paper's reported results) using absolute tolerances. Each quantity that falls within its tolerance earns partial credit; the final reward is proportional to the number of passing quantities. The verifier does not re-run the DFT calculations; it performs a lightweight numerical comparison. Reporting numbers alone without executing the workflow will not systematically pass, because the tolerances are chosen to require a genuine computational reproduction. The exact tolerances and reference values are not disclosed.
