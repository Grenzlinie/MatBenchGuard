STRUCTURE, PHASE TRANSFORMATIONS,
AND DIFFUSION

# Effect of Chemical Interaction on the Stability
of Metal Clusters in FCC Metals

I. N. Kar'kin, L. E. Kar'kina, and Yu. N. Gornostyrev

Institute of Metals Physics, Ural Division, Russian Academy of Sciences, ul. S. Kovalevskoi 18, Ekaterinburg, 620041 Russia
Received August 3, 2007

Abstract—Structural stability of small Ni, Al, and Au metal clusters with a number of atoms close to $N = 55$ and 147 has been studied by the method of molecular dynamics with the use of realistic potentials of interatomic interaction. It has been shown that in Ni, in which the icosahedral configuration is most stable, the mass spectrum predominantly contains peaks, which correspond to $N = 55$ and 147. At the same time, for Au and Al clusters, the consequence of magic numbers differs from that specified by the close packing of atoms, and its realization depends on experimental conditions. The results obtained allow concluding that the position of peaks in the mass spectrometric experiments with small clusters is determined by morphological features of the structural state, which depend on the character of interatomic interaction.

PACS numbers: 71.15.Pd, 61.46.+w
DOI: 10.1134/S0031918X08090056

## 1. INTRODUCTION

Lately, the physics of condensed matter pays a great attention to the study of objects consisting of structural elements of a nanosized scale (nanocrystals, fine films, powders, nanoparticles, microclusters). A large variety of cluster forms has a practical application in catalysis [1], sensing technology [2], production of new materials by cluster deposition onto a substrate [3], or growing microcrystals on a cluster basis [4].

For the first time, specific structural peculiarities of small clusters were revealed in the mass-spectrometric analysis of a beam of particles of alkali metals and noble gases which were deposited onto a cold substrate [5]. The fact of detecting peaks in the mass spectrum has aroused interest to the problem of existence of clusters with particular magnitudes of the number of atoms $N$ (magic numbers). These preferred numbers should be closely related to the mechanisms of formation and growth of microclusters and the conditions of existence of the most stable cluster isomers. In particular, the sequence of magic numbers in the mass spectrum of Na particles was explained by an electron-structure-related origin (the formation of closed delocalized electron shells [5]). According to another widespread point of view the structure of clusters is determined by a tendency to achieving the closest atomic packing with axes of 5-fold symmetry [6–11]. In this case, the most stable clusters are those with $N = 55$, $147…$ (sequence of Mackay icosahedra), in which a perfect icosahedral order is formed. The authors of [12] investigated the problem of the stability of a structural state depending on the number of atoms in a cluster within the framework of the kinetic approach, which considers the competition of processes of deposition and evaporation of atoms from the surface. The sequence of magic numbers, which was found in [12] on the basis of the results obtained with the use of a Lennard-Jones potential, is in good agreement with the peaks observed in the mass spectrum of noble gases.

The results found in [6–12] were obtained for systems in which the interaction between ions has a pairwise central character. At the same time, in real metals, where unpaired contributions to the interaction energy play a substantial part, the energy minimum can be achieved for more complex morphological types of clusters (e.g., polytetrahedral, amorphous), whose structure does not answer the principles of closest packing [13]. As a result, the sequence of numbers that is observed in the mass spectrum of metallic clusters is determined not only by the geometrical factors (atomic packing) but also by the character of chemical bond. In addition, as was shown in [13], the ratio of energies of different cluster configurations depends on temperature, which also affects the results of mass spectroscopy.

In this work, we report the results of a study of the structural stability of Ni, Al, and Au clusters depending on temperature near the “magic” numbers $N = 55$ and 147 by the method of molecular dynamics. The results of a simulation with realistic potentials of interatomic interaction demonstrate the determining role of interatomic interaction in the realization of energetic preference of clusters and their structural stability.

![](./images/811900585933537280_1.jpg)

Fig. 1. Calorimetric curves obtained upon cooling for (a) Ni, (b) Al, and (c) Au clusters with the number of atoms $N$ from 50 to 60 and from 142 to 152.

![](./images/811900585933537280_2.jpg)

Fig. 2. Structure of (a, b) Ni₅₁ clusters upon relaxation with the difference in time Δτ ~ 30 ps, T = 820 K and the structure of the ground states of (c) Au₆₀ and (d) Al₅₀ clusters.

## 2. STRUCTURE OF Ni, Al, AND Au CLUSTERS DEPENDING ON TEMPERATURE

The simulation of Ni, Al, and Au clusters was performed based on multiparticle potential of interatomic interaction using the embedded-atom method [14, 15]. Studies were carried out for clusters with a number of atoms in the ranges from 50 to 60 and from 142 to 152. In the initial configuration, the atoms populated coordination shells near some fixed atom in accordance with positions of the fcc lattice. Heating and subsequent cooling of clusters were carried gradually in steps of 20 K, the exposure time at a given temperature was ~2 × 10⁵ steps of MD or 200 ps (a duration of the MD step was 10⁻¹⁵ s). As was demonstrated earlier [13], this rate of the interparticle change allows realizing a quasi-equilibrium state of clusters at N <200.

Figure 1 shows the variation of the potential energy Eₚ per one atom during cooling of fcc-metal clusters preliminarily heated to temperatures above the melting temperature Tₘ. The Ni clusters with magic numbers N = 55 and N = 147 are energetically preferable within the chosen ranges of N (Fig. 1a); in this case, the structure of the ground state which is achieved during cooling corresponds to the Mackay icosahedron. At the same time, for Au and Al the icosahedral configuration at N = 55 and 147 is not energetically advantageous, and the minimum of Eₚ is achieved at the boundaries of the N interval (Figs. 1b and 1c). After cooling, in Au clusters there is formed an amorphous-like structure containing elementary 13-atom icosahedral fragments, whose energy is lower than that for the icosahedral configuration [13]. During cooling of Al₅₀–Al₆₀ clusters, there takes place an ordering of icosahedral fragments with the formation of a polytetrahedral configuration of the Frank–Casper type [13] (Fig. 2d); only at N = 60, there is formed a highly distorted icosahedral structure (Fig. 2c). For the Al₁₄₂–Al₁₅₂ clusters, the polytetrahedral structure was obtained at N ≥ 147; for smaller clusters there was realized an amorphous-like structure with several chaotically located icosahedral fragments.

The monotonous decrease in the Eₚ energy with decreasing temperature is mainly caused by a reduction of the average spacing between atoms in a cluster. A sharp decrease in Eₚ(T) in a narrow temperature range indicates the occurrence of crystallization processes, which can also be confirmed by a change in the root-mean-square displacement of atoms [13]. These processes manifest themselves most clearly in Ni and Au clusters with numbers of atoms N from 142 to 152. In Ni₅₃–Ni₅₇ clusters, the recrystallization temperature is also well pronounced, but with decreasing deviation of N from the “magic” value the crystallization proceeds gradually in a wide temperature range and is accompanied by a dynamic coexistence of different structural states (Fig. 2a, 2b).

In Al clusters, the transition from the liquid to solid state proceeds gradually. The slope of the Eₚ(T) curves slowly changes in a wide temperature range, and a jumplike change in the potential energy testifies to the fact that the transition occurs via a number of intermediate configurations. Therefore, both the process of vitrification (crystallization during transition into an amorphous state) of Au clusters and the formation of an icosahedral configuration in Ni clusters are accompanied by a descent in the Eₚ(T) curve; i.e., they manifest features of a first-order phase transition. At the same time, the formation of a polytetrahedral state in Al clusters upon cooling develops continuously.

Figure 3 shows the dependence of the energy Eₚ of the ground state of clusters on the number of atoms for the two intervals under investigation, N = 50–60 and 142–152. For the Ni clusters there is observed a well pronounced local energy minimum upon N magnitudes that correspond to “magic” numbers 55 and 147 (Figs. 3a and 3d). In the case of Au, the energy preference of clusters with a certain N magnitude is much weaker (Figs. 3b and 3e), and the positions of the local minima do not correspond to the magic numbers. For the Al clusters, the energy of the ground state decreases gradually with a growth of the number of particles in the cluster in accordance with the relationship $E(N) = E0 - AN^{-1/3}$ (Figs. 3c and 3f), which reflects a decrease in the fraction of surface cluster atoms with an increase of its size. Thus, in the case of Al clusters, the energetically preferred structural states do not exist.

The above results vividly demonstrate the interrelation between the morphological features of the struc-

![](./images/811900585933537280_3.jpg)

Fig. 3. Dependence of energy of the ground state on the number of atoms for (a) $Ni_{50}-Ni_{60}$, (b) $Au_{50}-Au_{60}$, (c) $Al_{50}-Al_{60}$,
(d) $Ni_{142}-Ni_{152}$, (e) $Au_{142}-Au_{152}$, and (f) $Al_{142}-Al_{152}$ clusters. Dashed line corresponds to the approximation $E(N)=E0-AN^{-1/3}$.

tural state and the stability of metallic clusters. In par-
ticular, for amorphous or polytetrahedral clusters the
states with magic numbers $N$ stop being energetically
preferable. As was discussed in [13], whether there
arises an amorphous or polytetrahedral structure of
clusters is mainly determined by the contribution of
unpairwise interatomic interactions in Au and Al. At the
same time, an icosahedral structure is realized in Ni
clusters, in which the interatomic interaction is close to
the central pairwise interaction.

### 3. DISCUSSION OF RESULTS:
EFFECT OF INTERATOMIC INTERACTION
ON THE STRUCTURE STABILITY

The results of simulation of Ni, Al, and Au clusters
demonstrate that the most substantial influence on the
type of a cluster configuration and, hence, on the energy
preference of clusters with the magic numbers of atoms
comes from the specific features of chemical interac-
tion. In the case of Ni, where the interaction is close to
the central pairwise type (see [13]), the icosahedral
structure is particularly stable; it is retained upon heat-
ing up to the melting temperature and is recovered upon
cooling from a temperature $T>T_{m}$; a regular icosahe-
dron with completely populated shells ($N=55,147$)
answers the local energy minimum (Fig. 3). During
cooling of $Ni_{142-152}$ clusters, the crystallization process
proceeds similarly to a first-order phase transition,
which testifies to the structure specificity of the icosa-
hedral state (the extension of the range of phase transi-
tion upon deviations from $N=55$ is probably due to the
lability of small clusters (Figs. 2a and 2b)).

In Au clusters, there is formed an amorphous-like
structure and the position of local energy minima does
not correspond to the magic numbers. For polytetrahe-
dral Al clusters, local minima on the $E_{p}(N)$ dependence
are absent. Let us consider how such features will man-
ifest themselves in the mass spectrometry of metal clus-
ters. Solov’yev et al. [12] proposed a model that
explains the preference of certain cluster sizes in the
mass spectrum as a result of competition of processes
of deposition and evaporation of atoms from the sur-
face. A change in the number of atoms $\Delta n_{N}$ of a given

![](./images/811900585933537280_4.jpg)

Fig. 4. Dependence of $\Delta_N^{(2)}$ on the number of particles in the intervals (a) $N = 50$–60 and (b) $N = 142$–152.

size $N$ in the ensemble of clusters, $\Delta n_N = n_{N+1}\exp(-\Delta_N^{(1)}/kT)[1 - \exp(-\Delta_N^{(2)}/kT)]$, depends exponentially on the difference between the energies of clusters in which the number of atoms differs by unity, i.e. $\Delta_N^{(1)} = E_N - E_{N+1}$, $\Delta_N^{(2)} = E_{N-1} - 2E_N + E_{N+1}$. The most substantial effect on the preference of a cluster configuration of size $N$ comes from the multiplier in square brackets, whose magnitude is determined by the energy factor $\Delta_N^{(2)}$ (the second derivative of energy with respect to the number of particles).

Figure 4 shows the dependence of the energy factor $\Delta_N^{(2)}$ on the number of particles in a cluster. At $N = 55$, $\Delta_N^{(2)} > 0$ for all the metals studied, and the magnitude of the energy factor is substantially higher for Ni in comparison with Al and Au (Fig. 4a), which indicates an enhanced stability of the $Ni_{55}$ cluster. For the clusters of other sizes, the parameter $\Delta_N^{(2)}$ does not exceed ~0.1 eV and in some cases it is close to zero or has negative magnitudes. Thus, we can expect the presence of $Ni_{52}$, $Al_{52}$, $Au_{52}$, $Au_{57}$, and $Ni_{58}$ clusters in the mass spectrum if the temperature of the particles deposited does not exceed 1000 K, while $Ni_{55}$ clusters are being formed upon cooling from the melting temperature.

For the clusters with $N$ close to 147, high positive values of the energy factor $\Delta_N^{(2)}$ were observed for $Ni_{147}$, $Al_{145}$, $Al_{148}$, $Al_{150}$, $Au_{144}$, $Au_{146}$, and $Au_{148}$ clusters (Fig. 4b). In this range of $N$, the existence of clusters with a "magic" number of atoms is expected only for Ni, while Al and Au have different $N$ values.

![](./images/811900585933537280_5.jpg)

Fig. 5. Temperature dependence of $\Delta_N^{(2)}$ for (a) $Ni_{55}$, $Al_{55}$, and $Au_{55}$ and (b) $Ni_{147}$, $Al_{145}$, and $Au_{144}$ clusters.

Figure 5 demonstrates the temperature dependence of the parameter $\Delta_N^{(2)}$ for those clusters, in which the most stable ground state was obtained at $T = 0$ K. As is seen, the magnitude of the parameter $\Delta_N^{(2)}$ of $Ni_{55}$ and $Ni_{147}$ does not virtually change up to the melting temperature $T_m$, which testifies to the high stability of Ni clusters with the filled icosahedron shells. All the other cluster configurations appear to be stable only at tem-

peratures below $0.6T_{\mathrm{m}}$. At $T > 0.6T_{\mathrm{m}}$, $\Delta_{N}^{(2)}$ decreases rapidly and changes its sign; hence, upon high temperatures there exists no preferable cluster configurations aside from $\mathrm{Ni}_{55}$ and $\mathrm{Ni}_{147}$.

Therefore, the appearance of peaks in the mass spectrum for Au and Al is to a considerable degree determined by kinetic factors, such as the ratio between the cooling rate and the rate of redistribution of atoms between various cluster configurations. In particular, if the atoms in the beam used for deposition exist at temperatures $T < 0.7T_{\mathrm{m}}$ during a sufficiently long period of time, we can expect the appearance of peaks in the mass spectrum at $N = 145$, 148, and 150 for Al and at $N =$ 144, 146, and 148 for Au. Otherwise, no preferred cluster states would exist.

## CONCLUSIONS

The problem of the conditions for the existence of most stable cluster isomers is closely related to their formation and growth mechanisms, and pertains directly to the sequence of "magic" numbers, which is observed experimentally in the mass spectrum of the deposited particles. To solve this problem, we have studied the stability of the structural state of Ni, Al, and Au metallic clusters with the numbers of atoms $N$ close to the "magic" numbers $N = 55$ and 147 depending on the temperature, using the molecular-dynamics method. It has been shown that in metals in which the character of the atomic interaction is close to the central pairwise interaction (as in Ni), the icosahedral configuration is most stable, and the mass spectrum contains predominant peaks corresponding to $N = 55$ and 147. An increase in the fraction of unpairwise contributions to the energy of interatomic interaction leads to the prevalence of other morphological cluster types (e.g., an amorphous or polytetrahedral type). As a result, the sequence of magic numbers for Au and Al clusters differs from that prescribed by considerations of close packing ($N = 55, 147\ldots$), and its realization depends on the regime of cooling of the beam used for deposition.

## REFERENCES

1. Y. Ding, M. Chen, and J. Erlebacher, "Metallic Mesoporous Nanocomposites for Electrocatalysis," J. Am. Chem. Soc. **126** (22), 6876–6877 (2004).

2. Hieda R. G. Mitsunori, M. Dixon, T. Daniel, et al., "Ultrasensitive Quartz Crystal Microbalance with Porous Gold Electrodes," Appl. Phys. Lett. **84**, 628 (2004).

3. P. Jensen, "Growth of Nanostructures by Cluster Deposition: Experiments and Simple Models," Rev. Mod. Phys. **71** (5), 1695–1737 (1999).

4. A. A. Vikarchuk and A. P. Volenko, "Pentagonal Copper Crystals: Various Growth Shapes and Specific Features of Their Internal Structure," Fiz. Tverd. Tela **47** (2), 339–344 (2005) [Phys. Solid State **47** (2), 352–356 (2005)].

5. S. Sugano and H. Koizumi, *Microcluster Physics* (Springer, Berlin, 1998), pp. 236–370.

6. D. J. Wales and J. P. K. Doye, "Global Optimization by Basin-Hopping and the Lowest Energy Structures of Lennard-Jones Clusters Containing up to 110 Atoms," J. Chem A **101**, 5111–5116 (1997) (arXiv:cond-mat/9803344).

7. J. P. K. Doye and D. J. Wales, "Structural Consequences of the Range of the Interatomic Potential: A Menagerie of Clusters," J. Chem. Soc, Far. Trans. **93**, 4233 (1997) (arXiv:cond-mat/9709201).

8. Cambridge Cluster Database at http://brian.ch.cam.ac.uk

9. J. P. K. Doye and D. J. Wales, "Global Minima for Transition Metal Clusters Described by Sutton–Chen Potentials," New J. Chem. **22**, 733–744 91998) (arXiv:cond-mat/9711038).

10. J. M. Soler, M. R. Beltran, K. Michaelian, et al., "Metallic Bonding and Cluster Structure," Phys. Rev. **61**, 5771–5780.

11. S. C. Hendy and B. D. Hall, "Molecular Dynamics Simulations of Lead Clusters," Phys. Rev B: Condens. Matter **64**, 085425 (2001) (arXiv:cond-mat/0012167).

12. I. A. Solov'yev, A. V. Solov'yev, and W. Greiner, "Cluster Growing Process and Sequence of Magic Numbers," Phys. Rev. Lett. **90**, 053401.

13. Yu. N. Gornostyrev, I. N. Kar'kin, M. I. Katsnel'son, and A. V. Trefilov, "Evolution of the Atomic Structure of Metal Clusters upon Heating and Cooling: Computer Simulation of FCC Metals," Fiz. Met. Metalloved. **96** (2), 19–29 (2003) [Phys. Met. Metallogr. **96** (2), 135–144 (2003)].

14. A. F. Volter and S. P. Chen, "Accurate Interatomic Potentials for Ni, Al, and $\mathrm{Ni}_{3}\mathrm{Al}$," Mater. Res. Soc. Symp. Proc. **82**, 175 (1987).

15. F. Ercolessi and J. B. Adams, "Interatomic Potentials from First-Principles Calculations: The Force-Matching Method," Europhys. Lett. **26** (8), 583–588 (1994).