Accepted Manuscript

Meso-scale simulation of elastocaloric cooling in SMA films

Frank Wendler, Hinnerk Ossmer, Christoph Chluba, Eckhard Quandt, Manfred Kohl

![](./images/813124236926255105_1.jpg)

PII: S1359-6454(17)30519-0

DOI: 10.1016/j.actamat.2017.06.044

Reference: AM 13879

To appear in: Acta Materialia

Received Date: 14 November 2016

Revised Date: 9 May 2017

Accepted Date: 21 June 2017

Please cite this article as: F. Wendler, H. Ossmer, C. Chluba, E. Quandt, M. Kohl, Meso-scale simulation of elastocaloric cooling in SMA films, Acta Materialia (2017), doi: 10.1016/j.actamat.2017.06.044.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

![](./images/813124236926255105_2.jpg)

# Meso-Scale Simulation of Elastocaloric Cooling in SMA Films

Frank Wendler¹, Hinnerk Ossmer¹, Christoph Chluba², Eckhard Quandt² and Manfred Kohl¹

¹Karlsruhe Institute of Technology (KIT), Institute of Microstructure Technology (IMT), Hermann-von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Germany
²University of Kiel, Chair for Inorganic Functional Materials, Faculty of Engineering, Institute for Materials Science, Kaiserstr. 2, 24143 Kiel, Germany

## Abstract
A model for the evolution of the mechanical and thermal properties of shape memory alloy (SMA) films during elastocaloric cycling is developed and compared with experiments. The focus is on Ti-Ni-Cu-Co films of $20\ \mu\text{m}$ thickness showing ultra-low fatigue properties. The films undergo a highly localized pseudoelastic transformation under tensile load cycling featuring strain and temperature band patterns that depend on the loading conditions. The corresponding temperature change is of special interest for film-based elastocaloric cooling applications. Starting from a thermodynamics-based Gibbs free energy model comprising mechanical and chemical contributions, we include a martensite-austenite interface free energy term, for which formulations from a phase-field model are adapted. A 3D continuum mechanics description is modified to treat plane stress conditions appropriate for polycrystalline thin films. The nucleation mechanism of strain bands under dynamic loading is described by introducing a spatial random distribution of the transformation stress barriers reflecting the degree of material inhomogeneity. Heat transfer due to conduction and convection is taken into account. The simulations predict the correlated mechanical and thermal local response of the films including band formation and evolution, tilt angle as well as strain-rate dependence. Macroscopic stress-strain characteristics and thermal evolution curves well represent the experimental results.

## 1. Introduction
The need for energy efficient and environmentally friendly cooling technologies has led to an increased interest in solid-state cooling based on caloric effects [1-3]. Amongst these, the elastocaloric effect is particularly promising, providing large temperature changes without the need for strong magnetic or electric fields [4, 5]. Elastocaloric cooling exploits the exchange

of latent heat during the diffusion-less first order phase transformation between austenite (A) and martensite (M) phase in shape memory alloys (SMA) subjected to external stress [6].

The corresponding stress-strain behavior is usually referred to as pseudoelasticity or superelasticity. TiNi-based alloys offer recoverable strains of up to 10%, latent heats of up to 30 J/g and temperature change of 25 - 58 K under adiabatic conditions [7, 8]. Recently, a number of demonstrators including heat recovery have been developed showing large cooling power and interesting values of COP exceeding 3 on the device level [9-12].

Due to favorable scaling behavior, elastocaloric cooling is well applicable for small scale applications, for example in microelectronics, bio-medical and lab-on-chip systems [13, 14]. The high-surface-to-volume ratio inherent to thin films enables fast heat transfer and high cycling rates, especially for the case of narrow hysteresis [9]. However, in microscale applications the localized nature of the transformation is an important issue, as it affects the dynamics of heat release and absorption. For polycrystalline TiNi, for instance, the stress-induced pseudoelastic transformation often evolves via local strain bands being in martensitic phase, which nucleate and propagate after an initial elastic deformation. These deformation bands, called Lüders-like strain bands (LSB), are mostly observed in thin samples. Their origin was explained as morphological instability driven by local geometric defects of the material, similar to a necking instability [15]. A strong dependence of the band number on the loading rate has been found, related to the change of temperature close to the transformation front [15, 16]. For the applications in elastocaloric cooling, important challenges are the understanding and control of these local strain and temperature effects as well as the heat transfer dynamics.

The modeling of the strain band mechanism involves a tight coupling of mechanics, phase kinetics and thermal evolution as well as a pronounced hysteresis in the stress-strain behavior. As the strain rate $\dot{\varepsilon}$ and heat transfer to the environment influence the thermal effect [17], a model for elastocaloric cooling has to capture the full sample geometry. In the literature, various models for the pseudoelastic deformation of polycrystalline SMAs have

been presented that differ in the length scale of interest, for instance the meso-scale (μm range) or the macroscopic (device) scale.

Micromechanical approaches resolve the evolution on a crystallographic (grain scale) level by constructing elastic, chemical and thermal energy contributions. Hence the typical grain sizes in TiNi films often being in the range below 1 μm restrict simulations to small representative volume elements in a hypothetically uniform sample [18, 19]. Macroscale models as those related to the work of Tanaka and Nagaki, for instance, use an equation of state to calculate the internal phase fraction as a function of temperature and stress [20]. They achieve a good prediction of the macroscopic properties under uniaxial stress, but need to prescribe the transformation direction (M→A, A→M) for the whole sample [21]. On a meso-scopic length scale, the approaches related to Shaw & Kyriakides [15] present a 3D continuum-level description that captures the martensitic transition with a $J_2$ plasticity model, where front speed and number of bands are implicitly determined as part of the thermo-mechanical problem. Macroscopic stress-strain features and evolving band number have been determined during rate-dependent loading of 1D wires in [22], but the irreversible approach excluded unloading associated with self-cooling. An extension to the reverse M→A transformation for a 1D problem is presented in [23] using a free energy density with a strain gradient term, and a kinetic law. A 3D model with plastic flow rules including a local reorientation of the transformation strain tensor has been formulated by Azadi et al. [24] and applied to strain band evolution in TiNi stripes [25].

In SMAs, the austenite-martensite interfacial energy is a significant contribution, which is related to mechanical incompatibilities of the adjacent phases and leads to the micro-elastic strains [26-28]. Phase-field (PF) models include this energy with a diffuse interface description that circumvents the singularities arising during nucleation, merging and vanishing of phase domains. At the scale of crystal grains, many PF models have been developed previously that use either the strain as order parameter with a Landau polynomial expansion for the free energy landscape [29], or a thermodynamic free energy and abstract order parameters (often a local phase fraction), e.g. [30]. Several PF models were introduced

recently, that are able to capture transformation band formation in polycrystalline alloys.

These models either reside in a 1D formulation applicable to wires [31, 32] or are restricted to isothermal conditions for small tube [33] or stripe samples [34].

Here, we present a validated temperature-dependent PF model that allows the simulation of the load-dependent formation and evolution of strain and temperature bands in SMA films at the mesoscopic scale (~10 $\mu$m resolution). Therefore, limitations of previous PF models related to linear kinetics and small bulk driving forces, as formulated, for instance in [30], are circumvented. Due to the special interest in describing elastocaloric cooling applications, relatively high strain rates up to $0.1\ \text{s}^{-1}$ will be explored.

### 2. Experimental Methods
The materials under investigation are $\text{Ti}_{54.7}\text{Ni}_{30.7}\text{Cu}_{12.3}\text{Co}_{2.3}$ films that exhibit extremely high cyclic stability. Details on film fabrication and properties have been published recently [9, 35-38]. The mechanical performance of the SMA films is investigated by uniaxial tensile tests.

Stripe-shaped samples of 1.75 mm width and 15 mm length are obtained by a sacrificial layer etching process as described in [37]. The film samples are attached to alumina plates at both ends with two-component adhesive, which are then connected to the tensile test machine equipped with a 50 N force sensor. The resolution of force and displacement measurement is 0.25 N and 0.25 $\mu$m, respectively. Cyclic tensile tests are performed at different strain rates. Each cycle comprises a strain-controlled loading and unloading step, each followed by a halting step of 10 s for temperature equalization. Unloading is stopped at a small pre-load of 30 MPa in order to avoid buckling of the film. A maximum strain of 2.1%, closely below the onset of the linear elastic martensite regime, is chosen to increase sample lifetime. During tensile test experiments, the time-dependent surface temperature of the sample is monitored by an infrared (IR) camera with a spatial resolution of 25 $\mu$m and a field-of-view of $16 \times 12\ \text{mm}^2$. Samples are covered with a thin layer of black carbon to increase emissivity. Simultaneously, a representative test area of $3 \times 2\ \text{mm}^2$ is observed by a CCD camera. The local strain distribution is evaluated by digital image correlation (DIC) with a resolution of 80 $\mu$m.

### 3. Experimental Results

#### 3.1. Performance at the Macroscale

The macroscopic stress-strain response of a TiNiCuCo film sample upon tensile load cycling is depicted in Fig. 1 for different strain rates. Engineering stress is determined by the measured force and initial cross section of the sample. The thermodynamic cycle comprises the following six stages:

(I.) In the first loading stage up to $\varepsilon \approx 0.6\%$ the material undergoes elastic deformation. The observed small deviation from linearity at the onset of the stress plateau can be attributed to a homogeneous transformation [8, 39, 40]. For instance, martensite fraction was found to reach 3% before strain localization sets in [41] and the amount of heat produced in this stage is typically very low [42].

(II.) The stress-induced A→M transformation starts in the second stage, which is associated with formation of local strain bands (LSBs) reminiscent of the mechanism of Lüders band formation in tensile loaded low-carbon steel. An almost horizontal stress plateau is observed in the quasistatic (isothermal) limit. The slope of this plateau increases for increasing strain rate due to self-heating as latent heat is released faster than transferred to the ambient [16].

(III.) During the third stage, strain is held constant for ten seconds, enabling the release of remaining latent heat to the environment. A stress decrease is observed, resembling high-temperature creep behavior in metals.

(IV.) The sample is in predominantly martensitic state and undergoes elastic unloading. We note that this is an idealization, as the real material probably contains both elastically loaded martensite and still untransformed austenite [43].

(V.) Subsequently, the stress plateau of unloading occurs due to the reverse M→A phase transformation at a lower stress level than the forward plateau.

(VI.) The last stage comprises elastic unloading in austenite phase and temperature equalization within a waiting time of 10 seconds.

![](./images/813124236926255105_3.jpg)

The mechanical work given by the enclosed area in the stress-strain characteristics is increasing with the strain rate, as does the inclination of the stress plateaus. Although the apparent stress level at the onset of the plateaus seem to increase, the deviation from the initial linear part (stage I) starts approximately at the same stress level for all strain rates. This is also the case at the end of the relaxation stage III and at the onset of the plateau stage (IV →V). This indicates (1) the existence of a critical stress level for onset of pseudo-elastic deformation, that is strain-rate independent and (2) that homogeneous transformations in both 'elastic' stages (I and IV) before onset of the plateau cause a negligible change of temperature affecting the plateau stress.

### 3.2. Performance at the Mesoscale
At the mesoscopic length scale, the localized stress-induced phase transformation during the stages II and V is investigated by in-situ DIC analysis [21]. Local strain maps from the test area in the center of the film (Fig. 2) show regions of high local strain that are considered as predominantly tension-oriented martensite, whereas regions of low strain are predominantly austenitic. During loading and unloading, the following observations are made:
- Stress-induced and reverse phase transformation occur by nucleation and propagation of Lüders-like bands with sharp interfaces.
- Bands are oriented at an angle of $55^\circ$ with respect to tensile (x-) direction.
- Both possible inclinations occur, leading to bands that cross or partly intersect.
- At low strain rate, few individual bands nucleate and propagate near sample fixations.
- Bands are randomly distributed along the sample length rather than being equidistant.
- Reverse and forward transformation bands appear at nearly the same positions.

The localized strain is associated with a localized temperature with similar distribution. However, only the fast transforming fronts produce sharp thermal bands (Fig. 2; also [35]).

Fig. 2 appears here

## 4. Thermomechanical Model

In this section, we formulate governing equations for martensite kinetics, mechanical displacement and temperature. Our approach is based on the Müller-Achenbach-Seelecke (MAS) model, which was developed to treat uniaxial stress loads [44-46] and was applied to polycrystalline SMA wires [47, 48]. We extend this model for plane stress conditions and interface energy in the following.

### 4.1 Kinetic Equations

In the MAS model the coexisting phases are austenite A and martensite phases M₊ and M₋, which each represent a coarse grained description of the microscopic set of variants that accommodate strain under tension (M₊) and compression (M₋) load. For transition kinetics, a Helmholtz free energy density $\varPsi(\varepsilon,T)$ is defined, which contains elastic and chemical contributions for the phases A, M₊ and M₋. It is piecewise defined as a continuous and differentiable function of scalar strain $\varepsilon$, connecting the minima of the phases in strain space,

$$
\varPsi(\varepsilon, T)= \begin{cases}\frac{E_{M}}{2}\left(\varepsilon+\varepsilon_{T}\right)^{2} & \varepsilon \leq-\gamma_{M}(T) \\ -\frac{E_{0}(T)}{2}\left(\varepsilon+\varepsilon_{0}(T)\right)^{2} & -\gamma_{M}(T) \leq \varepsilon \leq-\gamma_{A}(T) \\ \frac{E_{A}}{2} \varepsilon^{2}+\Delta \beta(T) & |\varepsilon| \leq \gamma_{A}(T) \\ -\frac{E_{0}(T)}{2}\left(\varepsilon-\varepsilon_{0}(T)\right)^{2} & \gamma_{A}(T) \leq \varepsilon \leq \gamma_{M}(T) \\ \frac{E_{M}}{2}\left(\varepsilon-\varepsilon_{T}\right)^{2} & \varepsilon \geq \gamma_{M}(T).\end{cases}\tag{1}
$$

$E_A$ and $E_M$ are the elastic moduli of A and M, $\varepsilon_T$ the transformation strain as determined from the onset of plateau stress in the stress-strain characteristic (Fig. 1), and $\beta(T)$ the chemical free energy difference between A and M. The parameters $E_0$, $\gamma_M$ and $\gamma_A$ are determined from the constraints to form a smoothly connected curve [46]. The Gibbs free energy $g(\sigma,\varepsilon,T)=$ $\varPsi(\varepsilon,T)-\sigma\varepsilon$ is chosen as the appropriate thermodynamic potential to include external loading conditions, and defines phase equilibria by the conditions $\frac{\partial g}{\partial \varepsilon}=0$ and $\frac{\partial^{2} g}{\partial \varepsilon^{2}}>0$. This 1D scalar strain description is applicable for problems such as tensile loading of TiNi wires [48] or bending of thin beams using Euler-Bernoulli theory [49]. Extension of the MAS model to multi-axial stress states was discussed for ferroelectric crystals [50, 51], but is

computationally costly due to the search for transition paths in a multi-dimensional free energy space. Here, we propose an efficient approach by retaining the 1D energy landscape in assuming that the transition always follows a linear strain path connecting the minima of austenite and martensite in the multi-dimensional strain space. Fig. 3(a) visualizes this transition path for the 2D strain space applicable for thin films ($g(\varepsilon) = \Psi(\varepsilon)$ for $\sigma = 0$ is chosen here). In this way, after a correction of the elastic moduli (Supplemental A), we can keep the energy formulation from Eq. (1).

Fig 3 appears here

In the MAS model, rate equations for the phase fractions of austenite ($x_A$), tension and compression martensite ($x_{M_+}$ and $x_{M_-}$) are formulated based on transition state theory as

$$
\dot{x}_{M_{+}}=-x_{M_{+}} p^{M_{+} A}+x_{A} p^{A M_{+}} \tag{2}
$$

$$
\dot{x}_{M_{-}}=-x_{M_{-}} p^{M_{-} A}+x_{A} p^{A M_{-}} \tag{3}
$$

$$
\dot{x}_{A}=-x_{A} p^{A M_{-}}-x_{A} p^{A M_{+}}+x_{M_{+}} p^{M_{+} A}+x_{M_{-}} p^{M_{-} A}. \tag{4}
$$

Microscopic layer elements of representative volume $V_D$ may transform from a parent phase $\alpha$ to a product phase $\beta$ with a transition rate $p^{\alpha \beta}$, even if a local energy barrier must be crossed. The transition rates are derived from Boltzmann factors, which include the quotient of the Gibbs free energy barrier $\Delta g V_D$ and the thermal energy $k_B T$ ($k_B$: Boltzmann constant) and include the approach frequency $1/\tau$ as a kinetic factor. For the study of pseudoelasticity, only $M_+$ and A are coexisting, so only $x_{M_+}$ from Eq. (2) needs to be determined ($x_A=1-x_{M_+}$). The transformation rates $p^{\alpha \beta}$ can be written in closed form [46] as

$$
p^{A M_{+}}(\sigma, T)=\frac{1}{\tau} \frac{e^{-\left(\frac{\sigma^{A M_{+}}-\sigma}{\omega_{A}}\right)^{2}}}{\operatorname{erf}\left(\frac{\sigma^{A M_{+}}-\sigma}{\omega_{A}}\right)+\operatorname{erf}\left(\frac{\sigma^{A M_{+}}+\sigma}{\omega_{A}}\right)} \tag{5}
$$

$$
p^{M_{+} A}(\sigma, T)=\frac{1}{\tau} \sqrt{\frac{E_{M}}{E_{A}}} \frac{e^{-\left(\frac{\sigma^{M_{+} A}-\sigma}{\omega_{M}}\right)^{2}}}{\operatorname{erfc}\left(\frac{\sigma^{M_{+} A}-\sigma}{\omega_{M}}\right)} \tag{6}
$$

Here, the coefficients $\omega_{\alpha}(T)=\sqrt{E_{\alpha} k_{B} T / V_{D}}$ ($\alpha$ = A, M$_+$) in the exponential factors introduce a stress scaling. As both formulations Eqs. (5, 6) diverge when $\sigma$ traverses the stress plateau value, we chose approximate functions given in Supplemental D, that also lead to a computational benefit after implementation within a finite element framework. The transition rates $p^{\alpha \beta}$ ($\alpha, \beta$ = A, M$_+$) are strongly nonlinear functions of the barrier stress, formulated as

$$
\sigma^{\alpha \beta}(T, \boldsymbol{r})=\left[\sigma_{0}^{\alpha \beta}+C^{\alpha \beta}\left(T-T_{r e f}\right)\right] \cdot(1+\xi(\boldsymbol{r})). \tag{7}
$$

The first factor in Eq. (7) is the conventional formulation for the transformation stress given by $\sigma_{0}^{\alpha \beta}$ at $T_{r e f}$, with a temperature dependence given by the reciprocal Clausius-Clapeyron coefficients $C^{\alpha \beta}=d \sigma^{\alpha \beta} / d T$ [44]. The second factor is a random distribution term $\xi(\boldsymbol{r})$ depending on the location $\boldsymbol{r}$ within the sample. We propose this material heterogeneity as a major factor to reproduce the evolution mechanism of the strain bands (see Sect. 4.6).

**Introduction of interface energy:** In a former study, the M-A interfacial energy in the MAS model has been taken into account as average interface energy per layer $E/N$, $\frac{E_{I}}{N}=2 e x_{A}\left(1-x_{A}\right)$, with $e$ the energy per interface and $x_{A}$ the austenite fraction [52]. Contrary to this approach, we consider the interface energy as an external energy contribution with separate evolution law, from which additional terms must be added to the MAS rate equations. Different from our previous work [21], we here integrate interface energy in a quantifiable way by comparison to a PF model of Allen-Cahn type, as described in [30]. In such a formulation, the total energy, which we interpret as the Gibbs free energy $G(\varepsilon, \sigma, T, x_{\alpha}, \nabla x_{\alpha})$, depends on the phase field variables and their gradients. We point out, that the phase fractions $x_{A}=1$ and $x_{A}=0$ on the length scale considered here correspond to predominantly austenitic and predominantly oriented martensitic polycrystals, respectively, which are not necessarily in a pure phase state. As mentioned before, a single phase field for the martensite phase fraction $x_{M}$ ($x_{A}=1-x_{M}$) is sufficient, simplifying the nomenclature.

The total energy in a PF model formulation is given by integration of bulk and interface density contributions as

$$
G_{total}(\varepsilon, \sigma, T, x_{M})=G_{bulk}(\varepsilon, \sigma, T, x_{M})+G_{int}(x_{M}, \nabla x_{M}), \tag{8}
$$

$$
G_{bulk}(\varepsilon, \sigma, T, x_{M})=\int\left\{g_{bulk}(\varepsilon, \sigma, T, x_{M})\right\} dV \tag{8a}
$$

$$
G_{int}(x_{M}, \nabla x_{M})=\int\left\{\gamma \delta|\nabla x_{M}|^{2}+\frac{\gamma}{\delta} 9 x_{M}{ }^{2}\left(1-x_{M}\right)^{2}\right\} dV \tag{8b}
$$

where $G_{int}$ is proportional to the interface tension $\gamma$. The parameter $\delta$ defines the length scale of the spatial transition from austenite to martensite phase, which is interpreted as the width of the transformation zone in the polycrystalline material. This width of the transformation zone can be considerably larger than the average grain size, which was recently found using SEM-DIC and EBSD [65]. The first term in Eq. (8b) is a gradient energy density, favoring smooth transitions between A and M phase. The second is a double-well potential which imposes an energy penalty on deviations from the bulk states $x_{M} \in\{0,1\}$, and ensures stability of the interface width in time. In this way a constant spatial profile for $x_{M}$ develops in equilibrium, so that an energy per unit area $\gamma$ is distributed over a distance $\delta$. This interfacial energy includes contributions from several length scales and is mostly micro-strain energy necessary to accommodate incompatible A and M phases. A PF model evolution equation can be derived from Eq. (8) for the martensite fraction by demanding a continuous decrease of free energy with time (time-dependent Ginzburg-Landau equation)

$$
\dot{x}_{M}=-\frac{\omega}{\delta} \frac{\tilde{\partial} G}{\tilde{\partial} x_{M}}=\omega\left(\frac{1}{\delta} \frac{\partial G_{b u l k}}{\partial x_{M}}+\gamma \nabla^{2} x_{M}-9 \frac{\gamma}{\delta^{2}} x_{M}\left(1-x_{M}\right)\left(1-2 x_{M}\right)\right), \tag{9}
$$

where $\frac{\tilde{\partial} G}{\tilde{\partial} x_{M}}$ here denotes the variational derivative of functional $G$ with respect to $x_{M}$ and $\omega$ is a kinetic coefficient [30]. The last two terms in Eq. (9) represent the effects of the interface that are not taken into account in the original rate equations of the MAS model (Eqs. (2-4)). By postulating that the interface evolves according to the energy minimization dictated by Eq. (9), we consider the interface energy-related terms as extensions to Eqs. (2-4) resulting in the following rate equations:

$$
\dot{x}_{M}=-x_{M} p^{M_{+} A}+x_{A} p^{A M_{+}}+\tilde{\gamma} \nabla^{2} x_{M}-9 \frac{\tilde{\gamma}}{\delta^{2}} x_{M}\left(1-x_{M}\right)\left(1-2 x_{M}\right) \tag{10}
$$

$$
\dot{x}_{A}=-x_{M}.
$$

$\tilde{\gamma}=\gamma\omega$ is the product of the kinetic coefficient of the PF model and the interface free energy, and determines the influence of the interface. In contrast to former gradient energy formulations [23, 35], the model is now defined with quantifiable values of interface energy and kinetic coefficient (see Supplemental B).

The coupling of the two approaches as expressed in Eq. (10) results in a hybrid MAS-PF model, that can be generalized to more than two coexisting phases, when interface energy is defined as given in [53]. This has the advantage of low computational costs when implemented in an FEM scheme and it retains the thermodynamically consistent description of phase transformation by the MAS model. Furthermore, a highly nonlinear kinetic relationship with hysteretic behavior is captured, different from the linear kinetics in standard PF models as described in [30, 53]. Hysteresis results as a consequence of the different transition paths under loading/unloading in the free energy landscape. It is important to note that this approach is not self-consistent, which would necessitate including the interface energy in the Gibbs free energy.

### 4.2 Mechanical Equations

The evolution law for the displacement vectors $\boldsymbol{u}$ (momentum conservation) writes
$$
\rho \ddot{\boldsymbol{u}}=-\nabla \cdot \boldsymbol{\sigma}, \tag{11}
$$
with $\rho$ the density, and $\boldsymbol{\sigma}$ the stress tensor. As elastic strain is defined as the difference between total strain $\boldsymbol{\varepsilon}$ and transformation strain $\boldsymbol{\varepsilon}_{T}$, stress follows the constitutive relation
$$
\boldsymbol{\sigma}=\boldsymbol{C}\left(\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}_{T}(\boldsymbol{x})\right), \tag{12}
$$
(isotropic Hooke's law) for which the finite strain approximation for the total strain $\boldsymbol{\varepsilon}=$ $1 / 2\left(\nabla \boldsymbol{u}+\nabla \boldsymbol{u}^{T}\right)$ is applied. We assume the tensile direction to be along the $x$-axis. The transformation strain tensor $\boldsymbol{\varepsilon}_{T}$ is then given by interpolation between the austenite and martensite strains using the phase fractions $x_{\alpha}$ as weight factors,
$$
\boldsymbol{\varepsilon}_{T}(\boldsymbol{x})=\sum_{\alpha} x_{\alpha} \boldsymbol{\varepsilon}_{T}^{\alpha}, \tag{13}
$$
$$
\text { with } \boldsymbol{\varepsilon}_{T}^{A}=\mathbf{0}, \boldsymbol{\varepsilon}_{T}^{M}=\left(\begin{array}{ccc}
\varepsilon_{T} & 0 & 0 \\
0 & -0.5 \varepsilon_{T} & 0 \\
0 & 0 & -0.5 \varepsilon_{T}
\end{array}\right) \tag{14}
$$

The form of $\varepsilon_{T}^{M}$ from Eq. (14) represents a constant homogeneous deformation, resulting in a longitudinal extension in x-direction and volume preserving lateral contraction, which is well fulfilled for the case of a thin film during uniaxial loading as studied here. $\varepsilon_{T}$ quantifies the amount of longitudinal deformation in the martensitic state, and can be extracted from the stress-strain characteristics of the material as indicated in Fig. 1. It must be noted that effects of thermal strain are neglected in Eq. (12), which is about two orders of magnitude smaller than $\varepsilon_{T}$. An isotropic elastic property tensor $C$ is assumed with fixed Poisson ratio of $\nu=0.3$ for all phases. Young's modulus is determined as phase-average of the reciprocal moduli

$$
E(\boldsymbol{x})=\left(\frac{x_{M}}{E_{M}}+\frac{x_{A}}{E_{A}}\right)^{-1}, \quad(15)
$$

where $E_{A}$ and $E_{M}$ are determined from the linear parts in the stress-strain characteristic Fig. 1 (stages I and IV). As the material transforms predominantly in (sharp) bands aligned transverse to the principle stress direction, the use of the Reuss limit as a lower bound for a laminate composite is reasonable, in which a given stress is assumed to act perpendicular to the lamination direction [54]. It was shown previously that this assumption leads to a good approximation of the free energy in polycrystalline TiNi [55].

The SMA stripe sample is defined as rectangle located in the xy-plane, and a plane stress state $(\sigma_{33}=0)$ is assumed for the 2D simulations. At the boundaries near the clamps, normal displacement components are chosen to be zero at one side and made time dependent at the other, representing the momentary external deformation. All other boundaries are treated as traction free, demanding $\boldsymbol{\sigma} \cdot \hat{\boldsymbol{n}}=\mathbf{0}$ for boundaries with unit normal $\hat{\boldsymbol{n}}$.

### 4.3 Temperature Evolution
Self-heating and self-cooling of the material mainly results from the release an uptake of latent heat during the phase transition, respectively. The thermal energy balance writes

$$
\rho c_{p} \dot{T}=\nabla \cdot k(\boldsymbol{x}) \nabla T+\Delta h^{A M_{+}}(\sigma) \cdot \dot{x}_{M}, \quad(16)
$$

where $k(\boldsymbol{x})$ denotes a phase dependent thermal conductivity, due to the large difference for austenite and martensite [56]. It is calculated locally as the phase average of the reciprocal conductivities $k_{A}$ and $k_{M}$,

$$
k(\boldsymbol{x})=\left(\frac{x_{A}}{k_{A}}+\frac{x_{M}}{k_{M}}\right)^{-1}. \tag{17}
$$

This is the mixing rule in a laminated A-M composite for heat flow perpendicular to the interfaces, what we assume here as the main direction of the temperature gradient according to the observed thermal patterns. The heat release/uptake rate in Eq. (16) includes the transformation enthalpy, which for the case of the $\mathrm{M}_{+} \leftrightarrow \mathrm{A}$ transition is given by [46]

$$
\Delta h^{A M_{+}}(\sigma)=\rho L+\frac{\sigma^{2}}{2}\left(\frac{1}{E_{A}}-\frac{1}{E_{M}}\right)+\sigma \varepsilon_{T} \tag{18}
$$

The first term $\rho L$ in Eq. (18) is the standard latent heat of entropic origin. The last two terms are stress-dependent contributions, taking into account the change of elastically stored energy and internal friction processes at the moving phase boundary. They increase the enthalpy by $4 \%$ for stress magnitude of $\sigma=\sigma^{\mathrm{AM}+} \approx 250 \mathrm{MPa}$, but may become significant when self-heating rises the stress level. In Eq. (18), we have neglected any caloric effect due to a change of specific heats of austenite and martensite that were found to be identical in our DSC measurements. Also, the heat produced by martensite-austenite interfaces is assumed to be negligible and therefore is not considered in Eq. (18). For the two fixed sample boundaries a constant temperature condition $(T=T_{0})$ is chosen, which are assumed to be perfect heat sinks. Convective air cooling is assumed at the remaining boundaries by applying the heat flux $\dot{q}=-h_{conv}(T-T_{0})$, where $h_{conv}$ denotes the convective heat transfer coefficient. Due to the high surface-to-volume ratio of the film, this constitutes the major mechanism, accounting for $84 \%$ of the heat loss.

Eqs. (16) and (11) are solved using the finite element software COMSOL Multiphysics with user defined functions for the elastic modulus, transformation strain and the heat source terms as given above. The martensite fraction Eq. (10) is treated by adapting a customable PDE solver module. Mechanical and phase evolution are coupled via the local phase fraction $x_{M}$ and a scalar stress $\sigma$, which enters the transformation rate Eqs. (5) and (6). We choose the maximum shear stress (Tresca stress) $\sigma_{T r}=1 / 2\left(\sigma_{1}-\sigma_{3}\right)$, calculated from the difference of the first and third principal stresses of the local stress. In order to include compressive

load conditions - although not necessary in the present study - the sign of the hydrostatic stress is taken into account, giving $\sigma = sign(\sigma_{11} + \sigma_{22} + \sigma_{33})\sigma_{Tr}$.

### 4.4 Simulation Parameters
All model parameters used in the following simulations are compiled in Table 1. Most of them were determined by mechanical, thermal and caloric characterization of the studied TiNiCuCo material. A detailed description of the parameter generation process can be found in Supplemental B and C.

**Table 1:** Thermomechanical, model-specific and process-related parameters used in the simulations; A denotes austenite, M oriented martensite.

<table>
<thead>
  <tr>
    <th>Thermomechanical parameter</th>
    <th>symbol</th>
    <th>value</th>
    <th>reference</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Plateau stress A→M</td>
    <td>$\sigma^{AM}$</td>
    <td>242 MPa</td>
    <td>this work</td>
  </tr>
  <tr>
    <td>Plateau stress M→A</td>
    <td>$\sigma^{MA}$</td>
    <td>134 MPa</td>
    <td>“</td>
  </tr>
  <tr>
    <td>$T$ for stress measurements</td>
    <td>$T_{ref}$</td>
    <td>294.45 K</td>
    <td>“</td>
  </tr>
  <tr>
    <td>A→M Clausius Clapeyron coeff.</td>
    <td>$c^{AM}$</td>
    <td>10.4 MPa/K</td>
    <td>“</td>
  </tr>
  <tr>
    <td>M→A Clausius Clapeyron coeff.</td>
    <td>$c^{MA}$</td>
    <td>14.0 MPa/K</td>
    <td>“</td>
  </tr>
  <tr>
    <td>Transformation strain</td>
    <td>$\varepsilon_{T}$</td>
    <td>0.0075</td>
    <td>“</td>
  </tr>
  <tr>
    <td>Young's modulus A</td>
    <td>$E_{A}$</td>
    <td>35.9 GPa</td>
    <td>“</td>
  </tr>
  <tr>
    <td>Young's modulus M</td>
    <td>$E_{M}$</td>
    <td>16 GPa</td>
    <td>“</td>
  </tr>
  <tr>
    <td>Poisson ratio</td>
    <td>$v$</td>
    <td>0.3</td>
    <td>[21]</td>
  </tr>
  <tr>
    <td>Density</td>
    <td>$\rho$</td>
    <td>6500 kg/m³</td>
    <td>[21]</td>
  </tr>
  <tr>
    <td>Latent heat</td>
    <td>$L$</td>
    <td>5.6 J/g (3.64·10⁷ J/m³)</td>
    <td>this work</td>
  </tr>
  <tr>
    <td>Heat capacity</td>
    <td>$C_{p}$</td>
    <td>420 J/kgK (2.73·10⁶ J/m³K)</td>
    <td>[35]</td>
  </tr>
  <tr>
    <td>Thermal conductivity A</td>
    <td>$k_{A}$</td>
    <td>18 W/mK</td>
    <td>[57]</td>
  </tr>
  <tr>
    <td>Thermal conductivity M</td>
    <td>$k_{M}$</td>
    <td>8.6 W/mK</td>
    <td>[57]</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th>MAS and PF model parameters</th>
    <th>symbol</th>
    <th>value</th>
    <th>reference</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Transforming layer volume</td>
    <td>$V_{D}$</td>
    <td>5·10⁻²³ m³</td>
    <td>[58]</td>
  </tr>
  <tr>
    <td>Relaxation time constant</td>
    <td>$\tau$</td>
    <td>1·10⁻³ s</td>
    <td>[48]</td>
  </tr>
  <tr>
    <td>Interface tension A-M</td>
    <td>$\gamma$</td>
    <td>12 Jm⁻²</td>
    <td>[28, 59]</td>
  </tr>
  <tr>
    <td>Kinetic coefficient</td>
    <td>$\omega$</td>
    <td>2·10⁻⁸ m⁴J⁻¹s⁻¹</td>
    <td>calculated<br>from [60]</td>
  </tr>
  <tr>
    <td></td>
    <td>$\tilde{\gamma}=\gamma\omega$</td>
    <td>10⁻⁸ - 10⁻⁶ m²s⁻¹</td>
    <td></td>
  </tr>
  <tr>
    <td>Interface width</td>
    <td>$2\delta$</td>
    <td>1.0·10⁻⁴ m</td>
    <td>[28]</td>
  </tr>
</tbody>
</table>

<table>
<thead>
  <tr>
    <th>Geometry and process parameters</th>
    <th>symbol</th>
    <th>value</th>
    <th>reference</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Sample dimensions</td>
    <td>$l \times w \times h$</td>
    <td>15 × 1.75 × 0.02 mm</td>
    <td>this work</td>
  </tr>
</tbody>
</table>

<table>
<tr><td>Strain rate</td><td>$\dot{\varepsilon}$</td><td>$0.0001-1\ s^{-1}$</td><td>"</td></tr>
<tr><td>Heat transfer coefficient</td><td>$h_t$</td><td>$20.0\ W/m^{2}K$</td><td>"</td></tr>
<tr><td>Ambient temperature</td><td>$T_0$</td><td>$294.65\ K$</td><td>"</td></tr>
</table>

### 4.5 Strain band angle

The shape of the transformation strain tensor imposes a macroscopic condition at the local scale, namely the deformation of the martensite with respect to the austenite. With the constant transformation strain tensor $\varepsilon_{T}^{M+}$ from Eq. (14) simulations at a rate of $\dot{\varepsilon}=10^{-3}\ s^{-1}$ are conducted without taking material heterogeneity into account. The sample center, as depicted in Fig. 4, shows martensite growing from both sample ends, after which strain bands with a roughly constant angle of $55^{\circ}$ with respect to the loading axis develop. This angle agrees with the DIC strain images and with literature data for thin TiNi stripe samples [35]. Interestingly, in the simulations the band tilt angle can be continuously changed between 45 and $90^{\circ}$, when the lateral transformation strain is unequally distributed between the diagonal components $\varepsilon_{T,22}$ and $\varepsilon_{T,33}$, taking into account that volume preservation demands for $\varepsilon_{T,22}+\varepsilon_{T,33}=-\varepsilon_{T,11}$. The two limiting cases, given by the tensors

$$
\varepsilon_{T}^{y}=\begin{pmatrix}
\varepsilon_{T} & 0 & 0 \\
0 & -\varepsilon_{T} & 0 \\
0 & 0 & 0
\end{pmatrix} \text{ and } \varepsilon_{T}^{z}=\begin{pmatrix}
\varepsilon_{T} & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -\varepsilon_{T}
\end{pmatrix} \tag{19}
$$

lead to $45^{\circ}$ and roughly $90^{\circ}$ band inclination (Fig. 4). Due to stress accumulation at the A-M-interface edges, the $90^{\circ}$ case does not show stable interface propagation, but a sequential separation of obtuse tilted martensite lamellae.

The nearly uniform uniaxial strain during loading, with small deviation at the edges of the sample clamps, justifies the assumed homogeneous transformation relation. By reorienting the transformation strain tensor into the local first principal stress direction it is possible to treat more general loading conditions, which has been used previously [24, 61]. A corresponding description of $\varepsilon_{T}$ is given in Eq. (A4) in Supplemental A and was tested in simulations. As no significant difference in the results is found, we keep the constant transformation strain tensor in the following.

Fig 4 appears here

### 4.6 Material Inhomogeneity and Interface Energy

External mechanical conditions like specimen fixation [62] and microstructural heterogeneity [63] both have a profound effect on the localization and propagation of strain during tensile deformation. In the stress-strain curve, heterogeneity results in a smooth transition from the elastic to the plateau stage (Fig. 1), which means that in parts of the sample the barrier stress is considerably smaller than the (macroscopic) plateau stress. Different from the homogenization approach of previous 1D-MAS models, where the stress barrier $\sigma_\alpha(T,x)$ has a dependency on the local martensite fraction $x$ [46, 47], we treat heterogeneity as local randomly distributed material parameters, e.g. elastic moduli or transformation strain. In the experiments, DIC images for repeated cycles showed strain bands appearing at the same locations [35], which supports this idea of a 'frozen in', static property. It is reasonable that spatial fluctuations influence the driving force for transformation, given by $\sigma^{\alpha\beta}-\sigma$. A direct influence would change the barrier height $\sigma^{\alpha\beta}$, an indirect effect would change the local stress level $\sigma$, e.g. as in the case of the stress fields forming around foreign-phase precipitates. We have performed simulation series with randomly distributed Young's moduli $E_A$, $E_M$ and transformation strain $\varepsilon_T$, while keeping the average value unchanged. From this analysis, we can exclude the indirect influence, as significant effects in the simulations occurred only at standard deviations larger than 50% of the average, which is too much to be caused by local fluctuations.

Instead, a low degree of scatter of about 1-5% of the transformation stress barrier $\sigma^{\alpha\beta}(\boldsymbol{r})$ as given by Eq. (7) provides a natural explanation for the nucleation of new strain bands ahead of the propagation front, as observed in the experiment (Sect. 3.2). This scatter could be related to precipitates or other material impurities, or residual stresses that have been conserved from previous plastic processes. In the simulations we apply a lognormal distribution of $\sigma^{\alpha\beta}(\boldsymbol{r})$ with standard deviation of 5% of $\sigma_0^{\alpha\beta}$ (12 MPa), which produces the observed band density at $\dot{\varepsilon}=10^{-3}$ s in the simulations. The propagation dynamics during the initial stage of loading is depicted in Fig. 5. In agreement with experimental observations, the transformation starts at the fixed sample ends where initially the highest stresses occur.

Approximately wedge-shaped martensite (blue: 100% austenite, red: 100% martensite) grows into the sample interior, emitting strain bands from the central tips. Additionally, martensite nucleates (bright blue) and quickly forms bands all across the austenitic region, showing two different band inclinations at ±55±1.5° with respect to the tensile direction and occasional crossings. Several bands fade away during the stage of nucleation due to the cost of interface energy. Although at this strain rate a single band orientation finally dominates, higher strain rates can lead to a criss-cross pattern.

Fig 5 appears here

The two factors in the model with the highest impact on the evolving phase morphology are the interface free energy $\tilde{\gamma}$, and the level of material heterogeneity, here defined as standard deviation of the plateau stress distribution $s(\sigma^{\alpha\beta})$. Interface energy suppresses nucleation and promotes propagation of continuous bands, whereas a significant scatter of $\sigma^{\alpha\beta}$ creates many new nuclei transforming at lower stress level. The interdependency of both factors is further discussed in Supplemental B, where we show that a realistic morphology only develops for appropriate values of both interface energy and plateau stress heterogeneity.

## 5. Simulations of Cyclic Loading
Similar to the experiment, the strain-controlled cycle (Sect. 2) is simulated by increasing the sample strain from zero to 2.1% at constant rate (loading) and holding it constant for 10 s to allow for thermal equilibration. Subsequently, the strain is decreased at the same rate and another rest time of 10 s is allocated. In contrast to the experiment, no prestress is applied.

### 5.1 Performance at the Macroscale
The engineering stress-strain characteristics are plotted in Fig. 6 for various strain rates in the range of $10^{-4}$ and $0.1\ s^{-1}$ corresponding to isothermal and quasi-adiabatic conditions, respectively. Stress is determined as the average of Tresca stress over the sample and the engineering strain as the ratio of sample displacement and length. For all loading rates, the parameter set reproduces the macroscopic mechanical response of the experiments well, especially at low strain rates of $10^{-4}\ s^{-1}$ - $10^{-3}\ s^{-1}$, where thermal effects due to the release or


uptake of latent heat are still minor. An exception is the initial stress peak in Fig. 6(a), which is not observed in the measured data. Notably, only the thermal coupling via self-heating or cooling changes the inclination of the stress plateaus in the model during stages II and VI (compare with Fig. 1).

Figure 6 appears here

At higher strain rates self-heating or -cooling increases the slope of the M→A and A→M stress plateaus. A saturation of the thermal effect is experimentally observed for strain rates above $10^{-1}\ \text{s}^{-1}$ [35]. The slope of the unloading transformation plateau (stage V) approaches that of the 'elastic' martensite unloading (stage IV) due to the increasing effect of self-cooling, see Fig. 6(d). The Clausius-Clapeyron coefficients of $C^{AM}=10.4\ \text{MPa/K}$ and $C^{MA}=14\ \text{MPa/K}$ applied here impose a higher stress change due to the thermal effect upon cooling. As the stress value approaches zero at the end of stage V, possible cycling frequencies are limited for elastocaloric applications. The backward transition kinetics appears then as a limiting factor, which is equally observed in the simulations. At the highest simulated strain rate of $\dot{\varepsilon}=10^{-1}\ \text{s}^{-1}$ problems with numerical convergence at the end of the cycle appear, as the remaining martensite is increasingly compressed due to the imposed displacement boundary condition.

Fig. 7 shows time-dependent experimental and simulated characteristics of macroscopic strain, stress, temperature in the sample center (1 x 1 mm²) and martensite volume fraction for strain rates $\dot{\varepsilon}$ of $10^{-3}$ and $10^{-2}\ \text{s}^{-1}$.

Figure 7 appears here

The dynamics of the stress-induced forward/reverse transformation is determined by the competition between release/absorption of latent heat, heat convection and conduction. These effects are well described by the simulation model. In particular, the stress relaxation during stage III at maximum strain of 2.1 % is clearly represented. Please note that the experimental characteristics have been shifted by 30 MPa to account for the prestrain applied in the experiment. The simulated martensite fraction indicates that the transformation

is incomplete at the end of loading stage II (89 % at $10^{-3}\ \text{s}^{-1}$, 70 % at $10^{-2}\ \text{s}^{-1}$) and continues during stage III up to values between 97.5 and 99 %. We conclude that the stress relaxation in stage III is caused by the ongoing phase transformation of the remaining austenite, as has also been observed earlier [64]. As will be shown below, some austenite remains as single or multiple bands in the simulations, which cannot be resolved, however, in experimental DIC strain maps. The cooling during thermal equilibration of the SMA sample in stage III is clearly observed. Here, temperature and stress drop are strictly related by $\Delta\sigma = C^{AM}\Delta T = 80$ MPa, following the Clausius-Clapeyron relation. For all strain rates, the exponential temperature decay in stage III is slower compared to the temperature increase in stage VI due to ongoing heat production in strained condition.

At low strain rate, no exact agreement between experimental and simulated temperatures is found as averaging in the sample center is affected by temperature bands forming at arbitrary locations. These effects disappear at higher strain rates of $10^{-2}\ \text{s}^{-1}$ and beyond due to averaging by the interaction of many temperature bands. At the low strain rate of $10^{-3}\ \text{s}^{-1}$ the experimental data shows a decline of temperature during 'elastic' unloading in stage IV different from the simulation. This is attributed to the sudden stop of heat production during the ongoing forward transformation when decreasing the stress. The strain rate dependencies of maximum and minimum temperatures during loading and unloading, respectively, are summarized in Supplemental E showing good accordance between experiment and simulation.

### 5.2 Performance at the Mesoscale
The evaluation of the thermomechanical response including local temperature and strain effects as a function of strain rate is a crucial test for the model. The evolving martensitic domain pattern is shown in Fig. 8 during loading and unloading at a strain rate of $10^{-3}\ \text{s}^{-1}$ ((a), upper panel) and $10^{-2}\ \text{s}^{-1}$ ((b), lower panel). The images are taken at approximately equidistant time steps, indicated by open circles in the strain plot in Fig. 7. The local martensite fraction $x_{M_{+}}$ shown here is proportional to the longitudinal transformation strain $\varepsilon_{T,11}$. As expected from experiment, the number of strain bands increases for increasing

strain rate. For comparison, an experimental strain map in the center of the SMA stripe is shown in Fig. 8(c) (lower panel) revealing a pattern with partly crossing bands similar as in the simulation Fig. 8(b).

Fig 8 appears here

A clear asymmetry between forward and reverse transformation is observed: During loading, well-defined strain bands evolve at the end of the elastic austenite regime in the stress-strain characteristics, shortly before the stress plateau $\sigma^{AM_{+}}$ is reached. After going through the elastic part of unloading (compare stage IV in Fig. 7) austenite starts to grow at the fixations, but also quickly appears throughout the sample in a homogeneous manner. At a later stage of the reverse transformation clear austenite bands appear. In both cycles displayed in Fig. 8 the transformation is not complete at the end of the loading ramp and continues while the sample rests at constant maximum strain ($t = 21$ s for $\dot{\varepsilon}=10^{-2}\ \text{s}^{-1}$ and 2.3 s for $10^{-2}\ \text{s}^{-1}$).

Comparing the evolution at the end of the plateau stages (II and IV), the kinetics is faster for the M$\rightarrow$A as compared to the A$\rightarrow$M transformation. This occurs despite the 50 % lower stress rate during unloading, which is imposed by the constant strain rate and the lower modulus of martensite ($E_A \approx 0.5\ E_M$). As an example for the overall change of martensite fraction refer to Fig. 7 (lower panel).

Several factors affect the thermal profiles during transformation, namely the M-A front velocity, the transition width of M-A interface zone and the efficiency of the thermal transport described by the heat conductivity and convective heat transfer coefficient. As an example, Fig. 9 shows local temperature maps from the simulation at strain rate $\dot{\varepsilon}=10^{-3}\ \text{s}^{-1}$ in comparison with the experimental IR images. These images may be also compared with the martensitic domain pattern in Fig. 8 (a) at respective time steps. Upon loading (Fig. 9 (a)), thermal bands proceeding from the sample ends to the center are dominating. The number of perceivable temperature bands is typically much lower at low strain rate compared to high strain rate. This is because only few fast moving phase fronts produce significant heat, while weaker strain bands moving at lower speed contribute much less. During the unloading process, experimental and simulated patterns differ: In the simulation, the cooling effect is


dominated by the austenite interface growing from the clamps towards the center. In the experiment, cooling bands are formed primarily in the sample center, which can be attributed to the incomplete forward transformation affecting the evolution of martensite during reverse transformation.

Figure 9 appears here

### 6. Discussion
The model well represents the observed thermomechanic behavior and produces a band morphology close to observation. The stress-strain behavior is fully explained by heat transfer dynamics and resulting evolution of phase transformation due to the Clausius-Clapeyron dependency. Hence, no further parameters like propagation stress or rate-dependent frictional terms are necessary. Three major factors have been found to be essential for Lüders-like strain band formation:

(1) A homogeneous transformation strain $\varepsilon_T$ (Eq. (14)) between austenite and martensite in the elastic energy, that imposes equal lateral contraction and leads to strain band angles at ~55°. An extension to general plane stress conditions is possible (Eq. (A4), Supplemental A).

(2) The interface energy as defined in Eq. (8b) produces stable A-M interfaces and corresponds to an energy barrier for the nucleation of new martensite bands.

(3) The random distribution of the stress barrier generates M/A nuclei statistically distributed along the sample. The simulated patterns closely resemble the observed DIC strain maps. In the A→M transition, strain bands partly emanate from the wedge-like martensite fronts, and partly nucleate ahead of the front in the sample interior.

The spatial noise of the barrier stress given by $s(\sigma^{AM+})$ and the interface energy $\gamma$ are strongly correlated, so that the initial density of nucleated strain bands can be adapted by the combination of both. With the present parameter choice the sample of 15 mm length produces a single band at strain rate $10^{-4}\ \text{s}^{-1}$, 4 bands at $10^{-3}\ \text{s}^{-1}$ and 18 at $10^{-2}\ \text{s}^{-1}$. There are several possible origins of the scatter in $\sigma^{AM+}$, for instance fluctuations in precipitate density, which were found in this material [38] or textural fluctuations. We tentatively propose here a negative correlation between transformation strain $\varepsilon_T$ and barrier stress, which has also been

suggested previously [63]. This provides an explanation for recoverable strain decrease and reduction of plateau stresses in the case of material fatigue, an ubiquitous feature in conventional TiNi based SMAs: Plastic processes reduce $\varepsilon_T$ locally, and lead to residual stresses, that reduce the transformation barrier. On the other hand, the simulations show that without a significant amount of interface energy, the localized nature of the transition decreases and bands become more granular and blurred (See Supplemental, Fig. S2). A similar effect has been often observed in cyclically loaded NiTi as a concomitant of functional fatigue (e.g. [35]). The relationship between the properties of the stress barrier noise (width of distribution, local correlations), the magnitude of interface energy and the localization of strain is an open issue and will be examined in further work.

The A→M transformation continues after the end of loading under strain control (beginning of stage III), which fully explains the stress drop observed in the experiments. Therefore, also heat release continues during the thermal equilibration stage II. This leads to an asymmetry of temperature equilibration, which is found to be shorter for stage VI, corresponding to the cooling of a heat source, than for stage III, corresponding to the heating of a heat sink.

Probably, the A→M forward transformation is not complete, as the latent heat determined by DSC (13.7 J/g) had to be reduced significantly in the simulations to 5.6 J/g to predict the temperature effect correctly. Thus, a 'fully transformed' part of the sample ($x_{M_+}=1$) under the conditions of our experiment could consist of less than 50% martensite. Several studies on NiTi report a small homogeneous transformation (~0.5 %) preceding the nucleation of strain bands in tensile loading, e.g. for microtubes [41] and flat stripes [42]. In this work, both simulation and experiment indicate that in the TiNiCuCo sample nearly no martensite is formed before reaching the stress plateau $\sigma^{AM}$, apart from some early martensite formation appearing at places with low stress barrier, determined by the spatial noise. Contrarily, a significant amount of austenite is formed during 'elastic' unloading of martensite before strain bands evolve, recognizable at the temperature drop in stage IV (Fig. 7). This effect is present, but very weak, also in the simulations, where a remaining thin band of austenite


starts to expand again. For a more comprehensive treatment the 'elastic' martensite, which does not represent the fully transformed state, could be regarded as a composite of martensite and retained austenite at the microscale.

The simulations show that the number of thermal bands arising during superelastic SMA cycling may differ from the number of local strain bands for low strain rates. As many A-M fronts propagate at low velocity, their thermal signal is quickly smoothened by the fast heat transport. For instance, at $\dot{\varepsilon} \leq 10^{-3} \mathrm{~s}^{-1}$ only the two outer M-A fronts close to the clamps leave a clear thermal trace (Fig. 9).

### 7. Conclusions
In order to simulate the local strain response during uniaxial loading of SMA thin films, a hybrid model is proposed based on the Müller-Achenbach-Seelecke (MAS) model that is extended by interface energy terms originating from phase-field (PF) modeling. The model can be parameterized using experimental stress-strain characteristics and DSC measurements that provide the elementary thermomechanical constants. Material inhomogeneity is introduced as a spatially distributed random transformation stress, which – together with the martensite-austenite interface energy – leads to Lüders-like strain bands as observed in DIC images.

Thermo-mechanically coupled material behavior for various strain rates from $\dot{\varepsilon}=10^{-4} \mathrm{~s}^{-1}$ to $10^{-1} \mathrm{~s}^{-1}$ is well represented by the simulations. The stress drop during the rest periods in the strain cycle is related to a continuing forward transformation, driven by sample cooling and quantitatively corresponds to the thermal effect related to the A-M phase diagram.

The obtained model is used to study cooling with SMA thin films, and further permits the study of SMA film vibration damping, as general time-dependent 2D plane stress problems can be treated. An extension of the model to 3D for true multiaxial stress states requires additional analysis and adaption of the elastic energy landscape. Furthermore, the dependency of the band formation on M-A interface energy and the proposed connection between local transformation strain and transformation barrier stress points towards a way to incorporate functional fatigue into the model.

### Acknowledgements

The authors gratefully acknowledge funding by the German Science Foundation (DFG) within the priority program SPP1599 (www.ferroiccooling.de). We thank S. Seelecke for fruitful discussions about model and simulations.

### References

[1] Takeuchi I, Sandeman K. Solid-state cooling with caloric materials. Physics Today 2015;68:48.

[2] Fähler S, Rößler UK, Kastner O, Eckert J, Eggeler G, Emmerich H, Entel P, Müller S, Quandt E, Albe K. Caloric Effects in Ferroic Materials: New Concepts for Cooling. Advanced Engineering Materials 2012;14:10.

[3] Mañosa L, Planes A, Acet M. Advanced materials for solid-state refrigeration. Journal of Materials Chemistry A 2013;1:4925.

[4] Cui J, Wu Y, Muehlbauer J, Hwang Y, Radermacher R, Fackler S, Wuttig M, Takeuchi I. Demonstration of high efficiency elastocaloric cooling with large $\Delta$T using NiTi wires. Applied Physics Letters 2012;101:073904.

[5] Goetzler W, Zogg R, Young J, Johnson C. Energy Savings Potential and RD&D Opportunities for Non-Vapor-Compression HVAC Technologies, prepared for U.S. Department of Energy (Navigant Consulting, Inc., 2014). 2014.

[6] Bonnot E, Romero R, Manosa L, Vives E, Planes A. Elastocaloric effect associated with the martensitic transition in shape-memory alloys. Physical review letters 2008;100:125901.

[7] Otubo J, Rigo OD, Coelho AA, Neto CM, Mei PR. The influence of carbon and oxygen content on the martensitic transformation temperatures and enthalpies of NiTi shape memory alloy. Materials Science and Engineering: A 2008;481-482:639.

[8] Pieczyska EA, Gadaj SP, Nowacki WK, Tobushi H. Phase-Transformation Fronts Evolution for Stress- and Strain-Controlled Tension Tests in TiNi Shape Memory Alloy. Experimental Mechanics 2006;46:531.

[9] Ossmer H, Chluba C, Kauffmann-Weiss S, Quandt E, Kohl M. TiNi-based films for elastocaloric microcooling— Fatigue life and device performance. APL Materials 2016;4:064102.

[10] Ossmer H, Wendler F, Gueltig M, Lambrecht F, Miyazaki S, Kohl M. Energy-efficient miniature-scale heat pumping based on shape memory alloys. Smart Materials and Structures 2016;25:085037.

[11] Tušek J, Engelbrecht K, Eriksen D, Dall'Olio S, Tušek J, Pryds N. A regenerative elastocaloric heat pump. Nature Energy 2016;1:16134.

[12] Qian S, Ling J, Hwang Y, Radermacher R, Takeuchi I. Thermodynamics cycle analysis and numerical modeling of thermoelastic cooling systems. International Journal of Refrigeration 2015;56:65.

[13] Carmo JP, Silva MF, Ribeiro JF, Wolffenbuttel RF, Alpuim P, Rocha JG, Gonçalves LM, Correia JH. Digitally-controlled array of solid-state microcoolers for use in surgery. Microsystem Technologies 2011;17:1283.

[14] El-Ali J, Perch-Nielsen IR, Poulsen CR, Bang DD, Telleman P, Wolff A. Simulation and experimental validation of a SU-8 based PCR thermocycler chip with integrated heaters and temperature sensor. Sensors and Actuators A: Physical 2004;110:3.

[15] Shaw JA, Kyriakides S. Initiation and Propagation of localized Deformation in elasto-plastic Strips under uniaxial Tension. International Journal of Plasticity 1998;13:837.

[16] He YJ, Sun QP. Rate-dependent domain spacing in a stretched NiTi strip. International Journal of Solids and Structures 2010;47:2775.

[17] Depriester D, Maynadier A, Lavernhe-Taillard K, Hubert O. Thermomechanical modelling of a NiTi SMA sample submitted to displacement-controlled tensile test. International Journal of Solids and Structures 2014;51:1901.

[18] Patoor E, Lagoudas DC, Entchev PB, Brinson LC, Gao X. Shape memory alloys, Part I: General properties and modeling of single crystals. Mechanics of Materials 2006;38:391.

[19] Lagoudas DC, Entchev PB, Popov P, Patoor E, Brinson LC, Gao X. Shape memory alloys, Part II: Modeling of polycrystals. Mechanics of Materials 2006;38:430.

[20] Tanaka K, Nagaki S. A Thermomechanical Description of Materials with Internal Variables in the Process of Phase Transitions. Ingenieur-Archiv 1982;51:287.

[21] Ossmer H, Lambrecht F, Gültig M, Chluba C, Quandt E, Kohl M. Evolution of temperature profiles in TiNi films for elastocaloric cooling. Acta Materialia 2014;81:9.

[22] Iadicola MA, Shaw JA. Rate and thermal sensitivities of unstable transformation behavior in a shape memory alloy. International Journal of Plasticity 2014;20:577.

[23] Chang B-C, Shaw JA, Iadicola MA. Thermodynamics of Shape Memory Alloy Wire: Modeling, Experiments, and Application. Continuum Mechanics and Thermodynamics 2006;18:83.

[24] Azadi B, Rajapakse RKND, Maijer DM. Multi-dimensional constitutive modeling of SMA during unstable pseudoelastic behavior. International Journal of Solids and Structures 2007;44:6473.

[25] Azadi Borujeni B, Maijer DM, Rajapakse RKND. Finite Element Simulation of Strain Rate Effects on localized unstable pseudoelastic Response of Shape Memory Alloys. Journal of Mechanics of Materials and Structures 2008;3:1811.

[26] Stupkiewicz S, Maciejewski G, Petryk H. Elastic micro-strain energy of austenite- martensite interface in NiTi. Modelling and Simulation in Materials Science and Engineering 2012;20:035001.

[27] Petryk H, Stupkiewicz S, Maciejewski G. Interfacial energy and dissipation in martensitic phase transformations. Part II: Size effects in pseudoelasticity. Journal of the Mechanics and Physics of Solids 2010;58:373.

[28] Dong L, Zhou RH, Wang XL, Hu GK, Sun QP. On interfacial energy of macroscopic domains in polycrystalline NiTi shape memory alloys. International Journal of Solids and Structures 2016;80:445.

[29] Levitas VI. Phase field approach to martensitic phase transformations with large strains and interface stresses. Journal of the Mechanics and Physics of Solids 2014;70:154.

[30] Mennerich C, Wendler F, Jainta M, Nestler B. Rearrangement of martensitic variants in Ni2MnGa studied with the phase-field method. The European Physical Journal B 2013;86.

[31] Grandi D, Maraldi M, Molari L. A macroscale phase-field model for shape memory alloys with non-isothermal effects: Influence of strain rate and environmental conditions on the mechanical response. Acta Materialia 2012;60:179.

[32] Maraldi M, Molari L, Grandi D. A non-isothermal phase-field model for shape memory alloys: Numerical simulations of superelasticity and shape memory effect under stress- controlled conditions. Journal of Intelligent Material Systems and Structures 2012;23:1083.

[33] He YJ, Sun QP. Effects of structural and material length scales on stress-induced martensite macro-domain patterns in tube configurations. International Journal of Solids and Structures 2009;46:3045.

[34] He YJ, Sun QP. Macroscopic equilibrium domain structure and geometric compatibility in elastic phase transition of thin plates. International Journal of Mechanical Sciences 2010;52:198.

[35] Ossmer H, Chluba C, Gueltig M, Quandt E, Kohl M. Local Evolution of the Elastocaloric Effect in TiNi-Based Films. Shape Memory and Superelasticity 2015;1:142.

[36] Chluba C, Ossmer H, Zamponi C, Kohl M, Quandt E. Ultra-Low Fatigue Quaternary TiNi-Based Films for Elastocaloric Cooling. Shape Memory and Superelasticity 2016;2:95.

[37] Bechtold C, Chluba C, Lima de Miranda R, Quandt E. High cyclic stability of the elastocaloric effect in sputtered TiNiCu shape memory films. Applied Physics Letters 2012;101:091903.

[38] Chluba C, Ge W, Lima de Miranda R, Strobel J, Kienle L, Quandt E, Wuttig M. Ultralow-fatigue shape memory alloy films. Science 2015;348:1004.

[39] Shaw JA, Kyriakides S. On the Nucleation and Propagation of Phase Transformation Fronts in a NiTi alloy. Acta Materialia 1997;45:683.

[40] Shaw JA. Simulations of localized thermo-mechanical behavior in a NiTi shape memory alloy. International Journal of Plasticity 2000;16:541.

[41] Li ZQ, Sun QP. The initiation and growth of macroscopic martensite band in nano- grained NiTi microtube under tension. Intenational Journal of Plasticity 2002;18:1481.

[42] Pieczyska EA, Tobushi H, Kulasinski K. Development of transformation bands in TiNi SMA for various stress and strain rates studied by a fast and sensitive infrared camera. Smart Materials and Structures 2013;22:035007.

[43] Liu Y, Houver I, Xiang H, Bataillard L, Miyazaki S. Strain Dependence of Pseudoelastic Hysteresis of NiTi. Metallurgical and Materials Transactions A 1999;30A:1275.

[44] Müller I, Seelecke S. Thermodynamic Aspects of Shape Memory Alloys. Mathematical and Computer Modelling 2001;34:1307.

[45] Seelecke S, Müller I. Shape memory alloy actuators in smart structures: Modeling and simulation. Applied Mechanics Reviews 2004;57:23.

[46] Massad JE, Smith RC. A homogenized free energy model for hysteresis in thin-film shape memory alloys. Thin Solid Films 2005;489:266.

[47] Heintze O, Seelecke S. A coupled thermomechanical model for shape memory alloys—From single crystal to polycrystal. Materials Science and Engineering: A 2008;481-482:389.

[48] Furst SJ, Crews JH, Seelecke S. Numerical and experimental analysis of inhomogeneities in SMA wires induced by thermal boundary conditions. Continuum Mechanics and Thermodynamics 2012;24:485.

[49] Richter F, Kastner O, Eggeler G. Finite-Element Simulation of the Anti-Buckling-Effect of a Shape Memory Alloy Bar. Journal of Materials Engineering and Performance 2011;20:719.

[50] Seelecke S, Kim S-J, Ball BL, Smith RC. A rate-dependent two-dimensional free energy model for ferroelectric single crystals. Continuum Mechanics and Thermodynamics 2005;17:337.

[51] Kim S-J, Seelecke S. A rate-dependent three-dimensional free energy model for ferroelectric single crystals. International Journal of Solids and Structures 2007;44:1196.

[52] Achenbach M. A model for an alloy with shape memory. International Journal of Plasticity 1989;5:371.

[53] Nestler B, Garcke H, Stinner B. Multicomponent alloy solidification: phase-field modeling and simulations. Physical review. E, Statistical, nonlinear, and soft matter physics 2005;71:041609.

[54] Liu B, Feng X, Zhang S-M. The effective Young's modulus of composites beyond the Voigt estimation due to the Poisson effect. Composites Science and Technology 2009;69:2198.

[55] Hackl K, Heinen R. An upper bound to the free energy of n-variant polycrystalline shape memory alloys. Journal of the Mechanics and Physics of Solids 2008;56:2832.

[56] Faulkner MG, Amalraj JJ, Bhattacharyya A. Experimental determination of thermal and electrical properties of Ni-Ti shape memory wires. Smart Materials and Structures 2000;9:632.

[57] Coda A, Urbano M, Fumagalli L, Butera F. Investigation on the Hysteretic Behavior of NiTi Shape Memory Wires Actuated Under Quasi-Equilibrium and Dynamic Conditions. Journal of Materials Engineering and Performance 2009;18:725.

[58] Furst SJ, Seelecke S. Modeling and experimental characterization of the stress, strain, and resistance of shape memory alloy actuator wires with controlled power input. Journal of Intelligent Material Systems and Structures 2012;23:1233.

[59] Yastrebov VA, Fischlschweiger M, Cailletaud G, Antretter T. The role of phase interface energy in martensitic transformations: A lattice Monte-Carlo simulation. Mechanics Research Communications 2014;56:37.

[60] Feng P, Sun Q. Experimental investigation on macroscopic domain formation and evolution in polycrystalline NiTi microtubing under mechanical force. Journal of the Mechanics and Physics of Solids 2006;54:1568.

[61] Thiebaud F, Collet M, Foltete E, Lexcellent C. Implementation of a multi-axial pseudoelastic model to predict the dynamic behavior of shape memory alloys. Smart Materials and Structures 2007;16:935.

[62] Favier D, Louche H, Schlosser P, Orgéas L, Vacher P, Debove L. Homogeneous and heterogeneous deformation mechanisms in an austenitic polycrystalline Ti-50.8at.% Ni thin tube under tension. Investigation via temperature and strain fields measurements. Acta Materialia 2007;55:5310.

[63] Hornbogen E, Heckmann A. Microstructure, frequency and localisation of pseudo-elastic fatigue strain in NiTi. Z. Metallkd. 2003;94:1062.

[64] Pieczyska EA, Gadaj SP, Nowacki WK, Tobushi H. Stress relaxation during superelastic behavior of TiNi shape memory alloy. International Journal of Applied Electromagnetics and Mechanics 2006;23:3.

[65] Kimiecik M, Jones JW and Daly S. Quantitative Studies of microstructural phase transformation in Nickel-Titanium. Materials Letters 2013;95:25.

![](./images/813124236926255105_4.jpg)

Fig. 1: Stress-strain characteristics of the TiNiCuCo film for different strain rates as indicated.
The strain-controlled cycle comprises six distinguishable stages I - VI as indicated. Loading
is stopped shortly before the end of the pseudoelastic plateau. The values of critical stress
for austentite - martensite and reverse transformation $\sigma^{AM}$ and $\sigma^{MA}$, respectively, are
indicated for the strain rate of $10^{-3}\ \text{s}^{-1}$.

![](./images/813124236926255105_5.jpg)

Fig. 2: Local strain and temperature distribution within a representative test area of 3 x 2
$mm^2$ of a TiNiCuCo film sample during (a) loading and (b) unloading along x-direction at a
strain rate of 0.02 $s^{-1}$.

![](./images/813124236926255105_6.jpg)

![](./images/813124236926255105_7.jpg)

Fig. 3: (a) 2D elastic energy landscape for plane stress $\Psi(\varepsilon_1,\varepsilon_1)$ at A-M equilibrium temperature in the principle strain coordinate frame, at a temperature where martensite is stable. The proposed transition path (white) for scalar strain $\varepsilon$ continuously connects the austenite $(\varepsilon=0)$ and martensite parabolae $(\varepsilon=\pm\varepsilon_T)$. Minima of A and M are indicated (here, only M₊ is taken into account for better visibility). (b) Gibbs free energy density $g(\sigma,\varepsilon,T)$ with parameters from Table 1, at a stress slightly above the A-M plateau. The minima of the elastically strained austenite and martensite ($\varepsilon=0.0065$ and 0.0225) agree with the experimental strain values in Fig. 1.

![](./images/813124236926255105_8.jpg)

Fig. 4: Strain map determined by DIC and profiles of martensite phase fraction (red: 1, blue: 0) in the central part of the sample at the strain rate of $\dot{\varepsilon}=10^{-3}$ s. Depending on the transformation strain tensor $\varepsilon_{T}$ (Eq. 14, Eq. 19) different tilt angles are obtained: Equal transversal y and z contraction leads to strain bands aligned by $55^{\circ}$ with respect to the tensile direction (left). Increasing the y component $\varepsilon_{T,22}$ reduces the band inclination angle down to $45^{\circ}$(center), decreasing $\varepsilon_{T,22}$ increases the angle up to $\sim90^{\circ}$(right).

![](./images/813124236926255105_9.jpg)

Fig. 5: Profiles of martensite phase fraction (red: 1, blue: 0) at subsequent time steps assuming a scatter of 12 MPa in the stress barrier (strain rate $\dot{\varepsilon}=10^{-3}$ s, parameters from Table 1). These profiles reveal the locations for nucleation, growth and vanishing of strain bands.

![](./images/813124236926255105_10.jpg)

Fig. 6: Simulated (blue) and experimental (black) stress-strain characteristics of the TiNiCuCo sample at different strain rates. The simulation parameters are listed in Table 1.

![](./images/813124236926255105_11.jpg)

Fig. 7: Macroscopic strain, macroscopic stress, sample temperature and martensite phase fraction (computed as sample area averages) in the center of a TiNiCuCo film sample during loading and unloading as function of time. The strain rate is $10^{-3}\ s^{-1}$ on the left, and $10^{-2}\ s^{-1}$ on the right side. Simulation data are given as solid line (blue), experimental data, where available, as dashed line (black). Black squares indicate time steps of the mesoscopic images in Fig.8.

![](./images/813124236926255105_12.jpg)

Fig. 8: Evolution of mesoscopic strain patterns in the TiNiCuCo film specimen during loading (left) and unloading (right) at different strain rates as indicated. Strain patterns inferred from simulated profiles of martensite phase fractions (red: 1, blue: 0) at the strain rate of $10^{-3}\ \text{s}^{-1}$ (a) and $10^{-2}\ \text{s}^{-1}$ (b). Experimental strain patterns determined by DIC of a representative test area of 2×3 mm for a strain rate of $0.02\ \text{s}^{-1}$ (c).

![](./images/813124236926255105_13.jpg)

Fig. 9: Simulated (left) and experimentally determined temperature profiles (right) in the TiNiCuCo film specimen upon loading and unloading for a strain rate $0.001\ \text{s}^{-1}$. The time steps compare to respective strain profiles in Fig. 8. (a): $\text{M}\rightarrow\text{A}$ transformation, (b): $\text{A}\rightarrow\text{M}$ transformation.