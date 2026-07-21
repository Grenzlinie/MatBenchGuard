![](./images/812787094400270337_1.jpg)

# Epitaxial growth kinetics on patterned substrates

N. Haider, M. R. Wilby, and D. D. Vvedensky

Citation: *Applied Physics Letters* **62**, 3108 (1993); doi: 10.1063/1.109153
View online: http://dx.doi.org/10.1063/1.109153
View Table of Contents: http://scitation.aip.org/content/aip/journal/apl/62/24?ver=pdfcov
Published by the AIP Publishing

---

## Articles you may be interested in
[Kinetic Monte Carlo simulation of InAs quantum dot growth on nonlithographically patterned substrates](https://aip.scitation.org/doi/10.1116/1.2731335)
J. Vac. Sci. Technol. B **25**, 1072 (2007); 10.1116/1.2731335

[Growth kinetics and modeling of selective molecular beam epitaxial growth of GaAs ridge quantum wires on pre-patterned nonplanar substrates](https://aip.scitation.org/doi/10.1116/1.1773841)
J. Vac. Sci. Technol. B **22**, 2266 (2004); 10.1116/1.1773841

[Selective epitaxial growth of organic molecules on patterned alkali halide substrates](https://aip.scitation.org/doi/10.1063/1.123416)
Appl. Phys. Lett. **74**, 941 (1999); 10.1063/1.123416

[Strainmodulated epitaxy: Modification of growth kinetics via patterned, compliant substrates](https://aip.scitation.org/doi/10.1116/1.588892)
J. Vac. Sci. Technol. B **14**, 2170 (1996); 10.1116/1.588892

[High quality molecular beam epitaxial growth on patterned GaAs substrates](https://aip.scitation.org/doi/10.1063/1.96012)
Appl. Phys. Lett. **47**, 712 (1985); 10.1063/1.96012

---

![](./images/812787094400270337_2.jpg)

# Epitaxial growth kinetics on patterned substrates
N. Haider, M. R. Wilby, $^{a)}$ and D. D. Vvedensky
The Blackett Laboratory, Imperial College, London SW7 2BZ, United Kingdom
(Received 21 December 1992; accepted for publication 23 March 1993)

The temperature dependence of the growth kinetics on V-grooved substrates is studied by computer simulation, with attention focused upon the evolution of the morphology. We find a distribution of growth rates on GaAs(001) at high temperatures due to surface diffusion of adatoms from one facet to the other. However, at low temperatures, where surface migration processes are less important, growth on these substrates proceeds in a shape-preserving manner. Comparison with scanning microprobe reflection high-energy electron-diffraction intensity oscillations on GaAs(001) near (111) surfaces shows that our results are in qualitative agreement with observed behavior.

Molecular-beam epitaxy (MBE) overgrowth on patterned substrates attracts interest in the growth mechanisms because it shows intriguing and potentially useful growth features which are not observed on singular or vicinal surfaces. One such feature is the lateral variation of the growth rate on nonplanar substrates. $^{1}$ There are two mechanisms related to the MBE growth technique which are responsible for the phenomenon. First, the growth rate is limited by a geometric factor, whereby the effective incident flux arriving at each facet is a function of the orientation of the facet. $^{2}$ The second mechanism influencing the local growth rate is the surface migration of the species from facet to facet. $^{3}$ This phenomena is dependent on the crystallographic orientation of each facet, the growth parameters, and the nature of the atoms on the surface. If the dimensions of the pattern are of the order of the surface diffusion length of the mobile surface species, then it is possible for those adatoms to migrate to and incorporate in planes with lower surface energies.

In order to understand and exploit the kinetics of growth on patterned substrates we must develop a microscopic model of the interaction between two distinct facets. In this letter we study the growth kinetics, in particular, the effect of surface migration, on an (001) surface with a faceted V groove [45° with respect to planar (001) surface] during MBE. This allows us to study the general features during both equilibrium and far-from-equilibrium growth phases on a faceted structure and allows comparisons to be made with experiment. The details of such a complex interplay of two facets as a function of growth conditions can most easily be resolved by computer-simulation techniques, though there have been analytic studies that have clarified some general issues related to this question. $^{4,5}$

Our model of facet growth during MBE entails growth of a simple cubic lattice in which vacancies and overhangs are forbidden, the so-called solid-on-solid (SOS) criterion. $^{6}$ The use of a monoatomic model emphasizes the kinetics of the growth-III species as being rate limiting, i.e., by comparison, the dissociative reaction kinetics and the subsequent migration of the As occur over a sufficiently short time scale as to be regarded as effectively instantaneous. This allows a mean-field treatment of the As, which is assumed to play only a stoichiometric role at the microscopic level. Experimental evidence for this comes from the observation that the growth kinetics of GaAs are affected only at low As pressure. $^{7}$

The growth kinetics in our model are described by two processes: the random deposition of atoms onto the surface and the migration of adatoms along the substrate. Evaporation is neglected, since for typical growth conditions in MBE of III-V compounds the desorption flux of the group-III species is negligible. The deposition site is chosen randomly with each site being chosen with equal probability. Each surface atom migrates to a nearest neighbor with a site-dependent Arrhenius hopping rate, $k(E,T)$ $=k_{0}\exp(-E/k_{B}T)$, where $k_{0}$ is the vibrational frequency of a surface atom $(k_{0}=2k_{B}T/h)$, $k_{B}$ is Boltzmann's constant, $T$ is the substrate temperature, and $E$ is the energy barrier to hopping, which depends on the environment of the active atom before hopping, and $h$ is Planck's constant. The hopping process is isotropic in that each of the four destination sites have equal probability of being chosen.

In order to consider situations where facets other than (001) are stable, we must modify our basic model. $^{8}$ Previous studies $^{9}$ showed that for a lattice gas with nearest-neighbor interactions $(J_{1}>0)$ the equilibrium crystal shape evolves from cubic at $T=0$ K to spherical at high temperatures. During this transition facets remain which are separated by rounded regions with smooth edges. By including the second-nearest-neighbor interaction $(J_{2}$ $=RJ_{1}$, with $1>R>0)$ the evolution is similar to the nearest-neighbor model except that (111) and (110) facets are found in addition to (001) facets. For $R<0$, the equilibrium crystal shape remains cubic from $T=0$ K up to a finite temperature before rounded surfaces appear at the corners of the cube. In this case both smooth and sharp edges are found.

These studies illustrate the need for including second-nearest-neighbor interactions to incorporate facetting behavior. The hopping barrier $E$ introduced above now is taken to have the following form: $E=E_{S}+nE_{N}+mE_{2N}$, where $n$ is the number of nearest neighbors in the plane of the facet and $m$ is the number of next-nearest neighbors out of this plane (Fig. 1). The neglect of next-nearest

$^{a)}$Also at Department of Electrical and Electronic Engineering, University College, London WC1E 7JE, UK.


![](./images/812787094400270337_3.jpg)

FIG. 1. Nearest-neighbor, second-nearest-neighbor, and surface contributions to the hopping barrier in the SOS model. The shaded atoms give the effective substrate contribution to the barrier on the respective surfaces.

neighbors in the lateral plane is only for computational reasons and is not expected to lead to any qualitative differences from the results reported below. In the absence of experiments¹⁰ which may be used to estimate¹¹,¹² values for energy barrier, we will use values that are expected to reflect the average morphological behavior of GaAs based on observations during scanning microprobe RHEED experiments on GaAs (001) near the (111) surface. The simulations were carried out on 200×200 V-grooved lattices with periodic boundary conditions at substrate temperatures ranging from 700 to 850 K with an incident deposition flux of one monolayer per second.

We consider first a simulation with the parameters $E_{2N}$ =0.1 eV, $E_S$=1.0 eV, and $E_N$=0.3 eV. Since $E_{2N}<E_N$, this choice results in greater mobility of single adatoms on the (001) surface as compared to the diagonal surface (Fig. 1). Figure 2(a) shows the effective growth rate. In both panels of this figure the two-dimensional morphology has been projected by averaging over one lateral substrate dimension to give a one-dimensional surface profile. The relative growth rate is simply this average morphology from which the number of monolayers grown are subtracted. This allows the general features of growth to be readily identified and compared with experimental observations. At low temperatures growth occurs in a shape-preserving manner because the low adatom mobility means that atoms cannot easily migrate to the lower-energy facet. At higher temperatures, the flat terrace shows a large negative growth rate because free adatoms are diffusing across the flat terrace toward the diagonal facet, on which there is a lower mobility. As deposition continues, adatoms diffuse down the diagonal facet, resulting in a positive growth rate deep in the groove. If growth is continued indefinitely the growth front will planarize as the two diagonal facets merge. Aside from a difference in time scale, this is the

![](./images/812787094400270337_4.jpg)

FIG. 2. The projected effective growth rate after growth of 500 monolayers for the indicated substrate temperatures. The initial lattice is shown as a reference. The adatom mobility is (a) higher on the flat surface than on the diagonal surface, and (b) is lower on the flat surface than on the diagonal surface.

![](./images/812787094400270337_5.jpg)

FIG. 3. A comparison between (a) a SREM image of the GaAs surface near the edge of the (111)B surface during MBE at a temperature of 450 °C where the vertical axis is the time axis with stripes reflecting RHEED intensity oscillations and (b) the time evolution of the projected effective growth rate at the indicated times. The growth rates on the (001) surface near the edge of the (111)B surface are seen to decrease.

3109
Appl. Phys. Lett., Vol. 62, No. 24, 14 June 1993
Haider, Wilby, and Wedensky

![](./images/812787094400270337_6.jpg)

![](./images/812787094400270337_7.jpg)

FIG. 4. A comparison between (a) a SREM image of the GaAs surface near the (111)A surface during MBE growth at a temperature of $550\ ^{\circ}\text{C}$ and (b) the time evolution of the projected effective growth rate at the indicated times. The growth rates on the (001) surface near the edge of the (111)A surface are seen to increase.

behavior seen with the original model, where only nearest-neighbor interactions are considered.

Consider now the case where $E_{2N}$=0.38 eV, $E_{S}$=0.3 eV, and $E_{N}$=0.1 eV, so $E_{2N}>E_{N}$. This ensures a greater mobility of single adatoms on the diagonal surface as compared with the (001) surface (Fig. 1). The value of $E_{S}$ was changed in order to maintain a similar temperature scale for both cases. The effective growth rate is shown in Fig. 2(b). At low temperatures growth again occurs in a shape-preserving manner as in the previous case. At higher temperatures, the groove exhibits a negative growth rate since adatoms migrate from the diagonal facet to the flat terrace. This leads to a maximum in the supersaturation at the edge of the flat surface, resulting in the formation of a "lip." As growth continues the growth front again planarizes as the two diagonal facets diverge, which is the opposite behavior to that seen for the case discussed above.

These observations are reinforced by real-time scanning microprobe RHEED measurements on GaAs(001) near (111)A and (111)B surfaces (Figs. 3 and 4). Experimental data from real-time scanning microprobe RHEED measurements$^{13}$ on GaAs(001) near a (111)B [Fig. 3(a)] show that the period of the specular RHEED intensity increased on the (001) surface near the (111)B facet, implying a slower growth rate. The relative growth rate rapidly decreases as a function of the distance from the edge of the interface. Near this interface the experiment shows that the intervals between the maxima in the brightness is becoming larger with time, which indicates that the effective growth rate is decreasing. The experimental results$^{14}$ also show that the gradient of the (111)B facet is smaller at higher temperatures, which is also in agreement with the observed projected morphology in Fig. 2(a).

The corresponding measurements on GaAs(001) near a (111)A surface reveal a higher growth rate, as shown in Fig. 4(a). The relative growth rate increases rapidly as a function of the distance from the edge of the interface. Near this interface the intervals between the maxima in the reflected intensity are decreasing with time, which implies that the effective growth rate is increasing, with the gradients of the increases being smaller at higher temperatures. All of these observations are in qualitative agreement with the simulated morphologies in Fig. 2(b).

N. H. would like to thank the U. K. Science and Engineering Research Council for their financial assistance. The authors would also like to thank Professor Y. Katayama for providing the experimental results. The support of Imperial College and the Research Development Corporation of Japan under the auspices of the "Atomic Arrangement: Design and Control for New Materials" Joint Research Program is gratefully acknowledged.

$^{1}$J. S. Smith, P. L. Derry, S. Margalit, and A. Yariv, Appl. Phys. Lett. 47, 712 (1985).
$^{2}$W. T. Tsang and A. Cho, Appl. Phys. Lett. 30, 293 (1977).
$^{3}$E. Kapon, M. C. Tamargo, and D. M. Hwang, Appl. Phys. Lett. 50, 347 (1987).
$^{4}$C. Ratsch and A. Zangwill, Appl. Phys. Lett. 58, 403 (1991).
$^{5}$M. Ozdemir and A. Zangwill, J. Vac. Sci. Technol. A 10, 684 (1992).
$^{6}$J. D. Weeks and G. H. Gilmer, Adv. Chem. Phys. 40, 157 (1979).
$^{7}$P. Chen, J. Y. Kim, A. Madhukar, and N. M. Cho, J. Vac. Sci. Technol. B 4, 890 (1986).
$^{8}$S. Clarke and D.D. Vvedensky, Phys. Rev. Lett. 58, 2235 (1987).
$^{9}$C. Rottman and M. Wortis, Phys. Rev. B 29, 328 (1984).
$^{10}$J. H. Neave, P. J. Dobson, B. A. Joyce, and J. Zhang, Appl. Phys. Lett. 47, 100 (1985).
$^{11}$T. Shitara, E. Kondo, and T. Nishinaga, J. Cryst. Growth 99, 530 (1990).
$^{12}$T. Shitara, D. D. Vvedensky, M. R. Wilby, J. Zhang, J. H. Neave, and B. A. Joyce, Phys. Rev. B 46, 6815 (1992).
$^{13}$M. Hata, A. Watanabe, and T. Isu, J. Cryst. Growth 111, 83 (1991).
$^{14}$M. Hata, T. Isu, A. Watanabe, and Y. Katayama, J. Vac. Sci. Technol. B 8, 692 (1990).