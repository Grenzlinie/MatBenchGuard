Article

# Dynamic Stability Analysis in Hybrid Nanocomposite Polymer Beams Reinforced by Carbon Fibers and Carbon Nanotubes

Behrooz Keshtegar $^{1,2}$ , Reza Kolahchi $^{3,*}$ , Arameh Eyvazian $^{4,*}$ and Nguyen-Thoi Trung $^{1,2}$

1 Division of Computational Mathematics and Engineering, Institute for Computational Science, Ton Duc Thang University, Ho Chi Minh City 800010, Vietnam; beh.keshtegar@tdtu.edu.vn (B.K.); nguyenthoitrung@tdtu.edu.vn (N.-T.T.)
2 Faculty of Civil Engineering, Ton Duc Thang University, Ho Chi Minh City 800010, Vietnam
3 Institute of Research and Development, Duy Tan University, Da Nang 550000, Vietnam
4 Mechanical and Industrial Engineering Department, College of Engineering, Qatar University, P.O. Box 2713 Doha, Qatar

* Correspondence: rezakolahchi@duytan.edu.vn (R.K.); eyvazian@qu.edu.qa (A.E.)

Abstract: The objective of this innovative research is assessment of dynamic stability for a hybrid nanocomposite polymer beam. The considered beam formed by multiphase nanocomposite, including polymer-carbon nanotubes (CNTs)-carbon fibers (CFs). Hence, as to compute the effective material characteristics related to multiphase nanocomposite layers, the Halpin-Tsai model, as well as micromechanics equations are employed. To model the structure realistically, exponential shear deformation beam theory (ESDBT) is applied and using energy methods, governing equations are achieved. Moreover, differential quadrature method (DQM) as well as Bolotin procedures are used for solving the obtained governing equations and the dynamic instability region (DIR) relative to the beam is determined. To extend this novel research, various parameters pinpointing the influences of CNT volume fraction, CFs volume percent, boundary edges as well as the structure's geometric variables on the dynamic behavior of the beam are presented. The results were validated with the theoretical and experimental results of other published papers. The outcomes reveal that increment of volume fraction of CNT is able to shift DIR to more amounts of frequency. Further, rise of carbon fibers volume percent leads to increase the excitation frequency of this structure.

Keywords: polymer beam; carbon fibers; carbon nanotubes; dynamic stability; exponential shear deformation beam theory

## 1. Introduction

When a structure is subjected to periodic and pulsatile loads, it is well known that the ordinary forced response will lead to dynamic instability. This subject is very important since the periodic loads may cause parametric vibrations, which may damage the structures. Nanocomposite plates can be used in different industries such as aircrafts and automobile which may be subjected to periodic and pulsatile loads. However, dynamic stability of nanocomposite plates is a novel topic which should be studied.

Different papers were brought into investigation regarding polymer nanocomposites (PNCs) special applications [1], device usages [2], its processing technologies for future usages [3-6] and safety analysis [7-9]. Pastoriza-Santos et al. [10] discussed the processes of manufacturing and different usages of plasmonic PNC ranging from light-harvesting improvement to tracing biologic as well as chemicals molecules. Leon et al. [11] brought up significant proficiency of PNC in terms of additive manufacturing usages. It is found that PNC are preferable due to their significant mechanical, chemical and thermal characteristics under harsh conditions. In the aspect of energy density, Liu et al. [12] analyzed dielectric PNC having multilayered structure. They claimed that the discharged energy density of this multilayered structure is the greatest discharged energy densities which were presented.

---

Citation: Keshtegar, B.; Kolahchi, R.; Eyvazian, A.; Trung, N.-T. Dynamic Stability Analysis in Hybrid Nanocomposite Polymer Beams Reinforced by Carbon Fibers and Carbon Nanotubes. Polymers 2021, 13, 106. https://doi.org/10.3390/polym13010106

Received: 19 April 2020
Accepted: 27 May 2020
Published: 29 December 2020

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812519659168333825_1.jpg)

Copyright: © 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

---

Polymers 2021, 13, 106. https://doi.org/10.3390/polym13010106
https://www.mdpi.com/journal/polymers

Nevertheless, there are limitations in the conduction of polymers that Abbasi et al. [13] discussed and offered some advices. It is believed that there are constraints related to electrically conductive polymers and considering carbon-based nanoparticles can push back them. Hence, this research reviewed some improvements in this field.

Further, it should be noticed that hybrid composites refer to specific substances made up of organic and inorganic ingredients and nanocomposite term, points at hybrid inorganic–organic composites having components in nano scale. These materials are utilized in formations of structures because of their striking properties such as safety [14–16] and reliability [17–19]. Xia and Lo [20] offered a method by which ibuprofen (IBU)—considered as organic pollutant in flowing waters, can be eliminated from the water using hybrid nanocomposites. It is shown that hybrid nanocomposite matrix can be increased the strength of organic pollutant. Filippov et al. [21] presented a novel method for characterizing hybrid nanocomposites. Ebrahimi and Dabbagh [22] carried out a research regarding vibration of hybrid nanocomposite plates. Using classical plate theory and Hamilton principle, the governing equations are obtained and solved analytically. It is observed that hybrid nanocomposites are able to resist high amounts of frequency compared to the ordinary composites. Dabbagh et al. [23] reported thermal buckling of hybrid nanocomposites beam. Using refined plate theory as well as Hamilton’s principle, the governing equations are obtained and utilizing Galerkin’s procedure, the motion equations are solved. It is shown that hybrid nanocomposite structures are tougher toward critical buckling loads than conventional composites. Moreover, creep as well as viscoelastic behaviors of hybrid glass/epoxy nanocomposites are studied experimentally by Salehi and colleague [24].

Without doubt, besides invented methods as to tightening structures in various domains, reinforcing structures via nanocomposites and CFs have been featured strongly since last decade. Nanocomposites such as CNTs have been preferable materials to be added into structures for this intention due to high fracture resistance and capability of vibration damping. Regardless of nanotube’s types containing single walled carbon nanotubes (SWCNTs) and multi walled carbon nanotubes (MWCNTs) and their branches, they possess notable properties in different fields such as significant electrical and thermal conductivities, strength and elasticity and energy storage that have made them desirable. Moreover, investigations regarding CNTs and their composites are of interest between scientists to enhance damping properties of these materials, especially epoxy, in terms of loss modulus [25,26] or damping ratio [27,28]. There are researches exploring properties of nanocomposites Vinson [29] and Herman et al. [30]. Gul and Aydogdu [31] investigated wave dispersion of DWCNTs. They explained that, through Doublet Mechanics, the wave dispersion was studied which had precise outcomes for flexural as well as axial wave dispersion in nanotubes. Vibration analysis of SWCNTs was carried out by Avramov [32]. Using Sanders-Koiter shell methods—as well as nonlocal elasticity—the motion equations were derived and solved numerically via the Galerkin procedure. In another study, Bian and Wang [33] carried out a research as to buckling of DWCNTs in a thermal environment. The influence of finite temperature and various nonlocal effects have been studied. They revealed that buckling of DWCNT declines whereas the finite temperature rises. Natural frequency analysis of FG-CNTs curved shell panel which is shallow has been done by Mehar et al. [34]. In this study, higher-order theory is used for obtaining governing equations and finite element method (FEM) is utilized for solving equations. Further, the precision of this numerical method is compared with different numerical procedures. Zhang et al. [35] analyzed deflection of FG-CNTRC plate which is on the Pasternak medium. First-order shear deformation theory (FSDT) besides Ritz methods are utilized in order to obtain and solve governing equations, respectively. In this work, the influences relevant to CNT distributions and volume fraction and foundation up deflection are analyzed. Jiao et al. [36] discussed dynamic buckling behavior of FG-CNTRC shell. The structure is under time-varying load and FSDT is applied to derive motion equations. Galerkin method is used for solving the equations and the influence of dispersion of CNTs and

their volume fraction and other parameters are taken into account. Mirzaei and Kiani [37] investigated buckling evaluation of FG-CNTRC plates in thermal environment. In this study, besides various parameters including different boundary conditions and aspect ratio, the influence of CNTs are discussed. They indicated that FG-X distribution type is the better choice. In another research, wave dispersion of FG nanocomposites which are rein- forced through CNTs are investigated by Janghorban and Nami [38]. Dynamic analysis of structures induced by non-conservative loading and electromagnetic interactions has been studied in the literature. Based on the equivalent single-layer linear theory for laminated shells, Kolahchi et al. [39] presented dynamic buckling of sandwich nanoplate subjected to harmonic compressive load based on nonlocal elasticity theory. Mikhasev et al. [40] investigated free and forced vibrations of thin cylindrical sandwich panels with magne- torheological core. Hajmohammad et al. [41] analyzed dynamic response of sandwich plates under the blast load based on sinusoidal shear deformation theory. Malikan and Ere- meyev [42] investigated the effect of flexoelectricity on dynamic response of piezoelectric nanobeam assuming internal viscoelasticity. Malikan et al. [43] studied torsional stability of a nanocomposite shell subjected to magnetic field utilizing nonlocal strain gradient theory. Keshtegar et al. [44] presented dynamic stability of nanocomposite-truncated sandwich conical shells based on differential cubature method.

To date, no research has been conducted studying and analyzing the dynamic behavior of a hybrid nanocomposite polymer beam reinforced via CFs as well as CNTs using ESDBT. In this study, we examine the beams composed by multiphase nanocomposites, including carbon/fiber/CNT/ polymer which the responses of beams are extracted using micromechanics—as well as Halpin-Tsai equations. With respect to DQM and Bolotin procedures, the obtained motion equations are solved, and DIR are attained, respectively. Distinct variables are investigated, such as the influences of CNT volume fraction, CF volume percent, boundary edges as well as the structure's geometric variables on the dynamic behavior of the beam.

## 2. Problem Definition

Figure 1 illustrates a polymer beam, in which the CNTs and CFs are considered the reinforcements. Further, the thickness and length of the beam, respectively are $h$ and $L$.

![](./images/812519659168333825_2.jpg)

Figure 1. Configuration of polymer beam reinforced via carbon fibers (CFs) as well as carbon nanotubes (CNTs).

In this section, in order to model the structure mathematically, ESDBT is employed and hence, the displacement vectors are given by [45]:

$$
\begin{aligned}
u_{1}(x, z, t) & =u(x, t)-z \frac{\partial w(x, t)}{\partial x}+\Phi(z)\left(\frac{\partial w(x, t)}{\partial x}-\psi(x, t)\right), \\
u_{2}(x, z, t) & =0, \\
u_{3}(x, z, t) & =w(x, t).
\end{aligned} \tag{1}
$$

In above relation, $u_1$ and $u_3$ respectively describe mid-plane displacements in longitudinal and thickness directions. Moreover, $\psi$ defines rotation related to cross section and $\Phi(z)$ represents shape function of the beam that can be written as

$$
\Phi(z)=z e^{-2(z / h)^{2}},
\tag{2}
$$

in which $h$ refers to thickness of structure. Furthermore, the strain components of this structure are described as

$$
\varepsilon_{x x}=\left(\frac{\partial u}{\partial x}\right)-z\left(\frac{\partial^{2} w}{\partial x^{2}}\right)+\left(z e^{-2(z / h)^{2}}\right)\left(\frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial \psi}{\partial x}\right),
\tag{3}
$$

$$
\gamma_{x z}=\left(e^{-2(z / h)^{2}}-\frac{4 z^{2} e^{-2(z / h)^{2}}}{h^{2}}\right)\left(\frac{\partial w}{\partial x}-\psi\right).
\tag{4}
$$

It should be noted that stress–strain relations can be written as

$$
\sigma_{x x}=C_{11} \varepsilon_{x x},
\tag{5}
$$

$$
\tau_{x z}=C_{44} \gamma_{x z},
\tag{6}
$$

where $C_{11}$ and $C_{44}$ express the elastic constants achieved through Halpin–Tsai model.

### 2.1. Modeling CNT/Fiber/Polymer Multiphase Nanocomposite

Carbon nanotubes were grown directly on carbon fibers using chemical vapor deposition. When embedded in a polymer matrix, the change in length scale of carbon nanotubes relative to carbon fibers results in a multiscale composite [46]. Incorporation of micromechanics as well as Halpin–Tsai model [47] are utilized for reaching polymer beam's equivalent material properties in two phases. Orthotropic effective characteristics related to CNT-reinforced multi-phase laminates are given by

$$
E_{11}=V_{F} E_{11}^{F}+V_{M N C} E^{M N C},
\tag{7}
$$

$$
\frac{1}{E_{22}}=\frac{1}{E_{22}^{F}}+\frac{V_{M N C}}{E^{M N C}}-V_{F} V_{M N C}-\frac{\frac{v_{F} E^{M N C}}{E_{22}^{F}}+\frac{v_{M N C}^{2} E_{22}^{F}}{E^{M N C}}-2 v_{F} v_{M N C}}{V_{F} E_{22}^{F}+V_{M N C} E^{M N C}},
\tag{8}
$$

$$
\frac{1}{G_{12}}=\frac{V_{F}}{G_{12}^{F}}+\frac{V_{M N C}}{G^{M N C}},
\tag{9}
$$

$$
\rho=V_{F} \rho^{F}+V_{M N C} \rho^{M N C},
\tag{10}
$$

$$
v_{12}=V_{F} v^{F}+V_{M N C} v^{M N C},
\tag{11}
$$

in which $G$, $E$ and $\rho$ respectively express shear modulus, Young's modulus and mass density; $V$ as well as $v$ represent volume fraction and Poisson's ratio, respectively. Further, the subscript and superscript $MNC$ and $F$, respectively refer to matrix of nanocomposite and fibers. With respect to Halpin–Tsai equations, nanocomposite's elastic modulus is written as follow [48]:

$$
E^{M N C}=\frac{E^{M}}{8}\left[5\left(\frac{1+2 \beta_{d d} V_{C N}}{1-\beta_{d d} V_{C N}}\right)+3\left(\frac{1+2\left(\ell^{C N} / \mathrm{d}^{C N}\right) \beta_{d l} V_{C N}}{1-\beta_{d l} V_{C N}}\right)\right],
\tag{12}
$$

in which

$$
\beta_{d l}=\left(\frac{\left(E_{11}^{C N} / E^{M}\right)-\left(\mathrm{d}^{C N} / 4 t^{C N}\right)}{\left(E_{11}^{C N} / E^{M}\right)+\left(\ell^{C N} / 2 t^{C N}\right)}\right),
\tag{13}
$$

$$
\beta_{d d}=\left(\frac{\left(E_{11}^{C N} / E^{M}\right)-\left(\mathrm{d}^{C N} / 4 t^{C N}\right)}{\left(E_{11}^{C N} / E^{M}\right)+\left(d^{C N} / 2 t^{C N}\right)}\right),
\tag{14}
$$

in which $V_{M}$ as well as $E^{M}$ respectively describe matrix's volume fraction and Young's modulus. Moreover $V_{C N}, E^{C N}, t^{C N}, d^{C N}$ and $\ell^{C N}$ respectively define volume fraction, Young's modulus, thickness, outer diameter and length correlative to CNTs. The CNT volume fraction is given by

$$
V_{C N}=\frac{w_{C N}}{w_{C N}+\left(\rho^{C N} / \rho^{m}\right)-\left(\rho^{C N} / \rho^{m}\right) w_{C N}},
\tag{15}
$$

in which $\rho^{m}$ and $\rho^{C N}$ respectively hint at mass density of matrix and CNTs and $w_{C N}$ is mass fraction. Likewise, Poisson's ratio, mass density and shear modulus related to $M N C$ are written as below:

$$
v^{M N C}=v^{M},
\tag{16}
$$

$$
\rho^{M N C}=V_{C N} \rho^{C N}+V_{M} \rho^{M},
\tag{17}
$$

$$
G^{M N C}=\frac{E^{M N C}}{2\left(1+v^{M N C}\right)},
\tag{18}
$$

in which $v^{M N C}$ as well as $v^{M}$ respectively represent Poisson's ratio related to $M N C$ and matrix. It is mentioned that because of the CNT's small extent, the Poisson's ratio related to matrix and $M N C$ will be assumed analogous [49].

### 2.2. Motion Equations

In this part, the structure's strain energy is described as below:

$$
U=\frac{1}{2} \int_{V}\left(\sigma_{x x} \varepsilon_{x x}+\tau_{x z} \gamma_{x z}\right) d V,
\tag{19}
$$

Likewise, by introducing Equations (3) and (4) into Equation (19), we have

$$
U=\frac{1}{2} \int_{0}^{L}\left[\iint\left[N_{x}\left(\left(\frac{\partial u}{\partial x}\right)\right)-M_{x}\left(\frac{\partial^{2} w}{\partial x^{2}}\right)+F_{x}\left(\frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial \psi}{\partial x}\right)+Q_{x}\left(\left(\frac{\partial w}{\partial x}-\psi\right)\right)\right] d x,\right.
\tag{20}
$$

Therefore, stress resultants are given by

$$
N_{x}=\int \sigma_{x x} d A,
\tag{21}
$$

$$
M_{x}=\int \sigma_{x x} z d A,
\tag{22}
$$

$$
F_{x}=\int \sigma_{x x} \Phi(z) d A,
\tag{23}
$$

$$
Q_{x}=\int \tau_{x z} \frac{\partial \Phi(z)}{\partial z} d A,
\tag{24}
$$

In order to extend above equations, Equations (3)-(6) are substituted into Equations (21)-(24) and the outcomes are presented in Appendix A. For the next step, the kinetic energy for this structure are written as

$$
K=\frac{\rho}{2} \int\left(\dot{u}_{1}{ }^{2}+\dot{u}_{2}{ }^{2}+\dot{u}_{3}{ }^{2}\right) d V
\tag{25}
$$


Substituting Equation (1) into Equation (25) yields

$$
K=\frac{\rho}{2} \int\left(\left(\frac{\partial u}{\partial t}-z \frac{\partial^{2} w}{\partial x \partial t}+z\left(\frac{\partial^{2} w}{\partial x \partial t}-\frac{\partial \psi}{\partial t}\right)\right)^{2}+\left(\frac{\partial w}{\partial t}\right)^{2}\right) d V.
\tag{26}
$$

in which $\rho$ refers to the density of the beam. The inertia moments are expressed as follow

$$
\left\{\begin{array}{l}
I_{0} \\
I_{1} \\
I_{2} \\
I_{3} \\
I_{4} \\
I_{5}
\end{array}\right\}=\int\left[\begin{array}{c}
\rho \\
\rho z \\
\rho z^{2} \\
\rho \Phi(z) \\
\rho z \Phi(z) \\
\rho \Phi(z)^{2}
\end{array}\right] d A,
\tag{27}
$$

Factoring in Equation (27), the Equation (26) is rewritten as

$$
\begin{gathered}
K=0.5 \int\left[I_{0}\left(\left(\frac{\partial u}{\partial t}\right)^{2}+\left(\frac{\partial w}{\partial t}\right)^{2}\right)-2 I_{1}\left(\frac{\partial u}{\partial t} \frac{\partial^{2} w}{\partial x \partial t}\right)+I_{2}\left(\frac{\partial^{2} w}{\partial x \partial t}\right)^{2}\right. \\
\left.+I_{3} \frac{\partial u}{\partial t}\left(\frac{\partial^{2} w}{\partial x \partial t}-\frac{\partial \psi}{\partial t}\right)-I_{4} \frac{\partial^{2} w}{\partial x \partial t}\left(\frac{\partial^{2} w}{\partial x \partial t}-\frac{\partial \psi}{\partial t}\right)+I_{5}\left(\frac{\partial^{2} w}{\partial x \partial t}-\frac{\partial \psi}{\partial t}\right)^{2}\right] d x.
\end{gathered}
\tag{28}
$$

Eventually, motion equations are achieved utilizing Hamilton's principle:

$$
\int_{0}^{t}(\delta U-\delta K) d t=0,
\tag{29}
$$

By introducing Equations (20), (28) into Equation (29), the governing equations are expressed as follow

$$
\delta u: \frac{\partial N_{x}}{\partial x}=I_{0} \frac{\partial^{2} u}{\partial t^{2}}+\left(I_{3}-I_{1}\right) \frac{\partial^{3} w}{\partial x \partial t^{2}}-I_{3} \frac{\partial^{2} \psi}{\partial t^{2}},
\tag{30}
$$

$$
\begin{gathered}
\delta w: \frac{\partial^{2} M_{x}}{\partial x^{2}}+\left(2 e_{31} V_{0}+P\right) \frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial^{2} F_{x}}{\partial x^{2}}+\frac{\partial Q_{x}}{\partial x}=I_{0} \frac{\partial^{2} w}{\partial t^{2}} \\
+\left(I_{1}-I_{3}\right) \frac{\partial^{3} u}{\partial x \partial t^{2}}+\left(2 I_{4}-I_{2}-I_{5}\right) \frac{\partial^{4} w}{\partial x^{2} \partial t^{2}}+\left(I_{5}-I_{4}\right) \frac{\partial^{3} \psi}{\partial x \partial t^{2}},
\end{gathered}
\tag{31}
$$

$$
\delta \psi: Q_{x}-\frac{\partial F_{x}}{\partial x}=I_{5} \frac{\partial^{2} \psi}{\partial t^{2}}-I_{3} \frac{\partial^{2} u}{\partial t^{2}}+\left(I_{4}-I_{5}\right) \frac{\partial^{3} w}{\partial x \partial t^{2}},
\tag{32}
$$

where $P=\alpha P_{c r}+\beta P_{c r} \cos (\omega t)$ in which $\alpha, \beta, P_{c r}$ and $\omega$ are static load factor, dynamic load factor, critical load and frequency, respectively. For expansion of above equations, Equations (A1)-(A4) are substituted into Equations (30)-(32) and hence, they are expressed as below:

$$
\begin{gathered}
A_{11}\left(\frac{\partial^{2} u}{\partial x^{2}}\right)-B_{11}\left(\frac{\partial^{3} w}{\partial x^{3}}\right)+E_{11}\left(\frac{\partial^{3} w}{\partial x^{3}}-\frac{\partial^{2} \psi}{\partial x^{2}}\right) \\
=I_{0} \frac{\partial^{2} u}{\partial t^{2}}+\left(I_{3}-I_{1}\right) \frac{\partial^{3} w}{\partial x \partial t^{2}}-I_{3} \frac{\partial^{2} \psi}{\partial t^{2}},
\end{gathered}
\tag{33}
$$

$$
\begin{gathered}
\left(B_{11}-E_{11}\right)\left(\frac{\partial^{3} u}{\partial x^{3}}\right)-\left(D_{11}-F_{11}\right)\left(\frac{\partial^{4} w}{\partial x^{4}}\right)+\left(F_{11}-H_{11}\right)\left(\frac{\partial^{4} w}{\partial x^{4}}-\frac{\partial^{3} \psi}{\partial x^{3}}\right) \\
+L_{44}\left(\frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial \psi}{\partial x}\right)+\left(2 e_{31} V_{0}+P\right)=I_{0} \frac{\partial^{2} w}{\partial t^{2}} \\
+\left(I_{1}-I_{3}\right) \frac{\partial^{3} u}{\partial x \partial t^{2}}+\left(2 I_{4}-I_{2}-I_{5}\right) \frac{\partial^{4} w}{\partial x^{2} \partial t^{2}}+\left(I_{5}-I_{4}\right) \frac{\partial^{3} \psi}{\partial x \partial t^{2}},
\end{gathered}
\tag{34}
$$

$$
\begin{gathered}
L_{44}\left(\frac{\partial w}{\partial x}-\psi\right)-E_{11}\left(\frac{\partial^{2} u}{\partial x^{2}}\right)+F_{11}\left(\frac{\partial^{3} w}{\partial x^{3}}\right) \\
-H_{11}\left(\frac{\partial^{3} w}{\partial x^{3}}-\frac{\partial^{2} \psi}{\partial x^{2}}\right)=I_{5} \frac{\partial^{2} \psi}{\partial t^{2}}-I_{3} \frac{\partial^{2} u}{\partial t^{2}}+\left(I_{4}-I_{5}\right) \frac{\partial^{3} w}{\partial x \partial t^{2}},
\end{gathered}
\tag{35}
$$

At the end, for investigating different cases of this beam, various boundary edges are considered which can be computed as below

- **Clamped-Clamped**

$$
\begin{aligned}
& w=u=\psi=0, \quad @ \quad x=0 \\
& w=u=\psi=0. \quad @ \quad x=L
\end{aligned}
\tag{36}
$$

- **Clamped-Simply**

$$
\begin{aligned}
& w=u=\psi, \quad @ \quad x=0 \\
& w=u=M_{x}=0, \quad @ \quad x=L
\end{aligned}
\tag{37}
$$

- **Simply-Simply**

$$
\begin{aligned}
& w=u=M_{x}=0, \quad @ \quad x=0 \\
& w=u=M_{x}=0, \quad @ \quad x=L
\end{aligned}
\tag{38}
$$

## 3. Solving Procedure

As mentioned, for solution of motion equations besides determination of DIR, DQM is employed. In the method, the various orders of the beam's differential equations are converted to a set of algebraic equations based on weighting coefficients. In other words, with respect to this precise procedure, one derivative of a function at one contemplated separate point can be computed, utilizing the sum of the extent of function at every separate point opted out in the scope of the solution. The approximation of the derivative function can be expressed in a general form as [50-52]

$$
\frac{d^{n} f\left(x_{i}\right)}{d x^{n}}=\sum_{j=1}^{N} C_{i j}^{(n)} f\left(x_{j}\right) \quad n=1, \ldots, N-1,
\tag{39}
$$

in which $f(x)$ refers to the function, $N$ describes number of points, $x_{i}$ represents an instance point of the function scope, $f_{i}$ expresses the amount of the function at $i$th instance point and $C_{i j}$ denotes weighting coefficients. Moreover, selecting grid points, as well as weighting coefficients would be essential parameter in gaining precise consequences. Grid points can be contemplated through Chebyshev polynomials as

$$
x_{i}=\frac{L}{2}\left[1-\cos \left(\frac{i-1}{N_{x}-1}\right) \pi\right] \quad i=1, \ldots, N_{x}
\tag{40}
$$

With respect to the Chebyshev polynomials, grid points would be denser in the neighbor of boundaries. The weighting coefficients are achieved using following relation

$$
C_{i j}^{(1)}=\frac{L_{1}\left(x_{i}\right)}{\left(x_{i}-x_{j}\right) L_{1}\left(x_{j}\right)} \quad \text { for } i \neq j, \quad i, j=1,2, \ldots, N
\tag{41}
$$

where

$$
L_{i}(x)=\prod_{j=1}^{N}\left(x_{i}-x_{j}\right).
\tag{42}
$$

With respect to DQM, motion equations in matrix are expressed form as below:

$$
\left([K]\left\{\begin{array}{l}
\left\{d_{b}\right\} \\
\left\{d_{d}\right\}
\end{array}\right\}+P[K]_{G}\left\{\begin{array}{l}
\left\{d_{b}\right\} \\
\left\{d_{d}\right\}
\end{array}\right\}+[M]\left\{\begin{array}{l}
\left\{\ddot{d}_{b}\right\} \\
\left\{\ddot{d}_{d}\right\}
\end{array}\right\}\right)=\left\{\begin{array}{l}
\{0\} \\
\{0\}
\end{array}\right\},
\tag{43}
$$

where $[M],[K]$ as well as $[C]$ define mass matrix, stiffness matrix and damper matrix, respectively. Further, $\left\{d_{b}\right\}$ and $\left\{d_{d}\right\}$ define boundary points as well as domain points, respectively. With respect to Bolotin's method, elements related to $\{Y\}$ can be described in Fourier series having period $2 T$ as

$$
\{Y\}=\sum_{k=1,3, \ldots}^{\infty}\left[\{a\}_{k} \sin \frac{k \omega t}{2}+\{b\}_{k} \cos \frac{k \omega t}{2}\right],
\tag{44}
$$

In this part, by substituting Equation (44) into Equation (43) and setting the factors of cosine and sine—as well as the sum of constant terms to zero—we have

$$
\left| \left( [K] - \left( \alpha \pm \frac{\beta}{2} \right) P_{cr}[K]_G \right) - [M] \frac{\omega^2}{4} \right| = 0, \tag{45}
$$

Hence, as to gain variation of $\omega$ and DIR based on $\beta$, the mentioned relation can be solved according to eigenvalue problem.

## 4. Numerical Consequences
This part is presented to investigate and analyze the influence of diverse variables on the dynamic behavior of the beam with length of L = 2 m and thickness of h = 30 cm. As noted previously, the hypothesized beam is composed of epoxy and CFs. In addition, CNTs are considered the reinforcements and properties of these materials are assumed, according to [34]. Young's modulus, Poisson's ratio and density of epoxy are $E^M = 3.51$ GPa, $\nu^M = 0.3$ and $\rho^M = 1200$ Kg/m³, respectively. Further, material characteristics including Young's modulus, Shear modulus, Poisson's ratio and density related to the CFs, respectively are $E_{11}^F = 233.05$ GPa, $E_{22}^F = 23.1$ GPa, $G_{12}^F = 8.96$ GPa, $\nu^F = 0.2$ and $\rho^F = 1750$ Kg/m³. Likewise, Young's modulus, Poisson's ratio, density, outer diameter, thickness and length of CNT, respectively are $E^{CN} = 640$ GPa, $\nu^{CN} = 0.27$, $\rho^{CN} = 1350$ Kg/m³, $d^{CN} = 1.4$ nm, $t^{CN} = 0.34$ nm and $\ell^{CN} = 25 \times 10^{-6}$ m.

### 4.1. Validation
To date, in spite of proliferation of researches in mechanic and material fields, there is no work analyzing dynamic behavior of hybrid nanocomposite polymer beams reinforced via CFs and CNTs using ESDBT and determining DIR. Therefore, in order to demonstrate the precision—as well as validity of the considered theories and numerical methods—some characteristics containing CNTs, CFs and ESDBT are disregarded to fit in this beam with the research published by Joubaneh et al [53]. In this research, vibration of a three-layer beam is studied based on theoretical and experimental methods. For this purpose, a beam with shear modulus of 22.1 GPa, Poisson's ratio of 0.3, density of 60 kg/m³, thickness of 15 mm and length of 260 mm is assumed which is covered with two layers at the top and bottom of core with Young's modulus of 210 GPa, Poisson's ratio of 0.3, density of 7900 kg/m³ and thickness of 1.9 mm. For experimental analyses, a clamped-free boundary condition of beam with three layers is installed on a VDL shaker (B & K V830-335-SPA16K) using a head plate and a fixture, both made of aluminum, as shown in Figure 2.

![](./images/812519659168333825_3.jpg)

Figure 2. Schematic of experimental setup extracted from Joubaneh et al. [53].

The theoretical and experimental results of [53] are shown in Table 1: the outcomes are validated with our numerical method. As can be seen, the results of this study are close to the theoretical and experimental results [53,54].

Table 1. Comparison of the obtained natural frequencies.

<table>
<thead>
  <tr>
    <th>Mode</th>
    <th>DQ Method [54]</th>
    <th>Experiment [53]</th>
    <th>Present Work</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>118.00</td>
    <td>111.19</td>
    <td>112.12</td>
  </tr>
  <tr>
    <td>2</td>
    <td>381.00</td>
    <td>364.60</td>
    <td>366.23</td>
  </tr>
  <tr>
    <td>3</td>
    <td>719.84</td>
    <td>680.80</td>
    <td>687.33</td>
  </tr>
  <tr>
    <td>4</td>
    <td>1141.94</td>
    <td>1063.50</td>
    <td>1074.98</td>
  </tr>
  <tr>
    <td>5</td>
    <td>1676.51</td>
    <td>1652.07</td>
    <td>1666.44</td>
  </tr>
</tbody>
</table>

In another validation, the buckling of nanocomposite beam is studied. A Poly methyl methacrylate (PMMA) with Young's modulus, Poisson's ratio and density of epoxy are $E^M = 2.5\ \text{GPa}, \nu^M = 0.3$ and $\rho^M = 1190\ \text{Kg/m}^3$, respectively is assumed which is reinforced with 0.12 carbon nanotube with Young's modulus, Poisson's ratio and the density of epoxy are $E_{11}^{CN} = 600\ \text{GPa}$, $E_{22}^{CN} = 10\ \text{GPa}$, $\nu^{CN} = 0.19$ and $\rho^{CN} = 1400\ \text{Kg/m}^3$, respectively. The non-dimensional buckling load $\overline{P} = P/hE^M$ for different boundary condition is presented in Table 2. It is shown that the result of this study are in good agreement with Asadi and Wang [55] and Yas and Samadi [56].

Table 2. Comparison of the obtained critical buckling load.

<table>
<thead>
  <tr>
    <th>BC</th>
    <th>Asadi and Wang [55]</th>
    <th>Yas and Samadi [56]</th>
    <th>Present Work</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>SS</td>
    <td>0.09831</td>
    <td>0.09859</td>
    <td>0.09844</td>
  </tr>
  <tr>
    <td>CS</td>
    <td>0.14878</td>
    <td>0.14948</td>
    <td>0.14852</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>0.21264</td>
    <td>0.21395</td>
    <td>0.21272</td>
  </tr>
</tbody>
</table>

Table 3 presents the dimensionless frequency of the beam reinforced by CNTs, considering the material properties the same as those mentioned in before validation. The results are reported for different theories of first-order shear deformation theory (FSDT), third order shear deformation theory (TSDT), exponential order shear deformation theory (ESDT), higher order shear deformation theory (HSDT) and trigonometric shear deformation theory (TrSDT) which are presented by Wattanasakulpong and Ungbhakorn [57]. It is seen that the accuracy of the obtained results is good.

Table 3. Comparison of the obtained dimensionless frequency.

<table>
<thead>
  <tr>
    <th>Theory</th>
    <th>Wattanasakulpong and Ungbhakorn [57]</th>
    <th>Present Work</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>FSDT</td>
    <td>0.9976</td>
    <td>0.9974</td>
  </tr>
  <tr>
    <td>TSDT</td>
    <td>0.9745</td>
    <td>0.9749</td>
  </tr>
  <tr>
    <td>ESDT</td>
    <td>0.9756</td>
    <td>0.9759</td>
  </tr>
  <tr>
    <td>HSDT</td>
    <td>0.9745</td>
    <td>0.9744</td>
  </tr>
  <tr>
    <td>TrSDT</td>
    <td>0.9749</td>
    <td>0.9741</td>
  </tr>
</tbody>
</table>

### 4.2. Parametric Study

In this section, the dynamic stability of the structure is studied for different parameters. All of figures show the excitation frequency against dynamic load factor (i.e., $\beta$) which represent the DIR of structure. In these figures, the regions inside and outside the boundary curves correspond to unstable (parametric resonance) and stable regions, respectively.

At first, so as to assess the precision as well as convergence of applied numerical method, Figure 3 is depicted. As observed, excitation frequencies were obtained for various grid points. It is clear that fifteen grid points can be factored in the precise outcomes in this numerical method.

![](./images/812519659168333825_4.jpg)

Figure 3. Precision and convergence of differential quadrature method (DQM).

Figure 4 presents the influence of CNT weight-percentage on DIR. Likewise, it is worth noting that the inside sections of triangular shapes represent unstable areas and consequently, the outside sections indicate stable areas of this beam. It is obvious that rise of CNT weight percentage triggers increase in excitation frequency of this structure. To put it differently, the DIR takes place at higher extents of excitation frequencies while increasing weight percentage of CNTs. It is justified with this fact that increase in CNT weight percentage leads to enhancement of stiffness as well as bending rigidity related to this structure.

![](./images/812519659168333825_5.jpg)

Figure 4. Effect of CNT weight percentage on dynamic instability region (DIR).

In this work, various boundary edges were factored in to extend this research for different cases. Therefore, Figure 5 shows the influence of different boundary edges containing clamped-clamped (CC), clamped-simply (CS) and simply-simply (SS) boundary edges on the dynamic behaviors of this system. As observed, boundary edges have an undisputed effect on the DIR of the beam, and it is vivid that this structure with CC boundary edges

contains higher DIR compared to CS as well as SS having lower quantities. In fact, it raises bending rigidity.

![](./images/812519659168333825_6.jpg)

Figure 5. Effect of distinct boundary edges on DIR.

Figure 6 illustrates to indicate the significance related to presence of CFs and its volume percent and consequently its influence on the dynamic behaviors of the system. As expected, increase in volume percent of CFs results in shift of DIR to higher extents of excitation frequencies owing to rise of system's stiffness.

![](./images/812519659168333825_7.jpg)

Figure 6. Effect of volume percent of CFs on DIR.

Having been plotted below, Figures 7 and 8 are the exemplary states to ascertain the influence of geometric variables on the dynamic behavior of the beam. Figures 7 and 8, respectively evaluate the changes of length and thickness of structure. It is construed that rise of length parameter of polymeric beam results in alteration of DIR into the lower extents. In fact, this change can affect characteristics related to the structure and cause softness of whole structure. Inversely, increment of the thickness leads to improvement in the stiffness of system and move in DIR to the higher extents.

![](./images/812519659168333825_8.jpg)

Figure 7. Effect of beam length on DIR.

![](./images/812519659168333825_9.jpg)

Figure 8. Effect of beam thickness on DIR.

## 5. Conclusions

This concerned the evaluation of dynamic instability related to hybrid nanocomposite polymer beam. The considered beam composed by multiphase nanocomposite, include polymer-CNTs- CFs. Halpin-Tsai as well as micromechanics equations were applied to compute effective material characteristics correlative to multiphase nanocomposite layers. Employing ESDBT besides Hamilton's principle, governing equations were obtained. Further, the DQM and Bolotin procedures were utilized to solve the governing equations and achieve dynamic behavior of polymer beam. Different parameters such as various boundary edges, geometric parameters, CNTs and CFs volume fractions were brought up and their influences were illustrated on DIR. The prominent outcomes are presented as following

- Increments of weight-percentage of CNTs can lead to shift of DIR to the right;
- Presence of CFs as well as CNTs play paramount role in dynamic behavior of hybrid polymer structure and raise the excitation frequency;

- Considering CC boundary edge causes increase in excitation frequency of structure compared to CS and SS boundary edges;
- The obtained results accentuate the geometric parameters and their influence on the dynamic behavior of structures.

Author Contributions: Conceptualization, R.K., B.K. and A.E.; formal analysis, R.K., A.E. and N.-T.T.; investigation, B.K., R.K., A.E. and N.-T.T.; supervision, R.K.; writing—original draft, B.K., R.K. and A.E.; writing—review & editing, R.K. and A.E. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflict of interest.

## Appendix A

$$
N_{x}=A_{11}\left(\frac{\partial u}{\partial x}+\frac{1}{2}\left(\frac{\partial w}{\partial x}\right)^{2}\right)-B_{11}\left(\frac{\partial^{2} w}{\partial x^{2}}\right)+E_{11}\left(\frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial \psi}{\partial x}\right), \tag{A1}
$$

$$
M_{x}=B_{11}\left(\frac{\partial u}{\partial x}+\frac{1}{2}\left(\frac{\partial w}{\partial x}\right)^{2}\right)-D_{11}\left(\frac{\partial^{2} w}{\partial x^{2}}\right)+F_{11}\left(\frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial \psi}{\partial x}\right), \tag{A2}
$$

$$
F_{x}=E_{11}\left(\frac{\partial u}{\partial x}+\frac{1}{2}\left(\frac{\partial w}{\partial x}\right)^{2}\right)-F_{11}\left(\frac{\partial^{2} w}{\partial x^{2}}\right)+H_{11}\left(\frac{\partial^{2} w}{\partial x^{2}}-\frac{\partial \psi}{\partial x}\right), \tag{A3}
$$

$$
Q_{x}=L_{44}\left(\frac{\partial w}{\partial x}-\psi\right), \tag{A4}
$$

in which

$$
A_{11}=\int C_{11} d A, \tag{A5}
$$

$$
B_{11}=\int C_{11} z d A, \tag{A6}
$$

$$
E_{11}=\int C_{11} \Phi(z) d A, \tag{A7}
$$

$$
F_{11}=\int C_{11} z \Phi(z) d A, \tag{A8}
$$

$$
H_{11}=\int C_{11} \Phi(z)^{2} d A, \tag{A9}
$$

$$
L_{44}=\int C_{44} \frac{\partial \Phi(z)}{\partial z} d A, \tag{A10}
$$

## References

1.  Fischer, H. Polymer nanocomposites: From fundamental research to specific applications. *Mater. Sci. Eng. C* 2003, 23, 763–772. [CrossRef]
2.  Godovsky, D.Y. Device applications of polymer-nanocomposites. In *Biopolymers Pva Hydrogels, Anionic Polymerisation Nanocomposites*; Springer: Cham, Switerland, 2000; pp. 163–205.
3.  Tanaka, T.; Montanari, G.; Mulhaupt, R. Polymer nanocomposites as dielectrics and electrical insulation-perspectives for processing technologies, material characterization and future applications. *IEEE Trans. Dielectr. Electr. Insul.* 2004, 11, 763–784. [CrossRef]

4. Zhang, J.; Xiao, M.; Gao, L.; Chu, S. A combined projection-outline-based active learning kriging and adaptive importance sampling method for hybrid reliability analysis with small failure probabilities. Comput. Methods Appl. Mech. Eng. 2019, 344, 13-33. [CrossRef]

5. Zhang, J.; Xiao, M.; Gao, L.; Fu, J. A novel projection outline based active learning method and its combination with kriging metamodel for hybrid reliability analysis with random and interval variables. Comput. Methods Appl. Mech. Eng. 2018, 341, 32-52. [CrossRef]

6. Zhang, Y.; Gao, L.; Xiao, M. Maximizing natural frequencies of inhomogeneous cellular structures by kriging-assisted multiscale topology optimization. Comput. Struct. 2020, 230, 106197. [CrossRef]

7. Zhu, S.-P.; Keshtegar, B.; Chakraborty, S.; Trung, N.-T. Novel probabilistic model for searching most probable point in structural reliability analysis. Comput. Methods Appl. Mech. Eng. 2020, 366, 113027. [CrossRef]

8. Keshtegar, B. Chaotic conjugate stability transformation method for structural reliability analysis. Comput. Methods Appl. Mech. Eng. 2016, 310, 866-885. [CrossRef]

9. Keshtegar, B. Enriched FR conjugate search directions for robust and efficient structural reliability analysis. Eng. Comput. 2018, 34, 117-128. [CrossRef]

10. Pastoriza-Santos, I.; Kinnear, C.; Pérez-Juste, J.; Mulvaney, P.; Liz-Marzán, L.M. Plasmonic polymer nanocomposites. Nat. Rev. Mater. 2018, 3, 375-391. [CrossRef]

11. de Leon, A.C.; Chen, Q.; Palaganas, N.B.; Palaganas, J.O.; Manapat, J.; Advincula, R.C. High performance polymer nanocomposites for additive manufacturing applications. React. Funct. Polym. 2016, 103, 141-155. [CrossRef]

12. Liu, F.; Li, Q.; Cui, J.; Li, Z.; Yang, G.; Liu, Y.; Dong, L.; Xiong, C.; Wang, H.; Wang, Q. High-energy-density dielectric polymer nanocomposites with trilayered architecture. Adv. Funct. Mater. 2017, 27, 1606292. [CrossRef]

13. Abbasi, H.; Antunes, M.; Velasco, J.I. Recent advances in carbon-based polymer nanocomposites for electromagnetic interference shielding. Prog. Mater. Sci. 2019, 103, 319-373. [CrossRef]

14. Zhang, J.; Xiao, M.; Gao, L.; Chu, S. Probability and interval hybrid reliability analysis based on adaptive local approximation of projection outlines using support vector machine. Comput. Aided Civ. Infrastruct. Eng. 2019, 34, 991-1009. [CrossRef]

15. Xiao, M.; Zhang, J.; Gao, L.; Lee, S.; Eshghi, A.T. An efficient kriging-based subset simulation method for hybrid reliability analysis under random and interval variables with small failure probability. Struct. Multidiscip. Optim. 2019, 59, 2077-2092. [CrossRef]

16. Keshtegar, B.; Zhu, S.-P. Three-term conjugate approach for structural reliability analysis. Appl. Math. Model. 2019, 76, 428-442. [CrossRef]

17. Keshtegar, B.; Meng, D.; Ben Seghier, M.E.A.; Xiao, M.; Trung, N.-T.; Bui, D.T. A hybrid sufficient performance measure approach to improve robustness and efficiency of reliability-based design optimization. Eng. Comput. 2020. [CrossRef]

18. Gao, L.; Xiao, M.; Shao, X.; Jiang, P.; Nie, L.; Qiu, H. Analysis of gene expression programming for approximation in engineering design. Struct. Multidiscip. Optim. 2012, 46, 399-413. [CrossRef]

19. Xiao, M.; Zhang, J.; Gao, L. A system active learning kriging method for system reliability-based design optimization with a multiple response model. Reliab. Eng. Syst. Saf. 2020, 199, 106935. [CrossRef]

20. Xia, D.; Lo, I.M. Synthesis of magnetically separable bi2o4/fe3o4 hybrid nanocomposites with enhanced photocatalytic removal of ibuprofen under visible light irradiation. Water Res. 2016, 100, 393-404. [CrossRef]

21. Filippov, A.; Afonin, D.; Kononenko, N.; Lvov, Y.; Vinokurov, V. New approach to characterization of hybrid nanocomposites. Colloids Surf. A Physicochem. Eng. Asp. 2017, 521, 251-259. [CrossRef]

22. Ebrahimi, F.; Dabbagh, A. Vibration analysis of multi-scale hybrid nanocomposite plates based on a halpin-tsai homogenization model. Compos. Part B Eng. 2019, 173, 106955. [CrossRef]

23. Dabbagh, A.; Rastgoo, A.; Ebrahimi, F. Thermal buckling analysis of agglomerated multiscale hybrid nanocomposites via a refined beam theory. Mech. Based Des. Struct. Mach. 2020, 1-27. [CrossRef]

24. Salehi, H.; Salehi, M. Experimental study on the mechanical, creep, and viscoelastic behavior of tio 2/glass/epoxy hybrid nanocomposites. Mech. Compos. Mater. 2016, 52, 623-636. [CrossRef]

25. Koratkar, N.A.; Wei, B.; Ajayan, P.M. Multifunctional structural reinforcement featuring carbon nanotube films. Compos. Sci. Technol. 2003, 63, 1525-1531. [CrossRef]

26. Koratkar, N.; Wei, B.; Ajayan, P.M. Carbon nanotube films for damping applications. Adv. Mater. 2002, 14, 997-1000. [CrossRef]

27. Zhou, X.; Shin, E.; Wang, K.; Bakis, C.E. Interfacial damping characteristics of carbon nanotube-based composites. Compos. Sci. Technol. 2004, 64, 2425-2437. [CrossRef]

28. Rajoria, H.; Jalili, N. Passive vibration damping enhancement using carbon nanotube-epoxy reinforced composites. Compos. Sci. Technol. 2005, 65, 2079-2093. [CrossRef]

29. Vinson, J.R. The Behavior of Sandwich Structures of Isotropic and Composite Materials; CRC Press: Boca Raton, FL, USA, 1999.

30. Herrmann, A.S.; Zahlen, P.C.; Zuardy, I. Sandwich structures technology in commercial aviation. In Sandwich Structures 7: Advancing with Sandwich Structures and Materials; Springer: Cham, Switerland, 2005; pp. 13-26.

31. Gul, U.; Aydogdu, M. Wave propagation in double walled carbon nanotubes by using doublet mechanics theory. Phys. E Low-Dimens. Syst. Nanostruct. 2017, 93, 345-357. [CrossRef]

32. Avramov, K. Nonlinear vibrations characteristics of single-walled carbon nanotubes by nonlocal elastic shell model. Int. J. Non-Linear Mech. 2018, 107, 149-160. [CrossRef]

33. Bian, L.; Wang, Y. Temperature-related study on buckling properties of double-walled carbon nanotubes. *Eur. J. Mech. A/Solids* 2020, 80, 103875. [CrossRef]

34. Mehar, K.; Panda, S.K.; Bui, T.Q.; Mahapatra, T.R. Nonlinear thermoelastic frequency analysis of functionally graded cnt-reinforced single/doubly curved shallow shell panels by fem. *J. Therm. Stresses* 2017, 40, 899–916. [CrossRef]

35. Zhang, L.; Song, Z.; Liew, K. Nonlinear bending analysis of fg-cnt reinforced composite thick plates resting on pasternak foundations using the element-free imls-ritz method. *Compos. Struct.* 2015, 128, 165–175. [CrossRef]

36. Jiao, P.; Chen, Z.; Li, Y.; Ma, H.; Wu, J. Dynamic buckling analyses of functionally graded carbon nanotubes reinforced composite (fg-cntrc) cylindrical shell under axial power-law time-varying displacement load. *Compos. Struct.* 2019, 220, 784–797. [CrossRef]

37. Mirzaei, M.; Kiani, Y. Thermal buckling of temperature dependent fg-cnt reinforced composite plates. *Meccanica* 2016, 51, 2185–2201. [CrossRef]

38. Janghorban, M.; Nami, M.R. Wave propagation in functionally graded nanocomposites reinforced with carbon nanotubes based on second-order shear deformation theory. *Mech. Adv. Mater. Struct.* 2017, 24, 458–468. [CrossRef]

39. Kolahchi, R.; Zarei, M.S.; Hajmohammad, M.H.; Oskouei, A.N. Visco-nonlocal-refined zigzag theories for dynamic buckling of laminated nanoplates using differential cubature-bolotin methods. *Thin-Walled Struct.* 2017, 113, 162–169. [CrossRef]

40. Mikhasev, G.I.; Eremeyev, V.A.; Wilde, K.; Maevskaya, S.S. Assessment of dynamic characteristics of thin cylindrical sandwich panels with magnetorheological core. *J. Intell. Mater. Syst. Struct.* 2019, 30, 2748–2769. [CrossRef]

41. Hajmohammad, M.H.; Kolahchi, R.; Zarei, M.S.; Nouri, A.H. Dynamic response of auxetic honeycomb plates integrated with agglomerated cnt-reinforced face sheets subjected to blast load based on visco-sinusoidal theory. *Int. J. Mech. Sci.* 2019, 153, 391–401. [CrossRef]

42. Malikan, M.; Eremeyev, V.A. On the dynamics of a visco-piezo-flexoelectric nanobeam. *Symmetry* 2020, 12, 643. [CrossRef]

43. Malikan, M.; Krasheninnikov, M.; Eremeyev, V.A. Torsional stability capacity of a nano-composite shell based on a nonlocal strain gradient shell model under a three-dimensional magnetic field. *Int. J. Eng. Sci.* 2020, 148, 103210. [CrossRef]

44. Keshtegar, B.; Farrokhian, A.; Kolahchi, R.; Trung, N.-T. Dynamic stability response of truncated nanocomposite conical shell with magnetostrictive face sheets utilizing higher order theory of sandwich panels. *Eur. J. Mech. A/Solids* 2020, 82, 104010. [CrossRef]

45. Şimşek, M.; Reddy, J. A unified higher order beam theory for buckling of a functionally graded microbeam embedded in elastic medium using modified couple stress theory. *Compos. Struct.* 2013, 101, 47–58. [CrossRef]

46. Thostenson, E.; Li, W.; Wang, D.; Ren, Z.; Chou, T. Carbon nanotube/carbon fiber hybrid multiscale composites. *J. Appl. Phys.* 2002, 91, 6034–6037. [CrossRef]

47. Shen, H.-S. A comparison of buckling and postbuckling behavior of fgm plates with piezoelectric fiber reinforced composite actuators. *Compos. Struct.* 2009, 91, 375–384. [CrossRef]

48. Kim, M.; Park, Y.-B.; Okoli, O.I.; Zhang, C. Processing, characterization, and modeling of carbon nanotube-reinforced multiscale composites. *Compos. Sci. Technol.* 2009, 69, 335–342. [CrossRef]

49. Clyne, T.; Hull, D. *An Introduction to Composite Materials*; Cambridge University Press: Cambridge, UK, 2019.

50. Fakhar, A.; Kolahchi, R. Dynamic buckling of magnetorheological fluid integrated by visco-piezo-gpl reinforced plates. *Int. J. Mech. Sci.* 2018, 144, 788–799. [CrossRef]

51. Motezaker, M.; Jamali, M.; Kolahchi, R. Application of differential cubature method for nonlocal vibration, buckling and bending response of annular nanoplates integrated by piezoelectric layers based on surface-higher order nonlocal-piezoelasticity theory. *J. Comput. Appl. Math.* 2020, 369, 112625. [CrossRef]

52. Kolahchi, R.; Zhu, S.-P.; Keshtegar, B.; Trung, N.-T. Dynamic buckling optimization of laminated aircraft conical shells with hybrid nanocomposite martial. *Aerosp. Sci. Technol.* 2020, 98, 105656. [CrossRef]

53. Joubaneh, E.F.; Barry, O.R.; Tanbour, H.E. Analytical and experimental vibration of sandwich beams having various boundary conditions. *Shock Vib.* 2018, 2018, 3682370. [CrossRef]

54. Hajmohammad, M.H.; Farrokhian, A.; Kolahchi, R. Smart control and vibration of viscoelastic actuator-multiphase nanocomposite conical shells-sensor considering hygrothermal load based on layerwise theory. *Aerosp. Sci. Technol.* 2018, 78, 260–270. [CrossRef]

55. Asadi, H.; Wang, Q. An investigation on the aeroelastic flutter characteristics of fg-cntrc beams in the supersonic flow. *Compos. Part B Eng.* 2017, 116, 486–499. [CrossRef]

56. Yas, M.; Samadi, N. Free vibrations and buckling analysis of carbon nanotube-reinforced composite timoshenko beams on elastic foundation. *Int. J. Press. Vessel. Pip.* 2012, 98, 119–128. [CrossRef]

57. Wattanasakulpong, N.; Ungbhakorn, V. Analytical solutions for bending, buckling and vibration responses of carbon nanotube-reinforced composite beams resting on elastic foundation. *Comput. Mater. Sci.* 2013, 71, 201–208. [CrossRef]