# Computation of Curvature Factors for Copper Fermi Surface (HCu7 Model)

## Problem background
In de Haas–van Alphen (dHvA) experiments, the amplitude of the quantum oscillations depends on the curvature factor C = |∂²A/∂k_H²|⁻¹/², where A is the extremal cross‑sectional area of the Fermi surface and k_H is the wave‑vector component parallel to the magnetic field. Together with the related fourth‑derivative parameter α⁻¹/², C is needed to extract the spin‑splitting factor G = cos(½π g m/m₀) and thus the electronic g‑factor. Previous published C values for copper were inconsistent, and reliable values are required to interpret absolute dHvA amplitude measurements. This reproduction task computes C and α⁻¹/² for copper (Cu) using the well‑established Halse seven‑term Fourier description of the Fermi surface (HCu7) over a range of field orientations in the (110) plane.

## Approach
The HCu7 model represents the Fermi‑surface radius vector as a finite Fourier series with seven fitted coefficients. For a given magnetic‑field orientation, the radius vector k(ψ) in the plane perpendicular to the field is found by solving the Fourier equation with a false‑position iteration for each polar angle ψ. The extremal cross‑sectional area A is then obtained by numerically integrating ½∫ k²(ψ) dψ. This area computation is repeated for several small displacements k_H along the field direction to obtain a table of A(k_H). The data are fitted to the expansion A = A₀ + ½ a₂ k_H² + (1/24) a₄ k_H⁴ to extract the second and fourth derivatives a₂ = ∂²A/∂k_H² and a₄ = ∂⁴A/∂k_H⁴. From these, the curvature factor C = 1/√(|a₂|) and the auxiliary quantity α⁻¹/² = √(24 a₂² / (A_s a₄) · (F_s/H)) are computed, where A_s is the cross‑sectional area of a free‑electron sphere with the same conduction‑electron density as Cu (using the copper fcc lattice constant a = 3.614 Å and one electron per atom) and F_s/H is taken as 10⁴. For rosette orbits the extremum shifts away from the symmetry centre, requiring a careful determination of the true extremal area when fitting the A(k_H) expansion.

## Reproduction target
Using the above method, compute C and α⁻¹/² for copper with the HCu7 model at every belly, rosette, and dogsbone orientation in the (110) plane listed in the output contract. Produce a CSV file (cu_hcu7_110.csv) with columns angle_deg, C, and alpha_inv_sqrt; one row per orientation/orbit type.

## Assets

- Halse Fermi surface Fourier coefficients for Cu (HCu7): 10.1098/rsta.1969.0055
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute A(k_H) data for HCu7 Cu (110) plane
- Role: process
- Action: For each orientation angle and orbit type (belly, rosette, dogsbone) in the (110) plane as specified in the output contract, solve the HCu7 Fourier surface equation to obtain the Fermi-surface radius k(ψ) as a function of the polar angle ψ in the plane perpendicular to the magnetic field, using false-position iteration. Compute the extremal cross-sectional area A via numerical integration for several small displacements k_H along the field direction. Save the computed A(k_H) values optionally as evidence.
- Evidence: `/app/outputs/hcu7_110_areas.csv`

### Step 2: Derive C and α^{-1/2} for HCu7 Cu (110) plane
- Role: scored (load-bearing)
- Action: For each angle and orbit type, fit the A(k_H) data to the expansion A = A0 + 1/2 a2 k_H^2 + 1/24 a4 k_H^4, using the known extremal area A0 from the Fourier fit (account for shifted extremum for rosette orbits). Extract a2 = ∂²A/∂k_H² and a4 = ∂⁴A/∂k_H⁴. Compute C = 1/√(|a2|). Compute α^{-1/2} from the formula involving A_s (spherical Fermi-surface area derived from Cu lattice constant a=3.614 Å and one electron per atom) and a fixed ratio F_s/H = 1e4. Write the results to cu_hcu7_110.csv.
- Output file: `/app/outputs/cu_hcu7_110.csv`
- Format: csv
- Contract: angle_deg: float, C: float, alpha_inv_sqrt: float. One row per orientation/orbit (belly, rosette, dogsbone) as listed in the output contract.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cu_hcu7_110.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cu_hcu7_110.csv
- path: `/app/outputs/cu_hcu7_110.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Curvature factor C and α^{-1/2} for copper (HCu7) at the (110) plane belly orbits at angles 0,2,5,10,15,20,22,23,24,46,48,50,52,54.74,58,60,65,70,72,76,80,85,90 degrees, rosette orbits at 0,3,6,8 degrees, and dogsbone orbit at 76 degrees. Near-critical orientations 23° and 24° where C diverges are included in the file but excluded from scoring.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `C`, `alpha_inv_sqrt`
  - `units`:
    - `angle_deg`: degrees
    - `C`: dimensionless
    - `alpha_inv_sqrt`: dimensionless

Notes: The check compares each C and α^{-1/2} value to hidden reference values from the paper with a tolerance; near-critical belly orientations where ∂²A/∂k_H² changes sign are excluded from scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cu_hcu7_110.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "C",
          "alpha_inv_sqrt"
        ],
        "units": {
          "angle_deg": "degrees",
          "C": "dimensionless",
          "alpha_inv_sqrt": "dimensionless"
        }
      },
      "description": "Curvature factor C and α^{-1/2} for copper (HCu7) at the (110) plane belly orbits at angles 0,2,5,10,15,20,22,23,24,46,48,50,52,54.74,58,60,65,70,72,76,80,85,90 degrees, rosette orbits at 0,3,6,8 degrees, and dogsbone orbit at 76 degrees. Near-critical orientations 23° and 24° where C diverges are included in the file but excluded from scoring."
    }
  ],
  "notes": "The check compares each C and α^{-1/2} value to hidden reference values from the paper with a tolerance; near-critical belly orientations where ∂²A/∂k_H² changes sign are excluded from scoring."
}
```

## How you are scored
A hidden verifier will read your cu_hcu7_110.csv. It checks that the file exists, is correctly formatted CSV with the required columns, and contains the expected set of angle_deg rows. For each row (excluding a few near‑critical orientations where C diverges and the curvature factor is not well‑defined), the verifier compares your reported C and α⁻¹/² to independently determined reference values. Entries that fall within an acceptable tolerance contribute to your score; entries outside this tolerance are ignored. The final reward is proportional to the fraction of included rows that meet the tolerance. There is no credit for simply having the file; each entry must be numerically correct.
