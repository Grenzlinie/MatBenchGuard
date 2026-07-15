# DFT properties of chlorine on graphene: single adatom and chlorographene

## Problem background
Graphene's extraordinary electronic properties can be tuned by chemical functionalization. A critical family of modifiers is halogens, yet the interaction of chlorine with graphene—from a single adsorbed atom to a fully chlorinated sheet (chlorographene)—remains incompletely characterized. Understanding the bonding character, migration behavior, and the resulting structural, electronic, and vibrational properties is essential for designing graphene-based devices. This task aims to determine these key properties through first-principles density functional theory (DFT) calculations.

## Approach
Use density functional theory within the local density approximation (LDA) and projector augmented wave (PAW) pseudopotentials, implemented in Quantum ESPRESSO. For a single chlorine atom on graphene, model the system with a (4×4) supercell and place the adatom at the top site. Perform geometry relaxation, compute the binding energy relative to bare graphene and a free chlorine atom, and obtain the migration energy barrier by scanning along the T→B→H→T symmetry path with constrained relaxations. Bader analysis is used to obtain charge transfer, and spin-polarized calculations yield the magnetic moment. For chlorographene (CCl), relax the chair conformation (alternating chlorine on both sides of the buckled graphene) in the hexagonal unit cell, then compute the LDA band gap and Γ‑point phonon frequencies to identify the Raman‑active modes. The key results are extracted from the raw DFT outputs and assembled into a single JSON artifact.

## Reproduction target
Produce a file `/app/outputs/reproduced_properties.json` with the following quantitative DFT properties:
- For single chlorine adsorption: binding energy (eV), migration barrier (meV), diffusion constant at 300 K (cm²/s), C–Cl bond length (Å), Bader charge transfer (e), magnetic moment (μB).
- For chlorographene: lattice constant (Å), C–C bond length (Å), C–Cl bond length (Å), buckling δ (Å), LDA band gap (eV), and four Raman‑active mode frequencies (cm⁻¹).
All calculations must be performed with Quantum ESPRESSO using LDA and PAW pseudopotentials; Bader analysis is required for charge transfer.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotential for C: https://www.quantum-espresso.org/pseudopotentials/
- PAW pseudopotential for Cl: https://www.quantum-espresso.org/pseudopotentials/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- Python 3 with numpy, scipy: numpy scipy
- Graphene crystal structure

## Workflow steps

### Step 1: DFT reference calculations
- Role: process
- Action: Compute ground-state total energies of a (4×4) graphene supercell, an isolated Cl atom, and a Cl₂ molecule using the local density approximation (LDA) with PAW pseudopotentials in Quantum ESPRESSO. Store optimized geometries and total energies for later binding energy formulas.
- Evidence: `/app/outputs/reference_energies.log`

### Step 2: Single Cl adsorption and migration barrier
- Role: process
- Action: Perform geometry optimization for a single Cl atom placed at the top site of a (4×4) graphene supercell. Scan the total energy along the T‑B‑H‑T symmetry path by constrained relaxations to obtain the minimum migration barrier. Compute Bader charges, magnetic moment, and structural parameters (C–Cl bond length, buckling). Save all relevant total energies and atomic configurations.
- Evidence: `/app/outputs/single_cl_results.log`

### Step 3: Chlorographene optimization and Raman‑active phonons
- Role: process
- Action: Relax the chair-conformation CCl structure (alternating Cl on both sides) in a hexagonal unit cell. Compute the LDA band gap and run a Γ‑point phonon calculation to obtain the Raman‑active mode frequencies. Save structural parameters and phonon frequencies.
- Evidence: `/app/outputs/ccl_results.log`

### Step 4: Compile reproduced DFT properties
- Role: scored (load-bearing)
- Action: From the outputs of steps 1–3, compute all required quantities and write them to '/app/outputs/reproduced_properties.json' according to the specified schema. Quantities to include: for single Cl adsorption – binding energy, migration barrier, diffusion constant at 300 K, C–Cl bond length, Bader charge transfer, magnetic moment; for chlorographene – lattice constant, C–C and C–Cl bond lengths, buckling, band gap, Raman‑active mode frequencies (four values).
- Output file: `/app/outputs/reproduced_properties.json`
- Format: json
- Contract: {
  "single_cl_adsorption": {
    "binding_energy_eV": float,
    "migration_barrier_meV": float,
    "diffusion_constant_300K_cm2s": float,
    "C_Cl_bond_length_A": float,
    "charge_transfer_e": float,
    "magnetic_moment_muB": float
  },
  "chlorographene": {
    "lattice_constant_a_A": float,
    "C_C_bond_length_A": float,
    "C_Cl_bond_length_A": float,
    "buckling_delta_A": float,
    "band_gap_eV": float,
    "Raman_active_frequencies_cm-1": [float, float, float, float]
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_properties.json
- path: `/app/outputs/reproduced_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Compiled key DFT properties for single Cl on graphene and chlorographene, including structural, electronic, vibrational, and magnetic quantities. The verifier compares each numeric field to hidden paper gold values within tolerances.
- schema:
  - `type`: object
  - `required`: `single_cl_adsorption`, `chlorographene`
  - `properties`:
    - `single_cl_adsorption`:
      - `type`: object
      - `required`: `binding_energy_eV`, `migration_barrier_meV`, `diffusion_constant_300K_cm2s`, `C_Cl_bond_length_A`, `charge_transfer_e`, `magnetic_moment_muB`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `migration_barrier_meV`:
          - `type`: number
        - `diffusion_constant_300K_cm2s`:
          - `type`: number
        - `C_Cl_bond_length_A`:
          - `type`: number
        - `charge_transfer_e`:
          - `type`: number
        - `magnetic_moment_muB`:
          - `type`: number
    - `chlorographene`:
      - `type`: object
      - `required`: `lattice_constant_a_A`, `C_C_bond_length_A`, `C_Cl_bond_length_A`, `buckling_delta_A`, `band_gap_eV`, `Raman_active_frequencies_cm-1`
      - `properties`:
        - `lattice_constant_a_A`:
          - `type`: number
        - `C_C_bond_length_A`:
          - `type`: number
        - `C_Cl_bond_length_A`:
          - `type`: number
        - `buckling_delta_A`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
        - `Raman_active_frequencies_cm-1`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4

Notes: All DFT runs must use LDA with PAW pseudopotentials; Bader analysis is required for charge transfer. Only the single Cl adsorption and chlorographene properties are scored; coverage‑dependent and strain‑response quantities are excluded per the approved reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "single_cl_adsorption",
          "chlorographene"
        ],
        "properties": {
          "single_cl_adsorption": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "migration_barrier_meV",
              "diffusion_constant_300K_cm2s",
              "C_Cl_bond_length_A",
              "charge_transfer_e",
              "magnetic_moment_muB"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "migration_barrier_meV": {
                "type": "number"
              },
              "diffusion_constant_300K_cm2s": {
                "type": "number"
              },
              "C_Cl_bond_length_A": {
                "type": "number"
              },
              "charge_transfer_e": {
                "type": "number"
              },
              "magnetic_moment_muB": {
                "type": "number"
              }
            }
          },
          "chlorographene": {
            "type": "object",
            "required": [
              "lattice_constant_a_A",
              "C_C_bond_length_A",
              "C_Cl_bond_length_A",
              "buckling_delta_A",
              "band_gap_eV",
              "Raman_active_frequencies_cm-1"
            ],
            "properties": {
              "lattice_constant_a_A": {
                "type": "number"
              },
              "C_C_bond_length_A": {
                "type": "number"
              },
              "C_Cl_bond_length_A": {
                "type": "number"
              },
              "buckling_delta_A": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              },
              "Raman_active_frequencies_cm-1": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4
              }
            }
          }
        }
      },
      "description": "Compiled key DFT properties for single Cl on graphene and chlorographene, including structural, electronic, vibrational, and magnetic quantities. The verifier compares each numeric field to hidden paper gold values within tolerances."
    }
  ],
  "notes": "All DFT runs must use LDA with PAW pseudopotentials; Bader analysis is required for charge transfer. Only the single Cl adsorption and chlorographene properties are scored; coverage‑dependent and strain‑response quantities are excluded per the approved reproduction target."
}
```

## How you are scored
A hidden verifier reads your `reproduced_properties.json`, validates its schema, and compares each numeric field against reference values using domain‑specific tolerances that account for legitimate code‑to‑code variation. Your final reward is the weighted average of per‑field scores; every stage of the workflow contributes, and simply reporting numbers without performing the DFT calculations is not sufficient.
