Article

# Curvature Potential Unveiled Topological Defect Attractors

Luka Mesarec $^{1}$ , Aleš Iglič $^{1}$ , Veronika Kralj-Iglič $^{2}$ , Wojciech Góźdź $^{3}$ , Epifanio G. Virga $^{4}$ and Samo Kralj $^{5,6,*}$

1 Laboratory of Physics, Faculty of Electrical Engineering, University of Ljubljana, Tržaška 25, 1000 Ljubljana, Slovenia; luka.mesarec@fe.uni-lj.si (L.M.); ales.iglic@fe.uni-lj.si (A.I.)
2 Faculty of Health Sciences, University of Ljubljana, Zdravstvena pot 5, 1000 Ljubljana, Slovenia; veronika.kralj-iglic@zf.uni-lj.si
3 Institute of Physical Chemistry, Polish Academy of Sciences, Kasprzaka 44/52, 01-224 Warsaw, Poland; wtg@ichf.edu.pl
4 Department of Mathematics, University of Pavia, 27100 Pavia, Italy; eg.virga@unipv.it
5 Condensed Matter Physics Department, Jožef Stefan Institute, Jamova 39, 1000 Ljubljana, Slovenia
6 Faculty of Natural Sciences and Mathematics, University of Maribor, Koroška 160, 2000 Maribor, Slovenia
* Correspondence: samo.kralj@um.si; Tel.: +386-31-389-278

Abstract: We consider the theoretical and positional assembling of topological defects (TDs) in effectively two-dimensional nematic liquid crystal films. We use a phenomenological Helfrich-Landau-de Gennes-type mesoscopic model in which geometric shapes and nematic orientational order are expressed in terms of a curvature tensor field and a nematic tensor order parameter field. Extrinsic, intrinsic, and total curvature potentials are introduced using the parallel transport concept. These potentials reveal curvature seeded TD attractors. To test ground configurations, we used axially symmetric nematic films exhibiting spherical topology.

Keywords: topological defects; nematic liquid crystals; nematic shells; geometric potentials; curvature

---

## 1. Introduction

Topological defects (TDs) [1] refer to localized regions in an ordered manifold, where the local order is frustrated. They are present in all branches of physics because the sole condition for their existence is symmetry breaking [2]. Several key features of TDs could be extracted by studying two-dimensional (2D) systems, which could be efficiently mathematically and numerically approached [3]. Two-dimensional systems are, in particular, convenient as a means of analyzing the impact of geometry (curvature, topology) on the creation, stabilization, and positional assembling of TDs [4].

Two-dimensional systems hosting an orientational order field could exhibit point TDs [1]. Their key feature is characterized by a topological charge, which is a quantized and conserved quantity [5]. In 2D, this is equivalent to the winding number $m$ [5], which elucidates the total reorientation of the respective order parameter field on encircling the defect counterclockwise. One commonly refers to TDs exhibiting $m > 0$ and $m < 0$ as defects and antidefects. In general, a nearby pair {defect, antidefect} = {$\mathfrak{m}, -\mathfrak{m}$} tends to annihilate into a local defectless state. Namely, TDs introduce local strong energetically expensive elastic distortions. For this reason, within defect cores, the ordering field is commonly melted or exhibits a qualitatively different structure with respect to bulk order [6]. TDs are, in general, rare in bulk equilibrium [2]. However, TDs might introduce new qualitative and effective properties into a system or can be exploited in several applications. Consequently, it is of interest to find efficient mechanisms, which enable the creation, stabilization, and manipulation of TDs.

In 2D systems, TDs could be efficiently controlled via the curvature of the ordered manifold. One commonly distinguishes between intrinsic and extrinsic curvature [7,8]. Note that several theoretical approaches express elastic distortions in terms of covariant

---

![](./images/812430325333360640_1.jpg)

Citation: Mesarec, L.; Iglič, A.; Kralj-Iglič, V.; Góźdź, W.; Virga, E.G.; Kralj, S. Curvature Potential Unveiled Topological Defect Attractors. Crystals 2021, 11, 539. https://doi.org/10.3390/cryst11050539

Academic Editor: Christophe Blanc

Received: 27 April 2021
Accepted: 7 May 2021
Published: 12 May 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812430325333360640_2.jpg)

Copyright: © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

Crystals 2021, 11, 539. https://doi.org/10.3390/cryst11050539
https://www.mdpi.com/journal/crystals

derivatives [7,8]. These penalize deviations of the ordering field from local geodesics (the latter are analogs of straight lines in Euclidean space). In such approaches, the extrinsic curvature contributions, which are sensitive to how a 2D curved manifold is embedded in 3D, are discarded. Note that the energy associated with the extrinsic term, as described in [7,8], was actually considered in essentially the same form in studying biological membrane shapes [9–14] without TDs (the deviatoric term in Appendix C). A simple analysis [7] suggests that both intrinsic and extrinsic curvatures are in general present, featuring in elastic-free energies weighted by elastic constants of comparable magnitude. Furthermore, in several cases, the local impact of intrinsic and extrinsic contributions on TDs could be conflicting [7,8]. However, research on the mutual influence of curvature and TDs is relatively scarce.

An ideal system to study the physics of TDs is constituted by nematic liquid crystals (NLCs) [15,16]. In bulk equilibrium, NLCs are commonly described in terms of the nematic director field $n$, which exhibits head-to-tail symmetry, and tends to be uniformly aligned in bulk equilibrium. Due to their unique combination of liquid crystallinity, softness, optical transparency, and diversity, TDs could be relatively easily created, manipulated, and observed. Furthermore, thin and effectively 2D LC structures could be relatively easily experimentally realized, e.g., in nematic LC shells or biological membranes [17–21].

In this paper, we consider the role of combined intrinsic and extrinsic curvatures on structures in 2D nematic shells. We introduce the geometric potentials [21,22] that will reveal "hotspots", to which TDs are attracted. The structure of the paper is as follows. In the Methods section, we present our model, where we describe 2D configurations using both nematic and curvature fields, represented in tensorial form. Curvature potentials are introduced along with axially symmetric shapes, which we use to illustrate curvature-driven phenomena. In the Results section, we present examples, which demonstrate the usefulness of geometric potentials to predict positional assembling of LCs on curved substrates. In the Appendices A–C, we describe some technical details.

## 2. Methods

We consider a two-dimensional curved manifold exhibiting a nematic in-plane orientational order. At the mesoscopic level, this is commonly described by the *nematic director* field [16], $n$, which is of unit length and exhibits the head-to-tail symmetry (i.e., $|n| = 1$, and the states $\pm n$ are physically equivalent). An equilibrium ground state of $n$ is uniformly aligned along a single symmetry breaking direction in flat 2D manifolds. On the contrary, curved manifolds could host TDs due to topological reasons [5]. In the following, we present how one could predict the spatial positions of TDs for a given substrate geometry without solving the relevant Euler–Lagrange equilibrium equations. For illustration purposes, we henceforth limit the study to closed surfaces exhibiting spherical topology.

### 2.1. Intrinsic and Extrinsic Curvature Contributions

Orientational order on a curved manifold is in general controlled by two qualitatively different mechanisms: the intrinsic and extrinsic curvature contributions [7,8]. We first present their main roles using a minimal model, in which order is solely represented by $n$, which we parametrize by an angle $\theta$ as

$$
n = \cos\theta e_1 + \sin\theta e_2 . \tag{1}
$$

Here, the unit vectors $\{e_1, e_2\}$ determine the local principal curvature directions [23]. These define the outer local surface normal of a local surface patch: $v = e_1 \times e_2$.

We express the elastic free energy density in terms of a single positive constant $K$ [16]

$$
f_e = \frac{K}{2}|\nabla_s n|^2 . \tag{2}
$$

This contribution enforces spatially homogeneous orientational order. The operator $\nabla_s(\bullet) = \nabla(\bullet)(e_1 \otimes e_1 + e_2 \otimes e_2)$ stands for the surface gradient [24], which deprives the "common" gradient $\nabla$ of the leg along $v$. As $\{e_1,e_2\}$ correspond to principal curvature directions, we can write [25]

$$
\nabla_s e_1 = \kappa_{g1} e_2 \otimes e_1 + \kappa_{g2} e_2 \otimes e_2 - \sigma_1 v \otimes e_1, \tag{3a}
$$

$$
\nabla_s e_2 = -\kappa_{g1} e_1 \otimes e_1 - \kappa_{g2} e_1 \otimes e_2 - \sigma_2 v \otimes e_2. \tag{3b}
$$

Here, $\kappa_{g1}$ ($\kappa_{g2}$) is the geodesic curvature and $\sigma_1$ ($\sigma_2$) the principal curvature along $e_1$ ($e_2$), respectively. It follows from Equation (3) that

$$
|\nabla_s n|^2 = |\nabla_s \theta + A|^2 + n.\underline{C}^2 n, \tag{4}
$$

where

$$
\underline{C} = \sigma_1 e_1 \otimes e_1 + \sigma_2 e_2 \otimes e_2 \tag{5}
$$

stands for the curvature tensor and

$$
A = \kappa_{g1} \ e_1 + \kappa_{g2} \ e_2 \tag{6}
$$

is referred to as the spin connection [23,24]. The invariants of $\underline{C}$, trace and determinant, yield the mean curvature $H$ and the Gaussian curvature $G$:

$$
H = \frac{1}{2}(\sigma_1 + \sigma_2), \tag{7a}
$$

$$
G = \sigma_1 \sigma_2. \tag{7b}
$$

For later use, we also define the deviatoric curvature measure [9] as

$$
E = -\left|\sigma_1^2 - \sigma_2^2\right|. \tag{7c}
$$

Furthermore,

$$
\nabla \times A = G v. \tag{8}
$$

The first and the second terms in the right-hand side of Equation (4) are typical representatives of intrinsic and extrinsic curvature contributions. Note that, in the single elastic constant approximation, both terms are present and are weighted by the same constant $K$.

The intrinsic term is the origin of ordering frustration in cases $G \neq 0$, which could be resolved by introducing TDs. On the other hand, the extrinsic term acts as a local ordering field, which is present if the principal curvatures are different. The key roles of these terms are summarized in Appendix A. There, we illustrate that a local surface patch possessing $G > 0$ ($G < 0$) attracts TDs with a positive (negative) topological charge. Furthermore, regions exhibiting $E < 0$ tend to expel TDs. Namely, in them a local ordering along a preferred orientation is enforced, which is incompatible with local nematic ordering of TDs.

### 2.2. Helfrich–Landau-Type Phenomenological Model

We next consider a more detailed model in which we focus on the impact of curvature on the position of TDs in nematic orientational order. We introduce the geometric potentials derived from the model free energy, which efficiently determine the location of TDs for a given manifold geometry. Positions of TDs reflect the interplay between intrinsic and extrinsic curvature contributions.

We describe the nematic order by the tensor order parameter field $Q$. In the local curvature principal frame (see Equation (5)), we use the following parametrization [24]

$$
\underline{Q} = q_0(e_1 \otimes e_1 - e_2 \otimes e_2) + q_m(e_1 \otimes e_2 + e_2 \otimes e_1). \tag{9}
$$

Here, $q_0$ and $q_m$ are variational variables. In its eigenframe, determined by the nematic director field $n$ (see Equation (1)) it can be expressed as [24]:

$$
\underline{Q}=\lambda\left(n \otimes n-n_{\perp} \otimes n_{\perp}\right).\tag{10}
$$

Here, $\{n, n_{\perp}\}$ are the eigenvectors of $\underline{Q}$, corresponding to eigenvalues $\{\lambda, -\lambda\}$, where $\lambda \in [0,\ 1/2]$ reveals the amplitude of nematic order in an infinitesimally small surface patch determined by the surface normal $v = n \times n_{\perp}$.

In the spirit of the classical Landau-type approach, we expand the free energy density $f = f_H + f_c + f_e$ in terms of invariants constructed using $\underline{Q}$ and $\underline{C}$. The classical Helfrich curvature ($f_H$), condensation ($f_c$), and elastic ($f_e$) contributions are expressed as [21,26]

$$
f_{H}=\frac{\kappa}{2}(Tr \underline{C})^{2},\tag{11a}
$$

$$
f_{c}=\alpha_{0}\left(T-T^{*}\right) Tr \underline{Q}^{2}+\frac{\beta}{4}\left(Tr \underline{Q}^{2}\right)^{2},\tag{11b}
$$

$$
f_{e}=\frac{1}{2} k_{i} Tr\left(\nabla_{s} \underline{Q}\right)^{2}+k_{e} Tr\left(\underline{Q} \underline{C}^{2}\right).\tag{11c}
$$

We introduced only the most essential terms to explain key mechanisms controlling positions of TDs. The classical Helfrich vesicle curvature contribution [26] $f_H$ is weighted by a positive bending modulus $\kappa$; it describes resistance to the manifold bending deformations. The quantities $\alpha_0$, $\beta$, $T^*$ in $f_c$ are positive phenomenological constants. The condensation term enforces nematic orientational order below the critical temperature $T_c$. In a flat geometry, $T_c = T^*$ and the condensed bulk equilibrium nematic order for $T < T^*$ is given by

$$
\lambda_{0}=\sqrt{\frac{\alpha_{0}\left(T^{*}-T\right)}{\beta}}.\tag{12}
$$

In the elastic free energy term, we included the simplest symmetry, which allowed for intrinsic and extrinsic curvature contributions, which are weighted by positive intrinsic ($k_i$) and extrinsic ($k_e$) elastic moduli.

### 2.2.1. Scaling and Dimensionless Free Energy Terms

In our illustrations we restrict to closed 2D manifolds hosting in-plane nematic order, where $T < T_c$. We consider axially symmetric geometries of surface area $A$, exhibiting spherical topology.

For mathematical and numerical convenience, we scale the tensor order parameter with respect to the reference bulk equilibrium order $\lambda_0$ (i.e., within a flat uniformly aligned nematic film, see Equation (12)). The curvature tensor and spatial coordinates are scaled with respect to describing the radius of a spherically shaped manifold of surface area $A$. Therefore, $\underline{Q} \rightarrow \underline{Q}/\lambda_0$, $\underline{C} \rightarrow R\underline{C}$, $\nabla_s \rightarrow R\nabla_s$.

$$
R=\sqrt{A /(4 \pi)},\tag{13}
$$

In addition to the geometrically imposed length scale $R$, an important role is also played by the nematic order parameter correlation length $\xi$. It describes a typical distance on which a locally perturbed nematic amplitude is recovered. We estimate it by

$$
\xi=\sqrt{k_{i} /\left(\alpha_{0}\left(T^{*}-T\right)\right)}.\tag{14}
$$

The resulting dimensionless free energy density ($f \rightarrow fR^2/k_i$) reads as

$$
f=\frac{1}{2} \frac{\kappa}{k_{i}} Tr \underline{C}^{2}+\lambda_{0}^{2}\left(\left(\frac{R}{\xi}\right)^{2} g_{c}+\frac{1}{2} g_{i}+\mu g_{e}\right),\tag{15}
$$

$$
g_{c}=-Tr \underline{Q}^{2}+\frac{1}{4}\left(Tr \underline{Q}^{2}\right)^{2},
\tag{16a}
$$

$$
g_{i}=Tr\left(\nabla_{s} \underline{Q}\right)^{2},
\tag{16b}
$$

$$
g_{e}=Tr\left(\underline{Q} \underline{C}^{2}\right),
\tag{16c}
$$

where $\mu=\frac{k_{e}}{\lambda_{0} k_{i}}$.

Note that the extrinsic term is weighted against the intrinsic term by a dimensionless coefficient $\mu \propto \lambda_{0}^{-1}$, which tends to diverge on approaching $T_{c}$ from below. In the numerical analysis, we used the parametrization of $\underline{Q}$ given by Equation (9) in terms of the scaled variational fields $\left\{q_{0} / \lambda_{0}, q_{m} / \lambda_{0}\right\}$. We consider axially symmetric 2D closed manifolds referred to as a 3D Cartesian system $(x, y, z)$, defined by unit vectors $\left\{e_{x}, e_{y}, e_{z}\right\}$. We represent the position vector $r$ defining the 2D shapes by

$$
r=\rho(s) \cos (\varphi) e_{x}+\rho(s) \sin (\varphi) e_{y}+z(s) e_{z}.
\tag{17}
$$

where $\rho(s)$ and $z(s)$ are the coordinates of the shape profile in the $(\rho, z)$-plane, $\varphi \in[0,2 \pi]$ stands for the azimuthal angle and $s$ represents the arc length of the profile curve.

We calculate 2D shapes and the corresponding nematic structures by minimizing the total free energy for a given relative volume $v=\frac{V}{V_{0}} \in[0,1]$. Here, $V$ refers to the volume enclosed by an axially symmetric shape of total surface area $A$, and $V_{0}=4 \pi R^{3} / 3$ is the volume of the sphere having the same surface area, where $R$ is given by Equation (13). Technical details are given in Appendix B.

### 2.2.2. Curvature Potentials

We introduce geometric curvature potentials [22] which reveal attracting or repelling regions for TDs within a curved manifold. These potentials are calculated for a given geometry of the manifold.

To this purpose, we need to identify local ground states of $\underline{Q}$ for a given manifold geometry. In flat geometry, this corresponds to a spatially homogeneous alignment of $n$ along a single symmetry breaking direction, and $\lambda=\lambda_{0}$, yielding $g_{i}=g_{e}=0$. In curved manifolds the local ground state might exhibit a finite elastic penalty, which we refer to as the fossil elastic energy (see also [27]).

To determine this, we request that the nematic director is locally parallel transported [24]. In this case, it exhibits locally minimal elastic distortions. A locally parallel transported unit vector $e^{(p)}$ (the superscript (p) indicates that a vector is parallel transported) obeys the equation [24]

$$
\nabla_{s} e^{(p)}=-v \otimes \underline{C} e^{(p)}.
\tag{18}
$$

The corresponding scaled parallel transported nematic order tensor is expressed as

$$
\underline{Q}^{(p)}=n^{(p)} \otimes n^{(p)}-n_{\perp}^{(p)} \otimes n_{\perp}^{(p)}.
\tag{19}
$$

Note that the assumption that $\lambda=\lambda_{0}$ is here understood. Taking into account Equations (1), (18) and (19) we obtain

$$
w_{i} g_{i}^{(p)}=Tr\left(\nabla_{s} \underline{Q}^{(p)}\right)^{2}=\sigma_{1}^{2}+\sigma_{2}^{2},
\tag{20a}
$$

$$
w_{e} g_{e}^{(p)}=Tr\left(\underline{Q}^{(p)} \underline{C}^{2}\right)=\left(\sigma_{1}^{2}-\sigma_{2}^{2}\right) \cos (2 \theta).
\tag{20b}
$$

The equations above introduce the intrinsic curvature potential $w_{i}$ and the extrinsic curvature potential $w_{e}$. One sees that $w_{i}$ is independent of $\theta$. Next, $w_{e}$ is directly proportional to the deviatoric free energy term which was originally introduced in studying biological membrane shapes [12,14,28,29] (see Appendix C). For a positive value of $k_{e}$

$(\mu > 0)$, the extrinsic curvature potential tends to align $\boldsymbol{n}$ along the principal direction exhibiting minimal absolute curvature, for which $w_e^{(min)} = -|\sigma_1^2 - \sigma_2^2|$. This term acts similar to an ordering field, which is incompatible with a local nematic TD. Consequently, regions, where the extrinsic curvature is present, do not favor the presence of TDs.

An additionally important parameter affecting the location of TDs is the effective local temperature. Namely, the presence of TDs in 2D requires local melting of nematic order. In our model, $\lambda = 0$ at the center of TDs. However, this is energetically costly below $T_c$. Namely, in bulk equilibrium, where $T_c = T^*$, the condensation of nematic order is energetically advantageous and $f^{(eq)} = f_c^{(eq)} = -\alpha_0^2(T^* - T)^2/(4\beta)$. Here, the superscript (eq) denotes the bulk equilibrium condition. The linear size of the defect core is roughly given by the nematic correlation length. Therefore, the free energy penalty $\Delta F$ for introducing a point defect is roughly given by

$$
\Delta F \sim \frac{\alpha_0^2(T_c - T)^2}{4\beta} \pi \xi^2. \tag{21}
$$

Furthermore, elastically distorted regions exhibit effectively different temperatures. To illustrate this, we limit ourselves to consider the intrinsic curvature term, which is quadratic in $\lambda^2$. Neglecting spatial variations in $\lambda$, and taking into account only quadratic contribution in $\lambda$, we have that

$$
f_c + f_e \sim \alpha_0(T - T^*)2\lambda^2 + \frac{k_i\lambda^2}{2} w_i = \alpha_0\left(T - T_{eff}^*\right)2\lambda^2, \tag{22}
$$

where

$$
T_{eff}^* = T^* - \frac{k_i}{4\alpha_0} w_i. \tag{23}
$$

Therefore, in elastically distorted regions, the critical temperature is effectively reduced, which locally softens the nematic order. Consequently, such regions attract cores of TDs. Note that both geometric potentials are, in general, present in a distorted region. Their common impact on the local nematic amplitude is measured by

$$
w_t = \frac{1}{2} w_i + \mu\ w_e^{(min)}, \tag{24}
$$

which we refer to as the total curvature potential. Here, $w_e^{(min)}$ corresponds to the minimal value of $w_e$ upon varying $\theta$. Our approximate analysis suggests that TDs will be attracted to regions where $w_t > 0$ exhibits a maximum. That is, in these regions, the nematic order is softer due to an effectively lower local phase transition temperature.

## 3. Results

Of our interest here is the impact of intrinsic and extrinsic curvature on positions of TDs in nematic order within axially symmetric closed surfaces which are accessible in our model. It is already well known that regions exhibiting $G > 0$ ($G < 0$) attract TDs bearing positive (negative) topological charge if the extrinsic curvature is neglected. We aim to primarily predict positions of TDs for a given substrate geometry, where both curvature contributions are taken into account.

Figure 1 shows the typical, qualitatively different, and axially symmetric structures considered in our study and their essential geometric properties, i.e., a spatially varying Gaussian curvature $G$ (Equation (7b)) and a nonvanishing deviatoric curvature $E$ (Equation (7c)), both expressed as functions of the arc length $s$ along the generating profile. They are commonly dubbed stomatocytes, oblates, and prolates, and are depicted in black, red, and blue color, respectively. The key parameter determining their stability is the reduced volume $v$. Stomatocytes are stable for a relatively low $v$ values. Their salient feature is a narrow neck where $G \ll 0$, whereas elsewhere $G > 0$. Prolate-type shapes are stable for

relatively large values of $v$. The Gaussian curvature is maximal at poles and the deviatoric curvature has maximal absolute value at the equatorial region. At intermediate $v$ values oblate-type structures are stable. In them, the positive Gaussian curvature and the absolute value of deviatoric curvature exhibit a pronounced maximum at the equatorial region.

![](./images/812430325333360640_3.jpg)

Figure 1. Typical $G(s)$ (thick lines) and $E(s)$ (thin lines) spatial variations for stomatocytes (black color), oblates (red color) and prolates (blue color). $L_s$ is the length of the profile curve and $R$ the radius of the sphere with the same surface area as the surface of the investigated shape.

In Figure 2, we plot the extrinsic curvature potential $w_e$ for the representative prolate (Figure 2a), oblate (Figure 2b), and stomatocyte (Figure 2c) shapes for varying $s$ and $\theta$. The diagrams reveal a curvature-preferred local orientation of $n$. Furthermore, regions with a large enough $|w_e|$ do not favor the presence of TDs. In Figure 3, we present the total curvature potential $w_t$ for these shapes for varying $s$ and $\mu$, which measures the relative importance of extrinsic and intrinsic curvature contributions. One sees that $\mu$ has a particularly strong impact on oblate shapes (Figure 3b). Typical equilibrium configurations (shapes and nematic textures) in the absence ($\mu=0$) and for a relatively strong presence of extrinsic curvature contribution ($\mu=1$) are plotted in Figures 4 and 5, respectively. In the first panels, we plot nematic configurations in the $(s,\varphi)$ plane. Centers of defects are revealed by regions where $\lambda=0$ and we mark them with capital letters A, B. The linear size of defect cores, where the nematic order is essentially melted, is roughly given by $\xi$. In the second panels, we plot shapes of closed nematic shells, where we also indicate the location of TDs. In the third panels, we plot $w_t=w_t(s)$ dependence of corresponding shapes. One sees that maxima of $w_t(s)$ are indeed attractors of TDs.

![](./images/812430325333360640_4.jpg)

Figure 2. Extrinsic potential $w_e$ as a function of the arc length $s$ and the nematic director orientation angle $\theta$ for (a) prolates, (b) oblates and (c) stomatocytes. Shell profiles are given within graphs for each shape. $L_s$ stands for the length of the profile curve.

![](./images/812430325333360640_5.jpg)

Figure 3. Dependence of $w_t$ on the arc length $s$ upon increasing the relative weight of the extrinsic term $2k_\mathrm{e}/k_\mathrm{i}$ for (a) prolates, (b) oblates and (c) stomatocytes. Red lines denote global and local maxima of $w_t$. Shell profiles are given within graphs for each shape.

![](./images/812430325333360640_6.jpg)

Figure 4. Intrinsic curvature dominated order parameter profiles, equilibrium membrane shapes and the corresponding $w_t(s)$ profiles for (a) prolates, (b) oblates and (c) stomatocytes. The nematic director field is superimposed onto the order parameter profile $\lambda/\lambda_0$ in the $(\varphi,s)$-plane. The function $w_t(s)$ was calculated for $\lambda_0=1/2$. Positions of TDs are denoted with capital letters. $L_s$ stands for the length of the profile curve. Parameters: (a) $v=0.80$, (b) $v=0.60$, (c) $v=0.45$; $R/\xi=7$, $k_\mathrm{e}=0$, $k_\mathrm{i}=\kappa$.

![](./images/812430325333360640_7.jpg)

Figure 5. Extrinsic curvature dominated order parameter profiles, equilibrium membrane shapes and the corresponding $w_t(s)$ profiles for (a) prolates, (b) oblates and (c) stomatocytes. The nematic director field is superimposed onto the order parameter profile $\lambda/\lambda_0$ in the $(\varphi,s)$-plane. The function $w_t(s)$ was calculated for $\lambda_0=1/2$. Positions of TDs are denoted with capital letters. $L_s$ stands for the length of the profile curve. Parameters: (a) $v=0.80$, (b) $v=0.60$, (c) $v=0.45$; $R/\xi=7$, $k_e=k_i/2$, $k_i=\kappa$.

Below, we discuss in more detail the role of curvature fields in determining the location of TDs. Note that, according to the Gauss-Bonnet and Poincaré-Hopf theorems [23], the to- tal topological charge of TDs equals $m=2$ for the spherical geometry (see Equation (A2) in Appendix A). Furthermore, highly charged TDs are energetically unfavorable for structures characterized by $\frac{R}{\xi}\gg1$. For this reason, TDs bearing elementary charges $|m|=1/2$ are favored. Consequently, prolate and oblate structures possess four $m=1/2$ TDs. On the con- trary, the stomatocytes possess a region where $G<0$, which attracts $m<0$. Furthermore, $|G|$ is large enough in this region to trigger the nucleation of additional defect-antidefect pairs $\left\{m=\frac{1}{2},m=-\frac{1}{2}\right\}$ aiming to establish topological neutrality in each surface patch characterized by different values of the average Gaussian curvature $\overline{G}$ (see Appendix A).

For $\mu=0$ the positions of defects are dominated by intrinsic curvature and are attracted to maxima of $w_t(s)$. Note that, in the case of prolate shapes, the defects are not exactly placed at maxima of $w_t(s)$, because these points attract two TDs of the same charge and are, therefore, mutually repealed. On the contrary, in oblate structures, the equatorial region is large enough to accommodate all four TDs. In stomatocytes, antidefects and defects are attracted to the respective maxima of $w_t(s)$ in regions exhibiting $G<0$ and $G>0$, respectively. This is in line with the ETCC mechanism [20] (see Appendix A) and also the proposed "attractiveness" of $w_t(s)$ maxima. Note that, in $G>0$, the regions'

maxima are relatively shallow. Consequently, locations of $m=1/2$ TDs are dominated by their mutual repulsion.

For $\mu=1$ we observe only quantitative changes in prolate shapes and additional qualitative changes in the remaining competitive shapes. In the prolate configuration, a relatively strong extrinsic curvature field appears outside the poles of the shape. Conse- quently, the four TDs are pushed closer to the poles in comparison to the $\mu=0$ case. In this case, the extrinsic and intrinsic curvatures impose similar preferences to TDs. On the contrary, in oblate shapes the intrinsic curvature favors positioning TDs in the equatorial region, while the extrinsic one tends to expel them from there. One sees that they are located at local maxima in $w_{t}(s)$. Note that they are not located at the global maximum because, there, two mutually repelling TDs would be located at the same point. Finally, in the stomatocyte configuration shown, the extrinsic term is strong enough to prevent the formation of additional defect pairs. Note that the region at $s/L_{s}\sim0.6$ does not possess TDs. However, the nematic order there is strongly suppressed due to relatively strong local elastic distortions.

Finally, in Figure 6 we plot the stability diagram of the competing structures on varying $v$ in the presence and absence of the extrinsic contribution. One sees that the latter strongly favors oblate-type shapes.

![](./images/812430325333360640_8.jpg)

Figure 6. Stability diagram of equilibrium closed membrane shapes as a function of relative volume $v$ in the presence ($k_{\mathrm{e}}=k_{\mathrm{i}}/2$, solid line) and in the absence ($k_{\mathrm{e}}=0$, dashed line) of the extrinsic contribution. Profiles of stable shapes presented in the diagram for different values of the reduced volume $v$ and $k_{\mathrm{i}}/\kappa$ were calculated in the presence of the extrinsic term ($k_{\mathrm{e}}=k_{\mathrm{i}}/2$). Stomatocyte shapes are colored in black, oblate shapes (including discocyte shapes) in red and prolate shapes in blue. $R/\xi=7$.

## 4. Conclusions

Of interest in this study was the identification of attractor sites for topological defects (TDs) on two-dimensional (2D) curved substrates hosting nematic orientational order. In general, the positions of TDs are influenced by both intrinsic and extrinsic curvature contributions. Their impact on TDs may be antagonistic with regard to their geometries. Furthermore, in most studies so far, the role of extrinsic curvature contributions has been (in several cases unjustifiably) neglected and the combined effects of both curvature

contributions are so far scarcely explored. In our study, we intended to contribute to a general understanding of their mutual influence on TDs in orientational order.

In our theoretical analysis, we described the local geometry by the curvature tensor and the nematic order by the nematic tensor order parameter. Positions of centers of points of TDs in our study were fingerprinted by points where the nematic order parameter amplitude was locally melted. To predetermine positions attracting TDs, we introduced intrinsic $w_i$ and extrinsic $w_e$ geometric potentials by applying the classical notion of parallel transport. This enabled us to determine local ground states for a given substrate geometry.

The intrinsic potential is independent of the local nematic director orientation $\theta$, while the extrinsic term depends on $\theta$. The regions characterized by $|w_e| \gg 1$ tend to expel TDs because, in them, geometrically enforced ordering is imposed, which is incompatible with locally relatively variable nematic structures of TDs. The minimization of $w_e$ with respect to $\theta$ yields its ground state value $w_e^{(\text{min})}$. Our analysis reveals that maxima of the total geometric potential $w_t = w_i + \mu\ w_e^{(\text{min})}$ are attracting TDs. Here, $\mu = k_e/(k_i\lambda_0)$ measures the relative importance of $w_i$ and $w_e^{(\text{min})}$. Note that $\mu \propto 1/\lambda_0$ and, in general, one expects comparable values of $k_e$ and $k_i$. Therefore, just below the nematic-isotropic phase transition the extrinsic contribution is expected to play a dominant role. We tested the predicting power of geometric potentials by studying curvature-imposed positional assembly of TDs in axially symmetric nematic shells, exhibiting spherical symmetry. Upon varying the relative volume $v$, the shells could exhibit three qualitatively different geometries, and in each TDs were attracted to maxima of $w_t$, confirming our expectation.

Our study effectively illustrates that curved substrates could be exploited for efficient assembling of TDs to predetermined positions. This is advantageous for several applications. For example, the cores of fixed TDs could be exploited to manipulate the polarization of light [30]. Furthermore, TDs could efficiently trap appropriate nanoparticles [31,32]. Note that TDs in liquid crystals could be relatively easily manipulated [33-41], which offers an indirect path to manipulate assemblies of trapped NPs. Finally, understanding the curvature-enabled stabilization mechanisms of TDs and their assemblies might shed light on still unresolved problems in fundamental physics [42]. For example, it seems that fields represent fundamental natural entities, and topologically protected localized field distortions, such as TDs, might be related to "particles", if nature is viewed from this alternative perspective [43].

Author Contributions: Conceptualization, S.K., L.M., V.K.-I., A.I., E.G.V.; visualization, formal analysis, software, investigation, L.M. W.G.; writing-original draft preparation, S.K., L.M.; writing-review and editing, S.K., L.M., V.K.-I., W.G., A.I., E.G.V.; supervision, S.K., A.I. All authors have read and agreed to the published version of the manuscript.

Funding: S.K. acknowledges the support of a Slovenian Research Agency (ARRS) grant P1-0099 and J1-2457. The authors acknowledge the support of a Slovenian Research Agency (ARRS) grants P1-0099, P2-0232 and J1-2457 and the funding from the European Union's Horizon 2020-Research and Innovation Framework Programme under Grant agreement No. 801338 (VES4US project). WG would like to acknowledge the support from NCN grant No. 2018/30/Q/ST3/00434.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Conflicts of Interest: The authors declare no conflict of interest.

### Appendix A

We first illustrate that the *intrinsic* curvature term can generate TDs on surface patches characterized by $G \neq 0$. Namely, its contribution $K|\nabla_{s}\theta + A|^{2}$ in Equation (4) is removed if $\nabla_{s}\theta = -A$. Applying $\nabla \times$ operation to this equation yields a frustrating condition

$$
\nabla \times \nabla_{s} \theta \equiv 0 = -\nabla \times A \propto G \neq 0, \tag{A1}
$$

which could be resolved by the local melting of order (i.e., by introducing a topological defect).

Furthermore, according to the Gauss–Bonnet and Poincaré–Hopf theorems the integrated Gaussian curvature over a closed surface hosting in-plane order is quantized:

$$
m = 2(1 - g) = \frac{1}{2\pi} G d^{2} r. \tag{A2}
$$

Here, $m$ stands for the total topological charge within the closed surface of genus $g$. The latter quantity counts the number of holes within the surface. For example, in spherical topology, $g = 0$ and $m = 2$. Equation (A2) suggests that one could imagine that a positive (negative) Gaussian curvature effectively acts as a smeared negative (positive) topological charge, which is neutralized by "real" discrete topological charge, carried by TDs. In this perspective one introduces the smeared curvature charge

$$
dm_{G} = -\frac{G d^{2} r}{2\pi} \tag{A3}
$$

to a surface elementary patch $d^{2}r$. For a closed surface, it strictly holds that $m + m_{G} = 0$, so that the total system is *topologically neutral* (i.e., the total topological charge of the whole system equals zero). Hence, Equation (A3) suggests that a local region exhibiting [33] $G > 0$ ($G < 0$) attracts TDs bearing $m > 0$ ($m < 0$).

This phenomenon is embodied in the Effective Topological Charge Cancellation (ETCC) mechanism [20,33], which refers to surfaces exhibiting spatially varying $G$. It claims that each surface patch $\Delta\zeta$, to which one can assign a characteristic average Gaussian curvature $\overline{G}[\Delta\zeta] = \frac{1}{\Delta\zeta} \iint_{\Delta\zeta} G d^{2}r$, tends to be topologically neutral. Therefore, the total topological charge $m[\Delta\zeta]$ of TDs within it tends to compensate the corresponding total smeared curvature charge $m_{G}[\Delta\zeta] = \iint_{\Delta\zeta} dm_{G}$.

Next, we focus on the *extrinsic* contribution in Equation (4). Taking into account Equation (1) and Equation (5), it follows that

$$
n.\underline{C}^{2}n = \sigma_{1}^{2} \cos^{2}\theta + \sigma_{2}^{2} \sin^{2}\theta. \tag{A4}
$$

For $K > 0$, this term is minimized for $n$ aligned along the principal direction exhibiting the minimal curvature.

### Appendix B

Here, we present technical details for calculating the equilibrium of 2D shapes and the corresponding nematic structures. Functions describing the coordinates of the shape profile $\rho(s)$ and $z(s)$ (see Equation (17)) are calculated as [20,44–46]:

$$
\rho(s) = \int_{0}^{s} \cos\theta(s') \mathrm{d}s',\ z(s) = \int_{0}^{s} \sin\theta(s') \mathrm{d}s'. \tag{A5}
$$

where the function $\theta(s)$ represents the angle of the tangent to the profile curve with the plane that is perpendicular to the axis of rotation $e_{z}$. For closed and smooth surfaces, we have to apply the following boundary conditions: $\theta(0) = 0, \theta(L_{s}) = \pi, \rho(0) = \rho(L_{s}) = 0$.

Where $L_s$ stands for the length of the profile curve. In our simulations, the function $\theta(s)$ is approximated by the Fourier series [20,44–46]:

$$
\theta(s)=\theta_{0} \frac{s}{L_{s}}+\sum_{i=1}^{N} a_{i} \sin \left(\frac{\pi}{L_{s}} i \cdot s\right), \tag{A6}
$$

where $N$ is the number of Fourier modes, $a_i$ are the Fourier amplitudes, and $\theta_0 = \theta(L_s) = \pi$ is the angle at the north pole of the surface. The local principal curvatures $\sigma_1$ and $\sigma_2$, which appear in different energy contributions, are calculated as $\frac{d\theta(s)}{ds}$ and $\frac{\sin\theta(s)}{\rho(s)}$, respectively [20].

Our goal is to determine equilibrium closed shell shapes and the nematic ordering profiles on these shells. Equilibrium shell shapes are determined by the numerical minimization of a function of many variables [44–46]. These variables include the Fourier amplitudes $a_i$ and the shape profile length $L_s$ (see Equation (A6)). During the minimization procedure, the reduced volume $v$ is kept constant. Next, we determine the equilibrium nematic configuration on previously calculated shape. The nematic order tensor is given by Equation (9), where $q_0$ and $q_m$ are variational parameters. Equilibrium configurations for $q_0$ and $q_m$ are calculated on a fixed shape by using the standard Monte Carlo method. The closed surface in the coordinates $(\varphi,s)$ is represented as a network of $101 \times 101$ points. After that, the equilibrium shape is adjusted according to the current nematic texture. We repeat this process several times to obtain the equilibrium shell shape and the equilibrium nematic configuration.

## Appendix C

Here, we demonstrate the similarity between the extrinsic term used in our study and the deviatoric term used in the study of biological membranes. Phospholipid bilayers forming a closed surface of biological membranes are assumed to be covered with anisotropic components oriented at different directions [25,26,47,48]. The orientation of the inclusion can be described by $\theta$, which in this case represents the rotation of the principal directions of the inclusion's intrinsic shape relative to the membrane principal directions. The energy of a single inclusion is proportional to the mismatch between the intrinsic shape of the inclusion and the local membrane shape [9,11,13,26,47,48]:

$$
W_{d}(\theta)=\left(2 K_{1}+K_{2}\right)\left(H-H_{m}\right)^{2}-K_{2}\left(D^{2}-2 D D_{m} \cos (2 \theta)+D_{m}^{2}\right), \tag{A7}
$$

where $K_1$ and $K_2$ are constants, $H$ is the local mean curvature of the membrane given by Equation (7a) and $D = (\sigma_1 - \sigma_2)/2$ is the curvature deviator of the membrane. Inclusion's intrinsic shape is described by its intrinsic mean curvature $H_m$ and its intrinsic curvature deviator $D_m$ [25,26,47,48]. If $D_m = 0$ the inclusion is isotropic while if $D_m \neq 0$ it is anisotropic. In this formulation, membrane components are two-dimensional (described by two parameters).

For minimal elastic distortions, the energy associated with the extrinsic term used in this study can be written as (see Equations (1), (18), (19) and (20b)):

$$
W_{e}(\theta)=k_{e}\left(\sigma_{1}^{2}-\sigma_{2}^{2}\right) \cos (2 \theta)=4 k_{e} H D \cos (2 \theta), \tag{A8}
$$

where $k_e$ is the extrinsic elastic modulus. We notice that the deviatoric term (Equation (A7)) and the extrinsic term (Equation (A8)) have the same dependence on the orientation of inclusions proportional to $\cos(2\theta)$. The main difference is that the deviatoric term takes into account also the anisotropy of the inclusion's intrinsic shape described by $D_m$. If we focus only on the orientation dependent part of the energy, we can write

$$
W(\theta)=-\gamma \cos (2 \theta), \tag{A9}
$$

where $\gamma$ is a constant, including different constants and curvatures, which can be deter- mined by comparing Equation (A9) with Equations (A7) and (A8). With the aid of statistical mechanics, we can calculate the average orientation of a single inclusion [47]:

$$
\langle\cos (2 \theta)\rangle=\frac{\int_{0}^{2 \pi} \cos (2 \theta) \exp \left(-W(\theta) / k_{B} T\right) \mathrm{d} \theta}{\int_{0}^{2 \pi} \exp \left(-W(\theta) / k_{B} T\right) \mathrm{d} \theta}, \tag{A10}
$$

where $k_{B}$ is the Boltzmann constant and $T$ is the temperature. The result of the integration includes the quotient of the modified Bessel functions $I_{0}$ and $I_{1}$ [47]:

$$
\langle\cos (2 \theta)\rangle=\frac{I_{1}\left(\gamma / k_{B} T\right)}{I_{0}\left(\gamma / k_{B} T\right)}. \tag{A11}
$$

The average orientation of the inclusion as a function of $\gamma$ is presented in Figure A1 [47].

![](./images/812430325333360640_9.jpg)

Figure A1. The average orientation $\langle\cos (2 \theta)\rangle$ of membrane inclusion as a function of $\gamma / k_{B} T$.

It can be seen in Figure A1 that the orientational ordering increases with increasing $\gamma$. In case of Equation (A7), $\gamma$ is proportional to the inclusion's intrinsic curvature deviator $D_{m}$ and the curvature deviator of the membrane $D$. The effect of orientational ordering is in this case strong in highly curved anisotropic regions containing anisotropic membrane components. In case of Equation (A8), membrane inclusions are modelled as straight rods and $\gamma$ is proportional to the mean membrane curvature $H$ and the curvature deviator of the membrane $D$. Strong orientational ordering is, therefore, present in highly curved anisotropic membrane regions except on saddle-like surfaces for which $H=0$ and $D \neq 0$.

For one-dimensional curved membrane components, we can use a model proposed in [49-52]. The elastic energy of a flexible rod-like membrane component (e.g., curved protein) is given by:

$$
W_{p}(\theta)=\kappa\left(C-C_{p}\right)^{2}, \tag{A12}
$$

where $\kappa$ is a constant, $C_{p}$ is the intrinsic curvature of the crescent-shaped membrane domain and $C$ is the local membrane curvature seen by the attached domain, which can be expressed by Euler relation as $C=H+D \cos (2 \theta)$. Here, $\theta$ is the angle between the orientation of the one-dimensional membrane domain and the principal curvature $\sigma_{1}$. Using this model, it was shown that curved BAR protein domains can induce the growth of tubular protrusions [49,52]. Without the application of external force, BAR domains were found to be oriented perpendicular to the protrusion in order to minimize the elastic energy given by Equation (A12) [52]. This theoretical prediction was recently confirmed in [53,54]. Equation (A12) can also be written as:

$$
W_{p}(\theta)=\kappa\left(H^{2}+2 H D \cos (2 \theta)-2 H C_{p}-2 D C_{p} \cos (2 \theta)+D^{2} \cos ^{2}(2 \theta)+C_{p}^{2}\right). \tag{A13}
$$

We can observe that some parts of Equation (A13) are the same as in the extrinsic term given by Equations (A7) and (A8).

## References

1.  Mermin, N.D. The topological theory of defects in ordered media. *Rev. Mod. Phys.* 1979, 51, 591. [CrossRef]
2.  Zurek, W.H. Cosmological experiments in superfluid helium? *Nature* 1985, 317, 505–508. [CrossRef]
3.  Kosterlitz, J.M.; Thouless, D.J. Ordering, metastability and phase transitions in two-dimensional systems. *J. Phys. C Solid State Phys.* 1973, 6, 1181. [CrossRef]
4.  Bowick, M.; Nelson, D.R.; Travesset, A. Curvature-induced defect unbinding in toroidal geometries. *Phys. Rev. E* 2004, 69, 041102. [CrossRef]
5.  Volovik, G.E.; Lavrentovich, O.D. Topological dynamics of defects: Boojums in nematic drops. *Sov. Phys. JETP* 1983, 85, 1159.
6.  Schopohl, N.; Sluckin, T.J. Defect core structure in nematic liquid crystals. *Phys. Rev. Lett.* 1987, 59, 2582. [CrossRef]
7.  Selinger, R.L.B.; Konya, A.; Travesset, A.; Selinger, J.V. Monte Carlo studies of the XY model on two-dimensional curved surfaces. *J. Phys. Chem. B* 2011, 115, 13989–13993. [CrossRef] [PubMed]
8.  Napoli, G.; Vergori, L. Extrinsic curvature effects on nematic shells. *Phys. Rev. Lett.* 2012, 108, 207803. [CrossRef]
9.  Kralj-Iglič, V.; Svetina, S.; Žekš, B. Shapes of bilayer vesicles with membrane embedded molecules. *Eur. Biophys. J.* 1996, 24, 311–321. [CrossRef] [PubMed]
10. Fournier, J.B. Nontopological saddle-splay and curvature instabilities from anisotropic membrane inclusions. *Phys. Rev. Lett.* 1996, 76, 4436. [CrossRef]
11. Kralj-Iglič, V.; Heinrich, V.; Svetina, S.; Žekš, B. Free energy of closed membrane with anisotropic inclusions. *Eur. Phys. J. B* 1999, 10, 5–8. [CrossRef]
12. Kralj-Iglič, V.; Iglič, A.; Hägerstrand, H.; Peterlin, P. Stable tubular microexovesicles of the erythrocyte membrane induced by dimeric amphiphiles. *Phys. Rev. E* 2000, 61, 4230. [CrossRef] [PubMed]
13. Kralj-Iglič, V.; Remškar, M.; Vidmar, G.; Fošnarič, M.; Iglič, A. Deviatoric elasticity as a possible physical mechanism explaining collapse of inorganic micro and nanotubes. *Phys. Lett. A* 2002, 296, 151–155. [CrossRef]
14. Fournier, J.B.; Galatola, P. Bilayer membranes with 2D-nematic order of the surfactant polar heads. *Braz. J. Phys.* 1998, 28. [CrossRef]
15. Lavrentovich, O.D. Topological defects in dispersed words and worlds around liquid crystals, or liquid crystal drops. *Liq. Cryst.* 1998, 24, 117–126. [CrossRef]
16. Kleman, M.; Laverntovich, O.D. *Soft Matter Physics: An Introduction*; Springer Science & Business Media: New York, NY, USA, 2007.
17. Fernández-Nieves, A.; Vitelli, V.; Utada, A.S.; Link, D.R.; Márquez, M.; Nelson, D.R.; Weitz, D.A. Novel defect structures in nematic liquid crystal shells. *Phys. Rev. Lett.* 2007, 99, 157801. [CrossRef] [PubMed]
18. Liang, H.L.; Schymura, S.; Rudquist, P.; Lagerwall, J. Nematic-smectic transition under confinement in liquid crystalline colloidal shells. *Phys. Rev. Lett.* 2011, 106, 247801. [CrossRef] [PubMed]
19. Liang, H.L.; Zentel, R.; Rudquist, P.; Lagerwall, J. Towards tunable defect arrangements in smectic liquid crystal shells utilizing the nematic-smectic transition in hybrid-aligned geometries. *Soft Matter* 2012, 8, 5443–5450. [CrossRef]
20. Mesarec, L.; Góźdź, W.; Iglič, A.; Kralj, S. Effective topological charge cancelation mechanism. *Sci. Rep.* 2016, 6, 1–12.
21. Mesarec, L.; Góźdź, W.; Iglič, A.; Kralj-Iglič, V.; Virga, E.G.; Kralj, S. Normal red blood cells’ shape stabilized by membrane’s in-plane ordering. *Sci. Rep.* 2019, 9, 1–11. [CrossRef] [PubMed]
22. Virga, E.G. Curvature Potentials for Defects on Nematic Shells. Lecture Given on the 26 June 2013 at the Isaac Newton Institute for Mathematical Sciences, Cambridge. Available online: https://sms.cam.ac.uk/media/1508874?format=mpeg4&quality=360p&fetch_type=dl (accessed on 8 May 2021).
23. Kamien, R.D. The geometry of soft materials: A primer. *Rev. Mod. Phys.* 2002, 74, 953. [CrossRef]
24. Rosso, R.; Virga, E.G.; Kralj, S. Parallel transport and defects on nematic shells. *Contin. Mech. Thermodyn.* 2012, 24, 643–664. [CrossRef]
25. Kralj, S.; Rosso, R.; Virga, E.G. Curvature control of valence on nematic shells. *Soft Matter* 2011, 7, 670–683. [CrossRef]
26. Helfrich, W. Elastic properties of lipid bilayers: Theory and possible experiments. *Z. Naturforsch. C* 1973, 28, 693–703. [CrossRef]
27. Sonnet, A.M.; Virga, E.G. Bistable curvature potential at hyperbolic points of nematic shells. *Soft Matter* 2017, 13, 6792–6802. [CrossRef] [PubMed]
28. Fischer, T.M. Bending stiffness of lipid bilayers. V. Comparison of two formulations. *J. Phys. II* 1993, 3, 1795–1805. [CrossRef]
29. Kralj-Iglič, V.; Babnik, B.; Gauger, D.R.; May, S.; Iglič, A. Quadrupolar Ordering of Phospholipid Molecules in Narrow Necks of Phospholipid Vesicles. *J. Stat. Phys.* 2006, 125, 727–752. [CrossRef]
30. Tiwari, S.C. Topological defects, geometric phases, and the angular momentum of light. *Optik* 2009, 120, 414–417. [CrossRef]
31. Coursault, D.; Grand, J.; Zappone, B.; Ayeb, H.; Lévi, G.; Félidj, N.; Lacaze, E. Linear self-assembly of nanoparticles within liquid crystal defect arrays. *Adv. Mater.* 2012, 24, 1461–1465. [CrossRef] [PubMed]
32. Karatairi, E.; Rožič, B.; Kutnjak, Z.; Tzitzios, V.; Nounesis, G.; Cordoyiannis, G.; Thoen, J.; Glorieux, C.; Kralj, S. Nanoparticle-induced widening of the temperature range of liquid-crystalline blue phases. *Phys. Rev. E* 2010, 81, 041703. [CrossRef]
33. Vitelli, V.; Turner, A.M. Anomalous coupling between topological defects and curvature. *Phys. Rev. Lett.* 2004, 93, 215301. [CrossRef] [PubMed]

34. Murray, B.S.; Pelcovits, R.A.; Rosenblatt, C. Creating arbitrary arrays of two-dimensional topological defects. *Phys. Rev. E* 2014, 90, 052501. [CrossRef] [PubMed]

35. Chiccoli, C.; Feruli, I.; Lavrentovich, O.D.; Pasini, P.; Shiyanovskii, S.V.; Zannoni, C. Topological defects in schlieren textures of biaxial and uniaxial nematics. *Phys. Rev. E* 2002, 66, 030701. [CrossRef] [PubMed]

36. Svenšek, D.; Žumer, S. Instability modes of high-strength disclinations in nematics. *Phys. Rev. E* 2004, 70, 061707. [CrossRef]

37. Nikkhou, M.; Škarabot, M.; Čopar, S.; Ravnik, M.; Žumer, S.; Muševič, I. Light-controlled topological charge in a nematic liquid crystal. *Nat. Phys.* 2015, 11, 183–187. [CrossRef]

38. Afghah, S.; Selinger, R.L.; Selinger, J.V. Visualising the crossover between 3D and 2D topological defects in nematic liquid crystals. *Liq. Cryst.* 2018, 45, 2022–2032. [CrossRef]

39. Wang, X.; Miller, D.S.; Bukusoglu, E.; De Pablo, J.J.; Abbott, N.L. Topological defects in liquid crystals as templates for molecular self-assembly. *Nat. Mater.* 2016, 15, 106–112. [CrossRef]

40. Tai, J.S.B.; Ackerman, P.J.; Smalyukh, I.I. Topological transformations of Hopf solitons in chiral ferromagnets and liquid crystals. *Proc. Natl. Acad. Sci. USA* 2018, 115, 921–926. [CrossRef]

41. Smalyukh, I.I. Knots and other new topological effects in liquid crystals and colloids. *Rep. Prog. Phys.* 2020, 83, 106601. [CrossRef]

42. Hobson, A. There are no particles, there are only fields. *Am. J. Phys.* 2013, 81, 211–223. [CrossRef]

43. Skyrme, T.H.R. A unified field theory of mesons and baryons. *Nucl. Phys.* 1962, 31, 556–569. [CrossRef]

44. Góźdź, W.T. Spontaneous curvature induced shape transformations of tubular polymersomes. *Langmuir* 2004, 20, 7385–7391. [CrossRef] [PubMed]

45. Góźdź, W.T. Influence of spontaneous curvature and microtubules on the conformations of lipid vesicles. *J. Phys. Chem. B* 2005, 109, 21145–21149. [CrossRef] [PubMed]

46. Góźdź, W.T. The interface width of separated two-component lipid membranes. *J. Phys. Chem. B* 2006, 110, 21981–21986. [CrossRef]

47. Iglič, A.; Kralj-Iglič, V.; Božič, B.; Bobrowska-Hägerstrand, M.; Isomaa, B.; Hägerstrand, H. Torocyte shapes of red blood cell daughter vesicles. *Bioelectrochemistry* 2000, 52, 203–211. [CrossRef]

48. Mesarec, L.; Drab, M.; Penič, S.; Kralj-Iglič, V.; Iglič, A. On the Role of Curved Membrane Nanodomains and Passive and Active Skeleton Forces in the Determination of Cell Shape and Membrane Budding. *Int. J. Mol. Sci.* 2021, 22, 2348. [CrossRef] [PubMed]

49. Perutková, Š.; Kralj-Iglič, V.; Frank, M.; Iglič, A. Mechanical stability of membrane nanotubular protrusions influenced by attachment of flexible rod-like proteins. *J. Biomech.* 2010, 43, 1612–1617. [CrossRef] [PubMed]

50. Baumgart, T.; Capraro, B.R.; Zhu, C.; Das, S.L. Thermodynamics and mechanics of membrane curvature generation and sensing by proteins and lipids. *Annu. Rev. Phys. Chem.* 2011, 62, 483–506. [CrossRef]

51. Iglič, A.; Slivnik, T.; Kralj-Iglič, V. Elastic properties of biological membranes influenced by attached proteins. *J. Biomech.* 2007, 40, 2492–2500. [CrossRef]

52. Mesarec, L.; Góźdź, W.; Iglič, V.K.; Kralj, S.; Iglič, A. Closed membrane shapes with attached BAR domains subject to external force of actin filaments. *Colloids Surf. B Biointerfaces* 2016, 141, 132–140. [CrossRef] [PubMed]

53. Jarin, Z.; Pak, A.J.; Bassereau, P.; Voth, G.A. Lipid-composition-mediated forces can stabilize tubular assemblies of I-BAR proteins. *Biophys. J.* 2021, 120, 46–54. [CrossRef] [PubMed]

54. Tozzi, C.; Walani, N.; Le Roux, A.L.; Roca-Cusachs, P.; Arroyo, M. A theory of ordering of elongated and curved proteins on membranes driven by density and curvature. *Soft Matter* 2021, 17, 3367–3379. [CrossRef] [PubMed]