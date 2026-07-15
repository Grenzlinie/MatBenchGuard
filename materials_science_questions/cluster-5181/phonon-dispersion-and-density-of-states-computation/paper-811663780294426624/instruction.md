# DFT Phonon Frequencies of Mixed Tetrahedranide Clusters

## Problem background
The vibrational spectra of pure and mixed tetrahedranide anions [E4]4- (E = Si, Ge, Sn) are of fundamental interest for understanding bonding in Zintl phases. This task concerns the theoretical determination of the internal vibrational frequencies of mixed tetrahedral clusters [SixGe4-x]4- and [GexSn4-x]4- (x = 1, 2, 3) in hypothetical K4 compounds. Computing these frequencies by first-principles methods enables assignment of the experimentally observed Raman bands and provides insight into the force constants and the effect of cluster composition on the vibrational modes.

## Approach
The approach is a density functional theory (DFT) workflow using the SIESTA code. For each mixed cluster composition, a hypothetical crystal structure is constructed by linear interpolation of the lattice parameters between the pure end members K4Si4, K4Ge4, and K4Sn4, whose crystal structures are publicly available. Full structural relaxation is performed with the GGA-PBE exchange-correlation functional and Troullier-Martins pseudopotentials. The zone-center phonon frequencies are then obtained via the finite displacement method (typical displacement ~0.04 Å) as implemented in SIESTA's vibra package. From the calculated phonon results, the six internal vibrational modes of the E4 tetrahedron are identified and assigned symmetry labels according to the correlation from Td to C3v (for x = 1, 3: 2A1 + 2E) or to C2v (for x = 2: 3A1 + A2 + B1 + B2). The computed frequencies are reported together with their mode and symmetry designations.

## Reproduction target
Produce a file `computed_frequencies.json` that contains the zone-center phonon frequencies (in cm-1) and symmetry labels for the internal modes of the six mixed clusters: K4[Si3Ge], K4[Si2Ge2], K4[SiGe3], K4[Ge3Sn], K4[Ge2Sn2], and K4[GeSn3]. The file must be a JSON array of objects, each with the fields `cluster` (string), `mode` (string, e.g., "v1(A1)"), `frequency` (float, cm-1), and `symmetry` (string, e.g., "A1"). All six modes for each cluster must be included.

## Assets

- SIESTA DFT code: https://departments.icmab.es/leem/siesta/
- Crystal structures of K4Si4, K4Ge4, K4Sn4: 10.1524/ncrs.2005.220.14.324; 10.1524/ncrs.1999.214.4.453; 10.1524/ncrs.1999.214.4.457

## Workflow steps

### Step 1: Prepare input structures and SIESTA input files
- Role: process
- Action: Obtain the crystal structures of K4Si4, K4Ge4, and K4Sn4 from public databases. Construct hypothetical crystal structures for each mixed composition K4[SixGe4-x] and K4[GexSn4-x] (x=1,2,3) by linear interpolation of lattice parameters between the end members. Generate SIESTA .fdf input files with appropriate computational parameters (exchange-correlation functional, pseudopotentials, k-point sampling, etc.).
- Evidence: `/app/outputs/prepared_structures.log`

### Step 2: Run SIESTA DFT relaxation and phonon calculations
- Role: process
- Action: For each mixed cluster structure, perform full structural relaxation using SIESTA with GGA-PBE functional. Then compute the zone-center (Γ point) phonon frequencies using the finite displacement method (displacement amplitude typical 0.04 Å) via the SIESTA vibra package. Save the phonon calculation outputs.
- Evidence: `/app/outputs/dft_results.tar.gz`

### Step 3: Extract internal vibrational frequencies and assign symmetries
- Role: scored (load-bearing)
- Action: From the SIESTA phonon calculation outputs for each mixed cluster, identify the six internal vibrational modes of the E4 tetrahedron. Assign mode symmetry labels following the correlation Td → C3v (2A1+2E) or C2v (3A1+A2+B1+B2). Write the results to computed_frequencies.json with entries for each cluster: cluster (string), mode (string), frequency (float, cm^{-1}), symmetry (string). Include all internal modes for the six mixed clusters: K4[Si3Ge], K4[Si2Ge2], K4[SiGe3], K4[Ge3Sn], K4[Ge2Sn2], K4[GeSn3].
- Output file: `/app/outputs/computed_frequencies.json`
- Format: json
- Contract: JSON array of objects with fields: cluster (string, e.g. "K4[Si3Ge]"), mode (string, e.g. "v1(A1)"), frequency (float, cm^{-1}), symmetry (string, e.g. "A1").
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_frequencies.json
- path: `/app/outputs/computed_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed zone-center phonon frequencies for internal modes of mixed tetrahedral cluster anions in K4 compounds. Each entry pairs a cluster composition with a vibrational mode label, its frequency, and symmetry assignment.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `cluster`, `mode`, `frequency`, `symmetry`
    - `properties`:
      - `cluster`:
        - `type`: string
      - `mode`:
        - `type`: string
      - `frequency`:
        - `type`: number
        - `units`: cm^{-1}
      - `symmetry`:
        - `type`: string

Notes: The hidden gold values are the theoretical frequencies reported in the paper for the same clusters computed with SIESTA-GGA. The checker compares each frequency within a tolerance and verifies symmetry labels.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "cluster",
            "mode",
            "frequency",
            "symmetry"
          ],
          "properties": {
            "cluster": {
              "type": "string"
            },
            "mode": {
              "type": "string"
            },
            "frequency": {
              "type": "number",
              "units": "cm^{-1}"
            },
            "symmetry": {
              "type": "string"
            }
          }
        }
      },
      "description": "DFT-computed zone-center phonon frequencies for internal modes of mixed tetrahedral cluster anions in K4 compounds. Each entry pairs a cluster composition with a vibrational mode label, its frequency, and symmetry assignment."
    }
  ],
  "notes": "The hidden gold values are the theoretical frequencies reported in the paper for the same clusters computed with SIESTA-GGA. The checker compares each frequency within a tolerance and verifies symmetry labels."
}
```

## How you are scored
A hidden verifier independently checks your `computed_frequencies.json`. For each entry, the verifier compares the reported frequency to a reference theoretical frequency for that cluster and mode, using appropriate tolerances. It also verifies that the symmetry label matches the expected assignment. The final reward is proportional to the number of correctly reproduced frequencies across all clusters; partial credit is given. The verifier expects results that are consistent with a genuine re‑execution of the DFT workflow; simply reporting the paper's numbers without performing the calculation will not be sufficient.
