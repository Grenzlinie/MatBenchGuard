# First-principles DFT calculation of binding energy, tensile stiffness, and phonon stability of carbon chains

## Problem background
Carbyne is a one‐dimensional carbon allotrope that can exist in two structural forms: cumulene, with consecutive double bonds (=C=C=), and polyyne, with alternating triple and single bonds (–C≡C–). First‐principles calculations can predict which of these two phases is thermodynamically more stable, which is mechanically stiffer, and whether either phase is dynamically unstable (indicated by imaginary phonon frequencies). This task asks you to compute those three key properties from density functional theory (DFT) and thereby provide a quantitative assessment of the relative stability and stiffness of the two carbon chains.

## Approach
Use plane‑wave DFT with the Perdew–Wang 91 (PW91) generalized‑gradient approximation (GGA) exchange–correlation functional, as implemented in the open‑source Quantum ESPRESSO package. Represent the carbon atoms with a suitable GGA pseudopotential from a public library (e.g., SSSP).

1. **Crystal binding energy**: Optimize the unit cells of cumulene and polyyne and compute their total energies. Additionally, compute the total energy of a single carbon atom in a large box. From these, derive the binding energy per atom as \(W = (2E_{\text{atom}} - E_{\text{cell}})/2\). The difference \(W_{\text{polyyne}} - W_{\text{cumulene}}\) (in meV/atom) reveals which phase is thermodynamically preferred.
2. **Tensile stiffness**: Starting from the equilibrium structures, apply a series of small uniaxial strains along the chain direction and compute the total energy at each strain. Fit the energy–strain curve to a second‑order polynomial and extract the tensile stiffness \(C = (1/a)\, d^2E/d\varepsilon^2\), where \(a\) is the equilibrium cell length. This quantity measures the mechanical resistance of each chain to stretching.
3. **Phonon stability of cumulene**: For the optimized cumulene cell, calculate the phonon dispersion along the high‑symmetry path G–Q–Z. Record the lowest phonon frequency and flag whether any imaginary (negative) frequencies appear. Imaginary modes signal dynamical instability.

## Reproduction target
Perform all DFT calculations with Quantum ESPRESSO using the PW91 functional and a public carbon pseudopotential (e.g., from the SSSP library). Produce the following three scored artifacts in `/app/outputs`:

- `total_energies.json`: crystal binding energy per atom for both cumulene and polyyne, and the binding‑energy difference (polyyne minus cumulene) in meV/atom.
- `tensile_stiffness.json`: tensile stiffness of cumulene and polyyne in eV/Å.
- `phonon_frequencies.json`: minimum phonon frequency (THz), a Boolean flag indicating the presence of imaginary modes, and the frequencies at high‑symmetry points for cumulene.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotential for Carbon: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Compute crystal binding energy per atom
- Role: scored (load-bearing)
- Action: Perform first-principles DFT calculations using the GGA-PW91 exchange-correlation functional to optimize the unit cells of cumulene and polyyne, and obtain the total energy of an isolated carbon atom in a large periodic box. From the converged total energies, derive the crystal binding energy per atom: W = (2*E_atom - E_cell)/2, and compute the binding energy difference (polyyne minus cumulene) in meV/atom. Write the results to total_energies.json.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: {"cumulene": {"total_energy_cell": float (eV), "binding_energy_per_atom": float (eV/atom)}, "polyyne": {"total_energy_cell": float (eV), "binding_energy_per_atom": float (eV/atom)}, "binding_energy_difference_polyyne_minus_cumulene": float (meV/atom)}
- Scoring: scored by hidden verifier

### Step 2: Compute tensile stiffness of cumulene and polyyne
- Role: scored
- Action: Using the equilibrium structures of cumulene and polyyne, perform DFT total energy calculations for a series of uniaxial strains along the chain direction. Fit the energy vs strain curve to a second-order polynomial and extract the tensile stiffness C = (1/a) d²E/dε², where a is the equilibrium cell length. Write the stiffness values to tensile_stiffness.json.
- Output file: `/app/outputs/tensile_stiffness.json`
- Format: json
- Contract: {"cumulene_tensile_stiffness": float (eV/Å), "polyyne_tensile_stiffness": float (eV/Å)}
- Scoring: scored by hidden verifier

### Step 3: Compute phonon dispersion of cumulene and assess dynamical stability
- Role: scored
- Action: Using the optimized cumulene unit cell, compute the phonon dispersion along the high-symmetry path G–Q–Z (as denoted in the paper). Identify the lowest phonon frequency and determine whether any imaginary (negative) frequencies exist. Output the minimum frequency, a boolean flag, and the list of frequencies at high-symmetry points in THz to phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: {"minimum_frequency": float (THz), "has_imaginary_frequencies": bool, "frequencies_at_high_symmetry": [float], "units": "THz"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/tensile_stiffness.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Crystal binding energies, binding-energy difference, band gaps, static dielectric constants, and supercell stability analysis.
- schema:
  - `type`: object
  - `required`: `cumulene`, `polyyne`, `binding_energy_difference_polyyne_minus_cumulene`, `cumulene_band_gap_eV`, `polyyne_band_gap_eV`, `cumulene_static_epsilon_real`, `polyyne_static_epsilon_real`, `supercell_optimal_N`, `supercell_energy_at_optimal_N_eV`, `supercell_energy_at_N4_eV`
  - `properties`:
    - `cumulene`:
      - `type`: object
      - `required`: `total_energy_cell`, `binding_energy_per_atom`
      - `properties`:
        - `total_energy_cell`:
          - `type`: number
          - `unit`: eV
        - `binding_energy_per_atom`:
          - `type`: number
          - `unit`: eV/atom
    - `polyyne`:
      - `type`: object
      - `required`: `total_energy_cell`, `binding_energy_per_atom`
      - `properties`:
        - `total_energy_cell`:
          - `type`: number
          - `unit`: eV
        - `binding_energy_per_atom`:
          - `type`: number
          - `unit`: eV/atom
    - `binding_energy_difference_polyyne_minus_cumulene`:
      - `type`: number
      - `unit`: meV/atom
    - `cumulene_band_gap_eV`:
      - `type`: number
      - `unit`: eV
    - `polyyne_band_gap_eV`:
      - `type`: number
      - `unit`: eV
    - `cumulene_static_epsilon_real`:
      - `type`: number
    - `polyyne_static_epsilon_real`:
      - `type`: number
    - `supercell_optimal_N`:
      - `type`: integer
    - `supercell_energy_at_optimal_N_eV`:
      - `type`: number
      - `unit`: eV
    - `supercell_energy_at_N4_eV`:
      - `type`: number
      - `unit`: eV

### tensile_stiffness.json
- path: `/app/outputs/tensile_stiffness.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Tensile stiffness values for cumulene and polyyne.
- schema:
  - `type`: object
  - `required`: `cumulene_tensile_stiffness`, `polyyne_tensile_stiffness`
  - `properties`:
    - `cumulene_tensile_stiffness`:
      - `type`: number
      - `unit`: eV/Å
    - `polyyne_tensile_stiffness`:
      - `type`: number
      - `unit`: eV/Å

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies of cumulene highlighting presence of imaginary modes.
- schema:
  - `type`: object
  - `required`: `minimum_frequency`, `has_imaginary_frequencies`, `frequencies_at_high_symmetry`, `units`
  - `properties`:
    - `minimum_frequency`:
      - `type`: number
      - `unit`: THz
    - `has_imaginary_frequencies`:
      - `type`: boolean
    - `frequencies_at_high_symmetry`:
      - `type`: array
      - `items`:
        - `type`: number
      - `unit`: THz
    - `units`:
      - `type`: string
      - `const`: THz

Notes: Band gap, dielectric constant, and supercell stability results are folded into total_energies.json to keep the output surface count unchanged while covering all headline findings.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "cumulene",
          "polyyne",
          "binding_energy_difference_polyyne_minus_cumulene",
          "cumulene_band_gap_eV",
          "polyyne_band_gap_eV",
          "cumulene_static_epsilon_real",
          "polyyne_static_epsilon_real",
          "supercell_optimal_N",
          "supercell_energy_at_optimal_N_eV",
          "supercell_energy_at_N4_eV"
        ],
        "properties": {
          "cumulene": {
            "type": "object",
            "required": [
              "total_energy_cell",
              "binding_energy_per_atom"
            ],
            "properties": {
              "total_energy_cell": {
                "type": "number",
                "unit": "eV"
              },
              "binding_energy_per_atom": {
                "type": "number",
                "unit": "eV/atom"
              }
            }
          },
          "polyyne": {
            "type": "object",
            "required": [
              "total_energy_cell",
              "binding_energy_per_atom"
            ],
            "properties": {
              "total_energy_cell": {
                "type": "number",
                "unit": "eV"
              },
              "binding_energy_per_atom": {
                "type": "number",
                "unit": "eV/atom"
              }
            }
          },
          "binding_energy_difference_polyyne_minus_cumulene": {
            "type": "number",
            "unit": "meV/atom"
          },
          "cumulene_band_gap_eV": {
            "type": "number",
            "unit": "eV"
          },
          "polyyne_band_gap_eV": {
            "type": "number",
            "unit": "eV"
          },
          "cumulene_static_epsilon_real": {
            "type": "number"
          },
          "polyyne_static_epsilon_real": {
            "type": "number"
          },
          "supercell_optimal_N": {
            "type": "integer"
          },
          "supercell_energy_at_optimal_N_eV": {
            "type": "number",
            "unit": "eV"
          },
          "supercell_energy_at_N4_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Crystal binding energies, binding-energy difference, band gaps, static dielectric constants, and supercell stability analysis."
    },
    {
      "file": "tensile_stiffness.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "cumulene_tensile_stiffness",
          "polyyne_tensile_stiffness"
        ],
        "properties": {
          "cumulene_tensile_stiffness": {
            "type": "number",
            "unit": "eV/Å"
          },
          "polyyne_tensile_stiffness": {
            "type": "number",
            "unit": "eV/Å"
          }
        }
      },
      "description": "Tensile stiffness values for cumulene and polyyne."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "minimum_frequency",
          "has_imaginary_frequencies",
          "frequencies_at_high_symmetry",
          "units"
        ],
        "properties": {
          "minimum_frequency": {
            "type": "number",
            "unit": "THz"
          },
          "has_imaginary_frequencies": {
            "type": "boolean"
          },
          "frequencies_at_high_symmetry": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "unit": "THz"
          },
          "units": {
            "type": "string",
            "const": "THz"
          }
        }
      },
      "description": "Phonon frequencies of cumulene highlighting presence of imaginary modes."
    }
  ],
  "notes": "Band gap, dielectric constant, and supercell stability results are folded into total_energies.json to keep the output surface count unchanged while covering all headline findings."
}
```

## How you are scored
A hidden verifier will independently read each of the three output files and compare the computed results against a hidden reference. The scoring is weighted across the three stages, with the largest weight on the binding‑energy difference and smaller weights on the tensile stiffness and phonon check. For directional quantities (where “higher” or “lower” corresponds to a clear physical ordering) the verifier awards full credit when the computed value meets or exceeds the expected threshold, and only reduces credit when the outcome is worse. Simply writing a number that looks plausible is not sufficient; the values must be physically consistent and must trace back to the DFT workflow described in the steps.
