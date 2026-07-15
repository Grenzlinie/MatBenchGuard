# Deep levels in cesium lead bromide from native defects and hydrogen†
Michael W. Swift *a and John L. Lyons *b

Lead halide perovskites such as $CsPbBr_3$ have achieved widespread attention as optoelectronic materials, due in large part to their good performance despite significant defect densities. This "defect tolerance" has often been explained by hypothesizing that there is negli- gible trap-assisted non-radiative recombination in these materials because none of the dominant defects give rise to deep levels in the gap. We refer to this as the "shallow defect hypothesis". In this work, we reject the shallow defect hypothesis for $CsPbBr_3$. Via a thorough first-principles inventory of native defects and hydrogen impurities, we show that a number of relevant defects do in fact have deep levels, most notably the bromine interstitial and hydrogen interstitial. This adds to a growing body of evidence against the shallow defect hypothesis, suggesting that the observed defect tolerance may be due instead to relatively low recombination rates at deep levels. Guided by the theoretical identification of these defects, experiments can take steps to mitigate trap-assisted non-radiative recombination, further boosting the efficiency of lead halide perovskite optoelectronics.

Metal halide perovskites are well known as an exciting solar cell technology with rapidly growing efficiency.¹ Cesium lead bromide ($CsPbBr_3$), an all-inorganic member of this materials family, has attracted great interest as a platform for nanocrystal-based LEDs and single-photon emitters²⁻⁷ with remarkable excitonic properties.⁸⁻¹¹ $CsPbBr_3$ has also been used in nonvolatile memory¹² in addition to its photovoltaic applications.¹³

Like other metal halide perovskites, $CsPbBr_3$ exhibits excel- lent performance despite significant defect densities.³⁻⁵,⁷,¹⁴⁻¹⁶ This "defect tolerance" has sometimes been explained by claiming that all energetically favorable intrinsic defects are shallow.³⁻⁵,¹⁴,¹⁷ We will call this the "Shallow Defect Hypothesis" (SDH) in the remainder of this work. The SDH would indeed eliminate trap-assisted non-radiative recombination (also known as Shockley-Read-Hall recombination) as an important loss mechanism, since it occurs most efficiently at defect levels deep in the band gap. Confusingly, the hypothesis itself has sometimes been called "defect tolerance", despite the fact that there are many other possible explanations for this phenomenon.

The SDH remains controversial. There is experimental evidence of deep defect levels in organic⁷,¹⁶,¹⁸⁻²² and inorganic¹⁵,²³⁻²⁵ metal halide perovskites. Many alternative explanations for defect tolerance have been proposed that do not invoke the SDH, including polaronic effects,²⁶⁻²⁹ polar fluctuations,³⁰ and interactions with low-frequency lattice phonons.²⁷,³¹,³² A number of theoretical papers have identified deep defect levels in methylammonium lead iodide (MAPI)³³⁻³⁷ and $CsPbI_3$.³⁸,³⁹ If true, the SDH would lead to a bleak picture for future improvements in efficiency. Other loss mechanisms (such as Auger recombination) are determined by the fundamental electronic structure of the material, and would be difficult to address. By contrast, the strategy for reducing trap- assisted recombination is straightforward: namely, by identifying the detrimental defects and taking steps during synthesis to eliminate their presence. In fact, there are a number of experimental reports that taking steps to reduce defect densities does in fact improve efficiency,⁷,¹³,¹⁸,²⁰,²²⁻²⁴ suggesting that deep defects are in fact commonly present in as-grown material.

A theoretical investigation of defects in $CsPbBr_3$ can thus prove valuable by scrutinizing the SDH in this material. Previous computational studies on defects in $CsPbBr_3$ (ref. 9, 17, 40-43) broke important ground, but fall short of rigorously addressing the SDH. Some of the previous works did not calculate charge state transition levels.⁴⁰,⁴¹ Others use semilocal functionals or do not include spin-orbit coupling (SOC).⁹,⁴²,⁴³ However, as shown in ref. 34 and 36 for MAPI, the positions of the band edges, the formation energies of charged defects, and the positions of charge transition levels are not correctly

---
ªASEE Postdoctoral Fellow Resident at Center for Computational Materials Science, US Naval Research Laboratory, Washington, DC 20375, USA. E-mail: michael.swift.ctr@nrl.navy.mil
ᵇCenter for Computational Materials Science, US Naval Research Laboratory, Washington, DC 20375, USA. E-mail: john.lyons@nrl.navy.mil
† Electronic supplementary information (ESI) available: Complete defect formation energy results and more methodological information.³⁴,³⁶,³⁸,⁴⁵,⁴⁶,⁴⁹,⁵³,⁵⁹⁻⁶⁷ See DOI: 10.1039/d0ta11742k

captured unless advanced functionals and SOC are included in all calculations. The studies that do not meet this criteria are therefore unreliable when assessing the SDH. Another important consideration is the inclusion of all relevant defect charge states. Previous theoretical studies of bromine interstitials in $CsPbBr_3$ did not consider $Br_i^+$,¹⁷,⁴⁰ likely because positively charged halogen ions are typically rare and highly reactive. However, positive iodine interstitials have been shown to be important in MAPI, where they form a trimer with two lattice halide ions.³³⁻³⁵,³⁷,⁴⁴ The omission of $Br_i^+$ may be highly consequential, as ref. 37 showed that the $(-/+)$ transition of $I_i$ is an important source of non-radiative recombination. Antisites have also suffered from an incomplete consideration of relevant charge states; deep antisite levels have been identified but dismissed as irrelevant based on the formation energies of the neutral antisites.¹⁷ However, charged antisites can be significantly lower in energy depending on conditions. These issues motivate us to revisit native defects in orthorhombic $CsPbBr_3$ using SOC and the HSE hybrid functional⁴⁵ (with 35% mixing and $0.1\ \mathring{A}^{-1}$ screening to reproduce the experimental band gap of 2.3 eV (ref. 46)), paying close attention to all relevant charge states and transition levels of native defects over a range of chemical potential conditions.

Impurities in $CsPbBr_3$ must also be taken into account. For instance, it is well established that hydrogen is an important impurity in traditional semiconductors⁴⁷⁻⁴⁹ with some level of unintentional incorporation almost unavoidable.⁴⁷,⁵⁰ Hydrogen is abundant in the growth precursors for halide perovskites, raising the possibility of unintentional hydrogen incorporation in these materials as well. We therefore include hydrogen impurities in our investigation. While previous work has investigated proton diffusion in MAPI,⁵¹,⁵² to our knowledge this is the first systematic first-principles study of hydrogen in inorganic halide perovskites, and the first to consider hydrogen transition levels and hydrogen complexes in any halide perovskite.

The concentrations and transition levels of point defects can be determined by defect formation energies $E^f$. For defect X with charge $q$, $E^f[\text{X}^q]$ is given by a well-established formalism⁵³

$$
E^f[\text{X}^q] = E[\text{X}^q] - E[\text{bulk}] - \sum_i n_i\mu_i + qE_\text{F} + \Delta^q, \tag{1}
$$

where $E[\text{X}^q]$ is the DFT total energy of a supercell containing the defect X in charge state $q$, $E[\text{bulk}]$ is the DFT total energy of a pristine supercell, $n_i$ is the number of atoms of species $i$ added ($n_i > 0$) or removed ($n_i < 0$) to form the defect, and $\mu_i$ is the chemical potential of species $i$ (see Section S.I and Fig. S.1 in the ESI†). $E_\text{F}$ is the Fermi level, typically referenced to the valence-band maximum (VBM). $\Delta^q$ is a correction for finite-size effects.⁵⁴,⁵⁵ Note that this is a purely static defect model. While it has been suggested that dynamical effects may influence defect levels,³¹,³²,⁴¹ these effects are beyond the scope of the present work.

Defect formation energies for all self-interstitials, antisites, vacancies, and hydrogen impurities are plotted as a function of Fermi level in the ESI, Fig. S.2 and S.3.† These figures contain a great deal of information and can be difficult to interpret. We will first discuss the data as a whole, then go on to highlight some important details. Our first approach is to identify the convex hull of the defect formation energies, *i.e.*, the set of all defects which are the lowest-energy defect at some Fermi level. Fig. 1 shows this “defect hull” for Pb-rich and Br-rich chemical potentials, representing the limiting cases for growth conditions. If hydrogen impurities are present, they may contribute to the hull as well; these defect lines are shown in Fig. 1 together with the native defects. The defect hull not only shows the most abundant defects, but also gives an idea of the equilibrium Fermi level for the given chemical potential conditions. The Fermi level is set by charge neutrality, *i.e.*, the point at which the concentrations of positive and negative defects together with any free carriers balance. Since defect concentrations follow a Boltzmann distribution, the charge-neutrality Fermi level is well approximated as the point at which the lowest-energy positive and negative defect formation energy lines cross in the defect hull. We can compare this approximation to the result of solving for the Fermi-level position at charge-neutrality ($E_\text{F}^0$) based on all calculated defects and free carriers. We find that $E_\text{F}^0 = 1.66$ eV in Pb-rich conditions and 0.37 eV in Br-rich conditions. In each case, this is in good agreement with the approximation based on the defect hull.

Another synthesis of the results may be found by focusing on thermodynamic charge-state transition levels, or “defect levels”. Defect levels are values of $E_\text{F}$ at which the formation energies of different charge states of a given defect are equal, and appear as kinks in plots of $E^f$ *vs.* $E_\text{F}$ (*e.g.*, Fig. 1). A defect is considered shallow if it does not have any defect levels in the gap. From

![](./images/812490673319051265_1.jpg)

Fig. 1 Defect formation energies ($E^f$) versus Fermi level ($E_\text{F}$) for defects that make up the “defect hull” at Pb-rich ($\mu_\text{Br} = -1.56$ eV, $\mu_\text{Pb} = 0.00$ eV, $\mu_\text{Cs} = -2.49$ eV) and Br-rich ($\mu_\text{Br} = 0.00$ eV, $\mu_\text{Pb} = -2.93$ eV, $\mu_\text{Cs} = -4.24$ eV) conditions. Defects are shown if they contribute to the hull either when considering only native defects or when considering native defects and hydrogen impurities.

eqn (1) it is apparent that the transition level (referenced to the VBM) between charge states $q$ and $q'$ is given by

$$
\varepsilon(q/q') = \frac{E^\mathrm{f}[q; E_\mathrm{F}=0] - E^\mathrm{f}[q'; E_\mathrm{F}=0]}{q' - q}. \tag{2}
$$

Note that $\varepsilon(q/q')$ does not depend on chemical potential conditions. Transition levels of the defects with levels in the gap are shown in Fig. 2.

Under Pb-rich conditions, the Fermi level is relatively high ($E_\mathrm{F}^0 = 1.66$ eV at 300 K based on all calculated defects), though the low formation energy of $V_\mathrm{Pb}^{2-}$ at the CBM suggests that pushing the Fermi level higher to achieve $n$-type doping will be difficult. $V_\mathrm{Br}$, $V_\mathrm{Pb}$, and $V_\mathrm{Cs}$ are the most abundant native defects. $V_\mathrm{Br}$ is shallow, and $V_\mathrm{Pb}$ has a transition level at $\varepsilon(2-/2+) = 0.10$ eV, relatively close to the VBM. $V_\mathrm{Br}^+$ and $V_\mathrm{Pb}^{2-}$ form a complex with charge 1$-$ and a binding energy of 1.22 eV. All of the self-interstitials have formation energies close to 1.25 eV, though only $\mathrm{Pb}_i$ is in the hull (defects not included in Fig. 1 may be found in the ESI, Fig. S.2 and S.3$\dagger$). $\mathrm{Pb}_i$ has a deep level at $\varepsilon(0/2+) = 2.01$ eV. We note that ref. 17 suggests that growth in Br-poor (Pb-rich) conditions will lead to lower defect concentrations. By contrast, we find that charged native defects (especially vacancies) could still have non-negligible concentrations in Pb-rich conditions.

Hydrogen is likely to be important in Pb-rich conditions. At the charge neutrality Fermi level, with the chemical potential set at the solubility limit, $\mathrm{H}_\mathrm{Br}^0$ has formation energy 0.71 eV, $\mathrm{H}_i^+$ 0.87 eV, and $\mathrm{H}_\mathrm{Pb}^-$ 0.97 eV. $\mathrm{H}_i^+$ has a level $\varepsilon(-/+) = 1.80$ eV and $\mathrm{H}_\mathrm{Br}$ has a level $\varepsilon(0/+) = 0.27$ eV.

Under Br-rich conditions, the Fermi level drops to 0.37 eV at 300 K based on a charge neutrality analysis. Holes in the valence band make a significant contribution to this analysis, in agreement with experimentally observed p-type conductivity in Br-rich conditions.⁵⁶ The picture of relevant defects changes significantly compared to Pb-rich conditions. The formation energy of $\mathrm{Br}_i^-$ has dropped to 0.98 eV, making this a highly relevant deep defect at the Br-rich extreme. The consideration of $\mathrm{Br}_i^+$ proves critical, since we find that $\mathrm{Br}_i$ acts as a "negative-$U$" center with a deep level at $\varepsilon(-/+) = 0.34$ eV. The deep levels of $\mathrm{Br}_\mathrm{Pb}$ at $\varepsilon(2-/0) = 0.38$ eV and $\varepsilon(3-/2-) = 1.53$ eV may also be relevant, though $\mathrm{Br}_\mathrm{Pb}^{2-}$ still has a fairly high formation energy (1.86 eV). $\mathrm{H}_\mathrm{Pb}^-$ has become slightly more favorable at 0.89 eV. $\mathrm{H}_i^+$ is slightly less favorable at 1.14 eV, while $\mathrm{H}_\mathrm{Br}$ has become irrelevant with a formation energy close to 4 eV.

![](./images/812490673319051265_2.jpg)

Fig. 2 Thermodynamic charge state transition levels for those defects that have levels in the gap. Solid lines are transitions between stable charge states. For levels in which the charge state changes by more than 1, the single-carrier transitions (i.e., $|q' - q| = 1$) involving unstable charge states are also shown as dashed lines. These levels are relevant for carrier capture processes including trap-assisted non-radiative recombination.

Given the importance of $\mathrm{H}_i$ (especially at Pb-rich conditions) and $\mathrm{Br}_i$ (especially at Br-rich conditions), it is worth exploring the configurations of these defects. The local atomic structures near the hydrogen interstitial and bromine interstitial are shown and discussed in the ESI (Fig. S.5 and Section S.IV).$\dagger$ Our results for $\mathrm{Br}_i$ are reminiscent of $\mathrm{I}_i$ in MAPI, which has been shown to give rise to significant non-radiative recombination largely due the anharmonicity of its potential energy surface.³⁷ While a full calculation of non-radiative recombination rates is beyond the scope of this work, we find similar anharmonicity in the $\mathrm{Br}_i$ potential energy surface based on the configuration coordinate diagrams⁵⁷ shown in Fig. 3, suggesting that its capture coefficients are likely significant.

We have presented a thorough inventory of native point defects and hydrogen impurities in $\mathrm{CsPbBr}_3$ using a hybrid functional, including SOC, and considering a broad range of charge states. We determined the formation energies of all relevant charge states at varying chemical potential conditions, as well as the thermodynamic charge-state transition levels. These results definitively reject the SDH that has been proposed to explain defect tolerance in the metal halide perovskites. We find that $\mathrm{Br}_i^+$ is an abundant defect (especially in Br-rich conditions) with a $(-/+)$ transition level 0.34 eV above the VBM. The $\mathrm{Br}_\mathrm{Pb}$ antisite, though less favorable than some other defects, has deep levels at 0.38 eV and 1.53 eV and may not be negligible. We also find that $\mathrm{H}_i$ and $\mathrm{H}_\mathrm{Br}$ are important impurities that may be unintentionally introduced by hydrogen-containing precursors during growth (especially in Pb-rich conditions). Both these defects have deep levels ($\mathrm{H}_i$ at 1.80 eV and $\mathrm{H}_\mathrm{Br}$ at 0.27 eV).

![](./images/812490673319051265_3.jpg)

Fig. 3 Configuration coordinate diagram for the $\mathrm{Br}_i(0/+)$ and $\mathrm{Br}_i(-/0)$ charge state transitions, showing strong anharmonicity.

It is worth asking, if the SDH is not true, what accounts for "defect tolerance" in the lead halide perovskites? There is some evidence that non-radiative recombination rates at deep centers may be relatively modest in these materials, but when taken together with moderate defect densities, this still adds up to a significant loss mechanism. $^{7,15,37}$ This agrees with the fact that reduced defect densities have been associated with improved performance. $^{7,13,18,20,22-24}$ In this way the perovskites may be "defect tolerant" in a similar sense as gallium nitride; early devices showed good performance despite high defect densities, while later devices with optimized growth (guided in part by theory) achieved much higher efficiencies. $^{58}$

Overall, our results contribute to ongoing investigations into mechanisms behind defect tolerance. Answering the questions shrouding these remarkable materials will enable even greater efficiencies in perovskite-based single-photon emitters and optoelectronic devices.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
We thank Xie Zhang, Chris G. Van de Walle, and Sarah Brittman for helpful discussions. M. W. S. acknowledges support from the Naval Research Laboratory Postdoctoral Fellowship through the American Society for Engineering Education. J. L. L. was supported by the ONR/NRL 6.1 Base Research Program. Calculations were performed at the DoD Supercomputing Resource Center at ARL.

## References
1 Best Research-Cell Efficiency Chart, https://www.nrel.gov/pv/cell-efficiency.html, National Renewable Energy Laboratory (NREL).
2 L. Protesescu, S. Yakunin, M. I. Bodnarchuk, F. Krieg, R. Caputo, C. H. Hendon, R. X. Yang, A. Walsh and M. V. Kovalenko, *Nano Lett.*, 2015, **15**, 3692-3696.
3 D. N. Dirin, L. Protesescu, D. Trummer, I. V. Kochetygov, S. Yakunin, F. Krumeich, N. P. Stadie and M. V. Kovalenko, *Nano Lett.*, 2016, **16**, 5866-5874.
4 M. V. Kovalenko, L. Protesescu and M. I. Bodnarchuk, *Science*, 2017, **358**, 745-750.
5 H. Huang, M. I. Bodnarchuk, S. V. Kershaw, M. V. Kovalenko and A. L. Rogach, *ACS Energy Lett.*, 2017, **2**, 2071-2083.
6 X. Lao, X. Li, H. Ågren and G. Chen, *Nanomaterials*, 2019, **9**, 172.
7 Z. Fang, W. Chen, Y. Shi, J. Zhao, S. Chu, J. Zhang and Z. Xiao, *Adv. Funct. Mater.*, 2020, **30**, 1909754.
8 M. A. Becker, R. Vaxenburg, G. Nedelcu, P. C. Sercel, A. Shabaev, M. J. Mehl, J. G. Michopoulos, S. G. Lambrakos, N. Bernstein, J. L. Lyons, T. Stöferle, R. F. Mahrt, M. V. Kovalenko, D. J. Norris, G. Rainò and A. L. Efros, *Nature*, 2018, **553**, 189-193.
9 M. Sebastian, J. A. Peters, C. C. Stoumpos, J. Im, S. S. Kostina, Z. Liu, M. G. Kanatzidis, A. J. Freeman and B. W. Wessels, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2015, **92**, 1263.
10 D. Rossi, X. Liu, Y. Lee, M. Khurana, J. Puthenpurayil, K. Kim, A. V. Akimov, J. Cheon and D. H. Son, *Nano Lett.*, 2020, **20**, 7321-7326.
11 A. Liu, D. B. Almeida, L. G. Bonato, G. Nagamine, L. F. Zagonel, A. F. Nogueira, L. A. Padilha and S. T. Cundiff, 2020, arXiv:2002.08349.
12 D. Liu, Q. Lin, Z. Zang, M. Wang, P. Wangyang, X. Tang, M. Zhou and W. Hu, *ACS Appl. Mater. Interfaces*, 2017, **9**, 6171-6176.
13 J. Duan, Y. Zhao, X. Yang, Y. Wang, B. He and Q. Tang, *Adv. Energy Mater.*, 2018, **8**, 1802346.
14 M. Buchanan, *Nat. Phys.*, 2020, **16**, 996.
15 M. Bruzzi, F. Gabelloni, N. Calisi, S. Caporali and A. Vinattieri, *Nanomaterials*, 2019, **9**, 177.
16 T. Leijtens, G. E. Eperon, A. J. Barker, G. Grancini, W. Zhang, J. M. Ball, A. R. S. Kandada, H. J. Snaith and A. Petrozza, *Energy Environ. Sci.*, 2016, **9**, 3472-3481.
17 J. Kang and L.-W. Wang, *J. Phys. Chem. Lett.*, 2017, **8**, 489-493.
18 L. K. Ono, S. F. Liu and Y. Qi, *Angew. Chem., Int. Ed.*, 2020, **59**, 6676-6698.
19 I. Levine, O. G. Vera, M. Kulbak, D. R. Ceratti, C. Rehermann, J. A. Márquez, S. Levcenko, T. Unold, G. Hodes, I. Balberg, D. Cahen and T. Dittrich, *ACS Energy Lett.*, 2019, **4**, 1150-1157.
20 S. Heo, G. Seo, Y. Lee, D. Lee, M. Seol, J. Lee, J.-B. Park, K. Kim, D.-J. Yun, Y. S. Kim, J. K. Shin, T. K. Ahn and M. K. Nazeeruddin, *Energy Environ. Sci.*, 2017, **10**, 1128-1133.
21 A. Baumann, S. Väth, P. Rieder, M. C. Heiber, K. Tvingstedt and V. Dyakonov, *J. Phys. Chem. Lett.*, 2015, **6**, 2350-2354.
22 W. S. Yang, B.-W. Park, E. H. Jung, N. J. Jeon, Y. C. Kim, D. U. Lee, S. S. Shin, J. Seo, E. K. Kim, J. H. Noh and S. I. Seok, *Science*, 2017, **356**, 1376-1379.
23 S. Yuan, Z.-K. Wang, M.-P. Zhuo, Q.-S. Tian, Y. Jin and L.-S. Liao, *ACS Nano*, 2018, **12**, 9541-9548.
24 M. Zhang, Z. Zheng, Q. Fu, P. Guo, S. Zhang, C. Chen, H. Chen, M. Wang, W. Luo and Y. Tian, *J. Phys. Chem. C*, 2018, **122**, 10309-10315.
25 Y. Zhang, T. Guo, H. Yang, R. Bose, L. Liu, J. Yin, Y. Han, O. M. Bakr, O. F. Mohammed and A. V. Malko, *Nat. Commun.*, 2019, **10**, 189.
26 K. Miyata, D. Meggiolaro, M. T. Trinh, P. P. Joshi, E. Mosconi, S. C. Jones, F. De Angelis and X.-Y. Zhu, *Sci. Adv.*, 2017, **3**, e1701217.
27 F. Ambrosio, J. Wiktor, F. De Angelis and A. Pasquarello, *Energy Environ. Sci.*, 2018, **11**, 101-105.
28 E. Cinquanta, D. Meggiolaro, S. G. Motti, M. Gandini, M. J. P. Alcocer, Q. A. Akkerman, C. Vozzi, L. Manna, F. De Angelis, A. Petrozza and S. Stagira, *Phys. Rev. Lett.*, 2019, **122**, 166601.
29 F. Wang, Y. Fu, M. E. Ziffer, Y. Dai, S. F. Maehrlein and X.-Y. Zhu, *J. Am. Chem. Soc.*, 2021, **143**, 5-16.
30 O. Yaffe, Y. Guo, L. Z. Tan, D. A. Egger, T. Hull, C. C. Stoumpos, F. Zheng, T. F. Heinz, L. Kronik,

M. G. Kanatzidis, J. S. Owen, A. M. Rappe, M. A. Pimenta and L. E. Brus, *Phys. Rev. Lett.*, 2017, **118**, 136001.

31 W. Chu, Q. Zheng, O. V. Prezhdo, J. Zhao and W. A. Saidi, *Sci. Adv.*, 2020, **6**, eaaw7453.

32 W. Chu, W. A. Saidi, J. Zhao and O. V. Prezhdo, *Angew. Chem., Int. Ed.*, 2020, **59**, 6435-6441.

33 M. H. Du, *J. Mater. Chem. A*, 2014, **2**, 9091-9098.

34 M.-H. Du, *J. Phys. Chem. Lett.*, 2015, **6**, 1461-1466.

35 D. Meggiolaro, S. G. Motti, E. Mosconi, A. J. Barker, J. Ball, C. Andrea Riccardo Perini, F. Deschler, A. Petrozza and F. De Angelis, *Energy Environ. Sci.*, 2018, **11**, 702-713.

36 D. Meggiolaro and F. De Angelis, *ACS Energy Lett.*, 2018, **3**, 2206-2222.

37 X. Zhang, M. E. Turiansky, J.-X. Shen and C. G. Van de Walle, *Phys. Rev. B*, 2020, **101**, 140101.

38 X. Zhang, M. E. Turiansky and C. G. Van de Walle, *J. Phys. Chem. C*, 2020, **124**, 6022-6027.

39 Y. Huang, W.-J. Yin and Y. He, *J. Phys. Chem. C*, 2018, **122**, 1345-1350.

40 Y. Kang, S. Kang and S. Han, *Mater. Today Adv.*, 2019, **3**, 100019.

41 A. V. Cohen, D. A. Egger, A. M. Rappe and L. Kronik, *J. Phys. Chem. Lett.*, 2019, **10**, 4490-4498.

42 J. Yin, H. Yang, K. Song, A. M. El-Zohry, Y. Han, O. M. Bakr, J.-L. Brédas and O. F. Mohammed, *J. Phys. Chem. Lett.*, 2018, **9**, 5490-5495.

43 H. Shi and M.-H. Du, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **90**, 1236.

44 D. R. Ceratti, A. V. Cohen, R. Tenne, Y. Rakita, L. Snarski, L. Cremonesi, I. Goldian, I. Kaplan-Ashiri, T. Bendikov, V. Kalchenko, M. Elbaum, M. A. C. Potenza, L. Kronik, G. Hodes and D. Cahen, 2020, arXiv:2009.14617.

45 J. Heyd, G. E. Scuseria and M. Ernzerhof, *J. Chem. Phys.*, 2003, **118**, 8207-8215.

46 C. C. Stoumpos, C. D. Malliakas, J. A. Peters, Z. Liu, M. Sebastian, J. Im, T. C. Chasapis, A. C. Wibowo, D. Y. Chung, A. J. Freeman, B. W. Wessels and M. G. Kanatzidis, *Cryst. Growth Des.*, 2013, **13**, 2722-2727.

47 J. Neugebauer and C. G. Van de Walle, *Phys. Rev. Lett.*, 1995, **75**, 4452-4455.

48 C. T. Sah, J. Y. Sun and J. J. Tzou, *Appl. Phys. Lett.*, 1983, **43**, 204-206.

49 A. Janotti and C. G. Van de Walle, *Nat. Mater.*, 2007, **6**, 44-47.

50 B. Clerjaud, *Phys. B*, 1991, **170**, 383-391.

51 D. A. Egger, L. Kronik and A. M. Rappe, *Angew. Chem.*, 2015, **127**, 12614-12618.

52 D. R. Ceratti, A. Zohar, R. Kozlov, H. Dong, G. Uraltsev, O. Girshevitz, I. Pinkas, L. Avram, G. Hodes and D. Cahen, *Adv. Mater.*, 2020, **32**, 2002467.

53 C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti and C. G. Van de Walle, *Rev. Mod. Phys.*, 2014, **86**, 253-305.

54 C. Freysoldt, J. Neugebauer and C. G. Van de Walle, *Phys. Rev. Lett.*, 2009, **102**, 016402.

55 C. Freysoldt, J. Neugebauer and C. G. Van de Walle, *Phys. Status Solidi B*, 2011, **248**, 1067-1076.

56 A. Zohar, M. Kulbak, I. Levine, G. Hodes, A. Kahn and D. Cahen, *ACS Energy Lett.*, 2019, **4**, 1-7.

57 A. Alkauskas, Q. Yan and C. G. Van de Walle, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **90**, 075202.

58 S. P. DenBaars, D. Feezell, K. Kelchner, S. Pimputkar, C.-C. Pan, C.-C. Yen, S. Tanaka, Y. Zhao, N. Pfaff, R. Farrell, M. Iza, S. Keller, U. Mishra, J. S. Speck and S. Nakamura, *Acta Mater.*, 2013, **61**, 945-951.

59 M. Swift, A. Janotti and C. G. Van de Walle, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2015, **92**, 214114.

60 M. Swift and C. G. Van de Walle, *J. Phys. Chem. C*, 2016, **120**, 9562-9568.

61 G. Kresse and J. Furthmüller, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1996, **54**, 11169-11186.

62 P. E. Blöchl, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1994, **50**, 17953-17979.

63 D. Broberg, B. Medasani, N. E. Zimmermann, G. Yu, A. Canning, M. Haranczyk, M. Asta and G. Hautier, *Comput. Phys. Commun.*, 2018, **226**, 165-179.

64 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

65 A. Jain, G. Hautier, C. J. Moore, S. Ping Ong, C. C. Fischer, T. Mueller, K. A. Persson and G. Ceder, *Comput. Mater. Sci.*, 2011, **50**, 2295-2310.

66 J. B. Varley, A. Janotti and C. G. Van de Walle, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **89**, 075202.

67 N. Österbacka, P. Erhart, S. Falletta, A. Pasquarello and J. Wiktor, *Chem. Mater.*, 2020, **32**, 8393-8400.