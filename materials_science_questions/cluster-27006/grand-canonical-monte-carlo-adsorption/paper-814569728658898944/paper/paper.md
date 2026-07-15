Accepted Manuscript

pyIAST: Ideal adsorbed solution theory (IAST) Python package

Cory M. Simon, Berend Smit, Maciej Haranczyk

![](./images/814569728658898944_1.jpg)

PII:
S0010-4655(15)00440-3
DOI:
http://dx.doi.org/10.1016/j.cpc.2015.11.016
Reference:
COMPHY 5819

To appear in: Computer Physics Communications

Received date: 10 August 2015
Revised date: 18 November 2015
Accepted date: 28 November 2015

Please cite this article as: C.M. Simon, B. Smit, M. Haranczyk, pyIAST: Ideal adsorbed solution theory (IAST) Python package, Computer Physics Communications (2015),
http://dx.doi.org/10.1016/j.cpc.2015.11.016

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# pyIAST: Ideal Adsorbed Solution Theory (IAST)
## Python Package

Cory M. Simon

UC Berkeley, Department of Chemical and Biomolecular Engineering, Berkeley, CA 94720-1462, USA
Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720-8139, USA

Berend Smit

Institut des Sciences et Ingenierie Chimiques, Ecole Polytechnique Federale de Lausanne (EPFL), Rue de l'Industrie 17, CH-1951 Sion, Switzerland
UC Berkeley, Department of Chemical and Biomolecular Engineering, Berkeley, CA 94720-1462, USA

Maciej Haranczyk*

Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720-8139, USA

* corresponding author. Email: mharanczyk@lbl.gov, fax: 510-486-5812.

---

### Abstract
Ideal adsorbed solution theory (IAST) is a widely-used thermodynamic framework to readily predict mixed-gas adsorption isotherms from a set of pure-component adsorption isotherms. We present an open-source, user-friendly Python package, pyIAST, to perform IAST calculations for an arbitrary number of components. pyIAST supports several common analytical models to characterize the pure-component isotherms from experimental or simulated data. Alternatively, pyIAST can use numerical quadrature to compute the spreading pressure for IAST calculations by interpolating the pure-component isotherm data. pyIAST can also perform reverse IAST calculations, where one seeks the required gas phase composition to yield a desired adsorbed phase composition.

Source code: https://github.com/CorySimon/pyIAST

Preprint submitted to Computer Physics Communications
November 17, 2015

Documentation: http://pyiast.readthedocs.org/en/latest/

Keywords:
Ideal adsorbed solution theory, IAST, mixed-gas adsorption

---

## PROGRAM SUMMARY
**Program Title:** pyIAST
**Programming language:** Python
**Operating system:** Linux, Mac, Windows
**Keywords:** Ideal adsorbed solution theory, IAST
**Classification:** 23 Statistical Physics and Thermodynamics
**External routines/libraries:** Pandas, Numpy, Scipy
**Nature of problem:** Using ideal adsorbed solution theory (IAST) to predict mixed-gas adsorption isotherms from pure-component adsorption isotherm data
**Solution method:** Characterize the pure-component adsorption isotherm from experimental or simulated data by fitting a model or using linear interpolation; solve the nonlinear system of equations of IAST
**Licence:** MIT
**Running time:** Less than a second.

## 1. Introduction
Adsorption is a ubiquitous process in the chemical sciences. For example, porous materials can be used to separate and therefore purify gases by selectively adsorbing one component over another [1], such as capturing carbon dioxide from flue gas [2], separating gaseous hydrocarbons in the petroleum industry [3], and capturing radioactive noble gases from used nuclear fuel reprocessing off-gas [4]. Porous materials can be used as gas sensors to monitor industrial processes and the environment and detect chemical threats [5]. The high surface areas and uniform and tunable pore topology of some crystalline porous materials make them useful as heterogeneous catalysts [6]. Further, porous materials can be used to densify and store gases [7], for example storing natural gas [8] or hydrogen [9, 10] onboard passenger vehicles.

For each of these myriad of applications, adsorption occurs in the presence of a *mixture* of gases [11]. Even for (pure) gas storage applications, the effect of impurities must typically be considered (i.e. a mixture) [8, 10, 12].

Pure-component adsorption isotherms are routinely measured with high accuracy using commercial instruments [13]. On the other hand, accurate measurements of adsorption isotherms in the presence of a mixture of gases are complicated and time-consuming [11, 14] and require custom-built in- struments [13]. To exacerbate this problem, modeling pressure and tem- perature swing adsorption processes requires mixed-gas adsorption data at many different gas compositions [15]; the required number of experiments to characterize composition space quickly becomes intractable as the number of components increases.

Ideal adsorbed solution theory (IAST), developed by Myers and Prausnitz [16] in 1965, is a widely used [17] thermodynamic framework for readily pre- dicting multi-component adsorption isotherms from only the pure-component adsorption isotherms at the same temperature. IAST rests upon the assump- tion that the adsorbed species form an ideal mixture, which is a reasonable approximation in many systems [16, 18–26]. In these applicable cases, IAST is a powerful tool that can reduce the need for laborious mixed-gas adsorp- tion measurements. Further, for cases where one is interested in several different mixture conditions, taking an array of laborious multi-component adsorption isotherm measurements may be impractical. Even for molecular simulations, simulating pure-component adsorption isotherms and applying IAST can be faster than performing multi-component grand-canonical Monte Carlo simulations [27] depending on the number of conditions of interest.

In this work, we release a Python package, pyIAST, under an MIT license to perform IAST calculations to predict mixed-gas adsorption from pure- component adsorption isotherms. The IAST framework does not enforce any specific adsorption model for the pure-component species. In practice, we have experimental or simulated data to characterize the pure-component adsorption isotherms. pyIAST can fit standard analytical isotherm mod- els (Langmuir, Quadratic, BET [28], approximated Temkin isotherm [29], Henry’s law) to this data to characterize the pure-component isotherms. Ad- ditionally, pyIAST can interpolate the isotherm data for IAST calculations, circumventing the burden of finding an appropriate analytical model and scrutinizing the quality of its fit to the data [30, 31]. pyIAST can handle an arbitrary number of components in the mixture. In addition, pyIAST per- forms reverse IAST calculations, where one calculates the required gas phase composition to yield a desired adsorbed phase composition. This feature is useful in catalysis, where one seeks to control the adsorbed phase composition to yield the appropriate stoichiometry in the adsorbed phase [32].

We first review the governing equations of IAST by deriving them from thermodynamics. We then discuss the two approaches to characterize the pure-component adsorption isotherms from data for input to pyIAST. To showcase our pyIAST package, we apply IAST to a gaseous mixture of methane and ethane in equilibrium with an adsorbed phase in a nanoporous material. This case study also serves as a verification of our code by com- paring the IAST result to binary grand-canonical Monte Carlo simulations of methane/ethane adsorption. We further verify pyIAST by comparing to the competitive Langmuir isotherm, which is an analytical solution to IAST when the pure-component isotherms follow Langmuir models with the same saturation loading. Finally, showcase pyIAST in predicting a tertiary mixture adsorption isotherm from pure $CO_2$, $N_2$, and $H_2O$ isotherms and compare to a rare experimentally measured mixed-gas adsorption isotherm by Mason et al. [13].

## 2. Ideal Adsorbed Solution Theory (IAST)
Below, we briefly review IAST. This also allows us to define our notation and introduce the governing equations that are solved by pyIAST.

Consider a gaseous mixture of $N$ chemical species at a pressure $P_T$ in equilibrium with an adsorbed phase on a surface. Let $y_i$ and $x_i$ be the mole fractions in the gas phase and adsorbed phase, respectively, for species $i=1,2,...,N$. We assume that we have experimental or simulated data characterizing the pure-component adsorption isotherms, $n_i^\circ(P)$, the moles of gas adsorbed on the surface when in equilibrium with a gas phase of pure species $i$ as a function of its pressure $P$. In ideal adsorbed solution theory, the goal is to use $n_i^\circ(P)$ for $i=1,2,...,N$ to predict the moles of gas of each species adsorbed on the surface when in equilibrium with the multicomponent gaseous mixture, $n_i=n_i(P_T,\{y_j\})$. IAST assumes throughout that the temperature $T$ is fixed and that the pure-component isotherms are measured at the same temperature as the mixed-gas of interest. In Sec 3, we will address how to translate pure-component isotherm data into a representative function $n_i^\circ(P)$ for IAST calculations.

For an isothermal physical adsorption process, we assume (1) the change in each thermodynamic property of the adsorbent when gas molecules adsorb is negligible compared to the change for the adsorbate, (2) each adsorbed species has access to the same area of the adsorbent surface, and (3) a Gibbs dividing surface defines an adsorbed phase. [16]


The first law of thermodynamics in differential form for the Gibbs free energy $G=G(T,\pi,\{n_i\})$ of the adsorbed phase is:

$$
d G=-S d T+A d \pi+\sum_{i=1}^{N} \mu_{i} d n_{i},
\tag{1}
$$

where $A$ is the area of the surface and $\pi$ is the spreading pressure. The spread- ing pressure is the analogy of pressure in two dimensions; $\pi d A$ is therefore the work done on the surroundings in the conceptual process of increasing the area of the adsorbent surface [16]. To further extend this analogy, in a two-dimensional ideal gas, the equation of state is $\pi A=N k_{B} T$ (derived in Appendix A).

The ideal solution assumption is that the enthalpy and area change upon mixing of the two adsorbate species is zero. In this case, the Gibbs free energy of a multi-component adsorbed phase at spreading pressure $\pi$ is:

$$
G(T, \pi,\left\{n_{j}\right\})=\sum_{i=1}^{N} G_{i}(T, \pi, n_{i})-T \Delta S_{m i x},
\tag{2}
$$

where $G_{i}(T, \pi, n_{i})$ is the Gibbs free energy of component $i$ in its pure state at the same temperature and spreading pressure as the mixture; thus the Gibbs free energy change upon mixing is determined by the entropy change upon mixing $\Delta S_{m i x}=-R \sum_{i} n_{i} \log x_{i}$ [33], where $R$ is the universal gas constant. As the chemical potential of adsorbed species $i$, $\mu_{i}$, is related to the Gibbs free energy by $\mu_{i}=\left(\frac{\partial G}{\partial n_{i}}\right)_{T, \pi, n_{j \neq i}}$, it follows from eqn 2 that

$$
\mu_{i}(T, \pi,\left\{x_{j}\right\})=\mu_{i}^{\circ}(T, \pi)+R T \log x_{i}.
\tag{3}
$$

Here, $\mu_{i}^{\circ}(T, \pi)$ is the chemical potential of adsorbed pure species $i$ at the same temperature and spreading pressure as the mixture.

At thermodynamic equilibrium, the chemical potentials in the adsorbed and gaseous phase are equal; the gas phase thus can be thought to impose the chemical potential. The chemical potential of species $i$ in an ideal gas (denoted by superscript $g$) is:

$$
\mu_{i}^{g}(T, P, y_{i})=\mu_{i}^{g, 0}(T)+R T \log p_{i},
\tag{4}
$$

where $p_{i}=y_{i} P_{T}$ is the partial pressure of species $i$ in the gas phase and $\mu_{i}^{g, 0}(T)$ is the reference chemical potential (derivation in Appendix B). Equating

$\mu_i^g(T,P,y_i)$ from eqn 4 and $\mu_i(T,\pi,\{x_i\})$ for the adsorbed phase from eqn 3,
we obtain:

$$
p_i = x_i e^{\frac{\mu_i^\circ(T,\pi)-\mu_i^{g,0}(T)}{RT}}. \tag{5}
$$

Consider the limit $x_i \to 1$, a limit of pure species $i$. In this limit, $p_i$ becomes
the pressure in the gas phase required to yield a spreading pressure $\pi$ of pure
species $i$ in the adsorbed phase. Defining this particular pressure as $x_i \to 1$
to be $p_i^\circ = p_i^\circ(\pi,T)$, we see that the exponential term is equivalent to $p_i^\circ$.
With this, we arrive at the analogy of Raoult's law for an adsorbed phase in
equilibrium with a gaseous phase:

$$
p_i = x_i p_i^\circ(\pi,T) \text{ for } i=1,2,...,N. \tag{6}
$$

By definition of $p_i^\circ$, it follows that the pure-component spreading pressures
$\pi_i$ at pressure $p_i^\circ$ are all equal to the spreading pressure of the mixture $\pi$:

$$
\pi = \pi_1(p_1^0) = \pi_2(p_2^0) = \cdots = \pi_N(p_N^0). \tag{7}
$$

Given expressions for the spreading pressure of a pure-component ad-
sorbed phase, $\pi_i(p_i^\circ)$, eqns 6 and 7 form $N+N-1$ equations for $2N$ un-
knowns, $\{p_i^\circ\}$ and $\{x_i\}$. The knowns here are $\{y_i\}$ and $P_T$, the mole fractions
in and the total pressure of the gas phase, respectively. These equations can
then be solved for $\{p_i^\circ\}$ and $\{x_i\}$ with the additional constraint $\sum_i x_i=1$.

We here show that we can indirectly calculate the spreading pressure
$\pi_i(p_i^\circ)$ from the pure-component adsorption isotherm $n_i^\circ(P)$. By Euler's the-
orem for homogeneous functions, the Gibbs free energy for a pure-component
system of species $i$ is $G = \mu_i^\circ n_i^\circ$. Taking the differential of $G = \mu_i^\circ n_i^\circ$ and
subtracting eqn 1 for a pure-component system, we obtain the Gibbs-Duhem
equation for a pure-component adsorbed phase at constant temperature:

$$
-Ad\pi_i + n_i^\circ d\mu_i^\circ = 0 \text{ at constant } T. \tag{8}
$$

Since the gas phase imposes the chemical potential, $\mu_i^\circ = \mu_i^g(T,p_i^\circ,1)$ by eqn 4,
and $d\mu_i^\circ = RT d\log p_i^\circ$. Thus, we can rewrite the Gibbs-Duhem relation as:

$$
Ad\pi_i = RT\frac{n_i(p_i^\circ)}{p_i^\circ} dp_i^\circ. \tag{9}
$$

Integrating eqn 9, we obtain an expression for the spreading pressure of
adsorbed pure-component $i$ in equilibrium with a pure-component $i$ gas phase
at pressure $p_i^\circ$:

$$
\pi_i(p_i^\circ) = \frac{RT}{A} \int_0^{p_i^\circ} \frac{n_i^\circ(P)}{P} dP. \tag{10}
$$

We used $\pi_i(0) = 0$ in the integration limit. Eqn 10 describes how we use the pure-component adsorption isotherms $n_i^\circ(P)$ to obtain the composition $\{x_i\}$ of the adsorbed phase through eqns 6 and 7.

We also desire the absolute gas adsorption $n_i(P, \{y_i\})$. Here, we derive an expression for the total moles of gas adsorbed on the surface, $n_T$. It follows that $n_i = x_i n_T$. The Gibbs-Duhem relation for the adsorbed mixture is:

$$
-A d \pi+\sum_{i=1}^{N} n_{i} d \mu_{i}=0 \text { at constant } T. \tag{11}
$$

Dividing by $n_T$,

$$
\frac{A}{n_{T}}=\sum_{i} x_{i}\left(\frac{\partial \mu_{i}}{\partial \pi}\right)_{T, x_{j}}. \tag{12}
$$

The derivative can be simplified using eqn 3 [34]:

$$
\left(\frac{\partial \mu_{i}}{\partial \pi}\right)_{T, x_{j}}=\left(\frac{\partial \mu_{i}^{\circ}}{\partial \pi}\right)_{T}=\frac{A}{n_{i}^{\circ}}, \tag{13}
$$

and the equality on the right follows from the Gibbs-Duhem equation of the pure-component system in eqn 8. Eqns 12 and 13 combined yield an expression to solve for the total moles of gas adsorbed $n_T$ from the pure-component adsorption isotherms $n_i^\circ(P)$, $\{p_i^\circ\}$, and $\{x_i\}$ obtained above:

$$
\frac{1}{n_{T}}=\sum_{i=1}^{N} \frac{x_{i}}{n_{i}^{\circ}\left(p_{i}^{\circ}\right)}. \tag{14}
$$

The relationship in eqn 14 is a two-dimensional analogy to Amagat's law of additive volumes for a three-dimensional system [34]. The expression $A/n_T$ is the area per adsorbed molecule in the mixture; $A/n_i^\circ(p_i^\circ)$ is the area per adsorbed molecule in the pure-component system at the same temperature and spreading pressure as the mixture. Eqn 14 thus expresses that the area per adsorbate in the mixture is the weighted average of the area allocated to each adsorbate in the pure-component systems at the same spreading pressure; this is consistent with the ideal solution assumption that there is no area change upon mixing [16].

This concludes the derivation of ideal adsorbed solution theory. Given the functions for the pure-component adsorption isotherms $\{n_i^\circ(P)\}$ and a specified bulk gas at pressure $P_T$ and composition $\{y_i\}$, we solve for $\{x_i\}$

and $\{p_i^\circ\}$ using the nonlinear system of equations in eqns 6 and 7. The pure-component adsorption isotherms allow us to calculate the spreading pressures via eqn 10. Finally, we can compute the total number of moles adsorbed using eqn 14. The computational strategy we use to solve the nonlinear system of equations closely follows that in Ref. [35] outlined for a binary mixture. Fig 1 shows this workflow of an IAST calculation in pyIAST.

Note that we can account for nonideality (i) in the gas phase by replacing the pressure $P$ in the above equations with the fugacity and (ii) in the adsorbed phase by replacing the adsorbed phase mole fractions $x_i$ by $x_i\gamma_i$, where $\gamma_i$ is the activity coefficient of species $i$ in the adsorbed mixture. [16]

## 3. Characterizing the pure-component adsorption isotherm $n_i^\circ(P)$

For IAST calculations, we need the pure-component adsorption isotherms $n_i^\circ(P)$ to compute the integral in eqn 10 to obtain the spreading pressure; in practice, we have a set of experimental or simulated data points to characterize $n_i^\circ(P)$. pyIAST can translate this pure-component isotherm data into a function $n_i^\circ(P)$ in two disparate ways: (1) fit an analytical model to the data and (2) linearly interpolate the data. For the first option, we solve the integral in eqn 10 analytically for the given model and evaluate it using the fitted model parameters. For the second option, we compute the integral in eqn 10 using numerical quadrature. In Sec 3.6, we discuss the advantages and disadvantages of each of the two approaches.

### 3.1. Analytical models

The first option is to fit the simulated or experimental pure-component adsorption isotherm data to an analytical model $n_i^\circ(P)$ using a least-squares loss function. From this analytical model and identified parameters, we can write an analytical formula for the spreading pressure in eqn 10. pyIAST can fit several common [35] analytical models to the data: Langmuir, quadratic, BET, and approximated Temkin adsorption isotherms and Henry's law. See Fig 2 for caricatures of these adsorption isotherm models. The list `pyiast.MODELS` lists all models implemented in pyIAST, which we review here. Note that pyIAST supports only thermodynamically consistent isotherm models [36, 37] that obey Henry's law at low coverage, i.e. models such that $\lim_{P \to 0} \frac{dn_i^\circ}{dP}$ is finite. For example, pyIAST does not support the empirical [38] Freundlich isotherm [39]. In each section title, we note the keyword for the respective model in pyIAST.

![](./images/814569728658898944_2.jpg)

Figure 1: Work flow of pyIAST. For this example, the goal is to predict an adsorption isotherm in a nanoporous material, IRMOF-1, immersed in a gaseous mixture of methane and ethane. First, one measures or simulates the pure methane and pure ethane adsorption isotherms. Then, pyIAST will translate the data into a function $n_{i}^{\circ}(P)$ for $i =\text{CH}_4$, $\text{C}_2\text{H}_6$ by fitting to an analytical model or interpolating the isotherm. For a given gas phase composition and pressure, pyIAST first solves eqns 6 and 7 for $\{x_i\}$ and $\{p_i^{\circ}\}$, and then solves for the total gas adsorption by eqn 14.

![](./images/814569728658898944_3.jpg)

![](./images/814569728658898944_4.jpg)

Figure 2: Caricatures of adsorption isotherm models implemented in pyIAST. (a) Lang- muir, (b) Dual-site Langmuir (c) Quadratic, (d) BET (e) Asymptotic approximation to the Temkin isotherm ($\theta < 0$ here for adsorbate-adsorbate attractions) (f) Henry's law. In each saturating isotherm, $M$ is marked on the $y$-axis. For (b), we plotted the Langmuir isotherm for sites of type 1 and 2 separately. For (e), we plotted the Langmuir isotherm for comparison, which corresponds to $\theta = 0$, as the solid, black curve.

### 3.1.1. Langmuir model, `model="Langmuir"`

The Langmuir adsorption isotherm assumes a single layer of molecules can adsorb onto $M$ distinct, identical, independent adsorption sites; adsorbed molecules do not interact except through volume exclusion. The Langmuir model has an addition parameter $K$ (units: pressure$^{-1}$) that describes the affinity of the adsorbate with the adsorbent (see Fig 2(a)):

$$
n_{i}^{\circ}(P)=M \frac{K P}{1+K P}. \tag{15}
$$

As half of the adsorption sites are occupied at $P=1/K$, the Langmuir constant $K$ is inversely related to the pressure at which the isotherm saturates. At low pressures, the Langmuir model is approximated by Henry's law $n_{i}^{\circ}(P) \sim M K P$.

The spreading pressure for a Langmuir adsorption isotherm via eqn 10 is

$$
\frac{A}{R T} \pi_{i}(P)=M \log (1+K P). \tag{16}
$$

Statistical mechanical derivations of the Langmuir adsorption isotherm can be found in Refs. [29, 40].

### 3.2. Dual-site Langmuir model, `model="DSLangmuir"`

The dual-site Langmuir model is a first attempt to model an adsorbent surface with energetic heterogeneity. In this scenario, the adsorbent surface has two different types of adsorption sites. As in the Langmuir model, we neglect adsorbate-adsorbate interactions and take each adsorption site to be independent, implying that the dual-site Langmuir adsorption isotherm is the sum of the Langmuir isotherm models for the two types of sites:

$$
N(P)=M_{1} \frac{K_{1} P}{1+K_{1} P}+M_{2} \frac{K_{2} P}{1+K_{2} P}, \tag{17}
$$

where $M_{i}$ is the number of adsorption adsorption sites of type $i$, which have Langmuir constant $K_{i}$, for $i \in \{1,2\}$.

The spreading pressure for a dual-site Langmuir adsorption isotherm via eqn 10 is

$$
\frac{A}{R T} \pi_{i}(P)=M_{1} \log \left(1+K_{1} P\right)+M_{2} \log \left(1+K_{2} P\right). \tag{18}
$$


#### 3.2.1. Quadratic model, `model="Quadratic"`

The quadratic adsorption isotherm exhibits an inflection point; the load-
ing is convex at low pressures but changes concavity as it saturates, yielding
an S-shape. See Fig 2(c). The S-shape can be explained by adsorbate-
adsorbate attractive forces [41]; the initial convexity is due to a cooperative
effect [42] of adsorbate-adsorbate attractions aiding in the recruitment of
additional adsorbate molecules. The quadratic isotherm model is:

$$
n_{i}^{\circ}(P)=M \frac{\left(K_{A}+2 K_{B} P\right) P}{1+K_{A} P+K_{B} P^{2}},
\tag{19}
$$

where $2M$ is the saturation loading and $K_A$ (units: pressure$^{-1}$) and $K_B$
(units: pressure$^{-2}$) are constants. The spreading pressure for a quadratic
isotherm via eqn 10 is:

$$
\frac{A}{RT}\pi_i(P)=M\log(1+K_A P+K_B P^2).
\tag{20}
$$

A statistical mechanical derivation of the quadratic adsorption isotherm
can be found in [40]. Here, pairs of adsorbate molecules experience attractive
forces. The parameter $K_A$ can be interpreted as the Langmuir constant; the
strength of the adsorbate-adsorbate attractive forces is embedded in $K_B$.

#### 3.2.2. Brunauer-Emmett-Teller (BET) model, `model="BET"`

In the Brunauer-Emmett-Teller (BET) adsorption isotherm model [28],
we have $M$ independent, identical adsorption sites on the surface – as in the
Langmuir model – but now adsorbate molecules are allowed to stack to form
an indefinite number of layers. The multi-layer BET adsorption isotherm
model is:

$$
n_{i}^{\circ}(P)=M \frac{K_{A} P}{\left(1-K_{B} P\right)\left(1-K_{B} P+K_{A} P\right)},
\tag{21}
$$

where $K_A$ is the Langmuir constant for the first layer of adsorbate molecules
in direct contact with the surface, and $K_B$ is the constant for the second and
higher layers of adsorbate molecules.

The spreading pressure for a BET isotherm via eqn 10 is:

$$
\frac{A}{RT}\pi_i(P)=M\log\left(\frac{1-K_B P+K_A P}{1-K_B P}\right).
\tag{22}
$$

A statistical mechanical derivation of the BET adsorption isotherm can
be found in Ref. [40].


### 3.3. Asymptotic Approximation to the Temkin model, `model="TemkinApprox"`

The Temkin adsorption isotherm [43], like the Langmuir model, considers a surface with $M$ identical adsorption sites, but takes into account adsorbate-adsorbate interactions by assuming that the heat of adsorption is a linear function of the coverage. We independently derived the Temkin isotherm in Ref. [29] using a mean-field argument and used an asymptotic approximation to obtain an explicit equation for the loading:

$$
n_{i}^{\circ}(P)=M\left(\frac{K P}{1+K P}+\theta\left(\frac{K P}{1+K P}\right)^{2}\left(\frac{K P}{1+K P}-1\right)\right). \tag{23}
$$

Here, $M$ and $K$ have the same physical meaning as in the Langmuir model. The additional parameter $\theta$ describes the strength of the adsorbate-adsorbate interactions ($\theta<0$ for attractions). Fig 2(e) shows how eqn 23 is a perturbation on the Langmuir model for $\theta<0$; the effect of adsorbate-adsorbate interactions are most significant at intermediate coverages.

The spreading pressure of the isotherm model in eqn 23 via eqn 10 is:

$$
\frac{A}{R T} \pi_{i}(P)=M\left(\log (1+K P)+\theta \frac{2 K P+1}{2(K P+1)^{2}}\right). \tag{24}
$$

### 3.4. Henry's law, `model="Henry"`

Henry's law is:
$$
n_{i}^{\circ}(P)=K_{H} P, \tag{25}
$$
where $K_H$ is the Henry coefficient (units: loading/pressure). Henry's law describes adsorption only in the low coverage regime because $n_{i}^{\circ}(P)$ unrealistically increases indefinitely with $P$; thus caution must be used when extrapolating experimental data with Henry's law. The spreading pressure for Henry's law is $\frac{A}{R T} \pi_{i}(P)=K_{H} P$.

#### 3.4.1. Remark

For some combinations of analytical models for pure-component adsorption isotherms, IAST can be used to obtain an analytical expression for the mixed-gas adsorption isotherm. For example, if all single-component adsorption isotherms obey the Langmuir model in eqn 15 with Langmuir constant $K_i$ and exhibit the same saturation loading $M$ - often a strong assumption - IAST recovers the competitive Langmuir isotherm [44]:

$$
n_{i}\left(P,\left\{y_{j}\right\}\right)=M \frac{K_{i} p_{i}}{1+\sum_{j} K_{j} p_{j}}, \tag{26}
$$

where $p_i = y_i P_T$ is the partial pressure of species $i$ in a gas mixture with total pressure $P_T$. An analytical model for the multi-component adsorp- tion isotherm is more computationally efficient because it circumvents the need to solve the nonlinear system of equations in eqns 6 and 7. Other derivations for mixture adsorption isotherms can be found in the literature for when the pure-component adsorption isotherm models follow: Langmuir and Freundlich isotherms [44], quadratic isotherms [45], BET and Langmuir isotherms [46], and quadratic and BET and quadratic and Langmuir for the special case when saturation loadings are equal [35].

### 3.5. Numerical quadrature
An alternative to assuming the pure-component adsorption isotherm fol- lows a given functional form is to linearly interpolate the pure-component adsorption isotherm data to approximate $n_i^{\circ}(P)$ and use numerical quadra ture [47] to evaluate the integral in eqn 10 to obtain the spreading pressure for IAST calculations.

Consider that we have $L$ data points of the pressure $P$ and uptake $n_i^{\circ}$ that characterize the adsorption isotherm, $\{(P_j, n_i^{\circ}(P_j))\}$, $j=1,2,...,L$, where $P_1 < P_2 < \cdots < P_{L-1} < P_L$. Fig 3 illustrates the numerical quadrature method to compute $\frac{A}{RT} \pi_i(p_i^{\circ})$ from the integral in eqn 10, where $p_i^{\circ} \leq P_L$; the circular points in Fig 3 represent $\{(P_j, n_i^{\circ}(P_j)/P_j)\}$. For interested readers, we outline the details of the numerical quadrature below.

We tackle the integral by splitting the integration into three parts:
$$
\frac{A}{R T} \pi_{i}\left(p_{i}^{\circ}\right)=\int_{0}^{P_{1}} \frac{n_{i}^{\circ}(P)}{P} d P+\sum_{j=1}^{k-1} \int_{P_{j}}^{P_{j+1}} \frac{n_{i}^{\circ}(P)}{P} d P+\int_{P_{k}}^{p_{i}^{\circ}} \frac{n_{i}^{\circ}(P)}{P} d P, \quad(27)
$$
where index $k$ is defined such that $P_{k} \leq p_{i}^{\circ}<P_{k+1}$.

The integral $\int_{0}^{P_{1}}$ requires extrapolation of the isotherm for $P<P_{1}$. We assume that Henry's law $n_{i}^{\circ}(P)=K_{H} P$ is obeyed in the region $P \in[0, P_{1}]$, with the Henry coefficient $K_{H}$ estimated from the first data point, $K_{H}=$ $n_i^{\circ}(P_1)/P_1$. This gives us the limiting behavior:
$$
\lim _{P \rightarrow 0} \frac{n_{i}^{\circ}(P)}{P}=K_{H}, \quad(28)
$$
which is added to Fig 3 as the star. Thus,
$$
\int_{0}^{P_{1}} \frac{n_{i}^{\circ}(P)}{P} d P \approx \int_{0}^{P_{1}} K_{H} d P=n_{i}^{\circ}\left(P_{1}\right), \quad(29)
$$

equal to the area of the left-most green-shaded rectangle in Fig 3.

The integrals $\int_{P_{j}}^{P_{j+1}}$ are computed by approximating $n_{i}^{\circ}(P)$ by linearly interpolating the data points $(P_{j}, n_{i}^{\circ}(P_{j}))$ and $(P_{j+1}, n_{i}^{\circ}(P_{j+1}))$. That is, $n_{i}^{\circ}(P) \approx m_{j} P+b_{j}$ for $P \in[P_{j}, P_{j+1}]$, where $m_{j}$ is the slope and $b_{j}$ is the intercept of the line passing through the points $(P_{j}, n_{i}^{\circ}(P_{j}))$ and $(P_{j+1}, n_{i}^{\circ}(P_{j+1}))$.
Then,
$$
\int_{P_{j}}^{P_{j+1}} \frac{n_{i}^{\circ}(P)}{P} \approx m_{j}\left(P_{j+1}-P_{j}\right)+b_{j} \log \left(P_{j+1} / P_{j}\right),\qquad(30)
$$
represented by the areas of the next three green-shaded segments in Fig 3.

The last portion of the integral, $\int_{P_{k}}^{p_{i}^{\circ}}$, is computed analogously to eqn 30 , except now $m_{k}$ and $b_{k}$ are the slope and intercept of the line passing through the points $(P_{k}, n_{i}^{\circ}(P_{k}))$ and $(p_{i}^{\circ}, \hat{n_{i}^{\circ}}(p_{i}^{\circ}))$, where $\hat{n_{i}^{\circ}}(p_{i}^{\circ})$ is the linearly interpolated value of $n_{i}^{\circ}$ at $p_{i}^{\circ}$. This portion of the integral is the right-most green-shaded segment in Fig 3.

Depending on the composition and pressure of the gas we are investigating with IAST, we may need knowledge of $\pi_{i}(p_{i}^{\circ})$ for $p_{i}^{\circ}>P_{L}$, and thus $n_{i}^{\circ}(p_{i}^{\circ})$ for $p_{i}^{\circ}>P_{L}$. In this case, the linear interpolation method is inapplicable due to a lack of data for $P>P_{L}$, unless we assume some behavior for $n_{i}^{\circ}(P)$ for $P>P_{L}$. We will see that an option in pyIAST is to approximate $n_{i}^{\circ}(P)$ as a constant for $p_{i}^{\circ}>P_{L}$, which is reasonable if the isotherm data exhibits a plateau at the last few pressure points. Conveniently, the spreading pressure is most sensitive to the low-coverage regime of the pure-component adsorption isotherm [16].

### 3.6. Fit an analytical model or use numerical quadrature?
Here, we address the question of whether to fit an analytical model to the data or interpolate the data to represent the pure-component adsorption isotherm $n_{i}^{\circ}(P)$. The central issues that can lead to inaccuracy for IAST calculations are (1) imprecisely representing the pure-component adsorption isotherm data and (2) computing the pure-component spreading pressure beyond the range of the data available (extrapolating) [31]. We first discuss issue (1).

Consider fitting an analytical model to the pure-component adsorption isotherm data. Of course, if the user chooses a functional form that does not fit the data, the IAST predictions can be inaccurate. For example, Van Heest et al. [30] show that IAST predictions for a xenon/krypton adsorption

![](./images/814569728658898944_5.jpg)

Figure 3: Numerical quadrature to compute the spreading pressure $\pi_{i}(p_{i}^{\circ})$. Using the data $\{(P_{j},n_{i}^{\circ}(P_{j}))\}$, $j=1,2,...,L$ that characterize the pure-component adsorption isotherm, the circular points in this visualization are the points $\{(P_{j},n_{i}^{\circ}(P_{j})/P_{j})\}$. We model the uptake before the first pressure point with Henry's law and estimate the Henry coefficient $K_{H}$ from the first data point, $K_{H}\approx n_{i}^{\circ}(P_{1})/P_{1}$. This gives us the limiting behavior of the integrand $\lim_{P	o 0}n_{i}^{\circ}(P)/P=K_{H}$, plotted as the star. The red, vertical line denotes $p_{i}^{\circ}$, which by definition of $k$ falls between $P_{k}$ and $P_{k+1}$. The blue curve between $P_{1}$ and $p_{i}^{\circ}$ is the function $n_{i}^{\circ}(P)/P$ approximated by linearly interpolating the data $\{(P_{j},n_{i}^{\circ}(P_{j}))\}$. Using numerical quadrature to compute eqn 10, $\frac{A}{RT}\pi_{i}(p_{i}^{\circ})$ is approximately the area shaded in green.

in metal-organic framework HKUST-1 lead to incorrect predictions when fit- ting a dual-site Langmuir model to the pure-component isotherm data, but IAST agrees very well with binary grand-canonical Monte Carlo simulations when using numerical quadrature. Ref. [30] calls for meticulousness when fitting analytical models to the pure-component isotherm data for IAST cal- culations: the user must test different functional forms to identify one of an appropriate shape and scrutinize the quality of its fit to the data. Nu- merical quadrature takes this burden off of the user since, by construction, linear interpolation will fit the data perfectly. Further, some isotherms ex- hibit complex shapes, making it difficult to find an appropriate analytical model.

An appropriately shaped analytical model can better-represent the isotherm than linear interpolation if the data is not highly resolved in pressure space. The numerical quadrature illustrated in Fig 3 assumes that $n_{i}^{\circ}(P)$ is linear

between data points; thus, if the grid of pressure points is coarse, this ap-
proximation can introduce errors due to inconsideration of the curvature of
$n_i^\circ(P)$ between data points. On the other hand, an appropriate analytical
model will capture the curvature between data points. In principle, one could
capture the curvature between points in numerical quadrature by using e.g.
cubic spline interpolation [47] for $n_i^\circ(P)$, but the high variance in fitting cu-
bic splines often leads to non-physical isotherm shapes, and consequently we
restrict pyIAST to linear interpolation for $n_i^\circ(P)$.

In the case that the data is noisy, analytical models may be favorable since
they can exhibit low variance in the presence of noisy measurements, whereas
linear interpolation will incorporate the noise into the IAST calculations (the
bias-variance trade-off [48]).

Depending on the pressure and composition of the mixture investigated
with IAST, one may need to compute $\pi_i(P)$ for a pressure $P$ outside the
range of the available data (issue 2). This can be an issue for both methods
of characterizing $n_i^\circ(P)$: fitting an analytical model and linear interpolation.

By definition of interpolation, pyIAST by default throws an exception
when $\pi_i(P)$ is needed for $P$ greater than the largest pressure for which data is
available. If the pure-component adsorption isotherm is measured/simulated
to a high pressure and exhibits a plateau, it may be reasonable to assume
that the loading is a constant value beyond the highest pressure in the data,
as implemented as an option in pyIAST to both use interpolation and ex-
trapolate the pure-component adsorption isotherm data when needed.

Fitting to an appropriate analytical model is a more natural way to ex-
trapolate the isotherm beyond the data, as e.g. the Langmuir, Quadratic,
and BET adsorption isotherms are derived from physical assumptions. How-
ever, if the data does not exhibit much curvature, the fitted parameters in
the analytical models exhibit high variance; that is, the optimal parameters
become highly sensitive to noise in the data. Intuitively, it is difficult to
estimate the saturation loading of an isotherm in the low-coverage regime
where the data does not exhibit much curvature.

Thus, emphatically, even when using analytical models, it may be nec-
essary to collect pure-component isotherm data at higher pressures in order
to proceed with IAST if data is needed beyond the largest pressure observed
in the available data. To induce caution in users extrapolating their data,
pyIAST prints a warning when the IAST result required extrapolation of the
pure-component adsorption isotherm data.

Finally, we remark that the convenience of using numerical quadrature


to compute the spreading pressure $\pi_i(P)$ comes with a greater computa-
tional cost than assuming an analytical model. For the analytical models,
we derived explicit expressions for $\pi_i(P)$ (e.g. eqn 16), whereas for numerical
quadrature we carry out the numerical quadrature procedure illustrated in
Fig 3. Thus, fitting to an analytical model may significantly reduce compu-
tation time in applications where IAST calculations are needed repeatedly,
such as in packed-bed a(b)dsorber modeling [49]. In the vast majority of
cases we see in the literature, the extra computational cost for numerical
quadrature is insignificant.

We note the flexibility of pyIAST to mix different types of adsorption
isotherm models for its IAST calculations (e.g., use Langmuir for one com-
ponent and interpolation for another).

## 4. IAST Package Case Study

As an illustration of how to use pyIAST, we consider a gaseous mix-
ture of methane and ethane at 298 K and 65 bar in equilibrium with an
adsorbed phase inside a nanoporous material. This mixture is relevant in
the application of porous materials to store natural gas onboard vehicles
[8]. Natural gas consists of mostly methane (> 95%), but it also contains
higher hydrocarbons, nitrogen, and carbon dioxide [8, 12]; the second largest
constituent of natural gas is typically ethane. We consider the adsorption
of methane/ethane in metal-organic framework IRMOF-1 [50], a nanoporous
material with one of the highest measured [51] methane deliverable capacities
to date [52]; see Fig 1 for a visualization of the IRMOF-1 crystal structure.
IAST is applicable as we abstract the walls of the pores in IRMOF-1 as a
ravelled-up surface to which gas molecules adsorb.

Using the grand-canonical Monte Carlo algorithm, we simulated pure-
component ethane and methane adsorption isotherms at 298 K to use for an
IAST calculation. See Fig 4. Our goal is to predict the methane and ethane
adsorption in IRMOF-1 at different gas phase mole fractions of ethane $y_{C_2H_6}$
in the methane/ethane mixture at 65 bar and 298 K. As both verification of
our code and validation of IAST for this mixture in IRMOF-1, we compare
the IAST calculations to binary-component grand-canonical Monte Carlo
simulations of methane/ethane adsorption at different $y_{C_2H_6}$. Our simulation
methods are detailed in Appendix C. The data and pyIAST code to reproduce
this case study are available in the /test folder of the Github repository.

![](./images/814569728658898944_6.jpg)

Figure 4: Simulated pure-component methane $(CH_{4})$ and ethane $(C_{2}H_{6})$ adsorption isotherms in IRMOF-1 at 298 K.

### 4.1. Constructing pure-component adsorption isotherm models

We load the pure-component adsorption isotherm data displayed in Fig 4, stored as two .csv files, into a Pandas DataFrame. A DataFrame is a data structure for conveniently storing and accessing tabular data.

```
import pandas as pd
df_ch4 = pd.read_csv("IRMOF-1_methane_isotherm_298K.csv")
df_ch3ch3 = pd.read_csv("IRMOF-1_ethane_isotherm_298K.csv")
```

Next, we use pyIAST to construct an adsorption isotherm object for each pure-component adsorption isotherm. We start with an attempt to fit a Langmuir adsorption isotherm model to characterize $n_{C_{2}H_{6}}^{\circ}(P)$. The `ModelIsotherm` class in pyIAST is used for all analytical models; we notify pyIAST which model to fit to the data by passing e.g. `model="Langmuir"` for a model in the list `pyiast._MODELS`. We construct a `ModelIsotherm` object by passing it the Pandas DataFrame containing the pure-component ethane isotherm, `df_ch3ch3`, and the names of the columns (keys) corresponding to the loading and pressure.


```python
import pyiast
ch3ch3_isotherm = pyiast.ModelIsotherm(df_ch3ch3,
                          loading_key="Loading(mmol/g)",
                          pressure_key="Pressure(bar)",
                          model="Langmuir")

# Print identified parameters
ch3ch3_isotherm.print_params()
# > Langmuir identified model parameters:
# >    K = 0.229837
# >    M = 21.932328
# >    RMSE =  0.862745372792

# get dictionary of parameters
ch3ch3_isotherm.params
# > {'K': 0.22983701506470389, 'M': 21.932328016544513}

# predicted loading at 10 bar using fitted model (mmol/g)
ch3ch3_isotherm.loading(10.0)
# > 15.28288389268168
```

In the construction of the `ModelIsotherm` object, a least-squares non-linear fitting routine finds the parameters of best fit. The above code and resulting output illustrates how to print the identified parameters and root mean square error (RMSE), access a dictionary containing the parameters of best fit, and predict loading using the fitted model from an instance of the `ModelIsotherm` class. We can visualize the fit of the Langmuir model to the adsorption isotherm data with the `plot_isotherm()` function:

```python
pyiast.plot_isotherm(ch3ch3_isotherm, xlogscale=True)
```

Fig 5 shows that the Langmuir model provides a poor fit to the pure-component ethane adsorption isotherm data and thus will lead to inaccurate IAST calculations. As a better approximation of $n_{C_2H_6}^\circ(P)$, we turn to the method of linearly interpolating the ethane adsorption isotherm data in Fig 4 since we have data on a sufficiently resolved grid of pressures.

![](./images/814569728658898944_7.jpg)

Figure 5: Characterizing $n_{C_{2}H_{6}}^\circ(P)$ from pure-component adsorption isotherm data (red points). Shown is the Langmuir model fit by `ModelIsotherm` (solid line) and the interpo- lation model fit by `InterpolatorIsotherm` (dashed line). Fits can be visualized by the function `plot_isotherm()`.

The `InterpolatorIsotherm` object linearly interpolates the pure-component adsorption isotherm data and uses numerical quadrature to compute the spreading pressure (see Sec 3.5). Similar to the `ModelIsotherm` class, we con- struct an instance of the `InterpolatorIsotherm` class by passing `df_ch3ch3` and the names of the pressure and loading columns. By default, the `InterpolatorIsotherm` will throw an exception when we attempt to extrapolate the pure-component adsorption isotherm data beyond the highest pressure available in Fig 4. As we have ethane adsorption data at high enough pressures to see saturation in the isotherm, a reasonable assumption is that the saturation loading is equal to the highest uptake in the data. We enforce this assumption by pass- ing a `fill_value` in the construction of the `InterpolatorIsotherm` object, setting it equal to the maximum loading of ethane observed in Fig 4.

```
ch3ch3_isotherm = pyiast.InterpolatorIsotherm(df_ch3ch3,
                      loading_key="Loading(mmol/g)",
                      pressure_key="Pressure(bar)",
                      fill_value=df_ch3ch3["Loading(mmol/g)"].max())
```

The fit of this `ch3ch3_isotherm` is shown in Fig 5.

Analogously, we also construct an `InterpolatorIsotherm` object for methane, `ch4_isotherm`. These adsorption isotherm objects will be passed

as inputs to the iast() function to perform IAST calculations.

### 4.2. Performing IAST calculations
Given the characterization of the pure-component adsorption isotherms $n_{C_{2}H_{6}}^{\circ}(P)$ and $n_{CH_{4}}^{\circ}(P)$ using InterpolatorIsotherm objects, we can now predict binary methane/ethane adsorption isotherms in IRMOF-1 using IAST.

As an example, consider predicting the moles of adsorbed methane and ethane, $n_{CH_{4}}$ and $n_{C_{2}H_{6}}$, in IRMOF-1 in equilibrium with a 95/5 mol % methane/ethane mixture at 298 K and 65 bar. Our function to perform IAST calculations, iast(), takes a list or array of partial pressures of the gases and a list of the corresponding instances of ModelIsotherm's and/or InterpolatorIsotherms's. The verboseflag prints details of the internal computations, such as $p_{i}^{\circ}$ and the spreading pressure of the mixture.

```
# partial pressures of ethane and methane in gas phase (bar)
partial_pressures = [0.05 * 65.0, 0.95 * 65.0]
component_loadings = pyiast.iast(partial_pressures,
                  [ch3ch3_isotherm, ch4_isotherm],
                  verboseflag=False)
# > array([  4.4612935 ,  13.86364776])
```

The iast() function returns an array component_loadings of component uptakes in the adsorbed phase, $n_{C_{2}H_{6}}$ and $n_{CH_{4}}$, computed from IAST. Here, $n_{T}=n_{CH_{4}}+n_{C_{2}H_{6}}$ and $x_{CH_{4},C_{2}H_{6}}=n_{CH_{4},C_{2}H_{6}}/n_{T}$. pyIAST did not print a warning that it needed to extrapolate the pure-component isotherm data for this IAST calculation, indicating that passing the fill_value in the InterpolatorIsotherm for ethane was not necessary. That is, we collected pure-component ethane adsorption isotherm data at a sufficiently high pressure for this IAST calculation.

Using the above procedure in a loop, we computed the mixed-gas adsorption isotherms $n_{CH_{4}}(y_{C_{2}H_{6}}, P=65$ bar) and $n_{C_{2}H_{6}}(y_{C_{2}H_{6}}, P=65$ bar) at varying gas phase compositions $y_{C_{2}H_{6}}$. Fig 6 shows that the component uptakes predicted by pyIAST match the binary-component grand-canonical Monte Carlo simulations of methane/ethane adsorption in IRMOF-1. This agreement serves as both partial verification of pyIAST and validation of IAST for a methane/ethane mixture in IRMOF-1 at these conditions.

![](./images/814569728658898944_8.jpg)

Figure 6: Verification and validation of IAST for IRMOF-1 in equilibrium with a methane/ethane mixture at 298 K and 65 bar total pressure. Shown are mixed-gas adsorption isotherms $n_{CH_{4}}(y_{C_{2}H_{6}}, P=65$ bar) (green) and $n_{C_{2}H_{6}}(y_{C_{2}H_{6}}, P=65$ bar) (red) as a function of the mole fraction of ethane in the gas phase, $y_{C_{2}H_{6}}$, computed with IAST (lines) and binary-component grand-canonical Monte Carlo simulations of methane/ethane adsorption (points).

### 4.3. Beyond binary mixtures

While our case study focused on a binary methane/ethane mixture, pyIAST can handle $>2$ components. Here, we compare IAST predictions to an experimentally measured tertiary-component gas adsorption isotherm. Mason and coworkers [13] measured pure-component water, carbon dioxide, and nitrogen adsorption isotherms in activated carbon AX-21 at $40\ ^{\circ}\text{C}$. Then, they measured the adsorption of nitrogen and carbon dioxide in the presence of a mixture of 166 mbar $\text{CO}_{2}$, 679 mbar $\text{N}_{2}$, and 20 mbar $\text{H}_{2}\text{O}$ at $40\ ^{\circ}\text{C}$ – a composition relevant to capturing $\text{CO}_{2}$ from the flue gas of coal-fired power plants. Here, we illustrate how pyIAST is used to predict the result.

Fig 7(a) and 7(b) (points) show the experimentally measured pure-component $\text{H}_{2}\text{O}$, $\text{CO}_{2}$, and $\text{N}_{2}$ adsorption isotherms in AX-21 at $40\ ^{\circ}\text{C}$. Using pyIAST, we fit Henry and Langmuir models to the $\text{N}_{2}$ and $\text{CO}_{2}$ isotherms, respectively, and use linear interpolation for the $\text{H}_{2}\text{O}$ isotherm since it exhibits a relatively complex shape. The lines in Figs 7(a) and 7(b) show the pyIAST fits to the data from the code below.

```python
import pandas as pd
import pyiast

df_N2 = pd.read_csv("N2.csv")
N2_isotherm = pyiast.ModelIsotherm(df_N2,
                                   loading_key="Loading(mmol/g)",
                                   pressure_key="P(bar)",
                                   model="Henry")

df_CO2 = pd.read_csv("CO2.csv")
CO2_isotherm = pyiast.ModelIsotherm(df_CO2,
                                    loading_key="Loading(mmol/g)",
                                    pressure_key="P(bar)",
                                    model="Langmuir")

df_H2O = pd.read_csv("H2O.csv")
H2O_isotherm = pyiast.InterpolatorIsotherm(df_H2O,
                                          loading_key="Loading(mmol/g)",
                                          pressure_key="P(bar)",
                                          fill_value=df_H2O["Loading(mmol/g)"].max())
```

We calculate the component loadings in AX-21 in the presence of the mixture with pyIAST by passing a list of partial pressures and pure-component isotherms to the `iast()` function. This returns an array `component_loadings` of component loadings at these gas conditions, predicted by IAST.

```python
# list of CO2, N2, and H2O partial pressures (bar)
partial_pressures = [0.166, 0.679, 0.02]
component_loadings = pyiast.iast(p,
                    [CO2_isotherm, N2_isotherm, H2O_isotherm])
# > array([ 0.51451255,  0.30433924,  0.61999649])
```

The solid bars in Fig. 7(c) show the experimentally measured $CO_2$ and $N_2$ uptakes in the presence of the mixture with their error bars (water uptake not reported). The decorated bars show the corresponding predictions according to pyIAST. Mason et al. [13] used IAST for a *binary* 166 mbar/679

mbar $CO_{2}/N_{2}$ mixture, ignoring the presence of water, and found that the predicted $CO_{2}$ uptake matches the experimental measurement very well; pyIAST's binary mixture calculations are consistent with theirs. Interest- ingly, IAST predicts that the addition of water- considering a 166 mbar/679 mbar/20 mbar $CO_{2}/N_{2}/H_{2}O$ mixture- enhances $CO_{2}$ and $N_{2}$ uptake from the binary case when water was ignored. As a result, the $CO_{2}$ uptake in the tertiary mixture according to IAST is greater than experiment. The reason is that IAST imposes that the free energy of mixing is given by the entropy of mixing; this implies that the energetics of the adsorbate-adsorbate interac- tions are the same between all species in the mixture. The water isotherm in Fig 7(a) is concave up, suggesting strong water-water interactions that yield cooperative adsorption. The ideal solution assumption in IAST imposes that adsorbed water molecules will similarly recruit more $CO_{2}$ and $N_{2}$ , explaining why IAST predicts that water enhances the uptake of $CO_{2}$ and $N_{2}$ beyond the binary case considered in Mason et al. [13].

### 4.4. Reverse IAST calculations
In reverse IAST, we specify the desired mole fractions in the adsorbed phase, $\{x_{i}\}$ , and the total bulk gas pressure $P_{T}$ and then calculate the bulk gas composition $\{y_{i}\}$ that yields these adsorbed mole fractions. This is useful for when one seeks to control the composition of the adsorbed phase, such as in catalysis [32]. As an example, we seek the bulk gas composition - at the same temperature as the pure-component isotherms, 298 K - that will yield a 50/50 mol % methane/ethane mixture in the adsorbed phase at a total bulk gas pressure of 65.0 bar. The following code will return two arrays `gas_mole_fractions` and `component_loadings`, the required mole fractions in the gas phase and the resulting component uptakes in the adsorbed phase, respectively.

```
total_pressure = 65.0  # total bulk gas pressure (bar)
adsorbed_mole_fractions = [0.5, 0.5]  # desired adsorbed mole fractions
gas_mole_fractions, component_loadings = pyiast.reverse_iast(
                                          adsorbed_mole_fractions,
                                          total_pressure,
                                          [ch3ch3_isotherm, ch4_isotherm])
```

![](./images/814569728658898944_9.jpg)

Figure 7: Applying IAST to a 3-component mixture of 166 mbar CO₂, 679 mbar N₂, and 20 mbar H₂O at 40 °C in equilibrium with an adsorbed phase in activated carbon AX-21 from Mason et al. [13]. (a, b) Pure-component H₂O (panel a), CO₂ (panel b, green), and N₂ (panel b, blue) isotherms in AX-21 at 40 °C from Ref. [13]. Points are experiment; lines are pyIAST fitted model predictions. Vertical lines show partial pressure of each component in the mixture. (c) Bar chart shows uptakes of CO₂ (green), N₂ (blue), and H₂O (red) in AX-21 in the presence of the mixture predicted by IAST from the pure-component isotherms (decorated) and measured by experiment (solid bars) [13]. Error bars are shown for the two experimental measurements; water uptake was not measured.

As both verification of our code and validation of reverse IAST for this methane/ethane mixture in IRMOF-1, we compare the reverse IAST calculations to binary grand-canonical Monte Carlo simulations of methane/ethane adsorption that yielded different adsorbed phase compositions, $x_{C_2H_6}$ (the same simulations in Fig 6). Fig 8 shows excellent agreement between reverse IAST calculations and our binary grand-canonical Monte Carlo simulations.

![](./images/814569728658898944_10.jpg)

Figure 8: Verification and validation of reverse IAST for IRMOF-1 in equilibrium with a methane/ethane mixture at 298 K and 65 bar. In reverse IAST, we specify the desired mole fraction of ethane in the adsorbed phase, $x_{C_2H_6}$, and calculate the gas phase mole fraction, $y_{C_2H_6}$, required to yield this desired adsorbed phase composition. The required $y_{C_2H_6}$ to yield desired $x_{C_2H_6}$, computed with IAST (lines) and found in binary-component grand-canonical Monte Carlo simulations of methane/ethane adsorption (points) are shown.

### 4.5. A remark on units

The units of pressure and gas adsorption in each pure-component adsorption isotherm DataFrame should be consistent. The pressures passed to pyIAST functions must be in the same units as the pure-component adsorption isotherm DataFrame corresponding to the `pressure_key` column. The mixed-gas adsorption outputs of pyIAST have the same units as the adsorption in the pure-component adsorption isotherm DataFrame corresponding to the `loading_key` column. Emphatically, gas adsorption must be in a molar unit (e.g. mol/g or $mmol/m^3$), and not mass (e.g. not $mg/m^3$), for the thermodynamic equations of IAST to hold.

### 4.6. Tests for further verification of pyIAST

While the agreement between pyIAST and binary grand-canonical Monte Carlo simulations in Fig 6 serves as validation of IAST for this ethane/methane mixture in IRMOF-1 and a partial verification for pyIAST, we outline two more comprehensive test suites here.

### 4.6.1. Isotherm fitting
To ensure that pyIAST correctly fits analytical models to pure-component isotherm data in the `ModelIsotherm` class, we generated synthetic data following each isotherm model available in pyIAST (a list can be found in `pyiast._MODELS`) for a given set of parameters. We then asserted that pyIAST correctly identified these parameters from the synthetic data. This test is available in the IPython Notebook `test/Isotherm tests.ipynb`.

### 4.6.2. Comparing to the competitive Langmuir isotherm
In the case that the pure-component adsorption isotherms follow a Langmuir model with the same saturation loading, IAST yields an analytical solution for the mixed-gas adsorption isotherm, the competitive Langmuir model in eqn 26. We verify that pyIAST solves the equations of IAST correctly by (1) generating synthetic pure-component isotherm data for fictitious gases A, B, and C that follow a Langmuir isotherm with the same saturation loading $M$ but different Langmuir constants, $K_i$ (see Fig 9(a)), (2) fitting Langmuir models to this synthetic data using pyIAST's `ModelIsotherm`, (3) using pyIAST to predict the mixed-gas adsorption isotherm of A, B, and C at 1 bar total pressure, thoroughly exploring ternary composition space, and (4) asserting that the loadings of A, B, and C predicted by pyIAST match the competitive Langmuir model in eqn 26. Fig 9 shows the ternary plots of the component loadings of A, B, and C according to the competitive Langmuir model (second from bottom row) and according to pyIAST (bottom row). Across all of ternary composition space, pyIAST matches the competitive Langmuir model. This test is available in the IPython Notebook `test/Test IAST for Langmuir case.ipynb`.

## 5. Limitations of IAST
Widely used [17], ideal adsorbed solution theory (IAST) has shown remarkable success in readily predicting mixed-gas adsorption isotherms from pure-component isotherms with a reasonable accuracy in a variety of systems [17]. Here, we duly remark that mixed-gas isotherms exhibit deviations from IAST when its assumptions are invalid [18, 19, 26, 54–57]. IAST rests upon the assumptions that:
(i) the adsorbates form an ideal mixture. Deviations from ideal mixing can occur due to appreciable energetic heterogeneity in the adsorbent surface [58–60] and size and asphericity differences between adsorbates [18, 61]. One

---

![](./images/814569728658898944_11.jpg)

Figure 9: Testing pyIAST for a tertiary mixture of fictitious gases A, B, and C at a total pressure of 1 bar. (a) We generated synthetic pure-component A, B, and C isotherm data that follow Langmuir models with saturation loading $M=1$ and Langmuir constants $K_A=2$, $K_B=10$, and $K_C=20$. (b-g) A point inside the triangle of this ternary plot represents a unique composition of the A/B/C mixture at 1 bar. The triangle is partitioned into hexagons. The color of each hexagon represents the uptake of species $i$ at the center of the hexagon according to the competitive Langmuir isotherm in eqn 26 (second from bottom rom) and pyIAST (bottom row). For each row, the three different triangles and colormaps represent the uptakes of species A, B, and C. The colors correspond to (a). Plots created by Ref. [53]

can account for non-ideality of adsorbates with an activity coefficient if mix- ture data is available [16] (real adsorbed solution theory [54, 62]). Energetic heterogeneity can be accounted for using heterogeneous IAST (HIAST [59]), which assumes IAST holds locally at each adsorption site; the overall adsorp- tion isotherm can be integrated over all sites using a distribution of energies [63]. Segregated IAST (SIAST) is another framework where the pore space of a material is partitioned into regions where IAST is applied separately [64].

(ii) adsorbates have access to the same area of surface. The latter assump- tion cannot hold, for example, in a molecular sieve, where the area accessible to each adsorbent is dependent upon the size of the adsorbate [16].

(iii) changes in the thermodynamic properties of the adsorbent are neg- ligible relative to the same properties for the adsorbate. This assumption is negated in materials that exhibit structural transitions upon gas adsorp- tion [13, 65]. Osmotic Framework Adsorbed Solution Theory (OFAST) [66] has been developed for predicting mixed-gas adsorption isotherms from pure- component adsorption isotherms in frameworks exhibiting structural transi- tions upon adsorption.

These corrections to IAST must often be implemented on a case-by-case basis and are difficult to include in a transferable code such as pyIAST.

## 6. Conclusions
While measuring pure-component adsorption isotherms is relatively rou- tine, measuring mixed-gas adsorption isotherms is complicated and time- consuming and requires custom instruments [13, 15]. Further, often one is interested in many different gas compositions and pressures; taking mixed-gas adsorption measurements at such an array of conditions is often impractical. Ideal adsorbed solution theory (IAST) [16] is a widely used [17] thermody- namic framework to predict mixed-gas adsorption isotherms from a set of pure-component adsorption isotherms at the same temperature.

We first reviewed the equations of IAST derived from thermodynam- ics and discussed the two disparate methods of characterizing the pure- component adsorption isotherms: fitting an analytical model and linearly interpolating the data. We then provided a tutorial of how to use our Python package pyIAST to perform IAST calculations using a case study of methane/ethane adsorption in a nanoporous material. pyIAST can han- dle an arbitrary number of components and is also capable of reverse IAST

calculations, where we calculate the gas phase composition to yield a desired adsorbed phase composition.

The source code for pyIAST, registered as an official Python package with the Python Package Index (PyPI) under an MIT license, is openly available on Github https://github.com/CorySimon/pyIAST. More extensive online documentation is hosted on Read the Docs, http://pyiast.readthedocs. org/en/latest/. Using the pip Python package manager, pyIAST can be easily installed in a single command in the terminal, `pip install pyiast`.

### 7. Acknowledgements
C.M.S. is supported by the U.S. Department of Energy, Office of Science, Office of Workforce Development for Teachers and Scientists, Office of Science Graduate Student Research (SCGSR) program. The SCGSR program is administered by the Oak Ridge Institute for Science and Education for the DOE under contract number DE-AC05-06OR23100. M.H. was supported by the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Chemical Sciences, Geosciences and Biosciences, under Award DE-FG02-12ER16362. Thanks to Jeffery A. Greathouse for invaluable discussions and providing literature. Thanks to Jarad Mason for kindly sending me his raw $CO_2$, $N_2$, and $H_2O$ isotherm data.

### 8. References

[1] J.-R. Li, J. Sculley, H.-C. Zhou, Metal-organic frameworks for separations, Chem. Rev. 112 (2) (2011) 869-932.

[2] D. M. D'Alessandro, B. Smit, J. R. Long, Carbon dioxide capture: prospects for new materials, Angew. Chem. Int. Ed. 49 (35) (2010) 6058-6082.

[3] E. D. Bloch, W. L. Queen, R. Krishna, J. M. Zadrozny, C. M. Brown, J. R. Long, Hydrocarbon separations in a metal-organic framework with open iron(II) coordination sites, Science 335 (6076) (2012) 1606-1610.

[4] D. Banerjee, A. J. Cairns, J. Liu, R. K. Motkuri, S. K. Nune, C. A. Fernandez, R. Krishna, D. M. Strachan, P. K. Thallapally, Potential of metal-organic frameworks for separation of xenon and krypton, Acc. Chem. Res. 48 (2) (2014) 211-219.

[5] L. E. Kreno, K. Leong, O. K. Farha, M. Allendorf, R. P. Van Duyne, J. T. Hupp, Metal-organic framework materials as chemical sensors, Chem. Rev. 112 (2) (2011) 1105-1125.

[6] J. Lee, O. K. Farha, J. Roberts, K. A. Scheidt, S. T. Nguyen, J. T. Hupp, Metal-organic framework materials as catalysts, Chem. Soc. Rev. 38 (5) (2009) 1450-1459.

[7] R. E. Morris, P. S. Wheatley, Gas storage in nanoporous materials, Angew. Chem. Int. Ed. 47 (27) (2008) 4966-4981.

[8] T. A. Makal, J.-R. Li, W. Lu, H.-C. Zhou, Methane storage in advanced porous materials, Chemical Society Reviews 41 (23) (2012) 7761-7779.

[9] L. Schlapbach, A. Züttel, Hydrogen-storage materials for mobile applications, Nature 414 (6861) (2001) 353-358.

[10] N. L. Rosi, J. Eckert, M. Eddaoudi, D. T. Vodak, J. Kim, M. O'Keeffe, O. M. Yaghi, Hydrogen storage in microporous metal-organic frameworks, Science 300 (5622) (2003) 1127-1129.

[11] O. Talu, Needs, status, techniques and problems with binary gas adsorption experiments, Adv. Colloid Interface Sci. 76 (1998) 227-269.

[12] H. Zhang, P. Deria, O. K. Farha, J. T. Hupp, R. Q. Snurr, A thermo- dynamic tank model for studying the effect of higher hydrocarbons on natural gas storage in metal-organic frameworks, Energy Environ. Sci.8 (5) (2015) 1501-1510.

[13] J. A. Mason, T. M. McDonald, T.-H. Bae, J. E. Bachman, K. Sumida, J. J. Dutton, S. S. Kaye, J. R. Long, Application of a high-throughput analyzer in evaluating solid adsorbents for post-combustion carbon cap- ture via multicomponent adsorption of $CO_{2}, N_{2}$ , and $H_{2} O$ , J. Am. Chem. Soc. 137 (14) (2015) 4787-4803.

[14] O. Talu, Measurement and analysis of mixture adsorption equilibrium in porous solids, Chem. Ing. Tech. 83 (1-2) (2011) 67-82.

[15] S. Sircar, Basic research needs for design of adsorptive gas separation processes, Ind. Eng. Chem. Res. 45 (16) (2006) 5435-5448.

[16] A. Myers, J. M. Prausnitz, Thermodynamics of mixed-gas adsorption, AIChE J. 11 (1) (1965) 121-127.

[17] K. S. Walton, D. S. Sholl, Predicting multicomponent adsorption: 50years of the ideal adsorbed solution theory, AIChE J. 61 (9) (2015)2757-2762.

[18] N. F. Cessford, N. A. Seaton, T. Duren, Evaluation of ideal adsorbed solution theory as a tool for the design of metal-organic framework materials, Ind. Eng. Chem. Res. 51 (13) (2012) 4911-4921.

[19] Q. Yang, C. Zhong, Molecular simulation of carbon diox- ide/methane/hydrogen mixture adsorption in metal-organic frame- works, J. Phys. Chem. B 110 (36) (2006) 17776-17783.

[20] R. Babarao, Z. Hu, J. Jiang, S. Chempath, S. I. Sandler, Storage and separation of $CO_{2}$ and $CH_{4}$ in silicalite, C168 schwarzite, and IRMOF1: a comparative study from Monte Carlo simulation, Langmuir 23 (2)(2007) 659-666.

[21] S. Keskin, J. Liu, J. K. Johnson, D. S. Sholl, Testing the accuracy of correlations for multicomponent mass transport of adsorbed gases in metal- organic frameworks: Diffusion of $H_{2}/CH_{4}$ mixtures in CuBTC, Langmuir 24 (15) (2008) 8254-8261.

[22] Y.-S. Bae, K. L. Mulfort, H. Frost, P. Ryan, S. Punnathanam, L. J. Broadbelt, J. T. Hupp, R. Q. Snurr, Separation of $\text{CO}_2$ from $\text{CH}_4$ using mixed-ligand metal- organic frameworks, Langmuir 24 (16) (2008) 8592-8598.

[23] B. Liu, Q. Yang, C. Xue, C. Zhong, B. Chen, B. Smit, Enhanced adsorp- tion selectivity of hydrogen/methane mixtures in metal- organic frame- works with interpenetration: A molecular simulation study, J. Phys. Chem. C 112 (26) (2008) 9854-9860.

[24] D. W. Hand, S. Loper, M. Ari, J. C. Crittenden, Prediction of multi- component adsorption equilibria using ideal adsorbed solution theory, Environ. Sci. Technol. 19 (11) (1985) 1037-1043.

[25] R. Krishna, S. Calero, B. Smit, Investigation of entropy effects during sorption of mixtures of alkanes in MFI zeolite, Chem. Eng. J. 88 (1) (2002) 81-94.

[26] J. Rother, T. Fieback, Multicomponent adsorption measurements on activated carbon, zeolite molecular sieve and metal-organic framework, Adsorption 19 (5) (2013) 1065-1074.

[27] D. Frenkel, B. Smit, Understanding Molecular Simulations: from Algo- rithms to Applications, 2nd Edition, Vol. 1, Academic Press, San Diego, 2002.

[28] S. Brunauer, P. H. Emmett, E. Teller, Adsorption of gases in multi- molecular layers, J. Am. Chem. Soc. 60 (2) (1938) 309-319.

[29] C. M. Simon, J. Kim, L.-C. Lin, R. L. Martin, M. Haranczyk, B. Smit, Optimizing nanoporous materials for gas storage, PCCP 16 (12) (2014) 5499-5513.

[30] T. Van Heest, S. L. Teich-McGoldrick, J. A. Greathouse, M. D. Allen- dorf, D. S. Sholl, Identification of metal-organic framework materials for adsorption separation of rare gases: Applicability of ideal adsorbed solution theory (IAST) and effects of inaccessible framework regions, J. Phys. Chem. C 116 (24) (2012) 13183-13195.

[31] H. Chen, D. S. Sholl, Examining the accuracy of ideal adsorbed solu- tion theory without curve-fitting using transition matrix Monte Carlo simulations, Langmuir 23 (11) (2007) 6431-6437.

[32] A. W. Thornton, D. A. Winkler, M. S. Liu, M. Haranczyk, D. F. Kennedy, Towards computational design of zeolite catalysts for $CO_{2}$ reduction, R. Soc. Chem. Adv. 5 (55) (2015) 44361-44370.

[33] M. S. Shell, Thermodynamics and Statistical Mechanics: An Integrated Approach, Cambridge University Press, 2015.

[34] C. Radke, J. Prausnitz, Thermodynamics of multi-solute adsorption from dilute liquid solutions, AIChE J. 18 (4) (1972) 761-768.

[35] A. Tarafder, M. Mazzotti, A method for deriving explicit binary isotherms obeying the ideal adsorbed solution theory, Chem. Eng. Tech- nol. 35 (1) (2012) 102-108.

[36] O. Talu, A. L. Myers, Rigorous thermodynamic treatment of gas ad- sorption, AIChE J. 34 (11) (1988) 1887-1893.

[37] J. Tóth, Some consequences of the application of incorrect gas/solid adsorption isotherm equations, J. Colloid Interface Sci. 185 (1) (1997)228-235.

[38] K. Y. Foo, B. H. Hameed, Insights into the modeling of adsorption isotherm systems, Chem. Eng. J. 156 (1) (2010) 2-10.

[39] H. M. F. Freundlich, Over the adsorption in solution, J. Phys. Chem.(1906) 385-471.

[40] T. L. Hill, An introduction to statistical thermodynamics, Dover Publi- cations, 1986.

[41] C. Hinz, Description of sorption data with isotherm equations, Geo- derma 99 (3) (2001) 225-243.

[42] C. H. Giles, D. Smith, A. Huitson, A general treatment and classification of the solute adsorption isotherm. I. Theoretical, J. Colloid Interface Sci.47 (3) (1974) 755-765.

[43] V. P. M.I. Tempkin, Kinetics of ammonia synthesis on promoted iron catalyst, Acta Phys. Chim. USSR 12 (1940) 327-356.

[44] M. D. LeVan, T. Vermeulen, Binary Langmuir and Freundlich isotherms for ideal adsorbed solutions, J. Phys. Chem. 85 (22) (1981) 3247-3250.

[45] M. Ilić, D. Flockerzi, A. Seidel-Morgenstern, A thermodynamically con- sistent explicit competitive adsorption isotherm model based on second-order single component behaviour, J. Chromatogr., A 1217 (14) (2010) 2132-2137.

[46] F. Gritti, G. Guiochon, Band splitting in overloaded isocratic elution chromatography: II. New competitive adsorption isotherms, J. Chro- matogr., A 1008 (1) (2003) 23-41.

[47] U. M. Ascher, C. Greif, A First Course on Numerical Methods, Vol. 7, SIAM, 2011.

[48] T. Hastie, R. Tibshirani, J. Friedman, T. Hastie, J. Friedman, R. Tib- shirani, The elements of statistical learning, Vol. 2, Springer, 2009.

[49] H. O. R. Landa, D. Flockerzi, A. Seidel-Morgenstern, A method for efficiently solving the IAST equations with an application to adsorber dynamics, AIChE J. 59 (4) (2013) 1263-1277.

[50] H. Li, M. Eddaoudi, M. O'Keeffe, O. M. Yaghi, Design and synthesis of an exceptionally stable and highly porous metal-organic framework, Nature 402 (6759) (1999) 276-279.

[51] J. A. Mason, M. Veenstra, J. R. Long, Evaluating metal-organic frame- works for natural gas storage, Chem. Sci. 5 (1) (2014) 32-51.

[52] C. M. Simon, J. Kim, D. A. Gomez-Gualdron, J. S. Camp, Y. G. Chung, R. L. Martin, R. Mercado, M. W. Deem, D. Gunter, M. Haranczyk, et al., The materials genome in action: identifying the performance limits for methane storage, Energy Environ. Sci. 8 (4) (2015) 1190-1199.

[53] M. Harper, Python-ternary: A python library for ternary plotshttps: //github.com/marcharper/python-ternary.

[54] E. Costa, J. Sotelo, G. Calleja, C. Marron, Adsorption of binary and ternary hydrocarbon gas mixtures on activated carbon: experimental determination and theoretical prediction of the ternary equilibrium data, AIChE J. 27 (1) (1981) 5–12.

[55] R. Krishna, J. Van Baten, Segregation effects in adsorption of $CO_2$-containing mixtures and their consequences for separation selectivities in cage-type zeolites, Sep. Purif. Technol. 61 (3) (2008) 414–423.

[56] A. Myers, Activity coefficients of mixtures adsorbed on heterogeneous surfaces, AIChE J. 29 (4) (1983) 691–693.

[57] Y. Wang, M. D. LeVan, Adsorption equilibrium of binary mixtures of carbon dioxide and water vapor on zeolites 5a and 13x, J. Chem. Eng. Data 55 (9) (2010) 3189–3195.

[58] S. Sircar, Influence of adsorbate size and adsorbent heterogeneity of IAST, AIChE J. 41 (5) (1995) 1135–1145.

[59] D. Valenzuela, A. L. Myers, O. Talu, I. Zwiebel, Adsorption of gas mixtures: effect of energetic heterogeneity, AIChE J. 34 (3) (1988) 397–402.

[60] M. Murthi, R. Q. Snurr, Effects of molecular siting and adsorbent hetero- geneity on the ideality of adsorption equilibria, Langmuir 20 (6) (2004) 2489–2497.

[61] J. Dunne, A. L. Myers, Adsorption of gas mixtures in micropores: effect of difference in size of adsorbate molecules, Chem. Eng. Sci. 49 (17) (1994) 2941–2951.

[62] O. Talu, I. Zwiebel, Multicomponent adsorption equilibria of nonideal mixtures, AIChE J. 32 (8) (1986) 1263–1276.

[63] X. Hu, D. D. Do, Comparing various multicomponent adsorption equi- librium models, AIChE J. 41 (6) (1995) 1585–1592.

[64] J. A. Swisher, L.-C. Lin, J. Kim, B. Smit, Evaluating mixture adsorption models using molecular simulation, AIChE J. 59 (8) (2013) 3054–3064.

[65] F.-X. Coudert, Responsive metal–organic frameworks and framework materials: Under pressure, taking the heat, in the spotlight, with friends, Chem. Mater. 27 (6) (2015) 1905–1916.

[66] F.-X. Coudert, C. Mellot-Draznieks, A. H. Fuchs, A. Boutin, Prediction of breathing and gate-opening transitions upon binary mixture adsorp- tion in metal- organic frameworks, J. Am. Chem. Soc. 131 (32) (2009) 11329–11331.

[67] M. G. Martin, J. I. Siepmann, Transferable potentials for phase equilib- ria. 1. united-atom description of n-alkanes, J. Phys. Chem. B 102 (14) (1998) 2569–2577.

[68] A. K. Rappé, C. J. Casewit, K. Colwell, W. Goddard Iii, W. Skiff, UFF, a full periodic table force field for molecular mechanics and molecular dynamics simulations, J. Am. Chem. Soc. 114 (25) (1992) 10024–10035.

### Appendix A. Two-dimensional ideal gas law

Consider an ideal gas of particles on a two-dimensional surface of area $a$.
The single-particle partition function $q$ is:

$$
q(a, T)=\frac{1}{\Lambda^{2}} \int_{a} e^{-\beta U(x)} d x=\frac{1}{\Lambda^{2}} a, \tag{A.1}
$$

where $\Lambda$ is the de Broglie wavelength, $U(x)$ is the energy as a function of
the position on the surface, $x$, of area $a$. For an ideal gas, $U(x)=0 \forall x$. For
a system of $N$ non-interacting, ideal gas particles, the canonical partition
function $Q$ is:

$$
Q(N, a, T)=\frac{1}{N !} q(a, T)^{N}. \tag{A.2}
$$

The product of single-particle partition functions appears because the par-
ticles are independent; we divide by $N!$ because the particles are indistin-
guishable.

By the first law of thermodynamics in differential form, the spreading
pressure $\pi$ is related to the Helmholtz free energy $A$ by:

$$
-\pi=\left(\frac{\partial A}{\partial a}\right)_{T, N}. \tag{A.3}
$$

Since the Helmholtz free energy $A=-k_{B} T \log Q$, this implies that:

$$
-\pi=-k_{B} T\left(\frac{\partial \log Q}{\partial a}\right)_{T, N}. \tag{A.4}
$$

Taking the logarithm of eqn A.2 and applying Stirling's approximation $\log (N !) \approx$
$N \log N - N$ for large $N$, we arrive at the equation of state for a two-
dimensional ideal gas:

$$
\pi=k_{B} T \frac{N}{a}. \tag{A.5}
$$

### Appendix B. Ideal gas chemical potential

Here, we derive the chemical potential of species $i$ in a mixture of ideal
gases. Without loss of generality, we consider a binary mixture of two com-
ponents.


Following the logic in Appendix A, the canonical partition function $Q$ for an ideal gas of $N_1$ particles of species 1 and $N_2$ particles of species 2 in a volume $V$ is:

$$
Q(N_1, N_2, V, T) = \left( \frac{1}{N_1!} \left( \frac{V}{\Lambda_1^3} \right)^{N_1} \right) \left( \frac{1}{N_2!} \left( \frac{V}{\Lambda_2^3} \right)^{N_2} \right). \tag{B.1}
$$

Now the product of single-particle partition functions is divided by $N_1!$ and $N_2!$ since particles of the same species are indistinguishable but we can distinguish between species 1 and 2. The chemical potential is related to the Helmholtz free energy $A$ by:

$$
\mu_i = \left( \frac{\partial A}{\partial N_i} \right)_{T,V,N_{j\neq i}}. \tag{B.2}
$$

Since the Helmholtz free energy $A = -k_B T \log Q$,

$$
\mu_i = -k_B T \left( \frac{\partial \log Q}{\partial N_i} \right)_{T,V,N_{j\neq i}}. \tag{B.3}
$$

Taking the logarithm of eqn B.1 and using Stirling's approximation $\log(N_i!) \approx N_i \log N_i - N_i$ for large $N_i$, we arrive at an expression for the chemical potential for species $i$ in an ideal gas:

$$
\mu_i = k_B T \log \left( \frac{N_i}{V} \right) + \log \Lambda_i^3. \tag{B.4}
$$

By the ideal gas law $p_i V = N_i k_B T$, where $p_i$ is the partial pressure of species $i$ in the mixture. Thus:

$$
\mu_i(T, P) = \mu_i^0(T) + k_B T \log p_i, \tag{B.5}
$$

where the reference chemical potential $\mu_i^0(T) = \log(\Lambda_i^3/(k_B T))$.

### Appendix C. Molecular simulation methods

Here, we outline the molecular simulation methods to obtain the pure-component and mixture methane/ ethane adsorption isotherms in the nanoporous material IRMOF-1 used for our test case for pyIAST.

We use the TraPPE united atom model for methane and ethane [67]. To model the energetics of the interaction of the adsorbate pseudoatoms with the atoms of the framework and with other adsorbate pseudoatoms, we use Lennard-Jones potentials; total energy is assumed to be pairwise additive. We take parameters for the framework atoms from the Universal Force Field [68] and parameters for ethane and methane pseudoatoms from the Ref. [67], applying Lorentz-Berthelot mixing rules to obtain cross-interaction parame- ters. We take van der Waals interactions beyond a cutoff distance of 12.5 Å to be negligible and thus zero, allowing us to implement periodic boundary con- ditions to mimic a crystal structure of infinite extent. We replicated the unit cell of IRMOF-1 twice in the $a$, $b$, and $c$ crystallographic directions to utilize the nearest image convention in applying periodic boundary conditions.

The IRMOF-1 crystal structure that we used for our molecular simula- tions is in the /test directory. The IRMOF-1 structure is taken to be rigid.

With the above energetic model, we use the grand-canonical Monte Carlo (GCMC) algorithm [27] to simulate methane/ ethane adsorption. We treat both methane and ethane as an ideal gas by considering pressure and fugacity to be equal. That is, in all plots, the pressure is actually the fugacity. We first superimposed a three-dimensional grid of points on the unit cell of the crystal and computed the potential energy of each adsorbate psuedoatom ($\text{CH}_3$ and $\text{CH}_4$) at each grid point. For our GCMC simulations, when we calculate the adsorbate-adsorbent interaction, we linearly interpolate this grid to speed-up our simulations. We used a grid resolution of $0.06$ Å.

For the pure-component adsorption isotherms, our Monte Carlo moves were particle transitions (30%), particle exchange (60%), and particle regrow moves (10%). We define a Monte Carlo cycle as $N$ Monte Carlo moves, where $N$ is the number of adsorbate molecules in our system or 20, whichever is greater. We used 200,000 Monte Carlo cycles, half of which were for equilibration/burn cycles. We found that the average number of particles in a unit cell of IRMOF-1 during the simulation does not change significantly when less cycles are used, indicating convergence.

For the binary component GCMC simulations, we utilized 50,000 cycles with 20,000 equilibration/burn cycles. The Monte Carlo moves here are particle translation (30%), particle exchange (50%), particle regrow (10%) and identity change (10%).

Program title: pyIAST

Catalogue identifier: AEZA_v1_0

Program summary URL: http://cpc.cs.qub.ac.uk/summaries
/AEZA_v1_0.html

Program obtainable from: CPC Program Library, Queen's
University, Belfast, N. Ireland

Licensing provisions: MIT

No. of lines in distributed program, including test data, etc.:
38478

No. of bytes in distributed program, including test data, etc.:
1918879

Distribution format: tar.gz

Programming language: Python.

Operating system: Linux, Mac, Windows.

Classification: 23.

External routines: Pandas, Numpy, Scipy

Nature of problem:
Using ideal adsorbed solution theory (IAST) to predict mixed
gas adsorption isotherms from pure-component adsorption
isotherm data.

Solution method:
Characterize the pure-component adsorption isotherm from
experimental or simulated data by fitting a model or using
linear interpolation; solve the nonlinear system of equations of
IAST.

Running time:
Less than a second.