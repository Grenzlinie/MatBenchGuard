# A Semianalytical Spectral Element Method for the Analysis of 3-D Layered Structures

Jiefu Chen, Bao Zhu, Wanxie Zhong, and Qing Huo Liu, *Fellow, IEEE*

Abstract—A semianalytical spectral element method (SEM) is proposed for electromagnetic simulations of 3-D layered structures. 2-D spectral elements are employed to discretize the cross section of a layered structure, and the Legendre transformation is then used to cast the semidiscretized problem from the Lagrangian system into the Hamiltonian system. A Riccati equation-based high precision integration method is utilized to perform integration along the longitudinal direction, which is the undiscretized direction, to generate the stiffness matrix of the whole layered structure. The final system of equations by the semianalytical SEM will take the form of a set of linear equations with a block tri-diagonal matrix, which can be solved efficiently by the block Thomas algorithm. Numerical examples demonstrate the high efficiency and accuracy of the proposed method.

Index Terms—Block Thomas algorithm, block tri-diagonal matrix, finite-element method (FEM), Gauss–Lobatto–Legendre (GLL) polynomials, Hamiltonian system, high precision integration (HPI) method, Lagrangian system, layered structure, Riccati equation, semianalytical spectral element method (SEM).

## I. INTRODUCTION

ELECTROMAGNETIC simulations of layered structures are frequently encountered in many areas such as integrated optics, geophysical prospecting, and electronic packaging [1]–[3]. As shown in Fig. 1, the interconnect structure in packaging problems is a typical layered structure. It contains several parallel layers along a specific direction, which is referred to as the longitudinal direction hereinafter. Each layer is homogeneous along the longitudinal direction; while its geometry as well as material distribution can be arbitrary on the transverse plane, i.e., the plane perpendicular to the longitudinal direction. Due to the flexibility in geometric modeling, the finite-element method (FEM) can be employed to perform full wave analysis, and thus to obtain the electrical properties of layered structures. However, as the number of layers and the complexity of each layer increase, directly using the FEM to discretize the whole structure may lead to a huge system of coupled equations, thus making the overall efficiency of conventional FEM very low for the analysis of layered structures.

![](./images/811701226881155074_1.jpg)

Fig. 1. Interconnect problem is a typical layered structure. The structure can be divided into $N$ layers. The geometry and material distribution of each layer are homogeneous along the longitudinal direction, but can be arbitrary in the transverse plane.

The piecewise homogeneity of layered structures along the longitudinal direction can be exploited to improve the efficiency of the conventional FEM. The numerical mode-matching method (NMM) [4], [5] breaks a whole 3-D (or 2-D) layered structure into $N$ regions. After obtaining the eigenmodes of each region by 2-D FEM, the $N$-region wave propagation problem can be solved by introducing generalized reflection and transmission operators. The NMM can reduce a 3-D problem into several 2-D problems, thus greatly decreasing the number of unknowns, and consequently, memory cost and computation time. This method has been applied to various geophysical subsurface sensing problems and open-region waveguide discontinuity problems [6]–[8]. The layered finite element (LAFE) method is another efficient FEM method designed for layered structures [9]–[11]. The LAFE method starts from a 3-D mesh for a 3-D layered structure, and then reduces a 3-D layered system into a 2-D layered system by eliminating volume unknowns, which will be recovered after the 2-D layered system is solved. This method can be used in both time- and frequency-domain simulations.

Here, we proposed a semianalytical spectral element method (SEM) for the analysis of layered structures. A piecewise homogeneous 3-D layered structure is first divided into several substructures homogeneous along the longitudinal direction. 2-D scalar and vector spectral elements [12]–[14], which are special types of a higher order FEM, are used to represent longitudinal and transverse unknowns on the cross section of each

Manuscript received October 15, 2009; accepted September 01, 2010. Date of publication November 15, 2010; date of current version January 12, 2011.

J. Chen and Q. H. Liu are with the Department of Electrical and Computer Engineering, Duke University, Durham NC 27708-0291 USA (e-mail: jiefu.chen@duke.edu; qhliu@ee.duke.edu).

B. Zhu and W. Zhong are with the Department of Engineering Mechanics, Dalian University of Technology, Dalian 116024, China (e-mail: zhubao.dlut@gmail.com; wxzhong@dlut.edu.cn).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TMTT.2010.2090408

substructure, respectively. The semidiscretized system is then transformed from the Lagrangian system into the Hamiltonian system, where a Riccati-based high precision integra- tion (HPI) [15]–[17] method is utilized to perform integration along the the longitudinal direction and to generate the stiffness matrix of a substructure. No matter how long a substructure is, HPI for the semidiscretized system can achieve machine preci- sion, i.e., the numerical errors of longitudinal integration by HPI can be as small as the round-off error on a computer. Stiffness matrices of substructures can be directly assembled to a global system matrix taking the form of a block tri-diagonal matrix. A block Thomas algorithm [18] is employed here to solve the final system of equations with high efficiency.

In this paper, we will discuss the proposed method as:. Section II governing equation and corresponding functional, Section III 2-D spectral elements for discretization of substruc- ture's cross section, Section IV semidiscretized system in the Lagrangian system, Section V Hamiltonian system and Riccati equations, Section VI HPI method, Section VII block Thomas algorithm for block tri-diagonal matrix, Section VIII numerical examples, and Section IX conclusion.

## II. GOVERNING EQUATION AND FUNCTIONAL

Consider an $N$-layer piecewise homogeneous structures shown in Fig. 1. Within each layer, the geometry and material distribution are homogeneous along the longitudinal direction, but can be arbitrary on the cross section. For such a structure, we can decompose it into $N$ layers along the longitudinal direction and treat each layer as a substructure. Each substruc- ture is modeled by the proposed semianalytical SEM and then be assembled into a global discretized system of the whole structure. Details are elaborated as follows.

Consider a substructure as shown in Fig. 2. $\Omega$ denotes the cross section of the substructure, which is laid on the $xy$ plane. The substructure has a finite length along the $z$ axis (longitu- dinal direction). The $z$ coordinates of the left and right end are assumed as $z_a$ and $z_b$, respectively. We first omit the excita- tion terms, which will be imposed onto the global discretized system after all substructures are assembled together. The gov- erning equation for the substructure is

$$
\nabla \times \left(\frac{1}{\mu_{r}} \nabla \times \mathbf{E}\right)-k_{0}^{2} \epsilon_{r} \mathbf{E}=0, \quad \text { in } \Omega \times\left[z_{a}, z_{b}\right] \quad(1)
$$

where $\epsilon_{r}$ and $\mu_{r}$ denote the relative permittivity and relative permeability, respectively. $k_0$ denotes the wavenumber in the vacuum. Without loss of generality, we can always assume the circumference of the substructure is comprised by a perfect electric conductor (PEC) $\partial\Omega_1$ and perfect magnetic conductor (PMC) $\partial\Omega_2$, i.e.,

$$
\hat{\mathbf{n}} \times \mathbf{E}=\mathbf{0}, \quad \text { on } \partial \Omega_{1} \quad(2)
$$

$$
\hat{\mathbf{n}} \times(\nabla \times \mathbf{E})=\mathbf{0}, \quad \text { on } \partial \Omega_{2}. \quad(3)
$$

For open region problems (with respect to the $x$ and $y$ direction), we can always apply a perfectly matched layer (PML) to enclose the cross section and then let the outermost circumference be a PEC or PMC.

![](./images/811701226881155074_2.jpg)

Fig. 2. One layer of a layered structure is treated as a substructure and mod- eled by the semianalytical SEM. This substructure is homogeneous along the $z$ direction, but can be inhomogeneous along the $x$ and $y$ directions.

The one-variable functional corresponding to the above gov- erning equation and boundary conditions is

$$
\begin{aligned}
\Pi(\mathbf{E})=\frac{1}{2} \int_{z_{a}}^{z_{b}} \iint_{\Omega} \frac{1}{\mu_{r}}(\nabla \times \mathbf{E}) & \cdot(\nabla \times \mathbf{E}) d \Omega d z \\
& -\frac{1}{2} \int_{z_{a}}^{z_{b}} \iint_{\Omega} k_{0}^{2} \epsilon_{r} \mathbf{E} \cdot \mathbf{E} d \Omega d z \quad(4)
\end{aligned}
$$

with the unspecified fields $\mathbf{E}$ on the left end $z = z_a$ and right end $z = z_b$.

Field $\mathbf{E}$ can be decomposed into transverse and longitudinal components

$$
\mathbf{E}=\mathbf{E}_{t}+\mathbf{E}_{z} \quad(5)
$$

where

$$
\mathbf{E}_{t} \triangleq\left(E_{x} \hat{\mathbf{x}}+E_{y} \hat{\mathbf{y}}\right) \quad \mathbf{E}_{z} \triangleq E_{z} \hat{\mathbf{z}}. \quad(6)
$$

Operator $\nabla$ can also be decomposed into a transverse operator and longitudinal operator

$$
\nabla=\nabla_{t}+\hat{\mathbf{z}} \frac{\partial}{\partial z} \quad(7)
$$

where

$$
\nabla_{t} \triangleq \hat{\mathbf{x}} \frac{\partial}{\partial x}+\hat{\mathbf{y}} \frac{\partial}{\partial y}. \quad(8)
$$

With (5) and (7), the functional (4) can be expressed as

$$
\begin{aligned}
& \Pi\left(\mathbf{E}_{t}, E_{z}\right) \\
& =\frac{1}{2} \int_{z_{a}}^{z_{b}} \iint_{\Omega}\left[\frac{1}{\mu_{r}}\left(\nabla_{t} \times \mathbf{E}_{t}\right) \cdot\left(\nabla_{t} \times \mathbf{E}_{t}\right)\right. \\
& \quad+\frac{1}{\mu_{r}}\left(\nabla_{t} E_{z}\right) \cdot\left(\nabla_{t} E_{z}\right)+\frac{1}{\mu_{r}} \dot{\mathbf{E}}_{t} \cdot \dot{\mathbf{E}}_{t} \\
& \quad-\frac{1}{\mu_{r}}\left(\nabla_{t} E_{z}\right) \cdot \dot{\mathbf{E}}_{t}-\frac{1}{\mu_{r}} \dot{\mathbf{E}}_{t} \cdot\left(\nabla_{t} E_{z}\right) \\
& \left.\quad-k_{0}^{2} \epsilon_{r} \mathbf{E}_{t} \cdot \mathbf{E}_{t}-k_{0}^{2} \epsilon_{r} E_{z} E_{z}\right] d \Omega d z \quad(9)
\end{aligned}
$$

where $\dot{\mathbf{E}}_{t} \triangleq(\partial \mathbf{E}_{t}) /(\partial z)$.

![](./images/811701226881155074_3.jpg)

Fig. 3. Schematics of 2-D spectral elements for semianalytical SEM. The 2-D scalar spectral element is shown in (a), which is used to represent longitudinal field components. The 2-D vector spectral element consists of (b) and (c), which are employed to represent transverse field components. Both scalar and vector spectral elements are defined in a unit square in the reference domain, and they can be curved quadrilaterals in the physical domain after geometric transformation. $M=3$ is illustrated in this figure.

## III. 2-D SPECTRAL ELEMENTS FOR CROSS SECTION

2-D spectral elements are used to discretize the substructure's cross section. More specifically, 2-D vector spectral element and scalar spectral element are employed to discretize the transverse component $\mathbf{E}_{t}$ and the longitudinal component $E_{z}$, respectively. The spectral element [12]-[14] is a special type of higher order finite element with sampling points defined as the Gauss-Lobatto-Legendre (GLL) points, which are roots of the derivatives of the GLL polynomials. By choosing GLL points rather than equal-spaced grids as sampling points, the spectral element can avoid the well-known Runge phenomenon [19] and achieve spectral accuracy, which means the numerical results can converge exponentially as the increase of interpolation order of basis functions.

As shown in Fig. 3, the 2-D spectral elements are defined in the reference domain $(\xi, \eta) \in[-1,1] \times[-1,1]$. The basis function of the 2-D scalar spectral element with $M$th order of interpolation is defined as

$$
N_{z}^{e}(\xi, \eta)=\phi_{m}^{(M)}(\xi) \phi_{p}^{(M)}(\eta)
$$

and the basis function of the 2-D vector spectral element contains two components

$$
\left\{\begin{aligned}
\mathbf{N}_{t \xi}^{e}(\xi, \eta) & =\hat{\boldsymbol{\xi}} \phi_{m}^{(M-1)}(\xi) \phi_{p}^{(M)}(\eta) \\
\mathbf{N}_{t \eta}^{e}(\xi, \eta) & =\hat{\boldsymbol{\eta}} \phi_{m}^{(M)}(\xi) \phi_{p}^{(M-1)}(\eta)
\end{aligned}\right.
$$

where

$$
\phi_{m}^{(M)}(\xi)=\frac{-\left(1-\xi^{2}\right) L_{M}^{\prime}(\xi)}{M(M+1) L_{M}\left(\xi_{m}\right)\left(\xi-\xi_{m}\right)}, \quad m=0, \ldots, M
$$

$L_{M}(\xi)$ is the Legendre polynomial of degree of $M$ and $L_{M}^{\prime}(\xi)$ is its derivative, and $\xi_{m}$ is chosen as the roots of $\left(1-\xi_{m}^{2}\right) L_{M}^{\prime}\left(\xi_{m}\right)=0 . \phi_{p}^{(M)}(\eta)$ is similar to $\phi_{m}^{(M)}(\xi)$, but for a different coordinate variable.

Within each element, the transverse and longitudinal field components can be expressed as

$$
\mathbf{E}_{t}=\sum_{i=1}^{n_{t}} \mathbf{N}_{t i}^{e} e_{t i}^{e}=\left\{\mathbf{N}_{t}^{e}\right\}^{T}\left\{e_{t}^{e}\right\}
$$

$$
\mathbf{E}_{z}=\sum_{i=1}^{n_{z}} N_{z i}^{e} e_{z i}^{e}=\left\{N_{z}^{e}\right\}^{T}\left\{e_{z}^{e}\right\}
$$

where $n_{t}$ and $n_{z}$ denote the degree of freedom of the vector spectral element and scalar spectral element, respectively. Since the spectral elements are constructed in the reference domain, not in the physical domain, co-variant and contra-variant transformations should be employed to the discretized fields and their derivatives. Details are referred to [20] and not elaborated here.

## IV. SEMIDISCRETIZED SYSTEM AND STIFFNESS MATRIX IN THE LAGRANGIAN SYSTEM

Discretizing the cross section of the substructure by the aforementioned spectral elements, we will obtain a semidiscretized functional as

$$
\begin{aligned}
\Pi=\frac{1}{2} \int_{z_{a}}^{z_{b}}[ & \left\{e_{t}\right\}^{T} \mathbf{M}_{1}\left\{e_{t}\right\}+\left\{e_{z}\right\}^{T} \mathbf{M}_{2}\left\{e_{z}\right\} \\
& \left.+\left\{\dot{e}_{t}\right\}^{T} \mathbf{M}_{3}\left\{\dot{e}_{t}\right\}-2\left\{\dot{e}_{t}\right\}^{T} \mathbf{M}_{4}\left\{e_{z}\right\}\right] d z
\end{aligned}
$$

where

$$
\begin{aligned}
\mathbf{M}_{1}=\sum_{e=1}^{M} \iint_{\Omega^{e}} & {\left[\frac{1}{\mu_{r}^{e}}\left\{\nabla_{t} \times \mathbf{N}_{t}^{e}\right\} \cdot\left\{\nabla_{t} \times \mathbf{N}_{t}^{e}\right\}^{T}\right.} \\
& \left.-k_{0}^{2} \epsilon_{r}^{e}\left\{\mathbf{N}_{t}^{e}\right\} \cdot\left\{\mathbf{N}_{t}^{e}\right\}^{T}\right] d \Omega
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{M}_{2}=\sum_{e=1}^{M} \iint_{\Omega^{e}} & {\left[\frac{1}{\mu_{r}^{e}}\left\{\nabla_{t} N_{z}^{e}\right\} \cdot\left\{\nabla_{t} N_{z}^{e}\right\}^{T}\right.} \\
& \left.-k_{0}^{2} \epsilon_{r}^{e}\left\{N_{z}^{e}\right\} \cdot\left\{N_{z}^{e}\right\}^{T}\right] d \Omega
\end{aligned}
$$

$$
\mathbf{M}_{3}=\sum_{e=1}^{M} \iint_{\Omega^{e}}\left[\frac{1}{\mu_{r}^{e}}\left\{\mathbf{N}_{t}^{e}\right\} \cdot\left\{\mathbf{N}_{t}^{e}\right\}^{T}\right] d \Omega
$$

$$
\mathbf{M}_{4}=\sum_{e=1}^{M} \iint_{\Omega^{e}}\left[\frac{1}{\mu_{r}^{e}}\left\{\mathbf{N}_{t}^{e}\right\} \cdot\left\{\nabla_{t} N_{z}^{e}\right\}^{T}\right] d \Omega .
$$

Applying the circumferential boundary conditions and taking the variation for longitudinal fields, we can obtain an expression of $\left\{e_{z}\right\}$ as

$$
\left\{e_{z}\right\}=\mathbf{M}_{2}^{-1} \mathbf{M}_{4}^{T}\left\{\dot{e}_{t}\right\} .
$$

By inserting the above expression into (15) and eliminating the longitudinal components $\left\{e_{z}\right\}$, the original semidiscretized functional can be cast into the Lagrangian system

$$
\Pi(\mathbf{q}, \dot{\mathbf{q}})=\frac{1}{2} \int_{z_{a}}^{z_{b}} L(\mathbf{q}, \dot{\mathbf{q}}) d z
$$

where $\mathbf{q} \triangleq \{e_t\}$ is the vector of the discretized transverse field, and it is renamed here as the generalized displacement following the classic mechanic terms. $L(\mathbf{q}, \dot{\mathbf{q}})$ is the Lagrangian function

$$
L(\mathbf{q}, \dot{\mathbf{q}})=\mathbf{q}^{T} \mathbf{K}_{11} \mathbf{q}+\dot{\mathbf{q}}^{T} \mathbf{K}_{22} \dot{\mathbf{q}} \tag{22}
$$

where

$$
\mathbf{K}_{11}=\mathbf{M}_{1} \tag{23}
$$

and

$$
\mathbf{K}_{22}=\mathbf{M}_{3}-\mathbf{M}_{4} \mathbf{M}_{2}^{-1} \mathbf{M}_{4}^{T}. \tag{24}
$$

Since the circumferential boundary conditions are already imposed onto (21), based on the uniqueness theorem [21], all the field values within the substructure are determined if the tangential (viz. the transverse) components on the left and right end are specified

$$
\mathbf{q}_{a}=\left.\mathbf{q}\right|_{z=z_{a}} \quad \mathbf{q}_{b}=\left.\mathbf{q}\right|_{z=z_{b}}. \tag{25}
$$

Based on the above conclusion, we know that if the longitudinal integration is carried out for (21), the resultant discretized functional should be a quadratic function of $\mathbf{q}_{a}$ and $\mathbf{q}_{b}$, i.e.,

$$
\Pi\left(\mathbf{q}_{a}, \mathbf{q}_{b}\right)=\frac{1}{2} \mathbf{q}_{a}^{T} \mathbf{K}_{a a} \mathbf{q}_{a}+\mathbf{q}_{b}^{T} \mathbf{K}_{b a} \mathbf{q}_{a}+\frac{1}{2} \mathbf{q}_{b}^{T} \mathbf{K}_{b b} \mathbf{q}_{b} \tag{26}
$$

where the matrices $\mathbf{K}_{a a}$, $\mathbf{K}_{b a}$, and $\mathbf{K}_{b b}$ are the results of performing longitudinal integration for $\mathbf{K}_{11}$ and $\mathbf{K}_{22}$ in the Lagrangian function. After we calculate the values of these three matrices, the global stiffness matrix of this substructure is immediately available

$$
\mathbf{K}=\left[\begin{array}{ll}
\mathbf{K}_{a a} & \mathbf{K}_{b a}^{T} \\
\mathbf{K}_{b a} & \mathbf{K}_{b b}
\end{array}\right]. \tag{27}
$$

Once the stiffness matrices in $\mathbf{K}$ are obtained, we can assemble the stiffness matrices of all substructures together into a global system matrix. Solving a system of equations with this global matrix, we will obtain the numerical results for the whole layered structure.

## V. HAMILTONIAN SYSTEM AND RICCATI EQUATIONS

Theoretically, the matrices $\mathbf{K}_{a a}$, $\mathbf{K}_{b a}$, and $\mathbf{K}_{b b}$ can be obtained by integrating the Lagrangian function. However, the accuracy cannot be guaranteed if we directly employ numerical integration methods to (21). To calculate the values of the stiffness matrix with high accuracy and construct the so-called semianalytical SEM, we will use a Riccati equation-based HPI method [15], which is performed in the Hamiltonian system.

We first introduce a generalized force by Legendre transformation

$$
\mathbf{p}=\frac{\partial L}{\partial \dot{\mathbf{q}}}=\mathbf{K}_{22} \dot{\mathbf{q}} \tag{28}
$$

and we will obtain the Hamiltonian function as

$$
H(\mathbf{q}, \mathbf{p})=\mathbf{p}^{T} \dot{\mathbf{q}}-L(\mathbf{q}, \dot{\mathbf{q}})=-\frac{1}{2} \mathbf{q}^{T} \mathbf{B} \mathbf{q}+\frac{1}{2} \mathbf{p}^{T} \mathbf{D} \mathbf{p} \tag{29}
$$

where

$$
\mathbf{B}=\mathbf{K}_{11} \quad \mathbf{D}=\mathbf{K}_{22}^{-1}. \tag{30}
$$

The Legendre transformation can also be applied to the discretized functional $\Pi(\mathbf{q}_{a}, \mathbf{q}_{b})$ to generate a new functional based on variables $\mathbf{q}_{a}$ and $\mathbf{p}_{b}$

$$
\Gamma\left(\mathbf{q}_{a}, \mathbf{p}_{b}\right)=\mathbf{p}_{b}^{T} \mathbf{q}_{b}-\Pi\left(\mathbf{q}_{a}, \mathbf{q}_{b}\right). \tag{31}
$$

By taking variation of the above functional, we will have

$$
\delta \Gamma\left(\mathbf{q}_{a}, \mathbf{p}_{b}\right)=\mathbf{q}_{b}^{T} \delta \mathbf{p}_{b}+\mathbf{p}_{a}^{T} \delta \mathbf{q}_{a} \tag{32}
$$

and

$$
\mathbf{q}_{b}=\frac{\partial \Gamma}{\partial \mathbf{p}_{b}} \quad \mathbf{p}_{a}=\frac{\partial \Gamma}{\partial \mathbf{q}_{a}}. \tag{33}
$$

From (31)-(33), we know the new functional $\Gamma(\mathbf{q}_{a}, \mathbf{p}_{b})$ should be a quadratic function of $\mathbf{q}_{a}$ and $\mathbf{p}_{b}$, i.e.,

$$
\Gamma\left(\mathbf{q}_{a}, \mathbf{p}_{b}\right)=\frac{1}{2} \mathbf{q}_{a}^{T} \mathbf{Q} \mathbf{q}_{a}+\mathbf{q}_{b}^{T} \mathbf{F} \mathbf{q}_{a}+\frac{1}{2} \mathbf{p}_{b}^{T} \mathbf{G} \mathbf{p}_{b}. \tag{34}
$$

Based on (26), (31), (33), and (34), a set of mutual transformation relationships can be found between matrices $\mathbf{K}_{a a}$, $\mathbf{K}_{b a}$, $\mathbf{K}_{b b}$, and matrices $\mathbf{Q}$, $\mathbf{F}$, $\mathbf{G}$

$$
\mathbf{K}_{a a}=-\mathbf{Q}+\mathbf{F}^{T} \mathbf{G}^{-1} \mathbf{F} \quad \mathbf{K}_{b a}=-\mathbf{G}^{-1} \mathbf{F} \quad \mathbf{K}_{b b}=\mathbf{G}^{-1}
\tag{35}
$$

$$
\mathbf{Q}=\mathbf{K}_{b a}^{T} \mathbf{K}_{b b}^{-1} \mathbf{K}_{b a} \quad \mathbf{F}=-\mathbf{K}_{b b}^{-1} \mathbf{K}_{b a} \quad \mathbf{G}=\mathbf{K}_{b b}^{-1}. \tag{36}
$$

Equation (35) shows that instead of directly integrating (21) to obtain the stiffness matrix, we can first calculate matrices $\mathbf{Q}$, $\mathbf{F}$, and $\mathbf{G}$, and then transform them to $\mathbf{K}_{a a}$, $\mathbf{K}_{b a}$, and $\mathbf{K}_{b b}$.

For a substructure whose distributions of geometry and material are homogeneous along the $z$ direction, the matrices $\mathbf{Q}$, $\mathbf{F}$, and $\mathbf{G}$ are determined by matrices $\mathbf{B}$ and $\mathbf{D}$ in the Hamiltonian function, and the length of the substructure

$$
\eta=z_{b}-z_{a}. \tag{37}
$$

It has been proven that the above matrix functions satisfy the Riccati equations [15]

$$
\left\{\begin{aligned}
d \mathbf{F} / d \eta &=-\mathbf{G B F}=\mathbf{F D Q} \\
d \mathbf{G} / d \eta &=\mathbf{D}-\mathbf{G B G}=\mathbf{F D F}^{T} \\
d \mathbf{Q} / d \eta &=-\mathbf{F B F}=\mathbf{Q D Q}-\mathbf{B}
\end{aligned}\right. \tag{38}
$$

with initial conditions

$$
\mathbf{Q}(\eta=0)=\mathbf{0} \quad \mathbf{G}(\eta=0)=\mathbf{0} \quad \mathbf{F}(\eta=0)=\mathbf{I} \tag{39}
$$

where $\mathbf{0}$ and $\mathbf{I}$ denote the zero matrix and identity matrix with the same size as matrices $\mathbf{Q}$, $\mathbf{F}$, and $\mathbf{G}$, respectively.

The above Riccati equations seem very complex at first glance, however, they can be solved by an algorithm called HPI [15] with numerical errors as small as the rounding error on a computer. After $\mathbf{Q}$, $\mathbf{F}$, and $\mathbf{G}$ are obtained, the stiffness matrix of the substructure can be calculated based on (35) and it can

be further combined with stiffness matrices of the neighbor substructure to assemble the global system matrix.

## VI. HPI METHOD

The first step of using HPI to solve the Riccati equations (38) is to divide the integration interval based on the $2N$ algorithm [22]

$$
\tau=\frac{\eta}{2^{N}} \tag{40}
$$

where $N$ is a positive integer number. For example, $N=20$ suggested in [15] can achieve machine precision for most cases. $N=20$ means $\tau=\eta / 1048576$, i.e., even for a substructure as long as 100 wavelengths, a slice with value $\tau$ will be shorter than $1 / 10000$ of a wavelength. It is suitable and accurate to perform a Taylor expansion for matrices $\mathbf{F}, \mathbf{G}$, and $\mathbf{Q}$ within the small interval $\tau$

$$
\begin{cases}
\mathbf{F}(\tau)=\mathbf{I}+\mathbf{F}^{\prime}(\tau) \\
\mathbf{F}^{\prime}(\tau)=\boldsymbol{\phi}_{1} \tau+\boldsymbol{\phi}_{2} \tau^{2}+\boldsymbol{\phi}_{3} \tau^{3}+\boldsymbol{\phi}_{4} \tau^{4}+O\left(\tau^{5}\right) \\
\mathbf{G}(\tau)=\boldsymbol{\gamma}_{1} \tau+\boldsymbol{\gamma}_{2} \tau^{2}+\boldsymbol{\gamma}_{3} \tau^{3}+\boldsymbol{\gamma}_{4} \tau^{4}+O\left(\tau^{5}\right) \\
\mathbf{Q}(\tau)=\boldsymbol{\theta}_{1} \tau+\boldsymbol{\theta}_{2} \tau^{2}+\boldsymbol{\theta}_{3} \tau^{3}+\boldsymbol{\theta}_{4} \tau^{4}+O\left(\tau^{5}\right)
\end{cases} \tag{41}
$$

where matrices $\boldsymbol{\phi}, \boldsymbol{\gamma}$, and $\boldsymbol{\theta}$ have the same dimensions as $\mathbf{F}, \mathbf{G}$, and $\mathbf{Q}$. Since $\tau$ is a very small number, the higher order items $O\left(\tau^{5}\right)$ by Taylor expansion are usually smaller than or comparable to the minimum quantity defined by the double precision when compared with $\mathbf{F}(\tau), \mathbf{G}(\tau)$, and $\mathbf{Q}(\tau)$. Omitting these higher order items will not lead to the loss of any significant digits. Comparing (41) with (38), we can obtain expressions of matrices $\boldsymbol{\phi}, \boldsymbol{\gamma}$, and $\boldsymbol{\theta}$ over the interval $\tau$

$$
\begin{cases}
\boldsymbol{\gamma}_{1}=\mathbf{D} \\
\boldsymbol{\gamma}_{2}=\mathbf{0} \\
\boldsymbol{\gamma}_{3}=-\boldsymbol{\gamma}_{1} \mathbf{B} \boldsymbol{\gamma}_{1} / 3 \\
\boldsymbol{\gamma}_{4}=\left(-\boldsymbol{\gamma}_{2} \mathbf{B} \boldsymbol{\gamma}_{1}-\boldsymbol{\gamma}_{1} \mathbf{B} \boldsymbol{\gamma}_{2}\right) / 4
\end{cases} \tag{42}
$$

$$
\begin{cases}
\boldsymbol{\phi}_{1}=\mathbf{0} \\
\boldsymbol{\phi}_{2}=-\boldsymbol{\gamma}_{1} \mathbf{B} / 3 \\
\boldsymbol{\phi}_{3}=\left(-\boldsymbol{\gamma}_{2} \mathbf{B}-\boldsymbol{\gamma}_{1} \mathbf{B} \boldsymbol{\phi}_{1}\right) / 3 \\
\boldsymbol{\phi}_{4}=\left(-\boldsymbol{\gamma}_{3} \mathbf{B}-\boldsymbol{\gamma}_{2} \mathbf{B} \boldsymbol{\phi}_{1}-\boldsymbol{\gamma}_{1} \mathbf{B} \boldsymbol{\phi}_{2}\right) / 4
\end{cases} \tag{43}
$$

$$
\begin{cases}
\boldsymbol{\theta}_{1}=-\mathbf{B} \\
\boldsymbol{\theta}_{2}=\left(-\boldsymbol{\phi}_{1}^{T} \mathbf{B}-\mathbf{B} \boldsymbol{\phi}_{1}\right) / 2 \\
\boldsymbol{\theta}_{3}=\left(-\boldsymbol{\phi}_{2}^{T} \mathbf{B}-\mathbf{B} \boldsymbol{\phi}_{2}-\boldsymbol{\phi}_{1}^{T} \mathbf{B} \boldsymbol{\phi}_{1}\right) / 3 \\
\boldsymbol{\theta}_{4}=\left(-\boldsymbol{\phi}_{3}^{T} \mathbf{B}-\mathbf{B} \boldsymbol{\phi}_{3}-\boldsymbol{\phi}_{2}^{T} \mathbf{B} \boldsymbol{\phi}_{1}-\boldsymbol{\phi}_{1}^{T} \mathbf{B} \boldsymbol{\phi}_{2}\right) / 4.
\end{cases} \tag{44}
$$

After the calculation over interval $\tau$, $\mathbf{F}(2\tau)$, $\mathbf{G}(2\tau)$, and $\mathbf{Q}(2\tau)$ can be obtained by combining two small $\tau$ together as

$$
\begin{cases}
\mathbf{G}(2 \tau)=\mathbf{G}(\tau)+\mathbf{F}(\tau)\left[\mathbf{G}(\tau)^{-1}+\mathbf{Q}(\tau)\right]^{-1} \mathbf{F}(\tau)^{T} \\
\mathbf{F}^{\prime}(2 \tau)=\mathbf{F}^{\prime}(\tau)\left[\mathbf{I}+\mathbf{G}(\tau) \mathbf{Q}(\tau)\right]^{-1} \mathbf{F}^{\prime}(\tau) \\
\quad+\left[\left(\mathbf{F}^{\prime}(\tau)-\mathbf{G}(\tau) \mathbf{Q}(\tau) / 2\right]\left[\mathbf{I}+\mathbf{G}(\tau) \mathbf{Q}(\tau)\right]^{-1}\right. \\
\quad+\left[\mathbf{I}+\mathbf{G}(\tau) \mathbf{Q}(\tau)\right]^{-1}\left[\mathbf{F}^{\prime}(\tau)-\mathbf{G}(\tau) \mathbf{Q}(\tau) / 2\right] \\
\mathbf{Q}(2 \tau)=\mathbf{Q}(\tau)+\mathbf{F}(\tau)^{T}\left[\mathbf{Q}(\tau)^{-1}+\mathbf{G}(\tau)\right]^{-1} \mathbf{F}(\tau).
\end{cases} \tag{45}
$$

It is worth noting that during the combination only the increment of $\mathbf{F}(\tau)$, i.e., $\mathbf{F}^{\prime}(\tau)=\mathbf{F}(\tau)-\mathbf{I}$, is calculated. That is because this small quantity must be kept away from $\mathbf{I}$ during computation, otherwise all the significant digits of $\mathbf{F}^{\prime}(\tau)$ will be lost due to the addition of a small quantity $\mathbf{F}^{\prime}(\tau)$ to a much larger quantity $\mathbf{I}$.

After repeating (45) for $N$ times, the integration interval will be equal to $\eta$ and we can obtain the matrices $\mathbf{G}(\eta), \mathbf{Q}(\eta)$, and $\mathbf{F}(\tau)=\mathbf{F}^{\prime}(\tau)+\mathbf{I}$ with very high accuracy.

## VII. BLOCK THOMAS ALGORITHM FOR BLOCK TRI-DIAGONAL MATRIX

After assembling all the stiffness matrices, applying boundary conditions onto the first and last interfaces of the whole structure, and imposing the excitations, the equations to be solved will take a form of a block tri-diagonal system

$$
\left[\begin{array}{ccccc}
\mathbf{B}_{1} & \mathbf{C}_{1} & \mathbf{0} & \ldots & \mathbf{0} \\
\mathbf{A}_{2} & \mathbf{B}_{2} & \mathbf{C}_{2} & \ddots & \vdots \\
\mathbf{0} & \mathbf{A}_{3} & \mathbf{B}_{3} & \ddots & \mathbf{0} \\
\vdots & \ddots & \ddots & \ddots & \mathbf{C}_{N-1} \\
\mathbf{0} & \ldots & \mathbf{0} & \mathbf{A}_{N} & \mathbf{B}_{N}
\end{array}\right]\left[\begin{array}{c}
\mathbf{q}_{1} \\
\mathbf{q}_{2} \\
\vdots \\
\vdots \\
\mathbf{q}_{N}
\end{array}\right]=\left[\begin{array}{c}
\mathbf{f}_{1} \\
\mathbf{f}_{2} \\
\vdots \\
\vdots \\
\mathbf{f}_{N}
\end{array}\right] \tag{46}
$$

where $\mathbf{A}_{i}=\mathbf{K}_{b a}^{(i-1)}, \mathbf{B}_{i}=\mathbf{K}_{a a}+\mathbf{K}_{b b}^{(i)}$, and $\mathbf{C}_{i}=\mathbf{K}_{b a}^{(i) T}$, $\mathbf{q}_{i}$ and $\mathbf{f}_{i}$ are the discretized generalized displacement and discretized excitation corresponding to the $i$ th interface, respectively.

The block Thomas algorithm can be used here to accelerate the process of solving (46). The block Thomas algorithm is a generalized version of Thomas algorithm [18], which is designed for a tri-diagonal matrix.

The pseudocode of the block Thomas algorithm is as follows:

$$
\begin{cases}
\mathbf{C}_{1}^{\prime}=\mathbf{B}_{1}^{-1} \mathbf{C}_{1} \\
\mathbf{f}_{1}^{\prime}=\mathbf{B}_{1}^{-1} \mathbf{f}_{1} \\
\text { for } i=2: N \\
\quad \mathbf{C}_{i}^{\prime}=\left(\mathbf{B}_{i}-\mathbf{A}_{i} \mathbf{C}_{i-1}^{\prime}\right)^{-1} \mathbf{C}_{i}, \\
\quad \mathbf{f}_{i}^{\prime}=\left(\mathbf{B}_{i}-\mathbf{A}_{i} \mathbf{C}_{i-1}^{\prime}\right)^{-1}\left(\mathbf{f}_{i}-\mathbf{A}_{i} \mathbf{f}_{i-1}^{\prime}\right) \\
\text { end } \\
\mathbf{q}_{N}=\mathbf{f}_{N}^{\prime} \\
\text { for } i=N-1:-1: 2 \\
\quad \mathbf{q}_{i}=\mathbf{f}_{i}^{\prime}-\mathbf{C}_{i}^{\prime} \mathbf{q}_{i+1} \\
\text { end }
\end{cases} \tag{47}
$$

More details, as well as a discussion of efficiency of the block Thomas algorithm can be referred to [18].

## VIII. NUMERICAL EXAMPLES AND DISCUSSIONS

The first example is shown in Fig. 4, where a uniform plane wave is impinging onto a PEC-backed stratified dielectric slab with incident angle $\theta=\pi / 4$. Along the $x$ direction, the stratified dielectric slab has thickness $L=1 \mathrm{~cm}$, and it is evenly divided into ten layers of dielectric with the distribution of permittivity shown in Fig. 5. We simulate this electromagnetic problem by both the conventional FEM and the proposed semianalytical SEM with the same discretization scheme (ten elements per layer along the $x$ direction), and then extract the reflection coefficient from the simulated electromagnetic fields. Since this is a 1-D problem and does not require discretization of the cross section, the comparison between the conventional FEM and the semianalytical SEM is essentially a comparison between the FEM and HPI for the longitudinal integration in (21).

Fig. 6 shows the reflection coefficients under different working frequencies by the two numerical methods, as well as

![](./images/811701226881155074_4.jpg)

Fig. 4. Uniform plane wave is impinging onto a PEC-backed stratified dielectric slab, which consists of ten layers with different values of permittivity given by Fig. 5.

![](./images/811701226881155074_5.jpg)

Fig. 5. Distribution of relative permittivity of the stratified dielectric slab. (a) Real part of $\epsilon_r$. (b) Imaginary part of $\epsilon_r$ of the layered medium in Fig. 4.

![](./images/811701226881155074_6.jpg)

Fig. 6. Reflection coefficients under different working frequencies obtained by the conventional FEM, semianalytical SEM, and analytical method.

![](./images/811701226881155074_7.jpg)

Fig. 7. Relative errors of reflection coefficients under different working frequencies obtained by the conventional FEM and semianalytical SEM.

![](./images/811701226881155074_8.jpg)

Fig. 8. Microwave filter containing ten identical cells. The unit of length in this figure is centimeters (cm).

![](./images/811701226881155074_9.jpg)

Fig. 9. (a) Conventional FEM mesh and (b) semianalytical SEM mesh for one cell of the microwave filter. Meshes of the other nine cells are the same as the shown one for both cases.

the analytical method [23]. The relative errors under different frequencies by the conventional FEM and semianalytical SEM are shown in Fig. 7. From the two figures, we can observe that the accuracy of the semianalytical SEM is several orders higher than that of the conventional FEM. Furthermore, with the increase of working frequency, i.e., the decrease of discretization density for a fixed mesh, the numerical error by the conventional FEM becomes larger and larger, while the error by semianalytical SEM is always around or below $10^{-14}$, which is on the same level of computer's round-off error defined by double precision. In other words, the longitudinal integration by HPI can achieve machine precision.

The second example is a microwave filter with ten identical cells. Each cell is a waveguide discontinuity structure with the geometry and dimensions shown in Fig. 8. A conventional FEM, as well as semianalytical SEM are employed to calculate the reflection and transmission coefficients corresponding to an incident $\text{TE}_{10}$ wave with various values of working frequencies. As shown in Fig. 9, a relatively dense conventional FEM mesh is used to discretize the microwave filter (61 440 first-order 3-D edge element in total); while for the semianalytical SEM, each cell is divided into three substructures with only six 2-D spectral elements on the cross section. In other words, only 180 semianalytical spectral elements are used to discretize the whole structure of the microwave filter.

Fig. 10 shows the numerical results of reflection and transmission coefficients by the conventional FEM and semianalytical SEM (third-order 2-D SEM for discretization of cross section in this case), it also shows reference results, which are obtained by the conventional FEM with a much denser mesh and higher order of basis functions than that shown in Fig. 9. From this figure, we observe that the microwave filter presents bandgaps

![](./images/811701226881155074_10.jpg)

Fig. 10. (a) Reflection and (b) transmission coefficients of the microwave filter by conventional FEM and semianalytical SEM.

<table>
<caption>TABLE I Comparison of Efficiency and Accuracy Between the Conventional FEM and the Semianalytical SEM</caption>
  <thead>
    <tr>
      <th></th>
      <th>conventional FEM</th>
      <th>semi-analytical SEM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>number of element</td>
      <td>61440</td>
      <td>180</td>
    </tr>
    <tr>
      <td>number of unknowns</td>
      <td>208120</td>
      <td>2046</td>
    </tr>
    <tr>
      <td>memory (MB)</td>
      <td>123</td>
      <td>9</td>
    </tr>
    <tr>
      <td>CPU time (minute)</td>
      <td>708.4</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>relative error of $|S_{11}|$</td>
      <td>$6.2 \times 10^{-2}$</td>
      <td>$3.9 \times 10^{-3}$</td>
    </tr>
    <tr>
      <td>relative error of $|S_{12}|$</td>
      <td>$7.7 \times 10^{-2}$</td>
      <td>$3.0 \times 10^{-3}$</td>
    </tr>
  </tbody>
</table>

due to the periodicity along the direction of wave propagation. We also can find that even with a much smaller number of element, the semianalytical SEM can give results closer to reference than results by a conventional FEM. More detailed comparison of efficiency, as well as accuracy between two numerical methods are shown in Table I. From this table, we can find that the semianalytical SEM is more efficient and more accurate than the conventional FEM.

The accuracy of the semianalytical SEM can be increased by either refining the SEM mesh on the cross section, i.e., $h$-refinement, or increasing the order of the SEM basis function, i.e., $p$-refinement. We use the same discretization scheme as Fig. 9(b), but with different orders of basis functions for spectral elements on the cross section, to re-solve the microwave filter problem. The relative errors of calculated reflection and transmission coefficients by the semianalytical SEM with different interpolation orders are shown in Fig. 11 and Table II,

![](./images/811701226881155074_11.jpg)

Fig. 11. Relative errors of reflection and transmission coefficients of the microwave filter by the semianalytical SEM with different interpolation orders for transverse discretization.

<table>
<caption>TABLE II Semianalytical SEM With Different Interpolation Orders for Transverse Discretization</caption>
  <thead>
    <tr>
      <th>SEM order</th>
      <th>number of unknowns</th>
      <th>CPU time (minute)</th>
      <th>relative error of $|S_{11}|$</th>
      <th>relative error of $|S_{12}|$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3rd</td>
      <td>2046</td>
      <td>2.0</td>
      <td>$3.9 \times 10^{-3}$</td>
      <td>$3.0 \times 10^{-3}$</td>
    </tr>
    <tr>
      <td>4th</td>
      <td>3784</td>
      <td>9.0</td>
      <td>$1.6 \times 10^{-3}$</td>
      <td>$3.3 \times 10^{-3}$</td>
    </tr>
    <tr>
      <td>5th</td>
      <td>6050</td>
      <td>28.0</td>
      <td>$9.3 \times 10^{-4}$</td>
      <td>$7.4 \times 10^{-4}$</td>
    </tr>
    <tr>
      <td>6th</td>
      <td>8844</td>
      <td>72.1</td>
      <td>$4.6 \times 10^{-4}$</td>
      <td>$3.6 \times 10^{-4}$</td>
    </tr>
    <tr>
      <td>7th</td>
      <td>12166</td>
      <td>178.1</td>
      <td>$2.8 \times 10^{-4}$</td>
      <td>$2.2 \times 10^{-4}$</td>
    </tr>
    <tr>
      <td>8th</td>
      <td>16016</td>
      <td>321.6</td>
      <td>$1.3 \times 10^{-4}$</td>
      <td>$1.0 \times 10^{-4}$</td>
    </tr>
  </tbody>
</table>

from which we can conclude that the numerical errors by the proposed method decrease exponentially as the increase of interpolation orders of spectral elements on the cross section, i.e., the semianalytical SEM, can achieve spectral accuracy.

## IX. CONCLUSION

In this paper, we have discussed a semianalytical SEM specially designed for layered structures. A 3-D piecewise homogeneous structure is decomposed into several substructures based on the distributions of material and geometry along the longitudinal direction. Each substructure is then modeled by a combination of 2-D spectral elements for discretization of the cross section and a high precision algorithm for the integration along the longitudinal direction. Compared to other efficient algorithms such as NMM and LAFE, the semianalytical SEM only requires a set of 2-D meshes, and meanwhile does not need the expensive step of solving eigenproblems corresponding to the semidiscretized substructures. Numerical examples demonstrate that the semianalytical SEM is very efficient and accurate, and it can achieve spectral accuracy with the increase of interpolation order of 2-D spectral elements for the discretization of cross sections of substructures.

## REFERENCES

[1] J. R. Wait, *Electromagnetic Waves In Stratified Media*. New York: Oxford Univ. Press, 1970.

[2] S. G. Johnson and J. D. Joannopoulos, "Three-dimensionally periodic dielectric layered structure with omnidirectional photonic band gap," *Appl. Phys. Lett.*, vol. 77, no. 22, pp. 3490-3492, Nov. 2000.

[3] P. Meuris, W. Schoenmaker, and W. Magnus, "Strategy for electromagnetic interconnect modeling," *IEEE Trans. Comput.-Aided Design Integr. Circuits Syst.*, vol. 20, no. 6, pp. 753-762, Jun. 2001.

[4] Q. H. Liu and W. C. Chew, “Numerical mode-matching method for the multiregion vertically stratified media,” *IEEE Trans. Antennas Propag.*, vol. 38, no. 4, pp. 498–506, Apr. 1990.

[5] H. Derudder, F. Olyslager, D. De Zutter, and S. Van den Berghe, “Ef- ficient mode-matching analysis of discontinuities in finite planar sub- strates using perfectly matched layers,” *IEEE Trans. Antennas Propag.*, vol. 49, no. 2, pp. 185–195, Feb. 2001.

[6] Q. H. Liu and W. C. Chew, “Analysis of discontinuities in planar di- electric waveguides: An eigenmode propagation method,” *IEEE Trans. Microw. Theory Tech.*, vol. 39, no. 3, pp. 422–430, Mar. 1991.

[7] Q. H. Liu, “Electromagnetic field generated by an off axis source in a cylindrically layered medium with an arbitrary number of horizontal discontinuities,” *Geophysics*, vol. 58, no. 5, pp. 616–625, 1993.

[8] G. X. Fan, Q. H. Liu, and S. P. Blanchard, “3-D numerical mode-matching (NMM) method for resistivity well-logging tools,” *IEEE Trans. Antennas Propag.*, vol. 48, no. 10, pp. 1544–1552, Oct. 2000.

[9] D. Jiao, S. Chakravarty, and C. H. Dai, “A layered finite element method for electromagnetic analysis of large-scale high-frequency integrated circuits,” *IEEE Trans. Antennas Propag.*, vol. 55, no. 2, pp. 422–432, Feb. 2007.

[10] H. Gan and D. Jiao, “A time-domain layered finite element reduction recovery (LAFE-RR) method for high-frequency VLSI design,” *IEEE Trans. Antennas Propag.*, vol. 55, no. 12, pp. 3620–3629, Dec. 2007.

[11] H. Gan and D. Jiao, “A recovery algorithm of linear complexity in the time-domain layered finite element reduction recovery (LAFE-RR) method for large-scale electromagnetic analysis of high-speed ICs,” *IEEE Trans. Adv. Packag.*, vol. 31, no. 3, pp. 612–618, Aug. 2008.

[12] A. Kirsch and P. Monk, “A finite element/spectral method for approx- imating the time-harmonic Maxwell system in R3,” *SIAM J. Appl. Math.*, vol. 55, no. 5, pp. 1324–1344, Oct. 1995.

[13] G. Cohen, *Higher-Order Numerical Methods for Transient Wave Equa- tions*. Berlin, Germany: Springer, 2002.

[14] J. H. Lee, T. Xiao, and Q. H. Liu, “A 3-D spectral-element method using mixed-order curl conforming vector basis functions for electro- magnetic fields,” *IEEE Trans. Microw. Theory Tech.*, vol. 54, no. 1, pp. 437–444, Jan. 2006.

[15] W. X. Zhong, *Duality System in Applied Mechanics and Optimal Con- trol*. Norwell, MA: Kluwer, 2004.

[16] W. X. Zhong, “On precise integration method,” *J. Comput. Appl. Math.*, vol. 163, no. 204, pp. 59–78, Feb. 2004.

[17] J. Chen, B. Zhu, and W. X. Zhong, “On the semi-analytical dual edge element and its application to waveguide discontinuities,” *Acta Phys. Sin.*, vol. 58, no. 2, pp. 1091–1099, Feb. 2009.

[18] G. Meurant, “A review on the inverse of symmetric tridiagonal and block tridiagonal matrices,” *SIAM J. Matrix Anal. Appl.*, vol. 13, no. 3, pp. 707–728, Jul. 1992.

[19] D. Gottlieb and J. S. Hesthaven, “Spectral methods for hyperbolic prob- lems,” *J. Comput. Appl. Math.*, vol. 128, no. 1–2, pp. 83–131, Mar. 2001.

[20] C. W. Crowley, P. P. Silvester, and H. Hurwitz, Jr., “Covariant projec- tion elements for 3-D vector field problems,” *IEEE Trans. Magn.*, vol. 24, no. 1, pp. 397–400, Jan. 1988.

[21] C. A. Balanis, *Advanced Engineering Electromagnetics*. New York: Wiley, 1989.

[22] E. Angel and R. Bellman, *Dynamic Programming and Partial Differ- ential Equations*. New York: Academic, 1972.

[23] W. C. Chew, *Waves And Fields in Inhomogeneous Media*. New York: Wiley, 1999.

![](./images/811701226881155074_12.jpg)

Jiefu Chen received the B.S. degree in engineering mechanics and M.S. degree in dynamics and control from the Dalian University of Technology, Dalian, China, in 2003 and 2006, respectively, and is cur- rently working toward the Ph.D. degree in electrical engineering at Duke University, Durham, NC.

Since 2007, he has been a Research Assistant with the Department of Electrical and Computer Engi- neering at Duke University. His research interest is fast algorithms for computational electromagnetics and their applications in electronic packaging, electromagnetic compatibility, and signal integrity.

![](./images/811701226881155074_13.jpg)

Bao Zhu received the B.S. degree in engineering me- chanics from the Dalian University of Technology, Dalian, China, in 2005, and is currently working to- ward the Ph.D. degree in engineering mechanics at the Dalian University of Technology.

From September 2008 to September 2009, he was a visiting student with the Department of Elec- trical and Computer Engineering, Duke University, Durham, NC. His research interest is time-domain algorithms for computational mechanics and com- putational electromagnetics.

![](./images/811701226881155074_14.jpg)

Wanxie Zhong received the B.S. degree in bridge en- gineering from Tongji University, Shanghai, China, in 1956.

From 1956 to 1962, he was with the Institute of Mechanics, Chinese Academy of Science, as a Research Scientist. Since 1962, he has been with the Dalian University of Technology, Dalian, China where he is currently a Professor of engineering mechanics. He has authored or coauthored over 300 papers in refereed journals and 14 books. His research interests include engineering mechanics, computational mechanics, and optimal control.

Prof. Zhong is a member of the Chinese Academy of Science.

![](./images/811701226881155074_15.jpg)

Qing Huo Liu (S'88-M'89-SM'94-F'05) received the Ph.D. degree in electrical engineering from the University of Illinois at Urbana-Champaign, in 1989.

From September 1986 to December 1988, he was with the Electromagnetics Laboratory, University of Illinois at Urbana-Champaign, as a Research Assistant, and from January 1989 to February 1990, he was a Postdoctoral Research Associate. From 1990 to 1995, he was a Research Scientist and Program Leader with Schlumberger-Doll Research, Ridgefield, CT. From 1996 to May 1999, he was an Associate Professor with New Mexico State University. Since June 1999, he has been with Duke University, Durham, NC, where he is currently a Professor of electrical and computer engineering. He has authored or coauthored over 450 papers in refereed journals and conference proceedings. He is currently Deputy Editor-in-Chief of *Electromagnetic Waves and Applications* and Deputy Editor-in-Chief of *Progress in Electromagnetics Research*. He is an Editor for *Journal of Computational Acoustics*. His research interests include computational electromagnetics and acoustics, inverse problems, geophysical subsurface sensing, biomedical imaging, electronic packaging, and the simula- tion of photonic devices and nanodevices.

Dr. Liu is a Fellow of the Acoustical Society of America. He is a member of Phi Kappa Phi and Tau Beta Pi. He is a full member of the U.S. National Committee, URSI Commissions B and F. He is an associate editor for the IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING. He was the recipient of the 1996 Presidential Early Career Award for Scientists and Engineers (PECASE) presented by the White House, the 1996 Early Career Research Award presented by the Environmental Protection Agency, and the 1997 CAREER Award presented by the National Science Foundation (NSF).