![](./images/812353532148580352_1.jpg)

Available online at www.sciencedirect.com

![](./images/812353532148580352_2.jpg)

Acta Materialia 52 (2004) 3435-3446

![](./images/812353532148580352_3.jpg)

www.actamat-journals.com

# On the fracture toughness of ferroelectric ceramics with electric field applied parallel to the crack front

Jianxin Wang, Chad M. Landis *

Department of Mechanical Engineering and Materials Science, MS 321, Rice University, P.O. Box 1892, Houston, TX 77251-1892, USA

Received 16 February 2004; received in revised form 23 March 2004; accepted 26 March 2004
Available online 24 April 2004

## Abstract
Mode I steady crack growth is analyzed to determine the toughening due to domain switching in ferroelectric ceramics with electric field applied parallel to the crack front. A multi-axial, electromechanically coupled, incremental constitutive theory is applied to model the material behavior of the ferroelectric ceramic. The constitutive law is then implemented within the finite element method to study steady crack growth. The effects of electric field on the fracture toughness of both initially unpoled and poled materials are investigated. Results for the predicted fracture toughness, remanent strain and remanent polarization distributions, and domain switching zone shapes and sizes are presented. The effects of the plane-strain constraint and transverse stress are also established. Finally, the model predictions are discussed in comparison to recent experimental observations.

© 2004 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Fracture toughness; Finite element methods; Ferroelectrics; Piezoelectrics; Domain switching

---

## 1. Introduction
Ferroelectric materials are widely used as actuators and sensors in smart structure applications due to their prominent electromechanical coupling features. Since these devices often operate under strong mechanical and electrical loading conditions, the brittle ferroelectric material is susceptible to fracture. Hence, an understanding of ferroelectric fracture is a key issue for the efficient and reliable design of these devices. There have been numerous experimental investigations on the fracture toughness of ferroelectric ceramics, [1-8], and it is commonly accepted that domain switching leads to increased toughening and R-curve behavior in these materials. It is also well known that both electric field and mechanical stress drive the domain switching process and hence fracture in ferroelectrics is inherently a coupled electromechanical process. The present paper aims to investigate the detailed electromechanical fields near growing cracks in ferroelectrics and to determine the effects of electric field applied parallel to the crack front on the toughness enhancement due to domain switching in these materials.

This work is motivated by recent experimental and theoretical investigations on the effects of electric field on the fracture toughness of ferroelectrics. The investigations presented here have focused on the specific case where the electric polarization and electric field in the sample are in the out-of-plane direction parallel to the crack front as illustrated in Fig. 1. Meschke et al. [5] and Kolleck et al. [6] have observed experimentally that the steady state fracture toughness of ferroelectrics increases with the increase of applied electric field for an initially unpolarized specimen. Additionally, Lucato et al. [7] and Hackemann and Pfeiffer [8] have observed that out-of-plane poling has practically no effect on the fracture toughness of ferroelectrics when the out-of-plane electric field is zero. Recent theoretical explanations of these phenomena have focused on the role of domain switching in the toughening process. Kolleck et al. [6] and Yang et al. [9] treat domain switching with the concepts developed for transformation toughening in

*Corresponding author. Tel.: +1-713-348-3609; fax: +1-713-348-5423.
E-mail address: landis@rice.edu (C.M. Landis).

1359-6454/$30.00 © 2004 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.actamat.2004.03.041

![](./images/812353532148580352_4.jpg)

partially stabilized zirconia [10,11] to analyze the frac-
ture toughening behavior. Kreher [12] proposed a frac-
ture model based on the balance of energy supplied by
the driving forces and the total energy either dissipated
by domain switching, stored in the crack wake region or
consumed by the formation of new fracture surface. For
these proposed theories either the details of the me-
chanical and electrical coupling behavior of the material
is neglected or the calculation of the complicated crack
tip electromechanical fields is avoided. The model to be
presented in this work intends to amend these simplifi-
cations by applying a recently developed phenomeno-
logical constitutive law for ferroelectric switching within
the finite element method to determine the details of the
crack tip fields and the toughening due to domain
switching during steady crack growth.

The remainder of this paper is organized as follows.
In Section 2 the nonlinear phenomenological constitu-
tive model for coupled electromechanical domain
switching is presented. In Section 3 the fracture model
and the finite element formulation which implements the
constitutive model for steady crack growth will be de-
scribed. The results will be presented and analyzed in
Section 4. A discussion of the results and comparisons
to experimental observations is included in Section 5.

## 2. Constitutive model

The nonlinear constitutive response of ferroelectric
materials is a result of the mechanism of domain
switching. A summary of the recent developments on
micro-electromechanical and phenomenological consti-
tutive modeling of ferroelectrics can be found in Kamlah
[13] and Landis [14]. The phenomenological constitutive
model presented below is based on the work of Landis
et al. [15–17]. This constitutive model has been verified
against experimental observations and micro-electro-
mechanical self-consistent simulations based on the
model of Huber et al. [18]. A formulation of the model
required to investigate in-plane mechanical loading with
out-of-plane electrical loading is presented here.

In this work, it is assumed that the primary me-
chanical loading is applied in the $x_1 - x_2$ plane and
electric field is applied only in the $x_3$ direction as illus-
trated in Fig. 1. Due to the constraint of plane-strain,
axial stresses in the $x_3$ direction are allowed to develop
as well. Also, due to symmetry, remanent polarization
can only develop in the $x_3$ direction. Materials poled in
the $x_3$ direction will have elastic, dielectric and piezo-
electric properties that are transversely isotropic with
the $x_1 - x_2$ plane being the plane of isotropy. For sim-
plicity it will be assumed that elastic and dielectric
properties are isotropic and not affected by changes in
the remanent polarization of the material. It is also as-
sumed that the piezoelectric properties are proportional
to the remanent polarization. Under these conditions,
the constitutive relationships can be expressed as:

$$
\varepsilon_{i j}=\frac{1+v}{E} \sigma_{i j}-\frac{v}{E} \sigma_{k k} \delta_{i j}+\left(\varepsilon_{i j}^{r}-\varepsilon_{i j}^{0}\right)+d_{3 i j} E_{3}, \quad(2.1)
$$

$$
D_{3}=d_{3 i j} \sigma_{i j}+\kappa E_{3}+\left(P_{3}^{r}-D_{3}^{0}\right), \quad(2.2)
$$

where
$$
\begin{aligned}
& d_{333}=\frac{d_{33} P_{3}^{r}}{P_{0}}, \quad d_{311}=d_{322}=\frac{d_{31} P_{3}^{r}}{P_{0}}, \\
& d_{312}=d_{321}=d_{331}=d_{313}=d_{332}=d_{323}=0.
\end{aligned}\quad(2.3)
$$

Here, $\varepsilon_{i j}$ are the Cartesian components of the infinitesi-
mal strain tensor as referenced from the initial strain
state $\varepsilon_{i j}^{0}$, and $\sigma_{i j}$ are the components of the Cauchy
stress. The isotropic elastic properties are the Poisson's
ratio $v$ and the Young's modulus $E$, and $\delta_{i j}$ is the Kro-
necker delta. The components of the remanent strain as
referenced from a thermally depolarized state are given
as $\varepsilon_{i j}^{r}$. Furthermore, $d_{3 i j}$ are the components of the pie-
zoelectric tensor, $E_3$ is the electric field in the $x_3$ direc-
tion, $D_3$ is the electric displacement in $x_3$ direction as
referenced from the initial electrical displacement $D_3^0$.
Finally, the dielectric permittivity is $\kappa$, $P_3^r$ is the total
remanent polarization in $x_3$ direction, and $d_{31}$ and $d_{33}$ are
the piezoelectric coefficients when $P_3^r$ reaches the maxi-
mum attainable remanent polarization $P_0$.

Prior to crack growth the material is loaded by a
uniaxial electric field and there is no mechanical loading
involved. After this initial electrical loading operation
the initial strain and electric displacement are given as:

$$
\varepsilon_{i j}^{0}=\varepsilon_{i j}^{r, 0}+d_{3 i j}^{0} E_{3}, \quad(2.4)
$$

$$
D_{3}^{0}=\kappa E_{3}+P_{3}^{r, 0}. \quad(2.5)
$$

Here, $\varepsilon_{i j}^{r, 0}$ and $P_{3}^{r, 0}$ are the Cartesian components of the
initial remanent strain and initial remanent polarization,

and $d_{3 i j}^{0}$ are the components of the piezoelectric tensor when $P_{3}^{r}=P_{3}^{r, 0}$. Note that in all cases discussed in this paper, the reference states for $\varepsilon_{i j}^{r}, \varepsilon_{i j}^{r, 0}, P_{3}^{r}$, and $P_{3}^{r, 0}$ correspond to the state of the material as cooled from above the Curie temperature, i.e., a thermally depolarized sample. Within the implementation of the constitutive law, the knowledge of this pre-poled state $\varepsilon_{i j}^{r, 0}$ and $P_{3}^{r, 0}$ must always be retained and incorporated into the total remanent strain and the total remanent polarization in order to refer to the thermally depolarized state.

The purpose of the nonlinear constitutive law is to provide the evolution of the stress, electric displacement, remanent strain and remanent polarization histories given the total strain and electric filed histories. Domain switching occurs when a specific switching condition is met. This switching criterion can be used to define a surface in stress and electric field space and will be referred to as the switching surface. The specific form of the switching surface implemented here is that proposed in $[15,17]$
$$
\Phi=\frac{3 \hat{s}_{i j} \hat{s}_{i j}}{2 \sigma_{0}^{2}}+\frac{\hat{E}_{3} \hat{E}_{3}}{E_{0}^{2}}+\frac{\beta \hat{E}_{3} P_{3}^{r} \hat{s}_{33}}{E_{0} P_{0} \sigma_{0}}-1=0,
\tag{2.6}
$$
where
$$
\hat{\sigma}_{i j}=\sigma_{i j}-\sigma_{i j}^{\mathrm{B}}, \quad \text { with } \quad \hat{s}_{i j}=\hat{\sigma}_{i j}-\frac{1}{3} \hat{\sigma}_{k k} \delta_{i j}
$$
and
$$
\hat{E}_{3}=E_{3}-E_{3}^{\mathrm{B}}+\frac{\partial d_{3 i j}}{\partial P_{3}^{r}} E_{3} \sigma_{i j},
\tag{2.7}
$$
where $\sigma_{i j}^{\mathrm{B}}$ is the back stress tensor, $E_{3}^{\mathrm{B}}$ is the back electric field, $\sigma_{0}$ is the initial switching strength of the material in uniaxial tension or compression, $E_{0}$ is the coercive field, and $\beta$ is a positive scalar parameter. The postulate of maximum dissipation is satisfied if the switching surface is convex and the increments of remanent strain and polarization are normal to the surface. The switching surface defined in Eq. (2.6) is convex if $\beta<3$, and normality requires the remanent increments to be given as
$$
\dot{\varepsilon}_{i j}^{r}=\lambda \frac{\partial \Phi}{\partial \hat{\sigma}_{i j}} \quad \text { and } \quad \dot{P}_{i}^{r}=\lambda \frac{\partial \Phi}{\partial \hat{E}_{i}},
\tag{2.8}
$$
where $\lambda$ is the switching multiplier. To determine the back stress and back electric field, it is assumed that the remanent strain and remanent polarization can be applied as internal variables that fully characterize the thermodynamic state of the material. This assumption leads to the identification of a remanent potential, $\Psi^{r}\left(\varepsilon_{i j}^{r}, P_{3}^{r}\right)$, such that the back stress and back electric field components can be derived from the potential in the following manner
$$
\sigma_{i j}^{\mathrm{B}}=\frac{\partial \Psi^{r}}{\partial \varepsilon_{i j}^{r}} \quad \text { and } \quad E_{3}^{\mathrm{B}}=\frac{\partial \Psi^{r}}{\partial P_{3}^{r}}.
\tag{2.9}
$$

Finally, the form of $\Psi^{r}$ must be specified to complete the constitutive theory. For the results to be presented $\Psi^{r}$ is split into a mechanical part $\Psi^{\sigma}$ that enforces the strain saturation conditions, and an electrical part $\Psi^{E}$ that enforces the polarization saturation conditions, i.e.,
$$
\Psi^{r}=\Psi^{\sigma}+\Psi^{E},
\tag{2.10}
$$
$$
\Psi^{\sigma}=\frac{1}{2} H_{0}^{\sigma} \varepsilon_{\mathrm{c}}\left[\frac{J_{2}^{e}}{\varepsilon_{\mathrm{c}}} \exp \left(\frac{m}{1-\bar{\varepsilon} / \varepsilon_{\mathrm{c}}}\right)\right]^{2},
\tag{2.11}
$$
where $H_{0}^{\sigma}$ is a characteristic level of back stress that primarily affects the initial slope of uniaxial stress versus remanent strain curve, $m$ is another hardening parameter that controls how abruptly the strain saturation conditions can be approached. The multi-axial remanent strain saturation conditions are enforced by causing $\Psi^{\sigma}$ to approach infinity as the strain-like variable $\bar{\varepsilon}$ approaches the saturation level of remanent strain in uniaxial compression $\varepsilon_{\mathrm{c}}$. The effective saturation remanent strain quantity $\bar{\varepsilon}$ is defined as
$$
\bar{\varepsilon}=J_{2}^{e} f\left(J_{3}^{e} / J_{2}^{e}\right),
\tag{2.12}
$$
where
$$
\begin{gathered}
f\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)=-0.0965\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)^{3}+0.01\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)^{6}+0.8935 \\
\text { for } \quad\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)<0,
\tag{2.13}
\end{gathered}
$$
and
$$
\begin{aligned}
f\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)= & -0.1075\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)^{3}-0.027\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)^{6}-0.028\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right)^{21} \\
& +0.8935 \text { for }\left(\frac{J_{3}^{e}}{J_{2}^{e}}\right) \geqslant 0.
\tag{2.14}
\end{aligned}
$$

Here, $f$ is a functional fit to the numerical results obtained from the micromechanical computations described in [16]. The following remanent strain invariants are used to describe the multi-axial remanent strain state
$$
J_{2}^{e}=\left(\frac{2}{3} e_{i j}^{r} e_{i j}^{r}\right)^{1 / 2} \quad \text { and } \quad J_{3}^{e}=\left(\frac{4}{3} e_{i j}^{r} e_{j k}^{r} e_{k i}^{r}\right)^{1 / 3},
\tag{2.15}
$$
where $e_{i j}^{r}$ is the remanent strain deviator, $e_{i j}^{r}=\varepsilon_{i j}^{r}-$ $\delta_{i j} \varepsilon_{k k}^{r} / 3$.

Next, the electrical part of $\Psi^{r}$ has the form of
$$
\Psi^{E}=H_{0}^{E} P_{0}\left[\ln \left(\frac{1}{1-\left|P_{3}^{r}\right| / P_{\text {sat }}}\right)-\frac{\left|P_{3}^{r}\right|}{P_{\text {sat }}}\right],
\tag{2.16}
$$
where
$$
P_{\text {sat }}=\frac{3 P_{0}}{4\left(\varepsilon_{\mathrm{t}}+\varepsilon_{\mathrm{c}}\right)}\left(\varepsilon_{33}^{r}+\varepsilon_{\mathrm{c}}\right)+\frac{P_{0}}{4}.
\tag{2.17}
$$

Here $\varepsilon_{\mathrm{t}}$ is the remanent saturation strain in uniaxial tension and according to Eqs. (2.11)-(2.14) is equal to $1.368 \varepsilon_{\mathrm{c}}$. The hardening parameter $H_{0}^{E}$ is a characteristic level of back electric field that primarily affects the slope of the uniaxial electric field versus remanent polarization

response. The maximum attainable remanent polariza-
tion $P_0$ has been defined previously. Note that the level
where the remanent polarization saturates $P_{\text{sat}}$ is a
function of the remanent strain and the maximum of $P_0$
can only be attained if $\varepsilon_{33}^r = \varepsilon_{\text{t}}$. If $\varepsilon_{33}^r = -\varepsilon_{\text{c}}$ then the
maximum level for $P_3^r$ is only $P_0/4$ . This result and the
linear approximation to the functional form for $P_{\text{sat}}$ gi-
ven in Eq. (2.17) are taken directly from the micro-
electromechanical computations described in [17]. Also
note that Eqs. (2.16) and (2.17) are the particular form
of the functions described in [17] when only the $P_3^r$
component of the remanent polarization is involved.
A more detailed description of the model can be found
in [15–17]. For the numerical implementation of the
constitutive model into the finite element model, a
backward Euler integration routine was developed to
solve the constitutive equations. The scheme is similar to
that described in [19].

## 3. The fracture model and finite element formulation

A schematic of the geometry and loading to be
modeled here is shown in Fig. 1. Two types of initial
electrical states will be considered in this work: initially
unpoled and initially poled states. The initially unpoled
samples begin in the thermally depolarized state of the
material. The initially poled samples are poled by ap-
plying a uniaxial electric field in the $x_3$ direction to a
level of $E_3^p$ and then removing the applied field. Note
that the poling field $E_3^p$ must be greater than the coercive
field $E_0$ in order to induce remanent polarization. This
entire electrical loading procedure is performed in the
absence of mechanical stress. The poling process induces
both residual remanent polarization and strain in the
material as referenced from the thermally depolarized
state. Fig. 2 illustrates the (a) electric displacement
versus electric field, (b) strain versus electric field re-
sponse during such electrical loading, (c) depolarization
due to mechanical stress, and (d) the stress versus strain
response during depolarization. Due to the irreversibil-
ity of the domain switching process, there is a continu-
ous range of partial poling states that the material can
attain in the range from the initially unpoled state to a
fully poled state. Note that the straight lines within the
loops in Fig. 2(a) and (b) represent linear unloading
during the removal of the applied electric field, and
those in Fig. 2(c) and (d) depict the initial behavior
during depolarization by compressive stress from dif-
ferent *partially* poled states. After the initial poling step
or lack of it, the electromechanical loading history for
the specimen is as follows. Electric field is applied in the
$x_3$ direction in the absence of mechanical stress. If the
applied electric field is of sufficient magnitude then
poling of initially unpoled samples or a reversal of
poling in initially poled samples may result. In any case,
this step in the electrical loading procedure induces new
states of strain and electric displacement, which have
been previously called the initial strain $\varepsilon_{ij}^0$ and initial
electric displacement $D_3^0$. The initial strain and electric
displacement consist of both linear reversible parts and
remanent parts as given by Eqs. (2.4) and (2.5). The final
step in the loading process is to apply the in-plane me-
chanical loads while keeping the out-of-plane electric
field fixed at the level attained in the previous step.
Under plane-strain conditions the out-of-plane axial
strain $\varepsilon_{33}$ is assumed to remain unchanged from its state
after the electrical loading step, i.e., $\varepsilon_{33} = \varepsilon_{33}^0$. Steady
crack growth then occurs while the in-plane mechanical
loads are applied.

During crack growth, small scale switching will be
assumed such that the representative height of the
nonlinear switching zone near the crack tip is much
smaller than any other characteristic specimen dimen-
sion such as crack length, specimen width or ligament
width. Furthermore, under plane-strain conditions it is
assumed that the specimen thickness is much greater
than the switching zone size as well. The assumption of
small scale switching will not be valid when the applied
out-of-plane electric field is of sufficient magnitude to
cause switching itself. However, it is assumed here that
the in-plane applied mechanical loads can still be char-
acterized by a Mode I $K$-field. Under these conditions a
characteristic switching zone half-height, $R_{\text{s}}$, can be
identified as

$$
R_{\text{s}}=\frac{1}{3\pi}\left(\frac{K_{\text{I}}}{\sigma_{0}}\right)^{2}=\frac{1}{3\pi}\frac{\mathscr{G}E'}{\sigma_{0}^{2}}. \tag{3.1}
$$

Here $K_{\text{I}}$ is the Mode I stress intensity factor. Within the
small scale switching approximation, the far field be-
havior of the solution surrounding the switching zone
must asymptotically match the stresses given by the near
tip elastic crack tip field. Hence, the tractions imposed
on the outer boundary of the finite element model are
derived from the following stresses

$$
\left\{\begin{array}{l}
\sigma_{11} \\
\sigma_{22} \\
\sigma_{12}
\end{array}\right\}=\frac{K_{\text{I}}}{\sqrt{2\pi r}}\cos\frac{\theta}{2}\left\{\begin{array}{c}
1-\sin\frac{\theta}{2}\sin\frac{3\theta}{2} \\
1+\sin\frac{\theta}{2}\sin\frac{3\theta}{2} \\
\sin\frac{\theta}{2}\cos\frac{3\theta}{2}
\end{array}\right\}, \tag{3.2}
$$

where $r$ and $\theta$ represent a polar coordinate system cen-
tered on the crack tip, with $\theta$ measuring the angle be-
tween the radial direction and the $x_1$-axis. Under small
scale switching conditions the prevailing mechanical
conditions that govern the nonlinear behavior near the
crack tip due to the geometry and far field loading of a
sample are completely characterized by $K_{\text{I}}$. Further-
more, the applied energy release rate, $\mathscr{G}$, is related to $K_{\text{I}}$
as

$$
\mathscr{G}=\frac{K_{\text{I}}^{2}}{E'}, \tag{3.3}
$$

![](./images/812353532148580352_5.jpg)

Fig. 2. The uniaxial electromechanical behavior of the model material with three levels of the poling field $E_3^p$ leading to different partially poled states.
(a) The electric field versus electrical displacement hysteresis loops. (b) The electric field versus strain butterfly loop. (c) The stress versus electrical
displacement depolarization loop. (d) The stress versus strain loop during depolarization. Notice that the intermediate lines in (a) and (b) represent
the response during the unloading of electric field, and those in (c) and (d) represent the depolarization behavior from a partially poled state.

where $E' = E$ for plane-stress and $E' = \frac{E}{1-v^2}$ for plane-
strain. Note that $R_s$ is a very good estimate of the
switching zone size when there is no out-of-plane ap-
plied electric field. However, due to the electromechan-
ical coupling in ferroelectrics, the out-of-plane electric
field will affect the in-plane stresses at which switching
will occur and consequently the size of the switching
zone. This effect will be discussed in further detail in the
Section 4 of this paper.

It is also important to note that, for the assumed form
of the switching surface of Eq. (2.6), when the applied
electric field is near or equal to the coercive field, the
assumptions of small scale switching are not rigorously
valid. When the applied electric field is equal to $E_0$,
Eq. (2.6) indicates that the switching surface associated
with mechanical loading shrinks to a point for unpoled
materials. Hence, under such conditions any non-
hydrostatic applied stress will cause small increments of
switching. However, switching will be relatively diffuse
far from the crack tip and it will be assumed that the
tractions associated with the $K$-field given by Eq. (3.2)
and the applied energy release rate given by Eq. (3.3)
will remain approximately valid.

The analysis presented in this paper will focus only on
the toughening due to domain switching during the
steady crack growth conditions described above. Under
steady growth conditions, all increments of field quan-
tities can be related to derivatives with respect to the $x_1$
coordinate direction by

$$
\dot{\phi}=-\dot{a} \frac{\partial \phi}{\partial x_{1}}.\tag{3.4}
$$

Here, $\phi$ is any scalar field quantity such as a Cartesian
component of remanent strain or remanent polarization,
and $\dot{a}$ is the increment of crack advance in the $x_1$ di-
rection. Within this model, crack propagation will be
assumed to occur when the crack tip energy release rate
$\mathscr{G}_{\text{tip}}$ reaches a critical value. In order to compute the
relationship between the maximum or steady state far
field applied energy release rate $\mathscr{G}_{\text{ss}}$ and $\mathscr{G}_{\text{tip}}$, a steady
state finite element formulation will be implemented. In
the far field, traction corresponding to Eq. (3.2) is ap-
plied to the model and Eq. (3.3) can be used to compute
$\mathscr{G}_{\text{ss}}$. Then, under steady state conditions, $\mathscr{G}_{\text{tip}}$ can be
calculated using a formula similar to Hutchinson's
$I$-integral [20] as

$$
\mathscr{G}_{\text {tip }}=I \equiv \int_{S}\left(W n_{1}-\sigma_{i j} n_{j} u_{i, 1}+D_{i} n_{i} E_{1}\right) \mathrm{d} S,
\tag{3.5}
$$

where $S$ is a surface enclosing the crack tip, $n_{i}$ are the components of the unit normal directed outward from the surface, $u_{i}$ are the components of the displacement vector, $D_{i}$ are the components of the electric displacement vector, $E_{1}$ is the electric field in $x_{1}$ direction, and $W$ is the history dependent electric enthalpy density at a material point defined by

$$
W=\int_{0}^{\varepsilon_{i j}, E_{i}} \sigma_{i j} d \varepsilon_{i j}-D_{i} \mathrm{d} E_{i}.
\tag{3.6}
$$

In general Eq. (3.5) is a surface integral instead of a contour integral because electrical energy can enter the system from the electrodes attached to the surface of the specimen. However, due to the fact that $E_{1}=E_{2}=0$ and $E_{3}$ is constant throughout the calculation, Eq. (3.5) can be simplified to a contour integral as

$$
\mathscr{G}_{\text {tip }}=\int_{\Gamma}\left(W n_{1}-\sigma_{i j} n_{j} u_{i, 1}\right) \mathrm{d} \Gamma.
\tag{3.7}
$$

For a traction-free crack, the contour $\Gamma$ begins on the lower crack face, encircles the crack tip in the counterclockwise sense, and ends on the upper crack face. The calculation of $\mathscr{G}_{\text {tip }}$ is carried out after the finite element solution is obtained.

The finite element formulation required to solve the steady crack growth boundary value problem is based on the variational statement

$$
\begin{aligned}
& \int_{V} \delta \varepsilon_{i j} C_{i j k l} \varepsilon_{k l}^{n+1} \mathrm{d} V \\
& \quad=\int_{S} \delta u_{i} T_{i} \mathrm{d} S+\int_{V} \delta \varepsilon_{i j} C_{i j k l}\left(\varepsilon_{k l}^{r, n}-\varepsilon_{k l}^{0}+d_{3 k l}^{n} E_{3}\right) \mathrm{d} V,
\end{aligned}
\tag{3.8}
$$

where $S$ is the boundary of the volume $V, C_{i j k l}$ are the Cartesian components of the isotropic elastic stiffness tensor that can be written in terms of $E$ and $v$, and the tractions acting on the boundary $S$ are given as $T_{i}=\sigma_{j i} n_{j}$. These tractions are determined from the stress field of Eq. (3.2). Note that no electrical terms are needed in this finite element formulation because the electrical field equations, $\nabla \cdot \mathbf{D}=0$ and $\nabla \times \mathbf{E}=0$, are automatically satisfied by the fields $E_{1}=E_{2}=0$ and $E_{3}=$ constant with $D_{1}=D_{2}=0$ and $D_{3}=d_{3 i j} \sigma_{i j}+\kappa E_{3}+$ $P_{3}^{r}=D_{3}\left(x_{1}, x_{2}\right)$. However, the electrical behavior, in particular the changes in $P_{3}^{r}$ and $d_{3 i j}$, does have a significant effect on the in-plane mechanical fields through the constitutive behavior of the material. Returning to the finite element formulation, after the application of the appropriate finite element interpolations and the cancellation of the appropriate variational terms, the left-hand side of Eq. (3.8) represents the linear elastic stiffness matrix dotted with the vector of unknown nodal displacements in the $(n+1)$ th iteration. Note that this stiffness matrix does not depend on any non-linear deformations or non-linear polarization, only on the finite element mesh geometry and elastic properties of the material. Hence the stiffness matrix remains constant for all iterations. The first term on the right-hand side represents the vector of known applied nodal forces arising from the tractions described by Eq. (3.2), which correspond to a specified level of the far field applied energy release rate. Note that these applied tractions do not change from iteration to iteration. Finally, the second term on the right-hand side can be viewed as the body force due to the distributions of piezoelectric strain and remanent strain in the material from the $n$th iteration. As alluded to in this discussion, the finite element Eq. (3.8) is solved with an iterative technique. To start, uniform remanent strain and polarization distributions are assumed and integrated on the right hand side of Eq. (3.8) and added to the applied traction boundary conditions. Next, the system of finite element equations is solved to obtain a new but approximate solution for the nodal displacements. A new approximate strain distribution is derived from these nodal displacements. Then, the incremental constitutive model described in Section 2 is integrated along streamlines of constant height above the crack plane from $x=+\infty$ to $x=-\infty$ to obtain updated approximations for the stress, remanent strain, and remanent polarization distributions. The new remanent strain and remanent polarization distributions are then integrated on the right hand side of Eq. (3.8) and the matrix solution/streamline integration procedure is repeated until a suitable level of convergence is achieved. Additional descriptions of the steady state crack growth finite element formulation can be found in [19,21]. Once convergence is obtained, the crack tip energy release rate is computed from Eq. (3.5) using the domain integral technique [22].

### 4. Results

The goal of this paper is to investigate the influence of the electric field on the fracture behavior of ferroelectric materials when the electric field or the poling direction is applied parallel to the crack front. Two cases of electrical loading will be considered here, the initially unpoled and initially poled cases. After electrical loading of either case, the electric field $E_{3}$ is kept constant and the initial state $\varepsilon_{i j}^{0}, \varepsilon_{i j}^{r, 0}$ and $P_{3}^{r, 0}$ is attained for the fracture simulation, after which the mechanical load is applied. In order to identify important parameters that affect the toughness of ferroelectric materials a dimensional analysis is performed on the constitutive equations, i.e., Eqs. (2.1)-(2.7), and the fundamental differential field equations. Such analysis identifies the following normalized field variables, $\sigma_{i j} / \sigma_{0}, \varepsilon_{i j} / \varepsilon_{\mathrm{c}}, \varepsilon_{i j}^{r} / \varepsilon_{\mathrm{c}}, D_{3} / P_{0}, P_{3}^{r} / P_{0}$. Each of these normalized field variables are a function

of the normalized spatial coordinates $x_1/R_s$ and $x_2/R_s$, and also depend on the initial poling field $E_3^p/E_0$, applied electric field $E_3/E_0$, and normalized material parameters $E\varepsilon_{\mathrm{c}}/\sigma_{0}$, $d_{33}E_{0}/\varepsilon_{\mathrm{c}}$, $\kappa E_{0}/P_{0}$, $\sigma_{0}\varepsilon_{\mathrm{c}}/E_{0}P_{0}$, $H_{0}^{\sigma}/\sigma_{0}$, $H_{0}^{E}/E_{0}$, $d_{33}/d_{31}$, $v$, $\beta$ and $m$. Finally, the normalized steady state toughness of the material $\mathscr{G}_{\mathrm{ss}}/\mathscr{G}_{0}$ is not a spatially varying field and hence will only depend on the applied electrical loading and material parameters. It would be a rather daunting task to investigate the effects of all ten dimensionless material quantities identified here. Instead, this work will focus on the effects of the applied electrical loading $E_3^p/E_0$ and $E_3/E_0$ on the toughening for a specific set of material properties. These material properties and constitutive parameters are characteristic of a soft PLZT material as measured by Lynch [23], and are specifically given as: $\sigma_{0}=27.5$ MPa, $E_{0}=0.35$ MV/ m, $P_{0}=0.26$ C/m$^2$, $\varepsilon_{\mathrm{c}}=0.12\%$, $\beta=2.95$, $\kappa=3\times10^{-8}$C/(mV), $E=70$ GPa, $v=0.4$, $d_{33}=6\times10^{-10}$ m/ V, $d_{31}=-\frac{d_{33}}{2}$, $m=0.01$, $H_{0}^{\sigma}=0.5\sigma_{0}$, $H_{0}^{E}=0.05E_{0}$. It should be noted here that simply changing the parameters listed above does not always result in a model material that produces reasonable constitutive response like that displayed in Fig. 2. Hence, if another material composition is to be modeled, it is likely that in addition to changing the constitutive parameters listed above, the functional forms of the remanent potentials of Eqs. (2.10), (2.11) and (2.16) must be changed as well.

As mentioned previously, the primary result from each steady crack growth calculation is the ratio of the far field applied energy release rate, $\mathscr{G}_{\mathrm{ss}}$, to the crack tip energy release rate $\mathscr{G}_{\mathrm{tip}}$. However, prior to presenting results for the relative level of toughening, some features of the switching zones near the crack tip will be given first. Fig. 3 illustrates the sizes and shapes of the switching zones around steadily growing cracks in initially unpoled material (a,b), and initially poled material (c). Fig. 3(d) and (e) can be interpreted as for either initially unpoled or poled material since the constitutive response is the same for all unpoled and poled cases if the applied electric field is large enough. The specific electrical loading parameters used to generate these results are: unpoled (a) $E_3^p/E_0=0$, $E_3/E_0=0$, (b) $E_3^p/E_0=0$, $E_3/E_0=0.5$, (c) poled $E_3^p/E_0=2$, $E_3/E_0=0.5$, and (d,e) $E_3^p/E_0\leqslant3$, $E_3/E_0=3$. Note that the spatial coordinates have been normalized by the length scale $R_{0}=\mathscr{G}_{0}E'/3\pi\sigma_{0}^{2}$, which can be interpreted as the size of the switching zone when the applied energy release rate is equal to $\mathscr{G}_{0}$. This normalization is used instead of $R_s$ in order to make the scales on each plot in Fig. 3 comparable.

In Fig. 3(a)-(e) the outer solid line delineates the boundary between material that is undergoing changes in remanency due to the in-plane mechanical loading and material that is not. The inner solid contour delineates the location inside the switching zone where the change in remanent strain reaches the characteristic elastic level of $\Delta\tilde{\varepsilon}^{r}=\sigma_{0}/E$, and the dashed contour is where the remanent polarization change achieves the characteristic linear dielectric level $|\Delta P_{3}^{r}|=\kappa E_{0}$. It is worth noting that in most cases the sizes of these inner switching zone contours where the effective remanent strain and polarization changes are equal to their characteristic linear values is significantly smaller than the outer switching zone boundary. This illustrates the fact that intense switching is confined to a region very close to the crack tip. Furthermore, note that the shapes of the switching zones depicted in these figures are that of the active switching zone. In other words, in the active switching zone, neighboring points at the same height above the crack plane have different remanent strain and polarization states. Whereas, in the linearly unloaded wake, neighboring points at the same height above the crack plane have identical remanent states. Lastly, material points outside of the active switching zone or the unloaded wake have a remanent state that is identical to that when the mechanical loading is initially applied.

Within this model it is assumed that crack growth occurs when $\mathscr{G}_{\mathrm{tip}}$ reaches the intrinsic fracture toughness of the material $\mathscr{G}_{0}$. Hence the ratio $\mathscr{G}_{\mathrm{ss}}/\mathscr{G}_{0}$ indicates the amount of toughening due to domain switching, with $\mathscr{G}_{\mathrm{ss}}/\mathscr{G}_{0}=1$ corresponding to no toughness enhancement or R-curve behavior. With regard to R-curve behavior, $\mathscr{G}_{0}$ should be interpreted as the applied energy release rate where crack growth first begins, and $\mathscr{G}_{\mathrm{ss}}$ is the steady state or plateau level of the applied energy release rate after sufficiently large amounts of crack growth. Fig. 4 shows the ratio of $\mathscr{G}_{\mathrm{ss}}/\mathscr{G}_{0}$ versus the applied out-of-plane electric field for a range of initial poling states. The cases associated with the solid bold curve and the dashed bold curve will be discussed first, as these cases practically envelop the others and form an inverted butterfly loop. The solid and dashed regions of the inserted hysteresis and butterfly loops in the upper left and right hand corners correspond to the solid and dashed portions of the inverted toughness butterfly loop.

Consider a thermally depolarized material poled by a uniaxial out-of-plane electric field of magnitude $3E_{0}$. The states of electric displacement and strain for this material can be found at the upper right corners of the hysteresis loops in Fig. 2(a) and (b). Then, keeping this level of applied electric field fixed, steady crack growth occurs at an applied energy release rate of $\mathscr{G}_{\mathrm{ss}}=1.54\mathscr{G}_{0}$ and the switching zone for this case is illustrated in Fig. 3(d) and (e). This level of toughening is the lowest depicted on Fig. 4. However, if the applied electric field was larger, the steady state toughness would decrease even farther, approaching $\mathscr{G}_{0}$ as $E_{3}\rightarrow\infty$. The reason for this behavior is that for materials with out-of-plane remanent polarization, an applied electric field in the same direction as the polarization tends to inhibit domain switching. In other words, the alignment of the polar domains with the electric field is an energetically

![](./images/812353532148580352_6.jpg)

Fig. 3. Switching zone sizes and shapes for initially unpoled (a,b) and initially poled (c) cases. Figures (d) and (e) can be interpreted as for either initially poled or initially unpoled samples. The outermost curved contours on these plots delineate the location of the active switching boundary. The inner solid contours give the location within the active switching zones where the effective remanent strain change achieves the characteristic elastic level of $\Delta \bar{\varepsilon}^{r} \equiv \sqrt{2 \Delta \varepsilon_{i j}^{r} \Delta \varepsilon_{i j}^{r} / 3}=\sigma_{0} / E$. The inner dashed contours give the location within the active switching zones where the change of remanent polarization achieves the characteristic linear dielectric level $|\Delta P_{3}^{r}|=\kappa E_{0}$. Notice that the spatial coordinates are normalized by $R_{0}$ which is the characteristic switching zone size when the applied energy release rate reaches $\mathscr{G}_{0}$ i.e., $R_{0}=\mathscr{G}_{0} E^{\prime} / 3 \pi \sigma_{0}^{2}$. Therefore, if $\mathscr{G}_{0}$ is the same for all cases, then the spatial coordinate normalizations for each plot are identical.

favorable state. Since it is the domain switching process that gives rise to the dissipation of energy and the increase in fracture toughness, any phenomenon that inhibits switching will also tend to decrease the fracture toughness. The remainder of the bold dashed curve is obtained by first poling the material with an electric field of $E_{3}^{p}=3 E_{0}$, then reversing the electric field to a lower or negative level of $E_{3}$, and finally applying the in-plane mechanical loading to produce steady crack growth. During this type of initial electrical loading the electric displacement and strain behavior of the material traces out the outmost hysteresis loops depicted in Fig. 2(a) and (b) and in the inserted plots in the upper left and right hand corners of Fig. 4. As the electric field is removed, the inhibiting effect of the field on domain switching decreases and hence the fracture toughness increases. Furthermore, when the electric field is reversed sufficiently it actually enhances the driving force for domain switching and the fracture toughness of the material increases dramatically. In fact, the spikes or "butterfly legs" of the toughness versus electric field curve in Fig. 4 correspond to the legs of the butterfly

![](./images/812353532148580352_7.jpg)

Fig. 4. The normalized toughness enhancement $\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}$ versus the applied out-of-plane electric field for a range of initial poling states for plane-strain conditions. The bold solid line and bold dashed line on the main plot correspond to the solid and dashed lines on the outer hysteresis and butterfly loops depicted on the inserts in the upper left and right corners. The thin lines represent the toughening behavior of unpoled or partially poled materials. Points A and B are highlighted to indicate the relationships between the electromechanical constitutive response and the fracture toughness predictions.

loops in Fig. 2(b) and the steep regions of the hysteresis loop in Fig. 2(a). However, if the reversal of the initial applied electric field is large enough, then the initial polarization of the material will be reversed as well, and the case where the polarization and electric field are aligned is revisited. Hence, as the initial electric field is driven to large negative levels, it will again inhibit domain switching and cause low values of the steady state fracture toughness. Finally, the bold solid curve is a mirror image of the bold dashed curve and is obtained by poling in the negative out-of-plane direction first. Notice that points A and B are denoted on the three loops in this figure in order to aid in the understanding of the correlation between the fundamental electromechanical constitutive behavior and the fracture toughness predictions.

Also on Fig. 4 are the cases where the material is partially poled by a moderate electric field, then the electric field is removed, a new electric field $E_{3}$ is applied, and finally steady crack growth proceeds due to in-plane mechanical loading. For all of the partially poled cases negative $E_{3}$ levels correspond very closely with the fully poled, bold dashed curve described above. The differences between the partially poled cases and the fully poled cases are only evident at intermediate positive levels of $E_{3}$. These levels of $E_{3}$ correspond to the linear unloading regions indicated with the arrows on Fig. 2(a) and (b). For large levels of $E_{3}$ the partially poled cases eventually merge with the bold solid line that represents the situation where the material has been initially poled by a strong negative electric field. The regions of similar toughening behavior between the partially and fully poled cases can be understood by considering the hysteresis and butterfly loops of Fig. 2(a) and (b). Specifically, the levels of applied electric field where the toughness curves merge in Fig. 4 coincide with the electric field levels where the linear unloading segments for the partially poled materials meet the outer hysteresis and butterfly loops in Fig. 2. At these levels of electric field the partially poled materials commence additional nonlinear behavior.

Lastly, Fig. 4 also contains a plot of toughness versus applied electric field for initially unpoled material. When considering the toughening behavior of the unpoled material during the application of electric field, it is informative to analyze the unpoled material without applied electric field. This case is presented in detail by Landis [19]. When the material is unpoled and there are no applied electric fields then the problem is purely mechanical and the steady state toughness of the material depends on a greatly reduced set of parameters. Dimensional analysis suggests that $\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}=\tilde{\mathscr{G}}(\varepsilon_{\mathrm{c}} E /$ $\bar{\sigma}_{0}, H_{0}^{\sigma} / \bar{\sigma}_{0}, m, v)$ for the non-electrical case. To analyze the effects of the electric field on the unpoled sample, assume that the applied electric field primarily influences only the effective switching stress $\bar{\sigma}_{0}$. Specifically, it will be assumed that the switching stress can be represented as $\bar{\sigma}_{0}=\bar{\sigma}_{0}(E_{3})$ where $\bar{\sigma}_{0}(E_{3}=0)=\sigma_{0}$. Then, a first order Taylor series expansion can be applied to determine the effects of electric field on the toughness.

$$
\begin{aligned}
\frac{\mathscr{G}_{\mathrm{ss}}}{\mathscr{G}_{0}}\left(E_{3}\right)= & \left.\frac{\mathscr{G}_{\mathrm{ss}}}{\mathscr{G}_{0}}\right|_{E_{3}=0}+\left.\frac{\partial\left(\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right)}{\partial\left(\varepsilon_{\mathrm{c}} E / \bar{\sigma}_{0}\right)}\right|_{E_{3}=0}\left[\frac{\varepsilon_{\mathrm{c}} E}{\bar{\sigma}_{0}\left(E_{3}\right)}-\frac{\varepsilon_{\mathrm{c}} E}{\sigma_{0}}\right] \\
& +\left.\frac{\partial\left(\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right)}{\partial\left(H_{0}^{\sigma} / \bar{\sigma}_{0}\right)}\right|_{E_{3}=0}\left[\frac{H_{0}^{\sigma}}{\bar{\sigma}_{0}\left(E_{3}\right)}-\frac{H_{0}^{\sigma}}{\sigma_{0}}\right] \\
= & \left.\frac{\mathscr{G}_{\mathrm{ss}}}{\mathscr{G}_{0}}\right|_{E_{3}=0}+\left\{\left.\frac{\partial\left(\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right)}{\partial\left(\varepsilon_{\mathrm{c}} E / \bar{\sigma}_{0}\right)}\right|_{E_{3}=0} \frac{\varepsilon_{\mathrm{c}} E}{\sigma_{0}}\right. \\
& \left.+\left.\frac{\partial\left(\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right)}{\partial\left(H_{0}^{\sigma} / \bar{\sigma}_{0}\right)}\right|_{E_{3}=0} \frac{H_{0}^{\sigma}}{\sigma_{0}}\right\}\left[\frac{\sigma_{0}}{\bar{\sigma}_{0}\left(E_{3}\right)}-1\right]. \quad(4.1)
\end{aligned}
$$

For the specific case investigated in this paper the parameters are, $\varepsilon_{\mathrm{c}} E / \sigma_{0}=3.05, H_{0}^{\sigma} / \sigma_{0}=0.5$, and the initial toughness and derivatives have been computed from the numerical results presented in [19] as $\left.\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right|_{E_{3}=0}=2.87,\left.\partial\left(\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right) / \partial\left(\varepsilon_{\mathrm{c}} E / \bar{\sigma}_{0}\right)\right|_{E_{3}=0}=0.715$ and $\left.\partial\left(\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}\right) / \partial\left(H_{0}^{\sigma} / \bar{\sigma}_{0}\right)\right|_{E_{3}=0}=-0.5$. Finally, with the switching condition assumed in this work and given by Eq. (2.6) the function $\bar{\sigma}_{0}(E_{3})$ can be determined for an unpoled material as $\bar{\sigma}_{0}(E_{3})=\sigma_{0}[1-(E_{3}/E_{0})^{2}]$. Therefore, for the material properties and assumed form of

the switching surface used in this work, the toughness enhancement for an unpoled material as a function of electric field can be given as

$$
\frac{\mathscr{G}_{\mathrm{ss}}}{\mathscr{G}_{0}}\left(E_{3}\right)=2.87+1.93\left[\frac{1}{\sqrt{1-\left(E_{3} / E_{0}\right)^{2}}}-1\right]. \quad(4.2)
$$

Of course Eq. (4.1) is a Taylor series expansion about $E_{3}=0$ and can only be expected to be accurate for $E_{3}$ near zero. However, a comparison of Eq. (4.2) with the numerical results presented in Fig. 4 confirms that Eq. (4.2) is accurate to within $1 \%$ error for $\left|E_{3}\right| \leqslant 0.8 E_{0}$, and at $\left|E_{3}\right|=0.9 E_{0}$ Eq. (4.2) overpredicts the toughening by $6 \%$. Finally, a similar analysis of the height of the switching zone, $h_{\mathrm{s}}$, for the initially unpoled materials can be made by substituting $\bar{\sigma}_{0}\left(E_{3}\right)$ for $\sigma_{0}$ in Eq. (3.1). For the assumed material properties given in this work $h_{\mathrm{s}}$ is given as

$$
h_{\mathrm{s}}\left(E_{3}\right)=\frac{1}{3 \pi} \frac{\mathscr{G}_{\mathrm{ss}} E^{\prime}}{\sigma_{0}^{2}} \frac{1.04}{1-\left(E_{3} / E_{0}\right)^{2}}. \quad(4.3)
$$

For the results generated with the present model, Eq. (4.3) is accurate to within $1 \%$ for $\left|E_{3}\right| \leqslant 0.9 E_{0}$. Lastly, these results suggest a more general form of the toughening and switching zone heights for arbitrary switching stress dependencies as

$$
\frac{\mathscr{G}_{\mathrm{ss}}}{\mathscr{G}_{0}}\left(E_{3}\right)=c_{1}+c_{2}\left[\frac{\sigma_{0}}{\bar{\sigma}_{0}\left(E_{3}\right)}-1\right], \quad(4.4)
$$

and

$$
h_{\mathrm{s}}\left(E_{3}\right)=\frac{c_{3}}{3 \pi} \frac{\mathscr{G}_{\mathrm{ss}} E^{\prime}}{\bar{\sigma}_{0}\left(E_{3}\right)^{2}}, \quad(4.5)
$$

where $c_{1}, c_{2}$ and $c_{3}$ are constants.

One observation of the results displayed on Fig. 4 that is somewhat counterintuitive is the fact that under no applied electric field the toughness enhancement of the poled samples is actually very slightly smaller than the toughness enhancement for the unpoled sample. This results is counterintuitive because one would expect that the poling process would create an out-of-plane remanent state that would allow for an increased amount of dissipation from domain switching due to in-plane mechanical loads. For example, an unpoled material loaded by an in-plane tensile stress can have a maximum in-plane change in remanent strain of approximately $1.37 \varepsilon_{\mathrm{c}}$. Whereas, a material fully poled out-of-plane can have a maximum in-plane change of remanent strain of approximately $2.06 \varepsilon_{\mathrm{c}}$. Hence, it would appear that the poled material has a greater propensity for domain switching, dissipation and increased toughening. However, this is not the case, and the reason is due to the out-of-plane mechanical loading imposed by the $\sigma_{33}$ stress component arising from the plane-strain constraint. As with an applied out-of-plane electric field, domains poled out-of-plane are in a low energy state with a tensile out-of-plane stress $\sigma_{33}$. If domains aligned in the out-of-plane direction are switched towards an in-plane direction, this switching process will cause a negative out-of-plane strain. In order to enforce the plane-strain constraint a tensile $\sigma_{33}$ stress will be induced by such a switching process. Therefore, the plane-strain constraint impedes domain switching in poled materials and hence the full potential toughness enhancement cannot be achieved.

In order to verify and quantify the effects of the plane-strain constraint on the toughness enhancement, simulations were performed with no applied electric field on samples with differing levels of partial poling under both plane-strain and plane-stress conditions. Results for the toughness enhancement versus the level of the partial poling field are displayed on Fig. 5. Note that the poling field of $E_{3}^{p}=E_{0}$ does not cause any change in remanency and so this level of poling field also corresponds to the unpoled case. Also, both of the curves in Fig. 5 are practically flat for $E_{3}^{p} \geqslant 2 E_{0}$. From this figure it is clear that the out-of-plane mechanical constraint plays a significant role on the fracture toughness. Under plane-strain conditions the toughness behavior has a very weak dependence on the level of partial poling, while for plane-stress, i.e., $\sigma_{33}=0$, the toughness increases as the material is more fully poled. Hence, the common intuition that the toughness enhancement correlates with the potential for in-plane switching is valid for plane-stress but not for the plane-strain out-of-plane constraint.

![](./images/812353532148580352_8.jpg)

Fig. 5. A comparison of the effects of plane-strain versus plane-stress out-of-plane mechanical constraint on the toughness enhancement of partially poled materials. The normalized toughness enhancement $\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}$ is plotted versus the initial poling field $E_{3}^{p} / E_{0}$. For all cases the initial poling field is removed and no subsequent electric field is applied.

![](./images/812353532148580352_9.jpg)

Fig. 6. The effects of the transverse stress $T_{11}$ on the toughness enhancement under plane strain conditions. The normalized toughness enhancement $\mathscr{G}_{\mathrm{ss}} / \mathscr{G}_{0}$ is plotted versus the applied out-of-plane electric field with or without $T$-stress for: (a) initially unpoled and (b) initially poled with $E_{3}^{p} / E_{0}=2$.

The final sets of results generated in this study are displayed in Fig. 6(a) and (b). The plots illustrate the effects of transverse stress or $T$-stress on the toughening behavior. To analyze the effects of $T$-stress, the model is modified by simply adding a constant $T_{11}$ term to the far field $\sigma_{11}$ stress given in Eq. (3.2). The additional $T$-stress introduces a new dimensionless parameter $T_{11} / \sigma_{0}$ to the model. Previous models that apply a "transformation toughening" type analysis of the fracture problem [24,25] have predicted that a positive $T_{11}$ will decrease the level of toughening while a negative $T_{11}$ will increase the toughening for unpoled materials. The results of the present model displayed in Fig. 6(a) indicate that positive and negative $T$-stress produce very modest increases in the toughness of the unpoled material, with the negative $T$-stress yielding a slightly larger increase. In fact, Fig. 6(a) for the unpoled material and Fig. 6(b) for the poled material indicate that $T$-stress has a significant effect on toughening only when the applied out-of-plane electric field is near the coercive field.

## 5. Discussion

The model presented here differs from previous theoretical explanations of the effects of electric field and polarization on the fracture toughness of ferroelectrics in that an incremental, micro-electromechanically tested, phenomenological constitutive law has been applied instead of a discrete switching law. Additionally, in contrast to applying simplifying assumptions associated with most transformation toughening models, the details of the electromechanical fields have been obtained from finite element computations. The fields computed in this work include both the perturbing influences of ferroelectric switching and the changing piezoelectric effect that results from such switching. The detailed constitutive model applied in this work has allowed for both qualitative and quantitative characterizations of the effects of electric field on the toughening due to domain switching in ferroelectric ceramics. The model predicts a range of phenomena that indicate that the toughening is dependent on both the level of electric filed parallel to the crack front and on the polarization state. For poled materials, an electric field applied in the same direction as the polarization tends to inhibit domain switching and toughening, whereas an electric field applied opposite to the polarization directions enhances switch toughening. For initially unpoled materials, applied electric fields below the coercive field level enhance the fracture toughness of the material. As a complement to these qualitative characterizations, the quantitative predictions of the model allow for a direct comparison to some recent experimental studies.

Due to the fact that it is in contrast to conventional wisdom concerning toughening due to domain switching, the most interesting result from the model simulations is that, without an applied electric field, the toughness of an initially unpoled material is very similar to that of a material poled parallel to the crack front. For the material parameters characteristic of a soft PLZT material the model simulations have predicted that $\mathscr{G}_{\mathrm{ss}}=2.87 \mathscr{G}_{0}$ for the unpoled material and $\mathscr{G}_{\mathrm{ss}}=2.80 \mathscr{G}_{0}$ for the fully poled material. Measurements by Hackemann and Pfeiffer [8] on a soft PZT material indicate that the toughness enhancements for both poled and unpoled samples is in the range approximately $\mathscr{G}_{\mathrm{ss}}=3 \mathscr{G}_{0}-4 \mathscr{G}_{0}$. Furthermore, Lucato et al. [7] have made similar measurements on a PZT 151 composition and found that the toughness of unpoled samples is approximately $\mathscr{G}_{\mathrm{ss}}=2.1 \mathscr{G}_{0}$ and that of poled samples (with short-circuited electrodes on the out-of-plane surfaces) is approximately $\mathscr{G}_{\mathrm{ss}}=1.9 \mathscr{G}_{0}$. Hence, experiments suggest that if there is any difference between the toughening of poled and unpoled samples, then the poled specimens actually incur less toughening due to

domain switching than unpoled samples. The present model predicts this behavior as well. Furthermore, it was shown that the out-of-plane mechanical constraint, i.e., plane-strain versus plane-stress, is the fundamental reason for this behavior.

One final set of experimental observations that warrants consideration is the study by Kolleck et al. [6]. Toughness and R-curve measurements were performed on two different PZT compositions, and a barium titanate material. In general, it was observed that the toughness of initially unpoled samples increased with increasing levels of out-of-plane applied electric field. The same basic trend in behavior is predicted by the present model, however a direct comparison is difficult due to the lack of nonlinear constitutive information on these specific compositions. Furthermore, assuming that the measurements of the crack growth initiation toughness levels are accurate, the R-curve measurements on barium titanate clearly indicate that the level of initiation toughness increases with increasing electric field. Such behavior cannot be predicted from the present model, as $\mathscr{G}_{0}$ is an input parameter of the model. This model only predicts the multiplicative factor of toughness enhancement over the initiation toughness. In general, the initiation toughness could depend on both the level of applied electric field and the level of out-of-plane remanent polarization, i.e., $\mathscr{G}_{0}=\mathscr{G}_{0}(E_{3},P_{3}^{r})$, and this physical behavior is required as an input to the model.

Ultimately, the present model predicts a range of interesting effects of electric field applied parallel to the crack front on the fracture toughness, or more specifically the toughening during R-curve behavior due to domain switching during crack growth. The qualitative "shape" of the toughness enhancement versus applied electric field forms an inverted butterfly loop that correlates directly with the strain versus electric field butterfly hysteresis loop during uniaxial electrical loading. The model predicts the unintuitive behavior that the fracture toughness of a material poled out-of-plane is comparable to the toughness of an initially unpoled material. This prediction has previously been confirmed experimentally. It was demonstrated that this behavior is primarily due to the out-of-plane mechanical constraint imposed by plane strain conditions.

## Acknowledgements
The authors would like to acknowledge support from the Army Research Office Grant No. DAAD19-02-1-0241.

## References
[1] Pisarenko GG, Chusko VM, Kovalev SP. J Am Ceram Soc 1985;68(5):259.
[2] Metha K, Virkar AV. J Am Ceram Soc 1990;73(3):567.
[3] Zhang Z, Raj R. J Am Ceram Soc 1995;78(12):3363.
[4] Guiu F, Hahn BS, Lee HL, Caderon JM, Reece MJ. J Eur Ceram Soc 1997;17:502.
[5] Meschke F, Kolleck A, Schneider GA. J Eur Ceram Soc 1997;17:1143.
[6] Kolleck A, Schneider GA, Meschke FA. Acta Mater 2000;48:4099.
[7] Lucato SL, Lindner J, Lupascu DC, Rodel J. Key Eng Mater 2002;206-213:609.
[8] Hackemann S, Pfeiffer W. J Eur Ceram Soc 2003;23:141.
[9] Yang W, Fang F, Tao M. Int J Solids Struct 2001;38:2203.
[10] McMeeking RM, Evans AG. J Am Ceram Soc 1982;65:242-6.
[11] Budiansky B, Hutchinson JW, Lambropoulos JC. Int J Solids Struct 1983;19(4):337.
[12] Kreher WS. J Mech Phys Solids 2002;50:1029.
[13] Kamlah M. Continuum Mech Thermodyn 2001;13:219.
[14] Landis CM, Curr Opin Solid State Mater Sci 2004; in press.
[15] Landis CM. J Mech Phys Solids 2002;50:127.
[16] Landis CM. J Appl Mech 2003;70:470.
[17] Landis CM, Wang J, Shen J. J Intell Mater Sys Struct 2004; in press.
[18] Huber JE, Fleck NA, Landis CM, McMeeking RM. J Mech Phys Solids 1999;47:1663.
[19] Landis CM. J Mech Phys Solids 2003;51:1347.
[20] Hutchinson JW. Harvard University Report, DEAP S-8. Division of Applied Sciences, Harvard; 1974.
[21] Dean RH, Hutchinson JW. In: Fracture Mechanics, ASTM-STP 700; 1980. p. 383.
[22] Li FZ, Shih CF, Needleman A. Eng Fract Mech 1985;21(2):405.
[23] Lynch CS. Acta Mater 1996;44:4137.
[24] Fett T, Glazounov A, Hoffmann MJ, Munz D, Thun G. Eng Fract Mech 2001;68:1207.
[25] Cui YQ, Yang W. Theor Appl Fract Mech 2003;39:137.