![](./images/812034414711144449_1.jpg)

# An Analytical Solution for the Wilson Point in Homogeneously Nucleating Flows

Lixi Huang and John B. Young

*Proc. R. Soc. Lond. A* 1996 **452**, 1459-1473
doi: 10.1098/rspa.1996.0074

## Email alerting service
Receive free email alerts when new articles cite this article - sign up in the box at the top right-hand corner of the article or click [here]

To subscribe to *Proc. R. Soc. Lond. A* go to: http://rspa.royalsocietypublishing.org/subscriptions

This journal is © 1996 The Royal Society

# An analytical solution for the Wilson point in homogeneously nucleating flows

By Lixi Huang $^{1}$ and John B. Young $^{2}$

$^{1}$ Peterhouse, University of Cambridge, Cambridge CB2 1RD, UK
$^{2}$ Whittle Laboratory, University of Cambridge, Madingley Road, Cambridge CB3 0DY, UK

The calculation of conditions at the Wilson point is the key to both theoretical and numerical studies of the condensation of pure vapours by homogeneous nucleation. Nucleation and droplet growth occur in a very short period of time, during which the changes of many vapour properties due to the normal thermofluid dynamic processes are negligible compared with the change of the heat release rate. This feature is exploited in an analysis leading to an approximate solution for the maximum subcooling and other properties at the Wilson point. The analysis is general but attention is focused on the main application of interest, which is the condensation of steam in high-speed flows by homogeneous nucleation. Crucial approximations are justified over a wide range of steam pressures and the analytical results reveal the dependency of steam properties at the Wilson point on controlling parameters such as the rate of pressure decrease. A direct link is established between the steam properties at the saturation point and those at the Wilson point, which, when used in multidimensional condensation flow calculations, should remove the need for very fine meshes and excessive computing resources which are otherwise required.

## 1. Introduction

The numerical calculation of the two-dimensionally homogeneously nucleating steady flow of supersaturated vapours was first achieved by Oswatitsh (1941) and is now well established (see, for example, Schnerr & Dohrmann (1989) for moist air flow in nozzles and around isolated aerofoils; Young (1992) and Bakhtar & So (1991) for pure steam flow in turbomachinery cascades). A number of methods for periodically unsteady flows have also been reported (White & Young 1993; Schnerr *et al.* 1994). Agreement with experiment is generally good, indicating the essential correctness of the theory of homogeneous nucleation and droplet growth in high-speed flow. Nevertheless, serious problems still remain if the techniques are to be extended to three-dimensional, possibly unsteady, flows in such complex geometries as turbine cascades.

The main difficulty relates to the fact that the zone of intense homogeneous nucleation in a high-speed flow occupies a very short distance in the flow direction. Within this zone, vast numbers of submicroscopic droplets form and grow rapidly, releasing their latent heat to the surrounding vapour. The heat release eventually checks the increase of vapour subcooling, the flow returns towards thermodynamic equilibrium and nucleation effectively ceases. The point of maximum subcooling along a fluid

Proc. R. Soc. Lond. A (1996) **452**, 1459-1473
© 1996 The Royal Society
Printed in Great Britain
1459
TEX Paper

![](./images/812034414711144449_2.jpg)

streamline (or pathline in unsteady flow) is known as the Wilson point and an accurate knowledge of the flow properties here is the key to successful prediction of the flow behaviour further downstream. Quite obviously, the computational problem of keeping track of a sufficient number of groups of growing droplets to characterize the nucleation process along a sufficient number of streamlines in a complex three-dimensional flow field is a huge undertaking, both in terms of the construction of the computer program and the hardware requirements of storage and processing time.

With a view to simplification, this paper presents an approximate, but nonetheless accurate, method for calculating conditions at the Wilson point in a nucleating flow. The method is completely analytical and does not require the usual numerical integration of the droplet growth equations for a discretized droplet spectrum. It is also sufficiently general that incorporation into a flow calculation method is not dependent on the use of a particular flow solver.

One of the attractions of the analysis is its simplicity. The solution is obtained as an algebraic expression relating the various controlling parameters to the subcooling at the Wilson point, and this yields physical insight which is difficult to acquire from a purely numerical approach. An attempt in this direction was made by Dobbins (1983) and his work provided the starting point for the present study. The only other analytical approaches are those of Gyarmathy & Meyer (1965) (which succeeded in isolating the 'rate of expansion' as an important controlling parameter) and the rather complicated asymptotic method of Clarke & Delale (1986), which does not appear well suited for generalization.

The problem is posed in a Lagrangian coordinate system in which fluid particles are followed and only the Lagrangian time coordinate $t$ is formally required to specify the position of a fluid particle. (This approach should not be confused with the one-dimensional model in an Eulerian coordinate system.) The temporal path from the saturation point $t = t_{\rm s}$ to the Wilson point $t = t_{\rm W}$ must be specified in some way and there are a number of possibilities depending on the particular problem considered. For expansions through near one-dimensional nozzles, the variation of the flow cross-sectional area is normally specified and this defines the solution. For more complex two- or three-dimensional geometries, however, the streamline pattern is determined by the pressure distribution of the neighbouring flow field and is not known *a priori*. In these circumstances, it is advantageous to construct the theory in terms of an independently prescribed pressure distribution in the vicinity of the Wilson point rather than a prescribed streamtube area variation. This is because multidimensional flows are normally computed by iterative numerical techniques and an approximation for the pressure field is readily available at each stage of the iteration procedure. The local variation of streamtube area is much harder to obtain.

Although the following analysis is not confined to a particular fluid, attention is, nevertheless, focused on the application of prime concern to the authors, which is the condensation of pure steam by homogeneous nucleation. It is for this application only that the approximations of the theory have been rigorously validated.

### 2. Equations to be solved

The following assumptions are made: (i) the vapour flow is inviscid and the intense nucleation zone is not intercepted by an adiabatic shock wave; (ii) the liquid phase is very finely dispersed in the mixture which can therefore be modelled as a continuum; (iii) there is no slip velocity between the phases; (iv) the vapour behaves
Proc. R. Soc. Lond. A (1996)

An analytical solution for nucleating flows

as a perfect gas; and (v) the specific heat capacity of the liquid is constant. All these approximations are standard and well established for low-pressure condensing flows of steam and many other substances. Assumption (iv) can easily be relaxed but is included here so as not to over complicate the analysis.

All vapour phase properties are represented by symbols without subscripts, e.g. density $\rho$, temperature $T$, pressure $p$, isobaric specific heat capacity $c_{p}$ and enthalpy $h$. The liquid phase and mixture are indicated by subscripts 'L' and 'mix', respectively.

The vapour subcooling is defined as the difference between $T_{\mathrm{s}}$, the saturation temperature at the local static pressure $p$, and $T$, the actual vapour temperature,
$$
\Delta T=T_{\mathrm{s}}-T.
$$

If the pressure distribution is given, the knowledge of the subcooling variation allows all other properties to be determined. Denoting conditions at the Wilson point by the subscript 'W' and the Lagrangian time derivative $\mathrm{d} / \mathrm{d} t$ by an over-head dot, e.g. $\Delta \dot{T} \equiv \mathrm{d}(\Delta T) / \mathrm{d} t$, we postulate a Taylor expansion about the Wilson point for the subcooling distribution,
$$
\Delta T(t)=\Delta T_{\mathrm{W}}+\Delta \dot{T}_{\mathrm{W}}\left(t-t_{\mathrm{W}}\right)+\frac{1}{2} \Delta \ddot{T}_{\mathrm{W}}\left(t-t_{\mathrm{W}}\right)^{2}+\cdots,
$$
which is to be truncated at the second-order term. Since the first derivative $\Delta \dot{T}_{\mathrm{W}}$ vanishes at the Wilson point by definition, it leaves only the maximum subcooling $\Delta T_{\mathrm{W}}$ and the second derivative $\Delta \ddot{T}_{\mathrm{W}}$ to give a locally parabolic approximation to the subcooling distribution. To determine these two quantities, two equations are needed. These are obtained from the momentum and energy conservation equations for the vapour-liquid mixture together with the Clausius-Clapeyron equation and the equation of state for the vapour phase. The two derived equations contain the wetness growth terms $\dot{Y}_{\mathrm{W}}, \ddot{Y}_{\mathrm{W}}$ ( $Y$ being the wetness fraction), for which two additional equations will then be derived from the theories of nucleation and droplet growth.

### (a) Momentum, energy and Clausius-Clapeyron equations

In the absence of interphase velocity slip, the familiar Euler momentum and energy equations are valid for the two-phase mixture. Thus,
$$
\rho_{\text {mix }} \frac{\mathrm{d} \boldsymbol{V}}{\mathrm{d} t}+\nabla p=0, \quad \rho_{\text {mix }} \frac{\mathrm{d}}{\mathrm{d} t}\left(h_{\text {mix }}+\frac{1}{2} V^{2}\right)=\frac{\partial p}{\partial t},
$$
where $\rho_{\text {mix }}$ and $h_{\text {mix }}$ are the mixture density and specific enthalpy, and $\boldsymbol{V}$ is the flow velocity. These equations can be combined to give the Lagrangian or thermodynamic form of the energy equation:
$$
\rho_{\text {mix }} \frac{\mathrm{d} h_{\text {mix }}}{\mathrm{d} t}=\frac{\mathrm{d} p}{\mathrm{~d} t}. \tag{2.1}
$$

The following development applies to both steady and unsteady flows and it must be emphasized that applications are by no means restricted to one-dimensional flows.

Neglecting the volume of the liquid phase, $\rho_{\text {mix }}=\rho /(1-Y)$, where $\rho$ is the vapour density and $Y$ is the wetness fraction. Assuming all droplets are at the saturation temperature (see below),
$$
h_{\text {mix }}=(1-Y) h+Y h_{\mathrm{L}}=h-Y\left(h-h_{\mathrm{L}}\right),
$$
where $h_{\mathrm{L}}=h_{\mathrm{L}}\left(T_{\mathrm{s}}\right)$ and $\mathrm{d} h_{\mathrm{L}}=c_{\mathrm{L}} \mathrm{d} T_{\mathrm{s}}$. Also, $h-h_{\mathrm{L}}=h_{\mathrm{fg}}-c_{p} \Delta T$, where $h_{\mathrm{fg}}$ is the

Proc. R. Soc. Lond. A (1996)

specific enthalpy of condensation and $c_p$ is the isobaric specific heat capacity of the vapour phase. Introducing these expressions, (2.1) becomes

$$
(1-Y) c_{p} \dot{T}+Y c_{\mathrm{L}} \dot{T}_{\mathrm{s}}-\left(h_{\mathrm{fg}}-c_{p} \Delta T\right) \dot{Y}=\frac{(1-Y)}{\rho} \dot{p}. \tag{2.2}
$$

The saturation temperature is related to the pressure by the Clausius-Clapeyron equation, which, assuming the vapour behaves as a perfect gas and the volume of the liquid is negligible, can be written

$$
\frac{1}{T_{\mathrm{s}}} \frac{\mathrm{d} T_{\mathrm{s}}}{\mathrm{d} t}=\frac{R T_{\mathrm{s}}}{h_{\mathrm{fg}}} \frac{1}{p} \frac{\mathrm{d} p}{\mathrm{~d} t}. \tag{2.3}
$$

Combining equations (2.2) and (2.3), and introducing the equation of state for the vapour $p=\rho R T$, gives

$$
\frac{\dot{T}}{T}=\frac{\dot{Y}}{1-Y}\left(\frac{h_{\mathrm{fg}}-c_{p} \Delta T}{c_{p} T}\right)+\frac{\dot{p}}{p}\left(\frac{\gamma-1}{\gamma}-\frac{Y}{1-Y} \frac{c_{\mathrm{L}} T_{\mathrm{s}}}{c_{p} T} \frac{R T_{\mathrm{s}}}{h_{\mathrm{fg}}}\right), \tag{2.4}
$$

where $\gamma$ is the ratio of specific heats of the vapour phase, $c_{p} /(c_{p}-R)$, which is about 1.3. Before the Wilson point, $Y$ is very small, typically $Y<0.001$, so that both $Y$ in $1-Y$ and

$$
\frac{Y}{1-Y} \frac{c_{\mathrm{L}} T_{\mathrm{s}}}{c_{p} T} \frac{R T_{\mathrm{s}}}{h_{\mathrm{fg}}}
$$

in the right-hand side bracket of equation (2.4) can be ignored. The insertion of $\dot{T}=\dot{T}_{\mathrm{s}}-\Delta \dot{T}$, and the Clausius-Clapeyron equation (2.3) into equation (2.4), then gives the equation for the variation of subcooling:

$$
\frac{\Delta \dot{T}}{T}+\dot{Y}\left(\frac{h_{\mathrm{fg}}-c_{p} \Delta T}{c_{p} T}\right)+\frac{\dot{p}}{p}\left(\frac{\gamma-1}{\gamma}-\frac{R T_{\mathrm{s}}}{h_{\mathrm{fg}}} \frac{T_{\mathrm{s}}}{T}\right)=0. \tag{2.5}
$$

### (b) Two equations for the Wilson point

We now define

$$
k_{p}=\frac{-1}{p} \frac{\mathrm{d} p}{\mathrm{~d} t}, \quad L=\frac{h_{\mathrm{fg}}-c_{p} \Delta T}{c_{p} T}, \quad \gamma_{\mathrm{s}}=\frac{\gamma-1}{\gamma}-\frac{R T_{\mathrm{s}}}{h_{\mathrm{fg}}} \frac{T_{\mathrm{s}}}{T},
$$

so that equation (2.5) is rewritten as

$$
\Delta \dot{T}=T\left(\gamma_{\mathrm{s}} k_{p}-L \dot{Y}\right). \tag{2.6}
$$

$k_p$ is the rate of proportional pressure decrease. The parameter $L$ varies only slightly through the zone of intense nucleation preceding the Wilson point and can be treated as a constant evaluated at the Wilson point, a typical value of which is $4.0 . \gamma_{\mathrm{s}}$ is basically a constant with typical values for low-pressure steam around 0.2. All typical values are based on the case of a Wilson point with a pressure of 0.1 bar and a maximum subcooling of 35 K.

The second derivative of subcooling is given by

$$
\Delta \ddot{T}=T\left(\gamma_{\mathrm{s}} \dot{k}_{p}-L \ddot{Y}\right)+C_{q}, \tag{2.7}
$$

where

$$
C_{q}=\gamma_{\mathrm{s}} k_{p} \dot{T}-\dot{Y} \frac{\mathrm{d}}{\mathrm{d} t}(L T)
$$

represents the terms arising from the variations of temperature $T$ and the evaporation enthalpy $h_{\text{fg}}$. At the Wilson point, $\Delta \dot{T}_{\mathrm{W}}=0$, equations (2.6) and (2.4) give

$$
\dot{Y}_{\mathrm{W}}=\frac{\gamma_{\mathrm{s}}}{L} k_{p \mathrm{~W}}, \quad \dot{T}_{\mathrm{W}}=-T_{\mathrm{W}}\left(\frac{R T_{\mathrm{s}}^{2}}{h_{\mathrm{fg}} T}\right)_{\mathrm{W}} k_{p \mathrm{~W}}.
$$

Hence,

$$
C_{q \mathrm{~W}}=-\gamma_{\mathrm{s}}\left(1+\frac{c_{\mathrm{L}} / c_{p}-1}{L}\right) \frac{R T_{\mathrm{sW}}}{h_{\mathrm{fg}}} T_{\mathrm{sW}} k_{p \mathrm{~W}}^{2} \approx-0.02 T_{\mathrm{sW}} k_{p \mathrm{~W}}^{2}.
$$

We will show later that $k_{p \mathrm{~W}}^{2} \ll \ddot{Y}_{\mathrm{W}}$; thus, $C_{q}$ in equation (2.7) can be ignored. Finally, equations (2.6) and (2.7) give

$$
\left.egin{array}{l}
\Delta \dot{T}_{\mathrm{W}}=T_{\mathrm{W}}\left(\gamma_{\mathrm{s}} k_{p \mathrm{~W}}-L \dot{Y}_{\mathrm{W}}\right)=0, \
\Delta \ddot{T}_{\mathrm{W}}=T_{\mathrm{W}}\left(\gamma_{\mathrm{s}} \dot{k}_{p \mathrm{~W}}-L \ddot{Y}_{\mathrm{W}}\right).
\end{array}ight\}
\tag{2.8}
$$

As $\dot{Y}_{\mathrm{W}}$ is necessarily positive, the first of equations (2.8) shows that $k_{p}=$ $-\mathrm{d}(\ln p) / \mathrm{d} t>0$. Thus, the pressure is always decreasing at the Wilson point irrespective of the local Mach number or flow geometries.

In passing, it should be noted that $k_{p}$ is related to, but is not identical to, the 'rate of expansion' introduced by Gyarmathy & Meyer (1965), and usually referred to as 'pdot'. The difference is that, whereas $k_{p}$ is the local value of $-\mathrm{d}(\ln p) / \mathrm{d} t$ in the actual condensing flow, Gyarmathy's 'pdot' represents the rate of expansion in a similar but hypothetical flow where condensation is inhibited. $k_{p}$ is thus precisely defined, whereas Gyarmathy's 'pdot' is open to alternative interpretations.

The governing equations (2.8) contain $\dot{Y}_{\mathrm{W}}$ and $\ddot{Y}_{\mathrm{W}}$, which have to be found from the theories of nucleation and droplet growth. First we need to introduce some approximations for the two theories.

### (c) Nucleation and droplet growth

The classical nucleation rate is expressed as follows (see, for example, McDonald 1962, 1963):

$$
I=I_{0} \exp \left(\frac{-\Theta^{2}}{\Delta T^{2}}\right),
\tag{2.9}
$$

where

$$
I_{0}=\frac{\rho}{\rho_{\mathrm{L}}}\left(\frac{2 \sigma}{\pi m_{\mathrm{m}}^{3}}\right)^{1 / 2}, \quad \Theta=T_{\mathrm{s}}\left(\frac{T_{\mathrm{c}}}{T}\right)^{1 / 2}, \quad T_{\mathrm{c}}=\frac{16 \pi \sigma^{3}}{3 k \rho_{\mathrm{L}}^{2} h_{\mathrm{fg}}^{2}}.
$$

$I$ is the number of critical-sized droplets formed per unit time per unit mass of mixture, $k=1.38 \times 10^{-23} \mathrm{~J} \mathrm{~K}^{-1}$ is the Boltzmann constant, $m_{\mathrm{m}}$ is the mass of a molecule and $\sigma$ is the liquid surface tension varying with the temperature $T$. $T_{\mathrm{c}}$ and $\Theta$ are defined for convenience and both have dimension of temperature and typical values of 82 and $175 \mathrm{~K}$, respectively. Non-isothermal and other corrections to the theory (see, for example, Young 1982) can be included if desired, but they do not change the basic course of the solution to come.

The nucleation rate $I$ is a strongly nonlinear function of $\Delta T$. A tiny increase in $\Delta T$ results in a massive increase in $I$. This is the one single factor that causes the 'collapse' of metastable equilibrium and the factor that enables the simplification of the extremely nonlinear problem.

Taylor expansions based on the Wilson point for both $\Theta$ and $\Delta T$ are now formu- lated. Let $\tau = t_{\mathrm{W}} - t$ be the local coordinate which measures the time backwards from the Wilson point. Thus,
$$
\Theta(\tau)=\Theta_{\mathrm{W}}(1-k_{\Theta \mathrm{W}} \tau+\cdots), \quad \Delta T(\tau)=\Delta T_{\mathrm{W}}\left(1+\frac{1}{2} \frac{\Delta \ddot{T}_{\mathrm{W}}}{\Delta T_{\mathrm{W}}} \tau^{2}+\cdots\right),
$$
where $k_{\Theta \mathrm{W}}=(\dot{\Theta} / \Theta)_{\mathrm{W}}<0$ and its value is found to be a certain proportion of $k_{p}$:
$$
\frac{k_{\Theta \mathrm{W}}}{-k_{p \mathrm{~W}}}=\left(\frac{R T_{\mathrm{s}}}{h_{\mathrm{fg}}}\right)_{\mathrm{W}}\left(\frac{T_{\mathrm{sW}}}{T_{\mathrm{W}}}\right)\left(\left[\frac{1}{2}+\frac{3}{2} \frac{\mathrm{d}(\ln \sigma)}{\mathrm{d}(\ln T)}-\frac{\mathrm{d}\left(\ln h_{\mathrm{fg}}\right)}{\mathrm{d}(\ln T)}\right]_{\mathrm{W}},\right.
$$
which, for low pressure steam, is about 0.02. Note that $\tau^{2}$ is the first small quantity in $\Delta T(\tau)$ since $\Delta \dot{T}_{\mathrm{W}}=0$.

Retaining the first small term from each of the two expansions, the exponent in the nucleation rate equation becomes
$$
-\frac{\Theta^{2}}{\Delta T^{2}}=-\frac{\Theta_{\mathrm{W}}^{2}}{\Delta T_{\mathrm{W}}^{2}}\left(1-2 k_{\Theta \mathrm{W}} \tau-\frac{\Delta \ddot{T}_{\mathrm{W}}}{\Delta T_{\mathrm{W}}} \tau^{2}\right).
$$

The largest nucleation rate occurs at the Wilson point and is given by
$$
I_{\mathrm{W}}=I_{0 \mathrm{~W}} \exp \left(-\Theta_{\mathrm{W}}^{2} / \Delta T_{\mathrm{W}}^{2}\right).
$$

$I$ at upstream positions is also evaluated by a Taylor expansion:
$$
I(\tau)=I_{\mathrm{W}}\left(1-\frac{\dot{I}_{0 \mathrm{~W}}}{I_{0 \mathrm{~W}}} \tau\right) \exp \left(-\frac{\tau}{\tau_{\Theta}}-\frac{\tau^{2}}{\tau_{\mathrm{n}}^{2}}\right),\qquad(2.10)
$$
where $\tau_{\mathrm{n}}$ and $\tau_{\Theta}$ have been introduced for convenience,
$$
\tau_{\mathrm{n}}=\frac{\Delta T_{\mathrm{W}}}{\Theta_{\mathrm{W}}}\left(\frac{\Delta T_{\mathrm{W}}}{-\Delta \ddot{T}_{\mathrm{W}}}\right)^{1 / 2}, \quad \tau_{\Theta}=\frac{\Delta T_{\mathrm{W}}^{2}}{2 \Theta_{\mathrm{W}}^{2}\left(-k_{\Theta \mathrm{W}}\right)}.\qquad(2.11)
$$

$\tau_{\mathrm{n}}$ is the time scale during which the nucleation rate changes by a factor of e. It is a measure of the temporal width of the zone of intense nucleation. We shall refer to it as the 'nucleation time'. $\tau_{\Theta}$ is the time scale during which significant changes in $\Theta$ occur. Since $\Theta$ does not change much through the zone of intense nucleation, $\tau_{\Theta} \gg \tau_{\mathrm{n}}$; the change of the nucleation rate $I$ close to the Wilson point is dominated by the second order term $(\tau / \tau_{\mathrm{n}})^{2}$ in the exponent. The fact that all variations associated with the vapour phase thermofluid processes have a time scale much longer than the intense nucleation zone is characterized by $k_{p} \tau_{\mathrm{n}} \ll 1$, where $k_{p} \tau_{\mathrm{n}}$ has typically low values around 0.01. This is an essential relationship by which most of the simplifications made in this paper are justified.

We now derive an expression for the droplet radius $r$ in terms of $\Delta T_{\mathrm{W}}$ and $\Delta \ddot{T}_{\mathrm{W}}$. It is assumed that, near the Wilson point, the radius of those droplets that contribute most significantly to the heat release fall in the range
$$
0 \leftarrow r_{\mathrm{c}} \ll r \ll \ell,\qquad(2.12)
$$
where
$$
r_{\mathrm{c}}=\frac{2 \sigma T_{\mathrm{s}}}{\rho_{\mathrm{L}} h_{\mathrm{fg}} \Delta T}, \quad \ell=\frac{\mu(2 \pi R T)^{1 / 2}}{2 p},
$$
are the Kelvin-Helmholtz critical radius and the molecular mean free path, respec- tively, $\mu$ being the vapour dynamic viscosity. The upper limit implies that droplet

![](./images/812034414711144449_3.jpg)

Figure 1. Approximations for the droplet growth theory. The critical radius $r_{\mathrm{c}}$ decreases before the Wilson point is reached. In the figure, both $r_{\mathrm{c}}$ and the difference between the realistic and approximate radii are exaggerated.

growth up to the Wilson point takes place under 'free-molecule' conditions. The lower limit implies that the droplets mainly responsible for the heat release at the Wilson point have grown considerably larger than the critical radius. Numerical cal- culations indicate that, for low-pressure steam in most practical situations, both approximations are acceptable.

Following Gyarmathy (1976), we assume that the droplet temperature attains instantaneously its quasi-steady value of $T_{\mathrm{s}}-\Delta T_{\text {cap }}$ where $\Delta T_{\text {cap }}=(r_{\mathrm{c}}/r)\Delta T$ is the capillary subcooling due to the effects of surface curvature. It therefore follows that, at the Wilson point, all droplets of consequence have effectively attained the saturation temperature $T_{\mathrm{s}}$.

Under these conditions, the droplet growth rate at the Wilson point is given, according to Young (1991), by

$$
\dot{r}=C_{r}\Delta T,\quad C_{r}=\frac{p}{(2\pi RT_{\mathrm{s}})^{1/2}\rho_{\mathrm{L}}}\left(\frac{\gamma+1}{2\gamma}\right)\left(\frac{c_{p}}{h_{\mathrm{fg}}}\right). \tag{2.13}
$$

The expression for $\dot{r}$ is, strictly speaking, only valid for established droplets near the Wilson point. Nevertheless, the approximation is now made that droplets are nucleated with zero radius and that $\dot{r}$ remains constant up to the Wilson point. The approximations inherent in this assumed growth law are illustrated in figure 1.

The droplet radius $r$ is a function of two time variables, one being the current time $t$ and the other being the time of nucleation $t_{\mathrm{n}}$, hence $r(t,t_{\mathrm{n}})$. For the Wilson point, $t=t_{\mathrm{W}}$, and the corresponding droplet radius is given by

$$
r_{\mathrm{W}}(\tau)\equiv r(t_{\mathrm{W}},t_{\mathrm{W}}-\tau)=\int_{t_{\mathrm{W}}-\tau}^{t_{\mathrm{W}}}C_{r}\Delta T\,\mathrm{d}t.
$$

To integrate, the growth coefficient $C_{r}$ also has to be approximated by a truncated Taylor expansion about the Wilson point, $C_{r}=C_{r\mathrm{W}}(1-k_{r\mathrm{W}}\tau)$, where

$$
k_{r\mathrm{W}}=-k_{p\mathrm{W}}+\frac{\dot{T}_{\mathrm{sW}}}{T_{\mathrm{sW}}}\left[\frac{1}{2}-\frac{\mathrm{d}(\ln h_{\mathrm{fg}})}{\mathrm{d}(\ln T_{\mathrm{s}})}\right]_{\mathrm{W}}=-k_{p\mathrm{W}}\left\{1+\left(\frac{RT_{\mathrm{s}}}{h_{\mathrm{fg}}}\right)_{\mathrm{W}}\left[\frac{1}{2}-\frac{\mathrm{d}(\ln h_{\mathrm{fg}})}{\mathrm{d}(\ln T_{\mathrm{s}})}\right]_{\mathrm{W}}\right\}.
$$

For low pressure steam, $k_{r\mathrm{W}}\approx -k_{p\mathrm{W}}$. With the expansions for $C_{r}$ and $\Delta T$, the

expression for the droplet radius becomes

$$
r_{\mathrm{W}}(\tau)=C_{r \mathrm{~W}} \Delta T_{\mathrm{W}}\left(\tau-\frac{1}{2} k_{r \mathrm{~W}} \tau^{2}+\frac{1}{6} \frac{\Delta \ddot{T}_{\mathrm{W}}}{\Delta T_{\mathrm{W}}} \tau^{3}\right). \tag{2.14}
$$

### (d) Wetness growth

Having simplified the nucleation and droplet growth equations, we can now calculate the wetness growth terms, $\dot{Y}_{\mathrm{W}}$ and $\ddot{Y}_{\mathrm{W}}$ so that equations (2.8) can be solved for $\Delta T_{\mathrm{W}}$ and $\Delta \ddot{T}_{\mathrm{W}}$. The wetness fraction $Y$ at any Lagrangian time $t$ is the sum of contributions from droplets formed at all upstream times starting from $t_{\mathrm{s}}$ when the saturation line is first crossed:

$$
Y(t)=\rho_{\mathrm{L}} \frac{4}{3} \pi \int_{t_{\mathrm{s}}}^{t} I\left(t_{\mathrm{n}}\right) r^{3}\left(t, t_{\mathrm{n}}\right) \mathrm{d} t_{\mathrm{n}}.
$$

For $t=t_{\mathrm{W}}$, the integration variable $t_{\mathrm{n}}$ can be changed to $\tau=t_{\mathrm{W}}-t_{\mathrm{n}}$, so the integration limits become $\tau=0 \rightarrow\left(t_{\mathrm{W}}-t_{\mathrm{s}}\right)$. As in (Dobbins 1983), the upper limit can be replaced by $+\infty$ since the nucleation rate according to equation (2.9) vanishes rapidly for earlier times. After inserting the nucleation equation (2.10) and the droplet radius equation (2.14), the wetness at the Wilson point becomes

$$
\begin{aligned}
Y_{\mathrm{W}}=\rho_{\mathrm{L}} \frac{4}{3} \pi I_{\mathrm{W}}\left(C_{r \mathrm{~W}} \Delta T_{\mathrm{W}}\right)^{3} \int_{0}^{\infty} & \left(1-\frac{\dot{I}_{0 \mathrm{~W}}}{I_{0 \mathrm{~W}}} \tau\right) \tau^{3}\left(1-\frac{1}{2} k_{r \mathrm{~W}} \tau+\frac{1}{6} \frac{\Delta \ddot{T}_{\mathrm{W}}}{\Delta T_{\mathrm{W}}} \tau^{2}\right)^{3} \\
& \times \exp \left[-\left(\frac{\tau}{\tau_{\Theta}}+\frac{\tau^{2}}{\tau_{\mathrm{n}}^{2}}\right)\right] \mathrm{d} \tau.
\end{aligned} \tag{2.15}
$$

Two approximations are now made. The first is to neglect the linear term in the exponent, $\tau / \tau_{\Theta}$, under the condition of $\tau_{\Theta} \gg \tau_{\mathrm{n}}$. To justify this approximation, we study the integral involving an arbitrary pre-exponential power $\tau^{m}$:

$$
\int_{0}^{\infty} \tau^{m} \exp \left(-\frac{\tau}{\tau_{\Theta}}-\frac{\tau^{2}}{\tau_{\mathrm{n}}^{2}}\right) \mathrm{d} \tau.
$$

The integrand increases from 0 at $\tau=0$ and decays to 0 extremely rapidly as $\tau$ exceeds the scale of the nucleation time $\tau_{\mathrm{n}}$. The peak is found at $\tau=\tau^{*}$, where

$$
\tau^{*}=\frac{\tau_{\mathrm{n}}}{4}\left[\left(8 m+\frac{\tau_{\mathrm{n}}^{2}}{\tau_{\Theta}^{2}}\right)^{1 / 2}+\frac{\tau_{\mathrm{n}}}{\tau_{\Theta}}\right].
$$

For $\tau_{\mathrm{n}} \ll \tau_{\Theta}, \tau^{*} \approx \tau_{\mathrm{n}}\left(\frac{1}{2} m\right)^{1 / 2}$. Therefore, the linear term $\tau / \tau_{\Theta}$ is much smaller than the quadratic term $\tau^{2} / \tau_{\mathrm{n}}^{2}$ in the compact region around $\tau=\tau^{*}$, where the integrand is of the order unity. We therefore drop the linear term. In other words, the small changes in all other terms of the nucleation exponent have negligible influence compared with the deceleration of subcooling, $-\Delta \ddot{T}$, near the Wilson point. The above integration is readily worked out:

$$
\int_{0}^{\infty} \tau^{m} \exp \left(-\tau^{2} / \tau_{\mathrm{n}}^{2}\right) \mathrm{d} \tau=
\begin{cases}
\frac{1}{2} \tau_{\mathrm{n}}^{2} & \text { for } m=1, \\
\frac{1}{4} \pi^{1 / 2} \tau_{\mathrm{n}}^{3} & \text { for } m=2, \\
\frac{1}{2} \tau_{\mathrm{n}}^{4} & \text { for } m=3.
\end{cases}
$$

The second approximation is the neglect of all higher order terms in the pre-exponential power function. For example, we can drop the term $k_{r \mathrm{~W}} \tau^{4}$ in the ex-

panded form of the integrand of equation (2.15) in favour of the dominating term $\tau^{3}$, the error being of the order $k_{r \mathrm{W}} \tau_{\mathrm{n}} \ll 1$.

With these two approximations, the nucleation rate of equation (2.10) and the droplet radius of equation (2.14) become
$$
I(\tau)=I_{\mathrm{W}} \exp \left(-\tau^{2} / \tau_{\mathrm{n}}^{2}\right), \quad r_{\mathrm{W}}(\tau)=C_{r \mathrm{W}} \Delta T_{\mathrm{W}} \tau .\qquad(2.16)
$$

The wetness fraction at the Wilson point is calculated as
$$
Y_{\mathrm{W}}=\frac{4}{3} \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \int_{0}^{\infty} \tau^{3} \exp \left(\tau^{2} / \tau_{\mathrm{n}}^{2}\right) \mathrm{d} \tau=\frac{4}{3} \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \frac{1}{2} \tau_{\mathrm{n}}^{4}. \quad(2.17)
$$

The wetness growth, $\dot{Y}_{\mathrm{W}}$, and the second derivative, $\ddot{Y}_{\mathrm{W}}$, are found as follows:
$$
\begin{aligned}
\dot{Y}_{\mathrm{W}} & =\rho_{\mathrm{L}} \frac{4}{3} \pi\left[I_{\mathrm{W}} r_{\mathrm{W}}^{3}\left(t_{\mathrm{W}}, t_{\mathrm{W}}\right)+\int_{0}^{\infty} I(\tau) 3 r_{\mathrm{W}}^{2}(\tau) \dot{r}_{\mathrm{W}} \mathrm{d} \tau\right] \\
& =4 \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \int_{0}^{\infty} \tau^{2} \mathrm{e}^{-\left(\tau / \tau_{\mathrm{n}}\right)^{2}} \mathrm{~d} \tau \\
& =4 \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \frac{1}{4} \tau_{\mathrm{n}}^{3} \pi^{1 / 2},
\end{aligned}
$$
where $r_{\mathrm{W}}\left(t_{\mathrm{W}}, t_{\mathrm{W}}\right)=r_{c \mathrm{W}}=0$ as was tactically assumed. Similarly,
$$
\begin{aligned}
\ddot{Y}_{\mathrm{W}} & =\rho_{\mathrm{L}} 8 \pi\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{2} \int_{0}^{\infty} I(\tau) r_{\mathrm{W}}(\tau) \mathrm{d} t+k_{r \mathrm{W}} \dot{Y}_{\mathrm{W}} \\
& =8 \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \int_{0}^{\infty} \tau \mathrm{e}^{-\left(\tau / \tau_{\mathrm{n}}\right)^{2}} \mathrm{~d} \tau+k_{r \mathrm{W}} \dot{Y}_{\mathrm{W}} \\
& =8 \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \frac{1}{2} \tau_{\mathrm{n}}^{2}+k_{r \mathrm{W}} \dot{Y}_{\mathrm{W}}.
\end{aligned}
$$

The last term $k_{r \mathrm{W}} \dot{Y}_{\mathrm{W}}$ can be ignored since its ratio to the remaining term is of the scale $k_{r \mathrm{W}} \tau_{\mathrm{n}} \ll 1$.

### 3. Solution of the equations

The wetness growth terms found above, $\dot{Y}_{\mathrm{W}}, \ddot{Y}_{\mathrm{W}}$, are expressed in terms of the maximum subcooling $\Delta T_{\mathrm{W}}$ and the nucleation time $\tau_{\mathrm{n}}$, which is defined in terms of $\Delta \ddot{T}_{\mathrm{W}}$ in equation (2.11) and now replaces $\Delta \ddot{T}_{\mathrm{W}}$ as the unknown quantity. Therefore, together with the governing equations (2.8), they form a complete set of four equations for the Wilson point:
$$
\left.\begin{array}{c}
\frac{\Delta \dot{T}_{\mathrm{W}}}{T_{\mathrm{W}}}=\gamma_{\mathrm{s}} k_{p \mathrm{W}}-L \dot{Y}_{\mathrm{W}}=0, \\
\frac{\Delta \ddot{T}_{\mathrm{W}}}{T_{\mathrm{W}}}=\gamma_{\mathrm{s}} \dot{k}_{p \mathrm{W}}-L \ddot{Y}_{\mathrm{W}}=-\frac{\Delta T_{\mathrm{W}}^{3}}{\Theta_{\mathrm{W}}^{2} T_{\mathrm{W}} \tau_{\mathrm{n}}^{2}}, \\
\dot{Y}_{\mathrm{W}}=\pi^{3 / 2} \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \tau_{\mathrm{n}}^{3} \\
\ddot{Y}_{\mathrm{W}}=4 \pi \rho_{\mathrm{L}} I_{\mathrm{W}}\left(C_{r \mathrm{W}} \Delta T_{\mathrm{W}}\right)^{3} \tau_{\mathrm{n}}^{2},
\end{array}\right\}\qquad(3.1)
$$
where $I_{\mathrm{W}}=I_{0 \mathrm{~W}} \exp \left(-\Theta_{\mathrm{W}}^{2} / \Delta T_{\mathrm{W}}^{2}\right)$ is the maximum nucleation rate.

### (a) The general solution

The insertion of $\dot{Y}_\mathrm{W}$ and $\ddot{Y}_\mathrm{W}$ from the third and the fourth equations of (3.1) into the first two gives two equations for the two unknowns, $\Delta T_\mathrm{W}$ and $\tau_\mathrm{n}$:

$$
\left.
\begin{aligned}
\gamma_\mathrm{s}k_{p\mathrm{W}} &= L\pi^{3/2}\rho_\mathrm{L}I_\mathrm{W}(C_{r\mathrm{W}}\Delta T_\mathrm{W})^3\tau_\mathrm{n}^3 \\
\gamma_\mathrm{s}\dot{k}_{p\mathrm{W}} - 4L\pi\rho_\mathrm{L}I_\mathrm{W}(C_{r\mathrm{W}}\Delta T_\mathrm{W})^3\tau_\mathrm{n}^2 &= -\frac{\Delta T_\mathrm{W}^3}{\Theta_\mathrm{W}^2T_\mathrm{W}\tau_\mathrm{n}^2}.
\end{aligned}
\right\} \tag{3.2}
$$

The nucleation time $\tau_\mathrm{n}$ can now be eliminated from equations (3.2) to give a single implicit equation for $\Delta T_\mathrm{W}$. Although this is a rather complicated algebraic equation, there is, in principle, no intrinsic difficulty in solving it by an iterative procedure once $k_{p\mathrm{W}}$ and $\dot{k}_{p\mathrm{W}}$ have been specified. However, rather than pursuing this general solution further, it is more instructive to consider the special case when $\dot{k}_{p\mathrm{W}} = 0$.

### (b) The special case $\dot{k}_{p\mathrm{W}} = 0$

This corresponds to the situation when the given 'rate of expansion' is constant through the zone of intense nucleation right up to the Wilson point:

$$
k_p = -\frac{\mathrm{d}(\ln p)}{\mathrm{d}t} = k_{p\mathrm{W}} = \text{const.} > 0.
$$

Under these circumstances, $k_p$ is effectively the same as Gyarmathy's 'pdot'. With $\dot{k}_{p\mathrm{W}} = 0$, equations (3.2) give an implicit expression for $\Delta T_\mathrm{W}$:

$$
(\gamma_\mathrm{s}k_p)^4\left(\frac{\Theta_\mathrm{W}}{\Delta T_\mathrm{W}}\right)^{12}\exp\left(\frac{\Theta_\mathrm{W}}{\Delta T_\mathrm{W}}\right)^2 = \rho_\mathrm{L}LI_{0\mathrm{W}}\left(\frac{T_\mathrm{s}}{T_\mathrm{W}}\right)^6\left(\frac{1}{4}\pi C_{r\mathrm{W}}T_{\mathrm{cW}}\right)^3. \tag{3.3}
$$

Note that $T_{\mathrm{cW}}$ is a temperature present in the nucleation rate exponent, cf. equation (2.9), and $C_{r\mathrm{W}}T_{\mathrm{cW}}$ represents an interesting coupling of the nucleation and droplet growth theories. For a given $k_p$, equation (3.3) can be readily solved for $\Delta T_\mathrm{W}$ by, for example, a Newton–Raphson iteration procedure.

Equation (3.3) is one of the main results of the analysis as it shows the dependency of the Wilson point subcooling on the 'rate of expansion', $k_p$, for those cases where $k_p$ remains constant through the zone of intense nucleation. Although the qualitative aspects of these relationships have been known for many years, this is the first time that an accurate analytical representation has been forthcoming.

The nucleation time $\tau_\mathrm{n}$ can now be obtained by equating the two expressions of $\ddot{Y}_\mathrm{W}/\dot{Y}_\mathrm{W}$ found by the two combinations of equations (3.1), so that

$$
k_p\tau_\mathrm{n} = \frac{\pi^{1/2}}{4}\frac{\Delta T_\mathrm{W}^3}{\gamma_\mathrm{s}\Theta_\mathrm{W}^2T_\mathrm{W}}.
$$

A typical value of this is 0.01, confirming the fundamental assumption $k_p\tau_\mathrm{n} \ll 1$. Also, we have

$$
\ddot{Y}_\mathrm{W} = \frac{4\gamma_\mathrm{s}}{L\pi^{1/2}}\frac{k_p^2}{k_p\tau_\mathrm{n}} \gg k_p^2,
$$

justifying the neglect of $C_q$ in equation (2.7).

Proc. R. Soc. Lond. A (1996)

### (c) Calculation of other Wilson-point properties

Once $\Delta T_{\mathrm{W}}$ and $\tau_{\mathrm{n}}$ have been found, other wetness properties at the Wilson point are easily calculated. The following expressions are quite general and are not restricted to the special case $\dot{k}_{p \mathrm{~W}}=0$.

The total droplet number per unit mass of mixture is given by

$$
N_{\mathrm{W}}=\int_{0}^{\infty} I(\tau) \mathrm{d} \tau=I_{\mathrm{W}} \int_{0}^{\infty} \mathrm{e}^{-\left(\tau / \tau_{\mathrm{n}}\right)^{2}} \mathrm{~d} \tau=\frac{1}{2} \pi^{1 / 2} I_{\mathrm{W}} \tau_{\mathrm{n}} .\qquad(3.4)
$$

As freshly nucleated droplets at the critical radius cannot grow against a falling gradient of subcooling, the Wilson point represents the cut-off point for droplet production. The total droplet number per unit mass of mixture $N$ therefore remains constant at the value of $N_{\mathrm{W}}$ along a fluid pathline following the Wilson point. If, at a later point on the pathline, the wetness fraction is $Y$, then (assuming there has been no secondary nucleation) the mass-mean droplet radius (denoted in the conventional way by $r_{30}$) is given by

$$
Y=\frac{4}{3} \pi r_{30}^{3} \rho_{\mathrm{L}} N_{\mathrm{W}} .\qquad(3.5)
$$

A knowledge of $N_{\mathrm{W}}$ effectively fixes the value of $r_{30}$ at all later points on the pathline. This is the reason why it is so important to be able to calculate the Wilson-point conditions accurately.

At the Wilson point itself, the wetness fraction is given by equation (2.17) and, hence, from equation (3.5),

$$
\left(r_{30}\right)_{\mathrm{W}}=\frac{C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} \tau_{\mathrm{n}}}{\pi^{1 / 6}}=0.826 C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} \tau_{\mathrm{n}} .
$$

The Sauter mean droplet radius $r_{32}$ is given by

$$
\begin{aligned}
\left(r_{32}\right)_{\mathrm{W}} & =\int_{0}^{\infty} I(\tau) r_{\mathrm{W}}^{3}(\tau) \mathrm{d} \tau \bigg/ \int_{0}^{\infty} I(\tau) r_{\mathrm{W}}^{2}(\tau) \mathrm{d} \tau \\
& =\frac{2 C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} \tau_{\mathrm{n}}}{\pi^{1 / 2}}=1.128 C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} \tau_{\mathrm{n}} .
\end{aligned}
$$

Other mean droplet radii can be found in a similar way.

The droplet size distribution functions at the Wilson point can also be calculated. The number distribution function $f_{\mathrm{n}}\left(r_{\mathrm{W}}\right)$ is defined such that $f_{\mathrm{n}}\left(r_{\mathrm{W}}\right) \mathrm{d} r_{\mathrm{W}}$ represents the fraction of all droplets having radii in the range $r_{\mathrm{W}} \rightarrow r_{\mathrm{W}}+\mathrm{d} r_{\mathrm{W}}$ and satisfies the integral

$$
\int_{0}^{\infty} f_{\mathrm{n}}\left(r_{\mathrm{W}}\right) \mathrm{d} r_{\mathrm{W}}=1 .
$$

The combination of the droplet number equation (3.4) with the approximate radius $r_{\mathrm{W}}(\tau)=C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} \tau$ of equation (2.16) gives

$$
\int_{0}^{\infty} \frac{I_{\mathrm{W}}}{C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} N_{\mathrm{W}}} \mathrm{e}^{-\left(r_{\mathrm{W}} / r_{\mathrm{nW}}\right)^{2}} \mathrm{~d} r_{\mathrm{W}}=1,
$$

where $r_{\mathrm{nW}}=C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} \tau_{\mathrm{n}}$. By comparison,

$$
f_{\mathrm{n}}\left(r_{\mathrm{W}}\right)=\frac{I_{\mathrm{W}}}{C_{r \mathrm{~W}} \Delta T_{\mathrm{W}} N_{\mathrm{W}}} \mathrm{e}^{-\left(r_{\mathrm{W}} / r_{\mathrm{nW}}\right)^{2}} .
$$

Evidently the droplet distribution is half-Gaussian.

### Table 1. An example for $p_\mathrm{W} = 0.1$ bar, $k_p = 1000\ \mathrm{s}^{-1}$

<table>
  <thead>
    <tr>
      <th>variable</th>
      <th>analytical</th>
      <th>numerical</th>
      <th>units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\Delta T_\mathrm{W}$</td>
      <td>35.1</td>
      <td>34.3</td>
      <td>K</td>
    </tr>
    <tr>
      <td>$N_\mathrm{W}$</td>
      <td>2.46e+18</td>
      <td>1.70e+18</td>
      <td>$(s\ \mathrm{kg})^{-1}$</td>
    </tr>
    <tr>
      <td>$r_{30}$</td>
      <td>2.69</td>
      <td>4.62</td>
      <td>nm</td>
    </tr>
    <tr>
      <td>$r_{32}$</td>
      <td>3.67</td>
      <td>8.37</td>
      <td>nm</td>
    </tr>
    <tr>
      <td>$Y_\mathrm{W}$</td>
      <td>0.02%</td>
      <td>0.07%</td>
      <td></td>
    </tr>
  </tbody>
</table>

The droplet mass distribution function $f_\mathrm{m}(r_\mathrm{W})$ is defined such that $f_\mathrm{m}(r_\mathrm{W}) \mathrm{d}r_\mathrm{W}$ represents the fraction of the total liquid mass contained in the radius range $r_\mathrm{W} \to r_\mathrm{W} + \mathrm{d}r_\mathrm{W}$. A similar analysis based on the integral for $Y_\mathrm{W}$ shows that

$$
f_\mathrm{m}(r_\mathrm{W}) = \frac{\pi^{1/2} I_\mathrm{W}}{C_{r\mathrm{W}} \Delta T_\mathrm{W} N_\mathrm{W}} \left( \frac{r_\mathrm{W}}{r_\mathrm{nW}} \right)^3 \mathrm{e}^{-(r_\mathrm{W}/r_\mathrm{nW})^2}.
$$

### 4. Validation and example calculations

Although the assumptions and approximations of the analysis have been justified as far as possible in the previous sections, the only completely convincing validation can be by comparison with numerical solution of the original equations. We therefore present the results of a typical calculation to illustrate the level of accuracy achieved. The numerical calculation essentially involves the Runge–Kutta integration of the energy equation (2.2), the nucleation equation (2.9) and the droplet growth equation (2.13) together with the Clusius–Clapeyron equation (2.3) and the equation of state for the vapour phase. The method is very similar to that described by Young (1992) and White & Young (1993).

#### (a) Comparison with a numerical solution

The calculation presented refers to the inviscid expansion of pure steam from a dry saturated condition to a Wilson point pressure $p_\mathrm{W} = 0.1$ bar at a constant rate of expansion $k_p = 1000\ \mathrm{s}^{-1}$, a case on which all the 'typical values' of constants and coefficients in the previous sections are based.

Table 1 shows that the maximum subcooling $\Delta T_\mathrm{W}$ calculated by solving the single equation (3.3) is accurate to within 0.8 K and the total number of droplets accurate to within about 30%. It is noted, however, that the Sauter mean radius at the Wilson point obtained from the full numerical calculation is considerably larger than that determined by the analytical method. This is attributed to the neglect of the slow-growth period of the droplets at the time of nucleation, cf. figure 1. This disparity is not important, however, because all droplets grow very rapidly downstream of the Wilson point and the final droplet radius after full reversion to equilibrium is essentially determined by the maximum subcooling at the Wilson point.

Satisfactory accuracy has been achieved because the fundamental assumption of $k_p \tau_\mathrm{n} \ll 1$ is sound: in the present example, $k_p \tau_\mathrm{n} = 0.013$. This central assumption justifies the neglect of the changes of many variables except $\Delta T_\mathrm{W}$. For example, the change of the droplet growth coefficient $C_r$ is neglected because its effect across the intense nucleation zone is measured by $k_{r\mathrm{W}} \tau_\mathrm{n}$, which in the present example is

Proc. R. Soc. Lond. A (1996)

![](./images/812034414711144449_4.jpg)

Figure 2. The Wilson subcooling $\Delta T_{\mathrm{W}}$ as a function of the constant expansion rate $k_{p}$. The five curves are for different pressures at the Wilson point $p_{\mathrm{W}}$.

$-0.014$. The change of $\Theta$ in the exponent of the nucleation rate is characterized by its time constant $\tau_{\Theta}$, cf. equation (2.11), and the ratio $\tau_{\Theta}/\tau_{\mathrm{n}}=58.6$ indicates that it is much larger than the intense nucleation zone.

Apart from the above approximations, we also assumed that droplets have grown considerably larger than the critical value but nonetheless still remain small compared with the molecular mean free path, cf. inequality (2.12). The validity of that assumption is now demonstrated by the results of the example, $r_{32}=6.83$, $r_{\mathrm{c}}=\ell/130$.

### (b) Example calculations

We now present the results of some calculations to illustrate the power of the analytical approach and its inherent possibilities. As a basis, we take pure steam condensing at a range of Wilson-point pressures from 0.1 to 10 bar and a range of expansion rates $k_{p}$ from $10^{2}$ to $10^{6}\ \mathrm{s}^{-1}$. In all the calculations, it was assumed that $k_{p}$ remained constant throughout the zone of intense nucleation.

It is important to appreciate that the calculations illustrate trends and do not give precise results which compare formally with experimental measurements. This is not to imply that the analytical method is incapable of such accuracy, but simply that the necessary fine adjustment of the governing equations has not been undertaken. Experience has shown, for example, that the classical nucleation rate equation does not describe precisely the homogeneous nucleation of steam (and many other fluids) and that, to obtain good agreement with experiments, various corrections to the theory should be included. Also, for nucleation at higher pressures, it is important that the governing equations should be modified to include imperfect gas effects. These modifications have been omitted here so as not to over complicate the presentation.

Equation (3.3) is first solved to obtain $\Delta T_{\mathrm{W}}$. Figure 2 shows the variation of the Wilson subcooling with $k_{p}$ for a range of Wilson point pressures $p_{\mathrm{W}}=0.1\rightarrow10$ bar. $\Delta T_{\mathrm{W}}$ increases with $k_{p}$ at constant Wilson-point pressure $p_{\mathrm{W}}$ and decreases with $p_{\mathrm{W}}$ at the same expansion rate $k_{p}$.

Now for $p_{\mathrm{W}}=0.1$ bar, we plot the variations of other properties at the Wilson point as functions of the expansion rate $k_{p}$. Figures $3a,b$ show that the nucleation time scale $\tau_{\mathrm{n}}$ is always very short compared with the time it takes for the pressure to change, $k_{p}\tau_{\mathrm{n}}\ll1$. Both the droplet number $N_{\mathrm{W}}$ and the wetness fraction at the Wilson point $Y_{\mathrm{W}}$ increase with $k_{p}$ but the mean radii $r_{30},r_{32}$ at the Wilson point decrease with $k_{p}$.

![](./images/812034414711144449_5.jpg)

Figure 3. Properties at the Wilson point as functions of the expansion rate $k_p$ for a fixed pressure $p_W = 0.1$ bar: (a) the nucleation time scale $\tau_{\mathrm{n}}$; (b) $k_p \tau_{\mathrm{n}}$, the ratio of the nucleation time $\tau_{\mathrm{n}}$ to the time scale of pressure change $k_p^{-1}$; (c) the droplet number per unit mass of mixture at and downstream of the Wilson point, $\log_{10} N_W$; (d) the wetness fraction at the Wilson point, $Y_W$; (e) is the mass-mean radius $r_{30}$; (f) is the Sauter-mean radius, $r_{32}$.

## 5. Concluding remarks

The paper has described an analytical method for calculating the homogeneous nucleation of a pure vapour in a high-speed flow. The method is mathematically simple and, despite some apparently significant approximations, is still remarkably accurate compared with a full numerical solution. The main result consists of a single algebraic expression relating the Wilson subcooling to the controlling parameters, the most important of which is the local 'rate of expansion'. Once the subcooling has been found, all the wetness properties at the Wilson point can be easily calculated, including the droplet size distribution.

By working in a Lagrangian frame of reference, the nucleation and droplet-growth kinetics have been divorced from the fluid mechanics of the particular problem under consideration with the result that the solution method is independent of any particular flow solver. This flexibility, coupled with the simplicity and accuracy of the method, suggests that, with development, it might form the basis for a three- dimensional calculation procedure for homogeneously nucleating flows.

## References

Bakhtar, F. & So, K. S. 1991 A study of nucleating flow of steam in a cascade of supersonic blading by the time-marching method. *Int. J. Heat Fluid Flow* **12**, 54-62.

Clarke, J. H. & Delale, C. F. 1986 Nozzle flows with non-equilibrium condensation. *Physics Fluids* **29**, 1398-1413.

Dobbins, R. A. 1983 A theory of the Wilson line for steam at low pressures. *Trans. ASME* **105**, 414-422.

Proc. R. Soc. Lond. A (1996)

An analytical solution for nucleating flows

Gyarmathy, G. & Meyer, H. 1965 Spontaneous condensation phenomena. I, II. *V.D.I. Forschungsheft 508* (Central Electricity Generating Board translation no. C.E.4160).

McDonald, J. E. 1962 Homogeneous nucleation of vapour condensation. I. Thermodynamic aspects. *Am. J. Phys.* **30**, 870-877.

McDonald, J. E. 1963 Homogeneous nucleation of vapour. II. Kinetic aspects. *Am. J. Phys.* **31**, 31-41.

Oswatitsch, Von Kl. 1941 Die Nebelbildung in Windkanälen und ihr Einfluß auf Modellversuche. *Jahrbuch der Deutschen Luftfahrtforschung*, I, 692-703.

Schnerr, G. H. & Dohrmann, U. 1989 Transonic flow around airfoils with relaxation and energy supply by homogeneous condensation. In *AIAA 20th Fluid Dynamics, Plasma Dynamics and Lasers Conf.* (Buffalo), paper no. AIAA 89-1834.

Schnerr, G. H., Adam St. & Mundinger, G. 1994 Frequency control of shock oscillations in high speed two-phase flow. In *Proc. 4th Triennial Int. Symp. on Fluid Control, Measurement and Visualization (FLUCOME'94)* (ed. P. Hebrard), vol. 2, pp. 957-962.

White, A. J. & Young, J. B. 1993 A time-marching method for the prediction of two-dimensional, unsteady flows of condensing steam. *AIAA J. Propulsion Power* **9**, 579-587.

Young, J. B. 1982 The spontaneous condensation of steam in supersonic nozzles. *Physico-Chemical-Hydrodynamics* **3**, 57-82.

Young, J. B. 1991 The condensation and evaporation of liquid droplets in a pure vapour at arbitrary Knudsen number. *Int. J. Heat Mass Transfer* **34**, 1649-1661.

Young, J. B. 1992 Two-dimensional, nonequilibrium, wet-steam calculations for nozzles and turbine cascades. *Trans. ASME, J. Turbomachinery* **114**, 569-579.

Received 25 July 1995; revised 4 October 1995; accepted 30 October 1995

*Proc. R. Soc. Lond. A* (1996)