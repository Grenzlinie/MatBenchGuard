# Quasi-harmonic Debye thermodynamic properties of ReN

## Problem background
Rhenium mononitride (ReN) is a hard 5d transition metal nitride with potential industrial applications. The ground-state crystal structure and the pressure-induced phase transition remain highly debated. Candidate structures include cubic types such as NbO-type and hexagonal types such as NiAs-type. Determining which phase is most stable and how it transforms under pressure is important for understanding the mechanical and thermal behavior of this material. The elastic constants, Vickers hardness, Debye temperature, thermal expansion, and heat capacity are key quantities for evaluating its performance under extreme conditions.

## Approach
This reproduction employs first-principles density functional theory (DFT) with the projector augmented wave (PAW) method and the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional. Total energies of NbO-type and NiAs-type ReN are computed as functions of unit-cell volume. The energy-volume data are fitted to the third-order Birch-Murnaghan equation of state to extract equilibrium properties and to construct enthalpy-pressure curves; the crossing of these enthalpy curves identifies the phase transition pressure. Elastic constants are obtained by applying non-volume-conserving strains (cubic distortions for NbO-type, hexagonal distortions for NiAs-type) and fitting the resulting energy-strain data to fourth-order polynomials. The second-order elastic constants are then combined via the Voigt-Reuss-Hill averaging scheme to derive bulk modulus, shear modulus, Young's modulus, and Poisson's ratio. Vickers hardness is estimated from the elastic moduli using Tian's formula. Finally, the quasi-harmonic Debye model is applied to the NbO-type phase to compute the Debye temperature, isochoric heat capacity Cv, and thermal expansion coefficient α as functions of temperature at selected pressures (0 and 50 GPa). Open-source DFT codes (e.g., Quantum ESPRESSO) can be used as a substitute for the proprietary code of the original study.

## Reproduction target
The task is to determine which phase (NbO-type or NiAs-type) is thermodynamically more stable at zero pressure and to find the pressure at which the NiAs phase becomes more stable. Compute and report the elastic constants C11, C12, C44 for NbO-type and C11, C33, C44, C12, C13 for NiAs-type at zero pressure. From these, derive the bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and Vickers hardness for both phases. Using the quasi-harmonic Debye model for the NbO-type structure, obtain the Debye temperature at zero pressure, and generate the temperature-dependent curves of isochoric heat capacity Cv and thermal expansion coefficient α at pressures of 0 GPa and 50 GPa.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code capable of PAW-PBE): https://www.quantum-espresso.org/
- PAW-PBE pseudopotentials for Re and N: https://www.materialscloud.org/discover/sssp/
- GIBBS2 code (quasi-harmonic Debye model) or self-implemented equivalent: https://github.com/gibbscode/gibbs2
- Python libraries (numpy, scipy, etc.): pypi

## Workflow steps

### Step 1: DFT total-energy vs volume calculations
- Role: process
- Action: Perform first-principles DFT total-energy calculations for NbO-type and NiAs-type ReN at a series of unit-cell volumes using an open-source PAW-PBE code. Write the volume-energy data to an evidence file.
- Evidence: `/app/outputs/ev_data.csv`

### Step 2: Phase transition pressure via EOS fitting and enthalpy comparison
- Role: scored (load-bearing)
- Action: Fit the E-V data for NbO and NiAs to the third-order Birch-Murnaghan equation of state. Compute enthalpy H = E + PV over a pressure range and determine the crossing pressure where the NiAs phase becomes more stable. Output the transition pressure and enthalpy curves.
- Output file: `/app/outputs/phase_transition.json`
- Format: json
- Contract: JSON object with keys: transition_pressure_GPa (float), NbO_enthalpy (list of objects with P and H), NiAs_enthalpy (list of objects with P and H).
- Scoring: scored by hidden verifier

### Step 3: DFT strain calculations for elastic constants
- Role: process
- Action: Perform DFT total-energy calculations for NbO-type and NiAs-type ReN under the non-volume-conserving strains needed to derive elastic constants (cubic distortions for NbO, hexagonal distortions for NiAs) at the equilibrium volume. Write the energy-strain data to an evidence file.
- Evidence: `/app/outputs/strain_energy.csv`

### Step 4: Elastic properties and Vickers hardness
- Role: scored
- Action: Fit the energy-strain data to fourth-order polynomials and extract the second-order elastic constants Cij for both NbO and NiAs phases. Compute bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and Vickers hardness using the Voigt-Reuss-Hill scheme and Tian's formula. Output all derived properties.
- Output file: `/app/outputs/elastic_properties.json`
- Format: json
- Contract: JSON object with keys: NbO (object with C11, C12, C44, bulk_modulus, shear_modulus, youngs_modulus, poissons_ratio, Vickers_hardness, all floats), NiAs (object with C11, C33, C44, C12, C13, bulk_modulus, shear_modulus, youngs_modulus, poissons_ratio, Vickers_hardness, all floats).
- Scoring: scored by hidden verifier

### Step 5: Quasi-harmonic Debye model thermodynamic properties
- Role: scored
- Action: Using the E-V data and fitted EOS parameters for NbO-type ReN, apply the quasi-harmonic Debye model (e.g., GIBBS2 code) to compute the Debye temperature at zero pressure and the isochoric heat capacity Cv and thermal expansion coefficient α as functions of temperature at pressures 0 and 50 GPa. Output the Debye temperature and the four temperature-dependent curves.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: JSON object with keys: Debye_temperature_NbO_K (float), thermal_expansion_0GPa (list of objects with T and alpha), thermal_expansion_50GPa (list of objects with T and alpha), heat_capacity_0GPa (list of objects with T and Cv), heat_capacity_50GPa (list of objects with T and Cv).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_transition.json`
- `/app/outputs/elastic_properties.json`
- `/app/outputs/thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_transition.json
- path: `/app/outputs/phase_transition.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The transition pressure from the crossing of NbO and NiAs enthalpy curves, verified against the paper-reported value within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `transition_pressure_GPa`: float (pressure in GPa)
    - `NbO_enthalpy`: array of {P: float (GPa), H: float (eV or arbitrary unit)}
    - `NiAs_enthalpy`: array of {P: float (GPa), H: float (same unit as NbO)}

### elastic_properties.json
- path: `/app/outputs/elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constants and derived mechanical properties for both phases at zero pressure, compared to the paper's reported values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `NbO`: object with fields C11, C12, C44, bulk_modulus, shear_modulus, youngs_modulus, poissons_ratio, Vickers_hardness (all floats, elastic moduli in GPa, hardness in GPa)
    - `NiAs`: object with fields C11, C33, C44, C12, C13, bulk_modulus, shear_modulus, youngs_modulus, poissons_ratio, Vickers_hardness (all floats, elastic moduli in GPa, hardness in GPa)

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Debye temperature compared to paper reference; Cv and α curves checked for correct qualitative trends (Dulong-Petit limit, pressure dependence).
- schema:
  - `type`: object
  - `required`:
    - `Debye_temperature_NbO_K`: float (Debye temperature in K at 0 GPa)
    - `thermal_expansion_0GPa`: array of {T: float (K), alpha: float (10^-5 K^-1 or arbitrary)}
    - `thermal_expansion_50GPa`: array of {T: float (K), alpha: float}
    - `heat_capacity_0GPa`: array of {T: float (K), Cv: float (J/mol/K)}
    - `heat_capacity_50GPa`: array of {T: float (K), Cv: float}

Notes: The agent must use open-source DFT and the quasi-harmonic Debye model; the paper's VASP results are not required. All artifacts are human-readable and re-derivable from the raw data the agent computes. No paper identity or gold values are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_transition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "transition_pressure_GPa": "float (pressure in GPa)",
          "NbO_enthalpy": "array of {P: float (GPa), H: float (eV or arbitrary unit)}",
          "NiAs_enthalpy": "array of {P: float (GPa), H: float (same unit as NbO)}"
        }
      },
      "description": "The transition pressure from the crossing of NbO and NiAs enthalpy curves, verified against the paper-reported value within tolerance."
    },
    {
      "file": "elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "NbO": "object with fields C11, C12, C44, bulk_modulus, shear_modulus, youngs_modulus, poissons_ratio, Vickers_hardness (all floats, elastic moduli in GPa, hardness in GPa)",
          "NiAs": "object with fields C11, C33, C44, C12, C13, bulk_modulus, shear_modulus, youngs_modulus, poissons_ratio, Vickers_hardness (all floats, elastic moduli in GPa, hardness in GPa)"
        }
      },
      "description": "Elastic constants and derived mechanical properties for both phases at zero pressure, compared to the paper's reported values with tolerances."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Debye_temperature_NbO_K": "float (Debye temperature in K at 0 GPa)",
          "thermal_expansion_0GPa": "array of {T: float (K), alpha: float (10^-5 K^-1 or arbitrary)}",
          "thermal_expansion_50GPa": "array of {T: float (K), alpha: float}",
          "heat_capacity_0GPa": "array of {T: float (K), Cv: float (J/mol/K)}",
          "heat_capacity_50GPa": "array of {T: float (K), Cv: float}"
        }
      },
      "description": "Debye temperature compared to paper reference; Cv and α curves checked for correct qualitative trends (Dulong-Petit limit, pressure dependence)."
    }
  ],
  "notes": "The agent must use open-source DFT and the quasi-harmonic Debye model; the paper's VASP results are not required. All artifacts are human-readable and re-derivable from the raw data the agent computes. No paper identity or gold values are exposed."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects the three scored files in `/app/outputs`:

- **phase_transition.json**: The verifier recomputes the transition pressure from the enthalpy curves you supply and checks that the crossing point lies within an acceptable tolerance of an expected value.
- **elastic_properties.json**: The verifier compares your elastic constants and Vickers hardness against a hidden reference and verifies that the NiAs phase satisfies mechanical stability criteria.
- **thermodynamic_properties.json**: The verifier compares the Debye temperature to a reference and examines the temperature dependence of the heat capacity and thermal expansion curves. The heat capacity should approach the classical Dulong-Petit limit (~49.9 J mol⁻¹ K⁻¹) at high temperatures and decrease with pressure; the thermal expansion coefficient should exhibit a rapid T³-like rise at low temperatures and a slower, approximately linear increase at high temperatures, decreasing monotonically with pressure.

Each scored artifact contributes a fraction of the total reward; the final score is the weighted sum of the individual checks.
