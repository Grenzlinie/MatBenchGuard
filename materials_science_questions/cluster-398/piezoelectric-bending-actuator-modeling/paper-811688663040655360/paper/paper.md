• Research Paper •
January 2011 Vol.54 No.1: 143–149
doi: 10.1007/s11433-010-4196-6

# Analysis of transient responses in a laminated piezoelectric cylindrical shell

HAN Xu¹*, GONG Shuang¹, HE XiaoQiao² & JIANG Chao¹

¹ State Key Laboratory of Advanced Design and Manufacturing for Vehicle Body, College of Mechanical and Vehicle Engineering, Hunan University, Changsha 410082, China;
² City University of Hong Kong, Hong Kong, China

Received May 9, 2010; accepted September 21, 2010

A hybrid numerical method is proposed for analysis of transient responses in a multilayered piezoelectric cylindrical shell. In the present method, the associated equations of the displacement field and the electro-potential field are developed using an analytical-numerical method. The piezoelectric cylindrical shell is discretized into layered annular elements along the wall thickness direction. The governing equations are determined by Hamilton's Principle considering the coupling between the elastic and electric field in each element. The modal analysis and Fourier transformation with respect to the spatial cylindrical polar coordinates in the direction of wave propagation are introduced to formulate the displacement field and electro-potential field in the wave-number domain. The results of transient responses at any location can be obtained by performing an inverse Fourier transformation. The transient responses of an actual piezoelectric cylindrical shell excited by a coupled elec-tro-mechanical circular line load are investigated as a numerical example. The computational results demonstrate the efficiency of the present method.

transient response, piezoelectric material, cylindrical shell
PACS: 02.60.Cb, 43.35.Pt, 77.65.Dq

Piezoelectric materials can be integrated with the structural systems to form smart structures. The characteristics they exhibit, such as the self-diagnosis function, the self-repair-ing and adaptive capability, have widespread applications in many branches of industry, as diverse as aerospace, auto-motive and biological engineering, etc. A preferable under-standing of the electro-elastic waves in piezoelectric media is of practical and exploratory significance for stretching their availability. Meanwhile, problems relevant to the elas-tic wave in systems with shell-type geometry are encoun-tered in many engineering applications. As for aerospace, automotive and nuclear industries, where considerable re-searches are carried out on strong and lightweight structures, the wave motion and vibration of circular cylindrical shells have had special interest.

Studies of the wave propagation in piezoelectric struc-tures have attracted the attention of scientists and engineers. A great variety of theoretical and experimental researches are concerned with this topic. Gao and Shen et al. [1] ob-tained the exact solutions for the free vibration and forced vibration of a finite-length rectangular orthotropic piezo-electric laminate, using the power series expansion method. Wu and Shen et al. [2] extended this method to analyze the free vibration of functional gradient piezoelectric plates. Li et al. [3] derived a high-order theory for functional graded piezoelectric shells based on the generalized Hamilton's principle. Based on a state-space method and the Kel-vin-Voigt viscoelastic model, Yan and Chen [4] theoreti-cally studied the electro-mechanical time-dependent behav-ior of the simply-supported FGM beam bonded with two surface piezoelectric layers with viscoelastic interfaces.

*Corresponding author (email: xu_han688@hotmail.com)

© Science China Press and Springer-Verlag Berlin Heidelberg 2011
phys.scichina.com www.springerlink.com

Cheng et al. [5,6] adopted the transfer matrix method incorporated with an asymptotic expansion technique to analyze the response of the FGPM structure. Introducing two displacement functions as well as two stress functions, Chen and Ding [7] established a state-space model to study the free vibration of a transversely isotropic FGPM plate, in which the state equations are transformed to the ones with constant coefficients by a laminated approximation. Using the orthogonal expansion technique, etc., Ding et al. [8] developed an analytical method for solving the transient response of an axisymmetric plane strain problem of piezoelectric hollow cylinders. Liu and Wang et al. [9] discussed the propagation behavior of Rayleigh waves in layered piezoelectric structures. To visualize the effects of anisotropy on wave propagation, Liu et al. [10,11] introduced a set of six characteristic wave surfaces for composite laminated material. Based on these concepts, the unique propagation properties of elastic waves in a functionally graded piezoelectric cylinder and multilayered piezoelectric cylinder are investigated by Han and Liu et al. [12,13] However, the analysis of transient responses of piezoelectric laminated structures remains worthy of further investigation, especially using numerical methods capable of delivering better accuracy and economical benefits.

Based on the analytical-numerical method proposed by Han et al. [14] for analyzing wave motion in a functionally graded cylindrical shell, which efficiently combined the finite element method, the Fourier transformation and modal analysis, this paper attempts to extend it to analysis of transient responses in a multilayered piezoelectric cylindrical shell. The layered elements are introduced to represent the physical model of the structure, which reduces the nodes compared with the FEM method. The displacement and electro-potential field are discretized in the wall thickness direction with a three nodal line approximation. The governing equations are determined by the coupled electro-elastic theory and Hamilton's Principle. Performing the Fourier transformation, the governing equations are transformed to the wave-number domain. The transient responses are obtained by employing the modal analysis and inverse Fourier transformation. The results of the numerical example provide the transient responses excited by a coupled electro-mechanical line load in a PZT-5A/ PVDF composite cylindrical shell.

## 1 Governing equations

A hybrid laminated piezoelectric cylindrical shell is divided in the radial direction into $N$ layered annular elements, as shown in Figure 1. The inner and outer radii and the thicknesses of the cylindrical shell, as well as the $n$th layered annular element, are denoted by $R_{1}, R_{2}$, and $H, r_{n-1}, r_{n}$ and $h_{n}$ respectively. The constitutive relations within the $n$th element are given in matrix form [15] as:
$$
\begin{aligned}
\boldsymbol{\sigma} & =\boldsymbol{c}_{n} \boldsymbol{\varepsilon}-\boldsymbol{e}_{n}^{\mathrm{T}} \boldsymbol{E} \\
\boldsymbol{D} & =\boldsymbol{g}_{n} \boldsymbol{E}+\boldsymbol{e}_{n} \boldsymbol{\varepsilon}
\end{aligned}
\tag{1}
$$
where $\boldsymbol{\sigma}=\left[\begin{array}{lllllll}\sigma_{z} & \sigma_{\theta} & \sigma_{r} & \sigma_{r \theta} & \sigma_{r z} & \sigma_{z \theta}\end{array}\right]^{\mathrm{T}}$ is the stress vector,
$\boldsymbol{\varepsilon}=\left[\begin{array}{llllll}\varepsilon_{z} & \varepsilon_{\theta} & \varepsilon_{r} & \varepsilon_{r \theta} & \varepsilon_{r z} & \varepsilon_{z \theta}\end{array}\right]^{\mathrm{T}}$ is the mechanical strain vector,
$\boldsymbol{D}=\left[\begin{array}{lll}D_{z} & D_{\theta} & D_{r}\end{array}\right]^{\mathrm{T}}$ is the electric displacement vector,
$\boldsymbol{E}=\left[\begin{array}{lll}E_{z} & E_{\theta} & E_{r}\end{array}\right]^{\mathrm{T}}$ is the electric field vector, and $\boldsymbol{c}_{n}, \boldsymbol{g}_{n}$ and
$\boldsymbol{e}_{n}$ are the elastic, piezoelectric and dielectric material con-

![](./images/811688663040655360_1.jpg)

Figure 1 Mechanical model of a piezoelectric cylindrical shell.

stant matrices of the $n$th element, respectively. The relationship between the displacement field and strain tension is given by
$$
\boldsymbol{\varepsilon}=\boldsymbol{L}_{d} \boldsymbol{U}, \tag{2}
$$
where $\boldsymbol{U}=\left[\begin{array}{lll}u & v & w\end{array}\right]^{\mathrm{T}}$ is the displacement vector, in which $u$, $v$, and $w$ denote the displacement components in the axial, circumferential and radial directions, respectively.
The differential operator matrix $\boldsymbol{L}_{d}$ can be written as:
$$
\boldsymbol{L}_{d}=\left[\begin{array}{cccccc}
\frac{\partial}{\partial z} & 0 & 0 & 0 & \frac{\partial}{\partial r} & \frac{1}{r} \frac{\partial}{\partial \theta} \\
0 & \frac{1}{r} \frac{\partial}{\partial \theta} & 0 & \frac{\partial}{\partial r}-\frac{1}{r} & 0 & \frac{\partial}{\partial z} \\
0 & \frac{1}{r} & \frac{\partial}{\partial r} & \frac{1}{r} \frac{\partial}{\partial \theta} & \frac{\partial}{\partial z} & 0
\end{array}\right]. \tag{3}
$$

The Maxwell equations in the quasi-static approximation are formulated in matrix form as [14]:
$$
\begin{aligned}
\boldsymbol{E}=-\operatorname{grad} \varphi & =-\boldsymbol{L}_{\varphi} \varphi, \\
\operatorname{div} \boldsymbol{D} & =0,
\end{aligned} \tag{4}
$$
where $\varphi$ denotes the electrostatic potential, while
$$
\boldsymbol{L}_{\varphi}^{\mathrm{T}}=\left[\begin{array}{lll}
\frac{\partial}{\partial z} & \frac{\partial}{\partial \theta} & \frac{\partial}{\partial r}
\end{array}\right]. \tag{5}
$$

Within the $n$th element, the displacement field $\boldsymbol{U}$ and electro-potential field $\varphi$ are discretized along the wall thickness direction into nodal displacement vectors and nodal electro-potential vectors on the inner, middle and outer annular surfaces. Hence, the displacement field and electro-potential field are approximated as the interpolation of vectors on three annular nodal surfaces:
$$
\boldsymbol{U}(z, \theta, r, t)=\boldsymbol{N}_{d}(r) \boldsymbol{d}(z, \theta, t), \tag{6}
$$
$$
\varphi(z, \theta, r, t)=\boldsymbol{N}_{\phi}(r) \boldsymbol{\phi}(z, \theta, t), \tag{7}
$$
where $\boldsymbol{d}$ and $\boldsymbol{\phi}$ represent displacement and electro-potential vectors on annular nodal surfaces respectively:
$$
\begin{aligned}
\boldsymbol{d}^{\mathrm{T}}=\left[\begin{array}{lll}
\boldsymbol{d}_{\mathrm{i}}^{\mathrm{T}} & \boldsymbol{d}_{\mathrm{m}}^{\mathrm{T}} & \boldsymbol{d}_{\mathrm{o}}^{\mathrm{T}}
\end{array}\right] & =\left[\begin{array}{lllllllll}
u_{\mathrm{i}} & v_{\mathrm{i}} & w_{\mathrm{i}} & u_{\mathrm{m}} & v_{\mathrm{m}} & w_{\mathrm{m}} & u_{\mathrm{o}} & v_{\mathrm{o}} & w_{\mathrm{o}}
\end{array}\right], \\
\boldsymbol{\phi}^{\mathrm{T}}=\left[\begin{array}{lll}
\phi_{\mathrm{i}} & \phi_{\mathrm{m}} & \phi_{\mathrm{o}}
\end{array}\right], &
\end{aligned} \tag{8}
$$
in which subscripts i, m, and o denote the inner, middle and outer surfaces of the element, respectively.

Also, the shape function matrices $N_{d}$ and $N_{\phi}$ are the quadratic shape functions, given by
$$
\begin{aligned}
& \boldsymbol{N}_{d}(r)=\left[\left(1-3 \hat{r}+2 \hat{r}^{2}\right) \boldsymbol{I} \quad 4\left(\hat{r}-\hat{r}^{2}\right) \boldsymbol{I} \quad\left(-\hat{r}+2 \hat{r}^{2}\right) \boldsymbol{I}\right] \\
& \boldsymbol{N}_{\varphi}(r)=\left[\left(1-3 \hat{r}+2 \hat{r}^{2}\right) \quad 4\left(\hat{r}-\hat{r}^{2}\right) \quad\left(-\hat{r}+2 \hat{r}^{2}\right)\right]
\end{aligned} \tag{9}
$$
where $\hat{r}=\left(r-r_{n-1} / r_{n}-r_{n-1}\right)$ and $I$ is the 3×3 identity matrix.

The governing equations of the $n$th element can be developed using Hamilton's principle.
$$
\boldsymbol{F}=\boldsymbol{M}_{s} \ddot{\boldsymbol{d}}+\boldsymbol{A}_{D} \boldsymbol{d}+\boldsymbol{C}_{D} \boldsymbol{\phi}, \tag{10}
$$
$$
\boldsymbol{D}_{r}=\boldsymbol{C}_{D}^{\mathrm{T}} \boldsymbol{d}-\boldsymbol{G}_{D} \boldsymbol{\phi}, \tag{11}
$$
where the double dots denote the second derivative with respect to time $t$, and $\boldsymbol{F}$ and $\boldsymbol{D}_{r}$ are the nodal external traction vector and nodal electric displacement in the $r$-direction, respectively. $\boldsymbol{M}_{s}$ represents the elastic mass matrix. $\boldsymbol{A}_{D}, \boldsymbol{C}_{D}$ and $\boldsymbol{G}_{D}$ are the mass matrix, elastic stiffness matrix, piezoelectric coupling matrix and dielectric stiffness matrix respectively. The detailed expression of each matrix can be referred in literature [13,16].

Introducing the following matrices and vectors:
$$
\begin{gathered}
\boldsymbol{K}_{D}=\left[\begin{array}{cc}
\boldsymbol{A}_{D} & \boldsymbol{C}_{D} \\
\boldsymbol{C}_{D}^{\mathrm{T}} & -\boldsymbol{G}_{D}
\end{array}\right], \boldsymbol{M}=\left[\begin{array}{cc}
\boldsymbol{M}_{s} & 0 \\
0 & 0
\end{array}\right], \\
\boldsymbol{T}^{\mathrm{T}}=\left[\begin{array}{ll}
\boldsymbol{F}^{\mathrm{T}} & \boldsymbol{D}_{r}^{\mathrm{T}}
\end{array}\right], \boldsymbol{\Psi}^{\mathrm{T}}=\left[\begin{array}{ll}
\boldsymbol{d}^{\mathrm{T}} & \boldsymbol{\phi}^{\mathrm{T}}
\end{array}\right].
\end{gathered}
$$

Eqs. (10) and (11) can be expressed as a combined representation which is a set of differential equations with respect to $z, \theta$, and $t$.
$$
\boldsymbol{T}=\boldsymbol{M} \ddot{\boldsymbol{\Psi}}+\boldsymbol{K}_{D} \boldsymbol{\Psi}, \tag{12}
$$

Assembling the matrix of all the adjacent annular elements, the governing equation for the entire piezoelectric cylindrical shell is obtained.
$$
\boldsymbol{T}_{t}=\boldsymbol{M}_{t} \ddot{\boldsymbol{\psi}}_{t}+\boldsymbol{K}_{D t} \boldsymbol{\psi}_{t}, \tag{13}
$$
where $M_{t}$ is the global mass matrix, and $K_{D t}$ is the global stiffness matrix.

## 2 Transient response in the transformed domain

We introduce the Fourier transformation with respect to the coordinates $z$ and $\theta$ as follows:
$$
\tilde{\boldsymbol{\psi}}_{t}\left(k_{z}, k_{\theta}, t\right)=\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} \boldsymbol{\psi}_{t}(z, \theta, t) \mathrm{e}^{-\mathrm{i} k_{z}} \mathrm{e}^{-\mathrm{i} k_{\theta}} \mathrm{d} z \mathrm{~d} \theta, \tag{14}
$$
where $\mathrm{i}=\sqrt{-1} ; k_{z}$, and $k_{\theta}$ possess the features of wave numbers in the circumferential direction and in the $z$-axis direction respectively.

Applying the above Fourier transformation to eq. (13) leads to the transformed governing equation in the wave number domain:
$$
\tilde{\boldsymbol{T}}_{t}=\boldsymbol{M}_{t} \ddot{\tilde{\boldsymbol{\psi}}}_{t}+\boldsymbol{K}_{t} \tilde{\boldsymbol{\psi}}_{t}, \tag{15}
$$
where $\tilde{\boldsymbol{T}}_{t}, \ddot{\tilde{\boldsymbol{\psi}}}_{t}$, and $\tilde{\boldsymbol{\psi}}_{t}$ are the corresponding terms in

the transformed domain of $T_{t}$, $\ddot{\psi}_{t}$, and $\psi_{t}$; the global stiffness matrix $M_{t}$ and the mass matrix $K_{t}$ are given by

$$
\boldsymbol{K}_{t}=\left[\begin{array}{cc}
\boldsymbol{A}_{t} & \boldsymbol{C}_{t} \\
\boldsymbol{C}_{t}^{\mathrm{T}} & -\boldsymbol{G}_{t}
\end{array}\right], \quad \boldsymbol{M}_{t}=\left[\begin{array}{cc}
\boldsymbol{M}_{\mathrm{st}} & 0 \\
0 & 0
\end{array}\right],
\tag{16}
$$

in which

$$
\boldsymbol{A}_{t}=k_{z}^{2} \boldsymbol{A}_{1 t}+k_{z} k_{\theta} \boldsymbol{A}_{2 t}+k_{\theta}^{2} \boldsymbol{A}_{3 t}+\mathrm{i} k_{z} \boldsymbol{A}_{4 t}+\mathrm{i} k_{\theta} \boldsymbol{A}_{5 t}+\boldsymbol{A}_{6 t}. \tag{17}
$$

The expressions of piezoelectric coupling matrix $C_{t}$ and dielectric stiffness matrix $G_{t}$ are formulated by substituting A into eq. (17) with $C$ and $G$.

The following boundary conditions are considered. When the piezoelectric cylindrical shell is excited by mechanical loads, the mechanical and electrical boundary conditions indicated by eq. (18) are used for investigation. And when the electrode excitation is loaded, the boundary conditions indicated by eq. (19) should be satisfied:

$$
\tilde{\boldsymbol{F}}_{\mathrm{t}}=\hat{\tilde{\boldsymbol{F}}}_{\mathrm{t}}, \quad \tilde{\boldsymbol{D}}_{r t}=0,
\tag{18}
$$

$$
\tilde{\boldsymbol{F}}_{t}=0, \tilde{\boldsymbol{D}}_{r t}=0, \tilde{\phi}_{t i}=\tilde{\phi}_{\mathrm{e}},
\tag{19}
$$

where subscript $i$ denotes that the electrode excitation is loaded onto the $i$th nodal annual surface.

In eqs. (15) and (16), the dimension of matrix $K_{t}$ and $M_{t}$ is $4 \times(2 N+1)$, and, except for the elastic mass matrix, all the entries of the global mass matrix equal 0. This indicates that for the electro-potential vector, there is no derivation with respect to time $t$. Hence, we change eq. (15) into the following form:

$$
\tilde{\boldsymbol{F}}_{t}+\tilde{\boldsymbol{F}}_{\mathrm{te}}=\boldsymbol{M}_{\mathrm{st}} \ddot{\tilde{\boldsymbol{d}}}_{t}+\boldsymbol{K}_{\mathrm{st}} \tilde{\boldsymbol{d}}_{t},
\tag{20}
$$

$$
\tilde{\phi}_{t}=\boldsymbol{G}_{D}^{-1} \boldsymbol{C}_{D}^{\mathrm{T}} \tilde{\boldsymbol{d}}_{t}-\boldsymbol{G}_{D}^{-1} \tilde{\boldsymbol{D}}_{r t},
\tag{21}
$$

where

$$
\boldsymbol{K}_{\mathrm{st}}=\boldsymbol{A}_{t}+\boldsymbol{C}_{t} \boldsymbol{G}_{t}^{-1} \boldsymbol{C}_{t}^{\mathrm{T}},
\tag{22}
$$

$$
\tilde{\boldsymbol{F}}_{\mathrm{te}}=\boldsymbol{C}_{t} \boldsymbol{G}_{t}^{-1} \tilde{\boldsymbol{D}}_{r t}.
\tag{23}
$$

The dimension of the reduced global stiffness matrix and mass matrix $K_{\text {st }}$ and $M_{\text {st }}$ is $3 \times(2 N+1)$. The matrix $K_{\text {st }}$ possesses the features of an elastic stiffness matrix, piezoelectric coupling matrix and dielectric stiffness matrix. $\tilde{\boldsymbol{F}}_{\text {te }}$ can be regarded as the equivalent mechanical load in the transformed domain excited by the electrode.

When mechanical excitation is loaded, the piezoelectric cylindrical shell is electrically open, and $\tilde{\boldsymbol{F}}_{\text {te }}=0$. Hence, solving the solution of the reduced-order governing equation eq. (20) is exactly the same as solving the governing equation of the laminated cylindrical shell with the implementation of HNM. When the electrode is excited on the surface of the piezoelectric cylindrical shell, the forced electrical boundary conditions in eq. (19) should be satisfied. Assuming the electrically loaded surface is fully insulated, suppose the specified electro-potential in the transformed domain on the loading surface is $\tilde{\phi}_{\mathrm{e}}$. The boundary conditions can be satisfied by replacing the $i \times i$ element $\boldsymbol{G}_{t i i}$ in the dielectric stiffness matrix $G_{t}$ with a large value $\alpha$, so the corresponding element $\tilde{D}_{r t i}$ in vector $\tilde{\boldsymbol{D}}_{r t}$ is set as $\alpha \tilde{\phi}_{\mathrm{e}}$. The nodal excitation in the governing equation eq. (20), into which the modified $G_{t}$ and $\tilde{\boldsymbol{D}}_{r t}$ are substituted, represents the superposition of the mechanical load and the equivalent mechanical load.

When no mechanical or electrical excitation is applied on the piezoelectric cylindrical shell, eq. (20) is transformed into the corresponding eigenvalue problem expressed by eq. (24). Note that the solutions of eq. (24) can be used directly for analysis of characteristic waves of the piezoelectric cylindrical shell [13], as this is also exactly the equation of free wave motion obtained by assuming the responses take the form of the harmonic circular cylindrical wave, which is mathematically identical to the complex double Fourier series expansion.

$$
\boldsymbol{K}_{\mathrm{st}} \tilde{\boldsymbol{d}}_{t}-\omega^{2} \boldsymbol{M}_{\mathrm{st}} \tilde{\boldsymbol{d}}_{t}=0,
\tag{24}
$$

Solving eq. (24), for any given $k_{z}, k_{\theta}$ we can obtain a set of eigen-frequencies $\omega_{m}(m=1,2, \ldots, 3(2 N+1))$ and the corresponding left and right eigenvectors $\boldsymbol{\Lambda}_{m}^{\mathrm{L}}$ and $\boldsymbol{\Lambda}_{m}^{\mathrm{R}}$. Using modal analysis and Duhamel's integral methods, the transient responses of displacement $\tilde{\boldsymbol{d}}_{t}$ and electro-potential $\tilde{\boldsymbol{\phi}}$ in the transformed domain are obtained [17]. For example, consider a piezoelectric cylindrical shell excited by a mechanical load with a time-history defined as the Heaviside function, then the displacement response in the transformed domain is formulated as eq. (25).

$$
\boldsymbol{d}_{t}\left(k_{z}, k_{\theta}, t\right)=\sum_{m=1}^{M} \frac{\boldsymbol{\Lambda}_{m}^{\mathrm{L}} \tilde{\boldsymbol{F}} \boldsymbol{\Lambda}_{m}^{\mathrm{R}}\left(1-\cos \omega_{m} t\right)}{\omega_{m}^{2} \boldsymbol{\Lambda}_{m}^{\mathrm{L}} \boldsymbol{M}_{s t} \boldsymbol{\Lambda}_{m}^{\mathrm{R}}},
\tag{25}
$$

We substitute eq. (25) into eq. (21), then the electro-potential response in the transformed domain is obtained.

## 3 Transient response in the space domain

Performing the inverse Fourier Transformation with respect to $k_{z}$ and $k_{\theta}$, the displacement response and the electro-potential response in the space domain are obtained.

$$
\left\{\begin{array}{l}
\boldsymbol{d}_{t}(z, \theta, t)=\left(\frac{1}{2 \pi}\right)^{2} \iint_{-\infty}^{+\infty} \boldsymbol{d}_{t}\left(k_{z}, k_{\theta}, t\right) \mathrm{e}^{\mathrm{i} k_{z}} \mathrm{e}^{\mathrm{i} k_{\theta}} \mathrm{d} k_{z} \mathrm{~d} k_{\theta} \\
\boldsymbol{\phi}(z, \theta, t)=\left(\frac{1}{2 \pi}\right)^{2} \iint_{-\infty}^{+\infty} \tilde{\boldsymbol{\phi}}\left(k_{z}, k_{\theta}, t\right) \mathrm{e}^{\mathrm{i} k_{z}} \mathrm{e}^{\mathrm{i} k_{\theta}} \mathrm{d} k_{z} \mathrm{~d} k_{\theta}
\end{array}\right.
\tag{26}
$$

In numerical computation, the integration in eq. (26) can be carried out with numerical methods such as iFFT.

## 4 Numerical example

Consider a piezoelectric cylindrical shell consisting of two laminas with the same thickness. The materials of the inner and outer laminas are PVDF and PZT-5A respectively. Properties of these two materials are listed in Table 1. The outer radius is $\bar{R}_{2}=20$. In numerical computation, both laminas are evenly divided into four layered annular elements, in other words, the entire piezoelectric cylindrical shell is discretized into 54 annular nodal surfaces.

In this numerical example, the circular line load, which is independent of coordinate $\theta$, is considered. Hence, the governing equation eq. (13) turns into the differential equation which is also independent of $\theta$. Thus, analysis of the transient responses of the piezoelectric cylindrical shell subjected to the circular line load is simplified to a two-dimensional problem. Formulation of the two-dimensional problem can be easily derived from the three-dimensional counterpart elaborated above by neglecting all the partial differential components with respect to $\theta$. Accordingly, eq. (25) is simplified to a one-dimensional inverse Fourier transformation from wave number $k_{z}$ to space domain coordinate $z$. The following dimensionless parameters are used:

$$
\begin{aligned}
& \bar{t}=t / t_{0}, t_{0}=H / c_{0}, c_{0}=\sqrt{c_{66} / \rho_{0}}, \bar{r}=r / H, \\
& \bar{z}=z / H, \bar{k}_{z}=k_{z} H, \bar{u}=u / u_{0}, \\
& \bar{v}=v / u_{0}, \bar{w}=w / u_{0}, u_{0}=H f_{0} / c_{66}, \\
& \bar{\varphi}=\varphi / \varphi_{0}, \varphi_{0}=\left(e_{s} H f_{0}\right) /\left(g_{s} c_{66}\right)
\end{aligned}
\tag{27}
$$

<table>
<caption>Table 1 Material property of PZT-5A and 0° PVDF [18]</caption>
<thead>
<tr>
<th>Material property</th>
<th>PZT-5A</th>
<th>0° PVDF</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_{11}$ (GPa)</td>
<td>99.200</td>
<td>238.240</td>
</tr>
<tr>
<td>$C_{22}$ (GPa)</td>
<td>99.200</td>
<td>23.600</td>
</tr>
<tr>
<td>$C_{33}$ (GPa)</td>
<td>86.856</td>
<td>10.640</td>
</tr>
<tr>
<td>$C_{12}$ (GPa)</td>
<td>54.016</td>
<td>3.980</td>
</tr>
<tr>
<td>$C_{13}$ (GPa)</td>
<td>50.778</td>
<td>2.190</td>
</tr>
<tr>
<td>$C_{23}$ (GPa)</td>
<td>21.100</td>
<td>1.920</td>
</tr>
<tr>
<td>$C_{44}$ (GPa)</td>
<td>21.100</td>
<td>2.150</td>
</tr>
<tr>
<td>$C_{55}$ (GPa)</td>
<td>21.100</td>
<td>4.400</td>
</tr>
<tr>
<td>$C_{66}$ (GPa)</td>
<td>22.593</td>
<td>6.430</td>
</tr>
<tr>
<td>$e_{31}$ (cm⁻²)</td>
<td>−7.209</td>
<td>−0.130</td>
</tr>
<tr>
<td>$e_{32}$ (cm⁻²)</td>
<td>−7.209</td>
<td>−0.145</td>
</tr>
<tr>
<td>$e_{33}$ (cm⁻²)</td>
<td>15.118</td>
<td>−0.276</td>
</tr>
<tr>
<td>$e_{24}$ (cm⁻²)</td>
<td>12.320</td>
<td>−0.009</td>
</tr>
<tr>
<td>$e_{15}$ (cm⁻²)</td>
<td>12.322</td>
<td>−0.135</td>
</tr>
<tr>
<td>$g_{11}$ ($10^{-10}$Fm⁻¹)</td>
<td>153.00</td>
<td>1.1068</td>
</tr>
<tr>
<td>$g_{22}$ ($10^{-10}$Fm⁻¹)</td>
<td>153.00</td>
<td>1.1068</td>
</tr>
<tr>
<td>$g_{33}$ ($10^{-10}$Fm⁻¹)</td>
<td>153.00</td>
<td>1.1068</td>
</tr>
<tr>
<td>$\rho$ ($10^{3}$kg m⁻³)</td>
<td>7.750</td>
<td>7.800</td>
</tr>
</tbody>
</table>

where $\rho_{0}$ and $c_{66}$ stand for the mass density and material constant of PZT-5A material respectively, $c_{0}$ is the shear wave velocity in the z-direction within the PZT-5A medium, and $t_{0}$ is the time for this shear wave to travel across one dimensionless unit length. $e_{s}$=C² m⁻² and $g_{s}$=$10^{-10}$ F m⁻¹ are the reference piezoelectric and dielectric properties respectively. When the piezoelectric cylindrical shell is subjected to mechanical loads, $f_{0}$=$q_{0}$. When electrode excitation is loaded, $f_{0}$=$e_{s}p_{0}/H$, where $q_{0}$, and $p_{0}$ are unit values of mechanical and electro-potential excitations.

In the numerical computation, a circular mechanical line load in the radial direction with the time history of one cycle of a sine function is applied to the outer surface of the piezoelectric cylindrical shell. The expression of mechanical excitation is formulated in eq. (28).

$$
\boldsymbol{F}_{t}=f(t) \delta(z) \boldsymbol{Q}_{t}, \tag{28}
$$

where $\delta(z)$ stands for the delta function:

$$
\begin{gathered}
f(t)=
\begin{cases}
\sin \left(2 \pi t / t_{d}\right), & 0<t<t_{d}, \\
0, & t<0, t>t_{d},
\end{cases}
\quad \overline{t_{d}}=4 ; \\
\boldsymbol{Q}_{t}=\left[\begin{array}{llllll}
0 & 0 & q_{0} & 0 & \cdots & 0
\end{array}\right]. \tag{29}
\end{gathered}
$$

Meanwhile, assuming an electro-potential excitation with the time history of a Heaviside function is loaded onto the inner surface of the cylindrical shell, then the electro-potential distribution on the inner surface is formulated by eq. (30).

$$
\phi_{e}=10 H e_{s} q_{0} \delta(z) H(t) / g_{s} c_{66}, \tag{30}
$$

where $H(t)$ is the Heaviside function.

Figure 2 shows the responses of the displacement in the radial direction at $\bar{z}$=10 on the inner, middle and outer surfaces of the piezoelectric cylindrical shell, respectively, which are subjected to the coupled electro-potential circular line load denoted by eqs. (29) and (30). It can be seen that at the dimensionless time around 23, a drastic change in the response is observed on the inner surface where the lamina material is PVDF. This surface wave is excited by the electro-potential excitation. It can be seen from this figure that its energy exhibits a strong concentration on the inner lamina side, and but is barely observed on the outer surface of the cylindrical shell where the lamina consists of PZT-5A material with a much stronger dielectric property compared with PVDF. It can also be confirmed that, before this surface wave excited by electro-potential excitation arrives, the displacement response magnitudes, which mainly depend on the elastic property, do not vary significantly along the radial direction, because the order of magnitude of piezoelectric and dielectric coefficients is far less than that of elastic ones. Figure 3 compares the responses on the inner surfaces of the piezoelectric cylindrical shell and a cylindrical shell with the same mechanical properties, which are

![](./images/811688663040655360_2.jpg)

Figure 2 Time histories of displacement $\bar{w}$ at $\bar{z}$=10 on three surfaces subjected to electrode excitation on the surface of PVDF and mechanical excitation on the surface of PZT-5A.

![](./images/811688663040655360_3.jpg)

Figure 3 Comparison between responses of a piezoelectric cylindrical shell and the corresponding cylindrical shell without piezoelectric properties, subjected to the mechanical load on its outer surfaces.

subjected to a mechanical load denoted by eq. (29). As the influence of piezoelectric properties is less visible without the electrical excitation, the shapes of the two curves are very similar, but the piezoelectric characteristic does decrease the arrival time of elastic waves. In addition, the absence of those abrupt changes demonstrates that the surface waves observed in Figure 2 are the results of the electrical excitation.

Figure 4 shows the responses of the displacement in the axial direction on the inner, middle and outer surfaces at the dimensionless time $\bar{t}$=10. From this figure, it can be found that at the arrival position of the surface wave subjected to the electro-potential excitation illustrated in Figure (2), a sudden change of displacement magnitude is also observed, the energy of which is more concentrated on the inner surface compared with the displacement response in the radial direction. Its existence cannot be visually confirmed on the outer and middle annular surfaces. Figure 5 illustrates the comparison of displacement responses in the axial direction at $\bar{z}$=10 on the inner surface of the cylindrical shell, which are excited by a mechanical load denoted by eq. (29) and the coupled excitation denoted by eqs. (29) and (30), respectively.

![](./images/811688663040655360_4.jpg)

Figure 4 Responses of displacement $\bar{u}$ on the inner/middle/outer surfaces subjected to an electrode excitation on the surface of the PVDF and mechanical excitation on the surface of PZT-5A ($\bar{t}$=10).

Figure 6 shows the distribution of electro-potential on the inner, middle and outer surfaces of the cylindrical shell subjected to a mechanical load denoted by eq. (29) on the outer surface, at the dimensionless time $\bar{t}$=10. The piezoelectric cylindrical shell is electrically open. It may be seen that the variation of amplitude along the thickness direction is more remarkable than that of Figure 2, and the responses are concentrated on the inner surface of the cylindrical shell, the extent of which is not as remarkable as that of the surface waves we observed in Figures 2 and 4.

![](./images/811688663040655360_5.jpg)

Figure 5 Comparison of responses $\bar{u}$ at $\bar{z}$=10 on the surface of the PVDF excited by a mechanical load and a coupled electro-mechanical load.

![](./images/811688663040655360_6.jpg)

Figure 6 Electrostatic potential responses on the inner, middle, and outer surfaces $(\bar{t}=10)$ excited by a mechanical line load with the time history of one cycle of a sine function.

## 5 Conclusion
A numerical method is proposed for the analysis of transient responses in a multilayered piezoelectric cylindrical shell. Based on the coupled electro-elastic theory and Hamilton's Principle, the governing differential equations of the piezoelectric cylindrical shell are formulated. By employing the Fourier transformation and three nodal line approximation, the solutions for the governing differential equations can be obtained by the integration with respect to wave-number, which is convenient in numerical computation. With introduction of the layered annular element, the presented method is flexible for dealing with a multi-layered piezoelectric cylindrical shell consisting of an arbitrary number of material layers or any type of piezoelectric material. As the displacement and electro-potential field are discretized only in the wall thickness direction, the accuracy is fairly well maintained without the expense of lower efficiency or more cost of computer memory in obtaining the numerical simulation, which yields better practicality for many associated applications, such as the inverse analysis for material characterization, etc. The numerical examples have demonstrated the functionality of the present method.

This work was supported by the China National Funds for Distinguished Young Scientists (Grant Nos. 10725208), a research grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Grant No. CityU 113809), and the National Natural Science Foundation of China (Grant Nos. 10802028).

1 Gao J X, Shen Y P, Wang J. Three dimensional analysis for free vibration of rectangular composite laminates with piezoelectric layers. J Sound Vib, 1998, 213: 383-390

2 Wu X H, Shen Y P. Three-dimensional solution for the free vibration of functionally gradient piezoelectric plates. Acta Mech Solida Sin, 2003, 24: 75-82

3 Li X F. Electroelastic field induced by thin interface electrodes between two bonded dissimilar piezoelectric ceramics. Sci China Ser G-Phys Mech Astron, 2006, 49: 526-539

4 Yan W, Chen W Q. Electro-mechanical response of functionally graded beams with imperfectly integrated surface piezoelectric layers. Sci China Ser G-Phys Mech Astron, 2006, 49: 513-525

5 Cheng Z Q, Lim C W, Kitipornchai S. Three-dimensional exact solution for inhomogeneous and laminated piezoelectric plates. Int J Solids Struct, 1999, 37: 1425-1439

6 Cheng Z Q, Lim C W, Kitipornchai S. Three-dimensional asymptotic approach to inhomogeneous and laminated piezoelectric plates. Int J Solids Struct, 2000, 37: 3153-3175

7 Chen W Q, Ding H J. On free vibration of a functionally graded piezoelectric rectangular plate. Acta Mech, 2002, 153: 207-216

8 Ding H J, Wang H M, Hou P F, et al. The transient responses of piezoelectric hollow cylinders for axisymmetric plane strain problems. Int J Solids Struct, 2003, 40: 105-123

9 Liu H, Wang T J, Wang Z K, et al. Effect of initial stress on the propagation behavior of generalized Rayleigh waves in layered piezoelectric structures. Acta Mech Sin, 2000, 32: 491-496

10 Liu G R, Tani J, Ohyoshi T, et al. Characteristic wave surfaces in anisotropic laminated plates. J Vib Acoust, 1991, 113: 279-285

11 Liu G R, Xi Z C. Elastic Waves in Anisotropic Laminates. Boca Raton: CRC Press Inc., 2002

12 Han X, Liu G R. Elastic waves in a functionally graded piezoelectric cylinder. Smart Mater Struct, 2003, 12: 962-971

13 Han X, Liu G R, Ohyoshi T, et al. Dispersion and characteristic surfaces of waves in hybrid multilayered piezoelectric circular cylinders. Comput Mech, 2004, 33: 334-344

14 Han X, Xu D, Liu G R, et al. Transient responses in a functionally graded cylindrical shell to a point load. J Sound Vib, 2002, 251: 783-805

15 Rogacheva N N. The theory of piezoelectric shells and plates. Boca Raton: CRC Press Inc., 1993. 3-10

16 Han X, Liu G R, Xi Z C, et al. Characteristics of waves in a functionally graded cylinder. Int J Numer Meth Eng, 2002, 53: 653-676

17 Liu G R, Tani J. Surface waves in functionally gradient piezoelectric plates. J Vib Acoust, 1994, 116: 440-448

18 Vel S S, Batra R C. Three-dimensional analytical solution for hybrid multilayered piezoelectric plates. J Appl Mech, 2000, 67: 558-567