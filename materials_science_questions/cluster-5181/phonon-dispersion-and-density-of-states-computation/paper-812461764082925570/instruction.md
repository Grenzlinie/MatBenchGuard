# Non-local dielectric phonon frequencies and fields in superlattices

## Problem background
Polar optical phonons in semiconductor superlattices create electrostatic fields that govern carrier scattering and electron‑phonon interactions. Standard continuum dielectric models neglect the distinction between the local field that polarises the lattice and the actual test‑charge field, and thus fail to capture key features of the lattice dynamics. This task explores a non‑local dielectric response theory that properly accounts for these local‑field corrections. By solving an eigenvalue problem derived from a microscopic dielectric matrix, one can simultaneously obtain the direction‑dependent phonon eigenfrequencies and the associated mesoscopic electrostatic field profiles inside a superlattice. The model is applied to a (GaAs)₁₀(AlAs)₁₀ [001] superlattice, and the goal is to compute the long‑wavelength AlAs‑like phonon frequencies as a function of the propagation direction as well as the local electric field components at monolayer positions for the extreme propagation geometries.

## Approach
The core of the approach is a non‑local, frequency‑dependent dielectric matrix that couples different phonon branches through an irregular Coulomb term that depends on the direction of the phonon wave‑vector. The short‑range part of the interatomic interaction is described by dispersion functions fitted to bulk lattice‑dynamical calculations, while the long‑range part is built from effective transverse charges and a background dielectric constant. The full matrix is constructed in a basis of standing‑wave envelope functions that vanish outside the active AlAs layer, with effective layer widths that account for interface spread. Diagonalising this matrix for propagation directions from purely in‑plane to purely out‑of‑plane yields the phonon eigenfrequencies. The eigenvectors then give the electric field components at each monolayer position inside the supercell. The procedure separates modes by parity and polarization, so that the final eigenvalue problem reduces to a small matrix whose eigenvalues and eigenvectors are computed numerically, and from which the local field profiles are reconstructed directly.

## Reproduction target
Implement the non‑local dielectric eigenvalue problem for the (GaAs)₁₀(AlAs)₁₀ [001] superlattice using the provided short‑range dispersion parameters and effective charges. Compute the long‑wavelength AlAs‑like phonon eigenfrequencies for propagation directions ranging from entirely in‑plane to entirely out‑of‑plane (θ = 0° to 90° in 1° steps). For the AlAs‑like modes, compute the local electrostatic field components E_z(z) and E_x(z) at each monolayer position z within the supercell for the two limiting configurations θ = 0° (wave‑vector parallel to the growth direction) and θ = 90° (wave‑vector perpendicular to the growth direction). Output all computed frequencies (theta_deg, mode_index, frequency_cm⁻¹) and field profiles (mode_index, z_monolayer, E_z and E_x in meV/Å) in a single JSON file.

## Assets

- 11-parameter rigid-ion model for GaAs (Kunc et al. 1975): 10.1002/pssb.2220720125
- GaAs lattice constant and atomic masses: https://www.ioffe.ru/SVA/NSM/Semicond/GaAs/basic.html
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute phonon frequencies and fields from non-local dielectric model
- Role: scored (load-bearing)
- Action: Construct the non-local dielectric matrix for the (GaAs)10(AlAs)10 superlattice using the given short-range dispersion functions (Ω(k)=Ω−η(1−exp{−(k/χ)^R}) with fitted parameters: AlAs Ω=362 cm⁻¹, η_z=22, η_x=22, χ_z=1.36, χ_x=1.08; GaAs Ω=268 cm⁻¹, η_z=40, η_x=55, χ_z=1.54, χ_x=1.24), background dielectric constant ε∞=12, transverse charges from the Kunc rigid-ion model, and effective layer widths (d1=20a0+2δ1, d2=20a0+2δ2 with δ1=δ2=a0 for Γ1/Γ3 and δ1=δ2=0 for Γ5). Diagonalize the matrix for propagation directions spanning from purely in-plane to purely out-of-plane (θ = 0° to 90°, step 1°). From the eigenvectors, compute the local electric field components Ez(z) and Ex(z) at each monolayer position for the AlAs-like modes at θ=0° and θ=90°. Save all computed frequencies (theta_deg, mode_index, frequency_cm-1) and field profiles (mode_index, z_monolayer, Ez_meV_per_A, Ex_meV_per_A) to the output file.
- Output file: `/app/outputs/phonon_results.json`
- Format: json
- Contract: Object with keys 'frequencies' (list of {theta_deg: float, mode_index: int, frequency_cm-1: float}) and 'fields' (list of {mode_index: int, z_monolayer: int, Ez_meV_per_A: float, Ex_meV_per_A: float}).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_results.json
- path: `/app/outputs/phonon_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed phonon eigenfrequencies and local electrostatic field profiles for the (GaAs)10(AlAs)10 superlattice. The checker will recompute the RMSD of frequencies and the mean absolute relative error of field amplitudes compared to hidden reference values digitized from the paper.
- schema:
  - `type`: object
  - `required`:
    - `frequencies`: array of objects
    - `fields`: array of objects
  - `items`:
    - `frequency_item`:
      - `theta_deg`: number
      - `mode_index`: integer
      - `frequency_cm-1`: number
    - `field_item`:
      - `mode_index`: integer
      - `z_monolayer`: integer
      - `Ez_meV_per_A`: number
      - `Ex_meV_per_A`: number
  - `units`:
    - `frequency_cm-1`: cm⁻¹
    - `Ez_meV_per_A`: meV/Å
    - `Ex_meV_per_A`: meV/Å

Notes: The agent must implement the non-local dielectric eigenvalue problem using the supplied parameters. The output JSON must contain the full set of frequencies for all AlAs-like modes over θ=0..90° and the field profiles at θ=0° and θ=90°.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "frequencies": "array of objects",
          "fields": "array of objects"
        },
        "items": {
          "frequency_item": {
            "theta_deg": "number",
            "mode_index": "integer",
            "frequency_cm-1": "number"
          },
          "field_item": {
            "mode_index": "integer",
            "z_monolayer": "integer",
            "Ez_meV_per_A": "number",
            "Ex_meV_per_A": "number"
          }
        },
        "units": {
          "frequency_cm-1": "cm⁻¹",
          "Ez_meV_per_A": "meV/Å",
          "Ex_meV_per_A": "meV/Å"
        }
      },
      "description": "Computed phonon eigenfrequencies and local electrostatic field profiles for the (GaAs)10(AlAs)10 superlattice. The checker will recompute the RMSD of frequencies and the mean absolute relative error of field amplitudes compared to hidden reference values digitized from the paper."
    }
  ],
  "notes": "The agent must implement the non-local dielectric eigenvalue problem using the supplied parameters. The output JSON must contain the full set of frequencies for all AlAs-like modes over θ=0..90° and the field profiles at θ=0° and θ=90°."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact in your submission. For the phonon frequencies, the verifier computes a deviation measure across all angles and modes against reference values; for the electrostatic field profiles, it evaluates the agreement of the field amplitudes at each monolayer position. These two components are combined with predetermined weights to produce your final reward. Reporting a plausible number is not enough — the verifier compares your computed outputs to the expected physical results, and your score increases monotonically as your solution gets closer to the reference.
