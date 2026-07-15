# Evaporation of a spherical droplet in a moderate-pressure gas

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2001 Phys.-Usp. 44 725

(http://iopscience.iop.org/1063-7869/44/7/A03)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 160.36.178.25
This content was downloaded on 26/12/2014 at 18:03

Please note that terms and conditions apply.

**METHODOLOGICAL NOTES**
PACS numbers: 68.10.Jy, 82.70.Rr, 92.60.Jq

# Evaporation of a spherical droplet in a moderate-pressure gas

A V Kozyrev, A G Sitnikov

DOI: 10.1070/PU2001v044n07ABEH000953

## Contents
1. Introduction 725
2. Diffusion model of droplet evaporation 726
    2.1 Statement of the problem and main approximations; 2.2 Boundary conditions for the diffusion model
3. Theory of the evaporation process 728
    3.1 Calculation of the temperature of an evaporating droplet; 3.2 Calculation of the vapor tension near the droplet surface; 3.3 Calculation of the evaporation time of a droplet
4. Discussion of the results 729
    4.1 Analysis of the applicability limits of the problem; 4.2 Two regimes of evaporation of a droplet; 4.3 Parameters of the evaporation process for droplets of mercury, water and hexane; 4.4 Evaporation of water droplets; 4.5 Growth and evaporation of droplets in the neighborhood of the dew point
5. Conclusions 733
References 733

**Abstract.** A diffusion model for the evaporation of a single spherical droplet is examined taking into account the reduction in the droplet temperature and vapor pressure near its surface, for arbitrary condensation and surface tension coefficients. Quite general analytical expressions for the dependence of the lifetime of a droplet on its initial radius are derived for the first time. This model makes it possible to estimate the condensation coefficient of the vapor molecules from the experimental form of this dependence.

## 1. Introduction
Droplet aerosols are important in many branches of science and technology, such as chemistry, medicine, the physics of the atmosphere, and heat and power engineering [1, 2]. The problem of aerosol formation is also important in connection with the intensive study of plasma chemical processes in gas discharge, in which, as a rule, a broad spectrum of products is formed [3]. Naturally, each of these has its own value of the relative vapor tension with respect to the equilibrium state. It is often necessary to estimate the time of formation or complete evaporation of such an aerosol.

One should pay special attention to the formation of a nonequilibrium aerosol in an electric discharge. In Refs [4, 5] experiments are described in which the corona — streamer discharge in a mixture of gases at the atmospheric pressure first gives rise to the formation of an aerosol by stimulated condensation of unsaturated vapor on ions, and, after the discharge stops, the aerosol slowly evaporates. Although the vapor pressure of volatile liquids in these experiments was just a few percent of the pressure of saturation, the time of evaporation of the aerosol was abnormally large and amounted to tens of minutes. The classical theory of evaporation can explain neither the process of the fast growth of an aerosol in an unsaturated vapor nor its subsequent slow evaporation. Observe that the process of formation of an aerosol in a gas discharge is totally different from the kinetics of atmospheric water aerosol. The latter depends mainly on the process of formation and condensation growth of nuclei of the new phase from the supersaturated vapor against the background of slowly varying conditions in the gas phase [6]. In contrast, the aerosol in the low-temperature plasma of a gas discharge has no shortage of primary nuclei, because this role is efficiently performed by numerous ions. The main processes that determine the growth of droplets in the recombining plasma are the competing processes of coagulation and evaporation of droplets.

Before describing the process of growth and evaporation of an aerosol as a collective of particles over a broad size range, we need to identify the physical factors that influence the process of evaporation of a single droplet of liquid — that is, one needs to be able to calculate, as accurately as possible, the process of growth of an individual droplet under the given conditions of the external environment.

Despite the simplicity of the statement of the problem, its solution in the general case runs into difficulties. This may be the reason why the theory of evaporation of a droplet has not found its way into the university textbooks. We hope that this paper will at least partially fill this gap in the curriculum of general and molecular physics.

The problem of evaporation of a single spherical droplet in a medium with given parameters can be regarded as

---
A V Kozyrev, A G Sitnikov Institute of High Current Electronics,
Siberian Branch of the Russian Academy of Sciences
Akademicheskii prosp. 4, 634055 Tomsk, Russian Federation
Tel. (7-3822) 25 84 11
E-mail: kozyrev@to.hcei.tsc.ru; alex@to.hcei.tsc.ru
Tel. (7-095) 135 05 51

Received 9 February 2001, revised 22 May 2001
Uspekhi Fizicheskikh Nauk 171 (7) 765–774 (2001)
Translated by A S Dobroslavskii; edited by A V Getling

classical. In its simplest form it was solved by Maxwell in 1877 [7]. Using the equations of diffusion and continuity of the molecular flux for a spherically symmetrical geometry,

$$
w(r)=-D \frac{\partial n}{\partial r}, \quad W=4 \pi r^{2} w(r)=-\left.4 \pi D R^{2} \frac{\partial n}{\partial r}\right|_{r=R}, \quad(1)
$$

Maxwell derived the known expression for the flux $W$ of particles evaporated from the droplet:

$$
W=4 \pi D R\left(n_{R}-n_{0}\right). \quad(2)
$$

Here $D$ is the coefficient of diffusion of vapor molecules in the surrounding gas and $n_{R}$ and $n_{0}$ are the concentrations of particles near the surface of the droplet and at infinity, respectively.

It would seem that, knowing the total flux of evaporated molecules (2), one can easily calculate the so-called lifetime of a droplet with initial radius $R_{0}$. It turns out, however, that such a statement of the problem is oversimplified. For example, Maxwell assumed that the vapor near the surface of the droplet is always saturated, and therefore $n_{R}=n_{\mathrm{s}}(T)$. Here $n_{\mathrm{s}}(T)$ is the equilibrium concentration of vapor molecules just above the surface of the liquid phase at temperature $T$. Firstly, however, the vapor at the surface will be saturated only if the rate of supply of molecules from the surface of the droplet is large enough compared with the rate of their diffusive escape. In general, this is not the case. Secondly, evaporation leads to the removal of energy from the droplet and must be accompanied by a reduction of its temperature with respect to the temperature of the surrounding medium. This implies that the concentration $n_{\mathrm{s}}$ of saturated vapor near the surface will be determined not by the preset temperature of the surrounding gas $T$, but rather by the unknown temperature of the droplet $T_{R}$, and $n_{\mathrm{s}}(T)$ is an exponential function of temperature. Because of this, even the neglect of only this feature of evaporation makes Maxwell's formula (2) very crude.

One of the refinements in the theory of evaporation is associated with the kinetics of the process of interaction of vapor molecules with the surface of the liquid phase. Hertz and Knudsen, using the equation of state of an ideal gas for the vapor and the principle of detailed equilibrium, obtained the following formula for the density $w_{\mathrm{s}}$ of the flux of vapor molecules from the surface [8]:

$$
w_{\mathrm{s}}(T)=\frac{\alpha_{\mathrm{c}} P_{\mathrm{s}}(T)}{\sqrt{2 \pi M k T}}, \quad(3)
$$

where $P_{\mathrm{s}}(T)=n_{\mathrm{s}} k T$ is the pressure of saturated vapor at temperature $T, M$ is the mass of evaporating molecules, $\alpha_{\mathrm{c}}$ is the coefficient of condensation, which equals the probability of a vapor molecule incident on the surface of the condensed phase not being reflected.

Book [8] contains an indication of the low values of the coefficient of condensation for water and some organic liquids. For pure water it is usual to set $\alpha_{\mathrm{c}} \approx 0.04$, and for most other substances $\alpha_{\mathrm{c}} \simeq 1$. It is hard to find any consistent figures for $\alpha_{\mathrm{c}}$ for different media in handbooks, which can be explained by the fact that this coefficient is strongly affected by the presence of small uncontrollable impurities. In particular, it was Knudsen who reported strong variations in the rate of evaporation of droplets of mercury as the latter were even slightly oxidized [8]. The authors of monograph [1] also point out a considerable decrease in the rate of evaporation of water droplets even in the presence of small amounts of surfactants. It would be reasonable to assume that impurities of this kind mainly alter the coefficient of condensation. Note that Maxwell's classical theory of evaporation does not resolve this problem, since it predicts the independence of the evaporation rate for a droplet on the condensation coefficient [7]. Accordingly, one of the tasks of this paper consists in identifying the conditions under which the coefficient of condensation will considerably affect the rate of evaporation. Given the availability of a sufficiently general theory, the knowledge of such conditions would make it possible to measure indirectly the coefficient of condensation from experimental data about the rate of evaporation of a droplet.

An integral part of the theory of evaporation is the description of the escape of evaporated particles from the surface. The formation of a diffusive flux of vapor molecules occurs at a distance approximately equal to the mean free path $\bar{l}$ from the surface of the liquid phase. A correct theory of evaporation must include a kinetic description of the molecular flow [9]. The pattern of vapor flow near the spherical droplet must depend on the droplet radius $R$, or, to be more precise, on the Knudsen number $\mathrm{Kn}=\bar{l} / R$. The calculation of the vapor flow becomes much simpler in the approximation of a continuous medium, with $\mathrm{Kn} \ll 1$.

The next refinement of the model should be a consistent description of the process of energy exchange between gas molecules and the condensed phase at the interface. Strictly speaking, near the interface the velocity distribution function of gas molecules is not equilibrated and needs to be determined, but, for the sake of simplicity, the gas is often characterized by a certain effective temperature. In the general case, this temperature near the surface must lie in between the temperature of the surface of the liquid phase and the gas temperature away from the surface.

Finally, a consistent theory of evaporation of a droplet must also take into account the existence of the free energy of the surface, because it is this energy that determines the pressure of saturated vapor above the curved interface.

From this brief review of the problem we see that even a slight refinement of the theory of evaporation considerably complicates the relevant equations. Textbooks, monographs and reviews only cite solutions to these equations for particular extreme or special cases, because the general solution can only be obtained by numerical methods. As a rule, however, numerical results give much less insight than analytical expressions, and lack universality.

For methodological purposes it seems expedient to formulate a relatively simple model of evaporation of a droplet, which would be capable of analytically taking into account the most important factors affecting the evaporation time — the temperature decrease in the course of evaporation, the surface tension of the liquid phase, the reduced vapor pressure near the surface, and the effects of the condensation coefficient. As will be shown below, all these requirements are satisfied by the diffusion model of droplet evaporation.

## 2. Diffusion model of droplet evaporation

### 2.1 Statement of the problem and main approximations
Consider a single spherical droplet of radius $R$, placed in an unbounded atmosphere of a chemically inert gas that contains the vapor of the substance of the droplet with the

relative pressure $f_0$. Here and below we denote any parameter $p$ of the problem by $p_0$ away from the droplet and by $p_R$ near the evaporation surface.

The geometry of the problem is assumed to be spherically symmetrical — that is, we only consider the radial profiles of temperature and vapor concentration. The origin of the radial coordinate is fixed at the center of the droplet. The ambient temperature $T_0$ and the concentration $n_0$ of vapor at infinity are constant and fixed. Accordingly, the relative vapor tension (relative humidity in the case of water vapor) at infinity is also constant and fixed, $f_0 = n_0/n_\text{s}(T_0)$.

We also assume that, always, $T_R \approx T_0$. This assumption will considerably simplify our calculations, allowing us to use the linear approximation for the temperature dependence of the saturated vapor pressure $P_\text{s}(T)$, without limiting too much the applicability of our model. In this way, from the start we exclude the process of fast evaporation, which entails a strong cooling of the droplet, from consideration.

In analytical models, evaporation is usually considered without taking into account the effects of surface tension on the rate of evaporation. Indeed, this effect can be neglected for not very small droplets far from the dew point. Near the dew point, however, this effect cannot be neglected because the so-called critical radius strongly depends on the free energy of the interface [1, 10]. From the outset we shall take into account the effects of the surface tension $\sigma$ on the saturated vapor pressure $P_\text{s}$ near the spherical surface of the liquid.

To calculate the flux of molecules and heat, we use the approximation of a continuous medium, which holds for sufficiently large droplets. We assume as known the coefficient of diffusion of vapor molecules in the surrounding gas $D$, the heat conductivity of the gas $\lambda$, the coefficient of condensation for the liquid $\alpha_\text{c}$, the vaporization heat per molecule $L_0$ at temperature $T_0$, and the saturated-vapor pressure as a function of temperature $P_\text{s}(T)$. The transport coefficients can be assumed constant if the concentration of vapor molecules is always much smaller than the concentration of molecules of the ambient gas. In other words, we assume that the ambient temperature $T_0$ is low compared with the boiling point of the droplet material.

In our description of diffusion and heat conduction we assume that all profiles of concentration and temperature are quasi-stationary, and in our calculation they will not show an explicit dependence on the time. This assumption is reasonable as long as the characteristic time $\tau$ of variation of the droplet radius $R$ satisfies the condition

$$
\tau \gg \frac{R^2}{D} . \tag{4}
$$

All of the above assumptions fit the real situation well for gas pressures of the order of the atmospheric pressure.

### 2.2 Boundary conditions for the diffusion model
In our description of the fluxes of vapor and heat we confine ourselves to the simplest assumptions — the linear diffusion of molecules and the supply of energy to the evaporating droplet by heat conduction. The equations of diffusion and heat conduction require quite definite boundary conditions. Figure 1 shows the profiles of concentration of vapor and temperature near the evaporating droplet. Far from the droplet, for $r \to \infty$, these conditions are quite obvious: $n \to n_0$, and $T \to T_0$.

![](./images/812459960758697984_1.jpg)

**Figure 1.** Parameters of the problem and notation.

A characteristic feature of the statement of the problem in the diffusion approximation are the jumps of concentration and temperature at the interface. The existence of such jumps was first noted by Langmuir in 1915. The jumps of concentration and temperature are usually not defined in the framework of the diffusion approximation and are regarded as additional parameters of the problem [7].

In this work we assume the coefficient of condensation of molecules $\alpha_\text{c}$ to be known and independent of the radius of the droplet, because in our approximation the radius of the droplet is fairly large: $R \gg \bar{l}$.

To describe the heat exchange on the surface of a droplet, we introduce the coefficient $\alpha_\text{t}$ that characterizes the temperature difference between the liquid and gas at the interface. Since the equation of heat conduction coincides in form with the diffusion equation (1), the total energy flux to the evaporating droplet $Q$ will be expressed in the same way as the flux of particles in (2):

$$
Q = 4\pi\alpha_\text{t}\lambda R(T_0 - T_R) , \tag{5}
$$

where $\lambda$ is the heat conductivity of the buffer gas.

From Fig. 1 we can see that the actual heat flux to the droplet depends not on the difference $T_0 - T_R$, but rather on $T_0 - T_R'$. This possible distinction, $T_R' \neq T_R$, is reflected in equation (5) by the coefficient $\alpha_\text{t} \neq 1$. Such an introduction of coefficient $\alpha_\text{t}$ is equivalent to the following definition: $\alpha_\text{t} = (T_0 - T_R')/(T_0 - T_R)$. We assume that this coefficient is a constant parameter of the problem, which is justified by the relatively narrow range of variation of the temperature of the droplet in the course of evaporation.

Observe that the jump of concentration and the jump of temperature near the surface of the droplet are described in entirely different ways. The jump of concentration depends on the current radius of the evaporating droplet, and changes in the course of evaporation. Accordingly, we have to calculate it specially. In contrast, we regard the relative temperature jump $\alpha_\text{t}$ as a constant parameter that does not change in the course of evaporation.

In the framework of the diffusion model, the two constant coefficients, $\alpha_\text{c}$ and $\alpha_\text{t}$, can be regarded as the adjustment parameters of the model that should be defined either from the condition of best fit with experimental data or from a comparison with a more comprehensive theory that consistently describes the physical aspects of interaction of vapor and gas molecules with the surface of condensed phase.

## 3. Theory of the evaporation process

### 3.1 Calculation of the temperature of an evaporating droplet
The concentration of particles near the droplet surface, $n_R$, and at infinity, $n_0$, can be expressed in terms of the saturated vapor pressure and the relative vapor tension:
$$
n_R = f_R \frac{P_\mathrm{s}(T_R)}{kT_R} \,, \quad n_0 = f_0 \frac{P_\mathrm{s}(T_0)}{kT_0} \,,
\tag{6}
$$
where $f_R$ and $f_0$ are the relative vapor tensions at the surface and at infinity, respectively, and $k$ is Boltzmann's constant.

From (2) and (6) we express the flux of particles
$$
W = 4\pi D R \frac{P_\mathrm{s}(T_0)}{kT_0} \left( f_R \frac{P_\mathrm{s}(T_R)T_0}{P_\mathrm{s}(T_0)T_R} - f_0 \right) .
\tag{7}
$$

If we assume that the saturated vapor tension $P_\mathrm{s}(T)$ depends on the temperature as $\exp(-L_0/(kT))$ and $T_R \approx T_0$, then with due account for the curvature of the droplet surface, the ratio of saturated vapor pressures can be approximated as
$$
\frac{P_\mathrm{s}(T_R)}{P_\mathrm{s}(T_0)} \simeq 1 + \frac{L_0}{kT_R} \frac{T_R - T_0}{T_0} + \frac{R_\sigma}{R} .
\tag{8}
$$

Here we have used the known formula of Thomson (Kelvin) for the saturated vapor pressure over a curved surface, and introduced the notation for the characteristic radius $R_\sigma = 2\sigma v_\mu/(kT_0)$, where $\sigma$ is the surface tension, and $v_\mu$ is the mean volume occupied by one molecule of the liquid phase.

Upon substituting (8) into (7), with the same accuracy for the flux of particles we obtain
$$
W = 4\pi D R \frac{P_\mathrm{s}(T_0)}{kT_0} \left( f_R - f_0 + \omega f_R \frac{T_R - T_0}{T_R} + f_R \frac{T_0}{T_R} \frac{R_\sigma}{R} \right) ,
\tag{9}
$$
where for compactness we use the notation $\omega \equiv L_0/(kT_R) - 1$.

From the energy flux (5), we can find the linkage between the rate of decrease of the droplet volume and the difference of temperatures:
$$
\frac{\mathrm{d}V}{\mathrm{d}t} = 4\pi R^2 \frac{\mathrm{d}R}{\mathrm{d}t} = -\frac{QM}{L_0\rho} = 4\pi \alpha_t \lambda R \frac{M}{L_0\rho} \left( T_R - T_0 \right) , \tag{10}
$$
where $M$ and $\rho$ are the mass of the evaporating molecules and the density of the liquid phase, respectively. From (10) we obtain the relative temperature difference
$$
\frac{T_R - T_0}{T_R} = \frac{\rho k(\omega + 1)}{\alpha_t \lambda M} R \frac{\mathrm{d}R}{\mathrm{d}t} .
\tag{11}
$$

Knowing the flow of evaporating particles enables us to find the rate of reduction of the droplet volume:
$$
\frac{\mathrm{d}V}{\mathrm{d}t} = 4\pi R^2 \frac{\mathrm{d}R}{\mathrm{d}t} = -W \frac{M}{\rho} .
\tag{12}
$$

Substituting expression (9) into the right-hand side of this equation yields for the radius of the droplet:
$$
R \frac{\mathrm{d}R}{\mathrm{d}t} = -\frac{DM}{\rho} \frac{P_\mathrm{s}(T_0)}{kT_0} \left( f_R - f_0 + \omega f_R \frac{T_R - T_0}{T_R} + f_R \frac{T_0}{T_R} \frac{R_\sigma}{R} \right) .
\tag{13}
$$

Upon substituting (11) into (13), we can find an explicit expression for the rate of variation of the droplet radius:
$$
\begin{aligned}
R \frac{\mathrm{d}R}{\mathrm{d}t} &= -\frac{DM}{\rho} \frac{P_\mathrm{s}(T_0)}{kT_0} \left[ f_R \left( 1 + \frac{R_\sigma}{R} \right) - f_0 \right] \\
&\quad \times \left[ 1 + \frac{D P_\mathrm{s}(T_0)(\omega + 1)}{\alpha_t \lambda T_0} f_R \left( \omega - \frac{R_\sigma}{R} \right) \right]^{-1} . \quad (14)
\end{aligned}
$$

It is expedient to introduce a new dimensionless parameter of the problem $a$, which characterizes the relative effects of diffusion and heat conduction on the rate of evaporation of the droplet:
$$
a \stackrel{\text{def}}{\equiv} \frac{\alpha_t \lambda T_0}{D P_\mathrm{s}(T_0) \omega (\omega + 1)} .
\tag{15}
$$

By substituting (14) into (11), we can estimate the difference between the temperature of the surface of evaporation and the ambient temperature:
$$
z \equiv \frac{T_0 - T_R}{T_R} = \frac{R(f_R - f_0) + f_R R_\sigma}{\omega R(f_R + a) - f_R R_\sigma} ,
\tag{16}
$$
where $f_R$ is yet to be defined.

### 3.2 Calculation of the vapor tension near the droplet surface
Now let us calculate the relative vapor tension near the surface of the droplet, $f_R$. This quantity is often taken to be equal to unity or calculated from kinetic theory. Sometimes the calculation is simplified by introducing the intermediate layer that hosts the surface concentration jump [7]. We shall calculate $f_R$ from the natural condition of equality of the particle fluxes near the surface and at infinity.

From (12) we express the flux of evaporated particles in terms of the rate of variation of the radius of the droplet:
$$
w = \frac{W}{4\pi R^2} = -\frac{\rho}{M} \frac{\mathrm{d}R}{\mathrm{d}t} .
\tag{17}
$$

On the other hand, the flux of evaporated particles can be found from (3) and (8):
$$
\begin{aligned}
w &= \frac{\alpha_c P_\mathrm{s}(T_R)}{\sqrt{2\pi M k T_R}} \left( 1 - f_R \right) \\
&\quad \approx w_\mathrm{s}(T_0) \left( 1 + \frac{R_\sigma}{R} - (\omega + 1) \frac{z}{z + 1} \right) (1 - f_R) . \quad (18)
\end{aligned}
$$

By means of equating (17) and (18) and substituting (14) and (16) into the resulting expression, we get the equation for the relative humidity $f_R$ near the surface of the droplet:
$$
\begin{aligned}
-\frac{\rho}{M w_\mathrm{s}(T_0)} R \frac{\mathrm{d}R}{\mathrm{d}t} &= \frac{[(R + R_\sigma)(z + 1) - z R(\omega + 1)](1 - f_R)}{z + 1} \\
&= \frac{\alpha_t \lambda}{k w_\mathrm{s}(T_0)(\omega + 1)} z .
\tag{19}
\end{aligned}
$$

We introduce the parameter $b$ with the dimension of length, the parameter $\tau$ with the dimension of time, and the dimensionless parameter $\beta$ describing the surface tension:
$$
b \stackrel{\text{def}}{\equiv} \frac{\alpha_t \lambda}{k w_\mathrm{s}(T_0) \omega (\omega + 1)(a + 1)} , \quad
\tau \stackrel{\text{def}}{\equiv} b^2 \frac{\rho k(\omega + 1)}{\alpha_t \lambda M} , \quad
\beta \stackrel{\text{def}}{\equiv} \frac{R_\sigma}{b \omega (a + 1)} .
\tag{20}
$$

It is convenient to regard the parameters $b$ and $\tau$ as the characteristic scales of radius and time. Therefore, below we shall consider the radius $R$ and the time $t$ to be dimensionless. Then equation (19) becomes

$$
-R \frac{\mathrm{d} R}{\mathrm{~d} t}=\frac{\{[R+\beta \omega(a+1)](z+1)-z R(\omega+1)\}\left(1-f_{R}\right)}{\omega(a+1)(z+1)}=z.
\tag{21}
$$

From (16) we express the relative tension near the surface in terms of the relative temperature difference $z$:

$$
f_{R}=\frac{R\left(f_{0}+a \omega z\right)}{[R+\beta \omega(a+1)](z+1)-z R(\omega+1)},
\tag{22}
$$

and substitute it into (21). As a result, we obtain the desired equations that link the two quantities, $R$ and $z$:

$$
R(z)=\frac{(z-\beta)(z+1)}{\varphi_{0}-z}, \quad \varphi_{0}=\frac{1-f_{0}}{\omega(a+1)},
\tag{23}
$$

$$
z(R)=\frac{1}{2}\left[\sqrt{R^{2}+2 R\left(1-\beta+2 \varphi_{0}\right)+(1+\beta)^{2}}-R-1+\beta\right].
\tag{24}
$$

As a result of these manipulations we get the explicit expression (24) for the relative temperature difference between the droplet and environment.

The relative tension $f_{R}(R)$ is related to the function $z$ by expression (22). If we expand $z$ in a Taylor series in $\beta$ and $\varphi_{0}$ near the point $\beta=0, \varphi_{0}=0$ to the square term inclusive, we get the following approximate expansion, which will considerably facilitate our analysis of expression (24):

$$
z(R) \approx \frac{R \varphi_{0}+\beta}{R+1}\left(1+\frac{R\left(\beta-\varphi_{0}\right)}{(R+1)^{2}}\right).
\tag{25}
$$

### 3.3 Calculation of the evaporation time of a droplet
The differential equation for the radius of the droplet (21) can be easily integrated if we go to the new variable $z$, because the function $R(z)$ is already determined in (23). Such a substitution of variables leads to a differential equation with separable variables:

$$
\begin{aligned}
& -\frac{R}{z} \frac{\mathrm{d} R}{\mathrm{~d} t}=-\frac{R(z)}{z} \frac{\mathrm{d} R(z)}{\mathrm{d} z} \frac{\mathrm{d} z}{\mathrm{~d} t} \\
& \quad=\frac{(z-\beta)(z+1)\left[z^{2}-2 z \varphi_{0}-\varphi_{0}+\beta\left(\varphi_{0}+1\right)\right]}{z\left(\varphi_{0}-z\right)^{3}} \frac{\mathrm{d} z}{\mathrm{~d} t}=1,
\end{aligned}
\tag{26}
$$

which integrates to the explicit primitive

$$
\begin{aligned}
t(z(R)) & =\frac{1}{2} \frac{1}{\varphi_{0}^{2}\left(z-\varphi_{0}\right)^{2}} \\
& \times\left\{\beta\left(\varphi_{0}+1\right)\left[2 \varphi_{0}\left(\varphi_{0} z+2 \varphi_{0}-z\right)+\beta\left(2 z-3 \varphi_{0}-\varphi_{0}^{2}\right)\right]\right. \\
& \left.-\varphi_{0}^{2}\left[2 \varphi_{0} z+\varphi_{0}+4 \varphi_{0}^{2} z-4 \varphi_{0} z^{2}+2 z^{3}-\varphi_{0}^{3}\right]\right\} \\
& -\frac{\left(\varphi_{0}+1\right)\left(\varphi_{0}^{2}+\beta\right)\left(\varphi_{0}-\beta\right)}{\varphi_{0}^{3}} \ln \left|\varphi_{0}-z\right| \\
& -\frac{\beta\left[\beta\left(\varphi_{0}+1\right)-\varphi_{0}\right]}{\varphi_{0}^{3}} \ln |z|+\text { const }.
\end{aligned}
\tag{27}
$$

The time in which the radius of the droplet reduces from $R$ to $R_{0}$ can be found simply by finding the difference of primitives at these arguments:

$$
\theta\left(R, R_{0}\right)=\left.t(z(R))\right|_{R} ^{R_{0}}.
\tag{28}
$$

For practical calculations it is convenient to have an estimate for the time of the complete evaporation of the droplet. The lifetime of the droplet $\theta$ as an explicit function of the initial radius $R$ can be found from (28) substituting $R_{0}=0$:

$$
\begin{aligned}
\theta= & \left.t(z(R))\right|_{R} ^{0}=\frac{1}{2} \frac{z-\beta}{\varphi_{0}^{2}\left(\varphi_{0}-z\right)^{2}} \\
& \times\left\{\varphi_{0}\left[2 \varphi_{0} z^{2}-z\left(3 \varphi_{0}^{2}+1\right)+2 \varphi_{0}\left(\varphi_{0}^{2}+\varphi_{0}+1\right)\right]\right. \\
& \left.-\beta\left[\varphi_{0}\left(\varphi_{0}^{2}+4 \varphi_{0}+3\right)-2 z\left(\varphi_{0}+1\right)\right]\right\} \\
& -\frac{\left(\varphi_{0}+1\right)\left(\varphi_{0}^{2}+\beta\right)\left(\varphi_{0}-\beta\right)}{\varphi_{0}^{3}} \ln \left(\frac{\varphi_{0}-\beta}{\varphi_{0}-z}\right) \\
& -\frac{\beta\left[\beta\left(\varphi_{0}+1\right)-\varphi_{0}\right]}{\varphi_{0}^{3}} \ln \frac{\beta}{z},
\end{aligned}
\tag{29}
$$

where the function $z(R)$ is defined in (24). Although the diffusion theory developed here does not hold for small droplets, for the sake of simplicity we have extended the limit of integration to $R=0$, because the time of evaporation of a tiny droplet with size $R \leqslant \bar{l}$ is negligibly small compared with the total lifetime of a droplet with the initial size $R \gg \bar{l}$.

## 4. Discussion of the results

### 4.1 Analysis of the applicability limits of the problem
Let us use our results to redefine the criterion of steadiness of process (4). Upon substituting the characteristic scales of the problem $b$, $\tau$ from (20) into (4) and using the kinetic expressions for $\lambda$ and $D$, we write the criterion in the form

$$
\frac{k D \rho}{\alpha_{\mathrm{t}} \lambda M} \omega(\omega+1) \simeq \frac{\rho}{\rho_{\mathrm{g}}} \frac{\omega^{2}}{\alpha_{\mathrm{t}}} \sqrt{\frac{M_{\mathrm{g}}}{M+M_{\mathrm{g}}}} \gg 1.
\tag{30}
$$

Here $\rho_{\mathrm{g}}$ is the density of the gas medium, and $M_{\mathrm{g}}$ is the mean mass of molecules of the gas medium. Since $\omega \gg 1$, we can safely assume that criterion (30) is satisfied with a good margin of several orders of magnitude.

Strictly speaking, one must also check that the temperature regime within the droplet is quasi-stationary. We assume that the temperature of the liquid phase inside the droplet is everywhere the same, and at any time is determined by the current radius of the droplet (24). The variation of temperature across a droplet of liquid with specific heat $c$, density $\rho$, and heat conductivity $\lambda_{1}$ in our case can obviously be regarded as negligible:

$$
\frac{\Delta T}{T} \simeq \frac{c \rho b^{2}}{\lambda_{1} \tau} \simeq \frac{\alpha_{\mathrm{t}}}{\omega} \frac{\lambda}{\lambda_{1}} \ll 1.
\tag{31}
$$

Let us fathom the applicability of expansion (8). The approximation is good as long as the discarded term is much

smaller than the retained term:

$$
\left| -(\omega+1)z+\frac{R_{\sigma}}{R} \right| \ll 2.
$$

Let us first analyze the situation with the surface tension neglected — that is, assuming that $\beta=0$ everywhere. In view of (25), we reduce the criterion of applicability of expansion (8) to the inequality

$$
|1-f_0| \ll 2(a+1)\left(1+\frac{1}{R}\right), \tag{32}
$$

which is stronger, the larger the dimensionless parameter $a$. The inclusion of surface tension will only reduce the discarded term, because for the evaporating droplet the term with the temperature and the term with surface tension have opposite signs. Because of this, the necessary and sufficient condition of applicability of the expansion consists in the simultaneous satisfaction of two inequalities, (32) and $R \gg \beta$.

### 4.2 Two regimes of evaporation of a droplet
The proposed theory of evaporation allows us to describe two basically different regimes of evaporation of a droplet.

Let us look into the situation in which the relative pressure of vapor in the environment is far from saturation, so that $\varphi_0 \gg \beta$. In this case we can neglect the effects of surface tension on the rate of evaporation of the droplet. Then the general formula for the lifetime of the droplet (29) for the extreme cases of large and small initial radii can be written in the form of asymptotic expansions,

$$
\theta(R) \approx \frac{1}{\varphi_0}
\begin{cases}
R+\frac{1}{2}(1-\varphi_0-2\varphi_0^2)R^2 & \text{for } R \ll 1, \\
\frac{1}{2}R^2+\frac{1+2\varphi_0-\varphi_0^2}{1+\varphi_0}R & \text{for } R \gg 1.
\end{cases} \tag{33}
$$

From these expressions we can see that in the limit of large droplets we have the well-known dependence of the time of evaporation of the droplet on the squared radius, while in the limit of small droplets the time of evaporation is a linear function of the initial radius. The reasons for such a deviation from Maxwell's theory are illustrated in Fig. 2, which shows universal approximate curves of the relative vapor tension near the surface of evaporation versus the radius of the droplet:

$$
f_R \approx \frac{x+f_0}{x+1}, \quad x=R\frac{a+f_0}{a+1}. \tag{34}
$$

![](./images/812459960758697984_2.jpg)

Figure 2. Relative vapor tension near the surface of the droplet $f_R$ vs. the dimensionless radius $x$ at different values of $f_0$.

They were obtained from expression (22) by substituting only the linear (with respect to $R$) term of expansion $z(R)$ from (25).

As the radius of the droplet decreases, the probability of the recapture of evaporated molecules decreases dramatically, and, because of the limited rate of supply of new molecules to the surface, the pressure of vapor above the surface decreases and eventually tends to $f_0$. The rate of evaporation of small droplets is therefore limited not by the process of diffusive escape of evaporated molecules, but rather by the rate of release of molecules from the surface. Accordingly, such a regime of evaporation can be called the regime of depletion as compared with Maxwell's classical regime. If the droplet is sufficiently small, the relative pressure of vapor near the surface is reduced, and the temperature of a small droplet is slightly higher than the temperature of larger droplets. These factors lead to a considerable increase in the evaporation time as compared with the predictions of Maxwell's theory. The magnitude of $\alpha_{\rm c}$ has an especially strong effect on the rate of evaporation of a droplet in the regime of depletion.

Let us estimate the absolute size of a droplet $r_0$ at which the relative vapor tension in the neighborhood of the droplet is reduced. For simplicity, we set $f_0=0$; then from (34) we can easily find that the two-fold reduction of the relative vapor tension $f_R$ above the droplet (from 1 to 1/2) corresponds to the following absolute magnitude of the droplet radius:

$$
r_0 \approx \frac{b(a+1)}{a} = \frac{4D}{\alpha_{\rm c}\bar{v}} = \frac{4\bar{l}}{3\alpha_{\rm c}}, \tag{35}
$$

where $\bar{v}=\sqrt{8kT_0/(\pi M)}$ is the mean velocity. Here we have used expressions (15) and (20) for the parameters $a$ and $b$, and the approximate expression for the diffusion coefficient $D \approx \bar{l}\bar{v}/3$. Observe that, within the framework of the diffusion model, we have actually arrived at the same value of $r_0$ that has usually been derived from kinetic considerations [11].

Thus, the characteristic radius $r_0$, at which the Maxwell regime of evaporation is replaced by the depletion regime, depends explicitly on the condensation coefficient $\alpha_{\rm c}$. This gives an opportunity for measuring the coefficient of condensation by comparing the experimental and calculated lifetimes of the droplet as functions of its radius.

Of course, the dependence (29) obtained in the diffusion approximation only holds for $R \gg \bar{l}$, and the transition to the depletion regime occurs for very small droplets, whose individual sizes are virtually impossible to measure experimentally. However, at very small values of $\alpha_{\rm c} \ll 1$, for example, in the case where a volatile liquid is covered with a film of nonvolatile surfactant, the transition to the depletion regime should occur even with rather large droplets, $r_0 \gg \bar{l}$. There are indications, for example, that the evaporation rate of droplets of some very dilute water solutions is hundreds or even thousands of times lower than that of droplets of pure water [1]. This means that even for droplets measuring tens to hundreds of micrometers, the complete evaporation time proportional to the squared initial radius is gradually

replaced by a linear dependence on $R$ [formula (33)]. In this case one can adjust the condensation coefficient so as to align the theoretical curve (29) with the measured curve, and thus measure indirectly the coefficient of condensation. Such experiments are quite feasible, all the more so because not only the radius $r_0$ but also the characteristic time of evaporation increase as the condensation coefficient increases, since $\tau \propto 1/\alpha_{\rm c}^2$. The smaller $\alpha_{\rm c}$, the larger the radius at which our curve (29) begins to deviate from Maxwell's theory. Observe that it is the availability of an analytical expression for the droplet's lifetime that makes such a comparison between theory and experiment practically efficient.

### 4.3 Parameters of the evaporation process for droplets of mercury, water and hexane
Let us now perform a comparative analysis of the process of evaporation for three substances: water, mercury and $n$-hexane. The physical properties of these substances are highly different, which will help us to prove the universality of our theory. For $n$-hexane, the vapor tension is high. Mercury has a high density, high surface tension, and low vapor tension. Water is the best studied substance and exhibits certain anomalous thermophysical properties owing to its ability to form hydrogen intermolecular bonds. In particular, unlike mercury and hexane, the molecule of water is polar, which probably accounts for the relatively low value of the condensation coefficient, $\alpha_{\rm c} \approx 0.04$ [7, 8].

The applications of these substances are also quite different. Mercury is used in gas discharge lamps and in vacuum equipment, and its vapor is a health hazard. Because of this, it is important to know the rate of evaporation of mercury. Hexane is a component of the gasoline cut, and its rate of evaporation is indicative of the rate of evaporation of fuel in general. The importance of calculation of the evaporation rate of water droplets is obvious.

The table below gives the initial physical characteristics and then above-introduced characteristic parameters for the substances in question, calculated under the assumption of evaporation in atmospheric air at about the standard conditions: $p=10^5$ Pa and $T_0=300$ K. The coefficients of heat conductivity of air are assumed to be $\lambda=0.026$ W m$^{-1}$ K$^{-1}$ and $\alpha_{\rm t}=1$.

The vapor tension of mercury is quite low, so the rate of evaporation is relatively small, and the temperature of a droplet is virtually the same as ambient. It is interesting that the high coefficient of surface tension of mercury in dimensionless variables, $\beta$, does not make its evaporation stand out against other substances. Owing to the large value of the parameter $\alpha \gg 1$, the rate of evaporation of the droplet is completely determined by the coefficient of diffusion of mercury atoms and does not depend on the heat conductivity of the environment, as assumed in Maxwell's theory. For the same reason, criterion (32) is always satisfied with a good margin.

<table>
<caption>Table. Characteristics of pure substances and parameters of the problem$\dagger$</caption>
<thead>
<tr>
<th>Substance</th>
<th>$P_{\rm s}$, Pa</th>
<th>$L_0$,<br>kJ mol$^{-1}$</th>
<th>$\rho$, kg m$^{-3}$</th>
<th>$D$, cm$^2$ s$^{-1}$</th>
<th>$\alpha_{\rm c}$</th>
<th>$\sigma$, mN m$^{-1}$</th>
<th>$\omega$</th>
<th>$a$</th>
<th>$b$, nm</th>
<th>$\tau$, $\mu$s</th>
<th>$\beta$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mercury</td>
<td>0.27</td>
<td>65.6</td>
<td>13550</td>
<td>0.21</td>
<td>1.0</td>
<td>465</td>
<td>25.3</td>
<td>2066</td>
<td>475</td>
<td>127</td>
<td>$2.2^{-5}$</td>
</tr>
<tr>
<td>Water</td>
<td>$3.6^3$</td>
<td>43.8</td>
<td>997</td>
<td>0.25</td>
<td>0.04</td>
<td>71</td>
<td>16.6</td>
<td>0.303</td>
<td>976</td>
<td>292</td>
<td>$4.9^{-5}$</td>
</tr>
<tr>
<td>$n$-hexane</td>
<td>$2.2^4$</td>
<td>37.7</td>
<td>660</td>
<td>0.10</td>
<td>1.0</td>
<td>18</td>
<td>14.1</td>
<td>0.171</td>
<td>19.2</td>
<td>0.02</td>
<td>$4.7^{-3}$</td>
</tr>
<tr>
<td colspan="12">$\dagger$ We use abbreviated notation. for example, $3.6^3 \equiv 3.6 \times 10^3$.</td>
</tr>
</tbody>
</table>

By contrast, for hexane droplets of almost any size at $f_0=0$ this criterion is not satisfied. In this case the linear expansion (8) underestimates the magnitude of the vapor tension, and the function $\theta(R)$ for hexane at $f_0 \approx 0$ gives considerably exaggerated evaporation times. The estimate becomes more accurate for $f_0 \to 1$. In spite of the low value of the coefficient of surface tension $\sigma$ of hexane, its effects on the evaporation process persist over a much greater range of relative tensions as compared with water or mercury. This is indicated by the relatively large value of the dimensionless parameter $\beta$.

On the other hand, we should note the very small characteristic scale $b$ of hexane. This implies that, in the framework of the diffusion model, the evaporation of droplets of pure hexane always occurs in Maxwell's regime. Even a small quantity of a surfactant in hexane, however, can greatly reduce the coefficient of condensation of hexane molecules. In this case the characteristic radius $b \propto 1/\alpha_{\rm c}$ and the characteristic time of evaporation $\tau \propto 1/\alpha_{\rm c}^2$ can become much larger. It is known that an electric discharge in organic vapors gives rise to a whole spectrum of complex compounds that could act as surfactants. Seemingly, it was this situation that was observed in the above-mentioned experiments with stimulated condensation of unsaturated vapor in a corona streamer discharge [4].

Physically, the most interesting is the process of evaporation of water droplets that will be discussed in detail below.

### 4.4 Evaporation of water droplets
On the one hand, the parameter $a$ of water is of the order of unity, and the thermal conductivity of the environment has a considerable effect on the rate of evaporation. On the other hand, the characteristic parameter $b$ even for pure water is fairly large, so that the transition to the depletion regime occurs already at droplet sizes in the micrometer range, where the diffusion approximation still holds.

Besides, for submicron droplets, at dimensionless radii $R \ll 1$, criterion (32) is satisfied fairly well over the entire range $0 < f_0 < 1$. However, this cannot be said about large droplets. To illustrate this last statement, let us turn to the calculation of the so-called psychrometric temperature. Such is the temperature of liquid in a relatively large vessel, and such will be the reading of a wet thermometer in a psychrometer in a stationary gas. Setting $R \to \infty$ in (24) or (25), we get the psychrometric temperature $z=\varphi_0$. Figure 3 shows two calculated curves for the difference of readings of the dry and wet thermometers versus the relative humidity $z(f_0)$. We see that the agreement with the experimental points (the table for a standard VIT-2 hygrometer) is quite good. The discrepancy between theory and experiment arises precisely in the region where criterion (32), which assumes the form $1-f_0 \ll 2.6$ in the case of water, is violated. From a comparison with experiment one can obtain a direct estimate of coefficient $\alpha_{\rm t}$, because its magnitude appears in the expression for the parameter $a$. Good agreement between

![](./images/812459960758697984_3.jpg)

Figure 3. Relative temperature drop of the wet thermometer $z$ vs. the relative humidity $f_0$ for different temperatures of the dry thermometer: (1) $T_0 = 295$ K; (2) $T_0 = 305$ K (points in the diagram correspond to the psychrometric table for a standard VIT-2 psychrometer).

the slopes of the calculated and experimental curves indicates that $\alpha_t \approx 1$ for pure water in air.

The coefficient of condensation begins to tell on the rate of evaporation when the droplet becomes small enough. For water droplets the deviation from Maxwell's theory starts even at micrometer droplet sizes, when it is certainly still possible to use the approximation of a continuous medium (the free path of molecules in normal conditions is $\bar{l} \simeq 60$ nm $\ll 1$ $\mu$m). This is illustrated in Fig. 4, which shows the droplet lifetimes calculated using formula (29) at $\beta = 0$. Since criterion (32) at $R < 1$ is satisfied for $0 < f_0 < 1$, the theoretically calculated lifetime of small droplets can be regarded as quite reliable.

### 4.5 Growth and evaporation of droplets in the neighborhood of the dew point
A consistent account of surface tension in the proposed model gives a correct estimate for the time of evaporation of droplets near the dew point.

![](./images/812459960758697984_4.jpg)

Figure 4. Time of complete evaporation of water droplets $\theta$ vs. the initial radius $R$ at $T_0 = 300$ K, $f_0 = 0.5$: (1) the Maxwell regime of evaporation; (2) $\alpha_c = 0.04$; (3) $\alpha_c = 0.001$.

The proposed theory allows one to indicate the character- istic range of relative humidity where the effects of surface tension become important. From the expression for the temperature of the droplet (24) we can see that the surface tension has a considerable effect if
$$2\varphi_0 \simeq \beta, \quad 1 - f_0 \simeq \frac{R_\sigma}{2b}.$$

For pure water, which has $R_\sigma = 1.1$ nm under normal conditions, this estimate corresponds to $1 - f_0 \simeq 6 \times 10^{-4}$.

Let us first consider the case where $f_0$ is exactly equal to 1. In this situation the surface tension is a crucial factor. To find the time of evaporation of a droplet we need to go to the limit $\varphi_0 \to 0$ in equation (29). As a result, we get
$$
\theta_0(z)=\frac{\beta^2}{3 z^3}-\frac{\beta(1-\beta)}{2 z^2}+\frac{1}{6 \beta}-\frac{1}{2}+z-\beta+(1-\beta) \ln \frac{z}{\beta}.
\tag{36}
$$

Substituting expression (24) into (36) under the condition $\varphi_0 = 0$ yields the sought function $\theta_0(R)$. This function in the extreme cases of large and small radii can be expressed by the same formula
$$
\theta_0(R) \approx \frac{1}{\beta}\left(\frac{1}{2} R^2+\frac{1}{3} R^3\right).
\tag{37}
$$

Observe that formula (37), being asymptotically accurate in the limits of very large and very small values of $R$, also gives a very good approximation in the intermediate region $R \simeq 1$. Therefore, this expression can be rightly called an interpola- tion formula and used for all values of the radius.

If $f_0$ is only slightly different from 1, then for the lifetime of the droplet we must use the general expression (29). The passage through the dew point is reflected by a change of the sign of the parameter $\varphi_0$; to be more precise, $\varphi_0 > 0$ in unsaturated vapor, and $\varphi_0 < 0$ in supersaturated vapor.

For supersaturated vapor, as can easily be seen from expression (23), there is a critical size of droplets $R_{\text{crit}}$. The droplets with $R < R_{\text{crit}}$ will continue to evaporate even in the supersaturated vapor, and only droplets with $R > R_{\text{crit}}$ will grow because of the condensation of vapor on their surface. Since a droplet with the critical radius is in thermal equilibrium with the environment, it will suffice to set $z = 0$ in (23) and find the corresponding value of the dimensionless $R_{\text{crit}}$:
$$
R_{\text{crit}}=-\frac{\beta}{\varphi_0}=\frac{R_\sigma}{b\left(f_0-1\right)}.
\tag{38}
$$

For $\varphi_0 < 0$ expression (23) gives positive values of the radius at $z > 0$ ($T_R < T_0$) if $R < R_{\text{crit}}$ (the drop is colder than the environment — evaporation regime), and at $z < 0$ ($T_R > T_0$) if $R > R_{\text{crit}}$ (the drop is warmer than the environment — condensation regime).

Figure 5 shows the results of exact calculations using formula (29) for the time of evaporation of a water droplet near the dew point. To demonstrate the difference between the curves, a lowered value of the coefficient of condensation was used in this calculation. The dashed line in the same diagram shows the evaporation time of the droplet calculated neglecting the surface tension. We see that in the range of small droplets it deviates considerably from the exact dependence (29).

![](./images/812459960758697984_5.jpg)

Figure 5. Lifetime of water droplet $\theta$ vs. the initial radius $R$ near the dew point at $\alpha_{c}=0.001$: (1) $f_{0}=0.999$, surface tension neglected; (2) $f_{0}=0.999$; (3) $f_{0}=1.001$; (4) $f_{0}=1.0$.

It is interesting that all our formulas can also be used to calculate the time of condensation growth of a droplet in supersaturated vapor. In the regime of condensation $(z<0)$ the expression for the rate of variation of the radius changes its sign automatically, and the same formula (28) can be used to calculate the time of growth of a droplet from a certain, sufficiently large radius $R>R_{\text{crit}}$ to a radius $R_{0}$. Naturally, the range of applicability of the theoretical model to the calculation of the rate of growth of the droplet is restricted by the same inequality (32).

Here, however, some comments are due. Condensation of aerosols from supersaturated vapor is a collective process that involves a multitude of droplets of very different sizes. Calculations of the kinetics of evaporation and condensation of an ensemble of particles must self-consistently take into account both the change of the relative humidity and the dynamics of the droplet size distribution function [10]. There is, however, a practically important case where the number of droplets in the system is relatively small, and their growth does not materially affect the temperature and the relative humidity of the environment (such is the situation, for example, in a Wilson cloud chamber). Therefore, our theory is quite capable of giving a correct estimate of the growth of droplets after the nucleation under such conditions. Formulas for the rate of growth of an individual droplet can also be useful for the description of the process of condensation of an ensemble of droplets as one of the equations of the system, providing that the change of parameters of the environment is taken into account in a self-consistent manner.

## 5. Conclusions

Even though the proposed theory of evaporation of a solitary spherical droplet does not predict any new effects, it certainly has methodological and practical merits.

- This theory adequately reflects the variety of physical processes associated with the evaporation of a droplet far from the boiling point in an atmosphere of a buffer gas at moderate pressure. By means of using the coefficients $\alpha_{c}$ and $\alpha_{t}$ as additional parameters of the problem, one can expand considerably the applicability of the diffusion model. The limits of applicability of the theory are outlined in this model in a physically clear way.

- With the use of straightforward mathematics, it was possible to find for the first time an exact solution of the problem of evaporation of a droplet in a relatively broad neighborhood of the dew point with due account for the effects of surface tension on the saturated vapor pressure near the curved phase interface.

- The analytical solution of the problem gives a clear idea of the interplay of various factors affecting the rate of evaporation of the droplet. Of special practical importance are the analytical expressions for the overall (integral) lifetime of the droplet, which, unlike the differential rate of evaporation, can rather easily be measured experimentally. The availability of a fairly general analytical theory opens the possibility of efficient evaluations of low-valued condensation coefficients from the experimental curves of the integral lifetime of a droplet as a function of its initial radius.

## References

1. Green H, Lane W *Particulate Clouds: Dusts, Smokes and Mists* 2nd ed. (Princeton, N.J.: Van Nostrand, 1964) [Translated into Russian (Moscow: Khimiya, 1972)]
2. Dovgalyuk Yu A, Ivlev L S *Fizika Vodnykh i Drugikh Atmosfernykh Aerozolei* (Physics of Water and Other Atmospheric Aerosols) (St. Petersburg: Izd. SPbGU, 1998)
3. Rusanov V D, Fridman A A *Fizika Khimicheski Aktivnoī Plazmy* (Physics of Chemically Active Plasma) (Moscow: Nauka, 1984)
4. Bugaev S P et al. *Dokl. Ross. Akad. Nauk* **361** 612 (1998) [*Dokl. Phys.* **43** 473 (1998)]
5. Bugaev S P et al. *Plasma Chem. Plasma Proces.* **18** (2) 247 (1998)
6. Kuni F M, Shchekin A K, Grinin A P *Usp. Fiz. Nauk* **171** 345 (2001) [*Phys. Usp.* **44** 331 (2001)]
7. Fuks N A *Isparenie i Rost Kapel’ v Gazoobraznoī Srede* (Evaporation and Growth of Droplets in Gaseous Medium) (Itogi Nauki i Tekhniki, Ser. Fiziko-Matematicheskie Nauki, Vol. 1) (Moscow: Izd. AN SSSR, 1958)
8. Hirth J P, Pound G M *Condensation and Evaporation* (New York: Macmillan, 1963) [Translated into Russian (Moscow: Metallurgiya, 1966)]
9. Ivchenko I N, Muradyan S M *Izv. Akad. Nauk SSSR Ser. Mekh. Zhidk. Gaza* (1) 112 (1982)
10. Lifshitz E M, Pitaevskiĭ L P *Fizicheskaya Kinetika* (Physical Kinetics) (Moscow: Nauka, 1979) [Translated into English (Oxford: Pergamon Press, 1981)]
11. Kuni F M *Kolloid. Zh.* **46** 674 (1984)