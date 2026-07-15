# Reproduce structural parameters and phase transition pressures of SnO2 from DFT

## Problem background
Tin dioxide (SnO₂) is a wide-band-gap semiconductor with applications in gas sensing and solar cells. This work uses first-principles density functional theory (DFT) to investigate the ground-state structural properties and the pressure-induced phase transitions from the ambient rutile structure to the CaCl₂-type and then to a cubic structure. The quantities of interest are the equilibrium lattice constants and internal atomic coordinates for each phase, as well as the pressures at which the structural transitions occur.

## Approach
The reproduction is based on DFT calculations within the local density approximation (LDA) and the generalized gradient approximation (GGA/PBE). You will use an open-source plane-wave code and standard pseudopotentials. For each of the three SnO₂ structures — rutile (space group P4₂/mnm), CaCl₂-type (Pnnm), and cubic (Pa-3) — you will set up the unit cell with the appropriate Wyckoff positions. For a range of volumes around the expected equilibrium, you will relax the internal atomic coordinates and optimize the cell shape (e.g., c/a ratio for rutile, b/a ratio for CaCl₂-type) while keeping the volume constant, and collect the total energy. The resulting energy–volume curves will be fitted to the Murnaghan equation of state to obtain the equilibrium lattice parameters and internal coordinates. To determine transition pressures, you will compute enthalpy H = E + PV for each phase over a range of pressures and locate the pressure where the enthalpy curves of the lower-pressure and higher-pressure phases intersect.

## Reproduction target
Produce two scored output files: (1) `/app/outputs/structural_params.json` containing the equilibrium lattice parameters (a, b, c in Å) and internal coordinates (u, v) for each of the three phases under both LDA and GGA functionals; (2) `/app/outputs/transition_pressures.json` containing the rutile→CaCl₂ and CaCl₂→cubic transition pressures (in GPa) for both LDA and GGA. The data must be obtained by executing the DFT workflow described in the steps; self‑reported numbers without evidence of the required computations will not be accepted.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials for O and Sn: https://www.materialscloud.org/discover/sssp

## Omitted quantities

The paper also reports cohesive energy, bulk modulus, band gaps, effective masses, and ionicity factor. These are not included as scored artifacts for the following reasons:
- **Cohesive energy and bulk modulus**: derivable from the same equation-of-state fit, but require accurate isolated-atom total energies and are less central to the phase-transition claim; they are omitted to keep the task focused on the structural quantities that directly determine the transition pressures.
- **Band gaps**: the paper reports both GGA and EVGGA gaps; however, the open-source code (Quantum ESPRESSO) does not provide EVGGA, and the GGA gap is well-known to be systematically underestimated and highly sensitive to pseudopotential and k-point choices. A reliable tolerance cannot be established without mandating a specific computational protocol beyond what is described.
- **Effective masses**: determined from band curvatures at the Γ point; they are exquisitely sensitive to the k-point sampling and the specific band interpolation scheme, and again the paper's EVGGA values are not accessible with the chosen toolchain. A meaningful scoring would require a reference calculation that is not available.
- **Ionicity factor**: this is an empirical measure derived from charge density plots using a model-dependent formula; there is no independently verifiable gold value, and its precise numerical value depends on the charge density analysis method. It is therefore not a well-posed computational reproduction target.

The core phase transition claim is fully captured by the equilibrium structural parameters and transition pressures, which are scored.

## Workflow steps

### Step 1: Generate total energy vs volume curves
- Role: process
- Action: For each SnO₂ phase (rutile P4₂/mnm, CaCl₂-type Pnnm, cubic Pa-3) and exchange-correlation functional (LDA, GGA/PBE), set up the unit cell and run DFT calculations over a range of volumes. At each volume, relax the internal atomic positions and optimize cell shape while keeping volume constant. Collect total energy and cell data into a structured evidence file.
- Evidence: `/app/outputs/total_energy_vs_volume.json`

### Step 2: Extract equilibrium lattice parameters
- Role: scored (load-bearing)
- Action: For each phase and functional, fit the total energy vs volume data to the Murnaghan equation of state to find equilibrium volume. Compute equilibrium lattice parameters (a, b, c) and internal coordinates (u, v).
- Output file: `/app/outputs/structural_params.json`
- Format: json
- Contract: JSON object with keys: rutile_LDA {a (Angstrom), c (Angstrom), u}, rutile_GGA {a, c, u}, CaCl2_LDA {a, b, c, u, v}, CaCl2_GGA {a, b, c, u, v}, cubic_LDA {a, u}, cubic_GGA {a, u}
- Scoring: scored by hidden verifier

### Step 3: Determine phase transition pressures
- Role: scored (load-bearing)
- Action: Using the total energy vs volume data, compute enthalpy H = E + PV for each phase over a range of pressures. Identify the pressure where the enthalpy curves of the lower- and higher-pressure phases intersect to determine the rutile→CaCl₂ and CaCl₂→cubic transition pressures.
- Output file: `/app/outputs/transition_pressures.json`
- Format: json
- Contract: JSON object with keys: LDA {rutile_cacl2 (GPa), cacl2_cubic (GPa)}, GGA {rutile_cacl2, cacl2_cubic}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_params.json`
- `/app/outputs/transition_pressures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_params.json
- path: `/app/outputs/structural_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium structural parameters from EOS fitting. Each top-level key corresponds to a phase/functional combination with the listed fields.
- schema:
  - `type`: object
  - `required`:
    - `rutile_LDA`: object with a (Angstrom), c (Angstrom), u (dimensionless)
    - `rutile_GGA`: object with a, c, u
    - `CaCl2_LDA`: object with a, b, c, u, v (all Angstrom except u,v dimensionless)
    - `CaCl2_GGA`: object with a, b, c, u, v
    - `cubic_LDA`: object with a (Angstrom), u
    - `cubic_GGA`: object with a, u
  - `items`: None
  - `required_columns`: None
  - `units`:
    - `a`: Angstrom
    - `b`: Angstrom
    - `c`: Angstrom
    - `u`: dimensionless
    - `v`: dimensionless

### transition_pressures.json
- path: `/app/outputs/transition_pressures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Transition pressures determined from common tangent of enthalpy curves.
- schema:
  - `type`: object
  - `required`:
    - `LDA`: object with rutile_cacl2 (GPa), cacl2_cubic (GPa)
    - `GGA`: object with rutile_cacl2 (GPa), cacl2_cubic (GPa)
  - `items`: None
  - `required_columns`: None
  - `units`:
    - `rutile_cacl2`: GPa
    - `cacl2_cubic`: GPa

Notes: Both LDA and GGA results must be provided. Tolerances accommodate systematic differences between DFT implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "rutile_LDA": "object with a (Angstrom), c (Angstrom), u (dimensionless)",
          "rutile_GGA": "object with a, c, u",
          "CaCl2_LDA": "object with a, b, c, u, v (all Angstrom except u,v dimensionless)",
          "CaCl2_GGA": "object with a, b, c, u, v",
          "cubic_LDA": "object with a (Angstrom), u",
          "cubic_GGA": "object with a, u"
        },
        "items": null,
        "required_columns": null,
        "units": {
          "a": "Angstrom",
          "b": "Angstrom",
          "c": "Angstrom",
          "u": "dimensionless",
          "v": "dimensionless"
        }
      },
      "description": "Equilibrium structural parameters from EOS fitting. Each top-level key corresponds to a phase/functional combination with the listed fields."
    },
    {
      "file": "transition_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA": "object with rutile_cacl2 (GPa), cacl2_cubic (GPa)",
          "GGA": "object with rutile_cacl2 (GPa), cacl2_cubic (GPa)"
        },
        "items": null,
        "required_columns": null,
        "units": {
          "rutile_cacl2": "GPa",
          "cacl2_cubic": "GPa"
        }
      },
      "description": "Transition pressures determined from common tangent of enthalpy curves."
    }
  ],
  "notes": "Both LDA and GGA results must be provided. Tolerances accommodate systematic differences between DFT implementations."
}
```

## How you are scored
Your submission is evaluated automatically by a hidden verifier. The verifier reads your `structural_params.json` and `transition_pressures.json` and compares each reported value against independently established reference values. The comparison uses tolerances that accommodate systematic differences between DFT implementations, so a careful reproduction performed with the described workflow is expected to pass. Both LDA and GGA results must be present; missing or incomplete entries are penalized. Each scored artifact carries a weight that is combined into a final reward; simple schema validation alone contributes negligible reward. The verifier is unknown to you — the only way to succeed is to carry out the stated DFT protocol faithfully.
