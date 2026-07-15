## Problem background

Accurate prediction of quasiparticle (band) energies in semiconductors requires proper treatment of exchange and correlation between core and valence electrons. In post-transition elements like Ga and Ge, a standard local-density approximation (LDA) for core-valence interactions overbinds s states relative to p states, leading to errors ~0.4 eV in key band-energy differences even when valence-valence effects are treated in the GW approximation. The core-polarization-potential (CPP) method addresses this by adding one- and two-electron operators to the valence Hamiltonian that capture core dipole polarizability and core-valence correlation, while retaining exact Hartree-Fock core-valence exchange. This task reproduces quasiparticle band-energy differences for Si, Ge, GaAs, and AlAs using the CPP-augmented GW approach.

## Approach

The workflow combines atomistic pseudopotential generation, plane-wave LDA calculations, and a modified GW implementation that incorporates core-polarization effects.

- **Pseudopotentials:**
  Norm-conserving Hamann-Schlüter-Chiang pseudopotentials with Vanderbilt cutoff functions are generated for Al, Si, Ga, Ge, and As. Two sets are needed:
  1. LDA pseudopotentials, using the local-density approximation for exchange-correlation.
  2. Hartree-Fock pseudopotentials, where the nonlocal Fock exchange is replaced by an equivalent orbital-dependent local potential to achieve exact Hartree-Fock atomic results.
  The reference configurations and cutoff radii (in bohr) are:

| Element | Reference config. | s r_c | p r_c | d r_c |
|---|---|---|---|---|
| Al | s¹p⁰·⁵d⁰·⁵ | 1.3 | 1.3 | 1.3 |
| Si | s¹p¹·⁵d⁰·⁵ | 1.4 | 1.4 | 1.3 |
| Ga | s¹p⁰·³d⁰·⁷ | 1.5 | 1.5 | 1.45 |
| Ge | s¹p¹·⁵d⁰·⁵ | 1.4 | 1.4 | 1.3 |
| As | s¹p²·⁵d⁰·⁵ | 1.3 | 1.3 | 1.3 |

  The semilocal pseudopotentials use l=2 as the local channel.

- **CPP parameters:**
  The one-electron core-polarization potential V_e and two-electron potential V_e-e depend on linear, static core dipole polarizabilities α and angular-momentum-dependent cutoff lengths λ^{(l)}. These are taken from the published data (Table I of the source) and are:

| Element | α (bohr³) | λ^{(0)} | λ^{(1)} | λ^{(2)} |
|---|---|---|---|---|
| Al | 0.2675 | 0.7129 | 0.6969 | 0.7207 |
| Si | 0.1650 | 0.6509 | 0.6214 | 0.6387 |
| Ga | 1.3147 | 0.9996 | 1.0008 | 1.1552 |
| Ge | 0.7772 | 0.8633 | 0.8552 | 0.8248 |
| As | 0.4833 | 0.7475 | 0.7301 | 0.6786 |

  The two-electron truncation length Λ is the arithmetic mean of λ^{(0)} and λ^{(1)}. For l≥3 use λ^{(2)}.

- **Crystal structures:**
  Si and Ge are in the diamond structure; GaAs and AlAs are in the zinc-blende structure. Use experimental lattice constants: Si 5.43 Å, Ge 5.65 Å, GaAs 5.653 Å, AlAs 5.660 Å.

- **LDA band structure:**
  Self-consistent LDA calculations are performed for each solid using the Hartree-Fock pseudopotentials, a plane-wave basis (wavefunction cutoff 16 Ry, potential cutoff 64 Ry), the Ceperley-Alder exchange-correlation functional, and a 10-point special k-point set. The output provides LDA wavefunctions and eigenvalues that serve as the starting point for GW.

- **CPP-GW implementation:**
  An open-source GW code (e.g., BerkeleyGW or Yambo) is extended to incorporate core-polarization effects:
  * The core screening matrix ε_C⁻¹ is computed from CPP parameters via Ewald-Kornfeld dipole sums:
    - For each atom I, define the truncation function f(x)=[1−exp(−x²)]² and the two-electron cut-off length Λ_I = ½(λ^{(0)} + λ^{(1)}).
    - For each G+q vector Q, compute the form factor J_I(Q) = ∫₀^∞ dr (sin(Qr)/(Qr)) d/dr f(r/Λ_I).
    - The coupling vector is Θ_{Ii}(Q) = √(4π/Ω_C) (Q_i/Q) J_I(Q) exp(−i Q·τ_I).
    - Build the 3N×3N dipole-interaction matrix M_{Ii,Jj} using standard Ewald-Kornfeld sums for the dipolar lattice (including self-term and inter-site contributions, omitting intracore dipole self-interaction).
    - Form K_{Ii,Jj} = α_I^{-1} δ_{Ii,Jj} − M_{Ii,Jj}.
    - Invert K and construct the core screening matrix: ε_C⁻¹_{G,G′}(q) = (Q′/Q)[δ_{G,G′} − Σ_{Ii,Jj} Θ_{Ii}(Q) (K⁻¹)_{Ii,Jj} Θ^*_{Jj}(Q′)].
  * The full microscopic dielectric matrix is constructed as ε = ε_C − ν χ_V⁰.
  * The generalized plasmon-pole model is modified to account for the replacement ν → W_C = ε_C⁻¹ ν in the Kramers-Kronig sum rules.
  * The self-energy Σ consists of exchange (Σ_x), dynamic exchange (Σ_dx), and Coulomb-hole (Σ_coh) terms that are modified appropriately.

- **Quasiparticle energies:**
  For each material, compute quasiparticle energies at the Γ, X, and L points using the CPP-GW method with rigid-shift corrections, LDA wavefunctions, and Hartree-Fock pseudopotentials. Spin-orbit splittings may be added a posteriori.

- **Band-energy differences:**
  From the quasiparticle energies, extract the following transition energies (all in eV) and write them to JSON files.

## Reproduction target

Compute the CPP-augmented GW quasiparticle band-energy differences for Si, Ge, GaAs, and AlAs and output the specified transition energies into four JSON files.

## Assets

- Quantum ESPRESSO (pw.x, ld1.x) – open-source DFT suite for pseudopotential generation and plane-wave calculations (https://www.quantum-espresso.org/).
- An open-source GW implementation that can be modified (e.g., BerkeleyGW https://berkeleygw.org/ or Yambo https://www.yambo-code.org/).
- The pseudopotential and CPP parameters are listed above in the Approach section.

## Workflow steps

### Step 1: Generate LDA pseudopotentials
- Role: process
- Action: Generate norm-conserving LDA pseudopotentials for Al, Si, Ga, Ge, As using the reference configurations and cutoff radii given in the Approach. Use the Hamann-Schlüter-Chiang scheme with Vanderbilt cutoff functions and semilocal form.
- Evidence: `/app/outputs/lda_pp_generation.log`

### Step 2: Generate Hartree-Fock pseudopotentials
- Role: process
- Action: Generate norm-conserving Hartree-Fock pseudopotentials for the same five elements with the same reference configurations and cutoff radii. Ensure that the nonlocal Fock exchange is treated via an equivalent local potential to obtain exact Hartree-Fock atomic results.
- Evidence: `/app/outputs/hf_pp_generation.log`

### Step 3: LDA band structure calculations with Hartree-Fock pseudopotentials
- Role: process
- Action: For Si, Ge, GaAs, and AlAs, perform self-consistent LDA calculations using the Hartree-Fock pseudopotentials, experimental lattice constants, and the plane-wave parameters described in the Approach. Output the self-consistent charge density and Kohn-Sham wavefunctions.
- Evidence: `/app/outputs/lda_bandstructure.log`

### Step 4: Implement CPP-modified GW code
- Role: process
- Action: Extend a chosen GW code with the CPP formalism. Implement the computation of the core screening matrix ε_C⁻¹ via Ewald-Kornfeld sums, modify the dielectric response and self-energy expressions as described in the Approach, and build the modified code.
- Evidence: `/app/outputs/cpp_gw_modifications.txt`

### Step 5: Run CPP-GW quasiparticle calculations
- Role: process
- Action: For Si, Ge, GaAs, and AlAs, run the CPP-augmented GW code using the LDA wavefunctions from Step 3, the Hartree-Fock pseudopotentials, and the CPP parameters from the Approach. Compute quasiparticle energies at Γ, X, and L high-symmetry points. (Spin-orbit splittings may be added a posteriori as done in the paper.)
- Evidence: `/app/outputs/gw_run.log`

### Step 6: Extract Si band-energy differences (scored)
- Role: scored
- Action: From the Si quasiparticle energies, compute and write the following band-energy differences to `Si_bands.json`:
  - Γ_{8v} → Γ_{6c} (Gamma_to_Gamma)
  - Γ_{8v} → X_{5c} (Gamma_to_X)
  - Γ_{8v} → L_{6c} (Gamma_to_L)
  - L_{6c} → X_{5c} (L_to_X)
  - Fundamental band gap E_g (Eg)
  All values in eV.
- Output file: `/app/outputs/Si_bands.json`
- Format: json
- Contract: Keys "Gamma_to_Gamma", "Gamma_to_X", "Gamma_to_L", "L_to_X", "Eg" (all numbers, eV).
- Scoring: scored by hidden verifier.

### Step 7: Extract Ge band-energy differences (scored)
- Role: scored
- Action: From the Ge quasiparticle energies, compute and write to `Ge_bands.json`:
  - Γ_{8v} → Γ_{7c} (Gamma_to_Gamma, direct gap)
  - Γ_{8v} → X_{5c} (Gamma_to_X)
  - Γ_{8v} → L_{6c} (Gamma_to_L)
  - L_{6c} → X_{5c} (L_to_X)
  - Fundamental band gap E_g (Eg)
  All values in eV.
- Output file: `/app/outputs/Ge_bands.json`
- Format: json
- Contract: Keys "Gamma_to_Gamma", "Gamma_to_X", "Gamma_to_L", "L_to_X", "Eg" (all numbers, eV).
- Scoring: scored by hidden verifier.

### Step 8: Extract GaAs band-energy differences (scored)
- Role: scored
- Action: From the GaAs quasiparticle energies, compute and write to `GaAs_bands.json`:
  - Γ_{8v} → Γ_{6c} (Gamma_to_Gamma)
  - Γ_{8v} → X_{6c} (Gamma_to_X)
  - Γ_{8v} → L_{6c} (Gamma_to_L)
  - L_{6c} → X_{6c} (L_to_X)
  - X_{6c} → X_{7c} (X_to_X_splitting)
  All values in eV.
- Output file: `/app/outputs/GaAs_bands.json`
- Format: json
- Contract: Keys "Gamma_to_Gamma", "Gamma_to_X", "Gamma_to_L", "L_to_X", "X_to_X_splitting" (all numbers, eV).
- Scoring: scored by hidden verifier.

### Step 9: Extract AlAs band-energy differences (scored)
- Role: scored
- Action: From the AlAs quasiparticle energies, compute and write to `AlAs_bands.json`:
  - Γ_{8v} → Γ_{6c} (Gamma_to_Gamma)
  - Γ_{8v} → X_{6c} (Gamma_to_X)
  - Γ_{8v} → L_{6c} (Gamma_to_L)
  - L_{6c} → X_{6c} (L_to_X)
  - X_{6c} → X_{7c} (X_to_X_splitting)
  All values in eV.
- Output file: `/app/outputs/AlAs_bands.json`
- Format: json
- Contract: Keys "Gamma_to_Gamma", "Gamma_to_X", "Gamma_to_L", "L_to_X", "X_to_X_splitting" (all numbers, eV).
- Scoring: scored by hidden verifier.

## Output files

All output files must be written under `/app/outputs/`.

Scored files:
- `/app/outputs/Si_bands.json`
- `/app/outputs/Ge_bands.json`
- `/app/outputs/GaAs_bands.json`
- `/app/outputs/AlAs_bands.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Si_bands.json
- path: `/app/outputs/Si_bands.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Quasiparticle band-energy differences for Si (eV).
- schema:
  - `type`: object
  - `properties`:
    - `Gamma_to_Gamma`:
      - `type`: number
    - `Gamma_to_X`:
      - `type`: number
    - `Gamma_to_L`:
      - `type`: number
    - `L_to_X`:
      - `type`: number
    - `Eg`:
      - `type`: number
  - `required`: `Gamma_to_Gamma`, `Gamma_to_X`, `Gamma_to_L`, `L_to_X`, `Eg`

### Ge_bands.json
- path: `/app/outputs/Ge_bands.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Quasiparticle band-energy differences for Ge (eV).
- schema:
  - `type`: object
  - `properties`:
    - `Gamma_to_Gamma`:
      - `type`: number
    - `Gamma_to_X`:
      - `type`: number
    - `Gamma_to_L`:
      - `type`: number
    - `L_to_X`:
      - `type`: number
    - `Eg`:
      - `type`: number
  - `required`: `Gamma_to_Gamma`, `Gamma_to_X`, `Gamma_to_L`, `L_to_X`, `Eg`

### GaAs_bands.json
- path: `/app/outputs/GaAs_bands.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Quasiparticle band-energy differences for GaAs (eV).
- schema:
  - `type`: object
  - `properties`:
    - `Gamma_to_Gamma`:
      - `type`: number
    - `Gamma_to_X`:
      - `type`: number
    - `Gamma_to_L`:
      - `type`: number
    - `L_to_X`:
      - `type`: number
    - `X_to_X_splitting`:
      - `type`: number
  - `required`: `Gamma_to_Gamma`, `Gamma_to_X`, `Gamma_to_L`, `L_to_X`, `X_to_X_splitting`

### AlAs_bands.json
- path: `/app/outputs/AlAs_bands.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Quasiparticle band-energy differences for AlAs (eV).
- schema:
  - `type`: object
  - `properties`:
    - `Gamma_to_Gamma`:
      - `type`: number
    - `Gamma_to_X`:
      - `type`: number
    - `Gamma_to_L`:
      - `type`: number
    - `L_to_X`:
      - `type`: number
    - `X_to_X_splitting`:
      - `type`: number
  - `required`: `Gamma_to_Gamma`, `Gamma_to_X`, `Gamma_to_L`, `L_to_X`, `X_to_X_splitting`

Notes: All values are in electronvolts (eV). The verifier compares each entry to a gold value with a hidden absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Si_bands.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "Gamma_to_Gamma": {
            "type": "number"
          },
          "Gamma_to_X": {
            "type": "number"
          },
          "Gamma_to_L": {
            "type": "number"
          },
          "L_to_X": {
            "type": "number"
          },
          "Eg": {
            "type": "number"
          }
        },
        "required": [
          "Gamma_to_Gamma",
          "Gamma_to_X",
          "Gamma_to_L",
          "L_to_X",
          "Eg"
        ]
      },
      "description": "Quasiparticle band-energy differences for Si (eV)."
    },
    {
      "file": "Ge_bands.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "Gamma_to_Gamma": {
            "type": "number"
          },
          "Gamma_to_X": {
            "type": "number"
          },
          "Gamma_to_L": {
            "type": "number"
          },
          "L_to_X": {
            "type": "number"
          },
          "Eg": {
            "type": "number"
          }
        },
        "required": [
          "Gamma_to_Gamma",
          "Gamma_to_X",
          "Gamma_to_L",
          "L_to_X",
          "Eg"
        ]
      },
      "description": "Quasiparticle band-energy differences for Ge (eV)."
    },
    {
      "file": "GaAs_bands.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "Gamma_to_Gamma": {
            "type": "number"
          },
          "Gamma_to_X": {
            "type": "number"
          },
          "Gamma_to_L": {
            "type": "number"
          },
          "L_to_X": {
            "type": "number"
          },
          "X_to_X_splitting": {
            "type": "number"
          }
        },
        "required": [
          "Gamma_to_Gamma",
          "Gamma_to_X",
          "Gamma_to_L",
          "L_to_X",
          "X_to_X_splitting"
        ]
      },
      "description": "Quasiparticle band-energy differences for GaAs (eV)."
    },
    {
      "file": "AlAs_bands.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "Gamma_to_Gamma": {
            "type": "number"
          },
          "Gamma_to_X": {
            "type": "number"
          },
          "Gamma_to_L": {
            "type": "number"
          },
          "L_to_X": {
            "type": "number"
          },
          "X_to_X_splitting": {
            "type": "number"
          }
        },
        "required": [
          "Gamma_to_Gamma",
          "Gamma_to_X",
          "Gamma_to_L",
          "L_to_X",
          "X_to_X_splitting"
        ]
      },
      "description": "Quasiparticle band-energy differences for AlAs (eV)."
    }
  ],
  "notes": "All values are in electronvolts (eV). The verifier compares each entry to a gold value with a hidden absolute tolerance."
}
```

## How you are scored

A hidden verifier reads each scored JSON file and compares every transition energy to the correct reference value using an absolute tolerance. The final reward is the proportion of transitions that fall within the tolerance across all four materials. Reporting numbers without running the full CPP-GW pipeline will not pass because the verifier uses a different tolerance check. Ensure every required key is present and files are valid JSON.
