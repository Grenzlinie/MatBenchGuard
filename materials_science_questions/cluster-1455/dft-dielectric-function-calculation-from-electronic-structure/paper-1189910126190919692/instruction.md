# Static Dielectric Constants and Phonon Polariton Dispersion Shift

## Problem background
Phonon polaritons (PhPs) in the van der Waals crystal α-MoO₃ enable deep subwavelength confinement of mid-infrared light, but active tuning of their dispersion remains a challenge. Metal intercalation into the van der Waals gap has been proposed as a chemical route to modify the crystal's dielectric response and thereby shift the PhP dispersion. Understanding the mechanism requires quantifying how the static dielectric permittivity changes upon intercalation and whether that change alone can explain the resulting dispersion shift. This task investigates the hypothesis that tin intercalation increases the static dielectric permittivity of α-MoO₃, leading to a measurable shift of the phonon polariton wavevector along the [100] direction.

## Approach
The computational approach combines density functional theory (DFT) with analytical electromagnetic modeling:

1. **DFT geometry relaxation:** The atomic positions and lattice parameters of pristine α-MoO₃ (primitive cell) and a 3×3×1 supercell with one Sn atom placed in the van der Waals gap are optimized to low residual forces.

2. **Dielectric constant extraction:** The static dielectric tensor (ε∞) for both systems is computed via density functional perturbation theory (DFPT) or an equivalent linear-response method, using the same DFT functional and pseudopotentials as the relaxation.

3. **Analytical PhP dispersion:** Using the computed ε∞ and published Lorentz oscillator parameters that describe the phonon modes of α-MoO₃ along the three principal axes, the frequency-dependent dielectric permittivity ε_x(ω) is obtained. The phonon polariton dispersion (wavevector versus frequency) for a 120‑nm‑thick α‑MoO₃ flake on a silicon substrate is then calculated from the slab waveguide dispersion relation for a uniaxial thin film. The shift in dispersion due to intercalation is quantified as the relative change in wavevector at a fixed frequency.

## Reproduction target
Compute the static dielectric tensor (ε∞) for pristine α‑MoO₃ and for Sn‑intercalated α‑MoO₃ (3×3×1 supercell, one Sn atom). Using those constants together with the published Lorentz oscillator parameters for α‑MoO₃, calculate the analytical phonon polariton dispersion for a 120‑nm‑thick flake on silicon over the frequency range 820–970 cm⁻¹. Report:
- The three static dielectric components for pristine and Sn‑intercalated systems.
- The analytical PhP dispersion curves for both systems.
- The relative dispersion shift Δk/k at 860 cm⁻¹, where Δk = k_pristine − k_Sn.

## Assets

- α-MoO₃ crystal structure: Materials Project ID mp-1867 (https://materialsproject.org/materials/mp-1867) or COD entry 1531279
- Pseudopotentials for Mo, O, Sn: SSSP Efficiency 1.3.0 (https://www.materialscloud.org/discover/sssp/table/efficiency)
- DFT software (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: DFT geometry relaxation
- Role: process
- Action: Perform DFT geometry relaxation of (i) the pristine α-MoO₃ primitive cell and (ii) a 3×3×1 supercell with one Sn atom placed in the van der Waals gap at the most stable intercalation site. The relaxations must optimize atomic positions and lattice parameters to meet reasonable force convergence criteria.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 2: DFT static dielectric constants via linear response
- Role: process
- Action: Using the relaxed geometries from step_01, compute the static dielectric tensor (ε∞) for both pristine and Sn-intercalated α-MoO₃ via density functional perturbation theory or an equivalent linear-response method. Use the same DFT functional and pseudopotentials as in step_01.
- Evidence: `/app/outputs/dielectric_raw_output.txt`

### Step 3: Analytical phonon polariton dispersion and data report
- Role: scored (load-bearing)
- Action: 1) Extract the computed static dielectric tensor components ε_x, ε_y, ε_z for pristine and Sn-intercalated α-MoO₃ from the DFPT output. 2) Using the Lorentz oscillator model with the fixed phonon parameters from Ref [38] (doi:10.1002/adma.202001908), compute the frequency-dependent dielectric permittivity ε_x(ω) over the frequency range 820–970 cm⁻¹. 3) Compute the phonon polariton (PhP) dispersion (wavevector k vs frequency ω) for a 120‑nm‑thick α‑MoO₃ flake on a silicon substrate using the analytical slab waveguide model, with no free parameters beyond the geometry and the permittivity model. 4) Calculate the relative dispersion shift Δk/k at ω = 860 cm⁻¹, defined as (k_pristine − k_Sn)/k_pristine. 5) Write all computed quantities to dft_and_dispersion_results.json.
- Output file: `/app/outputs/dft_and_dispersion_results.json`
- Format: json
- Contract: {
  "pristine": {
    "epsilon_x": number,
    "epsilon_y": number,
    "epsilon_z": number
  },
  "Sn_intercalated": {
    "epsilon_x": number,
    "epsilon_y": number,
    "epsilon_z": number
  },
  "dispersion_shift": number (Δk/k at 860 cm⁻¹, as a decimal fraction),
  "analytical_dispersion_pristine": [{"frequency_cm-1": number, "wavevector_um-1": number}, ...],
  "analytical_dispersion_Sn": [{"frequency_cm-1": number, "wavevector_um-1": number}, ...]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_and_dispersion_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_and_dispersion_results.json
- path: `/app/outputs/dft_and_dispersion_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline DFT-calculated static dielectric constants, analytically computed phonon polariton dispersion, and the relative shift Δk/k, which constitute the main computational evidence for dielectric permittivity modulation as the mechanism of the observed dispersion shift.
- schema:
  - `type`: object
  - `required`: `pristine`, `Sn_intercalated`, `dispersion_shift`, `analytical_dispersion_pristine`, `analytical_dispersion_Sn`
  - `properties`:
    - `pristine`:
      - `type`: object
      - `required`: `epsilon_x`, `epsilon_y`, `epsilon_z`
      - `epsilon_x`:
        - `type`: number
      - `epsilon_y`:
        - `type`: number
      - `epsilon_z`:
        - `type`: number
    - `Sn_intercalated`:
      - `type`: object
      - `required`: `epsilon_x`, `epsilon_y`, `epsilon_z`
      - `epsilon_x`:
        - `type`: number
      - `epsilon_y`:
        - `type`: number
      - `epsilon_z`:
        - `type`: number
    - `dispersion_shift`:
      - `type`: number
      - `description`: Δk/k at 860 cm⁻¹, decimal fraction
    - `analytical_dispersion_pristine`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `frequency_cm-1`, `wavevector_um-1`
        - `frequency_cm-1`:
          - `type`: number
        - `wavevector_um-1`:
          - `type`: number
    - `analytical_dispersion_Sn`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `frequency_cm-1`, `wavevector_um-1`
        - `frequency_cm-1`:
          - `type`: number
        - `wavevector_um-1`:
          - `type`: number

Notes: No gold values or tolerances are disclosed here. The checker will compare the submitted constants and shift against hidden paper-reported gold with appropriate tolerances and will also recompute the analytical dispersion from the submitted ε∞ to verify internal consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_and_dispersion_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "pristine",
          "Sn_intercalated",
          "dispersion_shift",
          "analytical_dispersion_pristine",
          "analytical_dispersion_Sn"
        ],
        "properties": {
          "pristine": {
            "type": "object",
            "required": [
              "epsilon_x",
              "epsilon_y",
              "epsilon_z"
            ],
            "epsilon_x": {
              "type": "number"
            },
            "epsilon_y": {
              "type": "number"
            },
            "epsilon_z": {
              "type": "number"
            }
          },
          "Sn_intercalated": {
            "type": "object",
            "required": [
              "epsilon_x",
              "epsilon_y",
              "epsilon_z"
            ],
            "epsilon_x": {
              "type": "number"
            },
            "epsilon_y": {
              "type": "number"
            },
            "epsilon_z": {
              "type": "number"
            }
          },
          "dispersion_shift": {
            "type": "number",
            "description": "Δk/k at 860 cm⁻¹, decimal fraction"
          },
          "analytical_dispersion_pristine": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "frequency_cm-1",
                "wavevector_um-1"
              ],
              "frequency_cm-1": {
                "type": "number"
              },
              "wavevector_um-1": {
                "type": "number"
              }
            }
          },
          "analytical_dispersion_Sn": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "frequency_cm-1",
                "wavevector_um-1"
              ],
              "frequency_cm-1": {
                "type": "number"
              },
              "wavevector_um-1": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Headline DFT-calculated static dielectric constants, analytically computed phonon polariton dispersion, and the relative shift Δk/k, which constitute the main computational evidence for dielectric permittivity modulation as the mechanism of the observed dispersion shift."
    }
  ],
  "notes": "No gold values or tolerances are disclosed here. The checker will compare the submitted constants and shift against hidden paper-reported gold with appropriate tolerances and will also recompute the analytical dispersion from the submitted ε∞ to verify internal consistency."
}
```

## How you are scored
A hidden verifier independently inspects your `dft_and_dispersion_results.json` and compares it to a hidden reference (a combination of paper‑reported values and self‑consistency checks). The scoring is a weighted sum of the following checks:
- **Static dielectric constants:** Your computed ε∞ for pristine and Sn‑intercalated systems are compared to the reference values with predefined tolerances.
- **Dispersion self‑consistency:** The verifier recomputes the analytical phonon polariton dispersion from your submitted ε∞ using the same Lorentz parameters and waveguide model, then compares the recomputed dispersion curves to the ones you reported.
- **Dispersion shift:** The verifier checks that the reported sign of Δk/k is physically consistent with an increase in permittivity and that its magnitude falls within an expected range.

Each check contributes a portion of the final reward; simply reporting numbers is not enough—they must be the result of genuine DFT and analytical calculations.
