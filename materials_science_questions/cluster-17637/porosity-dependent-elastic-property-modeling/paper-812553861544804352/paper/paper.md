ORIGINAL PAPER

![](./images/812553861544804352_1.jpg)

# Numerical investigation on seismic behaviour of aged concrete gravity dams to near source and far source ground motions

Soumya Gorai¹ · Damodar Maity¹

Received: 3 September 2019 / Accepted: 25 September 2020
© Springer Nature B.V. 2020

## Abstract
This study presents a numerical investigation on the seismic behaviour of aged concrete gravity dams under near source and far source ground motions. Two-dimensional formulation of a concrete gravity dam is carried out implementing the finite element technique, considering full reservoir and rigid base condition. Degradation of concrete properties due to hydro-chemo-mechanical effects and the influence of sediment layers are taken into account to calculate the response of the dam-reservoir coupled system at different ages. Two near source and far source ground motions from real earthquake events are selected for time-history analysis. Seismic performance evaluation is also carried out to assess the probable damage level of the dam. The outcomes of this study show the variation of seismic response of the dam over the ages and the necessity of considering the aging effect, e.g. degradation of concrete and influence of sediment layers, in the inspection of seismic safety issues of concrete gravity dam. This study also reveals the critical effect of near source ground motions on concrete gravity dams at later ages.

Keywords Dam-reservoir system · Seismic analysis · Finite element method · Degradation of concrete · Influence of sediment depth · Near source and far source ground motions

## 1 Introduction
Ground motions, recorded in the proximity of an active fault (the range of upper limit of fault distance is 20–60 km), are generally considered as near source (or near fault) ground motions (Stewart et al. 2002; Li and Xie 2007). However, this definition does not reflect the main features of near source ground motions. The significant characteristic of near source ground motions is the long-period pulse(s), which appear prominently in velocity and/or displacement time history (Fig. 1a). These pulses are generally originated by “forward-directivity” (Bray and Rodriguez-Marek 2004) and “fling-step” (Yadav and Gupta 2017) effect. Whereas, far source (or far fault) ground motions do not

---

✉ Soumya Gorai
soumya.gorai@iitkgp.ac.in

¹ Department of Civil Engineering, Indian Institute of Technology Kharagpur, Kharagpur, West Bengal 721302, India

Published online: 14 October 2020

![](./images/812553861544804352_2.jpg)

![](./images/812553861544804352_3.jpg)
![](./images/812553861544804352_4.jpg)

**(a)** Gilroy #3, Gillroy Sewage Plant (near source)
**(b)** Gillroy #7, Mantelli Ranch (far source)

Fig. 1 Illustration of near source and far source ground motions recorded during Loma Prieta earthquake

exhibit such pulse-type characteristics (Fig. 1b). Near source ground motions exhibit high Peak Ground Velocity as compared to far source ground motions, and the ratio of PGV to PGA is larger than 0.1 s. Earthquake energy is mainly concentrated within one or more pulses in near source ground motions which arrive early of the event (Ertun-cay and Costa 2019) and thus cause significant destruction to the structures. Charac-terization of pulse-type ground motions (Mavroeidis and Papageorgiou 2003; Joshi et al. 2012; Mukhopadhyay and Gupta 2013a, b) and their effect on various structures (Sehhati et al. 2011; Adanur et al. 2012; Bhandari et al. 2018; Yang et al. 2019) has become a recent trend in the field of earthquake engineering of structures. Research-ers took interest in the seismic behaviour of concrete gravity dams to near source and far source ground motions since last decade. Near source ground motions have differ-ent outcomes on earthquake response of concrete gravity dams (Bayraktar et al. 2008). Maximum horizontal displacement and maximum tensile principal stress along the dam height are higher to near source ground motions than those of far source records (Bay-raktar et al. 2010). Near fault ground motions attributed by "forward-directivity" effect generally cause more damage to the dams as compared to "fling-step" pulse motions. However, different seismic response quantities of concrete gravity dams are sensitive to different ground motion parameters (Huang 2015). Seismic performance demands of the dam are considerably enhanced under near source ground motions because of their impulsive characteristics (Wang et al. 2014). However, near source ground motions recorded very near to fault plane show the unusual spectral shape and thus reduce the response of the dam. On the contrary, far source ground motions having a high spectral ratio in the period of dominant vibration modes of the dam-reservoir-foundation system, increase the response (Gorai and Maity 2019). Equivalent pulses extracted from pulse-type ground motions cannot capture the behaviour of concrete gravity dams properly, which signify that ground motion parameters other than pulse properties may govern the response of the dam (Yazdani and Alembagheri 2017a, b).

![](./images/812553861544804352_5.jpg)

Natural Hazards

Concrete gravity dams are built across the river to withstand the water to serve for flood control, electricity generation, water supply, irrigation, etc. Dams are constructed for a long design life (generally 100 years). However, the degradation of concrete occurs through its life span because of hydro-chemo-mechanical actions. Alkali Aggregate Reaction (AAR) and calcium leaching are the main chemical effects, occurred due to continuous exposure with reservoir water at the upstream side. The formation and growth of micro-cracks (mechanical effect) also decay the properties over the ages. On the other hand, concrete gains strength even after 28 days and it develops with time. Hence, degradation of properties and strength gain, both factors should be incorporated in order to assess the long-term behaviour of concrete gravity dams. Washa et al. (1989) reported the outcome from an experimental programme that has been carried out on cylindrical specimens to estimate the gain in compressive strength up to 50 years. Dolen (2005) addressed a field quality control programme, in which laboratory and field data are compared to predict the changes in concrete properties over the years. Kuhl et al. (2004a) developed a numerical model considering calcium leaching and mechanically induced damage to solve a one-dimensional boundary value problem and addressed the long-term behaviour of a macroscopic material. In a subsequent study (Kuhl et al. 2004b), the proposed model is incorporated to examine the response of the concrete beam under chemical action and mechanical loading. The chemical reaction between silica in aggregate and alkali in cement produces expansive gel which is the prime cause of concrete deterioration (Pan et al. 2013a). Pan et al. (2013a, b) implemented the chemo-damage model to numerically investigate the AAR strain in concrete which showed good agreement with experimental data. Pan et al. (2014) have also carried out a nonlinear analysis of concrete dams combining the concrete damage plasticity model, creep effect and AAR kinetics law. Gogoi and Maity (2007) proposed a relation to predict the degraded elastic modulus of concrete, based on the study of Washa et al. (1989) and further incorporated the degraded modulus of elasticity for numerical investigation of the seismic response of the aged dam-reservoir system. Long-term seismic behaviour of dam-foundation and dam-reservoir system have also been examined by Burman et al. (2011) and Mandal and Maity (2016), respectively. However, in these aforementioned studies, the degradation index representing the chemical effect is considered constant over time. Azizan et al. (2017) evaluated an empirical relation to predict the AAR strain and degraded elastic modulus and implemented that to inspect the behaviour of the aged dam. Sediments are deposited in the stagnant water of the reservoir, and sediment depth is increased over the years if not removed at frequent intervals by dredging. Sediment layers absorb pressure waves, and the damping caused by the escaping energy due to the radiation of incident acoustic waves at the reservoir bed reduces the response of the system (Hatami 1997; Gogoi and Maity 2007; Mandal 2016). Azizan et al. (2017) have not considered the interactive forces from the reservoir, and thus the effect of increasing sediment depth on the response of the dam-reservoir system is ignored. Thus, it is clearly understood that all of these previous studies have certain limitations. It is also worth mentioning that no other researchers have attempted to examine the behaviour of aged concrete gravity dams under near source and far source ground motions.

The main objective of this study is to evaluate the long-term response of the dam-reservoir system under near source and far source ground motions. Therefore, the work focuses on the consideration of all important aspects that affect the seismic behaviour of the dam-reservoir system in long term and comparison of seismic response of the dam-reservoir system to near source and far source earthquakes at later ages. A two-dimensional model of the dam-reservoir system is formulated using the finite element technique in the MATLAB framework. The concrete gravity dam is considered to be constructed on a hard

![](./images/812553861544804352_6.jpg)

rock foundation, and thus the foundation is assumed rigid in this study. Changes in properties of concrete are evaluated considering degradation due to AAR expansion, mechanical action and gain in compressive strength. The effect of increasing sediment depth is also considered to incorporate the consequence of the variation of hydrodynamic pressure to the response of the system. Two sets of ground motions are used as external excitation. First set represents near source ground motions and contains two ground motion records. The other set represents far source ground motions and contains two ground motions from the same earthquake events. Dynamic response of the dam-reservoir system is obtained at the age 1 year, 50 years and 75 years to different ground motions. A qualitative assessment of the probable damage level of the dam is also carried out at different ages under different ground motions.

## 2 Methodology

### 2.1 Numerical modelling of gravity dam-reservoir system

The structural system has been analysed considering 2D plane strain formulation. The dam domain is modelled implementing displacement-based Lagrangian formulation. The dynamic equilibrium equation of the dam domain can be expressed as

$$
\left[M_{d}\right]\{\ddot{x}(t)\}+\left[C_{d}\right]\{\dot{x}(t)\}+\left[K_{d}\right]\{x(t)\}=-\left[M_{d}\right]\left\{\ddot{x}_{g}(t)\right\} \tag{1}
$$

where $[M_d]$, $[C_d]$ and $[K_d]$ indicate mass, viscous damping and stiffness matrices of the dam, respectively. $\{x(t)\}$ represents the nodal unknown displacement, and an over dot denotes time derivative. $\{\ddot{x}_g(t)\}$ indicates the ground acceleration vector. The reservoir domain is formulated employing pressure based Eulerian formulation. Infinite extent of the reservoir is modelled introducing a local non-reflecting boundary condition (NRBC) at reservoir far end (Gogoi and Maity 2010). Absorption of longitudinal waves (Hatami 1997; Gogoi and Maity 2007; Khiavi 2016) at reservoir bottom due to the deposition of sedimentary material is also taken into account. The equation of motion of the reservoir, considering pressure as a nodal unknown variable, can be expressed as

$$
[E]\{\ddot{p}(t)\}+[A]\{\dot{p}(t)\}+[G]\{p(t)\}=-\left\{F_{r}(t)\right\} \tag{2}
$$

where the nodal unknown pressure of the reservoir domain is expressed as $\{p\}$. Expressions of the matrices $[E],[A]$, $[G]$ and force vector $F_r(t)$ can be found in the study of Gogoi and Maity (2006, 2007). The dam-reservoir coupled system is analysed using a direct-coupling methodology. The coupled equation of the dam-reservoir system is given as

$$
\left[\begin{array}{cc}
M_{d} & 0 \\
\rho_{f} Q^{T} & E
\end{array}\right]\left\{\begin{array}{l}
\ddot{x}(t) \\
\ddot{p}(t)
\end{array}\right\}+\left[\begin{array}{cc}
C_{d} & 0 \\
0 & A
\end{array}\right]\left\{\begin{array}{l}
\dot{x}(t) \\
\dot{p}(t)
\end{array}\right\}+\left[\begin{array}{cc}
K_{d} & -Q \\
0 & G
\end{array}\right]\left\{\begin{array}{l}
x(t) \\
p(t)
\end{array}\right\}=-\left\{\begin{array}{c}
M_{d} \ddot{x}_{g}(t) \\
F_{r}(t)
\end{array}\right\} \tag{3}
$$

where $[Q]$ indicates the coupling term between the pressure of the reservoir and displacement of the dam at the dam-reservoir interface. The formulation and solution technique of the fluid-structure coupled problem are described and implemented in several studies (Gogoi and Maity 2006; Mandal 2016; Mandal and Maity 2016), therefore not explained here in detail. As the non-reflecting boundary condition at the reservoir far end is frequency dependent, time-varying frequency content of earthquake signal is captured using the wavelet transform technique (Morlet et al. 1982a, b; Heidaria and Salajegheh 2009).

![](./images/812553861544804352_7.jpg)

Time-history analysis is carried out using Newmark's average acceleration ($\gamma = 0.5$ ,$\beta = 0.25$) method as a time-integration scheme.

The geometry of the non-overflow monolith of the Koyna dam, situated at Maharashtra, India, is considered for numerical application. It is established in previous studies (Gogoi and Maity 2006, 2010) that a reservoir truncation length of 0.2–0.5 times of reservoir depth, with an artificial NRBC at the reservoir far end, produces accurate results in comparison with infinite reservoir length. The reservoir length is truncated at a distance of 51.5 m which is 0.5 times the depth of reservoir water. The dam and reservoir domain are discretized using an 8-noded isoparametric element. An optimum meshing (nos. of elements) of the coupled system is finalized after a mesh convergence study. The geometry and finite element discretization of the system are shown in Fig. 2.

### 2.2 Evaluation of degradation of concrete

The degradation of concrete basically signifies the reduction in net area that supports the load acting on it. Compressive strength gain in concrete and deterioration of concrete occur simultaneously over the ages. Deterioration of concrete arises due to hydro-chemo-mechanical effects because of the continuous contact with reservoir water. The degradation parameter of concrete can be measured in terms of total porosity ($\psi$) (Kuhl et al. 2004a), which is equal to the sum of initial porosity ($\psi_0$), mechanical porosity ($\psi_\text{m}$) and chemical porosity ($\psi_\text{c}$). Hence, the porosity is defined as

$$
\psi = \psi_0 + \psi_\text{m} + \psi_\text{c} \tag{4}
$$

The mechanical porosity is caused by the formation and propagation of micro-cracks in concrete due to external loading and is defined as

$$
\psi_\text{m} = (1 - \psi_0 - \psi_\text{c})d_\text{m} \tag{5}
$$

The mechanical damage function $d_\text{m}$ is given as

$$
d_\text{m}(\kappa_\text{m}) = \alpha_s - \frac{\kappa_\text{m}^0}{\kappa_\text{m}}\left[1 - \alpha_\text{m} + \alpha_\text{m} e^{\left\{\beta_\text{m}\left(\kappa_\text{m}^0 - \kappa_\text{m}\right)\right\}}\right] \tag{6}
$$

where $\kappa_\text{m}^0$ and $\kappa_\text{m}$ represent initial damage threshold and internal variable describing the current damage threshold, respectively. $\alpha_m$ and $\beta_m$ are material parameters and derived

Fig. 2 Finite element mesh of Koyna gravity dam-reservoir system
![](./images/812553861544804352_8.jpg)

experimentally (Bangert et al. 2003). $\alpha_{\mathrm{s}}$ is taken as 1.0 which represents the maximum permissible mechanically induced degradation. One-dimensional boundary value problem is solved by Kuhl et al. (2004a) in which increasing equivalent strain measurement beyond $\kappa_{\mathrm{m}}^{0}$ is correlated with increasing mechanical damage $d_{\mathrm{m}}$. A detailed explanation of the parameters of the above expression and the solution procedure may be found in the study of Kuhl et al. (2004a) and Gogoi and Maity (2007). The chemical porosity, arising only from alkali-aggregate reaction (AAR), is given by

$$
\psi_{\mathrm{c}}=d_{\text {aar }} \tag{7}
$$

$d_{\text {aar }}$ represents the damage of the concrete because of volumetric expansion due to AAR. The chemical reaction in time depends on reactive temperature (Pan et al. 2013b). The AAR extent used to describe expansion evaluation is as follows (Pan et al. 2013a, b),

$$
\zeta(t, \mathrm{T})=\frac{1-\mathrm{e}^{-\frac{t}{\tau_{\mathrm{c}}(\mathrm{T})}}}{1+\mathrm{e}^{-\frac{t-\tau_{\mathrm{l}}(\mathrm{T})}{\tau_{\mathrm{c}}(\mathrm{T})}}} \tag{8}
$$

where $\tau_{\mathrm{c}}$ and $\tau_{\mathrm{l}}$ indicate the characteristics of time and latency time, respectively. So, the expansive gels, produced by the AAR effect, destroy the concrete matrix and cause stiffness degradation to the material. The AAR damage factor $\left(d_{\text {aar }}\right)$ is obtained from the AAR strain $\left(\varepsilon_{\text {aar }}\right)$ as

$$
d_{\text {aar }}=\frac{\varepsilon_{\text {aar }}}{\varepsilon_{\text {aar }}+0.003} \tag{9}
$$

Pan et al. (2013b) combined AAR kinetics with the plastic-damage model and applied it to the numerical investigation of AAR affected Kariba dam (Zimbabwe). The measured data of the dam were calibrated with numerical results, and an empirical relation is established by Azizan et al. (2017) from AAR data, which is given as

$$
\varepsilon_{\text {aar }}=0.00435 t^{1.1163} \tag{10}
$$

where $t$ indicates the age of concrete in years. The elastic modulus of degraded concrete can be obtained in terms of total porosity (by taking into account the initial porosity, mechanical porosity, chemical porosity) and gain in compressive strength from the expression (Gogoi and Maity 2007),

$$
E_{\mathrm{m}}=(1-\psi)^{\frac{t}{\tau_{a}}} E_{0} \tag{11}
$$

where $\tau_{a}$ is the design life. Un-degraded elastic modulus of concrete $\left(E_{0}\right)$ can be obtained from the relation,

$$
E_{0}=5000 \sqrt{f(t)} \tag{12}
$$

where $f(t)$ is the compressive strength at that particular age. Long-term test programmes on concrete had been conducted at the University of Wisconsin-Madison to determine the variation of compressive strength, transverse strength, secant and dynamic elastic modulus. The test results, obtained in a span of 50 years, are reported by Washa et al. (1989). A core testing programme was conducted on concrete dams of 50-100 years old by US Department of the Interior, Bureau of Reclamation to develop a database model for aging concrete (Dolen 2005). The outcomes of these programmes reveal the trend of compressive

![](./images/812553861544804352_9.jpg)

Natural Hazards

strength which is approximately proportional to the logarithm of the age. The relationship of age and the compressive strength of un-degraded concrete are established by Azizan et al. (2017) based on the experimental studies of Washa et al. (1989) and Dolen (2005) and are as follows:

$$f(t)=3.57 \ln (t)+44.33 \tag{13}$$
Washa et al. (1989) :

$$f(t)=1.51 \ln (t)+31.79 \tag{14}$$
Dolen (2005) :

Therefore, the value of total porosity and un-degraded elastic modulus at a particular age are put into Eq. (11) and degraded elastic modulus is obtained. Finally, the variation of elastic modulus of degraded concrete is obtained by Azizan et al. (2017) at different ages based on Eq. (11) and the authors proposed an empirical relation using the data which is as follows:

$$E_{\mathrm{m}}(t)=0.0175 t^{3}-3.4054 t^{2}+29.807 t+E_{i} \tag{15}$$

where $E_{i}$ is an initial value based on the studies of Washa et al. (1989) and Dolen (2005). The empirical relation is applicable for 1-100 years. The empirical relation for prediction of degraded elastic modulus of concrete is based on the following assumptions (Mandal 2017): (1) Design life of the dam is 100 years, (2) Degradation model is isotropic, and (3) Degradation of concrete strength of the gross section as a whole, which is the worst case. The procedure for establishing the empirical relation for prediction of degraded elastic modulus of concrete is described in the form of a flowchart in Fig. 3 and are also presented in detail in the study of Gogoi and Maity (2007), and Azizan et al. (2017). It is to be noted that Eqs. (13) and (14) represent the gain in compressive strength without any aging effect as those are obtained from the data of un-degraded concrete. The estimate of the tensile strength of degraded concrete is necessary as it is required for performance assessment. The variation of the tensile strength of concrete is considered the same as the changes in elastic modulus (Pan et al. 2014) and is given by

$$f_{t}=f_{t 0} \cdot\left(\frac{E_{\mathrm{m}}}{E_{t 0}}\right) \tag{16}$$

![](./images/812553861544804352_10.jpg)

Fig. 3 Procedure of evaluation of degradation of concrete properties

![](./images/812553861544804352_11.jpg)

where $f_{t0}$ and $E_{t0}$ is the initial tensile strength and elastic modulus of the concrete. $f_t$ is the tensile strength of degraded concrete. The initial tensile strength (Oluokun et al. 1991) is obtained from the following expression for normal-weight concrete,

$$
f_{t0}=0.294f_{c}^{0.69}. \tag{17}
$$

## 2.3 Variation of reflection coefficient

Sedimentary materials are deposited at the reservoir bottom due to the stagnant reservoir water. The presence of sediments at the reservoir bottom considerably alters the response of the reservoir because of the absorption of compression waves. The absorption of compression waves at the bottom of the reservoir can be expressed with the boundary condition (Khiavi 2016),

$$
\frac{\partial p}{\partial n}+q p+\rho_{f} a_{n}=0 \tag{18}
$$

where $n$ is the outward direction normal at the water-reservoir bottom interface, $a_n$ represents the normal component at the boundary and the coefficient $q=\frac{1}{c}\left(\frac{1-\alpha}{1+\alpha}\right)$. $\alpha$ is the wave reflection coefficient at the interface of two mediums and defined as the ratio of the amplitude of reflected pressure wave to the amplitude of vertically incident compression wave. It can be expressed in terms of acoustic impedance of the mediums and is as follows (Gogoi and Maity 2007),

$$
\alpha=\frac{1-c_{\mathrm{f}} \rho_{\mathrm{f}} / c_{\mathrm{s}} \rho_{\mathrm{s}}}{1+c_{\mathrm{f}} \rho_{\mathrm{f}} / c_{\mathrm{s}} \rho_{\mathrm{s}}} \tag{19}
$$

where $c_{\mathrm{f}}=$ velocity of a compression wave in water (1438.7 m/s), $c_{\mathrm{s}}=$ velocity of compression wave in sediment $(1500 \mathrm{~m} / \mathrm{s})=\sqrt{\frac{E_{\mathrm{s}}}{\rho_{\mathrm{s}}}}$, $\rho_{\mathrm{f}}=$ density of water $(1000 \mathrm{~kg} / \mathrm{m}^{3})$, and $\rho_{s}=$ mass density of sediment material $(2000 \mathrm{~kg} / \mathrm{m}^{3})$ (Hatami 1997). The equivalent reflection coefficient due to the sediment layer and underlying foundation strata can be obtained as

$$
\alpha_{e q}=\frac{\alpha_{1} d_{1}+\alpha_{2} d_{2}}{d_{1}+d_{2}} \tag{20}
$$

where $\alpha_{1}$ and $\alpha_{2}$ are the reflection coefficient of the sediment layer and underlying foundation strata, $d_{1}$ and $d_{2}$ are the thickness of the sediment layer and foundation strata, respectively. If the sedimentary materials are not flushed out at regular intervals, thickness of the sediment layer increases, and thus the value of the reflection coefficient also varies. The changes in the value of the reflection coefficient with ages are obtained considering a sedimentation rate 0.15 m/year and 0.3 m/year (Fig. 4). The elastic modulus and thickness of the foundation are considered as excessively large to represent a rigid foundation. The properties of water and sedimentary material are mentioned above. It is observed that the equivalent reflection coefficient is maximum (i.e. $\alpha=1$) at the time of impounding the reservoir water. The reflection coefficient is reduced with the increase in the thickness of the sediment layers in course of time.

![](./images/812553861544804352_12.jpg)

![](./images/812553861544804352_13.jpg)

## 3 Selection of ground motion records

Two sets of ground motion records from real earthquake events are selected from the ground motion database of Pacific Earthquake Engineering Research Center (https://ngawest2.berkeley.edu/). First set includes two near source ground motions and second set includes two far source ground motions from the same earthquake events (Table 1). The site to fault distance for the selected near source ground motions is less than 10 km. The selected ground motions exhibit the characteristics of near source and far source ground motions as described earlier. Koyna dam is situated in the seismic zone IV (Indian Standard 1893:2016). The zero period pseudo-spectral acceleration for seis- mic zone IV is 0.24 g. Hence, all the ground motions are normalized to the same PGA level of 0.24 g through amplitude scaling. Acceleration time histories of scaled ground motions are shown in Fig. 5. The velocity and displacement time histories of original ground motions are shown in Figs. 6 and 7, respectively.

## 4 Results and discussions

### 4.1 Validation of present formulation

The paper published by Samii and Lotfi (2007) is considered as a benchmark study on seismic analysis of the dam-reservoir system using the direct-coupling approach. Pine Flat Dam is considered as a numerical exercise in their study. Hence, the formulation of finite element modelling and the direct-coupling technique in this study are validated considering the numerical example of the Pine Flat Dam-reservoir system. Frequency- dependent non-reflecting boundary condition and absorption of acoustic waves at res- ervoir bed are discussed in detail in the study of Gogoi and Maity (2007, 2010), hence discussion on those aspects are not repeated here. The dimension of the dam-reservoir system (Fig. 8) and material properties (Table 2) are adopted from the study of Samii and Lotfi (2007). Free vibration analysis is carried out, and the first five natural frequen- cies of the dam-reservoir coupled system are obtained. The comparison of the results (Table 3) proves the correctness of the present formulation.

![](./images/812553861544804352_14.jpg)

<table><caption>Table 1 Parameters of selected near source and far source ground motions</caption>
<thead>
<tr>
<th>Earthquake</th>
<th>Sl. no</th>
<th>Ground motion type</th>
<th>Fault distance (km)</th>
<th>Station</th>
<th>$M_{w}$</th>
<th>PGA (m/s²)</th>
<th>PGV (m/s)</th>
<th>PGV/PGA (s)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Northridge</td>
<td>NF1*</td>
<td>Near source</td>
<td>7.1</td>
<td>Newhall—LA county fire station</td>
<td>6.7</td>
<td>5.78</td>
<td>0.95</td>
<td>0.16</td>
</tr>
<tr>
<td>FF1#</td>
<td>Far source</td>
<td>29.8</td>
<td>Lake Hughes</td>
<td>6.7</td>
<td>2.21</td>
<td>0.13</td>
<td>0.06</td>
</tr>
<tr>
<td rowspan="2">Imperial valley</td>
<td>NF2</td>
<td>Near source</td>
<td>7.0</td>
<td>El Centro Array #4</td>
<td>6.5</td>
<td>3.63</td>
<td>0.8</td>
<td>0.22</td>
</tr>
<tr>
<td>FF2</td>
<td>Far source</td>
<td>21.8</td>
<td>Superstation Mountain, CA</td>
<td>6.5</td>
<td>1.82</td>
<td>0.08</td>
<td>0.05</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9">*NF near fault, #FF far fault</td>
</tr>
</tfoot>
</table>

![](./images/812553861544804352_15.jpg)

![](./images/812553861544804352_16.jpg)

Fig. 5 Acceleration time histories of scaled ground motions

![](./images/812553861544804352_17.jpg)

Fig. 6 Velocity time histories of original ground motions

![](./images/812553861544804352_18.jpg)

Fig. 7 Displacement time histories of original ground motions

![](./images/812553861544804352_19.jpg)

Fig. 8 Pine Flat Dam-reservoir system adopted from the study by Samii and Lotfi (2007)

Table 2 Properties of concrete
and water for validation study
adopted from the study by Samii
and Lotfi (2007)

<table>
<tr><td>Modulus of elasticity of concrete</td><td>22,750 MPa</td></tr>
<tr><td>Poisson's ratio of concrete</td><td>0.2</td></tr>
<tr><td>Unit weight of concrete</td><td>2480 kg/m³</td></tr>
<tr><td>Compression wave velocity of water</td><td>1440 m/s</td></tr>
<tr><td>Mass density of water</td><td>981 kg/m³</td></tr>
</table>

![](./images/812553861544804352_20.jpg)

**Table 3 Natural frequencies of Pine flat Dam-reservoir system**

<table>
  <thead>
    <tr>
      <th>Mode Number</th>
      <th colspan="2">Natural frequency (Hz)</th>
    </tr>
    <tr>
      <th></th>
      <th>Samii and Lotfi (2007)</th>
      <th>Present study</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1st mode</td>
      <td>2.5267</td>
      <td>2.5966</td>
    </tr>
    <tr>
      <td>2nd mode</td>
      <td>3.2681</td>
      <td>3.3182</td>
    </tr>
    <tr>
      <td>3rd mode</td>
      <td>4.6665</td>
      <td>4.7396</td>
    </tr>
    <tr>
      <td>4th mode</td>
      <td>6.2126</td>
      <td>6.5459</td>
    </tr>
    <tr>
      <td>5th mode</td>
      <td>7.9181</td>
      <td>8.0086</td>
    </tr>
  </tbody>
</table>

## 4.2 Estimation of properties of concrete

Changes in properties of concrete over the ages are estimated on the basis of the concrete grade used in the experimental programme of Washa et al. (1989). The 28-day compressive strength of the concrete is obtained as 36.3 MPa. The initial value $(E_{i})$ in Eq. (15) is considered as 32,660 MPa (Mandal 2017). Variation of elastic modulus of un-degraded and degraded concrete is obtained from Eqs. (12) and (15), respectively and are shown in Fig. 9. Tensile strength at the initial stage and tensile strength at later ages are calculated from Eqs. (17) and (16), respectively. Table 4 summarizes the properties of degraded concrete over the ages. It is clearly observed that the modulus of elasticity and tensile strength of concrete are reduced significantly due to deterioration. Hence, whilst evaluating the seismic response of the aged dam-reservoir system, properties of degraded concrete are utilized as input parameters.

**Fig. 9 Variation of elastic modulus of un-degraded and degraded concrete**

![](./images/812553861544804352_21.jpg)

**Table 4 Properties of degraded concrete at different ages**

<table>
  <thead>
    <tr>
      <th>Age (years)</th>
      <th>Elastic modulus (MPa)</th>
      <th>Tensile strength (MPa)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>32,686.42</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>25</td>
      <td>31,550.23</td>
      <td>3.66</td>
    </tr>
    <tr>
      <td>50</td>
      <td>27,824.35</td>
      <td>3.23</td>
    </tr>
    <tr>
      <td>75</td>
      <td>23,122.96</td>
      <td>2.68</td>
    </tr>
    <tr>
      <td>100</td>
      <td>19,086.7</td>
      <td>2.21</td>
    </tr>
  </tbody>
</table>

![](./images/812553861544804352_22.jpg)

### 4.3 Influence of reflection coefficient on the response of reservoir

An analysis has been performed in order to show the influence of the reflection coefficient on the seismic response of the reservoir. The reservoir is subjected to a complete cycle of sinusoidal acceleration (considering the dam is rigid) having an amplitude of $9.81\ \text{m/s}^2$ and different frequencies such as $\frac{\omega}{\omega_{\text{r}}}=0.05,0.25,1,5$. $\omega$ and $\omega_{\text{r}}$ represent the excitation frequency and the natural frequency of the reservoir, respectively. Hydrodynamic pressure coefficient $\left(C_{\text{p}}=p/\rho_{\text{f}}gH_{\text{f}}\right)$ near the heel at different reflection coefficients are obtained and shown in Fig. 10. It is observed that the effect of the reflection coefficient is significant when the excitation frequency is equal or higher than the natural frequency of the reservoir. The absorption of longitudinal waves is increased under a low reflection coefficient and hence hydrodynamic pressure coefficient is reduced. Therefore, the variation of the reflection coefficient should be considered to get a true response of the aged dam-reservoir system.

![](./images/812553861544804352_23.jpg)

Fig. 10 Hydrodynamic pressure coefficient under sinusoidal excitation for different reflection coefficients

### 4.4 Response of aged dam-reservoir system to near source and far source ground motions

The concrete gravity dam-reservoir coupled system (Fig. 2) is subjected to scaled near source and far source acceleration time histories (Fig. 5), assumed to act at the dam base. Elastic modulus and tensile strength of concrete are considered as mentioned in Table 4. Unit weight and Poisson's ratio of concrete are taken as $2415.82\ \text{kg/m}^3$ and 0.235. Proper- ties of reservoir water are considered as mentioned in Sect. 2.3. Prior to the time-history analysis, the natural time-periods of the system (Table 5) at different ages are obtained from Eigen value analysis. It is observed that natural time-period of the dam-reservoir sys- tem is increased with age. It is necessary to mention that at the age of 100 years, there is an excessive reduction of the tensile strength of the concrete. Therefore, the behaviour of the concrete gravity dam at 100 years cannot be interpreted properly through linear time-his- tory analysis. Hence, the seismic behaviour of the dam-reservoir system is investigated up to the age of 75 years. The sedimentation rate is considered as 0.3 m/year for time-history analysis.

Relative horizontal crest displacement histories (positive value represent downstream deflection) at different ages under near source and far source ground motions of Northridge earthquake are shown in Fig. 11. It is clearly noticed that horizontal crest displacement to NF1 differs considerably from that to FF1, though all the ground motion records arenormalized to have the same PGA level. It is definitely caused by the long-period pulse(s)(apparent in velocity time history) of near source ground motion that exposes the structure to high energy within a short duration at early of the event and produces large deforma- tion. Moreover, horizontal crest displacement is increased at later ages under both ground motions. It is also noticed that the dam experiences more downstream deformation at later ages. Elastic modulus decreases over the ages (Fig. 9) due to degradation, so the dam becomes more flexible, and thus deformation increases at later ages. Major principal stress(tensile) history at heel (node H) under NF1 and FF1 at different ages are shown in Fig. 12. It is observed that tensile stresses are higher at early of the life of the dam, i.e. at the age1 year and are reduced later. The reason behind such a response is that the stiffness of the dam is intact at an early age, causing higher stress. Degradation of concrete reduces stiff- ness at later ages which cause stress relaxation. Therefore, at later ages, deformations are increased but stresses are reduced. Contour plots of major principal (tensile) stress of the dam, along with the hydrodynamic pressure of the reservoir at the time instance when the tensile stress is maximum at the heel, are shown in Fig. 13. It is clearly revealed that tensile stresses in the dam domain and hydrodynamic pressure distribution of reservoir domain vary over the ages. It is also noticed that the tensile stresses of the dam exceed the tensile strength of the material at several regions at every age under NF as well as FF ground motions. Moreover, there is a huge reduction in the tensile strength of concrete over time(Table 4). Hence, an evaluation of the seismic performance of the concrete gravity dam

Table 5 Natural time-period of dam-reservoir system at different ages

<table>
<thead>
<tr>
<th>Age (years)</th>
<th colspan="2">Natural time-period (s)</th>
</tr>
<tr>
<th></th>
<th>1st mode</th>
<th>2nd mode</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.393</td>
<td>0.251</td>
</tr>
<tr>
<td>50</td>
<td>0.418</td>
<td>0.257</td>
</tr>
<tr>
<td>75</td>
<td>0.451</td>
<td>0.265</td>
</tr>
</tbody>
</table>

![](./images/812553861544804352_24.jpg)

![](./images/812553861544804352_25.jpg)

![](./images/812553861544804352_26.jpg)

Fig. 11 Relative horizontal crest displacement histories at different ages under Northridge earthquake

is required to have an insight into the probable damage level of the dam, which will be discussed in the subsequent section. It is revealed from the analysis that the neck (node N) experiences the highest compressive stress in every case. Hence, the contour plot of minor principal (compressive) stress of the dam along with hydrodynamic pressure of the reservoir at the time instance, when compressive stress is maximum at the neck, is shown in Fig. 14. It is noticed that compressive stresses under NF1 is comparatively greater than that under FF1, however, there is not much variation of compressive stresses over the ages under FF1. The peak amplitude of seismic response quantities of the dam-reservoir system at various ages under all near source and far source ground motions are listed in Table 6. Response values under Imperial valley earthquakes show the same evidence that, near source motion cause higher displacement, stresses and hydrodynamic pressure in the dam-reservoir system than far source motion. Hydrodynamic pressure exerted by the reservoir is reduced with the age in most of the cases, because increased sediment depth reduces the reflection coefficient, and thus more absorption of longitudinal waves takes place at the reservoir bed. Therefore, consideration of the influence of sediments is necessary for an accurate response of the dam-reservoir system. Near source ground motion of Northridge earthquake produces the highest crest displacement, principal stresses and hydrodynamic pressure.

![](./images/812553861544804352_27.jpg)

![](./images/812553861544804352_28.jpg)

Fig. 12 Major principal stress histories at heel at different ages under Northridge earthquake

pressure amongst all the cases. Alteration of seismic response of the dam over the ages is quite drastic under NF2, e.g. max. relative horizontal crest displacement at the age of 75 years under NF2 is increased about 12.8% than that at the age of 50 years. However, the maximum relative horizontal crest displacement under FF2 is reduced (0.025 m) at the age of 75 years as compared to that at an early age. The reason behind such an exceptional response can be explained w.r.t. the normalized pseudo-acceleration spectrum of the earthquake motions (Fig. 15), where $T_{\mathrm{n}, 75}$ represents the natural time-period of 1st mode of vibration of the dam-reservoir system at the age of 75 years. It can be noticed that the fundamental time-period of the coupled system lies in the descending stage of the spectrum of far source ground motions and the pseudo-spectral acceleration ratio of FF2 at the period $T_{\mathrm{n}, 75}$ is considerably low (Fig. 15b). Hence, the coupled system is less excited at the age of 75 years under FF2, and thus the deformation of the dam is decreased. Higher seismic response of the dam-reservoir system under NF earthquakes can also be explained w.r.t. the normalized pseudo-acceleration spectrum. The concrete gravity dam-reservoir system is typically a 1st mode dominated structural system that is more excited under NF ground motions because they exhibit higher pseudo-spectral acceleration amplitude than FF ground motions at the fundamental time-period of the coupled system (Fig. 15).

![](./images/812553861544804352_29.jpg)

![](./images/812553861544804352_30.jpg)

Fig. 13 Contour of major principal (tensile) stress and hydrodynamic pressure of dam-reservoir system

## 4.5 Seismic performance evaluation of aged Koyna dam

Tensile stress produced in concrete dams exceeds the tensile strength of the concrete during strong earthquake motion. Hence, most of the studies in recent years have considered nonlinearity in concrete to investigate the tensile cracking in concrete dams. There are mainly two approaches to predict cracks in concrete, namely the discrete crack approach and the smeared crack approach. Besides, the damage-plasticity model is the most widely used numerical model to analyse the nonlinear behaviour of concrete dams under seismic loading. It is quite evident that different constitutive nonlinear models of concrete produce considerably different results for the same input parameters, and a nonlinear analysis requires huge computational efforts and cost. Hence, a rational and systematic methodology was proposed by Ghanaat (2002, 2004) in which a qualitative assessment of the performance level of concrete gravity dams is carried out in terms of Demand Capacity Ratio (DCR), Cumulative Overstress Duration (COD) and spatial proportion of overstressed region on the basis of linear time-history analysis. This procedure is also adopted in the guideline of USACE (2003) and further followed in few other studies (Hariri-Ardebili and Mirzabozorg 2012; Wang et al. 2014; Gorai and Maity 2019). The Demand Capacity Ratio is termed as the ratio of the tensile stress to the tensile strength of concrete. Therefore, $\mathrm{DCR}=1$ indicates a stress level equal to the tensile strength and $\mathrm{DCR}=2$ represents a stress level equal to twice the tensile strength.

![](./images/812553861544804352_31.jpg)

![](./images/812553861544804352_32.jpg)

Fig.14 Contour of minor principal (compressive) stress and hydrodynamic pressure of dam-reservoir system

<table>
<thead>
<tr>
<th colspan="2">Table 6 Peak amplitude of seismic response quantities of dam-reservoir system</th>
<th colspan="2">Northridge</th>
<th colspan="2">Imperial Valley</th>
</tr>
<tr>
<th>Response quantity</th>
<th>Age (years)</th>
<th>NF1</th>
<th>FF1</th>
<th>NF2</th>
<th>FF2</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">Max. relative horizontal crest displacement (m)</td>
<td>1</td>
<td>0.041</td>
<td>0.029</td>
<td>0.035</td>
<td>0.028</td>
</tr>
<tr>
<td>50</td>
<td>0.043</td>
<td>0.033</td>
<td>0.039</td>
<td>0.029</td>
</tr>
<tr>
<td>75</td>
<td>0.045</td>
<td>0.036</td>
<td>0.044</td>
<td>0.025</td>
</tr>
<tr>
<td rowspan="3">Max. major principal stress at heel (MPa)</td>
<td>1</td>
<td>7.66</td>
<td>5.20</td>
<td>6.80</td>
<td>5.45</td>
</tr>
<tr>
<td>50</td>
<td>6.32</td>
<td>4.85</td>
<td>6.47</td>
<td>4.92</td>
</tr>
<tr>
<td>75</td>
<td>6.38</td>
<td>4.61</td>
<td>6.20</td>
<td>3.97</td>
</tr>
<tr>
<td rowspan="3">Max. minor principal stress at neck (MPa)</td>
<td>1</td>
<td>−8.11</td>
<td>−6.49</td>
<td>−6.61</td>
<td>−6.42</td>
</tr>
<tr>
<td>50</td>
<td>−7.82</td>
<td>−6.46</td>
<td>−6.34</td>
<td>−5.67</td>
</tr>
<tr>
<td>75</td>
<td>−6.95</td>
<td>−6.50</td>
<td>−6.09</td>
<td>−4.72</td>
</tr>
<tr>
<td rowspan="3">Max. hydrodynamic pressure (MPa)</td>
<td>1</td>
<td>0.29</td>
<td>0.20</td>
<td>0.24</td>
<td>0.20</td>
</tr>
<tr>
<td>50</td>
<td>0.27</td>
<td>0.17</td>
<td>0.22</td>
<td>0.18</td>
</tr>
<tr>
<td>75</td>
<td>0.25</td>
<td>0.19</td>
<td>0.21</td>
<td>0.17</td>
</tr>
</tbody>
</table>

![](./images/812553861544804352_33.jpg)

![](./images/812553861544804352_34.jpg)

![](./images/812553861544804352_35.jpg)

Fig. 15 Normalized pseudo-acceleration spectrum of near source and far source earthquakes

The Cumulative Overstress Duration is defined as the total duration in exceedance of a particular stress level. The spatial extent of the overstressed region is considered as the global Damage Index (DI) to interpret the damage state of concrete dams. This methodology leads to a conservative decision for the performance evaluation of concrete dams under low to moderate level of earthquakes. Three performance levels have been proposed for concrete gravity dams (Ghanaat 2002, 2004), 1. If $\text{DCR}<1$, the response pattern of the dam is in elastic range; 2. In the case of $1\leq\text{DCR}\leq2$, the performance evaluation curve is below threshold and the proportion of the overstressed region is less than 15% of dam c/s then the damage is minor or moderate; 3. If $\text{DCR}>2$ and overstressed region is more than 15% then the damage is severe, and in this case, a nonlinear analysis is required for accurate assessment of cracks and collapse patterns. As the heel region (Node H) experiences higher tensile stress, COD is determined on the basis of major principal (tensile) stress history at the heel. Performance assessment curves along with the Performance Threshold Curve (PTC) and contours of the overstressed region corresponding to $\text{DCR}=1$ along with DCR values at different ages under Northridge and Imperial Valley earthquake are shown in Figs. 16 and 17, respectively. The spatial proportion of the overstressed region as the percentage of c/s of the dam is also mentioned just below the contour legends (Figs. 16b and 17b). It is observed that the performance assessment curves for FF1 lie below the PTC at every age (Figs. 16a). The performance assessment curves under NF1 lie above the PTC, and the COD value increases with the age of the dam, thus the heel region is subjected to more stress exceedance beyond the stress demand corresponding to $\text{DCR}=1$ and $\text{DCR}=2$ at later ages. Contour plots also suggest that cracks will propagate to a greater depth at the heel with the aging of the dam (Fig. 16b). The heel region may exhibit minor cracking under FF1 at every age, whereas at the age of 50 years and 75 years the neck region is also vulnerable for crack formation under NF1 (Fig. 16b). The performance assessment curves under FF2 are below the PTC at every age; however, the COD value at $\text{DCR}=1$is slightly greater than the permissible limit at the age of 75 years (Fig. 17a). The COD value corresponding to $\text{DCR}=1$ is considerably higher than the permissible limit at every age under NF2 and the COD value corresponding to $\text{DCR}=2$ increases with the age and finally is above the permissible limit at the age of 75 years. There is a little possibility of minor cracking at the heel region under FF2 at every age (Fig. 17b). The heel region is likely to experience more stress exceedance above the stress demand corresponding to $\text{DCR}=1$ and

![](./images/812553861544804352_36.jpg)

![](./images/812553861544804352_37.jpg)

Fig. 16 Assessment of seismic performance of Koyna dam under Northridge earthquake

major tensile cracking at later ages under NF2 (Fig. 17b). However, there is no possibil-
ity of tensile cracking at the neck region to the near source ground motions of the Impe-
rial Valley earthquake. Hence, it is perceived that the DCR value is slightly higher than
2 under NF ground motions at 75 years and the proportion of the overstressed region is
less than 15% for all the cases. Therefore, linear time-history analysis in combination
with a qualitative assessment of damage level is quite appropriate in these cases. In an
overall sense, it is to be inferred that seismic performance demand to the concrete grav-
ity dam is higher under near source ground motions especially at later ages. The cumu-
lative duration of exceeding a particular stress level increases with ages. Near source

![](./images/812553861544804352_38.jpg)

![](./images/812553861544804352_39.jpg)

Fig. 17 Assessment of seismic performance of Koyna dam under Imperial Valley earthquake

ground motions may cause severe damage to the concrete gravity dam in the form of tensile cracking and joint opening at the age of 75 years.

## 5 Conclusion and summary

The seismic response of concrete gravity dam-reservoir coupled system at different ages is obtained under near source and far source ground motions. A systematic procedure is followed to evaluate seismic performance from linear time-history analysis which is quite appropriate for seismic assessment of concrete dams under low to moderate level

![](./images/812553861544804352_40.jpg)

earthquakes. Deterioration of concrete due to hydro-chemo-mechanical effects and vari- ation of reflection coefficient at reservoir bed are incorporated to calculate the seismic response of the aged dam-reservoir system. Near source ground motion produces greater seismic response of the system due to the presence of dominant pulses. The elastic modu- lus of concrete is decreased over the ages, resulting in the dam being more flexible. Hence, the horizontal crest displacement is increased with the age in most of the cases. Stresses are reduced at later ages due to relaxation caused by the reduction in stiffness. Sediment depth increases over the ages which cause more absorption of acoustic waves at the reser- voir bottom, thus exerting less hydrodynamic pressure. Qualitative assessment of perfor- mance level reveals that the concrete gravity dam experiences extreme damage to the near source ground motions at later ages.

Acknowledgements The authors are thankful to anonymous reviewers for their valuable suggestions and comments. This research did not receive any specific grant from funding agencies in the public, commercial or not-for-profit sectors.

## References
Adanur S, Altunişik AC, Bayraktar A, Akköse M (2012) Comparison of near-fault and far-fault ground motion effects on geometrically nonlinear earthquake behavior of suspension bridges. Nat Hazards 64:593–614. https://doi.org/10.1007/s11069-012-0259-5

Azizan NZN, Mandal A, Majid TA et al (2017) Numerical modeling of ageing concrete dam due to alkali-aggregate and thermal chemical reaction. Struct Eng Mech 64:793–802. https://doi.org/10.12989/sem.2017.64.6.793

Bangert F, Grasberger S, Kuhl D, Meschke G (2003) Environmentally induced deterioration of concrete: physical motivation and numerical modeling. Eng Fract Mech 70:891–910. https://doi.org/10.1016/S0013-7944(02)00156-X

Bayraktar A, Altunisik AC, Sevim B et al (2008) Near-fault ground motion effects on the nonlinear response of dam-reservoir-foundation systems. Struct Eng Mech 28:411–442. https://doi.org/10.12989/sem.2008.28.4.411

Bayraktar A, Türker T, Akköse M, Ateş Ş (2010) The effect of reservoir length on seismic performance of gravity dams to near- and far-fault ground motions. Nat Hazards 52:257–275. https://doi.org/10.1007/s11069-009-9368-1

Bhandari M, Bharti SD, Shrimali MK, Datta TK (2018) The numerical study of base-isolated buildings under near-field and far-field earthquakes. J Earthq Eng 22:989–1007. https://doi.org/10.1080/13632469.2016.1269698

Bray JD, Rodriguez-Marek A (2004) Characterization of forward-directivity ground motions in the near-fault region. Soil Dyn Earthq Eng 24:815–828. https://doi.org/10.1016/j.soildyn.2004.05.001

Burman A, Maity D, Sreedeep S, Gogoi I (2011) Long-term influence of concrete degradation on dam-foundation interaction. Int J Comput Methods 08:397–423. https://doi.org/10.1142/S0219876211002472

Dolen TP (2005) Materials properties model of aging concrete. DSO-05–05. Dam Safety Technology Development Program, Denver, Colorado

Ertuncay D, Costa G (2019) An alternative pulse classification algorithm based on multiple wavelet analy- sis. J Seismol 23:929–942. https://doi.org/10.1007/s10950-019-09845-y

Ghanaat Y (2002) Seismic performance and damage criteria for concrete dams. In: Proceedings of the 3rd U.S.-Japan workshop on advanced research on earthquake engineering. San Diego, California

Ghanaat Y (2004) Failure modes approach to safety evaluation of dams. In: Proceedings of the 13th world conference on earthquake engineering. Vancouver, Canada

Gogoi I, Maity D (2006) A non-reflecting boundary condition for the finite element modeling of infinite reservoir with layered sediment. Adv Water Resour 29:1515–1527. https://doi.org/10.1016/j.advwatres.2005.11.004

Gogoi I, Maity D (2007) Influence of sediment layers on dynamic behavior of aged concrete dams. J Eng Mech 133:400–413. https://doi.org/10.1061/(ASCE)0733-9399(2007)133:4(400)

![](./images/812553861544804352_41.jpg)

Natural Hazards

Gogoi I, Maity D (2010) A novel procedure for determination of hydrodynamic pressure along upstream face of dams due to earthquakes. Comput Struct 88:539–548. https://doi.org/10.1016/j.compstruc.2010.01.007

Gorai S, Maity D (2019) Seismic response of concrete gravity dams under near field and far field ground motions. Eng Struct 196:109292. https://doi.org/10.1016/j.engstruct.2019.109292

Hariri-Ardebili MA, Mirzabozorg H (2012) Effects of near-fault ground motions in seismic performance evaluation of a symmetric arch dam. Soil Mech Found Eng 49:192–199. https://doi.org/10.1007/s112004-012-9189-1

Hatami K (1997) Effect of reservoir bottom on earthquake response of concrete dams. Soil Dyn Earthq Eng 16:407–415. https://doi.org/10.1016/S0267-7261(97)00023-7

Heidaria A, Salajegheh E (2009) Wavelet analysis for processing of earthquake records. Asian J Civ Eng 10:397–408

Huang J (2015) Earthquake damage analysis of concrete gravity dams: modeling and behavior under near-fault seismic excitations. J Earthq Eng 19:1037–1085. https://doi.org/10.1080/13632469.2015.1027019

Joshi A, Kumari P, Singh S, Sharma ML (2012) Near-field and far-field simulation of accelerograms of Sikkim earthquake of September 18, 2011 using modified semi-empirical approach. Nat Hazards 64:1029–1054. https://doi.org/10.1007/s11069-012-0281-7

Khiavi MP (2016) Investigation of the effect of reservoir bottom absorption on seismic performance of concrete gravity dams using sensitivity analysis. KSCE J Civ Eng 20:1977–1986. https://doi.org/10.1007/s12205-015-1159-5

Kuhl D, Bangert F, Meschke G (2004a) Coupled chemo-mechanical deterioration of cementitious materials. Part I: modeling. Int J Solids Struct 41:15–40. https://doi.org/10.1016/j.ijsolstr.2003.08.005

Kuhl D, Bangert F, Meschke G (2004b) Coupled chemo-mechanical deterioration of cementitious materials. Part II: numerical methods and simulations. Int J Solids Struct 41:41–67. https://doi.org/10.1016/j.ijsolstr.2003.08.004

Li S, Xie LL (2007) Progress and trend on near-field problems in civil engineering. Acta Seismol Sin 20:105–114. https://doi.org/10.1007/s11589-007-0105-0

Mandal KK (2016) Finite element analysis of aged concrete gravity dams considering dam-reservoir-foundation interaction. Ph.D. thesis, Indian Institute of Technology Kharagpur, India

Mandal A (2017) Earthquake analysis of aged concrete gravity dams considering nonlinear soil-structure-fluid interaction. Ph.D. thesis, Indian Institute of Technology Kharagpur, India

Mandal KK, Maity D (2016) Seismic response of aged concrete dam considering interaction of dam and reservoir in coupled way. Asian J Civ Eng 17:571–592. https://doi.org/10.13140/RG.2.1.4983.4649

Mavroeidis GP, Papageorgiou AS (2003) A mathematical representation of near-fault ground motions. Bull Seismol Soc Am 93:1099–1131. https://doi.org/10.1785/0120020100

Morlet J, Arens G, Fourgeau E, Giard D (1982a) Wave propagation and sampling theory-part I: complex signal and scattering in multilayered media. Geophysics 47:203–221

Morlet J, Arens G, Fourgeau E, Giard D (1982b) Wave propagation and sampling theory—Part II: sampling theory and complex waves. Geophysics 47:222–236. https://doi.org/10.1190/1.1441329

Mukhopadhyay S, Gupta VK (2013a) Directivity pulses in near-fault ground motions-I: identification, extraction and modeling. Soil Dyn Earthq Eng 50:1–15. https://doi.org/10.1016/j.soildyn.2013.02.017

Mukhopadhyay S, Gupta VK (2013b) Directivity pulses in near-fault ground motions-II: estimation of pulse parameters. Soil Dyn Earthq Eng 50:38–52. https://doi.org/10.1016/j.soildyn.2013.02.019

Oluokun FA, Burdette EG, Deatherage JH (1991) Splitting tensile strength and compressive strength relationship at early ages. ACI Mater J 88:115–121

Pan J, Feng Y, Xu Y et al (2013a) Chemo-damage modeling and cracking analysis of AAR-affected concrete dams. Sci China Technol Sci 56:1449–1457. https://doi.org/10.1007/s11431-013-5187-4

Pan J, Feng YT, Jin F, Zhang C (2013b) Numerical prediction of swelling in concrete arch dams affected by alkali-aggregate reaction. Eur J Environ Civ Eng 17:231–247. https://doi.org/10.1080/19648189.2013.771112

Pan J, Xu Y, Jin F, Zhang C (2014) A unified approach for long-term behavior and seismic response of AAR-affected concrete dams. Soil Dyn Earthq Eng 63:193–202. https://doi.org/10.1016/j.soildyn.2014.03.018

PEER Ground Motion Database (2019) Pacific Earthquake Engineering Research Center (PEER) next generation attenuation (NGA) database. https://peer.berkeley.edu/peer_ground_motion_database/. Accessed 22 Jun 2019

Samii A, Lotfi V (2007) Comparison of coupled and decoupled modal approaches in seismic analysis of concrete gravity dams in time domain. Finite Elem Anal Des 43:1003–1012. https://doi.org/10.1016/j.finel.2007.06.015

![](./images/812553861544804352_42.jpg)

Sehhati R, Rodriguez-Marek A, ElGawady M, Cofer WF (2011) Effects of near-fault ground motions and equivalent pulses on multi-story structures. Eng Struct 33:767–779. https://doi.org/10.1016/j.engstruct.2010.11.032

Stewart JP, Chiou S-J, Bray JD et al (2002) Ground motion evaluation procedures for performance-based design. Soil Dyn Earthq Eng 22:765–772. https://doi.org/10.1016/S0267-7261(02)00097-0

USACE (2003) Time-history dynamic analysis of concrete hydraulic structures: engineering and design, Engineering Manual, EM 1110-2-6051. Washington, USA

Wang G, Zhang S, Wang C, Yu M (2014) Seismic performance evaluation of dam-reservoir-foundation systems to near-fault ground motions. Nat Hazards 72:651–674. https://doi.org/10.1007/s11069-013-1028-9

Washa GW, Saemann JC, Cramer SM (1989) Fifty-year properties of concrete made in 1937. ACI Mater J 86:367–371

Yadav KK, Gupta VK (2017) Near-fault fling-step ground motions: characteristics and simulation. Soil Dyn Earthq Eng 101:90–104. https://doi.org/10.1016/j.soildyn.2017.06.022

Yang F, Wang G, Ding Y (2019) Damage demands evaluation of reinforced concrete frame structure subjected to near-fault seismic sequences. Nat Hazards 97:841–860. https://doi.org/10.1007/s11069-019-03678-1

Yazdani Y, Alembagheri M (2017a) Nonlinear seismic response of a gravity dam under near-fault ground motions and equivalent pulses. Soil Dyn Earthq Eng 92:621–632. https://doi.org/10.1016/j.soildyn.2016.11.003

Yazdani Y, Alembagheri M (2017b) Seismic vulnerability of gravity dams in near-fault areas. Soil Dyn Earthq Eng 102:15–24. https://doi.org/10.1016/j.soildyn.2017.08.020

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812553861544804352_43.jpg)