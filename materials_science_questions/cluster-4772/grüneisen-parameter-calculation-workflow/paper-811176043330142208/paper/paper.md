# Anomalous thermal conductivity and suppression of negative thermal expansion in $ScF_3$

Ambroise van Roekeghem, $^{*}$ Jesús Carrete, and Natalio Mingo

CEA, LITEN, 17 Rue des Martyrs, 38054 Grenoble, France

(Received 5 January 2016; revised manuscript received 13 June 2016; published 25 July 2016)

The empty perovskite $ScF_3$ exhibits negative thermal expansion up to 1100 K. We demonstrate that *ab initio* calculations of temperature-dependent effective phonon spectra allow us to quantitatively describe the behavior of this compound and the suppression of negative thermal expansion. Based on this result, we predict an anomalous temperature dependence of the thermal conductivity and interpret it as a general feature of the perovskite class. Finally, we comment on the fact that the suppression of negative thermal expansion at such a high temperature is beyond the reach of the quasiharmonic approximation and we discuss this suppression based on the temperature dependence of the mode Grüneisen parameters.

DOI: 10.1103/PhysRevB.94.020303

Negative thermal expansion (NTE), caused by anharmonicity in solids, is crucial for technological applications to obtain materials with no volume variation over given temperature ranges [1]. Being able to find new materials exhibiting this behavior from *ab initio* calculations is thus an important issue. Recently, attention has been drawn to fluorides and empty perovskites, following the discovery of $ScF_3$, which exhibits NTE up to 1100 K [2]. Few attempts to understand and reproduce this behavior from realistic calculations have been performed so far. Within the quasiharmonic approximation, contradictory results have been obtained by different groups: While Li and collaborators found a persistent NTE at high temperature [3], Liu and collaborators found the suppression of NTE around 400 K [4]. In both cases, the calculated lattice parameters were different from the experimental measurements by about 1% [5], whereas the maximum experimental variations of the lattice parameters due to the thermal expansion are about 0.5% [2]. Moreover, the value of the coefficient of thermal expansion (CTE) at low temperature was also too small by at least a factor of two. Li and collaborators pointed out that the structural quarticity of the transverse vibrations of the fluorine atoms improves the behavior of the calculated NTE coefficient with respect to experiment, with the NTE being stronger at low temperature and weaker at high temperature as compared to the quasiharmonic approximation. Still, they could not perform a quantitative calculation over the whole Brillouin zone and their approximation to the effect of quartic anharmonicity failed to show the suppression of NTE at high temperature [3]. In contrast, calculations using density-functional molecular dynamics, which take into account anharmonicity, reproduce the suppression of NTE [6]. Besides these difficulties, other clues highlight the importance of anharmonicity in this material and in the class of perovskites in general. In particular, several measurements of the thermal conductivity in various perovskites describe an anomalous temperature dependence and point out the role of the soft modes in those compounds [7–14]. So far, there is no calculation or measurement of the thermal conductivity of $ScF_3$ available in the literature.

In this Rapid Communication, we use *ab initio* calculations of temperature-dependent effective phonon dispersions and scattering rates to investigate the effects of anharmonicity in $ScF_3$. We compute the temperature-dependent interatomic force constants using regression analysis of forces from density functional theory coupled with a harmonic model of the quantum canonical ensemble, to obtain the evolution of the lattice parameter and of the phonon spectrum with quantitative agreement with experimental data up to 1000 K. We then calculate the thermal conductivity and predict an anomalous temperature dependence similar to what has been measured in other perovskites, which is caused by anharmonicity. Finally, we show that the suppression of negative thermal expansion at high temperature is beyond the reach of the quasiharmonic approximation, and we discuss this phenomenon in terms of the mode Grüneisen parameters.

Several methods have been recently developed to deal with anharmonic effects at finite temperature in solids. The self-consistent *ab initio* lattice-dynamical method (SCAILD) [15] establishes a self-consistency loop on the phonon frequencies in the high-temperature limit by computing forces created by displacements with an amplitude fixed by the classical mean-square displacement. The temperature-dependent effective potential approach (TDEP) [16,17] is based on *ab initio* molecular dynamics (AIMD) and relies on fitting the computed forces from the AIMD trajectory to a model Hamiltonian, which can include second- or higher-order terms. In the stochastic self-consistent harmonic approximation (SSCHA) [18], the free energy of an ensemble of harmonic oscillators in the real potential is minimized with respect to the second-order force constants and to the structure of the compound. Finally, an approach [19] based on the self-consistent phonon theory (SCPH) [20] estimates the anharmonic self-energy using third- and fourth-order force constants extracted by compressive sensing techniques from density-functional-theory (DFT) calculations [21]. In our case, we use an approach inspired by the SCAILD method but using the full quantum mean square thermal displacement matrix as in the SSCHA and allowing the possibility for updating the eigenvectors and obtaining higher-order force constants by fitting the forces in real space, as in TDEP. In the harmonic approximation, the probability of finding the system in a configuration in which each ion $i$ is displaced in direction $\alpha$ by $u_{i\alpha}$

$^{*}$ambroise.van-roekeghem@polytechnique.edu


is $\rho_{h}(\{u_{i\alpha}\}) \propto \exp(-\frac{1}{2}u^{T}\Sigma^{-1}u)$, with $\Sigma(i\alpha,j\beta)$ being the quantum covariance for atoms $i,j$ and directions $\alpha,\beta$:

$$
\Sigma(i\alpha,j\beta)=\frac{\hbar}{2\sqrt{M_{i}M_{j}}}\sum_{m}\omega_{m}^{-1}[1 + 2n_{B}(\omega_{m})]\epsilon_{mia}\epsilon_{mj\beta}^{*}
$$

where $M$ is the atomic mass, $\omega_{m}$ is the phonon frequency of mode $m$ (comprising both wave-vector and branch degrees of freedom), $\epsilon_{m}$ is the corresponding wave function, and $n_{B}$ is the Bose-Einstein distribution. From the phonon frequencies and eigenvectors of the starting phonon spectrum, we compute the matrix $\Sigma$ using the $\Gamma$ point of a $4\times4\times4$ supercell and use it as the covariance matrix of a multidimensional Gaussian distribution to generate $N$ random sets of atomic displacements $\{u_{i\alpha}^{n}\}$, with $i$ indexing each atom and direction in the supercell and $n$ being a given random configuration. The forces $\mathbf{f}_{i}^{n}$ acting on each atom of the supercell generated by this set of displacements $\{u_{i\alpha}^{n}\}$ are calculated by density functional theory. Finally, we use those forces and displacements to fit the second- and third-order force constants [22] of a model potential, using least-squares minimization. These force constants allow us to calculate a new phonon spectrum. In practice, we start from the spectrum calculated using small displacements and we iterate the procedure described above until convergence. In addition, for each cycle we calculate the external pressure $P = -\left(\frac{\partial E_{p}}{\partial V}\right)_{S}-\left(\frac{\partial E_{k}}{\partial V}\right)_{S}$. The derivative of the potential energy $E_{p}$ is computed using the mean of the external pressure $P^{DFT}$ obtained by density functional theory: $-\left(\frac{\partial E_{p}}{\partial V}\right)_{S}=\frac{1}{N}\sum_{n<N}P^{DFT}(\{u_{i\alpha}^{n}\})$, thus taking into account the anharmonicity of the potential. For the derivative of the kinetic energy $E_{k}$, we use the quasiharmonic expression $\left(\frac{\partial E_{k}}{\partial V}\right)_{S}=-\frac{1}{2V}\sum_{m}\hbar\omega_{m}\gamma_{m}[\frac{1}{2}+n_{B}(\omega_{m})]$, with $\gamma_{m}$ being the Grüneisen parameter of mode $\omega_{m}$ [23]. We then update the lattice parameter until the mean external pressure becomes negligible. This allows us to calculate the thermal expansion of the material, including even-order anharmonic effects within the effective second-order force constants, as shown for instance in Refs. [24,25].

Figure 1 shows the phonon spectra and densities of states obtained at 8, 300, 900, and 1500 K compared to the IXS measurements of the phonon frequencies at 8 and 300 K from Ref. [26]. We observe that the effects of temperature are antagonistic depending on the frequency range: Lower frequency modes harden with increasing temperature, while higher frequency modes soften, with a boundary between those two regimes at around 10 THz. This is in qualitative agreement with the neutron-weighted data of Ref. [3], except for the peaks around 3 and 12 THz, which were seen to have the opposite behavior. Since both the phonon dispersions and the IXS data indeed point toward a hardening of the lower frequencies, the disagreement with the neutron-weighted density of states likely comes from the phonon-neutron matrix elements.

![](./images/811176043330142208_1.jpg)

FIG. 1. Temperature-dependent phonon dispersion (left and bottom) compared to the inelastic x-ray scattering (IXS) measurements of Ref. [26] at 8 K (black crosses) and 300 K (black dots), and corresponding density of states (right).

Figure 2 shows the calculated lattice parameter compared to the experimental measurements of Greve and collaborators [2]. We use the PBEsol functional, which has been conceived to give more reliable results for the crystal structure of solids as compared to the local density approximation (LDA) or the generalized gradient approximation (GGA) [27], and we average the value of the lattice parameter over 30 cycles. We also take into account electronic excitations in the thermal expansion by using Fermi-Dirac statistics to determine the partial occupancies. Indeed, electronic excitations have been shown to have a non-negligible impact on the free energy, phonon dispersion, and CTE in aluminium and rhodium, in particular near the melting temperature [28,29]. We obtain

![](./images/811176043330142208_2.jpg)

FIG. 2. Temperature dependence of the lattice parameter of $ScF_{3}$ using the PBEsol exchange-correlation potential, compared to the experimental data of Ref. [2].


![](./images/811176043330142208_3.jpg)

FIG. 3. Phonon lifetimes on a $15 \times 15 \times 15$ grid as a function of energy at 900 K using force constants from different temperatures (left) and thermal conductivity interpolated between calculations with fixed second- and third-order force constants corresponding to different temperatures (right).

quantitative agreement up to 1500 K, with a deviation of the lattice parameter of less than $1\%$.

We now compute the thermal conductivity of $ScF_3$, which has neither been measured nor previously calculated, up to our knowledge. We use the full solution of the Boltzmann transport equation as implemented in the SHENGBTE code [30] and compute values from 300 to 1500 K using the temperature-dependent effective second- and third-order force constants. Figure 3 displays the lifetimes calculated at 900 K while artificially using force constants obtained for different temperatures and the thermal conductivity. When temperature increases, two important phenomena occur simultaneously: The lifetimes of the soft modes become longer due to the modification of their frequencies but also all lifetimes are enhanced globally. Indeed, close to a displacive instability the three-phonon scattering rate of the soft mode becomes particularly high because it is proportional to $\omega^{-1}$, as seen for instance in $SrTiO_3$ [31]. The global enhancement of lifetimes is mainly due to the reduction of the available phase space for three-phonon processes [32,33], which in turn is due to the shrinking in energy of the phonon density of states by the simultaneous softening of high-energy modes and hardening of low-energy modes. As a result, the thermal conductivity acquires an anomalous temperature dependence that we can roughly describe by a power law close to $\kappa \propto T^{-0.6}$ (see Fig. 3). This behavior is reminiscent of what has been found in other perovskites, such as the prototype compound $SrTiO_3$ [11,12], in which the thermal conductivity has been shown to follow a power law $\kappa \propto T^{-\alpha}$ with $\alpha \approx 0.6$-$0.7$. We speculate that the presence of soft modes in many perovskites—which are very sensitive to temperature—makes such anomalous dependence a common behavior in this class.

To better understand the suppression of NTE in $ScF_3$, let us begin by summarizing the problem in simple arguments. Within the quasiharmonic approximation, the sign of the CTE $\alpha_V$ follows the weighted Grüneisen parameter $\gamma$ via $\alpha_V = \frac{\gamma C_v \rho}{K_T}$, with $K_T$ being the isothermal bulk modulus, $C_v$ being the isochoric heat capacity, and $\rho$ being the density [34,35]. In this material, all phonon modes have energies lower than 1000 K, which means that the heat capacity and weighted Grüneisen parameter have negligible thermal variation above this temperature. Moreover, the volume of the unit cell at 1300 and 900 K is approximately the same, excluding the possibility that the potential volume variation of the Grüneisen parameter could explain by itself the change of expansion regime. It is thus very unlikely that the suppression of NTE around 1100 K can be explained within the quasiharmonic approximation. This is in contrast to the other famous compound exhibiting NTE over a large temperature range, $ZrW_2O_8$, in which NTE persists until its decomposition [36], and to many compounds which exhibit NTE over a small temperature range before its suppression due to the thermal population of higher-energy phonon modes, such as the prototype material of the empty perovskite family $ReO_3$ [37,38] or, more prosaically, silicon [39]. Thus, $ScF_3$ presents an explicit case where high-order anharmonicity plays a crucial role. In passing, we note that even in those compounds with apparently simpler behavior there remain important related questions, such as the possible role of quartic anharmonicity in the temperature dependence of the phonon spectrum of $ZrW_2O_8$ [40] or the reappearance of NTE in $ReO_3$ around 650 K [41], which could not be explained within the Grüneisen formalism [37,42] and was tentatively attributed to the strong anharmonic behavior of a soft mode [41,43].

We now discuss the CTE in terms of the Grüneisen parameters [44]. We calculate the mode-dependent Grüneisen parameters $\gamma_m = -\frac{V}{\omega_m} (\frac{\partial \omega_m}{\partial V})_T$ and the weighted Grüneisen parameter $\gamma = \sum_m \gamma_m c_{vm}/\sum_m c_{vm}$, using the second- and third-order force constants of a given temperature as [17,45,46]

$$
\gamma_{m}=-\frac{1}{6 \omega_{m}^{2}} \sum_{i j k \alpha \beta \gamma} \frac{\epsilon_{m i \alpha}^{*} \epsilon_{m j \beta}}{\sqrt{M_{i} M_{j}}} r_{k}^{\gamma} \Psi_{i j k}^{\alpha \beta \gamma} e^{i \mathbf{q} \cdot \mathbf{r}_{j}}.
$$

Since the sign of the CTE $\alpha_V = \frac{\gamma C_v \rho}{K_T}$ is the same as $\gamma$, the evolution of $\gamma$ with temperature allows us to interpret the change of regime in terms of the evolution of the contribution of different phonon modes. In the high-temperature limit and if we do not take into account the modification of the second- and third-order force constants, the weighted Grüneisen parameter becomes constant and equal to the arithmetical mean of all mode-dependent Grüneisen parameters.

In Fig. 4, we decouple the effect of temperature due to the modification of the weight of the mode heat capacity from the effect due to the modification of the force constants by tracing several temperature-dependent weighted Grüneisen parameter curves using fixed force constants obtained at different temperatures. A large contribution to the NTE comes from the soft mode line between the R and M points, due to its small frequency and large variation—which shows that these types of compounds close to a mechanical instability are good candidates for NTE. When the temperature is increased, these mode Grüneisen parameters are mostly impacted by the modification of their frequency, which lowers their contribution to NTE. Still, the mode Grüneisen parameters at a given frequency are globally pushed up by temperature in the low-energy region. This is similar to what happens for the lifetimes, as discussed above. Both effects are necessary to


![](./images/811176043330142208_4.jpg)

FIG. 4. Mode-dependent Grüneisen parameters on a $15 \times 15 \times$
15 grid as a function of energy and temperature (left) and weighted
Grüneisen parameter interpolated between calculations with fixed
second- and third-order force constants corresponding to different
temperatures (right).

quantitatively understand the suppression of NTE that appears
around 1100 K (see the right panel of Fig. 4), in agreement
with the experiment.

It is also remarkable that the full temperature dependence
of the weighted Grüneisen parameter differs importantly from
the one obtained within the quasiharmonic approximation
in the whole temperature range, showing that higher-order
anharmonic effects are crucial in the behavior of the CTE
even at lower temperatures. This last statement is all the
more true if one takes into account the variation of the
volume to recalculate the phonon dispersions. Indeed, the soft
mode frequencies are lowered when the lattice parameter is
reduced and a phase transition can take place under pressure
[26,47]. In the standard Grüneisen formalism, this translates
in a lowering of the phonon frequencies with temperature via
$(\partial \omega_{m} / \partial T)_{P}=(\partial \omega_{m} / \partial V)_{T}(\partial V / \partial T)_{P}=-\omega_{m} \gamma_{m} \alpha_{V}$. In con-
trast, our calculations and the experimental data show that the
soft mode frequencies increase with temperature. A similar
anomaly has been observed in experimental measurements of
the phonon density of states in $ZrW_{2} O_{8}$ [40] and tentatively
attributed to quartic anharmonicity, which is indeed partially
captured in our method. Interestingly, the same anomalous
behavior happens also for the higher energy optical modes, that
are softened while the volume decreases in spite of a positive
Grüneisen parameter, showing that anharmonicity plays an
important role over the whole phonon spectrum.

In conclusion, we have used temperature-dependent anhar-
monic calculations to compute the evolution of the phonon
frequencies and scattering rates in $ScF_{3}$. We have predicted
an anomalous temperature dependence of the thermal con-
ductivity, notably due to the hardening of the soft mode
frequencies with increasing temperature, and interpreted it
as a general feature of this class of compounds. Finally, we
have shown that the weighted Grüneisen parameter acquires a
dependence in temperature that is qualitatively different from
the quasiharmonic behavior and explains the suppression of
negative thermal expansion. This demonstrates that taking
into account high-order anharmonicity is crucial for the
qualitative and quantitative computation of physical properties
at intermediate and high temperatures. Furthermore, this work
paves the way toward the search for new materials displaying
negative thermal expansion or low thermal conductivity from
ab initio calculations over a large temperature range.

Acknowledgments. We acknowledge useful discussions
with Ion Errea, Ole Hellman, Wu Li, and Stefano Curtarolo.
This work is partially supported by the French Agence
Nationale de la Recherche “Carnot” project SIEVE.

[1] M. T. Dove and H. Fang, Negative thermal expansion and
associated anomalous physical properties: Review of the lattice
dynamics theoretical foundation, Rep. Prog. Phys. 79, 066503
(2016).
[2] B. K. Greve, K. L. Martin, P. L. Lee, P. J. Chupas, K. W.
Chapman, and A. P. Wilkinson, Pronounced negative thermal
expansion from a simple structure: Cubic $ScF_{3}$, J. Am. Chem.
Soc. 132, 15496 (2010).
[3] C. W. Li, X. Tang, J. A. Muñoz, J. B. Keith, S. J. Tracy,
D. L. Abernathy, and B. Fultz, Structural Relationship between
Negative Thermal Expansion and Quartic Anharmonicity of
Cubic $ScF_{3}$, Phys. Rev. Lett. 107, 195504 (2011).
[4] Y. Liu, Z. Wang, M. Wu, Q. Sun, M. Chao, and Y. Jia, Negative
thermal expansion in isostructural cubic $ReO_{3}$ and $ScF_{3}$: A
comparative study, Comput. Mater. Sci. 107, 157 (2015).
[5] C. W. Li, Phonon anharmonicity of ionic compounds and metals,
Ph.D. thesis, California Institute of Technology, Pasadena,
2012, http://resolver.caltech.edu/CaltechTHESIS:05012012-
155623422.
[6] P. Lazar, T. Bučko, and J. Hafner, Negative thermal expansion
of $ScF_{3}$: Insights from density-functional molecular dynamics
in the isothermal-isobaric ensemble, Phys. Rev. B 92, 224302
(2015).
[7] M. Tachibana, T. Kolodiazhnyi, and E. Takayama-Muromachi,
Thermal conductivity of perovskite ferroelectrics, Appl. Phys.
Lett. 93, 092902 (2008).
[8] Y. Suemune and H. Ikawa, Thermal conductivity of $KMnF_{3}$,
$KCoF_{3}$, $KNiF_{3}$, and $KZnF_{3}$ single crystals, J. Phys. Soc. Jpn.
19, 1686 (1964).
[9] J. Martin, Thermal conductivity of $RbCaF_{3}$, in Phonon Scatter-
ing in Solids, edited by L. Challis, V. Rampton, and A. Wyatt
(Springer, New York, 1976), p. 258.
[10] A. J. H. Mante and J. Volger, The thermal conductivity of $BaTiO_{3}$
in the neighbourhood of its ferroelectric transition temperatures,
Phys. Lett. A 24, 139 (1967).
[11] H. Muta, K. Kurosaki, and S. Yamanaka, Thermoelectric
properties of reduced and La-doped single-crystalline $SrTiO_{3}$,
J. Alloys. Compd. 392, 306 (2005).
[12] S. R. Popuri, A. J. M. Scott, R. A. Downie, M. A. Hall, E.
Suard, R. Decourt, M. Pollet, and J.-W. G. Bos, Glass-like
thermal conductivity in $SrTiO_{3}$ thermoelectrics induced by
A-site vacancies, RSC Adv. 4, 33720 (2014).

[13] T. Maekawa, K. Kurosaki, and S. Yamanaka, Thermal and mechanical properties of perovskite-type barium hafnate, J. Alloys. Compd. 407, 44 (2006).

[14] S. Yamanaka, T. Hamaguchi, T. Oyama, T. Matsuda, S.-i. Kobayashi, and K. Kurosaki, Heat capacities and thermal conductivities of perovskite type BaZrO3 and BaCeO3, J. Alloys. Compd. 359, 1 (2003).

[15] P. Souvatzis, O. Eriksson, M. I. Katsnelson, and S. P. Rudin, Entropy Driven Stabilization of Energetically Unstable Crystal Structures Explained from First Principles Theory, Phys. Rev. Lett. 100, 095901 (2008).

[16] O. Hellman, I. A. Abrikosov, and S. I. Simak, Lattice dynamics of anharmonic solids from first principles, Phys. Rev. B 84, 180301 (2011).

[17] O. Hellman and I. A. Abrikosov, Temperature-dependent effec- tive third-order interatomic force constants from first principles, Phys. Rev. B 88, 144301 (2013).

[18] I. Errea, M. Calandra, and F. Mauri, First-Principles Theory of Anharmonicity and the Inverse Isotope Effect in Supercon- ducting Palladium-Hydride Compounds, Phys. Rev. Lett. 111, 177002 (2013).

[19] T. Tadano and S. Tsuneyuki, Self-consistent phonon calculations of lattice dynamical properties in cubic $SrTiO_3$ with first- principles anharmonic force constants, Phys. Rev. B 92, 054301 (2015).

[20] N. R. Werthamer, Self-consistent phonon formulation of anhar- monic lattice dynamics, Phys. Rev. B 1, 572 (1970).

[21] F. Zhou, W. Nielson, Y. Xia, and V. Ozolinš, Lattice Anhar- monicity and Thermal Conductivity from Compressive Sensing of First-Principles Calculations, Phys. Rev. Lett. 113, 185501 (2014).

[22] In this study, we use a cutoff of $5$ Å for the third-order force constants. Increasing this cutoff at $0$ K caused only marginal modifications of the Grüneisen parameters.

[23] This expression comes from the equipartition of energy in harmonic oscillators: $(\frac{\partial E_{k}}{\partial V})_{S}=\frac{1}{2}(\frac{\partial E}{\partial V})_{S}=\frac{1}{2}(\frac{\partial F}{\partial V})_{T}$ and the usual quasiharmonic derivation.

[24] O. Hellman, P. Steneteg, I. A. Abrikosov, and S. I. Simak, Temperature dependent effective potential method for accurate free energy calculations of solids, Phys. Rev. B 87, 104111 (2013).

[25] T. Lan, C. W. Li, O. Hellman, D. S. Kim, J. A. Muñoz, H. Smith, D. L. Abernathy, and B. Fultz, Phonon quarticity induced by changes in phonon-tracked hybridization during lattice expansion and its stabilization of rutile $TiO_2$, Phys. Rev. B 92, 054304 (2015).

[26] S. U. Handunkanda, E. B. Curry, V. Voronov, A. H. Said, G. G. Guzmán-Verri, R. T. Brierley, P. B. Littlewood, and J. N. Hancock, Large isotropic negative thermal expansion above a structural quantum phase transition, Phys. Rev. B 92, 134101 (2015).

[27] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Restoring the density-gradient expansion for exchange in solids and surfaces, Phys. Rev. Lett. 100, 136406 (2008).

[28] B. Grabowski, L. Ismer, T. Hickel, and J. Neugebauer, $Ab$ initio up to the melting point: Anharmonicity and vacancies in aluminum, Phys. Rev. B 79, 134106 (2009).

[29] B. Grabowski, Towards $ab$ initio assisted materials design: DFT based thermodynamics up to the melting point, Ph.D. thesis, Universität Paderborn, Paderborn, Germany, 2009, http://d- nb.info/999994581/34..

[30] W. Li, J. Carrete, N. A. Katcho, and N. Mingo, SHENGBTE: A solver of the Boltzmann transport equation for phonons, Comput. Phys. Commun. 185, 1747 (2014).

[31] K. Tani, Life time of soft modes in displacive-type ferroelectrics, Phys. Lett. A 25, 400 (1967).

[32] L. Lindsay and D. A. Broido, Three-phonon phase space and lattice thermal conductivity in semiconductors, J. Phys. Condens. Matter 20, 165209 (2008).

[33] In passing, we note that the modification of the lattice parameter in itself has nearly no incidence on the thermal conductivity.

[34] E. Grüneisen, Theorie des festen Zustandes einatomiger Ele- mente, Ann. Phys. 344, 257 (1912).

[35] N. Ashcroft and N. Mermin, Solid State Physics (Saunders College, Philadelphia, 1976).

[36] T. A. Mary, J. S. O. Evans, T. Vogt, and A. W. Sleight, Negative thermal expansion from 0.3 to 1050 kelvin in $ZrW_2O_8$, Science 272, 90 (1996).

[37] T. Chatterji, P. F. Henry, R. Mittal, and S. L. Chaplot, Negative thermal expansion of $ReO_3$: Neutron diffraction experiments and dynamical lattice calculations, Phys. Rev. B 78, 134105 (2008).

[38] M. Dapiaggi and A. N. Fitch, Negative (and very low) thermal expansion in $ReO_3$ from 5 to 300 K, J. Appl. Crystallogr. 42, 253 (2009).

[39] D. F. Gibbons, Thermal expansion of some crystals with the diamond structure, Phys. Rev. 112, 136 (1958).

[40] G. Ernst, C. Broholm, G. Kowach, and A. Ramirez, Phonon density of states and negative thermal expansion in $ZrW_2O_8$, Nature (London) 396, 147 (1998).

[41] T. Chatterji, T. C. Hansen, M. Brunelli, and P. F. Henry, Negative thermal expansion of $ReO_3$ in the extended temperature range, Appl. Phys. Lett. 94, 241902 (2009).

[42] U. D. Wdowik, K. Parlinski, T. Chatterji, S. Rols, and H. Schober, Lattice dynamics of rhenium trioxide from the quasiharmonic approximation, Phys. Rev. B 82, 104301 (2010).

[43] T. Chatterji, P. G. Freeman, M. Jimenez-Ruiz, R. Mittal, and S. L. Chaplot, Pressure- and temperature-induced $M_3$ phonon softening in $ReO_3$, Phys. Rev. B 79, 184302 (2009).

[44] Such a discussion stays meaningful in the present case, since the definition $\alpha_{V}=\frac{\gamma C_{v}\rho}{K_{T}}$ gives $\gamma=\frac{1}{\rho C_{v}}(\frac{\partial S}{\partial V})_{T}$, the thermal density matrix $\rho_{h}$ is calculated within the harmonic approximation, and $S=-k_{B}\mathrm{Tr}(\rho_{h}\ln\rho_{h})$.

[45] J. Fabian and P. B. Allen, Thermal Expansion and Grüneisen Pa- rameters of Amorphous Silicon: A Realistic Model Calculation, Phys. Rev. Lett. 79, 1885 (1997).

[46] D. A. Broido, A. Ward, and N. Mingo, Lattice thermal conductivity of silicon from empirical interatomic potentials, Phys. Rev. B 72, 014308 (2005).

[47] K. Aleksandrov, V. Voronov, A. Vtyurin, S. Goryainov, N. Zamkova, V. Zinenko, and A. Krylov, Lattice dynamics and hydrostatic-pressure-induced phase transitions in $ScF_3$, J. Exp. Theor. Phys. 94, 977 (2002).
