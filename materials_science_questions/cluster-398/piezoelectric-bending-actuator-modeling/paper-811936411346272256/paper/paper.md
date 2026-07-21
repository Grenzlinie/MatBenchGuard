![](./images/811936411346272256_1.jpg)

Available online at www.sciencedirect.com

![](./images/811936411346272256_2.jpg)

International Journal of Solids and Structures 45 (2008) 3313-3333

![](./images/811936411346272256_3.jpg)

# Electro-mechanical frictionless contact behavior of a functionally graded piezoelectric layered half-plane under a rigid punch

Liao-Liang Ke $^{a,b}$, Jie Yang $^{a,*}$, Sritawat Kitipornchai $^{a}$, Yue-Sheng Wang $^{b}$

$^{a}$ Department of Building and Construction, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong
$^{b}$ Institute of Engineering Mechanics, Beijing Jiaotong University, Beijing 100044, PR China

Received 15 November 2007; received in revised form 20 January 2008
Available online 9 February 2008

## Abstract

The frictionless contact problem of a functionally graded piezoelectric layered half-plane in-plane strain state under the action of a rigid flat or cylindrical punch is investigated in this paper. It is assumed that the punch is a perfect electrical conductor with a constant potential. The electro-elastic properties of the functionally graded piezoelectric materials (FGPMs) vary exponentially along the thickness direction. The problem is reduced to a pair of coupled Cauchy singular integral equations by using the Fourier integral transform technique and then is numerically solved to determine the contact pressure, surface electric charge distribution, normal stress and electric displacement fields. For a flat punch, the normal stress intensity factor and electric displacement intensity factor are also given to quantitatively characterize the singularity behavior at the punch ends. Numerical results show that both material property gradient of the FGPM layer and punch geometry have a significant influence on the contact performance of the FGPM layered half-plane.
© 2008 Elsevier Ltd. All rights reserved.

Keywords: Contact mechanics; Functionally graded piezoelectric materials; Frictionless; Conducting punch; Singular integral equation

## 1. Introduction

Functionally graded materials (FGMs) are inhomogeneous composites with both compositional profile and material properties varying smoothly and continuously so that the interface problem that usually occurs in homogeneous composites can be eliminated or alleviated (Suresh and Mortensen, 1998). Over the past 10 years, the contact mechanics of FGMs have received considerable research efforts (Giannakopoulos and Suresh, 1997a,b; Suresh, 2001; Guler and Erdogan, 2004, 2006, 2007; Ke and Wang, 2006, 2007a,b,c; Choi and Paulino, in press). These studies indicated that composite structures incorporated with FGMs, being

* Corresponding author. Tel.: +852 2194 2895; fax: +852 2788 7612.
E-mail address: jyang2@cityu.edu.hk (J. Yang).

0020-7683/$ - see front matter © 2008 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijsolstr.2008.01.028

appropriately designed, exhibit greatly improved resistance to surface contact deformation and damage compared with conventional homogeneous structures.

Piezoelectric devices may suffer from surface contact damage when subjected to a highly localized load exerted by a rigid body. Sosa and Castro (1994) presented analytical solutions of a piezoelectric half-plane subjected to a point force and a point charge by using state space approach and Fourier transform technique. Wang and Zheng (1995) and Ding et al. (2000) employed the potential function method to obtain the general solutions for the indentation of a piezoelectric half-space. Matysiak (1985) investigated the problem of pressing a rigid conducting punch into a piezoelectro-elastic half-space. Fan et al. (1996) studied the stress and electrical field distributions in a piezoelectric half-plane under a contact load through the Stroh's formalism. Giannakopoulos and Suresh (1999) presented a general theory for the axisymmetric indentation of transversely isotropic piezoelectric solids, and the results for different electrical boundary conditions involving conducting and insulting punches were obtained. Chen (1999, 2000) and Chen et al. (1999) conducted a series of investigation in the three-dimensional contact problems of piezoelectric materials. Saigal et al. (1999), Ramamurty et al. (1999) and Sridhar et al. (2000) investigated, theoretically or experimentally, the use of indentation technique to evaluate the electro-mechanical properties of piezoelectric composites. Based on a local/global stiffness matrix formulation, Guillermo and Paul (2003) and Guillermo (2006) dealt with the frictionless response contact of an arbitrarily multilayered piezoelectric half-plane indented by a rigid insulting punch. The axisymmetric contact problem of a circular indenter on a piezoelectric layer or half-space was solved by Wang and Han (2006) who considered both insulting and conducting punches in their work. Li and Wang (2006) investigated the Hertzian contact problem of anisotropic piezoelectric materials. The adhesive contact behavior of a piezoelectric half-space was analyzed by Chen and Yu (2005) and Rogowski and Kalinski (2007), respectively.

Recently, the concept of FGMs has been extended to the development of new piezoelectric materials named functionally graded piezoelectric materials (FGPMs) with graded microstructures and continuously varying electro-elastic properties (Zhu et al., 1999; Almajid et al., 2001). Quite a few studies on their electro-mechanical response under various loading conditions have been reported (Li and Weng, 2002; Yang et al., 2003, 2004, 2005; Chue and Ou, 2005; Pan and Han, 2005; Ueda, 2006, 2007; Yang and Xiang, 2007, among many others). However, no work has been done to address the contact problem of FGPMs.

This paper investigates the two-dimensional frictionless contact of a transversely isotropic FGPM layered half-plane under a rigid punch that may be flat and cylindrical in shape. It is assumed that the punch is a perfect electrical conductor with a constant potential. The present analysis employs Fourier integral transform technique to convert the governing equations into a pair of coupled Cauchy singular integral equations. The surface contact pressure, surface electric charge distribution, normal stress and electric displacement fields are obtained by numerically solving the integral equations. A comprehensive parametric study is conducted to highlight the effects of both the material property gradient and the punch geometry on the contact behavior of FGPM layered half-plane.

## 2. Fundamental solutions to an FGPM layered half-plane

Consider the problem shown in Fig. 1 where a normal concentrated line force $P$ and a positive concentrated line electric charge $Q$ act on the top surface of a functionally graded piezoelectric layer of thickness $h$ perfectly bonded to a transversely isotropic homogeneous piezoelectric half-plane with poling in the thickness direction. The $x$-axis is along the longitudinal direction at the interface while the $z$-axis is along the thickness direction and points upwards. To achieve a continuous change in the material properties so that the interfacial stress concentration due to property mismatch can be avoided, the elastic constants $c_{kl}(z)$, piezoelectric constants $e_{kl}(z)$ and dielectric constants $\varepsilon_{kk}(z)$ of the FGPM layer are designed to vary exponentially along the thickness direction as

$$
\left\{c_{k l}(z), e_{k l}(z), \varepsilon_{k k}(z)\right\}=\left\{c_{k l 0}, e_{k l 0}, \varepsilon_{k k 0}\right\} e^{\beta z}, \quad 0<z \leqslant h,\qquad(1)
$$

where $c_{kl0}$, $e_{kl0}$ and $\varepsilon_{kk0}$ are the electro-mechanical properties of both inhomogeneous FGPM upper layer and homogeneous piezoelectric half-plane at the interface $z=0$, the value of $\beta$ characterizes the material property

![](./images/811936411346272256_4.jpg)

Fig. 1. An FGPM layered half-plane subjected to a concentrated normal load $P$ and a positive concentrated electric charge $Q$.

gradient in the $z$-direction and $\beta=0$ corresponds to a special case where the upper layer is homogeneous as well.

It should be mentioned that piezoelectric composites do not always retain their crystal symmetry. This means that a 6 mm material may become a 4 mm one in some cases, depending on the exact location of the composite microstructure. Thus the simple rule of mixtures in Eq. (1) is no longer valid. These cases, however, are not considered in the present analysis.

### 2.1. General solutions for the FGPM layer

The constitutive equations for the transversely isotropic FGPM layer under plane strain state can be expressed in terms of displacement components $u_x$, $u_z$ and electric potential $\phi$ as

$$
\sigma_{x x 1}(x, z)=c_{11}(z) \frac{\partial u_{x 1}(x, z)}{\partial x}+c_{13}(z) \frac{\partial u_{z 1}(x, z)}{\partial z}+e_{31}(z) \frac{\partial \phi_{1}(x, z)}{\partial z},
\tag{2a}
$$

$$
\sigma_{z z 1}(x, z)=c_{13}(z) \frac{\partial u_{x 1}(x, z)}{\partial x}+c_{33}(z) \frac{\partial u_{z 1}(x, z)}{\partial z}+e_{33}(z) \frac{\partial \phi_{1}(x, z)}{\partial z},
\tag{2b}
$$

$$
\sigma_{z x 1}(x, z)=c_{44}(z)\left[\frac{\partial u_{x 1}(x, z)}{\partial z}+\frac{\partial u_{z 1}(x, z)}{\partial x}\right]+e_{15}(z) \frac{\partial \phi_{1}(x, z)}{\partial x},
\tag{2c}
$$

$$
D_{x 1}(x, z)=e_{15}(z)\left[\frac{\partial u_{x 1}(x, z)}{\partial z}+\frac{\partial u_{z 1}(x, z)}{\partial x}\right]-\varepsilon_{11}(z) \frac{\partial \phi_{1}(x, z)}{\partial x},
\tag{2d}
$$

$$
D_{z 1}(x, z)=e_{31}(z) \frac{\partial u_{x 1}(x, z)}{\partial x}+e_{33}(z) \frac{\partial u_{z 1}(x, z)}{\partial z}-\varepsilon_{33}(z) \frac{\partial \phi_{1}(x, z)}{\partial z},
\tag{2e}
$$

where $\sigma_{x x}$, $\sigma_{z z}$, $\sigma_{z x}$, $D_{x}$, $D_{z}$ are the stress and electric displacement components, respectively, and the FGPM layer is denoted by subscript " 1 ".

In the absence of body force and body charge, the equilibrium equation and Maxwell's equation are given as

$$
\frac{\partial \sigma_{x x 1}}{\partial x}+\frac{\partial \sigma_{z x 1}}{\partial z}=0, \quad \frac{\partial \sigma_{z x 1}}{\partial x}+\frac{\partial \sigma_{z z 1}}{\partial z}=0,
\tag{3a}
$$

$$
\frac{\partial D_{x 1}}{\partial x}+\frac{\partial D_{z 1}}{\partial z}=0.
\tag{3b}
$$

Substituting Eqs. (1) and (2) into Eq. (3) leads to the following governing equations

$$
\begin{aligned}
& c_{110} \frac{\partial u_{x 1}^{2}}{\partial x^{2}}+c_{440} \frac{\partial u_{x 1}^{2}}{\partial z^{2}}+\left(c_{130}+c_{440}\right) \frac{\partial u_{z 1}^{2}}{\partial x \partial z}+\left(e_{310}+e_{150}\right) \frac{\partial \phi_{1}^{2}}{\partial x \partial z}+\beta\left[c_{440}\left(\frac{\partial u_{x 1}}{\partial z}+\frac{\partial u_{z 1}}{\partial x}\right)+e_{150} \frac{\partial \phi_{1}}{\partial x}\right]=0, \quad(4 \mathrm{a}) \\
& c_{440} \frac{\partial u_{z 1}^{2}}{\partial x^{2}}+c_{330} \frac{\partial u_{z 1}^{2}}{\partial z^{2}}+\left(c_{130}+c_{440}\right) \frac{\partial u_{x 1}^{2}}{\partial x \partial z}+e_{150} \frac{\partial \phi_{1}^{2}}{\partial x^{2}}+e_{330} \frac{\partial \phi_{1}^{2}}{\partial z^{2}}+\beta\left(c_{130} \frac{\partial u_{x 1}}{\partial x}+c_{330} \frac{\partial u_{z 1}}{\partial z}+e_{330} \frac{\partial \phi_{1}}{\partial z}\right)=0, \quad(4 \mathrm{~b}) \\
& e_{150} \frac{\partial u_{z 1}^{2}}{\partial x^{2}}+e_{330} \frac{\partial u_{z 1}^{2}}{\partial z^{2}}+\left(e_{150}+e_{310}\right) \frac{\partial u_{x 1}^{2}}{\partial x \partial z}-\varepsilon_{110} \frac{\partial \phi_{1}^{2}}{\partial x^{2}}-\varepsilon_{330} \frac{\partial \phi_{1}^{2}}{\partial z^{2}}+\beta\left(e_{310} \frac{\partial u_{x 1}}{\partial x}+e_{330} \frac{\partial u_{z 1}}{\partial z}-\varepsilon_{330} \frac{\partial \phi_{1}}{\partial z}\right)=0 . \quad(4 \mathrm{c})
\end{aligned}
$$

Applying Fourier integral transform to Eq. (4) with respect to $x$ gives
$$
\begin{aligned}
& -c_{110} s^{2} \tilde{u}_{x 1}+c_{440} \tilde{u}_{x 1}^{\prime \prime}+\left(c_{130}+c_{440}\right) \mathrm{i} s \tilde{u}_{z 1}^{\prime}+\left(e_{310}+e_{150}\right) \mathrm{i} s \tilde{\phi}_{1}^{\prime}+\beta\left[c_{440}\left(\tilde{u}_{x 1}^{\prime}+\mathrm{i} s \tilde{u}_{z 1}\right)+e_{150} \mathrm{i} s \tilde{\phi}_{1}\right]=0, \quad(5 \mathrm{a}) \\
& -c_{440} s^{2} \tilde{u}_{z 1}+c_{330} \tilde{u}_{z 1}^{\prime \prime}+\left(c_{130}+c_{440}\right) \mathrm{i} s \tilde{u}_{x 1}^{\prime}-e_{150} s^{2} \tilde{\phi}_{1}+e_{330} \tilde{\phi}_{1}^{\prime \prime}+\beta\left(c_{130} \mathrm{i} s \tilde{u}_{x 1}+c_{330} \tilde{u}_{z 1}^{\prime}+e_{330} \tilde{\phi}_{1}^{\prime}\right)=0, \quad(5 \mathrm{~b}) \\
& -e_{150} s^{2} \tilde{u}_{z 1}+e_{330} \tilde{u}_{z 1}^{\prime \prime}+\left(e_{150}+e_{310}\right) \mathrm{i} s \tilde{u}_{x 1}^{\prime}+\varepsilon_{110} s^{2} \tilde{\phi}_{1}-\varepsilon_{330} \tilde{\phi}_{1}^{\prime \prime}+\beta\left(e_{310} \mathrm{i} s \tilde{u}_{x 1}+e_{330} \tilde{u}_{z 1}^{\prime}-\varepsilon_{330} \tilde{\phi}_{1}^{\prime}\right)=0, \quad(5 \mathrm{c})
\end{aligned}
$$
where a prime indicates the derivative with respective to $z$, and ' $\sim$ ' indicates the Fourier transform. The transformed displacement components and the electric potential are obtained by solving Eq. (5) as
$$
\left[\tilde{u}_{x 1}(s, z), \tilde{u}_{z 1}(s, z), \tilde{\phi}_{1}(s, z)\right]=\sum_{j=1}^{6}\left[1, a_{j}(s), b_{j}(s)\right] A_{j}(s) e^{n_{j} z},
$$
where $A_{j}(s)(j=1,2, \ldots, 6)$ are to be solved, and $n_{j}$ are the roots of a characteristic equation
$$
\operatorname{det}\left[\overline{G}_{i k}(s, n)\right]=0, \quad i, k=1,2,3,
$$
with
$$
\overline{G}_{i k}=\left[\begin{array}{ccc}
c_{440} n^{2}-c_{110} s^{2}+\beta c_{440} n & \left(c_{130}+c_{440}\right) \mathrm{i} n s+\beta c_{440} \mathrm{i} s & \left(e_{310}+e_{150}\right) \mathrm{i} n s+\beta e_{150} \mathrm{i} s \\
\left(c_{130}+c_{440}\right) \mathrm{i} n s+\beta c_{130} \mathrm{i} s & c_{330} n^{2}-c_{440} s^{2}+\beta c_{330} n & e_{330} n^{2}-e_{150} s^{2}+\beta e_{330} n \\
\left(e_{150}+e_{310}\right) \mathrm{i} n s+\beta e_{310} \mathrm{i} s & e_{330} n^{2}-e_{150} s^{2}+\beta e_{330} n & \varepsilon_{110} s^{2}-\varepsilon_{330} n^{2}-\beta \varepsilon_{330} n
\end{array}\right].
$$

This characteristic equation is bi-cubic with real coefficients and has two distinct real roots and four distinct complex roots (see Appendix A for details). Both $a_{j}(s)$ and $b_{j}(s)$ can be determined by
$$
a_{j}=\frac{\bar{g}_{21} \bar{g}_{13}-\bar{g}_{11} \bar{g}_{23}}{\bar{g}_{12} \bar{g}_{23}-\bar{g}_{13} \bar{g}_{22}}, \quad b_{j}=\frac{\bar{g}_{21} \bar{g}_{12}-\bar{g}_{11} \bar{g}_{22}}{\bar{g}_{13} \bar{g}_{22}-\bar{g}_{12} \bar{g}_{23}},
$$
where $\bar{g}_{m k}(m=1,2$ and $k=1,2,3)$ is the $m$ th row and $k$ th column element in matrix $\overline{G}_{i k}$.

Applying Fourier transform to Eq. (2) and substituting Eq. (6) into the resulting equation, the transformed displacement components, stress components, electric potential and electric displacement of the FGPM layer can be written in a matrix form as
$$
\left\{\tilde{u}_{x 1}(z, s), \tilde{u}_{z 1}(z, s), \tilde{\phi}_{1}(z, s), \tilde{\sigma}_{z z 1}(z, s), \tilde{\sigma}_{z x 1}(z, s), \tilde{D}_{z 1}(z, s)\right\}^{\mathrm{T}}=\left[T_{1}(z, s)\right]\{A(s)\},
$$
where
$$
\begin{aligned}
& \{A(s)\}=\left\{A_{1}(s), A_{2}(s), A_{3}(s), A_{4}(s), A_{5}(s), A_{6}(s)\right\}^{\mathrm{T}}, \\
& {\left[T_{1}(z, s)\right]=\left[T_{1 j}^{a}(z, s), T_{2 j}^{a}(z, s), T_{3 j}^{a}(z, s), T_{4 j}^{a}(z, s), T_{5 j}^{a}(z, s), T_{6 j}^{a}(z, s)\right]^{\mathrm{T}}, \quad j=1,2, \ldots, 6}
\end{aligned}
$$
with
$$
\begin{aligned}
& T_{1 j}^{a}(z, s)=e^{n_{j} z}, \quad T_{2 j}^{a}(z, s)=a_{j} e^{n_{j} z}, \quad T_{3 j}^{a}(z, s)=b_{j} e^{n_{j} z}, \\
& T_{4 j}^{a}(z, s)=\left[c_{130} \mathrm{i} s+c_{330} a_{j} n_{j}+e_{330} b_{j} n_{j}\right] e^{\left(n_{j}+\beta\right) z}, \\
& T_{5 j}^{a}(z, s)=\left[c_{440} n_{j}+c_{440} \mathrm{i} s a_{j}+e_{150} \mathrm{i} s b_{j}\right] e^{\left(n_{j}+\beta\right) z}, \\
& T_{6 j}^{a}(z, s)=\left[e_{310} \mathrm{i} s+e_{330} a_{j} n_{j}+\varepsilon_{330} b_{j} n_{j}\right] e^{\left(n_{j}+\beta\right) z}.
\end{aligned}
$$

The superscript "T" denotes the transposition of a matrix.

### 2.2. General solutions for the homogeneous piezoelectric half-plane

Similar to the solution process in Section 2.1, the transformed displacement components and electric potential for the homogeneous piezoelectric half-plane ($z<0$) that satisfy the conditions at infinity which require $u_{x2}, u_{z2}, \phi_2 \to 0$ as $\sqrt{x^2+z^2} \to \infty$ may be written as

$$
\left[\tilde{u}_{x 2}(s, z), \tilde{u}_{z 2}(s, z), \tilde{\phi}_{2}(s, z)\right]=\sum_{i=1}^{3}\left[1, c_{i}(s), d_{i}(s)\right] B_{i}(s) e^{m_{i} z},
\tag{10}
$$

where the subscript "2" indicates the piezoelectric half-plane, $B_i(s)$ ($i=1,2,3$) are unknown functions in $s$ that need to be solved, and $m_i$ are the roots with positive real part for the characteristic equation below

$$
\operatorname{det}\left[G_{i k}(s, m)\right]=0, \quad i, k=1,2,3,
\tag{11}
$$

where

$$
G_{i k}(s, m)=\left[\begin{array}{ccc}
c_{440} m^{2}-c_{110} s^{2} & \left(c_{130}+c_{440}\right) \mathrm{i} m s & \left(e_{310}+e_{150}\right) \mathrm{i} m s \\
\left(c_{130}+c_{440}\right) \mathrm{i} m s & c_{330} m^{2}-c_{440} s^{2} & e_{330} m^{2}-e_{150} s^{2} \\
\left(e_{150}+e_{310}\right) \mathrm{i} m s & e_{330} m^{2}-e_{150} s^{2} & \varepsilon_{110} s^{2}-\varepsilon_{330} m^{2}
\end{array}\right].
$$

$c_i(s)$ and $d_i(s)$ in Eq. (10) can be obtained by

$$
c_{i}=\frac{g_{21} g_{13}-g_{11} g_{23}}{g_{12} g_{23}-g_{13} g_{22}}, \quad d_{i}=\frac{g_{21} g_{12}-g_{11} g_{22}}{g_{13} g_{22}-g_{12} g_{23}},
\tag{12}
$$

where $g_{mk}$ ($m=1,2$ and $k=1,2,3$) is the $m$th row and $k$th column element in matrix $G_{ik}$.

The transformed displacement components, stress components, electric potential and electric displacement of the homogeneous piezoelectric half-plane can also be represented in a matrix form as

$$
\left\{\tilde{u}_{x 2}(z, s), \tilde{u}_{z 2}(z, s), \tilde{\phi}_{2}(z, s), \tilde{\sigma}_{z z 2}(z, s), \tilde{\sigma}_{z x 2}(z, s), \tilde{D}_{z 2}(z, s)\right\}^{\mathrm{T}}=\left[T_{2}(z, s)\right]\{B(s)\},
\tag{13}
$$

where
$$
\{B(s)\}=\left\{B_{1}(s), B_{2}(s), B_{3}(s)\right\}^{\mathrm{T}},
$$
$$
\left[T_{2}(z, s)\right]=\left[T_{1 i}^{b}(z, s), T_{2 i}^{b}(z, s), T_{3 i}^{b}(z, s), T_{4 i}^{b}(z, s), T_{5 i}^{b}(z, s), T_{6 i}^{b}(z, s)\right]^{\mathrm{T}}, \quad i=1,2,3
$$
and
$$
\begin{aligned}
& T_{1 i}^{b}(z, s)=e^{m_{i} z}, \quad T_{2 i}^{b}(z, s)=c_{i} e^{m_{i} z}, \quad T_{3 i}^{b}(z, s)=d_{i} e^{m_{i} z}, \\
& T_{4 i}^{b}(z, s)=\left[c_{130} \mathrm{i} s+c_{330} c_{i} m_{i}+e_{330} d_{i} m_{i}\right] e^{m_{i} z}, \\
& T_{5 i}^{b}(z, s)=\left[c_{440} m_{i}+c_{440} \mathrm{i} s c_{i}+e_{150} \mathrm{i} s d_{i}\right] e^{m_{i} z}, \\
& T_{6 i}^{b}(z, s)=\left[e_{310} \mathrm{i} s+e_{330} c_{i} m_{i}+\varepsilon_{330} d_{i} m_{i}\right] e^{m_{i} z}.
\end{aligned}
$$

### 2.3. Fundamental solutions

The unknown functions $A_j(s)$ ($j=1\ldots,6$) and $B_i(s)$ ($i=1,2,3$) in Eqs. (9) and (13) can be determined from the boundary conditions on the top surface $z=h$

$$
\sigma_{z z 1}(x, h)=-\delta(x) P,
\tag{14a}
$$
$$
\sigma_{z x 1}(x, h)=0,
\tag{14b}
$$
$$
D_{z 1}(x, h)=-\delta(x) Q,
\tag{14c}
$$

and interfacial continuity conditions at $z=0$

$$
u_{x 1}(x, 0)=u_{x 2}(x, 0), \quad u_{z 1}(x, 0)=u_{z 2}(x, 0),
\tag{15a}
$$

$$
\sigma_{z z 1}(x, 0)=\sigma_{z z 2}(x, 0), \quad \sigma_{z x 1}(x, 0)=\sigma_{z x 2}(x, 0),
\tag{15b}
$$

$$
D_{z 1}(x, 0)=D_{z 2}(x, 0), \quad \phi_{z 1}(x, 0)=\phi_{z 2}(x, 0),
\tag{15c}
$$

where $\delta(.)$ is the Dirac delta function. In the transformed domain, the above conditions can be re-expressed as

$$
\left[H_{1}\right]\left[T_{1}(h, s)\right]\{A\}=\{-P, 0,-Q\}^{\mathrm{T}},
\tag{16}
$$

$$
\left[T_{1}(0, s)\right]\{A\}=\left[T_{2}(0, s)\right]\{B\},
\tag{17}
$$

where

$$
\left[H_{1}\right]=\left[\begin{array}{llllll}
0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1
\end{array}\right].
$$

Eqs. (16) and (17) constitute a recursive relationship which, upon making use of Eqs. (9) and (13), yields the expressions of $\{A\}$ and $\{B\}$ in terms of $\{-P, 0,-Q\}^{\mathrm{T}}$

$$
\{A\}=[V]\left[V_{n}\right]^{-1}\{-P, 0,-Q\}^{\mathrm{T}},
\tag{18}
$$

$$
\{B\}=\left[V_{n}\right]^{-1}\{-P, 0,-Q\}^{\mathrm{T}},
\tag{19}
$$

where

$$
[V]=\left[T_{1}(0, s)\right]^{-1}\left[T_{2}(0, s)\right], \quad\left[V_{n}\right]=\left[H_{1}\right]\left[T_{1}(h, s)\right][V].
$$

Substituting (18) back into Eq. (9) and then taking inverse Fourier transform gives

$$
\left\{u_{x 1}(x, z), u_{z 1}(x, z), \phi_{1}(x, z), \sigma_{z z 1}(x, z), \sigma_{z x 1}(x, z), D_{z 1}(x, z)\right\}^{\mathrm{T}}=\frac{1}{2 \pi} \int_{-\infty}^{\infty}[M(s, z)]\{-P, 0,-Q\}^{\mathrm{T}} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s,
\tag{20}
$$

where $[M]$ is a $6 \times 3$ matrix defined by

$$
[M(s, z)]=\left[T_{1}(z, s)\right][V]\left[V_{n}\right]^{-1}.
$$

Extracting the displacement components and electric potential at $z=h$ from Eq. (20), we have

$$
\left\{u_{x 1}(x, h), u_{z 1}(x, h), \phi_{1}(x, h)\right\}^{\mathrm{T}}=\frac{1}{2 \pi} \int_{-\infty}^{\infty}[F(s, h)]\{-P, 0,-Q\}^{\mathrm{T}} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s,
\tag{21}
$$

where

$$
[F(s, h)]=\left[H_{2}\right][M(s, h)], \quad\left[H_{2}\right]=\left[\begin{array}{llllll}
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0
\end{array}\right].
$$

The above infinite integral is divergent because it does not vanish as the transform variable $s \rightarrow \pm \infty$. Consider the asymptotic behavior of matrix $[F(s, h)]$

$$
\lim _{s \rightarrow+\infty} s[F]=\left[\begin{array}{lll}
f_{11}^{\infty} & f_{12}^{\infty} & f_{13}^{\infty} \\
f_{21}^{\infty} & f_{22}^{\infty} & f_{23}^{\infty} \\
f_{31}^{\infty} & f_{32}^{\infty} & f_{33}^{\infty}
\end{array}\right],
$$

Eq. (21) can be rewritten as

$$
\begin{aligned}
\left\{u_{x 1}(x, h), u_{z 1}(x, h), \phi_{1}(x, h)\right\}^{\mathrm{T}}= & \frac{1}{2 \pi} \int_{-\infty}^{\infty}[\Pi]\{-P, 0,-Q\}^{\mathrm{T}} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s+\frac{1}{2 \pi} \int_{-\infty}^{\infty}\{[F]-[\Pi]\} \\
& \times\{-P, 0,-Q\}^{\mathrm{T}} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s,
\end{aligned}
\tag{22}
$$

where

$$
[I]=\frac{1}{s}\left[\begin{array}{ccc}
f_{11}^{\infty} & \operatorname{sign}(s) f_{12}^{\infty} & f_{13}^{\infty} \\
\operatorname{sign}(s) f_{21}^{\infty} & f_{22}^{\infty} & \operatorname{sign}(s) f_{23}^{\infty} \\
\operatorname{sign}(s) f_{31}^{\infty} & f_{32}^{\infty} & \operatorname{sign}(s) f_{33}^{\infty}
\end{array}\right].
$$

With the odd-even properties of matrix $[F(s)]$ in mind,

$$
F_{1 k}(-s)=(-1)^{k} F_{1 k}(s), \quad F_{2 k}(-s)=(-1)^{k+1} F_{2 k}(s), \quad F_{3 k}(-s)=(-1)^{k+1} F_{3 k}(s), \quad k=1,2,3,
\tag{23}
$$

and using the relation below

$$
\int_{0}^{\infty} \frac{\cos (s x)}{s} \mathrm{~d} s=-\ln |x|, \quad \int_{0}^{\infty} \frac{\sin (s x)}{s} \mathrm{~d} s=\frac{\pi}{2} \operatorname{sign}(x),
\tag{24}
$$

the displacement components and electric potential at the top surface, involving logarithmic singularity, can be obtained as

$$
\begin{aligned}
u_{x 1}(x, h)= & -\frac{\mathrm{i} f_{11}^{\infty} P}{2} \operatorname{sign}(x)-\frac{\mathrm{i} f_{13}^{\infty} Q}{2} \operatorname{sign}(x)-\frac{\mathrm{i} P}{\pi} \int_{0}^{\infty}\left(F_{11}-\frac{f_{11}^{\infty}}{s}\right) \sin (s x) \mathrm{d} s \\
& -\frac{\mathrm{i} Q}{\pi} \int_{0}^{\infty}\left(F_{13}-\frac{f_{13}^{\infty}}{s}\right) \sin (s x) \mathrm{d} s,
\end{aligned}
\tag{25}
$$

$$
\begin{aligned}
u_{z 1}(x, h)=\frac{f_{21}^{\infty} P}{\pi} \ln |x|+\frac{f_{23}^{\infty} Q}{\pi} \ln |x|-\frac{P}{\pi} \int_{0}^{\infty}\left(F_{21}-\frac{f_{21}^{\infty}}{s}\right) \cos (s x) \mathrm{d} s-\frac{Q}{\pi} \int_{0}^{\infty}\left(F_{23}-\frac{f_{23}^{\infty}}{s}\right) \cos (s x) \mathrm{d} s,
\end{aligned}
\tag{26}
$$

$$
\begin{aligned}
\phi_{1}(x, h)=\frac{f_{31}^{\infty} P}{\pi} \ln |x|+\frac{f_{33}^{\infty} Q}{\pi} \ln |x|-\frac{P}{\pi} \int_{0}^{\infty}\left(F_{31}-\frac{f_{31}^{\infty}}{s}\right) \cos (s x) \mathrm{d} s-\frac{Q}{\pi} \int_{0}^{\infty}\left(F_{33}-\frac{f_{33}^{\infty}}{s}\right) \cos (s x) \mathrm{d} s.
\end{aligned}
\tag{27}
$$

Note that the last two including the integrals in Eqs. (25)-(27) vanish when the upper layer is homogeneous (i.e. $\beta=0$) and the results by Sosa and Castro (1994) can readily be recovered. The infinite integrals in Eqs. (25)-(27) are convergent and can be easily evaluated by using numerical methods.

### 3. Punch problem for an FGPM layered half-plane

In this section, the fundamental solutions derived in Section 2 will be used to solve the contact problem of a rigid punch shown in Fig. 2 where the punch is a perfect conductor with a constant electric potential $\phi_{0}$, i.e. $\phi(x, h)=\phi_{0}$ within the contact region $-a \leqslant x \leqslant a$. This is a typical mixed boundary value problem in which the normal displacement component is known from the given punch profile within the contact region whereas the surface traction and normal electric displacement component are zero outside the contact region. Let $p(x)$ and $q(x)$ be the surface contact pressure and surface electric charge distribution within the contact region, respectively, and $\sigma_{z z 1}(x, h)=-p(x), D_{z 1}(x, h)=-q(x)$ (Giannakopoulos and Suresh, 1999). The superposition theorem gives the displacement components and electric potential of the surface

![](./images/811936411346272256_5.jpg)

Fig. 2. Frictionless contact between an FGPM layered half-plane and a conducting rigid punch.

$$
\begin{aligned}
u_{x 1}(x, h)= & -\frac{\mathrm{i} f_{11}^{\infty}}{2}\left[\int_{-a}^{x} p(t) \mathrm{d} t-\int_{x}^{a} p(t) \mathrm{d} t\right]-\frac{\mathrm{i} f_{13}^{\infty}}{2}\left[\int_{-a}^{x} q(t) \mathrm{d} t-\int_{x}^{a} q(t) \mathrm{d} t\right] \\
& -\frac{1}{\pi} \int_{-a}^{a} I_{1}(x, t) p(t) \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} I_{2}(x, t) q(t) \mathrm{d} t,
\end{aligned}
\tag{28}
$$

$$
\begin{aligned}
u_{z 1}(x, h)= & \frac{f_{21}^{\infty}}{\pi} \int_{-a}^{a} \ln |x-t| p(t) \mathrm{d} t+\frac{f_{23}^{\infty}}{\pi} \int_{-a}^{a} \ln |x-t| q(t) \mathrm{d} t \\
& -\frac{1}{\pi} \int_{-a}^{a} I_{3}(x, t) p(t) \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} I_{4}(x, t) q(t) \mathrm{d} t,
\end{aligned}
\tag{29}
$$

$$
\begin{aligned}
\phi_{1}(x, h)= & \frac{f_{31}^{\infty}}{\pi} \int_{-a}^{a} \ln |x-t| p(t) \mathrm{d} t+\frac{f_{33}^{\infty}}{\pi} \int_{-a}^{a} \ln |x-t| q(t) \mathrm{d} t \\
& -\frac{1}{\pi} \int_{-a}^{a} I_{5}(x, t) p(t) \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} I_{6}(x, t) q(t) \mathrm{d} t,
\end{aligned}
\tag{30}
$$

where

$$
\begin{aligned}
& I_{1}(x, t)=\mathrm{i} \int_{0}^{\infty}\left(F_{11}-\frac{f_{11}^{\infty}}{s}\right) \sin [s(x-t)] \mathrm{d} s, \quad I_{2}(x, t)=\mathrm{i} \int_{0}^{\infty}\left(F_{13}-\frac{f_{13}^{\infty}}{s}\right) \sin [s(x-t)] \mathrm{d} s, \\
& I_{3}(x, t)=\int_{0}^{\infty}\left(F_{21}-\frac{f_{21}^{\infty}}{s}\right) \cos [s(x-t)] \mathrm{d} s, \quad I_{4}(x, t)=\int_{0}^{\infty}\left(F_{23}-\frac{f_{23}^{\infty}}{s}\right) \cos [s(x-t)] \mathrm{d} s, \\
& I_{5}(x, t)=\int_{0}^{\infty}\left(F_{31}-\frac{f_{31}^{\infty}}{s}\right) \cos [s(x-t)] \mathrm{d} s, \quad I_{6}(x, t)=\int_{0}^{\infty}\left(F_{33}-\frac{f_{33}^{\infty}}{s}\right) \cos [s(x-t)] \mathrm{d} s.
\end{aligned}
$$

Differentiation of Eqs. (28)-(30) with respect to $x$ yields

$$
\theta_{1}(x)=-\mathrm{i} f_{11}^{\infty} p(x)-\mathrm{i} f_{13}^{\infty} q(x)-\frac{1}{\pi} \int_{-a}^{a} K_{1}(x, t) p(t) \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} K_{2}(x, t) q(t) \mathrm{d} t,
\tag{31}
$$

$$
\theta_{2}(x)=-\frac{f_{21}^{\infty}}{\pi} \int_{-a}^{a} \frac{p(t)}{t-x} \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} K_{3}(x, t) p(t) \mathrm{d} t-\frac{f_{23}^{\infty}}{\pi} \int_{-a}^{a} \frac{q(t)}{t-x} \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} K_{4}(x, t) q(t) \mathrm{d} t,
\tag{32}
$$

$$
\theta_{3}(x)=-\frac{f_{31}^{\infty}}{\pi} \int_{-a}^{a} \frac{p(t)}{t-x} \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} K_{5}(x, t) p(t) \mathrm{d} t-\frac{f_{33}^{\infty}}{\pi} \int_{-a}^{a} \frac{q(t)}{t-x} \mathrm{d} t-\frac{1}{\pi} \int_{-a}^{a} K_{6}(x, t) q(t) \mathrm{d} t,
\tag{33}
$$

where $-a \leqslant x \leqslant a$,

$$
\theta_{1}(x)=\frac{\partial u_{x 1}(x, h)}{\partial x}, \quad \theta_{2}(x)=\frac{\partial u_{z 1}(x, h)}{\partial x}, \quad \theta_{3}(x)=\frac{\partial \phi_{1}(x, h)}{\partial x}, \quad K_{j}(x, t)=\frac{\partial I_{j}(x, t)}{\partial x}, \quad j=1,2, \ldots, 6.
$$

Eqs. (31)-(33) are coupled Cauchy singular integral equations for the surface contact pressure $p(x)$ and surface electric charge distribution $q(x)$ provided that the profile and electric potential of the punch are prescribed. $K_{j}(x, t)$ is the generalized Fredholm integral kernel without singularity. In the following discussion, Eqs. (32) and (33) will be used to solve contact pressure and electric charge distribution for frictionless contact problem, and Eq. (31) will be used to solve the in-plane stress on the surface.

Note that the resultant force $P$ and total electric charge $Q$ are related with $p(x)$ and $q(x)$ by

$$
\int_{-a}^{a} p(t) \mathrm{d} t=P,
$$

$$
\int_{-a}^{a} q(t) \mathrm{d} t=Q.
$$

Introducing the following normalized quantities

$$
t=a \eta, \quad x=a \varsigma, \quad-a \leqslant(t, x) \leqslant a, \quad-1 \leqslant(\eta, \varsigma) \leqslant 1 .
$$

Eqs. (32)-(35) can be expressed in dimensionless form as

$$
-\frac{f_{21}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta-\frac{a}{\pi} \int_{-1}^{1} K_{3}(\varsigma, \eta) p(\eta) \mathrm{d} \eta-\frac{f_{23}^{\infty}}{\pi} \int_{-1}^{1} \frac{q(\eta)}{\eta-\varsigma} \mathrm{d} \eta-\frac{a}{\pi} \int_{-1}^{1} K_{4}(\varsigma, \eta) q(\eta) \mathrm{d} \eta=\theta_{1}(\varsigma),
$$

$$
-\frac{f_{31}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta-\frac{a}{\pi} \int_{-1}^{1} K_{5}(\varsigma, \eta) p(\eta) \mathrm{d} \eta-\frac{f_{33}^{\infty}}{\pi} \int_{-1}^{1} \frac{q(\eta)}{\eta-\varsigma} \mathrm{d} \eta-\frac{a}{\pi} \int_{-1}^{1} K_{6}(\varsigma, \eta) q(\eta) \mathrm{d} \eta=\theta_{2}(\varsigma),
$$

$$
\int_{-1}^{1} p(\eta) \mathrm{d} \eta=\frac{P}{a},
$$

$$
\int_{-1}^{1} q(\eta) \mathrm{d} \eta=\frac{Q}{a}.
$$

These equations will be solved numerically to find the contact pressure and electric charge distribution in the next section for two subset problems.

## 4. Examples

This section gives the numerical solutions of contact pressure distribution $p(x)$ and electric charge distribution $q(x)$ at the top surface when the FGPM layered half-plane is acted by a conducting rigid flat punch and a conducting rigid cylindrical punch.

### 4.1. A conducting rigid flat punch

We first consider the frictionless contact between an FGPM layered half-plane and a conducting flat punch shown in Fig. 3a. Because the indentation depth and electric potential are constant inside the contact region, one has

$$
\frac{\partial u_{z 1}(\varsigma, h)}{\partial \varsigma}=0, \quad \frac{\partial \phi_{1}(\varsigma, h)}{\partial \varsigma}=0,
$$

thus,

$$
\theta_{1}(\varsigma)=0, \quad \theta_{2}(\varsigma)=0 .
$$

For a flat punch with a constant electric potential, both the normal contact pressure $p(x)$ and electric charge distribution $q(x)$ exhibit square root singularity at the ends $\varsigma= \pm 1$ (Giannakopoulos and Suresh, 1999; Chen,

![](./images/811936411346272256_6.jpg)

Fig. 3. Frictionless contact problem between the FGPM layered half-plane and (a) a conducting flat punch; and (b) a conducting cylindrical punch.

2000; Wang and Han, 2006). With consideration of Eqs. (42), (37)-(40) are solved numerically by the method used by Erdogan and Gupta (1972). Express $p(\eta)$ and $q(\eta)$ in the form of

$$
p(\eta)=\frac{f_{1}(\eta)}{\sqrt{1-\eta^{2}}}, \quad q(\eta)=\frac{f_{2}(\eta)}{\sqrt{1-\eta^{2}}},
\tag{43}
$$

Eqs. (37)-(40) reduce to

$$
\frac{1}{N} \sum_{l=1}^{N}\left\{\left[\frac{f_{21}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{3}\left(\varsigma_{r}, \eta_{l}\right)\right] f_{1}\left(\eta_{l}\right)+\left[\frac{f_{23}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{4}\left(\varsigma_{r}, \eta_{l}\right)\right] f_{2}\left(\eta_{l}\right)\right\}=0,
\tag{44}
$$

$$
\frac{1}{N} \sum_{l=1}^{N}\left\{\left[\frac{f_{31}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{5}\left(\varsigma_{r}, \eta_{l}\right)\right] f_{1}\left(\eta_{l}\right)+\left[\frac{f_{33}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{6}\left(\varsigma_{r}, \eta_{l}\right)\right] f_{2}\left(\eta_{l}\right)\right\}=0,
\tag{45}
$$

$$
\frac{1}{N} \sum_{l=1}^{N} f_{1}\left(\eta_{l}\right)=\frac{P}{a \pi},
\tag{46}
$$

$$
\frac{1}{N} \sum_{l=1}^{N} f_{2}\left(\eta_{l}\right)=\frac{Q}{a \pi},
\tag{47}
$$

where $\eta_{l}=\cos [(2 l-1) \pi / 2 N], \varsigma_{r}=\cos [\pi r / N], r=1,2, \ldots, N-1$, and $N$ is the total number of the collocation points distributed over the range $(-1,1)$. Eqs. (44)-(47) provide $2 N$ equations from which $2 N$ unknowns $f_{1}$ $(\eta_{1}), \ldots, f_{1}(\eta_{N}), f_{2}(\eta_{1}), \ldots, f_{2}(\eta_{N})$ can be determined. The contact pressure and electric charge distribution at these points $p(\eta_{1}), \ldots, p(\eta_{N}), q(\eta_{1}), \ldots, q(\eta_{N})$ can subsequently be calculated.

The singularity of the contact pressure and electric displacement at the ends of the flat punch is quantita- tively characterized by stress intensity factor and electric displacement intensity factor as (Chen, 2000; Guler and Erdogan, 2004)

$$
K_{\sigma}(a)=\lim _{x \rightarrow a} \sqrt{2(a-x)} p(x)=\sqrt{a} f_{1}(1),
\tag{48}
$$

$$
K_{D}(a)=\lim _{x \rightarrow a} \sqrt{2(a-x)} q(x)=\sqrt{a} f_{2}(1).
\tag{49}
$$

### 4.2. A conducting rigid cylindrical punch

A cylindrical punch of radius $R$ is often approximated to be a parabolic punch of same radius of curvature at the center of the contact region, as shown in Fig. 3b. This approximation is adequate for a punch with a small value of $a / R$, which is the case considered in this paper. Let $\delta_{0}$ be the maximum indentation depth at $\varsigma=0$. The punch profile is given by

$$
u_{z 1}(\varsigma, h)=\delta_{0}-\frac{(a \varsigma)^{2}}{2 R}. \tag{50}
$$

Therefore, for a cylindrical punch with a constant electric potential, we have

$$
\frac{\partial u_{z 1}(\varsigma, h)}{\partial \varsigma}=-\frac{a \varsigma}{R}, \quad \frac{\partial \phi_{1}(\varsigma, h)}{\partial \varsigma}=0, \tag{51}
$$

and

$$
\theta_{1}(\varsigma)=-\frac{a \varsigma}{R}, \quad \theta_{2}(\varsigma)=0. \tag{52}
$$

It has been found (Giannakopoulos and Suresh, 1999) that for a conducting spherical punch with a constant potential, the contact pressure $p(\varsigma)$ is smooth at the ends $\varsigma=\pm 1$, while the electric charge distribution is the sum of two parts,

$$
q(\varsigma)=q_{1}(\varsigma)+q_{2}(\varsigma), \tag{53}
$$

where the first part $q_{1}(\varsigma)$ is induced by the normal load $P$ and is smooth at both ends $\varsigma=\pm 1$; the second part $q_{2}(\varsigma)$ is induced by the constant electric potential $\phi_{0}$ and has the square root singularity at both ends $\varsigma=\pm 1$. Following the work by Giannakopoulos and Suresh (1999) and taking into consideration of Eqs. (52) and (53), (37)-(40) may be written as

$$
\frac{f_{21}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{a}{\pi} \int_{-1}^{1} K_{3}(\varsigma, \eta) p(\eta) \mathrm{d} \eta+\frac{f_{23}^{\infty}}{\pi} \int_{-1}^{1} \frac{q_{1}(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{a}{\pi} \int_{-1}^{1} K_{4}(\varsigma, \eta) q_{1}(\eta) \mathrm{d} \eta=\frac{a \varsigma}{R}, \tag{54}
$$

$$
\frac{f_{31}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{a}{\pi} \int_{-1}^{1} K_{5}(\varsigma, \eta) p(\eta) \mathrm{d} \eta+\frac{f_{33}^{\infty}}{\pi} \int_{-1}^{1} \frac{q_{1}(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{a}{\pi} \int_{-1}^{1} K_{6}(\varsigma, \eta) q_{1}(\eta) \mathrm{d} \eta=0, \tag{55}
$$

$$
\int_{-1}^{1} p(\eta) \mathrm{d} \eta=\frac{P}{a}, \tag{56}
$$

$$
\int_{-1}^{1} q_{1}(\eta) \mathrm{d} \eta=\frac{Q_{1}}{a}, \tag{57}
$$

and

$$
\frac{f_{23}^{\infty}}{\pi} \int_{-1}^{1} \frac{q_{2}(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{a}{\pi} \int_{-1}^{1} K_{4}(\varsigma, \eta) q_{2}(\eta) \mathrm{d} \eta=0, \tag{58}
$$

$$
\int_{-1}^{1} q_{2}(\eta) \mathrm{d} \eta=\frac{Q-Q_{1}}{a}. \tag{59}
$$

where $Q_{1}$ is the electric charge due to the normal load $P$.

Eqs. (54)-(57) can be solved numerically by expressing $p(\eta)$ and $q_{1}(\eta)$ in the form of (Erdogan and Gupta, 1972)

$$
p(\eta)=f(\eta) \sqrt{1-\eta^{2}}, \quad q_{1}(\eta)=g_{1}(\eta) \sqrt{1-\eta^{2}}. \tag{60}
$$

Upon application of collocation method, Eqs. (54)-(57) become

$$
\sum_{l=1}^{N} \frac{\left(1-\eta_{l}^{2}\right)}{(N+1)}\left\{\left[\frac{f_{21}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{3}\left(\varsigma_{r}, \eta_{l}\right)\right] f\left(\eta_{l}\right)+\left[\frac{f_{23}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{4}\left(\varsigma_{r}, \eta_{l}\right)\right] g_{1}\left(\eta_{l}\right)\right\}=\frac{a \varsigma_{r}}{R},
$$

$$
\sum_{l=1}^{N} \frac{\left(1-\eta_{l}^{2}\right)}{(N+1)}\left\{\left[\frac{f_{31}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{5}\left(\varsigma_{r}, \eta_{l}\right)\right] f\left(\eta_{l}\right)+\left[\frac{f_{33}^{\infty}}{\eta_{l}-\varsigma_{r}}+a K_{6}\left(\varsigma_{r}, \eta_{l}\right)\right] g_{1}\left(\eta_{l}\right)\right\}=0,
$$

$$
\sum_{l=1}^{N} \frac{\left(1-\eta_{l}^{2}\right) f\left(\eta_{l}\right)}{(N+1)}=\frac{P}{a \pi},
$$

$$
\sum_{l=1}^{N} \frac{\left(1-\eta_{l}^{2}\right) g_{1}\left(\eta_{l}\right)}{(N+1)}=\frac{Q_{1}}{a \pi},
$$

where $\eta_{l}=\cos [l \pi /(N+1)], \varsigma_{r}=\cos [\pi(2 r-1) / 2(N+1)], \quad r=1,2, \ldots, N+1$. Obviously Eqs. (61)-(64) give $2 N+4$ equations for $2 N+2$ unknowns $\left(f\left(\eta_{1}\right), \ldots, f\left(\eta_{N}\right), g_{1}\left(\eta_{1}\right), \ldots, g_{1}\left(\eta_{N}\right), Q_{1}\right.$ and $\left.a\right)$. To solve this problem, $N$ is selected to be an even integer and two equations corresponding to $r=N / 2+1$ are ignored in the present analysis (Erdogan and Gupta, 1972). It should be pointed out that for the cylindrical punch the solution thus obtained automatically satisfies the consistency condition given by Muskhelishvili (1953).

Similarly, Eqs. (58) and (59) can also be solved numerically by expressing $q_{2}(\eta)$ as (Erdogan and Gupta, 1972)

$$
q_{2}(\eta)=\frac{g_{2}(\eta)}{\sqrt{1-\eta^{2}}}.
$$

Eqs. (58) and (59) are reduced to

$$
\frac{1}{N} \sum_{w=1}^{N}\left[\frac{f_{23}^{\infty}}{\eta_{w}-\varsigma_{t}}+a K_{4}\left(\varsigma_{t}, \eta_{w}\right)\right] g_{2}\left(\eta_{w}\right)=0,
$$

$$
\frac{1}{N} \sum_{w=1}^{N} g_{2}\left(\eta_{w}\right)=\frac{Q-Q_{1}}{a \pi},
$$

where $\eta_{w}=\cos [(2 w-1) \pi / 2 N], \varsigma_{t}=\cos [\pi t / N], t=1,2, \ldots, N-1$, and $N$ is the total number of the collocation points in $(-1,1)$. Eqs. (66) and (67) give $N$ equations to determine $g_{2}\left(\eta_{1}\right), \ldots, g_{2}\left(\eta_{N}\right)$.

After $f\left(\eta_{i}\right), g_{1}\left(\eta_{i}\right), g_{2}\left(\eta_{i}\right)$ have been obtained from Eqs. (61)-(67), the surface contact pressure and surface electric charge distribution at each point $p\left(\eta_{i}\right), q\left(\eta_{i}\right)(i=1, \ldots, N)$ can be calculated.

For both flat punch and cylindrical punch problems, once the normal contact stress $\sigma_{z z 1}(x, h)=-p(x)$ and electrical displacement $D_{z 1}(x, h)=-q(x)$ have been obtained, the in-plane stress $\sigma_{x x 1}(x, h)$ on the top surface of the FGPM layer can be determined from Eqs. (2) and (31) as

$$
\sigma_{x x 1}(x, h)=\left(\Delta_{0}-\mathrm{i} \Delta_{2} f_{11}^{\infty}\right) p(x)+\left(\Delta_{1}-\mathrm{i} \Delta_{2} f_{13}^{\infty}\right) q(x)-\frac{\Delta_{2}}{\pi} \int_{-a}^{a} K_{1}(x, t) p(t) \mathrm{d} t-\frac{\Delta_{2}}{\pi} \int_{-a}^{a} K_{2}(x, t) q(t) \mathrm{d} t,
$$

where
$$
\Delta_{0}=-\frac{c_{130} e_{330}+e_{310} e_{330}}{e_{330}^{2}+c_{330} \varepsilon_{330}}, \quad \Delta_{1}=-\frac{c_{130} e_{330}-c_{330} e_{310}}{e_{330}^{2}+c_{330} \varepsilon_{330}},
$$
$$
\Delta_{2}=\left[\frac{e_{310}\left(c_{330} e_{310}-c_{130} e_{330}\right)-c_{130}\left(c_{130} \varepsilon_{330}+e_{310} e_{330}\right)}{e_{330}^{2}+c_{330} \varepsilon_{330}}+c_{110}\right] e^{\beta h}.
$$

## 5. Numerical results and discussion

In what follows, it is assumed that the homogeneous piezoelectric half-plane is made of piezoceramic PZT-4 whose electro-mechanical properties are listed in Table 1 (Giannakopoulos and Suresh, 1999). The material properties of the FGPM layer vary exponentially as described in Eq. (1) such that both the piezoelectric half-plane and FGPM layer have the same material properties at the interface $z=0$. The exponential param-

<table><caption>Table 1
Material properties of PZT-4</caption>
<tbody>
<tr>
<td>
$c_{110}$ (GPa)
</td>
<td>
$c_{130}$ (GPa)
</td>
<td>
$c_{330}$ (GPa)
</td>
<td>
$c_{440}$ (GPa)
</td>
<td>
$e_{310}$ ($\text{C/m}^2$)
</td>
<td>
$e_{330}$ ($\text{C/m}^2$)
</td>
<td>
$e_{150}$ ($\text{C/m}^2$)
</td>
<td>
$\varepsilon_{110}$ (C/Vm)
</td>
<td>
$\varepsilon_{330}$ (C/Vm)
</td>
</tr>
<tr>
<td>
139
</td>
<td>
74.3
</td>
<td>
115
</td>
<td>
25.6
</td>
<td>
$-5.2$
</td>
<td>
15.1
</td>
<td>
12.7
</td>
<td>
$64.61\times 10^{-10}$
</td>
<td>
$56.2\times 10^{-10}$
</td>
</tr>
</tbody>
</table>

eter$\beta h$ is termed as gradient index and $\beta h=0$ is a special case in which the FGPM layer becomes homogeneous and the whole structure is made of piezoceramic PZT-4. Unless stated otherwise, the thickness of the FGPM layer is $h=0.01$ m, the radius of the rigid cylindrical punch is $R=0.08$ m while the half-length of the flat punch is $a=0.01$ m. A comprehensive parametric study is conducted to investigate the effects of gradient index and punch geometry on the frictionless contact behavior of the FGPM layered half-plane under a conducting rigid punch. Numerical results are presented in both tabular and graphical forms.

Figs. 4 and 5 show, respectively, the effect of gradient index $\beta h$ on the contact pressure and electric charge distribution on the top surface of the FGPM layered half-plane under a flat or a cylindrical punch with a concentrated load $P=1$ KN/m and an electric charge $Q=10^{-6}$ C/m. As can be expected, both the contact pressure and electric charge distribution show a typical square root singularity behavior at both ends $x=\pm a$ of

![](./images/811936411346272256_7.jpg)

Fig. 4. Effect of gradient parameter $\beta h$ on (a) surface contact pressure; and (b) surface electric charge distribution under a flat punch ($P=1$ KN/m, $Q=10^{-6}$ C/m).

![](./images/811936411346272256_8.jpg)

Fig. 5. Effect of gradient parameter $\beta h$ on (a) surface contact pressure; and (b) surface electric charge distribution under a cylindrical punch ($P=1$ KN/m, $Q=10^{-6}$ C/m and $a/h=0.00199$, $0.00244$, $0.00284$ when $R/h=0.4$, $0.6$, $0.8$).

the flat punch (Fig. 4). Under the cylindrical punch, the electric charge is singular at the edge of the contact region whereas the contact pressure is quite smooth (Fig. 5). This is quite similar to the results previously reported by Giannakopoulos and Suresh (1999), Chen (2000) and Wang and Han (2006) for the contact prob- lem of homogeneous piezoelectric materials. Note that $\beta h=0$ corresponds to a homogeneous piezoelectric half-plane. For this case, the close-form solutions of the flat and cylindrical punches are presented in Appendix B. With an increase in gradient index from $\beta h=-0.8$ to 0.8, the contact pressure and electric charge produced by the flat punch increase significantly in areas near two ends where concentration in stress and electric charge takes place. Those induced by the cylindrical punch increase as well but the contact region is considerably narrowed.

Fig. 6 presents the contact pressure and electric charge distributions on the top surface under a flat punch $(a=0.01 ~m)$ with different combinations of mechanical and electrical loads. The results of surface contact pressure at $P=1 KN / m, Q=10^{-6}, 8 \times 10^{-6}, 16 \times 10^{-6} C / m$ are plotted in Fig. 6a and the surface electric charge distributions at $Q=10^{-6} C / m, P=1,10,20 KN / m$ are displayed Fig. 6b. Results for the FGPM lay ered half-plane under a cylindrical punch $(R=0.08 ~m)$ are given in Fig. 7. In both figures, the gradient index is $\beta h=0.4$ . It is seen from Fig. 6 that under a flat punch, an increase in the applied electric charge $Q$ (the applied normal load $P$ ) on the punch lowers the contact pressure (electric charge) in almost the whole contact region

![](./images/811936411346272256_9.jpg)

Fig. 6. FGPM layered half-plane under a flat punch with various electro-mechanical loading: (a) surface contact pressure distribution; and(b) surface electric charge distribution.

![](./images/811936411346272256_10.jpg)

Fig. 7. FGPM layered half-plane under a cylindrical punch with various electro-mechanical loading: (a) surface contact pressure distribution; and (b) surface electric charge distribution.

![](./images/811936411346272256_11.jpg)

Fig. 8. Effect of gradient parameter $\beta h$ on the in-plane contact stress distribution under (a) a flat punch; and (b) a cylindrical punch ($P=1$ KN/m, $Q=10^{-6}$ C/m).

except the small areas near punch ends where the peak values of contact pressure (electric charge) are found. The contact pressure distribution is almost not affected by varying the applied electric charge $Q$ from $10^{-6}$ to $16\times 10^{-6}$ C/m with $P=1$ KN/m. The electric charge distribution in this case, however, is significantly influenced by the magnitude of normal force $P$ when the applied electric charge is fixed at $Q=10^{-6}$ C/m. As $P$ increases, not only the surface electric charge is decreased but the contact region is widened as well. At the same time, the electric charge distribution changes from a concave curve to a convex one.

In-plane normal stress $\sigma_{xx1}(x,h)$ on the top surface is important in terms of crack initiation. Figs. 8a and b present, respectively, the effect of gradient index $\beta h$ on the in-plane stress $\sigma_{xx1}(x,h)$ on the top surface of the FGPM layered half-plane under a flat or a cylindrical punch with a concentrated load $P=1$ KN/m and an electric charge $Q=10^{-6}$ C/m. It is observed that the in-plane stresses $\sigma_{xx1}(x,h)$ at both ends of the punches are tensile for $\beta h>0$, zero for the homogeneous piezoelectric half-plane ($\beta h=0$) and compressive for $\beta h<0$. Near the center of the contact region, the in-plane stresses for both flat and cylindrical punch are compressive and increase considerably as $\beta h$ varies from $-0.8$ to $0.8$. These results imply that the peak value of in-plane normal stress $\sigma_{xx1}(x,h)$ contact can be effectively lowered by using a smaller or negative $\beta h$.

As mentioned earlier, the contact pressure, electric charge and electric displacement on the top surface of the FGPM layered half-plane have high singularity at the ends of a flat punch. Table 2 lists the stress and electric displacement intensity factors at the end $x=a$ with different values of $\beta h$, normalized by $\sigma_{\sigma}\sqrt{a}$ and $\sigma_{D}\sqrt{a}$, respectively, where $\sigma_{\sigma}=P/a$ and $\sigma_{D}=Q/a$. Both the stress and electric displacement intensity factors tend to be higher as $\beta h$ changes from $-0.8$ to $0.8$, indicating that an increasing gradient index results in a higher singularity of the stress and electric displacement at the ends of a flat punch.

Tables 3 and 4 demonstrate the effect of gradient index $\beta h$ on the indentation depth $\delta_{0}$ and electric potential $\phi_{0}$ induced by a cylindrical punch with $P=1$ KN/m and $Q=10^{-6}$ C/m. Since it is impossible to calculate the absolute displacement and electric potential of a point on the top surface, relative indentation depth $\Delta\delta_{0}$ and relative electric potential $\Delta\phi_{0}$ are given in both tables which are defined as the difference

Table 2
Normalized stress intensity factor $K_{\sigma}(a)/\sigma_{a}\sqrt{a}$ and electric displacement intensity factor $K_{D}(a)/\sigma_{b}\sqrt{a}$ at the flat punch ends ($P=1$ KN/m, $Q=10^{-6}$ C/m, $a=0.001$ m)

<table>
<thead>
<tr>
<th>$\beta h$</th>
<th>$K_{\sigma}(a)/\sigma_{a}\sqrt{a}$</th>
<th>$K_{D}(a)/\sigma_{b}\sqrt{a}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$-0.8$</td>
<td>0.2368</td>
<td>0.2695</td>
</tr>
<tr>
<td>$-0.4$</td>
<td>0.2735</td>
<td>0.2919</td>
</tr>
<tr>
<td>$0.0$</td>
<td>0.3183</td>
<td>0.3183</td>
</tr>
<tr>
<td>$0.4$</td>
<td>0.3726</td>
<td>0.3493</td>
</tr>
<tr>
<td>$0.8$</td>
<td>0.4381</td>
<td>0.3856</td>
</tr>
</tbody>
</table>

Table 3
Relative indentation depth $\Delta \delta _{0}$ (cm) of an FGPM layered half-plane with varying $\beta h$ under a flat punch ($P=1\mathrm{KN/m}$, $Q=10^{-6}\mathrm{C/m}$)

<table><thead><tr><th>$\beta h$</th><th>$x_{0}=0.0$ m</th><th>$x_{0}=0.005$ m</th><th>$x_{0}=0.010$ m</th></tr></thead><tbody><tr><td>$-0.8$</td><td>$1.71\times 10^{-5}$</td><td>$2.16\times 10^{-6}$</td><td>$9.80\times 10^{-7}$</td></tr><tr><td>$-0.4$</td><td>$1.27\times 10^{-5}$</td><td>$1.98\times 10^{-6}$</td><td>$9.45\times 10^{-7}$</td></tr><tr><td>$0.0$</td><td>$9.72\times 10^{-6}$</td><td>$1.85\times 10^{-6}$</td><td>$9.28\times 10^{-7}$</td></tr><tr><td>$0.4$</td><td>$7.38\times 10^{-6}$</td><td>$1.71\times 10^{-6}$</td><td>$8.92\times 10^{-7}$</td></tr><tr><td>$0.8$</td><td>$5.63\times 10^{-6}$</td><td>$1.56\times 10^{-6}$</td><td>$8.43\times 10^{-7}$</td></tr></tbody></table>

Table 4
Relative electric potential $\Delta \phi _{0}$ (V) of an FGPM layered half-plane with varying $\beta h$ under a cylindrical punch ($P=1\ \mathrm{KN/m}$, $Q=10^{-6}\mathrm{C/m}$)

<table><thead><tr><th>$\beta h$</th><th>$x_{0}=0.0$ m</th><th>$x_{0}=0.005$ m</th><th>$x_{0}=0.010$ m</th></tr></thead><tbody><tr><td>$-0.8$</td><td>303.8</td><td>49.0</td><td>22.2</td></tr><tr><td>$-0.4$</td><td>223.3</td><td>39.9</td><td>19.0</td></tr><tr><td>$0.0$</td><td>160.0</td><td>31.9</td><td>15.9</td></tr><tr><td>$0.4$</td><td>117.1</td><td>25.9</td><td>13.5</td></tr><tr><td>$0.8$</td><td>86.4</td><td>21.2</td><td>11.5</td></tr></tbody></table>

Table 5
The roots of characteristic equation (7) when $s=1$

<table><thead><tr><th>$n$</th><th>$\beta =-40$</th><th>$\beta =0$</th><th>$\beta =40$</th></tr></thead><tbody><tr><td>$n_{1}$</td><td>40.020</td><td>1.204</td><td>0.0199</td></tr><tr><td>$n_{2}$</td><td>$-0.0199$</td><td>$-1.204$</td><td>$-40.020$</td></tr><tr><td>$n_{3}$</td><td>$40.070+1.164\mathrm{i}$</td><td>$1.069+0.200\mathrm{i}$</td><td>$0.0695+1.164\mathrm{i}$</td></tr><tr><td>$n_{4}$</td><td>$40.070-1.164\mathrm{i}$</td><td>$1.069-0.200\mathrm{i}$</td><td>$0.0695-1.164\mathrm{i}$</td></tr><tr><td>$n_{5}$</td><td>$-0.0695+1.164\mathrm{i}$</td><td>$-1.069+0.200\mathrm{i}$</td><td>$-40.070+1.164\mathrm{i}$</td></tr><tr><td>$n_{6}$</td><td>$-0.0695-1.164\mathrm{i}$</td><td>$-1.069-0.200\mathrm{i}$</td><td>$-40.070-1.164\mathrm{i}$</td></tr></tbody></table>

between the vertical surface displacement (electric potential) at point $x=x_{0}$ and that at reference point $x=0.02$ m, i.e. (see Table 5)

$$
\Delta \delta_{0}=u_{z 1}\left(x_{0}, 0.01\right)-u_{z 1}(0.02,0.01), \quad \Delta \phi_{0}=\phi_{1}\left(x_{0}, 0.01\right)-\phi_{1}(0.02,0.01).\tag{69}
$$

It is observed that both the relative indentation depth and electric potential can be greatly reduced by using a higher gradient index $\beta h$.

Quantitative electro-mechanical field analysis is very important in the design of smart structures. Once the surface contact pressure and electric charge distribution are found, the electro-mechanical fields within the FGPM layered half-plane can be determined. Fig. 9 presents the through-thickness distributions of normal stress $\sigma_{z z}$ and electric displacement $D_{z}$ at $x=0$ for an FGPM layered half-plane under a rigid flat punch, respectively. The normal load is $P=1\ \mathrm{KN/m}$ and the applied electric charge $Q=10^{-6}\mathrm{C/m}$. The normal stress $\sigma_{z z}$ reaches its maximum value at a position slightly below the loaded surface then decays very rapidly down to FGPM layered half-plane. However, the electric displacement $D_{z}$ is the maximal at the loaded top surface and decreases along the thickness direction. The maximum values of $\sigma_{z z}$ and $D_{z}$ are reduced as gradient index $\beta h$ increases.

The longitudinal distributions of normal stress $\sigma_{z z}$ and electric displacement $D_{z}$ at the interface $z=0$ when FGPM layered half-plane is subjected to a normal load $P=1\ \mathrm{KN/m}$ and applied electric charge $Q=10^{-6}\mathrm{C/}$ m is plotted in Fig. 10. Results show that both normal stress and electric displacement are symmetric about the $z$-axis and reach their maximum values at the center of the contact region ($x=0$). Compressive normal stress and negative electric displacement are induced at the interface over the region $-0.02\mathrm{m}\leqslant x\leqslant 0.02$ m by the given electro-mechanical loading. The use of a greater or positive gradient index $\beta h$ lowers the maximum values of $D_{z}$ and $\sigma_{z z}$, especially the former, at the interface.

![](./images/811936411346272256_12.jpg)

Fig. 9. Effect of gradient index $\beta$h on the through-thickness distribution of (a) normal stress $\sigma_{zz}$; and (b) electric displacement $D_{z}$ at $x=0.0$ m under a flat punch ($P=1$ KN/m, $Q=10^{-6}$ C/m).

![](./images/811936411346272256_13.jpg)

Fig. 10. Effect of gradient index $\beta$h on the longitudinal distribution of (a) normal stress $\sigma_{zz}$; and (b) electric displacement $D_{z}$ at $z=0.0$ m under a flat punch ($P=1$ KN/m, $Q=10^{-6}$ C/m).

The influence of punch geometry is also studied and the results are presented in Figs. 11 and 12 where the gradient index is $\beta h=0.4$, the normal load $P=1$ KN/m, and the applied electric charge $Q=10^{-6}$ C/m. It can be observed from Fig. 11 that as the half-width of a flat punch $a$ increases, both contact pressure and electric charge at the top surface, particularly the maximum values, are significantly decreased and more evenly distributed in the whole contact region, suggesting that using a wider flat punch can effectively suppress the normal stress and electric charge concentrations near the punch edges. The results for the system under a cylindrical punch with varying radius $R$ are given in Fig. 12. Similar to the observations in Fig. 11, it is found that the maximum contact pressure and electric charge are greatly lowered and the contact region becomes wider as the FGPM layered half-plane is loaded by a cylindrical punch with a larger radius.

## 6. Concluding remarks

Two-dimensional frictionless contact analysis of a functionally graded piezoelectric layered half-plane acted by a rigid conducting punch is presented in this paper. The electro-elastic properties of the FGPM layer are assumed to follow an exponential variation along the thickness direction. The contact pressure, normal stress, electric charge and electric displacement distributions on the top surface and within the FGPM layer are

![](./images/811936411346272256_14.jpg)

Fig. 11. Effect of flat punch width $a$ on the (a) surface contact pressure $p(x)$; and (b) surface electric charge distribution $q(x)$ ($P=1$ KN/m, $Q=10^{-6}$ C/m).

![](./images/811936411346272256_15.jpg)

Fig. 12. Effect of cylindrical punch radius $R$ on the (a) surface contact pressure $p(x)$; and (b) surface electric charge distribution $q(x)$ ($P=1$ KN/m, $Q=10^{-6}$ C/m and $a/h=0.00199, 0.00244, 0.00284$ when $R/h=4, 6, 8$).

obtained. It is found from the parametric study that the contact behavior of the FGPM layered half-plane is considerably influenced by both material property gradient and punch geometry. The results obtained in the present work provide very useful information in improving the resistance to contact damage and electricity induced failure at the contact surface of piezoelectric materials.

### Acknowledgements

This work described in this paper was fully funded by a research grant from the City University of Hong Kong (No. 7002079). The authors are grateful for this financial support.

### Appendix A

The characteristic equation (7) may be rewritten in the form of

$$
r_{6} n^{6}+r_{5} n^{5}+r_{4} n^{4}+r_{3} n^{3}+r_{2} n^{2}+r_{1} n+r_{0}=0, \tag{A1}
$$

where
$$r_{0}=\left(e_{150}^{2}+c_{440} \varepsilon_{110}\right)\left(c_{130} \beta^{2} s^{4}+c_{110} s^{6}\right),$$

$$
\begin{aligned}
r_{1}= & \beta s^{2}\left\{\beta^{2}\left[c_{330} e_{150} e_{310}-c_{130} e_{150} e_{330}-c_{440} e_{310} e_{330}-c_{130} c_{440} \varepsilon_{330}\right]+\left[c_{130}^{2} \varepsilon_{110}-c_{440} e_{310}^{2}\right.\right. \\
& \left.\left.-2 c_{110} e_{150} e_{330}-c_{110} c_{330} \varepsilon_{110}-c_{110} c_{440} \varepsilon_{330}+2 c_{130}\left(e_{150}^{2}+e_{150} e_{310}+c_{440} \varepsilon_{310}\right)\right] s^{2}\right\},
\end{aligned}
$$

$$
\begin{aligned}
r_{2}= & \beta^{2} s^{2}\left[c_{110} e_{330}^{2}-3 c_{130} e_{150} e_{330}-2 c_{130} e_{310} e_{330}-3 c_{440} e_{310} e_{330}-3 c_{130} c_{440} \varepsilon_{330}-c_{130}^{2} \varepsilon_{330}\right. \\
& \left.+c_{330}\left(e_{150}^{2}+3 e_{150} e_{310}+e_{310}^{2}+c_{440} \varepsilon_{110}+c_{110} \varepsilon_{330}\right)\right]+s^{4}\left[c_{130}^{2} \varepsilon_{110}-c_{440} e_{310}^{2}-2 c_{110} e_{150} e_{330}\right. \\
& \left.-c_{110} c_{330} \varepsilon_{110}-c_{110} c_{440} \varepsilon_{330}+2 c_{130}\left(e_{150}^{2}+e_{150} e_{310}+c_{440} \varepsilon_{110}\right)\right],
\end{aligned}
$$

$$
\begin{aligned}
r_{3}= & -\beta^{3} c_{440}\left(e_{330}^{2}+c_{330} \varepsilon_{330}\right)+2 \beta s^{2}\left[e_{330}\left(c_{110} e_{330}-2 c_{440} e_{310}\right)-c_{130}^{2} \varepsilon_{330}\right. \\
& \left.+c_{330}\left(e_{150}^{2}+2 e_{150} e_{310}+e_{310}^{2}+c_{440} \varepsilon_{110}+c_{110} \varepsilon_{330}\right)-2 c_{130}\left(e_{150} e_{330}+e_{310} e_{330}+c_{440} \varepsilon_{330}\right)\right],
\end{aligned}
$$

$$
\begin{aligned}
r_{4}= & -3 \beta^{2} c_{440}\left(e_{330}^{2}+c_{330} \varepsilon_{330}\right)+s^{2}\left[e_{330}\left(c_{110} e_{330}-2 c_{440} e_{310}\right)-c_{130}^{2} \varepsilon_{330}\right. \\
& \left.+c_{330}\left(e_{150}^{2}+2 e_{150} e_{310}+e_{310}^{2}+c_{440} \varepsilon_{110}+c_{110} \varepsilon_{330}\right)-2 c_{130}\left(e_{150} e_{330}+e_{310} e_{330}+c_{440} \varepsilon_{330}\right)\right],
\end{aligned}
$$

$$r_{5}=-3 \beta c_{440}\left(e_{330}^{2}+c_{330} \varepsilon_{330}\right),$$

$$r_{6}=-c_{440}\left(e_{330}^{2}+c_{330} \varepsilon_{330}\right).$$

When piezoceramic PZT-4 is used for the piezoelectric half-plane and the material of the FGPM layer at the interface $z=0$, this 6th-order nonlinear equation with real coefficients has two distinct real roots $(n_{1}$ and $n_{2})$ and four distinct complex roots $(n_{3}-n_{6})$. This has been verified in numerical calculations. These characteristic roots are given in Table 5 for different $\beta$ (1/m) values when $s=1$.

## Appendix B

For a flat punch on a homogeneous piezoelectric half-plane, the governing equations reduce to

$$
\frac{f_{21}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{f_{23}^{\infty}}{\pi} \int_{-1}^{1} \frac{q(\eta)}{\eta-\varsigma} \mathrm{d} \eta=0, \qquad (B1)
$$

$$
\frac{f_{31}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{f_{33}^{\infty}}{\pi} \int_{-1}^{1} \frac{q(\eta)}{\eta-\varsigma} \mathrm{d} \eta=0, \qquad (B2)
$$

$$
\int_{-1}^{1} p(\eta) \mathrm{d} \eta=\frac{P}{a}, \qquad (B3)
$$

$$
\int_{-1}^{1} q(\eta) \mathrm{d} \eta=\frac{Q}{a}. \qquad (B4)
$$

The close-form solutions of the contact pressure and electric charge distribution can be easily obtained as (Hills et al., 1993)

$$
p(\eta)=\frac{P}{a \pi \sqrt{1-\eta^{2}}}, \quad q(\eta)=\frac{Q}{a \pi \sqrt{1-\eta^{2}}}, \quad-1 \leqslant \eta \leqslant 1. \qquad (B5)
$$

For a cylindrical punch on a homogeneous piezoelectric half-plane, the governing equations can be written as

$$
\frac{f_{21}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{f_{23}^{\infty}}{\pi} \int_{-1}^{1} \frac{q_{1}(\eta)}{\eta-\varsigma} \mathrm{d} \eta=\frac{a \varsigma}{R},
\tag{B6}
$$

$$
\frac{f_{31}^{\infty}}{\pi} \int_{-1}^{1} \frac{p(\eta)}{\eta-\varsigma} \mathrm{d} \eta+\frac{f_{33}^{\infty}}{\pi} \int_{-1}^{1} \frac{q_{1}(\eta)}{\eta-\varsigma} \mathrm{d} \eta=0,
\tag{B7}
$$

$$
\int_{-1}^{1} p(\eta) \mathrm{d} \eta=\frac{P}{a},
\tag{B8}
$$

$$
\int_{-1}^{1} q_{1}(\eta) \mathrm{d} \eta=\frac{Q_{1}}{a},
\tag{B9}
$$

and

$$
\frac{f_{23}^{\infty}}{\pi} \int_{-1}^{1} \frac{q_{2}(\eta)}{\eta-\varsigma} \mathrm{d} \eta=0,
\tag{B10}
$$

$$
\int_{-1}^{1} q_{2}(\eta) \mathrm{d} \eta=\frac{Q-Q_{1}}{a}.
\tag{B11}
$$

The close-form solutions of the contact pressure and electric charge distribution can be obtained as (Hills et al., 1993)

$$
p(\eta)=p_{0} \sqrt{1-\eta^{2}}, \quad q_{1}(\eta)=q_{0} \sqrt{1-\eta^{2}}, \quad q_{2}(\eta)=\frac{Q-Q_{1}}{a \pi \sqrt{1-\eta^{2}}},
\tag{B12}
$$

where

$$
p_{0}=\frac{a}{A_{0} R}, \quad q_{0}=\frac{a}{A_{1} R}, \quad A_{0}=f_{21}^{\infty}-\frac{f_{23}^{\infty} f_{31}^{\infty}}{f_{33}^{\infty}}, \quad A_{1}=f_{23}^{\infty}-\frac{f_{21}^{\infty} f_{33}^{\infty}}{f_{31}^{\infty}}.
\tag{B13}
$$

Submitting (B12) into (B8) and (B9) yields the relations between contact region half-width $a$ and normal load $P$ and electric charge $Q_{1}$

$$
a^{2}=\frac{2 P A_{0} R}{\pi}=\frac{2 Q_{1} A_{1} R}{\pi}.
\tag{B14}
$$

### References
Almajid, A., Taya, M., Hudnut, S., 2001. Analysis of out-of-plane displacement and stress field in a piezocomposite plate with functionally graded microstructure. International Journal of Solids and Structures 38, 3377–3391.

Chen, W.Q., 1999. Inclined circular flat punch on a transversely isotropic piezoelectric half-space. Archives of Applied Mechanics 69, 455–464.

Chen, W.Q., 2000. On piezoelectric contact problem for a smooth punch. International Journal of Solids and Structures 37, 2331–2340.

Chen, W.Q., Shioya, T., Ding, H.J., 1999. The elasto-electric field for a rigid conical punch on a transversely isotropic piezoelectric half-space. Journal of Applied Mechanics 66, 764–771.

Chen, Z.R., Yu, S.W., 2005. Micro-scale adhesive contact of a spherical rigid punch on a piezoelectric half-space. Composites Science and Technology 65, 1372–1381.

Choi, H.J., Paulino, G.H., in press. Thermoelastic contact mechanics for a flat punch sliding over a graded coating/substrate system with frictional heat generation. Journal of the Mechanics and Physics of Solids.

Chue, C.H., Ou, Y.L., 2005. Mode III crack problems for two bonded functionally graded piezoelectric materials. International Journal of Solids and Structures 42, 3321–3337.

Ding, H.J., Hou, P.F., Gou, F.L., 2000. The elastic and electric fields for three-dimensional contact for transversely isotropic piezoelectric materials. International Journal of Solids and Structures 37, 3210–3229.

Erdogan, F., Gupta, G.D., 1972. On the numerical solution of singular integral equations. Quarterly Journal of Mechanics and Applied Mathematics 29, 525–534.

Fan, H., Sze, K.Y., Yang, W., 1996. Two-dimensional contact on a piezoelectric half-space. International Journal of Solids and Structures 33, 1305–1315.

Giannakopoulos, A.E., Suresh, S., 1997a. Indentation of solids with gradients in elastic properties: part I. Point force solution. International Journal of Solids and Structures 34, 2357–2392.

Giannakopoulos, A.E., Suresh, S., 1997b. Indentation of solids with gradients in elastic properties: part II. Axisymmetric indenters. International Journal of Solids and Structures 34, 2393-2428.

Giannakopoulos, A.E., Suresh, S., 1999. Theory of Indentation of piezoelectric materials. Acta Materialia 47, 2153-2164.

Guillermo, R., Paul, H., 2003. Frictionless contact in a layered piezoelectric half-space. Smart Materials and Structures 12, 612-625.

Guillermo, R., 2006. Frictionless contact in a layered piezoelectric media characterized by complex eigenvalues. Smart Materials and Structures 15, 1287-1295.

Guler, M.A., Erdogan, F., 2004. Contact mechanics of graded coatings. International Journal of Solids and Structures 41, 3865-3889.

Guler, M.A., Erdogan, F., 2006. Contact mechanics of two deformable elastic solids with graded coatings. Mechanics of Materials 38, 633-647.

Guler, M.A., Erdogan, F., 2007. The frictional sliding contact problems of rigid parabolic and cylindrical stamps on graded coatings. International Journal of Mechanical Sciences 49, 161-182.

Hills, D.A., Nowell, D., Sackfield, A., 1993. Mechanics of Elastic Contacts. Butterworth-Heinemann, Oxford.

Ke, L.L., Wang, Y.S., 2006. Two-dimensional contact mechanics of functionally graded materials with arbitrary spatial variations of material properties. International Journal of Solids and Structures 43, 5779-5798.

Ke, L.L., Wang, Y.S., 2007a. Two-dimensional sliding frictional contact of functionally graded materials. European Journal of Mechanics A/Solids 26, 171-188.

Ke, L.L., Wang, Y.S., 2007b. Fretting contact with finite friction of a functionally graded coating with arbitrarily varying elastic modulus. Part 1: normal loading. Journal of Strain Analysis for Engineering Design 42, 293-304.

Ke, L.L., Wang, Y.S., 2007c. Fretting contact with finite friction of a functionally graded coating with arbitrarily varying elastic modulus. Part 2: tangential loading. Journal of Strain Analysis for Engineering Design 42, 305-313.

Li, C., Weng, G.J., 2002. Antiplane crack problem in functionally graded piezoelectric materials. Journal of Applied Mechanics 69, 481-488.

Li, X.Y., Wang, M.Z., 2006. Hertzian contact of anisotropic piezoelectric bodies. Journal of Elasticity 84, 153-166.

Matysiak, S., 1985. Axisymmetric problem of punch pressing into a piezoelectro-elastic half space. Bulletin of the Polish Academy of Sciences 33, 25-34.

Muskhelishvili, N.I., 1953. Singular Integral Equations. Noordhoff, Leyden.

Pan, E., Han, F., 2005. Green's functions for transversely isotropic piezoelectric functionally graded multilayered half spaces. International Journal of Solids and Structures 42, 3207-3233.

Ramamurty, U., Sridhar, S., Giannakopoulos, A.E., Suresh, S., 1999. An experimental study of spherical indentation on piezoelectric materials. Acta Materialia 47, 2417-2430.

Rogowski, B., Kalinski, W., 2007. The adhesive contact problem for a piezoelectric half-space. International Journal of Pressure Vessels and Piping 84, 502-511.

Saigal, A., Giannakopoulos, A.E., Pettermann, H.E., Suresh, S., 1999. Electric response during indentation of a piezoelectric ceramic- polymer composite. Journal of Applied Physics 86, 603-606.

Sosa, H.A., Castro, M.A., 1994. On concentrated loads at the boundary of a piezoelectric half-plane. Journal of the Mechanics of Physics and Solids 42, 1105-1122.

Sridhar, S., Giannakopoulos, A.E., Suresh, S., 2000. Mechanical and electrical response of piezoelectric solids to conical indentation. Journal of Applied Physics 87, 8451-8456.

Suresh, S., 2001. Graded materials for resistance to contact deformation and damage. Science 292, 2447-2451.

Suresh, S., Mortensen, A., 1998. Fundamentals of functionally graded materials: processing and thermomechanical behavior of graded metals and metal-ceramic composites. IOM Communications Ltd., London.

Ueda, S., 2006. A finite crack in a semi-infinite strip of a grade piezoelectric material under electric loading. European Journal of Mechanics A/Solids 25, 250-259.

Ueda, S., 2007. A penny-shaped crack in a functionally graded piezoelectric strip under thermal loading. Engineering Fracture Mechanics 74, 1255-1273.

Wang, B.L., Han, J.C., 2006. A circular indenter on a piezoelectric layer. Archives of Applied Mechanics 76, 367-379.

Wang, Z.K., Zheng, B.L., 1995. The general solution of three-dimensional problem in piezoelectric media. International Journal of Solids and Structures 32, 105-115.

Yang, J., Kitipornchai, S., Liew, K.M., 2003. Large amplitude vibration of thermo-electro-mechanically stressed FGM laminated plates. Computer Methods in Applied Mechanics in Engineering 192, 3861-3892.

Yang, J., Kitipornchai, S., Liew, K.M., 2004. Non-linear analysis of the thermo-electric-mechanical behaviour of shear deformable FGM plates with piezoelectric actuators. International Journal for Numerical Methods in Engineering 59, 1605-1632.

Yang, J., Liew, K.M., Kitipornchai, S., 2005. Stochastic analysis of compositionally graded plates with system uncertainties under static loading. International Journal of Mechanical Sciences 47, 1519-1541.

Yang, J., Xiang, H.J., 2007. Thermo-electro-mechanical characteristics of functionally graded piezoelectric actuators. Smart Materials and Structures 16, 784-797.

Zhu, X.H., Zhu, J.M., Zhou, S.H., Li, Q., Liu, Z.G., 1999. Microstructures of the monomorph piezoelectric ceramic actuators with functionally gradient. Sensor and Actuators A - Physical 74, 198-202.