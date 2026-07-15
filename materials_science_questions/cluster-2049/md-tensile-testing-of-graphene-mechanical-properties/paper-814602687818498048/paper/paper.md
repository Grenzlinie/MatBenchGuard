# Nanoscale

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: J. Han, N. Pugno and S. Ryu, *Nanoscale*, 2015, DOI: 10.1039/C5NR04134A.

![](./images/814602687818498048_1.jpg)

This is an **Accepted Manuscript**, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the [Information for Authors].

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard [Terms & Conditions] and the [Ethical guidelines] still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/814602687818498048_2.jpg)

www.rsc.org/nanoscale

# Nanoindentation cannot accurately predict the tensile strength of graphene or other 2D materials

Jihoon Han, $^{a,b}$ Nicola Pugno $^{c,d,e}$ and Seunghwa Ryu$^{*a}$

Due to the difficulty of performing uniaxial tensile testing, the strengths of graphene and its grain boundaries have been measured in experiments by nanoindentation testing. From a series of molecular dynamics simulations, we find that the strength measured in uniaxial simulation and the strength estimated from the nanoindentation fracture force can differ significantly. Fracture in tensile loading occurs simultaneously with the onset of crack nucleation near 5-7 defects, while the graphene sheets often sustain the indentation loads after the crack initiation because the sharply concentrated stress near the tip does not give rise to enough driving force for further crack propagation. Due to the concentrated stress, strength estimation is sensitive to the indenter tip position along grain boundaries. Also, it approaches the strength of pristine graphene if the tip is located slightly away from the ground boundary line. Our findings reveal the limitations of nanoindentation testing in quantifying the strength of graphene, and show that the loading-mode-specific failure mechanism must be taken into account in designing reliable devices from graphene and other technologically important 2D materials.

## Introduction

Pristine, defect-free graphene, which is packed in a honeycomb lattice with sp2 carbon-carbon bonds, exhibits exceptional mechanical properties$^{1-4}$, showing great promise for the development of high strength materials and devices. The ideal intrinsic strength of 120 GPa and the in-plane stiffness of 1.0 TPa are mechanically measured by atomic-force-microscopy-based nanoindentation testing for freely suspended pristine graphene prepared by mechanical exfoliation$^{2,5-7}$. However, polycrystalline graphene synthesized by chemical vapor deposition$^{8-12}$ is an inevitable choice for realistic applications in need of large-area graphene. Recent transmission electron microscopy experiments$^{13-15}$ revealed that the grain boundary (GB) lines$^{16}$ consist of an array of pentagon-heptagon (5-7) defects and vacancies$^{17-21}$, which can serve as stress-intensifying sites under mechanical loading.

To quantify the effect of GBs on the strength of graphene, many theoretical and experimental studies have been performed using uniaxial tensile loading and nanoindentation testing$^{22-32}$. In atomistic simulations, uniaxial tension simulations predict that the strength of polycrystalline graphene, even if only topological 5-7 defects without vacancies are considered is lower than the strength of pristine graphene$^{23-28}$. The weakening of polycrystalline graphene is attributed to the buildup of pre-stress around 5-7 defects along GBs. In general, high-angle GBs show higher strength than low-angle GBs due to denser 5-7 defect pile-up, which counterbalances the dipole stress field more effectively.

Meanwhile, in experimental studies, strength levels determined in nanoindentation testing have only been reported due to the difficulty of performing uniaxial testing$^{29-32}$. Lee *et al.*$^{32}$ reported that the GB strength is comparable to the strength of pristine graphene regardless of the misorientation angle, which is inconsistent with theoretical predictions. In contrast, other studies$^{29-31}$ have shown that the strength of GB is significantly lower than the pristine strength, and that higher angle GB has higher strength. To reveal the origin of the inconsistency between theoretical and experimental studies, as well as the mismatch among experimental nanoindentation testing, it is necessary to reveal the failure mechanism of graphene under different loadings. A few molecular dynamics simulation studies have been reported the effect of defects on the failure force of nanoindentation$^{33,34}$ which is found to critically depend on the indentation site. Sha *et al.*$^{34}$ shows the fracture behaviour of polycrystalline graphene with GB triple junctions, which are regarded as weakest points, under nanoindentation is critically

---

$^{a}$ Department of Mechanical Engineering, Korea Advanced Institute of Science and Technology (KAIST), 291 Daehak-ro, Yuseong-gu, Daejeon, 305-701, Republic of Korea. E-mail: ryush@kaist.ac.kr
$^{b}$ Research Reactor Utilization Department, Korea Atomic Energy Research Institute, 898-111 Daedeok-daero, Yuseong-gu, Daejeon, 305-535, Republic of Korea
$^{c}$ Laboratory of Bio-Inspired and Graphene Nanomechanics, Department of Civil, Environmental and Mechanical Engineering, University of Trento, Via Mesiano 77, I-38123 Trento, Italy
$^{d}$ Centre for Materials and Microsystems, Fondazione Bruno Kessler, Via Sommarive 18, I-38123 Povo (Trento), Italy
$^{e}$ School of Engineering and Materials Science, Queen Mary University of London, Mile End Road, E1 4NS, London, UK
† Electronic Supplementary Information (ESI) available: Modelling of polycrystalline graphene, verification of loading speed, biaxial tensile simulations, comparison of stress distribution, size effect of indenter radius, force-deflections curves, stability analysis of crack propagation. See DOI: 10.1039/x0xx00000x

![](./images/814602687818498048_3.jpg)

![](./images/814602687818498048_4.jpg)

![](./images/814602687818498048_5.jpg)

![](./images/814602687818498048_6.jpg)

Fig. 1 – (a) Schematic of nanoindentation simulations. (b) Force-displacement curve obtained from the nanoindentation of pristine graphene. (c) In-plane stress distribution along the central line of the graphene sheet. (d) Stress versus force curve obtained from (b) and (c) at various deflections.

dependent on the indentation site due to non-uniform stress distribution. For the strength of polycrystalline graphene, several molecular dynamics simulations are performed to investigate the effects of the grain size³⁸ and Stone-Thrower-Wales (STW)³⁹. They revealed that the strength depends on the grain size under uniaxial tensile loading and follow an inverse pseudo Hall-Petch relation. In another work, the strength of the STW defective graphene are sensitive to defect orientation and tilting angles. However, a detailed investigation on the failure mechanism difference between the nanoindentation and the uniaxial tensile loading was missing, which can provide additional insight on the discrepancy.

In this study, we perform molecular dynamics simulations to compare the predicted strength as well as the failure mechanism in both uniaxial tensile simulations and nanoindentation simulations. We limit the focus of our study on the bicrystal graphene to study the strength estimation of individual GBs in detail, and to mimic the typical experimental condition where the indenter radius is much smaller than the grain size²⁹⁻³². We find that fractures in tension occur simultaneously with the onset of crack nucleation near 5-7 defects. Under tensile loads, a uniform stress field is applied to the entire graphene sheet, providing a driving force for the catastrophic propagation of crack after the crack nucleation. On the contrary, graphene sheets often sustain loads after crack nucleation during indentation simulations. The applied stress from nanoindentation is concentrated sharply around the indenter tip, and crack propagation does not follow crack nucleation immediately when the distance between 5-7 defects is large, i.e. in the case of low-angle GBs. Thus, the failure force from nanoindentation cannot be directly linked to the onset of crack nucleation.

Due to this stress concentration of nanoindenter probe, strength estimation depends significantly on the indenter position along the GB. For the same reason, the predicted strengths of tilt GBs approach the strength of pristine

![](./images/814602687818498048_7.jpg)

Fig. 2 – (a) Force-deflection curve of pristine graphene from nanoindentation and atomic configurations at the indentation depth at fracture. (b) Stress-strain curve of pristine graphene from uniaxial tensile simulation and atomic configurations at fracture. Scale bars represent 50 Å.

graphene if the center of the indenter tip is located slightly away from the GB line. Our findings show the limitation of nanoindentation testing in quantifying the strength of graphene, and also imply that the loading-mode-specific failure mechanism must be taken into account in designing reliable devices from graphene and other technologically important 2D materials.

## Methods
Here, we explain the methodology for nanoindentation simulation of graphene sheet. To calculate the tip force of indentation, which corresponds to the indentation depth, nanoindentation simulations are carried at room temperature using molecular dynamics simulations. The simulation cell sizes are chosen to be around 50nm×50nm along x and y-axes, and are sufficiently larger than stress fields of dislocations. The adaptive intermolecular reactive empirical bond order (AIREBO) potential³⁵ is used to describe a bond interaction between carbon atoms in the graphene sheet. The cutoff radius of $r_{cc}$=1.92 Å²³,²⁴,²⁶,²⁷ is used to avoid the influence of nonphysical behavior on the fracture process. Molecular dynamics simulations are performed using LAMMPS³⁶ with a time step of 1.0 fs. The samples are initially equilibrated for 20 ps, using the NPT ensemble (widely known as isothermal-isobaric ensemble) at 300 K. Nanoindentation simulation is conducted with NVT ensemble (widely known as Nosé-Hoover thermostat) at 300 K.

We consider a frictionless rigid spherical indenter of radius R that exerts a force on each atom given by:
$$
F(r) = -K(r-R)^2 \tag{1}
$$
where K, r, and R indicate the specific force constant, the distance from the each atom to the center of the indenter, and the radius of the spherical indenter, respectively. The non-zero value of repulsive force exerts for $r < R$. In our study, K of 10 eV/Å³ and R of 50 Å are used to simulate the indentation of the polycrystalline graphene. Note that the ratio of indenter radius to sample size ($R/L \approx 1/5$) is similar to that used in Rasool's experimental conditions.³⁰ It has been shown that the rupture force does not depend on the sample size if it is more than twice larger than the indenter radius.⁴⁰

The carbon atoms inside the circular hole region could freely move (blue atoms in Fig. 1(a)), but the atoms outside the circular hole region are fixed to form a clamped boundary condition (red atoms in Fig. 1(a)). The position of indenter tip is located on the geometric center of the polycrystalline graphene and is moved in z-direction by 0.01 Å from the original position of indenter at every 5 ps until it fails completely. A constant indenter speed of 0.02 Å/ps is used (see section S2 of the Supplementary information for the

![](./images/814602687818498048_8.jpg)

Fig. 3 – Strength estimation as a function of indenter position (D) for (a) symmetric tilt GBs and (b) asymmetric tilt GBs. The inset of (a) is a schematic diagram of a nanoindentation simulation in which the indenter tip is located on the GB line. The strength estimation from nanoindentation and uniaxial tensile simulations is plotted together for (c) symmetric tilt GBs and (d) asymmetric tilt GBs.

effect of indenter speed). As the indenter gradually moves downward, the force exerted on the indenter is measured for circular clamped graphene sheet. The force is averaged over 5 ps at each deformation increment to avoid thermal fluctuation.

## Results and Discussions

We first perform nanoindentation of a pristine graphene sheet via molecular dynamics simulations, as shown in Fig. 1(a). We obtain the force-deflection curve for pristine graphene, as depicted in Fig. 1(b). Fig. 1(c) presents the sharp stress concentration around the indenter tip on the verge of rupture (see Fig. S4 in the Supplementary Information for the stress field on the graphene sheets with and without GB). The atomic virial stress is calculated with an atomic volume of $8.8\ \mathring{A}^3$. $^{24}$

Combining Fig. 1(b) and Fig. 1(c) at various indentation depths, we obtain the indenter tip stress versus force curve for pristine graphene, as shown in Fig. 1(d). Indenter stresses are defined by the average maximum stress between $\sigma_{xx}$ and $\sigma_{yy}$ at various indentation depths. In the remaining part of this study, following previous studies, we estimate the strength of polycrystalline graphene by converting the failure force into the strength using the stress-force relationship (see Fig. 1(d)). $^{2,30,32}$ Thus, GB strengths, which are estimated by the failure force, are directly compared with strength measured by tensile simulations.

The estimated strength of pristine graphene is 105 GPa, which is in good agreement with the results of the experimental nanoindentation tests $^{2,30,32}$. In comparison, the previous uniaxial tension simulations, conducted using the

![](./images/814602687818498048_9.jpg)

Fig. 4 – Atomic configurations at various indentation depths or tensile strains. (a) Force-deflection curve from nanoindentation and atomic configurations at various deflections. Failure occurs at significantly further indentation after the crack nucleation. (b) Stress-strain curve from uniaxial tension and atomic configurations at various indentation depths. Failure occurs immediately after the crack nucleation. Scale bars represent 50 Å.

same empirical potential, predict a strength of 120 GPa²³,²⁶,²⁷.
The strength is underestimated in the nanoindentation test because the graphene sheet is subjected to equibiaxial tensile load. The strength obtained from biaxial tensile simulation shows a good match with the strength estimated from nanoindentation (see Fig. S3 in the Supplementary Information). Basically, crack nucleates when the maximum stress reaches the materials strength. In addition, we carefully compare the failure mechanism between the uniaxial tensile simulation and the nanoindentation simulation. Both studies predict catastrophic crack propagation right after the crack initiation (see Fig. 2). This implies that both tests capture the onset of crack nucleation, and thus can serve as equivalent tests for estimating graphene strength, apart from the different strength estimation values that originate from the different stress states.

Having established the validity of the nanoindentation simulation for pristine graphene, we carry out nanoindentation simulations for bi-crystalline graphene sheets having GBs with various misorientation tilt angles. We construct a series of symmetric and asymmetric tilt GBs with various tilt angles (see Fig. S1 in the Supplementary Information). We place the GB line at the center of the hole and measure the failure force as a function of indenter location along the GB line (see the inset of Fig. 3(a)). The 5-7 defects are periodically located for the symmetric tilt GBs, and the distance between 5-7 defects increases with decreasing tilt angle. The inter-defect distance is 40 Å for symmetric tilt GB with an angle of 5.7°, and 8 Å for symmetric tilt GB with an angle of 27.8°. Interestingly, the failure force turns out to be sensitive to the location of the indenter for low angle tilt GBs. The failure force can be converted to the strength estimation via the stress-force plot, as shown in Fig. 1(d). We plot the

![](./images/814602687818498048_10.jpg)

Fig. 5 – Strength estimation as a function of indenter position (S) for (a) symmetric tilt GBs and (b) asymmetric tilt GBs.

strength estimation as a function of distance (D), where D=0 refers to the center of the 5-7 defect. The entire graphene sheet is shifted by distance D when the distance between the indenter tip and the 5-7 defect is adjusted. The strength estimation can vary up to 50%, and this is significantly beyond the statistical error from thermal fluctuations, as shown in Fig. 3(a). We perform an equivalent set of simulations for asymmetric tilt GBs, and obtain similar results, as shown in Fig. 3(b). All stress-strain curves are depicted in Figs. S6-S7 in the Supplementary Information.

As a function of tilt angles, the estimated strengths from the failure force of nanoindentation are compared with the strengths obtained from uniaxial tensile simulations, as shown in Figs. 3(c)-(d). We present the strength minima and maxima from Figs. 3(a)-(b) as error bars, which show a wide scatter for the same tilt angle. Such a wide spread of strength estimation for the same tilt angle has also been observed in the previous nanoindentation experiments³⁰. Given that a wide range of strength estimation can be obtained for the same GB configuration, even wider strength estimation is expected in experiments in which many different GB configurations are found for a similar tilt angle. Notably, the strength of GB is overestimated in nanoindentation tests, whereas an opposite tendency is found for pristine graphene.

![](./images/814602687818498048_11.jpg)

Fig. 6 – Atomic configurations at fracture for crack propagation generated away from the GB. (a) Force-deflection curve and atomic configurations of (a) symmetric tilt GBs with an angle of 17.9° at distance (S) of 6 nm, and (b) asymmetric tilt GBs with an angle of 17.39° at the distance (S) of 5 nm. Scale bars represent 50 Å.

To examine the observed discrepancy between uniaxial tensile and nanoindentation studies, we compare the evolution of atomic configuration in the nanoindentation simulation with that in the tensile simulation. We find that the graphene sheets under indentation often sustain loads after crack nucleation. Fig. 4(a) shows the evolution of atomic configurations for a symmetric tilt GB with an angle of 5.7°. The initial crack nucleation occurs at 3.54 nm, but the graphene sheet sustains the load up to the deflection of 4.6 nm, until catastrophic failure occurs beyond 5.0 nm. The pre-stress around the 5-7 defects enables crack nucleation at a small deflection, but fast-diminishing stress away from the center of the indenter does not provide a sufficient driving force for catastrophic crack propagation. A crack grows in a stable manner until it reaches the size of the indenter radius. The overestimation of strength of GB is attributed to the delay in catastrophic crack growth after nucleation. The amount of delay depends on the atomic configuration near the crack tip, and this leads to the observed variation in strength as a function of distance D. On the contrary, the onset of crack nucleation is immediately captured by the failure in the uniaxial tension simulation, as depicted in the Fig. 4(b). The

homogeneous stress field provides a driving force for unstable crack growth, followed by fracturing right after crack nucleation. The observed crack growth can be explained by the relation between the crack size and energy release rate from linear elastic fracture mechanics theory. We derive a formula for the energy release rate as a function of contact radius $(r_1)$ and crack length (a) (see section S7 and Fig. S10 of Supplementary Information). When the distance (r) from the center of indenter tip is larger than $r_1$, the stress field decays as 1/r because of the force balance in the vertical direction (indentation force $F = 2\pi rt\sigma(r)\sin\theta$ where t is the thickness of graphene and $\sin\theta \approx r_1/R$). When the crack length (a) becomes larger than the contact radius $(r_1)$, the potential energy is given as $\Delta \mathrm{U} \approx \Delta \mathrm{U}_{1}+2 \pi \mathrm{t} / \mathrm{E} \cdot \int_{r_{1}}^{a} \sigma(r)^{2} r d r=\Delta \mathrm{U}_{1}+F^{2} / 2 \pi t E \sin ^{2} \theta \cdot \ln a / r_{1}$, where $\Delta \mathrm{U}_{1}$ is the potential energy change within the contact area. Accordingly, the energy release rate becomes inversely proportional to crack length, i.e. $\mathrm{G}(a) \propto 1 / a$. Thus, crack growth becomes stable when the crack size is larger than indenter radius.

This delayed crack propagation is not observed in pristine graphene because very high stress is required for crack nucleation in the absence of pre-stress. Upon crack nucleation, large accumulated elastic energy is released to instantaneously create a crack bigger than the indenter radius. Similarly, in the high-tilt angle GB sample, the pre-stress of the 5-7 defects is effectively cancelled. Thus, the high-tilt angle GB fails in a manner similar to that of pristine graphene, and its strength estimation is close to the value of pristine graphene as shown in Figs. 3(a)-(b). To summarize, the nanoindentation has a tendency to underestimate the strength of pristine graphene due to the biaxial stress state, while the nanoindentation overestimates the strength of GB because of the delayed crack propagation. This gives one explanation on why the strength difference between pristine and polycrystalline graphene is underestimated in some literature $^{32}$.

We also investigate the effect of misalignment of the indenter tip on the strength of GB. We measure the failure force as a function of the distance (S) away from the GB line (see the inset of Fig. 5(a)). All stress-strain curves are depicted in Figs. S4-S5 in the Supplementary Information. In the case of high-tilt angle GBs, the failure force approaches that of pristine graphene at a distance much smaller than the indenter radius (50 Å), while it does so at a larger distance for low-tilt angle GBs. This distance dependence can be understood in terms of pre-stress generated from the 5-7 defect array. The dipolar pre-stress of a single 5-7 defect is not effectively counterbalanced for low-angle GBs, for which inter-defect distance is relatively large. In contrast, in high-angle GBs in which 5-7 defects are located close to each other, the dipolar pre-stress field is effectively cancelled. Moreover, we find that the failure occurs away from the GB in the bi-crystal graphene when the distance S is similar to the indenter radius, regardless of indenter radius (see Section S5 of supplementary information). Fig. 6 shows the failure mechanism of the graphene sheet when the indenter is located away from the GBs for both symmetric and asymmetric GBs. The failure occurs near the center of the indenter tip even though the crack initiated near the 5-7 defect. This explains the high strength estimation in the case of indenter misalignment, as shown in Fig. 5.

Lee et al. $^{32}$ reported that the strength of GBs is comparable to the strength of pristine graphene regardless of the tilt angle, while Rasool et al. $^{30}$ reported that strength depends on the tilt angle. This difference might be caused by the different indenter radiuses used in those studies. The indenter radius in the former study is 26-38 nm; a small misalignment of ~10 nm could have led to an overestimation of the strength. In contrast, Rasool et al. used an indenter with a radius of 115 nm, which would for correct strength estimation even for larger misalignment. In addition, Lee et al. attributed this phenomena to the discrepancy of atomic structures between symmetric and asymmetric GB. However, we observed that symmetric and asymmetric GBs show the same tendency of strength estimations (see Figs. 3(c)-(d)).

## Conclusions

In conclusion, we find that the strengths of polycrystalline graphene are locally measureable quantities that are only valid within the radius of the indenter, because nanoindentation produces a sharp stress concentration near the indenter tip. In contrast to tensile simulation, bi-crystalline graphene can sustain the indenter load beyond the crack initiation. Thus, the strength estimated from nanoindentation is not suitable for mapping into the tensile strength. The strength estimation of polycrystalline graphene can vary as the indenter location changes along the GB line, which explains the scatter obtained in previous experimental studies. Also, we find that nanoindentation has a tendency to underestimate the pristine graphene strength and overestimate the polycrystalline graphene strength. This gives another explanation for how nanoindentation experiments can underestimate the strength difference between polycrystalline graphene $^{37}$ and pristine graphene. Our findings elucidate the problem of mapping the strength estimated from nanoindentation fracture force to strength of the material under tensile loading. Moreover, the difference between fracture mechanisms in the two different loading modes can serve as a guideline to design mechanically reliable devices based on 2D materials.

## Acknowledgements

The authors wish to thank Prof. Seyoung Im, Korea Advanced Institute of Science and Technology (KAIST), for his encouragement and discussion. We acknowledge financial support from the Basic Science Research Program through the National Research Foundation of Korea (NRF), funded by the Ministry of Science, ICT & Future Planning (2013R1A1A010091) and the computing resources from the Supercomputing Center/Korea Institute of Science and Technology Information (KSC-w014-C2-039). N.M.P. is supported by the European Research Council (ERC StG Ideas 2011 BIHSNAM no. 279985 on 'Bio-inspired hierarchical supernanomaterials', ERC PoC 2013-1

ARTICLE

REPLICA2 no. 619448 on 'Large-area replication of biological anti-adhesive nanosurfaces', ERC PoC 2013-2 KNOTOUGH no. 632277 on 'Super-tough knotted fibres'), by the European Commission under the Graphene Flagship (WP10 'Nanocomposites', no. 604391) and by the Provincia Autonoma di Trento ('Graphene nanocomposites', no. S116/2012-242637 and reg. delib. no. 2266).

# Notes and references

1  J. S. Bunch, A. M. van der Zande, S. S. Verbridge, I. W. Frank, D. M. Tanenbaum, J. M. Parpia, H. G. Craighead and P. L. McEuen, *Science*, 2007, 315, 490-493.
2  C. Lee, X. D. Wei, J. W. Kysar and J. Hone, *Science*, 2008, 321, 385-388.
3  S. P. Koenig, N. G. Boddeti, M. L. Dunn and J. S. Bunch, *Nat. Nanotechnol.*, 2011, 6, 543-546.
4  G. Lopez-Polin, C. Gomez-Navarro, V. Parente, F. Guinea, M. I. Katsnelson, F. Perez-Murano and J. Gomez-Herrero, *Nat. Phys.*, 2015, 11, 26-31.
5  S. Berciaud, S. Ryu, L. E. Brus and T. F. Heinz, *Nano Lett.*, 2009, 9, 346-352.
6  D. Garcia-Sanchez, A. M. van der Zande, A. S. Paulo, B. Lassagne, P. L. McEuen and A. Bachtold, *Nano Lett.*, 2008, 8, 1399-1403.
7  J. S. Bunch, S. S. Verbridge, J. S. Alden, A. M. van der Zande, J. M. Parpia, H. G. Craighead and P. L. McEuen, *Nano Lett.*, 2008, 8, 2458-2462.
8  Q. K. Yu, J. Lian, S. Siriponglert, H. Li, Y. P. Chen and S. S. Pei, *Appl. Phys. Lett.*, 2008, 93.
9  A. Reina, X. T. Jia, J. Ho, D. Nezich, H. B. Son, V. Bulovic, M. S. Dresselhaus and J. Kong, *Nano Lett.*, 2009, 9, 30-35.
10 Y. Lee, S. Bae, H. Jang, S. Jang, S. E. Zhu, S. H. Sim, Y. I. Song, B. H. Hong and J. H. Ahn, *Nano Lett.*, 2010, 10, 490-493.
11 S. Bae, H. Kim, Y. Lee, X. Xu, J.-S. Park, Y. Zheng, J. Balakrishnan, T. Lei, H. Ri Kim, Y. I. Song, Y.-J. Kim, K. S. Kim, B. Ozyilmaz, J.-H. Ahn, B. H. Hong and S. Iijima, *Nat. Nano.*, 2010, 5, 574-578.
12 X. Li, W. Cai, J. An, S. Kim, J. Nah, D. Yang, R. Piner, A. Velamakanni, I. Jung, E. Tutuc, S. K. Banerjee, L. Colombo and R. S. Ruoff, *Science*, 2009, 324, 1312-1314.
13 S. Malola, H. Häkkinen and P. Koskinen, *Phys. Rev. B*, 2010, 81, 165447.
14 O. V. Yazyev and S. G. Louie, *Phys. Rev. B*, 2010, 81, 195420.
15 J. Cervenka, M. I. Katsnelson and C. F. J. Flipse, *Nat. Phys.*, 2009, 5, 840-844.
16 J. Avila, I. Razado, S. Lorcy, R. Fleurier, E. Pichonat, D. Vignaud, X. Wallart and M. C. Asensio, *Sci. Rep.*, 2013, 3, 2439.
17 J. C. Meyer, A. K. Geim, M. I. Katsnelson, K. S. Novoselov, T. J. Booth and S. Roth, *Nature*, 2007, 446, 60-63.
18 P. Y. Huang, C. S. Ruiz-Vargas, A. M. van der Zande, W. S. Whitney, M. P. Levendorf, J. W. Kevek, S. Garg, J. S. Alden, C. J. Hustedt, Y. Zhu, J. Park, P. L. McEuen and D. A. Muller, *Nature*, 2011, 469, 389-392.
19 K. Kim, Z. Lee, W. Regan, C. Kisielowski, M. F. Crommie and A. Zettl, *Acs Nano*, 2011, 5, 2142-2146.
20 K. Kim, V. I. Artyukhov, W. Regan, Y. Y. Liu, M. F. Crommie, B. I. Yakobson and A. Zettl, *Nano Letters*, 2012, 12, 293-297.
21 J. R. Xiao, J. Staniszewski and J. W. Gillespie Jr, *Compos. Struct.*, 2009, 88, 602-609.
22 J. F. Zhang, J. J. Zhao and J. P. Lu, *Acs Nano*, 2012, 6, 2704-2711.
23 J. Han, S. Ryu, D. Sohn and S. Im, *Carbon*, 2014, 68, 250-257.
24 T. H. Liu, C. W. Pao and C. C. Chang, *Carbon*, 2012, 50, 3465-3472.

25 L. J. Yi, Z. N. Yin, Y. Y. Zhang and T. C. Chang, *Carbon*, 2013, 51, 373-380.
26 Y. J. Wei, J. T. Wu, H. Q. Yin, X. H. Shi, R. G. Yang and M. Dresselhaus, *Nat. Mater.*, 2012, 11, 759-763.
27 R. Grantab, V. B. Shenoy and R. S. Ruoff, *Science*, 2010, 330, 946-948.
28 Y. I. Jhon, S. E. Zhu, J. H. Ahn and M. S. Jhon, *Carbon*, 2012, 50, 3708-3716.
29 C. S. Ruiz-Vargas, H. L. L. Zhuang, P. Y. Huang, A. M. van der Zande, S. Garg, P. L. McEuen, D. A. Muller, R. G. Hennig and J. Park, *Nano Lett.*, 2011, 11, 2259-2263.
30 H. I. Rasool, C. Ophus, W. S. Klug, A. Zettl and J. K. Gimzewski, *Nat. Commun.*, 2013, 4, 2811.
31 A. Zandiatashbar, G. H. Lee, S. J. An, S. Lee, N. Mathew, M. Terrones, T. Hayashi, C. R. Picu, J. Hone and N. Koratkar, *Nat. Commun.*, 2014, 5, 3186.
32 G. H. Lee, R. C. Cooper, S. J. An, S. Lee, A. van der Zande, N. Petrone, A. G. Hammerherg, C. Lee, B. Crawford, W. Oliver, J. W. Kysar and J. Hone, *Science*, 2013, 340, 1073-1076.
33 Z. Song, V. I. Artyukhov, J. Wu, B. I. Yakobson and Z. Xu, *ACS Nano*, 2015, 9, 401-408.
34 Z. D. Sha, Q. Wan, Q. X. Pei, S. S. Quek, Z. S. Liu, Y. W. Zhang and V. B. Shenoy, *Sci. Rep.*, 2014, 4, 7437.
35 S. J. Stuart, A. B. Tutein and J. A. Harrison, *J. Chem. Phys.*, 2000, 112, 6472-6486.
36 S. Plimpton, *J. Comput. Phys.*, 1995, 117, 1-19.
37 X. Jia, J. Campos-Delgado, M. Terrones, V. Meunier and M. S. Dresselhaus, *Nanoscale*, 2011, 3, 86-95.
38 Z. D. Sha, S. S. Quek, Q. X. Pei, Z. S. Liu, T. J. Wang, V. B. Shenoy and Y. W. Zhang, *Sci. Rep.*, 2014, 4, 5991.
39 L. He, S. Guo, J. Lei, Z. Sha and Z. Liu, *Carbon*, 2014, 75, 124-132.
40 B. I. Costescu and F. Grater, *Phys. Chem. Chem. Phys.* 2014, 16, 12582-12590.

8 | *J. Name.*, 2012, **00**, 1-3

This journal is © The Royal Society of Chemistry 20xx