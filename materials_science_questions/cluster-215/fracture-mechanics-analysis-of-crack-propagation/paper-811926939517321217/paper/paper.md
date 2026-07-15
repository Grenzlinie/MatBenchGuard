![](./images/811926939517321217_1.jpg)

# J-integral and crack driving force in elastic-plastic materials

N.K. Simha $^{a,b,*}$, F.D. Fischer $^{c}$, G.X. Shan $^{d}$, C.R. Chen $^{e}$, O. Kolednik $^{f}$

$^{a}$ Department of Aerospace Engineering and Mechanics, University of Minnesota, 107 Akerman Hall, 110 Union St. S.E., Minneapolis, MN 55455, USA
$^{b}$ Department of Orthopaedic Surgery, University of Minnesota, MMC 289, 420 Delaware St. S.E., Minneapolis, MN 55455, USA
$^{c}$ Institute of Mechanics, Montanuniversität, Franz-Josef-Strasse 18, A-8700 Leoben, Austria
$^{d}$ Siemens VAI Metals Technologies, Turmstrasse 44, A-4031 Linz, Austria
$^{e}$ Materials Center Leoben Forschung GmbH, Franz-Josef-Strasse 13, A-8700 Leoben, Austria
$^{f}$ Erich Schmid Institute of Materials Science, Austrian Academy of Sciences, Jahnstrasse 12, A-8700 Leoben, Austria

---

## ARTICLE INFO

**Article history:**
Received 10 May 2007
Received in revised form
7 January 2008
Accepted 5 April 2008

**Keywords:**
Configurational forces
Crack-tip shielding
Energy release rate
Elastic-plastic material
J-integral
Plasticity

---

## ABSTRACT

This paper discusses the crack driving force in elastic-plastic materials, with particular emphasis on incremental plasticity. Using the configurational forces approach we identify a "plasticity influence term" that describes crack tip shielding or anti-shielding due to plastic deformation in the body. Standard constitutive models for finite strain as well as small strain incremental plasticity are used to obtain explicit expressions for the plasticity influence term in a two-dimensional setting. The total dissipation in the body is related to the near-tip and far-field $J$-integrals and the plasticity influence term. In the special case of deformation plasticity the plasticity influence term vanishes identically whereas for rigid plasticity and elastic-ideal plasticity the crack driving force vanishes. For steady state crack growth in incremental elastic-plastic materials, the plasticity influence term is equal to the negative of the plastic work per unit crack extension and the total dissipation in the body due to crack propagation and plastic deformation is determined by the far-field $J$-integral. For non-steady state crack growth, the plasticity influence term can be evaluated by post-processing after a conventional finite element stress analysis. Theory and computations are applied to a stationary crack in a C(T)-specimen to examine the effects of contained, uncontained and general yielding. A novel method is proposed for evaluating $J$-integrals under incremental plasticity conditions through the configurational body force. The incremental plasticity near-tip and far-field $J$-integrals are compared to conventional deformational plasticity and experimental $J$-integrals.

© 2008 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

### 1.1. Application of the J-integral in elastic-plastic bodies

A fundamental issue in fracture mechanics is to determine the criteria for the growth of preexisting cracks in materials. It is perhaps equally important to establish whether the various parameters measured in standard laboratory experiments, like the experimental $J$-integral, characterize the crack growth resistance and are applicable for describing crack growth in arbitrary structures. These issues are well resolved in the context of elastic materials. For linear elastic materials, Griffith's

---

* Corresponding author at: Department of Aerospace Engineering and Mechanics, University of Minnesota, 107 Akerman Hall, 110 Union St. S.E., Minneapolis, MN 55455, USA.
E-mail addresses: simha@umn.edu (N.K. Simha), fischer@unileoben.ac.at (F.D. Fischer), guoxin.shan@siemens.com (G.X. Shan), crchen64@yahoo.com.cn (C.R. Chen), kolednik@unileoben.ac.at (O. Kolednik).

0022-5096/$ - see front matter © 2008 Elsevier Ltd. All rights reserved.
doi:10.1016/j.jmps.2008.04.003

![](./images/811926939517321217_2.jpg)

approach says that a crack extends if the thermodynamic crack driving force, characterized by the energy release rate $G$, becomes equal or larger than the crack growth resistance, $R$ (Griffith, 1921), whereas the Irwin (1957) approach postulates that a crack grows when the crack tip stress intensity factor $K$ reaches a critical value $K_{\mathrm{c}}$. The Griffith and Irwin criteria are equivalent for linear elastic materials, since energy release rate and stress intensity factor are related. Standard methods are available to determine the crack growth resistance $R$ and the critical stress intensity factor $K_{\mathrm{c}}$, and it is widely accepted that these parameters are valid for arbitrary structures since they do not depend on the experimental loading conditions or specimen geometry. For materials and structures where crack growth is accompanied only by limited plastic deformation (small-scale yielding), the engineering approach is to treat this as a perturbation of the linear elastic case and apply the Griffith and Irwin criteria, occasionally with the crack length extended by the radius of the crack tip plastic zone.

For crack growth in elastic-plastic materials under large-scale or general yielding conditions, the common approach is to use criteria based on the crack tip opening displacement (Wells, 1963), Rice's $J$-integral (Rice, 1968a,b) and the energy dissipation rate (Turner, 1990; Turner and Kolednik, 1994). However, the use of each of these criteria is somewhat problematic: The crack tip opening displacement is difficult to determine experimentally, since measurements should be taken in the interior of a specimen (Kolednik and Stüwe, 1985), the $J$-integral approach suffers from conceptual difficulties when applying it to elastic-plastic materials, e.g. (Rice, 1976), and the energy dissipation rate is strongly dependent on the size and geometry of the structure which makes the transferability of the data from a test specimen to an arbitrary structure difficult (Kolednik et al., 1997). Amongst these three parameters the $J$-based approach is used most widely and is the main focus of this paper, so we will now discuss this in some detail.

The $J$-integral approach presumes deformation plasticity and treats elastic-plastic materials as non-linear elastic. The $J$-integral evaluated on a contour around the crack tip, $J_{\text {tip }}$, characterizes both the thermodynamic crack driving force, i.e., the energy released per unit crack extension, and the intensity of the crack tip fields in non-linear elastic materials (Rice, 1968a,b). In the homogeneous context, the $J$-integral is independent of the contour used to evaluate it, so $J_{\text {tip }}=J_{\text {far }}$ where $J_{\text {far }}$ is the $J$-integral on a contour in the far-field. This path independence is important, since the energy released at the crack tip $\left(J_{\text {tip }}\right)$ cannot be easily measured, whereas the total energy released during crack extension in a body $\left(J_{\text {far }}\right)$ can be readily measured. The deformation plasticity setting has been also adopted in the development of the experimental $J$-integral, $J^{(A)}$, which is determined from the area $A$ under the load vs. load-line displacement curve (Rice et al., 1973; Kolednik, 1991). It can be shown that the deformational plasticity $J_{\text {far }}=J^{(A)}$ for a stationary crack, but not for a growing crack (Rice et al., 1973; Kolednik, 1993).

The primary advantage of presuming deformation plasticity is to utilize the path independence of the $J$-integral. The main disadvantage is that it does not describe irreversible plastic deformation. Deformation plasticity presumes proportional loading, i.e. all loading paths should remain radial in stress space. Hence, proportional loading is not valid for moving cracks due to unloading behind the crack tip and when the axes of the principal stresses at a fixed material point rotate during the deformation, which occurs in the context of large (finite) deformation even for a stationary crack (McMeeking, 1977; Anderson, 1995). Consequently, incremental theory of plasticity is required for a realistic modeling of the behavior of cracks in elastic-plastic materials.

In incremental plasticity, however, it is well known that the $J$-integral becomes path-dependent even for homogeneous elastic-plastic materials. Numerical studies find that for the large strain case the $J$-integral increases as the distance from the crack tip to the integration contour increases; at least for a stationary crack the $J$-integral reaches a saturation value at large distances which corresponds to the experimental $J$-integral $J^{(A)}$ (McMeeking, 1977; Brocks et al., 2003). Although the stress analysis is performed in incremental plasticity, such studies implicitly assume deformation plasticity for calculating the $J$-integral, e.g. (Parks, 1977). This means that the $J$-integral is evaluated using a stored energy density that contains the plastic work. Physically, the plastic work has already been dissipated and is not available for driving the crack growth. Hence, the deformation plasticity near-tip $J$-integral loses its meaning as the crack driving force in incremental plasticity, but it keeps its meaning as describing the intensity of the crack tip fields (Rice, 1968a,b). Since the derivation of the experimental $J$-integral $J^{(A)}$ is based on deformation plasticity, its validity for incremental plasticity is also unclear.

To address the problem of path dependence of the $J$-integral in incremental plasticity, other path-independent integrals have been identified. For example, Kishimoto et al. (1980) and Miyazaki and Nakagaki (1995) use the divergence theorem and certain equilibrium conditions to identify an integral that is path independent in the context of incremental plasticity (derivations are summarized in the Appendix). However, these approaches are ad hoc in the sense that the second law of thermodynamics is not invoked, so the relation between these integrals and a thermodynamic driving force at the crack tip is unclear (in contrast to $J_{\text {tip }}$ ). Also the physical meaning of these path independent integrals is unclear, since their relation to the experimentally measurable parameters is not established (in contrast to $J_{\text {far }}$ ).

On a more general level, it is unclear if $J_{\text {tip }}$ alone controls crack extension in elastic-plastic materials. One approach to determine what controls crack growth, is to appeal to the second law of thermodynamics and require that the dissipation in the entire body be maximized. In elastic materials the only source of dissipation is the propagating crack tip, so the dissipation in the entire elastic body is equal to the dissipation at the crack tip. Consequently maximizing crack tip dissipation is equivalent to maximizing the dissipation in the entire body. In contrast, both the crack tip propagation and plastic deformation can dissipate energy in elastic-plastic materials. The large crack tip stresses will invariably result in some plastic deformation around the crack tip. This suggests that crack tip propagation will necessarily require enlargement of the associated plastic region, which implies that crack growth would occur only if sufficient energy was available both for the dissipation by the crack tip as well as for the plastic work necessary to enlarge the plastic region

around the crack tip. In this paper we will localize the second law of thermodynamics to identify the driving force at the crack tip, but will examine also the total dissipation in the entire body in order to identify the driving force for both crack propagation and corresponding plastic deformation.

Lastly, we discuss the applicability of experimentally determined crack growth parameters to arbitrary structures. In the commonly used compact tension (C(T)-) specimens, it is well known that plastic deformation occurs also in regions remote from the crack tip (e.g. on the back face), and this remote plastic region may or may not be connected to the crack tip plastic zone depending on the loading conditions. The remote plastic region, which occurs due to the finite size of the specimen, could result in a shielding or anti-shielding effect and is perhaps the main source of the geometry and size dependence of the energy dissipation rate. Although there has been some progress (Stampfl and Kolednik, 2000), standard methods are not available to separate the dissipation due to plastic deformation near and remote from the crack tip in C(T)-specimens. Consequently, we will examine the role of remote plasticity and its influence on the near tip and far-field $J$-integrals.

### 1.2. Outline of the paper

For crack growth in the context of incremental plasticity we conclude that: (a) The physical meaning of the $J$-integral is unclear and (b) An appropriate measure for the crack driving force that can be determined using standard laboratory tests and that is applicable for arbitrary structures has not been found. The goal of this paper is to clarify these issues. Our approach is to first derive the $J$-integral without appealing to non-linear elasticity. Then, we explicitly identify the energy dissipated by plastic work in the cracked body and relate it to the near-tip and far-field $J$-integrals. The theory is then applied computationally to a C(T)-specimen to understand the influence of plastic deformation in the near-tip and remote regions on the crack driving force.

Early derivations of the $J$-integral used variational arguments and non-dissipative energies, and there are lingering doubts of whether the $J$-integral is appropriate for incrementally plastic materials. So the first task in the paper is to derive the $J$-integral in an explicit dissipative context without using variational approaches or energy conservation. The theoretical derivations follow the configurational forces approach (Gurtin, 1995; Maugin, 1995). The role of the Eshelby stress tensor, which is central to the configurational forces approach, in elastic-plastic materials has been studied by Maugin and coworkers (Maugin, 1994; Cleja-Tigoiu and Maugin, 2000). Specifically, Maugin (1994) has derived the form of the Eshelby stress tensor in the finite and small-strain setting by extending the standard variational energy to include a dissipation potential. This paper extends the analysis by Maugin (1994), and specifically examines the relation between the plastic dissipation and the $J$-integrals in the far field and near the crack tip. As general references to the configurational forces approach, we refer the reader to Maugin (1995, 1999), Gurtin (1995, 2000), Kienzler and Herrmann (2000); in the context of fracture we provide extensive references in our previous papers (Simha et al., 2003, 2005). Also since Maugin (1994) provides an extensive list in the context of elastic-plastic materials, we omit a comprehensive literature review and refer only to papers directly used in the calculation. Relevant results from Simha et al. (2003, 2005) are collected in Section 2.

To understand the influence of plastic deformation on the crack driving force, we adopt a simple framework. A cracked elastic-plastic body has two sources of dissipation: one is the propagation of the crack tip whereas the other is plastic deformation in the body. We explicitly identify the dissipation due to plastic deformation in the cracked body per unit crack extension and relate it to the $J$-integrals on contours close to the tip and in the far field (Section 3). Since crack growth corresponds to a motion in the reference configuration, derivations are first performed in the finite strain setting and then considered in the small strain setting which is widely used. In Section 4 we show that the plastic dissipation rate vanishes identically for deformational plasticity, while the crack tip driving force vanishes in rigid plasticity. In Section 5, we describe computational methods for evaluating the configurational forces and $J$-integrals and perform computations for a crack in a C(T)-specimen. We then elucidate in Section 6 the influence of the plastic deformation in the near tip and remote regions on the crack tip driving force by examining the relations between the $J$-integrals on various contours and the experimental $J$-integral $J^{(A)}$.

## 2. Configurational forces for a cracked body

In recent papers (Simha et al., 2003, 2005), we have derived the crack driving force without making any assumptions on the constitutive nature of the body. Hence detailed calculations are omitted here and the derivation is only discussed. In the configurational forces approach two systems of forces are introduced: the classical deformational forces that act in the current configuration, such as gravity, and a second system of forces called configurational forces that act in the reference configuration (Gurtin, 1995, 2000). The configurational forces are responsible for kinematic changes in the reference, such as the propagation of phase boundaries or crack growth due to the movement of the crack tip. Consequently there are separate balance laws for the deformational and configurational forces. These balance laws and certain invariance requirements on the second law of thermodynamics are sufficient to study cracks in elastic-plastic bodies.

For simplicity we ignore inertia and heat transfer, and consider the following mechanical setting: In the bulk we choose a deformational (1st Piola-Kirchhoff) stress $\mathbf{S}$, a configurational stress $\mathbf{C}$ and a configurational force $\mathbf{f}$. At the crack tip, a configurational force $\mathbf{f}_T$ is considered, whereas deformational forces are ignored. In the two-dimensional setting (Fig. 1), the

![](./images/811926939517321217_3.jpg)

Fig. 1. Crack in a two-dimensional body $\mathscr{B}$ in its reference configuration; the disk of radius $r$ and centered at the crack tip is denoted as $\mathscr{B}_r$. The $J$-integral near the tip is taken on $\Gamma_r$ and in the far field on $\Gamma_{\text{far}}$.

deformational and configurational force balances result in (Simha et al., 2003)

$$
\nabla \cdot \mathbf{S}=\mathbf{0}, \quad \nabla \cdot \mathbf{C}+\mathbf{f}=\mathbf{0} \quad \text { in the body } \mathscr{B},
\tag{2.1}
$$

$$
\mathbf{S} \hat{\mathbf{p}}=\mathbf{0}, \quad [\mathbf{C}] \hat{\mathbf{p}}=\mathbf{0} \quad \text { on the crack faces, }
\tag{2.2}
$$

$$
\lim _{r \rightarrow 0} \int_{\Gamma_{r}} \mathbf{S} \hat{\mathbf{m}} \mathrm{d} l=\mathbf{0}, \quad \lim _{r \rightarrow 0} \int_{\Gamma_{r}} \mathbf{C} \hat{\mathbf{m}} \mathrm{d} l+\mathbf{f}_{T}=\mathbf{0} \quad \text { at the crack tip. }
\tag{2.3}
$$

Here $\Gamma_r$ designates the crack tip contour with its unit normal vector $\hat{\mathbf{m}}$. The vector $\hat{\mathbf{p}}$ is the unit normal to the crack faces and $\llbracket \rrbracket$ denotes the jump across the crack face. The symbol $\nabla$ denotes the gradient operator described in the reference configuration and $\nabla \cdot$ the divergence. Eq. $(2.1)_1$ is the standard equilibrium equation of continuum mechanics. Eq. $(2.2)_1$ says that crack faces are traction free, while Eq. $(2.3)_1$ requires the limiting value of the integral of the singular stress to vanish. These equations correspond to the quasistatic crack problem, and are satisfied by the K-field of LEFM, for instance. The corresponding relations for the configurational forces $(2.1)_2,(2.2)_2$ and $(2.3)_2$, are derived in Simha et al. (2005) following Gurtin's configurational forces approach (Gurtin, 1995), and we note that their validity can be readily verified using alternative methods, e.g. Maugin (1995).

The Clausius-Duhem inequality (second law of thermodynamics) requires that the dissipation $\Psi(\mathscr{D})$ be non-negative for every subregion $\mathscr{D}$ of the body $\mathscr{B}$; the dissipation is the difference between the rate of working and the rate of change of energy. Applying certain invariance requirements on the Clausius-Duhem inequality results in the following: First, the bulk configurational stress is (Gurtin, 1995)

$$
\mathbf{C}=\phi \mathbf{I}-\mathbf{F}^{\mathrm{T}} \mathbf{S},
\tag{2.4}
$$

where $\phi$ is the (Helmholtz) potential or the stored energy density, $\mathbf{I}$ is the identity tensor and $\mathbf{F}$ is the deformation gradient. Thus $\mathbf{C}$ is Eshelby's energy-momentum tensor (Eshelby, 1970). Second, the dissipation $\Psi(\mathscr{D})$ in any part of the body $\mathscr{D}$ containing the crack tip is (Gurtin and Podio-Guidugli, 1996)

$$
\Psi(\mathscr{D})=\int_{\mathscr{D}}\left(\mathbf{S} \cdot \dot{\mathbf{F}}-\dot{\phi}\right) \mathrm{d} A+\mathbf{v}_{T} \cdot \lim _{r \rightarrow 0} \int_{\Gamma_{r}}\left(\phi \mathbf{I}-\mathbf{F}^{\mathrm{T}} \mathbf{S}\right) \hat{\mathbf{m}} \mathrm{d} l \geqslant 0,
\tag{2.5}
$$

where $\dot{\mathbf{F}}$ denotes the time derivative of $\mathbf{F}$ (at fixed points in the reference configuration, i.e. at fixed $\mathbf{x} \in \mathscr{B}$) and $\mathbf{v}_{T}$ is the crack tip velocity (in the reference configuration). Eqs. (2.4) and (2.5) are also derived in Simha et al. (2003).

Now that the configurational stress is known, the force balances $(2.1)_2,(2.3)_2$ are used to obtain the configurational forces in the body and at the crack tip as

$$
\mathbf{f}=-\nabla \cdot\left(\phi \mathbf{I}-\mathbf{F}^{\mathrm{T}} \mathbf{S}\right),
\tag{2.6}
$$

$$
\mathbf{f}_{T}=-\lim _{r \rightarrow 0} \int_{\Gamma_{r}}\left(\phi \mathbf{I}-\mathbf{F}^{\mathrm{T}} \mathbf{S}\right) \hat{\mathbf{m}} \mathrm{d} l.
\tag{2.7}
$$

Localizing Eq. (2.5), we obtain the dissipation at each point in the body as (Simha et al., 2003)

$$
\psi_{\text {bulk }}=\mathbf{S} \cdot \dot{\mathbf{F}}-\dot{\phi} \geqslant 0,
\tag{2.8}
$$

whereas the dissipation due to the crack tip moving with a velocity $\mathbf{v}_T$ is

$$
\psi_{\text{tip}} = (-\mathbf{f}_T) \cdot \mathbf{v}_T \geqslant 0. \tag{2.9}
$$

Eq. (2.9) states the second law of thermodynamics for the crack tip; hence, by following standard reasoning, we identify $(-\mathbf{f}_T)$ as the crack driving force, since it is the force term conjugate to the crack tip velocity. The energy dissipated per unit crack extension is equal to

$$
J_{\text{tip}} = \hat{\mathbf{e}} \cdot (-\mathbf{f}_T) = \hat{\mathbf{e}} \cdot \lim_{r \to 0} \int_{\Gamma_r} (\phi \mathbf{I} - \mathbf{F}^\mathrm{T} \mathbf{S}) \hat{\mathbf{m}} \mathrm{d}l \geqslant 0, \tag{2.10}
$$

where the unit vector $\hat{\mathbf{e}} = \mathbf{v}_T/|\mathbf{v}_T|$ lies along the direction of crack growth. This is Rice's $J$-integral written in direct notation for the finite strain setting and is consistent with formulations in Freund and Hutchinson (1985) and Moran and Shih (1987). The near-tip $J$-integral, $J_{\text{tip}}$, is a scalar crack driving force since it is obtained as the projection of the vector driving force $(-\mathbf{f}_T)$ along the direction of crack growth $\hat{\mathbf{e}}$. In terms of $J_{\text{tip}}$, the dissipation due to the crack tip can be written as

$$
\psi_{\text{tip}} = |\mathbf{v}_T| J_{\text{tip}} \geqslant 0. \tag{2.11}
$$

Lastly, the configurational force balance for a region that does not contain the crack tip is used to relate the near-tip and far-field $J$-integrals. Consider the region $\mathscr{D}$ between a circle close to the tip $\Gamma_r$ and another contour $\Gamma$ that encloses the tip contour (Fig. 1); this region does not include the crack tip or the region inside $\Gamma_r$. Thus only the configurational body force and contact forces act on this region, so the statement of configurational force balance for region $\mathscr{D}$ is

$$
\int_{\mathscr{D}} \mathbf{f} \mathrm{d}A + \int_{\Gamma} \mathbf{C} \hat{\mathbf{m}} \mathrm{d}l - \int_{\Gamma_r} \mathbf{C} \hat{\mathbf{m}} \mathrm{d}l = 0.
$$

Next, using representation equation (2.4) and taking the scalar product of the above equation with $\hat{\mathbf{e}}$, we get for $r \to 0$ the expression

$$
J_{\text{tip}} - J_{\Gamma} = \hat{\mathbf{e}} \cdot \int_{\mathscr{D}} \mathbf{f} \mathrm{d}A, \tag{2.12}
$$

where $J_{\Gamma}$ is the $J$-integral on the contour $\Gamma$ given by

$$
J_{\Gamma} = \hat{\mathbf{e}} \cdot \int_{\Gamma} (\phi \mathbf{I} - \mathbf{F}^\mathrm{T} \mathbf{S}) \hat{\mathbf{m}} \mathrm{d}l. \tag{2.13}
$$

If we let $\Gamma$ become a contour adjacent to the external boundary of the cracked body, then

$$
J_{\text{tip}} - J_{\text{far}} = \hat{\mathbf{e}} \cdot \int_{\mathscr{B}} \mathbf{f} \mathrm{d}A, \tag{2.14}
$$

where the area integral is performed over the entire body $\mathscr{B}$ and $J_{\text{far}}$ is taken on the far-field contour $\Gamma_{\text{far}}$. We reiterate that all the above relations have been derived without making any assumptions about the constitutive nature of the body.

## 3. Cracks in elastic-plastic bodies

We will now show that the configurational body force does not vanish in homogeneous elastic-plastic materials and thereby elucidate how plastic deformation influences the crack driving force. The finite strain setting is considered first and then the small strain setting.

### 3.1. Finite plasticity

We collect relevant relations from standard continuum models of plasticity, e.g. Maugin (1999) and Lubarda (2002). First, the total deformation is expressed via an intermediate configuration by assuming that the elastic deformation follows plastic deformation. Then the corresponding deformation gradients are given by

$$
\mathbf{F} = \mathbf{F}^\mathrm{e} \mathbf{F}^\mathrm{p}. \tag{3.1}
$$

Only the total deformation gradient $\mathbf{F}$ is a gradient of a vector field. Specifically, the plastic component of the deformation gradient $\mathbf{F}^\mathrm{p}$ is not the gradient of a vector field, and standard compatibility conditions for gradients are not satisfied by $\mathbf{F}^\mathrm{p}$. We presume that the plastic deformation is incompressible $(\det \mathbf{F}^\mathrm{p} = 1)$. Next, for homogeneous elastic-plastic materials, the (Helmholtz) free energy density $\phi$ has the form

$$
\phi = \phi(\mathbf{F}^\mathrm{e}, \alpha), \tag{3.2}
$$

where $\alpha$ is an internal variable introduced to account for isotropic hardening effects (for simplicity, kinematic hardening effects are neglected). Thus the stored energy depends on the elastic deformation gradient $\mathbf{F}^\mathrm{e}$ and the internal variable $\alpha$. This is appropriate for isotropic homogeneous elastic-plastic bodies in the finite strain setting.

The dissipation in the bulk (2.8) now reduces to

$$
\psi_{\mathrm{bulk}}=\left(\mathbf{S}\left(\mathbf{F}^{\mathrm{p}}\right)^{\mathrm{T}}-\frac{\partial \phi}{\partial \mathbf{F}^{\mathrm{e}}}\right) \cdot \dot{\mathbf{F}}^{\mathrm{e}}+\mathbf{S} \cdot \mathbf{F}^{\mathrm{e}} \dot{\mathbf{F}}^{\mathrm{p}}-\frac{\partial \phi}{\partial \alpha} \dot{\alpha} \geqslant 0.
$$

Since this is to be non-negative for all processes, we appeal to the Coleman-Noll argument and obtain the 1st Piola-Kirchoff stress as

$$
\mathbf{S}=\frac{\partial \phi}{\partial \mathbf{F}^{\mathrm{e}}}\left(\mathbf{F}^{\mathrm{p}}\right)^{-\mathrm{T}}. \tag{3.3}
$$

Then the bulk dissipation simplifies to

$$
\psi_{\mathrm{bulk}}=\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{S} \cdot \dot{\mathbf{F}}^{\mathrm{p}}-\frac{\partial \phi}{\partial \alpha} \dot{\alpha} \geqslant 0. \tag{3.4}
$$

This agrees with results of Maugin (1994), who also gives alternative expressions for the dissipation that do not depend on the plastic spin.

Next we calculate the configurational body force (2.6). This is best done in component form, so let $x_{i}$ denote Cartesian coordinates of vector $\mathbf{x}$ in the reference configuration. Then

$$
-f_{i}=\left(\phi \delta_{i j}-F_{i k}^{\mathrm{T}} S_{k j}\right)_{, j}=\phi_{, i}-F_{k i, j} S_{k j},
$$

where $\partial / \partial x_{i}=_{, i}, \delta_{i j}$ is the Kronecker delta function and the second equality is obtained using the equilibrium condition $(S_{k j j}=0)$. Using Eqs. (3.2) and (3.3) we get

$$
\phi_{, i}=\frac{\partial \phi}{\partial F_{k l}^{\mathrm{e}}} F_{k l, i}^{\mathrm{e}}+\frac{\partial \phi}{\partial \alpha} \alpha_{, i}=S_{k m} F_{l m}^{\mathrm{p}} F_{k l, i}^{\mathrm{e}}+\frac{\partial \phi}{\partial \alpha} \alpha_{, i}
$$

and

$$
-f_{i}=\frac{\partial \phi}{\partial \alpha} \alpha_{, i}+S_{k m}\left(F_{l m}^{\mathrm{p}} F_{k l, i}^{\mathrm{e}}-F_{k i, m}\right).
$$

The full deformation gradient $\mathbf{F}$ is the gradient of a vector field, so the compatibility condition is that the order of partial differentiation can be reversed, i.e. $F_{k i, m}=F_{k m, i}$. Then using Eq. (3.1) we get

$$
F_{k m, i}=\left(F_{k l}^{\mathrm{e}} F_{l m}^{\mathrm{p}}\right)_{, i}=F_{k l, i}^{\mathrm{e}} F_{l m}^{\mathrm{p}}+F_{k l}^{\mathrm{e}} F_{l m, i}^{\mathrm{p}}.
$$

Consequently, the configurational body force due to plasticity has the form

$$
f_{i}=S_{k m}\left(F_{k l}^{\mathrm{e}} F_{l m, i}^{\mathrm{p}}\right)-\frac{\partial \phi}{\partial \alpha} \alpha_{, i},
$$

or in direct notation

$$
\mathbf{f}=\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{S} \cdot \frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial \mathbf{x}}-\frac{\partial \phi}{\partial \alpha} \frac{\partial \alpha}{\partial \mathbf{x}}. \tag{3.5}
$$

The component of the configurational body force along the crack growth direction is

$$
\mathbf{f} \cdot \hat{\mathbf{e}}=\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{S} \cdot \frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial x_{1}}-\frac{\partial \phi}{\partial \alpha} \frac{\partial \alpha}{\partial x_{1}}, \tag{3.6}
$$

where $x_{1}=\mathbf{x} \cdot \hat{\mathbf{e}}$ is the coordinate parallel to the direction of crack growth. Notice that this expression for $\mathbf{f} \cdot \hat{\mathbf{e}}$ contains the same quantities as the plastic dissipation in the bulk (3.4), except that the derivative with respect to time has been replaced by the derivative with respect to the direction of crack growth $x_{1}$. Remember that $\mathbf{f} \cdot \hat{\mathbf{e}}$ appears in the relation between the near-tip and far-field $J$-integrals (2.14). The bulk dissipation $\psi_{\text {bulk }}$ gives the energy dissipated per unit volume and per unit time (2.8), whereas the quantity $\mathbf{f} \cdot \hat{\mathbf{e}}$ in Eq. (2.14) is related to the energy consumed or released by plasticity at a material point per unit crack growth through Eq. (3.6). It is a crack driving force term that appears at a material point due to plastic deformation (3.6). Note that, contrary to Eq. (3.4), the quantity $\mathbf{f} \cdot \hat{\mathbf{e}}$ in (3.6) can be positive or negative, depending mainly on the gradient of the plastic component of the deformation gradient in the crack growth direction (when neglecting the hardening effect).

The effect of plastic deformation in a pre-cracked body is obtained by integrating the component of the configurational body force along the crack growth direction,

$$
\begin{aligned}
C_{\mathrm{p}} & =\hat{\mathbf{e}} \cdot \int_{\mathscr{A}}\left[\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{S} \cdot \frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial \mathbf{x}}-\frac{\partial \phi}{\partial \alpha} \frac{\partial \alpha}{\partial \mathbf{x}}\right] \mathrm{d} A \\
& =\int_{\mathscr{A}}\left[\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{S} \cdot \frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial x_{1}}-\frac{\partial \phi}{\partial \alpha} \frac{\partial \alpha}{\partial x_{1}}\right] \mathrm{d} A.
\end{aligned} \tag{3.7}
$$

We call this the "plasticity influence term", $C_{\mathrm{p}}$. It is the total configurational force due to plasticity, projected on the crack growth direction and is obtained by integrating Eq. (3.6) over the body. It then follows from Eq. (2.14), that the near-tip and

the far-field $J$-integrals are related through

$$J_{\mathrm{tip}}=J_{\mathrm{far}}+C_{\mathrm{p}}.\tag{3.8}$$

For homogeneous hyperelastic materials $\phi=\phi(\mathbf{F}^{\mathrm{e}})$ with $\mathbf{F}^{\mathrm{p}}=\mathbf{I}$ and $\alpha\equiv0$, the configurational body force and the plasticity influence term $C_{\mathrm{p}}$ vanish, and Eq. (3.8) implies the path independence of the $J$-integral. In contrast, gradients in the plastic strain or the internal hardening variable will contribute to the configurational body force and thereby to the plastic influence term, even in homogeneous elastic-plastic materials. If $C_{\mathrm{p}}<0$, plasticity exerts a shielding effect: the effective crack driving force at the tip is smaller than the externally applied crack driving force. If $C_{\mathrm{p}}>0$, an anti-shielding effect occurs, and the crack tip experiences a higher crack driving force than externally applied (e.g. due to back face plastic deformation in C(T)-specimens as in Section 5).

For steady-state crack growth, we can prove that $C_{\mathrm{p}}$ is equal to the negative of the total energy required for plastic deformation per unit crack extension and that $C_{\mathrm{p}}\leqslant0$. Let $(\xi_{1},\xi_{2})$ denote Cartesian coordinates with origin at the moving crack tip. Visualizing a straight horizontal crack of length $a$ in Fig. 1, we have $\xi_{1}(t)=x_{1}-a(t)$ and $\xi_{2}(t)=x_{2}$ where $(x_{1},x_{2})$ are fixed Cartesian coordinates in the reference configuration. Thus

$$\left.\frac{\partial}{\partial x_{1}}\right|_{t}=\left.\frac{\partial}{\partial \xi_{1}}\right|_{t} \quad \text{and} \quad \left.\frac{\partial}{\partial t}\right|_{x_{1}}=\left.\frac{\partial}{\partial \xi_{1}} \frac{\partial \xi_{1}}{\partial t}\right|_{x_{1}}=-\dot{a} \frac{\partial}{\partial \xi_{1}},$$

where $\dot{a}=\mathrm{d}a/\mathrm{d}t\geqslant0$. For steady-state crack propagation, the bulk dissipation (3.4) and the plasticity influence term (3.7) become

$$\psi_{\mathrm{bulk}}=-\dot{a}\left[(\mathbf{F}^{\mathrm{e}})^{\mathrm{T}}\mathbf{S}\cdot\frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial \xi_{1}}-\frac{\partial \phi}{\partial \alpha}\frac{\partial \alpha}{\partial \xi_{1}}\right]\geqslant0,\tag{3.9}$$

$$C_{\mathrm{p}}=\int_{\mathscr{A}}\left[(\mathbf{F}^{\mathrm{e}})^{\mathrm{T}}\mathbf{S}\cdot\frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial \xi_{1}}-\frac{\partial \phi}{\partial \alpha}\frac{\partial \alpha}{\partial \xi_{1}}\right]\mathrm{d}A.\tag{3.10}$$

Comparing Eqs. (3.9) and (3.10), we see that the dissipation in the entire bulk of the body, but excluding the crack tip, is given by

$$\Psi_{\mathrm{bulk}}=\int_{\mathscr{A}}\psi_{\mathrm{bulk}}\mathrm{d}A=-\dot{a}C_{\mathrm{p}}.\tag{3.11}$$

In this homogeneous incremental elastic-plastic context, we can write $\Psi_{\mathrm{bulk}}=\dot{W}_{\mathrm{p}}=\dot{a}(\mathrm{d}W_{\mathrm{p}}/\mathrm{d}a)$ where $W_{\mathrm{p}}$ denotes the plastic work in the entire body. Thus $C_{\mathrm{p}}=-(\mathrm{d}W_{\mathrm{p}}/\mathrm{d}a)$ and the plasticity influence term is equal to the negative of the total energy required for plastic deformation per unit crack growth under steady-state conditions. Next, since $\dot{a}>0$ and $\Psi_{\mathrm{bulk}}$ is by definition non-negative, it follows from Eq. (3.11) that

$$C_{\mathrm{p}}\leqslant0 \quad \text{and} \quad J_{\mathrm{tip}}\leqslant J_{\mathrm{far}} \quad \text{for steady-state crack growth.}\tag{3.12}$$

This means that for steady-state crack growth plasticity could exert a shielding effect which reduces the crack driving force, but not an anti-shielding effect. Lastly, by including the dissipation at the crack tip (2.11), we can write the total dissipation in the body as

$$\Psi(\mathscr{B})=\dot{a}[J_{\mathrm{tip}}-C_{\mathrm{p}}]=\dot{a}J_{\mathrm{far}} \quad \text{for steady-state crack growth.}\tag{3.13}$$

A corresponding relation was found by Nguyen et al. (2005) but only in the small strain context.

For more general situations, like non-steady state crack extension, one possibility is to treat the time $t$ as being parametrized by the load line displacement via $v_{\mathrm{LL}}=\dot{v}_{\mathrm{LL}}t$ with a constant $\dot{v}_{\mathrm{LL}}>0$. The crack tip coordinates can now be written as $\xi_{1}=x_{1}-a(v_{\mathrm{LL}})$ and $\xi_{2}=x_{2}$. Then for a function described as $f(x_{1},x_{2},t)=\hat{f}(\xi_{1},\xi_{2},v_{\mathrm{LL}})$ the derivative $\dot{f}$ can be written as

$$
\begin{aligned}
\left.\frac{\mathrm{d}f(x_{1},x_{2},t)}{\mathrm{d}t}\right|_{x_{1},x_{2}}&=\left[\frac{\partial \hat{f}(\xi_{1},\xi_{2},v_{\mathrm{LL}})}{\partial v_{\mathrm{LL}}}+\frac{\partial \hat{f}(\xi_{1},\xi_{2},v_{\mathrm{LL}})}{\partial \xi_{1}}\frac{\partial \xi_{1}}{\partial v_{\mathrm{LL}}}\right]\dot{v}_{\mathrm{LL}} \\
&=\left[f'-a'\frac{\partial \hat{f}}{\partial \xi_{1}}\right]\dot{v}_{\mathrm{LL}}=\dot{v}_{\mathrm{LL}}f'-\dot{a}\frac{\partial \hat{f}}{\partial \xi_{1}},
\end{aligned}
$$

where $'=\partial/\partial v_{\mathrm{LL}}$ and $\dot{a}=a'\dot{v}_{\mathrm{LL}}$. Then the dissipation at a point in an elastic-plastic body (3.4) becomes

$$\psi_{\mathrm{bulk}}=\dot{v}_{\mathrm{LL}}\left[(\mathbf{F}^{\mathrm{e}})^{\mathrm{T}}\mathbf{S}\cdot\mathbf{F}^{\mathrm{p}'}-\frac{\partial \phi}{\partial \alpha}\alpha'\right]-\dot{a}\left[(\mathbf{F}^{\mathrm{e}})^{\mathrm{T}}\mathbf{S}\cdot\frac{\partial \mathbf{F}^{\mathrm{p}}}{\partial \xi_{1}}-\frac{\partial \phi}{\partial \alpha}\frac{\partial \alpha}{\partial \xi_{1}}\right]\geqslant0.\tag{3.14}$$

Consequently, the total dissipation in a cracked elastic-plastic body can be rewritten using Eqs. (2.5), (2.11) and (3.7) as

$$
\begin{aligned}
\Psi(\mathscr{B})&=\dot{v}_{\mathrm{LL}}\int_{\mathscr{A}}\left[(\mathbf{F}^{\mathrm{e}})^{\mathrm{T}}\mathbf{S}\cdot\mathbf{F}^{\mathrm{p}'}-\frac{\partial \phi}{\partial \alpha}\alpha'\right]\mathrm{d}A+\dot{a}(J_{\mathrm{tip}}-C_{\mathrm{p}}) \\
&=\dot{v}_{\mathrm{LL}}\int_{\mathscr{A}}\left[(\mathbf{F}^{\mathrm{e}})^{\mathrm{T}}\mathbf{S}\cdot\mathbf{F}^{\mathrm{p}'}-\frac{\partial \phi}{\partial \alpha}\alpha'\right]\mathrm{d}A+\dot{a}J_{\mathrm{far}}.\tag{3.15}
\end{aligned}
$$

The second version follows from Eq. (3.8) and $C_p$ is given by the same expression as in Eq. (3.10), but with $\xi_1 = x_1 - a(v_{\text{LL}})$. Comparing Eqs. (3.13) and (3.15) shows that the integral in Eq. (3.15) accounts for non-steady-state state conditions, like for an evolving plastic zone. Contrary to the steady-state case (3.13), the total dissipation in the body is not related to $J_{\text{far}}$ in a simple manner.

### 3.2. Small strain plasticity

In the infinitesimal strain setting, relevant equations are

$$
\nabla \cdot \boldsymbol{\sigma}=0 \quad \text { in the cracked body, } \tag{3.16}
$$

$$
\boldsymbol{\sigma} \hat{\mathbf{p}}=0 \quad \text { on the crack faces, } \tag{3.17}
$$

$$
\boldsymbol{\varepsilon}=\boldsymbol{\varepsilon}^{\mathrm{e}}+\boldsymbol{\varepsilon}^{\mathrm{p}}, \tag{3.18}
$$

$$
\mathbf{C}=\left(\phi \mathbf{I}-\left(\mathbf{I}+\nabla \mathbf{u}^{\mathrm{T}}\right) \boldsymbol{\sigma}\right), \tag{3.19}
$$

$$
J_{\mathrm{tip}}=\hat{\mathbf{e}} \cdot \lim _{r \rightarrow 0} \int_{\Gamma_{r}}\left(\phi \mathbf{I}-\nabla \mathbf{u}^{\mathrm{T}} \boldsymbol{\sigma}\right) \hat{\mathbf{m}} \mathrm{d} l, \tag{3.20}
$$

$$
J_{\Gamma}=\hat{\mathbf{e}} \cdot \int_{\Gamma}\left(\phi \mathbf{I}-\nabla \mathbf{u}^{\mathrm{T}} \boldsymbol{\sigma}\right) \hat{\mathbf{m}} \mathrm{d} l, \tag{3.21}
$$

where $\boldsymbol{\sigma}$ is the Cauchy stress, $\mathbf{u}$ is the displacement, $\boldsymbol{\varepsilon}=(\nabla \mathbf{u}+\nabla \mathbf{u}^{\mathrm{T}})/2$ is the linear strain tensor, which is split into elastic ($\boldsymbol{\varepsilon}^{\mathrm{e}}$) and plastic ($\boldsymbol{\varepsilon}^{\mathrm{p}}$) parts and $\mathbf{C}$ is Eshelby's energy momentum tensor. The total strain $\boldsymbol{\varepsilon}$ is related to the gradient of a vector field $\mathbf{u}$, while the plastic part $\boldsymbol{\varepsilon}^{\mathrm{p}}$ is specifically not obtained from the gradient of a vector field. Maugin (1993) shows that the finite deformation $J$-integral (2.10) linearizes to Eq. (3.20), which is Rice's result written in direct notation (Rice, 1968a). Lastly, $J_{\Gamma}$ is the small strain $J$-integral over a contour $\Gamma$. The $\mathbf{I} \boldsymbol{\sigma}$ term in Eq. (3.19) does not make a contribution to either the $J$-integral or the configurational body force due to Eq. (3.16). A purely infinitesimal strain derivation would yield $\mathbf{C}=\phi \mathbf{I}-\nabla \mathbf{u}^{\mathrm{T}} \boldsymbol{\sigma}$, which is different from the limiting value of the finite-strain result (3.19); however the $J$-integral and configurational body force are the same.

The evolution of the plastic strain is determined by a yield surface and a flow rule. The deviatoric stress $\mathbf{s}=\boldsymbol{\sigma}-\left(\frac{1}{3}\right)\text{Tr}(\boldsymbol{\sigma})\mathbf{I}$ is the non-hydrostatic part of the total stress and is used to specify the yield surface as

$$
\frac{3}{2} \mathbf{s} \cdot \mathbf{s}=\sigma_{0}^{2}, \tag{3.22}
$$

where $\sigma_0$ is the yield stress of the material. When the stress state lies on the yield surface, the evolution of the plastic strain is given by a flow rule

$$
\dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}=\frac{3 \dot{\varepsilon}_{\mathrm{pv}}}{2 \sigma_{0}} \mathbf{s}, \tag{3.23}
$$

where $\varepsilon_{\text{pv}}$ is the equivalent plastic strain. Finally, the stored energy density $\phi(\boldsymbol{\varepsilon}^{\mathrm{e}}, \alpha)$ is split additively into an elastic part $\phi_{\mathrm{e}}(\boldsymbol{\varepsilon}^{\mathrm{e}})$ and a second part $\phi_{\mathrm{h}}(\alpha)$ with replacement of $\alpha$ by $\varepsilon_{\text{pv}}$ as

$$
\phi=\phi_{\mathrm{e}}\left(\boldsymbol{\varepsilon}^{\mathrm{e}}\right)+\phi_{\mathrm{h}}\left(\varepsilon_{\mathrm{pv}}\right). \tag{3.24}
$$

The first part of stored energy density ($\phi_{\mathrm{e}}$) depends only on the elastic strain, while the second part ($\phi_{\mathrm{h}}$), which depends on the equivalent plastic strain, takes into account the recoverable energy of the stored dislocations.

The dissipation in the bulk (2.8) now reduces to

$$
\psi_{\mathrm{bulk}}=\boldsymbol{\sigma} \cdot \dot{\boldsymbol{\varepsilon}}-\dot{\phi}=\left(\boldsymbol{\sigma}-\frac{\partial \phi_{\mathrm{e}}}{\partial \boldsymbol{\varepsilon}^{\mathrm{e}}}\right) \cdot \dot{\boldsymbol{\varepsilon}}^{\mathrm{e}}+\boldsymbol{\sigma} \cdot \dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \dot{\varepsilon}_{\mathrm{pv}} \geqslant 0.
$$

Since this is to be non-negative for all processes, we again appeal to the Coleman-Noll argument and obtain the Cauchy stress as

$$
\boldsymbol{\sigma}=\frac{\partial \phi_{\mathrm{e}}}{\partial \boldsymbol{\varepsilon}^{\mathrm{e}}}, \tag{3.25}
$$

and the bulk dissipation reduces to

$$
\psi_{\mathrm{bulk}}=\boldsymbol{\sigma} \cdot \dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \dot{\varepsilon}_{\mathrm{pv}} \geqslant 0. \tag{3.26}
$$

Next we calculate the configurational body force (2.6). Let $x_i$ denote Cartesian coordinates, then using Eq. (3.19) we get

$$
-f_{i}=\left(\phi \delta_{i j}-\left[\delta_{i k}+\left(\nabla \mathbf{u}^{\mathrm{T}}\right)_{i k}\right] \sigma_{k j}\right)_{, j}=\phi_{, i}-u_{k, i j} \sigma_{k j}=\phi_{, i}-\varepsilon_{k j, i} \sigma_{k j}.
$$

Above, the second equality is obtained using the equilibrium condition $(\sigma_{kj,j} = 0)$ while the third follows since the Cauchy stress is symmetric and the total strain is related to the gradient of a vector field (so the compatibility condition allows us to change the order of partial differentiation). Using Eqs. (3.24) and (3.25) we get

$$
\phi_{, i}=\frac{\partial \phi_{\mathrm{e}}}{\partial \varepsilon_{k j}^{\mathrm{e}}} \varepsilon_{k j, i}^{\mathrm{e}}+\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial x_{i}}=\sigma_{k j} \varepsilon_{k j, i}^{\mathrm{e}}+\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial x_{i}}.
$$

Finally, the additive decomposition of the total strain (3.18) implies

$$
-f_{i}=\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial x_{i}}-\sigma_{k j} \varepsilon_{k j, i}^{\mathrm{p}}.
$$

Consequently, the configurational body force due to plasticity gets the form

$$
\mathbf{f}=\boldsymbol{\sigma} \cdot \frac{\partial \boldsymbol{\varepsilon}^{\mathrm{p}}}{\partial \mathbf{X}}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial \mathbf{X}},
$$

and the component of the configurational body force along the crack growth direction is

$$
\mathbf{f} \cdot \hat{\mathbf{e}}=\boldsymbol{\sigma} \cdot \frac{\partial \boldsymbol{\varepsilon}^{\mathrm{p}}}{\partial x_{1}}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial x_{1}}.
$$

As in the finite strain case (cf. Eqs. (3.4) and (3.6)), notice that $\mathbf{f} \cdot \hat{\mathbf{e}}$ contains the same quantities as the plastic dissipation in the bulk (cf. Eqs. (3.26) and (3.28)) except that the derivative with respect to time has been replaced by the derivative with respect to the direction of crack growth $x_{1}$. Lastly, by integrating $\mathbf{f} \cdot \hat{\mathbf{e}}$, the plasticity influence term is

$$
\begin{aligned}
C_{\mathrm{p}} & =\hat{\mathbf{e}} \cdot \int_{\mathscr{A}}\left[\boldsymbol{\sigma} \cdot \frac{\partial \boldsymbol{\varepsilon}^{\mathrm{p}}}{\partial \mathbf{X}}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial \mathbf{X}}\right] \mathrm{d} A \\
& =\int_{\mathscr{A}}\left(\sigma_{j k} \frac{\partial \varepsilon_{j k}^{\mathrm{p}}}{\partial x_{1}}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial x_{1}}\right) \mathrm{d} A.
\end{aligned}
$$

As before the difference between the near-tip and far-field $J$-integrals is equal to the plasticity influence term (3.8).

For steady-state crack growth, the plasticity influence term satisfies $C_{\mathrm{p}} \leqslant 0$, so $J_{\text {tip }} \leqslant J_{\text {far }}$. Thus plasticity can exert a shielding effect, but not an anti-shielding effect and the total dissipation in the body is given by Eq. (3.13) under steady-state conditions. For non-steady conditions, with time parametrized via the load line displacement, the total dissipation in the body, including the crack tip, becomes

$$
\begin{aligned}
\Psi(\mathscr{B}) & =\dot{v}_{\mathrm{LL}} \int_{\mathscr{A}}\left(\sigma_{j k} \varepsilon_{j k}^{\mathrm{p} \prime}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \varepsilon_{\mathrm{pv}}^{\prime}\right) \mathrm{d} A+\dot{a}\left(J_{\text {tip }}-C_{\mathrm{p}}\right) \\
& =\dot{v}_{\mathrm{LL}} \int_{\mathscr{A}}\left(\sigma_{j k} \varepsilon_{j k}^{\mathrm{p} \prime}-\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}} \varepsilon_{\mathrm{pv}}^{\prime}\right) \mathrm{d} A+\dot{a} J_{\mathrm{far}} .
\end{aligned}
$$

which is analogous to the finite strain expression (3.15).

## 4. Special cases

### 4.1. Deformation plasticity or proportional loading

Here the plastic strain is obtained by integrating the flow rule (3.23) as

$$
\varepsilon^{\mathrm{p}}=\frac{3 \varepsilon_{\mathrm{pv}}}{2 \sigma_{0}} \mathbf{s}.
$$

The hardening part of the stored energy density is obtained as

$$
\phi_{\mathrm{h}}\left(\varepsilon_{\mathrm{pv}}\right)=\int_{0}^{\varepsilon_{\mathrm{pv}}} \sigma_{0}\left(\tilde{\varepsilon}_{\mathrm{pv}}\right) \mathrm{d} \tilde{\varepsilon}_{\mathrm{pv}},
$$

yielding

$$
\frac{\partial \phi_{\mathrm{h}}}{\partial \varepsilon_{\mathrm{pv}}}=\sigma_{0} .
$$

Typically, deformation plasticity is treated as non-linear elasticity along with the path independence of the $J$-integral. In this setting we now show that the plasticity influence term (3.29) vanishes for deformational plasticity.

The gradient of the plastic strain is

$$
\frac{\partial \boldsymbol{\varepsilon}^{\mathrm{p}}}{\partial \mathbf{X}}=\frac{3 \mathbf{s}}{2} \frac{\partial}{\partial \mathbf{X}}\left(\frac{\varepsilon_{\mathrm{pv}}}{\sigma_{0}}\right)+\frac{3 \varepsilon_{\mathrm{pv}}}{2 \sigma_{0}} \frac{\partial \mathbf{s}}{\partial \mathbf{X}} .
$$

Thus the first term of the integrand in the plasticity influence term (3.29) becomes with (3.22)

$$
\begin{aligned}
\boldsymbol{\sigma} \cdot \frac{\partial \varepsilon^{\mathrm{p}}}{\partial \mathbf{X}} & =\left[\frac{3}{2} \mathbf{s} \cdot \mathbf{s}\right] \frac{\partial}{\partial \mathbf{X}}\left(\frac{\varepsilon_{\mathrm{pv}}}{\sigma_{0}}\right)+\left[\frac{3}{2} \mathbf{s} \cdot \frac{\partial \mathbf{s}}{\partial \mathbf{X}}\right] \frac{\varepsilon_{\mathrm{pv}}}{\sigma_{0}} \\
& =\sigma_{0}^{2} \frac{\partial}{\partial \mathbf{X}}\left(\frac{\varepsilon_{\mathrm{pv}}}{\sigma_{0}}\right)+\left[\frac{1}{2} \frac{\partial \sigma_{0}^{2}}{\partial \mathbf{X}}\right] \frac{\varepsilon_{\mathrm{pv}}}{\sigma_{0}} \\
& =\sigma_{0} \frac{\partial \varepsilon_{\mathrm{pv}}}{\partial \mathbf{X}}.
\end{aligned}
$$

Since this is exactly the second term of the integrand in Eq. (3.29), the plasticity influence term vanishes identically,

$$C_{\mathrm{p}}=0 \quad \text { and } \quad J_{\text {tip }}=J_{\text {far }} \quad \text { for deformation plasticity. }\qquad(4.1)$$

So the $J$-integral is path independent in homogeneous deformation plasticity.

### 4.2. Rigid plasticity
Here the stored elastic energy density vanishes ($\phi_{\mathrm{e}}=0$, $\phi=\phi_{\mathrm{h}}$). The stress is no longer defined by Eq. (3.25), but specified in terms of the plastic strain which is equal to the total strain. Then, using $u_{j, k i}=u_{j, i k}$ and the equilibrium condition (3.16), we get
$$\sigma_{j k} \varepsilon_{j k, i}=\sigma_{j k} u_{j, i k}=\left(\sigma_{j k} u_{j, i}\right)_{, k}.$$

Since $\phi=\phi_{\mathrm{h}}(\varepsilon^{\mathrm{pv}})$ we get
$$\frac{\partial \phi}{\partial \varepsilon^{\mathrm{pv}}} \frac{\partial \varepsilon^{\mathrm{pv}}}{\partial X_{i}}=\frac{\partial \phi}{\partial X_{i}}=\left(\phi \delta_{i k}\right)_{, k}.$$

The plasticity influence term (3.29) reduces to
$$C_{\mathrm{p}}=e_{i} \int_{\mathscr{B}}\left(\sigma_{j k} u_{j, i}-\phi \delta_{i k}\right)_{, k} \mathrm{~d} A=e_{i} \int_{\partial \mathscr{B}}\left(u_{j, i} \sigma_{j k}-\phi \delta_{i k}\right) m_{k} \mathrm{~d} l,\qquad(4.2)$$
where the divergence theorem was used to obtain the contour integral. On the crack faces, $\sigma_{j k} m_{k}=e_{i} m_{i}=0$, so we can replace $\partial \mathscr{B}$ with the far-field contour $\Gamma_{far }$ to get
$$C_{\mathrm{p}}=\mathbf{e} \cdot \int_{\Gamma_{\text {far }}}\left(\nabla \mathbf{u}^{\mathrm{T}} \boldsymbol{\sigma}-\phi \mathbf{I}\right) \hat{\mathbf{m}} \mathrm{d} l.\qquad(4.3)$$

Notice that this is exactly the negative of the $J$-integral (3.21) over the far-field. Thus,
$$C_{\mathrm{p}}=-J_{\text {far }} \quad \text { and } \quad J_{\text {tip }}=0 \quad \text { for rigid plastic materials. }\qquad(4.4)$$

Consequently, the crack driving force vanishes for a rigid, hardening material.

### 4.3. Elastic-ideal plasticity
Here the stored energy density is equal to the elastic strain energy density ($\phi=\phi_{\mathrm{e}}$) as ($\phi_{\mathrm{h}}=0$), so $\phi_{, i}=\sigma_{j k} \varepsilon_{j k, i}^{\mathrm{e}}$. The second term in the integrand for the plasticity influence term (3.29) vanishes, then using Eq. (3.18) we get
$$C_{\mathrm{p}}=e_{i} \int_{\mathscr{B}}\left(\sigma_{j k} \varepsilon_{j k, i}-\sigma_{j k} \varepsilon_{j k, i}^{\mathrm{e}}\right) \mathrm{d} A=e_{i} \int_{\mathscr{B}}\left(\sigma_{j k} u_{j i, k}-\left(\phi \delta_{i k}\right)_{, k}\right) \mathrm{d} A.$$

Then following the reasoning behind Eqs. (4.2) and (4.3), we find that
$$C_{\mathrm{p}}=-J_{\text {far }} \quad \text { and } \quad J_{\text {tip }}=0 \quad \text { for elastic-ideally plastic materials. }\qquad(4.5)$$

Consequently, the crack driving force vanishes for a elastic-ideally plastic material.

## 5. Crack in an elastic-plastic C(T)-specimen
Here we will examine the influence of plastic deformation near the crack tip and in remote regions by performing a computational study using a C(T)-specimen with a stationary crack (thickness $B=25$ mm, width $W=50$ mm, crack length $a=25$ mm). The material is an annealed mild steel with the German designation St37. The material data are Young's modulus $E=200$ GPa, Poisson's ratio $v=0.3$, yield strength $\sigma_{y}=270$ MPa, ultimate tensile strength $\sigma_{u}=426$ MPa, average strain hardening coefficient $n=0.2$. The plastic deformation is described by a true stress vs. true plastic strain curve, shown in Chen et al. (2003). The internal hardening variable $\varkappa$ is taken to be the equivalent plastic strain $\varepsilon_{\mathrm{pv}}$. A conventional stress analysis is performed with ABAQUS (http//www.hks.com, Vers. 6.4) using a uniform mesh of standard four node elements (mesh size 0.5 mm) with the large deformation option. The loading is simulated by prescribing the load line displacement $v_{\mathrm{LL}}$.

The stress, total and plastic strain fields are evaluated in the context of incremental plasticity assuming plane strain conditions.

### 5.1. Computation of configurational forces and J-integrals

After the stress analysis, the configurational force $\mathbf{f}$ is evaluated at each node from Eq. (2.6) by post-processing, following e.g. Mueller et al. (2002), Mueller et al. (2004), Denzer et al. (2003) and more details will be given elsewhere (Kolednik et al., 2007).

The far-field $J$-integral can be written in terms of the configurational body force by using Eqs. (2.4) and (2.13), the divergence theorem, and Eqs. (2.1) and (2.2) as follows:

$$
J_{\mathrm{far}}=\hat{\mathbf{e}} \cdot \int_{\Gamma_{\mathrm{far}}} \mathbf{C} \hat{\mathbf{m}} \mathrm{d} l=\hat{\mathbf{e}} \cdot \int_{\mathscr{B}} \nabla \cdot \mathbf{C} \mathrm{d} A=-\hat{\mathbf{e}} \cdot \int_{\mathscr{B}} \mathbf{f} \mathrm{d} A,
$$

where $\Gamma_{\text {far }}$ coincides with the external boundary of the cracked body (Fig. 1). Consequently, $J_{\text {far }}$ is evaluated computationally as

$$
J_{\mathrm{far}} \approx \sum_{\text {elements in } \mathscr{B}}-(\hat{\mathbf{e}} \cdot \mathbf{f}) \Delta A_{\mathrm{e}},
$$

where $\Delta A_{\mathrm{e}}$ denotes the element area and the summation is performed over all elements in the interior of the body. The external boundary is like an interface (between the body and air), which results in non-zero values for the configurational force (Simha et al., 2005). Consequently, the elements adjacent to the external surface are not included in the sum in Eq. (5.1). The results below show that the configurational forces vanish outside the contour $\Gamma_{2}$ which is at a distance of $2 \mathrm{~mm}$ in front of the crack tip in Fig. 2. Consequently, the $J$-integral over this contour, $J_{\Gamma 2}$, was obtained by evaluating the sum in Eq. (5.1) only over the elements within $\Gamma_{2}$.

The configurational force component along the crack growth direction $\hat{\mathbf{e}} \cdot \mathbf{f}$, and $J$-integrals $J_{\Gamma 2}$ and $J_{\text {far }}$ were calculated as functions of the load-line displacement $v_{\mathrm{LL}}$. The incremental elastic-plastic quantities $\mathbf{f}^{\mathrm{ep}}, J_{\mathrm{far}}^{\mathrm{ep}}$ and $J_{\Gamma 2}^{\mathrm{ep}}$ are obtained by taking $\phi$ as the elastic strain energy density for post-processing. For comparison with current methods based on deformation plasticity, the corresponding non-linear elastic quantities, $\mathbf{f}^{\text {nl el }}, J_{\text {far }}^{\text {nl el }} J_{\Gamma 2}^{\text {nl el }}$ are obtained by taking $\phi$ as the total strain energy density (from the incremental plasticity finite-element stress analysis!) for post-processing.

The far-field $J$-integral values are compared to conventionally determined $J$-integral values. These are ABAQUS $J$-integral values which are calculated using the virtual crack extension method (Parks, 1977), in the following denomiated as $J^{\mathrm{VCE}}$, and experimental $J$-integral values as used in fracture mechanics experiments. It should be noted that deformation plasticity is implicitly assumed in the calculation of $J^{\mathrm{VCE}}$, i.e., the material is considered as being non-linear elastic. In standardized fracture mechanics experiments, e.g. ESIS P2-92 (1992), ASTM E1820 (2005), the experimental $J$-integral $J^{(A)}$ is determined from the area $A$ below the load vs. load-line displacement curve (Rice et al., 1973)

$$
J^{(A)}=\frac{\eta A}{b B},
$$

where $b=W-a$ denotes the ligament length, $B$ the specimen thickness and $\eta$ a geometry factor depending on the crack length to width ratio $a / W$. In some cases, the total area is divided into elastic and plastic parts, $A=A_{\mathrm{el}}+A_{\mathrm{pl}}$.

![](./images/811926939517321217_4.jpg)

Fig. 2. Distribution of configurational forces $\mathbf{f}^{\text {nl el }}$ near the crack tip of a non-linear elastic material at a load line displacement $v_{\mathrm{LL}}=0.35 \mathrm{~mm}$.

Correspondingly, $J^{(A)}$ can be also divided into elastic and plastic terms,

$$
J^{(A)}=J_{\mathrm{el}}^{(A)}+J_{\mathrm{pl}}^{(A)}=\frac{\eta A_{\mathrm{el}}}{b B}+\frac{\eta A_{\mathrm{pl}}}{b B}.
$$

It should be noted that the elastic part of the experimental $J$-integral, $J_{\mathrm{el}}^{(A)}$, is usually determined from the load, the crack length and the specimen geometry (ESIS P2-92, 1992; ASTM E1820, 2005). To the knowledge of the authors, the physical meaning of $J_{\mathrm{el}}^{(A)}$ and $J_{\mathrm{pl}}^{(A)}$ has not been discussed in literature.

### 5.2. Results

The computations for the C(T)-specimen for deformation plasticity show that the configurational force vanishes in almost all regions of the body. Fig. 2 presents the configurational force distribution near the crack tip at a load line displacement $v_{\mathrm{LL}}=0.35 \mathrm{~mm}$. The configurational force is large directly at the crack tip node (we get $-(\hat{\mathbf{e}} \cdot \mathbf{f}^{\text {nl el }}) \Delta A_{\mathrm{e}}=$ $23.6 \mathrm{~kJ} \mathrm{~m}^{-2}$ ). Note that only the component of the configurational force in crack growth direction, $f_{1}=\hat{\mathbf{e}} \cdot \mathbf{f}$, contributes to the plasticity influence term $C_{\mathrm{p}}$ and the crack driving force $J_{\text {tip }}$. The configurational force rapidly decreases to zero at a distance of less than $2 \mathrm{~mm}$. The $J$-integral $J_{\Gamma 2}^{\text {nl el }}$ and the far-field $J$-integral $J_{\text {far }}^{\text {nl el }}$ are evaluated from Eq. (5.1) and plotted in Fig. 3 against the load-line displacement $v_{\mathrm{LL}}$. The two curves coincide which is reasonable, since $\mathbf{f}^{\text {nl el }}$ is negligible outside the path $\Gamma_{2}$. For example, $J_{\Gamma 2}^{\text {nl el }}=J_{\text {far }}^{\text {nl el }}=35 \mathrm{~kJ} \mathrm{~m}^{-2}$ at $v_{\mathrm{LL}}=0.35 \mathrm{~mm}$.

For a homogeneous material in incremental plasticity, the configurational body force arises only due to plastic deformation. The distribution of the equivalent plastic strain in the C(T)-specimen is shown in Fig. 4 for selected values of the load-line displacement, at $v_{\mathrm{LL}}=0.20,0.343$ and $0.352 \mathrm{~mm}$. Plastic deformation occurs for small loads only in the crack tip region. At a load-line displacement of $v_{\mathrm{LL}}=0.20 \mathrm{~mm}$, plastic deformation starts at the back face of the specimen (Fig. 4a). With increasing loading both the crack tip plastic zone and the region of remote plasticity expand (Fig. 4b). Eventually the two regions merge (at $v_{\mathrm{LL}}=0.35 \mathrm{~mm}$ ), resulting in general yielding of the ligament (Fig. 4c).

Fig. 5a shows the distribution of the configurational force $\mathbf{f}^{\text {ep }}$ near the crack tip at a load line displacement of $v_{\mathrm{LL}}=0.35 \mathrm{~mm}$. Directly at the crack tip node we get a high configurational force $-\left(\hat{\mathbf{e}} \cdot \mathbf{f}^{\mathrm{ep}}\right) \Delta A_{\mathrm{e}}=27.9 \mathrm{~kJ} \mathrm{~m}^{-2}$. Again the configurational force decreases with increasing distance from the crack tip, but the decrease is slower than for the non-linear elastic case, Fig. 2. The field of the configurational forces $\mathbf{f}^{\text {ep }}$ at the maximum loading, $v_{\mathrm{LL}}=0.44 \mathrm{~mm}$, is shown in Fig. 5b; note that the large values near the crack tip are not depicted. In general, the configurational body force field reflects the plastic strain distribution and vanishes in regions where there is negligible plastic deformation. Configurational forces appear also at the crack faces and the back face of the specimen due to the jump of the material properties from body to air. Notice that the configurational force at the crack tip node is negative, i.e., it points to the left-hand side (Fig. 5a), whereas the $f_{1}$-component at each node in the remote plastic region is positive,

![](./images/811926939517321217_5.jpg)

Fig. 3. Comparison of different $J$-integral vs. load-line displacement curves: Far-field and near-tip $J$-integrals for non-linear elastic ($J_{\text{far}}^{\text{nl el}}$ and $J_{\Gamma2}^{\text{nl el}}$) and elastic-plastic ($J_{\text{far}}^{\text{ep}}$ and $J_{\Gamma2}^{\text{ep}}$) materials from configurational forces computations, $J$-integral from ABAQUS $J^{\text{VCE}}$ and experimental $J$-integral terms, $J^{(A)}$ and $J_{\text{el}}^{(A)}$.

![](./images/811926939517321217_6.jpg)

Fig. 4. Distribution of the equivalent plastic strain in a C(T) specimen at a load line displacement of (a) $v_{\rm LL}=0.20$ mm, (b) $v_{\rm LL}=0.343$ mm, (c) $v_{\rm LL}=0.352$ mm.

i.e., points to the right hand side. In the crack tip plastic zone, $f_1$-components pointing in either directions will always be found.

Fig. 3 compares the $J_{r2}$ and $J_{\rm far}$ vs. load-line displacement curves for deformation and incremental plasticity. In addition, the curves of the ABAQUS $J$-integral, $J_{\rm far}^{\rm VCE}$, and the experimental $J$-integral terms, $J^{(A)}$ and $J_{\rm el}^{(A)}$, are shown. It is seen that the $J_{\rm far}^{\rm nl\ el}$-, $J_{r2}^{\rm ep}$-, $J_{\rm far}^{\rm VCE}$- and $J^{(A)}$-curves coincide for all $v_{\rm LL}$-values, showing the well-known parabolic dependency on $v_{\rm LL}$. The $J_{\rm far}^{\rm ep}$-curve also coincides for small loading, but only up to $v_{\rm LL}=0.20$ mm where remote plasticity starts at the back face of the specimen. Up to $v_{\rm LL}=0.35$ mm, where general yielding occurs, the $J_{\rm far}^{\rm ep}$-values coincide well with the values of $J_{\rm el}^{(A)}$. For higher $v_{\rm LL}$-values, $J_{\rm el}^{(A)}$ nearly exhibits saturation with only a weak increase probably due to strain hardening, whereas the $J_{\rm far}^{\rm ep}$-values further increase with loading. Other curves in Fig. 3 are discussed in Section 6.3.

![](./images/811926939517321217_7.jpg)

Fig. 5. Distribution of configurational forces $\mathbf{f}^{\text{cp}}$ in an elastic-plastic material: (a) configurational forces near the crack tip at a load line displacement $v_{\text{LL}}=0.35$ mm, (b) configurational forces in the body at a load line displacement $v_{\text{LL}}=0.44$ mm (large force at crack tip is not shown for clarity).

## 6. Discussion

We start with a discussion of the theoretical derivations in this paper. Then the broader implications of the derivations and the numerical C(T)-specimen study will be discussed.

### 6.1. The configurational forces approach in the context of prior literature

The configurational forces approach does not appeal to energy conservation, but instead obtains results by explicitly using the dissipation inequality. Consequently, the configurational force $(-\mathbf{f}_{\Gamma})$ is the vector and the near tip $J$-integral $J_{\text{tip}}$ is the scalar driving force on a crack tip in elastic-plastic materials, even in the context of incremental plasticity. In (homogeneous) hyperelastic materials, $J_{\text{tip}}$ is identical to the total energy released in the specimen per unit crack extension, whereas this is not so in elastic-plastic materials due to the dissipation in the plastic zone which induces the plasticity influence term $C_{\text{p}}$. The plasticity influence term $C_{\text{p}}$ vanishes in the context of deformation plasticity, whereas the crack driving force $J_{\text{tip}}$ vanishes in the case of rigid plasticity.

In the context of infinitesimal strains, expressions similar to Eq. (3.29) have been derived by Lei et al. (2000), Lei (2005) and Nguyen et al. (2005). As summarized in Appendix A, Lei et al. (2000) and Lei (2005) use equilibrium conditions and the divergence theorem to rewrite $J_{\text{tip}}$ as the sum of a far-field integral $J_{\text{far}}$ and a $C_{\text{p}}$-term. Nguyen et al. (2005) integrate the balance of the energy-momentum tensor over the region between $\Gamma_{r}$ and $\Gamma_{\text{far}}$ in Fig. 1; however their results cannot be

used when there is remote plasticity or general yielding conditions since the derivations presume steady-state crack growth. The derivations here present a more consistent approach, since we do not assume a priori that $J_{\text{tip}}$ is valid for elastic-plastic materials, but instead prove that it is indeed the thermodynamic driving force at the crack tip. Moreover, the plasticity influence term $C_{\text{p}}$ is derived without using steady state assumptions and can hence be used to study general yielding conditions.

### 6.2. Dissipation and parameters controlling crack growth

We first consider inhomogeneous non-linear elastic materials, which are conceptually easier to understand. For example, think on a bimaterial C(T)-specimen with a sharp interface where the material properties exhibits a jump, as treated in Simha et al. (2005). Configurational forces appear at the crack tip and along the interface. Since the interface does not move, the total dissipation in the body is equal to the energy dissipated at the crack tip. The first term on the right-hand side in Eq. (2.5) vanishes (note that time derivative $\dot{\phi}$ is taken at fixed reference position), and Eqs. (2.5) and (2.11) provide the total dissipation in the body in terms of the crack tip velocity $\dot{a} \geqslant 0$ as

$$
\Psi(\mathscr{B})=\dot{a} J_{\text{tip}} \geqslant 0 \quad \text{for general quasi-static crack growth.}
\tag{6.1}
$$

When the cracked body is inhomogeneous the near-tip $J$-integral is related to the far-field $J$-integral as

$$
J_{\text{tip}}=J_{\text{far}}+C_{\text{inh}},
\tag{6.2}
$$

where the material inhomogeneity term $C_{\text{inh}}$ accounts for the shielding ($C_{\text{inh}}<0$) or anti-shielding ($C_{\text{inh}}>0$) due to a continuous distribution of inhomogeneities or sharp interfaces (Simha et al., 2005). Inhomogeneities can either shield or enhance the far-field crack driving force, but Eq. (6.1) shows that the total dissipation in pre-cracked elastic bodies will always be determined by $J_{\text{tip}}$. Consequently, for inhomogeneous non-linear elastic materials $J_{\text{tip}}$ is the parameter that controls crack growth, not $J_{\text{far}}$.

For pre-cracked elastic-plastic bodies, the total dissipation in the body due to both plastic deformation and crack growth under quasi-static steady state conditions with tip velocity $\dot{a}>0$ is (3.13)

$$
\Psi(\mathscr{B})=\dot{a} J_{\text{far}} \geqslant 0.
\tag{6.3}
$$

Consequently, the parameter controlling both crack extension and associated plastic deformation under steady state crack growth conditions is the far-field $J$-integral. The total dissipation in a pre-cracked elastic-plastic body due to both plastic deformation and crack growth under non-steady state conditions with tip velocity $\dot{a} \geqslant 0$ is

$$
\Psi(\mathscr{B})=\dot{a} J_{\text{far}}+\dot{v}_{\text{LL}} \int_{\mathscr{B}}\left(\boldsymbol{\sigma} \cdot \frac{\mathrm{d} \boldsymbol{\varepsilon}^{\mathrm{p}}}{\mathrm{d} v_{\text{LL}}}\right) \mathrm{d} A \geqslant 0 ;
\tag{6.4}
$$

it is obtained by ignoring the hardening energy $\phi_{\mathrm{h}}$ in Eq. (3.30) and is appropriate for the C(T) computations in Section 5. The integral in Eq. (6.4) will have contributions at every point in the body $\mathscr{B}$ where the plastic strain changes with increasing load-line displacement $v_{\text{LL}}$. Such changes can be influenced strongly by specimen geometry, like at the back-face of the C(T) specimen.

It is interesting to compare the dissipation for non-steady state crack growth (6.4) with the relations for steady state conditions (3.13) and (6.3). The total dissipation in the body is proportional to $J_{\text{far}}$ for steady state crack growth. This means that the far-field $J$-integral $J_{\text{far}}$ is the thermodynamic driving force for both crack extension and plastic deformation in incremental elastic-plastic materials under steady state conditions. For non-steady state crack growth, the total dissipation in the body is, in general, not proportional to $J_{\text{far}}$. Therefore, $J_{\text{far}}$ can be considered to be the thermodynamic driving force for non-steady state crack extension in incremental elastic-plastic bodies only if $\dot{a} J_{\text{far}}$ is the dominant quantity in Eq. (6.4).

### 6.3. J-integrals in deformation and incremental plasticity

For a homogeneous non-linear elastic material, the configurational body force $\mathbf{f}^{\text{nl el}}$ should vanish identically everywhere in the body; at the crack tip the configurational force $\mathbf{f}_{T}^{\text{nl el}}$ should appear. The computations for the C(T)-specimen show vanishing configurational body forces in almost all regions of the body, apart from the region close to the crack tip where configurational body forces appear due to numerical inaccuracies (Fig. 2). At a load line displacement of $v_{\text{LL}}=0.35$ mm, for example, the configurational force at the crack tip node should yield the condition $-(\hat{\mathbf{e}} \cdot \mathbf{f}^{\text{nl el}}) \Delta A_{\mathrm{e}}=J_{\text{tip}}^{\text{nl el}}=35 \mathrm{~kJ} \mathrm{~m}^{-2}$. We get a distribution of rapidly decreasing configurational forces with a value of $-(\hat{\mathbf{e}} \cdot \mathbf{f}^{\text{nl el}}) \Delta A_{\mathrm{e}}=23.6 \mathrm{~kJ} \mathrm{~m}^{-2}$ directly at the crack tip, but the integration of the configurational forces within the path $\Gamma_{2}$ yields the correct value of the $J$-integral, $J_{\Gamma 2}^{\text{nl el}}=J_{\text{far}}^{\text{nl el}}=35 \mathrm{~kJ} \mathrm{~m}^{-2}$. In fact, $J_{\Gamma 2}^{\text{nl el}}, J_{\text{far}}^{\text{nl el}}$, and the ABAQUS $J$-integral, $J^{\text{CE}}$, are all equal over the entire $v_{\text{LL}}$-range in Fig. 3, so we can conclude that our post-processing procedure yields correct and accurate results.

The situation is more complicated for a homogeneous, elastic-plastic material in incremental plasticity. In the bulk the configurational body force $\mathbf{f}^{\text{ep}}$ arises due to plastic deformation. Whether additionally a finite value of the configurational force $\mathbf{f}_{T}^{\text{ep}}$ arises at the crack tip is per se not known; the decrease of the stresses due to plasticity and the blunting of the

crack tip might reduce this value to zero (Rice, 1979). The computations show at the crack tip node a value of $-(\hat{\mathbf{e}} \cdot \mathbf{f}^{\mathrm{ep}})\Delta A_{\mathrm{e}}=27.9\mathrm{kJ}\,\mathrm{m}^{-2}$, which is similar in size to the value for the non-linear elastic case $(23.6\mathrm{kJ}\,\mathrm{m}^{-2})$ but slightly higher. The integration of the configurational forces within the path $\Gamma_{2}$ yields the same values of the $J$-integral as for a non-linear elastic material, $J_{\Gamma_{2}}^{\mathrm{ep}} \approx J_{\Gamma_{2}}^{\mathrm{nl\,el}}=J_{\mathrm{far}}^{\mathrm{nl\,el}}$. This is so, independently of the load line displacement, up to $v_{\mathrm{LL}}=0.44\mathrm{mm}$, see Fig. 3. However, there is no clear way to separate the contributions of plastic deformation and numerical errors to $\mathbf{f}^{\mathrm{ep}}$ and thereby to calculate a reliable value of the near-tip $J$-integral $J_{\mathrm{tip}}$; see further discussion in the two sections below.

For the following discussion, it is useful to use the physical interpretation of $J_{\mathrm{far}}$ as a global driving force. Analogous to the near-tip $J$-integral $J_{\mathrm{tip}}$, which is commonly called the crack driving force, we interpret the far-field $J$-integral, $J_{\mathrm{far}}$ as a driving force for both crack extension and the corresponding plastic deformation in the body based on the discussion following Eq. (6.4). From the curves in Fig. 3 and the plastic zone shapes in Fig. 4, it can be concluded that the far-field $J$-integral in incremental plasticity is nearly identical to the $J$-integral for non-linear elastic materials as long as plastic deformation is confined to a region around the crack tip and no remote plasticity occurs $(v_{\mathrm{LL}}<0.20\mathrm{mm}$ in Fig. 3),

$$
J_{\mathrm{far}}^{\mathrm{ep}} \approx J_{\mathrm{far}}^{\mathrm{nl\,el}}=J^{(A)} \quad \text{for contained yielding.}
$$

If plasticity occurs at the back face of the specimen $(v_{\mathrm{LL}}>0.20\mathrm{mm}$ in Fig. 3), the far-field $J$-integral in incremental plasticity is smaller than the $J$-integral for non-linear elastic materials,

$$
J_{\mathrm{far}}^{\mathrm{ep}}<J_{\mathrm{far}}^{\mathrm{nl\,el}}=J^{(A)} \quad \text{for uncontained yielding.}
$$

The lower value of the far-field $J$-integral in incremental plasticity can be explained by the fact that the energy dissipated during earlier plastic deformation cannot contribute to the current global driving force. This is consistent with the observation that until the onset of general yielding of the ligament at $v_{\mathrm{LL}}=0.35\mathrm{mm}$ (Fig. 4c), the $J$-integral in incremental plasticity coincides well with the elastic term of the experimental $J$-integral,

$$
J_{\mathrm{far}}^{\mathrm{ep}} \approx J_{\mathrm{el}}^{(A)}<J_{\mathrm{el}}^{\mathrm{nl\,el}}=J_{\mathrm{far}}^{(A)} \quad \text{for contained and uncontained yielding.}
$$

This suggests that the experimental $J$-integral term corresponding to the total plastic work in the specimen, $J_{\mathrm{pl}}^{(A)}$, does not contribute to the global driving force. The above relation (6.7) does not hold, however, above the plastic limit load where the plastic zone extends over the whole unbroken ligament of the specimen $(v_{\mathrm{LL}}=0.35\mathrm{mm}$ in Fig. 3). While $J_{\mathrm{el}}^{(A)}$ nearly exhibits saturation for general yielding conditions with only a weak increase due to strain hardening, $J_{\mathrm{far}}^{\mathrm{ep}}$ increases significantly with further loading,

$$
J_{\mathrm{far}}^{\mathrm{nl\,el}}=J^{(A)}>J_{\mathrm{far}}^{\mathrm{ep}}>J_{\mathrm{el}}^{(A)} \quad \text{for general yielding.}
$$

The global driving force, $J_{\mathrm{far}}^{\mathrm{ep}}$, being higher than the elastic experimental $J$-integral term, $J_{\mathrm{el}}^{(A)}$, is consistent with observations of the crack mouth opening displacement CMOD, which can be viewed as a measure of the global driving force. As long as general yielding does not occur, CMOD is determined mainly by the plastic zone around the crack tip which is entirely surrounded by elastically deformed material. When general yielding occurs, CMOD is additionally increased by the global plastic deformation of the specimen along the plastic hinge which extends towards the back face of the specimen (Fig. 4c); the elastically deformed upper and lower parts of the specimen rotate around this plastic hinge which leads to an increase of CMOD.

### 6.4. $J_{\mathrm{tip}}$ in incremental plasticity

Our theoretical derivation shows that $J_{\mathrm{tip}}$ is the scalar crack driving force ((2.9), (2.10)). However, the derivation does not address whether the limit of the integral in Eq. (2.10) will remain finite, resulting in a non-vanishing $J_{\mathrm{tip}}$. According to Rice (1979), $J_{\mathrm{tip}}$ vanishes even in deformation plasticity in the context of small strain assumptions for elastic-plastic materials that exhibit a saturation in hardening. As the stress singularity at a blunting crack tip vanishes in the context of large deformations and incremental plasticity, it is well known that the limit in Eq. (2.10) vanishes and again $J_{\mathrm{tip}} \to 0$, see e.g. Brocks et al. (2003). The physical and practical implications of this apparent anomaly have not been resolved. Our derivations do not provide any additional insight into this issue.

In computational elastic-plastic fracture mechanics studies $J_{\mathrm{tip}}$ is commonly evaluated on a small contour around the crack tip. Following this, we ignore the limit $r \to 0$ in Eq. $(2.3)_{2}$ and use Eqs. (2.10), $(2.1)_{2}$ and $(2.3)_{2}$ and the divergence theorem to write $J_{\mathrm{tip}}$ as an area integral

$$
\begin{aligned}
J_{\mathrm{tip}} & =-\hat{\mathbf{e}} \cdot \mathbf{f}_{\Gamma} \approx \hat{\mathbf{e}} \cdot \int_{\Gamma_{r}} \mathbf{C} \hat{\mathbf{m}} \mathrm{d} l \\
& \approx \hat{\mathbf{e}} \cdot \int_{\mathscr{B}_{r}} \nabla \cdot \mathbf{C} \mathrm{d} A \approx \sum_{\text{elements in } \mathscr{B}_{r}}-(\hat{\mathbf{e}} \cdot \mathbf{f}) \Delta A_{\mathrm{e}},
\end{aligned}
$$

where $\mathscr{B}_{r}$ is some small region surrounding the crack tip. The region inside the path $\Gamma_{2}$, which is $2\mathrm{mm}$ in front of the crack tip, appears to be a good candidate for $\mathscr{B}_{r}$. Then $J_{\Gamma_{2}}^{\mathrm{ep}}$ can be treated as an approximation for $J_{\mathrm{tip}}^{\mathrm{ep}}$, and the results of our

numerical study on the C(T)-specimen, Fig. 3, suggest that
$$J_{\text{tip}}^{\text{ep}} \approx J_{\Gamma 2}^{\text{ep}} \approx J_{\Gamma 2}^{\text{nl el}} \approx J_{\text{tip}}^{\text{nl el}}.\tag{6.10}$$

Thus it follows that the crack driving force for an elastic-plastic material in incremental plasticity under plane strain conditions approximately equals the crack driving force calculated in deformation plasticity. At the current status of the investigation, this is valid for contained, uncontained and general yielding conditions for a C(T) specimen under large deformation, plane strain conditions. However, further studies are needed to establish the validity of Eq. (6.10) under different in-plane or out-of-plane constraint conditions.

### 6.5. The plasticity influence term, $C_{\mathrm{p}}$

In accordance with the interpretation of $J_{\Gamma 2}^{\text{ep}}$ as an approximation of the near-tip $J$-integral, we follow Eq. (3.8) and introduce an approximate expression to compute the plasticity influence term
$$
\begin{aligned}
C_{\mathrm{p}, \Gamma 2} & =-\left(J_{\mathrm{far}}-J_{\Gamma 2}\right)=\hat{\mathbf{e}} \cdot \int_{\mathscr{B}-\mathscr{B}_{\Gamma 2}} \mathbf{f} \mathrm{d} A \\
& \approx \sum_{\text {elements in } \mathscr{B}-\mathscr{B}_{\Gamma 2}}(\hat{\mathbf{e}} \cdot \mathbf{f}) \Delta A_{\mathrm{e}},
\end{aligned}\tag{6.11}
$$
where $\mathscr{B}_{\Gamma 2}$ denotes the region inside the path $\Gamma_{2}$, a distance of $2 \mathrm{~mm}$ from the crack tip. The parameter $C_{\mathrm{p}, \Gamma 2}$ describes the shielding effect of the plastic deformation in the region $\mathscr{B}-\mathscr{B}_{\Gamma 2}$ of the body; it is a substitute term of the plasticity influence term $C_{\mathrm{p}}$. Then, analogous to Eq. (3.8), we have
$$J_{\mathrm{far}}^{\mathrm{ep}}=J_{\Gamma 2}^{\mathrm{ep}}-C_{\mathrm{p}, \Gamma 2}.\tag{6.12}$$

This computational interpretation of the plasticity influence term is required, since the near-tip $J$-integral $J_{\text{tip}}^{\text{ep}}$ cannot be determined.

In terms of $C_{\mathrm{p}, \Gamma 2}$, shielding due to the plastic deformation occurs when $C_{\mathrm{p}, \Gamma 2}<0$ and anti-shielding when $C_{\mathrm{p}, \Gamma 2}>0$. From the curves in Fig. 3 and the plastic zone shapes in Fig. 4, it is seen that $J_{\mathrm{far}}^{\mathrm{ep}} \approx J_{\Gamma 2}^{\mathrm{ep}}$ for contained yielding and $J_{\mathrm{far}}^{\mathrm{ep}} \leqslant J_{\Gamma 2}^{\mathrm{ep}}$ for uncontained or general yielding conditions. Consequently
$$C_{\mathrm{p}, \Gamma 2} \approx 0 \quad \text { for contained yielding, }\tag{6.13}$$

$$C_{\mathrm{p}, \Gamma 2}>0 \quad \text { for uncontained or general yielding. }\tag{6.14}$$

Thus we have a negligible effect as long as no remote plasticity occurs, whereas for uncontained or general yielding conditions anti-shielding occurs.

Although it might appear surprising at a first glance, the latter effect (6.14), can be easily explained: Remember that only the component of the configurational force in crack growth direction, $f_{1}=\hat{\mathbf{e}} \cdot \mathbf{f}$, influences the plasticity influence term. The $f_{1}$-component is positive in the whole zone of remote plastic yielding near the back face of the specimen, i.e. it points to the right-hand side, which is opposite to its direction at the crack tip node, compare Figs. 5a and b. Therefore, the integration of $f_{1}$ (6.11), yields a positive plasticity influence term, i.e., an anti-shielding effect. Additional reasoning arises from the consideration of the crack driving force in terms of the crack tip opening displacement COD: Back-face plasticity facilitates the bending of the specimen and, thus, increases COD and the crack driving force.

We have shown in Section 3.1 that for steady-state crack growth, $C_{\mathrm{p}}$ should be non-positive and equal to the negative value of the total energy required for plastic deformation per unit crack growth. This is not in conflict with Eq. (6.13), since the initial stages of crack growth in a virgin specimen does not satisfy steady-state conditions. It should be emphasized that all results for our computational example discussed in Sections 6.3-6.5 have been generated for a stationary crack, i.e., they give only the conditions for the first increment of crack growth.

Another point is seen from the picture of the plastic zone, Fig. 4, and the relation of the plasticity influence term (3.29), where for simplicity we neglect the second term in the integrand. Consider a horizontal section through Fig. $4 \mathrm{~b}$ at a certain distance from the crack plane. Within the plastic zone surrounding the crack tip, the components of the plastic strain tensor first increase, reach a maximum value and then decrease as $x_{1}$ (horizontal component) increases. For a non-hardening material, the amount of increase would be equal to the amount of decrease, so there would be no net contribution to the plasticity influence term. For a hardening material, it is plausible that the contribution remains small, and this might be an explanation for the negligible or small $C_{\mathrm{p}, \Gamma 2}$-values under contained yielding conditions (6.13). The situation is different in the remote plastic zone near the back face: there the components of the plastic strain tensor only increase as $x_{1}$ increases and no canceling effect occurs. This explains why remote plasticity near the back face of the specimen leads to a large and positive value of $C_{\mathrm{p}}$. In steady-state crack growth (and contained yielding) the region where the plastic strain tensor increases with $x_{1}$ is far left of the crack tip, i.e. $x_{1} \rightarrow-\infty$ (think of a crack that has moved half way through an infinite specimen). Thus there remains only the regions where the plastic strain tensor decreases. This picture explains why $C_{\mathrm{p}}$ is non-zero and negative for steady-state crack growth. Note that steady-state crack growth only applies if no remote plasticity occurs and the crack tip plastic zone does not change its size or strain intensity.

## 7. Summary

The concept of configurational forces was applied to study pre-existing cracks in elastic-plastic materials. By explicitly considering dissipation due to plastic deformation, we obtain relations between the near-tip and far-field $J$-integrals on the one-hand and the energy dissipated at the crack tip, by plastic deformation in the body and the total dissipation in the body on the other hand. Derivations are first performed for finite strains and results are summarized for small strains. The theoretical results are implemented computationally to study a C(T) specimen in the context of incremental plasticity with $J$-integrals evaluated from the configurational body force. Relations between the incremental plastic near-tip and far-field $J$-integrals, on the one hand, and commonly used experimental or deformational plasticity based $J$-integrals, on the other hand, are obtained. The conclusions of the paper are:

- The near-tip $J$-integral $J_{\text{tip}}$ ((2.10), (3.20)) is the scalar driving force at the crack tip even in incrementally elastic-plastic materials, based on the second law of thermodynamics.
- The configurational body force vanishes in homogeneous elastic bodies, but not in homogeneous elastic-plastic bodies. This makes the $J$-integral path dependent in incrementally plastic materials. The configurational body force ((3.5), (3.27)) depends primarily on the gradient of the plastic strain.
- The plasticity influence term $C_{\text{p}}$ determines the crack tip shielding ($C_{\text{p}} > 0$) or anti-shielding ($C_{\text{p}} < 0$) due to plastic deformation in a cracked body. It is equal to the integral over the cracked body of the component of the configurational body force in the crack-growth direction ((3.7), (3.29)) and depends mainly on the gradient of the plastic strain. The crack driving force $J_{\text{tip}}$ is equal to the sum of the global driving force $J_{\text{far}}$ and the plasticity influence term $C_{\text{p}}$. For self-similar or steady-state crack growth $C_{\text{p}} \leqslant 0$ and equal to the negative of the total energy required for plastic deformation in the body per unit crack extension.
- The total energy dissipated in a cracked elastic body is determined by the crack driving force, $J_{\text{tip}}$, and inhomogeneities result in either shielding or anti-shielding ((6.1), (6.2)). In contrast, the total energy dissipated in a homogeneous cracked elastic-plastic body is determined by $J_{\text{far}}$, not $J_{\text{tip}}$, for steady state crack growth (6.3). Although there are additional contributions from an evolving plastic zone for non-steady crack growth ((3.15), (3.30)), $J_{\text{far}}$ appears to be the most appropriate $J$-integral for characterizing the thermodynamic driving force for both crack growth and plastic deformation.
- The computations for a C(T) specimen with a stationary crack show that the deformational plasticity $J_{\text{far}}$ evaluated by our configurational forces method, the ABAQUS $J$-integral calculated using the virtual crack extension method $J^{\text{VCE}}$ and the experimental $J$-integral $J^{(A)}$ which is determined from the area below the load vs. displacement curve in fracture mechanics experiments are equal for all values of the load-line displacement; moreover, they accurately estimate the incremental plastic global driving force, $J_{\text{far}}^{\text{ep}}$, when yielding is contained, but overestimate under uncontained and general yielding. The elastic part of the experimental $J$-integral, $J_{\text{el}}^{(A)}$, accurately estimates the incremental plastic global driving force for contained and uncontained yielding, but underestimates under general yielding conditions. For the initial stages of crack growth corresponding to contained yielding, the plasticity influence term $C_{\text{p}}$ is negligible, whereas $C_{\text{p}} > 0$ (anti-shielding) for uncontained or general yielding. The stationary crack computations are relevant only for the first increment of crack extension. We are examining the case of a continuously growing crack in ongoing work.

## Acknowledgement

The authors acknowledge gratefully the financial support by the Österreichische Forschungsförderungsgesellschaft mbH, the Province of Styria, the Steirische Wirtschaftsförderungsgesellschaft mbH and the Municipality of Leoben under the frame of the Austrian Kplus Programme (Project number SP18-WP3) and the Comet K2 center in MPPE (Project number A4.11).

## Appendix A. Path-independent integrals

Several treatments can be found in the literature to define path independent integrals not restricted by any specific material behavior like deformation plasticity, eigenstrains or inertial effects, e.g. Maugin (1995). We summarize some approaches in the context of elastic-plastic materials. Kishimoto et al. (1980) were among the first to introduce the path-independent integral $\hat{J}$, which can be written in the notation of Fig. 1 as

$$
\hat{J}=-\int_{\Gamma_{r}}\left(\sigma_{i j} m_{j} u_{i, 1}\right) \mathrm{d} l. \tag{A.1}
$$

Although Kishimoto et al. (1980) use transformations between crack tip coordinates and fixed coordinates, etc., the essence of their calculation to relate $\hat{J}$ to the far-field $J$-integral is as follows. The divergence theorem, equilibrium equation (3.16) and traction free crack faces (3.17) imply that

$$
\int_{\mathscr{R}-\mathscr{R}_{r}} \frac{\partial}{\partial x_{j}}\left(\sigma_{i j} u_{i, 1}\right) \mathrm{d} A=\int_{\partial \Gamma_{\text {far }}}\left(\sigma_{i j} m_{j} u_{i, 1}\right) \mathrm{d} l+\hat{J}, \tag{A.2}
$$

while the divergence theorem gives

$$
\int_{\mathscr{R}-\mathscr{R}_{r}} \frac{\partial \phi_{\mathrm{e}}}{\partial x_{1}} \mathrm{~d} A=\int_{\Gamma_{\mathrm{far}}} \phi_{\mathrm{e}} m_{1} \mathrm{~d} l-\int_{\Gamma_{r}} \phi_{\mathrm{e}} m_{1} \mathrm{~d} l. \tag{A.3}
$$

Subtracting Eq. (A.2) from Eq. (A.3) yields

$$
\int_{\mathscr{R}-\mathscr{R}_{r}}\left[\frac{\partial \phi_{\mathrm{e}}}{\partial x_{1}}-\frac{\partial}{\partial x_{j}}\left(\sigma_{i j} u_{i, 1}\right)\right] \mathrm{d} A=\int_{\Gamma_{\mathrm{far}}}\left(\phi_{\mathrm{e}} m_{1}-\sigma_{i j} m_{j} u_{i, 1}\right) \mathrm{d} l-\int_{\Gamma_{r}} \phi_{\mathrm{e}} m_{1} \mathrm{~d} l-\hat{J}. \tag{A.4}
$$

Using the definition of the Cauchy stress (3.25), the chain rule, the equilibrium equation (2.1), the decomposition of the total strain into elastic and plastic parts (3.18) and the symmetry of the Cauchy stress, we can rewrite the integrand as

$$
\left[\frac{\partial \phi_{\mathrm{e}}}{\partial x_{1}}-\frac{\partial}{\partial x_{j}}\left(\sigma_{i j} u_{i, 1}\right)\right]=\sigma_{i j} \frac{\partial \varepsilon_{i j}^{\mathrm{e}}}{\partial x_{1}}-\sigma_{i j} \frac{\partial \varepsilon_{i j}}{\partial x_{1}}=-\sigma_{i j} \frac{\partial \varepsilon_{i j}^{\mathrm{p}}}{\partial x_{1}}.
$$

Then it follows, by writing the first integral on the right-hand side of Eq. (A.4) as $J_{\text{far}}$,

$$
\hat{J}=J_{\mathrm{far}}-\int_{\Gamma_{r}} \phi_{\mathrm{e}} m_{1} \mathrm{~d} s+\int_{\mathscr{R}-\mathscr{R}_{r}} \sigma_{i j} \frac{\partial \varepsilon_{i j}^{\mathrm{p}}}{\partial x_{1}} \mathrm{~d} A.
$$

In the limit as $r \rightarrow 0$, the elastic energy remains bounded, and we get

$$
\hat{J}=J_{\mathrm{far}}+\int_{\mathscr{R}} \sigma_{i j} \frac{\partial \varepsilon_{i j}^{\mathrm{p}}}{\partial x_{1}} \mathrm{~d} A. \tag{A.5}
$$

The integral in Eq. (A.5) agrees with the plasticity influence term $C_{\mathrm{p}}$ (3.29), when hardening is ignored. However, Kishimoto et al. (1980) do not show that $\hat{J}$ is the thermodynamic driving force at the crack tip.

Miyazaki and Nakagaki (1995) start with the definition

$$
J_{r}=\int_{\partial \mathscr{R}_{r}}\left(\phi_{\mathrm{e}} m_{1}-\sigma_{i j} m_{j} u_{i, 1}\right) \mathrm{d} l
$$

for the crack tip driving force. Since

$$
\int_{\mathscr{R}-\mathscr{R}_{r}}\left[\frac{\partial \phi_{\mathrm{e}}}{\partial x_{1}}-\frac{\partial}{\partial x_{j}}\left(\sigma_{i j} u_{i, 1}\right)\right] \mathrm{d} A=\int_{\Gamma_{\mathrm{far}}}\left(\phi_{\mathrm{e}} m_{1}-\sigma_{i j} m_{j} u_{i, 1}\right) \mathrm{d} l-\int_{\Gamma_{r}}\left(\phi_{\mathrm{e}} m_{1}-\sigma_{i j} m_{j} u_{i, 1}\right) \mathrm{d} l, \tag{A.6}
$$

they obtain

$$
J_{r}=J_{\mathrm{far}}-\int_{\mathscr{R}-\mathscr{R}_{r}}\left[\frac{\partial \phi_{\mathrm{e}}}{\partial x_{1}}-\sigma_{i j} \varepsilon_{i j, 1}\right] \mathrm{d} a. \tag{A.7}
$$

$J_{r}$ can be identified with the $T^{\star}$ integral (Atluri and Nishioka, 1984; Nishioka et al., 1995).

Lei et al. (2000) and Lei (2005) have used this formulation with a stored energy density that depends explicitly on reference coordinates (to model inhomogeneities) as $\phi_{\mathrm{e}}=\phi_{\mathrm{e}}\left(\varepsilon_{i j}^{\mathrm{e}}, x_{1}, x_{2}\right)$ and splitting the strain into elastic and plastic parts (3.18). Then Eq. (A.7) reduces by applying the chain rule to

$$
J_{r}=J_{\mathrm{far}}-\left.\int_{\mathscr{R}-\mathscr{R}_{r}} \frac{\partial \phi_{\mathrm{e}}}{\partial x_{1}}\right|_{\varepsilon_{i j}^{\mathrm{e}}} \mathrm{d} A+\int_{\mathscr{R}-\mathscr{R}_{r}} \sigma_{i j} \varepsilon_{i j, 1}^{\mathrm{p}} \mathrm{d} A. \tag{A.8}
$$

For the homogeneous case, the first integral vanishes. Thus Lei (2005) obtains the first term in Eq. (3.29), but does not account for the hardening contribution.

### References

Anderson, T.L., 1995. Fracture Mechanics. CRC Press, Boca Raton, FL, USA.
ASTM E1820-05, 2005. Standard test method for measurement of fracture toughness. In: Annual Book of ASTM Standards, vol. 03.01. ASTM International, West Conshohocken, PA, USA.
Atluri, S.N., Nishioka, T., 1984. Incremental path-independent integrals in inelastic and dynamic fracture mechanics. Eng. Fract. Mech. 20, 209-244.
Brocks, W., Cornec, A., Scheider, I., 2003. Computational aspects of nonlinear fracture mechanics. In: de Borst, R., Mang, H.A. (Eds.), Comprehensive Structural Integrity, Volume 3: Numerical and Computational Methods. Elsevier, New York, pp. 127-209.
Chen, C.R., Kolednik, O., Scheider, I., Siegmund, T., Tatschl, A., Fischer, F.D., 2003. On the determination of the cohesive zone parameters for the modeling of micro-ductile crack growth in thick specimens. Int. J. Fract. 120, 517-536.
Cleja-Tigoiu, S., Maugin, G.A., 2000. Eshelby's stress tensors in finite elastoplasticity. Acta Mech. 139, 231-249.
Denzer, R., Barth, F.J., Steinmann, P., 2003. Studies in elastic fracture mechanics based on the material force method. Int. J. Numer. Methods Eng. 58, 1817-1835.
Eshelby, J.D., 1970. Energy relations and the energy-momentum tensor in continuum mechanics. In: Kanninen, M., Adler, W., Rosenfield, A., Jaffee, R. (Eds.), Inelastic Behavior of Solids. McGraw-Hill, New York, pp. 77-115.
ESIS P2-92, 1992. ESIS Procedure for Determining the Fracture Behaviour of Materials. European Structural Integrity Society, Delft, The Netherlands.
Freund, L.B., Hutchinson, J.W., 1985. High strain-rate crack growth in rate-dependent plastic solids. J. Mech. Phys. Solids 33, 169-191.
Griffith, A.A., 1921. The phenomena of rupture and flow in solids. Philos. Trans. R. Soc. London A 221, 163-198.
Gurtin, M.E., 1995. The nature of configurational forces. Arch. Rat. Mech. Anal. 131, 67-100.

Gurtin, M.E., 2000. Configurational Forces as Basic Concepts of Continuum Physics. Springer, New York.

Gurtin, M.E., Podio-Guidugli, P., 1996. Configurational forces and the basic laws for crack propagation. J. Mech. Phys. Solids 44, 905-927.

Irwin, G.R., 1957. Analysis of stresses and strains near the end of a crack traversing a plate. ASME J. Appl. Mech. 24, 361-364.

Kienzler, R., Herrmann, G., 2000. Mechanics in Material Space. Springer, Berlin.

Kishimoto, K., Aoki, S., Sakata, M., 1980. On the path independent integral—$\hat{J}$. Eng. Fract. Mech. 13, 841-850.

Kolednik, O., 1991. On the physical meaning of the $J$-$a$-curves. Eng. Fract. Mech. 38, 403-412.

Kolednik, O., 1993. A simple model to explain the geometry dependence of the $J$-$a$-curves. Int. J. Fract. 63, 263-274.

Kolednik, O., Stüwe, H.P., 1985. The stereophotogrammetric determination of the critical crack tip opening displacement. Eng. Fract. Mech. 21, 145-155.

Kolednik, O., Shan, G.X., Fischer, F.D., 1997. The energy dissipation rate—a new tool to interpret geometry and size effects. ASTM STP, vol. 1296, pp. 126-151.

Kolednik, O., Chen, C.R., Shan, G.X., Simha, N.K., Fischer, F.D., 2007. In preparation.

Lubarda, V., 2002. Elastoplasticity Theory. CRC Press, Boca Raton.

Lei, Y., 2005. $J$-integral evaluation for cases involving non-proportional stressing. Eng. Fract. Mech. 72, 577-596.

Lei, Y., O'Dowd, N.P., Webster, G.A., 2000. Fracture mechanics analysis of a crack in a residual stress field. Int. J. Fract. 106, 195-216.

Maugin, G.A., 1993. Material Inhomogeneities in Elasticity. Chapman and Hall, London.

Maugin, G.A., 1994. Eshelby stress in elastoplasticity and ductile fracture. Int. J. Plasticity 10, 393-408.

Maugin, G.A., 1995. Material forces: concepts and applications. ASME J. Appl. Mech. Rev. 48, 213-245.

Maugin, G.A., 1999. The Thermomechanics of Nonlinear Irreversible Behaviors. World Scientific Inc., London.

McMeeking, R.M., 1977. Path dependence of the $J$-integral and the role of $J$ as a parameter characterizing the near tip field. ASTM STP, vol. 631, pp. 28-41.

Miyazaki, N., Nakagaki, M., 1995. Two-dimensional finite element analysis of stably growing cracks in inhomogeneous materials. Int. J. Pres. Ves. Piping 63, 249-260.

Moran, B., Shih, C.F., 1987. Crack tip and associated domain integrals from momentum and energy balance. Eng. Fract. Mech. 27, 615-647.

Mueller, R., Kolling, S., Gross, D., 2002. On configurational forces in the context of the finite element method. Int. J. Numer. Methods Eng. 53, 1557-1574.

Mueller, R., Gross, D., Maugin, G.A., 2004. Use of material forces in adaptive finite element methods. Comp. Mech. 33, 421-434.

Nguyen, T.D., Govindjee, S., Klein, P.A., Gao, H., 2005. A material force method for inelastic fracture mechanics. J. Mech. Phys. Solids 53, 91-121.

Nishioka, T., Kobayashi, Y., Fujimoto, T., Epstein, J.S., 1995. Finite element analysis of near-tip deformation in inhomogeneous elastic-plastic fracture specimens. Int. J. Pres. Ves. Piping 63, 277-291.

Parks, D.M., 1977. The virtual crack extension method for nonlinear material behavior. Comput. Meth. Appl. Mech. Eng. 12, 353-364.

Rice, J.R., 1968a. A path independent integral and the approximate analysis of strain concentration by notches and cracks. ASME J. Appl. Mech. 35, 379-386.

Rice, J.R., 1968b. Mathematical analysis in the mechanics of fracture. In: Liebowitz, H. (Ed.), Fracture—An Advanced Treatise, vol. 2. Academic Press, New York, pp. 191-311.

Rice, J.R., 1976. Elastic-plastic fracture mechanics. In: Erdogan, F. (Ed.), The Mechanics of Fracture, AMD, vol. 19. ASME, New York, pp. 23-53.

Rice, J.R., 1979. The mechanics of quasi-static crack growth. In: Kelly, R.E. (Ed.), Proceedings of the Eighth U.S. National Congress of Applied Mechanics. ASME, New York, pp. 191-216.

Rice, J.R., Paris, P.C., Merkle, J.G., 1973. Some further results of $J$-integral analysis and estimates. ASTM STP, vol. 536, pp. 231-245.

Simha, N.K., Fischer, F.D., Kolednik, O., Chen, C.R., 2003. Inhomogeneity effects on the crack driving force in elastic and elastic-plastic materials. J. Mech. Phys. Solids 51, 209-240.

Simha, N.K., Fischer, F.D., Kolednik, O., Predan, J., Shan, G.X., 2005. Crack tip shielding due to smooth and discontinuous material inhomogeneities. Int. J. Fract. 135, 73-93.

Stampfl, J., Kolednik, O., 2000. The separation of the fracture energy in metallic materials. Int. J. Fract. 101, 321-345.

Turner, C.E., 1990. A re-assessment of the ductile tearing resistance, Part I and II. In: Firrao, D. (Ed.), Fracture Behavior and Design of Materials and Structures, Proceedings of the ECF8, vol. II. EMAS, UK pp. 933-949 and 951-968.

Turner, C.E., Kolednik, O., 1994. A micro and macro approach to the energy dissipation rate model of stable ductile crack growth. Fatigue Fract. Eng. Mater. Struct. 17, 1089-1107.

Wells, A.A., 1963. Application of fracture mechanics at and beyond general yielding. Br. Weld. J. 10, 563-570.