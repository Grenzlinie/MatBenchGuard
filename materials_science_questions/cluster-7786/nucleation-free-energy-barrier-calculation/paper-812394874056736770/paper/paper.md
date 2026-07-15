# HOMOGENEOUS NUCLEATION OF SILICON

Frank Einar Kruis,* Joop Schoonman and Brian Scarlett

Laboratories of Particle Technology and Inorganic Chemistry, Chemical Engineering Department,
Delft University of Technology, Julianalaan 136, 2628 BL Delft, Netherlands

(First received 14 January 1994; and in final form 28 March 1994)

Abstract—The homogeneous nucleation of silicon from the Si–H–Cl system was studied theoretically for a wide range of compositions and temperatures. Contour plots of the conversion ratio and the chemical potential to nucleate are displayed. Nucleation rates were calculated using a modified classical nucleation model (Girshick *et al.* (1990) *Aerosol Sci. Technol.* **13**, 465) which agrees well with reported data on the onset of nucleation for the $\text{SiH}_4/\text{H}_2$ and $\text{SiH}_2\text{Cl}_2/\text{H}_2$ systems. It is important to use a correctly defined supersaturation and a temperature-dependent surface tension. Theoretically, the nucleation time lag is found to be substantial in the vicinity of the nucleation onset and at high silane concentrations. The decomposition kinetics of the silane becomes important in systems with a very fast temperature rise, for example in a laser-heated reactor.

## 1. INTRODUCTION

Homogeneous nucleation of silicon is an important phenomenon both in particle synthesis from the gas phase (chemical vapour precipitation, CVP) and in heterogeneous deposition (chemical vapour deposition, CVD). In CVD processes, especially the manufacture of microelectronic devices, the formation of particles must be avoided whilst in the laser-CVP process homogeneous nucleation is the essential step through which the powder is formed. An understanding of this process and a quantitative description is, therefore, necessary.

In a development of the laser-CVP process for $\text{Si}_3\text{N}_4$ (Bauer, 1991; Bauer *et al.*, 1991; Kruis, 1993), $\text{SiH}_4$ was replaced by the chlorinated silanes $\text{SiH}_2\text{Cl}_2$, $\text{SiHCl}_3$, and $\text{SiCl}_4$. The experimental results revealed that pure $\text{SiH}_2\text{Cl}_2$ does nucleate at high temperatures but that $\text{SiHCl}_3$ and $\text{SiCl}_4$ do not. One of the purposes of this work is to investigate the conversion ratio, the nucleation potential and the nucleation rate of $\text{SiH}_4$ and of the chlorinated silanes. Unfortunately, the prediction of nucleation rates is *a priori* not reliable and requires experimental measurements. The nucleation model was therefore checked by using reported experimental results.

Earlier studies were focused mainly on the thermochemical data and chemical equilibrium calculations. An overview is given by Kruis *et al.* (1992). Nucleation phenomena in the Si–H–Cl system have been reported more scarcely. Several studies concern the temperature at which nucleation starts (Eversteijn, 1971; Herrick and Woodruff, 1984). Allen and Sawin (1986) studied the chemical potential for nucleation at temperatures of 1073 and 1273 K and Herrick and Woodruff (1984) performed nucleation rate calculations. More recently, aerosol technologists showed interest in the modelling of nucleation, especially in correcting the classical model and in finding criteria for its use. They have also developed kinetic models which are applicable when the kinetic factors become more important than the thermodynamic factors and when the control of runaway nucleation is of interest.

In this work, an investigation is made of the procedure to screen the different silanes for their nucleation potential at different temperatures and hydrogen dilutions. A study of the nucleation rate, and especially the onset of nucleation temperature, is attempted using existing nucleation models. Special attention is given to the assumptions inherent in the models.

* Present address: Laboratoire des Sciences du Genie Chimique CNRS-ENSIC, 1 Rue Grandville, BP 451, 54001 Nancy Cedex, France.

## 2. THEORY OF HOMOGENEOUS NUCLEATION

Homogeneous nucleation occurs only in a supersaturated system. This supersaturation is defined as

$$
S=p / p_{\mathrm{s}}. \tag{1}
$$

The term $p$ is the ambient partial pressure and $p_{\mathrm{s}}$ the partial pressure in the saturated system. In the case of 'physical' nucleation, for example in the condensation of water, the supersaturation is easy to calculate. However, in those cases where particles are formed by chemical reaction, as in silicon nucleation, this is less well defined. It is generally agreed (Kato et al., 1981) that the partial pressure in a chemically supersaturated system can be obtained from calculations of the equilibrium of the pure vapour system, neglecting the presence of solid or liquid phases. In this way the situation before nucleation starts is simulated. The values of $p_{\mathrm{s}}$ are defined to be those at the gas-solid or gas-liquid equilibrium point. In the literature, there are several approaches for calculating $p_{\mathrm{s}}$. Herrick and Woodruff (1984) used a simple expression for the gas-solid equilibrium values over the whole range of dilution by hydrogen whilst in this work equilibrium calculations of the partial pressure of silicon were made for a given dilution ratio and temperature.

The classical nucleation theory, which was developed by Volmer, Becker, Frenkel and Zeldovich in the 1930s (Zettlemoyer, 1969), is the most common approach for treating a supersaturated system. Such a system is inherently unstable. However, in order to calculate the number concentration of clusters, a hypothetical pseudoequilibrium state is assumed so that thermodynamic theories can be used. The pseudoequilibrium number concentration of clusters containing $k$ molecules, $n_{k}^{\mathrm{e}}$, is determined from the associated free energy change, $\Delta G$. The molecule is often called a monomer in nucleation theory, and the cluster is called a $k$-mer:

$$
\Delta G /\left(k_{\mathrm{b}} T\right)=-k \ln S+\theta k^{2 / 3}. \tag{2}
$$

The pseudoequilibrium number concentration $n_{k}^{\mathrm{e}}$ is defined as

$$
n_{k}^{\mathrm{e}}=N \exp \left(-\Delta G /\left(k_{\mathrm{b}} T\right)\right), \tag{3}
$$

where $N$ is a normalization constant, $k_{\mathrm{b}}$ is the Boltzmann constant, $S$ is the supersaturation and $\theta$ is a dimensionless surface tension:

$$
\theta=\frac{\sigma s_{1}}{k_{\mathrm{b}} T}, \tag{4}
$$

in which $\sigma$ is the surface tension of the condensed species and $s_{1}$ is the surface area of a monomer. In the classical theory, $N$ is equated to the monomer concentration, $n_{1}$. The cluster properties are assumed to be equal to the bulk thermodynamic properties. This assumption will be discussed in a later paragraph. Once the free barrier to nucleation is overcome, a cluster will grow further. The critical cluster size, $k^{*}$, is found by locating the maximum value of $\Delta G$ and is given by

$$
k^{*}=(2 \theta /(3 \ln S))^{3}. \tag{5}
$$

Classical nucleation theory assumes that both collisional growth by incorporation of a monomer and evaporative shrinking of a cluster by loss of a monomer take place. Cluster-cluster collisions and simultaneous evaporation of more than one monomer from a cluster are neglected. Using the kinetic theory of gases for calculating the number of collisions it can be shown (Warren and Seinfeld, 1984) that the nucleation rate is

$$
J_{\mathrm{cl}}=N \frac{\beta_{11} n_{1}}{12} \sqrt{\frac{\Theta}{2 \pi}} \exp \left(-4 \frac{\Theta^{3}}{27(\ln S)^{2}}\right), \tag{6}
$$

$\beta_{11}$ is the collision frequency function for monomers which can be calculated from the

collision frequency function for collisions between $i$-mers and $j$-mers:

$$
\beta_{i j}=\left(\frac{3 v_{1}}{4 \pi}\right)^{1 / 6} \sqrt{\frac{6 k_{\mathrm{b}} T}{\rho_{\mathrm{p}}}\left(\frac{1}{i}+\frac{1}{j}\right)}\left(i^{1 / 3}+j^{1 / 3}\right)^{2},
\tag{7}
$$

where $\rho_{\mathrm{p}}$ is the particle mass.

An alternative to the classical theory is the statistical mechanical theory (Pound et al., 1971), in which the clusters are assumed to have vibrational, rotational and translational energy. This results in nucleation rates which, for water for example, are 17 orders of magnitude higher than the results obtained using the classical theory and are mostly not in agreement with the experimental results. The extremely high dependence of the nucleation rate on the saturation rate and surface tension makes it difficult to distinguish by experiment predictions which differ by orders of magnitude. However, the classical nucleation rate is often a factor of $10^{3}-10^{7}$ lower than the experimental results (Okuyama et al., 1987).

Katz and Wiedersich (1977), and Warren and Seinfeld (1984) recognized that use of the equilibrium cluster size distribution is not correct and gave a kinetic description of the nucleation process. Warren and Seinfeld (1984) found a nucleation rate higher than the original thermodynamic form of classical nucleation by a factor of $S^{(\theta-1)}$. In systems with a high value of $\theta$, typically between 10 and 40, and a high supersaturation, this would give an extreme increase in the nucleation rate maybe a factor of $10^{20}-10^{100}$ higher. Thus, this model is not included in the calculations in this work. Katz and Wiedersich (1977) included an unevaluated normalization constant in their final expression. Girshick et al. (1990) suggested an evaluation of this normalization constant by requiring that equation (3) be satisfied for monomers, resulting in

$$
N=n_{\mathrm{s}} \exp \theta
\tag{8}
$$

and giving the nucleation rate for the kinetic model $J_{\text {kin }}$ as

$$
J_{\text {kin }}=\frac{\exp \theta}{S} J_{\mathrm{cl}}.
\tag{9}
$$

As a result, the kinetic expression for the nucleation rate is $10^{3}-10^{6}$ times larger than the classical thermodynamic expression, which seems to be more in agreement with reported experiments (Okuyama et al., 1987; Nguyen et al., 1987).

### 3. METHOD OF CALCULATION

The thermochemical data of the Si-H-Cl-N system were studied and reported earlier (Kruis et al., 1992). The resulting thermochemical values were used here in the equilibrium calculations for the Si-H-Cl system using the program SOLGASMIX (Erikson, 1975). The silicon partial pressure, $p$, was calculated first by suppressing the presence of solid or liquid phases and then the partial pressure in the saturated system, $p_{\mathrm{s}}$, was calculated by including them. For example, in the $\mathrm{SiH}_{4} / \mathrm{H}_{2}$ system nine gases $\left(\mathrm{SiH}_{4}, \mathrm{Si}, \mathrm{Si}_{2}, \mathrm{Si}_{3}, \mathrm{H}, \mathrm{H}_{2}, \mathrm{SiH}, \mathrm{SiH}_{2}\right.$, $\mathrm{SiH}_{3}$ ) were included in the equilibrium calculations. So $p$ was calculated first including only these nine gases and then $p_{\mathrm{s}}$ by including the nine gases and the liquid or solid Si phase. This approach is similar to that used by Katz and Donohue (1982). Sometimes $p$ and $p_{\mathrm{s}}$ are calculated by considering only one reaction (Kato et al., 1981) and, thus, only a limited number of gases but this is an oversimplification which might introduce appreciable errors.

The conversion ratio, defined as the fractional number of moles of Si deposited during equilibration of the vapour, can also be calculated. Further calculations were made using a contour program (GRAPHER 3-D).

### 4. RESULTS AND DISCUSSION

In order to investigate the phase behaviour of the Si-H-Cl system, the phase behaviour for the different silane gases was screened as a function of temperature and hydrogen dilution. In Fig. 1, contours of constant conversion ratio of the silicon are shown. All the

![](./images/812394874056736770_1.jpg)

Fig. 1. Contour plot of conversion ratio as a function of temperature and the mole fraction of (A) $SiH_{4}$, (B) $SiH_{2}Cl_{2}$ and (C) $SiHCl_{3}$, in $H_{2}$.

silane homologues exhibit the same behaviour at higher temperatures and low concentra- tions. The conversion ratio increases as the temperature decreases or the concentration increases. The chlorosilanes have a maximum value of the conversion ratio at a concentra- tion of around $10^{-4} mol mol^{-1}$ and at a temperature of 1400 K. When the concentration of the silane homologue is high, the contours are nearly vertical. Changing the temperature does not then change the conversion ratio significantly. When more chlorine is present in the silane homologue, the conversion ratio is lower. Silane displays a different behaviour. Since it has a large operating region with a conversion ratio higher than 0.95, it is the most promising gas from the synthesis point of view.

It may be questioned whether it is correct to use the same expression for the partial pressure in the saturated system, $p_{s}$, over the whole range of silane homologue concentra- tions, as for example was done by Herrick and Woodruff (1984). In the present calculations $p_{s}$ proved indeed to be independent of the silane homologue concentration at low temperatures. However, in the case of high temperatures, above 1800 K, $p_{s}$ becomes a function of the silane homologue concentration. An explanation for this is that it is not possible for $p_{s}$ to become larger than the silicon input, hence $p_{s}$ becomes constant at higher values. Thus, using the same expression over the whole range of silane homologue concentrations can introduce non-realistic values for $p_{s}$ and unnecessary errors in the supersaturation.

It is generally thought (e.g. Allen and Sawin, 1986) that the free energy change, $\Delta G$, or the chemical potential to nucleate can be used to screen different gases for their nucleation potential. Note that the thermodynamic driving force for particle formation becomes larger as the chemical potential to nucleate becomes more negative. In Fig. 2, this nucleation potential for the different silanes is shown as a function of concentration and temperature. In general,

![](./images/812394874056736770_2.jpg)

Fig. 2. Contour plot of chemical potential to nucleate (kJ mol⁻¹) as a function of temperature and mole fraction of (A) SiH₄, (B) SiH₂Cl₂ and (C) SiHCl₃, in H₂.

when the temperature increases $\Delta G$ becomes more negative and the thermodynamic driving force increases. This is also the case when the concentration in hydrogen of the silane homologue increases. The nucleation potential is more sensitive to changes in temperature than changes in concentration, thus the contours of constant nucleation potential are nearly horizontal. The nucleation potential of SiH₄ and SiH₂Cl₂ differ no more than $10\ \text{kJ mol}^{-1}$ but the nucleation potential of SiHCl₃ differs much more. For all gases, the thermodynamic driving force is maximal at low temperatures and high concentrations.

In order to compare experimental data taken from the literature with calculations of the nucleation rate, both the classical and the kinetic model have been used here. Nucleation experiments in chemical reacting systems are usually performed by slowly increasing the temperature of a tubular furnace through which a gas mixture flows and visually observing the appearance of particles. The temperature at which particles are first observed is called the 'onset of nucleation temperature', and the nucleation rate is estimated to be about $1\ \#\ (\text{cm}^3\text{s})^{-1}$ (Herrick and Woodruff, 1984), with # denoting the number of particles. It is clear that this is not a very precise method. Visual observation is only reliable for particles larger than one micron and in sufficient quantity, hence the nucleus has to be enlarged by condensation or coagulation. Current aerosol nucleation experiments use a Condensation Nucleus Counter for detecting particles larger than 5 nm. Using a model which takes into account condensation and coagulation, the nucleation rate can be calculated (see e.g. Warren et al., 1987). However, the visual experiments are still useful for an approximate estimate of the onset of nucleation, especially as the nucleation rate increases very rapidly with increasing temperature. Eversteijn (1971) studied experimentally the nucleation of SiH₄ in H₂ and Herrick and Woodruff (1984) SiH₂Cl₂ in H₂.

Since the nucleation rate is a very strong function of the surface tension, it is important to use correct values. Since a very large temperature range (800-2600 K) is considered, it is necessary to consider the temperature dependence of the surface tension and also to take into account the melting of silicon at 1685 K. Mezey and Giber (1982) measured the surface tension of solid silicon to be $1.24\ \text{J m}^{-2}$ at 298 K and $0.779\ \text{J m}^{-2}$ at 1683 K. Krystian and Olson (1991) concluded, from experimental results, that the surface tension is almost a linear function of temperature for the solid elements. Hence, for temperatures up to 1685 K, the experimental values were here interpolated. Experimental results for liquid silicon are available at different temperatures between 1700 and 2000 K (Levin *et al.*, 1966). They also show the surface tension to be a linear function of temperature. The following expressions for the surface tension were therefore used:

$$\sigma=1.339-3.329 \times 10^{-4} T \quad \text{for } T<1685 \text{ K,} \tag{10}$$

$$\sigma=0.912-1.04 \times 10^{-4} T \quad \text{for } T>1685 \text{ K.} \tag{11}$$

Since the temperature dependence of the other necessary physical properties is not so pronounced and is less likely to yield large deviations of the nucleation rate, the values for solid-state silicon were used.

Nucleation rate calculations were performed over a range of temperatures and composi- tions for the different silane homologues using both the classical and the kinetic formula. The temperature at which the nucleation rate, $J$, equals $1\ \#\ (\text{cm}^3\text{ s})^{-1}$, is called the temperature for the onset of nucleation. It appeared that each homologue exhibits a maximum in the plot of nucleation rate against temperature. As a result, a specific value for the nucleation at two different temperatures may be obtained. At low temperatures the supersaturation is large but the partial pressure of silicon is very small, thus inhibiting nucleation below a certain temperature. At higher temperatures this effect is reversed, the partial pressure is large but the supersaturation is small. Therefore, nucleation occurs only between two limiting temperatures. In Fig. 3, the predicted temperature for the onset of nucleation is displayed and is compared with the experimental values. In general, the kinetic model gives rates which are a factor of $10^3$-$10^6$ higher than the classical nucleation rate and a lower nucleation temperature at the low-temperature points. From the graphs it can be concluded that the

![](./images/812394874056736770_3.jpg)

Fig. 3(A).

![](./images/812394874056736770_4.jpg)

Fig. 3. The temperature for the onset of nucleation ($J=1$ # ($\mathrm{cm}^3\ \mathrm{s})^{-1}$) calculated using the classical and the kinetic model as a function of temperature and mole fraction of (A) $\mathrm{SiH}_4$, (B) $\mathrm{SiH}_2\mathrm{Cl}_2$ and (C) $\mathrm{SiHCl}_3$, in $\mathrm{H}_2$. At each temperature there is a lower and an upper temperature between which nucleation takes place. Experimental values are from Table II of Eversteijn (1971) in the case of the $\mathrm{SiH}_4$ and from Table I of Herrick and Woodruff (1984) in the case of the $\mathrm{SiH}_2\mathrm{Cl}_2$.

kinetic model displays better agreement with the experimental data, and so the kinetic model was used for the subsequent figures. In Fig. 4, the critical cluster size, $k^*$, at the lowest temperature where nucleation occurs is displayed. From this figure a different trend in the critical cluster size of $\mathrm{SiHCl}_3$ can be seen compared to that of $\mathrm{SiH}_4$ and $\mathrm{SiH}_2\mathrm{Cl}_2$. This can be explained by the slope of the nucleation potential (Fig. 2). In the case of $\mathrm{SiH}_4$ and $\mathrm{SiH}_2\mathrm{Cl}_2$ the nucleation potential continuously decreases with increasing concentration and thus the supersaturation rises, causing the critical cluster size, $k^*$, to increase (equation (5)). But in the

![](./images/812394874056736770_5.jpg)

Fig. 4. The critical cluster size, $k^{*}$, at the onset of nucleation temperature $(J=1 \#\ (cm^{3} s)^{-1})$ using
the kinetic model.

case of $SiHCl_{3}$ the behaviour is different. When, for example at 1200 K, the concentration increases, the supersaturation first increases, then decreases at a mole fraction of $10^{-3}$ and then increases again at a mole fraction of $10^{-1}$. This is reflected in the behaviour of the critical nucleus size, $k^{*}$. In Fig. 5, the nucleation rate at several concentrations is shown as a function of temperature. At high concentrations homogeneous nucleation is only possible in the $SiH_{4}$ and the $SiH_{2} Cl_{2}$ system, except for pure $SiHCl_{3}$ where the nucleation rate is very low $(<10^{4} \#\ (cm^{3} s)^{-1})$. This latter fact explains unsuccessful attempts to synthesize Si from $SiHCl_{3}$ (Bauer, 1991) and also why, in the micro-electronics industry, chlorinated silanes are preferred in order to prevent particle deposition on wafers. The main reason for the lower nucleation rate of $SiHCl_{3}$ is the lower value of the supersaturation and thus of the nucleation potential. For instance, at a temperature of 1200 K and a mole fraction of $10^{-2}$ the supersaturation in the $SiH_{4}, SiH_{2} Cl_{2}$ and $SiHCl_{3}$ system is, respectively, $1.5 × 10^{4}, 1.2 × 10^{3}$ and 66. A general conclusion is that dilution with $H_{2}$ lowers the nucleation rate and increases the temperature for the onset of nucleation. At very low concentrations, for example $10^{-4}$ mole fraction, the nucleation behaviour of the different silane homologues becomes similar. Comparison of these calculations with the calculations of Herrick and Woodruff (1984), who used the classical model, reveals that the qualitative behaviour is similar. Since Herrick and Woodruff used an estimate of the surface tension which was not mentioned in their paper, it is not possible to explain why they found that the experimental results agreed with the classical model. In the present study a more elaborate way to calculate the correct saturation pressures has been used as well as the most recent thermochemical data. The thermochemical data used by Herrick and Woodruff were older values. Probably the most important factor is that the calculations in this work do not depend on an estimate of the surface tension but are based on experimental values.

## 5. DISCUSSION OF THE VALIDATION AND APPLICABILITY OF THE MODEL

In the nucleation model several assumptions are made:

(a) surface tension is size-independent (capillarity approximation),

(b) particles are spherical,
(c) particles are electrically neutral,
(d) London-van der Waals forces are neglected,
(e) the cluster size distribution is in equilibrium,
(f) cluster-cluster coagulation and cluster-aerosol coagulation (scavenging) is neglected,
(g) the nucleation rate neglects coagulation between particles larger than the critical size after nucleation has started, resulting in abnormally high particle concentrations.

Most of these assumptions are easily understood but some require more detailed discussion.

![](./images/812394874056736770_6.jpg)

Fig. 5(A) and (B).

![](./images/812394874056736770_7.jpg)

Fig. 5. The nucleation rate according to the kinetic model as a function of temperature at different mole fractions (indicated in the legend) of (A) $SiH_{4}$, (B) $SiH_{2}Cl_{2}$ and (C) $SiHCl_{3}$, in $H_{2}$.

The capillarity approximation is generally accepted to be valid, even in systems where the critical nucleus size is several molecules. It seems strange to treat nuclei of almost molecular sizes, between 3 and 13 molecules, in the case of $SiH_{4}$ and $SiH_{2}Cl_{2}$, as macroscopic drops or crystals. The literature suggests that the concepts can be extrapolated almost down to molecular level without the introduction of serious error so far as the qualitative trends of the phenomena are concerned (Reiss et al., 1988). This can be explained by the fact that surface energy merely reflects the unsaturated bonding at a surface and this feature may retain its meaning at the molecular level.

The assumption that the cluster size distribution is in equilibrium is more speculative. The time needed to attain a steady-state cluster distribution is called the 'time lag'. Shi et al. (1990) derived a kinetic expression for the transient period during which the cluster concentrations increase to their steady-state values. The time lag, $\tau$, is given by

$$
\tau=\left(\frac{2}{3} n_{1} s_{1} \sqrt{\frac{k_{\mathrm{b}} T \theta}{2 \pi m_{1}}}\right)^{-1}, \tag{12}
$$

where $m_{1}$ is the mass of a molecule. The time lag for the common nucleation systems studied, for example DBP formation (Warren et al., 1987), is of the order of microseconds. Girshick et al. (1990) simulated this transient period using a discrete-sectional model. In this simulation a nucleation rate was not used but particle formation was simulated by applying the general aerosol dynamic equation to a discrete representation for monomers and small clusters and a more approximate representation of the larger sizes. They found a time lag of the order of microseconds for iron at 1600 K with a supersaturation $S=200$. When an approximate calculation of the time lag in the $SiH_{4}-H_{2}$ system at the temperature for the onset of nucleation is made, a rather larger time is found, i.e. 9000 s $(0.4\ \mathrm{SiH}_{4}$ in $\mathrm{H}_{2})$, 130 s $(10^{-2}\ \mathrm{SiH}_{4}$ in $\mathrm{H}_{2})$ and 0.14 s $(10^{-4}\ \mathrm{SiH}_{4}$ in $\mathrm{H}_{2})$. Considering the expression for the time lag it can be seen that $n_{1}$ is the parameter which varies most. Increasing the temperature to 200 K above the onset of nucleation, increases $n_{1}$ by a factor of $10^{4}-10^{5}$. Thus, the time lag is in the order of milliseconds for all concentrations. At 400 K above the onset of nucleation, the time lag is of the order of microseconds. The main cause of the appreciable time lag calculated is

the small value of $n_1$ in the silicon system. The time lag is, thus, maximal at high $\mathrm{SiH}_4$ concentrations and in the neighbourhood of the onset of nucleation. Thus, it can be understood why the experiments of Herrick and Woodruff (1984), performed at mole fractions between $10^{-2}$ and $10^{-1}$, show a larger uncertainty in the onset of nucleation temperature than the experiments of Eversteijn (1971), which were performed at mole fractions between $10^{-5}$ and $10^{-3}$. Clearly, nucleation experiments must take this delay into account. Also, the 'snowing' effect in CVD reactors, i.e. sudden, unpredictable particle formation, can be explained by this phenomenon. When operating the reactor in the neighbourhood of the onset of nucleation, homogeneous nucleation is postponed by an appreciable time lag but a small perturbation in the residence time or temperature might declench a sudden particle formation. Thus, performing CVD synthesis in the vicinity of these conditions, which can be seen in Fig. 3, risk encountering this 'snowing' effect.

When the saturation ratio is very large and an energy barrier to nucleation no longer exists, the steady-state cluster profile does not apply because of cluster-cluster collisions which are not included in either the classical or the kinetic model. The monomer very quickly produces a great number of clusters which coagulate. The monomer itself is then stable for growth and evaporation can be neglected. In that case the process can best be simulated using a discrete-sectional model, or with a moment model coupled to the kinetic model to account for the cluster-cluster collisions (Girshick *et al.*, 1990). Warren *et al.* (1987) state that cluster-cluster collisions should not significantly influence the nucleation rate when approximately $\ln S<0.3 \theta$ and $\ln S<0.7 \theta-2$. They state that the critical nucleus size must be at least two molecules for the homogeneous nucleation model to be applicable because when the critical nucleus size is one molecule the system is kinetically limited only by the production of the gas molecules. Equation (5) results, indeed, in $\ln S<0.3 \theta$. In the case here this applies except in the case of pure gases. When the silanes are diluted with an equal amount of $\mathrm{H}_2$, the critical nucleus size is more than two molecules and cluster-cluster collisions do not play a role. The origin of the second condition is not quite so clear. In this case, for a value of $\theta$ between 15 (at high temperatures) and 30 (at low temperatures), the second condition is automatically obeyed when the first one is obeyed.

Neglecting cluster-aerosol coagulation (scavenging) can produce errors when the aerosol surface is large and the rate of production of monomers is high (Warren and Seinfeld, 1984). It does not change the temperature for the onset of nucleation. The cluster-aerosol coagulation is especially important when calculating simultaneous nucleation, coagulation and condensation. In order to estimate the monomer production rate, the kinetic parameters of the silane decomposition must be known. Alam and Flagan (1986) and Flint and Haggerty (1990) agree that the most important reaction is the initial silane decomposition reaction which produces silylene, $\mathrm{SiH}_2$, resulting in the following kinetic expression at atmospheric pressure:

$$
\frac{\mathrm{d}\left[\mathrm{SiH}_{4}\right]}{\mathrm{d} t}=-1.26 \times 10^{14} \exp \left(\frac{-28100}{T}\right)\left[\mathrm{SiH}_{4}\right]. \tag{13}
$$

From this expression both the $\mathrm{SiH}_4$ decrease and the monomer increase can be calculated. Since systems with an increase in temperature are of interest here, the $\mathrm{SiH}_4$ decrease with $\mathrm{d} T / \mathrm{d} t$ ratios from 1 to $10^{9} \mathrm{~K} \mathrm{~s}^{-1}$ has been calculated. In Fig. 6, the temperature at which an arbitrary fraction, $1 \%$, of the $\mathrm{SiH}_4$ is still left is shown. In Fig. 7, the $\mathrm{SiH}_4$ decrease is displayed for $\mathrm{d} T / \mathrm{d} t=10^{6} \mathrm{~K} \mathrm{~s}^{-1}$. The dilution of $\mathrm{SiH}_4$ with another gas does not alter these figures. From this it becomes clear that the higher the heating rate, the higher the temperature at which the $\mathrm{SiH}_4$ seems to decompose. As an illustration Haggerty (1984), heating pure $\mathrm{SiH}_4$ with a laser at rates of $10^{5}-10^{7} \mathrm{~K} \mathrm{~s}^{-1}$, found the temperatures for the onset of nucleation to be between 1200 and 1400 K. This agrees well with the results found here. Also the slope of the $\mathrm{SiH}_4$ decomposition curve becomes steeper with increasing heating rate, thus the decomposition takes place in a smaller time. For $\mathrm{d} T / \mathrm{d} t=10^{6} \mathrm{~K} \mathrm{~s}^{-1}$ the decomposition takes place in 3 ms. From these figures an average monomer production rate in this 3 ms interval is calculated to be $2 \times 10^{21}$ molecules $(\mathrm{cm}^{3} \mathrm{~s})^{-1}$ for pure $\mathrm{SiH}_4$, which is a

![](./images/812394874056736770_8.jpg)

Fig. 6. The temperature at which 99% of the SiH₄ is decomposed at different rates of temperature rise, dT/dt.

![](./images/812394874056736770_9.jpg)

Fig. 7. SiH₄ decomposition with increasing temperature, dT/dt = 10⁶ K s⁻¹.

very high rate compared to the ordinary aerosol formation processes. The minimum decomposition rate was used here since there is some indication that the activation energy decreases at high temperatures (Tao and Hunt, 1992). Therefore, at small temperature rises and low decomposition temperatures the nucleation process is itself rate limiting. With high dT/dt ratios the kinetic retardation of the SiH₄ decomposition causes the nucleation to start at a higher temperature than that calculated using nucleation models. The nucleation then takes place in a 'burst', since all the SiH₄ will decompose in a very short time scale at a temperature at which the nucleation rate is very high. In that case coagulation is very important and the highly concentrated aerosol is not stable.

## 6. CONCLUSIONS

The conversion ratio and the nucleation potential of silicon in the Si–H–Cl system are calculated for a wide range of compositions and temperatures. As the temperature rises the nucleation potential decreases which is contrary to experimental observations of particle formation at increasing temperatures. Therefore, the nucleation potential is not the only relevant parameter in predicting particle formation. The calculation of supersaturation in chemical reacting systems is illustrated. The nucleation rate was calculated using a temperature-dependent surface tension and a modified classical nucleation model (Girshick *et al.*, 1990). This agrees well with reported values of the onset of nucleation in spite of conditions typically thought to cause difficulties in using the existing nucleation models. These are high supersaturation ratio and low silicon partial pressure at low temperatures and *vice versa* at high temperatures. It is shown that $\text{H}_2$ dilution lowers the nucleation rate. $\text{SiH}_2\text{Cl}_2$ and $\text{SiH}_4$ show similar behaviour but $\text{SiHCl}_3$ shows appreciable nucleation rates only on dilution with $\text{H}_2$. Thus, this model is more useful than the nucleation potential for establishing nucleation regions in the space of temperature and gas composition. It is especially useful in systems where particle formation is unwanted, as in the micro-electronics industry.

The nucleation time lag, when calculated using a theoretical model, is shown to be substantial in the vicinity of the onset of nucleation and at high silane concentrations. The decomposition kinetics of the silane is found to be important in systems with a very fast temperature rise, for example a laser-heated gas. In that case, the silane decomposes at higher temperatures than the onset of nucleation temperature, resulting in a burst of nucleation because of the extremely high monomer production rate. Thus, the figures depicting the onset of nucleation temperature are usefull in distinguishing between the regions with appreciable particle formation above a certain temperature and the regions without particle formation. These regions are separated by a zone with a possible tendancy to exhibit the 'snowing' effect due to the relatively elevated values of the time lag. The onset of nucleation temperature range from circa 800 K in the case of pure $\text{SiH}_4$ and $\text{SiH}_2\text{Cl}_2$ until circa 1400 K on $\text{H}_2$ dilution with a factor $10^5$. $\text{SiHCl}_3$ does not show significant particle formation at temperatures lower than 1300 K.

Acknowledgements—This research was supported by a grant from the Netherlands Ministry of Economic Affairs in the framework of the Innovation Directed Research Programs (IOP-Ceramics) and also by DSM. We are grateful to Prof. Sotiris Pratsinis for helpful suggestions during the final revision of this article.

## REFERENCES

Alam, M. K. and Flagan, R. C. (1986) *Aerosol Sci. Technol.* **5**, 237.
Allen, K. D. and Sawin, H. H. (1986) *J. electrochem. Soc.* **133**, 421.
Bauer, R. (1991) Laser chemical vapor precipitation of ceramic powders. Ph.D. thesis, Delft University of Technology.
Bauer, R., Becht, J. G. M., Kruis, F. E., Scarlett, B. and Schoonman, J. (1991) *J. Am. Ceram. Soc.* **74**, 2759.
Erikson, G. (1975) *Chem. Scripta* **8**, 100.
Eversteijn, F. J. (1971) *Philips Res. Rep.* **26**, 134.
Flint, J. H. and Haggerty, J. S. (1990) *Aerosol Sci. Technol.* **13**, 72.
Girshick, S. L., Chiu, C. P. and McMurry, P. H. (1990) *Aerosol Sci. Technol.* **13**, 465.
Haggerty, J. S. (1984) Sinterable ceramic powders from laser heated gas phase reactions and rapidly solidified ceramic materials. Report MIT-EL 84-009 MIT, Cambridge.
Herrick, C. S. and Woodruff, D. W. (1984) *J. electrochem. Soc.* **131**, 2417.
Kato, A., Hojo, J. and Okabe, Y. (1981) *Memoirs of the Faculty of Engineering*, Kyushu University **41**, 319.
Katz, J. L. and Donohue, M. D. (1982) *J. Colloid Interface Sci.* **85**, 267.
Katz, J. L. and Wiedersich, H. (1977) *J. Colloid Interface Sci.* **61**, 351.
Kristyan, S. and Olson, J. A. (1991) *J. phys. Chem.* **95**, 921.
Kruis, F. E. (1993) Particle formation in a laser-heated aerosol reactor. Application to silicon and silicon nitride synthesis. Ph.D. thesis, Delft University of Technology.
Kruis, F. E., Scarlett, B., Bauer, R. A. and Schoonman, J. (1992) *J. Am. Ceram. Soc.* **75**, 619.
Levin, E. S., Gel'd, P. V. and Baum, B. A. (1966) *Russian J. phys. Chem.* **40**, 1455.
Mezey, L. Z. and Giber, J. (1982) *Surface Sci.* **117**, 220.
Nguyen, H. V., Okuyama, Y., Mimura, T., Kousaka, Y., Flagan, R. C. and Seinfeld, J. H. (1987) *J. Colloid Interface Sci.* **119**, 491.
Okuyama, K., Kousaka, Y., Warren, D. R., Flagan, R. C. and Seinfeld, J. H. (1987) *Aerosol Sci. Technol.* **6**, 15.

Pound, G. M., Nishioka, K., and Lothe, P. (1971) Theory of homogeneous nucleation from the vapour. In: *Surface Chemistry and Colloids* (Edited by Kerker, M.), Ser. 1, p. 147.

Reiss, H., Mirabel, P. and Whetten, R. L. (1988) *J. phys. Chem.* **92**, 7241.

Shi, S., Seinfeld, J. H. and Okuyama, K. (1990) *Phys. Rev. A* **41**, 2101.

Tao, M. and Hunt, L. P. (1992) *J. electrochem. Soc.* **139**, 806.

Warren, D. R., Okuyama, K., Kousaka, Y., Seinfeld, S. and Flagan, R. C. (1987) *J. Colloid Interface Sci.* **116**, 563.

Warren, D. R. and Seinfeld, J. H. (1984) *Aerosol Sci. Technol.* **3**, 135.

Zettlemoyer, M. (1969) *Nucleation*. Dekker, New York.