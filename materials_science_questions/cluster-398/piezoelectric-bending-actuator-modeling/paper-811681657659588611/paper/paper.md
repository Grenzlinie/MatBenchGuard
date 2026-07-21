An asymptotic approach for the analysis of piezoelectric fiber composite beams

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2011 Smart Mater. Struct. 20 025023

(http://iopscience.iop.org/0964-1726/20/2/025023)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 202.28.191.34
This content was downloaded on 02/03/2015 at 03:00

Please note that terms and conditions apply.

# An asymptotic approach for the analysis of piezoelectric fiber composite beams

J-S Kim $^{1,3}$, J R Hill $^{2}$ and K W Wang $^{2}$

$^{1}$ School of Mechanical Engineering, Kumoh National Institute of Technology, Gumi, Gyeongbuk 730-701, Korea
$^{2}$ Department of Mechanical Engineering, The University of Michigan, Ann Arbor, MI 48109, USA

E-mail: junsik.kim@kumoh.ac.kr

Received 15 July 2010, in final form 19 December 2010
Published 26 January 2011
Online at stacks.iop.org/SMS/20/025023

## Abstract
An asymptotic-expansion-method-based approach is developed to analyze piezoelectric fiber composite beams, by employing the virtual work principle. Starting from the three-dimensional linear piezoelectricity, a microscopic two-dimensional model and a macroscopic one-dimensional model are systematically derived by taking advantage of the slenderness of the beam. This enables us to derive a sophisticated yet efficient tool for the modeling and analysis of piezoelectric fiber-based composites, which can provide us with good physical insights on the behavior of slender adaptive structures in terms of actuation and sensing. The non-classical boundary conditions of the beam are obtained by applying the orthogonality of asymptotic displacements to the beam fundamental solutions. The accuracy and efficiency of the proposed approach are demonstrated by comparing its analytical/numerical predictions with the experimental results, three-dimensional finite element solutions, and one-dimensional beam solutions obtained by the classical rule of mixture.

(Some figures in this article are in colour only in the electronic version)

## 1. Introduction
Piezoelectric materials have been used extensively in various engineering systems as transducers that convert mechanical energy into electrical energy and vice versa. In many applications, piezoelectric fiber/polymer composites have been developed and found desirable [1, 2]. In order to optimally synthesize piezoelectric fiber composite transducers and structures, one can directly use the three-dimensional finite element analysis (3D FEA). It is however time-consuming and numerically expensive to model such piezoelectric fiber composites via the 3D FEA. Thus homogenization methods have been proposed to predict the effective three-dimensional homogenized material properties of piezoelectric fiber composites [3–5]. In this way, the computational efforts (including meshing and modeling) can be reduced, since such a composite material is now treated as a single-phase material.

The homogenization techniques can in general be classified into two groups; the unit cell model approach [3, 5], and the cross-sectional model approach [4, 6, 7]. It has been shown that some piezoelectric characteristics cannot be accurately predicted by the unit cell model [4]. We therefore focused on the cross-sectional model approach in this research. Utilizing such an approach, one normally uses asymptotic methods that are mathematically rigorous to predict the structure’s cross-sectional electromechanical properties as well as its overall behavior. When using the cross-sectional approach, however, it is very difficult to obtain higher order effects such as transverse shear deformations because it requires a proper set of boundary conditions (i.e. asymptotically correct boundary conditions, see [8, 9]), especially for the displacement prescribed boundaries. These higher order effects are important for applications involving beams that are weak in shear, such as sandwich beams or piezoelectric fiber composite beams, which is of specific interest in this study.

Recently, Cesnik and Palacios [6] and Roy *et al* [7] have applied the variational-asymptotic method (VAM) [10] to analyze a coupled electro/thermo/elastic problem via a two-dimensional finite element discretization. While

![](./images/811681657659588611_1.jpg)

Figure 1. A 3D slender composite structure.

these are effective methods, the proper set of boundary conditions for higher order effects is not considered. Another asymptotic approach is the formal asymptotic expansion method (FAM), which is based on the three-dimensional static equations [11]. This has been extended to the static problem of piezoelectricity [12]. In this work, a classical piezoelectric beam model was presented and discussed, where the higher order effects and boundary condition issues were not addressed. The decay method has been used in previous studies [8, 9] to determine the boundary conditions; however it is mathematically too complicated for engineering applications. In addition, a finite element realization of the FAM is not trivial since the cross-sectional deformation includes the rigid body modes that should be removed in order to derive the nontrivial warping functions [13-15]. When the higher order effects are significant, a proper set of equations based on the weak form should be derived to provide a connection between the cross-sectional analysis, beam governing equations, and boundary conditions.

The objective of this research is to develop a sophisticated yet efficient homogenization tool for analyzing piezoelectric fiber/polymer composites with arbitrarily assigned electric potential on the cross-section while considering the higher order effect. To address the aforementioned issues, this research proposes an asymptotic approach based on the virtual work principle via a two-dimensional finite element cross- sectional analysis. Utilizing this tool for the modeling and analysis of piezoelectric fiber/polymer composites can provide us with accurate and good physical insight on the behavior of such active structures.

The technical efforts in this investigation can be summarized as follows:

(a) Develop an asymptotic model of the piezoelectric fiber/polymer composite beams via the virtual work principle with the aid of two-dimensional finite element cross-sectional analysis.

(b) Develop a proper set of boundary conditions for piezoelectric beams that are efficient for engineering applications.

(c) Perform an experimental validation study on piezoelectric fiber/polymer composite specimens.

## 2. Asymptotic formulation

A 3D slender beam is considered in this study, which has arbitrary cross-sectional geometry and material anisotropy. It is illustrated in figure 1, where multiple piezoelectric fibers are embedded in a polymeric based matrix to form a beam type structure. Throughout this paper, Greek indices will take values in the set 2, 3, whereas Latin indices will take values 1-3. In order to apply the asymptotic expansion method by taking the advantage of slenderness of beam structures, thebeam cross-section is scaled in the following manner:
$$y_{1}=x_{1}, \quad y_{\alpha}=\frac{x_{\alpha}}{\epsilon}, \quad(1)$$
in which a small parameter, $\epsilon$ , is defined as $\epsilon=\frac{h}{l_{c}}$ , where $h$  and $l_{c}$ represent the maximum dimension of the beam cross section and the characteristic length of the beam, respectively. In equation (1), $y_{1}$ is called the slow or macroscopic scale, whereas $y_{2}$ and $y_{3}$ are referred to as the fast or microscopic scale [16].

### 2.1. Three-dimensional linear piezoelectricity

The three-dimensional linear piezoelectricity (IEEE standard on piezoelectricity [17]), which consists of equilibrium equations, constitutive equations, and strain-displacement andelectric potential relationships, are given as follows:
$$T_{i j, j}=0, \quad D_{i, i}=0,$$

$$T_{i j}=c_{i j k l}^{E} S_{k l}-e_{i j k} E_{k}, \quad D_{i}=e_{i k l} S_{k l}+\varepsilon_{i k}^{S} E_{k}, \quad(2)$$

$$S_{k l}=\frac{1}{2}\left(u_{k, l}+u_{l, k}\right), \quad E_{i}=-\varphi_{, i}$$
where $T_{i j}$ is the stress tensor, $S_{i j}$ is the strain tensor, $D_{i}$ is the electrical displacement vector, $E_{i}$ is the electric field parallel to the $x_{i}$ coordinate, and $\varphi$ is the electric potential. () $_{, i}$  denotes the partial derivative with respect to the $x_{i}$ coordinate. The superscripts $E$ and $S$ represent quantities at constant electric field and at constant strain, respectively. The associatedboundary conditions are summarized as follows:
$$T_{i j} n_{j}=\tilde{p}_{i} \quad \text { on } S_{T},$$

$$\begin{array}{ll}
u_{i}=\tilde{u}_{i} & \text { on } S_{u}, \\
D_{i} n_{i}=\tilde{q} & \text { on } S_{D},
\end{array}\qquad(3)$$

$$\varphi=\tilde{\varphi} \quad \text { on } S_{\varphi},$$

where $S_{(\bullet)}$ represent the boundaries of the beam associated with the subscripts $(\bullet)$, and $(\tilde{\ })$ denotes the prescribed quantity. $p_{i}$ is the traction, and $q$ is the surface charge density.

Considering equations (2) and (3), one can find the virtual work (or corresponding weak form) as follows:
$$
\begin{aligned}
\delta W= & \int_{\Omega}\left(T_{i j} \delta S_{i j}-D_{1} \delta E_{i}\right) \mathrm{d} \Omega-\int_{S_{T}} \tilde{p}_{i} \delta u_{i} \mathrm{~d} S \\
& -\int_{S_{D}} \tilde{q} \delta \varphi \mathrm{d} S=0.
\end{aligned}
\tag{4}
$$

### 2.2. Asymptotic expansions
Before substituting equations (2) into equation (4), one first needs to express the constitutive equations in terms of the small parameter $\epsilon$. By employing the scaled coordinates in equations (1), the strain tensor and the electric field can be rewritten in the matrix form by
$$
\mathbf{S}=\frac{1}{\epsilon} \mathcal{L}_{23} \mathbf{u}+\mathcal{L}_{1} \mathbf{u}_{, 1}, \quad \mathbf{E}=-\frac{1}{\epsilon} \mathcal{L}_{23 d} \varphi-\mathcal{L}_{1 d} \varphi_{, 1}, \quad (5)
$$
where the linear differential operator $\mathcal{L}_{23}$ and the constant matrix $\mathcal{L}_{1}$ are defined by
$$
\mathcal{L}_{23}=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & ()_{, 2} & 0 \\
0 & 0 & ()_{, 3} \\
0 & ()_{, 3} & ()_{, 2} \\
()_{, 3} & 0 & 0 \\
()_{, 2} & 0 & 0
\end{array}\right], \quad \mathcal{L}_{1}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{array}\right].
\tag{6}
$$

Similarly $\mathcal{L}_{23 D}$ and $\mathcal{L}_{1 D}$ are defined as follows:
$$
\mathcal{L}_{23 d}=\left\{\begin{array}{c}
0 \\
()_{, 2} \\
()_{, 3}
\end{array}\right\}, \quad \mathcal{L}_{1 d}=\left\{\begin{array}{l}
1 \\
0 \\
0
\end{array}\right\}.
\tag{7}
$$

The stress tensor and the electrical displacements are then given by
$$
\mathbf{T}=\mathbf{c}^{E} \mathbf{S}-\mathbf{e E}, \quad \mathbf{D}=\mathbf{e}^{\mathrm{t}} \mathbf{S}+\boldsymbol{\varepsilon}^{S} \mathbf{E},
\tag{8}
$$
where the superscript t denotes the transpose of the matrix. The stress and strain tensors, and the electric field and displacement vectors are expressed in the vector forms such that
$$
\begin{gathered}
\mathbf{T}=\left\lfloor T_{11} T_{22} T_{33} T_{23} T_{13} T_{12}\right\rfloor^{\mathrm{t}}, \\
\mathbf{S}=\left\lfloor S_{11} S_{22} S_{33} 2 S_{23} 2 S_{13} 2 S_{12}\right\rfloor^{\mathrm{t}}, \\
\mathbf{E}=\left\lfloor E_{1} E_{2} E_{3}\right\rfloor^{\mathrm{t}}, \\
\mathbf{D}=\left\lfloor D_{1} D_{2} D_{3}\right\rfloor^{\mathrm{t}}.
\end{gathered}
\tag{9}
$$

The order of magnitude of applied tractions, prescribed displacements, electric potential and surface charge density, which yields the behavior of a beam [16, 12], is presupposed as follows:
$$
\begin{aligned}
& \tilde{p}_{1}\left(x_{i}\right)=\epsilon^{1} \bar{p}_{1}\left(y_{i}\right), \tilde{p}_{\alpha}\left(x_{i}\right)=\epsilon^{2} \bar{p}_{\alpha}\left(y_{i}\right), \tilde{q}\left(x_{i}\right)=\epsilon^{1} \bar{q}\left(y_{i}\right), \\
& \tilde{u}_{\alpha}\left(x_{i}\right)=\epsilon^{0} \bar{u}_{\alpha}\left(y_{i}\right), \tilde{u}_{1}\left(x_{i}\right)=\epsilon^{1} \bar{u}_{1}\left(y_{i}\right), \tilde{\varphi}\left(x_{i}\right)=\epsilon^{2} \bar{\varphi}\left(y_{i}\right).
\end{aligned}
\tag{10}
$$

It is also assumed that all the elastic and piezoelectric constants are independent of the small parameter $\epsilon$. According to the standard asymptotic technique, the solutions of the problem can be expanded in terms of the small parameter. Here we seek the two solutions that are the displacements and the electric potential. One should select the scalings for these carefully, because they are closely related to the convergence results of the asymptotic method [16, 12]. The following scalings are assumed:
$$
\begin{aligned}
\mathbf{u}\left(x_{i}\right) & =\mathbf{u}^{(0)}\left(y_{1}\right)+\epsilon \mathbf{u}^{(1)}\left(y_{i}\right)+\epsilon^{2} \mathbf{u}^{(2)}\left(y_{i}\right)+\cdots, \\
\varphi\left(x_{i}\right) & =\epsilon \varphi^{(1)}\left(y_{1}\right)+\epsilon^{2} \varphi^{(2)}\left(y_{i}\right)+\cdots,
\end{aligned}
\tag{11}
$$
where $\mathbf{u}^{(0)}(y_{1}) = \lfloor 0\ v_2^{(0)}\ v_3^{(0)} \rfloor^{\mathrm{t}}$ and $\mathbf{u}^{(k)}(y_{i}) = \lfloor u_1^{(k)}\ u_2^{(k)}\ u_3^{(k)} \rfloor^{\mathrm{t}},\ k\geqslant1$. Notice here that the displacement components $v_i^{(0)}$ is a function of $y_1$ coordinate only, whereas $u_i^{(k)}$ is a function of $y_i$ coordinates.

The stress, strain, electric field and electric displacement expansions can be obtained by substituting equations (11) into equations (9) via equations (5), which are summarized as follows:
$$
\begin{aligned}
\mathbf{T}\left(x_{i}\right) & =\mathbf{T}^{(0)}\left(y_{i}\right)+\epsilon \mathbf{T}^{(1)}\left(y_{i}\right)+\epsilon^{2} \mathbf{T}^{(2)}\left(y_{i}\right)+\cdots, \\
\mathbf{S}\left(x_{i}\right) & =\mathbf{S}^{(0)}\left(y_{i}\right)+\epsilon \mathbf{S}^{(1)}\left(y_{i}\right)+\epsilon^{2} \mathbf{S}^{(2)}\left(y_{i}\right)+\cdots, \\
\mathbf{E}\left(x_{i}\right) & =\mathbf{E}^{(0)}\left(y_{i}\right)+\epsilon \mathbf{E}^{(1)}\left(y_{i}\right)+\epsilon^{2} \mathbf{E}^{(2)}\left(y_{i}\right)+\cdots, \\
\mathbf{D}\left(x_{i}\right) & =\mathbf{D}^{(0)}\left(y_{i}\right)+\epsilon \mathbf{D}^{(1)}\left(y_{i}\right)+\epsilon^{2} \mathbf{D}^{(2)}\left(y_{i}\right)+\cdots.
\end{aligned}
\tag{12}
$$

Subsequently substituting equations (12) into equation (4) and collecting the same order of the small parameter $\epsilon$ yields
$$
\delta W\left(x_{i}\right)=\delta W^{(0)}\left(y_{i}\right)+\epsilon \delta W^{(1)}\left(y_{i}\right)+\epsilon^{2} \delta W^{(2)}\left(y_{i}\right)+\cdots. \tag{13}
$$

From equation (13), one can now obtain the microscopic and macroscopic equations at each asymptotic level.

### 2.3. The zeroth order virtual work
The zeroth order virtual work $\delta W^{(0)}$ is summarized as follows:
$$
\delta W^{(0)}=\int_{y_{1}} \int_{S_{\mathrm{c}}}\left(\delta \mathbf{S}^{(0) t} \mathbf{T}^{(0)}-\delta \mathbf{E}^{(0) t} \mathbf{D}^{(0)}\right) \mathrm{d} S \mathrm{~d} y_{1}=0, \quad (14)
$$
where $S_{\mathrm{c}}$ denotes the beam cross-section. One can easily find the following solutions since the problem is well posed [11, 16, 12]. That is
$$
\mathbf{T}^{(0)}=\mathbf{0}, \quad \mathbf{D}^{(0)}=\mathbf{0}, \quad \mathbf{S}^{(0)}=\mathbf{0}, \quad \mathbf{E}^{(0)}=\mathbf{0}.
\tag{15}
$$

This leads to
$$
\begin{gathered}
\mathbf{S}^{(0)}=\mathbf{0} \rightarrow \mathbf{u}_{\mathrm{p}}^{(1)}=-\lfloor 100\rfloor^{\mathrm{t}}\left(y_{3} v_{3,1}^{(0)}+y_{2} v_{2,1}^{(0)}\right), \\
\mathbf{E}^{(0)}=\mathbf{0} \rightarrow \varphi^{(1)}=\hat{\varphi}^{(1)}\left(y_{1}\right).
\end{gathered}
\tag{16}
$$

The displacement solution is defined up to the rigid body displacements, $\mathbf{u}_{\mathrm{R}}^{(1)}=\left\lfloor v_{1}^{(1)}, v_{2}^{(1)}-y_{3} \phi^{(1)}, v_{3}^{(1)}+y_{2} \phi^{(1)}\right\rfloor^{\mathrm{t}}$, which accounts for three translations $(v_{i})$ and one rotation of

the cross-section $(\phi)$. This forms the fundamental solutions for the problem.

$$
\begin{aligned}
\mathbf{u}^{(1)}=\hat{\mathbf{u}}^{(1)} & \equiv \mathbf{u}_{\mathrm{p}}^{(1)}+\mathbf{u}_{\mathrm{R}}^{(1)}=\Theta\left(y_{\alpha}\right) \hat{\mathbf{v}}^{(1)}\left(y_{1}\right), \\
\varphi^{(1)} & =\hat{\varphi}^{(1)}\left(y_{1}\right).
\end{aligned} \quad(17)
$$

Note that the rigid body displacement has the property, $\mathcal{L}_{23} \mathbf{u}_{\mathrm{R}}=0$, and the matrix $(\Theta)$ and degrees of freedom for the fundamental solution $\left(\hat{\mathbf{v}}^{(1)}\right)$ are defined by

$$
\Theta\left(y_{\alpha}\right)=\left[\begin{array}{cccccc}
1 & 0 & 0 & 0 & -y_{2} & -y_{3} \\
0 & 1 & 0 & -y_{3} & 0 & 0 \\
0 & 0 & 1 & y_{2} & 0 & 0
\end{array}\right], \quad(18)
$$

$$
\hat{\mathbf{v}}^{(1)}\left(y_{1}\right)=\left\lfloor v_{1}^{(1)} v_{2}^{(1)} v_{3}^{(1)} \phi^{(1)} v_{2,1}^{(0)} v_{3,1}^{(0)}\right\rfloor^{\mathrm{t}}. \quad(19)
$$

The first order virtual work $\delta W^{(1)}$ is found to be trivial because of equations (15) and (10).

### 2.4. The second order virtual work

Now let us consider the second order virtual work $\delta W^{(2)}$ that is given as follows:

$$
\begin{aligned}
\delta W^{(2)}= & \int_{y_{1}} \int_{S_{\mathrm{c}}}\left(\delta \mathbf{S}^{(1) \mathrm{t}} \mathbf{T}^{(1)}-\delta \mathbf{E}^{(1) \mathrm{t}} \mathbf{D}^{(1)}\right) \mathrm{d} S \mathrm{~d} y_{1} \\
& -\int_{S_{T}}\left(\overline{\mathbf{p}}^{(1) \mathrm{t}} \delta \mathbf{u}^{(1)}+\overline{\mathbf{p}}^{(2) \mathrm{t}} \delta \mathbf{u}^{(0)}\right) \mathrm{d} S \\
& -\int_{S_{D}} \bar{q} \delta \varphi^{(1)} \mathrm{d} S=0.
\end{aligned}
$$

Equation (20) together with the results of the zeroth order virtual work enables us to find the first nontrivial warping solutions. To this end, the solutions of the second virtual work can be decomposed into two parts as:

$$
\begin{aligned}
\mathbf{u}^{(2)}\left(y_{i}\right) & =\hat{\mathbf{u}}^{(2)}\left(y_{i}\right)+\mathbf{u}_{\mathrm{w}}^{(2)}\left(y_{i}\right), \\
\varphi^{(2)}\left(y_{i}\right) & =\hat{\varphi}^{(2)}\left(y_{1}\right)+\varphi_{\mathrm{w}}^{(2)}\left(y_{i}\right),
\end{aligned}
$$

where the subscript w denotes the warping solution to be found. Subsequently the strain and the electric field can be expressed by

$$
\begin{aligned}
\mathbf{S}^{(1)} & =\mathcal{L}_{1} \Psi\left(y_{\alpha}\right) \hat{\mathbf{e}}^{(1)}+\mathcal{L}_{23} \mathbf{u}_{\mathrm{w}}^{(2)}, \\
\mathbf{E}^{(1)} & =-\mathcal{L}_{1 d} \hat{\varphi}_{, 1}^{(1)}-\mathcal{L}_{23 d} \varphi_{\mathrm{w}}^{(2)},
\end{aligned}
$$

in which the classical strain measure $\hat{\mathbf{e}}^{(1)}$ is expressed as $\hat{\mathbf{e}}^{(1)}=$ $\left\lfloor v_{1,1}^{(1)} v_{2,11}^{(0)} v_{3,11}^{(0)} \phi_{, 1}^{(1)}\right\rfloor^{\mathrm{t}}$, and the matrix $\Psi$ defined by

$$
\Psi\left(y_{\alpha}\right)=\left[\begin{array}{cccc}
1 & -y_{2} & -y_{3} & 0 \\
0 & 0 & 0 & -y_{3} \\
0 & 0 & 0 & y_{2}
\end{array}\right].
$$

Substituting equations (21) and (22) into equation (20) and collecting terms associated with the fundamental solution and the warping solution gives us

$$
\begin{aligned}
& \delta W^{(2)}\left(\delta \mathbf{u}^{(2)}, \delta \varphi^{(2)}\right) \\
& \quad=\delta \widehat{W}^{(2)}\left(\delta \hat{\mathbf{u}}^{(2)}, \delta \hat{\varphi}^{(2)}\right)+\delta W_{\mathrm{w}}^{(2)}\left(\delta \mathbf{u}_{\mathrm{w}}^{(2)}, \delta \varphi_{\mathrm{w}}^{(2)}\right),
\end{aligned}
$$

where the first term forms the one-dimensional macroscopic equation whereas the second term does the two-dimensional microscopic equation for the problem. One needs to find the solution of the two-dimensional microscopic equation that is eventually smeared into the one-dimensional macroscopic equation. By recalling equations (5), the second order virtual work for the microscopic problem can be summarized as follows:

$$
\delta W_{\mathrm{w}}^{(2)}=\int_{y_{1}} \int_{S_{\mathrm{c}}}\left[\delta\left(\mathcal{L}_{23} \mathbf{u}_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{T}^{(1)}+\delta\left(\mathcal{L}_{23 d} \varphi_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{D}^{(1)}\right] \mathrm{d} S \mathrm{~d} y_{1} .
$$

Unlike the zeroth order virtual work, the analytical solution of equation (25) cannot be found in general [16]. Thus one has to seek its solution via a numerical method. In this paper, a finite element discretization is employed to solve the problem. The displacement and the electric potential are interpolated by using the standard isoparametric shape functions such that

$$
\mathbf{u}_{\mathrm{w}}^{(2)}=\mathbf{N}_{u} \mathbf{U}_{\mathrm{w}}^{(2)}, \quad \varphi_{\mathrm{w}}^{(2)}=\mathbf{N}_{\varphi} \Phi_{\mathrm{w}}^{(2)},
$$

where $\mathbf{N}_{u}$ and $\mathbf{N}_{\varphi}$ are the interpolation function matrices. Substituting equation (26) into equation (25) yields

$$
\left[\begin{array}{cc}
K_{u u} & K_{u \varphi} \\
K_{u \varphi}^{\mathrm{t}} & K_{\varphi \varphi}
\end{array}\right]\left\{\begin{array}{c}
\mathbf{U}_{\mathrm{w}}^{(2)} \\
\Phi_{\mathrm{w}}^{(2)}
\end{array}\right\}=\left[\begin{array}{cc}
F_{23 e} & F_{23 \varphi} \\
G_{23 e} & G_{23 \varphi}
\end{array}\right]\left\{\begin{array}{c}
\hat{\mathbf{e}}^{(1)} \\
\hat{\varphi}_{, 1}^{(1)}
\end{array}\right\}, \quad(27)
$$

where the matrices are defined by

$$
\begin{aligned}
K_{u u} & =\left\langle\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{c}^{E}\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)\right\rangle, \\
K_{u \varphi} & =\left\langle\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{e}\left(\mathcal{L}_{23 d} \mathbf{N}_{\varphi}\right)\right\rangle, \\
K_{\varphi \varphi} & =-\left\langle\left(\mathcal{L}_{23 d} \mathbf{N}_{\varphi}\right)^{\mathrm{t}} \varepsilon^{S}\left(\mathcal{L}_{23 d} \mathbf{N}_{\varphi}\right)\right\rangle, \\
F_{23 e} & =-\left\langle\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{c}^{E}\left(\mathcal{L}_{1} \Psi\right)\right\rangle, \\
F_{23 \varphi} & =-\left\langle\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{e}^{\mathrm{t}}\left(\mathcal{L}_{1 d}\right)\right\rangle, \\
G_{23 e} & =-\left\langle\left(\mathcal{L}_{23 d} \mathbf{N}_{\varphi}\right)^{\mathrm{t}} \mathbf{e}\left(\mathcal{L}_{1} \Psi\right)\right\rangle, \\
G_{23 \varphi} & =\left\langle\left(\mathcal{L}_{23 d} \mathbf{N}_{\varphi}\right)^{\mathrm{t}} \varepsilon^{S}\left(\mathcal{L}_{1 d}\right)\right\rangle,
\end{aligned}
$$

in which $\langle\bullet\rangle=\int_{S_{\mathrm{c}}} \bullet \mathrm{d} S$ and $\langle\bullet\rangle_{S_{D}}=\int_{S_{D}} \bullet \mathrm{d} S$.

### 2.5. Solution of microscopic second order virtual work

Now the warping solution can be obtained by solving the discretized equation given in equation (27) in terms of the classical strain measure and the electric field along the axial coordinate. There are two constraints in this equation. First, the mechanical displacement degrees of freedom should be orthogonal to the rigid body displacement $\mathbf{u}_{\mathrm{R}}$. Second, the electric potential degrees of freedom should satisfy the prescribed condition on $S_{\varphi}$.

One needs to consider the mechanical displacement orthogonality condition first. It is given by

$$
\int_{S}\left(\delta \mathbf{u}_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \cdot \mathbf{u}_{\mathrm{R}} \mathrm{d} S=\mathbf{0}
$$

which can be expressed in the matrix form (after the finite element discretization for $\mathbf{u}_{\mathrm{R}}$ [18]). To this end, the rigid body displacement is discretized by

$$
\mathbf{u}_{\mathrm{R}}=\Psi_{\mathrm{R}} \mathbf{v}_{\mathrm{R}}, \quad \Psi_{\mathrm{R}}=\mathbf{N}_{u} \bar{\Psi}_{\mathrm{R}},
$$

which causes equation (29) to become
$$
\left(\delta \mathbf{U}_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{H} \bar{\Psi}_{\mathrm{R}} \mathbf{v}_{\mathrm{R}}=0,\qquad(31)
$$
where $\mathbf{H}=\left\langle\mathbf{N}_{u}^{\mathrm{t}} \mathbf{N}_{u}\right\rangle$, and $\bar{\Psi}_{\mathrm{R}}$ contains four columns that represent the rigid body mode. Notice here that $\mathbf{v}_{\mathrm{R}}$ can be regarded as the Lagrange multiplier.

By following the standard Lagrange multiplier method, one can now combine equations (27) and (31) in such a way that
$$
\begin{aligned}
& {\left[\begin{array}{ccc}
K_{u u} & K_{u \varphi} & \mathbf{H} \bar{\Psi}_{\mathrm{R}} \\
K_{u \varphi}^{\mathrm{t}} & K_{\varphi \varphi} & \mathbf{0} \\
\bar{\Psi}_{\mathrm{R}}^{\mathrm{t}} \mathbf{H} & \mathbf{0} & \mathbf{0}
\end{array}\right]\left\{\begin{array}{l}
\mathbf{U}_{\mathrm{w}}^{(2)} \\
\Phi_{\mathrm{w}}^{(2)}
\end{array}\right\}} \\
& \quad=\left[\begin{array}{cc}
F_{23 e} & F_{23 \varphi} \\
G_{23 e} & G_{23 \varphi} \\
\mathbf{0} & \mathbf{0}
\end{array}\right]\left\{\begin{array}{l}
\hat{\mathbf{e}}^{(1)} \\
\hat{\varphi}_{, 1}^{(1)}
\end{array}\right\}.
\end{aligned}\qquad(32)
$$

The electric potential degrees of freedom $\Phi_{\mathrm{w}}^{(2)}$ also satisfy the electric boundary condition presented in equations (3). To this end, one can separate it in such a way that
$$
\Phi_{\mathrm{w}}^{(2)}=\left[\Phi_{f}^{(2)} \bar{\Phi}\right]^{\mathrm{t}}.\qquad(33)
$$

Note that the prescribed electric potential is scaled to the second order as given in equations (10), and therefore, it only appears at the second order of the electric potential. Applying this to equation (32) and reducing the matrices yield
$$
\begin{aligned}
& {\left[\begin{array}{ccc}
\tilde{K}_{u u} & \widetilde{K}_{u \varphi} & \mathbf{H} \bar{\Psi}_{\mathrm{R}} \\
\tilde{K}_{u \varphi}^{\mathrm{t}} & \widetilde{K}_{\varphi \varphi} & \mathbf{0} \\
\bar{\Psi}_{\mathrm{R}}^{\mathrm{t}} \mathbf{H} & \mathbf{0} & \mathbf{0}
\end{array}\right]\left\{\begin{array}{l}
\mathbf{U}_{\mathrm{w}}^{(2)} \\
\Phi_{f}^{(2)} \\
\mathbf{v}_{\mathrm{R}}
\end{array}\right\}} \\
& \quad=\left[\begin{array}{cc}
\widetilde{F}_{23 e} & \widetilde{F}_{23 \varphi} \\
\widetilde{G}_{23 e} & \widetilde{G}_{23 \varphi} \\
\mathbf{0} & \mathbf{0}
\end{array}\right]\left\{\begin{array}{l}
\hat{\mathbf{e}}^{(1)} \\
\hat{\varphi}_{, 1}^{(1)}
\end{array}\right\}-\left\{\begin{array}{c}
\widehat{K}_{u \varphi} \\
\mathbf{0} \\
\mathbf{0}
\end{array}\right\} \bar{\Phi},
\end{aligned}\qquad(34)
$$
where $\tilde{\bullet}$ matrices indicate the reduced matrices from $\bullet$ matrices, which is associated with the prescribed potential degrees of freedom $\bar{\Phi}$, and $\widehat{\bullet}$ matrices are parts of $\bullet$ matrices.

Consequently the warping solutions of equation (34) can be expressed as follows:
$$
\begin{aligned}
\mathbf{U}_{\mathrm{w}}^{(2)} & =\Gamma_{r m e}^{(1)} \hat{\mathbf{e}}^{(1)}+\Gamma_{\varphi}^{(1)} \hat{\varphi}_{, 1}^{(1)}+\Gamma_{p}^{(1)} \bar{\Phi}, \\
\Phi_{\mathrm{w}}^{(2)} & =\Xi_{\mathrm{e}}^{(1)} \hat{\mathbf{e}}^{(1)}+\Xi_{\varphi}^{(1)} \hat{\varphi}_{, 1}^{(1)}+\Xi_{p}^{(1)} \bar{\Phi},
\end{aligned}\qquad(35)
$$
where $\Phi_{\mathrm{w}}^{(2)}$ is reconstructed via equation (33). The subscripts, $e, \varphi$ and $p$ indicate the one-dimensional macroscopic strain, the one-dimensional electric potential, and the prescribed electric potential, respectively. $\Gamma_{(\bullet)}^{(1)}$ and $\Xi_{(\bullet)}^{(1)}$ represent the cross-sectional mechanical warping and electric potential distribution due to $(\bullet)$. Here one can clearly see that the warping solutions are affected by the electric potential as well as the mechanical strain.

### 2.6. Microscopic higher order virtual work

In the third order virtual work, the macroscopic and microscopic equations obtained from the second order virtual work appear again, already set to zero. In this way, the microscopic third order virtual work can be summarized as follows:
$$
\begin{aligned}
\delta W_{\mathrm{w}}^{(3)}= & \int_{y_{1}} \int_{S_{\mathrm{c}}}\left[\delta\left(\mathcal{L}_{23} \mathbf{u}_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{T}^{(2)}+\delta\left(\mathcal{L}_{1} \mathbf{u}_{w, 1}^{(2)}\right)^{\mathrm{t}} \mathbf{T}^{(1)}\right. \\
& \left.+\delta\left(\mathcal{L}_{23 d} \varphi_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{D}^{(2)}+\delta\left(\mathcal{L}_{1 d} \varphi_{w, 1}^{(2)}\right)^{\mathrm{t}} \mathbf{D}^{(1)}\right] \mathrm{d} S \mathrm{~d} y_{1} \\
& -\int_{S_{T}} \delta \mathbf{u}_{\mathrm{w}}^{(2) \mathrm{t}} \overline{\mathbf{p}}^{(1)} \mathrm{d} S-\int_{S_{D}} \delta \varphi_{\mathrm{w}}^{(2)} \bar{q} \mathrm{~d} S=0,
\end{aligned}\qquad(36)
$$
which can be rewritten in the matrix form
$$
\begin{aligned}
& {\left[\begin{array}{cc}
K_{u u} & K_{u \varphi} \\
K_{u \varphi}^{\mathrm{t}} & K_{\varphi \varphi}
\end{array}\right]\left\{\begin{array}{l}
\mathbf{U}_{\mathrm{w}}^{(3)} \\
\Phi_{\mathrm{w}}^{(3)}
\end{array}\right\}=\left[\begin{array}{ll}
F_{23 e} & F_{23 \varphi} \\
G_{23 e} & G_{23 \varphi}
\end{array}\right]\left\{\begin{array}{l}
\hat{\mathbf{e}}^{(2)} \\
\hat{\varphi}_{, 1}^{(2)}
\end{array}\right\}} \\
& \quad+\left[\begin{array}{ll}
F_{11 e} & F_{11 \varphi} \\
G_{11 e} & G_{11 \varphi}
\end{array}\right]\left\{\begin{array}{l}
\hat{\mathbf{e}}_{, 1}^{(1)} \\
\hat{\varphi}_{, 11}^{(1)}
\end{array}\right\} \\
& \quad+\left[\begin{array}{ll}
F_{231 u} & F_{231 \varphi} \\
G_{231 u} & G_{231 \varphi}
\end{array}\right]\left\{\begin{array}{l}
\mathbf{U}_{w, 1}^{(2)} \\
\Phi_{w, 1}^{(2)}
\end{array}\right\}+\left\{\begin{array}{l}
F_{P}^{(3)} \\
F_{Q}^{(3)}
\end{array}\right\},
\end{aligned}\qquad(37)
$$
in which the new matrices are defined by
$$
\begin{aligned}
F_{11 e} & =\left\langle\left(\mathcal{L}_{1} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{c}^{E}\left(\mathcal{L}_{1} \Psi\right)\right\rangle, \\
F_{11 \varphi} & =\left\langle\left(\mathcal{L}_{1} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{e}^{\mathrm{t}}\left(\mathcal{L}_{1 d}\right)\right\rangle, \\
G_{11 e} & =\left\langle\left(\mathcal{L}_{1 d} \mathbf{N}_{\varphi}\right)^{\mathrm{t}} \mathbf{e}\left(\mathcal{L}_{1} \Psi\right)\right\rangle, \\
G_{11 \varphi} & =-\left\langle\left(\mathcal{L}_{1 d} \mathbf{N}_{\varphi}\right)^{\mathrm{t}} \varepsilon^{S}\left(\mathcal{L}_{1 d}\right)\right\rangle, \\
F_{231 u} & =\left\langle\left(\mathcal{L}_{1} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{c}^{E}\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)\right\rangle-\left\langle\left(\mathcal{L}_{23} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{c}^{E}\left(\mathcal{L}_{1} \mathbf{N}_{u}\right)\right\rangle, \quad(38) \\
F_{231 \varphi} & =\left\langle\left(\mathcal{L}_{1} \mathbf{N}_{u}\right)^{\mathrm{t}} \mathbf{e}^{\mathrm{t}}\left(\mathcal{L}_{23 d} \mathbf{N}_{\varphi}\right)\right\rangle-\left\langle\left(\mathcal{L}_{23}$$

$$
F_{P}^{(3)}=\left\langle\mathbf{N}_{u}^{\mathrm{t}} \overline{\mathbf{p}}^{(1)}\right\rangle_{\partial S}, \quad F_{Q}^{(3)}=\left\langle\mathbf{N}_{\varphi}^{\mathrm{t}} \bar{q}\right\rangle_{S_{D}},
$$
where $\langle\bullet\rangle_{\partial S}=\int_{\partial S} \bullet \mathrm{d} S$.

One can solve the preceding equation by removing the rigid body modes via the Lagrange multiplier method and applying the electric potential boundary condition, which is outlined in section 2.5. The electric potential for this microscopic problem is set to zero because of the scaling, i.e., $\Phi_{\mathrm{w}}^{(3)}=\left[\Phi_{f}^{(3)} \mathbf{0}\right]^{\mathrm{t}}$. The solution of equation (37) is then represented by
$$
\begin{aligned}
& \mathbf{U}_{\mathrm{w}}^{(3)}=\Gamma_{\mathrm{e}}^{(1)} \hat{\mathbf{e}}^{(2)}+\Gamma_{\mathrm{e}}^{(2)} \hat{\mathbf{e}}_{, 1}^{(1)}+\Gamma_{\varphi}^{(1)} \hat{\varphi}_{, 1}^{(2)}+\Gamma_{\varphi}^{(2)} \hat{\varphi}_{, 11}^{(1)}+\overline{\mathbf{U}}_{F}^{(3)}, \\
& \Phi_{\mathrm{w}}^{(3)}=\Xi_{\mathrm{e}}^{(1)} \hat{\mathbf{e}}^{(2)}+\Xi_{\mathrm{e}}^{(2)} \hat{\mathbf{e}}_{, 1}^{(1)}+\Xi_{\varphi}^{(1)} \hat{\varphi}_{, 1}^{(2)}+\Xi_{\varphi}^{(2)} \hat{\varphi}_{, 11}^{(1)}+\bar{\Phi}_{F}^{(3)},
\end{aligned}\qquad(39)
$$
where the last term with the subscript, $F$, are associated with the prescribed traction and surface charge density on the cross- sectional boundary of a beam.

Finally the microscopic higher order virtual work can now be generalized as follows:
$$
\begin{aligned}
\delta W_{\mathrm{w}}^{(k)}= & \int_{y_{1}} \int_{S_{\mathrm{c}}}\left[\delta l\left(\mathcal{L}_{23} \mathbf{u}_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{T}^{(k-1)}\right. \\
& +\delta\left(\mathcal{L}_{1} \mathbf{u}_{w, 1}^{(2)}\right)^{\mathrm{t}} \mathbf{T}^{(k-2)}+\delta\left(\mathcal{L}_{23 d} \varphi_{\mathrm{w}}^{(2)}\right)^{\mathrm{t}} \mathbf{D}^{(k-1)} \\
& \left.+\delta\left(\mathcal{L}_{1 d} \varphi_{w, 1}^{(2)}\right)^{\mathrm{t}} \mathbf{D}^{(k-2)}\right] \mathrm{d} S \mathrm{~d} y_{1}=0,
\end{aligned}\qquad(40)
$$


where $k \geqslant 4$. The solutions for the microscopic higher virtual work are eventually generalized by

$$
\begin{aligned}
\mathbf{U}_{\mathrm{w}}^{(k)}= & \sum_{m=1}^{k-1}\left(\Gamma_{e}^{(m)} \partial_{y_{1}}^{m-1} \hat{\mathbf{e}}^{(k-m)}+\Gamma_{\varphi}^{(m)} \partial_{y_{1}}^{m} \hat{\varphi}^{(k-m)}\right)+\overline{\mathbf{U}}_{F}^{(k)}, \\
\Phi_{\mathrm{w}}^{(k)}= & \sum_{m=1}^{k-1}\left(\Xi_{e}^{(m)} \partial_{y_{1}}^{m-1} \hat{\mathbf{e}}^{(k-m)}+\Xi_{\varphi}^{(m)} \partial_{y_{1}}^{m} \hat{\varphi}^{(k-m)}\right)+\bar{\Phi}_{F}^{(k)}. \\
& (41)
\end{aligned}
$$

Note that it is not necessary to compute all the matrices at each microscopic virtual work to obtain the warping solutions. In fact, the matrices $\Gamma^{(k)}$ and $\Xi^{(k)}$ with $k \geqslant 3$ are simply computed by the recursive formulation that is similar to the case of composite beams [13], so that one can obtain good physical insight of the three-dimensional electromechanical behaviors without solving the macroscopic virtual work.

### 3. Macroscopic formulation

In this section, a set of macroscopic one-dimensional equations are systematically derived from the macroscopic virtual work at each level, $\delta \widehat{W}^{(k)}$. The macroscopic one-dimensional boundary conditions are discussed, especially for the displacement prescribed boundary.

#### 3.1. One-dimensional macroscopic problems

Some meaningful information related to the beam equilibrium equation appears first at the second order virtual work. Recalling equations (22) and (24), one can write the second order macroscopic virtual work as follows:

$$
\begin{aligned}
\delta \widehat{W}^{(2)}= & \int_{y_{1}} \int_{S_{\mathrm{c}}}\left[\delta\left(\mathcal{L}_{1} \Psi \hat{\mathbf{e}}^{(1)}\right)^{\mathrm{t}} \mathbf{T}^{(1)}+\delta\left(\mathcal{L}_{1 d} \hat{\varphi}_{, 1}^{(1)}\right)^{\mathrm{t}} \mathbf{D}^{(1)}\right] \mathrm{d} S \mathrm{~d} y_{1} \\
& -\int_{S_{T}}\left(\overline{\mathbf{p}}^{(1) t} \delta \mathbf{u}^{(1)}+\overline{\mathbf{p}}^{(2) t} \delta \mathbf{u}^{(0)}\right) \mathrm{d} S \\
& -\int_{S_{D}} \bar{q} \delta \hat{\varphi}^{(1)} \mathrm{d} S=0,
\end{aligned}
$$

which can be simplified by

$$
\int_{y_{1}}\left[\delta \hat{\mathbf{e}}^{(1) t} \mathcal{N}^{(1)}+\delta \hat{\varphi}_{, 1}^{(1)} \mathcal{D}^{(1)}\right] \mathrm{d} y_{1}=\mathcal{F}^{(1)}+\mathcal{Q}^{(1)},
$$

where

$$
\begin{gathered}
\mathcal{N}^{(1)} \equiv\left\langle\left(\mathcal{L}_{1} \Psi\right)^{\mathrm{t}} \mathbf{T}^{(1)}\right\rangle, \quad \mathcal{D}^{(1)} \equiv\left\langle\mathcal{L}_{1 d} \mathbf{D}^{(1)}\right\rangle, \\
\mathcal{F}^{(1)} \equiv\left\langle\bar{p}_{1}\left(\delta v_{1}^{(1)}-y_{\alpha} \delta v_{\alpha, 1}^{(0)}\right)+\bar{p}_{\alpha} \delta v_{\alpha}^{(0)}\right\rangle_{S_{T}}, \\
\mathcal{Q}^{(1)} \equiv\left\langle\bar{q} \delta \hat{\varphi}^{(1)}\right\rangle_{S_{D}} .
\end{gathered}
$$

Equation (43) is referred to as the zeroth order macroscopic problem, since it is comparable to that of Euler-Bernoulli beam theory.

The third order virtual work forms the first order macroscopic problem. The process is similar to that in the third order microscopic virtual work. The preceding macroscopic equations appear again. By omitting such equations, the third order macroscopic virtual work is then summarized by

$$
\begin{aligned}
\delta \widehat{W}^{(3)}= & \int_{y_{1}} \int_{S_{\mathrm{c}}}\left[\delta\left(\mathcal{L}_{1} \Psi \hat{\mathbf{e}}^{(1)}\right)^{\mathrm{t}} \mathbf{T}^{(2)}+\delta\left(\mathcal{L}_{1 d} \hat{\varphi}_{, 1}^{(1)}\right)^{\mathrm{t}} \mathbf{D}^{(2)}\right] \mathrm{d} S \mathrm{~d} y_{1} \\
& -\int_{S_{T}} \overline{\mathbf{p}}^{(2) \mathrm{t}} \delta \mathbf{u}^{(1)} \mathrm{d} S,
\end{aligned}
$$

which becomes

$$
\int_{y_{1}}\left[\delta \hat{\mathbf{e}}^{(1) \mathrm{t}} \mathcal{N}^{(2)}+\delta \hat{\varphi}_{, 1}^{(1)} \mathcal{D}^{(2)}\right] \mathrm{d} y_{1}=\mathcal{F}^{(2)},
$$

where

$$
\mathcal{F}^{(2)} \equiv\left\langle\left(\bar{p}_{3} y_{2}-\bar{p}_{2} y_{3}\right) \delta \phi^{(1)}\right\rangle_{S_{T}} .
$$

Finally the higher order macroscopic problems can be now generalized as follows:

$$
\widetilde{W}^{(k)}=\int_{y_{1}}\left[\delta \hat{\mathbf{e}}^{(1) t} \mathcal{N}^{(k-1)}+\delta \hat{\varphi}_{, 1}^{(1)} \mathcal{D}^{(k-1)}\right] \mathrm{d} y_{1}=0,
$$

where $k \geqslant 4$. Note that there are no external loadings in these problems. The higher order resultants $\mathcal{N}^{(k-1)}$ and $\mathcal{D}^{(k-1)}$ include the derivatives $\left(\partial_{y_{1}}\right)$ of the solutions of previous macroscopic problems that act like the external loadings.

#### 3.2. Macroscopic constitutive equations

The mechanical and electric resultants, $\mathcal{N}^{(k)}$ and $\mathcal{D}^{(k)}, k \geqslant 1$, defined in previous sections are explicitly expressed by

$$
\mathcal{N}^{(k)} \equiv\left\lfloor N^{(k)} M_{\alpha}^{(k)} M_{1}^{(k)}\right\rfloor^{\mathrm{t}}, \quad \mathcal{D}^{(k)} \equiv Q_{1}^{(k)},
$$

where

$$
\begin{gathered}
N^{(k)}=\left\langle T_{11}^{(k)}\right\rangle, \quad M_{\alpha}^{(k)}=-\left\langle y_{\alpha} T_{11}^{(k)}\right\rangle, \\
M_{1}^{(k)}=\left\langle y_{2} T_{13}^{(k)}-y_{3} T_{12}^{(k)}\right\rangle, \quad Q_{1}^{(k)}=\left\langle D_{1}^{(k)}\right\rangle .
\end{gathered}
$$

One can now obtain the first order macroscopic electromechanical constitutive equation for the zeroth order macroscopic problem.

$$
\left\{\begin{array}{c}
\mathcal{N}^{(1)} \\
\mathcal{Q}_{1}^{(1)}
\end{array}\right\}=\left[\begin{array}{cc}
\mathcal{A}_{\mathrm{e}}^{(1)} & \mathcal{A}_{\varphi}^{(1)} \\
\mathcal{B}_{\mathrm{e}}^{(1)} & \mathcal{B}_{\varphi}^{(1)}
\end{array}\right]\left\{\begin{array}{c}
\hat{\mathbf{e}}^{(1)} \\
\hat{\varphi}_{, 1}^{(1)}
\end{array}\right\}+\left\{\begin{array}{c}
\mathcal{A}_{p}^{(1)} \\
\mathcal{B}_{p}^{(1)}
\end{array}\right\} \bar{\Phi},
$$

where the dimensions of $\mathcal{A}_{\mathrm{e}}^{(1)}$ and $\mathcal{A}_{\varphi}^{(1)}$ are $4 \times 4$ and $4 \times 1$, respectively, and $\mathcal{A}_{\mathrm{p}}^{(1)}$ is a $4 \times n_{p}$ matrix whose column depends on the degrees of freedom of the prescribed potential. They are defined by

$$
\begin{gathered}
\mathcal{A}_{\mathrm{e}}^{(1)}=\left\langle\left(\mathcal{L}_{1} \Psi\right)^{\mathrm{t}} \mathbf{c}^{E}\left(\mathcal{L}_{1} \Psi\right)\right\rangle+F_{23 e}^{\mathrm{t}} \Gamma_{\mathrm{e}}^{(1)}+G_{23 e}^{\mathrm{t}} \Xi_{\mathrm{e}}^{(1)}, \\
\mathcal{A}_{\varphi}^{(1)}=\left\langle\left(\mathcal{L}_{1} \Psi\right)^{\mathrm{t}} \mathbf{e}^{\mathrm{t}}\left(\mathcal{L}_{1 d}\right)\right\rangle+F_{23 e}^{\mathrm{t}} \Gamma_{\varphi}^{(1)}+G_{23 e}^{\mathrm{t}} \Xi_{\varphi}^{(1)}, \\
\mathcal{A}_{p}^{(1)}=F_{23 e}^{\mathrm{t}} \Gamma_{p}^{(1)}+G_{23 e}^{\mathrm{t}} \Xi_{p}^{(1)},
\end{gathered}
$$

and the matrices associated with the electric displacement, $\mathcal{B}_{\mathrm{e}}^{(1)}=(1 \times 4), \mathcal{B}_{\varphi}^{(1)}=(1 \times 1)$ and $\mathcal{B}_{\mathrm{p}}^{(1)}=\left(1 \times n_{p}\right)$, are defined as

$$
\begin{gathered}
\mathcal{B}_{\mathrm{e}}^{(1)}=\left\langle\left(\mathcal{L}_{1 d}\right)^{\mathrm{t}} \varepsilon\left(\mathcal{L}_{1} \Psi\right)\right\rangle+F_{23 \varphi}^{\mathrm{t}} \Gamma_{\mathrm{e}}^{(1)}+G_{23 \varphi}^{\mathrm{t}} \Xi_{\mathrm{e}}^{(1)}, \\
\mathcal{B}_{\varphi}^{(1)}=-\left\langle\left(\mathcal{L}_{1 d}\right)^{\mathrm{t}} \varepsilon^{S}\left(\mathcal{L}_{1 d}\right)\right\rangle+F_{23 \varphi}^{\mathrm{t}} \Gamma_{\varphi}^{(1)}+G_{23 \varphi}^{\mathrm{t}} \Xi_{\varphi}^{(1)}, \\
\mathcal{B}_{p}^{(1)}=F_{23 \varphi}^{\mathrm{t}} \Gamma_{p}^{(1)}+G_{23 \varphi}^{\mathrm{t}} \Xi_{p}^{(1)} .
\end{gathered}
$$

Similarly the higher order macroscopic constitutive equations can now be generalized as follows:

$$
\begin{aligned}
\left\{\begin{array}{c}
\mathcal{N}^{(k)} \\
Q_{1}^{(k)}
\end{array}\right\} & =\sum_{m=1}^{k}\left(\left[\begin{array}{cc}
\mathcal{A}_{\mathrm{e}}^{(m)} & \mathcal{A}_{\varphi}^{(m)} \\
\mathcal{B}_{\mathrm{e}}^{(m)} & \mathcal{B}_{\varphi}^{(m)}
\end{array}\right]\left\{\begin{array}{c}
\partial_{y_{1}}^{m-1} \hat{\mathbf{e}}^{(k-m+1)} \\
\partial_{y_{1}}^{m-1} \hat{\varphi}_{, 1}^{(k-m+1)}
\end{array}\right\}\right) \\
& +\left[\begin{array}{cc}
F_{23 e}^{\mathrm{t}} & G_{23 e}^{\mathrm{t}} \\
F_{23 \varphi}^{\mathrm{t}} & G_{23 \varphi}^{\mathrm{t}}
\end{array}\right]\left\{\begin{array}{c}
\overline{\mathbf{U}}_{F}^{(k+1)} \\
\bar{\Phi}_{F}^{(k+1)}
\end{array}\right\}, \quad k \geqslant 2,
\end{aligned}
\tag{54}
$$

in which the term presented in the second line is induced by the warping due to the prescribed traction and surface charge density on the cross-sectional boundary. The matrices $\mathcal{A}^{(k)}$ and $\mathcal{B}^{(k)}$ are computed by

$$
\begin{aligned}
& \mathcal{A}_{r}^{(k)}=F_{23 e}^{\mathrm{t}} \Gamma_{r}^{(k)}+F_{11 e}^{\mathrm{t}} \Gamma_{r}^{(k-1)}+G_{23 e}^{\mathrm{t}} \Xi_{r}^{(k)}+G_{11 e}^{\mathrm{t}} \Xi_{r}^{(k-1)}, \\
& \mathcal{B}_{r}^{(k)}=F_{23 \varphi}^{\mathrm{t}} \Gamma_{r}^{(k)}+F_{11 \varphi}^{\mathrm{t}} \Gamma_{r}^{(k-1)}+G_{23 \varphi}^{\mathrm{t}} \Xi_{r}^{(k)}+G_{11 \varphi}^{\mathrm{t}} \Xi_{r}^{(k-1)},
\end{aligned}
\tag{55}
$$

where $k \geqslant 2$, and the subscript $r$ represents either $e$ or $\varphi$.

The finite element discretization is applied to the one-dimensional macroscopic problems by using three-noded finite elements. Quadratic Lagrangian functions for $v_{1}^{(k)}, \phi^{(k)}$ and $\hat{\varphi}^{(k)}$, and fifth order Hermite functions for $v_{\alpha}^{(k)}$ are employed. A detailed procedure is omitted here for brevity, which can be found in reference [13].

### 3.3. One-dimensional macroscopic boundary conditions

By considering the zeroth order macroscopic problem, equation (43), and carrying out the integration by parts, one can obtain the zeroth order macroscopic boundary conditions as follows:

$$
\begin{gathered}
\delta \tilde{\mathbf{v}}^{(1)}=0: \quad N^{(1)}=\bar{N}, \quad M_{\alpha, 1}^{(1)}=-\bar{V}_{\alpha}, \\
M_{1}^{(1)}=0, \quad M_{\alpha}^{(1)}=\bar{M}_{\alpha}, \quad \delta \hat{\varphi}^{(1)}=0: \\
Q_{1}^{(1)}=\bar{Q}_{1},
\end{gathered}
\tag{56}
$$

where $\tilde{\mathbf{v}}^{(1)} \equiv\left\lfloor v_{1}^{(1)} v_{\alpha}^{(0)} \phi^{(1)} v_{\alpha, 1}^{(0)}\right\rfloor^{\mathrm{t}}$, and the prescribed quantities for the edge boundary perpendicular to the $y_{1}$ coordinate can be expressed by

$$
\begin{gathered}
\left\lfloor\bar{N} \bar{M}_{2} \bar{M}_{3}\right\rfloor^{\mathrm{t}}=\left\langle\Theta^{\mathrm{t}}\left\lfloor\bar{p}_{1} 00\right\rfloor^{\mathrm{t}}\right\rangle_{S_{r}}, \\
\bar{V}_{\alpha}=\left\langle\bar{p}_{\alpha}\right\rangle_{S_{r}}, \quad \bar{Q}_{1}=\langle\bar{q}\rangle_{S_{D}},
\end{gathered}
\tag{57}
$$

and similarly the first order macroscopic boundary conditions for the first order macroscopic problem are given by

$$
\begin{gathered}
\delta \tilde{\mathbf{v}}^{(2)}=0: \quad N^{(2)}=0, \quad M_{\alpha, 1}^{(2)}=0, \\
M_{1}^{(2)}=\bar{M}_{1}, \quad M_{\alpha}^{(2)}=0, \\
\delta \hat{\varphi}^{(2)}=0: \quad Q_{1}^{(2)}=0,
\end{gathered}
\tag{58}
$$

where $\bar{M}_{1}=\left\langle y_{2} \bar{p}_{3}-y_{3} \bar{p}_{2}\right\rangle_{S_{r}}$.

Finally the higher order beam boundary conditions are generalized as follows:

$$
\begin{gathered}
\delta \tilde{\mathbf{v}}^{(k)}=0: \quad N^{(k)}=0, \quad M_{\alpha, 1}^{(k)}=0, M_{1}^{(k)}=0, \\
M_{\alpha}^{(k)}=0, \delta \hat{\varphi}^{(k)}=0: \quad Q_{1}^{(k)}=0,
\end{gathered}
\tag{59}
$$

where $k \geqslant 3$.

The boundary conditions presented above provide us with guidelines to solving the macroscopic problems at each level. The displacement boundary conditions however are not asymptotically correct in general [8, 19]. In other words, the mechanical displacement degrees of freedom of the macroscopic problems, $\tilde{\mathbf{v}}^{(k)}$, cannot be arbitrarily prescribed. Although there exists a way to obtain the asymptotically correct displacement boundary conditions [8], it is not practical for engineering applications. To circumvent this, one can introduce the orthogonality conditions of asymptotic displacements, $\mathbf{u}^{(k)}$, to six fundamental solutions, $\hat{\mathbf{u}}^{(k)}$, as constraints [13].

The displacement boundary conditions associated with $\delta \tilde{\mathbf{v}}^{(k)}$ can be interpreted as constraint equations. In this way, accurate yet simple boundary conditions can be obtained, which are asymptotically correct up to $\mathcal{O}(\epsilon^{2})$ for orthotropic beams [20]. One can express them in the weak form

$$
\int_{S_{u}}\left(\delta \hat{\mathbf{u}}^{(k)}\right)^{\mathrm{t}}\left(\mathbf{u}^{(k)}-\overline{\mathbf{u}}\right) \mathrm{d} S=0,
\tag{60}
$$

in which $S_{u}$ denotes the displacement prescribed boundary. Substituting equations (17) into the above yields

$$
\left(\delta \hat{\mathbf{v}}^{(k)}\right)^{\mathrm{t}} \int_{S_{u}} \Theta^{\mathrm{t}}\left(y_{2}, y_{3}\right)\left(\mathbf{u}^{(k)}-\overline{\mathbf{u}}\right) \mathrm{d} S=0,
\tag{61}
$$

where the matrix $\Theta$ related to six fundamental solutions is given in equation (18), and $\overline{\mathbf{u}}$ represents the vector containing the prescribed displacements, which $\overline{\mathbf{u}}=\mathbf{0}$ for a clamped boundary. Similar constraint equations can be found in flexible multibody dynamics [21]. The asymptotic displacements $\mathbf{u}^{(k)}$ are given by

$$
\mathbf{u}^{(k)}=\Theta \hat{\mathbf{v}}^{(k)}+\mathbf{N}_{u} \mathbf{U}_{\mathrm{w}}^{(k)}, \quad k \geqslant 1,
\tag{62}
$$

in which $\mathbf{U}_{\mathrm{w}}^{(k)}$ is defined in equations (41), and $\mathbf{U}_{\mathrm{w}}^{(1)}=\mathbf{0}$.

Substituting equation (62) into equation (61) via equations (41) yields the macroscopic displacement boundary conditions on $S_{u}$ as follows:

$$
\begin{gathered}
\left.\hat{\mathbf{v}}^{(1)}\right|_{S_{u}}=\mathbf{0}, \\
\left.\hat{\mathbf{v}}^{(2)}\right|_{S_{u}}=-\mathbf{H}_{\theta}^{-1}\left\langle\Theta^{\mathrm{t}} \mathbf{N}_{u}\right\rangle\left(\Gamma_{\mathrm{e}}^{(1)} \hat{\mathbf{e}}^{(1)}+\Gamma_{\varphi}^{(1)} \hat{\varphi}_{, 1}^{(1)}+\Gamma_{p}^{(1)} \bar{\Phi}\right), \\
\left.\hat{\mathbf{v}}^{(k)}\right|_{S_{u}}=-\mathbf{H}_{\theta}^{-1}\left\langle\Theta^{\mathrm{t}} \mathbf{N}_{u}\right\rangle \mathbf{U}_{\mathrm{w}}^{(k)}, \quad k \geqslant 3,
\end{gathered}
\tag{63}
$$

where $\mathbf{H}_{\theta} \equiv\left\langle\Theta^{\mathrm{t}} \Theta\right\rangle$. Note that the fundamental displacements, $\hat{\mathbf{v}}^{(k)}$, are different from the macroscopic displacement boundary conditions, $\delta \tilde{\mathbf{v}}^{(k)}$. The boundary conditions given in equations (63) should be rearranged so that they match with the one-dimensional macroscopic problems [13].

## 4. Experimental setup and procedure

In order to validate this analytical method, experimental investigations are performed on a piezoelectric fiber/polymer composite specimen. In the following section, the fabrication methodology is presented, as well as the procedure used for the experimentation of the composite specimen.

![](./images/811681657659588611_2.jpg)
![](./images/811681657659588611_3.jpg)

Figure 2. Specimen fabrication; (a) mold with PZT strips inserted and (b) elastomer inserted.

The first step used in the fabrication process of the piezoelectric fiber/polymer composite beams is to create a mold capable of precisely locating the piezoelectric fibers while the polymer composite is added (see figure 2). This mold consists of a two piece, solid acrylic frame, machined to create a cavity the size of the external dimensions of the beam. The two pieces are fixed together with screws so that the final composite beam can be easily removed from the mold. Additionally, there are two end pieces whose main function is to hold the piezoelectric fibers in place while the beam is assembled. Holes are precisely drilled in these two pieces in order to correctly space the piezoelectric fibers. For this specimen, four 1 mm holes are drilled exactly 3 mm apart, forming a square for the fibers. Additionally, one of the end pieces is manufactured so that it can be used as the cantilevered side of the beam, while the other end piece will be removed after the manufacturing process is completed. This mold will produce composite specimens with four piezoelectric fibers and with the final dimensions of 4.34 mm deep ×4.14 mm wide ×47 mm long.

The specimens used in this verification study utilize commercially available PZT, whose material properties are given in table 1. Using a dicing saw, strips are cut on-site from a larger sample, which comes coated and poled. For the preliminary tests, PZT strips 1 mm × 1 mm were used. For the matrix material, a silicone elastomer is used (Dow Corning 170), which is a two-part, 1:1 weight ratio fast curing elastomer. With a working time of approximately 1 h, the elastomer can be mixed together in liquid form and poured into the mold. After curing for 24 h at room temperature, the modulus of elasticity is around 1 MPa.

The beam is assembled by clamping the mold together, inserting the four PZT fibers into the holes, with one end extending out of the cantilevered side, as seen in figure 2. This is done so that the PZT fibers can be more easily wired. When the PZT is in place, the elastomer is poured in to the mold, excess elastomer is removed, and the specimen is allowed to harden for 24 h. After the elastomer has cured, the specimen is removed from the mold, and each PZT fiber is connected to lead wires, so that each PZT fiber can be controlled separately.

The experimental test setup, as seen in figure 3, is comprised of the test specimen, a fiber optic sensor (PHILTEC D20) used to measure the out-of-plane displacement of the beam, and a computer with dSpace and MATLAB used for signal processing. The fiber optic sensor is calibrated and is used to measure the tip deflection of the beam.

<table>
<caption>Table 1. Material properties of PZT4 and silicone elastomer.</caption>
<thead>
<tr>
<th>Moduli</th>
<th>Unit</th>
<th>Silicone elastomer</th>
<th>PZT-4</th>
</tr>
</thead>
<tbody>
<tr>
<td>$c_{11}^{E}$</td>
<td>GPa</td>
<td>$1.2×10^{-3}$</td>
<td>139</td>
</tr>
<tr>
<td>$c_{12}^{E}$</td>
<td>GPa</td>
<td>$0.4×10^{-3}$</td>
<td>78</td>
</tr>
<tr>
<td>$c_{13}^{E}$</td>
<td>GPa</td>
<td>$0.4×10^{-3}$</td>
<td>74</td>
</tr>
<tr>
<td>$c_{22}^{E}$</td>
<td>GPa</td>
<td>$1.2×10^{-3}$</td>
<td>139</td>
</tr>
<tr>
<td>$c_{23}^{E}$</td>
<td>GPa</td>
<td>$0.4×10^{-3}$</td>
<td>74</td>
</tr>
<tr>
<td>$c_{33}^{E}$</td>
<td>GPa</td>
<td>$1.2×10^{-3}$</td>
<td>115</td>
</tr>
<tr>
<td>$c_{44}^{E}$</td>
<td>GPa</td>
<td>$0.4×10^{-3}$</td>
<td>26</td>
</tr>
<tr>
<td>$c_{55}^{E}$</td>
<td>GPa</td>
<td>$0.4×10^{-3}$</td>
<td>26</td>
</tr>
<tr>
<td>$c_{66}^{E}$</td>
<td>GPa</td>
<td>$0.4×10^{-3}$</td>
<td>31</td>
</tr>
<tr>
<td>$e_{31}$</td>
<td>C m$^{-2}$</td>
<td>0</td>
<td>$-5.2$</td>
</tr>
<tr>
<td>$e_{32}$</td>
<td>C m$^{-2}$</td>
<td>0</td>
<td>$-5.2$</td>
</tr>
<tr>
<td>$e_{33}$</td>
<td>C m$^{-2}$</td>
<td>0</td>
<td>15.1</td>
</tr>
<tr>
<td>$e_{24}$</td>
<td>C m$^{-2}$</td>
<td>0</td>
<td>12.7</td>
</tr>
<tr>
<td>$e_{15}$</td>
<td>C m$^{-2}$</td>
<td>0</td>
<td>12.7</td>
</tr>
<tr>
<td>$\varepsilon_{11}^{s}/\varepsilon_{0}^{a}$</td>
<td>—</td>
<td>3.15</td>
<td>763</td>
</tr>
<tr>
<td>$\varepsilon_{22}^{s}/\varepsilon_{0}^{a}$</td>
<td>—</td>
<td>3.15</td>
<td>763</td>
</tr>
<tr>
<td>$\varepsilon_{33}^{s}/\varepsilon_{0}^{a}$</td>
<td>—</td>
<td>3.15</td>
<td>658</td>
</tr>
</tbody>
</table>

$^{a}$ The permittivity of free space
$\varepsilon_{0}=8.854×10^{-12}$ F m$^{-1}$.

![](./images/811681657659588611_4.jpg)

Figure 3. Test setup of a piezoelectric composite beam with a fiber optic sensor.

## 5. Results and discussion
Utilizing the integrated system model, analytical and numerical techniques are performed to analyze the system behavior. In this section, the proposed formal asymptotic method is first applied to a piezoelectric beam and the results are compared to those of the three-dimensional finite element analysis. It is then applied to a piezoelectric fiber composite cantilever beam. Results from the proposed approach are compared to those obtained by the experimental investigation and the classical rule of mixture approach based on the strength of materials [4]. The piezoelectric and matrix material properties used in this study are listed in table 1.

In all figures reported herein, the zeroth, first, and second order solutions to the given problem are represented by the mechanical displacement vector and the electric potential such that

$$
\begin{aligned}
\mathbf{u}_{\text{beam}}^{(k)}\left(x_{i}\right) & \equiv \mathbf{u}^{(0)}\left(x_{1}\right) \\
& +\sum_{n=0}^{k}\left[\Theta\left(x_{a}\right) \hat{\mathbf{v}}^{(n+1)}\left(x_{1}\right)+\mathbf{N}_{u} \mathbf{U}_{\mathrm{w}}^{(n+2)}\left(x_{i}\right)\right], \\
\varphi_{\text{beam}}^{(k)}\left(x_{i}\right) & \equiv \sum_{n=0}^{k}\left[\hat{\varphi}^{(n+1)}\left(x_{1}\right)+\mathbf{N}_{\varphi} \Phi_{\mathrm{w}}^{(n+2)}\left(x_{i}\right)\right],
\end{aligned}
\tag{64}
$$

where $k$ ($\geqslant 0$) represents the $k$th order solutions. These solutions are referred to as ABA-0th, ABA-1st and ABA-2nd, where ABA stands for asymptotic beam analysis, respectively,

Note that the effects of electromechanical coupling are included in the warping solutions $\mathbf{U}_{\mathrm{w}}^{(n+2)}$ and $\Phi_{\mathrm{w}}^{(n+2)}$. The zeroth order solutions correspond to the classical Euler–Bernoulli–Navier beam theory, and first order and/or second order solutions are comparable to the Rankine–Timoshenko beam theory. In what follows, it will be demonstrated that the boundary conditions given in equations (56), (58), (59) and (63) are simple enough for engineering applications and accurate enough for high precision analyses, as long as the interior solutions are desired.

### 5.1. Analysis of piezoelectric beams
A study is first carried out to assess the accuracy of the proposed method by comparing it with a three-dimensional finite element analysis, on analyzing a bimorph pure piezoelectric cantilever beam illustrated in figure 4. The length-to-thickness ratio ($S \equiv h/l$) of the beam is 4, and the beam dimension is assumed to be $10\ \text{mm} \times 10\ \text{mm} \times 40\ \text{mm}$. The degrees of freedom are about 10 000 and 250 for the three-dimensional finite element analysis and the present analysis, respectively. 100 V on both the bottom and top surfaces is applied to the beam. The mid surface of the beam is grounded, so that the applied electric potential causes a bending deformation. In order to get a good displacement reading, the fiber optic sensor is located at 85% of the beam length at the midpoint of the beam width. The sensor measures the vertical displacement of the beam and the experimental measurements are compared with the analytically predicted displacements. The proposed approach with the zeroth order solution is compared to the three- dimensional finite element analysis where eight-noded brick elements with incompatible modes [22] are used. The three- dimensional mesh configuration is shown in figure 4(b). The normalized centroid deflections of the piezoelectric beam along the normalized axial coordinate are shown in figure 5, where the zeroth order solution (ABA-0th) is compared to the three-dimensional FEM solution and the zeroth order solution without the cross-sectional deformation (ABA-0th*). It is seen that the proposed approach shows excellent agreement with the three-dimensional FEM analysis, including at locations near the clamped end of the beam ($x_1/h \geqslant 1$) where the three-dimensional edge effect starts to decay. It is of interest to see that the zeroth order solution is able to capture the asymmetric cross-sectional deformation due to the electric fields (i.e., tension on bottom and compression on top), as

![](./images/811681657659588611_5.jpg)

Figure 4. A piezoelectric cantilever beam; (a) beam configuration and (b) 3D mesh configuration.

![](./images/811681657659588611_6.jpg)

Figure 5. Comparison of deflections along the axial coordinate; –: ABA-0th*, –: ABA-0th, •: 3D FEM.

![](./images/811681657659588611_7.jpg)

Figure 6. Comparison of cross-sectional deformation; $\cdots$: undeformed mesh, —: ABA-0th, •: 3D FEM.

illustrated in figure 6, in which the centroid displacements are set to zero in order to compare the cross-sectional deformation at the mid-span. With the aid of this capability, the fundamental beam solution, which is the zeroth order solution without the warping function, is improved by accurately predicting the cross-sectional deformation (see figure 5), so that the three- dimensional exact interior solution (away from the clamped boundary) can be recovered. The present model does satisfy the clamped boundary condition in the asymptotic sense (i.e., average sense) such that

$$
\mathbf{u}_{\text{beam}}(0, \mathbf{0}) \neq 0 \text{ but } \int_{S} \mathbf{u}_{\text{beam}}(0, x_{\alpha}) \mathrm{d} S=0, \tag{65}
$$

which is asymptotically correct up to $\mathcal{O}(\epsilon^{2})$. This accounts for the difference between the zeroth order solutions with and without cross-sectional deformation as shown in figure 5.

In figure 7, the electric potential distributions through the thickness of a piezoelectric beam are plotted at $x_{2}=0$ and $x_{1}=l / 2$ for the length-to-thickness ratio of 10 (i.e., $S=10$); (a) under the tip shear force of 1 N with grounded bottom surface and (b) under electric loads (100 V on top and bottom surfaces, 0 V on the mid-plane). As demonstrated in figure 7, the results from the present analysis are well correlated with those of the three-dimensional FEM analysis once again. As far as the electric potential is concerned, the electromechanical coupling behavior is important when a piezoelectric beam is used as the sensor, which mainly comes from $\Xi_{\mathrm{e}}^{(1)}$ given in equations (35), as shown in figure 7(a). Such coupling behavior is not significant when the beam is used as an actuator. This is illustrated in figure 7(b), where the electric potential distributions are governed by the prescribed electric potential, $\Xi_{\mathrm{p}}^{(1)}$ presented in equations (35). As shown in figure 7(b), the three-dimensional electric potential can be accurately predicted by considering the electromechanical coupling behavior.

In order to investigate the asymptotic behavior of the proposed approach, tip deflections of a piezoelectric beam are presented in figure 8. The tip deflection is normalized by multiplying by $-10^{11} / S^{3}$ for mechanical loads (tip shear force of 1 N) and $-10^{8} / S^{2}$ for electric loads (100 V are applied on top and bottom surfaces and mid-plane is grounded), so that the zeroth order solution becomes constant with respect to the length-to-thickness ratio $S$. It is of interest to see that the normalized tip deflections tend to decrease with $S$ under mechanical loads, whereas they tend to increase with $S$ when electric load is applied. In figure 8(a), tip deflections in the range of $S \leqslant 10$ suggest that the transverse shear deformation is significant, whereas, in figure 8(b), they indicate that the cross-sectional in-plane deformation due to the prescribed electric potential is dominant. For the case of electric loads, the second order solution is the same as the zeroth order solution since the transverse shear deformation is not significant at all. Results of the present approach shows excellent agreement with those of the three-dimensional FEM, even for short piezoelectric beams $(S \leqslant 4)$ via the asymptotically correct boundary conditions up to $\mathcal{O}(\epsilon^{2})$ presented in equation (61).

### 5.2. Analysis of piezoelectric fiber composite beams
A piezoelectric fiber composite made of PZT-4 and silicone polymer is shown in figure 9, where the beam has four piezoelectric fibers. The dimension of the beam is 4.35 mm (depth) $\times$ 4.14 mm (width) $\times$ 47 mm (length), and the dimension of a single piezoelectric fiber is $1 \mathrm{~mm} \times 1 \mathrm{~mm} \times$ 47 mm, which is located at the center of each quadrant. A 100 V input is applied to the two top located fibers, whereas $-100 \mathrm{~V}$ is applied to the two bottom fibers, so that a large bending deformation can be generated. Figure 10 shows the deformed configuration of the piezoelectric fiber composite beam, where the dotted line represents the centroid deformed configuration and a dotted line mesh indicates the deformed cross-section at the $85\%$ axial location. In fact, it is possible to calculate the cross-sectional deformation at any axial location,

![](./images/811681657659588611_8.jpg)

Figure 7. Comparison of electric potential distributions; (a) under mechanical loads and (b) under electric loads; —: ABA-0th, ●: 3D FEM,--: prescribed potential.

![](./images/811681657659588611_9.jpg)

Figure 8. Tip deflections of a piezoelectric beam with varying length-to-thickness ratio; (a) under mechanical loads and (b) under electric loads; –: ABA $-0$th$^*$, ---: ABA-2nd, ●: 3DFEM.

![](./images/811681657659588611_10.jpg)

Figure 9. Configuration of a piezoelectric fiber composite beam.

so that the present analysis is capable of providing the three- dimensional distribution of displacements and stresses. In this specific electric loading case, the predicted tip deflection is $11.7\ \mu$m.

In figure 11, the first order cross-sectional mechanical deformation mode of a piezoelectric composite beam considered herein is illustrated, which corresponds to $\Gamma_{\mathrm{e}}^{(1)}$ given in equations (35). One can see the 3D Poisson effects for the extension and bending modes (which are usually neglected in classical beam theories) and the Saint-Venant torsional warping. These cross-sectional deformation modes are slightly different from those of the beam made of isotropic materials due to the presence of the piezoelectric fibers, especially for a torsion mode. In addition to these classical mechanical deformation modes induced by the mechanical strain, there

![](./images/811681657659588611_11.jpg)

Figure 10. 3D deformed mesh configuration of the beam.

is another mechanical deformation mode, $\Gamma_{\mathrm{p}}^{(1)}$ presented in figure 12(a), due to the prescribed electric potential, $\Xi_{\mathrm{p}}^{(1)}$ illustrated in figure 12(b). The tension and the compression are clearly seen for top and bottom located piezoelectric fibers, respectively. In actuation, this mode $\Gamma_{\mathrm{p}}^{(1)}$ plays an important

Extension
![](./images/811681657659588611_12.jpg)

Bending 2
![](./images/811681657659588611_13.jpg)

Bending 3
![](./images/811681657659588611_14.jpg)

Torsion
![](./images/811681657659588611_15.jpg)

Figure 11. The first cross-sectional mechanical deformation of the beam, $\Gamma_{\mathrm{e}}^{(1)}$; $\cdot\cdot\cdot$: undeformed mesh, —: deformation mode.

(a)
![](./images/811681657659588611_16.jpg)

(b)
![](./images/811681657659588611_17.jpg)

Figure 12. The first cross-sectional modes induced by the prescribed potential; $\cdot\cdot\cdot$: undeformed mesh; (a) $\Gamma_{\mathrm{p}}^{(1)}$, —: deformation mode, and (b) $\Xi_{\mathrm{p}}^{(1)}$, —: electric potential.

role as compared to $\Gamma_{\mathrm{e}}^{(1)}$, if there are no mechanical loads applied to the beam. From the first electric warping matrix $\Xi_{\mathrm{e}}^{(1)}$, one can see the electric potential distribution due to the mechanical loads on the cross-section. Each column of $\Xi_{\mathrm{e}}^{(1)}$ matrix is depicted in figure 13, where the bending-3 mode is dominant. This is different from the cross-sectional mechanical mode, since the piezoelectric fibers are assumed to be poled along the thickness direction. The electric potential is therefore large when the beam undergoes bending with respect to the $x_{3}$-axis, since the piezoelectric constant $d_{31}$ is a major factor in this kind of behavior. It is of interest to see that the electric potential due to torsion is very close to zero. In other words, the current configuration may not be useful as torsion sensors. The non-classical cross-sectional mechanical deformation modes can be found in one of the second order warping functions $\Gamma_{\mathrm{e}}^{(2)}$, as shown in figure 14. One can clearly see that shear deformation effects in two bending modes, in-plane cross-sectional distortion in a torsion mode, and the characteristic behavior of piezoelectric fibers embedded into soft silicone matrix. These analysis results demonstrate that the proposed approach has the capability to provide in-depth understanding of the behavior of a three- dimensional piezoelectric composite beam.

### 5.3. Experimental results and comparison
Test results reported herein are based on a piezoelectric fiber composite beam whose dimension is the same as that given in section 5.2. The experimental results are compared to those obtained by the classical rule of mixture approach based on strength of materials [4] as well as those predicted by the proposed approach. The classical rule of mixture approach is based on the micromechanical analysis of a representative volume, where the effective piezoelectric constants are obtained from three-dimensional piezoelectric

![](./images/811681657659588611_18.jpg)

Figure 13. The first cross-sectional electric potential due to the mechanical strain, $\Xi_{\mathrm{e}}^{(1)}$; $\cdots$: undeformed mesh, —: electric potential.

![](./images/811681657659588611_19.jpg)

Figure 14. The second cross-sectional mechanical deformation of the beam, $\Gamma_{\mathrm{e}}^{(2)}$; $\cdots$: undeformed mesh, —: deformation mode.

material properties via the rule of mixture. First, a static test is performed to determine the voltage/displacement ratio. For a static case, the voltage is incremented by steps of 25 V approximately every 3 s, as shown in figure 15(a). For each increment, the beam is allowed to reach a static condition. Figure 15(b) shows the hysteresis loop for the beam. At 150 V, a deflection of 17 $\mu$m is achieved at the 85% axial location. Comparison between experiment and analysis is shown in table 2, where the experimental result represents the averaged value of quantities shown in figure 15(b). It is shown that the results from the formal asymptotic method correlate well with the experimental data, whereas the classical rule of mixture approach produces more than 30% error. This clearly indicates that the classical rule of mixture approach is not adequate for the precision analysis of such a piezoelectric composite beam and the proposed new method is needed.

The dynamic (quasi-static) response of the beam is measured with an input of 5 Hz, $\pm 60$ V sine wave. First the

![](./images/811681657659588611_20.jpg)

Figure 15. Static response of the beam; (a) time history and (b) hysteresis loop.

<table>
<caption>Table 2. Comparison of static beam displacements ($\mu$m).</caption>
<thead>
<tr>
<th>Voltage (V)</th>
<th>ABA-0th</th>
<th>Rule of mixture</th>
<th>Experiment¹</th>
</tr>
</thead>
<tbody>
<tr>
<td>50</td>
<td>5.8</td>
<td>3.68</td>
<td>5.5</td>
</tr>
<tr>
<td>100</td>
<td>11.7</td>
<td>7.36</td>
<td>11.5</td>
</tr>
<tr>
<td>150</td>
<td>17.5</td>
<td>11.0</td>
<td>17</td>
</tr>
</tbody>
</table>

¹ Indicates the averaged value of data presented in figure 15(b).

<table>
<caption>Table 3. Comparison of quasi-static beam displacements with 60 V excitation at 5 Hz ($\mu$m).</caption>
<thead>
<tr>
<th>The number of PZTs</th>
<th>ABA-0th</th>
<th>Experiment</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single PZT</td>
<td>1.9</td>
<td>1.25–2¹</td>
</tr>
<tr>
<td>Bottom PZTs</td>
<td>3.85</td>
<td>3</td>
</tr>
<tr>
<td>All PZTs</td>
<td>7</td>
<td>6</td>
</tr>
</tbody>
</table>

¹ Indicates the range of responses using four different actuators.

![](./images/811681657659588611_21.jpg)

Figure 16. Quasi-static responses of the beam with different actuation scenario; —: single PZT, – –: bottom PZTs,--- all PZTs.

responses are obtained when this voltage is applied to each PZT individually. The results show that the effects from each individual PZT are similar. Next the responses are investigated when the voltages are applied to different combinations of PZT fibers: A single PZT, only the bottom two PZTs, and all PZTs (with top and bottom PZTs out of phase to increase deflection), as shown in figure 16. As more PZTs are used, the deflection increases as expected. In table 3, numerical results from the present analysis are compared to those obtained from the experiment. For a single PZT case, the experimental results vary from 1.25 to 2 $\mu$m, depending on the location of the actuated piezoelectric fiber. Good correlations between the numerical and test results are observed for the various cases, as shown in table 3.

## 6. Concluding remarks

An asymptotic approach is developed to model piezoelectric fiber-based composite beams by systematically separating two-dimensional microscopic and one-dimensional macroscopic problems from the three-dimensional electromechanical problem. Asymptotically correct boundary conditions are obtained by applying the generalized orthogonality conditions of asymptotic displacements to six fundamental solutions as constraints. This approach can be utilized to analyze piezoelectric fiber composite beams having arbitrary cross-sections, beyond the classical approximation or the zeroth order solution, with asymptotically correct boundary conditions.

The approach is first compared with a three-dimensional finite element analysis on a pure piezoelectric beam specimen, showing that is accurate and yet more efficient. A piezoelectric fiber/polymer composite beam specimen is fabricated and tested to validate the analytical predictions. The experimental results are compared to those obtained by the proposed approach and the classical rule of mixture method. It is shown that the classical rule of mixture approach yields more than 30% error, whereas results from the new approach are well correlated with the experimental data. Throughout the analysis and experiment, it is demonstrated that the present asymptotic analysis has the capability of providing in-depth understanding and characterization of the piezoelectric fiber composite beams.

### Acknowledgment

The authors acknowledge the support for this research work from the Taiwan Textile Research Institute.

### References

[1] Waller D J, Safari A, Card R J and O'Toole M P 1990 Lead zirconate titanate fiber/polymer composites prepared by a replication process *J. Am. Ceram. Soc.* **73** 3503–6

[2] Carpi F and De Rossi D 2005 Electroactive polymer-based devices for e-textiles in biomedicine *IEEE Trans. Inform. Technol. Biomed.* **9** 295–318

[3] Dunn M L and Taya M 1993 Micromechanics predictions of the effective electroelastic moduli of piezoelectric composites *Int. J. Solids Struct.* **30** 161–75

[4] Mallik N and Ray M C 2003 Effective coefficients of piezoelectric fiber-reinforced composites *AIAA J.* **41** 704–10

[5] Berger H, Kari S, Gabbert U, Rodriguez-Ramos R, Bravo-Castillero J, Guinovart-Diaz R, Sabina F J and Maugin G A 2006 Unit cell models of piezoelectric fiber composites for numerical and analytical calculation of effective properties *Smart Mater. Struct.* **15** 451–8

[6] Palacios R and Cesnik C E S 2005 Cross-sectional analysis of nonhomogeneous anisotropic active slender structures *AIAA J.* **43** 2624–38

[7] Roy S, Yu W and Han D 2007 An asymptotically correct classical model for smart beams *Int. J. Solids Struct.* **44** 8424–39

[8] Gregory R D and Wan F Y M 1984 Decaying states of plane strain in a semi-infinite strip and boundary conditions for plate theory *J. Elast.* **14** 27–64

[9] Buannic N and Cartraud P 2001 Higher-order effective modeling of periodic heterogeneous beams II. Derivation of the proper boundary conditions for the interior asymptotic solution *Int. J. Solids Struct.* **38** 7168–80

[10] Berdichevsky V L 1981 On the energy of an ealstic rod *J. Appl. Math. Mech. (PMM)* **45** 518–29

[11] Trabucho L and Viãno J M 1996 Mathematical modelling of rods *Handbook of Numerical Analysis* vol IV ed P G Ciarlet and J L Lions (Amsterdam: North-Holland) pp 487–969

[12] Narra-Figueiredo I M and Franco-Leal C M 2006 A generalized piezoelectric Bernoulli–Navier anisotropic rod model *J. Elast.* **85** 85–106

[13] Kim J-S, Cho M and Smith E C 2008 An asymptotic analysis of composite beams with kinematically corrected end effects *Int. J. Solids Struct.* **45** 1954–77

[14] Kim J-S 2009 An asymptotic analysis of anisotropic heterogeneous plates with consideration of end effects *J. Mech. Mater. Struct.* **4** 1535–53

[15] Kim J-S and Wang K W 2010 Vibration analysis of composite beams with end effects via the formal asymptotic method *J. Vib. Acoust.* **132** 041003

[16] Buannic N and Cartraud P 2001 Higher-order effective modeling of periodic heterogeneous beams I. Asymptotic expansion method *Int. J. Solids Struct.* **38** 7139–61

[17] Standards Committee of the IEEE Ulatrasonics, Ferroelectrics, and Frequency Control Society 1987 *An American National Standard: IEEE Standards on Piezoelectricity* (New York: The Institute of Electrical and Electronics Engineers) ANSI/IEEE Std 176-1987

[18] Cesnik C E S, Sutyrin V G and Hodges D H 1996 Refined theory of composite beams: The role of short-wavelength extrapolation *Int. J. Solids Struct.* **33** 1387–408

[19] Fan H and Widera G E O 1994 On the use of variational principles to derive beam boundary conditions *J. Appl. Mech.* **61** 470–1

[20] Horgan C O and Simmonds J G 1991 Asymptotic analysis of an end-loaded transversely isotropic, elastic, semi-infinite strip weak in shear *Int. J. Solids Struct.* **27** 1895–914

[21] Simeon B 2006 On Lagrange multipliers in flexible multibody dynamics *Comput. Methods Appl. Mech. Eng.* **195** 6993–7005

[22] Yeo S T and Lee B C 1997 New stress assumption for hybrid stress elements and refined four-noded plane and eight-noded brick elements *Int. J. Numer. Methods Eng.* **40** 2933–52