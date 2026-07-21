# Simulated SPA-LEED diffraction from a 1D Frenkel-Kontorova model

## Problem background
A one‑dimensional Frenkel‑Kontorova (FK) model is used to describe the relaxation of a surface atomic chain on a rigid substrate.  Combined with a simple kinematic diffraction approximation, the model explains the emergence of diffraction features in spot‑profile analysis low‑energy electron diffraction (SPA‑LEED).  

You will implement the 1D FK energy minimisation, add a vertical corrugation, and compute the kinematic SPA‑LEED intensity as a function of the parallel wave‑vector offset (expressed as a percentage of the surface Brillouin zone).

## Mathematical model

### 1. Frenkel-Kontorova energy
A chain of **N** Cu atoms sits on a rigid periodic substrate.  The total potential energy is

$$
E = \frac{\gamma a^{2}}{2} \sum_{n=0}^{N-2} \bigl( \xi_{n+1} - \xi_n - f \bigr)^2
    + \frac{W}{2} \sum_{n=0}^{N-1} \bigl[ 1 - \cos(2\pi \xi_n) \bigr].
\tag{1}
$$

- **a** = Cu bulk lattice constant (3.61 Å)
- **f** = misfit = (b − a)/a = **−0.01**  (the unstrained first‑layer spacing is b = 0.99 a)
- **ξₙ** = displacement of the n‑th atom from the nearest substrate potential minimum, in units of **a**
- **γ** = effective spring constant describing lateral stiffness of the surface layer
- **W** = amplitude of the substrate potential = **0.8 eV**

Minimise the total energy with respect to the set {ξₙ}.  The equilibrium lateral positions are  
**xₙ = a (n + ξₙ)**  (place the origin so that the substrate potential minima are at integer multiples of **a**).

### 2. Vertical corrugation
Atoms displaced from the substrate potential minima are lifted above the surface.  The height variation is modelled as a cosine with amplitude **a√2**:

$$
z_n = A_v \cos\!\left(\frac{2\pi n}{N}\right), \qquad A_v = a\sqrt{2} .
$$

### 3. Kinematic diffraction intensity
SPA‑LEED is treated in the kinematic approximation.  The scattered intensity for a parallel wave‑vector offset **Δk∥** (unit: rad/Å) is proportional to the squared modulus of the structure factor:

$$
I(\Delta k_\parallel) \propto
\Bigl| \sum_{n=0}^{N-1} \exp\!\bigl[ i \Delta k_\parallel x_n + i S_z z_n \bigr] \Bigr|^2 .
$$

- The vertical scattering factor **S_z** is fixed: **S_z = 4.97**.
- No attenuation factor is applied because all chain atoms reside at the same surface layer.

Convert between parallel wave‑vector offset in % BZ and physical wave‑vector via

$$
\Delta k_\parallel (\text{rad/Å}) = \frac{\text{k\_percent\_BZ}}{100} \times \frac{2\pi}{a}.
$$

### 4. Instrumental broadening and normalisation
Convolve the raw intensity with a Gaussian that has a full‑width at half‑maximum (FWHM) of **0.1 % BZ**.  Finally, normalise the profile so that the global maximum intensity equals **1.0**.

## Parameters & assets

| Parameter | Symbol | Value | Notes |
|-----------|--------|-------|-------|
| Cu bulk lattice constant | **a** | 3.61 Å | Standard crystallographic value |
| Substrate potential amplitude | **W** | 0.8 eV | Twice the diffusion barrier over bridge site |
| Misfit | **f** | –0.01 | first‑layer spacing b = 0.99 a |
| Vertical corrugation amplitude | **A_v** | **a√2** | Cosine shape |
| Vertical scattering factor | **S_z** | 4.97 | From literature |
| Spring constant | **γ** | 1.72 × 10³ eV/Å² | Calibrated from the strain‑relief energy (see below) |
| Instrumental resolution | – | Gaussian, FWHM = 0.1 % BZ | Consistent with SPA‑LEED resolution |
| Chain length | **N** | ≈ 100 atoms | Representative of the upper‑terrace width |

### Calibration of the spring constant γ
The spring constant is fixed by requiring that the harmonic energy of a uniform chain with spacing b = 0.99 a, when all substrate interactions are ignored, equals the literature strain‑relief energy of 1.12 eV per atom.  This gives

$$
\frac{1}{2}\,\gamma\, a^{2}\, f^{2} = 1.12\ \text{eV},
\qquad
\gamma = \frac{2 \times 1.12\ \text{eV}}{a^{2} f^{2}}.
$$

Insert **a = 3.61 Å** and **f = −0.01** to obtain **γ ≈ 1.72 × 10³ eV/Å²**.  Use this value in Eq. (1); all energies are expressed in eV and lengths in Å.

## Reproduction target
Produce a two‑column CSV file named `step_01_diffraction_profile.csv`:

- **Column 1**: `k_percent_BZ` – parallel wave vector offset in % BZ (float).
- **Column 2**: `intensity` – normalised intensity (maximum = 1.0, non‑negative).

The profile must result from the full pipeline: FK energy minimisation → lateral positions → vertical corrugation → kinematic diffraction summation → convolution with instrumental broadening → normalisation.

## Workflow steps

### Step 1: Simulated SPA-LEED diffraction intensity profile
- **Role**: scored
- **Action**: Implement the 1D FK model (Eq. 1), minimise energy, add vertical corrugation (cosine, amplitude a√2), compute kinematic diffraction intensity using **S_z = 4.97**, convolve with a Gaussian of FWHM 0.1 % BZ, normalise to maximum 1.0, and save the CSV.
- **Output file**: `/app/outputs/step_01_diffraction_profile.csv`
- **Format**: csv
- **Contract**: CSV header `k_percent_BZ`, `intensity` (float, non‑negative).

## Output files
Write all artifacts under `/app/outputs`:

- `/app/outputs/step_01_diffraction_profile.csv`

## Output contract

The verifier expects exactly this file.  Write it under `/app/outputs` and follow the schema.

### step_01_diffraction_profile.csv
- **path**: `/app/outputs/step_01_diffraction_profile.csv`
- **format**: csv
- **purpose**: scored
- **target_policy**: exact_match
- **schema**:
  - **type**: table
  - **required_columns**: `k_percent_BZ`, `intensity`
  - **units**:
    - `k_percent_BZ`: % BZ
    - `intensity`: arbitrary units (normalised)

The hidden checker verifies physical consistency (normalisation, non‑negative intensity, presence of a distinct diffraction feature) by inspecting properties of the submitted profile.  You must genuinely run the FK minimisation and the full diffraction calculation.

## Self-check before finishing (optional)
A machine‑readable copy of the output contract is provided below; use it to verify file existence and column presence before final submission.

```json
{
  "outputs": [
    {
      "file": "step_01_diffraction_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": ["k_percent_BZ", "intensity"],
        "units": {
          "k_percent_BZ": "% BZ",
          "intensity": "arbitrary units (normalized)"
        }
      }
    }
  ]
}
```

## How you are scored
Your submitted `step_01_diffraction_profile.csv` is evaluated by a hidden verifier that inspects the profile’s shape and physical consistency.  Points are awarded for correct structure (normalisation, non‑negative intensity, etc.) and for presenting a clear diffraction peak consistent with the physical setting.  A profile that faithfully implements the FK relaxation and diffraction described above will earn the maximum reward.  The verifier produces an automatic score on a 0‑to‑1 scale.