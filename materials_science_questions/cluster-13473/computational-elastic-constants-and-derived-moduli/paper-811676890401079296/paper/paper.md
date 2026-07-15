# Crystal to Glass Transition and Melting in Two Dimensions

M. LI¹,², W. L. JOHNSON¹ AND W. A. GODDARD III²
¹W. M. Keck Laboratory, 138-78, California Institute of Technology, Pasadena, California 91125
²Molecular & Materials Simulation Center, Beckman Institute, 139-74, California Institute of Technology, Pasadena, California 91125

## ABSTRACT

Thermodynamic properties, structures, defects and their configurations of a two-dimensional Lennard-Jones (LJ) system are investigated close to crystal to glass transition (CGT) via molecular dynamics simulations. The CGT is achieved by saturating the LJ binary arrays below glass transition temperature with one type of the atoms which has different atomic size from that of the host atoms. It was found that for a given atomic size difference larger than a critical value, the CGT proceeds with increasing solute concentrations in three stages, each of which is characterized by distinct behaviors of translational and bond-orientational order correlation functions. An intermediate phase which has a quasi-long range orientational order but short range translational order has been found to exist prior to the formation of the amorphous phase. The destabilization of crystallinity is observed to be directly related to defects. We examine these results in the context of two dimensional (2D) melting theory. Finite size effects on these results, in particular on the intermediate phase formation, are discussed.

## INTRODUCTION

Both crystal to glass transition and melting are topological order to disorder transitions. The similarities of the starting and end phase and the disappearance of long range translational symmetries at the transitions suggest that they are the same [1]. In general the thermodynamics and in particular, the kinetics of these transitions resemble each other remarkably [1]. Although the mechanism of melting is still in debate [2], the theories and models developed for melting have been extensively used in the understanding of the CCT [1, 3-10]. However, these analogous criteria suffer from the same problem as they do in melting, namely that they are not able to provide a detailed microscopic picture of how these transitions proceed. In this paper, 2D LJ binary arrays under the polymorphic constraint are studied. By keeping the array at a sufficiently low temperature and thus eliminating chemical inhomogeneity, we expect to see certain intrinsic mechanisms of the CGT and to establish relationships between microscopic properties (such as atomic interactions and atomic size differences) with the thermodynamic and kinetic properties during the CGT.

The crystal to glass transitions can be obtained by a number of methods [1,11]. There are rarely cases where a pure system can be amorphized unless some extreme kinetic constraints are imposed. As in rapid quenching of melts, the majority of systems that can be amorphized usually contain several components. These multicomponent amorphizable systems invariably become metastable prior to the transition with much increased free energy. The composition-induced crystal to glass transition seems to be present in most of these systems and thus can be regarded as a general characteristic of solid state amorphization. Even mechanical deformation- and irradiation-induced amorphization can be regarded as composition-induced. The defects produced in these processes such as dislocations, antiphase and grain boundaries, antisite defects and interstitials directly contribute to the rise of free energy of the systems as well as the solute solubility. In particular, one can regard the chemical disordering such as the formation of antisite defects and interstitials in intermetallics caused either by irradiation or by mechanical deformation as a process producing metastable solid solutions. This motivated us to use solid solutions as

173
Mat. Res. Soc. Symp. Proc. Vol. 321. ©1994 Materials Research Society

a model system. In our early work in a binary LJ solid solution [6] characterized by two parameters, the solute concentration and solute-solvent atomic size difference, we found that a crystal saturated with solute atoms of sufficiently large atomic size mismatch can transform into a glass. Dramatic softening of elastic constants, especially shear elastic constants, prior to the CGT led us to believe that it is caused by mechanical instability. Furthermore, the molar volume and enthalpy of the crystalline and the amorphous phases at the transition differ only slightly. Compared with abrupt changes in both volume and enthalpy at thermal melting, the CGT seemed to be a much weaker transition. However, the finite system size, short simulation time and possible insufficient relaxation in the system made it difficult to draw a firm conclusion about the nature of the transition. In addition, three-dimensional microscopic configurations of the system could not be observed easily. In 2D arrays, however, we can minimize these problems by using larger systems and longer simulation times. The atomic configurations and defects and their evolution can also be visualized directly.

# CRYSTAL TO GLASS TRANSITIONS IN BINARY LJ ARRAYS

To simulate the CGT, we used a model system of binary arrays of atoms, A and B types, interacting with a Lennard-Jones potential. Arrays of solid solutions were generated by dispersing small solute atoms B on a hexagonal lattice occupied by solvent atoms A. Structural and thermodynamic properties were calculated using MD methods. Further computational details can be found in ref. 12 and 13. The most relevant parameters that can be varied are solute and solvent atomic size ratio, $\alpha = \mathrm{R_{BB}/R_{AA}}$, where $\mathrm{R_{AA}}$ and $\mathrm{R_{BB}}$ are A and B atomic radii, LJ potential well depths of three types of interactions, $\epsilon_{AA}, \epsilon_{AB}$ and $\epsilon_{BB}$, and solute concentrations, $X_B = \mathrm{N_B/N_{tot}}$, where $\mathrm{N_B}$ and $\mathrm{N_{tot}}$ are number of B atoms and the total number of atoms used in simulations. A large potential depth between solute and solute atoms can lead to a large negative heat of mixing and a large atomic size difference can cause large local lattice distortions and fast solute atom diffusion, both of which, for instance, have been found to be essential for solid state amorphization. In our simulations, however, the potential depths of all three types of interactions were set equal to minimize the possibility of cluster formation, phase separation or any other chemical inhomogeneity. So we are left with only two parameters, the atomic size ratio and solute composition.

Since the system is finite, possible wavelengths of fluctuations of composition, struc- ture, thermodynamic and defect properties, are restricted to this size. The finite size can affect the simulation results significantly, especially close to the CGT. The quality of the simulation results can also be affected by inadequate sampling of the system because of the randomness of the solute distributions in a finite sample. To make a finite system repre- sentative of that of an infinite system, several initial configurations with different random solute distributions were used. However, $\mathrm{N_{tot}} = 256$ atoms used in this simulation are still relatively small. A more detailed work which checks the finite size effects will be presented elsewhere [13]. In the remainder of this paper, we will present these preliminary simulation results close to the CGT in the binary arrays with $\alpha = 0.75$, temperature $T = 0.25$ (in reduced LJ units), which is slightly below the glass transition temperature, and pressure $P = 0.0$.

Structure evolution of the binary LJ solid solution can be observed through radial distribution functions (RDF) shown in Fig. 1. As the solute concentration increases, the peaks of RDF's become broadened but can still be well resolved. The double peaks corre- sponding to the second and third nearest neighbor positions remain distinguishable even when the amorphous phase forms at $X_B \geq 17.2\%$. To have a more quantitative mea- surement of atomic order and symmetry of the system, we calculated the the translational and bond-orientational order correlation functions [14]. The translational order correlation function is defined by $\rho_G(r) = < \rho_G(r)\rho_G(0) >$, where $\rho_G(r) = \exp(-i\vec{G} \cdot \vec{r})$ is the transla- tional order parameter with the shortest reciprocal lattice vector $G$ in a perfect hexagonal

lattice. The orientational order correlation function is defined by $\Psi(r)=<\psi(r)\psi(0)>$, where $\psi(r)$ is the orientational order parameter that measures the angular order of the nearest neighbor atom bonds with respect to a reference axis.

![](./images/811676890401079296_1.jpg)

Fig. 1 Solid line: total RDF; dotted line: partial RDF for AA atoms; dashed line: partial RDF for AB atoms; dot-dashed line: partial RDF for BB atoms

![](./images/811676890401079296_2.jpg)

Fig. 2 (a) Translational order correlation functions; (b) Bond-orientational order correla- tion functions. From top to bottom: $X_B = 0.10, 0.148, 0.172, 0.25$.

In 2D crystalline phases, the quasi-long range translational symmetry decays alge- braically, while the orientational correlation function remains a constant over a long range [14]. In liquid or amorphous phases, both correlation functions are short-range and decay exponentially over distance. More interesting is a possible intermediate phase, called the hexatic phase, existing between these ordered and disordered phases, which has quasi- long-range orientational order but short-range translational order. Nelson, Rubinstein and Spaepen [15] demonstrated the existence of such phase in an experiment using hard sphere binary arrays. We will show in this paper that such a phase could also exist in binary arrays with atoms interacting with soft LJ potentials.

Fig. 2 shows the calculated correlation functions at different solute concentrations in the binary arrays. It can be seen clearly that the correlation functions behave remarkably similarly to those predicted by the theory of two dimensional melting [14]. For $X_B < 0.148$, $\Psi(r)$ remains a constant while $\rho_G(r)$ decays only slightly at large distances; the translational correlation function decays fast to almost zero for $X_B \geq 0.148$ over the distance of the sample size, but the orientational correlation function shows a slight decay

in the same manner as $\rho_G(r)$ does at $X_B < 0.148$. Finally both of them exponentially decay to zero at roughly the third or fourth nearest neighbor distances when $X_B \geq 0.199$.

![](./images/811676890401079296_3.jpg)

Fig. 3 Atomic configurations of the LJ Binary arrays at (a) $X_B = 0.10$ (crystal); (b) $X_B = 0.172$ (Hexatic ?); (c) $X_B = 0.25$ (amorphous). •: A atom; o: B atom.

![](./images/811676890401079296_4.jpg)

Fig. 4 (a) Molar enthalpy; (b) density and (c) elastic constants.

We also plotted the atomic configurations from which these correlation functions were calculated. An edge dislocation is defined by an extra row of atoms in two dimensions. The translational order defined above will be interrupted across such a row of atoms defining a dislocation. At $X_B = 0.148$ the distance over which the translational correlation function tends to vanish is approximately the same as the mean distance between two dislocation aggregates. Fig. 3b shows the atomic configuration at $X_B = 0.172$ where translational order is absent beyond the third or fourth nearest neighbor, but the long-range orientational order is still present at large distances. The dislocations in this system become more dense and some well defined crystalline patches start showing different orientations. The amorphous structure shown in Fig. 3c corresponds to the binary arrays at $X_B = 0.25$ with both short-ranged $\rho_G(r)$ and $\Psi(r)$.

Fig. 4a and 4b show the changes of density and enthalpy during the CGT as $X_B$ increases. Interestingly no abrupt changes have been observed for the density at $X_B = 0.172$ where the long range translational order disappears and at the composition $X_B = 0.199$ where long range orientational order vanishes. The enthalpy has a slight jump $(< 2\%)$ when long-range translational order disappears at $X_B = 0.172$. In addition, we have not observed any hysteresis.

Fig. 4c shows the variations of the two independent elastic constants in the two dimensional binary arrays with $X_B$. The shear constants $\mu$ decreases and $\lambda$ increases at $X_B < 0.199$, leaving the bulk modulus almost a constant. $\mu$ decays sharply and reaches an extremely small value at $X_B \geq 0.148$. It goes to zero only if stress fluctuations in the system are large enough to spontaneously activate dislocations and drive them sliding

across the system. $\lambda$ starts decaying only after the system enters the amorphous region. As the binary array gets close to the CGT, it develops an elastic anisotropy. The relation $\mu = C_{44} = C' = (C_{11} - C_{12})/2$ in an isotropic media such as the hexagonal lattice is no longer obeyed, particularly in the region of "hexatic phase". This may be attributed to the preferred orientation of dislocations with the shortest Burgers vectors parallel to the closed packed atomic directions and thus breaking the isotropic symmetry. Finite size can also enhance this effect significantly. One presumably expects this effect to get smaller as the size gets larger [13].

## IS THE CGT MEDIATED BY DEFECTS UNBINDING?

A dislocation and a disclination in 2D can be defined conveniently by nearest neighbor numbers [16]. A disclination occurs when an atom has a number of nearest neighbors different from six, and usually two disclinations with typically 5 and 7 nearest neighbors bind together to form a dislocation. Thus dislocations and other more complicated defect configurations can be visualized by simply mapping the coordination numbers. Fig. 5 shows the defect configurations at the different stages of the CGT. The increasing number of dislocations are responsible for the destruction of long-range translational order at $X_B < 0.172$ (Fig. 5a), but further increase of dislocations will not significantly change the long-range orientational order. At $0.172 \leq X_B < 0.199$ (Fig. 5b) orientational order still persists over a long distance but translational order vanishes over not more than the fourth nearest neighbor distance.

![](./images/811676890401079296_5.jpg)

Fig. 5 Defect configurations of the LJ binary arrays at (a) $X_B = 0.148$ (crystal); (b) $X_B = 0.172$ (Hexatic ?); (c) $X_B = 0.25$ (amorphous). X denotes a disclination with 5 nearest neighbors; O a disclination with with 7 nearest neighbors.

Above results of the CGT suggest that its mechanism is different from the defect-unbinding theory of melting [14] in which dislocation-pairs need to unbind to single dislocations to destroy long-range translational symmetry at $T_m$ and these single dislocations need to unbind again at $T_2(\leq T_m)$ into disclinations to destroy long-range orientational symmetry. In the LJ binary arrays, the increasing number of dislocations and their clusters can be sufficient to disrupt long-range translational order. If dislocation density increases further to form "dislocation cell structure", then the long-range orientational order will be destroyed. The correlation length of the orientational correlation function defines the domain over which certain crystalline features are preserved (Fig. 5b). Boundaries with such large dislocation density are full of solute atoms. If the domain size is large enough, one expects to see the formation of a so called nanocrystalline phase [17]. If dislocation densities increase further and these boundaries start proliferating, an amorphous phase forms. Another convincing evidence against the defect unbinding mechanism for the CGT is provided by the dislocation coupling constant, or Kosterlitz-Thouless constant K, which, at $X_B = 0.172$, is still much larger than the value $16\pi$ as predicted if dislocation unbinding presumably occurs [14]. However, we do not rule out the possibility of the defect unbinding mechanism in certain systems in which a fairly large repulsive interaction between solute atoms may raise the barriers of dislocation clustering and thus forces them to unbind [13].

## SUMMARY

We summarize some general features of the CGT in 2D from our simulation results. First, like its 3D counterpart, the 2D binary arrays undergo the CGT for sufficiently large atomic size differences with increasing solute concentrations. This is in agreement with experimental observations in both liquid to glass transitions and solid state amorphizations where atomic size difference was found to be necessary (but not sufficient) in determining the glass-forming ability [1, 18]. We also found that it is more difficult to make a glass in 2D than in 3D. Second, decreasing of the crystallinity of the binary arrays as more and more solute atoms are saturated is directly caused by defects created around them. At low temperatures, thermal vibrations and resulted anharmonicities are relatively small. So density as well as configurations of these defects, most of which are dislocations, play a dominant role in destabilizing the crystalline order and inducing the CGT. Third, the CGT proceeds in three stages at each of which an unique microstructure exists. An intermediate phase consisting of ensembles of crystalline-like clusters was found to exist prior to the formation of the amorphous phase. This phase is characterized by a quite long range orientational order but short-range translational order. However, finite sample sizes used in our simulation can also lead to similar results. This topic is currently under investigation [13].

## ACKOWNLEDGEMENT

The financial support of this work is provided by grants from the DOE under contract No. DEFG038GER45242 and NSF under contract No. DMR-8811795 and CHE-91-100284.

## REFERENCES:

1. W. L. Johnson, Prog. Mater. Sci., 30, 81, (1986); R. W. Cahn and W. L. Johnson, J. Mater. Sci., 1, 724, (1986).
2. K. J. Strandburg, Rev. Mod. Phys., 60, 161, (1988); F.F. Abraham, Phys. Rept., 80, 339, (1981).
3. D. Wolf, P. R. Okamoto, S. Yip, et al., J. Mater. Res., 5, 286, (1990); P. R. Okmoto, and M. Meshii, *Science of Advanced Materials*, edited by H. Wiedersich and M. Meshii (ASM International, Materials Park, OH, 1990), pp. 33.
4. M. Born, J. Chem. Phys., 7, 591, (1939).
5. J. L. Tallon and W. H. Robinson, Phil. Mag. A, 36, 741, (1977); J. L. Tallon, Phil. Mag. A., 39, 151, (1979).
6. M. Li and W. L. Johnson, Phys. Rev. Lett., 70, 1120, (1993); W. L. Johnson, M. Li and C. E. Krill, J. Non-crystal. Sol., 156, 481, (1993).
7. C. E. Krill, J. Li, C. Ettl, K. Samwer and W. B. Yellon, J. Non-cryst. Sol., 156, 506, (1993).
8. J. Koike, Phys. Rev. B, 47, 7700, (1993).
9. R. Devanathan, N. Q. Lam, P. R. Okamoto and M. Meshii, MRS Symposia Pro- ceeding No. 291. pp. 653 (MRS, Pittsburgh, 1992).
10. H. Fecht and W. L. Johnson, Nature, 334, 50, (1988).
11. D. E. Luzzi (ed.), J. Alloys and Compounds, 194, (1993)
12. M. Li and W. L. Johnson, Phys. Rev. B, 46, 5237, (1992).
13. M. Li, W. L. Johnson and W. A. Goddard, unpublished results.
14. D. R. Nelson and B. I. Halperin, Phys. Rev. B, 19, 2457, (1979).
15. D. R. Nelson, M. Rubinstein and F. Spaepen, Phil. Mag. A, 46, 105, (1982).
16. M. P. Allen, D. Frekel and W. Gignac, J. Chem. Phys., 78, 4206, (1983).
17. W. L. Johnson, unpublished results.
18. T. Egami and Y. Waseda, J. Non-Cryst. Sol., 64, 113, (1984);B. C. Giesson, *Proc. 4th Int. Conf. on Rapidly Quenched Metals*, edited by T. Masumoto and K. Suzuki, (Japan Institute of Metals, Sendai, 1982), Vol. 1, pp. 213.

178