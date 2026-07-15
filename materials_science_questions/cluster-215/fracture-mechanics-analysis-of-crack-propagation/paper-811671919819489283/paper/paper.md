# A Burger Model for the Effective Behavior of a Microcracked Viscoelastic Solid

Sy Tuan Nguyen* and Luc Dormieux

Laboratoire Navier, ENPC, Champs-sur-Marne, France

Yann Le Pape and Julien Sanahuja

Edf, Moret-sur-Loing, France

**ABSTRACT:** This article aims at the determination of the effective behavior of a microcracked linear viscoelastic solid. Due to the nonlinearity of the strain concentration in the cracks, the latter cannot be derived directly from a combination of the correspondence theorem with the Eshelby-based homogenization schemes. The proposed alternative approach is based on the linear relationship between the macroscopic strain and the local displacement discontinuity across the crack. An approximation of the effective behavior in the framework of a Burger model is derived analytically.

**KEY WORDS:** microcracks, micromechanics, viscoelasticity, damage.

## INTRODUCTION

$T$HE RATE-DEPENDENT MECHANICAL behavior of concrete is often approximated by a linear viscoelastic model, the simplest formulation of which is a non-aging one. The practical interest lies in the well-known correspondence principle which transforms a time-dependent boundary value problem into a linear elastic one.

This idea is investigated in this article in order to assess the influence of microcracks on the effective behavior of a non-aging linear viscoelastic (NALV) solid. The determination of the effective behavior in the framework of homogenization amounts to solving a boundary value problem defined

*Author to whom correspondence should be addressed. E-mail: stuan.nguyen@gmail.com

International Journal of DAMAGE MECHANICS, Vol. 20-November 2011

1056-7895/11/08 1116-14 $10.00/0
DOI: 10.1177/1056789510395554
© The Author(s), 2011. Reprints and permissions:
http://www.sagepub.co.uk/journalsPermissions.nav

on a representative elementary volume (REV). As already reported in the literature (e.g. Beurthey and Zaoui, 2000), homogenization of NALV hetero- geneous materials can be expected from a combination of the correspondence principle and the Eshelby-based homogenization schemes for random elastic heterogeneous media. However, this article shows that the nonlinearity of the strain concentration in the cracks prevents a straightforward application of this reasoning. Based on an alternative approach, the contribution of this article is to provide a quantitative assessment of damage in viscoelastic media and to derive a simple damage-dependent Burger model.

Notations: Let us introduce the second-order identity tensor 1, the fourth- order identity tensor $\mathbb{I}$, the fourth-order projectors of the spherical and deviatoric parts, respectively denoted by $\mathbb{J}=1 \otimes 1 / 3$ and $\mathbb{K}=\mathbb{I}-\mathbb{J}$.

The average of the field $a(\mathbf{z})$ in the REV $\Omega$ (resp. in the subset $\Omega^{\alpha} \subset \Omega$ ) is denoted by $\bar{a}$ (resp. $\bar{a}^{\alpha}$):

$$
\bar{a}=\frac{1}{|\Omega|} \int_{\Omega} a(\mathbf{z}) \mathrm{d} V \quad ; \quad \bar{a}^{\alpha}=\frac{1}{\left|\Omega^{\alpha}\right|} \int_{\Omega^{\alpha}} a(\mathbf{z}) \mathrm{d} V
\tag{1}
$$

## 3D NALV BEHAVIOR

A class of 3D isotropic NALV constitutive behaviors is obtained in trans- posing classical unidimensional rheological models to the tensorial context. Burger's model, namely a Maxwell system connected in series with a Kelvin-Voigt one (Figure 1) turns out to model the linear viscoelastic beha- vior of concrete quite well (Le, 2008). In the following, the subscripts $M$ and $K$, respectively, refer to the 'Maxwell' and the 'Kelvin' parts. In order to derive the state equation, the total strain is decomposed into the respective contributions of the Maxwell and Kelvin parts:

$$
\varepsilon=\varepsilon_{M}+\varepsilon_{K}
\tag{2}
$$

Each element of the model (spring or dashpot) is characterized by an iso- tropic fourth-order tensor, related to its elasticity or viscosity:

$$
\begin{aligned}
& \mathbb{C}_{K}^{e}=3 k_{K} \mathbb{J}+2 \mu_{K} \mathbb{K} ; \quad \mathbb{C}_{K}^{v}=\eta_{K}^{s} \mathbb{J}+\eta_{K}^{d} \mathbb{K} ; \\
& \mathbb{C}_{M}^{e}=3 k_{M} \mathbb{J}+2 \mu_{M} \mathbb{K} ; \quad \mathbb{C}_{M}^{v}=\eta_{M}^{s} \mathbb{J}+\eta_{M}^{d} \mathbb{K}
\end{aligned}
\tag{3}
$$

Accordingly, $k_{\alpha}$ and $\mu_{\alpha}(\alpha=K$ or $M)$ denote the bulk and shear moduli, whereas $\eta_{\alpha}^{s}$ and $\eta_{\alpha}^{d}$ represent a bulk and shear viscosity, respectively. The Maxwell strain $\varepsilon_{M}$ is related to the total stress $\sigma$ by:

$$
\dot{\varepsilon}_{M}=\mathbb{S}_{M}^{e}: \dot{\sigma}+\mathbb{S}_{M}^{v}: \sigma
\tag{4}
$$

![](./images/811671919819489283_1.jpg)

Figure 1. Rheological model for concrete.

where $\mathbb{S}_{M}^{e}$ is the tensor of elastic compliance (inverse of $\mathbb{C}_{M}^{e}$) and $\mathbb{S}_{M}^{v}$ the inverse of the viscosity tensor $\mathbb{C}_{M}^{v}$. Similarly, in the state equation of the Kelvin part, the total stress $\sigma$ is related to the Kelvin contribution $\varepsilon_{K}$ to the total strain:
$$
\sigma=\mathbb{C}_{K}^{e}: \varepsilon_{K}+\mathbb{C}_{K}^{v}: \dot{\varepsilon}_{K}
\tag{5}
$$
in which appear the stiffness and viscosity tensors $\mathbb{C}_{K}^{e}$ and $\mathbb{C}_{K}^{v}$. Combining (2), (4), (5), and their time derivatives, a second-order differential equation w.r.t. time is obtained:
$$
\mathbb{X}: \sigma+\mathbb{Y}: \dot{\sigma}+\mathbb{Z}: \ddot{\sigma}=\mathbb{C}_{K}^{e}: \dot{\varepsilon}+\mathbb{C}_{K}^{v}: \ddot{\varepsilon}
\tag{6}
$$
in which:
$$
\mathbb{X}=\mathbb{C}_{K}^{e}: \mathbb{S}_{M}^{v} ; \quad \mathbb{Y}=\mathbb{I}+\mathbb{C}_{K}^{e}: \mathbb{S}_{M}^{e}+\mathbb{C}_{K}^{v}: \mathbb{S}_{M}^{v} ; \quad \mathbb{Z}=\mathbb{C}_{K}^{v}: \mathbb{S}_{M}^{e}
\tag{7}
$$

According to (7), it is readily seen that:
$$
\begin{aligned}
& \mathbb{X}=\frac{3 k_{K}}{\eta_{M}^{s}} \mathbb{J}+\frac{2 \mu_{K}}{\eta_{M}^{d}} \mathbb{K} ; \quad \mathbb{Y}=\left(1+\frac{k_{K}}{k_{M}}+\frac{\eta_{K}^{s}}{\eta_{M}^{s}}\right) \mathbb{J}+\left(1+\frac{\mu_{K}}{\mu_{M}}+\frac{\eta_{K}^{d}}{\eta_{M}^{d}}\right) \mathbb{K} ; \\
& \mathbb{Z}=\frac{\eta_{K}^{s}}{3 k_{M}} \mathbb{J}+\frac{\eta_{K}^{d}}{2 \mu_{M}} \mathbb{K}
\end{aligned}
\tag{8}
$$

The implementation of the correspondence theorem is based on the Laplace-Carson transform:
$$
a^{*}(p)=\int_{-\infty}^{+\infty} a^{\prime}(t) e^{-p t} \mathrm{~d} t=p \int_{-\infty}^{+\infty} a(t) e^{-p t} \mathrm{~d} t
\tag{9}
$$

When applied to (6), the Laplace-Carson transform yields the state equation of the solid in the form $\sigma^{*}=\mathbb{C}^{*}(p): \varepsilon^{*}$ with:
$$
\mathbb{C}^{*}(p)=\left(\mathbb{X}+p \mathbb{Y}+p^{2} \mathbb{Z}\right)^{-1}:\left(p \mathbb{C}_{K}^{e}+p^{2} \mathbb{C}_{K}^{v}\right)
\tag{10}
$$

Owing to (3) and (8), $\mathbb{C}^{*}(p)$ appears as an isotropic tensor which can be put in the form $3 k^{*} \mathbb{J}+2 \mu^{*} \mathbb{K}$ with
$$
\frac{1}{k^{*}(p)}=\frac{1}{k_{M}}+\frac{3}{p \eta_{M}^{s}}+\frac{1}{k_{K}+p \eta_{K}^{s} / 3}
\tag{11}
$$

and

$$
\frac{1}{\mu^{*}(p)}=\frac{1}{\mu_{M}}+\frac{2}{p \eta_{M}^{d}}+\frac{1}{\mu_{K}+p \eta_{K}^{d} / 2} \tag{12}
$$

Note that a Poisson coefficient $v^{*}(p)$ can be defined as usual:

$$
v^{*}=\frac{3 k^{*}-2 \mu^{*}}{2\left(3 k^{*}+\mu^{*}\right)} \tag{13}
$$

The correspondence principle summarized by $\sigma^{*}=\mathbb{C}^{*}(p): \varepsilon^{*}$ is the basis of the approach developed in this article. However, it is recalled that the effective behavior of linear viscoelastic composites can alternatively deter- mined in an approximate way by a time-integration scheme (Lahellec and Suquet, 2007).

# HOMOGENIZATION OF VISCOELASTIC MICROCRACKED SOLID

Let us now investigate the damage induced by microcracks in a NALV material of the type described in section '3D NALV Behavior'. The most natural way to address this question consists in taking advantage of the results concerning the effective behavior of microcracked linear elastic mate- rials (e.g. Budiansky and O'Connell, 1976; Horii and Nemat-Nasser, 1983; Dormieux et al., 2006) and to apply the correspondence principle. However, some precaution has to be taken in the transposition of mathematical results from elasticity to viscoelasticity.

## A Review of the Linear Elastic Case

More precisely, it is well known that the usual homogenization schemes in heterogeneous elasticity, such as the dilute scheme or the Mori-Tanaka scheme, are based on the concept of strain localization which, in turn, takes root in the linearity of the homogenization problem. In short, given a REV $\Omega$ and some macroscopic strain $\mathbf{E}$, linear displacement boundary conditions are prescribed on the boundary of $\Omega$:

$$
(\forall \mathbf{z} \in \partial \Omega): \quad \boldsymbol{\xi}(\mathbf{z})=\mathbf{E} \cdot \mathbf{z} \tag{14}
$$

If the response is linear, the local strain $\varepsilon(\mathbf{z})$ is linearly related to $\mathbf{E}$ by a fourth-order so-called 'strain localization' tensor:

$$
\varepsilon(\mathbf{z})=\mathbb{A}(\mathbf{z}): \mathbf{E} \tag{15}
$$

The effective stiffness tensor $\mathbb{C}^{hom}$ of the composite is then shown to be the average $\overline{\mathbb{C}(\mathbf{z}):\mathbb{A}(\mathbf{z})}$, where $\mathbb{C}(\mathbf{z})$ denotes the local stiffness tensor. In the case of a porous medium with a homogeneous solid phase of stiffness tensor $\mathbb{C}^s$, one obtains (e.g. Dormieux et al., 2006):

$$
\mathbb{C}^{hom} = \mathbb{C}^s : (\mathbb{I} - \varphi\overline{\mathbb{A}}^p) \tag{16}
$$

where $\overline{\mathbb{A}}^p$ is the average of $\mathbb{A}(\mathbf{z})$ over the pore space $\Omega^p$ and $\varphi$ the porosity. Classical estimates of $\overline{\mathbb{A}}^p$ are derived from the solution of the Eshelby inhomogeneity problem. The latter considers a single ellipsoidal inhomogeneity $I$ embedded in an infinite homogeneous medium made up of an elastic material. Given some macroscopic strain $\mathbf{E}$, linear displacement boundary conditions of the form:

$$
|\mathbf{z}| \to \infty : \quad \boldsymbol{\xi}(\mathbf{z}) \to \mathbf{E} \cdot \mathbf{z} \tag{17}
$$

are adopted at infinity. Then, the strain $\boldsymbol{\varepsilon}^I$ in the inhomogeneity proves to be uniform. For instance, in the case of a cavity embedded in an infinite solid medium with stiffness tensor $\mathbb{C}^s$, $\boldsymbol{\varepsilon}^I$ is given by:

$$
\boldsymbol{\varepsilon}^I = (\mathbb{I} - \mathbb{S})^{-1} : \mathbf{E} \tag{18}
$$

where $\mathbb{S}$ is the Eshelby (1957) tensor of the cavity which depends on the geometry of the cavity and on the bulk elasticity tensor $\mathbb{C}^s$. Hence, recalling (15), the dilute scheme simply amounts to taking $\overline{\mathbb{A}}_{dil}^p = (\mathbb{I} - \mathbb{S})^{-1}$ as an estimate for $\overline{\mathbb{A}}^p$. The Mori–Tanaka scheme can be viewed as a refined analysis aiming at capturing mechanical interaction between elementary pores (resp. cracks). The corresponding estimate comprises a correcting term w.r.t. the dilute one and reads $\overline{\mathbb{A}}_{MT}^p = (\mathbb{I} - \mathbb{S})^{-1} : ((1 - \varphi)\mathbb{I} + \varphi(\mathbb{I} - \mathbb{S})^{-1})^{-1}$.

The usual 3D crack model is a flat spheroid characterized by its aspect ratio $\omega \ll 1$. In this case, the Eshelby tensor $\mathbb{S}$ is a function of $\omega$. Let the subscript $n$ be associated with the direction of the normal to the crack. The mathematical problem encountered specifically in the case of cracks lies in the fact that the coefficients $nn\alpha\beta$ (as well as $n\alpha n\alpha$) of the tensor $(\mathbb{I} - \mathbb{S})^{-1}$ are of the order of $1/\omega$. This implies that the ratio of normal strain $\varepsilon_{nn}$ to the macroscopic strain $\mathbf{E}$ is of the order of $1/\omega$. This in turn induces nonnegligible variations of the aspect ratio $\omega$ and is in contradiction with the assumption of linearity on which the concept of strain concentration tensor is based. This question has been discussed into details in Deudé et al. (2002).

In order to overcome this difficulty, the idea consists in considering the rate-type formulation of the problem. In other words, the strain concentration tensor should be replaced by a strain *rate* concentration tensor so that (15) becomes

$$
\dot{\boldsymbol{\varepsilon}}(\mathbf{z}) = \mathbb{A}(\mathbf{z}) : \dot{\mathbf{E}} \tag{19}
$$

Similarly, the rate-type formulation of the Eshelby problem for a spheroidal cavity now yields:

$$
\dot{\varepsilon}^{I}=(\mathbb{I}-\mathbb{S}(\omega))^{-1}: \dot{\mathbf{E}}
\tag{20}
$$

in which $\omega$ now refers to the aspect ratio in the current configuration of the spheroidal cavity. Eventually, the use of $\overline{\mathbb{A}}_{d i l}^{p}$ or $\overline{\mathbb{A}}_{M T}^{p}$ in (16) leads to an estimate of the tangent effective stiffness. For mathematical reasons related to the fact that the crack porosity $\varphi$ is proportional to $\omega$ (e.g. Deudé et al., 2002), it turns out that this tangent effective stiffness is in fact independent of $\omega$. This renders the effective behavior linear elastic. However, from a rigorous point of view, the rate-type reasoning is indispensable in order to avoid the troubles associated with large strain in the direction of the normal to the cracks.

## The Viscoelastic Case

The standard extension to NAL viscoelasticity of the homogenization schemes in linear elasticity is based on the Laplace-Carson transform. It amounts to replacing the elastic homogenization rule $\mathbb{C}^{h o m}=\overline{\mathbb{C}: \mathbb{A}}$ by

$$
\mathbb{C}^{\text {hom* }}=\overline{\mathbb{C}^{*}: \mathbb{A}_{v}}
\tag{21}
$$

In (21), the strain concentration tensor $\mathbb{A}_{v}$ has now to be estimated for a fictitious REV having the same geometry as the real one and elastic properties characterized by the elastic stiffness $\mathbb{C}^{*}$. Clearly enough, since the Laplace-Carson transform is a linear operator, it can only be applied to a linear set of equations. Now, in the case of microcracks, the previous section has emphasized the existence of a nonlinearity at the local scale in the relationship between the crack strain and the macroscopic strain. This implies that the homogenization of a viscoelastic cracked medium is not as straightforward as (21) could be since it cannot be based on the strain concentration concept. The purpose of this section is to present an alternative approach.

We therefore consider a REV $\Omega$ made up the NALV solid described at section '3D NALV Behavior' and of a network of plane penny-shaped cracks. As opposed to the 3D ellipsoidal crack model considered in the Eshelby-type approach, the mathematical penny-shaped crack is a 2D concept in nature. In particular, it does not refer to an aspect ratio. During the time period of loading, the displacement $\xi(\mathbf{z}, t)$ is prescribed on the boundary $\partial \Omega$. The latter is related to the history of the macroscopic strain $\mathbf{E}(t)$ by $\xi(\mathbf{z}, t)=\mathbf{E}(t) \cdot \mathbf{z}$. Accordingly, the macroscopic strain is related to the

microscopic strain field in the solid $\Omega^{s}$ by an average rule which has to be
corrected by a term accounting for the strain in the cracks:

$$
\mathbf{E}=\frac{1}{|\Omega|}\left(\int_{\Omega^{s}} \boldsymbol{\varepsilon} \mathrm{d} V+\sum_{i} \int_{C_{i}}[\xi]_{i} \stackrel{s}{\otimes} \mathbf{n}_{i} \mathrm{~d} S\right)
\tag{22}
$$

where $C_{i}$ denotes crack $\mathrm{n}^{\mathrm{o}} i, \mathbf{n}_{i}$ the unit normal to the crack plane and $[\xi]_{i}$ the
displacement discontinuity between the two lips of the crack defined accord-
ing to the orientation of $\mathbf{n}_{i}$.

Let $\boldsymbol{\Sigma}(t)$ and $\boldsymbol{\sigma}(\mathbf{z}, t)$ respectively, denote the macroscopic stress tensor and
the microscopic stress field, which are related by the average rule: $\boldsymbol{\Sigma}=\overline{\boldsymbol{\sigma}}$.
In the case of empty cracks, it takes the form:

$$
\boldsymbol{\Sigma}=\frac{1}{|\Omega|} \int_{\Omega^{s}} \boldsymbol{\sigma} \mathrm{d} V
\tag{23}
$$

The idea consists in anticipating that both the microscopic strain field in the
solid and the displacement discontinuity vectors $[\xi]_{i}$ linearly depend on the
macroscopic strain, which will have to be confirmed a posteriori. Thus, it is
justified to apply Laplace–Carson transform to (22), which yields:

$$
\mathbf{E}^{*}=\frac{1}{|\Omega|} \int_{\Omega^{s}} \boldsymbol{\varepsilon}^{*} \mathrm{~d} V+\frac{1}{|\Omega|}\left(\sum_{i} \int_{C_{i}}[\xi]_{i}^{*} \stackrel{s}{\otimes} \mathbf{n}_{i} \mathrm{~d} S\right)
\tag{24}
$$

We now seek the relationship between the macroscopic strain $\mathbf{E}^{*}$ and stress
$\boldsymbol{\Sigma}^{*}$. To begin with, combining the stress average rule (23) with the state
equation of the solid in the form $\boldsymbol{\sigma}^{*}=\mathbb{C}^{*}(p): \varepsilon^{*}$, the strain average rule
(24) now reads:

$$
\mathbf{E}^{*}=\mathbb{C}^{*}(p)^{-1}: \boldsymbol{\Sigma}^{*}+\frac{1}{|\Omega|}\left(\sum_{i} \int_{C_{i}}[\xi]_{i}^{*} \stackrel{s}{\otimes} \mathbf{n}_{i} \mathrm{~d} S\right)
\tag{25}
$$

We now look for an estimate of $[\xi]_{i}^{*}$ as a function of $\boldsymbol{\Sigma}^{*}$. To do so, we resort
to the so-called stress-based dilute scheme (Dormieux and Kondo, 2009).
Accordingly, a single penny-shaped crack in an infinite elastic medium of
stiffness $\mathbb{C}^{*}(p)$ with a remote stress state $\boldsymbol{\Sigma}^{*}$ is considered. The displacement
discontinuity $[\xi]_{i}^{*}$ is then estimated by the solution of this classical problem
of linear elastic fracture mechanics.

More precisely, consider the cylindrical coordinates system defined w.r.t.
the axis of symmetry of the crack. The radius of the penny-shaped crack is
denoted by $a$ and $\rho$ is the distance to the axis of symmetry. If the remote
stress is isotropic, say $\boldsymbol{\Sigma}^{*}=\Sigma^{*} \mathbf{1}$, the discontinuity is normal to the crack
plane (mode I) and reads:

$$
\left[\xi_{n}\right]^{*}=\frac{4\left(1-v^{*}\right)}{\pi} \frac{\Sigma^{*}}{\mu^{*}} \sqrt{a^{2}-\rho^{2}}
\tag{26}
$$

In turn, with shear stresses at infinity, say $\boldsymbol{\Sigma}^{*}=\boldsymbol{\Sigma}^{*} \mathbf{n} \stackrel{s}{\otimes} \mathbf{t}$, with $\mathbf{t}$ parallel to the crack plane, the discontinuity is in the crack plane (mode II) and reads:

$$
\left[\xi_{t}\right]^{*}=\frac{8}{\pi} \frac{\Sigma^{*}}{\mu^{*}} \frac{1-\nu^{*}}{2-\nu^{*}} \sqrt{a^{2}-\rho^{2}}
\tag{27}
$$

(26) or (27) linearly relate the elementary displacement discontinuity and the macroscopic stress. In turn, the use of the latter in (25) clearly yields a linear relationship between $\boldsymbol{\Sigma}^{*}$ and $\mathbf{E}^{*}$, which can be put in the form $\boldsymbol{\Sigma}^{*}=\mathbb{C}^{h o m^{*}}(p): \mathbf{E}^{*}$. This equation characterizes the effective behavior, up to an inverse Laplace-Carson transform.

Combined with (27) and (26), it also a posteriori confirms the assumption of a linear relationship between the local displacement discontinuity and the macroscopic strain.

For further investigation, it is necessary to specify the distribution of crack orientations. In the sequel, the method is illustrated for the case of an isotropic distribution of crack orientations.

## Isotropic Distribution of Crack Orientations

In this section, an isotropic distribution of crack orientations is considered. This implies that $\mathbb{C}^{h o m^{*}}(p)$ is an isotropic tensor which is sought in the form:

$$
\mathbb{C}^{h o m^{*}}(p)=3 k^{h o m^{*}}(p) \mathbb{I}+2 \mu^{h o m^{*}}(p) \mathbb{K}
\tag{28}
$$

In order to determine $k^{h o m^{*}}(p)$ and $\mu^{h o m^{*}}(p)$, we successively consider an isotropic and a deviatoric loading.

## Effective Behavior under Isotropic Loading

Under an isotropic loading in which the macroscopic stress reads $\Sigma^{*} \mathbf{1}$, the elementary contribution of a crack to the macroscopic strain in (25) is derived from (26):

$$
\int_{C}[\boldsymbol{\xi}]^{*} \stackrel{s}{\otimes} \mathbf{n} \mathrm{d} S=\frac{8 a^{3}}{3} \frac{\Sigma^{*}\left(1-\nu^{*}\right)}{\mu^{*}} \mathbf{n} \otimes \mathbf{n}
\tag{29}
$$

Assuming that all cracks have the same radius $a$, an integration over all orientations on the unit sphere yields the total crack contribution:

$$
\frac{1}{|\Omega|}\left(\sum_{i} \int_{C_{i}}[\boldsymbol{\xi}]_{i}^{*} \stackrel{s}{\otimes} \mathbf{n}_{i} \mathrm{~d} S\right)=\frac{8 N a^{3}}{3} \frac{\Sigma^{*}\left(1-\nu^{*}\right)}{\mu^{*}} \int_{|\mathbf{n}|=1} \mathbf{n} \otimes \mathbf{n} \frac{\mathrm{d} S}{4 \pi}=\frac{8 N a^{3}}{9} \frac{\Sigma^{*}\left(1-\nu^{*}\right)}{\mu^{*}} \mathbf{1}
\tag{30}
$$

in which $N$ denotes the number of cracks per unit volume. Introducing (30) into (25) leads to the homogenized state equation under isotropic loading:

$$
\Sigma^{*}(p)=k^{h o m *}(p) \operatorname{tr} \mathbf{E}^{*}(p) \quad \text { with } \quad k^{h o m *}=\frac{k^{*}}{1+\epsilon Q^{*}} ; Q^{*}=\frac{16}{9} \frac{1-v^{* 2}}{1-2 v^{*}} \quad(31)
$$

where $\epsilon=N a^{3}$, often referred to as crack density parameter (Budiansky and O'Connel, 1976), appears to characterize the damage level.

For practical implementation, it is appealing to seek an effective Burger model for the cracked medium, i.e. to seek the appropriate set of parameters $k_{M}(\epsilon), k_{K}(\epsilon), \eta_{M}^{s}(\epsilon)$, and $\eta_{K}^{s}(\epsilon)$. Recalling (11), the latter should meet the following condition:

$$
\frac{1}{k^{h o m *}(p)}=\frac{1}{k_{M}(\epsilon)}+\frac{3}{p \eta_{M}^{s}(\epsilon)}+\frac{1}{k_{K}(\epsilon)+p \eta_{K}^{s}(\epsilon) / 3}
$$

Recalling the expression (31) of $k^{h o m *}(p)$ and that of $v^{*}(p)$ (Equation (13)), it is readily seen that (32) cannot be satisfied rigorously. Our purpose is rather to identify the best approximation of the effective behavior in the class of Burger models. The idea is to satisfy the series expansion of (32) to the first order at $p=0$ and $p=\infty$. Recalling that

$$
\lim _{t \rightarrow \infty} a(t)=\lim _{p \rightarrow 0} a^{*}(p) \quad ; \quad \lim _{t \rightarrow 0} a(t)=\lim _{p \rightarrow \infty} a^{*}(p)
$$

the sought Burger model is expected to be an excellent approximation in the short and long terms. For forthcoming reference, we note the series expansion of $Q^{*}$ in the vicinity of $p=0$:

$$
Q^{*}=Q_{o}^{o}+Q_{1}^{o} p+O\left(p^{2}\right)
$$

with

$$
Q_{o}^{o}=\frac{16}{9} \frac{\eta_{M}^{s}\left(\eta_{M}^{s}+2 \eta_{M}^{d}\right)}{\eta_{M}^{d}\left(2 \eta_{M}^{s}+\eta_{M}^{d}\right)}
$$

and

$$
Q_{1}^{o}=\frac{16}{27} \eta_{M}^{s} \frac{\eta_{M}^{s}{ }^{2}+\eta_{M}^{d} \eta_{M}^{s}+\eta_{M}^{d}{ }^{2}}{\left(2 \eta_{M}^{s}+\eta_{M}^{d}\right)^{2}}\left(3\left(\frac{1}{\mu_{M}}+\frac{1}{\mu_{K}}\right)-2 \frac{\eta_{M}^{s}}{\eta_{M}^{d}}\left(\frac{1}{k_{M}}+\frac{1}{k_{K}}\right)\right) \quad(36)
$$

whereas, in the vicinity of $p=\infty$, we have:

$$
Q^{*}=Q_{o}^{\infty}+\frac{Q_{-1}^{\infty}}{p}+O\left(\frac{1}{p^{2}}\right)
$$

with
$$
Q_{o}^{\infty}=\frac{4}{3} \frac{k_{M}\left(3 k_{M}+4 \mu_{M}\right)}{\mu_{M}\left(3 k_{M}+\mu_{M}\right)} \tag{38}
$$
and
$$
Q_{-1}^{\infty}=-\frac{4}{3} k_{M} \frac{9 k_{M}^{2}+6 \mu_{M} k_{M}+4 \mu_{M}^{2}}{\left(3 k_{M}+\mu_{M}\right)^{2}}\left(3 \frac{k_{M}}{\mu_{M}}\left(\frac{1}{\eta_{M}^{s}}+\frac{1}{\eta_{K}^{s}}\right)-2\left(\frac{1}{\eta_{M}^{d}}+\frac{1}{\eta_{K}^{d}}\right)\right) \tag{39}
$$

Combining (11) and (31) together with (34) and (37), the series expansions of the bulk 'compliance' in the vicinity of $p=0$ and $p=\infty$, respectively, read:
$$
p=0: \quad \frac{1}{k^{h o m^{*}}}=3 \frac{1+\epsilon Q_{o}^{o}}{\eta_{M}^{s}} \frac{1}{p}+3 \frac{\epsilon Q_{1}^{o}}{\eta_{M}^{s}}+\left(1+\epsilon Q_{o}^{o}\right)\left(\frac{1}{k_{M}}+\frac{1}{k_{K}}\right)+O(p) \quad(40)
$$
and
$$
p=\infty: \quad \frac{1}{k^{h o m^{*}}}=\frac{1+\epsilon Q_{o}^{\infty}}{k_{M}}+\frac{1}{p}\left(3\left(1+\epsilon Q_{o}^{\infty}\right)\left(\frac{1}{\eta_{M}^{s}}+\frac{1}{\eta_{K}^{s}}\right)+\frac{\epsilon Q_{-1}^{\infty}}{k_{M}}\right)+O\left(1 / p^{2}\right) \tag{41}
$$

In turn, alternative series expansions of $1 / \mathrm{k}^{hom*}$ are derived from the Burger model approximation (Equation (32)):
$$
p=0: \quad \frac{1}{k^{h o m^{*}}}=\frac{3}{\eta_{M}^{s}(\epsilon)} \frac{1}{p}+\frac{1}{k_{M}(\epsilon)}+\frac{1}{k_{K}(\epsilon)}+O(p) \tag{42}
$$
and
$$
p=\infty: \quad \frac{1}{k^{h o m^{*}}}=\frac{1}{k_{M}(\epsilon)}+\frac{3}{p}\left(\frac{1}{\eta_{M}^{s}(\epsilon)}+\frac{1}{\eta_{K}^{s}(\epsilon)}\right)+O\left(1 / p^{2}\right) \tag{43}
$$

The damaged stiffness and viscosity parameters, that is $k_{M}(\epsilon), k_{K}(\epsilon), \eta_{M}^{s}(\epsilon)$ and $\eta_{K}^{s}(\epsilon)$, must ensure the compatibility between (40) and (42), as well as between (41) and (43). This yields:
$$
\begin{aligned}
& \frac{1}{k_{M}(\epsilon)}=\frac{1+\kappa_{M} \epsilon}{k_{M}} \quad ; \quad \frac{1}{k_{K}(\epsilon)}=\frac{1+\kappa_{K} \epsilon}{k_{K}} \\
& \frac{1}{\eta_{M}^{s}(\epsilon)}=\frac{1+v_{M}^{s} \epsilon}{\eta_{M}^{s}} \quad ; \quad \frac{1}{\eta_{K}^{s}(\epsilon)}=\frac{1+v_{K}^{s} \epsilon}{\eta_{K}^{s}}
\end{aligned} \tag{44}
$$
where a set of constants $\kappa_{M}, \kappa_{K}, v_{M}^{s}$, and $v_{K}^{s}$ are determined from the following system (Figure 2):
$$
\begin{gathered}
\kappa_{M}=Q_{o}^{\infty} \quad ; \quad v_{M}^{s}=Q_{o}^{o} \\
\frac{\kappa_{M}-Q_{o}^{o}}{k_{M}}+\frac{\kappa_{K}-Q_{o}^{o}}{k_{K}}=3 \frac{Q_{1}^{o}}{\eta_{M}^{s}} \quad ; \quad \frac{v_{M}^{s}-Q_{o}^{\infty}}{\eta_{M}^{s}}+\frac{v_{K}^{s}-Q_{o}^{\infty}}{\eta_{K}^{s}}=\frac{Q_{-1}^{\infty}}{3 k_{M}}
\end{gathered} \tag{45}
$$

![](./images/811671919819489283_2.jpg)
![](./images/811671919819489283_3.jpg)

Figure 2. Approximation of the effective behavior of a microcracked medium by a Burger model (numerical data for concrete; Le, 2008): $k_M$=24.42 GPa, $\mu_M$=13.27 GPa, $k_K$=39.27 GPa, $\mu_K$=14.07 GPa, $\eta_M^s=22\,10^8$ GPa.s, $\eta_M^d=7.75\,10^8$ GPa.s , $\eta_K^s=1.52\,10^8$ GPa.s, and $\eta_K^d=0.254\,10^8$ GPa.s. Each curve represents one of the eight constants of the Burger model of the damaged material, normalized by the corresponding constant of the undamaged material.

## Effective Behavior under Deviatoric Loading
Given a Cartesian orthonormal frame $(\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3)$, consider for example a deviatoric loading in which the macroscopic stress reads:

$$
\boldsymbol{\Sigma}^* = \Sigma^*(\mathbf{e}_1 \otimes \mathbf{e}_1 - \mathbf{e}_3 \otimes \mathbf{e}_3)
\tag{46}
$$

The elementary contribution of an elementary crack to the macroscopic strain in (25) is derived from (27) and (26), according to its orientation. Let $\mathbf{n}$ coincide with the radial unit vector $\mathbf{e}_r$ (spherical coordinates $\theta$ and $\phi$) :

$$
[\boldsymbol{\xi}]^* = \frac{4\Sigma^*(1 - \nu^*)}{\pi\mu^*}\left(X_r\mathbf{e}_r + \frac{2}{2 - \nu^*}(X_\theta\mathbf{e}_\theta + X_\phi\mathbf{e}_\phi)\right)\sqrt{a^2 - \rho^2}
\tag{47}
$$

with

$$
\begin{aligned}
X_r=\cos^2\phi\sin^2\theta-\cos^2\theta; X_\theta=\sin\theta\cos\theta(1+\cos^2\phi); X_\phi=-\sin\theta\sin\phi\cos\phi
\end{aligned}
\tag{48}
$$

Integration over all crack orientations on the unit sphere yields:

$$
\frac{1}{|\Omega|}\left(\sum_{i}\int_{C_i} [\boldsymbol{\xi}]_i^*\stackrel{s}{\otimes}\mathbf{n}_i\,\mathrm{d}S\right)=\frac{\epsilon M^*}{2\mu^*}\boldsymbol{\Sigma}^*(p) \quad \text{with} \quad M^*=\frac{32}{45}\frac{(1 - \nu^*)(5 - \nu^*)}{2 - \nu^*}
\tag{49}
$$

Introducing (49) into (25) leads to the homogenized state equation under deviatoric loading:

$$
\boldsymbol{\Sigma}^{*}(p)=2 \mu^{h o m^{*}}(p) \mathbf{E}^{*}(p) \quad \text { with } \quad \mu^{h o m^{*}}=\frac{\mu^{*}}{1+\epsilon M^{*}} \tag{50}
$$

As done previously for an isotropic loading, we seek an effective Burger model for the cracked medium under shear. The latter is characterized by the appropriate set of parameters $\mu_{M}(\epsilon), \mu_{K}(\epsilon), \eta_{M}^{d}(\epsilon)$ and $\eta_{K}^{d}(\epsilon)$ defined by the following condition (Equation (12)):

$$
\frac{1}{\mu^{h o m^{*}}(p)}=\frac{1}{\mu_{M}(\epsilon)}+\frac{2}{p \eta_{M}^{d}(\epsilon)}+\frac{1}{\mu_{K}(\epsilon)+p \eta_{K}^{d}(\epsilon) / 2} \tag{51}
$$

This equation is to be satisfied in the vicinity of $p=0$ and $p=\infty$. The series expansion of $M^{*}$ in the vicinity of $p=0$ reads:

$$
\begin{aligned}
p=0: M^{*}=M_{o}^{o}+M_{1}^{o} p+O\left(p^{2}\right) ; \quad p=\infty: M^{*}=M_{o}^{\infty}+\frac{M_{-1}^{\infty}}{p}+O\left(1 / p^{2}\right)
\tag{52}
\end{aligned}
$$

with

$$
M_{o}^{o}=\frac{32}{45} \frac{\left(\eta_{M}^{s}+2 \eta_{M}^{s}\right)\left(3 \eta_{M}^{s}+2 \eta_{M}^{d}\right)}{\left(\eta_{M}^{s}+\eta_{M}^{d}\right)\left(2 \eta_{M}^{s}+\eta_{M}^{d}\right)} \tag{53}
$$

$$
M_{1}^{o}=\frac{32}{45} \frac{\eta_{M}^{s} \eta_{M}^{d}\left(7 \eta_{M}^{s}{ }^{2}+10 \eta_{M}^{s} \eta_{M}^{d}+4 \eta_{M}^{d}{ }^{2}\right)}{\left(\eta_{M}^{s}+\eta_{M}^{d}\right)^{2}\left(2 \eta_{M}^{s}+\eta_{M}^{d}\right)^{2}}\left(\frac{\eta_{M}^{s}}{3 k_{K}}+\frac{\eta_{M}^{s}}{3 k_{M}}-\frac{\eta_{M}^{d}}{2 \mu_{K}}-\frac{\eta_{M}^{d}}{2 \mu_{M}}\right)
\tag{54}
$$

$$
M_{o}^{\infty}=\frac{16}{45} \frac{\left(9 k_{M}+4 \mu_{M}\right)\left(3 k_{M}+4 \mu_{M}\right)}{\left(3 k_{M}+2 \mu_{M}\right)\left(3 k_{M}+\mu_{M}\right)} \tag{55}
$$

$$
M_{-1}^{\infty}=\frac{16}{15} \frac{k_{M} \mu_{M}\left(63 k_{M}^{2}+60 k_{M} \mu_{M}+16 \mu_{M}^{2}\right)}{\left(3 k_{M}+\mu_{M}\right)^{2}\left(3 k_{M}+2 \mu_{M}\right)^{2}}\left(\frac{3 k_{M}}{\eta_{M}^{s}}+\frac{3 k_{M}}{\eta_{K}^{s}}-\frac{2 \mu_{M}}{\eta_{M}^{d}}-\frac{2 \mu_{M}}{\eta_{K}^{d}}\right)
\tag{56}
$$

Combining (12) and (49) together with (52), the series expansions of the shear 'compliance' in the vicinity of $p=0$ and $p=\infty$, respectively, read:

$$
\begin{aligned}
p=0: \quad \frac{1}{\mu^{h o m^{*}}}=2 \frac{1+\epsilon M_{o}^{o}}{\eta_{M}^{d}} \frac{1}{p}+2 \frac{\epsilon M_{1}^{o}}{\eta_{M}^{d}}+\left(1+\epsilon M_{o}^{o}\right)\left(\frac{1}{\mu_{M}}+\frac{1}{\mu_{K}}\right)+O(p)
\tag{57}
\end{aligned}
$$

and
$$
p=\infty: \quad \frac{1}{\mu^{h o m^{*}}}=\frac{1+\epsilon M_{o}^{\infty}}{\mu_{M}}+\frac{1}{p}\left(2\left(1+\epsilon M_{o}^{\infty}\right)\left(\frac{1}{\eta_{M}^{d}}+\frac{1}{\eta_{K}^{d}}\right)+\frac{\epsilon M_{-1}^{\infty}}{\mu_{M}}\right)+O\left(1 / p^{2}\right)
\tag{58}
$$

In turn, alternative series expansions of $1 / \mu^{h o m^{*}}$ are derived from the Burger model approximation (Equation (51)):
$$
p=0: \quad \frac{1}{\mu^{h o m^{*}}}=\frac{2}{\eta_{M}^{d}(\epsilon)} \frac{1}{p}+\frac{1}{\mu_{M}(\epsilon)}+\frac{1}{\mu_{K}(\epsilon)}+O(p)
\tag{59}
$$
and
$$
p=\infty: \quad \frac{1}{\mu^{h o m^{*}}}=\frac{1}{\mu_{M}(\epsilon)}+\frac{2}{p}\left(\frac{1}{\eta_{M}^{d}(\epsilon)}+\frac{1}{\eta_{K}^{d}(\epsilon)}\right)+O\left(1 / p^{2}\right)
\tag{60}
$$

The damaged stiffness and viscosity parameters, that is $\mu_{M}(\epsilon), \mu_{K}(\epsilon), \eta_{M}^{d}(\epsilon)$ and $\eta_{K}^{d}(\epsilon)$, must ensure the compatibility between (57) and (59), as well as between (58) and (60). This yields:
$$
\begin{aligned}
& \frac{1}{\mu_{M}(\epsilon)}=\frac{1+m_{M} \epsilon}{\mu_{M}} \quad ; \quad \frac{1}{\mu_{K}(\epsilon)}=\frac{1+m_{K} \epsilon}{\mu_{K}} \\
& \frac{1}{\eta_{M}^{d}(\epsilon)}=\frac{1+v_{M}^{d} \epsilon}{\eta_{M}^{d}} \quad ; \quad \frac{1}{\eta_{K}^{d}(\epsilon)}=\frac{1+v_{K}^{d} \epsilon}{\eta_{K}^{d}}
\end{aligned}
\tag{61}
$$
where a set of constants $m_{M}, m_{K}, v_{M}^{d}$ and $v_{K}^{d}$ are determined from the following system (Figure 2):
$$
\begin{gathered}
m_{M}=M_{o}^{\infty} \quad ; \quad v_{M}^{d}=M_{o}^{o} \\
\frac{m_{M}-M_{o}^{o}}{\mu_{M}}+\frac{m_{K}-M_{o}^{o}}{\mu_{K}}=2 \frac{M_{1}^{o}}{\eta_{M}^{d}} \quad ; \quad \frac{v_{M}^{d}-M_{o}^{\infty}}{\eta_{M}^{d}}+\frac{v_{K}^{d}-M_{o}^{\infty}}{\eta_{K}^{d}}=\frac{M_{-1}^{\infty}}{2 \mu_{M}}
\end{gathered}
\tag{62}
$$

Despite the fact that the damaged Burger model is identified from the short- and long-term regimes, it appears to be an excellent approximation in between these limit cases.

## CONCLUDING REMARKS

The homogenization of NAVL heterogenous media is generally regarded as a simple extension of the linear elastic case, because of the correspondence principle based on the Laplace-Carson transform. However, in the case of cracks, attention must be paid to the local geometrical nonlinearity which prevents a straightforward application of standard Eshelby-based homogenization schemes in the Laplace-Carson space. In turn, the so-called stress-based dilute scheme is an appropriate one for the derivation of the

'true' effective behavior. It is based on the solution to a classical problem of linear fracture mechanics, in which the geometrical transformation of the crack is characterized by the displacement jump induced by stress boundary conditions at infinity. As opposed to the strain in the crack, the displace- ment jump is a linear function of the macroscopic stress. This is the reason why the (linear) Laplace-Carson transform and the correspondence princi- ple can be implemented in the framework of the stress-based dilute scheme, while Eshelby-based homogenization schemes fail.

For the sake of practical implementation, our purpose was to derive an approximate effective behavior of a NAVL cracked medium within the class of Burger models. Accordingly, we have proposed micromechanics-based analytical expressions of the effective elastic and viscous coefficients, in the form of simple functions of the damage parameter. As opposed to various examples of NALV composites (e.g. Rougier et al., 1993), this means that the long-range memory effect reported in the literature does not manifest itself in this situation. Indeed, while the 'true' effective behavior does not rigorously belong to the class of Burger models, the associated relaxation spectrum proves to remain discrete. However, it is believed that this result is strongly related to the stress-based dilute scheme.

## REFERENCES

Beurthey, S. and Zaoui, A. (2000). Structural Morphology and Relaxation Spectra of Viscoelastic Heterogeneous Materials, *European Journal of Mechanics A/Solids*, **19**: 1-16.

Budiansky, B. and O'Connell, R. (1976). Elastic Moduli of a Cracked Solid, *International Journal of Solids and Structures*, **12**: 81-97.

Dormieux, L., Kondo, D. and Ulm, F. (2006). *Microporomechanics*, Chichester: Wiley.

Deudé, V., Dormieux, L., Kondo, D. and Maghous, S. (2002). Micromechanical Approach to Nonlinear Poroelasticity: Application to Cracked Rocks, *Journal of Engineering Mechanics*, **128**: 848-855.

Eshelby, J.D. (1957). The Determination of the Elastic Field of an Ellipsoidal Inclusion, and Related Problems, *Proceedings of the Royal Society of London. Series A*, **241**: 376-396.

Horii, H. and Nemat-Nasser, S. (1983). Overall Modulii of Solids with Microcracks : Load- induced Anisotropy, *Journal of the Mechanics and Physics of Solids*, **31**: 155-171.

Dormieux, L. and Kondo, D. (2009). Stress-based Estimates and Bounds of Effective Elastic Properties: The Case of Cracked Media with Unilateral Effects, *Computational Material Science*, **46**: 173-179.

Lahellec, N. and Suquet, P. (2007). Effective Behavior of Linear Viscoelastic Composites: A Time-integration Approach, *International Journal of Solids and Structures*, **44**: 507-529.

Le, Q.V. (2008). Modélisation Multi-échelle Des Matériaux Viscoélastiques Hétérogènes, PhD Thesis, Univ. Paris-Est.

Rougier, Y., Stolz, C. and Zaoui, A. (1993). Représentation Spectrale En Viscoélasticité Linéaire Des Matériaux Hétérogènes, *Comptes Rendus de l' Académie des Sciences Paris II*, **316**: 1517-1522.