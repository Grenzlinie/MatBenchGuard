# Anharmonic oscillator fit to bismuth monohalide band heads

## Problem background
The bismuth monohalides BiF, BiCl, BiBr, and BiI all possess an X³Σ⁻ ground state that is split by spin–spin coupling into two fine-structure components, a lower X₁0⁺ state and an upper X₂1 state. The energy separation (electronic term value Tₑ) and the vibrational constants (ωₑ, ωₑxₑ) of the X₂1 state are fundamental quantities that characterize the electronic structure of these molecules. Emission spectra of the X₂1→X₁0⁺ transition have been recorded, providing a set of measured band-head wavenumbers for several isotopic species. From these wavenumbers, the molecular constants can be extracted by a least-squares fit to an anharmonic oscillator model.

## Approach
The measured band-head wavenumbers (digitised from the original publication and provided as the bundled CSV resource band_heads.csv) are fitted to the standard anharmonic oscillator expression for the transition wavenumber:

  ν = Tₑ + ωₑ'(v'+½) − ωₑxₑ'(v'+½)² − ωₑ''(v''+½) + ωₑxₑ''(v''+½)²

where primed constants refer to the X₂1 upper state and double-primed constants to the X₁0⁺ ground state. Cubic anharmonic terms (ωₑyₑ) can be omitted if they do not significantly improve the fit.

The fitting is performed separately for each target molecule. For BiF, the high-resolution band origins (identified in the data file) must be used; for Bi³⁵Cl, Bi⁷⁹Br, and BiI the medium-resolution band heads are sufficient. The ground-state vibrational constants may either be fixed to well-established literature values or fitted simultaneously with the upper-state constants. Standard non-linear least-squares optimisation (e.g., Levenberg–Marquardt) is applied. The workflow delivers the fitted X₂1 state constants for the four species as a single JSON file.

## Reproduction target
Use the bundled CSV file band_heads.csv, which contains (v', v'') assignments and band-head wavenumbers, to determine the electronic term value Tₑ, the harmonic frequency ωₑ, and the anharmonicity constant ωₑxₑ of the X₂1 state for each of the following four species:
- BiF (high-resolution band origins)
- Bi³⁵Cl
- Biy⁷Br
- BiI

Output the fitted constants as a single JSON object with top-level keys 'BiF_highres', 'Bi35Cl', 'Bi79Br', 'BiI', where each value is an object containing the floats 'Te', 'we', and 'wexe' (all in cm⁻¹). Write this object to the file /app/outputs/molecular_constants.json.

## Assets

- Band head wavenumbers for BiF, BiCl, BiBr, BiI
- SciPy: scipy

## Workflow steps

### Step 1: Fit molecular constants for X₂1 states
- Role: scored
- Action: Load band head wavenumbers from the bundled band_heads.csv. For each required molecule (BiF high-resolution origins, Bi³⁵Cl, Bi⁷⁹Br, BiI), select the appropriate (v', v'') transitions and their wavenumbers. Perform a least-squares fit of these wavenumbers to the anharmonic oscillator formula ν = T_e + ω_e'(v'+½) − ω_ex_e'(v'+½)² − ω_e''(v''+½) + ω_ex_e''(v''+½)² (cubic terms may be omitted). The agent may fix ground-state constants to literature values or fit them simultaneously. Output the fitted upper-state constants (T_e, ω_e, ω_ex_e) for each molecule to molecular_constants.json. Use the high-resolution band origins for BiF and the medium-resolution band heads for Bi³⁵Cl, Bi⁷⁹Br, BiI.
- Output file: `/app/outputs/molecular_constants.json`
- Format: json
- Contract: JSON object with keys 'BiF_highres', 'Bi35Cl', 'Bi79Br', 'BiI'. Each value is an object containing 'Te' (float, cm⁻¹), 'we' (float, cm⁻¹), 'wexe' (float, cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/molecular_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### molecular_constants.json
- path: `/app/outputs/molecular_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Molecular constants for the X₂1 states of bismuth monohalides obtained from least-squares fits to band head wavenumbers.
- schema:
  - `type`: object
  - `required`:
    - `BiF_highres`: object (keys: Te, we, wexe; all float in cm⁻¹)
    - `Bi35Cl`: object (keys: Te, we, wexe; all float in cm⁻¹)
    - `Bi79Br`: object (keys: Te, we, wexe; all float in cm⁻¹)
    - `BiI`: object (keys: Te, we, wexe; all float in cm⁻¹)

Notes: Only the X₂1 state constants are scored. The ground-state constants, the a2 state energy, Bi³⁷Cl, Bi⁸¹Br, and lower-resolution BiF constants are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "molecular_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BiF_highres": "object (keys: Te, we, wexe; all float in cm⁻¹)",
          "Bi35Cl": "object (keys: Te, we, wexe; all float in cm⁻¹)",
          "Bi79Br": "object (keys: Te, we, wexe; all float in cm⁻¹)",
          "BiI": "object (keys: Te, we, wexe; all float in cm⁻¹)"
        }
      },
      "description": "Molecular constants for the X₂1 states of bismuth monohalides obtained from least-squares fits to band head wavenumbers."
    }
  ],
  "notes": "Only the X₂1 state constants are scored. The ground-state constants, the a2 state energy, Bi³⁷Cl, Bi⁸¹Br, and lower-resolution BiF constants are not required."
}
```

## How you are scored
A hidden verifier reads your submitted molecular_constants.json and compares each reported Te, ωₑ, and ωₑxₑ to a predetermined reference (the published constants) using prescribed tolerances. The reward is proportional to the number of values that fall within the allowed ranges. Only the X₂1 state constants for the four species listed above are scored; ground-state constants and constants for other isotopic variants are not evaluated. The verifier also checks that the file is well-formed JSON that matches the required schema.
