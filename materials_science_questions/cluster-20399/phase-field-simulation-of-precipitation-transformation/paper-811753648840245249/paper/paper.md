# Computational modeling of titanium structures subjected to thermo-chemo-mechanical environment
Caglar Oskay $^{a,*}$, Mark Haney $^{b}$

$^{a}$ Department of Civil and Environmental Engineering, Vanderbilt University, Nashville, TN 37235, United States
$^{b}$ Structural Sciences Center, Air Force Research Laboratory, Wright Patterson Air Force Base, Dayton, OH 45433, United States

---

## ARTICLE INFO

**Article history:**
Received 5 January 2010
Received in revised form 31 July 2010
Available online 22 August 2010

**Keywords:**
Multi-physics
Titanium
Failure
Embrittlement
Alpha-case

---

## ABSTRACT

This manuscript provides a new coupled thermo-chemo-mechanical computational model for titanium structures subjected to extreme loading and environment. The proposed model accounts for the formation of oxygen enriched (alpha-case) titanium, as well as the coupling effects between the response characteristics of mechanical and oxygen infiltration processes into titanium at high temperature environment. The formation of alpha-case at the surface of the structure is modeled as diffusion of oxygen into the titanium substrate. The mechanical response of the structure is idealized using the Johnson-Cook model, which is generalized to account for the effects of oxygen induced embrittlement and hardening. The interplay between mechanical damage, oxygen infiltration and temperature on the chemo-mechanical response is evaluated using numerical simulations. The fully coupled mechanical and diffusion processes are solved based on a staggered coupling algorithm. The capabilities of the computational model are assessed by the analysis of a panel composed of Ti-6Al-2Sn-4Zr-2Mo titanium alloy subjected to thermal shock loading.

© 2010 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Alpha-stabilizers such as oxygen, nitrogen and hydrogen available in the environment diffuse into titanium and titanium alloys at elevated temperatures. The resulting material, called alpha-case titanium, exhibits significantly different structural properties including embrittlement, increased hardness, and reduction in fatigue life (Donachie, 2000; Leyens and Peters, 2003).

Formation of alpha-case is routinely observed during the manufacturing of titanium structures. For instance in investment casting, an oxygen-rich alpha-case titanium layer develops along the interface between the structure and the investment material (Boettinger et al., 2000; Bumps et al., 1953; Ogden and Jaffe, 1955; Roe et al., 1960; Sung and Kim, 2005). The standard practice in the investment community is to physically remove the oxygen-rich alpha-case layer by chemical milling. The prediction of the thickness of oxygen-rich layer to be removed and the diffusion characteristics of oxygen in titanium has been an active research field in the past four decades (e.g.,Boettinger et al., 2000; Chan et al., 2008; Keanini et al., 2007. Comprehensive review of earlier diffusivity characterization of titanium and titanium alloys is provided by Liu and Welsch (1988)). The majority of the investigations consider the oxygen ingress into titanium to obey Fick's law of diffusion and employ one-dimensional analytical models to relate the alpha-case layer thickness to the diffusivity and thermal conditions. The effect of variable diffusivity within the titanium microstructure (i.e., alpha, beta and oxide phases) due to phase transformations or heterogeneity have been investigated based on numerical and analytical diffusion models as well (Schuh, 2000; Rosa, 1970). Coupling the effect of aggressive agent transport and degradation in the mechanical response in metals have been subject to many investigations. A tremendous body of literature exists in numerical and experimental characterization of the coupled response mechanisms, and an extensive literature survey is out of the scope of this paper. A number of material models that relate the elasto-plastic and damage processes to transport of aggressive agents have been devised. For instance, Sofronis and McMeeking (Sofronis and McMeeking, 1989) proposed a coupled diffusion-stress analysis model to idealize the local effect of hydrogen transport around a crack tip. Carranza and Haber (1999) employed a coupled stress-assisted diffusion model with the oxygen embrittlement model based on Sofronis and McMeeking's model (Sofronis and McMeeking, 1989) to study intergranular fracture in nickel-based superalloys. Deng et al. (2005) recently proposed a damage mechanics model that incorporates the grain-boundary oxygen embrittlement effects to investigate creep behavior of steel alloys.

Characterization of the response of titanium and titanium alloy aircraft structures and components operating in hypersonic

---

* Corresponding author. Address: VU Station B#351831, 2301 Vanderbilt Place, Nashville, TN 37235, United States.
E-mail address: caglar.oskay@vanderbilt.edu (C. Oskay).

0020-7683/$ - see front matter © 2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijsolstr.2010.08.014

environment poses additional challenges. First, the alpha-case layer forms during the operational environment of the aircraft and it cannot be eliminated during manufacturing. The alpha-case layer formed during the operation acts as potential sites for initiation of cracks, which may grow under the aerodynamic service loads to cause failure of the structure or the component. Second, the growth of alpha-case layer is affected by the state of mechanical damage. Nucleation and growth of the microcracks and voids enhance the formation of alpha-case in the structure. The characterization of the response is therefore a coupled multiphysics problem involving thermal, chemical diffusion and mechanical processes.

Fig. 1 illustrates the coupling between the thermal state of the structure, diffusion of oxygen as well as deformation and damage state of the structure. Some of the coupling mechanisms between these processes have been well characterized including the thermal actuation of oxygen diffusion, as well as embrittlement and hardening due to oxygen diffusion. In contrast, other coupling mechanisms such as the effect of microcracking on the oxygen diffusion characteristics have not yet been sufficiently characterized. In addition to the presence of multiple physical processes, the evaluation of the response of titanium structures under thermomechanical loading conditions spans a number of spatial scales. The oxygen-enriched alpha-case titanium typically extends up to a boundary region with a thickness in the order of tens of microns. In contrast, the overall thickness of the titanium structure is in the millimeter scale. The heterogeneity of the diffusion and mechanical characteristics of the titanium microstructure, which has a characteristic size of the order of a few microns or submicron scale, provides additional complexity to accurate computational characterization of structural response in extreme thermomechanical environments. Fig. 2 illustrates the relevant spatial scales: the scale of the alpha-case boundary region, the scale of the titanium grain structure and the scale of the overall structure.

In this manuscript, we propose a new coupled computational model to characterize the response of titanium structures subjected to thermo-chemo-mechanical loading and environmental conditions. To the best of the authors' knowledge, this study constitutes one of the first efforts in the analysis of mechanical failure response of titanium structures at the structural level. The proposed computational model is unique in modeling the alpha-case formation and the mechanical response of titanium structures in the following respects:

1. The classical alpha-case formation model is enhanced to account for the effect of mechanical damage on the diffusivity of oxygen through the structure.

2. The elastic-plastic model to idealize the mechanical response of titanium structures based on the well-known Johnson-Cook model is generalized to account for the effects of increased oxygen content.

3. A semi-explicit coupled chemo-mechanical computational strategy is proposed to evaluate the coupled multi-physical processes (i.e., diffusion of oxygen and mechanical response).

4. A computational algorithm to bridge the scale of the alpha-case boundary region and the scale of the overall titanium structure is proposed. This algorithm avoids fine discretization of the titanium substrate, while accurately describing the damage evolution and diffusion processes at the boundary region.

The remainder of this manuscript is organized as follows: The oxygen diffusion model for modeling the evolution of alpha-case layer, which incorporates the effects of mechanical damage, is discussed in Section 2. The modified Johnson-Cook model for alpha-case titanium and titanium alloys is explained in Section 3. Section 4 details the heat conduction model employed to predict the thermal profile in titanium structures. In Section 5, the implementation details including the scale bridging between the boundary scale and the titanium substrate as well as the coupled solution strategy for the chemo-mechanical boundary value problem are presented. In Section 6, the capabilities of the proposed model are demonstrated by computational analysis of a Ti-6Al-2Sn-4Zr-2Mo panel subjected to thermal shock loading. Section 7 presents the conclusions and future research directions.

## 2. Oxygen diffusion model

Infiltration of oxygen into titanium and titanium alloys has been experimentally analyzed by numerous investigators since the 1950s. The infiltration of oxygen into titanium depends on the diffusion coefficients of oxygen through the alpha and beta phases as well as grain boundaries, grain size, temperature, microcrack density, among other factors (Rosa, 1970; Pitt and Ramulu, 2004). Oxygen infiltration into titanium has been traditionally modeled as a one-dimensional diffusion problem characterized by the apparent diffusivity coefficient, $D$. In one-dimensional setting, the diffusion process is idealized using Fick's second law:

$$
\frac{\partial c}{\partial t}=\frac{\partial}{\partial y}\left(D \frac{\partial c}{\partial y}\right) \tag{1}
$$

where $c(y,t)$ is the oxygen concentration, $y$ the position coordinate towards the interior of the titanium structure, $D(T,t)$ the diffusivity of oxygen in titanium, $t$ denotes time coordinate, and $T$ the

![](./images/811753648840245249_1.jpg)

Fig. 1. Multiple physical processes affecting the response prediction of alpha-case titanium.

![](./images/811753648840245249_2.jpg)

Fig. 2. Multiple scales affecting the response prediction of titanium structures subjected to thermo-mechanical environment.

temperature. The oxygen concentration in the titanium substrate, $c_{\infty}$, and the ambient oxygen concentration, $c_{0}(t)$, provide the initial and boundary conditions of the problem:
$$
c(y=0, t)=c_{0}(t) ; \quad c(y=\infty, t)=c_{\infty}
\tag{2}
$$

When the diffusivity is constant along the depth coordinate, Eq. (1) yields an analytical solution in the following form:
$$
c(y, t)=c_{0}(t)-\left[c_{0}(t)-c_{\infty}\right] \operatorname{erf}\left(\frac{y}{\sqrt{4 \tau}}\right)
\tag{3}
$$
in which, time variable $\tau$ is given as:
$$
\tau=\int_{0}^{t} D\left(T, t^{\prime}\right) d t^{\prime}
\tag{4}
$$

The temperature dependent diffusivity is expressed as:
$$
D(\omega, T)=D_{0} \exp \left(-\frac{Q}{R T}\right)
\tag{5}
$$

$D_{0}$ is the pre-exponential constant, which is the reference diffusion coefficient at the solidus temperature, $Q$ the activation energy, and $R$ the universal gas constant. An oxygen concentration front with the critical oxygen concentration level $c_{\text {crit }}$ occurs at depth $\bar{y}$, which satisfies:
$$
\bar{y}(t)=2 \lambda \sqrt{\tau}
\tag{6}
$$
where, $\lambda$ is the solution of the following nonlinear equation:
$$
\Phi(\lambda):=\operatorname{erf}(\lambda)+\frac{c_{\text {crit }}-c_{\infty}}{c_{0}-c_{\infty}}-1=0
\tag{7}
$$

The one-dimensional model defined above has been successfully employed to predict the thickness of alpha-case layer as a function of time and temperature in metal forming conditions. In the analysis of aerospace structures subjected to thermo-mechanical loading, the one-dimensional model does not account for the effect of mechanical damage on the diffusivity of the titanium structure. Furthermore, the mechanical loading and the shock conditions provide a multidimensional thermal and mechanical response profile. The diffusivity of the titanium therefore varies along the spatial directions. The one-dimensional diffusion model does not account for the variability of diffusivity within the spatial problem domain. In this study, the one-dimensional diffusion model is generalized to account for the effect of mechanical loading on the oxygen diffusion, and expanded to two-dimensions.

### 2.1. Modeling the effect of mechanical damage on diffusivity

The diffusion process is affected by the formation of microscopic defects within structures due to thermal and mechanical loads. The apparent diffusivity may be enhanced as a function of the microcrack density. An example of this effect has been investigated by Krajcinovic et al. (1992). They proposed a diffusion model, which incorporates the effect of microcrack density on diffusion characteristics of chemical ions into concrete microstructure based on percolation theory. Percolation theory (Stauffer, 1985) provides a theoretical basis for describing the effect of microcracking on the diffusion processes. Percolation theory has been previously adopted to solve additional engineering problems involving diffusion of fluids in solid media (e.g., Barenblatt et al., 1960; Salganik, 1974).

Let $\omega$ denote the mechanical damage at a material point measured as the microcrack density. The diffusivity of the oxygen of titanium in the presence of mechanical damage in addition to the thermal effects is expressed as:
$$
D(\omega, T)=D_{0}[1+\mathcal{D}(\omega)] \exp \left(-\frac{Q}{R T}\right)
\tag{8}
$$
in which, the effect of mechanical damage on diffusivity is expressed in terms of an initiation and a percolation component:
$$
\mathcal{D}=D_{i}+D_{p}
\tag{9}
$$
where,
$$
D_{i}=a \omega ; \quad D_{p}= \begin{cases}0 & \omega<\omega_{c} \\ \frac{\left(\omega-\omega_{c}\right)^{2}}{\left(\omega-\omega_{e c}\right)} & \omega_{c} \leqslant \omega<\omega_{e c} \\ \infty & \omega \geqslant \omega_{e c}\end{cases}
\tag{10}
$$

At relatively low levels of microcrack density $\omega<\omega_{c}$, the oxygen diffusivity linearly increases with damage (Salganik, 1974). $\omega_{c}$ is the conduction percolation threshold. When damage exceeds elastic percolation threshold, $\omega_{e c}$, a continuous path across the representative volume at the material point is formed, permitting the free flow of oxygen (Stauffer, 1985). In the intermediate values of mechanical damage, the rate of change of apparent diffusivity progressively increases with increasing mechanical damage. Fig. 3 illustrates the effect the presence of damage on the diffusivity. In our numerical simulations, a finite value for $D_{p}$ is employed for $\omega>\omega_{e c}$ to avoid numerical instability.

![](./images/811753648840245249_3.jpg)

Fig. 3. Effect of mechanical damage on diffusivity.

Table 1
Material parameters employed to model the oxygen diffusion in Ti-6Al-2Sn-4Zr-2Mo.

<table>
  <thead>
    <tr>
      <th>$D_0$ [cm²/s]</th>
      <th>Q [kJ/mole]</th>
      <th>$c_\infty$ [wt.%]</th>
      <th>$c_0$ [wt.%]</th>
      <th>$\omega_c$</th>
      <th>$\omega_{ec}$</th>
      <th>$a$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.62</td>
      <td>203</td>
      <td>0.15</td>
      <td>10.0</td>
      <td>0.1</td>
      <td>0.5</td>
      <td>3.56</td>
    </tr>
  </tbody>
</table>

### 2.2. Modeling diffusion in two dimensions

In this manuscript, we employ a two-dimensional diffusion equation to describe the evolution of oxygen concentration in titanium structures. Two-dimensional treatment is necessary when curved panels are subjected to severe thermo-mechanical environments, and when thermal shocks on the panel induce two-dimensional temperature profiles within the panels. These problems lead to an uneven diffusion of oxygen along the panel surface. The two-dimensional diffusion equation is expressed as:

$$
\dot{c}(\mathbf{x}, t)=\nabla \cdot[D(\mathbf{x}, t) \nabla c(\mathbf{x}, t)] \tag{11}
$$

The initial and boundary conditions of the two-dimensional diffusion problem are:

$$
c(\mathbf{x}, t)=c_{0} ; \quad \mathbf{x} \in \Gamma_{D}^{c} \tag{12}
$$

$$
c(\mathbf{x}, t=0)=c_{\infty} ; \quad \mathbf{x} \in \Omega \tag{13}
$$

in which, $\Gamma_{D}^{c}$ denotes the outer boundary of the titanium structure exposed to elevated oxygen concentration, $c_{0}$. The initial oxygen concentration value, $c_{\infty}$, is provided by the chemical composition of the titanium alloy. $\Omega \subset \mathbb{R}^{2}$ denotes the domain of the structure. Eq. (11), along with the initial and boundary conditions, is evaluated numerically using the finite element method. The boundary value problem for the diffusion equation is coupled with the mechanical response model, since diffusivity, $D$, is a function of the mechanical damage, $\omega$.

The literature on diffusion of oxygen in titanium is extensive. A survey of studies on the determination of diffusion parameters for pure titanium and some titanium alloys is found in Ref. (Liu and Welsch, 1988). The majority of these investigations focus on oxygen diffusion in pure titanium. A relatively limited number of investigations focus on titanium alloys as well. The literature reveals a significant scatter in the values of pre-exponential constant and activation energy based on the type of alloy and the experimental technique employed to evaluate these constants. For pure titanium, the scatter is of five orders of magnitude for the pre-exponential constant and 100% for the activation energy. In this study, we focus on the response of Ti-6Al-2Sn-4Zr-2Mo, which has been previously investigated (Shamblen and Redden, 1968; Shenoy et al., 1986). We employ the pre-exponential constant and activation energy values reported by Ref. (Shamblen and Redden, 1968). In the numerical simulations below, the parameters that characterize the effects of damage on diffusivity: $a$, $\omega_{c}$ and $\omega_{ec}$ is taken to be 3.56, 0.1 and 0.5, respectively. Experimental investigations are being conducted to calibrate these material parameters and will be reported in a separate publication. The full list of diffusion parameters employed in our simulations are summarized in Table 1.

Fig. 4 illustrates the evolution of alpha-case depth as a function of damage variable, $\omega$, at constant temperature of $T=600^{\circ} \mathrm{C}$. The alpha-case depth is defined by the iso-contour of the critical oxygen concentration value of $c_{\text {crit }}=4.5 \%$. A steady increase in diffusivity is observed as a function of damage variable up to the elastic percolation limit. For higher values of damage, oxygen infiltrates significantly rapidly into the titanium. The combined accelerating effect of temperature and damage state on the evolution of alpha-case depth in time is illustrated in Fig. 5.

### 3. Mechanical response based on modified Johnson–Cook model

The ingress of oxygen is well known to cause embrittlement, increase in the hardness of titanium alloys and drastically reduce the fatigue life (Donachie, 2000; Leyens and Peters, 2003). In this study, we concentrate on modeling the monotonic mechanical response of titanium as a function of oxygen concentration. The governing equilibrium equation for the boundary value problem describing the mechanical response is:

![](./images/811753648840245249_4.jpg)

Fig. 4. Evolution of alpha-case depth in Ti-6Al-2Sn-4Zr-2Mo as a function of mechanical damage state at temperature $T=600^{\circ} \mathrm{C}$.

![](./images/811753648840245249_5.jpg)

Fig. 5. Evolution of alpha-case depth in Ti-6Al-2Sn-4Zr-2Mo as a function of temperature and mechanical damage state.

$$
\nabla \cdot \boldsymbol{\sigma}+\rho \mathbf{b}=0 ; \quad \mathbf{x} \in \Omega
\tag{14}
$$

in which, $\boldsymbol{\sigma}$ denotes stress, $\mathbf{b}$ the body force and, $\rho$ the density. The boundary and initial conditions for the deformation field are:

$$
\mathbf{u}(\mathbf{x}, t)=\overline{\mathbf{u}}(\mathbf{x}, t) ; \quad \mathbf{x} \in \Gamma_{D}^{\mathbf{u}}
\tag{15}
$$

$$
\boldsymbol{\sigma} \cdot \mathbf{n}=\overline{\mathbf{t}}(\mathbf{x}, t) ; \quad \mathbf{x} \in \Gamma_{N}^{\mathbf{u}}
\tag{16}
$$

$$
\mathbf{u}(\mathbf{x}, t=0)=\mathbf{u}_{0}(\mathbf{x}) ; \quad \mathbf{x} \in \Omega
\tag{17}
$$

where; $\overline{\mathbf{u}}$ the prescribed boundary displacement along the Dirichlet boundary $\Gamma_{D}^{\mathbf{u}}$, $\overline{\mathbf{t}}$ the prescribed boundary traction along the Neumann boundary, $\Gamma_{N}^{\mathbf{u}}$ such that: $\Gamma_{D}^{\mathbf{u}} \cup \Gamma_{N}^{\mathbf{u}} \equiv \partial \Omega$ and $\Gamma_{D}^{\mathbf{u}} \cap \Gamma_{N}^{\mathbf{u}} \equiv \emptyset$, $\mathbf{u}_{0}$ is the initial deformation state of the structure and, $\mathbf{n}$ denotes normal vector. The constitutive response of titanium alloys are idealized based on a visco-plastic constitutive relationship:

$$
\dot{\boldsymbol{\sigma}}=\mathbf{L}:\left(\dot{\boldsymbol{\varepsilon}}-\dot{\boldsymbol{\varepsilon}}^{v p}\right)
\tag{18}
$$

where, $\boldsymbol{\varepsilon}$ and $\boldsymbol{\varepsilon}^{v p}$ denote total strain and viscoplastic strain tensors, respectively. Superscribed dot denotes material time derivative. The evolution of the viscoplastic strain is expressed as a power law of the form:

$$
\dot{\boldsymbol{\varepsilon}}^{v p}=\gamma\left\langle\frac{f}{\sigma_{Y}}\right\rangle^{q} \frac{\partial f}{\partial \boldsymbol{\sigma}}
\tag{19}
$$

in which, $\gamma$ is the fluidity parameter, $\sigma_{Y}$ the yield stress, $q$ viscoplastic hardening exponent, and $f(\boldsymbol{\sigma}, \sigma_{Y})$ the Von-Mises yield function.

### 3.1. Modified Johnson-Cook yield stress

Johnson-Cook model provides a functional relationship for yield response of metals, which vary as a function of the applied strain, strain rate and temperature. Johnson-Cook model has been previously employed to idealize the response of titanium alloys (Kay, 2003). The classical Johnson-Cook yield stress is defined as (Johnson and Cook, 1985):

$$
\sigma_{Y}=\left[A+B\left(\bar{\varepsilon}^{v p}\right)^{n}\right]\left[1+C \ln \left(\dot{\varepsilon}^{*}\right)\right]\left[1+\left(T^{*}\right)^{m}\right]
\tag{20}
$$

where, $A, B, C, n$ and $m$ are material parameters. The effective viscoplastic strain, is defined as:

$$
\bar{\varepsilon}^{v p}=\sqrt{\frac{2}{3} \boldsymbol{\varepsilon}^{v p}: \boldsymbol{\varepsilon}^{v p}}
\tag{21}
$$

$T^{*}$ is the non-dimensional temperature:

$$
T^{*}=\frac{T-T_{\text {room }}}{T_{\text {melt }}-T_{\text {room }}}
\tag{22}
$$

where, $T_{\text {room }}$ and $T_{\text {melt }}$ are the room and melting temperatures, respectively. $\dot{\varepsilon}^{*}$ is the non-dimensional strain rate:

$$
\dot{\varepsilon}^{*}=\frac{\dot{\bar{\varepsilon}}^{v p}}{\dot{\varepsilon}^{0}}
\tag{23}
$$

where, the reference strain rate $\dot{\varepsilon}^{0}$ is taken to be unity.

The classical Johnson-Cook yield stress does not take into account the increase in the hardness of titanium as a function of the oxygen ingress. We have extended the original yield stress model to incorporate the oxygen-ingress induced hardening. The relationship between the hardness, $H$, and oxygen concentration, $c$ has been experimentally investigated (e.g., Boettinger et al., 2000; Bumps et al., 1953; Ogden and Jaffe, 1955; Roe et al., 1960) for titanium and titanium alloys. For instance, Ogden and Jaffe (1955) proposed the following relationship:

$$
H=65+310 c^{1 / 2}
\tag{24}
$$

Chan et al. (2008) found that this relationship overpredicts the hardness for oxygen concentrations of over 1.5%. An alternative linear model proposed by Roe et al. (1960) is adopted in this study:

$$
H=H_{0}+b c
\tag{25}
$$

in which, $H_{0}$ denotes the reference hardness value. Assuming that the thickness of the oxide layer forming on the surface of the alpha-case titanium layer is negligible, the effect of oxygen concentration on the yield stress is expressed based on Tabor's relationship (Tabor, 1951). To this extent, the yield stress of titanium is linearly related to the oxygen concentration:

$$
\sigma_{Y}=\sigma_{Y_{0}}+k c
\tag{26}
$$

in which, $\sigma_{Y_{0}}$ is the yield strength at bulk oxygen concentration $c_{\infty}$. In view of the above-mentioned model, the Johnson-Cook yield stress model is modified to represent the response of oxygen rich titanium:

$$
\sigma_{Y}=\left[A+B\left(\bar{\varepsilon}^{v p}\right)^{n}+F c\right]\left[1+C \ln \left(\dot{\varepsilon}^{*}\right)\right]\left[1+\left(T^{*}\right)^{m}\right]
\tag{27}
$$

in which, $F$ is a material parameter.

### 3.2. Modified Johnson-Cook damage

We employ a strain-based damage progression formulation to model the failure of titanium structures subjected to mechanical and thermal loads in addition to alpha-case formation. Damage parameter, $\omega$, is defined as the ratio between the accumulated viscoplastic strain, $\bar{\varepsilon}^{v p}$ and the failure strain, $\varepsilon_{f}$:

![](./images/811753648840245249_6.jpg)

Fig. 6. Constitutive response of Ti-6Al-2Sn-4Zr-2Mo titanium at bulk and critical oxygen concentrations when T = 1200°F.

$$
\omega=\frac{\bar{\varepsilon}^{v p}}{\varepsilon_{f}}
\tag{28}
$$

The failure strain is described as a function of stress, strain rate and temperature:

$$
\varepsilon_{f}=\left[D_{1}(C)+D_{2} \exp \left(D_{3} \sigma^{*}\right)\right]\left[1+D_{4} \ln \left(\dot{\varepsilon}^{*}\right)\right]\left[1+D_{5} T^{*}\right]
\tag{29}
$$

where, $D_2$, $D_3$, $D_4$ and $D_5$ are material parameters; $\sigma^{*}$ is the ratio between the pressure and the effective stress, $\bar{\sigma}$:

$$
\sigma^{*}=\frac{\operatorname{tr}(\boldsymbol{\sigma})}{3 \bar{\sigma}} ; \quad \bar{\sigma}=\sqrt{\frac{3}{2} \boldsymbol{\sigma}: \boldsymbol{\sigma}}
\tag{30}
$$

The Johnson-Cook failure strain (Johnson and Cook, 1985) model, which was originally developed based on parametric failure analysis of experimental datasets, includes a constant $D_1$ parameter. In this study, progressive embrittlement of titanium due to ingress of oxygen is modeled by considering an oxygen concentration dependent $D_1$ parameter:

$$
D_{1}= \begin{cases}D_{1}^{\infty} & \text { if } \quad c \leqslant c_{\infty} \\ \frac{1}{c_{\infty}-c_{\text {crit }}}\left[\left(D_{1}^{\infty}-D_{1}^{\alpha}\right) c+D_{1}^{\alpha} c_{\infty}-D_{1}^{\infty} c_{\text {crit }}\right] & \text { if } \quad c_{\infty}<c<c_{\text {crit }} \\ D_{1}^{\alpha} & \text { if } \quad c \geqslant c_{\text {crit }}\end{cases}
\tag{31}
$$

$D_{1}^{\infty}$ is the value of $D_1$ parameter at the oxygen concentration level in the titanium substrate. The bulk titanium reaches its most brittle state (i.e., $D_1 = D_{1}^{\alpha}$) as the oxygen concentration reaches the critical value, $c_{\text{crit}}$. A linear relationship between the oxygen concentration and embrittlement is assumed in the intermediate concentration levels.

Damage parameter $\omega$ does not affect the evolution of the constitutive response until complete failure at the material point (i.e., $\omega=1$). At failure, the residual stiffness at the material point is set to a small fraction of the elastic stiffness of the material, which accounts for failure induced relaxation and load redistribution. Since no progressive softening takes place in the model, the underlying differential equations do not loose ellipticity, and consequent damage localization and spurious mesh dependency effects observed in classical continuous damage mechanics models do not occur. Fig. 6 illustrates the stress-strain response of Ti-6Al-2Sn-4Zr-2Mo titanium subjected to pure tension at 650 °C. The figure shows the constitutive response at oxygen concentration levels of 0.295%, 1%, 2%, 3%, 4% and 4.5%. $c=4.5\%$ and $c=0.295\%$ are the critical and bulk oxygen concentrations, respectively. Increasing oxygen concentration clearly indicates a rise in the yield stress and a drop in ductility as a function of the rise in oxygen concentration. The effect of temperature on the constitutive response of titanium is illustrated in Fig. 7 for critical and bulk oxygen concentrations. Fig. 7 shows the compounded embrittlement and hardening of titanium as a function of temperature and oxygen concentration. The material parameters used for Ti-6Al-2Sn-4Zr-2Mo are tabulated in Table 2. The classical Johnson-Cook parameters are obtained by minimizing the discrepancy between the hardening curves computed by the model and experimental data presented in Ref. (Wood and Favor, 1972). The critical oxygen concentration will be obtained based metallography, as the oxygen-rich layer displays a color contrast with the substrate bulk alloy as described in Ref. (Boettinger et al., 2000). The effect of oxygen concentration on the damage response of

![](./images/811753648840245249_7.jpg)

Fig. 7. Constitutive response of Ti-6Al-2Sn-4Zr-2Mo at various temperatures.

<table><caption>Table 2
Material parameters of the generalized Johnson–Cook Model for oxygen infiltrated titanium.</caption>
<tbody>
<tr>
<td>
$A$ [MPa]
</td>
<td>
$B$ [MPa]
</td>
<td>
$C$
</td>
<td>
$F$ [MPa]
</td>
<td>
$n$
</td>
<td>
$m$
</td>
</tr>
<tr>
<td>
827
</td>
<td>
820
</td>
<td>
0.014
</td>
<td>
110
</td>
<td>
0.93
</td>
<td>
0.85
</td>
</tr>
<tr>
<td>
$D_{1}^{\infty}$
</td>
<td>
$D_{1}^{x}$
</td>
<td>
$D_{2}$
</td>
<td>
$D_{3}$
</td>
<td>
$D_{4}$
</td>
<td>
$D_{5}$
</td>
</tr>
<tr>
<td>
$-0.22$
</td>
<td>
$-0.27$
</td>
<td>
0.27
</td>
<td>
0.48
</td>
<td>
0.014
</td>
<td>
0.5
</td>
</tr>
<tr>
<td>
$T_{melt}$ [$^\circ$F]
</td>
<td>
$\dot{\varepsilon}^{0}$
</td>
<td>
$c_{crit}$ [wt %]
</td>
<td>
$c_{\infty}$ [wt.%]
</td>
<td>
$q$
</td>
<td>
$\gamma$ [MPa-hr]$^{-1}$
</td>
</tr>
<tr>
<td>
3092
</td>
<td>
1.0
</td>
<td>
4.5
</td>
<td>
0.295
</td>
<td>
0.3
</td>
<td>
1.0
</td>
</tr>
</tbody>
</table>

alpha-case titanium will be calibrated using tensile testing of coupon level specimens with varying degrees of oxygen exposure.

### 4. Heat conduction model

Accurate prediction of the thermal response of titanium structures is critical to modeling and prediction of alpha-case formation and mechanical failure due to embrittlement, since the alpha-case formation is primarily controlled by the thermal state of the structure. The thermal response is modeled based on the following boundary value problem:

$$
\nabla \cdot(k(T) \nabla T)+r=\rho c_{v}(T) \frac{\partial T}{\partial t} \quad \text { on } \Omega
\tag{32}
$$

$$
T=\overline{T}(x, y, t) \quad \text { on } \partial \Omega_{D}^{T}
\tag{33}
$$

$$
-k \frac{\partial T}{\partial n}=\beta(x, y, t) T-T_{0}(x, y, t) \quad \text { on } \partial \Omega_{N}^{T}
\tag{34}
$$

$$
T(x, y, t=0)=\widehat{T}(x, y) \quad \text { on } \Omega
\tag{35}
$$

in which, $k$ is the thermal conductivity, $c_{v}$ specific heat, $r$ heat source/sink, $\overline{T}$ prescribed temperature at the boundary, $\beta$ the reference film coefficient and $T_{0}$ the reference sink temperature, and $\widehat{T}$ is the initial thermal state of the structure. The conductivity and the specific heat of titanium is nonlinearly related to the temperature. This nonlinear relationship is expressed using fitting polynomials to the experimental values provided in Ref. (Wood and Favor, 1972). Quadratic polynomials yield adequate fit to express the functional relationship between temperature and conductivity and specific heat for Ti-6Al-2Sn-4Zr-2Mo. The experimental and fitted conductivity and specific heat curves are shown in Fig. 8. The density of the titanium alloy is taken to be $4.539 \mathrm{~g} / \mathrm{cm}^{3}$.

![](./images/811753648840245249_8.jpg)

Fig. 8. Thermal properties of Ti-6Al-2Sn-4Zr-2Mo: conductivity and specific heat.

### 5. Implementation

The proposed thermo-chemo-mechanical model is implemented in the commercial software package DiffPack. DiffPack is an object oriented development framework for the numerical solution of partial differential equations (Langtangen, 2003). DiffPack provides a library of C++ classes to facilitate development of solution algorithms for complex PDEs. The finite element implementation of the thermal, mechanical and diffusion processes based on the Bubnov-Galerkin method is standard and the details of the implementation is found in classical finite element method texts (e.g., Hughes, 2000; Owen and Hinton, 1980). We focus on the two aspects of the numerical implementation: (1) Bridging the scales associated with the boundary region and the titanium substrate, and; (2) Evaluation of the chemo-mechanical problem based on a semi-explicit coupled solution strategy.

#### 5.1. Bridging the boundary scale and the structural scale

The alpha-case formation in titanium structures occurs along the surfaces subjected to high temperature and fluxes along with high concentration of oxygen. The embrittled alpha-case is typically confined to a few microns thick boundary region. The thickness of the boundary region is significantly smaller than the overall thickness of the structure, which is of the order of millimeters. The disparity between the boundary scale and the structural scale is illustrated in Fig. 9. Numerical prediction of the oxygen infiltration induced embrittlement and consequent structural failure requires fine resolution of the boundary scale to accurately capture the extent of the alpha-case region. Therefore, boundary region illustrated in Fig. 9 is discretized with a dense finite element mesh. Fine discretization of the entire structural domain is computationally costly from memory and performance perspectives, and typically not needed since the alpha-case region does not extend beyond the thin boundary region. In this study, we consider a fine discretization of the boundary region, which encloses the alpha-case, and a coarse discretization of the bulk titanium structure.

We decompose $\Omega$ into a boundary region, denoted as $\Omega_{b}$ and the substrate, $\Omega_{s}$:

$$
\Omega=\Omega_{s} \cup \Omega_{b}
\tag{36}
$$

such that $\Omega_{s} \cap \Omega_{b}=\emptyset$. The alpha-case region, denoted by $\Omega_{\alpha}$ is embedded in the boundary region (i.e., $\Omega_{\alpha}(t) \subset \Omega_{b}$) for the entire observation period. A transition region $\Omega_{\text {transition }}=\Omega_{b} \backslash \Omega_{\alpha}$ separates the alpha-case region from the substrate. The boundary region and the substrate is separated by the interface denoted as $\Gamma_{I}$. The continuity of the cardinal unknown fields for the mechanical, thermal and chemical problems are ensured based on a penalty formulation described below.

The governing boundary value problem for the mechanical process is written in the weak form as:

$$
\int_{\Omega} \mathbf{v} \cdot(\nabla \cdot \boldsymbol{\sigma}) d \Omega+\int_{\Omega} \mathbf{v} \cdot \rho \mathbf{b} d \Omega=0
\tag{37}
$$

where, $\mathbf{v}$ is a member of the test function space with sufficient smoothness within $\Omega$ and homogeneous along the Dirichlet boundaries. Decomposing the domain into the boundary region and substrate, and using the divergence theorem on Eq. (37), we reach the weak form of the governing equation:

$$
\begin{aligned}
& \int_{\Omega_{b}} \nabla \mathbf{v}^{b}: \boldsymbol{\sigma}^{b} d \Omega+\int_{\Omega_{s}} \nabla \mathbf{v}^{s}: \boldsymbol{\sigma}^{s} d \Omega-\int_{\Gamma_{N b}} \mathbf{v}^{b} \cdot \overline{\mathbf{t}} d \Gamma-\int_{\Gamma_{N s}} \mathbf{v}^{s} \cdot \overline{\mathbf{t}} d \Gamma \\
& \quad-\int_{\Gamma_{I b}} \mathbf{v}^{b} \cdot \boldsymbol{\sigma}^{b} \cdot \mathbf{n} d \Gamma-\int_{\Gamma_{I s}} \mathbf{v}^{s} \cdot \boldsymbol{\sigma}^{s} \cdot \mathbf{n} d \Gamma-\int_{\Omega_{b}} \mathbf{v}^{b} \cdot \rho \mathbf{b} d \Omega \\
& \quad-\int_{\Omega_{s}} \mathbf{v}^{s} \cdot \rho \mathbf{b} d \Omega=0
\end{aligned}
\tag{38}
$$


![](./images/811753648840245249_9.jpg)

Fig. 9. The schematic description of the structural and the boundary scale. Alpha-case forms only at the boundary scale.

in which, superscript $b$ and $s$ denotes fields defined over the boundary region and substrate domains, respectively, colon denotes double tensor contraction, and $\Gamma_{Nb} \cup \Gamma_{Ns} \equiv \Gamma_{N}^{u}$. Using the traction continuity along the interface $(\boldsymbol{\sigma}^{s} \cdot \mathbf{n}|_{\Gamma_{Ns}} + \boldsymbol{\sigma}^{b} \cdot \mathbf{n}|_{\Gamma_{Nb}} = 0)$ and setting the internal tractions to $\mathbf{t}|_{\Gamma_{I}} = \eta(\mathbf{u}^{s} - \mathbf{u}^{b})$:

$$
\begin{aligned}
& \int_{\Omega_{b}} \nabla \mathbf{v}^{b}: \boldsymbol{\sigma}^{b} d \Omega+\int_{\Omega_{s}} \nabla \mathbf{v}^{s}: \boldsymbol{\sigma}^{s} d \Omega-\int_{\Gamma_{Nb}} \mathbf{v}^{b} \cdot \overline{\mathbf{t}} d \Gamma-\int_{\Gamma_{Ns}} \mathbf{v}^{s} \cdot \overline{\mathbf{t}} d \Gamma \\
& \quad -\int_{\Omega_{b}} \mathbf{v}^{b} \cdot \rho \mathbf{b} d \Omega-\int_{\Omega_{s}} \mathbf{v}^{s} \cdot \rho \mathbf{b} d \Omega+\delta G_{p}=0
\end{aligned}
\tag{39}
$$

with $\delta G_{p}$, the penalty contribution to bridge the scales across the boundary:

$$
\delta G_{p}=\int_{\Gamma_{I}} \eta\left(\mathbf{u}^{b}-\mathbf{u}^{s}\right)\left(\mathbf{v}^{b}-\mathbf{v}^{s}\right) d \Gamma
\tag{40}
$$

where, $\eta$ is the penalty parameter.

Bridging the boundary region and the substrate in the chemical (oxygen diffusion) and the thermal processes are formulated based on a similar penalty formulation to the formulation defined for the mechanical boundary value problem. Let $u$ denote either the oxygen concentration $c$ or the temperature field, $T$. The governing equation for the diffusion problems is expressed in the weak form as:

$$
\int_{\Omega} v \nabla \cdot(k \nabla u) d \Omega-\int_{\Omega} h v \dot{u} d \Omega=0
\tag{41}
$$

where, $v$ is the test function, $k$ denotes the thermal conductivity or the oxygen diffusivity for thermal and chemical processes, respectively. $h=\rho c_{v}$ for the thermal process and $h=1$ for the chemical process. Decomposing the structural domain into $\Omega_{b}$ and $\Omega_{s}$, and using similar arguments to those explained for the mechanical process above, the weak form of the thermal boundary value problem is expressed as:

$$
\begin{aligned}
& \int_{\Omega_{b}} \nabla v^{b} \cdot k \nabla T^{b} d \Omega+\int_{\Omega_{s}} \nabla v^{s} \cdot k \nabla T^{s} d \Omega+\int_{\Gamma_{Nb}} v^{b}\left(\beta T^{v}-T_{0}\right) d \Gamma \\
& \quad +\int_{\Gamma_{Ns}} v^{s}\left(\beta T^{s}-T_{0}\right) d \Gamma+\int_{\Omega_{b}} \rho c_{v} v^{b} \dot{T}^{b} d \Omega-\int_{\Omega_{s}} \rho c_{v} v^{s} \dot{T}^{s} d \Omega+\delta G_{p}=0
\end{aligned}
\tag{42}
$$

The oxygen diffusion problem is expressed as:

$$
\begin{aligned}
& \int_{\Omega_{b}} \nabla v^{b} \cdot D \nabla c^{b} d \Omega+\int_{\Omega_{s}} \nabla v^{s} \cdot D \nabla c^{s} d \Omega+\int_{\Omega_{b}} v^{b} \dot{c}^{b} d \Omega \\
& \quad -\int_{\Omega_{s}} v^{s} \dot{c}^{s} d \Omega+\delta G_{p}=0
\end{aligned}
\tag{43}
$$

where the penalty term is defined similar to Eq. (40):

$$
\delta G_{p}=\int_{\Gamma_{I}} \eta\left(u^{b}-u^{s}\right)\left(v^{b}-v^{s}\right) d \Gamma
\tag{44}
$$

### 5.2. Strategy to evaluate the coupled chemo-mechanical problem

The simulation of the response of titanium structures containing alpha-case requires the evaluation of the chemical, mechanical and thermal processes defined in Sections 2-4, respectively. The diffusion of heat through the structure is a significantly faster process than the diffusion of oxygen. The structure reaches the thermal steady state prior to significant oxygen infiltration into the structure. Due to the disparity between the time scales associated with the thermal and chemo-mechanical problems, it is assumed that the thermal state of the structure remains decoupled form the chemo-mechanical state. The thermal steady state of the structure is numerically evaluated prior to the chemo-mechanical processes and the computed steady state thermal field is passed to the chemo-mechanical solver as constant input.

The mechanical state of the structure is a function of the oxygen concentration field due to the embrittlement and hardening of alpha-case titanium. The diffusion characteristics of oxygen through the structure are, in return, a function of the mechanical state due to the enhancement of diffusivity in the presence of microcracks. The mechanical and chemical processes are therefore strongly coupled to each other. In this work, we employ a staggered, semi-explicit computational algorithm to solve the coupled system of diffusion and mechanical boundary value problems.

Let the displacement vector $\mathbf{u}$ be discretized using the standard finite element shape functions such that: $\mathbf{u}(\mathbf{x}, t)=\sum_{a=1}^{n} N_{a}(\mathbf{x}) \mathbf{u}_{a}(t)$. Substituting the displacement discretization into the weak form of the mechanical problem and adopting the matrix notation, we obtain:

$$
\int_{\Omega} \mathbf{B}_{a}^{t} \boldsymbol{\sigma} d \Omega+\mathbf{f}_{a}=0
\tag{45}
$$

in which, $\mathbf{B}_{a}=\nabla N_{i}$ expressed in the matrix form; superscript $t$ denotes transpose; $\mathbf{f}_{a}$ includes the forcing terms due to the boundary tractions and the body forces. The bridging between the boundary and the structural scales is omitted in Eq. (45) for simplicity of the presentation.

Substituting Eq. (19) into Eq. (18) and employing the displacement field discretization, the stress field satisfies the following rate equation:

$$
\dot{\boldsymbol{\sigma}}-\mathbf{L} \sum_{b=1}^{n} \mathbf{B}_{b} \dot{\mathbf{u}}_{b}+\mathbf{L} \dot{\boldsymbol{\varepsilon}}^{v p}=0
\tag{46}
$$

The time component of Eq. (46) is discretized based on forward Euler algorithm:

$$
\Delta \boldsymbol{\sigma}-\mathbf{L} \sum_{b=1}^{n} \mathbf{B}_{b} \Delta \mathbf{u}_{b}+\Delta t \mathbf{L}_{t} \dot{\boldsymbol{\varepsilon}}^{v p}=0
\tag{47}
$$

in which, $\Delta(\cdot) \equiv{ }_{t+\Delta t}(\cdot)-{ }_{t}(\cdot)$; left subscripts $t+\Delta t$ and $t$ denote values of the field at the current time step and the previous time step, respectively. For clarity, the left subscript for the field values at the current time step is omitted in the following presentation. Substituting Eq. (47) into Eq. (45), we obtain:

$$
\sum_{b=1}^{n} \int_{\Omega} \mathbf{B}_{a}^{t} \mathbf{L} \mathbf{B}_{b} d \Omega \Delta \mathbf{u}_{b}=\Delta t \int_{\Omega} \mathbf{B}_{a}^{t} \mathbf{L}_{t} \dot{\boldsymbol{\varepsilon}}^{v p} d \Omega-\Delta \mathbf{f}_{a}
\tag{48}
$$

in which, $\Delta \mathbf{f}_{i}$ is the external load increment at the current time step. Eq. (48) is expressed as a linear system using the standard finite element assembly procedure to evaluate the displacement increment. The resulting linear system is coupled to the chemical process

since the viscoplastic strain state is a function of the oxygen concentration.

The boundary value problem for oxygen diffusion is evaluated based on a fully implicit backward Euler time integration scheme. Discretizing the time dimension, the strong form diffusion equation (Eq. (11)) yields:
$$
c-{ }_{t} c=\Delta t \nabla \cdot(D \nabla c) \tag{49}
$$
in which, the left subscripts for the current values of the fields are omitted. The bridging between the boundary and the structural scales is omitted for simplicity of the presentation. Substituting the time discretization into the weak form of the nonlinear diffusion problem and discretizing the weak form using standard finite element shape functions $(c=\sum_{a=1}^{n} N_{a}(\mathbf{x}) c_{a}, v=\sum_{a=1}^{n} N_{a}(\mathbf{x}) v_{a})$ lead to:
$$
\begin{aligned}
\mathcal{F}_{a} \equiv & \sum_{b=1}^{n} \int_{\Theta} N_{a}(\mathbf{x}) N_{b}(\mathbf{x}) d \Omega\left(c_{b}-{ }_{t} c_{b}\right) \\
& +\Delta t \sum_{b=1}^{n} \int_{\Theta} D(c) \nabla N_{b} \nabla N_{a} d \Omega c_{b}=0
\end{aligned} \tag{50}
$$
which constitutes a nonlinear system of equations, in view of the nonlinear diffusivity, $D$. $D$ is a function of the oxygen concentration through the explicit dependence to the mechanical damage state $\omega$, whose evolution is affected by the oxygen concentration. The nonlinear system is evaluated using the Newton-Raphson algorithm:
$$
{ }^{k+1} \mathbf{c}={ }^{k} \mathbf{c}-\left.\left(\frac{d \mathbf{F}}{d \mathbf{c}}\right)\right|_{{ }^{k} \mathbf{c}} ^{-1} \mathbf{F}|_{{ }^{k} \mathbf{c}} \tag{51}
$$
in which, $\mathbf{c}=\{c_{1}, c_{2}, \ldots c_{n}\}$ and $\mathbf{F}=\{\mathcal{F}_{1}, \mathcal{F}_{2}, \ldots \mathcal{F}_{n}\}$. The left superscript denotes the iteration count for the Newton-Raphson algorithm.

The coupled chemo-mechanical boundary value problem is evaluated using the following procedure:

1. At time $t=0$, set the temperature field, $T$ to the steady state thermal response field computed by numerical evaluation of the heat diffusion equation. Initialize oxygen concentration, $c$ and displacement field, $\mathbf{u}$ based on the initial conditions of the chemical and mechanical boundary value problems, respectively.

2. Evaluate and assemble the standard stiffness matrix for the linear-elastic mechanical problem:
$$
\mathbf{K}=\mathbf{A} \sum_{b=1}^{n} \int_{\Omega} \mathbf{B}_{a}^{t} \mathbf{L} \mathbf{B}_{b} d \Omega \tag{52}
$$
in which, $\mathbf{A}$ denotes the assembly operation.

3. Advance time: $t \leftarrow t+\Delta t$.

4. Compute and assemble the forcing term of the mechanical process at the current step (the right hand side of the Eq. (48)).

5. Solve the linear system for the mechanical boundary value problem to evaluate the current incremental displacement field $\Delta \mathbf{u}_{b}$.

6. Update the nodal displacement coefficients, and the stress at the integration points of the finite element mesh:
$$
\mathbf{u}_{b}={ }_{t} \mathbf{u}_{b}+\Delta \mathbf{u}_{b} ; \quad b=1,2, \ldots, n \tag{53}
$$
$$
\boldsymbol{\sigma}={ }_{t} \boldsymbol{\sigma}+\mathbf{L} \sum_{b=1}^{n} \mathbf{B}_{b} \Delta \mathbf{u}_{b}-\Delta t \mathbf{L}_{t} \dot{\boldsymbol{\varepsilon}}^{v p} \tag{54}
$$

7. Initialize the viscoplastic strain and damage parameter for the Newton-Raphson algorithm for chemical process evaluation:
$$
{ }^{0} \boldsymbol{\varepsilon}^{v p}=\hat{\boldsymbol{\varepsilon}}^{v p}({ }_{t} \mathbf{c}, \boldsymbol{\sigma}, T) ; \quad{ }^{0} \omega=\hat{\omega}({ }_{t} \mathbf{c}, \boldsymbol{\sigma}, T,{ }^{0} \boldsymbol{\varepsilon}^{v p}) ; \quad{ }^{0} \mathbf{c}={ }_{t} \mathbf{c} ;
$$
$$
{ }^{0} D=D({ }^{0} \omega)
$$

8. Assemble $\mathbf{F}$ vector defined in Eq. (50) and its jacobian.

9. Evaluate the oxygen concentration coefficient vector at the current time step, $\mathbf{c}$ by updating the viscoplastic strain, damage and diffusivity at each iteration.

10. If end time is reached STOP.

11. Go to Step 2 for the evaluation of the next time step.

The computational algorithm includes an adaptive time stepping methodology. The time step cut-backs are introduced in case of failure of convergence in the proposed staggered evaluation procedure, whereas the time step size is adaptively increased in case of smooth response based on total number of iterations to convergence.

## 6. Numerical example

The capabilities of the proposed computational model are assessed by considering the analysis of a Ti-6Al-2Sn-4Zr-2Mo plate subjected to a thermal shock loading. The 2-D plate is illustrated in Fig. 10. The top $60 \mu \mathrm{m}$ is taken to be the boundary region and discretized finely to accurately describe the evolution of alpha-case and damage formation. The titanium substrate is discretized using relatively coarse finite elements to reduce the computational complexity of the simulations. The plate is subjected to a flux distribution along the top edge with a magnitude of $1.0 \mathrm{~W} / \mathrm{mm}^{2}$. The flux magnitude is elevated due to a shock to $6.5 \mathrm{~W} / \mathrm{mm}^{2}$ at the middle portion of the structure.The thickness of the structure is $2.286 \mathrm{~mm}$. The thermal properties of the titanium alloy are provided in Section 4. The bottom edge is assumed to remain at constant temperature of $149^{\circ} \mathrm{C}$. The steady state thermal profile of the plate under the variable flux loading is shown in Fig. 11.

The steady thermal state of the plate is employed as the initial thermal conduction of the chemo-mechanical simulations. The diffusion and mechanical properties of the plate are summarized in Tables 1 and 2, respectively. The boundary conditions for the

![](./images/811753648840245249_10.jpg)

Fig. 10. The geometry and finite element discretization of the Ti-6Al-2Sn-4Zr-2Mo subjected to thermal shock loading.

![](./images/811753648840245249_11.jpg)

Fig. 11. Steady state thermal profile.

chemo-mechanical simulation are illustrated in Fig. 10. The ambient oxygen concentration is assumed to be 10%. The structure is subjected to uniform tensile loading in the lateral direction at 0, 605, 610, 611, 612, 613, 614, 615 MPa magnitude. The application of the load is linear up to the desired amplitude within the first hour of the observation period. The loading is kept at the constant amplitude for the remainder of the observation period. The response of the structure is observed for 400 h.

Fig. 12 shows the oxygen concentration profiles within the boundary region at $t = 400$ h under stress free condition, and when the structure is subjected to 605 MPa and 615 MPa uniform uniaxial tension in the lateral direction. Alpha-case region ($c > 4.5\%$) forms around the mid-section of the titanium panel. This is due to the elevated temperatures, which results from the thermal shock applied at the center of the top boundary. At the end of the observation period, the maximum alpha-case depth was $16\ \mu\text{m}$ for the stress free configuration and the applied uniaxial stress of 605 MPa. The maximum alpha-case depth for the 615 MPa uniform tension configuration is $45\ \mu\text{m}$, which is significantly more than the lower stress conditions. We further investigated the formation of the alpha-case layer under intermediate loading amplitudes. Fig. 13 illustrates the maximum depth of alpha-case within the titanium structure as a function of the applied stress amplitude. A significant and sudden jump in the alpha-case region thickness is observed between 611–612 MPa range. The sudden jump in the alpha-case formation is due to the enhancement of oxygen diffusivity at high damage regions. The mechanical damage within the boundary region exceeds the percolation threshold for high amplitude loading conditions, which lead to significant increase in the diffusivity. This is evident in the damage and equivalent stress profiles shown in Fig. 14 under low applied stress (605 MPa) and high applied stress (615 MPa) conditions. Under low applied stress, damage is localized and has a small magnitude, which does not significantly alter the characteristics of oxygen diffusion into the structure. At high applied stress levels, significant damage develops particularly within the middle of the boundary region. The deformed equivalent stress profiles

![](./images/811753648840245249_12.jpg)

Fig. 13. The variation of the maximum alpha-case depth within the titanium structure as a function of applied stress.

![](./images/811753648840245249_13.jpg)

Fig. 12. Oxygen concentration profiles at the end of the observation period ($t = 400$ h) when the applied stress magnitude is: (a) 0 MPa, (b) 605 MPa, and (c) 615 MPa.

![](./images/811753648840245249_14.jpg)

Fig. 14. Damage and stress profiles within the titanium structure subjected to thermal shock loading at the end of the observation period ($t=400$ h): (a) Damage profile when the applied stress magnitude is 605 MPa, (b) equivalent stress profile when the applied stress magnitude is 605 MPa, (c) damage profile when the applied stress magnitude is 615 MPa, and (d) equivalent stress profile when the applied stress magnitude is 615 MPa. The deformations are amplified by a factor of 2 in (b) and (d).

(Fig. 14b and d) illustrate significant plastic deformations under high applied stress.

## 7. Conclusions and future research

In this manuscript, we presented a computational model for the analysis of failure in titanium structures subjected to combined thermo-chemo-mechanical environments. The proposed model accounts for the coupling between the thermal, chemical and mechanical processes. A generalized Johnson-Cook model is implemented to idealize the mechanical response in the presence of oxygen ingress induced alpha-case formation. An oxygen diffusivity model that accounts for the effect of mechanical damage processes is proposed. The coupled system is evaluated using a semi-explicit computational strategy. The scale bridging between the very finely discretized boundary region, within which, alpha-case forms and the titanium substrate is evaluated based on the penalty formulation. Two important issues regarding the proposed computational model remain outstanding. First, while the effect of oxygen concentration on the mechanical response is reasonably well known and validated, the effect of mechanical damage and stress on the diffusivity of titanium has not been thoroughly investigated. Particularly, experimental investigations are necessary to satisfactorily calibrate and validate the proposed model. Second, the mechanical and chemical response of titanium microconstituents, alpha- and beta-grains, grain boundaries and oxide layer are not homogeneous. The effects of the variability of properties within the heterogeneous microstructure may be explicitly incorporated through a multiscale computational model. We will concentrate our future efforts in the development of multiscale computational models and experimental verification.

### Acknowledgements

The authors gratefully acknowledge Air Force Summer Faculty Fellowship Program (AF SFFP Contract No: FA9550-09-C-0114) and Air Force Research Laboratory for support, collaboration and funding of this research.

### References

Barenblatt, G.I., Zheltov, I.P., Kochina, I.N., 1960. Basic concepts in the theory of seepage of homogeneous liquids in fissured rocks. Prikl. Mat. Mekh 24, 852-864.

Boettinger, W.J., Williams, M.E., Coriell, S.R., Kattner, U.R., Mueller, B.A., 2000. Alpha case thickness modeling in investment castings. Metall. Mater. Trans. B 31B, 1419-1427.

Bumps, E.S., Kessler, H.D., Hansen, M., 1953. The titanium-the titanium-oxygen system. Trans. ASM 45, 1008-1028.

Carranza, F.L., Haber, R.B., 1999. A numerical study of intergranular fracture and oxygen embrittlement in an elastic-viscoplastic solid. J. Mech. Phys. Solids 47, 27-58.

Chan, K.S., Koike, M., Johnson, B.W., Okabe, T., 2008. Modeling of alpha-case formation and its effects on the mechanical properties of titanium alloy castings. Metall. Mater. Trans. A 39, 171-180.

Deng, X., Fashang, M., Sutton, M.A., 2005. A damage mechanics model for creep and oxygen embrittlement in metals. Int. J. Damage Mech. 14, 101-126.

Donachie, M.J., 2000. Titanium: A Technical Guide, second ed. ASM International.

Hughes, T.J.R., 2000. The Finite Element Method: Linear Static and Dynamic Finite Element Analysis. Dover Publications.

Johnson, G.R., Cook, W.H., 1985. Fracture characteristics of three metals subjected to various strain, strain rates, temperatures and pressures. Eng. Fract. Mech. 21 (1), 31-48.

Kay, G., 2003. Failure modeling of titanium 6al-4v and aluminum 2024-t3 with the johnson-cook material model. Final report, U.S. Department of Transportation and Federal Aviation Administration.

Keanini, R.G., Watkins, G.K., Okabe, T., Koike, M., 2007. Theoretical study of alpha case formation during titanium casting. Metall. Mater. Trans. B 38, 729-732.

Krajcinovic, D., Basista, M., Mallick, K., Sumarac, D., 1992. Chemo-micromechanics of brittle solids. J. Mech. Phys. Solids 40, 965-990.

Langtangen, H.P., 2003. Computational Partial Differential Equations: Numerical Methods and Diffpack Programming. Springer.

Leyens, C., Peters, M., 2003. Titanium and Titanium Alloys. Wiley-VCH.

Liu, Z., Welsch, G., 1988. Literature survey on diffusivities of oxygen, aluminum and vanadium in alpha titanium, beta titanium, and in rutile. Metall. Trans. A 19, 1121-1125.

Ogden, H.R., Jaffe, R.I., 1955. The effects of carbon, oxygen and nitrogen on the mechanical properties of titanium and titanium alloys. TML Report 20, Titanium Metallurgical Laboratory, Battelle Memorial Institute Columbus, OH.

Owen, D.R.J., Hinton, E., 1980. Finite Elements in Plasticity: Theory and Practice. Pineridge Press Limited.

Pitt, F., Ramulu, M., 2004. Influence of grain size and microstructure on oxidation rates in titanium alloy ti-6al-4v under superplastic forming conditions. J. Mater. Eng. Perform. 13, 727-734.

Roe, W.P., Palmer, H.R., Opie, W.R., 1960. Diffusion of oxygen in alpha and beta titanium. Trans. ASM 52, 191-200.

Rosa, C.J., 1970. Oxygen diffusion in alpha and beta titanium in the temperature range of $932\ ^{\circ}\text{C}$ and $1142\ ^{\circ}\text{C}$. Metall. Trans. 1, 2517-2522.

Salganik, R.L., 1974. Transport processes in bodies with a large number of cracks. Mekhan. Tverd. Tela 27, 1534-1538.

Schuh, C., 2000. Modeling gas diffusion into metals with a moving-boundary phase transformation. Metall. Mater. Trans. A 31, 2411-2421.

Shamblen, C.E., Redden, T.K., 1968. Air contamination and embrittlement of titanium alloys. In: Jaffee, R.I., Promisel, N.E. (Eds.), The Science, Technology and Application of Titanium. Pergamon Press, New York, pp. 199-208.

Shenoy, R.N., Unnam, J., Clark, R.K., 1986. Oxidation and embrittlement of Ti-6Al-2Sn-4Zr-2Mo alloy. Oxid. Met. 26, 105-123.

Sofronis, P., McMeeking, R.M., 1989. Numerical analysis of hydrogen transport near a blunt crack tip. J. Mech. Phys. Solids 37, 317-350.

Stauffer, D., 1985. Introduction to Percolation Theory. Taylor & Francis, London.

Sung, S.-Y., Kim, Y.-J., 2005. Alpha case formation mechanism on titanium investment castings. Mater. Sci. Eng. A 405, 173-177.

Tabor, D., 1951. Hardness of Metals. Clarendon Press, Oxford.

Wood, R.A., Favor, R.J., 1972. Titanium alloys handbook. Technical Report AD0758335, Metals and Ceramics Information Center, Battelle Columbus Labs, December, 1972.