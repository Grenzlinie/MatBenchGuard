# First-principles investigation of structural, mechanical, electronic, magnetic and thermoelectric properties of VTiRhZ (Z=Al, Ga, In) quaternary Heusler alloys

## Problem background
Quaternary Heusler alloys of the form XX'YZ are candidate materials for spintronic and thermoelectric applications due to their tunable electronic, magnetic, and transport properties. This task investigates the structural, dynamical, mechanical, electronic, magnetic, and thermoelectric properties of three such alloys — VTiRhAl, VTiRhGa, and VTiRhIn — using first-principles density functional theory. The objective is to compute the equilibrium crystal structure, confirm dynamical and mechanical stability, obtain the electronic band structure and magnetic moments, and evaluate the thermoelectric figure of merit of each alloy, in order to assess their potential for half-metallic ferromagnetism and thermoelectric energy conversion.

## Approach
The approach is based on density functional theory (DFT) with the Perdew–Burke–Ernzerhof generalized gradient approximation (GGA‑PBE) for exchange and correlation. The type‑I cubic configuration (LiMgPdSn-type, space group F‑43m) is used as the initial structure for all three alloys. First, full structural relaxations are performed to determine equilibrium lattice constants. Phonon dispersion curves are computed using density functional perturbation theory (DFPT) or the finite‑displacement method to assess dynamical stability. Independent elastic constants C11, C12, and C44 are extracted from stress‑strain DFT calculations, from which derived mechanical moduli (bulk, shear, Young’s modulus, Poisson’s ratio, anisotropy, Cauchy pressure, Pugh’s ratio, and melting temperature) can be obtained. Spin‑polarized band structures and densities of states are computed to determine band gaps and spin polarization at the Fermi level. Total and atom‑resolved magnetic moments are extracted from the spin‑resolved charge density. Finally, thermoelectric transport properties (Seebeck coefficient, electrical conductivity, power factor, electronic thermal conductivity) are calculated within the constant relaxation time approximation using Boltzmann transport theory for the minority‑spin channel at 300 K and 800 K. Lattice thermal conductivity is estimated from the elastic constants and density using Slack’s equation, leading to the dimensionless figure of merit ZT for both p‑type and n‑type doping. All computations are performed with open‑source tools (Quantum ESPRESSO, PHONOPY, BoltzTraP2) and standard pseudopotentials.

## Reproduction target
The reproduction target is to compute and report the following quantities for each of the three alloys VTiRhAl, VTiRhGa, and VTiRhIn:
1. Equilibrium lattice constants (in Å) from structural optimization in the type‑I cubic configuration.
2. Phonon dynamical stability: maximum negative (imaginary) phonon frequency (in cm⁻¹) and a boolean indicating that no imaginary frequencies exceed –5 cm⁻¹.
3. Independent elastic constants C11, C12, and C44 (in GPa).
4. Electronic properties: spin‑majority and spin‑minority band gaps (in eV) and spin polarization at the Fermi level (%).
5. Magnetic moments: total magnetic moment and local moments on each atomic site (V, Ti, Rh, and the Z element) in μB.
6. Thermoelectric properties: maximum ZT and the corresponding Seebeck coefficient (μV/K) and power factor (W/m·K²·s) for both p‑type and n‑type doping at 300 K and 800 K.
The computed results should demonstrate the trends in these properties as the Z atom changes from Al to Ga to In.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- BoltzTraP2: https://bitbucket.org/sousaw/boltzTraP/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Lattice constants and structural optimization
- Role: scored
- Action: Perform DFT structural optimization for VTiRhAl, VTiRhGa, and VTiRhIn in the type‑I cubic configuration (space group F‑43m) using the GGA‑PBE functional. Extract equilibrium lattice constants.
- Output file: `/app/outputs/step_01_lattice_constants.json`
- Format: json
- Contract: {"VTiRhAl": float, "VTiRhGa": float, "VTiRhIn": float}
- Scoring: scored by hidden verifier

### Step 2: Phonon dynamical stability
- Role: scored
- Action: Compute phonon dispersion curves for each alloy using density functional perturbation theory (DFPT) or the finite‑displacement method (via PHONOPY). Report the maximum negative (imaginary) frequency in cm⁻¹ and a boolean (dynamical_stable) indicating no imaginary frequencies within a tolerance of –5 cm⁻¹.
- Output file: `/app/outputs/step_02_phonon_stability.json`
- Format: json
- Contract: {"VTiRhAl": {"max_neg_freq": float, "dynamical_stable": bool}, "VTiRhGa": {"max_neg_freq": float, "dynamical_stable": bool}, "VTiRhIn": {"max_neg_freq": float, "dynamical_stable": bool}}
- Scoring: scored by hidden verifier

### Step 3: Elastic constants
- Role: scored (load-bearing)
- Action: Compute the independent elastic constants C11, C12, C44 (in GPa) for each alloy from first‑principles stress‑strain DFT calculations. (The checker will later recompute the derived mechanical moduli: bulk modulus, shear modulus, Young's modulus, Poisson's ratio, anisotropy factor, Cauchy pressure, Pugh's ratio, and melting temperature from these constants.)
- Output file: `/app/outputs/step_03_elastic_constants.json`
- Format: json
- Contract: {"VTiRhAl": {"C11": float, "C12": float, "C44": float}, "VTiRhGa": {"C11": float, "C12": float, "C44": float}, "VTiRhIn": {"C11": float, "C12": float, "C44": float}}
- Scoring: scored by hidden verifier

### Step 4: Electronic properties
- Role: scored
- Action: Compute spin‑polarized band structure and density of states for each alloy. Report the spin‑up (majority) band gap (in eV; set to -1 if metallic), the spin‑down (minority) band gap, and the spin polarization at the Fermi level (%).
- Output file: `/app/outputs/step_04_electronic_properties.json`
- Format: json
- Contract: {"VTiRhAl": {"bandgap_majority": float, "bandgap_minority": float, "spin_polarization": float}, "VTiRhGa": {...}, "VTiRhIn": {...}}
- Scoring: scored by hidden verifier

### Step 5: Magnetic moments
- Role: scored
- Action: Extract total and atom‑resolved magnetic moments (in μB) from the spin‑resolved charge density for each alloy.
- Output file: `/app/outputs/step_05_magnetic_moments.json`
- Format: json
- Contract: {"VTiRhAl": {"total": float, "V": float, "Ti": float, "Rh": float, "Z": float}, "VTiRhGa": {...}, "VTiRhIn": {...}}
- Scoring: scored by hidden verifier

### Step 6: Thermoelectric properties
- Role: scored
- Action: Using the Boltzmann transport equation (BoltzTraP2) on a dense k‑mesh, compute the Seebeck coefficient (S), power factor (PF) and electronic thermal conductivity per relaxation time as functions of chemical potential at 300 K and 800 K for the minority‑spin channel. Compute the lattice thermal conductivity using Slack’s equation from the elastic constants and density. Evaluate the figure of merit ZT for p‑type and n‑type doping and report the maximum ZT together with the corresponding Seebeck coefficient and power factor at each temperature for each alloy.
- Output file: `/app/outputs/step_06_thermoelectric.json`
- Format: json
- Contract: {"VTiRhAl": {"T300": {"S_p": float, "PF_p": float, "ZT_p": float, "S_n": float, "PF_n": float, "ZT_n": float}, "T800": {...}}, "VTiRhGa": {...}, "VTiRhIn": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_constants.json`
- `/app/outputs/step_02_phonon_stability.json`
- `/app/outputs/step_03_elastic_constants.json`
- `/app/outputs/step_04_electronic_properties.json`
- `/app/outputs/step_05_magnetic_moments.json`
- `/app/outputs/step_06_thermoelectric.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_constants.json
- path: `/app/outputs/step_01_lattice_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constants of the three Heusler alloys in the type‑I configuration.
- schema:
  - `type`: object
  - `required`:
    - `VTiRhAl`: float (Å)
    - `VTiRhGa`: float (Å)
    - `VTiRhIn`: float (Å)

### step_02_phonon_stability.json
- path: `/app/outputs/step_02_phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon dynamical stability: maximum negative (imaginary) frequency; a value > –5 cm⁻¹ indicates stability.
- schema:
  - `type`: object
  - `required`:
    - `VTiRhAl`:
      - `max_neg_freq`: float (cm⁻¹)
      - `dynamical_stable`: bool
    - `VTiRhGa`:
      - `max_neg_freq`: float (cm⁻¹)
      - `dynamical_stable`: bool
    - `VTiRhIn`:
      - `max_neg_freq`: float (cm⁻¹)
      - `dynamical_stable`: bool

### step_03_elastic_constants.json
- path: `/app/outputs/step_03_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Independent elastic constants. The checker recomputes derived mechanical moduli (B, G, E, ν, A, Cp, B/G, Tmelt) and compares them to hidden paper values.
- schema:
  - `type`: object
  - `required`:
    - `VTiRhAl`:
      - `C11`: float (GPa)
      - `C12`: float (GPa)
      - `C44`: float (GPa)
    - `VTiRhGa`:
      - `C11`: float (GPa)
      - `C12`: float (GPa)
      - `C44`: float (GPa)
    - `VTiRhIn`:
      - `C11`: float (GPa)
      - `C12`: float (GPa)
      - `C44`: float (GPa)

### step_04_electronic_properties.json
- path: `/app/outputs/step_04_electronic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin‑resolved band gaps and spin polarization at the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `VTiRhAl`:
      - `bandgap_majority`: float (eV)
      - `bandgap_minority`: float (eV)
      - `spin_polarization`: float (%)
    - `VTiRhGa`:
      - `bandgap_majority`: float (eV)
      - `bandgap_minority`: float (eV)
      - `spin_polarization`: float (%)
    - `VTiRhIn`:
      - `bandgap_majority`: float (eV)
      - `bandgap_minority`: float (eV)
      - `spin_polarization`: float (%)

### step_05_magnetic_moments.json
- path: `/app/outputs/step_05_magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total and atom‑resolved magnetic moments.
- schema:
  - `type`: object
  - `required`:
    - `VTiRhAl`:
      - `total`: float (μB)
      - `V`: float (μB)
      - `Ti`: float (μB)
      - `Rh`: float (μB)
      - `Z`: float (μB)
    - `VTiRhGa`:
      - `total`: float (μB)
      - `V`: float (μB)
      - `Ti`: float (μB)
      - `Rh`: float (μB)
      - `Z`: float (μB)
    - `VTiRhIn`:
      - `total`: float (μB)
      - `V`: float (μB)
      - `Ti`: float (μB)
      - `Rh`: float (μB)
      - `Z`: float (μB)

### step_06_thermoelectric.json
- path: `/app/outputs/step_06_thermoelectric.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermoelectric transport properties: maximum ZT and corresponding Seebeck coefficient and power factor for p‑type and n‑type doping at 300 K and 800 K.
- schema:
  - `type`: object
  - `required`:
    - `VTiRhAl`:
      - `T300`:
        - `S_p`: float (μV/K)
        - `PF_p`: float (W/m·K²·s)
        - `ZT_p`: float
        - `S_n`: float (μV/K)
        - `PF_n`: float (W/m·K²·s)
        - `ZT_n`: float
      - `T800`:
        - `S_p`: float (μV/K)
        - `PF_p`: float (W/m·K²·s)
        - `ZT_p`: float
        - `S_n`: float (μV/K)
        - `PF_n`: float (W/m·K²·s)
        - `ZT_n`: float
    - `VTiRhGa`:
      - `T300`:
        - `S_p`: float
        - `PF_p`: float
        - `ZT_p`: float
        - `S_n`: float
        - `PF_n`: float
        - `ZT_n`: float
      - `T800`:
        - `S_p`: float
        - `PF_p`: float
        - `ZT_p`: float
        - `S_n`: float
        - `PF_n`: float
        - `ZT_n`: float
    - `VTiRhIn`:
      - `T300`:
        - `S_p`: float
        - `PF_p`: float
        - `ZT_p`: float
        - `S_n`: float
        - `PF_n`: float
        - `ZT_n`: float
      - `T800`:
        - `S_p`: float
        - `PF_p`: float
        - `ZT_p`: float
        - `S_n`: float
        - `PF_n`: float
        - `ZT_n`: float

Notes: The elastic constants step is load‑bearing; the checker recomputes the derived mechanical moduli and melting temperature from the submitted Cij. Phonon stability is assessed by the threshold on max_neg_freq (> –5 cm⁻¹). Electronic band gaps and magnetic moments are compared to paper‑reported values with appropriate tolerances. Thermoelectric results are compared directly to the paper's ZT and transport values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "VTiRhAl": "float (Å)",
          "VTiRhGa": "float (Å)",
          "VTiRhIn": "float (Å)"
        }
      },
      "description": "Equilibrium lattice constants of the three Heusler alloys in the type‑I configuration."
    },
    {
      "file": "step_02_phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "VTiRhAl": {
            "max_neg_freq": "float (cm⁻¹)",
            "dynamical_stable": "bool"
          },
          "VTiRhGa": {
            "max_neg_freq": "float (cm⁻¹)",
            "dynamical_stable": "bool"
          },
          "VTiRhIn": {
            "max_neg_freq": "float (cm⁻¹)",
            "dynamical_stable": "bool"
          }
        }
      },
      "description": "Phonon dynamical stability: maximum negative (imaginary) frequency; a value > –5 cm⁻¹ indicates stability."
    },
    {
      "file": "step_03_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "VTiRhAl": {
            "C11": "float (GPa)",
            "C12": "float (GPa)",
            "C44": "float (GPa)"
          },
          "VTiRhGa": {
            "C11": "float (GPa)",
            "C12": "float (GPa)",
            "C44": "float (GPa)"
          },
          "VTiRhIn": {
            "C11": "float (GPa)",
            "C12": "float (GPa)",
            "C44": "float (GPa)"
          }
        }
      },
      "description": "Independent elastic constants. The checker recomputes derived mechanical moduli (B, G, E, ν, A, Cp, B/G, Tmelt) and compares them to hidden paper values."
    },
    {
      "file": "step_04_electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "VTiRhAl": {
            "bandgap_majority": "float (eV)",
            "bandgap_minority": "float (eV)",
            "spin_polarization": "float (%)"
          },
          "VTiRhGa": {
            "bandgap_majority": "float (eV)",
            "bandgap_minority": "float (eV)",
            "spin_polarization": "float (%)"
          },
          "VTiRhIn": {
            "bandgap_majority": "float (eV)",
            "bandgap_minority": "float (eV)",
            "spin_polarization": "float (%)"
          }
        }
      },
      "description": "Spin‑resolved band gaps and spin polarization at the Fermi level."
    },
    {
      "file": "step_05_magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "VTiRhAl": {
            "total": "float (μB)",
            "V": "float (μB)",
            "Ti": "float (μB)",
            "Rh": "float (μB)",
            "Z": "float (μB)"
          },
          "VTiRhGa": {
            "total": "float (μB)",
            "V": "float (μB)",
            "Ti": "float (μB)",
            "Rh": "float (μB)",
            "Z": "float (μB)"
          },
          "VTiRhIn": {
            "total": "float (μB)",
            "V": "float (μB)",
            "Ti": "float (μB)",
            "Rh": "float (μB)",
            "Z": "float (μB)"
          }
        }
      },
      "description": "Total and atom‑resolved magnetic moments."
    },
    {
      "file": "step_06_thermoelectric.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "VTiRhAl": {
            "T300": {
              "S_p": "float (μV/K)",
              "PF_p": "float (W/m·K²·s)",
              "ZT_p": "float",
              "S_n": "float (μV/K)",
              "PF_n": "float (W/m·K²·s)",
              "ZT_n": "float"
            },
            "T800": {
              "S_p": "float (μV/K)",
              "PF_p": "float (W/m·K²·s)",
              "ZT_p": "float",
              "S_n": "float (μV/K)",
              "PF_n": "float (W/m·K²·s)",
              "ZT_n": "float"
            }
          },
          "VTiRhGa": {
            "T300": {
              "S_p": "float",
              "PF_p": "float",
              "ZT_p": "float",
              "S_n": "float",
              "PF_n": "float",
              "ZT_n": "float"
            },
            "T800": {
              "S_p": "float",
              "PF_p": "float",
              "ZT_p": "float",
              "S_n": "float",
              "PF_n": "float",
              "ZT_n": "float"
            }
          },
          "VTiRhIn": {
            "T300": {
              "S_p": "float",
              "PF_p": "float",
              "ZT_p": "float",
              "S_n": "float",
              "PF_n": "float",
              "ZT_n": "float"
            },
            "T800": {
              "S_p": "float",
              "PF_p": "float",
              "ZT_p": "float",
              "S_n": "float",
              "PF_n": "float",
              "ZT_n": "float"
            }
          }
        }
      },
      "description": "Thermoelectric transport properties: maximum ZT and corresponding Seebeck coefficient and power factor for p‑type and n‑type doping at 300 K and 800 K."
    }
  ],
  "notes": "The elastic constants step is load‑bearing; the checker recomputes the derived mechanical moduli and melting temperature from the submitted Cij. Phonon stability is assessed by the threshold on max_neg_freq (> –5 cm⁻¹). Electronic band gaps and magnetic moments are compared to paper‑reported values with appropriate tolerances. Thermoelectric results are compared directly to the paper's ZT and transport values."
}
```

## How you are scored
A hidden verifier independently scores each output artifact from the workflow steps. The elastic constants are load‑bearing: the checker recomputes derived mechanical moduli (bulk modulus, shear modulus, Young’s modulus, Poisson’s ratio, anisotropy factor, Cauchy pressure, Pugh’s ratio, and melting temperature) from the submitted Cij and compares them to a secret reference. Phonon stability is checked by the threshold on the reported maximum negative frequency. Electronic band gaps, magnetic moments, and thermoelectric ZT values are compared to hidden expected values within appropriate tolerances. Additionally, the verifier checks that lattice constants, band gaps, mechanical moduli, and ZT follow a monotonic trend with respect to the atomic number of the Z element. Each stage contributes a weight to the final reward; simply quoting the paper’s numbers is not sufficient—the raw computed artifacts must be re‑derivable and consistent with the prescribed workflow.
