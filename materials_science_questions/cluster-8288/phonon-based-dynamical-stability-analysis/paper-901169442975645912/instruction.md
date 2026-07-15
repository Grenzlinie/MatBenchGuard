# Phonon-mediated superconductivity and dynamical instability in Y2C3

## Problem background
Y2C3 is a known superconductor; its high-symmetry body-centered cubic I-43d structure exhibits dynamical instability, manifested as zone-center imaginary phonon modes. These modes originate from a flat electronic band near the Fermi level. Following the imaginary eigenvector to distort and fully relax the lattice to a low-symmetry P1 structure stabilizes the phonons, and the previously unstable low-energy modes then carry strong electron-phonon coupling, giving rise to the superconducting critical temperature. Understanding this instability-to-superconductivity mechanism is important for high-throughput searches that would otherwise discard compounds with computed imaginary modes. Your task is to reproduce the key computational results that demonstrate the origin and stabilization of the dynamical instability and its connection to superconductivity.

## Approach
This is a compute-driven reproduction using density functional theory (DFT) and density functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO, with the PBE exchange-correlation functional and standard ultrasoft pseudopotentials. You will start from the primitive I-43d structure of Y2C3, fully relax it, then compute its phonon dispersion and electronic band structure to identify any imaginary (negative) phonon modes and check for the presence of a flat band along the Γ–N direction. Next, you will displace the atoms along the eigenvector of one of the prominent imaginary modes, fully relax the distorted structure to obtain the P1 phase, and then compute its phonon dispersion to confirm dynamical stability. Finally, you will interpolate the electron-phonon coupling matrices on a fine grid and derive the isotropic Eliashberg spectral function α²F(ω), from which you extract the integrated electron-phonon coupling strength λ, the logarithmic average phonon frequency ω_log, and the superconducting critical temperature Tc using the McMillan-Allen-Dynes formula with a Coulomb pseudopotential μ* = 0.16. The results reveal the transformation from an unstable high-symmetry phase to a stable low-symmetry superconductor.

## Reproduction target
You will produce two scored artifacts. (1) For the relaxed I-43d structure, provide a JSON file containing a list of zone-center imaginary phonon frequencies (in cm⁻¹), a boolean indicating whether a flat band exists within 10 meV of the Fermi level along the Γ–N path, and the band energies at Γ and N (in eV) for that band. (2) For the relaxed P1 structure, provide a JSON file with the lowest phonon frequency at Γ (in THz), the electron-phonon coupling strength λ (dimensionless), the logarithmic average phonon frequency ω_log (in K), and the superconducting critical temperature Tc (in K).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Y and C (PBE): SSSP PBE efficiency 1.3.0
- Initial Y2C3 I-43d crystal structure: Materials Project mp-1199623

## Workflow steps

### Step 1: Relax I-43d Y2C3 primitive cell
- Role: process
- Action: Relax the atomic positions and cell parameters of the initial I-43d structure using DFT (PBE, ultrasoft pseudopotentials, kinetic energy cutoff 50 Ry, 6×6×6 k‑mesh, Gaussian smearing 0.05 eV).
- Evidence: `/app/outputs/relax.log`

### Step 2: Compute phonon and flat band of I-43d
- Role: scored
- Action: Using the relaxed I-43d structure, perform an SCF calculation, then a DFPT phonon calculation on a 2×2×2 q‑grid to obtain phonon frequencies, and compute the electronic band structure along the Γ–N path. Extract the list of zone‑center phonon frequencies, identify any imaginary (negative) modes, and determine whether a flat band exists within 10 meV of EF; record the band energies at Γ and N for that band.
- Output file: `/app/outputs/step_01_I43d_results.json`
- Format: json
- Contract: {"imaginary_phonon_freqs_cm-1": [float, ...], "flat_band_present": bool, "band_edges_Gamma_N_eV": {"Gamma": float, "N": float}}
- Scoring: scored by hidden verifier

### Step 3: Distort and relax to P1 structure
- Role: process
- Action: From the DFPT output of step1, obtain the eigenvector of imaginary mode 4. Displace the I-43d atomic positions along this eigenvector and fully relax both atomic positions and cell parameters (same DFT settings) to obtain the low‑symmetry P1 structure.
- Evidence: `/app/outputs/p1_relax.log`

### Step 4: Compute phonon and EPC of P1 structure
- Role: scored (load-bearing)
- Action: On the relaxed P1 structure, perform an SCF calculation, then a DFPT phonon calculation on a 2×2×2 q‑grid to verify dynamical stability (no imaginary modes). Afterwards, interpolate to a fine 12×12×12 k‑ and q‑grid and compute the isotropic Eliashberg spectral function α²F(ω). From α²F(ω) derive the integrated electron‑phonon coupling strength λ, the logarithmic average phonon frequency ω_log, and the superconducting critical temperature Tc using the McMillan‑Allen‑Dynes formula with Coulomb pseudopotential μ* = 0.16.
- Output file: `/app/outputs/step_02_P1_results.json`
- Format: json
- Contract: {"lowest_phonon_freq_Gamma_THz": float, "lambda_epc": float, "omega_log_K": float, "Tc_K": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_I43d_results.json`
- `/app/outputs/step_02_P1_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_I43d_results.json
- path: `/app/outputs/step_01_I43d_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Imaginary phonon modes and flat band presence in the high-symmetry I-43d structure.
- schema:
  - `type`: object
  - `required`:
    - `imaginary_phonon_freqs_cm-1`: list of floats (cm⁻¹)
    - `flat_band_present`: boolean
    - `band_edges_Gamma_N_eV`: object with keys Gamma, N (float, eV)

### step_02_P1_results.json
- path: `/app/outputs/step_02_P1_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electron-phonon coupling quantities and Tc for the stabilized P1 structure, compared to paper reference values.
- schema:
  - `type`: object
  - `required`:
    - `lowest_phonon_freq_Gamma_THz`: float (THz)
    - `lambda_epc`: float (dimensionless)
    - `omega_log_K`: float (K)
    - `Tc_K`: float (K)

Notes: The paper also reports results under pressure (20, 30 GPa), with large electronic smearing, and for several other compounds. Those are explicitly excluded from the reproduction scope to keep the task focused.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_I43d_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "imaginary_phonon_freqs_cm-1": "list of floats (cm⁻¹)",
          "flat_band_present": "boolean",
          "band_edges_Gamma_N_eV": "object with keys Gamma, N (float, eV)"
        }
      },
      "description": "Imaginary phonon modes and flat band presence in the high-symmetry I-43d structure."
    },
    {
      "file": "step_02_P1_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lowest_phonon_freq_Gamma_THz": "float (THz)",
          "lambda_epc": "float (dimensionless)",
          "omega_log_K": "float (K)",
          "Tc_K": "float (K)"
        }
      },
      "description": "Electron-phonon coupling quantities and Tc for the stabilized P1 structure, compared to paper reference values."
    }
  ],
  "notes": "The paper also reports results under pressure (20, 30 GPa), with large electronic smearing, and for several other compounds. Those are explicitly excluded from the reproduction scope to keep the task focused."
}
```

## How you are scored
The hidden verifier evaluates each scored output independently and combines the scores into a final reward between 0 and 1. For the I-43d results, the verifier checks that the reported phonon frequencies include negative (imaginary) modes and that the flat-band flag is true, and it verifies that the band-edge energies are plausible. For the P1 results, the verifier compares your reported λ, ω_log, and Tc against hidden reference values, awarding higher credit the closer your results are to the expected values; this uses a graded scale, not a pass/fail threshold. Reporting the paper’s numbers is not sufficient – the workflow must be executed to produce the required artifacts.
