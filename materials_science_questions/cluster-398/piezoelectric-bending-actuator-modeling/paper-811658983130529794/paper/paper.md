# Effect of Piezoelectricity on Nonlinear Free Vibration of Moderately Thick Laminated Piezoelectric Plates

Yufang Zheng $^{a}$ and Liqiong Deng $^{b}$

College of Civil Engineering, Fuzhou University, Fuzhou, 350108, P. R. China

$^{a}$ zheng_yufang@163.com, $^{b}$ dengliqiong@fzu.edu.cn

**Keywords:** piezoelectric effect, moderately thick, laminated plate, amplitude-frequency

**Abstract.** On the basis of laminated plate theory and piezoelectric theory, the nonlinear free vibration governing equations for symmetric cross-ply moderately thick laminated piezoelectric plates are established. The Galerkin procedure furnishes an infinite system of equations for time functions which are solved by the method of harmonic balance. In the numerical results, the influences of piezoelectric effect and various location of piezoelectric layer on the nonlinear vibrating frequency of the laminated piezoelectric plates are discussed.

## Introduction
Piezoelectric materials have received increased attention for applications in smart structure/materials systems. Tzou [1] studied the dynamic behavior and control of piezoelectric laminated circular plates with an initial nonlinear large deformation. Batra [2] presented the vibration of an elastic rectangular plate forced by piezoelectric actuators under time harmonic electric voltage. Gao[3] investigated the geometrically nonlinear transient vibration response and control of plates with piezoelectric patches. Jayakumar [4] studied the nonlinear free vibration of simply supported piezo-laminated rectangular plates with immovable edges utilizing Kirchoff's hypothesis and Von Karman strain-displacement relations. To author's work, Zheng [5] have studied the nonlinear dynamic stability of moderately thick laminated plates with piezoelectric layers. Although extensions studies have been made in vibrations of laminated piezoelectric composite structures, relatively, only a few works have been devoted to study the effect of piezoelectricity on moderately thick laminated piezoelectric plates.

In this present work, the nonlinear vibration of symmetric cross-ply moderately thick laminated piezoelectric plates is investigated. The nonlinear equations of motion for laminated plates are derived first, followed by using the Galerkin technique and harmonic balance method to analyze the nonlinear vibrating frequency. Numerical examples are provided for different parameters.

## Basic equations
Consider a symmetric cross-ply laminated piezoelectric rectangular plate, having length $a$ in the $x$ direction, width $b$ in the $y$ direction and thickness $h$ in the $z$ direction, which consists of $N$ plies, simply supported at four edges. Some of these layers are made of the PZT5 piezoelectric materials as actuators, while others are made of graphite-epoxy composite materials. The midsurface of the plate contains the $x,y$ axes and the origin of the coordinate system is taken at the upper left corner of the plate. According to the Timoshenko-Mindlin kinematic assumption, the nonlinear strain-displacement relations are as follows

$$
\begin{gathered}
\varepsilon_{x}=\varepsilon_{x}^{0}+z \kappa_{x}=u_{, x}+\frac{1}{2} w_{, x}^{2}+z \varphi_{, x}, \quad \varepsilon_{y}=\varepsilon_{y}^{0}+z \kappa_{y}=v_{, y}+\frac{1}{2} w_{, y}^{2}+z \psi_{, y}, \\
\gamma_{x y}=\gamma_{x y}^{0}+z \kappa_{x y}=u_{, y}+v_{, x}+w_{, x} w_{, y}+z\left(\varphi_{, y}+\psi_{, x}\right), \quad \gamma_{x z}=\varphi+w_{, x}, \quad \gamma_{y z}=\psi+w_{, y},
\end{gathered}
\tag{1}
$$

in which $u$, $v$ and $w$ are the displacement components on the middle surface at the $x$, $y$ and $z$ directions, and $\varphi$ and $\psi$ are rotation angles of the normal to the middle surface in the $xz$ and $yz$ planes, respectively. The comma indicates the partial derivative with respect to the coordinate variable.

For the laminated piezoelectric plate, let the piezoelectric layers be polarized along the $z$ direction. The constitutive equation for orthotropic piezoelectric materials can be expressed as
$$
\left\{\begin{array}{l}
\sigma_{x} \\
\sigma_{y} \\
\sigma_{x y}
\end{array}\right\}=\left[\begin{array}{ccc}
C_{11}^{p} & C_{12}^{p} & 0 \\
C_{12}^{p} & C_{22}^{p} & 0 \\
0 & 0 & C_{66}^{p}
\end{array}\right]\left\{\begin{array}{l}
\varepsilon_{x} \\
\varepsilon_{y} \\
\varepsilon_{x y}
\end{array}\right\}-\left\{\begin{array}{l}
e_{31} \\
e_{32} \\
0
\end{array}\right\} E_{z}, \quad \left\{\begin{array}{l}
\sigma_{x z} \\
\sigma_{y z}
\end{array}\right\}=\left[\begin{array}{cc}
C_{44}^{p} & 0 \\
0 & C_{55}^{p}
\end{array}\right]\left\{\begin{array}{l}
\gamma_{x z} \\
\gamma_{y z}
\end{array}\right\},
\tag{2}
$$
where $C_{i j}^{p}$ is the reduced stiffnesses of piezoelectric materials, $e_{31}$ and $e_{32}$ are the piezoelectric stress constants, and $E_{Z}$ is the electric field intensity, which can be expressed using the applied excitation voltage $V_{k}$ and the thickness $h_{k}$ of the piezoelectric layer, that is $E_{Z}=V_{k} / h_{k}$.

For the constitutive relationship of elastic layers, only taking
$$
e_{31}=e_{32}=0, \quad C_{i j}^{p}=C_{i j}^{e}.
$$

Neglecting the effects of in-plane inertia, rotary inertia and coupled normal-rotary inertia, the nonlinear equilibrium equations for moderately thick laminated plates are [6]
$$
\begin{gathered}
N_{x, x}+N_{x y, y}=0, \quad N_{x y, x}+N_{y, y}=0, \\
Q_{x, x}+Q_{y, y}+\left[N_{x} w_{, x}+N_{x y} w_{, y}\right]_{, x}+\left[N_{x y} w_{, x}+N_{y} w_{, y}\right]_{, y}=I_{p} \ddot{w}, \\
M_{x, x}+M_{x y, y}-Q_{x}=0, \quad M_{y, y}+M_{x y, x}-Q_{y}=0,
\end{gathered}
\tag{3}
$$
where $I_{p}=\sum_{k=1}^{N} \rho_{k} h_{k}$. According to the classical plate theory, the stress resultants and couples are defined as follows:
$$
\begin{gathered}
\left\{\begin{array}{l}
N_{x} \\
N_{y} \\
N_{x y}
\end{array}\right\}=\int_{\frac{-h}{2}}^{\frac{h}{2}}\left\{\begin{array}{l}
\sigma_{x} \\
\sigma_{y} \\
\sigma_{x y}
\end{array}\right\} \mathrm{d} z=\left[\begin{array}{ccc}
A_{11} & A_{12} & \\
& A_{22} & \\
& & A_{66}
\end{array}\right]\left\{\begin{array}{l}
\varepsilon_{x}^{0} \\
\varepsilon_{y}^{0} \\
\gamma_{x y}^{0}
\end{array}\right\}-\left\{\begin{array}{l}
N_{x}^{p} \\
N_{y}^{p} \\
0
\end{array}\right\},\left\{\begin{array}{l}
Q_{x} \\
Q_{y}
\end{array}\right\}=\int_{\frac{-h}{2}}^{\frac{h}{2}} k_{s}\left\{\begin{array}{l}
\sigma_{x z} \\
\sigma_{y z}
\end{array}\right\} \mathrm{d} z=k_{s}\left[\begin{array}{ll}
A_{44} & \\
& A_{55}
\end{array}\right]\left\{\begin{array}{l}
\gamma_{x z} \\
\gamma_{y z}
\end{array}\right\}, \\
\left\{\begin{array}{l}
M_{x} \\
M_{y} \\
M_{x y}
\end{array}\right\}=\int_{\frac{-h}{2}}^{\frac{h}{2}}\left\{\begin{array}{l}
\sigma_{x} \\
\sigma_{y} \\
\sigma_{x y}
\end{array}\right\} z \mathrm{~d} z=\left[\begin{array}{ccc}
D_{11} & D_{12} & \\
& D_{22} & \\
& & D_{66}
\end{array}\right]\left\{\begin{array}{l}
\kappa_{x} \\
\kappa_{y} \\
\kappa_{x y}
\end{array}\right\}-\left\{\begin{array}{l}
M_{x}^{p} \\
M_{y}^{p} \\
0
\end{array}\right\}
\end{gathered}
\tag{4}
$$
in which $N_{x}^{p}, N_{y}^{p}$ and $M_{x}^{p}, M_{y}^{p}$ represent the additional actuator forces and moments induced by the electric field, and they can be written as
$$
N_{x}^{p}=\sum_{k=1}^{N} e_{31}^{k} V_{k}, N_{y}^{p}=\sum_{k=1}^{N} e_{32}^{k} V_{k}, M_{x}^{p}=\frac{1}{2} \sum_{k=1}^{N} e_{31}^{k} V_{k}\left(z_{k}+z_{k-1}\right), M_{y}^{p}=\frac{1}{2} \sum_{k=1}^{N} e_{32}^{k} V_{k}\left(z_{k}+z_{k-1}\right).
$$

By substituting Eq.1, Eq.2 and Eq.4 into Eq.3 and introducing the following dimensionless parameters
$$
\begin{gathered}
\xi=x / a, \eta=y / b, \lambda=a / b, H=a / h, \bar{h}_{k}=h_{k} / h, U=a u / h^{2}, V=a v / h^{2}, W=w / h, \Phi=H \varphi, \Psi=H \psi, \\
\tau=\frac{t}{a^{2}} \sqrt{E h^{3} / I_{p}}, \bar{A}_{i j}(\tau)=A_{i j}(\tau) /(E h), \bar{D}_{i j}(\tau)=D_{i j}(\tau) /\left(E h^{3}\right), V_{1}=e_{31} V /(E h), V_{2}=e_{32} V /(E h)
\end{gathered}
$$

The dimensionless nonlinear governing equations of motions of the laminated piezoelectric plate in terms of $U, V, W, \Phi$ and $\Psi$ can be obtained.

### Solution methodology

For a simply supported plate, a solution is sought in the following separable form:

$$
\begin{align*}
U &= \sum_{m=1}^{\infty} \sum_{n=1,3,\cdots}^{\infty} \sin(2\pi m\xi)\sin(\pi n\eta)U_{mn}(\tau), &
V &= \sum_{m=1,3,\cdots}^{\infty} \sum_{n=1}^{\infty}\sin(\pi m\xi)\sin(2\pi n\eta)V_{mn}(\tau), \\
W &= \sum_{m=1,3,\cdots}^{\infty} \sum_{n=1,3,\cdots}^{\infty} \sin(\pi m\xi)\sin(\pi n\eta)W_{mn}(\tau), &
\Phi &= \sum_{m=1,3,\cdots}^{\infty} \sum_{n=1,3,\cdots}^{\infty} \cos(\pi m\xi)\sin(\pi n\eta)\Phi_{mn}(\tau) \tag{5} \\
\Psi &= \sum_{m=1,3,\cdots}^{\infty} \sum_{n=1,3,\cdots}^{\infty} \sin(\pi m\xi)\cos(\pi n\eta)\Psi_{mn}(\tau).
\end{align*}
$$

Substituting Eq.5 into the governing equations, and making use of the one-term approximation of the Galerkin method, we can obtain the nonlinear equations in terms of $U_{11},V_{11},W_{11},\Phi_{11}$and $\Psi_{11}$. For simplifying calculations, the functions $U_{11}(\tau),V_{11}(\tau),\Phi_{11}(\tau)$and $\Psi_{11}(\tau)$ can be expressed in terms of second powers of $W_{11}(\tau)$. Then, the resulting equations can be transformed into the function of $W_{11}$.

For the case of nonlinear free vibration, the method of harmonic balance is used to solve the equation. The unknown $W_{11}(\tau)$ is expanded as Fourier cosine series in $\tau$

$$
W_{11}(\tau)=\sum_{i=0}^{\infty}W_{i}\cos(i\omega\tau), \tag{6}
$$

where $W_{i}$ is constant Fourier coefficients for the ith harmonic amplitudes, and $\omega$ is the dimensionless nonlinear vibrating frequency.

Then, substituting Eq.6 into the resulting equation, and each term is converted into the first power of cosine functions. Equating the coefficients of like terms of cosine functions to zero, a system of simultaneous nonlinear algebraic equations is obtained. These equations can be solved for $W_{i}$ for a given set of the parameters for elastic plate and piezoelectric layer and dimensionless vibrating frequency $\omega$.

### Numerical Results

Numerical results for effect of piezoelectricity on nonlinear free vibration are presented for symmetric cross-ply laminated piezoelectric rectangular plate. Assume every layer of the plate has the identical thickness. The orthotropic elastic plate is taken as graphite-epoxy and the piezoelectric material is taken as PZT5. The material properties are taken as [7]:

Graphite-epoxy:
$E_{L}=132.4\mathrm{GPa}, E_{T}=10.8\mathrm{GPa}, G_{LT}=5.5\mathrm{GPa}, G_{TZ}=3.6\mathrm{GPa}, G_{LZ}=5.6\mathrm{GPa}\ \nu_{LT}=0.24, \rho_{e}=1580\mathrm{kg/m^3}$

PZT5:
$E_{L}=E_{T}=62\mathrm{GPa}, G_{TZ}=18\mathrm{GPa}, G_{LZ}=G_{LT}=23.6\mathrm{GPa}\ \nu_{LT}=0.31, \rho_{p}=7750\mathrm{kg/m^3}, e_{31}=e_{32}=-19.77\mathrm{C/m^2}$

Fig.1 presents the influence of the applied voltage on the nonlinear vibrating frequency of symmetric cross-ply [PZT5/$0^\circ/90^\circ/0^\circ/90^\circ/0^\circ$/PZT5]laminated piezoelectric plate. $\omega_0$ denotes the dimensionless linear frequency neglecting the effects of piezoelectricity. When the applied voltage is negative, the vibrating frequency decreases. When the applied voltage is positive, the vibrating frequency increases. It is concluded that it is possible to control (enhance/reduce) the frequency of vibration with the applied electric potential difference. Fig.2 displays the effect of various location for piezoelectric layer on nonlinear vibrating frequency of symmetric cross-ply

laminated piezoelectric plate of three lamination schemes- $[0^{\circ}/90^{\circ}/$PZT5$/0^{\circ}/$PZT5$/90^{\circ}/0^{\circ}]$, $[0^{\circ}/$PZT5$/90^{\circ}/0^{\circ}/90^{\circ}/$PZT5$/0^{\circ}]$ and [PZT5$/0^{\circ}/90^{\circ}/0^{\circ}/90^{\circ}/0^{\circ}/$PZT5]. It can be seen that when the piezoelectric layers is located at the top and bottom surfaces of the laminated piezoelectric plate, the vibrating frequency is biggest. So, generally, we can bonding piezoelectric layer on the surface of the damaged structures to improve the vibrating frequency and stability.

![](./images/811658983130529794_1.jpg)

Fig.1 Effect of applied voltage on nonlinear frequency of laminated piezoelectric plates

![](./images/811658983130529794_2.jpg)

Fig.2 Effect of various location for piezoelectric layer on nonlinear frequency of laminated piezoelectric plates

## Conclusions
The effects of piezoelectricity on the nonlinear vibration of symmetric cross-ply moderately thick laminated piezoelectric plates are investigated. Numerical results show that the piezoelectricity has obvious effect on the nonlinear amplitude-frequency response curves of the structure. The property of the piezoelectric materials will provide a control mean for damaged structures.

## Acknowledgements
The project was supported by the Young Technological Talents' Innovation Fund of Fujian Province (2006F3077).

## References
[1] H.S. Tzou and Y.H. Zhou: J. Sound Vib Vol.188 (1995), p.189

[2] R.C. Batra and X.Q. Liang: Int. J. Solids Struct Vol.33 (1996), p.1597

[3] J.X. Gao and Y.P. Shen: J. Sound Vib Vol.264 (2003), p.911

[4] K. Jayakumar, D. Yadav and B.N. Rao: Commun Nonlin Sci Num Simul Vol. 14(2009), p.1646

[5] Y.F. Zheng, F. Wang and Y.M. Fu: Int. J. Nonlin Sci Num vol.10(2009), p.459

[6] Y. Nath and K.K. Shukla: J. Sound Vib Vol. 247(2001), p.509

[7] D. Varelis and D.A. Saravanos: AIAA Journal Vol.42 (2004), p.1227

Advanced Materials, CEAM 2011

10.4028/www.scientific.net/AMR.239-242

Effect of Piezoelectricity on Nonlinear Free Vibration of Moderately Thick Laminated Piezoelectric
Plates

10.4028/www.scientific.net/AMR.239-242.1223