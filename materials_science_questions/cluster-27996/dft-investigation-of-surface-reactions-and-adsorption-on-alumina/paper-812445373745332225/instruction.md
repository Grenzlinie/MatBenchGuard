# BOC-MP Calculation of Heats of Chemisorption and Activation Barriers on Ag(111)

## Problem background
Silver-catalysed oxidation of propylene and the transformations of allylic species (C₃H₅X, X=H, OH, O, Cl) are industrially important but mechanistically complex. The bond‑order conservation Morse‑potential (BOC‑MP) method provides a phenomenological analytical framework to predict heats of molecular chemisorption and intrinsic activation barriers from a small set of atomic binding energies. This task applies the BOC‑MP formalism to allylic species on a Ag(111) surface, computing energetic quantities that are relevant to understanding the preferred reaction pathways and the role of surface oxygen and chlorine. Reproducing these computed heats and barriers tests the predictive power of the BOC‑MP model for this class of surface reactions.

## Approach
The BOC‑MP method expresses molecular heats of chemisorption $Q$ and activation barriers $\Delta E^*$ solely in terms of atomic chemisorption energies $Q_{\mathrm A}$ and gas‑phase bond energies $D_{\mathrm{AB}}$, via the analytic equations given below. No structural (bond‑length) information is required; the coordination mode of each adsorbate is decided by comparing the $Q$ values predicted for the possible mono‑, di‑ and chelated sites.

**Atomic chemisorption energies** (zero‑coverage limit on Ag(111) are:
- $Q_{\rm H}=52$ kcal/mol (experimental)
- $Q_{\rm O}=80$ kcal/mol (experimental)
- $Q_{\rm C}=133$ kcal/mol (derived from $Q_{\rm C_2H_4}=9$ kcal/mol)
- $Q_{\rm Cl}$ is not reliably known; use the trial set $Q_{\rm Cl}\in\{50,55,60\}$ kcal/mol. For allyl chloride entries compute $Q$ for each trial value.

When a mono‑coordinated ($\eta^1$) molecule AB bonds through atom A to an on‑top site ($n=1$), the heat of chemisorption depends on the nature of A:
- **Strong bonding** (radicals with a localised unpaired electron, e.g. $\dot{\rm OH}$, $\dot{\rm CH}_2$, $\dot{\rm OCH}_2{\rm R}$):
  $$Q_{\rm AB} = \frac{Q_{\rm A}^{\,2}}{Q_{\rm A}+D_{\rm AB}} \tag{1}$$
- **Weak bonding** (closed‑shell molecules, e.g. ${\rm H_2O}$, ${\rm ROH}$, ${\rm RCHO}$, on‑top via O):
  $$Q_{\rm AB} = \frac{Q_{0\rm A}^{\,2}}{Q_{0\rm A}+D_{\rm AB}}, \qquad Q_{0\rm A}=Q_{\rm A} \tag{2}$$
- **Medium bonding** (mono‑valent carbon radicals such as $\dot{\rm CH}_2{\rm R}$ and $\sigma\!-\!\dot{\rm C}_3{\rm H}_5$):
  $$Q_{\rm AB} = \frac12\left( \frac{Q_{\rm A}^{\,2}}{Q_{\rm A}+D_{\rm AB}} + \frac{Q_{0\rm A}^{\,2}}{\frac13Q_{0\rm A}+D_{\rm AB}} \right), \qquad Q_{0\rm A}=Q_{\rm A} \tag{3}$$

For dicoordinated ($\eta^2$) species:
- **Homonuclear $\eta^2$** (two identical atoms, or a polyatomic molecule whose A–A vector is parallel to the surface, e.g. ${\rm C_2H_4}$):
  $$Q_{{\rm A}_2} = \frac{\frac92 Q_{0\rm A}^{\,2}}{3Q_{0\rm A}+8D_{{\rm A}_2}}, \qquad Q_{0\rm A}=Q_{\rm A} \tag{4}$$
  where $D_{{\rm A}_2}$ is the total energy of **all bonds formed by the A atom** (for ethene $D_{{\rm A}_2}=355$ kcal/mol).
- **Chelated $\eta^2$** (molecule coordinated via two different groups A and B):
  $$Q_{\rm AB(X)} = Q_{\rm A(X)}+Q_{\rm B(X)}-\frac{Q_{\rm A(X)}Q_{\rm B(X)}}{Q_{\rm A(X)}+Q_{\rm B(X)}} \tag{5}$$
  where $Q_{\rm A(X)}$ and $Q_{\rm B(X)}$ are the monocoordination chemisorption energies of the two groups.
- **Symmetric chelate** (A = B):
  $$Q_{{\rm A}_2(\rm X)} = \frac32 Q_{\rm A(X)} \tag{6}$$

Activation barriers are obtained from the computed $Q$ values:
- **Dissociation** ${\rm AB_s \to A_s + B_s}$:
  $$\Delta E^*_{\rm AB,s} = \frac12\!\left( \Delta H + \frac{Q_{\rm A}Q_{\rm B}}{Q_{\rm A}+Q_{\rm B}} \right), \qquad \Delta H = D_{\rm AB}+Q_{\rm AB}-Q_{\rm A}-Q_{\rm B} \tag{7}$$
- **Disproportionation** ${\rm A_s + BC_s \to AB_s + C_s}$:
  $$\Delta E^*_{\rm (AB)C,s} = \frac12\!\left( \Delta H + \frac{Q_{\rm AB}Q_{\rm C}}{Q_{\rm AB}+Q_{\rm C}} \right), \qquad \Delta H = (D_{\rm A}+D_{\rm BC}-D_{\rm AB}-D_{\rm C}) + Q_{\rm A}+Q_{\rm BC}-Q_{\rm AB}-Q_{\rm C} \tag{8}$$
- **Recombination** (reverse of dissociation) is obtained from thermodynamics.

**Species, coordination modes, and gas‑phase bond energies needed for Step 1**

For every row in the paper’s Table 1 (all values in kcal/mol):

| Species                         | Coordination mode / component D values                                                                          | Total $D$ (gas‑phase) |
|---------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------|
| H                               | atomic, $Q_{\rm H}=52$                                                                                         | 0                     |
| O                               | atomic, $Q_{\rm O}=80$                                                                                         | 0                     |
| C                               | atomic, $Q_{\rm C}=133$                                                                                        | 0                     |
| Cl (trial)                      | atomic, $Q_{\rm Cl}=50,55,60$                                                                                 | 0                     |
| OH                              | $\eta^1$(O) strong, $D = 102$                                                                                  | 102                   |
| H₂O                             | $\eta^1$(O) weak, $D = 220$                                                                                    | 220                   |
| CH₂=CH₂ (ethylene)              | $\eta^2$(C,C) homonuclear, $D_{\rm A_2}=355$                                                                  | 538                   |
| CH₂=CHCH₃ (propylene)           | $\eta^2$(C=C, H) chelate.  C=C group: homonuclear as ethylene ($Q=9$). H group: weak bonding, $D=86$, $Q_{\rm H}=52$ | 822                   |
| $\pi\-\mathrm{CH_2\!\sim\!CH\!\sim\!CH_2}$ (π‑allyl) | $\eta^2$(C,C) symmetric chelate. Each C treated as CH₂ radical: strong bonding, $D=130$. Compute $Q_{\rm CH_2}$ via eq. (1), then $Q_{\pi\text{-allyl}} = 3/2\,Q_{\rm CH_2}$ (eq. (6)). | 736                   |
| $\sigma\-\mathrm{CH_2\!=\!CH\!-\!CH_2}$ (σ‑allyl)    | Two modes: (i) $\eta^1$(C) medium bonding, $D=130$; (ii) $\eta^2$(C=C, C) chelate: C=C as ethylene, C radical medium bonding, $D=130$. | 722                   |
| CH₂=CHCH₂Cl (allyl chloride)    | $\eta^2$(C=C, Cl) chelate. C=C: as ethylene. Cl: weak bonding, $D=78$, using $Q_{\rm Cl}$ trial values.       | 803                   |
| CH₂=CHCH₂OH (allyl alcohol)     | $\eta^2$(C=C, O) chelate. C=C: as ethylene. O (alcohol): weak bonding, $D=92$.                            | 918                   |
| CH₂=CHCH₂O (allyl alkoxide)     | $\eta^2$(C=C, O) chelate. C=C: as ethylene. O (radical): strong bonding, $D=92$.                          | 816                   |
| CH₂=CHCHO (acrolein)            | $\eta^2$(C=C, O) chelate. C=C: as ethylene. O (carbonyl): weak bonding, $D=173$.                          | 802                   |
| C₆H₁₀ (1,5‑hexadiene, diallyl)  | $\eta^2$(C=C, C=C) chelate via two C=C groups, each $Q=9$; use eq. (5) with $Q_{\rm A}=Q_{\rm B}=9$.           | 1529                  |

**Reactions for which activation barriers are required (Step 2)**

*Table 3 — Reactions relevant to oxidation of propylene on Ag(111)*
| Reaction equation |
|---|
| $\mathrm{CH_2CHCH_{3,s} \rightleftarrows CH_2CHCH_{3,g}}$ |
| $\mathrm{CH_2CHCH_{3,s} \rightleftarrows \pi\!-\!CH_2CHCH_{2,s} + H_s}$ |
| $\mathrm{CH_2CHCH_{3,s} + O_s \rightleftarrows \pi\!-\!CH_2CHCH_{2,s} + OH_s}$ |
| $\mathrm{CH_2CHCH_{3,s} + OH_s \rightleftarrows \pi\!-\!CH_2CHCH_{2,s} + H_2O_s}$ |
| $\mathrm{\pi\!-\!CH_2CHCH_{2,s} + O_s \rightleftarrows CH_2CHCH_2O_s}$ |
| $\mathrm{CH_2CHCH_2O_s \rightleftarrows CH_2CHCHO_s + H_s}$ |
| $\mathrm{CH_2CHCH_2O_s + O_s \rightleftarrows CH_2CHCHO_s + OH_s}$ |
| $\mathrm{\pi\!-\!CH_2CHCH_{2,s} + O_s \rightleftarrows CH_2CHCHO_s + H_s}$ |

*Table 4 — Transformations of allyl alcohol and allyl chloride on Ag(111)*
| Reaction equation |
|---|
| $\mathrm{CH_2CHCH_2OH_s \rightleftarrows CH_2CHCH_2OH_g}$ |
| $\mathrm{CH_2CHCH_2OH_s \rightleftarrows CH_2CHCH_2O_s + H_s}$ |
| $\mathrm{CH_2CHCH_2OH_s \rightleftarrows \pi\!-\!CH_2CHCH_{2,s} + OH_s}$ |
| $\mathrm{CH_2CHCH_2OH_s + O_s \rightleftarrows CH_2CHCH_2O_s + OH_s}$ |
| $\mathrm{CH_2CHCH_2OH_s + OH_s \rightleftarrows CH_2CHCH_2O_s + H_2O_s}$ |
| $\mathrm{CH_2CHCH_2OH_s + \pi\!-\!CH_2CHCH_{2,s} \rightleftarrows CH_2CHCH_2O_s + CH_2CHCH_{3,s}}$ |
| $\mathrm{CH_2CHCH_2O_s \rightleftarrows CH_2CHCHO_s + H_s}$ |
| $\mathrm{CH_2CHCH_2O_s + O_s \rightleftarrows CH_2CHCHO_s + OH_s}$ |
| $\mathrm{CH_2CHCH_2O_s + OH_s \rightleftarrows CH_2CHCHO_s + H_2O_s}$ |
| $\mathrm{CH_2CHCH_2O_s + \pi\!-\!CH_2CHCH_{2,s} \rightleftarrows CH_2CHCHO_s + CH_2CHCH_{3,s}}$ |
| $\mathrm{CH_2CHCH_2Cl_s \rightleftarrows CH_2CHCH_2Cl_g}$   | (three rows for $Q_{\rm Cl}=50,55,60$)
| $\mathrm{CH_2CHCH_2Cl_s \rightleftarrows \pi\!-\!CH_2CHCH_{2,s} + Cl_s}$ | (three rows for $Q_{\rm Cl}=50,55,60$)
| $\mathrm{H_2O_s \rightleftarrows OH_s + H_s}$ |
| $\mathrm{H_2O_s + O_s \rightleftarrows 2\,OH_s}$ |
| $\mathrm{OH_s \rightleftarrows O_s + H_s}$ |

**Overrides for barrier calculations**
- For ALL reactions that involve $\mathrm{OH_s}$ or $\mathrm{CH_2CHCH_2O_s}$, DO NOT use the computed $Q$ values from Step 1. Instead use the experimentally adjusted values **$Q_{\rm OH}=55$ kcal/mol** and **$Q_{\rm OC_3H_5}=59$ kcal/mol** when evaluating eqs. (7)–(8).
- For the two allyl chloride reactions (desorption and dissociation) produce three separate entries, one for each trial $Q_{\rm Cl}\in\{50,55,60\}$, labelling them accordingly in the output table.

## Reproduction target
1. **Compute the heats of chemisorption** $Q$ (kcal/mol) and total bond energies $D+Q$ (kcal/mol) for every species listed in the input table above, using the BOC‑MP equations and the given atomic $Q_{\mathrm A}$ and bond‑energy $D$ values. Include the three $Q_{\rm Cl}$ variants for allyl chloride. Write the results to `table1_chemisorption_energies.csv`.
2. **Using the molecular $Q$ values from step 1 and the adjusted $Q_{\rm OH}$, $Q_{\rm OC_3H_5}$ where required**, compute the forward and reverse intrinsic activation barriers $\Delta E^{\,*}_{\rm f}$ and $\Delta E^{\,*}_{\rm r}$ (kcal/mol) for every reaction listed in the Tables 3 and 4 sections above. For allyl chloride reactions, produce entries for each trial $Q_{\rm Cl}$. Write the complete barrier table to `tables_3_4_activation_barriers.csv`.
Both files must follow the exact column order and types specified in the Output contract.

## Assets
No external assets are required. All needed atomic chemisorption energies ($Q_{\rm H}$, $Q_{\rm O}$, $Q_{\rm C}$, trial $Q_{\rm Cl}$), gas‑phase bond energies $D$, coordination‑mode assignments, and the BOC‑MP equations are provided directly in this task description.

## Workflow steps

### Step 1: Compute molecular heats of chemisorption (Table 1)
- Role: scored (load-bearing)
- Action: For OH, use the experimental value Q=55 kcal/mol from the paper; for CH₂CHCH₂O (allyl alkoxide), use the adjusted value Q=59 kcal/mol from the paper; these are not computed via the BOC‑MP equations. For all other species, implement the BOC-MP equations (A.1)–(A.7) using the provided atomic chemisorption energies Q_H=52, Q_O=80, Q_C=133, and trial Q_Cl={50,55,60} kcal/mol, the gas-phase bond energies D for each species from Table 1, and the appropriate coordination-mode assignments (monocoordination strong/weak/medium, dicoordination, chelated as described in the paper's appendix and fig. 1). Compute for every row in Table 1 the molecular heat of chemisorption Q and total bond energy D+Q. For allyl chloride, produce entries for each trial Q_Cl value.
- Output file: `/app/outputs/table1_chemisorption_energies.csv`
- Format: csv
- Contract: columns: species (string), coordination_mode (string), D_kcal_mol (float), Q_kcal_mol (float), D_plus_Q_kcal_mol (float)
- Scoring: scored by hidden verifier

### Step 2: Compute intrinsic activation barriers (Tables 3 and 4)
- Role: scored (load-bearing)
- Action: Using the previously computed molecular Q values and the fixed atomic Q_A values, apply BOC-MP formulas (A.8) and (A.9) to compute forward and reverse intrinsic activation barriers ΔE* for every elementary reaction listed in Tables 3 and 4. For reactions where adjusted experimental Q_OH=55 and Q_OC₃H₅=59 kcal/mol are required (as stated in the paper's text), replace the computed values accordingly. For allyl chloride reactions, produce entries for each trial Q_Cl value (50, 55, 60).
- Output file: `/app/outputs/tables_3_4_activation_barriers.csv`
- Format: csv
- Contract: columns: table_id (string, e.g. 'Table3' or 'Table4'), reaction_equation (string), Q_Cl_value_if_applicable (integer or empty), DeltaE_f_kcal_mol (float), DeltaE_r_kcal_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1_chemisorption_energies.csv`
- `/app/outputs/tables_3_4_activation_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1_chemisorption_energies.csv
- path: `/app/outputs/table1_chemisorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Heats of chemisorption and total bond energies for all atomic and molecular species listed in Table 1. The checker will recompute each value from the atomic Q_A and gas-phase D using the BOC‑MP formulas, compare within a tight tolerance, and score field‑wise exact‑match correctness. Note: OH uses Q=55 kcal/mol and allyl alkoxide uses Q=59 kcal/mol as per the paper's Table 1.
- schema:
  - `type`: table
  - `required_columns`: `species`, `coordination_mode`, `D_kcal_mol`, `Q_kcal_mol`, `D_plus_Q_kcal_mol`
  - `units`:
    - `D_kcal_mol`: kcal/mol
    - `Q_kcal_mol`: kcal/mol
    - `D_plus_Q_kcal_mol`: kcal/mol

### tables_3_4_activation_barriers.csv
- path: `/app/outputs/tables_3_4_activation_barriers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Intrinsic forward and reverse activation barriers for all elementary reactions in Tables 3 and 4. The checker recomputes each barrier from the agent's previous Q_AB values and the atomic Q_A using the BOC‑MP formulas, then compares against reference values within tolerance. For reactions involving OH or allyl alkoxide, the adjusted experimental Q values (55 and 59 kcal/mol) are used.
- schema:
  - `type`: table
  - `required_columns`: `table_id`, `reaction_equation`, `Q_Cl_value_if_applicable`, `DeltaE_f_kcal_mol`, `DeltaE_r_kcal_mol`
  - `units`:
    - `DeltaE_f_kcal_mol`: kcal/mol
    - `DeltaE_r_kcal_mol`: kcal/mol

Notes: Numerical tolerances are set according to the recompute tier (T1) to absorb floating‑point differences from independent implementations. The same atomic Q_A and gas‑phase D values as published in the paper are used by both agent and checker. The output schemas enforce the exact column order shown; the checker will read them by name.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1_chemisorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "coordination_mode",
          "D_kcal_mol",
          "Q_kcal_mol",
          "D_plus_Q_kcal_mol"
        ],
        "units": {
          "D_kcal_mol": "kcal/mol",
          "Q_kcal_mol": "kcal/mol",
          "D_plus_Q_kcal_mol": "kcal/mol"
        }
      },
      "description": "Heats of chemisorption and total bond energies for all atomic and molecular species listed in Table 1. The checker will recompute each value from the atomic Q_A and gas-phase D using the BOC‑MP formulas, compare within a tight tolerance, and score field‑wise exact‑match correctness. Note: OH uses Q=55 kcal/mol and allyl alkoxide uses Q=59 kcal/mol as per the paper's Table 1."
    },
    {
      "file": "tables_3_4_activation_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "table_id",
          "reaction_equation",
          "Q_Cl_value_if_applicable",
          "DeltaE_f_kcal_mol",
          "DeltaE_r_kcal_mol"
        ],
        "units": {
          "DeltaE_f_kcal_mol": "kcal/mol",
          "DeltaE_r_kcal_mol": "kcal/mol"
        }
      },
      "description": "Intrinsic forward and reverse activation barriers for all elementary reactions in Tables 3 and 4. The checker recomputes each barrier from the agent's previous Q_AB values and the atomic Q_A using the BOC‑MP formulas, then compares against reference values within tolerance. For reactions involving OH or allyl alkoxide, the adjusted experimental Q values (55 and 59 kcal/mol) are used."
    }
  ],
  "notes": "Numerical tolerances are set according to the recompute tier (T1) to absorb floating‑point differences from independent implementations. The same atomic Q_A and gas‑phase D values as published in the paper are used by both agent and checker. The output schemas enforce the exact column order shown; the checker will read them by name."
}
```

## How you are scored
A hidden verifier independently implements the same BOC‑MP equations (1)–(8) using the atomic $Q_{\rm A}$ and bond‑energy $D$ parameters given in this task. It recomputes every $Q$, $D+Q$, $\Delta E^{\,*}_{\rm f}$ and $\Delta E^{\,*}_{\rm r}$ value from your submitted CSV files and compares each numeric field against its own recomputed value within a tight tolerance. The final reward is the fraction of numeric fields in both scored files that agree within tolerance. Both CSV files must be present, contain the required columns with the correct names and types, and match the specified output schemas; structural or missing‑column errors reduce the score. You do not need to match any particular published number — only to produce values that a correct BOC‑MP calculation yields.
