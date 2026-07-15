![](./images/811028193661157378_1.jpg)

Materials Science and Engineering A219 (1996) 109-125

![](./images/811028193661157378_2.jpg)

# A molecular dynamics study of transformation toughening in the gamma TiAl/beta Ti-V system

M. Grujicic*, P. Dang

Program in Materials Science and Engineering, Department of Mechanical Engineering, 241 Flour Daniel EIB, Clemson University, Clemson, SC 29634-0921, USA

Received 15 December 1995

## Abstract

The materials evolution in a region surrounding the crack tip was carried out using molecular dynamics simulations for the case of a crack in the gamma TiAl phase impinging at the right angle onto the interface between a gamma TiAl phase and a metastable Ti-15V (at.%) phase. The corresponding linear anisotropic continuum solutions for the singular stress and displacement fields were developed using an enriched finite element method. These solutions were used to both generate the initial crack and to prescribe the boundary conditions applied to the computational atomistic crystal during the molecular dynamics simulation runs. The atomic interactions were described in terms of the appropriated embedded atom method (EAM) type interatomic potentials. The crack-tip behavior for the two-phase gamma/beta material was ultimately compared with the one in the corresponding single phase gamma and single phase beta materials. The simulation results showed that under the same applied level of external stress, the crack tip becomes blunted and the crack stops propagating in the gamma TiAl/beta Ti-15V bicrystal and in the single beta-phase crystal while the crack extends by brittle cleavage in the single-phase gamma crystal. The blunting process was found to be controlled by the martensitic transformation which takes place in the beta phase ahead of the crack tip. Depending on the local stress conditions, which are significantly affected by the presence of interfacial dislocations, the crystal structure of martensite was found to be either close packed hexagonal, body centered orthorhombic and/or face centered orthorhombic. Finally, the implications of crack tip martensitic transformation on materials toughness are analyzed in quantitative terms using the concept of the Eshelby's conservation integral, i.e. the energy release rate.

**Keywords**: Embedded atom method; Gamma TiAl phase; Interatomic potentials

## 1. Introduction

It is well established that martensitic transformation taking place in the region around cracks in both metals [1] and ceramics [2] is the reason for record fracture toughness levels achieved in these materials. In our ongoing research we have recently found an almost two-fold increase in room temperature fracture toughness of single-phase gamma titanium aluminide ($K_{\text{IC}} =$ 10.5 MPa m$^{1/2}$) when 10 vol.% of a metastable dispersed Ti-V-Al-Fe base beta phase is added which undergoes a stress/strain induced b.c.c. $\rightarrow$ orthorhombic martensitic transformation ($K_{\text{IC}} = 19.6$ MPa m$^{1/2}$) [3]. Since limited fracture toughness and tensile ductility at temperatures below approximately $600^\circ$C are the major obstacles to a wide scale application of gamma TiAl, the transformation toughening appears to have a potential for helping resolve this problem.

Modeling of materials evolution in a region surrounding the crack tip and the associated mechanism of transformation toughening has been generally carried out using the continuum material approach in which no account of materials microstructure is taken [4]. Since the atomic-scale events are difficult to study experimentally, their effect on the fracture toughness can not be easily measured. Recent advances in the computational materials science coupled with a higher affordability of the more powerful computers has enabled atomistic computer modeling of the crack tip phenomena to become a respectable alternative for elucidating the role of small-scale effects on the fracture process. Among various atomistic modeling techniques, molecular dynamics is particularly attractive since it enables the time

* Corresponding author.

0921-5093/96/$15.00 © 1996 — Elsevier Science S.A. All rights reserved
PII S0921-5093(96)10421-4

evolution of the material around the crack tip, includ- ing the crack-tip phase transformation, to be studied. For example, Hoagland et al. [5,6] used molecular dynamics simulations to analyze dislocation emission from the crack tip, which results in crack-tip blunting and, in turn, enhances materials toughness. Clapp and coworkers [7-10] carried out an extensive molecular dynamics study of the thermally-induced and stress-as- sisted $B 2 \to L 1_{0}$ martensitic transformation in ordered NiAl. Grujicic and Dang [11-13] conducted a molecu- lar dynamics investigation of the martensitic transfor- mation and transformation toughening mechanism in $Fe-(20-40) Ni$ (at.\%) and $Ti-(0-25) V$ (at.\%) alloys.

In each of the molecular dynamics studies mentioned above, the initial atomic configurations, whose time evolution was studied, was a single phase material. The work presented in this paper, on the other hand, deals with the two-phase material, in which one phase, gamma TiAl, contains a crack while the other phase,beta $Ti-V$ , is metastable and can undergo a stress/ strain-induced martensitic transformation. Before molecular dynamics atomistic simulations of the crack tip phenomena in the two phase gamma/beta material described above could be carried out, a linear elastic continuum solution for the corresponding stress and displacement fields had to be developed, so that more realistic boundary conditions can be imposed on the atomistic computational crystal used during simula- tions.

The organization of the paper is as following: the embedded atom method (EAM) inter-atomic potentials used to describe atomic interactions are briefly dis- cussed in Section 2.1. The procedures used to generate and equilibrate the two phase (gamma + beta) atomistic computational bicrystal and to introduce a crack in the gamma phase are described in Section 2.2. A brief account of the molecular dynamics computational method used is given in Section 2.3. In Section 3, the results are presented and discussed. The main conclu- sions resulting from the present work are listed in Section 4.

## 2. Computational procedure

### 2.1. Interatomic potentials

In contrast to the traditional pair potentials, the EAM interatomic potentials take into account, in an implicit way, the many body effects and have therefore been proven more reliable in representing the atomic interactions in metals [14,15]. In the present work, the EAM-type interatomic potentials are used for both the gamma TiAl phase and the beta $Ti-V$ phase. Gamma TiAl has an $L 1_{0}$ type ordered structure and the two atomic species reside on separate sublattices [20].

Farkas (private communication, 1995) recently devel- oped the EAM-type potentials for gamma TiAl and showed that a reasonable agreement can be obtained between the model predictions and the experimentally measured properties of this phase. In the present work the Farkas potentials were used to describe $Ti-Ti$ , $Al-Al$ and $Ti-Al$ interactions within the gamma TiAl phase. The beta $Ti-V$ phase has a disordered body centered cubic (b.c.c.) structure, and to simplify the calculation this phase was treated as a pseu- domonoatomic phase composed of the 'effective' $Ti-V$  atoms rather than the individual $Ti$ and $V$ atoms. The derivation of the EAM potential functions for the pseudomonoatomic beta phase by applying an averag- ing scheme to the corresponding EAM functions of the constituent elements ( $Ti$ and $V$ ) and their validation were discussed in details in our previous work [12]. Based on these EAM potentials, our quasiharmonic calculations $[11,19]$ revealed that the b.c.c. structure is unstable in pure $Ti$ , metastable in $Ti-15$ at. $\% ~V$ and stable in $Ti-25$ at. $\% ~V$ relative to the h.c.p. structure at0 and $100 ~K$ which is consistent with the available thermodynamic data [17]. All the simulations in the present study were done using the $Ti-15 ~V$ b.c.c. beta phase.

There are six distinct pairs whose interactions (the $\phi_{i j}$  terms in Eq. (1)) must be known. As mentioned earlier the pair potentials for the $Ti-Ti, Al-Al$ and $Ti-Al$  pairs along with the corresponding embedding energy functions for the gamma phase have been determined by Farkas (private communication, 1995). The effective Ti-V atom/effective Ti-V atom pair potential as well as the corresponding embedding energy have been derived in our previous work [12]. Hence, there remain two unknown interatomic parameters, the Ti/effective Ti-V atom and the Al/effective Ti-V atom pair poten- tials. The two parameters are designated as $\phi_{i \beta}(i=Ti$ , $Al, \beta=$ the effective $Ti-V$ atom) and were determinedin the present work using the Johnson's approach [18]as following:

$$
\phi_{i \beta}=\frac{1}{2}\left[\frac{f_{\beta}\left(r_{\beta \beta}\right)}{f_{i}\left(r_{i i}\right)} \phi_{i i}\left(r_{i i}\right)+\frac{f_{i}\left(r_{i i}\right)}{f_{\beta}\left(r_{\beta \beta}\right)} \phi_{\beta \beta}\left(r_{\beta \beta}\right)\right] \quad \begin{aligned}
& i=\mathrm{Ti}, \mathrm{Al} \\
& \text { (1) }
\end{aligned}
$$

where $f_{\beta}$ and $\phi_{\beta \beta}$ are respectively the atomic electron density and the pair potential functions of the beta Ti-V phase which are obtained using the aforemen- tioned pseudomonoatomic approximation [14].

### 2.2. Computational crystal

#### 2.2.1. Formation of the computational bicrystal

The computational atomistic gamma/beta bicrystal used in the present work is shown in Fig. 1. In accor- dance with the general findings [34], an orientation relationship in which the highest atomic density planes

![](./images/811028193661157378_3.jpg)

Fig. 1. Computational gamma TiAl/beta Ti-15V bicrystal used in the present work.

and directions of the two phases are parallel to one another was assumed. That is: $x\|[111]_{\gamma}\|[110]_{\beta}$, $y\|[0\overline{1}1]_{\gamma}\|[001]_{\beta}$ and $z\|[2\overline{1}\overline{1}]_{\gamma}\|[\overline{1}10]_{\beta}$.

The interface (habit) plane was assumed to be the closest packed planes in the two structures. This may not be fully justified since, it is well-established that the plane matching can be significantly improved if structural ledges are allowed to form on the high atomic density interface [35]. Since in such a case the resulting macroscopic interface corresponds to a high index plane, atomistic simulations would require a prohibitively large computational crystal and could not be carried out.

The size of the computational bicrystal used in the present work, in terms of the number of the interpla- nar spacings $d_{(u v w)}$ of the $(u v w)$ planes, is as follows: $17d_{(111)}×28d_{(022)}×30d_{(211)}$ for the gamma phase and $18d_{(110)}×25d_{(002)}×22d_{(110)}$ for the beta phase respectively. The bicrystal contains 10654 atoms (2610 Ti, 2610 Al and 5434 equivalent Ti-V atoms). With this size of the computational bicrystal, the two crystals have the following dimensional mismatch in the plane of the interface: $0.49\%$ mismatch in the $y\|[0\overline{1}1]_{\gamma}\|[001]_{\beta}$ direction and a $0.70\%$ mismatch in the $z\|[2\overline{1}\overline{1}]_{\gamma}\|[\overline{1}10]_{\beta}$ direction.

Before creating a crack in the gamma crystal, the structure of the computational bicrystal was minimized using molecular statics under the periodic boundary conditions in the $y$- and $z$-directions and the free surface boundary condition in the $x$-direction. The structure of the gamma/beta interface after the aforementioned energy minimization procedure is shown in Fig. 2. It is seen that the mismatch in the number of the associated planes in the two phases across the gamma/beta interface has been accommodated by the formation of appropriate interfacial dislocations: the first type of interfacial dislocations, type A, have the line direction $l=$ $[2\overline{1}\overline{1}]_{\gamma}\|[\overline{1}10]_{\beta}$ and the Burgers vector $b=1/2[0,\ \bar{a}_{\gamma},$ $c_{\gamma}]_{\gamma}\|a_{\beta}[001]_{\beta}$, Fig. 2(a). There are three A-type dislocations in Fig. 2(a) with the interdislocation spacing of $\sim 9d_{(022)\gamma}$ or $25d_{(002)\beta}$. The other interfacial dislocations, type B, have the line direction $l=$ $[0\overline{1}1]_{\gamma}\|[001]_{\beta}$ and the Burgers vector $b=$ $a_{\gamma}[100]_{\gamma}\|a_{\beta}[010]_{\beta}$, Fig. 2(b). There is only one of these dislocations per periodic length in the $z$-direction, i.e. the interdislocation spacing is $\sim 28d_{(220)\gamma}$ or $25d_{(002)\beta}$. As shown in Fig. 2(c) the A and B interfacial dislocations run respectively parallel to the $z$ and $y$ edges of the computational bicrystal and hence intersect at the right angle.

### 2.2.2. Generation of a crack in the initial computational bicrystal
Before atomistic simulations of the crack-tip martensitic transformation and the resulting toughness enhancement can be carried out, a continuum solution to the problem of a crack which is located in the gamma phase and whose tip is touching the gamma/beta interface and which is subject to a uniaxial Mode I external loading, Fig. 3, had to be obtained. In particular the singular stresses and the corresponding displacements which dominate the near crack-tip continuum stress and displacement fields have to be derived. These fields are used to both generate a crack in the computational bicrystal and apply the appropriate boundary conditions to it.

The external Mode I loading gives rise, in the case of a crack touching the gamma/beta interface, to a singular stress field composed of two terms (named A and B for convenience) with distinct orders of stress singularity $\lambda_{\mathrm{A}}$ and $\lambda_{\mathrm{B}}$, as following:

![](./images/811028193661157378_4.jpg)

Fig. 2. Equilibrium structure of the gamma TiAl/beta Ti-15V interface: (a) atomic positions projected onto the $(2\overline{1}\overline{1})_{\gamma}\parallel(\overline{1}10)_{\beta}$ planes, (b) atomic positions projected onto the $(0\overline{1}1)_{\gamma}\parallel(001)_{\beta}$ planes and (c) interface structure by projections of two $(110)_{\gamma}$ and two $(111)_{\beta}$ planes beside the interface.

$$
\sigma_{i j}(r, \theta)=\frac{K_{\mathrm{A}}}{r^{1-\lambda_{\mathrm{A}}}} h_{\mathrm{A} i j}(\theta)+\frac{K_{\mathrm{B}}}{r^{1-\lambda_{\mathrm{B}}}} h_{\mathrm{B} i j}(\theta), \quad i, j=r, \theta
\tag{2}
$$

Where $K_{\mathrm{A}}$ and $K_{\mathrm{B}}$ represent the generalized stress intensity factors, $h_{\mathrm{A} i j}(\theta)$ and $h_{\mathrm{B} i j}(\theta)$ the corresponding angular dependences of the stresses, and $\theta$ is the polar angle. Eq. (2) indicates that the stress field is singular at the crack tip $(r=0)$ when $\lambda_{\mathrm{A}}$ and $\lambda_{\mathrm{B}}$ are less than 1. In addition, to satisfy the condition for finiteness of the strain energy, admissible values of $\lambda$ should satisfy the condition $\lambda>0$. Therefore, the admissible orders of stress singularity fall in the range $0<\lambda<1$.

The corresponding (plane strain) displacement field also contains two terms, each associated with the corresponding stress term in Eq. (2) as following:

$$
\begin{aligned}
&u_{i}(r, \theta)=K_{\mathrm{A}} r^{\lambda_{\mathrm{A}}} f_{\mathrm{A} i}(\theta)+K_{\mathrm{B}} r^{\lambda_{\mathrm{B}}} f_{\mathrm{B} i}(\theta), \quad \mathrm{i}=r, \theta \\
&u_{z}(r, \theta)=0
\tag{3}
\end{aligned}
$$

where $f_{i}(\theta)$ are the angular displacement functions which are related to the corresponding angular stress functions.

The analytical form for the stress and displacement field functions. Eqs. (2) and (3) for the two anisotropic materials, as in the present case, is not available and these functions have to be determined numerically. In the present work the functions are determined using a two-step procedure: first a finite element method introduced by Yamada and Okumura [22] is used to determine the orders of the stress singularity and the angular variations of the stress and displacement fields. Next,

![](./images/811028193661157378_5.jpg)

Fig. 3. (a) Computational bicrystal with a crack in the gamma phase touching the gamma/beta interface and (b) the relationship between the computational bicrystal and the typical gamma/beta two phase microstructure observed in reference [3].

an enriched finite element formulation is used to deter- mine the generalized stress intensity factors.

Fig. 4 shows a crack touching the interface in a bi-material crystal where the stress singularity occurs at the crack tip O. In order to determine the orders of the stress singularity, $\lambda$, and the corresponding angular variation of the stress and displacement fields, the region surrounding the crack tip is divided into a number of quadratic sector elements, where the loca- tion of each element is defined in polar coordinates by its nodes 1-3. The location of a point $P$ in the element can then be defined using the following singular trans- formation of Yamada et al. [23]:

$$
\begin{gathered}
r=r_{0}\left(\frac{1+\xi}{2}\right)^{1 / \lambda} \quad \text { or } \quad \varrho=\frac{r}{r_{0}}=\left(\frac{1+\xi}{2}\right)^{1 / \lambda} \quad \text { and } \\
\theta=\sum_{i=1}^{3} H_{i} \theta_{i}
\end{gathered}
\tag{4}
$$

where

$$
H_{1}=\frac{1}{2}\left(-\eta+\eta^{2}\right), \quad H_{2}=1-\eta^{2}, \quad H_{3}=\frac{1}{2}\left(\eta+\eta^{2}\right).
\tag{5}
$$

and $\eta$ and $\xi$ are the natural coordinates of the elements as defined in Fig. 4.

In accordance with Eq. (3), the displacement field in the element relative to the inplane displacement of the crack tip $\bar{u}$, due to inplane loads is assumed to have the following form:

$$
\bar{u}=\varrho^{\lambda} \sum_{i=1}^{3}\left[H_{i}\right]\left\{\bar{u}_{i}\right\}=\varrho^{\lambda}[H]\{\bar{u}\}
\tag{6}
$$

where

$$
\left[H_{i}\right]=\left[\begin{array}{cc}
H_{i} & 0 \\
0 & H_{i}
\end{array}\right]
$$

$$
\left\{\bar{u}_{i}\right\}^{\mathrm{T}}=\left\{\bar{u}_{r i} \bar{u}_{\theta i}\right\}
$$

the inplane displacement vector of the node $i$ ($i$
$=1,2,3$)

$$
[H]=\left[\begin{array}{cccccc}
H_{1} & 0 & H_{2} & 0 & H_{3} & 0 \\
0 & H_{1} & 0 & H_{2} & 0 & H_{3}
\end{array}\right]
$$

and

$$
\{\bar{u}\}^{\mathrm{T}}=\left\{\bar{u}_{r 1} \bar{u}_{\theta 1} \bar{u}_{r 2} \bar{u}_{\theta 2} \bar{u}_{r 3} \bar{u}_{\theta 3}\right\}
$$

The strains are next obtained from the proper differ- entiation of the displacements which through the use of Eqs. (4)-(6) result in:

$$
\varepsilon=\left\{\begin{array}{c}
\varepsilon_{r} \\
\varepsilon_{\theta} \\
\gamma_{r \theta}
\end{array}\right\}=\sum_{i=1}^{3}\left[B_{i}\right]\left\{\bar{u}_{i}\right\}=[B]\{\bar{u}\}
\tag{7}
$$

where

$$
[B]=\frac{1}{r_{0}} \varrho^{\lambda-1}\left(\lambda\left[B_{\mathrm{a}}\right]+\left[B_{\mathrm{b}}\right]\right)
$$

$$
\left[B_{i \mathrm{a}}\right]=\left[\begin{array}{cc}
H_{i} & 0 \\
0 & 0 \\
0 & H_{i}
\end{array}\right]
$$

![](./images/811028193661157378_6.jpg)

Fig. 4. Definition of the element geometry and the natural coordinates in a typical structure where a singular stress state occurs.

$$
\left[B_{i \mathrm{~b}}\right]=\left[\begin{array}{cc}
0 & 0 \\
H_{i} & \frac{2}{\theta_{\mathrm{s}}} \frac{\partial H_{i}}{\partial \eta} \\
\frac{2}{\theta_{\mathrm{s}}} \frac{\partial H_{i}}{\partial \eta} & -H_{i}
\end{array}\right], \quad i=1,2,3
\tag{8}
$$

During the derivation of $[B_{ib}]$ in Eq. (8) it was assumed that $\theta_{2}=(\theta_{1}+\theta_{3})/2$ and $\theta_{\mathrm{s}}=\theta_{3}-\theta_{1}$, and hence $\partial \eta / \partial \theta=2 / \theta_{\mathrm{s}}$.

For each of the sector elements depicted in Fig. 4 to be in equilibrium, it must satisfy the principle of virtual work, which for the plane strain case can be expressed as:

$$
\begin{aligned}
& \int_{0}^{r_{0}} \int_{\theta_{1}}^{\theta_{3}}\left(\sigma_{r} \delta \varepsilon_{r}+\sigma_{\theta} \delta \varepsilon_{\theta}+\tau_{r \theta} \delta \gamma_{r \theta}\right) t r \mathrm{~d} r \mathrm{~d} \theta \\
& =r_{0} \int_{\theta_{1}}^{\theta_{3}}\left(T_{r} \delta \bar{u}_{r 0}+T_{r \theta} \delta \bar{u}_{\theta 0}\right) t \mathrm{~d} \theta
\end{aligned}
\tag{9}
$$

where $\delta u$'s and $\delta \varepsilon$'s are the virtual displacements and the corresponding virtual strains, $T_{r}$ and $T_{r \theta}$ represent respectively the applied normal and shear stresses at the outer boundary of the element, $\bar{u}_{r 0}$ and $\bar{u}_{\theta 0}$ the surface displacements at $r=r_{0}$, and $t$ is the element thickness. It should be noted here that the tractions on the edges O1 and O3 of the element in Fig. 4 are not included in Eq. (9) since these edges are either the internal edges in the material or they are stress free crack faces.

By carrying out the $(r, \theta \rightarrow \varrho, \eta)$ variables substitution through the use of Eqs. (3)-(8), and by taking into account that $T_{r}=\sigma_{r 0}=\sigma_{r}(r=r_{0})$, $T_{r \theta}=\tau_{r \theta 0}=\tau_{r \theta}(r=r_{0})$ and assuming the materials constitutive relation $\{\sigma\}=[D]\{\varepsilon\}$, Eq. (9) after integration of its left hand side with respect to $\varrho$ becomes:

$$
\begin{aligned}
& \frac{\theta_{\mathrm{s}} t}{4 \lambda} \delta\{\bar{u}\}^{\mathrm{T}} \int_{-1}^{1}\left(\lambda\left[B_{\mathrm{a}}\right]^{\mathrm{T}}+\left[B_{\mathrm{b}}\right]^{\mathrm{T}}\right)[D]\left(\lambda\left[B_{\mathrm{a}}\right]+\left[B_{\mathrm{b}}\right]\right) \mathrm{d} \eta\{\bar{u}\} \\
& =\frac{t \theta_{\mathrm{s}}}{2} \delta\{\bar{u}\}^{\mathrm{T}} \int_{-1}^{1}[H][d]\left(\lambda\left[B_{\mathrm{a}}\right]+\left[B_{\mathrm{b}}\right]\right) \mathrm{d} \eta\{\bar{u}\}
\end{aligned}
\tag{10}
$$

The plane strain material stiffness matrix is given as

$$
[D]=\left[\begin{array}{lll}
D_{11} & D_{12} & D_{16} \\
D_{12} & D_{22} & D_{26} \\
D_{16} & D_{26} & D_{66}
\end{array}\right] \quad \text { and }
$$

$$
[d]=\left[\begin{array}{lll}
D_{11} & D_{12} & D_{16} \\
D_{16} & D_{26} & D_{66}
\end{array}\right]
$$

is comprised of the first row and the last row of the matrix $[D]$.

Eq. (10) must hold for any arbitrary variation in the nodal displacements $\delta\{u\}$, and hence the $\delta\{u\}^{\mathrm{T}}$ term can be eliminated from this equation which when written for the entire computational domain $S$ (i.e. for all the elements) becomes:

$$
\left(\lambda^{2}[A]+\lambda[B]+[C]\right)\{\bar{U}\}=0
\tag{11}
$$

where

$$
[A]=\sum_{S}\left(\left[k_{\mathrm{a}}\right]-\left[k_{\mathrm{sa}}\right]\right)
\tag{12}
$$

$$
[B]=\sum_{S}\left(\left[k_{\mathrm{b}}\right]-\left[k_{\mathrm{sb}}\right]\right)
\tag{13}
$$

$$
[C]=\sum_{S}\left[k_{\mathrm{c}}\right]
\tag{14}
$$

$$
\{\bar{U}\}=\sum_{S}\{\bar{u}\}
\tag{15}
$$

$$
\left[k_{\mathrm{a}}\right]=\int_{-1}^{1}\left[B_{\mathrm{a}}\right]^{\mathrm{T}}[D]\left[B_{\mathrm{a}}\right] \mathrm{d} \eta
\tag{16}
$$

$$
\left[k_{\mathrm{c}}\right]=\int_{-1}^{1}\left[B_{\mathrm{b}}\right]^{\mathrm{T}}[D]\left[B_{\mathrm{b}}\right] \mathrm{d} \eta
\tag{17}
$$

$$
\left[k_{\mathrm{b}}\right]=\int_{-1}^{1}\left(\left[B_{\mathrm{a}}\right]^{\mathrm{T}}[D]\left[B_{\mathrm{b}}\right]+\left[B_{\mathrm{b}}\right]^{\mathrm{T}}[D]\left[B_{\mathrm{a}}\right]\right) \mathrm{d} \eta
\tag{18}
$$

$$
\left[k_{\mathrm{sa}}\right]=2 \int_{-1}^{1}[H]^{\mathrm{T}}[d]\left[B_{\mathrm{a}}\right] \mathrm{d} \eta
\tag{19}
$$

and

$$
\left[k_{\mathrm{sb}}\right]=2 \int_{-1}^{1}[H]^{\mathrm{T}}[d]\left[B_{\mathrm{b}}\right] \mathrm{d} \eta
\tag{20}
$$

Summation over $S$ in Eqs. (12)-(15) implies assembly of the elements into the global model. For instance $\{\bar{U}\}=\left\{\bar{u}_{r 1} \bar{u}_{\theta 1} \cdots \bar{u}_{r, 2 n+1} \bar{u}_{\theta, 2 n+1}\right\}$, where $n$ is number of sector elements and hence $2 n+1$ is the number of nodes.

Because the matrix $[C]$ is singular, the characteristic Eq. (11) can be transformed uniquely into the standard eigenvalue problem. By solving Eq. (21), the admissible values for the order of stress singularity are obtained as the eigenvalues $\lambda$ which satisfy the condition $0<\lambda<1$ and the corresponding nodal displacements $\{U\}$ are obtained from the eigenvectors $\left\{\begin{array}{l}\bar{V} \\ \bar{U}\end{array}\right\}$ associated with each admissible value of $\lambda$.

$$
[S]\left\{\begin{array}{l}
\bar{V} \\
\bar{U}
\end{array}\right\}=\lambda\left\{\begin{array}{l}
\bar{V} \\
\bar{U}
\end{array}\right\}
\tag{21}
$$

where
$$
[S]=\left[\begin{array}{cc}
0 & \mathrm{I} \\
-A^{-1} C & -A^{-1} B
\end{array}\right], \quad\{\bar{U}\}=\lambda\{\bar{V}\}
$$

and
$$
\begin{aligned}
& \left\{\begin{array}{l}
\bar{V} \\
\bar{U}
\end{array}\right\}^{\mathrm{T}} \\
& =\left\{\bar{v}_{r 1}, \bar{v}_{\theta 1}, \ldots, \bar{v}_{r, 2 n+1}, \bar{v}_{\theta, 2 n+1}, \bar{u}_{r 1}, \bar{u}_{\theta 1}, \ldots, \bar{u}_{r, 2 n+}\right. \\
& \left.1, \bar{u}_{\theta, 2 n+1}\right\}
\end{aligned}
$$

In its principal coordinate system of materials orthotropy, the gamma phase which has a face centered tetragonal structure has six nonzero independent elastic constants. $C_{11}=2.28, \quad C_{12}=1.02, \quad C_{13}=1.36, \quad C_{33}=$ $2.78, C_{44}=1.4$ and $C_{66}=0.776$ (all in $10^{11} \mathrm{~N} \mathrm{~m}^{-2}$ ) [3]. The beta phase has a body centered cubic structure and thus only three independent elastic constants: $C_{11}=$ $1.121, C_{12}=0.771$ and $C_{44}=0.885\left(10^{11} \mathrm{~N} \mathrm{~m}^{-2}\right)$ [3]. Using these values of the elastic constants, the materials stiffness matrix $[D]$ was first computed and then the eigenvalue problem, Eq. (21) was solved to yield two admissible values of $\lambda(0.4788$ and 0.4113$)$ in the range $0<\lambda<1$. Fig. 5(a) and (b) show the corresponding angular variation of the tangential and the radial displacements constructed using the appropriate elements of the two eigenvectors. It should be noted that for the pure Mode I case, the radial displacement is an even function of $\theta$ and the tangential displacement is an odd function of $\theta$. Similarly, for the pure Mode II case the tangential displacement is an even function of $\theta$ and the radial displacement is an odd function of $\theta$. Fig. 5(a) and (b) suggest that the two displacement fields are neither pure Mode I nor pure Mode II. However, the displacement field associated with $\lambda=0.4788$, named Mode A, is more 'Mode I-like' while the displacement field associated with $\lambda=0.4113$, named Mode B, is more 'Mode II-like'. The angular dependences of the inplane stresses $\sigma_{r r}, \sigma_{r \theta}$ and $\sigma_{\theta \theta}$ for the two modes can be determined using Eq. (7) and the materials constitutive relation $\{\sigma\}=[D]\{\varepsilon\}$ and the results are not shown for brevity.

To complete the evaluation of the near crack-tip stress and displacement fields, Eqs. (2) and (3), the generalized stress intensity factor $K_{\mathrm{A}}$ and $K_{\mathrm{B}}$ must be determined. This was done in the present work using the enriched-finite element formation proposed by Ben- zley [24]. Within this formulation the displacements $u$ and $v$ within the enriched elements, in terms of the nodal displacements are given by:

$$
\begin{aligned}
u(\xi, \phi)= & \sum_{i=1}^{m} N_{i}(\xi, \phi) u_{i} \\
& +K_{\mathrm{A}} Z(\xi, \phi)\left[F_{\mathrm{A} u}(\xi, \phi)-\sum_{j=1}^{m} N_{j}(\xi, \phi) F_{\mathrm{A} u j}\right] \\
& +K_{\mathrm{B}} Z(\xi, \phi)\left[F_{\mathrm{B} u}(\xi, \phi)-\sum_{j=1}^{m} N_{j}(\xi, \phi) F_{\mathrm{B} u j}\right]
\end{aligned}
$$

$$
\begin{aligned}
v(\xi, \phi)= & \sum_{i=1}^{m} N_{i}(\xi, \phi) v_{i} \\
& +K_{\mathrm{A}} Z(\xi, \phi)\left[F_{\mathrm{A} v}(\xi, \phi)-\sum_{j=1}^{m} N_{j}(\xi, \phi) F_{\mathrm{A} v j}\right] \\
& +K_{\mathrm{B}} Z(\xi, \phi)\left[F_{\mathrm{B} v}(\xi, \phi)-\sum_{j=1}^{m} N_{j}(\xi, \phi) F_{\mathrm{B} v j}\right]
\end{aligned}
$$

where $N_{i}$ are the usual interpolation (shape) functions expressed in terms of the natural element coordinates $\xi$ and $\phi$, and the summation is taken over all $m$ nodes of a given element. For isoparametric quadratic quadrilateral elements used in the present case $m=8$. A 'zeroing' function $Z(\xi, \phi)$ is added in Eqs. (22) and (23) to obtain the required compatibility between the enriched elements surrounding the crack tip and the regular elements surrounding the enriched elements. This function is equal to unity for the enriched elements, and zero for the regular elements. The enriched/regular interelement compatibility was achieved by separating them with a layer of 'transition' elements in which the zeroing function $Z(\xi, \phi)$ varies between one and zero. Any zeroing function used must be unity along the boundaries of the transition element which are in con-

![](./images/811028193661157378_7.jpg)

Fig. 5. Displacement fields for the gamma TiAl/beta Ti-V case: (a) Mode A, angular dependence of displacement normalized with respect to $h_{00}$ $(\theta=0)$, (b) Mode b, angular dependence of displacement normalized with respect to $h_{r 0}(\theta=0)$.

tact with the enriched elements and be zero on the element edges which are in contact with the regular elements. The specific choice of $Z(\xi, \phi)$ for a given transition element depends on whether an entire edge or a single corner node of the transition element is in contact with the enriched elements surrounding the crack tip. In the present work the following form of $Z(\xi, \phi)$ was used [7,8]:

$$
\begin{aligned}
& Z(\xi, \phi) \\
& = \begin{cases}\frac{1}{4}(1 \pm \xi)(1 \pm \phi) & \text { : zeroing from corner node } \\
\frac{1}{2}(1 \pm \xi) & \text { : zeroing from element edge } \\
\frac{1}{2}(1 \pm \phi) & \text { : zeroing from element edge }\end{cases}
\end{aligned}
$$

Functions $F_{\mathrm{A} u}, F_{\mathrm{A} v}, F_{\mathrm{B} u}$ and $F_{\mathrm{B} v}$ in Eqs. (22) and (23) are the coefficients of the stress intensity factors $K_{\mathrm{A}}$ and $K_{\mathrm{B}}$ in the expressions for the singular displacement field, Eq. (3), i.e.:

$$
\begin{aligned}
& F_{\mathrm{A} u}(r, \theta)=r^{\lambda_{\mathrm{A}}}\left[f_{\mathrm{A} r}(\theta) \cos (\theta)-f_{\mathrm{A} \theta}(\theta) \sin (\theta)\right] \\
& F_{\mathrm{B} u}(r, \theta)=r^{\lambda_{\mathrm{B}}}\left[f_{\mathrm{B} r}(\theta) \cos (\theta)-f_{\mathrm{B} \theta}(\theta) \sin (\theta)\right] \\
& F_{\mathrm{A} v}(r, \theta)=r^{\lambda_{\mathrm{A}}}\left[f_{\mathrm{A} r}(\theta) \sin (\theta)+f_{\mathrm{A} \theta}(\theta) \cos (\theta)\right] \\
& F_{\mathrm{B} v}(r, \theta)=r^{\lambda_{\mathrm{B}}}\left[f_{\mathrm{B} r}(\theta) \sin (\theta)+f_{\mathrm{B} \theta}(\theta) \cos (\theta)\right]
\end{aligned}
$$

$F_{\mathrm{A} u j}, F_{\mathrm{A} v j}, F_{\mathrm{B} u j}$ and $F_{\mathrm{B} v j}$ appearing in Eqs. (22) and (23) are the asymptotic displacement functions given in Eq. (25) evaluated at the $j$ th node. To obtain the functions given in Eq. (25) in terms of the natural coordinates, $(\xi, \phi)$, the polar coordinates $(r, \theta)$ are first transferred into the Cartesian coordinates $(x, y)$ and these are, in turn, transferred into the natural coordinates using the shape functions $N_{i}$ and nodal coordinates $\left(x_{i}, y_{i}, i=\right.$ $1, \cdots, m, m=$ number of nodes).

A careful examination of Eqs. (22) and (23) reveals that in order to determine the displacement field around

the crack tip, one must evaluate $2m$ nodal displacements $(x_i, y_i, i=1,\cdots,m)$, and two generalized stress intensity factors $K_{\text{A}}$ and $K_{\text{B}}$. This was done in the present work by using the standard virtual work approach [36] to determine the elements stiffness matrix [25-27]. The stiffness matrix was found to have the following form:

$$
[k] = \begin{bmatrix}
\underset{(2m \times 2m)}{[k^{11}]} & \vdots & \underset{(2m \times 2)}{[k^{12}]} \\
\cdots & \vdots & \cdots \\
\underset{(2 \times 2m)}{[k^{21}]} & \vdots & \underset{(2 \times 2)}{[k^{22}]}
\end{bmatrix}
\tag{26}
$$

where matrix $[k^{11}]$ is identical to the stiffness matrix for the regular quadratic quadrilateral element, $[k^{12}] = [k^{21}]^{\text{T}}$ contains the contribution of both the regular and the enriched parts of Eqs. (22) and (23), and $[k^{22}]$ contains only the contribution of the enriched parts of Eqs. (22) and (23). Each element of the matrix $[k]$ is a double integral with respect to the natural coordinates and is evaluated using the Gaussian Quadrature method. The element stiffness matrices are next entered into the USER ELEMENT subroutine of the general purpose finite element code ABAQUS [28]. The element assembly to form the global stiffness matrix and the solution to the boundary value problem at hand are then solved using ABAQUS to get the nodal displacements and the two generalized stress intensity factors, $K_{\text{A}}$ and $K_{\text{B}}$.

The following boundary value problem was solved to evaluate $K_{\text{A}}$ and $K_{\text{B}}$. A periodic square arrangement of 10 vol.% of square-shaped beta phase particles is introduced into the gamma TiAl matrix. Cracks parallel to the $x$-axis and running from one beta phase particle to another are next generated in the gamma phase matrix and the structure located under constant remote displacement conditions in $y$-direction and a zero displacement condition in $z$-direction. The computed average values of $K_{\text{A}}$ and $K_{\text{B}}$ are respectively $1.83$ MPa $\mu\text{m}^{0.47885}$ and $0.18$ MPa $\mu\text{m}^{0.41138}$. This result reveals a significant coupling between the two singular stress terms in Eq. (2), i.e. even though only a Mode I loading was applied, both the Mode I-like Mode A and the Mode II-like Mode B stress and displacement fields are activated.

The computed $K_{\text{A}}$ and $K_{\text{B}}$ values, the stress singularity and the angular dependence data shown in Fig. 5 are all used in Eqs. (2) and (3) to prescribe the appropriate boundary conditions on the border atoms of the atomistic bicrystal and thus account for the effect of the (exterior) continuum bicrystal on the (interior) atomistic bicrystal. In the present case, the following boundary conditions were used: (a) to achieve the plane strain condition, the fixed periodic boundary conditions were used in the $z$-direction, the crack front direction; (b) to prevent the gamma/beta interfacial dislocations from escaping to the free surface by gliding along the interface the fixed displacement boundary conditions were applied on the three atomic layers of the gamma phase in $x$- and $y$-directions. The magnitude of the (fixed) displacements at a given level of (generalized) stress intensity factors has been determined using Eq. (3); (c) the fixed displacement boundary conditions can not be used in the case of the beta phase since such conditions were found to interfere with the b.c.c. $\rightarrow$ h.c.p. martensitic transformation in this phase be preventing the $(110)_{\beta}[\overline{1}10]_{\beta}$ transformation shuffling from taking place. Instead, fixed stress boundary conditions, obtained using Eq. (2), were prescribed on the three outermost atomic layers of the beta phase. Consequently, as shown in Fig. 3(a), three distinct atomic regions can be identified in the beta phase. In Region I, no external stresses (forces) are applied to the atoms which are allowed to move freely in response to the atomic interaction forces during the molecular dynamics simulation runs. In Region II, the atoms are subject to the fixed stress boundary conditions but are otherwise free to move. The role of Region III is to provide the atoms which act as neighbors to the atoms in the Region II, and thus ensure a bulk-like environment as opposed to a free surface coordination for the atoms in Region II.

### 2.3. Computational method

The evolution of the material in the region around the crack tip is studied by carrying out the standard molecular dynamics calculations in the computational bicrystal described above. Within the molecular dynamics scheme, the classical equations of motion for the atom are solved to determine the atomic positions and velocities in the computational bicrystal as a function of time [29]. The method is therefore suitable for studying time-dependent phenomena such as phase transformations, crack and dislocation propagations, etc. Based on our previous work [12], a temperature of 100 K was selected for all the atomistic simulation carried out in the present work. This temperature provides a good compromise between achieving the required level of thermodynamic temperature stability of the beta phase (necessary to ensure the occurrence of martensitic transformation during loading) and the minimization of thermal atomic vibrations (desirable to facilitate the identification of various crystal structures which may form during loading). To obtain this temperature, initially each atom was assigned a random velocity from the corresponding Boltzmann distribution. To maintain the simulation temperature at 100 K, exponential relaxation of the average squared velocity with a time constant of 0.1 ps was applied at each time step (2 fs). This

![](./images/811028193661157378_8.jpg)

Fig. 6. Evolutions of the atomic positions in the gamma TiAl/beta Ti-15V bicrystal with a crack projected on the $(2\overline{1}\overline{1})_{\gamma}\parallel(\overline{1}10)_{\beta}$ planes as a function of the simulation time.

allowed the temperature to be maintained within $\pm 2\%$ of the desired temperature.

## 3. Results and discussion

The initial atomic configuration in the bicrystal with a crack in the gamma phase, subject to an average remote stress level of 180 MPa, was created by displacing the atoms in accordance with Eq. (3) and is shown in Fig. 6(a). It should be noted that due to the introduction of the crack into the computational bicrystal one of the $\boldsymbol{b}=1/2[0,\bar{a}_{\gamma},c_{\gamma}]_{\gamma}\parallel a_{\beta}[001]_{\beta}$ interfacial dislocations coincides with the crack tip with its extra-half plane being one of crack surfaces.

The progress of the materials evolution at the crack tip as a function of simulation time is shown in Fig. 6. After approximately 1 ps of the simulation time, Fig. 4(b), the two crack faces in the near vicinity of the crack tip are seen to have moved a little bit outward. This movement is clearly related with the observed sliding of the $\boldsymbol{b}=1/2[0,\bar{a}_{\gamma},c_{\gamma}]_{\gamma}\parallel a_{\beta}[001]_{\beta}$ interfacial dislocations along the gamma/beta interface and away from the crack tip as well as with the relaxation of the atoms at the crack surfaces. As a result of these crack-tip processes, an additional extra $(0\overline{1}1)_{\gamma}$ plane has been created making the total of four $\boldsymbol{b}=1/2[0,\bar{a}_{\gamma},c_{\gamma}]_{\gamma}$ interfacial dislocations. The atomic configuration shown in Fig. 4(c) suggests, as was expected, that with the exception of some minor atomic rearrangement, there are no

phase transformations in the gamma phase. In sharp contrast, the beta-phase region ahead of the crack tip has undergone significant changes in its structure at this stage. The region in the beta phase corresponding to approximately $-40^{\circ} \leqslant \theta \leqslant 40^{\circ}$ ($\theta$ is the polar angle), has transformed into a base centered orthorhombic structure with a two atom basis. In the regions of the beta phase corresponding to $-180^{\circ} \leqslant \theta \leqslant-40^{\circ}$ and $40^{\circ} \leqslant \theta \leqslant 180^{\circ}$, on the other hand, a face-centered or thorhombic (f.c.o.) structure is observed.

These findings are consistent with the common exper- imental observations [30], which show that, while sev- eral different structures of martensites exist in the transformed beta phase, only two, a hexagonal close packed (h.c.p.) $\alpha'$ structure and a face-centered or thorhombic (f.c.o.) $\alpha^{\prime \prime}$ structure exist in the bulk mate rial. The $\alpha'$ martensite is most prevalent in pure or low-alloyed Ti. The $\alpha^{\prime \prime}$ martensite, on the other hand, is commonly observed in the Ti-base alloys containing a higher level of beta stabilizing elements (such as V, Nb, Ta, etc.) and as a result of the stress/strain-induced martensitic transformation [30]. According to Burgers [31], the b.c.c. $\to$ h.c.p. mertensitic phase transformation can be described in terms of the following two elemen- tal processes: (a) shuffling of the parallel adjacent $(110)_{bcc}$ planes in the opposite $[1 \overline{1} 0]_{bcc}$ directions by an amount of $1 / 6 d(110)_{bcc}$ , where $d$ refers to the corre sponding interplanar spacing and (b) a pure shear on the $\{112\}_{bcc}$ planes in the $\langle 11 \overline{1}\rangle_{bcc}$ directions. The shuffling displacements produce the characteristic h.c.p.-type ABAB stacking of the close packed $(0001)_{hcp}$ planes. The transformation shear, on the other hand, converts the irregular hexagonal atomic arrangement in the $(110)_{bcc}$ planes with the characteristic angle $\theta=$ 109.47° into the regular hexagonal atomic arrangement $(\theta=120^{\circ})$ in a close-packed $(0001)_{hcp}$ plane. The b.c.o. structure observed in the present work, Fig. 8(b) and (c), has been produced by the operation of the sametwo elemental processes, i.e. by the $\{110\}_{\beta}\langle 1 \overline{1} 0\rangle_{\beta}$  shuffling and by the $\{112\}_{\beta}\langle 11 \overline{1}\rangle_{\beta}$ shear, but the mag nitude of the shuffling displacements and transforma- tion shear are smaller than their counterparts in the case of the b.c.c. $\to$ h.c.p. transformation. In fact, the h.c.p. structure can be considered as a b.c.o. structure in which the additional relations exist between the lattice parameters: $a_{hcp}=\sqrt{3} b_{hcp}=\sqrt{3 / 8} c_{hcp}$ .

In order to conduct a more detailed analysis of the martensitic transformation in the beta-phase portion of the computational bicrystal, three atomic configura- tions, corresponding to the one in Fig. 6(c), but each at a different value of the $z$ -coordinate are shown in Fig.7. In each case only the projections of the atoms in alloy residing on three adjacent parallel $(\overline{1} 10)_{\beta}$ planes are shown. A number of important findings can be made based on the results shown in Fig. 7: (a) transfor-mation shuffling is seen to take place in the $[110]_{\beta}$  direction at some values of the $z$ coordinate in the beta crystal and in the $[\overline{1} \overline{1} 0]_{\beta}$ direction at the others (com pare configurations $X$ and $Y$ at $z=0-2 d_{(110) \beta}$ and z= 10-12d(110)). In addition, the direction of the transformation shear varies with the $z$ coordinates. This finding appears to be related to the use of the fixed periodic boundary conditions in $z$ direction, and is the manifestation of the self-accommodation of the shape change accompanying the transformation; (b) the f.c.o. martensite phase undergoes a slip deformation due to the passage of the edge dislocations with the line direc-tion $l=\langle 11 \overline{2}\rangle_{fco }$ , the Burges vector $b=a_{fco } / 2\langle\overline{1} 10\rangle_{fco }$ and the $\{111\}_{fco }$ slip plane, Fig. 7(c). Different $\{111\}_{fco }$  planes act as slip planes along the $z$ direction of the crystal, which is again an indication of the self-accom- modation of the b.c.c. $\to$ f.c.o. transformation shape change. The emission of the $b=a_{fco} / 2\langle\overline{1}_{fco}$ dislocations from the gamma/beta interface near the crack tip acts as a lattice invariant deformation mechanism which is an integral part of the b.c.c. $\to$ f.c.o. martensitic trans formation; and (c) the orientation relationships between the parent beta structure and two martensitic structureswere determined as following:

$$(\overline{1} 10)_{\mathrm{bcc}}\|(001)_{\mathrm{fco}}\|(001)_{\mathrm{bco}}$$

$$[111]_{\mathrm{bcc}}\|[\overline{1} 10]_{\mathrm{fco}}\|[\overline{1} 10])_{\mathrm{bco}}$$

which is in excellent agreement with the selected area electron diffraction data in $Ti-10 ~V-3 Al-2 Fe$ beta alloy [21,32].

In order to further clarify the effect of the beta phase on the materials evolution at crack tip and on the crack behavior, the molecular dynamics analysis has been extended to include also the cases of a single phase gamma crystal and a single phase beta crystal each containing a crack. The orientation of the computa- tional crystal as well as of the crack in these single- phase material simulations were selected in such a way that they match their corresponding counterparts given in Fig. 1. The generation of a crack in the single phase material is quite straightforward and is done by displac- ing the atoms from their perfect-crystal positions using the plane-strain linear (anisotropic) elastic solution for the Mode I displacement functions corresponding to a given level of stress intensity factor $K_{I}[5,6,13]$ . To compare the crack behavior in single phase and two- phase crystals, the enriched-finite element formulation discussed earlier was used to determine the Mode I stress intensity factors in the two single phase materialsunder the same remotely applied average stress of 180MPa. The following results were obtained: $K_{I}=1.06$  $MPa m^{1 / 2}=1.39 K_{Gr}$ in single phase gamma and $K_{I}=$  $0.81 MPa m^{1 / 2}$ in the single phase beta, where $K_{Gr}$ is the Griffith stress intensity factor. The procedure for com- puting $K_{Gr}$ in atomistic crystals is described elsewhere[13]. These values of the stress intensity factors were

![](./images/811028193661157378_9.jpg)

Fig. 7. Atomic positions in the beta phase projected on the $(\overline{1}10)_{\beta}$ planes at 10 ps of molecular dynamics simulation time: (a) $z=0-2d_{(110)\beta}$, (b) $z=10-12d_{(110)\beta}$ and (c) $z=12-14d_{(110)\beta}$. Schematic representations of the transformed b.c.o. structure and f.c.o. structure along with its slip system were also given in (b) and (c).

next used to displace the atoms from their positions in the perfect crystals and thus create a crack in the two single phase computational atomistic crystals.

The molecular dynamics simulation results for the single phase gamma crystal containing a crack subject to the same type of boundary conditions as the one applied to the gamma part of the computational bicrystal in Fig. 3, i.e. the fixed displacement boundary condition in the $x$ and $y$ directions and the fixed periodic boundary conditions in the $z$ direction, as shown in Fig. 8. The crack is seen to initially propagate along the original $(0\overline{1}1)_{\gamma}$ crack plane. However, at a later stage of crack propagation, the crack leaves its original crack plane temporarily and begins to advance along the $(2\overline{5}1)_{\gamma}$ plane before it turns back onto another $(0\overline{1}1)_{\gamma}$ plane, Fig. 8(b). The crack propagation, appears to involve only bond breaking with no visible dislocation emission and hence the fracture mode in single phase gamma can be characterized as brittle cleavage.

Fig. 9 shows the results of our molecular dynamics simulation of crack propagation in single phase beta under the boundary conditions identical to those applied to the beta part of the gamma-beta bicrystal in the fixed stress boundary conditions in $x$ and $y$ directions and the periodic boundary conditions in $z$ direction. For clarity only the innermost atoms near the crack-tip region are shown and the open and filled circles are used to differentiate between the atoms residing on two adjacent $(110)_{\text{bcc}}$ planes. The first evidence of the formation of the h.c.p. phase was seen at approximately 0.4 ps and only on the portion of crack surfaces close to the crack tip. As described earlier, the b.c.c.$\rightarrow$h.c.p. martensitic transformation involves $\{110\}_{\text{bcc}}\langle\overline{1}10\rangle_{\text{bcc}}$ shuffling and $\{112\}_{\text{bcc}}\langle 11\overline{1}\rangle$ pure shear. Ultimately the transformation front moves into the region ahead of the crack tip but as seen in Fig. 9, 3 ps, the very crack-tip region resists the b.c.c.$\rightarrow$h.c.p. transformation and instead acquires an f.c.o. structure. The resistance of the crack-tip region toward the b.c.c.$\rightarrow$h.c.p. transformation is consistent with the fact that there is a relatively large negative volume change $(\sim -5\%)$ associated with this transformation [3] and hence the region ahead of the crack tip which is under the largest positive hydrostatic stress opposes the transformation the most. Consequently the f.c.o. which is associated with a smaller negative transformation vol-

ume change $(\sim -3\%)$ rather than the h.c.p. structure forms at the crack tip. The approximate $-3\%$ volume change is in fair agreement with its counterpart in a Ti-10V-2Fe-3Al alloy $(-1.3\%)$ as reported by Durig et al. [32]. As a result of the observed martensitic transformation in Fig. 9, the crack tip became blunted and despite the fact that the applied stress intensity factor exceeds the Griffith stress intensity factor by $50\%$, the crack propagation ceases.

By comparing the atomic configurations shown in Fig. 6 (gamma/beta bicrystal), Fig. 8 (gamma crystal) and Fig. 9 (beta crystal), each corresponding to the same level of remotely applied stress, at least two important observations can be made regarding the ef- fect of martensitic transformation in the beta phase on the crack behavior in the gamma phase: (a) while the crack readily extends in the single phase gamma crystal, Fig. 8, its propagation ceases, at least temporarily, when a beta phase is present in the region ahead of the crack tip, Fig. 6; (b) the apparent toughening effect of the beta phase must be related to the accompanying martensitic transformation (the lattice-invariant slip de- formation included) in this phase which has almost completely transformed, Fig. 6.

![](./images/811028193661157378_10.jpg)

Fig. 8. Atomic positions in the single-phase gamma TiAl crystal with a crack projected on the $(2\overline{1}\overline{1})_{\gamma}$ plane after (a) 1 ps and (b) 10 ps of the simulation time.

At last, it is interesting to compare the effectiveness of martensitic transformation in enhancing the fracture toughness in the two-phase gamma-beta bicrystal with that in the single-phase beta crystal. To quantify the effect of martensitic transformation on materials tough- ness in the single-phase crystals, the Eshelby's conserva- tion integral $F$ [33], which provides a means for determination of the energy release rate accompanying crack extension in cases where plasticity effects cannot be neglected, was evaluated. The component of the Eshelby's integral along the crack propagation direc- tion $x$, $F_{1}$, which represents the force acting to propa- gate the crack tip, is given by:

$$
F_{1}=\int_{\Gamma}\left[W \delta_{1 j}-\sigma_{k j} \frac{\partial u_{k}}{\partial x_{1}}\right] \mathrm{d} S_{j}
\tag{27}
$$

where $W$ is the crystal strain energy density, $u_{k}$ is the k-component $(k=x,y)$ of the displacement, $\sigma_{k j}$ is the stress components, $\mathrm{d} S_{j}=\mathrm{d} S \cdot n_{j}$, here $n_{j}$ is the $j$ compo- nent $(j=x,y)$ of the unit outward normal vector to the contour segment of length $\mathrm{d} S$ and $\Gamma$ a closed contour surrounding the crack. In the present work $\Gamma$ was chosen as a circle centered at the crack tip with the radius of 4 nm.

It must be noted that Eq. (27) can only be applied if the field quantities (stress, strain, displacement) are continuous along the integration contour $\Gamma$. Since such continuity conditions for the field quantities are not satisfied (e.g. $\sigma_{r r}$ is discontinuous across the gamma/ beta interface), Eq. (27) cannot be used in the case of gamma-beta bicrystal. To overcome this problem, we recall the original definition of the energy release rate (the $J$ integral) in the nonlinear elastic materials:

$$
J=-\frac{1}{L} \frac{\mathrm{d} \Pi}{\mathrm{d} a}
\tag{28}
$$

where $\Pi$ and $L$ are respectively the potential energy and the thickness of the crystal and $a$ is the crack length. The potential energy is given by

$$
\Pi=U-W
\tag{29}
$$

where $U$ is the strain energy of the body and $W$ the work done by the external force. If the crack extends under the condition of fixed boundary displacement, ($\Delta=\mathrm{constant}$), there is no change in the work done by the external force, $\mathrm{d} W=0$. Hence, the combination of Eqs. (28) and (29) leads to

$$
J=-\frac{1}{L}\left(\frac{\mathrm{d} U}{\mathrm{~d} a}\right)_{\Delta}
\tag{30}
$$

![](./images/811028193661157378_11.jpg)

Fig. 9. Atomic positions in the single-phase beta Ti-15V crystal with a crack projected on the $(110)_{\beta}$ plane at (a) 0.4 ps and (b) 3 ps of the simulation time.

Since the strain energy $(U)$ for the gamma/beta computational crystal can be readily evaluated by summing up the strain energy of all the atoms in the bicrystal, Eq. (30) was used in the present work to quantify the extent of toughening due to transformation. Under the assumption that Eqs. (2) and (3) can be used when the crack tip is few atomic spacings away from the interface plane, a series of atomic configurations was generated, each corresponding to the same level of applied stress (180 MPa) but with the crack tip shifted by $1-4\ d_{(110)_{\gamma}}$ into the gamma phase or $1-4\ d_{(110)_{\beta}}$ into the beta phase. Each configuration is next relaxed through the use of molecular dynamics simulations, for the same simulation time (e.g. 1 ps) under the boundary conditions described in connection with Fig. 3. Lastly, the positions of the boundary atoms are set of coincide with those in the case of the crack tip residing on the gamma-beta interface and the molecular dynamics simulation runs repeated. The $({\rm d}U/{\rm d}a)_{\Delta}$ term in Eq. (30) is then evaluated using a finite difference approximation, i.e.

$$
\left(\frac{\mathrm{d} U}{\mathrm{~d} a}\right)_{\Delta}=\frac{E_{a+\Delta a}^{R}-E_{a}^{R}}{\Delta a}=\frac{1}{\Delta a} \sum_{i=1}^{n_{R}}\left(E_{a+\Delta a}^{i}-E_{a}^{i}\right) \tag{31}
$$

where $E_{a}^{R}$ and $E_{a+\Delta a}^{R}$ refer to energy of a circular cylinder with the Radius $R$ and the center at the gamma/beta interface, where the crack tip is located at $a$ and $a+\Delta a$, respectively. $E^{i}$ pertains to the energy of atom $i$ in such cylinder and $n_{R}$ is the total number of atoms in the cylinder. It should be noted that since the $E^{i}$ calculated using the EAM approach includes both the strain and surface energy contributions, the substitution of Eq. (31) into Eq. (30), yield the net force acting on the crack tip (the $F_{1}$ integral) rather than the driving force acting on the crack tip (the $J$ integral).

To verify the validity of the aforementioned procedure and Eq. (31), $F_{1}$ integral was evaluated first for the two single phase crystals and the results compared with those obtained using Eq. (27). As shown in Fig. 10, the two sets of results are in excellent agreement for the case of gamma TiAl in which no phase transformation occurs. For the case of the single phase beta crystal, the agreement is only fair and for the largest contour radius used (18 nm), Eq. (31) overestimates $F_{1}$ obtained using Eq. (27) by approximately 35%. Nevertheless, it is quite encouraging that the trend in $F_{1}$ evaluated using Eq. (31) is correct, i.e. the net force acting on the interface is negative and hence this equation is used to evaluate $F_{1}$ for the gamma/beta bicrystal when the crack tip resides in the interface, Fig. 10. The results shown in Fig. 10 suggest that the martensitic transformation acts more effectively in opposing the crack propagation (i.e. the net force on the crack tip is more negative) when the crack resides in the beta phase as opposed to the

![](./images/811028193661157378_12.jpg)

Fig. 10. The circular contour radius dependence of energy release rate in the gamma/beta bicrystal, single phase gamma and single phase beta.

case when the crack is in the gamma phase and its tip is at the gamma/beta interface. In the beta phase, Fig. 9, there is a significant amount of transformation seen taking place in the crack wake (i.e. behind the crack tip), which assists crack tip blunting. Contrary, in the gamma-beta bicrystal, Fig. 6, the crack wake is situ- ated in the gamma phase which is brittle and provides little assistance to crack tip blunting.

The aforementioned procedure based on the use of Eqs. (30) and (31) is next employed to obtain a rough estimate of the shape of the fracture resistance ($J_R$ vs. $a$) curve for the case of a crack initially located in the gamma phase which moves into and continues to prop- agate inside the beta phase. As the schematic shown in Fig. 11 indicates, the shape of the resistance curve is closely related to the $-F_1$ vs. a curve under the dis- placement control conditions ($\Delta =$ constant).

![](./images/811028193661157378_13.jpg)

Fig. 11. A schematic representation of the fracture resistance ($J_R$ vs. $a$) curve and the fracture driving force ($J$ vs. $a$) curve under constant displacement conditions.

Fig. 12 shows the $-F_1$ vs. a curve obtained using the procedure based on Eqs. (30) and (31) for the case of a crack in the bulk gamma phase, a crack moving from gamma into beta and for a crack in the bulk beta phase. All the results shown in Fig. 12 were obtained under the same level of remotely applied uniaxial stress (180 MPa). The error bars are used to indicate the scatter in the $-F_1$ data obtained in each case for a different choice of the contour radius. The solid lines are used to connect the data obtained for $R=15$ nm. The results shown in Fig. 12 suggest that martensitic transformation gives rise to significant enhancement in materials toughness only when the crack tip is located on the beta phase side of the gamma/beta interface. This implies that the role of martensitic transformation ahead of the crack tip (present also when the crack tip is on the gamma phase side of the gamma/beta inter- face) has a less important role in transformation tough- ening than the transformation taking place in the crack wake behind the crack tip (present only when the crack tip is on the beta phase side of the gamma/beta inter- face).

Since gamma TiAl is an intrinsically brittle material, as was confirmed by our atomistic simulation results, Fig. 9, one should expect that the computed Griffith level of the stress intensity factor, $K_{Gr}$, is comparable with the measured values of the critical stress intensity factor, $K_{IC}$. However, for this comparison to be objec- tive, $K_{IC}$ values for the single crystal rather than those for the polycrystalline gamma TiAl should be used. Booth and Roberts [16] recently measured the tempera- ture dependent of the stress intensity factor in single- phase single crystal of Ti-54.7at.%Al gamma titanium aluminide. Extrapolation of their data gives $K_{IC}=1.1$

![](./images/811028193661157378_14.jpg)

Fig. 12. An approximate shape of the fracture resistance curve.

MPa $m^{1/2}$ and $K_{IC}=1.4$ MPa $m^{1/2}$ for $(100)_{\gamma}$ and $(001)_{\gamma}$ cleavage planes, respectively. Using these results and taking into account the differences in the surface energy of $(100)_{\gamma}$, $(001)_{\gamma}$ and $(011)_{\gamma}$ planes, the critical stress intensity factor for the $(011)_{\gamma}$ cleavage plane is obtained as $K_{IC}=0.91$ MPa $m^{1/2}$. This result suggests that the Griffith level and the 'measured' level of the stress intensity factor agree to within 20% of each other.

## 4. Conclusions

Based on the results presented in the present work, the following conclusions can be drawn:

(1) When a crack in the gamma TiAl phase makes contact with a gamma/Ti at.% V beta interface, the ensuing martensitic transformation in the beta phase causes a significant evolution of the material at the crack tip which has a major effect on the subsequent crack behavior and materials toughness.

(2) The martensitic transformation involves at least two different crystal structures of martensite, a b.c.o. structure closely related to the h.c.p. structure and an f.c.o. structure, each present in a number of crystallographically equivalent variants. A lattice invariant slip deformation, which accommodates the b.c.c. $\rightarrow$ f.c.o. transformation shape change, is found to take place in the f.c.o. martensite, while the similar shape change associated with the b.c.c. $\rightarrow$ b.c.o. martensitic transformation appears to be accommodated by simultaneous formation of at least two b.c.o. variants.

(3) The occurrence of martensitic transformation ahead of the crack tip causes the crack tip to blunt which reduces the force acting to propagate the crack and consequently the crack propagation ceases. The effect of transformation appears to be more effective in the case of a crack residing in the beta phase than in the case of a crack residing in the gamma phase with its tip at or slightly away from the gamma/beta interface.

## Acknowledgements

The work presented here has been supported by the National Science Foundation under Grants DMR-9317804 and CMS-9531930. The authors are indebted to Drs. Bruce A. MacDonald and William A. Spitzig of NSF for the continuing interest in the present work. The help of Professor D. Farkas in providing us with the TiAl EAM potentials and the helpful discussions with Professors P.F. Joseph and S.B. Biggers, Dr S.S. Pageau, Mr K. Gadi, Mr N. Zhang and Mr J. Du are greatly appreciated.

## References

[1] G.B. Olson and M. Cohen, in S.D. Antolovich, R.O. Ritchie and W.W. Gerberich (eds.), *Mechanical Properties and Phase Transformations in Engineering Materials*, TMS-AIME, 1986, p. 367.

[2] A.G. Evans and R.M. Cannon, *Acta Metall.*, 34 (1986) 761.

[3] P. Dang, *Ph.D. Thesis* in progress, Clemson University, 1996.

[4] C.L. Hom and R.M. McMeeking, *Int. J. Solids Struct.*, 26 (1990) 1211.

[5] R.G. Hoagland, M.S. Daw, S.M. Foiles and M.I. Baskes, *J. Mater. Res.*, 5 (1990) 313.

[6] R.G. Hoagland, M.S. Daw and J.P. Hirth, *J. Mater. Res.*, 6 (1991) 2565.

[7] A. Moncevicz, P.C. Clapp and J.A. Rifkin, *Mater. Res. Soc. Symp. Proc.*, 213 (1991) 209.

[8] Z.Z. Yu and P.C. Clapp, *Metall. Trans.*, 20A (1989) 1617.

[9] P.C. Clapp, Y. Shao and J.A. Rifkin, *Mater. Res. Soc. Symp. Proc.*, 246 (1992) 1.

[10] D. Kim, P.C. Clapp and J.A. Rifkin, *Mater. Res. Soc. Symp. Proc.*, 213 (1991) 249.

[11] M. Grujicic and P. Dang, *Mater. Sci. Eng.*, A205 (1996) 139.

[12] M. Grujicic and P. Dang, *Mater. Sci. Eng.*, A205 (1996) 153.

[13] M. Grujicic and P. Dang, *Mater Sci Eng.*, A199 (1995) 173.

[14] M.S. Daw and M.I. Baskes, *Phys. Rev. Lett.*, 50 (1983) 1285.

[15] M.S. Daw and M.I. Baskes, *Phys. Rev.*, B29 (1984) 6443.

[16] A. Booth and S.G. Roberts as referenced by M.H. Yoo, J. Zou and C.L. Fu, *Mater. Sci. Eng.*, A192/193 (1995) 14.

[17] B. Sundman, B.J. Jansson, J.O. Andersson, *Calphad*, 9 (1985) 153.

[18] R.A. Johnson, *Phys. Rev.*, B39 (1989) 12554.

[19] A.A. Maradudin, E.W. Montroll, G.H. Weiss and I.P. Ipatova, in H. Ehrenreich, F. Seitz and D. Turnbull (eds.), *Theory of Lattice Dynamics in the Harmonic Approximation*, Suppl. 3 in the Solid State Physics, 2nd edn., Academic Press, New York, 1971.

[20] P. Villars and L.D. Calvert (eds.), *Pearson's Handbook of Crystal- lographic Data for Intermetallic Phases*, Vol. 2, American Society for Metals, Metals Park, OH, 1985.

[21] M. Grujicic and C.P. Narayan, *Mater. Sci. Eng.*, A161 (1992) 217.

[22] Y. Yamada and Okumura, in S.N. Atluri, E.R. Gallagher and O.C. Zienkiewicz (eds.), *Hybrid and Mixed Finite Methods*, Wiley, New York, 1983, pp. 325.

[23] Y. Yamada and H. Okumura, in K. Kawata and T. Akasaka (eds.), *Proc. Jpn.-U.S.A. Conf.*, Tokyo, 1981, pp. 55-64.

[24] S. Benzley, *Int. J. Numer. Methods Eng.*, 8 (1974) 537.

[25] S.S. Pageau, P.F. Joseph and S.B. Biggers Jr., *Int. J. Numer. Methods Eng.*, 38 (1995) 81.

[26] S.S. Pageau, P.F. Joseph and S.B. Biggers Jr., *Int. J. Numer. Methods Eng.*, 38 (1995) 81.

[27] K.S. Gadi, P.F. Joseph and A.C. Kaya, Durability and damage tolerance of composites symposium, *Int. Mech. Eng. Congr. and Exposition, San Francisco, California, USA, November 12-17, 1995*.

[28] *ABAQUS Computer Program*, Version 5.4, Hibbitt, Karlsson, and Sorensen, Providence, RI, Sept. 1995.

[29] H.C. Andersen, *J. Chem. Phys.*, 72 (1980) 2348.

[30] J.C. Williams, in R.I. Jaffee and H.M. Burte (eds.), *Titanium Sci. Technol.*, 3 (1973) 1433.

[31] W.G. Burgers, *Physica*, 1 (1934) 561.

[32] T.W. Durig, P.M. Middieton, G.T. Terlinde and J.C. Williams, in R.I. Jafee and H.M. Burte (eds.), *Titanium Sci. Technol.*, 3 (1973), p. 1503.

[33] G.C. Sih and H. Liebowitz, in H. Liebowitz (ed.), *Fracture-An Advanced Treatise*, Vol. II, Academic Press, New York, 1968, p. 67.

[34] U. Dahmen, *Acta Metall.*, 30 (1982) 63.

[35] J.M. Rigsbee and H.I. Aaronson, *Acta Metall.*, 27 (1979) 351.

[36] Z.P. Bazant and L.F. Estenssoro, *Int. J. Solids Struct.*, 13 (1977) 479.