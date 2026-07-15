# 3D Nuclear Pasta Structure Simulation and Equation of State via RMF+Thomas-Fermi

## Problem background
In the inner crust of a neutron star, nuclear matter is expected to arrange itself into exotic non-uniform structures known as “nuclear pasta.” These structures—named droplet, rod, slab, tube, and bubble—arise from the competition between the nuclear surface tension and the long-range Coulomb repulsion among protons. Understanding their properties is essential for modelling neutron star cooling, crustal oscillations, and the interpretation of quasi-periodic oscillations observed in giant flares from magnetars. A key open question is which crystalline configuration (face-centered cubic fcc or body-centered cubic bcc) is energetically favoured for the droplet phase, especially near the transition to the rod phase, and how the equation of state and structural parameters (energy per baryon, pressure, droplet radii, lattice constants, volume fractions) depend on baryon density and proton fraction.

## Approach
The pasta structures are simulated using a relativistic mean-field (RMF) model under the Thomas–Fermi approximation. In this approach, nucleons are described as a Fermi gas moving in self-consistently generated meson mean fields (σ, ω, ρ) and the Coulomb potential. The model is solved on a three-dimensional periodic cubic grid without assuming any geometrical symmetry; several unit periods are accommodated in the simulation box, allowing the system to naturally adopt the energetically most favourable shape and lattice. The set of coupled field equations for the mesons and the Coulomb potential is solved for a given average baryon density and proton fraction, while the density distributions and chemical potentials of protons, neutrons, and electrons are iteratively adjusted until chemical equilibrium is reached everywhere. By comparing the total energies of candidate configurations (droplet fcc, droplet bcc, rod, slab, tube, bubble, uniform matter) the ground state is identified. The simulations are performed for three fixed proton fractions and for cold catalyzed matter in β-equilibrium, yielding converged density distributions, meson fields, Coulomb potentials, and total energies. From these raw simulation outputs, the equation of state (energy per baryon, total pressure, baryon partial pressure) and the ground-state pasta phase are extracted; for the droplet phase, the radius, lattice constant, and volume fraction are computed. For catalyzed matter, the fcc and bcc droplet lattices are explicitly compared to determine which is energetically preferred.

## Reproduction target
Produce two scored artifacts. For fixed proton fractions Y_p = 0.5, 0.3, and 0.1, simulate a range of average baryon densities covering the pasta phases and write results to results_fixed_Yp.json. Each entry must report: rho_B (fm⁻³), Y_p, energy_per_baryon (MeV), total_pressure (MeV fm⁻³), baryon_partial_pressure (MeV fm⁻³), pasta_phase (one of droplet, rod, slab, tube, bubble). For droplet phases also report droplet_radius (fm), lattice_constant (fm), and volume_fraction. For cold catalyzed matter (β-equilibrium), simulate the density range from well below saturation to the rod phase and write results to results_catalyzed.json. Each entry must report: rho_B, total_energy_per_baryon (MeV), Coulomb_energy_per_baryon (MeV), proton_number_fraction, pasta_phase (droplet or rod). For droplet densities, report both fcc and bcc lattice data: energy_fcc, energy_bcc (MeV), droplet_radius_fcc, droplet_radius_bcc (fm), lattice_constant_fcc, lattice_constant_bcc (fm), volume_fraction_fcc, volume_fraction_bcc, and lattice_type (the energetically favoured one). The structural parameters must be defined as in the RMF+Thomas-Fermi literature: lattice constant from cell volume and number of droplets, droplet radius from the second moment of the proton density, and volume fraction from the cube of their ratio.

## Assets

- RMF parameter set (coupling constants and meson masses)

## Workflow steps

### Step 1: Run 3D RMF+TF simulations
- Role: process
- Action: Implement and execute the full 3D relativistic mean-field (RMF) solver under the Thomas-Fermi approximation with periodic boundary conditions for all required baryon density / proton fraction combinations and candidate structures (droplet fcc, droplet bcc, rod, slab, tube, bubble, uniform). Use the parameter set (g_σN, g_ωN, g_ρN, b, c, m_σ, m_ω, m_ρ) that reproduces uniform nuclear matter properties. The solver must self-consistently solve the coupled field equations for the σ, ω, R meson fields and Coulomb potential, and iterate density distributions and chemical potentials until convergence. Produce converged density distributions, meson mean-fields, Coulomb potentials, and total energies for each configuration.
- Evidence: none

### Step 2: Produce results_fixed_Yp.json
- Role: scored (load-bearing)
- Action: From the simulation outputs, for each fixed proton-fraction case (Y_p = 0.5, 0.3, 0.1) and each density simulated, compute energy per baryon, total pressure, baryon partial pressure, and identify the pasta phase (droplet, rod, slab, tube, bubble). For droplet phases, additionally compute droplet radius, lattice constant, and volume fraction. Write the results to results_fixed_Yp.json.
- Output file: `/app/outputs/results_fixed_Yp.json`
- Format: json
- Contract: Array of objects; each object has keys: rho_B (number, units: fm^{-3}), Y_p (number), energy_per_baryon (number, units: MeV), total_pressure (number, units: MeV fm^{-3}), baryon_partial_pressure (number, units: MeV fm^{-3}), pasta_phase (string, one of: droplet, rod, slab, tube, bubble). For droplet phases only: droplet_radius (number, units: fm), lattice_constant (number, units: fm), volume_fraction (number).
- Scoring: scored by hidden verifier

### Step 3: Produce results_catalyzed.json
- Role: scored
- Action: For cold catalyzed (beta-equilibrium) matter over the density range simulated, compute total energy per baryon, Coulomb energy per baryon, proton number-fraction, and identify the pasta phase (droplet or rod). For droplet phases, report both fcc and bcc energies, radii, lattice constants, and volume fractions, and indicate which lattice is energetically favored. Write the results to results_catalyzed.json.
- Output file: `/app/outputs/results_catalyzed.json`
- Format: json
- Contract: Array of objects; each object has keys: rho_B (number, units: fm^{-3}), total_energy_per_baryon (number, units: MeV), Coulomb_energy_per_baryon (number, units: MeV), proton_number_fraction (number), pasta_phase (string: droplet or rod). For droplet phases: lattice_type (string: fcc or bcc), energy_fcc (number, units: MeV), energy_bcc (number, units: MeV), droplet_radius_fcc (number, units: fm), droplet_radius_bcc (number, units: fm), lattice_constant_fcc (number, units: fm), lattice_constant_bcc (number, units: fm), volume_fraction_fcc (number), volume_fraction_bcc (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_fixed_Yp.json`
- `/app/outputs/results_catalyzed.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_fixed_Yp.json
- path: `/app/outputs/results_fixed_Yp.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equation of state and structural parameters for fixed proton fractions Y_p = 0.5, 0.3, 0.1. The checker compares reported energies, pressures, phase labels, and droplet properties against hidden reference values from the paper within tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `rho_B`, `Y_p`, `energy_per_baryon`, `total_pressure`, `baryon_partial_pressure`, `pasta_phase`
    - `properties`:
      - `rho_B`:
        - `type`: number
        - `unit`: fm^{-3}
      - `Y_p`:
        - `type`: number
      - `energy_per_baryon`:
        - `type`: number
        - `unit`: MeV
      - `total_pressure`:
        - `type`: number
        - `unit`: MeV fm^{-3}
      - `baryon_partial_pressure`:
        - `type`: number
        - `unit`: MeV fm^{-3}
      - `pasta_phase`:
        - `type`: string
        - `enum`: `droplet`, `rod`, `slab`, `tube`, `bubble`
      - `droplet_radius`:
        - `type`: number
        - `unit`: fm
        - `optional`: True
      - `lattice_constant`:
        - `type`: number
        - `unit`: fm
        - `optional`: True
      - `volume_fraction`:
        - `type`: number
        - `optional`: True

### results_catalyzed.json
- path: `/app/outputs/results_catalyzed.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equation of state, droplet properties, and lattice preference for cold catalyzed matter (beta-equilibrium). The checker compares reported values against hidden references and verifies that the reported lattice type is self-consistent and physically plausible.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `rho_B`, `total_energy_per_baryon`, `Coulomb_energy_per_baryon`, `proton_number_fraction`, `pasta_phase`
    - `properties`:
      - `rho_B`:
        - `type`: number
        - `unit`: fm^{-3}
      - `total_energy_per_baryon`:
        - `type`: number
        - `unit`: MeV
      - `Coulomb_energy_per_baryon`:
        - `type`: number
        - `unit`: MeV
      - `proton_number_fraction`:
        - `type`: number
      - `pasta_phase`:
        - `type`: string
        - `enum`: `droplet`, `rod`
      - `lattice_type`:
        - `type`: string
        - `enum`: `fcc`, `bcc`
        - `optional`: True
      - `energy_fcc`:
        - `type`: number
        - `unit`: MeV
        - `optional`: True
      - `energy_bcc`:
        - `type`: number
        - `unit`: MeV
        - `optional`: True
      - `droplet_radius_fcc`:
        - `type`: number
        - `unit`: fm
        - `optional`: True
      - `droplet_radius_bcc`:
        - `type`: number
        - `unit`: fm
        - `optional`: True
      - `lattice_constant_fcc`:
        - `type`: number
        - `unit`: fm
        - `optional`: True
      - `lattice_constant_bcc`:
        - `type`: number
        - `unit`: fm
        - `optional`: True
      - `volume_fraction_fcc`:
        - `type`: number
        - `optional`: True
      - `volume_fraction_bcc`:
        - `type`: number
        - `optional`: True

Notes: The checker uses hidden reference values extracted from the paper's tables and figures. For fixed Y_p, checks include energy per baryon within relative tolerance and pasta phase matching. For catalyzed matter, it additionally verifies lattice preference ordering and consistency of volume fractions. Tolerances and exact comparison rules are defined in the hidden grading spec.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_fixed_Yp.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "rho_B",
            "Y_p",
            "energy_per_baryon",
            "total_pressure",
            "baryon_partial_pressure",
            "pasta_phase"
          ],
          "properties": {
            "rho_B": {
              "type": "number",
              "unit": "fm^{-3}"
            },
            "Y_p": {
              "type": "number"
            },
            "energy_per_baryon": {
              "type": "number",
              "unit": "MeV"
            },
            "total_pressure": {
              "type": "number",
              "unit": "MeV fm^{-3}"
            },
            "baryon_partial_pressure": {
              "type": "number",
              "unit": "MeV fm^{-3}"
            },
            "pasta_phase": {
              "type": "string",
              "enum": [
                "droplet",
                "rod",
                "slab",
                "tube",
                "bubble"
              ]
            },
            "droplet_radius": {
              "type": "number",
              "unit": "fm",
              "optional": true
            },
            "lattice_constant": {
              "type": "number",
              "unit": "fm",
              "optional": true
            },
            "volume_fraction": {
              "type": "number",
              "optional": true
            }
          }
        }
      },
      "description": "Equation of state and structural parameters for fixed proton fractions Y_p = 0.5, 0.3, 0.1. The checker compares reported energies, pressures, phase labels, and droplet properties against hidden reference values from the paper within tolerances."
    },
    {
      "file": "results_catalyzed.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "rho_B",
            "total_energy_per_baryon",
            "Coulomb_energy_per_baryon",
            "proton_number_fraction",
            "pasta_phase"
          ],
          "properties": {
            "rho_B": {
              "type": "number",
              "unit": "fm^{-3}"
            },
            "total_energy_per_baryon": {
              "type": "number",
              "unit": "MeV"
            },
            "Coulomb_energy_per_baryon": {
              "type": "number",
              "unit": "MeV"
            },
            "proton_number_fraction": {
              "type": "number"
            },
            "pasta_phase": {
              "type": "string",
              "enum": [
                "droplet",
                "rod"
              ]
            },
            "lattice_type": {
              "type": "string",
              "enum": [
                "fcc",
                "bcc"
              ],
              "optional": true
            },
            "energy_fcc": {
              "type": "number",
              "unit": "MeV",
              "optional": true
            },
            "energy_bcc": {
              "type": "number",
              "unit": "MeV",
              "optional": true
            },
            "droplet_radius_fcc": {
              "type": "number",
              "unit": "fm",
              "optional": true
            },
            "droplet_radius_bcc": {
              "type": "number",
              "unit": "fm",
              "optional": true
            },
            "lattice_constant_fcc": {
              "type": "number",
              "unit": "fm",
              "optional": true
            },
            "lattice_constant_bcc": {
              "type": "number",
              "unit": "fm",
              "optional": true
            },
            "volume_fraction_fcc": {
              "type": "number",
              "optional": true
            },
            "volume_fraction_bcc": {
              "type": "number",
              "optional": true
            }
          }
        }
      },
      "description": "Equation of state, droplet properties, and lattice preference for cold catalyzed matter (beta-equilibrium). The checker compares reported values against hidden references and verifies that the reported lattice type is self-consistent and physically plausible."
    }
  ],
  "notes": "The checker uses hidden reference values extracted from the paper's tables and figures. For fixed Y_p, checks include energy per baryon within relative tolerance and pasta phase matching. For catalyzed matter, it additionally verifies lattice preference ordering and consistency of volume fractions. Tolerances and exact comparison rules are defined in the hidden grading spec."
}
```

## How you are scored
Each of the two output files is scored independently by a hidden verifier. The verifier reads the JSON artifacts and compares the reported quantities against hidden reference values derived from the original study. For results_fixed_Yp.json, it checks that the energy per baryon values and the pasta phase labels agree with the expected ground-state assignment across the simulated density range. For results_catalyzed.json, it additionally checks the Coulomb energy, the proton number fraction, and that the reported lattice type and energy ordering are self-consistent and physically plausible. Droplet radii, lattice constants, and volume fractions are verified against expected values and internally audited for consistency. The scoring uses tolerances that account for legitimate differences arising from reimplementation (different numerical grids, solver convergence, or compiler optimizations). The per-artifact scores are combined by weight to produce the final reward; the two scored outputs carry the majority of the weight. Simply reporting a number that matches the hidden reference without actually running the simulation is insufficient; the verifier may cross-check internal relations that only a correct physical simulation can satisfy.
