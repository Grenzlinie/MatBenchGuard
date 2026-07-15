1018
# Molecular dynamics simulation of the phase transition in adamantane
A. S. TREW AND G. S. PAWLEY

Department of Physics, University of Edinburgh, King's Buildings, Edinburgh EH9 3JZ, U.K.
Received November 2, 1987

This paper is dedicated to Professor J. A. Morrison

A. S. TREW and G. S. PAWLEY. Can. J. Chem. 66, 1018 (1988).

Phase changes in adamantane have been studied by MD simulation on the DAP computers, using a zero-pressure technique to simulate clusters of 128 and 256 molecules where each member interacts with all others via the rigid molecule model and the 6-exp atom-atom potential. The form of the potential has been modified to permit the use of the 16 hydrogen sites only, giving a 65% saving in the calculation times. This model is shown to give lattice dynamics of adamantane closely similar to results with potentials which are generally accepted.

Using this potential the system equilibrates into the correct low temperature phase $(P \overline{4} 2_{1} c)$ and on heating, a transition is observed at $210 \pm 10 ~K$ to an $F m 3 m$ phase where the molecules lie preferentially in the $T_{d}$ orientations, as expected. Further heating beyond $240 \pm 15 ~K$ removes all apparent orientational order, though the underlying lattice is still fcc. On recooling the cluster from 300 to 100 K the orientational distribution function developed a significant degree of order as determined through the calculation of a correlation function designed to show any local order. This order is consistent with the lowest phase structure, but would in itself be insufficient to suggest a particular crystal structure.

A. S. TREW et G. S. PAWLEY. Can. J. Chem. 66, 1018 (1988).

Dans le but d'étudier les changements de phase de l'adamantane, on a fait appel à une simulation MD sur des ordinateurs DAP et on a utiliser une technique à pression zéro pour simuler des agrégats de 128 et 256 molécules dans lesquels chaque membre interagit avec tous les autres par le biais d'une molécule modèle et par le potentiel atome-atome au 6-exp. On a modifié la forme du potentiel pour permettre l'utilisation de seulement 16 sites d'hydrogène et on a ainsi sauvé 65% du temps de calcul. On démontre que ce modèle fournit des dynamiques du réseau de l'adamantane qui sont très semblables aux résultats obtenus avec des potentiels qui sont généralement acceptés.

Lorsqu'on utilise ce potentiel, le système s'équilibre et, à basse température, il atteint la bonne phase $(P \overline{4} 2_{1} c)$ par chauffage, on observe une transition à $210 \pm 10 ~K$ qui conduit à une phase $F m 3 m$ dans laquelle les molécules se trouvent préférentiellement, tel qu'attendu, dans les orientations $T_{d}$ . Si on continue le chauffage au-delà de $240 \pm 15 ~K$ , tout ordre apparent d'orientation est éliminé même si le réseau sous-jacent est encore fcc. En refroidissant l'agrégat de 300 à 100 K, la fonction de distribution de l'orientation présente un degré important d'ordre qui a été déterminé par le biais de calculs de la fonction de corrélation développée pour mettre en évidence l'ordre local. Cet ordre est en accord avec la structure de la phase la plus basse; toutefois, cet ordre serait insuffisant pour suggérer une structure cristalline particulière.

[Traduit par la revue]

## Introduction
There has been considerable interest for some time in the study of plastic crystals and their phase changes. Experimental measurements of deuterated adamantane using neutron coherent inelastic scattering when compared with model lattice dynamics calculations (1) suggested that simple atom-atom potentials would be appropriate for modelling. The use of these potential functions for molecular dynamics (MD) was then suggested as the obvious way to model the plastic phase. The computing power available at the time of these experiments was not sufficient for a serious attempt at a MD simulation, but now that very cost-effective computation can be done with parallel com- puters the problem becomes viable. In this paper we present the results of a MD investigation of the phase transition of adaman- tane in its deuterated form $(C_{10} D_{16})$ using the ICL Distributed Array Processor (DAP) (2).

A somewhat simpler problem was chosen to test the MD method for the modelling of plastic to crystalline phase transi- tions before embarking on adamantane. $SF_{6}$ was chosen because of its smaller size, and a simulation of a sample of 4096 mole- cules was done on the DAP. It was obvious at the outset that the conditions required of such phase transition studies included the control of the pressure of the system. A zero pressure simulation soon yielded a transition to a crystalline phase (3) which has now been shown to be found in nature (4). Another necessary condi- tion for a physically acceptable simulation is that the behaviour of the sample should not be determined by the boundary condi- tions, whatever these conditions may be. For $SF_{6}$ these were cyclic conditions, and there was clearly no finite-size artefact as the crystal phase developed as a mass of crystallites. A similar study of the phase transition in $n$ -butane (5) using the stress-free algorithm of Parrinello and Rahman (6) and recent unpublished work on adamantane both failed to give lower crystal phases, and another method is now sought to avoid any sample con- straints resulting from cyclic conditions.

Adamantane, or tricyclo-(3,3,1,1)-decane is one of the best known of plastic crystals. It has been extensively studied ex- perimentally (1, 7) and computationally (1, 8). It is a globular molecule displaying tetrahedral symmetry $T_{d}$ consisting of an octahedron formed by six methylene groups from which four methine groups extend. X-Ray diffraction studies (9, 10) show that at low temperatures the crystal has a $P \overline{4} 2_{1} c$ space group with $a=b=6.60 \AA, c=8.81 \AA$ , while above $208.6 ~K$ it transforms to a plastic phase with space group $F m 3 m, a=9.45 \AA$ . In the low temperature phase the molecules are oriented at an angle of $9^{\circ}$ relative to the $a$ or $b$ axes (9) while in the plastic phase they are randomly distributed between the two $T_{d}$ orientations (10). This is a rotationally frustrated state and so individual molecules will alternate dynamically between the two orientations. In addition, an ordered structure with space group $F 43 m$ has been reported at room temperature (11) but this is somewhat controversial and is thought to be due to the unusual annealing conditions for the crystals studied (10). The triple point of adamantane is 543 K but it sublimes easily even at room temperature as we find with our simulations.

We have chosen to perform MD calculations on a free cluster

in order to remove as much as possible the constrictions of boundaries. The simulation is therefore stress-free; the gain in avoiding self-image boundary condition artefacts is off-set to some extent by having a large fraction of the sample molecules involved with the cluster surface. Nevertheless we expect that our experience with $SF_{6}$ clusters containing similar numbers of molecules will be reflected in the adamantane simulations (12). For a sample of $128 SF_{6}$ molecules a phase change was clearly observed on cooling, this transition being exactly as observed in the cyclic boundary 4096 molecule simulation and was achieved in a fraction of the computer time. Diffraction patterns from larger cluster simulations of $SF_{6}$ have been compared with electron diffraction results using similar sized clusters, and give excellent agreement (13). These results lead us to conclude that there is a good proportion of molecules in orientations as found in the bulk, and that cluster simulations are well suited to the search for the solid state phase transitions we wish to study.

Earlier experiments had failed to find non-crystallographic structures from this molecular system (14), in contrast to the results from atomic clusters (15). Simulations have been done insearch of icosahedral structures in very small molecular (16, 17) and atomic (16, 18) systems, on 2-dimensional (19) and 3- dimensional (20) atomic liquid clusters, and on water (21) using the model of Stillinger and Rahman (22).

Thus although the simulation of clusters is now new, their use in the search for bulk properties in the solid has been neglected. Although the quantity of bulk material is reduced in free clus- ters, the method gives the possibility of studying other phe- nomena. Surface effects are an obvious area of study, but any defect in the bulk can now be studied, from vacancies and interstitials to twinning and grain boundaries. The technique is surprisingly efficient on the DAP. Nevertheless, it is a computa- tionally intensive method for very large systems when all possi- ble interactions are calculated, and this usually limits the size of the cluster to a few hundred molecules. Algorithms giving more efficiency for the very large systems will require more computer storage than is currently readily available; storage will certainly increase in future machines and the method will become more generally feasible.

## The simulations
The calculations were performed on the two ICL DAPs atEdinburgh University. These machines are SIMD arrays of 64 x 64 interconnected processing elements and are very well suited to problems which involve the calculation of many-bodyinteractions. The present problem runs with about $90 \%$  efficiency. The DAP has a speed of 20 Mflops but as such figures are always misleading we prefer to state that in this type of work the DAP is roughly $30 \%$ more powerful than a Cray-1 running an appropriate algorithm (D. Tildesley, private communica- tion).
To form the cluster, a spherical sample of molecules is cre- ated in the required initial crystalline state. Molecules are given translational and orientational order but with random linear and angular velocities obeying a gaussian distribution for the pre- scribed temperature. The interaction between each pair of atoms belonging to different molecules is then calculated and hence the resultant forces and torques on each molecule. These may then be used to predict the next configuration. Time integration is accomplished by use of the Beeman algorithm (23). This method is well known and extensively used and gives good energy stability in our calculations, provided that the time-step chosen is not too large. For all of this work, except immediately after initialisation of a new cluster, we have used a time-step of0.015 ps. The systematic energy fluctuation is then typically at most 1 part in $10^{6}$ per time-step. This is close to the precision expected from arithmetic round-off in performing the calcula- tions.
Restrictions on the amount of computer time available effec- tively determine the number of molecules in the system. Clus- ters with 128 adamantane molecules were chosen as the largest practicable for general investigations on the ICL DAP. Howev- er, we have also performed a number of simulations with 256 molecules and find that there is no qualitative difference in the results from these and the smaller systems. This is in agreement with previous investigations of $SF_{6}(12)$ by the cluster method which showed that the phases and transitions produced were independent of the number of molecules but that transition temperatures increased with cluster size.
A brief description of how the DAP is used to perform these calculations will help in understanding the applicability of SIMD computers to these problems. For our 128 moleculeproblem let us think of the molecule information arranged as 128 component vectors both along and top and down the side of a128 x 128 matrix. The components of this matrix can be used to contain the interaction between the row and column molecules, and the total force and torque on a particular molecule can then be found by summing the interactions by rows (or indeed by columns). Row summation is particularly easy on the DAP, as also is the row and column broadcasting needed before calculat- ing the interactions at the various matrix elements. The matrix elements are the processing elements (PEs) of the DAP, and as the DAP has only 64 x 64 PEs (32 x 32 in the AMT DAP 510), the mapping just described has to be done in stages, but this gives us the opportunity of avoiding most of the double calcula- tion implicit in the description above. In fact it is easy to avoid all double calculation except for the case where the number of molecules is N for a N x N DAP. For other mapping strategies the reader is referred to a paper devoted to SIMD mapping (24).
Let us now return to the adamantane simulations. As with previous investigations (1, 8) we assume a rigid molecule in- teracting via the 6-exp pairwise additive potential

$$\text { [1] } V(i, j)=-A_{a b} r_{i j}^{-6}+B_{a b} \exp \left(-C_{a b} r^{i j}\right)$$

where a and b indicate the species of the atoms at sites i and j, and $r_{i j}$ is the distance between two atoms belonging to different molecules. Several studies have been undertaken to measure the A, B, and C parameters for the H-H, C-H, and C-C interac- tions, most notably by Williams (25) and Kitaigorodskii (26), both of which give similar lattice dynamics (cf. Figs. 1 and 2). In these calculations the deuterated form of the molecule is used but the standard H-H potential is assumed for D-D. Because of the large amount of computation necessary for a complex molecule such as adamantane we have derived a modified H-H potential which when used on its own for adamantane gives the lattice dynamics of Fig. 3. The corresponding modes are easily identified, and the frequencies for the "reduced" potential are nicely bracketed by those of Williams and Kitaigorodskii. The rationale behind the simplification of the potential is that the molecule trajectories are principally determined by the interac- tions between the deuteriums, and the interactions involving the carbon atoms, being somewhat screened by the deuteriums, do not contribute significantly to the motion. The immediate con- sequence of this modification is that it permits the use of a "reduced molecule" of 16 atoms thus diminishing the amount of computation by a factor of $(26 / 16)^{2}$ . The smaller cluster there

![](./images/812087294566596608_1.jpg)

FIG. 1. Lattice dynamics calculations for the $P\overline{4}_{1}c$ phase of deuterated adamantane using the Williams (24) potential. The first four sections show the modes with wave-vectors in the $a-b$ plane, the last two sections show modes with wave-vectors along the $c$ axis. For $(\xi00)$ modes S and A mean, respectively, symmetric and antisymmetric with respect to the diad axis perpendicular to $c$. The representations for the $(\xi\xi0)$ modes are distinguished by the $z$ rotational and translational eigenvector components; when the former are symmetric, $S(rot)$, then the latter are antisymmetric, $A(trans)$, and vice versa. At (1/2, 1/2, 0) there are two representations, both doubly degenerate, in which $z$ rotation and translation only occur in the two branches which are continuous over this boundary. For $(00\xi)$, $z$ denotes modes with eigenvectors along the $c$ axis, $D(xy)$ means a double degeneracy with eigenvectors in the $a-b$ plane.

![](./images/812087294566596608_2.jpg)

FIG 2. Lattice dynamics calculations for the $P\overline{4}_{1}c$ phase of deuterated adamantane using the Kitaigorodskii (25) potential. The representations correspond to Fig. 1.

fore necessitates the calculation of $16^{2}\times128^{2}/2$ (about 2.2 million) forces per time-step and takes approximately 7 s on the DAP.

The modified potential has parameters $A_{\text{HH}}=128.25$ kcal $\text{mol}^{-1}\ \mathring{\text{A}}^{-6};B_{\text{HH}}=94500.0$ kcal $\text{mol}^{-1};C_{\text{HH}}=4.86\ \mathring{\text{A}}^{-1}$.

On initialisation, or after a temperature change, it is necessary to let the cluster equilibrate. This is done in effect by placing the system in a heat bath at the desired temperature and allowing it to gain or lose energy as necessary for temperature equalisation. This is achieved by the usual velocity/angular-velocity scaling. Given that the system may have to undergo a phase change, equilibration is deemed to have occurred when the potential energy stabilises. This usually takes from 5 to 10 ps, i.e. 1 250 to 2 500 time-steps.

### Analysis
We have used two basic techniques for analysing the clusters, an orientational and a structural analysis. These have been the working tools for understanding the simulations, and demonstrate the importance of graphics beyond that of result presentation.

#### (i) Orientational analysis
As the molecules have $T_{d}$ symmetry it is possible to project four vectors from the centre of the molecule through the tetrahedral vertices and onto the surface of a sphere, marking the points of intersection by a dot. Groups of molecules with similar orientations will then produce clustering of dots on the sphere. In fact because of the symmetry of the structures found, all

![](./images/812087294566596608_3.jpg)

FIG. 3. Lattice dynamics for the $P \overline{4}_{1} c$ phase of the reduced molecule using the modified H---H potential. The representations correspond to Fig. 1.

necessary information is contained within one hemisphere and we can thus confine attention to this. On average each molecule will give two dots, though producing one or three is also possi- ble. For representation in two dimensions the distance from the pole to each dot on the hemisphere is calculated and used as the radius for that dot on a plane, positioned at the same azimuthal angle. This gives an "equal-area" presentation, so that the densi- ty of dots on the plot corresponds exactly to the solid angle density of the orientational distribution function.

### (ii) Structural analysis
Although the dot-plots give a good overall impression of the orientational state of the molecules in the cluster they contain no information about the translational structure. While powder diffraction patterns could be produced to investigate this, the calculations are computationally intensive and the small size of our cluster (radius $\sim 20 \AA$) means that any features in the Fourier transform are rather broad. It is consequently difficult to mea- sure lattice spacings accurately, and we therefore use the mole- cule radial distribution function both to derive lattice spacings and to show any translational order. This works well, giving a typical peak of about $0.2 \AA$ full width at half maximum, and we are thus confident of the derived lattice spacings to about $0.1 \AA$.

## Results
The $P \overline{4} 2_{1} c$ to $F m 3 m$ phase transition involves a change in the definition of the $a$ and $b$ lattice vectors by a $45^{\circ}$ rotation about $c$. In order to avoid confusion about the directions of $a$ and $b$ we prefer to fix these parallel to those in the cubic system. This has the effect of increasing the quoted tetragonal lattice parameters by a factor of $\sqrt{2}(6.60 \to 9.33 \AA)$. However, this convention has an added bonus later when we attempt to determine the direction of the local $c$ axis.

Starting with an initial configuration at $100 ~K$ in the observed low-temperature phase, both the 128 and 256 molecule clusters equilibrated into the $P \overline{4} 2_{1} c$ state within 5-10 ps but with a unit cell $a=b=9.6 \AA, c=9.1$ A. This is approximately $3 \%$ larger than determined by X-ray diffraction studies of real crystals (9)—a discrepancy which is significant at the $1 \sigma$ level. However, lattice statics investigations of the low temperature phase using the modified potential also show a similar increase in the crystal- lographic cell. We are therefore confident that this is not a consequence of the free-boundary condition technique used, or the small size of the sample. Figure 4 shows the dot plot representations and radial distribution functions of the cluster in the tetragonal phase after equilibration at $100 ~K$. Examination of the orientational dot plot shows that the $9^{\circ}$ orientation of the molecules relative to the tetragonal axes is reduced to $4 \pm 1^{\circ}$. This may be correlated with the slight increase in cell size.

On heating to $220 ~K$ it was found that a phase change took place, as evident from Fig. 5. The new lattice has an fcc structure with $a=9.9 \AA$. This is a $6 \%$ increase on the ex perimental value, and the dot plot shows that the molecules have lost their orientation with respect to the tetragonal $a, b$ axes. The molecules are therefore adopting the expected tetrahedral orientations. Inspection of individual molecules shows jumps between the two $T_{d}$ orientations, but because of lack of compu ter time the statistics of reorientations are poor. We are, howev- er, confident that both the observed low and high temperature phases have been simulated.

Determination of transition temperatures in these simulations is difficult to achieve precisely. One method for improving the accuracy is to overlay dot plots generated by the addition of configurations for different times at the same temperature. Un- fortunately, calculation of sufficient data requires prohibitive amounts of computer time. Our best estimate of the transition temperature is $210 \pm 10 ~K$. It is not clear, given the uncertainty in this value and the interpretation difficulties on cooling, to determine whether there is hysteresis present on cooling.

Further heating of the fcc phase beyond $240 \pm 15 ~K$ gave a second change. Although the new structure maintained its fcc lattice with the same lattice parameter the molecular orientations became disordered, c.f. Fig. 6. The increased random compo- nent in the radial distribution function is due to surface relaxa- tion.

Recooling this phase to $100 ~K$ produced a structure with the same fcc lattice, $a=9.9 \AA$, but with a non-random orientational distribution — c.f. Fig. 7. A possible explanation is that the cluster has undergone the phase change back to the low tempera- ture phase but is no longer a single crystal, rather a collection of crystallites distinguishable by the direction of their $c$ axes.

![](./images/812087294566596608_4.jpg)

![](./images/812087294566596608_5.jpg)

FIG. 4 (a) Dot plot representation of the $P\overline{4}_{1}c$ phase at 100 K for the
256 molecule cluster. The lines indicating the two molecular orienta-
tions with respect to the tetragonal axes are also shown. (b) Radial
distribution function for the 256 molecule cluster at 100 K.

In order to investigate any short range order in the $c$-axis
direction we consider each molecule site in turn and calculate
the local lattice parameters by measuring the centre-to-centre
distances to the next molecule along the cubic cell directions.
Since the $c$ axis is the shortest of the three axes for the tetragonal
phase (in the cubic axial system) we may identify the smallest
measured distance as defining the local $c$-axis direction, pro-
vided that it is less than some limit, $c_{\text{max}}$, and that the data for the
site are complete (i.e. all three local cell parameters can be
found). Comparison of the state ($c$-axis direction) of a site with
that of its nearest neighbours, next nearest neighbours etc. can
then be used to form correlation functions on a variety of length
scales.

It is simple to predict the expected number of agreements
between sites on the basis of a random distribution of states. Let
us suppose that we have a number of sites, some fraction, $f$, of
which are assigned a state drawn randomly from $k$ posssible
states; in our case $k=3$. If $N$ comparisons are made, then,
taking care not to double count, the expected number of agree-
ments is

$$[2]\quad L=Nf^{2}/k$$

and hence the correlation function has a mean value, $w$, which is
simply

$$[3]\quad w=L/N=f^{2}/k$$

with a standard deviation given by the binomial distribution of

$$[4]\quad \sigma=\{f^{2}(1-f^{2}/k)\}^{1/2}$$

A value of unity for the correlation function can occur only for a
bulk sample because $f$ is reduced by the virtue of the cluster
surface. Figure 8 shows the observed correlation functions for
the nearest and next nearest neighbours respectively. The curves
are for configurations at 100 K (before heating, upper curve),
300 and 100 K (after cooling) together with those expected from
random crystallite orientations, denoted r 300 K and r 100 K for
the 300 K and 100 K (after cooling) configurations, respective-
ly. These random curves are calculated from eq. [3] using the
value of $f$ determined for that particular cluster and value of

![](./images/812087294566596608_6.jpg)

![](./images/812087294566596608_7.jpg)

FIG. 5. (a) Dot plot of the $Fm3m$ phase after heating to 220 K for the
128 molecule cluster. (b) Radial distribution function for the 128
molecule cluster at 220 K.

![](./images/812087294566596608_8.jpg)

FIG. 6. (a) Dot plot of the plastic phase after heating to 300 K for the 256 molecule cluster. (b) Radial distribution function for the 256 molecule cluster at 300 K.

![](./images/812087294566596608_9.jpg)

FIG. 7. (a) Dot plot of the $P\overline{4}_{1}c$ phase after cooling to 100 K from 300 K for the 256 molecule cluster. (b) Radial distribution function for the 256 molecule cluster cooled to 100 K.

$c_{\text{max}}$. Differences between random curves therefore reflect variations in the fraction of sites which are assigned $a$ state. Both diagrams display the same general features. The error bars are $\pm\sigma$; those on the observed curves are calculated from observed temporal fluctuations, while those on the random curves are a combination of these errors with those calculated from eq. [4].

Examination of these figures shows the high degree of order in the structure before heating. Also clear are the relative displacements along the abscissa of the correlation functions after heating to those before heating. This is caused by the lattice expansion already noted.

A comparison of the correlation functions at 300 K with the random curves shows that the simulation curves remain above the levels expected, although this is not statistically significant at the $2\sigma$ ($P < 5\%$) level. This may be indicative of some slight local correlation but a direct search for crystallites in the fcc structure proved unsuccessful. On cooling, the level of correlation rises to become statistically significant at the $2\sigma$ level and a number of possible "crystallites" can be identified in the larger cluster, though these are small and contain only a few molecules each. While the correlation functions have not reproduced the original degree of order, this would not be expected even from a polycrystalline system when compared with a single crystal, because of the disorder at crystallite boundaries. It may be supposed that these boundaries also contribute to the larger potential energy of the recooled cluster which, at 100 K is 23% more than at the same temperature before heating. Unfortunately, the system is so small that examination of the spatial distribution of the molecule potential energies does not show localised minima corresponding to the crystallites.

## Conclusions

A comprehensive MD study has been made of phase changes in adamantane using approximately 100 h of calculation time on the ICL DAPs at the University of Edinburgh. We have employed a $\text{H}—\text{H}$ potential modified so that when used on its own with deuterated adamantane it gives lattice dynamics similar to those of Williams (25) or Kitaigorodskii (26) in both high and low temperature phases. This enables the use of a reduced molecule of 16 atoms with a consequent reduction in the necessary calculation by 65%.

![](./images/812087294566596608_10.jpg)

FIG. 8. (a) Correlation functions for the nearest neighbours plotted as a function of the minimum acceptable value of $c$, $c_{\text{max}}$. (b) Correlation functions for the next nearest neighbours plotted as a function of $c_{\text{max}}$.

Using this potential we observe the system to equilibrate into the correct low temperature phase $(P\overline{4}2_1c)$ with lattice parameters only slightly larger than expected from lattice dynamics. This non-trivial achievement demonstrates that the modified potential and the reduced rigid molecule give a good model.

On heating the system a phase transition is observed at $210 \pm$ 10 K (experimental value 208.6 K) to a rotationally frustrated phase on a fcc lattice. Further heating removed the orientational order though the translational structure was preserved until sublimation took place.

Recooling the cluster to 100 K gave regions which could be identified as a collection of crystallites rather than a single crystal. This is not surprising since the cubic phase is not uniaxial and therefore there are three possible directions for the new local $c$-axis. We suppose that given sufficient time for annealing at an optimum temperature, or equivalently a very much slower cooling rate through the transition, larger crystallites could have been formed. Unfortunately, this would require much more computer time than is currently practicable, though with the rapid improvements in computer technology will soon render such simulations feasible.

Future work will involve the search for local transient ordering in the plastic phase and a study of reorientations in both the rotationally frustrated and orientationally disordered structures. Furthermore it is hoped that future simulations will help in the interpretation of the inelastic neutron scattering experiments which initiated this work (1, 7).

1. C. G. WINDSOR, D. H. SAUNDERSON, J. N. SHERWOOD, D. TAYLOR, and G. S. PAWLEY. J. Phys. C, 11, 1741 (1978).
2. R. W. HOCKNEY and C. R. JESSHOPE. Parallel computers. Adam Hilger, Bristol. 1981.
3. G. S. PAWLEY and G. W. THOMAS. Phys. Rev. Lett. 48, 410 (1982).
4. B. M. POWELL, G. DOLLING, G. S. PAWLEY, and L. S. BARTELL. Mol. Phys. In press.

5. K. REFSON and G. S. PAWLEY. Mol. Phys. **61**, 669 (1987); **61**, 693 (1987).

6. M. PARRINELLO and A. RAHMAN. Phys. Rev. Lett. **45**, 1196 (1980).

7. J. C. DAMIEN, J. LEFEBVRE, M. MORE, B. HENNION, R. CURRAT, and R. FOURET. J. Phys. C, **11**, 4323 (1978); C. G. WINDSOR, J. C. DAMIEN, J. LEFEBVRE, and R. M. RICHARDSON. J. Phys. C, **14**, 1555 (1981); M. BEE, J. P. AMOUREUX, and R. E. LECHNER. Mol. Phys. **40**, 617 (1980).

8. M. MEYER and G. CICCOTTI. Mol. Phys. **56**, 1235 (1985); M. MEYER, C. MARHIC, and G. CICCOTTI. Mol. Phys. **58**, 723 (1986); G. CICCOTTI, M. FERRARIO, E. MEMEO, and M. MEYER. Phys. Rev. Lett. **59**, 2574 (1987).

9. C. E. NORDMAN and D. L. SCHMITKONS. Acta Crystallogr. **18**, 764 (1965).

10. J. P. AMOUREUX, M. BEE, and J. C. DAMIEN. Acta Crystallogr. B**36**, 2633 (1980).

11. P. A. REYNOLDS. Acta Crystallogr. A**34**, 242 (1978).

12. A. H. FUCHS and G. S. PAWLEY. J. Phys. In press.

13. J. FARGES, M. F. DE FERAUDY, B. RAOULT, G. TORCHET, A. FUCHS, and G. S. PAWLEY. In preparation.

14. J. FARGES, M. F. DE FERAUDY, B. RAOULT, and G. TORCHET. J. Chem. Phys. **78**, 5067 (1983).

15. J. J. BURTON. J. Chem. Soc. Faraday Trans. 2, **69**, 540 (1973); M. R. HOARE and P. PAL. J. Cryst. Growth, **17**, 77 (1972).

16. B. W. VAN DE WAAL. J. Chem. Phys. **79**, 3948 (1983).

17. R. D. ETTERS, K. FLURCHICK, R. P. PAN, and V. CHANDRASEKHARAN. J. Chem. Phys. **75**, 929 (1981).

18. L. B. SPORNICK, R. L. DANILOWICZ, A. A. HELMY, and R. D. ETTERS. J. Chem. Phys. **84**, 2310 (1986).

19. F. H. STILLINGER and T. A. WEBER. Phys. Rev. A**25**, 978 (1982).

20. S. M. THOMPSON, K. E. GUBBINS, J. P. R. B. WALTON, R. A. R. CHANTRY, and J. S. ROWLINSON. J. Chem. Phys. **81**, 530 (1984).

21. F. H. STILLINGER and T. A. WEBER. J. Phys. Chem. **87**, 2833 (1983).

22. F. H. STILLINGER and A. RAHMAN. J. Chem. Phys. **60**, 1545 (1974).

23. D. BEEMAN. J. Comp. Phys. **20**, 130 (1976).

24. G. S. PAWLEY and G. W. THOMAS. J. Comp. Phys. **47**, 165 (1982).

25. D. E. WILLIAMS. J. Chem. Phys. **47**, 4680 (1967).

26. A. I. KITAIGORODSKII. J. Chim. Phys. **63**, 6 (1966).