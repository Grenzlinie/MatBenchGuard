# Computational Molecular Dipole Moment and Kerr Constant Calculation for Tin Tropolonate Configurations

## Problem background
The molecular geometry of six-coordinate organotin compounds of the type R₂Sn(trop)₂ (R = Cl, CH₃, C₆H₅; trop = tropolonate anion) in solution is of considerable interest because both cis and trans arrangements of the ligands are possible. Experimental dipole moments and electric birefringence (Kerr effect) measurements provide a powerful route to distinguish between candidate structures. The molar Kerr constant of a molecule depends on its optical polarizability anisotropy and its permanent electric dipole moment, as expressed by the Langevin–Born theory. The goal is to compute theoretical molar Kerr constants for each plausible configuration and compare them with the experimental results to deduce the preferred geometry. This requires assembling the bond and group polarizability anisotropies from known literature data and from the experimental Kerr constant of the tropolone ligand itself, then performing vector addition of these anisotropies for each candidate structure under assumed octahedral bond angles.

## Approach
The approach rests on the Langevin–Born theory, which relates the molar Kerr constant (mK) to the principal molecular polarizabilities b₁, b₂, b₃ and the dipole moment components μ₁, μ₂, μ₃, along with the ratio of distortion to electron polarization (DP/EP). For the planar tropolone ligand, the in-plane polarizabilities are assumed equal (b₁ = b₂), allowing its optical anisotropy (b₁ − b₃) to be calculated directly from its experimental dipole moment and molar Kerr constant using a simplified form of the Langevin–Born equation. With this anisotropy in hand, the bond/group polarizability differences for Sn–Cl, Sn–CH₃, and Sn–O (taken from published quantum chemical estimates) are combined to obtain the anisotropy of the Sn(trop) group, treating the two Sn–O bonds as orthogonal. For each tin tropolonate derivative — Cl₂Sn(trop)₂, (CH₃)₂Sn(trop)₂, and (C₆H₅)₂Sn(trop)₂ — three candidate structures are considered: centrosymmetric trans (D₂h), cis of C₂ symmetry, and a cis form distorted toward C₂v. In each case, the molecular polarizability tensor is constructed by resolving the individual bond/group anisotropies along the principal axes of an assumed regular octahedral geometry and summing them. The differences (b₁−b₂) and (b₁−b₃) are then computed. Using the full Langevin–Born equation together with the dipole moment components derived from the assigned bond moments, theoretical molar Kerr constants are calculated for every candidate. Additionally, group dipole moments of the Sn(trop) moiety are derived from the measured total dipole moments and the known Sn–R bond moments.

## Reproduction target
Produce a single JSON file (`computed_results.json`) containing all computed quantities:
- The polarizability anisotropy of tropolone, (b₁−b₃), in units of 10⁻²⁴ cm³.
- The bond/group polarizability anisotropies for Sn–Cl, Sn–CH₃, Sn–O, and Sn(trop).
- For each of the three derivatives, for each candidate structure (trans D₂h, cis C₂, cis C₂v): the polarizability differences (b₁−b₂) and (b₁−b₃) and the theoretical molar Kerr constant (in 10⁻¹² cgs).
- The group dipole moment of the Sn(trop) moiety (in Debye) for each derivative.

## Assets

- Bond moments from Lorberth & Noth (1965)
- Polarizability anisotropies from Lippincott & Stutman (1964)
- Experimental dipole moment and Kerr constant of tropolone
- NumPy: numpy

## Workflow steps

### Step 1: Compute optical anisotropy of tropolone
- Role: process
- Action: Using the provided experimental dipole moment and molar Kerr constant of tropolone in cyclohexane (or CCl4) and the simplified Langevin-Born equation for a planar molecule (assuming b1=b2 and b3 perpendicular to the ring plane), compute the polarizability anisotropy (b1-b3) of tropolone. The equation is: mK = (2πN/405kT)[ 2(DP/EP)(b1-b3)^2 + (1/kT) μ_obsd^2 (b1-b3) ], with DP/EP = 1.1, and 2πN/405kT evaluated at 25°C.
- Evidence: none

### Step 2: Assemble bond/group polarizability anisotropies
- Role: process
- Action: Combine the computed tropolone anisotropy with the provided literature bond polarizability anisotropies (Sn-Cl: 5.5e-24 cm3, Sn-CH3: 5.3e-24 cm3, Sn-O: 3.5e-24 cm3) to obtain the Sn(trop) group anisotropy. The Sn(trop) group anisotropy is the sum of the tropolone ring anisotropy and the contributions from two Sn-O bonds oriented at 90° to each other.
- Evidence: none

### Step 3: Compute molecular polarizability differences for all candidate structures
- Role: process
- Action: For each derivative and candidate structure, use the molecular coordinate systems defined below to resolve each bond/group polarizability tensor into the molecular frame, sum the tensors, and then compute the principal polarizabilities b₁, b₂, b₃ and the differences (b₁‑b₂), (b₁‑b₃). All anisotropies are expressed as the difference between the largest in‑plane component and the perpendicular component (b∥ – b⊥). The molecular axes are chosen so that the tensor is diagonal after summation.

  * **trans D₂h**: Place the Sn atom at the origin. The two Sn–R bonds lie along the ±x axis. The four O atoms of the two tropolonate ligands lie in the yz plane: one ligand has its two O atoms at (0, d, 0) and (0, 0, d), the other at (0, −d, 0) and (0, 0, −d). The tropolone ring lies in the yz plane. For each Sn(trop) group, the principal axes are oriented with b₁ and b₂ in the yz plane at 45° to the y and z axes, and b₃ along the x axis. The Sn–R bonds are uniaxial along x, contributing an anisotropy Δ to the x direction. Summing the two groups (each with anisotropy a = 17.7 × 10⁻²⁴ cm³) and the two Sn–R bonds (each Δ = bond anisotropy) yields the molecular polarizability differences.

  * **cis C₂** (C₂ symmetry axis = z): The two Sn–R bonds are in the xy plane at 90° to each other, along the +x and +y directions. The two tropolonate ligands occupy the remaining positions: ligand A chelates via two O atoms located at (0, −d, d) and (0, d, d), so its ring plane contains the z axis and the y direction; its b₃ axis (perpendicular to the ring) points along x. Ligand B is obtained by a 180° rotation about z, giving O atoms at (0, d, −d) and (0, −d, −d), with b₃ along −x. In each Sn(trop) group, the in‑plane axes b₁ and b₂ are in the yz plane with b₁ along the direction bisecting the O‑Sn‑O angle (i.e., along z) and b₂ along y. Sum all tensors and diagonalize.

  * **cis C₂ᵥ** (mirror plane σᵥ): The two Sn–R bonds are cis and lie in the xz mirror plane at an angle of about 75° to each other; the precise angle is less than 90° due to distortion. The two tropolonate ligands are positioned such that their ring planes are parallel and perpendicular to the y axis. For the vector addition, one may orient the Sn(trop) b₃ axes along ±y, and the in‑plane axes b₁ and b₂ in the xz plane with b₁ pointing approximately along the bisector of the O–Sn–O angle. The agent should compute by summing the tensors as described for cis C₂ but with the modified geometry.

  All vector additions shall be carried out using standard tensor summation. The resulting b₁, b₂, b₃ are the eigenvalues of the total polarizability matrix; then compute (b₁ – b₂) and (b₁ – b₃).
- Evidence: none

### Step 4: Compute molar Kerr constants and group moments, output final results
- Role: scored (load-bearing)
- Action: Using the polarizability differences from the previous step, the resolved dipole moment components derived from the provided bond moments and geometry, and the full Langevin‑Born equation

$$
_{\mathrm{m}} K = \frac{2\pi N}{405kT} \left[ \left(\frac{D\!P}{E\!P}\right) \Big( (b_1-b_2)^2 + (b_2-b_3)^2 + (b_3-b_1)^2 \Big) + \frac{1}{kT} \Big( (\mu_1^2-\mu_2^2)(b_1-b_2) + (\mu_2^2-\mu_3^2)(b_2-b_3) + (\mu_3^2-\mu_1^2)(b_3-b_1) \Big) \right]
$$

with $\frac{D\!P}{E\!P}=1.1$, $N=6.02214\times10^{23}$, $k=1.38065\times10^{-23}\,\mathrm{erg\,K^{-1}}$, $T=298.15\,\mathrm{K}$, and the dipole moment components $\mu_1,\mu_2,\mu_3$ obtained from the bond moments and the assumed geometry (see bond moments: Sn–Cl 4.2 D, Sn–CH₃ 0.6 D, Sn–C₆H₅ 1.1 D). The constant $\frac{2\pi N}{405kT}$ can be evaluated directly from these constants. Compute the theoretical molar Kerr constant for every candidate structure. Also derive the group dipole moment of the Sn(trop) moiety. The measured total dipole moments for the three complexes (from the paper's Table II) are: Cl₂Sn(trop)₂ μ = 8.8 D, (CH₃)₂Sn(trop)₂ μ = 3.65 D, (C₆H₅)₂Sn(trop)₂ μ = 4.6 D. The bond moments (Sn–Cl 4.2 D, Sn–CH₃ 0.6 D, Sn–C₆H₅ 1.1 D) are known from Lorberth & Nöth. Assuming a regular octahedral cis configuration where the Sn–R bonds are oriented at 90° to each other and to the Sn(trop) group moment direction, perform vector subtraction to obtain the scalar magnitude of the Sn(trop) group moment for each derivative. The Sn(trop) group moment is the contribution from a single tropolonate ligand to the overall molecular dipole moment. Aggregate all results into a single JSON file as specified in the output contract.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: {"type": "object", "required": ["tropolone_anisotropy", "bond_anisotropies", "derivatives", "group_moments"], "properties": {"tropolone_anisotropy": {"type": "number", "description": "(b1-b3) in 1e-24 cm^3"}, "bond_anisotropies": {"type": "object", "required": ["Sn-Cl", "Sn-CH3", "Sn-O", "Sn(trop)"], "properties": {"Sn-Cl": {"type": "number"}, "Sn-CH3": {"type": "number"}, "Sn-O": {"type": "number"}, "Sn(trop)": {"type": "number"}}}, "derivatives": {"type": "object", "required": ["Cl2Sn(trop)2", "(CH3)2Sn(trop)2", "(C6H5)2Sn(trop)2"], "properties": {"Cl2Sn(trop)2": {"type": "object", "required": ["trans_D2h", "cis_C2", "cis_C2v"], "properties": {"trans_D2h": {"type": "object", "required": ["b1_minus_b2", "b1_minus_b3", "molar_Kerr"], "properties": {"b1_minus_b2": {"type": "number", "unit": "1e-24 cm^3"}, "b1_minus_b3": {"type": "number", "unit": "1e-24 cm^3"}, "molar_Kerr": {"type": "number", "unit": "1e-12 cgs"}}}, "cis_C2": {"$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2/properties/trans_D2h"}, "cis_C2v": {"$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2/properties/trans_D2h"}}}, "(CH3)2Sn(trop)2": {"$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2"}, "(C6H5)2Sn(trop)2": {"$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2"}}}, "group_moments": {"type": "object", "required": ["Cl2Sn(trop)2", "(CH3)2Sn(trop)2", "(C6H5)2Sn(trop)2"], "properties": {"Cl2Sn(trop)2": {"type": "number", "unit": "D"}, "(CH3)2Sn(trop)2": {"type": "number", "unit": "D"}, "(C6H5)2Sn(trop)2": {"type": "number", "unit": "D"}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Consolidated scored artifact containing all quantities derived from the computational workflow: the tropolone optical anisotropy, bond/group polarizability anisotropies, molecular polarizability differences and molar Kerr constants for every candidate structure of each tin tropolonate derivative, and the derived group dipole moments.
- schema:
  - `type`: object
  - `required`: `tropolone_anisotropy`, `bond_anisotropies`, `derivatives`, `group_moments`
  - `properties`:
    - `tropolone_anisotropy`:
      - `type`: number
      - `unit`: 1e-24 cm^3
    - `bond_anisotropies`:
      - `type`: object
      - `required`: `Sn-Cl`, `Sn-CH3`, `Sn-O`, `Sn(trop)`
      - `properties`:
        - `Sn-Cl`:
          - `type`: number
          - `unit`: 1e-24 cm^3
        - `Sn-CH3`:
          - `type`: number
          - `unit`: 1e-24 cm^3
        - `Sn-O`:
          - `type`: number
          - `unit`: 1e-24 cm^3
        - `Sn(trop)`:
          - `type`: number
          - `unit`: 1e-24 cm^3
    - `derivatives`:
      - `type`: object
      - `required`: `Cl2Sn(trop)2`, `(CH3)2Sn(trop)2`, `(C6H5)2Sn(trop)2`
      - `properties`:
        - `Cl2Sn(trop)2`:
          - `type`: object
          - `required`: `trans_D2h`, `cis_C2`, `cis_C2v`
          - `properties`:
            - `trans_D2h`:
              - `type`: object
              - `required`: `b1_minus_b2`, `b1_minus_b3`, `molar_Kerr`
              - `properties`:
                - `b1_minus_b2`:
                  - `type`: number
                  - `unit`: 1e-24 cm^3
                - `b1_minus_b3`:
                  - `type`: number
                  - `unit`: 1e-24 cm^3
                - `molar_Kerr`:
                  - `type`: number
                  - `unit`: 1e-12 cgs
            - `cis_C2`:
              - `$ref`: #/properties/derivatives/properties/Cl2Sn(trop)2/properties/trans_D2h
            - `cis_C2v`:
              - `$ref`: #/properties/derivatives/properties/Cl2Sn(trop)2/properties/trans_D2h
        - `(CH3)2Sn(trop)2`:
          - `$ref`: #/properties/derivatives/properties/Cl2Sn(trop)2
        - `(C6H5)2Sn(trop)2`:
          - `$ref`: #/properties/derivatives/properties/Cl2Sn(trop)2
    - `group_moments`:
      - `type`: object
      - `required`: `Cl2Sn(trop)2`, `(CH3)2Sn(trop)2`, `(C6H5)2Sn(trop)2`
      - `properties`:
        - `Cl2Sn(trop)2`:
          - `type`: number
          - `unit`: D
        - `(CH3)2Sn(trop)2`:
          - `type`: number
          - `unit`: D
        - `(C6H5)2Sn(trop)2`:
          - `type`: number
          - `unit`: D

Notes: The hidden checker will compare each numeric field against the paper's reported gold values using appropriate absolute tolerances. The structural schema must be strictly adhered to; missing or extra fields will result in zero credit for the corresponding entry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "tropolone_anisotropy",
          "bond_anisotropies",
          "derivatives",
          "group_moments"
        ],
        "properties": {
          "tropolone_anisotropy": {
            "type": "number",
            "unit": "1e-24 cm^3"
          },
          "bond_anisotropies": {
            "type": "object",
            "required": [
              "Sn-Cl",
              "Sn-CH3",
              "Sn-O",
              "Sn(trop)"
            ],
            "properties": {
              "Sn-Cl": {
                "type": "number",
                "unit": "1e-24 cm^3"
              },
              "Sn-CH3": {
                "type": "number",
                "unit": "1e-24 cm^3"
              },
              "Sn-O": {
                "type": "number",
                "unit": "1e-24 cm^3"
              },
              "Sn(trop)": {
                "type": "number",
                "unit": "1e-24 cm^3"
              }
            }
          },
          "derivatives": {
            "type": "object",
            "required": [
              "Cl2Sn(trop)2",
              "(CH3)2Sn(trop)2",
              "(C6H5)2Sn(trop)2"
            ],
            "properties": {
              "Cl2Sn(trop)2": {
                "type": "object",
                "required": [
                  "trans_D2h",
                  "cis_C2",
                  "cis_C2v"
                ],
                "properties": {
                  "trans_D2h": {
                    "type": "object",
                    "required": [
                      "b1_minus_b2",
                      "b1_minus_b3",
                      "molar_Kerr"
                    ],
                    "properties": {
                      "b1_minus_b2": {
                        "type": "number",
                        "unit": "1e-24 cm^3"
                      },
                      "b1_minus_b3": {
                        "type": "number",
                        "unit": "1e-24 cm^3"
                      },
                      "molar_Kerr": {
                        "type": "number",
                        "unit": "1e-12 cgs"
                      }
                    }
                  },
                  "cis_C2": {
                    "$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2/properties/trans_D2h"
                  },
                  "cis_C2v": {
                    "$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2/properties/trans_D2h"
                  }
                }
              },
              "(CH3)2Sn(trop)2": {
                "$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2"
              },
              "(C6H5)2Sn(trop)2": {
                "$ref": "#/properties/derivatives/properties/Cl2Sn(trop)2"
              }
            }
          },
          "group_moments": {
            "type": "object",
            "required": [
              "Cl2Sn(trop)2",
              "(CH3)2Sn(trop)2",
              "(C6H5)2Sn(trop)2"
            ],
            "properties": {
              "Cl2Sn(trop)2": {
                "type": "number",
                "unit": "D"
              },
              "(CH3)2Sn(trop)2": {
                "type": "number",
                "unit": "D"
              },
              "(C6H5)2Sn(trop)2": {
                "type": "number",
                "unit": "D"
              }
            }
          }
        }
      },
      "description": "Consolidated scored artifact containing all quantities derived from the computational workflow: the tropolone optical anisotropy, bond/group polarizability anisotropies, molecular polarizability differences and molar Kerr constants for every candidate structure of each tin tropolonate derivative, and the derived group dipole moments."
    }
  ],
  "notes": "The hidden checker will compare each numeric field against the paper's reported gold values using appropriate absolute tolerances. The structural schema must be strictly adhered to; missing or extra fields will result in zero credit for the corresponding entry."
}
```

## How you are scored
After you submit your output, a hidden verifier will inspect `computed_results.json`. It will independently compare each numeric field against a hidden set of reference values using predefined absolute tolerances. The score for each field contributes a weighted fraction to the overall reward; fields that are missing, malformed, or outside the allowed tolerance receive zero contribution. The final reward is a single number between 0 and 1. The verifier checks numerical accuracy, not just the presence of the file. You must produce a complete JSON according to the specified schema; any field omitted or incorrectly typed will incur zero credit.
