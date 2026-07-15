# Nonlinear Vibration and Modal Analysis of FG Nanocomposite Sandwich Beams Reinforced by Aggregated CNTs

Amin Pourasghar, Zengtao Chen
Department of Mechanical Engineering, University of Alberta, Edmonton, Alberta, T6G 2G8, Canada

In the present work, by considering the aggregation effect of single-walled carbon nanotubes (SWCNT), the nonlinear vibration of functionally graded (FG) nanocomposite sandwich Timoshenko beams resting on Pasternak foundation are presented. The material properties of the FG nanocomposite sandwich beam are estimated using the Eshelby-Mori-Tanaka approach and differential quadrature method (DQM) is used to obtain natural frequency. The nonlinear governing equations and boundary conditions are derived using the Hamilton principle and von Kármán geometric nonlinearity. The higher order nonlinear governing equations and boundary conditions are calculated using the Hamilton principle. A direct iterative method is employed to determine the nonlinear frequencies and mode shapes of the beams. It is shown that the mechanical properties and therefore vibration of functionally graded carbon nanotube reinforced (FG-CNTR) sandwich beams are severely affected by CNTs aggregation. A detailed parametric study is carried out to investigate the influences of Winkler foundation modulus, shear elastic foundation modulus, length to span ratio, thicknesses of face sheets on the nonlinear vibration of the structure. POLYM. ENG. SCI., 00:000-000, 2019. © 2019 Society of Plastics Engineers

## INTRODUCTION

Over the past few years, there has been an ever-increasing interest in the synthesis, characterization, functionalization, molecular modeling, and design of nanocomposite materials. The outstanding and exceptional mechanical, electrical, and thermal properties of carbon nanotubes [1-4] have stimulated researchers to exploit them as a new generation of reinforcing agents for polymers. Numerous studies have been made to analytically and experimentally determine the mechanical properties of CNTR nanocomposites as molecular dynamics (MD) simulation [5-7], continuum mechanics [8-10], and multiscale simulation [11, 12] Seidel et al. [13] focused on the obtain effective elastic properties of composites consisting of aligned single or multiwalled carbon nanotubes embedded in a polymer matrix. They also investigated on the effect of an interphase layer between the nanotube and the polymer matrix as a result of functionalization. For the same reasons mentioned above, CNTs have received increased attention as reinforcements for polymer composites.

One of the characteristic features of CNT morphology is the formation of aggregation in the matrix. The macromechanical properties of nanocomposites are affected by the microstructure and volume fraction of CNTs. Several methods are used to evaluate the effective properties of nanocomposites, including those based on single inclusion theory [14], such as Mori-Tanaka method [15], the self-consistent scheme [16], and differential method [17], among others.

The Mori-Tanaka (MT) model is one of the best known analytical approaches to determine the effective material constants of composite materials. Yang et al. [18] used the MT approach to show the effect of CNT aggregation in the composite. They illustrated the degree of CNT aggregation dramatically influences the effective properties of the CNT/SMP composites. Barai [19] developed a two-scale micromechanical model to analyze the effect of CNT aggregation and interface condition on the plastic strength of CNT/matrix inclusions, and the small-scale addressed the property of the clustered inclusions.

The nonlinear and linear vibration of sandwich beams, plates, and panels has been an object of many studies [20-27]. Nanocomposite FG sandwich structures are widely used in the field of transportation (helicopter blades, ship's hull, etc.) for their low weight and high in-plane and flexural stiffness. So, with the wide application of FG sandwich structures, understanding their responses becomes an essential task. Though there are research works reported on general sandwich structures, studies related to the nonlinear vibration of FG nanocomposite sandwich structures are few in numbers.

Bending analysis of a sandwich beam with softcore and carbon nanotube reinforced composite face sheets in the literature is carried out by Jedari Salami [28] based on extended high-order sandwich panel theory. In this theory, the face sheets follow the first-order shear deformation theory. Xiang and Yang develops a two-dimensional elasticity solution [29] to obtain the free and forced vibration characteristics of laminated FG Timoshenko beam of variable thickness, which consists of a homogeneous substrate and two inhomogeneous functionally graded layers, subjected to one-dimensional steady heat conduction in the thickness direction, employing the differential quadrature method (DQM).

Ke et al. [30, 31] analyzed the nonlinear free vibrations of FG-CNTR Timoshenko beams with symmetric and unsymmetrical distributions of CNTs along the thickness direction using Ritz method and direct iterative technique. Also, they investigated [31] on the nonlinear free vibration of the FGM microbeams based on the modified couple stress theory and Timoshenko beam theory. MT homogenization technique is employed to model the through-the-thickness variation of the material properties in a simple power-law function. They used the DQM to discretize the nonlinear governing equations, which are then solved by a direct iterative algorithm to obtain the nonlinear vibration frequencies of the FGM microbeams.

However, this article is motivated by the lack of studies in the technical literature concerning to the influence of graded agglomerated CNTs on nonlinear free vibration analysis of functionally graded sandwich carbon nanotube reinforced (FGS-CNTR) beams on Pasternak foundation. A numerical method that makes use of the DQM together with an iterative algorithm is employed to determine the nonlinear vibration frequencies of the FG nanocomposite beams with different boundary conditions. The face sheets are

---
Correspondence to: A. Pourasghar; e-mail: pourasgh@ualberta.ca
DOI 10.1002/pen.25119
Published online in Wiley Online Library (wileyonlinelibrary.com).
© 2019 Society of Plastics Engineers

POLYMER ENGINEERING AND SCIENCE—2019

reinforced by CNT volume fraction graded according to a power-law distribution. Various material profiles through the thickness of face sheets can be illustrated by using the power-law distribution. Nonlinear free vibration analysis of FGS-CNTRS beams is studied based on Timoshenko beam theory and through MT model and DQ method, which is found to be a simple and efficient numerical technique for solving partial differential equations [32-36]. The effects of the degree of CNT aggregation, CNT volume fraction, Pasternak foundation, geometric parameters, and so forth, on the nonlinear vibration of the structure are presented in this article.

# MATERIAL PROPERTIES OF CNTRCS

## Effect of CNT Aggregation on the Properties of the Composite

To better predict material properties of FG nanocomposite sandwich beams, the MT homogenization scheme is used in this study [37-39]. The CNTs were arranged within the matrix in such manner to introduce clustering. It has been observed that, due to large aspect ratio, the low bending rigidity of CNTs and van der Waals forces, CNTs tend to bundle or cluster together making it quite difficult to produce fully dispersed CNT reinforced composites. The effect of nanotube aggregation on the elastic properties of randomly oriented CNTRC is presented in this section. Two parameter micromechanics models are derived to determine the effect of nanotube aggregation on the elastic properties of randomly oriented CNTRC (Fig. 1). It is assumed that some CNTs are uniformly distributed throughout the matrix and that other CNTs appear in cluster form because of aggregation, as shown in Fig. 1. The total volume of the CNTs in the representative volume element (RVE), denote by $V_{r}$, can be divided into the following two parts [14, 15]:

$$
V_{r}=V_{r}^{\text{cluster}}+V_{r}^{m} \tag{1}
$$

Where $V_{r}^{\text{cluster}}$ denote the volumes of CNTs inside a cluster, and $V_{r}^{m}$ is the volume of CNTs in the matrix and outside the clusters. The two parameters used to describe the aggregation are defined as:

$$
\mu=\frac{V_{\text{cluster}}}{V}, \quad \eta=\frac{V_{r}^{\text{cluster}}}{V_{r}} \quad 0 \leq \eta, \mu \leq 1 \tag{2}
$$

![](./images/812778406948110340_1.jpg)

FIG. 1. RVE with Eshelby cluster model of aggregation of CNTs. [Color figure can be viewed at wileyonlinelibrary.com]

where $V$ is the volume of RVE, $V_{\text{cluster}}$ volume of clusters in the RVE. $\mu$ volume fraction of clusters concerning the total volume $V$ of the RVE, $\eta$ volume ratio of the CNTs inside the clusters over the entire CNT inside the RVE. The effective bulk modulus $K$ and the effective shear modulus $G$ of the composite are derived from the MT method as follows [39]:

$$
K=K_{\text{out}}\left[1+\frac{\mu\left(\frac{K_{\text{in}}}{K_{\text{out}}}-1\right)}{1+\alpha(1-\mu)\left(\frac{K_{\text{in}}}{K_{\text{out}}}-1\right)}\right] \tag{3}
$$

$$
G=G_{\text{out}}\left[1+\frac{\mu\left(\frac{G_{\text{in}}}{G_{\text{out}}}-1\right)}{1+\beta(1-\mu)\left(\frac{G_{\text{in}}}{G_{\text{out}}}-1\right)}\right] \tag{4}
$$

With

$$
\nu_{\text{out}}=\frac{\left(3 K_{\text{out}}-2 G_{\text{out}}\right)}{2\left(3 K_{\text{out}}+G_{\text{out}}\right)} \tag{5}
$$

$$
\alpha=\frac{\left(1+\nu_{\text{out}}\right)}{3\left(1-\nu_{\text{out}}\right)} \tag{6}
$$

$$
\beta=\frac{2\left(4-5 \nu_{\text{out}}\right)}{15\left(1-\nu_{\text{out}}\right)} \tag{7}
$$

The effective Young's modulus E and Poisson's ratio $v$ of the composite can be calculated in terms of $K$ and $G$ by:

$$
E=\frac{9 K G}{3 K+G} \tag{8}
$$

$$
v=\frac{3 K-2 G}{6 K+2 G} \tag{9}
$$

Consider an FGS_CNTR beams resting on Pasternak foundations as shown in Fig. 2. In the present work, $V_{C N}$ and $V_{m}$ are considered as the CNT and matrix volume fraction, respectively. We assume for FG beam, the volume fraction of the CNT is given by the power-law-type function:

$$
V_{C N}(z)=\left\{\begin{aligned}
V_{C N}=V_{o}+\left(V_{i}-V_{o}\right)\left(\frac{z+h / 2}{h_{f}}\right)^{q} &, \frac{-h}{2} \leq z \leq \frac{-h}{2}+h_{f} \\
V_{i} &, \frac{-h}{2}+h_{f} \leq z \leq \frac{h}{2}-h_{f} \\
V_{C N}=V_{o}+\left(V_{i}-V_{o}\right)\left(\frac{-z+h / 2}{h_{f}}\right)^{q} &, \frac{h}{2}-h_{f} \leq z \leq \frac{h}{2}
\end{aligned}\right.
\tag{10}
$$

where the volume fraction index $q$ $(0 \leq q \leq \infty)$, $h$ and $h_{f}$ are the thicknesses of beam and the face sheets, respectively, and $V_{o}$ and $V_{i}$, which have values that range from 0 to 1, denote the maximum and minimum volume fraction of CNT that could exist in the thickness direction. According to relation (10), the amount of CNT in the core of the structure is constant and equal to $V_{i}$. Various material profiles through the thickness of face sheets can be illustrated by using the power-law distribution.

![](./images/812778406948110340_2.jpg)

FIG. 2. Geometry of FGS-CNTR beam. [Color figure can be viewed at wileyonlinelibrary.com]

The through-thickness variations of CNT volume fraction for some profiles are illustrated in Fig. 3. In Fig. 3, the classic CNT volume fraction profiles are presented. As we can see, a sandwich beam made up of three discrete layers with a homogeneous core (which can be consist of CNT or not).

## EQUATIONS OF MOTION

Timoshenko beam theory is employed in this article with the following displacement field to account for the effect of transverse shear strain, which is essential in the deformation of composite structures.

$$
U(x, y, z, t)=u_{0}(x, z, t)+z \psi(x, z, t) \tag{11a}
$$

$$
W(x, y, z, t)=w_{0}(x, z, t) \tag{11b}
$$

in which $u_0$ and $w_0$ represent the components of displacement at $z=0$, $\psi$ is the section normal vector rotations about the $y$-axes, and $t$ is time.

Consider the FGS-CNTR beam shown in Fig. 2. The beam is assumed to be rested on the two-parameter elastic (Pasternak) foundation whose supporting action is described by

$$
P=K_{w} w-K_{s} \frac{\partial^{2} w}{\partial x^{2}} \tag{12}
$$

![](./images/812778406948110340_3.jpg)

FIG. 3. Variation of the CNT volume fraction through the thickness of the beam. [Color figure can be viewed at wileyonlinelibrary.com]

where $P$ is the foundation reaction per unit area, $w$ is the transverse deflection of the beam, and $K_w$, $K_s$ are Winkler and shearing layer elastic coefficients of the foundation. It is worth noting that the Pasternak elastic foundation model is an extension of the well-known Winkler model $(K_s=0)$.

The normal linear strain $\varepsilon_x$ and shear strain $\gamma_{xz}$ are associated with the displacements as:

$$
\varepsilon_{x}=\frac{\partial u_{0}}{\partial x}+z \frac{\partial \psi}{\partial x}+\frac{1}{2}\left(\frac{\partial w_{0}}{\partial x}\right)^{2}, \gamma_{x z}=\frac{\partial w_{0}}{\partial x}+\psi \tag{13}
$$

Using the linear elastic constitutive law, the normal stress $\sigma_x$ and shear stress $\tau_{xz}$ are given by

$$
\begin{aligned}
& \sigma_{x}(z)=Q_{11}(z) \varepsilon_{x} \\
& \tau_{x z}(z)=Q_{55}(z) \gamma_{z x}
\end{aligned} \tag{14}
$$

in which

$$
Q_{11}(z)=\frac{E(z)}{1-\nu^{2}}, \quad Q_{55}(z)=\frac{E(z)}{2(1+\nu)} \tag{15}
$$

Employing Hamilton's principle, the equations of motion and the related boundary conditions can be derived. According to Hamilton's principle

$$
\delta \int_{0}^{t}\left(T-\Pi+\gamma_{p}\right) d t=0 \tag{16}
$$

Where $\delta$, $T$, and $\Pi$ denote the variational symbol, the kinetic energy of the beam, and potential energy composed of strain energy the beam together with the elastic potential energy of the elastic foundation, respectively. It is worth noting that $\gamma_p$ is the work done by an external force that is zero for free vibration analysis.

By setting the coefficients of $\delta u$, $\delta w$, and $\delta \psi$ to zero leads to the equations of motion as.

$$
\delta u: \frac{\partial N_{x}}{\partial x}=I_{1} \frac{\partial^{2} u_{0}}{\partial t^{2}}+I_{2} \frac{\partial^{2} \psi}{\partial t^{2}} \tag{17a}
$$

$$
\delta w: \frac{\partial Q_{x}}{\partial x}+\frac{\partial}{\partial x}\left(N_{x} \frac{\partial w}{\partial x}\right)-K_{f} w_{0}+K_{s} \frac{\partial^{2} w_{0}}{\partial x^{2}}=I_{1} \frac{\partial^{2} w}{\partial t^{2}} \tag{17b}
$$

$$
\delta \Psi: \frac{\partial M_{x}}{\partial x}-Q_{x}=I_{2} \frac{\partial^{2} u_{0}}{\partial t^{2}}+I_{3} \frac{\partial^{2} \psi}{\partial t^{2}} \tag{17c}
$$

where the resultant normal force $N_x$, bending moment $M_x$, and transverse shear force $Q_x$ are calculated from

$$
\left\{\begin{array}{l}
N_{x} \\
M_{x} \\
Q_{x}
\end{array}\right\}=\int_{-h / 2}^{h / 2}\left\{\begin{array}{c}
\sigma_{x x} \\
z \sigma_{x x} \\
\tau_{x z}
\end{array}\right\} d z=\left\{\begin{array}{l}
A_{11}\left[\frac{\partial u_{0}}{\partial x}+\frac{1}{2}\left(\frac{\partial w_{0}}{\partial x}\right)^{2}\right]+B_{11} \frac{\partial \psi}{\partial x} \\
B_{11}\left[\frac{\partial u_{0}}{\partial x}+\frac{1}{2}\left(\frac{\partial w_{0}}{\partial x}\right)^{2}\right]+D_{11} \frac{\partial \psi}{\partial x} \\
k^{*} A_{55}\left(\frac{\partial w_{0}}{\partial x}+\psi\right)
\end{array}\right\}
$$

(18)

In this study, the shear correction factor $k^{*}=\frac{5}{6}$ is used, and the stiffness components $A_{11}, B_{11}, D_{11}, A_{55}$ of the beam are defined as:

$$
\begin{gathered}
\left(A_{11}, B_{11}, D_{11}\right)=\int_{-h / 2}^{h / 2} Q_{11}(z)\left(1, z, z^{2}\right) d z, A_{55}=\int_{-h / 2}^{h / 2} Q_{55}(z) d z \\
\left(I_{1}, I_{2}, I_{3}\right)=\int_{-h / 2}^{h / 2} \rho(z)\left(1, z, z^{2}\right) d z
\end{gathered}
$$

(19)

Different boundary conditions of the beams such as hinged- hinged (H-H), clamped-hinged (C-H), clamped-clamped (C-C), and clamped-free (C-F) can be considered. These conditions are described as:

$$
\begin{aligned}
& \text { Clamped }(\mathrm{C}): u_{0}=w_{0}=\Psi=0 \\
& \text { Hinged }(\mathrm{H}): u_{0}=w_{0}=M_{x}=0
\end{aligned}
$$

(20)

Since we need to compare our results with the similar ones in the previous works, in the present study we used a beam with the hinged condition over simply supported beam. By using the fol- lowing dimensionless quantities

$$
\begin{gathered}
\xi=\frac{x}{L},(\bar{U}, \bar{W})=\frac{\left(u_{0}, w_{0}\right)}{h}, \\
\left(a_{11}, a_{55}, b_{11}, d_{11}\right)=\left(\frac{A_{11}}{A_{110}}, \frac{A_{55}}{A_{110}}, \frac{B_{11}}{A_{110} h}, \frac{D_{11}}{A_{110} h^{2}}\right), \\
\psi=\Psi, \lambda=L / h,\left(\bar{I}_{1}, \bar{I}_{2}, \bar{I}_{3}\right)=\left(\frac{I_{1}}{I_{10}}, \frac{I_{2}}{I_{10} h}, \frac{I_{3}}{I_{10} h^{2}}\right) \\
k_{w}=\frac{K_{w} L^{2}}{A_{110}}, k_{s}=\frac{K_{s}}{A_{110}} \\
\tau=\frac{t}{L} \sqrt{\frac{A_{110}}{I_{10}}}
\end{gathered}
$$

(21)

in which $A_{110}$ and $I_{10}$ are the values of $A_{11}$ and $I_{1}$ of a homoge neous polymeric beam., Eq. (21) can be transformed into the fol- lowing dimensionless form:

$$
a_{11}\left(\frac{\partial^{2} u}{\partial \xi^{2}}+\frac{1}{\lambda} \frac{\partial w}{\partial \xi} \frac{\partial^{2} w}{\partial \xi^{2}}\right)+b_{11} \frac{\partial^{2} \psi}{\partial \xi^{2}}=\bar{I}_{1} \frac{\partial^{2} u}{\partial \tau^{2}}+\bar{I}_{2} \frac{\partial^{2} w}{\partial \tau^{2}}
$$

(22a)

$$
\begin{aligned}
& k^{*} a_{55}\left(\frac{\partial^{2} w}{\partial \xi^{2}}+\lambda \frac{\partial \psi}{\partial \xi}\right)+\frac{a_{11}}{\lambda}\left(\frac{\partial^{2} u}{\partial \xi} \frac{\partial^{2} w}{\partial \xi^{2}}+\frac{3}{2 \lambda}\left(\frac{\partial w}{\partial \xi}\right)^{2} \frac{\partial^{2} w}{\partial \xi^{2}}+\frac{\partial^{2} u}{\partial \xi^{2}} \frac{\partial w}{\partial \xi}\right)+ \\
& \frac{b_{11}}{\lambda}\left(\frac{\partial^{2} \psi}{\partial \xi^{2}} \frac{\partial w}{\partial \xi}+\frac{\partial \psi}{\partial \xi} \frac{\partial^{2} w}{\partial \xi^{2}}\right)-k_{w} w+k_{s} \frac{\partial^{2} w}{\partial \xi^{2}}=\bar{I}_{1} \frac{\partial^{2} w}{\partial \tau^{2}}
\end{aligned}
$$

(22b)

$$
\begin{aligned}
b_{11}\left(\frac{\partial^{2} u}{\partial \xi^{2}}+\frac{1}{\lambda} \frac{\partial w}{\partial \xi} \frac{\partial^{2} w}{\partial \xi^{2}}\right)+d_{11} \frac{\partial^{2} \psi}{\partial \xi^{2}}-k^{*} \lambda a_{55}\left(\frac{\partial w}{\partial \xi}+\eta \psi\right) & \\
= & \bar{I}_{2} \frac{\partial^{2} u}{\partial \tau^{2}}+\bar{I}_{3} \frac{\partial^{2} \psi}{\partial \tau^{2}}
\end{aligned}
$$

(22c)

The associated boundary conditions can also be written in a dimensionless form as:

For a clamped-clamped (C-C) boundary condition.

$$
u=w=\psi=0
$$

(23)

For a hinged-hinged (H-H) boundary condition.

$$
u=w=b_{11}\left(\frac{\partial u}{\partial \xi}+\frac{1}{2 \lambda}\left(\frac{\partial w}{\partial \xi}\right)^{2}\right)+d_{11} \frac{\partial \psi}{\partial \xi}=0
$$

(24)

### GDQ METHOD

The DQM [40, 41] is used to solve Eq. (25) and the associated boundary conditions to determine the nonlinear frequencies of FGS-CNTR beam resting on Pasternak foundation. The fundamen- tal idea of the DQM is to approximate the derivative of a function at a sample point as a linear weighted sum of the function values at all of the sample points in the problem domain. Hence, the $n$th order of a continuous function $f(x, z)$ concerning $x$ at a given point $x_{i}$ can be approximated as a linear sum of weighting values at all of the discrete points in the domain of $\mathrm{x}$, that is

$$
\frac{\partial^{f n\left(x_{i}, z\right)}}{\partial x^{n}}=\sum_{k=1}^{N} c_{i k}^{n} f\left(x_{i k}, z\right), \quad(\mathrm{i}=1,2, \ldots \mathrm{N}, \mathrm{n}=1,2, \ldots \mathrm{N}-1)
$$

(25)

where $N$ is the number of sampling points, and $c_{i j}^{n}$ [40] is the $x_{i}$ dependent weight coefficients.

The cosine pattern is used to generate the DQ point system

$$
x_{i}=\frac{1}{2}\left(1-\cos \left(\frac{i-1}{n-1} \pi\right)\right) \quad i=1,2, \ldots, N
$$

(26)

Applying Eq. (25) to Eq. (22), one obtains a set of ordinary differential equations

$$
a_{11}\left(\sum_{j=1}^{N} C_{i j}^{2} u_{j}+\frac{1}{\lambda} \sum_{j=1}^{N} C_{i j}^{1} w_{j} \sum_{j=1}^{N} C_{i j}^{2} w_{j}\right)+b_{11} \sum_{j=1}^{N} C_{i j}^{2} \psi_{j}=\bar{I}_{1} \ddot{u}+\bar{I}_{2} \ddot{w}
$$

(27a)

$$
k^{*} a_{55}\left(\sum_{j=1}^{N} C_{i j}^{2} w_{j}+\lambda \sum_{j=1}^{N} C_{i j}^{1} \psi_{j}\right)+
$$

$$
\begin{aligned}
& \frac{a_{11}}{\lambda}\left(\sum_{j=1}^{N} C_{i j}^{1} u_{j} \sum_{j=1}^{N} C_{i j}^{2} w_{j}+\frac{3}{2 \lambda}\left(\sum_{j=1}^{N} C_{i j}^{1} w_{j}\right)^{2} \sum_{j=1}^{N} C_{i j}^{2} w_{j}+\sum_{j=1}^{N} C_{i j}^{2} u_{j} \sum_{j=1}^{N} C_{i j}^{1} w_{j}\right) \\
& +\frac{b_{11}}{\lambda}\left(\sum_{j=1}^{N} C_{i j}^{2} \psi_{j} \sum_{j=1}^{N} C_{i j}^{1} w_{j}+\sum_{j=1}^{N} C_{i j}^{1} \psi_{j} \sum_{j=1}^{N} C_{i j}^{2} w_{j}\right)-k_{w} w_{i}+k_{s} \sum_{j=1}^{N} C_{i j}^{2} w_{j}=\bar{I}_{1} \ddot{w}
\end{aligned}
$$

(27b)

$$
\begin{aligned}
& b_{11}\left(\sum_{j=1}^{N} C_{i j}^{2} u_{j}+\frac{1}{\lambda} \sum_{j=1}^{N} C_{i j}^{1} w_{j} \sum_{j=1}^{N} C_{i j}^{2} w_{j}\right) \\
& +d_{11} \sum_{j=1}^{N} C_{i j}^{2} \psi_{j}-k^{*} a_{55} \lambda\left(\sum_{j=1}^{N} C_{i j}^{1} w_{j}+\lambda \psi_{i}\right)=\bar{I}_{2} \ddot{u}+\bar{I}_{3} \ddot{\psi}
\end{aligned}
\tag{27c}
$$

The associated boundary conditions can be handled in the same way. For example, the dimensionless boundary condition of clamped-Hinged (C-H) supported beams is

$$
u_{1}=w_{1}=\psi_{1}=0 \quad \text { at } \zeta=0
$$

$$
\begin{cases}
u_{N}=w_{N}=0 & \\
M_{x}=b_{11}\left(\sum_{j=1}^{N} c_{N j}^{1} u_{j} \frac{1}{2 \lambda}\left(\sum_{j=1}^{N} c_{N j}^{1} w_{j}\right)^{2}\right)+d_{11} \sum_{j=1}^{N} c_{N j}^{1} \Psi_{j}=0 & \text { at } \zeta=1
\end{cases}
\tag{28}
$$

After implementation of the boundary conditions, Eq. (27) can be written in matrix form as

$$
\left(K_{L}+\frac{1}{2} K_{N L 1}+\frac{1}{3} K_{N L 2}\right) U_{d}+M \ddot{U}_{d}=0
\tag{29}
$$

where $M$ is the mass matrix; $K_{L}$ is the linear stiffness matrix; $K_{N L 1}$ and $K_{N L 2}$ are nonlinear stiffness matrices that are linear and quadratic functions in $U_{d}$, respectively.

Expanding the dynamic displacement vector $U_{d}$ in the form of $U_{d}=U_{d}^{*} e^{i \omega t}$ where $\omega=\Omega L \sqrt{\sigma / E}$ represents the dimensionless frequency, $\Omega$ is the nonlinear vibration frequency of the FG nanocomposite sandwich beam, $U_{d}^{*}$ is the vibration mode shape vector. Substituting $U_{d}$ into Eq. (29) yields the nonlinear eigenvalue equations as follows

$$
\left(K_{L}+\frac{1}{2} K_{N L 1}+\frac{1}{3} K_{N L 2}\right) U_{d}^{*}-M \omega^{2} U_{d}^{*}=0
\tag{30}
$$

To solve the resulting system of nonlinear eigenvalue Eq. (30), an iterative procedure should be used. For this purpose, in the first step, the nonlinear terms due to the transverse displacement are neglected, and the resulting eigenvalue problem is solved in each case. In the second step, the eigenvector is appropriately scaled up such that the maximum transverse displacement is equal to the given vibration amplitude $w_{\max }$. Then, the eigenvalue problems are solved again to obtain the new eigenvalues and eigenvectors. In the third step, the eigenvector is scaled up again and step 2 is repeated until the relative error between the eigenvalues obtained from two consecutive iterations is within $0.1 \%$.

## RESULTS AND DISCUSSION

### Verification

In the numerical results, nonlinear free vibration analysis of the FGS-CNTR Timoshenko beam with different boundary conditions is investigated. Here, we consider PMMA, referred to Polymethyl methacrylate, as the matrix $(E_{m}=2.5\ GPa$, $\rho=1,190\ kg/m^{3})$ and (10, 10) SWCNT as the reinforcement (see Table 1):

<table>
<caption>Table 1. Material properties of equivalent fiber [42].</caption>
<thead>
<tr>
<th>Mechanical properties</th>
<th>CNT</th>
</tr>
</thead>
<tbody>
<tr>
<td>Longitudinal Young’s modulus</td>
<td>5.456 (Tpa)</td>
</tr>
<tr>
<td>Transverse Young’s modulus</td>
<td>1.010 (Tpa)</td>
</tr>
<tr>
<td>Longitudinal shear modulus</td>
<td>0.431 (Tpa)</td>
</tr>
<tr>
<td>Poisson’s ratio</td>
<td>0.175</td>
</tr>
</tbody>
</table>

Before starting numerical studies, to establish the accuracy of the present formulation and the computer program developed by the author, results obtained from the present study are compared with the available results in the literature. The nonlinear fundamental frequencies of CNTR beam $(\eta=L/h=1,\ h=0.1)$ is compared with data presented in Ref. 31. Table 2 shows that the present results are in good agreement with the results of Wang et al. [31]. The parameter used in this example are $E^{m}=2.5\ GPa,\ v^{m}=0.34,\ \rho^{m}=1190\ Kg/m^{3}$ for matrix, and the armchair (10,10) SWCNTs are used as the reinforcements with $E_{11}^{\text{cnt}}=600GPa,E_{22}^{\text{cnt}}=10GPa,v^{cnt}=0.19$ and $\rho^{\text{cnt}}=1400$.

Before analyzing the vibration of FGS-CNTR beams, the effects of aggregation degree (μ and η) on the effective longitude Young’s modulus of FG-CNTRC beam needs to be investigated Fig. 4. Using the relations presented in previous sections, it is possible to observe the variations of the effective material properties through the thickness of the FGS-CNTR beam for different aggregation parameters. For this goal, a particular case of the FGS-CNTR beam is considered in which $h_{f}=0.35,\ h_{c}=0.3$ and $q=2$. The variations of Young’s modulus of beams concerning the different aggregation parameters μ and η = 0.75 are illustrated in Fig. 4. As expected, at a constant value of z/h ratio, with the increase of parameter μ (μ < η), the effective Young’s modulus increases. Figure 4 represents the fact that the highest values of Young’s modulus are attained for the aggregation state of η = μ = 0.75 (fully dispersed), where the volume fraction of CNTs in the cluster and the matrix are equal. As it is observed, when μ is less than η (μ < η), the effective Young’s modulus increases with increasing the value of μ and has the maximum amount when the CNTs are uniformly dispersed in the composite, that is, μ = η. So, it is undeniable that the aggregation parameters have significant effects on the material properties. Therefore, one can come to this conclusion that CNTs aggregation plays an essential role in vibrational characteristics of FGS-CNTR beams.

Now, vibration analysis of FGS-CNTR beams rested on Pasternak foundation is studied using the MT approach. The thickness of

<table>
<caption>Table 2. Comparison of dimensionless nonlinear frequency $\omega_{nl}/\omega_{l}$ for UD-CNTRC beams $(L/h=10)$.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2">$V_{\text{cnt}}^{*}$</th>
<th rowspan="2">Method</th>
<th rowspan="2">$\omega_{l}$</th>
<th colspan="5">$W_{\text{max}}$</th>
</tr>
<tr>
<th>0.1</th>
<th>0.2</th>
<th>0.3</th>
<th>0.4</th>
<th>0.5</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">C-C</td>
<td rowspan="2">0.12</td>
<td>Ritz³⁰</td>
<td>1.6678</td>
<td>1.0154</td>
<td>1.0605</td>
<td>1.1318</td>
<td>1.2251</td>
<td>1.3381</td>
</tr>
<tr>
<td>Present</td>
<td>1.6621</td>
<td>1.0142</td>
<td>1.0544</td>
<td>1.1143</td>
<td>1.1872</td>
<td>1.2748</td>
</tr>
<tr>
<td rowspan="2">0.28</td>
<td>Ritz³⁰</td>
<td>2.3634</td>
<td>1.0176</td>
<td>1.0687</td>
<td>1.1490</td>
<td>1.2544</td>
<td>1.3829</td>
</tr>
<tr>
<td>Present</td>
<td>2.3420</td>
<td>1.0171</td>
<td>1.0646</td>
<td>1.1337</td>
<td>1.2157</td>
<td>1.3044</td>
</tr>
<tr>
<td rowspan="4">H-H</td>
<td rowspan="2">0.12</td>
<td>Ritz³⁰</td>
<td>1.2576</td>
<td>1.0278</td>
<td>1.1070</td>
<td>1.2278</td>
<td>1.3791</td>
<td>1.5522</td>
</tr>
<tr>
<td>Present</td>
<td>1.2551</td>
<td>1.0256</td>
<td>1.0952</td>
<td>1.1938</td>
<td>1.3083</td>
<td>1.4302</td>
</tr>
<tr>
<td rowspan="2">0.28</td>
<td>Ritz³⁰</td>
<td>1.8297</td>
<td>1.0299</td>
<td>1.1151</td>
<td>1.2439</td>
<td>1.4046</td>
<td>1.5874</td>
</tr>
<tr>
<td>Present</td>
<td>1.8201</td>
<td>1.0299</td>
<td>1.1094</td>
<td>1.2065</td>
<td>1.3261</td>
<td>1.4525</td>
</tr>
</tbody>
</table>

![](./images/812778406948110340_4.jpg)

FIG. 4. The variation of Young's modulus and along the thickness of the FGS-CNTR beam with aggregation effect. [Color figure can be viewed at wileyonlinelibrary.com]

the sandwich beam is 1 and kept unchanged in all numerical exam- ples, whereas the thickness of core layer and face sheets change corresponding to the core-to-face sheet thickness ratio $h_{c} / h_{f}=2$ ,4,8. Also, to be close to the reality, the amount of $q$ in most cases considered 1 and 50, which shows the linear and uniform distribu- tion of CNT in the face sheets, respectively (Fig. 3).

Tables 3-5 show the effects of the elastic foundation coeffi- cients and different values of core-to-face sheet thickness ratio(h /hf = 2, 4) on the dimensionless nonlinear and linear vibration of various types of CNTRC sandwich beams for different bound- ary conditions. By increasing $q$ which leads to increasing the vol ume fraction of CNT on the face sheets, both linear and nonlinear frequencies of beam will increase. It can be seen that among the three boundary conditions considered, the clamped-clamped beam has the maximum values of linear and nonlinear frequencies. Also, it can be inferred that with increasing the $h_{c} / h_{f}$ ratio, the fre quency decreases. This justifies by the fact that reducing of the thickness of face sheets will result in decrease of CNT volume fraction value, so it becomes softer. It is also observed, the fre- quency (both linear and nonlinear) of the beams increase when resting on elastic foundations. It happens because the beam becomes stiffer with elastic foundations.

TABLE 3. Nonlinear frequency $\omega_{n l}$ for C-C CNTRC sandwich beams $(L / h=10, q=1, V_{i}=0.05, V_{o}=0.1, \eta=0.4, \mu=0.4)$ .

<table><thead><tr><th rowspan="2">$(k_{w},k_{s})$</th><th rowspan="2">$h_{c}/h_{f}$</th><th rowspan="2">$ω_{l}$</th><th colspan="3">$q=1$</th><th rowspan="2">$ω_{l}$</th><th colspan="3">$q=100$</th></tr><tr><td>$w_{max}=0.1$</td><td>0.3</td><td>0.5</td><td>$w_{max}=0.1$</td><td>0.3</td><td>0.5</td></tr></thead><tbody><tr><td rowspan="2">(0,0)</td><td>2</td><td>2.2869</td><td>2.2928</td><td>2.3396</td><td>2.4293</td><td>2.5346</td><td>2.5411</td><td>2.5919</td><td>2.6894</td></tr><tr><td>4</td><td>2.1863</td><td>2.1888</td><td>2.2457</td><td>2.3459</td><td>2.4139</td><td>2.4165</td><td>2.4756</td><td>2.5584</td></tr><tr><td rowspan="2">(0,1,0)</td><td>2</td><td>2.3083</td><td>2.3109</td><td>2.3316</td><td>2.3728</td><td>2.5539</td><td>2.5603</td><td>2.6108</td><td>2.7076</td></tr><tr><td>4</td><td>2.2087</td><td>2.2112</td><td>2.2676</td><td>2.3668</td><td>2.4342</td><td>2.4368</td><td>2.4954</td><td>2.5989</td></tr><tr><td rowspan="2">(0.1,0.2)</td><td>2</td><td>2.7680</td><td>2.7728</td><td>2.8107</td><td>2.8840</td><td>2.9758</td><td>2.9784</td><td>2.9986</td><td>3.1071</td></tr><tr><td>4</td><td>2.6856</td><td>2.6909</td><td>2.7326</td><td>2.8131</td><td>2.8737</td><td>2.8794</td><td>2.9243</td><td>3.0108</td></tr></tbody></table>

TABLE 4. Nonlinear frequency $\omega_{n l}$ for H-H CNTRC sandwich beams $(L / h=10, q=1, V_{i}=0.05, V_{o}=0.1, \eta=0.4, \mu=0.4)$ .

<table><thead><tr><th rowspan="2">$(k_{w},k_{s})$</th><th rowspan="2">$h_{c}/h_{f}$</th><th rowspan="2">$ω_{l}$</th><th colspan="3">$q=1$</th><th rowspan="2">$ω_{l}$</th><th colspan="3">$q=100$</th></tr><tr><td>$w_{max}=0.1$</td><td>0.3</td><td>0.5</td><td>$w_{max}=0.1$</td><td>0.3</td><td>0.5</td></tr></thead><tbody><tr><td rowspan="2">(0,0)</td><td>2</td><td>1.0381</td><td>1.0497</td><td>1.1360</td><td>1.2934</td><td>1.1502</td><td>1.1641</td><td>1.2677</td><td>1.4424</td></tr><tr><td>4</td><td>0.9918</td><td>1.0044</td><td>1.0974</td><td>1.2532</td><td>1.0958</td><td>1.1105</td><td>1.2083</td><td>1.3746</td></tr><tr><td rowspan="2">(0,1,0)</td><td>2</td><td>1.0845</td><td>1.0951</td><td>1.1798</td><td>1.3438</td><td>1.1921</td><td>1.2056</td><td>1.3059</td><td>1.4761</td></tr><tr><td>4</td><td>1.0404</td><td>1.0524</td><td>1.1414</td><td>1.2920</td><td>1.1399</td><td>1.1540</td><td>1.2484</td><td>1.4100</td></tr><tr><td rowspan="2">(0.1,0.2)</td><td>2</td><td>1.7668</td><td>1.7744</td><td>1.8329</td><td>1.9396</td><td>1.8337</td><td>1.8425</td><td>1.9100</td><td>2.0324</td></tr><tr><td>4</td><td>1.7404</td><td>1.7486</td><td>1.8086</td><td>1.9059</td><td>1.8009</td><td>1.8079</td><td>1.8702</td><td>1.9856</td></tr></tbody></table>

TABLE 5. Nonlinear frequency $\omega_{n l}$ for C-H CNTRC sandwich beams $(L / h=10, q=1, V_{i}=0.05, V_{o}=0.1, \eta=0.4, \mu=0.4)$ .

<table><thead><tr><th rowspan="2">$(k_{w},k_{s})$</th><th rowspan="2">$h_{c}/h_{f}$</th><th rowspan="2">$ω_{l}$</th><th colspan="3">$q=1$</th><th rowspan="2">$ω_{l}$</th><th colspan="3">$q=100$</th></tr><tr><td>$w_{max}=0.1$</td><td>0.3</td><td>0.5</td><td>$w_{max}=0.1$</td><td>0.3</td><td>0.5</td></tr></thead><tbody><tr><td rowspan="2">(0,0)</td><td>2</td><td>1.9060</td><td>1.9207</td><td>2.0300</td><td>2.2142</td><td>2.1110</td><td>2.1247</td><td>2.2209</td><td>2.4575</td></tr><tr><td>4</td><td>1.8218</td><td>1.8368</td><td>1.9475</td><td>2.1313</td><td>2.0106</td><td>2.0237</td><td>2.1354</td><td>2.3216</td></tr><tr><td rowspan="2">(0,1,0)</td><td>2</td><td>1.9316</td><td>1.9462</td><td>2.0542</td><td>2.2363</td><td>2.1342</td><td>2.1499</td><td>2.2674</td><td>2.4661</td></tr><tr><td>4</td><td>1.8487</td><td>1.8634</td><td>1.9727</td><td>2.1544</td><td>2.0349</td><td>2.0497</td><td>2.1597</td><td>2.3458</td></tr><tr><td rowspan="2">(0.1,0.2)</td><td>2</td><td>2.4611</td><td>2.4708</td><td>2.5454</td><td>2.6791</td><td>2.6235</td><td>2.6351</td><td>2.7233</td><td>2.8797</td></tr><tr><td>4</td><td>2.3963</td><td>2.4057</td><td>2.4780</td><td>2.6074</td><td>2.5431</td><td>2.5535</td><td>2.6329</td><td>2.7748</td></tr></tbody></table>


![](./images/812778406948110340_5.jpg)

FIG. 5. Nonlinear mode shapes of CNTRC sandwich beams at $w_{\text{max}} = 0.5$ and $L/h = 15$: (a) C-C, (b) H-H and (c) C-H. [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812778406948110340_6.jpg)

FIG. 6. Nonlinear mode shapes of CNTRC sandwich beams at $L/h = 15$ for C-H boundary condition. [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812778406948110340_7.jpg)

![](./images/812778406948110340_8.jpg)

FIG. 7. Effect of core thickness on the nonlinear frequency ratio versus dimensionless amplitude curves of the CNTRC beams with $q=1$ $V_{i}=0$, $V_{o}=0.05$ and L/h = 15 (a) C-C, (b) H-H. [Color figure can be viewed at wileyonlinelibrary.com]

It is clear that when $V_{i}=0$, the amount of CNT volume fraction in the substrate is equal to zero, so we have sandwich beams with CNTRC face sheets with different CNT volume fractions $V_{CN}$ and when $V_{i}\neq0$ the substrate is consist of CNT. As mentioned before, when $q=0$, the CNT has a uniform distribution of volume fraction through the thickness of the beam in case of $V_{i}\neq0$ and CNT volume fraction is equal to zero in case of $V_{i}=0$. So, it becomes possible to compare the CNTR sandwich beam with a regular CNTR beam and beam without CNT. Figure 5 presents nonlinear fundamental mode shapes for CNTRC beams with various $q$ at $w_{\text{max}}=0.5$. It is found that the nanotube volume fraction $V_{cnt}$ has an insignificant effect on the nonlinear mode shape for all beams. The maximum amplitude occurs at the midpoint of the H-H and C-C beams but not for the C-H beam.

The nonlinear fundamental mode shapes for the displacement W, are plotted in Fig. 6 with various elastic foundation parameter at $w_{\text{max}}=0.5$. Note that $V_{i}=0$ shows that there is no CNT in the substrate and $q=1$ corresponds to the linear distribution of CNT on the face sheets. The maximum displacement approaches the center of the beam as we increase the elastic foundation stiffness.

![](./images/812778406948110340_9.jpg)

FIG. 8. Effect of state of aggregation on the nonlinear frequency ratio versus dimensionless amplitude curves of the CNTRC beams with $q=1$. [Color figure can be viewed at wileyonlinelibrary.com]

Figure 7 shows the effect of the different values of core-to-face sheet thickness ratio $(h_{c}/h_{f}=2,4,8)$ on the dimensionless nonlinear and linear vibration of various types of CNTRC sandwich beams when $V_{i}=0$, $V_{o}=0.05$, $q=1$ and $L/h=15$. Results show that an increase in the $h_{c}/h_{f}$ significantly reduces the linear frequency for both boundary conditions (C-C and H-H) but slightly decrease the nonlinear frequency ratio for H-H boundary conditions and it has an opposite trend for C-C boundary condition.

In Fig. 8, we find that fully dispersal of the randomly oriented CNTs (clustered, $\eta=\mu=0.4$ and $\eta=\mu=0.9$) results in the highest linear fundamental frequency, while an aggregated state would have a lower frequency ($\eta=0.4$, $\mu=0.1$ and $\eta=0.9$, $\mu=0.1$). That is because aggregates have lower modulus than individual dispersed CNTs and thus reduced reinforcing efficiency. But for dimensionless nonlinear frequency $(\omega_{nl}/\omega_{l})$, it is essential to consider both linear and nonlinear frequency. Fully dispersed CNT leads to both bigger linear and nonlinear frequencies but a lower nonlinear frequency ratio.

## CONCLUSIONS

The nonlinear free vibration of FG-CNTR sandwich beams rested on Pasternak foundation is studied based on Timoshenko beam theory and by applying von Kármán geometric nonlinearity. The effective material properties of the nanocomposite beam are assumed to be graded in the thickness direction and estimated by the MT approach. The GDQ method and a direct iterative approach is employed to obtain the nonlinear vibration frequencies and mode shapes of FG-CNTRC beams with different boundary conditions. Results present this fact that mechanical properties and therefore vibration of FG-CNTR sandwich beams are severely affected by CNTs aggregation. It can be concluded from numerical results that CNT volume fraction, aggregation state, core-to-face sheet thickness ratio $(h_{c}/h_{f})$, and end supporting conditions play an important role on the nonlinear frequencies and mode shapes. Also, it is seen that both Winkler and Pasternak elastic coefficients play effective roles in both frequency and mode shape.


REFERENCES

1. Y. Ngabonziza, J. Li, and C.F. Barry, Acta Mech., 220, 289 (2011).

2. R. Moradi-Dastjerdi, A. Pourasghar, and M. Foroutan, Acta Mech., 224, 2817 (2013).

3. S.I. Kundalwal and S.A. Meguid, Acta Mech., 226, 2035 (2015).

4. A. Allaoui, S. Bai, H.M. Cheng, and J.B. Bai, Comput. Sci. Technol., 62, 1993 (2002).

5. M. Griebel and J. Hamaekers, Comput. Methods Appl. Mech. Eng., 193, 1773 (2004).

6. Y. Han and J. Elliott, Comput. Mater. Sci., 39, 315 (2007).

7. M. Griebel, J. Hamaekers, and F. Heber, Comput. Mater. Sci., 45, 1097 (2009).

8. Y.J. Liu and X.L. Chen, Mech. Mater., 35, 69 (2003).

9. D. Luo, W.X. Wang, and Y. Takao, Compos. Sci. Technol., 67, 2947 (2007).

10. A. Selmi, C. Friebel, I. Doghri, and H. Hassis, Compos. Sci. Technol., 67, 2071 (2007).

11. D.C. Hammerand, G.D. Seidel, and D.C. Lagoudas, Mech. Adv. Mater. Struct., 14, 277 (2004).

12. T.S. Gates, G.M. Odegard, S.J.V. Frankland, and T.C. Clancy, Compos. Sci. Technol., 65, 2416 (2005).

13. G.D. Seidel and D.C. Lagoudas, Mech. Mater., 38, 884 (2006).

14. J.D. Eshelby, Proc R Soc, 241, 376 (1957).

15. T. Mori and K. Tanaka, Acta Metall, 21, 571 (1973).

16. R.M. Christensen and K.H. Lo, J. Mech. Phys. Solids, 27, 315 (1979).

17. Z. Hashin, J. Mech. Phys. Solids, 36, 719 (1988).

18. Q.-s. Yang, X.-q. He, X. Liu, F.-f. Leng, and Y.-W. Mai, Com- pos.: Part B, 43, 33 (2012).

19. P. Barai and G.J. Weng, Int. J. Plast., 27, 539 (2011).

20. B. Safaei, R. Moradi-Dastjerdi, Z. Qin, and F. Chu, Compos. Part B: Eng., 161, 44 (2019).

21. R. Kolahchi, B. Keshtegar, and M.H. Fakhar, J. Sandwich Struct. Mater., 109963621773107 (2017). https://doi.org/10.1177/ 1099636217731071.

22. B. Safaei, R. Moradi-Dastjerdi, and F. Chu, Compos. Struct., 192, 28 (2018).

23. R. Moradi-Dastjerdi and H. Malek-Mohammadi, J. Sandwich Struct. Mater., 19(6), 736 (2017).

24. R. Kolahchi, M.S. Zarei, M.H. Hajmohammad, and A. Nouri, Int. J. Mech. Sci., 130, 534 (2017).

25. R. Moradi-Dastjerdi, H. Malek-Mohammadi, and H. Momeni- Khabisi, ZAMM-J. Appl. Mathem. Mech., 97(11), 1418 (2017).

26. M.H. Hajmohammad, M.S. Zarei, A. Nouri, and R. Kolahchi, J. Sandwich Struct. Mater., 109963621772037 (2017). https:// doi.org/10.1177/1099636217720373.

27. R. Shokri-Oojghz, R. Moradi-Dastjerdi, H. Mohammadi, and K. Behdinan, Polym. Compos., 40, E1918 (2019). https://doi.org/ 10.1002/pc.25206.

28. S.J. Salami, Physica E, 76, 187 (2016).

29. H.J. Xiang and J. Yang, Compos. Part B/Eng, 39, 292 (2008).

30. L.L. Ke, J. Yang, and S. Kitipornchai, Compos. Struct., 92, 676 (2010).

31. L.L. Ke, Y. Wang, J. Yang, and S. Kitipornchai, Int. J. Eng. Sci., 50, 256 (2012).

32. M.H. Yas, A. Pourasghar, S. Kamarian, and M. Heshmati, Mater. Des., 49, 583 (2013).

33. A. Pourasghar and Z.T. Chen, Compos. Part B Eng., 99, 436 (2016).

34. M. Tang, Q. Ni, L. Wang, Y. Luo, and Y. Wang, Int. J. Eng. Sci., 85, 20 (2014).

35. A. Pourasghar and S. Kamarian, J. Vib. Control, 21, 2499 (2015).

36. N. Shafiei, A. Mousavi, and M. Ghadiri, Int. J. Eng. Sci., 102, 12 (2016).

37. R. Moradi-Dastjerdi and A. Pourasghar, J. Vib. Control, 22, 1062 (2016).

38. Y.I. Prylutskyy, S.S. Durov, O.V. Ogloblya, E.V. Buzaneva, and P. Scharff, Comput. Mater. Sci., 17, 352 (2000).

39. A. Pourasghar, M.H. Yas, and S. Kamarian, Polym. Compos., 34, 707 (2013).

40. C. Shu, Differential Quadrature and its Application in Engineer- ing, Springer, Berlin, Germany (2000).

41. C. Shu and B.E. Richards, Int. J. Numer Meth. Fluid, 15, 791 (1992).

42. J.E. Jam, A. Pourasghar, S. Kamarian, and S. Maleki, Polym. Compos., 34, 241 (2013).