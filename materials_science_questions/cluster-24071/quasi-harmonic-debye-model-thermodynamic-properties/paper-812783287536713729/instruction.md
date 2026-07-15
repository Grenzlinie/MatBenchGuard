# First-principles quasi-harmonic thermodynamic properties of TiAl intermetallics

## Problem background
γ-TiAl and α2-Ti3Al are the two principal intermetallic phases in titanium aluminide alloys that are attractive for high-temperature structural applications due to low density, good specific strength, and oxidation resistance. Accurate knowledge of their anisotropic thermal expansion coefficients and thermodynamic properties (heat capacity, bulk modulus) across the operational temperature range is essential for predicting microstructural evolution, internal stresses, and component durability. Experimental measurements are scarce, especially for the α2 phase, and often affected by alloying element additions and multiphase interactions. First-principles calculations within the quasi-harmonic approximation (QHA) can fill this gap, but the standard treatment assumes that the cell shape (c/a ratio) is determined solely by the volume and does not depend directly on temperature. The present work instead investigates two approaches: (i) the conventional `ground-state optimized cell shape` (gs‑cs) where c/a is a function of volume only, and (ii) a more rigorous `temperature-optimized cell shape` (to‑cs) where the Helmholtz free energy is minimized with respect to c/a at each temperature, thereby decoupling temperature and volume effects on the cell geometry. The task is to compute and compare the full suite of thermodynamic quantities for both phases using both methods, and to provide convenient analytical fits for the to‑cs results.

## Approach
The workflow starts with density functional theory (DFT) calculations using Quantum ESPRESSO to obtain the 0 K total energy E(V) and the ground-state lattice parameters a0(V), c0(V) over a range of volumes around equilibrium. Phonon spectra are then computed with phonopy on supercells to obtain the vibrational Helmholtz free energy F_vib(T,V). In the gs‑cs approach, the quasi-harmonic approximation (phonopy‑qha) combines E(V) and F_vib(T,V) to yield the temperature-dependent equilibrium volume V(T); the lattice constants are then recovered via the relationship x(T) = x0(V(T)) that maps zero‑temperature optimised geometry onto temperature‑volume results, and thermal expansion coefficients αa, αc are obtained by numerical differentiation (central differences). Heat capacity Cp is evaluated from the second temperature derivative of the Helmholtz free energy, and bulk modulus B from fitting the Birch–Murnaghan equation of state at each temperature.

For the to‑cs treatment, additional DFT total-energy calculations are performed for several c/a ratios at each volume, yielding E_tot(V, c/a). Phonon calculations for these (V, c/a) configurations give F_vib(T, V, c/a). The total free energy F(T, V, c/a) = E_tot + F_vib is constructed, and at each temperature the free energy is minimized with respect to c/a (fit with a quadratic polynomial) to obtain F(T, V). The resulting free energy versus volume is then fitted with the Birch–Murnaghan equation of state to extract the equilibrium volume V0(T), bulk modulus B(T), and the optimal c/a(T). From the temperature-dependent lattice parameters a(T), c(T) deduced from V(T) and c/a(T), the anisotropic expansion coefficients and heat capacity are computed analogously.

Finally, the to‑cs quantities for both phases are fitted to a multi‑term analytical expression of the form X(T) = a0 + Σᵢ aᵢ Tⁱ + Σᵢ bᵢ T⁻ⁱ + c ln(T) (with four polynomial and four inverse‑power terms plus a logarithm) to provide compact functional forms usable in higher‑level modeling.

## Reproduction target
Compute the temperature‑dependent specific volume, c/a ratio, Helmholtz free energy, anisotropic thermal expansion coefficients αa and αc, constant‑pressure heat capacity Cp, and bulk modulus B for stoichiometric γ‑TiAl (tetragonal L1₀) and α2‑Ti₃Al (hexagonal D0₁₉) for both the gs‑cs and to‑cs approaches over the temperature range 0 to 1000 K in steps of 10 K. Assemble the results into two comma‑separated value (CSV) files, one per phase, with the columns: T, V_atom_gs_cs, V_atom_to_cs, c_a_gs_cs, c_a_to_cs, F_gs_cs, F_to_cs, alpha_a_gs_cs, alpha_a_to_cs, alpha_c_gs_cs, alpha_c_to_cs, Cp_gs_cs, Cp_to_cs, B_gs_cs, B_to_cs (units as defined in the contract). For the to‑cs data, fit the temperature‑dependent quantities F, Cp, B, αa, αc to the analytical form described in the approach and store the fitted coefficients (a0…a4, b1…b4, c per quantity) in a JSON file `analytical_fits.json` with the top‑level keys `gamma_TiAl` and `alpha2_Ti3Al`. All output files must be placed under `/app/outputs`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- phonopy: https://phonopy.github.io/phonopy/
- phonopy-qha: https://phonopy.github.io/phonopy/qha.html
- SSSP Efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structures of γ-TiAl and α2-Ti3Al

## Workflow steps

### Step 1: DFT structural optimization over volume range
- Role: process
- Action: Perform DFT structural optimization for γ-TiAl and α2-Ti3Al across a set of volumes around equilibrium, relaxing cell shape and internal coordinates to obtain 0 K total energy E(V) and lattice parameters a0(V), c0(V).
- Evidence: `/app/outputs/evidence_dft_volumes.txt`

### Step 2: Phonon calculations for volume-optimized structures (gs-cs)
- Role: process
- Action: For each volume from the previous step, construct a supercell, compute phonon frequencies and the harmonic vibrational Helmholtz free energy F_vib(T,V). The cell shape is kept at the ground-state optimized values.
- Evidence: `/app/outputs/evidence_phonon_gs_cs.txt`

### Step 3: Quasi-harmonic volume and gs-cs properties
- Role: process
- Action: Combine E(V) and F_vib(T,V) to obtain temperature-dependent equilibrium volume V_gs(T) and free energy F_gs(T) using phonopy-qha. Then derive gs-cs lattice constants a(T), c(T) and compute thermal expansion coefficients and heat capacity.
- Evidence: `/app/outputs/evidence_gs_cs_properties.npz`

### Step 4: DFT calculations for c/a-varied configurations
- Role: process
- Action: For each volume from the volume range, perform DFT total-energy calculations at several c/a ratios around the equilibrium values for both phases, fixing the cell shape and relaxing internal coordinates. Obtain E_tot(V, c/a).
- Evidence: `/app/outputs/evidence_dft_ca_varied.txt`

### Step 5: Phonon calculations for c/a-varied configurations
- Role: process
- Action: For each (V, c/a) configuration, compute phonon frequencies and the harmonic vibrational Helmholtz free energy F_vib(T, V, c/a).
- Evidence: `/app/outputs/evidence_phonon_ca_varied.txt`

### Step 6: to-cs free energy minimization and property derivation
- Role: process
- Action: Construct total Helmholtz free energy F(T,V,c/a) = E_tot(V,c/a) + F_vib(T,V,c/a). For each temperature, minimize with respect to c/a, fit the resulting F(T,V) with the Birch–Murnaghan equation of state to obtain equilibrium volume, bulk modulus, and optimal c/a(T). Then compute lattice parameters, thermal expansion coefficients, and heat capacity for both phases.
- Evidence: `/app/outputs/evidence_to_cs_properties.npz`

### Step 7: Compile γ-TiAl properties CSV
- Role: scored (load-bearing)
- Action: Combine the computed gs-cs and to-cs data for γ-TiAl into a CSV file with columns for temperature, specific volumes, c/a ratios, free energies, expansion coefficients, heat capacities, and bulk modulus. Temperature range 0–1000 K in 10 K steps.
- Output file: `/app/outputs/gamma_TiAl_properties.csv`
- Format: csv
- Contract: CSV with columns: T, V_atom_gs_cs, V_atom_to_cs, c_a_gs_cs, c_a_to_cs, F_gs_cs, F_to_cs, alpha_a_gs_cs, alpha_a_to_cs, alpha_c_gs_cs, alpha_c_to_cs, Cp_gs_cs, Cp_to_cs, B_gs_cs, B_to_cs. Units: T in K, V in Å³/atom, c/a dimensionless, F in eV/atom, alpha in K⁻¹, Cp in J/K/mol, B in GPa.
- Scoring: scored by hidden verifier

### Step 8: Compile α2-Ti3Al properties CSV
- Role: scored (load-bearing)
- Action: Combine the computed gs-cs and to-cs data for α2-Ti3Al into a CSV file with the same column structure as the γ-TiAl file.
- Output file: `/app/outputs/alpha2_Ti3Al_properties.csv`
- Format: csv
- Contract: CSV with columns: T, V_atom_gs_cs, V_atom_to_cs, c_a_gs_cs, c_a_to_cs, F_gs_cs, F_to_cs, alpha_a_gs_cs, alpha_a_to_cs, alpha_c_gs_cs, alpha_c_to_cs, Cp_gs_cs, Cp_to_cs, B_gs_cs, B_to_cs. Units: T in K, V in Å³/atom, c/a dimensionless, F in eV/atom, alpha in K⁻¹, Cp in J/K/mol, B in GPa.
- Scoring: scored by hidden verifier

### Step 9: Analytical fitting of to-cs quantities
- Role: scored
- Action: Fit the to-cs temperature-dependent data (Helmholtz free energy F, heat capacity Cp, bulk modulus B, and expansion coefficients αa, αc) for both phases to the multi-term expression given in the paper's Eq. A1. Save the fitted coefficients in a JSON file.
- Output file: `/app/outputs/analytical_fits.json`
- Format: json
- Contract: JSON object with keys 'gamma_TiAl' and 'alpha2_Ti3Al'. Each contains a dict with keys F, Cp, B, alpha_a, alpha_c. Each value is a dict with keys a0, a1, a2, a3, a4 (arrays of floats), b1, b2, b3, b4 (arrays of floats), and c (float). Coefficients correspond to the analytical form Eq. A1 using units described in the paper.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_TiAl_properties.csv`
- `/app/outputs/alpha2_Ti3Al_properties.csv`
- `/app/outputs/analytical_fits.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_TiAl_properties.csv
- path: `/app/outputs/gamma_TiAl_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent thermodynamic properties of γ-TiAl from gs-cs and to-cs approaches, 0–1000 K at 10 K intervals.
- schema:
  - `type`: table
  - `required_columns`: `T`, `V_atom_gs_cs`, `V_atom_to_cs`, `c_a_gs_cs`, `c_a_to_cs`, `F_gs_cs`, `F_to_cs`, `alpha_a_gs_cs`, `alpha_a_to_cs`, `alpha_c_gs_cs`, `alpha_c_to_cs`, `Cp_gs_cs`, `Cp_to_cs`, `B_gs_cs`, `B_to_cs`
  - `units`:
    - `T`: K
    - `V_atom_gs_cs`: Å³/atom
    - `V_atom_to_cs`: Å³/atom
    - `c_a_gs_cs`: dimensionless
    - `c_a_to_cs`: dimensionless
    - `F_gs_cs`: eV/atom
    - `F_to_cs`: eV/atom
    - `alpha_a_gs_cs`: K⁻¹
    - `alpha_a_to_cs`: K⁻¹
    - `alpha_c_gs_cs`: K⁻¹
    - `alpha_c_to_cs`: K⁻¹
    - `Cp_gs_cs`: J/K/mol
    - `Cp_to_cs`: J/K/mol
    - `B_gs_cs`: GPa
    - `B_to_cs`: GPa

### alpha2_Ti3Al_properties.csv
- path: `/app/outputs/alpha2_Ti3Al_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent thermodynamic properties of α2-Ti3Al from gs-cs and to-cs approaches, 0–1000 K at 10 K intervals.
- schema:
  - `type`: table
  - `required_columns`: `T`, `V_atom_gs_cs`, `V_atom_to_cs`, `c_a_gs_cs`, `c_a_to_cs`, `F_gs_cs`, `F_to_cs`, `alpha_a_gs_cs`, `alpha_a_to_cs`, `alpha_c_gs_cs`, `alpha_c_to_cs`, `Cp_gs_cs`, `Cp_to_cs`, `B_gs_cs`, `B_to_cs`
  - `units`:
    - `T`: K
    - `V_atom_gs_cs`: Å³/atom
    - `V_atom_to_cs`: Å³/atom
    - `c_a_gs_cs`: dimensionless
    - `c_a_to_cs`: dimensionless
    - `F_gs_cs`: eV/atom
    - `F_to_cs`: eV/atom
    - `alpha_a_gs_cs`: K⁻¹
    - `alpha_a_to_cs`: K⁻¹
    - `alpha_c_gs_cs`: K⁻¹
    - `alpha_c_to_cs`: K⁻¹
    - `Cp_gs_cs`: J/K/mol
    - `Cp_to_cs`: J/K/mol
    - `B_gs_cs`: GPa
    - `B_to_cs`: GPa

### analytical_fits.json
- path: `/app/outputs/analytical_fits.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted coefficients for analytical expressions of to-cs thermodynamic properties (Eq. A1) for both phases. The object contains gamma_TiAl and alpha2_Ti3Al keys, each with sub-keys F, Cp, B, alpha_a, alpha_c. Each sub-key holds coefficient arrays a0..a4, b1..b4 and c as described in the paper.
- schema:
  - `type`: object
  - `required`: `gamma_TiAl`, `alpha2_Ti3Al`

Notes: The checker compares the agent's CSV data at selected temperatures and the fitted coefficients against hidden reference values digitized from the paper, using relative tolerances appropriate for a different DFT code. It also checks physical trends (e.g., alpha_a > alpha_c for gamma to-cs, Cp approaching Dulong-Petit limit).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_TiAl_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "V_atom_gs_cs",
          "V_atom_to_cs",
          "c_a_gs_cs",
          "c_a_to_cs",
          "F_gs_cs",
          "F_to_cs",
          "alpha_a_gs_cs",
          "alpha_a_to_cs",
          "alpha_c_gs_cs",
          "alpha_c_to_cs",
          "Cp_gs_cs",
          "Cp_to_cs",
          "B_gs_cs",
          "B_to_cs"
        ],
        "units": {
          "T": "K",
          "V_atom_gs_cs": "Å³/atom",
          "V_atom_to_cs": "Å³/atom",
          "c_a_gs_cs": "dimensionless",
          "c_a_to_cs": "dimensionless",
          "F_gs_cs": "eV/atom",
          "F_to_cs": "eV/atom",
          "alpha_a_gs_cs": "K⁻¹",
          "alpha_a_to_cs": "K⁻¹",
          "alpha_c_gs_cs": "K⁻¹",
          "alpha_c_to_cs": "K⁻¹",
          "Cp_gs_cs": "J/K/mol",
          "Cp_to_cs": "J/K/mol",
          "B_gs_cs": "GPa",
          "B_to_cs": "GPa"
        }
      },
      "description": "Temperature-dependent thermodynamic properties of γ-TiAl from gs-cs and to-cs approaches, 0–1000 K at 10 K intervals."
    },
    {
      "file": "alpha2_Ti3Al_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "V_atom_gs_cs",
          "V_atom_to_cs",
          "c_a_gs_cs",
          "c_a_to_cs",
          "F_gs_cs",
          "F_to_cs",
          "alpha_a_gs_cs",
          "alpha_a_to_cs",
          "alpha_c_gs_cs",
          "alpha_c_to_cs",
          "Cp_gs_cs",
          "Cp_to_cs",
          "B_gs_cs",
          "B_to_cs"
        ],
        "units": {
          "T": "K",
          "V_atom_gs_cs": "Å³/atom",
          "V_atom_to_cs": "Å³/atom",
          "c_a_gs_cs": "dimensionless",
          "c_a_to_cs": "dimensionless",
          "F_gs_cs": "eV/atom",
          "F_to_cs": "eV/atom",
          "alpha_a_gs_cs": "K⁻¹",
          "alpha_a_to_cs": "K⁻¹",
          "alpha_c_gs_cs": "K⁻¹",
          "alpha_c_to_cs": "K⁻¹",
          "Cp_gs_cs": "J/K/mol",
          "Cp_to_cs": "J/K/mol",
          "B_gs_cs": "GPa",
          "B_to_cs": "GPa"
        }
      },
      "description": "Temperature-dependent thermodynamic properties of α2-Ti3Al from gs-cs and to-cs approaches, 0–1000 K at 10 K intervals."
    },
    {
      "file": "analytical_fits.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma_TiAl",
          "alpha2_Ti3Al"
        ]
      },
      "description": "Fitted coefficients for analytical expressions of to-cs thermodynamic properties (Eq. A1) for both phases. The object contains gamma_TiAl and alpha2_Ti3Al keys, each with sub-keys F, Cp, B, alpha_a, alpha_c. Each sub-key holds coefficient arrays a0..a4, b1..b4 and c as described in the paper."
    }
  ],
  "notes": "The checker compares the agent's CSV data at selected temperatures and the fitted coefficients against hidden reference values digitized from the paper, using relative tolerances appropriate for a different DFT code. It also checks physical trends (e.g., alpha_a > alpha_c for gamma to-cs, Cp approaching Dulong-Petit limit)."
}
```

## How you are scored
Each scored workflow stage produces an artifact (`gamma_TiAl_properties.csv`, `alpha2_Ti3Al_properties.csv`, `analytical_fits.json`). A hidden verifier, which has access to reference data digitized from the original publication but hidden from you, will independently evaluate your artifacts. It will compare your computed values at selected temperature points against the reference data using prescribed relative tolerances and will check that expected physical trends hold (for example, monotonic temperature behaviour, the high‑temperature limit of the heat capacity approaching the Dulong–Petit value, and the relative ordering of expansion coefficients αa and αc). The analytical fit coefficients are compared directly to hidden target coefficients. The verifier assigns a score to each artifact and combines them by a predefined weighting to produce the final reward. Simply reporting the reference numbers without actually performing the calculations will likely not satisfy all consistency checks and tolerances; the verifier expects a genuine re‑computation of the pipeline.
