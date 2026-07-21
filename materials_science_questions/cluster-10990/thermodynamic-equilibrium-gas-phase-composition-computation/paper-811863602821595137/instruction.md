# Partial Pressure Calculation of Bi and Bi-O Vapor Species at 1400 K

## Background
In high‑temperature pyrometallurgy, bismuth vapor species and oxides influence impurity behavior. Published thermodynamic data have been compiled to produce standard Gibbs energy equations for the formation of gaseous Bi, Bi₂, Bi₃, Bi₄, BiO, Bi₂O, Bi₂O₂, Bi₂O₃, Bi₃O₄, and Bi₄O₆. These equations are used here to compute equilibrium partial pressures at 1400 K for two defined gas‑phase conditions.

## Provided thermodynamic equations
All equations have the form  
ΔG° = A + B T + C T ln T + D T² + E / T (J/mol).  
Temperature range: 544.59 K – 1600 K. Standard state for Bi is pure liquid, and the standard pressure is 1 atm = 101 325 Pa.  
Use the universal gas constant R = 8.314 J mol⁻¹ K⁻¹.

The reactions and their coefficients are:

| Reaction | A | B | C | D | E |
|----------|---|---|---|---|---|
| Bi(l) → Bi(g) | 190 523 | 100.3 | 0 | 0 | 0 |
| Bi₂(g) → 2 Bi(g) | 197 360 | 105.9 | 0 | 0 | 0 |
| Bi₃(g) → 3 Bi(g) | 319 671 | 231.1 | 0 | 0 | 0 |
| Bi₄(g) → 4 Bi(g) | 583 571 | 348.1 | 0 | 0 | 0 |
| Bi(g) + ½ O₂ → BiO(g) | −97 000 | −84.0 | 2.6 | −0.22 | 5.85 × 10⁶ |
| 2 Bi(g) + ½ O₂ → Bi₂O(g) (linear) | −706 200 | 2533 | −310 | 0.06 | 7.4 × 10⁷ |
| 2 Bi(g) + ½ O₂ → Bi₂O(g) (angular) | 2.9 × 10⁶ | −24 175 | 3290 | −1.1 | −5.0 × 10⁸ |
| 2 Bi(g) + O₂ → Bi₂O₂(g) | 2.64 × 10⁶ | 65 230 | 3190 | −1.1 | −4.8 × 10⁸ |
| 4 Bi(g) + 3 O₂ → Bi₄O₆(g) | −1.24 × 10⁶ | −4860 | 818 | −0.46 | −27 350 |
| 3 Bi(g) + 2 O₂ → Bi₃O₄(g) | 4.5 × 10⁶ | −43 560 | 6010 | −2.21 | −8.24 × 10⁸ |
| 2 Bi(g) + ³⁄₂ O₂ → Bi₂O₃(g) | 8.8 × 10⁶ | −70 770 | 9590 | −3.16 | −1.5 × 10⁹ |

## Task description
Use the equations above to compute the equilibrium partial pressures (Pa) of the eleven gas‑phase species at **T = 1400 K** for the two imposed conditions listed below. Assume ideal gas behavior and use the standard pressure **P° = 101 325 Pa** for all equilibrium calculations.

**Condition A**  
- P_Bi = 1.01 Pa  
- P_O₂ = 1.01 × 10⁻³ Pa  

**Condition B**  
- P_Bi = 1.01 × 10³ Pa  
- P_O₂ = 1.01 × 10⁻³ Pa  

For the dissociation reactions (Bi₂ → 2 Bi, etc.), convert ΔG° to the appropriate formation constant before applying the law of mass action. For the monomer Bi, the partial pressure is directly imposed by the condition.

## Output file
Write the results to `/app/outputs/step_04_partial_pressures.csv` with the following columns:  
`species`, `T`, `P_Bi_set`, `P_O2_set`, `P_partial`.  

- `species` : exact string from the list below  
- `T` : temperature in K (always 1400.0)  
- `P_Bi_set` : imposed monomer Bi partial pressure in Pa  
- `P_O2_set` : imposed O₂ partial pressure in Pa  
- `P_partial` : computed equilibrium partial pressure in Pa  

The file must contain one row for each of the 11 species under each condition (22 rows total). The allowed species names are:
`Bi`, `Bi2`, `Bi3`, `Bi4`, `BiO`, `Bi2O_linear`, `Bi2O_angular`, `Bi2O2`, `Bi2O3`, `Bi3O4`, `Bi4O6`.

**Important**: the hidden verifier compares your reported partial pressures against reference values computed from the same set of equations. Relative error tolerances are tighter for major species (Bi, Bi₂, BiO, Bi₂O_linear, Bi₂O_angular) and looser for the minor ones. A perfect score requires all 22 pairs to pass.

## Output contract (self‑check)
```json
{
  "outputs": [
    {
      "file": "step_04_partial_pressures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "T",
          "P_Bi_set",
          "P_O2_set",
          "P_partial"
        ],
        "column_types": {
          "species": "string",
          "T": "float",
          "P_Bi_set": "float",
          "P_O2_set": "float",
          "P_partial": "float"
        },
        "units": {
          "T": "K",
          "P_Bi_set": "Pa",
          "P_O2_set": "Pa",
          "P_partial": "Pa"
        },
        "allowed_species": [
          "Bi",
          "Bi2",
          "Bi3",
          "Bi4",
          "BiO",
          "Bi2O_linear",
          "Bi2O_angular",
          "Bi2O2",
          "Bi2O3",
          "Bi3O4",
          "Bi4O6"
        ]
      }
    }
  ],
  "notes": "Reference values are computed from the standard Gibbs energy equations provided above, using P° = 101325 Pa and ideal gas equilibrium."
}
```