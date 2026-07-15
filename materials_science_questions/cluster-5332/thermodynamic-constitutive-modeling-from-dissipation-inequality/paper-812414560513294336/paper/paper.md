# A PRIORI STABILITY ESTIMATES AND UNCONDITIONALLY STABLE PRODUCT FORMULA ALGORITHMS FOR NONLINEAR COUPLED THERMOPLASTICITY

F. ARMERO and J. C. SIMO

Stanford University

Abstract-This article describes new a priori stability estimates for the full nonlinear system of coupled thermoplasticity at finite strains and presents a fractional step method leading to a new class of unconditionally stable staggered algorithms. These results are shown to hold for general models of multiplicative plasticity that include, as a particular case, the single-crystal model. The proposed product formula algorithm is designed via an entropy based operator split that yields one of the first known staggered algorithms that retains the property of nonlinear unconditional stability. The scheme employs an isentropic step, in which the total entropy is held constant, followed by a heat conduction step (with nonlinear source) at fixed configuration. The nonlinear stability analysis shows that the proposed staggered scheme inherits the a priori energy estimate for the continuum problem, regardless of the size of the time-step. In sharp contrast with these results, it is shown that widely used staggered methods employing an isothermal step followed by a heat conduction problem can be at most only conditionally stable. The excellent performance of the methodology is illustrated in representative numerical simulations.

## I. INTRODUCTION

Coupled thermomechanical problems typically involve different time scales associated with the thermal and mechanical fields. It is widely accepted that an effective numerical integration scheme for the full coupled thermomechanical problem should take advantage of these different time scales. Considerations of this type motivate the so-called staggered algorithms, whereby the problem is partitioned into several smaller sub-problems that are solved sequentially. This technique is especially attractive because the large and generally nonsymmetric system that results from a simultaneous solution scheme is replaced by much smaller, typically symmetric, subsystems. For thermomechanical problems the standard approach exploits a natural partitioning of the problem in a mechanical phase, with the temperature held constant, followed by a thermal phase at fixed configuration. In the engineering literature, approaches of this type go back to the work of ARGYRIS and DOLTSINIS [1981] and others; see the review articles of PARK and FELIPPA [1983] and DOLTSINIS [1990]. Although computationally appealing, the well-known restriction to conditional stability is the crucial limitation of these approaches, which becomes of special significance for strongly coupled problems. Stabilization techniques designed to remove the restriction of conditional stability have been devised by a number of authors; e.g. the early augmentation schemes of PARK et al. [1977], the iterative scheme of ARGYRIS and DOLTSINIS [1981], and the more recent augmentation strategy of FARHAT, PARK, and DUBOIS-PELEGRIN [1991], among others. These techniques, however, are typically restricted to the linear problem and, even in this situation, they often become intricate and computationally expensive.

As noted in SIMO and MIEHE [1992], the class of staggered schemes outlined above can be interpreted as product formula algorithms arising from an operator split of the

problem of evolution into an isothermal step followed by a heat-conduction step at fixed configuration. We shall refer to this operator split simply as the *isothermal split*. The global staggered algorithm is therefore constructed in the spirit of classical fractional step methods (YANENKO [1971]). The recent analysis in ARMERO and SIMO [1992] shows that the isothermal split does not preserve the contractivity property of the coupled problem of (nonlinear) thermoelasticity. As a result, staggered schemes of this type can be at best only conditionally stable. The analysis provides explicit estimates for the critical time step leading to numerical instability and identifies an alternative operator split that renders unconditionally stable staggered algorithms. In this split, henceforth referred to as the *adiabatic split*, the problem is partitioned into an adiabatic mechanical phase in which the total entropy of the system is held constant, in place of the standard isothermal phase.

This article addresses the extension of these ideas to the full nonlinear system of coupled thermoplasticity at finite strains. A main goal is the design and analysis of fractional step methods that preserve all the computational advantages of conventional staggered schemes while retaining the property of unconditional stability. The proposed methodology is shown to be applicable to general models of multiplicative plasticity, described in the review article of AsARO [1983] and the more recent accounts in BOYCE, WEBBER, and PARKS [1989], HARREN [1991], and MORAN, ORTIZ, and SHIH [1992], amongst others. A key step in this development is the derivation of a new a priori energy estimate, valid for the aforementioned models, obtained by identifying a nonincreasing functional along the flow that generalizes to coupled nonlinear thermoplasticity the notion of canonical free energy in thermoelasticity; see ERICKSEN [1966]. This a priori estimate leads to a natural notion of nonlinear numerical stability that does not preclude interesting physical phenomena such as formation of shear bands in the presence of thermoplastic softening. Alternative notions of nonlinear stability, B-stability in particular (see HAIRER & WANNER [1991] for a precise discussion of this notion), are tailored to contractive problems of evolution and, therefore, not applicable to the problem at hand. A similar situation occurs in the classical model of (infinitesimal) perfect plasticity where contractivity of the plastic flow holds in stresses but not in displacements, thus allowing the appearance of discontinuities; see e.g. TEMAM [1985], SIMO [1991], DEMENGEL [1989], and references therein for a review of the mathematical status of this subject.

An outline of the remainder of this article is as follows. Section II summarizes the initial boundary value problem for coupled thermoplasticity and describes a general class of models of multiplicative plasticity at finite strains. A priori stability estimates are presented in Section III, and the formulation and stability analysis of the proposed *isentropic* operator split is described in Section IV. The accuracy, unconditional stability properties, and performance of the proposed methodology are illustrated in Section V in a number of representative numerical simulations. Conclusions are drawn in Section VI. For the convenience of the reader and to facilitate comparisons with alternative formulations found in the literature, a detailed step-by-step implementation of a specific model of thermoplasticity is given in an Appendix.

## II. THE COUPLED THERMOMECHANICAL PROBLEM

We describe below the system of quasilinear partial differential equations governing the evolution of the coupled thermoplastic problem. We adopt general constitutive equations that incorporate current models of finite strain plasticity and, in particular, micromechanically motivated models based on a multiplicative factorization of the

deformation gradient. The objective is to provide a general framework for the formu- lation of a priori stability estimates and unconditionally stable algorithms, described in the subsequent Sections, applicable to a wide range of formulations of plasticity. To clar- ify this setting, an outline is given of how representative models found in the literature fit within this general framework.

### II.1. General form of the local balance laws

The local system of partial differential equations governing the coupled thermome- chanical problem is defined by the momentum balance equation and the energy balance equation, restricted by the second law. This system is supplemented by suitable consti- tutive equations. To be explicit, let $\boldsymbol{\varphi}(\cdot, t)$ denote the motion in a time interval $[0, T]$ of a continuum body with reference configuration $\Omega$, material particles labeled by $\mathbf{X} \in \bar{\Omega}$, velocity field $\mathbf{V}:=\partial \boldsymbol{\varphi} / \partial t$, deformation gradient $\mathbf{F}:=D \boldsymbol{\varphi}$, and associated absolute temperature field $\theta(\cdot, t)$. The Lagrangian form of balance of momentum and reduced bal- ance of energy then take the form (see e.g. TRUESDELL & NOLL [1965]):

$$
\left.
\begin{aligned}
\dot{\boldsymbol{\varphi}} & =\mathbf{V} \\
\rho_{0} \dot{\mathbf{V}} & =\operatorname{DIV}[\mathbf{P}] \quad+\mathbf{B} \\
\theta \dot{\eta} & =-\operatorname{DIV}[\mathbf{Q}]+\mathfrak{D}_{\mathrm{int}}+R
\end{aligned}
\right\} \quad \text { in } \Omega \times[0, T], \tag{1a}
$$

where $\eta$ denotes the entropy, $\mathbf{P}$ the nominal stress tensor, $\mathbf{Q}$ the nominal heat flux, $\rho_{0}>0$ the reference density, and $\mathbf{B}$ and $R$ designate the body force and the heat sup- ply, respectively. In addition, $\mathfrak{D}_{\text {int }}$ denotes the internal dissipation given by

$$
\mathfrak{D}_{\mathrm{int}}:=\underbrace{\mathbf{P} \cdot \dot{\mathbf{F}}}_{\text {stress power }}+\underbrace{\theta \dot{\eta}}_{\text {thermal power }}-\underbrace{\dot{E}}_{\text {internal energy change }}, \tag{1b}
$$

where $E$ denotes the internal energy in the system, which is restricted by the Clausius- Duhem form of the second law (see TRUESDELL & NOLL [1965, p. 295]); i.e.,

$$
\mathfrak{D}:=\mathfrak{D}_{\mathrm{int}}+\mathfrak{D}_{\mathrm{con}} \geq 0 \quad \text { in } \Omega \times[0, T], \quad \text { where } \mathfrak{D}_{\mathrm{con}}:=-\frac{1}{\theta} \operatorname{GRAD}[\theta] \cdot \mathbf{Q}. \tag{1c}
$$

$\mathfrak{D}_{\text {con }}$ is the dissipation due to heat conduction. Equations (1a,b) are supplemented by standard mechanical boundary conditions and initial conditions for the motion, the velocity field, and the absolute temperature. As in ERICKSEN [1966], for the stability analysis in Section III it proves critical to assume thermal boundary condition of the fol- lowing form

$$
\theta=\theta_{0} \text { (constant) } \quad \text { on } \partial \Omega \times[0, T]. \tag{2}
$$

The reference temperature value $\theta_{0}$ is often called the "environmental temperature" and interpreted as the temperature of the medium in which the motion of the solid takes place. It is emphasized that the preceding balance laws are completely general and hold independent of any assumptions related to the constitutive response of the material.

### II.2. General inelastic constitutive equations

We consider a generic constitutive framework in which the deformation $\boldsymbol{\varphi}(\cdot, t)$ is regarded as a map defining the macroscopic motion of a continuum, with microstructural properties described by an additional set of internal variables collectively denoted by $\mathbf{G}(\cdot, t)$. In the context of single-crystal metal plasticity, for instance, $\mathbf{G}$ is a measure of plastic flow induced by the motion of dislocations through the crystal lattice. This micromechanical interpretation is accomplished by assigning to $\mathbf{G}$ the meaning of a local 'plastic deformation gradient' in a multiplicative factorization of the total deformation; see e.g. Asaro [1983] or Boyce, Webber, and Parks [1989] for a detailed exposition of these ideas. The evolution of the microstructural variables $\mathbf{G}$ is typically described in current constitutive models via rate equations of the general form

$$
\dot{\mathbf{G}}=\hat{\mathbf{G}}_{\mathbf{F}}(\mathbf{P}, \mathbf{G}, \Theta) \quad \text { in } \Omega \times[0, T],
$$

where $\hat{\mathbf{G}}_{\mathbf{F}}$ is a prescribed function, possibly nonsmooth, which depends implicitly on $\mathbf{F}$ in order to ensure frame invariance. Generic constitutive equations for the internal energy and the heat flux take the functional form

$$
E=\hat{E}(\mathbf{F}, \mathbf{G}, \eta) \quad \text { and } \quad \mathbf{Q}=\hat{\mathbf{Q}}(\mathbf{F}, \mathbf{G}, \eta).
$$

A standard argument then yields the following constitutive equations for the nominal stress and the absolute temperature, together with the reduced version of the dissipation inequality:

$$
\mathbf{P}=\partial_{\mathbf{F}} \hat{E}, \quad \Theta=\partial_{\eta} \hat{E} \quad \text { and } \quad \mathfrak{D}_{\mathrm{int}}=-\partial_{\mathbf{G}} \hat{E} \cdot \dot{\mathbf{G}}.
$$

Observe that $\hat{\mathbf{G}}_{\mathbf{F}}$ must be such that $\mathfrak{D}_{\text {int }}$ defined by $(4 b)_{3}$ is compatible with the second law defined by inequality (1c).

The preceding framework includes the specific models of rate-independent multiplicative plasticity summarized below, as well as viscoplastic models considered by a number of authors in linearized stability analyses of the rate-dependent coupled thermomechanical problem; see e.g. Anand, Kim, and Shawki [1987] and the review in Shawki and Clifton [1989]. In particular, in the absence of microstructural variables, $\mathfrak{D}_{\text {int }}=0$ and one recovers the classical model of nonlinear thermoelasticity; see Truesdell and Noll [1965, Sec. 80].

### II.3. Representative inelastic models of multiplicative plasticity

Micromechanically based phenomenological models of finite strain plasticity adopt a local multiplicative factorization of the deformation gradient into elastic and plastic parts, introduced in a phenomenological context in Lee and Liu [1967] and Lee [1969], which regard the plastic part as a microstructural internal variable. Hardening mechanisms in the material taking place at the microlevel are characterized by an additional set of phenomenological internal variables collectively denoted here by $\xi_{\alpha}$; see Asaro [1983] for a micromechanical interpretation. In the thermomechanical theory, an additional part of the configurational entropy arises as a result of dislocation and lattice defect motion, see e.g. Cottrell [1967]. This additional part is characterized in Simo

and MIEHE [1992] by an additional internal variable, denoted by $\eta^{p}$, and motivates the following set of microstructural internal variables

$$
\mathbf{G}=\left\{\mathbf{F}^{p}, \xi_{\alpha}, \eta^{p}\right\} \quad \text { with } \quad \mathbf{F}=\mathbf{F}^{e} \mathbf{F}^{p} \quad \text { and } \quad \eta=\eta^{e}+\eta^{p}. \tag{5}
$$

In the single crystal model, the internal energy $\hat{E}$ depends on lattice distortion, which is characterized by the elastic part $\mathbf{F}^{e}$ of the deformation gradient, thus motivating the functional form:

$$
E=\hat{E}\left(\mathbf{C}^{e}, \eta^{e}\right)+\hat{H}\left(\xi_{\alpha}\right) \quad \text { where } \mathbf{C}^{e}=\mathbf{F}^{e T} \mathbf{F}^{e}. \tag{6}
$$

The dependence of $E$ on the deformation via $\mathbf{C}^{e}$ is used by a number of authors, MANDEL [1972, 1974] in particular, and occurs in the original work of LEE [1969]. The assumption that the thermoelastic and hardening contributions in (6) are uncoupled, although suggested by experimental results in ZDEBEL and LEHMANN [1987], is unnecessary and introduced here only for simplicity. The formulation of a model of plasticity incorporating the microstructural variables (5) and the internal energy (6) then proceeds as follows.

II.3.1. Constitutive relations. Let $\mathbf{S}$ denote the symmetric second Piola-Kirchhoff stress relative to the intermediate (local) configuration defined by $\mathbf{F}^{p}$. By specialization of the general constitutive relations (4) one obtains

$$
\mathbf{S}=2 \partial_{\mathbf{C}^{e}} \hat{E}, \quad \Theta=\partial_{\eta^{e}} \hat{E} \quad \text { and } \quad \mathfrak{D}_{\mathrm{int}}=-\partial_{\mathbf{F}^{p}} \hat{E} \cdot \dot{\mathbf{F}}^{p}-\partial_{\xi_{\alpha}} \hat{E} \dot{\xi}_{\alpha}-\partial_{\eta^{p}} \hat{E} \dot{\eta}. \tag{7}
$$

Note that $\mathbf{P}=\mathbf{F}^{e} \mathbf{S} \mathbf{F}^{p-T}$, a relation that follows from the multiplicative factorization $(5)_{2}$ and standard results in continuum mechanics (see e.g. TRUESDELL & NOLL [1965, p. 124]). For an internal energy defined by (6), a straightforward application of the chain rule yields the following result for the partial derivatives arising in the expression for the reduced dissipation:

$$
\partial_{\mathbf{F}^{p}} \hat{E}=-\mathbf{C}^{e} \mathbf{S} \mathbf{F}^{p-T}, \quad \partial_{\eta^{p}} \hat{E}=-\Theta \quad \text { and } \quad \partial_{\xi_{\alpha}} \hat{E}=:-\beta^{\alpha}. \tag{8}
$$

Here $\beta^{\alpha}$ is merely a convenient shorthand notation for $\partial_{\xi_{\alpha}} \hat{E}$, often referred to as the 'flux' conjugate to the affinity $\xi_{\alpha}$ in the context of (irreversible) thermodynamics with internal variables. Inserting relations (8) into $(7)_{3}$ specifies the internal dissipation as

$$
\mathfrak{D}_{\text {int }}=\underbrace{\left[\mathbf{C}^{e} \mathbf{S}\right] \cdot \mathbf{L}^{p}}_{\mathfrak{D}_{\text {mech }}^{p}}+\underbrace{\beta^{\alpha} \dot{\xi}_{\alpha}+\Theta \dot{\eta}^{p}}_{\mathfrak{D}_{\text {ther }}^{p}}, \quad \text { where } \mathbf{L}^{p}:=\dot{\mathbf{F}}^{p} \mathbf{F}^{p-1}. \tag{9}
$$

The first two terms in (9) appear in MANDEL [1972], see also ANAND [1985, eqn (23)]. Consistent with the interpretation assigned to $\eta^{p}$, an additional contribution to the internal dissipation arises in the presence of thermal effects given by $\mathfrak{D}_{\text {ther }}^{p}=\Theta \dot{\eta}^{p}$. The stress tensor $\boldsymbol{\Sigma}:=\left[\mathbf{C}^{e} \mathbf{S}\right]$ conjugate to the plastic rate of deformation $\mathbf{L}^{p}$ is generally nonsymmetric, although restricted by the symmetry condition $\mathbf{C}^{e-1} \boldsymbol{\Sigma}=\boldsymbol{\Sigma}^{T} \mathbf{C}^{e-1}$, and first appears in MANDEL [1972] who refers to $\mathbf{L}^{p}$ as the plastic distortion rate.

### II.3.2. Evolution laws: Flow rule.
The formulation of a model of finite strain plasticity is completed by specifying the evolution eqns (3). This aspect of the theory is where the key differences between existing models arise.

i. In the fundamental work of MANDEL [1972], a yield criterion with functional form $\tilde{\Phi}(\boldsymbol{\Sigma},\beta^{\alpha},\Theta)$ is postulated along with a finite strain version of the classical (isothermal) principle of maximum dissipation of von Mises, see HILL [1950, p. 60], leading to the following version of the evolution eqns (3)

$$
\mathbf{L}^{p}=\gamma \partial_{\boldsymbol{\Sigma}} \tilde{\Phi} \quad \text { and } \quad \dot{\xi}_{\alpha}=\gamma \partial_{\beta^{\alpha}} \tilde{\Phi}. \tag{10}
$$

Here $\gamma \geq 0$ is the plastic multiplier obeying the standard Kuhn-Tucker conditions $\tilde{\Phi} \leq 0$ and $\gamma \tilde{\Phi}=0$, along with the consistency requirement $\gamma \dot{\tilde{\Phi}}=0$. Observe that relation $(10)_{1}$ defines a nine-dimensional flow rule.

ii. As noted in LUBLINER [1986], Mandel's derivation of (10) from the principle of maximum dissipation does not account for the symmetry constraint $\mathbf{C}^{e-1} \boldsymbol{\Sigma}=\boldsymbol{\Sigma}^{T} \mathbf{C}^{e-1}$; see LUBLINER [1990, p. 460] for further discussion and an alternative form of $(10)_{1}$. Simo and MIEHE [1992] further observe that temperature effects are ignored in Mandel's isothermal version of the principle of maximum dissipation, and remove this restriction by appealing to a thermomechanical extension of this classical principle. For an associative model, (9) implies the evolution equation

$$
\dot{\eta}^{p}=\gamma \partial_{\Theta} \tilde{\Phi} \quad \text { with } \eta=\eta^{e}+\eta^{p}, \tag{11}
$$

which provides a phenomenological interpretation for the evolution of $\eta^{p}$ in terms of the temperature changes of the flow stress in a plastic process.

iii. Flow rules that take into account the symmetry constraint on $\boldsymbol{\Sigma}$ can be motivated by casting expression (9) for the internal dissipation in the equivalent form $^{1}$

$$
\mathcal{D}_{\text {int }}=\mathbf{S} \cdot \mathbf{D}^{p}+\beta^{\alpha} \dot{\xi}_{\alpha}+\Theta \dot{\eta}^{p}, \quad \text { where } \mathbf{D}^{p}:=\operatorname{sym}\left[\mathbf{C}^{e} \mathbf{L}^{p}\right]. \tag{12}
$$

Definition $(12)_{2}$ appears in Simo [1985, eqn (3.14b)] and gives the symmetrization of $\mathbf{L}^{p}$ relative to $\mathbf{C}^{e}$, which is consistent with the interpretation of $\mathbf{C}^{e}$ as the metric tensor in the intermediate configuration. The same definition for $\mathbf{D}^{p}$ occurs in MORAN, ORTIZ, and SHIH [1990] where, consistent with the view of $\mathbf{C}^{e}$ as a metric, the plastic spin is also defined as the skew-symmetric part of $\mathbf{L}^{p}$ relative to $\mathbf{C}^{e}$. This leads to the decomposition

$$
\mathbf{L}^{p}=\mathbf{C}^{e-1}\left[\mathbf{D}^{p}+\mathbf{W}^{p}\right], \quad \text { where } \mathbf{W}^{p}=\operatorname{skew}\left[\mathbf{C}^{e} \mathbf{L}^{p}\right]. \tag{13}
$$

Because in most metal elastic deformations are typically small in comparison with plastic deformations, (13) differs slightly from the usual decomposition of $\mathbf{L}^{p}$ into symmetric and skew-symmetric parts. Assuming a yield criterion of the form $\tilde{\Phi}(\mathbf{S}, \beta^{\alpha}, \Theta)$, which depends on $\boldsymbol{\Sigma}$ via the symmetric part $\mathbf{S}=\mathbf{C}^{e-1} \boldsymbol{\Sigma}$, MORAN, ORTIZ, and SHIH [1990] suggest the associative flow rule $\mathbf{D}^{p}=\gamma \partial_{\mathbf{S}} \tilde{\Phi}$ and note that the plastic spin $\mathbf{W}^{p}$, defined by $(13)_{2}$, remains unspecified. These authors remark that the further assump-

---

$^{1}$ We remark that the alternative expression $\mathcal{D}_{\text {mech }}^{p}=\chi \mathbf{S} \cdot \mathbf{D}^{p}$, where $\chi$ is a factor going back to the classical work of TAYLOR and QUINNEY [1933], is often used in the present context and can be motivated by micro-mechanical considerations; see BEVER, HOLT, and TITCHENER [1973].

tion of zero plastic spin, commonly made in phenomenological theories of plasticity, implies the condition $\mathbf{W}^p = \mathbf{0}$ and completely specifies the orientation of the intermediate configuration. In view of (13) this leads to the flow rule

$$
\mathbf{L}^p=\gamma \mathbf{C}^{e-1} \partial_{\mathbf{S}} \hat{\Phi}, \quad \dot{\xi}_{\alpha}=\gamma \partial_{\beta^{\alpha}} \hat{\Phi} \quad \text { and } \quad \dot{\eta}^{p}=\gamma \partial_{\Theta} \hat{\Phi}. \tag{14}
$$

We remark that explicit constitutive equations for the plastic spin arise naturally in the model of single-crystal plasticity as a result of Schmidt's law; see HILL and RICE [1972], ASARO [1983], HILL and HAVNER [1982], and the more recent discussions in BOYCE, WEB- BER, and PARKS [1989], HARREN [1991], and MORAN, ORTIZ, and SHIH [1992], among others. This structure is often used as a motivation for the development of phenomenological flow rules for the plastic spin; see DAFALIAS [1984] and ANAND [1985].

II.3.3. Models of multiplicative plasticity in the current configuration. Models of plasticity widely used in numerical simulations are typically formulated directly in the current configuration. See e.g. the review articles of NEEDLEMAN and TVEEGARD [1984], and HUGHES [1984]. To establish a connection between these models and formulations of multiplicative plasticity, we adopt the flow rule (14) as a point of departure and set $\mathbf{b}^{e}:=\mathbf{F}^{e} \mathbf{F}^{e T}$. An algebraic manipulation using $(5)_{2}$ then yields

$$
\mathbf{F}^{e}\left[\mathbf{C}^{e-1} \partial_{\mathbf{S}} \hat{\Phi}\right] \mathbf{F}^{e T}=\mathbf{n b}^{e}, \quad \text { where } \mathbf{n}:=\mathbf{F}^{e-T}\left[\partial_{\mathbf{S}} \hat{\Phi}\right] \mathbf{F}^{e-1}. \tag{15}
$$

Relation $(15)_{2}$ provides an interpretation of $\mathbf{n}$ as the normal field to the yield surface $\hat{\Phi}(\mathbf{S}, \beta^{\alpha}, \Theta)$, convected to the current configuration via the elastic deformation gradient $\mathbf{F}^{e}$. Similarly, definition $(12)_{2}$ along with $(5)_{2}$ yields the identity:

$$
\mathbf{F}^{e} \operatorname{sym}\left[\mathbf{L}^{p}\right] \mathbf{F}^{e T}=-\frac{1}{2} \mathfrak{£}_{\mathbf{v}} \mathbf{b}^{e} \quad \text { where } \mathfrak{£}_{\mathbf{v}} \mathbf{b}^{e}:=\mathbf{F} \frac{\partial}{\partial t}\left[\mathbf{F}^{-1} \mathbf{b}^{e} \mathbf{F}^{-T}\right] \mathbf{F}^{T}, \tag{16}
$$

which can be verified by a direct calculation. Relation $(16)_{2}$ defines $\mathfrak{£}_{\mathbf{v}} \mathbf{b}^{e}$ as the convected derivative (or Lie derivative) of the left Cauchy-Green tensor $\mathbf{b}^{e}$, while relation $(16)_{1}$ shows that $\mathfrak{£}_{\mathbf{v}} \mathbf{b}^{e}$ is a measure of plastic deformation directly related to $\mathbf{L}^{p}$. In fact, $\mathfrak{£}_{\mathbf{v}} \mathbf{b}^{e}=\mathbf{0}$ if and only if $\operatorname{sym}\left[\mathbf{L}^{p}\right]=\mathbf{0}$. By combining the preceding two results, the flow rule (14) can be recast in the entirely equivalent form:

$$
-\frac{1}{2} \mathfrak{£}_{\mathbf{v}} \mathbf{b}^{e}=\gamma \operatorname{sym}\left[\mathbf{n b}^{e}\right], \quad \dot{\xi}_{\alpha}=\gamma \partial_{\beta^{\alpha}} \hat{\Phi} \quad \text { and } \quad \dot{\eta}^{p}=\gamma \partial_{\Theta} \hat{\Phi}. \tag{17}
$$

Observe that (17) is not restricted to isotropy. The formulation in the current configuration is completed by the constitutive equation $\boldsymbol{\tau}=2 \mathbf{F}^{e}\left[\partial_{\mathbf{C}^{e}} \hat{E}\right] \mathbf{F}^{e T}$ and $\Theta=\partial_{\eta^{e}} \hat{E}$ for the Kirchhoff stress tensor and the absolute temperature, respectively.

II.3.4. General isotropic model of multiplicative plasticity. Under the restriction to isotropy, models of multiplicative plasticity are invariant relative to the orientation of the intermediate configuration. A standard result (see e.g. TRUESDELL & NOLL [1965]) then shows that the internal energy becomes a function of $\mathbf{b}^{e}$; i.e. $\hat{E}(\mathbf{C}^{e}, \eta^{e})=\hat{e}(\mathbf{b}^{e}, \eta^{e})$. In addition, the yield criterion is a (necessarily isotropic) function of the Kirchhoff stress of the form $\hat{\phi}(\boldsymbol{\tau}, \beta^{\alpha}, \Theta) \leq 0$. The Kirchhoff stress tensor $\boldsymbol{\tau}$ and $\mathbf{n}$ are given by

$$
\boldsymbol{\tau}=2 \partial_{\mathbf{b}^{e}} \hat{e}\left(\mathbf{b}^{e}, \eta^{e}\right) \mathbf{b}^{e} \quad \text { and } \quad \mathbf{n}=\partial_{\boldsymbol{\tau}} \hat{\phi}\left(\boldsymbol{\tau}, \beta^{\alpha}, \Theta\right). \tag{18}
$$

Formula $(18)_1$ is a well-known result in elasticity; see TRUESDELL and NOLL [1965], while formula $(18)_2$ follows from $(15)_2$ by a straightforward application of the chain rule. The flow rule (17) with $\mathfrak{n}$ defined by $(18)_2$ first appears in SIMO and MIEHE [1992] under the restriction to isotropy. These relations furnish the most general form of an isotropic formulation of multiplicative plasticity. Specialization of $\hat{\phi}$ to the Mises yield criterion results in an extension to finite strains of the classical model of $J_2$-flow theory.

### III. A PRIORI STABILITY ESTIMATES

The central issue in a nonlinear stability analysis of coupled problems concerns the appropriate notion of nonlinear stability. In the linear regime, there is a notion of stability going back to the fundamental work of LAX, see RICHTMYER and MORTON [1967, Chapter 2], which exploits the underlying semigroup structure of the problem of evolution. For nonlinear dissipative problems of evolution, nonlinear stability is often phrased in terms of an a priori estimate on the dynamics. Typical examples include the incompressible Navier-Stokes equations, see e.g. TEMAM [1979], and the system of coupled nonlinear thermoelasticity where the a priori estimate arises from the second law; see ERICKSEN [1966], GURTIN [1975], BALL and KNOWLES [1986], and ARMERO and SIMO [1992]. The goal of this section is to present analogous results for the model of nonlinear thermoplasticity described in Section II.3. To our knowledge, these results are new. Existing estimates for plasticity are restricted either to the mechanical theory, see SIMO [1991a] and references therein, or limited to the linear perturbation analyses for the rate-dependent coupled problem initiated in CLIFTON [1980]; see MOLINARI and CLIFTON [1983], ANAND, KIM, and SHAWKI [1987], and the review in SHAWKI and CLIFTON [1989]. The key tool in the development of these stability estimates is the Clausius-Duhem form of the second law comprised by inequality (1c). For coupled thermoelasticity, the inequality $\mathfrak{D}_{\text{con}} \geq 0$ implied by (1c) plays a central role in the analysis on BALL and KNOWLES [1986].

#### III.1. The general abstract problem of evolution

The general initial boundary value problem (IBVP) for coupled thermoplasticity at finite strains is defined by (1), the abstract constitutive equation (4), and standard initial conditions for the mechanical and thermal fields, supplemented by boundary conditions. In addition to the thermal boundary condition (2), consider the general boundary conditions for the macroscopic deformation $\boldsymbol{\varphi}(\cdot, t)$ and the traction vector $\mathbf{T}(\cdot, t):=\mathbf{P}(\cdot, t) \mathbf{N}(\cdot)$, where $\mathbf{N}(\cdot)$ is the unit outward normal to the boundary $\partial \Omega$:

$$
\boldsymbol{\varphi}=\overline{\boldsymbol{\varphi}} \quad \text { on } \Gamma_{\boldsymbol{\varphi}} \times[0, T] \quad \text { and } \quad \mathbf{P N}=\overline{\mathbf{T}} \quad \text { on } \Gamma_{T} \times[0, T]. \tag{19}
$$

Here $\overline{\boldsymbol{\varphi}}$ and $\overline{\mathbf{T}}$ are specified boundary data on the parts $\Gamma_{\boldsymbol{\varphi}}$ and $\Gamma_{T}$ of the boundary $\partial \Omega$, respectively, subject to the standard restrictions $\Gamma_{\boldsymbol{\varphi}} \cup \Gamma_{T}=\partial \Omega$ and $\Gamma_{\boldsymbol{\varphi}} \cap \Gamma_{T}=\emptyset$.

Assume that the mechanical loads derive from a potential $V_{\text{ext}}(\boldsymbol{\varphi})$, according to the standard relation $\mathbf{B}=-\partial_{\boldsymbol{\varphi}} V_{\text{ext}}$, and consider for simplicity the case of zero heat source; i.e. $R=0$. With the preceding notation in hand, define the functional $\mathbb{L}(\boldsymbol{\varphi}, \mathbf{V}, \eta ; \mathbf{G})$ by the expression

$$
\begin{aligned}
\mathbb{L}(\boldsymbol{\varphi}, \mathbf{V}, \eta ; \mathbf{G}):= & {\left[\int_{\Omega}\left[\hat{E}(\mathbf{F}, \mathbf{G}, \eta)-\theta_{0} \eta+\frac{1}{2} \rho_{0} \mathbf{V} \cdot \mathbf{V}\right] d \Omega\right] } \\
& +\left[\int_{\Omega} V_{\text {ext }} d \Omega-\int_{\Gamma} \mathbf{T} \cdot \boldsymbol{\varphi} d \Gamma\right],
\end{aligned}
$$

where the second term within brackets gives the total potential energy of the mechanical loading. In the absence of microstructural variables, expression (20) reduces to the canonical free energy function for thermoelasticity introduced in DUHEM [1911]. In the present, more general context, the rate of change of $\mathbb{L}(\boldsymbol{\varphi}, \mathbf{V}, \eta ; \mathbf{G})$ along the dynamics generated by the coupled IBVP is computed using the chain rule, constitutive equation (4), boundary conditions (20), and Green's formula, as follows:

$$
\begin{aligned}
\frac{d}{d t} \mathbb{L}(\boldsymbol{\varphi}, \mathbf{V}, \eta ; \mathbf{G})= & \int_{\Omega}\left[\rho_{0} \mathbf{V} \cdot \dot{\mathbf{V}}+\partial_{\mathbf{F}} \hat{E} \cdot \operatorname{GRAD}[\mathbf{V}]-\mathbf{B} \cdot \mathbf{V}\right] d \Omega-\int_{\Gamma} \mathbf{T} \cdot \mathbf{V} d \Omega \\
& +\int_{\Omega}\left[\partial_{\mathbf{G}} \hat{E} \cdot \dot{\mathbf{G}}+\left(\partial_{\eta} \hat{E}-\theta_{0}\right) \dot{\eta}\right] d \Omega \\
= & \int_{\Omega}\left\{\mathbf{V} \cdot\left[\rho_{0} \dot{\mathbf{V}}-\operatorname{DIV}[\mathbf{P}]-\mathbf{B}\right]+\left[-\mathfrak{D}_{\mathrm{int}}+\left(\theta-\theta_{0}\right) \dot{\eta}\right]\right\} d \Omega. \quad(21)
\end{aligned}
$$

The first bracket in (21) vanishes as a result on the momentum equations $(1 a)_{1,2}$. Inserting the reduced energy equation $(1 a)_{3}$ into the second term within brackets and using Green's formula along with the thermal boundary condition (2) gives

$$
\begin{aligned}
\frac{d}{d t} \mathbf{L}(\boldsymbol{\varphi}, \mathbf{V}, \eta ; \mathbf{G}) & =-\int_{\Omega}\left[\mathfrak{D}_{\mathrm{int}}+\left(1-\theta_{0} / \theta\right)\left(\operatorname{DIV}[\mathbf{Q}]-\mathfrak{D}_{\mathrm{int}}\right)\right] d \Omega \\
& =-\int_{\Omega}\left[\left(\theta_{0} / \theta\right) \mathfrak{D}_{\mathrm{int}}-\operatorname{GRAD}\left[1-\theta_{0} / \theta\right] \cdot \mathbf{Q}\right] d \Omega \\
& =-\int_{\Omega} \frac{\theta_{0}}{\theta}\left[\mathfrak{D}_{\mathrm{int}}-\frac{1}{\theta} \operatorname{GRAD}[\theta] \cdot \mathbf{Q}\right] d \Omega=-\int_{\Omega} \frac{\theta_{0}}{\theta} \mathfrak{D} d \Omega \leq 0, \quad(22)
\end{aligned}
$$

because $\mathfrak{D} \geq 0$ as a result of the Clausius-Duhem form (1c) of the second law. Consequently, the functional $\mathbb{L}(\boldsymbol{\varphi}, \mathbf{V}, \eta ; \mathbf{G})$ is non-increasing along the flow generated by the coupled IBVP. We regard this condition as a fundamental a priori estimate for the coupled IBVP, which must be preserved by the time-stepping algorithm.

For nonlinear thermoelasticity (i.e. $\mathbf{G} \equiv 0$ ) inequality (22) first appears in DUHEM [1911]. Subsequently ERICKSEN [1966] shows that $\mathbb{L}(\boldsymbol{\varphi}, \eta)$ is in fact a Lyapunov function for the nonlinear thermoelastic problem. For linear thermoelasticity, in the absence of external loads the linearization of $\mathbb{L}[\cdot]$ about the reference configuration reduces to

$$
\mathbb{L}_{\text {lin }}(\mathbf{u}, \mathbf{v}, \vartheta)=\frac{1}{2} \int_{\Omega}\left[\varepsilon[\mathbf{u}] \cdot \mathbf{C} \varepsilon[\mathbf{u}]+\frac{c_{0}}{\theta_{0}} \vartheta^{2}+\rho_{0} \mathbf{v} \cdot \mathbf{v}\right] d \Omega,
$$

where $\mathbf{C}$ is the (isothermal) mechanical tangent tensor, $c_{0}$ is the reference heat capacity, $\mathbf{u}$ is the displacement field, $\mathbf{v}$ is the velocity field and $\vartheta:=\theta-\theta_{0}$ denotes the rel-


ative temperature field. In addition, $\varepsilon[\mathbf{u}] := \mathrm{sym}[\nabla \mathbf{u}]$ is the infinitesimal strain tensor. As pointed out in DAFERMOs [1976], $\mathbb{L}_{\text{lin}}[\cdot]$ defined by (23) defines a norm [in the Hilbert space $\mathcal{V} = [H^1(\Omega)]^3 \times [L^2(\Omega)]^3 \times L^2(\Omega)$] and the a priori estimate renders linearized thermoelasticity a semigroup of contractions in $\mathcal{V}$. For the linearized problem, this contractive structure is exploited in ARMERO and SIMO [1992] in a rigorous stability analysis of staggered algorithms.

### III.2. Dissipation and the second law in multiplicative plasticity
The a priori stability estimate (22) depends critically on the inequality (1c) implied by the second law. To apply these results to coupled thermoplasticity, the first task is to verify that the evolution equations in the representative class of models outlined in Section 2 are in fact compatible with the inequality (1c). The first observation is that $\mathcal{D}_{\text{int}} \equiv 0$ in a purely elastic process. Because elastic processes are admissible, inequality (1c) implies $\mathcal{D}_{\text{con}} \geq 0$. It is well known, for instance, that the classical Fourier law of heat conduction satisfies this inequality. Similarly, because $\mathcal{D}_{\text{con}} = \mathcal{D}_{\text{ther}}^p \equiv 0$ in an isothermal process, inequality (1c) implies that $\mathcal{D}_{\text{mech}}^p \geq 0$. Therefore, satisfaction of second law for all admissible processes in the material requires

$$
\begin{gathered}
\mathcal{D}_{\text{mech}}^p \geq 0, \quad \mathcal{D}_{\text{con}} \geq 0 \quad \text{and} \quad \mathcal{D} = \mathcal{D}_{\text{mech}}^p + \mathcal{D}_{\text{ther}}^p + \mathcal{D}_{\text{con}} \geq 0 \quad \text{in } \Omega \times [0, T].
\end{gathered}
\tag{24}
$$

It follows that any specific choice of rate equations governing the evolution of $\mathbf{G}$, defined here by (5), is restricted by the preceding inequalities. Two representative models are examined to provide an illustration of how these restrictions are satisfied in plasticity.

#### III.2.1. The model of Mandel.
Consider the original model of MANDEL [1972] with a yield criterion of the form $\tilde{\Phi}(\boldsymbol{\Sigma}, \beta, \Theta) = f(\boldsymbol{\Sigma}) + \beta - \sigma_Y(\Theta) \leq 0$. Here $\sigma_Y(\Theta) > 0$ is the flow stress and $\beta = -\partial_{\xi} \hat{H}(\xi)$ is a measure of isotropic hardening. As in standard models of classical plasticity, see HILL [1950], assume further that the function $f(\cdot)$ is convex and homogeneous of degree-one. Euler's theorem then implies $\partial_{\boldsymbol{\Sigma}} f(\boldsymbol{\Sigma}) \cdot \boldsymbol{\Sigma} = f(\boldsymbol{\Sigma})$. This property in conjunction with the flow rule (10) specifies $\mathcal{D}_{\text{mech}}^p$ in (12) as

$$
\begin{aligned}
\mathcal{D}_{\text{mech}}^p &= \gamma\left[\boldsymbol{\Sigma} \cdot \partial_{\boldsymbol{\Sigma}} f(\boldsymbol{\Sigma}) + \beta - \sigma_Y(\Theta)\right] + \gamma \sigma_Y(\Theta) \\
&= \gamma \tilde{\Phi} + \gamma \sigma_Y(\Theta) = \gamma_Y(\Theta) \geq 0, \quad \text{because } \gamma \tilde{\phi} = 0 \text{ and } \gamma \geq 0.
\end{aligned}
\tag{25}
$$

It follows that the mechanical dissipation is nonnegative and equals the plastic slip rate $\gamma \geq 0$ times the flow stress. In view of relation (11) the part $\mathcal{D}_{\text{ther}}^p$ of the internal dissipation is given by $\mathcal{D}_{\text{ther}}^p = -\gamma \Theta \sigma_Y'(\Theta)$ for the specific form of the yield criterion under consideration. Inequality $(24)_3$ is then always satisfied in the presence of thermal softening, because $\sigma_Y'(\Theta) \leq 0$ ensures that $\mathcal{D}_{\text{ther}}^p \geq 0$. An identical argument applies to a flow rule of the form (17) if the yield criterion $\hat{\Phi}$ is homogeneous of degree one in $\mathbf{S}$ and linear in $\beta^\alpha$.

#### III.2.2. Models of multiplicative plasticity in the current configuration.
An entirely analogous argument applies to plasticity models formulated in the current configuration. Using (16) and the standard relation $\boldsymbol{\tau} = \mathbf{F}^e \mathbf{S} \mathbf{F}^{eT}$ gives:

$$
\mathcal{D}_{\text{mech}}^p = \mathbf{F}^e \mathbf{S} \mathbf{F}^{eT} \mathbf{b}^{e-1} \cdot \left[\mathbf{F}^e \mathbf{L}^p \mathbf{F}^{eT}\right] + \beta^\alpha \dot{\xi}_\alpha = \boldsymbol{\tau} \mathbf{b}^{e-1} \cdot \left[\mathbf{F}^e \mathbf{L}^p \mathbf{F}^{eT}\right] + \beta^\alpha \dot{\xi}_\alpha.
\tag{26}
$$

Now consider a conventional yield criterion of form $\hat{\phi}(\tau, \beta, \theta)=f(\tau)+\beta-\sigma_{Y}(\theta) \leq 0$ with $\beta=-\partial_{\xi} \hat{H}(\xi)$, where $\xi$ is the equivalent plastic strain with rate equation $\dot{\xi}=\gamma$, from $(17)_{2}$. Assume further that $f(\tau)$ is a convex function, homogeneous of degree one so that $f(\tau)=\partial_{\tau} f(\tau) \cdot \tau$. Classical examples include the Mises and Tresca yield functions. Inserting the flow rule (17) into (26), using expression (18), the Kuhn-Tucker relations $\gamma \hat{\phi}=0$ and $\gamma \geq 0$, and noting that $\tau$ commutes with $\mathbf{b}^{e}$ as a result of isotropy gives

$$
\mathfrak{D}_{\text {mech }}^{p}=\gamma\left[\tau \cdot \partial_{\tau} f(\tau)+\beta\right]=\gamma \hat{\phi}+\gamma \sigma_{Y}(\theta)=\gamma \sigma_{Y}(\theta) \geq 0.
$$

Since $\mathfrak{D}_{\text {ther }}^{p}=\theta \dot{\eta}^{p}=-\gamma \theta \sigma_{Y}^{\prime}(\theta)$ it follows that the assumption $\sigma_{Y}^{\prime}(\theta) \leq 0$ of thermoplastic softening again ensures consistency with the second law, reflected in inequalities (24).

### III.3. A priori stability estimates for multiplicative thermoplasticity

By specialization of the general result (22) one obtains an a priori estimate in terms of the functional $\mathbb{L}[\cdot]$ for any of the models described in the preceding Section. However, in a model of multiplicative plasticity the internal energy is defined by (6) and depends on the microstructural variables $\mathbf{G}$ via the elastic part of the deformation and the hardening variables (as well as elastic entropy). It is therefore natural to introduce an alternative functional $\mathbb{V}[\cdot]$ defined by the expression

$$
\begin{aligned}
\mathbb{V}(\chi):= & {\left[\int_{\Omega}\left[\hat{E}\left(\mathbf{C}^{e}, \eta^{e}, \xi_{\alpha}\right)-\theta_{0} \eta^{e}+\frac{1}{2} \rho_{0} \mathbf{V} \cdot \mathbf{V}\right] d \Omega\right] } \\
& +\left[\int_{\Omega} V_{\mathrm{ext}} \mathrm{d} \Omega-\int_{\Gamma} \mathbf{T} \cdot \boldsymbol{\varphi} d \Gamma\right], \quad \text { where } \chi:=\left\{\mathbf{V}, \mathbf{C}^{e}, \eta^{e}, \xi_{\alpha}\right\}.
\end{aligned}
$$

In the isotropic case, the variable $\mathbf{C}^{e}$ is replaced by $\mathbf{b}^{e}$ in (28). By making use of the identity

$$
\mathbf{P} \cdot \dot{\mathbf{F}}=\mathbf{S} \cdot \frac{1}{2} \dot{\mathbf{C}}^{e}+\mathbf{S} \cdot \mathbf{D}^{p} \quad \text { with } \mathbf{D}^{p}:=\operatorname{sym}\left[\mathbf{C}^{e} \mathbf{L}^{p}\right],
$$

which can be verified easily by a direct calculation exploiting the multiplicative factorization $(5)_{2}$, a calculation entirely analogous to that leading to (22) together with inequalities $(24)_{1,2}$ now yields the sharper estimate

$$
\frac{d}{d t} \mathbb{V}(\chi)=-\int_{\Omega} \frac{\theta_{0}}{\theta}\left[\mathfrak{D}_{\text {mech }}^{p}+\mathfrak{D}_{\text {con }}\right] d \Omega \leq 0,
$$

where $\mathfrak{D}_{\text {mech }}^{p}$ is defined by (12). Obviously, for nonlinear thermoelasticity the functions $\mathbb{V}[\cdot]$ and $\mathbb{L}[\cdot]$ coincide. However, in contrast with the situation found in nonlinear thermoelasticity, for coupled thermoplasticity $\mathbb{V}[\cdot]$ cannot be viewed as a Lyapunov function because $\mathbb{V}[\cdot]$ does not define a proper 'norm' on the deformation $\boldsymbol{\varphi}$. In particular, estimate (30) does not preclude the possible formation of shear bands, characterized by the localization of the total and plastic deformations in the presence of thermoplastic softening. This situation is completely parallel to the one encountered in infinitesimal isothermal perfect plasticity where the IBVP is contractive in stresses, but not necessar-

ily in the (total) deformation; see Simo [1991]. Therefore, estimate (30) is compatible with current linear perturbation analyses for rate-dependent inelastic solids of the type found in ANAND, KIM and SHAWKI [1987] and others; see the review article of SHAWKI and CLIFTON [1989].

In summary, the a priori estimate (30) provides a meaningful notion of nonlinear sta- bility that does not preclude interesting physical phenomena and holds for general mod- els of multiplicative plasticity. This a priori estimate plays a central role in the analysis of nonlinear numerical stability described below.

## IV. UNCONDITIONALLY STABLE STAGGERED ALGORITHMS

To motivate the proposed methodology, we begin with a brief summary of the results obtained in ARMERO and SIMo [1992] related to standard staggered algorithms based on the isothermal split of the problem. The restricted stability of algorithms designed on the basis of this split motivates the introduction of the adiabatic split, whose formula- tion for the thermoplastic case is presented in Section IV.2. For concreteness, we shall take as a representative model of multiplicative plasticity that defined by the internal energy (6). Furthermore, to establish a connection with current methodologies, we adopt the absolute temperature field $\theta$ in place of the entropy as an independent variable by introducing the free energy function $\hat{\Psi}(C^{e}, \xi_{\alpha}, \theta)$ via the standard Legendre transfor mation $\hat{\Psi}=\hat{E}-\theta \eta$. Accordingly, in the discussion that follows, we adopt the short- hand notation

$$
\overline{\boldsymbol{\chi}}=\left\{\mathbf{C}^{e}, \xi_{\alpha}, \theta\right\} \quad \text { and } \quad \boldsymbol{\chi}:=\{\mathbf{V}, \overline{\boldsymbol{\chi}}\}
$$

for the primary variables in the problem. We then have the constitutive equations

$$
\mathbf{S}=2 \partial_{\mathbf{C}^{e}} \hat{\Psi}(\overline{\boldsymbol{\chi}}), \quad \eta^{e}=-\partial_{\theta} \hat{\Psi}(\overline{\boldsymbol{\chi}}) \quad \text { and } \quad \beta^{\alpha}=-\partial_{\xi_{\alpha}} \hat{\Psi}(\overline{\boldsymbol{\chi}}),
$$

which are equivalent to (7), along with expression $\mathfrak{D}_{\text {mech }}^{p}=\mathbf{S} \cdot \mathbf{D}^{p}+\beta^{\alpha} \dot{\xi}_{\alpha} \geq 0$ for the plastic dissipation. Recall that the nominal stress is given by $\mathbf{P}=\mathbf{F}^{e} \mathbf{S} \mathbf{F}^{p-T}$.

### IV.1. The isothermal split

Standard staggered time-stepping algorithms for coupled thermomechanical problems consist of a mechanical phase at constant temperature, followed by a thermal phase at constant fixed configuration. In Simo and MIEHE [1992] this strategy is shown to arise from the following operator split of the coupled problem of evolution:

Problem 1. (Isothermal)
Problem 2. (Heat Conduction)

$$
\left.\left.\begin{array}{rl}
\dot{\boldsymbol{\varphi}} & =\mathbf{V} \\
\rho_{0} \dot{\mathbf{V}} & =\operatorname{DIV}[\mathbf{P}(\overline{\boldsymbol{\chi}})]+\mathbf{B} \\
c_{0} \dot{\theta} & =0
\end{array}\right\} \quad \begin{array}{rl}
\dot{\boldsymbol{\varphi}} & =\mathbf{0} \\
\rho_{0} \dot{\mathbf{V}} & =\mathbf{0} \\
c_{0} \dot{\theta} & =-\operatorname{DIV}[\mathbf{Q}(\overline{\boldsymbol{\chi}})]+\mathfrak{D}_{\text {mech }}^{p}-\mathcal{K}
\end{array}\right\} .
$$

We emphasize that, contrary to common practice, the evolution equations (17) for the microstructural variables $\mathbf{G}:=\left\{\mathbf{F}^{p}, \eta^{p}, \xi_{\alpha}\right\}$ are enforced in both phases of the operator

split. Note further that the thermal equation has been written in first order form through
the definitions $c_{0}:=-\theta \partial_{\theta \theta}^{2} \hat{\Psi}$ (reference heat capacity) and $\mathcal{K}:=-\theta \partial_{\theta}\left[\mathbf{S} \cdot \mathbf{D}^{p}-\mathfrak{D}_{\text {mech }}^{p}\right]$
(elastic-plastic structural heating).

Unfortunately, despite its conceptual appeal, a partition of the thermoplastic prob-
lem of evolution in the format of (33) does not preserve the a priori estimate (30). This
conclusion holds true even in the much simpler setting of linearized thermoelasticity. For
this problem, the function $\mathbb{V}[\cdot]$ (or $\mathbb{L}[\cdot]$ ) collapses to $\mathbb{L}_{\text {lin }}(\mathbf{u}, \mathbf{v}, \vartheta)=:\|(\mathbf{u}, \mathbf{v}, \vartheta)\|_{\nu}^{2}$
defined by (23) and one obtains the following result in the isothermal mechanical phase:

$$
\begin{aligned}
\left.\frac{d}{d t} \mathbb{L}_{\text {lin }}(\mathbf{u}, \mathbf{v}, \vartheta)\right|_{\text {Problem } 1} & =\left.\frac{d}{d t}\|(\mathbf{u}, \mathbf{v}, \vartheta)\|_{\nu}^{2}\right|_{\text {Problem } 1} \\
& =-\int_{\Omega} \mathbf{m} \nabla \vartheta \cdot \mathbf{v} d v \neq C\|(\mathbf{u}, \mathbf{v}, \vartheta)\|_{\nu}^{2} \quad \forall(\mathbf{u}, \mathbf{v}, \vartheta) \in \mathcal{V}, \quad(34)
\end{aligned}
$$

for some constant $C$, because the inequality $\|\nabla \vartheta\|_{L^{2}} \leq \hat{M}\|\vartheta\|_{L^{2}}$ does not hold for some
constant $\hat{M}>0$ and $\forall \vartheta \in H^{1}(\Omega)$. In deriving (34) we have assumed for simplicity con-
stant isotropic coupling terms defined by $\mathbf{m}:=\partial_{\theta \epsilon}^{2} \hat{\Psi}$. Furthermore, it can be shown
that the partitioned operators do not generate a semigroup in $\mathcal{V}$, implying that each of
the two subproblems in (33) are improperly posed when considered separately. Despite
this negative result, a numerical stability analysis via the energy method of the fully dis-
crete problem presented in the aforementioned reference shows that algorithms based
on this split of the coupled problem can retain conditional stability in a finite element
setting. This positive result is a direct consequence of the existence of the inverse esti-
mate (CIARLET [1978]) $\left\|\nabla \vartheta^{h}\right\| \leq(M / h)\left\|\vartheta^{h}\right\|$ for a finite element space $\mathcal{V}^{h}$ approxima-
tion of $\mathcal{V}\left(\mathcal{V}^{h} \subset \mathcal{V}\right)$. The nonuniformity of this estimate implies that this algorithm
cannot exhibit unconditional stability, in the sense that contractivity in the natural norm
is not inherited by the discrete problem.

Consideration of the quasistatic case (obtained formally by setting $\rho_{0}=0$ ) shows the
unability of algorithms based on this split to handle strongly coupled problems. The par-
tition (33) can be understood as defining a Gauss-Seidel scheme for the solution of the
simultaneous system of coupled equations. It can be shown that the convergence of this
iterative scheme implies a limiting condition for strongly coupled problems of the type
$\Delta t / h^{2} \geq$ constant, which reproduces the results obtained in actual numerical simula-
tions (see Section V.1).

### IV.2. The adiabatic split

We consider the extension of a partition of the coupled problem introduced in ARMERO
and SıMo [1992] in the restricted context of nonlinear thermoelasticity, referred to as the
adiabatic split. The key idea is to partition the problem into a mechanical phase in which
the entropy is held constant, followed by a thermal phase in which the configuration
(but not the microstructural variables) are held constant. Because the total entropy in
thermoplasticity is decomposed additively according to expression $(5)_{3}$, a number of
alternative strategies can be envisaged in the extension of an adiabatic partition to the
coupled thermoplastic problem. The strategy proposed below is motivated by the fol-
lowing design conditions:

1. The final formulation of the operator split must inherit the stability estimate (30)
for the fractional step method to retain unconditional stability.

2. The two subproblems defined by the operator split should possess a symmetric structure in the sense that a subsequent spatial discretization yields symmetric stiffness matrices.

3. Time stepping integrators leading to a fractional step method should exhibit good numerical accuracy, comparable to schemes obtained via analogous time-discretizations of the full coupled problem.

4. The cost involved in the final implementation of the resulting fractional step must be comparable to that involved in the implementation of fractional step methods based on the conventional isothermal split.

These requirements are necessary if the final class of algorithms are to represent a significant improvement over existing methods. In particular, condition 1 provides vastly superior stability characteristics while the remaining conditions ensure that this enhanced performance is not obtained at the expense of either accuracy or computational convenience. Setting $\eta^e(\bar{\chi}) = -\partial_\Theta \hat{\Psi}(\bar{\chi})$, the following alternative partition of the coupled problem of evolution is proposed:

**Problem 1. (Adiabatic)**
$$
\left.
\begin{aligned}
\dot{\boldsymbol{\varphi}} &= \mathbf{V} \
\rho_0 \dot{\mathbf{V}} &= \mathrm{DIV}[\mathbf{P}(\bar{\chi})] + \mathbf{B} \
\Theta \dot{\eta}^e(\bar{\chi}) &= 0 \
\dot{\eta}^p &= 0
\end{aligned}
\right.
$$

**Problem 2. (Heat Conduction)**
$$
\left.
\begin{aligned}
\dot{\boldsymbol{\varphi}} &= \mathbf{0} \
\rho_0 \dot{\mathbf{V}} &= \mathbf{0} \
\Theta \dot{\eta}^e(\bar{\chi}) &= -\mathrm{DIV}[\mathbf{Q}(\bar{\chi})] + \mathfrak{D}_{\text{mech}}^p \
\dot{\eta}^p &= \gamma \partial_\Theta \hat{\Phi}
\end{aligned}
\right\}. \tag{35}
$$

We remark that the plastic flow evolution equations for $\mathbf{F}^p$ and $\xi_\alpha$ (see Section II) are to be enforced in the two phases of the split. Additionally, the temperature field is regarded as the independent variable in the two subproblems defined by (35) rather than the entropy. As in the thermoelastic case, this split is characterized by a mechanical phase at constant entropy, followed by a heat conduction problem at fixed configuration. Observe that both the elastic and plastic parts of the entropy are held fixed in the mechanical phase. This fact is shown below to be crucial for the symmetry of the final formulation.

To ensure that requirement 1 is satisfied, the a priori estimate (30) must be evaluated in both phases of the split. A calculation similar to that described in Section III together with inequalities (24) yields the results:
$$
\left.
\begin{aligned}
\left.\frac{d}{d t} \mathbb{V}(\bar{\chi})\right|_{\text{Problem 1}} &= -\int_\Omega \mathfrak{D}_{\text{mech}}^p d\Omega \leq 0, \
\left.\frac{d}{d t} \mathbb{V}(\bar{\chi})\right|_{\text{Problem 2}} &= -\int_\Omega \frac{\Theta_0}{\Theta} \left[\mathfrak{D}_{\text{mech}}^p + \mathfrak{D}_{\text{con}}\right] d\Omega \leq 0,
\end{aligned}
\right\}, \tag{36}
$$
which show that the split defined by (35) preserves the a priori estimate (30). Therefore, in sharp contrast with schemes based on the conventional isothermal split, unconditionally stable algorithms consistent with the full coupled problem can be obtained merely as the product of two unconditionally stable algorithms consistent with each phase; i.e.

$$
\boxed{
\begin{aligned}
&[\text{Uncond. stable algor. 2}] \circ [\text{Uncond. stable algor. 1}] \\
&\quad = [\text{Uncond. stable coupled algor.}]
\end{aligned}
}\tag{37}
$$

The product formula algorithm defined by (37) exhibits first order accuracy in time; second order accurate schemes are obtained through a double pass technique originally introduced in STRANG [1969].

IV.2.1. Adiabatic mechanical phase. To gain further insight into the implications of the split (35), consider a specific time discretization of the first phase via a standard backward-Euler method. For a typical time increment $[t_n, t_{n+1}]$, with $\Delta t = t_{n+1} - t_n$, this scheme results in the semidiscrete equations

$$
\left.
\begin{aligned}
(\tilde{\boldsymbol{\varphi}}_{n+1} - \boldsymbol{\varphi}_n)/\Delta t &= \tilde{\mathbf{V}}_{n+1}, \\
\rho_0(\tilde{\mathbf{V}}_{n+1} - \mathbf{V}_N)/\Delta t &= \mathrm{DIV}[\tilde{\mathbf{P}}(\tilde{\bar{\chi}}_{n+1})] + \mathbf{B}, \\
\eta^e(\tilde{\bar{\chi}}_{n+1}) - \eta^e(\bar{\chi}_n) &= 0, \\
\tilde{\eta}_{n+1}^p - \eta_n^p &= 0,
\end{aligned}
\right\}\tag{38}
$$

where the quantities $(\tilde{\cdot})_{n+1}$ refer to the intermediate values at $t_{n+1}$ after a pass through the mechanical phase. The independent variables in this phase are $\{\tilde{\boldsymbol{\varphi}}_{n+1}, \tilde{\mathbf{V}}_{n+1}, \tilde{\Theta}_{n+1}\}$ with prescribed values $\{\boldsymbol{\varphi}_n, \mathbf{V}_n, \Theta_n\}$ at time $t_n$. The internal variables $\{\mathbf{F}^p, \eta^p, \xi_\alpha\}$ also have prescribed values at time at $t_n$. Their updated values $(\tilde{\cdot})_{n+1}$ are obtained by numerical integration of their corresponding evolution equations via a return mapping algorithm. The Appendix describes in detail the implementation of this algorithm in this context.

After a spatial finite element discretization is introduced, the actual solution of the resulting nonlinear algebraic system of equations is accomplished by means of conventional iterative schemes for symmetric nonlinear systems; for instance, Newton's method. Regardless of the specific solution procedure employed, the effective implementation of schemes based on the split (35) relies on two crucial observations summarized below.

### Remarks

1. The role of the design constraint $\tilde{\eta}_{n+1}^p = \eta_n^p$. In view of the evolution equation $\dot{\eta}^p = \gamma \partial_\Theta \hat{\Phi}$, $\dot{\eta}^p$ is proportional to the change of yield criterion with temperature and condition $\tilde{\eta}_{n+1}^p = \eta_n^p$ implies that no thermal softening occurs in the first phase. Therefore, the consistency condition is enforced (both the trial and plastic corrector steps of the return map), with the flow stress frozen at the initial temperature $\Theta_n$. It is this feature that renders the final formulation symmetric in a consistent linearization of the governing equations. We refer to Remark I.1 in the Appendix for a detailed discussion.

2. The treatment of the temperature field in the first phase of the split (35). The constitutive equation $\Theta = \partial_{\eta^e} \hat{E}$ along with the design condition $\tilde{\eta}_{n+1}^e = \eta_n^e$ gives an explicit relation for the temperature field $\tilde{\Theta}_{n+1}$ in terms of the configuration and (possibly) the hardening variables, thus defining an exact adiabatic update. If one

is given the free energy $\hat{\Psi}(\bar{\chi})$ in place of the internal energy $\hat{E}$, the solution of the implicit equation

$$
\partial_{\Theta} \hat{\Psi}\left(\bar{\chi}_{n}\right)-\partial_{\Theta} \hat{\Psi}\left(\tilde{\bar{\chi}}_{n+1}\right)=0 \quad \text { gives } \quad \tilde{\Theta}_{n+1}=\hat{\tilde{\Theta}}_{n+1}\left(\tilde{\mathbf{C}}_{n+1}^{e}, \tilde{\xi}_{\alpha n+1} ; \bar{\chi}_{n}\right) \quad(39)
$$

and defines the exact adiabatic update. This equation can be solved numerically, if necessary. The key implication in a FEM context is that only the mechanical degrees of freedom $\{\tilde{\boldsymbol{\varphi}}_{n+1}, \tilde{\mathbf{V}}_{n+1}\}$ are involved in the global solution of the first phase, because $\tilde{\Theta}_{n+1}$ is defined locally by (39). This property renders the numerical implementation essentially identical to that of the more traditional isothermal split.

IV.2.2. Thermal phase at constant configuration. Application of a backward-Euler scheme to the thermal phase of the adiabatic split (35) yields the following equations

$$
\left.\begin{array}{c}
\boldsymbol{\varphi}_{n+1}-\tilde{\boldsymbol{\varphi}}_{n+1}=\mathbf{0}, \\
\mathbf{V}_{n+1}-\tilde{\mathbf{V}}_{n+1}=\mathbf{0}, \\
\Theta_{n+1}\left[\eta^{e}\left(\bar{\chi}_{n+1}\right)-\eta_{n}^{e}\right] / \Delta t=-\operatorname{DIV}\left[\mathbf{Q}\left(\bar{\chi}_{n+1}\right)\right]+\mathfrak{D}_{\mathrm{mech}, n+1}^{p},
\end{array}\right\}
$$

where $\eta_{n}^{e}:=-\partial_{\Theta} \hat{\Psi}(\bar{\chi}_{n})$. The first two equations in (40) merely imply $\boldsymbol{\varphi}_{n+1}=\tilde{\boldsymbol{\varphi}}_{n+1}$ and $\mathbf{V}_{n+1}=\tilde{\mathbf{V}}_{n+1}$. The last equation in (40) follows from the relation $\eta^{e}(\tilde{\bar{\chi}}_{n+1})=\eta^{e}(\bar{\chi}_{n})=$ $\eta_{n}^{e}$, satisfied in the mechanical phase, along with the conservation form of the heat equation in (35). Although the intermediate temperature $\tilde{\Theta}_{n+1}$ is the initial condition for the thermal phase, this special treatment of the energy equation make the final numerical implementation independent of $\tilde{\Theta}_{n+1}$. We note also that this form has shown a superior numerical accuracy in numerical experiments. Thus, this phase reduces to a heat conduction problem at the known fixed configuration $\tilde{\boldsymbol{\varphi}}_{n+1}$ with the only remaining independent variable in this phase being $\Theta_{n+1}$.

The mechanical plastic dissipation arising in phenomenological models of plasticity is typically given by the expression $\mathfrak{D}_{\text {mech }}^{p}=\gamma \sigma_{Y}(\Theta)$ (see Section III.2). Consequently, the term $\mathfrak{D}_{\text {mech }, n+1}^{p}$ in $(40)_{3}$ is computed by

$$
\mathfrak{D}_{\mathrm{mech}, n+1}^{p}:=\Delta \gamma_{n+1} \sigma_{Y}\left(\Theta_{n+1}\right) / \Delta t .
$$

Here $\Delta \gamma$ denotes the incremental plastic consistency multiplier, computed via the return mapping algorithm with the initial conditions $\bar{\chi}_{n}$. Hence, the final formulation becomes completely independent of the intermediate values $\{\tilde{\bar{\chi}}_{n+1}\}$. The actual value of the plastic entropy does not enter explicitly in the calculation and can be computed as a post-processing by the formula

$$
\eta_{n+1}^{p}=\eta_{n}^{p}+\left.\Delta \gamma_{n+1} \partial_{\Theta} \hat{\Phi}\right|_{n+1} .
$$

In summary, the implementation of the first phase in the split (35) is identical to that arising in the purely mechanical theory, with the stored energy replaced here by the adiabatic internal energy function $E=\hat{E}(\mathbf{C}^{e},\xi_{\alpha},\eta^{e}|_{\text{fixed}})$. The tangent elastic moduli then become the adiabatic elasticities of the material. The implementation of the thermal

phase in the split (35) reduces to the solution of the heat equation $(42)_3$ at a (known) fixed configuration $\{\boldsymbol{\varphi}_{n+1}, \mathbf{V}_{n+1}\}$.

It is therefore apparent that the effort involved in the solution of fractional step methods based on the operator split (35) is essentially identical to that required for schemes based on the conventional isothermal split. In addition to the vastly improved stability characteristics, the adiabatic split is especially well suited for problems where the characteristic time associated with temperature effect is so small that the entire process can be assumed to be nearly adiabatic. An example is the formation of shear bands under high strain rates in the presence of strain softening.

## V. REPRESENTATIVE NUMERICAL SIMULATIONS

In this Section we present three numerical simulations that demonstrate the unconditional stability and good accuracy properties of the proposed class of staggered algorithms. The time-stepping algorithms are implemented in conjunction with two finite element spatial discretizations described in the examples.

### V.1. A model of $J_2$-flow theory

We consider a thermomechanical model of $J_2$-flow at finite strains, with a logarithmic stored energy function (ANAND [1979]) and isotropic saturation hardening combined with linear thermal softening, summarized in Box 1. This model falls within the format of the general class of models for multiplicative plasticity described in Section II, with the plastic incompressibility condition $\det[\mathbf{F}^p] = 1$ enforced. Setting $J := \det[\mathbf{F}] = \det[\mathbf{F}^e]$ and denoting the volume preserving part of the elastic left Cauchy-Green tensor $\mathbf{b}^e$ by $\overline{\mathbf{b}}^e := J^{-2/3} \mathbf{b}^e$, the constitutive equation for the elastic entropy then takes the explicit form:

$$
\eta^e = -\partial_{\theta} \hat{\Psi} = c_0 \log(\theta/\theta_0) + 3\kappa\alpha \log J - K_{\theta}(\xi), \tag{43}
$$

where $K_{\theta}(\xi) := \partial_{\theta} K(\xi, \theta)$ does not depend on $\theta$ by the assumed linearity of the thermal softening. This expression leads, after performing a Legendre transformation, to the following explicit result for the internal energy

$$
\begin{aligned}
\hat{e}(\mathbf{b}^e, \xi, \eta^e) &= W(\overline{\mathbf{b}}^e) + U(J) + 3\kappa\alpha\theta_0 \log J \\
& \quad - c_0 \theta_0[1 - \exp[(\eta^e - 3\kappa\alpha \log J + K_{\theta}(\xi))/c_0]] \\
& \quad + [K(\xi, \theta_0) - \theta_0 K_{\theta}(\xi)], \tag{44a}
\end{aligned}
$$

where $W(\overline{\mathbf{b}}^e)$, $U(J)$ and $K(\xi, \theta_0)$ are given in Box 1. The function $K_{\theta}(\xi)$ is also given by an explicit expression; namely,

$$
K_{\theta}(\xi) = -\frac{1}{2}h(\theta_0)\omega_h \xi^2 - [y_0(\theta_0)\omega_0 - y_{\infty}(\theta_0)\omega_h]H(\xi), \tag{44b}
$$

where $H(\xi)$ is defined in Box 1.

The numerical simulations described below are designed to test different features of the algorithms. In Section V.1 the performance of algorithms designed on the basis of the adiabatic split, the conventional isothermal split and the full coupled problem is com-

## BOX 1: Thermoplastic model $-J_2$-flow theory

### 1. Free energy function:
$$
\hat{\Psi}\left(\mathbf{b}^{e}, \xi, \theta\right)=W\left(\overline{\mathbf{b}}^{e}\right)+U(J)+M(J, \theta)+T(\theta)+K(\xi, \theta),
$$

#### i. Logarithmic hyperelastic response ($\mu > 0$ and $\kappa > 0$ constant),
$$
W\left(\overline{\mathbf{b}}^{e}\right)=\mu \sum_{A=1,3}\left[\log \left(\bar{\lambda}_{A}^{e}\right)\right]^{2} \text{ and } U(J)=\frac{1}{2} \kappa \log ^{2} J,
$$
where $\bar{\lambda}_{A}^{e}=J^{-1 / 3} \lambda_{A}^{e}$ ($\lambda_{A}^{e}$ being the elastic principal stretches).

#### ii. Thermoelastic coupling,
$$
M(J, \theta)=-3 \kappa \alpha\left(\theta-\theta_{0}\right) \log J.
$$

#### iii. Thermal contribution,
$$
T(\theta)=c_{0}\left[\left(\theta-\theta_{0}\right)-\theta \log \left(\theta / \theta_{0}\right)\right].
$$

#### iv. Hardening potential,
$$
K(\xi, \theta)=\frac{1}{2} h(\theta) \xi^{2}+\left[y_{0}(\theta)-y_{\infty}(\theta)\right] H(\xi)
$$
$$
\text{where } H(\xi):=
\begin{cases}
\xi-\left(1-e^{-\delta \xi}\right) / \delta, & \text{if } \delta \neq 0; \\
0, & \text{if } \delta=0.
\end{cases}
$$

### 2. Plastic response:

#### i. Von Mises Yield criterion with flow stress $\sigma_{Y}(\theta):=y_{0}(\theta)$,
$$
\hat{\phi}(\tau, \beta, \theta)=\sqrt{\frac{3}{2}}\|\operatorname{dev}[\tau]\|+\beta-\sigma_{Y}(\theta) \leq 0,
$$

#### ii. Hardening variable conjugate to $\xi$,
$$
\beta:=-\partial_{\xi} \hat{\Psi}=-\left[h(\theta) \xi+\left(y_{0}(\theta)-y_{\infty}(\theta)\right)\left(1-e^{-\delta \xi}\right)\right].
$$

#### iii. Linear thermal softening,
$$
\left.
\begin{aligned}
y_{0}(\theta) &=y_{0}\left(\theta_{0}\right)\left[1-\omega_{0}\left(\theta-\theta_{0}\right)\right] \\
h(\theta) &=h\left(\theta_{0}\right)\left[1-\omega_{h}\left(\theta-\theta_{0}\right)\right] \\
y_{\infty}(\theta) &=y_{\infty}\left(\theta_{0}\right)\left[1-\omega_{h}\left(\theta-\theta_{0}\right)\right]
\end{aligned}
\right\}
$$

pared in the quasistatic expansion of a thick-walled thermoplastic cylinder. Section V.2 describes the results obtained in the simulation of the impact of a 3-D cylindrical bar to assess relative performance in the dynamic regime. Finally, Section V.3 summarizes the results obtained in a problem involving the formation of shear bands in plane strain using the adiabatic split.

### V.2. Expansion of a thick-walled thermoplastic cylinder
This problem corresponds to the quasistatic expansion of a thermoplastic thick-walled cylinder. This example has been used by several authors as a test problem to compare the performance of different time-stepping algorithms (e.g. ARGYRIS & DOLTSINIS [1981] and SIMO & MIEHE [1992]). Figure 1 depicts the initial configuration of the discretized solid, as well as the prescribed boundary conditions. Both the internal and external faces of the cylinder are assumed thermally insulated. Plane-strain conditions are assumed in the axial direction so that a unit band of axisymmetric finite elements need only be con- sidered. Isoparametric axisymmetric finite elements based on the enhanced formulation described in SIMO and ARMERO [1992] are employed. The values of the inner and outer radii adopted in the simulation are $a_0 = 100$ mm and $b_0 = 200$ mm, respectively. Table 1 summarizes the material properties chosen for this example: Linear hardening (i.e., $\delta = 0$), and a reference temperature value $\Theta_0 = 293$ K.

The simulations are performed by imposing the displacement at the inner face, with a final inner radius of $a_{\text{final}} = 3.1a_0$. Hence, large strains are involved. Figure 2 shows the convergence plots obtained for two different nominal strain rates ($\dot{a}/a_0 = 1.0 \cdot 10^{-2}\ \text{s}^{-1}$ and $1.0 \cdot 10^{0}\ \text{s}^{-1}$). The temperature at the inner face of the cylinder is plot- ted vs. the number of equal time steps employed. The performance of the adiabatic split introduced in Section IV.2 is compared with the standard isothermal split and a simul- taneous solution of the problem. In the three cases, the thermal phase is integrated via a backward-Euler scheme, with consistent capacity matrix for the isothermal split. These results demonstrate the good numerical accuracy obtained with the proposed adiabatic split. A slightly better convergence is observed relative to the conventional isothermal split. The difference, however, is rather small.

As already pointed out, conditional stability is the main drawback of the isothermal split that manifests itself in the inability of this split to handle strongly coupled prob- lems in the quasistatic regime. For the thermoelastic problem, an increase of the cou- pling strength (i.e. an increase in the thermal expansion coefficient $\alpha$) results in an unstable performance of the isothermal split. This undesirable behavior is also found

![](./images/812414560513294336_1.jpg)

Fig. 1. Nonlinear thermoplastic thick-walled cylinder. Initial configuration and boundary conditions.

<table>
<caption>Table 1. Nonlinear thermoplastic thick-walled cylinder — Material properties</caption>
<tbody>
<tr>
<td>Bulk modulus</td>
<td>$\kappa$</td>
<td>58.333 GPa</td>
</tr>
<tr>
<td>Shear modulus</td>
<td>$\mu$</td>
<td>26.923 GPa</td>
</tr>
<tr>
<td>Flow stress</td>
<td>$y_0$</td>
<td>0.070 GPa</td>
</tr>
<tr>
<td>Linear hardening</td>
<td>$h$</td>
<td>0.210 GPa</td>
</tr>
<tr>
<td>Density</td>
<td>$\rho_0$</td>
<td>$2700. \, \text{kg/m}^3$</td>
</tr>
<tr>
<td>Expansion coefficient</td>
<td>$\alpha$</td>
<td>$2.38 \cdot 10^{-5} \, \text{K}^{-1}$</td>
</tr>
<tr>
<td>Conductivity</td>
<td>$k$</td>
<td>$150. \, \text{N/sK}$</td>
</tr>
<tr>
<td>Specific capacity</td>
<td>$c_s$</td>
<td>$900. \, \text{m}^2/\text{s}^2\text{K}$</td>
</tr>
<tr>
<td>Flow stress softening</td>
<td>$\omega_0$</td>
<td>$3.0 \cdot 10^{-4} \, \text{K}^{-1}$</td>
</tr>
<tr>
<td>Hardening softening</td>
<td>$\omega_h$</td>
<td>$3.0 \cdot 10^{-4} \, \text{K}^{-1}$</td>
</tr>
</tbody>
</table>

$$
\dot{a}/a_o = 1.0 \cdot 10^{-2} \, s^{-1}
$$

![](./images/812414560513294336_2.jpg)

$$
\dot{a}/a_o = 1.0 \, s^{-1}
$$

![](./images/812414560513294336_3.jpg)

Fig. 2. Nonlinear thermoplastic thick-walled cylinder. Convergence test for two nominal strain rates.

in the presence of physical dissipative mechanisms, in particular, in coupled thermoplas- ticity. Figure 3 shows the evolution in time of the temperature at the inner face of the cylinder when the thermal expansion coefficient is increased to $\alpha=1.4 \cdot 10^{-4} ~K^{-1}$. The nominal strain rate is $\dot{a} / a_{0}=1.0 \cdot 10^{-2} ~s^{-1}$. The unstable behavior of the isothermal split is apparent from this result. Large oscillations appear, which worsen the smaller the time step. By contrast, the adiabatic split does exhibit any indication of numerical instability in this strongly coupled case, while retaining good numerical accuracy when compared to the simultaneous solution. We remark that such a high value of $\alpha$ is not physically realistic. The isothermal split will perform well in most of these coupled ther- momechanical problems, but only because they can be characterized as weakly coupled. Observe that the temperature in Fig. 3 increases in time. This fact indicates that the plas- tic dissipation is still the dominant part of the heat source compared to this enhanced thermoelastic effect, which makes the temperature decrease because the specimen is expanded.

### V.3. Dynamic impact of a thermoplastic cylindrical bar
This example corresponds to the dynamic impact of a three-dimensional bar on a rigid frictionless hot wall. The goal of this problem is to check the performance of the algo- rithms based on the adiabatic split in this dynamic setting.

The bar considered in the simulation has a length of $l_{0}=32.4 ~mm$ and a circular cross section of $r_{0}=3.2 ~mm$. Figure 4 shows the reference mesh. A quarter of the bar is discretized, with 972 isoparametric 8-node trilinear bricks with constant pressure(Q1/P0), following the mixed formulation presented in SIMo, TAYLOR, and PISTER[1985]. Table 2 includes the material properties assumed in the example; linear harden- ing (i.e., $\delta=0$ ) is assumed. The initial velocity of the bar is $v_{0}=0.227 ~mm / \mu s$ along the axis of the cylinder. The temperature at the free face is assumed fixed at the refer-

![](./images/812414560513294336_4.jpg)

Fig. 3. Nonlinear thermoplastic thick-walled cylinder. Evolution of the temperature at the inner face for an artificially enhanced thermal expansion coefficient $\alpha=1.4 \cdot 10^{-4} ~K^{-1}(\dot{a} / a_{0}=1.0 \cdot 10^{-2} ~s^{-1})$.

![](./images/812414560513294336_5.jpg)

Fig. 4. Dynamic impact of a cylindrical bar. Reference configuration.

ence value $\theta_{0}=293.15 \mathrm{~K}$, while the wall temperature is $\bar{\theta}=\theta_{0}+100 \mathrm{~K}$. The lateral face of the bar is assumed to be thermally insulated.

We perform the simulations with both the adiabatic and isothermal splits. In both cases, the dynamical mechanical phase is integrated with the standard Newmark $\alpha=1 / 4$ $\gamma=1 / 2$ algorithm, i.e. trapezoidal rule (we refer to Simo [1992] for a detailed discussion of other alternatives) with a lumped mass matrix. The thermal phase is integrated by a backward-Euler scheme in both simulations. We consider a lumped capacity matrix for the isothermal split, as well. The simulation is carried out for $t \in[0,80] \mu \mathrm{s}$, with equal time increments of $\Delta t=1.25 \mu \mathrm{s}$.

Figure 5 shows the temperature distribution as well as the deformed configurations at $t=40 \mu \mathrm{s}$ and $t=80 \mu \mathrm{s}$, obtained with the adiabatic split. In Figure 6 the maximum radial displacement is plotted vs. time for both simulations. We observe a perfect agreement between both simulations, which permits us to conclude that the presented adiabatic split results in a good numerical accuracy in this dynamic context as well. We note that the same remarks pointed out in the previous Section hold in this case. The isothermal split presents conditional stability in these dynamic simulations; but, as shown in ARMERO and Simo [1992], the stability condition is inversely proportional to the strength of coupling. For these weakly coupled problems, both the isothermal and adiabatic splits will then perform very similarly. The superior stability properties of the adiabatic split become critical, however, in the presence of a stronger coupling.

<table>
<caption>Table 2. Dynamic impact of a cylindrical bar — Material properties</caption>
<tr>
<td>Bulk modulus</td>
<td>$\kappa$</td>
<td>130. GPa</td>
</tr>
<tr>
<td>Shear modulus</td>
<td>$\mu$</td>
<td>43.3333 GPa</td>
</tr>
<tr>
<td>Flow stress</td>
<td>$y_{0}$</td>
<td>0.40 GPa</td>
</tr>
<tr>
<td>Linear hardening</td>
<td>$h$</td>
<td>0.10 GPa</td>
</tr>
<tr>
<td>Density</td>
<td>$\rho_{0}$</td>
<td>8930. kg/m³</td>
</tr>
<tr>
<td>Expansion coefficient</td>
<td>$\alpha$</td>
<td>$1.0 \cdot 10^{-5} \mathrm{~K}^{-1}$</td>
</tr>
<tr>
<td>Conductivity</td>
<td>$k$</td>
<td>45. N/sK</td>
</tr>
<tr>
<td>Specific capacity</td>
<td>$c_{s}$</td>
<td>$460 . \mathrm{m}^{2} / \mathrm{s}^{2} \mathrm{~K}$</td>
</tr>
<tr>
<td>Flow stress softening</td>
<td>$\omega_{0}$</td>
<td>$2.0 \cdot 10^{-3} \mathrm{~K}^{-1}$</td>
</tr>
<tr>
<td>Hardening softening</td>
<td>$\omega_{h}$</td>
<td>$0 . \mathrm{K}^{-1}$</td>
</tr>
</table>

![](./images/812414560513294336_6.jpg)

Fig. 5. Dynamic impact of a cylindrical bar. Relative temperature $(\theta-\theta_{0})$ distribution at (a) $t=40 \mu s$ and (b) $t=80 \mu s$ obtained by adiabatic split. Both deformed configurations are at the same scale.

### V.4. Plane strain, nearly adiabatic shear banding

This final example consists of the plane-strain tensile test of a rectangular bar. It is characterized by the formation of thermally triggered shear bands. For high strain rates, heat conduction is practically nonexistent. This induces a localized over-heating at the center of the bar due to the heat generated by plastic dissipation, resulting in a high local increase of the temperature and strong decrease of the yield stress due to the thermal softening. This softening response triggers the localization of the deformation, and shear bands, at $45^{\circ}$ with the axial direction of loading in this case, appear as the basic deformation mechanism. This phenomenon is normally referred to as "adiabatic" shear banding.

The specimen considered in the numerical simulations has a width of $w_{0}=12.826 \mathrm{~mm}$ and a length of $l_{0}=53.334 \mathrm{~mm}$; plane strain conditions are assumed. Figure 7 depicts

![](./images/812414560513294336_7.jpg)

Fig. 6. Dynamic impact of a cylindrical bar. Maximal radial displacement vs. time.

![](./images/812414560513294336_8.jpg)

Fig. 7. Plane-strain nearly adiabatic shear banding. Initial configuration and boundary conditions.

the mesh of the initial configuration with the assumed boundary conditions. The bar is assumed insulated along its lateral face, while the temperature is kept constant to the reference value $\Theta_0=293.15$ K on the upper and lower faces. Because of the symmetry, a quarter of the specimen is discretized, imposing the corresponding symmetry bound- ary conditions, with 200 4-node isoparametric quad based on the enhanced formulation presented in Simo and ARMERO [1992]. The enhanced strain interpolations are chosen so that, in the linear regime, one recovers the one-point quadrature. For the present example, the nonlinear terms stabilize the spurious modes associated to this technique. Table 3 includes the assumed values of the material properties for this problem. We note that all these values are physically realistic; they correspond to steel. Observe, in par- ticular, the presence of mechanical work hardening, which will be overcome at high strain rates by the (small) thermal softening. We consider the source term $\mathfrak{D}_{int}$ in the energy equation defined as a fraction of the plastic work, with a dissipation factor of $\chi=0.9$. No initial imperfections, neither geometric nor material, are assumed; the final localized pattern of the deformation is triggered by the thermal field alone.

Figure 8 shows the final configuration at an imposed top displacement $\bar{u}=5.0$ mm. The simulations are performed under quasistatic conditions with a staggered algorithm based on the proposed adiabatic split. Two different nominal strain rates are considered:

$$\text{a. } \dot{l}/l_0=4 \cdot 10^{-2} \mathrm{~s}^{-1} \quad \text{and} \quad \text{b. } \dot{l}/l_0=4 \cdot 10^{4} \mathrm{~s}^{-1}.$$

<table>
<caption>Table 3. Plane strain nearly adiabatic shear banding--Material properties</caption>
<tbody>
<tr>
<td>Bulk modulus</td>
<td>$\kappa$</td>
<td>164.206 GPa</td>
</tr>
<tr>
<td>Shear modulus</td>
<td>$\mu$</td>
<td>80.1938 GPa</td>
</tr>
<tr>
<td>Flow stress</td>
<td>$y_0$</td>
<td>0.450 GPa</td>
</tr>
<tr>
<td>Linear hardening</td>
<td>$h$</td>
<td>0.12924 GPa</td>
</tr>
<tr>
<td>Saturation hardening</td>
<td>$y_\infty$</td>
<td>0.715 GPa</td>
</tr>
<tr>
<td>Hardening exponent</td>
<td>$\delta$</td>
<td>16.93</td>
</tr>
<tr>
<td>Density</td>
<td>$\rho_0$</td>
<td>7800. kg/m³</td>
</tr>
<tr>
<td>Expansion coefficient</td>
<td>$\alpha$</td>
<td>$1\cdot10^{-5}\ \text{K}^{-1}$</td>
</tr>
<tr>
<td>Conductivity</td>
<td>$k$</td>
<td>45. N/sK</td>
</tr>
<tr>
<td>Specific capacity</td>
<td>$c_s$</td>
<td>460. m²/s²K</td>
</tr>
<tr>
<td>Flow stress softening</td>
<td>$\omega_0$</td>
<td>$2.0\cdot10^{-3}\ \text{K}^{-1}$</td>
</tr>
<tr>
<td>Hardening softening</td>
<td>$\omega_h$</td>
<td>$2.0\cdot10^{-3}\ \text{K}^{-1}$</td>
</tr>
</tbody>
</table>

The first strain rate leads to a diffuse necking mode, whereas the second strain rate produces sharp shear bands that appear to be well-resolved in the simulation. Figure 9 shows the load/displacement curves obtained for these two strain rates. Table 4 sum- marizes the values of the Euclidean norm of the residual, obtained within typical time increment, in an iterative solution procedure employing Newton's method. The quadratic rate of convergence exhibited by the iteration is the result of an exact linearization of the two symmetric subproblems leading to an exact expression for the algorithmic tan- gent moduli summarized in the Appendix.

## VI. CONCLUDING REMARKS
A general a priori estimate for multiplicative thermoplasticity has been presented and applied to the design of time stepping algorithms that retain the property of uncondi- tional stability by inheriting the a priori stability estimate. The notion of nonlinear numerical stability induced by this estimate does not preclude interesting physical phe- nomena to be expected, such as the formation of shear bands in the presence of ther- mal softening. An unconditionally stable staggered scheme has been constructed within the framework of the classical method of fractional steps via a physically motivated split of the full problem of evolution. In contrast with existing staggered algorithms, the pro- posed scheme inherits the a priori stability estimate while retaining the partitioning of the full coupled problem into two symmetric subproblems. This allows the use of cost- effective numerical linear algebra solutions techniques for symmetric systems.

<table>
<caption>Table 4. Plane strain "adiabatic" shear banding--Residual norms for a typical increment $(\dot{l}/l_0=4\cdot10^4\ \text{s}^{-1})$</caption>
<tbody>
<tr>
<th>Mechanical phase</th>
<th>Thermal phase</th>
</tr>
<tr>
<td>$1.96287\cdot10^{+01}$</td>
<td>$2.41033\cdot10^{+05}$</td>
</tr>
<tr>
<td>$1.13417\cdot10^{-02}$</td>
<td>$2.00488\cdot10^{+02}$</td>
</tr>
<tr>
<td>$1.08594\cdot10^{-05}$</td>
<td>$1.48953\cdot10^{-04}$</td>
</tr>
<tr>
<td>$5.09266\cdot10^{-10}$</td>
<td>$6.13528\cdot10^{-09}$</td>
</tr>
</tbody>
</table>

![](./images/812414560513294336_9.jpg)

Fig. 8. Plane-strain, nearly adiabatic shear banding. Relative temperature $(\theta-\theta_{0})$ and equivalent plastic strain $(\xi)$ distributions at $\bar{u}=5.0$ mm for two different nominal strain rates: (a) $\dot{l}/l_{0}=4 \cdot 10^{-2} \mathrm{~s}^{-1}$, (b) $\dot{l}/l_{0}=4 \cdot 10^{4} \mathrm{~s}^{-1}$. (Notice the different scales between (a) and (b)).

The implementation of staggered algorithms based on the proposed split entails only minor modifications of widely used staggered techniques. The numerical examples described in Section V demonstrate the effectiveness of these algorithms in the solution of a wide class of problems, both in the quasistatic and dynamic regimes, and in situa-

![](./images/812414560513294336_10.jpg)

Fig. 9. Plane-strain nearly adiabatic shear banding. Load/displacement curves.

situations where strain localization arises as a result of thermoplastic softening. The cost involved is essentially identical to that of conventional methods, symmetry of the two subproblems is preserved, and good accuracy is achieved without upsetting the key prop- erty of unconditional stability.

It should be emphasized that the operator split methods proposed here fall within framework of the classical method of fractional steps, and are used in the design of effective integrators in time. On the other hand, spatial operator split methods, of the type used in classical ADI and domain decomposition methods (see e.g. GLOWINSKI & LE TALLEC [1989]), have been exploited by ORTIZ, PINSKY, and TAYLOR [1983] and HUGHES, LEVIT, and WINGET [1983a] in the design of spatial element-by-element tech- niques. Contrary to the present methods, these latter techniques appear to experience accuracy limitations arising from conditional consistency; see the Epilogue in HUGHEs, LEVIT, and WINGET [1983b].

Acknowledgements-Support for this research was provided by NSF under Grant no. 2-DJA2-544 with Stan- ford University. This support is gratefully acknowledged.

## REFERENCES

1911 DUHEM, P., Traité d'Energetique ou de Thermodynamique Générale, Gauthier Villars, Paris.
1933 TAYLOR, G.I., and QUINNEY, M.A., "The Latent Energy Remaining in a Metal after Cold Working," Proc. Roy. Soc. Lond., A143, 307.
1950 HILL, R., The Mathematical Theory of Plasticity, Clarendon, Oxford.
1965 TRUESDELL, C., and NOLL, W., "The Nonlinear Field Theories of Mechanics," in FLUEGGE, S., (ed.), Handbuch der Physik Bd. III/3, Springer-Verlag, Berlin.
1966 ERICKSEN, J.L., "Thermoelastic Stability," Proc. 5th National Cong. Appl. Mech., 187.
1967 COTTRELL, A.H., "Dislocations & Plastic Flow in Crystals," Oxford University Press, London.
1967 LEE, E.H., and LIU, D.T., "Finite Stain Elastic-Plastic Theory Particularly for Plane Wave Analy- sis," Journal of Applied Physics, 38.
1967 RICHTMYER, R.D., and MORTON, K.W., Difference Methods for Initial Value Problems, 2nd edition, Interscience, New York.
1969 LEE, E.H., "Elastic-plastic Deformation at Finite Strains," Journal of Applied Mechanics, 36, 1.

1969 STRANG, G., "Approximating Semigroups and the Consistency of Difference Schemes," Proc. Am. Math. Soc. 20, 1.

1971 YANENKO, N.N., The Method of Fractional Steps, Springer Verlag, New York.

1972 HILL, R., and RICE, J.R., "Constitutive Analysis of Elastic-Plastic Crystals at Arbitrary Strains," J. Mech. Phys. Sol. 20, 401.

1973 BEVER, M.B., HOLT, D.L., and TITCHENER, A.L., The Stored Energy of Cold Work, Pergamon Press, Tarrytown, NY.

1974 MANDEL, J., "Thermodynamics and Plasticity," in DELGADO DOMINGERS, J.J., NINA, N.R., and WHITELAW, J.H. (eds.), Foundations of Continuum Thermodynamics, Macmillan, London, pp. 283-304.

1975 GURTIN, M.E., "Thermodynamics and Stability," Arch. Rational Mech. Anal. 59, 53.

1976 DAFERMOS, C.M., "Contraction Semigroups and Trend to Equilibrium in Continuum Mechanics," Springer Lecture Notes in Math., 503, 295.

1977 PARK, K.C., FELIPPA, C.A., and DERUNTZ, J.A., "Stabilization of Staggered Solution Procedures for Fluid-Structure Interaction Analysis," in BELYTSCHKO, T., and GEERS, T.L. (eds.), Computational Methods for Fluid-Structure Interaction Problems, ASME Applied Mechanics Symposia Series, AMD 26, pp. 94-124.

1978 CIARLET, P.G., The Finite Element Method for Elliptic Problems, North Holland, Amsterdam.

1979 ANAND, L., "On H. Henky's Approximate Strain-Energy Function for Moderate Deformations," J. App. Mech. 46, 78.

1979 TEMAM, R., The Navier-Stokes Equations, 2nd ed. Studies in Mathematics and its Applications, North- Holland, Amsterdam.

1980 CLIFTON, R.J., "Adiabatic Shear Banding," in Materials Response to Ultra-High Strain Rates, Chap. 8, in NMAB-356, National Materials Advisory Board (NRC), Washington DC.

1981 ARGYRIS, J.H., and DOLTSINIS, J.ST., "On the Natural Formulation and Analysis of Large Defor- mation Coupled Thermomechanical Problems," Computer Methods in Applied Mechanics and Engi- neering, 25, 195.

1983 ASARO, R., "Micromechanics of Crystals and Polycrystals," in Wu, T.Y., and HUTCHINSON, J.W. (eds.), Advances in Applied Mechanics 23, 1.

1983a HUGHES, T.J.R., LEVIT, I., and WINGET, J., "Element-by-Element Implicit Algorithms for Heat Con- duction," J. Eng. Mech., 109, 110.

1983b HUGHES, T.J.R., LEVIT, I., and WINGET, J., "An Element-by-Element Solution Algorithm for Prob- lems of Structural and Solid Mechanics," Computer Methods in Applied Mechanics and Engineer- ing, 36, 241.

1983 MOLINARI, A., and CLIFTON, R.J., "Localisation de la Déformation Viscoplastiqueen Cisaillement Simple: Résultats Exacts en Théorie Non Linéaire," Comptes Rendu de l'Academie des Sciences, Ser. II 296, 1.

1983 ORTIZ, M., PINSKY, P.M., and TAYLOR, R.L., "Unconditionally Stable Element-by-Element Algorithms for Dynamic Problems," Computer Methods in Applied Mechanics and Engineering, 36, 223.

1983 PARK, K.C., and FELIPPA, C.A., "Partitioned Analysis of Coupled Problems," in BELYTSCHKO, T., and HUGHES, T.J.R. (eds.), Computational Methods in Transient Analysis, North Holland, Amsterdam.

1984 DAFALIAS, Y.F., "A Missing Link in the Formulation and Numerical Implementation of Finite Trans- formation Elastoplasticity," in WILLAM, K.J. (ed.), Constitutive Equations: Macro and Computational Aspects, ASME.

1984 HUGHES, T.J.R., "Numerical Implementation of Constitutive Models: Rate Independent Deviatoric Plasticity," in NEMAT-NASSER, S., ASARO, R., and HEGEMIER, G. (eds.), Theoretical Foundations for Large Scale Computations of Nonlinear Material Behavior, Martinus Nijhoff Publishers, The Netherlands.

1984 NEEDLEMAN, A., and TVERGAARD, V., "Finite Element Analysis of Localization Plasticity," in ODEN, J.T., and CAREY, G.F. (eds.), Finite Elements, Vol V: Special Problems in Solid Mechanics, Prentice- Hall, Englewood Cliffs, NJ.

1985 ANAND, L., "Constitutive Equations for Hot Working of Metals," Int. J. Plasticity, 1, 213.

1985 SIMO, J.C., "On the Computational Significance of the Intermediate Configuration and Hyperelas- tic Stress Relations in Finite Deformation Elastoplasticity," Mech. Mat., 4, 439.

1985 SIMO, J.C., TAYLOR, R.L., and PISTER, K.S., "Variational and Projection Methods for the Volume Constraint in Finite Deformation Elasto-Plasticity," Comp. Meth. Appl. Mech. Eng., 51, 177.

1985 TEMAM, R., "A Generalized Norton-Hoff Model and the Prandtl-Reuss Law of Plasticity," Arch. Rational Mech. Anal., 137.

1985 TEMAM, R., Mathematical Problems in Plasticity, Gauthier-Villars, Paris.

1986 BALL, J.M., and KNOWLES, G., "Lyapunov Functions for Thermomechanics with Spatially Varying Boundary Temperatures," Archive for Rational Mechanics and Analysis, 92, 193.

1986 LUBLINER, J., "Normality Rules in Large-Deformation Plasticity," Mechanics of Materials, 5, 29.

1987 ANAND, L., KIM, K.H., and SHAWKI, T.G., "Onset of Shear Localization in Viscoplastic Solids," J. Mech. Phys. Sol., 35, 407.

1987
ZDEBEL, U., and LEHMANN, T., "Some Theoretical Considerations and Experimental Investigations on a Constitutive Law in Thermoplasticity," Int. J. Plasticity, 3, 369.

1989
BoYCE, M.C., WEBBER, G.G., and PARKs, D.M., "On the Kinematics of Finite Strain Plasticity," J. Mech. Phys. Sol., 37, 647.

1989
DEMENGEL, F., "Compactness Theorems for Spaces of Functions with Bounded Derivatives and Appli- cations to Limit Analysis Problems in Plasticity," Arch. Rational Mech. Anal., 105, 123.

1989
GLOWINSKI, R., and LE TALLEC, P., Augmented Lagrangian and Operator-Splitting Methods in Non- linear Mechanics, SIAM Studies in Applied Mathematics, Philadelphia.

1989
SHAWKI, T.G., and CLIFTON, R.J., "Shear Band Formation in Thermal Viscoplastic Materials," Mech. Mat., 8, 13.

1990
DOLTSINIs, I.ST., "Aspects of Modeling and Computation in the Analysis of Metal Forming," Engi- neering Computations, 7, 2.

1990
LUBLINER, J., Plasticity Theory, MacMillan, London.

1990
MORAN, B., ORTIZ, M., and SHIH, C.F., "Formulation of Implicit Finite Element Methods for Multi- plicative Deformation Plasticity," Int. J. Num. Meth. Eng., 29, 483.

1991
FARHAT, C., PARK, K.C., and DUBOIS-PELERIN, Y., "An Unconditionally Stable Staggered Algorithm for Transients Finite Element Analysis of Coupled Thermoelastic Problems," Comp. Meth. Appl. Mech. Eng., 85, 349.

1991
HAIRER, E., and WANNER, G., Solving Ordinary Differential Equations II, Springer Series in Com- putational Mathematics, Vol. 14, Springer-Verlag, Berlin.

1991
HARREN, S.V., "The Finite Deformation of Rate-Dependent Polycrystals-I. A Self-Consistent Frame- work," J. Mech. Phys. Sol., 39, 345.

1991
SImo, J.C., "Nonlinear Stability of the Time Discrete Variational Problem in Nonlinear Heat Con- duction and Elastoplasticity," Computer Methods in Applied Mechanics and Engineering, 88, 111.

1992
ARMERO, F., and SImo, J.C., "A New Unconditionally Stable Fractional Step Method for Nonlin- ear Coupled Thermomechanical Problems," Int. J. Num. Meth. Eng., 35, 737.

1992
MORAN, B., ORTIZ, M., and SHIH, C.F., "An Analysis of Cracks in Ductile Single Crystals-I. Anti- Plane Shear," J. Mech. Phys. Sol., 40, 291.

1992
SImo, J.C., "Algorithms for Static and Dynamic Multiplicative Plasticity that Preserve the Classi- cal Return Mapping Schemes of the Infinitesimal Theory," Computer Methods in Applied Mechan- ics and Engineering, 99, 61.

1992
SImo, J.C., and MIEHE, C., "Associative Coupled Thermoplasticity at Finite Strains: Formulation, Numerical Analysis and Implementation," Comp. Meth. Appl. Mech. Eng., 98, 41.

1992
SImo, J.C., and ARMERO, F., "Geometrically Nonlinear Enhanced Strain Mixed Methods and the Method of Incompatible Modes," Int. J. Num. Meth. Eng., 33, 1413.

Division of Applied Mechanics
Department of Mechanical Engineering
Stanford University, Stanford, CA 94305

(Received 6 April 1992; in final revised form 12 April 1993)

## APPENDIX: IMPLEMENTATION OF A FRACTIONAL STEP

This Appendix outlines the implementation of a staggered scheme based on the adi- abatic split (35) for the model of $J_{2}$-flow theory summarized in Box 1 of Section V. The goal is to illustrate the application of the proposed methodology in a specific example to gain further insight into the algorithmic issues involved. Each of the two phases, the split, mechanical phase and thermal phase, is discussed separately. The implementation employs a new class of return mapping algorithms, recently proposed in Simo [1992] in the context of the purely mechanical theory, which can accommodate any return map of infinitesimal plasticity with no modification. The return map is performed here in the principal axes defined by the trial step. The reader is directed to this reference for further elaboration and a detailed derivation of the expressions quoted below.

### I.1. Mechanical (isentropic) phase

Because the model outlined in Box 1 is restricted to isotropy, the internal variables are $\bar{\chi}=\{\mathbf{b}^{e}, \xi, \eta^{p}\}$. At time $t_{n}$ in a typical time increment $[t_{n}, t_{n+1}]$, the primary vari

ables $\{\boldsymbol{\varphi}_{n}, \boldsymbol{\theta}_{n}\}$ and the internal variables $\{\mathbf{b}_{n}^{e}, \xi_{n}, \eta_{n}^{p}\}$ are given. In this phase of the product formula, one solves for the current configuration $\boldsymbol{\varphi}_{n+1}$ via an iterative procedure in which the current iterate is assumed given. The computation of the new iterate involves the evaluation of the current (Kirchhoff) stresses $\boldsymbol{\tau}_{n+1}$ and of the updated internal variables $\{\tilde{\mathbf{b}}_{n}^{e}, \tilde{\xi}_{n}, \tilde{\eta}_{n}^{p}\}$. Given a finite element discretization, this update is performed at each quadrature point and proceeds as follows.

Step 1. Trial state (kinematics). Compute the relative deformation gradient $\mathbf{f}_{n+1}$:
$$
\mathbf{f}_{n+1}=\nabla \mathbf{x}_{n}\left(\boldsymbol{\varphi}_{n+1} \circ \boldsymbol{\varphi}_{n}^{-1}\right)=\mathbf{I}_{3}+\nabla \mathbf{x}_{n} \mathbf{u}_{n+1},
\tag{45}
$$
where $\mathbf{x}_{n}:=\boldsymbol{\varphi}_{n}(\mathbf{X})$, $\mathbf{u}_{n+1}=\hat{\mathbf{u}}_{n+1}(\mathbf{x}_{n})$ is the current displacement field and $\mathbf{I}_{3}$ is the $3 \times 3$ identity matrix. The current Jacobian is obtained as $J_{n+1}=J_{n} \det[\mathbf{f}_{n+1}]$. Compute the trial elastic left Cauchy-Green tensor (with frozen plastic flow) as
$$
\mathbf{b}_{n+1}^{e \operatorname{tr}}:=\mathbf{f}_{n+1} \mathbf{b}_{n}^{e} \mathbf{f}_{n+1}^{T}.
\tag{46}
$$

Step 2. Spectral decomposition of $\mathbf{b}_{n+1}^{e \operatorname{tr}}$. Compute the trial elastic principal stretches $\{\lambda_{A_{n+1}}^{e \operatorname{tr}}\}$ by solving the cubic characteristic equation in closed form via Cardano's formulae. Compute the principal directions $\{\mathbf{n}_{n+1}^{\operatorname{tr}(A)}\}$ via the closed form formula
$$
\mathbf{n}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{n}_{n+1}^{\operatorname{tr}(A)}=\left[\frac{\mathbf{b}_{n+1}^{e \operatorname{tr}}-\left(\lambda_{B_{n+1}}^{e \operatorname{tr}}\right)^{2} \mathbf{I}_{3}}{\left(\lambda_{B_{n+1}}^{e \operatorname{tr}}\right)^{2}-\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{2}}\right]\left[\frac{\mathbf{b}_{n+1}^{e \operatorname{tr}}-\left(\lambda_{C_{n+1}}^{e \operatorname{tr}}\right)^{2} \mathbf{I}_{3}}{\left(\lambda_{C_{n+1}}^{e \operatorname{tr}}\right)^{2}-\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{2}}\right],
\tag{47}
$$
for $A=1,2,3$, with $B=1+\bmod (3, A)$ and $C=1+\bmod (3, B)$. If multiple roots appear when solving for the principal stretches, a perturbation of the repeated roots is introduced before applying formula (47).

Step 3. Trial Kirchhoff stress. Evaluation of the elastic constitutive equation $(18)_{1}$ for the internal energy function (44a) results in the following expression of the trial Kirchhoff stresses
$$
\left.
\begin{array}{c}
\boldsymbol{\tau}_{n+1}^{\operatorname{tr}}=J_{n+1} p_{n+1}^{\operatorname{tr}} \mathbf{I}_{3}+\mathbf{s}_{n+1}^{\operatorname{tr}}, \\
p_{n+1}^{\operatorname{tr}}=\left[\kappa \log J_{n+1}-3 \kappa \alpha\left(\hat{\boldsymbol{\theta}}\left(J_{n+1}, \xi_{n}, \eta_{n}^{e}\right)-\theta_{0}\right)\right] / J_{n+1}, \\
\mathbf{s}_{n+1}^{\operatorname{tr}}:=\operatorname{dev}\left[\boldsymbol{\tau}_{n+1}^{\operatorname{tr}}\right]=\sum_{A=1}^{3} \bar{\sigma}_{A_{n+1}}^{\operatorname{tr}} \mathbf{n}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{n}_{n+1}^{\operatorname{tr}(A)}, \\
\bar{\sigma}_{A_{n+1}}^{\operatorname{tr}}=2 \mu \log \left[\bar{\lambda}_{A_{n+1}}^{e \operatorname{tr}}\right],
\end{array}
\right\}
\tag{48}
$$
with $\bar{\lambda}_{A_{n+1}}^{e \operatorname{tr}}:=J_{n+1}^{-1 / 3} \lambda_{A_{n+1}}^{e \operatorname{tr}}$ and the explicit function
$$
\hat{\boldsymbol{\theta}}\left(J, \xi, \eta^{e}\right)=\theta_{0} \exp \left[\left(\eta^{e}-3 \kappa \alpha \log J+K_{\theta}(\xi)\right) / c_{0}\right],
\tag{49}
$$
where $K_{\theta}(\xi)$ is given by (44b). The elastic entropy $\eta_{n}^{e}$ at $t_{n}$ is given in closed form by (43) as $\eta_{n}^{e}=\hat{\eta}^{e}(J_{n}, \theta_{n}, \xi_{n})$.

Step 4. Yield condition. Check plastic loading by evaluating the yield function at the trial state:
$$
\phi_{n+1}^{\operatorname{tr}}\left(\boldsymbol{\tau}_{n+1}^{\operatorname{tr}}, \xi_{n}, \theta_{n}\right)=\sqrt{\frac{3}{2}}\left\|\mathbf{s}_{n+1}^{\operatorname{tr}}\right\|+\beta_{n}-y_{0}\left(\theta_{n}\right),
\tag{50}
$$

where the conjugate hardening variable $\beta_n$ is computed explicitly as in Box 1. The norm in (50) is easily obtained as

$$
\left\|\mathbf{s}_{n+1}^{\mathrm{tr}}\right\|=\left[\sum_{A=1}^{3}\left(\bar{\sigma}_{A_{n+1}}^{\mathrm{tr}}\right)^{2}\right]^{1 / 2} \tag{51}
$$

If $\phi_{n+1}^{\mathrm{tr}} \leq 0$, set $(\cdot)_{n+1}=(\cdot)_{n+1}^{\mathrm{tr}}$ and go to step 6.

Step 5. Return mapping. To enforce consistency, solve for $\Delta \gamma_{n+1}$ the equations

$$
\left.\begin{array}{c}
\sqrt{\frac{3}{2}}\left\|\mathbf{s}_{n+1}^{\mathrm{tr}}\right\|-3 \mu \Delta \gamma_{n+1}+\beta_{n+1}-y_{0}\left(\theta_{n}\right)=0, \\
\beta_{n+1}=-K_{\xi}\left(\xi_{n+1}, \hat{\theta}\left(J_{n+1}, \xi_{n+1}, \eta_{n}^{e}\right)\right), \\
\xi_{n+1}=\xi_{n}+\Delta \gamma_{n+1},
\end{array}\right\} \tag{52}
$$

where an explicit expression of $(52)_2$ is given in Box 1. The solution of this nonlinear system of equations is performed via Newton's method; the linearization involved in such strategy becomes straightforward because an explicit closed form expression is available for all the functions involved.

The final Kirchhoff stress at $t_{n+1}$ is computed by performing the classical radial return projection in principal directions as

$$
\left.\begin{array}{c}
\boldsymbol{\tau}_{n+1}=J_{n+1} p_{n+1} \mathbf{I}_{3}+\mathbf{s}_{n+1}, \\
p_{n+1}=\left[\kappa \log J_{n+1}-3 \kappa \alpha\left(\hat{\theta}\left(J_{n+1}, \xi_{n+1}, \eta_{n}^{e}\right)-\theta_{0}\right)\right] / J_{n+1}, \\
\mathbf{s}_{n+1}:=\operatorname{dev}\left[\boldsymbol{\tau}_{n+1}\right]=\sum_{A=1}^{3} \bar{\sigma}_{A_{n+1}} \mathbf{n}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{n}_{n+1}^{\operatorname{tr}(A)}, \\
\bar{\sigma}_{A_{n+1}}=\bar{\sigma}_{A_{n+1}}^{\operatorname{tr}}-2 \mu \sqrt{\frac{3}{2}} \Delta \gamma_{n+1} \bar{\nu}_{A_{n+1}}, \\
\bar{\nu}_{A_{n+1}}=\bar{\nu}_{A_{n+1}}^{\operatorname{tr}}=\bar{\sigma}_{A_{n+1}}^{\operatorname{tr}} /\left\|\mathbf{s}_{n+1}^{\operatorname{tr}}\right\| .
\end{array}\right\} \tag{53}
$$

The updated internal variable $\mathbf{b}_{n+1}^{e}$ is obtained explicitly as

$$
\mathbf{b}_{n+1}^{e}=\sum_{A=1}^{3} \lambda_{A_{n+1}}^{e} \mathbf{n}_{n+1}^{\operatorname{tr}(A)}, \quad \lambda_{A_{n+1}}^{e}=\exp \left[-\sqrt{\frac{3}{2}} \Delta \gamma_{n+1} \bar{\nu}_{A_{n+1}}\right] \lambda_{A_{n+1}}^{e \operatorname{tr}} . \tag{54}
$$

Note, however, that this $\mathbf{b}_{n+1}^{e}$ is not needed in the final implementation. The final updated value is computed in the thermal phase.

Step 6. Exact algorithmic tangent moduli. It can be shown that the linearization of the preceding algorithm takes the following closed-form expression:

$$
\mathbf{c}_{n+1}=\sum_{A=1}^{3} \sum_{B=1}^{3} a_{A B_{n+1}}^{e p} \mathbf{m}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{m}_{n+1}^{\operatorname{tr}(B)}+2 \sum_{A=1}^{3} \sigma_{A_{n+1}} \mathbf{c}_{n+1}^{\operatorname{tr}(A)}. \tag{55}
$$

where $\sigma_{A_{n+1}}=\bar{\sigma}_{A_{n+1}}+J_{n+1} p_{n+1}$ and $\mathbf{m}_{n+1}^{\operatorname{tr}(A)}=\mathbf{n}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{n}_{n+1}^{\operatorname{tr}(A)}$. The moduli $\mathbf{c}_{n+1}^{\operatorname{tr}(A)}$ are independent of the plasticity model and are given by:

$$
\begin{aligned}
\mathbf{c}_{n+1}^{\operatorname{tr}(A)}= & \frac{1}{d_{A}}\left[\mathbf{I}_{b^{e \operatorname{tr}}}-\mathbf{b}_{n+1}^{e \operatorname{tr}} \otimes \mathbf{b}_{n+1}^{e \operatorname{tr}}-I_{3}\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{-2}\left[\mathbf{I}-\left(\mathbf{1}-\mathbf{m}_{n+1}^{\operatorname{tr}(A)}\right) \otimes\left(\mathbf{1}-\mathbf{m}_{n+1}^{\operatorname{tr}(A)}\right)\right]\right] \\
& +\frac{\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{2}}{d_{A}}\left[\left[\mathbf{b}_{n+1}^{e \operatorname{tr}} \otimes \mathbf{m}_{n+1}^{\operatorname{tr}(A)}+\mathbf{m}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{b}_{n+1}^{e \operatorname{tr}}\right]\right. \\
& \left.+\left(I_{1}-4\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{2}\right) \mathbf{m}_{n+1}^{\operatorname{tr}(A)} \otimes \mathbf{m}_{n+1}^{\operatorname{tr}(A)}\right],
\end{aligned}
$$

where $I_{b}^{i j k l}:=\frac{1}{2}\left[b^{i k} b^{j l}+b^{i l} b^{j k}\right], d_{A}:=\left[\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{2}-\left(\lambda_{B_{n+1}}^{e \operatorname{tr}}\right)^{2}\right]\left[\left(\lambda_{A_{n+1}}^{e \operatorname{tr}}\right)^{2}-\left(\lambda_{C_{n+1}}^{e \operatorname{tr}}\right)^{2}\right]$, $I_{1}=\operatorname{tr}\left[\mathbf{b}_{n+1}^{e \operatorname{tr}}\right]$ and $I_{3}=J_{n+1}^{2}$.

The coefficients $\mathbf{a}_{n+1}^{e p}:=\left[a_{A B_{n+1}}^{e p}\right]$ are included in Box 2, where we have made use of the notation $\hat{\Theta}_{n+1}=\hat{\Theta}\left(J_{n+1}, \xi_{n+1}, \eta_{n}^{e}\right), \overline{\boldsymbol{\nu}}=\left[\bar{\nu}_{A_{n+1}}\right]$ and $\mathbf{1}_{3}=[111]^{T}$. We observe that for an elastic step the moduli reduce to the adiabatic elasticities. For a plastic step there are, in general, coupling terms between the plastic contributions and the volumetric part. For the case $K_{\Theta \xi}(\xi) \equiv 0$, however, the tangent has the same form as in the uncoupled theory, with the elastic contributions given by the adiabatic elasticities.

Remark I.1. According to equation $(38)_{4}$, the plastic entropy $\tilde{\eta}_{n+1}^{p}$ is given by $\tilde{\eta}_{n+1}^{p}=$ $\eta_{n}^{p}$. The physical implication of this relation is that thermal softening (the mechanism associated to the change of plastic entropy) is not introduced in the mechanical phase. Numerically, this condition is implemented merely by evaluating the yield stress at $\Theta_{n}$ (i.e., $y_{0}\left(\Theta_{n}\right)$ ) in the equations above. As noted in Section IV, this is the crucial property that renders symmetric the present return mapping algorithm. If consistency were enforced with a yield stress $y_{0}\left(\tilde{\Theta}_{n+1}\right)$ (i.e. accounting for thermal softening, so that $\tilde{\eta}_{n+1}^{p} \neq \eta_{n}^{p}$ ) a nonsymmetric contribution to the tangent stiffness matrix would result. In fact, a direct calculation shows that the last term in the thermoplastic tangent in Box 2 would be replaced by the nonsymmetric contribution $\left(\hat{\Theta}_{n+1} / c_{0} \bar{\delta}_{3}\right) \overline{\boldsymbol{\rho}}_{n+1} \otimes \boldsymbol{\rho}_{n+1}$ where

$$
\left.\begin{array}{l}
\overline{\boldsymbol{\rho}}_{n+1}=-3 \kappa \alpha \mathbf{1}_{3}+\sqrt{\frac{2}{3}} \frac{\left[K_{\Theta \xi}\left(\xi_{n+1}\right)+y_{0}^{\prime}\left(\Theta_{n+1}\right)\right]}{\delta_{0}} \overline{\boldsymbol{\nu}}_{n+1} \\
\bar{\delta}_{3}=1+\frac{K_{\Theta \xi}\left(\xi_{n+1}\right)\left[K_{\Theta \xi}\left(\xi_{n+1}\right)+y_{0}^{\prime}\left(\Theta_{n+1}\right)\right]}{3 \mu} \frac{\hat{\Theta}_{n+1}}{c_{0} \delta_{0}}
\end{array}\right\}
$$

with $\boldsymbol{\rho}_{n+1}$ and $\delta_{0}$ as defined in Box 2.

### I.2. Thermal phase

This phase involves the solution of the energy equation $(40)_{3}$ for the temperature $\Theta_{n+1}$, while the configuration $\boldsymbol{\varphi}_{n+1}$ is kept constant to the converged value in the previous mechanical phase. In an iterative solution scheme, for a given iterate $\Theta_{n+1}^{(k)}$ the computation of the new estimate involves the evaluation of the source term corresponding to the plastic dissipation $\mathfrak{D}_{\text {mech } n+1}^{p}$ (from the converged solution at $t_{n}$ ). As indicated

## BOX 2: Consistent algorithmic tangent

- Elastic step. ($\phi_{n+1}^{\text{tr}} \leq 0$)

$$
\mathbf{a}_{n+1}^{e p} = \left[\kappa + \frac{(3\kappa\alpha)^2 \hat{\Theta}_{n+1}}{c_0}\right] \mathbf{1}_3 \otimes \mathbf{1}_3 + 2\mu\left[\mathbf{I}_3 - \frac{1}{3}\mathbf{1}_3 \otimes \mathbf{1}_3\right]
$$

- Plastic step. ($\phi_{n+1}^{\text{tr}} > 0$)

$$
\begin{aligned}
\mathbf{a}_{n+1}^{e p} &= \kappa \mathbf{1}_3 \otimes \mathbf{1}_3 + 2\mu\left[\delta_1\left(\mathbf{I}_3 - \frac{1}{3} \mathbf{1}_3 \otimes \mathbf{1}_3\right) - \delta_2 \bar{\boldsymbol{\nu}}_{n+1} \otimes \bar{\boldsymbol{\nu}}_{n+1}\right] \\
&+ \frac{\hat{\Theta}_{n+1}}{c_0 \delta_3} \boldsymbol{\rho}_{n+1} \otimes \boldsymbol{\rho}_{n+1}
\end{aligned}
$$

where
$$
\boldsymbol{\rho}_{n+1} = -3\kappa\alpha \mathbf{1}_3 + \sqrt{\frac{2}{3}} \frac{K_{\Theta\xi}(\xi_{n+1})}{\xi_0} \bar{\boldsymbol{\nu}}_{n+1}
$$

$$
\delta_0 = 1 + \frac{K_{\xi\xi}(\xi_{n+1}, \hat{\Theta}_{n+1})}{3\mu}
$$

$$
\delta_1 = 1 - \sqrt{\frac{3}{2}} \frac{2\mu \Delta \gamma_{n+1}}{\left\|\mathbf{s}_{n+1}^{\text{tr}}\right\|}
$$

$$
\delta_2 = \frac{1}{\delta_0} - (1 - \delta_1)
$$

$$
\delta_3 = 1 + \left[K_{\Theta\xi}(\xi_{n+1})\right]^{2/3} \mu \frac{\hat{\Theta}_{n+1}}{c_0 \delta_0}
$$

in Section IV.2.2. this computation is performed via the same isothermal return mapping algorithm, with configuration and temperature fixed at $\{\boldsymbol{\varphi}_{n+1}, \Theta_{n+1}^{(k)}\}$, leading eventually to the final updated values $\{\mathbf{b}_{n+1}^e, \xi_{n+1}\}$. This iterative update is performed again at each quadrature point and has the same structure as its isentropic counterpart described in the previous Section. In particular, the algorithm follows exactly the same steps; only the following considerations need to be made.

1. Steps 1 and 2 need only be performed once during this phase, since $\mathbf{f}_{n+1}$ and $\mathbf{b}_{n}^e$ remain frozen.
2. Steps 3 to 5 have the same expressions, with the only exception that now both $\Theta_n$ and $\hat{\Theta}(\cdot)$ (i.e. eqn 49) have to be replaced by the current value $\Theta_{n+1}$.

3. Step 6 is not needed, because the linearization of the stresses is not required for solving the energy equation $(40)_3$. Instead, compute the mechanical plastic dissipation via (41), i.e.

$$
\mathcal{D}_{\mathrm{mech}, n+1}^{p}=\Delta \gamma_{n+1} y_{0}\left(\theta_{n+1}\right) / \Delta t, \tag{58}
$$

and its linearization as

$$
\partial_{\theta} \mathcal{D}_{\mathrm{mech}, n+1}^{p}=\left[\Delta \gamma_{n+1} y_{0}^{\prime}\left(\theta_{n+1}\right)-y_{0}\left(\theta_{n+1}\right) \frac{y_{0}^{\prime}\left(\theta_{n+1}\right)+K_{\theta \xi}\left(\xi_{n+1}\right)}{3 \mu \delta_{0}}\right] / \Delta t, \tag{59}
$$

where $\delta_0$ is defined in Box 2.