ORIGINAL PAPER

S. Pouresmaeeli · S. A. Fazelzadeh

# Frequency analysis of doubly curved functionally graded carbon nanotube-reinforced composite panels

Received: 2 January 2016 / Revised: 11 April 2016
© Springer-Verlag Wien 2016

Abstract Vibration characteristics of moderately thick doubly curved functionally graded composite panels reinforced by carbon nanotube are analyzed. Here, special cases of doubly curved shell panels such as spherical, cylindrical and hyperbolic paraboloid panels and five different distributions of carbon nanotubes through the thickness direction are considered. By utilizing the modified rule of mixture, mechanical properties are esti- mated. The equations of motion are derived via the first-order shear deformation theory, and non-dimensional frequencies are obtained by the use of Galerkin's method. The suggested model is justified by a good agreement between the results given by present model and available data in the literature. The influences of volume frac- tion of carbon nanotubes, thickness ratio, aspect ratio, curvature ratio, and shallowness ratio on the frequencies of moderately thick doubly curved nanocomposite shell panels are also examined. Furthermore, the effect of various boundary conditions on the frequency analysis of doubly curved nanocomposite panels is studied, and the corresponding mode shapes are depicted.

## 1 Introduction

Experimental and theoretical researches show that carbon nanotubes (CNTs) possess remarkable mechanical properties such as high elastic modulus, high tensile strength and stiffness [1–3]. Based on these unique prop- erties, CNTs have been utilized in various fields of nanotechnology industry. Recently, CNTs are considered as appropriate candidates for the reinforcement of nanocomposites [4,5]. Nanocomposites made of a polymer as matrix and CNTs as reinforcement are well known as carbon nanotube-reinforced composites (CNTRCs). At the early studies, the distribution of the CNTs in the CNTRCs was assumed to be uniform along the thickness direction, and nanocomposites were considered as homogeneous ones. Later, to enhance the effectiveness of reinforcement, the CNTs were assumed to be distributed functionally graded along the thickness direc- tion of the nanocomposite. These kinds of nanocomposites are well known as functionally graded carbon nanotube-reinforced composites (FG-CNTRCs). In FG-CNTRC, mechanical properties of the nanocomposite alter continuously and gradually from one side to the other side along the thickness direction, the same as conventional functionally graded material (FGM). In order to evaluate characteristics of CNTRCs, mechanical and elastic properties of CNTRCs have been investigated by many researchers [6–10]. It was reported that the elastic stiffness of a nanocomposite improves between 36 and 42 % with an addition of a volume fraction of CNTs by 0.487 % by Qian et al. [6]. Moreover, Hu et al. [8] found that the characteristics of the reinforcement are dependent on the CNT length and transition layer and can be improved from 10 to 70 % along the CNT direction, with an addition of volume fraction from 0.48 to 2.75 %. The aforementioned researches showed

S. Pouresmaeeli · S. A. Fazelzadeh (⊠)
School of Mechanical Engineering, Shiraz University, Shiraz 71963-16548, Iran
E-mail: Fazelzad@shirazu.ac.ir
Tel.: +98 7136133238
Fax: +98 7136473511

Published online: 21 May 2016

that adding CNTs even at very low volume fractions improves mechanical and elastic properties of CNTRCs. Hence, CNTRCs can be applied extensively in weight-sensitive industries such as aerospace, maritime and automotive due to strength-to-weight ratio and high stiffness of CNTRCs.

Based on potential applications of the CNTRCs, they attract a great deal of attention and become subjects of primary interest in recent studies [11–22]. Sobhani Aragh et al. [23] investigated the natural frequencies of FG-CNTRC cylindrical panels via the Eshelby–Mori–Tanaka method to compute the effective mechanical properties. Based on the three-dimensional theory of elasticity, frequencies of FG-CNTRC cylindrical panels were studied, and the governing equations were examined by a generalized differential quadrature method [24]. Moradi-Dastjerdi et al. [25] investigated the effects of orientation and aggregation of CNTs on the natural frequencies of functionally graded nanocomposite cylinders by the use of the Eshelby–Mori–Tanaka approach and mesh-free method. A postbuckling analysis of SWCNT-reinforced composite cylindrical shells subjected to combined axial and radial mechanical loads in thermal environment was given in [26]. Vibration and stress wave propagation in the FG-CNTRC cylinders under an impact load were analyzed via a meshless approach by Moradi-Dastjerdi et al. [27]. Liew et al. [28] studied the postbuckling behavior of FG-CNTRC cylindrical panels under an axial compression load based on a meshless approach. Moreover, natural frequencies of a simply supported FG-CNTRC cylindrical panel embedded in piezoelectric layers were examined by the use of the three-dimensional theory of elasticity [29]. To evaluate the effects of centrifugal and Coriolis forces on the natural frequencies of rotating FG-CNTRC truncated conical shells, the equation of motion were derived by the use of first-order shear deformation theory and were discretized based on the differential quadrature method [30]. Zhang et al. [31] analyzed the large deflection geometrically nonlinear behavior of FG-CNTRC cylindrical panels subject to uniform point transverse mechanical loading via the meshless kp-Ritz method. Mehrabadi and Aragh [32] analyzed stress variations stemming from bending of FG-CNTRC open cylindrical shells. The material properties were estimated based on the Eshelby–Mori–Tanaka approach, and a comparison between 3-D elasticity and third-order shear deformation theory was given. Flexural strength and free vibration of FG-CNTRC cylindrical panels were investigated by the use of mesh-free kp-Ritz method and the first-order shear deformation shell theory by Zhang et al. [33]. In another study, they examined the dynamic stability of FG-CNTRC cylindrical panels under static and periodic axial force [34]. A postbuckling analysis of axially compressed CNTRC cylindrical panels resting on elastic foundations in thermal environments was performed in [35]. Zarouni et al. [36] studied natural frequencies of clamped fiber-reinforced composite conical shells resting on an elastic foundation. Ghorbanpour Arani et al. [37] analyzed the static stress of a CNTRC cylinder subject to non-axisymmetric thermo-mechanical loads and uniform electro-magnetic fields via Mori–Tanaka theory. The linear buckling behavior of FG-CNTRC conical shells under lateral pressure was studied using the first-order shear deformation shell theory, and the governing equations were discretized via trigonometric functions in circumferential direction and generalized differential quadrature method in axial direction [38]. Lei et al. [39] presented a frequency analysis of FG-CNTRC rotating cylindrical panels using the mesh-free kp-Ritz method. Recently, Zhang et al. [40] investigated natural frequencies of FG-CNTRC moderately thick rectangular plates with edges elastically restrained against transverse displacements and rotation of the plate cross section. Furthermore, Kundalwal and Meguid [41] examined the influence of CNT's waviness on active damping of nanotailored hybrid composites shells. Zhang et al. [42] studied frequencies of moderately thick functionally graded CNTRC plates resting on elastic foundations by the use of the element-free IMLS-Ritz method. Using the first-order shear deformation theory and the extended rule of mixture, governing equations of laminated FG-CNTRC plates were derived, and natural frequencies of a laminated nanocomposite were analyzed [43]. The vibrational characteristics of FG-CNTRC plates subjected to in-plane loads were studied by Zhang et al. [44]. The governing equations were derived utilizing Reddy's third-order shear deformation theory, and by applying the state-space Levy method the frequencies of the nanocomposite plate were determined. Furthermore, settling time and absolute amplitude corresponding to first resonant frequency of FG-CNTRC shells were investigated by Thomas and Roy [45]. Zhang et al. [46] investigated aerothermoelastic FG-CNTRC panels in supersonic airflow, and via the piezoelectric actuator and sensor active flutter control was examined. Furthermore, using the velocity feedback control method, the vibration of CNTRC thick plates was controlled [47]. The postbuckling of FG-CNTRC plates under axial loads was analyzed by Zhang et al. [48]. The edges of the nanocomposite plate are assumed to be elastically restrained against translation and rotation. Lei et al. [49] studied the bending responses of laminated FG-CNTRC composite plates using the element-free kp-Ritz method. By the use of piezoelectric patches and applying a genetic algorithm, optimal shape control of carbon nanotube-reinforced functionally graded composite plates was investigated [50].

Despite the extensive research in the area of the mechanical behavior of the CNTRC shells, there has been no attempt to tackle the problem described in the present paper. This paper provides a first attempt to

Frequency analysis of doubly curved panels

study the natural frequencies of moderately thick doubly curved FG-CNTRC panels, especially for spherical and hyperbolic paraboloid nanocomposite panels. In this study, five kinds of distributions of CNTs in the CNTRC panels are analyzed. To estimate the mechanical properties of the resulting nanocomposite, the rule of mixture is employed. Using the first-order shear deformation theory, equations of motion are derived, and hence, five complex and coupled equations with respect to displacements are derived. In order to solve the coupled equations of motion simultaneously, Galerkin's method is applied. The accuracy of the current results is confirmed by comparing the current results with those found in the literature. The influences of volume fraction of CNTs, thickness ratio $(h/a)$, aspect ratio $(a/b)$, curvature ratio $(R_x/R_y)$, and shallowness ratio $(a/R_x)$ are also elucidated. Additionally, the influence of edge boundary conditions on the natural frequencies of doubly curved CNTRC panels is examined, and the corresponding mode shapes of movable simply supported panels are depicted. Furthermore, the impact of FG distributions of CNTs along the thickness direction on the natural frequencies of CNTRC panels is analyzed.

## 2 Material properties of FG-CNTRC panels

To predict the material properties of nanocomposites reinforced by CNTs, several micromechanical models are proposed such as Eshelby–Mori–Tanaka scheme [23,51] and the extended rule of mixture [52,53]. As a result of simplicity, the rule of mixture is utilized extensively to estimate the overall material properties of CNTRCs. Researches demonstrate that ideal and flawless load transfer between the nanotube and polymer matrix does not occur [6,51], and the conventional rule of mixture method should be modified. Therefore, to consider the small-scale effect, CNT effectiveness parameters, $\eta_i$ ($i=1,2$ and 3) are defined. By comparing the elastic modulus of the FG-CNTRCs estimated by the MD simulations with those predicted by the extended rule of mixture, the value of the CNT effectiveness parameters can be computed. The effective properties of the FG-CNTRCs can be computed via the extended rule of mixture according to [28]

$$
\begin{align}
E_{11} &= \eta_1 V_{\text{CNT}} E_{11}^{\text{CNT}} + V_{\text{m}} E^{\text{m}}, \\
E_{22} &= \frac{\eta_2}{\left( \frac{V_{\text{CNT}}}{E_{22}^{\text{CNT}}} + \frac{V_{\text{m}}}{E^{\text{m}}} \right)}, \\
G_{12} &= \frac{\eta_3}{\left( \frac{V_{\text{CNT}}}{G_{12}^{\text{CNT}}} + \frac{V_{\text{m}}}{G^{\text{m}}} \right)}
\end{align} \tag{1}
$$

where $E_{11}$, $E_{22}$ and $G_{12}$ are the corresponding properties of the FG-CNTRCs. Moreover, $E_{11}^{\text{CNT}}$, $E_{22}^{\text{CNT}}$ and $G_{12}^{\text{CNT}}$ indicate Young's moduli of the CNTs in directions 1 and 2 and shear modulus, respectively. In addition, Young's modulus and shear modulus of the isotropic polymer matrix are expressed as $E^{\text{m}}$ and $G^{\text{m}}$. Furthermore, $V_{\text{CNT}}$ and $V_{\text{m}}$ are the volume fractions of the CNTs and matrix, respectively, and are defined as

$$
V_{\text{CNT}} + V_{\text{m}} = 1. \tag{2}
$$

Likewise, mass density and Poisson's ratio of the FG-CNTRC panels can be expressed as follows:

$$
\begin{align}
\rho &= V_{\text{CNT}} \rho^{\text{CNT}} + V_{\text{m}} \rho^{\text{m}}, \tag{3} \\
\nu_{12} &= V_{\text{CNT}}^* \nu_{12}^{\text{CNT}} + (1 - V_{\text{CNT}}^*) \nu^{\text{m}} \tag{4}
\end{align}
$$

where $\rho^{\text{CNT}}$ and $\rho^{\text{m}}$ indicate the densities of CNTs and matrix, and $\nu_{12}^{\text{CNT}}$ and $\nu^{\text{m}}$ are Poisson's ratios of the CNTs and polymer matrix, respectively. Moreover, $V_{\text{CNT}}^*$ is defined as [28]

$$
V_{\text{CNT}}^* = \frac{w_{\text{CNT}}}{w_{\text{CNT}} + (\rho^{\text{CNT}} / \rho^{\text{m}})(1 - w_{\text{CNT}})} \tag{5}
$$

wherein $w_{\text{CNT}}$ is the mass fraction of the CNTs.

Consider a doubly curved FG-CNTRC shell panel in the orthogonal curvilinear coordinate system $(x,y,z)$ of curvilinear length $a$ in the $x$ direction, curvilinear width $b$ in the $y$ direction, thickness $h$ in the $z$ direction, and principal radii of curvature $R_x$ and $R_y$, as shown in Fig. 1. Here, special kinds of the doubly curved shell panels are investigated such as cylindrical shell ($R_x=R$ and $R_y=\infty$), spherical shell ($R_x=R_y$), and hyperbolic

![](./images/814519641912115201_1.jpg)

Fig. 1 Geometrical dimensions of doubly curved panels

paraboloid shell $(R_x = -R_y)$, and the analysis will be limited to the case when $R_x$ and $R_y$ are constants. As mentioned before, the CNTs in CNTRCs can be distributed uniformly or functionally graded along the thickness direction. Uniformly distributed CNTs in a nanocomposite is a homogeneous kind of CNTRC and well known as UD. In addition, four cases of functionally graded distributions of CNTs in nanocomposite panels are taken into consideration, named as FG-A, FG-V, FG-O and FG-X, as shown in Fig. 2. To analyze a realistic and applied FG-CNTRC shell panel, it is assumed that the volume fractions of CNTs alter linearly. For these five kinds of CNTRC shell panels, the overall mass fractions of the CNTs in CNTRC are identical, and the CNT volume fractions are defined as follows [34]:

$$
	\text{UD}:\ V_{\text{CNT}}(z)=V_{\text{CNT}}^{*},\tag{6.1}
$$

$$
	\text{FG-A}:\ V_{\text{CNT}}(z)=\left(1-\frac{2z}{h}\right)V_{\text{CNT}}^{*},\tag{6.2}
$$

$$
	\text{FG-V}:\ V_{\text{CNT}}(z)=\left(1+\frac{2z}{h}\right)V_{\text{CNT}}^{*},\tag{6.3}
$$

$$
	\text{FG-O}:\ V_{\text{CNT}}(z)=2\left(1-\frac{2|z|}{h}\right)V_{\text{CNT}}^{*},\tag{6.4}
$$

$$
	\text{FG-X}:\ V_{\text{CNT}}(z)=\frac{4|z|}{h}V_{\text{CNT}}^{*}.\tag{6.5}
$$

### 2.1 Governing equations

In the current investigation, doubly curved FG-CNTRC shell panels are assumed as moderately thick panels and modeled by the first-order shear deformation theory. Based on the first-order shear deformation theory, the displacement of an arbitrary point can be expressed as [54–56]

$$
	u_x=\left(1+\frac{z}{R_x}\right)u\left(x,y,t\right)+z\phi_x,\quad u_y=\left(1+\frac{z}{R_y}\right)v\left(x,y,t\right)+z\phi_y,\quad u_z=w\left(x,y,t\right)\tag{7}
$$

where $u$, $v$, and $w$ indicate displacements of the mid-surface along $x$, $y$, and $z$ directions, respectively. Moreover, $\varphi_x$ and $\varphi_y$ are rotations of the normal to the mid-surface about the $y$ and $x$ axes, respectively. Here, the strain-displacement relations are assumed in linear forms as [54–56]

$$
\begin{aligned}
	\varepsilon_x&=\frac{\partial u}{\partial x}+\frac{w}{R_x}+z\frac{\partial \phi_x}{\partial x},\quad \varepsilon_y=\frac{\partial v}{\partial y}+\frac{w}{R_y}+z\frac{\partial \phi_y}{\partial y},\\
	\gamma_{xz}&=\phi_x+\frac{\partial w}{\partial x}-\frac{u}{R_x},\quad \gamma_{yz}=\phi_y+\frac{\partial w}{\partial y}-\frac{v}{R_y},\\
	\gamma_{xy}&=\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}+z\left[\frac{\partial \phi_x}{\partial y}+\frac{\partial \phi_y}{\partial x}+S\left(\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\right)\right]
\end{aligned}\tag{8}
$$

Frequency analysis of doubly curved panels

![](./images/814519641912115201_2.jpg)

Fig. 2 Configurations of the FG-CNTRC panels a UD; b FG-V; c FG-A; d FG-X; e FG-O

where $S$ is defined as $\frac{1}{2}\left(\frac{1}{R_y}-\frac{1}{R_x}\right)$. Applying Hamilton's principle, one can obtain the governing equations of equilibrium as follows:

$$
\frac{\partial N_{x x}}{\partial x}+\frac{\partial N_{x y}}{\partial y}+\frac{Q_{x z}}{R_x}-S \frac{\partial M_{x y}}{\partial y}=I_0 \frac{\partial^2 u}{\partial t^2}+I_1\left(\frac{2}{R_x} \frac{\partial^2 u}{\partial t^2}+\frac{\partial^2 \phi_x}{\partial t^2}\right)+I_2\left(\frac{1}{R_x^2} \frac{\partial^2 u}{\partial t^2}+\frac{1}{R_x} \frac{\partial^2 \phi_x}{\partial t^2}\right),(9.1)
$$

$$
\frac{\partial N_{y y}}{\partial y}+\frac{\partial N_{x y}}{\partial x}+\frac{Q_{y z}}{R_y}+S \frac{\partial M_{x y}}{\partial x}=I_0 \frac{\partial^2 v}{\partial t^2}+I_1\left(\frac{2}{R_y} \frac{\partial^2 v}{\partial t^2}+\frac{\partial^2 \phi_y}{\partial t^2}\right)+I_2\left(\frac{1}{R_y^2} \frac{\partial^2 v}{\partial t^2}+\frac{1}{R_y} \frac{\partial^2 \phi_y}{\partial t^2}\right),(9.2)
$$

$$
\frac{N_{x x}}{R_x}+\frac{N_{y y}}{R_y}-\frac{\partial Q_{x z}}{\partial x}-\frac{\partial Q_{y z}}{\partial y}=q-I_0 \frac{\partial^2 w}{\partial t^2}, \tag{9.3}
$$

$$
\frac{\partial M_{x x}}{\partial x}+\frac{\partial M_{x y}}{\partial y}-Q_{x z}=I_1 \frac{\partial^2 u}{\partial t^2}+I_2\left(\frac{1}{R_x} \frac{\partial^2 u}{\partial t^2}+\frac{\partial^2 \phi_x}{\partial t^2}\right), \tag{9.4}
$$

$$
\frac{\partial M_{y y}}{\partial y}+\frac{\partial M_{x y}}{\partial x}-Q_{y z}=I_1 \frac{\partial^2 v}{\partial t^2}+I_2\left(\frac{1}{R_y} \frac{\partial^2 v}{\partial t^2}+\frac{\partial^2 \phi_y}{\partial t^2}\right) \tag{9.5}
$$

where $q$ is the distributed transverse load on the FG-CNTRC panel. Also, $I_0$, $I_1$ and $I_2$ denote the normal, coupled normal-rotary and rotary mass moments of inertia, respectively, and are defined as

$$
\left\{I_0\ I_1\ I_2\right\}=\int_{-h / 2}^{h / 2} \rho\left\{1\ z\ z^2\right\} \mathrm{d} z. \tag{10}
$$

In addition, $N_{x x}$, $N_{y y}$ and $N_{x y}$ are in-plane stress resultants, and $M_{x x}$, $M_{y y}$ and $M_{x y}$ are stress couple resultants. Moreover, $Q_{x z}$ and $Q_{y z}$ denote transverse shear stress resultants. By neglecting $z / R_x$ and $z / R_y$ in comparison with unity, the stress resultants can be defined as

$$
\left\{N_{x x}, N_{y y}, N_{x y}, M_{x x}, M_{y y}, M_{x y}\right\}=\int_{-\frac{h}{2}}^{\frac{h}{2}}\left\{\sigma_{x x}, \sigma_{y y}, \sigma_{x y}, \sigma_{x x} z, \sigma_{y y} z, \sigma_{x y} z\right\} \mathrm{d} z,
$$

$$
\left\{Q_{x z}, Q_{y z}\right\}=K_{s} \int_{-\frac{h}{2}}^{\frac{h}{2}}\left\{\tau_{x z}, \tau_{y z}\right\} \mathrm{d} z, \tag{11}
$$

wherein $K_s$ is the shear correction factor. Based on the first-order shear deformation theory, shear strains are distributed uniformly along the thickness direction which leads to uniform and overestimated shear stresses in comparison with the actual distribution of shear stresses. To precise the estimated transverse shear stress resultants, a shear correction factor $K_s$ is applied as 5/6 [56]. As a result of the orthotropic characteristics of the CNTs, Hooke's law for the stress-strain relations of FG-CNTRC is defined as

$$
\left(\begin{array}{c}
\sigma_{x x} \\
\sigma_{y y} \\
\tau_{y z} \\
\tau_{x z} \\
\tau_{x y}
\end{array}\right)=\left[\begin{array}{ccccc}
\frac{E_{11}}{1-v_{12} v_{21}} & \frac{v_{12} E_{22}}{1-v_{12} v_{21}} & 0 & 0 & 0 \\
\frac{v_{12} E_{22}}{1-v_{12} v_{21}} & \frac{E_{22}}{1-v_{12} v_{21}} & 0 & 0 & 0 \\
0 & 0 & G_{23} & 0 & 0 \\
0 & 0 & 0 & G_{13} & 0 \\
0 & 0 & 0 & 0 & G_{12}
\end{array}\right]\left(\begin{array}{c}
\varepsilon_{x x} \\
\varepsilon_{y y} \\
\gamma_{y z} \\
\gamma_{x z} \\
\gamma_{x y}
\end{array}\right). \tag{12}
$$

By applying displacement definitions [Eq. (7)], strain-displacement relationships [Eq. (8)], Hooke's law [Eq. (12)], and stress resultants definition [Eq. (11)], the governing differential equations in terms of the mid-surface displacements and rotations can be obtained as

$$
\begin{aligned}
& A_{1} \frac{\partial^{2} u}{\partial x^{2}}+\left(C_{1}-2 S C_{2}+S^{2}\right) \frac{\partial^{2} u}{\partial y^{2}}+\left(v_{12} B_{1}+C_{1}-S^{2}\right) \frac{\partial^{2} v}{\partial x \partial y}+A_{2} \frac{\partial^{2} \phi_{x}}{\partial x^{2}}+\left(C_{2}-C_{3} S\right) \frac{\partial^{2} \phi_{x}}{\partial y^{2}} \\
& +\left(v_{12} B_{2}+C_{2}-C_{3} S\right) \frac{\partial^{2} \phi_{y}}{\partial x \partial y}+\left(\frac{A_{1}}{R_{x}}+\frac{v_{12} B_{1}}{R_{y}}+\frac{K_{s} F_{1}}{R_{x}}\right) \frac{\partial w}{\partial x}+\frac{K_{s} F_{1}}{R_{x}}\left(\phi_{x}-\frac{u}{R_{x}}\right)=I_{0} \frac{\partial^{2} u}{\partial t^{2}} \\
& +I_{1}\left(\frac{2}{R_{x}} \frac{\partial^{2} u}{\partial t^{2}}+\frac{\partial^{2} \phi_{x}}{\partial t^{2}}\right)+I_{2}\left(\frac{1}{R_{x}^{2}} \frac{\partial^{2} u}{\partial t^{2}}+\frac{1}{R_{x}} \frac{\partial^{2} \phi_{x}}{\partial t^{2}}\right),
\end{aligned} \tag{13.1}
$$

$$
\begin{aligned}
& B_{1} \frac{\partial^{2} v}{\partial y^{2}}+\left(C_{1}+2 S C_{2}+S^{2}\right) \frac{\partial^{2} v}{\partial x^{2}}+\left(v_{12} B_{1}+C_{1}-S^{2}\right) \frac{\partial^{2} u}{\partial x \partial y}+B_{2} \frac{\partial^{2} \phi_{y}}{\partial y^{2}}+\left(C_{2}+C_{3} S\right) \frac{\partial^{2} \phi_{y}}{\partial x^{2}} \\
& +\left(v_{12} B_{2}+C_{2}+C_{3} S\right) \frac{\partial^{2} \phi_{x}}{\partial x \partial y}+\left(\frac{B_{1}}{R_{y}}+\frac{v_{12} B_{1}}{R_{x}}+\frac{K_{s} D_{1}}{R_{y}}\right) \frac{\partial w}{\partial y}+\frac{K_{s} D_{1}}{R_{y}}\left(\phi_{y}-\frac{v}{R_{y}}\right)=I_{0} \frac{\partial^{2} v}{\partial t^{2}} \\
& +I_{1}\left(\frac{2}{R_{y}} \frac{\partial^{2} v}{\partial t^{2}}+\frac{\partial^{2} \phi_{y}}{\partial t^{2}}\right)+I_{2}\left(\frac{1}{R_{y}^{2}} \frac{\partial^{2} v}{\partial t^{2}}+\frac{1}{R_{y}} \frac{\partial^{2} \phi_{y}}{\partial t^{2}}\right),
\end{aligned} \tag{13.2}
$$

$$
\begin{aligned}
& \left(\frac{A_{1}}{R_{x}}+\frac{v_{12} B_{1}}{R_{y}}+\frac{K_{s} F_{1}}{R_{x}}\right) \frac{\partial u}{\partial x}+\left(\frac{B_{1}}{R_{y}}+\frac{v_{12} B_{1}}{R_{x}}+\frac{K_{s} D_{1}}{R_{y}}\right) \frac{\partial v}{\partial y}+\left(\frac{A_{2}}{R_{x}}+\frac{v_{12} B_{2}}{R_{y}}-K_{s} F_{1}\right) \frac{\partial \phi_{x}}{\partial x} \\
& +\left(\frac{B_{2}}{R_{y}}+\frac{v_{12} B_{2}}{R_{x}}-K_{s} D_{1}\right) \frac{\partial \phi_{y}}{\partial y}+\left(\frac{A_{1}}{R_{x}^{2}}+\frac{B_{1}}{R_{y}^{2}}+\frac{2 v_{12} B_{1}}{R_{x} R_{y}}\right) w-K_{s} F_{1} \frac{\partial^{2} w}{\partial x^{2}}-K_{s} D_{1} \frac{\partial^{2} w}{\partial y^{2}}=q-I_{0} \frac{\partial^{2} w}{\partial t^{2}},
\end{aligned} \tag{13.3}
$$

$$
\begin{aligned}
& A_{2} \frac{\partial^{2} u}{\partial x^{2}}+\left(C_{2}-S\right) \frac{\partial^{2} u}{\partial y^{2}}+\left(v_{12} B_{2}+C_{2}+S\right) \frac{\partial^{2} v}{\partial x \partial y}+A_{3} \frac{\partial^{2} \phi_{x}}{\partial x^{2}}+C_{3} \frac{\partial^{2} \phi_{x}}{\partial y^{2}}+\left(v_{12} B_{3}+C_{3}\right) \frac{\partial^{2} \phi_{y}}{\partial x \partial y} \\
& +\left(\frac{A_{2}}{R_{x}}+\frac{v_{12} B_{2}}{R_{y}}-K_{s} F_{1}\right) \frac{\partial w}{\partial x}-K_{s} F_{1}\left(\phi_{x}-\frac{u}{R_{x}}\right)=I_{1} \frac{\partial^{2} u}{\partial t^{2}}+I_{2}\left(\frac{1}{R_{x}} \frac{\partial^{2} u}{\partial t^{2}}+\frac{\partial^{2} \phi_{x}}{\partial t^{2}}\right),
\end{aligned} \tag{13.4}
$$
```

Frequency analysis of doubly curved panels

![](./images/814519641912115201_3.jpg)

Fig. 3 Convergence study of the non-dimensional frequency of CSCS and CCCC nanocomposite panels

Table 1 Validation of the non-dimensional frequencies of thick $Al/Al_2O_3$ functionally graded shells

<table>
<thead>
<tr>
<th>$b/R_y$</th>
<th>$a/R_x$</th>
<th>$k$</th>
<th colspan="2">Ref. [59]</th>
<th>Ref. [60]</th>
<th>Ref. [61]</th>
<th>Present study</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$1+z/R\neq1$</th>
<th>$1+z/R=1$</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5</td>
<td>0.5</td>
<td>0</td>
<td>0.0746</td>
<td>0.0753</td>
<td>0.0751</td>
<td>0.0762</td>
<td>0.0746</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.5</td>
<td>0.0647</td>
<td>0.0653</td>
<td>0.0657</td>
<td>0.0664</td>
<td>0.0646</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>0.0589</td>
<td>0.0595</td>
<td>0.0601</td>
<td>0.0607</td>
<td>0.0588</td>
</tr>
<tr>
<td></td>
<td></td>
<td>10</td>
<td>0.0455</td>
<td>0.0459</td>
<td>0.0464</td>
<td>0.0471</td>
<td>0.0455</td>
</tr>
<tr>
<td>0</td>
<td>0.5</td>
<td>0</td>
<td>0.0615</td>
<td>0.0622</td>
<td>0.0622</td>
<td>0.0629</td>
<td>0.0616</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.5</td>
<td>0.0527</td>
<td>0.0532</td>
<td>0.0535</td>
<td>0.0540</td>
<td>0.0527</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>0.0476</td>
<td>0.0482</td>
<td>0.0485</td>
<td>0.0490</td>
<td>0.0477</td>
</tr>
<tr>
<td></td>
<td></td>
<td>10</td>
<td>0.0383</td>
<td>0.0387</td>
<td>0.0390</td>
<td>0.0395</td>
<td>0.0384</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>0.0578</td>
<td>0.0577</td>
<td>0.0577</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.5</td>
<td>–</td>
<td>–</td>
<td>0.0492</td>
<td>0.0490</td>
<td>0.0490</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>–</td>
<td>–</td>
<td>0.0443</td>
<td>0.0442</td>
<td>0.0442</td>
</tr>
<tr>
<td></td>
<td></td>
<td>10</td>
<td>–</td>
<td>–</td>
<td>0.0364</td>
<td>0.0366</td>
<td>0.0366</td>
</tr>
</tbody>
</table>

$$
\begin{aligned}
& B_{2} \frac{\partial^{2} v}{\partial y^{2}}+\left(C_{2}+S\right) \frac{\partial^{2} v}{\partial x^{2}}+\left(v_{12} B_{2}+C_{2}-S\right) \frac{\partial^{2} u}{\partial x \partial y}+C_{3} \frac{\partial^{2} \phi_{y}}{\partial x^{2}}+B_{3} \frac{\partial^{2} \phi_{y}}{\partial y^{2}}+\left(v_{12} B_{3}+C_{3}\right) \frac{\partial^{2} \phi_{x}}{\partial x \partial y} \\
& \quad+\left(\frac{v_{12} B_{2}}{R_{x}}+\frac{B_{2}}{R_{y}}-K_{s} D_{1}\right) \frac{\partial w}{\partial y}-K_{s} D_{1}\left(\phi_{y}-\frac{v}{R_{y}}\right)=I_{1} \frac{\partial^{2} v}{\partial t^{2}}+I_{2}\left(\frac{1}{R_{y}} \frac{\partial^{2} v}{\partial t^{2}}+\frac{\partial^{2} \phi_{y}}{\partial t^{2}}\right).
\end{aligned}\tag{13.5}
$$

where $A_{i}, B_{i}, C_{i}, D_{1}$ and $F_{1}$ and $(i=1,2,3)$ are defined by

$$
\begin{aligned}
& \left\{A_{1} A_{2} A_{3}\right\}=\int_{-h / 2}^{h / 2}\left(\frac{E_{11}}{\left(1-v_{12} v_{21}\right)}\right)\left\{1 z z^{2}\right\} \mathrm{d} z \quad\left\{C_{1} C_{2} C_{3}\right\}=\int_{-h / 2}^{h / 2} G_{12}\left\{1 z z^{2}\right\} \mathrm{d} z, \\
& \left\{B_{1} B_{2} B_{3}\right\}=\int_{-h / 2}^{h / 2}\left(\frac{E_{22}}{\left(1-v_{12} v_{21}\right)}\right)\left\{1 z z^{2}\right\} \mathrm{d} z \quad\left\{D_{1} F_{1}\right\}=\int_{-h / 2}^{h / 2}\left\{G_{23} G_{13}\right\} \mathrm{d} z.
\end{aligned}\tag{14}
$$

### 2.2 Solution procedure

Up to now, the analysis has been general without reference to the boundary conditions. Here, FG-CNTRC shell panels with different combinations of boundary conditions is assumed. For the sake of brevity, the movable simply supported, immovable simply supported, and clamped boundary conditions of the FG-CNTRC panels are represented by $S, S^{*}$ and $C$, respectively. For combinations of edge boundary conditions, a counterclockwise notation initiating from $x=0$ is presented. Subsequently, the SCSC panel stands for the nanocomposite panel

Table 2 Comparison of the non-dimensional frequencies of isotropic panels with various boundary conditions

<table>
<thead>
<tr>
<th>Boundary conditions</th>
<th>$b_s/R_y$</th>
<th>$R_y/R_x$</th>
<th></th>
<th colspan="5">Modes</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
</tr>
</thead>
<tbody>
<tr>
<td>$S^*S^*S^*S^*$</td>
<td>0.3</td>
<td>0</td>
<td>Ref. [62]</td>
<td>66.57</td>
<td>85.62</td>
<td>103.77</td>
<td>104.95</td>
<td>113.70</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>66.54</td>
<td>85.51</td>
<td>103.70</td>
<td>104.81</td>
<td>113.54</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>Ref. [62]</td>
<td>121.99</td>
<td>121.99</td>
<td>130.15</td>
<td>139.21</td>
<td>144.52</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>121.95</td>
<td>121.95</td>
<td>130.01</td>
<td>139.07</td>
<td>144.30</td>
</tr>
<tr>
<td></td>
<td>0.5</td>
<td>0</td>
<td>Ref. [62]</td>
<td>88.43</td>
<td>99.89</td>
<td>137.82</td>
<td>140.07</td>
<td>166.64</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>88.57</td>
<td>99.55</td>
<td>137.64</td>
<td>139.71</td>
<td>166.54</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>Ref. [62]</td>
<td>188.59</td>
<td>188.99</td>
<td>188.99</td>
<td>201.27</td>
<td>204.38</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>188.35</td>
<td>189.01</td>
<td>189.01</td>
<td>200.98</td>
<td>204.19</td>
</tr>
<tr>
<td>$CS^*CS^*$</td>
<td>0.3</td>
<td>0</td>
<td>Ref. [62]</td>
<td>71.21</td>
<td>88.75</td>
<td>114.87</td>
<td>116.23</td>
<td>117.56</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>71.38</td>
<td>88.77</td>
<td>115.31</td>
<td>116.20</td>
<td>118.07</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>Ref. [62]</td>
<td>122.81</td>
<td>129.21</td>
<td>132.09</td>
<td>146.24</td>
<td>152.92</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>122.79</td>
<td>129.43</td>
<td>132.03</td>
<td>146.43</td>
<td>152.98</td>
</tr>
<tr>
<td></td>
<td>0.5</td>
<td>0</td>
<td>Ref. [62]</td>
<td>92.50</td>
<td>103.57</td>
<td>148.24</td>
<td>150.83</td>
<td>167.69</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>92.84</td>
<td>103.43</td>
<td>148.64</td>
<td>151.11</td>
<td>167.63</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>Ref. [62]</td>
<td>189.01</td>
<td>191.49</td>
<td>191.93</td>
<td>206.97</td>
<td>209.94</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>189.03</td>
<td>191.34</td>
<td>191.88</td>
<td>206.86</td>
<td>210.11</td>
</tr>
<tr>
<td>CCCC</td>
<td>0.3</td>
<td>0</td>
<td>Ref. [62]</td>
<td>83.92</td>
<td>90.40</td>
<td>115.05</td>
<td>125.87</td>
<td>140.53</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>84.54</td>
<td>90.48</td>
<td>115.50</td>
<td>126.73</td>
<td>141.57</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>Ref. [62]</td>
<td>130.16</td>
<td>130.16</td>
<td>134.01</td>
<td>153.35</td>
<td>167.20</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>130.43</td>
<td>130.43</td>
<td>134.03</td>
<td>153.90</td>
<td>168.05</td>
</tr>
<tr>
<td></td>
<td>0.5</td>
<td>0</td>
<td>Ref. [62]</td>
<td>99.26</td>
<td>119.00</td>
<td>151.13</td>
<td>156.35</td>
<td>172.52</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>99.55</td>
<td>119.54</td>
<td>151.59</td>
<td>156.82</td>
<td>172.66</td>
</tr>
<tr>
<td></td>
<td></td>
<td>1</td>
<td>Ref. [62]</td>
<td>191.99</td>
<td>191.99</td>
<td>196.93</td>
<td>209.96</td>
<td>216.19</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Present study</td>
<td>191.95</td>
<td>191.95</td>
<td>197.12</td>
<td>209.99</td>
<td>216.60</td>
</tr>
</tbody>
</table>

![](./images/814519641912115201_4.jpg)

Fig. 4 Change of the non-dimensional frequency with respect to the aspect ratio for various boundary conditions ($V_{\text{CNT}}^* = 0.11$, $a/h = 20$ and $a/R_x = 0.5$)

with the edges movable simply supported, clamped, movable simply supported and clamped at $x=0$, $y=0$, $x=a$ and $y=b$, respectively. Mathematical implementation of various boundary conditions at $x=0$ and $x=a$ is expressed as follows.

For movable simply supported edge:

$$
\begin{aligned}
N_{xx}\left(0,y,t\right) &= N_{xx}\left(a,y,t\right)=0, & v\left(0,y,t\right) &= v\left(a,y,t\right)=0 \\
M_{xx}\left(0,y,t\right) &= M_{xx}\left(a,y,t\right)=0, & \phi_{y}\left(0,y,t\right) &= \phi_{y}\left(a,y,t\right)=0 \\
w\left(0,y,t\right) &= w\left(a,y,t\right)=0.
\end{aligned} \tag{15}
$$

Frequency analysis of doubly curved panels

Table 3 Variation of the non-dimensional frequency of a movable simply supported plate and doubly curved panels

<table>
<thead>
<tr>
<th>$a/R_x$</th>
<th>$b/R_y$</th>
<th>$V_{\text{CNT}}^*$</th>
<th colspan="5">Non-dimensional frequency</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>UD</th>
<th>FG-A</th>
<th>FG-V</th>
<th>FG-X</th>
<th>FG-O</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5</td>
<td>0.5</td>
<td>0.11</td>
<td>20.2381</td>
<td>18.2514</td>
<td>18.5425</td>
<td>22.4320</td>
<td>17.1397</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>21.6551</td>
<td>19.5458</td>
<td>19.7789</td>
<td>23.9965</td>
<td>18.2670</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>25.0512</td>
<td>22.6250</td>
<td>22.9514</td>
<td>27.8827</td>
<td>21.2115</td>
</tr>
<tr>
<td>0.5</td>
<td>−0.5</td>
<td>0.11</td>
<td>17.1058</td>
<td>15.0240</td>
<td>14.8094</td>
<td>19.5876</td>
<td>13.3643</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>18.6256</td>
<td>16.4007</td>
<td>16.1809</td>
<td>21.2249</td>
<td>14.6095</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>21.0947</td>
<td>18.4751</td>
<td>18.2249</td>
<td>24.2735</td>
<td>16.3892</td>
</tr>
<tr>
<td>0.5</td>
<td>0</td>
<td>0.11</td>
<td>18.1263</td>
<td>15.9890</td>
<td>16.0598</td>
<td>20.5479</td>
<td>14.5525</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>19.6278</td>
<td>17.3575</td>
<td>17.3905</td>
<td>22.1792</td>
<td>15.7660</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>22.3797</td>
<td>19.7184</td>
<td>19.7991</td>
<td>25.4877</td>
<td>17.9030</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0.11</td>
<td>18.0075</td>
<td>15.7011</td>
<td>15.7011</td>
<td>20.6235</td>
<td>14.0683</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>19.6082</td>
<td>17.1474</td>
<td>17.1474</td>
<td>22.3489</td>
<td>15.3782</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>22.2068</td>
<td>19.3150</td>
<td>19.3150</td>
<td>25.5574</td>
<td>17.2523</td>
</tr>
</tbody>
</table>

Table 4 Change of the non-dimensional frequency of a CCCC plate and doubly curved panels

<table>
<thead>
<tr>
<th>$a/R_x$</th>
<th>$b/R_y$</th>
<th>$V_{\text{CNT}}^*$</th>
<th colspan="5">Non-dimensional frequency</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>UD</th>
<th>FG-A</th>
<th>FG-V</th>
<th>FG-X</th>
<th>FG-O</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5</td>
<td>0.5</td>
<td>0.11</td>
<td>59.9319</td>
<td>57.4229</td>
<td>56.9472</td>
<td>62.5277</td>
<td>54.6717</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>62.2918</td>
<td>60.0434</td>
<td>59.5914</td>
<td>64.8258</td>
<td>57.4414</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>74.6296</td>
<td>71.5722</td>
<td>70.9702</td>
<td>78.2783</td>
<td>67.9988</td>
</tr>
<tr>
<td>0.5</td>
<td>−0.5</td>
<td>0.11</td>
<td>59.6090</td>
<td>56.9421</td>
<td>56.7639</td>
<td>62.2114</td>
<td>54.3285</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>61.9647</td>
<td>59.5777</td>
<td>59.3858</td>
<td>64.5039</td>
<td>57.0957</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>74.2247</td>
<td>70.9719</td>
<td>70.7321</td>
<td>77.8808</td>
<td>67.5645</td>
</tr>
<tr>
<td>0.5</td>
<td>0</td>
<td>0.11</td>
<td>59.0812</td>
<td>56.4491</td>
<td>56.1259</td>
<td>61.7106</td>
<td>53.7283</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>61.4458</td>
<td>59.0868</td>
<td>58.7678</td>
<td>64.0080</td>
<td>56.5105</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>73.5657</td>
<td>70.3475</td>
<td>69.9307</td>
<td>77.2529</td>
<td>66.8066</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0.11</td>
<td>28.9498</td>
<td>26.9086</td>
<td>26.9086</td>
<td>30.8924</td>
<td>25.1242</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.14</td>
<td>30.4349</td>
<td>28.5217</td>
<td>28.5217</td>
<td>32.3018</td>
<td>26.7648</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.17</td>
<td>35.9558</td>
<td>33.3914</td>
<td>33.3914</td>
<td>38.6177</td>
<td>31.0656</td>
</tr>
</tbody>
</table>

For immovable simply supported edge:

$$
\begin{aligned}
u\left(0, y, t\right) & = u\left(a, y, t\right)=0, & v\left(0, y, t\right) & = v\left(a, y, t\right)=0, \\
M_{xx}\left(0, y, t\right) & = M_{xx}\left(a, y, t\right)=0, & \phi_y\left(0, y, t\right) & = \phi_y\left(a, y, t\right)=0, \\
w\left(0, y, t\right) & = w\left(a, y, t\right)=0. & &
\end{aligned} \tag{16}
$$

For clamped edge:

$$
\begin{aligned}
u\left(0, y, t\right) & = u\left(a, y, t\right)=0, & v\left(0, y, t\right) & = v\left(a, y, t\right)=0, \\
\phi_x\left(0, y, t\right) & = \phi_x\left(a, y, t\right)=0, & \varphi_y\left(0, y, t\right) & = \varphi_y\left(a, y, t\right)=0, \\
w\left(0, y, t\right) & = w\left(a, y, t\right)=0. & &
\end{aligned} \tag{17}
$$

For boundary conditions at $y=0$ and $y=b$, similar mathematical relations can be expressed. In order to solve the complex and highly coupled governing differential equations, Galerkin's method is employed. To apply Galerkin's method, displacements of the mid-surface and rotations of the normal to the mid-surface are discretized via sets of trigonometric expansions as follows:

$$
\begin{aligned}
u\left(x, y, t\right) & = \boldsymbol{\Phi}_u^T \mathbf{q}_u = \sum_{m=1}^{m'} \sum_{n=1}^{n'} q_{u_{mn}}\left(t\right)\varphi_{u_m}\left(x\right)\psi_{u_n}\left(y\right), \\
v\left(x, y, t\right) & = \boldsymbol{\Phi}_v^T \mathbf{q}_v = \sum_{m=1}^{m'} \sum_{n=1}^{n'} q_{v_{mn}}\left(t\right)\varphi_{v_m}\left(x\right)\psi_{v_n}\left(y\right), \\
w\left(x, y, t\right) & = \boldsymbol{\Phi}_w^T \mathbf{q}_w = \sum_{m=1}^{m'} \sum_{n=1}^{n'} q_{w_{mn}}\left(t\right)\varphi_{w_m}\left(x\right)\psi_{w_n}\left(y\right),
\end{aligned} \tag{18}
$$

![](./images/814519641912115201_5.jpg)

Fig. 5 Influence of the curvature ratio on the first seven non-dimensional frequencies of SSSS FG-X panels

![](./images/814519641912115201_6.jpg)

Fig. 6 Effect of the curvature ratio on the first eight frequencies of CCCC FG-X panels

$$
\varphi_{x}(x, y, t)=\boldsymbol{\Phi}_{x}^{T} \mathbf{q}_{x}=\sum_{m=1}^{m^{\prime}} \sum_{n=1}^{n^{\prime}} q_{x_{m n}}(t) \varphi_{x_{m}}(x) \psi_{x_{n}}(y),
$$

$$
\varphi_{y}(x, y, t)=\boldsymbol{\Phi}_{y}^{T} \mathbf{q}_{y}=\sum_{m=1}^{m^{\prime}} \sum_{n=1}^{n^{\prime}} q_{y_{m n}}(t) \varphi_{y_{m}}(x) \psi_{y_{n}}(y)
$$

where $m'$ and $n'$ are the number of modes, and $\mathbf{q}_{\mathbf{u}}, \mathbf{q}_{\mathbf{v}}, \mathbf{q}_{\mathbf{w}}, \mathbf{q}_{\mathbf{x}}$ and $\mathbf{q}_{\mathbf{y}}$ are time-dependent vectors of generalized coordinates. Furthermore, $\boldsymbol{\Phi}_{\mathbf{u}}, \boldsymbol{\Phi}_{\mathbf{v}}, \boldsymbol{\Phi}_{\mathbf{w}}, \boldsymbol{\Phi}_{\mathbf{x}}$ and $\boldsymbol{\Phi}_{\mathbf{y}}$ are shape functions. By the use of sets of trigonometric expansions, a set of ordinary differential equations is generated from partial differential governing equations [Eq. (2.1)]. Via Galerkin's method in conjunction with the state-space approach, the set of ordinary differential governing equations can be expressed as follows:

$$
\mathbf{A} \dot{\mathbf{q}}=\mathbf{B q} \tag{19}
$$

where matrix $\mathbf{A}$ indicates dynamic coupling of rotations and the mid-surface displacements. Furthermore, matrix $\mathbf{B}$ denotes static coupling of generalized coordinates. The component of the aforementioned matrices

![](./images/814519641912115201_7.jpg)

Fig. 7 Mode shapes of an SSSS FG-X spherical panel; a undeformed panel, b Mode 1, c Mode 2, d Mode 3, e Mode 4, f Mode 5

in terms of shape functions can be found in the "Appendix." In addition, $\mathbf{q}$ is the overall vector of generalized coordinates defined as

$$
\{\mathbf{q}\}=\left\{\mathbf{q}_{u 1}^{T} \mathbf{q}_{u 2}^{T} \mathbf{q}_{v 1}^{T} \mathbf{q}_{v 2}^{T} \mathbf{q}_{w 1}^{T} \mathbf{q}_{w 2}^{T} \mathbf{q}_{x 1}^{T} \mathbf{q}_{x 2}^{T} \mathbf{q}_{y 1}^{T} \mathbf{q}_{y 2}^{T}\right\}^{T} \tag{20}
$$

where

$$
\begin{aligned}
& \mathbf{q}_{u 1}=\mathbf{q}_{u}, \quad \mathbf{q}_{v 1}=\mathbf{q}_{v}, \quad \mathbf{q}_{w 1}=\mathbf{q}_{w}, \quad \mathbf{q}_{x 1}=\mathbf{q}_{x}, \quad \mathbf{q}_{y 1}=\mathbf{q}_{y}, \\
& \mathbf{q}_{u 2}=\dot{\mathbf{q}}_{u 1}, \quad \mathbf{q}_{v 2}=\dot{\mathbf{q}}_{v 1}, \quad \mathbf{q}_{w 2}=\dot{\mathbf{q}}_{w 1}, \quad \mathbf{q}_{x 2}=\dot{\mathbf{q}}_{x 1}, \quad \mathbf{q}_{y 2}=\dot{\mathbf{q}}_{y 1}.
\end{aligned} \tag{21}
$$

Notice that Eq. (17) is reduced to the classical eigenvalue problem, and the overall vector of generalized coordinates can be written in the following form:

$$
\mathbf{q}=\overline{\mathbf{q}} \exp (i \omega t) \tag{22}
$$

![](./images/814519641912115201_8.jpg)

Fig. 8 Variation of the non-dimensional frequency and PCF with respect to the curvature ratio for various kinds of SSSS CNTRC;
a non-dimensional frequency, b percentage change of frequency

where $\omega$ and $\overline{\mathbf{q}}$ are the natural frequency of CNTRC panels and the corresponding eigenvector of the problem, respectively. In order to investigate the vibrational characteristics of doubly curved FG-CNTRC panels, a non-dimensional frequency is defined as

$$
\Omega=\omega\left(\frac{a^{2}}{h}\right) \sqrt{\frac{\rho^{m}}{E^{m}}}. \tag{23}
$$

Additionally, to evaluate the impact of functionally graded distributions along the thickness direction on the natural frequencies, comparison studies are done, and the percentage change of frequency (PCF) is defined as follows:

$$
\mathrm{PCF}=\left(\frac{\left(\Omega_{\mathrm{FG}}-\Omega_{\mathrm{UD}}\right)}{\Omega_{\mathrm{UD}}}\right) \times 100 \tag{24}
$$

where $\Omega_{\mathrm{FG}}$ and $\Omega_{\mathrm{UD}}$ are non-dimensional frequencies of a functionally graded and uniform nanocomposite, respectively. The percentage change of the frequency parameter demonstrates the effectiveness of functionally graded distributions of CNTs in comparison with the uniform distribution of CNTs.

![](./images/814519641912115201_9.jpg)

Fig. 9 Influence of the curvature ratio on the non-dimensional frequency and PCF of CCCC panels; a non-dimensional frequency, b percentage change of frequency

## 3 Numerical results

As mentioned before, an FG-CNTRC panel is a mixture of the CNTs and a polymer matrix. To perform parametric studies, poly{(m-phenylenevinylene)-co-[(2,5-dioctoxy-p-phenylene) vinyl-ene]} well known as PmPV is considered as polymer matrix with the mechanical properties of $E^m = 2.1$ GPa, $\nu^m = 0.34$, and $\rho^m = 1150$ kg/m³ at room temperature. Moreover, (10, 10) SWCNTs are chosen as reinforcements, and the mechanical properties of CNTs are taken to be $E_{11}^{\text{CNT}} = 5.6466$ TPa, $E_{22}^{\text{CNT}} = 7.0800$ TPa, $G_{12}^{\text{CNT}} = 1.9445$ TPa, $\nu_{12}^{\text{CNT}} = \nu_{21}^{\text{CNT}} = 0.175$, and $\rho^{\text{CNT}} = 1400$ kg/m³ [57].

It is shown that the rule of mixture method should be modified via CNT effectiveness parameters, $\eta_i$ [10]. The CNT effectiveness parameters are predicted by matching properties calculated by the MD simulations and those obtained from the modified rule of mixture. In the following numerical results, the CNT effectiveness parameters are taken as [58]: $\eta_1 = 0.149$ and $\eta_2 = 0.934$ for $\text{V}_{\text{CNT}}^* = 0.11$, $\eta_1 = 0.150$ and $\eta_2 = 0.941$ for $\text{V}_{\text{CNT}}^* = 0.14$, moreover, $\eta_1 = 0.149$ and $\eta_2 = 1.381$ for $\text{V}_{\text{CNT}}^* = 0.17$, furthermore, $\eta_3 = \eta_2$.

![](./images/814519641912115201_10.jpg)

Fig. 10 Effect of the aspect ratio on the vibrational characteristics of a CNTRC spherical panel; a frequencies of SSSS panels, b frequencies of CCCC panels, c PCF of SSSS panels

Frequency analysis of doubly curved panels

![](./images/814519641912115201_11.jpg)

Fig. 11 Influence of the aspect ratio on the vibrational characteristics of a CNTRC cylindrical panel; a frequencies of SSSS panels, b frequencies of CCCC panels, c PCF of SSSS panels

![](./images/814519641912115201_12.jpg)

Fig. 12 Change of non-dimensional frequency and PCF of a CNTRC hyperbolic paraboloid panel with respect to the aspect ratio;
a frequencies of SSSS panels, b frequencies of CCCC panels, c PCF of SSSS panels

Frequency analysis of doubly curved panels

![](./images/814519641912115201_13.jpg)

Fig. 13 Variation of the non-dimensional frequency and PCF of an SSSS spherical panel with respect to the shallowness ratio; a non-dimensional frequency, b PCF

Initially, convergence studies are carried out in order to specify the proper number of modes and ensure accuracy and effectiveness of the present approach. For the sake of simplicity, the number of modes, $m'$ and $n'$, is assumed to be equal. The convergence of the natural frequency of CSCS and CCCC nanocomposite spherical panels is presented in Fig. 3. In the convergence study, UD panels with $a/b = 1$, $a/h = 20$, $a/R_{\mathrm{x}} = 1$ and $\mathrm{V}_{\mathrm{CNT}}^{*}=0.11$ are considered. It can be observed that with the increase of the number of modes, the natural frequency of nanocomposite spherical panels converges monotonically. According to the results of Fig. 3, we find that $m'=n'=18$ is an appropriate number of modes for both CSCS and CCCC panels.

To confirm the accuracy of the present investigation, non-dimensional frequencies of thick $\mathrm{Al}/\mathrm{Al}_{2}\mathrm{O}_{3}$ functionally graded shells are computed and compared with those available in the literature. In the validation study, special cases of movable simply supported panels with $a_{\mathrm{s}}/b_{\mathrm{s}}=1$ and $a_{\mathrm{s}}/h=10$ are considered. The $a_{\mathrm{s}}$ and $b_{\mathrm{s}}$ are lengths of the rectangular plan-form in the $x$- and $y$-directions, respectively. The results of the comparison study are presented in Table 1, and the non-dimensional frequency is defined as follows:

$$
\Omega=\omega h \sqrt{\rho_{\mathrm{c}} / E_{\mathrm{c}}} \tag{25}
$$

![](./images/814519641912115201_14.jpg)

Fig. 14 Influence of the shallowness ratio on the vibration of an SSSS cylindrical panel; a non-dimensional frequency, b PCF

where $\rho_{\mathrm{c}}$ and $E_{\mathrm{c}}$ are density and Young's modulus of alumina, and $k$ is the volume fraction exponent. The mechanical properties of alumina and aluminum in the comparison analysis are considered the same as mentioned in Ref. [59]. The results are found to be in good agreement with the existing data in Refs. [59-61].

Furthermore, comparison studies of the non-dimensional frequencies for various boundary conditions are presented in Table 2. Spherical and cylindrical isotropic panels with different combinations of boundary conditions, for instance $\mathrm{S}^{*} \mathrm{~S}^{*} \mathrm{~S}^{*} \mathrm{~S}, \mathrm{CS}^{*} \mathrm{CS}^{*}$ and $\mathrm{CCCC}$, are considered. Here, $a_{\mathrm{s}} / b_{\mathrm{s}}=1, v=0.3$, and $b_{\mathrm{s}} / h=$ 100 are considered, and the non-dimensional frequency is defined as

$$
\Omega=\omega\left(\frac{a_{\mathrm{s}} b_{\mathrm{s}}}{h}\right) \sqrt{\frac{12 \rho\left(1-v^{2}\right)}{E}} \tag{26}
$$

where $\rho, v$ and $E$ are density, Poisson's ratio and Young's modulus of isotropic panels. Reasonable agreement between the present results and those reported in Ref. [62] can be seen.

Figure 4 reveals the effects of edge boundary conditions on the non-dimensional frequency of CNTRC panels for various aspect ratios. Here, spherical UD-CNTRC panels with SSSS, $\mathrm{S}^{*} \mathrm{~S}^{*} \mathrm{~S}^{*} \mathrm{~S}^{*}, \mathrm{SCSC}, \mathrm{CSCS}$ and CCCC boundary conditions are considered. Here, we take $a / h=20, a / R_{x}=0.5$, and $\mathrm{V}_{\mathrm{CNT}}^{*}=0.11$. It should be noted that the difference between non-dimensional frequency of CCCC and CSCS panels is relatively larger for high aspect ratio panels. Furthermore, one can observe similar phenomena for

Frequency analysis of doubly curved panels

![](./images/814519641912115201_15.jpg)

Fig. 15 Effect of the shallowness ratio on the vibration of an SSSS hyperbolic paraboloid panel; a non-dimensional frequency, b PCF

SSSS and SCSC panels. As it is expected, CCCC and SSSS panels have the most and the least non-dimensional natural frequencies, respectively. Hence, in the following parametric studies, vibrational characteristics of doubly curved FG-CNTRC panels with CCCC and SSSS boundary conditions are investigated.

To illustrate the effect of the volume fractions, the non-dimensional frequencies of the SSSS and CCCC doubly curved nanocomposite panels are listed in Tables 3 and 4, respectively. Here, special cases of doubly curved panels such as a cylindrical, spherical and hyperbolic paraboloid shell are considered, and the geometrical dimensions of the panels are taken as $a/b = 1$ and $a/h = 20$. As it is expected, for different distributions of the CNTs with the increase of $V_{\text{CNT}}^{*}$, the non-dimensional frequencies of the plate and doubly curved panels increase due to the enhancement of the stiffness of the panels.

The influence of the curvature ratio, $R_x/R_y$, on the first seven frequencies of SSSS FG-X panels and the first eight natural frequencies of CCCC FG-X panels are depicted in Figs. 5 and 6, respectively. Here, we take $a/b = 1$, $a/h = 50$, $a/R_x = 0.5$ and $V_{\text{CNT}}^{*} = 0.11$. It is shown that the vibration modes vary in distinct manners as functions of the curvature ratio. The non-dimensional frequencies are either monotonic (non-decreasing) functions of curvature ratio or non-monotonic ones. It is seen that several frequency modes of SSSS and CCCC panels approach each other gradually and cross them afterward. This is known as crossings phenomenon [63,64]. This phenomenon has been observed previously by Lei et al. [39] in the vibration of CNTRC rotating cylindrical panels.

![](./images/814519641912115201_16.jpg)

Fig. 16 Variation of the non-dimensional frequency of a CCCC doubly curved panel with respect to the shallowness ratio; a spherical panel, b cylindrical panel, c hyperbolic paraboloid panel

![](./images/814519641912115201_17.jpg)

Fig. 17 Variation of the non-dimensional frequency and PCF of FG-X SSSS panels with respect to the curvature ratio for various values of the thickness ratio; a non-dimensional frequency, b PCF

The mode shapes corresponding to the first five frequencies of the SSSS FG-X spherical panel are illus- trated in Fig. 7. The corresponding geometrical and material properties are the same as in the aforementioned parametric study.

Figures 8 and 9 reveal the variation of non-dimensional frequency and PCF with respect to the curvature ratio for SSSS and CCCC CNTRC with $V_{\mathrm{CNT}}^{*}=0.11$, respectively. The geometrical dimensions of the panels are taken as $a/b=1,a/h=50$, and $a/R_{x}=0.5$. Based on Figs. 8a and 9a, FG-X and FG-O nanocomposite doubly curved panels have the most and the least non-dimensional natural frequencies, respectively. It is clear that for positive curvature ratio the non-dimensional frequencies of both SSSS and CCCC panels increase by increasing curvature ratio. For negative curvature ratio, the non-dimensional frequencies of CCCC panels decrease by increasing curvature ratio. Moreover, the hyperbolic paraboloid SSSS panels have the least non- dimensional frequencies among the special cases of a doubly curved panel (spherical, cylindrical and hyperbolic paraboloid), and the cylindrical CCCC panels have the least non-dimensional frequencies among the special cases of a CCCC panel. Furthermore, the effectiveness of functionally graded distributions of CNTs is displayed in Figs. 8b and 9b. FG-X panels show the highest effectiveness of FG distributions under both SSSS and CCCC edge boundary conditions. Unlike the FG-X panels, the other FG-CNTRC panels reveal negative effectiveness with respect to a UD nanocomposite. It can be seen from Fig. 8b that the percentage change of frequency of FG-X can be about $20\%$ for a hyperbolic paraboloid panel. For a larger value of curvature ratio, PCF of FG-X

![](./images/814519641912115201_18.jpg)

Fig. 18 Effect of the thickness ratio on the vibrational characteristics of an SSSS spherical panel; a non-dimensional frequency, b PCF

SSSS panel decreases and can be less than 2.7 % for a curvature ratio equal to 3. Furthermore, Fig. 9b reveals that for all values of curvature ratio, FG distribution of CNTs in FG-X CCCC panel are appropriately effective.

Figures 10, 11, and 12 show the effects of the aspect ratio, $a/b$, on the vibration of CNTRC spherical, cylindrical, and hyperbolic paraboloid panels, respectively. Here, we take $a/h=20$, $a/R_x=0.5$, and $V_{\text{CNT}}^*=0.11$. It is shown that with the increase of the aspect ratio, the non-dimensional frequency of spherical and cylindrical panels under both SSSS and CCCC boundary conditions increases uniformly. Moreover, the non-dimensional frequencies of hyperbolic paraboloid SSSS panels increase monotonically for an aspect ratio larger than unity, unlike for a smaller value of the aspect ratio. Furthermore, Figs. 10c, 11c and 12c reveal that by increasing aspect ratio the percentage change of the frequency parameter decreases remarkably. For instance, at the aspect ratio equal to 3, the effectiveness of FG distributions for FG-X spherical and cylindrical panels under SSSS boundary condition is less than 4.8 %.

The influence of shallowness ratio, $a/R_x$, on the vibration of CNTRC doubly curved panels (spherical, cylindrical, and hyperbolic paraboloid panels, respectively) under SSSS boundary condition is illustrated in Figs. 13, 14, and 15. Here, we take $a/h=20$, $a/b=1$, and $V_{\text{CNT}}^*=0.11$. Figure 13 reveals that the non-dimensional frequencies of SSSS spherical panels increase sharply with the increase of the shallowness ratio for all kinds of CNTRC. Moreover, the percentage change of the frequency parameter decreases to negligible values by increasing shallowness ratio. Furthermore, Fig. 14 states that with the increase of the shallowness ratio the non-dimensional frequencies of UD, FG-A, FG-V and FG-O SSSS cylindrical panels increase although notable changes of the non-dimensional frequencies of FG-X are not observed. It is noticeable that the larger

Frequency analysis of doubly curved panels

![](./images/814519641912115201_19.jpg)

Fig. 19 Influence of the thickness ratio on the vibrational characteristics of an SSSS cylindrical panel; a non-dimensional frequency, b PCF

the shallowness ratio, the smaller the effectiveness of the FG distributions. In addition, Fig. 15 shows that by increasing shallowness ratio the non-dimensional frequencies of a hyperbolic paraboloid panels decrease. However, by increasing shallowness ratio, the percentage change of the frequency parameters does not reveal considerable variations and remains almost unchanged. It is noticeable that the shallowness ratio equal to zero represents a CNTRC plate, and the percentage change of the frequency of an FG-X plate is about 14.5 %.

Figure 16 reveals the variation of non-dimensional frequency with respect to the shallowness ratio, $a/R_x$, for CCCC doubly curved panels with $V_{\text{CNT}}^* = 0.11$, respectively. Here, the geometrical dimensions of panels are taken as $a/h = 20$ and $a/b = 1$. Figure 16a shows that with the increase of the shallowness ratio, the non-dimensional frequencies of a CCCC spherical panel increase. Furthermore, the variation of non-dimensional frequency of a CCCC cylindrical panel with respect to the shallowness ratio is depicted in Fig. 16b. It is seen that for small values of the shallowness ratio (smaller than 0.5) the non-dimensional frequencies increase by increasing $a/R_x$, while for larger values of the shallowness ratio decreasing trends are observed. In addition, the non-dimensional frequency of extremely shallow hyperbolic paraboloid panel increases with the increase of the shallowness ratio (Fig. 16c). For values of the shallowness ratio larger than 0.5, notable changes of the non-dimensional frequencies of a CCCC hyperbolic paraboloid panel are not observed.

Figure 17 shows the influence of the thickness ratio, $h/a$, on the non-dimensional frequency and PCF of FG-X panels under SSSS boundary conditions. Furthermore, Figs. 18, 19, and 20 reveal the effect of the thickness ratio on the vibration of SSSS spherical, cylindrical and hyperbolic paraboloid panels, respectively. In this numerical example, to examine influences of the thickness ratio, the non-dimensional frequency is redefined as

![](./images/814519641912115201_20.jpg)

Fig. 20 Change of the non-dimensional frequency and PCF of an SSSS hyperbolic paraboloid panel with respect to the thickness ratio; a non-dimensional frequency, b PCF

$$
\Omega=\omega a \sqrt{\frac{\rho^{m}}{E^{m}}}, \tag{27}
$$

Here, we take $a/R_x=0.5$, $a/b=1$, and $V^*_{\text{CNT}}=0.11$. It is shown that with the increase of the thickness ratio, the non-dimensional frequencies of all types of doubly curved panels increase. Moreover, for CNTRC hyperbolic paraboloid panels the effectiveness of FG distributions decreases with the increase of the thickness ratio, whereas the PCF for spherical and cylindrical panels varies non-monotonically.

Figure 21 shows the influence of thickness ratio, $h/a$, on the non-dimensional frequency and PCF of FG-X panels under CCCC edge boundary conditions. The corresponding geometrical and material properties are the same as in the aforementioned parametric study. Similar to the natural frequencies of SSSS panels, by increasing the thickness ratio the non-dimensional frequencies of CCCC doubly curved panels increase. Furthermore, for larger values of thickness ratio (larger than 0.05), the effectiveness of the FG distribution of CNTs in an FG-X CCCC panel is negligible. Furthermore, Fig. 22 reveals the effect of the thickness ratio on the natural frequencies of CCCC spherical, cylindrical, and hyperbolic paraboloid panels. As it is expected, the non-dimensional frequencies of CCCC doubly curved panels increase with the increase of the thickness ratio.

![](./images/814519641912115201_21.jpg)

Fig. 21 Variation of the natural frequency and PCF of FG-X CCCC panels with respect to the curvature ratio for various values of the thickness ratio; a non-dimensional frequency, b PCF

## 4 Conclusions
A vibrational analysis of moderately thick FG-CNTRC doubly curved panels is the main contribution of the present paper. In this research, special types of the doubly curved panels, for instance cylindrical, spherical, and hyperbolic paraboloid shells under different combinations of boundary conditions were considered. To study the vibrational characteristics of moderately thick FG-CNTRC panels, mechanical properties of FG- CNTRC shell panels were estimated via the modified rule of mixture. By the use of Hamilton's principle and the first-order shear deformation theory, five complex and highly coupled differential equations of motion were derived. Here, Galerkin's method was employed to attain the natural frequencies of FG-CNTRC doubly curved shell panels. Firstly, convergence studies were conducted to determine the number of modes and ensure the convergence of the present approach for various boundary conditions. In order to confirm the accuracy of the suggested model, the results were compared with the existing data in the literature. The effects of different combinations of edge boundary conditions were investigated. To study the vibrational behavior, the influences of volume fraction of CNTs, thickness ratio, aspect ratio, curvature ratio and shallowness ratio on the SSSS and CCCC doubly curved panels were examined. In addition, the corresponding mode shapes of the movable simply supported panel were depicted. Furthermore, the effectiveness of functionally graded distributions of CNTs in comparison with the uniform distribution of CNTs was studied. As it is expected, the fully movable simply

![](./images/814519641912115201_22.jpg)

Fig. 22 Effect of the thickness ratio on the non-dimensional frequency of CCCC doubly curved panels; a spherical panel, b cylindrical panel, c hyperbolic paraboloid panel

Frequency analysis of doubly curved panels

supported and fully clamped panels had the least and the most non-dimensional frequencies, respectively. The results revealed that with the increase of the aspect ratio the non-dimensional frequencies of all types of SSSS and CCCC doubly curved panels increased significantly. However, the PCF of SSSS panels decreased with the increase of the aspect ratio. For both SSSS and CCCC panels, FG-X and FG-O doubly curved panels had the most and the least non-dimensional natural frequencies, respectively. Furthermore, with the increase of the shallowness ratio of spherical and cylindrical panels under SSSS boundary condition, the percentage change of frequency decreased. However, the PCF of SSSS hyperbolic paraboloid panel remained almost unchanged with the increase of the shallowness ratio. By increasing the thickness ratio, the non-dimensional frequencies of all types of SSSS and CCCC doubly curved panels increased. Additionally, the effectiveness of FG distribution of CNTs in a thicker FG-X panel under CCCC boundary conditions was negligible. The presented new results for the CNTRC doubly curved panels can be used as benchmark solution for future researches.

### Appendix

The matrices $\mathbf{A}$ and $\mathbf{B}$ can calculated by integration as follows:

$$
\begin{aligned}
\mathbf{A}_{i j} &=\int_{0}^{b} \int_{0}^{a} \mathbf{P}_{i j} \mathrm{d} x \mathrm{d} y \quad i, j=(1, \ldots, 10), \\
\mathbf{B}_{i j} &=\int_{0}^{b} \int_{0}^{a} \mathbf{T}_{i j} \mathrm{d} x \mathrm{d} y.
\end{aligned} \tag{A1}
$$

The components of the matrix $\mathbf{P}$ can be expressed in terms of shape functions as

$$
\begin{gathered}
\mathbf{P}_{i i}=\mathbf{I} \quad(i=1,3,5,7,9), \quad \mathbf{P}_{i j}=\mathbf{0} \quad(i=1,3,5,7,9 \text { and } i \neq j) \\
\mathbf{P}_{22}=\left(I_{0}+\frac{2 I_{1}}{R_{x}}+\frac{I_{2}}{R_{x}^{2}}\right) \boldsymbol{\Phi}_{u} \boldsymbol{\Phi}_{u}^{T}, \quad \mathbf{P}_{28}=\left(I_{1}+\frac{I_{2}}{R_{x}}\right), \boldsymbol{\Phi}_{u} \boldsymbol{\Phi}_{x}^{T}, \quad \mathbf{P}_{2 j}=\mathbf{0} \quad(j \neq 2,8) \\
\mathbf{P}_{44}=\left(I_{0}+\frac{2 I_{1}}{R_{y}}+\frac{I_{2}}{R_{y}^{2}}\right) \boldsymbol{\Phi}_{v} \boldsymbol{\Phi}_{v}^{T}, \quad \mathbf{P}_{410}=\left(I_{1}+\frac{I_{2}}{R_{y}}\right) \boldsymbol{\Phi}_{v} \boldsymbol{\Phi}_{y}^{T}, \quad \mathbf{P}_{4 j}=\mathbf{0} \quad(j \neq 4,10) \\
\mathbf{P}_{66}=-I_{0} \boldsymbol{\Phi}_{w} \boldsymbol{\Phi}_{w}^{T}, \quad \mathbf{P}_{6 j}=\mathbf{0} \quad(j \neq 6) \\
\mathbf{P}_{82}=\left(I_{1}+\frac{I_{2}}{R_{x}}\right) \boldsymbol{\Phi}_{x} \boldsymbol{\Phi}_{u}^{T}, \quad \mathbf{P}_{88}=I_{2} \boldsymbol{\Phi}_{x} \boldsymbol{\Phi}_{x}^{T} \\
\mathbf{P}_{8 j}=\mathbf{0} \quad(j \neq 2,8), \\
\mathbf{P}_{104}=\left(I_{1}+\frac{I_{2}}{R_{y}}\right) \boldsymbol{\Phi}_{y} \boldsymbol{\Phi}_{v}^{T}, \quad \mathbf{P}_{1010}=I_{2} \boldsymbol{\Phi}_{y} \boldsymbol{\Phi}_{y}^{T}, \quad \mathbf{P}_{10 j}=\mathbf{0} \quad(j \neq 4,10).
\end{gathered} \tag{A2}
$$

Furthermore, matrix $\mathbf{T}$ can be given in matrix form as

$$
[\mathbf{T}]=\left[\begin{array}{cccccccccc}
\mathbf{0} & \mathbf{I} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} \\
\mathbf{a}_{1} & \mathbf{0} & \mathbf{a}_{2} & \mathbf{0} & \mathbf{a}_{3} & \mathbf{0} & \mathbf{a}_{4} & \mathbf{0} & \mathbf{a}_{5} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{I} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} \\
\mathbf{b}_{1} & \mathbf{0} & \mathbf{b}_{2} & \mathbf{0} & \mathbf{b}_{3} & \mathbf{0} & \mathbf{b}_{4} & \mathbf{0} & \mathbf{b}_{5} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{I} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} \\
\mathbf{c}_{1} & \mathbf{0} & \mathbf{c}_{2} & \mathbf{0} & \mathbf{c}_{3} & \mathbf{0} & \mathbf{c}_{4} & \mathbf{0} & \mathbf{c}_{5} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{I} & \mathbf{0} & \mathbf{0} \\
\mathbf{d}_{1} & \mathbf{0} & \mathbf{d}_{2} & \mathbf{0} & \mathbf{d}_{3} & \mathbf{0} & \mathbf{d}_{4} & \mathbf{0} & \mathbf{d}_{5} & \mathbf{0} \\
\mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{I} \\
\mathbf{e}_{1} & \mathbf{0} & \mathbf{e}_{2} & \mathbf{0} & \mathbf{e}_{3} & \mathbf{0} & \mathbf{e}_{4} & \mathbf{0} & \mathbf{e}_{5} & \mathbf{0}
\end{array}\right] \tag{A3}
$$

where $\mathbf{a}_i$, $\mathbf{b}_i$, $\mathbf{c}_i$, $\mathbf{d}_i$ and $\mathbf{e}_i$ ($i=1,...,5$) are nonzero matrices and can be found as follows:

$$
\mathbf{a}_{\mathbf{1}}=A_{1} \boldsymbol{\Phi}_{u} \frac{\partial^{2} \boldsymbol{\Phi}_{u}^{T}}{\partial x^{2}}+\left(C_{1}-2 S C_{2}+S^{2}\right) \boldsymbol{\Phi}_{u} \frac{\partial^{2} \boldsymbol{\Phi}_{u}^{T}}{\partial y^{2}}-\frac{K_{s} F_{1}}{R_{x}^{2}} \boldsymbol{\Phi}_{u} \boldsymbol{\Phi}_{u}^{T}, \quad \mathbf{a}_{\mathbf{2}}=\left(v_{12} B_{1}+C_{1}-S^{2}\right) \boldsymbol{\Phi}_{u} \frac{\partial^{2} \boldsymbol{\Phi}_{v}^{T}}{\partial x \partial y},
$$

$$
\mathbf{a}_{\mathbf{3}}=\left(\frac{A_{1}+K_{s} F_{1}}{R_{x}}+\frac{v_{12} B_{1}}{R_{y}}\right) \boldsymbol{\Phi}_{u} \frac{\partial \boldsymbol{\Phi}_{w}^{T}}{\partial x}, \quad \mathbf{a}_{\mathbf{4}}=A_{2} \boldsymbol{\Phi}_{u} \frac{\partial^{2} \boldsymbol{\Phi}_{x}^{T}}{\partial x^{2}}+\left(C_{2}-S C_{3}\right) \boldsymbol{\Phi}_{u} \frac{\partial^{2} \boldsymbol{\Phi}_{x}^{T}}{\partial y^{2}}+\frac{K_{s} F_{1}}{R_{x}} \boldsymbol{\Phi}_{u} \boldsymbol{\Phi}_{x}^{T},
$$

$$
\mathbf{a}_{\mathbf{5}}=\left(v_{12} B_{2}+C_{2}-C_{3} S\right) \boldsymbol{\Phi}_{u} \frac{\partial^{2} \boldsymbol{\Phi}_{y}^{T}}{\partial x \partial y},
$$

$$
\mathbf{b}_{\mathbf{1}}=\left(v_{12} B_{1}+C_{1}-S^{2}\right) \boldsymbol{\Phi}_{v} \frac{\partial^{2} \boldsymbol{\Phi}_{u}^{T}}{\partial x \partial y}, \quad \mathbf{b}_{\mathbf{2}}=B_{1} \boldsymbol{\Phi}_{v} \frac{\partial^{2} \boldsymbol{\Phi}_{v}^{T}}{\partial y^{2}}+\left(C_{1}+2 S C_{2}+S^{2}\right) \boldsymbol{\Phi}_{v} \frac{\partial^{2} \boldsymbol{\Phi}_{v}^{T}}{\partial x^{2}}-\frac{K_{s} D_{1}}{R_{y}^{2}} \boldsymbol{\Phi}_{v} \boldsymbol{\Phi}_{v}^{T},
$$

$$
\mathbf{b}_{\mathbf{3}}=\left(\frac{B_{1}+K_{s} D_{1}}{R_{y}}+\frac{v_{12} B_{1}}{R_{x}}\right) \boldsymbol{\Phi}_{v} \frac{\partial \boldsymbol{\Phi}_{w}^{T}}{\partial y}, \quad \mathbf{b}_{\mathbf{4}}=\left(v_{12} B_{2}+C_{2}+C_{3} S\right) \boldsymbol{\Phi}_{v} \frac{\partial^{2} \boldsymbol{\Phi}_{x}^{T}}{\partial x \partial y},
$$

$$
\mathbf{b}_{\mathbf{5}}=B_{2} \boldsymbol{\Phi}_{v} \frac{\partial^{2} \boldsymbol{\Phi}_{y}^{T}}{\partial y^{2}}+\left(C_{2}+S C_{3}\right) \boldsymbol{\Phi}_{v} \frac{\partial^{2} \boldsymbol{\Phi}_{y}^{T}}{\partial x^{2}}+\frac{K_{s} D_{1}}{R_{y}} \boldsymbol{\Phi}_{v} \boldsymbol{\Phi}_{y}^{T},
$$

$$
\mathbf{c}_{\mathbf{1}}=\left(\frac{A_{1}+K_{s} F_{1}}{R_{x}}+\frac{v_{12} B_{1}}{R_{y}}\right) \boldsymbol{\Phi}_{w} \frac{\partial \boldsymbol{\Phi}_{u}^{T}}{\partial x}, \quad \mathbf{c}_{\mathbf{2}}=\left(\frac{B_{1}+K_{s} D_{1}}{R_{y}}+\frac{v_{12} B_{1}}{R_{x}}\right) \boldsymbol{\Phi}_{w} \frac{\partial \boldsymbol{\Phi}_{v}^{T}}{\partial y},
$$

$$
\mathbf{c}_{\mathbf{3}}=\left(\frac{A_{1}}{R_{x}^{2}}+\frac{B_{1}}{R_{y}^{2}}+\frac{2 v_{12} B_{1}}{R_{x} R_{y}}\right) \boldsymbol{\Phi}_{w} \boldsymbol{\Phi}_{w}^{T}-\left(K_{s} F_{1}\right) \boldsymbol{\Phi}_{w} \frac{\partial^{2} \boldsymbol{\Phi}_{w}^{T}}{\partial x^{2}}-\left(K_{s} D_{1}\right) \boldsymbol{\Phi}_{w} \frac{\partial^{2} \boldsymbol{\Phi}_{w}^{T}}{\partial y^{2}},
$$

$$
\mathbf{c}_{\mathbf{4}}=\left(\frac{A_{2}}{R_{x}}+\frac{v_{12} B_{2}}{R_{y}}-K_{s} F_{1}\right) \boldsymbol{\Phi}_{w} \frac{\partial \boldsymbol{\Phi}_{x}^{T}}{\partial x}, \quad \mathbf{c}_{\mathbf{5}}=\left(\frac{B_{2}}{R_{y}}+\frac{v_{12} B_{2}}{R_{x}}-K_{s} D_{1}\right) \boldsymbol{\Phi}_{w} \frac{\partial \boldsymbol{\Phi}_{y}^{T}}{\partial y},
$$

$$
\mathbf{d}_{\mathbf{1}}=A_{2} \boldsymbol{\Phi}_{x} \frac{\partial^{2} \boldsymbol{\Phi}_{u}^{T}}{\partial x^{2}}+\left(C_{2}-S\right) \boldsymbol{\Phi}_{x} \frac{\partial^{2} \boldsymbol{\Phi}_{u}^{T}}{\partial y^{2}}+\frac{K_{s} F_{1}}{R_{x}} \boldsymbol{\Phi}_{x} \boldsymbol{\Phi}_{u}^{T}, \quad \mathbf{d}_{\mathbf{2}}=\left(v_{12} B_{2}+C_{2}+S\right) \boldsymbol{\Phi}_{x} \frac{\partial^{2} \boldsymbol{\Phi}_{v}^{T}}{\partial x \partial y},
$$

$$
\mathbf{d}_{\mathbf{3}}=\left(\frac{A_{2}}{R_{x}}+\frac{v_{12} B_{2}}{R_{y}}-K_{s} F_{1}\right) \boldsymbol{\Phi}_{x} \frac{\partial \boldsymbol{\Phi}_{w}^{T}}{\partial x}, \quad \mathbf{d}_{\mathbf{4}}=A_{3} \boldsymbol{\Phi}_{x} \frac{\partial^{2} \boldsymbol{\Phi}_{x}^{T}}{\partial x^{2}}+C_{3} \boldsymbol{\Phi}_{x} \frac{\partial^{2} \boldsymbol{\Phi}_{x}^{T}}{\partial y^{2}}-K_{s} F_{1} \boldsymbol{\Phi}_{x} \boldsymbol{\Phi}_{x}^{T},
$$

$$
\mathbf{d}_{\mathbf{5}}=\left(C_{3}+v_{12} B_{3}\right) \boldsymbol{\Phi}_{x} \frac{\partial^{2} \boldsymbol{\Phi}_{y}^{T}}{\partial x \partial y},
$$

$$
\mathbf{e}_{\mathbf{1}}=\left(v_{12} B_{2}+C_{2}-S\right) \boldsymbol{\Phi}_{y} \frac{\partial^{2} \boldsymbol{\Phi}_{u}^{T}}{\partial x \partial y}, \quad \mathbf{e}_{\mathbf{2}}=B_{2} \boldsymbol{\Phi}_{y} \frac{\partial^{2} \boldsymbol{\Phi}_{v}^{T}}{\partial y^{2}}+\left(C_{2}+S\right) \boldsymbol{\Phi}_{y} \frac{\partial^{2} \boldsymbol{\Phi}_{v}^{T}}{\partial x^{2}}+\frac{K_{s} D_{1}}{R_{y}} \boldsymbol{\Phi}_{y} \boldsymbol{\Phi}_{v}^{T},
$$

$$
\mathbf{e}_{\mathbf{3}}=\left(\frac{B_{2}}{R_{y}}+\frac{v_{12} B_{2}}{R_{x}}-K_{s} D_{1}\right) \boldsymbol{\Phi}_{y} \frac{\partial \boldsymbol{\Phi}_{w}^{T}}{\partial y}, \quad \mathbf{e}_{\mathbf{4}}=\left(v_{12} B_{3}+C_{3}\right) \boldsymbol{\Phi}_{y} \frac{\partial^{2} \boldsymbol{\Phi}_{x}^{T}}{\partial x \partial y},
$$

$$
\mathbf{e}_{\mathbf{5}}=C_{3} \boldsymbol{\Phi}_{y} \frac{\partial^{2} \boldsymbol{\Phi}_{y}^{T}}{\partial x^{2}}+B_{3} \boldsymbol{\Phi}_{y} \frac{\partial^{2} \boldsymbol{\Phi}_{y}^{T}}{\partial y^{2}}-K_{s} D_{1} \boldsymbol{\Phi}_{y} \boldsymbol{\Phi}_{y}^{T}. \tag{A4}
$$

References

1. Treacy, M.M.J., Ebbesen, T.W., Gibson, J.M.: Exceptionally high Young's modulus observed for individual carbon nanotubes. Nature 38, 678-680 (1996)
2. Lu, J.P.: Elastic properties of carbon nanotubes and nanoropes. Phys. Rev. Lett. 79, 1297-1300 (1997)
3. Dai, H.: Carbon nanotubes: opportunities and challenges. Surf. Sci. 500, 218-241 (2002)
4. Cadek, M., Coleman, J.N., Barron, V., Hedicke, K., Blau, W.J.: Morphological and mechanical properties of carbon-nanotube-reinforced semicrystalline and amorphous polymer composites. Appl. Phys. Lett. 81, 5123-5125 (2002)
5. Thostenson, E.T., Chou, T.W.: On the elastic properties of carbon nanotube-based composites: modelling and characterization. J. Phys. D Appl. Phys. 36, 573-582 (2003)
6. Qian, D., Dickey, E.C., Andrews, R., Rantell, T.: Load transfer and deformation mechanisms in carbon nanotube-polystyrene composites. Appl. Phys. Lett. 76, 2868-2870 (2000)
7. Griebel, M., Hamaekers, J.: Molecular dynamics simulations of the elastic moduli of polymer-carbon nanotube composites. Comput. Methods Appl. Mech. Eng. 193, 1773-1788 (2004)

Frequency analysis of doubly curved panels

8. Hu, N., Fukunaga, H., Lu, C., Kameyama, M., Yan, B.: Prediction of elastic properties of carbon nanotube reinforced composites. Proc. R. Soc. A Math. Phys. **461**, 1685-1710 (2005)

9. Song, Y.S., Youn, J.R.: Modeling of effective elastic properties for polymer based carbon nanotube composites. Polymer **47**, 1741-1748 (2006)

10. Han, Y., Elliott, J.: Molecular dynamics simulations of the elastic properties of polymer/carbon nanotube composites. Comput. Mater. Sci. **39**, 315-323 (2007)

11. Ngabonziza, Y., Li, J., Barry, C.F.: Electrical conductivity and mechanical properties of multiwalled carbon nanotube-reinforced polypropylene nanocomposites. Acta Mech. **220**, 289-298 (2011)

12. Wernik, J.M., Meguid, S.A.: Multiscale modeling of the nonlinear response of nano-reinforced polymers. Acta Mech. **217**, 1-16 (2011)

13. Mehrabadi, S.J., Aragh, B.S., Khoshkhahesh, V., Taherpour, A.: Mechanical buckling of nanocomposite rectangular plate reinforced by aligned and straight single-walled carbon nanotubes. Compos. Part B Eng. **43**, 2031-2040 (2012)

14. Bhardwaj, G., Upadhyay, A.K., Pandey, R., Shukla, K.K.: Non-linear flexural and dynamic response of CNT reinforced laminated composite plates. Compos. Part B Eng. **45**, 89-100 (2013)

15. Yanase, K., Moriyama, S., Ju, J.W.: Effects of CNT waviness on the effective elastic responses of CNT-reinforced polymer composites. Acta Mech. **224**, 1351-1364 (2013)

16. Zhu, P., Zhang, L.W., Liew, K.M.: Geometrically nonlinear thermomechanical analysis of moderately thick functionally graded plates using a local Petrov-Galerkin approach with moving Kriging interpolation. Compos. Struct. **107**, 298-314 (2014)

17. Zhang, L.W., Zhu, P., Liew, K.M.: Thermal buckling of functionally graded plates using a local Kriging meshless method. Compos. Struct. **108**, 472-492 (2014)

18. Lei, Z.X., Zhang, L.W., Liew, K.M.: Elastodynamic analysis of carbon nanotube-reinforced functionally graded plates. Int. J. Mech. Sci. **99**, 208-217 (2015)

19. Zhang, L.W., Song, Z.G., Liew, K.M.: Nonlinear bending analysis of FG-CNT reinforced composite thick plates resting on Pasternak foundations using the element-free IMLS-Ritz method. Compos. Struct. **128**, 165-175 (2015)

20. Zhang, L.W., Liew, K.M.: Large deflection analysis of FG-CNT reinforced composite skew plates resting on Pasternak foundations using an element-free approach. Compos. Struct. **132**, 974-983 (2015)

21. Zhang, L.W., Liew, K.M.: Geometrically nonlinear large deformation analysis of functionally graded carbon nanotube reinforced composite straight-sided quadrilateral plates. Comput. Method Appl. Mech. Eng. **295**, 219-239 (2015)

22. Zhang, L.W., Lei, Z.X., Liew, K.M.: Buckling analysis of FG-CNT reinforced composite thick skew plates using an element-free approach. Compos. Part B Eng. **75**, 36-46 (2015)

23. Aragh, B.S., Barati, A.H.N., Hedayati, H.: Eshelby-Mori-Tanaka approach for vibrational behavior of continuously graded carbon nanotube-reinforced cylindrical panels. Compos. Part B Eng. **43**, 1943-1954 (2012)

24. Yas, M.H., Pourasghar, A., Kamarian, S., Heshmati, M.: Three-dimensional free vibration analysis of functionally graded nanocomposite cylindrical panels reinforced by carbon nanotube. Mater. Des. **49**, 583-590 (2013)

25. Moradi-Dastjerdi, R., Pourasghar, A., Foroutan, M.: The effects of carbon nanotube orientation and aggregation on vibrational behavior of functionally graded nanocomposite cylinders by a mesh-free method. Acta Mech. **224**, 2817-2832 (2013)

26. Shen, H.S., Xiang, Y.: Postbuckling of nanotube-reinforced composite cylindrical shells under combined axial and radial mechanical loads in thermal environment. Compos. Part B Eng. **52**, 311-322 (2013)

27. Moradi-Dastjerdi, R., Foroutan, M., Pourasghar, A.: Dynamic analysis of functionally graded nanocomposite cylinders reinforced by carbon nanotube by a mesh-free method. Mater. Des. **44**, 256-266 (2013)

28. Liew, K.M., Lei, Z.X., Yu, J.L., Zhang, L.W.: Postbuckling of carbon nanotube-reinforced functionally graded cylindrical panels under axial compression using a meshless approach. Comput. Method Appl. Mech. Eng. **268**, 1-17 (2014)

29. Alibeigloo, A.: Free vibration analysis of functionally graded carbon nanotube-reinforced composite cylindrical panel embedded in piezoelectric layers by using theory of elasticity. Eur. J. Mech. A Solids **44**, 104-115 (2014)

30. Heydarpour, Y., Aghdam, M.M., Malekzadeh, P.: Free vibration analysis of rotating functionally graded carbon nanotube-reinforced composite truncated conical shells. Compos. Struct. **117**, 187-200 (2014)

31. Zhang, L.W., Lei, Z.X., Liew, K.M., Yu, J.L.: Large deflection geometrically nonlinear analysis of carbon nanotube-reinforced functionally graded cylindrical panels. Comput. Method Appl. Mech. Eng. **273**, 1-18 (2014)

32. Mehrabadi, S.J., Aragh, B.S.: Stress analysis of functionally graded open cylindrical shell reinforced by agglomerated carbon nanotubes. Thin Wall. Struct. **80**, 130-141 (2014)

33. Zhang, L.W., Lei, Z.X., Liew, K.M., Yu, J.L.: Static and dynamic of carbon nanotube reinforced functionally graded cylindrical panels. Compos. Struct. **111**, 205-212 (2014)

34. Lei, Z.X., Zhang, L.W., Liew, K.M., Yu, J.L.: Dynamic stability analysis of carbon nanotube-reinforced functionally graded cylindrical panels using the element-free kp-Ritz method. Compos. Struct. **113**, 328-338 (2014)

35. Shen, H.S., Xiang, Y.: Postbuckling of axially compressed nanotube-reinforced composite cylindrical panels resting on elastic foundations in thermal environments. Compos. Part B Eng. **67**, 50-61 (2014)

36. Zarouni, E., Rad, M.J., Tohidi, H.: Free vibration analysis of fiber reinforced composite conical shells resting on Pasternak-type elastic foundation using Ritz and Galerkin methods. Int. J. Mech. Mater. Des. **10**, 421-438 (2014)

37. Ghorbanpour Arani, A., Haghparast, E., Khoddami Maraghi, Z., Amir, S.: Static stress analysis of carbon nano-tube reinforced composite (CNTRC) cylinder under non-axisymmetric thermo-mechanical loads and uniform electro-magnetic fields. Compos. Part B Eng. **68**, 136-145 (2015)

38. Jam, J.E., Kiani, Y.: Buckling of pressurized functionally graded carbon nanotube reinforced conical shells. Compos. Struct. **125**, 586-595 (2015)

39. Lei, Z.X., Zhang, L.W., Liew, K.M.: Vibration analysis of CNT-reinforced functionally graded rotating cylindrical panels using the element-free kp-Ritz method. Compos. Part B Eng. **77**, 291-303 (2015)

40. Zhang, L.W., Cui, W.C., Liew, K.M.: Vibration analysis of functionally graded carbon nanotube reinforced composite thick plates with elastically restrained edges. Int. J. Mech. Sci. **103**, 9-21 (2015)

41. Kundalwal, S.I., Meguid, S.A.: Effect of carbon nanotube waviness on active damping of laminated hybrid composite shells. Acta Mech. **226**, 2035–2052 (2015)

42. Zhang, L.W., Lei, Z.X., Liew, K.M.: Computation of vibration solution for functionally graded carbon nanotube-reinforced composite thick plates resting on elastic foundations using the element-free IMLS-Ritz method. Appl. Math. Comput. **256**, 488–504 (2015)

43. Lei, Z.X., Zhang, L.W., Liew, K.M.: Free vibration analysis of laminated FG-CNT reinforced composite rectangular plates using the kp-Ritz method. Compos. Struct. **127**, 245–259 (2015)

44. Zhang, L.W., Song, Z.G., Liew, K.M.: State-space Levy method for vibration analysis of FG-CNT composite plates subjected to in-plane loads based on higher-order shear deformation theory. Compos. Struct. **134**, 989–1003 (2015)

45. Thomas, B., Roy, T.: Vibration analysis of functionally graded carbon nanotube-reinforced composite shell structures. Acta Mech. **227**, 581–599 (2016)

46. Zhang, L.W., Song, Z.G., Liew, K.M.: Computation of aerothermoelastic properties and active flutter control of CNT reinforced functionally graded composite panels in supersonic airflow. Comput. Method Appl. Mech. Eng. **300**, 427–441 (2016)

47. Song, Z.G., Zhang, L.W., Liew, K.M.: Active vibration control of CNT reinforced functionally graded plates based on a higher-order shear deformation theory. Int. J. Mech. Sci. **105**, 90–101 (2016)

48. Zhang, L.W., Liew, K.M., Reddy, J.N.: Postbuckling of carbon nanotube reinforced functionally graded plates with edges elastically restrained against translation and rotation under axial compression. Comput. Method Appl. Mech. Eng. **298**, 1–28 (2016)

49. Lei, Z.X., Zhang, L.W., Liew, K.M.: Analysis of laminated CNT reinforced functionally graded plates using the element-free kp-Ritz method. Compos. Part B Eng. **84**, 211–221 (2016)

50. Zhang, L.W., Song, Z.G., Liew, K.M.: Optimal shape control of CNT reinforced functionally graded composite plates using piezoelectric patches. Compos. Part B Eng. **85**, 140–149 (2016)

51. Seidel, G.D., Lagoudas, D.C.: Micromechanical analysis of the effective elastic properties of carbon nanotube reinforced composites. Mech. Mater. **38**, 884–907 (2006)

52. Fidelus, J.D., Wiesel, E., Gojny, F.H., Schulte, K., Wagner, H.D.: Thermo-mechanical properties of randomly oriented carbon/epoxy nanocomposites. Compos. Part A Appl. Sci. Manuf. **36**, 1555–1561 (2005)

53. Esawi, A.M.K., Farag, M.M.: Carbon nanotube reinforced composites: potential and current challenges. Mater. Des. **28**, 2394–2401 (2007)

54. Reddy, J.N., Asce, M.: Exact solutions of moderately thick laminated shells. J. Eng. Mech. **110**, 794–809 (1984)

55. Amabili, M.: Nonlinear Vibrations and Stability of Shells and Plates. Cambridge University Press, New York (2008)

56. Kiani, Y., Akbarzadeh, A.H., Chen, Z.T., Eslami, M.R.: Static and dynamic analysis of an FGM doubly curved panel resting on the Pasternak-type elastic foundation. Compos. Struct. **94**, 474–484 (2012)

57. Fazelzadeh, S.A., Pouresmaeeli, S., Ghavanloo, E.: Aeroelastic characteristics of functionally graded carbon nanotube- reinforced composite plates under a supersonic flow. Comput. Method. Appl. Mech. Eng. **285**, 714–729 (2015)

58. Zhu, P., Lei, Z.X., Liew, K.M.: Static and free vibration analyses of carbon nanotube-reinforced composite plates using finite element method with first order shear deformation plate theory. Compos. Struct. **94**, 1450–1460 (2012)

59. Alijani, F., Amabili, M., Bakhtiari-Nejad, F.: Thermal effects on nonlinear vibrations of functionally graded doubly curved shells using higher order shear deformation theory. Compos. Struct. **93**, 2541–2553 (2011)

60. Matsunaga, H.: Free vibration and stability of functionally graded shallow shells according to a 2-D higher-order deformation theory. Compos. Struct. **84**, 132–146 (2008)

61. Chorfi, S.M., Houmat, A.: Nonlinear free vibration of a functionally graded doubly curved shallow shell of elliptical plan- form. Compos. Struct. **92**, 2573–2581 (2010)

62. Liew, K.M., Lim, C.W.: Vibration of doubly-curved shallow shells. Acta Mech. **114**, 95–119 (1996)

63. Kuttler, J.R., Sigillito, V.G.: On curve veering. J. Sound Vib. **75**, 585–588 (1981)

64. Perkins, N.C., Mote Jr., C.D.: Comments on curve veering in eigenvalue problems. J. Sound Vib. **106**, 451–463 (1986)