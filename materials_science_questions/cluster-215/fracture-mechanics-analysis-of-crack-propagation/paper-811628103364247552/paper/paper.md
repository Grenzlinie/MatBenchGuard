# Effect of crack density and connectivity on the permeability of microcracked solids
Zhou Chunsheng $^{a,b}$, Li Kefei $^{a,b,*}$, Pang Xiaoyun $^{a,b}$
$^{a}$ Key Laboratory of Civil Engineering, Safety and Durability of China Education Ministry, PR China
$^{b}$ Civil Engineering Department, Tsinghua University, 100084 Beijing, PR China

---

## ARTICLE INFO
**Article history:**
Received 9 November 2010
Received in revised form 28 April 2011
Available online 30 August 2011

**Keywords:**
Microcrack
Permeability
Connectivity
Interaction direct derivative
Representative volume element

---

## ABSTRACT
In composite theory microcracks in solid are usually treated as degenerated inclusions separately embedded in matrix. For heterogeneous engineering composites like concrete and rock, the real cracking patterns are more complicate and quite different from this assumption due to the natural clustering and inter-connection of microcracks. This paper investigates the permeability of solids containing a crack network with finite connectivity following both theoretical and numerical approaches. Firstly, no connectivity is assumed for cracks and the interaction direct derivative (IDD) method is employed to obtain the crack-altered permeability of solids. Then the amplification of permeability by crack connectivity is quantified for parallel crack cases and for general crack patterns. This amplification effect is modeled by a crack length augmentation factor. In this way the IDD method is extended to evaluate the permeability of cracked solids for a finite crack connectivity before total percolation of cracks. Afterwards, by a carefully designed Monte-Carlo algorithm, the representative volume element (RVE) is built numerically for cracked solids with cracks having random spatial locations and random lengths. The permeability of 2D cracked solids is solved by finite element method (FEM). Through this numerical tool, the effect of both crack density and connectivity on the permeability is solved, and especially the relation between crack connectivity and the geometrical coefficient of crack clustering is put into evidence. From this study it is showed that the extended IDD method can be adapted to a microcracked solid with finite connectivity and can provide good estimates for the permeability.

© 2011 Elsevier Ltd. All rights reserved.

---

## 1. Introduction
Evaluating the effective properties, physical or mechanical, of composite materials has applications in various areas of materials science and engineering. Generally, the effective properties depend not only on the properties of each phase but also on the specific microstructure of material, including phase volume fractions, spatial distribution and geometry of phase domains as well as possible clustering and connectivity of the phases (Torquato, 1991). The classical composite theory treats the phase topology as matrix-inclusion or polycrystalline packing structure (Nemat-Nasser and Hori, 1993). For the matrix-inclusion structure, only the matrix phase is continuous and inclusions are separately embedded in matrix without overlapping. In this image, cracks in solid are regarded as special inclusions, degenerated from flat circular or elliptics dispersed in matrix (Hoenig, 1983; Kachanov, 1992).

Heterogeneous composites like concrete and rock have a typical matrix-inclusion structure with aggregates or mineral grains as inclusions dispersed randomly in a porous matrix (Mehta and Monteiro, 2006). Under mechanical loads or environmental actions, the damage process of this matrix-inclusion structure includes the nucleation of new

---

* Corresponding author at: Civil Engineering Department, Tsinghua University, 100084 Beijing, PR China. Tel./fax: +86 10 6278 1408.
E-mail address: likefei@tsinghua.edu.cn (K. Li).

0167-6636/$ - see front matter © 2011 Elsevier Ltd. All rights reserved.
doi:10.1016/j.mechmat.2011.08.011

![](./images/811628103364247552_1.jpg)

Fig. 1. Microcracks in concrete samples subjected to drying (left) and compressive loads (right).

microcracks as well as the propagation, clustering and connecting of existing ones (Krajcinovic, 2000). The clustering and inter-connection make the microcracking pattern obviously different from the assumption of isolated crack inclusions in matrix-inclusion structure (Ringot and Bascoul, 2001), see Fig. 1. Properties study on cracked concretes showed an important influence of crack orientation and connecting degree on the material permeability (Jensen and Chatterji, 1996), and the connectivity of cracks should be considered as an intrinsic parameter for damage process (Krajcinovic, 1997).

Thus, how to identify the connectivity of cracks and take it into account in the effective properties analysis deserves more attention. The most commonly used micromechanic models for properties evaluation of solids containing crack-like inclusions are based on effective medium theory (EMT) (Hashin, 1968). These models include the dilute solution (Kachanov, 1992), the self-consistent scheme (SCS) (Budiansky and O'Connell, 1976), Mori-Tanaka method (MT) (Benveniste, 1987), the differential scheme (DS) (Norris, 1985) and the generalized self-consistent scheme (GSCS) (Huang et al., 1994), all using the concept of the Eshelby tensor. The EMT models reduce the properties analysis to one isolated inclusion placed into an "effective matrix" or undergoing an "effective field". However, direct application of this notion to connected cracks, especially for mechanical stability analysis, seems problematic since the inter-connections of cracks determines the mechanical behavior and the overall effect of connected cracks cannot easily be represented by an equivalent crack (Kachanov, 1992; Guéguen et al., 1997). The continuum percolation theory provide an alternative way to consider the connectivity of crack network and its impact on the material permeability (Efros and Kisin, 1986). In percolation theory the permeability of matrix is neglected completely, the analysis is focused on the formation process of percolation (critical) path and the permeability estimate is only valid at or above the percolation threshold (Xia and Thorpe, 1988; Hunt, 2001). However, its validity for crack connectivity far below the percolation threshold is still to be explored (Berkowitz and Balberg, 1993). The EMT and percolation theory are incompatible as they are founded on mutually exclusive basic assumptions (Guéguen et al., 1997). For engineered materials like concrete the analysis of physical properties as permeability is of interest in its service state, for durability considerations, with a finite connecting degree for cracks and rather below percolation state. Apparently, neither aforementioned approach can be used directly. The numerical simulation provides the last alternative for permeability analysis. The mechanical properties of cracked solids with crack clustering has been investigated numerically, through either representative volume element (RVE) or repeating unit cell (RUC) (Drago and Pindera, 2007), to study the effect of crack orientation (Kushch et al., 2009) and clustering (Kushch et al., 2009) on the stiffness and stress intensity factor.

This paper attempts to investigate the impact of crack connectivity on the solid permeability following both micromechanic and numerical approaches. The solid is considered to have a 2D homogeneous matrix and dispersed rectilinear cracks. For case of cracks without contact, the authors derive the explicit estimate of crack-altered permeability following the interaction direct derivative (IDD) method of the effective medium theory, and this solution is extended to cracks with finite connectivity. At the same time, the RVE is constructed numerically containing randomly oriented cracks. Through the numerical tool, the IDD estimate for isolated cracks is validated and the geometrical coefficient of crack clustering in the extended IDD model is studied in terms of crack connectivity and density in details. Finally the description of crack connectivity and its impact on solid permeability is discussed in depth.

## 2. IDD estimate for permeability

For the inclusion-matrix structure of composites, a micromechanic scheme named the effective self-consistent

scheme (ESCS), derived from three-phase assumption, has been recently proposed by Zheng and Du (2001). This scheme takes into account the various inclusion distributions as well as the interaction between inclusions and their immediately surrounding matrix, giving solutions for both linear mechanical and physical properties. The simplified method of this scheme, the interaction direct derivative (IDD) method, provides explicit solutions and is verified to have second order accuracy with respect to volume fraction of inclusions (Du and Zheng, 2002). Meanwhile, the dilute solution of conductivity of a homogeneous matrix with ellipsoidal inclusions has been derived by Shafiro and Kachanov (2000). Based on this dilute solution, the IDD method is employed to derive the effective permeability of 2D and 3D microcracked solids having isolated cracks in this section and extend to cracks of finite connectivity in next section.

### 2.1. IDD estimate method

Solution of linear physical properties of cracked solids, for electrical and thermal conduction, diffusion and liquid flow, can be generalized as the linear conduction problem and described as follows:
$$
\boldsymbol{F}(x)=\boldsymbol{S}(x) \cdot \boldsymbol{G}(x), \quad \nabla \cdot \boldsymbol{F}=0, \quad \nabla \times \boldsymbol{G}=0 \tag{1}
$$
where $\boldsymbol{F}(x)$ is a flux, $\boldsymbol{G}(x)$ is a driving force (gradient of some physical potential such as electrical potential, temperature or pressure) and $\boldsymbol{S}(x)$ denotes the conductivity or permeability. Since this physical law interrelates vectorial quantities, the tensor $\boldsymbol{S}$ characterizing the physical properties is of second-order. The analysis is therefore simpler than for elastic properties (in that case $\boldsymbol{S}$ is a fourth-order tensor). In our case for permeability evaluation, $\boldsymbol{S}$ is named the permeability tensor and $\boldsymbol{C}$ the permeation resistivity tensor. Moreover, one has,
$$
\boldsymbol{C}=\boldsymbol{S}^{-1}, \quad \boldsymbol{G}=\boldsymbol{C} \cdot \boldsymbol{F} \tag{2}
$$

In the following the permeability and resistivity tensors for matrix phase and inclusion $\omega_{i}$ are labelled by 0 and $i$ respectively, and the tensors without label stand for the effective medium. The permeability increment $\boldsymbol{H}$ of effective medium and fluctuations $\boldsymbol{H}_{i}$ of inclusion $\omega_{i}$, compared to matrix, are defined as,
$$
\boldsymbol{H}=\boldsymbol{S}-\boldsymbol{S}_{0}, \quad \boldsymbol{H}_{i}=\boldsymbol{S}_{i}-\boldsymbol{S}_{0} \tag{3}
$$

From the effective self-consistent scheme (Zheng and Du, 2001), the dilute estimation of the increment for linear physical properties, $\boldsymbol{H}^{\mathrm{d}}$, can also be expressed as,
$$
\boldsymbol{H}^{\mathrm{d}}=\sum_{i} c_{i}\left(\boldsymbol{H}_{i}^{-1}+\boldsymbol{\Omega}_{i}^{0}\right)^{-1} \tag{4}
$$
where $c_{i}$ is the volumetric fraction of inclusion $\omega_{i}, \boldsymbol{\Omega}_{i}^{0}$ is a stiffness-type tensor and called the eigenstiffness tensor of inclusion $\omega_{i}$. It characterizes the shape and orientation of $\omega_{i}$, defined as
$$
\boldsymbol{\Omega}_{i}^{0}=\boldsymbol{C}_{0} \cdot\left(\boldsymbol{I}-\Sigma_{i}^{0}\right) \tag{5}
$$
where $\boldsymbol{I}$ denotes the second-order identity tensor and $\boldsymbol{\Sigma}_{i}^{0}$ is the Eshelby tensor of inclusion $\omega_{i}$ for linear conductivity problem. For a solid containing $N$ groups of inclusions (inclusions having the same eigenstiffness tensor roll into one group), the effective properties tensor $\boldsymbol{H}$ is obtained through IDD method in explicit expression as (Du and Zheng, 2002),
$$
\boldsymbol{H}^{\mathrm{idd}}=\left(\boldsymbol{I}-\sum_{i=1}^{N} \boldsymbol{H}_{i}^{\mathrm{d}} \cdot \boldsymbol{\Omega}_{D i}^{0}\right)^{-1} \boldsymbol{H}^{\mathrm{d}} \tag{6}
$$
where $\boldsymbol{\Omega}_{D i}^{0}$ is the eigenstiffness tensor of matrix atmosphere $\omega_{i}^{D}$ with respect to the yet-unknown effective matrix medium. More mathematical details can be referred to Zheng and Du (2001).

### 2.2. Dilute estimate for linear physical properties

The analytical dilute estimate of conductivity with ellipsoidal inclusions has been derived by Shafiro and Kachanov (2000). The analytical solution is to be used and adapted here for permeability evaluation of solids containing crack-like inclusions. Considering a reference volume $V$ of material with permeability $\boldsymbol{S}_{0}$ containing one ellipsoidal inclusion $\omega_{i}$ ( $a_{1,2,3}$ are semi axes of the inclusion parallel to coordinate axes $x_{1,2,3}$ and $\boldsymbol{e}_{1,2,3}$ are unit vectors along them). The dilute estimate for permeability is given as,
$$
\boldsymbol{H}_{i}^{\mathrm{d}}=c_{i} \boldsymbol{H}_{i} \cdot \boldsymbol{A} \tag{7}
$$
and the tensor $\boldsymbol{A}$ is equivalent to the localization tensor in elastic problem, and is diagonal for inclusion with isotropic permeability,
$$
\boldsymbol{A}=\left[\boldsymbol{I}+\boldsymbol{H}_{i} \cdot \boldsymbol{S}_{0}^{-1} \cdot \boldsymbol{J}\right]^{-1} \tag{8}
$$

Here the geometry tensor $\boldsymbol{J}$ is also diagonal with isotropic inclusion. Its components $J_{j=1,2,3}$ are given in terms of standard elliptic integrals as,
$$
J_{1}=\frac{a_{1} a_{2} a_{3}}{2} \int_{0}^{\infty} \frac{d u}{\left(a_{1}^{2}+u\right) \sqrt{\left(a_{1}^{2}+u\right)\left(a_{2}^{2}+u\right)\left(a_{3}^{2}+u\right)}} \tag{9}
$$
with $J_{2}$ and $J_{3}$ obtained by cyclic permutations of all indices 1,2 and 3. For some special cases, $J_{j}$ can be simplified and relevant details can be found in Shafiro and Kachanov (2000). The dilute estimate Eq. (7) can be further arranged as,
$$
\boldsymbol{H}_{i}^{\mathrm{d}}=c_{i} \boldsymbol{H}_{i} \cdot \boldsymbol{A}=c_{i}\left[\boldsymbol{H}_{i}^{-1}+\boldsymbol{S}_{0}^{-1} \cdot \boldsymbol{J}\right]^{-1} \tag{10}
$$

By equating Eqs. (4) and (10) for inclusion $\omega_{i}$, one gets the eigenstiffness tensor $\boldsymbol{\Omega}_{i}^{0}$ and Eshelby tensor $\Sigma_{i}^{0}$ as,
$$
\boldsymbol{\Omega}_{i}^{0}=\boldsymbol{S}_{0}^{-1} \cdot \boldsymbol{J} \quad \text { and } \quad \boldsymbol{\Sigma}_{i}^{0}=\boldsymbol{I}-\boldsymbol{J} \tag{11}
$$

The eigenstiffness tensors $\boldsymbol{\Omega}_{i}^{0}$ and $\boldsymbol{\Omega}_{D i}^{0}$ can be obtained by Eq. (11) with the known geometry parameters of inclusion and matrix atmosphere. Then the IDD estimate for $N$ groups of inclusions can be solved by Eq. (6). Thus, the key point of applying IDD estimate is to determine the geometrical parameters of inclusion-matrix atmosphere which can best represent the interaction between inclusions and their immediate matrix.

![](./images/811628103364247552_2.jpg)

Fig. 2. Crack inclusion and its matrix atmosphere.

### 2.3. IDD estimate with ellipsoidal or elliptical matrix atmosphere

Ellipsoidal or elliptical matrix atmospheres have been adopted for microcracked solids (Huang et al., 1994). For crack inclusions in this study, the corresponding matrix atmosphere, the immediate part of matrix associated and interacting with the crack inclusion, is chosen as ellipsoidal for 3D case and elliptical for 2D case with their principal axes aligned on the crack plane (Fig. 2). The crack density in solid adopts the definition of volume (area) fraction of cracks with respect to the reference volume (area),

$$
\rho_{2}=\frac{\sum a_{i}^{2}}{A}, \quad \rho_{3}=\frac{\sum a_{i}^{3}}{V}
\tag{12}
$$

Here the crack volume is denoted by the cubic (square) of its half-length $a_{i}$. The dimension of the corresponding matrix atmosphere is determined so as to keep the same density in the crack-atmosphere cell. For two dimensional analysis, the lengths of semi-axes for elliptical matrix atmosphere are

$$
a_{1}=a+b, \quad a_{2}=b
\tag{13}
$$

where $a$ is the half-length of the crack. To observe the crack density $\rho_{2}$ in reference area, $b$ can be evaluated by the crack density,

$$
\frac{a^{2}}{\pi(a+b) b}=\rho_{2}, \quad\left(\frac{b}{a}\right)^{2}+\frac{b}{a}=\frac{1}{\pi \rho_{2}}
\tag{14}
$$

And for three dimensional analysis, the geometrical parameters for ellipsoidal atmosphere can be evaluated as,

$$
\frac{3 a^{3}}{4 \pi(a+b)^{2} b}=\rho_{3}, \quad \frac{b}{a}\left(\frac{b}{a}+1\right)^{2}=\frac{1}{\pi \rho_{3}}
\tag{15}
$$

#### 2.3.1. Three dimensional case

Let us limit the analysis on the matrix-crack structure with large contrast of permeability between the matrix and cracks. Actually it is true for most brittle engineering materials like cement-based materials and rocks: the material matrix intrinsic permeability is at the order of $1 \sim 10 \times 10^{-18} \mathrm{~m}^{2}$ and a microcrack with opening of $1 \mu \mathrm{m}$ has a permeability of 6 order higher of magnitude. Assume that the permeability of microcracks is infinite compared to that of the matrix, $\boldsymbol{S}_{i} \rightarrow \infty$. Then, $\boldsymbol{H}_{i}^{-1} \rightarrow 0$ in Eq. (10). Thus, the dilute estimation of ellipsoidal inclusion can be simplified as,

$$
\boldsymbol{H}_{i}^{\mathrm{d}}=c_{i} \boldsymbol{S}_{0} \cdot \boldsymbol{J}^{-1}
\tag{16}
$$

For spheroid inclusion, let $a_{1}=a_{2}=a>a_{3}$, aspect ratio $\gamma=a /$ $a_{3}$, then

$$
J_{1}=J_{2}=F(\gamma), \quad J_{3}=1-2 F(\gamma)
\tag{17}
$$

where

$$
F(\gamma)=\frac{1-g(\gamma)}{2\left(1-\gamma^{2}\right)}, \quad g(\gamma)=\frac{\gamma^{2}}{\sqrt{\gamma^{2}-1}} \arctan \sqrt{\gamma^{2}-1} \quad(18)
$$

if $\gamma \rightarrow \infty$, then $F(\gamma) \rightarrow 0, c_{i} \rightarrow 0$, but

$$
\lim _{\gamma \rightarrow \infty} \frac{c_{i}}{F(\gamma)}=\frac{16 a_{i}^{3}}{3 V}
\tag{19}
$$

The dilute estimation for penny-shaped microcracks can be given as

$$
\boldsymbol{H}^{\mathrm{d}}=\sum_{i} \boldsymbol{H}_{i}^{\mathrm{d}}=\sum_{i} \frac{16}{3} \frac{a_{i}^{3}}{V} \boldsymbol{S}_{0} \cdot\left(\boldsymbol{I}-\boldsymbol{e}_{3} \boldsymbol{e}_{3}\right)_{i}
\tag{20}
$$

The aspect ratio of matrix atmosphere $\gamma_{D}$ can be derived from Eq. (15) and

$$
\boldsymbol{\Omega}_{D i}^{0}=\boldsymbol{S}_{0}^{-1} \cdot\left[F\left(\gamma_{D}\right)\left(\boldsymbol{I}-\boldsymbol{e}_{3} \boldsymbol{e}_{3}\right)+\left(1-2 F\left(\gamma_{D}\right)\right) \boldsymbol{e}_{3} \boldsymbol{e}_{3}\right]_{i}
\tag{21}
$$

Substituting the above two equations into Eq. (6) yields the IDD approximate estimation for microcracked solid with any distribution. Supposing that the microcracks are uniformly distributed in the solid and the overall permeability is isotropic, then

$$
\boldsymbol{H}^{\mathrm{idd}}=\frac{\frac{32}{9} \rho_{3}}{1-\frac{32 F\left(\gamma_{D}\right)}{9} \rho_{3}} \boldsymbol{S}_{0}
\tag{22}
$$

Since the aspect ratio $\gamma_{D}$ of the chosen matrix atmosphere can be derived from Eq. (15), this solution contains only one fundamental factor, the crack density $\rho_{3}$.

#### 2.3.2. Two dimensional case

Two dimension analysis of permeability can be degenerated from the above 3D case. Supposing the three semi-axes $a_{1}>a_{2}>a_{3}$, 2D analysis is the limiting case of $a_{1} \rightarrow \infty$ and $a_{3} \rightarrow 0$. For super-permeable microcracks, the dilute estimation of compliance increment for crack inclusion $\omega_{i}$ is,

$$
\boldsymbol{H}_{i}^{\mathrm{d}}=c_{i} \boldsymbol{S}_{0} \cdot \boldsymbol{J}^{-1}
\tag{23}
$$

Since $a_{1} \rightarrow \infty$, then

$$
J_{1}=0, \quad J_{2}=\frac{a_{3}}{a_{2}+a_{3}}, \quad J_{3}=\frac{a_{2}}{a_{2}+a_{3}}
\tag{24}
$$

In the plane normal to $\boldsymbol{e}_{1}$, the in-plane permeability increment $\overline{\boldsymbol{H}}_{i}^{\mathrm{d}}$ can be arranged as

$$
\overline{\boldsymbol{H}}_{i}^{\mathrm{d}}=\frac{\pi a_{2} a_{3}}{A} \boldsymbol{S}_{0} \cdot\left(\frac{a_{2}+a_{3}}{a_{3}} \boldsymbol{e}_{2} \boldsymbol{e}_{2}+\frac{a_{2}+a_{3}}{a_{2}} \boldsymbol{e}_{3} \boldsymbol{e}_{3}\right)_{i}
\tag{25}
$$

As $a_{3} \rightarrow 0$, the dilute estimation is

$$
\overline{\boldsymbol{H}}^{\mathrm{d}}=\sum_{i} \frac{\pi a_{i}^{2}}{A} \boldsymbol{S}_{0} \cdot \boldsymbol{e}_{2} \boldsymbol{e}_{2}
\tag{26}
$$

where $a_{i}$ is the half length of $i$ th microcrack inclusion. If $2 \mathrm{D}$ elliptical matrix atmosphere is chosen its aspect ratio $\gamma_{D}$ can be derived from Eq. (14). The 2D eigenstiffness tensor is

$$
\overline{\boldsymbol{\Omega}}_{D i}^{0}=\boldsymbol{S}_{0}^{-1} \cdot\left[\gamma_{D} \boldsymbol{e}_{2} \boldsymbol{e}_{2}+\left(1-\gamma_{D}\right) \boldsymbol{e}_{3} \boldsymbol{e}_{3}\right]_{i}
\tag{27}
$$

Thus the relative permeability component along the crack's orientation $S_{1} / S_{0}$ can be derived by IDD estimation Eq. (6) for solid with parallelly arranged microcracks,

![](./images/811628103364247552_3.jpg)

Fig. 3. Ideal model for partly connected parallel cracks.

$$
\frac{S_{1}}{S_{0}}=\frac{1+\pi\left(1-\gamma_{D}\right) \rho_{2}}{1-\pi \gamma_{D} \rho_{2}}
\tag{28}
$$

The relative permeability $S/S_0$ for isotropic solid with randomly distributed microcracks is
$$
\frac{S}{S_{0}}=\frac{1+\frac{\pi}{2}\left(1-\gamma_{D}\right) \rho_{2}}{1-\frac{\pi}{2} \gamma_{D} \rho_{2}}
\tag{29}
$$
where
$$
\gamma_{D}=\frac{\sqrt{1+\frac{4}{\pi \rho_{2}}}-1}{\sqrt{1+\frac{4}{\pi \rho_{2}}}+1}
\tag{30}
$$

Considering
$$
\lim _{\rho_{2} \rightarrow \infty} \gamma_{D} \rho_{2}=\frac{1}{\pi}
\tag{31}
$$
the denominator of right side in Eq. (29) tends to a finite value, 1/2. It implies that no percolation for permeation can be predicted by this model. This is consistent with the assumptions of IDD method: the crack-inclusions are considered embedded in their immediate matrix atmospheres and separated from one and another whatever the crack density is.

## 3. Extended model for solids with connected microcracks

As crack density increases and crack interactions become stronger, the mutual positions of cracks become increasingly important, especially for inter-connected case, as shown later in Fig. 5 (right). In above sections, an equivalent crack density $\rho_{2}$ or $\rho_{3}$ is employed to characterize the microcracks. To describe the partly connected microcracks, the connectivity of cracks, $\phi$, is introduced as follow,
$$
\phi=1-\sum_{i=1}^{m} a_{i}^{2} \bigg/ \sum_{j=1}^{n} a_{j}^{2}
\tag{32}
$$
where $n$ is the total number of microcracks, $m$ is the number of isolated ones and $a_{i}$ denotes the half length of $i$ th crack.

### 3.1. Parallel cracks with connectivity

To obtain some analytical results on the influence of connectivity $\phi$ on effective permeability of solids, we start from the simple case of parallel cracks with partial connectivity. Suppose that in an infinite matrix there are $n$ parallel microcracks with identical half-length $a$, cf. Fig. 3. By Eq. (28) the effective permeability $S_{1}$ along the crack orientation can be expressed in terms of the initial 2D density $\rho_{2}^{0}$,
$$
\frac{S_{1}}{S_{0}}=1+\frac{\pi \rho_{2}^{0}}{1-\pi \gamma_{D}^{0} \rho_{2}^{0}}, \quad \rho_{2}^{0}=\frac{n a^{2}}{A}
\tag{33}
$$
where $n$ is the total number of microcracks in the reference area $A$ of 2D matrix with the superscript "0" for the initial state without connectivity.

Firstly, as any $r$ microcracks $(r \geqslant 2)$ with half-length $a$ are connected together these cracks are considered as one crack with half-length $ra$. By the connectivity definition in Eq. (32), compared to initial state, the connectivity $\phi_{0}^{r}$ is
$$
\phi_{0}^{r}=\frac{r}{n}
\tag{34}
$$
and the density $\rho_{2}^{r}$ now becomes
$$
\rho_{2}^{r}=\frac{(n-r) a^{2}+(r a)^{2}}{n a^{2}} \times \frac{n a^{2}}{A}=\left[1+(r-1) \phi_{0}^{r}\right] \rho_{2}^{0}
\tag{35}
$$

Secondly, for the case that any $2t(t \geqslant 1)$ microcracks with half-length $a$ are connected to form $t$ microcracks each with half-length $2a$, compared to the initial state, the connectivity $\phi_{0}^{2t}$ is
$$
\phi_{0}^{2 t}=\frac{2 t}{n}
\tag{36}
$$
and the density $\rho_{2}^{2t}$ is
$$
\rho_{2}^{2 t}=\frac{(n-2 t) a^{2}+t(2 a)^{2}}{n a^{2}} \times \frac{n a^{2}}{A}=\left(1+\phi_{0}^{2 t}\right) \rho_{2}^{0}
\tag{37}
$$

More generally, if the initial microcracks are randomly connected and become a new network with $m_{0}$ isolated microcracks with half-length $a$, $j$ connected cracks with half-length $m_{1}a, m_{2}a, \dots, m_{j}a$, ($\sum_{i=0}^{j} m_{i}=n$). Compared to the initial state the connectivity $\phi_{0}^{j}$ now is
$$
\phi_{0}^{j}=1-\frac{m_{0}}{n}=\frac{m_{1}+m_{2}+\cdots+m_{j}}{n}
\tag{38}
$$
and equivalent density $\rho_{2}^{j}$ satisfies
$$
\begin{aligned}
\frac{\rho_{2}^{j}}{\rho_{2}^{0}} &=\frac{\left(m_{1}^{2}+m_{2}^{2}+\cdots+m_{j}^{2}\right) a^{2}+m_{0} a^{2}}{n a^{2}} \\
&=1+\left(\sum_{i=1}^{j} m_{i}^{2} \bigg/ \sum_{i=1}^{j} m_{i}-1\right) \phi_{0}^{j}
\end{aligned}
\tag{39}
$$

As the microcracks are uniformly connected, i.e. $m_{1}=m_{2}=\cdots=m_{j}$, the left side of Eq. (39) attains its minimum.

Thirdly, if the reference area is composed of $m_0$ no-connected cracks with half-length $a$, $j$ cracks each with half-length $m_i a$ ($m_0 + m_1 + \cdots + m_j = n$). Now any two cracks, with half-length $m_r a$ and $m_t a$, are connected together forming a new crack with half-length $(m_r + m_t)a$. The relative connectivity $\phi_{r,t}^{r+t}$, after this combination operation, is
$$
\phi_{r, t}^{r+t}=\frac{m_{r}^{2}+m_{t}^{2}}{m_{0}^{2}+m_{1}^{2}+\cdots+m_{j}^{2}} \tag{40}
$$
while the density $\rho_{2}^{r+t}$ satisfies
$$
\frac{\rho_{2}^{r+t}}{\rho_{2}}=1+\frac{2 m_{r} m_{t}}{m_{0}^{2}+m_{1}^{2}+\cdots+m_{j}^{2}}=1+\frac{2 m_{r} m_{t}}{m_{r}^{2}+m_{t}^{2}} \phi_{r, t}^{r+t} \tag{41}
$$

From the analysis of above three special cases, it can be expected that the equivalent density $\rho_{2}'$ of randomly connected cracks can be adjusted by their connectivity $\phi$,
$$
\rho_{2}^{\prime}=(1+\beta \phi) \rho_{2} \tag{42}
$$
where $\beta$ is a constant closely related to the initial and final patterns of crack inter-connection. From Eq. (39), one can see that coefficient $\beta$ is smaller when microcracks are more evenly connected and large clustering of cracks gives big $\beta$ value. This equation states a simple fact that connectivity of cracks changes (amplifies in this case with $\beta>0$) the apparent crack density.

### 3.2. Randomly oriented cracks with connectivity

When two or more microcracks are randomly connected together, they may amplify or shield each other for permeation, referred to as amplifying or shielding effect of clustering (Kachanov, 1992). To quantify these amplifying and shielding effects, one has to cope with the detailed geometry of the connected cracks. Thus it is rather difficult, if not impossible, to account for the connectivity effect in the effective permeability estimate through an analytical way. However, motivated by the above analysis on parallel crack model, one can expect that the rule stated in Eq. (42) still holds.

As a microcrack is connected with another one, it can be assumed that the contribution of this connectivity to the effective permeability is equal to change its half-length $a_i$ to an equivalent length $a_i'$ for an isolated case, cf. Fig. 4,
$$
a_{i}^{\prime}=(1+\alpha) a_{i} \tag{43}
$$

Here the coefficient $\alpha$ is a physically meaningful constant characterizing the amplifying effect $(\alpha>0)$ or shielding effect $(\alpha<0)$ of crack intersection. Supposing the crack network contains $n$ microcracks and $m$ microcracks (labelled as $1,2,\dots m$) are isolated from the others, the equivalent density $\rho_{2}'$ is
$$
\begin{aligned}
\rho_{2}^{\prime} & =\frac{1}{A}\left(\sum_{i=1}^{m} a_{i}^{2}+\sum_{i=m+1}^{n}(1+\alpha)^{2} a_{i}^{2}\right) \\
& =(1-\phi) \rho_{2}+(1+\alpha)^{2} \phi \rho_{2}
\end{aligned} \tag{44}
$$
which can be further arranged as
$$
\rho_{2}^{\prime}=(1+\beta \phi) \rho_{2}, \quad \beta=\alpha^{2}+2 \alpha \tag{45}
$$

It is noted that only one coefficient $\alpha$ is chosen for all connected cracks so this coefficient is not specific to any individual crack. This equation is compatible with Eq. (42) for parallel crack model.

![](./images/811628103364247552_4.jpg)

Fig. 4. Equivalent models for connected cracks and isolated cracks.

Incorporating the equivalent density $\rho_{2}'$ with connectivity $\phi$, one can readily derive the IDD estimate for effective permeability of solids with connected cracks and the IDD estimate can be extended to crack networks with connectivity. As super-permeable microcracks are randomly oriented and connected and the matrix is isotropic, the effective permeability can be calculated by Eq. (29) as,
$$
\frac{S}{S_{0}}=1+\frac{\frac{\pi}{2} \rho_{2}^{\prime}}{1-\frac{\pi}{2} \gamma_{D}^{\prime} \rho_{2}^{\prime}} \tag{46}
$$

Following the same notion, the effective conductivity for 3D case with randomly oriented and connected cracks can be derived from Eq. (22). As for the physcially meaningful coefficients $\alpha, \beta$, their determination is not possible without knowledge on the detailed geometry of crack connection and intersection. Their quantification is given in the numerical analysis part of paper.

## 4. Numerical analysis

This part is dedicated to the numerical verification of the available explicit solution of permeability from the IDD method as well as the parameter study for the geometry coefficients proposed in the extended IDD model for cracks with connectivity. As suggested by Kachanov (1992) and Huang et al. (1996), numerical tests can be a reliable way to validate the analytical estimates if a properly designed representative volume element (RVE) is constructed. The numerical analysis is limited to 2D case in this section.

### 4.1. Random cracks and connectivity

The representative volume element is constructed as such: (1) randomly oriented or parallel cracks are embedded in a homogeneous and isotropic matrix; (2) the orientation, positioning and half-length of cracks observe their respective statistical characteristics; (3) the crack density and connectivity are predetermined. To accomplish this RVE generation, we resort to Monte-Carlo algorithm.

The Monte-Carlo algorithm for RVE generation is described as follows. Given the crack density $\rho_2$, crack connectivity $\phi$ and the statistical characteristics of crack half-length $a_i$, orientation, the isolated part of microcracks, $(1-\phi)\rho_2$, are firstly generated and located in the 2D square randomly without connection. Then, the inter-connected part of microcracks, $\phi \rho_2$, are generated and located randomly one by one into the RVE. As one connected crack is positioned in RVE and intersects at least one existing crack, the generated crack is accepted. If the generated

crack overlaps the square boundary its outer part is trimmed off. At the same time, the connectivity of microcrack network in this stage is carefully calculated and checked, and the groups of isolated and connected cracks are updated. Then the expected densities of connected cracks and isolated cracks are calculated to preserve the target desnity $\rho_{2}$ and connectivity $\phi$. This procedure is repeated until the target density $\rho_{2}$ and connectivity $\phi$ are achieved. The Monte-Carlo algorithm constructed for this study can ensure an accuracy of connectivity $\phi$ within a relative error of 0.2%. In fact, this generation procedure is similar to the natural microcrack nucleation process of solids like quasi-brittle materials: cracks nucleate firstly at isolated sites and then extend to other sites and intersect with other cracks.

### 4.2. Finite element methods and meshing

The RVE containing microcracks is subject to a macroscopic average potential gradient $\boldsymbol{G}=\nabla p$, producing an average flux $\langle\boldsymbol{F}\rangle$. Because the permeation in Eq. (1) is linear the average flux is linearly related to the average gradient by,
$$
\langle\boldsymbol{F}\rangle=\boldsymbol{S}_{\text {eff }} \cdot \boldsymbol{G}
\tag{47}
$$
where $\boldsymbol{S}_{\text {eff }}$ is the effective permeability tensor. For our case, unit potential gradient is imposed along $x$ direction and null flux conditions are prescribed at the upper and lower boundaries of RVE, cf. Fig. 5. Then, the potential field $p$ in steady state satisfies the Laplace equation and can be easily solved by finite element method, i.e.
$$
S_{x}=\frac{\left\langle F_{x}\right\rangle}{G_{x}}=\left(\frac{1}{A} \int_{A} S_{i} \frac{\partial p}{\partial x} d x\right) / G_{x}
\tag{48}
$$

For simulation cases with randomly oriented cracks, the permeability is assumed isotropic. However the anistropy due to numerical reasons, e.g. random crack generations, can be hardly avoided. Thus the average permeability $S$ is retained as its effective value,
$$
S=\frac{S_{x}+S_{y}}{2}
\tag{49}
$$
where $S_{x, y}$ is the effective permeability along $x, y$ direction.

The meshing of 2D RVE begins with the crack elements. Firstly all endpoints and intersection points of cracks in the network are identified and treated as prelocated nodes, and 2-node elements are used to mesh all the cracks. The 2D matrix is then meshed with 6-node triangle elements, sharing the nodes of already generated crack elements. This meshing scheme assures the good coherence between crack elements and matrix elements in permeation problem solution. In the analysis, the super-permeable property of microcracks is modeled by a relative permeability ratio of $1 \times 10^{8}$ compared to matrix.

### 4.3. Solution without connectivity

This section is to validate the IDD estimate in Eqs. (28) and (29) by numerical tests. The RVE is a $100 \times 100$ square, cf. Fig. 5 (left), containing 41 parallel microcracks without connection and aligned hexagonally. The cracks have the same half-length ranging from $1 \sim 9$ and the effective permeability is solved by finite element method as aforementioned. The solved effective permeability along the orientation of microcracks is compared to IDD estimate by Eq. (28) with elliptical matrix atmosphere in Fig. 6 (left). In the same figure are also presented the dilute solution estimate and the differential scheme (DS) estimate. During the performed simulation range, $\rho_{2}=0 \sim 0.33$, it can be seen that both IDD and DS estimates achieve good accuracy.

For validation of Eq. (29), another RVE of $160 \times 160$ is constructed with randomly oriented and located cracks but without connection. The half-length of cracks observes normal distribution $\mathrm{N}\left(10,2.5^{2}\right)$ and the crack density ranges from $0 \sim 1$. For each crack density level, 10 crack patterns are generated and the corresponding effective permeabilities are solved. The IDD estimate is compared with numerical results in Fig. 6 together with the dilute solution estimate and DS estimate. The IDD estimate shows a good agreement for whole range of crack density while dilute and DS estimates lose their accuracy as crack density depasses 0.15 and 0.35 respectively. These simulations validate the accuracy of IDD method for parallel and random cracks in 2D cases without connectivity.

### 4.4. Solution with finite connectivity

To validate the IDD extended model and explore the coefficient $\beta$ of crack geometry, this section performs numerical tests for different crack density $\rho_{2}$ and connectivity $\phi$. The RVE is chosen as a square of $160 \times 160$. For the 2D simulations, 10 levels of crack density $\rho_{2}=0.1 \sim 1.0$ and 80 levels of connectivity $\phi=0 \sim 0.8$ are

![](./images/811628103364247552_5.jpg)

Fig. 5. 2D numerical sample (RVE) containing parallel cracks (left), randomly cracks without intersection (middle) and with intersection (right).

![](./images/811628103364247552_6.jpg)

Fig. 6. Numerical results and IDD estimates of effective permeability for parallel (left) and randomly oriented (right) microcracks.

chosen. For each crack density and connectivity level, 10 different crack patterns are generated by aforementioned Monte-Carlo algorithm. The orientation and location of microcracks are assumed to be random, and the half-length of cracks observes normal type distribution N(10,2.5²). The effective permeability of each RVE is solved by finite ele- ment method and the relative permeability is noted as the ratio between the effective permeability and the per- meability of the matrix, $(S/S_{0})_{RVE}$. Parallelly, the relative permeability is also evaluated for the corresponding no- connected cases by IDD method through Eq. (29), noted as $(S/S_{0})_{IDD}$. The ratio between $(S/S_{0})_{RVE}$ and $(S/S_{0})_{IDD}$ scales the importance of crack connection (intersection) on the effective permeability. In Fig. 7 is presented this ratio in terms of connectivity $\phi$ for different density levels $\rho_{2}$. It is observed that the connectivity contributes to increase the effective permeability of microcracked solids in a mono- tone manner and the importance of its impact is much related to the crack density. With high crack density $\rho_{2} \to 1.0$, the effect of connectivity can double the effective permeability as $\phi>0.7$.

From the numerical results, the geometry coefficient $\beta$ of connected cracks can be evaluated through Eqs. (45) and (46), illustrated in Fig. 8. The analysis of $\beta$ in terms of crack connectivity and density would be more instruc- tive for the effect of crack clustering on effective perme- ability. Fig. 8 shows the coefficient $\beta$ in terms of the connectivity $\phi$ for different crack density values $\rho_{2}$. From the figure the first observation is that the coefficient $\beta$ is both $\phi$-dependent and $\rho_{2}$-dependent.

As $\phi=0$, the crack network degenerates to the case of isolated cracks thus the coefficient $\beta$ has no physical mean- ing and can adopt any value. For very low connectivity $\phi$ $\leqslant 0.05$, the coefficient $\beta$ shows large fluctuation with re- spect to connectivity whatever the density, meaning a few connected microcracks can randomly accelerate $(\beta>0)$ or shield $(\beta<0)$ the permeation process. Thus, as the crack clustering is rare the coefficient $\beta$ is rather sensi tive to the detailed geometry of crack intersection/connec- tion. Afterwards, the evolution of $\beta$ in terms of connectivity shows different patterns for low density cases $(\rho_{2}=0.1 \sim$ 0.5) and high density cases $(\rho_{2}>0.5)$. For low crack density

![](./images/811628103364247552_7.jpg)

Fig. 7. Ratio of $(S/S_{0})_{RVE}$ to $(S/S_{0})_{IDD}$ in terms of connectivity $\phi$ for different crack density $\rho_{2}$.

![](./images/811628103364247552_8.jpg)

Fig. 8. Geometry coefficient $\beta$ in terms of connectivity $\phi$ for different crack density $\rho_{2}$.

![](./images/811628103364247552_9.jpg)

Fig. 9. Crack clustering and cluster size analysis for random crack networks with $\rho_{2}=1.0, \phi=0.1$ (up) and $\phi=0.8$ (down).

cases, the geometrical parameter $\beta$ stabilizes for almost entire connectivity range $(\phi=0.1 \sim 0.8)$ with $\beta=0.165$ $\sim 0.376$ for $\rho_{2}=0.1 \sim 0.4$. That means the amplification effect by crack connectivity for permeation process becomes stable and $\beta$ can be assumed to be only $\rho_{2}$-dependent. Thus, the geometrical coefficient $\beta$ is not sensitive to the crack clustering size or pattern. For high density cases $(\rho_{2}>0.5)$, this amplification effect by crack connection continues to increase for $(\phi=0.1 \sim 0.8)$ and larger $\beta$ values are obtained compared to low density cases. It is noted that for large $\phi$ values, $\beta$ depasses 1.0. That means, for any two connected cracks, the amplification effect for

permeation is further increased by other connected cracks. In other words, the crack clustering becomes important and some local percolation occurs. In this situation, the geometrical coefficient $\beta$ is both $\phi$-dependent and $\rho_2$-dependent, thus sensitive to the crack clustering. In Fig. 9 are illustrated the RVE and the corresponding clustering size statistics for $\rho_2=1.0$, $\phi=0.1$, 0.8.

## 5. Concluding remarks
1. This paper attempts to incorporate the crack network with finite connectivity into the effective permeability estimate for microcracked solids. For this purpose, the IDD method, derived form the ESCS scheme of micromechanics for inclusion-matrix composites, is adopted. Following this approach, the cracks are treated as special type of inclusions and the IDD estimate for permeability is derived from the dilute solution of crack-inclusion and its matrix atmosphere, successively for 3D and 2D cases. These estimates apply to the standard inclusion-matrix composites thus no connectivity is involved. To take into account the crack connection and intersection, the authors start from the parallel crack models to obtain the analytical relation between the crack apparent density and the crack connectivity. On the basis of same expression, the connectivity for randomly distributed cracks is modeled by an amplification factor $\alpha$ compared to the corresponding isolated cracks case. By this idealization, the explicit IDD solution for permeability of cracked solids is extended to crack networks with a finite degree of connectivity.

2. The Monte-Carlo algorithm is used in the numerical part of paper and the representative volume element (RVE) is built to validate the IDD estimates for no connected network and investigate the physical significance of geometrical coefficient $\beta$. From the performed numerical tests, the IDD estimates are firstly validated and show good accuracy for whole crack density range compared to dilute solution and DS scheme estimates. Then, comprehensive numerical tests on the permeability and $\beta$ coefficient are performed in terms of density and connectivity of crack networks. From the available results, the $\beta$ coefficient shows different evolution patterns for low and high crack density cases. For low density cases, the crack clustering facilitates the permeation process by crack bridging, the corresponding amplification effect remains rather stable for entire connectivity range and the $\beta$ coefficient is not sensitive to crack clustering. For high density cases, the amplification effect of crack connection is more pronounced and the geometrical coefficient $\beta$ is both connectivity-dependent and density-dependent, moreover, sensitive to crack clustering distribution and size.

## Acknowledgement
This work was supported by a grant from the Major State Basic Research Development Program of China (973 Program) (No. 2009CB623106).

## References
Benveniste, Y., 1987. A new approach to the application of Mori-Tanaka's theory in composite materials. Mechanics of Materials 6 (2), 147-157.

Berkowitz, B., Balberg, I., 1993. Percolation theory and its application to groundwater hydrology. Water Resources Research 29 (4), 775-794.

Budiansky, R., O'Connell, R.J., 1976. Elastic moduli of a cracked solid. International Journal of Solids and Structures 12 (2), 81-97.

Drago, A., Pindera, M., 2007. Micro-macromechanical analysis of heterogeneous materials: Macroscopically homogeneous vs periodic microstructures. Composites Science and Technology 67 (6), 1243-1263.

Du, D.-X., Zheng, Q.-S., 2002. A further exploration of the interaction direct derivative (IDD) estimate for the effective properties of multiphase composites taking into account inclusion distribution. Acta Mechanica 157 (1), 61-80.

Efros, A.L., Kisin, V.I., 1986. Physics and Geometry of Disorder: Percolation Theory. Mir Publishers, Moscow.

Guéguen, Y., Chelidze, T., Ravalec, M.L., 1997. Microstructures, percolation thresholds, and rock physical properties. Tectonophysics 279 (1), 23-35.

Hashin, Z., 1968. Assessment of the self consistent scheme approximation: conductivity of particulate composites. Journal of Composite Materials 2 (3), 284-300.

Hoenig, A., 1983. Thermal conductivities of a cracked solid. Journal of Composite Materials 17 (3), 231-237.

Huang, Y., Hu, K.X., Chandra, A., 1994. A generalized self-consistent mechanics method for microcracked solids. Journal of the Mechanics and Physics of Solids 42 (8), 1273-1291.

Huang, Y., Chandra, A., Jiang, Z.Q., 1996. The numerical calculation of two-dimensional effective moduli for microcracked solids. International Journal of Solids and Structures 33 (11), 1575-1586.

Hunt, A.G., 2001. Applications of percolation theory to porous media with distributed local conductances. Advances in Water Resources 24 (3), 279-307.

Jensen, A. Damgaard, Chatterji, S., 1996. State of the art report on microcracking and lifetime of concrete - Part 1. Materials and Structures 29 (1), 3-8.

Kachanov, M., 1992. Effective elastic properties of cracked solids: critical review of some basic concepts. Applied Mechanics Reviews 45 (8), 304-335.

Krajcinovic, D., 1997. Selection of damage parameter - Art or science? Mechanics of Materials 28 (2), 165-179.

Krajcinovic, D., 2000. Damage mechanics: accomplishments, trends and needs. International Journal of Solids and Structures 37 (2), 267-277.

Kushch, V.I., Sevostianov, I., Mishnaevsky, L.J., 2009. Effect of crack orientation statistics on effective stiffness of microcracked solid. International Journal of Solids and Structures 46 (6), 1574-1588.

Kushch, V.I., Shmegera, S.V., Sevostianov, I., 2009. SIF statistics in micro cracked solid: Effect of crack density, orientation and clustering. International Journal of Engineering Science 47 (2), 192-208.

Mehta, P.K., Monteiro, P.J.M., 2006. Concrete: Microstructure, Properties, and Materials, 3rd ed. McGraw-Hill, New York.

Nemat-Nasser, S., Hori, M., 1993. Micromechanics: Overall Properties of Heterogeneous Materials. North-Holland, New York.

Norris, A.N., 1985. A differential scheme for the effective moduli of composites. Mechanics of Materials 4 (1), 1-16.

Ringot, E., Bascoul, A., 2001. About the analysis of microcracking in concrete. Cement and Concrete Composites 23 (2), 261-266.

Shafiro, B., Kachanov, M., 2000. Anisotropic effective conductivity of materials with nonrandomly oriented inclusions of diverse ellipsoidal shapes. Journal of Applied Physics 87 (12), 8561-8569.

Torquato, S., 1991. Random heterogeneous media: microstructure and improved bounds on effective properties. Applied mechanics reviews 44 (2), 37-76.

Xia, W., Thorpe, M.F., 1988. Percolation properties of random ellipses. Physical Review A 38 (5), 2650-2656.

Zheng, Q.-S., Du, D.-X., 2001. An explicit and universally applicable estimate for the effective properties of multiphase composites which accounts for inclusion distribution. Journal of the Mechanics and Physics of Solids 49 (11), 2765-2788.