# First-principles calculation of transferred hyperfine constants in a two-atom model

## Problem background
The transferred hyperfine interaction at a ligand ion (F⁻) near a magnetic ion (Mn²⁺) provides key insights into the spin density distribution and the strength of covalent bonding in insulators. In certain ionic crystals the distance between the magnetic ion and its neighbouring ligands is unusually large, making the problem sensitive to both overlap and charge-transfer effects. The static theory models this interaction using a two-centre three-electron configuration-interaction framework, where an electron from a doubly occupied ligand orbital can transfer to an empty metal d orbital, leaving a net spin density on the ligand. The goal is to compute the resulting hyperfine constants from first principles, thereby demonstrating the relative importance of overlap and Coulomb integrals at large separations.

## Approach
The reproduction is based on a static two-centre three-electron model. The Mn²⁺–F⁻ pair is treated as a diatomic system with one electron occupying a Mn 3d orbital and two electrons occupying a ligand orbital (1s, 2s, 2pσ, or 2pπ of F⁻). Configuration interaction between the ionic ground state and a charge-transferred state (an electron moved from the ligand to an empty d orbital) is handled via the Serber method. All necessary two-centre integrals — overlap, kinetic, and several types of Coulomb integrals — must be evaluated numerically using Hartree‑Fock atomic wave functions. The transfer coefficient γ is derived from these integrals together with a configurational energy difference Δ_B = -1.0 a.u. The ligand admixture amplitudes λ are then obtained from γ and the overlap integrals, yielding spin densities f_s, f_σ, f_π for the 2s, 2pσ, and 2pπ channels. Finally, those spin densities are combined with the known atomic and nuclear constants and the expectation values |χ_s(0)|² and ⟨r⁻³⟩ to compute the isotropic hyperfine constant A_s and the anisotropic components A_σ and A_π. The entire calculation is carried out for the single interatomic distance R = 2.58 Å. Only the static theory is reproduced; the temperature-dependent soft‑phonon contribution is not included.

## Hartree‑Fock wave function parameters
Use the following Slater‑type orbital (STO) exponents and expansion coefficients. The radial part of an STO is
R_nl(r) = N_nl r^(n-1) exp(-ζ r)
with the normalisation constant N_nl = (2ζ)^(n+1/2) / √((2n)!).

**F⁻ orbitals (single‑ζ)**
| orbital | n | l | ζ (a.u.⁻¹) |
|---------|---|---|------------|
| 1s     | 1 | 0 | 8.6507     |
| 2s     | 2 | 0 | 2.56384    |
| 2p     | 2 | 1 | 2.56384    |

**Mn²⁺ 3d orbital (double‑ζ)**
| orbital | n | l | ζ (a.u.⁻¹) | coefficient c |
|---------|---|---|-------------|---------------|
| 3d     | 3 | 2 | 5.15        | 0.5266        |
| 3d     | 3 | 2 | 1.90        | 0.6312        |

The spatial part of the 3d orbital is a linear combination of the two STOs with the given coefficients. For dσ and dπ combinations use the standard real spherical harmonics aligned with the internuclear axis (the z‑axis).

## Atomic and nuclear constants
| quantity | value |
|----------|-------|
| Landé g‑factor (g)         | 2.0023 |
| total electronic spin (S)  | 5/2    |
| nuclear g‑factor for ¹⁹F (g_N) | 5.256 |
| Bohr magneton (μ_B)        | 9.274009994×10⁻²⁴ J T⁻¹ |
| nuclear magneton (μ_N)     | 5.0507837461×10⁻²⁷ J T⁻¹ |
| Planck constant (h)        | 6.62607015×10⁻³⁴ J s |
| |χ_{2s}(0)|²              | 5.36 a₀⁻³ |
| ⟨r⁻³⟩ for F⁻ 2p           | 8.425 a₀⁻³ |

*Conversion:* 1 a₀ = 5.29177210903×10⁻¹¹ m. All integrals should be computed in atomic units; the hyperfine constants are then converted to MHz using the above constants and the formulas below.

## Formulas for the hyperfine constants
After computing the spin densities

f_s = λ_s², f_σ = λ_σ², f_π = λ_π²,

the hyperfine components (in SI units) are obtained from

A_s = (8π/3) g μ_B g_N μ_N |χ_s(0)|² f_s
A_σ = (1/S) g μ_B g_N μ_N ⟨r⁻³⟩ f_σ
A_π = (1/S) g μ_B g_N μ_N ⟨r⁻³⟩ f_π

with S = 5/2. The constants A_s, A_σ, A_π are in joules; convert to MHz by dividing by h and multiplying by 10⁻⁶. The total anisotropic constant is defined as the geometric mean

A_aniso = √(Aσ² + Aπ²).

## Determination of λ amplitudes
For each orbital pair (a₁ = ligand orbital, a₃ = Mn 3d orbital) carry out the following steps:

1. **Overlap integral**   S = ⟨a₁|a₃⟩  
2. **Kinetic energy integral**   T = ⟨a₁|−½∇²|a₃⟩  
3. **Coulomb integrals** required by Eq. (10):
   - ⟨a₃ a₁ || a₃ a₃⟩
   - ⟨a₁ a₃ || a₁ a₃⟩
   - ⟨a₁ a₁ || a₃ a₁⟩
   - ⟨a₁ a₁ || a₁ a₁⟩
   (these are two‑electron integrals over the two‑centre STO basis; evaluate them either analytically using spherical‑harmonic expansions or by numerical quadrature.)
4. **One‑electron Hartree energies** (in a.u.):
   - E_H(F⁻) for the ligand orbital a₁: for 1s use -25.828, for 2s use -1.074, for 2p use -0.180.
   - E_H(Mn²⁺) for the 3d orbital: use -1.236.
5. **Configuration energy difference** Δ_B = -1.0 a.u.  
6. **Transfer coefficient γ** from Eq. (10) of the paper:
   γ = [ ⟨a₁|H₁|a₃⟩ − ⟨a₁|H₁|a₁⟩ S  
         + ⟨a₃ a₁||a₃ a₃⟩ − ⟨a₁ a₃||a₁ a₃⟩ S  
         + ⟨a₁ a₁||a₃ a₁⟩ − ⟨a₁ a₁||a₁ a₁⟩ S ] / Δ_B
   where ⟨a₁|H₁|a₃⟩ is evaluated via Eq. (23) using the kinetic integrals and the Hartree energies:
   ⟨a₁|H₁|a₃⟩ = E_H(F⁻) S − E_H(Mn²⁺) S − ⟨a₂ a₃||a₂ a₁⟩ + T + V_coulomb.
   (The potential term V_coulomb is absorbed in the two‑electron integrals listed above; the internal core contributions are accounted for by the effective Hartree energies as discussed in the paper.)
7. **Admixture amplitude**  λ = γ + S  
   (for each symmetry: λ_s = γ_{2s} + S_{2s}, λ_σ = γ_{2pσ} + S_{2pσ}, λ_π = γ_{2pπ} + S_{2pπ}).
   The 1s orbital contributes only through the 1s‑2s cross term: the total 2s spin density is
   f_s = (λ_{2s} + λ_{1s})².

## Reproduction target
Produce the static transferred hyperfine constants for the F⁻ ion at the Mn²⁺–F⁻ distance of 2.58 Å. Specifically, compute the isotropic constant A_s (in MHz) and the total anisotropic constant A_aniso (in MHz), defined as above. These quantities must be written to the JSON file `/app/outputs/hyperfine_constants.json` with keys `As_MHz` and `A_aniso_MHz`.

## Output files
Write the following artifact under `/app/outputs`:
- `/app/outputs/hyperfine_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hyperfine_constants.json
- path: `/app/outputs/hyperfine_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The final reproduced transferred hyperfine constants for the F⁻ ion at the Mn²⁺–F⁻ distance of 2.58 Å.
- schema:
  - `type`: object
  - `required`:
    - `As_MHz`: number (MHz)
    - `A_aniso_MHz`: number (MHz)
  - `description`: Computed isotropic hyperfine constant As and total anisotropic constant A_aniso (geometric mean of Aσ and Aπ) in MHz.

Notes: The checker compares As_MHz and A_aniso_MHz to the paper‑reported values with a relative tolerance (scoring partial credit up to 30% deviation). Only the static theory is scored; the soft‑phonon contribution is omitted as it relies on experimental input.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: the file exists and the JSON object contains the required keys. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hyperfine_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "As_MHz": "number (MHz)",
          "A_aniso_MHz": "number (MHz)"
        },
        "description": "Computed isotropic hyperfine constant As and total anisotropic constant A_aniso (geometric mean of Aσ and Aπ) in MHz."
      },
      "description": "The final reproduced transferred hyperfine constants for the F⁻ ion at the Mn²⁺–F⁻ distance of 2.58 Å."
    }
  ],
  "notes": "The checker compares As_MHz and A_aniso_MHz to the paper-reported values with a relative tolerance (scoring partial credit up to 30% deviation). Only the static theory is scored; the soft-phonon contribution is omitted as it relies on experimental input."
}
```

## How you are scored
A hidden verifier will independently check the scored workflow artifact. The final hyperfine constants file (`hyperfine_constants.json`) is the only scored output. The verifier compares your `As_MHz` and `A_aniso_MHz` against the paper’s values. The reward is computed from the relative accuracy of these two numbers. No intermediate files are required for scoring.