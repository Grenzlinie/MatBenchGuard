# Mechanical material characterization of Co nanowires and their nanocomposite

Wen-Hwa Chen $^{a}$, Hsien-Chie Cheng $^{b,*}$, Yu-Chen Hsu $^{a}$, Ruoh-Huey Uang $^{c}$, Jiong-Shiun Hsu $^{d}$

$^{a}$ Department of Power Mechanical Engineering, National Tsing-Hua University, Hsinchu, Taiwan
$^{b}$ Department of Aerospace and Systems Engineering, Feng Chia University, No. 100, Wenhwa Rd., Seatwen, Taichung 40724, Taiwan
$^{c}$ Nanotechnology Research Center, Industrial Technology Research Institute, Hsinchu, Taiwan
$^{d}$ Department of Power Mechanical Engineering, National Formosa University, Yunlin, Taiwan

---

## ARTICLE INFO

**Article history:**
Received 25 April 2008
Received in revised form 6 August 2008
Accepted 17 September 2008
Available online 30 September 2008

**Keywords:**
A. Nanocomposites
B. Thermo-mechanical properties
C. Finite element analysis
D. Atomic force microscopy
Molecular dynamics

---

## ABSTRACT

The study attempts to evaluate the complete set of effective transversely isotropic properties of a nanocomposite at various nanofiber-volume fractions through effective continuum modeling and experimental testing. The investigation starts from the theoretical and experimental assessments of the elastic properties the nanoscale Co metal using molecular dynamics (MD) simulations and nanoindentation testing, respectively. For determining the thermal-mechanical material properties of the nanocomposite, an effective finite element modeling (FEM)-based continuum modeling approach are introduced. Results show that the nanoscale Co metal presents inhomogeneity in the elastic material properties, the degree of which increases with a decreasing dimension of nanomaterials. Comparisons of the present results with experimental and existing theoretical data demonstrate the effectiveness of the proposed methods. Furthermore, as a result of the Co filament, significant anisotropy can be found in the effective thermal-mechanical properties of the nanocomposite but surprisingly not in the effective Poisson's ratio and coefficient of thermal expansion (CTE).

© 2008 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

1D nanostructures, such as nanowires, rods or tubes, present distinct size-dependent quantum effects [1] probably as a result of their 1D confinement along the transverse direction. The quantization together with nanosize, single crystal structure and minor defects yields their remarkable, physical material properties. Over the past few years, great efforts have been made to develop novel synthesis techniques for fabrication of morphologically and structurally controlled 1D nanomaterials, including template assisted nanowire growth, laser ablation, e-beam lithography, scanning probe lithography, vapor growth, electrochemical fabrication, solution-liquid-solid growth, etc. [2,3]. 1D nanostructures have a great potential for use in nanoscale electronic or electromechanical devices as active electronic components or interconnects [4]. Fiber-reinforced nanocomposites, a significant part of nanocomposites, are one of the most typical applications of 1D nanostructures. In recent years, they have drawn more and more scientific research attention as they can lead to new and improved properties, including impact resistance, flame retardancy, elastic modulus, and barrier properties.

Well understanding of the material properties and behaviors of the nanocomposites is critical to the success of their engineering application and the design and the development of novel nanocomposites (see, e.g. [5-7]). Upon determining the material behaviors of the nanocomposites, the physical and mechanical aspects of experimental testing at this scale present significant measurement challenges. By contrast, the less expensive and more efficient computational approaches, such as continuum mechanics [8,9] or MD methods [10], are an effective alternative. However, it remains a great challenge to employ computational models to characterize the effective material properties of nanocomposites because of their tricky scale: too large to be atomic/molecular systems and too small to fully demonstrate bulk properties. To deal with the problems, a multiscale simulation (MS) model is preferred. Unfortunately, a general and sophisticated MS model is presently unavailable. The aim of the study is to explore the effective thermal-mechanical material properties of a novel nanocomposite through theoretical analysis and experimental testing. The motivation behind the investigation arises from both its technological importance and extraordinary material properties aforementioned.

From literature, many extensive studies have been reported on the exploration of material properties of various metal nanowires (see, e.g. [11,12]). Relatively, little attention has been given to the study of Co metal [13,14], and in addition, most of their focus is primarily on the investigation of its magnetic properties. Thus, the investigation starts from the theoretical and experimental assessments of the elastic properties of the nanoscale Co wires using MD simulations and nanoindentation testing. The modeled and experimental results in terms of elastic modulus are compared

---

* Corresponding author. Tel.: +886 4 24527162; fax: +886 4 24510862.
E-mail address: hccheng@fcu.edu.tw (H.-C. Cheng).

0266-3538/$ - see front matter © 2008 Elsevier Ltd. All rights reserved.
doi:10.1016/j.compscitech.2008.09.030

with each other. Moreover, the size dependence of the material properties is also evaluated, mainly due to surface effects. For evaluating the effective material properties of the nanocomposite, an effective continuum approach based on 3D elasticity and FEM is established over a range of nanowire-volume fractions. In addition, a simplified analytical estimate based on mechanics of materials is also proposed for determining the effective axial CTE. The obtained results are compared with those derived using the proposed analytical model and two conventional theoretical approaches – the rule-of-mixture (ROM) technique (see, e.g. [15]) and the simplified analytical estimates [16–18]. Experimental verifications of the proposed FEM-based approach in terms of axial elastic modulus are also carried out using (1) nanoindentation experiment and (2) static uniaxial compression testing.

## 2. The fabrication process of the nanowire-based composite
A polymer-based composite reinforced by thousands of millions of highly oriented, arrayed Co nanowires is considered as test vehicle of the investigation. The nanocomposite is fabricated through the template assisted nanowire growth technique [2] with an AAO template, followed by a polymer-diffusion process under a magnetic field [19] to make sure nanowires stay in an upright orientation. The particular template is made by Whatman Co and comprises nanopores of about 200.0 nanometers (nm) in diameter, 30.0 µm in length and 50.0 nm in spacing. The nanopores where the nanowires are deposited yield a volume fraction ($\zeta$) of 50% of the total template's cross-section area. The fabrication process of the Co-nanowire-reinforced polymer composite is schematically plotted in Fig. 1. For electrical conduction, a thin Au seed layer is deposited onto one side of the AAO template, and then Co metal is electrodeposited onto the Au seed layer within the nanopores of the AAO template. As soon as the electrodeposition of Co nanowires is completed, the AAO template is removed under a magnetic field, followed by a polymer-diffusion process of a low viscous polyimide into the gaps among nanowires as matrix. After the curing process, laser ablation is performed to eliminate excessive polymer resulted from the polymer filling process. At last, surface regularity is further improved with fine polish in order to meet the high surface-regularity demand of nanoindentation testing.

The nanocomposite comprises a dimension of 30.0 µm in thickness and 1.0 centimeter (cm) in diameter. A scanning electron microscope (SEM) picture of the cross-section of the nanocomposite, after laser ablation and mounting on a 600.0 µm thick substrate, are also presented in Fig. 1f. It is evident that the polymer is well fitted to the gaps among nanowires, and besides, no bubbles or cracks are observed.

![](./images/811900963106324480_1.jpg)

Fig. 1. A schematic plot of the fabrication process of the nanowire-based composite.

## 3. MD simulations
For Co metal, the primary energetically favorable atomic structure is arranged in an HCP (Hexagonal Close-Packed) unit cell. The side dimension of a hexagonal base is 2.507 Å. By assembly of the unit cell, a Co nanowire with an HCP structure is constructed. Based on the continuum mechanics assumption, the axial elastic modulus and Poisson's ratio of a Co nanowire can be derived through a uniaxial tension test.

In the investigation, the embedded-atom method (EAM) (e.g. [20]) is adopted to model the atomistic interactions among Co atoms. The method has been successfully applied to simulate the structure, surface and phase transformation of solid or liquid metals [21,22]. The calculated results from MD simulations are discrete; thus, the definition of stress under the continuum mechanics assumption would not be quite adequate for use in this study. In measuring stresses on atoms, the smoothed particle hydrodynamics (SPH) technique (Shen and Atluri [23]) is applied in the investigation.

## 4. Effective modeling of the nanocomposite
The equivalent thermal-mechanical material properties of the nanocomposite that is a binary material composed of a huge number of nanowires (over 400,000,000) embedded in a polymer matrix are evaluated using an effective approach. It can be considered as a composite structure with a periodical array of microstructures, each of which comprises one metal nanowire and partial polymer matrix (i.e., PI). These periodic microstructures are termed here "repetitive local structures" (RLSs). At both global and local scale, the nanocomposite as well as the RLSs possesses transverse isotropy, where material properties along the fiber (axial) direction are different from those of the transverse. In principle, the effective material properties of an RLS, as shown in Fig. 2, can represent those of the nanocomposite. Hence, the effective material properties of the Co-nanowire-based nanocomposite are evaluated using an RLS based on several theoretical approaches, including the currently proposed approach, which is termed the FEM-based approach, and analytical model, existing analytical methods [16–18], and the widely used ROM technique. It should be noted that in the derivation, both Co-nanowires and PI matrix are assumed isotropic.

### 4.1. The FEM-based approach
In assessing the effective material properties of the RLS by using the ROM technique and existing analytical models, simplifying assumptions are generally necessary due to their incapabil-

![](./images/811900963106324480_2.jpg)

Fig. 2. The axial thermal deformation of the RLS under an isothermal loading.

ity of dealing with either the multiaxiality of the micro-fields in the matrix and fiber or the micro-scale variations of the strains and stresses. In other words, these assessments would rely on the accuracy of their estimations of the thermal-mechanical re- sponses of the RLS or the continuously reinforced, unidirectional nanocomposite.

To ease the difficulty, a FEM-based approach is proposed. It is essentially an iterative process toward deriving the effective prop- erties of the RLS. The basic idea behind the approach is that the amount of heat or thermal-mechanical behaviors of the RLS when subjected to an external loading must be equivalent to those of the original one. The generalized Hooke's law relating stresses to strains for a transversely isotropic material can be rewritten in the following in terms of a matrix form:

$$
\varepsilon_{x}=\sigma_{x} / E_{x, y}-v_{x y} \sigma_{y} / E_{x, y}-v_{x z} \sigma_{z} / E_{z},\qquad(1)
$$

$$
\varepsilon_{y}=-v_{x y} \sigma_{x} / E_{x, y}+\sigma_{y} / E_{x, y}-v_{x z} \sigma_{z} / E_{z},\qquad(2)
$$

$$
\varepsilon_{z}=-v_{x z} \sigma_{x} / E_{x, y}-v_{x z} \sigma_{y} / E_{x, y}+\sigma_{z} / E_{z},\qquad(3)
$$

$$
\gamma_{y z}=\tau_{y z} / G_{y z},\qquad(4)
$$

$$
\gamma_{z x}=\tau_{z x} / G_{z x},\qquad(5)
$$

$$
\gamma_{x y}=\tau_{x y} / G_{x y},\qquad(6)
$$

and

$$
G_{x y}=\frac{E_{x, y}}{2\left(1+v_{x y}\right)},\qquad(7)
$$

where $\sigma_{x}$ denotes stress, strain and $v$ Poisson's ratio. The effective transverse and axial elastic moduli $(E_{x, y}, E_{z})$ can be obtained by solv ing Eq. (1), (2), (3), and (6), if the relationship of the normal stresses $(\sigma_{x}, \sigma_{y}, \sigma_{z})$ and normal strains $(\varepsilon_{x}, \varepsilon_{y}, \varepsilon_{z})$ and that of the shear stress $\tau_{x, y}$ and strain $\gamma_{x y}$ can be known apriori. Essentially, they can be obtained from FE modeling. By imposing an external loading on the $x$-, $y$ - and $z$-planes, respectively, of the RLS, the relationship of the normal stress and strain at the $x$-, $y$ - and $z$-directions can be obtained. Furthermore, by imposing an external loading along the $x$-direction on the $y$-plane of the RLS, the relationship of the shear stress $\tau_{x y}$ and strain $\gamma_{x y}$ can be determined.

The effective CTE of the RLS can be computed by the following expression:

$$
\delta_{i}=\alpha_{i}(\Delta T) L \quad(i=x, y, z),\qquad(8)
$$

where $\delta_{i}$ and $\alpha_{i}$ are the thermal deformation and effective CTE along the $i$-th direction, $\Delta T$ the temperature change, and $L$ the length of the RLS. If the associated elongations and the temperature change are known, the in-plane effective transverse $\alpha_{x, y}$ and out-of-pane CTE $\alpha_{z}$ can be calculated, respectively.

To deal with the effective thermal conductivity, the Fourier's law is applied, where the heat flux along the transverse direction of the RLS can be expressed as

$$
q_{x, y}=-k_{x, y} \frac{\partial T}{\partial d}.\qquad(9)
$$

Accordingly, the effective transverse thermal conductivity can be written as

$$
k_{x, y}=\frac{Q_{x, y}}{L \Delta T_{T}}.\qquad(10)
$$

Likewise the effective axial thermal conductivity can be also de- rived as

$$
k_{z}=\frac{L Q_{z}}{d^{2} \Delta T_{L}},\qquad(11)
$$

where $Q_{x, y}$ and $Q_{z}$ denotes the total heat flux on the $x(y)$-plane and the $z$-plane, $d$ and $L$ the width and length of the RLS, and $\Delta T_{T}$ and $\Delta T_{L}$ the temperature difference between two sides along the trans- verse direction and along the axial direction, respectively. The calculation procedure is briefed as follows. First impose a tempera- ture difference at the two parallel surfaces of the RLS while setting the remaining surfaces adiabatic. Then the resultant heat flux at one of the surfaces is calculated using an FEM. By substituting the calcu- lated resultant heat flux into Eqs. (10) and (11), respectively, the effective CTEs are obtained.

### 4.2. The analytical estimates

Since the ROM technique can provide an exact effective axial elastic modulus $E_{z}$ and thermal conductivity $k_{z}$ along the axial direction for this particular, transversely isotropic material, the analytical derivations are performed only for the effective trans- verse elastic modulus $E_{x, y}$, transverse thermal conductivity $k_{x, y}$ and CTEs $(\alpha_{z}$ and $\alpha_{x, y})$ along the axial and transverse directions.

Based on mechanics of materials, the equivalent axial CTE $\alpha_{z}$ can be derived as a function of the nanofiber-volume fraction $\xi$ in the RLS. When subjected to an isothermal loading, the RLS will under- take both axial and transverse thermal expansions. For conve- nience, we assume that the transverse strain on the RLS is zero when deriving the effective axial CTE. The thermal deformations of the matrix $\delta_{PI}$ and nanowire $\delta_{nw}$ under a temperature change $\Delta T$ can be expressed in Eq. (8).

When the matrix and metal nanowire are perfectly bonded, the matrix under elevated isothermal temperature would be sub- jected to compression $F_{PI}$ due to the restraint of the nanowire while the metal nanowire would experience tension $F_{Co}$ . Based on mechanics of materials, the amount of the shrinkage of the matrix $\delta_{PI}^{Shrinkage}$ and the elongation of the nanowire $\delta_{Co}^{Elongation}$ can be expressed in terms of the compression and tension, respectively. According to Fig. 2, the following relationship is observed:

$$
\delta=\delta_{\mathrm{PI}}-\delta_{\mathrm{PI}}^{\text {Shrinkage }}=\delta_{\mathrm{Co}}+\delta_{\mathrm{Co}}^{\text {Elongation }}.\qquad(12)
$$

Eq. (12) can be also written as

$$
\frac{F_{\mathrm{PI}} L}{E_{\mathrm{PI}} A_{\mathrm{PI}}}+\frac{F_{\mathrm{Co}} L}{E_{\mathrm{Co}} A_{\mathrm{Co}}}=\alpha_{\mathrm{PI}}(\Delta T) L-\alpha_{\mathrm{Co}}(\Delta T) L,\qquad(13)
$$

where $A_{PI}$ and $A_{Co}$ stand for the cross-sectional area of the matrix and nanowire, respectively, and the total cross-section area $A=A_{PI}+A_{Co}$ . Since there is no external mechanical loading on the structure, the sum of the compressive and tensile forces imposed,

respectively, on the matrix and nanowire should be null, resulting
in the following relation:

$$
F_{\mathrm{Co}}=F_{\mathrm{Pl}}=\frac{\left(\alpha_{\mathrm{Pl}}-\alpha_{\mathrm{Co}}\right)(\Delta T) E_{\mathrm{Co}} A_{\mathrm{Co}} E_{\mathrm{Pl}} A_{\mathrm{Pl}}}{E_{\mathrm{Co}} A_{\mathrm{Co}}+E_{\mathrm{Pl}} A_{\mathrm{Pl}}}, \tag{14}
$$

Furthermore, the relation of axial loading and deformation gives
the resultant deformation of the RLS,

$$
\delta=\frac{\left(\alpha_{\mathrm{Co}} E_{\mathrm{Co}} A_{\mathrm{Co}}+\alpha_{\mathrm{Pl}} E_{\mathrm{Pl}} A_{\mathrm{Pl}}\right)(\Delta T) L}{E_{\mathrm{Co}} A_{\mathrm{Co}}+E_{\mathrm{Pl}} A_{\mathrm{Pl}}}, \tag{15}
$$

Accordingly, the effective axial CTE can be expressed as

$$
\alpha_{z}=\frac{\alpha_{\mathrm{Co}} E_{\mathrm{Co}} A_{\mathrm{Co}}+\alpha_{\mathrm{Pl}} E_{\mathrm{Pl}} A_{\mathrm{Pl}}}{E_{\mathrm{Co}} A_{\mathrm{Co}}+E_{\mathrm{Pl}} A_{\mathrm{Pl}}}, \tag{16}
$$

Since $A_{\mathrm{Co}} / \breve{A}=\xi$ and $A_{\mathrm{Pl}} / \breve{A}=1-\xi$, Eq. (16) can be rewritten
as

$$
\alpha_{z}=\frac{\alpha_{\mathrm{Co}} \xi E_{\mathrm{Co}}+\alpha_{\mathrm{Pl}}(1-\xi) E_{\mathrm{Pl}}}{\xi E_{\mathrm{Co}}+(1-\xi) E_{\mathrm{Pl}}}. \tag{17}
$$

where $E_{\mathrm{Co}}$ ($E_{\mathrm{Pl}}$) and $\alpha_{\mathrm{Co}}$ ($\alpha_{\mathrm{Pl}}$) are the elastic modulus and CTE of Co
metal (PI matrix), respectively. Eq. (17) gives exactly the same
equation as that of Schapery [17]. Furthermore, the effective trans-
verse CTE expression given in [17] derived using an energy ap-
proach, the approximate effective transverse elastic modulus
presented in [16] obtained from an available elasticity solution for
multiple-inclusion problems, and the approximate effective trans-
verse thermal conductivity provided in [18] derived based on an
effective-medium approach analogous to the well-known self-con-
sistent method are employed for comparison.

## 5. Experimental testing

### 5.1. Nanoindentation testing

In the investigation, the nanoindentation measurement tech-
nique is applied to evaluate the longitudinal elastic modulus of
the nanocomposite so as to verify the predicted, theoretical data.
To perform imaging and nanoindentation testing, a nanoindenta-
tion system incorporating with an atomic force microscope
(AFM) is applied. It is a Hysitron Triboscope nanoindentation sys-
tem equipped with a three-sided pyramid Berkovich diamond tip
with a tip radius 150.0 nm. The force and displacement resolutions
are about 1.0 nN and 0.04 nm, respectively. In addition, an SEM is
applied to examine the surface roughness of the nanocomposite.
Prior to the experiment, the shape of the indentor tip is calibrated
by a standard quartz specimen. To examine whether the testing is
made at the anticipated area, post-test imaging is performed. In-
situ indents are then carried out under force control mode, and
the associated indent profiles are imaged using the same tip soon
after indentation.

### 5.2. Uniaxial compression testing

We also present the axial elastic modulus of the nanocomposite
derived using static uniaxial compression testing in order to further
validate the results of the nanoindentation testing and theoretical
analysis. In the testing, a micro-tester, Instron 8848, is responsible
for the compression test. The dimension of the nanocomposite
specimen is $6.75 \times 6.75 \times 0.030\ \mathrm{(mm^3)}$. The micro-tester equipped
with a 2.0 mm diameter circular flat punch carries out the measure-
ment by compressing a much larger area of the nanocomposite
rather than just a single nanowire or avery tiny indented area as
nanoindentation testing. During the compression progress, the
force-displacement relationship is recorded. By the slope of the
force-displacement curve, the effective axial elastic modulus of
the nanocomposite can be calculated.

## 6. Results and discussions

### 6.1. Experimental testing

#### 6.1.1. Nanoindentation testing

The elastic modulus and hardness of the Co nanowire and
nanocomposite film along the axial direction are probed with
nanoindentation and in-situ AFM. To ease measurement uncer-
tainty, a total of seven nanoindentation experiments at randomly
selected locations are attempted when characterizing the effec-
tive elastic modulus of the nanocomposite. The arithmetic mean
value of these seven measurement results and the associated
standard deviation are presented. On the other hand, only one at-
tempt is made when exploring that of the Co nanowire due to the
difficulty in precisely aligning the indent tip with the nanowire.
Fig. 3a shows a 3D AFM scanning image of an indent mark on
the nanocomposite film, and Fig. 3b presents that on the nano-
wire, where the indentation is clearly made right on the top
surface of a Co nanowire.

Fig. 4a illustrates the force-displacement curve of the nanoin-
dentation of the Co nanowire, where the peak compressive force
is about 100 $\mu$N and the peak depth is 23.4 nm. The reduced mod-
ulus $E_{\mathrm{r}}$ in accordance with Fig. 4a is about 183.2 GPa, which corre-
sponds to an elastic modulus of 191.4 GPa, and the hardness is
about 5.2 GPa. The literature data for the bulk Co metal is about
211.0 GPa (http://www.matweb.com), which is slightly larger than
that of the Co nanowire. Furthermore, an example of the force-dis-
placement curves of the nanoindentation of the nanocomposite is
shown in Fig. 4b, where the average peak compressive force is
about 4000 $\mu$N and the average peak depth is approximately
180.0 nm. The arithmetic mean value of the axial elastic modulus
of the seven measurement attempts together with the associated
standard deviation is $117.4 \pm 9.7$ GPa, and that of the hardness
and the associated standard deviation is $5.9 \pm 0.9$ GPa.

#### 6.1.2. Static uniaxial compression testing

Results show that there is a linear relationship between the
compressive load and deflection in the static uniaxial compression
testing of the nanocomposite. To lessen measurement uncertainty,
a total of five uniaxial compression experiments at randomly
selected locations are performed in the investigation. The arithme-
tic mean value of these five measurement results and the associ-
ated standard deviation are used to indicate the effective axial
elastic modulus of the nanocomposite. It is found that the effective
elastic modulus along the axial direction is $104.4 \pm 11.3$ GPa. By
comparing the result with that of the nanoindentation experiment
(i.e., $117.4 \pm 9.7$ GPa), as much as about 11% discrepancy can be
detected.

![](./images/811900963106324480_3.jpg)

Fig. 3. A 3D AFM scanning image of indent mark on (a) the nanocomposite film and
(b) the nanowire.

![](./images/811900963106324480_4.jpg)

(a) Co nanowire

![](./images/811900963106324480_5.jpg)

(b) Nanocomposite

Fig. 4. An example of the force-displacement curves by the nanoindentation testing.

### 6.2. MD simulations

#### 6.2.1. Elastic modulus of the co nanowire
Due to the lost of some neighbor atoms and the fracture of some atomic bonding for the atoms near the surfaces, these atoms would hold some self-balancing motion without any external force. The self-balancing stress of the nanowire is calculated based on the atomistic-level stress definition [23]. An example of stress distribu- tion $\sigma_{zz}$ on the cross-section of the Co nanowire at the free relaxa tion state is presented in Fig. 5. One can easily observe that there is a significant stress gradient across the cross-section: the closer to the free surface of the nanowire, the larger the stress. Overall, it presents tension near the free surface and compression or zero at the central area of the cross-section. The magnitude of the self-bal- ancing stress is quite remarkable and should not be neglected in the modeling. More importantly, the material with a nanoscale and high area-to-volume ratio can not be considered as homoge- neous. The result trend is quite consistent with that presented in [12] for a copper nanorod. The self-balancing stress state is used as a preload for subsequent MD characterizations of the elastic material properties of the Co metal.

The computational models for exploring the elastic modulus of the Co metal assume a fixed geometric aspect ratio with an identi- cal side dimension. In other words, they are all cubic hexagons comprising an equivalent number of unit HCP structures at all three directions. Fig. 6a presents the modeled axial elastic moduli as a function of the side dimension of the Co cubic hexagons. When the geometric aspect ratio is fixed, the elastic modulus monotoni- cally decreases with the increase of side dimension, and eventu- ally approaches a limit (i.e., 208.0 GPa) as the dimension exceeds approximately 6.0 nm. The convergent limit is comparable with the bulk value. By further comparing it with the nanoindentation data (i.e., 191.4 GPa), a difference about 8-9% is noticed. The devi- ation is probably due to that there is a certain amount of voids in the specimen, making the strength of the CO metal weaker. More- over, the estimated Poisson's ratios of various Co cubic hexagons are shown in Fig. 6b. The Poisson's ratio monotonically increases with an increasing side dimension of the cubic hexagon, and even- tually converges to a constant value 0.355 as the side dimension attains 5.0 nm. The convergent data is fairly consistent with the bulk value 0.32.

![](./images/811900963106324480_6.jpg)

Fig. 5. The stress distribution of an unstrained cobalt nanowire.

#### 6.2.2. Axial elastic modulus of the nanocomposite
The calculated results from the proposed FEM-based approach, the ROM technique, and the analytical estimates are presented in Fig. 7-10, as a function of the volume fraction of the embedded nanowire. In addition, the measured axial elastic modulus by the nanoindentation and uniaxial compression experiments at a nano- fiber-volume fraction 50% is also illustrated in Fig. 7a. As can be seen in Fig. 7a, the derived effective axial elastic modulus of the nanocomposite by the FEM-based method (i.e., 105.0 GPa) follows closely with that of the ROM technique (i.e., 105.5 GPa). Moreover, these two theoretical estimates also agree extremely well with that of the uniaxial compression testing (104.4 ± 11.3 GPa). When further compared with the result of the nanoindentation experi- ment (i.e., 117.4 ± 9.7 GPa), there is a slightly increasing discrep- ancy between the theoretical results and the nanoindentation. However the differences remain marginal. The comparisons reveal the validity of the proposed FEM-based approach and even the ROM technique for exploring the effective axial elastic modulus of the fiber-based nanocomposite.

It is interesting to find from Figs. 7 and 9 that for the transversely isotropic nanocomposite, the effective axial elastic moduli and ther- mal conductivities are always larger than the corresponding trans- verse ones, while the effective axial CTEs constantly smaller than the associated transverse ones. In addition, there is a very compara- ble effective Poisson's ratio along both the axial and transverse direc- tions. Furthermore, Fig. 7a shows that there is a linear monotonic dependence of the axial elastic modulus on the nanofiber-volume fraction. A similar trend can be also detected in Poisson's ratio (Fig. 8a) and thermal conductivity (Fig. 9a). On the other hand, the

![](./images/811900963106324480_7.jpg)

Fig. 6. The elastic material properties of the Co cubic hexagons versus the side dimension.

![](./images/811900963106324480_8.jpg)

Fig. 7. The effective elastic moduli versus volume ratio of the nanowires.

![](./images/811900963106324480_9.jpg)

Fig. 8. The effective Poisson's ratio versus volume ratio of the nanowires.

axial CTE (Fig. 10a) and the transverse material properties (Figs. 7b-10b) tend to have a nonlinear proportion to the nanofiber-volume fraction, where it even presents a nonlinear, nonmonotonic depen-

dence of the transverse CTE on the nanofiber-volume fraction. The transverse CTE increases with the nanofiber-volume fraction as it is less than about 10%, and becomes a totally opposite trend as it is

![](./images/811900963106324480_10.jpg)

![](./images/811900963106324480_11.jpg)

Fig. 9. The effective thermal conductivities versus volume ratio of the nanowires.

![](./images/811900963106324480_12.jpg)

![](./images/811900963106324480_13.jpg)

Fig. 10. The effective CTE versus volume ratio of the nanowires.

beyond that. This indicates that the ROM technique can be a robust and effective mean only when there is a "linear-like" relationship between the nanofiber-volume fraction and the estimated material properties. It is especially so for axial elastic modulus, Poisson's ratio and thermal conductivity but not for the axial CTE and the transverse elastic modulus, thermal conductivity and CTE. Remarkably, as much as 175% difference in the effective axial CTE between the FEM-based and the ROM approaches can be perceived.

The effective elastic modulus and thermal conductivity along both the axial and transverse directions increase with an increasing nanofiber-volume fraction while the effective Poisson's ratios in both directions and axial CTE exhibit oppositely. This is probably due to that the Co nanowire possesses a larger material stiffness and thermal conductance than the polymer matrix but a smaller Poisson's ratio and CTE than the matrix. Moreover, the results obtained from the proposed FEM-based method can have a very good match with those derived by the analytical estimates over a wide range of the nanofiber-volume fraction.

### 7. Conclusions
The MD simulation shows that there is an extraordinary size-dependent elastic modulus and Poisson's ratio of the nanoscale Co metal. An increasing side dimension of the nanoscale Co metal would decrease the elastic modulus but increase the corresponding Poisson's ratio. This is mainly due to the remarkable increase of the surface area-to-volume ratio as the size of materials is reduced down to nanoscale. The surface effect would also lead to a considerable self-balancing tensile normal stress $(\sigma_{zz})$ across the cross-section of the nanowire at free relaxation state, suggesting that the material properties of 1D wires with nanoscale do not appear homogeneous. Essentially, the degree of inhomogeneity increases with a decreasing dimension of nanomaterials. Moreover, the modeled elastic modulus of the Co nanowire by MD simulations (i.e., 208.0 GPa) agrees well with its bulk data (211.0 GPa), but shows a slightly larger difference with the measured (i.e., 191.4 GPa.). The observed discrepancy (8-9%) between the experimental and theoretical data might be due to a possible certain amount of voids in the specimen.

It is also found that the Co filament plays an important role in the thermal-mechanical properties of the nanocomposites. A very good agreement in the effective axial elastic modulus has been found between the theoretical and experimental predictions. Furthermore, the obtained results by using the proposed FEM-based method are consistent with those derived from existing analytical estimates and the proposed analytical model for the effective axial

CTE. The results also reveal that the widely used ROM technique can be a robust and effective tool in assessing the effective axial material properties, mainly because they present a "linear-like" relationship with the nanofiber-volume fraction. For the transversely isotropic nanocomposite, the effective axial elastic moduli and thermal conductivities are greater than the corresponding transverse ones over the range of nanofiber-volume fraction; on the other hand, for the effective CTE, the axial ones become less than the associated transverse. More surprisingly, the nanocomposites consist of an equivalent Poisson's ratio along the axial and transverse directions. Besides, the degree of anisotropy in the derived effective elastic modulus and thermal conductivity as a result of the Co filament turns out to be much more considerable than that of the effective Poisson's ratio and CTE.

## Acknowledgment
The authors are grateful to the National Science Council, Taiwan, R.O.C., under grants NSC95-2221-E-035-018-MY3 and NSC95-2221-E-007-013-MY3 for the partial financial supports of this work.

## References
[1] Chen WH, Cheng HC, Hsu YC. Mechanical properties of carbon nanotubes using molecular dynamics simulations with the inlayer van der Waals interactions. Comp Model Eng Sci 2007;20:123-45.
[2] Morales AM, Lieber CM. A laser ablation method for the synthesis of crystalline semiconductor nanowires. Science 1998;279:208-11.
[3] Yin AJ, Li J, Jian W, Bennett AJ, Xu JM. Fabrication of highly ordered metallic nanowire arrays by electrodeposition. Appl Phys Lett 2001;79:1039-41.
[4] Lin YM, Rabin O, Cronin SB, Ying JY, Dresselhaus MS. Semimetal-semiconductor transition in $Bi_{1-x}Sb_x$ alloy nanowires and their thermoelectric properties. Appl Phys Lett 2002;81:2403-5.
[5] Cho J, Luo JJ, Daniel IM. Mechanical characterization of graphite/epoxy nanocomposites by multi-scale analysis. Compos Sci Technol 2007;67:2399-407.
[6] Kanagaraj S, Varanda FR, Zhil'tsova TV, Oliveira MSA, Simoes JAO. Mechanical properties of high density polyethylene/carbon nanotube composites. Compos Sci Technol 2007;67:3071-7.
[7] Zhang J, Wu T, Wang L, Jiang W, Chen L. Microstructure and properties of $Ti_3SiC_2$/SiC nanocomposites fabricated by spark plasma sintering. Compos Sci Technol 2008;68:499-505.
[8] Ashrafi B, Hubert P. Modeling the elastic properties of carbon nanotube array/polymer composites. Compos Sci Technol 2006;66:387-96.
[9] González C, LLorca J. Mechanical behavior of unidirectional fiber-reinforced polymers under transverse compression: microscopic mechanisms and modeling. Compos Sci Technol 2007;67:2795-806.
[10] Frankland SJV, Harik VM, Odegard GM, Brenner DW, Gates TS. The stress-strain behavior of polymer-nanotube composites from molecular dynamics simulation. Compos Sci Technol 2003;63:1655-61.
[11] Branicio PS, Rino JP. Large deformation and amorphization of Ni nanowires under uniaxial strain: a molecular dynamics study. Phys Rev B 2000;62:16950-5.
[12] Wu HA. Molecular dynamics simulation of loading rate and surface effects on the elastic bending behavior of metal nanorod. Comput Mater Sci 2004;31:287-91.
[13] Cho JU, Wu JH, Min JH, Ko SP, Soh JY, Liu QX, et al. Control of magnetic anisotropy of Co nanowires. J Magn Magn Mater 2006;303:e281-5.
[14] Yuan J, Pei W, Hasagawa T, Washiya T, Saito H, Ishio S, et al. Study on magnetization reversal of cobalt nanowire arrays by magnetic force microscopy. J Magn Magn Mater 2008;320:134-9.
[15] Boresi PB, Chong KP. Elasticity in engineering mechanics. New York: John Wiley & Sons Inc.; 2000.
[16] Whitney JM. Elastic moduli of unidirectional composites with anisotropic filaments. J Compos Mater 1967;1:188-93.
[17] Schapery RA. Thermal expansion coefficients of composite material based on energy principles. J Compos Mater 1968;2:380-404.
[18] Markworth AJ. The transverse thermal conductivity of a unidirectional fiber composite with fiber-matrix debonding: a calculation based on effective-medium theory. J Mater Sci Lett 1993;12:1487-9.
[19] Lin RJ, Hsu YY, Fan RC, Chen YC, Cheng SY, Huang CT, Uang RH. Design of nanowire anisotropic conductive film for ultra-fine pitch flip chip interconnection. Electronics packaging technology conference. Singapore: IEEE; 2004. pp. 120-5.
[20] Pasianot R, Savino EJ. Embedded-atom-method interatomic potentials for hcp metals. Phys Rev B 1992;45:12704-10.
[21] Wang G, Strachan A, Cagin T, Goddard III WA. Molecular dynamics simulations of 1/2 <111> screw dislocation in Ta. Mater Sci Eng A 2001;309-310:133-7.
[22] Han XJ, Wang JZ, Chen M, Guo ZY. Molecular dynamics simulation of thermophysical properties of undercooled liquid cobalt. J Phys Condes Matter 2004;16:2565-74.
[23] Shen S, Atluri SN. Atomic-level stress calculation and continuum-molecular system equivalence. Comp Model Eng Sci 2004;6:91-104.