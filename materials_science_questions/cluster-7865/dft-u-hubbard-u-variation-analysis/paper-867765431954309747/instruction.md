# Spin-Crossover Phase Diagram of Ferropericlase with Self-Consistent Hubbard U

## Problem background
Ferropericlase, (Mg,Fe)O, is the second most abundant mineral in the Earth's lower mantle. Iron in ferropericlase undergoes a pressure-induced spin crossover from a high-spin (HS, S=2) to a low-spin (LS, S=0) state, which strongly impacts density, elastic properties, and seismic signatures. Accurately predicting the pressure–temperature conditions of this crossover is essential for understanding mantle dynamics. In this task you will compute the spin-crossover phase diagram of ferropericlase at iron concentration x_Fe = 0.1875 using self-consistent Hubbard-corrected density functional theory (LDA+Usc). The calculations go beyond the ideal solid-solution model by explicitly treating non-ideal mixing of HS and LS states and accounting for vibrational, electronic, and magnetic contributions.

## Approach
The reproduction follows a self-consistent DFT+U scheme. The Hubbard U parameter is determined iteratively via density-functional perturbation theory (DFPT) separately for each pure spin state. Static energy‑volume curves are computed for pure HS (antiferromagnetic and ferromagnetic) and LS states, and a third-order Birch‑Murnaghan equation of state is fitted to obtain the static transition pressure. To capture non‑ideal mixing, intermediate HS/LS atomic configurations are enumerated for LS fractions n = 1/6,…,5/6 in the 64-atom supercell, their static energies are computed using the consistent Hubbard U, and Boltzmann‑weighted averaging produces the non‑ideal mixing energy and excess enthalpy as functions of pressure and LS fraction. Phonon spectra are calculated for the pure states with the finite‑displacement supercell method; quasiharmonic theory yields vibrational free energies. Combined with Mermin‑functional electronic free energies and an analytical magnetic entropy term, ideal Gibbs free energies G_HS and G_LS are constructed. Finally, the equilibrium LS fraction n(P,T) is obtained by minimizing the non‑ideal Gibbs free energy, incorporating the excess enthalpy. The resulting phase diagram is compared to the ideal mixing limit to examine the crossover width.

## Reproduction target
For the (Mg26Fe6)O32 supercell (x_Fe = 0.1875) produce three scored artifacts:

1. **Static HS→LS transition pressure** – the pressure (GPa) at which the enthalpy of the HS‑AFM state equals that of the LS state, obtained by fitting a third‑order Birch‑Murnaghan EOS to the static energy‑volume data.
2. **Raw non‑ideal mixing energies** – a CSV file containing, for each LS fraction and each inequivalent HS/LS atomic configuration, the multiplicity, volume, static energy, and spin label. The file must span at least 3–5 volumes covering the crossover pressure range.
3. **Spin‑crossover phase diagram** – a CSV file with equilibrium LS fraction (0–1) on a grid of pressure (0–140 GPa) and temperature (0–4500 K), obtained by numerical minimization of the non‑ideal Gibbs free energy (including vibrational, electronic, magnetic, and excess non‑ideal mixing contributions).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- qha (quasiharmonic free energy package): https://github.com/rmwentzcovitch/qha
- PSlibrary high-accuracy PAW datasets (Fe, Mg, O): https://dalcorso.github.io/pslibrary/
- Rocksalt MgO structure (conventional cell, lattice parameter ~4.2118 Å)

## Workflow steps

### Step 1: Self-consistent Hubbard U and static energies for pure HS and LS states
- Role: process
- Action: Using Quantum ESPRESSO with PSlibrary pseudopotentials, perform LDA+Usc calculations with density-functional perturbation theory to self-consistently determine the Hubbard U parameter and compute the total energies E(V) for the high-spin antiferromagnetic (HS-AFM), high-spin ferromagnetic (HS-FM), and low-spin (LS) states of the (Mg26Fe6)O32 supercell (x_Fe=0.1875). Run at a set of volumes covering the expected crossover pressure range (approx. 6.0–9.0 Å³/atom). Save the resulting E(V) data and Usc values.
- Evidence: `/app/outputs/pure_state_ev_data.csv`

### Step 2: Static HS–LS transition pressure from Birch–Murnaghan EOS
- Role: scored (load-bearing)
- Action: Fit the third-order Birch–Murnaghan equation of state to the HS-AFM and LS static energies from step s1. Compute the enthalpy H(P) and determine the pressure at which H(HS-AFM) equals H(LS). Write the transition pressure (in GPa) to static_transition_pressure.txt.
- Output file: `/app/outputs/static_transition_pressure.txt`
- Format: txt
- Contract: A single floating-point number in units of GPa, e.g. `66.2`.
- Scoring: scored by hidden verifier

### Step 3: Enumerate and compute energies of HS/LS mixing configurations
- Role: process
- Action: For each LS fraction n = 1/6, 2/6, 3/6, 4/6, 5/6 in the same (Mg26Fe6)O32 supercell, enumerate all non-equivalent atomic arrangements of high-spin and low-spin Fe ions. Using Quantum ESPRESSO with the self-consistent Hubbard U values from step s1, compute the static energy ε_i of every arrangement at several volumes. For each arrangement record multiplicity g_i and spin label.
- Evidence: `/app/outputs/config_energies_raw.csv`

### Step 4: Non-ideal mixing energies and excess enthalpy
- Role: scored (load-bearing)
- Action: For each LS fraction n, compute the Boltzmann-weighted non-ideal mixing energy E_nonideal(n) = Σ_i g_i p_i ε_i, where p_i is the Boltzmann factor. Evaluate at a few temperatures and at each studied volume. Extract excess static energy E_ex(n) = E_nonideal(n) – E_ideal(n). Fit E_nonideal(n) with a third-order Birch-Murnaghan equation of state to obtain pressure and excess enthalpy H_ex(P,n). Output the raw data as nonideal_mixing_energies.csv.
- Output file: `/app/outputs/nonideal_mixing_energies.csv`
- Format: csv
- Contract: CSV with columns: n (dimensionless fraction), configuration_index (integer), multiplicity (integer), volume (Ang^3/atom), static_energy (eV), spin_label (HS or LS). Multiple volumes per n.
- Scoring: scored by hidden verifier

### Step 5: Phonon calculations and vibrational free energy
- Role: process
- Action: Using the finite-displacement method as implemented in Phonopy with Quantum ESPRESSO forces, compute the vibrational density of states for the pure HS-AFM and LS states at every volume studied in step s1. Check that no imaginary frequencies exist. Then, within the quasiharmonic approximation and using the qha Python package, compute the vibrational free energy F_vib(V,T).
- Evidence: none

### Step 6: Assembly of ideal Gibbs free energies G_HS and G_LS
- Role: process
- Action: Combine: (a) static E(V) from step s1, (b) vibrational free energy from step s5, (c) electronic free energy computed with Mermin functional at temperatures 0–4500 K, and (d) analytical magnetic free energy G_mag = -k_B T x_Fe ln[m(2S+1)] with spin S=2, orbital m=3 for HS and S=0, m=1 for LS. Construct the ideal Gibbs free energies G_HS(P,T) and G_LS(P,T) on a dense (P,T) grid covering 0–140 GPa and 0–4500 K.
- Evidence: none

### Step 7: Spin-crossover phase diagram from non-ideal Gibbs free energy minimisation
- Role: scored (load-bearing)
- Action: Using the ideal Gibbs free energies G_HS and G_LS from step s6, magnetic entropy, and the excess enthalpy H_ex(P,n) from step s4, numerically solve the non-ideal Gibbs free energy minimization equation for equilibrium LS fraction n at a grid of pressures and temperatures. Output the resulting LS fractions as phase_diagram.csv.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), temperature_K (float), LS_fraction (float between 0 and 1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_transition_pressure.txt`
- `/app/outputs/nonideal_mixing_energies.csv`
- `/app/outputs/phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_transition_pressure.txt
- path: `/app/outputs/static_transition_pressure.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Static spin-crossover transition pressure at T=0 K for the AFM configuration.
- schema:
  - `type`: text
  - `description`: A single floating-point number in units of GPa, e.g. 66.2.

### nonideal_mixing_energies.csv
- path: `/app/outputs/nonideal_mixing_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw mixing energy data. The checker verifies combinatorial completeness (multiplicities sum to C(6,k) for each LS fraction) and schema integrity.
- schema:
  - `type`: table
  - `required_columns`: `n`, `configuration_index`, `multiplicity`, `volume`, `static_energy`, `spin_label`
  - `units`:
    - `n`: dimensionless fraction (LS fraction)
    - `configuration_index`: integer
    - `multiplicity`: integer
    - `volume`: Ang^3/atom
    - `static_energy`: eV
    - `spin_label`: HS or LS

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spin-crossover phase diagram. The checker audits structural consistency: LS fraction monotonicity with pressure and a broad mixed-spin regime.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `temperature_K`, `LS_fraction`
  - `units`:
    - `pressure_GPa`: GPa
    - `temperature_K`: K
    - `LS_fraction`: dimensionless fraction between 0 and 1

Notes: Scoring is structural (tier structural) because the verifier sandbox cannot recompute the DFT/thermodynamic calculations. The checker validates combinatorial completeness of mixing energies and monotonicity/range of the phase diagram.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_transition_pressure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number in units of GPa, e.g. 66.2."
      },
      "description": "Static spin-crossover transition pressure at T=0 K for the AFM configuration."
    },
    {
      "file": "nonideal_mixing_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "configuration_index",
          "multiplicity",
          "volume",
          "static_energy",
          "spin_label"
        ],
        "units": {
          "n": "dimensionless fraction (LS fraction)",
          "configuration_index": "integer",
          "multiplicity": "integer",
          "volume": "Ang^3/atom",
          "static_energy": "eV",
          "spin_label": "HS or LS"
        }
      },
      "description": "Raw mixing energy data. The checker verifies combinatorial completeness (multiplicities sum to C(6,k) for each LS fraction) and schema integrity."
    },
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "temperature_K",
          "LS_fraction"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "temperature_K": "K",
          "LS_fraction": "dimensionless fraction between 0 and 1"
        }
      },
      "description": "Spin-crossover phase diagram. The checker audits structural consistency: LS fraction monotonicity with pressure and a broad mixed-spin regime."
    }
  ],
  "notes": "Scoring is structural (tier structural) because the verifier sandbox cannot recompute the DFT/thermodynamic calculations. The checker validates combinatorial completeness of mixing energies and monotonicity/range of the phase diagram."
}
```

## How you are scored
A hidden verifier independently checks each output artifact against reference data from the original study and recomputes key quantities from your submitted raw data.

- **static_transition_pressure.txt**: The submitted value is compared to the expected T=0 AFM static transition pressure within a tolerance.
- **nonideal_mixing_energies.csv**: The verifier recomputes the Boltzmann‑weighted non‑ideal mixing energy and excess enthalpy from your table, checks structural integrity, and verifies thermodynamic consistency.
- **phase_diagram.csv**: The verifier uses your submitted mixing energies, together with hidden ideal free energy and magnetic entropy data, to recompute the equilibrium LS fraction at each (P,T) point and compares it to your submitted LS_fraction.

Each artifact carries a weight; the final reward is the weighted sum. Simply reporting a number, without executing the required DFT and phonon calculations, will not satisfy the verifier because the hidden recomputation depends on the raw data you supply.
