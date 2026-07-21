**Finite element analysis of quasistatic crack propagation in brittle media with voids or inclusions**

Dongwoo Sohn $^{\mathrm{a}}$, Jae Hyuk Lim $^{\mathrm{b}}$, Young-Sam Cho $^{\mathrm{c}}$, Jeong Ho Kim $^{\mathrm{d}}$, Seyoung Im $^{\mathrm{a},*}$

$^{\mathrm{a}}$ Department of Mechanical Engineering, Korea Advanced Institute of Science and Technology (KAIST), 291 Daehak-ro, Yuseong-gu, Daejeon 305-701, Republic of Korea
$^{\mathrm{b}}$ Satellite Structure Department, Korea Aerospace Research Institute, 115 Gwahangno, Yuseong-gu, Daejeon 305-333, Republic of Korea
$^{\mathrm{c}}$ Division of Mechanical and Automobile Engineering, College of Engineering, Wonkwang University, 344-2 Shinyoung-dong, Iksan, Jeonbuk 570-749, Republic of Korea
$^{\mathrm{d}}$ Applied Analysis team, MIDAS IT, SK Technopark Tech-center 15th floor, 190-1 Sangdaewon1-dong, Joongwon-gu, Seongnam, Gyeonggi-do 462-721, Republic of Korea

---

### ARTICLE INFO

**Article history:**
Received 10 August 2010
Received in revised form 1 March 2011
Accepted 15 May 2011
Available online 23 May 2011

**Keywords:**
Crack propagation
Variable-node finite elements
Heterogeneous materials
T-stress

---

### ABSTRACT

A three-level finite element scheme is proposed for simulation of crack propagation in heterogeneous media including randomly distributed voids or inclusions. To reduce total degrees of freedom in the view of mesh gradation, the entire domain is categorized into three regions of different-level meshes: a region of coarse-level mesh, a region of intermediate-level mesh, and a region of fine-level mesh. The region of coarse-level mesh is chosen to be far from the crack to treat the material inhomogeneities in the sense of coarse-graining through homogenization, while the region near the crack is composed of the intermediate-level mesh to model the presence of inhomogeneities in detail. Furthermore, the region very near the crack tip is refined into the fine-level mesh to capture a steep gradient of elastic field due to the crack tip singularity. Variable-node finite elements are employed to satisfy the nodal connectivity and compatibility between the neighboring different-level meshes. Local remeshing is needed for readjustment of mesh near the crack tip in accordance with crack growth, and this is automatically made according to preset values of parameters determining the propagation step size of crack, and so the entire process is fully automatic. The effectiveness of the proposed scheme is demonstrated through several numerical examples. Meanwhile, the effect of voids and inclusions on the crack propagation is discussed in terms of $T$-stresses, with the aid of three-level adaptive scheme.

© 2011 Elsevier Inc. All rights reserved.

---

### 1. Introduction

The modeling and simulation of heterogeneous materials using the conventional regular finite element method (FEM) would require a tremendously large number of degrees of freedom to model the geometry of inhomogeneities which have various sizes and properties with random distribution, and thus leading to a difficult and cumbersome procedure. Though numerous studies on crack problems have been conducted during the past decades using various methods such as conventional FEM [1–3], boundary element method [4–6], meshless method [7–10], extended finite element method (XFEM) [11–14], and finite 'crack' element method [15], most of those studies have been limited to the case of homogeneous materials with a few exceptions [16–20].

---

* Corresponding author. Tel.: +82 42 350 3028; fax: +82 42 350 5028.
E-mail address: sim@kaist.ac.kr (S. Im).
URL: http://mpsl.kaist.ac.kr (S. Im).

0021-9991/$ - see front matter © 2011 Elsevier Inc. All rights reserved.
doi:10.1016/j.jcp.2011.05.016

Recently, it has attracted an amount of substantial attention to explore the effect of microstructures on the macroscopic failure behavior of heterogeneous materials or structures [21-24]. This has been made possible due to the availability of increasingly strong computing powers and the development of new numerical schemes. Particularly, the fracture and damage phenomena for heterogeneous materials have been studied from various aspects [16-22]. To name a few among others, but not limited to, debonding failure in composite material by Voronoi cell finite element method (VCFEM) [16] or XFEM [17,18], cortical bone fracture by XFEM [19], crack propagation in heterogeneous media with random fracture properties by FEM and Monte Carlo simulation [20] have been reported. For the simulation of the crack propagation in heterogeneous media, it is necessary to consider how to reconstruct the mesh in accordance to crack propagation, as well as how to construct the mesh around the region of inhomogeneities. These issues are resolved not only by the conventional FEM [20,25], but also by XFEM with the aid of level set functions [17,18,26,27] and VCFEM [16,28,29].

Furthermore, with growing interest in multiscale approach, the crack problem in heterogeneous media has often been reconsidered as one of the representative multiscale problems in the computational mechanics community. The multiscale methods for heterogeneous media are classified as follows: the hierarchical method which provides a one-way transfer of information from the microscale to the macroscale; the concurrent method which provides the direct connection between the microscale and the macroscale; and the semi-concurrent method which provides a two-way transfer of information between the microscale and the macroscale, mixing the concurrent method with the hierarchical methods [30]. At this point, the homogenization techniques [25,31-38] are used to make the effect of the microscale averaged overall, and then the averaged properties are applied to the macroscale. The hierarchical multiscale methods are applied to simulate the crack propagation in heterogeneous media, e.g., failure of composite materials using XFEM in combination with the level set methods [39]. In this case, the coupling of the microscale and the macroscale is usually treated in a weak sense through variational approaches. Similarly, the concurrent and semi-concurrent methods are applied for various simulations reflecting the effect of inhomogeneities, such as cohesive failure in quasi-brittle solids with microstructure [25], crack propagation in plate with holes [26,40], the interaction of microcrack and macrocrack [27], debonding of fiber from matrix in composite material [28,29], and so forth. Here, an issue on the non-matching meshes, particularly between the microscale and the macroscale, is resolved by introducing of various techniques, e.g., projection [27], Lagrange multiplier [26,28,29], Arlequin method [41], and variable-node elements [40].

The purpose of this work is to expand the two-level modeling in our previous work [40] into a three-level modeling and computing scheme for efficient simulation of crack propagation in two-dimensional heterogeneous media having voids and inclusions or fibers. The main objective of the simulation lies in finding the crack path (see [11,15] for similar works) and exploring the effect of $T$-stress on the directional stability of crack growth, by resorting to static analysis not considering time integration of the structural dynamics equation, nor considering the fracture toughness of a given specimen. To calculate $T$-stress which is highly localized quantity, the domain in the vicinity of the crack tip should be discretized with much refined elements, hence two-level approach [40] is not enough to obtain meaningful values. For this reason, the three-level mesh modeling has been devised in this paper. In the present approach, the entire domain is divided into three different-level subdomains: a region of a coarse-level mesh, a region of intermediate-level (or inhomogeneity-level) mesh, and a region of fine-level mesh. The region of coarse-level mesh is chosen to be far from the crack to treat the material inhomogeneities in the sense of coarse graining through homogenization theory, while the region of intermediate-level mesh is taken near crack to model the inhomogeneities in detail. The intermediate-level mesh is needed to account for the effect of the presence of inhomogeneities on the crack propagation. Lastly, the region of fine-level mesh is designated to be very close to the crack tip where the finest mesh is utilized to capture a steep gradient of elastic field due to the crack tip singularity as well as to properly represent interactions of the crack tip with voids or inclusions.

Variable-node finite elements [15,42-48] are employed to satisfy the nodal connectivity and compatibility between the neighboring different-level meshes. Local remeshing is needed for readjustment of mesh near the crack tip in accordance with crack growth, and this is automatically made according to some preset values of parameters determining the propagation step-size and the initial orientation of crack, and so the entire process is fully automatic. In this work, the construction of intermediate-level mesh is based on the distance from the crack tip, because high stress would be evaluated in the vicinity of the crack tip. Subsequently, the fine-level mesh is constructed such that it may enclose the crack tip, and this region is made non-overlapping with the intermediate-level mesh region.

In the three-level approach, the homogenization theory is utilized in the coarse-level mesh as a simple hierarchical multiscale method, and the different-level mesh is connected by the variable-node elements, as implemented in the concurrent multiscale method. Although the cohesive zone modeling [25,49-51] may be appropriate to represent the heterogeneous material behaviors as well as the history-dependent nonlinear material behaviors near the crack tip, we assume that the inverse square-root singularity of stresses is retained within the applicable range of linear elastic fracture mechanics (LEFM). In this work, the inhomogeneities (voids or inclusions) in brittle media are regarded as themselves scaled down from the macroscopic voids and inclusions, and the calculation through the conservation integral [52-56] is carried out outside the inhomogeneities within the range of LEFM in the intermediate or fine-level mesh region. Once the crack tip meets or interferes with a void or inclusion, the computation based on the conservation integral is terminated, and hereon is continued under another assumption, based on some intuitive physical observation. We focus on the subject of how to efficiently analyze crack propagation in consideration of inhomogeneities of tiny voids or inclusions.

The outline of the paper is as follows. In Section 2, the present multi-level scheme with the aid of variable-node finite elements is discussed together with the classical homogenization theory [31-33], in the framework of two-dimensional FEM. Then, in Section 3 we explain how to determine the incremental growth of crack or the incremental length and direc- tion for crack propagation, and how to implement automatic remeshing near the crack tip in accordance with crack propa- gation. The incremental length is automatically determined by the configuration of elements near the crack tip, and the direction of crack growth is calculated by the maximum hoop stress criterion [57], under the assumption of linear elastic behaviors. Numerical examples are given in Section 4, and we discuss the effect of voids and inclusions in heterogeneous media on crack propagation, and the directional stability of crack growth in terms of T-stress. Some results are also compared with experimental results. Finally, we close the paper with concluding remarks in Section 5.

## 2. Multi-level adaptive finite element scheme

Consider a two-dimensional heterogeneous structure containing a crack, as seen in Fig. 1(a). The presence of inhomo- geneities, including voids or fibers, will greatly perturb the stress field near crack tip, and so affect crack propagation. Thus, we need an accurate finite-element modeling for these inhomogeneities to explore crack propagation in this case. Notice that it would require very fine finite-element mesh to represent geometries and properties of the matrix material and the inhomogeneities. Thus the modeling of crack propagation for this structure by conventional regular FEM would lead to an enormously large number of degrees of freedom. Accordingly, the computational cost would be extremely high. In addition, it would not be straightforward to model a moving or propagating crack by simple conventional FEM. In this context, a multi-level approach seems to be worthwhile to consider, particularly for reduction of the number of degrees of freedom.

As indicated in Fig. 1(b), we consider three non-overlapping subdomains $\Omega_1$, $\Omega_2$ and $\Omega_3$. Here $\Omega_1$, named the region of coarse-level, representing a subdomain far from the crack tip. Note that the detailed presence of inhomogeneities here other than the average material properties has little effect on the crack propagation. On the other hand, $\Omega_2$, named the region of intermediate-level or inhomogeneity-level, denotes a subdomain relatively close to the crack tip where the details of the presence of inhomogeneities may possibly have some effect on the crack propagation. Lastly, $\Omega_3$, named the region of fine-level indicates a subdomain very close to the crack tip wherein extremely high stress gradient is expected due to the crack tip singularity. The region $\Omega_1$ is modeled with coarse-level mesh wherein each individual finite element includes numerous inhomogeneities, and the effect of these inhomogeneities on the elastic field is collectively reflected on the modified material properties with the aid of the homogenization theory [25,31-38]. The region of intermediate-level or inhomogeneity-level $\Omega_2$ is covered with intermediate-level mesh, wherein a typical element size is sufficiently small to model the details of the inhomogeneities as they are. However, this mesh of inhomogeneity-level is not enough to capture a steep gradient of elastic field due to the singularity at the crack tip. Therefore, the region $\Omega_3$, which is of the finest level, is chosen very near the crack tip, where maximum refinement is taken and singular finite elements in Fig. 2(a) are utilized to represent the inverse square-root singularity of stresses. The mesh localized in this way is expected to be effective for mod- eling crack propagation, which is affected dominantly by the local stress field near the crack tip. However, due to three non- overlapping meshes with different resolutions, non-matching interfaces appear between two neighboring meshes in $\Omega_1$ and $\Omega_2$, and in $\Omega_2$ and $\Omega_3$, respectively, as indicated in Fig. 1(b). That is, the nodal connectivity and compatibility conditions are not satisfied across the interface between two different meshes. To resolve this issue, these interfaces are treated with the variable-node elements [15,42-48]. Replacing the layer of elements in contact with the non-matching interface by a layer of

![](./images/811659071743590400_1.jpg)

Fig. 1. Sketch of multi-level approach for heterogeneous media: (a) heterogeneous media with a crack and (b) three-level modeling.

the variable-node elements, we see that the entire domain with three non-overlapping meshes is connected in a seamless way.

### 2.1. Three-level FEM with the aid of variable-node finite elements

The variable-node finite elements were developed by Cho et al. [42,43] and Lim et al. [44–47], and have been applied to a variety of complex problems in FEM such as non-matching meshes [42–46], adaptive mesh refinement [47], and contact mechanics [48]. For two-dimensional quadrilateral elements, the variable-node finite elements were proposed to allow an arbitrary number of nodes on element edge for four-node linear elements [43–45] and nine-node quadratic elements [42,44]. To connect the linear element with the quadratic element, transition element [44] was also presented by combining quadratic interpolation on the part of edges with linear interpolation on the rest. Moreover, based on an eight-node hexa- hedral element in three-dimensional domains, the variable-node element was developed to allow additional nodes on the element face as well as element edge [47]. Among others, in this work, we adopt two-dimensional variable-node element with linear interpolation [44,45] and linear-quadratic interpolation [44,58]. The linear variable-node element, so called "$(4 + k + l + m + n)$-node finite element" [45], permits an arbitrary placement of $k$ additional nodes on the bottom edge of a four-node element, $l$ additional nodes on the right edge, $m$ additional nodes on the top edge, and $n$ additional nodes on the left edge, as shown in Fig. 2(b). The linear interpolation is kept on the edge associated with two neighboring nodes. Fig. 2(c) shows a linear-quadratic transition element with seven nodes as a special type of variable-node element. This ele- ment includes the three additional nodes on the three edges, and then it has the quadratic interpolation on three edges and linear interpolation on the other edge. All nodes including the additional nodes of the variable-node elements have their own degrees of freedom [44]. These elements satisfy the basic properties of finite elements, such as partition of unity, linear or quadratic completeness, Kronecker delta condition. Note that the variable-node elements are capable of attaining constant stress state, and pass the patch test [44,45]. Therefore, the variable-node elements are directly used in the framework of the conventional FEM, without any process such as projection, interpolation, and imposition of constraints on the interface be- tween the different meshes. In addition, when the domain is constructed with the variable-node elements, the system matrix remains symmetric, and then the symmetric solver is applicable to efficiently obtain the solution. That is, the use of this

![](./images/811659071743590400_2.jpg)

Fig. 2. The elements used in three-level modeling: (a) a quadratic element and a quarter-point singular element; (b) a linear $(4 + k + l + m + n)$-node element; and (c) a linear-quadratic transition element.

![](./images/811659071743590400_3.jpg)

Fig. 3. Multi-level modeling with the aid of variable-node finite elements: (a) connection of elements in $\Omega_1$ and $\Omega_2$ and (b) connection of elements in $\Omega_2$ and $\Omega_3$.

element makes it possible to connect the different-level meshes in a seamless way, satisfying nodal connectivity and compatibility across the interface.

Consider a crack as shown in the first of Fig. 3(a). The presence of the detailed inhomogeneities on the region far from the crack tip would hardly affect the crack propagation in the direct way. Therefore, we account for the effect of these inhomogeneities on the crack propagation in overall average sense through the homogenization theory [25,31-38]. The first of Fig. 3(a) depicts the geometry of the entire domain that contains numerous voids or inclusions. First, assume that the coarse meshes are employed over the entire domain, because it is not necessary to construct the fine mesh over the entire domain. To set up the region of the intermediate-level $\Omega_2$ initially on the coarse-level domain $\Omega_1$, we consider a circle of radius $R$ with the origin at the crack tip as shown in the first of Fig. 3(a). All elements inside or touched by the circle are now switched to the region of intermediate-level mesh $\Omega_2$, as shown in the second of Fig. 3(a). The range of intermediate-level region, indicated by $R$, can be determined by various ways. In principle, the intermediate-level mesh is employed around the region where high error is estimated, or where high equivalent stress is evaluated. Error estimation should be used to determine the size of the intermediate-level mesh region and where to deploy it. In the crack propagation problem, naturally it should be deployed near the crack tip. Regarding its size $R$, it is determined through trial and error. After checking the invariance of the numerical results varying radius $R$, we estimate the appropriate size of intermediate-level region. The interface between

![](./images/811659071743590400_4.jpg)

Fig. 4. Averaged mechanical properties from the homogenization theory in the case of the boundary condition consistent with $\bar{\varepsilon}^{T}=[\bar{\varepsilon}_{x}, 0,0]$.

the different-level meshes in $\Omega_{1}$ and $\Omega_{2}$ is straightforwardly connected by the variable-node finite elements, which are orange-colored¹ in Fig. 3(a).

The region of the intermediate-level $\Omega_{2}$ consists of finite elements smaller than a typical size of inhomogeneities as shown in Fig. 3(b), but this level of refinement is not enough to capture a steep gradient of the elastic field due to the crack tip singularity. For accurate representation of the stress field, the region of fine-level $\Omega_{3}$ is taken very close to the crack tip. In addition, quarter-point singular elements, made up of quadratic elements in Fig. 2(a), are employed in $\Omega_{3}$ to represent the inverse square-root singularity of stresses at the crack tip [58,59]. This naturally brings in quadratic elements around the singular elements in $\Omega_{3}$ while linear elements are employed in $\Omega_{2}$. As a consequence, the order of interpolation is now different across the interface between $\Omega_{2}$ and $\Omega_{3}$. To connect the different type of elements, linear-quadratic transition elements [44,58] as well as linear variable-node finite elements are introduced on the interface, as shown in Fig. 3(b). Note that orange color in Fig. 3(b) indicates the linear variable-node elements as before, while blue the linear-quadratic transition elements. The construction and refinement of the elements in $\Omega_{3}$ are discussed further in detail in Section 3.2.

### 2.2. Homogenization schemes

In this section, the effect of the inhomogeneities in $\Omega_{1}$ is averaged through the homogenization schemes. The homogenization schemes are a class of methods to obtain overall material properties. To efficiently analyze the porous materials and fiber-reinforced composite materials, homogenization schemes, e.g., Voigt average [31], Reuss average [32], Voigt-Reuss-Hill average [33], self-consistent method [34] and Mori-Tanaka method [35], are often employed. The computational homogenization [25,38] was also proposed to extract homogenized material properties, reflecting the effects of the inhomogeneities in the overall average sense. In this work, focusing on developing three-level scheme to calculate the crack path and T-stress in linear elastic fields rather than the homogenization theory, we adopt Voigt average, one of the simple classical homogenization theories [31-33], to obtain the equivalent material properties. Voigt average is based on the uniform strain field.

Firstly, consider a typical element in $\Omega_{1}$. This may be thought of as a representative volume element (RVE) with randomly distributed inhomogeneities, voids or inclusions. Next, we construct the intermediate or the inhomogeneity-level mesh in the RVE for modeling the inhomogeneities, as shown in Fig. 4. Next, on this RVE we impose displacement boundary conditions corresponding to a given equivalent strain field, say each of $\bar{\varepsilon}^{T}=[\varepsilon_{x}, \varepsilon_{y}, \gamma_{xy}]=[0.01,0,0],[0,0.01,0]$, and [0,0,0.01], and applying Gauss theorem as

$$
\bar{\varepsilon}_{m n}=\frac{1}{\Omega_{R V E}} \int_{\Omega_{R V E}} \frac{1}{2}\left(\frac{\partial u_{m}}{\partial x_{n}}+\frac{\partial u_{n}}{\partial x_{m}}\right) d \Omega=\frac{1}{2 \Omega_{R V E}} \int_{\Gamma_{R V E}}\left(u_{m} n_{n}+u_{n} n_{m}\right) d \Gamma,
\tag{1}
$$

where $\bar{\varepsilon}_{mn}$ is an equivalent strain tensor, and $\Omega_{RVE}$ is the area of the RVE. By taking an area-average of stress field $\sigma_{ij}$ over $\Omega_{RVE}$, which is obtained through finite element analysis, an equivalent stress tensor $\bar{\sigma}_{ij}$ can be obtained.

$$
\bar{\sigma}_{i j}=\frac{1}{\Omega_{R V E}} \int_{\Omega_{R V E}} \sigma_{i j} d \Omega.
\tag{2}
$$

Finally, we obtain an equivalent material stiffness tensor $\bar{C}_{ijmn}$ from the equivalent strain and stress tensors:

---
¹ For interpretation of colour in Figs. 3 and 10, the reader is referred to the web version of this article.

$$
\bar{\sigma}_{i j}=\bar{C}_{i j m n} \bar{\varepsilon}_{m n}. \tag{3}
$$

The equivalent material stiffness tensor $\bar{C}_{ijmn}$ is now applied to the respective corresponding RVE or finite element for which $\bar{C}_{ijmn}$ has been computed in the region $\Omega_{1}$ of the present three-level model. Under the assumption that the inhomogeneities are very randomly distributed, the homogenized property is contemplated as isotropic, and then the resulting elastic stiffness is expressed in terms of the homogenized Young's modulus and Poisson's ratio. In this case, the homogenized properties for uniform strain field are almost the same, regardless of the loading directions, i.e., $\bar{\varepsilon}^{T}=[0.01,0,0]$, and $[0,0.01,0]$. In this work, we assume that a RVE contains numerous inhomogeneities in a uniform random distribution, as shown in Fig. 4, hence only two material constants – equivalent Young's modulus and Poisson's ratio – are needed. If the inhomogeneities are not in

![](./images/811659071743590400_5.jpg)

Fig. 5. Three consecutive incremental steps of crack growth in the intermediate-level mesh.

a uniform random distribution, the homogenized properties depend on the loading directions, and the independent material constants more than two are required under the assumption that RVE is an anisotropic material.

## 3. Prediction of crack path and element-remeshing near the crack tip
In this work, we are concerned with crack propagation path under a given specimen geometry, and boundary or loading condition. The prime issue in relation to finding crack path is the determination of the incremental growth size and the propagation orientation in the presence of the inhomogeneities. Another important issue is how to implement adaptive remeshing near the crack tip in accordance with the moving crack tip, in the view of computational efficiency.

### 3.1. Incremental growth size and orientation in quasistatic crack propagation
In the simulation of quasistatic crack propagation, it is necessary to determine a proper incremental growth size of crack propagation at each step. Too large an incremental value of growth size for one step would result in extremely non-smooth path of crack propagation.

To explain how to determine a size of crack growth, consider three consecutive incremental steps of crack growth near the crack tip, as shown in Fig. 5(a)-(d). In these figures, only the intermediate-level mesh in $\Omega_{2}$ is shown near the crack tip, as crack-growth size is determined on the intermediate-level mesh. That is, Fig. 5 is not final mesh configuration, and it does not show the fine-level mesh near the crack tip in the subdomain $\Omega_{3}$. It will be described in detail in Section 3.2 how to construct the fine-level mesh initially from the intermediate-level mesh. In the mesh of the intermediate-level in $\Omega_{2}$, the crack tip is always located on the node where the vertices of three-node triangular elements in $\Omega_{2}$ converge, as shown in Fig. 5. The radial line from the crack tip in the direction of a new incremental crack growth will intersect with the outer edge of one of the triangular elements surrounding the crack tip in $\Omega_{2}$. For convenience, we consider this intersection point as the next position of the crack tip. Thus, the size of an incremental growth of crack is automatically determined according to the construction of the intermediate-level mesh in $\Omega_{2}$. Note that this incremental size for each step is small, as the typical element size in $\Omega_{2}$ is small enough to model the individual inhomogeneities.

The direction of an incremental crack growth is determined based on the maximum hoop stress criterion [57], which is one among the various criteria for crack path prediction. The maximum hoop stress criterion was recommended for plane mixed-mode problems [60]. This criterion assumes that an incremental crack growth takes place in the direction of the maximum hoop stress from the present crack tip, as illustrated in Fig. 6. The angle of crack growth $\theta$ is expressed in terms of stress intensity factors $K_{I}$ and $K_{II}$ as (see Appendix A for detail)

$$
\theta=2 \arctan \frac{1}{4}\left(K_{I} / K_{I I}+\operatorname{sign}\left(K_{I I}\right) \sqrt{\left(K_{I} / K_{I I}\right)^{2}+8}\right),
$$

where $K_{I}$ and $K_{I I}$ are obtained by two-state conservation integral [52-55] following the procedures in Appendix B.

The domain of the conservation integral can be considered as two different types, as shown in Fig. 7. One encloses the inhomogeneities, as indicated by Domain A in Fig. 7, while the other does not include any inhomogeneities like Domain B in Fig. 7. To retain the physical interpretation of the $J$-integral, i.e., the energetic force associated with the translation of the singularity inside the $J$-integral contour, the path of the $J$-integral should not enclose any singularities other than the crack tip, and so it is not supposed to enclose any inhomogeneities. In the same context, the contour of the two-state

![](./images/811659071743590400_6.jpg)

Fig. 6. A coordinate system at the crack tip and domain for the two-state conservation integral.

![](./images/811659071743590400_7.jpg)

Fig. 7. The determination of the domain of conservation integral.

conservation integral should not enclose any inhomogeneities in its interior [53]. Thus, the domain for all conservation integrals should be set up in the matrix avoiding any inhomogeneities. The size of the domain for conservation integral is

![](./images/811659071743590400_8.jpg)

Fig. 8. Several cases of the domain of the conservation integrals.

![](./images/811659071743590400_9.jpg)

Fig. 9. Assumption of crack growth: (a) when crack tip meets with a void and (b) when crack tip meets with an inclusion.

determined automatically according to the position of the crack tip and the distribution of inhomogeneities, and several typical examples of the domain are shown in Fig. 8.

When the crack tip meets with a void or an inclusion, the aforementioned maximum hoop-stress criterion with the con- servation integral is not applicable, but another criterion should be applied. For voids, we assume that, when the crack tip meets with a void, the incremental crack growth occurs along the radial direction from the center of the void in the direction of maximum hoop stress on the void boundary (see Fig. 9(a)). When a crack meets with an inclusion, there may be three possibilities: the incremental crack growth may take place toward the inclusion, toward the matrix, or along the interface between the matrix and the inclusion. For simplicity, we assume that the inclusions are rigid in that crack is not allowed to penetrate into the inclusions, so that the crack propagate incrementally either into the matrix or along the interface. In this case, the procedure of prediction of crack path is as follows. Firstly, based on the stress field in the vicinity of crack tip, the direction of the maximum principal stress is searched. Let $\mathbf{v}_p$ be a vector pointing to the direction of the maximum principal stress from the present crack tip as seen in Fig. 9(b). If $\mathbf{v}_p$ is toward the matrix, the direction of $\mathbf{v}_p$ is regarded as the crack propagation direction, and the crack tip escapes from the interface between the matrix and the inclusion. Otherwise, or if $\mathbf{v}_p$ is toward the inclusion, it is assumed that interfacial debonding occurs.

### 3.2. Element-refinement and mesh-readjustment in the vicinity of the crack tip

In LEFM, crack tips retain the inverse square-root singularity of stresses. As mentioned in Section 2.1, the quarter-point singular elements as shown in Fig. 2(a) are employed in $\Omega_3$ to represent the singularity. The finer mesh is constructed in $\Omega_3$, including these singular elements, so that a steep gradient of elastic stress field due to this crack tip singularity may be captured.

The procedure of constructing the fine-level mesh i.e., the further refinement of the initially intermediate mesh into the fine mesh near the crack tip is illustrated in Fig. 10, which is a zoom-in of the crack tip region in Fig. 5(a). All finite elements initially in $\Omega_2$ consist of the linear elements, and the region including the crack tip is modeled by using constant strain (three-node) elements just temporarily as illustrated in Fig. 5 or in Fig. 10(a), which shows a typical intermediate-level mesh. Next, further circumferential refinement of these three-node elements should be made such that the angle $\theta_e$ between two neighboring radial edges of a refined temporary triangular element is subtended in a sufficiently small angle to obtain rea- sonable results. For clarity, we construct elements in $\Omega_3$ such that the mesh may be refined in the circumferential direction until $\theta_e$ is less than $22.5^\circ$ as illustrated in Fig. 10(b) [61]. Again, it leads to the non-matching mesh problem due to the different number of nodes between the four-node elements in $\Omega_2$ and the three-node elements in $\Omega_3$, where the mesh has been refined in the circumferential direction (see Fig. 10(b)). When the variable-node finite elements are applied to

![](./images/811659071743590400_10.jpg)

Fig. 10. The reconstruction of elements in $\Omega_{3}$ including the crack tip.

the interface between $\Omega_{2}$ and $\Omega_{3}$, as indicated by orange-colored elements in Fig. 10(c), the nodal connectivity and compatibility is satisfied with linear interpolation between any two neighboring nodes on the interface [44,45], which is indicated by the boundary between the orange subdomain and the inner green subdomain in Fig. 10(c).

Now, the temporary three-node triangular elements in the inner green zone of Fig. 10(c) are refined to rectangular elements by forming circumferential bands of elements in the radial direction around the crack tip (see Fig. 10(d)). After this, all the triangular elements in contact with the crack tip in the inner most band of the refined mesh are now transformed to the quarter-point singular elements of Fig. 2(a). To match the interpolation order with these quarter-point singular elements surrounding the crack tip, we need to surround these singular elements by eight-node quadratic elements, as indicated by yellow in Fig. 10(d). These quadratic elements and the singular elements constitute the fine-level region $\Omega_{3}$. However, there is a problem yet to be resolved. The difference in element interpolation orders between the orange variable-node elements in $\Omega_{2}$ and the outmost band of the yellow elements in $\Omega_{3}$ leads to the incompatibility across the circumferential interface between the two regions in Fig. 10(d). To overcome this incompatibility due to the difference in interpolation, we replace the elements in the outermost circumferential band of the yellow elements in $\Omega_{3}$ in Fig. 10(d) with linear-quadratic transition elements [44,58], as indicated by blue in Fig. 10(e). Hence, the finer quadratic elements in $\Omega_{3}$ are linked to linear elements in $\Omega_{2}$ in a seamless way, satisfying the linear conformality on the interface between $\Omega_{2}$ and $\Omega_{3}$.

![](./images/811659071743590400_11.jpg)

Fig. 11. Strategy of the element-refinement in accordance with the crack propagation in the three-level framework.

The adjustment of mesh is described for several steps of crack growth in Fig. 11. Fig. 11(a)-(d) show the corresponding final meshes obtained from Fig. 5(a)-(d), respectively. Therefore, they sequentially show three consecutive steps of the incremental crack growth just as Fig. 5(a)-(d) do. Recall that the length of each incremental crack growth depends on the size of the element that will enclose the new incremental crack growth in $\Omega_{2}$ in the vicinity of crack tip, as mentioned in Section 3.1 with the aid of Fig. 5. As the crack tip moves, the elements at the vicinity of the crack tip are automatically adjusted and refined.

In accordance with crack propagation, the region of the intermediate-level mesh $\Omega_{2}$ has to be readjusted; a new intermediate-level region should be created as explained in Section 2.1. For efficiency, in addition, it is desirable to turn the old

region of $\Omega_2$ far behind the current crack tip, i.e., outside the circle with the radius $R$ centered at the current crack tip, back to the coarse-level region $\Omega_1$. However, it may be necessary to keep part of the previous region of $\Omega_2$, particularly in case the crack path is so tortuous as to affect the numerical solution.

## 4. Numerical examples

In this section, some numerical examples on crack propagation are presented to demonstrate the effectiveness of the present three-level scheme. These numerical examples are conducted in the framework of two-dimensional, quasi-static, and brittle crack propagation. The first example is a single-edge-notched-tension (SENT) specimen with no inhomogeneities. This example is chosen to examine the performance of the proposed scheme in term of accuracy. The stress intensity factors and $T$-stresses for the SENT specimen are calculated in the three-level framework, and the values are compared with reference solutions. The second example is a plate with a hole. This example is chosen in order to check whether or not the crack path is accurately predicted under the mixed mode condition. Another motivation for the choice of this example is to examine the validity of the assumption depicted in Fig. 9(a) when the crack tip meets with a void or hole. The third example is the double cantilever beam (DCB) specimen with a kinked crack. The crack paths for homogeneous and heterogeneous specimens are obtained under two different boundary conditions. Furthermore, the stability of change in crack propagation direction, depending on the type of the boundary conditions, is discussed in terms of $T$-stress. All computations are carried out under plane-strain assumption.

### 4.1. SENT specimen

A homogeneous SENT specimen is loaded under uniform uniaxial tension $\sigma$ on the top and bottom faces as seen in Fig. 12(a). The aspect ratio of specimen is $h/w = 1.0$, where the width and the height of specimen are $w$ and $2h$, respectively. Fig. 12(b) illustrates the construction of meshes in $\Omega_2$ and $\Omega_3$ in the cases of $R = 0.5\ell$, $R = \ell$ and $R = 2.0\ell$. Here $R$ denotes the size of the intermediate-level region $\Omega_2$ such that all elements touched by or inside the circle of radius $R$ with its center located at the crack tip in $\Omega_1$ may be transformed to $\Omega_2$, as described in Fig. 12(b). Furthermore, $\ell$ is the characteristic length of

![](./images/811659071743590400_12.jpg)

Fig. 12. A model of SENT specimen: (a) geometry and loading and (b) composition of meshes in $\Omega_2$ and $\Omega_3$ for varying ranges of the intermediate-level mesh in $\Omega_2$.

<table>
<caption>Table 1
The normalized stress intensity factor $K_I/\sigma\sqrt{\pi a}$ in the SENT specimen.</caption>
<thead>
<tr>
<th>$a/w$</th>
<th>Tada et al. [62]</th>
<th>Yang and Ravi-Chandar [63]</th>
<th colspan="3">Three-level FE (present)</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$R=0.5\ell$</th>
<th>$R=1.0\ell$</th>
<th>$R=2.0\ell$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.2</td>
<td>1.380</td>
<td>1.380</td>
<td>1.372</td>
<td>1.373</td>
<td>1.371</td>
</tr>
<tr>
<td>0.3</td>
<td>1.663</td>
<td>1.676</td>
<td>1.664</td>
<td>1.664</td>
<td>1.661</td>
</tr>
<tr>
<td>0.4</td>
<td>2.106</td>
<td>2.134</td>
<td>2.111</td>
<td>2.110</td>
<td>2.107</td>
</tr>
<tr>
<td>0.5</td>
<td>2.815</td>
<td>2.858</td>
<td>2.811</td>
<td>2.811</td>
<td>2.810</td>
</tr>
<tr>
<td>0.6</td>
<td>4.023</td>
<td>4.090</td>
<td>3.986</td>
<td>3.990</td>
<td>4.030</td>
</tr>
<tr>
<td>0.7</td>
<td>6.347</td>
<td>6.471</td>
<td>6.206</td>
<td>6.297</td>
<td>6.346</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2
The normalized $T$-stress $T\sqrt{\pi a}/K_I$ in the SENT specimen.</caption>
<thead>
<tr>
<th>$a/w$</th>
<th>Larsson and Carlsson [64]</th>
<th>Kfouri [65]</th>
<th>Al-Ani and Hancock [66]</th>
<th>Yang and Ravi-Chandar [63]</th>
<th colspan="3">Three-level FE (present)</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>$R=0.5\ell$</th>
<th>$R=1.0\ell$</th>
<th>$R=2.0\ell$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.2</td>
<td>−0.45</td>
<td>−0.43</td>
<td>−0.45</td>
<td>−0.423</td>
<td>−0.439</td>
<td>−0.437</td>
<td>−0.434</td>
</tr>
<tr>
<td>0.3</td>
<td>−0.37</td>
<td>−0.36</td>
<td>−0.40</td>
<td>−0.361</td>
<td>−0.372</td>
<td>−0.368</td>
<td>−0.368</td>
</tr>
<tr>
<td>0.4</td>
<td>−0.27</td>
<td>−0.26</td>
<td>−</td>
<td>−0.266</td>
<td>−0.277</td>
<td>−0.271</td>
<td>−0.271</td>
</tr>
<tr>
<td>0.5</td>
<td>−0.15</td>
<td>−0.14</td>
<td>−0.14</td>
<td>−0.142</td>
<td>−0.152</td>
<td>−0.146</td>
<td>−0.144</td>
</tr>
<tr>
<td>0.6</td>
<td>−</td>
<td>−</td>
<td>−</td>
<td>0.014</td>
<td>0.008</td>
<td>0.013</td>
<td>0.013</td>
</tr>
<tr>
<td>0.7</td>
<td>−</td>
<td>−</td>
<td>0.17</td>
<td>0.215</td>
<td>0.218</td>
<td>0.212</td>
<td>0.211</td>
</tr>
</tbody>
</table>

a typical coarse element in $\Omega_1$ i.e., the diagonal length of a typical element in $\Omega_1$. As crack length $a$ increases, three-level meshes are automatically readjusted and reconstructed according to the scheme described in Section 3.2.

The stress intensity factors and $T$-stresses are obtained by two-state conservation integral [52–55] (see Appendix B for detail). The normalized stress intensity factors for mode $I$ $K_I/\sigma\sqrt{\pi a}$ are shown in Table 1, and the normalized $T$-stresses $T\sqrt{\pi a}/K_I$ in Table 2. Our results from the present three-level approach are in good agreement with those evaluated by other methods [62–66], provided $R\geqslant1.0\ell$ is chosen, regardless of the values of $a/w$. That is, it can be deduced that the appropriate

![](./images/811659071743590400_13.jpg)

Fig. 13. Geometry and loading of a plate with a hole.

value of $R$ equals $1.0\ell$ to obtain efficient and accurate numerical solutions in this example, when $80 \times 80$ elements are employed for intermediate-level region corresponding to one element in the coarse-level region. Note that it is necessary to accurately calculate intensity factor to explore the orientation of crack propagation as the incremental direction of crack growth is determined by stress intensity factors.

### 4.2. A plate with a hole
Giner et al. [67] carried out the numerical analysis and experimental test of crack propagation with a plate with a hole as shown in Fig. 13. The concentrated load $P = 20$kN is imposed on the top and bottom holes in the plate, which meets the requirement for the plane-strain crack tip field. In the actual computation, we imposed the boundary conditions to avoid rigid body motions as follows: at the loading point on the bottom hole, the displacements in the $x$- and $y$-directions were fixed; at the loading point on the top hole, the displacement in the $x$-direction was fixed; and the load $P$ was imposed only on the top hole, leading to the reaction force $P$ on the bottom hole. The initial edge crack, of which the length $a_0$ is 10 mm, is located a little above from the plate centre. Therefore, the mixed mode fracture occurs due to the eccentric crack and the hole in the plate. The material properties are as follows: Young's modulus $E = 71.7$ GPa, and Poisson's ratio $\nu = 0.33$.

Fig. 14 shows the three different-level meshes, which are constructed according to the procedure mentioned in Sections 2 and 3. The entire domain consists of $10 \times 24$ coarse-level elements. In the regions where two holes in top and bottom sides of the plate and one hole in the proximity of the crack are located, the coarse meshes are refined up to the level of the intermediate-level mesh, so that part of the coarse-level region $\Omega_1$ is transformed to the intermediate-level region $\Omega_2$. Although three holes are far away from the crack tip at an initial state, the elements near the holes are refined to maintain the consistency in the view that the refined meshes are employed in the region where the stress concentration is expected. The refined meshes play a role to represent the stress concentration due to the geometry discontinuities and loads near the holes as well as the crack tip. Furthermore, each coarse element inside a circle with radius $R$ centered at the crack tip is refined to $10 \times 10$ intermediate elements. Subsequently the fine-level mesh region $\Omega_3$ is constructed near the crack tip. Here the variable-node finite elements are used to connect the different-level meshes between $\Omega_1$ and $\Omega_2$ and between $\Omega_2$ and $\Omega_3$. It makes the displacement field continuous over the entire domain. As the crack tip moves to the new position predicted by the maximum hoop stress criterion, the three-level meshes are automatically reconstructed.

The results of crack propagation were obtained varying the value of $R$. Fig. 15(a)-(c) show several stages of crack propagation in the cases of $R = 0.5\ell$, $R = \ell$, and $R = 2.0\ell$, respectively. Fig. 15(d) also shows the result in the case of $R = \infty$, which

![](./images/811659071743590400_14.jpg)

Fig. 14. Three-level modeling for the plate with a hole.

![](./images/811659071743590400_15.jpg)

Fig. 15. Contour plot of von Mises stress in the case of: (a) $R = 0.5\ell$; (b) $R = \ell$; (c) $R = 2.0\ell$; and (d) $R = \infty$.

implies that the entire domain consists of the intermediate elements except the fine elements in the vicinity of the crack tip. That is, the model in Fig. 15(d) is composed of the intermediate and fine elements without the coarse elements in contrast to the others. Note that the crack paths and stress plots are almost identical regardless of the values of $R$. During the simulation of crack propagation, the number of nodes at each step varies between 3,932 and 5,275 in the case of $R = \ell$, and between 29,747 and 30,120 in the case of $R = \infty$. From this fact, it turns out that the present three-level approach in the case of $R = \ell$ enables one to simulate the crack propagation accurately and efficiently by using only about 13.2–17.5% of the total nodes for the fine meshes in the case of $R = \infty$.

Fig. 16(a) displays the crack paths, as compared with the numerical and experimental results in [67]. The crack paths obtained by the present scheme are in qualitative agreement with the results by Giner et al. [67]. They finished the numerical simulation when the crack tip meets with a hole, but we obtain the crack path after the crack passes through the hole by the simple assumption illustrated in Fig. 9(a). Although the assumption of crack propagation in the hole is somewhat ad-hoc, it is found that the prediction of crack path is reasonable, as compared with the experimental result.

To discuss the directional stability of the crack growth in the present example, we first consider the near-tip stress fields for Mode I and Mode II, which are given as follows, respectively.

$$
\left\{
\begin{array}{l}
\sigma_{11}^{*} \\
\sigma_{22}^{*} \\
\sigma_{12}^{*}
\end{array}
\right\} = \frac{K_{I}}{\sqrt{2\pi r}} \cos(\theta/2)
\left\{
\begin{array}{l}
1 - \sin(\theta/2) \sin(3\theta/2) \\
1 + \sin(\theta/2) \sin(3\theta/2) \\
\sin(\theta/2) \cos(3\theta/2)
\end{array}
\right\} +
\left\{
\begin{array}{l}
T \\
0 \\
0
\end{array}
\right\} + O(r^{1/2}), \tag{4}
$$

$$
\left\{
\begin{array}{l}
\sigma_{11}^{*} \\
\sigma_{22}^{*} \\
\sigma_{12}^{*}
\end{array}
\right\} = \frac{K_{II}}{\sqrt{2\pi r}}
\left\{
\begin{array}{l}
- \sin(\theta/2)[2 + \cos(\theta/2) \cos(3\theta/2)] \\
\sin(\theta/2) \cos(\theta/2) \cos(3\theta/2) \\
\cos(\theta/2)[1 - \sin(\theta/2) \sin(3\theta/2)]
\end{array}
\right\} + O(r^{1/2}), \tag{5}
$$

where $\sigma_{km}^{*}$ indicates the stress component with reference to the local crack tip coordinate (see Fig. 6). The second term $T$ in Eq. (4), which is a constant normal stress along the crack, is called $T$-stress. $T$-stress plays an important role in the analysis of a kinked crack. It is known that positive $T$-stress induces the directionally unstable crack growth, while, on the contrary, negative $T$-stress leads to directionally stable crack growth under Mode $I$ loading [68].

![](./images/811659071743590400_16.jpg)

Fig. 16. The results for various values of R: (a) crack paths, as compared with the results in [67] and (b) T-stress versus the position of the crack tip in the x-direction.

For the problem under consideration, we now explore the directional stability of the crack growth in terms of T-stress. Fig. 16(b) shows the plot of T-stress versus the position of the crack tip in the x-direction. The plots of T-stress remain almost the same, regardless of the values of R, except a slight fluctuation occurs for $R=0.5\ell$ (see Fig. 16(b)). At the early stage of crack propagation, the T-stress is negative and the crack growth is stable such that it maintains the straight propagation. As the crack tip approaches the hole boundary, however, the T-stress changes to positive and the crack growth becomes unstable so that the crack is bent towards the hole. As the crack tip escapes from the hole, initially the T-stress is negative and the crack propagates in a stable manner along the straight path. The T-stress changes to positive at the later stage as the free boundary or the right free edge of the specimen is approached, but the crack path turns out to be straight as disturbances in the stress intensity factors are not large enough to change the dominance of Mode I.

![](./images/811659071743590400_17.jpg)

Fig. 17. Models of DCB with a kinked crack: (a) under the concentrated loading on the left end (BC1) and (b) under the constraint of uniform displacements on the top and bottom faces (BC2).

![](./images/811659071743590400_18.jpg)

Fig. 18. Three-level modeling for the homogeneous DCB specimen with the initial kinked crack.

![](./images/811659071743590400_19.jpg)

Fig. 19. Crack paths and contour plots of von Mises stress for the homogeneous DCB specimen under BC1.

![](./images/811659071743590400_20.jpg)

Fig. 20. The crack path in homogeneous material, as compared with the results by Belytschko and Black [11] and Cho and Im [15].

### 4.3. DCB with a kinked crack

Consider a DCB specimen with a kinked crack as shown in Fig. 17. The length and orientation of the kinked crack are $\Delta x=0.00762$ m and $\Delta \theta=0.1$ rad, respectively. The case of load $P$ applied on the left end as depicted in Fig. 17(a), which was studied by Belytschko and Black [11] and Cho and Im [15], is examined here again for comparison. The displacements are fixed on the right edge in Fig. 17(a). In addition, another loading condition is considered as seen in Fig. 17(b): the uniform displacement loading $\bar{u}$ is imposed on the specimen with the same geometry as that in Fig. 17(a). Let BC1 and BC2 indicate the boundary conditions as depicted in Fig. 17(a) and (b), respectively. The specimens are made of three different kinds of materials under plane-strain assumption: homogeneous, porous, and fiber-reinforced composite material. Throughout the examples, the size of intermediate-level region $\Omega_{2}$ is set to $R=\ell$ from the crack tip. Since the DCB specimen is discretized on a similar level to the previous SENT specimen, the value of $R$ deduced in Section 4.1 is used in this example.

#### 4.3.1. Crack propagation in homogeneous DCB specimen

Firstly, the simulation for the homogeneous specimen is conducted in the present three-level framework. The material properties are as follows: Young's modulus $E=207$ GPa, Poisson's ratio $v=0.3$. The entire domain is divided into 300 coarse elements in the initial state as shown in Fig. 18.

The three different-level meshes are constructed according to the procedure depicted in Fig. 3. As the crack propagates, the region of the intermediate-level $\Omega_{2}$ within a distance of $R$ from the present crack tip continues to be updated. During this update, each coarse element touched by or inside a new circle with radius $R$ from the current crack tip in $\Omega_{1}$ is refined into 6,400 ($80 \times 80$) intermediate elements, as shown in Fig. 18.

Fig. 19 shows several stages of crack propagation under BC1. The crack path obtained by the present three-level FE scheme is shown in Fig. 20, and it is in good agreement with that obtained by Belytschko and Black [11] and Cho and Im [15].

The result of crack propagation for the homogeneous material under BC2 is shown in Fig. 21. BC2 imposes a global constraint such that the crack may grow in Mode I while BC1 does not provide any constraint regarding the crack growth. This nature of BC2 makes the crack path remain straight for BC2 without bending despite the presence of the perturbation like the kink, as opposed to the bent crack path under BC1. (A visualization of the crack propagation shown in Figs. 19 and 21 is available online [69].)

#### 4.3.2. Crack propagation in heterogeneous DCB specimen

We now consider crack propagation for the heterogeneous media with inhomogeneities, such as a porous material or a fiber-reinforced composite material, under plane-strain assumption. It is assumed that the inhomogeneities of voids or fibers are distributed randomly. The material properties of fibers are as follows: Young's modulus $E=1,000$ GPa, Poisson's ratio

![](./images/811659071743590400_21.jpg)

Fig. 21. Crack paths and contour plots of von Mises stress for the homogeneous DCB specimen under BC2.

$v = 0.3$. The fibers are assumed to be rigid in the sense that they are not penetrated by crack. The properties of the matrix of the porous material and the composite material are the same as those of the homogeneous material treated in the previous

![](./images/811659071743590400_22.jpg)

Fig. 22. The modeling for heterogeneous DCB specimen: (a) 10 coarse elements with random distribution of the inhomogeneities each of which is refined into numerous intermediate elements and (b) the overall configuration.

subsection. To model heterogeneous DCB specimens, we consider 10 coarse elements for RVEs, each of which has its own random distribution of various sizes of inhomogeneities, voids or fibers, as depicted in Fig. 22(a): the various sizes of dots indicate either voids in the porous material or fibers in the fiber-reinforced composite material, and the inhomogeneities account for approximately 10% volume fraction of each RVE. The numbers of the nodes and the elements for each RVE are indicated below the individual elements; for example, #N(15,872/24,193) under the first RVE in Fig. 22(a) means that the number of the nodes is 15,872 for the porous material and 24,193 for the composite material in this RVE, while #E(14,928/24,016) that the number of the elements is 14,928 for the porous material and 24,016 for the composite material. The heterogeneous specimen is finally made up by randomly picking one of these 10 RVEs for each coarse-element site of the specimen in Fig. 22(b), which shows the overall configuration of the specimen.

![](./images/811659071743590400_23.jpg)

Fig. 23. Three-level modeling for the heterogeneous DCB specimen with the initial kinked crack and randomly distributed inhomogeneities.

Fig. 23 shows the three-level modeling for the heterogeneous DCB specimens in consideration of inhomogeneities like voids and fibers. The crack propagation in the porous material under BC1 is shown in Fig. 24(a). The equivalent Young's moduli are in the range of $\bar{E}=159.8-162.1$ GPa, and Poisson's ratio $\bar{v}=0.2860-0.2892$ for the porous material. Since it is known which RVE is substituted by each coarse element, each individual equivalent value is assigned to the corresponding coarse element in $\Omega_1$. The result for the composite material under BC1 is shown in Fig. 24(b). The distribution of inhomogeneities in the composite material is the same as that in the porous material. The equivalent Young's moduli are in the range of $\bar{E}=229.4-230.1$ GPa, and Poisson's ratio $\bar{v}=0.2978-0.2984$ for the composite material. From Fig. 24(a) and (b), the crack paths in the heterogeneous media are seen to be bent similar to that in the homogeneous material under BC1.

Fig. 25(a) and (b) show the results for the crack propagation in the porous material and the composite material, respectively, under BC2. It is seen that the crack paths in the heterogeneous media remain almost straight due to the nature of the strong global constraint of BC2 dictating the crack to grow in Mode I. (A visualization of the crack propagation for heterogeneous media under BC1 and BC2 is also available online [69].)

### 4.3.3. The effect of inhomogeneities and boundary conditions on the crack paths
The detailed distribution of the inhomogeneities may affect the crack propagation. For the purpose of exploring the effect of the inhomogeneity distribution on the crack propagation, we examine the crack propagation for two additional random distributions of the inhomogeneities under each of the two different boundary conditions. Including the distribution of the inhomogeneities we considered in the previous subsection, we now have three different distributions of the inhomogeneities. The crack propagation for each of these three inhomogeneity distributions is shown in Fig. 26. Case 1 in Fig. 26(a) and (b) shows the complete crack path of propagation for the inhomogeneity distribution considered in the previous subsection under each of the two boundary conditions BC1 and BC2. On the other hand, Case 2 in Fig. 26(c) and (d), and Case 3 in Fig. 26(e) and (f) show the results for the remaining two distributions of the inhomogeneities, respectively.

As shown in Fig. 26(a), (c), and (e), we see that the crack path in the heterogeneous media under BC1 is less bent than that in the homogeneous material due to the effect of inhomogeneities. The presence of some inhomogeneities, such as voids or fibers, perturbs the local stress field near the crack tip, and this will affect the crack path. It can be seen that the crack propagates mainly through voids in the porous material, and that the crack tip avoids the reinforced fibers in propagation in the composite material. The direction of crack path is then shifted according to the maximum hoop stress criterion. Furthermore,

![](./images/811659071743590400_24.jpg)

Fig. 24. Crack paths and contour plots of von Mises stress for heterogeneous DCB specimens under BC1: (a) porous material and (b) fiber-reinforced composite material.

the crack paths under BC2 are shown in Fig. 26(b), (d), and (f). It is observed that the crack paths remain almost straight for all media, irrespective of the distribution of inhomogeneities, due to the overall constraint effect of BC2.

Fig. 27 shows the plot of $T$-stress versus computational step throughout the crack propagation for the homogeneous media under BC1 and BC2, respectively. The $T$-stresses are normalized by the initial value for each of two boundary conditions

![](./images/811659071743590400_25.jpg)

Fig. 25. Crack paths and contour plots of von Mises stress for heterogeneous DCB specimens under BC2: (a) porous material and (b) fiber-reinforced composite material.

BC1 and BC2. It is seen that the $T$-stress remains always positive throughout the crack propagation under BC1, while always negative under BC2. In the case of BC1, due to the positive $T$-stress, the crack growth is not stable so that it is very sensitive to the presence of some perturbation such as a kink. That is, the crack is bent due to the kink. On the contrary, the all-time

![](./images/811659071743590400_26.jpg)

Fig. 26. The crack paths in three cases of the inhomogeneity distribution: (a) Case 1 under BC1; (b) Case 1 under BC2; (c) Case 2 under BC1; (d) Case 2 under BC2; (e) Case 3 under BC1; and (f) Case 3 under BC2.

negative $T$-stress throughout the crack propagation under BC2 makes the crack growth stable, and the crack maintain the straight path despite the presence of the kink. This clearly verifies the role of $T$-stress in relation to the directional stability of crack growth.

We now explore how the $T$-stress is related to the crack growth stability in the heterogeneous materials. In the present heterogeneous materials, the local stress distribution near the crack tip must be subjected to severe variation or fluctuation due to the presence of voids or fibers, as the inhomogeneities may greatly distort the stress field near the crack tip. Indeed, due to this fluctuation the $T$-stress is not always positive under BC1, nor always negative under BC2 in the case of the porous material or the composite material. Therefore, we consider the level of the $T$-stress at each step of incremental crack growth, and count the number of the incremental steps corresponding to a given level of the $T$-stress.

Figs. 28 and 29 show the plots of $T$-stress frequencies in the heterogeneous media, under BC1 and BC2, respectively. These have been obtained in the form of histogram by counting the frequencies of computational steps having a given level of $T$-stress for all of the intervals. All values on the horizontal axes in the plots are normalized by the initial $T$-stress of the homogeneous material under the same boundary condition.

The $T$-stress under BC1 in Fig. 28 is not always positive in contrast with the $T$-stress in the homogeneous material under the same boundary condition. However, from this histogram it is clear that the positive $T$-stress is dominant over the negative $T$-stress under BC1 for each of the porous material and the composite material. Note that the directional stability of crack growth is not secured when $T > 0$, and so the prevalently positive $T$-stress suggests that the crack tip may move toward the bottom face of the specimen or be bent under BC1, as seen in Fig. 26(a), (c), and (e) due to the presence of the kink.

Under BC2, again the $T$-stress distributions in the heterogeneous media fluctuate due to the presence of the inhomogeneities. The $T$-stress histogram under BC2 is shown in Fig. 29. Note that the $T$-stress is dominantly negative under BC2, though it does not remain negative throughout the crack propagation as in the homogeneous material under the same boundary condition. Therefore, the crack propagation under BC2 is more or less stable and the crack paths are almost straight, though there are a bit rugged paths appearing in the case of the porous materials. Counting the total number of steps that yield negative $T$-stress in the course of the crack propagation in the porous material as seen in Fig. 29(a), we find that approximately 70% of the steps yield negative $T$-stress, while the remaining 30% of the steps positive stress. In the composite material, the steps which yield negative $T$-stress account for approximately 90% of the total computational steps. Thus, the degree of the predominance of the negative $T$-stress in the porous material of Fig. 29(a) is a little weak compared with the case of the composite material in Fig. 29(b). The degree of predominance of the negative stress may be linked to the stability of change in crack propagation direction. From Fig. 26(b), (d), and (f), it can be seen that a bit rugged crack growth appears with the relatively weak predominance of the negative $T$-stress in the case of the porous materials, in contrast to the straight crack growth in the composite materials.

Before closing, we emphasize that the $T$-stress values are impossible to calculate just with the intermediate-level mesh in $\Omega_2$, as conducted in [40], without bringing in the fine-level region $\Omega_3$. The intermediate mesh in $\Omega_2$ is too coarse to calculate any meaningful values of the highly localized quantity like $T$-stress. Note that $T$-stress is in the nature of the higher order compared with stress intensity factors. Accordingly, the accurate calculation of $T$-stress requires much finer mesh than when

![](./images/811659071743590400_27.jpg)

Fig. 27. The normalized $T$-stress versus computational step in the homogeneous material under BC1 and BC2.

![](./images/811659071743590400_28.jpg)

Fig. 28. Histogram of the normalized T-stress under BC1: (a) porous material and (b) fiber-reinforced composite material.

we calculate stress intensity factors. According to our computation, the two-level computation involving only the coarse-le- vel region $\Omega_{1}$ and the intermediate-level region $\Omega_{2}$, as in [40], give reasonable values of stress intensity factors, but this two- level computation yields totally erroneous solutions for $T$-stress values.

### 5. Conclusion

In this paper, we have proposed the three-level adaptive finite element scheme for simulation of crack propagation in brittle media with inhomogeneities, such as voids and inclusions. The proposed scheme is tractable to the full automation of the procedure. The crack path in heterogeneous materials, as well as homogeneous materials, can be obtained efficiently by the three-level approach with the aid of variable-node finite elements and the homogenization technique. Three non- overlapping meshes in coarse-, intermediate-, and fine-level regions are implemented with different resolutions, and the

![](./images/811659071743590400_29.jpg)

Fig. 29. Histogram of the normalized T-stress under BC2: (a) porous material and (b) fiber-reinforced composite material.

variable-node finite elements are utilized to connect them in a seamless way. The concept of Voigt average is used as the homogenization scheme to reduce the number of degrees of freedom in the coarse-level region far from the crack tip. Some examples have been presented to demonstrate the accuracy and effectiveness of the proposed scheme.

Furthermore, we have discussed the effect of inhomogeneities and boundary conditions on the crack propagation. In par- ticular, with the aid of the present three-level adaptive computation it has been possible to examine the directional stability of crack growth in terms of $T$-stress, as well as the crack path. It is verified that the predominance of the negative $T$-stresses links to the stable direction of crack path like a straight line.

Based on the present results, it seems to be worthwhile to investigate the effect of the inhomogeneities on the crack prop- agation, varying the volume fraction and material properties of the inhomogeneities. Future works may include these inves- tigations, as well as the extension of the present scheme to three-dimensional crack propagation and dynamic problems with branched cracks.

### Acknowledgements

This work was supported by the National Research Foundation of Korea (NRF) Grant funded by the Korean Government (MEST) (No. R0A-2007-000-20115-0).

### Appendix A. The direction of the incremental crack growth

For a polar coordinate system at crack tip as shown in Fig. 6, the hoop stress $\sigma_{\theta\theta}$ and shear stress $\tau_{r\theta}$ are expressed in terms of stress intensity factors $K_I$ and $K_{II}$.

$$
\sigma_{\theta\theta}=\frac{1}{\sqrt{2\pi r}}\cos\frac{\theta}{2}\left[K_I\cos^2\frac{\theta}{2}-\frac{3}{2}K_{II}\sin\theta\right],
\tag{6}
$$

$$
\tau_{r\theta}=\frac{1}{2\sqrt{2\pi r}}\cos\frac{\theta}{2}[K_I\sin\theta+K_{II}(3\cos\theta-1)].
\tag{7}
$$

Since shear stress component $\tau_{r\theta}$ vanishes in the direction of the maximum hoop stress, the angle of the incremental crack growth $\theta$ in Fig. 6 is given as

$$
\theta=2\arctan\frac{1}{4}\left(K_I/K_{II}+\text{sign}(K_{II})\sqrt{(K_I/K_{II})^2+8}\right).
\tag{8}
$$

Two-state conservation integral is utilized for computing $K_I$ and $K_{II}$ [52-56], and the procedure to obtain $K_I$ and $K_{II}$ is explained in Appendix B.

### Appendix B. Two-state conservation integrals

The two-state conservation integrals are very useful for calculating stress intensity factors, and the intensities for the higher order eigenfunctions including T-stress (see [52-55] for detail). In this appendix, we briefly describe how to find stress intensity factors and T-stress following the procedure in the preceding references.

The stress field for mode I and mode II can be written as an eigenfunction expansion [53,70]. Near the crack tip for the local coordinate system (see Fig. 6), the stress components for Mode I are given as in Eq. (4), and the stress components for Mode II as in Eq. (5). In these equations, $K_I$ and $K_{II}$ are mode I and mode II stress intensity factors, and "T" is a non-singular term, which is called T-stress, and the higher order terms of the series expansion are neglected here.

Stress intensity factors and T-stress are obtained by two-state conservation integral, which is also called interaction or mutual integral. Two independent admissible states of a cracked body are considered: state 1 is corresponding to the actual field under consideration and state 2 is auxiliary field which is to be discussed in Appendix B.1 and B.2 in detail. Then, the $J$-integral of the superimposed field (actual and auxiliary) can be written as in the following equation [52-55]:

$$
J^{(1+2)}=\int_{\Gamma}\left[\frac{1}{2}\left(\sigma_{ij}^{*(1)}+\sigma_{ij}^{*(2)}\right)\left(\varepsilon_{ij}^{*(1)}+\varepsilon_{ij}^{*(2)}\right)\delta_{1j}-\left(\sigma_{ij}^{*(1)}+\sigma_{ij}^{*(2)}\right)\frac{\partial\left(u_i^{*(1)}+u_i^{*(2)}\right)}{\partial x_1^*}\right]n_j^*\mathrm{d}\Gamma,
\tag{9}
$$

where superscript "*" means the local coordinate system at the crack tip (see Fig. 6), $\left(\sigma_{ij}^{*(1)},\ \varepsilon_{ij}^{*(1)},\ u_i^{*(1)}\right)$ and $\left(\sigma_{ij}^{*(2)},\ \varepsilon_{ij}^{*(2)},\ u_i^{*(2)}\right)$ denote the stresses, strains, displacements of state 1 and state 2, respectively. Furthermore, $n_j^*$ is the component of unit normal vector to contour $\Gamma_0$. Note that Eq. (9) can be rewritten as follows:

$$
J^{(1+2)}=J^{(1)}+J^{(2)}+J^{(1,2)},
\tag{10}
$$

$$
J^{(1,2)}=\int_{\Gamma}\left[W^{(1,2)}\delta_{1j}^*-\sigma_{ij}^{*(1)}\frac{\partial u_i^{*(2)}}{\partial x_1^*}-\sigma_{ij}^{*(2)}\frac{\partial u_i^{*(1)}}{\partial x_1^*}\right]n_j^*\mathrm{d}\Gamma,
\tag{11}
$$

where $J^{(1,2)}$ is the mutual or interaction integral, $W^{(1,2)}$ in Eq. (11) is mutual interaction strain energy, which is given by

$$
W^{(1,2)}=\sigma_{ij}^{*(1)}\varepsilon_{ij}^{*(2)}=\sigma_{ij}^{*(2)}\varepsilon_{ij}^{*(1)}.
\tag{12}
$$

The mutual integral, a path integral in Eq. (11), is now converted into a domain integral by multiplying the weighting function $q(\mathbf{x})$. Applying divergence theorem to Eq. (11), $J^{(1,2)}$ is be expressed for the domain.

$$
J^{(1,2)}=\int_{A}\left[\sigma_{ij}^{*(1)}\frac{\partial u_i^{*(2)}}{\partial x_1^*}+\sigma_{ij}^{*(2)}\frac{\partial u_i^{*(1)}}{\partial x_1^*}-W^{(1,2)}\delta_{1j}^*\right]\frac{\partial q}{\partial x_j^*}\mathrm{d}A,
\tag{13}
$$

where domain $A$ is enclosed by contour $\Gamma_0+C_+-\Gamma+C_-$, and $q(\mathbf{x})$ has unit value on the inner contour $\Gamma$ and vanishes on the outer contour $\Gamma_0$ in Fig. 6.

In actual calculation, the boundary of the domain adopted as in Fig. 8 does not coincide with the element boundaries, and the domain boundary cuts some of the elements. In this case, the value of $J^{(1,2)}$ is approximated by simply integrating over the quadrature points included in the conservation integration domain. This approximation has been confirmed correct through comparison to the result from refined mesh wherein the domain boundary coincides with the element boundaries.

### B.1. Calculation of Stress intensity factors

The value of $J$-integral with stress intensity factors can be written as

$$
J=\frac{K_{I}^{2}}{\bar{E}}+\frac{K_{I I}^{2}}{\bar{E}},
\tag{14}
$$

where $\bar{E}$ is determined by Young's modulus $E$ and Poisson's ratio $v$,

$$
\bar{E}=
\begin{cases}
E & \text { for plane stress, } \\
E /\left(1-v^{2}\right) & \text { for plane strain. }
\end{cases}
\tag{15}
$$

We now expand $J^{(1+2)}$ in terms of $K_{I}$ and $K_{I I}$ according to Eq. (14).

$$
J^{(1+2)}=\frac{\left(K_{I}^{(1)}+K_{I}^{(2)}\right)^{2}+\left(K_{I I}^{(1)}+K_{I I}^{(2)}\right)^{2}}{\bar{E}}=J^{(1)}+J^{(2)}+\frac{2}{\bar{E}}\left(K_{I}^{(1)} K_{I}^{(2)}+K_{I I}^{(1)} K_{I I}^{(2)}\right).
\tag{16}
$$

From Eqs. (10) and (16), it follows that

$$
J^{(1,2)}=\frac{2}{\bar{E}}\left(K_{I}^{(1)} K_{I}^{(2)}+K_{I I}^{(1)} K_{I I}^{(2)}\right).
\tag{17}
$$

Taking state 2 as mode $I$ ($K_{I}^{(2)}=1.0$, $K_{I I}^{(2)}=0.0$), the mode $I$ stress intensity factor for the actual field is obtained.

$$
K_{I}^{(1)}=\frac{\bar{E}}{2} J^{(1,2)}.
\tag{18}
$$

Conversely, the mode $II$ stress intensity factor for the actual field can be obtained by choosing state 2 as mode $II$ ($K_{I}^{(2)}=0.0$, $K_{I I}^{(2)}=1.0$).

$$
K_{I I}^{(1)}=\frac{\bar{E}}{2} J^{(1,2)},
\tag{19}
$$

where $J^{(1,2)}$ is numerically calculated from Eq. (13). The state 2 or the auxiliary stress and displacement field are given by

$$
\sigma_{i j}^{*(2)}=\frac{K_{I}^{(2)}}{\sqrt{2 \pi r}} f_{i j}^{I}(\theta)+\frac{K_{I I}^{(2)}}{\sqrt{2 \pi r}} f_{i j}^{I I}(\theta) \quad(i, j=1,2),
\tag{20}
$$

$$
u_{i}^{*(2)}=\frac{K_{I}^{(2)}}{\mu} \sqrt{\frac{r}{2 \pi}} g_{i}^{I}(\theta)+\frac{K_{I I}^{(2)}}{\mu} \sqrt{\frac{r}{2 \pi}} g_{i}^{I I}(\theta) \quad(i, j=1,2).
\tag{21}
$$

The functions of $\theta$ are given as follows:

$$
\left\{\begin{array}{l}
f_{11}^{I}(\theta) \\
f_{22}^{I}(\theta) \\
f_{12}^{I}(\theta)
\end{array}\right\}=\cos (\theta / 2)\left\{\begin{array}{l}
1-\sin (\theta / 2) \sin (3 \theta / 2) \\
1+\sin (\theta / 2) \sin (3 \theta / 2) \\
\sin (\theta / 2) \cos (3 \theta / 2)
\end{array}\right\},
\tag{22}
$$

$$
\left\{\begin{array}{l}
f_{11}^{I I}(\theta) \\
f_{22}^{I I}(\theta) \\
f_{12}^{I I}(\theta)
\end{array}\right\}=\left\{\begin{array}{l}
-\sin (\theta / 2)[2+\cos (\theta / 2) \cos (3 \theta / 2)] \\
\sin (\theta / 2) \cos (\theta / 2) \cos (3 \theta / 2) \\
\cos (\theta / 2)[1-\sin (\theta / 2) \sin (3 \theta / 2)]
\end{array}\right\},
\tag{23}
$$

$$
\left\{\begin{array}{l}
g_{1}^{I}(\theta) \\
g_{2}^{I}(\theta)
\end{array}\right\}=\frac{1}{4}\left\{\begin{array}{l}
(2 \kappa-1) \cos (\theta / 2)-\cos (3 \theta / 2) \\
(2 \kappa+1) \sin (\theta / 2)-\sin (3 \theta / 2)
\end{array}\right\},
\tag{24}
$$

$$
\left\{\begin{array}{l}
g_{1}^{I I}(\theta) \\
g_{2}^{I I}(\theta)
\end{array}\right\}=\frac{1}{4}\left\{\begin{array}{l}
(2 \kappa+3) \sin (\theta / 2)+\sin (3 \theta / 2) \\
-(2 \kappa-3) \cos (\theta / 2)-\cos (3 \theta / 2)
\end{array}\right\},
\tag{25}
$$

where $\mu$ is shear modulus, and

![](./images/811659071743590400_30.jpg)

Fig. 30. A point force imposed at the crack tip.

$$
\kappa=
\begin{cases}
(3-v)/(1+v) & \text{for plane stress}, \\
(3-4v) & \text{for plane strain}.
\end{cases}
\tag{26}
$$

### B.2. Calculation of T-stress

T-stress is obtained from two-state conservation integral by taking the point force solution for the superimposed auxiliary field or state 2. Considering a point force $f$ at the crack tip in $x_1^*$-direction (see Fig. 30), the stress fields in local coordinate system are [71]

$$
\begin{aligned}
\sigma_{11}^{*(2)} & =-\frac{f}{\pi r} \cos ^{3} \theta, \\
\sigma_{22}^{*(2)} & =-\frac{f}{\pi r} \cos \theta \sin ^{2} \theta, \\
\sigma_{12}^{*(2)} & =-\frac{f}{\pi r} \cos ^{2} \theta \sin \theta,
\end{aligned}
\tag{27}
$$

$$
\begin{aligned}
& u_{1}^{*(2)}=-\frac{f(1+\kappa)}{8 \pi \mu} \ln \frac{r}{d}-\frac{f}{4 \pi \mu} \sin ^{2} \theta, \\
& u_{2}^{*(2)}=-\frac{f(\kappa-1)}{8 \pi \mu} \theta+\frac{f}{4 \pi \mu} \sin \theta \cos \theta.
\end{aligned}
\tag{28}
$$

where $d$ is a constant for the translational rigid body mode and chosen to be the coordinate of a fixed point on the $x_1^*$-axis as shown in Fig. 30. The auxiliary field in Eqs. (27) and (28) is substituted in Eqs. (11) and (13). Then, the two-state integral $J^{(1,2)}$ for the contour $\Gamma$ as shown in Fig. 6 is given in term of $T$-stresses.

$$
J^{(1,2)}=-\lim _{\Gamma \rightarrow 0} \int_{\Gamma} \sigma_{i j}^{*(2)} n_{j}^{*} u_{i, 1}^{*(1)} d \Gamma=-\frac{T}{\bar{E}} \lim _{\Gamma \rightarrow 0} \int_{\Gamma} \sigma_{i j}^{*(2)} n_{j}^{*} \delta_{i 1} d \Gamma.
\tag{29}
$$

From the overall equilibrium for state 2, a point force is expressed as

$$
f=-\lim _{\Gamma \rightarrow 0} \int_{\Gamma} \sigma_{i j}^{*(2)} n_{j}^{*} \delta_{i 1} d \Gamma.
\tag{30}
$$

From Eqs. (29) and (30), we obtain the relationship between the $T$-stress and the two-state integral as

$$
T=\frac{\bar{E}}{f} J^{(1,2)}.
\tag{31}
$$

### References

[1] D.V. Swenson, N. Kaushik, Finite element analysis of edge cracking in plates, Eng. Fract. Mech. 37 (1990) 641-652.

[2] D.V. Swenson, A.R. Ingraffea, Modeling mixed-mode dynamic crack propagation using finite elements: theory and applications, Comput. Mech. 3 (1988) 381-397.

[3] P.O. Bouchard, F. Bay, Y. Chastel, Numerical modelling of crack propagation: automatic remeshing and comparison of different criteria, Comput. Methods Appl. Mech. Eng. 192 (2003) 3887-3908.

[4] Y. Zhang, G. Ruan, A calculation model and boundary element method simulation for 3-D blunt cracks, Eng. Fract. Mech. 47 (1994) 317-325.

[5] J. Sladek, V. Sladek, Computation of strip yield lengths for a crack in 2-D stationary thermoelasticity using the BEM, Eng. Anal. Boundary Elem. 11 (1993) 189-193.

[6] M. Ohtsu, Crack propagation in concrete: linear elastic fracture mechanics and boundary element method, Theor. Appl. Fract. Mech 9 (1988) 55-60.

[7] M. Fleming, Y.A. Chu, B. Moran, T. Belytschko, Enriched element-free Galerkin methods for crack tip fields, Int. J. Numer. Methods Eng. 40 (1997) 1483-1504.

[8] P. Krysl, T. Belytschko, The element free Galerkin method for dynamic propagation of arbitrary 3-D cracks, Int. J. Numer. Methods Eng. 44 (1999) 767-800.

[9] B.N. Rao, S. Rahman, An efficient meshless method for fracture analysis of cracks, Comput. Mech. 26 (2000) 398-408.

[10] S.C. Fan, X. Liu, C.K. Lee, Enriched partition-of-unity finite element method for stress intensity factors at crack tips, Comput. Struct. 82 (2004) 445-461.

[11] T. Belytschko, T. Black, Elastic crack growth in finite elements with minimal remeshing, Int. J. Numer. Methods Eng. 45 (1999) 601-620.

[12] N. Moës, J. Dolbow, T. Belytschko, A finite element method for crack growth without remeshing, Int. J. Numer. Methods Eng. 46 (1999) 131-150.

[13] G. Ventura, E. Budyn, T. Belytschko, Vector level sets for description of propagation cracks in finite elements, Int. J. Numer. Methods Eng. 58 (2003) 1571–1592.

[14] A. Combescure, A. Gravouil, D. Grégoire, J. Réthoré, X-FEM a good candidate for energy conservation in simulation of brittle dynamic crack propagation, Comput. Methods Appl. Mech. Eng. 197 (2008) 309–318.

[15] Y.-S. Cho, S. Im, MLS-based variable-node elements compatible with quadratic interpolation. Part II: Application for finite crack element, Int. J. Numer. Methods Eng. 65 (2006) 517–547.

[16] S. Ghosh, Y. Ling, B. Majumdar, R. Kim, Interfacial debonding analysis in multiple fiber reinforced composites, Mech. Mater. 32 (2000) 561–591.

[17] N. Sukumar, D.L. Chopp, N. Moës, T. Belytschko, Modeling holes and inclusions by level sets in the extended finite-element method, Comput. Methods Appl. Mech. Eng. 190 (2001) 6183–6200.

[18] D.B.P. Huynh, T. Belytschko, The extended finite element method for fracture in composite materials, Int. J. Numer. Methods Eng. 77 (2009) 214–239.

[19] E. Budyn, T. Hoc, Multiple scale modeling for cortical bone fracture in tension using X-FEM, Eur. J. Comput. Mech. 16 (2007) 215–238.

[20] Z. Yang, X.F. Xu, A heterogeneous cohesive model for quasi-brittle materials considering spatially varying random fracture properties, Comput. Methods Appl. Mech. Eng. 197 (2008) 4027–4039.

[21] D. Paquet, S. Ghosh, Microstructural effects on ductile fracture in heterogeneous materials. Part I: Sensitivity analysis with LE-VCFEM, Eng. Fract. Mech. 78 (2011) 205–225.

[22] D. Paquet, S. Ghosh, Microstructural effects on ductile fracture in heterogeneous materials. Part II: Applications to cast aluminum microstructures, Eng. Fract. Mech. 78 (2011) 226–233.

[23] Y. Ni, M.Y.M. Chiang, Prediction of elastic properties of heterogeneous materials with complex microstructures, J. Mech. Phys. Solids 55 (2007) 517–532.

[24] S. Bordas, R.H.W. Hoppe, S.I. Petrova, Mechanical failure in microstructural heterogeneous materials, Proceedings of Numerical Methods Application: Lecture Notes in Computer Science, vol. 4310, Springer, 2007 (pp. 533–541)..

[25] C.V. Verhoosel, J.J.C. Remmers, M.A. Gutierrez, R. de Borst, Computational homogenization for adhesive and cohesive failure in quasi-brittle solids, Int. J. Numer. Methods Eng. 83 (2010) 1155–1179.

[26] P.A. Guidault, O. Allix, L. Champaney, C. Cornuault, A multiscale extended finite element method for crack propagation, Comput. Methods Appl. Mech. Eng. 197 (2008) 381–399.

[27] S. Loehnert, T. Belytschko, A multiscale projection method for macro/microcrack simulations, Int. J. Numer. Methods Eng. 71 (2007) 1466–1482.

[28] S. Ghosh, J. Bai, P. Raghavan, Concurrent multi-level model for damage evolution in microstructurally debonding composites, Mech. Mater. 39 (2007) 241–266.

[29] P. Raghavan, S. Li, S. Ghosh, Two scale response and damage modeling of composite materials, Finite Elem. Anal. Des. 40 (2004) 1619–1640.

[30] T. Belytschko, J.-H. Song, Coarse-graining of multiscale crack propagation, Int. J. Methods Eng. 81 (2010) 537–563.

[31] W. Voigt, Lehrbuch der Kristallphysik, Teubner, Leipzig, 1928.

[32] A. Reuss, Berechnung der Fließgrenze von Mischkristallen auf Grund der Plastizitätsbedingung für Einkristalle, Z. Angew. Math. Mech. 9 (1929) 49–58.

[33] R. Hill, The elastic behavior of a crystalline aggregate, Proc. Phys. Soc. A. 65 (1952) 349–352.

[34] R. Hill, A self-consistent mechanics of composite materials, J. Mech. Phys. Solids 13 (1965) 213–222.

[35] T. Mori, K. Tanaka, Average stress in matrix and average elastic energy of materials with misfitting inclusions, Acta Metall. 21 (1973) 571–574.

[36] Z. Hashin, S. Shtrikman, A variational approach to the theory of the elastic behavior of multiphase materials, J. Mech. Phys. Solids 11 (1963) 127–140.

[37] I. Tsukrov, J. Novak, Effective elastic properties of solids with defects of irregular shapes, Int. J. Solids Struct. 39 (2002) 1539–1555.

[38] K. Terada, M. Hori, T. Kyoya, N. Kikuchi, Simulation of the multi-scale convergence in computational homogenization approaches, Int. J. Solids Struct. 37 (2000) 2285–2311.

[39] T. Hettich, A. Hund, E. Ramm, Modeling of failure in composites by X-FEM and level sets within a multiscale framework, Comput. Methods Appl. Mech. Eng. 197 (2008) 414–424.

[40] D. Sohn, J.H. Lim, Y.-S. Cho, S. Im, Multiscale finite element method for heterogeneous media with microstructures: crack propagation in a porous medium, J. Multiscale Modell. 1 (2009) 157–176.

[41] H.B. Dhia, G. Rateau, The Arlequin method as a flexible engineering design tool, Int. J. Numer. Methods Eng. 62 (2005) 1442–1462.

[42] Y.-S. Cho, S. Im, MLS-based variable-node elements compatible with quadratic interpolation. Part I: Formulation and application for non-matching meshes, Int. J. Numer. Methods Eng. 65 (2006) 494–516.

[43] Y.-S. Cho, S. Jun, S. Im, H.-G. Kim, An improved interface element with variable nodes for non-matching finite element meshes, Comput. Methods Appl. Mech. Eng. 194 (2005) 3022–3046.

[44] J.H. Lim, S. Im, Y.-S. Cho, Variable-node elements for non-matching meshes by means of MLS (moving least square) scheme, Int. J. Numer. Methods Eng. 72 (2007) 835–857.

[45] J.H. Lim, D. Sohn, J.H. Lee, S. Im, Variable-node finite elements with smoothed integration techniques and their applications for multiscale mechanics problems, Comput. Struct. 88 (2010) 413–425.

[46] J.H. Lim, S. Im, (4+n)-noded MLS (Moving Least Square)-based finite elements for mesh gradation, Struct. Eng. Mech. 25 (2007) 91–106.

[47] J.H. Lim, S. Im, Y.-S. Cho, MLS (Moving Least Square)-based finite elements for three-dimensional non-matching meshes and adaptive mesh refinement, Comput. Methods Appl. Mech. Eng. 196 (2007) 2216–2228.

[48] J.H. Kim, J.H. Lim, J.H. Lee, S. Im, A new computational approach to contact mechanics using variable-node finite elements, Int. J. Numer. Methods Eng. 73 (2008) 1966–1988.

[49] M. Ortiz, A. Pandolfi, A finite-deformation irreversible cohesive element for three-dimensional crack-propagation analysis, Int. J. Numer. Methods Eng. 44 (1999) 1267–1282.

[50] M. Elices, G.V. Guinea, J. Gómez, J. Planas, The cohesive zone model: advantages, limitations and challenges, Eng. Fract. Mech. 69 (2002) 137–163.

[51] R. de Borst, M.A. Gutiérrez, G.N. Wells, J.J.C. Remmers, H. Askes, Cohesive-zone models, higher-order continuum theories and reliability methods for computational failure analysis, Int. J. Numer. Methods Eng. 60 (2004) 289–315.

[52] S. Im, K.-S. Kim, An application of two-state M-integral for computing the intensity of the singular near-tip field for a generic wedge, J. Mech. Phys. Solids 48 (2000) 129–151.

[53] I. Jeon, S. Im, The role of higher order eigenfields in elastic-plastic cracks, J. Mech. Phys. Solids 49 (2001) 2789–2818.

[54] Y. Lee, S. Im, On the computation of the near-tip stress intensities for three-dimensional wedges via two-state M-integral, J. Mech. Phys. Solids 51 (2003) 825–850.

[55] Y.J. Kim, H.-G. Kim, S. Im, Mode decomposition of three-dimensional mixed-mode cracks via two-state integrals, Int. J. Solids Struct. 38 (2001) 6405–6426.

[56] C.F. Shih, R.J. Asaro, Elastic-plastic analysis of cracks on bimaterial interfaces: Part I - small scale yielding, J. Appl. Mech. 55 (1988) 299–316.

[57] F. Erdogan, G.C. Sih, On the crack extension in plate under plane loading and transverse shear, J. Basic Eng. 85 (1963) 519–527.

[58] O.C. Zienkiewicz, R.L. Taylor, J.Z. Zhu, The finite element method: its basis and fundamentals, sixth ed., Elsevier Butterworth-Heinemann, Oxford, 2005.

[59] R.S. Barsoum, On the use of isoparametric finite element in linear fracture mechanics, Int. J. Numer. Methods Eng. 10 (1974) 25–37.

[60] H.A. Richard, M. Fulland, M. Sander, Theoretical crack path prediction, Fatigue Fract. Eng. Mater. Struct. 28 (2005) 3–12.

[61] Abaqus analysis user's manual (Volume II, Version 6.8), Dassault Systemes, 2008.

[62] H. Tada, P.C. Paris, G.R. Irwin, The Stress Analysis of Cracks Handbook, Del Research Corporation, 1975.

[63] B. Yang, K. Ravi-Chandar, Evaluation of elastic T-stress by the stress difference method, Eng. Fract. Mech. 64 (1999) 589–605.

[64] S.G. Larsson, A.J. Carlsson, Influence of non-singular stress terms and specimen geometry on small scale yielding at crack tips in elastic plastic materials, J. Mech. Phys. Solids 21 (1973) 263–277.

[65] A.P. Kfouri, Some evaluations of the elastic T-term using Eshelby's method, Int. J. Fract. 30 (1986) 301-315.

[66] A.M. Al-Ani, J.W. Hancock, J-dominance of short cracks in tension and bending, J. Mech. Phys. Solids 39 (1991) 23-43.

[67] E. Giner, N. Sukumar, J.E. Tarancón, F.J. Fuenmayor, An Abaqus implementation of the extended finite element method, Eng. Fract. Mech. 76 (2009) 347-368.

[68] B. Cotterell, J.R. Rice, Slightly curved or kinked cracks, Int. J. Fract. 16 (1980) 155-169.

[69] Crack Propagation in heterogeneous media, <http://mpsl.kaist.ac.kr/results/crack.html>, 2011.

[70] M.L. Williams, On the stress distribution at the base of a stationary crack, J. Appl. Mech. 24 (1957) 109-114.

[71] A. Sutradhar, G.H. Paulino, Symmetric Galerkin boundary element computation of T-stress and stress intensity factors for mixed-mode cracks by the interaction integral method, Eng. Anal. Boundary Elem. 28 (2004) 1335-1350.