# Silicon Carbide Growth: C/Si Ratio Evaluation and Modeling

Michel Pons$^{1,a}$, Shin-Ichi Nishizawa$^{2,b}$, Peter Wellmann$^{3,c}$, E. Blanquet$^{1}$,
D. Chaussende$^{1}$, J.M. Dedulle$^{1}$ and R. Madar$^{1}$

$^{1}$ INPGrenoble-CNRS (SIMAP, LMGP), Domaine Universitaire, BP 75, 38402 Saint Martin
d'Hères, France.
$^{2}$ National Institute of Advanced Industrial Science and Technology (AIST), Central 2, 1-1-1
Umezono, Tsukuba, Ibaraki 305-8568, Japan
$^{3}$ Materials Department 6, University of Erlangen, Martensstr. 7, 91058 Erlangen, Germany.

$^{a}$ michel.pons@inpg.fr, $^{b}$ s.nishizawa@aist.go.jp, $^{c}$ peter.wellmann@ww.uni-erlangen.de

**Keywords:** Modeling, Simulation, Mass transport, Growth, C/Si ratio

**Abstract.** Modeling and simulation of the SiC growth processes, Physical Vapor Transport (PVT),
Chemical Vapor Deposition (CVD), are sufficiently mature to help building new process equipment
or up-scaling old ones. It is possible (i) to simulate accurately temperature and deposition
distributions, as well as doping (ii) to quantify the limiting phenomena, (iii) to understand the
important role of different precursors in CVD and hydrogen additions in PVT. The first conclusion
of this paper is the importance of the "effective" C/Si ratio during CVD epitaxy in hot-wall reactors
and its capability to explain the doping concentrations. The second conclusion is the influence of
the C/Si ratio in alternative bulk growth technique involving gas additions.

## Introduction

Nowadays, gas-solid chemical reactions are most commonly used for the growth of bulk silicon
carbide single crystals and epitaxial layers. One important challenge is the control of residual and
intentional doping. One way to change it is the control of the effective C/Si ratio. In the mid-1990s,
the site-competition theory proposed by Larkin [1] described the dependence of the doping atom
incorporation with the ratio of available silicon and carbon atoms (C/Si ratio) in the gas phase. The
site-competition epitaxy working model is based on the competition between the SiC and dopant
source gases for the available substitutional lattice sites on the growing SiC crystal surface. Dopant
incorporation is controlled by appropriately adjusting the C/Si ratio within the growth reactor to
affect the amount of dopant atoms incorporated into these sites. Specifically, Larkin's model is
based on the principle of competition between nitrogen and carbon for the C sites and between
aluminum and silicon for the Si sites during the growth of the epilayer. In summary, the nitrogen
donor concentration in the grown epilayer is inversely proportional to the C/Si ratio during epilayer
growth, whereas the aluminum acceptor concentration is proportional to the C/Si ratio.

This paper will address two issues on modeling and simulation. The first one is the study of
doping phenomena in hot-wall CVD reactor used for epitaxial growth at low growth rate (3-10
$\mu$m/h), around 1900 K using silane and propane diluted in H₂. The objective is to calculate the
effective C/Si ratio near the deposition area and to relate it to doping concentrations. The second
one is to quantify the recent trends observed on modified-PVT techniques like the influence of H₂
on C/Si ratio [2], the influence of an additional pipe to control P-doping [3], the continuous fed of
source material by HTCVD and the role of H₂ and/or chlorinated precursors [4-5]. The effects of
chlorine additions or of chlorinated precursors which recently emerged [6-8] and the subsequent
change in C/Si ratio will be briefly discussed from a thermodynamic and kinetic point of view.

For PVT and CVD, the STR Company (http://www.semitech.us) is now offering a software tool
designed as an easy-to-learn and user-friendly computer simulator. Another widely used software
package is CFD-ACE (http://www.cfdrc.com) which was used in the present work and combined
with kinetic and thermodynamic databases.

## CVD Growth and doping

Growth modeling. There are a lot of experimental results on epitaxial growth carried out in horizontal hot-wall reactors using $\text{SiH}_4$ and $\text{C}_3\text{H}_8$ diluted in $\text{H}_2$ at around $1600\ ^\circ\text{C}$ and 100 mbar [see for example 9-12]. The general trends of the published doping results reveal their complex dependence on experimental conditions and reactor design. Particularly, the discussion of the results based on inlet conditions such as the C/Si ratio and not the actual conditions on the growing epilayer surface is leading to confusion. Modeling and simulation of the growth rate and thickness uniformity is now mature and based on efficient thermodynamic and kinetic databases [13-18]. However, doping modeling is not mature yet [17-19].

![](./images/811867700916649985_1.jpg)

Fig. 1. Influence of source gas flow rate on calculated surface data (P = 250mbar, $\text{H}_2$=40sLm, and inlet C/Si ratio constant)

For the reactor already described in [17], the effect of silane flow rate on the growth rate for different inlet C/Si ratio is shown Fig. 1. When the silane gas flow rate increases, the growth rate also increases. The surface C- and Si-molar fractions increase with increasing the silane gas flow rate. However, the evolutions of C- and Si-molar fraction are different. Then, the surface conditions such as surface C- and Si-molar fractions and their ratio change even though the inlet C/Si ratio is kept constant. It can be concluded that, for conditions leading to the same growth rate, the C/Si ratio on the surface can be different and the expected surface morphology would be different. When the C/Si ratio at the inlet is equal to 1.5, the surface C/Si ratio increases with an increase of the silane flow rate. Then, the carbon in excess might lead to an increase of surface roughness. On the other hand, when the C/Si ratio at the inlet is 0.5, the surface C/Si ratio decreases and a smooth surface is expected.

Doping modeling. Kojima et al. [9] investigated the doping incorporation features on both the Si-terminated surface and the C-terminated surfaces. In their experiments, in order to change the C/Si ratio at the inlet, the $\text{SiH}_4$ flow rate was fixed and the $\text{C}_3\text{H}_8$ flow rate was varied. They concluded that for N doping, an increase of the $\text{C}_3\text{H}_8$ flow rate, i.e. an increase of the C/Si ratio, leads to a doping concentration decrease. This is the result of site competition epitaxy previously described. If nitrogen replaces carbon, increasing the amount of carbon, while keeping the nitrogen amount constant leads to a decrease of the replacement ratio. They also showed that, for Al doping, an increase of the $\text{C}_3\text{H}_8$ flow rate leads to an increase of dopant incorporation.

Fig. 2 shows the relationship between the calculated surface molar fraction of carbon and silicon at the center of the wafer and the experimental values of nitrogen and aluminum doping concentrations. When the molar fractions of carbon and silicon increase, nitrogen and aluminum doping concentrations decrease. The silicon amount at the surface changes with $\text{C}_3\text{H}_8$ flow rate even though the inlet $\text{SiH}_4$ flow rate is constant. The incorporation of both nitrogen and aluminum could be explained by the site competition model while taking into account the molar fractions of surface carbon and silicon. Fig. 2a shows that the nitrogen concentration on a C-terminated surface is higher than that on a Si-terminated surface. Nitrogen can easier replace the surface carbon in the first layer on the C-terminated surface than replacing the second layer of C-atoms during growth on Si-terminated surface. The evolutions of unintentional (residual) and intentional doping are homothetic. This means that the assumption that N concentration depends on $\text{N}_2$ flow rate and not on $\text{C}_3\text{H}_8$ and $\text{SiH}_4$ flow rate is validated. On the other hand, Fig. 2b shows that the aluminum concentration on Si-terminated surface is higher than that on C-terminated surface. Aluminum can easier replace surface silicon on the Si-terminated surface than replacing the second layer of Si-

atoms during growth on the C-terminated surface. However, the molar fraction evolution on the Si-terminated surface and C-terminated surface are different. This suggests that the doping mechanisms on Si- and C-terminated surface, and of nitrogen and aluminum, are different [19-20].

![](./images/811867700916649985_2.jpg)

Fig. 2. Relation between calculated surface condition and doping concentration in experiments (P=250mbar, $SiH_4$=6.67sccm, $C_3H_8$ flow rate was varied, $H_2$=40sLm.)
(a) Nitrogen doping( N=0 and 1sccm for unintentional and intentional doping, respectively.)
(b) Aluminum doping (TMA=0.1sccm in experiments)

### Alternative bulk growth techniques

SiC bulk crystals for wafer fabrication in the 2" to 4" range are mainly grown by the seeded sublimation technique (often referred to as PVT) at elevated temperatures > 2300K [21-23, 25]. It has been shown that, for certain applications, the growth process can be significantly improved by the implementation of CVD components. In the case of the high temperature chemical vapor deposition (HTCVD) technique [24] the SiC source material in the PVT reactor (usually SiC powder) is completely replaced by injection of Si- and C-containing precursor gases, like in regular CVD described above. A strength of HTCVD is the preparation of high purity SiC crystals. Similar to HTCVD, a well-established technique is Halide CVD [4]. Closer related to the conventional PVT are (i) the so called Modified-PVT (M-PVT) [6] which uses an additional gas pipe for controlled doping or tuning of the C/Si ratio in the gas phase and (ii) the so called Continuous Feed - Physical Vapor Transport (CF-PVT) [7-8] for the growth of large boules of high purity.

Modified PVT Technique. During conventional PVT, crystal growth of SiC process control is performed by setting of growth temperature (heating power), temperature gradient (furnace design) and inert gas pressure. The gas phase composition, and in particular the C/Si ratio, can be only tuned indirectly through the temperature field and crucible materials used. In the Modified-PVT technique an additional gas pipe is used for tuning of the gas phase composition [6]. Besides p-type doping using aluminum vapor, the control of the C/Si ratio is of particular interest.

A direct way to change the C/Si composition in the growth cell, for example, would be the feeding of gases like propane ($C_3H_8$) and silane ($SiH_4$). The cold gases, however, have to pass through a pipe zone at around $1000^\circ C$....$1500^\circ C$ when being injected into the hot  (T>$2000^\circ C$) growth cell. Parasitic deposition in the feeding pipe due to gas decomposition and formation of graphite in the case of propane [26] and SiC in the case of silane, respectively, may lead to pipe blocking. Another possibility to tune the gas phase composition would be the addition of hydrogen

(feeding of $H_2$) or chlorine (feeding of HCl) which shift the equilibrium species distribution of the subliming SiC powder inside the graphite crucible.

We have calculated the C/Si ratio for the addition of the elements hydrogen and chlorine to the typical PVT Si-C-Ar system through thermodynamic calculations using the Factsage software (www.factsage.com) and our optimized thermodynamic database [27]. To account for interference with dilution effects we have carried out a comparison between the reaction of solid <SiC> +Ar, solid <SiC> + H, solid <SiC> + Cl, all at constant pressure (4 and 25 mbar) and temperatures varying from 1900 to $2500^\circ C$. The major gaseous species in the Si-C-Ar system from non-congruent sublimation of <SiC> are $Si_2C$, $SiC_2$ and Si, respectively. Replacing argon by hydrogen or chlorine, the major gas species are $Si_2C$, $SiC_2$, Si, $C_2H_2$ and SiH or $SiCl_2$, SiCl, Si, $Si_2C$, $SiC_2$, respectively. The resulting C/Si ratio as a function of temperature has been plotted in Fig. 3. The C/Si ratio is always smaller than 1. While hydrogen tends to increase the the C/Si ratio, compared to inert gas argon, the addition of chlorine (Cl) leads to a more Si-rich gas phase due to the presence of very stable $SiCl_x$ species (Fig. 3a, pressure 4mbar). Comparing two system pressures in Fig. 3b shows that a higher C/Si ratio can be reached at the higher pressure (constant temperature of $2000^\circ C$). The calculations carried out here, of course, may only give a qualitative picture of the real conditions in the PVT reactor. Nevertheless, they are important guidelines for experiments currently carried out.

![](./images/811867700916649985_3.jpg)

Fig. 3. (a) C/Si ratio in the gas phase vs. temperature for the sublimation of solid <SiC> in Ar, H and Cl atmospheres (b) influence of $H_2$ dilution on the C/Si ratio at $2000\ ^\circ C$.

CF-PVT Technique. The experimental set-up is a modified sublimation reactor, with inductive heating and a water-cooled quartz tube [4]. The crucible is totally made of graphite and thermally insulated with graphite felts. It is composed of three main graphite pieces: the heating element, the sublimation chamber and the CVD chamber, which delimitate the three "reaction zones" (fig. 4a), the feeding zone (CVD),the transfer zone and the sublimation (PVT) zone .

All the TMS reacts in the CVD chamber and in the transfer zone (Fig. 4b). Its decomposition provides a high quantity of hydrogen which fills up the whole PVT area. Consequently, as far as the CVD precursor contains hydrogen atoms, the chemical system considered in the PVT zone contains hydrogen as well. Moreover, the formation of hydrocarbons from the precursor cracking in the CVD zone should contribute to an enrichment of C containing species in the PVT zone.

The building materials are the same as in a classical PVT system. The nitrogen concentration measured by SIMS and low temperature photoluminescence is very low, $2\ 10^{16}$, compared to that obtained in classical PVT systems working with the same Ar grade. This is due to $H_2$ and C-containing species coming from the decomposition of the precursor. The calculated C/Si ratio is five times higher than the C/Si ratio at the same temperature and without hydrogen. Al and B contents are lower than $10^{15}$. The material is not compensated and its resistivity is around 300 $\Omega$.cm. In this setup, it is possible to adjust the C/Si ratio by taking into account the decomposition of MTS and by modifying the $H_2$/Ar ratio of the carrier gas. But, as in the M-PVT system, it is necessary to be very careful on the temperature change coming from carrier gas composition.

![](./images/811867700916649985_4.jpg)

Fig. 4. (a). CF-PVT crucible set-up,(b). Mass fractions of $H_2$ and TMS

## Conclusions
The transport model developed for CVD epitaxy at 1600 °C was validated by a great number of experiments. It shows that the site competition model can explain the doping features while taking into account the concentrations of surface silicon and carbon, i.e, the actual C/Si ratio. The development of alternative bulk growth techniques which combines the state of the art PVT technique for bulk SiC crystal growth and CVD for feeding and doping allow a fine tuning of growth parameters. A precise control of the actual C/Si ratio over the substrate is only possible by a complete modeling and simulation of the growth apparatus. A that time, there is no enough experimental data like in CVD epitaxy, to be able to give a complete description of the transport phenomena responsible for doping changes. However, simplified transport modeling combined with thermodynamic calculations in different chemical systems and reactor concepts suggest the main trends to change the C/Si ratio and better control the doping concentration. It is clear that $H_2$ addition can lead to congruent sublimation of SiC (C/Si = 1) at high pressures (> 20 torr).The alternative bulk growth techniques, M-PVT and CF-PVT, have a great potential for the adjustment of residual doping and intentional doping as well.

## References
[1] D.J. Larkin: Phys. Stat. Sol.(b) 202 (1997), p. 305
[2] M. A. Fanton, Q. Li, A. Y. Polyakov, M. Skowronski, R. Cavalero, and R. Ray: J.Cryst. Growth 339-343 (2006), p. 339
[3] T. L. Straubinger, M. Bickermann, R. Weingartner, P. J. Wellmann, and A. Winnacker: J.Cryst. Growth 240 (2002), p. 117
[4] D. Chaussende, F. Baillet, L. Charpentier, E. Pernot, M. Pons, and R. Madar: J. Electrochem. Soc. 150 (2003), p. G653
[5] D. Chaussende, M. Ucar, L. Auvray, F. Baillet, M. Pons, and R. Madar: Crystal Growth & Design 5 (2005), p. 1539
[6] A. Fiorucci, D. Moscatelli and M. Masi, Surf. Coat. Tech., 201 (2007) 8825
[7] S. Nigam, H.J. Chung, A.Y. Polyakov, M.A. Fanton, B.E. Weiland, D.W. Snyder and M. Skowronski: J. Crystal Growth 284 (2005), p. 112.
[8] H. Pedersen, S. Leone, A. Henry, V. Darakchieva and E. Janzen: Surf. Coat.Tech. 201 (2007) 8931.

[9] K.Kojima, T.Suzuki, S.Kuroda, J.Nishio and K.Arai: Jpn.J.Appl.Phys. 42 (2003), p. L637

[10] T.Kimoto, A.Itoh and H.Matsunami: Appl.Phys.Lett. 67 (1995), p. 2385; H. Fujiwara, K. Danno, T. Kimoto, T. Tojo, H. Matsunami: J. Crystal Growth 281 (2005) p. 370

[11] U.Forsberg, Ö.Danielsson, A.Henry, M.K.Linnarsson and E.Janzen: J. Cryst. Growth 253 (2003), p. 340

[12] A.Schöner, in: Silicon Carbide, ed. by W.J.Choyke, H.Matsunami and G.Pensl, Springer (2003), p. 229

[13] P.M.Löfgren, W.Ji, C.Hallin and C.Y.Gu: J.Electrochem.Soc. 164 (2000), p. 147

[14] A.N.Vorobe'v, S.Yu Karpov, M.V.Bogdanov, A.E.Komissarov, O.V.Bord, A.I.Zhmakin and Yu N.Makarov: Comp.Mat.Sci. 520 (2002), p. 24

[15] Ö.Danielsson, A.Henry and E.Janzen: J.Crystal Growth 243 (2002), p. 170

[16] Ö.Danielsson, U.Forsberg and E.Janzen: J.Crystal Growth 250 (2003), p. 471

[17] J.Meziere, M.Ucar, E.Blanquet, M.Pons, P.Ferret and L.Di Cioccio: J. Cryst. Growth 267 (2004), p.436

[18] S.Nishizawa, K.Kojima, S.Kuroda, K.Arai and M.Pons: J.Cryst. Growth 275 (2005), p.e515

[19] S.Nishizawa and M.Pons: Microelectric Eng. 83 (2006), p.100

[20] S.Nishizawa and M.Pons: Mater.Sci.Forum: 483-485 (2005), p.53

[21] S. G. Muller, R. C. Glass, H. M. Hobgood, V. F. Tsvetkov, M. Brady, D. Henshall, D. Malta, R. Singh, J. Palmour, and C. H. Carter: Mat. Sci. Eng. B80 (2001), p.327

[22] N. Ohtani, T. Fujimoto, M. Katsuno, T. Aigo, and H. Yashiro: J.Cryst. Growth 237-239 (2002), p.1180

[23] D. Hofmann, M. Bickermann, R. Eckstein, M. Kolbl, S. G. Muller, E. Schmitt, A. Weber, and A. Winnacker: J.Cryst. Growth 198/199 (1999), p.1005

[24] A. Ellison, B. Magnusson, N. T. Son, L. Storasta and E. Janzen, Mater.Sci.Forum 433-436 (2003), p.33

[25] S.Nishizawa, T. Kato, Y. Kitou, N. Oyanagi, F. Hirose, H. Yamaguchi, W. Bahng, and K. Arai: Mater.Sci.Forum 457-460(2004), p.29

[26] Wellmann, P., P. Desperrier, R. Mueller, T. Straubinger, A. Winnacker, F. Baillet, E. Blanquet, J.M. Dedulle and M. Pons: J.Cryst.Growth 275 (2005), p. e555

[27] D. Chaussende, E. Blanquet, F. Baillet, M. Ucar and G. Chichignoud: Chem. Vap. Dep. 12 (2006), p 541

Silicon Carbide and Related Materials 2007
10.4028/www.scientific.net/MSF.600-603

Silicon Carbide Growth:C/Si Ratio Evaluation and Modeling
10.4028/www.scientific.net/MSF.600-603.83

DOI References

[1] D.J. Larkin: Phys. Stat. Sol.(b) 202 (1997), p. 305
doi:10.1002/1521-3951(199707)202:1<305::AID-PSSB305>3.0.CO;2-9

[2] M. A. Fanton, Q. Li, A. Y. Polyakov, M. Skowronski, R. Cavalero, and R. Ray: J.Cryst. rowth 339-343 (2006), p. 339
doi:10.1016/j.jcrysgro.2005.11.022

[3] T. L. Straubinger, M. Bickermann, R. Weingartner, P. J. Wellmann, and A. Winnacker: .Cryst. Growth 240 (2002), p. 117
doi:10.1016/S0921-5107(01)00976-X

[4] D. Chaussende, F. Baillet, L. Charpentier, E. Pernot, M. Pons, and R. Madar: J. lectrochem. Soc. 150 (2003), p. G653
doi:10.1149/1.1606689

[5] D. Chaussende, M. Ucar, L. Auvray, F. Baillet, M. Pons, and R. Madar: Crystal Growth & esign 5 (2005), p. 1539
doi:10.1021/cg050009i

[6] A. Fiorucci, D. Moscatelli and M. Masi, Surf. Coat. Tech., 201 (2007) 8825
doi:10.1016/j.surfcoat.2007.04.110

[7] S. Nigam, H.J. Chung, A.Y. Polyakov, M.A. Fanton, B.E. Weiland, D.W. Snyder and M. kowronski: J. Crystal Growth 284 (2005), p. 112.
doi:10.1016/j.jcrysgro.2005.06.027

[10] T.Kimoto, A.Itoh and H.Matsunami: Appl.Phys.Lett. 67 (1995), p. 2385; H. Fujiwara, K. anno, T. Kimoto, T. Tojo, H. Matsunami: J. Crystal Growth 281 (2005) p. 370
doi:10.1016/j.jcrysgro.2005.03.093

[22] N. Ohtani, T. Fujimoto, M. Katsuno, T. Aigo, and H. Yashiro: J.Cryst. Growth 237-239 2002), p.1180
doi:10.4028/www.scientific.net/MSF.389-393.55

[24] A. Ellison, B. Magnusson, N. T. Son, L. Storasta and E. Janzen, Mater.Sci.Forum 433-436 2003), p.33
doi:10.4028/www.scientific.net/MSF.433-436.33

[26] Wellmann, P., P. Desperrier, R. Mueller, T. Straubinger, A. Winnacker, F. Baillet, E. lanquet, J.M. Dedulle and M. Pons: J.Cryst.Growth 275 (2005), p. e555
doi:10.1016/j.jcrysgro.2004.11.070

[27] D. Chaussende, E. Blanquet, F. Baillet, M. Ucar and G. Chichignoud: Chem. Vap. Dep. 12 2006), p 541
doi:10.1002/cvde.200606471

[22] N. Ohtani, T. Fujimoto, M. Katsuno, T. Aigo, and H. Yashiro: J.Cryst. Growth 237-239 (2002), p.1180
doi:10.4028/www.scientific.net/MSF.389-393.55

[24] A. Ellison, B. Magnusson, N. T. Son, L. Storasta and E. Janzen, Mater.Sci.Forum 433-436 (2003), p.33
doi:10.4028/www.scientific.net/MSF.433-436.33

[26] Wellmann, P., P. Desperrier, R. Mueller, T. Straubinger, A. Winnacker, F. Baillet, E. Blanquet, J.M. Dedulle and M. Pons: J.Cryst.Growth 275 (2005), p. e555
doi:10.1016/j.jcrysgro.2004.11.070

[27] D. Chaussende, E. Blanquet, F. Baillet, M. Ucar and G. Chichignoud: Chem. Vap. Dep. 12 (2006), p 541
[ 9] [ 10]

doi:10.1002/cvde.200606471