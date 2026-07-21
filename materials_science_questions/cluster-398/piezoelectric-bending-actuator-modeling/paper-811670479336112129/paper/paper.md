International Scholarly Research Network
ISRN Mechanical Engineering
Volume 2011, Article ID 362030, 11 pages
doi:10.5402/2011/362030

# Research Article

## Thermal Buckling of Piezoelectric Composite Beam

S. Yazdani, $^{1}$ Y. Kiani, $^{2}$ M. Jabbari, $^{1}$ and M. R. Eslami $^{3}$

$^{1}$ ME Department, Islamic Azad Universit, South Tehran Branch, Tehran, Iran
$^{2}$ ME Department, Amirkabir University of Technology, Tehran, Iran
$^{3}$ Academy of Sciences, ME Department, Amirkabir University of Technology, Tehran, Iran

Correspondence should be addressed to M. R. Eslami, eslami@aut.ac.ir

Received 12 January 2011; Accepted 6 February 2011

Academic Editors: A. Combescure, A. Postelnicu, A. Z. Sahin, K. Yasuda, and D. Zhou

Copyright © 2011 S. Yazdani et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Buckling analysis of laminated composite beams with piezoelectric layers subjected to thermal loading and constant voltage is studied. The material properties are assumed to be homogeneous in any layer through the beam thickness. The first-order beam theory and nonlinear strain-displacement relation are used to obtain the governing equations of the composite beam. The beam is assumed under uniform type of thermal loading and various types of boundary conditions. For each case of boundary conditions, closed-form solutions are obtained. The effects of the applied actuator voltage, beam geometry, and boundary conditions on the buckling temperature are investigated.

## 1. Introduction

Static and dynamic analysis for multilayer composite structures have been well established for various engineering applications during the last decades. Brush and Almroth [1] have a general treatment on the subject of structural stability, including beams, plates, and shells. Wang et al. [2] presented the closed-form solutions for buckling of beams, plates, and shells based on the classical, first-order, and higher-order displacement theories under compressive loads. Eslami and Shariyat [3, 4] used the improved equations to obtain the elastic, plastic, and creep buckling of thin cylindrical shells under different mechanical loading conditions. Analytical solutions of refined beam theories are developed to study the buckling behavior of cross-ply rectangular beams with arbitrary boundary conditions [5]. Kolakowski et al. [6] presented a modal interactive buckling of thin-walled composite beam columns regarding distortional deformations. Buckling analysis of cross-ply laminated beams with general boundary conditions by Ritz method is studied by Aydogdu [7].

If the membrane stresses due to a temperature distribution in a composite laminate are compressive and sufficiently large, equilibrium may become unstable, and thermal buckling may occur. In recent years, many studies have focused on the analysis of the thermal buckling and postbuckling responses of composite laminates. Eslami et al. [8] obtained the thermoelastic buckling of thin cylindrical shells under a number of practical thermal loadings. Shear deformation effects on thermal buckling of cross-ply composite laminates have been studied by Mannini [9]. In this paper, thermal buckling of symmetric and antisymmetric cross-ply composite laminates is investigated. The first-order shear deformation theory in conjunction with the Rayleigh-Ritz method is used for the evaluation of the thermal buckling parameters of structures.

Jordan canonical form solution for thermally induced deformation of cross-ply laminated composite beams has been presented by Khdeir and Reddy [10]. Also, Khdeir [11] studied the thermal buckling of thick, moderately thick, and thin cross-ply laminated beams subjected to uniform temperature distribution. He presented the exact analytical solutions of refined beam theories to obtain the critical buckling temperature of cross-ply beams with various boundary conditions. Li and Song [12] studied the large thermal deflections of Timoshenko beams under transversely nonuniform temperature rise. Thermal buckling analysis of cross-ply laminated composite beams with general boundary conditions is presented by Aydogdu [13]. The study is concerned with the thermal buckling analysis of cross-ply laminated beams

subjected to different sets of boundary conditions. The anal- ysis is based on a three-degrees-of-freedom shear deformable beam theory. The governing equations are obtained by means of the minimum energy principle. Thermal buckling load optimization of angle-ply symmetrically laminated composite beams is studied by Topal [14]. The objective of the optimization problem is to maximize the critical thermal buckling load of the laminated beams, and the fibre orientation is considered as the design variable.

Advanced structures with integrated self-monitoring and control capabilities are increasingly becoming important due to the rapid development of smart structure and mechanical systems. Bailey and Hubbard [15] reported vibration control of a piezoelectric beam with a simplified beam model. Recently, discrete layer theories are utilized for the analysis of composite structures with piezoelectrics in order to fully consider the effects of the transverse shear and variable in- plane displacements [16]. Tzou et al. [17, 18] proposed the mathematical modelling of nonlinear thermopiezoelastic laminates and investigated the static and dynamic control of beams and plates. Abramovich [19] presented the closed- form solutions for deflection control of laminated composite beams with piezoceramic layers. In his study, the three coupled equations of motion of a general nonsymmetric piezolaminated composite beam subjected to axial and lateral traction, and its corresponding boundary conditions are derived using a variational approach. The static shape control is performed using either continuous piezoceramic layers or patches embedded or bonded to the surface of the beam structure. Closed-form solutions for the bending angle and the axial lateral displacements along the beam are presented for various configurations of layup, boundary conditions, and mechanical loading. Waisman and Abramovich [20] studied the active stiffening of laminated composite beams using piezoelectric actuators. The present study deals with the stiffening effects of a smart piezolaminated composite beam. The structure consists of piezoceramic layers or patches bonded on the surface of the beam. The analysis considers the linear piezoelectric constitutive relations and the first-order shear deformation theory. Aldraihem and Khdeir [21, 22] presented the exact deflection solutions of beams with shear piezoelectric patches and actuators. Jerome and Ganesan [23] developed a generalized plane strain finite element formulation to predict the critical buckling voltage and temperature of a piezo composite beam. Akhras and Li [24] proposed the three-dimensional thermal buckling analysis of piezoelectric antisymmetric angle-ply laminates using finite layer method.

In this paper, the thermal buckling of piezoelectric lam- inated composite beams is studied. The first-order shear deformation beam theory is employed, and the closed- form solutions are presented for different types of boundary conditions.

## 2. Formulation of Problem

Consider a laminated composite beam with length $L$, width $c$, and total thickness $h$. The rectangular Cartesian coordinates
![](./images/811670479336112129_1.jpg)

**Figure 1:** Geometry of cross-ply composite beam.

is used such that the $x$ axis is along the length of the beam on its middle surface and $z$ is measured from the middle surface and is positive upward, as shown in Figure 1. The analysis is based on the first-order beam theory. The displacement field for the beam is $\overline{u}$ and $\overline{w}$, which is based on Timoshenko beam theory, can be written as
$$
\begin{aligned}
\overline{u}(x, z) & =u(x)+z \phi(x), \\
\overline{w}(x, z) & =w(x),
\end{aligned}
\tag{1}
$$
where $u$ and $w$ are the axial and lateral displacements of a point on the midplane and $\phi$ is the bending rotation of the normal to the mid plane. The normal strain $\varepsilon_{x}$ and the transverse shear strain $\gamma_{x z}$ at any point in the laminate are
$$
\begin{aligned}
\varepsilon_{x} & =\frac{\partial \overline{u}}{\partial x}+\frac{1}{2}\left(\frac{\partial \overline{w}}{\partial x}\right)^{2}=u^{\prime}+\frac{1}{2} w^{\prime 2}+z \phi^{\prime}, \\
\gamma_{x z} & =\frac{\partial \overline{u}}{\partial z}+\frac{\partial \overline{w}}{\partial x}=\phi+w^{\prime},
\end{aligned}
\tag{2}
$$
where a $'$ stands for a derivation respect to $x$. When piezo composite beam is subjected to thermal load, the force and moment equations are written as [11, 19]
$$
\left[\begin{array}{c}
N_{x} \\
M_{x} \\
Q_{x z}
\end{array}\right]=\left[\begin{array}{ccc}
A_{11} & B_{11} & 0 \\
B_{11} & D_{11} & 0 \\
0 & 0 & A_{55}
\end{array}\right]\left[\begin{array}{c}
u^{\prime}+\frac{1}{2} w^{\prime 2} \\
\phi^{\prime} \\
\phi+w^{\prime}
\end{array}\right]-\left[\begin{array}{c}
N^{T} \\
M^{T} \\
0
\end{array}\right]-\left[\begin{array}{c}
N^{E} \\
M^{E} \\
0
\end{array}\right],
\tag{3}
$$
where in this equation
$$
\begin{gathered}
N_{x}=\int_{-h / 2}^{h / 2} c \sigma_{x} d z, \quad M_{x}=\int_{-h / 2}^{h / 2} c \sigma_{x} z d z, \\
Q_{x z}=\int_{-h / 2}^{h / 2} c \tau_{x z} d z,
\end{gathered}
\tag{4}
$$
$\sigma_{x}$ and $\tau_{x z}$ being the normal and shear stresses, respectively. Thermal force and thermal moment are
$$
\begin{aligned}
& N^{T}=c \sum_{n=1}^{N} \int_{z_{n-1}}^{z_{n}} Q_{11}^{n} \alpha_{x}^{n} \Delta T d z, \\
& M^{T}=c \sum_{n=1}^{N} \int_{z_{n-1}}^{z_{n}} Q_{11}^{n} \alpha_{x}^{n} \Delta T z d z.
\end{aligned}
\tag{5}
$$

Here, $N$ is the number of layers and $\alpha_x$ is the axial coefficient of thermal expansion. Terms $N^E$ and $M^E$ are the piezoelectric force and moment and are

$$
\begin{aligned}
N^{E} &= c \sum_{n=1}^{N_{a}}\left(Q_{11}\right)_{a}^{n} V^{n} d_{31}^{n}, \\
M^{E} &= \frac{c}{2} \sum_{n=1}^{N_{a}}\left(Q_{11}\right)_{a}^{n} V^{n} d_{31}^{n}\left(2 z_{a}^{n}+h_{a}^{n}\right).
\end{aligned}
\tag{6}
$$

A subscript $a$ stands for quantities associated with piezoelectric layers. Here, $V^n$ is the applied actuator voltage to the surface of $n$th piezoelectric layer nsd $d_{31}$ is the piezoelectric constant. Also, $A_{11}$, $B_{11}$, $D_{11}$, and $A_{55}$ are the usual extensional, bending-extension, bending, and transverse shear stiffness coefficients defined as

$$
\begin{aligned}
A_{11} &=c \int_{-h / 2}^{h / 2} \overline{Q}_{11} d z=c \sum_{n=1}^{N}\left(\overline{Q}_{11}\right)^{n}\left(z_{n+1}-z_{n}\right), \\
B_{11} &=c \int_{-h / 2}^{h / 2} \overline{Q}_{11} z d z=\frac{c}{2} \sum_{n=1}^{N}\left(\overline{Q}_{11}\right)^{n}\left(z_{n+1}^{2}-z_{n}^{2}\right), \\
D_{11} &=c \int_{-h / 2}^{h / 2} \overline{Q}_{11} z^{2} d z=\frac{c}{3} \sum_{n=1}^{N}\left(\overline{Q}_{11}\right)^{n}\left(z_{n+1}^{3}-z_{n}^{3}\right), \\
A_{55} &=c k \int_{-h / 2}^{h / 2} \overline{Q}_{55} z d z=c k \sum_{n=1}^{N}\left(\overline{Q}_{55}\right)^{n}\left(z_{n+1}-z_{n}\right),
\end{aligned}
\tag{7}
$$

where $N$ is the number of layers, $k$ is a shear correction factor, and $\overline{Q}_{11}$ and $\overline{Q}_{55}$ are the transformed material constants given by

$$
\begin{aligned}
\overline{Q}_{11}=Q_{11} \cos ^{4} \theta+Q_{22} \sin ^{4} \theta+2\left(Q_{12}+2 Q_{66}\right) \sin ^{2} \theta \cos ^{2} \theta, \\
\overline{Q}_{55}=G_{13} \cos ^{2} \theta+G_{23} \sin ^{2} \theta.
\end{aligned}
\tag{8}
$$

The angle $\theta$ is the angle between the fibre direction and longitudinal axis ($x$ axis) of the beam, and the constants $Q_{11}$, $Q_{12}$, $Q_{22}$, and $Q_{66}$ are

$$
\begin{aligned}
Q_{11} &=\frac{E_{11}}{1-\nu_{12} \nu_{21}}, \\
Q_{22} &=\frac{E_{22}}{1-\nu_{12} \nu_{21}}, \\
Q_{12} &=\frac{E_{11} \nu_{12}}{1-\nu_{12} \nu_{21}}, \\
Q_{66} &=G_{12}.
\end{aligned}
\tag{9}
$$

Using the principle of minimum total potential energy, the governing equations for the displacement field of (1) are derived in [1, 11, 19] as

$$
\begin{aligned}
\frac{d N_{x}}{d x} &=0, \\
\frac{d M_{x}}{d x}-Q_{x z} &=0, \\
\frac{d Q_{x z}}{d x}+N_{x} \frac{d^{2} w}{d x^{2}} &=0.
\end{aligned}
\tag{10}
$$

In this paper, it is assumed that the thermal load is uniform. The equilibrium equations in terms of the displacement components are obtained by substituting (3) into (10)

$$
\begin{aligned}
A_{11}\left(u^{\prime \prime}+w^{\prime} w^{\prime \prime}\right)+B_{11} \phi^{\prime \prime} &=0, \\
B_{11}\left(u^{\prime \prime}+w^{\prime} w^{\prime \prime}\right)+D_{11} \phi^{\prime \prime}-A_{55}\left(\phi+w^{\prime}\right) &=0, \\
A_{55}\left(\phi^{\prime}+w^{\prime \prime}\right)+N_{x} w^{\prime \prime} &=0.
\end{aligned}
\tag{11}
$$

### 3. Prebuckling Deformation

The flat prebuckling configurations are assumed. For this purpose, the prebuckling deformation of laminated composite beam should be studied to assure that the beam remains flat under uniform thermal loading. The deformation of a beam prior to buckling may be obtained by solving the equilibrium equations (11) with the nonlinear terms set equal to zero [11]

$$
\begin{aligned}
A_{11} u^{\prime \prime}+B_{11} \phi^{\prime \prime} &=0, \\
B_{11} u^{\prime \prime}+D_{11} \phi^{\prime \prime}-A_{55}\left(\phi+w^{\prime}\right) &=0, \\
A_{55}\left(\phi^{\prime}+w^{\prime \prime}\right) &=0.
\end{aligned}
\tag{12}
$$

Solving these equations, we obtain

$$
\begin{gathered}
u=\frac{B_{11}}{A_{11}} \frac{A_{55}}{\left(\left(B_{11}^{2} / A_{11}\right)-D_{11}\right)} b_{1} \frac{x^{2}}{2}+b_{5} x+b_{6}, \\
w=\frac{A_{55}}{\left(\left(B_{11}^{2} / A_{11}\right)-D_{11}\right)} b_{1} \frac{x^{3}}{6}+b_{2} \frac{x^{2}}{2}+b_{3} x+b_{4}, \\
\phi=-\frac{A_{55}}{\left(\left(B_{11}^{2} / A_{11}\right)-D_{11}\right)} b_{1} \frac{x^{2}}{2}-b_{2} x+b_{3}+b_{1}, \\
N_{x}=A_{11} b_{5}-B_{11} b_{2}-N^{T}-N^{E}, \\
M_{x}=A_{55} b_{1} x+B_{11} b_{5}-D_{11} b_{2}-M^{T}-M^{E}, \\
Q_{x z}=A_{55} b_{1},
\end{gathered}
\tag{13}
$$

where $b_1$ to $b_6$ are constants which have to be determined using the associated boundary conditions. The prebuckling boundary conditions are listed in Table 1. For each case of

<table><thead><tr><td><b>B.C.</b></td><td><b>B.Cs at$x=0$</b></td><td><b>B.Cs at$x=L$</b></td></tr></thead><tbody><tr><td><b>S-S</b></td><td><b>$u=w=M_{x}=0$</b></td><td><b>$u=w=M_{x}=0$</b></td></tr><tr><td><b>C-C</b></td><td><b>$u=w=ϕ=0$</b></td><td><b>$u=w=ϕ=0$</b></td></tr><tr><td><b>C-S</b></td><td><b>$u=w=ϕ=0$</b></td><td><b>$u=w=M_{x}=0$</b></td></tr><tr><td><b>C-R</b></td><td><b>$u=w=ϕ=0$</b></td><td><b>$u=ϕ=\frac {dM_{x}}{dx}=0$</b></td></tr><tr><td><b>S-R</b></td><td><b>$u=w=M_{x}=0$</b></td><td><b>$u=ϕ=\frac {dM_{x}}{dx}=0$</b></td></tr></tbody></table>

**Table 1:** Prebuckling boundary conditions for various edge supports. ($C$ indicates clamped, $S$ shows simply supported and $R$ is used for roller edge.)

boundary conditions, constants $b_1$ to $b_6$ have been evaluated and listed in Table 2,

$$
\begin{aligned}
I &= \frac{A_{55}}{\left(B_{11}^{2}/A_{11}\right)-D_{11}}, \\
G &= A_{55}L - \frac{B_{11}^{2}}{A_{11}}I\frac{L}{2} + D_{11}\frac{1+I(L^{2}/6)}{L/2}.
\end{aligned} \tag{14}
$$

From this table, one may obtain that except the *Clamped-Clamped* and *Clamped-Roller* laminated composite beams, the other types of boundary conditions under thermal loading initially start to deflect rather than buckling. But the $C$-$C$ and $C$-$R$ boundary condition follow the bifurcation type buckling for uniform temperature rise loading.

## 4. Stability Equations

To derive the stability equations, the adjacent-equilibrium criterion is used. Assume that the equilibrium state of a laminated composite beam is defined in terms of the displacement components $u_0$, $w_0$, and $\phi_0$ and the displacement components of a neighboring stable state differ by $u_1$, $w_1$, and $\phi_1$ with respect to the equilibrium position. Thus, the total displacements of a neighboring state are [1]

$$
\begin{aligned}
u &= u_0 + u_1, \\
w &= w_0 + w_1, \\
\phi &= \phi_0 + \phi_1.
\end{aligned} \tag{15}
$$

Similar to the displacements, the force and moment of a neighboring state may be related to the state of equilibrium as

$$
\begin{aligned}
N_x &= N_{x0} + N_{x1}, \\
M_x &= M_{x0} + M_{x1}, \\
Q_{xz} &= Q_{xz0} + Q_{xz1}.
\end{aligned} \tag{16}
$$

Here, $N_{x1}$, $M_{x1}$, and $Q_{xz1}$ represent the linear parts of the force and moment increments corresponding to $u_1$, $w_1$, and $\phi_1$. The stability equations may be obtained by substituting (15) and (16) in (3). Upon substitution, the terms in the resulting equations with subscript 0 satisfy the equilibrium conditions and, therefore, drop out of the equations. The remaining terms form the stability equations as

$$
\begin{aligned}
\frac{dN_{x1}}{dx} &= 0, \\
\frac{dM_{x1}}{dx} - Q_{xz1} &= 0, \\
\frac{dQ_{xz1}}{dx} + N_{x0}\frac{d^2w_1}{dx^2} &= 0.
\end{aligned} \tag{17}
$$

Using (3) and (15), the force and moment with subscript 1 may be defined by

$$
\begin{aligned}
N_{x1} &= A_{11}u_1' + B_{11}\phi_1', \\
M_{x1} &= B_{11}u_1' + D_{11}\phi_1', \\
Q_{xz1} &= A_{55}(\phi_1 + w_1').
\end{aligned} \tag{18}
$$

For $C$-$C$ and $C$-$R$ composite beam subjected to uniform temperature rise, one may obtain

$$
\begin{aligned}
N_{x0} &= -N^T - N^E, \\
M_{x0} &= -M^T - M^E.
\end{aligned} \tag{19}
$$

Combining (17) and (18) by eliminating $u_1$ and $\phi_1$ provides an ordinary differential equation in terms of $w_1$, which is the stability equation of composite beam under thermal loading

$$
\frac{d^4w_1}{dx^4} + \mu^2\frac{d^2w_1}{dx^2} = 0, \tag{20}
$$

with

$$
\mu^2 = \frac{-N_{x0}}{\left(D_{11} - \left(B_{11}^{2}/A_{11}\right)\right)\left(1 + (N_{x0}/A_{55})\right)}. \tag{21}
$$

When the temperature distribution in composite beam is uniform, the parameter $\mu$ is constant, and then the exact solution of (20) is

$$
w_1(x) = C_1\sin(\mu x) + C_2\cos(\mu x) + C_3x + C_4. \tag{22}
$$

<table><thead><tr><th>B.C.</th><th>$b_1$</th><th>$b_2$</th><th>$b_3$</th><th>$b_4$</th><th>$b_5$</th><th>$b_6$</th></tr></thead><tbody><tr><td>C-C</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td></tr><tr><td>C-R</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td></tr><tr><td>C-S</td><td>$\frac{M^T}{G}$</td><td>$\frac{2}{L}\left(1+I\frac{L^2}{6}\right)\frac{M^T+M^E}{G}$</td><td>$\frac{M^T+M^E}{G}$</td><td>$0$</td><td>$-\frac{B_{11}}{A_{11}}I\frac{M^T+M^E}{G}\frac{L}{2}$</td><td>$0$</td></tr><tr><td>S-R</td><td>$0$</td><td>$-\frac{M^T+M^E}{D_{11}}$</td><td>$-\frac{M^T+M^E}{D_{11}}L$</td><td>$0$</td><td>$0$</td><td>$0$</td></tr><tr><td>S-S</td><td>$0$</td><td>$-\frac{M^T+M^E}{D_{11}}$</td><td>$\frac{M^T+M^E}{D_{11}}\frac{L}{2}$</td><td>$0$</td><td>$0$</td><td>$0$</td></tr></tbody></table>

Using (17), (18), and (22), the expressions for $u_1$, $\phi_1$, and $N_{x1}, M_{x1}, Q_{xz1}$ become

$$
\begin{aligned}
u_1(x) =& \frac{B_{11}}{A_{11}}\left(1 - \frac{\mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}{A_{55} + \mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}\right) \\
& \times \mu\left(C_1\cos(\mu x) - C_2\sin(\mu x)\right) + C_5x + C_6,
\end{aligned} \tag{23}
$$

$$
\begin{aligned}
\phi_1(x) =& \left(1 - \frac{\mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}{A_{55} + \mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}\right) \\
& \times \mu\left(-C_1\cos(\mu x) + C_2\sin(\mu x)\right) - C_3,
\end{aligned} \tag{24}
$$

$$
N_{x1}(x) = A_{11}C_5,
$$

$$
\begin{aligned}
M_{x1}(x) =& \left(D_{11} - \frac{B_{11}^2}{A_{11}}\right)\left(1 - \frac{\mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}{A_{55} + \mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}\right) \\
& \times \mu^2\left(C_1\cos(\mu x) + C_2\sin(\mu x)\right) + B_{11}C_5,
\end{aligned}
$$

$$
\begin{aligned}
Q_{xz1}(x) =& \left(\frac{\mu^3\left(D_{11} - (B_{11}^2/A_{11})\right)}{1 + (\mu^2/A_{55})\left(D_{11} - (B_{11}^2/A_{11})\right)}\right) \\
& \times \left(C_1\cos(\mu x) - C_2\sin(\mu x)\right).
\end{aligned} \tag{25}
$$

Constants of these equations ($C_1$ to $C_6$) are obtained using the boundary conditions of the composite beam. To find the minimum value of $N_{x0}$ associated with the thermal buckling load, the parameter $\mu$ must be minimized. Five types of boundary conditions are assumed for the composite beam. Consider a beam with both edges clamped. The edge conditions of the clamped-clamped composite beam are

$$
u_1(0) = w_1(0) = \phi_1(0) = u_1(L) = w_1(L) = \phi_1(L) = 0. \tag{26}
$$

Using (22)-(24) and (26), the constants $C_1$ to $C_6$ must satisfy the system of equations

$$
\begin{gathered}
\begin{bmatrix}
0 & 1 & 0 & 1 & 0 & 0 \\
\sin(\mu L) & \cos(\mu L) & L & 1 & 0 & 0 \\
\frac{B_{11}}{A_{11}}P\mu & 0 & 0 & 0 & 0 & 1 \\
\frac{B_{11}}{A_{11}}P\mu\cos(\mu L) & -\frac{B_{11}}{A_{11}}P\mu\sin(\mu L) & 0 & 0 & L & 1 \\
-P\mu & 0 & -1 & 0 & 0 & 0 \\
-P\mu\cos(\mu L) & P\mu\sin(\mu L) & -1 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
C_1 \\
C_2 \\
C_3 \\
C_4 \\
C_5 \\
C_6
\end{bmatrix} \\
=
\begin{bmatrix}
0 \\
0 \\
0 \\
0 \\
0 \\
0
\end{bmatrix},
\end{gathered} \tag{27}
$$

where

$$
P = \left(1 - \frac{\mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}{A_{55} + \mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}\right). \tag{28}
$$

To have a nontrivial solution, the determinant of coefficient matrix must be zero, which yields

$$
P\mu L(2 - 2\cos(\mu L) + P\mu L\sin(\mu L)) = 0. \tag{29}
$$

The smallest positive value of $\mu$ which satisfies (29) is $\mu_{\text{min}} = 2\pi/L$. Table 3 shows different types of boundary conditions and the minimum values of $\mu$ associated with the thermal buckling loads. Now, the critical force for buckling from (21) (except for C-S beam, where the approximate solution from [2] is considered) is

$$
N_{x0} = -\frac{\mu^2\left(D_{11} - (B_{11}^2/A_{11})\right)}{1 + (\mu^2/A_{55})\left(D_{11} - (B_{11}^2/A_{11})\right)}. \tag{30}
$$

**Table 3:** Boundary conditions and minimum value of $\mu$ for various edge supports. (C indicates clamped, S shows simply supported, and R is used for roller edge).

<table>
  <thead>
    <tr>
      <th>B.C.</th>
      <th>B.Cs at $x=0$</th>
      <th>B.Cs at $x=L$</th>
      <th>$\mu_{min} \times L$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S-S</td>
      <td>$u_1 = w_1 = M_{x1} = 0$</td>
      <td>$u_1 = w_1 = M_{x1} = 0$</td>
      <td>$\pi$</td>
    </tr>
    <tr>
      <td>C-C</td>
      <td>$u_1 = w_1 = \phi_1 = 0$</td>
      <td>$u_1 = w_1 = \phi_1 = 0$</td>
      <td>$2\pi$</td>
    </tr>
    <tr>
      <td>C-S</td>
      <td>$u_1 = w_1 = \phi_1 = 0$</td>
      <td>$u_1 = w_1 = M_{x1} = 0$</td>
      <td>$4.49341$</td>
    </tr>
    <tr>
      <td>C-R</td>
      <td>$u_1 = w_1 = \phi_1 = 0$</td>
      <td>$u_1 = \frac{dw_1}{dx} = \frac{dM_{x1}}{dx} + N_{x0}\frac{dw_1}{dx} = 0$</td>
      <td>$\pi$</td>
    </tr>
    <tr>
      <td>S-R</td>
      <td>$u_1 = w_1 = M_{x1} = 0$</td>
      <td>$u_1 = \frac{dw_1}{dx} = \frac{dM_{x1}}{dx} + N_{x0}\frac{dw_1}{dx} = 0$</td>
      <td>$\frac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>

![](./images/811670479336112129_2.jpg)

**Figure 2:** Critical buckling temperatures for piezoelectric aluminium beams with various boundary conditions and various voltages.

![](./images/811670479336112129_3.jpg)

FIGURE 3: Critical buckling temperature for three layered cross-ply beams with various boundary conditions and various voltages.

Then with this equation and (19), the buckling force of the beam for all cases of boundary conditions can be written in the form

$$
N^{T}+N^{E}=\frac{\mu^{2}\left(D_{11}-\left(B_{11}^{2} / A_{11}\right)\right)}{1+\left(\mu^{2} / A_{55}\right)\left(D_{11}-\left(B_{11}^{2} / A_{11}\right)\right)}.\tag{31}
$$

## 5. Thermal Loading

Consider a beam under uniform temperature rise. That is, consider a beam at reference temperature $T_{0}$. The uniform temperature may be raised to $T_{0}+\Delta T$ such that the beam buckles. Substituting (5) and (6) into (31) gives

![](./images/811670479336112129_4.jpg)

FIGURE 4: Critical buckling temperature for antisymmetric four layered beam (0/90/0/90) with one piezoelectric layer on the top surface of the beam with various boundary conditions and various voltages.

![](./images/811670479336112129_5.jpg)

FIGURE 5: Critical buckling temperature for antisymmetric four layered beam (0/90/0/90) with two piezoelectric layers on the top and bottom surfaces of the beam with various boundary conditions.

**Table 4:** Effect of applied voltage on $\Delta T_{cr}$, (piezo aluminium beam).

<table>
  <thead>
    <tr>
      <th>Voltage (V)</th>
      <th>0</th>
      <th>200</th>
      <th>−200</th>
      <th>500</th>
      <th>−500</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S-S</td>
      <td>94.28291</td>
      <td>93.92787</td>
      <td>94.63797</td>
      <td>93.39529</td>
      <td>95.17054</td>
    </tr>
    <tr>
      <td>C-C</td>
      <td>370.19256</td>
      <td>369.83751</td>
      <td>370.54760</td>
      <td>369.30493</td>
      <td>371.08018</td>
    </tr>
    <tr>
      <td>C-S</td>
      <td>191.38436</td>
      <td>191.02931</td>
      <td>191.73940</td>
      <td>190.49673</td>
      <td>192.27198</td>
    </tr>
    <tr>
      <td>C-R</td>
      <td>94.28292</td>
      <td>93.927867</td>
      <td>94.63796</td>
      <td>93.39529</td>
      <td>95.17054</td>
    </tr>
    <tr>
      <td>S-R</td>
      <td>23.68170</td>
      <td>23.32666</td>
      <td>24.03675</td>
      <td>22.79408</td>
      <td>24.56932</td>
    </tr>
  </tbody>
</table>

![](./images/811670479336112129_6.jpg)

**Figure 6:** Difference between the buckling temperature for four layered antisymmetric beam (0/90/0/90) with one and two piezoelectric layers with various boundary conditions.

$$
\begin{aligned}
c\Delta T\sum_{n=1}^{N}\int_{z_{n-1}}^{z_{n}}Q_{11}^{n}\alpha_{x}^{n}dz & +c\sum_{n=1}^{N_{a}}(Q_{11})_{a}^{n}V^{n}d_{31}^{n} \\
& =\frac{\mu^{2}(D_{11}-(B_{11}^{2}/A_{11}))}{1+(\mu^{2}/A_{55})(D_{11}-(B_{11}^{2}/A_{11}))}.
\end{aligned}
\tag{32}
$$

## 6. Numerical Result and Discussions

In this section, various combinations of composite beams comprising piezoelectric layers are assumed. General boundary conditions are considered on both sides to determine the critical buckling temperatures.

### 6.1. Aluminium Beam.
Consider an aluminium beam with surface-bonded piezoelectric layers. we consider PZT-5A for piezoelectric layers. The beam thickness and length are $h = 0.01$ m and $L = 0.25$ m, and the actuator layer thickness is $h_{a} = 0.001$ m. The shear correction factor is $k = 5/6$. Young's modules, coefficient of thermal expansion, Poisson's ratio, and the shear modules for aluminum are $E = 72.4$ GPa, $\alpha = 22.5 \times 10^{-6}/^\circ\text{C}$, $\nu = 0.3$, and $G = 27.8$ GPa, respectively [25]. The PZT-5A properties are $E_{a} = 63$ GPa, $\alpha_{a} = 0.9 \times 10^{-6}/^\circ\text{C}$, $\nu_{12a} = 0.3$, $G_{a} = 24.2$ GPa, and $d_{31} = 2.54 \times 10^{-10}$ m/V [26]. Five electric loading cases are considered $V_{0} = 0, \pm 200$ V, $\pm 500$ V. Here, $V_{0} = 0$ V denotes a grounding condition. Figure 2 and Table 4 depict the critical buckling temperature for various types of boundary conditions, and various voltages subjected to the uniform temperature rise. Also, the critical buckling temperature for the S-S and C-R types of boundary conditions are equal and larger than the value related to the S-R beams but lower than C-C and C-S beams.

![](./images/811670479336112129_7.jpg)

**Figure 7:** Influence of thickness on the buckling temperature.

### 6.2. Glass-Epoxy Symmetric Beam.
Consider a three-layered cross-ply composite beam (0/90/0), with surface-bonded piezoelectric layers. Also, similar to the previous example, consider PZT-5A for piezoelectric layers. The beam thickness and length are $h = 0.0045$ m, and $L = 0.25$ m and the actuator layer thickness is $h_{a} = 0.001$ m. The shear correction factor is $k = 5/6$. It is assumed that the thickness and the material for all laminae are the same, (glass-epoxy) with the following characteristics [25]:

$$
\begin{gathered}
E_{11}=50 \mathrm{GPa}, \quad E_{22}=15.2 \mathrm{GPa}, \\
G_{12}=G_{13}=4.7 \mathrm{GPa}, \quad G_{23}=3.28 \mathrm{GPa}, \\
\alpha_{1}=6 \times 10^{-6} /{ }^{\circ} \mathrm{C}, \quad \alpha_{2}=\alpha_{3}=23.3 \times 10^{-6} /{ }^{\circ} \mathrm{C}, \\
\nu_{12}=\nu_{13}=0.254, \quad \nu_{23}=0.428 .
\end{gathered}
\tag{33}
$$

Figure 3 and Table 5 depict the critical buckling temperature for various types of boundary conditions and various voltages subjected to the uniform temperature rise. The critical buckling temperature for the S-S and C-R types of boundary conditions are equal and larger than the value related to the S-R beams, but lower than C-C and C-S beams.

### 6.3. Glass-Epoxy Antisymmetric Beam.
Consider an antisymmetric four-layered composite beam (0/90/0/90), with surface-bonded piezoelectric layers. Similar to the previous examples, consider PZT-5A for piezoelectric layers. The beam thickness and length are $h = 0.004$ m and $L = 0.25$ m, and the actuator layer thickness is $h_{a} = 0.001$ m. The shear correction factor is $k = 5/6$. The thickness and the material

**Table 5:** Effect of applied voltage on $\Delta T_{\text{cr}}$ (three-layered cross-ply composite beam).

| Voltage (V) | 0         | 200       | -200      | 500       | -500      |
|-------------|-----------|-----------|-----------|-----------|-----------|
| S-S         | 153.38994 | 149.04308 | 157.73679 | 142.52281 | 164.25707 |
| C-C         | 606.25793 | 601.91107 | 610.60478 | 595.39080 | 617.12506 |
| C-S         | 312.23341 | 307.88656 | 316.58027 | 301.36629 | 323.10054 |
| C-R         | 153.38994 | 149.04308 | 157.73679 | 142.52281 | 164.25707 |
| S-R         | 38.464062 | 34.117211 | 42.81091  | 27.59693  | 49.33119  |

**Table 6:** Effect of applied voltage on $\Delta T_{\text{cr}}$. (four-layered antisymmetric composite beam with one piezoelectric layer on the top surface of the beam).

| Voltage (V) | 0         | 200       | -200      | 500       | -500      |
|-------------|-----------|-----------|-----------|-----------|-----------|
| C-C         | 179.84154 | 177.55059 | 182.13249 | 174.11417 | 185.56892 |
| C-R         | 45.21492  | 42.92397  | 47.50587  | 39.48754  | 50.94230  |

**Table 7:** Effect of applied voltage on $\Delta T_{\text{cr}}$. (four-layered antisymmetric composite beam with two piezoelectric layers on top and bottom surfaces of the beam).

| Voltage (V) | 0         | 200       | -200      | 500       | -500      |
|-------------|-----------|-----------|-----------|-----------|-----------|
| C-C         | 448.83477 | 444.4855  | 453.22102 | 437.86920 | 459.80038 |
| C-R         | 113.24407 | 108.85784 | 117.63030 | 102.27848 | 124.20966 |

for all laminae are the same, (glass-epoxy), with material properties given in the previous example. In this example, we first consider one piezoelectric layer on the top surface of the beam, and then with two piezoelectric layers on the top and bottom surfaces of the beam.

Figures 4 and 5 and Tables 6 and 7 depict the critical buckling temperature for various types of boundary conditions and various voltages subjected to the uniform temperature rise. The critical buckling temperature for the $S$-$S$ and $C$-$R$ types of boundary conditions are equal and larger than the values related to the $S$-$R$ beams but lower than the $C$-$C$ and $C$-$S$ beams.

Figure 6 depicts the difference between the buckling temperature for the four-layered antisymmetric beam (0/90/0/90) with one and two piezoelectric layers with various boundary conditions.

The results show that for this type of piezoelectric layer, the buckling temperature decreases with the increase of the applied voltage and increases with the increase of applied voltage in opposite phase. The changes are, however, small. It should be mentioned that increasing or decreasing the buckling temperature by applying voltage in comparison with the grounding condition depends upon both the sign of applied voltage and the sign of the piezoelectric constant.

### 6.4. Influence of Geometry on Critical Buckling Temperature.
Consider three cross-ply composite beams with three layers (0/90/0) that are bonded with two piezoelectric layers on the top and bottom surfaces of the beams. The thickness of the beams are $h = 0.006$ m, $h = 0.0045$ m, and $h = 0.003$ m. The lengths of the beams are equal and is $L = 0.25$ m. The thickness and the material properties for all laminae are the same, (glass-epoxy), and the actuator layer is PZT-5A with thickness $h_a = 0.001$ m. The influence of beam geometry on the buckling temperature $\Delta T_{\text{cr}}$ for various types of boundary conditions under applied voltages is shown in Figure 7. As shown, when the thickness increases, the critical buckling temperature increases for various types of boundary conditions, as expected.

## 7. Conclusion
In this paper, the buckling analysis of composite beams with piezoelectric layers under various types of boundary conditions is investigated. Exact analytical solutions for the critical buckling temperature differences of beams are presented. The following are concluded.

(1) The buckling temperature difference for homogeneous, symmetric composite, and antisymmetric composite beams can be controlled by applying suitable voltage on the actuator layers, but the effect of this control voltage is small.

(2) For composite beams under uniform temperature rise, by increasing the beam thickness, the critical buckling temperature increases for any type of boundary conditions.

## References
[1] D. O. Brush and B. O. Almorth, *Buckling of Bars, Plates, and Shells*, McGraw-Hill, New York, NY, USA, 1975.

[2] C. M. Wang, C. Y. Wang, and J. N. Reddy, *Exact Solutions for Buckling of Structural Members*, CRC Press, Boca Raton, Fla, USA, 2004.

[3] M. R. Eslami and M. Shariyat, “Elasto-plastic buckling of cylindrical shells,” in *Proceedings of the ASME European Joint Conference on Engineering Systems Design and Analysis (ESDA ’92)*, Istanbul, Turkey, July 1992.

[4] M. R. Eslami and M. Shariyat, “Variational approach to elastic-plastic buckling of cylindrical shells,” in *Proceedings of the 7th International Conference on Pressure Vessel Technology*, Düsseldorf, Germany, 1992.

[5] A. A. Khdeir and J. N. Reddy, “Buckling of cross-ply laminated beams with arbitrary boundary conditions,” *Composite Structures*, vol. 37, no. 1, pp. 1–3, 1997.

[6] Z. Kolakowski, M. Krolak, and K. Kowal-Michalska, “Modal interactive buckling of thin-walled composite beam-columns regarding distortional deformations,” *International Journal of Engineering Science*, vol. 37, no. 12, pp. 1577–1596, 1999.

[7] M. Aydogdu, “Buckling analysis of cross-ply laminated beams with general boundary conditions by Ritz method,” *Composites Science and Technology*, vol. 66, no. 10, pp. 1248–1255, 2006.

[8] M. R. Eslami, A. R. Ziaii, and A. Ghorbanpour, “Thermoelastic buckling of thin cylindrical shells based on improved stability equations,” *Journal of Thermal Stresses*, vol. 19, no. 4, pp. 299–315, 1996.

[9] A. Mannini, "Shear deformation effects on thermal buckling of cross-ply composite laminates," *Composite Structures*, vol. 39, no. 1-2, pp. 1-10, 1997.

[10] A. A. Khdeir and J. N. Reddy, "Jordan canonical form solution for thermally induced deformations of cross-ply laminated composite beams," *Journal of Thermal Stresses*, vol. 22, no. 3, pp. 331-346, 1999.

[11] A. A. Khdeir, "Thermal buckling of cross-ply laminated composite beams," *Acta Mechanica*, vol. 149, no. 1-4, pp. 201-213, 2001.

[12] S. Li and X. I. Song, "Large thermal deflections of Timoshenko beams under transversely non-uniform temperature rise," *Mechanics Research Communications*, vol. 33, no. 1, pp. 84-92, 2006.

[13] M. Aydogdu, "Thermal buckling analysis of cross-ply lami- nated composite beams with general boundary conditions," *Composites Science and Technology*, vol. 67, no. 6, pp. 1096-1104, 2007.

[14] U. Topal, "Thermal buckling load optimization of laminated beams," in *Proceedings of the 5th International Advanced Technologies Symposium (IATS '09)*, Karabuk, Turkey, 2009.

[15] T. Bailey and J. E. Hubbard, "Distributed piezoelectric- polymer active vibration of a cantilever beam," *Journal of Guidance, Control, and Dynamics*, vol. 8, no. 5, pp. 605-611, 1985.

[16] D. H. Robbins and J. N. Reddy, "Analysis of piezoelectrically actuated beams using a layer-wise displacement theory," *Computers and Structures*, vol. 41, no. 2, pp. 265-279, 1991.

[17] H. S. Tzou and Y. H. Zhou, "Nonlinear piezothermoelasticity and multi-field actuations-part 2: control of nonlinear deflection, buckling and dynamics," *Journal of Vibration and Acoustics, Transactions of the ASME*, vol. 119, no. 3, pp. 382-389, 1997.

[18] Y. Bao, H. S. Tzou, and V. B. Venkayya, "Analysis of non- linear piezothermoelastic laminated beams with electric and temperature effects," *Journal of Sound and Vibration*, vol. 209, no. 3, pp. 505-518, 1998.

[19] H. Abramovich, "Deflection control of laminated composite beams with piezoceramic layers-closed form solutions," *Composite Structures*, vol. 43, no. 3, pp. 217-231, 1998.

[20] H. Waisman and H. Abramovich, "Active stiffening of laminated composite beams using piezoelectric actuators," *Composite Structures*, vol. 58, no. 1, pp. 109-120, 2002.

[21] O. J. Aldraihem and A. A. Khdeir, "Exact deflection solutions of beams with shear piezoelectric actuators," *International Journal of Solids and Structures*, vol. 40, no. 1, pp. 1-12, 2003.

[22] O. J. Aldraihem and A. A. Khdeir, "Precise deflection analysis of beams with piezoelectric patches," *Composite Structures*, vol. 60, no. 2, pp. 135-143, 2003.

[23] R. Jerome and N. Ganesan, "Generalized plane strain finite- element formulation for thermal and electrical buckling analysis of piezo composite beam," *Journal of Mechanics of Materials and Structures*, vol. 3, no. 9, 2008.

[24] G. Akhras and W. C. Li, "Three-dimensional thermal buckling analysis of piezoelectric antisymmetric angle-ply laminates using finite layer method," *Composite Structures*, vol. 92, no. 1, pp. 31-38, 2010.

[25] M. W. Hyer, *Stress Analysis of Fiber-Reinforced Composite Materials*, McGraw-Hill, New York, NY, USA, 1998.

[26] I. K. Oh, J. H. Han, and I. Lee, "Postbuckling and vibration characteristics of piezolaminated composite plate subject to thermo-piezoelectric loads," *Journal of Sound and Vibration*, vol. 233, no. 1, pp. 19-40, 2000.

Copyright of ISRN Mechanical Engineering is the property of International Scholarly Research Network and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.