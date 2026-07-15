Accepted Manuscript

![](./images/843477285435604993_1.jpg)

Active vibration control of GPLs-reinforced FG metal foam plates with piezoelectric sensor and actuator layers

Nam V. Nguyen, Jaehong Lee, H. Nguyen-Xuan

PII:
S1359-8368(19)30734-6

DOI:
https://doi.org/10.1016/j.compositesb.2019.05.060

Reference:
JCOMB 6849

To appear in:
Composites Part B

Received Date: 20 February 2019

Revised Date: 4 April 2019

Accepted Date: 5 May 2019

Please cite this article as: Nguyen NV, Lee J, Nguyen-Xuan H, Active vibration control of GPLs-reinforced FG metal foam plates with piezoelectric sensor and actuator layers, Composites Part B (2019), doi: https://doi.org/10.1016/j.compositesb.2019.05.060.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

### Highlights

- Free vibration and dynamic responses of smart FG metal foam plates reinforced by graphene platelets (GPLs) are investigated.

- Active vibration control of plates through the integration of piezoelectric sensors and actuators is presented.

- A $C^0$-HSDT polygonal finite element formulation (PFEM) enhanced with quadratic serendipity shape functions is employed.

- The influences of the porosity coefficient, weight fraction of GPLs on plate's behavior are considered.

# Active vibration control of GPLs-reinforced FG metal foam plates with piezoelectric sensor and actuator layers

Nam V. Nguyen$^{\rm a}$, Jaehong Lee$^{\rm b}$, H. Nguyen-Xuan$^{\rm c,b,*}$

$^{\rm a}$Faculty of Mechanical Technology, Industrial University of Ho Chi Minh City, Ho Chi Minh City, Vietnam
$^{\rm b}$Department of Architectural Engineering, Sejong University, 98 Gunja-dong, Gwangjin-gu, Seoul 143-747, South Korea
$^{\rm c}$CIRTech Institute, Ho Chi Minh City University of Technology (HUTECH), Ho Chi Minh City, Vietnam

---

## Abstract
This paper investigates free vibration and dynamic responses of smart FG metal foam plate structures reinforced by graphene platelets (GPLs). We then analyse active control of FG metal foam plates with piezoelectric sensor and actuator layers. To provide numerical solution of underlying problems, we develop a computational approach based on a $C^0$-HSDT polygonal finite element formulation (PFEM), which is suitable for modeling both thick and thin plates. To enhance accuracy of solution, we use in PFEM quadratic serendipity shape functions in combination with a generalized $C^0$-type higher-order shear deformation theory ($C^0$-HSDT). The FG core layers are constituted by combining between two porosity distributions and three GPL dispersion patterns distributed along the plate's thickness while two piezoelectric layers are perfectly bonded on the both bottom and top surfaces of host plate. The mechanical displacement field is approximated based on $C^0$-HSDT while the electric potential distribution through the thickness for each piezoelectric layer is assumed to be a linear function. For active control, a constant velocity feedback scheme is employed through a closed loop control with piezoelectric sensors and actuators. The effect of the porosity coefficient, weight fraction of GPLs on the plate's behaviors with various porosity distributions and GPL dispersion patterns are evidently demonstrated through numerical examples.

Keywords: Polygonal finite element method, Piezoelectric materials, FG metal foam plate, Graphene platelets reinforcement, Active control.

---

## 1. Introduction
Thanks to superior engineering properties such as lightweight, excellent energy-absorbing capability, great thermal resistant properties, etc., porous materials, such as metal foams, have been widely employed in various fields including aerospace engineering, automotive industrial, biomedical and other areas [1, 2, 3, 4]. In addition, to enhance the performance of engineering materials,

---
*Corresponding author
Email address: ngx.hung@hutech.edu.vn (H. Nguyen-Xuan )

Preprint submitted to Elsevier
May 9, 2019

the reinforcement by carbon-based nanofillers including carbon nanotubes (CNTs) [5, 6, 7, 8] and graphene platelets (GPLs) [9] into the porous materials as additives have been studied. Compared with CNTs, GPLs have revealed great potentials to become a good candidate for enhancing the stiffness of metal foam structures [10, 11] as they have excellent mechanical properties, a larger specific surface area as well as a lower manufacturing cost. Numerous investigations have been carried out to study behaviors of FG metal foam beams and plates reinforced with GPLs in the literature.

In this regard, Kitipornchai et al. [12] employed the Ritz method for the free vibration and elastic buckling analyses of FG porous beam reinforced with GPLs. Meanwhile, Chen et al. [13] presented the nonlinear vibration and post-buckling behaviors of the multi-layer FG porous beams with GPLs reinforcement using Timoshenko's beam theory. Based on an analytical approach, Liu et al. [14] performed the nonlinear static response and stability analysis of FG porous arch structures with GPLs reinforcement. By applying Chebyshev-Ritz method, Yang et al. [15] investigated the free vibration and buckling of the FG porous plates reinforced by GPLs uniformly or non-uniformly distributed in the metal matrix. Li et al. [16] analysed the static, free vibration as well as buckling of the FG porous plates with a small amount of GPLs using both first- and third-order shear deformation plate theories based on isogeometric analysis (IGA). The nonlinear free vibration analysis of FG porous plate with a small amount of GPLs resting on elastic foundation is reported by Gao et al. [17]. Li et al. [18] investigated the nonlinear vibration and dynamic buckling problems of the sandwich FG porous plate reinforced by GPL resting on Winkler-Pasternak elastic foundation using the Galerkin method and the fourth-order Runge-Kutta approach. Recently, Nguyen et al. [19] presented the static and dynamic responses of FG porous plate reinforced with GPLs embedded in piezoelectric layers by using IGA based on Bézier extraction.

Recently, the use of piezoelectric materials to build up advanced smart structures for modern industrial products has also been highly interested in the scientific community. In terms of investigation for the plates integrated with piezoelectric layers, numerous studies have been carried out to predict their behaviors in the literature [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]. In addition, Alibeigloo [30] presented the static and free vibration analyses of FG carbon nanotubes reinforced composite (FG-CNTRC) plates embedded in thin piezoelectric layers based on the three-dimensional theory of elasticity. Sharma et al. [31] performed the dynamic response and active vibration control behaviors of FG-CNTRC plates integrated with piezoelectric sensor and actuator layers based on FSDT. By using HSDT and element-free IMLS-Ritz model, Selim et al. [32] investigated the free vibration and active vibration control of FG-CNTRC plates with piezoelectric layers. Meanwhile, the dynamic responses of laminated CNTRC plates integrated with piezoelectric layers are reported by Nguyen-Quang et al. [33] based on IGA based on HSDT. Malekzade et al. [34] employed the transformed differential quadrature approach to analyze the free vibration of FG eccentric annular plate structures reinforced with GPLs and integrated piezoelectric layers.

In 2D finite element analysis, modeling the physical domain based on the typical triangular and quadrilateral elements becomes popular. However, their performance needs still to be improved by using the general shape functions via the framework of polygonal finite elements (PFEM). To by-

pass this bottleneck, PFEM where elements have arbitrary number of edges becomes a prominent alternative. In PFEM, the establishment of the general shape functions [35] formed the rational polynomial interpolation function in which the Kronecker-delta properties is maintained. This work is then extended to construct the shape functions for arbitrary convex polytopes by Warren [36] and for irregular polygons by Meyer et al. [37]. Furthermore, various approaches were introduced such as mean value coordinates [38], maximum entropy coordinates [39], natural neighbor [40], moving least squares coordinates [41], among others. Besides, Rand et al. [42] introduced the quadratic serendipity basis functions for polygonal elements where the nodal shape functions are calculated at vertices and mid-side nodes. Recently, PFEM has been broadly employed in various different areas of engineering [43, 44, 45, 46, 47, 48]. Regarding the investigation into plate structures, Nguyen-Xuan [49] proposed the formulation for thin and thick plates based on the Timoshenko's beam assumptions and FSDT. Nguyen et al. [50] then extended this work for laminated composite plates using $C^{0}$-HSDT. Most recently, the combination between PFEM and quadratic serendipity shape functions is reported by Nguyen et al. [51] for geometrically nonlinear analysis of FG porous plates. It is found in this study that the obtained results based on the quadratic serendipity shape functions are more accurate and stable than the previous PFEMs [50].

In view of the above literature, most of the existing reports focused on analyzing the FGM or FG-CNTRC plate structures integrated with piezoelectric layers. Moreover, there are no reports on the free vibration, dynamic and active control analyses of piezoelectric FG metal foam plates reinforced by GPLs using numerical approach, e.g, PFEM. To fill the existing gap in the literature, a new polygonal finite element formulation based on generalized $C^{0}$-HSDT and quadratic serendipity basis functions is presented to analyze aforementioned behaviors of piezoelectric FG metal foam plates with GPLs reinforcement. Accordingly, the quadratic serendipity basis functions are used to obtain more accurate results while the shear locking phenomenon can be easily suppressed by using the Timoshenko's beam theory. In addition, the FG metal foam core layer is made of combining two porosity distributions and three GPL dispersion patterns while two piezoelectric layers are perfectly bonded on the both bottom and top surfaces of plate. The active control for the dynamic responses of the FG metal foam plates with the effect of the structural damping based on a closed loop control with piezoelectric sensors and actuators is then studied. Besides, the influence of several noticeable parameters including porosity coefficient, weight fraction of GPLs as well as distributions of porosities and GPLs in metal matrix on the behaviors of the plate structures are addressed and discussed in detail.

The rest of this study is organized as follows. Section 2 presents the material model, linear piezoelectric constitutive equations and the variational as well as approximate formulations of the piezoelectric FG metal foam plates reinforced by GPLs based on $C^{0}$-HSDT. Meanwhile, Section 3 provides the active control analysis. Section 4 gives the comparison studies and numerical results for the free vibration and dynamic analyses as well as the active control of the piezoelectric FG metal foam plates reinforced with GPLs. The paper is closed with some affirmations which are drawn in Section 5.

### 2. Theory and formulation

#### 2.1. Material properties for metal foam reinforced by GPLs

Consider a piezoelectric FG plate model whose core layer is assumed to be made of metal foam reinforced with GPLs, as illustrated in Fig. 1. The piezoelectric FG plate has the length $a$, width $b$ and the total thickness $h = h_c + 2h_p$, where $h_c$ and $h_p$ are the thicknesses of the core and piezoelectric layers, respectively. Fig. 2 depicts two the porosity distributions and three GPL dispersion patterns along the thickness direction of the core layer of FG plates. The variation of Young's modulus $E$, shear modulus $G$ and mass density $\rho$ through the thickness of metal foam core layer corresponding to two different kinds of porosity distributions are explicitly formulated as

$$
\left\{
\begin{aligned}
E(z) &= E_1\left[1 - e_0\chi(z)\right], \\
G(z) &= G_1\left[1 - e_0\chi(z)\right], \\
\rho(z) &= \rho_1\left[1 - e_m\chi(z)\right],
\end{aligned}
\right. \tag{1}
$$

in which

$$
\chi(z)=\left\{
\begin{aligned}
cos(\pi z/h_c), & \quad -\frac{h_c}{2} \leq z \leq \frac{h_c}{2} \quad \text{Symmetric distribution} \\
cos(\pi z/2h_c+\pi/4), & \quad \text{Asymmetric distribution}
\end{aligned}
\right. \tag{2}
$$

where $E_1$, $G_1$ and $\rho_1$ denote the maximum values of effective Young's modulus, shear modulus and mass density, respectively. Meanwhile, the porosity coefficient can be defined as

$$
e_0=1-\frac{E_{min}}{E_{max}}, \quad (0 \leq e_0 < 1). \tag{3}
$$

where $E_{max}$ and $E_{min}$ denote the effective maximum and minimum values of Young's modulus for the metal foam core layer without GPLs reinforcement, as illustrated in Fig. 2a. Based on the Gaussian random field model [52], the mechanical properties of closed-cell cellular solids can be given as

$$
\frac{E(z)}{E_1}=\left(\frac{\rho(z)/\rho_1+0.121}{1.121}\right)^{2.3} \text{ for } \left(0.15 < \frac{\rho(z)}{\rho_1} < 1\right). \tag{4}
$$

Then, the mass coefficient $e_m$ in Eq. (1) can be given as

$$
e_m=\frac{1.121\left(1-\sqrt[2.3]{1-e_0\chi(z)}\right)}{\chi(z)}. \tag{5}
$$

The Poisson's ratio $\nu(z)$ of the closed-cell cellular solids can be determined by [53]

$$
\nu(z)=0.221\ell+\nu_1\left(0.342\ell^2-1.21\ell+1\right), \tag{6}
$$

where $\nu_1$ is the Poisson's ratio of the pure matrix material without internal pores with parameter $\ell$ is determined as

$$
\ell=1.121\left(1-\sqrt[2.3]{1-e_0\chi(z)}\right). \tag{7}
$$

The varied GPL volume fraction along the plate's thickness for three GPL dispersion patterns, as depicted in Fig. 2b, is expressed as

$$
V_{G P L}= \begin{cases}V_{i 1}\left[1-\cos \left(\pi z / h_{c}\right)\right], & \text { Symmetric distribution (GPL-S) } \\ V_{i 2}\left[1-\cos \left(\pi z / 2 h_{c}+\pi / 4\right)\right], & -\frac{h_{c}}{2} \leq z \leq \frac{h_{c}}{2} \quad \text { Asymmetric distribution (GPL-A) } \\ V_{i 3}, & \text { Uniform distribution (GPL-U) }\end{cases}
\tag{8}
$$

in which $V_{i 1}, V_{i 2}$ and $V_{i 3}$ represent the peak values of volume fraction of GPLs with $i=1,2$ corresponding to two porosity distributions which can be calculated by [15]

$$
\frac{\Lambda_{G P L} \rho_{m} \times \int_{-h_{c} / 2}^{h_{c} / 2}\left[1-e_{m} \chi(z)\right] d z}{\Lambda_{G P L} \rho_{m}+\rho_{G P L}\left(1-\Lambda_{G P L}\right)}= \begin{cases}V_{i 1} \int_{-h_{c} / 2}^{h_{c} / 2}\left[1-\cos \left(\pi z / h_{c}\right)\right] \frac{\rho(z)}{\rho_{1}} d z, \\ V_{i 2} \int_{-h_{c} / 2}^{h_{c} / 2}\left[1-\cos \left(\pi z / 2 h_{c}+\pi / 4\right)\right] \frac{\rho(z)}{\rho_{1}} d z, \\ V_{i 3} \int_{-h_{c} / 2}^{h_{c} / 2} \frac{\rho(z)}{\rho_{1}} d z.\end{cases}
\tag{9}
$$

On the other hand, the effective Young's modulus of metal matrix reinforced by GPLs without internal pores is obtained based on the Halpin-Tsai micromechanics model as [54, 55]

$$
E_{1}=\frac{3}{8}\left(\frac{1+\xi_{L} \eta_{L} V_{G P L}}{1-\eta_{L} V_{G P L}}\right) E_{m}+\frac{5}{8}\left(\frac{1+\xi_{W} \eta_{W} V_{G P L}}{1-\eta_{W} V_{G P L}}\right) E_{m},
\tag{10}
$$

in which

$$
\xi_{L}=\frac{2 l_{G P L}}{t_{G P L}}, \xi_{W}=\frac{2 w_{G P L}}{t_{G P L}}, \eta_{L}=\frac{\left(E_{G P L} / E_{m}\right)-1}{\left(E_{G P L} / E_{m}\right)+\xi_{L}}, \eta_{W}=\frac{\left(E_{G P L} / E_{m}\right)-1}{\left(E_{G P L} / E_{m}\right)+\xi_{W}},
\tag{11}
$$

where $l_{G P L}, w_{G P L}$ and $t_{G P L}$ are the average length, width and thickness of GPLs, respectively; Meanwhile, $E_{G P L}$ and $E_{m}$ are the Young's modulus of GPLs and metal matrix, respectively. Then, the Poisson's ratio and the mass density of the GPLs reinforced metal matrix are defined by the rule of mixture [56] as

$$
\nu_{1}=\nu_{G P L} V_{G P L}+\nu_{m} V_{m},
\tag{12}
$$

$$
\rho_{1}=\rho_{G P L} V_{G P L}+\rho_{m} V_{m},
\tag{13}
$$

where the mechanical properties for GPLs and metal matrix are denoted with subscript symbols $G P L$ and $m$, respectively. Finally, the relationship of GPL volume fraction $V_{G P L}$ and metal matrix $V_{m}$ can be expressed as $V_{G P L}+V_{m}=1$.

### 2.2. Linear piezoelectric constitutive equations

The linear constitutive equations of the FG plate integrated with piezoelectric layers can be given as follows [57, 58]

$$
\left\{\begin{array}{l}
\boldsymbol{\sigma} \\
\mathbf{D}
\end{array}\right\}=\left[\begin{array}{cc}
\mathbf{C} & -\mathbf{e}^{T} \\
\mathbf{e} & \boldsymbol{\Theta}
\end{array}\right]\left\{\begin{array}{l}
\boldsymbol{\varepsilon} \\
\mathbf{E}
\end{array}\right\},
\tag{14}
$$

in which $\boldsymbol{\sigma}$, $\boldsymbol{\varepsilon}$ and $\mathbf{C}$ are the stress, strain vectors and the material constant matrix of mechanical field, respectively; Meanwhile, $\mathbf{D}$ denotes the electric displacement vector and $\mathbf{e}$ represents the piezoelectric constant matrix; $\boldsymbol{\Theta}$ indicates the dielectric constant matrix; Herein, the electric field vector $\mathbf{E}$ is the gradient of electric potential field $\phi$ which can be expressed as [58]

$$
\mathbf{E}=-\operatorname{grad} \phi. \tag{15}
$$

### 2.3. Variational form of the governing equations
By employing the Hamilton's variational principle, the equation of motion for the piezoelectric FG plate can be obtained and expressed as follows [59]

$$
\delta \int_{t_{1}}^{t_{2}} \Pi d t=0, \tag{16}
$$

in which $t_{1}$ and $t_{2}$ denote the starting and finish time, respectively. Meanwhile, the total energy function $\Pi$ which contains the functions including kinetic energy, strain energy, dielectric energy and external work can be expressed as follows

$$
\Pi=\frac{1}{2} \int_{\Omega}\left(\rho \dot{\mathbf{u}}^{T} \dot{\mathbf{u}}-\boldsymbol{\sigma}^{T} \boldsymbol{\varepsilon}+\mathbf{D}^{T} \mathbf{E}\right) \mathrm{d} \Omega+\int_{\Gamma_{s}} \mathbf{u}^{T} \mathbf{f}_{s} \mathrm{~d} \Gamma_{s}-\int_{\Gamma_{\phi}} \phi \mathbf{q}_{s} \mathrm{~d} \Gamma_{\phi}+\sum \mathbf{u}^{T} \mathbf{F}_{p}-\sum \phi \mathbf{Q}_{p}, \tag{17}
$$

where $\mathbf{u}$ and $\dot{\mathbf{u}}$ represent the mechanical displacement and velocity field vectors; Meanwhile, $\mathbf{f}_{s}$ and $\mathbf{F}_{p}$ denote the external mechanical surface and concentrated load vectors; $\mathbf{q}_{s}$ and $\mathbf{Q}_{p}$ indicate the external surface and point charges, respectively, as depicted in Fig. 1; $\Gamma_{s}$ and $\Gamma_{\phi}$ denote the external mechanical and the electrical loading surface, respectively.

Two unknown vectors including the mechanical displacement field $\mathbf{u}$ and electric potential field $\phi$ in Eq. (17) need to obtain. In this study, the PFEM based on $C^{0}$-HSDT is applied to approximate the mechanical displacement field while the linear constitutive relationship is adopted for electric potential field. In next Sections, the formulations for each field will be explicitly presented.

### 2.4. Mechanical displacement field
#### 2.4.1. Displacement and strain field based on $C^{0}$-HSDT
According to the generalized HSDT [60, 61], the displacement field of any material point in FG plate can be expressed as

$$
\mathbf{u}(x, y, z)=\mathbf{u}^{0}(x, y)+z \mathbf{u}^{1}(x, y)+f(z) \mathbf{u}^{2}(x, y), \tag{18}
$$

where

$$
\mathbf{u}=\left\{\begin{array}{c}
u \\
v \\
w
\end{array}\right\}, \mathbf{u}^{0}=\left\{\begin{array}{c}
u_{0} \\
v_{0} \\
w_{0}
\end{array}\right\}, \mathbf{u}^{1}=-\left\{\begin{array}{c}
w_{0, x} \\
w_{0, y} \\
0
\end{array}\right\}, \mathbf{u}^{2}=\left\{\begin{array}{c}
\theta_{x} \\
\theta_{y} \\
0
\end{array}\right\}, \tag{19}
$$

in which $u_{0}, v_{0}, w_{0}, \theta_{x}$ and $\theta_{y}$ are the displacement components in the $x, y, z$ directions and the rotation components in the $y z$ and the $x z$ planes, respectively. Meanwhile, the subscript symbols

$x$ and $y$ are the derivatives of an arbitrary function with respect to $x$ and $y$ directions, respectively; and $f(z)$ is a function to describe the transverse strains and stresses through the plate's thickness. Without loss of the generality, in this work, the famous third-order function proposed by Reddy is chosen as $f(z)=z-\frac{4 z^{3}}{3 h^{2}}$ [62].

To eliminate the high order derivations in approximate formulations as well as impose the boundary conditions conveniently, two additional assumptions are made as follows

$$
w_{0, x}=\beta_{x}, w_{0, y}=\beta_{y}. \tag{20}
$$

Then, by substituting Eq. (20) into Eq. (19) yields

$$
\mathbf{u}^{0}=\left\{\begin{array}{c}
u_{0} \\
v_{0} \\
w_{0}
\end{array}\right\}, \mathbf{u}^{1}=-\left\{\begin{array}{c}
\beta_{x} \\
\beta_{y} \\
0
\end{array}\right\}, \mathbf{u}^{2}=\left\{\begin{array}{c}
\theta_{x} \\
\theta_{y} \\
0
\end{array}\right\}. \tag{21}
$$

As a result, the compatible strain fields derived from Eq. (21) only require the $C^{0}$-continuity of approximate fields. The in-plane strains of the FG plate can be given as

$$
\boldsymbol{\varepsilon}_{p}=\left\{\varepsilon_{x x}, \varepsilon_{y y}, \gamma_{x y}\right\}^{T}=\boldsymbol{\varepsilon}_{0}+z \boldsymbol{\kappa}_{1}+f(z) \boldsymbol{\kappa}_{2}, \tag{22}
$$

where the membrane strain $\boldsymbol{\varepsilon}_{0}$ and the bending strains $\boldsymbol{\kappa}_{1}, \boldsymbol{\kappa}_{2}$ are, respectively, expressed as

$$
\boldsymbol{\varepsilon}_{0}=\left\{\begin{array}{c}
u_{0, x} \\
v_{0, y} \\
u_{0, y}+v_{0, x}
\end{array}\right\}, \boldsymbol{\kappa}_{1}=-\left\{\begin{array}{c}
\beta_{x, x} \\
\beta_{y, y} \\
\beta_{x, y}+\beta_{y, x}
\end{array}\right\}, \boldsymbol{\kappa}_{2}=\left\{\begin{array}{c}
\theta_{x, x} \\
\theta_{y, y} \\
\theta_{x, y}+\theta_{y, x}
\end{array}\right\}. \tag{23}
$$

Meanwhile, the transverse shear strains can be expressed by

$$
\boldsymbol{\gamma}=\left\{\gamma_{x z}, \gamma_{y z}\right\}^{T}=\boldsymbol{\varepsilon}_{s}+f^{\prime}(z) \boldsymbol{\kappa}_{s}, \tag{24}
$$

where

$$
\boldsymbol{\varepsilon}_{s}=\left\{\begin{array}{c}
w_{0, x}-\beta_{x} \\
w_{0, y}-\beta_{y}
\end{array}\right\}, \boldsymbol{\kappa}_{s}=\left\{\begin{array}{c}
\theta_{x} \\
\theta_{y}
\end{array}\right\}, \tag{25}
$$

in which $f^{\prime}(z)$ represents the derivation of the function $f(z)$.

With the assuming of $\sigma_{z z}=0$, the constitutive equation of the FG plate is derived from Hooke's law as

$$
\left\{\begin{array}{c}
\sigma_{x x} \\
\sigma_{y y} \\
\tau_{x y} \\
\tau_{x z} \\
\tau_{y z}
\end{array}\right\}=\left[\begin{array}{ccccc}
Q_{11} & Q_{12} & 0 & 0 & 0 \\
Q_{21} & Q_{22} & 0 & 0 & 0 \\
0 & 0 & Q_{66} & 0 & 0 \\
0 & 0 & 0 & Q_{55} & 0 \\
0 & 0 & 0 & 0 & Q_{44}
\end{array}\right]\left\{\begin{array}{c}
\varepsilon_{x x} \\
\varepsilon_{y y} \\
\gamma_{x y} \\
\gamma_{x z} \\
\gamma_{y z}
\end{array}\right\}, \tag{26}
$$

in which material constants are given as

$$
Q_{11}=Q_{22}=\frac{E(z)}{1-\nu(z)^{2}}, Q_{12}=Q_{21}=\frac{\nu(z) E(z)}{1-\nu(z)^{2}}, Q_{44}=Q_{55}=Q_{66}=G(z). \tag{27}
$$

Then, by substituting Eqs. (22) and (24) into Eq. (26), one obtains

$$
\boldsymbol{\sigma}=\left\{\begin{array}{c}
\boldsymbol{\sigma}_{p} \\
\boldsymbol{\tau}
\end{array}\right\}=\left[\begin{array}{cc}
\hat{\mathbf{D}}^{\mathrm{b}} & \mathbf{0} \\
\mathbf{0} & \hat{\mathbf{D}}^{s}
\end{array}\right]\left\{\begin{array}{c}
\boldsymbol{\varepsilon}_{p} \\
\boldsymbol{\gamma}
\end{array}\right\}=\mathbf{C} \boldsymbol{\varepsilon}, \tag{28}
$$

where the material constant matrices $\hat{\mathbf{D}}^{b}$ and $\hat{\mathbf{D}}^{s}$ are given as

$$
\hat{\mathbf{D}}^{b}=\left[\begin{array}{ccc}
\mathbf{A} & \mathbf{B} & \mathbf{L} \\
\mathbf{B} & \mathbf{G} & \mathbf{P} \\
\mathbf{L} & \mathbf{P} & \mathbf{H}
\end{array}\right], \quad \hat{\mathbf{D}}^{s}=\left[\begin{array}{cc}
\mathbf{A}^{s} & \mathbf{B}^{s} \\
\mathbf{B}^{s} & \mathbf{D}^{s}
\end{array}\right], \tag{29}
$$

in which

$$
\begin{aligned}
(\mathbf{A}, \mathbf{B}, \mathbf{G}, \mathbf{L}, \mathbf{P}, \mathbf{H}) &=\int_{-h / 2}^{h / 2}\left(1, z, z^{2}, f(z), z f(z), f^{2}(z)\right)\left[\begin{array}{ccc}
Q_{11} & Q_{12} & 0 \\
Q_{21} & Q_{22} & 0 \\
0 & 0 & Q_{66}
\end{array}\right] \mathrm{d} z, \\
\left(\mathbf{A}^{s}, \mathbf{B}^{s}, \mathbf{D}^{s}\right) &=\int_{-h / 2}^{h / 2}\left(1, f^{\prime}(z), f^{\prime 2}(z)\right)\left[\begin{array}{cc}
Q_{55} & 0 \\
0 & Q_{44}
\end{array}\right] \mathrm{d} z,
\end{aligned} \tag{30}
$$

#### 2.4.2. PFEM formulation for FG plate

The bounded domain $\Omega$ is discretized into $n_{e}$ arbitrary polygonal elements including the triangular and quadrilateral ones such that $\Omega=\bigcup_{e=1}^{n_{e}} \Omega^{e}$ and $\Omega^{i} \cap \Omega^{j}=\emptyset, i \neq j$. Now, the approximate displacement function $\mathbf{u}^{h}(\mathbf{x})$ for FG plate element can be expressed as

$$
\mathbf{u}^{h}(\mathbf{x})=\sum_{I}^{n} \boldsymbol{\psi}_{I} \mathbf{I}_{7} \mathbf{d}_{I}=\sum_{I}^{n} \boldsymbol{\psi}_{I} \mathbf{d}_{I}, \quad \text { in } \Omega^{e}, \tag{31}
$$

in which $\boldsymbol{\psi}$ and $n$ denote the shape function and the number of vertices of element $\Omega^{e}$, respectively. Meanwhile, $\mathbf{d}_{I}=\left\{u_{I}, v_{I}, w_{I}, \beta_{x I}, \beta_{y I}, \theta_{x I}, \theta_{y I}\right\}^{T}$ represents the vector of the nodal degrees of freedom associated with the $I$ th vertex of arbitrary polygonal element, $\mathbf{I}_{7}$ indicates the unit matrix of 7th rank.

By substituting the approximation in Eq. (31) into Eqs. (23) and (25), the membrane, bending and shear strains can be presented in compact forms as follows

$$
\boldsymbol{\varepsilon}_{0}=\sum_{I}^{n} \mathbf{B}_{I}^{m} \mathbf{d}_{I}, \quad \boldsymbol{\kappa}_{1}=\sum_{I}^{n} \mathbf{B}_{I}^{b 1} \mathbf{d}_{I}, \quad \boldsymbol{\kappa}_{2}=\sum_{I}^{n} \mathbf{B}_{I}^{b 2} \mathbf{d}_{I}, \tag{32a}
$$

$$
\boldsymbol{\varepsilon}_{s}=\sum_{I}^{n} \mathbf{B}_{I}^{s 0} \mathbf{d}_{I}, \quad \boldsymbol{\kappa}_{s}=\sum_{I}^{n} \mathbf{B}_{I}^{s 1} \mathbf{d}_{I}, \tag{32b}
$$

in which

$$
\mathbf{B}_{I}^{m}=\left[\begin{array}{ccccccc}
\psi_{I, x} & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & \psi_{I, y} & 0 & 0 & 0 & 0 & 0 \\
\psi_{I, y} & \psi_{I, x} & 0 & 0 & 0 & 0 & 0
\end{array}\right], \mathbf{B}_{I}^{b 1}=-\left[\begin{array}{ccccccc}
0 & 0 & 0 & \psi_{I, x} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & \psi_{I, y} & 0 & 0 \\
0 & 0 & 0 & \psi_{I, y} & \psi_{I, x} & 0 & 0
\end{array}\right],
$$

$$
\mathbf{B}_{I}^{b 2}=\left[\begin{array}{ccccccc}
0 & 0 & 0 & 0 & 0 & \psi_{I, x} & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & \psi_{I, y} \\
0 & 0 & 0 & 0 & 0 & \psi_{I, y} & \psi_{I, x}
\end{array}\right],
$$

$$
\mathbf{B}_{I}^{s 0}=\left[\begin{array}{ccccccc}
0 & 0 & \psi_{I, x} & -\psi_{I} & 0 & 0 & 0 \\
0 & 0 & \psi_{I, y} & 0 & -\psi_{I} & 0 & 0
\end{array}\right], \mathbf{B}_{I}^{s 1}=\left[\begin{array}{ccccccc}
0 & 0 & 0 & 0 & 0 & \psi_{I} & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & \psi_{I}
\end{array}\right].
$$

(33)

One of the disadvantages of $C^{0}$ approximation is the shear locking phenomenon. In this study, in order to avoid this obstacle, a unified and efficient polygonal locking-free plate element is derived using an assumed strain field based on the Timoshenko's beam theory in next subsection.

### 2.4.3. A novel PFEM for FG plate element
#### 2.4.3.1. Deformation of Timoshenko's beam element.
By applying the Timoshenko's beam theory, the deflection $w(\xi)$, rotation $\theta(\xi)$ and shear strain $\gamma(\xi)$ of the thick beam element, as depicted in Fig. 3, can be expressed as follows [63, 64]

$$
w(\xi)=w_{i}(1-\xi)+w_{j} \xi+\frac{l}{2}\left(-\theta_{i}+\theta_{j}\right) \xi(1-\xi)-\frac{l}{2} \Gamma(1-2 \Im) \xi(1-\xi)(1-2 \xi), \quad(34 \mathrm{a})
$$

$$
\theta(\xi)=\theta_{i}(1-\xi)+\theta_{j} \xi-3 \Gamma(1-2 \Im) \xi(1-\xi),\quad(34b)
$$

$$
\gamma(\xi)=\Im \Gamma,\quad(34c)
$$

in which

$$
\Gamma=\frac{2}{l}\left(-w_{i}+w_{j}\right)+\theta_{i}+\theta_{j}, \quad \Im=\frac{6 \wp}{1+12 \wp}, \quad \wp=\frac{D^{b}}{D^{s} l^{2}},\quad(35)
$$

where $D^{b}, D^{s}$ and $l$ are the bending, shear stiffness constants and length of the thick beam element, respectively. It can be observed that, the parameter $\wp$ in Eq. (35) will close to zero as the plate's thickness $h$ approaches zero. As a result, the parameter $\Im$ will also tend to zero. Consequently, the transverse shear strain $\gamma(\xi)$ in Eq. (34c) will be suppressed. Next, this approach is further developed for arbitrary polygonal FG plate element.

#### 2.4.3.2. Assumed shear strain field.
Let us consider a polygonal plate element $\Omega^{e} \in \mathbb{R}^{2}$ with the normal and tangential directions of each edge, as depicted in Fig. 4. Then, the generalized nodal displacement of the element can be expressed as follows

$$
\mathbf{d}=\left\{\mathbf{d}_{1}, \mathbf{d}_{2}, \ldots, \mathbf{d}_{n-1}, \mathbf{d}_{n}\right\}^{T}.\quad(36)
$$

where $\mathbf{d}_{i}=\left\{u_{i}, v_{i}, w_{i}, \beta_{x i}, \beta_{y i}, \theta_{x i}, \theta_{y i}\right\}^{T}$ with $i=1,2,..., n-1, n$. Based on Timoshenko's beam assumptions along the sides of polygonal element, Nguyen-Xuan [49] developed an interpolation

procedure for assumed shear strain field. Accordingly, the transversal shear strain can be presented
in a compact form as

$$
\gamma=\left[\tilde{\mathbf{B}}^{s 0}, \mathbf{B}^{s 1}\right]\{\mathbf{d}\}, \quad(37)
$$

in which the matrix $\mathbf{B}^{s 1}$ is presented in Eq. (33). The matrix $\tilde{\mathbf{B}}^{s 0}=\left[\boldsymbol{\Xi}^{s}\right]\left[\mathbf{I}^{s}\right]\left[\boldsymbol{\Phi}^{s}\right]$ with $\left[\boldsymbol{\Xi}^{s}\right],\left[\mathbf{I}^{s}\right]$
and $\left[\boldsymbol{\Phi}^{s}\right]$ can be determined by, respectively

$$
\left[\boldsymbol{\Xi}^{s}\right]_{\{2 × n\}}=\sum_{\hat{i}, \hat{j}, \hat{k}, \hat{m}}\left[\begin{array}{c}
\frac{b_{\hat{m}} \psi_{\hat{j}}}{c_{\hat{i}} b_{\hat{m}}-c_{\hat{m}} b_{\hat{i}}}-\frac{b_{\hat{j}} \psi_{\hat{k}}}{c_{\hat{j}} b_{\hat{i}}-c_{\hat{i}} b_{\hat{j}}} \\
\frac{c_{\hat{m}} \psi_{\hat{j}}}{c_{\hat{i}} b_{\hat{m}}-c_{\hat{m}} b_{\hat{i}}}-\frac{c_{\hat{j}} \psi_{\hat{k}}}{c_{\hat{j}} b_{\hat{i}}-c_{\hat{i}} b_{\hat{j}}}
\end{array}\right], \quad(38)
$$

$$
\left[\mathbf{I}^{s}\right]_{\{n × n\}}=\left[\delta_{\hat{i} \hat{i}} \Im_{\hat{i}}\right], \quad(39)
$$

$$
\left[\boldsymbol{\Phi}^{s}\right]_{\{n, 7 n\}}=\sum_{\hat{i}, \hat{j}}\left[-2_{\hat{i}, 7 \hat{j}-4}, c_{\hat{i}, 7 \hat{j}-3},-b_{\hat{i}, 7 \hat{j}-2}\right]+\sum_{\hat{i}, \hat{k}}\left[2_{\hat{i}, 7 \hat{k}-4}, c_{\hat{i}, 7 \hat{k}-3},-b_{\hat{i}, 7 \hat{k}-2}\right], \quad(40)
$$

where $\Im_{\hat{i}}$ is found in Eq. (35). Meanwhile, $\psi_{\hat{i}}$ denotes the Wachspress shape function at $\hat{i}$ th vertex
of element and the coefficients $b_{\hat{i}}, c_{\hat{i}}$ can be determined as

$$
b_{\hat{i}}=y_{\hat{j}}-y_{\hat{k}}, c_{\hat{i}}=x_{\hat{k}}-x_{\hat{j}}, \quad(41)
$$

in which

$$
\left\{\begin{array}{l}
\hat{i}=1,2, \ldots, n-1, n ; \hat{j}=2,3, \ldots, n-1, n, 1 ; \\
\hat{k}=3,4, \ldots, n, 1,2 ; \hat{m}=n, 1, \ldots n-2, n-1.
\end{array}\right.
$$

#### 2.4.3.3. An improved of assumed bending strain field.
By applying the quadratic serendipity shape
functions, the assumed bending strains for the polygonal element are developed to improve the
performance of PFEM. Fig. 5 describes the quadratic serendipity shape functions for a pentagonal
element. Accordingly, the improved assumed bending strains can be written in compact form as
follows

$$
\boldsymbol{\varepsilon}_{p}=\left[\mathbf{B}^{m}, \tilde{\mathbf{B}}^{b 1}, \mathbf{B}^{b 2}\right]\{\mathbf{d}\}, \quad(43)
$$

where $\tilde{\mathbf{B}}^{b 1}=\mathbf{B}^{b 1}+\hat{\mathbf{B}}^{b 1}$. The matrices $\mathbf{B}^{m}, \mathbf{B}^{b 1}$ and $\mathbf{B}^{b 2}$ can be found in Eq. (33). And $\hat{\mathbf{B}}^{b 1}=$
$\left[\boldsymbol{\Xi}_{1}^{b}\right]\left[\boldsymbol{\Phi}_{1}^{b}\right]+\left[\boldsymbol{\Xi}_{2}^{b}\right]\left[\boldsymbol{\Phi}_{2}^{b}\right]$ with the matrices $\left[\boldsymbol{\Xi}_{1}^{b}\right],\left[\boldsymbol{\Xi}_{2}^{b}\right],\left[\boldsymbol{\Phi}_{1}^{b}\right]$ and $\left[\boldsymbol{\Phi}_{2}^{b}\right]$ are defined as, respectively

$$
\left[\boldsymbol{\Xi}_{1}^{b}\right]_{\{3 x n\}}=\left[\frac{\partial \varphi_{\bar{j}}}{\partial x}, 0, \frac{\partial \varphi_{\bar{j}}}{\partial y}\right]^{T},\left[\boldsymbol{\Xi}_{2}^{b}\right]_{\{3 x n\}}=\left[0, \frac{\partial \varphi_{\bar{j}}}{\partial y}, \frac{\partial \varphi_{\bar{j}}}{\partial x}\right]^{T}, \quad(44)
$$

$$
\left[\boldsymbol{\Phi}_{1}^{b}\right]_{\{n, 7 n\}}=\sum_{\hat{i}, \hat{j}}\left[\tilde{g}_{\hat{i}, 7 \hat{j}-4}^{1}, \tilde{g}_{\hat{i}, 7 \hat{j}-3}^{2}, \tilde{g}_{\hat{i}, 7 \hat{j}-2}^{3}\right]+\sum_{\hat{i}, \hat{k}}\left[-\tilde{g}_{\hat{i}, 7 \hat{k}-4}^{1}, \tilde{g}_{\hat{i}, 7 \hat{k}-3}^{2}, \tilde{g}_{\hat{i}, 7 \hat{k}-2}^{3}\right], \quad(45)
$$


$$
\left[\boldsymbol{\Phi}_{2}^{b}\right]_{\{n, 7 n\}}=\sum_{\hat{i}, \hat{j}}\left[\hat{g}_{\hat{i}, \tau \hat{j}-4}^{1}, \hat{g}_{\hat{i}, \tau \hat{j}-3}^{2}, \hat{g}_{\hat{i}, \tau \hat{j}-2}^{3}\right]+\sum_{\hat{i}, \hat{k}}\left[-\hat{g}_{\hat{i}, \tau \hat{k}-4}^{1}, \hat{g}_{\hat{i}, \tau \hat{k}-3}^{2}, \hat{g}_{\hat{i}, \tau \hat{k}-2}^{3}\right],
\tag{46}
$$

where $\bar{j}=n+1, n+2, \cdots, 2 n-1,2 n$. And

$$
\begin{aligned}
& \tilde{g}_{\hat{i}}^{1}=\frac{3 c_{\hat{i}}\left(1-2 \delta_{\hat{i}}\right)}{2 l_{\hat{i}}^{2}} ; \tilde{g}_{\hat{i}}^{2}=\frac{b_{\hat{i}}^{2}-0.5 c_{\hat{i}}^{2}\left(1-6 \delta_{\hat{i}}\right)}{2 l_{\hat{i}}^{2}} ; \tilde{g}_{\hat{i}}^{3}=\frac{3 b_{\hat{i}} c_{\hat{i}}\left(1-2 \delta_{\hat{i}}\right)}{4 l_{\hat{i}}^{2}}, \\
& \hat{g}_{\hat{i}}^{1}=\frac{-3 b_{\hat{i}}\left(1-2 \delta_{\hat{i}}\right)}{2 l_{\hat{i}}^{2}} ; \hat{g}_{\hat{i}}^{2}=\frac{3 b_{\hat{i}} c_{\hat{i}}\left(1-2 \delta_{\hat{i}}\right)}{4 l_{\hat{i}}^{2}} ; \hat{g}_{\hat{i}}^{3}=\frac{c_{\hat{i}}^{2}-0.5 b_{\hat{i}}^{2}\left(1-6 \delta_{\hat{i}}\right)}{2 l_{\hat{i}}^{2}},
\end{aligned}
\tag{47}
$$

in which $l_{\hat{i}}=\left\|x_{\hat{j}}-x_{\hat{k}}\right\|$ is the length of the $\hat{i}$ th edge of element while the indices $\hat{i}, \hat{j}, \hat{k}$ are found in Eq. (42). As evidently demonstrated in Eqs. (44-46), although the quadratic serendipity shape functions are adopted to determine the assumed bending strain field, the total number of DOFs per element does not increase when compared with the formulations in [50]. This means the mid-side nodes of element will be eliminated in the computational process.

### 2.5. Electric potential field

By discretizing the piezoelectric layer into $n_{s u b}$ sublayers along the thickness, the electric potential field on each layer is then approximated. Accordingly, the electric potential variation in each sublayer is considered to be linear and is approximated across the thickness as [65]

$$
\phi^{i}(z)=\mathbf{N}_{\phi}^{i} \phi^{i},
\tag{48}
$$

in which $\mathbf{N}_{\phi}^{i}$ and $\phi^{i}$ are the electric potential shape function and the electric potentials at the top and bottom surfaces of the sublayer, respectively, and are determined as

$$
\begin{aligned}
& \mathbf{N}_{\phi}^{i}=\frac{1}{h_{i}}\left\{\begin{array}{ll}
z_{i}-z, & z-z_{i-1}
\end{array}\right\}, h_{i}=z_{i}-z_{i-1}, \\
& \boldsymbol{\phi}^{i}=\left\{\begin{array}{ll}
\phi^{i-1}, & \phi^{i}
\end{array}\right\}^{T}, i=1,2, \ldots, n_{s u b}.
\end{aligned}
\tag{49}
$$

It is assumed that the values of the electric potential for each sublayer are estimated to equal at the same height along the thickness [66]. Hence, the electric potential field $\mathbf{E}$ for each sublayer element can be expressed as follows

$$
\mathbf{E}^{i}=-\nabla \mathbf{N}_{\phi}^{i} \phi^{i}=-\mathbf{B}_{\phi} \phi^{i},
\tag{50}
$$

Finally, the stress piezoelectric constant matrix $\mathbf{e}$ and the dielectric constant matrix $\boldsymbol{\Theta}$ can be defined by

$$
\mathbf{e}=\left[\begin{array}{ccccc}
0 & 0 & 0 & 0 & e_{15} \\
0 & 0 & 0 & e_{15} & 0 \\
e_{31} & e_{32} & e_{33} & 0 & 0
\end{array}\right], \boldsymbol{\Theta}=\left[\begin{array}{ccc}
p_{11} & 0 & 0 \\
0 & p_{22} & 0 \\
0 & 0 & p_{33}
\end{array}\right].
\tag{51}
$$


### 2.6. Governing equation of motion

By substituting Eqs. (28), (32), (48) and (50) into Eqs. (17) and (16), the governing equation of motion can be obtained and expressed as follows [65]

$$
\left[\begin{array}{cc}
\mathbf{M}_{u u} & \mathbf{0} \\
\mathbf{0} & \mathbf{0}
\end{array}\right]\left\{\begin{array}{c}
\ddot{\mathbf{d}} \\
\ddot{\boldsymbol{\phi}}
\end{array}\right\}+\left[\begin{array}{cc}
\mathbf{K}_{u u} & \mathbf{K}_{u \phi} \\
\mathbf{K}_{\phi u} & -\mathbf{K}_{\phi \phi}
\end{array}\right]\left\{\begin{array}{c}
\mathbf{d} \\
\boldsymbol{\phi}
\end{array}\right\}=\left\{\begin{array}{c}
\mathbf{F} \\
\mathbf{Q}
\end{array}\right\}, \tag{52}
$$

where

$$
\begin{gathered}
\mathbf{K}_{u u}=\int_{\Omega} \mathbf{B}_{u}^{\mathrm{T}} \mathbf{C B}_{u} \mathrm{d} \Omega, \mathbf{K}_{\phi \phi}=\int_{\Omega} \mathbf{B}_{\phi}^{\mathrm{T}} \boldsymbol{\Theta} \mathbf{B}_{\phi} \mathrm{d} \Omega, \mathbf{K}_{u \phi}=\int_{\Omega} \mathbf{B}_{u}^{\mathrm{T}} \tilde{\mathbf{e}}^{\mathrm{T}} \mathbf{B}_{\phi} \mathrm{d} \Omega, \mathbf{K}_{\phi u}=\mathbf{K}_{u \phi}^{\mathrm{T}}, \\
\mathbf{M}_{\mathbf{u u}}=\int_{\Omega} \tilde{\mathbf{N}}^{\mathrm{T}} \mathbf{m} \tilde{\mathbf{N}} \mathrm{d} \Omega, \mathbf{F}=\int_{\Omega} f_{s} \overline{\mathbf{N}} \mathrm{d} \Omega,
\end{gathered} \tag{53}
$$

in which

$$
\begin{gathered}
\mathbf{B}_{u}=\left[\begin{array}{lllll}
\mathbf{B}^{m} & \mathbf{B}^{b 1} & \mathbf{B}^{b 2} & \mathbf{B}^{s 0} & \mathbf{B}^{s 1}
\end{array}\right]^{\mathrm{T}}, \tilde{\mathbf{e}}=\left[\begin{array}{llllll}
\mathbf{e}_{m}^{\mathrm{T}} & z \mathbf{e}_{m}^{\mathrm{T}} & f(z) \mathbf{e}_{m}^{\mathrm{T}} & \mathbf{e}_{s}^{\mathrm{T}} & f^{\prime}(z) \mathbf{e}_{s}^{\mathrm{T}}
\end{array}\right], \\
\tilde{\mathbf{N}}=\left[\begin{array}{lll}
\mathbf{N}^{0} & \mathbf{N}^{1} & \mathbf{N}^{2}
\end{array}\right], \overline{\mathbf{N}}=\left[\begin{array}{lllllll}
0 & 0 & \psi_{I} & 0 & 0 & 0 & 0
\end{array}\right],
\end{gathered} \tag{54}
$$

where

$$
\begin{gathered}
\mathbf{e}_{m}=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
e_{31} & e_{32} & e_{33}
\end{array}\right], \mathbf{e}_{s}=\left[\begin{array}{cc}
0 & e_{15} \\
e_{15} & 0 \\
0 & 0
\end{array}\right], \mathbf{N}^{0}=\left[\begin{array}{ccccccc}
\psi_{I} & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & \psi_{I} & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & \psi_{I} & 0 & 0 & 0 & 0
\end{array}\right], \\
\mathbf{N}^{1}=-\left[\begin{array}{ccccccc}
0 & 0 & 0 & \psi_{I} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & \psi_{I} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{array}\right], \mathbf{N}^{2}=\left[\begin{array}{ccccccc}
0 & 0 & 0 & 0 & 0 & \psi_{I} & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & \psi_{I} \\
0 & 0 & 0 & 0 & 0 & 0 & 0
\end{array}\right]
\end{gathered} \tag{55}
$$

and

$$
\mathbf{m}=\left[\begin{array}{ccc}
I_{1} & I_{2} & I_{4} \\
I_{2} & I_{3} & I_{5} \\
I_{4} & I_{5} & I_{6}
\end{array}\right] \tag{56}
$$

where the mass inertia terms $I_{i}$ with $i=1: 6$ are given as

$$
\left(I_{1}, I_{2}, I_{3}, I_{4}, I_{5}, I_{6}\right)=\int_{-h / 2}^{h / 2} \rho(z)\left(1, z, z^{2}, f(z), z f(z), f^{2}(z)\right) \mathrm{d} z. \tag{57}
$$

Note that the electric potential field $\mathbf{E}$ depends only on the $z$ direction, the matrix $\mathbf{K}_{u \phi}$ in Eq. (53) can be rewritten as

$$
\mathbf{K}_{u \phi}=\int_{\Omega}\left(\left(\mathbf{B}^{m}\right)^{T} \mathbf{e}_{m}^{T} \mathbf{B}_{\phi}+z\left(\mathbf{B}^{b 1}\right)^{T} \mathbf{e}_{m}^{T} \mathbf{B}_{\phi}+f(z)\left(\mathbf{B}^{b 2}\right)^{T} \mathbf{e}_{m}^{T} \mathbf{B}_{\phi}\right) d \Omega. \tag{58}
$$

Now, by substituting the second equation into the first one of Eq. (52), one obtains

$$
\mathbf{M}_{u u} \ddot{\mathbf{d}}+\left(\mathbf{K}_{u u}+\mathbf{K}_{u \phi} \mathbf{K}_{\phi \phi}^{-1} \mathbf{K}_{\phi u}\right) \mathbf{d}=\mathbf{F}+\mathbf{K}_{u \phi} \mathbf{K}_{\phi \phi}^{-1} \mathbf{Q}. \tag{59}
$$

## 3. Active vibration control

In this section, the FG metal foam plate integrated with piezoelectric layers, as depicted in Fig. 6, is considered for the active control the responses of structure. In this model, the bottom layer represents a piezoelectric sensor labeled with the subscript $s$ while the other layer is a piezoelectric actuator which is denoted with the subscript $a$. When the FG plate structures deform, the electric charges are generated and gathered in the sensor layer because of the piezoelectric effect. These electric charges are then amplified based on the appropriate electronic circuit to convert into the voltage signal before being fed back and applied to the actuator layer though closed loop control algorithm. Due to the converse piezoelectric effect, the strains and stresses of structure are formed which can damp the dynamic responses of the plate structures.

Assuming without any the external charge $\mathbf{Q}$, the generated potential on the sensor layer can be obtained by the following the second equation of Eq. (52)

$$
\phi_{s}=\left[\mathbf{K}_{\phi \phi}^{-1}\right]_{s}\left[\mathbf{K}_{\phi u}\right]_{s} \mathbf{d}_{s}, \tag{60}
$$

Now, the sensor charge resulted due to the deformation is determined by

$$
\mathbf{Q}_{s}=\left[\mathbf{K}_{\phi u}\right]_{s} \mathbf{d}_{s}. \tag{61}
$$

Through the closed loop control, the actuator voltage $\phi_{a}$ can be expressed as [67]

$$
\phi_{a}=G_{d} \phi_{s}+G_{v} \dot{\phi}_{s}. \tag{62}
$$

in which $G_{d}$ and $G_{v}$ represent the displacement and velocity feedback control gains. Then, the magnitude of the actuator layer charge can be obtained by substituting Eqs. (62) and (60) into the second equation in Eq. (52)

$$
\mathbf{Q}_{a}=\left[\mathbf{K}_{\phi u}\right]_{a} \mathbf{d}_{a}-G_{d}\left[\mathbf{K}_{\phi \phi}\right]_{a}\left[\mathbf{K}_{\phi \phi}^{-1}\right]_{s}\left[\mathbf{K}_{\phi u}\right]_{s} \mathbf{d}_{s}-G_{v}\left[\mathbf{K}_{\phi \phi}\right]_{a}\left[\mathbf{K}_{\phi \phi}^{-1}\right]_{s}\left[\mathbf{K}_{\phi u}\right]_{s} \dot{\mathbf{d}}_{s}. \tag{63}
$$

Finally, by substituting Eq. (63) into Eq. (59) yields

$$
\mathbf{M} \ddot{\mathbf{d}}+\left(\mathbf{C}_{a}+\mathbf{C}_{R}\right) \dot{\mathbf{d}}+\mathbf{K}^{*} \mathbf{d}=\mathbf{F}, \tag{64}
$$

in which the stiffness matrix $\mathbf{K}^{*}$, active damping matrix $\mathbf{C}_{a}$ and Rayleigh damping matrix $\mathbf{C}_{R}$ can be defined as

$$
\mathbf{K}^{*}=\mathbf{K}_{u u}+G_{d}\left[\mathbf{K}_{u \phi}\right]_{a}\left[\mathbf{K}_{\phi \phi}^{-1}\right]_{s}\left[\mathbf{K}_{\phi u}\right]_{s}, \tag{65}
$$

$$
\mathbf{C}_{a}=G_{v}\left[\mathbf{K}_{u \phi}\right]_{a}\left[\mathbf{K}_{\phi \phi}^{-1}\right]_{s}\left[\mathbf{K}_{\phi u}\right]_{s}. \tag{66}
$$

$$
\mathbf{C}_{R}=\alpha_{R} \mathbf{M}+\beta_{R} \mathbf{K}_{u u}, \tag{67}
$$

where $\alpha_{R}$ and $\beta_{R}$ are Rayleigh damping coefficients that can be defined from experiments.

## 4. Numerical results

In the following section, some comparison studies regarding the piezoelectric FG plates are carried out to prove the accuracy and stability of the present formulation before applying for piezoelectric FG metal foam plate reinforced by GPLs. In this study, the piezoelectric material layers are perfectly bonded on the top and bottom surfaces of the plate structure as well as ignored the adhesive layers. For the free vibration analysis, two electric boundary conditions are considered including a closed-circuit condition, in which the electric potentials are grounded and an open-circuit condition means that the electric potentials remain free. The Newmark's integration scheme is employed to solve the system of time-dependent equations. Meanwhile, for the active vibration control, the modal superposition is adopted to reduce the computational cost and the first six modes are considered in the modal space analysis. In addition, the initial modal damping ratio for each mode is assumed to be $0.8$ %. It is noted that the displacement feedback control gain $G_d$ is taken to be zero in this study.

### 4.1. Comparison studies

The accuracy and efficiency of present approach are verified by comparing the results of free and force vibration analyses for the piezoelectric FGM square plates with some other published approaches. Firstly, the free vibration analysis of a full simply supported (SSSS) piezoelectric FGM square plate is carried out to investigate the convergence. The piezoelectric FGM square plate is combined of $Al$ and $Al_2O_3$ while two PZT-4 piezoelectric layers are integrated on both the upper and the lower surfaces. All material properties of the metallic, ceramic and piezoelectric materials are given in Table 1. The thickness-to-width ratio $(h_c/a)$ of the FGM square plate is taken equal to 0.05 while the thickness of each piezoelectric layer is $h_p=0.1h_c$. The FGM plate is discretized using the polygonal elements with 4 mesh levels, as depicted Fig. 7.

Table 2 presents the convergence of the first natural frequencies of SSSS piezoelectric FGM plate with material index $n=1.0$. The present results are compared with those of the analytical Levy-type solutions based on FSDT, which are reported by Askari Farsangi and Saidi [68]. It can be seen that obtained results converge well to the analytical solutions for two electrical boundaries. Furthermore, the difference between two mesh levels 3 and 4 is not significant. Therefore, for a practical point of view, the mesh level 3 with 462 nodes is used to model the square plate for the rest of this study. Moreover, Table 3 depicts the three first natural frequencies of the piezoelectric FGM plate with various thickness-to-width ratios and material indices. The obtained results are also compared with those of the element-free IMLS-Ritz method using HSDT provided by Selim et al. [26]. It can be observed that the results which are generated from the proposed formulation are generally in good agreement with the reference solutions.

In the following example, the active control for dynamic responses of a SSSS FGM plate is conducted based on a constant velocity feedback control $G_v$ and a closed loop control. In this specific example, the FGM plate composed of Ti-6Al-4V and aluminum oxide materials with $n=2.0$ has the side length $a=b=0.2$ m, while thickness of FG core layer and each PZT-G1195N layer

are taken to be 1 mm and 0.1 mm, respectively. The FGM plate is initially subjected to a uniform load $f_s$=100 N/m² and then this load is suddenly removed. Fig. 8 shows the dynamic responses of the central deflection of the FGM plate using a constant velocity feedback control gain. It can be seen that the obtained results are in good agreement with the reference solutions which are generated based on a cell-based smoothed discrete shear gap method (CS-DSG3) and FSDT [27].

### 4.2. Free vibration analysis

In this section, the free vibration analysis of a SSSS piezoelectric FG plate with metal foam core layer which is constituted by combining of two porosity distributions and three GPL dispersion patterns, respectively, is considered. The plate has a side length $a = b = 1$ m, thickness of core layer $h_c = 50$ mm and thickness of each PZT-4 layer $h_p = 1$ mm. As the metal matrix, the copper whose material properties are listed in Table 1, is selected while the dimensions of GPLs are $l_{GPL}=2.5\ \mu m$, $w_{GPL}=1.5\ \mu m$, $t_{GPL}=1.5\ nm$. Table 4 shows the first natural frequencies of the piezoelectric FG metal foams plate reinforced by GPLs for different parameters including porosity distribution, porosity coefficient, dispersion pattern and weight fraction of GPLs as well as electrical boundary. As can be seen, when adding a small amount of GPLs into the metal matrix, the fundamental natural frequencies increase since the stiffness of the plate structure is significantly enhanced. Under the same the porosity distribution, porosity coefficient, GPL weight fraction and electrical condition, the GPL-S provides the best reinforced performance while the GPL-A is the lowest. In addition, the FG plate with metal foams distributed symmetry (PD-S) obtain the fundamental natural frequency higher than the other.

Fig. 9 illustrates the influence of the porosity coefficients on the fundamental natural frequencies of the FG metal foam plate with the weight fraction of the GPLs $\Lambda_{GPL}=1.0\ wt.\ \%$. In this specific example, thickness of metal foams core layer and each PZT-G1195N layer are $h_c = 10$ mm and $h_p = 0.1$ mm, respectively. It can be observed that, for the asymmetric porosity distribution (PD-A), an increasing porosity coefficients in metal matrix leads to the decrease the fundamental natural frequencies. This conclusion has been broadly recognized by most reports regarding the beam structures with or without GPLs [12, 13]. However, this rule seems not to be suitable for the symmetric porosity distribution (PD-S) with porosity coefficient $e_0\geq0.5$, which means the fundamental natural frequencies will not always decrease as the increase of porosity coefficients. Accordingly, with $e_0\leq0.5$, the natural frequencies will gradually decrease when the porosity coefficients increase while the natural frequencies suddenly increase if the porosity coefficient $e_0$ reaches higher values. The phenomenon also clearly appeared in Table 4 and was carefully explained by Gao et al. [17]. Moreover, for any particular porosity coefficient, the combination of PD-S and GPL-S always obtains the highest fundamental natural frequencies while the combination between PD-A and GPL-A provides the lowest ones.

Next, the effect of GPL weight fraction on the fundamental natural frequencies of FG metal foam plate with $e_0=0.5$, various porosity distributions and GPL dispersion patterns is also plotted in Fig. 10. For all the cases, the higher fundamental natural frequencies can obtain with an increase the GPL weight fraction in metal matrix. Again, the piezoelectric FG plates which

are constituted by PD-S and GPL-S have the best reinforcement effect for both open-circuit and closed-circuit electrical boundaries. In addition, Table 5 shows the six first natural frequencies of the FG metal foams plate where the thickness of core layer and each PZT-4 layer are $h_c=10$ mm and $h_p=1$ mm, respectively, with porosity coefficient $e_0=0.3$ and the weight fraction of the GPLs $\Lambda_{GPL}=1.0$ wt. $\%$. In this Table, the natural frequency increment between closed and open circuit conditions which is given as $\Delta=\frac{\omega_{open}-\omega_{closed}}{\omega_{closed}}$ is also considered and presented. Fig. 11 depicts the first six mode shapes of the piezoelectric FG metal foam plate with PD-S, GPL-S, porosity coefficient $e_0=0.3$ and weight fraction of GPLs $\Lambda_{GPL}=1.0$ wt. $\%$.

Finally, the free vibration analysis is carried out for a CCCC piezoelectric FG metal foam plate with a hole of complicated shape reinforced by GPLs to illustrate the robustness of the proposed approach when dealing with complex geometries. Fig. 12a depicts the geometry of the piezoelectric FG metal foam plate and its dimensions with thickness of core layer $h_c=50$ mm and the thickness of each PZT-4 layer $h_p=1$ mm. The FG metal foam plate with a complicated shape hole is discretized into polygonal elements with 584 nodes, as depicted in Fig. 12b. Table 6 shows the first natural frequencies of piezoelectric FG metal foam plate with different GPLs dispersion patterns and porosity distributions.

### 4.3. Forced vibration analysis
The dynamic responses of a SSSS piezoelectric FG metal foam plate reinforced with GPLs are exhaustively investigated in this section. The plate structure has a side length $a=b=0.2$ m with the thickness of core layer $h_c=10$ mm and each PZT-G1195N piezoelectric layer $h_p=0.1$ mm. Regarding the applied force, the FG plate is subjected to time-dependent distributed sinusoidal transverse load which are given as $f_s=q_0 sin(\pi x/a) sin(\pi y/b)F(t)$, where $F(t)$ is determined as

$$
F(t)=
\begin{cases}
\begin{cases}
1 & 0\leq t\leq t_1, \\
0 & t>t_1,
\end{cases} & \text{Step load} \\
\begin{cases}
1-t/t_1 & 0\leq t\leq t_1, \\
0 & t>t_1,
\end{cases} & \text{Triangular load} \\
\begin{cases}
\sin\left(\pi t/t_1\right) & 0\leq t\leq t_1, \\
0 & t>t_1,
\end{cases} & \text{Sinsoidal load} \\
e^{-\gamma t}, & \text{Explosive blast load}
\end{cases}
\tag{68}
$$

where $q_0=0.1$ MPa, $\gamma=330s^{-1}$. The time history $F(t)$ is plotted in Fig. 13.

The influence of the porosity coefficient on dynamic responses of the piezoelectric FG metal foam plate with PD-S and GPL-S ($\Lambda_{GPL}=1.0$ wt. $\%$) under step and triangular loads, respectively, is described in Fig. 14. It can be seen that by increasing the porosity coefficients, the amplitude of transverse deflection of the FG metal foam plate can be increased due to the reduction of stiffness of plate structure. Meanwhile, the period of motions do not seem to influence. In addition, Fig. 15 presents the effect of the weight fraction as well as the dispersion pattern of GPLs on the dynamic responses of the piezoelectric FG metal foams plate with $e_0=0.3$ and the PD-A corresponding to sinusoidal and explosive blast loads, respectively. As can be observed that the central deflection with a smaller magnitude can obtain when plate structures are reinforced

by a small amount of GPLs in metal matrix. More importantly, the dispersion of GPLs into the metal matrix significantly affects the reinforcing performance of structures. With the same weight fraction $(\Lambda_{GPL})$, the GPL-S with GPLs dispersed symmetric through the midplane always obtains the smallest deflection while the GPL-A provides the largest one.

Finally, the active vibration control for a CCCC FG metal foam plate reinforced with GPLs under a sinusoidally distributed transverse load is presented. The dimensions of FG metal foam plate are the same as the previous example. Furthermore, the combination of PD-S and GPL-S performed various advantages in reinforcement the stiffness of structures. As a result, in the last example, the metal foam core layer is constituted by this integration with $e_0=0.5$ and $\Lambda_{GPL}=$ 1.0 wt. %. Fig. 16 describes the amplitude of the central deflection for FG metal foam plate with respect to various the velocity feedback gains $G_v$ and loads. It can be observed that controlled by a higher velocity feedback gain cause the dynamic responses of structure can be suppressed more faster as well as the magnitude to be decreased. Furthermore, as the velocity feedback gain $G_v$ is equal to zero, means that the plate structures are uncontrolled, the dynamic responses still attenuate with respect to time due to the effect of structural damping. It can be concluded that the dynamic responses of the FG metal foam plate structures in terms of the deflection, oscillation time or even both can be actively controlled in order to satisfy an expectation by applying an appropriate value for the velocity feedback control gain. It should be noted that the feedback control gain values are restricted since each piezoelectric material has its own breakdown voltage value.

## 5. Conclusions

In this paper, an efficient computational approach, known as the improved polygonal element finite method (PFEM), was proposed to study the free vibration and dynamic responses as well as active control of FG metal foam plates with GPLs reinforcement and piezoelectric layers. The generalized $C^0$-HSDT in conjunction with quadratic serendipity shape functions over polygonal elements was applied to approximate the mechanical displacement field while the electric potential distribution through the thickness for each piezoelectric layer is assumed to vary linearly. The core layers which are compounded by two porosity distributions and three GPL dispersion patterns, respectively are carefully investigated through various related parameters. The control algorithm based on the constant velocity feedback was adopted to control the dynamic responses of the plate structures. Through the numerical results, several major remarks can be drawn as follows

- The present computational approach is valid for both thin and thick plates. Finite element meshes are flexible with an arbitrary number of edges, instead of limiting to the triangular and quadrilateral ones as the traditional finite element method. High accuracy of obtained results demonstrated the reliability of the proposed approach into analysis of metal foam structures reinforced with GPLs.

- The metal foam plate structures which have a good performance in weight reduction is significantly improved in terms of strength by adding a small amount of GPLs. Furthermore, the distribution of porosities and GPLs along the plate's thickness also affect significantly the reinforcing performance. It is found that the plate structures with symmetric porosity

distribution where internal pores are distributed on the midplane and GPL-S with GPLs dispersed around the top and bottom surfaces provide the best reinforcing performance.

- Depending on the porosity coefficients as well as the distribution of porosities and GPLs in metal matrix, the increase of porosity coefficient do not always induce the decrease of the natural frequencies.

- The dynamic responses of the FG metal foam plate can be expectantly controlled based on the velocity feedback control algorithm through a closed loop.

- Finally, the combination advantages of both the metal foam architecture and GPL reinforcement into engineering material is a good idea to provide the advanced ultra-light high-strength structures.

### Acknowledgements

The support provided by RISE-project BESTOFRAC (734370)-H2020 is gratefully acknowledged.

### References

[1] J. Banhart, Manufacture, characterisation and application of cellular metals and metal foams, Progress in materials science 46 (6) (2001) 559-632.

[2] A. Tampieri, G. Celotti, S. Sprio, A. Delcogliano, S. Franzese, Porosity-graded hydroxyapatite ceramics to replace natural bone, Biomaterials 22 (11) (2001) 1365-1370.

[3] L.-P. Lefebvre, J. Banhart, D. C. Dunand, Porous metals and metallic foams: current status and recent developments, Advanced Engineering Materials 10 (9) (2008) 775-787.

[4] C. Betts, Benefits of metal foams and developments in modelling techniques to assess their materials behaviour: a review, Materials Science and Technology 28 (2) (2012) 129-143.

[5] S. Iijima, Helical microtubules of graphitic carbon, nature 354 (6348) (1991) 56.

[6] P. Phung-Van, Q. X. Lieu, H. Nguyen-Xuan, M. A. Wahab, Size-dependent isogeometric analysis of functionally graded carbon nanotube-reinforced composite nanoplates, Composite Structures 166 (2017) 120-135.

[7] C.-L. Thanh, P. Phung-Van, C. H. Thai, H. Nguyen-Xuan, M. A. Wahab, Isogeometric analysis of functionally graded carbon nanotube reinforced composite nanoplates using modified couple stress theory, Composite Structures 184 (2018) 633-649.

[8] P. Phung-Van, C.-L. Thanh, H. Nguyen-Xuan, M. Abdel-Wahab, Nonlinear transient isogeometric analysis of fg-cntrc nanoplates in thermal environments, Composite Structures 201 (2018) 882-892.

[9] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, A. A. Firsov, Electric field effect in atomically thin carbon films, science 306 (5696) (2004) 666-669.

[10] M. A. Rafiee, J. Rafiee, Z. Wang, H. Song, Z.-Z. Yu, N. Koratkar, Enhanced mechanical properties of nanocomposites at low graphene content, ACS nano 3 (12) (2009) 3884-3890.

[11] I. Zaman, H.-C. Kuan, J. Dai, N. Kawashima, A. Michelmore, A. Sovi, S. Dong, L. Luong, J. Ma, From carbon nanotubes and silicate layers to graphene platelets for polymer nanocomposites, Nanoscale 4 (15) (2012) 4578-4586.

[12] S. Kitipornchai, D. Chen, J. Yang, Free vibration and elastic buckling of functionally graded porous beams reinforced by graphene platelets, Materials & Design 116 (2017) 656-665.

[13] D. Chen, J. Yang, S. Kitipornchai, Nonlinear vibration and postbuckling of functionally graded graphene reinforced porous nanocomposite beams, Composites Science and Technology 142 (2017) 235-245.

[14] Z. Liu, C. Yang, W. Gao, D. Wu, G. Li, Nonlinear behaviour and stability of functionally graded porous arches with graphene platelets reinforcements, International Journal of Engineering Science 137 (2019) 37-56.

[15] J. Yang, D. Chen, S. Kitipornchai, Buckling and free vibration analyses of functionally graded graphene rein- forced porous nanocomposite plates based on chebyshev-ritz method, Composite Structures 193 (2018) 281-294.

[16] K. Li, D. Wu, X. Chen, J. Cheng, Z. Liu, W. Gao, M. Liu, Isogeometric analysis of functionally graded porous plates reinforced by graphene platelets, Composite Structures 204 (2018) 114-130.

[17] K. Gao, W. Gao, D. Chen, J. Yang, Nonlinear free vibration of functionally graded graphene platelets reinforced porous nanocomposite plates resting on elastic foundation, Composite Structures 204 (2018) 831-846.

[18] Q. Li, D. Wu, X. Chen, L. Liu, Y. Yu, W. Gao, Nonlinear vibration and dynamic buckling analyses of sand- wich functionally graded porous plate with graphene platelet reinforcement resting on winkler-pasternak elastic foundation, International Journal of Mechanical Sciences 148 (2018) 596-610.

[19] L. B. Nguyen, N. V. Nguyen, C. H. Thai, A. Ferreira, H. Nguyen-Xuan, An isogeometric bézier finite element analysis for piezoelectric fg porous plates reinforced by graphene platelets, Composite Structures 214 (2019)227-245.

[20] Z. Wang, S.-h. Chen, W. Han, The static shape control for intelligent structures, Finite elements in analysis and design 26 (4) (1997) 303-314.

[21] X. He, T. Ng, S. Sivashanker, K. Liew, Active control of fgm plates with integrated piezoelectric sensors and actuators, International journal of Solids and Structures 38 (9) (2001) 1641-1655.

[22] K. Liew, S. Sivashanker, X. He, T. Ng, The modelling and design of smart structures using functionally graded materials and piezoelectrical sensor/actuator patches, Smart Materials and Structures 12 (4) (2003) 647.

[23] F. Ebrahimi, A. Rastgoo, Free vibration analysis of smart annular fgm plates integrated with piezoelectric layers, Smart Materials and Structures 17 (1) (2008) 015044.

[24] X. Zhang, Z. Kang, Dynamic topology optimization of piezoelectric structures with active control for reducing transient response, Computer Methods in Applied Mechanics and Engineering 281 (2014) 200-219.

[25] R. Talebitooti, K. Daneshjoo, S. Safari, Optimal control of laminated plate integrated with piezoelectric sensor and actuator considering tsdt and meshfree method, European Journal of Mechanics-A/Solids 55 (2016) 199-211.

[26] B. Selim, L. Zhang, K. Liew, Active vibration control of fgm plates with piezoelectric layers based on reddys higher-order shear deformation theory, Composite Structures 155 (2016) 118-134.

[27] K. Nguyen-Quang, H. Dang-Trung, V. Ho-Huu, H. Luong-Van, T. Nguyen-Thoi, Analysis and control of fgm plates integrated with piezoelectric sensors and actuators using cell-based smoothed discrete shear gap method(cs-dsg3), Composite Structures 165 (2017) 115-129.

[28] M. Keleshteri, H. Asadi, Q. Wang, Postbuckling analysis of smart fg-cntrc annular sector plates with surface- bonded piezoelectric layers using generalized differential quadrature method, Computer Methods in Applied Mechanics and Engineering 325 (2017) 689-710.

[29] M. Keleshteri, H. Asadi, Q. Wang, On the snap-through instability of post-buckled fg-cntrc rectangular plates with integrated piezoelectric layers, Computer Methods in Applied Mechanics and Engineering 331 (2018) 53-71.

[30] A. Alibeigloo, Static analysis of functionally graded carbon nanotube-reinforced composite plate embedded in piezoelectric layers by using theory of elasticity, Composite Structures 95 (2013) 612-622.

[31] A. Sharma, A. Kumar, C. Susheel, R. Kumar, Smart damping of functionally graded nanotube reinforced com- posite rectangular plates, Composite Structures 155 (2016) 29-44.

[32] B. Selim, L. Zhang, K. Liew, Active vibration control of cnt-reinforced composite plates with piezoelectric layers based on reddys higher-order shear deformation theory, Composite Structures 163 (2017) 350-364.

[33] K. Nguyen-Quang, T. Vo-Duy, H. Dang-Trung, T. Nguyen-Thoi, An isogeometric approach for dynamic re- sponse of laminated fg-cnt reinforced composite plates integrated with piezoelectric layers, Computer Methods in Applied Mechanics and Engineering 332 (2018) 25-46.

[34] P. Malekzadeh, A. Setoodeh, M. Shojaee, Vibration of fg-gpls eccentric annular plates embedded in piezoelec- tric layers using a transformed differential quadrature method, Computer Methods in Applied Mechanics and Engineering 340 (2018) 451-479.

[35] E. L. Wachspress, A rational finite element basis, Elsevier, 1975.

[36] J. Warren, Barycentric coordinates for convex polytopes, Advances in Computational Mathematics 6 (1) (1996) 97-108.

[37] M. Meyer, A. Barr, H. Lee, M. Desbrun, Generalized barycentric coordinates on irregular polygons, Journal of graphics tools 7 (1) (2002) 13-22.

[38] M. S. Floater, Mean value coordinates, Computer aided geometric design 20 (1) (2003) 19-27.

[39] K. Hormann, N. Sukumar, Maximum Entropy Coordinates for Arbitrary Polytopes, Computer Graphics Forum 27 (5) (2008) 1513-1520. doi:10.1111/j.1467-8659.2008.01292.x.

[40] N. Sukumar, A. Tabarraei, Conforming polygonal finite elements, International Journal for Numerical Methods in Engineering 61 (12) (2004) 2045-2066. doi:10.1002/nme.1141.

[41] J. Manson, S. Schaefer, Moving Least Squares Coordinates, Computer Graphics Forum 29 (5) (2010) 1517-1524. doi:10.1111/j.1467-8659.2010.01760.x.

[42] A. Rand, A. Gillette, C. Bajaj, Quadratic serendipity finite elements on polygons using generalized barycentric coordinates, Mathematics of computation 83 (290) (2014) 2691-2716.

[43] K. Y. Sze, N. Sheng, Polygonal finite element method for nonlinear constitutive modeling of polycrystalline ferroelectrics, Finite Elements in Analysis and Design 42 (2) (2005) 107-129. doi:10.1016/j.finel.2005.04.004.

[44] N. Sukumar, B. Moran, A. Yu Semenov, V. Belikov, Natural neighbour galerkin methods, International journal for numerical methods in engineering 50 (1) (2001) 1-27.

[45] A. Tabarraei, N. Sukumar, Extended finite element method on polygonal and quadtree meshes, Computer Meth- ods in Applied Mechanics and Engineering 197 (5) (2008) 425-438. doi:10.1016/j.cma.2007.08.013.

[46] H. Nguyen-Xuan, S. Nguyen-Hoang, T. Rabczuk, K. Hackl, A polytree-based adaptive approach to limit analysis of cracked structures, Computer Methods in Applied Mechanics and Engineering 313 (2017) 1006-1039. doi:10.1016/j.cma.2016.09.016.

[47] K. N. Chau, K. N. Chau, T. Ngo, K. Hackl, H. Nguyen-Xuan, A polytree-based adaptive polygonal finite element method for multi-material topology optimization, Computer Methods in Applied Mechanics and Engineering 332 (2018) 712-739.

[48] T. Vu-Huu, P. Phung-Van, H. Nguyen-Xuan, M. A. Wahab, A polytree-based adaptive polygonal finite element method for topology optimization of fluid-submerged breakwater interaction, Computers & Mathematics with Applications 76 (5) (2018) 1198-1218.

[49] H. Nguyen-Xuan, A polygonal finite element method for plate analysis, Computers & Structures 188 (2017) 45-62.

[50] N. V. Nguyen, H. X. Nguyen, D.-H. Phan, H. Nguyen-Xuan, A polygonal finite element method for laminated composite plates, International Journal of Mechanical Sciences 133 (2017) 863-882.

[51] N. V. Nguyen, H. X. Nguyen, S. Lee, H. Nguyen-Xuan, Geometrically nonlinear polygonal finite element anal- ysis of functionally graded porous plates, Advances in Engineering Software 126 (2018) 110-126.

[52] A. P. Roberts, E. J. Garboczi, Elastic moduli of model random three-dimensional closed-cell cellular solids, Acta materialia 49 (2) (2001) 189-197.

[53] A. Roberts, E. J. Garboczi, Computation of the linear elastic properties of random porous materials with a wide variety of microstructure, in: Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences, Vol. 458, The Royal Society, 2002, pp. 1033-1054.

[54] J. H. Affdl, J. Kardos, The halpin-tsai equations: a review, Polymer Engineering & Science 16 (5) (1976) 344-352.

[55] S. C. Tjong, Recent progress in the development and properties of novel metal matrix nanocomposites reinforced with carbon nanotubes and graphene nanosheets, Materials Science and Engineering: R: Reports 74 (10) (2013) 281-350.

[56] T. Nakamura, T. Wang, S. Sampath, Determination of properties of graded materials by inverse analysis and instrumented indentation, Acta Materialia 48 (17) (2000) 4293-4306.

[57] H. F. Tiersten, Linear Piezoelectric Plate Vibrations: Elements of the Linear Theory of Piezoelectricity and the Vibrations Piezoelectric Plates, Springer, 2013.

[58] H. Tzou, C. Tseng, Distributed piezoelectric sensor/actuator design for dynamic measurement/control of distributed parameter systems: a piezoelectric finite element approach, Journal of sound and vibration 138 (1) (1990) 17-34.

[59] W.-S. Hwang, H. C. Park, Finite element modeling of piezoelectric sensors and actuators, AIAA journal 31 (5) (1993) 930-937.

[60] M. Aydogdu, A new shear deformation theory for laminated composite plates, Composite structures 89 (1) (2009) 94-101.

[61] C. H. Thai, A. Ferreira, M. A. Wahab, H. Nguyen-Xuan, A moving kriging meshfree method with naturally stabilized nodal integration for analysis of functionally graded material sandwich plates, Acta Mechanica 229 (7) (2018) 2997-3023.

[62] J. Reddy, Analysis of functionally graded plates, International Journal for numerical methods in engineering 47 (1-3) (2000) 663-684.

[63] A. Soh, Z. Long, S. Cen, A new nine dof triangular element for analysis of thick and thin plates, Computational Mechanics 24 (5) (1999) 408-417.

[64] A.-K. Soh, S. Cen, Y.-Q. Long, Z.-F. Long, A new twelve dof quadrilateral element for analysis of thick and thin plates, European Journal of Mechanics-A/Solids 20 (2) (2001) 299-326.

[65] S. Wang, A finite element model for the static and dynamic analysis of a piezoelectric bimorph, International Journal of Solids and Structures 41 (15) (2004) 4075-4096.

[66] S. Wang, S. Quek, K. Ang, Vibration control of smart piezoelectric composite plates, Smart materials and Structures 10 (4) (2001) 637.

[67] G. Liu, K. Dai, K. Lim, Static and vibration control of composite laminates integrated with piezoelectric sensors and actuators using the radial point interpolation method, Smart materials and structures 13 (6) (2004) 1438.

[68] M. A. Farsangi, A. Saidi, Levy type solution for free vibration analysis of functionally graded rectangular plates with piezoelectric layers, Smart Materials and Structures 21 (9) (2012) 094017.

![](./images/843477285435604993_2.jpg)

Figure 1: Configuration of a piezoelectric FG metal foam plate reinforced by GPLs.

![](./images/843477285435604993_3.jpg)

Figure 3: Timoshenko's beam element.

![](./images/843477285435604993_4.jpg)

Figure 2: Porosity distributions and dispersion patterns of GPLs [17].

![](./images/843477285435604993_5.jpg)

Figure 4: The normal and tangential direction of each edge of polygonal element.

![](./images/843477285435604993_6.jpg)

![](./images/843477285435604993_7.jpg)

Figure 5: The quadratic serendipity shape functions of a pentagonal element.

![](./images/843477285435604993_8.jpg)

Figure 6: A schematic view of a FG metal foam plate integrated piezoelectric sensor and actuator.

![](./images/843477285435604993_9.jpg)

Figure 8: Dynamic response of the SSSS FG square plate with respect to various velocity feedback gains $G_v$.

![](./images/843477285435604993_10.jpg)

(a) Level 1

![](./images/843477285435604993_11.jpg)

(b) Level 2

![](./images/843477285435604993_12.jpg)

(c) Level 3

![](./images/843477285435604993_13.jpg)

(d) Level 4

Figure 7: Polygonal meshes of a piezoelectric FG square plate.

![](./images/843477285435604993_14.jpg)

(a) Closed-circuit

![](./images/843477285435604993_15.jpg)

(b) Open-circuit

Figure 9: Effect of porosity coefficient on the natural frequencies of piezoelectric FG metal foam plate with $\Lambda_{GPL}=1.0$ wt. $\%$.

![](./images/843477285435604993_16.jpg)

Figure 10: Effect of GPL weight fraction on the natural frequencies of piezoelectric FG metal foam plate with $e_0 = 0.5$.

![](./images/843477285435604993_17.jpg)

Figure 11: First six shapes of the piezoelectric FG metal foam plate under PD-S and GPL-S $(e_0 = 0.3,\ \Lambda_{GPL} = 1.0\ wt.\ \%)$.

![](./images/843477285435604993_18.jpg)

Figure 12: A geometry and polygonal mesh of a piezoelectric FG metal foam square plate with complicated shape hole.

![](./images/843477285435604993_19.jpg)

Figure 13: Time history of load factor.

![](./images/843477285435604993_20.jpg)

(a) Step load

![](./images/843477285435604993_21.jpg)

(b) Triangular load

Figure 14: Effect of the porosity coefficient on dynamic responses of the SSSS piezoelectric FG metal foam plate with PD-S and GPL-S $(\Lambda_{GPL}=1.0$ wt. $\%)$.

![](./images/843477285435604993_22.jpg)

(a) Sinusoidal load

![](./images/843477285435604993_23.jpg)

(b) Explosive blast load

Figure 15: Effect of the weight fraction and dispersion pattern of GPLs on dynamic responses of the SSSS piezoelectric FG metal foam plate with PD-A ($e_0=0.3$).

![](./images/843477285435604993_24.jpg)

(a) Step load

![](./images/843477285435604993_25.jpg)

(b) Triangular load

![](./images/843477285435604993_26.jpg)

(c) Sinusoidal load

![](./images/843477285435604993_27.jpg)

(d) Explosive blast load

Figure 16: Effect of the velocity feedback control gain $G_v$ on dynamic responses of the CCCC piezoelectric FG metal foam plate subjected to various dynamic loads.

Table 2: The first natural frequencies (Hz) of the SSSS piezoelectric FG square plate with various mesh levels.

<table>
  <thead>
    <tr>
      <th rowspan="2">Mesh level</th>
      <th colspan="3">Closed</th>
      <th colspan="3">Open</th>
    </tr>
    <tr>
      <th>Present</th>
      <th>Analytical [68]</th>
      <th>Error (%)</th>
      <th>Present</th>
      <th>Analytical [68]</th>
      <th>Error (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 (138 nodes)</td>
      <td>344.963</td>
      <td>339.859</td>
      <td>1.502</td>
      <td>353.511</td>
      <td>350.092</td>
      <td>0.977</td>
    </tr>
    <tr>
      <td>2 (212 nodes)</td>
      <td>343.764</td>
      <td></td>
      <td>1.149</td>
      <td>352.351</td>
      <td></td>
      <td>0.645</td>
    </tr>
    <tr>
      <td>3 (462 nodes)</td>
      <td>342.691</td>
      <td></td>
      <td>0.833</td>
      <td>351.310</td>
      <td></td>
      <td>0.348</td>
    </tr>
    <tr>
      <td>4 (630 nodes)</td>
      <td>342.398</td>
      <td></td>
      <td>0.747</td>
      <td>351.024</td>
      <td></td>
      <td>0.266</td>
    </tr>
    <tr>
      <td colspan="7">$\text{Error} = \frac{\text{Present value}-\text{Analytical value}}{\text{Analytical value}} \times 100\%$</td>
    </tr>
  </tbody>
</table>

Table 1: Material properties of the core and piezoelectric layers ($\varepsilon_0 = 8.85 \times 10^{-12}$ F/m).

<table>
<thead>
<tr>
<th>Properties</th>
<th colspan="6">Core layer</th>
<th colspan="2">Piezoelectric layer</th>
</tr>
<tr>
<th></th>
<th>Al</th>
<th>$\text{Al}_2\text{O}_3$</th>
<th>Ti-6Al-4V</th>
<th>Aluminum oxide</th>
<th>Copper</th>
<th>GPLs</th>
<th>PZT-4</th>
<th>PZT-G1195N</th>
</tr>
</thead>
<tbody>
<tr>
<td>Elastic properties</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$E_{11}$ (GPa)</td>
<td>70</td>
<td>380</td>
<td>105.70</td>
<td>320.24</td>
<td>130</td>
<td>1010</td>
<td>81.3</td>
<td>63.0</td>
</tr>
<tr>
<td>$E_{22}$ (GPa)</td>
<td>70</td>
<td>380</td>
<td>105.70</td>
<td>320.24</td>
<td>130</td>
<td>1010</td>
<td>81.3</td>
<td>63.0</td>
</tr>
<tr>
<td>$E_{33}$ (GPa)</td>
<td>70</td>
<td>380</td>
<td>105.70</td>
<td>320.24</td>
<td>130</td>
<td>1010</td>
<td>64.5</td>
<td>63.0</td>
</tr>
<tr>
<td>$G_{12}$ (GPa)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>30.6</td>
<td>24.2</td>
</tr>
<tr>
<td>$G_{13}$ (GPa)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>25.6</td>
<td>24.2</td>
</tr>
<tr>
<td>$G_{23}$ (GPa)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>25.6</td>
<td>24.2</td>
</tr>
<tr>
<td>$\nu_{12}$</td>
<td>0.3</td>
<td>0.3</td>
<td>0.2981</td>
<td>0.26</td>
<td>0.34</td>
<td>0.186</td>
<td>0.33</td>
<td>0.30</td>
</tr>
<tr>
<td>$\nu_{13}$</td>
<td>0.3</td>
<td>0.3</td>
<td>0.2981</td>
<td>0.26</td>
<td>0.34</td>
<td>0.186</td>
<td>0.43</td>
<td>0.30</td>
</tr>
<tr>
<td>$\nu_{23}$</td>
<td>0.3</td>
<td>0.3</td>
<td>0.2981</td>
<td>0.26</td>
<td>0.34</td>
<td>0.186</td>
<td>0.43</td>
<td>0.30</td>
</tr>
<tr>
<td>Mass density</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\rho$ ($\text{kg/m}^3$)</td>
<td>2702</td>
<td>3800</td>
<td>4429</td>
<td>3750</td>
<td>8960</td>
<td>1062.5</td>
<td>7600</td>
<td>7600</td>
</tr>
<tr>
<td>Piezoelectric coefficients</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$k_{31}$ (m/V)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>$-1.22 \times 10^{-10}$</td>
<td>$254 \times 10^{-12}$</td>
</tr>
<tr>
<td>$k_{32}$ (m/V)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>$-1.22 \times 10^{-10}$</td>
<td>$254 \times 10^{-12}$</td>
</tr>
<tr>
<td>Electric permittivity</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$p_{11}$ (F/m)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>$1475\varepsilon_0$</td>
<td>$15.3 \times 10^{-9}$</td>
</tr>
<tr>
<td>$p_{22}$ (F/m)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>$1475\varepsilon_0$</td>
<td>$15.3 \times 10^{-9}$</td>
</tr>
<tr>
<td>$p_{33}$ (F/m)</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>—</td>
<td>$1300\varepsilon_0$</td>
<td>$15.3 \times 10^{-9}$</td>
</tr>
</tbody>
</table>

Table 3: The first three natural frequencies (Hz) of the SSSS piezoelectric FG square plate with different conditions.

<table>
<thead>
<tr>
<th>$h/a$</th>
<th>Electrical
condition</th>
<th>Mode</th>
<th colspan="3">$n=0.0$</th>
<th colspan="3">$n=0.5$</th>
<th colspan="3">$n=2.0$</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>Present</th>
<th>IMLS
Ritz[26]</th>
<th>Analytical
[68]</th>
<th>Present</th>
<th>IMLS
Ritz[26]</th>
<th>Analytical
[68]</th>
<th>Present</th>
<th>IMLS
Ritz[26]</th>
<th>Analytical
[68]</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.05</td>
<td>Closed</td>
<td>(1,1)</td>
<td>428.885</td>
<td>424.907</td>
<td>426.662</td>
<td>371.633</td>
<td>367.575</td>
<td>369.015</td>
<td>320.102</td>
<td>315.716</td>
<td>317.135</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(1,2)</td>
<td>1056.726</td>
<td>1046.812</td>
<td>1049.356</td>
<td>916.249</td>
<td>906.103</td>
<td>907.918</td>
<td>787.201</td>
<td>776.889</td>
<td>779.313</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(2,2)</td>
<td>1667.141</td>
<td>1647.337</td>
<td>1652.929</td>
<td>1446.531</td>
<td>1426.750</td>
<td>1430.642</td>
<td>1239.573</td>
<td>1221.231</td>
<td>1226.615</td>
</tr>
<tr>
<td></td>
<td>Open</td>
<td>(1,1)</td>
<td>434.874</td>
<td>432.151</td>
<td>433.747</td>
<td>379.159</td>
<td>376.685</td>
<td>377.934</td>
<td>329.839</td>
<td>327.535</td>
<td>328.724</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(1,2)</td>
<td>1071.133</td>
<td>1062.196</td>
<td>1066.390</td>
<td>934.374</td>
<td>925.467</td>
<td>929.406</td>
<td>810.511</td>
<td>801.917</td>
<td>807.162</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(2,2)</td>
<td>1689.272</td>
<td>1668.387</td>
<td>1679.191</td>
<td>1474.415</td>
<td>1453.265</td>
<td>1463.819</td>
<td>1275.207</td>
<td>1255.391</td>
<td>1269.525</td>
</tr>
<tr>
<td>0.1</td>
<td>Closed</td>
<td>(1,1)</td>
<td>827.343</td>
<td>822.704</td>
<td>826.463</td>
<td>717.840</td>
<td>712.541</td>
<td>715.319</td>
<td>615.319</td>
<td>609.894</td>
<td>613.305</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(1,2)</td>
<td>1906.338</td>
<td>1948.947</td>
<td>1952.530</td>
<td>1661.371</td>
<td>1691.326</td>
<td>1691.992</td>
<td>1410.556</td>
<td>1439.945</td>
<td>1445.353</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(2,2)</td>
<td>2744.670</td>
<td>2965.790</td>
<td>2974.440</td>
<td>2409.402</td>
<td>2577.999</td>
<td>2580.078</td>
<td>2031.625</td>
<td>2186.014</td>
<td>2197.887</td>
</tr>
<tr>
<td></td>
<td>Open</td>
<td>(1,1)</td>
<td>838.588</td>
<td>836.423</td>
<td>839.595</td>
<td>731.985</td>
<td>729.808</td>
<td>731.920</td>
<td>633.385</td>
<td>632.104</td>
<td>634.772</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(1,2)</td>
<td>1930.704</td>
<td>1976.195</td>
<td>1981.321</td>
<td>1692.145</td>
<td>1725.670</td>
<td>1728.702</td>
<td>1448.483</td>
<td>1483.560</td>
<td>1492.484</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(2,2)</td>
<td>2776.269</td>
<td>3001.279</td>
<td>3015.610</td>
<td>2449.726</td>
<td>2622.761</td>
<td>2693.452</td>
<td>2079.403</td>
<td>2242.320</td>
<td>2265.315</td>
</tr>
</tbody>
</table>

Table 4: The first natural frequencies (Hz) of the SSSS piezoelectric FG metal foam plate reinforced by GPLs.

<table>
<thead>
<tr>
<th>GPL</th>
<th>GPL weight</th>
<th>Electrical</th>
<th colspan="4">PD-S</th>
<th colspan="3">PD-A</th>
</tr>
<tr>
<th>pattern</th>
<th>fraction (%)</th>
<th>condition</th>
<th>$e_0=0.0$</th>
<th>$e_0=0.2$</th>
<th>$e_0=0.4$</th>
<th>$e_0=0.6$</th>
<th>$e_0=0.2$</th>
<th>$e_0=0.4$</th>
<th>$e_0=0.6$</th>
</tr>
</thead>
<tbody>
<tr>
<td>GPL-S</td>
<td>0.0</td>
<td>Closed</td>
<td>185.954</td>
<td>184.975</td>
<td>184.692</td>
<td>185.618</td>
<td>180.38</td>
<td>173.628</td>
<td>164.676</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>187.325</td>
<td>186.442</td>
<td>186.272</td>
<td>187.341</td>
<td>181.889</td>
<td>175.333</td>
<td>166.693</td>
</tr>
<tr>
<td></td>
<td>0.5</td>
<td>Closed</td>
<td>226.503</td>
<td>224.939</td>
<td>223.977</td>
<td>224.051</td>
<td>219.380</td>
<td>210.550</td>
<td>198.541</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>227.663</td>
<td>226.181</td>
<td>225.319</td>
<td>225.519</td>
<td>220.660</td>
<td>212.004</td>
<td>200.282</td>
</tr>
<tr>
<td></td>
<td>1.0</td>
<td>Closed</td>
<td>260.176</td>
<td>258.178</td>
<td>256.726</td>
<td>256.210</td>
<td>251.833</td>
<td>241.340</td>
<td>226.838</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>261.217</td>
<td>259.293</td>
<td>257.932</td>
<td>257.531</td>
<td>252.982</td>
<td>242.650</td>
<td>228.418</td>
</tr>
<tr>
<td>GPL-A</td>
<td>0.5</td>
<td>Closed</td>
<td>211.677</td>
<td>210.361</td>
<td>209.757</td>
<td>210.401</td>
<td>204.348</td>
<td>195.498</td>
<td>183.965</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>212.937</td>
<td>211.712</td>
<td>211.217</td>
<td>211.999</td>
<td>205.753</td>
<td>197.109</td>
<td>185.905</td>
</tr>
<tr>
<td></td>
<td>1.0</td>
<td>Closed</td>
<td>231.014</td>
<td>229.307</td>
<td>228.288</td>
<td>228.488</td>
<td>222.456</td>
<td>212.161</td>
<td>198.880</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>232.228</td>
<td>230.612</td>
<td>229.705</td>
<td>230.046</td>
<td>223.819</td>
<td>213.734</td>
<td>200.789</td>
</tr>
<tr>
<td>GPL-U</td>
<td>0.5</td>
<td>Closed</td>
<td>211.560</td>
<td>210.346</td>
<td>209.900</td>
<td>210.802</td>
<td>205.052</td>
<td>197.155</td>
<td>186.657</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>212.810</td>
<td>211.684</td>
<td>211.343</td>
<td>212.376</td>
<td>206.430</td>
<td>198.714</td>
<td>188.504</td>
</tr>
<tr>
<td></td>
<td>1.0</td>
<td>Closed</td>
<td>234.182</td>
<td>232.775</td>
<td>232.200</td>
<td>233.094</td>
<td>226.877</td>
<td>217.998</td>
<td>206.171</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>235.351</td>
<td>234.027</td>
<td>233.551</td>
<td>234.568</td>
<td>228.166</td>
<td>219.457</td>
<td>207.904</td>
</tr>
</tbody>
</table>

Table 5: The first six natural frequencies (Hz) of the SSSS piezoelectric FG square plate with different conditions.

<table>
<thead>
<tr>
<th>Mode</th>
<th colspan="3">GPL-S</th>
<th colspan="3">GPL-A</th>
<th colspan="3">GPL-U</th>
</tr>
<tr>
<th></th>
<th>Closed</th>
<th>Open</th>
<th>$\Delta\%$</th>
<th>Closed</th>
<th>Open</th>
<th>$\Delta\%$</th>
<th>Closed</th>
<th>Open</th>
<th>$\Delta\%$</th>
</tr>
</thead>
<tbody>
<tr>
<td>PD-S</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>53.511</td>
<td>54.674</td>
<td>2.173</td>
<td>48.619</td>
<td>49.924</td>
<td>2.684</td>
<td>49.116</td>
<td>50.382</td>
<td>2.578</td>
</tr>
<tr>
<td>2</td>
<td>134.004</td>
<td>136.898</td>
<td>2.160</td>
<td>121.809</td>
<td>125.059</td>
<td>2.668</td>
<td>123.053</td>
<td>126.205</td>
<td>2.561</td>
</tr>
<tr>
<td>3</td>
<td>134.053</td>
<td>136.948</td>
<td>2.160</td>
<td>121.854</td>
<td>125.105</td>
<td>2.668</td>
<td>123.099</td>
<td>126.251</td>
<td>2.561</td>
</tr>
<tr>
<td>4</td>
<td>214.735</td>
<td>219.337</td>
<td>2.143</td>
<td>195.289</td>
<td>200.463</td>
<td>2.649</td>
<td>197.280</td>
<td>202.298</td>
<td>2.544</td>
</tr>
<tr>
<td>5</td>
<td>268.693</td>
<td>274.423</td>
<td>2.133</td>
<td>244.439</td>
<td>250.886</td>
<td>2.637</td>
<td>246.930</td>
<td>253.183</td>
<td>2.532</td>
</tr>
<tr>
<td>6</td>
<td>268.928</td>
<td>274.657</td>
<td>2.130</td>
<td>244.657</td>
<td>251.105</td>
<td>2.636</td>
<td>247.150</td>
<td>253.403</td>
<td>2.530</td>
</tr>
<tr>
<td>PD-A</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td>51.691</td>
<td>52.900</td>
<td>2.339</td>
<td>46.816</td>
<td>48.187</td>
<td>2.928</td>
<td>47.485</td>
<td>48.798</td>
<td>2.765</td>
</tr>
<tr>
<td>2</td>
<td>129.469</td>
<td>132.479</td>
<td>2.325</td>
<td>117.311</td>
<td>120.727</td>
<td>2.912</td>
<td>118.984</td>
<td>122.253</td>
<td>2.747</td>
</tr>
<tr>
<td>3</td>
<td>129.516</td>
<td>132.527</td>
<td>2.325</td>
<td>117.355</td>
<td>120.771</td>
<td>2.911</td>
<td>119.028</td>
<td>122.298</td>
<td>2.747</td>
</tr>
<tr>
<td>4</td>
<td>207.506</td>
<td>212.294</td>
<td>2.307</td>
<td>188.108</td>
<td>193.550</td>
<td>2.893</td>
<td>190.784</td>
<td>195.991</td>
<td>2.729</td>
</tr>
<tr>
<td>5</td>
<td>259.679</td>
<td>265.642</td>
<td>2.296</td>
<td>235.477</td>
<td>242.260</td>
<td>2.880</td>
<td>238.823</td>
<td>245.312</td>
<td>2.717</td>
</tr>
<tr>
<td>6</td>
<td>259.908</td>
<td>265.871</td>
<td>2.294</td>
<td>235.688</td>
<td>242.472</td>
<td>2.878</td>
<td>239.037</td>
<td>245.527</td>
<td>2.715</td>
</tr>
</tbody>
</table>

Table 6: The first natural frequencies (Hz) of the CCCC piezoelectric FG metal foam plate with complicated shape hole reinforced by GPLs.

<table>
<thead>
<tr>
<th>GPL pattern</th>
<th>GPL weight fraction (%)</th>
<th>Electrical condition</th>
<th colspan="4">PD-S</th>
<th colspan="3">PD-A</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$e_0=0.0$</th>
<th>$e_0=0.3$</th>
<th>$e_0=0.5$</th>
<th>$e_0=0.7$</th>
<th>$e_0=0.3$</th>
<th>$e_0=0.5$</th>
<th>$e_0=0.7$</th>
</tr>
</thead>
<tbody>
<tr>
<td>GPL-S</td>
<td>0.0</td>
<td>Closed</td>
<td>805.134</td>
<td>794.049</td>
<td>787.516</td>
<td>781.828</td>
<td>769.823</td>
<td>738.376</td>
<td>693.824</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>808.156</td>
<td>797.319</td>
<td>790.953</td>
<td>785.415</td>
<td>773.385</td>
<td>742.511</td>
<td>698.969</td>
</tr>
<tr>
<td></td>
<td>1.0</td>
<td>Closed</td>
<td>1104.946</td>
<td>1082.612</td>
<td>1066.042</td>
<td>1046.436</td>
<td>1051.926</td>
<td>1003.302</td>
<td>932.303</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>1107.121</td>
<td>1084.965</td>
<td>1068.525</td>
<td>1049.053</td>
<td>1054.502</td>
<td>1006.338</td>
<td>936.221</td>
</tr>
<tr>
<td>GPL-A</td>
<td>1.0</td>
<td>Closed</td>
<td>1005.851</td>
<td>988.82</td>
<td>977.757</td>
<td>966.788</td>
<td>951.711</td>
<td>904.34</td>
<td>839.762</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>1008.595</td>
<td>991.816</td>
<td>980.932</td>
<td>970.144</td>
<td>955.058</td>
<td>908.339</td>
<td>844.892</td>
</tr>
<tr>
<td>GPL-U</td>
<td>1.0</td>
<td>Closed</td>
<td>1019.125</td>
<td>1003.897</td>
<td>994.72</td>
<td>986.542</td>
<td>972.206</td>
<td>930.438</td>
<td>871.078</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Open</td>
<td>1021.761</td>
<td>1006.753</td>
<td>997.726</td>
<td>989.686</td>
<td>975.317</td>
<td>934.061</td>
<td>875.618</td>
</tr>
</tbody>
</table>