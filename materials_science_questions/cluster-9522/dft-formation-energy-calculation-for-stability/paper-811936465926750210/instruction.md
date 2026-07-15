# First-Principles Formation Energies and CALPHAD Thermodynamic Modeling for As-Fe Compounds

## Problem background
In the fabrication of Fe/semiconductor hybrid structures for spintronic devices, knowledge of the thermodynamics of the binary As–Fe system is essential for understanding and controlling interface reactions. This system contains three stable compounds at room temperature—As₂Fe, AsFe, and AsFe₂—as well as the high‑temperature phase As₂Fe₃. Reliable values for the formation energies of these compounds are critical inputs for thermodynamic modeling, but existing experimental estimates carry large uncertainties, and previous Calphad assessments show significant discrepancies. The present task combines first‑principles density‑functional‑theory (DFT) calculations with a Calphad thermodynamic model to provide accurate formation energies and a consistent phase diagram for the As–Fe system. Your goal is to compute the formation energies of the three compounds from DFT total‑energy calculations, and to use the resulting data—together with given Calphad model parameters and SGTE unary Gibbs‑energy functions—to calculate the liquidus temperatures at key compositions and the arsenic activity in the liquid phase under specified conditions. The computed quantities will be compared to reference results from the original study to assess the accuracy of the reproduction.

## Approach
The reproduction proceeds in two main parts.

**DFT formation energies.**
Using the ABINIT density‑functional‑theory code with the projector‑augmented‑wave (PAW) method and the generalized‑gradient approximation (GGA), you will perform full structural relaxations and total‑energy calculations for the pure elements (non‑magnetic α‑As and ferromagnetic α‑Fe) and for the three compounds: As₂Fe (non‑magnetic), AsFe (antiferromagnetic with alternating spin arrangement along the crystallographic c‑axis), and AsFe₂ (antiferromagnetic with a doubled unit cell). From the converged total energies you will then compute the 0 K formation energy (in kJ per mole of atoms) of each compound relative to the pure elemental reference states.

**Calphad thermodynamic model.**
You will implement the Calphad Gibbs‑energy descriptions for the liquid, bcc, and fcc solution phases (substitutional regular‑solution model) and for the stoichiometric compounds As₂Fe, AsFe, and AsFe₂, using the parameters provided in the task specification. The AsFe compound is treated with an absolute‑reference‑state expression that reproduces measured heat‑capacity data; As₂Fe and AsFe₂ use a floating‑reference‑state form. The As₂Fe₃ phase is described by a two‑sublattice compound‑energy formalism. With the SGTE unary Gibbs‑energy functions for pure As and Fe, you will construct the equilibrium phase diagram by convex‑hull or equivalent technique and extract the liquidus temperatures at the three stoichiometric compositions (33.3, 50, and 66.7 at% As). You will also compute the thermodynamic activity of arsenic in the liquid at 1423 K and a mole fraction of As equal to 0.5.

The quantitative comparisons to be made are: the DFT formation energies (versus reference values obtained in the original study), the liquidus temperatures at the stoichiometric compositions, and the liquid‑phase arsenic activity under the stated conditions. These comparisons form the scored outputs of the task.

## Reproduction target
This task requires you to produce the following concrete results:

- **DFT formation energies:** Compute the 0 K formation energies (kJ/mol‑atom) of As₂Fe, AsFe, and AsFe₂, referenced to non‑magnetic α‑As and ferromagnetic α‑Fe, using ABINIT with PAW‑GGA. For each compound use the most stable magnetic state as identified by the DFT relaxations (expected to be non‑magnetic for As₂Fe, antiferromagnetic for AsFe, and antiferromagnetic for AsFe₂). Report the total energies, formation energies, and relaxed lattice constants in the specified CSV file.

- **Calphad liquidus and activity:** Implement the Calphad thermodynamic model with the given parameters and the SGTE unary functions. From the calculated phase diagram, extract the liquidus temperatures (K) at the As atomic fractions corresponding to the stoichiometries of As₂Fe (33.3 at% As), AsFe (50 at% As), and AsFe₂ (66.7 at% As). Also compute the arsenic activity in the liquid at 1423 K and x(As) = 0.5. Store these four quantities in the designated CSV.

The target is for these computed quantities to agree with the reference values obtained in the original study within the expected numerical uncertainties of DFT and Calphad methods. The precise reference numbers are not disclosed; your results will be scored by comparison against them.

## Assets

- ABINIT DFT code: https://www.abinit.org/
- PAW pseudopotentials for As and Fe: http://pseudopotentials.abinit.org/
- Crystal structure data for As-Fe compounds
- SGTE unary Gibbs energy functions: https://github.com/OpenCalphad/OpenCalphad/blob/master/OC_UN/databases/unary.tdb

## Workflow steps

### Step 1: DFT total energy calculations and structural relaxations
- Role: process
- Action: Run ABINIT with PAW-GGA (scalar-relativistic, spin-polarized) to relax geometries and compute total energies for αAs (nm), αFe (ferromagnetic), As₂Fe (nm), AsFe (antiferromagnetic with alternating spins along c), and AsFe₂ (antiferromagnetic with doubled unit cell). Use a plane-wave cutoff of 40 Ry, Fermi-Dirac smearing of 0.4 mRy, and Monkhorst-Pack k-point meshes as specified (8×8×8 for αAs, 12×12×12 for αFe, 6×6×12 for As₂Fe, 6×12×6 for AsFe, 10×10×6 for ferromagnetic AsFe₂, 10×10×4 for antiferromagnetic AsFe₂). Perform full geometry optimization (atomic positions and unit cell). Save total energy per formula unit and relaxed lattice parameters to evidence file.
- Evidence: `/app/outputs/dft_total_energies.txt`

### Step 2: Compute DFT formation energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in step_01, compute the 0 K formation energies (kJ/mol-atom) of As₂Fe, AsFe, AsFe₂ referenced to nm αAs and ferromagnetic αFe. Use the most stable magnetic state for each compound: nm As₂Fe, antiferromagnetic AsFe, antiferromagnetic AsFe₂. Output a CSV with columns compound, magnetic_state, total_energy_Ha, formation_energy_kJ_per_mol, a_Ang, b_Ang, c_Ang, volume_Ang3.
- Output file: `/app/outputs/step_02_formation_energies.csv`
- Format: csv
- Contract: Columns: compound (string), magnetic_state (string), total_energy_Ha (float), formation_energy_kJ_per_mol (float), a_Ang (float), b_Ang (float), c_Ang (float), volume_Ang3 (float).
- Scoring: scored by hidden verifier

### Step 3: CALPHAD phase diagram and thermodynamic properties
- Role: scored (load-bearing)
- Action: Implement the CALPHAD thermodynamic models with SGTE unary Gibbs energy functions and the following explicit parameters from the original study. Liquid phase (substitutional solution, Redlich‑Kister per mole of atoms): L0 = -83810.9 - 3.0716 T, L1 = 50261.1 - 4.6947 T, L2 = 75085.7 - 45.1907 T, L3 = -46496.7 (units J/mol-atom for all L). bcc phase: L0 = -122879.9 + 67.9395 T, L1 = -3248.55 + 45.8837 T, L2 = 23365.2. fcc phase: L0 = -80000 + 13.5 T. Stoichiometric As₂Fe (floating reference, per mole As₂Fe formula units): G = -37236.8 + 10.9657 T + (2/3) G_As^rhombo + (1/3) G_Fe^bcc. Stoichiometric AsFe (absolute reference, per mole AsFe formula units; the expression below is the full molar Gibbs energy already incorporating the SGTE reference-state values for pure As and Fe at 298.15 K): G = -37991.2 + 122.3339 T - 22.1461 T ln T - 4.6066e-3 T^2 - 7.205e-7 T^3. Stoichiometric AsFe₂ (floating reference, per mole AsFe₂ formula units): G = -28919.1 + 3.9343 T + (1/3) G_As^rhombo + (2/3) G_Fe^bcc. As₂Fe₃ phase described by compound energy formalism (Fe)(As,Va)_{0.75}; end‑member Gibbs energies per mole of formula units: G_Fe:As = -10812.6 - 5.5208 T + 0.75 G_As^rhombo + G_Fe^bcc; G_Fe:Va = 5000 - 0.3383 T + G_Fe^bcc. In all formulas, G_As^rhombo and G_Fe^bcc are the SGTE unary Gibbs energy functions for rhombohedral As and bcc Fe, respectively, expressed per mole of atoms. Compute the equilibrium phase diagram (convex hull or equivalent method). Extract liquidus temperatures (K) at As atomic fractions: 33.3 at% As (As₂Fe), 50 at% As (AsFe), 66.7 at% As (AsFe₂). Also compute As activity in liquid at 1423 K, x_As = 0.5. Output a CSV with columns property, value, unit.
- Output file: `/app/outputs/step_03_calphad.csv`
- Format: csv
- Contract: Columns: property (string), value (float), unit (string). Example rows: 'liquidus_T_33at_As', 'liquidus_T_50at_As', 'liquidus_T_67at_As', 'a_As_1423K_50at'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_formation_energies.csv`
- `/app/outputs/step_03_calphad.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_formation_energies.csv
- path: `/app/outputs/step_02_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT computed formation energies (kJ/mol-atom) and relaxed lattice parameters for As₂Fe, AsFe, AsFe₂ and reference elements.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `magnetic_state`, `total_energy_Ha`, `formation_energy_kJ_per_mol`, `a_Ang`, `b_Ang`, `c_Ang`, `volume_Ang3`
  - `units`:
    - `total_energy_Ha`: Ha
    - `formation_energy_kJ_per_mol`: kJ/mol-atom
    - `a_Ang`: Å
    - `b_Ang`: Å
    - `c_Ang`: Å
    - `volume_Ang3`: Å³

### step_03_calphad.csv
- path: `/app/outputs/step_03_calphad.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CALPHAD computed liquidus temperatures (K) and As activity (dimensionless) using the paper's thermodynamic parameters.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`, `unit`
  - `units`:
    - `value`: varies; unit specified in unit column

Notes: The DFT step uses ABINIT with specific pseudopotentials and parameters; the CALPHAD step uses the paper's Table 3 parameters exactly. The checker compares the agent's reported values against hidden paper reference values with tolerances appropriate for DFT and CALPHAD uncertainties.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "magnetic_state",
          "total_energy_Ha",
          "formation_energy_kJ_per_mol",
          "a_Ang",
          "b_Ang",
          "c_Ang",
          "volume_Ang3"
        ],
        "units": {
          "total_energy_Ha": "Ha",
          "formation_energy_kJ_per_mol": "kJ/mol-atom",
          "a_Ang": "Å",
          "b_Ang": "Å",
          "c_Ang": "Å",
          "volume_Ang3": "Å³"
        }
      },
      "description": "DFT computed formation energies (kJ/mol-atom) and relaxed lattice parameters for As₂Fe, AsFe, AsFe₂ and reference elements."
    },
    {
      "file": "step_03_calphad.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value",
          "unit"
        ],
        "units": {
          "value": "varies; unit specified in unit column"
        }
      },
      "description": "CALPHAD computed liquidus temperatures (K) and As activity (dimensionless) using the paper's thermodynamic parameters."
    }
  ],
  "notes": "The DFT step uses ABINIT with specific pseudopotentials and parameters; the CALPHAD step uses the paper's Table 3 parameters exactly. The checker compares the agent's reported values against hidden paper reference values with tolerances appropriate for DFT and CALPHAD uncertainties."
}
```

## How you are scored
A hidden verifier evaluates your two scored output files: `step_02_formation_energies.csv` (DFT formation energies) and `step_03_calphad.csv` (Calphad liquidus temperatures and activity).

For each step, the verifier reads the quantities you report and compares them to reference values derived from the original paper’s published results. The comparison uses tolerances appropriate for the computational methods (DFT with a specific code/functional and Calphad with the given model parameters). The score for a quantity increases as your computed value approaches the reference, and it reaches full credit when your value meets or exceeds the reference in the direction of better agreement (e.g., a lower formation energy error or a more accurate liquidus temperature). Larger deviations lead to a lower score.

The final reward is a weighted combination of the scores from the individual steps, with the main emphasis on the formation energies and the Calphad predictions. Reporting numbers alone is not sufficient—your artifacts must be in the exact format specified under “Output contract” so the verifier can parse them. The verifier does not have access to the internet or to the original paper; it only knows the expected reference values and the allowed tolerances for each quantity.
