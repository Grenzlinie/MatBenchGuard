# Ethanol Dehydrogenation on Silica: Cluster Model Energetics

## Problem background
Silicalite-1 and highly dehydrated silica contain distorted Si–O–Si bridges (active oxygen bridges) that catalyze the selective dehydrogenation of ethanol to acetaldehyde without transition metals. The reaction is proposed to proceed via dissociative adsorption of ethanol, forming adjacent hydroxyl and ethoxyl groups. The key open question is whether thermal vibrations at reaction temperature (above ~600 K) can bring the intermediate into configurations where the hydroxyl group becomes acidic and the ethoxyl group becomes reactive, leading to product formation. The present task uses quantum chemical calculations to assess the energetics of these intermediate configurations and their acidity/reactivity, providing a computational test of the proposed mechanism.

## Approach
The study employs ab initio SCF molecular orbital calculations at the HF/STO-3G level. The model system is a cluster representing a distorted Si–O–Si active bridge, with terminal Si atoms capped by (OH)L groups to mimic the silicate lattice. First, an optimized active bridge geometry is obtained by constrained displacement of two Si(O_LH)3 fragments along their local three-fold axes, starting from the crystal structure of the silicalite-1 pentasil ring. This bridge serves as the template. Next, isolated hydroxyl (–OH) and ethoxyl (–OC2H5) fragment clusters are optimized to determine their intrinsic geometries. Finally, four intermediate models (A43/43, B30/48, B53/30, B*) are constructed by combining these fragments and imposing specific O–Si–Si angle constraints that represent thermally excited conformations. For each model, a constrained SCF geometry optimization is performed; additionally, a single-point energy calculation on the deprotonated form of B30/48 yields the deprotonation energy. Relative energies between the intermediates and the acidity index are derived from the total energies.

## Reproduction target
Compute the total electronic energies (in eV, HF/STO-3G) for the four neutral intermediate cluster models (A43/43, B30/48, B53/30, B*) and for the B30/48 model after removal of the acidic proton H_a (deprotonated form). From these five energies, determine the relative energies of B30/48, B53/30, and B* with respect to A43/43, as well as the deprotonation energy E_a = E(B30_48_deprot) − E(B30_48). The required deliverables are the raw total energies; the checker will recompute the derived quantities.

## Assets

- PySCF: pyscf
- Silicalite-1 crystal structure (Olson et al. 1981): 10.1021/j150621a036

## Workflow steps

### Step 1: Optimize active oxygen bridge cluster
- Role: process
- Action: Construct the (HO_L)_3Si_a–O_x–Si_b(O_LH)_3 cluster using initial atomic coordinates derived from the silicalite-1 pentasil ring crystal structure. Fix the internal geometry of the Si(O_LH)_3 fragments as specified in the paper, and perform a constrained optimization by moving the two Si(O_LH)_3 fragments along their symmetric axes without rotation. Obtain the optimized Si_a–Si_b distance, Si–O_x bond length, and inter‑axial angles. This structure serves as the template for the intermediate models.
- Evidence: `/app/outputs/active_bridge_geometry.json`

### Step 2: Optimize isolated hydroxyl and ethoxyl fragment clusters
- Role: process
- Action: Build the isolated (HO_L)_3Si–OH cluster (model 1) and the isolated (HO_L)_3Si–OC2H5 cluster (model 2). Keep the Si(O_LH)_3 parts identical to the optimized active bridge template. Optimize the geometries of the –OH and –OC2H5 groups to obtain relaxed internal bond lengths and angles that will be used as fixed parameters when building the intermediate models.
- Evidence: `/app/outputs/fragment_geometries.json`

### Step 3: Compute total energies of intermediate models and deprotonated state
- Role: scored (load-bearing)
- Action: Assemble the intermediate cluster models A43/43, B30/48, B53/30, and B* by combining the optimized active bridge geometry and the fragment geometries. Apply the angle and distance constraints defined in the paper. For each model perform a constrained SCF geometry optimization at the HF/STO-3G level. Additionally, compute the total energy of the B30/48 model after removal of H_a (deprotonated form) at the neutral geometry. Write all five total electronic energies in eV to a JSON file.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: JSON object with keys: 'A43_43', 'B30_48', 'B53_30', 'B_star', 'B30_48_deprot'. Each value is a float representing the total HF/STO-3G electronic energy in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw total energies that the checker uses to recompute relative energies and deprotonation energy against hidden gold.
- schema:
  - `type`: object
  - `required`:
    - `A43_43`: float (eV)
    - `B30_48`: float (eV)
    - `B53_30`: float (eV)
    - `B_star`: float (eV)
    - `B30_48_deprot`: float (eV)

Notes: All energies must be reported in eV. The checker will compute ΔE(B30/48), ΔE(B53/30), ΔE(B*) relative to A43/43, and the deprotonation energy E_a = E(B30_48_deprot) - E(B30_48). Ordering and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "A43_43": "float (eV)",
          "B30_48": "float (eV)",
          "B53_30": "float (eV)",
          "B_star": "float (eV)",
          "B30_48_deprot": "float (eV)"
        }
      },
      "description": "Raw total energies that the checker uses to recompute relative energies and deprotonation energy against hidden gold."
    }
  ],
  "notes": "All energies must be reported in eV. The checker will compute ΔE(B30/48), ΔE(B53/30), ΔE(B*) relative to A43/43, and the deprotonation energy E_a = E(B30_48_deprot) - E(B30_48). Ordering and tolerances are hidden."
}
```

## How you are scored
Your submitted `/app/outputs/total_energies.json` is read by a hidden verifier that recomputes the relative energies ΔE(B30/48), ΔE(B53/30), ΔE(B*) and the deprotonation energy E_a. These values are compared against hidden reference values derived from the original study, using tolerances that account for implementation differences. The verifier also checks that the relative order ΔE(B30/48) < ΔE(B53/30) < ΔE(B*) holds. The reward is monotonic and directional: meeting or exceeding the reference stability (i.e., relative energies no larger than the reference thresholds, and a deprotonation energy consistent with the expected acidity) earns full credit, and credit degrades gracefully with larger deviations. A lazy reproduction that submits arbitrary numbers without running the constrained optimizations will not satisfy the hidden constraints and will score poorly.
