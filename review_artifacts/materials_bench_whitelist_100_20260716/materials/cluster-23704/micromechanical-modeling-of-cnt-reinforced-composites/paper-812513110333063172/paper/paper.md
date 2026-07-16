![](./images/812513110333063172_1.jpg)

# Mechanics of Advanced Materials and Structures

ISSN: (Print) (Online) Journal homepage: https://www.tandfonline.com/loi/umcm20

## The free vibration response of temperature-dependent carbon nanotube-reinforced composite stiffened plate

Pabitra Maji , Mrutyunjay Rout & Amit Karmakar

To cite this article: Pabitra Maji , Mrutyunjay Rout & Amit Karmakar (2021): The free vibration response of temperature-dependent carbon nanotube-reinforced composite stiffened plate, Mechanics of Advanced Materials and Structures, DOI: 10.1080/15376494.2020.1870782

To link to this article: https://doi.org/10.1080/15376494.2020.1870782

![](./images/812513110333063172_2.jpg)
Published online: 16 Jan 2021.

![](./images/812513110333063172_3.jpg)
Submit your article to this journal ![](./images/812513110333063172_4.jpg)

![](./images/812513110333063172_5.jpg)
Article views: 83

![](./images/812513110333063172_6.jpg)
View related articles ![](./images/812513110333063172_7.jpg)

![](./images/812513110333063172_8.jpg)
View Crossmark data ![](./images/812513110333063172_9.jpg)

![](./images/812513110333063172_10.jpg)
Citing articles: 1 View citing articles ![](./images/812513110333063172_11.jpg)

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=umcm20

ORIGINAL ARTICLE

# The free vibration response of temperature-dependent carbon nanotube-reinforced composite stiffened plate

Pabitra Maji$^{a}$, Mrutyunjay Rout$^{b}$, and Amit Karmakar$^{a}$

$^{a}$Mechanical Engineering Department, Jadavpur University, Kolkata, India; $^{b}$Department of Mechanical Engineering, Government College of Engineering, Bhawanipatna, India

## ABSTRACT
In this present investigation, an eight-nodded isoparametric finite element method is used to model the geometry of the stiffened plate based on first-order shear deformation theory. Three nodded isoparametric beam elements with four degrees of freedom per node are employed to model the stiffener's geometry. The carbon nanotubes are distributed through the thickness direction of the stiffened plate. The generalized dynamic equilibrium equation is derived from Lagrange's equation of motion using minimum potential energy. The significance of stiffeners addition, stiffeners dimension, aspect ratio, thickness ratio, boundary conditions, fiber volume fraction and temperature on the natural frequency is scrutinized in detail.

## ARTICLE HISTORY
Received 26 December 2020
Accepted 27 December 2020

## KEYWORDS
Plate; carbon nanotubes (CNTs); vibration; stiffeners; thermal environments; FEM.

## 1. Introduction
The advancement material like carbon nanotubes (CNTs) has received immense attention as reinforcement in the last decades. It has extraordinary mechanical, electrical, and thermal properties when compared with polymeric and metallic reinforcement, which make them ideal candidates as reinforcement. The addition of a small fraction of CNTs can enhance the significant amount of the thermal, mechanical, and electrical properties of the composition. The successful applications of CNTs are already received in aerospace, civil, nuclear, automobiles industries, and other high-performance applications. CNTs have high specific stiffness, strength, low specific weight, better damping, and shock-absorbing capacity. Stiffeners are secondary beams or sections attached to the plate on one side of the plate or both sides to better the dynamic performance. The stiffened plate has higher load delivery ability than the unstiffened plate with the same weight, making a reasonable structure. The stiffeners can be oriented in longitudinal direction and transverse directions. The stiffeners addition increases the mass, as well as the stiffness of the plate. It is also revealed that the first and second moments of inertia of the CNT-reinforced composite plates boost due to stiffeners' adding. The various type stiffeners such as I, T, Z, inverted T type section have so far been utilized in aircraft and ship structures equally in metallic and composite construction. The simple flat beam stiffener is the type almost constantly used in modern designs.

In the past few decades, the stiffened structures have been used increasingly in the various structural fields. Nayak and Bandyopadhyay [1] investigated the free vibration response of stiffened composite plates based on finite defer-ence methods. Chattopadhyay et al. [2] used a finite element method (FEM) to perform the stiffened laminated plate's free vibration. Harik and Guo [3] utilized the FEM to study the free vibrations of the eccentrically stiffened plate. Mukherjee and Mukhopadhyay [4] examined the free vibration of stiffened rectangular skew plates using FEM. Ghosh and Biswal [5] examined the free vibration response of a stiffened composite plate based on HSDT using FEM. Zeng and Bert [6] applied the FEM and Rayleigh-Ritz method to scrutinize the modal analysis of the orthogonal stiffened skew plate. Nayak and Bandyopadhyay [7] studied the free vibration of laminated stiffened shells based on FEM, in which X- and Y-directional stiffeners used. Based on FEM, Rajawat et al. [8] calculated the free vibrations of the laminated eccentric stiffened plate. A mesh-free Galerkin method was utilized by Peng et al. [9] to observe the free vibration and stability of stiffened plates based on the FSDT. Wang et al. [10] studied the nonlinear vibration of a stiffened plate. Some notable literature related to the free vibration of the stiffened plate was investigated by Rout and Karmakar [11], Xue and Wang [12], Zhang and Lin [13], Alaimo et al. [14], Mandal et al. [15], Sinha et al. [16], Dat et al. [17], and Mirjavadi et al. [18]. Later on, using standard FEM, Nayak et al. [19] also scrutinized the free vibration of a stiffened plate based on FSDT. Sahoo and Barlik [20] generated the natural frequency of a laminated stiffened plate based on FEM in which concentrically and eccentrically stiffeners are considered. Later on, Nguyen and Hoang [21], Rout et al. [22], Tran et al. [23], and Zarei et al. [24], predicted the free vibration response of stiffened shell panels.

---

**CONTACT** Pabitra Maji 📧 pabitrajumech2@gmail.com; Amit Karmakar 📧 shrikatha@yahoo.co.in 📍 Mechanical Engineering Department, Jadavpur University, Kolkata, India.

© 2021 Taylor & Francis Group, LLC

Milazzo and Oliveri [25] investigated the buckling and post-buckling of stiffened panels based on the First-order shear deformation theory using Ritz approach. In this study, the von-karmon non-linearity also considered. Based on the Rayleigh-Ritz approach, Oliveri et al. [26] scrutinized the non-linear post buckling of variable angle tow composite stiffened plate using FSDT theory under the thermal environment. Liu et al. [27] validated the numerical and experimental results of free vibration, static and dynamic behavior of curvilinear stiffened plated. Jafarpour and Khedmati [28] used conventional and super FEMs to study the modal responses of eccentric stiffened plates. The Von Karman non-linearity was worked out using arc-length method. Sinha et al. [16] examined the free vibration of composite stiffened plate using FEM and also validated the experimental and numerical results. Vescovini et al. [29] utilized the semi-analytical approach to characteristics the modal and buckling responses of curvilinear stiffened panels. The curvilinear stiffeners are modeled as 1D beam elements. Zhou et al. [30] proposed the semi-analytical method to study the vibro acoustic behavior of stiffened plates under time-harmonic excitations. Recently Sciascia et al. [31] studied the modal and transient responses of Variable-Stiffness Shell Structures based on the Ritz technique by incorporating first-order shear deformation theory. The Legendre orthogonal polynomials used to modeled the unknown displacement fields.

Liu et al. [32] used arbitrary boundary conditions to discover the free vibration of the variable thickness orthotropic plate using Galerkin's method. Bahmyari and Rahbar-Ranji [33] scrutinized the natural frequency of orthotropic plate with general boundary conditions using an element free Galerkin method. Later on Shi et al. [34] utilized the arbitrary boundary conditions to learn modal characteristics of moderate thick plate based on the Rayleigh-Ritz method using FSDT. In recent times, Guo and Feng [35] applied the improved Rayleigh-Ritz technique to observe the free vibrations of arbitrary shape plate with different boundary conditions.

Shen and Zhang [36] analyzed the buckling and post-buckling of FG-carbon nanotube-reinforced composites (CNTRCs) plate in the thermal environments using a multi-scale approach. Lei et al. [37] applied the element-free kp-Ritz method to investigate the free vibration of temperature-dependent CNTs reinforced composite plate using FSDT. Natarajan et al. [38] developed a new higher-order structural theory to perform the static and free vibration of CNTs face sheet sandwich plates. Malekzadeh and Zarei [39] used an FSDT to investigate the vibration characteristics of CNTs reinforced composite plate based on the differential quadrature method (DQM). Zhang et al. [40, 41] investigated the free vibration of CNTs reinforced composite plate in the thermal environments. Zhang et al. [42] also investigated the free vibration of FG-CNT moderately thick rectangular plates with edges elastic foundations based on the element-free improved moving least-squares Ritz (IMLS-Ritz) method using FSDT. Lei et al. [43, 44] developed kp-Ritz method to predict the vibration frequency analysis of FG-CNT reinforced composite rectangular plates. Moradi-Dastjerdi et al. [45] developed a refined plate theory to analyze the free vibration characteristics of CNTs sandwich plate resting on the Elastic Foundation. Mehar and Panda [46] examine the free vibration performance of the CNTs plate using HSDT based on FEM. Selim et al. [47] considered the active vibration behavior of the CNTs plate using HSDT. Kiani [48] measured the free vibration of CNTs reinforced composite skew plates based on the Ritz method in the thermal environment. Civalek [49] studied the free vibration characteristics of CNTs' neno-plates and shells in the thermal field based on the discrete singular convolution method. The free vibration study of FG-CNTRC annular plates was demonstrated by Torabi and Ansari [50], in the thermal field. Maji et al. [51, 52] used the FEM to explore the free vibration of CNTs reinforced conical shell panels based on FSDT. Qin et al. [53] discussed the free vibration response of CNTs rotating cylindrical shells with general boundary conditions using Chebyshev polynomials. Patel et al. [54] scrutinized the free vibration characteristics of CNTs plates based on the experimental and numerical methods. Civalek and Jalaei [55, 56] presented the vibration of CNTs reinforced quadrilateral and skew plate under the thermal environments. Tran et al. [57] developed a four-variable refined plate theory to predict the bending study of CNTs reinforced with integrated piezoelectric patch composite plates. Recently, Van Do et al. [58, 59], Selim et al. [60], and Dat et al. [17] studied the free vibration and dynamic response to CNTs plate in the thermal fields.

According to the author's knowledge, there is no article associated with the free vibration performance of CNTRC-stiffened plates in the thermal environments. To fill up this apparent empty space, the present assessment is carried out to study the free vibration performance of CNTRC-stiffened plate based on first-order shear deformation theory. The analysis has been worked out using an eight-noded isoparametric plate bending element. The stiffeners are modeled with a three-noded beam element. The originality of the present method is that there no further increase in degrees of freedom of the shell due to addition of stiffeners, which increases the computational proficiency as compare to the commercially available software. A constraint method is used to tie the nodal degrees of freedom of the stiffener with that of the shells together by considering eccentricity and wrapping effect. The limitation of the method is that the CNT reinforced stiffeners are required to place along the nodal lines of the shell only. In this investigation, four different graded CNTs distribution are assumed, which are dispersed through the depth of the CNTRC-stiffened plate. The influence of the number of stiffeners, stiffeners width, stiffeners thickness, aspect ratio, thickness ratio, boundary conditions, and temperature on the natural frequency is calculated in detail.

### 2. Theoretical formulation
The schematic diagram of CNTRC-stiffened plates is shown in Figure 1. The dimension of the plate having a length (a), width (b), uniform thickness (h), and radius of

![](./images/812513110333063172_12.jpg)

Figure 1. Geometry of the stiffened GRC plate.

curvature $R_x = R_y = \infty$. The first-order shear deformation theory (FSDT) is used to model the geometry of the CNTRC-stiffened plates based on an eight-noded isoparametric plate bending element. The mid-plane of the plate is attention as a reference plane.

$$
\tilde{u}(x,y,z,T) = u_0(x,y,T) + zu_1(x,y,T) \tag{1}
$$

$$
\tilde{v}(x,y,z,T) = v_0(x,y,T) + zv_1(x,y,T) \tag{2}
$$

$$
\tilde{w}(x,y,z,T) = v_0(x,y,T) \tag{3}
$$

where $u^0, v^0$, and $w^0$ are the reference plane displacement of the CNTRC-stiffened plate. The rotation about the $X$ and $Y$ axis are $u_1$, and $v_1$, respectively.

The infinitesimal strains of the $k$th plane of the CNTRC-stiffened plate are specified by,

$$
\begin{aligned}
\{\tilde{\varepsilon}\}_{k}^{T} &= \left\{\begin{array}{lllll}
\varepsilon_{xx}^{0} & \varepsilon_{yy}^{0} & \varepsilon_{xy}^{0} & \varepsilon_{xz}^{0} & \varepsilon_{yz}^{0}
\end{array}\right\}_{k}^{T} \\
&+ z\left\{\begin{array}{lllll}
k_{xx} & k_{yy} & k_{xy} & k_{xz} & k_{yz}
\end{array}\right\}_{k}^{T},
\end{aligned} \tag{4}
$$

$$
\left\{\begin{array}{c}
\varepsilon_{xx}^{0} \\
\varepsilon_{yy}^{0} \\
\varepsilon_{xy}^{0} \\
\varepsilon_{xz}^{0} \\
\varepsilon_{yz}^{0}
\end{array}\right\}_{k} = \begin{bmatrix}
\frac{\partial}{\partial x} & 0 & 0 & 0 & 0 \\
0 & \frac{\partial}{\partial y} & 0 & 0 & 0 \\
\frac{\partial}{\partial y} & \frac{\partial}{\partial x} & 0 & 0 & 0 \\
0 & 0 & \frac{\partial}{\partial x} & 1 & 0 \\
0 & 0 & \frac{\partial}{\partial y} & 0 & 1
\end{bmatrix}_{k} \left\{\begin{array}{c}
u_0 \\
v_0 \\
w_0 \\
u_1 \\
v_1
\end{array}\right\}_{k}, \tag{5}
$$

$$
\left\{\begin{array}{l}
k_{xx} \\
k_{yy} \\
k_{xy} \\
k_{xz} \\
k_{yz}
\end{array}\right\}_{k} = \begin{bmatrix}
\frac{\partial}{\partial x} & 0 \\
0 & \frac{\partial}{\partial y} \\
\frac{\partial}{\partial y} & \frac{\partial}{\partial x} \\
0 & 0 \\
0 & 0
\end{bmatrix}_{k} \left\{\begin{array}{l}
u_1 \\
v_1
\end{array}\right\}_{k}, \tag{6}
$$

$$
\{\tilde{\varepsilon}\}_{k} = \{\tilde{\varepsilon}^0\}_{k} + z\{\tilde{k}\}_{k}. \tag{7}
$$

The stress-resultant vector of the CNTRC-stiffened plate in the thermal field is known by,

$$
\{\tilde{\sigma}\}_{k} = [D]_{k}\{\tilde{\varepsilon} - \tilde{\alpha}\Delta T\}_{k}. \tag{8}
$$

The elasticity matrix is$[D]_{k}$.

The linear elastic strain energy of the CNTRC-stiffened plate is expressed as,

$$
U_k = \frac{1}{2} \int_{\Omega} \{\tilde{\varepsilon}\}_{\mathrm{k}}^{T} [\tilde{\sigma}]_{\mathrm{k}} \mathrm{d}\Omega, \tag{9}
$$

$$
\{\tilde{\varepsilon}\}_{k} = [B]_{k}\{\delta_{e}\}_{k}. \tag{10}
$$

The strain-displacement matrix is $[B]_{k}$.

The element elastic stiffness matrix of the stiffened plate is given as,

$$
[K_{se}]_{k} = \int_{A} [B]_{k}^{T} [D]_{k} [B]_{k} \mathrm{d}A. \tag{11}
$$

The kinetic energy of the CNTRC-stiffened plate element is known as,

$$
T_k = \frac{1}{2} \int_{\Omega} \rho_{k} \{\dot{\delta}\}_{k} \{\dot{\delta}\}_{k}^{T} \mathrm{d}\Omega, \tag{12}
$$

$$
[m]_{k} = \int_{z_{k-1}}^{z_{k}} [T_c]^{T} \rho_{k} [T_c] \mathrm{d}z, \tag{13}
$$

$$
[T_c] = \begin{bmatrix}
1 & 0 & 0 & z & 0 \\
0 & 1 & 0 & 0 & z \\
0 & 0 & 1 & 0 & 0
\end{bmatrix}. \tag{14}
$$

The elemental mass matrix of the CNTRC-stiffened plate is stated as,

$$
[M_{se}]_{k} = \int_{A} [N]^{T} [m]_{k} [N] \mathrm{d}A. \tag{15}
$$

The initial strain energy $(U_0^{\mathrm{th}})$ of CNTRC-stiffened plate is caused by the thermal environment, is known as,

$$
U_0^{\mathrm{th}} = \int_{v} \{\varepsilon'\}_{k} \left\{\sigma_0^{\mathrm{th}}\right\}_{k} \mathrm{d}v \tag{16}
$$

where $\{\varepsilon'\}_{k}$, and $\left\{\sigma_0^{\mathrm{th}}\right\}_{k}$ are defined the non-linear thermal strain, and the initial thermal stress vector.

The nonlinear thermal strain of CNTRC-stiffened plate are defined as,

$$
\{\varepsilon'\}_{k} = \frac{1}{2} \begin{bmatrix}
\hat{\psi}_{x}^{T} & 0 & 0 \\
0 & \hat{\psi}_{y}^{T} & 0 \\
\hat{\psi}_{y}^{T} & \hat{\psi}_{x}^{T} & 0 \\
\hat{\psi}_{z}^{T} & 0 & \hat{\psi}_{x}^{T} \\
0 & \hat{\psi}_{z}^{T} & \hat{\psi}_{y}^{T}
\end{bmatrix}_{k} \left\{\begin{array}{c}
\hat{\psi}_{x} \\
\hat{\psi}_{y} \\
\hat{\psi}_{z}
\end{array}\right\}_{k} = \frac{1}{2} [\hat{A}_x]_{k} \{\hat{\psi}\}_{k} \tag{17}
$$

where

$$
\begin{aligned}
\hat{\psi}_{x}^{T} & =\left[\frac{\partial u}{\partial x}, \frac{\partial v}{\partial x}, \frac{\partial w}{\partial x}\right]_{k} \\
\hat{\psi}_{y}^{T} & =\left[\frac{\partial u}{\partial y}, \frac{\partial v}{\partial y}, \frac{\partial w}{\partial y}\right]_{k} \\
\hat{\psi}_{z}^{T} & =\left[\frac{\partial u}{\partial z}, \frac{\partial v}{\partial z}, \frac{\partial w}{\partial z}\right]_{k}
\end{aligned}
\tag{18}
$$

$$
\{\hat{\psi}\}_{k}=\left[G_{\mathrm{th}}\right]_{k}\left\{\delta_{e}\right\}_{k}
\tag{19}
$$
where $\left[G_{\mathrm{th}}\right]_{k}$ is the shape functions derivatives.

Substituting the Eqs. (17) and (19) in (44), we have

$$
U_{0}=\frac{1}{2} \int_{v}\left\{\delta_{e}\right\}_{k}{ }^{T}\left[G_{\mathrm{th}}\right]_{k}{ }^{T}\left[\hat{A}_{x}\right]_{k}{ }^{T}\left\{\sigma_{0}^{\mathrm{th}}\right\}_{k} \mathrm{~d} v
\tag{20}
$$

Again,

$$
\left[\hat{A}_{x}\right]_{k}{ }^{T}\left\{\sigma_{0}^{\mathrm{th}}\right\}_{k}=\left[M_{\sigma e}^{\mathrm{th}}\right]_{k}\{\hat{\psi}\}_{k}=\left[M_{\sigma e}^{\mathrm{th}}\right]_{k}\left[G_{\mathrm{th}}\right]_{k}\left\{\delta_{e}\right\}_{k}
\tag{21}
$$
where $\left[M_{\sigma e}^{\mathrm{th}}\right]_{k}$ is the initial in-plane thermal stress resultants.

So, the additional strain energy stored in the stiffened plate is specified by,

$$
U_{0}=\frac{1}{2}\left\{\delta_{e}\right\}_{k}{ }^{T}\left[K_{\sigma e}^{\mathrm{th}}\right]_{k}\left\{\delta_{e}\right\}_{k}
\tag{22}
$$
where $\left[K_{\sigma e}^{\mathrm{th}}\right]_{k}$ are the thermal geometric stiffness matrices.

The elemental geometric stiffness matrices are given by,

$$
\left[K_{\sigma e}^{\mathrm{th}}\right]_{k}=\int_{v}\left[G_{\mathrm{th}}\right]_{k}{ }^{T}\left[M_{\sigma}^{\mathrm{th}}\right]_{k}\left[G_{\mathrm{th}}\right]_{k} \mathrm{~d} v
\tag{23}
$$

### 2.1. Finite element formulation

An eight-noded isoparametric plate bending FEM is used to model the geometry of the present investigation. The serendipity shape function is chosen in this study. The elemental stiffness, geometric stiffness and mass matrix can be expressed in the non-dimensional coordinate system as,

$$
\left[K_{s e}\right]_{k}=\int_{-1}^{1} \int_{-1}^{1}[B]_{k}{ }^{T}[D]_{k}[B]_{k}|J| \mathrm{d} \xi \mathrm{d} \eta,
\tag{24}
$$

$$
\left[K_{\sigma e}^{\mathrm{th}}\right]_{k}=\int_{-1}^{1} \int_{-1}^{1}\left[G_{\mathrm{th}}\right]_{k}{ }^{T}\left[M_{\sigma}^{\mathrm{th}}\right]_{k}\left[G_{\mathrm{th}}\right]_{k} \mathrm{~d} \xi \mathrm{d} \eta,
\tag{25}
$$

$$
\left[M_{s e}\right]_{k}=\int_{-1}^{1} \int_{-1}^{1}[N]^{T}[m]_{k}[N]|J| \mathrm{d} \xi \mathrm{d} \eta
\tag{26}
$$

### 2.2. Stiffeners formulations

Three-noded curved isoparametric beam elements with four degrees of freedom (two translations and two rotations) are used to model the stiffener [1, 19, 61]. A rectangular section with constant width $(b_{s t})$ and depth $(d_{s t})$, made of CNTs materials are considered for the stiffener. The shape functions of the stiffeners are stated as

$$
\begin{aligned}
& N_{i}^{x}=0.5 \xi \xi_{i}\left(1+\xi \xi_{i}\right) \quad \text { for } \quad i=1,3 \quad N_{i}^{x}=\left(1-\xi^{2}\right) \text { for } \quad i=2, \\
& N_{i}^{y}=0.5 \eta \eta_{i}\left(1+\eta \eta_{i}\right) \quad \text { for } \quad i=1,3 \quad N_{i}^{y}=\left(1-\eta^{2}\right) \text { for } \quad i=2 .
\end{aligned}
\tag{27}
$$

The nodal degree of freedom of X-directional stiffener can be denoted as,

$$
\sum_{i=1}^{3}\left\{\delta_{i}^{s x}\right\}=\sum_{i=1}^{3}\left[T_{s x}\right] \sum_{j=1}^{8}\left[\begin{array}{ccccc}
N_{i j} & 0 & 0 & 0 & 0 \\
0 & N_{i j} & 0 & 0 & 0 \\
0 & 0 & N_{i j} & 0 & 0 \\
0 & 0 & 0 & N_{i j} & 0 \\
0 & 0 & 0 & 0 & N_{i j}
\end{array}\right]\left\{\begin{array}{c}
u_{j}^{0} \\
v_{j}^{0} \\
w_{j}^{0} \\
\theta_{x j} \\
\theta_{y j}
\end{array}\right\}.
\tag{28}
$$

where $\left\{\tilde{\delta}_{i}^{s x}\right\}_{k}=\left\{\begin{array}{llll}u_{0}^{s x} & w_{0}^{s x} & \theta_{0}^{s x} & \theta_{0}^{s x}\end{array}\right\}_{k}^{T}$ is displacement vector,

$$
\left[T_{s x}\right]=\left[\begin{array}{ccccc}
1 & 0 & 0 & e & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1
\end{array}\right]
\tag{29}
$$

The eccentricity expressed as,

$$
e=\left(\frac{h+d_{s t}}{2}\right)
\tag{30}
$$

For X-directional stiffener, the generalized constituent relation can be stated as,

$$
\left[\tilde{\sigma}^{s x}\right]_{k}=\left[D^{s x}\right]_{k}\left[\tilde{\varepsilon}^{s x}\right]_{k}=\left[D^{s x}\right]_{k}\left[B^{s x}\right]_{k}\left[\tilde{\delta}_{i}^{s x}\right]_{k}.
\tag{31}
$$

where the resultant stress vector $\left[\tilde{\sigma}^{s x}\right]_{k}=\left\{\begin{array}{lll}N^{s x} & M^{s x} & T^{s x} Q^{s x}\end{array}\right\}_{k}^{T}$ and resultant strain vector,

$$
\left\{\tilde{\varepsilon}^{s x}\right\}_{k}=\left\{\begin{array}{llll}
\frac{\partial u^{s x}}{\partial x} & \frac{\partial \theta^{s x}}{\partial x} & \frac{\partial \theta^{s x}}{\partial x} & \left(\frac{\partial \theta^{s x}}{\partial x}+\frac{\partial w^{s x}}{\partial x}\right)
\end{array}\right\}_{k}^{T}.
\tag{32}
$$

The elasticity matrix of the X-stiffener element is obtained as follows,

$$
\left[D^{s x}\right]_{k}=\left[\begin{array}{cccc}
A_{11}^{s} b_{s t} & B_{11}^{s} b_{s t} & B_{16}^{s} b_{s t} & 0 \\
B_{11}^{s} b_{s t} & D_{11}^{s} b_{s t} & D_{16}^{s} b_{s t} & 0 \\
B_{16}^{s} b_{s t} & D_{16}^{s} b_{s t} & \frac{1}{6}\left(Q_{66}^{s}+Q_{44}^{s}\right) b_{s t}^{3} d_{s t} & 0 \\
0 & 0 & 0 & S_{44}^{s} b_{s t}
\end{array}\right]
\tag{33}
$$

$$
\left[\begin{array}{ccc}
A_{i j}^{s} & B_{i j}^{s} & D_{i j}^{s}
\end{array}\right]_{k}=\sum_{k=1}^{n l} \int_{z_{k-1}}^{z_{k}}\left[\bar{Q}_{i j}\right]_{k}\left(1, z, z^{2}\right) \mathrm{d} z \quad i, j=1,6
\tag{34}
$$

$$
\left[S_{i j}^{s}\right]_{k}=k_{s} \sum_{k=1}^{n l} \int_{z_{k-1}}^{z_{k}}\left[\bar{Q}_{i j}\right]_{k} \mathrm{~d} z \quad i, j=4
\tag{35}
$$

where $A_{i j}^{s}$ is extension stiffness matrix, $B_{i j}^{s}$ is extension bending coupling matrix, and $D_{i j}^{s}$ is bending stiffness matrix. The off-axis elastic constant matrix $\left[\bar{Q}_{i j}\right]_{k}$.

The inertia matrix of the X-stiffener is obtained as follows,

$$
\left[m_{s x}\right]_{k}=\left[\begin{array}{cccc}
P^{s} & 0 & 0 & 0 \\
& P^{s} & 0 & 0 \\
\operatorname{symm} & & I^{s} & 0 \\
& & & J^{s}
\end{array}\right],
\tag{36}
$$

$$
\left[\begin{array}{lll}
P^{s} & I^{s} & J^{s}
\end{array}\right]=\sum_{k=1}^{n l} \int_{z_{k-1}}^{z_{k}} \rho_{k}\left(1, z, b_{s t}^{3} / 3\right) \mathrm{d} z.
\tag{37}
$$

The nodal degree of freedom of Y-stiffener can be given by,

$$
\left\{\tilde{\delta}_{i}^{s y}\right\}=\left\{\begin{array}{llll}
v_{0}^{s y} & w_{0}^{s y} & \theta_{0}^{s y} & \tilde{\theta}_{0}^{s y}
\end{array}\right\}^{T}.
\tag{38}
$$

The generalized constituent relation for Y-directional stiffener can be obtained as follows,

$$
\left[\tilde{\sigma}^{s y}\right]_{k}=\left[D^{s y}\right]_{k}\left[\tilde{\varepsilon}^{s y}\right]_{k}=\left[D^{s y}\right]_{k}\left[B^{s y}\right]_{k}\left[\tilde{\delta}_{i}^{s y}\right]_{k},
\tag{39}
$$

$$
\left[\tilde{\sigma}^{s y}\right]_{k}=\left\{\begin{array}{llll}
N^{s y} & M^{s y} & T^{s y} & Q^{s y}
\end{array}\right\}_{k}^{T},
\tag{40}
$$

$$
\left\{\tilde{\varepsilon}^{s y}\right\}_{k}=\left\{\begin{array}{llll}
\frac{\partial v^{s y}}{\partial y} & \frac{\partial \theta^{s y}}{\partial y} & \frac{\partial \theta^{s y}}{\partial y} & \left(\frac{\partial \theta^{s y}}{\partial y}+\frac{\partial w^{s y}}{\partial y}\right)
\end{array}\right\}_{k}^{T}.
\tag{41}
$$

The element stiffness matrices of the stiffener in the natural coordinates system are obtained as,

$$
\left[K_{s x e}\right]_{k}=\int_{-1}^{1}\left[T_{s x}\right]_{k}^{T}\left[B_{s x}\right]_{k}^{T}\left[D_{s x}\right]_{k}\left[B_{s x}\right]_{k}\left[T_{s x}\right]_{k}\left[J_{s x}\right] \mathrm{d} \xi,
\tag{42}
$$

$$
\left[K_{s y e}\right]_{k}=\int_{-1}^{1}\left[T_{s y}\right]_{k}^{T}\left[B_{s y}\right]_{k}^{T}\left[D_{s y}\right]_{k}\left[B_{s y}\right]_{k}\left[T_{s y}\right]_{k}\left[J_{s y}\right] \mathrm{d} \eta,
\tag{43}
$$

$$
\left[K_{e}\right]_{k}=\left[K_{s e}\right]_{k}+\left[K_{s x e}\right]_{k}+\left[K_{s y e}\right]_{k}.
\tag{44}
$$

The element mass matrix of the stiffener in the natural coordinates system is obtained as,

$$
\left[M_{s x e}\right]_{k}=\int_{-1}^{1}\left[T_{s x}\right]_{k}^{T}\left[N_{s x}\right]_{k}^{T}\left[m_{s x}\right]_{k}\left[N_{s x}\right]\left[T_{s x}\right]_{k}\left[J_{s x}\right] \mathrm{d} \xi,
\tag{45}
$$

$$
\left[M_{s y e}\right]_{k}=\int_{-1}^{1}\left[T_{s y}\right]_{k}^{T}\left[N_{s y}\right]_{k}^{T}\left[m_{s y}\right]_{k}\left[N_{s y}\right]\left[T_{s y}\right]_{k}\left[J_{s y}\right] \mathrm{d} \eta,
\tag{46}
$$

$$
\left[M_{e}\right]_{k}=\left[M_{s e}\right]_{k}+\left[M_{s x e}\right]_{k}+\left[M_{s y e}\right]_{k}.
\tag{47}
$$

### 2.3. The effective material property of CNTs-stiffened plate

The four types of CNTs distribution through the thickness of the stiffened plates are depicted in Figure 2.

The effective material property of CNTs-stiffened plate are obtained based on the ROM stated as [48]

$$
\mathrm{UD} V_{\mathrm{CNT}}=V_{\mathrm{CNT}}^{*},
\tag{48}
$$

$$
\mathrm{FG}-\mathrm{X} V_{\mathrm{CNT}}=2(2|z| / h) V_{\mathrm{CNT}}^{*},
\tag{49}
$$

$$
\mathrm{FG}-\mathrm{O} V_{\mathrm{CNT}}=2(1-2|z| / h) V_{\mathrm{CNT}}^{*},
\tag{50}
$$

$$
\mathrm{FG}-\mathrm{V} V_{\mathrm{CNT}}=(1+2 z / h) V_{\mathrm{CNT}}^{*},
\tag{51}
$$

$$
V_{\mathrm{CNT}}^{*}=\frac{w_{\mathrm{CNT}}}{w_{\mathrm{CNT}}+\left(\rho_{\mathrm{CNT}} / \rho_{m}\right)-\left(\rho_{\mathrm{CNT}} / \rho_{m}\right) w_{\mathrm{CNT}}}.
\tag{52}
$$

$w_{\text{CNT}}$ and $\rho_{\text{CNT}}$ are the mass fraction and density of CNTs, respectively, and $\rho_{m}$ is the density of matrix.

$V_{m}$ and $V_{\text{CNT}}$ are the volume fraction of the matrix and CNTs, linked as

$$
V_{\mathrm{CNT}}+V_{m}=1
\tag{53}
$$

The equivalent material properties can be expressed as,

$$
E_{11}=\eta_{1} V_{\mathrm{CNT}} E_{11}^{\mathrm{CNT}}+V_{m} E_{m},
\tag{54}
$$

$$
\frac{\eta_{2}}{E_{22}}=\frac{V_{\mathrm{CNT}}}{E_{22}^{\mathrm{CNT}}}+\frac{V_{m}}{E_{m}},
\tag{55}
$$

$$
\frac{\eta_{3}}{G_{12}}=\frac{V_{\mathrm{CNT}}}{G_{12}^{\mathrm{CNT}}}+\frac{V_{m}}{G_{m}},
\tag{56}
$$

$E^{\text{CNT}}$ and $G^{\text{CNT}}$ are the Young's and shear modulus. $\eta_{i}(i=1,2,3)$ are the efficiency constraint. $E_{m}$ and $G_{m}$ are the Young's and shear modulus of the polymethyl methacrylate (PMMA) matrix.

The equivalent density, poisons ratio, and thermal conductivity are$\rho, v_{12},$ and$\alpha$ of CNTRC-stiffened plate is stated as,

$$
\rho=V_{\mathrm{CNT}} \rho_{\mathrm{CNT}}+V_{m} \rho_{m},
\tag{57}
$$

$$
v_{12}=V_{\mathrm{CNT}} v_{12}^{\mathrm{CNT}}+V_{m} v_{m},
\tag{58}
$$

$$
\alpha_{11}=V_{\mathrm{CNT}} \alpha_{11}^{\mathrm{CNT}}+V_{m} \alpha_{m},
\tag{59}
$$

$$
\alpha_{22}=\left(1+v_{12}^{\mathrm{CNT}}\right) V_{\mathrm{CNT}} \alpha_{22}^{\mathrm{CNT}}+\left(1+v_{m}\right) V_{m} \alpha_{m}-v_{12} \alpha_{11}. \quad(60)
$$

### 2.4. Solution procedure

Neglecting the damping results, the equation of motion for the free vibration responses are stated as,

$$
\left[M_{e}\right]_{k}\left\{\ddot{d}_{e}\right\}_{k}+\left(\left[K_{e}\right]_{k}+\left[K_{\sigma e}^{\mathrm{th}}\right]_{k}\right)\left\{d_{e}\right\}_{k}=0
\tag{61}
$$

Thus, the global stiffness $[K]$ and mass $[M]$ matrices of the CNTRC-stiffened plate are denoted by

$$
[K]=\sum_{k=1}^{\mathrm{NE}}\left[K_{e}\right]_{k},\left[K_{\sigma}^{\mathrm{th}}\right]=\sum_{k=1}^{\mathrm{NE}}\left[K_{\sigma e}^{\mathrm{th}}\right]_{k}, \text { and }[M]=\sum_{k=1}^{\mathrm{NE}}\left[M_{e}\right]_{k}
\tag{62}
$$

The free vibration equations in the global system is denoted by,

$$
[M]\{\ddot{d}\}+\left([K]+\left[K_{\sigma}^{\mathrm{th}}\right]\right)\{d\}=0
\tag{63}
$$

Assuming harmonic vibrations,$\{d\}=\{d\} e^{i \omega_{n} t}$, we have

$$
\left(\left([K]+\left[K_{\sigma}^{\mathrm{th}}\right]\right)-\omega_{n}^{2}[M]\right)\{d\}=0
\tag{64}
$$

This is a standard Eigen value problem and is solved for the Eigen value and eigenvectors [62]

$$
[A]\{d\}=\lambda\{d\}
\tag{65}
$$

where $[A]=\left([K]+\left[K_{\sigma}^{t h}\right]\right)^{-1}[M]$ and $\lambda=1 / \omega_{n}^{2}$

![](./images/812513110333063172_13.jpg)

(a) UD

![](./images/812513110333063172_14.jpg)

(b) FG-X

![](./images/812513110333063172_15.jpg)

(c) FG-O

![](./images/812513110333063172_16.jpg)

(d) FG-V

Figure 2. The four types of CNTs distribution through the thickness of the stiffened plate.

<table><caption>Table 1. Non-dimensional fundamental frequencies ($\varpi=\omega_n(a^2/h)\sqrt{\rho_m/E_m}$) of simply supported various types of CNTRC plates by varying temperatures ($V_{CNT}^{CNT}=0.12$, $a/b=1$, $b/h=10$, $\eta_1=0.137$, $\eta_2=1.002$ and $\eta_3=0.715$).</caption>
<thead>
<tr>
<th rowspan="2">Temperature (K)</th>
<th rowspan="2">Mode</th>
<th colspan="2">UD</th>
<th colspan="2">FG-V</th>
<th colspan="2">FG-O</th>
<th colspan="2">FG-X</th>
</tr>
<tr>
<th>Lei et al. [37]</th>
<th>FEM</th>
<th>Lei et al. [37]</th>
<th>FEM</th>
<th>Lei et al. [37]</th>
<th>FEM</th>
<th>Lei et al. [37]</th>
<th>FEM</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>1</td>
<td>12.126</td>
<td>12.005</td>
<td>11.309</td>
<td>11.151</td>
<td>10.453</td>
<td>10.436</td>
<td>13.128</td>
<td>12.843</td>
</tr>
<tr>
<td></td>
<td>2</td>
<td>16.554</td>
<td>16.520</td>
<td>16.261</td>
<td>16.057</td>
<td>15.353</td>
<td>15.399</td>
<td>17.104</td>
<td>16.556</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>16.983</td>
<td>16.544</td>
<td>17.040</td>
<td>16.556</td>
<td>17.036</td>
<td>16.556</td>
<td>17.390</td>
<td>16.6758</td>
</tr>
<tr>
<td>500</td>
<td>1</td>
<td>10.964</td>
<td>10.819</td>
<td>10.244</td>
<td>10.128</td>
<td>9.537</td>
<td>9.537</td>
<td>11.667</td>
<td>11.469</td>
</tr>
<tr>
<td></td>
<td>2</td>
<td>14.494</td>
<td>14.238</td>
<td>14.226</td>
<td>14.084</td>
<td>13.462</td>
<td>13.525</td>
<td>14.594</td>
<td>14.255</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>14.549</td>
<td>14.239</td>
<td>14.540</td>
<td>14.256</td>
<td>14.539</td>
<td>14.255</td>
<td>15.137</td>
<td>14.256</td>
</tr>
<tr>
<td>700</td>
<td>1</td>
<td>9.251</td>
<td>9.166</td>
<td>8.775</td>
<td>8.703</td>
<td>8.272</td>
<td>8.287</td>
<td>9.698</td>
<td>9.5864</td>
</tr>
<tr>
<td></td>
<td>2</td>
<td>11.515</td>
<td>11.365</td>
<td>11.543</td>
<td>11.385</td>
<td>11.103</td>
<td>11.172</td>
<td>11.551</td>
<td>11.385</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>11.827</td>
<td>11.365</td>
<td>11.551</td>
<td>11.385</td>
<td>11.509</td>
<td>11.385</td>
<td>12.286</td>
<td>11.885</td>
</tr>
</tbody>
</table>

## 3. Boundary conditions

Several boundary conditions (BCs) are used for the present investigation.

For SSSS cases:
$$
x=0,\ a;\ \nu^0=w^0=\nu_1=0, \tag{66}
$$
$$
y=0,\ b;\ u^0=w^0=u_1=0.. \tag{67}
$$

For SCSC cases:
$$
x=y=0;\ \nu^0=w^0=\nu_1=0,, \tag{68}
$$
$$
x=a,\ y=b;\ u^0=\nu^0=w^0=u_1=\nu_1=0. \tag{69}
$$

For CCCC cases:
$$
x=0,a;\ y=0,b;\ u^0=\nu^0=w^0=u_1=\nu_1=0. \tag{70}
$$

For CFFF cases:
$$
x=0;\ u^0=\nu^0=w^0=u_1=\nu_1=0. \tag{71}
$$

For SSCC cases:
$$
x=0;\ x=a;\nu^0=w^0=\nu_1=0, \tag{72}
$$
$$
y=0,\ y=b;\ u^0=\nu^0=w^0=u_1=\nu_1=0. \tag{73}
$$

For CFCF cases:
$$
x=0;\ y=0;\ u^0=\nu^0=w^0=u_1=\nu_1=0, \tag{74}
$$

<table>
<caption>Table 2. Natural frequencies(Hz) of simply supported cross-ply anti-symmetric eccentric at bottom stiffened plate ($a=b=254$ mm, $h=12.7$ mm, $b_{st}=6.35$ mm, $d_{st}=25.4$ mm, and $n_x=n_y=1$).</caption>
<thead>
<tr>
<th rowspan="2">Mode number</th>
<th rowspan="2">Nayak and Bandyopadhyay [1]</th>
<th rowspan="2">Rout et al. [61]</th>
<th colspan="3">Present FEM</th>
</tr>
<tr>
<th>($6\times6$)</th>
<th>($8\times8$)</th>
<th>($10\times10$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1141.00</td>
<td>1123.17</td>
<td>1141.83</td>
<td>1141.34</td>
<td>1141.24</td>
</tr>
<tr>
<td>2</td>
<td>2394.17</td>
<td>2367.77</td>
<td>2408.75</td>
<td>2400.85</td>
<td>2398.55</td>
</tr>
<tr>
<td>3</td>
<td>2415.82</td>
<td>2407.57</td>
<td>2425.38</td>
<td>2419.29</td>
<td>2417.61</td>
</tr>
<tr>
<td>4</td>
<td>2646.18</td>
<td>2656.00</td>
<td>2658.33</td>
<td>2651.84</td>
<td>2650.22</td>
</tr>
</tbody>
</table>

## 4. Validations

The numerical code is modeled based on the FEM to perform the free vibration characteristic of CNTRC-stiffened plates. Table 1 is illustrated the comparison study of the first three natural frequencies of square simply supported CNTRC plates at different temperatures with various graded CNTs distributions. It is observed that the present results are very close to those of published works of Lei et al. [37]. The present outcome of Table 2 is well-matched with the results of simply supported anti-symmetric cross-ply stiffened plate with “eccentric at bottom” stiffeners. Table 2 also shows the convergence study of natural frequencies of laminated stiffened plates, considering the mesh size of $6\times6$, $8\times8$, and $10\times10$, respectively. It is observed that the frequency value obtained for the two mesh sizes ($8\times8$ and $10\times10$) is more or less equal, and the percentage variation is less than unity. For computer effectiveness, lower mesh size of ($8\times8$) has been utilized for the further response. The above validations are represented the exactness and accuracy of the current FEM formulation.

## 5. Results and discussions

PMMA is denoted as matrix phase, and its material properties are [48], $\alpha_{m}=45\times10^{-6}\ (1+0.0005\ (T-T_0))\ 1/K.;$ $\rho_{m}=1150\mathrm{kg/m^{3}}$; $E_{m}=(3.52-0.0034\ (T-T_0))$ GPa and $\upsilon_{m}=0.34$. However, the single-walled carbon nano-tube (CNTs) is assumed as reinforcement to enhance the composite properties. Mechanical properties of a single walled carbon nano-tube (CNTs) with the temperature ($L=9.26$ nm, $R=0.068$ nm, $h=0.067$ nm) are $E_{11}^{\mathrm{CNT}}(\mathrm{GPa})=5646.6$, $E_{22}^{\mathrm{CNT}}(\mathrm{GPa})=7080.0$, $G_{12}^{\mathrm{CNT}}$ (GPa) $=1944.5$, $\alpha_{11}^{\mathrm{CNT}}(\times10^{-6}/\mathrm{K})=3.4584$, and $\alpha_{22}^{\mathrm{CNT}}(\times10^{-6}/\mathrm{K})=5.1682$ for temperature $=300\ \mathrm{K}$; $E_{11}^{\mathrm{CNT}}(\mathrm{GPa})=5530.8$, $E_{22}^{\mathrm{CNT}}(\mathrm{GPa})=6934.8$, $G_{12}^{\mathrm{CNT}}$ (GPa) $=1964.3$, $\alpha_{11}^{\mathrm{CNT}}(\times10^{-6}/\mathrm{K})=4.5361$, and $\alpha_{22}^{\mathrm{CNT}}\ (\times10^{-6}/\mathrm{K})=5.0189$ for temperature $=500\ \mathrm{K}$; $E_{11}^{\mathrm{CNT}}$ (GPa) $=5474.4$, $E_{22}^{\mathrm{CNT}}(\mathrm{GPa})=6864.1$, $G_{12}^{\mathrm{CNT}}$ (GPa) $=1964.4$, $\alpha_{11}^{\mathrm{CNT}}(\times10^{-6}/\mathrm{K})=4.6677$, and$\alpha_{22}^{\mathrm{CNT}}(\times10^{-6}/\mathrm{K})=4.8943$ for temperature $=700\ \mathrm{K}$; The efficiency parameters of a single-walled CNTs with a different volume fraction are $\eta_{1}=0.137$, $\eta_{2}=1.022$, and $\eta_{3}=0.715$ for $V_{CNT}=0.12$; $\eta_{1}=0.142$, $\eta_{2}=1.626$, and $\eta_{3}=1.138$ for $V_{CNT}=0.17$; $\eta_{1}=0.141$, $\eta_{2}=1.585$, and $\eta_{3}=1.109$ for $V_{CNT}$=0.28;

In the entire investigation, four different graded are concerned, such as UD, FG-X, FG-O, and FG-V, distributed through the plate's thickness. In this present research, two different $X$ and $Y$-directional eccentrically stiffened is considered. The various examples are also studied in this numerical study to realize its effect on the natural frequency. The different geometric parameters are, $a=$ length, $b=$ width, and $h=$ thickness of the plate. $b_{st}=$ stiffeners width, $d_{st}=$ stiffeners thickness, $n_x$ and $n_y$ denotes the number of $X$ and $Y$ directional stiffeners. Non-dimensional fundamental frequencies of CNTRC-stiffened plates are expressed as,

$$
\varpi=\omega_{n}(a^{2}/h)\sqrt{\rho_{m}/E_{m}} \tag{75}
$$

### 5.1. Effect of stiffeners addition

The natural frequency of CNTRC-stiffened plates with different boundary conditions (BCs) is illustrated in Table 3 by varying the number of stiffeners along with $X$ and $Y$ directions. The using geometric parameters are, $a/b=1.0$, $a/h=100$, $b_{st}=h$, and $d_{st}=2h$. It is remarkable that most of the cases, the natural frequency of the CNTRC plates increases due to stiffeners' addition. This is the fact that the stiffeners addition increases the mass, as well as the stiffness

<table>
<caption>Table 3. The NDFF of CNTRC-stiffened plate with different boundary conditions (BCs) by varying numbers of stiffeners in both directions, $T=300$ K, $V_{\mathrm{CNT}}=0.12$.</caption>
<thead>
<tr>
<th>Types of boundary conditions</th>
<th>No of stiffeners</th>
<th>UD</th>
<th>FG-X</th>
<th>FG-O</th>
<th>FG-V</th>
</tr>
</thead>
<tbody>
<tr>
<td>SSSS</td>
<td>$n_x$=0, $n_y$=0</td>
<td>22.5621</td>
<td>32.5109</td>
<td>19.7552</td>
<td>22.5621</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=0</td>
<td>29.3356</td>
<td>34.7048</td>
<td>22.8557</td>
<td>25.0310</td>
</tr>
<tr>
<td></td>
<td>$n_x$=0, $n_y$=1</td>
<td>26.8442</td>
<td>32.4343</td>
<td>19.7899</td>
<td>22.5542</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=1</td>
<td>29.3335</td>
<td>34.6497</td>
<td>22.9464</td>
<td>25.0416</td>
</tr>
<tr>
<td></td>
<td>$n_x$=2, $n_y$=2</td>
<td>30.3020</td>
<td>35.4828</td>
<td>24.1815</td>
<td>25.9803</td>
</tr>
<tr>
<td></td>
<td>$n_x$=3, $n_y$=3</td>
<td>31.3524</td>
<td>36.4138</td>
<td>25.4891</td>
<td>27.0433</td>
</tr>
<tr>
<td></td>
<td>$n_x$=4, $n_y$=4</td>
<td>31.7599</td>
<td>36.7641</td>
<td>25.9970</td>
<td>27.4305</td>
</tr>
<tr>
<td>CCCC</td>
<td>$n_x$=0, $n_y$=0</td>
<td>58.4351</td>
<td>70.0208</td>
<td>43.2123</td>
<td>49.2205</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=0</td>
<td>62.3072</td>
<td>73.4952</td>
<td>48.2721</td>
<td>53.5784</td>
</tr>
<tr>
<td></td>
<td>$n_x$=0, $n_y$=1</td>
<td>58.3457</td>
<td>69.8348</td>
<td>43.3238</td>
<td>49.2242</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=1</td>
<td>62.4025</td>
<td>73.4247</td>
<td>48.6970</td>
<td>53.7401</td>
</tr>
<tr>
<td></td>
<td>$n_x$=2, $n_y$=2</td>
<td>62.7901</td>
<td>73.7299</td>
<td>49.2579</td>
<td>54.1866</td>
</tr>
<tr>
<td></td>
<td>$n_x$=3, $n_y$=3</td>
<td>64.8099</td>
<td>75.4106</td>
<td>52.0569</td>
<td>56.4529</td>
</tr>
<tr>
<td></td>
<td>$n_x$=4, $n_y$=4</td>
<td>64.9604</td>
<td>75.5326</td>
<td>52.2687</td>
<td>56.6327</td>
</tr>
<tr>
<td>CFFF</td>
<td>$n_x$=0, $n_y$=0</td>
<td>9.3173</td>
<td>11.3410</td>
<td>6.6930</td>
<td>7.6791</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=0</td>
<td>9.8162</td>
<td>11.8009</td>
<td>7.2786</td>
<td>8.1986</td>
</tr>
<tr>
<td></td>
<td>$n_x$=0, $n_y$=1</td>
<td>9.3066</td>
<td>11.3279</td>
<td>6.6854</td>
<td>7.6705</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=1</td>
<td>9.8095</td>
<td>11.7896</td>
<td>7.2770</td>
<td>8.1916</td>
</tr>
<tr>
<td></td>
<td>$n_x$=2, $n_y$=2</td>
<td>10.0820</td>
<td>12.0422</td>
<td>7.6675</td>
<td>8.5025</td>
</tr>
<tr>
<td></td>
<td>$n_x$=3, $n_y$=3</td>
<td>10.1113</td>
<td>12.0546</td>
<td>7.7318</td>
<td>8.5432</td>
</tr>
<tr>
<td></td>
<td>$n_x$=4, $n_y$=4</td>
<td>10.6411</td>
<td>12.4968</td>
<td>8.4199</td>
<td>9.0392</td>
</tr>
<tr>
<td>SCSC</td>
<td>$n_x$=0, $n_y$=0</td>
<td>41.1102</td>
<td>49.5290</td>
<td>30.2453</td>
<td>34.5134</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=0</td>
<td>43.8626</td>
<td>52.0492</td>
<td>33.7310</td>
<td>37.5312</td>
</tr>
<tr>
<td></td>
<td>$n_x$=0, $n_y$=1</td>
<td>41.0539</td>
<td>49.4132</td>
<td>30.3081</td>
<td>34.5115</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=1</td>
<td>43.9400</td>
<td>52.0147</td>
<td>34.0189</td>
<td>37.6243</td>
</tr>
<tr>
<td></td>
<td>$n_x$=2, $n_y$=2</td>
<td>45.2745</td>
<td>53.1169</td>
<td>35.8232</td>
<td>38.9677</td>
</tr>
<tr>
<td></td>
<td>$n_x$=3, $n_y$=3</td>
<td>46.9302</td>
<td>54.5453</td>
<td>37.9793</td>
<td>40.7210</td>
</tr>
<tr>
<td></td>
<td>$n_x$=4, $n_y$=4</td>
<td>46.9880</td>
<td>54.5809</td>
<td>38.0779</td>
<td>40.7922</td>
</tr>
<tr>
<td>SSCC</td>
<td>$n_x$=0, $n_y$=0</td>
<td>28.2645</td>
<td>33.9656</td>
<td>21.3528</td>
<td>24.2803</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=0</td>
<td>31.2572</td>
<td>36.6400</td>
<td>25.0539</td>
<td>27.1910</td>
</tr>
<tr>
<td></td>
<td>$n_x$=0, $n_y$=1</td>
<td>28.5729</td>
<td>34.2026</td>
<td>21.8546</td>
<td>24.6614</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=1</td>
<td>31.5545</td>
<td>36.8652</td>
<td>25.5196</td>
<td>27.5378</td>
</tr>
<tr>
<td></td>
<td>$n_x$=2, $n_y$=2</td>
<td>31.8792</td>
<td>37.1391</td>
<td>25.9508</td>
<td>27.8766</td>
</tr>
<tr>
<td></td>
<td>$n_x$=3, $n_y$=3</td>
<td>33.3557</td>
<td>38.4516</td>
<td>27.7531</td>
<td>29.3215</td>
</tr>
<tr>
<td></td>
<td>$n_x$=4, $n_y$=4</td>
<td>33.5112</td>
<td>38.5873</td>
<td>27.9500</td>
<td>29.4831</td>
</tr>
<tr>
<td>CFCF</td>
<td>$n_x$=0, $n_y$=0</td>
<td>9.6120</td>
<td>11.6495</td>
<td>7.0418</td>
<td>8.0532</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=0</td>
<td>9.8850</td>
<td>11.8949</td>
<td>7.3878</td>
<td>8.3278</td>
</tr>
<tr>
<td></td>
<td>$n_x$=0, $n_y$=1</td>
<td>9.6113</td>
<td>11.6452</td>
<td>7.0483</td>
<td>8.0562</td>
</tr>
<tr>
<td></td>
<td>$n_x$=1, $n_y$=1</td>
<td>9.8841</td>
<td>11.8901</td>
<td>7.3944</td>
<td>8.3300</td>
</tr>
<tr>
<td></td>
<td>$n_x$=2, $n_y$=2</td>
<td>10.6437</td>
<td>12.5497</td>
<td>8.3638</td>
<td>9.0626</td>
</tr>
<tr>
<td></td>
<td>$n_x$=3, $n_y$=3</td>
<td>11.5552</td>
<td>13.3520</td>
<td>9.4806</td>
<td>9.9301</td>
</tr>
<tr>
<td></td>
<td>$n_x$=4, $n_y$=4</td>
<td>12.2008</td>
<td>13.9416</td>
<td>10.2505</td>
<td>10.5697</td>
</tr>
</tbody>
</table>

![](./images/812513110333063172_17.jpg)

Figure 3. The NDFF of CNTRC-stiffened plate by varying stiffeners thickness ratio at different temperatures.

of the plate. It is also revealed that the first and second moments of inertia of the CNTRC plates boost due to stiffeners' adding. However, most of the cases, the stiffness has a more significant effect in comparison with the mass.

Interestingly, the $X$-directional stiffeners have a most significant influence on the fundamental frequency. In contrast, $Y$-directional stiffeners have a major performance with SSSS BCs. However, it effect is minor with SSCC BCs. It is interesting, for CCCC, SCSC, CFCF, and CFFF boundary conditions, the natural frequency of the CNTRC-stiffened plate reduces in addition to the $Y$-directional stiffeners. This is because; the mass has a more significant effect than stiffness. However, for CCCC, SCSC, CFCF, and CFFF boundary conditions, $Y$-directional stiffeners' negative effect reduces $X$-directional stiffeners' influence. It is also noticeable that the significant boost in natural frequency is observed for CNTRC-stiffened plate with three stiffeners ($n_x = 3$, $n_y = 3$). On the other hand, more than three stiffeners accumulation along with both directions, it is noticed that the raise in NDFF is marginal.

It is observed that the highest values of the natural frequency of CNTRC-stiffened plate are always recognized in FG-X grading, irrespective of BCs. In contrast, the lowest values are observed in FG-O distribution. Hence, it is concluded that the FG-X distribution always gives the more efficient in increasing the stiffness of the CNTRC-stiffened plate. Also, it is revealed that the peak percentage boost in natural frequency is noticed in FG-O CNTRC-stiffened plate in addition to stiffeners, while the least values are observed in FG-X CNTRC-stiffened plate. The CCCC-CNTRC-stiffened plates always are provided the superior values of NDFF in evaluation to the other BCs, which are expected. This is a fact that the constraints of the CCCC BCs are higher than other BCs. It may be noted that the more influence of stiffeners is noticed with SSSS BCs.

### 5.2. Effect of stiffeners thickness ratio ($d_{st}/h$)

The influence of stiffeners thickness to plate thickness ratios ($d_{st}/h$) on NDFF of different graded CNTRC-stiffened plates with CCCC BCs are worked out by varying temperatures and are revealed in Figure 3. The geometric parameters of this example, are $a/b = 1.0$, $a/h = 100$, $n_x = 1$, $n_y = 1$, and $b_{st}=2h$, respectively. It is obvious that the raise in $d_{st}/h$ ratio of CNTRC-stiffened plate to increase the NDFF in all graded plates. This is because; the upper values of $d_{st}/h$

![](./images/812513110333063172_18.jpg)

Figure 4. The influence of NDFF of CNTRC-stiffened plate by varying stiffeners thickness ratio with CNTs volume fraction.

enhance the stiffness of the structure. Commonly, the mass and stiffness both enhance due to grow up in $d_{st}/h$; however, the more dominance achieve of stiffness is recognized. As a result, increase the natural frequency of the CNTRC-stiffened plate. Moreover, it is perceived that the natural frequency of the CNTRC-stiffened plate always reduces due to growing up in temperature. It is clearly identified that the highest percentage increase in NDFF is observed in FG-O cases, while for the same observation, the lowest percentage increase in NDFF is looked in FG-X cases. Further, the more pronounced effect of stiffeners thickness ratio is noticed at a lower temperature.

### 5.3. Effect of stiffeners widths

The influence of stiffeners width to plate thickness ratios $(b_{st}/h)$ on the natural frequency of different graded CNTRC stiffened plates with CCCC BCs is shown in Figure 4 at different CNTs volume fraction. The using parameters of present example are $a/b=1.0$, $a/h=100$, $n_x = 1$, $n_y = 1$, and $d_{st}=0.25h$. It is remarkable that the increase in $b_{st}/h$ ratio of CNTRC-stiffened plates reduce the value of NDFF in all graded plate. This is the fact that the higher values of $b_{st}/h$ provided the stiffer structure to the plates. Interestingly, the increase in stiffeners width increases both the mass and stiffness. However, stiffness has a more striking effect, leading to a considerable amount of natural frequency. As expected, the NDFF values of the CNTRC-stiffened plates increase due to the increase in CNTs volume fraction. The peak percentage growth in NDFF is detected in FG-O cases; in contrast, the least percentage boost in NDFF is identified in FG-X grading for the same worked out. Interestingly, the remarkable effect of stiffeners width ratio $(b_{st}/h)$ is observed at higher CNTs volume fraction.

### 5.4. Effect of an aspect ratio of the plate

The NDFF values of CNTRC-stiffened plate are plotted against the length to width ratios $(a/b)$ at different temperatures with CCCC BCs, which are shown in Figure 5. The using parameters are, $a=0.1$ m, $a/h=10$, $n_x = 1$, $n_y = 1$, $b_{st}=h$, and $d_{st}=0.25h$. The NDFF values of the CNTRC-stiffened plate boost rapidly due to an increase in aspect ratio $(a/b)$, irrespective of grading, and temperature. Usually,

![](./images/812513110333063172_19.jpg)

Figure 5. The NDFF of CNTRC-stiffened plate with the aspect ratio at different temperatures.

the mass and stiffness are enhanced in an increased aspect ratio (a/b). However, the domination effect of stiffness is noticed, which increases the NDFF of the CNTRC-stiffened plate. It is also recognized that the FG-X graded CNTRC- stiffened plate provides the maximum values of NDFF than other types of graded, irrespective of aspect ratio, while the FG-O distribution reveals the minimum values of NDFF.

### 5.5. Effect of plate thickness
The frequency parameters of CNTRC-stiffened plate are plotted against the thickness ratios (a/h) by varying the CNTs volume fractions illustrated in Figure 6. The investi- gated parameters are, $a=0.1m$, $n_x=1$, $n_y=1$, $b_{st}=h$, and $d_{st}=0.25h$. It can be seen that the NDFF values of the CNTRC-stiffened plate increases due to a rise in thickness ratios (a/h), irrespective of grading and CNTs volume frac- tions. It is also observed that the FG-X graded CNTRC-stiff- ened plate presents the highest values of NDFF than other graded, similarly for the FG-O distribution provides the low- est values of NDFF. It may be noted that the natural frequency of CNTRC-stiffened plate increases due to a rise in CNTs volume fractions.

### 5.6. Effect of temperature and CNTs volume fraction
In this investigation, the NDFF results of CNTRC-stiffened plates are obtained by varying temperature and CNTs vol- ume fraction with boundary conditions, and demonstrated in Tables 4 and 5, respectively. The using parameters in this example are $a/b=1.0$, $a/h=10$, $n_x=1$, $n_y=1$, $b_{st}=h$, and $d_{st}=0.25h$. It is revealed that the NDFF values of all graded CNTRC-stiffened plates always reduce due to an increase in temperature, irrespective of boundary conditions. Normally, the plate's elastic stiffness always decreases due to a rise in temperature, which is expected. In contrast, the NDFF val- ues of all graded CNTRC-stiffened plates always increase due to a rise in CNTs volume fraction, irrespective of boundary conditions. Generally, the elastic stiffness of the plate always enhances in addition to fiber volume frac- tions (CNTs).

It is observed that the highest percentage decrease rate of natural frequency is identified with FG-X cases due to

![](./images/812513110333063172_20.jpg)

Figure 6. The NDFF of CNTRC-stiffened plate with thickness ratio at different volume fractions.

<table>
<caption>Table 4. The natural frequency of CNTRC-stiffened SSSS plate with the temperature at different CNTs volume fraction.</caption>
<thead>
<tr>
<th>Temperature</th>
<th>V<sub>CNT</sub></th>
<th>UD</th>
<th>FG-X</th>
<th>FG-O</th>
<th>FG-V</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>0.12</td>
<td>12.6818</td>
<td>13.1931</td>
<td>11.8837</td>
<td>12.2364</td>
</tr>
<tr>
<td></td>
<td>0.17</td>
<td>16.1429</td>
<td>16.9080</td>
<td>15.1078</td>
<td>15.5737</td>
</tr>
<tr>
<td></td>
<td>0.28</td>
<td>17.5276</td>
<td>18.6344</td>
<td>16.6391</td>
<td>17.1631</td>
</tr>
<tr>
<td>500</td>
<td>0.12</td>
<td>11.1174</td>
<td>11.5183</td>
<td>10.4562</td>
<td>10.7524</td>
</tr>
<tr>
<td></td>
<td>0.17</td>
<td>14.1765</td>
<td>14.7892</td>
<td>13.3095</td>
<td>13.7079</td>
</tr>
<tr>
<td></td>
<td>0.28</td>
<td>15.3336</td>
<td>16.2320</td>
<td>14.6523</td>
<td>15.0805</td>
</tr>
<tr>
<td>700</td>
<td>0.12</td>
<td>9.1162</td>
<td>9.3808</td>
<td>8.6519</td>
<td>8.8649</td>
</tr>
<tr>
<td></td>
<td>0.17</td>
<td>11.6576</td>
<td>12.0780</td>
<td>11.0403</td>
<td>11.3346</td>
</tr>
<tr>
<td></td>
<td>0.28</td>
<td>12.5263</td>
<td>13.1752</td>
<td>12.1199</td>
<td>12.4158</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 5. The natural frequency of CNTRC-stiffened CCCC plate with the temperature at different CNTs volume fraction.</caption>
<thead>
<tr>
<th>Temperature</th>
<th>V<sub>CNT</sub></th>
<th>UD</th>
<th>FG-X</th>
<th>FG-O</th>
<th>FG-V</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>0.12</td>
<td>15.7504</td>
<td>15.9997</td>
<td>15.3920</td>
<td>15.6001</td>
</tr>
<tr>
<td></td>
<td>0.17</td>
<td>20.2617</td>
<td>20.7198</td>
<td>19.7803</td>
<td>20.0991</td>
</tr>
<tr>
<td></td>
<td>0.28</td>
<td>21.4479</td>
<td>22.3958</td>
<td>21.3210</td>
<td>21.6884</td>
</tr>
<tr>
<td>500</td>
<td>0.12</td>
<td>13.5384</td>
<td>13.7259</td>
<td>13.2826</td>
<td>13.4359</td>
</tr>
<tr>
<td></td>
<td>0.17</td>
<td>17.4326</td>
<td>17.7885</td>
<td>17.0938</td>
<td>17.3323</td>
</tr>
<tr>
<td></td>
<td>0.28</td>
<td>18.4158</td>
<td>19.1984</td>
<td>18.3891</td>
<td>18.6677</td>
</tr>
<tr>
<td>700</td>
<td>0.12</td>
<td>10.8066</td>
<td>10.9302</td>
<td>10.6596</td>
<td>10.7542</td>
</tr>
<tr>
<td></td>
<td>0.17</td>
<td>13.9308</td>
<td>14.1774</td>
<td>13.7436</td>
<td>13.8945</td>
</tr>
<tr>
<td></td>
<td>0.28</td>
<td>14.6796</td>
<td>15.2738</td>
<td>14.7423</td>
<td>14.9262</td>
</tr>
</tbody>
</table>

thermal effect, while the minimum values observe in FG-O graded plate. It may be noted that the maximum percentage increase rate of natural frequency is recognized with FG-X cases due to a rise in CNTs volume fraction effect. In contrast, the minimum values observe in FG-O graded plate.

### 5.7. Mode shapes
The consequence of $V_{CNT}$ on the mode shape of FG-O graded CNTRC-stiffened cantilevered plate is depicted in

Table 6. The dark nodal lines designate with zero displacements at the same time as the solid and dashed lines rise for positive and negative displacements, respectively. The first four modes of CNTRC-stiffened cantilevered plate ($V_{\text{CNT}} = 0.12$) are torsion (1T), spanwise bending (1B), cord wise bending (1C), and second torsion (2T), respectively. Also, for $V_{\text{CNT}} = 0.17$, the results are spanwise bending (1B), torsion (1T), cord wise bending (1C), and second torsion (2T), respectively. The effect of $V_{\text{CNT}}$ is clearly noticed. The first mode changes from cord wise bending to torsion, and the second mode changes from

<table>
<caption>Table 6. The effect of the number of stiffeners on the first four modes of FG-O graded CNTRC-stiffened cantilevered plate at $T=300K$, $a/b=1.0$, $a/h=100$, $n_x=1$; $n_y=1$.</caption>
<thead>
<tr>
<th>Mode</th>
<th>$V_{\text{CNT}}=0.12$</th>
<th>$V_{\text{CNT}}=0.17$</th>
<th>$V_{\text{CNT}}=0.28$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1st</td>
<td>![](./images/812513110333063172_21.jpg)</td>
<td>![](./images/812513110333063172_22.jpg)</td>
<td>![](./images/812513110333063172_23.jpg)</td>
</tr>
<tr>
<td>2nd</td>
<td>![](./images/812513110333063172_24.jpg)</td>
<td>![](./images/812513110333063172_25.jpg)</td>
<td>![](./images/812513110333063172_26.jpg)</td>
</tr>
<tr>
<td>3rd</td>
<td>![](./images/812513110333063172_27.jpg)</td>
<td>![](./images/812513110333063172_28.jpg)</td>
<td>![](./images/812513110333063172_29.jpg)</td>
</tr>
<tr>
<td>4th</td>
<td>![](./images/812513110333063172_30.jpg)</td>
<td>![](./images/812513110333063172_31.jpg)</td>
<td>![](./images/812513110333063172_32.jpg)</td>
</tr>
</tbody>
</table>

torsion to cord wise bending. However, for $V_{\text{CNT}}=0.28$, the clarification is torsion (1T), spanwise bending (1B), cord wise bending (1C), and second torsion (2T), respectively. It is very interesting; for $V_{\text{CNT}}=0.12$ and $V_{\text{CNT}}=0.28$, the almost similar mode shape is identified, but displacement values are different.

## 6. Conclusions

The free vibration performance of CNTRC-stiffened plate based on first-order shear deformation theory using FEM is investigated in this study. The stiffeners are modeled with a three-noded beam element. In this numerical study, four graded CNTs distribution are assumed through the thickness of the CNTRC-stiffened plate. A constraint method is used to tie the nodal degrees of freedom of the stiffener with that of the shells together by considering eccentricity and wrapping effect. The major conclusion is furnished below,

1. Most of the cases, it is observed that the natural frequency of the CNTRC plates increases due to stiffeners' addition. The $X$-directional stiffeners have a most significant influence on the fundamental frequency in comparison with the $Y$-directional stiffeners. It can be seen that with CCCC, SCSC, CFCF, and CFFF boundary conditions, the natural frequency of the CNTRC-stiffened plate reduce in addition to the $Y$-directional stiffeners.

2. It may be noted that the more influence of stiffeners is noticed with SSSS BCs.

3. It is observed that the highest values of the natural frequency of CNTRC-stiffened plate are always recognized in FG-X grading, irrespective of BCs. In contrast, the lowest values are observed in FG-O distribution.

4. The CCCC-CNTRC-stiffened plates always are provided the superior values of NDFF in evaluation to the other BCs. This is the fact that the constraints of the CCCC BCs are higher than in other BCs.

5. It is noticed that the NDFF of the CNTRC plate increase due to an increase in aspect ratio and $a/h$ ratio, respectively.

6. It is identified that the natural frequencies of the CNTRC-stiffened plates decrease due to the increase in temperature. In contrast, the opposite effect is noticed due to a rise in $V_{CNT}$.

7. It is revealed that the increase in a stiffeners thickness ratio of GRC-stiffened plate to increase the NDFF value. However, the same results are also found for the increase in stiffeners width to plate thickness ratio. Interestingly, the effect of stiffeners thickness is more prominent than the stiffener's width with the same weight.

## References

[1] A.N. Nayak and J.N. Bandyopadhyay, "Free vibration analysis of laminated stiffened shells," J. Eng. Mech., vol. 131, no. 1, pp. 100-105, 2005. DOI: 10.1061/(ASCE)0733-9399(2005)131:1(100).

[2] B. Chattopadhyay, P.K. Sinha, and M. Mukhopadhyay, "Finite element free vibration analysis of eccentrically stiffened composite plates," J. Reinf. Plast. Compos., vol. 11, no. 9, pp. 1003-1034, 1992. DOI: 10.1177/073168449201100903.

[3] I.E. Harik and M. Guo, "Finite element analysis of eccentrically stiffened plates in free vibration," Comput. Struct., vol. 49, no. 6, pp. 1007-1015, 1993. DOI: 10.1016/0045-7949(93)90012-3.

[4] A. Mukherjee and M. Mukhopadhyay, "Finite element free vibration analysis of stiffened plates," Aeronaut. J., vol. 90, no. 897, pp. 267-273, 1986.

[5] A.K. Ghosh and K.C. Biswal, "Free-vibration analysis of stiffened laminated plates using higher-order shear deformation theory," Finite Elem. Anal. Des., vol. 22, no. 2, pp. 143-161, 1996. DOI: 10.1016/0168-874X(95)00051-T.

[6] H. Zeng, and C.W. Bert, "Free vibration analysis of discretely stiffened skew plates," Int. J. Struct. Stab. Dyn., vol. 01, no. 01, pp. 125-144, 2001. DOI: 10.1142/S0219455401000032.

[7] A.N. Nayak and J.N. Bandyopadhyay, "Free vibration analysis and design aids of stiffened conoidal shells," J. Eng. Mech., vol. 128, no. 4, pp. 419-427, 2002. DOI: 10.1061/(ASCE)0733-9399(2002)128:4(419).

[8] A.S. Rajawat, A.K. Sharma, and P. Gehlot, "Free vibration analysis of stiffened laminated plate using FEM," Mater. Today, vol. 5, no. 2, pp. 5313-5321, 2018. DOI: 10.1016/j.matpr.2017.12.115.

[9] L.X. Peng, K.M. Liew, and S. Kitipornchai, "Buckling and free vibration analyses of stiffened plates using the FSDT mesh-free method," J. Sound Vib., vol. 289, no. 3, pp. 421-449, 2006. DOI: 10.1016/jsv.2005.02.023.

[10] T.Q. Wang, R.H. Wang, and N.J. Ma, "Nonlinear vibration of a stiffened plate considering the existence of initial stresses," KSCE J. Civ. Eng., vol. 23, no. 5, pp. 2303-2312, 2019. DOI: 10.1007/s12205-019-1387-1.

[11] M. Rout and A. Karmakar, "Free vibration of rotating twisted composite stiffened plate," International Conference on Mechanical Engineering, pp. 357-373, 2018.

[12] J. Xue and Y. Wang, "Free vibration analysis of a flat stiffened plate with side crack through the Ritz method," Arch. Appl. Mech., vol. 89, no. 10, pp. 2089-2102, 2019. DOI: 10.1007/s00419-019-01565-6.

[13] K. Zhang and T.R. Lin, "An analytical study of vibration response of a beam stiffened Mindlin plate," Appl. Acoust., vol. 155, pp. 32-43, 2019. DOI: 10.1016/j.apacoust.2019.05.004.

[14] A. Alaimo, C. Orlando, and S. Valvano, "An alternative approach for modal analysis of stiffened thin-walled structures with advanced plate elements," Eur. J. Mech. A Solids, vol. 77, pp. 103820, 2019. DOI: 10.1016/j.euromechsol.2019.103820.

[15] S. Mandal, A. Mitra, and P. Sahoo, 2019. "Experimental investigation on static and free vibration behavior of concentrically stiffened plates," International Conference on Mechanical Engineering, pp. 437-456.

[16] L. Sinha, S.S. Mishra, A.N. Nayak, and S.K. Sahu, "Free vibration characteristics of laminated composite stiffened plates: experimental and numerical investigation," Compos. Struct., vol. 233, pp. 111557, 2020. DOI: 10.1016/j.compstruct.2019.111557.

[17] N.D. Dat, T.Q. Quan, V. Mahesh, and N.D. Duc, "Analytical solutions for nonlinear magneto-electro-elastic vibration of smart sandwich plate with carbon nanotube reinforced nanocomposite core in hygrothermal environment," Int. J. Mech. Sci., vol. 186, pp. 105906, 2020. DOI: 10.1016/j.ijmecsci.2020.105906.

[18] S.S. Mirjavadi, M. Forsat, M.R. Barati, and A.S. Hamouda, "Geometrically nonlinear vibration analysis of eccentrically stiffened porous functionally graded annular spherical shell segments," Mech. Base Des. Struct. Mach., pp. 1-15, 2020.

[19] A.N. Nayak, L. Satpathy, and P.K. Tripathy, "Free vibration characteristics of stiffened plates," Int. J. Adv. Struct. Eng., vol. 10, no. 2, pp. 153-167, 2018. DOI: 10.1007/s40091-018-0189-x.

[20] P.R. Sahoo and M. Barik, "Free vibration analysis of stiffened plates," J. Vib. Eng. Technol., vol. 8, pp. 1-14, 2020.

[21] V.L. Nguyen and T.P. Hoang, "Analytical solution for free vibration of stiffened functionally graded cylindrical shell structure resting on elastic foundation," SN Appl. Sci., vol. 1, no. 10, pp. 1150, 2019. DOI: 10.1007/s42452-019-1168-y.

[22] M. Rout, S.S. Hota, and A. Karmakar, "Free vibration characteristics of delaminated composite pretwisted stiffened cylindrical shell," Proc. Inst. Mech. Eng. C., vol. 232, no. 4, pp. 595-611, 2018. DOI: 10.1177/0954406216686389.

[23] M.T. Tran, V.L. Nguyen, S.D. Pham, and J. Rungamornrat, "Free vibration of stiffened functionally graded circular cylindrical shell resting on Winkler-Pasternak foundation with different boundary conditions under thermal environment," Acta Mech., vol. 231, no. 6, pp. 2545-2564, 2020. DOI: 10.1007/s00707-020-02658-y.

[24] M. Zarei, G.H. Rahimi, and M. Hemmatnezhad, "Free vibra- tional characteristics of grid-stiffened truncated composite con- ical shells," Aerosp. Sci. Technol., vol. 99, pp. 105717, 2020. DOI: 10.1016/j.ast.2020.105717.

[25] A. Milazzo and V. Oliveri, "Buckling and postbuckling of stiff- ened composite panels with cracks and delaminations by Ritz approach," AIAA J., vol. 55, no. 3, pp. 965-980, 2017. DOI: 10.2514/1.J055159.

[26] V. Oliveri, A. Milazzo, and P.M. Weaver, "Thermo-mechanical post-buckling analysis of variable angle tow composite plate assemblies," Compos. Struct., vol. 183, pp. 620-635, 2018. DOI: 10.1016/j.compstruct.2017.07.050.

[27] J. Liu, Q. Fei, D. Jiang, D. Zhang, and S. Wu, "Experimental and numerical investigation on static and dynamic characteris- tics for curvilinearly stiffened plates using DST-BK model," Int. J. Mech. Sci., vol. 169, pp. 105286, 2020. DOI: 10.1016/j.ijmecsci.2019.105286.

[28] S. Jafarpour and M.R. Khedmati, "Vibration analysis of stiffened plates with initial geometric imperfections," Proceedings of the Institution of Mechanical Engineers, Part M: Journal of Engineering for the Maritime Environment, p. 1475090220967520, 2020.

[29] R. Vescovini, V. Oliveri, D. Pizzi, L. Dozio, and P.M. Weaver, "A semi-analytical approach for the analysis of variable-stiffness panels with curvilinear stiffeners," Int. J. Solids Struct., vol. 188-189, pp. 244-260, 2020. DOI: 10.1016/j.ijsolstr.2019.10.011.

[30] H. Zhou, Y. Zha, H. Wu, and J. Meng, "The vibroacoustic ana- lysis of periodic structure-stiffened plates," J. Sound Vib., vol. 481, pp. 115402, 2020. DOI: 10.1016/j.jsv.2020.115402.

[31] G. Sciascia, V. Oliveri, A. Milazzo, and P.M. Weaver, "Ritz solution for transient analysis of variable-stiffness shell structures," AIAA J., vol. 58, no. 4, pp. 1796-1810, 2020. DOI: 10.2514/1.J058686.

[32] M.F. Liu, T.P. Chang, and Y.H. Wang, "Free vibration analysis of orthotropic rectangular plates with tapered varying thickness and Winkler spring foundation," Mech. Based Des. Struct. Mach., vol. 39, no. 3, pp. 320-333, 2011. DOI: 10.1080/15397734.2011.543054.

[33] E. Bahmyari and A. Rahbar-Ranji, "Free vibration analysis of orthotropic plates with variable thickness resting on non-uni- form elastic foundation by element free Galerkin method," J. Mech. Sci. Technol., vol. 26, no. 9, pp. 2685-2694, 2012. DOI: 10.1007/s12206-012-0713-z.

[34] D. Shi, Q. Wang, X. Shi, and F. Pang, "Free vibration analysis of moderately thick rectangular plates with variable thickness and arbitrary boundary conditions," Shock Vib., vol. 2014, pp. 1-25, 2014. DOI: 10.1155/2014/572395.

[35] W. Guo and Q. Feng, "Free vibration analysis of arbitrary-shaped plates based on the improved Rayleigh-Ritz method," Adv. Civ. Eng., vol. 2019, pp. 1-14, 2019. DOI: 10.1155/2019/7041592.

[36] H.S. Shen and C.L. Zhang, "Thermal buckling and postbuckling behavior of functionally graded carbon nanotube-reinforced composite plates," Mater. Des., vol. 31, no. 7, pp. 3403-3411, 2010. DOI: 10.1016/j.matdes.2010.01.048.

[37] Z.X. Lei, K.M. Liew, and J.L. Yu, "Free vibration analysis of functionally graded carbon nanotube-reinforced composite plates using the element-free kp-Ritz method in thermal envi- ronment," Compos. Struct., vol. 106, pp. 128-138, 2013. DOI: 10.1016/j.compstruct.2013.06.003.

[38] S. Natarajan, M. Haboussi, and G. Manickam, "Application of higher-order structural theory to bending and free vibration analysis of sandwich plates with CNT reinforced composite facesheets," Compos. Struct., vol. 113, pp. 197-207, 2014. DOI: 10.1016/j.compstruct.2014.03.007.

[39] P. Malekzadeh and A.R. Zarei, "Vibration analysis of quadrilateral laminated plates with carbon nanotube reinforced composite layers," Thin-Walled Struct., vol. 82, pp. 221-232, 2014. DOI: 10.1016/j.tws.2014.04.016.

[40] L.W. Zhang, Z.X. Lei, and K.M. Liew, "Free vibration analysis of functionally graded carbon nanotube-reinforced composite triangular plates using the FSDT and element-free IMLS-Ritz method," Compos. Struct., vol. 120, pp. 189-199, 2015. DOI: 10.1016/j.compstruct.2014.10.009.

[41] L.W. Zhang, Z.G. Song, and K.M. Liew, "State-space Levy method for vibration analysis of FG-CNT composite plates sub- jected to in-plane loads based on higher-order shear deform- ation theory," Compos. Struct., vol. 134, pp. 989-1003, 2015. DOI: 10.1016/j.compstruct.2015.08.138.

[42] L.W. Zhang, W.C. Cui, and K.M. Liew, "Vibration analysis of functionally graded carbon nanotube reinforced composite thick plates with elastically restrained edges," Int. J. Mech. Sci., vol. 103, pp. 9-21, 2015. DOI: 10.1016/j.ijmecsci.2015.08.021.

[43] Z.X. Lei, L.W. Zhang, and K.M. Liew, "Free vibration analysis of laminated FG-CNT reinforced composite rectangular plates using the kp-Ritz method," Compos. Struct., vol. 127, pp. 245-259, 2015. DOI: 10.1016/j.compstruct.2015.03.019.

[44] Z.X. Lei, L.W. Zhang, and K.M. Liew, "Vibration of FG-CNT reinforced composite thick quadrilateral plates resting on Pasternak foundations," Eng. Anal. Bound. Elem., vol. 64, pp. 1-11, 2016. DOI: 10.1016/j.enganabound.2015.11.014.

[45] R. Moradi-Dastjerdi, G. Payganeh, and H. Malek-Mohammadi, "Free vibration analyses of functionally graded CNT reinforced nanocomposite sandwich plates resting on elastic foundation," J. Solid Mech., vol. 7, no. 2, pp. 158-172, 2015.

[46] K. Mehar and S.K. Panda, "Geometrical nonlinear free vibration analysis of FG-CNT reinforced composite flat panel under uni- form thermal field," Compos. Struct., vol. 143, pp. 336-346, 2016. DOI: 10.1016/j.compstruct.2016.02.038.

[47] B.A. Selim, L.W. Zhang, and K.M. Liew, "Vibration analysis of CNT reinforced functionally graded composite plates in a ther- mal environment based on Reddy's higher-order shear deform- ation theory," Compos. Struct., vol. 156, pp. 276-290, 2016. DOI: 10.1016/j.compstruct.2015.10.026.

[48] Y. Kiani, "Isogeometric large amplitude free vibration of graphene reinforced laminated plates in thermal environment using NURBS formulation," Comput. Methods Appl. Mech. Eng., vol. 332, pp. 86-101, 2018. DOI: 10.1016/j.cma.2017.12.015.

[49] Ö. Civalek, "Free vibration of carbon nanotubes reinforced (CNTR) and functionally graded shells and plates based on FSDT via discrete singular convolution method," Compos. B Eng., vol. 111, pp. 45-59, 2017. DOI: 10.1016/j.compositesb.2016.11.030.

[50] J. Torabi and R. Ansari, "Nonlinear free vibration analysis of thermally induced FG-CNTRC annular plates: Asymmetric ver- sus axisymmetric study," Comput. Methods Appl. Mech. Eng., vol. 324, pp. 327-347, 2017. DOI: 10.1016/j.cma.2017.05.025.

[51] P. Maji, M. Rout, and A. Karmakar, "Free vibration response of car- bon nanotube reinforced pretwisted conical shell under thermal environment," Proc. Inst. Mech. Eng., Part C: J. Mech. Eng. Sci., vol. 234, no. 3, pp. 770-783, 2020. DOI: 10.1177/0954406219886325.

[52] P. Maji, M. Rout, and A. Karmakar, "Free vibration analysis of CNTs-reinforced functionally graded conical shell," Int. J. Mech. Prod. Eng. Res. Dev., vol. 6, pp. 25-32, 2018.

[53] Z. Qin, X. Pang, B. Safaei, and F. Chu, "Free vibration analysis of rotating functionally graded CNT reinforced composite cylindrical shells with arbitrary boundary conditions," Compos. Struct., vol. 220, pp. 847-860, 2019. DOI: 10.1016/j.compstruct.2019.04.046.

[54] A. Patel, R. Das, and S.K. Sahu, "Experimental and numerical study on free vibration of multiwall carbon nanotube reinforced composite plates," Int. J. Struct. Stab. Dyn., vol. 20, no. 12, pp. 2050129, 2020. DOI: 10.1142/S0219455420501291.

[55] Ö. Civalek, "Vibration of functionally graded carbon nanotube reinforced quadrilateral plates using geometric transformation dis- crete singular convolution method," Int. J. Numer. Methods Eng., vol. 121, no. 5, pp. 990-1019, 2020. DOI: 10.1002/nme.6254.

[56] O. Civalek and M.H. Jalaei, "Shear buckling analysis of func- tionally graded (FG) carbon nanotube reinforced skew plates with different boundary conditions," Aerosp. Sci. Technol., vol. 99, pp. 105753, 2020. DOI: 10.1016/j.ast.2020.105753.

[57] H.Q. Tran, V.T. Vu, M.T. Tran, and P. Nguyen-Tri, "A new four-variable refined plate theory for static analysis of smart laminated functionally graded carbon nanotube reinforced

composite plates," Mech. Mater., vol. 142, pp. 103294, 2020.
DOI: 10.1016/j.mechmat.2019.103294.

[58]
V.N. Van Do, J.T. Jeon, and C.H. Lee, "Dynamic analysis of carbon nanotube reinforced composite plates by using Bézier extraction based isogeometric finite element combined with higher-order shear deformation theory," Mech. Mater., vol. 142, pp. 103307, 2020. DOI: 10.1016/j.mechmat.2019.103307.

[59]
V.N. Van Do, Y.K. Lee, and C.H. Lee, "Isogeometric analysis of FG-CNTRC plates in combination with hybrid type higher- order shear deformation theory," Thin-Walled Struct., vol. 148, pp. 106565, 2020. DOI: 10.1016/j.tws.2019.106565.

[60]
B.A.M.M. Selim, Z. Liu, and K.M. Liew, "Active control of functionally graded carbon nanotube-reinforced composite plates with piezoelectric layers subjected to impact loading," J. Vib. Control., vol. 26, no. 7-8, pp. 581-598, 2020. DOI: 10.1177/1077546319889849.

[61]
M. Rout, T. Bandyopadhyay, and A. Karmakar, "Free vibration analysis of pretwisted delaminated composite stiffened shallow shells: a finite element approach," J. Reinf. Plast. Compos., vol. 36, no. 8, pp. 619-636, 2017. DOI: 10.1177/0731684416689726.

[62]
A.J. Ferreira, MATLAB Codes for Finite Element Analysis, Springer, Netherlands, 2009.

## Appendix

$$
[D]_{k}=\left[\begin{array}{ccc}
A_{i j} & B_{i j} & 0 \\
B_{i j} & D_{i j} & 0 \\
0 & 0 & S_{i j}
\end{array}\right]
$$

$$
\left[\begin{array}{llll}
A_{i j} & B_{i j} & D_{i j} & S_{i j}
\end{array}\right]=\sum_{k=1}^{n l} \int_{z_{k-1}}^{z_{k}}\left(Q_{i j}\right)_{k}\left[1, z, z^{2}, k_{s}\right] \mathrm{d} z
$$

$$
[B]_{k}=\sum_{i}^{8}\left[\begin{array}{ccccc}
N_{i, x} & 0 & 0 & 0 & 0 \\
N_{i, y} & 0 & 0 & 0 & 0 \\
0 & N_{i, x} & 0 & 0 & 0 \\
0 & N_{i, y} & \frac{N_{i}}{R_{y}} & 0 & 0 \\
0 & 0 & N_{i, x} & 0 & 0 \\
0 & -\frac{N_{i}}{R_{y}} & N_{i, y} & 0 & 0 \\
0 & 0 & 0 & N_{i, x} & 0 \\
0 & 0 & 0 & N_{i, y} & 0 \\
0 & 0 & 0 & 0 & N_{i, x} \\
0 & 0 & 0 & 0 & N_{i, y} \\
0 & 0 & 0 & N_{i} & 0 \\
0 & 0 & 0 & 0 & N_{i}
\end{array}\right]
$$

$$
\left[\mathrm{D}^{s y}\right]_{k}=\left[\begin{array}{cccc}
\mathrm{A}_{22}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & \mathrm{B}_{22}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & \mathrm{B}_{26}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & 0 \\
\mathrm{~B}_{22}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & \mathrm{D}_{22}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & \mathrm{D}_{26}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & 0 \\
\mathrm{~B}_{26}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & \mathrm{D}_{26}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}} & \frac{1}{6}\left(\mathrm{Q}_{66}^{\mathrm{s}}+\mathrm{Q}_{55}^{\mathrm{s}}\right) \mathrm{b}_{\mathrm{st}}^{3} \mathrm{~d}_{\mathrm{st}} & 0 \\
0 & 0 & 0 & \mathrm{~S}_{55}^{\mathrm{s}} \mathrm{b}_{\mathrm{st}}
\end{array}\right]
$$

$$
\left[m_{s y}\right]_{k}=\left[\begin{array}{cccc}
P^{s} & 0 & 0 & 0 \\
& P^{s} & 0 & 0 \\
\text { symm } & & J^{s} & 0 \\
& & & I^{s}
\end{array}\right]\left[\mathrm{T}_{\mathrm{sy}}\right]_{\mathrm{k}}=\left[\begin{array}{ccccc}
0 & 1 & 0 & 0 & e \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1
\end{array}\right]
$$