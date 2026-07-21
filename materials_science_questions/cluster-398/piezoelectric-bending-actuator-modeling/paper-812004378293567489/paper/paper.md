![](./images/812004378293567489_1.jpg)

Available online at www.sciencedirect.com

![](./images/812004378293567489_2.jpg)

Computers and Structures 85 (2007) 1453-1460

# Computers & Structures
www.elsevier.com/locate/compstruc

# Finite element modeling of electrochemical-poroelastic behaviors of conducting polymers

## Yutaka Toi *, Woo-Sang Jung

Institute of Industrial Science, University of Tokyo, 4-6-1 Komaba, Meguro-ku, Tokyo 153-8505, Japan

Received 13 September 2006; accepted 5 February 2007
Available online 27 March 2007

## Abstract

A computational modeling is established for the electrochemical-poroelastic behavior of conducting polymers such as polypyrrole. The three-dimensional continuum modeling given by Della Santa et al. for the passive, poroelastic behavior of conducting polymers is extended to the formulation for the active, electrochemical-poroelastic formulation according to Onsager-like laws, which is combined with the one-dimensional equation for ionic transportation. The validity of the finite element formulation for these governing equations has been demonstrated by numerical studies for the passive and active responses of polypyrrole membranes.

© 2007 Elsevier Ltd. All rights reserved.

Keywords: Computational mechanics; High polymer materials; Structural analysis; Biomaterials; Electrochemistry; Poroelasticity; Finite element method; Stress relaxation

## 1. Introduction

Actuators using conducting polymers such as polypyr- role have the following advantages: (i) generation of large forces (several 10 times as large as human muscles), (ii) simple structures and light weight, (iii) noiseless, (iv) operation by low voltage (1–2 V). The development, application and production of such actuators are expected in the fields of robotics, biomedical engineering and micro-electro-mechanical systems [1–5].

The deformation of expansion and contraction of a con- ducting polymer membrane in an electrolyte bath takes place, due to the coming in and out of electrolyte caused by the pressure difference between the inside and outside of the membrane. This is a passive, poroelastic behavior [1–3]. When turning on electricity between a conducting polymer membrane and electrolyte, the deformation of expansion and contraction of the conducting polymer membrane is accelerated by the insertion and de-insertion of ions, which is an active, electrochemical-poroelastic behavior [1–3]. The polypyrrole doped with relatively small anions such as $ClO_{4}^{-}$ expand and contract due to the insertion and de-insertion of the anions (oxidation and reduction), which is classified as anion-driven actuators [4,5]. On the other hand, anions do not move in the polypyrrole doped with relatively large anions such as DBS (Docecyl Benzene Sulfonate), which expands and contracts due to the insertion and de-insertion of cations (reduction and oxidation). It is classified as cation-driven actuators [4,5].

Della Santa et al. [1–3] derived governing equations of continuum modeling based on poroelasticity theory for the response of conducting polymer actuators using polypyrrole. They compared one-dimensional theoretical solutions for the passive, poroelastic behavior with the experimental results, however, details of the formulation for the active, electrochemical-poroelastic behavior was not given. On the other hand, Tadokoro derived governing equations for the electrochemical-mechanical behaviors of ionic-conducting polymer–metal composites (IPMCs) such as Nafion membrane with platinum electrodes accompanied by the ionic movement under an electric field, the

* Corresponding author. Tel.: +81 3 5452 6178; fax: +81 3 5452 6180.
E-mail address: toi@iis.u-tokyo.ac.jp (Y. Toi).

0045-7949/$ - see front matter © 2007 Elsevier Ltd. All rights reserved.
doi:10.1016/j.compstruc.2007.02.014

### Nomenclature

| Symbol | Definition | Symbol | Definition |
|--------|------------|--------|------------|
| $[B]$ | strain-nodal displacement matrix for solid | $T$ | absolute temperature |
| $c(x,t)$ | electric charge density | $V_{\mathrm{e}}$ | finite element region |
| $\{c_{\mathrm{N}}\}$ | nodal charge density vector | $V^{\mathrm{f}}$ | mass flux |
| $d$ | location of electrode in electrolyte | $x_j$ | Cartesian coordinates |
| $[D^{\mathrm{s}}]$ | stress–strain matrix for solid | $\beta$ | porosity |
| $E$ | Young’s modulus | $\Delta$ | increment |
| $e$ | elemental charge | $\Delta P$ | pressure increment |
| $e^{\mathrm{f}}$ | volumetric strain in fluid | $\{\Delta P_{\mathrm{N}}\}$ | nodal pressure increment vector |
| $e^{\mathrm{s}}$ | volumetric strain in solid | $\Delta t$ | time increment |
| $f$ | frictional coefficient between solid and fluid | $\{\Delta u\}$ | displacement increment vector |
| $[H]$ | coefficient matrix | $\{\Delta u_{\mathrm{N}}\}$ | nodal displacement increment vector |
| $h$ | element length | $\{\Delta \sigma^{\mathrm{f}}\}$ | fluid stress increment vector |
| $i$ | electric current | $\{\Delta \sigma^{\mathrm{s}}\}$ | solid stress increment vector |
| $J$ | ionic flux | $\delta$ | variation |
| $k$ | Boltzman constant | $\delta_{ij}$ | Kronecker’s delta |
| $[K]$ | incremental element stiffness matrix | $\{\varepsilon\}$ | total strain vector |
| $[N_u], [N]$ | shape function matrices of eight-noded hexahedron element | $\varepsilon_{\mathrm{e}}$ | dielectric constant of electrolyte |
| $N_{\mathrm{a}}$ | Avogadro number | $\varepsilon_{ij}^{\mathrm{s}}$ | strain in solid |
| $P$ | pressure | $\eta_1$ | coefficient of viscosity for moving ions |
| $\nabla P$ | pressure gradient | $v$ | Poisson’s ratio |
| $\{Q_{\mathrm{N}}\}$ | nodal total charge vector | $\nabla \varphi$ | electric potential gradient |
| $Q_i, Q_j$ | nodal total charge | $\sigma_{ij}^{\mathrm{f}}$ | stress in fluid |
| $Q(x,t)$ | total electric charge | $\sigma_{ij}^{\mathrm{s}}$ | stress in solid |
| $S_x$ | cross-section area | $\sigma_{ij}^{\mathrm{t}}$ | total stress |
| | | $\{\sigma^{\mathrm{t}}\}$ | total stress vector |

mechanism for expansion and contraction of which differs from that of conducting polymers such as polypyrrole. The finite element modeling for the electrochemical–mechanical behavior of ionic-conducting polymer–metal composites was given by Toi and Kang [7,8].

The purpose of the present study is to establish computational modeling for the electrochemical-poroelastic behavior of conducting polymers to support design and development of the actuators using conducting polymers such as polypyrrole. The three-dimensional continuum modeling given by Della Santa et al. [1–3] based on Biot’s poroelasticity theory [9] is extended to the formulation for the active, electrochemical-poroelastic behavior according to Onsager’s law [10], which is combined with the one-dimensional ionic transportation equation given by Tadokoro et al. [6] to construct the system of governing equations. The governing equations are discretized by the finite element method [11]. Numerical calculations are conducted for the passive, poroelastic behavior and the active, electrochemical-poroelastic behavior, the results of which are respectively compared with the theoretical solution [1] and the experimental results [2] to illustrate the validity of the present modeling.

The finite element modeling for the electrochemical-poroelastic behavior of conducting polymer membranes and the computational results for polypyrrole membranes are described in Sections 2 and 3, respectively. Section 4 contains concluding remarks.

## 2. Finite element formulation of governing equations for electrochemical-poroelastic behaviors of conducting polymers

### 2.1. Stiffness equations for poroelastic solid

According to Biot’s theory [9], the equilibrium equation of poroelastic solids containing fluid is given as follows:
$$
\frac{\partial \sigma_{ij}^{\mathrm{t}}}{\partial x_j}=0 \tag{1}
$$
where
$$
\sigma_{ij}^{\mathrm{t}}=\sigma_{ij}^{\mathrm{s}}+\sigma_{ij}^{\mathrm{f}}\left(=\sigma_{ij}^{\prime}-P \delta_{ij}\right) \tag{2a}
$$

$$
\sigma_{ij}^{\mathrm{s}}=\sigma_{ij}^{\prime}-(1-\beta) P \delta_{ij}=\frac{E}{1+v} \varepsilon_{ij}^{\mathrm{s}}+\frac{v E}{(1+v)(1-2 v)} e^{\mathrm{s}} \delta_{ij} \tag{2b}
$$

$$
\sigma_{ij}^{\mathrm{f}}=-\beta P \delta_{ij} \tag{2c}
$$
in which the following notations are used: $\sigma_{ij}^{\mathrm{t}}$, total stress; $\sigma_{ij}^{\mathrm{s}}$, partial (average) stress of the solid phase; $\sigma_{ij}^{\prime}$, effective stress; $\sigma_{ij}^{\mathrm{f}}$, partial (average) stress of the liquid phase; $x_j$,

Cartesian coordinates; $E$, Young's modulus; $v$, Poisson's ratio; $\varepsilon_{ij}^{\mathrm{s}}$, strain of the solid phase; $e^{\mathrm{s}}$, volumetric strain of the solid phase; $\delta_{ij}$, Kronecker's delta; $\beta$, porosity; $P$, pressure. It is noted that the coefficients $E$ and $v$ in Eq. (2b) have a substantial difference from those of a conventional elastic system: they are variable with the porosity $\beta$ [1].

Neglecting external force components, the virtual work principle equivalent to Eq. (1) is expressed by the following equation:
$$
\int_{V_{\mathrm{e}}} \delta(\{\varepsilon\}^{\mathrm{T}}+\{\Delta \varepsilon\}^{\mathrm{T}})(\{\sigma^{\mathrm{t}}\}+\{\Delta \sigma^{\mathrm{t}}\}) \mathrm{d} V=0
\tag{3}
$$
where $\{\varepsilon\}$ is the total strain vector, $\{\sigma^{\mathrm{t}}\}$ the total stress vector, $\delta$ the variation, $\Delta$ an increment and $V_{\mathrm{e}}$ is the finite element region. Using Eq. (2a), Eq. (3) can be rewritten as
$$
\int_{V_{\mathrm{e}}} \delta\{\Delta \varepsilon\}^{\mathrm{T}}\{\Delta \sigma^{\mathrm{s}}\} \mathrm{d} V=-\int_{V_{\mathrm{e}}} \delta\{\Delta \varepsilon\}^{\mathrm{T}}\{\Delta \sigma^{\mathrm{f}}\} \mathrm{d} V
\tag{4}
$$

The displacement increment $\{\Delta u\}$ and the pressure increment $\Delta P$ in each element are assumed as follows:
$$
\{\Delta u\}=\left[N_{u}\right]\{\Delta u_{\mathrm{N}}\}
\tag{5a}
$$
$$
\Delta P=[N]\{\Delta P_{\mathrm{N}}\}
\tag{5b}
$$
where $[N_{u}]$ and $[N]$ are the shape function matrices of eightnode hexahedron elements. $\{\Delta u_{\mathrm{N}}\}$ and $\{\Delta P_{\mathrm{N}}\}$ are the nodal displacement increment vector and the nodal pressure increment vector, respectively. Using Eqs. (2b) and (2c), the solid stress increment vector $\{\Delta \sigma^{\mathrm{s}}\}$ and the fluid stress increment vector $\{\Delta \sigma^{\mathrm{f}}\}$ are respectively expressed by the following equations:
$$
\{\Delta \sigma^{\mathrm{s}}\}=\left[D^{\mathrm{s}}\right]\{\Delta \varepsilon\}=\left[D^{\mathrm{s}}\right][B]\{\Delta u_{\mathrm{N}}\}
\tag{6a}
$$
$$
\{\Delta \sigma^{\mathrm{f}}\}=-\beta[H] \Delta P
\tag{6b}
$$
where $[B]$ is the strain-nodal displacement matrix for solid, $[D^{\mathrm{s}}]$ the stress-strain matrix for solid and $[H]$ is the coefficient matrix determined by Eq. (2c).

Substituting Eqs. (6a) and (6b) into Eq. (4), the following three-dimensional element stiffness equation for poroelastic solids can be obtained:
$$
[K]\{\Delta u_{\mathrm{N}}\}=\beta\left[B^{*}\right]\{\Delta P_{\mathrm{N}}\}
\tag{7}
$$
where
$$
[K]=\int_{V_{\mathrm{e}}}[B]^{\mathrm{T}}\left[D^{\mathrm{s}}\right][B] \mathrm{d} V
\tag{8a}
$$
$$
\left[B^{*}\right]=\int_{V_{\mathrm{e}}}[B]^{\mathrm{T}}[H][N] \mathrm{d} V.
\tag{8b}
$$

### 2.2. Poisson's equation for pressure

According to Onsager's law [10], the relations among the ionic flux $J$, the mass flux $V^{\mathrm{f}}$, the electric potential gradient $\nabla \varphi$ and the pressure gradient $\nabla P$ can be expressed as follows:
$$
J=K_{11} \nabla \varphi+K_{12} \nabla P
\tag{9a}
$$
$$
V^{\mathrm{f}}=K_{21} \nabla \varphi+K_{22} \nabla P
\tag{9b}
$$

Calculating divergence of both hand sides of Eqs. (9a) and (9b) and eliminating $\nabla^{2} \varphi$, the following equation is used:
$$
\operatorname{div} V^{\mathrm{f}}=\frac{\partial e^{\mathrm{f}}}{\partial t}
\tag{10}
$$

Then, using the relation concerning the passive, poroelastic behavior [1]:
$$
\frac{\partial e^{\mathrm{f}}}{\partial t}=-\frac{(1-\beta)}{f} \nabla^{2} P
\tag{11}
$$
and Biot's equation of continuity [9]:
$$
\frac{\partial e^{\mathrm{s}}}{\partial t}=-\frac{\beta}{1-\beta} \frac{\partial e^{\mathrm{f}}}{\partial t}
\tag{12}
$$
the following Poisson's equation for pressure in the case of electrochemical response can be derived:
$$
\frac{\partial e^{\mathrm{s}}}{\partial t}=C_{1} \frac{-\beta}{(1-\beta)} \nabla J+C_{2} \frac{\beta}{f} \nabla^{2} P
\tag{13}
$$
where $f$ is a coefficient representing permeability of fluid in porous solids, which is called frictional coefficient between solid and fluid [1].

In each finite element, the volumetric strain rate of solid and the electric density rate are assumed as follows:
$$
\frac{\partial e^{\mathrm{s}}}{\partial t}=[N]\left\{\dot{e}_{\mathrm{N}}^{\mathrm{s}}\right\}
\tag{14a}
$$
$$
\nabla J=-\frac{\partial c}{\partial t}=-[N]\left\{\dot{c}_{\mathrm{N}}\right\}
\tag{14b}
$$

The basic equation for Galerkin finite element formulation of Eq. (13) is expressed by the following equation:
$$
\int_{V_{\mathrm{e}}}[N]^{\mathrm{T}}\left(\frac{\partial e^{\mathrm{s}}}{\partial t}+C_{1} \frac{\beta}{(1-\beta)} \nabla J-C_{2} \frac{\beta}{f} \nabla^{2} P\right) \mathrm{d} V=0
\tag{15}
$$

Substituting Eqs. (14a) and (14b) into Eq. (15), the following equation can be obtained:
$$
\begin{aligned}
& \int_{V_{\mathrm{e}}}[N]^{\mathrm{T}}[N]\left\{\dot{e}_{\mathrm{N}}^{\mathrm{s}}\right\} \mathrm{d} V \\
& \quad=-C_{1} \frac{\beta}{(1-\beta)} \int_{V_{\mathrm{e}}}[N]^{\mathrm{T}}[N]\left\{\dot{c}_{\mathrm{N}}\right\} \\
& \quad \quad-C_{2} \frac{\beta}{f} \int_{V_{\mathrm{e}}}\left(\frac{\partial[N]^{\mathrm{T}}}{\partial x} \frac{\partial[N]}{\partial x}+\frac{\partial[N]^{\mathrm{T}}}{\partial y} \frac{\partial[N]}{\partial y}+\frac{\partial[N]^{\mathrm{T}}}{\partial z} \frac{\partial[N]}{\partial z}\right)\left\{P_{\mathrm{N}}\right\} \mathrm{d} V
\end{aligned}
\tag{16}
$$

From Eq. (16), the following equation for pressure can be obtained:
$$
[S]\left\{\dot{e}_{\mathrm{N}}^{\mathrm{s}}\right\}=C_{1} \frac{\beta}{(1-\beta)}[S]\left\{\dot{c}_{\mathrm{N}}\right\}-C_{2} \frac{\beta}{f}[A]\left\{P_{\mathrm{N}}\right\}.
\tag{17}
$$

### 2.3. Evolution equation of volume strain rate

Substituting Eqs. (2a)-(2c) into Eq. (1) and applying the divergence operator to the derived equation, the following form of motion law for the passive, poroelastic behavior can be obtained:


$$
\frac{(1-v) E}{(1+v)(1-2 v)} \nabla^{2} e^{\mathrm{s}}=\beta \nabla^{2} P
\tag{18}
$$

Substituting Eq. (13) into Eq. (18), the following evolution equation of the volumetric strain for the electrochemical-poroelastic behavior can be derived:
$$
L \nabla^{2} e^{\mathrm{s}}=\frac{1}{C_{2}} \frac{\partial e^{\mathrm{s}}}{\partial t}+\frac{C_{1}}{C_{2}} \frac{\beta}{(1-\beta)} \nabla J
\tag{19a}
$$
where
$$
L=\frac{(1-v) E}{f(1+v)(1-2 v)}
\tag{19b}
$$

The basic equation of Galerkin finite element formulation of Eq. (19a) is expressed by the following equation:
$$
\int_{V_{\mathrm{e}}}[N]^{\mathrm{T}}\left(L \nabla^{2} e^{\mathrm{s}}-\frac{1}{C_{2}} \frac{\partial e^{\mathrm{s}}}{\partial t}-\frac{C_{1}}{C_{2}} \frac{\beta}{(1-\beta)} \nabla J\right) \mathrm{d} V=0
\tag{20}
$$

Applying Green's theorem to Eq. (20) and substituting Eqs. (14a) and (14b) into the derived equation, the following equation can be obtained:
$$
\begin{aligned}
& \int_{V_{\mathrm{e}}}[N]^{\mathrm{T}}[N]\left\{\dot{e}_{\mathrm{N}}^{\mathrm{s}}\right\} \mathrm{d} V \\
& \quad=C_{1} \frac{\beta}{(1-\beta)} \int[N]^{\mathrm{T}}[N]\left\{\dot{c}_{\mathrm{N}}\right\} \\
& \quad-C_{2} J \int_{V_{\mathrm{e}}}\left(\frac{\partial[N]^{\mathrm{T}}}{\partial x} \frac{\partial[N]}{\partial x}+\frac{\partial[N]^{\mathrm{T}}}{\partial y} \frac{\partial[N]}{\partial y}+\frac{\partial[N]^{\mathrm{T}}}{\partial z} \frac{\partial[N]}{\partial z}\right)\left\{e_{\mathrm{N}}^{\mathrm{s}}\right\} \mathrm{d} V
\end{aligned}
\tag{21}
$$

From Eq. (21), the following evolution equation of the volumetric strain can be obtained:
$$
[S]\left\{\dot{e}_{\mathrm{N}}^{\mathrm{s}}\right\}=C_{1} \frac{\beta}{(1-\beta)}[S]\left\{\dot{c}_{\mathrm{N}}\right\}-C_{2} J[A]\left\{e_{\mathrm{N}}^{\mathrm{s}}\right\}.
\tag{22}
$$

### 2.4. Ionic transportation equation

Turning on electricity of conducting polymer membranes in an electrolyte bath, the insertion and de-insertion of ions take place, which accelerates the deformation of expansion and contraction. Moving ions in the electrolyte bath are subjected to the forces due to viscous resistance, diffusion and electricity, the balance of which leads to the following differential equation with respect to the total electric charge $Q(x, t)$ [6]:
$$
\begin{aligned}
\eta_{1} \frac{\partial Q(x, t)}{\partial t}= & k T \frac{\partial^{2} Q(x, t)}{\partial x^{2}}-\frac{\partial Q(x, t)}{\partial x} \\
& \times\left\{\frac{e}{\varepsilon_{\mathrm{e}} S_{x}}\left[\int_{0}^{t} \mathrm{i}(\tau) \mathrm{d} \tau+Q(x, t)-Q(x, 0)\right]\right\}
\end{aligned}
\tag{23}
$$

Assuming that the electrodes in the polymer membrane and the electrolyte are located respectively at $x=0$ and $x=d$, the initial and boundary conditions are as follows [6]:
$$
\{Q(x, 0)\}=N_{\mathrm{a}} e S_{x} c_{0} x
\tag{24a}
$$
$$
\{Q(0, t)\}=0,
\tag{24b}
$$
$$
\{Q(d, t)\}=N_{\mathrm{a}} e S_{x} c_{0} d
$$
where $i$ is the electric current. The notations for the other symbols contained in Eqs. (23), (24a) and (24b) are given in Table 2. It should be noted that the ionic movement in the polymer membrane is assumed to be similar to that in the electrolyte bath for simplicity.

The electric charge density $c(x, t)$ is calculated by the following equation, using the obtained total charge:
$$
Q(x, t)=N_{\mathrm{a}} e S_{x} \int_{0}^{x} c(\xi, t) \mathrm{d} \xi
\tag{25}
$$

Zero slope is assumed as the boundary conditions for the electric charge density.

The finite element formulation is conducted for Eqs. (23) and (25). The total electric charge $Q(x, t)$ is linearly interpolated in each element.
$$
\{Q(x, t)\}=[N]\left\{Q_{\mathrm{N}}\right\}=\left[1-\frac{x}{h} \quad \frac{x}{h}\right]\left\{\begin{array}{c}
Q_{i} \\
Q_{j}
\end{array}\right\}
\tag{26}
$$
where $Q_{i}$ and $Q_{j}$ are the total charge at nodes. $h$ is the element length. The finite element formulation by Galerkin method is conducted for Eq. (23)
$$
\begin{aligned}
& \int_{0}^{h}[N]^{\mathrm{T}}\left(\eta_{1} \frac{\partial Q(x, t)}{\partial t}-k T \frac{\partial^{2} Q(x, t)}{\partial x^{2}}+\frac{\partial Q(x, t)}{\partial x}\right. \\
& \left.\quad \times\left\{\frac{e}{\varepsilon_{\mathrm{e}} S_{x}}\left[\int_{0}^{t} \mathrm{i}(\tau) \mathrm{d} \tau+Q(x, t)-Q(x, 0)\right]\right\}\right) \mathrm{d} x=0
\end{aligned}
\tag{27}
$$

Applying Green's theorem to Eq. (27) and substituting Eqs. (26) and (27) into the derived equation, the following ordinary differential equation system for the total charge can be obtained:
$$
\left[\begin{array}{ll}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{array}\right]\left\{\dot{Q}_{\mathrm{N}}\right\}+\left[\begin{array}{ll}
B_{11} & B_{12} \\
B_{21} & B_{22}
\end{array}\right]\left\{Q_{\mathrm{N}}\right\}=0
\tag{28}
$$
where
$$
\left[\begin{array}{ll}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{array}\right]=\left[\begin{array}{cc}
\frac{h}{3} & \frac{h}{6} \\
\frac{h}{6} & \frac{h}{3}
\end{array}\right]
\tag{29a}
$$
$$
\begin{aligned}
& {\left[\begin{array}{ll}
B_{11} & B_{12} \\
B_{21} & B_{22}
\end{array}\right]} \\
& \quad=\left[\begin{array}{ll}
\frac{k T}{\eta_{1} h}-\frac{e}{2 \eta_{1} \varepsilon_{\mathrm{e}} S_{x}}\left[\int_{0}^{t} i(\tau) d \tau\right]+B_{1} & -\frac{k T}{\eta_{1} h}+\frac{\Delta t e}{2 \eta_{1} \varepsilon_{\mathrm{e}} S_{x}}\left[\int_{0}^{t} i(\tau) d \tau\right]+B_{2} \\
-\frac{k T}{\eta_{1} h}-\frac{e}{2 \eta_{1} \varepsilon_{\mathrm{e}} S_{x}}\left[\int_{0}^{t} i(\tau) d \tau\right]+B_{3} & \frac{k T}{\eta_{1} h}+\frac{e}{2 \eta_{1} \varepsilon_{\mathrm{e}} S_{x}}\left[\int_{0}^{t} i(\tau) d \tau\right]+B_{4}
\end{array}\right]
\end{aligned}
\tag{29b}
$$
$$
\begin{aligned}
& B_{1}=-\frac{e}{\eta_{1} \varepsilon_{\mathrm{e}} S_{x}}\left[\frac{1}{3}\left(Q_{i}(x, t)-Q_{i}(x, 0)\right)+\frac{1}{6}\left(Q_{j}(x, t)-Q_{j}(x, 0)\right)\right] \\
& B_{3}=-\frac{e}{\eta_{1} \varepsilon_{\mathrm{e}} S_{x}}\left[\frac{1}{6}\left(Q_{i}(x, t)-Q_{j}(x, 0)\right)+\frac{1}{3}\left(Q_{j}(x, t)-Q_{j}(x, 0)\right)\right] \\
& B_{2}=-B_{1}, \quad B_{4}=-B_{3}
\end{aligned}
\tag{29c}
$$

Conducting the finite element formulation by Galerkin method for Eq. (25) relating the total charge with the charge density, the following equation can be obtained:

$$
\int_{0}^{h}[N]^{\mathrm{T}}\left(\frac{\partial Q(x, t)}{\partial x}-N_{\mathrm{a}} e S_{x} c(x, t)\right) \mathrm{d} x=0
\tag{30}
$$

Substituting Eq. (26) into Eq. (30), the following equation can be obtained:

$$
\left[\begin{array}{ll}
C_{11} & C_{12} \\
C_{21} & C_{22}
\end{array}\right]\left\{c_{\mathrm{N}}\right\}=\left[\begin{array}{ll}
D_{11} & D_{12} \\
D_{21} & D_{22}
\end{array}\right]\left\{Q_{\mathrm{N}}\right\}
\tag{31}
$$

where

$$
\left[\begin{array}{ll}
C_{11} & C_{12} \\
C_{21} & C_{22}
\end{array}\right]=\left[\begin{array}{cc}
\frac{N_{\mathrm{a}} e S_{x} h}{3} & \frac{N_{\mathrm{a}} e S_{x} h}{6} \\
\frac{N_{\mathrm{a}} e S_{x} h}{6} & \frac{N_{\mathrm{a}} e S_{x} h}{3}
\end{array}\right]
\tag{32a}
$$

$$
\left[\begin{array}{ll}
D_{11} & D_{12} \\
D_{21} & D_{22}
\end{array}\right]=\left[\begin{array}{cc}
-\frac{1}{2} & \frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2}
\end{array}\right]
\tag{32b}
$$

By summing up Eq. (28) for all elements and integrating with respect to time using a numerical integration scheme such as Euler method, time history of the total charge can be obtained. The charge density is calculated from Eq. (31).

### 2.5. Computational procedure

The so-called weakly-coupled approach is employed to solve the discretized field equations which are the stiffness equation for the displacement (7), Poisson's equation for the pressure (17), the evolution equation for the volumetric strain rate (22) and the ionic transportation equation for the electric charge (28). As seen from the mathematical structure of these governing equations, Eq. (28) is uncoupled with the other equations which are coupled with each other. It means physically that the ionic transportation is not influenced by the mechanical response of polypyrroles, which is a generally accepted assumption when the deformation is small compared with the size of specimens [6,8]. The extension to the coupled problem is a future work. All of the governing equations are solved in a sequential way within a small time increment. Sufficiently small time increments are used for simplicity in the present analysis instead of using iterative procedures which are known to be effective to reduce the numerical error due to piecewise linearization [11].

Computational procedure for the active, electrochemical-poroelastic behavior using finite element equations given in the preceding subsections is as follows. The electric charge density is obtained from the global system forms of Eqs. (28) and (31). The volumetric strain rate is obtained from the global system form of Eq. (22) by using the electric charge density rate and the volumetric strain. The pressure is calculated from the global system form of Eq. (17) by using the volumetric strain rate and the electric charge density rate. The displacement increment is calculated from the global system form of Eq. (7) by using the pressure increment. The stress increments in solid and fluid are calculated from Eqs. (6a) and (6b) by using the displacement increment and the pressure increment. These procedures are repeated at each small time increment intervals until the final time.

## 3. Results of finite element analysis

### 3.1. Analysis of passive, poroelastic behavior

The passive, poroelastic behavior of a polypyrrole membrane as shown in Fig. 1 has been simulated. Giving the polypyrrole film an initial strain in z-direction, the stress relaxation phenomenon due to the insertion of fluid has been analyzed by using material parameters given in Table 1. When the initial pressure in the polypyrrole membrane is lower than in the surrounding electrolyte, the insertion of the electrolyte into the polypyrrole membrane takes place, which causes increase of the internal pressure, increase of the stress in solid and relaxation of the total stress with time. Fig. 2 shows the finite element results for the time variation of the pressure distributions. In Fig. 3, the finite element results for the time histories of the internal pressure, the stress in solid and the total stress are compared with the theoretical solution given by Della Santa et al.

![](./images/812004378293567489_3.jpg)

Fig. 1. Polypyrrole film used for passive, poroelastic response analysis.

<table>
<caption>Table 1<br>Material parameters for passive, poroelastic response analysis</caption>
<tbody>
<tr>
<td>Initial strain</td>
<td>$e_{0}=0.00340909$</td>
</tr>
<tr>
<td>Poisson's ratio</td>
<td>$v=0.412$</td>
</tr>
<tr>
<td>Frictional coefficient</td>
<td>$f=1.29\times 10^{20}$ (Ns m$^{-4}$)</td>
</tr>
<tr>
<td>Young's modulus</td>
<td>$E=1290$ (MPa)</td>
</tr>
<tr>
<td>Porosity</td>
<td>$\beta=0.108$</td>
</tr>
<tr>
<td>Time increment</td>
<td>$\Delta t=0.005$ s</td>
</tr>
</tbody>
</table>

![](./images/812004378293567489_4.jpg)

Fig. 2. Pressure distribution in polypyrrole membrane.

![](./images/812004378293567489_5.jpg)

Fig. 3. Total stress, stress on the solid and fluid pressure vs. time.

[1]. The validity of the present analytical algorithm is confirmed from these results.

### 3.2. Analysis of electrochemical-poroelastic behavior

The natural stress relaxation phenomenon under no electric current was analyzed in the preceding subsection. In the present subsection, supposing cation-driven actuators, the active, electrochemical-poroelastic behavior is analyzed. The dimensions of a polypyrrole membrane is the same as in Fig. 1. Table 2 shows the material parameters used in the analysis ($c_0 = c(x,0) = 1147\ \text{mol/m}^3$).

Fig. 4 shows the calculated results in which the pressure rise is accelerated by the insertion of cations into the membrane, taking polypyrrole membrane side as negative and electrolyte side as positive. Fig. 4a shows assumed three

<table>
<caption>Table 2
Material parameters for active, electrochemical-poroelastic response analysis</caption>
<tbody>
<tr>
<td>Coefficient of viscosity for moving ions</td>
<td>$\eta_1 = 1.18 \times 10^{-11}\ (\text{N s/m}^2)$</td>
</tr>
<tr>
<td>Boltzman constant</td>
<td>$k = 1.380 \times 10^{-23}\ (\text{N m/K})$</td>
</tr>
<tr>
<td>Absolute temperature</td>
<td>$T = 293\ (\text{K})$</td>
</tr>
<tr>
<td>Elemental charge</td>
<td>$e = 1.6 \times 10^{-19}(\text{C})$</td>
</tr>
<tr>
<td>Dielectric constant of electrolyte</td>
<td>$\varepsilon_\text{e} = 2.8 \times 10^{-3}\ (\text{C}^2/\text{N m}^2)$</td>
</tr>
<tr>
<td>Time interval</td>
<td>$\Delta t = 5 \times 10^{-4}(\text{s})$</td>
</tr>
<tr>
<td>Space interval</td>
<td>$h = 2\ (\mu\text{m})$</td>
</tr>
<tr>
<td>Cross-section area</td>
<td>$S_x = 34.2 \times 10^{-6}\ (\text{m}^2)$</td>
</tr>
<tr>
<td>Avogadro number</td>
<td>$N_\text{a} = 6.02 \times 10^{-23}\ (/ \text{mol})$</td>
</tr>
</tbody>
</table>

![](./images/812004378293567489_6.jpg)

Fig. 4. Electrochemical-mechanical response of polypyrrole membrane (active insertion of cations). (a) Current patterns. (b) Time variations of charge density distribution (case 3). (c) Time histories of pressure.

types of electric current patterns whose durations of step- wise currents are two seconds (case 1), four seconds (case 2) and six seconds (case 3), respectively. Fig. 4b shows time variations of the electric charge density distribution in the membrane $(0 \leqslant x \leqslant 0.0175)$ and the electrolyte bath $(0.0175 < x \leqslant 0.175)$, from which it can be seen that the charge density rises with time by the insertion of cations into the membrane. Fig. 4c is the time-history of the pres- sure in the membrane. Comparing with the passive behav- iors analyzed in the preceding subsection, the pressure rises faster when turning on the electricity and it gradually approaches the pressure of electrolyte by the passive de- insertion of electrolyte after turning off the electricity. These results can be considered to be reasonable.

![](./images/812004378293567489_7.jpg)

Fig. 5. Electrochemical-mechanical response of polypyrrole membrane (active de-insertion of cations). (a) Current patterns. (b) time variations of charge density distribution (case 3). (c) Time histories of pressure.

![](./images/812004378293567489_8.jpg)

Fig. 6. Bipolymer strip.

![](./images/812004378293567489_9.jpg)

Fig. 7. Electrochemical-poroelastic response of bipolymer strip. (a) Current patterns. (b) Time variation of curvature change (case 3). (c) Bending deformation.

Fig. 5 shows the calculated results in which the pressure rise is decelerated by the de-insertion of cations into the membrane, taking polypyrrole membrane side as positive and electrolyte side as negative. Fig. 5a-c shows the electric current patterns, the time variation of the electric charge density distribution (case 3) and the time-history of the pressure in the membrane. The pressure decreases by the de-insertion of cations when turning on the electricity and it gradually approaches the pressure of electrolyte by the passive insertion of electrolyte after turning off the electricity, which can also be considered to be a reasonable result.

Another example for the active, electrochemical-poro-elastic analysis is shown in Fig. 6, which is a cantilever bending strip composed of polyethylene layer, polypyrrole layer and thin gold layer under repeated pulsed electric potentials between $-0.85\ \text{V}$ and $+0.3\ \text{V}$ [12]. Fig. 7a-c shows the electric current pattern, time-histories of the curvature change and the deformed profile, respectively. As the current pattern and most physical constants of the polypyrrole membrane used in the experiment [12] are unknown, they have been assumed so as to give the calculated curvature change in good correspondence with the experimental result.

From the above-mentioned numerical studies, the present computational modeling can be considered to be qualitatively reasonable, however, quantitative validation based on experiments remains as a future subject.

## 4. Concluding remarks

A computational modeling for the electrochemical-poroelastic behavior has been proposed to support design and development of actuators using conducting polymers such as polypyrrole. The three-dimensional continuum modeling given by Della Santa et al. based on Biot's poroelasticity theory has been extended to the formulation for the active, electrochemical-poroelastic behavior according to Onsagar's-like law, which is combined with the one-dimensional ionic transportation equation to construct the system of governing equations. Discretizing these equations by the finite element method, numerical sudies have been carried out for the passive, poroelastic behavior and the active, electrochemical-poroelastic behavior of polypyrrole membranes. The former result and the latter result have been compared with the theoretical solution and the experimental result, respectively. The validity has been verified from a qualitative point of view. Lots of processes including determination of physical constants are necessary for quantitative validation, which are future subjects with the applications to the other conducting polymers such as polyaniline and the multi-dimensional modeling of ionic transportation equation.

## References

[1] Della Santa A et al. Passive mechanical properties of polypyrrole films: a continuum, poroelastic model. Material Science and Engineering 1997;C5:101-9.

[2] Della Santa A et al. Performance and work capacity of a polypyrrole conducting polymer linear actuator. Synthetic Metals 1997;90:93-100.

[3] Della Santa A et al. Characterization and modelling of a conducting polymer muscle-like linear actuator. Smart Materials and Structures 1997;6:23-34.

[4] Cortes MT, Moreno JC. Artificial muscles based on conducting polymers. e-Polymers 2003;041:1-42.

[5] Hara S et al. Artificial muscles based on polypyrrole actuators with large strain and stress induced electrically. Polymer Journal 2004;36(2):151-61.

[6] Tadokoro S, et al. An actuator model of ICPF for robotic applications on the basis of physicochemical hypotheses. Proceedings of the 2000 IEEE International Conference on Robotics and Automation 2000; 1340-1346.

[7] Toi Y, Kang SS. Finite element modeling of electrochemical-mechanical behaviors of ionic conducting polymer-metal composites. Transactions of the Japan Society of Mechanical Engineers, Series A 2004;70(689):9-16.

[8] Toi Y, Kang SS. Finite element analysis of two-dimensional electrochemical-mechanical response of ionic conducting polymer-metal composite beams. Computers and Structures 2005;83:2573-83.

[9] Biot MA. Theory of elasticity and consolidation for a porous anisotropic solid. Journal of Applied Physics 1954;26:182-5.

[10] Katchalsky A, Curran PF. Non-equilibrium thermodynamics in biophysics. Harvard University Press; 1967.

[11] Bathe KJ. Finite element procedures. Prentice Hall; 1996.

[12] Pei Q, Inganas O. Electrochemical muscles: bending strips built from conjugated polymers. Synthetic Metals 1993;55-57:3718-23.