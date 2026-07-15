# First-principles calculation of transferred hyperfine constants in a two-atom model

## Problem background
The transferred hyperfine interaction at a ligand ion (F⁻) near a magnetic ion (Mn²⁺) provides key insights into the spin density distribution and the strength of covalent bonding in insulators. In certain ionic crystals the distance between the magnetic ion and its neighboring ligands is unusually large, making the problem sensitive to both overlap and charge-transfer effects. The static theory models this interaction using a two-center three-electron configuration-interaction framework, where an electron from a doubly occupied ligand orbital can transfer to an empty metal d orbital, leaving a net spin density on the ligand. Computing the resulting hyperfine constants from first principles demonstrates the relative importance of overlap and Coulomb integrals at large separations and establishes the functional dependence on interatomic distance.

## Approach
The reproduction is based on a static two-center three-electron model. The Mn²⁺–F⁻ pair is treated as a diatomic system with one electron occupying a Mn d orbital and two electrons occupying a ligand orbital (1s, 2s, 2pσ, or 2pπ of F⁻). Configuration interaction between the ionic ground state and a charge-transferred state (an electron moved from the ligand to an empty d orbital) is handled via the Serber method. All necessary two-center integrals — overlap, kinetic, and several types of Coulomb integrals — are evaluated numerically using Hartree‑Fock atomic wave functions for F⁻ and Mn²⁺ (Clementi & Roetti, 1974). The transfer coefficient γ is derived from these integrals together with an estimated configurational energy difference Δ_B = -1.0 a.u. The ligand admixture amplitudes λ are then obtained from γ and the overlap integrals, yielding spin densities f_s, f_σ, f_π for the 2s, 2pσ, and 2pπ channels. Finally, those spin densities are combined with known atomic and nuclear constants (electronic g-factor, nuclear g-factor for ¹⁹F, Bohr and nuclear magnetons, total spin S=5/2, and the relevant expectation values |χ_s(0)|² and ⟨r⁻³⟩) to compute the isotropic hyperfine constant A_s and the anisotropic components A_σ and A_π. The entire calculation is carried out for the single interatomic distance R=2.58 Å that corresponds to the Mn²⁺–F⁻ separation in the crystal of interest. Only the static theory is reproduced; the temperature-dependent soft-phonon contribution is not included.

## Reproduction target
Produce the static transferred hyperfine constants for the F⁻ ion at the Mn²⁺–F⁻ distance of 2.58 Å. Specifically, compute the isotropic constant A_s (in MHz) and the total anisotropic constant A_aniso (in MHz), defined as the geometric mean A_aniso = sqrt(Aσ² + Aπ²). These quantities must be written to the JSON file `/app/outputs/hyperfine_constants.json` with keys `As_MHz` and `A_aniso_MHz`. The underlying integrals, amplitudes, and spin densities are required intermediate stages and must be documented in the supporting artifacts `integrals.json` and `spin_densities.json`.

## Assets

- Clementi and Roetti Hartree-Fock atomic wave functions (1974): 10.1016/S0092-640X(74)80002-8

## Workflow steps

### Step 1: Compute two-center integrals
- Role: process
- Action: For the orbital pairs (1s, 2s, 2pσ, 2pπ of F⁻ with 3d_z² and 3d_t of Mn²⁺) at interatomic distance R=2.58 Å, compute overlap integrals, kinetic integrals, and the four types of Coulomb integrals required for the transfer coefficient γ (⟨a3a1||a3a3⟩, ⟨a1a3||a1a3⟩, ⟨a1a1||a3a1⟩, ⟨a1a1||a1a1⟩) using Hartree-Fock wave functions from Clementi & Roetti (1974).
- Evidence: `/app/outputs/integrals.json`

### Step 2: Compute transfer coefficient, λ amplitudes, and spin densities
- Role: process
- Action: Using the integrals from step01 and the configurational energy difference Δ_B = -1.0 a.u., compute the transfer coefficient γ for each orbital pair via the Serber-expression. Determine the ligand admixture amplitudes λ_s, λ_σ, λ_π from γ and overlap integrals. Compute the spin densities: 2s spin density f_s (including the 1s-2s cross term), 2pσ spin density f_σ, and 2pπ spin density f_π from λ².
- Evidence: `/app/outputs/spin_densities.json`

### Step 3: Calculate static transferred hyperfine constants
- Role: scored (load-bearing)
- Action: Using the spin densities from step02 and the following fixed parameters: electronic g=2.0023, Bohr magneton, nuclear g-factor for ¹⁹F (5.256), nuclear magneton, total spin S=5/2, |χ_s(0)|² for 2s, and ⟨r⁻³⟩ for 2p. Compute the isotropic hyperfine constant A_s and the anisotropic components A_σ, A_π. Convert to MHz and report As_MHz and the total anisotropic constant A_aniso_MHz = sqrt(Aσ_MHz² + Aπ_MHz²) in a JSON file.
- Output file: `/app/outputs/hyperfine_constants.json`
- Format: json
- Contract: {"As_MHz": <float>, "A_aniso_MHz": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
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

Notes: The checker compares As_MHz and A_aniso_MHz to the paper-reported values with a relative tolerance (scoring partial credit up to 30% deviation). Only the static theory is scored; the soft-phonon contribution is omitted as it relies on experimental input.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

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
A hidden verifier will independently check each scored workflow artifact. The final hyperfine constants file (`hyperfine_constants.json`) is the primary scored output; the supporting artifacts (`integrals.json` and `spin_densities.json`) are also evaluated as evidence that the pipeline was genuinely executed. Each artifact is scored according to a hidden criterion that rewards solutions that faithfully carry out the described first-principles procedure. The final reward is a weighted combination of the per-artifact scores. Simply echoing numbers from the literature, without having performed the required computational steps, will not receive full credit.
