## Problem background

Silicene and germanene are two-dimensional buckled honeycomb materials with potential applications in electronics. Their thermal expansion and thermomechanical properties are critical for device reliability because accumulated thermal strain can affect performance and lifetime. The interplay between lattice dimensionality, bond characteristics, and functionalization in these materials needs to be understood quantitatively.

## Approach

Use first-principles density functional theory (DFT) to obtain the electronic total energy as a function of the in‑plane lattice constant and to compute harmonic phonon frequencies and mode‑resolved Grüneisen constants for the four systems: pristine silicene (Si), hydrogenated silicene (HSi), pristine germanene (Ge), and hydrogenated germanene (HGe). Then apply the self‑consistent quasiharmonic approximation (SC‑QHA), which iteratively updates the phonon frequencies with temperature and solves for the temperature‑dependent lattice constant. From the converged solution compute the thermal expansion coefficient α(T), isovolume heat capacity C_V(T), the two‑dimensional bulk modulus B₂D(T), and its quasistatic part B₂D*(T) over the temperature range 0–600 K. Finally derive temperature slopes of the moduli at 300 K and an anharmonicity measure that quantifies the variation of the quasistatic modulus with lattice constant.

## Reproduction target

Produce, for each of the four systems (Si, HSi, Ge, HGe):
- Temperature‑dependent curves of α, C_V, B₂D, and B₂D* from 0 to 600 K, tabulated in a CSV file.
- Aggregated key quantities: B₂D at 0 K and at 300 K, the temperature slope dB₂D/dT at 300 K, and the anharmonicity measure a·dB₂D*/da (a is the lattice constant), reported in a JSON file.

The required numerical outputs are defined solely by the systems and the temperature conditions stated above; no specific paper artifact is cited.

## Assets

- **Quantum ESPRESSO** – open‑source DFT code.  
  Access: https://www.quantum-espresso.org/
- **PBE ultrasoft pseudopotentials for Si, Ge, H** – recommended source: SSSP efficiency library v1.3 or later.  
  Access: https://www.materialscloud.org/discover/sssp/table
- **Python scientific stack** – standard packages for numerical post‑processing (numpy, scipy, matplotlib).  
  Obtainable via PyPI.

## Workflow steps

### Step 1: DFT and phonon calculations  
- Role: process  
- Action: For each material (Si, HSi, Ge, HGe), perform DFT geometry optimization to obtain the equilibrium structure. Then compute the electronic total energy E^e as a function of in‑plane lattice constant a over a range centred on equilibrium. Subsequently, compute harmonic phonon frequencies at several a values using density‑functional perturbation theory, derive the mode‑resolved Grüneisen constants from the frequency shifts, and store all intermediate data for later use.  
- Evidence: `/app/outputs/dft_and_phonon_data.json`

### Step 2: Quasiharmonic thermodynamic simulation  
- Role: process  
- Action: Using the E^e(a) curve and Grüneisen data from Step 1, implement the self‑consistent quasiharmonic approximation (SC‑QHA) for each system. Solve iteratively for the temperature‑dependent lattice constant a(T), update phonon frequencies, and compute the thermodynamic quantities α(T), C_V(T), B₂D(T), and B₂D*(T) on a fine grid from 0 to 600 K. Also evaluate the temperature slope dB₂D/dT at 300 K and the anharmonicity measure a·dB₂D*/da from the electronic energy curvature. Store the full set of computed curves and derived numbers.  
- Evidence: `/app/outputs/raw_thermo_data.json`

### Step 3: Temperature‑dependent thermodynamic curves  
- Role: scored  
- Action: From the results of Step 2 compile the temperature‑dependent data for all four systems into a single CSV file with the columns specified below.  
- Output file: `/app/outputs/thermodynamic_curves.csv`  
- Format: csv  
- Contract:  
  Columns: `system` (values: Si, HSi, Ge, HGe), `temperature_K` (numeric, from 0 to 600 K, e.g. in steps of 10 K), `alpha_1e6K` (numeric, thermal expansion coefficient in units of 10⁻⁶ K⁻¹), `CV_kB_per_unitcell` (numeric, isovolume heat capacity in units of k_B per unit cell), `B2D_eV_Ang2` (numeric, two‑dimensional bulk modulus in eV/Å²), `B2Dstar_eV_Ang2` (numeric, quasistatic bulk modulus in eV/Å²).  
- Scoring: scored by hidden verifier

### Step 4: Key aggregated quantities  
- Role: scored (load-bearing)  
- Action: Extract from the computed data the key numerical results: B₂D at 0 K and at 300 K, dB₂D/dT at 300 K, and a·dB₂D*/da for each of Si, HSi, Ge, HGe. Write them as a JSON file with the structure specified below.  
- Output file: `/app/outputs/key_quantities.json`  
- Format: json  
- Contract:  
  Top‑level keys: `Si`, `HSi`, `Ge`, `HGe`. Each entry is an object with numeric keys: `B2D_0K` (eV/Å²), `B2D_300K` (eV/Å²), `dB2D_dT_300K` (eV/Å²/K), `a_dB2Dstar_da` (eV/Å²).  
- Scoring: scored by hidden verifier; the verifier cannot bypass the computational steps.

## Output files

- `/app/outputs/thermodynamic_curves.csv`
- `/app/outputs/key_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_curves.csv
- path: `/app/outputs/thermodynamic_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent thermodynamic curves. The verifier recomputes temperature slopes of the bulk moduli and verifies trend signs and ordering between systems.
- schema:
  - `type`: table
  - `required_columns`: `system`, `temperature_K`, `alpha_1e6K`, `CV_kB_per_unitcell`, `B2D_eV_Ang2`, `B2Dstar_eV_Ang2`
  - `units`:
    - `temperature_K`: K
    - `alpha_1e6K`: 10^-6 K^-1
    - `CV_kB_per_unitcell`: k_B per unit cell
    - `B2D_eV_Ang2`: eV/Å^2
    - `B2Dstar_eV_Ang2`: eV/Å^2

### key_quantities.json
- path: `/app/outputs/key_quantities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Key aggregated quantities. The verifier compares each value against a hidden reference with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Si`:
      - `B2D_0K`: number, eV/Å^2
      - `B2D_300K`: number, eV/Å^2
      - `dB2D_dT_300K`: number, eV/Å^2/K
      - `a_dB2Dstar_da`: number, eV/Å^2
    - `HSi`:
      - `B2D_0K`: number, eV/Å^2
      - `B2D_300K`: number, eV/Å^2
      - `dB2D_dT_300K`: number, eV/Å^2/K
      - `a_dB2Dstar_da`: number, eV/Å^2
    - `Ge`:
      - `B2D_0K`: number, eV/Å^2
      - `B2D_300K`: number, eV/Å^2
      - `dB2D_dT_300K`: number, eV/Å^2/K
      - `a_dB2Dstar_da`: number, eV/Å^2
    - `HGe`:
      - `B2D_0K`: number, eV/Å^2
      - `B2D_300K`: number, eV/Å^2
      - `dB2D_dT_300K`: number, eV/Å^2/K
      - `a_dB2Dstar_da`: number, eV/Å^2

Notes: The verifier does not re‑run DFT or SC‑QHA; it only analyses the submitted artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "temperature_K",
          "alpha_1e6K",
          "CV_kB_per_unitcell",
          "B2D_eV_Ang2",
          "B2Dstar_eV_Ang2"
        ],
        "units": {
          "temperature_K": "K",
          "alpha_1e6K": "10^-6 K^-1",
          "CV_kB_per_unitcell": "k_B per unit cell",
          "B2D_eV_Ang2": "eV/Å^2",
          "B2Dstar_eV_Ang2": "eV/Å^2"
        }
      },
      "description": "Temperature-dependent thermodynamic curves. The verifier recomputes temperature slopes of the bulk moduli and verifies trend signs and ordering between systems."
    },
    {
      "file": "key_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Si": {
            "B2D_0K": "number, eV/Å^2",
            "B2D_300K": "number, eV/Å^2",
            "dB2D_dT_300K": "number, eV/Å^2/K",
            "a_dB2Dstar_da": "number, eV/Å^2"
          },
          "HSi": {
            "B2D_0K": "number, eV/Å^2",
            "B2D_300K": "number, eV/Å^2",
            "dB2D_dT_300K": "number, eV/Å^2/K",
            "a_dB2Dstar_da": "number, eV/Å^2"
          },
          "Ge": {
            "B2D_0K": "number, eV/Å^2",
            "B2D_300K": "number, eV/Å^2",
            "dB2D_dT_300K": "number, eV/Å^2/K",
            "a_dB2Dstar_da": "number, eV/Å^2"
          },
          "HGe": {
            "B2D_0K": "number, eV/Å^2",
            "B2D_300K": "number, eV/Å^2",
            "dB2D_dT_300K": "number, eV/Å^2/K",
            "a_dB2Dstar_da": "number, eV/Å^2"
          }
        }
      },
      "description": "Key aggregated quantities. The verifier compares each value against a hidden reference with appropriate tolerances."
    }
  ],
  "notes": "The verifier does not re‑run DFT or SC‑QHA; it only analyses the submitted artifacts."
}
```

## How you are scored

The hidden verifier independently processes your submitted artifacts. For the thermodynamic curves (CSV) it recomputes derived quantities such as the temperature slopes of the bulk moduli and verifies trend signs and ordering between systems. For the key quantities (JSON) it compares each value against a hidden reference using appropriate tolerances. Each scored stage carries a pre‑defined weight; the combined score yields the final reward. Reporting paper numbers without generating the required artifacts does not satisfy the scoring contract.
