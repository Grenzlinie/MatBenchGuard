# Theoretical and numerical study of lamellar eutectoid growth influenced by volume diffusion.

Kumar Ankit$^{a,*}$, Abhik Choudhury$^{a,b}$, Cheng Qin$^{a}$, Sebastian Schulz$^{a}$, Malte McDaniel$^{a}$, Britta Nestler$^{a}$

$^{a}$Karlsruhe Institute of Technology (KIT), IAM-ZBS, Haid-und-Neu-Str. 7, D-76131 Karlsruhe, Germany

$^{b}$Laboratoire PMC (Condensed Matter Physics) - Ecole Polytechnique 91128, Palaiseau Cedex, France

## Abstract
We investigate the lamellar growth of pearlite at the expense of austenite during the eutectoid transformation in steel. To begin with, we extend the Jackson-Hunt-type calculation (previously used to analyze eutectic transformation) to eutectoid transformation by accounting for diffusion in all the phases. Our principal finding is that the growth rates in presence of diffusion in all the phases is different as compared to the case when diffusion in growing phases is absent. The difference in the dynamics is described by a factor $'\rho'$ which comprises of the ratio of the diffusivities of the bulk and the growing phases, along with the ratios of the slopes of the phase co-existence lines. Thereafter, we perform phase-field simulations, the results of which are in agreement with analytical predictions. The phase-field simulations also reveal that diffusion in austenite as well as ferrite leads to the formation of tapered cementite along with an overall increase in the transformation kinetics as compared to diffusion in austenite (only). Finally, it is worth noting that the aim of present work is not to consider the pearlitic transformation in totality, rather it is to isolate and thereby investigate the influence of diffusivity in the growing phases on the front velocity.

Keywords: Pearlite, Phase-field method, Coupled-growth, Jackson-Hunt Analysis

*Corresponding author. Tel.: +49 721 608-45022.
Email address: kumar.ankit@hs-karlsruhe.de (Kumar Ankit)

Preprint submitted to Acta Materialia
October 29, 2018

### 1. Introduction

The mechanism of eutectoid transformation in steel has been a topic of theoretical as well as experimental investigation since inception of steel as a structural material. The eutec-toid transformation involves the formation of a pearlite colony which appears as alternate lamellae of ferrite and cementite phases, that grow as a common front with the austenite. Cementite is the carbon rich phase whereas the carbon solubility in ferrite is relatively quite low [1, 2, 3].

The two principal mechanisms of eutectoid reaction, i.e. austenite to pearlite phase trans-formation, cited in the literature are volume diffusion and grain boundary diffusion. The former suggests the volume diffusion of carbon ahead of the phase interface, while the latter emphasizes the role of grain boundary diffusion as the rate controlling step. The pioneering work of Zener [4], Hillert [5] and Tiller [6] on pearlite formation explains the relation between the lamellar spacing and undercooling during the phase transformation. In spite of making a generous effort to explain the phenomenology of pearlitic transfor-mation, the classical Zener-Hillert model shows large deviations from the experimentally measured lamellar growth velocities. The model assumes no diffusion in the ferrite phase whilst considering diffusion in austenite phase (only). This would be a reasonable assump-tion in case of eutectic solidification problem, where the diffusivity in solid is lower than the diffusivity in liquid (bulk phase) by a factor of 1000. However, in a solid state phase transformation like the eutectoid reaction, the diffusivity in austenite (bulk phase) is com-parable to the ferrite. Thus, it is reasonable to expect some disagreement of experimental velocities with corresponding values derived from the Zener-Hillert co-operative growth model.

Jackson and Hunt [7] adapt the Zener-Hillert model for investigating directional solidifi-cation in eutectics with a constant velocity of growth front, which broadly falls in the same class of moving boundary problem as the eutectoid transformation. Recently, Nakajima et. al [8] use the multi phase-field method to simulate the co-operative pearlite growth by accounting for diffusion in the ferrite as well as the austenite phase. They predict a suc-cessive process of diffusion in ferrite and growth of cementite from the ferrite, resulting in an increase of the kinetics of pearlitic transformation by a factor of four as compared to growth from austenite exclusively. The simulated cementite lamella is found to be tapered and exhibits a conical morphology. This is interpreted as an effect of diffusion in ferrite. Steinbach and Plapp [9] claim an overlap of phase-field results with Hillert's model in absence of diffusion in ferrite. Further, they couple a stress-driven diffusion field to the phase field and study the effect of transformation strains. However, Pandit and Bhadeshia [10] argue that pearlite forms by reconstructive transformation, in which case, transforma-

tion strains should not be significant. They also emphasize the need to consider both the mechanisms, volume as well as interfacial diffusion, simultaneously for an overlap with experimental findings.

In the present article, we extend our previous work on Jackson-Hunt (JH) analysis of ternary eutectic alloys [11] to study the eutectoid transformation. The main question which we address is: Can a JH type analysis (previously done for eutectics) be extended to pre- dict lamellar growth velocities of pearlite by accounting for diffusion in austenite as well as ferrite? In order to answer this question, we first extend the JH analysis for eutectics by accounting for diffusion in austenite as well as ferrite. We analyze the case of sta- ble lamellar coupled growth and derive the expressions for lamellar growth velocity as a function of undercooling and lamellar spacing. This is followed by comparison of analyt- ical prediction with the numerical results of a thermodynamically consistent phase-field model.

The remainder of this article is organized as follows: In section 2 we derive an expression for lamellar growth velocity as a function of undercooling and spacing in pearlite using a JH type analysis. In section 3, the quantitative phase-field model used to simulate pearlite growth is outlined. In section 4, we describe the thermodynamic data-fitting procedure to approximate the variation of grand-potential of the respective phases as a function of chemical potential. In section 5 we derive the relation between the simulation parameters and corresponding quantities in the sharp interface limit. In section 6 we compare the lamellar growth velocity obtained from phase-field simulations to the analytical expres- sions for the velocity, derived in section 2. Section 7 concludes the article.

## 2. Theoretical analysis of coupled growth

We consider the diffusion of the components A and B ahead of the planar eutectoid front. For calculating the concentration fields ahead of the growth front in question, we make the following Fourier series expansion for $c_A$ and $c_B$,

$$
c_{X}^{\gamma}=\sum_{n=-\infty}^{\infty} X_{n} e^{i k_{n} x-q_{n} z}+\left(c_{X}^{\infty}\right)_{\gamma}, \quad X=A, B \tag{1}
$$

where $\gamma$ is the austenite phase. In the respective growing phases ($\alpha$ and $\beta$) the concentra- tion fields can be respectively written as,

$$
c_{X}^{\nu}=\sum_{n=-\infty}^{\infty} X_{n} e^{i k_{n} x+q_{n} z}+\left(c_{X}^{\infty}\right)_{\nu}, \quad X=A, B \quad \nu=\alpha, \beta. \tag{2}
$$


An elaborate description of the terms involved in the above expression and derivation from a stationary diffusion equation has been described in detail in the previous work on eutectic growth [11]. In the field under consideration, the growth front is assumed to be at $z=0$. Further, $z>0$ depicts austenite phase where exponential profiles for the concentrations of components A and B exist. For $z<0$, the composition profile in pearlite (for ferrite and cementite phases) have similar exponential profiles. Therefore, to account for the symmetry across the interface, we change the sign of the exponent $e^{-q_{n} z}$ to $e^{q_{n} z}$ when treating the concentration profiles in ferrite and cementite phases $(\forall z<0)$.

In the Jackson-Hunt analysis for the calculation of diffusion field in liquid and solid, the Stefan's condition at $\nu-\gamma$ interface, which expresses mass-conservation upon the phase transformation reads as

$$
\left.D^{\nu} \partial_{n} c_{X}^{\nu}\right|_{z=0}-\left.D^{\gamma} \partial_{n} c_{X}^{\gamma}\right|_{z=0}=v_{n} \Delta c_{X}^{\nu}, \quad \nu=\alpha, \beta \tag{3}
$$

where $\partial_{n} c_{X}^{\nu}$ denotes the partial derivative of $c_{X}^{\nu}$ in the direction normal to the interface. The quantity $v_{n}$ is the normal velocity of the interface (positive for a growing front) and $\Delta c_{X}^{\nu}=c_{X}^{\gamma}-c_{X}^{\nu}$. $D^{\gamma}$ and $D^{\nu}$ are chemical diffusion coefficients for bulk and growing phases respectively. For using the Stefan condition, we take the derivative of $c_{X}^{\nu}$ with respect to the 'z' coordinate

$$
\left.\partial_{z} c_{X}^{\nu}\right|_{z=0}=\sum_{n=-\infty}^{\infty} q_{n} X_{n} e^{i k_{n} x} \quad \nu=\alpha, \beta \tag{4}
$$

for the growing phases and

$$
\left.\partial_{z} c_{X}^{\gamma}\right|_{z=0}=\sum_{n=-\infty}^{\infty}-q_{n} X_{n} e^{i k_{n} x}, \tag{5}
$$

for the austenite phase. Integration across one lamella period (lamellar spacing) $\lambda$ gives,

$$
q_{n} X_{n}^{\alpha} D^{\alpha} \eta_{\alpha} \lambda+q_{n} X_{n}^{\beta} D^{\beta} \eta_{\beta} \lambda+q_{n} X_{n}^{\gamma} D^{\gamma} \lambda=\sum_{j=0}^{M-1} \int_{x_{j} \lambda}^{x_{j+1} \lambda} v_{n} \Delta c_{X}^{\nu_{j}} e^{-i k_{n} x} d x. \tag{6}
$$

where, M denotes the number of lamellae and $\eta_{\alpha}$ and $\eta_{\beta}$ are the respective phase volume fractions. In the above equation, there are three sets of unknowns $X_{n}^{\alpha}, X_{n}^{\beta}$ and $X_{n}^{\gamma}$ in contrast to the classical Jackson-Hunt type analysis with vanishing diffusivity in the solid, where $X_{n}^{\gamma}$ remains the only unknown, and is thereby fixed by the property of orthogonality of the respective modes. In the present situation, we need a relation among the fourier

coefficients, to fix the respective unknowns. We achieve these relations by arguing that the constitutional undercooling can be derived equivalently by using either the shifts in the equilibrium concentrations of the bulk or the growing phases. Hence, the resultant shift in the average concentration in the $\gamma$ phase and the corresponding shift in the $\alpha$ and $\beta$ phases must be constrained by the relation,

$$
m_{X}^{\alpha}\left(\left\langle c_{X}^{\alpha}\right\rangle-c_{X, E}^{\alpha}\right)=m_{X}^{\alpha, \gamma}\left(\left\langle c_{X}^{\gamma}\right\rangle-c_{X, E}^{\gamma}\right)
\tag{7}
$$

$$
m_{X}^{\beta}\left(\left\langle c_{X}^{\beta}\right\rangle-c_{X, E}^{\beta}\right)=m_{X}^{\beta, \gamma}\left(\left\langle c_{X}^{\gamma}\right\rangle-c_{X, E}^{\gamma}\right)
\tag{8}
$$

where $\langle c_{X}^{\alpha}\rangle$, $\langle c_{X}^{\beta}\rangle$ and $\langle c_{X}^{\gamma}\rangle$ denote the average phase concentrations at the interface, while $c_{X, E}^{\alpha}$, $c_{X, E}^{\beta}$ and $c_{X, E}^{\gamma}$ are the eutectoid compositions. $m_{X}^{\alpha}$ and $m_{X}^{\beta}$ represent the slopes (with respect to the concentration of component 'X') of the $\alpha$ and $\beta$ phase in equilibrium with austenite. Similarly, $m_{X}^{\alpha, \gamma}$ and $m_{X}^{\beta, \gamma}$ represent the slopes of the co-existence lines of the austenite phase in equilibrium with $\alpha$ and $\beta$ phases respectively.

While such an equation certainly has multiple solutions, we invoke the following assumption,

$$
m_{X}^{\alpha} X_{n}^{\alpha}=m_{X}^{\alpha, \gamma} X_{n}^{\gamma}
\tag{9}
$$

$$
m_{X}^{\beta} X_{n}^{\beta}=m_{X}^{\beta, \gamma} X_{n}^{\gamma}
\tag{10}
$$

which satisfies the given property. Substituting the preceding condition in equation 6 yields,

$$
\begin{aligned}
q_{n} X_{n}^{\gamma} \delta_{n m} \lambda\left[\frac{D^{\alpha}}{D^{\gamma}} \frac{m_{X}^{\alpha, \gamma}}{m_{X}^{\alpha}} \eta_{\alpha}+\frac{D^{\beta}}{D^{\gamma}} \frac{m_{X}^{\beta, \gamma}}{m_{X}^{\beta}} \eta_{\beta}+1\right] &=\sum_{j=0}^{M-1} \int_{x_{j} \lambda}^{x_{j+1} \lambda} \frac{v_{n}}{D^{\gamma}} \Delta c_{X}^{\nu_{j}} e^{-i k_{n} x} d x \\
&=\frac{2}{l} \sum_{j=0}^{M-1} \int_{x_{j} \lambda}^{x_{j+1} \lambda} e^{-i k_{n} x} \Delta c_{X}^{\nu_{j}} d x
\end{aligned}
\tag{11}
$$

and hence, we rearrange to

$$
X_{n}^{\gamma}=\frac{4}{l q_{n} \lambda k_{n}\left[\frac{D^{\alpha}}{D^{\gamma}} \frac{m_{X}^{\alpha, \gamma}}{m_{X}^{\alpha}} \eta_{\alpha}+\frac{D^{\beta}}{D^{\gamma}} \frac{m_{X}^{\beta, \gamma}}{m_{X}^{\beta}} \eta_{\beta}+1\right]} \sum_{j=0}^{M-1} \Delta c_{X}^{\nu_{j}} e^{-i k_{n} \lambda\left(x_{j+1}+x_{j}\right) / 2} \sin \left[k_{n} \lambda\left(x_{j+1}-x_{j}\right) / 2\right]
\tag{12}
$$

where $\nu_j$ represents the name of one of the growing phases $(\alpha, \beta)$ occurring in the sequence of M lamellae $(\nu_0, \nu_1, \nu_2 \dots \nu_{M-1})$ periodically arranged with a repeat distance (lamellar spacing) $\lambda$. The symbol $l$ appearing in the denominator represents the characteristic length scale of the concentration boundary layer. By considering the negative summation indices, we can formulate real and imaginary combinations of these coefficients,

$$
X_{n}^{\gamma}+X_{-n}^{\gamma}=\frac{8}{l q_{n} \lambda k_{n} \rho} \sum_{j=0}^{M-1} \Delta c_{X}^{\nu_{j}} \cos \left[k_{n} \lambda\left(x_{j+1}+x_{j}\right) / 2\right] \sin \left[k_{n} \lambda\left(x_{j+1}-x_{j}\right) / 2\right]
$$

$$
i\left(X_{n}^{\gamma}-X_{-n}^{\gamma}\right)=\frac{8}{l q_{n} \lambda k_{n} \rho} \sum_{j=0}^{M-1} \Delta c_{X}^{\nu_{j}} \sin \left[k_{n} \lambda\left(x_{j+1}+x_{j}\right) / 2\right] \sin \left[k_{n} \lambda\left(x_{j+1}-x_{j}\right) / 2\right] \text { (13) }
$$

where,
$$
\rho=\frac{D^{\alpha}}{D^{\gamma}} \frac{m_{X}^{\alpha, \gamma}}{m_{X}^{\alpha}} \eta_{\alpha}+\frac{D^{\beta}}{D^{\gamma}} \frac{m_{X}^{\beta, \gamma}}{m_{X}^{\beta}} \eta_{\beta}+1\qquad(14)
$$

Therefore, equation 1 can be rewritten as,

$$
\begin{aligned}
c_{X}^{\gamma}=\left(c_{X}^{\infty}\right)_{\gamma}+\frac{X_{0}^{\gamma}}{\rho}+\frac{1}{\rho} \sum_{j=0}^{M-1} & \sum_{n=1}^{\infty} \frac{8}{l q_{n} \lambda k_{n}} \cos \left[k_{n} \lambda\left(x_{j+1}+x_{j}\right) / 2\right] \sin \left[k_{n} \lambda\left(x_{j+1}-x_{j}\right) / 2\right] \cos \left(k_{n} x\right) \\
+ & \frac{1}{\rho} \sum_{j=0}^{M-1} \sum_{n=1}^{\infty} \frac{8}{l q_{n} \lambda k_{n}} \sin \left[k_{n} \lambda\left(x_{j+1}+x_{j}\right) / 2\right] \sin \left[k_{n} \lambda\left(x_{j+1}-x_{j}\right) / 2\right] \sin \left(k_{n} x\right)
\end{aligned}
$$

The general expression for the mean concentration $\left\langle c_{X}^{\gamma}\right\rangle_{m}$ ahead of the $m$th phase of the phase sequence can be calculated to yield

$$
\begin{aligned}
\left\langle c_{X}^{\gamma}\right\rangle_{m}= & \frac{1}{\left(x_{m+1}-x_{m}\right) \lambda} \int_{x_{m} \lambda}^{x_{m+1} \lambda} c_{X}^{\gamma} d x \\
= & \left(c_{X}^{\infty}\right)_{\gamma}+\frac{X_{0}^{\gamma}}{\rho}+\frac{1}{\left(x_{m+1}-x_{m}\right) \rho} \sum_{n=1}^{\infty} \sum_{j=0}^{M-1}\left\{\frac{16}{\lambda^{2} k_{n}^{2} l q_{n}} \Delta c_{X}^{\nu_{j}}\right. \\
& \left.\times \sin \left[\pi n\left(x_{m+1}-x_{m}\right)\right] \sin \left[\pi n\left(x_{j+1}-x_{j}\right)\right] \times \cos \left[\pi n\left(x_{m+1}+x_{m}-x_{j+1}-x_{j}\right)\right]\right\}
\end{aligned}
$$

For the binary eutectoid system with phases $\alpha, \beta$, and $\gamma$, we can derive the average concentrations of the components A, B by setting, $x_{0}=0, x_{1}=\eta_{\alpha}, x_{2}=1$ and applying

equation 16

$$
\begin{aligned}
\left\langle c_{X}^{\gamma}\right\rangle_{\alpha} & =\left(c_{X}^{\infty}\right)_{\gamma}+\frac{X_{0}^{\gamma}}{\rho}+\frac{1}{\eta_{\alpha} \rho} \sum_{n=1}^{\infty}\left\{\frac{16}{\lambda^{2} k_{n}^{2} l q_{n}}\left(\Delta c_{X}^{\alpha}-\Delta c_{X}^{\beta}\right) \times \sin ^{2}\left(\pi n \eta_{\alpha}\right)\right\} \\
& \cong\left(c_{X}^{\infty}\right)_{\gamma}+\frac{X_{0}^{\gamma}}{\rho}+\frac{2 \lambda}{\eta_{\alpha} \rho l} \mathcal{P}\left(\eta_{\alpha}\right) \Delta c_{X}
\end{aligned}
\tag{17}
$$

$$
\left\langle c_{X}^{\gamma}\right\rangle_{\beta}=\left(c_{X}^{\infty}\right)_{\gamma}+\frac{X_{0}^{\gamma}}{\rho}-\frac{2 \lambda}{\left(1-\eta_{\alpha}\right) \rho l} \mathcal{P}\left(1-\eta_{\alpha}\right) \Delta c_{X}
\tag{18}
$$

with $k_n=2\pi n/\lambda, q_n\approx k_n, \lambda/l\ll1, \Delta c_X=\Delta c_X^\alpha-\Delta c_X^\beta$ and the dimensionless function

$$
\mathcal{P}(\eta)=\sum_{n=1}^{\infty} \frac{1}{(\pi n)^{3}} \sin ^{2}(\pi n \eta)
\tag{19}
$$

which has the property $\mathcal{P}(\eta)=\mathcal{P}(1-\eta)=\mathcal{P}(\eta-1)$

Incorporating the Gibbs-Thomson effect and using the relation $l=2D^\gamma/v$ leads to,

$$
\Delta T_{\alpha}=-m_{B}^{\alpha, \gamma} B_{0}^{\gamma}-\frac{\lambda v}{\eta_{\alpha} D^{\gamma} \rho} \mathcal{P}\left(\eta_{\alpha}\right) m_{B}^{\alpha, \gamma} \Delta c_{B}+\Gamma_{\alpha}\langle\kappa\rangle_{\alpha}
\tag{20}
$$

$$
\Delta T_{\beta}=-m_{A}^{\beta, \gamma} A_{0}^{\gamma}-\frac{\lambda v}{\eta_{\beta} D^{\gamma} \rho} \mathcal{P}\left(\eta_{\beta}\right) m_{A}^{\beta, \gamma} \Delta c_{A}+\Gamma_{\beta}\langle\kappa\rangle_{\beta}
\tag{21}
$$

where $\langle\kappa\rangle_{\alpha}=2 \sin \theta_{\alpha \beta} /\left(\eta_{\alpha} \lambda\right),\langle\kappa\rangle_{\beta}=2 \sin \theta_{\beta \alpha} /\left(\eta_{\beta} \lambda\right), \Gamma_{\alpha}=\tilde{\sigma}_{\alpha \gamma} T_{E} / L_{\alpha}$ and $\Gamma_{\beta}=$
$\tilde{\sigma}_{\beta \gamma} T_{E} / L_{\beta}$. Additionally, for a binary alloy, the coefficients follow the condition, $B_{0}^{\gamma}=$
$-A_{0}^{\gamma}$. The global front undercooling is determined using the assumption of equal interface
undercooling $\Delta T_{\alpha}=\Delta T_{\beta}=\Delta T$. For a constant undercooling, we deduce the rela-
tion between the growth velocity 'v' and lamellar width '$\lambda$' by eliminating the unknown
amplitude $A_{0}^{\gamma}$ (or $B_{0}^{\gamma}$) as,

$$
v=\frac{\Delta T-\frac{2 T_{E}}{\lambda\left(m_{A}^{\beta, \gamma}+m_{B}^{\alpha, \gamma}\right)}\left[\frac{m_{B}^{\alpha, \gamma} \tilde{\sigma}_{\beta \gamma} \sin \theta_{\beta \alpha}}{\eta_{\beta} L_{\beta}}+\frac{m_{A}^{\beta, \gamma} \tilde{\sigma}_{\alpha \gamma} \sin \theta_{\alpha \beta}}{\eta_{\alpha} L_{\alpha}}\right]}{-\frac{\lambda}{D^{\gamma} \rho}\left(\frac{m_{A}^{\beta, \gamma} m_{B}^{\alpha, \gamma}}{m_{A}^{\beta, \gamma}+m_{B}^{\alpha, \gamma}}\right)\left[\frac{\mathcal{P}\left(\eta_{\alpha}\right) \Delta c_{B}}{\eta_{\alpha}}+\frac{\mathcal{P}\left(\eta_{\beta}\right) \Delta c_{A}}{\eta_{\beta}}\right]}.
\tag{22}
$$

It is worth clarifying that in the derived expression for binary eutectoids above, the growing
phases $\alpha$ and $\beta$ posses slopes with opposite signs for the same component. $m_{A}^{\beta, \gamma}$ and
$m_{B}^{\alpha, \gamma}$ denote the slopes of the phases $\beta$ and $\alpha$ respectively with respect to the minority

component in each phase. Hence, they will always be of the same sign. Therefore, for eutectoid systems, the denominator $m_{A}^{\beta, \gamma}+m_{B}^{\alpha, \gamma}$, is non-vanishing. Further, it is important to point the difference of the preceding expression with respect to the relations for the velocity derived for eutectic solidification in absence of diffusion in solid-phases [7, 11]. The velocity differs by the factor $\rho$, which depends on the ratio of the diffusivities in the growing phases and the bulk phase, together with the ratio of the slopes of the respective phase-coexistence lines.

## 3. Phase-field model

In the following investigation, we study phase evolution in a ternary system using a quan- titative phase-field model [12]. We start by writing down the grand-potential functional of the system, incorporating the interfacial and bulk contributions of the respective phases. The evolution equations for the phase and concentration fields can be evaluated in the standard way. Phase evolution is determined by the phenomenological minimization of the modified functional which is formulated as the grand potential functional,

$$
\Omega(T, \boldsymbol{\mu}, \boldsymbol{\phi})=\int_{V}\left(\Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})+\left(\epsilon \tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})+\frac{1}{\epsilon} \tilde{w}(\boldsymbol{\phi})\right)\right) d V. \quad(23)
$$

We write the grand potential density $\Psi$, as an interpolation of the individual grand potential densities $\Psi_{\alpha}$, where $\Psi_{\alpha}$ are functions of the chemical potential $\boldsymbol{\mu}$ and temperature T in the system,

$$
\Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})=\sum_{\alpha=1}^{N} \Psi_{\alpha}(T, \boldsymbol{\mu}) h_{\alpha}(\boldsymbol{\phi}) \quad \text { with, } \quad(24)
$$

$$
\Psi_{\alpha}(T, \boldsymbol{\mu})=f_{\alpha}\left(\boldsymbol{c}^{\alpha}(\boldsymbol{\mu}), T\right)-\sum_{i=1}^{K-1} \mu_{i} c_{i}^{\alpha}(\boldsymbol{\mu}, T)
$$

The concentration $c_{i}^{\alpha}(\boldsymbol{\mu}, T)$ is an inverse of the function $\mu_{i}^{\alpha}(\boldsymbol{c}, T)$ for every phase $\alpha$ and component i. From equation 24, the following relation can be derived,

$$
\frac{\partial \Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})}{\partial \mu_{i}}=\sum_{\alpha=1}^{N} \frac{\partial \Psi_{\alpha}(T, \boldsymbol{\mu})}{\partial \mu_{i}} h_{\alpha}(\boldsymbol{\phi}).
$$

where, $h_{\alpha}(\phi)=\phi_{\alpha}^{2}\left(3-2 \phi_{\alpha}\right)+2 \phi_{\alpha} \sum_{\beta<\gamma,(\beta, \gamma) \neq \alpha} \phi_{\beta} \phi_{\gamma}$. Since, the grand potential density $\Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})$, is the Legendre transform of the free energy density of the system $f(T, \boldsymbol{c}, \boldsymbol{\phi})$,

and from their coupled relation $\frac{\partial \Psi\left(T, \boldsymbol{\mu}, \boldsymbol{\phi}\right)}{\partial \mu_{i}}=-c_{i}$, it follows that,

$$
c_{i}=\sum_{\alpha=1}^{N} c_{i}^{\alpha}(\boldsymbol{\mu}, T) h_{\alpha}(\boldsymbol{\phi}). \tag{27}
$$

The evolution equation for the N phase-field variables can be written as,

$$
\tau \epsilon \frac{\partial \phi_{\alpha}}{\partial t}=\epsilon\left(\nabla \cdot \frac{\partial \tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})}{\partial \nabla \phi_{\alpha}}-\frac{\partial \tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})}{\partial \phi_{\alpha}}\right)-\frac{1}{\epsilon} \frac{\partial \tilde{w}(\boldsymbol{\phi})}{\partial \phi_{\alpha}}-\frac{\partial \Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})}{\partial \phi_{\alpha}}-\Lambda, \tag{28}
$$

where $\Lambda$ is the Lagrange parameter to maintain the constraint $\sum_{\alpha=1}^{N} \phi_{\alpha}=1$. $\tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})$ represents the gradient energy density and has the form,

$$
\tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})=\sum_{\substack{\alpha, \beta=1 \\(\alpha<\beta)}}^{N, N} \tilde{\sigma}_{\alpha \beta}\left|q_{\alpha \beta}\right|^{2}, \tag{29}
$$

where $q_{\alpha \beta}=\left(\phi_{\alpha} \nabla \phi_{\beta}-\phi_{\beta} \nabla \phi_{\alpha}\right)$ is a normal vector to the $\alpha-\beta$ interface. The double obstacle potential $\tilde{w}(\boldsymbol{\phi})$ which is previously described in [13, 14, 15] can be written as,

$$
\tilde{w}(\boldsymbol{\phi})=\frac{16}{\pi^{2}} \sum_{\substack{\alpha, \beta=1 \\(\alpha<\beta)}}^{N, N} \tilde{\sigma}_{\alpha \beta} \phi_{\alpha} \phi_{\beta}, \tag{30}
$$

where $\tilde{\sigma}_{\alpha \beta}$ is the surface energy. The parameter $\tau$ is written as $\frac{\sum_{\alpha<\beta}^{N, N} \tau_{\alpha \beta} \phi_{\alpha} \phi_{\beta}}{\sum_{\alpha<\beta}^{N, N} \phi_{\alpha} \phi_{\beta}}$, where $\tau_{\alpha \beta}$ is the relaxation constant of the $\alpha-\beta$ interface.

The concentration fields are obtained by a mass conservation equation for each of the $K-1$ independent concentration variables $c_{i}$. The evolution equation for the concentration fields can be derived as,

$$
\frac{\partial c_{i}}{\partial t}=\nabla \cdot\left(\sum_{j=1}^{K-1} M_{i j}(\boldsymbol{\phi}) \nabla \mu_{j}\right). \tag{31}
$$

$$
M_{i j}(\boldsymbol{\phi})=\sum_{\alpha=1}^{N} M_{i j}^{\alpha} g_{\alpha}(\boldsymbol{\phi}), \tag{32}
$$


where each $M_{ij}^{\alpha}$ represents the mobility matrix, of the phase $\alpha$, calculated by multiplying the diffusivity matrix with susceptibility matrix as,

$$
M_{ij}^{\alpha}=D_{ik}^{\alpha} \frac{\partial c_{k}^{\alpha}(\boldsymbol{\mu}, T)}{\partial \mu_{j}}. \tag{33}
$$

In the above expression (written in Einstein notation for a shorter description), a repeated index implies sum over all the elements. Every $M_{ij}^{\alpha}$ value is weighed with respect to the phase fractions represented by $g_{\alpha}(\phi)$ which gives the total mobility $M_{ij}(\phi)$. The function $g_{\alpha}(\phi)$ is in general not same as $h_{\alpha}(\phi)$ which interpolates the grand potentials, however, in the present description, we utilize the same. $D_{ij}^{\alpha}$ represent the inter-diffusivities in phase $\alpha$ and so on. Both the evolution equations require the information about the chemical potential $\boldsymbol{\mu}$. Two possibilities exist to determine the unknown chemical potential $\boldsymbol{\mu}$.

- The chemical potential $\boldsymbol{\mu}$ can be derived from the constraint relation in equation 27.
  The $K-1$ independent components $\mu_{i}$ are determined by simultaneously solving the $K-1$ constraints for each of the $K-1$ independent concentration variables $c_{i}$, from the given values of $c_{i}$ and $\phi_{\alpha}$ at a given grid point. A Newton iteration scheme can be used for solving the system of equations,

$$
\begin{aligned}
\left\{\mu_{i}^{n+1}\right\} & = \\
& \left\{\mu_{i}^{n}\right\}-\left[\sum_{\alpha=1}^{N} h_{\alpha}(\phi) \frac{\partial c_{i}^{\alpha}\left(\boldsymbol{\mu}^{n}, T\right)}{\partial \mu_{j}}\right]_{i j}^{-1}\left\{c_{i}-\sum_{\alpha=1}^{N} c_{i}^{\alpha}\left(\boldsymbol{\mu}^{n}, T\right) h_{\alpha}(\phi)\right\},
\end{aligned} \tag{34}
$$

  where $\{\}$ represents a vector while $[]$ denotes a matrix.

- Alternatively, explicit evolution equations for all the $K-1$ independent chemical potentials, can be formulated by inserting the constraint equation 27 into the evolution equation for each of the concentration fields. For a general, multi-phase, multi-component system, the evolution equations for the components of the chemical potential $\boldsymbol{\mu}$ can be written in matrix form by,

$$
\begin{aligned}
& \left\{\frac{\partial \mu_{i}}{\partial t}\right\}= \\
& {\left[\sum_{\alpha=1}^{N} h_{\alpha}(\phi) \frac{\partial c_{i}^{\alpha}(\boldsymbol{\mu}, T)}{\partial \mu_{j}}\right]_{i j}^{-1}\left\{\nabla \cdot \sum_{j=1}^{K-1} M_{i j}(\phi) \nabla \mu_{j}-\sum_{\alpha=1}^{N} c_{i}^{\alpha}(\boldsymbol{\mu}, T) \frac{\partial h_{\alpha}(\phi)}{\partial t}\right\}.}
\end{aligned} \tag{35}
$$


In the present work, an explicit formulation, as shown in equation 35 have been used for calculating $K-1$ independent chemical potentials.

## 4. Thermodynamic description

In order to describe the thermodynamics of the respective phases, we approximate the variation of the grand-potential of the respective phases using a polynomial of second degree in the chemical potential. Without going into the details, we would like to state that such an approximation is the minimum requirement for fitting the Gibbs-Thomson coefficients of the respective interfaces. In our present investigation we are especially interested in the coupled growth of ferrite($\alpha$) and cementite($\beta$) in austenite($\gamma$). Hence, the Gibbs-Thomson coefficients of the $\alpha-\gamma$ and $\beta-\gamma$ interfaces are important parameters required for the correct description of the system. Also, since we are treating a binary system, we have only a single independent chemical potential $\mu$, and we define our functions with only this chemical potential as the argument. We start by writing the grand-potential of a given phase as,

$$
\Psi^{\alpha}(T, \mu)=A^{\alpha}(T) \mu^{2}+B^{\alpha}(T) \mu+C^{\alpha}(T). \tag{36}
$$

At the eutectoid temperature $T_{E}$, where the three phases($\alpha, \beta, \gamma$) are at equilibrium, we fix the coefficients in the following manner,

$$
A^{\alpha}\left(T_{E}\right)=\frac{1}{2}\left(\frac{\partial^{2} \Psi^{\alpha}}{\partial \mu^{2}}\right)_{T_{E}, \mu_{e q}} \equiv \frac{-V_{m}}{\frac{\partial^{2} G^{\alpha}}{\partial c^{2}}} \tag{37}
$$

$$
B^{\alpha}\left(T_{E}\right)=-c-2 A^{\alpha} \frac{\mu_{e q}}{V_{m}} \tag{38}
$$

$$
C^{\alpha}\left(T_{E}\right)=\frac{G^{\alpha}}{V_{m}}+A^{\alpha}\left(T_{E}\right)\left(\frac{\mu_{e q}}{V_{m}}\right)^{2} \tag{39}
$$

where $V_{m}$ is the molar volume, $G^{\alpha}$ is the free energy of the phase at the eutectoid composition and the respective equilibrium temperature. The first derivative $\frac{\partial G^{\alpha}}{\partial c}$, which is the chemical potential $\mu_{e q}$ and the second derivative of the free energy $\frac{\partial^{2} G^{\alpha}}{\partial c^{2}}$, are also extracted from the thermodynamic functions of the respective phases derived from the CALPHAD database [16]. We point out that while the above procedure fixes the coefficients, A, B, C for austenite and ferrite, the calculation of corresponding values for the cementite

phase, are not as generic. Theoretically, the free energy as a function of composition of the cementite phase is represented by a point (only). However, for phase-field calculations, we require information about the changes in free energy, at least for small differences in composition. The database we used for this calculation yields two free energy values corresponding to compositions on either side of the eutectoid composition (of cementite). We utilize this information together with the chemical potential of the cementite phase in equilibrium with the austenite (at the eutectoid composition) to derive the free energy as a function of composition for the cementite phase (a parabola with a narrow opening). The grand-potential description is obtained by performing the Legendre transform of the free energy density which gives the grand-potential density (a wide-inverted parabola). It is worth mentioning that a limiting case (not applied here) could also be adopted for stoichiometric compounds (in general) by assuming the coefficient $A$ of cementite to be zero.

This is equivalent to assuming $\dfrac{\partial^2 f}{\partial c^2}$ as infinity. The coefficients $B$ and $C$ can thereafter be fixed using the information about the equilibrium chemical potential and the grandpotential both of which are thermodynamically defined for the stoichiometric compound as well.

To fit the information of the slopes of the equilibrium lines of the phase diagram, it is essential to describe the variation of the grand-potential as a function of temperature. We achieve this through a linear interpolation of the coefficients of the grand-potential density functions. The properties at a chosen lower temperature of ferrite and austenite are fixed by utilizing the same procedure as in equation 39, however using the values of the free energy $G^\alpha$, the chemical potential and the second derivative of the free energy with respect to concentration are derived from the thermodynamic functions in CALPHAD at the chosen temperature, and are computed at the respective phase concentrations at the eutectoid temperature. Due to unavailability of the chemical potential for cementite from the CALPHAD databases, the case of the cementite is treated differently. We derive this information, using the equilibrium between the cementite and austenite and approximating the chemical potential and grand-potential from the value given for the austenite at the chosen temperature, as both these quantities must be equal for the two phases at equilibrium. The procedure suffices because the austenite-cementite equilibrium is relevant during coupled growth of the ferrite and the cementite phases from the austenite.

It is noteworthy that in the present work, we do not model the difference in diffusive mechanisms of the cementite phase. While it may not be completely appropriate for the case of eutectoid reaction in steels, yet it does not hamper the spirit of the present work which is the comparison between phase-field simulations and a modified Jackson-Hunt theory. Therefore, in the present discussion, the set of parameters chosen for the diffusion

![](./images/867753739077813155_1.jpg)

Figure 1: Calculated phase diagram

of carbon in cementite are exemplary only for a possible eutectoid transformation.

## 5. Relation to sharp-interface limit

In this section we derive the relation between the simulation parameters and the corre-
sponding quantities in the sharp interface limit. Two of these quantities are the Gibbs-
Thomson coefficient and the slopes of the equilibrium co-existing lines. These relations
can be derived from the Clausius-Clapeyron equation for the case of binary alloys which
writes as,

$$
\frac{\partial \mu}{\partial T}=\frac{\left(\frac{\partial \Psi^{\alpha}}{\partial T}-\frac{\partial \Psi^{\gamma}}{\partial T}\right)}{\left(c^{\alpha}-c^{\gamma}\right)}. \tag{40}
$$

Expanding $\frac{\partial \mu}{\partial T}=\frac{\partial \mu^{\alpha, \gamma}}{\partial c} \frac{\partial c^{\alpha, \gamma}}{\partial T}$ we derive the slope of the equilibrium co-existence lines
as,

$$
m^{\alpha, \gamma}=\frac{\partial c^{\alpha, \gamma}}{\partial \mu} \frac{\left(c^{\alpha}-c^{\gamma}\right)}{\left(\frac{\partial \Psi^{\alpha}}{\partial T}-\frac{\partial \Psi^{\gamma}}{\partial T}\right)}=\frac{-1}{2 A^{\alpha, \gamma}} \frac{\left(c^{\alpha}-c^{\gamma}\right)}{\left(\frac{\partial \Psi^{\alpha}}{\partial T}-\frac{\partial \Psi^{\gamma}}{\partial T}\right)}. \tag{41}
$$

13

Similarly the Gibbs-Thomson coefficient $\Gamma_{\alpha \gamma}$ derives as;

$$
\Gamma_{\alpha \gamma}=\frac{\tilde{\sigma}_{\alpha \gamma}}{\left(\frac{\partial \Psi^{\alpha}}{\partial T}-\frac{\partial \Psi^{\gamma}}{\partial T}\right)}, \tag{42}
$$

where $\tilde{\sigma}_{\alpha \gamma}$ is the surface tension of the $\alpha-\gamma$ interface. Similar expressions for the Gibbs-
Thomson coefficients of the cementite phase can be derived by replacing $\alpha$ with $\beta$ in the
preceding equations. Theoretically, the deviations of chemical potential or the concentra-
tions due to curvature, would be non-existent for the cementite phase, by the virtue of the
infinite values of $\frac{\partial^{2} f}{\partial c^{2}}$. However, the approximate construction of the grand-potential den-
sities allow small deviations in composition due to curvature effects, although of a much
lower order as compared to the austenite and ferrite phases.

In our simulations, we set the conditions such that there is no interface kinetics in direct
correlation to the conditions imposed in the theoretical analysis. We derive the same, by
setting the interface relaxation coefficient $\tau_{(\alpha, \beta) \gamma}$ through a thin-interface analysis [17, 12]
as,

$$
\tau_{(\alpha, \beta) \gamma}=\frac{\left(c^{(\alpha, \beta)}-c^{\gamma}\right)^{2}}{D^{\gamma} \frac{\partial c^{\gamma}}{\partial \mu}}(M+F) \tag{43}
$$

where $c^{(\alpha, \beta)}$ are the equilibrium concentrations of the phases at equilibrium at the eutectoid
temperature and $M, F$ are solvability integrals derived from the thin-interface analysis.
The total sum of $M+F \approx 0.222$ which is used in the simulations. As can be seen from
the nature of the phase diagram in Figure 1, the difference between these concentrations
change a little with changing temperature. Hence, the assumption of using the values at the
eutectoid temperature holds. We state that the equation for the relaxation constant $\tau_{(\alpha, \beta) \gamma}$
used is strictly valid in cases pertaining to vanishing diffusivity in one of the phases, or for
instances of equal diffusivities in both phases. In the former case, the relation must be used
with the anti-trapping current which removes the chemical potential jump at the interface,
arising out of artificial solute trapping as a consequence of choosing a thick interface.

The case when the diffusivities in both the phases is arbitrary, the problem is not as trivial.
It is to be noted that the whole class of problems which falls in the category of two-phase
transport through a complex structure inherently exhibit thin-interface effects for station-
ary/moving interfaces. Despite some recent progress, so far no method has been found to
completely eliminate thin-interface effects in the case of arbitrary diffusion coefficients in

the two phases with a non-stationary interface [18, 19, 20, 21] in a closed form manner. One of the principal reasons for non-closure of the problem, is that the artificial discontinuous jump effects (arising out of arbitrary diffusivities) are independent of the velocity of the interface. This implies that such effects cannot be removed through the imposition of an anti-trapping current that has been previously used for removing the artificial solute trapping effects in one-sided diffusion problems. While few hints to the solution by the introduction of tensorial mobilities [19] and through the usage of artificial parameter $\chi$ (related to diffusive current in solid) [22] are present, a closed form solution is still in the process of being worked out. This in all certainty is not the highlight or aim of the present work.

The reason which allows us to take the liberty of overlooking these defects and derive meaningful results, is that the interface width used in the present problem is of a very small magnitude. It is worth noting that the interface width is proportional to the capillary length of the phases and in the present formulation, scales inversely with the factor $\frac{\partial^2 f}{\partial c^2}$.
Apparently, while the capillary length of the phases, austenite and ferrite are close to each other, the case of cementite is very restrictive to the choice of the interface width. By deriving leverage out of the fact that the thin-interface defects scale with the interface width, a small choice of the interface width in present simulations allows us to limit the magnitude of the thin-interface defects, and facilitates reasonably quantitative results.

In order to derive the relaxation constant, we utilize the mobility of the austenite and assume that even though the gradients of the chemical potential exist in the solid, the principal driving force is still due to the gradient of the chemical potential in the austenite. In the absence of a closed form solution, this seems like a reasonable choice. We substantiate our claim in the following sections, that the errors due to this assumption, do not seem to affect the quantitative aspects of our results.

## 6. Comparison between theory and simulation

In this section, we compare the growth velocity of pearlite obtained from phase-field simulation with the analytical results in the two regimes: diffusion in austenite (only) and diffusion in austenite as well as ferrite. The simulation set-up comprises of a bounding box with periodic boundary conditions in the transverse direction, while no flux boundary conditions are used in the growth direction. The bounding box width in the transverse direction directly controls the lamellar spacing $\lambda$ such that the pearlitic composition is retained (88% ferrite and 12% cementite). The chemical potential in the bounding box is initialized with the equilibrium chemical potential for eutectoid transformation. The box

width in the growth direction is chosen 10 times larger than the lamellar width such that the chemical potential gradient in bulk remains uniform at successive simulation time-steps. In order to completely rule out the possibility of non-uniformity of chemical potential in bulk phase, the simulation is carried in a moving frame (also known as shifting-box simulation). In the present simulations, the domain is shifted in the growth direction (upwards) by adding a row of grid-point at the top of domain and discarding off a row of grid-points at the bottom, every time the advancing lamellar front fills up 10% of the simulation box. Further, we have also ensured that the 10% of the box, comprising of the growing phases, have sufficient number of cells to describe the diffusional field. Although, we cannot claim to be error proof, a good match with analytical results, confirms, that the deviations are not large enough to influence the results obtained. To find the co-operative lamellar growth rate, the previously discarded grid-points are aggregated back and the position of advancing interface is determined by finding the position of the contour line $\phi_{\alpha} - \phi_{\beta} = 0$ through a linear interpolation of the neighboring values (where the sign of $\phi_{\alpha} - \phi_{\beta}$ changes). In the present context, $\alpha$ and $\beta$ denote any two phases, between which the interface is to be isolated.

The rate of change of the position of the interface in transverse direction is plotted as a function of time, and the simulation is run until there is no more change in the velocity of the interface, which indicates the steady-state has been attained. The procedure described above is repeated to calculate the steady state velocities for different lamellar widths '$\lambda$' and plotted for comparison with analytical results as shown in Figure 3.

The parameters used for analytical calculation of the lamellar growth velocity as well as for sharp-interface theory as summarized in Table 1. The phase profile obtained from the phase-field simulation for the two cases: diffusion in austenite (only) and diffusion in austenite as well as ferrite are shown in Figure 2(a) and Figure 2(b) respectively. The corresponding plots for chemical potential are shown in Figure 2(c) and Figure 2(d). It is to be noted that the phase-field simulation pictures shown in fig. 2 are merely snapshots of the region of interest and do not represent the entire simulation box. The growth velocities of pearlite evolving in austenite at an undercooling of 10K in both the regimes are plotted in Figure 3. We observe a reasonable overlap of analytically predicted growth velocity with phase-field results in absence of diffusion in ferrite. However, a small deviation is observed near the critical lamellar spacing when diffusion in ferrite is also accounted for along with diffusion in austenite, while we observe tapering of cementite near the growth front due to diffusion in ferrite. It is noteworthy, that such a taper causes a modification of the triple point orientation with respect to the growth direction, and thereby the triple point angles assumed in the analytical derivations differs from those resulting in the simulations. This indeed causes modifications in the velocities near to the critical spacing and

Table 1: Parameters used for analytical calculation and for sharp-interface theory

<table>
<thead>
<tr>
<th>Symbol</th>
<th>Value</th>
<th>Units</th>
</tr>
</thead>
<tbody>
<tr>
<td>$T_E$</td>
<td>989</td>
<td>K</td>
</tr>
<tr>
<td>$\Delta T$</td>
<td>10</td>
<td>K</td>
</tr>
<tr>
<td>$\sigma_{\alpha\gamma} = \sigma_{\beta\gamma} = \sigma_{\alpha\beta}$</td>
<td>0.49</td>
<td>J/$m^2$</td>
</tr>
<tr>
<td>$D^\alpha = D^\beta$</td>
<td>$2 \times 10^{-9}$</td>
<td>$m^2$/s</td>
</tr>
<tr>
<td>$D^\gamma$</td>
<td>$1 \times 10^{-9}$</td>
<td>$m^2$/s</td>
</tr>
<tr>
<td>$A^{\alpha,\gamma} = A^{\beta,\gamma}$</td>
<td>$-1.015385 \times 10^{-11}$</td>
<td>$m^3$/J</td>
</tr>
<tr>
<td>$A^{\alpha,\beta}$</td>
<td>$-1.184616 \times 10^{-12}$</td>
<td>$m^3$/J</td>
</tr>
<tr>
<td>$A^{\beta,\alpha}$</td>
<td>$-1.9 \times 10^{-14}$</td>
<td>$m^3$/J</td>
</tr>
<tr>
<td>$c_A^\alpha$</td>
<td>$8.85 \times 10^{-4}$</td>
<td>-</td>
</tr>
<tr>
<td>$c_A^\beta$</td>
<td>0.25</td>
<td>-</td>
</tr>
<tr>
<td>$c_A^\gamma$</td>
<td>0.034433</td>
<td>-</td>
</tr>
<tr>
<td>$c_B^\alpha$</td>
<td>0.999115</td>
<td>-</td>
</tr>
<tr>
<td>$c_B^\beta$</td>
<td>0.75</td>
<td>-</td>
</tr>
<tr>
<td>$c_B^\gamma$</td>
<td>0.965567</td>
<td>-</td>
</tr>
<tr>
<td>$\eta_\alpha$</td>
<td>0.88</td>
<td>-</td>
</tr>
<tr>
<td>$\eta_\beta$</td>
<td>0.12</td>
<td>-</td>
</tr>
<tr>
<td>$\theta_{\alpha\beta} = \theta_{\beta\alpha}$</td>
<td>$30^\circ$</td>
<td>degrees</td>
</tr>
<tr>
<td>$\tau_{\alpha\gamma}$ (calculated)</td>
<td>$1.724027 \times 10^8$</td>
<td>Js/$m^4$</td>
</tr>
<tr>
<td>$\tau_{\beta\gamma}$ (calculated)</td>
<td>$7.118288 \times 10^9$</td>
<td>Js/$m^4$</td>
</tr>
</tbody>
</table>


the critical spacing itself, which is also reflected in our simulations. However, for spacings further ahead, where the capillary term is less dominant with respect to the solutal effect, the agreement is better. Further, as already shown in previous works [23], there exists a difference between theoretical analysis of the Jackson-Hunt type and quantitative phase-field simulations, which arises because of the inherent assumptions used in the analytical derivations.

![](./images/867753739077813155_2.jpg)

Figure 2: Phase patterns (austenite in red, ferrite in blue and cementite in yellow) and chemical potentials plotted for corresponding cases: (a) and (c) Diffusion in austenite (only) and (b) and (d) Diffusion in austenite as well as ferrite. It is to be noted that the pictures above are merely snapshots depicting the region of interest and not the entire simulation box itself. The pearlite lamella width is $200\ \mu\text{m}$ which is half of the illustrated box-length.

![](./images/867753739077813155_3.jpg)

Figure 3: Comparison of pearlitic growth front velocities as a function of lamellar spacing at constant undercooling ($\Delta T = 10K$) derived from a Jackson-Hunt-type calculation with phase-field results in respective diffusion regimes.

### 7. Concluding remarks

In the present work, we generalize the Jackson-Hunt analysis in order to incorporate diffusion in the growing phases, in addition to the diffusion in the bulk. The results of the analysis predict that the growth front velocities change by a factor $\rho$, with respect to the case where diffusivity is absent in the growing phases. Phase-field simulations, conducted with a thermodynamically consistent model, confirm the theoretical predictions fairly well. In addition, the simulations predict the morphology of the growth front showing a tapering of cementite in the direction of growth.

It is worth clarifying that the present work does not aim to represent the eutectoid transformation in Fe-C systems, *in totality*. Our studies are limited to *only* a part of the entire eutectoid transformation phenomena, which is to analytically and numerically investigate the influence of diffusion in the growing phases, on the lamellar front velocity, which has been adequately achieved through our results. The presence of a stoichiometric phase like cementite imposes a limitation on the choice of length scale and therefore the interface width, thereby limiting the thin-interface defects arising due to having arbitrary diffusivities in all phases. This argument is further accentuated by a good agreement of analytical and numerical results as plotted in fig. 3. Further, this near-overlap also suggest that the aim of the present work has been adequately accomplished. Thus, the present phase-field simulations decomposes the effect of dual-diffusion mode (in bulk as well as growing phases), in isolation i.e. without considering additional effects for e.g. the lattice strains [24] which influence the growth morphology.

The complete problem of eutectoid transformation however, is complicated and a precise description is not the aim of the present work. The additional ingredients, include the contribution from grain-boundary which is an interesting direction for future research. Therefore, for comparison with experiments and particularly, to present a detailed argumentation with respect to the previous findings [8, 25] based on the results of this article would not be meaningful. To arrive at a reasonable overlap between simulations and experiments, it is necessary to consider the combined influence of bulk and grain-boundary diffusion together with transformation strains in the present phase-field model. We hope to report on an all-inclusive approach for modeling lamellar growth of pearlite, in the near future.

It will also be intriguing to address the faster kinetics of re-austenisation or pearlite dissolution (as compared to pearlite growth) by deriving and transferring ideas from the present work. To this end, studies need to be conducted to establish the exact mechanism and primary diffusion regime that governs the kinetics of such transformations. Low undercooling and presence of pre-existing cementite particles in austenite, alter the pearlite growth

morphology from lamellar to spherodized widely known as "divorced pearlite" [26]. The phenomena need to be investigated as simulations contribute in gaining further insight on spherodizing behavior or non co-operative growth of pearlite during widely used annealing treatment of steel.

### Acknowledgements

KA, CQ, SS and BN acknowledge the financial support from the German Research Foun- dation (DFG) in the framework of Graduate School - 1483. KA also thanks Center for Computing and Communication at RWTH Aachen University (HPC Cluster) for compu- tational resources.

### References

[1] Zackay V, Aaronson H. Decomposition of Austenite by Diffusional Processes. In- terscience Publishers, New York; 1962.

[2] Kral M, Mangan M, Spanos G, Rosenberg R. Mater Charact 2000;45(1):17 – 23.

[3] De Graef M, Kral M, Hillert M. JOM 2006;58:25–8.

[4] Zener C. Kinetics of the Decomposition of Austenite. Wiley, NY; 1947.

[5] Hillert M. Jernkont Ann 1957;147:757–89.

[6] Tiller W. Polyphase solidification. In: Liquid Metals and Solidification (ASM pro- ceedings). 1958, p. 276.

[7] Jackson K, Hunt J. T Metall Soc AIME 1966;226:1129.

[8] Nakajima K, Apel M, Steinbach I. Acta Mater 2006;54(14):3665–72.

[9] Steinbach I, Plapp M. Continuum Mech Therm 2011;:1–9.

[10] Pandit A. Theory of the pearlite transformation in steels. Ph.D. thesis; University of Cambridge, Cambridge; 2011.

[11] Choudhury A, Plapp M, Nestler B. Phys Rev E 2011;83:051608.

[12] Choudhury A, Nestler B. Phys Rev E 2012;85:021602.

[13] Nestler B, Garcke H, Stinner B. Phys Rev E 2005;71:041609.

[14] Steinbach I, Pezzolla F. Physica D 1999;134(4):385 -93.

[15] Stinner B, Nestler B, Garcke H. SIAM J Appl Math 2004;64(3):775-99.

[16] Gustafson P. Scand J Metall 1985;14(5):259-67.

[17] Karma A, Rappel WJ. Phys Rev E 1996;53:R3017.

[18] Almgren R. SIAM J Appl Math 1999;59(6):2086-107.

[19] Nicoli M, Plapp M, Henry H. Phys Rev E 2011;84:046707.

[20] Plapp M. Philos Mag 2011;91(1):25-44.

[21] Steinbach I. Modell Simul Mater Sci Eng 2009;17(7):073001.

[22] Ohno M, Matsuura K. Phys Rev E 2009;79:031603.

[23] Folch R, Plapp M. Phys Rev E 2005;72:011602.

[24] Steinbach I, Apel M. Acta Mater 2007;55(14):4817 -22.

[25] Nakajima K, Tanaka Y, Hosoya Y, Apel M, Steinbach I. Materi Sci Forum 2007;558-559(2):1013-20.

[26] Verhoeven J, Gibson E. Metall Mater Trans A 1998;29:1181-9.