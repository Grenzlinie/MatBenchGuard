# Extraction of Inter-site Polarization Matrix and Total Polarization for MnI2 Helical Spin States

## Problem background
Multiferroic materials exhibiting helical spin-spiral magnetic order can develop a ferroelectric polarization, but conventional models (inverse Dzyaloshinskii–Moriya interaction, spin-current/KNB model, bond polarization) fail to explain the observed polarization direction when the spiral propagation vector q lies in the triangular plane. A general symmetry-based expansion suggests that the electric polarization of a spin dimer arises from intra-site and inter-site contributions, with the inter-site part described by a 3×3 matrix M. For the layered compound MnI₂, which adopts a triangular lattice of Mn²⁺ ions, the magnitude and direction of the polarization in the helical state depend on the elements of this matrix and on a set of intra-site coefficients. Determining these coefficients and computing the total polarization for selected commensurate spiral states is the central computational challenge addressed here.

## Approach
The polarization of a single Mn-Mn pair is expressed as P = P₁(S₁) + P₂(S₂) + P₁₂(S₁,S₂). The intra-site terms are parameterized by symmetric coefficient vectors P₁^{αβ} (α,β ∈ {x,y,z}), while the inter-site term reduces to P₁₂ = M·(S₁×S₂), where M is a 3×3 real matrix with vanishing diagonal in the local frame. To extract these parameters for MnI₂, a 5×5×1 supercell of the CdI₂ structure is constructed and a single Mn-Mn pair is isolated (either by Mg substitution or by the no-substitution method with fixed background spins). Density functional calculations in the LDA+U+SOC scheme (U=5 eV, J=1 eV) are performed for a series of non-collinear spin configurations. The Berry-phase electric polarization is computed for each configuration. From these raw polarizations, mapping formulas based on symmetry are applied to obtain all non-zero elements of M and the relevant intra-site coefficients. With the coefficients determined, the total ferroelectric polarization of the bulk in a helical spin-spiral state is predicted by summing over all nearest-neighbor pairs. For two commensurate spiral states with wavevectors q=(1/3,0,0) and q=(1/3,1/3,0), the same DFT+U+SOC protocol is repeated in 3×1×1 and √3×√3 supercells with proper-screw spin arrangements to directly compute the total polarization via Berry phase. The modeling task thus spans three stages: raw dimer polarizations, coefficient extraction, and direct total polarization calculations.

## Reproduction target
Produce two output files:

1. inter_site_matrix_M.json: Contains the elements of the inter-site matrix M (in units of 10⁻⁵ eÅ) and the intra-site coefficients P1^{αβ} (in 10⁻⁶ eÅ) as arrays. The matrix M must report the non‑zero entries (M11, M22, M23, M32, M33) obtained from the no‑substitution method. The intra‑site coefficients include the diagonal differences and off‑diagonal terms as specified in the output schema.

2. total_polarization_helical_states.csv: Contains the total ferroelectric polarization vectors (Px, Py, Pz in μC/m²) for the two commensurate helical states, one with q = (1/3,0,0) and one with q = (1/3,1/3,0). All values must be computed from first‑principles DFT as described in the workflow.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org
- MnI2 crystal structure (CdI2-type, space group P-3m1): https://materialsproject.org/materials/mp-27943
- Pseudopotentials for Mn and I (SSSP efficiency set or GBRV): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Compute raw spin-dimer polarizations
- Role: process
- Action: Build a 5×5×1 supercell of MnI2 (CdI2-type) and perform LDA+U+SOC calculations (U=5 eV, J=1 eV with SOC) for two sets of spin-configurations, using the Berry-phase method to obtain raw electric polarization vectors in eÅ for each:

  (a) Intra-site coefficients (using the substitution method: replace all Mn²⁺ ions except the target dimer with nonmagnetic Mg²⁺, then place the dimer with specific spin directions):

    • Off-diagonal coefficient P1^xy: compute for four spin arrangements where (S1, S2) are
        ( (√2/2, √2/2, 0), (1,0,0) ), ( (√2/2, √2/2, 0), (-1,0,0) ),
        ( (√2/2, -√2/2, 0), (1,0,0) ), ( (√2/2, -√2/2, 0), (-1,0,0) ).
    • Off-diagonal coefficient P1^xz: compute for four arrangements with
        ( (√2/2, 0, √2/2), (1,0,0) ), ( (√2/2, 0, √2/2), (-1,0,0) ),
        ( (√2/2, 0, -√2/2), (1,0,0) ), ( (√2/2, 0, -√2/2), (-1,0,0) ).
    • Off-diagonal coefficient P1^yz: compute for four arrangements with
        ( (0, √2/2, √2/2), (1,0,0) ), ( (0, √2/2, √2/2), (-1,0,0) ),
        ( (0, √2/2, -√2/2), (1,0,0) ), ( (0, √2/2, -√2/2), (-1,0,0) ).
    • Diagonal intra-site differences and crude inter-site (not used for final M): compute for six arrangements with
        ( (1,0,0), (0,1,0) ), ( (1,0,0), (0,-1,0) ),
        ( (1,0,0), (0,0,1) ), ( (1,0,0), (0,0,-1) ),
        ( (0,1,0), (0,0,1) ), ( (0,1,0), (0,0,-1) ).

  (b) Inter-site matrix M (using the no‑substitution method: keep all Mn²⁺ ions, fix the 23 background spins to (0,0,1), and set the dimer spins as below):

    • For P12^yz: compute four arrangements where (S1, S2) are
        ( (0,1,0), (0,0,1) ), ( (0,1,0), (0,0,-1) ),
        ( (0,-1,0), (0,0,1) ), ( (0,-1,0), (0,0,-1) ).
    • For P12^xz: compute four arrangements where (S1, S2) are
        ( (1,0,0), (0,0,1) ), ( (1,0,0), (0,0,-1) ),
        ( (-1,0,0), (0,0,1) ), ( (-1,0,0), (0,0,-1) ).
    • For P12^xy: compute four arrangements where (S1, S2) are
        ( (1,0,0), (0,1,0) ), ( (1,0,0), (0,-1,0) ),
        ( (-1,0,0), (0,1,0) ), ( (-1,0,0), (0,-1,0) ).

  Collect the polarization vector (Px, Py, Pz) for each configuration and write them to a single JSON file (keys are configuration labels). All configurations use the local coordinate system: x is the direction from spin 1 to spin 2 (the Mn-Mn bond), y and z are perpendicular in the crystal.
- Evidence: `/app/outputs/raw_dimer_polarizations.json`

### Step 2: Extract inter-site matrix M and intra-site coefficients
- Role: scored (load-bearing)
- Action: Using the raw polarization vectors stored in `/app/outputs/raw_dimer_polarizations.json`, compute the intra-site coefficients and the inter-site matrix M as follows. All polarizations are in eÅ; when constructing M, express the result in 10⁻⁵ eÅ and for intra-site coefficients use 10⁻⁶ eÅ as final units.

  1. Intra-site off-diagonal:
       P1^xy = (P(I') + P(II') - P(III') - P(IV')) / 4,
       P1^xz = (P(I'') + P(II'') - P(III'') - P(IV'')) / 4,
       P1^yz = (P(I''') + P(II''') - P(III''') - P(IV''')) / 4,
     where the labels correspond to the substitution-method configurations listed in Step 1.

  2. Intra-site diagonal (choose a gauge with P1^xx = (0,0,0)):
       Compute Δ_xy = (P(I) + P(II)) / 2,   Δ_xz = (P(III) + P(IV)) / 2
       (using the six substitution-method configurations I–VI).
       Then set  P1^xx = (0,0,0),
                 P1^yy = –Δ_xy,
                 P1^zz = –Δ_xz.

  3. Inter-site M (from no‑substitution method):
       From the four-polarization sets for yz, xz, xy:
         P12^yz = (P(A_yz) + P(D_yz) – P(B_yz) – P(C_yz)) / 4,
         P12^xz = (P(A_xz) + P(D_xz) – P(B_xz) – P(C_xz)) / 4,
         P12^xy = (P(A_xy) + P(D_xy) – P(B_xy) – P(C_xy)) / 4.
       Then the non-zero elements of M (in 10⁻⁵ eÅ) are:
         M11 =  P12^yz_x,
         M22 = –P12^xz_y,
         M23 =  P12^xy_y,
         M32 = –P12^xz_z,
         M33 =  P12^xy_z.
- Output file: `/app/outputs/inter_site_matrix_M.json`
- Format: json
- Contract: JSON object with top-level keys 'M' (object with float keys M11, M22, M23, M32, M33), 'intra_site_coefficients' (object with keys P1xx, P1yy, P1zz, P1xy, P1xz, P1yz, each a list of three floats), and 'units' (string describing coefficient units).
- Scoring: scored by hidden verifier

### Step 3: Calculate total polarization for helical spin-spiral states
- Role: scored (load-bearing)
- Action: Build a 3×1×1 supercell and a √3×√3 supercell of MnI2 with proper-screw helical spin configurations for commensurate q=(1/3,0,0) and q=(1/3,1/3,0) states, respectively. Perform LDA+U+SOC calculations with Berry-phase polarization. Convert total polarization to μC/m² and output the two vectors (Px, Py, Pz) for each q.
- Output file: `/app/outputs/total_polarization_helical_states.csv`
- Format: csv
- Contract: CSV with columns: q_vec (string, e.g., '1/3,0,0' or '1/3,1/3,0'), Px (float, μC/m²), Py (float, μC/m²), Pz (float, μC/m²). Two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/inter_site_matrix_M.json`
- `/app/outputs/total_polarization_helical_states.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### inter_site_matrix_M.json
- path: `/app/outputs/inter_site_matrix_M.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced inter-site polarization matrix M and intra-site coefficients for the MnI2 spin dimer.
- schema:
  - `type`: object
  - `required`:
    - `M`: object containing float fields M11, M22, M23, M32, M33
    - `intra_site_coefficients`: object containing list-of-3-floats fields P1xx, P1yy, P1zz, P1xy, P1xz, P1yz
    - `units`: string

### total_polarization_helical_states.csv
- path: `/app/outputs/total_polarization_helical_states.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total ferroelectric polarization vectors from direct DFT for the two commensurate helical spin-spiral states.
- schema:
  - `type`: table
  - `required_columns`: `q_vec`, `Px`, `Py`, `Pz`
  - `units`:
    - `Px`: μC/m²
    - `Py`: μC/m²
    - `Pz`: μC/m²

Notes: The total polarization computation uses direct DFT supercell calculations; the gKNB model prediction from the extracted coefficients should be consistent, but only the direct DFT values are scored. Verifier compares each component with paper-reported references using tolerances appropriate for toolchain differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "inter_site_matrix_M.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "M": "object containing float fields M11, M22, M23, M32, M33",
          "intra_site_coefficients": "object containing list-of-3-floats fields P1xx, P1yy, P1zz, P1xy, P1xz, P1yz",
          "units": "string"
        }
      },
      "description": "Reproduced inter-site polarization matrix M and intra-site coefficients for the MnI2 spin dimer."
    },
    {
      "file": "total_polarization_helical_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_vec",
          "Px",
          "Py",
          "Pz"
        ],
        "units": {
          "Px": "μC/m²",
          "Py": "μC/m²",
          "Pz": "μC/m²"
        }
      },
      "description": "Total ferroelectric polarization vectors from direct DFT for the two commensurate helical spin-spiral states."
    }
  ],
  "notes": "The total polarization computation uses direct DFT supercell calculations; the gKNB model prediction from the extracted coefficients should be consistent, but only the direct DFT values are scored. Verifier compares each component with paper-reported references using tolerances appropriate for toolchain differences."
}
```

## How you are scored
A hidden verifier compares your submitted artifacts against reference values, using absolute tolerances that account for differences due to the DFT implementation (e.g., Quantum ESPRESSO instead of the original code).

- For inter_site_matrix_M.json, the non-zero matrix elements M11, M22, M23, M32, M33 are compared individually against reference values, and the intra-site coefficients are similarly compared. Correct sign, order of magnitude, and value within tolerance all matter.
- For total_polarization_helical_states.csv, the three Cartesian components (Px, Py, Pz) for each q are compared to reference vectors. The comparison rewards vectors that are close in magnitude and show the physically correct directional pattern; a substantial deviation in any component or in the overall polarization direction reduces the score.

Each scored artifact carries a predefined weight (details hidden); the final reward is a weighted sum between 0 and 1. The scoring is monotonic — a more accurate result that surpasses the reference is never penalized. Producing these artifacts requires a full DFT workflow; simply guessing or fabricating numbers is unlikely to pass the verifier’s tolerance checks.
