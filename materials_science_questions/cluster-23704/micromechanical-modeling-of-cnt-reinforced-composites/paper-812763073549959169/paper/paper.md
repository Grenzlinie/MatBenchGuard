Regular Article

# Free vibration analysis of polyethylene/CNT plates

B. Safaei¹, N.A. Ahmed², and A.M. Fattahi²,a

¹ Department of Mechanical Engineering, Tsinghua University, Beijing 100084, China
² Department of Mechanical Engineering Science, Faculty of Engineering and Built Environment, University of Johannesburg, 2006, South Africa

Received: 20 November 2018 / Revised: 24 February 2019
Published online: 19 June 2019
© Società Italiana di Fisica / Springer-Verlag GmbH Germany, part of Springer Nature, 2019

**Abstract.** In this work, we analyzed the free vibration of single-walled carbon nanotubes (SWCNTs)-reinforced composite plates with carbon nanotubes (CNTs) embedded in amorphous polyethylene. Here, the governing differential equations of simply supported and clamped boundary conditions were found using the generalized differential quadrature (GDQ) method. We used the rules of mixture according to different plate models including first-order shear deformation theory (FSDT), classical plate theory (CLPT), and higher-order shear deformation theory (HSDT) to find the fundamental frequencies of nanocomposite plates. The properties of the materials used in the fabrication of nanocomposite plates were investigated using the Multiscale Finite Element Method (FEM) simulation for both short (10,10) and long (10,10) SWCNTs composites. The results of FEM simulations were fitted using those of the rule of mixture to obtain optimum values of CNT efficiency parameters. A few selected numerical results have been provided to investigate the effects of the volume fractions of CNTs and the types of edge supports on the value of fundamental frequency of long- and short-CNTs reinforced composite plates.

## 1 Introduction

Nanocomposites are a special group of composites which at least one of their components is at the nano scale. Most nanocomposites contain a small amount of laminar inorganic filler or carbon nanotube with individual structures. Carbon nanotube (CNT) composites are great potential candidates as future materials. Their extraordinary properties have attracted many researchers. Ajayan *et al.* [1] performed one of the first studies on polymer/CNTs composites. In their study, they mechanically dispersed multi-walled carbon nanotubes (MWCNTs) in a liquid epoxy resin. Then, several experimental and theoretical researches were conducted with CNTs as reinforcing fibers to investigate the extraordinary mechanical and electrical properties of CNTs-based composites [2–7].

Many methods and continuum mechanics theories have been widely employed in investigating composites and sandwich structures systems. Huang *et al.* [8,9] performed the investigation of the vibration and damping of the elastic-viscoelastic-elastic sandwich. They concluded that the finite-element model had high accuracy in the prediction of the natural frequencies and loss of the viscoelastic sandwich beam and plate structures. Hammel *et al.* [10] studied the manufacture and enhancement of vapor-grown carbon fibers. Using theoretical models, Lau [11] studied the load transfer properties between CNTs and polymer. They showed that the maximum value of shear stress for pulling out one single-walled carbon nanotubes was higher than that of its corresponding value for MWCNTs. Several other researches with computational techniques and simulation models have been published on the response of nanocomposite structures under different loadings [12–15]. Sahmani *et al.* [16] investigated MD simulations to obtain the optimum value of the nonlocal parameter for the critical axial buckling load and corresponding shortening of nanosheets with different side lengths. Then, they introduced the nonlocal anisotropic shear deformable plate model for the uniaxial instability of loaded 3D metallic carbon nanosheets based on MD simulations [17]. Fattahi *et al.* [18] investigated the postbuckling behavior of nanoshells reinforced with FG-CNTs exposed to hydrostatic pressure along with heat conduction in thermal environment and nonlocal condition.

The effect of CNT waviness and aspect ratio on the dynamic behavior of CNT/polymer nanocomposite cylinders [19], plates [20] and sandwich plates [21] were studied using a mesh-free method. Qin *et al.* studied the free vibrations of rotating and cylindrical shells with arbitrary boundary conditions by using the Ritz method [22,23].

a e-mail: afattahi@uj.ac.za (corresponding author)

By considering the effect of CNT agglomeration formation, biaxial buckling and free vibration analyses of sandwich plates with FG-CNT/polymer face sheets were conducted using different plate theories for each sandwich's layers [24, 25]. Some researcher by using mathematical models studied continuum theories and investigated composites and sandwich structures systems theories [26–29]. For more information regarding analytical/numerical methods recently used in considering vibration and buckling behaviour of the materials in nano/micro to large scales, we refer to [30–33].

Some researchers have studied the thermo-mechanical behavior of polymer/carbon nanotube nanocomposites. Moheimani *et al.* [34] described a closed-form micromechanical model for estimating the effective thermal behavior of unidirectional CNT-reinforced polymer nanocomposites. They also went through the effects of short and long CNT composites on thermal resistance. Moradi-Dastjerdi *et al.* [35] presented transient heat transfer analysis FG-CNT/polymer nanocomposite cylinders and they showed that the distribution of CNT has a significant effect on the thermal responses of such cylinders. Mechanical properties in plates made of FG materials in micro/nano scales vary continuously in one or more directions investigated by Mohammadsalehi *et al.* [36]. Since circular plates are extensively being employed in a wide range of engineering applications, vibration analysis of these plates have been performed by many researchers. Safaei *et al.* [37] studied the free vibration of embedded single-layered graphene sheets and in another research they [38] evaluated the critical axial buckling strain of CNTs with different chiral angles. More recently, some researches about FG and nanobeam and panels vibrations were done by this article authors [39–45] which indicate the popularity of modified continuum mechanics, free and force vibration in nanomechanics. Moheimani *et al.* [46] derived the governing differential equations of a nano functionally graded beam under axial force. Krysko *et al.* [47] studied structurally nonlinear problems for two plates being in contact with each other, and so they [48] investigated nonlinear beam-beam and beam-cylindrical shell contact interactions. In another work Awrejcewicz *et al.* [49] investigated a regular contact/no-contact nonlinear dynamics of the multi-layer structure composed of one plate by boundary conditions.

In recent years some researchers investigated the numerical modeling of platelet-reinforced composites according to the Galerkin FEM method and unit cell boundary conditions based on 3D model [50–53]. Due to huge calculations in atomistic modeling, continuum modeling is utilized extensively; however, it has problems such as low accuracy and inability to develop accurate and detailed models for nano-materials and apply intermolecular forces. So the multi-scale method was created as a combined atomistic-continuum modeling [54–56].

In this work, free vibrations of CNTs-reinforced composite plates have been investigated and a multi-scale model has been developed for nanocomposites. Since the molecular structure of polyethylene can be easily generated without any functional units with only one repetitive unit, SWCNT nanofibers were considered to be embedded in an amorphous polyethylene network where the structure of each monomer remained the same while the adjacent units were rotated around the connecting C-C bond which led to similar properties in all directions. A variety of plate theories including first-order shear deformation theory (FSDT), classical plate theory (CLPT), and higher-order shear deformation theory (HSDT) was applied to analyze the vibrations of CNTs-reinforced composite plates. Also, we used the generalized differential quadrature (GDQ) method to obtain the governing differential equations in simply supported and clamped edge supports. FEM simulations was used to investigate the material properties for both short-(10,10) and long-(10,10) SWCNTs composites. Then, the results of FEM simulations were compared with those obtained from the mixture rule to the obtained optimum values of efficiency parameters for CNTs.

## 2 Review of plate theories

Different plate theories can be applied to show the behaviors of plates [56–63]. Assume a uniform square nanoplate with length $L$ and thickness $h$ with a coordinate system $(x,y,z)$ was on one corner of the nanoplate midplane where $x$, $y$ and $z$ axes were assumed to be along the length, width, depth (thickness) of the nanoplate. The general forms of displacement components $(u,v,w)$ along the axes $(x,y,z)$ are

$$
\begin{aligned}
u(x,y,z) &= -z\frac{\partial w}{\partial x} + \psi(z)\left(\frac{\partial w}{\partial x} + \varphi_x\right), \\
v(x,y,z) &= -z\frac{\partial w}{\partial y} + \psi(z)\left(\frac{\partial w}{\partial y} + \varphi_y\right), \\
w(x,y,z) &= w(x,t),
\end{aligned} \tag{1}
$$

where $u$, $v$, $w$ are the transverse displacements and $\varphi_x$, $\varphi_y$ are the angular displacements along the $x$ and $y$ directions. $\psi(z)$ is the shape function and is defined as

For CLPT: $\psi(z)=0$,
For FSDT: $\psi(z)=z$,
For HSDT: $\psi(z)=z-\frac{4z^3}{3h^2}$.

## 3 Free vibration analysis of nanocomposite plates

### 3.1 Constitutive equations

Euler-Lagrange and stress-displacement relations for different plate theories are

for CLPT:

$$
\varepsilon_{x x}=\frac{\partial u_{1}}{\partial x}=-z \frac{\partial^{2} w}{\partial x^{2}} \rightarrow \sigma_{x x}=\frac{-z E_{11}}{1-\nu_{12} \nu_{21}} \frac{\partial^{2} w}{\partial x^{2}}-\frac{z \nu_{12} E_{22}}{1-\nu_{12} \nu_{21}} \frac{\partial^{2} w}{\partial y^{2}},
\tag{2a}
$$

$$
\varepsilon_{y y}=\frac{\partial u_{2}}{\partial y}=-z \frac{\partial^{2} w}{\partial y^{2}} \rightarrow \sigma_{y y}=\frac{-z E_{22}}{1-\nu_{12} \nu_{21}} \frac{\partial^{2} w}{\partial y^{2}}-\frac{z \nu_{21} E_{11}}{1-\nu_{12} \nu_{21}} \frac{\partial^{2} w}{\partial x^{2}},
\tag{2b}
$$

$$
\gamma_{x y}=\frac{\partial u_{1}}{\partial y}+\frac{\partial u_{2}}{\partial x}=-2 z \frac{\partial^{2} w}{\partial x \partial y} \rightarrow \sigma_{x y}=-z \frac{E_{11}}{1-\nu_{21}} \frac{\partial^{2} w}{\partial x \partial y},
\tag{2c}
$$

$$
\gamma_{x z}=\frac{\partial u_{1}}{\partial z}+\frac{\partial u_{3}}{\partial x}=0 \rightarrow \sigma_{x z}=0,
\tag{2d}
$$

$$
\gamma_{y z}=\frac{\partial u_{2}}{\partial z}+\frac{\partial u_{3}}{\partial y}=0 \rightarrow \sigma_{y z}=0,
\tag{2e}
$$

$$
\frac{\partial^{2} M_{x x}}{\partial x^{2}}+\frac{\partial^{2} M_{y y}}{\partial y^{2}}+2 \frac{\partial^{2} M_{x y}}{\partial x \partial y}=\rho h \frac{\partial^{2} w}{\partial t^{2}},
\tag{3}
$$

where $\rho$ is the mass density and $M=\left\{M_{x x}, M_{y y}, M_{x y}\right\}^{T}=\int_{-h / 2}^{h / 2} z\left\{\sigma_{x x}, \sigma_{y y}, \sigma_{x y}\right\}^{T} \mathrm{d} z ;$

for FSDT:

$$
\varepsilon_{x x}=\frac{\partial u_{1}}{\partial x}=z \frac{\partial \varphi_{x}}{\partial x} \rightarrow \sigma_{x x}=\frac{z E_{11}}{1-\nu_{12} \nu_{21}} \frac{\partial \varphi_{x}}{\partial x}+\frac{z \nu_{12} E_{22}}{1-\nu_{12} \nu_{21}} \frac{\partial \varphi_{y}}{\partial y},
\tag{4a}
$$

$$
\varepsilon_{y y}=\frac{\partial u_{2}}{\partial y}=z \frac{\partial \varphi_{y}}{\partial y} \rightarrow \sigma_{y y}=\frac{z E_{22}}{1-\nu_{12} \nu_{21}} \frac{\partial \varphi_{y}}{\partial y}+\frac{z \nu_{21} E_{11}}{1-\nu_{12} \nu_{21}} \frac{\partial \varphi_{x}}{\partial x},
\tag{4b}
$$

$$
\gamma_{x y}=\frac{\partial u_{1}}{\partial y}+\frac{\partial u_{2}}{\partial x}=z\left(\frac{\partial \varphi_{x}}{\partial y}+\frac{\partial \varphi_{y}}{\partial x}\right) \rightarrow \sigma_{x y}=z \frac{E_{11}}{1+\nu_{21}}\left(\frac{\partial \varphi_{x}}{\partial y}+\frac{\partial \varphi_{y}}{\partial x}\right),
\tag{4c}
$$

$$
\gamma_{x z}=\frac{\partial u_{1}}{\partial z}+\frac{\partial u_{3}}{\partial x}=\frac{\partial w}{\partial x}+\varphi_{x} \rightarrow \sigma_{x z}=G_{12}\left(\frac{\partial w}{\partial x}+\varphi_{x}\right),
\tag{4d}
$$

$$
\gamma_{y z}=\frac{\partial u_{2}}{\partial z}+\frac{\partial u_{3}}{\partial x}=\frac{\partial w}{\partial y}+\varphi_{y} \rightarrow \sigma_{y z}=G_{12}\left(\frac{\partial w}{\partial y}+\varphi_{y}\right),
\tag{4e}
$$

$$
\frac{\partial Q_{x x}}{\partial x}+\frac{\partial Q_{y y}}{\partial y}=\rho h \frac{\partial^{2} w}{\partial t^{2}},
\tag{5a}
$$

$$
\frac{\partial M_{x x}}{\partial x}+\frac{\partial M_{x y}}{\partial y}-Q_{x x}=\rho h^{3} \frac{\partial^{2} \varphi_{x}}{\partial t^{2}},
\tag{5b}
$$

$$
\frac{\partial M_{y y}}{\partial y}+\frac{\partial M_{x y}}{\partial x}-Q_{y y}=\rho h^{3} \frac{\partial^{2} \varphi_{y}}{\partial t^{2}},
\tag{5c}
$$

where $Q=\left\{Q_{x x}, Q_{y y}\right\}^{T}=\int_{-h / 2}^{h / 2}\left\{\sigma_{x z}, \sigma_{y z}\right\}^{T} \mathrm{d} z ;$

for HSDT:

$$
\varepsilon_{x x}=\frac{\partial u_{1}}{\partial x}=z \frac{\partial \varphi_{x}}{\partial x}-\frac{4 z^{3}}{3 h^{2}}\left(\frac{\partial \varphi_{x}}{\partial x}+\frac{\partial^{2} w}{\partial x^{2}}\right) \rightarrow \sigma_{x x}=\frac{z E_{11}}{1-\nu_{12} \nu_{21}} \frac{\partial \varphi_{x}}{\partial x}-\frac{4 z^{3} E_{11}}{3 h^{2}\left(1-\nu_{12} \nu_{21}\right)}\left(\frac{\partial \varphi_{x}}{\partial x}+\frac{\partial^{2} w}{\partial x^{2}}\right), \tag{6a}
$$

$$
\varepsilon_{y y}=\frac{\partial u_{2}}{\partial y}=z \frac{\partial \varphi_{y}}{\partial y}-\frac{4 z^{3}}{3 h^{2}}\left(\frac{\partial \varphi_{y}}{\partial y}+\frac{\partial^{2} w}{\partial y^{2}}\right) \rightarrow \sigma_{y y}=\frac{z E_{22}}{1-\nu_{12} \nu_{21}} \frac{\partial \varphi_{y}}{\partial y}-\frac{4 z^{3} E_{22}}{3 h^{2}\left(1-\nu_{12} \nu_{21}\right)}\left(\frac{\partial \varphi_{y}}{\partial y}+\frac{\partial^{2} w}{\partial y^{2}}\right), \tag{6b}
$$

$$
\begin{aligned}
\gamma_{x y} &=\frac{\partial u_{1}}{\partial y}+\frac{\partial u_{2}}{\partial x}=z\left(\frac{\partial \varphi_{x}}{\partial y}+\frac{\partial \varphi_{y}}{\partial x}\right)-\frac{4 z^{3}}{3 h^{2}}\left(\frac{\partial \varphi_{x}}{\partial y}+\frac{\partial \varphi_{y}}{\partial x}+2 \frac{\partial^{2} w}{\partial x \partial y}\right) \rightarrow \sigma_{x y} \\
&=z \frac{E_{11}}{1+\nu_{21}}\left(\frac{\partial \varphi_{x}}{\partial y}+\frac{\partial \varphi_{y}}{\partial x}\right)-\frac{4 z^{3}}{3 h^{2}} \frac{E_{11}}{1+\nu_{21}}\left(\frac{\partial \varphi_{x}}{\partial y}+\frac{\partial \varphi_{y}}{\partial x}+2 \frac{\partial^{2} w}{\partial x \partial y}\right),
\end{aligned} \tag{6c}
$$

$$
\gamma_{x z}=\frac{\partial u_{1}}{\partial z}+\frac{\partial u_{3}}{\partial x}=\left(1-\frac{4 z^{2}}{h^{2}}\right)\left(\varphi_{x}+\frac{\partial w}{\partial x}\right) \rightarrow \sigma_{x z}=G_{12}\left(1-\frac{4 z^{2}}{h^{2}}\right)\left(\varphi_{x}+\frac{\partial w}{\partial x}\right), \tag{6d}
$$

$$
\gamma_{y z}=\frac{\partial u_{2}}{\partial z}+\frac{\partial u_{3}}{\partial y}=\left(1-\frac{4 z^{2}}{h^{2}}\right)\left(\varphi_{y}+\frac{\partial w}{\partial y}\right) \rightarrow \sigma_{y z}=G_{12}\left(1-\frac{4 z^{2}}{h^{2}}\right)\left(\varphi_{y}+\frac{\partial w}{\partial y}\right), \tag{6e}
$$

$$
\frac{\partial Q_{x x}}{\partial x}+\frac{\partial Q_{y y}}{\partial y}-\frac{4}{h^{2}}\left(\frac{\partial S_{x x}}{\partial x}+\frac{\partial S_{y y}}{\partial y}\right)+\frac{4}{3 h^{2}}\left(\frac{\partial^{2} R_{x x}}{\partial x^{2}}+\frac{\partial^{2} R_{y y}}{\partial y^{2}}+2 \frac{\partial^{2} R}{\partial x \partial y}\right)=\rho h \frac{\partial^{2} w}{\partial t^{2}}, \tag{7a}
$$

$$
\frac{\partial M_{x x}}{\partial x}+\frac{\partial M_{x y}}{\partial y}-\frac{4}{3 h^{2}}\left(\frac{\partial R_{x x}}{\partial x}+\frac{\partial R_{x y}}{\partial y}\right)-Q_{x x}+\frac{4}{h^{2}} S_{x x}=\rho h^{3} \frac{\partial^{2} \varphi_{x}}{\partial t^{2}}, \tag{7b}
$$

$$
\frac{\partial M_{y y}}{\partial y}+\frac{\partial M_{x y}}{\partial x}-\frac{4}{3 h^{2}}\left(\frac{\partial R_{y y}}{\partial y}+\frac{\partial R_{x y}}{\partial x}\right)-Q_{y y}+\frac{4}{h^{2}} S_{y y}=\rho h^{3} \frac{\partial^{2} \varphi_{y}}{\partial t^{2}}, \tag{7c}
$$

where

$$
R=\left\{R_{x x}, R_{y y}, R_{x y}\right\}^{T}=\int_{-h / 2}^{h / 2} z^{3}\left\{\sigma_{x x}, \sigma_{y y}, \sigma_{x y}\right\}^{T} \mathrm{~d} z \quad \text { and } \quad S=\left\{S_{x x}, S_{y y}\right\}^{T}=\int_{-h / 2}^{h / 2} z^{2}\left\{\sigma_{x z}, \sigma_{y z}\right\}^{T} \mathrm{~d} z.
$$

The substitution of stress-displacement relations in the corresponding Euler-Lagrange equations gives the constitutive equations for each plate theory as follows.

For CLPT:

$$
-\frac{E_{11} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{4} w}{\partial x^{4}}-\frac{E_{22} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{4} w}{\partial y^{4}}+\frac{\nu_{21} E_{11} h^{3}}{6\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{4} w}{\partial x^{2} \partial y^{2}}-\frac{E_{11} h^{3}}{6\left(1+\nu_{21}\right)} \frac{\partial^{4} w}{\partial x^{2} \partial y^{2}}=\rho h \frac{\partial^{2} w}{\partial t^{2}} ; \tag{8}
$$

for FSDT:

$$
\kappa G_{12} h\left(\frac{\partial \varphi_{x}}{\partial x}+\frac{\partial \varphi_{y}}{\partial y}+\frac{\partial^{2} w}{\partial x^{2}}+\frac{\partial^{2} w}{\partial y^{2}}\right)=\rho h \frac{\partial^{2} w}{\partial t^{2}}, \tag{9a}
$$

$$
\frac{E_{11} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{x}}{\partial x^{2}}+\frac{\nu_{12} E_{22} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{y}}{\partial x \partial y}+\frac{E_{11} h^{3}}{24\left(1+\nu_{21}\right)}\left(\frac{\partial^{2} \varphi_{x}}{\partial x \partial y}+\frac{\partial^{2} \varphi_{y}}{\partial y^{2}}\right)-\kappa_{12} h\left(\varphi_{x}+\frac{\partial w}{\partial x}\right)=\rho h^{3} \frac{\partial^{2} \varphi_{x}}{\partial t^{2}}, \tag{9b}
$$

$$
\frac{E_{22} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{y}}{\partial y^{2}}+\frac{\nu_{21} E_{11} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{x}}{\partial x \partial y}+\frac{E_{11} h^{3}}{24\left(1+\nu_{21}\right)}\left(\frac{\partial^{2} \varphi_{x}}{\partial x^{2}}+\frac{\partial^{2} \varphi_{y}}{\partial x \partial y}\right)-\kappa G_{12} h\left(\varphi_{y}+\frac{\partial w}{\partial y}\right)=\rho h^{3} \frac{\partial^{2} \varphi_{y}}{\partial t^{2}} ; \tag{9c}
$$

for HSDT:

$$
\begin{aligned}
& \frac{8 G_{12} h}{15}\left(\frac{\partial \varphi_{x}}{\partial x}+\frac{\partial \varphi_{y}}{\partial y}+\frac{\partial^{2} w}{\partial x^{2}}+\frac{\partial^{2} w}{\partial y^{2}}\right)+\frac{4 E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)}\left(\frac{\partial^{3} \varphi_{x}}{\partial x^{3}}+\frac{\partial^{3} \varphi_{y}}{\partial y^{3}}\right) \\
& +\frac{4 \nu_{12} E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)}\left(\frac{\partial^{3} \varphi_{x}}{\partial x \partial y^{2}}+\frac{\partial^{3} \varphi_{y}}{\partial x^{2} \partial y}\right)-\frac{4 E_{11} h^{3}}{252\left(1-\nu_{12} \nu_{21}\right)}\left(\frac{\partial^{4} w}{\partial x^{4}}+\frac{\partial^{4} w}{\partial y^{4}}\right)-\frac{4 \nu_{12} E_{22} h^{3}}{126\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{4} w}{\partial x^{2} \partial y^{2}} \\
& +\frac{4 E_{11} h^{3}}{315\left(1+\nu_{21}\right)}\left(\frac{\partial^{3} \varphi_{x}}{\partial x^{2} \partial y}+\frac{\partial^{3} \varphi_{y}}{\partial x \partial y^{2}}\right)-\frac{E_{11} h^{3}}{126\left(1+\nu_{21}\right)} \frac{\partial^{4} w}{\partial x^{2} \partial y^{2}}=\rho h \frac{\partial^{2} w}{\partial t^{2}},
\end{aligned}
\tag{10a}
$$

$$
\begin{aligned}
& \frac{17 E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{x}}{\partial x^{2}}-\frac{4 E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{3} w}{\partial x^{3}}+\frac{17 \nu_{12} E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{y}}{\partial x \partial y}-\frac{4 \nu_{12} E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{3} w}{\partial x \partial y^{2}} \\
& -\frac{4 E_{11} h^{3}}{315\left(1+\nu_{12}\right)} \frac{\partial^{3} w}{\partial x \partial y^{2}}+\frac{17 E_{11} h^{3}}{630\left(1+\nu_{12}\right)}\left(\frac{\partial^{2} \varphi_{x}}{\partial x \partial y}+\frac{\partial^{2} \varphi_{y}}{\partial y^{2}}\right)-\frac{8 G_{12} h}{15}\left(\varphi_{x}+\frac{\partial w}{\partial x}\right)=\rho h^{3} \frac{\partial^{2} \varphi_{x}}{\partial t^{2}},
\end{aligned}
\tag{10b}
$$

$$
\begin{aligned}
& \frac{17 E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{y}}{\partial y^{2}}-\frac{4 E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{3} w}{\partial y^{3}}+\frac{17 \nu_{21} E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{2} \varphi_{x}}{\partial x \partial y}-\frac{4 \nu_{21} E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \frac{\partial^{3} w}{\partial x^{2} \partial y} \\
& -\frac{4 E_{11} h^{3}}{315\left(1+\nu_{12}\right)} \frac{\partial^{3} w}{\partial x^{2} \partial y}+\frac{17 E_{11} h^{3}}{630\left(1+\nu_{12}\right)}\left(\frac{\partial^{2} \varphi_{x}}{\partial x^{2}}+\frac{\partial^{2} \varphi_{y}}{\partial x \partial y}\right)-\frac{8 G_{12} h}{15}\left(\varphi_{y}+\frac{\partial w}{\partial y}\right)=\rho h^{3} \frac{\partial^{2} \varphi_{y}}{\partial t^{2}}.
\end{aligned}
\tag{10c}
$$

### 3.2 Generalized differential quadrature (GDQ) method

The nonlinear form of eqs. (8)-(10) shows that there are nonlinear vibration. There is no exact analytical solution method for such differential equations and the use of series as an approximate solution is a suitable solution. GDQ among the most efficient numerical techniques in solving different boundary value problems. Several researchers have recently used GDQ to analyze nanostructures [58-62]. This method showed excellent efficiency, accuracy, and conve- nience and was very effective in solving complicated partial differential problems. Assume $\frac{\partial^{r} f}{\partial x^{r}}$ to be the $r$-th derivative of function $f(x)$ which can be expressed as a linear sum of function values:

$$
\left.\frac{\partial^{r} f(x)}{\partial x^{r}}\right|_{x=x_{P}}=\sum_{Q=1}^{n} A_{P Q}^{(r)} f\left(x_{P}\right),
\tag{11}
$$

where $n$ is the total number discrete grid points employed in the approximation and $A_{P Q}^{(r)}$ is coefficient of weighting.
The weighting coefficients of the first derivative can be obtained by

$$
A_{P Q}^{(1)}=\frac{M\left(x_{P}\right)}{\left(x_{P}-x_{Q}\right) M\left(x_{Q}\right)} \quad(P, Q=1,2, \ldots, n ; P \neq Q),
\tag{12}
$$

where

$$
M\left(x_{P}\right)=\prod_{Q=1 ; Q \neq P}^{n}\left(x_{P}-x_{Q}\right).
\tag{13}
$$

The weighting coefficients of higher-order derivatives are achieved by the recurrence relation presented below:

$$
A_{P Q}^{(r)}=
\begin{cases}
r\left[A_{P Q}^{(r-1)} A_{P Q}^{(1)}-\frac{A_{P Q}^{(r-1)}}{x_{p}-x_{q}}\right], & P \neq Q, \\
-\sum_{Q=1}^{n} A_{P Q}^{(r)}, & P=Q, \quad(P, Q=1,2, \ldots, n ; 2 \leq r \leq n-1).
\end{cases}
\tag{14}
$$

### 3.3 Implementation of the GDQ method in constitutive equations

According to GDQ, individual counterparts of constitutive differential equations for each plate theory at $r$-th point can be given as

for CLPT:
$$
\begin{aligned}
& -\frac{E_{11} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} A_{p k}^{(4)} W_{k q}-\frac{E_{22} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \sum_{m=1}^{N_{y}} B_{q m}^{(4)} W_{p m}-\frac{E_{11} h^{3}}{6\left(1+\nu_{21}\right)} \\
& +\frac{\nu_{21} E_{11} h^{3}}{6\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(2)} W_{k m}-\frac{E_{11} h^{3}}{6\left(1+\nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(2)} W_{k m}=-\rho h \omega^{2} W_{p q} ;
\end{aligned}
\tag{15}
$$

for FSDT:
$$
\kappa G_{12} h\left(\sum_{k=1}^{N_{x}} A_{p k}^{(1)} \phi_{x k q}+\sum_{m=1}^{N_{y}} B_{q m}^{(1)} \phi_{y p m}+\sum_{k=1}^{N_{x}} A_{p k}^{(2)} W_{k q}+\sum_{m=1}^{N_{y}} B_{q m}^{(2)} W_{p m}\right)=-\rho h \omega^{2} W_{p q},
\tag{16a}
$$

$$
\begin{aligned}
& \frac{E_{11} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} A_{p k}^{(2)} \phi_{x k q}+\frac{\nu_{12} E_{22} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{y p m} \\
& +\frac{E_{11} h^{3}}{24\left(1+\nu_{21}\right)}\left(\sum_{m=1}^{N_{y}} B_{q m}^{(2)} \phi_{y p m}+\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{x p m}\right)-\kappa G_{12} h\left(\phi_{x p q}+\sum_{k=1}^{N_{x}} A_{p k}^{(1)} W_{k q}\right)=-\rho h^{3} \omega^{2} \phi_{x p q},
\end{aligned}
\tag{16b}
$$

$$
\begin{aligned}
& \frac{E_{22} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \sum_{m=1}^{N_{y}} B_{q m}^{(2)} \phi_{y p m}+\frac{\nu_{21} E_{11} h^{3}}{12\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{x p m} \\
& +\frac{E_{11} h^{3}}{24\left(1+\nu_{21}\right)}\left(\sum_{k=1}^{N_{x}} A_{p k}^{(2)} \phi_{x k q}+\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{y p m}\right)-\kappa G_{12} h\left(\phi_{y p q}+\sum_{m=1}^{N_{y}} B_{q m}^{(1)} W_{p m}\right)=-\rho h^{3} \omega^{2} \phi_{y p q} ;
\end{aligned}
\tag{16c}
$$

for HSDT:
$$
\begin{aligned}
& \frac{8 G_{12} h}{15}\left(\sum_{k=1}^{N_{x}} A_{p k}^{(1)} \phi_{x k q}+\sum_{m=1}^{N_{y}} B_{q m}^{(1)} \phi_{y p m}+\sum_{k=1}^{N_{x}} A_{p k}^{(2)} W_{k q}+\sum_{m=1}^{N_{y}} B_{q m}^{(2)} W_{p m}\right) \\
& +\frac{4 E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)}\left(\sum_{k=1}^{N_{x}} A_{p k}^{(3)} \phi_{x k q}+\sum_{m=1}^{N_{y}} B_{q m}^{(3)} \phi_{y p m}\right) \\
& +\frac{4 \nu_{12} E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)}\left(\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(2)} \phi_{x p m}+\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(1)} \phi_{y p m}\right) \\
& -\frac{4 E_{11} h^{3}}{252\left(1-\nu_{12} \nu_{21}\right)}\left(\sum_{k=1}^{N_{x}} A_{p k}^{(4)} W_{k q}+\sum_{m=1}^{N_{y}} B_{q m}^{(4)} W_{p m}\right)-\frac{4 \nu_{12} E_{22} h^{3}}{126\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(2)} W_{k m} \\
& +\frac{4 E_{11} h^{3}}{315\left(1+\nu_{21}\right)}\left(\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(1)} \phi_{x p m}+\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(2)} \phi_{y p m}\right) \\
& -\frac{E_{11} h^{3}}{126\left(1+\nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(2)} W_{k m}=-\rho h^{3} \omega^{2} W_{p q},
\end{aligned}
\tag{17a}
$$

$$
\begin{aligned}
& \frac{17 E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} A_{p k}^{(2)} \phi_{x k q}-\frac{4 E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} A_{p k}^{(3)} W_{k q} \\
& +\frac{17 \nu_{12} E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{y p m}-\frac{4 \nu_{12} E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(2)} W_{k m} \\
& -\frac{4 E_{11} h^{3}}{315\left(1+\nu_{12}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(2)} W_{k m}+\frac{17 E_{11} h^{3}}{630\left(1+\nu_{12}\right)}\left(\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{x p m}+\sum_{m=1}^{N_{y}} B_{q m}^{(2)} \phi_{y p m}\right) \\
& -\frac{8 G_{12} h}{15}\left(\phi_{x p q}+\sum_{k=1}^{N_{x}} A_{p k}^{(1)} W_{k q}\right)=-\rho h^{3} \omega^{2} \phi_{x p q},
\end{aligned}
\tag{17b}
$$

$$
\begin{aligned}
& \frac{17 E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{m=1}^{N_{y}} B_{q m}^{(2)} \phi_{y p m}-\frac{4 E_{22} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{m=1}^{N_{y}} B_{q m}^{(3)} W_{p m}+\frac{17 \nu_{21} E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{x p m} \\
& -\frac{4 \nu_{21} E_{11} h^{3}}{315\left(1-\nu_{12} \nu_{21}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(1)} W_{k m}-\frac{4 E_{11} h^{3}}{315\left(1+\nu_{12}\right)} \sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(2)} B_{q m}^{(1)} W_{k m} \\
& +\frac{17 E_{11} h^{3}}{630\left(1+\nu_{12}\right)}\left(\sum_{k=1}^{N_{x}} A_{p k}^{(2)} \phi_{x k q}+\sum_{k=1}^{N_{x}} \sum_{m=1}^{N_{y}} A_{p k}^{(1)} B_{q m}^{(1)} \phi_{y p m}\right)-\frac{8 G_{12} h}{15}\left(\phi_{y p q}+\sum_{m=1}^{N_{y}} B_{q m}^{(1)} W_{p m}\right)=-\rho h^{3} \omega^{2} \phi_{y p q}.
\end{aligned}
\tag{17c}
$$

### 3.4 Implementation of GDQ method in boundary conditions

Applying the GDQ approximation gives discretized counterparts of different boundary conditions for each theory as for CLPT:

all edges simply supported (SSSS):

$$
W_{p q}=0, \quad \sum_{k=1}^{N_{x}} A_{p k}^{(2)} W_{k q}=0, \quad \text { at edges } x=0, L,
$$

$$
W_{p q}=0, \quad \sum_{m=1}^{N_{y}} B_{q m}^{(2)} W_{p m}=0, \quad \text { at edges } y=0, L ;
$$

all edges clamped (CCCC):

$$
W_{p q}=0, \quad \sum_{k=1}^{N_{x}} A_{p k}^{(1)} W_{k q}=0, \quad \text { at edges } x=0, L,
$$

$$
W_{p q}=0, \quad \sum_{m=1}^{N_{y}} B_{q m}^{(1)} W_{p m}=0, \quad \text { at edges } y=0, L ;
$$

for FSDT and HSDT:

all edges simply supported (SSSS):

$$
W_{p q}=0, \quad \sum_{k=1}^{N_{x}} A_{p k}^{(1)} \phi_{x k q}=0, \quad \text { at edges } x=0, L,
$$

$$
W_{p q}=0, \quad \sum_{m=1}^{N_{y}} B_{q m}^{(1)} \phi_{y p m}=0, \quad \text { at edges } y=0, L ;
$$

all edges clamped (CCCC):

$$
W_{p q}=0, \quad \phi_{x p q}=0, \quad \text { at edges } x=0, L,
$$

$$
W_{p q}=0, \quad \phi_{y p q}=0, \quad \text { at edges } y=0, L.
$$

## 4 Finite-element modeling

### 4.1 CNTs modeling

According to the limitations, continuous media are used and CNTs are simulated in lattice form. CNTs can be assumed as rolled graphene sheets [64-71]. Therefore, coordination of carbon atoms are obtained by mapping of carbon atom coordinates in graphene sheet using eq. (18):

$$
(X, Y, Z)=\left[R \cos \left(\frac{x}{R}\right), R \cos \left(\frac{x}{R}\right), y\right],\tag{18}
$$

where $X$, $Y$ and $Z$ are the coordinates of carbon atoms in the structure of CNTs which are obtained from the input of the coordinate of carbon atoms in the structure of graphene $(x, y)$ by mapping 2. The carbon atom coordinates were input into ANSYS software as the coordinates of the nodes of finite element model. Then, by using Beam188 elements, carbon-carbon bonds were created. The created elements had degrees of freedom namely the capacity of tolerating tensile, pressure, rotating and bending loads with no limitations for great stress and deformation and follow Timoshenko's beam element.

Short reinforcer volume elements with armchair and zigzag CNTs of (10,10) and (10,0), respectively, were used with the CNTs wall thickness (the distance between two graphene sheets) and diameter of 0.34 and 1.356 nm, respectively, with different aspect rations. In order to decrease numerical and geometrical (tension concentration) errors, relatively higher aspect rations were used.

The cross-section of nanotubes can be obtained according to eq. (19):

$$
A=\pi ×\left[\left(R+\frac{t}{2}\right)^{2}-\left(R-\frac{t}{2}\right)^{2}\right],\tag{19}
$$

where $t$ and $R$ are the wall thickness and radius of CNTs.

### 4.2 Matrix modeling

In this research, for the modeling of matrix, 3D element of Solid 186 was used which was consisted of 20 nodes on the element and 3 degrees of freedom on each node. Also, $\frac{1}{4}$ representative volume element (RVE) in ANSYS software was used and symmetric boundary conditions were applied on symmetric surfaces.

### 4.3 Interphase between matrix and CNTs

Generally, four different methods have been employed by researchers to define the mechanism and size of the forces exchanged between CNTs and matrix polymer: first, we can assumed no chemical bonding between CNTs and matrix polymer for which van der Waals forces are the solution. Lordi *et al.* [64] suggested a coil-shaped cover around the CNT for the addition of sucrose between CNTs and matrix for total non-binding which has been done experimentally. In the second method it has been assumed that there is strong bonding. In this method, it has been assumed C-C covalent bonds between polymer and nanotube which increases surface resistance significantly [65]. In the third method, the re- searchers assumed that there is a cross-link between polymer and nanotube. In this method, a small portion of covalent bonds consisted of multi-task amines which played the role of a mediator between nanotubes and polymer. However chemical bonds can be created due to the functionalization with the change of structure of the graphene layers of the nanotube [66]. In the fourth method, load transfer may be assigned to the mechanical continuity of nanotube and poly- mer due to geometrical rotation created in the nanotube although the carbon atoms of the CNT wall are chemically stable due to the structure of CNTs. So, the CNTs-based reinforcer exerts its effect on the matrix by van der Waals forces [67]. In this research, the fourth method was used for the modeling of intermediate phase. To describe inter-atom relations in the investigation of van der Waals bonds between the atoms of nanotube and composite resin, quantum me- chanics was used. Hence, only slow movements (slower than thermal vibration) in atoms, molecules, and ions were stud- ied and the internal electronic structure was neglected. Molecules and atoms exert internal forces to each other which can be presented by instant potential energy values for the whole system. Analytical solutions for the dynamic equa- tions of particles only work for a small group of questions and are limited to systems with few degrees of freedom [68].

To achieve certain distances called equilibrium lengths or bond lengths, attraction forces in atom nuclei or ions are balanced with electronic cloud repulsion forces and the desired distance is obtained. But the excessive reduction of atomic distance results in the rapid growth of the total repulsion force. The most common model for describing the attraction/repulsion of neutral atoms and molecules according to the location of atoms is the Lennard-Jones potential. The equation of force in terms of inter-atom distance is described by

$$
F(x)=-24 \frac{\varepsilon}{\sigma}\left[2\left(\frac{\sigma}{x+3.8}\right)^{13}-\left(\frac{\sigma}{x+3.8}\right)^{7}\right],\tag{20}
$$

![](./images/812763073549959169_1.jpg)

Fig. 1. Variation of Lennard-Jones van der Waals forces in terms of inter-atomic distance.

![](./images/812763073549959169_2.jpg)

Fig. 2. A part of the finite-element model by having matrix, interphase, and CNTs.

![](./images/812763073549959169_3.jpg)

Fig. 3. Interphase spring element.

where $X$ is the inter-atom distance and $\sigma$ and $\varepsilon$ are van der Waals parameters which are $\sigma_{LJ}=0.3825\,\text{nm}$ and $\varepsilon_{LJ}=0.4492\,Kj/\text{mol}$ for the $-\text{CH}_2-$ connection of nanotube and polymer; for rotation, these values are $\sigma_{LJ}=0.428\,\text{nm}$ and $\varepsilon_{LJ}=0.4742\,Kj/\text{mol}$ [64,67]. Figure 1 shows Lennard-Jones van der Waals forces in terms of inter-atomic distance [69,70].

In this research, to investigate the nonlinear behavior of the intermediate phase, the combin 39 element was used which is a nonlinear spring element. To input the characteristics to this element, eq. (20) was used. Figure 2 shows the finite-element model used in this research and fig. 3 shows interphase spring element used in this research.

Table 1. FEM results of elastic modulus of CNTs-reinforced composites.

<table>
<thead>
<tr>
<th rowspan="2">Carbon nanotube volume fraction</th>
<th colspan="2">Short-carbon nanotube composite</th>
<th colspan="2">Long-carbon nanotube composite</th>
</tr>
<tr>
<th>Longitudinal Modulus (GPa)</th>
<th>Transverse Modulus (GPa)</th>
<th>Longitudinal Modulus (GPa)</th>
<th>Transverse Modulus (GPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0%</td>
<td>3.12</td>
<td>3.12</td>
<td>3.12</td>
<td>3.22</td>
</tr>
<tr>
<td>5%</td>
<td>3.72</td>
<td>3.35</td>
<td>67.79</td>
<td>3.83</td>
</tr>
<tr>
<td>10%</td>
<td>5.46</td>
<td>4.33</td>
<td>101.02</td>
<td>5.09</td>
</tr>
<tr>
<td>15%</td>
<td>8.29</td>
<td>6.28</td>
<td>145.55</td>
<td>7.28</td>
</tr>
</tbody>
</table>

Table 2. Optimum values of CNTs efficiency parameters.

<table>
<thead>
<tr>
<th>Carbon nanotube volume fraction</th>
<th>$\vartheta_1$</th>
<th>$\vartheta_2$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Short-carbon nanotube reinforcement</td>
</tr>
<tr>
<td>5%</td>
<td>0.0253</td>
<td>1.0354</td>
</tr>
<tr>
<td>10%</td>
<td>0.0444</td>
<td>1.2853</td>
</tr>
<tr>
<td>15%</td>
<td>0.0627</td>
<td>1.7799</td>
</tr>
<tr>
<td colspan="3">Long-carbon nanotube reinforcement</td>
</tr>
<tr>
<td>5%</td>
<td>2.1587</td>
<td>1.17767</td>
</tr>
<tr>
<td>10%</td>
<td>1.6346</td>
<td>1.4775</td>
</tr>
<tr>
<td>15%</td>
<td>1.6877</td>
<td>2.0590</td>
</tr>
</tbody>
</table>

## 5 Modified rule of mixture

In this work, we have assumed that CNTs-reinforced composites consisting of a mixture of polyethylene matrix and (10,10) armchair SWCNTs with isotropic behavior. CNTs-reinforced composites showed anisotropic properties [6, 55–57]. Based on the modified mixture rule, the effective values of the shear modulus and Young's modulus for CNTs-reinforced composites can be calculated by [57]

$$
E_{11}=\vartheta_{1} V_{C N T} E_{11}^{C N T}+V_{m} E^{m}, \tag{21a}
$$

$$
\frac{\vartheta_{2}}{E_{22}}=\frac{V_{C N T}}{E_{22}^{C N T}}+\frac{V_{m}}{E^{m}}, \tag{21b}
$$

$$
\frac{\vartheta_{3}}{G_{12}}=\frac{V_{C N T}}{G_{12}^{C N T}}+\frac{V_{m}}{G^{m}}, \tag{21c}
$$

where $E_{11}^{CNT}$, $E_{22}^{CNT}$, and $G_{12}^{CNT}$ are longitudinal Young's modulus, transverse Young's modulus, and shear modulus of CNTs, respectively. $G^m$ and $E^m$ are the shear modulus and Young's modulus of the isotropic matrix, respectively. $V_{CNT}$, and $V_m$ are the volume fractions of carbon nanotube and matrix, respectively:

$$
V_{C N T}+V_{m}=1. \tag{22}
$$

Coefficients $\vartheta_1$, $\vartheta_2$, and $\vartheta_3$ are CNTs efficiency parameters to consider scale effect of materials obtained from the results of FEM simulations.

## 6 Results and discussion

The values of the critical buckling load for the (10,10) CNTs-reinforced composite plate with different end supports for different plate theories and CNT volume fractions are presented in this section. Polyethylene was used as matrix material with $E^m=3.22$ GPa, $\nu_m=0.3$, $\rho_m=925$ kg/m³ at room temperature. For the (10,10) armchair SWCNTs as reinforcement, $E_{11}^{CNT}=600$ GPa, $E_{22}^{CNT}=10$ GPa, $G_{12}^{CNT}=5$ GPa, $\nu_{CNT}=0.19$, $\rho_{CNT}=2300$ kg/m³ were assumed [32,68,71].

Table 1 shows the FEM results for elastic modulus of CNTs-reinforced composites by matching the values calculated by the mixture rule. CNTs efficiency parameters were obtained and are summarized in table 2 for both short and long SWCNTs reinforcements with different CNTs volume fractions. It has to be kept in mind that for shear modulus,

Table 3. Fundamental frequency of nanocomposite plate reinforced by short-SWCNTs with simply supported edge supports ($10^3$ Hz).

<table>
  <thead>
    <tr>
      <th>Aspect ratio
($L/h$)</th>
      <th>Carbon nanotube
volume fraction</th>
      <th>CLPT</th>
      <th>FSDT</th>
      <th>HSDT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">10</td>
      <td>0%</td>
      <td>20.1274</td>
      <td>19.6703</td>
      <td>19.6706</td>
    </tr>
    <tr>
      <td>5%</td>
      <td>22.2861</td>
      <td>21.7800</td>
      <td>21.7803</td>
    </tr>
    <tr>
      <td>10%</td>
      <td>27.2774</td>
      <td>26.6579</td>
      <td>26.6583</td>
    </tr>
    <tr>
      <td>15%</td>
      <td>34.1539</td>
      <td>33.3782</td>
      <td>33.3787</td>
    </tr>
    <tr>
      <td rowspan="4">20</td>
      <td>0%</td>
      <td>5.0318</td>
      <td>5.0028</td>
      <td>5.0029</td>
    </tr>
    <tr>
      <td>5%</td>
      <td>5.5715</td>
      <td>5.5394</td>
      <td>5.5394</td>
    </tr>
    <tr>
      <td>10%</td>
      <td>6.8193</td>
      <td>6.7801</td>
      <td>6.7802</td>
    </tr>
    <tr>
      <td>15%</td>
      <td>8.5385</td>
      <td>8.4893</td>
      <td>8.4894</td>
    </tr>
    <tr>
      <td rowspan="4">40</td>
      <td>0%</td>
      <td>1.2580</td>
      <td>1.2557</td>
      <td>1.2557</td>
    </tr>
    <tr>
      <td>5%</td>
      <td>1.3929</td>
      <td>1.3904</td>
      <td>1.3904</td>
    </tr>
    <tr>
      <td>10%</td>
      <td>1.7048</td>
      <td>1.7017</td>
      <td>1.7017</td>
    </tr>
    <tr>
      <td>15%</td>
      <td>2.1346</td>
      <td>2.1307</td>
      <td>2.1307</td>
    </tr>
  </tbody>
</table>

Table 4. Fundamental frequency of nanocomposite plate reinforced by short-SWCNTs with clamped edge supports ($10^3$ Hz).

<table>
  <thead>
    <tr>
      <th>Aspect ratio
($L/h$)</th>
      <th>Carbon nanotube
volume fraction</th>
      <th>CLPT</th>
      <th>FSDT</th>
      <th>HSDT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">10</td>
      <td>0%</td>
      <td>80.5327</td>
      <td>78.7227</td>
      <td>78.7231</td>
    </tr>
    <tr>
      <td>5%</td>
      <td>89.1711</td>
      <td>87.1460</td>
      <td>87.1464</td>
    </tr>
    <tr>
      <td>10%</td>
      <td>109.1423</td>
      <td>106.6637</td>
      <td>106.6642</td>
    </tr>
    <tr>
      <td>15%</td>
      <td>136.6565</td>
      <td>133.5529</td>
      <td>133.5534</td>
    </tr>
    <tr>
      <td rowspan="4">20</td>
      <td>0%</td>
      <td>20.1317</td>
      <td>20.0158</td>
      <td>20.0160</td>
    </tr>
    <tr>
      <td>5%</td>
      <td>22.2911</td>
      <td>22.1637</td>
      <td>22.1639</td>
    </tr>
    <tr>
      <td>10%</td>
      <td>27.2833</td>
      <td>27.1261</td>
      <td>27.1264</td>
    </tr>
    <tr>
      <td>15%</td>
      <td>34.1617</td>
      <td>33.9649</td>
      <td>33.9652</td>
    </tr>
    <tr>
      <td rowspan="4">40</td>
      <td>0%</td>
      <td>5.0325</td>
      <td>5.0233</td>
      <td>5.0233</td>
    </tr>
    <tr>
      <td>5%</td>
      <td>5.5722</td>
      <td>5.5621</td>
      <td>5.5621</td>
    </tr>
    <tr>
      <td>10%</td>
      <td>6.8198</td>
      <td>6.8075</td>
      <td>6.8075</td>
    </tr>
    <tr>
      <td>15%</td>
      <td>8.5393</td>
      <td>8.5238</td>
      <td>8.5238</td>
    </tr>
  </tbody>
</table>

$\vartheta_3 = \vartheta_2$ was assumed. By comparing the transverse and longitudinal Young's modulus predicted by the rule of mixture and FEM simulation, it was witnessed that with correct selection of $\vartheta_1$ and $\vartheta_2$, the rule of mixture perfectly predicted the elastic properties of nanocomposites.

Fundamental frequency values of composite plates reinforced with short-(10,10) SWCNTs with the thickness of $h = 0.005$ m and different side lengths and CNTs volume fractions are summarized in tables 3 and 4 for simply supported and clamped boundary conditions, respectively. Tables 5 and 6 show similar results for composite plates reinforced with long-(10,10) SWCNTs. It was concluded that the stiffness of nanocomposite plate reinforced with long-SWCNTs was significantly higher than those reinforced with short-SWCNTs.

Also, it was witnessed that by introducing the effects of transverse shear strains in FSDT and HSDT plate theories, fundamental frequencies became smaller than those obtained from CLPT plate theory for all CNT volume fractions, especially plates with lower side lengths. In addition, the difference between fundamental frequencies predicted by FSDT and HSDT plate theories was relatively high corresponding to lower side lengths. The obtained results showed that increasing CNT volume fractions increased the fundamental frequency of composite plates reinforced with both long- and short-SWCNTs and increasing the aspect ratio for CNT decreased the fundamental frequency of composite plates. This process may be different from the experimental results due to the nanoparticle agglomeration.

Table 5. Fundamental frequency of nanocomposite plate reinforced with long-SWCNTs with simply supported edge supports ($10^3$ Hz).

<table>
<thead>
<tr>
<th>Aspect ratio
($L/h$)</th>
<th>Carbon nanotube
volume fraction</th>
<th>CLPT</th>
<th>FSDT</th>
<th>HSDT</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">10</td>
<td>0%</td>
<td>20.1274</td>
<td>19.6703</td>
<td>19.6706</td>
</tr>
<tr>
<td>5%</td>
<td>76.9098</td>
<td>75.1632</td>
<td>75.1639</td>
</tr>
<tr>
<td>10%</td>
<td>90.6146</td>
<td>88.5470</td>
<td>88.5481</td>
</tr>
<tr>
<td>15%</td>
<td>105.3049</td>
<td>102.9134</td>
<td>102.9146</td>
</tr>
<tr>
<td rowspan="4">20</td>
<td>0%</td>
<td>5.0318</td>
<td>5.0028</td>
<td>5.0029</td>
</tr>
<tr>
<td>5%</td>
<td>19.2275</td>
<td>19.1167</td>
<td>19.1169</td>
</tr>
<tr>
<td>10%</td>
<td>22.6512</td>
<td>22.5207</td>
<td>22.5209</td>
</tr>
<tr>
<td>15%</td>
<td>26.3262</td>
<td>26.2746</td>
<td>26.2748</td>
</tr>
<tr>
<td rowspan="4">40</td>
<td>0%</td>
<td>1.2580</td>
<td>1.2557</td>
<td>1.2557</td>
</tr>
<tr>
<td>5%</td>
<td>4.8069</td>
<td>4.7982</td>
<td>4.7982</td>
</tr>
<tr>
<td>10%</td>
<td>5.6628</td>
<td>5.6525</td>
<td>5.6525</td>
</tr>
<tr>
<td>15%</td>
<td>6.5816</td>
<td>6.5696</td>
<td>6.5696</td>
</tr>
</tbody>
</table>

Table 6. Fundamental frequency of nanocomposite plate reinforced with long-SWCNTs with clamped edge supports ($10^3$ Hz).

<table>
<thead>
<tr>
<th>Aspect ratio
($L/h$)</th>
<th>Carbon nanotube
volume fraction</th>
<th>CLPT</th>
<th>FSDT</th>
<th>HSDT</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">10</td>
<td>0%</td>
<td>80.5317</td>
<td>78.7027</td>
<td>78.7031</td>
</tr>
<tr>
<td>5%</td>
<td>307.7315</td>
<td>300.7428</td>
<td>300.7439</td>
</tr>
<tr>
<td>10%</td>
<td>362.5271</td>
<td>354.2941</td>
<td>354.2954</td>
</tr>
<tr>
<td>15%</td>
<td>421.3459</td>
<td>411.7770</td>
<td>411.7789</td>
</tr>
<tr>
<td rowspan="4">20</td>
<td>0%</td>
<td>20.1317</td>
<td>20.0158</td>
<td>20.0160</td>
</tr>
<tr>
<td>5%</td>
<td>76.9273</td>
<td>76.4841</td>
<td>76.4844</td>
</tr>
<tr>
<td>10%</td>
<td>90.6252</td>
<td>90.1032</td>
<td>90.1035</td>
</tr>
<tr>
<td>15%</td>
<td>105.3284</td>
<td>104.7217</td>
<td>104.7221</td>
</tr>
<tr>
<td rowspan="4">40</td>
<td>0%</td>
<td>5.0325</td>
<td>5.0233</td>
<td>5.0233</td>
</tr>
<tr>
<td>5%</td>
<td>19.2295</td>
<td>19.1947</td>
<td>19.1947</td>
</tr>
<tr>
<td>10%</td>
<td>22.6534</td>
<td>22.6224</td>
<td>22.6224</td>
</tr>
<tr>
<td>15%</td>
<td>26.32901</td>
<td>26.2813</td>
<td>26.2813</td>
</tr>
</tbody>
</table>

## 7 Conclusions

In this study, the free vibration behavior of composite plates reinforced with CNTs under different edge supports was evaluated. Both long- and short-SWCNTs reinforcements with different types of plate theories, including CLPT, FSDT and HSDT, were considered. The governing differential equations of simply supported and clamped boundary conditions were found using the generalized differential quadrature (GDQ) method. The rule of mixture along with GDQ method was applied to discretize differential equations to achieve fundamental frequencies of nanocomposite plates. To obtain the best values of CNTs efficiency parameters for the rule of mixture, elastic modulus for composites with both long- and short-SWCNTs reinforcements were investigated with FEM simulation and the obtained results were matched with those obtained from the rule of mixture. Different CNTs volume fractions gave different CNTs efficiency parameters. Moreover, it was witnessed that increasing CNTs volume fractions increased the stiffness of nanocomposite plate especially for long-SWCNT reinforcement.

Publisher's Note The EPJ Publishers remain neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## References

1. P.M. Ajayan, O. Stephan, C. Colliex, D. Trauth, Science **265**, 1212 (1994).
2. L.S. Schadler, S.C. Giannaris, P.M. Ajayan, Appl. Phys. Lett. **73**, 3842 (1998).
3. R. Haggenmueller, H.H. Gommans, A.G. Rinzler, J.E. Fischer, K.I. Winey, Chem. Phys. Lett. **330**, 219 (2000).
4. L. Jin, C. Bower, O. Zhou, Appl. Phys. Lett. **73**, 1197 (1998).
5. C. Bower, R. Rosen, L. Jin, J. Han, O. Zhou, Appl. Phys. Lett. **74**, 3317 (1999).
6. Z. Jia, Z. Wang, C. Xu, J. Liang, B. Wei, D. Wu, S. Zhu, Mater. Sci. Eng. A **271**, 395 (1999).
7. O. Lourie, H.D. Wagner, Appl. Phys. Lett. **73**, 3527 (1998).
8. Z. Huang, Z. Qin, F. Chu, J. Sandwich Struct. Mater. **18**, 531 (2016).
9. Z. Huang, Z. Qin, F. Chu, Compos. Struct. **153**, 96 (2016).
10. E. Hammel, X. Tang, M. Trampert, T. Schmitt, K. Mauthner, A. Eder, Carbon **42**, 1153 (2004).
11. K. Lau, Chem. Phys. Lett. **370**, 399 (2003).
12. S.J.V. Frankland, V.M. Harik, G.M. Odegard, D.W. Brenner, T.S. Gates, Compos. Sci. Technol. **63**, 1655 (2003).
13. A.M.K. Esawi, M.M. Farag, Mater. Des. **28**, 2394 (2007).
14. K.T. Lau, C. Gu, D. Hui, Composites B **37**, 425 (2006).
15. M.M. Shokrieh, R. Rafiee, Compos. Struct. **92**, 647 (2010).
16. S. Sahmani, A.M. Fattahi, J. Mol. Graph. Model. **75**, 20 (2017).
17. S. Sahmani, A.M. Fattahi, Comput. Methods Appl. Mech. Eng. **322**, 187 (2017).
18. A.M. Fattahi, S. Sahmani, Microsyst. Technol. **23**, 5121 (2017).
19. R. Moradi-Dastjerdi, G. Payganeh, M. Tajdari, Polym. Compos. **38**, E542 (2017).
20. R. Moradi-Dastjerdi, H. Momeni-Khabisi, Steel Compos. Struct. **22**, 277 (2016).
21. R. Moradi-Dastjerdi, H. Momeni-Khabisi, J. Vib. Control **24**, 2327 (2018).
22. Z. Qin, F. Chu, J. Zu, Int. J. Mech. Sci. **133**, 91 (2017).
23. Z. Qin, Z. Yang, J. Zu, F. Chu, Int. J. Mech. Sci. **142-143**, 127 (2018).
24. R. Moradi-Dastjerdi, H. Malek-Mohammadi, J. Sandwich Struct. Mater. **19**, 736 (2017).
25. R. Moradi-Dastjerdi, H. Malek-Mohammadi, H. Momeni-Khabisi, Z. Angew. Math. Mech. **97**, 1418 (2017).
26. J. Awrejcewicz, V.A. Krysko, A.A. Sopenko, M.V. Zhigalov, A.V. Kirichenko, A.V. Krysko, Chaos, Solitons Fractals **104**, 635 (2017).
27. J. Awrejcewicz, V.A. Krysko, M.V. Zhigalov, A.V. Krysko, Int. J. Solids Struct. **117**, 39 (2017).
28. V.F. Kirichenko, J. Awrejcewicz, A.V. Kirichenko, A.V. Krysko, V.A. Krysko, Int. J. Non-Linear Mech. **74**, 51 (2015).
29. V.A. Krysko, J. Awrejcewicz, M.V. Zhigalov, I.V. Papkova, T.V. Yakovleva, A.V. Krysko, Nonlinear Dyn. **92**, 2093 (2018).
30. Y. Tanaka, Int. J. Hydromechatron. 1, 350 (2018).
31. M.H. Jalali, O. Zargar, M. Baghani, Iran. J. Sci. Technol. Trans. Mech. Eng. (2018) https://doi.org/10.1007/s40997-018-0193-6.
32. A.M. Fattahi, B. Safaei, Microsyst. Technol. **23**, 5079 (2017).
33. A. Pasharavesh, Y.A. Vaghasloo, M.T. Ahmadian, R. Moheimani, *Nonlinear vibration analysis of nano to micron scale beams under electric force using nonlocal theory*, ASME Conf. Proc., DETC2011-47615 (ASME, 2011) pp. 145-151.
34. R. Moheimani, M. Hasansade, Proc. Inst. Mech. Eng. Part C **233**, 2909 (2019).
35. R. Moradi-Dastjerdi, G. Payganeh, Steel Compos. Struct. **24**, 359 (2017).
36. M. Mohammadsalehi, O. Zargar, M. Baghani, Meccanica **52**, 1063 (2017).
37. B. Safaei, A.M. Fattahi, Mechanika **23**, 678 (2017).
38. B. Safaei, P. Naseradinmousavi, A. Rahmani, J. Mol. Graph. Model. **65**, 43 (2016).
39. A.M. Fattahi, S. Sahmani, Arab. J. Sci. Eng. **42**, 4617 (2017).
40. P. Ghanati, B. Safaei, Indian J. Phys. **93**, 47 (2019).
41. S. Sahmani, A.M. Fattahi, Microsyst. Technol. **24**, 1265 (2018).
42. S. Azizi, B. Safaei, A.M. Fattahi, M. Tekere, Adv. Mater. Sci. Eng. **2015**, 318539 (2015).
43. S. Azizi, A.M. Fattahi, J.T. Kahnamouei, Comput. Theor. Nanosci. **12**, 4179 (2015).
44. B. Safaei, R. Moradi-Dastjerd, F. Chu, Compos. Struct. **192**, 28 (2018).
45. B. Safaei, R. Moradi-Dastjerdi, Z. Qin, F. Chu, Compos. Part B **161**, 44 (2019).
46. R. Moheimani, M.T. Ahmadian, *On Free Vibration of Functionally Graded Euler-Bernoulli Beam Models Based on the Non-Local Theory*, in *ASME 2012 International Mechanical Engineering Congress and Exposition*, Vol. **12**, *Vibration Acoustics and Wave Propagation* (ASME, 2012).
47. A.V. Krysko, J. Awrejcewicz, M.V. Zhigalov, V.A. Krysko, Nonlinear Dyn. **85**, 2729 (2016).
48. A.V. Krysko, J. Awrejcewicz, O.A. Saltykova, S.S. Vetsel, V.A. Krysko, Chaos, Solitons Fractals **91**, 622 (2016).
49. J. Awrejcewicz, V.A. Krysko, T.V. Yakovleva, V.A. Krysko, J. Sound Vib. **369**, 77 (2016).
50. B. Safaei, A.M. Fattahi, F. Chu, Microsyst. Technol. **24**, 2663 (2018).
51. A.M. Fattahi, M. Mondali, J. Mech. Sci. Technol. **27**, 3419 (2013).
52. A.M. Fattahi, M. Mondali, J. Theor. Appl. Mech. **52**, 3 (2014).
53. A.M. Fattahi, E. Moaddab, N. Bibishahrbaneoi, J. Mech. Sci. Technol. **29**, 2067 (2015).
54. E. Perpète, M. Laso, *Multiscale Modelling of Polymer Properties*, first edition (Woodhead Publishing, 2007).
55. J.M. Wernik, S.A. Meguid, Acta Mech. **217**, 1 (2010).
56. M.M. Shokrieh, R. Rafiee, Compos. Sci. **92**, 2415 (2010).

57. H.S. Shen, Compos. Struct. **91**, 9 (2009).

58. P. Malekzadeh, A.R. Fiouz, Compos. Struct. **80**, 196 (2007).

59. M.A. De Rosa, N.M. Auciello, M. Lippiello, Mech. Res. Commun. **35**, 187 (2008).

60. Y.J. Hu, Y.Y. Zhu, C.J. Cheng, Int. J. Solids Struct. **46**, 1667 (2009).

61. O. Sepahi, M.R. Forouzan, P. Malekzadeh, Compos. Struct. **92**, 2369 (2010).

62. S.C. Pradhan, T. Murmu, Physica E **42**, 1944 (2010).

63. V. Stetsyuk, J.C.C. Kiong, Int. J. Hydromechatron. **1**, 332 (2018).

64. V. Lordi, N. Yao, J. Mater. Res. **15**, 2770 (2011).

65. B. Fiedler, F.H. Gojny, M.H.G. Wichmann, M.C.M. Nolte, K. Schulte, Compos. Sci. Technol. **66**, 3115 (2006).

66. Y. Hu, O.A. Shenderova, Z. Hu, C.W. Padgett, D.W. Brenner, Rep. Prog. Phys. **69**, 1847 (2006).

67. W.K. Liu, E.G. Karpov, H.S. Park, *Nano Mechanics and Materials: Theory, Multiscale Methods and Application, Nano Mechanics and Materials* (Wiley, 2006) p. 334.

68. C.F. Cornwell, L.T. Wille, Solid State Commun. **101**, 555 (1997).

69. D. Qian, W.K. Liu, R.S. Ruoff, Compos. Sci. Technol. **63**, 1561 (2003).

70. A. Lashkari Zadeh, M. Shariati, H. Torabi, J. Phys. Chem. Solids **73**, 1282 (2012).

71. V.N. Popov, V.E. Van Doren, M. Balkanski, Solid State Commun. **114**, 395 (2000).