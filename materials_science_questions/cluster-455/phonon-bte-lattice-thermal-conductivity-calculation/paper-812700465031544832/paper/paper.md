# Thermoelectric transport properties of (Ti₁–cAlc)NiSn half-Heusler alloy

Daniel Rabin, *ab Theodora Kyratsi, David Fuks and Yaniv Gelbstein b

The influence of Al on the thermoelectric properties of the half-Heusler (HH) TiNiSn compound is reported. The research combined ab initio Density Functional Theory (DFT) calculations with experimental microstructure evaluation and measurements of the transport properties up to 750 K. It is shown that Al addition to the Ti sub-lattice results in an increase of the absolute value of the Seebeck coefficient and electrical resistivity in polycrystalline TiNiSn, while preserving the n-type behavior of the ternary compound, in addition to a significant reduction of the thermal conductivity. In (Ti₀.₉₉Al₀.₀₁)NiSn, upon 1% Al substitution of Ti, an improvement of 17% in the thermoelectric figure of merit (0.42 at 723 K) compared to pure TiNiSn was observed. Theoretical lattice thermal conductivity calculations are applied to shed light on the different scattering mechanisms in this class of materials. It is shown that the major contribution to the lattice thermal conductivity reduction is stimulated by the presence of Sn-rich inclusions, in addition to an influence of mass fluctuation scattering due to substitution of Ti by Al. Although it is shown that in the widely applied polycrystalline TiNiSn, an addition of the acceptor Al dopant could not fully compensate n-type electronic active defects (e.g. grain boundaries) for obtaining p-type materials, the currently reported results pave a route for thermoelectric optimization of MNiSn (M = Ti, Ni, Sn) n-type half-Heusler compounds.

## 1. Introduction

Half-Heusler (HH)¹ alloys are promising materials for high temperature thermoelectric applications. The most common n- and p-type HH compounds are MNiSn (M = Ti, Ni, Sn) – and MCoSb (M = Ti, Ni, Sn) – based, respectively.²,³ Beyond their electronic properties, HHs are also attractive for such applications due to their suitable mechanical properties and chemical stability. HH has a cubic (F$\overline{4}$3m, Space group #216) crystallographic structure, containing four interpenetrating face-centered cubic sub-lattices, where one of them is empty.

Due to shortage in HH based p-type materials, there is an ongoing search for new compositions.³⁻⁷ In our previous work⁸ we suggested Al substituting for Ti as the potentially possible element for achieving p-type TiNiSn. An ab initio Density Functional Theory (DFT) calculation of electronic density of states (DOS) showed that such substitution in single-crystal TiNiSn results in a p-type conductivity. This research was focused on finding the solubility limit of Al in (Ti₁–cAlc)NiSn alloy, using CALPHAD thermodynamic modeling combined with DFT calculations and an experimental validation. It was estimated that the maximal solubility of Al in TiNiSn is ~1 at% at 1400 K.

The efficiency of thermoelectric (TE) materials is defined by the TE figure-of-merit (ZT), as shown in eqn (1).

$$
ZT = \frac{\alpha^{2}}{\kappa\rho}T \tag{1}
$$

where, $\alpha$ is the Seebeck coefficient, $\rho$ is the electrical resistivity, $\kappa$ is the thermal conductivity, and $T$ is temperature. The thermal conductivity is a sum of both electronic ($\kappa_{\text{e}}$) and lattice ($\kappa_{\text{l}}$) contributions, $\kappa = \kappa_{\text{e}} + \kappa_{\text{l}}$. When designing new TiNiSn⁹⁻¹² in particular or MNiSn (M = Ti, Ni, Sn) in general¹³⁻¹⁶ based TE materials, there is a special interest for reducing the high lattice thermal conductivity in order to achieve maximal $ZT$. This can be obtained using different scattering mechanisms; e.g. phonon-phonon, mass fluctuation, grain boundaries and inclusions.⁵,¹⁰,¹⁷⁻¹⁹ In order to study the influence of each mechanism, theoretical calculations can be applied, as was shown specifically for the MNiSn (M = Ti, Ni, Sn) system, in a recent work.¹⁸

In the current research, the influence of Al doping on the transport properties of TiNiSn was investigated, using theoretical and experimental methods. The (Ti₀.₉₉Al₀.₀₁)NiSn composition with Al substituting for Ti was chosen in order to preserve a HH single phase condition and to check the change in the lattice thermal conductivity caused by such doping. The sample characterization included the microstructure evaluation and the measurements of the electronic and thermal properties up

---

^a NRCN, P.O. Box 9001, Beer-Sheva 84190, Israel. E-mail: daniel.rabin7@gmail.com
^b Department of Materials Engineering, Ben-Gurion University of the Negev, Beer-Sheva 84105, Israel
^c Department of Mechanical and Manufacturing Engineering, University of Cyprus, Kallipoleos 75, Nicosia 1678, Cyprus

to 750 K. *Ab initio* DFT calculations are applied in order to examine the influence of Al addition on $\kappa_{\mathrm{l}}$. The role of microstructure of the alloy in the reduction of the lattice thermal conductivity is also discussed.

The originality of the paper is in combination of DFT calculations with quasi-harmonic approximation in lattice dynamics aimed to calculate thermodynamic and kinetic parameters to predict the influence of small amount of doping element on the lattice thermal conductivity and figure of merit of thermoelectric materials. We also carry out a comparative analysis of the role of secondary phases on reduction of the lattice thermal conductivity of Al doped TiNiSn and highlight the significance of high temperature mass fluctuations by calculations and measurements.

## 2. Experimental

$(Ti_{0.99}Al_{0.01})$NiSn alloy was synthesized using arc-melting furnace under argon atmosphere, the alloy was re-melted five times. The as-cast ingots were meshed into powder using metallic pestle and mortar, the powder was cold pressed into ingots that were re-melted to ensure homogeneity. Following re-melting, powder was similarly prepared and subjected to heat treatment at 1163 K for one week under argon atmosphere for phase stabilization. The heat treatment temperature was chosen according to previous study of TiNiSn.⁹ Subsequently, a hot-press process was carried out during 1 hour in 1273 K under the pressure 51 MPa to achieve nearly fully-dense materials. The density was measured using Archimedes method.

The crystal structure was analyzed using X-ray powder diffraction (XRD; Panalytical Empyrean) and GSAS-II software package (Argonne National Labs, DuPage, Illinois).²⁰ The microstructure was examined using scanning electron microscope (SEM, JEOL 5600) with energy-dispersive spectroscopy (EDS). The Seebeck coefficient $(\alpha)$ and the electrical resistivity $(\rho)$ were measured using LSR apparatus (Linseis LSR-3/800). The thermal diffusivity was measured using LFA apparatus (Laser Flash Analysis 457, NETZSCH).

## 3. Computational details

DFT using the Full Potential method with the Linearized Augmented Plane Waves (FP-LAPW) formalism, as implemented in the WIEN2k code²¹,²² was applied in all calculations. The full description of the calculation details can be found in our previous work.⁸ The DFT calculations included the generalized gradient approximation (GGA). GGA functionals can underestimate band gaps, and an alternative way to correct this situation is by using hybrid functionals or similar methods. DFT + Hubbard $U$ for solids have been shown to actually give better electronic properties than semi-local GGA methods, as discussed for example, in.²³,²⁴ Although previous work²⁵ demonstrated that the results of calculations of the electronic properties of Ni-containing compounds can be improved by including a $U$ factor (or application of hybrid functionals), studies of the TiNiSn based alloys using GGA-based DFT methods¹¹,¹² excellently fit the experiments results. For the pure TiNiSn compound, a unit cell containing 3 atoms had been used, while for the (Ti,Al)NiSn alloys a $2\times2\times2$ cubic supercell with 96 atoms was used. The accuracy in the total energy calculations for all considered cases was not less than $\sim10^{-4}$ Ryd.

## 4. Lattice thermal conductivity

The way to calculate the lattice thermal conductivity²⁶⁻³⁰ for a unit cell with more than one atom was suggested in,²⁶ and is presented by the following equation:

$$
\kappa_{\mathrm{l}}=10^{2} \cdot A \frac{\bar{M} \Theta_{\mathrm{D}}^{3} \delta^{\frac{1}{3}}}{\gamma^{2} n^{\frac{2}{3}} T}\left[\mathrm{~W} \mathrm{~m}^{-1} \mathrm{~K}^{-1}\right] \tag{2}
$$

where a primitive unit cell is considered, and $n$ is the number of atoms in this cell, (for TiNiSn, $n=3$); $\bar{M}$ is the average mass of the atoms in atomic mass units; $\delta$ is the volume per atom in $\mathring{A}^{3}$; $\Theta_{\mathrm{D}}$ is the Debye temperature in K; $\gamma$ is the Grüneisen parameter and the constant $A$ is given by the expression $A=\frac{2.43 \times 10^{-8}}{\left(1-\left(\frac{0.514}{\gamma}\right)+\left(\frac{0.228}{\gamma^{2}}\right)\right)}$.²⁶ This method for calculating the lattice thermal conductivity was applied for thermoelectric materials with simple structures (rocksalt, zinc blende and wurtzite) in ref. 28, and for more complex thermoelectric materials²⁹ including HH compounds.³⁰

The Debye temperature is expressed in the form (see, for example ref. 31)

$$
\Theta_{\mathrm{D}}=\frac{h}{k_{\mathrm{B}}}\left[\frac{3 \delta}{4 \pi}\right]^{1 / 3} \cdot v_{\mathrm{m}} \tag{3}
$$

where $v_{\mathrm{m}}$ is the average sound velocity, $h$ is Planck constant, $k_{\mathrm{B}}$ is Boltzmann constant, and $\delta$ is in $m^{3}$. $v_{\mathrm{m}}$ is given by the following equation³²

$$
v_{\mathrm{m}}=\left[\frac{1}{3}\left(\frac{2}{v_{\mathrm{t}}^{3}}+\frac{1}{v_{\mathrm{l}}^{3}}\right)\right]^{-1 / 3} \tag{4}
$$

where $v_{\mathrm{t}}$ and $v_{\mathrm{l}}$ are transverse and longitudinal sound velocities

$$
v_{\mathrm{t}}=\left(\frac{G}{d}\right)^{1 / 2}, \quad v_{\mathrm{l}}=\left(\frac{3 B+4 G}{3 d}\right)^{1 / 2}, \tag{5}
$$

and $B$, $G$, and $d$ are the bulk and shear modulus, and the density, respectively.

For TiNiSn, the discussed in ref. 33 relation, $G=0.59B$ was applied. It was previously demonstrated to be satisfied for TiNiSn.⁸,¹²

Grüneisen parameter can be calculated in several ways.³⁴ Jia *et al.*²⁸ suggested the relation presented by eqn (6).

$$
\gamma=\sqrt{\left[\left(\gamma_{\mathrm{L}}\right)^{2}+2\left(\gamma_{\mathrm{S}}\right)^{2}\right] / 3}, \tag{6}
$$

where the longitudinal, $\gamma_{\mathrm{L}}$, and shear, $\gamma_{\mathrm{S}}$, Grüneisen parameters are given by eqn (7).

$$
\gamma_{\mathrm{L}}=-\frac{1}{2} \frac{V}{B+\frac{4}{3} G} \frac{\partial\left(B+\frac{4}{3} G\right)}{\partial V}-\frac{1}{6}, \quad \gamma_{\mathrm{S}}=-\frac{1}{2} \frac{V}{G} \frac{\partial G}{\partial V}-\frac{1}{6}, \quad(7)
$$

It may be shown that with the linear dependence $G \sim B$ as for TiNiSn $\gamma_{\mathrm{S}}=\gamma_{\mathrm{L}}=\frac{1}{2} B_{0}{ }^{\prime}-\frac{1}{6}$, where $B_{0}{ }^{\prime}=\frac{\mathrm{d} B}{\mathrm{~d} P}$ if the Murnaghan equation of state $^{35}$ is used. In this case Grüneisen parameter can be expressed as:

$$
\gamma=\sqrt{\frac{\left[\left(\gamma_{\mathrm{L}}\right)^{2}+2\left(\gamma_{\mathrm{S}}\right)^{2}\right]}{3}}=\frac{1}{2} B_{0}{ }^{\prime}-\frac{1}{6} \quad(8)
$$

This expression for the Grüneisen parameter coincides with that of Slater. $^{36}$ The discussion about other differently deter mined Grüneisen parameters having the form $\gamma=a B_{0}{ }^{\prime}-b$ are also discussed in ref. 34.

In order to take into account the phonon scattering mechanisms additional to the described above phonon-phonon interaction in TiNiSn matrix, the following general definition of the thermal lattice conductivity $^{37}$ had been used:

$$
\kappa_{\mathrm{l}}=\frac{1}{3} C v_{\mathrm{s}} l=\frac{1}{3} C v_{\mathrm{s}}^{2} \tau \quad(9)
$$

where, $C$ is the heat capacity per unit volume, $l$ is the mean free path for phonons, $v_{\mathrm{s}}$ is the average sound velocity and $\tau$ is the relaxation time. The heat capacity was taken equal to $3 R$ ( $R$ - gas constant) per atom according to the Dulong-Petit formula.

This approach allows accounting different scattering mechanisms in the material, as discussed in the introduction. The effects of the presence of secondary-phase inclusions, such as $\mathrm{TiNi}_{2} \mathrm{Sn}$, Sn containing compounds and pure $\mathrm{Sn}$, on the lattice thermal conductivity can be described using the relaxation time, shown in eqn (10).

$$
\frac{1}{\tau}=\frac{1}{\tau_{\text {matrix }}}+\frac{1}{\tau_{\text {inclusions }}} \quad(10)
$$

As was demonstrated for TiNiSn $^{12}$ and in accordance with, $^{17}$ the relaxation time due to inclusions can be calculated by eqn (11).

$$
\frac{1}{\tau_{\text {inclusions }}}=\frac{3}{2} \frac{x}{R} v_{\mathrm{s}} \quad(11)
$$

where, $x$ and $R$ are the volume fraction and radius of the inclusions.

## 5. Results and discussion
### 5.1. Experimental results
Fig. 1 presents the XRD spectra of the arc-melted, AM, $(Ti_{0.99} Al_{0.01}) NiSn$ alloy and the same after heat treatment, HT, and hot-pressing, HP. The obtained phases are the same as previously reported for TiNiSn obtained with similar experi- mental procedures; $^{8,9}$ the as-cast structure includes the HH TiNiSn phase (MgAgAs, Space group #216) and other phases that formed in the solidification process (i.e. $TiNi_{2} Sn(MnCu_{2} Al$,(\#)TiNiSn, (*) $TiNi_{2} Sn$ , (\&) $Ti_{6} Sn_{5}$ , (\$) $Sn$

![](./images/812700465031544832_1.jpg)

Fig. 1 XRD spectra of the $(Ti_{0.99} Al_{0.01}) NiSn$ alloy following arc-melting(AM), heat treatment (HT) at $1163 ~K$ for 1 week and hot-pressing (HP). Themiller indexes for the TiNiSn phase are presented, the angles range is $2 \theta=$ 20°-90°.

Space Group \#225), $Ti_{6} Sn_{5}$ (Space group \#163) and pure Sn(BCT, Space group #141)), while the heat treatment stabilizes the main $HH$ phase with a remaining residual pure $Sn$ phase. The analysis of the HT + HP XRD spectrum showed a lattice parameter of 5.935 [ $\AA$ ] for the TiNiSn phase, isotropic crystallite size $(D_{iso })$ of $4.73[\mu m]$ and micro strain of $3924[\times 10^{-6}]$ . The dislocation density $\delta=212.7[\times 10^{-3}]$ was found using the
$$\text { relation } \delta=\frac{1}{D_{\text {iso }}[\mu \mu]} \cdot{ }^{38}$$

The SEM micrographs of the final consolidated sample(Fig. 2) show a structure of $HH$ matrix with scattered Sn-containing inclusions. A magnification of a specific area displays the presence of the $Ni_{3} Sn_{4}$ , Sn containing phase, in a lower amount than the XRD detection limit. This binary compound was probably formed during the solidification process because at the temperatures corresponding to this process in our experiments the two-phase mixture of this phase with liquid $Ni-Sn$ alloy exists (see the binary phase diagram of the $Ni-Sn$ system $^{39}$ ). In our previous CALPHAD calculations for the same system, $^{8}$ it was suggested that the equilibrium phases in(Ti,Al)NiSn alloy, with Al additions above its solubility limit( $\sim 1$ at $\%$ in Ti sub-lattice) in TiNiSn are TiNiSn, Sn, and NiAl.Based on these calculations it can be reasonably assumed that the expected stable phases of the currently investigated $(Ti_{0.99} Al_{0.01})$  NiSn composition after heat-treatment are the main HH Al-doped TiNiSn matrix with the embedded residual secondary phases from the solidification process. Another observed feature of the micro- structure is that the grain sizes are $\sim 10 \mu m$ . In addition, EDS measurements of the whole surface area of the investigated cross section shows a stoichiometric amount compatible with the TiNiSn composition. Measurements of the Al concentration gave a result of0.32 at $\%$ , which is equal to 0.96 at $\%$ in the Ti sub-lattice.

The temperature dependence of the transport properties of the $(Ti_{0.99} Al_{0.01}) NiSn$ alloy is shown in Fig. 3. For comparison,

![](./images/812700465031544832_2.jpg)

Fig. 2 Back scattered SEM micrographs of the (Ti₀.₉₉Al₀.₀₁)NiSn alloy following arc-melting, heat treatment and hot-pressing showing: (A) a major TiNiSn HH matrix (gray) with scattered Sn-rich inclusions (white) and (B) a selected area showing in addition to the main HH phase also an inevitable existence of a secondary Ni₃Sn₄ phase, in a lower amount than the XRD detection limit.

the measurements for pure TiNiSn, following a similar synthesis route,⁹ are also presented. It can be clearly seen that the Seebeck coefficient (Fig. 3A) in the Al containing alloy is negative (n-type) in the whole temperature range, indicating that electrons are the major charge carriers. The Al addition to TiNiSn resulted in an increase of the absolute value of the Seebeck coefficient and the electrical resistivity (Fig. 3B) simultaneously. This behavior is an indication of the reduction effect of the electron concentration, upon Al doping, in agreement with previous theoretical predictions indicating that Al is an acceptor dopant in TiNiSn.⁸ This acceptor action of Al, upon Ti substitution in TiNiSn, can be easily understood in terms of the 3 valence electrons of Al compared to the 4 of Ti.

The thermal conductivity was obtained from calculated thermal diffusivity, a, and density, d, values, according to eqn (12).

$$
\kappa = C \cdot d \cdot a \tag{12}
$$

where, C is the heat capacity (taken as 3R per atom according to the Dulong–Petit formula). In order to separate the lattice and electronic contributions to the thermal conductivity, the electron thermal conductivity term, $k_\text{e}$ was calculated using the Wiedemann-Franz law, according to eqn (13) (where L is the Lorentz number), while the lattice thermal conductivity term, $k_\text{l}$ was calculated by subtraction of $\kappa_\text{e}$ from $\kappa$ ($\kappa = \kappa_\text{e} + \kappa_\text{l}$).

$$
\kappa_\text{e} = \frac{LT}{\rho} \tag{13}
$$

The total thermal conductivity is shown in Fig. 3C. It can be clearly seen that above 400 K, the Al containing alloy exhibits a lower thermal conductivity, compared to the pure compound.

Fig. 3D shows the lattice and electronic contributions to the thermal conductivity, demonstrating that the main contribution to $k$ is due to $k_\text{l}$. Also, above 400 K the reduction in the total thermal conductivity is mainly attributed to the significant reduction in the lattice contribution, as the electronic part remains almost the same. This can be associated with mass fluctuations scattering when Al substitutes for Ti in the specific sub-lattice. This will be discussed in detail in the next section.

The figure of merit is shown in Fig. 3E. Above 700 K, the Al addition to TiNiSn clearly increase the ZT of the n-type material in comparison with the pure TiNiSn compound, up to a maximal value of 0.42 at 723 K, reflecting a 17% enhancement.

It is of interest to compare our results with the study of other Al containing n-type MNiSn alloys.⁷ In this work, the influence of 1 at% Al doping of (Zr₀.₅Hf₀.₅)NiSn with following measurement of transport properties in a lower temperature range of 50–350 K is reported and exhibited a similar trend above 150 K. Yet, higher Al concentrations of up to 5 at%, resulted in an increased metallic like behavior as the Al content increased. Although it is reported that all of the investigated compositions had a HH structure, it is likely to assume that for the Al-richer compositions, the solubility limit of Al in the HH phase is exceeded, resulting in the formation of other phases.

To conclude this part, as the Al solubility limit in TiNiSn is estimated to be ~1 at%,⁸ it is not feasible to generate a p-type conductivity by increasing the Al amount in the Ti sub-lattice in poly-crystalline TiNiSn-based alloys. Yet, optimization of the TE transport properties of poly-crystalline n-type MNiSn alloys by combining a partial compensation of the high electron concentration and a significant mass fluctuations induced phonon scattering upon Al additions, is a viable route for enhancing the TE properties of such materials.

### 5.2. Calculation of lattice thermal conductivity

The lattice parameter $(a_0)$, equilibrium bulk modulus $(B_\text{o})$ and the first derivative of the equilibrium bulk modulus with respect to pressure $(B_0')$ for three (Ti,Al)NiSn compositions, reflecting 0, 3 and 6 at% Al substitutions of Ti, were obtained by the fitting of the DFT calculated energy-to-volume dependences to the Murnaghan equation of state in volume optimization procedure, using the built in module of the WIEN2k software (see Fig. 4). Note that the Al amount in the calculated (Ti,Al)-NiSn compositions corresponds the substitution of one or two Al atoms for Ti in the Ti sub-lattice containing 32 atoms in the 96 atoms supercell. With these parameters $\Theta_\text{D}$ and $\gamma$ were calculated using eqn (3) and (8). In Table 1 the magnitudes of $a_0$, $B_\text{o}$, $B_0'$, $\Theta_\text{D}$, and $\gamma$ for non-doped and Al doped TiNiSn are presented to illustrate the influence of doping. For non-doped TiNiSn the calculated $a_0$, $\Theta_\text{D}$ and $B_\text{o}$ correspond well the experimental results 5.933 Å⁴⁰ and 5.92987 Å,⁴¹ 417 K⁴² and 335 K⁴³ and previously calculated 121.4 GPa,⁴⁴ respectively. In addition, our experimental result of 5.935 Å for the lattice parameter of the Al doped TiNiSn is in good agreement with the calculated value.

To account the contribution of the inclusions in the (Ti,Al)-NiSn matrix (eqn (9)–(11)), it was assumed that the inclusions

![](./images/812700465031544832_3.jpg)

Fig. 3 Temperature dependence of the transport properties: (A) Seebeck coefficient, $\alpha$; (B) electrical resistivity, $\rho$; (C) total thermal conductivity, $\kappa$; (D) lattice ($\kappa_{l}$) and electronic ($\kappa_{e}$) thermal conductivity; (E) dimensionless figure of merit, $ZT$. The reference data for the pure TiNiSn, following a similar synthesis approach is taken from Gelbstein et al.⁹

in the HH matrix can be described using $x = 0.05$ and $R = 1$ nm (eqn (11)), as was applied for TiNiSn system in a previous analysis.¹² Both cases refer to TiNnSn-based composition, obtained after a long heat treatment, with the main HH matrix and the solidification residuals of other secondary-phases (like Sn and $Ti_{2}$NiSn). Accounting the effect of grain boundaries was

![](./images/812700465031544832_4.jpg)

Fig. 4 DFT calculations of energy as a function of volume for (Ti₀.₉₄Al₀.₀₆)NiSn in 96 atoms supercell.

<table>
<thead>
<tr>
<th>Table 1 DFT calculated parameters of (Ti,Al)NiSn</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Composition</td>
<td>$a_0$ [Å]</td>
<td>$B_o$ [Gpa]</td>
<td>$B_0'$ [Gpa]</td>
<td>$\Theta_D$ [K]</td>
<td>$\gamma$</td>
</tr>
<tr>
<td>TiNiSn</td>
<td>5.943</td>
<td>127.24</td>
<td>4.03</td>
<td>413.4</td>
<td>1.85</td>
</tr>
<tr>
<td>(Ti₀.₉₄Al₀.₀₆)NiSn</td>
<td>5.942</td>
<td>124.60</td>
<td>4.29</td>
<td>410.2</td>
<td>1.98</td>
</tr>
</tbody>
</table>

also considered, but to be significant for the lattice thermal conductivity of a HH matrix, the average grain size should be under 10 $\mu$m.⁴⁵ As can be seen from the SEM micrographs (Fig. 2) this is not the currently investigated case where the average grain size is higher.

Finally, the lattice thermal conductivity of the (Ti,Al)NiSn alloy as a function of the Al concentration was calculated (eqn (2)). The multi-phase effect was considered using eqn (9)-(11) for each composition. The calculations results are shown in Fig. 5. As was explained before, the minimal possible Al composition simulated with the 96 atoms supercell is 3 at%Al in Ti sub-lattice. The additional calculation for 6 at%Al was carried out in order to examine the general trend of the influence of composition on the calculated lattice thermal conductivity. The calculated relaxation time for the inclusions is $\tau_{inclusions} = 3.70 \times 10^{-12}$. At 300 K the calculated relaxation times are $\tau_{TiNiSn} = 1.94 \times 10^{-12}$ and $\tau_{(Ti_{0.97}Al_{0.03})NiSn} = 1.82 \times 10^{-12}$. Note, the use of the Dulong-Petit formula for the heat capacity (eqn (9)) gives the deviation at low temperatures, as the Debye temperature of the TiNiSn compositions is ~400 K. For example, if we take the measured heat capacity equal to $23.8\ \text{J mol}^{-1}\text{K}^{-1}$ at 300 K,⁴³,⁴⁶ the calculated lattice thermal conductivity for TiNiSn + inclusions will be $7.5\ \text{W m}^{-1}\text{K}^{-1}$.

![](./images/812700465031544832_5.jpg)

Fig. 5 Temperature dependence of the calculated lattice thermal conductivity of (Ti,Al)NiSn, with changing Al concentration and the presence of secondary-phases.

<table>
<thead>
<tr>
<th>Table 2 Calculated and experimental lattice thermal conductivity of (Ti,Al)NiSn alloys</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Composition</td>
<td>$\kappa_{l}$ [$\text{W m}^{-1}\text{K}^{-1}$]@ 300 K</td>
<td>$\kappa_{l}$ [$\text{W m}^{-1}\text{K}^{-1}$]@ 700 K</td>
</tr>
<tr>
<td>TiNiSn</td>
<td>19.9</td>
<td>8.5</td>
</tr>
<tr>
<td>TiNiSn + inclusions</td>
<td>13.1</td>
<td>7.0</td>
</tr>
<tr>
<td>(Ti₀.₉₇Al₀.₀₃)NiSn</td>
<td>18.7</td>
<td>8.0</td>
</tr>
<tr>
<td>(Ti₀.₉₇Al₀.₀₃)NiSn + inclusions</td>
<td>12.5</td>
<td>6.6</td>
</tr>
<tr>
<td>(Ti₀.₉₉Al₀.₀₁)NiSn (exp.)</td>
<td>4.7@353 K</td>
<td>3.1@703 K</td>
</tr>
</tbody>
</table>

Table 2 summarizes the lattice thermal conductivity calculations and measurements for (Ti,Al)NiSn alloys at room temperature (300 K) and at higher temperature (700 K), which presents the optimal operation temperature for TiNiSn alloy in thermoelectric devices. Table 3 summarizes the theoretical calculations and measurements for pure TiNiSn at the same temperatures. For several measurements the average grain size (D) is also presented. Note that the difference between the results of the measurements is likely due to slightly different microstructure of the samples (residual phases, grain size), manufactured at slightly varied preparation processes. It may be seen that for monocrystalline TiNiSn at room temperature our calculated result are overestimated, similar to other theoretical results. Experimental measurements of the lattice thermal conductivity for of TiNiSn⁹,¹⁹ show that its temperature dependence is relatively weak, as was demonstrated in ref. 19. On the other hand, the temperature dependence of the theoretical monocrystalline model follows the $T^{-1}$ trend (eqn (2)). As a result, the difference between the theoretical and measured values decreases with increasing the temperature. Such difference between theoretical calculations and experimental measurements is well common in the literature, and results from the presence of defects in the material and more specifically, mass fluctuations due to the mixing of different atoms in the same sub-lattice, grain boundaries and secondary-phase inclusions in the major HH matrix. If the grains are large enough and the doping level is small (as in our case) than the inclusions have a major influence on the lattice thermal conductivity. In considered temperature range this effect is temperature independent (see eqn (9)-(11)) because the changes of $x$, $R$ and $v_s$ with temperature are negligible. This might explain the relatively small temperature dependence of the results of experimental measurements.

The currently calculated thermal conductivity accounting for Al substitution in the Ti sub-lattice and the presence of the secondary-phases in the TiNiSn matrix is equal to $6.6\ \text{W m}^{-1}\text{K}^{-1}$ at 700 K, for (Ti₀.₉₇Al₀.₀₃)NiSn, is in the order of magnitude (yet, two times higher) as compared with the experimentally measured value of $3.1\ \text{W m}^{-1}\text{K}^{-1}$ obtained at 703 K for (Ti₀.₉₉Al₀.₀₁)NiSn. Nevertheless, the results of the calculations clearly show the effect of Al alloying on the reduction of the lattice thermal conductivity of TiNiSn. It can be seen from our measurements (Fig. 3D) that

<table>
<caption>Table 3 Summary of calculated and measured lattice thermal conductivity of TiNiSn</caption>
<thead>
<tr>
<th>
</th>
<th>
$\kappa_{\text{l}}$ [W m⁻¹ K⁻¹] <br> $\sim$ 300 K
</th>
<th>
$\kappa_{\text{l}}$ [W m⁻¹ K⁻¹] <br> $\sim$ 700 K
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Theoretical calculation (monocrystalline)</td>
<td>13.8–17.9@300 K¹⁸</td>
<td>5.3@700 K⁴⁵ <br> 6.6@700 K⁴⁷</td>
</tr>
<tr>
<td>Experimental measurements</td>
<td>8–9.3@300 K¹⁸ <br> 8@300 Kᵃ¹⁰ <br> 4.5@323 Kᵇ⁹ <br> 3.8@310ᶜ¹⁹</td>
<td>4.1@623 Kᵇ⁹ <br> 3.1@650 Kᶜ¹⁹</td>
</tr>
</tbody>
</table>

$^{a}D \leq 10$ $\mu$m. $^{b}D \leq 95$ $\mu$m. $^{c}D \leq 100$ nm.

the largest decrease in the lattice thermal conductivity in the alloy compared to the pure compound occurs at elevated temperatures. Our calculations demonstrate that this happens when the phonon–phonon interactions are most significant and the Al induced mass-fluctuation are taken into account. Note that the previously reported low value of 3.1 which was measured at 650 K¹⁹ is for TiNiSn sample with ultrafine grains having the size $D \leq 100$ nm, that are smaller in orders of magnitude in comparison with our sample.

## 6. Conclusions

Combined experimental and theoretical work was carried out in order to study the influence of Al on the transport properties of TiNiSn half-Heusler compound. The basis to this research was our previous work⁸ which included theoretical demonstration of the acceptor behavior of Al in (Ti,Al)NiSn alloy and an estimation of the solubility limit in the Ti sub-lattice. The microstructure examination of the pre-selected (Ti₀.₉₉Al₀.₀₁)NiSn composition using XRD and SEM-EDS showed that there was no segregation of Al from the HH phase, confirming that the Al composition does not exceed the solubility limit in TiNiSn. Transport properties measurements up to 750 K confirmed that Al behaves as an electron acceptor, upon substituting Ti, while reducing the electron concentration of n-type TiNiSn. Above 400 K, a significant reduction of the thermal conductivity was observed for 1 at% Al substitution of Ti. As a result, the obtained alloy showed a figure of merit of 0.42 at 723 K, reflecting 17% improvement compared to the unalloyed TiNiSn compound. Additional electronic optimization, or even obtaining p-type behavior, is not expected with further addition of Al, as its solubility limit is estimated not exceeding 1 at%.

Due to the major influence of the lattice thermal conductivity on the material’s TE conversion efficiency, the effect of the involved mechanisms was theoretically analyzed. *Ab initio* DFT calculations combined with a semi-empirical model demonstrated the critical role of secondary-phases on reduction of the lattice thermal conductivity of TiNiSn alloys. The major contribution of high temperature mass fluctuations upon Al alloying was highlighted by both calculations and measurements.

Our results show a genuine route for improving the figure of merit of MNiSn (M = Ti, Ni, Sn) alloys, by using electron acceptor dopants, partially compensating the inherent high electron concentrations, while reducing the lattice thermal conductivity, mainly due to mass variations compared to the individual sub-lattice atoms in these half-Heusler compounds.

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

One of authors, Y. G. holds the Samuel Ayrton Chair in Metallurgy. The work was supported by the M-Era.Net 3-14910 “MarTEnergy” grant funded by the Cyprus Research Promotion Foundation (P2P/KOINA/M-ERA.NET/0317/04) and the Ministry of Science Technology and Space, Israel. The authors are thankful to Mr Yair George and Mr Gil Breuer for the help with the synthesis of the alloys and specimen’s preparation and to Dr Dimitri Mogiliansky for the XRD analysis.

## References

1. T. Graf, C. Felser and S. S. Parkin, Simple rules for the understanding of Heusler compounds, *Prog. Solid State Chem.*, 2011, **39(1)**, 1–50.

2. T. Zhu, C. Fu, H. Xie, Y. Liu and X. Zhao, High efficiency half-Heusler thermoelectric materials for energy harvesting, *Adv. Energy Mater.*, 2015, **5(19)**, 1500588.

3. J. Yu, K. Xia, X. Zhao and T. Zhu, High performance p-type half-Heusler thermoelectric materials, *J. Phys. D: Appl. Phys.*, 2018, **51(11)**, 113001.

4. J. Schmitt, Z. M. Gibbs, G. J. Snyder and C. Felser, Resolving the true band gap of ZrNiSn half-Heusler thermoelectric materials, *Mater. Horiz.*, 2015, **2(1)**, 68–75.

5. M. Kaller, D. Fuks and Y. Gelbstein, Sc solubility in p-type half-Heusler (Ti₁₋ₛScₛ) NiSn thermoelectric alloys, *J. Alloys Compd.*, 2017, **729**, 446–452.

6. A. Horyn, O. Bodak, L. Romaka, Y. Gorelenko, A. Tkachuk, V. Davydov and Y. Stadnyk, Crystal structure and physical properties of (Ti, Sc)NiSn and (Zr, Sc)NiSn solid solutions, *J. Alloys Compd.*, 2004, **363(1–2)**, 10–14.

7. M. Schwall, *Heusler compounds for thermoelectric applications*, Universitätsbibliothek Mainz, 2012.

8. D. Rabin, D. Fuks and Y. Gelbstein, Al solubility in (Ti₁₋ₛAlₛ) NiSn half-Heusler alloy, *Phys. Chem. Chem. Phys.*, 2019, **21(14)**, 7524–7533.

9. Y. Gelbstein, N. Tal, A. Yarmek, Y. Rosenberg, M. P. Dariel, S. Ouardi, B. Balke, C. Felser and M. Köhne, Thermoelectric properties of spark plasma sintered composites based on TiNiSn half-Heusler alloys, *J. Mater. Res.*, 2011, **26(15)**, 1919–1924.

10. S. Bhattacharya, M. Skove, M. Russell, T. Tritt, Y. Xia, V. Ponnambalam, S. Poon and N. Thadhani, Effect of boundary scattering on the thermal conductivity of TiNiSn-based half-Heusler alloys, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2008, **77(18)**, 184203.

11 K. Kirievsky, Y. Gelbstein and D. Fuks, Phase separation and antisite defects in the thermoelectric TiNiSn half-Heusler alloys, *J. Solid State Chem.*, 2013, **203**, 247–254.

12 K. Kirievsky, M. Shlimovich, D. Fuks and Y. Gelbstein, An *ab initio* study of the thermoelectric enhancement potential in nano-grained TiNiSn, *Phys. Chem. Chem. Phys.*, 2014, **16(37)**, 20023–20029.

13 S. Ouardi, G. H. Fecher, B. Balke, M. Schwall, X. Kozina, G. Stryganyuk, C. Felser, E. Ikenaga, Y. Yamashita and S. Ueda, Thermoelectric properties and electronic structure of substituted Heusler compounds: ${\text{NiTi}}_{0.3-x}{\text{Sc}}_{x}{\text{Zr}}_{0.35}{\text{Hf}}_{0.35}{\text{Sn}}$, *Appl. Phys. Lett.*, 2010, **97(25)**, 252113.

14 M. Gürth, G. Rogl, V. Romaka, A. Grytsiv, E. Bauer and P. Rogl, Thermoelectric high *ZT* half-Heusler alloys ${\text{Ti}}_{1-x-y}{\text{Zr}}_{x}{\text{Hf}}_{y}{\text{NiSn}}$ ($0 \leq x \leq 1; 0 \leq y \leq 1$), *Acta Mater.*, 2016, **104**, 210–222.

15 O. Appel, M. Schwall, D. Mogilyansky, M. Köhne, B. Balke and Y. Gelbstein, Effects of microstructural evolution on the thermoelectric properties of spark-plasma-sintered ${\text{Ti}}_{0.3}{\text{Zr}}_{0.35}{\text{Hf }}_{0.35}$ NiSn half-Heusler compound, *J. Electron. Mater.*, 2013, **42(7)**, 1340–1345.

16 O. Appel, M. Schwall, D. Mogilyansky, M. Köhne, B. Balke and Y. Gelbstein, Effects of microstructural evolution on the thermoelectric properties of spark-plasma-sintered ${\text{Ti}}_{0.3}{\text{Zr}}_{0.35}{\text{Hf}}_{0.35}{\text{NiSn}}$ half-Heusler compound, *J. Electron. Mater.*, 2013, **42(7)**, 1340–1345.

17 S. V. Faleev and F. Léonard, Theory of enhancement of thermoelectric properties of materials with nanoinclusions, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2008, **77(21)**, 214304.

18 S. N. Eliassen, A. Katre, G. K. Madsen, C. Persson, O. M. Løvvik and K. Berland, Lattice thermal conductivity of ${\text{Ti}}_{x}{\text{Zr}}_{y}{\text{Hf}}_{1-x-y}{\text{NiSn}}$ half-Heusler alloys calculated from first principles: key role of nature of phonon modes, *Phys. Rev. B*, 2017, **95(4)**, 045202.

19 M. Schrade, K. Berland, S. N. Eliassen, M. N. Guzik, C. Echevarria-Bonet, M. H. Sørby, P. Jenuš, B. C. Hauback, R. Tofan and A. E. Gunnæs, The role of grain boundary scattering in reducing the thermal conductivity of polycrystalline X NiSn (X = Hf, Zr, Ti) half-Heusler alloys, *Sci. Rep.*, 2017, **7(1)**, 13760.

20 B. H. Toby and R. B. Von Dreele, GSAS-II: the genesis of a modern open-source all purpose crystallography software package, *J. Appl. Crystallogr.*, 2013, **46(2)**, 544–549.

21 K. Schwarz, P. Blaha and G. K. H. Madsen, Electronic structure calculations of solids using the WIEN2k package for material sciences, *Comput. Phys. Commun.*, 2002, **147(1)**, 71–76.

22 P. Blaha, K. Schwarz, G. K. H. Madsen, D. Kvasnicka and J. Luitz, *WIEN2k, An augmented plane wave+ local orbitals program for calculating crystal properties*, Karlheinz Schwarz, *Techn*, Universitat Wien, Austria, 2001, ISBN 3-9501031-1-2, version 10.1 (release 10/6/2010).

23 V. I. Anisimov, F. Aryasetiawan and A. Lichtenstein, First-principles calculations of the electronic structure and spectra of strongly correlated systems: the LDA+*U* method, *J. Phys.: Condens. Matter*, 1997, **9(4)**, 767.

24 P. Guss, M. E. Foster, B. M. Wong, F. Patrick Doty, K. Shah, M. R. Squillante, U. Shirwadkar, R. Hawrami, J. Tower and D. Yuan, Results for aliovalent doping of ${\text{CeBr}}_{3}$ with ${\text{Ca}}^{2+}$, *J. Appl. Phys.*, 2014, **115(3)**, 034908.

25 M. Cococcioni and S. De Gironcoli, Linear response approach to the calculation of the effective interaction parameters in the LDA+*U* method, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2005, **71(3)**, 035105.

26 D. T. Morelli and G. A. Slack, *High lattice thermal conductivity solids*, *High Thermal Conductivity Materials*, Springer, 2006, pp. 37–68.

27 Z.-Y. Jiao, T.-X. Wang and S.-H. Ma, Phase stability, mechanical properties and lattice thermal conductivity of ceramic material $({\text{Nb}}_{1-x}{\text{Ti}}_{x}{)}_{4}{\text{AlC}}_{3}$ solid solutions, *J. Alloys Compd.*, 2016, **687**, 47–53.

28 T. Jia, G. Chen and Y. Zhang, Lattice thermal conductivity evaluated using elastic properties, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2017, **95(15)**, 155206.

29 S. Saha and G. Dutta, Elastic and thermal properties of the layered thermoelectrics BiOCuSe and LaOCuSe, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2016, **94(12)**, 125209.

30 S. Singh and R. Kumar, *Ab initio* calculations of elastic constants and thermodynamic properties of LuAuPb and YAuPb half-Heusler compounds, *J. Alloys Compd.*, 2017, **722**, 544–548.

31 G. Leibfried and W. Ludwig, *Theory of anharmonic effects in crystals, solid state physics*, Elsevier, 1961, pp. 275–444.

32 O. L. Anderson, A simplified method for calculating the Debye temperature from elastic constants, *J. Phys. Chem. Solids*, 1963, **24(7)**, 909–917.

33 M. Hichour, D. Rached, R. Khenata, M. Rabah, M. Merabet, A. H. Reshak, S. B. Omran and R. Ahmed, Theoretical investigations of NiTiSn and CoVSn compounds, *J. Phys. Chem. Solids*, 2012, **73(8)**, 975–981.

34 N. Vočadlo and G. D. Price, The Grüneisen parameter—computer calculations *via* lattice dynamics, *Phys. Earth Planet. Inter.*, 1994, **82(3–4)**, 261–270.

35 F. Murnaghan, The compressibility of media under extreme pressures, *Proc. Natl. Acad. Sci. U. S. A.*, 1944, **30(9)**, 244.

36 J. Slater, *Introduction to Chemical Physics*, McGraw-Hill Book Company, New York, 1939.

37 T. M. Tritt, *Thermal Conductivity: Theory, Properties, and Applications*, Klumer, Academic/Plenum Publishers, New York, USA, 2004.

38 A. Goktas, A. Tumbul and F. Aslan, A new approach to growth of chemically depositable different ZnS nanostructures, *J. Sol–Gel Sci. Technol.*, 2019, **90(3)**, 487–497.

39 C. Schmetterer, H. Flandorfer, K. W. Richter, U. Saeed, M. Kauffman, P. Roussel and H. Ipser, A new investigation of the system Ni–Sn, *Intermetallics*, 2007, **15(7)**, 869–884.

40 V. Romaka, P. Rogl, L. Romaka, Y. Stadnyk, N. Melnychenko, A. Grytsiv, M. Falmbigl and N. Skryabina, Phase equilibria, formation, crystal and electronic structure of ternary compounds in Ti–Ni–Sn and Ti–Ni–Sb ternary systems, *J. Solid State Chem.*, 2013, **197**, 103–112.

41 C. S. Birkel, W. G. Zeier, J. E. Douglas, B. R. Lettiere, C. E. Mills, G. Seward, A. Birkel, M. L. Snedaker, Y. Zhang and G. J. Snyder, Rapid microwave preparation of thermoelectric TiNiSn and TiCoSb half-Heusler compounds, *Chem. Mater.*, 2012, **24(13)**, 2558–2565.

42 R. Kuentzler, R. Clad, G. Schmerber and Y. Dossmann, Gap at the Fermi level and magnetism in RMSn ternary compounds (R = Ti, Zr, Hf and M = Fe, Co, Ni), *J. Magn. Magn. Mater.*, 1992, **104**, 1976-1978.

43 B. Dhong, *Physical metallurgy and properties of TiNiSn and PtMnSb*, PhD thesis, Iowa State University, 1997.

44 C. Colinet, P. Jund and J.-C. Tédenac, NiTiSn a material of technological interest: *ab initio* calculations of phase stability and defects, *Intermetallics*, 2014, **46**, 103-110.

45 P. Hermet and P. Jund, Lattice thermal conductivity of NiTiSn half-Heusler thermoelectric materials from first-principles calculations, *J. Alloys Compd.*, 2016, **688**, 248-252.

46 D. Wee, B. Kozinsky, B. Pavan and M. Fornari, Quasiharmonic vibrational properties of TiNiSn from *ab initio* phonons, *J. Electron. Mater.*, 2012, **41**(6), 977-983.

47 L. Andrea, G. Hug and L. Chaput, *Ab initio* phonon properties of half-Heusler NiTiSn, NiZrSn and NiHfSn, *J. Phys.: Condens. Matter*, 2015, **27**(42), 425401.

---

This journal is © the Owner Societies 2019

*Phys. Chem. Chem. Phys.*