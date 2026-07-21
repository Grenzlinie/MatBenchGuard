# DFT relaxation and Mahan–Sofo ZT for rare-earth telluride Ce3Te4

## Problem background
Thermoelectric materials directly convert heat to electricity and are promising for waste-heat recovery. Rare‑earth chalcogenides such as Ce₃Te₄ are of interest for high‑temperature applications because of their thermal stability and the potential contribution of highly localized f‑electrons to the Seebeck coefficient. This task uses first‑principles density‑functional theory (DFT) to compute the equilibrium structure and electronic density of states of Ce₃Te₄, and then applies the Mahan–Sofo analytic transport model to estimate an upper limit for its thermoelectric figure of merit (zT) at 1200 K.

## Approach
You will perform a DFT calculation using a plane‑wave basis and the projector‑augmented‑wave (PAW) method with the generalized‑gradient approximation (GGA). Set up the primitive cell of Ce₃Te₄ in the cubic Th₃P₄ structure (6 Ce + 8 Te atoms) with lattice vectors a₁=a₀(-½,½,½), a₂=a₀(½,-½,½), a₃=a₀(½,½,-½). Carry out a full structural relaxation (forces < 0.02 eV/Å) with a 23 Ry plane‑wave cutoff and an 8×8×8 Monkhorst–Pack k‑point mesh to obtain the equilibrium lattice constant a₀. Using the relaxed structure, compute the total electronic density of states (TDOS). Identify the highest sharp peak in the conduction band (above the Fermi level) and record its energy relative to the Fermi level. Finally, apply the Mahan–Sofo model: define the dimensionless peak position b = E_peak / (k_B T) with k_B = 8.617333262145×10⁻⁵ eV/K and T = 1200 K, and the function D(b) = e^b/(e^b+1)². The ideal zT is given by zT = 14.0 × [D(b) b²] / [D(2.4)×(2.4)²], where the prefactor 14.0 corresponds to the maximum possible zT under the idealised parameters of the model (lattice thermal conductivity k_l = 1 W/m·K, mean free path l = 0.3 nm).

## Reproduction target
Compute the equilibrium lattice constant a₀ of Ce₃Te₄ (in Å), the energy (in eV) of the dominant sharp DOS peak in the conduction band, and the ideal dimensionless figure of merit zT at 1200 K. Report each as a single numeric value in a plain text file, following the file‑naming and format rules in the Workflow steps.

## Assets

- DFT code (Quantum ESPRESSO or equivalent): https://www.quantum-espresso.org/
- PAW pseudopotentials for Ce and Te (GGA): https://github.com/dalcorso/pslibrary
- Python 3: python3

## Workflow steps

### Step 1: DFT structural relaxation
- Role: scored
- Action: Set up the primitive cell of Ce3Te4 (cubic Th3P4 structure, 6 Ce + 8 Te atoms, lattice vectors as specified in the paper) and perform DFT structural relaxation using GGA, PAW pseudopotentials, a plane-wave cutoff of 23 Ry, and an 8×8×8 Monkhorst–Pack k‑point mesh. Relax atomic positions until forces are below 0.02 eV/Å with conjugate‑gradient optimisation. Extract the final equilibrium lattice constant a0 in Å.
- Output file: `/app/outputs/step_01_lattice_constant.txt`
- Format: txt
- Contract: A single float in ångströms.
- Scoring: scored by hidden verifier

### Step 2: Electronic DOS and peak energy
- Role: scored (load-bearing)
- Action: Using the relaxed structure from step 1 and the same DFT parameters (GGA, PAW, 23 Ry, 8×8×8 k‑mesh), perform a self‑consistent field calculation to obtain the total electronic density of states (TDOS). Identify the highest sharp peak in the conduction band above the Fermi level and record its energy (in eV) relative to the Fermi level.
- Output file: `/app/outputs/step_02_dos_peak_energy.txt`
- Format: txt
- Contract: A single float in electronvolts.
- Scoring: scored by hidden verifier

### Step 3: Ideal ZT from Mahan‑Sofo model
- Role: scored (load-bearing)
- Action: Using the peak energy E_peak from step 2, apply the Mahan‑Sofo analytic transport model at 1200 K as described in the provided paper text (see Eqs. 1–3). The model defines a dimensionless position b = E_peak / (k_B T) with k_B = 8.617333262145×10⁻⁵ eV/K, a function D(b) = e^b / (e^b + 1)^2, and the dimensionless figure of merit ZT = k_0 / k_l. The computation must incorporate the idealised parameters: lattice thermal conductivity k_l = 1 W/m·K and mean‑free‑path l = 0.3 nm. Report the resulting ideal ZT as a single number.
- Output file: `/app/outputs/step_03_ideal_ZT.txt`
- Format: txt
- Contract: A single float (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_constant.txt`
- `/app/outputs/step_02_dos_peak_energy.txt`
- `/app/outputs/step_03_ideal_ZT.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_constant.txt
- path: `/app/outputs/step_01_lattice_constant.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant a0 of Ce3Te4 from DFT structural relaxation. The file contains a single numeric value in ångströms.
- schema:
  - `type`: text
  - `units`:
    - `value`: Å

### step_02_dos_peak_energy.txt
- path: `/app/outputs/step_02_dos_peak_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Energy of the sharp DOS peak in the conduction band relative to the Fermi level, in eV. The file contains a single numeric value.
- schema:
  - `type`: text
  - `units`:
    - `value`: eV

### step_03_ideal_ZT.txt
- path: `/app/outputs/step_03_ideal_ZT.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Ideal dimensionless figure of merit ZT at 1200 K computed from the Mahan‑Sofo model using the peak energy from step 2. The file contains a single numeric value.
- schema:
  - `type`: text
  - `units`:
    - `value`: dimensionless

Notes: The ZT value will be verified for self‑consistency by recomputing it from the submitted DOS peak energy. The lattice constant and DOS peak energy are compared to reference values. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "Å"
        }
      },
      "description": "Equilibrium lattice constant a0 of Ce3Te4 from DFT structural relaxation. The file contains a single numeric value in ångströms."
    },
    {
      "file": "step_02_dos_peak_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "eV"
        }
      },
      "description": "Energy of the sharp DOS peak in the conduction band relative to the Fermi level, in eV. The file contains a single numeric value."
    },
    {
      "file": "step_03_ideal_ZT.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "units": {
          "value": "dimensionless"
        }
      },
      "description": "Ideal dimensionless figure of merit ZT at 1200 K computed from the Mahan‑Sofo model using the peak energy from step 2. The file contains a single numeric value."
    }
  ],
  "notes": "The ZT value will be verified for self‑consistency by recomputing it from the submitted DOS peak energy. The lattice constant and DOS peak energy are compared to reference values. No gold values are disclosed here."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier scores each of the three output files independently:

- lattice constant (step_01_lattice_constant.txt): compared to a reference value with appropriate tolerances.
- DOS peak energy (step_02_dos_peak_energy.txt): compared to a reference value with appropriate tolerances.
- Ideal zT (step_03_ideal_ZT.txt): the verifier recomputes zT from your submitted peak energy and checks self‑consistency, and also compares your zT to a reference value.

The three scores are weighted as 30%, 30%, and 40% and summed to produce a final reward between 0 and 1. You must execute all the steps and produce the files as described; simply writing a known value without performing the calculation will not pass the self‑consistency check and will yield a low reward.
