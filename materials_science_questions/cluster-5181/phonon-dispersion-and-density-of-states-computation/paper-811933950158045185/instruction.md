# DFT Calculation of E2g2 Phonon Frequency Shift in Photoexcited Graphite

## Problem background
Graphite has a quasi-two-dimensional electronic structure with strong electron-phonon coupling near the Fermi level. Under femtosecond laser excitation, a non-equilibrium electron-hole plasma is created, which can alter the vibrational properties of the lattice through changes in the electron-phonon interaction. The in-plane E2g2 optical phonon mode is particularly sensitive to the electronic occupation. First-principles density-functional theory (DFT) calculations that account for nonadiabatic effects provide a way to quantify how different nonequilibrium electronic distributions shift the phonon frequency. This task computes the E2g2 phonon frequency shift for a single graphite layer under four photoexcited distribution models, as a function of the excitation charge density.

## Approach
We perform DFT calculations within the local-density approximation (LDA) using the ABINIT package and a norm-conserving Troullier-Martins pseudopotential for carbon. A single graphite sheet is modeled with its known hexagonal lattice constant. The equilibrium E2g2 phonon frequency at the Γ point is obtained via density-functional perturbation theory (DFPT). To simulate the effect of a photoexcited electron-hole plasma, the dynamical matrix is computed with fixed electronic occupations that represent four limiting nonequilibrium distributions:
1. As-excited distribution (AED) — electrons promoted from the π band to the π* band by vertical transitions at a fixed photon energy.
2. Nonthermal distribution (NTD) — a depletion window around the Fermi level, mimicking ultrafast relaxation before thermalization.
3. Hot thermal distribution (TD) — Fermi-Dirac statistics with an elevated electronic temperature corresponding to the excited charge density.
4. Ionized distribution (ID) — electrons removed from the top of the π band (hole doping).
For each distribution, the phonon frequency is computed at several excitation charge densities spanning the range 0.001–0.01 electrons per atom. The frequency shift Δω₂ (in THz) is recorded relative to the equilibrium value. The required computational parameters (plane-wave cutoff, k-point mesh) are chosen to converge the phonon frequency to high precision.

## Reproduction target
Compute the E2g2 phonon frequency shift (in THz) for a single graphite layer under the four electronic occupation distributions listed above, as a function of excitation charge density. Produce a CSV file (`frequency_shifts.csv`) containing at least four density values per distribution, covering 0.001–0.01 electrons/atom. Each row must report the distribution label (AED, NTD, TD, or ID), the density, and the corresponding frequency shift.

## Assets

- ABINIT DFT package: https://www.abinit.org/downloads
- Troullier-Martins pseudopotential for carbon: https://www.abinit.org/sites/default/files/pspnc/NC/C.pspnc
- Graphite crystal structure parameters

## Workflow steps

### Step 1: DFT Phonon Frequency Shift Calculation
- Role: scored (load-bearing)
- Action: Using DFT (local-density approximation) and density-functional perturbation theory with a norm-conserving pseudopotential for carbon, set up a single graphite layer with the known hexagonal lattice constant (a=2.46 Å). Compute the equilibrium E2g2 phonon frequency at the Γ point. Then, for each excitation charge density in the range 0.001–0.01 electrons per atom, compute the E2g2 phonon frequency under fixed electronic occupations that model four different photoexcited distributions: (1) as-excited distribution (AED) — vertical transitions with 3.1 eV photons; (2) nonthermal distribution (NTD) — a depleted energy window around the Fermi level; (3) hot thermal distribution (TD) — Fermi-Dirac with a high electronic temperature corresponding to the charge density; (4) ionized distribution (ID) — electrons removed from the top of the π band. Record the frequency shift Δω₂ (in THz) relative to the equilibrium frequency for each (distribution, density) pair.
- Output file: `/app/outputs/frequency_shifts.csv`
- Format: csv
- Contract: Columns: distribution (string, values: AED, NTD, TD, ID), density (float, electrons/atom), frequency_shift_THz (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequency_shifts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequency_shifts.csv
- path: `/app/outputs/frequency_shifts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the computed E2g2 phonon frequency shift for each (distribution, density) pair. The checker compares these shifts to reference values extracted from the paper's Figure 4 and also verifies monotonic ordering and relative magnitude across distributions.
- schema:
  - `type`: table
  - `required_columns`: `distribution`, `density`, `frequency_shift_THz`
  - `units`:
    - `density`: electrons/atom
    - `frequency_shift_THz`: THz

Notes: The agent must compute shifts for at least 4 distinct densities per distribution. The hidden checker verifies: (a) frequency shift is positive and increases monotonically with density for each distribution; (b) at any given density the shift ordering is ID > TD > NTD > AED; (c) the magnitude falls within a tolerance band derived from Fig. 4 of the paper. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequency_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distribution",
          "density",
          "frequency_shift_THz"
        ],
        "units": {
          "density": "electrons/atom",
          "frequency_shift_THz": "THz"
        }
      },
      "description": "CSV file containing the computed E2g2 phonon frequency shift for each (distribution, density) pair. The checker compares these shifts to reference values extracted from the paper's Figure 4 and also verifies monotonic ordering and relative magnitude across distributions."
    }
  ],
  "notes": "The agent must compute shifts for at least 4 distinct densities per distribution. The hidden checker verifies: (a) frequency shift is positive and increases monotonically with density for each distribution; (b) at any given density the shift ordering is ID > TD > NTD > AED; (c) the magnitude falls within a tolerance band derived from Fig. 4 of the paper. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier evaluates your `frequency_shifts.csv` by comparing your reported frequency shifts to hidden reference values derived from published DFT calculations. The verifier also checks internal consistency relationships among the shifts (e.g., monotonic behavior with density and relative ordering across distributions). The final reward is computed as a weighted combination of these checks. You are not given the reference values or the exact tolerances; your task is to faithfully implement the described DFT+DFPT methodology and report the resulting shifts. Higher agreement with the hidden reference yields a higher score.
