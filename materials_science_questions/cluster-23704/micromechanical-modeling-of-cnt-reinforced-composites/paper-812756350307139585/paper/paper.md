# Micromechanics of CNT grafted FRP based on hierarchical homogenization of transversely isotropic multi-coated model

Yi Cheng $^{a}$, Kaifu Zhang $^{a,*}$, Biao Liang $^{a}$, Hui Cheng $^{a}$, Guoyi Hou $^{a}$, Guanhua Xu $^{a}$, Wei Jin $^{b}$

$^{a}$ The Ministry of Education Key Lab of Contemporary Design and Integrated Manufacturing Technology, Northwestern Polytechnical University, Xi'an 710072, China
$^{b}$ AVIC xi'An Aircraft Industry(Group) Company LTD., Xi'an 710089, China

---

## ARTICLE INFO

**Keywords:**
CNT grafted FRP
Hierarchical modeling
Homogenization
Effective modulus

---

## ABSTRACT

Carbon nanotube grafted fiber reinforced polymer possesses promising mechanical properties compared to traditional fiber reinforced composites. A micromechanical model was developed to predict effective properties of the composite in this paper. At first, hierarchical models were conducted to represent CNT region and the whole composite separately. The CNT region was homogenized in micro-scale and regarded as functionally graded interphase surrounding fibers. The whole composite was simulated by a multi-coated model embedded into a transversely isotropic medium in meso-scale. To solve the multi-coated model, strain concentration tensors for each phase were obtained and incorporated into a sequentially homogenization method. Then the algorithm was implemented using MATLAB software to obtain effective moduli of the composite. The results were verified by FEM simulations and experimental results from existing literatures. In the end, effects of modulus, volume fraction and length of the CNTs on overall properties of the composite were studied.

---

### 1. Introduction

Carbon nanotubes (CNTs), with their noteworthy mechanical properties [1,2], are attractive candidates for enhancing mechanical properties of fiber reinforced polymer (FRP). By acting as "bridges" to inter-fiber domains, these nano-filaments show great promises in improving imperfect interface and poor transverse modulus of the FRPs. A variety of processes were conducted to incorporate the CNTs into the composites. Among all these methods, anchoring CNTs onto fabric material was an attractive approach to tailor the FRPs. They were usually achieved by chemical vapor deposition (CVD) [3], chemical grafting [4], electrospray techniques [5] and suspension deposition [6]. These kind of composites were called CNT grafted FRPs (CG-FRP) [7,8], fuzzy fiber composites [9] or CNT forests [10]. Plenty of experiments had already validated their effectiveness in enhancing mechanical properties of the composites, such as tensile elastic modulus [11], flexural elastic modulus [12], interlaminar shear stress (ILSS) [13], fracture toughness [14,15], energy absorption [16].

Detecting mechanism on enhancing of the composites attracted great attentions from researchers [17]. Apart from experimental methods, multi-scale modeling [18,19] was an efficient approach to estimate overall properties of the CNT-reinforced composites. Most multi-scale models involved Molecular dynamic (MD) simulation [20] or micromechanical modeling [21]. The MD simulation was conducted to obtain molecular-level properties, while the micromechanical model was used in higher scale level. The micromechanical models included Bridging Cell Method (BCM) [22], rule of mixture (ROM) [24], generalized method of cells (GMC) [25], Equivalent Single Layer (ESL) approaches [26], continuum micromechanics based approach [27], Halpin-Tsai (H-T) [28], Voigt-Reuss (V-R) methods [29,30] and generalized differential quadrature method (GDQM) [31]. However, objectives for most of the methods were randomly distributed CNTs and parameters studied were volume fraction, aspect ratio [32], agglomeration [33] and waviness [34] of the CNTs. It was found that the experimental results were still far below the ideal theoretical predictions.

In the above models, randomly distributed CNT reinforced polymer was often homogenized as an equivalent isotropic matrix with uniform properties [23]. However the CG-FRP requires distinguished micromechanical models due to its special microstructures. The CNTs in the CG-FRP are aligned regularly around and only around the fibers. So it can be concluded that polymer was reinforced in radical direction of fibers [35-37]. Bernard K. [38] described amount of CNTs on per unit area of fabric material as areal density of CNT. M.K. [39] proved that increasing of volume fraction/ length and decreasing of diameter of the CNTs lead to significant improvements in thermo mechanical properties of carbon nanotube-fiber reinforced metal. Richard Li [40] found mechanical properties of the composites obtained by experiments coincided with predictions from Role of Mixture (ROM). Nithya Subramanian [41]

---

* Corresponding author.
E-mail address: zhangkf@nwpu.edu.cn (K. Zhang)

https://doi.org/10.1016/j.ijmecsci.2019.105014
Received 15 May 2019; Received in revised form 23 June 2019; Accepted 9 July 2019
Available online 10 July 2019
0020-7403/© 2019 Elsevier Ltd. All rights reserved.

![](./images/812756350307139585_1.jpg)
![](./images/812756350307139585_2.jpg)
![](./images/812756350307139585_3.jpg)

![](./images/812756350307139585_4.jpg)

a) SEM of CG-FRP⁽⁴⁵⁾

![](./images/812756350307139585_5.jpg)

b) Model of CG-FRP in [41]

![](./images/812756350307139585_6.jpg)

c) Modeling of CG-FRP in present paper

Fig. 1. Microstructure of CG-FRP and its simplifica- tion.

<table>
<caption>Table 1 Geometrical parameters of the CG-FRP.</caption>
<thead>
<tr>
<th>Constituents</th>
<td colspan="2">Fiber</td>
<td colspan="4">CNT</td>
</tr>
<tr>
<th>Geometrical parameters</th>
<td>Volume fraction</td>
<td>Radius</td>
<td>Volume fraction</td>
<td>Radius</td>
<td>Length</td>
<td>Area density</td>
</tr>
</thead>
<tbody>
<tr>
<th>Symbols</th>
<td>$V_{F}$</td>
<td>$r_{F}$</td>
<td>$V_{CN}$</td>
<td>$r_{CN}$</td>
<td>$l_{CN}$</td>
<td>$\rho_{CN}$</td>
</tr>
<tr>
<th>Ranges</th>
<td>0~70%</td>
<td>5~7 um</td>
<td>less than 5% [39]</td>
<td>1~35 nm [38]</td>
<td>0~2 um</td>
<td>6000~50,000[38] ($r_{CN}=1.357 nm$)</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Mechanical properties of fiber, CNT and polymer.</caption>
<thead>
<tr>
<th colspan="2">Carbon fiber</th>
<th colspan="2">CNT</th>
<th colspan="2">Polymer</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{FI}(Mpa)$</td>
<td>15,410</td>
<td rowspan="2">$E_{CN}(Mpa)$</td>
<td rowspan="2">700,000~1,000,000</td>
<td rowspan="2">$E_{M}(Mpa)$</td>
<td rowspan="2">2890</td>
</tr>
<tr>
<td>$E_{FT}(Mpa)$</td>
<td>230,000</td>
</tr>
<tr>
<td>$v_{FI}$</td>
<td>0.46</td>
<td rowspan="2">$v_{CN}$</td>
<td rowspan="2">0.3</td>
<td rowspan="2">$v_{M}$</td>
<td rowspan="2">0.3</td>
</tr>
<tr>
<td>$v_{FT}$</td>
<td>0.29</td>
</tr>
<tr>
<td>$G_{FI}(Mpa)$</td>
<td>10,040</td>
<td rowspan="2">$G_{CN}(Mpa)$</td>
<td rowspan="2"></td>
<td rowspan="2">$G_{M}(Mpa)$</td>
<td rowspan="2">1111</td>
</tr>
<tr>
<td>$G_{FT}(Mpa)$</td>
<td>25,000</td>
</tr>
</tbody>
</table>

proposed an atomistic modeling framework to investigate interface of composites with fuzzy fibers. M. K. [42] homogenized CNT region at first and claimed properties of the CNT region rolled around car- bon fiber were polar angle related. Mojtaba Haghgoo [43] and Y.P. Qiu [44] proposed a micromechanical model including transversely isotropic spheroidal inclusions.

Some problems were found in the existing models. As dimensions of fiber are in micrometer scale and dimensions of CNTs in nanometer scale, it is unrealistic to explicitly establish these two kinds of reinforce- ments into a single model. A common way to deal with this issue was to homogenize CNTs and fibers separately. However, most of current works failed to consider local volume fraction variations of the CNTs along radical direction of the fibers. Meanwhile, as the equivalent CNT region was transversely isotropic, it also caused difficulties in homoge- nization of the CG-FRP.

In summary, the grafted CNTs around fibers can enhance mechan- ical properties of the CG-FRP. However micromechanical modeling of the CG-FRP was challenging. In this paper, hierarchical models for the CG-FRP were developed to study influences of the CNTs on overall prop- erties of the CG-FRP. In the second section, the CNT region was simu- lated by cylindrical inhomogeneity embedded into isotropic matrix in micro-scale and homogenized as functionally graded interphase around the fibers. After division of the interphase, the CG-FRP was modeled by multi-coated cylindrical inhomogeneities embedded into transversely isotropic medium in meso-scale. In the third section, a sequentially ho- mogenization procedure was conducted to obtain its effective proper- ties. Furthermore the results were verified by finite element simulations and experimental results from existing literatures. In the end, influences of volume fraction, elastic modulus and length of the CNTs on overall properties of the CG-FRP were studied.

### 2. Hierarchical models of the CG-FRP

#### 2.1. General frameworks

##### 2.1.1. Constituents and physical mechanisms of the CG-FRP

After studying SEM pictures and models of the CG-FRP in [41] and [45], simplification of the CG-FRP in this paper is shown in Fig. 1. The simplified model contains continuous unidirectional fiber, radically aligned CNT filaments and polymer matrix. The CNTs are supposed to have the same radius and lengths. Effects of waviness and agglomeration of the CNTs are not investigated in this paper.

Geometrical parameters and mechanical properties of each con- stituent in the CG-FRP used in this paper are listed in Tables 1 and 2. All of these data come from existing literatures. The fiber and the polymer are treated as transversely isotropic and isotropic material with fixed properties, respectively. Based on analysis of [39], the CNTs are

<table>
<caption>Table 3
Engineering properties of transversely isotropic material.</caption>
<tbody>
<tr>
<td>Tensile
elastic modulus</td>
<td>Transverse
elastic modulus</td>
<td>In-plane
Poisson’s ratio</td>
<td>Out-plane
Poisson’s ratio</td>
<td>In-plane
shear modulus</td>
<td>Out-plane
shear modulus</td>
</tr>
<tr>
<td>![](./images/812756350307139585_7.jpg)</td>
<td>![](./images/812756350307139585_8.jpg)</td>
<td>![](./images/812756350307139585_9.jpg)</td>
<td>![](./images/812756350307139585_10.jpg)</td>
<td>![](./images/812756350307139585_11.jpg)</td>
<td>![](./images/812756350307139585_12.jpg)</td>
</tr>
<tr>
<td>$E_I$</td>
<td>$E_T$</td>
<td>$v_{II}$</td>
<td>$v_{TI}$</td>
<td>$G_I$</td>
<td>$G_T$</td>
</tr>
</tbody>
</table>

regarded as isotropic and their elastic modulus, volume fraction and length will be regarded as variables in following research.

Subscripts “F”, “CN” and “M” indicate the fiber, the CNT and the polymer, “I” and “T” indicate physical mechanisms related to axial di- rection and perpendicular direction, respectively. Similar to FRPs, the CG-FRP exhibits one symmetric axis. So it is reasonable to conclude that overall properties of the CG-FRP are transversely isotropic and its engi- neering properties are shown in Table 3.

### 2.1.2. Walpole’s scheme of fourth order tensors
Calculations of fourth order tensors, such as elastic tensors of trans- versely isotropic materials, strain concentration tensors, are often used in following sections. To this end, a Walpole’s scheme is adopted in op- erations of these tensors.

Based on the Walpole’s scheme, all fourth order tensors $T_{ijkl}$, satisfy- ing $T_{ijkl}=T_{jikl}=T_{ijlk}$, can be simplified as:
$$\boldsymbol{T}=(\boldsymbol{C}, \boldsymbol{G}, \boldsymbol{H}, \boldsymbol{D}, \boldsymbol{E}, \boldsymbol{F}) \tag{1}$$

Corresponding matrix form of the $T_{ijkl}$ is:
$$
\left[\begin{array}{cccccc}
\frac{1}{2}(C+E) & \frac{1}{2}(C-E) & H & & & \\
\frac{1}{2}(C-E) & \frac{1}{2}(C+E) & H & & & \\
G & G & D & & & \\
& & & F & & \\
& & & & F & \\
& & & & & E
\end{array}\right] \tag{2}
$$

For fourth order transversely isotropic tensors, relationship $H = G$ is satisfied. Addition/subtraction, inner product and inverse operation of two fourth-order tensors $T=(C, G, H, D, E, F)$ and $T'=(C', G', H', D', E', F')$ obey following rules:
$$\boldsymbol{T} \pm \boldsymbol{T}^{\prime}=\left(C \pm C^{\prime}, G \pm G^{\prime}, H \pm H^{\prime}, D \pm D^{\prime}, E \pm E^{\prime}, F \pm F^{\prime}\right) \tag{3}$$

$$
\boldsymbol{T} \cdot \boldsymbol{T}^{\prime}=\left(C C^{\prime}+2 H G^{\prime}, G C^{\prime}+D G^{\prime}, C H^{\prime}+H D^{\prime}, D D^{\prime}+2 G H^{\prime}, E E^{\prime}, F F^{\prime}\right)
\tag{4}
$$

$$
\boldsymbol{T}^{-1}=\left(\frac{D}{\Delta},-\frac{G}{\Delta},-\frac{H}{\Delta}, \frac{C}{\Delta}, \frac{1}{E}, \frac{1}{F}\right) \tag{5}
$$
where $\Delta=CD-2GH$. Furthermore, following equations are satisfied:
$$\boldsymbol{A} \cdot \boldsymbol{B} \cdot \boldsymbol{C}=\boldsymbol{A} \cdot(\boldsymbol{B} \cdot \boldsymbol{C}) \tag{6}$$

$$\boldsymbol{A} \cdot(\boldsymbol{B}+\boldsymbol{C})=\boldsymbol{A} \cdot \boldsymbol{B}+\boldsymbol{A} \cdot \boldsymbol{C} \tag{7}$$

$$\boldsymbol{A} \cdot \boldsymbol{B} \neq \boldsymbol{B} \cdot \boldsymbol{A} \tag{8}$$

Using the Walpole’s scheme, identical fourth order tensor $\boldsymbol{I}$, stiff- ness/flexible tensors of transversely isotropic materials $(\boldsymbol{C}_T/\boldsymbol{F}_T)$ and stiffness/flexible tensors of isotropic materials $(\boldsymbol{C}_I/\boldsymbol{F}_I)$ can be expressed as follows:
$$\boldsymbol{I}=(1,0,0,1,1,1) \tag{9}$$

$$
\boldsymbol{C}_{T}=\left(\frac{E_{I} E_{T}}{\Theta}, \frac{E_{I} E_{T} v_{T}}{\Theta}, \frac{E_{I} E_{T} v_{T}}{\Theta}, \frac{E_{T}^{2}\left(1-v_{I}\right)}{\Theta}, 2 G_{I}, 2 G_{T}\right)
\tag{10}
$$

$$
\boldsymbol{C}_{I}=\frac{E}{(1+v)(1-2 v)}(1, v, v,(1-v),(1-2 v),(1-2 v)) \tag{11}
$$

$$
\boldsymbol{F}_{T}=\left(\frac{1-v_{I}}{E_{I}},-\frac{v_{T}}{E_{T}},-\frac{v_{T}}{E_{T}}, \frac{1}{E_{T}}, \frac{1}{2 G_{I}}, \frac{1}{2 G_{T}}\right) \tag{12}
$$

$$
\boldsymbol{F}_{I}=\left(\frac{1-v}{E},-\frac{v}{E},-\frac{v}{E}, \frac{1}{E}, \frac{1+v}{E}, \frac{1+v}{E}\right) \tag{13}
$$
where $\Theta=E_T(1-v_I)-2E_Iv_T^2$.

### 2.2. Schematic procedures of hierarchical modeling
As shown in Table 1, dimensions of the fiber is much larger than those of the CNTs’. Effects of the fiber is non-negligible in modeling of the CNTs, so basic assumption of micromechanical modeling is not valid in trans-scale. Furthermore, mismatching on meshes exists in finite ele- ment simulation. To this end, a two-step hierarchical modeling method, containing micro-scale and meso-scale, is conducted.

#### 2.2.1. Schematic procedures on hierarchical modeling of CG-FRP
Schematic procedures on the hierarchical modeling of the CG-FRP are displayed in Fig. 2. At first, CNT region around the fiber is modeled as CNT reinforced polymer (CNRP) in micro-scale. Then the CNRP is ho- mogenized as transversely isotropic material by Mori-Tanaka method. Because of the variation of local volume fraction of the CNTs, properties of the CNT region is location related and regarded as functionally graded interphase in this paper. After division of the interphase, a multi-coated model is conducted. The model is solved by sequentially homogeniza- tion method.

As shown above, there are two coordinate systems in above figure. A global coordinate system based on the CG-FRP locates its origin at mid- dle of the fiber and is denoted as $X_1$-$X_2$-$X_3$. Without losing of generality, the $X_3$ is supposed to be the fiber direction. A local coordinate system based on the CNRP in micro scale is denoted as $x_1$-$x_2$-$x_3$. The $x_3$ axis is length of the CNT. Parameters based on these two coordinate systems are distinguished by superscript $GLO$ and $LOC$, respectively.

#### 2.2.2. Micro-scale modeling of CNRP
The CNT region can be divided into rings surrounding the fiber with same thicknesses. It is easy to conclude that volume of the CNTs in these rings are the same. However, with increment of radius of the rings, vol- ume of the rings will increase. Volume fractions of the CNTs in these rings are defined as local volume fraction of CNT, which is denoted as

![](./images/812756350307139585_13.jpg)

Fig. 2. Schematic procedures on hierarchical modeling of CG-FRP.

![](./images/812756350307139585_14.jpg)

Fig. 3. RVE of CN-RP in micro-scale.

![](./images/812756350307139585_15.jpg)

Fig. 4. Local volume fraction of CNTs.

$V_{CN}^{LOC}$. It can be concluded that $V_{CN}^{LOC}$ will decrease gradually along radial direction of the fiber. A RVE in the ring $r_x$ distance from the center is established in micro-scale in Fig. 3.

$V_{CN}^{LOC}$ can be expressed as:
$$
V_{C N}^{L O C}\left(r_{x}\right)=r_{C F} \rho_{C N} \pi r_{C N}{ }^{2} / r_{x}
\tag{14}
$$
where $r_x \in (r_{CF}, r_{CF}+l_{CN})$. The $V_{CN}^{LOC}$ with various geometrical parameters are displayed in Fig. 4. The various geometrical parameters are listed in Table 4. As shown in Fig. 4, the $V_{CN}^{LOC}$ decreases as large as 20% along $r_x$.

Based on Voigt or Reuss estimations, effective modulus of heterogeneous materials are proportional to volume fraction of their reinforcements. So it is reasonable to imply that effective properties of the CNRP are radical related and can be obtained by Mori-Tanaka scheme:
$$
\boldsymbol{C}_{C N R P}^{e f f}=\boldsymbol{C}^{\boldsymbol{M}}+V_{C N}^{L O C} \Delta \boldsymbol{C}^{\boldsymbol{C N} / \boldsymbol{M}}: \boldsymbol{A}^{\boldsymbol{C N}}:\left(1-V_{C N}^{L O C}+V_{C N}^{L O C} \boldsymbol{A}^{\boldsymbol{C N}}\right)^{-1}
\tag{15}
$$

<table>
<caption>Table 4<br>CG-FRP with various geometrical parameters.</caption>
<thead>
<tr>
<th>Case</th>
<th>$r_{CF}(\mu m)$</th>
<th>$\rho_{CN}$</th>
<th>$r_{CN}(nm)$</th>
<th>$l_{CN}(\mu m)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>①</td>
<td>7</td>
<td>200</td>
<td>20</td>
<td>1.5</td>
</tr>
<tr>
<td>②</td>
<td>7</td>
<td>500</td>
<td>20</td>
<td>1.5</td>
</tr>
<tr>
<td>③</td>
<td>7</td>
<td>200</td>
<td>15</td>
<td>1.5</td>
</tr>
<tr>
<td>④</td>
<td>5</td>
<td>200</td>
<td>20</td>
<td>1.5</td>
</tr>
</tbody>
</table>

where $\boldsymbol{C}^{\boldsymbol{M}}$ represents elastic tensor of the polymer, $\Delta \boldsymbol{C}^{\boldsymbol{C N} / \boldsymbol{M}}$ represents difference of elastic tensors between the CNTs and the polymer, $\boldsymbol{A}^{\boldsymbol{C N}}$ represents strain concentration tensor of the CNTs, which can be expressed as:
$$
\boldsymbol{A}^{\boldsymbol{C N}}=\left[\boldsymbol{I}-\boldsymbol{S}^{\boldsymbol{C N}}\left[\left(\boldsymbol{C}^{\boldsymbol{C N}}-\boldsymbol{C}^{\boldsymbol{M}}\right) \boldsymbol{S}^{\boldsymbol{C N}}+\boldsymbol{C}^{\boldsymbol{M}}\right]^{-1}\left(\boldsymbol{C}^{\boldsymbol{C N}}-\boldsymbol{C}^{\boldsymbol{M}}\right)\right]
\tag{16}
$$

![](./images/812756350307139585_16.jpg)

Fig. 5. The multi-coated model of CG-FRP.

where $S^{CN}$ is Eshelby tensor for cylindrical inclusion in isotropic material and can be shown in the Walpole's scheme:

$$
S^{CN}=\left(\frac{1}{2(1-v)}, 0, \frac{v}{2(1-v)}, 0, \frac{3-4 v}{4(1-v)}, \frac{1}{2}\right)
\tag{17}
$$

where $v$ is Poisson's ratio of the polymer.

### 2.2.3. Meso-scale modeling of multi-coated model
Based on the analysis above, properties of the CNRP is location related and treated as functionally graded interphase surrounding the fibers. A common way to deal with the interphase is to divide it into multi layers. Properties of layers differ from each other. In this way, a multi-coated inclusion model for the CG-FRP is established in Fig. 5.

As shown above, this fiber is represented by a cylinder and the layers of interphase are represented by homogeneous thin cylindrical shells. Following assumptions are made:

1 N phases are included in the model. Phase 1 is denoted as the fiber. Phase 2~N-1 represent the functionally graded interphase and thicknesses of layers are the same. Phase N denotes the polymer.
2 Volume of the $i$ th phase in global coordinate system is denoted as $V_{i}^{GLO}$ and expressed as:

$$
V_{i}^{G L O}=V^{i} / \Omega^{N}
\tag{18}
$$

where $\Omega^{N}$ denotes of volume of the multi-coated model.

1 Based on Eshelby's work, all inhomogeneities can be simplified by ellipse or elliptic shells. Boundary of the $i$ th phase can be expressed as:

$$
\Gamma^{i}: \frac{X_{1}^{2}}{a_{1 i}^{2}}+\frac{X_{2}^{2}}{a_{2 i}^{2}}+\frac{X_{3}^{2}}{a_{3 i}^{2}}=1
\tag{19}
$$

where $X_{1}, X_{2}, X_{3}$ are three axes of in the global Cartesian coordinate and $a_{1 i}, a_{2 i}, a_{3 i}$ are half axis lengths of the ellipse. When $a_{1}=a_{2} \ll a_{3}$ is satisfied, the ellipse can degenerate to a cylinder. The ellipse and elliptic shells share the same center and have the same orientations.

### 2.3. Analysis of the hierarchical models of the CG-FRP

#### 2.3.1. Material properties of the multi-coated model
Total thickness of the interphase equals to length of the CNTs. In this way, thickness of each layer in the multi-coated model can be expressed as:

$$
t_{\text {lay }}=l_{C N} /(N-2)
\tag{20}
$$

The local volume fraction of CNT in Phase $i, V_{i}^{L O C}$, is gotten by integration of Eq. (14):

$$
\begin{aligned}
V_{i}^{L O C} & =\left[\pi r_{i}^{2}-\pi r_{i-1}{ }^{2}\right]^{-1} \int_{r_{i-1}}^{r_{i}} V_{C N}^{L O C}\left(r_{x}\right) 2 \pi r_{x} d r_{x} \\
& =2 \pi \rho_{C N} r_{F} r_{C N}{ }^{2} /\left(2 r_{F}+(2 i-3) t_{\text {lay }}\right)
\end{aligned}
\tag{21}
$$

where $r_{i}=r_{C F}+(i-1) t_{l a y}$. Substituting Eq. (21) into Eq. (15), flexibility tensors of each phase is gotten, which are denoted as $F_{I N T}^{L O C}$.

![](./images/812756350307139585_17.jpg)

Fig. 6. Section of one CG-FRP bundle.

As the local coordinate system differs from the global one, the $F_{I N T}^{L O C}$ should be transformed into the global coordinate system before modeling of the multi-coated model. Based on fact that the fibers are usually fastened together to form a bundle, section of the CG-FRP bundle is displayed in Fig. 6.

Probabilities of the CNTs enhancing any angles in $X_{1}-X_{2}$ plane are equal. So it is reasonable to assume that $x_{1}$ and $x_{3}$ in the local coordinate system are equivalent to each other in the global coordinate system. Symmetric axis for the interphase in global coordinate is transformed to $X_{3}$. Following rules are (Table 5) obeyed in transformation:

When denoting flexibility of the interphase in global coordinate system as $F_{I N T}^{G L O}$, it can be expressed in the Walpole's scheme:

$$
F_{I N T}^{G L O}=\left(\frac{1}{E_{T}^{I N T}}-\frac{v_{T T}^{I N T}}{E_{T}^{I N T}},-\frac{v_{T I}^{I N T}}{E_{T}^{I N T}},-\frac{v_{T I}^{I N T}}{E_{I}^{I N T}}, \frac{1}{E_{I}^{I N T}}, \frac{1}{E_{I}^{I N T}}, \frac{1}{2 G_{T}^{I N T}}\right)
\tag{22}
$$

#### 2.3.2. Strain concentration tensors for the multi-coated model in transversely isotropic material
As the interphase is transversely isotropic, reference medium of the CG-FRP should be considered as transversely isotropic and problems on cylindrical inclusions embedded into transversely isotropic material should be discussed. Based on Eshelby's and Mura's works, when eigenstrain $\varepsilon_{i j}^{*}(\boldsymbol{x}')$ is applied in an ellipsoidal sub-domain $\Omega$ of an infinitely extended anisotropic material, displacement at point $\boldsymbol{x}$ is expressed as:

$$
\begin{aligned}
\tilde{u}_{i}(\boldsymbol{x})= & -(2 \pi)^{-3} \frac{\partial}{\partial x_{l}} \int_{\Omega} d \boldsymbol{x}^{\prime} \int_{-\infty}^{\infty} C_{j l m n} \varepsilon_{n m}^{*}\left(\boldsymbol{x}^{\prime}\right) N_{i j}(\xi) D^{-1}(\xi) \\
& \times \exp \left\{i \xi \cdot\left(\boldsymbol{x}-\boldsymbol{x}^{\prime}\right)\right\} d \xi
\end{aligned}
\tag{23}
$$

where $\boldsymbol{x}'$ is point within the sub-domain $\Omega$, $\boldsymbol{x}$ is any point within the infinitely extended anisotropic material, $\xi$ is wave vector corresponding to a given period of the $\varepsilon_{i j}^{*}(\boldsymbol{x})$ in Fourier series form: $\varepsilon_{i j}^{*}(\boldsymbol{x})=$ $\sum \bar{\varepsilon}_{i j}^{*}(\xi) \exp (i \xi \cdot \boldsymbol{x})$, where $i=\sqrt{-1}$ and $\boldsymbol{\xi} \bullet \boldsymbol{x}=\xi_{k} x_{k}$.

After manipulation:

$$
\begin{aligned}
\tilde{u}_{i}(\boldsymbol{x})= & -\frac{a_{1} a_{2} a_{3}}{8 \pi^{2}} \int_{-1}^{1} d z \int_{0}^{2 \pi} d \phi \int_{0}^{R} r d r \\
& \times \int_{S^{2}} C_{k l m n} \varepsilon_{n m}^{*}\left(\boldsymbol{x}^{\prime}\right) N_{i k}(\bar{\xi}) D^{-1}(\bar{\xi}) \bar{\xi}_{l} \delta^{\prime}(\zeta \bar{\zeta} \cdot y-\zeta z) d S(\bar{\xi})
\end{aligned}
\tag{24}
$$

where $R=\left(1-z^{2}\right)^{1 / 2}$. Consequently,

$$
\begin{aligned}
\tilde{u}_{i, J}(\boldsymbol{x})= & -\frac{a_{1} a_{2} a_{3}}{8 \pi^{2}} \int_{-1}^{1} d z \int_{0}^{2 \pi} d \phi \int_{0}^{R} r d r \\
& \times \int_{S^{2}} C_{k l m n} \varepsilon_{n m}^{*}\left(\boldsymbol{x}^{\prime}\right) N_{i k}(\bar{\xi}) D^{-1}(\bar{\xi}) \bar{\xi}_{l} \bar{\xi}_{J} \delta^{\prime \prime}(\zeta \bar{\zeta} \cdot y-\zeta z) d S(\bar{\xi})
\end{aligned}
\tag{25}
$$

When the $\boldsymbol{x}$ is interior of the sub-domain $\Omega$ and a uniform eigenstrain $\varepsilon_{k l}^{*}$ is applied, the Eq. (25) has the similar formation as isotropic

<table>
<caption>Table 5
Transformation of coordinates.</caption>
<thead>
<tr>
<th colspan="4">Transformation of coordinate
systems</th>
<th colspan="6">Transformation of engineering properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>Before</td>
<td>$x_1$</td>
<td>$x_2$</td>
<td>$x_3$</td>
<td>$E_{GLO}^{INT}$</td>
<td>$E_{I}^{INT}$</td>
<td>$v_{TT}^{INT}$</td>
<td>$v_{IT}^{INT}$</td>
<td>$G_{T}^{INT}$</td>
<td>$G_{LO}^{INT}$</td>
</tr>
<tr>
<td>After</td>
<td>$X_1$</td>
<td>$X_3$</td>
<td>$X_2$</td>
<td>$E_{GLO}^{INT}$</td>
<td>$E_{I}^{INT}$</td>
<td>$v_{TT}^{INT}$</td>
<td>$v_{IT}^{INT}$</td>
<td>$G_{T}^{INT}$</td>
<td>$G_{LO}^{INT}$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 6
Simplification of subscript of fourth order
tensors.</caption>
<thead>
<tr>
<th>$i=$</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
</tr>
</thead>
<tbody>
<tr>
<td>$kl=$</td>
<td>11</td>
<td>22</td>
<td>33</td>
<td>23</td>
<td>31</td>
<td>12</td>
</tr>
</tbody>
</table>

inclusion problem, which is:

$$
\tilde{\varepsilon}_{i j}=S_{i j k l}^{a n} \varepsilon_{k l}^{*}
\tag{26}
$$

The above Eshelby's tensor for anisotropic material can be written
as:

$$
S_{i j k l}^{a n}=(1 / 8 \pi) C_{p q k l}\left(\bar{G}_{i p j q}+\bar{G}_{j p i q}\right)
\tag{27}
$$

where $\bar{G}_{i p j q}=2 \pi \int_{-1}^{1} \operatorname{Re}[G_{i p j q} / Z] d \tilde{\xi}_{3}$.

Using simplification in Table 6, elastic properties of transversely
isotropic material can be assumed as:

$$
\begin{aligned}
& C_{11}=C_{22}=d, \quad C_{33}=h, \quad \frac{1}{2}\left(C_{11}-C_{12}\right)=e \\
& C_{44}=C_{55}=f, \quad C_{13}+C_{44}=g, \quad C_{13}=C_{23}
\end{aligned}
\tag{28}
$$

The Eshelby's tensor for cylindrical inclusion embedded into in-
finitely extended transversely isotropic material can be expressed in the
Walpole's scheme:

$$
S_{j i k l}^{\text {tran }}=\left[\left(1-\frac{e}{d}\right), 0, \frac{1}{2}\left(\frac{g}{d}-\frac{f}{d}\right), 0, \frac{1}{2}\left(1+\frac{e}{d}\right), 1\right]
\tag{29}
$$

Calculation of the $S_{j i k l}^{\text {tran }}$ is shown in Appendix.

After applying the equivalent inclusion method to the multi-coated
model, strain concentration tensors for each phase are gotten:

$$
\varepsilon^{i}=\left(I-S^{i}\left[\left(C^{i}-C^{\mathrm{N}}\right) S^{i}+C^{\mathrm{N}}\right]^{-1}\left(C^{i}-C^{\mathrm{N}}\right)\right): \varepsilon^{0}=A^{i}: \varepsilon^{0}
\tag{30}
$$

where $\varepsilon^{i}$ is strain in phase $i, C^{i}$ is elastic modulus of the Phase $i, A^{i}$ is
strain concentration for the $i$ th phase. The $S^{i}$ in Eq. (30) is similar to
$S_{j i k l}^{\text {tran }}$ in Eq. (29). Superscript and subscript are omitted for simplification
and new superscript in the $S^{i}$ represents the $i$ th phase of the multi-coated
model.

## 3. Sequentially homogenization and finite element simulations of
the multi-coated model

### 3.1. General framework of sequentially homogenization method

Sequentially homogenization [46] is a novel method to obtain effec-
tive modulus of composites with functionally graded interphase. It can
take influences between multi layers into consideration. In the sequen-
tially homogenization procedures, each phase is added to the model se-
quentially from outside to inside. Schematic diagram of the sequentially
homogenization method is displayed in Fig. 7.

As shown in Fig. 7, the Phase (N-I) ~ Phase $i$ have already been
added to the matrix to form a temporary medium before incorporating
of the Phase (i-I). Its effective modulus is defined as $C_{i}^{eff}$ and obtained

![](./images/812756350307139585_18.jpg)

<p class="cap">Fig. 7. Schematic diagram of the sequentially homogenization method.</p>

by Mori-Tanaka (M-T) method:

$$
\begin{aligned}
C_{i}^{e f f} & =C^{N}+\sum_{k=i}^{N-1} V_{k}^{G L O}\left(C^{k}-C^{N}\right): A^{k}\left(\left(\sum_{k=i}^{i-1} V_{k}^{G L O}+V_{N}^{G L O}\right) I\right. \\
& \left.+\sum_{k=i}^{N-1} V_{k}^{G L O} A^{k}\right)^{-1}
\end{aligned}
\tag{31}
$$

where $V_{i}^{G L O}$ represents global volume fraction of the Phase $i$. It is related
to the volume fraction of fiber $V_{F}$, radius of fiber $r_{F}$ and number of layers
$t_{lay}$ :

$$
V_{i}^{G L O}=V_{F} \frac{2 r_{F} t_{l a y}+(2 i-3) t_{l a y}{ }^{2}}{r_{F}{ }^{2}}
\tag{32}
$$

Then a self-consistency scheme (SC) is applied to calculate overall
property of the multi-coated model. Different from general SC method,
properties of the matrix are substituted by corresponding temporary ho-
mogeneous reference mediums. Consequently, effective properties of the
multi-coated model is:

$$
C_{S e q}^{e f f}=C^{N}+\sum_{i=1}^{N-1} V_{i}^{G L O}\left(C^{i}-C_{i+1}^{e f f}\right): \overline{A^{i}}
\tag{33}
$$

where $\overline{A^{i}}$ represents the strain concentration tensor in terms of $C_{S e q}^{e f f}$, and
the $C_{i+1}^{e f f}$ is gotten from Eq. (31). Then the sequentially homogenization
method is implemented using MATLAB software and effective elastic
tensor of the CG-FRP is obtain:

$$
C_{C G-F R P}^{E E F F}\left(c_{C G-F R P}^{e f f}, g_{C G-F R P}^{e f f}, h_{C G-F R P}^{e f f}, d_{C G-F R P}^{e f f}, e_{C G-F R P}^{e f f}, f_{C G-F R P}^{e f f}\right)
\tag{34}
$$

Engineering properties of the CG-FRP are obtained based on follow-
ing relationships (Table 7):

### 3.2. Finite element simulation of the multi-coated model of

Apart from the sequentially homogenization method, a randomized
representative volume element (RVE) of multi-coated model of the CG-
FRP is established in ANSYS software.

As is analyzed in Section 2.2, it is unrealistic to build both of the
CNTs and the fibers in one finite element model. The CNT region is

![](./images/812756350307139585_19.jpg)

Fig. 8. Property variation of the multi-coated model.

### Table 7
Relationships between the Walpole's tensor and the engineering elastic properties.

<table>
<thead>
<tr>
<th>$v_{I}^{eff}$</th>
<th>$v_{T}^{eff}$</th>
<th>$G_{I}^{eff}$</th>
<th>$G_{T}^{eff}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\frac{a_{CG-FRP}^{eff}c_{CG-FRP}^{eff}-\Phi}{a_{CG-FRP}^{eff}c_{CG-FRP}^{eff}+\Phi}$</td>
<td>$\frac{g_{CG-FRP}^{eff}}{c_{CG-FRP}^{eff}}$</td>
<td>$\frac{c_{CG-FRP}^{eff}}{2}$</td>
<td>$\frac{f_{CG-FRP}^{eff}}{2}$</td>
</tr>
<tr>
<td>$E_{I}^{eff}$</td>
<td>$E_{T}^{eff}$</td>
<td>$\Phi$</td>
<td></td>
</tr>
<tr>
<td>$\frac{2c_{CG-FRP}^{eff}\Phi}{a_{CG-FRP}^{eff}c_{CG-FRP}^{eff}+\Phi}$</td>
<td>$\frac{\Phi}{c_{CG-FRP}^{eff}}$</td>
<td colspan="2">$c_{CG-FRP}^{eff}d_{CG-FRP}^{eff}-2g_{CG-FRP}^{eff}h_{CG-FRP}^{eff}$</td>
</tr>
</tbody>
</table>

homogenized beforehand by Eq. (15). Effectiveness of the M-T method used in Eq. (15) has been verified by plenty of literatures and discussion in Section 4.2 can also prove its validation. Homogenized effective engineering properties of the CG-FRP are divided and set to corresponding phase in the multi-coated model, as displayed in Fig. 8.

Horizontal direction of above figures are normalized radius, which can be expressed as:

$$
\bar{r}_{x}=r_{x} / r_{C F} \tag{35}
$$

Consequently, multi-coated finite element RVEs are established to represent the CG-FRP. One of the RVEs is displayed in Fig. 9 at a condition: $V_{F}=40\%, r_{F}=7000nm$ and $l_{CN}=1050nm$. In this way, combined volume fraction of the fiber and the interphase is 53%.

![](./images/812756350307139585_20.jpg)

Fig. 9. RVE of CG-FRP for FEM analysis.

As shown in Fig. 9, the interphase region is divided into 5 layers and material coordinate systems of these phases are also displayed in the figure.

Periodicities of mechanical fields are guaranteed through application of Periodic Boundary Conditions (PBCs). The PBCs are imposed as nodal displacements relationships between opposite RVE faces using constraint equations and it is related to loads' directions (Table 8): where $u, v, w$ stand for displacements along $x, y, z$ directions, respectively, and $W,T,L$ represent dimensions of RVE in $x, y, z$ directions.

### Table 8
PBCs applied onto RVE based on loads' directions.

<table>
<thead>
<tr>
<th rowspan="2">No</th>
<th rowspan="2">Loads</th>
<th colspan="3">PBCs</th>
</tr>
<tr>
<th>Nodes on faces perpendicular to X</th>
<th>Nodes on faces perpendicular to Y</th>
<th>Nodes on faces perpendicular to Z</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">1</td>
<td rowspan="3">Tensile elastic modulus</td>
<td>$v^{x+}-v^{x-}=0$</td>
<td>$u^{y+}-u^{y-}=0$</td>
<td>$u^{z+}-u^{z-}=0$</td>
</tr>
<tr>
<td>$w^{x+}-w^{x-}=0$</td>
<td>$w^{y+}-w^{y-}=0$</td>
<td>$v^{z+}-v^{z-}=0$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$w^{z+}-w^{z-}=\varepsilon L$</td>
</tr>
<tr>
<td rowspan="3">2</td>
<td rowspan="3">Transverse elastic modulus</td>
<td>$u^{x+}-u^{x-}=\varepsilon W$</td>
<td>$u^{y+}-u^{y-}=0$</td>
<td>$u^{z+}-u^{z-}=0$</td>
</tr>
<tr>
<td>$v^{x+}-v^{x-}=0$</td>
<td>$w^{y+}-w^{y-}=0$</td>
<td>$v^{z+}-v^{z-}=0$</td>
</tr>
<tr>
<td>$w^{x+}-w^{x-}=0$</td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="3">3</td>
<td rowspan="3">In-plane shear modulus</td>
<td>$u^{x+}-u^{x-}=0$</td>
<td>$u^{y+}-u^{y-}=0$</td>
<td>$u^{z+}-u^{z-}=0$</td>
</tr>
<tr>
<td>$v^{x+}-v^{x-}=0$</td>
<td>$v^{y+}-v^{y-}=0$</td>
<td>$v^{z+}-v^{z-}=0.5\varepsilon L$</td>
</tr>
<tr>
<td>$w^{x+}-w^{x-}=0$</td>
<td>$w^{y+}-w^{y-}=0.5\varepsilon T$</td>
<td>$w^{z+}-w^{z-}=0$</td>
</tr>
<tr>
<td rowspan="3">4</td>
<td rowspan="3">Out-plane shear modulus</td>
<td>$u^{x+}-u^{x-}=0$</td>
<td>$u^{y+}-u^{y-}=0.5\varepsilon T$</td>
<td>$u^{z+}-u^{z-}=0$</td>
</tr>
<tr>
<td>$v^{x+}-v^{x-}=0$</td>
<td>$v^{y+}-v^{y-}=0$</td>
<td>$v^{z+}-v^{z-}=0$</td>
</tr>
<tr>
<td>$w^{x+}-w^{x-}=0.5\varepsilon W$</td>
<td>$w^{y+}-w^{y-}=0$</td>
<td>$w^{z+}-w^{z-}=0$</td>
</tr>
</tbody>
</table>

![](./images/812756350307139585_21.jpg)

Fig. 10. Mesh of RVE.

Table 9
Strains applied and corresponding responses in FEM analysis.

| No | Strain                     | Response                   |
|----|----------------------------|----------------------------|
| 1  | $\{\varepsilon_{1}^{1},0,0,0,0,0\}$ | $\{\sigma_{1}^{1},\sigma_{2}^{1},\sigma_{3}^{1},0,0,0\}$ |
| 2  | $\{0,\varepsilon_{2}^{2},0,0,0,0\}$ | $\{\sigma_{1}^{2},\sigma_{2}^{2},\sigma_{3}^{2},0,0,0\}$ |
| 3  | $\{0,0,\varepsilon_{3}^{3},0,0,0\}$ | $\{\sigma_{1}^{3},\sigma_{2}^{3},\sigma_{3}^{3},0,0,0\}$ |
| 4  | $\{0,0,0,\gamma_{23}^{4},0,0\}$ | $\{0,0,0,\tau_{23}^{4},0,0\}$ |
| 5  | $\{0,0,0,0,\gamma_{31}^{5},0\}$ | $\{0,0,0,0,\tau_{31}^{5},0\}$ |
| 6  | $\{0,0,0,0,0,\gamma_{12}^{6}\}$ | $\{0,0,0,0,0,\tau_{12}^{6}\}$ |

Table 10
Engineering properties from FEM analysis.

| $E_{I}^{eff}$               | $E_{T}^{eff}$       | $G_{I}^{eff}$       | $G_{T}^{eff}$               |
|-----------------------------|---------------------|---------------------|-----------------------------|
| $\frac{1}{2}\left(\frac{\sigma_{1}^{1}}{\varepsilon_{1}^{1}}+\frac{\sigma_{2}^{2}}{\varepsilon_{2}^{2}}\right)$ | $\frac{\sigma_{3}^{3}}{\varepsilon_{3}^{3}}$ | $\frac{\tau_{12}^{6}}{\gamma_{12}^{6}}$ | $\frac{1}{2}\left(\frac{\tau_{23}^{4}}{\gamma_{23}^{4}}+\frac{\tau_{31}^{5}}{\gamma_{31}^{5}}\right)$ |

Superscripts + and − represent opposite sides of the RVE. $\varepsilon$ denotes strain applied to the RVE. Meshes of the RVE are displayed in Fig. 10.

As the fibers are randomly distributed, there is no symmetric axis in the RVE. To this end, properties in x and y directions are slightly different. Six different types of strains are applied (Table 9):

Superscripts in above list represent number of the strain conditions. Subscripts represent directions of the strains or the responses. Engineering properties of the CG-FRP can be obtained (Table 10):

Then results from the hierarchical models and the FEM are compared with experimental data in existing literatures in Table 11.

As shown in Table 11, three types of $V_{F}$ are included in the experimental data, including 0.3%, 41% and 67%. Tensile and transverse moduli from the present hierarchical models and the FEM are in good agreement with the experimental observations. It is also important to note that, both in experiments and theoretical works, the grafted CNTs can improve property the CG-FRP. Especially for transverse modulus, improvement as high as 30% is yielded by CG-FRP.

## 4. Results and discussion

In this section, results from the hierarchical models and the FEM are investigated to study effects of elastic modulus ($E_{CN}$), volume fraction ($V_{CN}$) and length ($l_{CN}$) of the CNTs on effective modulus of the CG-FRP.

### 4.1. Effects of elastic modulus of the CNTs

When studying effects of elastic modulus of the CNTs, $E_{CN}$ is chosen 0.7~1.0TPa and length of the CNT is fixed at $1.5\ \mu m$ or $0.7\ \mu m$ for $V_{CF}=20\%$, 40% and $V_{CF}=60\%$, respectively. Radius and areal density of the CNTs are chosen 25 nm and 200. So combined volume fractions of the fiber and the interphase in the multi-coated model become 29.5%, 59.0% and 72.6%. Then effective tensile/transverse modulus and in-plane/out-plane shear modulus obtained by the present hierarchical models and the FEM are presented below (Fig. 11).

Variations of results and deviations between these two methods are two of the most concerned issues in discussion. After analysis, following table is obtained (Table 12):

"Min" and "Max" denote the minimum and the maximum values. "Inc" denotes increment in percentage, which is defined by (Max-Min)/Min. "Dev" denotes deviation of data, which is defined by $\sum_{i=1}^{N}(|H_{i}-F_{i}|/H_{i})/N$, where $P_{i}$ and $F_{i}$ represent results from the present hierarchical models and the FEM, respectively.

#### (1) Variations of effective properties

Generally, effective moduli of the CG-FRP remain stable with increment of $E_{CN}$. Less than 0.5% increments are observed for all effective properties. It can be explained that volume fraction of the CNT is only around 1%. So contributions of $E_{CN}$ are limited.

#### (1) Deviations from the two methods

Predictions of tensile modulus by both methods alike each other very much. While deviation of the transverse modulus is less than −9% and those of the shear modulus are less than 15%. Furthermore the deviations increase with volume fraction of the fiber.

### 4.2. Effects of volume fraction of the CNTs

When studying effects of volume fractions of the CNTs, lengths of the CNT ($l_{CN}$) are chosen 0~2.1 um or 0~1.5 um for $V_{CF}=20\%$, 40% and $V_{CF}=60\%$, respectiely. Consequently, volume fractions of the CNT

Table 11
Comparisons between experimental data/ hierarchical models/ FEM.

|  | Experimental data |  |  | Hierarchical models |  |  | FEM results |  |  |
|----|----|----|----|----|----|----|----|----|----|
|  | $\text{E}_{11}$(GPa)<br>Vf=0.3%<br>Vcnt=0.08% | $\text{E}_{11}$(GPa)<br>Vf=67%<br>Vcnt=20% | $\text{E}_{22}$(GPa)<br>Vf=41%<br>Vcnt=2% | $\text{E}_{11}$(GPa)<br>Vf=0.3%<br>Vcnt=0.08% | $\text{E}_{11}$(GPa)<br>Vf=67%<br>Vcnt=20% | $\text{E}_{22}$(GPa)<br>Vf=41%<br>Vcnt=2% | $\text{E}_{11}$(GPa)<br>Vf=0.3%<br>Vcnt=0.08% | $\text{E}_{11}$(GPa)<br>Vf=67%<br>Vcnt=20% | $\text{E}_{22}$(GPa)<br>Vf=41%<br>Vcnt=2% |
| CG-FRP | $2.0\pm0.1[14]$ | $138\pm6.5[41]$ | $10.2\pm1.3[35]$ | 1.93 | 147.7 | 9.7 | 1.94 | 148.7 | 11.15 |
| FRP | $1.8\pm0.1[14]$ | $131[41]$ | $7.8\pm1.09[36]$ | 1.9 | 137.6 | 6.74 | 1.93 | 137 | 6.93 |

![](./images/812756350307139585_22.jpg)

![](./images/812756350307139585_23.jpg)

![](./images/812756350307139585_24.jpg)

![](./images/812756350307139585_25.jpg)

Fig. 11. Effective modulus V.S. modulus of CNT.

$(V_{CN})$ are 0~4.52%, 0~9.05%, 0~9.69%. Radius and areal density of the CNTs are chosen 25 nm and 200. While modulus and Poisson's ratio of the CNTs are fixed at 1TPa and 0.3. Following results are obtained (Fig. 12 and Table 13):

### (1) Variations of effective properties
Based on the figures and table above, both the theoretical and the FEM results reveal that effective properties of the CG-FRP increase with $V_{CN}$. The transverse modulus increases as large as 30~50%, which agrees with conclusion gotten from Table 11. The shear modulus increases more than 20%, however the tensile modulus does not change too much, which is less than 1.5%.

These can be explained that the CNTs enhanc directly on the transverse direction of the CG-FRP. Meanwhile bending of the CNTs can also enhanced shear modulus in both directions. However length direction of the CG-FRP is transverse direction of the CNT, so the tensile modulus is nearly unchanged.

### (1) Deviations from the two methods
Deviations of these two method increase with $V_{CN}$ and $V_{CF}$. Deviation of the transverse modulus is less than 10%, while deviations of the shear moduli are less than 15%.

It is worthwhile to notice in Fig. 12, all properties coincide with each other at $V_{CN}=0$ (no CNT is grafted onto fiber). This indicates that the M-T method is Section 2.2.2 is accurate enough for cylindrical inhomogeneity problem. So homogenization of the CNT region beforehand in the FEM models in Section 3.2 are reasonable.

### 4.3. Effects of length of the CNTs
It is noticed that, even for a fixed $V_{CN}$, length of the CNT $(l_{CN})$ can also be changed. The $V_{CN}$ can be written as:

$$
V_{C N}=\frac{\pi r_{C N}{ }^{2} l_{C N} \cdot 2 \pi r_{C F} \rho_{C N}}{\pi r_{C F}{ }^{2}} V_{C F} \tag{36}
$$

After denoting:

$$
A_{C N}=\frac{\pi r_{C N}{ }^{2} \cdot 2 \pi r_{C F} \rho_{C N}}{\pi r_{C F}{ }^{2}} V_{C F} \tag{37}
$$

where $A_{CN}$ represents area ration of the CNTs to surface of the fibers in per $V_{CF}$, then the $V_{CN}$ can be rewritten as:

$$
V_{C N}=A_{C N} \cdot l_{C N} \tag{38}
$$

<table>
<caption>Table 12<br>Data analysis of effective properties V.S. modulus of CNTs ($E_{CN}$).</caption>
<tbody>
<tr>
<td rowspan="2">$V_{CF}$=20%</td>
<td colspan="4">Effective transverse modulus</td>
<td colspan="4">Effective tensile modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>4.3889</td>
<td>4.3907</td>
<td>0.04%</td>
<td rowspan="2">−6.86%</td>
<td>48.5590</td>
<td>48.5600</td>
<td>0.00%</td>
<td rowspan="2">−0.36%</td>
</tr>
<tr>
<td>FEM</td>
<td>4.8853</td>
<td>4.8945</td>
<td>0.19%</td>
<td>48.7297</td>
<td>48.7369</td>
<td>0.01%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=20%</td>
<td colspan="4">Effective in-plane shear modulus</td>
<td colspan="4">Effective out-plane shear modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>1.5122</td>
<td>1.5124</td>
<td>0.01%</td>
<td rowspan="2">3.62%</td>
<td>1.8758</td>
<td>1.8762</td>
<td>0.02%</td>
<td rowspan="2">5.82%</td>
</tr>
<tr>
<td>FEM</td>
<td>1.4575</td>
<td>1.4577</td>
<td>0.01%</td>
<td>1.7666</td>
<td>1.7669</td>
<td>0.02%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=40%</td>
<td colspan="4">Effective transverse modulus</td>
<td colspan="4">Effective tensile modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>6.5416</td>
<td>6.5489</td>
<td>0.11%</td>
<td rowspan="2">−7.26%</td>
<td>94.1070</td>
<td>94.1100</td>
<td>0.00%</td>
<td rowspan="2">−0.49%</td>
</tr>
<tr>
<td>FEM</td>
<td>6.7027</td>
<td>6.7361</td>
<td>0.50%</td>
<td>94.5581</td>
<td>94.5724</td>
<td>0.02%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=40%</td>
<td colspan="4">Effective in-plane shear modulus</td>
<td colspan="4">Effective out-plane shear modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>2.1696</td>
<td>2.1706</td>
<td>0.05%</td>
<td rowspan="2">9.16%</td>
<td>4.0069</td>
<td>4.0089</td>
<td>0.05%</td>
<td rowspan="2">12.69%</td>
</tr>
<tr>
<td>FEM</td>
<td>1.9710</td>
<td>1.9718</td>
<td>0.04%</td>
<td>3.0177</td>
<td>3.0192</td>
<td>0.05%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=60%</td>
<td colspan="4">Effective transverse modulus</td>
<td colspan="4">Effective tensile modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>8.4288</td>
<td>8.4381</td>
<td>0.11%</td>
<td rowspan="2">−8.53%</td>
<td>139.3100</td>
<td>139.3100</td>
<td>0.00%</td>
<td rowspan="2">−0.16%</td>
</tr>
<tr>
<td>FEM</td>
<td>9.1362</td>
<td>9.1679</td>
<td>0.35%</td>
<td>139.5310</td>
<td>139.5410</td>
<td>0.01%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=60%</td>
<td colspan="4">Effective in-plane shear modulus</td>
<td colspan="4">Effective out-plane shear modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>2.8084</td>
<td>2.8093</td>
<td>0.03%</td>
<td rowspan="2">11.98%</td>
<td>8.5037</td>
<td>8.5047</td>
<td>0.01%</td>
<td rowspan="2">14.77%</td>
</tr>
<tr>
<td>FEM</td>
<td>2.4715</td>
<td>2.4730</td>
<td>0.06%</td>
<td>7.7571</td>
<td>7.7589</td>
<td>0.02%</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 13<br>Data analysis of effective properties V.S. volume fraction of CNTs ($V_{CN}$).</caption>
<tbody>
<tr>
<td rowspan="2">$V_{CF}$=20%</td>
<td colspan="4">Effective transverse modulus</td>
<td colspan="4">Effective tensile modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>4.0000</td>
<td>4.5692</td>
<td>14.23%</td>
<td rowspan="2">−4.51%</td>
<td>48.3120</td>
<td>48.6510</td>
<td>0.70%</td>
<td rowspan="2">−0.26%</td>
</tr>
<tr>
<td>FEM</td>
<td>4.0234</td>
<td>4.9991</td>
<td>24.25%</td>
<td>48.3121</td>
<td>48.8944</td>
<td>1.21%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=20%</td>
<td colspan="4">Effective in-plane shear modulus</td>
<td colspan="4">Effective out-plane shear modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>1.4134</td>
<td>1.5533</td>
<td>9.90%</td>
<td rowspan="2">3.46%</td>
<td>1.7299</td>
<td>1.9340</td>
<td>11.80%</td>
<td rowspan="2">6.13%</td>
</tr>
<tr>
<td>FEM</td>
<td>1.3692</td>
<td>1.4964</td>
<td>9.29%</td>
<td>1.6114</td>
<td>1.8348</td>
<td>13.86%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=40%</td>
<td colspan="4">Effective transverse modulus</td>
<td colspan="4">Effective tensile modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>5.3342</td>
<td>7.1070</td>
<td>33.23%</td>
<td rowspan="2">−7.78%</td>
<td>93.7340</td>
<td>94.2270</td>
<td>0.53%</td>
<td rowspan="2">−0.35%</td>
</tr>
<tr>
<td>FEM</td>
<td>5.3956</td>
<td>8.3730</td>
<td>55.18%</td>
<td>93.7340</td>
<td>94.8768</td>
<td>1.22%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=40%</td>
<td colspan="4">Effective in-plane shear modulus</td>
<td colspan="4">Effective out-plane shear modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>1.8825</td>
<td>2.2815</td>
<td>21.2%</td>
<td rowspan="2">9.34%</td>
<td>3.3982</td>
<td>4.2203</td>
<td>24.19%</td>
<td rowspan="2">3.89%</td>
</tr>
<tr>
<td>FEM</td>
<td>1.6923</td>
<td>2.1252</td>
<td>25.58%</td>
<td>3.2500</td>
<td>4.0893</td>
<td>25.82%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=60%</td>
<td colspan="4">Effective transverse modulus</td>
<td colspan="4">Effective tensile modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>7.4700</td>
<td>10.1420</td>
<td>35.77%</td>
<td rowspan="2">−9.45%</td>
<td>139.1600</td>
<td>139.5500</td>
<td>0.28%</td>
<td rowspan="2">−0.29%</td>
</tr>
<tr>
<td>FEM</td>
<td>7.4908</td>
<td>11.5740</td>
<td>54.51%</td>
<td>139.1559</td>
<td>140.3274</td>
<td>0.84%</td>
</tr>
<tr>
<td rowspan="2">$V_{CF}$=60%</td>
<td colspan="4">Effective in-plane shear modulus</td>
<td colspan="4">Effective out-plane shear modulus</td>
</tr>
<tr>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
<td>Min</td>
<td>Max</td>
<td>Inc</td>
<td>Dev</td>
</tr>
<tr>
<td>Present model</td>
<td>2.6280</td>
<td>3.1803</td>
<td>21.01%</td>
<td rowspan="2">12.47%</td>
<td>8.1750</td>
<td>9.3125</td>
<td>13.91%</td>
<td rowspan="2">12.23%</td>
</tr>
<tr>
<td>FEM</td>
<td>2.2152</td>
<td>2.8701</td>
<td>29.56%</td>
<td>6.9325</td>
<td>8.4651</td>
<td>22.11%</td>
</tr>
</tbody>
</table>

![](./images/812756350307139585_26.jpg)

![](./images/812756350307139585_27.jpg)

![](./images/812756350307139585_28.jpg)

![](./images/812756350307139585_29.jpg)

Fig. 12. Effective modulus V.S. volume fraction of CNT.

In following parts, influences of the $l_{CN}$ on effective transverse modulus of the CG-FRP are discussed. Results can be classified into two circumstances:

(1) The CG-FRP with tiny CNTs, $V_{CN}$<0.1%

It comes to a conclusion that there exist an optimum $l_{CN}$ in tiny $V_{CN}$, which is shown in Fig 13. Stars in the figure represent maximum effective transverse moduli of the CG-FRP. The optimum $l_{CN}$ increases with $V_{CN}$. For example the optimum $l_{CN}$ for $V_{CN}$=0.01 is about 400 nm, and the optimum $l_{CN}$ for $V_{CN}$=0.08 increases to 1200 nm.

This phenomena can be explained: for a fixed $V_{CN}$, larger $l_{CN}$ indicates softer but thicker functionally graded interphase. Influences of these two parameters contradict to each other. So there must exists an optimum $l_{CN}$, where effective transverse modulus reaches the maximum value.

(1) General CG-FRP with $V_{CN}$>0.1%

It is reasonable to deduce from above section that the optimum $l_{CN}$ for CG-FRP with $V_{CN}$ larger than 0.1% is longer. However this theoretical optimum $l_{CN}$ often exceed the maximum length of the CNTs. The maximum $l_{CN}$ subjects to two conditions:

![](./images/812756350307139585_30.jpg)

Fig. 13. Effective transverse modulus V.S. $l_{CN}$ at tiny $V_{CN}$.

![](./images/812756350307139585_31.jpg)

Fig. 14. Effective transverse modulus V.S. $l_{CN}$.

① Gaps between the fibers are limited. For FRP at $V_{CF}$=70% and $r_{CF}$=7000 nm, the gap between two adjacent fibers is about 2730 nm. In this way, the optimum $l_{CN}$ in Fig. 13 for $V_{CN}$=0.08 almost reaches its maximum value;
② It is also limited by grafting techniques of the CNTs, length of the CNTs cannot be too large. In this paper the maximum value is applied as 2.1 um.

Consequently, in most cases, the theoretical optimum $l_{CN}$ often becomes impossible to reach. Influences of the $l_{CN}$ on effective transverse modulus of the CG-FRP are plotted in Fig. 14. It is concluded that increment of the $l_{CN}$ always leads to improvement on transverse modulus.

## 5. Conclusion

In this paper, effective properties of the CG-FRP were studied by sequentially homogenization of the hierarchical models. The hierarchical models were conducted in two scales: micro and meso scale. The micro-scale model was used to obtain equivalent effective modulus of CNRP. The meso-scale model was a multi-coated inclusion embedded into transversely isotropic material. Then effective properties of the multi-coated model were obtained by sequentially homogenization method. Furthermore a RVE for the multi-coated model is established and solved in FEM. Then effects of property and volume fraction of the CNTs were studied. Following conclusions can be obtained:

(1) This paper proposes a hierarchical modeling method to investigate effective properties of the CG-FRP. Due to variation of local volume fraction of the CNTs, the CNT region can be homogenized as functionally graded interphase around fibers. After division of the interphase, the CG-FRP can be represented by a multi-coated model embedded into transversely isotropic material;
(2) The sequentially homogenization method is proper to calculate the effective properties of the CG-FRP. Furthermore, randomly distributed multi-coated models for CG-FRP are established and analyzed in FEM. Results from these two methods coincide with experimental data from existing literatures.
(3) Based on the hierarchical models, elastic modulus of the CNT has limited influence on properties of the CG-FRP. Meanwhile tensile modulus of the CG-FRP nearly remains stable before and after grafting of the CNTs. Transverse and shear moduli of the CG-FRP observe a 30%~50% growth with increment of the volume fraction of CNT compared to FRP.
(4) For fixed CNT volume fraction, there exists a theoretical optimum length of the CNTs. It can be clearly observed at $V_{CN}$ <0.1%. However, for most CG-FRP with $V_{CN}$ >0.1%, the increment of $l_{CN}$ always leads to augment on transverse modulus of the CG-FRP.

## Acknowledgment

This work was supported by the Fund of Intelligent Robotic in Ministry of Science and Technology of the People's Republic of China [grant numbers no. 2017YFB1301703], the Fund for distinguished Young Scholars in Shaanxi Province of China [grant numbers no. S2018-jc-jq-0260] and the Fund on the Guidance of Technology Innovation in Shaanxi Province of China[grant numbers no. S2018-YD-CGHJ-0014]. The author would like to acknowledge the editors and the anonymous referees of their insightful comments.

## Appendix

The nonzero components of $\bar{G}_{ijkl}$ is Eq. (27) are given below:

$$
\begin{aligned}
\bar{G}_{1111}=\bar{G}_{2222}=& \frac{1}{2} \pi \int_{0}^{1} \Delta\left(1-x^{2}\right)\left\{\left[f\left(1-x^{2}\right)+h \rho^{2} x^{2}\right]\right. \\
&\left.\times\left[(3 e+d)\left(1-x^{2}\right)+4 f \rho^{2} x^{2}\right]-g^{2} \rho^{2}\left(1-x^{2}\right)\right\} d x
\end{aligned}
$$

$$
\bar{G}_{3333}=4 \pi \int_{0}^{1} \Delta \rho^{2} x^{2}\left[d\left(1-x^{2}\right)+f \rho^{2} x^{2}\right]\left[e\left(1-x^{2}\right)+f \rho^{2} x^{2}\right] d x
$$

$$
\begin{aligned}
\bar{G}_{1122}=\bar{G}_{2211}=& \frac{1}{2} \pi \int_{0}^{1} \Delta\left(1-x^{2}\right)\left\{\left[f\left(1-x^{2}\right)+h \rho^{2} x^{2}\right]\right. \\
&\left.\times\left[(e+3 d)\left(1-x^{2}\right)+4 f \rho^{2} x^{2}\right]-3 g^{2} \rho^{2} x^{2}\left(1-x^{2}\right)\right\} d x
\end{aligned}
$$

$$
\begin{aligned}
\bar{G}_{1133}=\bar{G}_{2233}=& 2 \pi \int_{0}^{1} \Delta \rho^{2} x^{2}\left\{[(d+e)\left(1-x^{2}\right)+2 f \rho^{2} x^{2}\right] \\
&\left.\times\left[f\left(1-x^{2}\right)+h \rho^{2} x^{2}\right]-g^{2} \rho^{2} x^{2}\left(1-x^{2}\right)\right\} d x
\end{aligned}
$$

$$
\bar{G}_{3311}=\bar{G}_{3322}=2 \pi \int_{0}^{1} \Delta\left(1-x^{2}\right)\left[d\left(1-x^{2}\right)+f \rho^{2} x^{2}\right]\left[e\left(1-x^{2}\right)+f \rho^{2} x^{2}\right] d x
$$

$$
\bar{G}_{1212}=\frac{1}{2} \pi \int_{0}^{1} \Delta\left(1-x^{2}\right)^{2}\left\{g^{2} \rho^{2} x^{2}-(d-e)\left[f\left(1-x^{2}\right)+h \rho^{2} x^{2}\right]\right\} d x
$$

$$
\bar{G}_{1313}=\bar{G}_{2323}=(-2 \pi) \int_{0}^{1} \Delta \rho^{2} x^{2}\left(1-x^{2}\right)\left[e\left(1-x^{2}\right)+f \rho^{2} x^{2}\right] d x
$$

where constants are shown in Eq. (28) and
$$
\Delta^{-1}=\left[e\left(1-x^{2}\right)+f \rho^{2} x^{2}\right]\left\{\left[d\left(1-x^{2}\right)+f \rho^{2} x^{2}\right]\left[f\left(1-x^{2}\right)+h \rho^{2} x^{2}\right]\right.
$$

$$
\left.-g^{2} \rho^{2} x^{2}\left(1-x^{2}\right)\right\}
$$

$$
\rho=a_{1} / a_{3}
$$

For $a_{1} \ll a_{3}, \rho=0$, the components of $S_{j i k l}^{\text {tran }}$ can be shown:

<table>
<thead>
  <tr>
    <th>$S_{1111}(S_{1122})$</th>
    <th>$S_{1133}$</th>
    <th>$S_{2211}$</th>
    <th>$S_{2222}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\frac {1}{4}(3-\frac {e}{d})$</td>
    <td>$\frac {1}{2}(\frac {e}{d}-\frac {f}{d})$</td>
    <td>$\frac {1}{4}(1-3\frac {e}{d})$</td>
    <td>$\frac {1}{4}(3-\frac {e}{d})$</td>
  </tr>
  <tr>
    <td>$S_{2233}$</td>
    <td>$S_{3311}(S_{3322},S_{3333})$</td>
    <td>$S_{2323}(S_{1313})$</td>
    <td>$S_{1212}$</td>
  </tr>
  <tr>
    <td>$\frac {1}{2}(\frac {e}{d}-\frac {f}{d})$</td>
    <td>0</td>
    <td>$\frac {1}{4}$</td>
    <td>$\frac {1}{4}(1+\frac {e}{d})$</td>
  </tr>
</tbody>
</table>

## References

[1] Popov V. Carbon nanotubes: properties and applications. Mater Sci Eng R 2004;43:61-102.
[2] Thostenson E, Li C, Chou T. Nanocomposites in context. Compos Sci Technol 2005;65(3-4):491-516.
[3] Rong H, Dahmen K-H, Garmestani H, Yu M, Jacob KI. Comparison of chemical vapor deposition and chemical grafting for improving the mechanical properties of carbon fiber/epoxy composites with multi-wall carbon nanotubes. J Mater Sci 2013;48(14):4834-42.

[4] Feng L, Li K-Z, Lu J-H, Qi L-H. Effect of growth temperature on carbon nanotube grafting morphology and mechanical behavior of carbon fibers and carbon/carbon composites. J Mater Sci Technol 2017;33(1):65-70.

[5] Li Q, Church JS, Naebe M, Fox BL. Interfacial characterization and reinforcing mechanism of novel carbon nanotube and carbon fibre hybrid composites. Carbon N Y 2016;109:7-86.

[6] Wu G, Ma L, Liu L, Wang Y, Xie F, Zhong Z, Zhao M, Jiang B, Huang Y. Interfacially reinforced methylphenylsilicone resin composites by chemically grafting multiwall carbon nanotubes onto carbon fibers. Compos Part B Eng 2015;82:50-8.

[7] Garcia E, Wardle B, John Hart A, Yamamoto N. Fabrication and multifunctional properties of a hybrid laminate with aligned carbon nanotubes grown in situ. Compos Sci Technol 2008;68(9):2034-41.

[8] Wicks SS, de Villoria RG, Wardle BL. Interlaminar and intralaminar reinforcement of composite laminates with aligned carbon nanotubes. Compos Sci Technol 2010;70(1):20-8.

[9] Einarsson E, Shiozawa H, Kramberger C, Rümmeli MH, Grüneis A, Pichler T, Maruyama S. Revealing the small-bundle internal structure of vertically aligned single-walled carbon nanotube films. J Phys Chem C 2007;111(48):17861-4.

[10] Futaba DN, Hata K, Yamada T, Hiraoka T, Hayamizu Y, Kakudate Y, Tanaike O, Hatori H, Yumura M, Iijima S. Shape-engineerable and highly densely packed single-walled nanotubes and their application as super-capacitor electrodes. Nat Mater 2006;5(12):987-94.

[11] Tüzemen MC, Salancı E, Avcı A. Enhancing mechanical properties of bolted carbon/epoxy nanocomposites with carbon nanotube, nanoclay, and hybrid loading. Compos Part B Eng 2017;128(1):146-54.

[12] Xu Hong, Tong Xiao, Zhang Yongyi, Li Qingwen, Lu Weibang. Mechanical and electrical properties of laminated composites containing continuous carbon nanotube film interleaves. Compos Sci Technol 2016;127:113-18.

[13] Kim Hansang, Oh Eugene, Thomas Hahn H, Lee Kun-Hong. Enhancement of fracture toughness of hierarchical carbon fiber composites via improved adhesion between carbon nanotubes and carbon fibers. Compos Part A-Appl S 2015;71:72-83.

[14] Lavagna Luca, Massella Daniele, Pantano Maria F, Federico Bosia, Pugno Nicola M, Pavese Matteo. Grafting carbon nanotubes onto carbon fibers doubles their effective strength and the toughness of the composite. Compos Sci Technol 2018;166:140-9.

[15] Chaudhry MS, Czekanski A, Zhu ZH. Characterization of carbon nanotube enhanced interlaminar fracture toughness of woven carbon fiber reinforced polymer composites. Int J Mech Sci 2017;131-132:480-9.

[16] Khan SU, Kim J-K. Impact and delamination failure of multiscale carbon nanotube-fiber reinforced polymer composites: a review. Int J Aeronaut Space Sci 2011;12(2):115-33.

[17] Satish G, Prasad VVS, Ramji Koona. Effect on mechanical properties of carbon nanotube based composite. Mater Today 2018;5:7725-34.

[18] Kundalwal SI, Meguid SA. Micromechanics modelling of the effective thermoelastic response of nano-tailored composites. Eur J Mech A/Solid 2015;53:241-53.

[19] Ansari R, Aghdam MH. Micromechanics viscoelastic analysis of carbon nanotube-reinforced composites subjected to uniaxial and biaxial loading. Compos B Eng 2016;90:512-22.

[20] Lv Qiang, Wang Zhikun, Chen Shenghui, Li Chunling, Sun Shuangqing, Hu Songqing. Effects of single adatom and stone-wales defects on the elastic properties of carbon nanotube/polypropylene composites: a molecular simulation study. Int J Mech Sci 2017;131-132:527-34.

[21] Radue MS, Odegard GM. Multiscale modeling of carbon fiber/carbon nanotube/epoxy hybrid composites: comparison of epoxy matrices. Compos Sci Technol 2018;166:20-6.

[22] Iacobellis Vincent, Radhi Ali, Behdinan Kamran. A bridging cell multiscale modeling of carbon nanotube-reinforced aluminum nanocomposites. Comps Struct 2018;202:406-12.

[23] Song ZG, Zhang LW, Liew KM. Vibration analysis of CNT-reinforced functionally graded composite cylindrical shells in thermal environments. Int J Mech Sci 2016;115-116:339-47.

[24] Kolahchi Reza, Zarei Mohammad Sharif, Hajmohammad Mohammad Hadi, Nouri Ali. Wave propagation of embedded viscoelastic FG-CNT-reinforced sandwich plates integrated with sensor and actuator based on refined zigzag theory. Int J Mech Sci 2017;130:534-45.

[25] Hadden CM, Klimek-McDonald DR, Pineda EJ, King JA, Reichanadter AM, Miskoglu I, Gowtham S, Odegard GM. Mechanical properties of graphene nanoplatelet/carbon fiber/epoxy hybrid composites: multiscale modeling and experiments. Carbon N Y 2015;95:100-12.

[26] Tornabene F, Fantuzzi N, Bacciocchi M. Linear static response of nanocomposite plates and shells reinforced by agglomerated carbon nanotubes. Compos Part B Eng 2017;115(1):449-76.

[27] Barai P, Weng GJ. A theory of plasticity for carbon nanotube reinforced composites. Int J Plast 2011;27(4):539-59.

[28] Chatzigeorgiou G, Efendiev Y, Lagoudas DC. Homogenization of aligned "fuzzy fiber" composites. Int J Solid Struct 2011;48(19):2668-80.

[29] Kundalwal S, Ray M. Effective properties of a novel continuous fuzzy-fiber reinforced composite using the method of cells and the finite element method. Eur J Mech Solid 2012;36:191-203.

[30] Lurie S, Volkov-Bogorodskiy D, Menshykov O. Modeling the effective mechanical properties of "fuzzy fiber" composites across scales length. Compos B Eng 2018;142:24-35.

[31] Nejati M, Asanjarani A, Dimitri R, Tornabene F. Static and free vibration analysis of functionally graded conical shells reinforced by carbon nanotubes. Int J Mech Sci 2017;130:383-98.

[32] Zare Yasser, Rhee Kyong Yop. Development of a conventional model to predict the electrical conductivity of polymer/carbon nanotubes nanocomposites across waviness and contact effects. Compos Part A-Appl S 2017;100:305-12.

[33] Hajmohammad Mohammad Hadi, Kolahchi Reza, Zarei Mohammad Sharif, Nouri Amir Hossein. Dynamic response of auxetic honeycomb plates integrated with agglomerated CNT-reinforced face sheets subjected to blast load based on visco-viscoelastic theory. Int J Mech Sci 2019;153-154:391-401.

[34] Kundalwal S, Ray M. Effect of carbon nanotube waviness on the effective thermoelastic properties of a novel continuous fuzzy fiber reinforced composite. Compos B Eng 2014;57:199-209.

[35] Kulkarni M, Carnahan D, Kulkarni K. Elastic response of a carbon nanotube fiber reinforced polymeric composite: a numerical and experimental study. Compos B Eng 2010;41(5):414-21.

[36] Shan H, Chou T. Transverse elastic moduli of unidirectional fiber composites with fiber/matrix interfacial debonding. Compos Sci Technol 1995;53(4):383-91.

[37] Kundalwal S, Ray M. Thermoelastic properties of a novel fuzzy fiber reinforced composite. J Appl Mech 2013;80(6):061011.

[38] Wittmaack Bernard K, Volkov Alexey N, Zhigilei Leonid V. Mesoscopic modeling of the uniaxial compression and recovery of vertically aligned carbon nanotube forests. Compos Sci Technol 2018;166:66-85.

[39] Hassanzadeh-Aghdam MK, Ansari R, Mahmoodi MJ. Micromechanical estimation of biaxial thermomechanical responses of hybrid fiber-reinforced metal matrix nanocomposites containing carbon nanotubes. Mech Mater 2018;119:1-15.

[40] Li Richard, Lachman Noa, Florin Peter, Wagner HDaniel, Wardle Brian L. Hierarchical and interfacial properties of carbon nanotube unidirectional composites with preserved tensile and interfacial properties. Compos Sci Technol 2015;117:139-45.

[41] Subramanian Nithya, Koo Bonsung, Venkatesan Karthik Rajan, Chattopadhyay Aditi. Interface mechanics of carbon fibers with radially-grown carbon nanotubes. Carbon N Y 2018;134:123-33.

[42] Hassanzadeh-Aghdam MK, Mahmoodi MJ, Ansari R. Micromechanics-based characterization of mechanical properties of fuzzy fiber-reinforced composites containing carbon nanotubes. Mech Mater 2018;118:31-43.

[43] Haghgoo Mojtaba, Ansari Reza, Hassanzadeh-Aghdam Mohammad Kazem. Effective elastoplastic properties of carbon nanotube-reinforced aluminum nanocomposites considering the residual stresses. J Alloy Compd 2018;752:476-88.

[44] Qiu YP, Weng GJ. On the application of mori-tanaka's theory involving transversely isotropic spheroidal inclusions. Int J Eng Sci 1990;28(11):1121-37.

[45] Calestani D, Culiolo M, Villani M, Delmonte D, Solzi M, Kim Tae-Yun, Kim Sang-Woo, Marchini L, Zappettini A. Functionalization of carbon fiber tows with ZnO nanorods for stress sensor integration in smart composite materials. Nanotechnology 2018;29:335501.

[46] Cheng Yi, Cheng Hui, Zhang Kaifu, Jones Kevontrez, Gao Jiaying, Hu Junshan, Li Hailin, Liu Wing Kam. A sequential homogenization of multi-coated micromechanical model for functionally graded interphase composites. Comput Mech 2019;1-17.