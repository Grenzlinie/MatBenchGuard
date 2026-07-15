# Compute VDE and HOMO-LUMO gap of ScSi16- and LuSi16- by DFT

## Problem background
Metal-doped silicon clusters (MSi_n^-) exhibit size-selective electronic properties due to a cooperative interplay between their geometric cage structures and electronic shell closures. Among them, the Frank-Kasper (T_d) cage encapsulating a metal atom at n=16 is a candidate for a stable "superatom" building block. A key signature of this stabilization is the vertical detachment energy (VDE) and the HOMO-LUMO gap of the anionic clusters, which can be accessed computationally by density functional theory (DFT). This task focuses on computing these electronic descriptors for two representative clusters, ScSi16^- and LuSi16^-, to evaluate their energetic signatures of cage encapsulation.

## Approach
The computation follows ab initio DFT with the B3PW91 hybrid functional. The Si, Sc, and Lu atoms are described by large-core Stuttgart quasi-relativistic effective core potentials (Stuttgart RLC ECPs) with a polarization function on Si, as is standard for such clusters. Starting from a Frank-Kasper Si16 cage structure with the metal atom at the center, a full geometry optimization of the anionic cluster is performed, followed by a vibrational frequency analysis to confirm a minimum. Using the optimized anion geometry, the vertical detachment energy (VDE) is evaluated via the ΔDFT method as the energy difference between the neutral cluster at the anion geometry and the anionic cluster. The HOMO-LUMO gap of the neutral cluster is then computed using time-dependent DFT (TD-B3PW91) at the same geometry. This protocol is repeated for both ScSi16^- and LuSi16^-.

## Reproduction target
Compute the VDE and HOMO-LUMO gap for ScSi16^- and LuSi16^- using the DFT/B3PW91/Stuttgart RLC ECP protocol described above, starting from the Frank-Kasper cage geometry. Report the results in a JSON file /app/outputs/results.json, which must contain for each cluster the anion total energy (E_anion_Ha), the neutral total energy at the anion geometry (E_neutral_Ha), the VDE in eV, and the HOMO-LUMO gap in eV. The checker will independently verify these quantities and assess the quality of the reproduction.

## Assets

- Frank-Kasper Si16 cage geometry reference: https://doi.org/10.1103/PhysRevLett.87.045503
- Stuttgart RLC ECP basis sets for Sc, Lu, Si: https://www.quantumchemistry.pd.chemie.tu-darmstadt.de/basissets/
- Open-source quantum chemistry code (e.g., ORCA): https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Prepare initial Frank-Kasper geometry
- Role: process
- Action: Obtain or construct Frank-Kasper Td Si16 cage coordinates with central metal atom (Sc and Lu) from literature (Kumar & Kawazoe, PRL 2001) and generate input files for DFT geometry optimization of the anionic clusters ScSi16- and LuSi16-.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: DFT geometry optimization and frequency analysis
- Role: process
- Action: Perform full geometry optimization of ScSi16- and LuSi16- at the B3PW91/Stuttgart RLC ECP level. Verify that the optimized structures are true minima via vibrational frequency analysis (no imaginary frequencies). Save output log.
- Evidence: `/app/outputs/opt_freq_output.log`

### Step 3: Compute VDE and HOMO-LUMO gap
- Role: scored (load-bearing)
- Action: Using the optimized anion geometries, compute the vertical detachment energy (VDE) as the ΔDFT energy difference E(neutral at anion geometry) - E(anion) via single-point calculations, and the neutral HOMO-LUMO gap via TD-B3PW91. Write all results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "ScSi16-": {
    "E_anion_Ha": <float>,
    "E_neutral_Ha": <float>,
    "VDE_eV": <float>,
    "HOMO_LUMO_gap_eV": <float>
  },
  "LuSi16-": {
    "E_anion_Ha": <float>,
    "E_neutral_Ha": <float>,
    "VDE_eV": <float>,
    "HOMO_LUMO_gap_eV": <float>
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed VDE and HOMO-LUMO gap for ScSi16- and LuSi16- clusters. The checker recomputes VDE from the provided E_anion_Ha and E_neutral_Ha, and verifies HOMO-LUMO gap structural validity (≥1.5 eV, consistency).
- schema:
  - `type`: object
  - `required`:
    - `ScSi16-`:
      - `E_anion_Ha`: float
      - `E_neutral_Ha`: float
      - `VDE_eV`: float
      - `HOMO_LUMO_gap_eV`: float
    - `LuSi16-`:
      - `E_anion_Ha`: float
      - `E_neutral_Ha`: float
      - `VDE_eV`: float
      - `HOMO_LUMO_gap_eV`: float
  - `units`:
    - `E_anion_Ha`: Hartree
    - `E_neutral_Ha`: Hartree
    - `VDE_eV`: eV
    - `HOMO_LUMO_gap_eV`: eV

Notes: Only the DFT‐computed part of the paper is targeted. Experimental spectra and adsorption reactivity are not in scope. The agent must run geometry optimization and single‐point calculations; moderate CPU time is expected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "ScSi16-": {
            "E_anion_Ha": "float",
            "E_neutral_Ha": "float",
            "VDE_eV": "float",
            "HOMO_LUMO_gap_eV": "float"
          },
          "LuSi16-": {
            "E_anion_Ha": "float",
            "E_neutral_Ha": "float",
            "VDE_eV": "float",
            "HOMO_LUMO_gap_eV": "float"
          }
        },
        "units": {
          "E_anion_Ha": "Hartree",
          "E_neutral_Ha": "Hartree",
          "VDE_eV": "eV",
          "HOMO_LUMO_gap_eV": "eV"
        }
      },
      "description": "Computed VDE and HOMO-LUMO gap for ScSi16- and LuSi16- clusters. The checker recomputes VDE from the provided E_anion_Ha and E_neutral_Ha, and verifies HOMO-LUMO gap structural validity (≥1.5 eV, consistency)."
    }
  ],
  "notes": "Only the DFT‐computed part of the paper is targeted. Experimental spectra and adsorption reactivity are not in scope. The agent must run geometry optimization and single‐point calculations; moderate CPU time is expected."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the artifacts you write to /app/outputs. The verifier extracts the total energies from results.json and recomputes the VDE as the difference. It then compares the recomputed VDE against a hidden reference, using tolerances appropriate for the method's expected numerical spread. The HOMO-LUMO gap is checked for structural validity (plausible magnitude and consistency between the two clusters). Each scored step contributes a weighted share to a final reward between 0 and 1; reporting a single number without the underlying calculation evidence will not earn full credit.
