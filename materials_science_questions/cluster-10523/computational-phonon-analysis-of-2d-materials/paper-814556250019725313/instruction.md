# Compute Cyclotron Transition Half-Width from Electron-Flexural Phonon Interactions in a Quantum Well

## Problem background
Electron–phonon interactions in semiconductor nanostructures strongly influence electronic transport and optical properties. In a quantum well under a perpendicular magnetic field, phonon-assisted cyclotron resonance (PACR) measures the absorption linewidth, providing insight into scattering mechanisms. This task focuses on the cyclotron transition line-width arising from electrons interacting with flexural confined acoustic phonons in a silicon infinite square well. The calculation uses a microscopic optical conductivity formula that accounts for the multiplicative effects of electron and phonon distribution functions, allowing a detailed treatment of phonon emission and absorption processes.

## Approach
Implement the theoretical formulation for the cyclotron transition line-width in a silicon quantum well. The real part of the optical conductivity near the cyclotron resonance is dominated by a line-width function that depends on the electron–phonon coupling. The electron states are quantized into Landau levels (transverse effective mass \(m_t\)) and electric subbands (longitudinal effective mass \(m_l\)) in an infinite square well of width \(L_z\). The electron–flexural phonon interaction is described by a deformation-potential coupling matrix element that involves the confined phonon displacement field and overlap integrals of the electron wavefunctions. The phonon confinement modifies the dispersion: the in-plane wavevector \(q_\parallel\) and the quantized perpendicular wavevectors \(q_{\mathrm{l},n}\) and \(q_{\mathrm{t},n}\) (branch index \(n\)) satisfy a pair of algebraic equations arising from the elastic boundary conditions. The line-width is obtained by summing over all allowed ‘implicit’ electron transitions (states \(\beta\)) that participate in phonon emission/absorption, with energy conservation enforced by a Dirac delta function in the transition factors. The computation is performed in the quantum limit, where the initial Landau index \(N_\alpha = 0\) and only the dominant implicit transitions (\(N_\beta = 0,1\) with electric subband pairs (1,2) and (2,3)) are retained. The silicon parameters are: \(m_t = 0.19\,m_e\), \(m_l = 0.92\,m_e\), mass density \(2.33\,\mathrm{g/cm^3}\), longitudinal sound speed \(8.97\times10^5\,\mathrm{cm/s}\), transverse sound speed \(5.37\times10^5\,\mathrm{cm/s}\), and deformation potential \(E_d = 7\,\mathrm{eV}\). Using these inputs, the procedure numerically solves the confined phonon dispersion at each \(q_\parallel\), evaluates the matrix elements, performs the sums over branches and implicit states, and computes the half-width \(\gamma_\alpha\) in meV. The calculation is repeated for a grid of temperatures, well widths, and magnetic fields as specified in the reproduction target.

## Reproduction target
Compute the cyclotron transition half-width (in meV) for silicon under the following three sequences of conditions, always using deformation potential \(E_d = 7\,\mathrm{eV}\):

1. Temperature dependence: \(T = 0, 10, 20, \dots, 100\,\mathrm{K}\) with \(B = 4\,\mathrm{T}\) and \(L_z = 31\,\mathrm{nm}\).
2. Well-width dependence: \(L_z = 20, 22, 24, \dots, 60\,\mathrm{nm}\) with \(T = 30\,\mathrm{K}\) and \(B = 4\,\mathrm{T}\).
3. Magnetic-field dependence: \(B = 2, 3, \dots, 8\,\mathrm{T}\) with \(T = 30\,\mathrm{K}\) and \(L_z = 45\,\mathrm{nm}\).

For each combination, output one row in a CSV file with the columns: `temperature_K`, `well_width_nm`, `magnetic_field_T`, `deformation_potential_eV`, `half_width_meV`. The CSV file must contain exactly these sequences; no other rows are required.

## Assets
No external datasets, models, or pre-trained weights are required. All necessary physical constants and material parameters are given in the task description and are publicly known. Standard scientific Python libraries (NumPy, SciPy, etc.) may be used and are available.

## Workflow steps

### Step 1: Compute cyclotron transition half-width
- Role: scored (load-bearing)
- Action: Compute the cyclotron transition half-width (in meV) for electrons in a silicon quantum well interacting with flexural confined acoustic phonons. Use the projection-reduction optical conductivity formula, including the microscopic expression for the line-width, the electron-flexural phonon coupling matrix element for an infinite square well, and the confined phonon dispersion equations. Perform the computation in the quantum limit (initial Landau index Nα=0) including the dominant implicit transitions. Use silicon parameters: transverse effective mass 0.19 m_e, longitudinal effective mass 0.92 m_e, mass density 2.33 g/cm³, deformation potential E_d = 7 eV, longitudinal sound speed 8.97×10⁵ cm/s, transverse sound speed 5.37×10⁵ cm/s. Evaluate the half-width at three sequences: (a) temperature from 0 to 100 K in steps of 10 K at B=4 T, L_z=31 nm; (b) well width from 20 to 60 nm in steps of 2 nm at T=30 K, B=4 T; (c) magnetic field from 2 to 8 T in steps of 1 T at T=30 K, L_z=45 nm. For each combination, write one row to halfwidths.csv with the columns: temperature_K, well_width_nm, magnetic_field_T, deformation_potential_eV, half_width_meV.
- Output file: `/app/outputs/halfwidths.csv`
- Format: csv
- Contract: CSV with header: temperature_K (integer/float), well_width_nm (float), magnetic_field_T (float), deformation_potential_eV (float), half_width_meV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/halfwidths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### halfwidths.csv
- path: `/app/outputs/halfwidths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the computed cyclotron transition half-width values for the flexural phonon mode at specified physical conditions.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `well_width_nm`, `magnetic_field_T`, `deformation_potential_eV`, `half_width_meV`

Notes: Only the flexural phonon mode is targeted; the dilatational mode is excluded. The checker recomputes gold half-widths at the agent's reported input conditions and applies a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "halfwidths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "well_width_nm",
          "magnetic_field_T",
          "deformation_potential_eV",
          "half_width_meV"
        ]
      },
      "description": "CSV file containing the computed cyclotron transition half-width values for the flexural phonon mode at specified physical conditions."
    }
  ],
  "notes": "Only the flexural phonon mode is targeted; the dilatational mode is excluded. The checker recomputes gold half-widths at the agent's reported input conditions and applies a relative tolerance."
}
```

## How you are scored
The hidden verifier independently recomputes the gold half-width value for each row in the submitted CSV using a reference implementation of the half-width formula. Your reported `half_width_meV` values are compared against these gold values using a relative tolerance; full credit requires all rows to pass within that tolerance. The verifier may also apply additional hidden checks of structural consistency, without disclosing the specific criteria. The overall score is a weighted combination of numeric agreement and structural integrity.
