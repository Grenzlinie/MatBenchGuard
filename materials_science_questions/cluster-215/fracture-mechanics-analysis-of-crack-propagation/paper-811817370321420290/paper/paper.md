# Numerical simulation of geofluid focusing and penetration due to hydraulic fracture

J.G. Wang ${ }^{\mathrm{a}, \mathrm{b}, *}$, Y. Zhang ${ }^{\mathrm{c}}$, J.S. Liu ${ }^{\mathrm{b}}$, B.Y. Zhang ${ }^{\mathrm{c}}$

${ }^{\mathrm{a}}$ Computational Geosciences Research Centre, Central South University, Changsha, China
${ }^{\mathrm{b}}$ School of Mechanical Engineering, The University of Western Australia, Australia
${ }^{\mathrm{c}}$ State Key Laboratory of Hydroscience and Engineering, Dept. of Hydraulic and Hydropower Engineering, Tsinghua University, Beijing, China

---

## A R T I C L E I N F O

**Article history:**
Received 24 April 2009
Accepted 25 November 2009
Available online 5 December 2009

**Keywords:**
Coupling process
Hydraulic fracture
Smeared theory
Meshless algorithm
Geofluid focusing
Geofluid penetrating

---

## A B S T R A C T

Ore body formation and mineralization are the consequence of transport, focusing and mixing processes of geofluids from the deep earth into the upper crust of the earth. These processes largely depend on geological structures, particularly heterogeneity such as cracks and faults. Both geological stress and geofluid-induced hydraulic pressure can create and alter the heterogeneity, thus changing the transport, focusing and mixing patterns. As a preliminary study, this paper investigates the intrusion and focusing of geofluids through simulation of the hydraulic fracturing process. First, the deformation of porous media and geofluid flow are coupled through the Biot's consolidation theory to consider both the elastoplasticity of porous media and the deformation induced evolution of permeability. Second, the crack induced anisotropy of stiffness and permeability is described, on the basis of a smeared theory and an equivalent anisotropic medium, to establish a criterion for tensile crack initiation and propagation at an element level. Finally, the resulting nonlinear equations are solved by a coupled algorithm of the meshless method and the finite element method (FEM). Numerical examples indicate that the proposed method is able to simulate the stress-induced crack propagation, geofluid intrusion and focusing in fluid-saturated porous media. It thus provides a potential tool for simulating the detailed mineralization process associated with the geological stress and geofluid intrusion.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The penetration and focusing of geofluids (such as magma, water and other fluids) can play important roles in the mineralization process (Lister and Kerr, 1991; Rubin, 1995; Zhang et al., 2006; Zhao et al., 1998, 2008b). Generally, the penetration of geofluids can create and widen the flow channels (Lister, 1990; Zhao et al., 2008c), while the focusing and mixing of geofluids can cause significant enrichment of minerals so that high grade and large ore deposits may be produced in the ore forming systems. Porous media such as permeable rocks are usually heterogeneous and saturated with geofluids (Zhao et al., 1997; 2001, 2004; Feltrin et al., 2009). Heterogeneity such as cracks, voids, fractures and faults provides storages and passages for the penetration (intrusion), focusing and mixing of geofluids (Zhao et al. 2006a, 2006c), thus causing mineral enrichment within the earth's crust. The heterogeneity is also altered when subjected to any change of geological stress and external geofluid intrusion. This alteration is usually expressed by local fractures as well as crack further propagations. The consequence is to locally change the spatial distribution (geometry) and material properties of porous media. Such a local alteration of geometry and material properties may further drive geofluids into weak zones, enlarge cracking zones, coalesce into larger and deeper flow passages, alter geofluid focusing, form new mixing zone, and finally produce various mineralization patterns (Zhao et al., 2006b, 2007a). Therefore, numerical simulation of such alterations is important to the understanding of mineral patterns associated with geochemical exploration.

The numerical simulation of the dynamic process of intrusion, focusing and mixing of geofluids is a challenging work. This dynamic process is complicated in both mathematical description and numerical solution algorithm. This is because the process usually involves local nonlinear deformation and damage of porous skeletons, initiation and opening of cracks, alteration of stiffness and permeability in the local damage zone, and coupling with geofluids flow, intrusion and focusing in the altered and interconnected porous channels. Generally, this complexity can be analyzed from following four aspects: First, the full coupling of this process is not easily described within a simple framework, but the Biot's consolidation theory (Biot, 1941) is a good basis. The Biot's theory describes the interaction of porous skeleton deformation and the geofluids flow. Second, the Biot's consolidation equation is so complicated that its solution is not a trivial work. Because of complicated geometry, complex boundary and initial conditions, several numerical algorithms such as the finite element method (FEM) and the particle simulation method (Zhao et al., 2007b) were successfully developed for dealing with large-scale crack generation problems in geological

---

* Corresponding author. School of Mechanical Engineering, The University of Western Australia, Australia. Tel.: +61 864888158.
E-mail addresses: jgwang@mech.uwa.edu.au, nuwjg@yahoo.com (J.G. Wang).

0375-6742/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.gexplo.2009.11.009

systems (Zhao et al., 2007c). Although FEM is widely used to solve crack propagation problems, it confronts some difficulties in simulating the propagation of a crack due to hydraulic fracturing and geofluid intrusion. Recently developed meshless methods as an alternative have demonstrated some advantages in the treatment of those moving boundary problems (Belytschko et al., 1996; Wang and Liu, 2002; Karim et al., 2002). Meshless methods may be particularly useful in the numerical simulation for geofluids intrusion and focusing problems. However, low computational efficiency is an obvious disadvantage of meshless methods when compared with FEM. A natural choice is to couple FEM and the meshless method to make full use of their advantages. Third, the criterion for the initiation and dynamic propagation of a crack (even in low speed) has not been well established so far although several criteria have been proposed (Ito, 2008). Finally, mechanical and hydraulic properties of porous media are evolved with local deformation and crack propagation, thus a relationship for this evolution should be established for numerical simulations.

As a preliminary step, this paper will investigate the intrusion and focusing of geofluids based on the Biot's consolidation theory and a smeared theory. It is organized as follows: Section 2 presents the fundamental concepts of the Biot's consolidation theory. With consideration of both the elastoplasticity of porous skeleton and the nonlinearity of permeability, the weak form of the coupling between skeleton deformation and fluid flow is derived. Section 3 discusses the discretization process of the weak form. In Section 4, a treatment for cracking-induced anisotropy of stiffness and permeability is proposed based on a smeared theory (Bazant et al., 1984). In Section 5, a coupled algorithm of FEM and the meshless method is proposed for the simulation of the dynamic propagation of cracking under either external forces or hydraulic pressure. Two classic problems, namely the crack propagation in a concrete beam and the hydraulic fracturing in a vertical porous column, are numerically investigated to check the numerical performances of the proposed algorithm. The conclusion and further study are discussed in Section 7.

## 2. Biot's consolidation theory

This section describes the interaction of porous skeletons and geofluids. As shown in Fig. 1, the layer of a porous medium is fully saturated with geofluids. This is a two-phase system, geofluids and porous skeleton. There is an interaction between these two phases at the pore-scale level. The Biot's consolidation theory (Biot, 1941) provides a good macro-level description for this interaction problem. If acceleration is not considered, the Biot's theory has six physical concepts as follows:

- Equilibrium equation of the porous skeleton-geofluids mixture
$$
\frac{\partial \sigma_{i j}}{\partial x_{j}}+b_{i}=0
\tag{1}
$$
or its incremental form in time interval $[t, t+\Delta t]$
$$
\frac{\partial \Delta \sigma_{i j}}{\partial x_{j}}+\Delta b_{i}=-\left(\frac{\partial \sigma_{i j}^{t}}{\partial x_{j}}+b_{i}^{t}\right).
\tag{2}
$$

- Relationship of displacement and strain for the porous skeleton
$$
\varepsilon_{i j}=\frac{1}{2}\left(\frac{\partial u_{i}}{\partial x_{j}}+\frac{\partial u_{j}}{\partial x_{i}}\right).
\tag{3}
$$

- Constitutive law of the porous skeleton in differential form
$$
d \sigma_{i j}^{\prime}=D_{i j k l} d \varepsilon_{k l}.
\tag{4}
$$

- Darcy's seepage law for geofluid flow
$$
q_{i}=-\frac{K_{i j}}{\gamma_{w}} \frac{\partial P}{\partial x_{j}}.
\tag{5}
$$

- Terzaghi's effective stress principle
$$
\sigma_{i j}=\sigma_{i j}^{\prime}+P \delta_{i j}.
\tag{6}
$$

- Continuity equation including the compressibility of the pore-fluid
$$
\frac{\partial \varepsilon_{v}}{\partial t}=-\frac{\partial q_{i}}{\partial x_{i}}+n^{\prime} c_{\mathrm{p}} \frac{\partial P}{\partial t}.
\tag{7}
$$

The volumetric strain of the pore skeleton is given as
$$
\varepsilon_{v}=\frac{\partial u_{i}}{\partial x_{i}}
\tag{8}
$$
where $\sigma_{i j}, \sigma_{i j}^{\prime}$ and $P$ are the total stress tensor, effective stress tensor and excess pore-fluid pressure (pore pressure is called later) at any time $t$ and $b_{i}$ the unit body force. $\Delta u_{i}$ is the displacement increment and $\Delta \sigma_{i j}$, $\Delta \varepsilon_{i j}$ the total stress and strain increments in time interval $[t, t+\Delta t]$. The discharge of the pore-fluid is $q_{i}$ in the $i$ th direction. $\gamma_{w}=\rho_{w} g$, where $\rho_{w}$ is the density of the pore-fluid and $g$ is the gravity acceleration. $\mathbf{D}_{i j k l}$ is the material matrix of the porous skeleton determined by the constitutive law of materials. $K_{i j}$ is a hydraulic conductivity tensor of the skeleton which usually has non-zero components $K_{x}$ in $x$ direction and $K_{y}$ in $y$ direction, respectively. The porosity is $n^{\prime}$ and the compressibility of the pore-fluid is denoted by $c_{\mathrm{p}}$. The spatial domain is denoted by $V$.

For the porous skeleton boundary
$$
\begin{cases}
u_{i}=\bar{u}_{i 0} & \text { on } S_{\bar{U}} \times[0, \infty) \\
\sigma_{i j}^{\prime} n_{j}=\overline{T_{i}} & \text { on } S_{\sigma} \times[0, \infty)
\end{cases}
\tag{9}
$$
where $\mathbf{n}=\left\{n_{1} n_{2} n_{3}\right\}$ is the outwards normal direction and $n_{i}$ is its directional cosine. The "×" denotes the "AND" for the spatial domain and temporal domain.

For the pore-fluid boundary
$$
\begin{cases}
P=P_{0} & \text { on } S_{p} \times[0, \infty) \\
q_{i}=q_{i 0} & \text { on } S_{q} \times[0, \infty)
\end{cases}
\tag{10}
$$

Initial condition
$$
\begin{cases}
u_{i}=0 \\
P=0
\end{cases} \text { on } V \times 0^{-}
\tag{11}
$$

The right sides are prescribed values. $S_{u}$ and $S_{\sigma}$ are the boundaries prescribed displacement and traction, respectively. $S_{p}$ and $S_{q}$ are the boundaries prescribed pore pressure and flux, respectively. $0^{-}$ is the

![](./images/811817370321420290_1.jpg)

Fig. 1. Problem statement.

time zero approaching from the minus side. The temporal domain $[0, \infty)$ indicates $t \in[0, \infty)$.

The variables within the time interval $[t, t+\Delta t]$ are of interest. If a one-step incremental approach is adopted in the time domain, the variables are all known at time $t$. The displacement increments of the porous skeleton satisfies the weak form of Eq. (2) as

$$
\begin{aligned}
& \int_{V}\{\delta(\Delta \varepsilon)\}^{T}\left\{\Delta \sigma^{t}\right\} d v+\int_{V}\left\{\delta\left(\frac{\Delta \Delta u_{i}}{\partial x_{i}}\right)\right\}^{T}\{P\}^{t+\Delta t} d v \\
& \quad-\int_{S_{\sigma}}\{\delta(\Delta \bar{u})\}^{T}\{n\} P^{t+\Delta t} d s-\int_{S_{\sigma}}\{\delta(\Delta \bar{u})\}^{T}\{\Delta \bar{T}\} d s \\
& \quad-\int_{V}\{\delta(\Delta \bar{u})\}^{T}\{\Delta b\} d v=-\int_{V}\{\delta(\Delta \varepsilon)\}^{T}\left\{\sigma^{t}\right\} d v \\
& \quad+\int_{S_{\sigma}}\{\delta(\Delta \bar{u})\}^{T}\{\bar{T}\}^{t} d v+\int_{V}\{\delta(\Delta \bar{u})\}^{T}\left\{b^{t}\right\} d v
\end{aligned}
$$

where $\delta(\Delta \bar{u})$ is the variation of displacement increment. The " $\delta$ " denotes the variation. The term at the right hand side includes the un-balanced force at the previous time step. This un-balanced force can be automatically corrected in the next step. Thus Eq. (12) can prevent numerical error from accumulation. This auto-corrector is especially useful in the incremental computation schemes for dissipation problems.

The weak form of the continuity equation is obtained as follows:

$$
\begin{aligned}
& \frac{1}{\gamma_{w}} \int_{V}\left\{\frac{\partial \delta P}{\partial x_{i}}\right\}^{T}\left\{K_{i} \frac{\partial P}{\partial x_{i}}\right\} d v+\int_{V}\{\delta P\}^{T} \frac{\partial}{\partial t}\left\{\frac{\partial \Delta u_{i}}{\partial x_{i}}\right\} d v \\
& \quad-\int_{V} n^{\prime} c_{p} \delta P \frac{\partial P}{\partial t} d v-\frac{1}{\gamma_{w}} \int_{S_{q}}\{\delta P\}^{T}\{q\} d s=0
\end{aligned}
$$

where $\delta P$ expresses the variation of the pore pressure.

### 3. Discretization of the weak form

A spatial discretization for displacement and pore pressure is as follows:

$$
\mathbf{u}=\sum_{i=1}^{n} N_{i} \mathbf{u}_{i} \quad P=\sum_{i=1}^{n} N_{i} P_{i}
$$

where $\mathbf{u}_{i}$ and $P_{i}$ are the nodal displacement and pore pressure, respectively. Shape function $N_{i}$ can be determined through either the radial PIM (Wang and Liu, 2002) or FEM. The use of the same shape functions for pore pressure and displacement is effective to the solution of Biot's consolidation theory (Wang et al., 2002). Based on the above approximation, the weak form of Eq. (12) can be discretized as

$$
K \Delta \mathbf{u}+K_{V} \mathbf{P}=F_{b}+F_{t}+F_{p}
$$

where

$$
\begin{aligned}
& K=\int_{V} B^{T} D B d v, \quad K_{V}=\int_{V} B_{V}^{T} N d v, \quad F_{b}=\int_{V} N^{T} b d v \\
& F_{t}=\int_{S_{\sigma}} N^{T} T d s, \quad F_{p}=\int_{S_{\sigma}} N^{T} P d s .
\end{aligned}
$$

For a plane strain problem, the sub-matrices of matrices $\mathbf{B}$ and $\mathbf{B}_{V}$ are expressed as

$$
\mathbf{B}_{i}=\left[\begin{array}{cc}
N_{i, x} & 0 \\
0 & N_{i, y} \\
N_{i, y} & N_{i, x}
\end{array}\right], \mathbf{B}_{V i}=\left[\begin{array}{cc}
N_{i, x} & 0 \\
0 & N_{i, y}
\end{array}\right]
$$

where $\mathbf{D}$ is the material matrix. $F_{b}, F_{t}$ and $F_{p}$ are the equivalent nodal forces produced by body force, traction and pore pressure on boundary $S_{\sigma}$, respectively.

After differentiating with time, Eq. (15) becomes

$$
K \frac{d \mathbf{u}}{d t}+K_{V} \frac{d \mathbf{P}}{d t}=\frac{d\left(F_{b}+F_{t}+F_{p}\right)}{d t} .
$$

The continuity equation (i.e. Eq. (13)) is discretized into

$$
K_{V}^{T} \frac{d \mathbf{u}}{d t}-K_{p t} \frac{d \mathbf{P}}{d t}+K_{p} \mathbf{P}=F_{q}
$$

where

$$
K_{p}=\int_{V} B_{p}^{T} K B_{p} d v, K_{p t}=\int_{V} n^{\prime} \beta N^{T} N d v, F_{q}=\int_{S_{q}} N^{T} q n d s
$$

and the sub-matrices of $\mathbf{K}$ and $\mathbf{B}_{p}$ are

$$
\mathbf{K}_{i}=\left[\begin{array}{cc}
K_{x} & 0 \\
0 & K_{y}
\end{array}\right], \mathbf{B}_{P i}=\left[\begin{array}{ll}
N_{i, x} & N_{i, y}
\end{array}\right] .
$$

A single step method is applied to the time domain:

$$
\int_{t}^{t+\Delta t} f(x) d x=\Delta t[(1-\theta) f(t)+\theta f(t+\Delta t)]
$$

where $\theta$ is a parameter corresponding to different approaches (Wang et al., 2002).

A system equation for a transient response problem is obtained as

$$
\begin{aligned}
& {\left[\begin{array}{cc}
K & K_{V} \\
K_{V}^{T} & \left(\Delta t \theta K_{p}-K_{p t}\right)
\end{array}\right]\left\{\begin{array}{l}
\Delta \mathbf{u} \\
\Delta \mathbf{P}
\end{array}\right\}=\left[\begin{array}{cc}
0 & 0 \\
0 & -\Delta t K_{p}
\end{array}\right]\left\{\begin{array}{l}
\mathbf{u}^{t} \\
\mathbf{P}^{t}
\end{array}\right\}} \\
& \quad+\left\{\begin{array}{c}
\Delta F_{b}+\Delta F_{t}+\Delta F_{p} \\
\Delta t F_{q}
\end{array}\right\} .
\end{aligned}
$$

If the pore pressure, $\mathbf{P}^{t+\Delta t}=\mathbf{P}^{t}+\Delta \mathbf{P}$, is used as unknowns, Eq. (23) can be rewritten as

$$
\left[\begin{array}{cc}
K & K_{V} \\
K_{V}^{T} & \left(\Delta t \theta K_{p}-K_{p t}\right)
\end{array}\right]\left\{\begin{array}{c}
\Delta \mathbf{u} \\
\mathbf{P}^{t+\Delta t}
\end{array}\right\}=\left\{\begin{array}{c}
F_{b}^{t}+F_{t}^{t}+F_{p}^{t}+F_{r}^{t} \\
\Delta t F_{q}-\left[\Delta t(1-\theta) K_{p}+K_{p t}\right] \mathbf{P}^{t}
\end{array}\right\}
$$

where

$$
\begin{aligned}
& F_{b}^{t}=\int_{V} N^{T} \Delta b d v, F_{t}^{t}=\int_{S_{\sigma}} N^{T} \Delta T d s, F_{p}^{t}=\int_{S_{\sigma}} N^{T} P d s \\
& F_{r}^{t}=-\int_{V} B^{T} \sigma^{t} d v+\int_{S_{\sigma}} N^{T} \bar{T}^{t} d s+\int_{V} N^{T} b^{t} d v .
\end{aligned}
$$

### 4. Cracking-induced changes of stiffness and permeability

The smeared theory improved by Bazant et al. (1984) is used to express the cracking-induced change of stiffness and permeability. Further, fracture energy is introduced to control the softening process of the porous medium.

#### 4.1. Criterion for tensile cracking

Our test results for compacted clay show that cracking occurs along a crack plane perpendicular to the minor principal stress $\sigma_{3}$ direction when the following criterion is satisfied:

$$
\sigma_{3}<\sigma_{t}
$$

where $\sigma_{t}$ is the uniaxial tensile strength of the porous medium.

Test results further suggested a combined criterion for both tensile failure and shear failure, as shown in Fig. 2 for a typical comparison with test data.

![](./images/811817370321420290_2.jpg)

Fig. 2. A combined criterion for tensile and shear failures.

### 4.2. Cracking-induced anisotropy
After cracking, the porous medium is assumed to lose its stiffness along the normal direction of the crack but other directions are not affected. The porous medium becomes anisotropic. This change is expressed through the alteration of the stiffness matrix at each stress point. For example, the Hooke's law of isotropic and crack-free materials (plane strain) is expressed as

$$
\left\{\begin{array}{c}
\sigma_{x} \\
\sigma_{y} \\
\tau_{x y}
\end{array}\right\}=\left[\begin{array}{ccc}
\frac{E(1-v)}{(1+v)(1-2 v)} & \frac{E v}{(1+v)(1-2 v)} & 0 \\
\frac{E v}{(1+v)(1-2 v)} & \frac{E(1-v)}{(1+v)(1-2 v)} & 0 \\
0 & 0 & G
\end{array}\right]\left\{\begin{array}{c}
\varepsilon_{x} \\
\varepsilon_{y} \\
\gamma_{x y}
\end{array}\right\}
\tag{27}
$$

where $E$ is the Young's modulus in tension, $\nu$ the Poisson's ratio and $G$ the shear modulus. For convenience, local coordinates are set up along the crack direction. In this coordinate system, the above stress-strain relationship is rewritten as

$$
\left\{\begin{array}{c}
\sigma_{x} \\
\sigma_{y} \\
\tau_{x y}
\end{array}\right\}=\left[\begin{array}{ccc}
D_{11}^{\prime} & D_{12}^{\prime} & 0 \\
D_{21}^{\prime} & D_{22}^{\prime} & 0 \\
0 & 0 & D_{33}^{\prime}
\end{array}\right]\left\{\begin{array}{c}
\varepsilon_{x} \\
\varepsilon_{y} \\
\gamma_{x y}
\end{array}\right\}=\left[D^{\prime}\right]\left\{\begin{array}{c}
\varepsilon_{x} \\
\varepsilon_{y} \\
\gamma_{x y}
\end{array}\right\}
\tag{28}
$$

where

$$
\begin{aligned}
& D_{11}^{\prime}=\frac{\mu(1-v) E}{1-v-2 \mu v^{2}}, \quad D_{22}^{\prime}=\frac{\left(1-\mu v^{2}\right) E}{(1+v)\left(1-v-2 \mu v^{2}\right)} \\
& D_{33}^{\prime}=\chi G, \quad D_{12}^{\prime}=D_{21}^{\prime}=\frac{\mu v E}{1-v-2 \mu v^{2}}
\end{aligned}
\tag{29}
$$

where $\chi$ and $\mu$ are the reduction coefficients for the shear modulus and Young's modulus, respectively. In our computation, $\chi=0.001$ and $\mu=0.01$.

In the global coordinate system, the stress-strain relationship is obtained through the following coordinate transformation:

$$
[D]=[R]^{T}\left[D^{\prime}\right][R]
\tag{30}
$$

where transformation matrix $[\mathbf{R}]$ is

$$
[R]=\left[\begin{array}{ccc}
\cos ^{2} \beta & \sin ^{2} \beta & \cos \beta \sin \beta \\
\sin ^{2} \beta & \cos ^{2} \beta & -\cos \beta \sin \beta \\
-2 \cos \beta \sin \beta & 2 \cos \beta \sin \beta & \cos ^{2} \beta-\sin ^{2} \beta
\end{array}\right]
\tag{31}
$$

where $\beta$ is the angle of the local coordinates in relation to the global coordinates.

### 4.3. Cracking-induced alteration of permeability
The crack will enlarge the existing flow channel and may create new channels for pore-fluid flow, thus enhancing the permeability of the porous medium. The local permeability matrix is

$$
\left\{K^{\prime}\right\}=\left\{k_{p} k_{t}\right\}^{T}
\tag{32}
$$

where $k_{p}$ is the permeability perpendicular to the crack which is not affected by the crack. $k_{t}$ is the permeability in the crack direction which can be expressed as a function of effective normal stress $\sigma_{n}$ (if stress $\sigma_{n}$ does not change significantly).

$$
k_{t}=k_{t 0} e^{-\alpha \sigma_{n}}
\tag{33}
$$

where $\alpha$ is a constant. A typical curve is shown in Fig. 3 when $\alpha=0.1 /$ kPa.

The permeability in global coordinates is

$$
\{K\}=\left[T_{c}\right]\left\{K^{\prime}\right\}
\tag{34}
$$

where

$$
\left[T_{c}\right]=\left[\begin{array}{cc}
\cos \beta & \sin \beta \\
-\sin \beta & \cos \beta
\end{array}\right].
\tag{35}
$$

### 4.4. Cracking-induced softening
Our laboratory test results revealed that the compacted clay has softening deformation even when in tension. The softening deforma- tion depends on its dry density and moisture. In order to rule out the

![](./images/811817370321420290_3.jpg)

Fig. 3. Change of permeability with normal tensile stress.

mesh-dependency in crack zones, the concept of fracture energy of a crack is introduced to adjust the stress-strain relationship in the softening zone, thus guaranteeing the uniqueness of solutions. The fracture energy of a crack refers to the dissipated energy per unit length of crack propagation. In computation, the fracture energy is kept constant in a given medium. The principle used in smeared theory has been proved to be equivalent to the opening width theory where a crack is treated as a discontinuity of displacement. However, the smeared theory is still in the framework of continua while the opening width theory introduces strong discontinuity in computation, thus affecting computational complexity and efficiency.

## 5. Coupled algorithm of FEM and the meshless method
As discussed in the introduction, meshless methods are superior to FEM in the treatment of moving boundaries. However, their computational efficiency is much lower than FEM. A good choice is to take advantages of both methods simultaneously in computation, where the moving boundary zone is treated by the meshless method and the rest zones are treated by FEM.

The radial PIM meshless method has following fundamental interpolation:
$$
u(\mathbf{x})=\left[\begin{array}{ll}
\mathbf{C}^{\mathrm{T}}(\mathbf{x}) & \mathbf{P}^{\mathrm{T}}(\mathbf{x})
\end{array}\right] \mathbf{H}^{-1}\left\{\begin{array}{c}
\mathbf{u}_{\mathbf{e}} \\
0
\end{array}\right\}=\mathbf{N}(\mathbf{x}) \mathbf{u}_{\mathbf{e}}
\tag{36}
$$
where the shape function is
$$
N_{k}(\mathbf{x})=\sum_{i=1}^{n} C_{i}(\mathbf{x}) \bar{H}_{i, k}+\sum_{j=1}^{m} P_{j}(\mathbf{x}) \bar{H}_{n+j, k}.
\tag{37}
$$

The radial basis function is taken as
$$
C_{i}(x, y)=\left(r_{i}^{2}+R^{2}\right)^{q}.
\tag{38}
$$

The polynomial basis function can be taken as
$$
P_{j}(x, y)=[1, x, y, \cdots]
\tag{39}
$$
where $\mathbf{H}$, a location matrix of an influence domain, is completely determined by the nodal distribution within the influence domain (see Wang et al., 2002). $R$ and $q$ are the shape parameters which are taken as $R=0.1$ and $q=1.03$ and $\mathbf{u}_{e}$ is a vector whose elements are $u\left(x_{i}\right)$, namely the nodal value at nodal point $x_{i}$. The $\bar{H}_{i, k}$ and $\bar{H}_{n+j, k}$ are the components of matrix $\mathbf{H}^{-1}$ which makes $\mathbf{H}^{-1} \mathbf{H}=\mathbf{I}$.

The shape function has following two important properties:
First, the Kronecker delta property
$$
N_{i}\left(x=x_{j}\right)=\left\{\begin{array}{ll}
1 & i=j, \quad j=1,2, \ldots, n \\
0 & i \neq j, \quad i, j=1,2, \ldots, n
\end{array}.\right.
\tag{40}
$$

Second, the reproducing properties of polynomials in zero- and one-order depending on polynomial basis $P(x)$.
$$
\sum_{i=1}^{n} N_{i}(x)=1, \quad \sum_{i=1}^{n} N_{i}(x) x_{i}=x.
\tag{41}
$$

With these properties, the coupling algorithm of the radial PIM and FEM is simple. As shown in Fig. 4, the node points along the interface are shared by the radial PIM and FEM. The integral is done over their respective own domains. In order to improve the numerical accuracy along the interface, the meshless interpolation can include those nodes near the interface in the FEM domain. Our numerical examples indicated that the accuracy could be well controlled through this direct coupling algorithm. In an influence domain, a crack can be regarded as the obstacle in the influence domain of any node. The shade part due to crack is shown in Fig. 5. This can be described through a visibility criterion (Belytschko et al., 1996) when computing the influence distance of node Q. Other numerical algorithms include the combination of an incremental method and an iterative method to trace the crack propagation.

![](./images/811817370321420290_4.jpg)

Fig. 4. Direct coupling algorithm of radial PIM and FEM.

## 6. Numerical performances
Two examples are used to check the capability of the currently proposed algorithm. Example 1 demonstrates its capability of simulating the crack development in a concrete beam (without geofluids). Shear locking effect of crack propagation and nodal density (mesh-dependency) on meshless methods are studied. Example 2 is a two-phase system. The process of hydraulic fracture is numerically simulated. The geofluid focusing and penetration are observed.

### 6.1. Example 1
Fig. 6 is a benchmark problem in fracture mechanics (where $D=300$ mm). Laboratory tests were implemented by Galvez et al. (1998) to observe the crack propagation in a concrete beam. The material parameters used in computation are listed in Table 1. For this problem, the crack propagation and displacement at the loading point

![](./images/811817370321420290_5.jpg)

Fig. 5. Node-crack visibility for meshless distance.

![](./images/811817370321420290_6.jpg)

Fig. 6. Model problem for crack development.

**Table 1**
Material parameters used in computation.

| Material | Young's modulus $E$ (GPa) | Poisson's ratio $\nu$ | Tensile strength $\sigma_{t}$ (MPa) | Fracture energy $G_{f}$ (N/m) |
|----------|---------------------------|-----------------------|-------------------------------------|--------------------------------|
| Concrete | 30                        | 0.2                   | 3.0                                 | 69                             |

are of interest. FEM usually confronts shear locking and mesh-dependency phenomena at the tip zone of the crack. These phenomena will be investigated here for the proposed method.

For the shear locking, Fig. 7 is the comparison of crack development patterns between the laboratory observation and numerical simulation. For the mesh-dependency, a three-point beam bending test by Peterson (1981) was computed (see Fig. 8 (a)). This plain concrete has the same Young's modulus and Poisson's ratio as used previously but its tensile strength is $\sigma_{t}=3.33$ MPa and fracture energy is $G_{f}=124$ N/m. Mesh-dependency (mesh sensitivity) can be identified through the observation of the loading-displacement curve at the decrease stage. Fig. 8(b) and (c) are two nodal distributions, namely dense and sparse nodes, used in the potential propagation zone of the crack. The computed displacement at the loading point is presented in Fig. 9, where upper and lower limits were obtained from laboratory tests. These two examples indicated that the numerical simulations are generally in good agreement with laboratory observations. The proposed numerical algorithm could effectively avoid the sensitivity of node density without shear locking.

### 6.2. Example 2

A typical laboratory test shown in Fig. 10 is numerically simulated to observe the pore pressure distribution at different stages due to the hydraulic fracturing process. The front column is comprised of gravel so as to support the clay block. A homogeneous water pressure is applied to the vertical surface of the gravel column. The back surface of the clay block has zero water pressure. A weak zone is located at the middle position. The weak zone and surroundings are discretized by the radial PIM and the rest zones are discretized by FEM. The

![](./images/811817370321420290_7.jpg)

![](./images/811817370321420290_8.jpg)

(a) Dimension and loadings for three-point beam bending test

![](./images/811817370321420290_9.jpg)

(b) Dense nodes

![](./images/811817370321420290_10.jpg)

Fig. 8. Two node densities for meshless methods to check mesh sensitivity.

mechanical properties of each material are listed in Table 2. Typical water pressures at different stages are shown in Fig. 11. At the initial stage, the high gradient of water pressure is observed around the tip of the weak zone. The weak zone is penetrated and opened by the water pressure (see Table 3). However, the penetration force gradually reduces with further seepage. The gradient of water pressure becomes evenly distributed at the stable seepage stage although some concentration is still observed around the tip of the weak zone.

## 7. Discussions and conclusions

Ore body formation and mineralization are controlled by complicated physical and chemical processes that involve the transport, focusing and mixing of geofluids. The penetration of geofluids can

![](./images/811817370321420290_11.jpg)

![](./images/811817370321420290_12.jpg)

Fig. 10. Model problem for hydraulic fracture.

create and widen the flow channels in permeable rocks, while the focusing and mixing of geofluids can cause significant enrichment of minerals so that high grade and large ore deposits can be produced in the ore forming systems. For permeable rocks, it is known that the heterogeneity such as cracks and faults plays an important role in the focusing and mixing of geofluids. Since both geological stress and geofluid-induced hydraulic pressure can initialize and alter this kind of heterogeneity, it needs to be considered in the ore forming process. Toward this direction, a numerical simulation tool is proposed in this paper to dynamically simulate the initiation and propagation of cracks and faults in fluid-saturated porous media. This tool is based on the Biot's consolidation theory and a smeared theory. It has been applied to a dry porous medium sample and a hydraulic fracturing example. From these preliminary investigations, the following understandings and conclusions can be drawn:

First, the initiation and propagation of cracks can be described by the proposed coupling algorithm of the radial PIM meshless method and FEM within the framework of the Biot's consolidation theory. This algorithm can effectively avoid the sensitivity of node density on numerical results after introducing fracture energy in the softening zone, so that shear locking in the crack propagation zone was not observed.

Second, the transport and focusing of geofluids mainly occur along the weak and fractured zones. It has also been observed that the geofluids intrusion can further penetrate a porous medium through hydraulic fracturing if the breakdown pressure of the porous medium is exceeded. At the tip of the crack, the focusing of geofluids is intensified, and in two sides of a crack/fault, leakage of geofluids is observed and pressure gradient is rapidly reduced. Further, the focusing and penetrating of geofluids locally interact with the deformation of surrounding materials in the crack tip zone.

Ore body formation and mineralization are commonly treated as a fully coupled problem involving multi-physical and chemical processes (Zhao et al., 2009). The proposed numerical tool that considers the interaction between material cracking and geofluid flow in this paper is just a starting point for the potential simulation of several mineralization problems in ore forming systems. Further development of this tool should consider thermal driving (temperature gradient) and chemical reaction processes. The thermal driving process can cause the mixing of geofluids (Zhao et al. 1997, 2008a) and the

![](./images/811817370321420290_13.jpg)

Fig. 11. Mechanism of hydraulic fracturing due to initial weak zone.

<table>
<caption>Table 2 Material parameters in computation.</caption>
<thead>
<tr>
<th>Material</th>
<th>Young's modulus<br>E (MPa)</th>
<th>Poisson's ratio<br>$\nu$</th>
<th>Hydraulic conductivity<br>$K$ (m/s)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gravel</td>
<td>10</td>
<td>0.3</td>
<td>1</td>
</tr>
<tr>
<td>Compacted clay</td>
<td>1</td>
<td>0.3</td>
<td>$1.0\mathrm{E}-8$</td>
</tr>
<tr>
<td>Weak zone</td>
<td>0.01</td>
<td>0.2</td>
<td>1</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3 Numerical results of stress at the tip points and opening of crack.</caption>
<thead>
<tr>
<th>Water pressure<br>(kPa)</th>
<th>Stress at tip point 1<br>(kPa)</th>
<th>Stress at tip point 2<br>(kPa)</th>
<th>Maximum opening<br>(mm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>100</td>
<td>$-36$</td>
<td>$-3$</td>
<td>0.43</td>
</tr>
<tr>
<td>200</td>
<td>$-24$</td>
<td>$-6$</td>
<td>0.85</td>
</tr>
<tr>
<td>300</td>
<td>$-12$</td>
<td>$-9$</td>
<td>1.29</td>
</tr>
</tbody>
</table>

chemical reaction can control the reaction front propagation along the two sides of a crack/fault as well as in the tip zone (Zhao et al. 2007a,b).

## Acknowledgements

This work is financially supported by Singapore DSTA (Project No. MINDEF-NUS-DIRP/2004/06 and MINDEF-NUS-JPP/07/07), China Na- tional Science Fund (Project No. 50639060), 973 Program (Project No. 2010CB732103), and Western Australia Energy Research Alliance (WA: ERA). The authors heartily appreciate the two reviewers. Their comments are very helpful in the improvement of this paper.

## References

Bazant, Z.P., Belytschko, T., Chang, T.P., 1984. Continuum theory for strain-softening. Journal of Engineering Mechanics-ASCE 110 (12), 1666-1692.

Belytschko, T., Krongauz, K., Organ, D.Y., Fleming, M., Krysl, P., 1996. Meshless methods: an overview and recent development. Computer Methods in Applied Mechanics and Engineering 139 (1-4), 3-47.

Biot, M.A., 1941. General theory of three-dimensional consolidation. Journal of Applied Physics 12 (2), 155-164.

Feltrin, L., McLellan, J.G., Oliver, N.H.S., 2009. Modelling the giant, Zn-Pb-Ag Century deposit, Queensland, Australia. Computers & Geosciences 35 (1), 108-133.

Galvez, J.C., Elices, M., Guinea, G.V., Planas, J., 1998. Mixed mode fracture of concrete under proportional and nonproportional loading. International Journal of Fracture 94 (3), 267-284.

Ito, T., 2008. Effect of pore pressure gradient on fracture initiation in fluid saturated porous media: rock. Engineering Fracture Mechanics 75 (7), 1753-1762.

Karim, M.R., Nogami, T., Wang, J.G., 2002. Analysis of transient response of saturated porous elastic soil under cyclic loading using element-free Galerkin method. International Journal of Solids and Structures 39 (6), 6011-6033.

Lister, J.R., 1990. Buoyancy-driven fluid fracture: the effects of material toughness and of low-viscosity precursors. Journal of Fluid Mechanics 210, 263-280.

Lister, J.R., Kerr, R.C., 1991. Fluid-mechanical models of crack propagation and their application to magma transport in dykes. Journal of Geophysical Research 96 (B6), 10049-10077.

Peterson, P.E., 1981. Crack Growth and Development of Fracture Zones in Plain Concrete and Similar Materials. Division of Building Materials, Lund Institute of Technology. TVBM-1006.

Rubin, A.M., 1995. Propagation of magma-filled cracks. Annual Review of Earth and Planetary Sciences 23, 287-336.

Wang, J.G., Liu, G.R., 2002. A point interpolation meshless method based on radial basis functions. International Journal for Numerical Methods in Engineering 54 (11), 1623-1648.

Wang, J.G., Liu, G.R., Lin, P., 2002. Numerical analysis of Biot's consolidation process by radial point interpolation method. International Journal of Solids and Structures 39 (6), 1557-1573.

Zhang, Y., Sorjonen-Ward, P., Ord, A., 2006. Modelling fluid transport associated with mineralization and deformation in the Outokumpu Cu-Zn-Co deposit, Finland. Journal of Geochemical Exploration 89 (1-3), 465-469.

Zhao, C., Mühlhaus, H.B., Hobbs, B.E., 1997. Finite element analysis of steady-state natural convection problems in fluid-saturated porous media heated from below. International Journal for Numerical and Analytical Methods in Geomechanics 21, 863-881.

Zhao, C., Hobbs, B.E., Mühlhaus, H.B., 1998. Finite element modelling of temperature gradient driven rock alteration and mineralization in porous rock masses. Computer Methods in Applied Mechanics and Engineering 165, 175-187.

Zhao, C., Hobbs, B.E., Walshe, J.L., Mühlhaus, H.B., Ord, A., 2001. Finite element modeling of fluid-rock interaction problems in pore-fluid saturated hydrothermal/sedimentary basins. Computer Methods in Applied Mechanics and Engineering 190, 2277-2293.

Zhao, C., Hobbs, B.E., Ord, A., Peng, S., Mühlhaus, H.B., Liu, L., 2004. Theoretical investigation of convective instability in inclined and fluid-saturated three-dimensional fault zones. Tectonophysics 387, 47-64.

Zhao, C., Hobbs, B.E., Hornby, P., Ord, A., Peng, S., 2006a. Numerical modelling of fluids mixing, heat transfer and non-equilibrium redox chemical reactions in fluid- saturated porous rocks. International Journal for Numerical Methods in Engineering 66, 1061-1078.

Zhao, C., Hobbs, B.E., Ord, A., Hornby, P., 2006b. Chemical reaction patterns due to fluids mixing and focusing around faults in fluid-saturated porous rocks. Journal of Geochemical Exploration 89, 470-473.

Zhao, C., Hobbs, B.E., Ord, A., Hornby, P., Peng, S., Liu, L., 2006c. Theoretical and numerical analyses of pore-fluid flow patterns around and within inclined large cracks and faults. Geophysical Journal International 166, 970-988.

Zhao, C., Hobbs, B.E., Ord, A., Hornby, P., Peng, S., Liu, L., 2007a. Mineral precipitation associated with vertical fault zones: the interaction of solute advection, diffusion and chemical kinetics. Geofluids 7, 3-18.

Zhao, C., Hobbs, B.E., Ord, A., Hornby, P., Peng, S., Liu, L., 2007b. Particle simulation of spontaneous crack generation problems in large-scale quasi-static systems. International Journal for Numerical Methods in Engineering 69, 2302-2329.

Zhao, C., Hobbs, B.E., Ord, A., Peng, S., Liu, L., 2007c. An upscale theory of particle simulation for two-dimensional quasi-static problems. International Journal for Numerical Methods in Engineering 72, 397-421.

Zhao, C., Hobbs, B.E., Ord, A., 2008a. Convective and Advective Heat Transfer in Geological Systems. Springer, Berlin.

Zhao, C., Hobbs, B.E., Hornby, P., Ord, A., Peng, S., Liu, L., 2008b. Theoretical and numerical analyses of chemical-dissolution front instability in fluid-saturated porous rocks. International Journal for Numerical and Analytical Methods in Geomechanics 32 (9), 1107-1130.

Zhao, C., Hobbs, B.E., Ord, A., Peng, S., 2008c. Particle simulation of spontaneous crack generation associated with the laccolithic type of magma intrusion processes. International Journal for Numerical Methods in Engineering 75 (1), 1172-1193.

Zhao, C., Hobbs, B.E., Ord, A., 2009. Fundamentals of Computational Geoscience: Numerical Methods and Algorithms. Springer, Berlin.