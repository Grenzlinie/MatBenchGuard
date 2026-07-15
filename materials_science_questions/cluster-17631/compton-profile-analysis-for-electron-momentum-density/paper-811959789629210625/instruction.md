# Compton Profile Analysis of PbS and PbSe with SPR-KKR

## Problem background
Lead chalcogenides PbS and PbSe are narrow‑gap IV‑VI semiconductors with important technological applications. Their electronic structure and electron momentum density can be probed by Compton scattering, which provides a one‑dimensional projection of the ground‑state momentum distribution. By scaling the valence Compton profiles to equal‑valence‑electron‑density (EVED), the degree of covalency in these isoelectronic compounds can be compared. This work aims to compute the band gaps, total Compton profiles, and EVED‑scale profiles for both materials and to assess the relative covalency trend.

## Approach
The electronic structure is calculated with the spin‑polarized relativistic Korringa‑Kohn‑Rostoker (SPR‑KKR) method in the atomic‑sphere‑approximation mode. Self‑consistent field runs are performed for rock‑salt PbS and PbSe using lattice constants from standard references, muffin‑tin radii given in the literature, and the Vosko‑Wilk‑Nusair local density approximation for exchange‑correlation. From the converged potential, directional valence Compton profiles along [100], [110] and [111] are computed, spherically averaged, and combined with free‑atom core profiles (Biggs et al. 1975) to obtain total Compton profiles. Band gaps at the L and Gamma points are extracted from the Kohn‑Sham eigenvalues. Finally, the valence profiles are separated from the core, normalized to five valence electrons, and scaled by the Fermi momentum to produce EVED profiles on a pz/pF scale, allowing a comparison of the relative covalency of the two compounds.

## Reproduction target
Produce three CSV files under /app/outputs:

1. band_gaps.csv – contains the band gaps (in eV) at the L and Gamma points for PbS and PbSe.
2. compton_profiles.csv – lists the total spherically averaged Compton profiles (e/a.u.) for both compounds on a grid of momenta from 0.0 to 7.0 a.u.
3. eved_profiles.csv – gives the EVED‑normalized Compton profiles (e/a.u.) for PbS and PbSe as functions of pz/pF.

From the EVED profiles, determine which compound exhibits a higher J(pz) at low momentum, and therefore which is more covalent.

## Assets

- SPR-KKR code (Munich SPR-KKR package v3.6): url: http://ebert.cup.uni-muenchen.de/SPRKKR
- Free-atom Compton profiles (Biggs et al. 1975): doi: 10.1016/0092-640X(75)90038-6

## Workflow steps

### Step 1: Prepare crystal structures and SPR-KKR inputs for PbS and PbSe
- Role: process
- Action: Create SPR-KKR input files for rock-salt PbS (a=5.636 Å) and PbSe (a=6.124 Å) with space group Fm-3m. Set muffin-tin radii as specified: Pb 3.213 Å, S 2.396 Å for PbS; Pb 3.193 Å, Se 2.593 Å for PbSe. Use l_max=2, 834 k-points in 1/48th BZ, and Vosko-Wilk-Nusair LDA exchange-correlation.
- Evidence: none

### Step 2: Run SPR-KKR SCF calculations for PbS and PbSe
- Role: process
- Action: Execute SPR-KKR self-consistent field (SCF) calculations for PbS and PbSe to convergence, obtaining the self-consistent potential, eigenvalues, and wavefunctions.
- Evidence: none

### Step 3: Extract band gaps at L and Gamma points
- Role: scored (load-bearing)
- Action: From the SCF results, extract the eigenvalues at the L and Gamma points for each compound and compute the band gaps (difference between conduction band minimum and valence band maximum at those points). Write the values to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: compound (string, 'PbS' or 'PbSe'), Eg_L (float, eV), Eg_Gamma (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute directional Compton profiles and total spherical profiles
- Role: process
- Action: Using SPR-KKR, compute valence directional Compton profiles J(pz) along [100], [110], [111] for each compound. Spherical average these profiles to obtain the valence Compton profile. Add free-atom core contribution from Biggs et al. tables to obtain the total spherically averaged Compton profile.
- Evidence: none

### Step 5: Output total Compton profiles
- Role: scored (load-bearing)
- Action: Write the total spherically averaged Compton profiles to compton_profiles.csv for p_z values: 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0 a.u.
- Output file: `/app/outputs/compton_profiles.csv`
- Format: csv
- Contract: CSV with columns: compound (string), p_z (float, a.u.), J_total (float, e/a.u.).
- Scoring: scored by hidden verifier

### Step 6: Generate EVED profiles and compare covalency
- Role: process
- Action: For each compound, subtract core contribution from total profile to obtain valence Compton profile. Calculate p_F from valence electron density (valence electrons per unit cell divided by volume). Normalize valence profile to 5 electrons integrated over 0–7 a.u., then scale momentum by p_F to obtain EVED profile J_EVED(p_z/p_F).
- Evidence: none

### Step 7: Output EVED profiles
- Role: scored
- Action: Write the EVED profiles to eved_profiles.csv for a grid of p_z/p_F values (e.g., 0.0 to ~2.0 in 0.1 steps). Include J_EVED for PbS and PbSe.
- Output file: `/app/outputs/eved_profiles.csv`
- Format: csv
- Contract: CSV with columns: p_z_over_pF (float), J_PbS (float, e/a.u.), J_PbSe (float, e/a.u.).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/compton_profiles.csv`
- `/app/outputs/eved_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Band gaps at L and Gamma points computed by SPR-KKR for PbS and PbSe. Compared to hidden paper SPR-KKR values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `Eg_L`, `Eg_Gamma`
  - `units`:
    - `Eg_L`: eV
    - `Eg_Gamma`: eV

### compton_profiles.csv
- path: `/app/outputs/compton_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total spherically averaged Compton profiles at specified p_z points. Checker computes mean absolute deviation against hidden paper SPR-KKR profiles.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `p_z`, `J_total`
  - `units`:
    - `p_z`: a.u.
    - `J_total`: e/a.u.

### eved_profiles.csv
- path: `/app/outputs/eved_profiles.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: EVED profiles for PbS and PbSe. The checker verifies the structural trend that J(0) for PbSe is greater than J(0) for PbS, confirming PbSe is more covalent.
- schema:
  - `type`: table
  - `required_columns`: `p_z_over_pF`, `J_PbS`, `J_PbSe`
  - `units`:
    - `p_z_over_pF`: dimensionless
    - `J_PbS`: e/a.u.
    - `J_PbSe`: e/a.u.

Notes: The total Compton profiles and band gaps are compared against hidden SPR-KKR reference values from the paper. The EVED trend is verified from the agent's submitted profiles.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "Eg_L",
          "Eg_Gamma"
        ],
        "units": {
          "Eg_L": "eV",
          "Eg_Gamma": "eV"
        }
      },
      "description": "Band gaps at L and Gamma points computed by SPR-KKR for PbS and PbSe. Compared to hidden paper SPR-KKR values within tolerance."
    },
    {
      "file": "compton_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "p_z",
          "J_total"
        ],
        "units": {
          "p_z": "a.u.",
          "J_total": "e/a.u."
        }
      },
      "description": "Total spherically averaged Compton profiles at specified p_z points. Checker computes mean absolute deviation against hidden paper SPR-KKR profiles."
    },
    {
      "file": "eved_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_z_over_pF",
          "J_PbS",
          "J_PbSe"
        ],
        "units": {
          "p_z_over_pF": "dimensionless",
          "J_PbS": "e/a.u.",
          "J_PbSe": "e/a.u."
        }
      },
      "description": "EVED profiles for PbS and PbSe. The checker verifies the structural trend that J(0) for PbSe is greater than J(0) for PbS, confirming PbSe is more covalent."
    }
  ],
  "notes": "The total Compton profiles and band gaps are compared against hidden SPR-KKR reference values from the paper. The EVED trend is verified from the agent's submitted profiles."
}
```

## How you are scored
A hidden verifier independently checks each artifact. The band‑gap values are compared to reference data, the total Compton profiles are evaluated against a hidden reference set (a mean absolute deviation criterion), and the EVED profiles are inspected for the structural trend that one compound’s J(0) is larger than the other’s. All checks must pass; the verifier combines the outcomes into a single reward between 0 and 1. The instruction does not contain the expected numerical values or tolerances – the goal is to obtain them by running the computational workflow described above.
