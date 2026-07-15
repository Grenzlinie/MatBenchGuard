# COMPUTER SIMULATION STUDIES OF ZEOLITE STRUCTURE AND STABILITY

R.A. JACKSON, R.G. BELL and C.R.A. CATLOW

Department of Chemistry, University of Keele, Keele, Staffordshire ST5 5BG, U.K.

## ABSTRACT
This paper describes applications of the lattice energy minimization method to studies of zeolite structure and relative stability. Particular attention is paid to the effect of the presence of aluminium on the stability of different structures.

## INTRODUCTION
The lattice energy minimization method has recently been applied to the modelling of zeolite structures (ref. 1). This work, which shows that structures may be modelled with success, is summarized in a later section. The technique can also be applied to studies of the relative stability of zeolites, both structure-stability relationships within the siliceous zeolites, and the effect on stability of aluminium incorporation. This latter effect is of obvious importance from the zeolite synthesis point of view, and the extent to which the technique can predict the relative stability of a zeolite with particular Si/Al ratio is important. In this paper, the lattice energy minimization method is described, and the interatomic potentials employed are discussed. This is followed by a summary of the structural work. The main part of the paper concerns the calculation of relative stabilities, both for siliceous zeolites and as a function of Si/Al ratio. A final discussion summarizes the present status of the calculations, and future aims of the work.

## DETAILS OF CALCULATIONS
### (i) Lattice energy minimization
The lattice energy minimization method is used to calculate minimum lattice energies and the corresponding crystal structures and lattice properties. It requires as input a starting structure and a set of interatomic potentials. The choice of potentials is of great importance, and is discussed in part (ii) of this section. The calculation of structures corresponding to a a minimum in the lattice energy can be carried out in two ways. A constant volume energy minimization adjusts atom positions but holds the unit cell fixed; a constant pressure minimization additionally adjusts the lattice parameters. A second derivative (Newton-Raphson) scheme is used in the minimization. For completeness it is noted that a free energy minimization method

has recently been developed (ref. 2). This allows the effect of temperature to be included in the simulations, and will have important future applications to zeolites.

### (ii) Interatomic potentials
The potential model used in these calculations has the same general form as that used in the simulation of a wide variety of ionic and semi-ionic materials (see, e.g. ref. 3). The interaction between any pair of ions has the form:

$$
V(r) = \frac{q_i q_j}{r_{ij}} + A \exp(-r_{ij}/\rho) - Cr^{-6}
$$

where $q_i$ and $q_j$ are the charges on ions i and j, and $A$, $\rho$, $C$ are parameters which may be obtained by empirical fitting or by direct calculation. Formal ion charges are used, and ionic polarisability may be included using the shell model (ref. 4) which treats each (polarisable) ion as a core and a shell, coupled by a harmonic spring. The charge is then distributed between the core and the shell. In addition, in silicate and aluminosilicate systems an extra term is included in the potential to account for the directionality of bonding of oxygen ions about silicon (and aluminium, when tetrahedrally coordinated). This term has the form:

$$
V \text{ (bond bending)} = \frac{1}{2} k (\theta - \theta_0)S^2
$$

where $k$ is a fitted parameter, and $\theta_0= 109.47^\circ$ for $SiO_2$ bonds. For zeolites, the potential used was obtained as follows. The Si-O potential was obtained by fitting to the $\alpha$-quartz structure and lattice properties (ref. 5). The Al-O potential was transferred from a fit to $Al_20_3$ (ref. 6) and then on framework cation-oxygen parameters were calculated directly by electron gas methods. All parameters are tabulated (ref. 1).

## SUMMARY OF STRUCTURAL CALCULATIONS
Recent structural calculations using lattice energy minimization have been described in a previous publication (ref. 1). The conclusions from this work will be summarized here. The calculations were carried out to determine the extent to which lattice energy minimization can reproduce zeolite crystal structures, and whether there is much sensitivity to details of potential. Zeolite Na-A was taken as an example, using the structure as determined by Pluth and Smith (ref. 7). The minimum energy structure was then calculated using a range of potential models, but all based on the potential obtained from $\alpha$-quartz, described in the previous section. Comparison of calculated and experimental bond lengths and angles was then made and the following conclusions drawn.

(i) Good general agreement with experiment is obtained with all potentials

(ii) Rigid ion and shell model potentials perform equally well in this example, although shell model potentials can often give more detailed structural information.

(iii) The good agreement that is achieved is encouraging in view of the fact that all the potentials used were obtained by fitting to other structures or by direct calculation.

(iv) This example involved 'calibrating' the potentials against a known structure. The results suggest that, with these potentials, lattice energy minimization can be used predictively, and this has been done in the relative stability calculations described in the next section.

(v) Apart from zeolite A, the same potential has been used successfully in structural simulations of other zeolites, and also for a range of layered aluminosilicates.

### Relative stabilities of siliceous zeolites
By calculating the minimum lattice energies for a range of zeolites, relative stabilities may be obtained. Table 1 gives the lattice energies per $SiO_2$ unit for a range of zeolites, with $\alpha$-quartz for comparison. It is observed that silicalite is the most stable structure; this accords with the results of synthesis experiments.

**TABLE 1**
Relative stabilities of siliceous zeolites.

<table>
  <thead>
    <tr>
      <th>zeolite</th>
      <th colspan="2">lattice energy per $SiO_2$ unit (eV)</th>
    </tr>
    <tr>
      <th></th>
      <th>rigid ion</th>
      <th>shell model</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>faujasite</td>
      <td>-123.48</td>
      <td>-128.45</td>
    </tr>
    <tr>
      <td>zeolite A</td>
      <td>-123.66</td>
      <td>-128.47</td>
    </tr>
    <tr>
      <td>mordenite</td>
      <td>-123.80</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <td>silicalite</td>
      <td>-123.89</td>
      <td>-128.59</td>
    </tr>
    <tr>
      <td>$\alpha$-quartz</td>
      <td>-123.90</td>
      <td>-128.64</td>
    </tr>
  </tbody>
</table>

### Effect of Aluminium Incorporation
The addition of aluminium to a siliceous zeolite will affect the stability, so calculations can play an important role here. These calculations were performed in two ways.

(i) **Averaged Al distribution.** A simple approach to the problem of inclusion of Al is to average the negative charge introduced by Al over all the tetrahedral sites- i.e. to lower the Si charge by an appropriate amount. This approach was used for faujasite and mordenite, and Table 2 gives the relative stabilities as a function of Si/Al ratio.

<table>
<caption>TABLE 2 Relative Stability of Faujasite and Mordenite as a function of Si/Al ratio.</caption>
<thead>
  <tr>
    <th>Si/Al ratio</th>
    <th colspan="2">lattice energy per TO₂ unit (eV), rigid ion model</th>
  </tr>
  <tr>
    <th></th>
    <th>faujasite</th>
    <th>mordenite</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>infinity</td>
    <td>-123.48</td>
    <td>-123.80</td>
  </tr>
  <tr>
    <td>5</td>
    <td>-116.59</td>
    <td>-116.75</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-110.10</td>
    <td>-108.52</td>
  </tr>
  <tr>
    <td>1.4</td>
    <td>-106.83</td>
    <td></td>
  </tr>
</tbody>
</table>

These results show how the relative stability decreases as a function of increasing Al content, and it is clear that there will be a maximum amount of Al that can be added before the calculations will predict an unstable product. Therefore, for faujasite, mordenite and silicalite, calculations were performed to establish the range of Si/Al ratio over which these zeolites are stable. The results are compared with the corresponding experimental results from synthesis work, in which the three zeolites are synthesized with varying Si/Al ratios. Fig. 1 shows the maximum predicted Al/Si ratios from calculation and experiment, and suggests that calculations of this kind can be used to predict stabilities as a function of this ratio.

![](./images/811926246437945346_1.jpg)

Fig. 1. Maximum predicted Al/Si ratio for ZSM-5, mordenite and faujasite.

(ii) Calculations with explicit Al distributions. Calculations have also been carried out in which aluminium ions have been included explicitly. The aim of this work is to look at Al distributions in more detail than is possible with the averaged approach given above. In this paper, calculations are reported of the energies of substitution of Al ions at Si sites in 4 zeolites, using two calculation methods. The first is the method already described, lattice energy minimization, in which one aluminium is introduced into the unit cell. For comparison, the same energies have

been calculated using an alternative approach based on the defect simulation code CASCADE (ref. 8). This code is used to calculate the energy to substitute an Al at a Si site in an infinite lattice. These two slightly different approaches will be expected to be in reasonable agreement for low concentrations of Al, as is the case here. Table 3 gives the energies calculated using the two methods. It can be seen from this table that, while the energy differences are all of the same order, the trends observed from the averaged calculations are reproduced, i.e. the trend of ease of Al incorporation is faujasite > zeolite A > mordenite > silicalite. Calculations are in progress for incorporation of larger numbers of Al ions, which will provide a further test of the averaged calculations.

TABLE 3
Substitution Energies for a Single Al Atom in Siliceous Zeolites (eV).

<table>
  <thead>
    <tr>
      <th></th>
      <th>constant volume<br>energy minimization</th>
      <th>defect calculation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>faujasite</td>
      <td>37.54</td>
      <td>37.82</td>
    </tr>
    <tr>
      <td>zeolite A</td>
      <td>37.74</td>
      <td>38.06</td>
    </tr>
    <tr>
      <td>mordenite</td>
      <td>38.05</td>
      <td>38.29</td>
    </tr>
    <tr>
      <td>silicalite</td>
      <td>38.04</td>
      <td></td>
    </tr>
  </tbody>
</table>

SUMMARY AND CONCLUSIONS

This paper has considered the application of lattice energy minimization to the calculation of the relative stabilities of zeolite structures. In the case of the effect of Al incorporation, averaged calculations have been carried out, which agree well with experiment on the important question of the dependence of stability on Si/Al ratio. This work is being reinforced by calculations which consider explicit inclusion of Al, and preliminary results confirm the findings of the averaged studies. So far, calculations have only considered one Al per unit cell. Calculations in progress will consider the full range of Si/Al ratios.

ACKNOWLEDGEMENTS

We are grateful to Shell Research BV for financial support, and to R.A. van Santen, M.F.M. Post and C.J.J. den Ouden for useful discussions.

REFERENCES

1 R.A. Jackson and C.R.A. Catlow, Molecular Simulation, 1 (1988) 207.
2 S.C. Parker and G.D. Price, Advances in Solid State Chemistry, 1 (1989) (ed. C.R.A. Catlow), in press.
3 C.R.A. Catlow, C.M. Freeman, M.S. Islam, R.A. Jackson, M. Leslie and S.M. Tomlinson, Phil. Mag. A, 58 (1988) 123.
4 B.G. Dick and A.W. Overhauser, Phys. Rev. B, 112 (1958) 90.

5 M.J. Sanders, M. Leslie and C.R.A. Catlow, *J. Chem. Soc., Chem. Comm.,* (1984) 1273.

6 C.R.A. Catlow and R. James, *Proc. Roy. Soc. Lond,* A384 (1982) 157.

7 J.J. Pluth and J.V. Smith, *J. Am. Chem. Soc.,* 102 (1980) 4704.

8 M. Leslie, Daresbury Report DL/SCI/TM31T (1982).