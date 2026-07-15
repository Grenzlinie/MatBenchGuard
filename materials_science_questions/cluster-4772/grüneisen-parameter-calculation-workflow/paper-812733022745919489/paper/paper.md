# On the role of intermolecular vibrational motions for ice polymorphs I: Volumetric properties of crystalline and amorphous ices

Cite as: J. Chem. Phys. 151, 114501 (2019); https://doi.org/10.1063/1.5119748
Submitted: 13 July 2019 . Accepted: 16 August 2019 . Published Online: 18 September 2019

Hideki Tanaka, Takuma Yagasaki, and Masakazu Matsumoto

## COLLECTIONS

EP This paper was selected as an Editor's Pick

![](./images/812733022745919489_1.jpg)

![](./images/812733022745919489_2.jpg) ![](./images/812733022745919489_3.jpg) ![](./images/812733022745919489_4.jpg)

---

## ARTICLES YOU MAY BE INTERESTED IN

Can clathrates heterogeneously nucleate ice?
The Journal of Chemical Physics 151, 114707 (2019); https://doi.org/10.1063/1.5119823

Dependence of a cooling rate on structural and vibrational properties of amorphous silicon: A neural network potential-based molecular dynamics study
The Journal of Chemical Physics 151, 114101 (2019); https://doi.org/10.1063/1.5114652

Experimental validation of interpolation method for pair correlations in model crystals
The Journal of Chemical Physics 151, 114502 (2019); https://doi.org/10.1063/1.5116176

![](./images/812733022745919489_5.jpg)

J. Chem. Phys. 151, 114501 (2019); https://doi.org/10.1063/1.5119748
151, 114501

© 2019 Author(s).

# On the role of intermolecular vibrational motions for ice polymorphs I: Volumetric properties of crystalline and amorphous ices

Cite as: J. Chem. Phys. 151, 114501 (2019); doi: 10.1063/1.5119748
Submitted: 13 July 2019 • Accepted: 16 August 2019 •
Published Online: 18 September 2019

![](./images/812733022745919489_6.jpg) ![](./images/812733022745919489_7.jpg) ![](./images/812733022745919489_8.jpg)

Hideki Tanaka,ᵃ and Takuma Yagasaki, and Masakazu Matsumoto

## AFFILIATIONS

Research Institute for Interdisciplinary Science, Okayama University, Okayama 700-8530, Japan

ᵃE-mail: htanakaa@okayama-u.ac.jp

## ABSTRACT

Intermolecular vibrations and volumetric properties are investigated using the quasiharmonic approximation with the TIP4P/2005, TIP4P/Ice, and SPC/E potential models for most of the known crystalline and amorphous ice forms that have hydrogen-disordering. The ice forms examined here cover low pressure ices (hexagonal and cubic ice I, XVI, and hypothetical dtc ice), medium pressure ices (III, IV, V, VI, XII, hydrogen-disordered variant of ice II), and high pressure ice (VII) as well as the low density and the high density amorphous forms. We focus on the thermal expansivities and the isothermal compressibilities in the low temperature regime over a wide range of pressures calculated via the intermolecular vibrational free energies. Negative thermal expansivity appears only in the low pressure ice forms. The sign of the thermal expansivity is elucidated in terms of the mode Grüneisen parameters of the low frequency intermolecular vibrational motions. Although the band structure for the low frequency region of the vibrational density of state in the medium pressure ice has a close resemblance to that in the low pressure ice, its response against volume variation is opposite. We reveal that the mixing of translational and rotational motions in the low frequency modes plays a crucial role in the appearance of the negative thermal expansivity in the low pressure ice forms. The medium pressure ices can be further divided into two groups in terms of the hydrogen-bond network flexibility, which is manifested in the properties on the molecular rearrangement against volume variation, notably the isothermal compressibility.

© 2019 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/1.5119748

## I. INTRODUCTION

Since the discovery of two amorphous states of water called low density amorphous (LDA) and high density amorphous (HDA) ices, which are expected to transform mutually via a first order-like phase transition, supercooled water has attracted substantial attention where the coexistence of two liquid phases has been the main concern.¹⁻⁵ According to the recent view, there can be two distinct phases of liquid water in the deeply supercooled state.⁶ The two phases are known as low density liquid (LDL) and high density liquid (HDL), though they are metastable. Liquid water freezes into crystalline ice in a very short period at temperatures near and below the homogeneous nucleation temperature, ~232 K.⁷⁻⁹ The liquid-liquid critical point is believed to exist between that temperature and the glass transition temperature of 136 K.¹⁰⁻¹³ We have examined the phase behaviors and the potential surfaces pertinent to individual states.¹⁴⁻¹⁶ The existence of the thermodynamically distinct two phases has been confirmed by some sophisticated methods⁶ although we are unable to access the liquid-liquid coexistence by conventional experiments. It could, however, also be assured by a more direct manner such as molecular dynamics (MD) simulations of the coexistence of the two phases,¹⁷ and a peculiar property of LDL was reported.¹⁸

The two liquid water states were known to have different relaxation processes other than the thermodynamic and structural properties, and the temperature dependence of the relaxation time is quite different from each other.⁴⁵ LDL is classified into a strong liquid whose viscosity is well described with the Arrhenius-type

equation, whereas HDL falls into a category of a fragile liquid obeying the Vogel-Tammann-Fulcher equation. $^{13}$

In addition to the two amorphous solids, there are at least 18 crystalline ice polymorphs as stable and metastable states including low pressure cubic ice (Ic), which have been regarded as a disordered stacking form of hexagonal ice (Ih). $^{19,20}$ All those structures are more or less dominated by four hydrogen-bonds around each central water molecule. The low density state, either LDA or LDL, is believed to have properties similar to low pressure ice Ih. Each water molecule in LDA is tetrahedrally coordinated with a small number of defects and its hydrogen-bond network resembles ice I. $^{21}$ On the other hand, HDA (HDL) has a density close to ice III or V. $^{22}$ It is intriguing to examine typical thermal properties of various ice forms in terms of their chemical potentials and to pursue similarity in thermal and structural properties between crystalline and amorphous ices.

In this paper, ice Ih, Ic, XVI, $^{23}$ and a hypothetical ice dtc $^{24-26}$ bearing a close analogy to one of the zeolites are called low pressure ices, in which water molecules form firm and tetrahedrally coordinated hydrogen-bonds with adjacent molecules. $^{22}$ In the phase diagram, ices II, III, V, and VI occupy the intermediate pressure region and ices IV and XII $^{27}$ are metastable phases found in this pressure region. They are called medium pressure ices. The unit cell of either ice form is a little complicated and there exist a variety of hydrogen-bond network patterns. Ice VII is a high-pressure phase consisting of two independent ice Ic frameworks that interpenetrate but are not hydrogen-bonded to one another; each water molecule thus has eight near neighbors but only forms hydrogen bonds to half of them.

In a previous paper, we examined the interaction energy at 0 K (cohesive energy), hydrogen-bond strength for both hydrogen-ordered ice II and the hypothetical disordered counterpart, ice IId. $^{28}$ A little stronger hydrogen-bond stabilizes ice II rather than ice IId. Here, our main focus will be placed on the thermodynamic properties associated with the locations of oxygens. Therefore, we restrict ourselves to hydrogen-disordered ice Ih, Ic, IId, III, IV, V, VI, VII, XII, XVI, and dtc ice along with two amorphous ices, LDA and HDA, as our target ice forms, although some of them are metastable under cryogenic conditions.

Negative thermal expansivity, which is observed for ice Ih at low temperatures, can be an indication of the nearly perfect tetrahedral coordination. (Thermal expansivity refers to volume expansivity throughout the present work. The linear expansivity may depend on the crystallographic axis. Comparison of the linear expansivities with experimental observations can be interesting, but we reserve it as a future work.) $^{29-33}$ In fact, it is also observed for C, Si, and Ge. $^{34,35}$ The expansivities of diamond and silicon have been calculated. $^{36,37}$ A quasiharmonic approximation has been developed to calculate the temperature dependence of the molar volume for ice $^{38-41}$ and clathrate hydrate, $^{42}$ the latter of which is a solid solution with a random occupation of its cages by guest species. It was revealed that the solid solution does not exhibit the negative thermal expansivity at all despite the fact that the corresponding framework without guest species, ice XVI, does. The calculated volumetric properties of clathrate hydrates under cryogenic conditions agree with experiment. $^{23}$

The thermal properties of ice have been investigated by other methods than the quasiharmonic approximation such as ab initio calculations and the path integral method that are useful to examine the isotope effects and to take account of the anharmonic contributions in cryogenic conditions. $^{43-46}$ On the other hand, the classical force field is meritorious in handling a large number of hydrogen-disordered ice structures and even amorphous states. In addition, the quasiharmonic approximation provides good agreement in volumetric properties of ice Ih, II, and III with the path integral calculation in which the anharmonic vibrational contribution is taken into account. $^{39}$ Encouraged by their successful application of the quasiharmonic approximation to several ice forms, we take advantage of the merit to explore various kinds of hydrogen-disordered crystalline ices and amorphous solids.

It is well known that the low frequency modes corresponding mostly to bending motions of three hydrogen-bonded molecules are responsible for the negative thermal expansivity of ice Ih (and also Ic). $^{38}$ The negative Grüneisen parameters of those modes and their relatively large contributions to the mode heat capacity at low temperatures below 60 K give rise to the negative thermal expansion of those ices. $^{38}$ Those modes may disappear or change their character by compression, and consequently, the negative thermal expansivity is expected to be no longer observed in ice polymorphs, except for the low pressure ice phases. In this paper, we will examine the Grüneisen parameters of the ice phases of the low, medium, and high pressure ices. It is of great interest to explore whether the negative thermal expansivity is observed for LDA whose local structure is similar to ice Ih or Ic.

The free energy and molar volume, which are easily calculated by the quasiharmonic approximation, also provide a way to estimate the isothermal compressibility. This property seems to be determined mainly by the interaction energy at temperature 0 K, and therefore, a fairly good agreement of the isothermal compressibility by the quasiharmonic approximation with classical MD simulations is expected. The temperature dependence of the isothermal compressibility for various ice forms is calculated and compared with MD simulations or experiments to characterize the response of the pressure against the volume variation, which is related to a kind of flexibility in the hydrogen-bond network for the individual ice form.

This paper is organized as follows: The theoretical and computational methods developed and used are described in Sec. II. The thermodynamic and structural properties of crystalline and amorphous ices are investigated in Sec. III, focusing on the appearance of the negative thermal expansivity under cryogenic conditions and the magnitude of the isothermal compressibility in various ice forms including amorphous solids. Our conclusions along with future work are remarked in Sec. IV.

## II. METHOD
### A. Intermolecular interaction for water and generation of crystalline ice structures

The intermolecular interaction is described by the TIP4P/2005 model, which has been known to be one of the best potential models to reproduce the phase behaviors of water including fluid states unless the pressure is extremely high. $^{26,47-51}$ We also calculate the volumetric properties by substituting TIP4P/Ice $^{52}$ or SPC/E $^{53}$ for TIP4P/2005, although some ice forms do not appear in the phase diagram of the SPC/E model. $^{54}$

The Gibbs free energy is given using $\langle V \rangle$ as

$$
G(T,p,N_\mathrm{w}) = A(T,\langle V \rangle,N_\mathrm{w}) + p\langle V \rangle. \tag{8}
$$

This is called the quasiharmonic approximation. The Gibbs free energy (chemical potential) of any ice form is obtained as a function of temperature and pressure.

The configurational entropy values, $S_\mathrm{r}$, in amorphous ices are unknown. We can, however, assume that an amorphous configuration is trapped in a potential energy basin and a hopping to one of the adjacent basins is a rare event when the temperature is lower than the glass transition temperature. $^{63}$ It is reasonable under this condition to expect that the free energy can be formulated in the same way as crystalline ices with an appropriate configurational entropy which depends only weakly on temperature and volume. The configurational entropy corresponding to the number of basins is much larger than the Pauling's approximate value given by Eq. (4). The glass transition temperature of LDL is reported to lie around $136\ \mathrm{K}.^{10-13}$ The LDL below that temperature can be the amorphous solid, LDA. Similarly, HDL below a certain temperature is HDA where structural relaxation is slow enough. $^{64}$ Figure S1 of the supplementary material presents the mean square displacements (MSDs) of liquid or amorphous water calculated from the MD simulations. We find that there is no diffusion below $100\ \mathrm{K}$. It suggests that thermodynamic properties obtained on the basis of Eq. (3) are reliable assuming that the configurational entropy is left a constant times $N_\mathrm{w}$ in a narrow range of molar volumes and at temperatures lower than $100\ \mathrm{K}$ and depends only on the type of amorphous form, LDA or HDA, generated by the MD simulations. Thus, we apply the quasiharmonic approximation with a constant but unknown configurational entropy to calculate some derivatives of the chemical potential for LDA and HDA at temperatures below $100\ \mathrm{K}$. The free energies for LDA and HDA at $0\ \mathrm{K}$ are correctly calculated since the entropy term vanishes.

## III. RESULTS AND ANALYSIS

### A. LDL and HDL structures from MD simulations

The potential energy and the pressure of liquid water obtained from the MD simulations are plotted against the density in Fig. 1.

![](./images/812733022745919489_9.jpg)

The almost constant pressure between $0.96$ and $1.12\ \mathrm{g\ cm}^{-3}$ at $180\ \mathrm{K}$ suggests the coexistence of the two liquid phases. The LDL transforms into the HDL around $150\ \mathrm{MPa}$ accompanying a fairly large increase in density. The density region between $0.96$ and $1.12\ \mathrm{g\ cm}^{-3}$ at $180\ \mathrm{K}$ has been identified with the coexistence of LDL with HDL by spontaneous separation of the two liquid phases in MD simulations. $^{17}$ The potential energy has a minimum value at a certain density in the region of LDL. Further decompression of the coexisting LDL or compression of the HDL increases its potential energy. Water at 200 or $220\ \mathrm{K}$ undergoes substantial but continuous change in pressure.

The structure factors, $S(k)$, of liquid water at $180\ \mathrm{K}$ are plotted in Fig. 2, which reveal the correlation in atomic position between two oxygen atoms as defined for a system composed of $N_\mathrm{w}$ water molecules by

$$
S(k) = \left\langle \frac{\left| \sum_{j} \exp(i\mathbf{k} \cdot \mathbf{r}_{j}) \right|^{2}}{N_\mathrm{w}} \right\rangle, \tag{9}
$$

where $\mathbf{r}_{j}$ is the position of the $j$th oxygen atom. It is noted that the first sharp diffraction peak around $k = 1.8$ is replaced by the peak at a higher wave number around $k = 2.2$ as LDL transforms into HDL. Another peak, though not so distinct, grows at a lower wave number around $k = 0.25$ in the density region of the coexistence of the two liquid phases, suggesting a phase separation between LDL and HDL in a large scale inside the simulation box.

Each water molecule in LDL has an almost perfect and long-ranged tetrahedral coordination while HDL is allowed to have a substantial deviation from 4-coordination. $^{21}$ Now, it is widely accepted that the so-called $q$-parameter measures the tetrahedrality in a simple manner. $^{65}$ Figure 3 plots the $q$-parameter of water molecules along the MD trajectory as a function of density at $T = 180$, 200, and $220\ \mathrm{K}$. We pay attention to only the case of the two-phase coexistence for the later analysis, i.e., $T = 180\ \mathrm{K}$. Its density dependence in the LDL state is not so distinct, but it is remarkable in the HDL state. The $q$-parameter of LDL has a lower limit constrained from a nearly perfect hydrogen-bond network, which must be closer to unity as observed in ice Ih or Ic structure. However, there may be no such limit and high pressure undermines the network structure of

![](./images/812733022745919489_10.jpg)

HDL up to a fairly high density. A harsh slope in the middle density region is due to the mixing of the two phases whose $q$-parameters are mutually different.

### B. Potential energy of the quenched structure of each phase

We compare the potential energy of the quenched structure, $U_{\rm q}$, for various crystalline and amorphous ices as a function of volume in Fig. 4. This is the most dominant contribution to the free energy for the low and medium pressure ice phases. Ice Ih has the lowest energy, and the energy for ice XVI (empty CS-II hydrate) is higher by roughly $1\ \rm kJ\ mol^{-1}$, which causes the free energy difference between the two phases. The energy increases with increasing the ice index from III to VII for the stable ice phases (ice IV is metastable). Distortion of hydrogen-bonds in the medium density region results in the higher energy values for ices from IId to ice VI (hydrogen-ordered ice II has lower energy than the disordered one by about $1\ \rm kJ\ mol^{-1}$).$^{28}$ There is a large gap in the molar volume between ice Ih at $19\ \rm cm^3\ mol^{-1}$ and those of the medium pressure ice phases ranging from 13 to $15\ \rm cm^3\ mol^{-1}$. The gap in the molar volume must arise from the balance between the potential energy and the $pV$ term. The potential energy difference between ice Ih and the medium pressure ice phases can be compensated only by a large volume contraction from ice Ih since the vibrational free energy does not make a serious difference. However, this does not necessarily mean that there is no metastable ice structure having the molar volume between 15 and $19\ \rm cm^3\ mol^{-1}$. Although ice VII has much higher potential energy than ice VI and its difference amounts to a few $\rm kJ\ mol^{-1}$, it is stable at very high pressures so that the $pV$ term makes up for the difference in the interaction energy.

### C. Intermolecular vibrational motions

Because the thermal expansivity and the isothermal compressibility are associated with the vibrational free energy, the vibrational

![](./images/812733022745919489_11.jpg)

**FIG. 3.** The tetrahedrality parameter, $q$, of water molecules in the instantaneous structures against the density at $T=180$ (circles), 200 (triangles), and 220 (crosses) K. There are three regions at 180 K, LDL (light blue), HDA (red), and the coexistence of them (black). The three straight lines are guides to the eye.

![](./images/812733022745919489_12.jpg)

**FIG. 4.** Potential energies of the quenched structures against the molar volume for all the crystalline and amorphous ices examined. The curve for ice Ic overlaps completely with that of ice Ih. The curve for ice IV almost overlaps with that for ice XII.

motion in ice deserves a detailed scrutiny. The distribution of the vibrations is expressed by the density of states (DOS), which is a function of frequency in the collective coordinates for intermolecular vibrational motions. Each molecular motion is composed of translational and rotational ones. Although a collective coordinate is a linear combination of translational and rotational variables of all the molecules, a difference in the time scale of those motions can separate the individual vibrational modes into the translation-dominant and rotation-dominant bands. The separation of the DOS of ice Ih into the translation-dominant band below $300\ \mathrm{cm}^{-1}$ and the rotation-dominant band above $550\ \mathrm{cm}^{-1}$ is perfect as shown in Fig. 5(a). The DOSs for all the ice forms examined here are shown in Fig. S2 of the supplementary material. The low pressure ices Ic and XVI have features similar to ice Ih. The DOSs of the medium to high pressure ice forms are also separated, as depicted in Figs. 5(b)-5(d). The bands lower than $100\ \mathrm{cm}^{-1}$ in the medium pressure ice forms bear resemblance to those in ice Ih. The low frequency modes remain in ice IId, III, V, and XII. The shape in this frequency region for either ice IV or VI is different from that in any other medium pressure ice forms (Fig. 5 and Fig. S2 of the supplementary material). The prominent peak below $100\ \mathrm{cm}^{-1}$ is almost missing in ice VII, and the separation between the translation-dominant and rotation-dominant bands is blurred as compression proceeds.

The high frequency modes around $1000\ \mathrm{cm}^{-1}$ grow in high pressure ice VII [Fig. 5(d)]. A distinct split into two peaks is seen in ice XVI in the high frequency region [Fig. S2(j) of the supplementary material]. Apparently, HDA has a similar DOS as LDL though LDA is closer to ice Ih (Ic). The calculated DOSs of ice Ih and V are in fairly good agreement with those obtained from neutron scattering experiments.⁶⁶

The separation of the DOS into the high and low frequency bands is not clear in the two amorphous ices compared with ice Ih [Fig. 5(a)]. The separation of the normal mode frequencies is seemingly associated with complete decoupling between the rotational and translational types of motions in collective coordinates. However, the classification of each collective coordinate into either type of motions is not the case even for any crystalline ice form. In fact, mixing of the two types of motions turns out to be not negligible as explained below in conjunction with imaginary modes and some properties derived from the vibrational frequencies.

The modes around $50\ \mathrm{cm}^{-1}$ are the bending modes of three hydrogen-bonded molecules in ice Ih and can also be responsible for the negative thermal expansivity below 60 K in low pressure ices. Those modes appear even in ice III and HDA, as shown in Fig. 5(b). However, the mode frequency of any medium pressure ice form has

![](./images/812733022745919489_13.jpg)

a different dependence on volume from that of the low pressure ice phases. Figure S3 of the supplementary material compares the DOSs for those ices each at two molar volumes, one corresponds to the pressure at 100 K in Table I and we choose the other volume at which the DOS is considerably different in each ice form, to see the rough trend. Compression gives rise to a blue shift in any band for the DOS in the frequency region around $300\ \mathrm{cm}^{-1}$, which is the normal behavior of intermolecular vibrational modes. While the modes around $50\ \mathrm{cm}^{-1}$ are insensitive to the volume contraction in the medium pressure ices, they exhibit a red shift in the low pressure ices including LDA. Although the whole shape in the DOS for HDA looks quite similar to that for LDA at a given volume, the variation against the volume is different. The frequency in the rotation-dominant band also shifts to the higher side upon compression. This shift is less distinct in the rotation-dominant band of ice VII and the gap almost vanishes at a high compression state [Fig. S3(l) of the supplementary material]. This may be related to a plastic state in the high pressure region. $^{67,68}$

### D. Imaginary modes

In the case of instantaneous structures of LDL and HDL, some of the mode frequencies are imaginary, indicating that the curvature of the potential surface is partially negative. The imaginary modes may lead to a passage from one potential basin to another on the potential energy surface, but most of them simply indicate that there are some inflection points. For display of imaginary modes, a minus sign is attached to each imaginary frequency instead of imaginary unit.

![](./images/812733022745919489_14.jpg)

FIG. 6. Percentage of imaginary modes at T = 180, 200, and 220 K.

![](./images/812733022745919489_15.jpg)

FIG. 7. Density of states of (a) LDL and (b) HDL for instantaneous structures at 100 MPa and those of (c) ice Ih at 100 MPa and (d) ice III at 300 MPa with (solid lines) and without (dotted lines) the translation-rotation coupling in the Hessian matrix.

The percentage of the number of imaginary modes of liquid water at 180, 200, and 220 K is plotted against the density in Fig. 6. It is reasonable to consider that the increase in such modes is associated with the increase in the number of defects in the hydrogen-bond network. In LDL, the number of the imaginary modes is apparently correlated with the tetrahedrality quantified by the $q$-parameter shown in Fig. 3. The number of the imaginary modes in HDL is rather irrelevant to the density (pressure) although it is dependent on temperature. Some cancellation between the density and the tetrahedrality may occur. In fact, the region in the DOS for imaginary modes stretches to lower frequency (in the present notation) with increasing density while the number of imaginary modes around $-50\ \text{cm}^{-1}$ decreases [see Figs. 7(a) and 7(b)].

The normal modes of the translational and rotational motions can be calculated separately removing their coupling. To this end, the Hessian matrix is reduced to a block diagonal matrix, $\mathbf{K}_\text{b}$, consisting only of two smaller matrices corresponding to the translational part, $\mathbf{K}_\text{tt}$, and the rotational part, $\mathbf{K}_\text{rr}$; each of them is of rank $3N_\text{w}$, as

$$
\mathbf{K}_\text{b} = \begin{pmatrix}
\mathbf{K}_\text{tt} & \mathbf{0} \\
\mathbf{0} & \mathbf{K}_\text{rr}
\end{pmatrix} \tag{10}
$$

and $\mathbf{K}_\text{tt}$ and $\mathbf{K}_\text{rr}$ are diagonalized individually. The DOSs of instantaneous structures of LDL and HDL for these matrices are plotted in Figs. 7(a) and 7(b). Figure S4 of the supplementary material shows the percentage of the imaginary modes with the separate diagonalization. The number of imaginary modes decreases significantly for both LDL and HDL in separated diagonalization, roughly a factor of 1/10. The separated diagonalization causes a fairly large blue shift of the modes below $500\ \text{cm}^{-1}$ and a small red shift above that frequency. The opposite shift of the modes above $500\ \text{cm}^{-1}$ is simply the consequence of the invariance of the trace of the Hessian matrix ($\mathbf{K}$ and $\mathbf{K}_b$).

## E. Molar volume of crystalline and amorphous ices

The molar volume of an amorphous state obtained from Eq. (7) depends on the density of the MD simulation used to generate the configurations, $d$. The gap in the molar volume of LDA between two initial densities ($d = 0.92$ and $0.96\ \text{g}\ \text{cm}^{-3}$) according to Eq. (7) remains to be around $0.5\ \text{cm}^3\ \text{mol}^{-1}$ upon compression as shown by light blue curves in Fig. 8. Those of HDA (red curves) are also constant, roughly $1\ \text{cm}^3\ \text{mol}^{-1}$. Although the absolute value depends on $d$, the pressure dependence of the molar volume (its temperature dependence as well) is almost the same for all the $d$ values. We hereafter show only two representative amorphous structures quenched from liquid states of $d = 0.96$ and $1.12\ \text{g}\ \text{cm}^{-3}$, which can coexist at 180 K and around $p = 150\ \text{MPa}$.

![](./images/812733022745919489_16.jpg)

FIG. 8. Molar volume calculated with the quasiharmonic approximation against the pressure at 0 K for LDA (light blue) and HDA (red) whose densities in the MD simulation are specified by $d$ in $\text{g}\ \text{cm}^{-3}$ together with the molar volume for ice Ih (blue) and III (green).

Because the anharmonic contribution becomes negligible at low temperatures, the chemical potential values of ices obtained from the quasiharmonic approximation are reliable below 100 K. Drawing a detailed phase diagram based on the calculated chemical potential values is outside the scope of the present study and we restrict our interest to the limited range in the $p$-$T$ space. The chemical potential values at 0 K are plotted against the pressure in Fig. 9. The dominant component to the chemical potential of water is either the potential energy of the quenched structure, $U_q$, at low pressures or the $pV$ term at high pressures. Although the stable forms of ice at this temperature are of the hydrogen-ordered ones, the chemical potential values at 0 K provide a clue to the stable phases at higher temperatures as compression proceeds. Substitution of ice Ih for medium pressure ice VI occurs around several hundred megapascals since ice II is not considered here. Another transition between ice VI and VII can be expected around 2 GPa by extending the two chemical potential curves.

There is a definite intersection between the LDA and HDA chemical potential curves. This does not provide a direct evidence for coexistence of the two distinct phases, but HDA can replace LDL around 200 MPa according to the chemical potential values at 0 K accompanying a volume jump of $2.8\ \text{cm}^3\ \text{mol}^{-1}$. This pressure is close to that of the plateau in the isotherm at 180 K in Fig. 1(a).

![](./images/812733022745919489_17.jpg)

FIG. 9. Chemical potentials of crystalline ice Ih, III, VI, VII and amorphous ice LDA and HDA against the pressure at 0 K.

![](./images/812733022745919489_18.jpg)

FIG. 10. (a) Molar volume against the pressure at 0 K and (b) relative molar volume to the value at 0 K for ice Ih, Ic, XVI, LDA, and HDA at 100 MPa, III at 300 MPa, V at 500 MPa, XII at 700 MPa, VI at 1.5 GPa, VII at 7 GPa, and dtc at 0.1 MPa as a function of temperature.

The molar volumes of crystalline and amorphous ices at low temperatures are obtained from the chemical potentials. The pressure dependence of the volume for crystalline and amorphous ices at 0 K is plotted in Fig. 10(a). There is a fairly large gap in molar volume between ice Ih and any of the medium pressure ice phases, which is expected from Fig. 4.

The anomalous thermal expansivity at low temperatures is well known in ice Ih. Then, questions arise as to whether other ice polymorphs have the negative thermal expansivity, how large it is in LDA compared with ice Ih (if any), and what causes the difference in the sign of thermal expansivity at low temperatures.

The temperature dependences of the molar volume difference from those at 0 K are shown in Fig. 10(b). The volume decreases with heating for ice Ih, XVI, and LDA below 60 K at a constant pressure. This behavior is not seen in HDA. The hypothetical ice, dtc, has a much larger volume and its volume change against the temperature is even more distinct than ice Ih.

The thermal expansivities of various ices are plotted in Fig. 11(a). Negative thermal expansivity is observed for ices Ih, Ic, XVI, and dtc ice. The calculated thermal expansivity of ice Ih is close to the experimental one as shown in Fig. 11(b). Agreement is excellent in the low temperature regime.³¹ The temperature that the thermal expansivity is minimum locates around 40 K for ice Ih and XVI. (The curve for ice Ic overlaps completely with that of ice Ih.) It shifts to a lower temperature side in LDA and is not so pronounced compared with the three crystalline forms. The experimental thermal expansivity of ice II is positive even at temperatures close to 0 K,⁶⁹ which agrees with our calculation for ice IId in the framework of the quasiharmonic approximation and with the previous calculation.³⁹ Moreover, any ice phase other than the low pressure ones has positive thermal expansivity. Thus, we can expect that the non-negative expansivity is true even for HDA. The thermal expansivity of ice III is fairly smaller than either of ice V or XII. This trend in the magnitude between ice III and V is also obtained from the MD simulations (Table SI of the supplementary material).⁷⁰ The thermal expansivity in dtc ice has its minimum around 35 K, a little lower than any of the other low pressure ice forms.

### F. Thermal expansivity and Grüneisen parameter

The thermal expansivity $\alpha = \left(\frac{\partial \ln V}{\partial T}\right)_p$ is related to the Grüneisen parameter, $\gamma = \sum_j C_j \gamma_j / \sum_j C_j$, as

$$
\alpha = -\left(\frac{\partial \ln V}{\partial p}\right)_T\left(\frac{\partial p}{\partial T}\right)_V = -\kappa_T \frac{\partial^2 A}{\partial T \partial V} = \kappa_T C_V \gamma V^{-1}, \tag{11}
$$

![](./images/812733022745919489_19.jpg)

FIG. 11. (a) Thermal expansivity calculated from the quasiharmonic approximation against the temperature for ice Ih, Ic, XVI, LDA, and HDA at 100 MPa, III at 300 MPa, V at 500 MPa, XII at 700 MPa, VI at 1.5 GPa, and VII at 7 GPa. (b) Comparison of the calculated (solid lines) thermal expansivities at 0.1 and 100 MPa with the experimental one (dotted line) for ice Ih at 0.1 MPa.

which has a different sign between these two quantities at low tem- peratures along with those of LDA and ice Ih. In order to examine this peculiar behavior in ice III, V, and HDA in more detail, we calculate the following quantity, $\zeta$, the displacement ratio for either hydrogen-oxygen or oxygen-oxygen atoms defined as

$$
\zeta = \frac{l - l_0}{\lambda l_0}, \tag{18}
$$

where $l_0$ stands for the mean distance between two atoms over the four hydrogen-bonded neighbors at volume $V_0$ and $l$ indicates the mean distance upon change of the volume to $V = V_0(1 + \lambda)^3$. If ice expands or shrinks uniformly, it is unity. In Table II, the dis- placement ratio, $\zeta$, and $q$-parameters are also listed. The displace- ment ratio is remarkably small for ice III, V, and HDA. A peculiar behavior in ice III and V is associated with significant molecular rearrangements in the course of the volume variation, which we expect to cause the decrease in the interaction energy. To examine this, we choose the volume at which the average quenched energy has a minimum for each ice form (see Fig. 4). The interaction energy is calculated for the configuration where the center of mass coordi- nates are simply scaled from the chosen volume while the orienta- tions are left unchanged. Figure S5 of the supplementary material plots these energy values against the molar volume as well as the quenched energies shown in Fig. 4. A large discrepancy in ice III (and less distinctly in V) is found between those two energy val- ues. In those two ice forms as well as HDA, the coordinates must be adjusted in accordance with the volume change. The coordi- nates in the other ice forms do not vary against the molar volume change.

Contraction or expansion hardly causes rearrangement of molecules in the perfect tetrahedral arrangement ice structures, i.e., ice Ih, Ic, and VII. By contrast, hydrogen-bonds in ice III, V, and HDA are distorted substantially and water molecules can adjust themselves against the change of the volume, as is manifested by the small $\zeta$ values. This effect, represented by the second term in Eq. (17), is large and contributes to recover the positive thermal expansivity for the medium pressure ice phases III and V. Despite that the orientation of each molecule in ice IId deviates significantly from the tetrahedral one as is evident from the $q$-parameter value, this ice structure does not undergo structural rearrangements in the process of volume change, i.e., $\zeta$ is close to unity. The same trend is also found in ice IV, VI, and XII. The distribution of the vibrational motions (DOS) in either ice VI or VII is different from that of the low pressure ice forms and those modes contributing to the negative thermal expansivity are missing as shown in Fig. 5 and Fig. S2 of the supplementary material. Therefore, no anomalous behavior in the thermal expansivity is observed in those ices even with only the first term in Eq. (17).

Calculations similar to $C_V \gamma$ are carried out for each block diago- nal matrix defined by Eq. (10). Such a Grüneisen parameter denoted by $C_V \gamma_b$ is listed in Table II. The decoupling of the translational and rotational motions influences the DOS as depicted in Fig. 7(c) to increase the mode frequencies that contribute to the negative ther- mal expansivity. $^{38}$ As a result, the vibrational free energy with the virtual decoupling eliminates the negative thermal expansivity from the low pressure ice forms.

The thermal expansivities at 0.1 and 100 MPa for ice Ih are plotted in Fig. 11(b). The negative thermal expansivity is more dis- tinct at higher pressures as far as the tetrahedral coordination is preserved in ice Ih. This originates from a quadratic nature of the frequency against the volume expansion (negative curvature), whose mode Grüneisen parameters are negative. It is anticipated that those anomalous mode frequencies should be leveled off or decrease at the limit of expansion while maintaining the tetrahedral arrangement of water molecules.

The comparison of the thermal expansivities from the quantum free energies with those from the classical ones [calculated with the classical vibrational free energy given by Eq. (6) instead of Eq. (5)] are depicted in Fig. S6 of the supplementary material. There is a large discrepancy between the quantum and classical treatments in any ice form. Despite those discrepancies at low temperatures, the relative magnitudes in the expansivity agree with those from the classical free energies.

The averaged $\gamma_j C_j$ at $T = 30$ K in each frequency bin with a size of $10\ \text{cm}^{-1}$ is plotted in Fig. 13. The mode Grüneisen parame- ters of the low frequency region below $100\ \text{cm}^{-1}$ in ice Ih and LDA are anomalously negative as well as ice Ic and XVI, while those of the higher frequency region are all positive. Since the heat capacity of a low frequency mode below $100\ \text{cm}^{-1}$ is relatively large at low temperatures [see Eq. (12)], the quantity $\gamma_j C_j$ in the low frequency

![](./images/812733022745919489_20.jpg)

FIG. 13. Frequency dependent Grüneisen parameter times mode heat capacity, $\gamma_j C_j$, at $T = 30$ K for (a) ice Ih (blue), LDA (light blue), and HDA (red), and (b) ice Ic (blue), III (green), V (magenta), VI (orange), and VII (purple).

region dominates and consequently $\gamma C_{\mathrm{v}}=\sum_{j} \gamma_{j} C_{j}$ is negative. This is what is observed in ice Ih and LDA as plotted in Fig. 13(a). The heat capacities of higher frequency modes become increasingly dominant with raising temperature and $\gamma C_{\mathrm{v}}$ turns to be positive. In the case of HDA, a small region having negative $\gamma_{j} C_{j}$ is found around $40 \mathrm{~cm}^{-1}$. However, it is always canceled by the positive one in the lower frequency side. No frequency region having negative $\gamma_{j} C_{j}$ is practically found in any ice form other than the low pressure ones as shown in Fig. 13(b).

### G. Isothermal compressibility

The isothermal compressibility (the inverse of the bulk modulus), $\kappa_{\mathrm{T}}$, for each ice structure is calculated from the chemical potential. Those of the typical ice polymorphs are depicted in Fig. 14 obtained from the quantum free energies. Each of ice Ih, XVI, and dtc ice has a large thermal compressibility. The compressibility for either of the low pressure ice form is dependent to some extent on the temperature. Its dependence for the medium pressure ice is smaller. Ice VII is the hardest to be compressed. Ice III has a large compressibility compared with ice Ih irrespective of its higher density, which has also been observed by the path integral calculation. $^{39}$

Table SI of the supplementary material tabulates those properties for ices III and V from experiments $^{69,71}$ and MD simulations. $^{70}$ A little larger compressibility has been observed by experiment and the MD simulations. The difference may be associated in part with the anharmonic contribution and/or the partial hydrogen-ordering. $^{72}$

We reveal, however, the large isothermal compressibility in ice III is obtained within the framework of the quasiharmonic approximation. Since the bulk modulus, $\kappa_{\mathrm{T}}{ }^{-1}$, is calculated from the Helmholtz free energy as

$$
\kappa_{\mathrm{T}}^{-1}=V\left(\frac{\partial^{2} A}{\partial V^{2}}\right)_{T, N_{\mathrm{w}}},
$$

its magnitude for each ice polymorph at $T=0 \mathrm{~K}$ is simply obtained from the curvature of the sum of the interaction energy and the zero-point vibrational energy. The bulk modulus at that temperature is roughly (exactly according to the classical mechanics) estimated from the plot of the interaction energy against the molar volume in Fig. 4. A close scrutiny indicates that the interaction energy in ice III changes rather sluggishly against the volume variation compared with any other form of the medium pressure ices. This has a direct bearing on the large isothermal compressibility of ice III. It is noted that ice III has a curvature as small as any medium pressure ice form as drawn in Fig. S5 of the supplementary material (dotted lines) even in the case of the simple scaling of the center-of-mass coordinates associated with the volume change. Ice III seems to be unique and ice $\mathrm{V}$ is marginal among the medium pressure ice forms as is manifested in the isothermal compressibility.

The discrepancy in the compressibility between the quantum and the classical treatments is rather small compared with the thermal expansivity as shown in Fig. S6 of the supplementary material. The differences in the low temperature regime are a little large in the low pressure ice forms. Its magnitude decreases with increasing temperature. The gap is much smaller in either ice VI or VII. Unlike the compressibility, the difference in the thermal expansivity seems to be affected mainly by the difference in the heat capacity since the heat capacity depends on the mechanics on which calculation of the free energy is based.

### H. Model dependence

Figure S7 of the supplementary material compares the volumetric properties of ice Ih, III, V, and VII calculated with the TIP4P/2005, TIP4P/Ice, and SPC/E water models. The obtained thermal expansivity and isothermal compressibility depend somewhat on the model potentials. However, the order of the magnitude in each property among the ice forms is common to the TIP4P/2005, TIP4P/Ice, and SPC/E models.

## IV. CONCLUDING REMARKS

We investigate the volumetric properties of crystalline and amorphous ices in a wide range of pressures and at temperatures below $200 \mathrm{~K}$ with a reliable intermolecular interaction model for water, TIP4P/2005, in order to examine similarities and differences between those ices. The free energy of ice at low temperatures can be systematically calculated with the quasiharmonic approximation once the intermolecular vibrational mode frequencies are known. This allows us to estimate the equilibrium volume and its derivatives.

The negative thermal expansivity, one of the anomalies for ice Ih, Ic, XVI, and dtc ice in cryogenic conditions, is also found for LDA. The thermal expansivity is positive at any temperature for HDA and the medium pressure ice phases. The negative thermal expansivity for the low pressure ice forms is explained by the negative mode Grüneisen parameters at low frequencies around $50 \mathrm{~cm}^{-1}$. In HDA, ice III and V, the rearrangement of each molecule associated with volume change plays a crucial role to eliminate the anomaly: if this effect is neglected in the calculation, their thermal expansivities turn to be negative at low temperatures. The non-negative thermal expansivity is also obtained for ice IId, IV, VI, VII, and XII.

![](./images/812733022745919489_21.jpg)

FIG. 14. Isothermal compressibility calculated from the quasiharmonic approximation against the temperature for ice Ih and XVI at 100 MPa, IId at 400 MPa, III at 300 MPa, V at 500 MPa, VI at 1.5 GPa, and VII at 7 GPa together with the hypothetical dtc ice at 0.1 MPa.