# First-Principles Electronic Band Structure and Lattice Thermal Conductivity of Zinc-Blende HgTe

## Problem background
Accurate first-principles description of the electronic band structure and lattice thermal conductivity of zinc-blende HgTe is challenging because standard semi-local exchange-correlation functionals (e.g., GGA-PBE) misrepresent the band ordering and spin-orbit splitting near the Fermi level. The material is a semi-metal with an inverted band structure, a large electron-hole effective mass ratio, and low thermal conductivity, making its transport properties sensitive to the choice of functional and the treatment of spin-orbit coupling. This task addresses the need for robust, reproducible computational predictions of the electronic band-edge properties and phonon-mediated heat transport in HgTe.

## Approach
The workflow is split into two independent computational pipelines. The first uses a hybrid exchange-correlation functional (HSE06) including spin-orbit coupling to compute the electronic band structure of zinc-blende HgTe along a high-symmetry path, from which the inverted band gap, spin-orbit splitting, and carrier effective masses are extracted at the Γ point. The second pipeline computes the lattice thermal conductivity by first obtaining harmonic phonon frequencies and group velocities via density-functional perturbation theory (DFPT), then constructing third-order anharmonic force constants, and finally solving the phonon Boltzmann transport equation variationally, including isotopic disorder scattering. The required inputs are the crystal structure (experimental lattice constant), open-source pseudopotentials, and natural isotopic abundances – all publicly available. The two pipelines yield five key quantities that are compared against previously reported theoretical values.

## Reproduction target
From the electronic band structure of zinc-blende HgTe computed with the HSE06 hybrid functional and spin-orbit coupling, extract the inverted band gap (Eg = E(Γ6) – E(Γ8)), spin-orbit splitting (Δ0 = E(Γ8) – E(Γ7)), conduction-band effective mass me along [100], and top valence-band effective mass mh along [100], all in units of eV and free-electron mass. Separately, from the solution of the phonon Boltzmann transport equation with three-phonon anharmonic and isotopic disorder scattering, extract the lattice thermal conductivity κL at 300 K. Submit these five values in the specified output files.

## Assets

- Crystal structure of zinc-blende HgTe
- Open-source DFT code supporting HSE06 and spin–orbit coupling: https://www.cp2k.org/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- D3Q code for third-order force constants and phonon BTE: https://github.com/affromero/d3q
- Pseudopotentials for Hg and Te: https://pseudopotentials.quantum-espresso.org/
- Natural isotopic abundances of Hg and Te

## Workflow steps

### Step 1: Electronic band structure simulation
- Role: process
- Action: Perform a DFT self‑consistent calculation for zinc‑blende HgTe using an open‑source code with the HSE06 hybrid exchange‑correlation functional and spin‑orbit coupling. Use the experimental lattice constant a = 6.460 Å. Compute the electronic band structure along a high‑symmetry path that includes at least L‑Γ‑X. Output the k‑point coordinates and the band energies (in eV) for all computed bands to a CSV file `bands.csv`.
- Evidence: `/app/outputs/bands.csv`

### Step 2: Electronic property extraction
- Role: scored (load-bearing)
- Action: From the band structure in `bands.csv`, identify the Γ6, Γ7, and Γ8 bands at the Γ point. Compute: the inverted band gap Eg = E(Γ6) – E(Γ8) (eV), the spin–orbit splitting Δ0 = E(Γ8) – E(Γ7) (eV). Determine the conduction‑band effective mass me and the top valence‑band effective mass mh along the [100] direction from the curvature of the band energies near Γ. Save the four values as a single‑row CSV with columns Eg,Delta0,me,mh.
- Output file: `/app/outputs/electronic_results.csv`
- Format: csv
- Contract: Columns: Eg (float, eV), Delta0 (float, eV), me (float, m0), mh (float, m0).
- Scoring: scored by hidden verifier

### Step 3: Phonon and lattice thermal conductivity simulation
- Role: process
- Action: Using Quantum ESPRESSO, compute the harmonic phonon frequencies and group velocities via density‑functional perturbation theory on a suitable q‑grid (LDA‑PZ pseudopotentials, kinetic energy cutoff 1360 eV). With the D3Q code, compute third‑order anharmonic force constants on a coarse q‑grid. Include isotopic disorder scattering using the natural isotopic compositions of Hg and Te. Solve the phonon Boltzmann transport equation (variational method) with a dense q‑grid interpolation to obtain the lattice thermal conductivity κL as a function of temperature for T = 100, 200, 300, 400, 500 K. Save temperature (K) and κL (W/mK) pairs to `thermal_conductivity.csv`.
- Evidence: `/app/outputs/thermal_conductivity.csv`

### Step 4: Thermal conductivity extraction at 300 K
- Role: scored (load-bearing)
- Action: From `thermal_conductivity.csv`, read the lattice thermal conductivity at T = 300 K. Output a JSON file `thermal_conductivity_results.json` with a single key `kappa_300K` whose value is the float number (W/mK).
- Output file: `/app/outputs/thermal_conductivity_results.json`
- Format: json
- Contract: JSON object: { 'kappa_300K': <float> } (units W/mK).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_results.csv`
- `/app/outputs/thermal_conductivity_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_results.csv
- path: `/app/outputs/electronic_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Single‑row CSV containing the inverted band gap, spin–orbit splitting, and effective masses determined from the HSE06+SOC band structure. The checker compares each value against a hidden paper‑reported reference using absolute‑deviation thresholds.
- schema:
  - `type`: table
  - `required_columns`: `Eg`, `Delta0`, `me`, `mh`
  - `columns`:
    - `Eg`:
      - `type`: float
      - `unit`: eV
    - `Delta0`:
      - `type`: float
      - `unit`: eV
    - `me`:
      - `type`: float
      - `unit`: m0
    - `mh`:
      - `type`: float
      - `unit`: m0

### thermal_conductivity_results.json
- path: `/app/outputs/thermal_conductivity_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: JSON object with the lattice thermal conductivity at 300 K computed from the phonon BTE. The checker compares the value to a hidden paper‑reported theoretical reference with an absolute tolerance.
- schema:
  - `type`: object
  - `required`: `kappa_300K`
  - `properties`:
    - `kappa_300K`:
      - `type`: float
      - `unit`: W/mK

Notes: The two scored artifacts correspond to the main reproducible computational quantities from the paper: electronic band‑edge properties and lattice thermal conductivity. Hidden tolerances are used to account for legitimate code‑to‑code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Eg",
          "Delta0",
          "me",
          "mh"
        ],
        "columns": {
          "Eg": {
            "type": "float",
            "unit": "eV"
          },
          "Delta0": {
            "type": "float",
            "unit": "eV"
          },
          "me": {
            "type": "float",
            "unit": "m0"
          },
          "mh": {
            "type": "float",
            "unit": "m0"
          }
        }
      },
      "description": "Single‑row CSV containing the inverted band gap, spin–orbit splitting, and effective masses determined from the HSE06+SOC band structure. The checker compares each value against a hidden paper‑reported reference using absolute‑deviation thresholds."
    },
    {
      "file": "thermal_conductivity_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "kappa_300K"
        ],
        "properties": {
          "kappa_300K": {
            "type": "float",
            "unit": "W/mK"
          }
        }
      },
      "description": "JSON object with the lattice thermal conductivity at 300 K computed from the phonon BTE. The checker compares the value to a hidden paper‑reported theoretical reference with an absolute tolerance."
    }
  ],
  "notes": "The two scored artifacts correspond to the main reproducible computational quantities from the paper: electronic band‑edge properties and lattice thermal conductivity. Hidden tolerances are used to account for legitimate code‑to‑code differences."
}
```

## How you are scored
A hidden verifier independently scores each artifact. The electronic quantities (Eg, Δ0, me, mh) are checked against reference values obtained from an HSE06+SOC calculation, using tolerance windows that absorb legitimate code-to-code differences. The lattice thermal conductivity at 300 K is checked similarly. Each scored artifact carries a weight; the final reward is a weighted combination of the per-artifact scores. Simply reporting the reference numbers is not sufficient – the verifier expects results that are consistent with a proper execution of the computational pipeline.
