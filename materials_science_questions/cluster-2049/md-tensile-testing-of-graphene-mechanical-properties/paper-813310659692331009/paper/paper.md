PHYSICAL REVIEW B 85, 205429 (2012)

# Graphene nanoribbons subject to gentle bends

P. Koskinen*

NanoScience Center, Department of Physics, University of Jyväskylä, 40014 Jyväskylä, Finland
(Received 24 February 2012; revised manuscript received 25 April 2012; published 15 May 2012)

Since graphene nanoribbons are thin and flimsy, they need support. Support gives firm ground for applications, and adhesion holds ribbons flat, although not necessarily straight: Ribbons with a high aspect ratio are prone to bend. The effects of bending on ribbons' electronic properties, however, are unknown. Therefore, this article examines the electromechanics of planar and gently bent graphene nanoribbons. Simulations with density-functional tight-binding and revised periodic boundary conditions show that gentle bends in armchair ribbons can cause significant widening or narrowing of energy gaps. Moreover, in zigzag ribbons sizable energy gaps can be opened due to axial symmetry breaking, even without magnetism. These results infer that, in the electronic measurements of supported ribbons, such bends must be heeded.

DOI: 10.1103/PhysRevB.85.205429
PACS number(s): 68.65.Pq, 61.48.Gh, 62.25.-g, 73.22.Pr

## I. INTRODUCTION

Graphene nanoribbons (GNRs) are atomically thin and only nanometers wide, which makes them the flimsiest materials in the world. Today such ribbons, acclaimed for promising applications, are fabricated in many ways, $^{1,2}$ and investigated for heat conduction, $^{3}$ edge features, $^{4-6}$ and electronic characteristics, $^{7}$ among many other properties. However, since the ribbons are flimsy, they need stabilizing support-although even then ribbons can get folded, torn, rippled, and bent. $^{7-10}$

Also supports are different, as the interaction with graphene can be either physical or chemical. In physisorption the support interaction is weak, graphene's electronic structure remains decoupled, and adhesion arises from the dispersive van der Waals interactions alone. $^{11}$ In chemisorption the support interaction is stronger, and the presence of chemical bonds alters graphene's electronic structure. $^{12}$ Therefore adhesion, responsible for holding ribbons planar, ranges from $\epsilon=4$ meV/atom to 70 meV/atom. $^{12,13}$ However, fabrication processes, surface inhomogeneities, pinning, AFM tip manipulation, heat treatment, or mechanical strains can make ribbons subject to gentle bends, as sketched in Fig. 1(a). Indeed, planar and gentle bending can be directly seen in scanning tunneling microscopy experiments. $^{7-10}$ Distortions like twisting, on the contrary, are less relevant on supports. $^{14-16}$ Only gentle bends are interesting, as sharp bends are structurally unstable (ribbons would desorb and fold instead). $^{8,10}$

The purpose of this work, therefore, is to answer the following simple question: What happens to GNRs' electronic structure upon planar bending? It turns out that simple geometrical arguments, together with nearest (and next-nearest) neighbor tight-binding reasoning, are sufficient for a thorough understanding of the electromechanics of bent GNRs. These insights should hence help interpreting imperfect experiments with these distortion-prone ribbons.

## II. SIMULATING PHYSISORBED RIBBONS WITH PURE BENDING

I modeled GNRs as free standing, without explicit presence of the support; it was there merely as a planar constraint. The underlying justification was to model physisorption where the support and GNR electronic structures are essentially decoupled. For chemisorption the results are not directly valid.

The focus is on the bent sections of very long ribbons, with bending viewed as a local property. Apart from bending, planar ribbons can also stretch and shear; those deformations have been investigated by conventional methods. $^{17,18}$ The deformation mode certainly depends on the experimental conditions, and especially in short ribbons the strain patterns can become complicated. $^{19,20}$ However, ribbons yield easily upon lateral forcing, and adjust themselves readily to minimum-energy geometries. $^{21-24}$ In bent geometries sliding is particularly easy as the ribbon and the support are mostly out of registry. Long ribbons pinned at two distant locations, therefore, can remove high-energy shearing and stretching by sliding, and favor pure bending. $^{25}$ I remark that the central results, as discussed below, will be valid also beyond pure bending.

I modeled the electronic structure by density-functional tight-binding (DFTB) method, $^{26,27}$ and the bent geometry itself by revised periodic boundary conditions. $^{28-30}$ Atoms in the simulation cell were from GNR translational cell of length $L$, and the associated symmetry operation was a rotation of an angle $\alpha$ around a given origin, as in Refs. 29 and 31 [see Fig. 1(b)]. This means, therefore, that the simulated systems were effectively GNR hoops, containing hundreds of thousands of atoms. Since the bends are gentle and the charge transfer with physisorption usually small, it's reasonable to assume that simulation describes the properties of bends in GNRs in a local sense. $^{5}$ At any rate, regarding the bending, simulations were exact and the sole approximation was the DFTB method itself.

Throughout this article I will use the dimensionless parameter

$$
\Theta=\frac{W}{2 R} \tag{1}
$$

to quantify the amount of bending. $^{32}$ Then, to simulate GNR of width $W$ with bending close to $\Theta'$, I chose $\alpha=L/R'$, with $R'=W/(2\Theta')$ as the initial guess for the radius of curvature, and optimized the structure. The only fixed parameter was $\alpha$, so $R$ and $\Theta$ were outcomes of the optimization, although $R \approx R'$ and $\Theta \approx \Theta'$. Here I remark that, because $\alpha$'s are small (down to $10^{-3}$ radians), the optimization was arduous and required

1098-0121/2012/85(20)/205429(5)
205429-1
©2012 American Physical Society

![](./images/813310659692331009_1.jpg)

FIG. 1. (Color online) (a) Supported graphene nanoribbon sketched for gentle, planar bends. (b) The red (dark gray) atoms constitute the unit cell, simulated with revised periodic boundary conditions; the symmetry operation is the rotation of an angle $\alpha$ around a given origin (not shown). The ribbon's width $W$ is defined by the outmost carbon atoms and $R$ is the mean radius of curvature. The bending parameter of Eq. (1), here $\Theta=0.1$, is also equal (approximately) to the compressive strain at the inner edge $(\varepsilon_{in}=-\Theta)$ and to the tensile strain at the outer edge $(\varepsilon_{out}=\Theta)$.

maximum force criteria as small as $f_{\text{max}} < 10^{-5}$ eV/Å (look at Ref. 30 to see why).

I conducted such simulations for hydrogen-passivated armchair ribbons ($N$-AGNRs) and zigzag ribbons ($N$-ZGNRs), with $N=5\ldots40$, with $W$ up to $84$ Å, with 74 different GNRs in total (see Ref. 33 for GNR notations). Each GNR was optimized for ten bendings between $\Theta=0$ and $\Theta=0.1$. The reason for $\Theta=0.1$ as the upper limit for bending that I term "gentle" will be clarified later. Finally, the number of $\kappa$ points was $50$ Å/$L$ for geometry optimization and $500$ Å/$L$ for electronic structure analysis.

### III. BENT RIBBONS GET STRETCHED

Let us now turn our attention to the results. Prior to discussing electronic properties, however, let us first look at energy and geometry. The energy in bent ribbons, as hinted by nanoshell elasticity, $^{34}$ comes chiefly from axial in-plane strain. A quick estimate yields energy per unit area as $E/A=\frac{1}{6}k\Theta^{2}$, where $k=25$ eV Å$^{-2}$ is graphene's in-plane modulus. $^{35}$ This simple estimate is in fair agreement with the simulations, as shown in the inset of Fig. 2. Only the narrowest ribbons deviate from this estimate, for two reasons: First, the comparison of $W$ between atomic and continuum methods is inherently ambiguous; for small $W$ this ambiguity is emphasized. Second, in narrow ribbons the value of $k$ is affected by distinct elastic properties near the edges. While I could remedy these deficiencies by improving the model, my main interest is not in the minutiae of narrow ribbons, but in the wider ribbons and their universal trends.

If we set the adhesion energy $\epsilon$ equal to the strain energy, we get
$$
\Theta_{\epsilon}=\sqrt{6\epsilon/kA_{c}} \tag{2}
$$
as a rough estimate for the limit where the ribbon rather desorbs and straightens than remains adsorbed and bent on the support. The maximum adhesion $\epsilon=70$ meV/atom yields $\Theta_{\epsilon}=0.08$, justifying the upper limit $\Theta\lesssim0.1$ for a "gently" bent ribbon, even though $\Theta_{\epsilon}$ really depends on the substrate. This is only an order-of-magnitude estimate, as fluctuations and finite-size effects can cause ribbons to desorb earlier. Direct experimental evidence $^{8}$ shows how GNRs on SiO$_2$ bend up to $\Theta\approx0.01$—still nearly half the simple-minded limit of $\Theta_{\epsilon}\approx0.025$ given by $\epsilon\approx6$ meV/Å$^{2}$. $^{36}$

![](./images/813310659692331009_2.jpg)

FIG. 2. (Color online) The cross-ribbon averaged strain $\varepsilon_{\text{avg}}$ as a function of bending parameter $\Theta$ for AGNRs (solid lines) and for ZGNRs (dashed lines); the bold dashed line is an analytical estimate. Inset: Elastic energy density as a function of bending; the bold dashed line is an analytical estimate, Eq. (4). In both plots the line width is proportional to $W$. Hence both in $\varepsilon_{\text{avg}}$ and in $E/A$ the largest deviations are for the narrowest ribbons.

Given the definition for $\Theta$, the strain on the ribbon's inner edge is $\varepsilon_{\text{in}}\approx-\Theta$ and on the outer edge $\varepsilon_{\text{out}}\approx\Theta$. With strains around $10\%$ the bond anharmonicities begin to emerge, and stretching becomes cheaper, compression more expensive. This implies that the neutral line moves away from the origin ($R$ increases) and the ribbon stretches. We can take this effect into account by a strain-dependent in-plane modulus, $k(\varepsilon)=k_{0}(1-\gamma\varepsilon)$. Then, by minimizing the total energy per unit length
$$
\int_{R-W/2}^{R+W/2}\frac{1}{2}k_{0}(1-\gamma\varepsilon)\varepsilon^{2}\mathrm{d}r \tag{3}
$$
with respect to $R$, we obtain the cross-ribbon averaged strain as
$$
\varepsilon_{\text{avg}}=\frac{1}{2}\gamma\Theta^{2}. \tag{4}
$$
This analytical estimate, given the value $\gamma=1.7$ obtained from DFTB simulations of stretched GNRs, agrees well with simulations, as shown in Fig. 2. The largest deviations occur again for the narrow ribbons, albeit with opposite tendencies for AGNRs and ZGNRs due to different edge morphologies.

### IV. ARMCHAIR RIBBONS ARE DOMINATED BY STRETCHING

Equipped with these geometrical notions, let us now turn our attention to the electronic properties, starting with AGNRs. The inset in Fig. 3(a) shows the energy gaps for the known three families of $N$-AGNRs, defined by $q=\mathrm{mod}(N,3).^{33,37}$ The gaps scale as $E_{g}\approx\beta W^{-1}$, where $\beta\approx13$ eV Å for $q=0,1$ (for $q=2$ the scaling is a bit different). Figure 3(a) shows how these gaps respond to bending: They widen or narrow with the same $q$-dependent families. Deviations occur only for the narrowest ribbons.

These trends can be understood by the following model. The energy gaps in stretched $q=0,1$ AGNRs depend on the

![](./images/813310659692331009_3.jpg)

![](./images/813310659692331009_4.jpg)

FIG. 3. (Color online) Electronic structure of bent AGNRs. (a) Bending-induced gap changes $E_{g}(\Theta)-E_{g}(0)$ for the three $q$ families of AGNRs. Line width is proportional to $W$; dashed lines are estimates for $q=0,1$. Inset: Gaps in straight AGNRs. (b) Wave functions for the frontier orbitals in straight 16-AGNR ($q=1$): the highest occupied molecular orbital (HOMO) and the lowest unoccupied molecular orbital (LUMO). (c) Density of states for 16-AGNR with straight ($\Theta=0.0$), bent ($\Theta=0.1$), and stretched ($\varepsilon=\frac{1}{2}\gamma(0.1)^2=0.85\%$) geometries.

strain as $\Delta E_{g}^{\text{straight}} \approx (-1)^{q}\varepsilon\delta$ with $\delta=12$ eV (fit for $q=2$ is just more complex). $^{17,38}$ The origin for this strain dependence is illustrated in Fig. 3(b) for 16-AGNR with $q=1$: The highest occupied orbital is bonding and the lowest unoccupied orbital is antibonding along the ribbon's axis, and therefore stretching tends to narrow the gap (for $q=0$ AGNRs the situation is the opposite and for $q=2$ intermediate). $^{39}$ Next, if we pretend, in effect, that the bent AGNRs experience only the average axial strain (even if the strain is uneven), and thus juxtapose $\varepsilon$ with $\varepsilon_{\text{avg}}$ from Eq. (4), we get

$$
\Delta E_{g}(\Theta)\approx\frac{1}{2}(-1)^{q}\gamma\delta\Theta^{2}. \tag{5}
$$

Figure 3(a) plots these estimates for $q=0$ and $q=1$ AGNRs by the dashed lines. The fair agreement suggests that the electronic structure of AGNRs subject to bending is dominated by the cross-ribbon averaged strain. Similar physics have been observed previously in bent carbon nanotubes and twisted GNRs. $^{15,31,39,40}$ Hence the argument is easily generalized to combined bending and stretching, where the electronic structure is modified by the average strain $\varepsilon_{\text{stretch}}+\frac{1}{2}\gamma\Theta^{2}.^{15}$

These trends, as given by four-valence DFTB, are reproduced by a $\pi$-only tight-binding Hamiltonian

$$
H=-t\sum_{i,j}^{\text{n.n.}}c_{i}^{\dagger}c_{j}-t'\sum_{i,j}^{\text{next-n.n.}}c_{i}^{\dagger}c_{j}, \tag{6}
$$

with the nearest-neighbor (n.n.) hopping parameter

$$
t(r)=2.6\ \text{eV}-5.8\ \text{eV}/\mathring{\text{A}}\ (r-1.42\mathring{\text{A}}), \tag{7}
$$

and with the next-nearest neighbor hopping equal to zero ($t'=$ 0, not shown). Figure 3(c) shows further that the stretching analogy extends beyond energy gaps, as the entire density of states (DOS) is well described by the stretched geometry. This carries the average strain analogy also for optical transitions, as shown earlier. $^{31}$ Note that, if gauged through the relative gap change $|\Delta E_{g}/E_{g}|\approx0.8\mathring{\text{A}}^{-1}W\Theta^{2}$, the influence of bending becomes more important as $W$ increases.

## V. ZIGZAG RIBBONS ARE DOMINATED BY BROKEN SYMMETRY

Let us now leave AGNRs and turn our attention to the electronic properties of ZGNRs. First I have to remind that, for

![](./images/813310659692331009_5.jpg)

FIG. 4. (Color online) Electronic structure of bent ZGNRs. (a) Band structure of 10-ZNGR with straight and bent geometries. For the straight ribbon, having a reflection symmetry, the dashed lines denote symmetric and solid lines denote antisymmetric states under reflection. (For the bent ribbons no such distinction can be made.) (b) Wave functions of the frontier orbitals in straight 10-ZGNR: highest occupied molecular orbital (HOMO, symmetric) and lowest unoccupied molecular orbital (LUMO, antisymmetric). (c) Density of states in straight and bent 10-ZGNR. The dashed lines are from a next-nearest-neighbor tight-binding model [Eq. (6) with Eq. (8)]. Inset: Gaps for all ZGNRs plotted as a function of $\Theta-\Theta_{\text{crit}}$ ($E_{g}=0$ when $\Theta<\Theta_{\text{crit}}$).

straight ZGNRs as such, the spin-parallel DFTB simulations are dubious, given the prediction for a spin-polarized ground state.³³ The magnetic structure should arise when the curious flat bands near the Fermi level⁴¹ [left panel of Fig. 4(a)]—the famous edge states—spin polarize, lift degeneracies, and open a gap (not shown).³³ This way spontaneous magnetization can stabilize the electronic structure.

It has been shown that, unlike in AGNRs,³⁸ the electronic structure in ZGNRs is unaffected by stretching.¹⁷,⁴² Therefore, after discovering above the average-strain argument with AGNRs, it's natural to guess that bending would leave ZGNRs' electronic structure unaffected. The right panel of Fig. 4(a) shows, however, that *bending can open an energy gap in ZGNRs*. That is, electronic structure is stabilized by sheer bending, and the cause for magnetic spin polarization is lost. Note how the band structure changes only near the Fermi level, while other bands remain stable.

The mechanism of the gap opening is related to broken reflection symmetry, as clarified by the following three-step reasoning. First step: The bands are called "flat" because they have small dispersion. In the absence of next-nearest-neighbor hopping ($t' = 0$), the Hamiltonian (6) gives edge states whose dispersion and energy are essentially zero, independent of $t$. This is illustrated in Fig. 4(b), where flat band electrons appear localized to next-nearest-neighbor sites, separated by vacancies. Therefore the $t$ in Eq. (7), even if strain dependent, doesn't affect the flat bands—splitting and dispersion hence require next-nearest-neighbor hopping $t'$. Second step: Fitting $t'$ to strained GNRs by DFTB gives
$$
t'(r)=0.25\ \mathrm{eV}-0.6\ \mathrm{eV\mathring{A}}\ (r-2.46\mathring{A}).\tag{8}
$$

The Hamiltonian (6), with hoppings (7) and (8), reproduces the electronic structure fairly well, as shown by the DOS for 10-ZGNR in Fig. 4(c). [Pure stretching leaves DOS intact (not shown).] Third step: the flat band energies (also the band dispersion) are proportional to $t'$ and hence proportional to edge strain via Eq. (8). Upon bending, the reflection symmetry breaks and states localize on either of the edges with strain difference $\varepsilon_{\rm out}-\varepsilon_{\rm in}=2\Theta$; opposite edges hence get unequal hoppings $\Delta t'=t'_{\rm out}-t'_{\rm in}\propto\Theta$. Because energy splitting is proportional to $\Delta t'$, it is also proportional to $\Theta$. This is the mechanism by which bending splits the flat bands with direct proportionality to $\Theta$.

As mentioned above, since $t'$ gives flat bands a small dispersion, splitting does not open the gap immediately. When $W$ increases, the span of the flat region in $k_z$ space increases, and gap opening requires larger splitting. A fit to all ZGNRs yields a critical value for opening a gap as $\Theta_{\rm crit}\approx W/200$ nm (or $R_{\rm crit}\approx100$ nm for all $W$), yielding the energy gap as
$$
E_{g}^{\rm ZGNR}\approx4\ \mathrm{eV}(\Theta-\Theta_{\rm crit}).\tag{9}
$$

The gaps, displaying values up to 0.4 eV, are plotted in the inset of Fig. 4(c).

## VI. CONCLUSIONS

The physics in AGNRs and ZGNRs hence appear quite different: AGNRs are governed by average strain, whereas ZGNRs are governed by broken reflection symmetry. The effects of broken symmetry on AGNRs or average strain on ZGNRs surely exist, but they are just less important. In ZGNRs bending can have particular impact on transport, since the localization of edge states depends on the direction of bending; if the ribbon has bends both to the left and to the right, the current-carrying electrons need to jump from one edge to the other, suggesting width-dependent resistivity.⁴³ Although it's plausible that bent ZGNRs indeed acquire gaps and turn nonmagnetic, spin-polarized calculations would be opportune, even if the existence of magnetism has been disputed also for the straight ribbons.⁴⁴

I obtained similar results also for unpassivated GNRs, observing similar phenomena. Thus it appears that these clear trends arise from simple physics with plausible explanations, and it's unlikely that, say, higher level electronic structure methods should change the picture. I believe, therefore, that these general trends are helpful enough to serve as rules of thumb to aid GNR device fabrication and analysis.

## ACKNOWLEDGMENTS

I acknowledge Teemu Peltonen for discussions, the Academy of Finland for funding, and the Finnish IT Center for Science (CSC) for computer resources.

*pekka.koskinen@iki.fi

¹D. V. Kosynkin, A. L. Higginbotham, A. Sinitskii, J. R. Lomed, A. Dimiev, B. K. Price, and J. M. Tour, *Nature (London)* **458**, 872 (2009).

²J. Cai, P. Ruffieux, R. Jafaar, M. Bieri, T. Braun, S. Blankenburg, M. Muoth, A. P. Seitsonen, M. Saleh, X. Feng *et al.*, *Nature (London)* **466**, 470 (2010).

³N. Wei, L. Xu, H.-Q. Wang, and J.-C. Zheng, *Nanotechnology* **22**, 105705 (2011).

⁴X. Jia, M. Hofmann, V. Meunier, B. G. Sumpter, J. Campos- Delgado, J. M. Romo-Herrera, H. Son, Y.-P. Hsieh, A. Reina, J. Kong *et al.*, *Science* **323**, 1701 (2009).

⁵K. Suenaga and M. Koshino, *Nature (London)* **468**, 1088 (2010).

⁶M. Acik and Y. J. Chabal, *Jpn. J. Appl. Phys.* **50**, 070101 (2011).

⁷X. Wang, Y. Ouyang, L. Jiao, H. Wang, L. Xie, J. Wu, J. Guo, and H. Dai, *Nat. Nanotechnol.* **6**, 563 (2011).

⁸X. Li, X. Wang, L. Zhang, S. Lee, and H. Dai, *Science* **319**, 1229 (2008).

⁹L. Jiao, L. Zhang, X. Wang, G. Diankov, and H. Dai, *Nature (London)* **458**, 877 (2009).

¹⁰L. Jiao, X. Wang, G. Diankov, H. Wang, and H. Dai, *Nat. Nanotechnol.* **5**, 321 (2010).

¹¹D. S. L. Abergel, V. Apalkov, J. Berashevich, K. Ziegler, and T. Chakraborty, *Adv. Phys.* **59**, 261 (2010).

¹²T. Olsen, J. Yan, J. J. Mortensen, and K. S. Thygesen, *Phys. Rev. Lett.* **107**, 156401 (2011).

¹³S. P. Koenig, N. G. Boddeti, M. L. Dunn, and J. S. Bunch, *Nat. Nanotechnol.* **6**, 543 (2011).

$^{14}$K. V. Bets and B. I. Yakobson, *Nano Res.* **2**, 161 (2009).

$^{15}$P. Koskinen, *Appl. Phys. Lett.* **99**, 13105 (2011).

$^{16}$O. O. Kit, T. Tallinen, L. Mahadevan, J. Timonen, and P. Koskinen, *Phys. Rev. B* **85**, 085428 (2012).

$^{17}$M. Poetchke, C. G. Rocha, L. E. F. Foa Torres, S. Roche, and G. Cuniberti, *Phys. Rev. B* **81**, 193404 (2010).

$^{18}$J. Wang, Z. Liu, and Z. Liu, *AIP Advances* **2**, 012103 (2012).

$^{19}$R. J. Young, L. Gong, I. A. Kinloch, I. Riaz, R. Jalil, and K. S. Novoselov, *ACS Nano* **5**, 3079 (2011).

$^{20}$Short means that the ribbon's length is of the same order of magnitude as its width.

$^{21}$F. Bonelli, N. Manini, E. Cadelano, and L. Colombo, *Eur. Phys. J. B* **70**, 449 (2009).

$^{22}$Z. Lu and M. L. Dunn, *J. Appl. Phys.* **107**, 044301 (2010).

$^{23}$C. Lee, Q. Li, W. Kalb, X.-Z. Liu, H. Berger, R. W. Carpick, and J. Hone, *Science* **328**, 76 (2010).

$^{24}$S. Cahangirov, C. Ataca, M. Topsakal, H. Sahin, and S. Ciraci, *Phys. Rev. Lett.* **108**, 126103 (2012).

$^{25}$If the long ribbon is pinned to the substrate at points with a distance *larger* than the ribbon's equilibrium length, the lowest-energy deformation will have uniaxial stretching; if the long ribbon is pinned to the substrate at points with a distance *smaller* than the ribbon's equilibrium length, the lowest-energy deformation will have pure bending.

$^{26}$D. Porezag, T. Frauenheim, T. Köhler, G. Seifert, and R. Kaschner, *Phys. Rev. B* **51**, 12947 (1995).

$^{27}$P. Koskinen and V. Mäkinen, *Comput. Mater. Sci.* **47**, 237 (2009).

$^{28}$P. Koskinen and O. O. Kit, *Phys. Rev. Lett.* **105**, 106401 (2010).

$^{29}$T. Dumitrica and R. D. James, *J. Mech. Phys. Solids* **55**, 2206 (2007).

$^{30}$O. O. Kit, L. Pastewka, and P. Koskinen, *Phys. Rev. B* **84**, 155431 (2011).

$^{31}$P. Koskinen, *Phys. Rev. B* **82**, 193409 (2010).

$^{32}$S. Malola, H. Häkkinen, and P. Koskinen, *Phys. Rev. B* **78**, 153409 (2008).

$^{33}$Y.-W. Son, M. L. Cohen, and S. G. Louie, *Phys. Rev. Lett.* **97**, 216803 (2006).

$^{34}$K. Kudin, G. Scuseria, and B. Yakobson, *Phys. Rev. B* **64**, 235406 (2001).

$^{35}$L. D. Landau and E. M. Lifshitz, *Theory of elasticity*, 3rd ed. (Pergamon, New York, 1986).

$^{36}$R. Miwa, T. M. Schmidt, W. L. Scopel, and A. Fazzio, *Appl. Phys. Lett.* **99**, 163108 (2011).

$^{37}$V. Barone, O. Hod, and G. E. Scuseria, *Nano Lett.* **6**, 2748 (2006).

$^{38}$O. Hod and G. E. Scuseria, *Nano Lett.* **9**, 2619 (2009).

$^{39}$D. Gunlycke, J. Li, J. W. Mintmire, and C. T. White, *Nano Lett.* **10**, 3638 (2010).

$^{40}$D.-B. Zhang and T. Dumitrică, *Small* **7**, 1023 (2011).

$^{41}$K. Nakada, M. Fujita, G. Dresselhaus, and M. S. Dresselhaus, *Phys. Rev. B* **54**, 17954 (1996).

$^{42}$L. Sun, Q. Li, H. Ren, H. Su, Q. W. Shi, and J. Yang, *J. Chem. Phys.* **129**, 074704 (2008).

$^{43}$M. Y. Han, J. C. Brant, and P. Kim, *Phys. Rev. Lett.* **104**, 056801 (2010).

$^{44}$J. Kunstmann, C. Özdogan, A. Quandt, and H. Feshke, *Phys. Rev. B* **83**, 045414 (2011).