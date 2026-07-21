# Charged-Phonon Model of Gate-Tunable Phonon Anomalies in ABC Trilayer Graphene

## Problem background
ABC (rhombohedral) stacked trilayer graphene exhibits unusual infrared absorption from in-plane optical phonons near 1580 cm⁻¹. In this non-polar layered material, interactions between the lattice vibrations and the electronic system can transfer oscillator strength from interband electronic transitions to the phonon mode. This charged-phonon effect produces a strong, doping-dependent absorption feature and a simultaneous frequency shift. This task implements the theoretical charged-phonon model to compute how the phonon spectral weight (integrated optical conductivity) and frequency shift vary with carrier density in ABC trilayer graphene.

## Approach
The approach proceeds in two main stages. First, the electronic band structure of ABC trilayer graphene is obtained from a tight-binding model that includes nearest-neighbor intralayer hopping (γ₀) and interlayer coupling (γ₁). The secular equation for the in-plane optical phonon modes, parameterized by interlayer force constants, is solved to identify the eigenvector of the single infrared-active mode (the Eᵤ mode). Second, the charged-phonon formalism is applied: the mixed current-phonon response function and the phonon self-energy are evaluated at the bare phonon energy. These response functions capture how electron-phonon coupling, modified by Pauli blocking at finite doping, renormalizes the phonon spectral weight and frequency. The calculation is performed under a rigid-band approximation (the Fermi level is shifted to match a given carrier density), using a constant deformation potential, room temperature, and a phenomenological broadening to model disorder. The resulting spectral weight and frequency shift are recorded for each specified doping level.

## Model details – explicit formulas

### 1. Tight-binding Hamiltonian for ABC trilayer graphene
In the basis ordered by layer (1,2,3) and sublattice (A,B) as  

```text
(|A1⟩, |B1⟩, |A2⟩, |B2⟩, |A3⟩, |B3⟩)
```

the **k**‑dependent 6×6 Hamiltonian is

```math
H(\mathbf{k}) =
\begin{pmatrix}
0      & γ_0 f(\mathbf{k}) & γ_1 & 0    & 0    & 0      \\
γ_0 f^*(\mathbf{k}) & 0    & 0   & 0    & 0    & 0      \\
γ_1    & 0                & 0   & γ_0 f(\mathbf{k}) & 0    & γ_1    \\
0      & 0                & γ_0 f^*(\mathbf{k}) & 0    & 0    & 0      \\
0      & 0                & 0   & 0                & 0    & γ_0 f(\mathbf{k}) \\
0      & 0                & γ_1 & 0                & γ_0 f^*(\mathbf{k}) & 0
\end{pmatrix}
```

where  
- `γ_0 = 3.16 eV` (intralayer nearest‑neighbor hopping),
- `γ_1 = 0.37 eV` (interlayer coupling between **B**‑sublattice of layer i and **A**‑sublattice of layer i+1, i = 1,2),
- `f(𝐤) = e^{i k_x a/√3} + 2 e^{-i k_x a/(2√3)} cos(k_y a/2)`, with lattice constant `a = 2.46 Å` (the graphene primitive cell).

The electronic energies ε_{n,𝐤} and eigenstates |n,𝐤⟩ (6‑component column vectors) are obtained by diagonalizing H(𝐤) on a sufficiently dense **k**‑point mesh covering the entire Brillouin zone.

### 2. Optical phonon dynamical matrix and Eᵤ eigenvector
The zone‑center optical phonon displacement of each layer is treated as a scalar (polarised along x, say). The bare phonon frequency is `ω₀ = 1580.5 cm⁻¹`. Interlayer coupling is described by the 3×3 dynamical matrix (in units of `cm⁻²`):

```math
D =
\begin{pmatrix}
ω_0^2 + ε + δ & -ε             & -δ             \\
-ε            & ω_0^2 + 2ε     & -ε             \\
-δ            & -ε             & ω_0^2 + ε + δ
\end{pmatrix}
```

with interlayer force constants  
- `ε = 2.2 cm⁻²` (nearest‑layer coupling),
- `δ = 3.0 cm⁻²` (next‑nearest‑layer coupling).

Diagonalise D. The infrared‑active Eᵤ mode corresponds to the eigenvector with the pattern **(+1, 0, −1)** (outer layers move in opposite directions, middle layer at rest). Normalise the eigenvector to obtain the unit‑vector **v** = (v₁, v₂, v₃) with v₁ ≈ −v₃ and v₂ ≈ 0.

### 3. Current operator and electron‑phonon coupling matrix elements
Define the x‑component current operator:

```math
J_x(\mathbf{k}) = \frac{\partial H(\mathbf{k})}{\partial k_x}
```

All matrix elements are computed in the basis of the Bloch eigenstates |n,𝐤⟩:

```math
(J_x)_{nm}(\mathbf{k}) \equiv \langle n,\mathbf{k}| J_x(\mathbf{k}) |m,\mathbf{k}\rangle .
```

The electron‑phonon coupling for the Eᵤ mode is described by the 6×6 operator

```math
\Delta_\nu = \mathrm{diag}(v_1, v_1,\; v_2, v_2,\; v_3, v_3)
```

which repeats each layer’s phonon displacement on both sublattices. With deformation potential `g = 0.27 eV` the coupling matrix element between bands n and m at **k** is

```math
(V_\nu)_{nm}(\mathbf{k}) = g\;\langle n,\mathbf{k}| \Delta_\nu |m,\mathbf{k}\rangle .
```

### 4. Response functions
Let `f(ε) = 1/[e^{(ε-μ)/(k_B T)} + 1]` be the Fermi‑Dirac distribution at temperature `T = 300 K` and chemical potential μ (determined self‑consistently from the carrier density `n`). Use a phenomenological broadening `η = 20 meV` (0.02 eV). All energies are expressed in eV (conversion: `1 cm⁻¹ = 1.23984×10⁻⁴ eV`).

The mixed current‑phonon response function at the bare phonon energy `ω₀` (converted to eV) is

```math
\chi_{j\nu}(\omega_0) = \sum_{\mathbf{k},n,m} 
\frac{[f(ε_{n,\mathbf{k}}) - f(ε_{m,\mathbf{k}})]\;
 (J_x)_{nm}(\mathbf{k})\; (V_\nu)_{mn}^*(\mathbf{k})}
{\omega_0 + iη + ε_{n,\mathbf{k}} - ε_{m,\mathbf{k}}}
```

and the phonon self‑energy is

```math
\chi_{\nu\nu}(\omega_0) = \sum_{\mathbf{k},n,m}
\frac{[f(ε_{n,\mathbf{k}}) - f(ε_{m,\mathbf{k}})]\;
 |(V_\nu)_{mn}(\mathbf{k})|^2}
{\omega_0 + iη + ε_{n,\mathbf{k}} - ε_{m,\mathbf{k}}}
```

where the sums run over all bands (n,m) and over a dense grid of **k** points covering the Brillouin zone. Only the real parts of these quantities are needed.

### 5. Phonon spectral weight and frequency shift
The charged‑phonon spectral weight (integrated optical conductivity) is

```math
W = \frac{\pi}{\omega_0}\; \bigl[\,\mathrm{Re}\,\chi_{j\nu}(\omega_0)\bigr]^2 .
```

The frequency shift (red shift) induced by the electron‑phonon interaction is

```math
\Delta\omega = \mathrm{Re}\,\chi_{\nu\nu}(\omega_0) .
```

Convert Δω from eV to cm⁻¹. The spectral weight W is to be reported in units of **10³ Ω⁻¹ cm⁻¹**. To obtain this unit, use the standard conversion

```math
W\,[10^3\,\Omega^{-1}\,\mathrm{cm}^{-1}] =
\frac{4\pi e^2}{\hbar}\;
\frac{1}{\omega_0\,[\mathrm{eV}]}\;
\bigl[\,\mathrm{Re}\,\chi_{j\nu}(\omega_0)\,\bigr]^2
\times 10^{-3}
```

where `e = 1.602176634×10⁻¹⁹ C` is the elementary charge and `ħ = 1.054571817×10⁻³⁴ J·s`.  (The numerical factor ensures that χ_{jν} computed from the above formulas with J in eV·Å and energies in eV yields the correct physical units.)

---

**All numerical parameters** are summarised here for convenience:

| Parameter | Value               | Description                         |
|-----------|---------------------|-------------------------------------|
| γ₀        | 3.16 eV             | Intralayer hopping                  |
| γ₁        | 0.37 eV             | Interlayer hopping (B₁‑A₂, B₂‑A₃)   |
| a         | 2.46 Å              | Graphene lattice constant           |
| ω₀        | 1580.5 cm⁻¹         | Bare optical phonon frequency      |
| ε         | 2.2 cm⁻²            | Nearest‑layer force constant        |
| δ         | 3.0 cm⁻²            | Next‑nearest‑layer force constant   |
| g         | 0.27 eV             | Deformation potential               |
| T         | 300 K               | Temperature                         |
| η         | 20 meV              | Phenomenological damping           |

---

## Reproduction target
Implement the tight-binding and charged-phonon model for the ABC trilayer. Compute the phonon spectral weight (integrated optical conductivity, in units of 10³ Ω⁻¹ cm⁻¹) and the frequency shift (in cm⁻¹) of the infrared-active mode at five carrier densities: 0, 1×10¹², 5×10¹², 1×10¹³, and 2×10¹³ cm⁻². Write the results to the CSV file specified in the workflow steps.

## Assets
All required numerical parameters (tight-binding hopping integrals, interlayer force constants, deformation potential, bare phonon frequency, temperature, and broadening) are explicitly stated in the workflow steps and the model details above. No external datasets, pre-trained models, or proprietary tools are needed; the entire workflow can be implemented using standard scientific Python libraries (NumPy, SciPy).

## Workflow steps

### Step 1: Compute ABC trilayer band structure and phonon eigenvector
- Role: process
- Action: Implement the 6×6 tight-binding Hamiltonian H(k) given in the Model details, using γ₀=3.16 eV, γ₁=0.37 eV, and a=2.46 Å. Diagonalize on a dense k‑point grid (e.g., 300×300 or denser) to obtain all bands ε_{n,k} and eigenvectors |n,k⟩. Construct the 3×3 dynamical matrix D with ε=2.2 cm⁻² and δ=3.0 cm⁻². Diagonalize D to obtain the three eigenvectors; select the eigenvector that has the form (+1,0,−1) (Eᵤ mode) and normalize it to unit length (v₁,v₂,v₃). This step provides the electronic structure and phonon eigenvector required for the charged-phonon calculation.
- Evidence: none

### Step 2: Compute phonon spectral weight and frequency shift
- Role: scored (load-bearing)
- Action: Using the band structure and Eᵤ eigenvector from Step 1, compute the charged‑phonon response functions and observables as defined in the Model details.
  - For each doping level n = 0, 1×10¹², 5×10¹², 1×10¹³, 2×10¹³ cm⁻²:
    1. Determine the Fermi level μ by integrating the density of states (rigid‑band doping) so that the carrier density matches n. Use the Fermi‑Dirac distribution at T=300 K.
    2. Evaluate χ_{jν}(ω₀) and χ_{νν}(ω₀) using the formulas in Section 4 of the Model details, with energies in eV (convert ω₀ from cm⁻¹ to eV using 1 cm⁻¹ = 1.23984×10⁻⁴ eV) and the broadening η=0.02 eV.
    3. Take the real parts, then compute spectral weight W (in 10³ Ω⁻¹ cm⁻¹) using the conversion formula in Section 5 and frequency shift Δω = Re χ_{νν} (converted to cm⁻¹).
  - Save the results to `abc_trilayer_charged_phonon_results.csv` with columns: doping (cm⁻²), spectral_weight (10³ Ω⁻¹ cm⁻¹), frequency_shift (cm⁻¹).
- Output file: `/app/outputs/abc_trilayer_charged_phonon_results.csv`
- Format: csv
- Contract: columns: doping (cm^-2), spectral_weight (10^3 Ω^-1 cm^-1), frequency_shift (cm^-1)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/abc_trilayer_charged_phonon_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### abc_trilayer_charged_phonon_results.csv
- path: `/app/outputs/abc_trilayer_charged_phonon_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed phonon spectral weight and frequency shift for ABC trilayer graphene at five doping levels, compared to hidden reference values from the paper's theoretical curves with tolerance and trend checks.
- schema:
  - `type`: table
  - `required_columns`: `doping`, `spectral_weight`, `frequency_shift`
  - `units`:
    - `doping`: cm^-2
    - `spectral_weight`: 10^3 Ω^-1 cm^-1
    - `frequency_shift`: cm^-1

Notes: The checker verifies the agent's reported values against reference values and checks the expected monotonic trends: spectral weight increases with doping magnitude, and frequency shift becomes more negative (red shift) with doping.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "abc_trilayer_charged_phonon_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping",
          "spectral_weight",
          "frequency_shift"
        ],
        "units": {
          "doping": "cm^-2",
          "spectral_weight": "10^3 Ω^-1 cm^-1",
          "frequency_shift": "cm^-1"
        }
      },
      "description": "Computed phonon spectral weight and frequency shift for ABC trilayer graphene at five doping levels, compared to hidden reference values from the paper's theoretical curves with tolerance and trend checks."
    }
  ],
  "notes": "The checker verifies the agent's reported values against reference values and checks the expected monotonic trends: spectral weight increases with doping magnitude, and frequency shift becomes more negative (red shift) with doping."
}
```

## How you are scored
Your submitted CSV file is evaluated by an automated hidden verifier. The verifier first checks that the file is well-formed with the required columns. It then compares the reported spectral weight and frequency shift at each doping level against reference values (derived from the original theoretical predictions) using appropriate tolerances. Additionally, the verifier examines the structural behavior of the results across the doping range to ensure they satisfy expected physical trends (e.g., monotonic variation of spectral weight and frequency shift with doping). The final reward is a weighted combination of these numeric and structural checks. Simply reporting numbers without a genuine implementation of the described model will not earn full credit.