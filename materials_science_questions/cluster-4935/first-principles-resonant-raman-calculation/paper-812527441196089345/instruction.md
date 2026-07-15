# Backscattering Raman Enhancement in Silicon Nanospheres via Mie Theory

## Problem background
High-refractive-index nanostructures can support low-loss optical resonances, including Mie-type resonances, that concentrate light on the nanoscale and produce strong electromagnetic near-field enhancements inside and around the structure. When such a nanostructure is made of a crystalline material like silicon, its intrinsic optical phonon modes generate a Raman scattering signal that is sensitive to the local electric field intensity. Because different optical resonances (electric dipole, magnetic dipole, magnetic quadrupole, and others) confine the field differently inside the material, they may each enhance the backscattering Raman intensity to a different degree. This task investigates the relationship between Mie resonances and Raman enhancement by computing the fields inside a single spherical silicon nanoparticle and calculating the resulting backscattering Raman intensity and the stored electric energy enhancement.

## Approach
The core idea is to treat spontaneous Raman scattering as a two-step electromagnetic process. First, an incident monochromatic plane wave at the excitation frequency excites a phonon mode inside the nanostructure; the local electric field at the excitation frequency determines the induced Raman polarization at each point. Second, the excited phonon radiates at the Stokes-shifted emission frequency (shifted by the silicon optical phonon energy). The backscattering Raman intensity collected along the illumination axis is obtained by: (1) solving Maxwell's equations for the nanoparticle at both frequencies to obtain the internal electric field distributions, (2) combining the excitation and emission fields into a position-dependent enhancement factor that assumes an isotropic Raman tensor and polarised detection parallel to the excitation polarisation, (3) integrating this enhancement factor over the nanoparticle volume, and (4) normalising by the Raman intensity that the same volume of bulk silicon would produce under identical illumination. In parallel, the stored electric energy enhancement at the excitation frequency is computed as the volume average of the squared field magnitude normalised by the incident field magnitude. For a spherical nanoparticle the electromagnetic problem is solved analytically using Mie theory, which gives the coefficients needed to construct the internal fields.

## Reproduction target
Use Mie theory (or an equivalent open-source implementation) to compute the normalised backscattering Raman enhancement and the stored electric energy enhancement for a single crystalline silicon nanosphere of radius 110 nm, illuminated at normal incidence by a plane wave whose electric field is linearly polarised. Perform the calculation at a range of excitation wavelengths from 400 nm to 800 nm inclusive (stepping by 10 nm is suggested). For each excitation wavelength, also compute the field at the Stokes-shifted emission frequency using the silicon optical phonon frequency of 520 cm⁻¹. Assume an isotropic Raman tensor and collect only the polarised backscattering component parallel to the excitation polarisation. Normalise the integrated Raman intensity by the corresponding bulk-silicon reference to obtain the dimensionless Raman enhancement. Write the results to a CSV file with columns wavelength_nm, raman_enhancement, and stored_energy_enhancement.

## Assets

- Silicon refractive index data: https://refractiveindex.info
- Silicon optical phonon frequency
- Mie scattering implementation: pyMieScatt

## Workflow steps

### Step 1: Compute Raman enhancement and stored electric energy enhancement
- Role: scored (load-bearing)
- Action: Using Mie theory, compute the internal electric field distributions inside a silicon nanosphere of radius 110 nm for normally incident plane waves at excitation wavelengths from 400 nm to 800 nm (e.g., step 10 nm) and at the Stokes-shifted emission frequency (shifted by the silicon optical phonon frequency of 520 cm^-1). Assume an isotropic Raman tensor and polarized detection parallel to the excitation polarization. Compute the backscattering Raman enhancement factor RE by integrating the enhancement factor over the sphere volume and normalizing by the bulk silicon reference. Also compute the stored electric energy enhancement as the volume average of |E|^2 / |E0|^2. Output a CSV file with these quantities.
- Output file: `/app/outputs/raman_enhancement_results.csv`
- Format: csv
- Contract: wavelength_nm: float (excitation wavelength in nm), raman_enhancement: float (dimensionless Raman enhancement ratio), stored_energy_enhancement: float (volume-averaged stored electric energy enhancement at excitation frequency)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raman_enhancement_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raman_enhancement_results.csv
- path: `/app/outputs/raman_enhancement_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the computed Raman enhancement and stored electric energy enhancement as functions of excitation wavelength for a silicon nanosphere of radius 110 nm.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `raman_enhancement`, `stored_energy_enhancement`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raman_enhancement_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "raman_enhancement",
          "stored_energy_enhancement"
        ]
      },
      "description": "CSV file containing the computed Raman enhancement and stored electric energy enhancement as functions of excitation wavelength for a silicon nanosphere of radius 110 nm."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently evaluates your submitted CSV file. The verifier recomputes the Mie solution for the same nanosphere and conditions using its own reference implementation, extracts the Raman enhancement values at selected excitation wavelengths, and compares them to your reported values. It also checks structural properties of the raman_enhancement curve (such as where the main peak occurs and whether the stored_energy_enhancement curve follows a consistent trend). Your reward is a float between 0 and 1: closer agreement yields a higher score, and exceeding a baseline accuracy ceiling earns full credit with no additional bonus. Submitting only the paper's reported numbers without performing the actual computation is not sufficient; the verifier evaluates the physical correctness of your output, not whether it matches a particular published figure.
