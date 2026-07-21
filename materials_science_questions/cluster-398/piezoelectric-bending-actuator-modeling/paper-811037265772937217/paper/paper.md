![](./images/811037265772937217_1.jpg)

Finite Elements in Analysis and Design 26 (1997) 303-314

FINITE ELEMENTS
IN ANALYSIS
AND DESIGN

# The static shape control for intelligent structures

Zhongdong Wang, Su-huan Chen*, Wanzhi Han

Centre for Computational Mechanics, Jilin University of Technology, Changchun 130022, People's Republic of China

## Abstract
A finite element formulation is presented for modeling the plate structure containing distributed piezoelectric sensors and actuators (S/As). A new plate bending element for analysis of the plate with distributed piezoelectric S/As is developed. This element saves much memory and computation time. Using the bending plate element, a general method of static shape control for the intelligent structure is put forth. Two examples are given to illustrate the application of the method presented in this paper. The purpose of the first example is to check the accuracy of the finite element method presented in this paper. The second example is to study the problem of the static shape control for the intelligent structure. It is concluded that the shape of the intelligent structure can reach the desired shape through passive control or active control.
© 1997 Elsevier Science B.V.

Keywords: Static shape control; Intelligent structures; Piezoelectric S/As

## 1. Introduction
The intelligent structures are the systems whose geometric and structural characteristics can be beneficially modified during their operational life to meet the mission's requirement [1]. They comprise the main structure and distributed piezoelectric S/As. Because of their self-monitoring and self-adaptive capabilities, the intelligent structures have recently attracted considerable attention for their potential applications as sensors for monitoring and as actuators for controlling the shape and response of the structures. The formation of those 'Smart' systems in advanced structural design has drawn significant research over past few years. The intelligent structures have some distinct advantages over the conventional actively controlled structure. Since the intelligent structures are distributed and are more accurate in monitoring and controlling response, this new technology could be applied in design of large-scale space structures, aircraft structures, satellite and so forth [2].

There are two basic phenomena, characteristic of piezoelectric materials, which permit them to be used as sensors and actuators in the intelligent structures. The first phenomenon is called the direct piezoelectric effect that implies when some mechanical force or pressure is applied on a piezoelectric component, some electrical charge or voltage is induced in the piezoelectric material.

* Corresponding author.

0168-874X/97/$17.00 © 1997 Elsevier Science B.V. All rights reserved
PII S0168-874X(97)00086-8

Conversely, if some charge or voltage is imposed on a piezoelectric material, the material generates some mechanical force or pressure. This phenomenon is called the converse piezoelectric effect. Lead zirconate titanate (PZT) and polyvinylidene fluoride (PVDF) in piezoelectric materials are often used as the distributed piezoelectric S/As because of their advantages.

Several analysis and numerical models have been developed to analyze the intelligent structure. Most of them are based on analysis approaches [3-5], and Ritz method [6]. Finite element method analysis for the intelligent structures with distributed piezoelectric material are described in Refs. [7-9]. In these methods the plate and thin S/As are modeled with the isoparametric hexahedron solid element, which will cause some drawbacks. The hexahedron solid elements are too thick for thin shell/plate applications. It will cause excessive strain energies and higher stiffness coefficients in thickness direction. To overcome this shortcoming, internal degrees of freedom were added in formulation, which make the problem large and complex.

There are two essential ideas in this paper. The first is the development of a new piezoelectric plate bending element with electric degree of freedom for analysis of the intelligent structure. By modeling the plate and piezoelectric S/As with this new element, the problem size is reduced greatly. The second is to develop a general method of static shape control for the intelligent structures. The static shape of the intelligent structure can be controlled by using this method. Finally, two numerical examples are presented to demonstrate the validity of the method presented in this paper.

## 2. Finite element formulation for the intelligent structure

### 2.1. Lagrangian equations [10]

The Lagrangian function is $L=K-U$, where $K$ and $U$ are the kinetic and potential energy of the system, respectively. In general, the kinetic energy depends functionally on the generalized coordinates $u_{1}, u_{2}, u_{3}, \ldots$, and the generalized velocities $\dot{u}_{1}, \dot{u}_{2}, \dot{u}_{3}, \ldots$, and the potential energy due to all conservative forces depends only on the generalized coordinate.

In practice, a system also has non-conservative forces, such as internal dissipative forces, applied electric potential on electrodes. The non-conservative part of energy can be written as
$$
W=\sum_{n} \int F_{n} \cdot u_{n} \mathrm{~d} \Omega \quad n=1,2,3, \ldots,\qquad(1)
$$
where the variable $F_{n}$ and $u_{n}$ are called generalized forces and coordinates, respectively, and the $\Omega$ is a region on which the generalized forces are applied.

Hamilton's principle means that the variation of the function $I=\int L \mathrm{~d} t$ is zero and subsequent integration by parts leads to
$$
\int_{t_{1}}^{t_{2}}\left[\left(\sum_{n} \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial \dot{u}_{n}}-\frac{\partial L}{\partial u_{n}}-F_{n}\right) \delta u_{n}\right] \mathrm{d} t=0 \quad n=1,2,3, \ldots\qquad(2)
$$

Since the generalized coordinates are linearly independent, we obtain
$$
\frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial \dot{u}_{n}}-\frac{\partial L}{\partial u_{n}}-F_{n}=0 \quad n=1,2,3, \ldots\qquad(3)
$$

These are the Lagrangian equations of motion for a system in the general case. In piezoelectric structure, the generalized coordinates are the components of the elastic displacement $u_1, u_2, u_3$ and the electric potential applied on the electrode, $v$.

### 2.2. Constitutive equation

#### 2.2.1. Piezoelectric field
The linear constitutive equations coupling between elastic field and electric field in a piezoelectric medium can be expressed by the direct and inverse piezoelectric equations, respectively [11]. These equations for the plate shape sensor and actuator are written as follows:

$$
\left\{\begin{array}{l}
D_{x} \\
D_{y} \\
D_{z}
\end{array}\right\}=\left[\begin{array}{lll}
e_{11} & e_{12} & e_{16} \\
e_{21} & e_{22} & e_{26} \\
e_{31} & e_{32} & e_{36}
\end{array}\right]\left\{\begin{array}{l}
\varepsilon_{x} \\
\varepsilon_{y} \\
\gamma_{x y}
\end{array}\right\}+\left[\begin{array}{lll}
\zeta_{11} & \zeta_{12} & \zeta_{13} \\
\zeta_{21} & \zeta_{22} & \zeta_{23} \\
\zeta_{31} & \zeta_{32} & \zeta_{33}
\end{array}\right]\left\{\begin{array}{l}
E_{x} \\
E_{y} \\
E_{z}
\end{array}\right\},
\tag{4}
$$

$$
\left\{\begin{array}{l}
\sigma_{x} \\
\sigma_{y} \\
\tau_{x y}
\end{array}\right\}=\left[\begin{array}{lll}
D_{p 11} & D_{p 12} & D_{p 16} \\
D_{p 21} & D_{p 22} & D_{p 26} \\
D_{p 31} & D_{p 32} & D_{p 36}
\end{array}\right]\left\{\begin{array}{l}
\varepsilon_{x} \\
\varepsilon_{y} \\
\gamma_{x y}
\end{array}\right\}-\left[\begin{array}{lll}
e_{11} & e_{21} & e_{31} \\
e_{12} & e_{22} & e_{32} \\
e_{16} & e_{26} & e_{36}
\end{array}\right]\left\{\begin{array}{l}
E_{x} \\
E_{y} \\
E_{z}
\end{array}\right\},
\tag{5}
$$

Eq. (4) describes the direct piezoelectric effect and Eq. (5) describes the inverse piezoelectric effect.

Eqs. (4) and (5) can be written simply as
$$
\{D\}=[e]\{\varepsilon\}+[\zeta]\{E\},
\tag{6}
$$

$$
\{\sigma\}=\left[D_{p}\right]\{\varepsilon\}-[e]^{\mathrm{T}}\{E\},
\tag{7}
$$
where $\{D\},\{E\},\{\varepsilon\}$, and $\{\sigma\}$ are the electric displacement, electrical field, strain, and stress vectors, respectively, and $[D_{\mathrm{p}}],[e],[\zeta]$ are the elasticity, piezoelectric, and dielectric constant matrices, respectively, $[e]^{\mathrm{T}}$ is defined as the transpose of $[e]$.

#### 2.2.2. Elastic field
The constitutive equation in the elastic field is as follows:

$$
[\sigma]=\left[D_{\mathrm{s}}\right]\{\varepsilon\},
\tag{8}
$$
where $[D]$ is the elasticity constant matrix of the main structure in the intelligent structure.

### 2.3. Finite element formulation

#### 2.3.1. Elastic field discretization
The arbitrary quadrilateral bending element of plate [12] is adopted in the problems. The element is a four-node, 12-degree-of-freedom isoparametric element for thin plates. The element nodal variable $\{u^{e}\}$ is defined as

$$
\left\{u^{e}\right\}=\left\{w_{1} \quad \theta_{x_{1}} \quad \theta_{y_{1}} \quad w_{2} \quad \theta_{x_{2}} \quad \theta_{y_{2}} \cdots w_{4} \quad \theta_{x_{4}} \quad \theta_{y_{4}}\right\}^{\mathrm{T}},
\tag{9}
$$
where $w$ is the normal displacement, $\theta_{x}(=\partial w / \partial y)$ and $\theta_{y}(=-\partial w / \partial x)$ are the rotation about the $x$ and $y$ axes. The normal displacement variable $w$ is expressed as the function of nodal displacement

variable by finite element interpolation functions as follows:

$$
w=[N]\left\{u^{e}\right\}=\left[\begin{array}{llllllllll}
N_{1} & N_{x_{1}} & N_{y_{1}} & N_{2} & N_{x_{2}} & N_{y_{2}} & \cdots & N_{4} & N_{x_{4}} & N_{y_{4}}
\end{array}\right]\left\{u^{e}\right\},
\tag{10}
$$

where $N_{1} \ N_{x_{1}} \ N_{y_{1}} \ \cdots N_{4} \ N_{x_{4}} \ N_{y_{4}}$ are the interpolation functions, they are written as follows:

$$
\begin{aligned}
{\left[\begin{array}{lll}
N_{1} & N_{x_{1}} & N_{y_{1}}
\end{array}\right]=\frac{1}{16} X_{1} Y_{1}[} & X_{1} Y_{1}-X_{2} Y_{2}+2 X_{1} X_{2}+2 Y_{1} Y_{2} \\
& \left.y_{21} X_{1} X_{2}+y_{31} Y_{1} Y_{2} \quad-x_{21} X_{1} X_{2}-x_{31} Y_{1} Y_{2}\right],
\end{aligned}
\tag{11}
$$

$$
\begin{aligned}
{\left[\begin{array}{lll}
N_{2} & N_{x_{2}} & N_{y_{2}}
\end{array}\right]=\frac{1}{16} X_{2} Y_{1}[} & X_{2} Y_{1}-X_{1} Y_{2}+2 X_{1} X_{2}+2 Y_{1} Y_{2} \\
& \left.-y_{21} X_{1} X_{2}+y_{42} Y_{1} Y_{2} \quad x_{21} X_{1} X_{2}-x_{42} Y_{1} Y_{2}\right],
\end{aligned}
\tag{12}
$$

$$
\begin{aligned}
{\left[\begin{array}{lll}
N_{3} & N_{x_{3}} & N_{y_{3}}
\end{array}\right]=\frac{1}{16} X_{1} Y_{2}[} & X_{1} Y_{2}-X_{2} Y_{1}+2 X_{1} X_{2}+2 Y_{1} Y_{2} \\
& \left.y_{43} X_{1} X_{2}-y_{31} Y_{1} Y_{2} \quad-x_{43} X_{1} X_{2}+x_{31} Y_{1} Y_{2}\right],
\end{aligned}
\tag{13}
$$

$$
\begin{aligned}
{\left[\begin{array}{lll}
N_{4} & N_{x_{4}} & N_{y_{4}}
\end{array}\right]=\frac{1}{16} X_{2} Y_{2}[} & X_{2} Y_{2}-X_{1} Y_{1}+2 X_{1} X_{2}+2 Y_{1} Y_{2} \\
& \left.y_{43} X_{1} X_{2}-y_{42} Y_{1} Y_{2} \quad-x_{43} X_{1} X_{2}+x_{42} Y_{1} Y_{2}\right],
\end{aligned}
\tag{14}
$$

where

$$
X_{1}=1-\xi, \quad X_{2}=1+\xi, \quad Y_{1}=1-\eta, \quad Y_{2}=1+\eta,
$$

$$
x_{i j}=x_{i}-x_{j}, \quad y_{i j}=y_{i}-y_{j} \quad(i, j=1,2,3,4).
$$

The strain variable $\{\varepsilon\}$ is expressed as the function of nodal displacement variable. It is

$$
\{\varepsilon\}=z\left\{\begin{array}{c}
-\frac{\partial^{2} w}{\partial x^{2}} \\
-\frac{\partial^{2} w}{\partial y^{2}} \\
-2 \frac{\partial^{2} w}{\partial x \partial y}
\end{array}\right\}=z\left[B_{u}\right]\left\{u^{e}\right\},
\tag{15}
$$

where $\left[B_{u}\right]=\left[\begin{array}{llll}B_{u_{1}} & B_{u_{2}} & B_{u_{3}} & B_{u_{4}}\end{array}\right]$ and

$$
\left[B_{u_{i}}\right]=-\left[\begin{array}{ccc}
\frac{\partial^{2} N_{i}}{\partial x^{2}} & \frac{\partial^{2} N_{x_{i}}}{\partial x^{2}} & \frac{\partial^{2} N_{y_{i}}}{\partial x^{2}} \\
\frac{\partial^{2} N_{i}}{\partial y^{2}} & \frac{\partial^{2} N_{x_{i}}}{\partial y^{2}} & \frac{\partial^{2} N_{y_{i}}}{\partial y^{2}} \\
2 \frac{\partial^{2} N_{i}}{\partial x \partial y} & 2 \frac{\partial^{2} N_{x_{i}}}{\partial x \partial y} & 2 \frac{\partial^{2} N_{y_{i}}}{\partial x \partial y}
\end{array}\right].
\tag{16}
$$

### 2.3.2. Electrical field discretization
The element nodal electric potential variable $\{v^{e}\}$ is defined as

$$
\left\{v^{e}\right\}=\left\{\begin{array}{llll}
v_{1} & v_{2} & v_{3} & v_{4}
\end{array}\right\}^{\mathrm{T}}.
\tag{17}
$$

The electric potential variable $\{v\}$ is expressed as the function of nodal electric potential variables. It is

$$
\{v\}=\left[N_{v}\right]\left\{v^{e}\right\},
\tag{18}
$$

where

$$
\left[N_{v}\right]=\left[\begin{array}{llll}N_{1} & N_{2} & N_{3} & N_{4}\end{array}\right]^{\mathrm{T}}
\tag{19}
$$

$$
\begin{aligned}
& N_{1}=\frac{1}{4}(1-\xi)(1-\eta) \quad N_{2}=\frac{1}{4}(1+\xi)(1-\eta), \\
& N_{3}=\frac{1}{4}(1-\xi)(1+\eta) \quad N_{4}=\frac{1}{4}(1+\xi)(1+\eta).
\end{aligned}
\tag{20}
$$

The electric field $\{E\}$ is defined by the electric potential $\{v\}$ by using a gradient operator $\nabla$, and written in terms of nodal electric potential variables

$$
\{E\}=-\nabla\{v\}=-\left[B_{v}\right]\left\{v^{\mathrm{e}}\right\},
\tag{21}
$$

where

$$
\left[B_{v}\right]=\left[\begin{array}{llll}B_{v_{1}} & B_{v_{2}} & B_{v_{3}} & B_{v_{4}}\end{array}\right],
\tag{22}
$$

$$
\left[B_{v_{i}}\right]=\left[\begin{array}{lll}\frac{\partial N_{i}}{\partial x} & \frac{\partial N_{i}}{\partial y} & \frac{\partial N_{i}}{\partial z}\end{array}\right].
\tag{23}
$$

### 2.4. Finite element equation formulation

The element kinetic energy is

$$
T_{\mathrm{e}}=\frac{1}{2} \int_{Q_{\mathrm{se}}} \rho_{\mathrm{s}}\{\dot{u}\}^{\mathrm{T}}\{\dot{u}\} \mathrm{d} Q+\frac{1}{2} \int_{Q_{\mathrm{pe}}} \rho_{\mathrm{p}}\{\dot{u}\}^{\mathrm{T}}\{\dot{u}\} \mathrm{d} Q
\tag{24}
$$

where $\rho_{\mathrm{s}}$ and $\rho_{\mathrm{p}}$ are the main structure material and piezoelectric material mass density, respectively. The subscript s,p and e represent the main structure, the piezoelectric material, and element, respectively. $Q$ is the volume of element.

The element potential energy is

$$
V_{\mathrm{e}}=\frac{1}{2} \int_{Q_{\mathrm{pe}}}\{\varepsilon\}^{\mathrm{T}}\{\sigma\} \mathrm{d} Q+\frac{1}{2} \int_{Q_{\mathrm{se}}}\{\varepsilon\}^{\mathrm{T}}\{\sigma\} \mathrm{d} Q.
\tag{25}
$$

The element electric energy is

$$
W_{\mathrm{ee}}=\frac{1}{2} \int_{Q_{\mathrm{pe}}}[E]^{\mathrm{T}}[D] \mathrm{d} Q.
\tag{26}
$$

The work by the surface force and the applied surface electrical charge density is (the work by the body force and point forces are eliminated)

$$
W_{\mathrm{e}}=\int_{S_{1}}\{u\}^{\mathrm{T}}\left\{f_{\mathrm{s}}^{\mathrm{e}}\right\} \mathrm{d} S-\int_{S_{2}}\{v\}^{\mathrm{T}}\left\{q^{\mathrm{e}}\right\} \mathrm{d} S,
\tag{27}
$$

where $S_{1}$ and $S_{2}$ are the surface areas where the surface forces and the electrical charge are applied, respectively. $\left\{f_{\mathrm{s}}^{\mathrm{e}}\right\}$ and $\left\{q^{\mathrm{e}}\right\}$ are the surface forces and the surface electrical charge density, respectively.

The general forces that contribute the non-conservative energy in Eq. (1) can be obtained from
$$
\{F\}=\frac{\partial W_{\mathrm{e}}}{\partial\left\{u^{\mathrm{e}}\right\}}+\frac{\partial W_{\mathrm{e}}}{\partial\left\{v^{\mathrm{e}}\right\}}.
\tag{28}
$$

Now, the Lagrangian function can be expressed as follows:
$$
L_{\mathrm{e}}=T_{\mathrm{e}}-V_{\mathrm{e}}+W_{\mathrm{ee}}
\tag{29}
$$

Substituting Eqs. (24)-(29) into Eq. (3), the element equations of motion of the plate with distributed piezoelectric S/As can be derived (not considering the structural damping)
$$
\left(\left[m_{\mathrm{p}}\right]+\left[m_{\mathrm{s}}\right]\right)\left\{\ddot{u}^{\mathrm{e}}\right\}+\left(\left[k_{u u s}\right]+\left[k_{u u p}\right]\right)\left\{u^{\mathrm{e}}\right\}+\left[k_{u v}\right]\left\{v^{\mathrm{e}}\right\}=\left\{F_{\mathrm{s}}^{\mathrm{e}}\right\},
\tag{30}
$$
$$
\left[k_{v u}\right]\left\{u^{\mathrm{e}}\right\}+\left[k_{v v}\right]\left\{v^{\mathrm{e}}\right\}=\left\{F_{\mathrm{c}}^{\mathrm{e}}\right\},
\tag{31}
$$
where
$$
\left[m_{\mathrm{p}}\right]=\int_{Q_{\mathrm{pe}}}\left[N_{u}\right]^{\mathrm{T}} \rho_{\mathrm{p}}\left[N_{u}\right] \mathrm{d} Q, \quad\left[m_{\mathrm{s}}\right]=\int_{Q_{\mathrm{se}}}\left[N_{u}\right]^{\mathrm{T}} \rho_{\mathrm{s}}\left[N_{u}\right] \mathrm{d} Q, \quad\left[k_{u u s}\right]=z^{2} \int_{Q_{\mathrm{se}}}\left[B_{u}\right]^{\mathrm{T}}\left[D_{\mathrm{s}}\right]\left[B_{u}\right] \mathrm{d} Q,
$$
$$
\left[k_{u u p}\right]=z^{2} \int_{Q_{\mathrm{pe}}}\left[B_{u}\right]^{\mathrm{T}}\left[D_{\mathrm{p}}\right]\left[B_{u}\right] \mathrm{d} Q ;
$$
$$
\left[k_{u v}\right]=\left[k_{v u}\right]^{\mathrm{T}}=z \int_{Q_{\mathrm{pe}}}\left[B_{u}\right]^{\mathrm{T}}\left[e^{\mathrm{T}}\right]\left[B_{v}\right] \mathrm{d} Q, \quad\left[k_{v v}\right]=-\int_{Q_{\mathrm{pe}}}\left[B_{v}\right]^{\mathrm{T}}[\zeta]\left[B_{v}\right] \mathrm{d} Q ;
$$
$$
\left\{F_{\mathrm{s}}^{\mathrm{e}}\right\}=\int_{S_{1}}\left[N_{u}\right]^{\mathrm{T}}\left\{f_{\mathrm{s}}^{\mathrm{e}}\right\} \mathrm{d} S, \quad\left\{F_{\mathrm{c}}^{\mathrm{e}}\right\}=-\int_{S_{2}}\left[N_{v}\right]^{\mathrm{T}}\left\{q^{\mathrm{e}}\right\} \mathrm{d} S.
$$

The static case is only considered for the static shape control. Letting $\left[k_{u u}\right]=\left[k_{u u s}\right]+\left[k_{u u p}\right]$ and substituting it into Eq. (30), we obtain the element static equation of the intelligent plate structure as follows:
$$
\left[k_{u u}\right]\left\{u^{\mathrm{e}}\right\}+\left[k_{u v}\right]\left\{v^{\mathrm{e}}\right\}=\left\{F_{\mathrm{s}}^{\mathrm{e}}\right\},
\tag{32}
$$
$$
\left[k_{v u}\right]\left\{u^{\mathrm{e}}\right\}+\left[k_{v v}\right]\left\{v^{\mathrm{e}}\right\}=\left\{F_{\mathrm{c}}^{\mathrm{e}}\right\}.
\tag{33}
$$

### 3. Condensation of element matrices

In order to assemble element matrices into global system matrices as the normal finite element method, the element matrices need to be condensed. In addition, the displacement vectors are more important than the electrical potential vectors in the static shape control analysis. It is not absolutely necessary to save element electrical potential vectors in each solution equations. Thus, the elec- trical potential vectors are usually condensed to save computer memory and improve computation efficiency. However, a recovery scheme can be set up if the sensing information is required.

Employing the Guyan reduction method to eliminate the element electrical potential vectors $\{v^{\mathrm{e}}\}$ yields the modified element static equation: i.e.,

$$
[k]\{u^{\mathrm{e}}\}=\{F_{\mathrm{s}}^{\mathrm{e}}\}+\{F_{\mathrm{e}}^{\mathrm{e}}\}, \tag{34}
$$

where

$$
[k]=[k_{uu}]-[k_{uv}][k_{vv}]^{-1}[k_{vu}],
$$

$$
\{F_{\mathrm{e}}^{\mathrm{e}}\}=-[k_{uv}][k_{vv}]^{-1}\{F_{\mathrm{c}}^{\mathrm{e}}\}.
$$

The element electrical potential vectors can be recovered by

$$
\{v^{\mathrm{e}}\}=[k_{vv}]^{-1}(\{F_{\mathrm{c}}^{\mathrm{e}}\}-[k_{vu}]\{u^{\mathrm{e}}\}). \tag{35}
$$

Note that $\{F_{\mathrm{c}}^{\mathrm{e}}\}$ is usually zero in the distributed piezoelectric sensor layer. Thus, the distributed piezoelectric sensor element electrical potential output is estimated by

$$
\{v^{\mathrm{e}}\}=-[k_{vv}]^{-1}[k_{vu}]\{u^{\mathrm{e}}\}. \tag{36}
$$

The system static equation is written as follows:

$$
[K]\{U\}=\{F_{\mathrm{S}}\}+\{F_{\mathrm{E}}\}. \tag{37}
$$

## 4. The static shape control for the intelligent structure

The load term of Eq. (34) contains two terms, i.e., the mechanical force and the electrical force. The electrical force, the second term in Eq. (34), is determined by the surface charge density input to the distributed actuator layer, which can be written as follows:

$$
\{q^{\mathrm{e}}\}=\frac{1}{s}\{c\}, \tag{38}
$$

where $\{c\}$ is the charges input, and $s$ the area of electrode. The charges input to the actuators can be denoted

$$
\{c\}=c_{\mathrm{p}} \cdot\{V_{\mathrm{AB}}^{\mathrm{e}}\}, \tag{39}
$$

where $c_{\mathrm{p}}=\varepsilon_{0}s/t$, $\varepsilon_{0}$ is the absolute permittivity, $t$ the thickness of the actuator, and $V_{\mathrm{AB}}^{\mathrm{e}}$ electrical voltage between $A$ and $B$ point in the actuator. Substituting Eq. (39) into (38), we obtain

$$
\{q^{\mathrm{e}}\}=\frac{\varepsilon_{0}}{t}\{V_{\mathrm{AB}}^{\mathrm{e}}\}. \tag{40}
$$

It is concluded that changing the electrical voltage input to the distributed actuators can change electrical forces. Further, if mechanical forces are constant the change of the electrical voltage input to the actuators will cause the change of the nodal displacement. Therefore, it is possible to control the shape of the plate with distributed piezoelectric S/As by changing the electrical voltage input to the actuators. $\{F_{\mathrm{e}}^{\mathrm{e}}\}$ can be regarded as the control forces.

According to the way of introducing electrical voltage into the actuators the static shape control for the intelligent structure can be classified into two types, i.e., passive control and active control.

### 4.1. Passive control

In the passive control all of the piezoelectric materials in the structure are considered as the actuators. The deformation of the structure can be controlled by applying electrical voltage to piezo- electric materials. In order to make the shape of the structure reach the desired shape it is required to continually apply electrical voltage to the actuators. The electrical voltage can be calculated by solution Eq. (36).

### 4.2. Active control

The basic configuration of an intelligent structure is composed of the main structure sandwiched between two piezoelectric thin layers. If one of the piezoelectric thin layer is acted as the distributed sensors and other the actuators, and a feedback control law is implemented by the control system, then, the shape of the structure can be controlled actively.

In the active control, the sensor outputs electrical potential after the structure is applied mechanical forces. It is

$$
\left\{v^{e}\right\}=-\left[k_{u v}\right]^{-1}\left[k_{v u}\right]\left\{u^{e}\right\}. \tag{41}
$$

The electrical potential is then amplified by the feedback gains through a feedback control circuit and fed back to the actuators as the applied electrical voltage. Thus,

$$
\left\{V_{\mathrm{AB}}^{\mathrm{e}}\right\}=G\left\{v^{e}\right\}, \tag{42}
$$

where $G$ is a feedback gain. Then, the actuators generate counteracting moment to control the shape of the structure. The procedure above related is iterated until the desired shape of the structure has been reached.

An active control system of a plate with piezoelectric materials, in which the bottom is acted as distributed sensors and the top as distributed actuators, is illustrated in Fig. 1.

![](./images/811037265772937217_2.jpg)

Fig. 1. The active control system of an intelligent plate.

## 5. Numerical examples

### 5.1. Piezoelectric bimorph beam

A piezoelectric bimorph beam [14] shown in Fig. 2 is considered to check the accuracy of the piezoelectric finite element method presented in this paper.

This beam consists of two identical PVDF uniaxial beams with opposite polarities. The cantilever beam is modeled by five identical plate elements. The material properties of PVDF are shown in Table 1.

The theoretical solution to the deflection of the beam is given by [13]

$$
w(x)=0.375 \frac{e_{31} V_{\mathrm{a}}}{E}\left(\frac{x}{t}\right)^{2}, \tag{43}
$$

![](./images/811037265772937217_3.jpg)

Fig. 2. Piezoelectric PVDF bimorph beam.

<table>
<caption>Table 1<br>Material properties of the main structure and piezoelectric</caption>
<thead>
<tr>
<th>Property</th>
<th>PVDF</th>
<th>Graphite/Epoxy</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{1}$</td>
<td>$0.2\,\text{E} + 10\,\text{N/m}^2$</td>
<td>$0.98\,\text{E} + 11\,\text{N/m}^2$</td>
</tr>
<tr>
<td>$E_{2}$</td>
<td>$0.2\,\text{E} + 10\,\text{N/m}^2$</td>
<td>$0.79\,\text{E} + 10\,\text{N/m}^2$</td>
</tr>
<tr>
<td>$G_{12}$</td>
<td>$0.775\,\text{E} + 9\,\text{N/m}^2$</td>
<td>$0.56\,\text{E} + 10\,\text{N/m}^2$</td>
</tr>
<tr>
<td>$v_{12}$</td>
<td>$0.29$</td>
<td>$0.29$</td>
</tr>
<tr>
<td>$v_{21}$</td>
<td>$0.28$</td>
<td>$0.28$</td>
</tr>
<tr>
<td>$\rho$</td>
<td>$1800\,\text{kg/m}^3$</td>
<td>$1520\,\text{kg/m}^3$</td>
</tr>
<tr>
<td>$e_{31}$</td>
<td>$0.046\,\text{c/m}^2$</td>
<td>$0.0$</td>
</tr>
<tr>
<td>$e_{32}$</td>
<td>$0.046\,\text{c/m}^2$</td>
<td>$0.0$</td>
</tr>
<tr>
<td>$e_{33}$</td>
<td>$0.0$</td>
<td>$0.0$</td>
</tr>
<tr>
<td>$\varepsilon_{11}$</td>
<td>$0.1062\,\text{E} - 9\,\text{F/m}$</td>
<td>$0.0$</td>
</tr>
<tr>
<td>$\varepsilon_{22}$</td>
<td>$0.1062\,\text{E} - 9\,\text{F/m}$</td>
<td>$0.0$</td>
</tr>
<tr>
<td>$\varepsilon_{33}$</td>
<td>$0.1062\,\text{E} - 9\,\text{F/m}$</td>
<td>$0.0$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2
Deflection of the PVDF bimorph beam (for a unit voltage) (m)</caption>
<thead>
<tr>
<th>Distance
(mm)</th>
<th>Method
Theory</th>
<th>Tseng [7]</th>
<th>Present</th>
</tr>
</thead>
<tbody>
<tr>
<td>20</td>
<td>0.0140 E − 06</td>
<td>0.0150 E − 06</td>
<td>0.0139 E − 06</td>
</tr>
<tr>
<td>40</td>
<td>0.0552 E − 06</td>
<td>0.0569 E − 06</td>
<td>0.0547 E − 06</td>
</tr>
<tr>
<td>60</td>
<td>0.1224 E − 06</td>
<td>0.1371 E − 06</td>
<td>0.1135 E − 06</td>
</tr>
<tr>
<td>80</td>
<td>0.2208 E − 06</td>
<td>0.2351 E − 06</td>
<td>0.2198 E − 06</td>
</tr>
<tr>
<td>100</td>
<td>0.3451 E − 06</td>
<td>0.3598 E − 06</td>
<td>0.3416 E − 06</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3
Tip deflection of the PVDF bimorph beam (for various voltage) (m)</caption>
<thead>
<tr>
<th>Voltage
(V)</th>
<th>Method
Theory</th>
<th>Tseng [7]</th>
<th>Present</th>
</tr>
</thead>
<tbody>
<tr>
<td>50</td>
<td>0.1725 E − 04</td>
<td>0.1670 E − 04</td>
<td>0.1755 E − 04</td>
</tr>
<tr>
<td>100</td>
<td>0.3451 E − 04</td>
<td>0.3200 E − 04</td>
<td>0.3409 E − 04</td>
</tr>
<tr>
<td>150</td>
<td>0.5175 E − 04</td>
<td>0.4897 E − 04</td>
<td>0.5067 E − 04</td>
</tr>
<tr>
<td>200</td>
<td>0.6900 E − 04</td>
<td>0.6417 E − 04</td>
<td>0.6819 E − 04</td>
</tr>
</tbody>
</table>

where $E$ is Young's modulus, and $V_a$ is the applied voltage, and $t$ is the thickness of the beam. The finite element solution can be obtained by solving Eq. (37).

When a unit voltage is applied across the thickness the deflections at the nodes are calculated by the finite element method presented in this paper. The deflection of the beam is calculated for various applied voltage between 0 and 200 V. The results are shown in Tables 2 and 3. The calculated deflections in the work of Tseng [7] and theoretical solution are also listed in Tables 2 and 3. The results show the close agreement between theoretical and the present finite element solutions, and the accuracy of the present finite element solution is higher than that of Tseng's [7]. The total number of degrees of freedom used in this analysis is compared in Table 4 with that in Tseng's, showing that the present finite element formulation with plate element for the intelligent structure saves much memory and computation times.

### 5.2. Static shape control

Consider a plate containing distributed piezoelectric materials on both upper and bottom surfaces as shown in Fig. 3. All material properties used are given in Table 1. The plate was originally flat and was simply supported along two parallel edges and free on other two edges.

Due to the force the plate deformed into a curved shape. The deformed configuration of the plate resulting from the applied force was plotted along the central line of the plate and is shown in Fig. 4.

The problem is studied in two cases. The first case is that all piezoelectric in the plate is considered as the actuators, and the second case is that piezoelectric of the bottom layer is considered as the sensors to sense the strain and to generate electrical potential and piezoelectric of the top layer as the actuators to control the shape of the structure.

<table>
<caption>Table 4 Comparison of problem size</caption>
<thead>
<tr>
<th>Method</th>
<th>Node no.</th>
<th colspan="3">D.O.F.</th>
</tr>
<tr>
<th></th>
<th></th>
<th>Structural</th>
<th>Electric</th>
<th>Total</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tseng [7]</td>
<td>36</td>
<td>108</td>
<td>36</td>
<td>144</td>
</tr>
<tr>
<td>Present</td>
<td>12</td>
<td>36</td>
<td>12</td>
<td>48</td>
</tr>
</tbody>
</table>

![](./images/811037265772937217_4.jpg)

Fig. 3. A plate with piezoelectric S/As.

![](./images/811037265772937217_5.jpg)

Fig. 4. Change of the deflection of the plate for passive control.

![](./images/811037265772937217_6.jpg)

Fig. 5. Change of the deflection of the plate for active control.

In the first case, the passive control is required. The numerical simulation was to determine the amount of the electrical potential applied to the piezoelectric, which makes the shape of the plate reach the desired shape. The solution indicated that by applying 110 V voltage to all piezoelectric the entire deformation shape of the plate was nearly flat.

In the second case, the intelligent structure can be formed a active static shape control system by implementing the feedback control law on a feedback circuit. The feedback gain that made the shape of the structure reach the desired shape was determined by our finite element method. Calculated results are illustrated in Fig. 5.

### 6. Conclusions

A finite element formulation for the plate with distributed piezoelectric S/As is presented. A new piezoelectric plate element is developed. This new piezoelectric plate element saves memory and computation time compared with previous works. Based on the new plate element, a general method was developed for the static shape control of the intelligent structure. Finite element analysis of the model verifies that the method can provide a close fit to any desired shape. The input voltage and feedback gain making the shape of the intelligent structure reach the desired shape can be obtained by the present method.

From this study it is believed that the computer code based on a finite element formulation could be further developed as a design tool for designing large-scale structure containing distributed piezoelectric S/As.

### Acknowledgements

This work is supported by the National Natural Science Foundation of China.

### References

[1] S.L. Venneri and B.K. Wada, "Overview of NASA's adaptive structures program", *44th Congr. of The International Astronautical Federation*, Australia, pp. 23-34, 1993.

[2] B.K. Wada, *Adaptive Structure*, ASME, New York, pp. 1-8, 1989.

[3] T. Bailey and J.E. Hubbard, "Distributed piezoelectric polymer active vibration control of a cantilever beam", *J. Guidance Control Dynamics* **5** (3), pp. 606-610, 1985.

[4] J.M. Plump and Hubbard, "Nonlinear control of a distributed systems: simulation and experimental results", *J. Dynamic Syst. Measurement Control* **109**, pp. 133-139, 1987.

[5] J.L. Crawly, "Use of piezoelectric actuators as element of intelligent structure", *AIAA J.* **25** (10), pp. 1373-1385. 1987.

[6] J.L. Crawly and K.B. Lazarus, "Induced strain actuation of isotropic and anisotropic plates", *AIAA J.* **29** (6), pp. 944-951, 1991.

[7] C.I. Tseng, Electromechanical dynamics of a coupled piezoelectric/mechanical system applied to vibration control and distributed sensing, Ph.D. Dissertation, Univ. of Kentucky, Lexington, Ky. July, 1989.

[8] H.S. Tzou and C.I. Tseng, "Distributed piezoelectric sensor/actuation design for dynamic measurement/control of distributed systems: a piezoelectric finite element approach", *J. Sound Vib.* **138** (1), pp. 17-34, 1990.

[9] S.K. Ha and C. Keilers, "Finite element analysis of composite structure containing distributed piezoelectric sensors and actuators", *AIAA J.* **30** (3), pp. 772-780, 1992.

[10] L.C. Chin, V. Varadan and K. Varadan, "Hybrid finite element formulation for piezoelectric arrays subjected to fluid loading", *Int. J. Numer. Methods Eng.* **37** (3), pp. 2987-3003, 1994.

[11] V.Z. Parton and B.A. Kudryavtsev, *Electromagnetoelasticity Piezoelectrics and Electrically Conductive Solids*, Gordon and Breach, Amsterdam, The Netherlands, 1988.

[12] S. Luo and G. Pan, "Arbitrary quadrilateral element of plate bending", *Comput. Struct. Mech. Appl. (China)* **2** (3), pp. 65-72, 1985.

[13] H.S. Tzou, "Development of a light-weight robot end-effector using polymeric piezoelectric bimorph", *Proc. 1989 IEEE Int. Conf. on Robotic and Automation*, Computer Society Press, Los Angles, pp. 1704-1709, 1989.

[14] W.S. Hwang and H.C. Park, "Finite element modeling of piezoelectric sensors and actuators", *AIAA J.* **31** (5), pp. 930-937, 1993.