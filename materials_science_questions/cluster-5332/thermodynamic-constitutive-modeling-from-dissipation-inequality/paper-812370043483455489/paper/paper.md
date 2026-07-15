![](./images/812370043483455489_1.jpg)

International Journal of Plasticity 20 (2004) 1313–1345

![](./images/812370043483455489_2.jpg)
www.elsevier.com/locate/ijplas

# The Payne effect in finite viscoelasticity: constitutive modelling based on fractional derivatives and intrinsic time scales

A. Lion*, C. Kardelky

Department of Mechanical Engineering, University of Kassel, D-34109 Kassel,
Mönchebergstrasse 7, Germany

Received in final revised form 11 July 2003

Dedicated to Prof. Dr.-Ing. P. Haupt on the occasion of his 65th birthday.

## Abstract

As we know from experimental testing, the stiffness behaviour of carbon black-filled elastomers under dynamic deformations is weakly dependent on the frequency of deformation but strongly dependent on the amplitude. Increasing strain amplitudes lead to a decrease in the dynamic stiffness, which is known as the Payne effect. In this essay, we develop a constitutive approach of finite viscoelasticity to represent the Payne effect in the context of continuum mechanics. The starting point for the constitutive model resulting from this development is the theory of finite linear viscoelasticity for incompressible materials, where the free energy is assumed to be a linear functional of the relative Piola strain tensor. Motivated by the weak frequency dependence of the dynamic stiffness of reinforced rubber, the memory kernel of the free energy functional is of the Mittag Leffler type. We demonstrate that the model is compatible with the Second Law of Thermodynamics and equal to a fractional differential equation between the overstress of the Second Piola Kirchhoff type and the Piola strain tensor. In order to represent the dependence of the dynamic stiffness on the amplitude of strain, we replace the physical time by an intrinsic time variable. The temporal evolution of the intrinsic time is driven by an internal variable, which is a measure for the current state of the material's microstructure. The material constants of the model are estimated using a stochastic identification algorithm of the Monte Carlo type. We demonstrate that the constitutive approach

* Corresponding author. Fax: +49-561-804-2720.
E-mail address: lion@ifm.maschinenbau.uni-kassel.de (A. Lion).

0749-6419/$ - see front matter © 2003 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijplas.2003.07.001

pursued here represents the combined frequency and amplitude dependence of filler-reinforced rubber. In comparison with the micromechanical Kraus model developed for sinusoidal strains, the theory set out in this essay allows the representation of the stress response under arbitrary loading histories.

© 2003 Elsevier Ltd. All rights reserved.

**Keywords:** Elastomers; Finite Viscoelasticity; Fractional Derivatives; Payne effect

---

### 1. Introduction

From numerous engineering applications we know that there are many fields where constitutive models are needed to represent the dynamic properties of polymers, especially of carbon black-filled rubber under infinitesimal and finite thermomechanical deformations. The first example to be discussed is an elastomeric engine mount for a passenger car. Under typical operating conditions its loading history can be decomposed into the sum of two terms. The first term is the temporally constant preload which is determined by the weight of the engine. It acts in a vertical direction and is called static load. Since rubber mounts have strongly nonlinear force displacement characteristics, the local stiffness of the mount depends on the magnitude of the static load. The second term is the so-called dynamic load. It is caused by the rotation of the engine's crankshaft, the motions of the pistons and the more or less stochastic excitations when the vehicle is riding over uneven road surfaces. Numerical values of the eigenfrequencies of vertical oscillations of passenger car's engines lie between 10 and 15 Hz, whereas the excitations caused by the roughness of the roads are characterised by frequency spectra up to 40 Hz. In order to simulate the corresponding comfort effects of vehicles based on the finite element or the multibody dynamics approach, we need constitutive models for elastomers representing the nonlinear static behaviour in combination with frequency and amplitude dependence. The second example to be discussed concerns the rolling resistance of automotive tyres. When a vehicle is riding over a flat track with a constant velocity, each particle of the sidewalls of its tyres is periodically deformed. In addition to this, a constant preload caused by the tyre pressure is superimposed. Since the perimeter of a tyre is about 2 m and typical riding velocities are between 1 and 70 m/s, the frequency range of interest is between 0.5 and 35 Hz. This periodic deformation leads to local hysteresis behaviour and heat generation which contributes to the rolling resistance of the tyre. The second contribution factor in terms of the rolling resistance is determined by local sliding motions between the particles of the tread and the road surface. In order to simulate such behaviour, we need constitutive models representing both the nonlinear static and the dynamic material properties of filled rubber under different amplitudes and frequencies of deformation.

As we know, the material behaviour of filler-reinforced elastomers is mainly hyperelastic (cf. Drozdov and Dorfmann, 2003, and citations therein) but a lot of more or less significant, inelastic phenomena can be observed. If a virgin specimen made of carbon black-reinforced rubber is cyclically deformed with large amplitudes, we observe the Mullins effect. It is a softening phenomenon which is caused

by the strain-induced breakage of weak physical bonds. Experimental data and constitutive models representing this phenomenon are provided (for example, by Lion, 1996, 2000; Besdo and Ihlemann, 1996, 2003a,b; Miehe and Keck, 2000; or Laiarinandrasana et al., 2003). As we are also aware, the material behaviour of filled rubber and synthetic elastomers under finite deformations is highly dependent on the rate of deformation and the temperature (cf. Lion, 1997; Khan and Zhang, 2001; Khan and Lopez-Pamies, 2002). Experimental data and constitutive theories to describe such behaviour have been proposed (for example, by Khan and Zhang, 2001; Lion, 1997; Reese, 2003).

In order to investigate the dynamic material behaviour of rubber under uniaxial tension and compression, a specimen is loaded with a sinusoidal displacement-controlled process $u(t)$ of the following form (cf. Fig. 1):

$$
u(t)=u_{0}+\Delta u \sin (2 \pi f t) \tag{1}
$$

$f$ is the frequency of excitation, $\Delta u$ the amplitude and $u_{0}$ an arbitrary but time-independent pre-deformation. To calculate stresses and strains we choose the geometry of the pre-deformed specimen as a reference. Thus the longitudinal pre-strain $\varepsilon_{0}$ of the specimen with undeformed length $l_{R}$ is $\varepsilon_{0}=u_{0} / l_{0}$, where $l_{0}=$ $l_{\mathrm{R}}+u_{0}$ is the length of the pre-deformed specimen. The dynamic strain amplitude $\Delta \varepsilon$ referred to $l_{0}$ is $\Delta \varepsilon=\Delta u / l_{0}$. After division of Eq. (1) by the factor $l_{0}$, we obtain

$$
\frac{u(t)}{l_{0}}=\varepsilon(t)=\varepsilon_{0}+\Delta \varepsilon \sin (2 \pi f t). \tag{2}
$$

If the strain amplitude $\Delta \varepsilon$ is sufficiently small, the force response $F(t)$ of fillerreinforced elastomers is in a good approximation also a harmonic function (cf. Roland, 1990) and can be written as

$$
F(t)=F_{0}+\Delta F \sin (2 \pi f t+\varphi). \tag{3}
$$

$F_{0}$ is the so-called static force depending only on the pre-deformation; the force amplitude $\Delta F$ and the phase angle $\varphi$ depend, in general, on the pre-deformation, the frequency and the strain amplitude. Assuming incompressibility, i.e.

![](./images/812370043483455489_3.jpg)

Fig. 1. Static and dynamic deformations of a test specimen.

$Al = A_0l_0 = A_{\mathrm{R}}l_{\mathrm{R}}$, relating the force to the cross-sectional area $A_0$ of the pre-deformed specimen and application of the theorems of addition leads to

$$
\frac{F(t)}{A_{0}}=\sigma(t)=\sigma_{0}+\Delta \sigma(\cos (\varphi) \sin (2 \pi f t)+\sin (\varphi) \cos (2 \pi f t)).\tag{4}
$$

The stress amplitude and the static stress are defined as $\Delta \sigma=\Delta F / A_{0}$ and $\sigma_{0}=F_{0} / A_{0}$.

If we define the storage and dissipation moduli $G'$ and $G''$ as

$$
G^{\prime}\left(\varepsilon_{0}, f, \Delta \varepsilon\right)=\frac{\Delta \sigma}{\Delta \varepsilon} \cos (\varphi)\tag{5}
$$

and

$$
G^{\prime \prime}\left(\varepsilon_{0}, f, \Delta \varepsilon\right)=\frac{\Delta \sigma}{\Delta \varepsilon} \sin (\varphi)\tag{6}
$$

the dynamic stress response can be rewritten as

$$
\sigma(t)=\sigma_{0}+\Delta \varepsilon\left(G^{\prime}\left(\varepsilon_{0}, f, \Delta \varepsilon\right) \sin (2 \pi f t)+G^{\prime \prime}\left(\varepsilon_{0}, f, \Delta \varepsilon\right) \cos (2 \pi f t)\right).\tag{7}
$$

In general, carbon black-reinforced rubber has a fairly weak frequency dependence in conjunction with a pronounced amplitude dependence. If the strain amplitude $\Delta \varepsilon$ increases, the storage modulus $G'$ lessens and the dissipation modulus $G''$ shows a more or less pronounced sigmoidal behaviour, which is the well-known Payne effect (cf. Payne, 1960). Comprehensive experimental and theoretical work in this field has been provided (for example, by Lion et al., 2003; Metzeler and Nonnenmacher, 2003; Chazeau et al., 2000; Lion, 1999; Huber, 1997; Wang et al., 1997; Ulmer, 1996; Huber, et al. 1996).

Since filled elastomers are nonlinear viscoelastic materials, their dynamic properties are also temperature-dependent. In this essay, the temperature dependence is neither investigated nor considered in the constitutive model. We refer the interested reader (for example, to Lion, 1998).

A first model to represent and understand the Payne effect on a physical level is the so-called Kraus model. It has been discussed in detail (for example, by Huber, 1997; Ulmer, 1996; Lion, 2000). The fundamental idea is that during sinusoidal deformations there is always breakage and recovery of weak physical bonds. The rate of breakage is assumed to be an increasing function of the strain amplitude and the rate of recovery a decreasing function. Under stationary conditions, which are characterised by constant strain and stress amplitudes, there is a dynamic equilibrium between the number of breakage and recovery processes per unit of time. The storage modulus is assumed to be proportional to the total number of intact bonds and the dissipation modulus to the rate of breakage per unit of time. The result of the theory reads as follows:

$$
G^{\prime}(\Delta \varepsilon)=G_{\infty}^{\prime}+\frac{G_{0}^{\prime}-G_{\infty}^{\prime}}{1+\left(\Delta \varepsilon / \Delta \varepsilon_{\mathrm{c}}\right)^{2 m}}
\tag{8}
$$

$$
G^{\prime \prime}(\Delta \varepsilon)=G_{\infty}^{\prime \prime}+\frac{2\left(G_{\mathrm{m}}^{\prime \prime}-G_{\infty}^{\prime \prime}\right)\left(\Delta \varepsilon / \Delta \varepsilon_{\mathrm{c}}\right)^{m}}{1+\left(\Delta \varepsilon / \Delta \varepsilon_{\mathrm{c}}\right)^{2 m}}
\tag{9}
$$

$\Delta \varepsilon_{\mathrm{c}}$ is the characteristic value of the strain amplitude, where the dissipation modulus reaches its maximum $G_{\mathrm{m}}^{\prime \prime}$. The asymptotic values of the storage and dissipation moduli for large strain amplitudes are $G_{\infty}^{\prime}$ and $G_{\infty}^{\prime \prime}$; the constant $G_{0}^{\prime}$ is the value of the storage modulus for small strain amplitudes and m is a non-negative phenomenological exponent to fit the experimental data. As shown experimentally by Vieweg et al. (1995) and Heinrich and Vilgis (1995), the exponent m is independent of the frequency, the temperature and the carbon black content. Its value is about 0.5. Based on this observation, m is presumed to be determined by the filler material itself. To this end, Huber et al. (1996) developed a physical theory where the numerical value of m is determined by the fractal dimension of the carbon black clusters (cf. Huber et al., 1996).

Some minor modifications to Eqs. (8) and (9) to represent experimental data with more accuracy have been proposed by Ulmer (1996). Nevertheless, models of this type are only able to represent the material in the frequency domain under harmonic strains: it is impossible to model the material in the time domain for arbitrary loading processes. A very first attempt to model the Payne effect in the frequency domain using a constitutive approach formulated in the time domain was developed by Lion (1999). In this approach the material is represented by a series of physical nonlinear Maxwell elements in parallel. The nonlinearity is introduced by viscosity functions depending on a structural variable which is a measure for the current state of the material's microstructure. Since the microstructure, or equivalently the number of intact physical bonds, changes under periodic strains with different amplitudes, the structural variable is a measure for the strain amplitude. The evolution equation for this variable is formulated in such a way that it becomes nearly constant under stationary processes with constant amplitudes. In order to obtain expressions in closed form for the storage and dissipation moduli, the nonlinear differential equations for the Maxwell elements are linearised and solved for sinusoidal strain processes. As the main result of this approach, the dynamic moduli depend on both variables the strain amplitude and the frequency. Under simplifying assumptions, the theory proposed by Lion (1999) reduces to the Kraus model specified by Eqs. (8) and (9). Since the number of Maxwell elements needed to represent the weak frequency dependence of rubber is fairly large, the mathematical form of the evolution equation for the structural variable is complicated and the theory is only one-dimensional, we have chosen to formulate a three-dimensional finite strain constitutive theory in the time domain in this essay. As we demonstrate, the Payne effect is reproduced in the frequency domain and the closed form expressions are calculated analytically for the dynamic moduli.

## 2. Experimental data of carbon black-filled rubber

For the purpose of formulating a three-dimensional constitutive theory to describe the dynamic behaviour of carbon black-filled rubber, experimental tests were carried out in the tyre testing laboratories of the Continental company in Germany (cf. Reinhardt, 2001). We selected a tread compound with a shore-A hardness of about 68 and a carbon black content of 60 phr. Both the diameter and the length $l_{\mathrm{R}}$ of the undeformed specimens were about 10 mm and the testing temperature was about $10\ ^{\circ}\mathrm{C}$ or 283 K. In order to exclude the Mullins effect, i.e. the softening phenomenon during the first deformation cycles, all specimens were preconditioned with a cyclic strain-controlled process. The maximum strain reached in this process has to be similar to or larger than the maximum strain reached in the real experiments (cf. Lion, 1996). In the preconditioning process applied in this essay, the pre-strain was about $-0.3$ under compression and the amplitude 0.13. If preconditioning were omitted, the Mullins effect would be superimposed by the physical phenomena of interest, which would complicate the interpretation of the recorded data or even make it impossible. Subsequent to this preconditioning process, a temporally constant pre-strain $\varepsilon_{0}=u_{0}/l_{0}=-0.11$ was applied under compression. The amplitude $\Delta\varepsilon$ of the superimposed harmonic strain was varied between $0.001\ (0.1\%)$ and $0.05\ (5\%)$ and the frequency between 10 and 60 Hz. Additional experiments were carried out with pre-strains $\varepsilon_{0}=-0.2$ and $\varepsilon_{0}=-0.3$ but the behaviour of the dynamic moduli as a function of frequency and amplitude was identical. We refer the reader to Reinhardt (2001).

The experimental data of the dynamic moduli $G'$ and $G''$ belonging to $\varepsilon_{0}=-0.1$ were plotted in Figs. 2 and 3 against the strain amplitude for different frequencies.

![](./images/812370043483455489_4.jpg)

Fig. 2. Storage modulus at different amplitudes and frequencies.

![](./images/812370043483455489_5.jpg)

Fig. 3. Dissipation modulus at different amplitudes and frequencies.

We observe a pronounced decrease of the storage modulus and a less pronounced sigmoidal behaviour of the dissipation modulus with increasing strain amplitudes. Since the storage modulus is a measure for the stiffness of the material, it is pro- portional to the number of intact physical bonds which can transfer forces on the microscopic scale. Its monotonic decline is caused by a decrease in the number of intact bonds with increasing amplitudes. As we know, the dissipation modulus is a measure for the energy loss per loading cycle and is proportional to the breakage rate of the bonds. Since the rate of breakage is proportional to the number of intact bonds and increases with increasing amplitudes, we observe a sigmoidal behaviour: in the ascending flanks of the curves, the energy loss increases with the amplitude because there are enough intact bonds; in the descending flank of the curve the energy loss decreases with the amplitude because the number of intact bonds has considerably decreased.

As we observe in the plots, the frequency dependence is monotonically in both cases. i.e. increasing frequencies lead to an increase in stiffness and an increase in energy loss per cycle.

### 3. General constitutive theory

The general constitutive theory to be formulated in this essay is based on the foundations provided by Haupt and Lion (2002). Since elastomeric materials behave incompressibly in many engineering applications, we assume

$$\operatorname{det}(\mathbf{F})=1. \tag{10}$$

The space and time-dependent tensor field $\mathbf{F}(\mathbf{X}, t)$ is the deformation gradient. In this case, the general stress response can be written as

$$
\mathbf{S}=-p \mathbf{1}+\mathbf{S}_{\mathrm{E}}
\tag{11}
$$

or

$$
\tilde{\mathbf{T}}=-p \mathbf{C}^{-1}+\tilde{\mathbf{T}}_{\mathrm{E}},
\tag{12}
$$

where $\mathbf{S}=\operatorname{det}(\mathbf{F}) \mathbf{T}$ is the weighted Cauchy stress tensor, $\mathbf{T}$ the Cauchy stress tensor, $\mathbf{1}$ the 2nd order unit tensor, $\mathbf{S}_{\mathrm{E}}$ the weighted Cauchy extra stress, $\tilde{\mathbf{T}}=\mathbf{F}^{-1} \mathbf{S} \mathbf{F}^{T-1}$ the 2nd Piola Kirchhoff stress, $\tilde{\mathbf{T}}_{\mathrm{E}}=\mathbf{F}^{-1} \mathbf{S}_{\mathrm{E}} \mathbf{F}^{T-1}$ the corresponding extra stress, $\mathbf{C}=$ $\mathbf{F}^{T} \mathbf{F}$ the right Cauchy Green tensor and $p$ the constitutively non-determined pressure. For the sake of simplicity we assume a constant temperature distribution in space and time, so that it is sufficient to consider the isothermal form of the 2nd law of thermodynamics:

$$
-\rho_{\mathrm{R}} \dot{\psi}+\tilde{\mathbf{T}}_{\mathrm{E}} \cdot \dot{\mathbf{E}} \geqslant 0
\tag{13}
$$

In the Clausius Duhem inequality $\rho_{\mathrm{R}}$ is the mass density of the reference configuration, $\psi$ the free energy per unit mass, $\mathbf{E}=1 / 2(\mathbf{C}-\mathbf{1})$ the Green strain tensor and a superscript dot denotes the material time rate. Since we have $\operatorname{det}(\mathbf{C})=$ 1 and therefore $\mathrm{d} / \mathrm{d} t \operatorname{det}(\mathbf{C})=0=\operatorname{det}(\mathbf{C}) \mathbf{C}^{-1} \cdot \dot{\mathbf{C}}$, the power $-p \mathbf{C}^{-1} \cdot \dot{\mathbf{E}}=$ $-1 / 2 p \mathbf{C}^{-1} \cdot \dot{\mathbf{C}}$ between the constitutively non-determined reaction stress $-p \mathbf{C}^{-1}$ and the kinematical possible strain rate is zero. From a physical point of view, the 2nd law of thermodynamics requires the temporal change in the free energy to be equal to or smaller than the stress power supplied.

As proposed by Haupt and Lion (2002), we first assume the general expression

$$
\rho_{\mathrm{R}} \psi(t)=\frac{1}{2} \mu_{\mathrm{eq}}(\operatorname{tr}(\mathbf{B})-3)-\int_{-\infty}^{t} G(t-s) \operatorname{tr}\left(\mathbf{e}_{t}^{\prime}(s)\right) \mathrm{d} s
\tag{14}
$$

for the free energy functional and demonstrate its compatibility with Eq. (13). To describe the amplitude dependence of the dynamic moduli of filled rubber in a thermodynamically consistent manner, we then replace the time variables $t$ and $s$ by so-called intrinsic time variables $z$ and $\xi$, which are determined by evolution equations. $\mathbf{B}=\mathbf{F F}^{T}$ is the left Cauchy Green tensor, $\operatorname{tr}(\mathbf{B})=\mathbf{B} \cdot \mathbf{1}=B_{11}+B_{22}+B_{33}$ the trace of $\mathbf{B}, \mu_{\text {eq }} \geqslant 0$ an elasticity parameter and $G(t)$ the relaxation function with the asymptotic behaviour $G(\infty)=0$. The tensor

$$
\mathbf{e}_{t}(s)=\mathbf{F}(t)[\mathbf{e}(s)-\mathbf{e}(t)] \mathbf{F}^{T}(t)
\tag{15}
$$

is the relative Piola strain,

$$
\mathbf{e}(t)=1 / 2\left(\mathbf{C}^{-1}(t)-\mathbf{1}\right)
\tag{16}
$$

the Piola strain at time t and $\mathbf{e}_{t}^{\prime}(s)=\mathbf{F}(t) \mathbf{e}^{\prime}(s) \mathbf{F}^{T}(t)$ the derivative of $\mathbf{e}_{t}(s)$ with respect to the past time $s$. If we assume $\mathbf{F}(-\infty)=\mathbf{1}$ in combination with $\operatorname{det}(\mathbf{F})=1$, we obtain:

$$
\mathbf{e}_{t}(t)=\mathbf{0},
\tag{17}
$$

$$
\mathbf{e}_{t}(-\infty)=-\mathbf{F}(t) \mathbf{e}(t) \mathbf{F}^{T}(t)=\frac{1}{2}(\mathbf{B}-\mathbf{1})
\tag{18}
$$

and
$$
\begin{aligned}
\operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(t)\right) & =\left.\mathbf{1} \cdot \frac{\mathrm{d}}{\mathrm{d} s}\left(\mathbf{e}_{t}(s)\right)\right|_{s=t}=\left(\mathbf{F}(t) \mathbf{e}^{\prime}(t) \mathbf{F}^{T}(t)\right) \cdot \mathbf{1}=\mathbf{e}^{\prime}(t) \cdot \mathbf{C}(t) \\
& =-\frac{1}{2} \mathbf{C}^{-1}(t) \mathbf{C}^{\prime}(t) \mathbf{C}^{-1}(t) \cdot \mathbf{C}(t)=-\frac{1}{2} \operatorname{tr}\left(\mathbf{C}^{-1}(t) \mathbf{C}^{\prime}(t)\right) \\
& =-\frac{1}{2} \operatorname{tr}\left(\left[\mathbf{F}^{\prime} \mathbf{F}^{-1}\right]^{T}+\left[\mathbf{F}^{\prime} \mathbf{F}^{-1}\right]\right)=-\operatorname{tr}(\mathbf{D})=0
\end{aligned}
\tag{19}
$$

A superscript prime is the derivative with respect to its argument, for example $\mathbf{e}^{\prime}(t)=\mathrm{d} \mathbf{e}(t) / \mathrm{d} t$ and the symmetric part of the velocity gradient $\mathbf{L}=\dot{\mathbf{F}} \mathbf{F}^{-1}$ is $\mathbf{D}$. Considering $\operatorname{tr}(\mathbf{C})=\operatorname{tr}(\mathbf{B})$, differentiating the free energy specified in Eq. (14) with respect to time,
$$
\rho_{\mathrm{R}} \dot{\psi}(t)=\frac{1}{2} \mu_{\mathrm{eq}} \mathbf{1} \cdot \dot{\mathbf{C}}(t)-G(0) \underbrace{\operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(t)\right)}_{=0}-\int_{-\infty}^{t} \frac{\partial}{\partial t} G(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right) \mathrm{d} s
\tag{20}
$$

and using the identity $\dot{\mathbf{E}}=1 / 2 \dot{\mathbf{C}}$ in combination with
$$
\frac{\partial}{\partial t}\left[G(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right)\right]=G^{\prime}(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right)+G(t-s) \mathbf{e}^{\prime}(s) \cdot \dot{\mathbf{C}}(t)
\tag{21}
$$

($G^{\prime}$ is the derivative of $G$ with respect to its argument) leads to
$$
\rho_{\mathrm{R}} \dot{\psi}(t)=\left[\mu_{\mathrm{eq}} \mathbf{1}-2 \int_{-\infty}^{t} G(t-s) \mathbf{e}^{\prime}(s) \mathrm{d} s\right] \cdot \dot{\mathbf{E}}-\int_{-\infty}^{t} G^{\prime}(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right) \mathrm{d} s.
\tag{22}
$$

Inserting Eq. (22) into the Clausius Duhem inequality Eq. (13), we obtain
$$
\left[\tilde{\mathbf{T}}_{\mathrm{E}}-\mu_{\mathrm{eq}} \mathbf{1}+2 \int_{-\infty}^{t} G(t-s) \mathbf{e}^{\prime}(s) \mathrm{d} s\right] \cdot \dot{\mathbf{E}}+\int_{-\infty}^{t} G^{\prime}(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right) \mathrm{d} s \geqslant 0,
\tag{23}
$$

which is satisfied for arbitrary values of $\dot{\mathbf{E}}$ if the extra stress is determined by
$$
\tilde{\mathbf{T}}_{\mathrm{E}}=\mu_{\mathrm{eq}} \mathbf{1}-2 \int_{-\infty}^{t} G(t-s) \mathbf{e}^{\prime}(s) \mathrm{d} s
\tag{24}
$$

and the dissipation

$$
\int_{-\infty}^{t} G^{\prime}(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right) \mathrm{d} s \geqslant 0
\tag{25}
$$

is non-negative for arbitrary deformation processes. The latter requirement is satisfied if the curvature $G^{\prime \prime}(t)$ of the relaxation function is non-negative. Integration by parts of Eq. (25) and using $\partial G / \partial s=-\partial G / \partial t$ leads to

$$
\begin{aligned}
\int_{-\infty}^{t} G^{\prime}(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right) \mathrm{d} s= & \underbrace{-\left.G(t-s) \operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(s)\right)\right|_{-\infty} ^{t}}_{=0} \\
& +\int_{-\infty}^{t} G^{\prime \prime}(t-s) \operatorname{tr}\left(\mathbf{e}_{t}(s)\right) \mathrm{d} s,
\end{aligned}
\tag{26}
$$

which is non-negative for $G^{\prime \prime}(t) \geqslant 0$ since $G(\infty)=0$ and $\operatorname{tr}\left(\mathbf{e}^{\prime}{ }_{t}(t)\right)=0$. Haupt and Lion (2002) demonstrated that $\operatorname{tr}\left(\mathbf{e}_{t}(s)\right) \geqslant 0$ in the case of incompressibility.

In order to obtain an additional requirement for the relaxation function we take the free energy defined by Eq. (14) into account. Integration by parts leads to

$$
\begin{aligned}
\rho_{\mathrm{R}} \psi(t)= & \frac{1}{2} \mu_{\mathrm{eq}} \underbrace{(\operatorname{tr}(\mathbf{B})-3)}_{\geqslant 0}-\left[\underbrace{G(\infty)}_{=0} \operatorname{tr}\left(\mathbf{e}_{t}(-\infty)\right)-G(0) \underbrace{\operatorname{tr}\left(\mathbf{e}_{t}(t)\right)}_{=0}\right] \\
& -\int_{-\infty}^{t} G^{\prime}(t-s) \operatorname{tr}\left(\mathbf{e}_{t}(s)\right) \mathrm{d} s
\end{aligned}
\tag{27}
$$

which is non-negative if the requirement $G^{\prime}(t) \leqslant 0$ is satisfied, i.e. if the relaxation function is monotonically decreasing.

To derive the third requirement for the relaxation function we consider the general stress functional in the form of Eqs. (12) and (24),

$$
\tilde{\mathbf{T}}=-p \mathbf{C}^{-1}+\mu_{\mathrm{eq}} \mathbf{1}-2 \int_{-\infty}^{t} G(t-s) \mathbf{e}^{\prime}(s) \mathrm{d} s,
\tag{28}
$$

prescribe a jump in the deformation gradient,

$$
\mathbf{F}(t)= \begin{cases}\mathbf{1} \text { for } t \leqslant 0 \\ \mathbf{F}_{0} \text { for } t>0\end{cases}
\tag{29}
$$

and calculate the corresponding stress response $\tilde{\mathbf{T}}_{0}(t)=\mathbf{F}_{0}^{-1} \mathbf{S}_{0}(t) \mathbf{F}_{0}^{T-1}$ for $t>0$. Integration of Eq. (28) by parts and considering $\mathbf{e}(-\infty)=\mathbf{0}$ leads to the intermediate result

$$
\tilde{\mathbf{T}}_{0}=-p \mathbf{C}^{-1}+\mu_{\mathrm{eq}} \mathbf{1}-2 G(0) \mathbf{e}(t)-2 \int_{-\infty}^{t} G^{\prime}(t-s) \mathbf{e}(s) \mathrm{d} s.
\tag{30}
$$

Taking Eq. (29), the definitions $\mathbf{C}_{0}^{-1}=\mathbf{F}_{0}^{-1} \mathbf{F}_{0}^{T-1}, \quad \mathbf{B}_{0}=\mathbf{F}_{0} \mathbf{F}_{0}^{T}$ and $\mathbf{e}_{0}=1 / 2\left(\mathbf{C}_{0}^{-1}-\mathbf{1}\right)$, the push forward transformation $\mathbf{S}_{0}(t)=\mathbf{F}_{0} \tilde{\mathbf{T}}_{0}(t) \mathbf{F}_{0}^{T}$ and $t>0$ into account, we obtain


$$
\mathbf{S}_{0}(t)=-p \mathbf{1}+\mu_{\mathrm{eq}} \mathbf{B}_{0}+G(t)\left[\mathbf{B}_{0}-\mathbf{1}\right].
$$

Assuming uniaxial tension, i.e. $\mathbf{F}_{0}=\lambda_{0} \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}+\lambda_{0}^{-1 / 2}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right)$ and $\mathbf{S}_{0}=$ $\sigma_{0} \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}$ we find the relation

$$
\sigma_{0}(t)=\mu_{\mathrm{eq}}\left[\lambda_{0}^{2}-\frac{1}{\lambda_{0}}\right]+G(t)\left[\lambda_{0}^{2}-\frac{1}{\lambda_{0}}\right],
$$

which confirms the physical meaning of $G(t)$ as the relaxation function and supplies the third requirement in the form of $G(t) \geqslant 0$. Obviously, the stress response belonging to a jump in the deformation gradient demonstrates the free energy Eq. (14) to correspond to a constitutive law of a viscoelastic Neo Hookean material. The first term is the equilibrium stress, the second term the overstress and the constant $\mu_{\text {eq }}$ corresponds to the equilibrium modulus of elasticity.

This discussion has shown that the free energy functional Eq. (14) and the corre- sponding stress Eq. (24) and dissipation Eq. (25) are thermodynamically consistent if the requirements

$$
G(t) \geqslant 0, \quad G^{\prime}(t) \leqslant 0, \quad G^{\prime \prime}(t) \geqslant 0
$$

are satisfied. These are much weaker requirements for $G(t)$ than the frequently used complete monotony in the form of $(-1)^{n} d^{n} G / \mathrm{d} t^{n} \geqslant 0$ with $n=0,1,2, \ldots$ (cf. Schwarzl 1990, p. 144).

Since this model is not able to describe the amplitude dependence of dynamic moduli, we reformulate the process-dependent part of the free energy. To this end, we replace the physical time variables $t$ and $s$ by process-dependent intrinsic time variables $z$ and $\xi$,

$$
\rho_{\mathrm{R}} \psi(t)=\frac{1}{2} \mu_{\mathrm{eq}}(\operatorname{tr}(\mathbf{B}(t))-3)-\int_{-\infty}^{z(t)} G(z(t)-\xi) \operatorname{tr}\left(\frac{\partial}{\partial \xi} \mathbf{e}_{z}(\xi)\right) \mathrm{d} \xi,
$$

with

$$
\dot{z}(t)=M(\ldots) \geqslant 0, \quad z(t)=\int_{-\infty}^{t} M(\ldots) \mathrm{d} \tau, \quad \xi=\int_{-\infty}^{s} M(\ldots) \mathrm{d} \tau
$$

and

$$
\mathbf{e}_{z}(\xi)=\mathbf{F}(z)\left[\mathbf{e}(\xi)-\mathbf{e}(z)\right] \mathbf{F}^{T}(z).
$$

The scalar function $M(\ldots)$ depends on the process history and describes the rate of the intrinsic time with respect to the physical time. Since time-like variables should monotonically increase the requirement $M \geqslant 0$ is obvious. The idea to replace the physical time by another time variable was originally introduced by

Valanis (1971) and applied, for example, by Krempl and Bordonaro (1998) in the context of Nylon 66. For details we also refer the reader to Haupt (2002).

In order to prove the thermodynamical consistency of this model, we apply the chain rule $\mathrm{d}/\mathrm{d}t=\dot{z}(t)\mathrm{d}/\mathrm{d}z$, calculate the material time rate of Eq. (34) [cf. Eqs. (19) and (20)],

$$
\begin{aligned}
\rho_{\mathrm{R}} \dot{\psi}(t)=& \frac{1}{2} \mu_{\mathrm{eq}} \mathbf{1} \cdot \dot{\mathbf{C}}(t) \\
& -\left\{\underbrace{G(0) \operatorname{tr}\left(\left.\frac{\partial}{\partial \xi} \mathbf{e}_{z}(\xi)\right|_{\xi=z}\right)}_{=0}-\int_{-\infty}^{z(t)} \frac{\partial}{\partial z}\left(G(z-\xi) \operatorname{tr}\left(\frac{\partial}{\partial \xi} \mathbf{e}_{z}(\xi)\right)\right) \mathrm{d} \xi\right\} \dot{z}(t)
\end{aligned}
\tag{37}
$$

take the relation $2\dot{\mathbf{E}}=\dot{z}d\mathbf{C}/\mathrm{d}z$ into account and find

$$
\begin{aligned}
\rho_{\mathrm{R}} \dot{\psi}(t)= & {\left[\mu_{\mathrm{eq}} \mathbf{1}-2 \int_{-\infty}^{z} G(z-\xi) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi\right] \cdot \dot{\mathbf{E}} } \\
& -\int_{-\infty}^{z} G^{\prime}(z-\xi)^{\prime} \operatorname{tr}\left(\frac{\partial}{\partial \xi} \mathbf{e}_{z}(\xi)\right) \mathrm{d} \xi \quad M(\ldots).
\end{aligned}
\tag{38}
$$

Inserting this result into the Clausius Duhem inequality Eq. (13), we obtain the expression

$$
\begin{aligned}
& {\left[\tilde{\mathbf{T}}_{\mathrm{E}}-\mu_{\mathrm{eq}} \mathbf{1}+2 \int_{-\infty}^{z} G(z-\xi) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi\right] \cdot \dot{\mathbf{E}} } \\
& \quad+\int_{-\infty}^{z} G^{\prime}(z-\xi) \operatorname{tr}\left(\frac{\partial}{\partial \xi} \mathbf{e}_{z}(\xi)\right) \mathrm{d} \xi \quad M(\ldots) \geqslant 0
\end{aligned}
\tag{39}
$$

which is non-negative for the stress strain relation

$$
\tilde{\mathbf{T}}_{\mathrm{E}}=\mu_{\mathrm{eq}} \mathbf{1}-2 \int_{-\infty}^{z} G(z-\xi) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi
\tag{40}
$$

for the extra stress and the dissipation

$$
\int_{-\infty}^{z} G^{\prime}(z-\xi) \operatorname{tr}\left(\frac{\partial}{\partial \xi} \mathbf{e}_{z}(\xi)\right) \mathrm{d} \xi \mathrm{M}(\ldots) \geqslant 0,
\tag{41}
$$

since $M\geqslant0$ and

$$
G(z)\geqslant0,\quad G'(z)\leqslant0,\quad G''(z)\geqslant0
\tag{42}
$$

is assumed. The three inequalities of Eq. (42) require the relaxation function to be non-negative, to decrease monotonically and to have a non-negative curvature with respect to its argument. In comparison with Eq. (33), the only additional requirement for thermodynamical consistency is $M \geqslant 0$. It is a natural requirement with no restriction, because the intrinsic time has to be a monotonic increasing quantity.

## 4. A special model for carbon black-reinforced rubber

The frequency dependence of the dynamic moduli of filler-reinforced rubber is fairly weak (cf. Figs. 2 and 3) and essentially of the power-law type (cf. Lion, 1998). As shown in recent literature (cf. Metzeler and Nonnenmacher, 2003; Haupt and Lion, 2002; Drozdov, 1997; Drozdov, 1998; Metzeler et al., 1995; Caputo and Mainardi, 1971), such behaviour can be represented with a minimum of material constants using the fractional calculus. An adequate and thermomechanically consistent, uniaxial model for small strains is the so-called fractional standard linear solid (cf. Haupt et al., 2000; Lion, 2001, Mainardi, 1997; Koeller, 1984). It corresponds to a linear spring with a modulus $\mu_{\text {eq }}$ in parallel with a fractional Maxwell element (spring with a modulus $\mu_{\mathrm{ov}}$ in series with a fractional damper with a viscosity $\zeta^{\beta} \mu_{\mathrm{ov}}$ ):

$$
\sigma=\sigma_{\mathrm{ov}}+\mu_{\mathrm{eq}} \varepsilon \text { with } \sigma_{\mathrm{ov}}+\zeta^{\beta} \frac{\mathrm{d}^{\beta} \sigma_{\mathrm{ov}}}{\mathrm{d} t^{\beta}}=\mu_{\mathrm{ov}} \zeta^{\beta} \frac{\mathrm{d}^{\beta} \varepsilon}{\mathrm{d} t^{\beta}}
\tag{43}
$$

Looking at Eq. (43), we see that this fractional differential equation is fairly similar to the first order differential equation of the classical Maxwell element: $\mu_{\mathrm{ov}}$ is the elastic modulus and $\zeta$ the relaxation time. The difference to the classical element is that the first order derivatives of stress and strain are replaced by fractional derivatives of the (same) order $0 \leqslant \beta<1$. Different derivative orders would lead to thermodynamical inconsistencies, for example to a negative dissipation modulus, which has been shown by Lion (2001). In the sense of the Riemann Liouville definition, the fractional differential operator $\mathrm{d}^{\beta} / \mathrm{d} t^{\beta}$ is defined as

$$
\frac{\mathrm{d}^{\beta}}{\mathrm{d} t^{\beta}} f(t)=\frac{1}{\Gamma(1-\beta)} \int_{0}^{t} \frac{f^{\prime}(s)}{(t-s)^{\beta}} \mathrm{d} s \quad 0 \leqslant \beta<1,
\tag{44}
$$

where $f$ is a causal function with $f(s) \equiv 0$ for $s \leqslant 0$; $\Gamma(x)$ is the Eulerian Gamma function. Using the Laplace transformation technique, it can be shown that the functional representation of Eq. (43) reads as

$$
\sigma(t)=\int_{0}^{t}\left\{\mu_{\mathrm{eq}}+\mu_{\mathrm{ov}} E_{\beta}\left(-\left(\frac{t-s}{\zeta}\right)^{\beta}\right)\right\} \varepsilon^{\prime}(s) \mathrm{d} s
\tag{45}
$$

where the kernel

$$
E_{\beta}(x)=\sum_{k=0}^{\infty} \frac{x^{k}}{\Gamma(1+\beta k)}
\tag{46}
$$

is the Mittag Leffler function. For the details we refer the reader to the textbook of Oldham and Spanier (1974), Caputo and Mainardi (1971), Haupt and Lion (2002) or to the references cited by Metzeler and Nonnenmacher (2003). Since $E_{\beta}(x)$ equals the exponential function for $\beta=1$, the Mittag Leffler function is also known as the fractional exponential function. An application of this model to describe the frequency dependence of the dynamic moduli of a polyethylene melt can be found in Haupt et al. (2000).

In order to combine the fundamental characteristics of the fractional standard linear solid specified by Eq. (43) to describe frequency-dependent material behaviour with the concept of a process-dependent time scale, we propose the constitutive model (cf. Eq. (40))

$$
\tilde{\mathbf{T}}_{\mathrm{E}}=\mu_{\mathrm{eq}} \mathbf{1}-2 \int_{-\infty}^{z} G(z-\xi) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi
\tag{47}
$$

for the extra stress tensor with the relaxation function

$$
G(z)=\mu_{\mathrm{ov}} E_{\beta}\left(-\left(\frac{z}{\zeta}\right)^{\beta}\right)=\mu_{\mathrm{ov}} \sum_{k=0}^{\infty} \frac{(-1)^{k}\left(\frac{z}{\zeta}\right)^{\beta k}}{\Gamma(1+\beta k)}.
\tag{48}
$$

Since the Mittag Leffler function $E_{\beta}(-(z / \zeta)^{\beta})$ possesses a positive relaxation spectrum [see Eq. (32) in Haupt et al., 2000] and thus satisfies the requirements of Eq. (42), this model is compatible with the 2nd law of thermodynamics. For the evolution of the intrinsic time variable $z(t)$ we transfer the one-dimensional approach proposed by Lion et al. (2003) to finite strains, where the rate $\mathrm{d} z / \mathrm{d} t$ is assumed to be a linear function of a structural variable $q(t)$,

$$
\dot{z}(t)=1+b q(t) \text { with } z(0)=0.
\tag{49}
$$

$b \geqslant 0$ is a material parameter. In the context of a physical interpretation the variable $q(t)$ is a phenomenological measure for the current state of the material's microstructure and is determined by the evolution equation

$$
\dot{q}(t)=\frac{1}{\lambda}\left(\tau^{\alpha} \sqrt{\frac{2}{3}}\left\|\mathbf{F}(t)\left\{\frac{\mathrm{d}^{\alpha}}{\mathrm{d} t^{\alpha}} \mathbf{e}(t)\right\} \mathbf{F}^{T}(t)\right\|-q\right)
\tag{50}
$$

with $\|\mathbf{Y}\|=(\mathbf{Y} \cdot \mathbf{Y})^{1 / 2}=\sqrt{\sum_{i, k=1}^{3} Y_{i k}^{2}}$ and the initial condition

$$
q(0)=0.
\tag{51}
$$

The constant $\tau = 1s$ is introduced for dimensional reasons and $\lambda > 0$ is a material parameter corresponding to the duration of structural relaxation phenomena. The values of $\lambda$ are in the region of several hundred seconds (cf. Lion, 1999 and references therein). The reason for the introduction of the fractional derivative of the Piola strain as the driving force for the structural variable is the combined frequency and amplitude dependence of filled rubber.

In order to demonstrate that the overstress of the second Piola Kirchhoff type

$$
\tilde{\mathbf{T}}_{\mathrm{ov}}=-2 \mu_{\mathrm{ov}} \int_{0}^{z} E_{\beta}\left(-\left(\frac{z-\xi}{\zeta}\right)^{\beta}\right) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi
\tag{52}
$$

satisfies a differential equation similar to Eq. (43), we define the fractional differentiation with respect to the intrinsic time $z$,

$$
\frac{\mathrm{d}^{\beta}}{\mathrm{d} z^{\beta}} \tilde{\mathbf{T}}_{\mathrm{ov}}=\frac{1}{\Gamma(1-\beta)} \int_{0}^{z} \frac{\tilde{\mathbf{T}}_{\mathrm{ov}}^{\prime}(\bar{z})}{(z-\bar{z})^{\beta}} \mathrm{d} \bar{z}.
\tag{53}
$$

Then we calculate

$$
\tilde{\mathbf{T}}_{\mathrm{ov}}^{\prime}(\bar{z})=-2 \mu_{\mathrm{ov}} \mathbf{e}^{\prime}(\bar{z})-2 \mu_{\mathrm{ov}} \int_{0}^{\bar{z}} \frac{\mathrm{d}}{\mathrm{d} \bar{z}} E_{\beta}\left(-\left(\frac{\bar{z}-\xi}{\zeta}\right)^{\beta}\right) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi
\tag{54}
$$

since $E_{\beta}(0)=1$ and

$$
\frac{\mathrm{d}}{\mathrm{d} \bar{z}} E_{\beta}\left(-\left(\frac{\bar{z}-\xi}{\zeta}\right)^{\beta}\right)=\frac{1}{\zeta} \sum_{k=1}^{\infty} \frac{(-1)^{k}}{\Gamma(\beta k)}\left(\frac{\bar{z}-\xi}{\zeta}\right)^{\beta k-1},
\tag{55}
$$

where the functional equation $\Gamma(1+\beta k)=\beta k \Gamma(\beta k)$ of the Gamma function has been taken into account and obtain

$$
\begin{aligned}
\frac{\mathrm{d}^{\beta} \tilde{\mathbf{T}}_{\mathrm{ov}}}{\mathrm{d} z^{\beta}}= & -2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \mathbf{e}}{\mathrm{d} z^{\beta}} \\
& -\frac{2 \mu_{\mathrm{ov}}}{\zeta} \int_{0}^{z} \int_{0}^{\bar{z}} \sum_{k=1}^{\infty} \frac{(-1)^{k}(z-\bar{z})^{-\beta}(\bar{z}-\xi)^{\beta k-1}}{\Gamma(1-\beta) \Gamma(\beta k)}\left(\frac{1}{\zeta}\right)^{\beta k-1} \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi \mathrm{d} \bar{z}.
\end{aligned}
\tag{56}
$$

Considering the identity

$$
\int_{0}^{z} \int_{0}^{\bar{z}} f(\xi, \bar{z}) \mathrm{d} \xi \mathrm{d} \bar{z}=\int_{0}^{z} \int_{\xi}^{z} f(\xi, \bar{z}) \mathrm{d} \bar{z} \mathrm{d} \xi
\tag{57}
$$

valid for $0 \leqslant \xi \leqslant \bar{z} \leqslant z$ (see, for example, Hackbusch, 1997) and exchanging the sequence of integration and summation (cf. Burg et al., 1985) leads to

$$
\begin{aligned}
\frac{\mathrm{d}^{\beta} \tilde{\mathbf{T}}_{\mathrm{ov}}}{\mathrm{d} z^{\beta}}= & -2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \mathbf{e}}{\mathrm{d} z^{\beta}} \\
& -\frac{2 \mu_{\mathrm{ov}}}{\zeta} \int_{0}^{z} \sum_{k=1}^{\infty} \int_{\xi}^{z} \frac{(-1)^{k}(z-\bar{z})^{-\beta}(\bar{z}-\xi)^{\beta k-1}}{\Gamma(1-\beta) \Gamma(\beta k)}\left(\frac{1}{\zeta}\right)^{\beta k-1} \mathrm{~d} \bar{z} \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi.
\end{aligned}
\tag{58}
$$

Applying the substitution $x=(z-\bar{z})/(z-\xi)$ and $\int_{0}^{1}x^{a}(1-x)^{b}\mathrm{d}x=\Gamma(1+a)\Gamma(1+b)/\Gamma(2+a+b)$ to evaluate the inner integral, we obtain

$$
\int_{\xi}^{z}(z-\bar{z})^{-\beta}(\bar{z}-\xi)^{\beta k-1} d \bar{z}=(z-\xi)^{\beta(k-1)} \frac{\Gamma(1-\beta) \Gamma(\beta k)}{\Gamma(1+\beta(k-1))}
\tag{59}
$$

and with Eq. (58)

$$
\begin{aligned}
\frac{\mathrm{d}^{\beta} \tilde{\mathbf{T}}_{\mathrm{ov}}}{\mathrm{d} z^{\beta}}=-2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \mathbf{e}}{\mathrm{d} z^{\beta}}+\frac{2 \mu_{\mathrm{ov}}}{\zeta^{\beta}} \int_{0}^{z} \underbrace{\sum_{k=1}^{\infty} \frac{(-1)^{k-1}(z-\xi)^{\beta(k-1)}}{\zeta^{\beta(k-1)} \Gamma(1+\beta(k-1))}}_{=\sum_{k=0}^{\infty} \frac{(-1)^{k}(z-\xi)^{\beta k}}{\zeta^{\beta k} \Gamma(1+\beta k)}=E_{\beta}\left(-\left(\frac{z-\xi}{\zeta}\right)^{\beta}\right)} \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \mathrm{d} \xi.
\end{aligned}
\tag{60}
$$

This leads finally to the fractional differential equation

$$
\frac{\mathrm{d}^{\beta} \tilde{\mathbf{T}}_{\mathrm{ov}}}{\mathrm{d} z^{\beta}}=-2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \mathbf{e}}{\mathrm{d} z^{\beta}}-\frac{1}{\zeta^{\beta}} \tilde{\mathbf{T}}_{\mathrm{ov}}
\tag{61}
$$

between the overstress of the second Piola Kirchhoff type and the Piola strain tensor.

As the main difference to the constitutive model proposed by Haupt and Lion (2002, Eq. 6.18), we notice that Eq. (61) is formulated not with respect to the physical time but with respect to an intrinsic time variable. Since the intrinsic time is a functional of the deformation process, Eq. (61) corresponds to a nonlinear functional between the involved stress and strain tensors.

## 5. Linearisation of the model

For the purpose of fitting the finite strain constitutive model to the experimental data of the dynamic moduli, we linearise all kinematical and constitutive equations relative to the pre-deformed state as sketched in Fig. 4.

To this end we consider a finite but temporally constant pre-deformation, described by the space-dependent deformation gradient $\mathbf{F}_{0}(\mathbf{X}_{\mathrm{R}})$; $\mathbf{X}_{\mathrm{R}}$ are the material coordinates of the reference and $\mathbf{X}_{0}$ the spatial coordinates of the pre-deformed

configuration. The space and time-dependent incremental deformation gradient $\mathbf{f}(\mathbf{X}_{0},t)$ operates on the pre-deformed configuration, maps material tangent vectors to the current configuration and is superimposed as follows (the space dependence is omitted):

$$
\mathbf{F}(t)=\mathbf{f}(t)\mathbf{F}_{0} \tag{62}
$$

Since we assume the incremental deformations to be small, $\mathbf{f}$ is nearly the unit tensor, i.e.

$$
\mathbf{f}(t)=\mathbf{1}+\mathbf{h}(t) \text{ with } \|\mathbf{h}(t)\|=\tilde{\delta}(t),\ \delta=\max_{\substack{\mathbf{X}_{0}\in P\\0\leqslant t\leqslant T}}\tilde{\delta}(\mathbf{X}_{0},t),\ \delta<<1 \tag{63}
$$

where $\delta$ is a measure for the magnitude of the incremental displacement gradient $\mathbf{h}$ operating on the pre-deformed configuration as well; $T$ is the duration of the process. In the following we consider $\delta<<1$, linearise all kinematical tensors and obtain

$$
\mathbf{F}^{-1}=\left[(\mathbf{1}+\mathbf{h})\mathbf{F}_{0}\right]^{-1}=\mathbf{F}_{0}^{-1}(\mathbf{1}+\mathbf{h})^{-1}=\mathbf{F}_{0}^{-1}(\mathbf{1}-\mathbf{h})+\mathbf{O}(\delta^{2}), \tag{64}
$$

$$
\begin{aligned}
\mathbf{C}&=\mathbf{F}^{T}\mathbf{F}=\mathbf{F}_{0}^{T}(\mathbf{1}+\mathbf{h})^{T}(\mathbf{1}+\mathbf{h})\mathbf{F}_{0}=\mathbf{F}_{0}^{T}(\mathbf{1}+\mathbf{h}+\mathbf{h}^{T})\mathbf{F}_{0}+\mathbf{O}(\delta^{2})\\
&=\mathbf{C}_{0}+\mathbf{F}_{0}^{T}(\mathbf{h}+\mathbf{h}^{T})\mathbf{F}_{0}+\mathbf{O}(\delta^{2})=\mathbf{C}_{0}+2\mathbf{F}_{0}^{T}\mathbf{E}_{\mathbf{L}}\mathbf{F}_{0}+\mathbf{O}(\delta^{2}),
\end{aligned} \tag{65}
$$

$$
\mathbf{C}^{-1}=\mathbf{F}^{-1}\mathbf{F}^{T-1}=\mathbf{C}_{0}^{-1}-2\mathbf{F}_{0}^{-1}\mathbf{E}_{\mathbf{L}}\mathbf{F}_{0}^{T-1}+\mathbf{O}(\delta^{2}), \tag{66}
$$

![](./images/812370043483455489_6.jpg)

Fig. 4. Different configurations.

$$
\mathbf{B}=\mathbf{F F}^{T}=\mathbf{B}_{0}+\mathbf{h} \mathbf{B}_{0}+\mathbf{B}_{0} \mathbf{h}^{T}+\mathbf{O}\left(\delta^{2}\right),
\tag{67}
$$

$$
\mathbf{E}=\frac{1}{2}[\mathbf{C}-\mathbf{1}]=\frac{1}{2}\left[\mathbf{C}_{0}-\mathbf{1}\right]+\mathbf{F}_{0}^{T} \mathbf{E}_{\mathrm{L}} \mathbf{F}_{0}+\mathbf{O}\left(\delta^{2}\right)=\mathbf{E}_{0}+\mathbf{F}_{0}^{T} \mathbf{E}_{\mathrm{L}} \mathbf{F}_{0}+\mathbf{O}\left(\delta^{2}\right),
\tag{68}
$$

$$
\begin{aligned}
\mathbf{e} & =\frac{1}{2}\left[\mathbf{C}^{-1}-\mathbf{1}\right]=\frac{1}{2}\left[\mathbf{C}_{0}^{-1}-\mathbf{1}\right]-\mathbf{F}_{0}^{-1} \mathbf{E}_{\mathrm{L}} \mathbf{F}_{0}^{T-1}+\mathbf{O}\left(\delta^{2}\right) \\
& =\mathbf{e}_{0}-\mathbf{F}_{0}^{-1} \mathbf{E}_{\mathrm{L}} \mathbf{F}_{0}^{T-1}+\mathbf{O}\left(\delta^{2}\right).
\end{aligned}
\tag{69}
$$

If $\mathbf{Y}$ is a 2nd order tensor and we have $\|\mathbf{Y}\| \leqslant M \delta^{r}$ for $\delta \rightarrow 0$, we write $\mathbf{Y}=\mathbf{O}\left(\delta^{r}\right)$, where $\mathbf{O}$ is the Landau symbol; the definitions
$$
\mathbf{C}_{0}=\mathbf{F}_{0}^{T} \mathbf{F}_{0}, \quad \mathbf{B}_{0}=\mathbf{F}_{0} \mathbf{F}_{0}^{T},
\tag{70}
$$
and
$$
\mathbf{E}_{\mathrm{L}}=\frac{1}{2}\left[\mathbf{h}+\mathbf{h}^{T}\right]
\tag{71}
$$
have been applied in the above equations.

To linearise the differential equation Eq. (61), let us calculate the fractional time rate of the linear portion of the Piola strain tensor Eq. (69). First we define the unit step function or Heaviside function
$$
\theta(x)=\left\{\begin{array}{l}
0 \text { for } x \leqslant 0 \\
1 \text { for } x>0
\end{array}\right.
\tag{72}
$$
and calculate the fractional derivative of a constant tensor $\mathbf{e}_{0}$ multiplied by $\theta(x)$. Taking the property $\mathrm{d} \theta(x) / \mathrm{d} x=\Delta(x)$ into account, where $\Delta(x)$ is the Dirac function, we find
$$
\frac{\mathrm{d}^{\beta}}{\mathrm{d} z^{\beta}}\left[\mathbf{e}_{0} \theta(z)\right]=\frac{\mathbf{e}_{0}}{\Gamma(1-\beta)} \int_{0}^{z} \frac{\Delta(\bar{z})}{(z-\bar{z})^{\beta}} d \bar{z}=\frac{\mathbf{e}_{0}}{\Gamma(1-\beta)} \frac{1}{z^{\beta}} \rightarrow 0 \text { for } z \rightarrow \infty,
\tag{73}
$$
i.e. the fractional derivative of constant tensors tends asymptotically to zero. Considering this result in combination with Eq. (69), we obtain the asymptotic relation
$$
\frac{\mathrm{d}^{\beta}}{\mathrm{d} z^{\beta}} \mathbf{e} \approx \frac{\mathrm{d}^{\beta}}{\mathrm{d} z^{\beta}}\left[\mathbf{e}_{0}-\mathbf{F}_{0}^{-1} \mathbf{E}_{\mathrm{L}}(z) \mathbf{F}_{0}^{T-1}\right]=-\mathbf{F}_{0}^{-1} \frac{\mathrm{d}^{\beta} \mathbf{E}_{\mathrm{L}}}{\mathrm{d} z^{\beta}} \mathbf{F}_{0}^{T-1},
\tag{74}
$$
valid for large values of $z$ and sufficiently small $\delta$. Looking at the evolution law Eq. (50), the linearisation of the tensor $\mathbf{F}(t)\left(\mathrm{d}^{\alpha} \mathbf{e} / \mathrm{d} t^{\alpha}\right) \mathbf{F}^{T}(t)$ for large times reads as

$$
\begin{aligned}
\lim _{t \rightarrow \infty} \mathbf{F}(t)\left\{\frac{\mathrm{d}^{\alpha}}{\mathrm{d} t^{\alpha}} \mathbf{e}(t)\right\} \mathbf{F}^{T}(t) & \approx-\lim _{t \rightarrow \infty}\left(\mathbf{F}_{0}+\mathbf{h}\right)\left\{\mathbf{F}_{0}^{-1} \frac{\mathrm{d}^{\alpha} \mathbf{E}_{\mathrm{L}}}{\mathrm{d} t^{\alpha}} \mathbf{F}_{0}^{T-1}\right\}\left(\mathbf{F}_{0}+\mathbf{h}\right)^{T} \\
& \approx-\frac{\mathrm{d}^{\alpha} \mathbf{E}_{\mathrm{L}}}{\mathrm{d} t^{\alpha}}.
\end{aligned}
$$

In order to linearise the stress, let us take a look at Eq. (52), where the overstress of the second Piola Kirchhoff type is represented as a functional of the history of the Piola strain tensor. Considering Eqs. (69) and (74) we find

$$
\frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{e}(\xi) \approx-\mathbf{F}_{0}^{-1}\left[\frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{E}_{\mathrm{L}}(\xi)\right] \mathbf{F}_{0}^{T-1}.
$$

With the approximation

$$
\begin{aligned}
\tilde{\mathbf{T}}_{\mathrm{ov}} & =\mathbf{F}^{-1} \mathbf{S}_{\mathrm{ov}} \mathbf{F}^{T-1}=\left(\mathbf{F}_{0}^{-1}(\mathbf{1}-\mathbf{h})\right) \mathbf{S}_{\mathrm{ov}}\left((\mathbf{1}-\mathbf{h}) \mathbf{F}_{0}^{T-1}\right)+\mathbf{O}\left(\delta^{2}\right) \\
& \approx \mathbf{F}_{0}^{-1} \mathbf{S}_{\mathrm{ov}} \mathbf{F}_{0}^{T-1}
\end{aligned}
$$

Eq. (52) leads to the geometric linear functional for the overstress,

$$
\mathbf{S}_{\mathrm{ov}}=2 \mu_{\mathrm{ov}} \int_{0}^{z} E_{\beta}\left(-\left(\frac{z-\xi}{\zeta}\right)^{\beta}\right) \frac{\mathrm{d}}{\mathrm{d} \xi} \mathbf{E}_{\mathrm{L}}(\xi) \mathrm{d} \xi.
$$

The linearised version of the fractional differential equation Eq. (61), which is equivalent to the functional representation of Eq. (78), reads as

$$
\frac{\mathrm{d}^{\beta} \mathbf{S}_{\mathrm{ov}}}{\mathrm{d} z^{\beta}}=2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \mathbf{E}_{\mathrm{L}}}{\mathrm{d} z^{\beta}}-\frac{1}{\zeta^{\beta}} \mathbf{S}_{\mathrm{ov}}.
$$

For the constitutive laws determining the intrinsic time, Eqs. (49) and (50), we obtain the linear differential equations

$$
\dot{q}(t)=\frac{1}{\lambda}\left(\tau^{\alpha} \sqrt{\frac{2}{3}}\left\|\frac{\mathrm{d}^{\alpha}}{\mathrm{d} t^{\alpha}} \mathbf{E}_{\mathrm{L}}(t)\right\|-q\right),
$$

and

$$
\dot{z}(t)=1+b q(t) \text { with } z(0)=0.
$$

As we see, the temporal evolution of $q$ is independent of the pre-deformation $\mathbf{F}_{0}$. This is the actual reason, for the introduction of the push forward transformation in Eq. (50). Considering the relations $\tilde{\mathbf{T}}=-p \mathbf{C}^{-1}+\tilde{\mathbf{T}}_{\mathrm{E}}, \tilde{\mathbf{T}}_{\mathrm{E}}=\mu_{\mathrm{eq}} \mathbf{1}+\tilde{\mathbf{T}}_{\mathrm{ov}}$ and $\mathbf{S}=\mathbf{F} \tilde{\mathbf{T}} \mathbf{F}^{T}$ in combination with Eq. (67) and omitting the higher-order terms in the displacement gradient $\mathbf{h}$, we obtain

$$
\begin{aligned}
\mathbf{S}= & -p \mathbf{1}+\mu_{\mathrm{eq}} \mathbf{B}_{0}+\mu_{\mathrm{eq}}\left(\mathbf{h} \mathbf{B}_{0}+\mathbf{B}_{0} \mathbf{h}^{T}\right) \\
& +\mu_{\mathrm{ov}} \int_{0}^{z} E_{\beta}\left(-\left(\frac{z-\xi}{\zeta}\right)^{\beta}\right) \frac{\mathrm{d}}{\mathrm{d} \xi}\left[\mathbf{h}(\xi)+\mathbf{h}^{T}(\xi)\right] \mathrm{d} \xi
\end{aligned}
$$

for the weighted Cauchy stress acting on the current configuration. We see that the total stress is the sum of four terms: the constitutively non-determined reaction stress $-p \mathbf{1}$ is caused by the incompressibility constraint Eq. (10); the static stress $\mu_{\mathrm{eq}} \mathbf{B}_{0}$ is caused by the time-independent pre-deformation; the linear portion of equilibrium stress $\mu_{\mathrm{eq}}\left(\mathbf{h} \mathbf{B}_{0}+\mathbf{B}_{0} \mathbf{h}^{T}\right)$ is determined by the pre-deformation and the incremental strain; the rate-dependent overstress $\mathbf{S}_{\mathrm{ov}}$ is a functional of the deformation history relative to the pre-deformed configuration.

## 6. One-dimensional version of the model for dynamic processes

In order to estimate the material constants, let us evaluate the linearised version of the constitutive model for uniaxial processes under tension and compression. To this end, we prescribe the deformation gradient $\mathbf{F}_{0}$ of the static pre-deformation as
$$
\mathbf{F}_{0}=\lambda_{0} \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}+\frac{1}{\sqrt{\lambda_{0}}}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right),
$$

and the incremental deformation gradient as
$$
\mathbf{f}(t)=\left(1+\varepsilon_{\mathrm{L}}(t)\right) \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}+\frac{1}{\sqrt{1+\varepsilon_{\mathrm{L}}(t)}}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right),
$$

leading to
$$
\mathbf{B}_{0}=\mathbf{F}_{0} \mathbf{F}_{0}^{T}=\lambda_{0}^{2} \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}+\frac{1}{\lambda_{0}}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right),
$$

and
$$
\mathbf{h}(t)=\mathbf{f}(t)-\mathbf{1}=\varepsilon_{\mathrm{L}}(t) \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}+\left(\frac{1}{\sqrt{\left(1+\varepsilon_{\mathrm{L}}(t)\right)}}-1\right)\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right).
$$

Considering the linearisation $\left(1+\varepsilon_{\mathrm{L}}\right)^{-1 / 2} \approx 1-\varepsilon_{\mathrm{L}} / 2$, we obtain
$$
\mathbf{h}(t)=\varepsilon_{\mathrm{L}}(t)\left(\overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}-\frac{1}{2}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right)\right)
$$

and

$$
\mathbf{E}_{\mathrm{L}}(t)=\varepsilon_{\mathrm{L}}(t)\left(\overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}-\frac{1}{2}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right)\right).
\tag{88}
$$

Since the incremental strain tensor $\mathbf{E}_{\mathrm{L}}$ is a deviator which acts as the driving force in Eq. (78), the viscoelastic overstress $\mathbf{S}_{\mathrm{ov}}$ determined by Eq. (78) or (79) has the same structure,

$$
\mathbf{S}_{\mathrm{ov}}(t)=\sigma_{\mathrm{ov}}(t)\left(\overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}-\frac{1}{2}\left(\overrightarrow{\mathbf{e}}_{2} \otimes \overrightarrow{\mathbf{e}}_{2}+\overrightarrow{\mathbf{e}}_{3} \otimes \overrightarrow{\mathbf{e}}_{3}\right)\right).
\tag{89}
$$

Under uniaxial tension and compression the weighted Cauchy stress has no lateral components and reads as

$$
\mathbf{S}(t)=\sigma(t) \overrightarrow{\mathbf{e}}_{1} \otimes \overrightarrow{\mathbf{e}}_{1}.
\tag{90}
$$

For the physical interpretation of the deformation process prescribed above, we can take a look at Fig. 1, where the geometric relations $\lambda_{0}=l_{0} / l_{\mathrm{R}}$ and $\varepsilon_{\mathrm{L}}=(l(t)-$ $l_{0}) / l_{0}$ become clear.

Inserting Eqs. (85), (87), (89) and (90) into Eq. (82), the general functional relation for the weighted Cauchy stress, we obtain

$$
\sigma=-p+\mu_{\mathrm{eq}} \lambda_{0}^{2}+\mu_{\mathrm{eq}}\left(\varepsilon_{\mathrm{L}} \lambda_{0}^{2}+\lambda_{0}^{2} \varepsilon_{\mathrm{L}}\right)+\sigma_{\mathrm{ov}}
\tag{91}
$$

and for the vanishing lateral component

$$
0=-p+\frac{\mu_{\mathrm{eq}}}{\lambda_{0}}+\mu_{\mathrm{eq}}\left(-\frac{\varepsilon_{\mathrm{L}}}{2 \lambda_{0}}-\frac{\varepsilon_{\mathrm{L}}}{2 \lambda_{0}}\right)-\frac{1}{2} \sigma_{\mathrm{ov}},
\tag{92}
$$

leading to

$$
\sigma=\mu_{\mathrm{eq}}\left(\lambda_{0}^{2}-\frac{1}{\lambda_{0}}\right)+\mu_{\mathrm{eq}}\left(2 \lambda_{0}^{2}+\frac{1}{\lambda_{0}}\right) \varepsilon_{\mathrm{L}}+\frac{3}{2} \sigma_{\mathrm{ov}}
\tag{93}
$$

after eliminating the pressure $p$. The stress tensor $\mathbf{T}_{R 0}$ of the first Piola Kirchhoff type relates the current force to the area of the statically pre-deformed specimen and acts on the pre-deformed configuration. It can be calculated by

$$
\mathbf{T}_{R 0}=\mathbf{S f}^{T-1} \approx \mathbf{S}\left(\mathbf{1}-\mathbf{h}^{T}\right)
\tag{94}
$$

or by $\sigma_{R 0}=\sigma\left(1-\varepsilon_{\mathrm{L}}\right)$ in the uniaxial form. Omitting higher order terms in $\varepsilon_{\mathrm{L}}$ leads to

$$
\sigma_{R 0}=\mu_{\mathrm{eq}}\left(\lambda_{0}^{2}-\frac{1}{\lambda_{0}}\right)+\mu_{\mathrm{eq}}\left(\lambda_{0}^{2}+\frac{2}{\lambda_{0}}\right) \varepsilon_{\mathrm{L}}+\frac{3}{2} \sigma_{\mathrm{ov}}.
\tag{95}
$$

Inserting the special representations of $\mathbf{E}_{\mathrm{L}}$ and $\mathbf{S}_{\mathrm{ov}}$ specified by Eqs. (88) and (89) into Eqs. (79) to (81) we obtain the one-dimensional formulation of the model for the overstress:

$$
\frac{\mathrm{d}^{\beta} \sigma_{\mathrm{ov}}}{\mathrm{d} z^{\beta}}=2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \varepsilon_{\mathrm{L}}}{\mathrm{d} z^{\beta}}-\frac{1}{\zeta^{\beta}} \sigma_{\mathrm{ov}},
\tag{96}
$$

$$
\dot{q}(t)=\frac{1}{\lambda}\left(\tau^{\alpha}\left|\frac{\mathrm{d}^{\alpha}}{\mathrm{d} t^{\alpha}} \varepsilon_{\mathrm{L}}(t)\right|-q\right),
\tag{97}
$$

$$
\dot{z}(t)=1+b q(t) \text { with } z(0)=0.
\tag{98}
$$

Looking at Eq. (95), we see that the total stress is the sum of three terms. The first term is the static stress, which is determined by the equilibrium stress strain relation evaluated at the pre-deformation stage; the second term is determined by the local tangent modulus of the equilibrium stress and the third term, the nonlinear rate-dependent overstress, is defined by Eqs. (96) – (98).

Our next task is to evaluate the above equations for stationary sinusoidal excitations in the form of

$$
\varepsilon_{\mathrm{L}}(t)=\Delta \varepsilon \sin (\omega t).
\tag{99}
$$

Since we need the fractional derivatives of the sine and cosine functions in the stationary state, we take the formulae (12) and (39) from Lion et al. (2003) into account:

$$
\frac{\mathrm{d}^{\alpha}}{\mathrm{d} t^{\alpha}} \sin (\omega t)=\omega^{\alpha} \sin \left(\omega t+\frac{\alpha \pi}{2}\right)
\tag{100}
$$

$$
\frac{\mathrm{d}^{\alpha}}{\mathrm{d} t^{\alpha}} \cos (\omega t)=\omega^{\alpha} \cos \left(\omega t+\frac{\alpha \pi}{2}\right)
\tag{101}
$$

To derive the stationary solution of Eq. (97) belonging to the input specified by Eq. (99), we consider the initial condition $q(0)=0$ and first calculate the general solution of Eq. (97),

$$
q(t)=\frac{\tau^{\alpha}}{\lambda} \int_{0}^{t} \mathrm{e}^{-\frac{t-s}{\lambda}}\left|\frac{\mathrm{d}^{\alpha} \varepsilon_{\mathrm{L}}}{\mathrm{d} s^{\alpha}}(s)\right| \mathrm{d} s.
\tag{102}
$$

Due to the periodicity of $\varepsilon_{\mathrm{L}}(t)$ and its fractional derivative, the stationary solution of Eq. (97) or (102) is also periodic in time, i.e. we have $q(t)=q(t+2 \pi / \omega)$. This leads to

$$
q(t)=q\left(t+\frac{2 \pi}{\omega}\right)=\frac{\tau^{\alpha}}{\lambda} \int_{0}^{t+2 \pi / \omega} \mathrm{e}^{-\frac{t+2 \pi / \omega-s}{\lambda}}\left|\frac{\mathrm{d}^{\alpha} \varepsilon_{\mathrm{L}}}{\mathrm{d} s^{\alpha}}(s)\right| \mathrm{d} s
\tag{103}
$$

and after splitting the integral into the sum of two terms to

$$
q(t)=\frac{1}{e^{\frac{2 \pi}{\omega \lambda}}-1} \frac{\tau^{\alpha}}{\lambda} \int_{t}^{t+2 \pi / \omega} \mathrm{e}^{-\frac{t-s}{\lambda}}\left|\frac{\mathrm{d}^{\alpha} \varepsilon_{\mathrm{L}}}{\mathrm{d} s^{\alpha}}(s)\right| \mathrm{d} s.
\tag{104}
$$

Assuming the typical duration $\lambda$ of structural relaxation effects in the material to be essentially larger than the typical period $2 \pi / \omega$ of the strain excitation, we have $2 \pi / \lambda \omega<<1$. In this case the exponential function in the integrand of Eq. (104) can be approximated by 1 and the term $\mathrm{e}^{2 \pi / \lambda \omega}$ by $1+2 \pi / \lambda \omega$ leading to

$$
q(t)=\frac{\omega \tau^{\alpha}}{2 \pi} \int_{0}^{2 \pi / \omega}\left|\frac{\mathrm{d}^{\alpha} \varepsilon_{\mathrm{L}}}{\mathrm{d} s^{\alpha}}(s)\right| \mathrm{d} s.
\tag{105}
$$

Inserting the fractional derivative of $\varepsilon_{\mathrm{L}}(t)$ specified in Eqs. (99) and (100), we obtain

$$
q(t)=\Delta \varepsilon(\omega \tau)^{\alpha} \frac{\omega}{2 \pi} \int_{t}^{t+2 \pi / \omega}\left|\sin \left(\omega s+\frac{\alpha \pi}{2}\right)\right| \mathrm{d} s=\frac{\Delta \varepsilon(\omega \tau)^{\alpha}}{2 \pi} \int_{0}^{2 \pi}|\sin (x)| \mathrm{d} x
\tag{106}
$$

or finally (cf. Lion et al., 2003)

$$
q(t)=\frac{2}{\pi} \Delta \varepsilon(\omega \tau)^{\alpha}.
\tag{107}
$$

As we can see, the structural variable $q(t)$, which is a phenomenological measure for deformation-induced changes in the microstructure, becomes constant under harmonic strain excitations. It is a linear function of the amplitude $\Delta \varepsilon$ and a power function of the angular frequency $\omega$ of excitation. For the rate of the intrinsic time Eq. (98), we then find

$$
\dot{z}(t)=1+b \frac{2}{\pi} \Delta \varepsilon(\omega \tau)^{\alpha}
\tag{108}
$$

or, after integration,

$$
z(t)=\left(1+b \frac{2}{\pi} \Delta \varepsilon(\omega \tau)^{\alpha}\right) t. \tag{109}
$$

The higher both the frequency and the amplitude of the incremental deformation, the faster is the temporal evolution of the intrinsic time $z(t)$. We see that the temporal evolution of the intrinsic time depends nonlinearly on the frequency, which is determined by the fractional time derivative occurring in the evolution law Eq. (80) or (97). Detailed parameter investigations motivating the fractional time rate in Eq. (80) have been carried out by Lion et al. (2003).

Since $z(t)$ is proportional to the physical time under stationary conditions, Eq. (109) is fairly similar to the well-known time/temperature shift principle which is frequently applied in the theory of linear thermoviscoelasticity. In this theory one would have $z(t)=a(\theta) t$ where $\theta$ is the thermodynamic temperature, but here we have

$$
z(t)=a(\omega, \Delta \varepsilon) t. \tag{110}
$$

In order to judge the ability of the asymptotic formula Eq. (107) to approximate the time-dependent solution for times of sufficient length, numerical simulations with $\lambda=1 s, \alpha=0.5$ and different frequencies were carried out. To this end, the fractional derivative of the dynamic strain specified in Eq. (99), was inserted into Eq. (97) and a numerical integration was carried out. Fig. 5 compares the curves determined by numerical integration with the horizontal lines supplied by the asymptotic formula. As we can see, the approximation is fairly accurate for sufficiently long times. A section of the 10 Hz curve is shown in Fig. 6.

For the purpose of reformulating the fractional differential equation for the overstress for the case under discussion of stationary harmonic processes, we consider the definition

$$
\frac{\mathrm{d}^{\beta}}{\mathrm{d} z^{\beta}} f(z)=\frac{1}{\Gamma(1-\beta)} \int_{0}^{z} \frac{1}{(z-\xi)^{\beta}} \frac{\mathrm{d}}{\mathrm{d} \xi} f(\xi) \mathrm{d} \xi, \tag{111}
$$

of the fractional derivative, substitute $z=a(\omega, \Delta \varepsilon) t, \xi=a(\omega, \Delta \varepsilon) s$ and take the chain rule $\mathrm{d} f / \mathrm{d} \xi=1 / a(\omega, \Delta \varepsilon) \mathrm{d} f / \mathrm{d} s$ into account. A simple calculation leads to the fractional chain rule

$$
\frac{\mathrm{d}^{\beta}}{\mathrm{d} z^{\beta}} f(z)=\frac{1}{a(\omega, \Delta \varepsilon)^{\beta}} \frac{\mathrm{d}^{\beta}}{\mathrm{d} t^{\beta}} f(t) \tag{112}
$$

and with the differential equation Eq. (96) to

![](./images/812370043483455489_7.jpg)

Fig. 5. Fig. 5. Behaviour of the structural variable for different frequencies: $\lambda = 1s$, $\alpha = 0.5$.

$$
\frac{\mathrm{d}^{\beta} \sigma_{\mathrm{ov}}}{\mathrm{d} t^{\beta}}=2 \mu_{\mathrm{ov}} \frac{\mathrm{d}^{\beta} \varepsilon_{\mathrm{L}}}{\mathrm{d} t^{\beta}}-\left(\frac{a(\omega, \Delta \varepsilon)}{\zeta}\right)^{\beta} \sigma_{\mathrm{ov}}.
\tag{113}
$$

In contrast to Eq. (96), this relation is valid for stationary harmonic processes only. It corresponds to a linear fractional Maxwell element with a relaxation time depending on both the frequency and the amplitude, i.e. $\hat{\zeta}=\zeta / a(\omega, \Delta \varepsilon)$. Fractional viscoelasticity models with constant relaxation times have been investigated, for example, by Metzeler and Nonnenmacher (2003), Lion (2001) or originally by Caputo and Mainardi (1971).

To calculate the dynamic stress response, we insert the fractional derivative of the strain process specified by Eq. (99) into Eq. (113), assume

$$
\sigma_{\mathrm{ov}}(t)=\Delta \varepsilon(A \sin (\omega t)+B \cos (\omega t)),
\tag{114}
$$

with the unknown amplitude and frequency-dependent functions $A$ and $B$, calculate

$$
\frac{\mathrm{d}^{\beta} \sigma_{\mathrm{ov}}}{\mathrm{d} t^{\beta}}=\Delta \varepsilon \omega^{\beta}\left(A \sin \left(\omega t+\beta \frac{\pi}{2}\right)+B \cos \left(\omega t+\beta \frac{\pi}{2}\right)\right)
\tag{115}
$$

and consider the theorems of addition,

![](./images/812370043483455489_8.jpg)

Fig. 6. Enlargement of a section of the 10 Hz curve of Fig. 5.

$$
\sin\left(\omega t+\beta\frac{\pi}{2}\right)=\sin(\omega t)\cos\left(\beta\frac{\pi}{2}\right)+\cos(\omega t)\sin\left(\beta\frac{\pi}{2}\right), \tag{116}
$$

$$
\cos\left(\omega t+\beta\frac{\pi}{2}\right)=\cos(\omega t)\cos\left(\beta\frac{\pi}{2}\right)-\sin(\omega t)\sin\left(\beta\frac{\pi}{2}\right). \tag{117}
$$

Inserting Eq. (115) into Eq. (113), considering Eqs. (116) and (117) and rearranging the terms leads to the following equation, which has to be satisfied for any time $t$:

$$
\begin{aligned}
&\left\{\left(1+\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)\right) A-\left(\frac{\omega \zeta}{a}\right)^{\beta} \sin \left(\beta \frac{\pi}{2}\right) B-2 \mu_{\mathrm{ov}}\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)\right\} \sin (\omega t)+ \\
&\left\{\left(1+\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)\right) B+\left(\frac{\omega \zeta}{a}\right)^{\beta} \sin \left(\beta \frac{\pi}{2}\right) A-2 \mu_{\mathrm{ov}}\left(\frac{\omega \zeta}{a}\right)^{\beta} \sin \left(\beta \frac{\pi}{2}\right)\right\} \cos (\omega t)=0
\end{aligned}
$$

Taking the linear independence of the harmonic functions $\sin(\omega t)$ and $\cos(\omega t)$ into account leads to a system of two linear algebraic equations which were used to determine the unknown functions $A$ and $B$:

$$
A=2 \mu_{\mathrm{ov}} \frac{\left(\frac{\omega \zeta}{a}\right)^{2 \beta}+\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)}{1+2\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)+\left(\frac{\omega \zeta}{a}\right)^{2 \beta}}
\tag{118}
$$

$$
B=2 \mu_{\mathrm{ov}} \frac{\left(\frac{\omega \zeta}{a}\right)^{\beta} \sin \left(\beta \frac{\pi}{2}\right)}{1+2\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)+\left(\frac{\omega \zeta}{a}\right)^{2 \beta}}
\tag{119}
$$

In order to determine the total stress acting on the pre-deformed configuration, we consider Eqs. (95) and (114) and obtain

$$
\sigma_{R 0}(t)=\mu_{\mathrm{eq}}\left(\lambda_{0}^{2}-\frac{1}{\lambda_{0}}\right)+G^{\prime}\left(\lambda_{0}, \omega, \Delta \varepsilon\right) \Delta \varepsilon \sin (\omega t)+G^{\prime \prime}(\omega, \Delta \varepsilon) \Delta \varepsilon \cos (\omega t)
\tag{120}
$$

with the pre-deformation, frequency and amplitude-dependent storage and dissipation moduli

$$
G^{\prime}\left(\lambda_{0}, \omega, \Delta \varepsilon\right)=\mu_{\mathrm{eq}}\left(\lambda_{0}^{2}+\frac{2}{\lambda_{0}}\right)+3 \mu_{\mathrm{ov}} \frac{\left(\frac{\omega \zeta}{a}\right)^{2 \beta}+\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)}{1+2\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)+\left(\frac{\omega \zeta}{a}\right)^{2 \beta}}
\tag{121}
$$

and

$$
G^{\prime \prime}(\omega, \Delta \varepsilon)=3 \mu_{\mathrm{ov}} \frac{\left(\frac{\omega \zeta}{a}\right)^{\beta} \sin \left(\beta \frac{\pi}{2}\right)}{1+2\left(\frac{\omega \zeta}{a}\right)^{\beta} \cos \left(\beta \frac{\pi}{2}\right)+\left(\frac{\omega \zeta}{a}\right)^{2 \beta}}
\tag{122}
$$

and the shifting function

$$
a(\omega, \Delta \varepsilon)=1+b \frac{2}{\pi} \Delta \varepsilon(\omega \tau)^{\alpha}.
\tag{123}
$$

Looking at Eq. (120) we see that the total stress is the sum of the static stress depending only on the static pre-deformation $\lambda_{0}$ and the dynamic stress depending on pre-deformation, amplitude and frequency.

Eqs. (121) – (123) describing the dependence of both the storage and the dissipa- tion modulus on the process parameters look fairly similar to the corresponding formulae known from linear viscoelasticity of thermorheological simple materials. In this theory the function $a(\ldots)$ would depend on temperature $\theta$ but not on

frequency; the functional form of $a(\theta) \geqslant 0$ can be arbitrary. In the theory developed in this essay, the moduli depend on frequency and amplitude but in a special form.

To sketch a consequence of the classical theory of thermoviscoelasticity, we assume the dynamic moduli $G'(\omega, \theta_0)$ and $G''(\omega, \theta_0)$ to be known as functions of frequency $\omega$ at an arbitrary reference temperature $\theta_0$. The theory of thermo- rheological simple materials states that the moduli at any other temperature $\theta$ can be written in the form of

$$
G^{\prime}(\omega, \theta)=G^{\prime}(\omega / a(\theta), \theta_{0})=G^{\prime}(\Omega, \theta_{0})
\tag{124}
$$

and

$$
G^{\prime \prime}(\omega, \theta)=G^{\prime \prime}(\omega / a(\theta), \theta_{0})=G^{\prime \prime}(\Omega, \theta_{0}),
\tag{125}
$$

where the normalised shift function has the property $a(\theta_0)=1$; $\Omega$ is the reduced frequency. Reformulating the moduli leads to

$$
\begin{aligned}
G^{\prime}(\omega / a(\theta), \theta_{0}) & =G^{\prime}(10^{\log (\omega)-\log (a(\theta))}, \theta_{0})=\hat{G}^{\prime}(\log (\omega)-\log (a(\theta)), \theta_{0}) \\
& =\tilde{G}^{\prime}(\log (\Omega), \theta_{0})
\end{aligned}
\tag{126}
$$

and

$$
\begin{aligned}
G^{\prime \prime}(\omega / a(\theta), \theta_{0}) & =G^{\prime \prime}(10^{\log (\omega)-\log (a(\theta))}, \theta_{0})=\hat{G}^{\prime \prime}(\log (\omega)-\log (a(\theta)), \theta_{0}) \\
& =\tilde{G}^{\prime \prime}(\log (\Omega), \theta_{0}).
\end{aligned}
\tag{127}
$$

As we see, on a logarithmically divided frequency axis the curves are shifted in horizontal direction depending on the temperature. If, for example, the moduli are measured in a given frequency range under different constant temperatures $\theta_i$, we plot the curves in a diagram with a logarithmically scaled frequency axis, select a reference curve (reference temperature $\theta_0$) and shift the remaining curves in horizontal direction just until one unique and more or less smooth master curve is obtained. This is the dynamic modulus belonging to the reference temperature $\theta_0$ and to a much larger frequency range.

As demonstrated by Eq. (123), the reduced frequency $\Omega$ has the form $\Omega=\omega / a(\omega, \Delta \varepsilon)$ in the theory developed in this paper. To attempt to transfer the idea of thermorheological simple materials to the amplitude dependence, we assume the dynamic moduli belonging to different strain amplitudes $\Delta \varepsilon_i$ to be known as functions of $\omega$ in a given range. Then we plot the curves in a diagram with a logarithmically divided frequency axis. Due to the combined frequency and amplitude dependence of the shifting function $a(\omega, \Delta \varepsilon)$ the moduli curves belonging to different strain amplitudes are not only shifted in horizontal direction but also deformed. The reason for this deformation is the frequency dependence of $a(\omega, \Delta \varepsilon)$.

As we explained above, there are common properties but also differences between the approach of thermorheologically simple materials to describe the temperature and frequency dependence and the proposed constitutive theory of finite, nonlinear viscoelasticity to represent the amplitude and frequency dependence.

## 7. Simulations

To demonstrate the ability of the developed constitutive theory to represent the material behaviour observed, the parameters of the model were identified using a stochastic Monte Carlo method. To this end, both a maximum value $p_{\text{max}}$ and a minimum value $p_{\text{min}}$ of each material parameter $(\mu_{\text{eq}}, \mu_{\text{ov}}, \zeta, \tau, \alpha, \beta, b)$ was estimated and prescribed during the identification procedure. Then we chose a diagonal matrix $\mathbf{r}$ containing a set of arbitrary random numbers $0 \leqslant r_{i} \leqslant 1$ with $i=1, \ldots 7$ and generated stochastically distributed parameters using

$$
\overline{\mathbf{p}}=\mathbf{r} \mathbf{p}_{\min }+(\mathbf{1}-\mathbf{r}) \overline{\mathbf{p}}_{\max }
$$

or, equivalently,

$$
p_{i}=r_{i}+\left(1-r_{i}\right) p_{\text {maxi }}, \quad i=1, \ldots 7 .
$$

The column vectors $\overline{\mathbf{p}}_{\text{max}}$, $\overline{\mathbf{p}}_{\text{min}}$ and $\overline{\mathbf{p}}$ contain the maximum, minimum and stochastic values of the parameters. The differences between the experimental data of Figs. 2 and 3 and the simulations based on Eqs. (121)-(123) and (128) were measured using a weighted, quadratic error norm. Since the magnitude of the dissipation modulus is about 1/3 of that of the storage modulus, the differences between the simulated and measured dissipation moduli were multiplied by a factor of 3. Using this method, several ten thousand parameter sets were tested and evaluated.

Nevertheless, this procedure is very fast because the parameters occur in algebraic equations which can be fitted to the measured data; no numerical integration is necessary. The parameters belonging to the smallest value of the error norm are listed in Table 1. The corresponding model simulations are shown in Figs. 7 and 8.

Comparing the experimental data of the storage modulus shown in Fig. 2 with the corresponding simulations in Fig. 7, we see that the order of magnitude and the monotonic decrease are qualitatively and quantitatively reproduced as a function of the strain amplitude. The same statement holds for the representation of the dissipation modulus, shown in Figs. 3 and 8, but the frequency dependence is underestimated.

Table 1
Identified material parameters

<table>
<thead>
<tr>
<th>$\mu_{eq}$ (MPa)</th>
<th>$\mu_{ov}$ (MPa)</th>
<th>$\zeta$ (s)</th>
<th>$\tau$ (s)</th>
<th>$\alpha$ ($-$)</th>
<th>$\beta$ ($-$)</th>
<th>$b$ ($-$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.86</td>
<td>10.24</td>
<td>421</td>
<td>1.0</td>
<td>0.449</td>
<td>0.494</td>
<td>51078</td>
</tr>
</tbody>
</table>

![](./images/812370043483455489_9.jpg)

Fig. 7. Simulated data of storage modulus.

![](./images/812370043483455489_10.jpg)

Fig. 8. Simulated data of the dissipation modulus.

A proposal to improve the representation of dissipation modulus is to consider several nonlinear Maxwell elements in the form of Eq. (52) in parallel. Each Maxwell element can be formulated, in principle, with respect to its own intrinsic time scale $z_{i}(t)$. Then there are more material constants available to fit the experimental data.

The second proposal is related to the assumed mathematical form of the evolution law of Eq. (50). In a further project, this evolution law could be modified.

As we know, the Kraus model in the form of Eqs. (8) and (9) can also match the behaviour of dynamic moduli as a function of strain amplitude, but only at a fixed frequency. For a different frequency one has to re-identify the whole set of material constants and for each frequency one obtains, in general, different values.

Compared to this, the proposed theory represents the frequency and amplitude dependence of moduli in parallel and allows numerical calculations in the time domain for arbitrary deformation processes. The representation of both the frequency and the amplitude dependence is possible with only six parameters, which is the same number as contained in the Kraus model.

## 8. Conclusions

We have developed a three-dimensional, finite strain constitutive theory leading to expressions relating the storage and dissipation moduli to the pre-deformation, the frequency of excitation and the amplitude, thus describing the Payne effect using six parameters. As opposed to common approaches proposed in literature, our theory is formulated in the time domain. It can relate the stress to any strain history and is not restricted to the steady-state response to a deformation that varies sinusoidally with time. The corresponding relations for the storage and loss moduli have been calculated analytically. As we have shown, the moduli depend on a reduced frequency $\Omega$, which is a function of the strain amplitude and the angular frequency of excitation. Since the shift function $a(\omega, \Delta \varepsilon)$ depends on two variables, the curves of dynamic moduli, plotted on a logarithmically divided frequency axis, are not only shifted if $\Delta \varepsilon$ changes but also deformed.

The fundamental ingredients of the devised theory are a constitutive model of finite strain viscoelasticity and an evolution equation for an internal variable, which is a phenomenological measure for the current state of the material's microstructure. It determines the temporal behaviour of an intrinsic time variable. Motivated by experience in material modelling, both ingredients make use of fractional time rates. The finite strain model is based on the general concept proposed by Haupt and Lion (2002) and is compatible with the second law of thermodynamics. To compare the theory with measured data, we fitted the expressions of dynamic moduli to the test data of carbon black-filled rubber with a filler content of 60 phr. As we demon- strated, the model describes the general trend of the amplitude and frequency dependence qualitatively and quantitatively; the frequency was varied between 10 and 60 Hz and the strain amplitude between 0.1 and 5%.

Since fractional time derivatives are functionals depending on the whole process history, the numerical integration of constitutive models incorporating fractional derivatives is fairly time-consuming. Since the relaxation spectra of the fractional Maxwell element or the Mittag Leffler function are known, it is possible to apply the approximation method proposed and applied by Haupt et al. (2000). In this case, fractional differential equations can be approximated by a system of ordinary

differential equations of the first order. Its number depends on the frequency range of interest and the desired accuracy. This method will be applied in the future.

## References

Besdo, D., Ihlemann, J., 2003a. Properties of rubberlike materials under large deformations by self- organizing linkage patterns. International Journal of Plasticity 19, 1001-1018.

Besdo, D., Ihlemann, J., 2003b. A phenomenological constitutive model for rubberlike materials and its numerical applications. International Journal of Plasticity 19, 1019-1036.

Besdo, D., Ihlemann, J., 1996. Zur Modellierung des Stoffverhaltens von Elastomeren. Kautschuk Gummi Kunststoffe 49, 495-503.

Burg, C., Haf, H., Wille, F., 1985. Höhere Mathematik für Ingenieure, Vol. 1 (Analysis). Teubner Publications (in German).

Caputo, M., Mainardi, F., 1971. Linear models in anelastic solids. Riv. Il Nuovo Cimento (Sere. II) 1, 161-198.

Chazeau, L., Brown, J.D., Yano, L.C., Sternstein, S.S., 2000. Modulus recovery kinetics other insights into the Payne effect for filled elastomers. Polym. Comp. 21, 202-222.

Drozdov, A.D., Dorfmann, L., 2003. A micromechanical model for the response of filled elastomers at finite strains. International Journal of Plasticity 19, 1037-1067.

Drozdov, A.D., 1998. Viscoelastic Structures. Acta Mechanica.

Drozdov, A.D., 1997. Fractional differential models in finite viscoelasticity. Acta Mechanica 124, 155-180.

Hackbusch, W., 1997. Integralgleichungen: Theorie und Numerik. Teubner publications, Germany.

Haupt, P., 2002. Continuum mechanics and theory of materials, 2nd ed. Springer Publications.

Haupt, P., Lion, A., 2002. On finite linear viscoelasticity of incompressible isotropic materials. Acta Mechanica 159, 87-124.

Haupt, P., Lion, A., Backhaus, E., 2000. On the dynamic behaviour of polymers under finite strains: constitutive modelling and identification of parameters. International Journal of Solids and Structures 37, 3633-3646.

Heinrich, G., Vilgis, T.A., 1995. Effect of filler on the dynamic mechanical properties of crosslinked polymer solids. Macromol. Symp. 93, 253-260.

Huber, G., Vilgis, G.A., Heinrich, G., 1996. Universal properties in the dynamical deformation of filled rubbers. J. Phys. Condens. Matter. 8, L409-L412.

Huber, G., 1997. Universelle Eigenschaften gefüllter Elastomere. Doctoral Thesis, University of Mainz, Germany (in German).

Khan, A.S., Lopez-Pamies, O., 2002. Time and temperature-dependent response and relaxation of a soft polymer. International Journal of Plasticity 18, 1359-1372.

Khan, A.S., Zhang, H., 2001. Finite deformation of a polymer: experiments and modelling. International Journal of Plasticity 17, 1167-1188.

Koeller, R.C., 1984. Applications of fractional calculus to the theory of viscoelasticity. Journal of Applied Mechanics 51, 299-307.

Krempl, E., Bordonaro, C.M., 1998. Non-proportional loading of nylon 66 at room temperature. Inter- national Journal of Plasticity 14, 245-258.

Laiarinandrasana, L., Piques, R., Robisson, A., 2003. Visco-hyperelastic model with internal state variable coupled with discontinuous damage concept under total Lagrangian formulation. International Journal of Plasticity 19, 977-1000.

Lion, A., Kardelky, C., Haupt, P., 2003. On the frequency and amplitude dependence of the Payne effect: theory and experiments. Rubber Chemistry and Technology 76, 533-547.

Lion, A., 2001. Thermomechanically consistent formulations of the standard linear solid using fractional derivatives. Archives of Mechanics 53, 253-273.

Lion, A., 2000. Thermomechanik von Elastomeren: Experimente und Materialtheorie. Habilitation Thesis. Department of Mechanical Engineering, University of Kassel (in German).

Lion, A., 1999. Strain-dependent dynamic properties of filled rubber: a nonlinear viscoelastic approach based on structural variables. Rubber Chemistry and Technology 72, 410-428.

Lion, A., 1998. Thixotropic behaviour of rubber under dynamic loading histories: experiments and theory. Journal of the Mechanics and Physics of Solids 46, 895-930.

Lion, A., 1997. On the large deformation behaviour of reinforced rubber at different temperatures. Journal of the Mechanics and Physics of Solids 45, 1805-1834.

Lion, A., 1996. A constitutive model for carbon black-filled rubber: experimental investigations and mathematical modelling. Continuum Mechanics and Thermodynamics 8, 153-169.

Mainardi, F., 1997. Fractional calculus: some basic problems in continuum and statistical physics. Fractals and Fractional Calculus in Continuum Mechanics. CISM Courses and Lectures, Vol. 378, Springer Ltd., pp. 291-341.

Metzeler, R., Nonnenmacher, T.F., 2003. Fractional relaxation processes and fractional rheological models for the description of a class of viscoelastic materials. International Journal of Plasticity 19, 940-941.

Metzeler, R., Schick, W., Kilian, H.G., Nonnenmacher, T.F., 1995. Relaxation in filled polymers: a fractional calculus approach. J. Chem. Phys. 103, 7180-7186.

Miehe, C., Keck, J., 2000. Superimposed finite elastic-viscoelastic-plastoelastic stress response with damage in filled rubbery polymers: experiments, modelling and algorithmic implementation. Journal of the Mechanics and Physics of Solids 48, 323-365.

Oldham, K.B., Spanier, J., 1974. The Fractional Calculus: Theory and Applications of Differentiation and Integration to Arbitrary Order. Academic Press, New York and London.

Payne, A.R., 1960. A note on the existence of a yield point on the dynamic modulus of loaded vulcani- sates. Journal of Applied Polymer Science 3, 127.

Reese, S., 2003. A micromechanically motivated material model for the thermo-viscoelastic material behaviour of rubberlike polymers. International Journal of Plasticity 19, 909-940.

Reinhardt, G., 2001. Experimental investigations of rubber under dynamic loads. Diploma thesis, University of Kassel, Germany, Institute of Mechanics, Department of Mechanical Engineering (in German).

Roland, C., 1990. Dynamic mechanical behaviour of filled rubber at small strains. Journal of Rheology 34, 25-34.

Schwarzl, F.R., 1990. Polymermechanik. Springer Publications.

Ulmer, J.D., 1996. Strain dependence of dynamic mechanical properties of carbon black-filled rubber compounds. Rubber Chemistry and Technology 69, 15-47.

Valanis, K.C., 1971. A theory of viscoplasticity without a yield surface. Arch. Mech. 23, 517-533.

Vieweg, S., Unger, R., Schröter, K., Donth, E., Heinrich, G., 1995. Frequency and temperature dependence of the small strain behaviour of carbon black-filled vulcanisates. Polym. Networks Blends 4, 199-204.

Wang, M.J., Patterson, W.J., Ouyang, G.B., 1996. Paper No. 33 presented at the spring ACS Rubber Division Meeting, Montreal, 5-8 May 1996 (abstract in Rubber Chemistry and Technology I, 69, 15).