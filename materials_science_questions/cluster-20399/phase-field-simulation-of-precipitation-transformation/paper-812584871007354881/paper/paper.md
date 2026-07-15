Journal Pre-proof

A numerical model coupling phase transformation to predict
microstructure evolution and residual stress during quenching of 1045
steel

Ali Kouhi Esfahani, Mahdi Babaei, Saeid Sarrami-Foroushani

![](./images/812584871007354881_1.jpg)

PII:
S0378-4754(20)30244-5
DOI:
https://doi.org/10.1016/j.matcom.2020.07.016
Reference:
MATCOM 5087

To appear in:
Mathematics and Computers in Simulation

Received date: 15 September 2019
Revised date: 9 July 2020
Accepted date: 14 July 2020

Please cite this article as: A.K. Esfahani, M. Babaei and S. Sarrami-Foroushani, A numerical
model coupling phase transformation to predict microstructure evolution and residual stress
during quenching of 1045 steel, Mathematics and Computers in Simulation (2020), doi:
https://doi.org/10.1016/j.matcom.2020.07.016.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the
addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive
version of record. This version will undergo additional copyediting, typesetting and review before it
is published in its final form, but we are providing this version to give early visibility of the article.
Please note that, during the production process, errors may be discovered which could affect the
content, and all legal disclaimers that apply to the journal pertain.

© 2020 International Association for Mathematics and Computers in Simulation (IMACS).
Published by Elsevier B.V. All rights reserved.

# A numerical model coupling phase transformation to predict microstructure evolution and residual stress during quenching of 1045 steel

Ali Kouhi Esfahani$^\mathrm{a}$, Mahdi Babaei$^\mathrm{b}$, Saeid Sarrami-Foroushani$^{\mathrm{c}*}$

a. Department of Materials Engineering, Isfahan University of Technology, Isfahan 84156-83111, Iran

b. School of Metallurgy and Materials Engineering, College of Engineering, University of Tehran, Tehran, Iran

c. Department of Civil Engineering, Isfahan University of Technology, Isfahan 84156-83111, Iran

Submitted to:
Mathematics and Computers in Simulation

---
* Corresponding author; Department of Civil Engineering, Isfahan University of Technology, Isfahan, 84157-83111. Tel.: +98 31 33913816. Fax: +98 31 33912700.
E-mail address: sarrami@cc.iut.ac.ir (S. Sarrami)

### Abstract

This article deals with the numerical simulation of quenching in low alloy steels based on finite element method adapting the effect of stress on the martensitic transformation to predict temperature history, microstructure evolution, and internal stresses. By superimposing the cooling curves of selected points on the CCT diagram of 1045 steel, verification of the simulated microstructures in the cylindrical specimen are carried out by comparing it with the micrographs of microstructures. Afterward, steel gears are treated in two cooling mediums to predict volume changes of gear samples quenched in oil and water. A comparison of the experimental results with those of numerical simulation generates an overall good agreement and indicates the well-demonstrated predictive capability of the model associated with kinetics of phase transformation, thermo-physical properties, and latent heat release for real-time quenching applications.

Keywords: Finite element method; Steel; Quenching; Residual stress; Phase transformation.

### 1. Introduction

Final microstructure and mechanical properties of steel during quench hardening are subject to distortion, cracking, and undesired distribution of microstructures and residual stresses, which denotes the prediction and simulation of the quenching state as a vital process in order to obtain the most desirable properties.

For the kinetics modeling of diffusive transformations, most researchers have applied the Johnson-Mehl equation [1] coupled with the numerical model known as Scheil's Additivity Rule [2]. The Scheil additivity rule, which was later improved by Avrami [3], considers the non-isothermal nature of austenite decomposition to meet the applicability of the Johnson-Mehl kinetics equation under non-isothermal conditions. Grong and Shercliff [4] began early attempts on developing finite element numerical model to study the microstructural changes resulting from austenite decomposition during continuous cooling. The state variable approach gives a powerful numerical framework to extend the simulation to non-isothermal conditions. Nonetheless, they reviewed a numerical approach in microstructure evolution, which accentuates only on thermal aspects, neglecting the thermal-mechanical coupling effect.

Variations of temperature in the component provide the driving force for phase transformation, the rate of which depends on cooling rate, and latent heat released during phase transformation altering the thermal field. On the other hand, the fluctuating internal stress field is continuously generated due to thermal and phase transformations strains. Transformations may be induced or totally inhibited by stress. This concept is generally referred as stress induced/inhibited phase transformation (SIPT). Silva et al. [5] employed FEM to study phase transformation effect on residual stress generated by quenching in notched steel cylinders. Thermal stresses in water quenched stainless steel spheres and geometric distortion in cut cylinders and end-quenched

cylinders were subjects of some researchers [6, 7]. Oliveira et al. [8, 9] investigated the effect of stress concentrations in phase distributions and residual stresses using a developed multiphase constitutive model allowing the analysis of the geometric influence. Simsir et al. [10] developed a FEM capable of prediction of distortion and residual stress state after quenching of asymmetric 3D components.

Lusk et al. [11] correlated differential shape change with the differential microstructural change. They obtained kinetic parameters for a variable model of austenite decomposition using a new forward fitting algorithm based on the estimation of shape change using each phase lattice parameters. To improve the accuracy of the decomposition simulation, Lee et al. [6, 12] modeled austenite decomposition kinetics using a set of equations made to modify the transformation model. Jung et al. [13] proposed a cooling-rate-dependent martensitic transformation kinetics model using the relationship between variable $M_s$, the C content in residual austenite, and the ferrite and bainite fractions. Pietrzyk and Kuziak [14] developed finite element simulations by incorporating the appropriate models in order to investigate the kinetics of austenite transformations based on dilatometry results of Jominy end quench tests.

Woodard et al. [15] established a correlation between the microstructure evolutions with thermal properties. They developed a 2D finite element algorithm for simulating the quenching process of cylindrical sample considering the dependence of phase change on latent heat. It was deduced that both the onset of transformation and the amount of product phases along the radius of the cylinder was dependent on latent heat. Since the coefficient of the heat equation is nonlinearly embedded in the kinetics of phase transformation via physical properties of each individual phase as well as the generation of latent heat, a small variation in temperature leads to sensible variation in phase distribution. Although they fundamentally investigated the effect of latent heat, their study lacks

some mandatory experimental tests to verify results except hardness measurements.

Kang and Im [16, 17] improved Woodard approach for investigating the dimensional change resulting from the phase transformation and temperature variation by studying the effect of the transformation-induced plasticity (TRIP). They considered the mutual relation between applied stress and generation rate of each phase volume fraction, even below yield strength. Their article disregards reporting the volume phase fraction and stress distribution over the entire quenching time. Furthermore, their algorithm ignores modeling bainite transformation and pearlite formation.

Ju et al. [18] used FEM to model martensitic transformation plasticity considering the influence of thermal stress on deformation due to transformation plasticity.

Although numerous works have been conducted on the modeling of phase transformation in the quenching process, there are only a few FEM studies of the stress-dependent non-diffusional austenite-martensite transformation in the literature [18]. The Koistinen and Marburger [19] equation is employed in most simulation studies to predict martensite fraction after quenching despite its restrictions for carbon steels. Instead, the evolution of martensite during quenching of a multiphase steel is predicted using a kinetic model, which takes into account the effect of stress on non-diffusional austenite to martensite transformation. According to modified Magee's rule [20], the non-diffusional transformation of austenite-martensite is governed by carbon content, temperature, and stress state.

In this study, the finite element simulation was implemented based on acquired temperature-dependent equilibrium volume fraction of ferrite as well as stress-dependent martensitic transformation to numerically investigate microstructure evolution and its instant effect on residual stress and distortion during the continuous cooling condition. In order to account for the decrease of volume fraction of ferrite with a decline in the transformation temperature under $A_{C1}$, the

equilibrium volume fraction of pro-eutectoid ferrite was calculated by extension of $A_{CM}$ equilibrium phase boundary of Fe-Fe₃C diagram to lower temperatures. In terms of microstructural evolution, the starting temperature of diffusional transformations was treated with additivity rule as non-isothermal condition occurring during quenching. Furthermore, by introducing virtual time, the volume fraction of each phase was accumulated over time so that the onset and the location of initiating of each individual phase, and particularly bainite, was manifestly predicted. The simulation of temperature gradients, volume fraction of each phase, stress variation, and dimensional changes of the cylindrical hypo-eutectoid 1045 steel samples in a quenching process using the finite element model was verified with experimentally measured values. Accordingly, the developed model was used for quenching simulation of industrial gear sample in oil and water as two different cooling mediums.

## 2. Mathematical model of microstructure

### 2.1. Diffusional transformation

To predict the volume fraction of microstructural phases of ferrite, bainite and pearlite generated during the quenching process, diffusional transformation models should be derived. In isothermal condition, the kinetics of diffusional transformation is expressed with regard to the Johnson-Mehl-Avrami-Kolmogorov (JMAK) model, as follows:

$$
F_{i}^{j}(T)=1.0-\exp \left[-b(T). t_{j}^{n(T)}\right] \tag{1}
$$

where $F_{i}^{j}$ represents the volume fraction of the $i$th product in the $j$th time step, $t$ is passed time since the onset of the transformation, $b$ and $n$ are material parameters calculated from TTT diagram of the desired material. The $b$ and $n$ parameters are computed as

$$
b(T)=-\frac{\ln \left(1-F_{s}\right)}{t_{s}^{n}(T)}
$$

$$
n(T)=\frac{\ln \left(\frac{\ln \left(1-F_{s}\right)}{\ln \left(1-F_{f}\right)}\right)}{\ln \left(\frac{t_{s}(T)}{t_{f}(T)}\right)}
$$

where $t_{s}$ is the time when the transformation is started at a specific temperature and $t_{f}$ is the time when the transformation is completed. $t_{s}$ and $t_{f}$, which are temperature dependent, are obtained from TTT diagram of 1045 steel for arbitrary temperatures. $F_{s}$ and $F_{f}$ are the accumulated volume fraction of the transformed phase at the start and finish of the transformation. In the present research $F_{s}$ and $F_{f}$ are considered 0.1 and 0.99, respectively [21]. During the quenching process, continuous cooling occurred while Eq.1 is only valid for the isothermal condition. Considering the additivity rule [22, 23], calculations could be extended to non-isothermal condition. The cooling curve is treated by division to series of small time steps depicted in Fig. 1(a).

![](./images/812584871007354881_2.jpg)

Fig 1. (a) Schematic of additivity rule, (b) virtual time.

An isothermal condition is assumed for each time step and accumulated volume fraction of

transformed phase is computed by JMAK equation and additivity rule. At the end of each time step (j), transformed fraction calculated by JMAK equation is obtained and for the next time step (j+1), JMAK equation for the new temperature gives a new relation $F_{i}(t, T_{j+1})$. Introducing a virtual time, $\theta_{j}$, for which $F_{i}(\theta_{j}, T^{j+1})=F_{i}^{j}$ is shown in Fig. 1(b), new transformed fraction for the (j+1)th step could be calculated as follows:

$$
F_{i}^{j+1}=F_{i}\left(\theta_{j}+\Delta t_{j}, T^{j+1}\right) \tag{3}
$$

The virtual time step is computed as

$$
\theta_{j}=\left[-\frac{\ln \left(1-F_{i}^{j-1}\right)}{b}\right]^{1 / n} \tag{4}
$$

with regard to additivity rule, diffusional transformation is assumed to begin when accumulation fraction reaches 1.0 as following:

$$
\sum \frac{\Delta t_{j}}{t_{i n c}\left(T^{j}\right)}=1 \tag{5}
$$

where $\Delta t_{j}$ and $t_{i n c}$ represent respectively $j^{\text {th }}$ time step and transformation incubation time at the temperature $T^{j}$.

### 2.2 Non-diffusional transformation

Regarding the non-diffusional transformation, Koistinen and Marburger [19] developed an equation only considering temperatures below $\mathrm{M}_{\mathrm{s}}$. In other words, the calculation of the martensite transformation increment exclusively adopts temperature replacement. Magee [20] adopted a different approach, known as Magee's rule, to take the effect of stress on non-diffusional transformation into consideration. In this regard, the martensite volume fraction is a function of both the temperature and stress state as following:

$$
\xi_{M}=1-\exp \left[\varphi\left(T-M_{s}\right)-\psi\left(\sigma_{i j}\right)\right] \tag{6}
$$

where the material constant, $\varphi$, is that martensite generates as temperature changes from martensite start temperature, $M_s$, and

$$
\begin{aligned}
& \psi\left(\sigma_{i j}\right)=A \sigma_{m}+B J_{2}^{1 / 2} \\
& J_{2}=\frac{1}{2} s_{i j} s_{i j}
\end{aligned}
\tag{7}
$$

in which the first term represents the effect of mean stress, $\sigma_{m}(=\sigma_{k k} / 3)$, and the latter is the deviatory stress. $A$ and $B$ are the constants which are experimentally measured by Onodera et al. [24].

### 2.3 Volume fraction of ferrite

When a multiphase steel is subject of the phase transformation modeling, the JMAK equation based on the total fraction of unity requires actual fractions. Phadke and Jutta et al. [25, 26] have computed the maximum amount of austenite transformable to pro-eutectoid ferrite employing the well-known lever rule in the case of hypo-eutectoid zone of the Fe-Fe₃C phase diagram. The consequent volume fraction of ferrite is near $V_{Feq}$ and mainly constant in various cooling rates. This approach is against the fact inferred form metallographic analysis, CCT diagrams, and also experimental tests in isothermal condition for hypo-eutectic steels showing that whole volume fraction of ferrite decrease with decline in transformation temperature under $A_{e1}$ [27]. The prediction of microstructure from phase diagrams are limited to equilibrium conditions, i.e. very slow cooling. Non-equilibrium cooling will result in different microstructures with altered properties.

Lee et al. [12] deems this procedure defective in hypo-eutectoid steels since the total volume fraction of ferrite decreases with a decline in transformation temperature under $A_{C1}$. Reti et al. [28] suggests another approach to determine the amount of pro-eutectoid ferrite under the $A_1$ temperature by an extended line of equilibrium phase boundary of austenite and

austenite/cementite or the $A_{CM}$ temperature curve. Fig. 2 depicts volume fraction of pro-eutectoid ferrite for 1045 steel as a function of temperature both above and below the Ael temperature.

![](./images/812584871007354881_3.jpg)

Fig. 2 volume fraction of pro-eutectoid ferrite for 1045 steel as a function of temperature both above and below the Ael temperature

### 2.4 Hardness prediction

The microstructure variation of the steel affects actual hardness, which is generally expressed with linear combination of all phase's hardness as

$$
\phi=\sum_{I=1}^{N} \xi_{I} H V_{I} \tag{8}
$$

where $\xi_{I}$ and $H V_{I}$ are the volume fraction and hardness of the $I^{\text {th }}$ phase, respectively. In accordance with studies of Maynier et al. [29], which were conducted by experimental tests in various types of alloy steel, the hardness of each phase could be measured based on constituting elements of desired alloy steel.

## 3. Thermo-elastic-plastic constitutive equation

Inhomogeneous temperature gradients result in non-uniform transformations of which the kinetics

vary locally in the domain. Since each point of the domain has its own temperature gradient, a non-uniform thermal strain distribution, results in stress distribution. In addition, each transformation has a specific dimension change. Thus, the intricate stress state is the inevitable result of concurrent non-uniform temperature distribution and inhomogeneous transformations occurring. Moreover, such stresses usually surpass the initial yield stress, necessitating an elastoplastic analysis coupled with temperature-dependent material. Fig. 3 depicts the coupling effects of temperature, stress/strain, and microstructure during the continuous cooling of steels.

![](./images/812584871007354881_4.jpg)

Fig. 3 The coupling effects of temperature, stress/strain, and microstructure in heat treatment

Concerning thermo-mechanical constitutive equation coupled with phase transformation kinetics, yield surface is a function of not only plastic strain but also temperature. In this study, the yield surface is expanded and shifted simultaneously in stress space and represented as:

$$
d F=\frac{\partial F}{\partial \sigma_{i j}} d \sigma_{i j}+\frac{\partial F}{\partial \alpha_{i j}} d \alpha_{i j}+\frac{\partial F}{\partial k} d k \tag{9}
$$

where $\alpha_{i j}$ and $k$ denote for transition and expansion of the yield surface, respectively. After the definition of yield function, flow rule and hardening rule, a constitutive law is set in the form of stress increment [16]:

$$
d \sigma_{i j}=C_{i j k l}^{e p}\left(d \varepsilon_{k l}-d \varepsilon_{k l}^{t h}-d \varepsilon_{k l}^{t r}-d \varepsilon_{k l}^{t p}\right)+d M_{i j}
\tag{10}
$$

where $d \varepsilon_{k l}, d \varepsilon_{k l}^{t h}, d \varepsilon_{k l}^{p h}, d \varepsilon_{k l}^{t p}$ represent elastic, thermal, phase transformation and transformation induced plasticity strain, respectively. The elasto-plasticity matrix $C_{i j k l}^{e p}$ and the vector $d M_{i j}$ are expressed as:

$$
\begin{aligned}
C_{i j k l}^{e p} & =C_{i j k l}^{e}-\frac{C_{i j k l}^{e} a_{i j} a_{k l} C_{i j k l}^{e}}{L}, \\
d M_{i j} & =\left(s_{i j}-\frac{C_{i j k l}^{e} a_{k l} s_{i j} a_{i j}}{L}\right) \frac{d \mu}{\mu}+\frac{C_{i j k l}^{e} a_{k l}}{L}\left(\frac{\partial \sigma_{Y_{0}}}{\partial T}+(1-\gamma) \bar{\varepsilon}^{p} \frac{\partial H}{\partial T}\right) d T+\frac{\sigma_{k k}}{3} \frac{d K}{K} \delta_{i j}
\end{aligned}
\tag{11}
$$

where $\delta_{i j}, K$ and $\mu$ are Kronecker delta, bulk modulus, and Lame's constant, respectively. Also, $\gamma$ expresses mixed hardening parameter with the range of $0 \leq \gamma \leq 1$. $\sigma_{Y_{0}}$ and $\bar{\varepsilon}_{p}$ indicate initial yield strength and effective plastic strain, respectively. $a_{i j}$ and $L$ are also defined as:

$$
a_{i j}=\frac{3}{2 \sigma_{Y}}\left(s_{i j}-\alpha_{i j}\right), \quad L=H+a_{i j} C_{i j k l}^{e} a_{k l}
\tag{12}
$$

where $C_{i j k l}^{e}$ and $H$ stand for elastic matrix and stress-hardening parameter, respectively. Eq. (10) represents thermo-elastic-plastic constitutive equation coupling microstructure evolution. In order to simulate temperature variation, phase distribution, and volume change during the continuous cooling process, a finite element program coupled with the kinetics of transformation is developed.

## 4. Finite element formulation

In this study, the convection boundary condition is considered on the outer surface, and the initial temperature of the sample sets the beginning condition for the quenching process. Thus, the austenitization temperature of desired steel, $T_{0}$, is set as the uniform initial temperature of the sample as following:

$$
\begin{aligned}
\left.T\right|_{t=0} & =T_{0} \\
f_{n} & =-h_{C}\left(T_{S}-T_{A}\right)
\end{aligned}
\tag{13}
$$

where $h_{C}$ is the heat convection coefficient, $T_{S}$ and $T_{A}$ denote surface temperature and ambient temperature on the transition surface with unit normal $n$, respectively. Fig. 4 shows the dependence of the heat convection coefficient, which is used in this study [30]. Heat convection coefficients of water and oil in Fig. 4 were obtained by employing AISI 304 stainless steel, which would guarantee no generated additional latent heat by phase transformation in its calculation.

![](./images/812584871007354881_5.jpg)

Fig. 4 Dependence of heat convection coefficient to the temperature.

As heat analysis is accompanied with transformation kinetics, heat equation coefficients vary with each phase fraction and temperature. In order to deal with such multiphase material, mixture rule was employed to calculate thermal coefficients during continuous cooling as follows:

$$
\begin{aligned}
k & =\sum F_{i} k_{i} \\
C_{p} & =\sum F_{i} C_{p i}
\end{aligned}
\tag{14}
$$

where $k_{i}, C_{p i}, F_{i}$ denote thermal conductivity, specific heat and volume fraction of the $i$th phase, respectively. For modeling the decomposition of austenite in a 1045 steel, it is necessary to acquire

various physical properties as functions of temperature. Fig. 5 shows thermo-physical properties of various phases in AISI 1045 steel [15]. It is assumed that the thermo-physical coefficients of diffusional products, which are ferrite, pearlite and bainite, are equivalent and specific heat of austenite and martensite at lower temperatures are extrapolated of those of austenite at higher temperatures.

![](./images/812584871007354881_6.jpg)

Fig 5. Thermo-physical properties of various phases in 1045 steel (a) thermal conductivity (b) specific heat.

In addition, the generated heat rising from phase transformation is deemed as an internal heat origin in transient heat analysis and is computed as

$$
\dot{q}=\sum \Delta H_{i} \frac{\Delta F_{i}}{\Delta t} \tag{15}
$$

where $\Delta H_{i}$ denotes the amount of heat generation at temperature $T_{i}$ and $\Delta F_{i}$ represents the quantity of phase transformation occurring in each individual interval time step. The heat generated due to diffusional phase transformations was calculated from the equations proposed by Darken and Gurry [31]. Furthermore, the generated latent heat due to bainite transformation is similar to that of pearlite transformation.

Based on the principle of virtual work, the matrix form of the heat equation after finite element discretization is obtained as

$$
[P]\{\dot{T}\}+[K]\{T\}=\{Q\}+\{R\} \tag{16}
$$

where

$$
\begin{aligned}
{[P] } & =\int_{V}\left[N^{T}\right][N] \rho C_{p} d V \\
{[K] } & =\int_{V}\left[B^{T}\right] k[B] d V \\
\{Q\} & =\int_{S_{E}}\left[N^{T}\right] h_{A}\left(T_{S}-T_{A}\right) d S \\
\{R\} & =\int_{V}\left[N^{T}\right] \dot{q} d V=\int_{V} \sum\left[N^{T}\right] \Delta H_{i} \frac{\partial F_{i}}{\partial t} d V .
\end{aligned} \tag{17}
$$

where $[B]$ is matrix filled with a gradient of shape function$[N]$.

In terms of mechanical formulation, based on the infinitesimal theory of strain as well as the principle of virtual work, the governing equation could be obtained as

$$
[K]\{U\}=\{R\} \tag{18}
$$

where

$$
[K]=\int_{V}[B]^{T}\left[C^{e p}\right][B] d V \tag{19}
$$

$$
R=\int_{V}\left[B^{T}\right]\left[C^{e p}\right]\left(d \varepsilon^{t h}+d \varepsilon^{p h}+d \varepsilon^{t p}\right) d V-\int_{V}\left[B^{T}\right][M] d V
$$

In this work, the Newton–Raphson iteration method was employed and the overall procedure is summarized in Figs. 6a. and 6b.

![](./images/812584871007354881_7.jpg)

(1) Compute the displacement increments in the time step t in $i_{th}$ iteration
$$^t du_i = {^t K_i^{-1}} {^t R_i}$$
For first iteration, i=1
$$^t R_i = {^t R_i} + {^t \psi}$$
For subsequent iterations
$$^t R_i = {^t \psi_i}$$

(2) Compute the total displacement and stress
$$^t u_i = {^t u_{i-1}} + {^t du_i}$$
$$^t \sigma_i = {^t \sigma_{i-1}} + {^t d\sigma_i}$$

(3) Evaluate the residual force
$$^t \psi_i = {^t dR_i} - \int_V B^T {^t \sigma_i}dV$$

(4) Check the tolerance
$$\frac{\left\| {^t \psi_i} \right\|}{\left\| {^t dR_i} \right\|} \leq \varepsilon$$

If the convergence has been reached, then go to step (5)
If not, set $^t \psi_i = {^t dR_i}$ , then go to step (1)

(5) If convergence has been reached, consider
$$^t u = {^t u_i}, {^t \sigma} = {^t \sigma_i}, {^t \psi} = {^t \psi_i}$$
And the load vector for the next step becomes
$$^{t+\Delta t} dR_i = {^{t+\Delta t} dR_i} + {^t \psi}$$
And repeat the same procedure form step (1) to step (5)

(b)

Fig. 6 (a) Thermo-mechanical algorithm coupled with microstructure evolution and (b) Newton-Raphson algorithm for obtaining solution.

## 5. Model Validation

To validate the simulation results and comparison of the predicted cooling rates with the experimental data, a cylindrical 1045 steel sample with dimensions of 100 mm in length and 50 mm in diameter was subjected to quenching treatment. A 2D axial symmetrical modeling is conducted to simulate the cylindrical 1045 steel sample. The mesh generation is depicted in Fig. 7. The austenitization process prior to quenching was conducted in an electric furnace at 840 °C

and the temperature of the quenching media was 25 °C. The simulation model provides the prediction of the cooling curve superimposed on the CCT diagram, volume fraction variation over time, hardness distribution, residual and von Mises stresses. Metallographic and hardness tests were undertaken to validate the predicted results. The preparation of samples was implemented by the standard metallographic grinding procedure followed by chemical etching with a solution of Nital 3%. The percentage of the phases was estimated with the aid of routines programmed into the metallographic image analysis software. This tool allowed quantifying the area of metallographic mosaics based on the color and morphology. Furthermore, Vickers microhardness tests were made subsequently on various regions in the samples with a load and dwell time of 4.9 N and 10 s, respectively. Finally, for further verification, a steel gear specimen was undergone quenching treatment in oil and water as a quenching medium with different quenching severity, and the predicted results obtained from the developed model were compared to the experimental data. The temperature values were recorded using thermocouples that were placed at gear core and surface. The data acquisition system was used to collect the monitored temperatures by thermocouples at each time during the cooling of the specimen.

![](./images/812584871007354881_8.jpg)

Fig. 7 The mesh generation used to simulate the quenching of cylindrical 1045 steel sample.

## 6. Results and Discussion

### 6.1 Cylindrical specimen

Fig. 8 shows the predicted cooling curves superimposed on the CCT diagram and the optical microstructures from different locations along the radial direction of the cylindrical specimen after of quenching treatment. It is observed that the surface microstructure is completely martensite. The microstructure at 5 mm from surface shows mixture of pearlite with some ferrite while the center microstructure is composed of pearlite with even more ferrite. The formation of ferrite (white regions) and pearlite (dark areas) is evident in microstructures of near center regions of specimen. The verification of the simulated microstructure is made possible by comparing the micrographs of microstructures. The phase fractions were quantified using the image analysis of the optical micrographs and compared to calculated phase fractions of specimens in order to verify the finite element simulation.

![](./images/812584871007354881_9.jpg)

Fig. 8 Calculated cooling curves superimposed on the CCT diagram and microstructures from various locations along radial direction in 1045 steel specimen after quenching, (a) specimen surface, (b) 20 mm from specimen center, (c) specimen center. The inset of the images shows the processed areas of ferrite in green color with aid of image processing.

Fig. 9 represents the comparison between the measured phase fractions and simulated ones. The simulated phase fractions obtained by finite element simulation based on the module with phase transformation considerations agree well with and experimental data measured from microstructures using image analysis.

![](./images/812584871007354881_10.jpg)

Fig. 9 Measured and predicted phase fraction of ferrite and pearlite phase after the quenching (a) at 20 mm from the specimen center, (b) at the specimen center.

Fig. 10a reveals the predicted volume fractions of phases along the central radius of the cylindrical specimen at different quenching times. With increasing quenching time, the volume fractions of pearlite and ferrite increase towards the center because of decreasing cooling rate, while the martensite reaches its utmost amount at the surface due to the maximum cooling rate promoting the non-diffusional transformation. The volume fraction of pearlite reaches its maximum amount at 5 mm from the surface, corresponding to the maximum depth of martensite formation. The martensite as the dominant micro-constituent constitutes almost the entire microstructure of the

specimen surface with the highest cooling rate. With moving away from surface towards the core, the cooling rate drops, thereby promoting the diffusional transformation of austenite to other products. The bainite highest volume fraction is discernible at a distance of about 2.5 mm from the edge despite being marginal. As shown in Fig. 10b, despite the marginal decrease in retained austenite from 60 s to 200 s of the treatment, there is a stable trend in microstructure distribution over this period of treatment, assuring no significant additional transformation.

![](./images/812584871007354881_11.jpg)

Fig. 10 The predicted volume fraction of the microstructural constituents along the central radius of the cylindrical specimen at different quenching times (a) 5 s, (b) 20 s, (c) 60 s, (d) 200 s and (e) retained austenite at 60 and 200 s.

Regarding the volume fraction variation of constituents with time, after 20 seconds of the quenching process, there would be no further bainite noticeable. The simulation result after 20 s confirms the maximum amount of pearlite at about 5 mm from the specimen surface. As time goes by, ferrite and pearlite phases extend to the central region of the specimen reaching volume fractions of about 20 and 80%, respectively. The simulation results after 20 s show the highest amount of bainite in the near surface region of the specimen. The reason might be as follows: at the outermost point from center, the decomposition of austenite to martensite occurs almost completely due to high cooling rates; while at center points, the temperature is higher than the start temperature of bainite. Because of lower cooling rates, the austenite decomposition to ferrite and pearlite leaves no retained austenite left behind required for bainite transformation. The microstructural evolution after 200 s from start of the simulation shows the ferrite and pearlite in the whole specimen as dominant phases. After 200 s, the ultimate microstructure on the surface is comprised mainly of martensite and small fractions of retained austenite. In comparison the microstructure in the neighborhood of the center consists of combined phases of the ferrite, pearlite.

In order to investigate the stress state during continuous cooling of samples where various phase transformation occurring alter the sign of the stress, the mean stress which could manifest the stress sign is calculated as time passes by. Up until coinciding with CCT curve, the stresses present are only due to temperature gradient. The cooling curve of the surface exceeds the critical cooling curve evidencing the formation of martensite. During the transformation, the surface region tends to expand more than the center with a slower cooling curve and dominant phase transformation of austenite to pearlite. This will result in high compressive stresses in the center and tensile stresses in surface regions. Fig. 11 shows the radial, Z, theta, and mean stress over time for both surface

and center of the specimen. As can be seen, mean stress (sigma/3)

![](./images/812584871007354881_12.jpg)

Fig. 11 The (a) Radial, (b) Z, (c) theta, and (d) mean stress over time for both surface and center of the specimen.

With further cooling, the contraction of the center is impeded by the surface being martensitic and having reached room temperature earlier. This will result in high tensile stresses in the center and compressive stresses in surface regions. In addition, the latent heat generation during austenite-martensite and austenite-pearlite phase transformation spark a decrease in the compressive stress on the surface and increase in the tensile stress.

Fig. 12 shows the hardness profile obtained from the 1045 steel sample and hardness values calculated from the simulation as a function of distance from the center. The as-quenched hardness distribution is determined by applying the empirical formulas developed by Maynier et al. [29],

which takes into account the hardness of each phase. The quenching velocity and chemical composition are used to determine the hardness of each phase ($HV_l$ in Eq. (8)) while the phase fractions ($\xi_l$ in Eq. (8)) are needed to apply the mixture rule.

The constituent volume fraction in the microstructure forms the basis of the calculation. It appears that there is a good harmony between the empirical data and the predicted hardness values for the cylindrical 1045 steel specimen. It seems that the dramatic drop of the hardness value happens at the uttermost depth of martensite in the 5 mm from the specimen surface. In addition, a good correlation between the variation of martensite volume fraction with hardness could be confirmed. As depicted in the hardness distribution along the specimen radius, areas of high hardness are abundant in the upright edge of the cylinder cross section as compared to other surfaces since it contains martensite in deeper layers. The inconsistencies observed in some results might have several sources. Some errors may come from experimental procedures such as metallography and chemical analysis (hardness predictions). Another source of errors might be due to dissimilarities of the chemical composition and the primary austenite grain size of the specimens compared with those of samples used for developments of TTT diagram.

![](./images/812584871007354881_13.jpg)

Fig. 12 (a) hardness contour and (b) experimental and simulation hardness values as a function of distance from the center.

In order to evaluate the effect of phase transformation stress on the magnitude of stress, the effective stress which could represent the stress state with positive scaler value is calculated at the end of the cooling process. Fig. 13 illustrates the von Mises stress distribution in the 1045 steel specimen with and without considering phase transformation. As it appears, the range of stress distribution along the radius of the specimen would be more extensive when considering the phase transformation during quenching as compared to the case with the phase transformation ignored. In addition, it can be noticed from stress contour that, as long as the phase transformation is taken into account, the effective stress is maximum in the surface region of the specimen with the approximate amount of 1400 MPa. In case of phase transformation ignored, the maximum effective stress is limited to 420 MPa. When considering effective stresses below 420 MPa, the same trend of distribution in the stress contour could be noticed for both conditions. Therefore, the maximum effective stress in both case differs in the locations and range. The phase transformation consideration would take account of some parameters that can influence the simulated results of effective stress. The volume expansion resulted from phase transformation of austenite to other products may give rise to increased effective stress, and particularly the surface region having the highest stress level is involved with extensive austenite to martensite phase transformation delivering the most volume expansion. The inset of the Fig. 13 shows a more detailed distribution of the stress range up to 280 MPa illuminating the stress range between 205 MPa and 230 MPa as the most frequent stress values.

![](./images/812584871007354881_14.jpg)

Fig. 13 The von Mises stress distribution in the 1045 steel specimen (a) without considering phase transformation and (b) coupled with phase transformation.

The dimensional change of the cylinder during quenching treatment is depicted in Fig. 14. It is interesting that geometry change along diameter and length considerably decreased when the effect of phase transformation stress was considered. The inset of Fig. 14 shows the simulated deformed shape of the cylindrical specimen after quenching, representing the graphical calculated geometry change solved by finite element simulations.

![](./images/812584871007354881_15.jpg)

Fig. 14 The calculated dimension variation with time of quenching treatment. The inset of the image shows the comparison of deformed shapes after quenching of the cylindrical eutectoid steel with and without considering the phase transformation (PT).

Fig. 15 shows the comparison between measured dimensional change along diameter (red bar) and length (blue bar) of the cylindrical specimen during quenching with calculated ones. It can be observed the predicted result considering the phase transformation well matches with the experimental data, whereas the dimensional change was significantly overestimated when the effect of phase transformation was neglected. The pickling of the sample surface was conducted before measuring the dimensions to remove the oxide scale. However, the scale thickness is orders of magnitude lower than the overall dimension change to interfere with the obtained results.

![](./images/812584871007354881_16.jpg)

Fig. 15 Comparison between calculated dimensional values with measured ones after quenching in water (PT: Phase Transformation).

Fig. 16 shows the history of volume variation predicted from simulation coupled with phase transformation and without phase transformation consideration in the specimen. It can be inferred from comparison of two conditions that there is far less dip in volume during transformation for the case of calculation coupled with phase transformation kinetics than the calculation with phase transformation kinetics ignored. The reason is that the austenite structure, FCC is a closed packed one and hence smaller in volume than BCC (ferrite structure), BCT (martensite structure) or any orthorhombic structure (cementite structure); therefore, the volume increases with austenite transforming to pearlite and martensite. Accounting for phase transformation during volume calculation, volume expansion resulting from austenite transformation to other products would compensate for a major portion of volume contraction caused by linear thermal volume reduction. In other words, the time required for the same volume decrease for both calculations differs and actually is longer for the case of calculations embedding phase transformation kinetics than that required for calculations with phase transformation ignored.

![](./images/812584871007354881_17.jpg)

Fig. 16 The specimen volume variation history predicted from simulation coupled with and without phase transformation consideration.

In case of volume calculation when considering phase transformation there can be seen a discernible peak after 25 s of quenching process implicating a significant increase in volume. This volume rise, which is not seen in the case of volume calculation with phase transformation ignored, might be the result of great martensitic formation giving rise to exceptional austenite to martensite transformational volume expansion.

### 6.2 Industrial gear specimen

This section reports a simulation of quenching process of industrial steel gear in water and oil medium. Figs. 17a and 17b represent industrial steel gear and its finite element model, respectively. Due to symmetry, only 1/20 of the model has been considered in the simulation.

![](./images/812584871007354881_18.jpg)

Fig. 17 (a) The gear sample model and (b) the finite element model.

Fig. 18 depicts the simulated and experimentally measured cooling history of the specimens quenched in water and oil. As can be seen, the recorded cooling curves accorded well with the simulated cooling curves implying an acceptable consistency between the applied boundary conditions, thermo-physical properties, and heat generations due to phase transformations with actual conditions. It is also evidenced greater quenching severity of water as compared to oil. It is also worth noting that the latent heat generated during the austenite-pearlite transformation could result in a temperature increase, which is apparently observable as a marginal rise in the surface temperature curve. The slight incline in the temperature curve is more noticeable in oil quenched specimen as compared to water quenched one, which could be associated with the lower cooling rate leading to greater austenite to pearlite transformation.

![](./images/812584871007354881_19.jpg)

Fig. 18 Simulated and experimentally measured cooling history of the specimens quenched in (a) water and (b) oil.

Fig. 19 shows the predicted phase distribution in water and oil quenched steel gear. It can be observed that in oil quenched specimen, most of the microstructure is composed of pearlite leaving behind a little place for martensite, while in water quenched gear martensite constitutes almost all of the microstructure. Having shown pearlite as dominant microstructure in oil-quenched specimen, the predicted phase distribution approves what was noted as a cause of slight rise in the middle of temperature history. In case of water quenched specimen, negligible amount of evolved pearlite in the microstructure does not produce enough latent heat capable of causing a noticeable rise in the cooling curve.

![](./images/812584871007354881_20.jpg)

Fig. 19 Predicted phase distribution of (a) ferrite, (b) bainite, (c) pearlite, (d) martensite in the steel gear quenched in water and oil.

Fig. 20 illuminates simulated hardness distribution contour for both water and oil quenched samples. It is very clear to observe that water-quenched specimen comprising higher amount of martensite possesses greater hardness.

![](./images/812584871007354881_21.jpg)

Fig. 20 Simulated hardness distribution in water and oil quenched samples.

Fig. 21 shows the calculated and experimental distributions of hardness in water and oil quenched specimens. Despite some minor inconsistencies observed in some locations, the predicted phase distribution generates a reasonable agreement with predicted hardness distribution addressing a reliable finite element model with well-demonstrated predictive capability for real-time quenching applications. The reason for discrepancies between experimental and simulation results might be due to the geometric influence of gearing since the volume to surface ratio controls the heat extraction significantly. Although considering the actual heat transfer coefficient of the hardening oil, no altering or kinetic effects due to the complex geometry of gearings are considered. Therefore, in the case of the oil quenched sample, there might be slight deviations in measured hardness from simulated ones. Also, Vickers hardness measurements are susceptible to uncertainties.

![](./images/812584871007354881_22.jpg)

Fig. 21 Comparison between the predicted and the measured distribution of hardness in the gear quenched in oil and water.

Fig. 22 illustrates predicted volume change of specimens during quenching in different mediums.

Because of the high quenching severity of water compared to oil, the volume of water quenched sample contracts more rapidly than oil quenched one. In both cases, some amount of expansion, which appears due to phase transformation in specimens during quenching, compensates some part of volume contraction occurred because of temperature drop. The marginal volume rises of two specimens occur in different temperature and time signifying distinctive phase transformations. In this regard, phase transformation of the specimens resulting in compensational volume expansion could be distinguished by exact specimen temperature and time of quenching process. The responsible phase transformation for volume rise occurs at higher temperature and longer time (10 s) for oil-quenched specimen contrasting rapid and low temperature phase transformation in water quenched one. The reason could be sought from phase distribution contour implying that majority

of the austenite transforms to martensite in the water-quenched specimen, while the resultant amount of martensite in the oil-quenched specimen is lower and the amounts of pearlite and bainite are higher than those in the water quenched one. The martensite as the dominant microstructure in water quenched specimen forms more rapidly at lower temperatures but the dominant pearlite and bainite in oil-quenched specimen will form at higher temperatures and longer times. Another noteworthy feature is the greater rise in volume for water quenching process than that for oil quenching one. The reason could be as follows: The martensite with BCT structure and austenite with FCC closed packed structure have the least and the most amount of density among other structures of products, respectively. As a result, considering greater expansion from austenite- martensite transformation than other phase transformations, the water-quenched specimen being more martensitic in microstructure will have greater expansion; consequently, a more noticeable rise in volume history in comparison with oil quenched one.

![](./images/812584871007354881_23.jpg)

Fig. 22 Predicted volume change during quenching in oil and water.

Continuing to study the volume curves with time reveals an intersection of the two curves after 25 seconds of quenching, indicating that phase transformation makes a great deal in volume variation

during quenching in different media. The intersection is caused by the extent of the volume expansion resulting from particular phase transformation occurred in two specimens quenched in oil and water. The water-quenched specimen will have nearly all of its microstructure comprised of martensite, which according to the simulation results, leads to a volume rise greater than that in oil-quenched specimen with dominant austenite to pearlite phase transformation. In this regard, the upcoming volume contraction will be counterbalanced by this volume rise to an extent that at the end of quenching the final volume will be the same as the volume at the beginning of phase transformational volume rise. This degree of volume rise is not observed for the oil-quenched specimen, letting thermal drop to continue volume contraction, and consequently, the final volume will be less than that of the water-quenched one.

### 7. Conclusions
This study investigated quench behavior of low alloy steels coupled with the temperature dependence of ferrite formation as well as the stress dependence of martensitic transformation. The phase transformation kinetic model predictions where the volume fraction of bainite calculated as a separate phase was incorporated with the finite element program greatly improved volume calculations and stress distribution predictions. The microstructure distribution profile over time revealed how the sign of the stress changes as the phase transformations takes place; tensile stress for the surface and compressive stress for the center at the beginning of the cooling are reversed at the end of the cooling. The importance of phase transformations consideration in the simulation was confirmed by more extended range of effective stress distribution, higher von Mises stress and far less volume dip in calculations embedded with phase transformation kinetics as compared to the regular calculations. Moreover, inferior decrease in diameter and length of the

cylindrical specimen were in good agreement with those of experimental results representing the capability of the implemented phase transformation model. In order to assess the capacity of the developed model for different mediums, the simulation was performed for mediums with different quenching severity. Quenching process of a steel gear in water and oil medium highlighted a high degree of martensite formation for water quenching compared to oil quenching where the pearlite formation is the dominant one. Due to different phase distributions as a result of different severity of the quenching medium, different hardness as well as volume change were seen for oil and water mediums. The simulation of quenching process of a steel gear in water and oil medium using finite element program generated an overall agreement in comparing the experimental cooling curves with the simulated cooling ones verifying the result of simulations and showing applicability of the model as a guideline in practical applications.

### References

[1] W. Johnson, R. Mehl, Reaction Kinetics in Processes of Nucleation and Growth, Transactions of AIME, 135 (1939) 416-458.

[2] S. Erich, Anlaufzeit der Austenitumwandlung, Archiv für das Eisenhüttenwesen, 8 (1935) 565-567.

[3] M. Avrami, Kinetics of Phase Change. II Transformation- Time Relations for Random Distribution of Nuclei, The Journal of Chemical Physics, 8 (1940) 212-224.

[4] Ø. Grong, H.R. Shercliff, Microstructural modelling in metals processing, Progress in Materials Science, 47 (2002) 163-282.

[5] E.P. Silva, P.M.C.L. Pacheco, M.A. Savi, On the thermo-mechanical coupling in austenite–martensite phase transformation related to the quenching process, International Journal of Solids and Structures, 41 (2004) 1139-1155.

[6] S.-J. Lee, Y.-K. Lee, Finite element simulation of quench distortion in a low-alloy steel incorporating transformation kinetics, Acta Materialia, 56 (2008) 1482-1490.

[7] S. Hossain, M.R. Daymond, C.E. Truman, D.J. Smith, Prediction and measurement of residual stresses in quenched stainless-steel spheres, Materials Science and Engineering: A, 373 (2004) 339-349.

[8] W.P. de Oliveira, M.A. Savi, P.M.C.L. Pacheco, Finite element method applied to the quenching of steel cylinders using a multi-phase constitutive model, Archive of Applied Mechanics, 83 (2013) 1013-1037.

[9] W.P. de Oliveira, M.A. Savi, P.M.C.L. Pacheco, L.F.G. de Souza, Thermomechanical analysis of steel cylinders quenching using a constitutive model with diffusional and non-diffusional phase transformations, Mechanics of Materials, 42 (2010) 31-43.

[10] C. Şimşir, C.H. Gür, 3D FEM simulation of steel quenching and investigation of the effect of asymmetric geometry on residual stress distribution, Journal of Materials Processing Technology, 207 (2008) 211-221.

[11] M. Lusk, W. Wang, X. Sun, Y.K. Lee, On the Role of Kinematics in Constructing Predictive Models of Austenite Decomposition, Materials Science and Technology 2003 Meeting, (2003) 311-331.

[12] S.-J. Lee, E.J. Pavlina, C.J. Van Tyne, Kinetics modeling of austenite decomposition for an end-quenched 1045 steel, Materials Science and Engineering: A, 527 (2010) 3186-3194.

[13] M. Jung, M. Kang, Y.-K. Lee, Finite-element simulation of quenching incorporating improved transformation kinetics in a plain medium-carbon steel, Acta Materialia, 60 (2012) 525-536.

[14] M. Pietrzyk, R. Kuziak, Computer aided interpretation of results of the Jominy test, Archives of Civil and Mechanical Engineering, 11 (2011) 707-722.

[15] P.R. Woodard, S. Chandrasekar, H.T.Y. Yang, Analysis of temperature and microstructure in the quenching of steel cylinders, Metallurgical and Materials Transactions B, 30 (1999) 815.

[16] S.-H. Kang, Y.-T. Im, Three-dimensional thermo-elastic-plastic finite element modeling of quenching process of plain-carbon steel in couple with phase transformation, International Journal of Mechanical Sciences, 49 (2007) 423-439.

[17] S.-H. Kang, Y.-T. Im, Finite element investigation of multi-phase transformation within carburized carbon steel, Journal of Materials Processing Technology, 183 (2007) 241-248.

[18] D.Y. Ju, W.M. Zhang, Y. Zhang, Modeling and experimental verification of martensitic transformation plastic behavior in carbon steel for quenching process, Materials Science and Engineering: A, 438-440 (2006) 246-250.

[19] D.P. Koistinen, R.E. Marburger, A general equation prescribing the extent of the austenite-martensite transformation in pure iron-carbon alloys and plain carbon steels, Acta Metallurgica, 7 (1959) 59-60.

[20] C.L. Magee, Nucleation of Martensite, American Society for Metals, (1968).

[21] P. Carlone, G.S. Palazzo, R. Pasquino, Finite element analysis of the steel quenching process: Temperature field and solid-solid phase change, Computers & Mathematics with Applications, 59 (2010) 585-594.

[22] Y. Zhang, H. Zhang, G. Wang, S. Hu, Application of mathematical model for microstructure and mechanical property of hot rolled wire rods, Applied Mathematical Modelling, 33 (2009) 1259-1269.

[23] S. Serajzadeh, Prediction of temperature distribution and phase transformation on the run-out table in the process of hot strip rolling, Applied Mathematical Modelling, 27 (2003) 861-875.

[24] H. Onodera, H. Gotoh, I. Tamura, Effect of Volume Change on Martensitic Transformation Induced by Tensile or Compressive Stress in Polycrystalline Iron Alloys, Japan Inst. Metals,, (1976) 327-332.

[25] S. Phadke, P. Pauskar, R. Shivpuri, Computational modeling of phase transformations and mechanical properties during the cooling of hot rolled rod, Journal of Materials Processing Technology, 150 (2004) 107-115.

[26] R. Jutta, J. Anders, Literature review of heat treatment simulations with respect to phase transformation, residual stresses and distortion, Scandinavian Journal of Metallurgy, 29 (2000) 47-62.

[27] E.B. Hawbolt, B. Chau, J.K. Brimacombe, Kinetics of austenite-ferrite and austenite-pearlite transformations in a 1025 carbon steel, Metallurgical Transactions A, 16 (1985) 565-578.

[28] T. Reti, Z. Fried, I. Felde, Computer simulation of steel quenching process using a multi-phase transformation model, Computational Materials Science, 22 (2001) 261-278.

[29] P. Maynier, J. Dollet, P. Bastien, Prediction of microstructure via empirical formulas based on CCT diagrams, Metallurgical Society AIME, (1978) 163-178.

[30] M.E. Kakhki, A. Kermanpur, M.A. Golozar, Numerical simulation of continuous cooling of a low alloy steel to predict microstructure and hardness, Modelling and Simulation in Materials Science and Engineering, 17 (2009) 045007.

[31] L.S. Darken, R.W. Gurry, Physical chemistry of metals, McGraw-Hill1953.

Figure captions

Fig. 1. (a) Schematic of additivity rule, (b) virtual time.

Fig. 2 volume fraction of ferrite at each temperature calculated using the extrapolated Fe-C phase boundaries.

Fig. 3 The coupling effects of temperature, stress/strain, and microstructure in heat treatment

Fig. 4 Dependence of heat convection coefficient to the temperature.

Fig. 5 Thermo-physical properties of various phases in 1045 steel (a) thermal conductivity (b) specific heat.

Fig. 6 (a) Thermo-mechanical algorithm coupled with microstructure evolution and (b) Newton-Raphson algorithm for obtaining solution.

Fig. 7 The mesh generation used to simulate the quenching of cylindrical 1045 steel specimen.

Fig. 8 Calculated cooling curves superimposed on the CCT diagram and microstructures from various locations in 1045 steel specimen after quenching, (a) specimen surface, (b) 20 mm from specimen center, (c) specimen center. The inset of the images shows the processed areas of ferrite in green color with aid of image processing.

Fig. 9 Measured and predicted phase fraction of ferrite and pearlite phase after the quenching (a) at 20 mm from specimen center, (b) at the specimen center.

Fig. 10 The predicted volume fraction of the microstructural constituents along the central radius of the cylindrical specimen at different quenching times (a) 5 s, (b) 20 s, (c) 60 s, (d) 200 s and (e) retained austenite at 60 and 200 s.

Fig. 11 The (a) Radial, (b) Z, (c) theta, and (d) mean stress over time for both surface and center of specimen.

Fig. 12 (a) hardness contour and (b) experimental and simulation hardness values as a function of

distance from center.

Fig. 13 The von Mises stress distribution in the 1045 steel specimen (a) without considering phase transformation and (b) coupled with phase transformation.

Fig. 14 The calculated dimension variation with time of quenching treatment. The inset of image shows the comparison of deformed shapes after quenching of the cylindrical eutectoid steel with and without considering the phase transformation (PT).

Fig. 15 Comparison between calculated dimensional values with measured ones after quenching in water (PT: Phase Transformation).

Fig. 16 The specimen volume variation history predicted from simulation coupled with and without phase transformation consideration

Fig. 17 (a) the gear sample model and (b) the finite element model.

Fig. 18 Simulated and experimentally measured cooling history of the specimens quenched in (a) water and (b) oil.

Fig. 19 Predicted phase distribution of (a) ferrite, (b) bainite, (c) pearlite, (d) martensite in the steel gear quenched in water, and oil.

Fig. 20 Simulated hardness distribution in water and oil quenched samples.

Fig. 21 Comparison between the predicted and the measured distribution of hardness in the gear quenched in oil and water.

Fig. 22 Predicted volume change during quenching in oil and water.