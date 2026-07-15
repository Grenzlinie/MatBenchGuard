![](./images/813123853029998593_1.jpg)

Int. J. Heat Mass Transfer. Vol. 39, No. 16, pp. 3453-3464, 1996
Copyright © 1996 Elsevier Science Ltd
Printed in Great Britain. All rights reserved
0017-9310/96 $15.00+0.00

0017-9310(95)00396-7

# High pressure vaporization of LOX droplet crossing the critical conditions

PIERRE HALDENWANG, COLETTE NICOLI and JOËL DAOU

Institut de Recherche sur les Phénomènes Hors Equilibre, UMR-CNRS 138, Université de Provence,
Centre de St-Jérôme, Service 252 (F) 13397 Marseille Cedex 20, France

(Received 24 April 1995 and in final form 30 October 1995)

**Abstract**—Vaporization of liquid $O_2$ droplet in quiescent high-temperature and high-pressure $H_2$ gas is numerically investigated. Classical thermodynamic modeling of high pressure mixtures allows us to study the transition from subcritical to supercritical vaporization regime. It is observed that subcritical vaporization can be obtained up to pressures several times the oxygen critical pressure. Respective domain of both regimes is determined vs temperature and pressure. Border region corresponds to minimum value of droplet lifetime. This results from two cooperative phenomena: transient effect and thermodynamic property of mixtures. Sensitivity analysis additionally shows that state of art in dense fluid transport modeling yields results that should be considered accurate only as far as orders of magnitude are concerned.

Copyright © 1996 Elsevier Science Ltd.

## 1. INTRODUCTION

Droplet vaporization and combustion at high pressure are involved in many practical engines. In several industrial applications (like diesel engines, rocket engines) the pressure of the combustion chamber is even higher than the critical pressure of the fuel. To achieve optimal design, further investigations are required in the field of droplet vaporization and combustion in supercritical regime. This theme has been the subject of particular attention over the past few years in the field of experiments [1, 2] as well as theoretical approaches [3–5].

Previous theoretical investigations by Spalding [6], Rosner [7], Sanchez-Tarifa *et al.* [8], Lazar and Faeth [9] and Rosner and Chang [10] have shown that during the vaporization or combustion a droplet can approach and exceed its critical point when ambient pressure is sufficiently high (of the order of twice the critical pressure of the pure component of the droplet). It has been pointed out that specific high pressure phenomena like solubility of ambient gases in the liquid phase, thermodynamic non idealities and property variations cannot be neglected in studies of droplet vaporization in near critical conditions. These works have been the subject of review articles by Law [11] and Sirignano [12].

Successive numerical investigations by Manrique *et al.* [13], Curtis *et al.* [14] and Scherrer [15] have considered this problem with an increasing complexity of thermodynamic model for liquid-vapour coexistence. Hsieh *et al.* [16] have provided an analysis of droplet vaporization that can correctly study the near critical vaporization process. One can also find in Farrel *et al.* [17], Litchfort *et al.* [18] and Delplanque *et al.* [5] thermodynamic models that have permitted the approach of high pressure regimes. More recently, Curtis *et al.* [3] and Yang *et al.* [19, 20] have extended previous works [14, 16] to higher temperature and pressure environment. Among those contributions, references [19] and [20] contain results useful for the sake of quantitative comparison with the present work.

Our purpose is to furnish a deeper insight into both subcritical and supercritical regimes. The investigation is carried out in the framework of cryogenic rocket engines: we are concerned with the numerical study of an isolated droplet of liquid oxygen (LOX droplet), in a stagnant hot gas composed of hydrogen. We scan a pressure range much higher than the critical pressure of pure oxygen. The cryogenic droplet heated by the ambient gas, vaporizes while the surface temperature increases. The present work provides the conditions (pressure and ambient temperature) for which the interface disappears during the droplet lifetime, i.e. critical state is reached at the droplet surface.

A few words are also given about the ways the droplet surface crosses the mixture critical conditions. Because of the large influence of the selected transport models, we restrict the description of the transition to a qualitative aspect. However careful attention is numerically devoted to this aspect, because the transition may be non-trivial (as the fact that latent heat vanishes at critical state seems to indicate).

Our high pressure modeling contains obvious weak points. We consequently perform sensitivity analysis to the selected models. Furthermore, droplet lifetimes which strongly depend on transport properties in both domains (subcritical and supercritical) are quantitatively studied. We have conducted a rather large amount of parametric studies that allow us to propose physical interpretations of the observed phenomena.

## NOMENCLATURE

|  |  |  |  |
| --- | --- | --- | --- |
| $C_{\text{p}_i}$ | partial specific heat of species $i$ | $Y$ | mass fraction of $\text{O}_2$ |
| $D$ | molecular diffusivity of $\text{O}_2$ in the mixture | $Y_i$ | mass fraction of species $i$. |
| $D_{\text{im}}$ | molecular diffusion coefficient of species $i$ in the mixture | **Greeks** |  |
| $h_i$ | partial enthalpy of formation | $\kappa$ | thermal diffusivity |
| $J_{\text{diff}}^i$ | mass diffusive flux of species $i$ | $\lambda$ | thermal conductivity |
| $J_i$ | mass flux of species $i$ | $\rho$ | density |
| $Le$ | Lewis number $(\kappa/D)$ | $\tau_{\text{life}}$ | non-dimensional droplet lifetime |
| $m$ | vaporized mass rate per unit area | $\tau_\kappa$ | thermal diffusive time. |
| $m^*L$ | heat flux required for phase change | **Subscripts** |  |
| $P$ | chamber pressure | $i$ | value of species $i$ ($i = \text{O}_2$ or $\text{H}_2$) |
| $r$ | space variable | $\text{c}$ | critical value |
| $t$ | time | $\text{liq}$ | liquid value |
| $t_{\text{life}}$ | droplet lifetime | $\text{s}$ | interface value |
| $T$ | temperature | $\text{vap}$ | vapour value |
| $T_0$ | initial temperature in the liquid | $0$ | values at initial time |
| $v$ | flow radial velocity | $\infty$ or $\text{inf}$ | values at $r = \infty$. |

As a matter of fact, our results at high ambient temperature show a close similarity with experiments of droplet combustion by Faeth *et al.* [21], Sato *et al.* [1, 2] and Chauveau *et al.* [22]: the droplet lifetime exhibits a minimum when pressure becomes such that subcritical regime is no longer allowed. Because this minimum value is observed at the transition between both regimes we have called this effect "transcritical minimum". We propose an attempt to interpret this phenomena.

## 2. THE MODEL

We consider a single, spherical, cold droplet of $\text{O}_2$ heating up and vaporizing in a quiescent hot $\text{H}_2$ environment at high pressure, as in zero gravity experiments. Initially, the pure liquid droplet (of radius $r_0$) has a uniform temperature $T_0$ (100 K) and is surrounded by a hot ambient gas, at temperature $T_\infty$ (in the range 500 K-2500 K). The droplet vaporization process produces a Stefan flow. The velocity of this flow has a negligible magnitude compared with the speed of sound. Therefore isobaric hydrodynamics is assumed. The modeling follows the classical thermodynamic procedure, except for mixture heat capacity that requires special attention. This is one of the weak points of the model. The other ones are related to transport coefficients in dense mixtures for which kinetics theory of gases is no longer valid.

### 2.1. Model for subcritical vaporization regime
At a given pressure and for the equation of state $\rho = f(T, Y)$, the problem is to find the conditions for the existence of an interface by solving:

(i) the spherical temperature field determined as solution of

$$
\rho C_{\text{p}}\left[\frac{\partial T}{\partial t}+(\vec{V} \cdot \vec{\nabla}) T\right]=\vec{\nabla} \cdot(\lambda \vec{\nabla} T)-\left(\sum_{i=1}^{2} \overline{J_{\text{diff}}^i} C_{\text{p}_i}\right) \vec{\nabla} T
\tag{1}
$$

where $C_{\text{p}_i}$ is the partial specific heat of species $i$. Therefore specific heat of the mixture is given by

$$
C_{\text{p}}=\sum_{i=1}^{2} C_{\text{p}_i} Y_i
\tag{2}
$$

where $Y_i$ is the mass fraction of species $i$.

$\overline{J_{\text{diff}}^i}$, the mass diffusive flux of species $i$ is defined by the Fick law

$$
\overline{J_{\text{diff}}^i}=-\rho D_{\text{im}} \vec{\nabla} Y_i
\tag{3}
$$

where $D_{\text{im}}$ is the molecular diffusive coefficient of species $i$ in the mixture;

(ii) the oxygen mass fraction field determined as a solution of

$$
\rho\left[\frac{\partial Y}{\partial t}+(\vec{V} \cdot \vec{\nabla}) Y\right]=\vec{\nabla} \cdot(\rho D \vec{\nabla} Y)
\tag{4}
$$

$Y$ and $D$ are the mass fraction and the molecular diffusive coefficient of the species $\text{O}_2$ in the mixture, respectively;

(iii) the radial velocity field, or Stefan flow, governed by the mass conservation equation

$$
\frac{\partial \rho}{\partial t}+\vec{\nabla} \cdot(\rho \vec{V})=0
\tag{5}
$$

where $\rho$ is given by classical cubic equation of state for mixtures [23].

At the droplet surface the matching conditions are :
* the mass balance for the mixture:
$$
\begin{aligned}
m & =\rho_{\mathrm{liq}}\left(T_{\mathrm{s}}, Y_{\mathrm{s}}\right)\left(v_{\mathrm{liq}}\left(r_{\mathrm{s}}\right)-\mathrm{d} r_{\mathrm{s}} / \mathrm{d} t\right) \\
& =\rho_{\mathrm{vap}}\left(T_{\mathrm{s}}, Y_{\mathrm{s}}\right)\left(v_{\mathrm{vap}}\left(r_{\mathrm{s}}\right)-\mathrm{d} r_{\mathrm{s}} / \mathrm{d} t\right)
\end{aligned} \tag{6}
$$

* the energy balance:
$$
\lambda_{\mathrm{liq}}\left(\frac{\partial T}{\partial n}\right)_{\mathrm{liq}}+m^{*} L\left(T_{\mathrm{s}}, Y_{\mathrm{s}}\right)=\lambda_{\mathrm{vap}}\left(\frac{\partial T}{\partial n}\right)_{\mathrm{vap}} \tag{7}
$$

where the quantity $m^{*} L\left(T_{\mathrm{s}}, Y_{\mathrm{s}}\right)$ refers to the energy flux transferred through the interface, in order to pro- vide the enthalpy of vapour phase formation. This global quantity is related to partial enthalpies and total species mass fluxes by
$$
\begin{aligned}
-m^{*} L(T, Y)=\left(\bar{h}_{\mathrm{vap}, \mathrm{O}_{2}}-\bar{h}_{\mathrm{liq}, \mathrm{O}_{2}}\right) J_{\mathrm{O}_{2}} & \\
+ & \left(\bar{h}_{\mathrm{vap}, \mathrm{H}_{2}}-\bar{h}_{\mathrm{liq}, \mathrm{H}_{2}}\right) J_{\mathrm{H}_{2}} \tag{8}
\end{aligned}
$$
with
$$
J_{i}=\left(m Y_{i}-\rho(T, Y) D_{\mathrm{im}} \frac{\partial Y_{i}}{\partial n}\right)_{\mathrm{liq}} \tag{9}
$$

* the balance of oxygen mass :
$$
\left(m Y_{i}-\rho(T, Y) D \frac{\partial Y}{\partial n}\right)_{\mathrm{liq}}=\left(m Y-\rho(T, Y) D \frac{\partial Y}{\partial n}\right)_{\mathrm{vap}} \tag{10}
$$

* the liquid-gas interface (or droplet surface) is the locus where the thermodynamic equilibrium con- ditions are met for the mixture. This appears as a coexistence relationship between, for instance, the three following quantities: $\mathscr{F}\left(P, T_{\mathrm{s}},\left(Y_{\mathrm{s}}\right)_{\mathrm{vap}}\right)=0$. We derive the latter equation from thermodynamic model in the following classical way [23]. The Redlich- Kwong-Soave cubic model for pure component is firstly chosen. Then, using classical rules for mixtures, an equation of state for binary mixture is derived. The phase equilibrium relationship at interface is after- wards obtained by specifying that temperature, pres- sure and fugacities of each species are identical in both phases. The model is now complete because fugacity and partial enthalpy of formation can be expressed as functions of the mixture equation of state. The equilibrium liquid-vapour diagram of the $\mathrm{H}_{2}-\mathrm{O}_{2}$ mix- ture is plotted on Fig. 1, for several pressure values. There is however no experimental data for validating this thermodynamic modeling. Nevertheless, exper- imental data can be found for the $\mathrm{H}_{2}-\mathrm{N}_{2}$ cryogenic mixture that is close to the present one. A good agree- ment has been noticed [5,24] for the $\mathrm{H}_{2}-\mathrm{N}_{2}$ mixture between experimental data and classical ther- modynamic modeling.

* The boundary conditions to be satisfied are
$$
\text { at } r=\infty \quad T=T_{\infty} \quad Y=0
$$

![](./images/813123853029998593_2.jpg)

Fig. 1. Diagram of liquid-vapour equilibrium in the plane "temperature/O₂ mass fraction" for O₂-H₂ mixture at a given pressure.

$$
\text { at } r=0 \quad \partial T_{\text {liq }} / \partial r=\partial Y_{\text {liq }} / \partial r=0 \text {. }
$$

* Most of transport properties of the pure fluids $\mathrm{O}_{2}$ and $\mathrm{H}_{2}$ are evaluated from Gas Encyclopaedia [25]. For estimating $C_{\mathrm{p}}$, the mixture heat capacity, relation (2) is used with two different ways of evaluation of $C_{\mathrm{p}, i}$, the partial heat capacities of species $i$ in the mixture. On the one hand, from the mixture equation of state it is possible to derive a theoretical expression of $C_{\mathrm{p}}$ [26]. This way presents however a major draw- back which corresponds to the limitation of such a thermodynamic modeling: for a given pressure there is a particular mixture composition, called mixture pseudo-critical point, for which the quantities $C_{\mathrm{p}, i}$ diverge. This approach remains practicable as long as the actual composition and temperature fields are in such a way that no space point meets the vicinity of the pseudo-critical conditions. On the other hand, in order to overcome the latter drawback, relation (2) can be used by identifying the partial heat capacities with the heat capacities of each pure substance. Those have been extracted from [25]. Actually this procedure corresponds to an acceptable approximation except in the vicinity of the critical conditions of pure sub- stances at which the value again diverges. This is the reason why we have preferentially performed the study when this singular behaviour is erased. This leads to the so-called "smoothed $C_{\mathrm{p}}$ " results. Additionally, for the sake of sensitivity study, we shall furnish further comparisons when perfect gas assump- tion for heat capacities is assumed.

* Let us now consider the transport modeling which also contains several weaknesses. Firstly, for the time being and as all previous contributions, we do not take into account any of the singular behaviours [27, 28] of transport coefficients in the vicinity of the mix- ture critical conditions. Furthermore there are several orders of magnitude between binary diffusion coefficients in liquid and gas. Therefore it seems impossible, due to the lack of experimental data, to perform a continuous modeling (when liquid-vapour interface disappears) that would connect a gas-like

fluid to a liquid-like fluid. Consequently we have used for binary diffusion coefficient, in liquid and dense gas, empirical correlations that can be found in ref- erence [23]. As for thermal conductivity, we have used standard mixing rules [29] applied to the values of pure substances established from experimental data. Mixture thermodynamic and transport property evaluation methods are summarized in Appendix.

Our present problem, that can be called 'Stefan problem in mixture', presents some technical diffi- culties: the localization of the interface, conceived as a free surface, requires dynamical adaptation of grid and a space-time transformation of mesh. Numerical solution is achieved by using a second order space- time discretization. The global scheme is implicit and carried out in the framework of finite volume methods [30]. Furthermore, $v_{s}$ , the gas flow velocity at the drop let surface and one of the thermodynamic quantities at the interface have to be seen as 'eigenvalues' of the problem. Hence, at each time step, a numerical algorithm involving Newton-Raphson iterative tech- nique is used to solve the differential system completed by the set of equilibrium relationships at interface. Therefore, at each time step the iterative procedure is stopped when regression rate and surface temperature have converged.

### 2.2. Model for the supercritical vaporization regime
If the critical point of the binary mixture (which only depends on the chamber pressure) is reached during the regression of the droplet, the interface van- ishes. From this instant on, integration of con- servation laws is carried out continuously from the droplet centre to the quiescent infinity. Unlike the subcritical vaporization where temperature field and mass fraction field have to satisfy at the interface the constraint of liquid-vapour coexistence, in the supercritical regime no particular relationship is imposed to both fields. The numerical problem is then reduced to a spherical convection-diffusion problem in a single fluid phase. The vaporization process can be seen either as a heating process or a mixing process. According to our interest relative to these processes, we can define the supercritical droplet as follows. On the one hand, if we consider the transformation of a cold 'puff' in a lighter fluid, we shall retain as droplet border the locus where the temperature is the mixture critical one (i.e. $T_{s}=T_{c}$ ). On the other hand, if we are interested in mixing process, preceding combustion for instance, we shall define as droplet the loci where the $O_{2}$ mass fraction is higher than $Y_{c}$ , the mixture critical value (i.e. we set $Y_{s}=Y_{c}$ ).

For the sake of comparison with vaporization experiments in presence of combustion we select the point of view of mixing. In that case, from the critical instant on, we shall follow the locus where $Y_{s}=Y_{c}$ in order to determine the droplet radius.

## 3. RESULTS
We have performed an extensive study of both vaporization regimes with respect to the most impor- tant parameters, i.e. temperature and pressure of chamber. Particularly, we focus our attention on the dependence of droplet lifetime on pressure. The reason for this interest is due to several experiments by Faeth et al. [21], by Sato et al. [1] and very recently by Chauveau et al. [22]. These authors have observed that a minimum of the droplet lifetime in presence of combustion is attained for pressures in the vicinity of the fuel critical pressure. Although these experiments dealt with hydrocarbons, our purpose is to suggest physical interpretations for these observations.

We shall call subcritical regime the vaporization process for which the mass fraction at interface remains higher than the mixture critical value (and consequently, the surface temperature remains lower than the corresponding critical temperature) during the whole droplet lifetime. On the other hand, the "supercritical regime" will correspond to a vapo- rization process for which the subcritical period lasts a negligible part compared with whole droplet lifetime. The latter case typically appears in a chamber at high pressure and high temperature.

Most of our results will be presented in non-dimen- sional form. It is worth noticing that elementary dimensional analysis yields the following obviousness. The unique time scale that can be built from the physi-cal parameters of this problem has the form :
$$\tau_{\mathrm{D}}=r_{0}^{2} / D\qquad(11)$$
where $D$ is a typical diffusion coefficient. We shall set $D=\kappa, \kappa$ being the thermal diffusivity of the hot gas phase far from the droplet. Therefore, the Vashy- Buckingham theorem (or $\Pi$ -theorem) allows us towrite $t_{char }$ , any characteristic time, as :
$$t_{\text {char }}=\tau_{\kappa} \Phi\left(\Pi_{1}, \Pi_{2}, \Pi_{3}, \ldots, f_{1}, f_{2}, f_{3}, \ldots\right) \quad(12)$$
with $\tau_{\kappa}=r_{0}^{2} / \kappa$ and where the $\Pi_{i}$ are non-dimensional numbers like the Lewis number, the ratio of gas and liquid densities, the ratio of enthalpy of formation to some energy of reference, etc. The functions $f_{i}$ are non dimensional fields traducing the non-constancy of the physical properties. As illustration, note that the classical Godsave [31]-Spalding [33] formula for $\tau_{GS}$ , the droplet reduced lifetime, just requires two numbers $\Pi_{1}$ and $\Pi_{2}$ . In this manner it reads :
$$\tau_{\mathrm{GS}}=\Phi\left(\Pi_{1}, \Pi_{2}\right)=\frac{1}{2} \Pi_{1}\left[\log \left(1+\Pi_{2}\right)\right]^{-1} \quad(13)$$
where $\Pi_{1}$ is the ratio of the liquid density to the gas density and $\Pi_{2}$ is nothing but the Spalding number. Note moreover that the dependence of $\Phi$ on $\Pi_{2}$ is a slow varying function provided that $\Pi_{2}$ is sufficiently large; the latter condition is fulfilled with a high tem- perature environment.

### 3.1. Subcritical regime
This regime naturally appears at low pressure and has been the subject of a large number of important contributions [31-33] that have established the quasi- steady vaporization model. Furthermore several

![](./images/813123853029998593_3.jpg)

Fig. 2. $T_{\mathrm{s}}$, the interface temperature vs non-dimensional time ($T_{0}=100 \mathrm{~K}, T_{\infty}=1000 \mathrm{~K}, P=8 \mathrm{MPa}$): subcritical case.

theoretical works [7, 10, 32] have stated that the more the pressure increases the more questionable is the assumption of quasi-steadiness. Our purpose is to quantitatively determine the existence domain of sub- critical regime for LOX droplets. We shall also try to qualify the degree of unsteadiness in this domain.

As illustration, we present results obtained when a liquid $\mathrm{O}_{2}$ droplet, initially at $100 \mathrm{~K}$, evaporates in a chamber at 80 bars and $1000 \mathrm{~K}$. First of all, note that the mixture critical temperature at 80 bars is $147 \mathrm{~K}$, accordingly to Fig. 1. The numerical simulation shows that the temperature of the droplet surface increases continuously from $100 \mathrm{~K}$ to $146.5 \mathrm{~K}$, as seen on Fig. 2 where time is normalized by $\tau_{\kappa}$, the thermal diffusion characteristic time (here $\tau_{\kappa} \approx 6 \times 10^{-4} \mathrm{~s}$ for $r_{0}=100$ $\mu \mathrm{m}$). The highest temperature value is obtained at the end of the droplet life-that we conventionally define as the instant when $97 \%$ of the initial liquid mass is evaporated. This value of $146.5 \mathrm{~K}$ is very close to the critical value: the interface temperature reaches the critical value just at the end of its lifetime. These results confirm that at high pressure no quasi-steady state exists [3, 5, 16, 32]. Nevertheless, our simulation proves that the famous " $D^{2}$ law" remains valid during an important part of the vaporization period. This fact can be observed in Fig. 3 where the quantity $r_{\mathrm{s}}^{*} \mathrm{~d} r_{\mathrm{s}} / \mathrm{d} t$ is plotted vs non-dimensional time. From time $t=6$ on, this quantity appears as quasi-constant. Note that at $t=6$ less than $20 \%$ of the liquid mass is evaporated. Consequently, we can consider that some degree of quasi-steadiness is attained.

![](./images/813123853029998593_4.jpg)

Fig. 3. Validity of the " $D^{2}$ law" in the subcritical regime: time derivative of droplet radius multiplied by radius is plot- ted versus non-dimensional time ($T_{0}=100 \mathrm{~K}, T_{\infty}=1000 \mathrm{~K}$, $P=8 \mathrm{MPa}$).

![](./images/813123853029998593_5.jpg)

Fig. 4. "Trajectories" of the scalar fields in the $(T, Y)$ diagram. Curves are respectively the solutions after 1,6 and 33 time units ($T_{0}=100 \mathrm{~K}, T_{\infty}=1000 \mathrm{~K}, P=8 \mathrm{MPa}$).

Umemura [27, 28] has suggested presenting the his- tory of the vaporization with the help of a set of curves in the $(T, Y)$ diagram. This is carried out, at a given instant, by eliminating $r$, the space variable, between the temperature and mass fraction instantaneous fields. Figure 4 presents, at three different instants ($t=1$, $t=6$ and $t=33$), the characteristic states of the mixture (temperature and $\mathrm{O}_{2}$ mass fraction), to- gether with the liquid-vapour coexistence curve. Below this dotted curve, the state corresponds to the gaseous phase, while above the mixture is in the liquid state. As time increases, the surface conditions get closer to the mixture critical conditions as illustrated on Fig. 4 by the curve at time $t=33$ which corresponds to the end of droplet lifetime.

At this point it is important to estimate how far the low pressure model by Spalding and Godsave can be usable. In this way, we need to establish what is the Spalding number in our problem. We decide to definethis number as follows:

$$
\begin{aligned}
B=\Pi_{2}=\left(C_{\mathrm{p}}\right)_{\infty}\left(T_{\infty}-\left\langle T_{\mathrm{s}}\right\rangle\right) \cdot & {\left[\left(C_{\mathrm{p}}\right)_{\mathrm{liq}}\left(\left\langle T_{\mathrm{s}}\right\rangle-T_{0}\right)\right.} \\
& \left.+\left\langle m^{*} L\right\rangle /\langle m\rangle\right]^{-1} \quad(14)
\end{aligned}
$$

where the symbol $\langle\cdot\rangle$ means the time averaged value of respectively, $T_{\mathrm{s}}$ the surface temperature, $m^{*} L$ the heat flux required for phase change and $m$ the vapo- rized mass of liquid. Rough estimate of equation (14) from our numerical results (always for $p=80$ bars and $T_{\infty}=1000 \mathrm{~K}$) gives: $B=64$. Reported in equation (13), this quantity, together with $\Pi_{1}=\rho_{\text {liq }} /$ $\rho_{\infty}=600$, leads to a non-dimensional droplet life- time $\tau_{\text {liq }}(r=0.3)=\left[1-(0.3)^{2}\right] \tau_{\mathrm{GS}}(r=0)=65$. This value compared with 33, the numerical result, shows that equation (13) almost preserves the order of magnitude of the lifetime. Further comparisons show that the Godsave-Spalding model, although it

![](./images/813123853029998593_6.jpg)

Fig. 5. Interface temperature at the end of droplet lifetime vs pressure for several temperatures of chamber. The solid line is the projection on the $(P, T)$ plane of the $O_{2}-H_{2}$ mixture critical line.

assumes the constancy of all physical properties, is nevertheless an acceptable guide (if $\langle T_{\mathrm{s}}\rangle$ is known!) for predicting the qualitative behaviours in the subcritical regime.

A parametric study of the subcritical domain has been carried out for various pressures and temperatures of the chamber. In Fig. 5, the final surface temperature of all subcritical regimes is reported with respect to pressure. We observe that the final surface temperature increases with pressure until the representative point $(P, T_{\mathrm{s}})$ intersects the projection of the mixture critical line on the $(P, T)$ plane. Retaining on Fig. 5 the intersection point of each curve with the projected critical line, we obtain for a given surrounding temperature the pressure corresponding to the limit of the subcritical vaporization domain. This allows us to plot on Fig. 6 the curve (solid line) limiting the subcritical domain. Of course this curve is very sensitive to the modeling. In order to illustrate this point, we have considered two opposite modelings of mixture heat capacity. On Fig. 6 the already mentioned solid line corresponds to the application of equation (2) with heat capacities of pure substances obtained from experimental data [25]. On the other hand, the dashed line on Fig. 6 results from the same computation with a gas phase owing the heat capacity of perfect gases. Although the discrepancy is relatively large $(20 \%)$, the following qualitative result seems to be quite robust: subcritical regime can be observed for ambient pressures much higher than the critical pressure of pure oxygen. The latter point is in agreement with previous works [5, 7, 20, 34].

![](./images/813123853029998593_7.jpg)

Fig. 6. Transcritical pressure vs temperature of chamber (i.e. conditions of chamber for which critical state is attained just as the droplet disappears): sensitivity analysis with respect to both modelings of mixture heat capacity (see text).

### 3.2. Transition to supercritical regime
According to the selected transport modelings, we can observe two ways for crossing the critical conditions. One way exhibits a weak singular behaviour. Its appearance is very sensitive to all the weak points of the modeling, and because it does not quantitatively affect the droplet lifetime, we shall content ourself with a qualitative description of the transition from the subcritical regime to the supercritical one.

From the numerical point of view, the closer the droplet surface approaches the critical conditions, the more iterations are needed to obtain at each time step the convergence of the numerical procedure. At a certain discrete time (say, $t=[n+1] \Delta t$ ) this iterative procedure no longer converges. We then have the temptation to decide that the last subcritical time is $t=n \Delta t$ and the first supercritical instant is $t=[n+1] \Delta t$. However, this deserves more attention because the regression rate can strongly increase as we approach the critical conditions. To properly treat the transition, we decide to proceed as follows. If at $t=[n+1] \Delta t$ no convergence is found for the iterative system, we choose a half time step and we try to find convergence at $t=[n+1 / 2] \Delta t$. By acting recursively, we can approach closer and closer the transition. We built a series of time increments the sum of which converges towards $t_{\mathrm{c}}$, the critical instant.

As a result, during this iterative procedure we observe two distinct behaviours. When the transport coefficients are really discontinuous on both sides of the interface, the transition appears as a regular phenomenon. Conversely, if the transport coefficients are more or less continuous, as it could be envisaged when tending to a unique fluid phase, we have observed a singular behaviour: the regression rate weakly diverges at the finite time $t_{\mathrm{c}}$. More precisely, we found that $\mathrm{d} r_{\mathrm{s}} / \mathrm{d} t$ behaves as $\left(t_{\mathrm{c}}-t\right)^{-\alpha}$ with $\alpha$ a small exponent of order 0.1. Moreover, Umemura has pointed out that binary diffusion coefficient vanishes $[27,28]$ at critical point. We have studied the influence of the latter property. The result is striking in the sense that the vaporization rate is found to remain finite during all the transition.

### 3.3. Supercritical regime
When critical conditions are observed on the droplet surface, the liquid-vapour interface disappears. Thus, the supercritical regime has to be seen as the dilution of a dense, cold pocket in a light, hot environ-

![](./images/813123853029998593_8.jpg)

Fig. 7. Validity of the " $D^{2}$ law" in the supercritical case: solid line represents the droplet radius squared versus non- dimensional time $(T_{0}=100 ~K, T_{\infty}=1000 ~K, P=10 MPa)$ . Critical transition appears at about $t=0.5$ in non-dimen sional time units. Dashed line illustrates that the " $D$ " law" approximates the droplet regression most of its lifetime.

![](./images/813123853029998593_9.jpg)

Fig. 8. Density $(kg / m^{3})$ and temperature $(K)$ profiles as func tion of radial coordinate, reduced by the radius at critical instant. The profiles are drawn at $t=3$ time units, i.e. inthe supercritical regime $(T_{0}=100 ~K, T_{\infty}=1000 ~K, P=10$  MPa).

ment. All the following results concern the dilution in a rigorously quiescent chamber, because the "droplet" confinement is no longer due to surface tension but just due to inertia. Now, defining the "droplet" as the sphere where $O_{2}$ mass fraction is larger than the mixture critical $O_{2}$ mass fraction, we can study the regression rate of this pocket.

As illustration, we present the simulation of "drop- let vaporization" in a chamber at 1000 K and 100 bars. Figure 7 gives the droplet radius squared, reduced with its initial value, as a function of time reduced with the thermal diffusion characteristic time of ambient gas. It can be observed that transition occurs at about $t=0.5$ . After the transition, the drop let radius increases as the consequence of superficial thermal expansion. This is due to the fact that thermal transfer in dense fluid is more efficient than mass diffusion (Lewis number larger than one). It can be noticed that the " $D$ law" is almost satisfied in the supercritical regime.

Furthermore, our results confirm the previous study by Sanchez-Tarifa et al. [8] which concludes that the concept of droplet can be extrapolated in the super- critical regime. The basic reason is the large sensitivity of density to temperature in the vicinity of mixture critical point. This property implies large gas expan- sion and the related convective transport isolates the cold pocket from diffusion process. It helps to main- tain strong density gradients. This clearly appears on Fig. 8 where the radial dependence of the density and temperature fields is plotted (the distance from the droplet centre has been reduced with the droplet radius at $t_{c}$ , the time of transition).

### 3.4. Study of lifetimes in both regimes
We have carried out a parametric study of the drop- let lifetime (the droplet is initially at 100 K) for various ambient conditions. The results obtained for both regimes are reported on Fig. 9 where the dimensional lifetime of a $500 \mu m$ radius droplet is plotted as a function of pressure, reduced with the $O_{2}$ critical pres sure (i.e. 50 bars). On Fig. 9 every curve defined by a surrounding temperature presents a minimum of the lifetime in the vicinity of the pressure given by Fig. 6. In what follows this behaviour will be referred as "transcritical minimum". These results are in an inter- esting agreement with experimental results of droplet combustion obtained in micro-gravity: for the sake of qualitative comparison the measurements by Sato et al. [2] have been reported in Fig. 9. The agreement is just qualitative because the data are concerned with combustion of $n$ -octane. Nevertheless, we imagine that in such experiments a decisive factor is the mixing process of the droplet component with the combustion products.

Furthermore note that far in the supercritical regime the droplet lifetime is independent of pressure. A more quantitative study of our data at very high pressure shows that the droplet lifetime behaves as $(T_{\infty})^{-3 / 4}$ .

![](./images/813123853029998593_10.jpg)

Fig. 9. 1 mm-diameter droplet lifetime (s) vs pressure, reduced by $O_{2}$ critical pressure, for various temperature of hydrogen-filled chamber.

### 3.5. Sensitivity analysis

As mentioned before, our modeling contains several weaknesses. It is imperative to check the influence of the different hypotheses on our results. Two points will be investigated: heat capacity modeling and choice of binary diffusion coefficient. Four different approaches of the specific heat capacity will be envisaged. The plausible modelings of heat capacity have already been the subject of a detailed description in Section 2.

As for the species diffusivity, certainly the most badly known physical property, only two ways will be compared. As a result, all the available models possess the following weaknesses:

(1) For the time being the modelings proposed in the literature do not allow us to continuously connect a unique fluid having on the one side the properties of a cold liquid and on the other side the properties of a high pressure gas. This remark is also valid (to a lesser degree) for thermal conductivity.

(2) Mass transport properties at high pressure are usually studied either for self-diffusivity or for binary diffusivity of tracers of one species in the other pure species. Reliable mixing rules do not seem to exist [23] in order to extend these results to dense binary mixtures of various composition.

(3) As pointed out by Umemura [27, 28] species diffusivity should have a vanishing behaviour when crossing the mixture critical conditions. According to our experience, this property would affect the solution only during the short time of the transition. Therefore it can deeply modify the nature of the transition but cannot quantitatively affect the droplet lifetime.

First of all let us recall what is our modeling of reference. $C_{p_i}$, the partial heat capacity in the mixture is identified with the heat capacity of the species considered as a pure substance. The latter is extracted from experimental data [25]. Then we erase from $C_{p_i}$ the divergent behaviour in the vicinity of the critical conditions of pure component. The latter quantity is finally reported in equation (2) for every species. The binary diffusivity modeling, supposed as the most reliable one, has been mentioned in Section 2 and recalled in the Appendix: for the liquid phase the Wilke-Chang modification of the Stokes-Einstein law and for the gas phase the Wilke-Lee correlation suggested by gas kinetic theory. This reference modeling has been used to estimate the lifetime of a 1 mm-diameter LOX droplet in a surrounding hydrogen at 1000 K. The result is reported on Fig. 10 and corresponds to the solid line curve labelled (a) "reference results".

In Fig. 10 three other curves (b, c and d) concern the departure from the reference in term of sensitivity to heat capacity and a fifth one (e) in terms of sensitivity to binary diffusion.

Curve (b): $C_{p_i}$, the partial heat capacity in the mixture is once more identified with the heat capacity of the species considered as a pure substance. The latter is again extracted from experimental data [25], but reported without modification in equation (2) for every species. We call this curve "$C_p$: Rough data of pure substance".

Curve (c): $C_{p_i}$ is estimated from theoretical derivation of partial heat capacities. We recall that this estimate is established from the Redlich-Kwong-Soave equation of state and intrinsically contains a diverging behaviour at the pseudo-critical point. This curve is labelled "$C_p$: RKS theoretical modeling".

Curve (d): $C_{p_i}$ is derived from perfect gas theory. This approach is known to only make sense at low pressure. This curve is labelled "$C_p$: Perfect gas modeling".

Curve (e) is concerned with the measurement of the sensitivity to mass diffusivity. We deliberately choose a modeling far from the spirit of the reference one. We try to introduce some degree of continuity in the following way: inspecting the experimental data of $O_2$ and $H_2$ considered as pure gaseous substance, one can notice that $Le$, the Lewis number, more or less follows a temperature dependent rule: $Le(T)=(Le)_\infty(T/T_\infty)^{-0.25}$. We decide to allocate this property to their mixture. Then the binary diffusion coefficient of the mixture is immediately deduced from mixture thermal diffusivity. We admit that this modeling is however unfounded in the liquid phase. This curve is labelled "$D$: Continuous Lewis number".

![](./images/813123853029998593_11.jpg)

Fig. 10. Study of sensitivity: droplet lifetime (s) vs reduced pressure for four various modelings of mixture specific heat and two modelings of mass transport (see text).

According to Fig. 10, one notices that the so-called transcritical minimum corresponds to a rather robust behaviour although the quantitative effects are of the order of 30%. Note that the perfect gas assumption tends to underestimate heat capacity and therefore we are faced with a decreasing of the droplet lifetime as a consequence of overestimating thermal diffusivity. Note additionally that the curve "RKS theoretical modeling" follows the global aspect of the other curves. This proves that at every point the mixture has never approached the vicinity of the pseudo-critical point; if it were the case the lifetime would have

![](./images/813123853029998593_12.jpg)

Fig. 11. 1 mm-diameter droplet lifetime (s) vs reduced pressure: comparison with two previous works by Yang et al. [19,20] and influence of both definitions ($Y_{\mathrm{s}}=Y_{\mathrm{c}}$ or $T_{\mathrm{s}}=T_{\mathrm{c}}$) of supercritical droplet.

![](./images/813123853029998593_13.jpg)

Fig. 12. Non-dimensional droplet lifetime, multiplied by the density of hydrogen at chamber conditions, with respect to reduced pressure for various temperatures of chamber.

tremendously increased. Despite the roughness of the modification in transport modeling, the results globally remain in the same range of 30% accuracy. Although the transition appears at higher pressure, the phenomenon of "transcritical minimum" is preserved.

### 3.6. Discussing droplet lifetimes
At this point it is of interest to compare our results with previous works. Three numerical works are available in the literature. In ref. [5] the authors give just one result corresponding to the lifetime of a $100 \mu \mathrm{m}$-diameter LOX droplet in a chamber at 100 bars and 1000 K. Using equation (12) we transpose this lifetime of the order of 15 ms to a 1 mm-diameter LOX droplet. Unfortunately the latter value (1.5 s) does not have the same order of magnitude than ours (0.5 s). There are furthermore two extensive results by Yang et al. reported in two papers [19,20]. However, both contributions are for us a source of questioning because the authors reported twice the same study using an apparently identical modeling and reporting rather different results. In such a case the most recent results are supposed to be the most precise. As a matter of fact, our reference results, as shown by curve (a) on Fig. 11, are in better agreement with their oldest results [19] [reported by curve (b) on Fig. 11], especially for subcritical regime. For the sake of a better comparison we additionally decide to change our definition of the supercritical droplet. As done by these authors, we now define the supercritical droplet as the loci where the temperature is lower than the mixture critical temperature. This new computation corresponds to curve labelled "d: reference results $(T_{\mathrm{s}}=T_{\mathrm{c}})$" while our previous definition corresponds to curve labelled "a: reference results $(Y_{\mathrm{s}}=Y_{\mathrm{c}})$". According to this new definition our results present the same global aspect than the oldest ones [19] of these authors, including the absence of the "transcritical minimum". The latter property seems however exist in their most recent work [20] illustrated by curve (c), although their data are not of the same order as ours.

We are indeed faced with a large discrepancy between the different contributions (see also ref. 35). There is more than one order of magnitude between references [5] and [20]. Our results agree within a 30% range with reference [19] as far as we identically define the supercritical droplet. On the other hand a rather weak perturbation on $C_{\mathrm{p}}$ modeling produces the same range of precision, as noticeable in Fig. 10. Actually it does not seem reasonable to guarantee our present results within a range of accuracy better than 30%. The discrepancy between the various predictions recommends to perform experiments with non reactive mixtures [24] substituting for the $\mathrm{H}_{2}-\mathrm{O}_{2}$ mixture.

We also conclude from Fig. 11 that the "transcritical minimum" phenomenon is linked to the mixing definition $(Y_{\mathrm{s}}=Y_{\mathrm{c}})$ of the supercritical droplet. Renouncing to the quantitative point of view, we have now to provide us with physical interpretations.

## 4. PHYSICAL INTERPRETATION
Starting from the same results as those of Fig. 9, the lifetime is first transformed in non-dimensional form by dividing by $\tau_{\kappa}$. Then this quantity, multiplied by $\rho_{\infty}$ the density of the initial environment, is reported on Fig. 12 with respect to the reduced pressure. An interesting overlapping of the related curves appears as soon as the ambient temperature is large enough (say 1000 K). This property becomes striking at low and high pressure. In what follows, this is interpreted as the consequence of the quasi-steadiness that we have observed for both regimes.

As suggested by our results we assume that a sharp density gradient exists in the vicinity of $r_{\mathrm{s}}(t)$, the instantaneous droplet radius (whatever the definition of the droplet radius we have selected in the supercritical vaporization regime). Therefore, for $r \leqslant(1-\varepsilon) r_{\mathrm{s}}(t)$ there is a dense phase, at rest, close to the liquid state while for $r \leqslant(1+\varepsilon) r_{\mathrm{s}}(t)$ the density is that of a high pressure gas. If we perform the following

change of variable $r = ur_{\text{s}}(t)$ that makes the "interface" fixed, mass conservation law, equation (5), can be rewritten in spherical geometry as [36]:

$$
\frac{1}{r_{\mathrm{s}}^{2}(t)} \frac{\partial}{\partial t}\left(\rho r_{\mathrm{s}}^{3}(t)\right)+\frac{1}{u^{2}} \frac{\partial}{\partial u}\left[u^{2} \rho\left(v-u \frac{\mathrm{d} r_{\mathrm{s}}}{\mathrm{d} t}\right)\right]=0. \quad(15)
$$

Integrating equation (15) from $1-\varepsilon$ to $1+\varepsilon$ and assuming $\varepsilon \ll 1$, it is straightforward to derive the following conservation condition :

$$
-(1-\varepsilon)^{3} \rho_{\text {liq }} \frac{\mathrm{d} r_{\mathrm{s}}}{\mathrm{d} t}=(1+\varepsilon)^{2} \rho_{\text {vap }} v_{\text {vap }} \quad(16)
$$

in which we let $v_{\text{liq}}$, the fluid velocity in liquid phase, equal zero. Moreover $\mathrm{d} r_{\mathrm{s}} / \mathrm{d} t$, the interface regression velocity, has been neglected compared with $v_{\text{vap}}$, the velocity in gas phase. For vanishing $\varepsilon$, equation (16) is nothing but equation (6) written with both latter assumptions. Furthermore quasi-steadiness implies that the time scale in gas phase is short compared with the droplet lifetime. Therefore dimensional analysis of the problem restricted to gas phase gives, as previously discussed, the following dependence:

$$
v_{\text {vap }}=\left[\kappa / r_{\mathrm{s}}(t)\right] \Psi\left(\Pi_{2}, \Pi_{3}, \ldots, f_{1}, f_{2}, f_{3}, \ldots\right) \quad(17)
$$

where $\Psi$ does not depend on time. Hence, neglecting $\varepsilon$ compared with 1 in equation (16), we obtain the expected " $D^{2}$ law":

$$
r_{\mathrm{s}} \frac{\mathrm{d} r_{\mathrm{s}}}{\mathrm{d} t}=-\frac{\rho_{\text {vap }}}{\rho_{\text {liq }}} \kappa \Psi. \quad(18)
$$

Integration of equation (18) provides us with a rough estimate of droplet lifetime:

$$
t_{\text {life }}=\frac{1}{2} \frac{\rho_{\text {liq }}}{\rho_{\text {vap }}} \frac{r_{0}^{2}}{\kappa} \frac{1}{\Psi}. \quad(19)
$$

Assuming, as in equation (13), that $\Psi$ is a slow varying function, we are now in a position to interpret the results of Fig. 12 where the non-dimensional lifetime depends in inverse ratio to pressure. This behaviour is contained in the ratio of both densities in equation (19) because $\rho_{\text{liq}}$ is quasi-constant with respect to pressure. Furthermore, remark that the product $\rho_{\text{vap}} \kappa$ is more or less independent of pressure. Consequently, when quasi-steady regime is reached, the droplet lifetime becomes independent of pressure. This can be observed in Fig. 9 at low and high pressure, where droplet lifetime tends to be constant vs pressure. Additionally, the quantity $\rho_{\text{vap}} \kappa$ has the same dependence on temperature as the thermal conductivity. For gases as oxygen and hydrogen, it is of the order of $T^{3 / 4}$. This brings forward an explanation of the dependence of $(T_{\infty})^{-3 / 4}$ of the droplet lifetime, observed at the highest pressures on Fig. 9.

At this point, let us recall that equation (19) just refers to thermal diffusion and completely forgets mass transport. It is then quite surprising that our numerical results can be interpreted only in terms of this equation. One way to understand this fact is to remark [32] that quasi-steady assumption implies that vaporization rate is controlled by heat and mass diffusion processes in the far field where the fluid is light. Therefore, thermal and species diffusion being of the same order $[L e=\mathrm{O}(1)]$, equation (19) can hold.

![](./images/813123853029998593_14.jpg)

Fig. 13. Instantaneous droplet radius vs reduced pressure, for both definitions of supercritical "droplet" radius $(Y_{\mathrm{s}}=Y_{\mathrm{c}}$ or $T_{\mathrm{s}}=T_{\mathrm{c}}$ ), for two pressures of chamber ( $P=7 MPa$ and $P=10 MPa$ ).

Let us now discuss the so-called "transcritical minimum". On the one hand, the fact that the droplet lifetime decreases as pressure increases towards the mixture critical pressure, is classically explained by putting forward equation (13) combined with equation (14). Remember that the quantity $\langle m^{*} L\rangle$ is vanishing close to the critical point and therefore the Spalding number is increasing. On the other hand, it is clear that in the concerned pressure range the unsteady effects could not be ignored. When crossing the critical conditions the vaporization process is indeed highly unsteady because we switch from subcritical to supercritical regime. We have drawn on Fig. 13 the instantaneous droplet radius according to both definitions and for two values of pressure. It is noticeable that when transition occurs the radius is considerably enhanced when "interface at $Y_{\mathrm{s}}=Y_{\mathrm{c}}$ " is the chosen definition. Note additionally that "interface at $T_{\mathrm{s}}=T_{\mathrm{c}}$ " leads for both pressures to a smaller radius than the one when "interface at $Y_{\mathrm{s}}=Y_{\mathrm{c}}$ " is selected. This is a consequence of the fact that in a dense fluid thermal diffusion is more effective than mass diffusion (Lewis number larger than one). Then, the former increase of radius is due to the expansion of the fluid included between the "interface at $T_{\mathrm{s}}=T_{\mathrm{c}}$ " and the "interface at $Y_{\mathrm{s}}=Y_{\mathrm{c}}$ ". When transition occurs at the beginning of the droplet life (i.e. at high pressure), the vaporization lifetime, based on the mass diffusion process summarized with equation (19), is increased, while the thermal diffusion process is not affected. As a result of this analysis, we have suggested a reason for the qualitatively different behaviours observed according to both definitions of the supercritical droplet radius, leading to a mixing time larger than the heating time.

However, because the initial droplet enhancement is less important when pressure increases, the above argument is not sufficient to completely explain our results. Why does the lifetime keep on decreasing (vs pressure) when the definition of the droplet surface is the $T_{\mathrm{c}}$ isotherm, while the lifetime continuously increases when the definition of the droplet surface is the $Y_{\mathrm{c}}$ contour level? To propose an answer for this issue, we consider now a cooperative additional effect suggested by thermodynamics of high pressure mixtures. Coming back to Fig. 1, we note that, as the pressure increases, the critical conditions are such that $T_{\mathrm{c}}$ and $Y_{\mathrm{c}}$ decrease. Thus, the critical conditions are closer to the initial droplet temperature $(T_{0}=100 \mathrm{~K})$. Consequently, when the definition of the droplet surface is the $T_{\mathrm{c}}$ isotherm, the higher is the pressure, the easier is the "vaporization" considered as a heating process. Conversely, if the "interface at $Y_{\mathrm{c}}$ " is chosen, the droplet conditions $(Y=1)$ go away from the critical conditions when pressure increases. The latter effect delays the "vaporization" considered as a mixing process.

Both cooperative arguments provide us with a coherent frame making clear the behaviour we have called the "transcritical minimum".

## 5. CONCLUSIONS

The topic of this numerical study is the vaporization of a liquid $\mathrm{O}_{2}$ droplet in presence of an ambient, quiescent $\mathrm{H}_{2}$ gas at high temperature and high pressure. The complete analysis of the problem (transport-diffusion in both phases) has needed the resolution of the time-dependent conservation equations (mass, species, energy). Although our model tends to faithfully represent physical properties of the $\mathrm{O}_{2}-\mathrm{H}_{2}$ mixture at high pressure, it contains an important amount of inherent weaknesses. Nevertheless, a sensitivity analysis has shown that the qualitative aspects of our results present a sufficient degree of robustness.

For the subcritical regime, modifications induced by high pressure study show that the classical Spalding-Godsave estimate furnishes a droplet lifetime twice as large as our results. We show that the vaporization process can remain subcritical although the chamber pressure is much larger than the $\mathrm{O}_{2}$ critical pressure, as indicated on Fig. 6. As we approach the critical conditions, weakly singular behaviour of the regression rate can appear. However the present study just mentions this phenomenon because its appearance depends on the selected model of physical properties. As for the supercritical vaporization, the concept of droplet is preserved because a strong density gradient exists. This is due to the extreme sensitivity of thermal expansion coefficient in the vicinity of the critical conditions. Therefore, in this zone, rapid gas expansion produces Stefan flow that tends to isolate the cold "puff".

According to the "mixing" definition of supercritical droplet surface (we set $Y_{\mathrm{s}}=Y_{\mathrm{c}}$ ), the droplet lifetime presents a minimum for the pressure values given by the curve on Fig. 6. We have called this property as "transcritical minimum". At high temperature, the pressure value is close to the critical pressure of the droplet component (here $\mathrm{O}_{2}$ ). This result is in qualitative agreement with experimental results on combustion of hydrocarbon droplets $[1,2$, $21,22]$. However, if the "heating" definition of the supercritical droplet is chosen, the transcritical minimum disappears and the lifetime is a decreasing function of pressure.

The present study also gives some credit to the classical "quasi-steady" assumption as long as the pressure is far from the transcritical value. In Section 4 we have proposed a dimensional analysis using this assumption. It leads to the " $D^{2}$ law" at low and high pressure as it has been observed in our numerical results. Furthermore it provides us with high pressure estimates of droplet lifetime, equation (19), that explain the following results: at high pressure the droplet lifetime is independent on pressure and depends on temperature of chamber as:

$$
\tau_{\text {life }} \sim\left(T_{\infty}\right)^{-3 / 4}.
$$

Lastly, we propose a physical interpretation of the "transcritical minimum". At moderate pressure, it is well established $[31,33]$ that the droplet lifetime is a decreasing function of pressure. For explaining the increase at higher pressures, we put forward two cooperative arguments. The first one is of thermodynamic origin [Fig. 1]: when pressure increases, the thermal state of the liquid contained in the droplet becomes nearer to the thermal state required for vaporization. However, if we now consider the state in term of composition, the liquid goes away from the composition necessary to vaporize. The second one is related to the fact that in dense gas mass diffusivity is lower than heat diffusivity. This allows the fluid located between $T=T_{\mathrm{c}}$ and $Y=Y_{\mathrm{c}}$ to thermally expand. Consequently, when the "mixing" definition of the droplet is selected, a larger droplet radius is measured. In the supercritical regime, the rate of mixing thus diminishes when pressure increases, because mass diffusion starts with a larger "initial" radius.

Acknowledgements-The authors are grateful to Professor Amable Liñan for fruitful discussions. This work has received support from PRC:CNES/SEP/CNRS "Combustion dans les moteurs-fusées" under contract no. 900028-C.

## REFERENCES

1. J. Sato, M. Tsue, M. Niwa and M. Kono, Microgravity droplet combustion in high pressures near critical pressures on fuels, in AIP Conference Proceeding, no 197, Am. Inst. Physics, p. 387 (1989).
2. J. Sato, M. Tsue, M. Niwa and M. Kono, Effect of natural convection on high-pressure droplet combustion, Combust. Flame 82, 142 (1990).
3. E. W. Curtis and P. V. Farrel, A numerical study of high-pressure droplet vaporization, Combust. Flame 90, 85-102 (1992).
4. J. Daou, P. Haldenwang, C. Nicoli, Supercritical burn-

ing of liquid (LOX) droplet with detailed chemistry,
Combust. Flame 101, 153-169 (1995).

5. J. P. Delplanque and W. A. Sirignano, Numerical study
of the transient vaporization of an oxygen droplet at
sub- and super-critical conditions, Int. J. Heat Mass
Transfer 36(2), 303-314 (1993).

6. D. B. Spalding, Theory of particle combustion at high
pressures, ARS J. 29, 828-835 (1959).

7. D. E. Rosner, On liquid droplet combustion at high
pressures, AIAA JI 5(1), 163-166 (1967).

8. C. Sanchez-Tarifa, A. Crespo and E. Fraga, A theor-
etical model for the combustion of droplets in super-
critical conditions and gas pockets, Astron. Acta 17, 685-
692 (1972).

9. R. S. Lazar and G. M. Faeth, Bipropellant droplet com-
bustion in the vicinity of the critical point, Proceedings
of the 13th International Symposium on Combustion,
Combustion Institute, 801-811 (1971).

10. D. E. Rosner and W. S. Chang, Transient evaporation
and combustion of a fuel droplet near its critical tem-
perature, Combust. Sci. Technol. 7, 145-158 (1973).

11. C. K. Law, Recent advances in droplet vaporization
and combustion, Prog. Energy Combust. Sci. 8, 171-201
(1982).

12. W. A. Sirignano, Fuel droplet vaporization and spray
combustion theory, Prog. Energy Combust. Sci. 9, 291-
322 (1983).

13. J. A. Manrique and G. L. Borman, Calculation of steady
state droplet vaporization at high ambient pressures, Int.
J. Heat Mass Transfer 12, 1081-1095 (1969).

14. E. W. Curtis, J. P. Hartfield and P. V. Farrel,
Microgravity vaporization of droplets under super-
critical conditions, Proceedings of the 36th Congress of
International Astronautical Federation, IAF Paper 87
American Institute of Physics, 373-386 (1989).

15. D. Scherrer, Combustion supercritique d'une goutte
d'oxygène liquide, Rapport ONERA (Paris), 34/6112
(1986).

16. K. C. Hsieh, J. S. Shuen and V. Yang, Droplet vapo-
rization in high-pressure environments I: Near Critical
conditions, Combust. Sci. Technol. 76, 111-132 (1991).

17. P. V. Farrel and B. D. Peters, Droplet vaporization in
supercritical pressure environment, Acta Astronautica
13, 673-680 (1986).

18. R. J. Lichford and S. M. Jeng, Proceedings of the 26th
Joint Propulsion Conference, AIAA, Paper 90-2191
(1990).

19. V. Yang, N. N. Lin and J. S. Shuen, Vaporization of
liquid oxygen (LOX) droplets in supercritical conditions.
30th Aerospace Sciences Meeting, AIAA Paper 92-0103
(1992).

20. V. Yang, N. N. Lin and J. S. Shuen, Vaporization of
liquid oxygen (LOX) droplets in supercritical hydrogen
environments, Combust Sci. Technol. 97, 247-270 (1994).

21. G. M. Faeth, D. P. Dominicis, J. F. Tulpinski and
D. R. Olson, Supercritical bipropellant droplet combus-
tion, Proceedings of the 12th Symposium International
Combustion, The Combustion Institute, 9-18 (1969).

22. C. Chauveau and I. Gökalp, High pressure droplet burn-
ing experiments in reduced gravity, Paper presented at
the third Int. Microgravity Combustion Workshop,
NASA Lewis, Cleveland, April (1995).

23. R. C. Reid, J. M. Prausnitz and B. E. Poling, The Proper-
ties of Gases and Liquids. McGraw-Hill, New York
(1987).

24. C. Nicoli, P. Haldenwang and J. Daou, Substitute mix-
tures for LOX droplet vaporization study, Combust. Sci.
Technol. (in press).

25. Gas Encyclopedia, L'Air Liquide Company/Elsevier,
Amsterdam (1976).

26. S. T. Walas, Phase Equilibria in Chemical Engineering.
Butterworth, Stoneham, MA (1985).

27. A. Umemura, Supercritical liquid fuel combustion, Pro-
ceedings of the 21st International Symposium on Combus-
tion, The Combustion Institute, 463-471 (1986).

28. A. Umemura, X. Y. Chang and T. Fujiwara, Super-
critical droplet evaporation, ICLASS-91, Gaithersburg,
MD, paper 4 (July 1991).

29. R. J. Kee, J. Warnartz, J. A. Miller, Sandia Report-
Sand 83-8209, March (1983).

30. J. Daou, Etude de la vaporisation-combustion des gout-
tes d'oxygène liquide (LOX) à haute pression Thèse de
l'Université de Provence, Marseille (unpublished)
(1994).

31. G. A. E. Godsave, Studies of the combustion on drops
in a fuel spray-The burning of single drops of fuel,
Proceedings of the 4th International Symposium on Com-
bustion. Williams and Wilkins, Baltimore, pp. 818-830
(1953).

32. A. Crespo and A. Linan, Unsteady effects in droplet
evaporation and combustion, Combust. Sci. Technol. 11,
9-18 (1975).

33. D. B. Spalding, The combustion of liquids fuels, Pro-
ceedings of the 4th International Symposium on Combus-
tion, Combustion Institute, Pittsburgh, 847-864 (1953).

34. J. S. Shuen and V. Yang, Combustion of liquid-fuel
droplets in supercritical conditions, Combust. Flame 89,
299-319 (1992).

35. P. Lafon, Modélisation et simulation numérique de l'év-
aporation et de la combustion de gouttes à haute pres-
sion, Thèse de l'Université d'Orleans (unpublished)
(1994).

36. H. Viviand, Formes conservatives des équations de la
dynamique des gaz, La Recherche Aérospatiale 1, 65-68
(1974).

## APPENDIX

<table>
<caption>Table A1. Estimate methods for mixture thermodynamic transport properties</caption>
<thead>
<tr>
<th>Property of pure species</th>
<th>Method</th>
<th>Mixing rule</th>
</tr>
</thead>
<tbody>
<tr>
<td>Liquid specific heat</td>
<td>Experimental data fit [25]<br>Theoretical derivation from Soave EOS [26]</td>
<td>Mass fraction weighting</td>
</tr>
<tr>
<td>Gas specific heat</td>
<td>Experimental data fit [25]<br>Theoretical derivation from Soave EOS [26]</td>
<td>Mass fraction weighting</td>
</tr>
<tr>
<td>Liquid viscosity</td>
<td>Experimental data fit [25]</td>
<td rowspan="3">Mathur et al. [29]</td>
</tr>
<tr>
<td>Liquid thermal conductivity</td>
<td>Experimental data fit [25]</td>
</tr>
<tr>
<td>Gas thermal conductivity</td>
<td>Experimental data fit [25]</td>
</tr>
<tr>
<td>Liquid mass diffusivity</td>
<td>Wilke Chang [23]</td>
<td></td>
</tr>
<tr>
<td>Gas mass diffusivity</td>
<td>Wilke and Lee [23]</td>
<td></td>
</tr>
</tbody>
</table>