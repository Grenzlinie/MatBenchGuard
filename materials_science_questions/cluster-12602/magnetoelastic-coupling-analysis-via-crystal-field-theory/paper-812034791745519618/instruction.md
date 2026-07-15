# Magnetoelastic coupling analysis via crystal field theory

## Problem background
In paramagnetic crystals, the interaction between the spin of a magnetic ion and lattice vibrations (phonons) is characterised by magnetoelastic coupling coefficients. For Ni²⁺ ions occupying substitutional sites in the cubic perovskite KMgF₃, the crystal‑field symmetry restricts the quadrupolar part of the magnetoelastic tensor to just two independent components, G₁₁ and G₄₄. These coefficients govern the strength of the spin‑phonon interaction and are directly probed in acoustic paramagnetic resonance (a.p.r.) experiments. A reliable theoretical determination of G₁₁ and G₄₄ is essential for understanding spin‑lattice relaxation and for validating the point‑charge crystal field model in this system. Your task is to compute G₁₁ and G₄₄ from the microscopic electrostatics of the Ni²⁺ 3d electrons.

## Approach
The calculation rests on the point‑charge crystal field model. In this framework, the environment of the Ni²⁺ ion (six nearest‑neighbour F⁻ ligands) is approximated by effective point charges e', giving rise to a cubic crystal field. The magnetoelastic coefficients are obtained via third‑order perturbation theory applied to the Hamiltonian

    ℋ₀ = ℋ_free ion + ℋ_crystal field + ℋ_orbit‑orbit + ℋ_spin‑spin,

with the perturbation

    ℋ' = β H·(L+2S) + λ L·S + ℋ_orbit‑lattice.

The orbit‑lattice Hamiltonian ℋ_orbit‑lattice couples the orbital degrees of freedom to a static acoustic strain. Only terms linear in the strain are retained, and the matrix elements between the ground orbital singlet (A₂) and the excited orbital triplets (T₂, T₁) are evaluated using the method of operator equivalents.

Carrying the perturbation expansion to third order yields closed‑form expressions for G₁₁ and G₄₄:

    G₁₁ = – (100/9) · λ² e e' / (E_T₂ – E_A₂)² · ⟨r⁴⟩ / R⁵ ,

    G₄₄ = – (4/7) λ² e e' { [3⟨r²⟩R⁻³ + (5/3)⟨r⁴⟩R⁻⁵] / (E_T₂ – E_A₂)² + [6⟨r²⟩R⁻³ + (5/2)⟨r⁴⟩R⁻⁵] / [(E_T₂ – E_A₂)(E_T₁ – E_A₂)] }.

Here
  • λ is the spin‑orbit coupling constant for Ni²⁺,
  • e is the electron charge,
  • e' is the effective charge on a ligand F⁻ ion,
  • ⟨r²⟩ and ⟨r⁴⟩ are the radial expectation values of r² and r⁴ for a Ni²⁺ 3d electron,
  • R is the lattice parameter of KMgF₃,
  • E_T₂ – E_A₂ and E_T₁ – E_A₂ are the crystal‑field excitation energies.

The product e e' is not known independently but can be deduced from the measured crystal‑field splitting, via the relation

    e e' ⟨r⁴⟩ / R⁵ = 6 Dq ,

where Dq is the conventional octahedral crystal‑field parameter. The numerical value of Dq (and therefore e e') is obtained from optical spectroscopy (Knox, Shulman & Sugano, Phys. Rev. 130, 512, 1963).

To complete the calculation you must:
  • obtain the spin‑orbit coupling constant λ from standard ligand‑field references,
  • extract the energies E_T₂ – E_A₂ and E_T₁ – E_A₂ and the value of Dq from Knox et al. (1963),
  • use published tables or Hartree‑Fock calculations to find ⟨r²⟩ and ⟨r⁴⟩ for Ni²⁺ 3d,
  • find the lattice constant R from the known crystallographic data of KMgF₃,
  • implement the above formulas in a numerical script (Python with numpy is sufficient) and output the two coefficients.

## Reproduction target
Compute the quadrupolar magnetoelastic coefficients G₁₁ and G₄₄ (in cm⁻¹ per unit strain) for Ni²⁺ in KMgF₃ using the point‑charge crystal field model and the publicly available parameters listed above. Write the results to a JSON file containing exactly the two keys "G11" and "G44" with the numeric values you obtain.

## Assets

- Crystal field parameters for KMgF3:Ni2+ (Knox, Shulman & Sugano 1963): 10.1103/PhysRev.130.512
- Radial expectation values for Ni2+ (standard Hartree-Fock or literature)
- Spin-orbit coupling constant for Ni2+ (free-ion value)
- Lattice parameter of KMgF3: 10.1016/0031-9163(67)90347-7
- Python numerical environment (numpy): numpy

## Workflow steps

### Step 1: Compute point‑charge magnetoelastic coefficients
- Role: scored (load-bearing)
- Action: Compute the quadrupolar magnetoelastic coefficients G11 and G44 for Ni2+ in KMgF3 using the point-charge crystal field model. Obtain necessary parameters from public literature: the spin-orbit coupling constant λ for Ni2+, the crystal field energy splittings (E_T2 − E_A2 and E_T1 − E_A2) from Knox et al. 1963, the radial expectation values ⟨r²⟩ and ⟨r⁴⟩ for Ni2+ 3d electrons, and the lattice parameter R of KMgF3. Implement the third-order perturbation expressions for G11 and G44 that involve these parameters, the effective ligand charge e', and the lattice parameter. Report the computed G11 and G44 in cm⁻¹ unit strain⁻¹.
- Output file: `/app/outputs/magnetoelastic_coefficients.json`
- Format: json
- Contract: {"G11": number, "G44": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetoelastic_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetoelastic_coefficients.json
- path: `/app/outputs/magnetoelastic_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed quadrupolar magnetoelastic coefficients G11 and G44 in cm⁻¹ per unit strain.
- schema:
  - `type`: object
  - `required`:
    - `G11`: number (cm⁻¹ unit strain⁻¹)
    - `G44`: number (cm⁻¹ unit strain⁻¹)

Notes: Only the theoretical point-charge calculation is scored; the experimental a.p.r. measurements are excluded per the taskability scope. The score compares the agent's reported values to the paper's published theoretical values within a tolerance, but the exact reference values and tolerance are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetoelastic_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "G11": "number (cm⁻¹ unit strain⁻¹)",
          "G44": "number (cm⁻¹ unit strain⁻¹)"
        }
      },
      "description": "Computed quadrupolar magnetoelastic coefficients G11 and G44 in cm⁻¹ per unit strain."
    }
  ],
  "notes": "Only the theoretical point-charge calculation is scored; the experimental a.p.r. measurements are excluded per the taskability scope. The score compares the agent's reported values to the paper's published theoretical values within a tolerance, but the exact reference values and tolerance are hidden."
}
```

## How you are scored
The hidden verifier will read your magnetoelastic_coefficients.json and compare both G₁₁ and G₄₄ to the corresponding reference values that were obtained from the original theoretical calculation. The comparison uses a fixed tolerance; you will receive the maximum score if your computed values lie within that tolerance, and zero otherwise. Because the calculation relies on physical constants and closed‑form expressions, the expected spread from different numerical implementations is small, so the tolerance is chosen to be fair while still requiring an accurate computation. Only the contents of the JSON file are evaluated; intermediate artifacts are not scored.
