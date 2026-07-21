## Problem background

Thermoelectric materials directly convert waste heat into electricity, and their performance is measured by the dimensionless figure of merit ZT. Calcium chalcogenide monolayers, particularly hexagonal CaS and CaSe, have shown promising ZT values but their performance varies strongly with temperature. This task investigates whether a bilayer heterostructure formed by stacking CaS and CaSe (the hybrid CaS/CaSe bilayer) can deliver a stable, high ZT over a wide temperature range (50–1200 K) compared to the constituent pure monolayers and the pure CaS bilayer. Using density functional theory (DFT) and semi-classical Boltzmann transport theory, you will compute the structural stability, electronic properties, and temperature-dependent thermoelectric transport coefficients of these four systems.

## Approach

The computational workflow proceeds in several stages using open-source codes. All steps are based on standard DFT and transport methods; no external datasets or pre-trained models are required.

1. **Initial structures:** Construct hexagonal unit cells for monolayer CaS, monolayer CaSe, bilayer CaS (CaS/CaS), and the hybrid CaS/CaSe bilayer with AB stacking, using known monolayer lattice parameters from prior work (CaS ~4.56 Å, CaSe ~4.78 Å).
2. **DFT geometry optimization:** Relax atomic positions and cell parameters for all four structures using the PBE exchange-correlation functional and Grimme's D2 van der Waals correction as implemented in Quantum ESPRESSO.
3. **Phonon dispersion and stability:** Compute phonon frequencies along high-symmetry k-paths for the three bilayer/heterostructure systems using density functional perturbation theory. Identify systems with imaginary frequencies as dynamically unstable; they are excluded from further transport analysis.
4. **Electronic structure:** For all dynamically stable systems (including the monolayers), compute the Kohn-Sham band structure and projected density of states, and extract the indirect band gap.
5. **Thermoelectric transport:** Use the band structures and cell volumes as input to the BoltzTraP code under the constant scattering time approximation (CSTA) and rigid band approximation (RBA) to calculate the temperature-dependent transport coefficients: electrical conductivity over relaxation time (σ/τ), thermal conductivity over relaxation time (κ/τ), Seebeck coefficient (S), and the dimensionless figure of merit ZT. The temperature range is 50 K to 1200 K in steps of 50 K.

The final outputs are a structured summary of the optimized structural/electronic properties and a CSV of the transport coefficients for all stable systems.

## Reproduction target

Produce two artifacts:
- A JSON file (`optimization_results.json`) containing the relaxed lattice constant, band gap, and dynamical stability flag for each system.
- A CSV file (`transport_properties.csv`) containing the temperature-series thermoelectric transport coefficients (σ/τ, κ/τ, Seebeck coefficient S, and ZT) for every dynamically stable system.

The verifier will independently check that the transport data are internally consistent by recomputing ZT from the provided σ/τ, κ/τ, S, and temperature, and will verify that the lattice constants, band gaps, and stability flags are plausible for these material systems.

## Assets

- **Quantum ESPRESSO** – open-source plane-wave DFT package, available at https://www.quantum-espresso.org/
- **BoltzTraP** – code for calculating band-structure-dependent transport quantities, available at https://www.boltzit.eu/ or https://github.com/wisetr/BoltzTraP2

No other external data, models, or weights are required. The solver must construct the initial geometries from the reported monolayer lattice parameters.

## Workflow steps

### Step 1: Structure setup and geometry optimization
- Role: process
- Action: Construct initial hexagonal unit cells for monolayer CaS, monolayer CaSe, bilayer CaS (CaS/CaS), and hybrid CaS/CaSe bilayer with AB stacking. Relax the atomic positions and cell parameters using Quantum ESPRESSO with PBE functional and DFT-D2 dispersion correction.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Phonon dispersion and stability analysis
- Role: process
- Action: Using the optimized structures from Step 1, compute phonon dispersion curves for the CaS/CaS bilayer, CaSe/CaSe bilayer, and CaS/CaSe hybrid bilayer along high-symmetry k-paths (density functional perturbation theory). Determine which systems show no imaginary acoustic modes (i.e., are dynamically stable).
- Evidence: `/app/outputs/phonon_results.log`

### Step 3: Electronic band structure and band gaps
- Role: process
- Action: For all dynamically stable systems (CaS monolayer, CaSe monolayer, CaS bilayer, and CaS/CaSe hybrid bilayer if stable), compute the Kohn-Sham band structure and projected density of states. Record the indirect band gap of each system.
- Evidence: `/app/outputs/electronic_structure.log`

### Step 4: Compile structural and electronic results
- Role: scored
- Action: Assemble the lattice constant, band gap, and dynamical stability flag for each of the four systems from the preceding steps into a single JSON file.
- Output file: `/app/outputs/optimization_results.json`
- Format: json
- Contract: A JSON object with keys `CaS_monolayer`, `CaSe_monolayer`, `CaS_bilayer`, `CaS_CaSe_hybrid`. Each value is an object containing:
  - `lattice_constant_angstrom` (float, the optimized in-plane lattice parameter)
  - `band_gap_eV` (float or `null` if the system is unstable)
  - `dynamically_stable` (bool)
- Scoring: scored by hidden verifier

### Step 5: Thermoelectric transport calculation (load-bearing)
- Role: scored (load-bearing)
- Action: Run BoltzTraP under the constant scattering time and rigid band approximations, using the DFT band structures and unit-cell volumes from the stable systems. Compute σ/τ, κ/τ, Seebeck coefficient S, and figure of merit ZT for temperatures from 50 K to 1200 K in steps of 50 K. Include all stable systems: CaS monolayer, CaSe monolayer, CaS bilayer, and CaS/CaSe hybrid bilayer.
- Output file: `/app/outputs/transport_properties.csv`
- Format: csv
- Contract: A CSV with columns:
  - `System` (string: one of `CaS_monolayer`, `CaSe_monolayer`, `CaS_bilayer`, `CaS_CaSe_hybrid`)
  - `Temperature_K` (integer)
  - `sigma_over_tau` (float, in units consistent with SI, per relaxation time τ)
  - `kappa_over_tau` (float, in units consistent with SI, per relaxation time τ)
  - `Seebeck_V_per_K` (float, Seebeck coefficient in V/K)
  - `ZT` (float, dimensionless figure of merit)
- Scoring: scored by hidden verifier (the verifier will recompute ZT internally and compare transport properties to expected reference behaviour)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimization_results.json
- path: `/app/outputs/optimization_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants, indirect band gaps, and dynamical stability flags for the four calcium chalcogenide systems.
- schema:
  - `type`: object
  - `required`:
    - `CaS_monolayer`:
      - `lattice_constant_angstrom`: float
      - `band_gap_eV`: float|null
      - `dynamically_stable`: bool
    - `CaSe_monolayer`:
      - `lattice_constant_angstrom`: float
      - `band_gap_eV`: float|null
      - `dynamically_stable`: bool
    - `CaS_bilayer`:
      - `lattice_constant_angstrom`: float
      - `band_gap_eV`: float|null
      - `dynamically_stable`: bool
    - `CaS_CaSe_hybrid`:
      - `lattice_constant_angstrom`: float
      - `band_gap_eV`: float|null
      - `dynamically_stable`: bool

### transport_properties.csv
- path: `/app/outputs/transport_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent thermoelectric transport coefficients (electrical conductivity, thermal conductivity, Seebeck coefficient, figure of merit) for all dynamically stable calcium chalcogenide systems, covering 50–1200 K in steps of 50 K.
- schema:
  - `type`: table
  - `required_columns`: `System`, `Temperature_K`, `sigma_over_tau`, `kappa_over_tau`, `Seebeck_V_per_K`, `ZT`
  - `units`:
    - `Seebeck_V_per_K`: V/K
    - `sigma_over_tau`: S/m per relaxation time
    - `kappa_over_tau`: W/(m·K) per relaxation time

Notes: The verifier recomputes ZT from the submitted columns and compares lattice constants/band gaps to reference values for these material systems. No hidden labels or external dataset are used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimization_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CaS_monolayer": {
            "lattice_constant_angstrom": "float",
            "band_gap_eV": "float|null",
            "dynamically_stable": "bool"
          },
          "CaSe_monolayer": {
            "lattice_constant_angstrom": "float",
            "band_gap_eV": "float|null",
            "dynamically_stable": "bool"
          },
          "CaS_bilayer": {
            "lattice_constant_angstrom": "float",
            "band_gap_eV": "float|null",
            "dynamically_stable": "bool"
          },
          "CaS_CaSe_hybrid": {
            "lattice_constant_angstrom": "float",
            "band_gap_eV": "float|null",
            "dynamically_stable": "bool"
          }
        }
      },
      "description": "Optimized lattice constants, indirect band gaps, and dynamical stability flags for the four calcium chalcogenide systems."
    },
    {
      "file": "transport_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "Temperature_K",
          "sigma_over_tau",
          "kappa_over_tau",
          "Seebeck_V_per_K",
          "ZT"
        ],
        "units": {
          "Seebeck_V_per_K": "V/K",
          "sigma_over_tau": "S/m per relaxation time",
          "kappa_over_tau": "W/(m·K) per relaxation time"
        }
      },
      "description": "Temperature-dependent thermoelectric transport coefficients (electrical conductivity, thermal conductivity, Seebeck coefficient, figure of merit) for all dynamically stable calcium chalcogenide systems, covering 50–1200 K in steps of 50 K."
    }
  ],
  "notes": "The verifier recomputes ZT from the submitted columns and compares lattice constants/band gaps to reference values for these material systems. No hidden labels or external dataset are used."
}
```

## How you are scored

A hidden verifier runs after your submission. It independently reads each output file listed above, recomputes relevant properties (e.g., ZT from the supplied σ/τ, κ/τ, S, and T), and compares the results to reference expectations for these material systems. Each output file contributes a weighted share to your total reward. Merely reporting plausible numbers is not enough; the verifier checks for internal consistency and agreement with the known physics of these systems. Process steps are mandatory but not individually scored; however, the load-bearing transport step cannot be correctly produced without genuinely executing them.

## Self-check

(script auto-appended by builder)
