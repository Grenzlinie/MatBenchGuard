Acta Mech 228, 547–560 (2017)
DOI 10.1007/s00707-016-1719-x
![](./images/811139273125265408_1.jpg)

ORIGINAL PAPER

G. E. Tupholme

# One-dimensional piezoelectric quasicrystals with an embedded moving, non-uniformly loaded shear crack

Received: 11 April 2016 / Revised: 28 July 2016 / Published online: 30 September 2016
© Springer-Verlag Wien 2016

Abstract Closed-form expressions are derived and discussed, using an extended dislocation layer method, for the components of the stress and electric fields created by a moving non-constantly loaded antiplane, Griffith-type strip crack within one-dimensional piezoelectric quasicrystals. Some typical numerical results are displayed graphically. Explicit results for the fields of an analogous stationary crack subjected to non-constant loading are derived, as a special case.

## 1 Introduction

Wide-ranging technological applications of quasicrystals are increasingly being exploited following their observation experimentally in 1982 by Shechtman and the first general announcement in 1984 of their discovery by Shechtman et al. [1]. Such materials unusually exhibit quasiperiodic translational symmetry and non-traditional orientational symmetry and have been found experimentally to be quite brittle and thus subject to defects.

There has been tremendous interest and progress in the development of comprehensive elasticity theories of quasicrystals, and the solutions of numerous boundary value problems within quasicrystals having been adequately reviewed and referenced by, for example, Ding et al. [2] and Fan [3,4].

However, more recently, exciting advances have been achieved on the detailed analyses and practical uti- lization of their inherent piezoelectric coupling effects. The fundamental governing equations of piezoelectric quasicrystals are now sufficiently well established for authors to have begun to study some boundary value problems in such materials by extending the techniques that have been adopted previously to successfully investigate the analogous situations in quasicrystals.

In 2004, Zhou et al. [5] investigated the piezoresistive behaviour of quasicrystals, and Li and Liu [6] used group representation theory to study the matrix forms of the piezoelectric coefficient tensors under all 31 point groups of one-dimensional quasicrystals. Further, a group-theoretical method was used by Rao et al. [7] to determine the second-order piezoelectric tensor coefficients in classes of quasicrystals.

Altay and Dökmeci [8] presented the basic equations governing the physical responses of three-dimensional piezoelectric quasicrystals in differential and variational invariant forms. The results of Li and Liu [6] were utilized by Wang and Pan [9] to analyse in detail the fields created by a screw dislocation moving uniformly within a one-dimensional hexagonal piezoelectric quasicrystal. Subsequently, Yang et al. [10] used the general- ized Stroh formalism to investigate analytically and numerically the elastic-electric fields around a stationary straight dislocation situated parallel to a periodic axis in one-dimensional quasicrystals with piezoelectric effects.

G. E. Tupholme (⊠)
Faculty of Engineering and Informatics, University of Bradford, Bradford BD7 1DP, UK
E-mail: g.e.tupholme@bradford.ac.uk
Tel.: +44 1274 234273

General three-dimensional solutions of static problems in one-dimensional hexagonal piezoelectric qua- sicrystals were developed by Li et al. [11] by the application of rigorous operator theory with two displacement functions. Using the methods of an operator and functions of a complex variable, Yu et al. [12] presented solutions of plane problems in one-dimensional piezoelectric quasicrystals, and, as an application, used the semi-inverse method to consider a mode III stationary crack in a hexagonal piezoelectric quasicrystal that is subject to far-field constant loads. Moreover, Yu et al. [13] adopted complex variable theory to investigate the elastic and electric fields of a one-dimensional hexagonal piezoelectric quasicrystal containing an antiplane elliptical cavity.

Most recently, conformal mapping techniques and complex variable theory enabled Guo et al. [14] to con- sider an embedded elliptical inclusion in one-dimensional hexagonal piezoelectric quasicrystal composites, and Yang and Li [15] to study a shear problem of a circular hole with a straight crack within one-dimensional hexagonal quasicrystals with piezoelectric effects. As a special case, these results reduce to those for a corre- sponding stationary constantly loaded Griffith crack.

However, no analysis by any technique whatsoever has been presented previously of a moving, non- constantly loaded, mode III strip crack in quasicrystals with piezoelectric effects. The objective of the analysis presented here is therefore to briefly show how the method of continuous dislocation layers, which was originally devised for use in isotropic purely elastic solids, can be appropriately adapted to explicitly deduce new and useful closed-form expressions for the fields' components of such a crack. With the boundary conditions necessitating finding the solutions of a system of three simultaneous equations which lead to three soluble integral equations, this involves considerably lengthy detailed algebraic manipulation, but nevertheless it is an extremely convenient and valuable extension of the basic technique.

In Sect. 2, the fundamental three-dimensional equations governing the behaviour of piezoelectric qua- sicrystals are first summarized, before the underlying constitutive equations of one-dimensional hexagonal piezoelectric quasicrystals with point group 6mm are outlined. The basic problem considered here is then formulated. As a prerequisite, in Sect. 3, the phonon and phason displacement and stress field components and the electric potential of a moving screw dislocation are stated, before the traditional dislocation layer method is extended, in Sect. 4, to derive and discuss closed-form representations for the fields around a non-uniformly loaded, moving antiplane shear crack, in such a material. Illustrative numerical results are displayed graphi- cally for the variation with speed of a stress component around the crack tip. In Sect. 5, the particular results for the previously unreported situation of a stationary non-uniformly loaded strip crack are deduced. Finally, a summary of the main features of this investigation is given in the concluding Sect. 6.

## 2 Basic equations for piezoelectric quasicrystals and formulation of the problem

The general three-dimensional equations governing the components of the material fields within the linear theory of piezoelectric quasicrystals have been conveniently expressed in both differential and variational invariant forms by Altay and Dökmeci [8]. Relative to a fixed system of rectangular Cartesian coordinates $(x_{1}, x_{2}, x_{3})$, the quasistatic equilibrium equations, in the absence of body forces and an electric charge density, the constitutive equations can be written compactly, respectively, using a suffix notation where $i, j, k, l=$ 1,2,3 with the adoption of the repeated suffices summation convention, as

$$
\sigma_{i j, i}=0, \quad H_{i j, i}=0, \quad D_{i j, i}=0, \tag{1}
$$

$$
\sigma_{i j}=c_{i j k l}\left(u_{k, l}+u_{l, k}\right) / 2+R_{i j k l} w_{k, l}-e_{k i j} E_{k}, \tag{2}
$$

$$
H_{i j}=R_{k l i j}\left(u_{k, l}+u_{l, k}\right) / 2+K_{i j k l} w_{k, l}-e_{k i j}^{\prime} E_{k}, \tag{3}
$$

$$
D_{i}=e_{k i j}\left(u_{j, k}+u_{k, j}\right) / 2+e_{k i j}^{\prime} w_{j, k}-\varepsilon_{i j} E_{j}, \tag{4}
$$

with a comma followed by $p$ denoting partial differentiation with respect to $x_{p}$ for $p=i, j, k, l$.

The components of the phonon stress and displacement, the phason stress and displacement, and the electric displacement and field are denoted by $\sigma_{i j}, u_{i}, H_{i j}, w_{i}, D_{i}$ and $E_{i}$, respectively, and $c_{i j k l}, R_{i j k l}, K_{i j k l}, e_{i j k}, e_{i j k}^{\prime}$ and $\varepsilon_{i j}$ are the phonon elastic constants, the phonon-phason coupling constants, the phason elastic constants, the phonon and phason piezoelectric constants, and the dielectric constants, respectively.

Here a non-constantly generally loaded strip crack of Griffith type is considered to be moving in its own plane with a uniform velocity within a homogeneous one-dimensional hexagonal piezoelectric quasicrystal with point group 6 mm.

A system of fixed rectangular Cartesian coordinates $(x, y, z)$ is chosen so that the material, which in its initial natural reference state has a uniform density, $\rho$, and is everywhere stress free and at rest, has the $x - y$ plane as its periodic plane and the positive $z$-axis as its direction of quasiperiodicity.

Within the material, the resulting components $\sigma_{XY}$, $\varepsilon_{XY}$ and $u_X$ of the phonon stress and strain tensors and displacement vector, $H_{zX}$, $w_{zX}$, and $w_X$ of the phason stress and strain tensors and displacement vector, and $D_X$ and $E_X$ of the electric displacement and field vectors, for $X$ and $Y = x, y$ or $z$, are then interrelated through constitutive equations having the matrix forms

$$
\left[\begin{array}{c}
\sigma_{x x} \\
\sigma_{y y} \\
\sigma_{z z} \\
\sigma_{y z} \\
\sigma_{x z} \\
\sigma_{x y} \\
H_{z z} \\
H_{z x} \\
H_{z y}
\end{array}\right]=\left[\begin{array}{ccccccccc}
c_{11} & c_{12} & c_{13} & 0 & 0 & 0 & R_{1} & 0 & 0 \\
c_{12} & c_{11} & c_{13} & 0 & 0 & 0 & R_{1} & 0 & 0 \\
c_{13} & c_{13} & c_{33} & 0 & 0 & 0 & R_{2} & 0 & 0 \\
0 & 0 & 0 & 2 c_{44} & 0 & 0 & 0 & 0 & R_{3} \\
0 & 0 & 0 & 0 & 2 c_{44} & 0 & 0 & R_{3} & 0 \\
0 & 0 & 0 & 0 & 0 & c_{11}-c_{12} & 0 & 0 & 0 \\
R_{1} & R_{1} & R_{2} & 0 & 0 & 0 & K_{1} & 0 & 0 \\
0 & 0 & 0 & 0 & 2 R_{3} & 0 & 0 & K_{2} & 0 \\
0 & 0 & 0 & 2 R_{3} & 0 & 0 & 0 & 0 & K_{2}
\end{array}\right]\left[\begin{array}{c}
\varepsilon_{x x} \\
\varepsilon_{y y} \\
\varepsilon_{z z} \\
\varepsilon_{y z} \\
\varepsilon_{x z} \\
\varepsilon_{x y} \\
w_{z z} \\
w_{z x} \\
w_{z y}
\end{array}\right]
$$

$$
-\left[\begin{array}{ccc}
0 & 0 & e_{31} \\
0 & 0 & e_{31} \\
0 & 0 & e_{33} \\
0 & e_{15} & 0 \\
e_{15} & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & e_{33}^{\prime} \\
e_{15}^{\prime} & 0 & 0 \\
0 & e_{15}^{\prime} & 0
\end{array}\right]\left[\begin{array}{c}
E_{x} \\
E_{y} \\
E_{z}
\end{array}\right],\qquad(5)
$$

$$
\left[\begin{array}{c}
D_{x} \\
D_{y} \\
D_{z}
\end{array}\right]=\left[\begin{array}{ccccccccc}
0 & 0 & 0 & 0 & 2 e_{15} & 0 & 0 & e_{15}^{\prime} & 0 \\
0 & 0 & 0 & 2 e_{15} & 0 & 0 & 0 & 0 & e_{15}^{\prime} \\
e_{31} & e_{31} & e_{33} & 0 & 0 & 0 & e_{33}^{\prime} & 0 & 0
\end{array}\right]\left[\begin{array}{c}
\varepsilon_{x x} \\
\varepsilon_{y y} \\
\varepsilon_{z z} \\
\varepsilon_{y z} \\
\varepsilon_{x z} \\
\varepsilon_{x y} \\
w_{z z} \\
w_{z x} \\
w_{z y}
\end{array}\right]
$$

$$
+\left[\begin{array}{ccc}
\varepsilon_{11} & 0 & 0 \\
0 & \varepsilon_{11} & 0 \\
0 & 0 & \varepsilon_{33}
\end{array}\right]\left[\begin{array}{c}
E_{x} \\
E_{y} \\
E_{z}
\end{array}\right],\qquad(6)
$$

with

$$
\varepsilon_{X Y}=\frac{1}{2}\left(\frac{\partial u_{X}}{\partial Y}+\frac{\partial u_{Y}}{\partial X}\right), \quad w_{z X}=\frac{\partial w_{z}}{\partial X}.\qquad(7)
$$

Utilizing the conventional contracted Voigt's notation with $i$ and $j$ taking integer values here, the elastic moduli in the phonon and phason fields are denoted by $c_{i j}$ and $K_{i}$, respectively, the phonon-phason coupling elastic moduli by $R_{i}$, the piezoelectric moduli by $e_{i j}$ and $e_{i j}^{\prime}$, and the dielectric moduli by $\varepsilon_{i j}$.

It is assumed that, at time $t$, the region $y=0, v t-c<x<v t+c,-\infty<z<\infty$ of the $x-z$ plane is occupied by a moving crack of width $2 c$ and constant speed of propagation $v$, as illustrated in Fig. 1, with a moving coordinate $\xi$ defined for convenience by

$$
\xi=x-v t.\qquad(8)
$$

An electric potential, $\phi$, can be defined such that the electric field vector, $\boldsymbol{E}$, can be written in terms of the electric potential, $\phi$, as

$$
\boldsymbol{E}=-\nabla \phi.\qquad(9)
$$

![](./images/811139273125265408_2.jpg)

Fig. 1 A loaded Griffith crack at time t, moving with uniform speed v in the x-direction

The application symmetrically to the two faces of the moving crack of non-constant phonon, phason and electrical loads subject to the boundary conditions
$$\sigma_{y z}(\xi, 0)=\mathcal{T}(\xi), \quad H_{z y}(\xi, 0)=\mathcal{H}(\xi), \quad D_{y}(\xi, 0)=\mathcal{D}(\xi), \quad \text { for }|\xi|<c,\qquad(10)$$
with the non-uniform functions $\mathcal{T}(\xi), \mathcal{H}(\xi)$ , and $\mathcal{D}(\xi)$ specified and the medium remaining undisturbed at infinity, induces a mode III antiplane deformation in which the field variables are all independent of $z$ .

Analyses corresponding to that below can be developed similarly by an interested reader for investigating antiplane deformations created by instead specifying on the crack faces whatever combinations involving any three of the components $\sigma_{y z}, \varepsilon_{y z}, H_{z y}, w_{z y}, D_{y}$ or $E_{y}$ are desired.

3 Moving piezoelectric quasicrystal screw dislocation

Before embarking upon a study of the fields around this moving mode III crack, it is desirable to outline the basic properties of a "piezoelectric quasicrystal screw dislocation" moving within the medium upon which the analysis is dependent.

This has an extended Burgers vector which is generalized from that of a conventional purely elastic screw dislocation by having finite discontinuities across its slip plane of magnitudes $b$ in the phonon displacement component $u_{z}, d$ in the phason displacement component $w_{z}$ , and $b_{4}$ (the strength of the charge dipole line) in the electric potential.

Expressions for the field quantities around such a dislocation have been presented by Wang and Pan [9]. In particular, for a screw dislocation line at the origin parallel to the z-axis moving along the x-axis with a speed $v$ in a one-dimensional hexagonal piezoelectric quasicrystal with point group $6 ~mm$ , it can be shown after appropriately renaming and regrouping various parameters and material moduli that
$$\begin{aligned}
u_{z}^{\mathrm{III}}(\xi, y)= & \frac{1}{2 \pi\left(\alpha^{2}+\bar{R}^{2}\right)}\left[b\left\{\alpha^{2} \tan ^{-1}\left(\frac{\beta_{1} y}{\xi}\right)+\bar{R}^{2} \tan ^{-1}\left(\frac{\beta_{2} y}{\xi}\right)\right\}\right. \\
& \left.+\mathrm{d} \alpha \bar{R}\left\{\tan ^{-1}\left(\frac{\beta_{1} y}{\xi}\right)-\tan ^{-1}\left(\frac{\beta_{2} y}{\xi}\right)\right\}\right],
\end{aligned}\qquad(11)$$

$$\begin{aligned}
w_{z}^{\mathrm{III}}(\xi, y)= & \frac{1}{2 \pi\left(\alpha^{2}+\bar{R}^{2}\right)}\left[b \alpha \bar{R}\left\{\tan ^{-1}\left(\frac{\beta_{1} y}{\xi}\right)-\tan ^{-1}\left(\frac{\beta_{2} y}{\xi}\right)\right\}\right. \\
& \left.+\mathrm{d}\left\{\bar{R}^{2} \tan ^{-1}\left(\frac{\beta_{1} y}{\xi}\right)+\alpha^{2} \tan ^{-1}\left(\frac{\beta_{2} y}{\xi}\right)\right\}\right],
\end{aligned}\qquad(12)$$

$$
\begin{aligned}
\phi^{\mathrm{III}}(\xi, y)= & \frac{1}{2 \pi}\left\{b \left[\frac { 1 } { \varepsilon _ { 1 1 } ( \alpha ^ { 2 } + \overline { R } ^ { 2 } ) } \left\{\alpha\left(e_{15} \alpha+e_{15}^{\prime} \overline{R}\right) \tan ^{-1}\left(\frac{\beta_{1} y}{\xi}\right)-\overline{R}\left(e_{15}^{\prime} \alpha-e_{15} \overline{R}\right) \tan ^{-1}\left(\frac{\beta_{2} y}{\xi}\right)\right\}\right.\right. \\
& \left.-\frac{e_{15}}{\varepsilon_{11}} \tan ^{-1}\left(\frac{y}{\xi}\right)\right] \\
& +\mathrm{d}\left[\frac { 1 } { \varepsilon _ { 1 1 } ( \alpha ^ { 2 } + \overline { R } ^ { 2 } ) } \left\{\overline{R}\left(e_{15} \alpha+e_{15}^{\prime} \overline{R}\right) \tan ^{-1}\left(\frac{\beta_{1} y}{\xi}\right)+\alpha\left(e_{15}^{\prime} \alpha-e_{15} \overline{R}\right) \tan ^{-1}\left(\frac{\beta_{2} y}{\xi}\right)\right\}\right. \\
& \left.\left.-\frac{e_{15}^{\prime}}{\varepsilon_{11}} \tan ^{-1}\left(\frac{y}{\xi}\right)\right]+b_{4} \tan ^{-1}\left(\frac{y}{\xi}\right)\right\},
\end{aligned}
$$

with throughout the superscript III indicating that the quantities are associated with a mode III deformation.
Here
$$
\alpha=\left\{\overline{c}_{44}-\overline{K}+\sqrt{\left(\overline{c}_{44}-\overline{K}\right)^{2}+4 \overline{R}^{2}}\right\} / 2,
$$

with the piezoelectrically stiffened elastic constants in the phonon and phason fields, $\overline{c}_{44}$ and $\overline{K}$, and the piezoelectrically stiffened phonon-phason coupling elastic constant, $\overline{R}$, respectively, given by
$$
\overline{c}_{44}=c_{44}+\frac{e_{15}^{2}}{\varepsilon_{11}}, \quad \overline{K}=K+\frac{e_{15}^{\prime 2}}{\varepsilon_{11}}, \quad \overline{R}=R+\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}},
$$

where the moduli $R_{3}$ and $K_{2}$ have been abbreviated to simply $R$ and $K$, respectively, throughout for ease of presentation, and
$$
\beta_{i}=\sqrt{1-\frac{v^{2}}{s_{i}^{2}}} \quad \text { for } i=1 \text { and } 2.
$$

The two piezoelectrically stiffened wave speeds, $s_{1}$ and $s_{2}$, under antiplane shear conditions are given by
$$
s_{i}=\sqrt{\varepsilon_{i} / \rho},
$$

with
$$
\varepsilon_{1}=\left\{\overline{c}_{44}+\overline{K}+\sqrt{\left(\overline{c}_{44}-\overline{K}\right)^{2}+4 \overline{R}^{2}}\right\} / 2, \quad \varepsilon_{2}=\left\{\overline{c}_{44}+\overline{K}-\sqrt{\left(\overline{c}_{44}-\overline{K}\right)^{2}+4 \overline{R}^{2}}\right\} / 2.
$$

The corresponding nonzero components of the phonon and phason stresses and electric displacement then follow, from Eqs. (11)-(13) using the constitutive equations (5) and (6), in the forms

$$
\begin{aligned}
\sigma_{x z}^{\mathrm{III}}(\xi, y)= & -\frac{y}{2 \pi}\left\{b \left[\frac { 1 } { ( \alpha ^ { 2 } + \overline { R } ^ { 2 } ) } \left\{\frac{\beta_{1} \alpha\left(\overline{c}_{44} \alpha+\overline{R}^{2}\right)}{\xi^{2}+\beta_{1}^{2} y^{2}}+\frac{\beta_{2} \overline{R}^{2}\left(\overline{c}_{44}-\alpha\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15}^{2}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]\right. \\
& \left.+\mathrm{d}\left[\frac{\overline{R}}{\left(\alpha^{2}+\overline{R}^{2}\right)}\left\{\frac{\beta_{1}\left(\overline{c}_{44} \alpha+\overline{R}^{2}\right)}{\xi^{2}+\beta_{1}^{2} y^{2}}-\frac{\beta_{2} \alpha\left(\overline{c}_{44}-\alpha\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]+b_{4} \frac{e_{15}}{\xi^{2}+y^{2}}\right\},
\end{aligned}
$$

$$
\begin{aligned}
\sigma_{y z}^{\mathrm{III}}(\xi, y)= & \frac{\xi}{2 \pi}\left\{b \left[\frac { 1 } { ( \alpha ^ { 2 } + \overline { R } ^ { 2 } ) } \left\{\frac{\beta_{1} \alpha\left(\overline{c}_{44} \alpha+\overline{R}^{2}\right)}{\xi^{2}+\beta_{1}^{2} y^{2}}+\frac{\beta_{2} \overline{R}^{2}\left(\overline{c}_{44}-\alpha\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15}^{2}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]\right. \\
& \left.+\mathrm{d}\left[\frac{\overline{R}}{\left(\alpha^{2}+\overline{R}^{2}\right)}\left\{\frac{\beta_{1}\left(\overline{c}_{44} \alpha+\overline{R}^{2}\right)}{\xi^{2}+\beta_{1}^{2} y^{2}}-\frac{\beta_{2} \alpha\left(\overline{c}_{44}-\alpha\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]+b_{4} \frac{e_{15}}{\xi^{2}+y^{2}}\right\},
\end{aligned}
$$

$$
H_{z x}^{\mathrm{III}}(\xi, y)=-\frac{y}{2 \pi}\left\{b\left[\frac{\overline{R}}{\left(\alpha^{2}+\overline{R}^{2}\right)}\left\{\frac{\beta_{1} \alpha(\alpha+\overline{K})}{\xi^{2}+\beta_{1}^{2} y^{2}}-\frac{\beta_{2}\left(\alpha \overline{K}-\overline{R}^{2}\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]\right.
$$

$$
+\mathrm{d}\left[\frac{1}{\left(\alpha^{2}+\overline{R}^{2}\right)}\left\{\frac{\beta_{1} \overline{R}^{2}(\alpha+\overline{K})}{\xi^{2}+\beta_{1}^{2} y^{2}}+\frac{\beta_{2} \alpha\left(\alpha \overline{K}-\overline{R}^{2}\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15}^{\prime 2}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]+b_{4} \frac{e_{15}^{\prime}}{\xi^{2}+y^{2}}
\biggr\},
\tag{21}
$$

$$
\begin{aligned}
H_{z y}^{\mathrm{III}}(\xi, y)= & \frac{\xi}{2 \pi}\left\{b\left[\frac{\bar{R}}{\left(\alpha^{2}+\bar{R}^{2}\right)}\left\{\frac{\beta_{1} \alpha(\alpha+\bar{K})}{\xi^{2}+\beta_{1}^{2} y^{2}}-\frac{\beta_{2}\left(\alpha \bar{K}-\bar{R}^{2}\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]\right. \\
& \left.+\mathrm{d}\left[\frac{1}{\left(\alpha^{2}+\bar{R}^{2}\right)}\left\{\frac{\beta_{1} \bar{R}^{2}(\alpha+\bar{K})}{\xi^{2}+\beta_{1}^{2} y^{2}}+\frac{\beta_{2} \alpha\left(\alpha \bar{K}-\bar{R}^{2}\right)}{\xi^{2}+\beta_{2}^{2} y^{2}}\right\}-\frac{e_{15}^{\prime 2}}{\varepsilon_{11}\left(\xi^{2}+y^{2}\right)}\right]+b_{4} \frac{e_{15}^{\prime}}{\xi^{2}+y^{2}}\right\},
\end{aligned}
\tag{22}
$$

$$
D_{x}^{\mathrm{III}}(\xi, y)=-\frac{y}{2 \pi} \frac{b e_{15}+d e_{15}^{\prime}-b_{4} \varepsilon_{11}}{\xi^{2}+y^{2}},
\tag{23}
$$

$$
D_{y}^{\mathrm{III}}(\xi, y)=\frac{\xi}{2 \pi} \frac{b e_{15}+d e_{15}^{\prime}-b_{4} \varepsilon_{11}}{\xi^{2}+y^{2}}.
\tag{24}
$$

The corresponding phonon and phason strain and electric field components can be derived analogously from Eqs. (11)-(13), if required.

## 4 Moving shear crack

The classical "dislocation layer technique" depends upon the recognition that a loaded crack can be modelled as a planar continuous array of appropriate dislocations to which it is equivalent. It was originally implemented for studying cracks within isotropic elastic solids, as usefully summarized by, for example, Bilby and Eshelby [16] and Lardner [17]. But this fundamental concept is exploited and extended here for studying the mode III crack under consideration currently by distributing an arrangement of moving piezoelectric quasicrystal screw dislocations, throughout the region of the crack plane $|\xi|<c, y=0,-\infty<z<\infty$.

With the densities of the discontinuities in the phonon and phason displacement components and electric potential of the proposed dislocations denoted by $f(\xi), g(\xi)$, and $f_{4}(\xi)$, respectively, it follows from Eqs. (20), (22), and (24) that at a point on the $\xi$-axis the resulting components of the phonon and phason stresses and electric displacement are represented by

$$
\begin{aligned}
\sigma_{y z}(\xi, 0)= & \frac{b}{2 \pi}\left[\left\{\frac{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)}{\alpha^{2}+\bar{R}^{2}}\right\}-\frac{e_{15}^{2}}{\varepsilon_{11}}\right] \int_{-c}^{c} \frac{f\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime} \\
& +\frac{d}{2 \pi}\left[\frac{1}{\bar{R}}\left\{\frac{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)}{\alpha^{2}+\bar{R}^{2}}\right\}-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}}\right] \int_{-c}^{c} \frac{g\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime} \\
& +\frac{b_{4} e_{15}}{2 \pi} \int_{-c}^{c} \frac{f_{4}\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime},
\end{aligned}
\tag{25}
$$

$$
\begin{aligned}
H_{z y}(\xi, 0)= & \frac{b}{2 \pi}\left[\frac{1}{\bar{R}}\left\{\frac{\beta_{1} \alpha(\alpha+\bar{K})-\beta_{2}\left(\alpha \bar{K}-\bar{R}^{2}\right)}{\alpha^{2}+\bar{R}^{2}}\right\}-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}}\right] \int_{-c}^{c} \frac{f\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime} \\
& +\frac{d}{2 \pi}\left[\left\{\frac{\beta_{1} \bar{R}^{2}(\alpha+\bar{K})+\beta_{2} \alpha\left(\alpha \bar{K}-\bar{R}^{2}\right)}{\alpha^{2}+\bar{R}^{2}}\right\}-\frac{e_{15}^{\prime 2}}{\varepsilon_{11}}\right] \int_{-c}^{c} \frac{g\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime} \\
& +\frac{b_{4} e_{15}^{\prime}}{2 \pi} \int_{-c}^{c} \frac{f_{4}\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime},
\end{aligned}
\tag{26}
$$

$$
D_{y}(\xi, 0)=\frac{b e_{15}}{2 \pi} \int_{-c}^{c} \frac{f\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime}+\frac{d e_{15}^{\prime}}{2 \pi} \int_{-c}^{c} \frac{g\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime}-\frac{b_{4} \varepsilon_{11}}{2 \pi} \int_{-c}^{c} \frac{f_{4}\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime}.
\tag{27}
$$

The Plemelj formulae are used for the evaluation of the improper integrals in Eqs. (25)-(27) which are taken to have their Cauchy principal values. After extremely lengthy and intricate algebraic manipulation

and simplification, the solutions of the system of three simultaneous equations which is yielded by equating the designated boundary conditions (10) to the above expressions (25)–(27) can be derived in the concise forms

$$
\begin{aligned}
\int_{-c}^{c} \frac{f\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime}=& \frac{2 \pi}{b \beta_{1} \beta_{2} \varepsilon_{11}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)} \\
& \times\left[\varepsilon_{11}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\} \mathcal{T}(\xi)-\varepsilon_{11} \bar{R}\left\{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)\right\} \mathcal{H}(\xi)\right. \\
& \left.-\left[e_{15}^{\prime} \bar{R}\left\{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)\right\}-e_{15}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right] \mathcal{D}(\xi)\right], \\
\int_{-c}^{c} \frac{g\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime}=& \frac{2 \pi}{\mathrm{d} \beta_{1} \beta_{2} \varepsilon_{11}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)} \\
& \times\left[-\varepsilon_{11} \bar{R}\left\{\beta_{1} \alpha(\alpha+\overline{K})-\beta_{2}\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\} \mathcal{T}(\xi)+\varepsilon_{11}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\} \mathcal{H}(\xi)\right. \\
& \left.+\left[e_{15}^{\prime}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\}-e_{15} \bar{R}\left\{\beta_{1} \alpha(\alpha+\overline{K})-\beta_{2}\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right] \mathcal{D}(\xi)\right], \quad(29) \\
\int_{-c}^{c} \frac{f_{4}\left(\xi^{\prime}\right)}{\xi-\xi^{\prime}} d \xi^{\prime}=& \frac{2 \pi}{b_{4} \beta_{1} \beta_{2} \varepsilon_{11}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)} \\
& \times\left\{-\left[e_{15}^{\prime} \bar{R}\left\{\beta_{1} \alpha(\alpha+\overline{K})-\beta_{2}\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}-e_{15}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right] \mathcal{T}(\xi)\right. \\
& +\left[e_{15}^{\prime}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\}-e_{15} \bar{R}\left\{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)\right\}\right] \mathcal{H}(\xi) \\
& -\left[\beta_{1} \beta_{2}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)-\frac{e_{15}^{2}}{\varepsilon_{11}}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right. \\
& \left.\left.-\frac{e_{15}^{\prime 2}}{\varepsilon_{11}}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\}+\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}} \bar{R}\left(\beta_{1}\left\{\alpha(\alpha+\overline{K})+\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)\right\}\right.\right. \\
& \left.\left.\left.-\beta_{2}\left\{\alpha\left(\bar{c}_{44}-\alpha\right)+\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right)\right] \mathcal{D}(\xi)\right\}.
\end{aligned}
$$

The relative phonon and phason displacements and electric potential of the two crack faces are also restricted to be zero at $\xi= \pm c$, and the befitting solutions of the integral equations (28)-(30) for the densities can be deduced from the studies of Muskhelishvili [18] and Gakhov [19], for example, to be

$$
\begin{aligned}
f(\xi)=& \frac{2}{\pi b \beta_{1} \beta_{2} \varepsilon_{11}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)} \frac{1}{\left(c^{2}-\xi^{2}\right)^{\frac{1}{2}}} \int_{-c}^{c} \frac{\left(c^{2}-\xi^{\prime 2}\right)^{\frac{1}{2}}}{\xi^{\prime}-\xi} \\
& \times\left[\varepsilon_{11}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\} \mathcal{T}\left(\xi^{\prime}\right)-\varepsilon_{11} \bar{R}\left\{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)\right\} \mathcal{H}\left(\xi^{\prime}\right)\right. \\
& \left.-\left[e_{15}^{\prime} \bar{R}\left\{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)\right\}-e_{15}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right] \mathcal{D}\left(\xi^{\prime}\right)\right] d \xi^{\prime}, \quad(31) \\
g(\xi)=& \frac{2}{\pi \mathrm{d} \beta_{1} \beta_{2} \varepsilon_{11}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)} \frac{1}{\left(c^{2}-\xi^{2}\right)^{\frac{1}{2}}} \int_{-c}^{c} \frac{\left(c^{2}-\xi^{\prime 2}\right)^{\frac{1}{2}}}{\xi^{\prime}-\xi} \\
& \times\left[-\varepsilon_{11} \bar{R}\left\{\beta_{1} \alpha(\alpha+\overline{K})-\beta_{2}\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\} \mathcal{T}\left(\xi^{\prime}\right)+\varepsilon_{11}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\} \mathcal{H}\left(\xi^{\prime}\right),\right. \\
& \left.+\left[e_{15}^{\prime}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\}-e_{15} \bar{R}\left\{\beta_{1} \alpha(\alpha+\overline{K})-\beta_{2}\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right] \mathcal{D}\left(\xi^{\prime}\right)\right] d \xi^{\prime}, \quad(32) \\
f_{4}(\xi)=& \frac{2}{\pi b_{4} \beta_{1} \beta_{2} \varepsilon_{11}\left(\bar{c}_{44} \overline{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)} \frac{1}{\left(c^{2}-\xi^{2}\right)^{\frac{1}{2}}} \int_{-c}^{c} \frac{\left(c^{2}-\xi^{\prime 2}\right)^{\frac{1}{2}}}{\xi^{\prime}-\xi} \\
& \times\left\{-\left[e_{15}^{\prime} \bar{R}\left\{\beta_{1} \alpha(\alpha+\overline{K})-\beta_{2}\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}-e_{15}\left\{\beta_{1} \bar{R}^{2}(\alpha+\overline{K})+\beta_{2} \alpha\left(\alpha \overline{K}-\bar{R}^{2}\right)\right\}\right] \mathcal{T}\left(\xi^{\prime}\right)\right. \\
& +\left[e_{15}^{\prime}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\}-e_{15} \bar{R}\left\{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)\right\}\right] \mathcal{H}\left(\xi^{\prime}\right)
\end{aligned}
$$


$$
\begin{aligned}
& -\left[\beta_{1} \beta_{2}\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)\left(\alpha^{2}+\bar{R}^{2}\right)-\frac{e_{15}^{2}}{\varepsilon_{11}}\left\{\beta_{1} \bar{R}^{2}(\alpha+\bar{K})+\beta_{2} \alpha\left(\alpha \bar{K}-\bar{R}^{2}\right)\right\}\right. \\
& -\frac{e_{15}^{\prime 2}}{\varepsilon_{11}}\left\{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)+\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)\right\}+\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}} \bar{R}\left(\beta_{1}\left\{\alpha(\alpha+\bar{K})+\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)\right\}\right. \\
& \left.\left.-\beta_{2}\left\{\alpha\left(\bar{c}_{44}-\alpha\right)+\left(\alpha \bar{K}-\bar{R}^{2}\right)\right\}\right)\right] \mathcal{D}\left(\xi^{\prime}\right)\right\} d \xi^{\prime}.
\end{aligned}
$$

With expressions for the required densities, $f(\xi), g(\xi)$, and $f_{4}(\xi)$, now having been ascertained, all the components of the phonon, phason and electric fields which are of interest can be deduced as desired from Eqs. (19)-(24) and (31)-(33).

As an illustration, for example, it is inferred from Eq. (20) that
$$
\begin{aligned}
\sigma_{y z}(\xi, y)= & \frac{b}{2 \pi} \int_{-c}^{c}\left(\xi-\xi^{\prime \prime}\right)\left[\frac{1}{\left(\alpha^{2}+\bar{R}^{2}\right)}\left\{\frac{\beta_{1} \alpha\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)}{\left(\xi-\xi^{\prime \prime}\right)^{2}+\beta_{1}^{2} y^{2}}+\frac{\beta_{2} \bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)}{\left(\xi-\xi^{\prime \prime}\right)^{2}+\beta_{2}^{2} y^{2}}\right\}\right. \\
& \left.-\frac{e_{15}^{2}}{\varepsilon_{11}\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+y^{2}\right\}}\right] f\left(\xi^{\prime \prime}\right) d \xi^{\prime \prime} \\
& +\frac{d}{2 \pi} \int_{-c}^{c}\left(\xi-\xi^{\prime \prime}\right)\left[\frac{\bar{R}}{\left(\alpha^{2}+\bar{R}^{2}\right)}\left\{\frac{\beta_{1}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)}{\left(\xi-\xi^{\prime \prime}\right)^{2}+\beta_{1}^{2} y^{2}}-\frac{\beta_{2} \alpha\left(\bar{c}_{44}-\alpha\right)}{\left(\xi-\xi^{\prime \prime}\right)^{2}+\beta_{2}^{2} y^{2}}\right\}\right. \\
& \left.-\frac{e_{15} e_{15}^{\prime}}{\varepsilon_{11}\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+y^{2}\right\}}\right] g\left(\xi^{\prime \prime}\right) d \xi^{\prime \prime}+\frac{b_{4}}{2 \pi} \int_{-c}^{c}\left(\xi-\xi^{\prime \prime}\right) \frac{e_{15}}{\left(\xi-\xi^{\prime \prime}\right)^{2}+y^{2}} f_{4}\left(\xi^{\prime \prime}\right) d \xi^{\prime \prime}. \quad(34)
\end{aligned}
$$

Then, by directly substituting into this the representations (31)-(33) for the densities, it follows after much involved rearrangement and manipulation that this phonon stress component can be conveniently expressed as
$$
\begin{aligned}
\sigma_{y z}(\xi, y)= & \frac{1}{\pi^{2}} \int_{-c}^{c}\left(c^{2}-\xi^{\prime 2}\right)^{\frac{1}{2}}\left[\left\{\bar{\Lambda}_{1} \mathcal{T}\left(\xi^{\prime}\right)+\bar{\Lambda}_{3} \mathcal{H}\left(\xi^{\prime}\right)+\bar{\Lambda}_{5} \mathcal{D}\left(\xi^{\prime}\right)\right\} \int_{-c}^{c} \frac{\left(\xi-\xi^{\prime \prime}\right) d \xi^{\prime \prime}}{\left(c^{2}-\xi^{\prime \prime 2}\right)^{\frac{1}{2}}\left(\xi^{\prime}-\xi^{\prime \prime}\right)\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+\beta_{1}^{2} y^{2}\right\}}\right. \\
& +\left\{\bar{\Lambda}_{2} \mathcal{T}\left(\xi^{\prime}\right)-\bar{\Lambda}_{3} \mathcal{H}\left(\xi^{\prime}\right)+\bar{\Lambda}_{6} \mathcal{D}\left(\xi^{\prime}\right)\right\} \int_{-c}^{c} \frac{\left(\xi-\xi^{\prime \prime}\right) d \xi^{\prime \prime}}{\left(c^{2}-\xi^{\prime \prime 2}\right)^{\frac{1}{2}}\left(\xi^{\prime}-\xi^{\prime \prime}\right)\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+\beta_{2}^{2} y^{2}\right\}} \\
& \left.-\frac{e_{15}}{\varepsilon_{11}} \mathcal{D}\left(\xi^{\prime}\right) \int_{-c}^{c} \frac{\left(\xi-\xi^{\prime \prime}\right) d \xi^{\prime \prime}}{\left(c^{2}-\xi^{\prime \prime 2}\right)^{\frac{1}{2}}\left(\xi^{\prime}-\xi^{\prime \prime}\right)\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+y^{2}\right\}}\right] d \xi^{\prime},
\end{aligned}
$$

with the dimensionless constants $\bar{\Lambda}_{1}, \bar{\Lambda}_{2}, \bar{\Lambda}_{3}, \bar{\Lambda}_{5}$ and $\bar{\Lambda}_{6}$ given by
$$
\bar{\Lambda}_{1}=\frac{\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)\left(\alpha \bar{K}-\bar{R}^{2}\right)}{\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)}, \bar{\Lambda}_{2}=\frac{\bar{R}^{2}\left(\bar{c}_{44}-\alpha\right)(\alpha+\bar{K})}{\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)},\qquad(36)
$$

$$
\bar{\Lambda}_{3}=\frac{\bar{R}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)\left(\bar{c}_{44}-\alpha\right)}{\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)}, \bar{\Lambda}_{5}=\frac{\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)\left\{e_{15}^{\prime} \bar{R}\left(\bar{c}_{44}-\alpha\right)+e_{15}\left(\alpha \bar{K}-\bar{R}^{2}\right)\right\}}{\varepsilon_{11}\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)},\qquad(37)
$$

$$
\bar{\Lambda}_{6}=-\frac{\bar{R}\left(\bar{c}_{44}-\alpha\right)\left\{e_{15}^{\prime}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-e_{15} \bar{R}(\alpha+\bar{K})\right\}}{\varepsilon_{11}\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)}.\qquad(38)
$$

For future reference, it is appropriate to note at this stage that
$$
\bar{\Lambda}_{1}+\bar{\Lambda}_{2}=1, \quad \bar{\Lambda}_{5}+\bar{\Lambda}_{6}=\frac{e_{15}}{\varepsilon_{11}}.\qquad(39)
$$

To aid the clarity of presentation, it is beneficial to introduce the functions $\mathcal{F}_{k}^{F}(\theta_{k}), \mathcal{R}_{k}(\xi, y)$, and $\theta_{k}(\xi, y)$, which are defined for $k = \beta_{1}, \beta_{2}$, and 1, and $F = \mathcal{T}, \mathcal{H}$, and $\mathcal{D}$, by

$$
\mathcal{F}_{k}^{F}\left(\theta_{k}\right)=\frac{1}{\pi} \int_{-c}^{c} \frac{k y \cos \theta_{k}+\left(\xi-\xi^{\prime}\right) \sin \theta_{k}}{\mathcal{R}_{k}\left\{\left(\xi-\xi^{\prime}\right)^{2}+k^{2} y^{2}\right\}}\left(c^{2}-\xi^{\prime 2}\right)^{\frac{1}{2}} F\left(\xi^{\prime}\right) d \xi^{\prime},
\tag{40}
$$

$$
\mathcal{R}_{k} e^{i \theta_{k}}=\left\{c^{2}-(\xi+i k y)^{2}\right\}^{\frac{1}{2}},
\tag{41}
$$

where the square root function in Eq. (41) has branches that are determined with $\theta_{k}$ chosen to be zero for $|\xi| < c$, $y = 0+$ and elsewhere by analytic continuation. This enables Eq. (35) to be neatly written, using the result (A.2) in the "Appendix", as

$$
\begin{aligned}
\sigma_{y z}(\xi, y)=& \bar{\Lambda}_{1} \mathcal{F}_{\beta_{1}}^{\mathcal{T}}\left(\theta_{\beta_{1}}\right)+\bar{\Lambda}_{2} \mathcal{F}_{\beta_{2}}^{\mathcal{T}}\left(\theta_{\beta_{2}}\right)+\bar{\Lambda}_{3}\left\{\mathcal{F}_{\beta_{1}}^{\mathcal{H}}\left(\theta_{\beta_{1}}\right)-\mathcal{F}_{\beta_{2}}^{\mathcal{H}}\left(\theta_{\beta_{2}}\right)\right\} \\
&+\bar{\Lambda}_{5} \mathcal{F}_{\beta_{1}}^{\mathcal{D}}\left(\theta_{\beta_{1}}\right)+\bar{\Lambda}_{6} \mathcal{F}_{\beta_{2}}^{\mathcal{D}}\left(\theta_{\beta_{2}}\right)-\frac{e_{15}}{\varepsilon_{11}} \mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}\right).
\end{aligned}
\tag{42}
$$

Similar analyses for other components, using Eqs. (19) and (21)-(24) in conjunction with Eqs. (31)-(33), (A.1) and (A2), produce the expressions

$$
\begin{aligned}
H_{z y}(\xi, y)=& \bar{\Lambda}_{4}\left\{\mathcal{F}_{\beta_{1}}^{\mathcal{T}}\left(\theta_{\beta_{1}}\right)-\mathcal{F}_{\beta_{2}}^{\mathcal{T}}\left(\theta_{\beta_{2}}\right)\right\}+\bar{\Lambda}_{2} \mathcal{F}_{\beta_{1}}^{\mathcal{H}}\left(\theta_{\beta_{1}}\right)+\bar{\Lambda}_{1} \mathcal{F}_{\beta_{2}}^{\mathcal{H}}\left(\theta_{\beta_{2}}\right) \\
&+\bar{\Lambda}_{7} \mathcal{F}_{\beta_{1}}^{\mathcal{D}}\left(\theta_{\beta_{1}}\right)+\bar{\Lambda}_{8} \mathcal{F}_{\beta_{2}}^{\mathcal{D}}\left(\theta_{\beta_{2}}\right)-\frac{e_{15}^{\prime}}{\varepsilon_{11}} \mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}\right),
\end{aligned}
\tag{43}
$$

$$
D_{y}(\xi, y)=\mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}\right),
\tag{44}
$$

$$
\begin{aligned}
\sigma_{x z}(\xi, y)=&-\frac{\bar{\Lambda}_{1}}{\beta_{1}} \mathcal{F}_{\beta_{1}}^{\mathcal{T}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)-\frac{\bar{\Lambda}_{2}}{\beta_{2}} \mathcal{F}_{\beta_{2}}^{\mathcal{T}}\left(\theta_{\beta_{2}}-\frac{\pi}{2}\right)-\bar{\Lambda}_{3}\left\{\frac{1}{\beta_{1}} F_{\beta_{1}}^{\mathcal{H}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)-\frac{1}{\beta_{2}} \mathcal{F}_{\beta_{2}}^{\mathcal{H}}\left(\theta_{\beta_{2}}-\frac{\pi}{2}\right)\right\} \\
&-\frac{\bar{\Lambda}_{5}}{\beta_{1}} \mathcal{F}_{\beta_{1}}^{\mathcal{D}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)-\frac{\bar{\Lambda}_{6}}{\beta_{2}} \mathcal{F}_{\beta_{2}}^{\mathcal{D}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)+\frac{e_{15}}{\varepsilon_{11}} \mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}-\frac{\pi}{2}\right),
\end{aligned}
\tag{45}
$$

$$
\begin{aligned}
H_{z x}(\xi, y)=&-\bar{\Lambda}_{4}\left\{\frac{1}{\beta_{1}} \mathcal{F}_{\beta_{1}}^{\mathcal{T}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)-\frac{1}{\beta_{2}} \mathcal{F}_{\beta_{2}}^{\mathcal{T}}\left(\theta_{\beta_{2}}-\frac{\pi}{2}\right)\right\}-\frac{\bar{\Lambda}_{2}}{\beta_{1}} \mathcal{F}_{\beta_{1}}^{\mathcal{H}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)-\frac{\bar{\Lambda}_{1}}{\beta_{2}} \mathcal{F}_{\beta_{2}}^{\mathcal{H}}\left(\theta_{\beta_{2}}-\frac{\pi}{2}\right) \\
&-\frac{\bar{\Lambda}_{7}}{\beta_{1}} \mathcal{F}_{\beta_{1}}^{\mathcal{D}}\left(\theta_{\beta_{1}}-\frac{\pi}{2}\right)-\frac{\bar{\Lambda}_{8}}{\beta_{2}} \mathcal{F}_{\beta_{2}}^{\mathcal{D}}\left(\theta_{\beta_{2}}-\frac{\pi}{2}\right)+\frac{e_{15}^{\prime}}{\varepsilon_{11}} \mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}-\frac{\pi}{2}\right),
\end{aligned}
\tag{46}
$$

$$
D_{x}(\xi, y)=-\mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}-\frac{\pi}{2}\right)
\tag{47}
$$

where

$$
\bar{\Lambda}_{4}=\frac{\bar{R}(\alpha+\bar{K})\left(\alpha \bar{K}-\bar{R}^{2}\right)}{\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)}, \quad \bar{\Lambda}_{7}=\frac{\bar{R}(\alpha+\bar{K})\left\{e_{15}^{\prime} \bar{R}\left(\bar{c}_{44}-\alpha\right)+e_{15}\left(\alpha \bar{K}-\bar{R}^{2}\right)\right\}}{\varepsilon_{11}\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)},
\tag{48}
$$

$$
\bar{\Lambda}_{8}=\frac{\left(\alpha \bar{K}-\bar{R}^{2}\right)\left\{e_{15}^{\prime}\left(\bar{c}_{44} \alpha+\bar{R}^{2}\right)-e_{15} \bar{R}(\alpha+\bar{K})\right\}}{\varepsilon_{11}\left(\alpha^{2}+\bar{R}^{2}\right)\left(\bar{c}_{44} \bar{K}-\bar{R}^{2}\right)},
\tag{49}
$$

and it is noted that

$$
\bar{\Lambda}_{7}+\bar{\Lambda}_{8}=\frac{e_{15}^{\prime}}{\varepsilon_{11}}.
\tag{50}
$$

It is relevant to observe here that Eqs. (42), (43), (45), and (46) indicate explicitly that, when the boundary conditions (10) are imposed, all the phonon and phason stress components depend upon $\mathcal{T}$, $\mathcal{H}$, and $\mathcal{D}$ together with the piezoelectric quasicrystal material constants and the speed of the crack, while it is clear from Eqs. (44) and (47) that the components of the electric displacement depend upon $\mathcal{D}$ and the crack speed only.

The distributions near a crack tip that are of interest practically of these components can be considered by putting

$$
\xi=c+r \cos \psi, \quad y=r \sin \psi
\tag{51}
$$

in terms of polar coordinates $r$ and $\psi$, into Eqs. (42)-(47) and studying cases where $r \ll c$. As $r \to 0$, it can be shown from Eq. (41) that approximately

$$
\mathcal{R}_{k} \sim \left\{ 2cr \left( \cos^{2} \psi + k^{2} \sin^{2} \psi \right)^{\frac{1}{2}} \right\}^{\frac{1}{2}}, \tag{52}
$$

$$
\theta_{k} \sim -(\pi - \Phi_{k})/2, \tag{53}
$$

with

$$
\Phi_{k} = \tan^{-1}(k \tan \psi) \tag{54}
$$

where $\tan^{-1}(\dots)$ indicates the principal value of the inverse tangent for $0 \leq \psi \leq \pi/2$ and $\pi$ plus the principal value for $\pi/2 \leq \psi \leq \pi$. Substitution of these into Eqs. (42)-(47) and (40), with the definition

$$
\Delta_{k} = \left( \cos^{2} \psi + k^{2} \sin^{2} \psi \right)^{\frac{1}{4}}, \tag{55}
$$

for $k = \beta_{1}, \beta_{2}$ and 1, yields

$$
\begin{aligned}
\sigma_{yz}(r, \psi) &\sim \frac{K_{\mathcal{T}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{1}}{\Delta_{\beta_{1}}} \cos \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{2}}{\Delta_{\beta_{2}}} \cos \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} + \frac{K_{\mathcal{H}}}{\sqrt{r}} \overline{\Lambda}_{3} \left\{ \frac{1}{\Delta_{\beta_{1}}} \cos \left( \frac{\Phi_{\beta_{1}}}{2} \right) - \frac{1}{\Delta_{\beta_{2}}} \cos \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} \\
&\quad + \frac{K_{\mathcal{D}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{5}}{\Delta_{\beta_{1}}} \cos \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{6}}{\Delta_{\beta_{2}}} \cos \left( \frac{\Phi_{\beta_{2}}}{2} \right) - \frac{e_{15}}{\varepsilon_{11}} \cos \left( \frac{\psi}{2} \right) \right\}, \tag{56}
\end{aligned}
$$

$$
\begin{aligned}
H_{zy}(r, \psi) &\sim \frac{K_{\mathcal{T}}}{\sqrt{r}} \overline{\Lambda}_{4} \left\{ \frac{1}{\Delta_{\beta_{1}}} \cos \left( \frac{\Phi_{\beta_{1}}}{2} \right) - \frac{1}{\Delta_{\beta_{2}}} \cos \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} + \frac{K_{\mathcal{H}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{2}}{\Delta_{\beta_{1}}} \cos \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{1}}{\Delta_{\beta_{2}}} \cos \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} \\
&\quad + \frac{K_{\mathcal{D}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{7}}{\Delta_{\beta_{1}}} \cos \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{8}}{\Delta_{\beta_{2}}} \cos \left( \frac{\Phi_{\beta_{2}}}{2} \right) - \frac{e_{15}'}{\varepsilon_{11}} \cos \left( \frac{\psi}{2} \right) \right\}, \tag{57}
\end{aligned}
$$

$$
D_{y}(r, \psi) \sim \frac{K_{\mathcal{D}}}{\sqrt{r}} \cos \left( \frac{\psi}{2} \right), \tag{58}
$$

$$
\begin{aligned}
\sigma_{xz}(r, \psi) &\sim -\frac{K_{\mathcal{T}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{1}}{\beta_{1} \Delta_{\beta_{1}}} \sin \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{2}}{\beta_{2} \Delta_{\beta_{2}}} \sin \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} \\
&\quad - \frac{K_{\mathcal{H}}}{\sqrt{r}} \overline{\Lambda}_{3} \left\{ \frac{1}{\beta_{1} \Delta_{\beta_{1}}} \sin \left( \frac{\Phi_{\beta_{1}}}{2} \right) - \frac{1}{\beta_{2} \Delta_{\beta_{2}}} \sin \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} \\
&\quad - \frac{K_{\mathcal{D}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{5}}{\beta_{1} \Delta_{\beta_{1}}} \sin \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{6}}{\beta_{2} \Delta_{\beta_{2}}} \sin \left( \frac{\Phi_{\beta_{2}}}{2} \right) - \frac{e_{15}}{\varepsilon_{11}} \sin \left( \frac{\psi}{2} \right) \right\}, \tag{59}
\end{aligned}
$$

$$
\begin{aligned}
H_{zx}(r, \psi) &\sim -\frac{K_{\mathcal{T}}}{\sqrt{r}} \overline{\Lambda}_{4} \left\{ \frac{1}{\beta_{1} \Delta_{\beta_{1}}} \sin \left( \frac{\Phi_{\beta_{1}}}{2} \right) - \frac{1}{\beta_{2} \Delta_{\beta_{2}}} \sin \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} \\
&\quad - \frac{K_{\mathcal{H}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{2}}{\beta_{1} \Delta_{\beta_{1}}} \sin \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{1}}{\beta_{2} \Delta_{\beta_{2}}} \sin \left( \frac{\Phi_{\beta_{2}}}{2} \right) \right\} \\
&\quad - \frac{K_{\mathcal{D}}}{\sqrt{r}} \left\{ \frac{\overline{\Lambda}_{7}}{\beta_{1} \Delta_{\beta_{1}}} \sin \left( \frac{\Phi_{\beta_{1}}}{2} \right) + \frac{\overline{\Lambda}_{8}}{\beta_{2} \Delta_{\beta_{2}}} \sin \left( \frac{\Phi_{\beta_{2}}}{2} \right) - \frac{e_{15}'}{\varepsilon_{11}} \sin \left( \frac{\psi}{2} \right) \right\}, \tag{60}
\end{aligned}
$$

$$
D_{x}(r, \psi) \sim -\frac{K_{\mathcal{D}}}{\sqrt{r}} \sin \left( \frac{\psi}{2} \right) \tag{61}
$$

as $r \to 0$, where the phonon and phason stress and electric displacement intensity factors, $K_{\mathcal{T}}$, $K_{\mathcal{H}}$, and $K_{\mathcal{D}}$, are defined for $F = \mathcal{T}, \mathcal{H}$, and $\mathcal{D}$ by

$$
K_{F} = -\frac{1}{\pi \sqrt{2c}} \int_{-c}^{c} \left( \frac{c + \xi'}{c - \xi'} \right)^{\frac{1}{2}} F(\xi') d\xi' \tag{62}
$$

![](./images/811139273125265408_3.jpg)

Fig. 2 Distribution of the scaled component of the phonon stress, $\sqrt{r}10^{5}\sigma_{\psi z}/K_{\mathcal{T}}$ around the crack tip for the scaled speeds $v/s_{2}=0$ and $v/s_{2}=0.99$

and correspond to that at the end of an isotropic elastic Griffith crack.

Finally, from Eqs. (56) and (59), (57), and (60), and (58) and (61), respectively, it follows that expressions near the crack tip for the components $\sigma_{\psi z}$ and $H_{z\psi}$ of the phonon and phason stress and $D_{\psi}$ of the electric displacement can be written in the forms

$$
\begin{aligned}
\sigma_{\psi z}(r, \psi) \sim & \frac{\bar{\Lambda}_{1} K_{\mathcal{T}}+\bar{\Lambda}_{3} K_{\mathcal{H}}+\bar{\Lambda}_{5} K_{\mathcal{D}}}{\sqrt{r} \Delta_{\beta_{1}}}\left\{\frac{1}{\beta_{1}} \sin \left(\frac{\Phi_{\beta_{1}}}{2}\right) \sin \psi+\cos \left(\frac{\Phi_{\beta_{1}}}{2}\right) \cos \psi\right\} \\
& +\frac{\bar{\Lambda}_{2} K_{\mathcal{T}}-\bar{\Lambda}_{3} K_{\mathcal{H}}+\bar{\Lambda}_{6} K_{\mathcal{D}}}{\sqrt{r} \Delta_{\beta_{2}}}\left\{\frac{1}{\beta_{2}} \sin \left(\frac{\Phi_{\beta_{2}}}{2}\right) \sin \psi+\cos \left(\frac{\Phi_{\beta_{2}}}{2}\right) \cos \psi\right\}-\frac{e_{15} K_{\mathcal{D}}}{\varepsilon_{11} \sqrt{r}} \cos \left(\frac{\psi}{2}\right),
\end{aligned}
\tag{63}
$$

$$
\begin{aligned}
H_{z \psi}(r, \psi) \sim & \frac{\bar{\Lambda}_{4} K_{\mathcal{T}}+\bar{\Lambda}_{2} K_{\mathcal{H}}+\bar{\Lambda}_{7} K_{\mathcal{D}}}{\sqrt{r} \Delta_{\beta_{1}}}\left\{\frac{1}{\beta_{1}} \sin \left(\frac{\Phi_{\beta_{1}}}{2}\right) \sin \psi+\cos \left(\frac{\Phi_{\beta_{1}}}{2}\right) \cos \psi\right\} \\
& -\frac{\bar{\Lambda}_{4} K_{\mathcal{T}}-\bar{\Lambda}_{1} K_{\mathcal{H}}-\bar{\Lambda}_{8} K_{\mathcal{D}}}{\sqrt{r} \Delta_{\beta_{2}}}\left\{\frac{1}{\beta_{2}} \sin \left(\frac{\Phi_{\beta_{2}}}{2}\right) \sin \psi+\cos \left(\frac{\Phi_{\beta_{2}}}{2}\right) \cos \psi\right\}-\frac{e_{15}^{\prime} K_{\mathcal{D}}}{\varepsilon_{11} \sqrt{r}} \cos \left(\frac{\psi}{2}\right),
\end{aligned}
\tag{64}
$$

$$
D_{\psi}(r, \psi) \sim \frac{K_{\mathcal{D}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right).
\tag{65}
$$

These indicate that, as in isotropic elastic materials, a $1/\sqrt{r}$ crack-tip behaviour governs all the field components and that their only dependence upon the non-uniform excitations, $\mathcal{T}(\xi), \mathcal{H}(\xi)$, and $\mathcal{D}(\xi)$, of the crack face is inherent upon the intensity factors introduced in Eq. (62).

For a material with specified piezoelectric quasicrystal moduli, it is interesting to remark that the sizes of the concentrated fields around the crack tip can be changed as required in a given practical situation by modifying any of the applied loads accordingly.

Agreement is attained with the corresponding results of Tupholme [20] for pure quasicrystals when the piezoelectric effects here are removed by putting $e_{15}=e_{15}^{\prime}=0$ throughout.

From Eqs. (31)-(33), it is evident that the above analysis is not valid when $\beta_{1}=0$ or $\beta_{2}=0$ or $\bar{c}_{44} \bar{K}-\bar{R}^{2}=$ 0 . From the definition (16), it follows that these particular values of $\beta_{1}$ and $\beta_{2}$ are achieved when the crack speed, $v$, reaches that of the two shear wave speeds, $s_{1}$ and $s_{2}$, given by Eq. (17).

There is a scarcity of reliable data for the values of the material moduli of piezoelectric quasicrystals, but representatively Li et al. [11] give $c_{44}=5.0 \times 10^{10} \mathrm{Nm}^{-2}, R=1.2 \times 10^{9} \mathrm{Nm}^{-2}, K=3.0 \times 10^{8} \mathrm{Nm}^{-2}$, $e_{15}=-0.138 \mathrm{Cm}^{-2}, e_{15}^{\prime}=-0.160 \mathrm{Cm}^{-2}, \varepsilon_{11}=82.6 \times 10^{-12} \mathrm{C}^{2} \mathrm{~N}^{-1} \mathrm{~m}^{-2}$. These, with typically $\rho=$ $5.1 \times 10^{3} \mathrm{~kg} \mathrm{~m}^{-3}$, yield the corresponding wave speeds to be $s_{1} \approx 3139 \mathrm{~ms}^{-1}$ and $s_{2} \approx 333 \mathrm{~ms}^{-1}$. Further, the product of $\bar{c}_{44}$ and $\bar{K}$ has a much larger magnitude than that of $\bar{R}^{2}$, and thus $\bar{c}_{44} \bar{K}-\bar{R}^{2}$ does not vanish.

Illustrative curves are depicted in Fig. 2 for the variation of the scaled component of the phonon stress, $\sqrt{r} 10^{5} \sigma_{\psi z} / K_{\mathcal{T}}$, with the angle $\psi$ around the crack tip for a representative electrically impermeable

crack with $\mathcal{H}(\xi)=\mathcal{D}(\xi)=0$. The corresponding numerical values of this scaled component can be cal- culated from Eq. (63), using the above data for the material constants when the crack speed, $v$, is such that $0 \leq v / s_{2}<1$. The graphs presented demonstrate that as $\psi$ increases from zero at a particular speed there is a decrease in the magnitude of the component of stress, with the decrease being smaller as the speed increases up to $v / s_{2}=0.99$ than that experienced around a stationary crack tip.

## 5 Stationary shear crack

No investigation of a stationary, non-uniformly loaded crack within a piezoelectric quasicrystal has been presented previously. It is therefore worthwhile to briefly exhibit the much simplified components of the fields which follow as a special case of the above analysis when $v=0$ throughout.

It is seen, from Eq. (16), that $\beta_{1}=\beta_{2}=1$ if $v=0$ and thus, by recalling from Eqs. (39) and (50) that $\bar{\Lambda}_{1}+\bar{\Lambda}_{2}=1, \bar{\Lambda}_{5}+\bar{\Lambda}_{6}=e_{15} / \varepsilon_{11}$ and $\bar{\Lambda}_{7}+\bar{\Lambda}_{8}=e_{15}^{\prime} / \varepsilon_{11}$, Eqs. (42)-(47) reduce for a stationary crack to

$$
\sigma_{y z}(x, y)=\mathcal{F}_{1}^{\mathcal{T}}\left(\theta_{1}\right), \quad H_{z y}(x, y)=\mathcal{F}_{1}^{\mathcal{H}}\left(\theta_{1}\right), \quad D_{y}(x, y)=\mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}\right),
\tag{66}
$$

$$
\sigma_{x z}(x, y)=-\mathcal{F}_{1}^{\mathcal{T}}\left(\theta_{1}-\frac{\pi}{2}\right), \quad H_{z x}(x, y)=-\mathcal{F}_{1}^{\mathcal{H}}\left(\theta_{1}-\frac{\pi}{2}\right), \quad D_{x}(x, y)=-\mathcal{F}_{1}^{\mathcal{D}}\left(\theta_{1}-\frac{\pi}{2}\right). \quad(67)
$$

Correspondingly, with $v=0$, Eqs. (56)-(61) yield that as $r \to 0$

$$
\sigma_{y z}(r, \psi) \sim \frac{K_{\mathcal{T}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right), H_{z y}(r, \psi) \sim \frac{K_{\mathcal{H}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right), D_{y}(r, \psi) \sim \frac{K_{\mathcal{D}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right),
\tag{68}
$$

$$
\sigma_{x z}(r, \psi) \sim-\frac{K_{\mathcal{T}}}{\sqrt{r}} \sin \left(\frac{\psi}{2}\right), H_{z x}(r, \psi) \sim-\frac{K_{\mathcal{H}}}{\sqrt{r}} \sin \left(\frac{\psi}{2}\right), D_{x}(r, \psi) \sim-\frac{K_{\mathcal{D}}}{\sqrt{r}} \sin \left(\frac{\psi}{2}\right),
\tag{69}
$$

and finally, from Eqs. (63)-(65),

$$
\sigma_{\psi z}(r, \psi) \sim \frac{K_{\mathcal{T}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right), H_{z \psi}(r, \psi) \sim \frac{K_{\mathcal{H}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right), D_{\psi}(r, \psi) \sim \frac{K_{\mathcal{D}}}{\sqrt{r}} \cos \left(\frac{\psi}{2}\right).
\tag{70}
$$

It is noteworthy from Eqs. (70) that for a stationary crack the stress component $\sigma_{\psi z}(r, \psi)$ depends upon the load $\mathcal{T}(x)$ alone and $H_{z \psi}(r, \psi)$ upon the load $\mathcal{H}(x)$ alone. This contrasts with the fields of a moving crack for which Eqs. (63) and (64) show that instead $\sigma_{\psi z}(r, \psi)$, and $H_{z \psi}(r, \psi)$ each depend upon $\mathcal{T}(\xi), \mathcal{H}(\xi)$, and $\mathcal{D}(\xi)$.

In the particular case, when the specified loads imposed on a stationary crack are pure constants, given by $\mathcal{T}(x)=T=$ constant, $\mathcal{H}(x)=H=$ constant, and $\mathcal{D}(x)=D=$ constant, the three intensity factors in Eq. (62) can be deduced to be simply

$$
K_{\mathcal{T}}=-\sqrt{\frac{c}{2}} T, \quad K_{\mathcal{H}}=-\sqrt{\frac{c}{2}} H, \quad K_{\mathcal{D}}=-\sqrt{\frac{c}{2}} D,
\tag{71}
$$

and thus the representations (68) become

$$
\sigma_{y z}(r, \psi) \sim-\sqrt{\frac{c}{2 r}} T \cos \left(\frac{\psi}{2}\right), H_{z y}(r, \psi) \sim-\sqrt{\frac{c}{2 r}} H \cos \left(\frac{\psi}{2}\right), D_{y}(r, \psi) \sim-\sqrt{\frac{c}{2 r}} D \cos \left(\frac{\psi}{2}\right).
\tag{72}
$$

This simplified specialized situation has been considered using a complex variable method by Yu et al. [12]. The results in Eq. (72) do indeed reproduce their solutions, with $-T,-H$, and $-D$ replaced by the remote loads $\sigma_{y z}^{\infty}, H_{z y}^{\infty}$ and $D_{y}^{\infty}$, respectively, which they impose.

## 6 Concluding remarks

The components of the phonon and phason stress and electric fields created within piezoelectric quasicrystals by a moving mode III Yoffe-like crack which is subjected to non-constant phason, phason, and electric loads are derived as analytical explicit expressions.

The focus of the analysis is upon using an appropriate adaptation of the classical technique of continuous dislocation layers to one-dimensional hexagonal piezoelectric quasicrystals.

Graphical illustrations of the variation in the component of the phonon stress with the angle around the tip of the crack are displayed for a range of crack speeds.

Finally, the main results of the analogous, simpler analysis of a stationary crack, which have not been presented previously, are derived.

## Appendix

It can be deduced using the methods of complex contour integration that

$$
\int_{-c}^{c} \frac{d \xi^{\prime \prime}}{\left(c^{2}-\xi^{\prime \prime 2}\right)^{\frac{1}{2}}\left(\xi^{\prime}-\xi^{\prime \prime}\right)\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+k^{2} y^{2}\right\}}=\frac{\pi\left\{k y \sin \Theta-\left(\xi-\xi^{\prime}\right) \cos \Theta\right\}}{y k \mathcal{R}\left\{\left(\xi-\xi^{\prime}\right)^{2}+k^{2} y^{2}\right\}}, \tag{A.1}
$$

$$
\int_{-c}^{c} \frac{\left(\xi-\xi^{\prime \prime}\right) d \xi^{\prime \prime}}{\left(c^{2}-\xi^{\prime \prime 2}\right)^{\frac{1}{2}}\left(\xi^{\prime}-\xi^{\prime \prime}\right)\left\{\left(\xi-\xi^{\prime \prime}\right)^{2}+k^{2} y^{2}\right\}}=\frac{\pi\left\{k y \cos \Theta+\left(\xi-\xi^{\prime}\right) \sin \Theta\right\}}{\mathcal{R}\left\{\left(\xi-\xi^{\prime}\right)^{2}+k^{2} y^{2}\right\}} \tag{A.2}
$$

for a constant $k$, where the branches of

$$
\mathcal{R} e^{i \Theta}=\left\{c^{2}-(\xi+i k y)^{2}\right\}^{\frac{1}{2}}
$$

are selected as for those in Eq. (52).

## References

1. Shechtman, D., Blech, I., Gratias, D., Cahn, J.W.: Metallic phase with long-range orientational order and no translational symmetry. Phys. Rev. Lett. **53**, 1951–1953 (1984)
2. Ding, D.H., Yang, W.G., Hu, C.Z., Wang, R.H.: Generalized elasticity theory of quasicrystals. Phys. Rev. B **48**, 7003–7009 (1993)
3. Fan, T.Y.: The Mathematical Theory of Elasticity of Quasicrystals and its Applications. Science Press/Springer, Bei-jing/Heidelberg (2011)
4. Fan, T.Y.: Mathematical theory and methods of mechanics of quasicrystalline materials. Engineering **5**, 407–448 (2013)
5. Zhou, X., Hu, C.-Z., Gong, P., Qiu, S.-D.: Piezoresistance properties of quasicrystals. J. Phys.: Condens. Matter **16**, 5419–5425 (2004)
6. Li, C.-L., Liu, Y.-Y.: The physical property tensors of one-dimensional quasicrystals. Chin. Phys. **13**, 924–931 (2004)
7. Rao, K.R.M., Rao, P.H., Chaitanya, B.S.K.: Piezoelectricity in quasicrystals: a group-theoretical study. Pramana J. Phys. **68**, 481–487 (2007)
8. Altay, G., Dökmeci, M.C.: On the fundamental equations of piezoelasticity of quasicrystal media. Int. J. Solids Struct. **49**, 3255–3262 (2012)
9. Wang, X., Pan, E.: Analytical solutions for some defect problems in 1D hexagonal and 2D octagonal quasicrystals. Pramana J. Phys. **70**, 911–933 (2008)
10. Yang, L.-Z., Gao, Y., Pan, E., Waksmanski, N.: Electric-elastic field induced by a straight dislocation in one-dimensional quasicrystals. Acta Phys. Polonica A **126**, 467–470 (2014)
11. Li, X.Y., Li, P.D., Wu, T.H., Shi, M.X., Zhu, Z.W.: Three-dimensional fundamental solutions for one-dimensional hexagonal quasicrystal with piezoelectric effect. Phys. Lett. A **378**, 826–834 (2014)
12. Yu, J., Guo, J., Pan, E., Xing, Y.: General solutions of plane problem in one-dimensional quasicrystal piezoelectric materials and its application on fracture mechanics. Appl. Math. Mech. **36**, 793–814 (2015)
13. Yu, J., Guo, J., Xing, Y.: Complex variable method for an anti-plane elliptical cavity of one-dimensional hexagonal piezoelectric quasicrystals. Chin. J. Aeronaut. **28**, 1287–1295 (2015)
14. Guo, J., Zhang, Z., Xing, Y.: Antiplane analysis for an elliptical inclusion in 1D hexagonal piezoelectric quasicrystal composites. Philos. Mag. **96**, 349–369 (2016)
15. Yang, J., Li, X.: Analytical solutions of problem about a circular hole with a straight crack in one-dimensional hexagonal quasicrystals with piezoelectric effects. Theor. Appl. Fract. Mech. **82**, 17–24 (2016)
16. Bilby, B.A., Eshelby, J.D.: Dislocations and the theory of fracture. In: Liebowitz, H. (ed.) Fracture, vol. 1, pp. 99–182. Academic Press, New York (1968)

17. Lardner, R.W.: Mathematical Theory of Dislocations and Fracture. University of Toronto Press, Toronto (1974)

18. Muskhelishvili, N.I.: Singular Integral Equations. Noordhoff Int. Pub, Leyden (1953)

19. Gakhov, F.D.: Boundary Value Problems. Pergamon, Oxford (1966)

20. Tupholme, G.E.: An antiplane shear crack moving in one-dimensional hexagonal qu quasicrystals. Int. J. Solids Struct. **71**, 255–261 (2015)