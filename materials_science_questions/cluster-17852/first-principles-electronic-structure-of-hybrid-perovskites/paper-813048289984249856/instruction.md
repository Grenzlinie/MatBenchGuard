# First-Principles Electronic Structure of Hybrid Perovskites: Polymorphs, Bandgaps, and Effective Masses

## Problem background
Hybrid organic-inorganic halide perovskites such as methylammonium lead iodide (MAPbI3) are record-breaking light absorbers for photovoltaics, but they suffer from significant stability and environmental issues that hinder commercialization. The search for alternative perovskite compositions that maintain strong optoelectronic performance while improving stability is therefore of central importance. This task investigates a proposed analog, fluoroammonium lead triiodide (FNH3PbI3), by examining its structural polymorphs, electronic band structure, charge-carrier effective masses, and key intermolecular interaction strengths. The objective is to determine, via first-principles density functional theory (DFT) calculations, whether this material exhibits the lattice geometries, bandgap characteristics, and carrier transport properties suitable for photovoltaic and optoelectronic applications.

## Approach
The core approach is periodic DFT using the PBE (Perdew–Burke–Ernzerhof) functional and projector augmented wave (PAW) pseudopotentials, implemented in an open-source plane-wave code (Quantum ESPRESSO). Three polymorphs of FNH3PbI3 are considered: two pseudocubic forms with the FNH3+ cation oriented along the [110] and [111] directions, and one orthorhombic Pnma phase. Each unit cell is fully optimized (ion positions and cell shape/volume) until forces are converged. From the relaxed geometries, electronic band structures are computed along high‑symmetry k‑point paths, both without and with spin‑orbit coupling (SOC). The resulting band energies are then analysed to extract: (i) the fundamental bandgap (energy and direct/indirect character) for each polymorph and SOC case, (ii) for the pseudocubic polymorphs, the Rashba spin‑splitting energies and the momentum offset k0 of the band extrema, and (iii) the electron and hole effective masses derived from the curvature of the band edges. In a separate, complementary set of calculations, molecular fragments representative of the noncovalent I···H–N and I···F–N interactions that stabilize the pseudocubic and orthorhombic structures are carved out of the relaxed periodic geometries. Single‑point all‑electron PBE calculations (e.g., with the Def2‑TZVPPD basis set) are performed on these fragments to obtain basis‑set superposition error (BSSE) corrected binding energies. The final deliverables are four structured JSON files containing the optimized lattice parameters, the bandgaps and Rashba parameters, the effective masses, and the fragment binding energies.

## Reproduction target
You must produce the following computed quantities using open‑source tools (Quantum ESPRESSO for periodic DFT, Psi4 or ORCA for molecular fragments) and the PBE functional:

1. **Optimized lattice parameters** for the three FNH3PbI3 polymorphs: pseudocubic [110], pseudocubic [111], and orthorhombic. Report the relaxed cell constants (a, b, c), angles (α, β, γ), and cell volume.

2. **Bandgap energies and character** for each polymorph, both without spin‑orbit coupling (non‑SOC) and with spin‑orbit coupling (SOC). For the two pseudocubic polymorphs, also extract the Rashba splitting energies and the k‑point shifts for the conduction and valence band edges where applicable.

3. **Effective masses** of electrons and holes for each polymorph, derived from the band curvatures of the non‑SOC and SOC band structures. Express all masses in units of the free‑electron mass mₑ.

4. **Binding energies** (BSSE‑corrected) for the eight specific molecular fragments described in the protocol: five fragments from the pseudocubic phase (blocks C–G) and three fragments from the orthorhombic phase (blocks A–C). Report each binding energy in both kcal/mol and eV.

All outputs must be written to the specified JSON files under /app/outputs, adhering exactly to the given schemas.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Psi4: https://psicode.org/
- ORCA: https://orcaforum.kofo.mpg.de/
- EMSL Basis Set Exchange: https://bse.pnl.gov/bse/portal

## Workflow steps

### Step 1: Geometry optimization of FNH3PbI3 polymorphs
- Role: process
- Action: Construct initial structures for the three polymorphs (pseudocubic with FNH3+ oriented along [110] and [111], and orthorhombic Pnma) from standard perovskite templates and the lattice constants described in the method. Perform full periodic DFT geometry optimization using the PBE functional and PAW pseudopotentials. Use a plane-wave cutoff of approximately 520 eV, force convergence threshold of 0.0002 eV/Å, and appropriate k-point meshes (e.g., 12×12×12 for pseudocubic, 10×8×10 for orthorhombic). Relax the ion positions and cell shape/volume until forces are below the threshold.
- Evidence: `/app/outputs/geometry_optimization_completed.json`

### Step 2: Electronic band structure calculations
- Role: process
- Action: Using the relaxed geometries from step_geom_opt, compute electronic band structures along high-symmetry k-point paths for all three polymorphs. Perform two calculations per polymorph: one without spin-orbit coupling (non-SOC) and one with spin-orbit coupling (SOC). Use the same functional and pseudopotentials as in the geometry optimization. Save the energy eigenvalues along the k-point paths for later extraction of properties.
- Evidence: `/app/outputs/bandstructure_status.json`

### Step 3: Extract lattice parameters
- Role: scored
- Action: From the relaxed geometries of step_geom_opt, extract the optimized lattice constants (a, b, c) and angles (α, β, γ) for each polymorph, as well as the cell volume. Write the values to optimized_lattice.json.
- Output file: `/app/outputs/optimized_lattice.json`
- Format: json
- Contract: JSON object with keys "pseudocubic_110", "pseudocubic_111", "orthorhombic". Each value is an object with fields "a", "b", "c" (float, Å), "alpha", "beta", "gamma" (float, degrees), "volume" (float, Å^3).
- Scoring: scored by hidden verifier

### Step 4: Bandgap and Rashba parameter extraction
- Role: scored (load-bearing)
- Action: From the band structure results of step_bandstructure, determine the bandgap energies and nature (direct/indirect) for non-SOC and SOC cases for each polymorph. For the pseudocubic polymorphs, also extract the Rashba splitting energies for the conduction and valence bands and the k-point shifts (k0) where applicable. Write all values to bandgaps_and_rashba.json.
- Output file: `/app/outputs/bandgaps_and_rashba.json`
- Format: json
- Contract: JSON object with keys "pseudocubic_110", "pseudocubic_111", "orthorhombic". Each value is an object with: "Eg_nonSOC" (eV), "nature_nonSOC" (string "direct" or "indirect"), "Eg_SOC" (eV), "nature_SOC" (string). Additionally, for pseudocubic polymorphs include "Rashba_CB_splitting" (eV), "Rashba_VB_splitting" (eV), "k0_CB" (Å^-1), "k0_VB" (Å^-1). Use null for missing values (e.g., orthorhombic Rashba parameters).
- Scoring: scored by hidden verifier

### Step 5: Effective mass extraction
- Role: scored
- Action: For each polymorph, from the band curvatures near the conduction band minimum and valence band maximum in the non-SOC and SOC band structures, compute the electron and hole effective masses using m* = ħ² (∂²ε/∂k²)⁻¹. Write the results to effective_masses.json.
- Output file: `/app/outputs/effective_masses.json`
- Format: json
- Contract: JSON object with keys "pseudocubic_110", "pseudocubic_111", "orthorhombic". Each value is an object with: "mh_star_nonSOC", "me_star_nonSOC", "mh_star_SOC", "me_star_SOC" (all floats, in units of m_e).
- Scoring: scored by hidden verifier

### Step 6: Binding energy calculations for molecular fragments
- Role: scored
- Action: From the relaxed periodic structures of step_geom_opt, extract the molecular fragments corresponding to the blocks C–G in the pseudocubic phase (Figure 2) and the three blocks A–C in the orthorhombic phase (Figure 3) as described in the method. Perform single-point PBE calculations with an all-electron basis set (e.g., Def2-TZVPPD) to obtain the basis-set superposition error corrected binding energies ΔE(BSSE) in kcal/mol and eV. Write the results to binding_energies.json.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: JSON array of objects. Each object has: "system" (string, either "pseudocubic" or "orthorhombic"), "block_label" (string, e.g., "Fig2C", "Fig2D", ..., "Fig3A", "Fig3B", "Fig3C"), "ΔE_BSSE_kcal_per_mol" (float), "ΔE_BSSE_eV" (float). The list must contain exactly the eight blocks: five from the pseudocubic phase (C-G) and three from the orthorhombic phase (A-C).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lattice.json`
- `/app/outputs/bandgaps_and_rashba.json`
- `/app/outputs/effective_masses.json`
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lattice.json
- path: `/app/outputs/optimized_lattice.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Relaxed lattice constants and cell volume for each polymorph.
- schema:
  - `type`: object
  - `required`:
    - `pseudocubic_110`:
      - `type`: object
      - `required`:
        - `a`: number (Å)
        - `b`: number (Å)
        - `c`: number (Å)
        - `alpha`: number (degrees)
        - `beta`: number (degrees)
        - `gamma`: number (degrees)
        - `volume`: number (Å^3)
    - `pseudocubic_111`:
      - `type`: object
      - `required`:
        - `a`: number (Å)
        - `b`: number (Å)
        - `c`: number (Å)
        - `alpha`: number (degrees)
        - `beta`: number (degrees)
        - `gamma`: number (degrees)
        - `volume`: number (Å^3)
    - `orthorhombic`:
      - `type`: object
      - `required`:
        - `a`: number (Å)
        - `b`: number (Å)
        - `c`: number (Å)
        - `alpha`: number (degrees)
        - `beta`: number (degrees)
        - `gamma`: number (degrees)
        - `volume`: number (Å^3)

### bandgaps_and_rashba.json
- path: `/app/outputs/bandgaps_and_rashba.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed bandgap energies (with and without SOC), bandgap nature, and Rashba spin-splitting parameters for the pseudocubic polymorphs.
- schema:
  - `type`: object
  - `required`:
    - `pseudocubic_110`:
      - `type`: object
      - `required`:
        - `Eg_nonSOC`: number (eV)
        - `nature_nonSOC`: string ("direct" or "indirect")
        - `Eg_SOC`: number (eV)
        - `nature_SOC`: string
        - `Rashba_CB_splitting`: number (eV) or null
        - `Rashba_VB_splitting`: number (eV) or null
        - `k0_CB`: number (Å^-1) or null
        - `k0_VB`: number (Å^-1) or null
    - `pseudocubic_111`:
      - `type`: object
      - `required`:
        - `Eg_nonSOC`: number (eV)
        - `nature_nonSOC`: string
        - `Eg_SOC`: number (eV)
        - `nature_SOC`: string
        - `Rashba_CB_splitting`: number (eV) or null
        - `Rashba_VB_splitting`: number (eV) or null
        - `k0_CB`: number (Å^-1) or null
        - `k0_VB`: number (Å^-1) or null
    - `orthorhombic`:
      - `type`: object
      - `required`:
        - `Eg_nonSOC`: number (eV)
        - `nature_nonSOC`: string
        - `Eg_SOC`: number (eV)
        - `nature_SOC`: string
        - `Rashba_CB_splitting`: null
        - `Rashba_VB_splitting`: null
        - `k0_CB`: null
        - `k0_VB`: null

### effective_masses.json
- path: `/app/outputs/effective_masses.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Effective masses of electrons and holes for each polymorph, in units of the free electron mass.
- schema:
  - `type`: object
  - `required`:
    - `pseudocubic_110`:
      - `type`: object
      - `required`:
        - `mh_star_nonSOC`: number (m_e)
        - `me_star_nonSOC`: number (m_e)
        - `mh_star_SOC`: number (m_e)
        - `me_star_SOC`: number (m_e)
    - `pseudocubic_111`:
      - `type`: object
      - `required`:
        - `mh_star_nonSOC`: number (m_e)
        - `me_star_nonSOC`: number (m_e)
        - `mh_star_SOC`: number (m_e)
        - `me_star_SOC`: number (m_e)
    - `orthorhombic`:
      - `type`: object
      - `required`:
        - `mh_star_nonSOC`: number (m_e)
        - `me_star_nonSOC`: number (m_e)
        - `mh_star_SOC`: number (m_e)
        - `me_star_SOC`: number (m_e)

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Binding energies for the eight molecular blocks described in the method (five pseudocubic fragments and three orthorhombic fragments).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`:
      - `system`: string ("pseudocubic" or "orthorhombic")
      - `block_label`: string (e.g., "Fig2C" .. "Fig3C")
      - `ΔE_BSSE_kcal_per_mol`: number (kcal/mol)
      - `ΔE_BSSE_eV`: number (eV)

Notes: All values are to be determined from the agent's own DFT calculations using open-source tools (Quantum ESPRESSO for periodic, Psi4/ORCA for molecular). The hidden checker compares the reported numbers to the paper's values within method-dependent tolerances. Exact composition and geometric extraction details for the molecular fragments are described in the method; the agent must deduce them from the relaxed structures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lattice.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pseudocubic_110": {
            "type": "object",
            "required": {
              "a": "number (Å)",
              "b": "number (Å)",
              "c": "number (Å)",
              "alpha": "number (degrees)",
              "beta": "number (degrees)",
              "gamma": "number (degrees)",
              "volume": "number (Å^3)"
            }
          },
          "pseudocubic_111": {
            "type": "object",
            "required": {
              "a": "number (Å)",
              "b": "number (Å)",
              "c": "number (Å)",
              "alpha": "number (degrees)",
              "beta": "number (degrees)",
              "gamma": "number (degrees)",
              "volume": "number (Å^3)"
            }
          },
          "orthorhombic": {
            "type": "object",
            "required": {
              "a": "number (Å)",
              "b": "number (Å)",
              "c": "number (Å)",
              "alpha": "number (degrees)",
              "beta": "number (degrees)",
              "gamma": "number (degrees)",
              "volume": "number (Å^3)"
            }
          }
        }
      },
      "description": "Relaxed lattice constants and cell volume for each polymorph."
    },
    {
      "file": "bandgaps_and_rashba.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pseudocubic_110": {
            "type": "object",
            "required": {
              "Eg_nonSOC": "number (eV)",
              "nature_nonSOC": "string (\"direct\" or \"indirect\")",
              "Eg_SOC": "number (eV)",
              "nature_SOC": "string",
              "Rashba_CB_splitting": "number (eV) or null",
              "Rashba_VB_splitting": "number (eV) or null",
              "k0_CB": "number (Å^-1) or null",
              "k0_VB": "number (Å^-1) or null"
            }
          },
          "pseudocubic_111": {
            "type": "object",
            "required": {
              "Eg_nonSOC": "number (eV)",
              "nature_nonSOC": "string",
              "Eg_SOC": "number (eV)",
              "nature_SOC": "string",
              "Rashba_CB_splitting": "number (eV) or null",
              "Rashba_VB_splitting": "number (eV) or null",
              "k0_CB": "number (Å^-1) or null",
              "k0_VB": "number (Å^-1) or null"
            }
          },
          "orthorhombic": {
            "type": "object",
            "required": {
              "Eg_nonSOC": "number (eV)",
              "nature_nonSOC": "string",
              "Eg_SOC": "number (eV)",
              "nature_SOC": "string",
              "Rashba_CB_splitting": "null",
              "Rashba_VB_splitting": "null",
              "k0_CB": "null",
              "k0_VB": "null"
            }
          }
        }
      },
      "description": "Computed bandgap energies (with and without SOC), bandgap nature, and Rashba spin-splitting parameters for the pseudocubic polymorphs."
    },
    {
      "file": "effective_masses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pseudocubic_110": {
            "type": "object",
            "required": {
              "mh_star_nonSOC": "number (m_e)",
              "me_star_nonSOC": "number (m_e)",
              "mh_star_SOC": "number (m_e)",
              "me_star_SOC": "number (m_e)"
            }
          },
          "pseudocubic_111": {
            "type": "object",
            "required": {
              "mh_star_nonSOC": "number (m_e)",
              "me_star_nonSOC": "number (m_e)",
              "mh_star_SOC": "number (m_e)",
              "me_star_SOC": "number (m_e)"
            }
          },
          "orthorhombic": {
            "type": "object",
            "required": {
              "mh_star_nonSOC": "number (m_e)",
              "me_star_nonSOC": "number (m_e)",
              "mh_star_SOC": "number (m_e)",
              "me_star_SOC": "number (m_e)"
            }
          }
        }
      },
      "description": "Effective masses of electrons and holes for each polymorph, in units of the free electron mass."
    },
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": {
            "system": "string (\"pseudocubic\" or \"orthorhombic\")",
            "block_label": "string (e.g., \"Fig2C\" .. \"Fig3C\")",
            "ΔE_BSSE_kcal_per_mol": "number (kcal/mol)",
            "ΔE_BSSE_eV": "number (eV)"
          }
        }
      },
      "description": "Binding energies for the eight molecular blocks described in the method (five pseudocubic fragments and three orthorhombic fragments)."
    }
  ],
  "notes": "All values are to be determined from the agent's own DFT calculations using open-source tools (Quantum ESPRESSO for periodic, Psi4/ORCA for molecular). The hidden checker compares the reported numbers to the paper's values within method-dependent tolerances. Exact composition and geometric extraction details for the molecular fragments are described in the method; the agent must deduce them from the relaxed structures."
}
```

## How you are scored
A hidden verifier will independently inspect each of the four output files. For each file, the verifier compares the values you report to reference values derived from the original study, using tolerances that account for the expected variability when the same physical quantities are computed with different DFT implementations (e.g., Quantum ESPRESSO vs. the originally used VASP). The scores from the individual artifacts are combined by weight to yield a final reward between 0 and 1. Simply copying published numbers without performing the required calculations is not sufficient; the verifier expects numerical results that are consistent with an honest execution of the prescribed computational workflow.
