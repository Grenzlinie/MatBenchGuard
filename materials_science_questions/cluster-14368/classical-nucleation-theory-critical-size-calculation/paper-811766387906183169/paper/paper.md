Geosci. Model Dev. Discuss., 3, 1139–1159, 2010
www.geosci-model-dev-discuss.net/3/1139/2010/
doi:10.5194/gmdd-3-1139-2010
© Author(s) 2010. CC Attribution 3.0 License.

![](./images/811766387906183169_1.jpg)

This discussion paper is/has been under review for the journal Geoscientific Model
Development (GMD). Please refer to the corresponding final paper in GMD if available.

# A simplified treatment of surfactant effects on cloud drop activation

T. Raatikainen and A. Laaksonen

Finnish Meteorological Institute, P.O. Box 503, 00101 Helsinki, Finland

Received: 18 June 2010 – Accepted: 30 June 2010 – Published: 30 July 2010

Correspondence to: T. Raatikainen (tomi.raatikainen@fmi.fi)

Published by Copernicus Publications on behalf of the European Geosciences Union.

---

![](./images/811766387906183169_2.jpg)

### Abstract

Dissolved surface active species, or surfactants, have a tendency to partition to solution surface and thereby decrease solution surface tension. Activating cloud droplets have large surface-to-volume ratios, and the amount of surfactant molecules in them is limited. Therefore, unlike with macroscopic solutions, partitioning to the surface can effectively deplete the droplet interior of surfactant molecules.

Surfactant partitioning equilibrium for activating cloud droplets can be solved numerically from a group of equations. This can be a problem when surfactant effects are examined by using large-scale cloud models. Namely, computing time increases significantly due to the partitioning calculations done in the lowest levels of nested iterations.

The purpose of this paper is to present analytical equations for surfactant partitioning equilibrium. Some simplifications are needed in deriving the equations, but the numerical errors caused by the simplifications are shown to be very minor. In addition, computing time is decreased roughly by an order of magnitude.

### 1 Introduction

The aerosol effect on cloud albedo and thereby on the radiation balance of the Earth constitutes the largest single scientific uncertainty in the assessment of the current radiative forcing (IPCC: Solomon et al., 2007). Among the reasons for the large uncertainty are various chemical effects (Charlson et al., 2001; Topping et al., 2007; Wex et al., 2008) such as surface tension reduction of activating cloud droplets. By preferentially partitioning to the droplet solution surface, surface active species can cause a clear decrease of the surface tension of aqueous solutions (Li et al., 1998; Sorjamaa et al., 2004). Decreased surface tension is often taken into account in aerosol and cloud modelling, but the effect of droplet size-dependent surface partitioning on solution concentrations is often ignored (e.g. Shulman et al., 1996; Facchini et al., 1999; Mircea et al., 2002; Broekhuizen et al., 2004). The reason for this is probably that the

![](./images/811766387906183169_3.jpg)

partitioning has no effect on bulk concentrations in large systems, such as laboratory samples from which the surface tensions are measured. However, the partitioning influence on droplet bulk concentrations does become relevant for micron-sized or smaller droplets having large surface area to volume ratios (Laaksonen, 1993; Sorjamaa et al., 2004; Prisle et al., 2010).

The effect of surfactant partitioning on cloud droplet activation have been studied both experimentally using CCN counters and theoretically relying on the Köhler theory (Li et al., 1998; Sorjamaa et al., 2004; Prisle et al., 2008, 2010). Briefly, models accounting for surface tension decrease but not for surfactant partitioning are predicting clearly too high cloud forming activity. On the other hand, predictions which either account for or ignore both the surface tension and partitioning effects are generally in reasonable agreement with experimental measurements of critical supersaturations. However, even if the models agree on this aspect, they can predict quite different critical droplet sizes and also the predicted droplet solution concentrations are clearly different. The critical drop size and its solute concentration affect solution thermodynamics (e.g. solubility), vapour-liquid equilibrium, and droplet growth dynamics (Kokkola et al., 2006).

A special problem in the surface partitioning calculations is that droplet concentrations are determined by numerically solving a set of non-linear equations, which is often too time-consuming in large-scale model calculations. The purpose of this paper is to present analytical equations for surfactant partitioning which are more practical for large-scale applications. We will also test the validity of the new equations against the numerical model.

## 2 Theory

Surfactant partitioning effects are greatest with small and dilute droplets. With very large droplets, accounting for surfactant mass balance has a minor effect on the bulk concentration as the concentration change due to partitioning to surface is roughly

![](./images/811766387906183169_4.jpg)

proportional to the inverse of radius. With most surfactants, the strongest surface tension decrease as a function of concentration (which influences the partitioning) takes place at very low concentrations. Both conditions are usually fulfilled at cloud droplet activation.

Here the term bulk refers to droplet's homogeneous liquid interior, which is the phase defining droplet properties such as equilibrium vapour pressures. Droplet surface is assumed to be in thermodynamic equilibrium with the bulk solution.

### 2.1 Cloud droplet activation

The equilibrium saturation ratio of water ($S$) over droplet surface can be calculated from the well known Köhler equation (Köhler, 1936):

$$
S = \gamma_{\rm w}x_{\rm w} \exp\left( \frac{4v_{\rm w}\sigma}{RTD_{\rm aq}} \right) \tag{1}
$$

Here, so called Raoult term gives water activity as a product of activity coefficient $\gamma_{\rm w}$ and mole fraction $x_{\rm w}$. Increased vapour pressure due to droplet curvature is taken into account by the exponential Kelvin term. In addition to partial molar volume of water $v_{\rm w}$ ($\rm m^3/mol$) (which we approximate by the molar volume of pure water), ideal gas constant $R$ ($\rm J/(mol\,K)$) and temperature $T$ ($\rm K$), the Kelvin term depends on droplet solution surface tension $\sigma$ ($\rm N/m$) and droplet diameter $D_{\rm aq}$ ($\rm m$).

Total molar concentrations of solutes can be calculated from the known dry particle composition (dry size $D_{\rm dry}$ and dry volume fractions of solutes $\xi$). Assuming volume additivity ($V_{\rm dry}$+$V_{\rm w}$=$V_{\rm aq}$), the molar concentration of water can be calculated from

$$
n_{\rm w}^{\rm T} = \frac{\pi}{6} \left( D_{\rm aq}^3 - D_{\rm dry}^3 \right) / v_{\rm w} \tag{2}
$$

where superscript $T$ denotes total molar concentration. When suitable water activity coefficient and surface tension parameterizations are available, droplet total concentrations can be used in calculating the equilibrium saturation ratio $S$. An example of

![](./images/811766387906183169_5.jpg)

a Köhler curve showing equilibrium supersaturation $SS=(S-1)\cdot100\%$ as a function of droplet size, is shown in Fig. 1.

When an initially dry particle is exposed to water vapour and relative humidity (RH) is increased above the deliquescence point, a droplet is formed. When RH is further increased, the droplet grows by condensation of water vapour until equilibrium given by Eq. (1) is reached, thus the droplet equilibrium growth follows the Köhler curve. However, when water supersaturation exceeds the maximum value of the Köhler curve, condensation of water can not lead to equilibrium any more, thus the droplet grows to cloud droplet sizes. Equilibrium theory is no longer valid for this non-equilibrium growth, which depends on the availability of water vapour. As the non-equilibrium growth is initiated at the maximum of the Köhler curve, the droplet size and supersaturation corresponding to the maximum are called critical diameter and supersaturation needed for cloud droplet formation.

As described above, the total number concentrations of the droplet species can be calculated from input parameters. These can be used in calculating water activity and solution surface tension needed in the Köhler equation (Eq. 1). However, some chemical and physical effects such as limited solubility and partial dissociation can have an effect on droplet bulk liquid phase concentrations. Of course, if e.g. some fraction of a solute is undissolved, bulk concentrations used in calculating water activity and surface tension should be determined from the dissolved fraction. Analogously, surfactant bulk-surface partitioning changes bulk solution concentrations. Here we are ignoring these other effects and focus on the surfactant partitioning.

### 2.2 Bulk-surface partitioning of surfactants

The effect that the partitioning to surface has on bulk solution concentrations depends greatly on the system size. For example, saturation surface excess ($\Gamma^\infty$) values, giving the maximum number of surfactant molecules per unit surface area, are on the order of $1\ \mathrm{\mu mol/m^2}$ (e.g. Tuckermann, 2007). For $1\ \mathrm{\mu m}$ and $1\ \mathrm{mm}$ droplets with $1\ \mathrm{mM}$ surfactant bulk concentration, the surface to bulk molar ratios are then roughly 6 and 0.006,

![](./images/811766387906183169_6.jpg)

respectively. The partitioning is thus not important for 1 mm droplets in the sense that it would have a noticeable effect on the bulk concentration. However, in the case of 1 $\mu$m and smaller droplets, the majority of the surfactant molecules can partition to surface, causing the bulk concentration to decrease strongly.

Surface and bulk solution concentrations can be solved from the Gibbs adsorption isotherm (Gibbs, 1928):

$$
\sum n_{i}^{\mathrm{S}} d \ln \left(\gamma_{i}^{\mathrm{B}} c_{i}^{\mathrm{B}}\right)+\frac{A}{R T} d \sigma^{\mathrm{B}}=0 \tag{3}
$$

where $n_{i}^{\mathrm{S}}$ (mol) is surface (excess) concentration, $\gamma_{i}^{\mathrm{B}}$ is activity coefficient and $c_{i}^{\mathrm{B}}$ is concentration of liquid phase component $i$, $A$ ($\mathrm{m}^2$) is droplet surface area, and $\sigma^{\mathrm{B}}$ (N/m) is droplet surface tension. Superscripts B and S refer to bulk and surface solutions, respectively, and subscript $i$ includes all liquid phase species such as molecular solutes, ions and water. We assume a closed system, thus $n_{i}^{\mathrm{T}}=n_{i}^{\mathrm{B}}+n_{i}^{\mathrm{S}}$. In addition, the ions of an electrolyte can not partition independently as the phases can not have a net charge.

In order to simplify the calculation of the surface concentrations, we can decrease the number of independent variables using suitable assumptions. Commonly, only the surfactant is expected to partition, i.e. $n_{i}^{\mathrm{S}}=0$ for other than surfactant species. Alternatively, it can be assumed that the partitioning of the surfactant (subscript s) is compensated by depletion of water from the surface, i.e. $V^{\mathrm{S}}=n_{\mathrm{w}}^{\mathrm{S}} v_{\mathrm{w}}+n_{\mathrm{s}}^{\mathrm{S}} v_{\mathrm{s}}=0$, which is in agreement with the definition of flat surface in the adsorption equation. In the case of multicomponent solutions, water and non-surfactant solutes (subscript $j$) can be assumed to behave as a pseudobinary solution so that the equalities $n_{\mathrm{w}}^{\mathrm{T}} / n_{\mathrm{w}}^{\mathrm{B}}=n_{j}^{\mathrm{T}} / n_{j}^{\mathrm{B}}$ and $V^{\mathrm{S}}=\sum n_{i}^{\mathrm{S}} v_{i}=0$ connect all concentrations to that of the surfactant (Sorjamaa et al., 2004; Prisle et al., 2010).

With any of the above mentioned assumptions, the adsorption equation contains only one unknown. The adsorption equation can of course be solved numerically, with numerically determined surface tension and activity gradients. Unfortunately, the

![](./images/811766387906183169_7.jpg)

numerical solution may be too slow for large-scale models, where bulk concentrations are needed in the lowest levels of nested iterations. Our purpose is to derive, making reasonable approximations, an analytical solution for Eq. (3), and to show that the results do not differ significantly from the numerical solution of Eq. (3).

### 2.2.1 Analytical solution for surfactant partitioning

The number of unknowns must first be reduced to one in order to solve Eq. (3) analytically. The first approximation is that other species than the surfactants do not exhibit bulk-surface partitioning, i.e. $n_i^\mathrm{S} \neq 0$ for surfactant species only. In the case of ionic surfactants, the surface concentrations of the ions are related to that of the undissociated surfactant via the dissociation factor. It can be shown that the surface tension is independent of droplet size (an implicit assumption that is practically always made) when the condition $V^\mathrm{S} = \sum n_i^\mathrm{S} \nu_i = 0$ holds (Laaksonen et al., 1999), which is not the case here. It will be shown below that the nonzero surface excess volume does not cause any numerical consequences.

The second approximation we make is that activity coefficients are set to unity or alternatively considered as constants. This approximation is needed, because there are no simple and generally valid activity coefficient equations for surfactant solutions. In any case, unit activity coefficients should be a fair approximation as activating droplets are dilute.

Our third approximation is that the surfactant concentration is linearly dependent on the number concentration ($c^\mathrm{B} = n^\mathrm{B}/c^0$). This is true for molality, but not for mole fraction or molarity. However, this is a fair approximation for dilute solutions, because total molar number and solution volume are only weakly dependent of the surfactant number concentration. In addition, this approximation makes the result independent of surface tension model concentration scale.

There are a number of functional forms available in the literature that describes the surface tension lowering of aqueous surfactant solutions. We apply by the well known

Szyskowski equation (Szyskowski, 1908):

$$
\sigma = \sigma_{\mathrm{w}} - RT\Gamma^{\infty}\ln\left(1 + \frac{c}{\beta}\right) \tag{4}
$$

where $\sigma_{\mathrm{w}}$ is surface tension of pure water, and saturation surface excess $\Gamma^{\infty}$ ($\mathrm{mol/m^2}$) and inverse activity coefficient $\beta$ (same unit with the concentration $c$) are experimentally determined parameters. Common concentration scales include molarity (mol/L or just M), molality (mol/kg) as well as dimensionless mole and mass fractions. With the above mentioned approximation, $c^{\mathrm{B}}=n^{\mathrm{B}}/c^{0}$, surface tension gradient can be calculated as:

$$
\frac{d\sigma^{\mathrm{B}}}{d\ln n^{\mathrm{B}}} = \frac{d\sigma^{\mathrm{B}}}{d\ln c^{\mathrm{B}}} = -\frac{RT\Gamma^{\infty}c^{\mathrm{B}}}{\beta + c^{\mathrm{B}}} = -\frac{RT\Gamma^{\infty}n^{\mathrm{B}}}{\beta c^{0} + n^{\mathrm{B}}} \tag{5}
$$

The last form of the equation is the most useful one, because our goal is to solve for surfactant bulk number concentration $(n^{\mathrm{B}})$. The constant $c^{0}$ depends on the unit (concentration scale) of $\beta$. For molarity, molality and mole fraction scales $c^{0}$ is volume of the droplet (L), mass of water (kg) and total number concentration (mol), respectively.

As a result, the equation to solve is:

$$
(n^{\mathrm{T}} - n^{\mathrm{B}})\frac{\sum \nu_{i}d\ln(n_{i}^{\mathrm{B}})}{d\ln n^{\mathrm{B}}} = \frac{A\Gamma^{\infty}n^{\mathrm{B}}}{\beta c^{0} + n^{\mathrm{B}}} \tag{6}
$$

where $\nu_{i}$ is dissociation factor and $n_{i}^{\mathrm{B}}$ is total bulk number concentration including also common ions for surfactant ion $i$. Here and from now on undissociated surfactant concentrations are given without subscript ($n^{\mathrm{B}}$ and $n^{\mathrm{T}}$); subscripted concentrations are reserved for ions from surfactant dissociation. Of course, it is not necessary that the surfactant is ionic. In the case of molecular surfactants and in the absence of common ions, the solution is simple. Therefore, cases with and without common ions are considered separately below.

![](./images/811766387906183169_8.jpg)

Surfactant without common ions. In the absence of common ions, the activity gradient term $\sum v_i d\ln(n_i^\mathrm{B})$ is just $v d\ln(n^\mathrm{B})$, where $v=v_++v_-$ is surfactant dissociation factor. Then Eq. (6) simplifies to

$$
v\left(n^\mathrm{T}-n^\mathrm{B}\right)=\frac{A \Gamma^\infty n^\mathrm{B}}{\beta c^0+n^\mathrm{B}} \tag{7}
$$

This leads to a quadratic equation with surfactant bulk number concentration as the unknown:

$$
n^\mathrm{T} \beta c^0+\left(n^\mathrm{T}-\beta c^0-A \Gamma^\infty / v\right) n^\mathrm{B}-\left(n^\mathrm{B}\right)^2=0 \tag{8}
$$

Only the positive solution for $n^\mathrm{B}$ is acceptable:

$$
n^\mathrm{B}=\frac{n^\mathrm{T}-\beta c^0-A \Gamma^\infty / v+\sqrt{\left(n^\mathrm{T}-\beta c^0-A \Gamma^\infty / v\right)^2+4 n^\mathrm{T} \beta c^0}}{2} \tag{9}
$$

Surfactant with common ions. Common ions, e.g. $\mathrm{Na}^+$ in aqueous sodium dodecyl sulfate (SDS)-NaCl solution, have an effect on the activity gradient term. For simplicity, we assume that the surfactant is composed of $v_+$ cations and $v_-$ anions, and there can be only one common ion so that one of the common ion concentrations represented by $n^+$ (mol) and $n^-$ (mol) is zero. Then the activity term is

$$
\sum v_i d \ln \left(n_i^\mathrm{B}\right)=v_+d \ln \left(v_+n^\mathrm{B}+n^+\right)+v_-d \ln \left(v_-n^\mathrm{B}+n^-\right) \tag{10}
$$

The gradient is

$$
\frac{\sum v_i d \ln \left(n_i\right)}{d \ln n^\mathrm{B}}=\frac{v n^\mathrm{B}+k_2}{n^\mathrm{B}+k_1} \tag{11}
$$

where common ion terms are denoted by $k_1$ and $k_2$:

$$
k_1 = n^-/v_- + n^+/v_+ \tag{12}
$$

$$
k_2 = v_+/v_-n^- + v_-/v_+n^+ \tag{13}
$$

For example, in the case of aqueous SDS-NaCl ($v_+=v_-=1$, $v=2$, $n^-=0$, $n^+=n_{\text{NaCl}}$)
$k_1$=$k_2$=$n_{\text{NaCl}}$.

By combining Eqs. (6) and (11) we have

$$
(n^{\text{T}} - n^{\text{B}})\frac{vn^{\text{B}} + k_2}{n^{\text{B}} + k_1} = \frac{A\Gamma^\infty n^{\text{B}}}{\beta c^0 + n^{\text{B}}} \tag{14}
$$

This can be can be simplified to a cubic equation:

$$
\begin{aligned}
&n^{\text{T}}k_2\beta c^0 + \left(n^{\text{T}}k_2 + (\nu n^{\text{T}} - k_2)\beta c^0 - k_1A\Gamma^\infty\right)n^{\text{B}} \\
&\quad + \left(\nu n^{\text{T}} - k_2 - \nu\beta c^0 - A\Gamma^\infty\right)(n^{\text{B}})^2 - \nu(n^{\text{B}})^3 = 0
\end{aligned} \tag{15}
$$

Cubic equations can be solved analytically, but it is sometimes difficult to find the correct real root. Instead, the correct root can be found efficiently by a suitable numerical method.

## 3 Model comparison

Here, we use iterative methods to test our analytical partitioning equations. Clearly, approximations needed for the analytical equations should not be important for the results, and the equations should be valid for slightly different Szyskowski surface tension parameterizations, e.g. with different concentration scales. Approximations are not needed and it is possible to use any kind of available surface tension and activity coefficient parameterizations when the adsorption equation (Eq. 3) is solved numerically. The iterative model, described in Appendix A, was designed so that selected approximations can be applied.

![](./images/811766387906183169_9.jpg)

We use the analytical and iterative models to predict the critical supersaturation (which is the most important parameter coming out of the Köhler theory, and the only directly detectable parameter in CCN experiments) of particles composed of sodium dodecyl sulfate (SDS) and sodium chloride (NaCl). In all modelling versions, critical droplet size is found iteratively by using the same search algorithm.

The SDS-NaCl mixture was chosen due to the availability of experimental surface tension data and well known chemical and physical properties (Sorja- maa et al., 2004; Prisle et al., 2010). The surface tension of aqueous SDS- NaCl solution can be described with the Szyskowski equation (Eq. 4) by using the following parameters from Prisle et al. (2010): $RT\Gamma^\infty$=$13.90×10^{-3}$ N/m and $\beta$=$(9.273×10^{-6}\text{M}^2)/(c_{\text{NaCl}}+9.733×10^{-3}\text{M})$. In addition, the effect of salt on water-NaCl solution surface tension was taken into account by assuming linear dependence on salt concentration ($c_{\text{NaCl}}$) with the slope of $1.61×10^{-3}$ N/m M$^{-1}$ (Prisle et al., 2010; Vanhanen et al., 2008). Note that parameter $\beta$ depends explicitly on salt concentration, but this is not a problem as it is independent of surfactant concentration. In addition to explicitly accounting for the salt effect on surface tension, a simple parameterization based on the SDS only is used ($RT\Gamma^\infty$=$13.90×10^{-3}$ N/m and $\beta$=$9.527×10^{-4}$ M).

### 3.1 Approximations needed for the analytical equations

In addition to some obvious considerations (e.g. $n^\text{T}$=$n^\text{B}$+$n^\text{S}$), some clear approximations had to be made:

- Only the surfactant partitions. This is a fair approximation. Water and salt should have slightly increased bulk concentrations, but their relative concentration would not be changed.

- Constant/unit activity coefficients. This approximation had to be done, because activity coefficients are complex functions of solution bulk concentrations.
![](./images/811766387906183169_10.jpg)

- Surfactant concentration is directly proportional to number concentration, i.e. $d\ln(c)$=$d\ln(n)$. This depends on the concentration scale of the Szyskowski equation, but generally it is a good approximation for dilute droplets.

In the iterative model (Appendix A1) the default is to allow partitioning for all species. Bulk solution concentrations are than connected to that of the surfactant by fixing surface volume to zero $\left(\sum n_{i}^{\mathrm{S}} v_{i}=0\right)$ and by the pseudobinary approximation ($n_{\mathrm{w}}^{\mathrm{T}}/n_{\mathrm{w}}^{\mathrm{B}}$=$n_{j}^{\mathrm{T}}/n_{j}^{\mathrm{B}}$, when $j$ is not surfactant). Activity coefficients can be either calculated from the Debye-Hückel model (Debye and Hückel, 1923; Clegg and Pitzer, 1992) or set to unity. Approximation $d\ln(c)$=$d\ln(n)$ is not needed for the iterative model, because activity gradients are calculated numerically.

Approximations of the analytical equations were tested by comparing predictions of the analytical model with those of the iterative model with selected approximations, also including all hybrids. The calculations showed that when activity coefficients are set to unity, predictions for SDS-NaCl particles are practically equal. When Debye-Hückel activities were used in the iterative models, slightly higher critical supersaturations were predicted. The other approximations such as $d\ln(c)$=$d\ln(n)$ and zero surface excess for other than the surfactant have negligible effect on model predictions. Figure 2 shows predictions of the analytical model as well as those of the iterative model with and without Debye-Hückel activity coefficients. Model predictions without activity coefficients are practically indistinguishable.

We do not know if the Debye-Hückel model is accurate for the current surfactant-salt mixture, but the effect of non-idealities is not the focus of this paper. It is possible that there are mixtures where unit activity coefficients lead to significant prediction errors. This is also a quite common uncertainty in modelling, because activity coefficients are rarely available for multicomponent mixtures. For simplicity, we use unit activity coefficients in the following calculations.

![](./images/811766387906183169_11.jpg)

### 3.2 Effect of surface tension parameterization

The goodness of the $d\ln(c)$=$d\ln(n)$ approximation depends somewhat on concentration scale of the surface tension parameterization and if other solutes are accounted or not. Figure 3 shows predictions from the analytical and iterative models with binary and ternary surface tension fits described in Sect. 3. Again, model predictions are practically equal. Because binary and ternary fits give different surface tensions for other than the pure surfactant case, different model predictions can be expected. This is not seen, so the effect of salt on solution surface tension can be ignored at least in this case. A likely reason is that due to the extensive surfactant partitioning and dilute droplets, critical droplet surface tension is always close to that of pure water. In addition, the surface tension gradient, which is important for partitioning equilibrium, is only weakly dependent on salt concentration.

The effect of concentration scale was tested by doing calculations with different binary surface tension fits based on molality, molarity and mole fraction scales. It was seen that predictions from the iterative and analytical models were practically equal (not shown). We can therefore conclude that the analytical equations are valid for various Szyskowski equation concentration scales.

It is possible that concentration dependent Szyskowski surface tension parameters do not fulfil conditions needed for the analytical equation. From several possible cases, we choose one in which the Szyskowski parameters depend explicitly on surfactant concentration. The Szyskowski parameters given in Prisle et al. (2010) depend on solute mass fraction, which of course changes due to surfactant partitioning. Model calculations based on sodium decanoate-NaCl surface tension parameterization (Prisle et al., 2010) are shown in Fig. 4. Again, model predictions are quite similar, but this finding is not generally valid. It seem that in this case NaCl has quite small effect on surface tension slopes, which is important for partitioning.

![](./images/811766387906183169_12.jpg)

### 4 Conclusions

Analytical equations were derived for droplet bulk solution concentrations that account for surfactant bulk-surface partitioning. Comparison of predictions from the analytical equation and from numerical solution of the original set of equations showed that the analytical equations predict critical droplet size, supersaturation and composition accurately. Furthermore, the analytical method is robust, meaning that a solution is always found. In addition to the common approximations needed for solving the Köhler and adsorption equations, additional approximations and limitations needed in deriving the analytical equation (i.e. only the surfactant was assumed to partition, activity coefficients were set to unity and surfactant concentration was taken to depend linearly on surfactant number concentration) were found to have minimal effects on the predictions. It should be stressed that the new analytical equation relies on the Szyskowski equation, so that if for some aqueous-surfactant system the surface tension reduction is given by some other equation, the Szyskowski parameters need to be determined first by a fitting procedure.

Analytical equations are most useful for large-scale models where cloud microphysics is explicitly accounted for. As bulk concentrations are needed at low-level functions, computation time of the partitioning equilibrium is crucial for total computation time. For example, when calculating critical droplet size (first level iteration) for droplets containing partially soluble solutes (second level iteration), partitioning calculations are in the third level. Use of the new equations reduces the computer time needed for the droplet concentration calculations roughly by an order of magnitude.

![](./images/811766387906183169_13.jpg)

### Appendix A
#### Iterative model

The number of independent variables in the adsorption equation is decreased to one by making two assumptions (Sorjamaa et al., 2004; Prisle et al., 2010). First of all, it is assumed that at the Gibbs dividing surface, the following equation holds:

$$
V^{\mathrm{S}} = \sum n_{i}^{\mathrm{S}} v_{i} = 0 \tag{A1}
$$

As shown by Laaksonen et al. (1999), Eq. (A1) is consistent with the assumption that the droplet surface tension (when keeping the bulk concentration constant) is not size-dependent. In the case of multicomponent solutions water and non-surfactant solutes (subscript $j$) are assumed to behave as a pseudobinary solution so that their concentration ratios remain unchanged:

$$
n_{\mathrm{w}}^{\mathrm{T}} / n_{\mathrm{w}}^{\mathrm{B}} = n_{j}^{\mathrm{T}} / n_{j}^{\mathrm{B}} \tag{A2}
$$

An alternative for the pseudobinary approximation is to ignore partitioning of the non-surfactant solutes. Equation (A1) still holds as water can be depleted from the surface.

Both surface tension and activity gradients are calculated numerically, so any types of equations giving surface tension and activity coefficients can be used. Because our focus is on surface tension and there are no general activity coefficient models for surfactant-salt solutions, activity coefficients are calculated from a Debye-Hückel extension. Our version of the equation is the ideal part of the Pitzer-Simonsen-Clegg model as given by Clegg and Pitzer (1992):

$$
\ln \gamma_{i} = \frac{2 A_{x} I_{x}^{3/2}}{1 + \rho \sqrt{I_{x}}} - z_{i}^{2} A_{x} \left( \frac{2}{\rho} \ln(1 + \rho \sqrt{I}) + \frac{\sqrt{I_{x}}}{1 + \rho \sqrt{I_{x}}} \right) \tag{A3}
$$

where $A_{x}$=2.917 (for water at 298.15 K), $\rho$=13.0 and mole fraction scale ionic strength $I$=$0.5 \sum x_{i} z_{i}^{2}$. Charge $z_{i}$ is zero for water.

![](./images/811766387906183169_14.jpg)

Acknowledgements. The financial support by the Academy of Finland Centre of Excellence program (project no 1118615) is gratefully acknowledged.

### References

Broekhuizen, K., Kumar, P. P., and Abbatt, J. P. D.: Partially soluble organics as cloud condensation nuclei: role of trace soluble and surface active species, Geophys. Res. Lett., 31, L01107, doi:10.1029/2003GL018203, 2004. 1140

Charlson, R. J., Seinfeld, J. H., Nenes, A., et al.: Atmospheric science: reshaping the theory of cloud formation, Science, 292, 2025–2026, 2001. 1140

Clegg, S. L. and Pitzer, K. S.: Thermodynamics of multicomponent, miscible, ionic solutions: generalized equations for symmetrical electrolytes, J. Phys. Chem., 96, 3513–3520, 1992. 1150, 1153

Debye, P. and Hückel, E.: Theory of electrolytes. 1. Freezing point lowering and related phenomena, Physik. Z., 24, 185–206, 1923. 1150

Facchini, M. C., Mircea, M., Fuzzi, S., and Charlson, R. J.: Cloud albedo enhancement by surface-active organic solutes in growing droplets, Nature, 401, 257–259, 1999. 1140

Gibbs, J. W.: The Collected Works of J. Willard Gibbs, Vol. 1, Longmans, Green and Co., New York, 1928. 1144

Köhler, H.: The nucleus in and the growth of hygroscopic droplets, T. Faraday Soc., 32, 1151–1161, 1936. 1142

Kokkola, H., Sorjamaa, R., Peräniemi, A., et al.: Cloud formation of particles containing humic-like substances, Geophys. Res. Lett., 33, L10816, doi:10.1029/2006GL026107, 2006. 1141

Laaksonen, A.: The composition size dependence of aerosols created by dispersion of surfactant solutions, J. Colloid Interf. Sci., 159, 517–519, 1993. 1141

Laaksonen, A., McGraw, R., and Vehkamäki, H.: Liquid-drop formalism and free-energy surfaces in binary homogeneous nucleation theory, J. Chem. Phys., 111, 2019–2027, 1999. 1145, 1153

Li, Z., Williams, A. L., and Rood, M. J.: Influence of soluble surfactant properties on the activation of aerosol particles containing inorganic Solute, J. Atmos. Sci., 55, 1859–1866, 1998. 1140, 1141

Mircea, M., Facchini, M. C., Decesari, S., Fuzzi, S., and Charlson, R. J.: The influence of the organic aerosol component on CCN supersaturation spectra for different aerosol types, Tellus B, 54, 74–81, 2002. 1140

Prisle, N. L., Raatikainen, T., Sorjamaa, R., Svenningsson, B., Laaksonen, A., and Bilde, M.: Surfactant partitioning in cloud droplet activation: a study of C8, C10, C12 and C14 normal fatty acid sodium salts, Tellus B, 60, 416–431, 2008. 1141

Prisle, N. L., Raatikainen, T., Laaksonen, A., and Bilde, M.: Surfactants in cloud droplet activation: mixed organic-inorganic particles, Atmos. Chem. Phys., 10, 5663–5683, doi:10.5194/acp-10-5663-2010, 2010. 1141, 1144, 1149, 1151, 1153, 1159

Shulman, M. L., Jacobson, M. C., Carlson, R. J., et al.: Dissolution behavior and surface tension effects of organic compounds in nucleating cloud droplets, Geophys. Res. Lett., 23, 277–280, 1996. 1140

Solomon, S., Qin, D., Manning, M., Chen, Z., Marquis, M., Averyt, K. M. T., and Miller, H. (Eds.): Climate Change 2007: The Physical Science Basis. Contribution of Working Group I to the Fourth Assessment Report of the Intergovernmental Panel on Climate Change, Cambridge University Press, Cambridge, UK and New York, NY, USA, 2007. 1140

Sorjamaa, R., Svenningsson, B., Raatikainen, T., Henning, S., Bilde, M., and Laaksonen, A.: The role of surfactants in Köhler theory reconsidered, Atmos. Chem. Phys., 4, 2107–2117, doi:10.5194/acp-4-2107-2004, 2004. 1140, 1141, 1144, 1149, 1153

Szyskowski, B. V.: Experimentelle Studien über kapillare Eigenschaften der wässerigen Lösungen von Fettsäuren, Z. Phys. Chem., 64, 385–414, 1908 (in German). 1146

Topping, D. O., McFiggans, G. B., Kiss, G., et al.: Surface tensions of multi-component mixed inorganic/organic aqueous systems of atmospheric significance: measurements, model pre- dictions and importance for cloud activation predictions, Atmos. Chem. Phys., 7, 2371–2398, doi:10.5194/acp-7-2371-2007, 2007. 1140

Tuckermann, R.: Surface tension of aqueous solutions of water-soluble organic and inorganic compounds, Atmos. Environ., 41, 6265–6275, 2007. 1143

Vanhanen, J., Hyvärinen, A.-P., Anttila, T., Raatikainen, T., et al.: Ternary solution of sodium chloride, succinic acid and water; surface tension and its influence on cloud droplet activa- tion, Atmos. Chem. Phys., 8, 4595–4604, doi:10.5194/acp-8-4595-2008, 2008. 1149

Wex, H., Stratmann, F., Topping, D., and McFiggans, G.: The Kelvin versus the Raoult term in the Köhler equation, J. Atmos. Sci., 65, 4004–4016, 2008. 1140

![](./images/811766387906183169_15.jpg)

![](./images/811766387906183169_16.jpg)

Fig. 1. Water supersaturation as a function of droplet size for a 40 nm dry particle. Kelvin and
Raoult terms are shown with the dashed line in the right hand side scale.

![](./images/811766387906183169_17.jpg)

![](./images/811766387906183169_18.jpg)

Fig. 2. Critical supersaturation for 40 nm SDS-NaCl particles as a function of dry particle surfactant mass fraction. Model predictions are made with analytical model and iterative model with and without activity coefficients.

![](./images/811766387906183169_19.jpg)

Fig. 3. Critical supersaturation for 40 nm SDS-NaCl particles as a function of dry particle surfactant mass fraction. Model predictions are made with analytical and iterative model with both binary and ternary surface tension parameterizations.

![](./images/811766387906183169_20.jpg)

Fig. 4. Critical supersaturation for 40 nm SDS-NaCl particles as a function of dry particle surfactant mass fraction. Model predictions are made with analytical and iterative modes with sodium decanoate-NaCl surface tension parameterization (Prisle et al., 2010).
![](./images/811766387906183169_21.jpg)

Copyright of Geoscientific Model Development Discussions is the property of Copernicus Gesellschaft mbH and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.