# First-principles Seebeck coefficient of layered black phosphorus

## Problem background
Black phosphorus (BP) is a layered semiconductor with a direct band gap of ~0.3 eV and strong in-plane anisotropy. Its thermoelectric properties, particularly the Seebeck coefficient, are predicted to be highly sensitive to both the carrier density and the number of layers, making it a candidate for high-performance thermoelectrics. However, direct experimental control of carrier density over a wide range is difficult, and first-principles electronic-structure calculations can provide a complete picture of the Seebeck coefficient as a function of carrier density for bulk and few-layer BP. This task reproduces those theoretical calculations: using density functional theory and Boltzmann transport theory, you will compute the Seebeck coefficient components for bulk, monolayer, bilayer, and five-layer BP at 210 K.

## Approach
The core idea is to combine first-principles electronic structure with semiclassical Boltzmann transport. First, the electronic band structures of bulk, monolayer, bilayer, and five-layer BP are obtained from density functional theory (DFT) calculations using the generalized gradient approximation (GGA-PBE) and an ultrasoft pseudopotential for phosphorus, as implemented in Quantum ESPRESSO. For the thin-layer systems, a vacuum layer is added to prevent spurious interactions between periodic images. The crystal structures are relaxed, and then self-consistent field and non-self-consistent band structure calculations are performed on a dense k-mesh. To correct the known underestimation of the band gap by PBE, a rigid shift of +0.2 eV is applied to the conduction band energies. The resulting band energies serve as input to BoltzTraP2, which solves the linearized Boltzmann transport equation in the constant relaxation time approximation at T = 210 K to compute the Seebeck coefficient tensor components S_x and S_y as functions of the volumetric carrier density. No fitting parameters are introduced; the output is a direct prediction of the material's intrinsic thermoelectric response.

## Reproduction target
Produce the in-plane Seebeck coefficient components S_x and S_y (in μV/K) for bulk, five-layer, bilayer, and monolayer black phosphorus as a function of volumetric carrier density at T = 210 K. You must include exactly these carrier density values (in cm^{-3}): 1e17, 2e17, 5e17, 1e18, 2e18, 5e18, 1e19, 2e19, 5e19, 1e20, 2e20, 5e20, 1e21. The verifier will check for the presence of these exact densities; missing any will cause the submission to be invalid. Save the results as a CSV file named seebeck_vs_carrier_density.csv with exactly four columns: layer (string: 'bulk', '5L', '2L', or '1L'), carrier_density (float, unit cm^{-3}), S_x (float, unit μV/K), and S_y (float, unit μV/K).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP2: BoltzTraP2
- PBE ultrasoft pseudopotential for phosphorus: https://www.materialscloud.org/discover/sssp/table/tool
- Black phosphorus crystal structure (bulk)

## Workflow steps

### Step 1: DFT electronic structure calculation
- Role: process
- Action: Perform DFT electronic structure calculations for bulk, monolayer, bilayer, and five-layer black phosphorus using Quantum ESPRESSO with GGA-PBE exchange-correlation functional. For slab systems, include a vacuum layer. Relax crystal structures, then run self-consistent field and non-self-consistent band structure calculations. Apply a +0.2 eV rigid shift to conduction band energies to match the experimental band gap. Produce band energies on a dense k-mesh suitable for BoltzTraP2.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Boltzmann transport calculation of Seebeck coefficient
- Role: scored (load-bearing)
- Action: Using the band structures from the previous step, run BoltzTraP2 at T=210 K under constant relaxation time approximation to compute S_x and S_y for each system (bulk, 5L, 2L, 1L) at exactly the following carrier densities (cm^{-3}): 1e17, 2e17, 5e17, 1e18, 2e18, 5e18, 1e19, 2e19, 5e19, 1e20, 2e20, 5e20, 1e21. Output results to seebeck_vs_carrier_density.csv.
- Output file: `/app/outputs/seebeck_vs_carrier_density.csv`
- Format: csv
- Contract: CSV columns: layer (string: 'bulk', '5L', '2L', '1L'), carrier_density (float, cm^{-3}), S_x (float, μV/K), S_y (float, μV/K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/seebeck_vs_carrier_density.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### seebeck_vs_carrier_density.csv
- path: `/app/outputs/seebeck_vs_carrier_density.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed Seebeck coefficient components as a function of volumetric carrier density for bulk and few-layer black phosphorus at T=210 K. Must include rows for each of the following carrier density values (cm^{-3}): 1e17, 2e17, 5e17, 1e18, 2e18, 5e18, 1e19, 2e19, 5e19, 1e20, 2e20, 5e20, 1e21, for each layer system (bulk, 5L, 2L, 1L).
- schema:
  - `type`: table
  - `required_columns`: `layer`, `carrier_density`, `S_x`, `S_y`
  - `units`:
    - `carrier_density`: cm^{-3}
    - `S_x`: μV/K
    - `S_y`: μV/K

Notes: The artifact is scored by comparing the agent's computed S_x and S_y values at selected carrier densities against the paper's theoretical reference curves.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "seebeck_vs_carrier_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "carrier_density",
          "S_x",
          "S_y"
        ],
        "units": {
          "carrier_density": "cm^{-3}",
          "S_x": "μV/K",
          "S_y": "μV/K"
        }
      },
      "description": "Computed Seebeck coefficient components as a function of volumetric carrier density for bulk and few-layer black phosphorus at T=210 K. Must include rows for each of the following carrier density values (cm^{-3}): 1e17, 2e17, 5e17, 1e18, 2e18, 5e18, 1e19, 2e19, 5e19, 1e20, 2e20, 5e20, 1e21, for each layer system (bulk, 5L, 2L, 1L)."
    }
  ],
  "notes": "The artifact is scored by comparing the agent's computed S_x and S_y values at selected carrier densities against the paper's theoretical reference curves."
}
```

## How you are scored
A hidden verifier will evaluate your submission automatically. It reads the file seebeck_vs_carrier_density.csv, extracts the S_x and S_y values at a preselected set of carrier densities for each layer system, and compares them against reference values that satisfy the underlying physics (the reference is a gold standard obtained from the same computational approach). The comparison uses a relative error metric; the reward is weighted toward the bulk and monolayer results, in line with their scientific importance. The verifier scores each scored step and combines the per-step rewards into a final overall reward between 0.0 (no agreement) and 1.0 (perfect or better agreement). Simply reporting a number without running the actual DFT+Boltzmann transport pipeline will not pass, because the hidden test densities and the tight tolerance are attainable only by a correct computational reproduction.
