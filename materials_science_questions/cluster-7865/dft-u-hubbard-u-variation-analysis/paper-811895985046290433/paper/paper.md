# Atomic and Electronic Structure of Cerium Oxide Stepped Model Surfaces

María M. Branda,†,‡ Christoph Loschen,§,⊥ Konstantin M. Neyman,§,∥ and Francesc Illas*,§

Consejo Nacional de Investigaciones Científicas y Tecnológicas (CONICET), Argentina, Departamento de Física, Universidad Nacional del Sur, 8000 Bahía Blanca, Argentina, Departament de Química Física and Institut de Química Teòrica i Computacional (IQT CUB), Universitat de Barcelona, C/ Martí i Franquès 1, 08028 Barcelona, Spain, and Institució Catalana de Recerca i Estudis Avançats (ICREA), 08010 Barcelona, Spain

Received: July 9, 2008; Revised Manuscript Received: August 26, 2008

The atomic and electronic structure of ceria surfaces exhibiting step edges have been studied by means of periodic density functional (LDA+U and GGA+U) calculations. A variety of stoichiometric and nonstoichiometric models of increasing complexity have been designed. The electronic structure has been explored using the topological Bader analysis, the calculated magnetic moments and the ELF (electron localization function) maps. It is concluded that $Ce^{3+}$ atoms may exist even in stoichiometric extended ceria samples and that the presence of oxygen vacancies in stepped surfaces also induces the presence of $Ce^{3+}$ atoms although in both cases, the reduced atoms tend to occupy the sites with smallest possible coordination number.

## 1. Introduction
Due to their chemical versatility as reducible oxides and as oxygen storage, cerium oxides $(CeO_{2-x})$, hereafter referred to generically as ceria, are increasingly used in catalysis either as support or as active phase. The water gas shift reaction $^{1,2}$ and the elimination of nitrogen and sulfur oxides from exhaust car emissions by $NO_{x}$ and $SO_{x}$ reduction $^{3}$ provide two important examples. The oxygen storage capacity (OSC) exhibited by this oxide is precisely the basis for its use in automotive three-way catalysts. $^{4}$ By releasing and storing oxygen during fuel-rich and lean conditions, a suitable oxygen pressure for the catalytic removal of harmful exhaust gases can be maintained. Therefore, from a microscopic point of view, structural and electronic understanding of the effects of oxygen vacancy formation is crucial for a complete description of the mechanisms involved in the partial reduction/oxidation connected with OSC of ceria. $^{5}$ In addition to its use in catalysis, ceria plays an increasingly important role in several technologies: it serves as a component in gas sensors, $^{6}$ in low-temperature solid oxide fuel cells, $^{7}$ in solar cells, $^{8}$ as well as in insulating material in field effect transistors. $^{9}$ Due to other important properties, such as a high dielectric constant and good epitaxy on Si, ceria has also been regarded as a prospective material for future microelectronic applications. In particular, it is considered as a possible candidate to replace $SiO_{2}$ in some electronic appliances. $^{10-14}$

An important feature of ceria, either in catalysis or in other applications, is that, rather than being a mere inert component, it is likely to participate in chemical reactions through facile changes of the oxidation states $Ce^{4+} \leftrightarrow Ce^{3+}$, accompanied by the release or uptake of oxygen and a concomitant partial occupancy of the Ce (4f) orbital. This is precisely at the heart of difficulties faced by standard theoretical methods based on density functional theory (DFT). In fact, the description of the insulating $CeO_{2}$ within conventional DFT is more or less straightforward $^{15}$ to the point that recent DFT calculations represent this material in close accordance with experimental findings, quite independent of the exchange correlation functional employed. $^{15-17}$ On the contrary, $Ce_{2}O_{3}$ is a typical strongly correlated insulator and hence known to be a notorious problem case for electronic structure calculations based on standard DFT. From the recent literature, it is now evident that calculations using the standard local density approach (LDA) or generalized gradient approach (GGA) give a wrong metallic ground-state for $Ce_{2}O_{3}$, the problem being almost the same as described at length for NiO and arising from the narrow band character of the partially occupied Ni 3d states. $^{18}$ Recent work on several strongly correlated systems such as $La_{2}CuO_{4},^{19,20}$ $LaMnO_{3}^{21}$ or $MnO^{22}$ exemplifies the failure of the standard LDA or GGA implementations of DFT. Clearly, to achieve a physically meaningful and accurate description of ceria systems containing formally $Ce^{3+}$ cations it is required to go beyond LDA and GGA and use an exchange-correlation potential able to account for the strong localized character of the Ce f electron in the $Ce^{3+}$ oxidation state. The shortcomings of standard DFT may be overcome by different approaches: for example by correcting for the self-interaction error $^{23,24}$ in the calculation of the Coulomb repulsion term (self-interaction correction, SIC), which has been used for cerium oxides and related systems, $^{25}$ by explicit inclusion of an effective local two-electron one-center repulsion $U_{eff}$ term (leading to methods usually termed as LDA+U or GGA+U) $^{26-28}$ and also applied to bulk ceria. $^{15,29,30}$ Here, it is important to point out that different strategies have been developed by different authors. Loschen et al. $^{15}$ have chosen a U values for LDA+U and GGA+U which provide a balanced description of $CeO_{2}$ and $Ce_{2}O3$ whereas later on Castleton et al. $^{29}$ have shown that such a description may be difficult to achieve and suggest U values somewhat larger, especially if localization of the Ce (4f) electrons is sought for. Note, however, that localization of the f-electron, i.e. a nonmetallic solution for $Ce_{2}O_{3}$ can be achieved already with values of $U > 0.4$ eV, if one starts with solutions of high U values and than sucessively decreases $U.^{17}$ Nevertheless, Castleton et al. $^{29}$ also show that the accurate description of different properties may require different U values thus introducing a

* To whom correspondence should be addressed.
† CONICET.
‡ Universidad Nacional del Sur.
§ Universitat de Barcelona.
∥ ICREA.
⊥ Present address: Henkel Adhesive Technologies, Scientific Computing, D-40589 Düsseldorf, Germany.

certain degree of empirical character on the theoretical descrip- tion of this complicated system. Properly accounting for nonlocal character of exchange interactions as in hybrid DFT approaches, which mix nonlocal Fock exchange with the Slater exchange functional $^{31,32}$ has also been shown to give improved results for the electronic structure of $Ce^{3+}$ containing systems $^{30,33}$ although hybrid calculations become soon prohibitively expen- sive when large unit cells are used and the amount of Fockexchange may vary from system to system. $^{18-21}$

Because of the difficulties encountered by first-principles methods, the first attempts to study ceria surfaces from an atomistic point of view relied on the use of empirical potentials and force fields $^{34-40}$ although with a largely increasing number of papers using electronic structure methods. $^{40-42}$ Although the absolute surface energies obtained by the different methods differ, the sequence of stability for the low-index surfaces is the same in all of these studies, with (111) being the most stable and (001) the least stable. The formation and behavior of Ovacancies in $CeO_{2}$ bulk and surface and properties of $Ce_{2} O_{3}$  have been initially modeled by empirical potentials $^{34-36,39}$ and by standard DFT methods. $^{42-45}$ The force-field calculations suggest that the $O$ vacancy is more stable at the surface than in the bulk but do not bring information about the electronic structure of this point defect. At the same time, Kresse et al. unambiguously show that the GGA description of $Ce_{2} O_{3}$ is incorrect. $^{45}$ This led some authors to explore the more accurateGGA+U or hybrid DFT methods. Thus, Jiang et al. were amongthe first to use a GGA+U method to study $CeO_{2}$ surfaces. $^{46}$  They carefully explored the relative stability of various low index $CeO_{2}$ surfaces using a GGA+U scheme with a $U$ value of $7 eV$ combined with a $J$ value of $0.7 eV$ ; the $U$ and $J$ values being chosen to best reproduce the properties of bulk $CeO_{2}$ .Nolan et al. $^{47}$ reported periodic GGA+U calculations for $O$  vacancies at the relaxed $CeO_{2}(100)$ surface using $U=5 eV$ . These authors investigated different values of the $U$ parameter ranging from 2 to $7 eV$ . Below $5 eV$ , significant delocalization was still found, but for $5 eV$ and above, the result converged to a localized description. In the same line STM (scanningtunneling microscopy) experiments and GGA+U calculations $^{48}$  indicate that the formation energies for the surface and subsurface $O$ vacancy at the $CeO_{2}(111)$ surface are virtually the same and the $Ce^{3+}$ cations have a strongly localized 4f electron. This agrees with the fact that the theoretically observed surface relaxation induced by the $O$ vacancy involves the $O$  anions nearby which move closer to the vacancy. This suggests that the electrons are not trapped in the vacancy, as in the case of the $MgO(001)$ surface. $^{49,50}$ This is further supported by periodic DFT results for partial reduction of bulk ceria, $^{43}$ where the vacancy formation energy was found to be lowered by confining the electrons to the f-core levels of two Ce ions close to the vacancy. This picture is also in agreement with the one emerging from force-field calculations which find that separating the $Ce^{3+}$ ions from the $O$ vacancy on the (111) surface has a significant energy cost. $^{34,35}$ Hence, the theoretical description arising from LDA+U or hybrid calculations predicting the existence of localized states in the band gap in reduced ceria surfaces is in agreement with ultraviolet- (UPS) and X-ray photoelectron spectroscopy (XPS) experiments. $^{51-54}$ These experiments also show that when the surface is partially reduced the top of the valence band spectrum can be described as a combination of spectra for fully reduced $Ce^{3+}$ and fully oxidized $Ce^{4+}$ . These occupied gap-states appear $1.2-1.5 eV$ above the O 2p-band and have been theoretically identified as localized Ce (4f) states. $^{5}$ Here it is important to stress that this picture of a complete localization of the excess electrons on the two surface Ce ions neighboring the vacancy arises from explicitly correlated second order Møller-Plesset perturbation (MP2) theory calcula- tions carried out for embedded cluster models and is contrary to the delocalized description seen in the standard periodic DFT calculations for the $CeO_{2}(110)$ surface using the GGA exchange correlation potential but are in full agreement with GGA+U results recently reported for the partially reduced $CeO_{2}$ bulkand (001) surface. $^{5}$

The discussion above permits one to firmly state that the existence of $Ce^{3+}$ in ceria extended surfaces has its origin in the presence of oxygen vacancies. It has been recently suggested that this effect is enhanced in ceria nanoparticles because the surface atoms have reduced coordination. $^{48,55-57}$ This leads to CeO2-x nonstoichiometric nanoparticles containing oxygen va-cancies with a concomitant transformation from $Ce^{4+}$ to $Ce^{3+}$  for a number of Ce sites. Indeed, this feature may be at the heart of the many useful properties of ceria nanoparticles. $^{58}$ The formation energies of nonstoichiometric nanoparticles have been studied recently by Loschen et al. $^{59,60}$ using GGA+U calcula tions combined with global optimizations using empirical potentials. These authors find that $(CeO_{2-x})_{n}$ nanoparticles formation energies scale linearly with the average coordination number of $Ce$ atoms and that reduced $Ce^{3+}$ cations tend to be located at lower coordinated sites. In particular, the bonding energy per $Ce$ atom is shown to correlate linearly with the average coordination number of $Ce$ , allowing predictions for particle sizes beyond the capabilities of current ab initio methods. From the discussion above, it appears that step edge and corner sites of $CeO_{2-x}$ nonstoichiometric nanoparticles tend to concentrate the reduced $Ce^{3+}$ cations which will surely exhibit a particular reactivity. Recent work by Lu et al. $^{61}$ brings important complementary information since these authors found that terraces of $CeO_{2}(111)$ thin films grown on $Ru(0001)$ often consist of several rotational domains. The circular shape of terraces suggests presence of a large variety of coordinatively unsaturated sites at the step edges which in addition preferen- tially nucleate gold particles deposited onto these films. Therefore, from the results on ceria nanoparticles discussedabove, one is tempted to assign these sites to reduced $Ce^{3+}$  cations. However, one must realize that there is an important chemical difference between the $Ce^{3+}$ and $Ce^{4+}$ of step edge Ce sites. In fact, while nanoparticles exhibit a large degree of nonstoichiometry, the thin films are in general essentially stoichiometric although this may depend on specific preparation conditions.

This poses an interesting question, namely the character of Ce edge sites in stoichiometric samples. The main goal of the present work is precisely the study of the electronic properties of the surface $Ce$ and $O$ ions on different step configurations, with and without oxygen vacancies. To this end, LDA+U calculations have been carried out to obtain the geometry of step containing model surfaces and careful, GGA+U, analysis of the electronic structure including Bader charges $^{62}$ and electron localization function (ELF) $^{63,64}$ has been performed. Results arethen compared with those corresponding to a perfect $CeO_{2}(111)$  surface which is taken as reference model for this analysis. Relevant results are also compared with those reported recentlyfor $(CeO_{2-x})_{n}$ nanoparticles. $^{59,60}$

## 2. Computational Details
In this work, periodic LDA+U and GGA+U calculations have been carried out for a series of slab models featuring different types of steps on a ceria surface. The physical idea

behind these schemes comes from the Hubbard Hamiltonian used in solid state physics for strongly correlated systems.26−28 In the practical implementations, the on-site two-electron integrals, which would appear in a post mean-field-theory method such as Hartree−Fock, are expressed in terms of two parameters. These are the Hubbard parameter U, which reflects the strength of the on-site Coulomb interaction, and the J parameter, which adjusts the strength of the exchange interaction. In the somewhat simplified, yet rotationally invariant method of Dudarev et al.,65 these two parameters are combined into a single parameter $U_{\text{eff}} = U - J$. Since LDA+U or GGA+U approaches seem also to be dependent on the specific chosen projector functions,16 Loschen et al. suggested a more practically oriented approach consisting in taking $U_{\text{eff}}$ as a sort of empirical parameter and fitting its value to reproduce certain experimental observables15 much in the same way as it has been done in molecular quantum chemistry for the so-called hybrid functionals but avoiding the introduction of nonlocal exchange and its concomitant computational complications. Both, LDA+U and GGA+U have been used with $U$ values taken from previous work dealing with bulk $CeO_2$ and $Ce_2O_3$.15 Hence, we take $U_{\text{eff}}$ = 5 eV for LDA+U and $U_{\text{eff}}$ = 3 eV for GGA+U with the VWN66 and PW91 exchange-correlation potential67,68 for the LDA and GGA part, respectively. Notice that the present $U$ values were suggested to provide a balanced description of both bulk $CeO_2$ and $Ce_2O_3$ bulk oxides.15 This pragmatic procedure may, however, not be free of artifacts since $U = 2$ eV has been suggested for a proper description of $Ce_2O_3^{30}$ whereas higher values16,29 have been proposed to obtain well localized $Ce^{3+}$ states in reduced $CeO_2$ models. In addition, the present approach seems to be able to properly describe localization in ceria nanoparticles containing both $Ce^{3+}$ and $Ce^{4+}$ atoms.59,60 However, given the semiempirical character of the LDA+U and GGA+U approaches one must admit that some results, especially those concerning Ce atoms with an oxidation state intermediate between +3 and +4, have to be regarded with caution since use of a large value of $U$ certainly will produce a more localized solution.29 However, it is also difficult to ascertain to what extent the description arising from a large $U$ value is not also a biased description. Hybrid functionals offer some clues but their results are also dependent on the amount of Fock exchange used in the definition of the exchange potential.18−21 Unfortunately, an unbiased fully ab initio description of nonstoichiometric ceria is still unreachable.

Previous work has shown that in general the GGA+U method leads to acceptable agreement with experiment at lower $U_{\text{eff}}$ energies than those necessary in the LDA+U method.15 This is, at least in part, attributed to the more accurate treatment of correlation effects within the GGA potential. Nevertheless, for $CeO_2$ there is clear indication that structural properties such as lattice constants and bulk modulus are somewhat better represented by the LDA+U method, whereas for $Ce_2O_3$ both LDA+U and GGA+U results show a similarly good accuracy.15 Therefore, geometry optimization has been performed throughout within the LDA+U scheme whereas energies and magnetic moments have been calculated by a GGA(PW91)+U approach. Net charges on relevant atoms were calculated using the topologic Bader analysis62 using the GGA+U density. This permits one to properly take into account the changes in atomic volume accompanying a change in oxidation state. This is an important point since otherwise calculated net charges on a given fixed volume can appear to be independent of the oxidation state.69 This is not the case for charges calculated following the Bader analysis. Loschen et al.15 have shown that the Bader charge on Ce atoms in bulk $CeO_2$ is +2.4e whereas the corresponding value for $Ce_2O_3$ is +2.0e. In addition, the latter charge is accompanied by a calculated magnetic moment of 0.96 $\mu_{\text{B}}$ resulting from the localized 4f electron in $Ce^{3+}$. The combined use of calculated Bader charges and magnetic moments permits us to clearly identify the two types of Ce atoms in the different surface models studied in the present work.

The periodic LDA+U and GGA+U calculations were carried out with the Vienna ab initio simulation package (VASP).70,71 The valence electronic states were expanded in a basis of plane waves with a cutoff of 415 eV for the kinetic energy and the effect of the core electrons on the valence states was represented with the projector augmented wave (PAW) approach72 as implemented in VASP.73 The total energy threshold defining self-consistency of the electron density was set to $10^{-3}$ eV, and the convergence criterion for structural optimization was set to be a total energy difference less than $10^{-2}$ eV for consecutive geometries. Numerical integration in the reciprocal space was carried out using a sufficiently dense grid of Monkhorst-Pack special k-points.74 The specific grids used for each surface model are discussed in the next section below.

### 3. Surface Models

To begin with, periodic slab models were constructed for the perfect $CeO_2$(111) surface with a vacuum width of $\sim$12 Å between the interleaved slabs. The slabs were cut from the bulk cubic (Fm3m) $CaF_2$ structure using the optimized lattice parameter values $a_0$ of 5.39 Å as obtained from LDA+U calculation with $U_{\text{eff}} = 5$ eV.15 Note that this is in excellent agreement with the experimental available results of $a_0 \approx 5.41$ Å (5.406(1) Å 75 or 5.411(1) Å 76). Slab models containing up to 15 atomic layers were examined and the three upper atomic layers were fully relaxed. The surface energy (LDA+U) for the slab models containing 9, 12, and 15 layers is found to be 0.81 eV per unit cell surface area indicating that the 9 layer (9 L) slab provides a sufficiently accurate model for the $CeO_2$(111) surface. For this model dipole−dipole interactions between images of dipolar slabs were negligible, <0.01 eV. Accuracy of numerical integration in the reciprocal space was also investigated. To this end the total energy was computed for the 9 layer slab using $3 \times 3 \times 1$, $4 \times 4 \times 1$ and $5 \times 5 \times 1$ grids resulting in values of −79.437, −79.445, and −79.446 eV, respectively. Accordingly, the $4 \times 4 \times 1$ grid was selected as sufficiently accurate and was used for all the remaining calculations.

A variety of terrace and step-containing models as constructed for the $CeO_2$(111) surface and a series of models containing oxygen vacancies were also considered. The first terrace model, hereafter denoted as **T1** (Terrace1) is defined by a $Ce_3O_6$ (1 × 1) unit cell; note that the surface unit cell consists just of one atom per layer. It is a regular stoichiometric $CeO_2$(111) 9 L slab with three upper relaxed layers (Figure 1a) and the initial unrelaxed structure was taken from the $CeO_2$ bulk optimized geometry ($a_0 = 5.39$ Å, LDA+U). The second terrace model, **T2** or Terrace2, is as **T1** but with the upper O layer atoms completely removed, resulting in a rather unstable termination (vide infra) and giving rise to a $Ce_3O_5$ (1 × 1) unit cell (see Figure 1b). Hence, the overall slab stoichiometry is $Ce_3O_5$ or equivalently $CeO_{1.67}$ ($Ce_2O_3 + CeO_2$) with formally 2 $Ce^{3+}$ and 1 $Ce^{4+}$ ions per unit cell. For the **T2** model, the two outermost atomic layers (top Ce layer and O layer just below it) were relaxed. Finally, **T3** or Terrace3 model arises also from **T1** but doubling it in the X direction (see Figure 1a) and with half of the upper O layer atoms removed leading to $(Ce_6O_{11})$ (2 × 1)

![](./images/811895985046290433_1.jpg)

Figure 1. Sketches of the optimized CeO₂(111) terrace surface slab models containing nine atomic layers: gray spheres, Ce cations; red spheres, O anions. Selected interatomic distances (dashed lines, italic font) in pm and topological (Bader) charges (solid lines, straight font) in a.u. Magnetic moments of individual atoms (in $\mu_B$) are also shown in parentheses for the cases where a spin polarized solution is found. (a) T1 model: Ce₃O₆ (1 × 1) unit cell, (b) T2 model derived from T1 with upper O layer atom removed, surface Ce₃O₅ (1 × 1) unit cell, (c) T3 model from doubling T1 and removing one of each two O layer in the topmost layer, Ce₆O₁₁ (2 × 1) unit cell.

(Figure 1c) and with formally $2\ Ce^{3+}$ and $4\ Ce^{4+}$ ions in the unit cell. In this way, the T1, T2, and T3 models represent stoichiometric and nonstoichiometric extended ceria surfaces with different surface terminations and hence different stability but without introducing morphological point defects. Since T2 and T3 introduce formally $Ce^{3+}$ ions, spin polarized calculations were always carried out to compare the effect of spin polariza- tion on the optimized geometries. The calculated results show that spin polarization does not significantly change the geo- metrical parameters; the largest effect being less than 1%. Bader charges forT2 and T3 were calculated for both spin restricted (SR) and spin polarized (SP) solutions. In this case, the results show that the Bader charges calculated at these different levels are different with changes in some cases reaching up to 9%. Then, geometry optimizations for every studied system was done at spin restricted level (SR) and with those geometries, electronic structure calculations at SP level in a single-point fashion were performed.

In order to examine the electronic structure of low-coordinated sites but without introducing at the same time any nonstoichi- ometry, different possible stoichiometric stepped slab surface models were built starting always from the planar CeO₂ (111) surface. Following the same notation used for the terrace models we refer to Ce₂₀O₄₀ (8 × 1) as S1 or Step 1 (Figure 2a). The notation above comes from the fact that this model is generated from the T1 by taking a 8 × 1 unit cell and removing 4 rows from the topmost layer, 4 from the second and 4 from the third resulting in a surface which is perpendicular to the <111> direction and with (1−10) Miller indexes. In a similar way S2 or Step 2 corresponds to Ce₂₀O₄₀ (8 × 1) and is derived from S1 by moving one O atom of the step to the opposite side of the step resulting now in two different surfaces (Figure 2b) at each side of the (111) terrace although without a single set of

![](./images/811895985046290433_2.jpg)

Figure 2. Sketches of the optimized step slab models of CeO₂(111) surface nine atomic layers thick: gray spheres, Ce cations; red spheres, O anions. Selected interatomic distances (dashed lines, italic font, pm) and topological (Bader) charges (solid lines, straight font, a.u.); in cases of open-shell systems magnetic moments of individual atoms (in $\mu_B$) are also shown in parentheses: (a) S1 model: (8 × 1), unit cell Ce₂₀O₄₀, (b) S2 model: (8 × 1), unit cell Ce₂₀O₄₀, derived from S1 by moving one O atom of the step to the opposite side of the step; (c) S3 model: (6 × 1), unit cell Ce₁₅O₃₀, (d) S4 model: (6 × 1), unit cell Ce₁₅O₃₀ derived from S3 by moving one O atom of the step to the opposite side of the step. Only the six upper layers are shown.

Miller indexes. Next, S3 or Step 3 may be defined by a Ce₁₅O₃₀ (6 × 1) unit cell and is also derived from T1 although in this case the lateral surface of the strip, which is also perpendicular to the <111> direction, corresponds to $(-211)$ or $(11-2)$ Miller planes forming angles of $30^{\circ}$ or $90^{\circ}$ with the $(1-10)$ one (Figure 2c). Note also that this (211)-type surface is nonpolar and thus stable, however less than those of types (111) or (110). Finally, S4 or Step4 model is derived from S3 by moving one O atom of the step to its opposite side. Note, that this may result in the generation of a formal $Ce^{3+}+O^{-}$ couple (Figure 2d) in a similar fashion as in S2, thus causing local nonstoichiometry. Neverthe- less, other distributions such as $Ce^{4+}+O^{2-}$ or $2Ce^{3+}+O^{0}$ are also in principle possible and, although intuition would suggest the formation of a $Ce^{3+}+O^{-}$ couple, the final outcome can only be obtained from reliable electronic structure calculations. Note that in these four stepped slab models the six upper atomic layers are fully relaxed.

The last series of models contains simultaneously steps (as morphological defects) and oxygen vacancies (as point defects). Hence, SV1 (Step/vacancy 1) may be represented by a Ce₂₄O₄₈ (8 × 2) units cell and is derived from S1 by doubling the cell and removing the lowest 3 layers (O−Ce−O) resulting in a 6 layer slab. Then one of the two O atoms of the step was moved far away on the lower terrace layer in such a way that each one of the oxygen vacancies thus created is now separated from its neighbor in the row by one O atom (Figure 3a). Note that, by construction, the resulting model preserves stoichiometry. In order to investigate the effect of nonstoichiometry, a second model, SV2 (Step/vacancy 2), is generated from SV1 by simply removing one of the two oxygen atoms of the step. Hence, each created O-vacancy is separated from its neighbor in the row by one O atom as in the case of the SV1 model. In this case the

![](./images/811895985046290433_3.jpg)

Figure 3. Sketches of the optimized step slab models of $CeO_2(111)$ surface six atomic layers thick: gray spheres, Ce cations; red spheres, O anions. Selected interatomic distances (dashed lines, italic font, pm) and topological (Bader) charges (solid lines, straight font, a.u.); in cases of open-shell systems magnetic moments of individual atoms (in $\mu_B$) are also shown in parentheses: (a) SV1 model: $(8 \times 2)$, unit cell $Ce_{24}O_{48}$, derived from S1 by doubling the cell and removing the lowest 3 layers (O-Ce-O); then one O atom of the 2 atoms of the step has been moved far on the 2nd layer terrace; (b) SV2 model: $(8 \times 2)$, unit cell $Ce_{24}O_{47}$, derived from SV1 by removing one O atom of the 2 atoms of the step; (c) SV3 model: $(8 \times 3)$, unit cell $Ce_{36}O_{71}$ derived from S1 by multiplying the cell by 3 (making it thicker) and removing the lowest 3 layers (O-Ce-O); then one O atom of the 3 atoms of the step has been removed.

unit cell is $Ce_{24}O_{47}\ (8 \times 2)$ (Figure 3b). Finally, SV3 (Step/vacancy 3) is derived from S1 by extending the slab in the $Y'$ direction by a factor of 3 (see Figure 2a) and removing the lowest 3 layers (O-Ce-O) resulting also in a 6 layer slab. Then one of the three oxygen atoms of the step was removed so that each created O-vacancy is now separated from its neighbor in the row by two O atoms (Figure 3c). It is worth mentioning that, in all the SV models, the step surface perpendicular to the terrace is that corresponding to the $(1-10)$ plane.

## 4. Results and Discussion

We start the discussion by inspecting the optimized structure of the terrace models and the corresponding electronic structure main features. For the T1 model, the present LDA+U geometry optimization (Figure 1a) indicates that the $CeO_2(111)$ is essentially unrelaxed, in agreement with previous findings. $^{40,42,77}$ Such a marginal relaxation is expected since the Ce atoms coordination number $(N_{Ce})$ is only reduced from 8 in the bulk to 7 in the terrace sites. The Bader charges for the Ce atoms in the second and deeper layer, computed from the GGA+U density, are ~2.4e and hence very close to those found for bulk $CeO_2,^{60}$ a small variation is found for the first layer Ce atoms, which display a slightly reduced charge of 2.3e. Figure 1a also reports charges for atomic oxygen but these follow the same trend as for bulk $CeO_2.^{60}$ Therefore, one can conclude that the electronic structure of the regular $CeO_2(111)$ surface is very similar to that of the bulk.

A different situation is found for the T2 model of the $CeO_2$ (111) surface (Figure 1b). In this case, the removal of the top layer of oxygen, leading to a fully reduced surface termination with 4-fold coordinated Ce atoms, results in a reorganization of the atomic and electronic structure of the two outermost layers, the Ce and O atoms relax so as to appear to be almost coplanar, the Ce atoms have their Bader charge divided by a factor of almost two whereas the O atoms preserve their charge. The resulting system may be regarded as a layer of CeO supported on $CeO_2(111)$ as expected from the stoichiometry. This is confirmed by the calculated magnetic moments on the Ce atoms of the top layer which are larger than one. Nevertheless, this seems to be a rather unrealistic surface termination because of its high polarity and the only purpose of describing it here is for comparison.

A more realistic representation of the partially reduced ceria surface is provided by the T3 model (Figure 1c). In this case one of each two O rows on the surface is removed leading to a surface model which is reminiscent of the missing row reconstruction models observed on several surfaces. $^{78}$ The effect on the atomic and electronic structure is also large, with Ce-Ce distance ranging from 364 to 400 pm compared to 382 pm for the bulk and also for the T1 model. Similarly, Ce-O surface distances exhibit a rather large dispersion with values in the 220-231 pm interval. The change in atomic structure is accompanied by significant change in the electronic structure with Ce atoms in the unit cell being clearly reduced. However, results show three types of Ce atoms instead of two, i.e., contrarily to what is expected from the unit cell stoichiometry: $4\ Ce^{4+}$ and $2\ Ce^{3+}$. The Bader charge permits to assign 3 Ce atoms in the unit cell clearly to $Ce^{4+}$, these three atoms have calculated Bader charge close to +2.4 which is similar to the value as found for bulk $CeO_2$ and are not especially labeled in Figure 1c. The Bader analysis and the calculated magnetic moments also allow us to assign two Ce atoms in the unit cell to nearly $Ce^{3+}$ cations; their Bader charge being ~+2.0 as found for bulk $Ce_2O_3$ and the calculated magnetic moments are ~0.6 $\mu_B$ also close to the values previously reported for bulk $Ce_2O_3$ $(0.96\ \mu_B).^{60}$ The remaining atom in the $Ce_6O_{11}(2 \times 1)$ unit cell of the T3 surface model appears to exhibit an intermediate oxidation state with a Bader charge of ~2.2e well midway between the value for $Ce^{4+}$ in bulk $CeO_2$ and that for $Ce^{3+}$ in bulk $Ce_2O_3$ and also with intermediate value for the magnetic moment $(0.4\ \mu_B)$. This result may seem counterintuitive since one expects two well defined $Ce^{3+}$ cations with localized magnetic moments. However, one must realize that the structure of the $Ce_6O_{11}(2 \times 1)$ unit cell has one Ce atom with $N_{Ce}=5$ and one with $N_{Ce}=6$, these are precisely the ones clearly identified as $Ce^{3+}$. A more localized solution can be obtained by further increasing the $U$ value although at the cost of loosing accuracy on the rest of calculated properties or of using different $U$ values for different properties as prescribed by Castleton et al. $^{29}$ but with the extra price of loosing predictive capability. Notice also that doubling the unit cell additionally in the $Y$ direction would allow for a larger degree of freedom in the electronic structure possibly resulting in a regular network of reduced $Ce^{3+}$ atoms interacting with each other through appropriate magnetic coupling between well localized 4f electrons on these reduced Ce atoms.

Nevertheless, the study of the magnetic coupling in this ideal reduced surface is not the purpose of the present work. In fact, the important point arising from this model is that it already allows us to show that reducing the $CeO_2(111)$ surface by removal of 50% of the topmost oxygen atomic layer implies a change of oxidation state on Ce atoms from +4 to +3 with significant localization of the additional electron, we will come back to this point later on. This result is not really surprising and could be anticipated from the known chemistry of ceria surfaces and ceria based catalysts. However, it allows us to have rather good confidence on the employed methodology and thus

![](./images/811895985046290433_4.jpg)

Figure 4. Electron localization function (ELF) maps for the T1 (a), T2 (b), and T3 (c) terrace surface models. The maps are drawn for a plane parallel to the surface. Ce atoms are assigned to $Ce^{4+}$ unless otherwise specified. O1 and O3 correspond to the first and third layer oxygen atoms respectively.

TABLE 1: Calculated Total Energy per $CeO_{2}$ Unit $(E_{CeO_{2}})$ and Formation Energy, $E_{f}$, Calculated at the GGA+U Level per Ce Atom with Respect to: $Ce(s) + 0.5(m/n) O_{2}(g) \to 1/n$ $Ce_{n}O_{m}$ of Ceria Systems under Scrutiny$^{a}$

<table>
<thead>
<tr>
<th>system</th>
<th>unit cell</th>
<th>$E_{CeO_{2}}$</th>
<th>$E_{f}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>bulk</td>
<td>$CeO_{2}$</td>
<td>$-25.21$</td>
<td>$-10.29$</td>
</tr>
<tr>
<td>T1</td>
<td>$Ce_{3}O_{6}$</td>
<td>$-24.90$</td>
<td>$-9.98$</td>
</tr>
<tr>
<td>T2</td>
<td>$Ce_{3}O_{5}$</td>
<td></td>
<td>$-8.40$</td>
</tr>
<tr>
<td>T3</td>
<td>$Ce_{6}O_{11}$</td>
<td></td>
<td>$-8.87$</td>
</tr>
<tr>
<td>S1</td>
<td>$Ce_{20}O_{40}$</td>
<td>$-24.68$</td>
<td>$-9.76$</td>
</tr>
<tr>
<td>S2</td>
<td>$Ce_{20}O_{40}$</td>
<td>$-24.61$</td>
<td>$-9.69$</td>
</tr>
<tr>
<td>S3</td>
<td>$Ce_{15}O_{30}$</td>
<td>$-24.73$</td>
<td>$-9.81$</td>
</tr>
<tr>
<td>S4</td>
<td>$Ce_{15}O_{30}$</td>
<td>$-24.47$</td>
<td>$-9.55$</td>
</tr>
<tr>
<td>SV1</td>
<td>$Ce_{24}O_{48}$</td>
<td>$-24.14$</td>
<td>$-9.22$</td>
</tr>
<tr>
<td>SV2</td>
<td>$Ce_{24}O_{47}$</td>
<td></td>
<td>$-9.25$</td>
</tr>
<tr>
<td>SV3</td>
<td>$Ce_{36}O_{71}$</td>
<td></td>
<td>$-9.30$</td>
</tr>
</tbody>
</table>

$^{a}$ All values are in eV.

analyze the oxidation state of low coordinated Ce atoms in a stoichiometric sample.

The analysis of the electronic structure of the terrace models described above is fully consistent with that arising from the ELF maps. Figure 4 reports the ELF maps in a plane parallel to the (111) surface. For the T1 model, the ELF maps (Figure 4a) show the typical form of $Ce^{4+}$ ions found in bulk $CeO_{2}.^{59}$ In a similar way, panels b and c in Figure 4 evidence the existence of reduced Ce atoms in the surface with ELF contours reminiscent to those found for bulk $Ce_{2}O_{3}.^{59}$

Before describing the various step surface models it is interesting to explore the relative stability of the three terrace surfaces just described. To this end, Table 1 reports the total energy of each model per $CeO_{2}$ unit which allows a direct comparison to the bulk. However, this quantity cannot be used for the nonstoichiometric models; hence we also computed the formation energy relative to a common reference such as gas phase $O_{2}$ and solid Ce: $O_{2}(g) + Ce(s)$. Results in Table 1 clearly show that the T1 terrace is the most stable one, followed by T2 and T3, as expected. On the other hand, from these values it is possible to obtain the energy cost to generate the perfect $CeO_{2}$ (111) surface from the bulk. The surface energy value is $\sim 0.55$ eV $(0.69$ J/m²) without relaxation and of $0.59$ eV $(0.73$ J/m²) with full relaxation for GGA+U with $U = 3$ eV, with this value being smaller than the LDA+U calculation $(\sim 0.81$ eV) reported in section 3 but closer to the GGA+U value $(\sim 0.45$ eV) of Jiang et al. $^{46}$ obtained using the PBE exchange- correlations potential. These authors found that the surface energy is rather insensitive to U and, hence, the difference between present and Jiang et al. values must be attributed to the different exchange-correlation functional used.

![](./images/811895985046290433_5.jpg)

Figure 5. Electron localization function (ELF) maps for the S1 (a), S2 (b), S3(c), and S4 (d) stepped surface models. The maps are drawnfor a plane perpendicular to the surface. Ce atoms are assigned to $Ce^{4+}$ unless otherwise specified.

Interestingly enough, the four step models depicted in Figure2 appear to be notably more stable than the reduced T2 and T3 surface models with values for both energy per $CeO_{2}$ unit and formation energy close to that of the perfect $CeO_{2}(111)$ surface represented by the T1 model. In addition, S1 and S3 appear to be more stable than S2 and S4 (Table 1), respectively, indicating that moving one oxygen row to the opposite site of the step, resulting in Ce atoms with smaller coordination and to maintain overall stoichiometry is not favored. This is clear from the optimized structures reported in Figure 2. Moreover, the difference between the energy of the perfect $CeO_{2}$ (111) surface and that of either T1 or stepped surface models provides a rough estimate of the formation energy of the respective stepped surfaces relative to that of $CeO_{2}$ (111). In this way we obtained GGA+U $(U = 3$ eV) values of 0.22, 0.29, 0.17, and 0.43 eV for S1, S2, S3, and S4, respectively, reinforcing our conclusion above and, in particular, the unfavored formation of S4, probably due to the local nonstoichiometry (see below).

All step models involve large geometrical rearrangementswith Ce-Ce distances which range from 357 pm in S1 to 415 pm in S2. This large geometrical effect does not change the topology of the resulting step although it considerably modifies the shape of the step when compared with the step cut from the bulk. For the S1, S2, and S3 models, the Bader charge on the Ce atoms varies between +2.14e and +2.36e suggesting that reduction to $Ce^{3+}$ is unlikely or at least sufficiently small so as to not allow for a well defined localized 4f density in the Ce atom with smaller charge. This is in line with the coordination number of these atoms which varies between 6 for Ce atoms at step edges and 7 for Ce atoms at the terraces and is further confirmed by the results of the spin polarized (SP) GGA+U calculations carried out for these models which, independently of the starting point, always converge to a solution without net magnetic moment. Hence, the variation in Bader charge from+2.29e for the Ce atoms near the perfect relaxed $CeO_{2}(111)$ model to +2.14e for the S2 models cannot be taken as indication of the existence of a significantly reduced Ce atom in this surface model. Note that the Bader charge for the Ce atoms near the perfect relaxed $CeO_{2}(111)$ which can serve as reference for surface Ce atoms in the oxidation state 4+ is +2.29 or already0.08e smaller than the value for the bulk (+2.3e7). Further arguments against the existence of largely reduced atoms in these stepped surfaces comes from inspection of the ELF maps reported in panels a-c in Figure 5 which always show ELF basins similar to those for the Ce atoms in the regular surface in Figure 1a. The only case where the ELF basin in Ce atoms shows a slight difference is for the low-coordinated atom in

the **S2** model, which indeed corresponds to the smallest Bader charge. Hence, one needs to conclude that in the eventuality that Ce atoms in these stepped surfaces acquire some extra charge, the resulting density is not enough to lead to a well localized 4f state. Results for the **S4** step fully confirm this finding. In fact, in the **S4** model, an O row has been moved from the step edge to the opposite site (Figure 5d). In this case, the spin polarized GGA+U calculations converge to a solution with nonzero magnetic moment precisely on the Ce atom which by construction is the one with the smallest coordination number ($N_\text{Ce} = 4$). Clearly this displacement is generating a local nonstoichiometry. The calculated magnetic moment of $0.48\ \mu_\text{B}$ is still smaller than the one found for bulk $\text{Ce}_2\text{O}_3$ ($0.96\ \mu_\text{B}$) although the Bader charge (+2.05e) is closer to the value for this bulk reference (+2.00e). Nevertheless, the ELF map in Figure 5d for the low-coordinated Ce atoms in the step edge is clearly different from that of the other Ce atoms and close to the shape of $\text{Ce}^{3+}$ atoms in nonstoichiometric ceria nanoparticles.⁵⁹ This is consistent with the picture emerging from the calculations for the electronic structure of the displaced O atom. The Bader charge of $-0.83$e is smaller than the $-1.15$e value corresponding to O atoms in bulk $\text{CeO}_2$ indicating the formation of a sort of $\text{O}^-$ species as expected from the formation of a $\text{Ce}^{3+}$ cation. At first sight one may think that this $\text{O}^-$ could exhibit a radical character but the absence of magnetic moment reveals that this is not the case.

A corollary of the previous discussion concerns the accuracy of the calculated Bader charges. The difference between the calculated values for the surface and bulk are probably due to the difficulty to numerically define the atomic basins. Another point of view is that the outer Ce atoms will collect all the density above the surface which might also origin from the inner Ce atoms, here a Hilbert space partitioning could give more "realistic" results than a spatial one. This is likely to be the case also for the low-coordinated atoms at the steps. Therefore, a small decrease on the calculated Bader charge on Ce atoms relative to the bulk $\text{CeO}_2$ reference cannot be taken as indication of partial reduction if this is not accompanied by the appearance of a nonzero magnetic moment and a concomitant difference in the ELF map. Nevertheless, an important conclusion emerges from the present study on models of stepped surfaces, namely that reduced Ce atoms can exist in stoichiometric $\text{CeO}_2$ samples. The existence of low coordinated Ce atoms seems to be enough to ensure that these are likely to be reduced to $\text{Ce}^{3+}$ although we also find $\text{Ce}^{3+}$ cations with quite large coordination number. This is at variance of results found for nonstoichiometric ceria nanoparticles where reduced $\text{Ce}^{3+}$ atoms tend to be located at the less-coordinated sites.⁵⁹,⁶⁰ Discussion of the electronic state of the oxygen is also of interest. Note that if there are $\text{Ce}^{3+}$ centers on stoichiometric surfaces one might also argue that reduced oxygen/oxidized $\text{O}^{2-}$ is also present leading to the existence of superoxide or peroxide species on these surfaces. The existence of such species has been proposed early on by some authors on the basis of IR and ESR spectroscopic techniques on polycrystalline samples or in $\text{CeO}_2$ based catalysts,⁷⁹⁻⁸³ and more recently it has been shown that cooperative effects between supported Au and $\text{CeO}_2$ lead to the formation of superoxide and peroxide intermediates at one-electron defect sites at the metal−support interface.⁸⁴ Indeed, for the **SV1** model, the O−O distance of $\sim1.4\ \text{Å}$ is reminiscent of that corresponding to a peroxo group. This is confirmed by the analysis of the Bader charges in the O which are nearly $-0.5$e indicating that a redistribution of the charge has occurred. This finding is in agreement with previous work of Huang and

![](./images/811895985046290433_6.jpg)

**Figure 6.** Electron localization function (ELF) maps for the **SV1** (a), **SV2** (b), and **SV3** (c) oxygen defective stepped surface models. The maps are drawn for a plane perpendicular to the surface. Ce atoms are assigned to $\text{Ce}^{4+}$ unless otherwise specified.

Fabris⁸⁵ showing that adsorption of O on $\text{CeO}_2(111)$ results in the formation of peroxo groups.

In order to examine the simultaneous effect of nonstoichiometry and reduced coordination we now discuss the results obtained for the **SV** models (Figure 3) which, as described above, arise from **S1** but introduce a different degree of nonstoichiometry by removing oxygen atoms in the **S1** model unit cell (as indicated in section 3). Results in Table 1 indicate that all the stepped surface models including those with oxygen vacancies are significantly less stable than the **S1** original step model but also less stable than any other of the surface models described so far. In addition, at first sight the order of stabilities corresponding to this family of models may appear quite strange since **SV1**, which is stoichiometric, is the least stable one. However, one must recall that in this case one oxygen vacancy is made in the $\text{Ce}_{24}\text{O}_{48}$ unit cell but the O atom removed from the step edge is deposited in the underlying terrace. Therefore, although the **SV1** model is stoichiometric by construction it contains de facto a local nonstoichiometry. On the other hand, the stability of the **SV2** and **SV3** models is very similar and follows the trend expected from their respective stoichiometry. The introduction of oxygen vacancies produces significant changes in the electronic structure, as it will be further mentioned below, but the overall atomic structure is reminiscent of that of the **S1** parent model. Analysis of the Bader charges shows, however, a more interesting picture. In fact, Figure 3 clearly shows that, while most of the Ce atoms in the unit cell have charges on the order of 2.34e and hence are tentatively assigned to $\text{Ce}^{4+}$, there are three Ce atoms located near the step edge with charges between +1.96e and 2.24e. Comparison to bulk values strongly indicates that the Ce atom with Bader charge $\sim+2.0$e should be assigned to $\text{Ce}^{3+}$. For the atoms with intermediate charge values it is not possible to deduce their oxidation states from this information only. Figure 3 also displays the relevant magnetic moments in the **SV** models obtained from spin polarized GGA+U calculations at their optimum (LDA+U) geometry. The existence of well defined magnetic moments in the Ce atoms with coordination number $N_\text{Ce}=5$ confirm the trend found for nanoparticles that $\text{Ce}^{3+}$ ions tend to occupy the low coordinated sites.⁵⁹,⁶⁰ Nevertheless, note that one Ce atom with $N_\text{Ce}=6$ and located near the edge also shows a noticeable reduced character. This interpretation is confirmed by the ELF plots in Figure 6 for the three different **SV** models although the differences in the ELF maps are almost unseen in the color scale used.

Before closing this discussion, it is important to remark that **SV1** is formally stoichiometric while both **SV2** and **SV3** can be regarded as containing two $\text{Ce}^{3+}$ ions. However, all indications point toward a description with one clear $\text{Ce}^{3+}$ cation and two partially reduced Ce atoms. At this point one must warn that it is not clear that the unit cells used in this work, even being at the limit of the present computational capabilities using large parallel supercomputers, are large enough to accommodate

the structural changes which accompany the simultaneous presence of more than one $Ce^{3+}$ in the unit cell. Hence, it is not possible to firmly conclude that the electronic structure of these ceria stepped surface models follows the trend expected from purely stoichiometric arguments or, as calculations seem to indicate, there are two different types of reduced Ce atoms: a first type of fully reduced ions and a second type of partially reduced cations. Nevertheless, recent work on large ceria nanoparticles, where the constraints mentioned above regarding the unit cell do not hold, also found partially reduced Ce atoms at edge sites. $^{60}$ Therefore, we conclude that this is likely to be the case here for the oxygen vacancy containing step model surfaces.

## 5. Conclusions
In this work periodic slab models have been constructed to represent ceria surfaces exhibiting step edges. A variety of stoichiometric and nonstoichiometric models of increasing complexity have been designed. The atomic and electronic structures of these surface models have been investigated by means of density functional theory based calculations using LDA+U and GGA+U exchange correlation potentials, respectively. The electronic structure has been explored using the topological Bader analysis, the calculated magnetic moments and the ELF maps.

For the perfect $CeO_{2}(111)$ surface, no significant differences are found with respect to the $CeO_{2}$ bulk, neither from the atomic geometrical parameters nor from the electronic structure. On the other hand, partially reduced $Ce^{3+}$ atoms as well as Ce atoms with intermediate oxidation state between $Ce^{3+}$ and $Ce^{4+}$ were found when the top oxygen atoms were removed from the surface leading to a Ce termination. In these cases, the degree of reduction on the surface Ce atoms appears to be strongly related to the coordination number of the surface Ce atoms which varies from $N_{Ce}=4$ to 6. Despite the fact that our conclusion about existence of partially reduced Ce atoms relies on the use of $U=3$ eV for the GGA+U calculations whereas the use of a larger U value would lead to more localized states, however the important conclusion here, namely that degree of reduction of the surface depends on the coordination of Ce atoms in the surface remains unaltered.

Two models for the most straightforward step formation on $CeO_{2}(111)$ have been evaluated, **S1/S2** and **S3/S4**, with the last ones being clearly more stable and thus being realistic models for steps on $CeO_{2}(111)$ surfaces which can serve as basis for further adsorption studies in computational heterogeneous catalysis.

For the slab models representing stepped surfaces a relatively large relaxation is predicted. However, the Ce atoms at the step edge tend to maintain the same oxidation state as in the perfect surface. The presence of low coordinated Ce atoms seems to be a sufficient but not necessary condition for the existence of $Ce^{3+}$ cations. Note that $Ce^{3+}$ cations are found with quite large coordination number. On the other hand, for the **S4** model, where one row of oxygen atoms from the side of the step are moved to the opposite side of the same while keeping the $CeO_{2}$ stoichiometry, we found evidence of reduced $Ce^{3+}$ atoms at the step edge. Hence, one may conclude that $Ce^{3+}$ ions may be present in extended stoichiometric $CeO_{2}$ samples as the energetic differences between this model and the perfect step model is rather low. Note, however, that the reduced $Ce^{3+}$ cations appear in a region of space which is locally nonstoichiometric provided the coordination number of these ions is sufficiently low. This is in agreement with recent findings for moderately large octahedral and cuboctahedral ceria nanoparticles $^{59,60}$

Finally, the models of stepped surfaces including a single oxygen vacancy always exhibit the presence of reduced Ce atoms although with a different degree of occupancy of the 4f one electron level. For these models, formal oxidation state arguments predict the existence of two $Ce^{3+}$ cations whereas the present density functional calculations show one $Ce^{3+}$ cations and two less reduced ones in the oxidation state between $Ce^{3+}$ and $Ce^{4+}$. Again, this may be due to the use of a too low U value in the GGA+U calculations, $^{29}$ which however is in line with previous findings for ceria nanoparticles. $^{59,60}$ Nevertheless, it is important to point out that larger unit cells which would allow for additional relaxation of the surface atoms may result in Ce atoms with a more defined oxidation state even using the present value of U.

To conclude, the present model study predicts that $Ce^{3+}$ atoms may exist even in stoichiometric extended ceria samples and that the presence of oxygen vacancies in stepped surfaces also induces the presence of $Ce^{3+}$ atoms. In both cases, the reduced atoms tend to occupy the sites with smallest possible coordination number. The degree of localization in these systems is clearly dependent on the choice of the computational method, and an unbiased full ab initio description of these systems seems to be still out of hand. In this respect note that Da Silva et al. $^{30}$ concluded that these studies focus on one of the most "difficult" elemental oxides in the periodic table, we fully agree with these authors. Nevertheless, the qualitative conclusions outlined above are firmly established. While the present conclusions are based on rather simplified models, the conclusions are general enough to be applicable to real samples. In this sense, note that these types of low-coordinated atoms are clearly apparent in STM images of ceria surfaces. $^{61}$

**Acknowledgment.** M.M.B. is grateful to CONICET-Argentina for making possible her stay at the Universitat de Barcelona. C.L. is grateful to the Alexander von Humboldt Foundation for a postdoctoral fellowship. This study has been supported by the Spanish Ministry of Education and Science (Grants CTQ2005-08459-CO2-01, UNBA05-33-001, HA2006-0102), by the Generalitat de Catalunya (Grants 2005SGR00697, 2005 PEIR 0051/69) and by the COST-D41 action. Computational time on the *MareNostrum* supercomputer of the Barcelona Supercomputing Center is gratefully acknowledged. The authors also wish to thank one of the reviewers for useful and pertinent remarks.

**Supporting Information Available:** Calculated structural and energetic parameters of selected studied systems. This material is available free of charge via the Internet at http://pubs.acs.org.

## References and Notes
(1) Fu, Q.; Saltsburg, H.; Flytzani-Stephanopoulus, M. *Science* **2003**, 301, 935.
(2) Rodriguez, J. A.; Ma, S.; Liu, P.; Hrbek, J.; Evans, J.; Perez, M. *Science* **2007**, 318, 1757.
(3) Trovarelli, A. *Catal. Rev.-Sci. Eng.* **1996**, 38, 439.
(4) Trovarelli, A. *Catalysis by Ceria and Related Materials*; Imperial College Press: London, 2002.
(5) Herschend, B.; Baudin, M.; Hermansson, K. *Surf. Sci.* **2005**, 599, 173.
(6) Bene, R.; Perczel, I. V.; Réti, F.; Meyer, F. A.; Fleisher, M.; Meixner, H. *Sens. Actuators B: Chem.* **2000**, 71, 36.
(7) Hibino, T.; Hashimoto, A.; Inohue, T.; Tokuno, J.; Yoshida, S.; Sano, M. *Science* **2000**, 288, 2031.
(8) Corma, A.; Atienzar, P.; Garcia, H.; Chane-Ching, J. Y. *Nat. Mater.* **2004**, 3, 394.
(9) Walkenhorst, A.; Schmitt, M.; Adrian, H.; Petersen, K. *Appl. Phys. Lett.* **1994**, 64, 1871.

(10) Nakazawa, T.; Inoue, T.; Satoh, M.; Yamamoto, Y. *Jpn. J. Appl. Phys.*, **1995**, 34, 548.

(11) Marabelli, M.; Wachter, P. *Phys. Rev. B* **1987**, 36, 1238.

(12) Guo, S.; Arwin, H.; Jacobsen, S. N.; Järrendahl, K.; Helmersson, U. *J. Appl. Phys.* **1995**, 77, 5369.

(13) Niwano, M.; Sato, S.; Koide, T.; Shidara, T.; Fujimori, A.; Fukutani, H.; Shin, S.; Ishigame, M. *J. Phys. Soc. Jpn.* **1988**, 57, 1489.

(14) Vesselei, M.; Kullman, L.; Granqvist, C. G.; Rottkay, N.; Rubin, M. *Appl. Opt.* **1998**, 37, 5993.

(15) Loschen, C.; Carrasco, J.; Neyman, K. M.; Illas, F. *Phys. Rev. B* **2007**, 75, 035115.

(16) Fabris, S.; de Gironcoli, S.; Baroni, S.; Vicario, G.; Balducci, G. *Phys. Rev. B* **2005**, 71, 041102.

(17) Kresse, G.; Blaha, P.; Da Silva, J. L. F.; Ganduglia-Pirovano, M. V. *Phys. Rev. B* **2005**, 72, 237101.

(18) Moreira, I. de P.R.; Illas, F.; Martin, R. L. *Phys. Rev. B* **2002**, 65, 155102.

(19) Illas, F.; Martin, R. L. *J. Chem. Phys.* **1998**, 108, 2519.

(20) Martin, R. L.; Illas, F. *Phys. Rev. Lett.* **1997**, 79, 1539.

(21) Muñoz, D.; Harrison, N. M.; Illas, F. *Phys. Rev. B* **2004**, 69, 085115.

(22) Franchini, C.; Bayer, V.; Podloucky, R.; Paier, J.; Kresse, G. *Phys. Rev. B* **2005**, 72, 045132.

(23) Petit, L.; Svane, A.; Szotek, Z.; Temmerman, W. M. *Phys. Rev. B* **2005**, 72, 205118.

(24) Gerward, L.; Olsen, J. S.; Petit, L.; Vaitheeswaran, G.; Kanchana, V.; Svane, A. *J. Alloys Compd.* **2005**, 400, 56.

(25) Svane, A.; Temmerman, W.; Szotek, Z. *Phys. Rev. B* **1999**, 59, 7888.

(26) Anisimov, V. I.; Aryasetiawan, F.; Lichtenstein, A. I. *J. Phys.: Condens. Matter* **1997**, 9, 767.

(27) Anisimov, V. I.; Solovyev, I. V.; Korotin, M. A.; Czyzyk, M. T.; Sawatzky, G. A. *Phys. Rev. B* **1993**, 48, 16929.

(28) Solovyev, I. V.; Dederichs, P. H.; Anisimov, V. I. *Phys. Rev. B* **1994**, 50, 16861.

(29) Castleton, C. W. M.; Kullgren, J.; Hermansson, K. *J. Chem. Phys.* **2007**, 127, 244704.

(30) Da Silva, J. L. F.; Ganduglia-Pirovano, M. V.; Sauer, J.; Bayer, V.; Kresse, G. *Phys. Rev. B* **2007**, 75, 045121.

(31) Becke, A. D. *J. Chem. Phys.* **1993**, 98, 1372.

(32) Becke, A. D. *Phys. Rev. A* **1988**, 38, 3098.

(33) Hay, P. J.; Martin, R. L.; Uddin, J.; Scuseria, G. E. *J. Chem. Phys.* **2006**, 125, 034712.

(34) Sayle, T. X. T.; Parker, S. C.; Catlow, C. R. A. *Surf. Sci.* **1994**, 316, 329.

(35) Sayle, T. X. T.; Parker, S. C.; Catlow, C. R. A. *J. Phys. Chem.* **1994**, 98, 13625.

(36) Conesa, J. C. *Surf. Sci.* **1995**, 339, 337.

(37) Vyas, S.; Grimes, R. W.; Gay, D. H.; Rohl, A. L. *J. Chem. Soc. Faraday Trans.* **1998**, 91, 427.

(38) Baudin, M.; Wójcik, M.; Hermansson, K. *Surf. Sci.* **2000**, 468, 51.

(39) Gotte, A.; Hermansson, K.; Baudin, M. *Surf. Sci.* **2004**, 552, 273.

(40) Skorodumova, N. V.; Baudin, M.; Hermansson, V. *Phys. Rev. B* **2004**, 69, 75401.

(41) Gennard, S.; Corá, F.; Catlow, C. R. A. *J. Phys. Chem. B* **1999**, 103, 10158.

(42) Yang, Z.; Woo, T. K.; Baudin, M.; Hermansson, K. *J. Chem. Phys.* **2004**, 120, 7741.

(43) Skorodumova, N. V.; Simak, S. I.; Lundqvist, B. I.; Abrikosov, I. A.; Johansson, B. *Phys. Rev. Lett.* **2002**, 89, 166601/1.

(44) Fabris, S.; de Gironcoli, S.; Baroni, S.; Vicario, G.; Balducci, G. *Phys. Rev. B* **2005**, 71, 75; 041102(R); 09.

(45) Kresse, G.; Blaha, P.; Da Silva, J. L. F.; Ganduglia- Pirovano, M. V. *Phys. Rev. B* **2005**, 72, 237101.

(46) Jiang, Y.; Adams, J. B.; van Schilfgaarde, M. *J. Chem. Phys.* **2005**, 123, 064701.

(47) Nolan, M.; Grigoleit, S.; Sayle, D. C.; Parker, S. C.; Watson, G. W. *Surf. Sci.* **2005**, 576, 217.

(48) Esch, F.; Fabris, S.; Zhou, L.; Montini, T.; Africh, C.; Fornasiero, P.; Comelli, G.; Rozei, R. *Science* **2005**, 309, 752.

(49) Scorza, E.; Birkenheuer, U.; Pisani, C. *J. Chem. Phys.* **1997**, 107, 9645.

(50) Ferrari, A. M.; Pacchioni, G. *J. Phys. Chem.* **1995**, 99, 17010.

(51) Pfau, A.; Schierbaum, K. D. *Surf. Sci.* **1994**, 321, 71.

(52) Mullins, D. R.; Radulovic, P. V.; Overbury, S. H. *Surf. Sci.* **1999**, 429, 186.

(53) Xiao, W.; Guo, Q.; Wang, E. *G. Chem. Phys., Lett.* **2003**, 368, 527.

(54) Henderson, M. A.; Perkins, C. L.; Engelhard, M. H.; Thevuthasan, S.; Peden, C. H. F. *Surf. Sci.* **2003**, 526, 1.

(55) Tsunekawa, S.; Ishikawa, K.; Li, Z.-Q.; Kawazoe, Y.; Kasuya, A. *Phys. Rev. Lett.* **2000**, 85, 3440.

(56) Zhang, F.; Chan, S.; Spanier, J. E.; Apak, E.; Jin, Q.; Robinson, R. D.; Herman, I. P. *Appl. Phys. Lett.* **2002**, 80, 127.

(57) Deshpande, S.; Patil, S.; Kuchibhatla, S.; Seal, S. *Appl. Phys. Lett.* **2005**, 85, 133113.

(58) Dutta, P.; Pal, S.; Seehra, M. S.; Shi, Y.; Eyring, E. M.; Ernst, R. D. *Chem. Mater.* **2006**, 18, 5144.

(59) Loschen, C.; Bromley, S. T.; Neyman, K. M.; Illas, F. *J. Phys. Chem. C* **2007**, 111, 10142.

(60) Loschen, C.; Migani, A.; Bromley, S. T.; Illas Neyman, K. M. *Phys. Chem. Chem. Phys.* **2008**, 10, 5730.

(61) Lu, J.-L.; Gao, H.-J.; Shaikhutdinov, S.; Freund, H.-J. *Surf. Sci.* **2006**, 600, 5004.

(62) Bader, R. F. W.; *Atoms in Molecules: A Quantum Theory*; Oxford Science: Oxford, U.K., 1990).

(63) Becke, A. D.; Edgecombe, K. E. *J. Chem. Phys.* **1990**, 92, 5397.

(64) Silvi, B.; Savin, A. *Nature* **1994**, 371, 683.

(65) Dudarev, S. L.; Botton, G. A.; Savrasov, S. Y.; Humphreys, C. J.; Sutton, A. P. *Phys. Rev. B* **1998**, 57, 1505.

(66) Vosko, S. H.; Wilk, L.; Nusair, M. *Can. J. Phys.* **1980**, 58, 1200.

(67) Perdew, J. P.; Chevary, J. A.; Vosko, S. H.; Jackson, K. A.; Pederson, M. R.; Singh, D. J.; Fiolhais, C. *Phys. Rev. B* **1992**, 46, 6671.

(68) Perdew, J. P.; Chevary, J. A.; Vosko, S. H.; Jackson, K. A.; Pederson, M. R.; Singh, D. J.; Fiolhais, C. *Phys. Rev. B* **1993**, 48, 4978.

(69) Raebiger, H.; Lany, S.; Zunger, A. *Nature* **2008**, 453, 763.

(70) Kresse, G.; Hafner, J. *Phys. Rev. B* **1993**, 47, 558.

(71) Kresse, G.; Furthmüller, J. *Phys. Rev. B* **1996**, 54, 11169.

(72) Blöchl, P. E. *Phys. Rev. B* **1994**, 50, 17953.

(73) Kresse, G.; Joubert, D. *Phys. Rev. B* **1999**, 59, 1758.

(74) Monkhorst, H. J.; Pack, J. D. *Phys. Rev. B* **1976**, 13, 5188.

(75) Duclos, S. J.; Vohra, Y. K.; Ruoff, A. L.; Jayaraman, A.; Espinosa, G. P. *Phys. Rev. B* **1998**, 38, 7755.

(76) Gerward, L.; Olsen, J. S. *Powder Diffr.* **1993**, 8, 127.

(77) Yang, Z.; Woo, T. K.; Hermansson, K. *Surf. Sci.* **2006**, 600, 4953.

(78) Ho, K. M.; Bohnen, K. P. *Phys. Rev. Lett.* **1987**, 59, 1833.

(79) Li, C.; Xin, Q.; Guo, X. X. *Catal. Lett.* **1992**, 12, 297.

(80) Zhang, X. L.; Klabunde, K. J. *Inorg. Chem.* **1992**, 9, 1706.

(81) Martinez Arias, A.; Soria, J.; Conesa, J. C. *J. Catal.* **1997**, 168, 364.

(82) Bulanin, K. M.; Lavalley, J. C.; Lamotte, J.; Mariey, L.; Tsyga- nenko, N. M.; Tsyganenko, A. A. *J. Phys. Chem. B* **1999**, 102, 6809.

(83) Binet, C.; Daturi, M.; Lavalley, J. C. *Catal. Today* **1999**, 50, 207.

(84) Guzman, J.; Carrettin, S.; Fierro-Gonzalez, J. C.; Hao, Y.; Gates, B. C.; Corma, A. *Angew. Chem., Int. Ed.* **2005**, 44, 4778.

(85) Huang, M.; Fabris, S. *Phys. Rev. B* **2007**, 75, 081404.

JP806066G