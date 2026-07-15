# Phonon symmetry decomposition via group theory in wurtzite ZnO

## Problem background
In wurtzite ZnO, electrons can scatter between different valleys of the conduction band via phonon interactions. This scattering is described by tensors whose symmetry properties are governed by the Clebsch–Gordan coefficients (CGCs) of the space group. The CGCs are the entries of a unitary matrix that reduces Kronecker products of irreducible representations (irreps) of the crystal space group, thereby block‑diagonalizing the scattering Hamiltonians. For the representative inter‑valley process L→M, the relevant Kronecker product is L₁⊗M₁ in the space group C₆ᵛ⁴ (No. 186, P6₃mc). The determination of these CGCs is a purely computational group‑theoretical problem whose solution provides the fundamental building blocks for constructing scattering tensors and effective k·p Hamiltonians in ZnO and related wurtzite semiconductors. This task asks you to compute those coefficients for L₁⊗M₁ from the known wave‑vector selection rules, star vectors, and Kronecker product decomposition.

## Approach
The computation follows the Berenson–Birman method for space‑group Clebsch–Gordan coefficients. First, the wave‑vector selection rules (WVSRs) are derived by enumerating all pairs of star vectors of the L and M points that satisfy momentum conservation. These WVSRs determine the nine allowed scattering channels. Using the known Kronecker product decomposition L₁⊗M₁ = A₁⊕A₅⊕L₁⊕L₂ (obtained from standard CDML tables or group‑theory software) and the explicit irreducible representation matrices for the L₁ and M₁ irreps of space group C₆ᵛ⁴, you construct the projected matrices that correspond to each irrep appearing in the direct sum. The Berenson–Birman procedure then yields the 9×9 unitary matrix U (the CGC matrix) whose columns are ordered by the irrep blocks A₁, A₅, L₁, L₂ and whose rows correspond to the nine WVSRs. Finally, the correctness of U is verified by applying it to the Kronecker product D(L₁)⊗D(M₁) and checking that the transformed matrix is block‑diagonal with the expected irrep blocks.

## Reproduction target
Compute the 9×9 unitary CGC matrix for the Kronecker product L₁⊗M₁ that block‑diagonalizes the product into the direct sum A₁⊕A₅⊕L₁⊕L₂. The matrix should be expressed as a JSON array of [real, imag] pairs with at least 6 decimal places, where the row order follows the nine WVSRs (as enumerated in step 1) and the column groups correspond to A₁, A₅, L₁ (three basis indices), and L₂ (three basis indices). Additionally, verify the block‑diagonal property: construct the Kronecker product matrices D(L₁)⊗D(M₁) from the irreducible representation matrices of space group C₆ᵛ⁴, apply the matrix U, and report the decomposition labelled by irrep symbols (A1, A5, L1, L2), the sizes of the diagonal blocks [1, 1, 3, 3], and the maximum absolute value of any off‑block‑diagonal element (the block‑diagonal norm).

## Assets

- Bilbao Crystallographic Server: https://www.cryst.ehu.es/

## Workflow steps

### Step 1: Derive wave-vector selection rules for L and M valleys
- Role: process
- Action: Using the star vectors for the L point (k_L(101), 2k_L(011), 3k_L(-111)) and the M point (k_M(010), 2k_M(100), 3k_M(010)), enumerate all pairs of wave vectors that satisfy momentum conservation for inter‑valley scattering from L to M. Export the list of allowed WVSRs as a structured evidence file.
- Evidence: `/app/outputs/wvsr_L1_M1.json`

### Step 2: Compute the Clebsch–Gordan coefficient matrix for L1⊗M1
- Role: scored (load-bearing)
- Action: Using the WVSRs from step 1 and the known Kronecker product decomposition L1⊗M1 = A1⊕A5⊕L1⊕L2, apply the Berenson–Birman method to construct the unitary matrix U that block‑diagonalizes the Kronecker product of the irreducible representations L1 and M1. Output the 9×9 matrix as a JSON object, rows ordered by the nine WVSR blocks and columns grouped as A1, A5, L1 (three basis indices), L2 (three basis indices). Each entry is a complex number expressed as a pair [real, imag] with at least 6 decimal places.
- Output file: `/app/outputs/cgc_matrix_L1_M1.json`
- Format: json
- Contract: JSON object with key 'matrix' containing a 9×9 array of [real, imag] pairs.
- Scoring: scored by hidden verifier

### Step 3: Verify block diagonalization of L1⊗M1
- Role: scored (load-bearing)
- Action: Construct the Kronecker product matrices D(L1)⊗D(M1) from the irreducible representation matrices of space group C6v4, apply the matrix U from step 2, and verify that the transformed matrix is block‑diagonal with blocks corresponding to A1, A5, L1, L2. Report the list of irrep labels (in block order), the size of each block, and the maximum absolute value of any element outside the diagonal blocks (the off‑block‑diagonal norm).
- Output file: `/app/outputs/reduction_verification.json`
- Format: json
- Contract: JSON object with keys: 'irreps_decomposition' (list of strings), 'block_sizes' (list of integers), 'block_diagonal_norm' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cgc_matrix_L1_M1.json`
- `/app/outputs/reduction_verification.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cgc_matrix_L1_M1.json
- path: `/app/outputs/cgc_matrix_L1_M1.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The 9×9 unitary CGC matrix for L1⊗M1. Each entry is a complex number given as [real, imag] with at least 6 decimal places. Rows correspond to the nine WVSR blocks, columns are grouped as A1, A5, L1 (3 basis indices), L2 (3 basis indices).
- schema:
  - `type`: object
  - `required`:
    - `matrix`: 9x9 array of [real,imag] pairs
  - `items`:
    - `matrix`: array of array of [number, number]
  - `required_columns`:
  - `units`: object

### reduction_verification.json
- path: `/app/outputs/reduction_verification.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Verification that the CGC matrix block‑diagonalizes the Kronecker product. The irrep labels are in block order (A1, A5, L1, L2), block sizes are [1,1,3,3], and block_diagonal_norm is the maximum absolute value of any off‑block‑diagonal element after applying U.
- schema:
  - `type`: object
  - `required`:
    - `irreps_decomposition`: list of irrep labels
    - `block_sizes`: list of integers
    - `block_diagonal_norm`: float
  - `items`:
    - `irreps_decomposition`: array of strings
    - `block_sizes`: array of integers
    - `block_diagonal_norm`: number
  - `required_columns`:
  - `units`: object

Notes: The reference for the CGC matrix is an independent recomputation using the same WVSRs and Berenson–Birman method. The block‑diagonal norm should be near zero (numeric tolerance). All quantities are expressed in the standard basis used in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cgc_matrix_L1_M1.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "matrix": "9x9 array of [real,imag] pairs"
        },
        "items": {
          "matrix": "array of array of [number, number]"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "The 9×9 unitary CGC matrix for L1⊗M1. Each entry is a complex number given as [real, imag] with at least 6 decimal places. Rows correspond to the nine WVSR blocks, columns are grouped as A1, A5, L1 (3 basis indices), L2 (3 basis indices)."
    },
    {
      "file": "reduction_verification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "irreps_decomposition": "list of irrep labels",
          "block_sizes": "list of integers",
          "block_diagonal_norm": "float"
        },
        "items": {
          "irreps_decomposition": "array of strings",
          "block_sizes": "array of integers",
          "block_diagonal_norm": "number"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Verification that the CGC matrix block‑diagonalizes the Kronecker product. The irrep labels are in block order (A1, A5, L1, L2), block sizes are [1,1,3,3], and block_diagonal_norm is the maximum absolute value of any off‑block‑diagonal element after applying U."
    }
  ],
  "notes": "The reference for the CGC matrix is an independent recomputation using the same WVSRs and Berenson–Birman method. The block‑diagonal norm should be near zero (numeric tolerance). All quantities are expressed in the standard basis used in the paper."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that independently recomputes the reference CGC matrix and the block‑diagonal decomposition using the same group‑theoretical procedure. The verifier compares your `cgc_matrix_L1_M1.json` element‑wise against its own recomputation, checks the unitarity of U (U·U† should equal the identity within numerical tolerance), and confirms that the reported irrep decomposition and block sizes are correct. For `reduction_verification.json`, the verifier validates the irrep labels, block sizes, and that the off‑block‑diagonal norm is below a small tolerance. The final reward is a weighted combination of the scores on the two scored artifacts, with the CGC matrix accuracy carrying the highest weight. Merely reporting the expected decomposition without genuinely computing and verifying the matrix will not yield a high score.
