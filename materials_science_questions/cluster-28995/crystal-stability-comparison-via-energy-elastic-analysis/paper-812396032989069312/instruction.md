# Acoustic Wave Band Gap Analysis in Periodic Composite Structures

## Problem background
Acoustic waves propagating in periodic composite media can exhibit frequency band gaps where no propagating modes exist. Understanding how these gaps depend on material parameters such as the density contrast between the spheres and the host is important for designing acoustic filters and studying wave localization. This task considers a scalar acoustic wave model (shear modulus μ=0) in a three-dimensional periodic structure consisting of identical spheres arranged in an fcc lattice within a uniform host material. The pressure field satisfies a modified wave equation with a spatially varying density. By solving for the allowed vibrational frequencies as a function of wavevector, one can determine whether complete gaps (frequency ranges with no allowed modes for any propagation direction) appear, and how their size is affected by changing the sphere-to-host density ratio while keeping the volume fraction and longitudinal velocity ratio fixed.

## Approach
Use the plane-wave expansion method to solve the scalar acoustic wave equation for a three-dimensional fcc periodic lattice. In this approach, the pressure field and the material parameters (density and the product of Lamé coefficient and density) are expanded in a Fourier series over the reciprocal lattice vectors. Substituting these expansions and applying Bloch's theorem leads to an N×N eigenvalue problem for each wavevector **k** in the irreducible Brillouin zone, where N is the number of retained plane waves. The eigenvalues ω² correspond to the squared angular frequencies of the acoustic modes. By sweeping **k** along a sufficient set of symmetry directions, you can construct the band structure or the density of states (DOS). A complete frequency gap is identified as a frequency interval with no eigenmodes for any **k**. For each specified density ratio, compute the band structure or DOS, locate the lowest complete gap (if any), and record its lower and upper edges together with the gap-to-midgap ratio. All computations should be performed for the fixed volume fraction x=14.4% and host-to-sphere longitudinal velocity ratio c_lo/c_li=2.65, with three different values of the density ratio y = ρ_i/ρ_o.

## Reproduction target
Compute the acoustic band structure or density of states for an fcc lattice of spheres at volume fraction 14.4% and velocity ratio c_lo/c_li=2.65, for each density ratio y = 5, 1, and 1/15. For each y, determine whether a complete frequency gap exists. If a gap is present, calculate its lower edge, upper edge, and the gap-to-midgap ratio. Write the results to /app/outputs/gap_results.json as three entries, one per density ratio, including the gap presence flag and (where applicable) the gap frequency values and ratio. All frequencies should be expressed in a consistent reduced unit.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Acoustic band gap computation
- Role: scored (load-bearing)
- Action: Implement the plane-wave expansion method for the scalar acoustic wave equation (∂²p/∂t² = λ ∇·(∇p/ρ)) on an fcc lattice of spheres. Set sphere volume fraction to 14.4% and host-to-sphere longitudinal velocity ratio c_lo/c_li = 2.65. For each density ratio y ∈ {5, 1, 1/15}, compute the band structure or density of states, identify the lowest complete frequency gap (if any), and record gap presence together with gap lower edge, upper edge, and gap-to-midgap ratio. Write the results to /app/outputs/gap_results.json.
- Output file: `/app/outputs/gap_results.json`
- Format: json
- Contract: A JSON object with key 'results' containing an array of 3 objects. Each object has keys: density_ratio (float), gap_present (bool), gap_lower_frequency (float or null), gap_upper_frequency (float or null), gap_midgap_ratio (float or null). If no gap exists, set gap_present=false and the frequency/ratio fields to null. Frequencies are normalized in consistent reduced units (e.g., ω a/(2π c) or similar).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gap_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gap_results.json
- path: `/app/outputs/gap_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gap presence and gap metrics for three acoustic conditions: high-density spheres (y=5), equal density (y=1), and low-density spheres (y=1/15). For conditions with no gap, the frequency/ratio fields must be null.
- schema:
  - `type`: object
  - `required`:
    - `results`: array of 3 objects
  - `items`:
    - `density_ratio`: float
    - `gap_present`: bool
    - `gap_lower_frequency`: float or null
    - `gap_upper_frequency`: float or null
    - `gap_midgap_ratio`: float or null
  - `units`:
    - `frequencies`: normalized frequency in reduced units (e.g., ω a/(2π c) or similar)

Notes: The task covers only the scalar acoustic wave case (μ=0). Elastic wave results and other lattice structures are excluded per the paper's scope and feasibility. The hidden checker compares the reported gap_present and gap_midgap_ratio values against the paper's trends with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gap_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "results": "array of 3 objects"
        },
        "items": {
          "density_ratio": "float",
          "gap_present": "bool",
          "gap_lower_frequency": "float or null",
          "gap_upper_frequency": "float or null",
          "gap_midgap_ratio": "float or null"
        },
        "units": {
          "frequencies": "normalized frequency in reduced units (e.g., ω a/(2π c) or similar)"
        }
      },
      "description": "Gap presence and gap metrics for three acoustic conditions: high-density spheres (y=5), equal density (y=1), and low-density spheres (y=1/15). For conditions with no gap, the frequency/ratio fields must be null."
    }
  ],
  "notes": "The task covers only the scalar acoustic wave case (μ=0). Elastic wave results and other lattice structures are excluded per the paper's scope and feasibility. The hidden checker compares the reported gap_present and gap_midgap_ratio values against the paper's trends with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will read /app/outputs/gap_results.json and check the reported gap_present flags and, when a gap is present, the gap_lower_frequency, gap_upper_frequency, and gap_midgap_ratio. The verifier uses pre‑defined criteria to assess whether the results are physically reasonable and consistent with the acoustic wave behaviour in periodic composites. It does not rely on exact numerical agreement with any single reference, but expects the overall pattern of gap existence and relative sizes across the three density ratios to match physically expected trends. The final score combines the verified outcomes into a single reward in the range [0, 1].
