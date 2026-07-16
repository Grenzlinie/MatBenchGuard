# Size-dependent Debye temperature of nanocrystals from analytical model

## Problem background
Nanocrystals exhibit size-dependent thermal properties such as the Debye temperature, Einstein temperature, and volume thermal expansion coefficient. Understanding how these quantities change with particle size, dimensionality, and the nature of the interface (free surface versus embedded in a matrix) is important for predicting material behavior at the nanoscale. A theoretical framework connects these properties to the root-mean-square (rms) displacement of atoms, using Lindemann's melting criterion and Mott's equation to relate the size-dependent changes to fundamental bulk material parameters. The task is to compute the ratios of these properties relative to their bulk values for a range of materials and conditions, using a specified analytical model.

## Approach
Implement the size-dependent model described below. The core idea is that the rms displacement of surface atoms differs from that of interior atoms, leading to a size-dependent scaling of the Debye temperature and related quantities.

**rms displacement scaling**  
For a nanocrystal of characteristic size D (diameter or thickness), the rms displacement ratio is  
σ(D)/σ(∞) = √[ exp( (α−1) / (D/D₀ − 1) ) ]  
where α = σₛ²(D)/σᵥ²(D) is the surface-to-interior rms ratio.

**Geometric cutoff size D₀**  
D₀ is the size at which all atoms are on the surface, given by  
D₀ = 2 (3 − d) h  
with d = 0 (nanoparticle), 1 (nanowire), 2 (thin film), and h the atomic diameter.

**Parameter α for free surfaces**  
For free-standing nanocrystals (or those on inert substrates), surface atoms have larger rms displacement, so α > 1. It is obtained from the vibrational part of the bulk melting entropy ΔSᵥᵢᵦ(∞):  
α = 2 ΔSᵥᵢᵦ(∞) / (3R) + 1  
where R = 8.314 J mol⁻¹ K⁻¹.

**Parameter α for embedded nanocrystals**  
For nanocrystals embedded in a matrix with coherent/semi-coherent interfaces, the interface suppresses atomic motion, giving α < 1. It is computed from matrix properties:  
α = [ (h_M / h)² × (Tₘ(∞) / Tₘ₍(∞)) + 1 ] / 2  
where h_M is the atomic diameter of the matrix and Tₘ₍(∞) is the bulk melting temperature of the matrix.

**Size-dependent property ratios**  
The Debye temperature ratio, Einstein temperature ratio, and volume thermal expansion coefficient ratio follow from the rms scaling:  
Θ_D(D)/Θ_D(∞) = Θ_E(D)/Θ_E(∞) = √[ exp( −(α−1) / (D/D₀ − 1) ) ]  
α_v(D)/α_v(∞) = exp( (α−1) / (D/D₀ − 1) )

**Implementation**  
For each test case (material, dimensionality d, size D in nm, interface type), compute D₀ from the material's atomic diameter h, compute α using the appropriate formula with provided bulk parameters, then evaluate the three ratios. Output the results as specified.

## Reproduction target
For the test cases listed below, compute the three dimensionless ratios: Θ_D(D)/Θ_D(∞), Θ_E(D)/Θ_E(∞), and α_v(D)/α_v(∞).  
Write the results to a CSV file as described in the Workflow steps.

**Required test cases**  
For each combination of material, dimension, size, and interface type in the table below, compute the ratios.

| material | dimension | size_nm | interface_type |
|----------|-----------|---------|----------------|
| Fe       | 0         | 5       | free           |
| Fe       | 0         | 10      | free           |
| Fe       | 0         | 20      | free           |
| Fe       | 0         | 50      | free           |
| β-Sn     | 0         | 10      | free           |
| β-Sn     | 0         | 20      | free           |
| β-Sn     | 0         | 50      | free           |
| Se       | 0         | 10      | free           |
| Se       | 0         | 20      | free           |
| Se       | 0         | 50      | free           |
| Cu       | 0         | 10      | free           |
| Cu       | 0         | 20      | free           |
| Cu       | 0         | 50      | free           |
| Co       | 0         | 10      | free           |
| Co       | 0         | 20      | free           |
| Co       | 0         | 50      | free           |
| Au       | 0         | 10      | free           |
| Au       | 0         | 20      | free           |
| Au       | 0         | 50      | free           |
| Pb       | 0         | 10      | free           |
| Pb       | 0         | 20      | free           |
| Pb       | 0         | 50      | free           |
| Ar       | 0         | 5       | embedded       |
| Ar       | 0         | 10      | embedded       |
| Ar       | 0         | 20      | embedded       |
| Ar       | 0         | 50      | embedded       |

Additionally, for materials Fe and Cu, also evaluate dimension=1 (nanowire) for sizes 10, 20, 50 nm with interface_type 'free', and dimension=2 (thin film) for sizes 10, 20, 50 nm with interface_type 'free'.

**Material parameters**  
The following bulk material parameters are provided. For embedded cases, use the matrix parameters specified separately.

| material | h (nm) | Tₘ(∞) (K) | ΔSᵥᵢᵦ(∞) (J mol⁻¹ K⁻¹) |
|----------|--------|-----------|--------------------------|
| Fe       | 0.2482 | 1811.00   | 6.42                     |
| β-Sn     | 0.3181 | 505.08    | 9.25                     |
| Se       | 0.4366 | 494.00    | 10.93                    |
| Cu       | 0.2556 | 1357.77   | 8.08                     |
| Co       | 0.2507 | 1768.00   | 7.83                     |
| Au       | 0.2884 | 1337.33   | 7.74                     |
| Pb       | 0.3500 | 600.61    | 6.71                     |
| Ar       | 0.3650 |  83.80    | (not used for embedded)  |

For the embedded interface (Ar in Al matrix):  
- Matrix atomic diameter h_M = 0.2863 nm  
- Matrix bulk melting temperature Tₘ₍(∞) = 933.47 K  
Use the Ar atomic diameter from the table above to compute α for embedded Ar.

*Note*: R = 8.314 J mol⁻¹ K⁻¹.

## Assets
No external datasets, models, or specific software packages are required beyond a Python environment with standard numerical libraries (e.g., numpy, pandas). All necessary material parameters and test case definitions are provided above. The source paper is not required and should not be retrieved.

## Workflow steps

### Step 1: Compute size-dependent property ratios
- Role: scored
- Action: Implement the size-dependent Debye temperature model (based on rms scaling, geometric cutoff D_0, thermodynamic α parameter for free and embedded interfaces, and the mappings to Debye, Einstein, and thermal expansion ratios) using the provided bulk material parameters from the paper's Table 1. For each required test case (specific material, dimension d, particle size D, interface type) compute the three ratios: Θ_D(D)/Θ_D(∞), Θ_E(D)/Θ_E(∞), and α_v(D)/α_v(∞), and write the results to CSV.
- Output file: `/app/outputs/predicted_ratios.csv`
- Format: csv
- Contract: Columns: material (str), dimension (int, 0=nanoparticle, 1=nanowire, 2=thin film), size_nm (float, diameter or thickness in nm), interface_type (str, 'free' or 'embedded'), ThetaD_ratio (float), ThetaE_ratio (float), alphav_ratio (float). One row per (material, size, interface) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_ratios.csv
- path: `/app/outputs/predicted_ratios.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV with computed size-dependent ratios for Debye temperature, Einstein temperature, and volume thermal expansion coefficient, using the model and bulk parameters from the paper.
- schema:
  - `type`: table
  - `required_columns`: `material`, `dimension`, `size_nm`, `interface_type`, `ThetaD_ratio`, `ThetaE_ratio`, `alphav_ratio`
  - `units`:
    - `ThetaD_ratio`: dimensionless
    - `ThetaE_ratio`: dimensionless
    - `alphav_ratio`: dimensionless

Notes: The test cases (material, dimension, sizes, interface types) and the necessary bulk material parameters will be provided in the instruction. The hidden checker will recompute the expected values using the same formulas and parameters and compare each row with a relative tolerance of 1e-6.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "dimension",
          "size_nm",
          "interface_type",
          "ThetaD_ratio",
          "ThetaE_ratio",
          "alphav_ratio"
        ],
        "units": {
          "ThetaD_ratio": "dimensionless",
          "ThetaE_ratio": "dimensionless",
          "alphav_ratio": "dimensionless"
        }
      },
      "description": "CSV with computed size-dependent ratios for Debye temperature, Einstein temperature, and volume thermal expansion coefficient, using the model and bulk parameters from the paper."
    }
  ],
  "notes": "The test cases (material, dimension, sizes, interface types) and the necessary bulk material parameters will be provided in the instruction. The hidden checker will recompute the expected values using the same formulas and parameters and compare each row with a relative tolerance of 1e-6."
}
```

## How you are scored
A hidden verifier independently recomputes the expected ratios for every test case using the same formulas and parameter values. It compares your submitted values in `predicted_ratios.csv` row by row against the recomputed gold with a very tight relative tolerance. Full credit (1.0) requires all rows to match within tolerance; otherwise, reward is reduced in proportion to the fraction of rows that match. Note: the verifier does not check intermediate steps – only the final CSV is scored.
