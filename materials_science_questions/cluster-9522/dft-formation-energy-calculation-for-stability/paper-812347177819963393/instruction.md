# DFT Formation Energy and Stability of Fe-K Substitutional Alloy under High Pressure

## Problem background
Potassium’s possible presence in the Earth’s core has long been debated because it would provide a significant internal heat source via the decay of ⁴⁰K, powering the geodynamo. High-pressure experiments showed that potassium can enter iron at core conditions, but the mechanism and the thermodynamic stability of the resulting alloy remained unresolved. This problem asks: under what pressures does substitutional potassium become energetically stable in hexagonal close-packed (hcp) ε-iron, and how large is the associated volume change? Answering this requires computing the Gibbs free energy difference and volume expansion from first principles.

## Approach
The computational strategy uses density functional theory (DFT) with the projector augmented wave (PAW) method and the generalized gradient approximation (GGA) for exchange-correlation. The workflow consists of:
1. Compute total energies for pure ε-iron (hcp) and pure potassium in the face-centered cubic (fcc) K II phase over a range of volumes.
2. Construct a 96-atom orthorhombic supercell of the hcp structure (c/a = 1.6), substitute one iron atom with potassium to yield composition Fe₀.₉₉K₀.₀₁, and relax atomic positions while computing total energies at several volumes.
3. Fit a third-order Birch–Murnaghan equation of state to the energy‑volume data for each system to obtain equilibrium volume V₀, bulk modulus K₀, and its pressure derivative K₀′.
4. From the fitted equations of state, compute the static (0 K) Gibbs free energy per atom for the alloying reaction Fe + (x−1)Fe + (1−x)K → FeₓK₍₁₋ₓ₎, with x=0.99. The Gibbs free energy difference ΔG(P) = G_alloy/atom − [x·G_Fe + (1−x)·G_K]/atom. Also calculate the percent volume difference 100×(V_alloy − V_Fe)/V_Fe as a function of pressure.
5. Add an approximate entropy contribution using the ideal mixing entropy at 2000 K, ΔS_mix = –k_B [x ln x + (1−x) ln (1−x)], to obtain a finite‑temperature ΔG curve.

## Reproduction target
Produce the following four files:
1. `eos_parameters.json` — fitted Birch–Murnaghan parameters for pure Fe, pure K (fcc K II), and Fe₀.₉₉K₀.₀₁ alloy.
2. `volume_difference_vs_pressure.csv` — percent volume expansion of the alloy relative to pure ε‑Fe for pressures from 0 to at least 50 GPa.
3. `dG_vs_pressure_static.csv` — static (0 K) Gibbs free energy difference per atom for the alloying reaction over the same pressure range, from which the pressure where ΔG = 0 can be interpolated.
4. `dG_vs_pressure_entropy.csv` — entropy‑corrected ΔG at 2000 K, with the corresponding zero‑crossing pressure.

All computations must be based on the described DFT supercell and equation‑of‑state fitting; no pre‑computed data may be substituted.

## Assets

- Quantum ESPRESSO or equivalent plane‑wave DFT code: https://www.quantum-espresso.org/
- PAW pseudopotentials for Fe and K (GGA‑PBE): http://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT reference calculations
- Role: process
- Action: Perform DFT total energy calculations for pure hcp ε‑Fe and pure fcc K (K II) over a range of volumes, using a plane‑wave DFT code with PAW pseudopotentials and GGA functional. Cover a sufficient volume range to later fit equations of state.
- Evidence: `/app/outputs/reference_ev_data.csv`

### Step 2: DFT alloy supercell calculations
- Role: process
- Action: Construct an orthorhombic supercell of the hcp structure (c/a=1.6, cell vectors lengths √3, 1, 1.6) with 96 atoms (2×4×3 replicas). Substitute one K atom for an Fe site to create Fe₀.₉₉K₀.₀₁. Perform ionic relaxation and compute total energies at a series of volumes.
- Evidence: `/app/outputs/alloy_ev_data.csv`

### Step 3: Equation of state fitting
- Role: scored
- Action: Fit a third‑order Birch‑Murnaghan equation of state to the energy‑volume data for pure Fe, pure fcc K, and the Fe₀.₉₉K₀.₀₁ alloy. Extract the parameters V₀ (Å³), K₀ (GPa), and K₀′ (dimensionless). Save as eos_parameters.json.
- Output file: `/app/outputs/eos_parameters.json`
- Format: json
- Contract: JSON object with keys pure_Fe, pure_K_fcc, Fe_K_alloy. Each object contains V0 (Angstrom^3), K0 (GPa), K0_prime (dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Volume expansion analysis
- Role: scored
- Action: Using the fitted EOS of pure Fe and the alloy, compute the percent volume difference 100*(V_alloy - V_Fe)/V_Fe as a function of pressure from 0 to at least 50 GPa. Output volume_difference_vs_pressure.csv.
- Output file: `/app/outputs/volume_difference_vs_pressure.csv`
- Format: csv
- Contract: CSV with columns pressure_GPa, volume_difference_percent.
- Scoring: scored by hidden verifier

### Step 5: Static Gibbs free energy difference
- Role: scored (load-bearing)
- Action: For the reaction xFe + (1-x)K → FeₓK₍₁₋ₓ₎ (x=0.99), compute the static (0 K) Gibbs free energy difference per atom ΔG(P) = G_alloy/atom – (x·G_Fe + (1-x)·G_K)/atom using the fitted EOS. Evaluate G = E + PV from the EOS curves. Output dG_vs_pressure_static.csv covering the pressure range where ΔG crosses zero (0 to at least 50 GPa).
- Output file: `/app/outputs/dG_vs_pressure_static.csv`
- Format: csv
- Contract: CSV with columns pressure_GPa, Delta_G_eV_per_atom.
- Scoring: scored by hidden verifier

### Step 6: Entropy‑corrected Gibbs free energy difference
- Role: scored
- Action: Apply an ideal mixing entropy contribution ΔS_mix = –k_B [x ln x + (1-x) ln (1-x)] at T=2000 K to the static ΔG. Compute ΔG_entropy(P) = ΔG_static(P) – T·ΔS_mix (per atom). Output dG_vs_pressure_entropy.csv.
- Output file: `/app/outputs/dG_vs_pressure_entropy.csv`
- Format: csv
- Contract: CSV with columns pressure_GPa, Delta_G_eV_per_atom.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_parameters.json`
- `/app/outputs/volume_difference_vs_pressure.csv`
- `/app/outputs/dG_vs_pressure_static.csv`
- `/app/outputs/dG_vs_pressure_entropy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_parameters.json
- path: `/app/outputs/eos_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted third‑order Birch‑Murnaghan equation of state parameters for pure Fe, pure K (fcc), and the Fe0.99K0.01 substitutional alloy.
- schema:
  - `type`: object
  - `required`: `pure_Fe`, `pure_K_fcc`, `Fe_K_alloy`
  - `properties`:
    - `pure_Fe`:
      - `V0`: number (Angstrom^3)
      - `K0`: number (GPa)
      - `K0_prime`: number
    - `pure_K_fcc`:
      - `V0`: number (Angstrom^3)
      - `K0`: number (GPa)
      - `K0_prime`: number
    - `Fe_K_alloy`:
      - `V0`: number (Angstrom^3)
      - `K0`: number (GPa)
      - `K0_prime`: number
  - `units`:
    - `V0`: Angstrom^3
    - `K0`: GPa
    - `K0_prime`: dimensionless

### volume_difference_vs_pressure.csv
- path: `/app/outputs/volume_difference_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Percent volume expansion of the alloy relative to pure ε‑Fe as a function of pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `volume_difference_percent`
  - `units`:
    - `pressure_GPa`: GPa
    - `volume_difference_percent`: %

### dG_vs_pressure_static.csv
- path: `/app/outputs/dG_vs_pressure_static.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static (0 K) Gibbs free energy difference per atom for the alloying reaction.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `Delta_G_eV_per_atom`
  - `units`:
    - `pressure_GPa`: GPa
    - `Delta_G_eV_per_atom`: eV per atom

### dG_vs_pressure_entropy.csv
- path: `/app/outputs/dG_vs_pressure_entropy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Entropy‑corrected Gibbs free energy difference per atom at T=2000 K.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `Delta_G_eV_per_atom`
  - `units`:
    - `pressure_GPa`: GPa
    - `Delta_G_eV_per_atom`: eV per atom

Notes: The pure‑K reference phase is K II (fcc). The entropy correction uses ideal mixing entropy at 2000 K. The volume expansion and Gibbs curves must cover at least 0–50 GPa.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "pure_Fe",
          "pure_K_fcc",
          "Fe_K_alloy"
        ],
        "properties": {
          "pure_Fe": {
            "V0": "number (Angstrom^3)",
            "K0": "number (GPa)",
            "K0_prime": "number"
          },
          "pure_K_fcc": {
            "V0": "number (Angstrom^3)",
            "K0": "number (GPa)",
            "K0_prime": "number"
          },
          "Fe_K_alloy": {
            "V0": "number (Angstrom^3)",
            "K0": "number (GPa)",
            "K0_prime": "number"
          }
        },
        "units": {
          "V0": "Angstrom^3",
          "K0": "GPa",
          "K0_prime": "dimensionless"
        }
      },
      "description": "Fitted third‑order Birch‑Murnaghan equation of state parameters for pure Fe, pure K (fcc), and the Fe0.99K0.01 substitutional alloy."
    },
    {
      "file": "volume_difference_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "volume_difference_percent"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "volume_difference_percent": "%"
        }
      },
      "description": "Percent volume expansion of the alloy relative to pure ε‑Fe as a function of pressure."
    },
    {
      "file": "dG_vs_pressure_static.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "Delta_G_eV_per_atom"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "Delta_G_eV_per_atom": "eV per atom"
        }
      },
      "description": "Static (0 K) Gibbs free energy difference per atom for the alloying reaction."
    },
    {
      "file": "dG_vs_pressure_entropy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "Delta_G_eV_per_atom"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "Delta_G_eV_per_atom": "eV per atom"
        }
      },
      "description": "Entropy‑corrected Gibbs free energy difference per atom at T=2000 K."
    }
  ],
  "notes": "The pure‑K reference phase is K II (fcc). The entropy correction uses ideal mixing entropy at 2000 K. The volume expansion and Gibbs curves must cover at least 0–50 GPa."
}
```

## How you are scored
Each of the four scored artifacts is checked by a hidden verifier that compares your results to independent reference values. The verifier:
- Reads `eos_parameters.json` and compares V₀, K₀, K₀′ for the Fe₀.₉₉K₀.₀₁ alloy within appropriate tolerances.
- Reads `volume_difference_vs_pressure.csv`, verifies that the zero‑pressure volume difference is within an expected range and that the curve is positive and decreases with pressure.
- Reads `dG_vs_pressure_static.csv`, interpolates the pressure at which ΔG becomes zero, and checks that it falls inside a specific interval and that the curve is monotonic.
- Reads `dG_vs_pressure_entropy.csv`, repeats the zero‑crossing interpolation, and checks its allowed range.
The reward is a weighted combination of these checks: the static stability pressure has the highest weight, followed by the entropy‑corrected pressure, the equation‑of‑state parameters, and the volume expansion curve. No numerical targets are revealed here — the task is to compute the required quantities honestly using the protocol described. Reporting the paper’s numbers without performing the underlying DFT and fitting will not satisfy the verifier.
