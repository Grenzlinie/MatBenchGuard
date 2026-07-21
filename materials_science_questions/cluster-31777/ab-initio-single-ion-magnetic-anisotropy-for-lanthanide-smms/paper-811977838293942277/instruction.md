# Point charge electric field gradient computation for two dysprosium sites

## Problem background
DyNi3 is an intermetallic compound that crystallises in the PuNi3 structure type (space group R3m) and contains two inequivalent dysprosium sites. The electric field gradient (EFG) at the Dy nuclei can be described by a point charge crystal field model, which is used to interpret Mössbauer quadrupole coupling data and to connect the crystal structure with hyperfine interactions. Reproducing the computed EFG principal component eV_zz for both sites is a fundamental step in validating the point charge description.

## Approach
The calculation follows a point charge crystal field model. First, the crystal structure of DyNi3 (PuNi3 type, R3m) is used to compute the lattice parameter A₂⁰⟨r²⟩ for each Dy site, employing effective charges from the companion paper (Rossat-Mignod & Yakinthos, 1971), a shielding factor σ₂ = 0.6, and the radial expectation ⟨r²⟩ = 0.726 a.u. Second, the total EFG is assembled from a 4f contribution and a lattice (réseau) contribution, using the decomposition: eVzz = (1−R) eVzz_4f + (1−γ∞) eVzz_réseau. The 4f term involves the Stevens reduced matrix element for Dy³⁺, ⟨r⁻³⟩ = 9.2 a.u., and the expectation value ⟨3J_z²−J(J+1)⟩ evaluated with the magnetic moment orientations obtained from neutron diffraction: site I moment (10 μ_B) along the b axis, site II moment (10 μ_B) along the c axis. The lattice term is derived from A₂⁰⟨r²⟩, and the nuclear quadrupole moment Q = 2.6 barn is used to convert the field gradient to eV_zz. The fixed parameters R = 0.15 and (1−γ∞) = 80 are adopted from literature values.

## Reproduction target
Compute the principal component eV_zz for both dysprosium sites I and II using the point charge model and the nuclear parameters specified above. Output the two values in a JSON file efg_results.json with keys "site_I_eVzz" and "site_II_eVzz"; the units are erg/cm². The computation must be performed from the crystal structure and the model; do not simply copy the numbers from the literature.

## Assets

- Crystal structure of DyNi3 (PuNi3 type, space group R3m)
- Point charge model details from Rossat-Mignod & Yakinthos (1971): 10.1002/pssb.2220470132

## Workflow steps

### Step 1: Compute electric field gradients eVzz
- Role: scored (load-bearing)
- Action: Retrieve the crystal structure of DyNi3 from public databases (PuNi3 type, space group R3m). Perform a point charge crystal field calculation using shielding factor sigma2 = 0.6 and radial expectation <r^2> = 0.726 a.u. to obtain the lattice parameter A20<r2> for each Dy site. Then compute the electric field gradient principal component eVzz for both sites using the decomposition: eVzz = (1-R)*eVzz_4f + (1-gamma_inf)*eVzz_reseau, with R=0.15, (1-gamma_inf)=80, <r^{-3}>=9.2 a.u., Stevens factor for Dy3+, nuclear quadrupole moment Q=2.6 barn, and magnetic moment orientations: site I moment 10 mu_B along b axis, site II moment 10 mu_B along c axis. Output the final eVzz values in erg/cm^2 as a JSON file.
- Output file: `/app/outputs/efg_results.json`
- Format: json
- Contract: { "site_I_eVzz": <float>, "site_II_eVzz": <float> }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/efg_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### efg_results.json
- path: `/app/outputs/efg_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electric field gradient principal component eVzz for the two Dy sites, as computed from the point charge model.
- schema:
  - `type`: object
  - `required`:
    - `site_I_eVzz`: float (erg/cm^2)
    - `site_II_eVzz`: float (erg/cm^2)

Notes: The checker compares the agent's site_I_eVzz and site_II_eVzz to paper-reported values within a tolerance. The point charge calculation must be performed; the agent cannot simply look up the final answer.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "efg_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "site_I_eVzz": "float (erg/cm^2)",
          "site_II_eVzz": "float (erg/cm^2)"
        }
      },
      "description": "Electric field gradient principal component eVzz for the two Dy sites, as computed from the point charge model."
    }
  ],
  "notes": "The checker compares the agent's site_I_eVzz and site_II_eVzz to paper-reported values within a tolerance. The point charge calculation must be performed; the agent cannot simply look up the final answer."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads your efg_results.json. The verifier compares your computed site_I_eVzz and site_II_eVzz to reference values derived from the point charge model, within a tolerance that accounts for legitimate implementation differences. Full credit is awarded if both values fall within the tolerance band. Only the final eV_zz values are scored; intermediate artifacts are not evaluated. Reporting the paper's numbers without genuine calculation will not satisfy the verifier.
