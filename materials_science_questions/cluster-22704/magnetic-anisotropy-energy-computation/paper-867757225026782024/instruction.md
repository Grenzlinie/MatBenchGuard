# Finite-Lattice Spin Model Magnetization via Exact Enumeration

## Problem background
Superatom-fullerene assemblies, where magnetic clusters are separated by non-magnetic spacer molecules (e.g., C60), exhibit collective magnetic behavior, including a low-temperature ferromagnetic phase. Understanding how interactions such as isotropic Heisenberg exchange, magnetocrystalline anisotropy, and Dzyaloshinskii-Moriya interaction (DMI) give rise to the observed magnetization vs. temperature response is key to designing magnetic solids with desired properties. This task investigates the magnetization of a finite-lattice model Hamiltonian that includes these interaction terms, exploring the conditions required to qualitatively reproduce experimentally observed magnetization trends.

## Approach
The system is modelled as a planar square array of 8 magnetic clusters, each treated as a classical spin with 5 discrete orientations. The model Hamiltonian incorporates isotropic Heisenberg exchange couplings between first (90°) and second (180°) nearest neighbours, a single-site magnetocrystalline anisotropy term that penalizes spin deviation from an easy axis, the Zeeman energy of each cluster’s magnetic moment in an applied external field, and an anisotropic Dzyaloshinskii-Moriya interaction on the 90° surface bonds. The total energy of each of the 5^8 possible spin configurations is computed by summing these contributions. Thermal averages are obtained by exact enumeration and Boltzmann weighting, yielding the equilibrium magnetization along the field direction as a function of temperature and applied field. The magnetization is normalized by the saturation value (number of clusters × moment per cluster). The task is to implement this Hamiltonian with a specific parameter set and compute the normalized magnetization curves for specified temperature and field ranges.

## Reproduction target
Compute the normalized magnetization (M/M_sat) of an 8-cluster square-planar array of magnetic superatoms, using the model Hamiltonian described in the Approach. Use the following fixed parameters: Heisenberg exchange J11 = 0.9×10⁻²³ J, with the ratio J11/J12 = -1.96 (i.e., nearest-neighbour coupling is antiferromagnetic); single-cluster magnetocrystalline anisotropy energy E_MAE = 3.04×10⁻²⁶ J per cluster; magnetic moment per cluster M = 5.4 μ_B; Dzyaloshinskii-Moriya interaction strength D12 = 1.5×10⁻²³ J on 90° surface bonds, with zero DMI on 180° bonds. Evaluate the magnetization for temperatures from 2 K to 30 K inclusive in steps of 1 K, and for applied magnetic fields of 200 Oe, 500 Oe, and 1000 Oe. All 5^8 spin configurations must be enumerated exactly; no Monte Carlo sampling is permitted. The magnetization along the field direction, averaged over the Boltzmann distribution, must be normalized by the saturation magnetization (8 × 5.4 μ_B). Write the result as a CSV file with columns: Temperature_K, Field_Oe, Normalized_Magnetization.

## Assets

- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Compute magnetization curves via exact enumeration
- Role: scored (load-bearing)
- Action: Implement the finite-assembly model Hamiltonian for an 8-cluster square-planar array with nearest- and second-nearest-neighbor interactions. For each of the 5 discrete spin orientations, enumerate all 5⁸ configurations exactly. For each configuration, compute the total energy as the sum of: isotropic Heisenberg exchange (J₁₁ for 180° bonds, J₁₂ for 90° bonds, with J₁₂ negative and the magnitude ratio |J₁₁/J₁₂|=1.96), single-cluster magnetocrystalline anisotropy (penalty E_MAE=3.04×10⁻²⁶ J when a cluster’s moment deviates from its easy axis), Zeeman energy (interaction of a cluster’s moment M=5.4 μ_B with the external field H at 200, 500, 1000 Oe), and Dzyaloshinskii–Moriya interaction on surface 90° bonds (D₁₂=1.5×10⁻²³ J, zero on 180° bonds). Using Boltzmann weighting, compute the thermal-average magnetization along the field direction for each temperature from 2 K to 30 K (step 1 K) and each field, normalized by the saturation magnetization (8×5.4 μ_B). Write the result as a CSV file.
- Output file: `/app/outputs/magnetization_curves.csv`
- Format: csv
- Contract: Temperature_K (float), Field_Oe (integer, one of 200,500,1000), Normalized_Magnetization (float between 0 and 1 inclusive)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curves.csv
- path: `/app/outputs/magnetization_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized magnetization (M/M_sat) as a function of temperature (2–30 K in 1 K steps) and applied magnetic field (200, 500, 1000 Oe) for an 8-cluster square-planar array with antiferromagnetic J₁₂ and DMI, computed via exact enumeration of 5⁸ spin configurations.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Field_Oe`, `Normalized_Magnetization`
  - `units`:
    - `Temperature_K`: K
    - `Field_Oe`: Oe
    - `Normalized_Magnetization`: dimensionless (0–1)

Notes: The checker independently recomputes the magnetization for the same model parameters and exact enumeration, then compares the submitted points within a hidden tolerance. The output must contain exactly one row for each (Temperature, Field) combination in the described ranges.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Field_Oe",
          "Normalized_Magnetization"
        ],
        "units": {
          "Temperature_K": "K",
          "Field_Oe": "Oe",
          "Normalized_Magnetization": "dimensionless (0–1)"
        }
      },
      "description": "Normalized magnetization (M/M_sat) as a function of temperature (2–30 K in 1 K steps) and applied magnetic field (200, 500, 1000 Oe) for an 8-cluster square-planar array with antiferromagnetic J₁₂ and DMI, computed via exact enumeration of 5⁸ spin configurations."
    }
  ],
  "notes": "The checker independently recomputes the magnetization for the same model parameters and exact enumeration, then compares the submitted points within a hidden tolerance. The output must contain exactly one row for each (Temperature, Field) combination in the described ranges."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. The verifier independently recomputes the normalized magnetization for the same model and parameter set, using its own implementation of exact enumeration. It compares your submitted Normalized_Magnetization values at all reported temperature points for each field to its own computed values. The reward is based on the fraction of points that agree within a hidden tolerance; full credit requires a sufficiently high fraction of points to be correct. Reporting a table of expected numbers without having performed the correct computation will not satisfy the verifier. Each output file in the workflow is scored separately, and the final reward is a weighted combination of these individual scores.
