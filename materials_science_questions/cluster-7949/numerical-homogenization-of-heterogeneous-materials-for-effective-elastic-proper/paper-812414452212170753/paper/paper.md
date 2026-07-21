# ELASTIC RESPONSE OF METAL MATRIX COMPOSITES WITH TAILORED MICROSTRUCTURES TO THERMAL GRADIENTS

JACOB ABOUDI
Faculty of Engineering, Tel-Aviv University, Ramat-Aviv 69978, Israel

MAREK-JERZY PINDERA
Civil Engineering and Applied Mechanics Department, University of Virginia, Charlottesville, VA 22903, U.S.A.

and

STEVEN M. ARNOLD
Aerospace Research Engineer, NASA-Lewis Research Center, Cleveland, OH 44135, U.S.A.

(Received 8 April 1993; in revised form 3 November 1993)

Abstract-A new micromechanical theory is presented for the response of heterogeneous metal matrix composites subjected to thermal gradients. In contrast to existing micromechanical theories that utilize classical homogenization schemes in the course of calculating microscopic and macroscopic field quantities, in the present approach the actual microstructural details are explicitly coupled with the macrostructure of the composite. Examples are offered that illustrate limitations of the classical homogenization approach in predicting the response of thin-walled metal matrix composites with large-diameter fibers to thermal gradients. These examples include composites with a finite number of fibers in the thickness direction that may be uniformly or nonuniformly spaced, thus admitting so-called functionally gradient composites. The results illustrate that the classical approach of decoupling micromechanical and macromechanical analyses in the presence of a finite number of large-diameter fibers, finite dimensions of the composite, and temperature gradient may lead to serious errors in the calculation of both macroscopic and microscopic field quantities. The usefulness of the new outlined approach in generating favorable stress distributions in the presence of thermal gradients by appropriately tailoring the internal microstructural details of the composite is also demonstrated.

## NOMENCLATURE

$u_{i}(S), T_{i}(S)$
displacement and traction components on the surface $S$ of a composite
$\varepsilon_{ij}^{0}, \sigma_{ij}^{0}$
average values of strains and stresses in a composite subjected to homogeneous boundary conditions
$\bar{\varepsilon}_{ij}, \bar{\sigma}_{ij}$
average values of strains and stresses in a representative volume element
$\varepsilon_{ij}(x_{k}), \sigma_{ij}(x_{k})$
strains and stresses at the point $x_{k}$ in a composite
$C_{ijkl}$
elements of the effective stiffness tensor of a composite
$p, q, r$
indices used to identify the cell $(p, q, r)$
$\alpha, \beta, \gamma$
indices used to identify the subcell $(\alpha \beta \gamma)$
$d_{\alpha}^{(p)}, h_{\beta}, l_{\gamma}$
dimensions of the subcell $(\alpha \beta \gamma)$ in the $p$th unit cell
$v_{(\alpha \beta \gamma)}^{(p)}$
volume of the subcell $(\alpha \beta \gamma)$
$\bar{x}_{1}^{(\alpha \beta)}, \bar{x}_{2}^{(\beta)}, \bar{x}_{3}^{(\gamma)}$
local subcell coordinates
$k_{i}^{(\alpha \beta \gamma)}$
coefficients of heat conductivity of the material in the subcell $(\alpha \beta \gamma)$
$T^{(\alpha \beta \gamma)}$
temperature field in the subcell $(\alpha \beta \gamma)$
$T_{0}^{(\alpha \beta)}$
temperature at the center of the subcell $(\alpha \beta \gamma)$
$T_{i}^{(\alpha \beta \gamma)}$
coefficients in the temperature expansion within the subcell $(\alpha \beta \gamma)$
$q_{i}^{(\alpha \beta \gamma)}$
components of the heat flux vector in the subcell $(\alpha \beta \gamma)$
$Q_{l l(m, n)}^{(\alpha \beta \gamma)}$
average values of the subcell heat flux component $q_{l}^{(\alpha \beta \gamma)}$ when $l=m=n=0$; higher-order heat fluxes for other values of $l, m, n$
$L_{(l, m, n)}^{(\alpha \beta \gamma)}$
surface integrals of subcell interfacial heat fluxes
$u_{i}^{(\alpha \beta \gamma)}$
displacement components in the subcell $(\alpha \beta \gamma)$
$w_{1}^{(\alpha \beta \gamma)}$
$x_{1}$ displacement component at the center of the subcell $(\alpha \beta \gamma)$
$\phi_{1}^{(\alpha \beta \gamma)}$
coefficients associated with the linear terms in the second-order expansion of the subcell displacement $u_{1}^{(\alpha \beta \gamma)}$
$\chi_{2}^{(\alpha \beta \gamma)}$
coefficients associated with the linear terms in the first-order expansion of the subcell displacement $u_{2}^{(\alpha \beta \gamma)}$
$\psi_{3}^{(\alpha \beta \gamma)}$
coefficients associated with the linear terms in the first-order expansion of the subcell displacement $u_{3}^{(\alpha \beta \gamma)}$

$U_{1}^{(\alpha \beta \gamma)}$
coefficients associated with the quadratic term $x_{1}^{(\alpha) 2}$ in the second-order expansion of the subcell displacement $u_{1}^{(\alpha \beta \gamma)}$

$V_{1}^{(\alpha \beta \gamma)}$
coefficients associated with the quadratic term $x_{2}^{(\beta) 2}$ in the second-order expansion of the subcell displacement $u_{1}^{(\alpha \beta \gamma)}$

$W_{1}^{(\alpha \beta \gamma)}$
coefficients associated with the quadratic term $x_{3}^{(\gamma) 2}$ in the second-order expansion of the subcell displacement $u_{1}^{(\alpha \beta \gamma)}$

$\varepsilon_{i j}^{(\alpha \beta \gamma)}$
local strain components in the subcell $(\alpha \beta \gamma)$

$\sigma_{i j}^{(\alpha \beta \gamma)}$
local stress components in the subcell $(\alpha \beta \gamma)$

$c_{i j k l}^{(\alpha \beta \gamma)}$
elements of the stiffness tensor of the material in the subcell $(\alpha \beta \gamma)$

$\Gamma_{i j}^{(\alpha \beta \gamma)}$
elements of the thermal tensor of the material in the subcell $(\alpha \beta \gamma)$

$S_{i j(l, m, n)}^{(\alpha \beta \gamma)}$
average values of the subcell stress components $\sigma_{i j}^{(\alpha \beta \gamma)}$ when $l=m=n=0$; higher-order stress components for other values of $l, m, n$

$I_{1(l, n, 0,0)}^{(\alpha \beta \gamma)}$
surface integrals of the subcell interfacial stresses $\sigma_{1 j}^{(\alpha \beta \gamma)}$ at $\bar{x}_{1}^{(\alpha)}= \pm d_{x}^{(\alpha)} / 2$

$J_{2(l, n, 0,0)}^{(\alpha \beta \gamma)}$
surface integrals of the subcell interfacial stresses $\sigma_{2 j}^{(\alpha \beta \gamma)}$ at $\bar{x}_{2}^{(\beta)}= \pm h_{\beta} / 2$

$K_{3(l, 0,0, n)}^{(\alpha \beta \gamma)}$
surface integrals of the subcell interfacial stresses $\sigma_{3 j}^{(\alpha \beta \gamma)}$ at $\bar{x}_{3}^{(\gamma)}= \pm l_{\gamma} / 2$

## 1. INTRODUCTION

The past 30 years have seen tremendous growth in the development and use of composite materials. The applications range from sporting and recreational accessories to advanced aerospace structural and engine components. Historically, composite materials have been classified into different categories based on the geometry and distribution of the reinforcement phase and the type of the matrix phase. For example, polymeric matrix (PMC), metal matrix (MMC), intermetallic matrix (IMC), and ceramic matrix (CMC) composites are four classes of composites based on the type of matrix used to contain the reinforcement phase. The reinforcement phase can be finite-length or continuous, oriented or random, thereby providing further classification into short-fiber, oriented or random composites, and unidirectional (continuous and oriented) composites.

Typically, the reinforcement phase in the various classes of composite materials is distributed in a statistically or macroscopically uniform fashion such that the resulting two-phase material is macroscopically homogeneous with properties that do not vary spatially. Numerous micromechanical approaches have been developed during the past 30 years, as discussed by Aboudi (1991), to calculate the average (often called *effective* or macroscopic) properties of such composites given the geometry, distribution and properties of the individual phases. The micromechanical analysis makes it possible to replace the heterogeneous microstructure of the composite with an equivalent homogeneous continuum characterized by a set of effective elastic properties that subsequently can be used in more complicated structural analyses. The effective elastic properties are defined as the constitutive parameters that relate volume averages of the stress and strain components under so-called homogeneous boundary conditions, specified either in terms of surface displacements or prescribed surface tractions.

The *central assumption* in applying the various well-established micromechanical techniques is the *existence* of a definable representative volume element (RVE) at each point within the heterogeneous continuum and the ability to apply homogeneous boundary conditions to such an element. This amounts to decoupling the local and global analyses by evaluating the effective material properties at a given point based only on the local states of stress and deformation at that point which are assumed to be known *a priori*. Such decoupling is based on the assumption of the applicability of a principle sometimes referred to in the literature as *the principle of local action* (Malvern, 1969). The decoupling of local and global analyses clearly limits the range of applicability of the classical homogenization approach to composites with very fine microstructures (i.e. inclusion dimensions) with respect to the overall dimensions of the composite, and imposes constraints on the severity of deformation gradients that can be admitted. Composites with fine microstructures include unidirectional composites reinforced with small-diameter fibers such as graphite and carbon, for instance. Alternatively, in composites containing relatively large-diameter fibers with respect to the thickness of a single ply, such as B/Al or SiC/Ti, the applicability and reliability of the traditional microscopic approach based on the concept of an RVE and the classical homogenization treatment is suspect, and remains to be established due to potential

coupling between the microstructure and the global response. This is illustrated in Fig. 1 for situations involving thermal gradients, and will be discussed in more detail in the following section.

Recently, a new concept involving tailoring the internal microstructure of the composite to achieve certain required response characteristics to given input parameters has taken root. This idea has been pursued vigorously by Japanese researchers [see, for example, Yamanouchi *et al.* (1990)] who have coined the term "functionally gradient materials" to describe this newly emerging class of composites. The idea involves spatially grading the properties of the material by using variable spacings between individual inclusions, as well as by using inclusions with different properties, sizes and shapes. Such an approach offers a number of advantages over the more traditional methods of changing the compliance of composite structural elements by varying the lamination sequence or dropping plies to reduce the cross-sectional geometry, for instance. Grading or tailoring

![](./images/812414452212170753_1.jpg)

Fig. 1. Applicability of the representative volume element based analysis for heterogeneous materials in the presence of thermal gradients.

![](./images/812414452212170753_2.jpg)

Fig. 2. Composite with nonperiodic fiber distribution in the $x_1$ direction (RCS denotes representative cross-section).

the internal microstructure of a composite material or a structural component allows the designer to truly integrate both the material and structural considerations into the final design and final product. This brings the entire structural design process to the material level in the purest sense, thereby increasing the number of possible material configurations for specific design applications.

Composite materials with tailored microstructures are ideal candidates for applications involving severe thermal gradients, ranging from thermal structures in advanced aircraft and aerospace engines to circuit boards. For instance, a direct consequence of the temperature gradient across the thickness of a structural component (such as a combustor liner or airfoil) is the tendency to bend in the out-of-plane direction. This tendency will be present irrespective of whether a homogeneous or heterogeneous material is considered. However, by judiciously tailoring the microstructure of a heterogeneous material, the thermal bending moment can be reduced, if not eliminated, consequently decreasing the severity of warping.

The potential benefits that may be derived from composites with tailored micro- structures have led to increased activities in the areas of processing, and materials science, of these materials. These activities, however, are handicapped by the lack of appropriate computational strategies for the response of functionally graded materials that explicitly couple the heterogeneous microstructure of the material with the global analysis. As implied by the foregoing brief discussion on the limits of applicability of the classical homogenization approach, and further elaborated upon in the following section, traditional micromechanical schemes currently used in analyzing functionally graded materials, that is those which implicitly assume the existence of an RVE and the validity of the principle of local state, suffer from theoretical shortcomings and cannot be used with confidence. As a result, a new analytical approach is presented (that explicitly couples the heterogeneous microstructure of the material with the global analysis) in order to respond to the current need to analyze the behavior of composites with tailored microstructures (e.g. functionally graded, large- diameter reinforcement) in the presence of thermal gradients. In particular, the problem considered herein is a composite plate with a finite thickness $H$ extending to infinity in the $x_2$-$x_3$ plane and subjected to a temperature gradient, see Fig. 2. The composite is reinforced by periodic arrays of fibers in the direction of the $x_2$ axis or the $x_3$ axis, or both. In the direction of the $x_1$ axis, hereafter called the functionally gradient (FG) direction, the fiber spacing between adjacent arrays may vary. The reinforcing fibers can be either continuous or finite-length. Further, each array of fibers can admit different thermoelastic properties. Consequently, the model admits a variety of tailored microstructural configurations whose response to the applied thermal gradient can be investigated (including unidirectional and bi-directional arrays with uniform or variable fiber spacings in the FG direction, as well as multi-phase arrays). These configurations can include functionally graded materials consisting of metallic and ceramic phases that produce continuously changing properties

for applications involving severe thermal gradients. In such applications, metallic-rich regions are placed in the vicinity of the surface exposed to lower temperatures whereas those regions exposed to elevated temperatures are ceramic-rich.

In addition, the present formulation makes it possible to test the applicability of the various homogenization schemes when predicting the response of composites with large-diameter fibers subjected to thermal gradients, i.e. when each ply consists of a single row of fibers in the thickness direction. Hence, the fundamental question of how many fibers (or plies) are required in the thickness direction for classical homogenization schemes to be valid in the presence of thermal gradients can therefore be finally answered using the present approach.

This question is the first to be addressed in Section 4 by presenting in-plane force and moment resultants in a composite with finite thickness reinforced with unidirectional SiC fibers, produced by the imposed temperature gradient, as a function of the number of uniformly spaced fibers in the FG direction for a fixed fiber volume fraction. These results are normalized by the continuum approach predictions obtained by first generating the effective thermoelastic properties of the individual rows of fibers using a suitable homogenization scheme and subsequently employing these effective properties in the ther- mal boundary-value problem of an equivalent homogeneous composite. Similarly, a bi- directionally reinforced composite with uniformly spaced fibers in both in-plane direc- tions is considered and the various quantities of interest compared with those obtained using the corresponding homogenized configuration. Finally, examples illustrating the effect of linearly, quadratically, and cubically varying fiber spacing in the FG direction are compared to the uniformly spaced configuration, and the advantages of using functionally graded composites with regard to reducing in-plane force and moment resultants are discussed.

## 2. ON THE APPLICABILITY OF THE CLASSICAL HOMOGENIZATION APPROACH

The various micromechanical approaches used to calculate effective properties of composites include use of simple Reuss and Voigt hypotheses, self-consistent schemes and their generalizations, differential schemes, the Mori-Tanaka method, concentric cylinder models, bounding techniques and approximate or numerical analyses of periodic arrays of inclusions or fibers in the surrounding matrix phase. As stated in the preceding section, the central assumption in applying these well-established techniques is the existence of an RVE and the ability to apply homogeneous boundary conditions to such an element. These homogeneous boundary conditions can be specified either in terms of surface displacements

$$
u_{i}(S)=\varepsilon_{i j}^{0} x_{j} \tag{1}
$$

or in terms of prescribed surface tractions

$$
T_{i}(S)=\sigma_{i j}^{0} n_{j}, \tag{2}
$$

where $n_{i}$ is the unit outward normal vector on the boundary surface $S$ of the composite, $x_{i}$ are the Cartesian coordinates of the surface, $\varepsilon_{i j}^{0}$ and $\sigma_{i j}^{0}$ are constants, and repeated index implies summation. For an inhomogeneous medium the constants $\varepsilon_{i j}^{0}$ and $\sigma_{i j}^{0}$ are the volume averaged strains and stresses under the prescribed boundary conditions given by eqns (1) and (2), respectively. This is a consequence of the following relations

$$
\bar{\varepsilon}_{i j}=\frac{1}{V} \int_{V} \varepsilon_{i j}\left(x_{k}\right) \mathrm{d} V=\frac{1}{V} \int_{S} \frac{1}{2}\left(u_{i} n_{j}+u_{j} n_{i}\right) \mathrm{d} S \tag{3}
$$

$$
\bar{\sigma}_{i j}=\frac{1}{V} \int_{V} \sigma_{i j}\left(x_{k}\right) \mathrm{d} V=\frac{1}{V} \int_{S} \frac{1}{2}\left(T_{i} x_{j}+T_{j} x_{i}\right) \mathrm{d} S, \tag{4}
$$

SAS 31:10-E

where $V$ is the volume enclosed by the surface $S$. The above relations hold provided that: the displacements $u_{i}$ are continuous; the tractions $T_{i}$ are continuous at all interfaces of the heterogeneous medium; and body forces vanish. Under the above conditions, the effective elastic moduli $C_{i j k l}$ are defined as

$$
\bar{\sigma}_{i j}=C_{i j k l} \bar{\varepsilon}_{k l}. \tag{5}
$$

In practice, the average strains and stresses that result from the application of homo- geneous boundary conditions are calculated for an RVE whose macroscopic behavior is indistinguishable from the behavior of the composite-at-large. By applying the homo- geneous boundary conditions to the bounding surface of the RVE, which are the same as the boundary conditions applied to the entire composite, its average behavior can be calculated. This average behavior, in turn, defines the composite's macroscopic properties. To qualify as an RVE, the volume of the element used to calculate average composite behavior must meet two criteria. First, it must be sufficiently small with respect to the dimensions of the composite-at-large in order to be considered a material point in the equivalent homogeneous continuum (i.e. $h \ll H$, see Fig. 1). Second, it must be sufficiently large with respect to the inclusion phase (i.e. $d \ll h$, see Fig. 1) so that to the first order the elastic strain energy induced by both sets of homogeneous boundary conditions is the same, rendering the effective elastic properties in eqn (5) independent of the manner in which boundary conditions are applied (Hill, 1963). In the case of periodic fiber arrays, the repeating unit cell is interpreted as the RVE provided that the homogeneous boundary conditions are replaced by either symmetry conditions on the deformation of the unit cell or periodic boundary conditions, depending on the type of loading.

Clearly, the range of applicability of the aforementioned approaches is limited to composites reinforced by fibers with very small diameters such as graphite or carbon fibers. In such composites, a typical RVE contains a sufficiently large number of fibers while occupying a very small volume of the entire composite, allowing one to disregard boundary- layer effects near the bounding surfaces of the RVE upon application of either type of homogeneous boundary conditions. As a result, even in the presence of highly inhomo- geneous deformation gradients within the composite-at-large, the field quantities within the RVE will not vary significantly, thereby permitting the definition of a material property at a point in the equivalent homogeneous continuum. In contrast, in composites with relatively large-diameter fibers with respect to the thickness of a single ply, the variation of the quantities of interest within the RVE (assuming that it can be defined) invalidates the basic assumptions on which the concept of effective properties is based. These local variations of the field quantities within the RVE may give rise to unexpected phenomena rooted in the local-global coupling which is neglected in the traditional micromechanical homogenization schemes. For instance, different thermal conductivities of the individual phases together with their directional arrangement may produce thermal gradients in the individual phases which are quite different from the thermal gradients in the homogeneous composite with equivalent effective properties subjected to identical boundary conditions (Fig. 1). This, in turn, may alter the local conductivity characteristics and produce unexpected effects such as localized "hot spots" for instance. The size of the RVE in relation to the thickness of the composite and the temperature gradient obviously will play an important role in the above scenario.

The preceding discussion raises questions about the applicability of the traditional microscopic approach based on the concept of an RVE in the presence of large thermal gradients and coarse or spatially variable microstructure. In light of this discussion, the current practice of decoupling the local response from the global response by calculating pointwise effective thermoelastic properties of functionally graded materials without regard to whether the actual microstructure admits the presence of an RVE, and subsequently using these properties in the global analysis of the heterogeneous material, remains to be justified. These issues were discussed qualitatively as early as 1974 by Pagano (1974) with regard to mechanical loading of macroscopically homogeneous composites. No further work in this area appears to have been published in the open literature since then. In order

![](./images/812414452212170753_3.jpg)

Fig. 3. The repeating unit cell of a composite with nonperiodic fiber distribution in the $x_{1}$ direction.

to resolve these issues, a model is required that explicitly couples the microstructural and macrostructural analyses. The model presented in the following section is a step in this direction for applications involving composites with uniformly or nonuniformly spaced, large-diameter fibers subjected to through-the-thickness thermal gradients.

## 3. ANALYTICAL MODEL

The heterogeneous composite shown in Fig. 2 can be constructed using the basic building block or repeating unit cell given in Fig. 3. This unit cell consists of eight subcells designated by the triplet $(\alpha \beta \gamma)$. Each index $\alpha, \beta, \gamma$ takes on the values 1 or 2 which indicate the relative position of the given subcell along the $x_{1}, x_{2}$, and $x_{3}$ axis, respectively. The dimensions of the unit cell along the $x_{2}$ and $x_{3}$ axes, $h_{1}, h_{2}$, and $l_{1}, l_{2}$, are fixed for the given configuration since these are the periodic directions, whereas the dimensions along the $x_{1}$ axis or the FG direction, $d_{1}^{(p)}, d_{2}^{(p)}$, can vary from unit cell to unit cell. The dimensions of the subcells within a given cell along the FG direction are designated with a running index $p$ which identifies the cell number. We note that $p$ remains constant in the $x_{2}-x_{3}$ plane. For the other two directions, $x_{2}$ and $x_{3}$, the corresponding indices $q$ and $r$ are introduced. Thus, a given cell is designated by the triplet $(p, q, r)$ for $p=1,2, \ldots, M$, where $M$ is the number of fibers in the thickness or FG direction, and an infinite range of $q$ and $r$ due to the periodicity of the composite in the $x_{2}$ and $x_{3}$ directions. The material occupying each subcell within the unit cell can be represented by a different set of thermoelastic parameters, allowing considerations of multiphase media as well as bidirectionally reinforced con- figurations. It is important to note that the repeating unit cell in the present framework is not taken to be the RVE whose effective properties can be obtained through homogenization as explained below. Rather, the RVE comprises an entire column of such cells spanning the thickness of the plate. Thus the principle of local action cannot be applied to an individual cell, requiring the response of each cell to be explicitly coupled to the response of the entire column of cells in the FG direction. This is what is meant by the statement that the present approach explicitly couples the microstructural details with the global analysis.

The thermal boundary-value problem outlined in the foregoing is solved in two steps. In the first step, the temperature distribution in the heterogeneous composite is determined

by solving the heat equation under steady-state conditions in each subregion or cell of the composite. Since the composite is periodic in the $x_{2}-x_{3}$ plane, it is sufficient to determine the distribution of temperatures in a single row of cells spanning the FG dimensions only, provided that appropriate continuity and compatibility conditions are satisfied. These conditions ensure that the given cell is indeed indistinguishable from the adjacent cells in the $x_{2}-x_{3}$ plane. Given the temperature distribution in the entire volume occupying the composite, internal displacements, strains and stresses are subsequently generated by solving the equilibrium equations in each subregion of the composite subject to appropriate con- tinuity and boundary conditions. As in the case of the thermal problem, only a single row of cells is considered due to periodic nature of the composite in the $x_{2}-x_{3}$ plane.

The analytical technique for the above problem is a derivative of the approach developed by the first author in the treatment of the effective response of doubly and triply periodic composites, referred to as the "method of cells" (Aboudi, 1991) and most recently the "generalized method of cells" (Paley and Aboudi, 1992; Aboudi and Pindera, 1992). In the original formulation of the method of cells, a continuously reinforced, unidirectional fibrous composite is modeled as a doubly periodic array of fibers embedded in a matrix phase. The periodic character of the assemblage allows one to identify a repeating unit cell that can be used as a building block to construct the entire composite. The properties of this repeating unit cell are thus representative of the properties of the entire assemblage. The unit cell consists of a single fiber subcell surrounded by three matrix subcells. Hence the name "method of cells". The rectangular geometry of the repeating unit cell allows one to obtain an approximate, closed-form solution for the stresses and strains in the individual subcells given some macroscopically homogeneous state of strain or stress applied to the composite. The solution is obtained by approximating the displacement field in each of the subcells in terms of the displacement of the center of the subcell and a linear expansion in the local coordinates $\overline{\mathbf{x}}^{(\alpha)}, \overline{\mathbf{x}}^{(\beta)}, \overline{\mathbf{x}}^{(\gamma)}$ centered at the subcell's mid-point. The coefficients or microvariables associated with the linear terms in the expansion, and the unknown displacements at the subcell centers are obtained by satisfying continuity of tractions and displacements in an average sense between individual subcells of a given cell, and between adjacent cells. In addition, a connectivity condition is imposed on subcell center dis- placements of a given cell with respect to the corresponding subcell center displacements in adjacent cells, that provides the necessary expressions for homogenized strains in terms of the displacement gradients of the subcell mid-points. The approximate solution to the given boundary-value problem, in turn, is used to determine macroscopic (average) or effective properties of the composite. In the generalized method of cells, the repeating unit cell is subdivided into an arbitrary number of subcells which makes it possible to include multiple phases and additional geometric details in modeling the repeating unit cell. The procedure for analyzing local stress and strain fields in this case, however, is the same as that used in the original method of cells (i.e. by approximating local subcell displacements using linear expansions in terms of local coordinates in the individual subcells).

Conversely, in the present analysis a higher order theory is required in order to capture the local effects created by the thermal gradient, the microstructure of the composite, and the finite dimension in the FG direction. Accordingly, in the thermal problem the tem- perature field in each subcell of a repeating unit cell is approximated using a quadratic expansion in local coordinates along the three coordinate directions associated with the given subcell. In the solution for the local strains and stresses, the displacement field in the FG direction in each subcell is also approximated using a quadratic expansion in local coordinates within the subcell. The displacement field in the $x_{2}$ and $x_{3}$ directions, however, is still approximated using a linear expansion in local coordinates to reflect the periodic character of the composite's microstructure in the $x_{2}-x_{3}$ plane.

The unknown coefficients associated with the linear and quadratic local coordinates in both the thermal problem and the solution for internal strains and stresses are obtained by satisfying continuity of displacements and tractions and boundary conditions in an average sense along similar lines as those employed in the original and generalized method of cells. A fundamental difference, however, between the present solution and the previous treatments lies in the fact that the considered composite contains elements of both material

and structural effects which cannot be treated (i.e. decoupled) using the classical homogenization schemes. Accordingly, the connectivity conditions (which provide expressions for the homogenized strains in terms of the subcell mid-point displacement gradients) are not imposed in the FG direction in solving the given boundary-value problem since it is not possible to define homogenized strains in this direction using classical micromechanical concepts. This is due to the absence of homogeneous boundary conditions that hold for both the repeating unit cell and the composite-at-large, as well as the finite dimension of the composite in the FG direction. These features set the present model apart from the classical micromechanical approaches currently employed by researchers working in the area of functionally gradient materials.

An outline of this new analytical approach for both the thermal and mechanical problem that summarizes the governing equations for the determination of the temperature and displacement fields in the individual subcells will now be given. A detailed derivation of these equations is presented in the Appendices so as not to obscure the basic concepts by the involved algebraic manipulations.

### 3.1. Thermal analysis: problem formulation
Suppose that the composite material occupies the region $0 \leqslant x_{1} \leqslant H$, $|x_{2}| < \infty$, $|x_{3}| < \infty$. Let the composite be subjected to the temperature $T_{T}$ on the top surface $(x_{1}=0)$ and to $T_{B}$ on the bottom surface $(x_{1}=H)$. Also, let $M$ denote the number of cells in the interval $0 \leqslant x_{1} \leqslant H$, i.e.

$$
M=H \bigg/ \sum_{p=1}^{M} (d_{1}^{(p)}+d_{2}^{(p)}).
$$

For $p=2,\dots,M-1$ the cells are internal, whereas for $p=1$ and $P=M$ they are boundary cells.

#### 3.1.1. Heat conduction equation.
For a steady-state situation, the heat flux field in the material occupying the subcell $(\alpha\beta\gamma)$ of the $p$th cell, in the region defined by $|\tilde{x}_{1}^{(\alpha)}| \leqslant \frac{1}{2} d_{\alpha}^{(p)}$, $|\tilde{x}_{2}^{(\beta)}| \leqslant \frac{1}{2} h_{\beta}$, $|\tilde{x}_{3}^{(\gamma)}| \leqslant \frac{1}{2} l_{\gamma}$, must satisfy

$$
\partial_{1} q_{1}^{(\alpha\beta\gamma)}+\partial_{2} q_{2}^{(\alpha\beta\gamma)}+\partial_{3} q_{3}^{(\alpha\beta\gamma)}=0, \tag{6}
$$

where $\partial_{1}=\partial/\partial\tilde{x}_{1}^{(\alpha)}$, $\partial_{2}=\partial/\partial\tilde{x}_{2}^{(\beta)}$, $\partial_{3}=\partial/\partial\tilde{x}_{3}^{(\gamma)}$. The components of the heat flux vector $q_{i}^{(\alpha\beta\gamma)}$ in this subcell are derived from the temperature field according to

$$
q_{i}^{(\alpha\beta\gamma)}=-k_{i}^{(\alpha\beta\gamma)} \partial_{i} T^{(\alpha\beta\gamma)}, \quad i=1,2,3 ; \text{ no sum}, \tag{7}
$$

where $k_{i}^{(\alpha\beta\gamma)}$ are the coefficients of heat conductivity of the material in the subcell $(\alpha\beta\gamma)$, and no summation is implied by repeated Greek letters in the above and henceforth. Given the relation between the heat flux and temperature, a temperature distribution that satisfies the heat conduction equation is sought subject to the continuity and boundary conditions given below.

#### 3.1.2. Heat flux continuity conditions.
The continuity of the heat flux vector $\mathbf{q}^{(\alpha\beta\gamma)}$ at the interfaces separating adjacent subcells within the repeating unit cell $(p,q,r)$ is fulfilled by imposing the relations

$$
\left.q_{1}^{(1\beta\gamma)} \right|_{\substack{(p,q,r) \\ \tilde{x}_{1}^{(1)}=d_{1}^{(p)}/2}} = \left.q_{1}^{(2\beta\gamma)} \right|_{\substack{(p,q,r) \\ \tilde{x}_{1}^{(2)}=-d_{2}^{(p)}/2}} \tag{8a}
$$

$$
\left.q_{2}^{(\alpha1\gamma)} \right|_{\substack{(p,q,r) \\ \tilde{x}_{2}^{(1)}=h_{1}/2}} = \left.q_{2}^{(\alpha2\gamma)} \right|_{\substack{(p,q,r) \\ \tilde{x}_{2}^{(2)}=-h_{2}/2}} \tag{8b}
$$

$$
\left.q_{3}^{(\alpha\beta1)} \right|_{\substack{(p,q,r) \\ \tilde{x}_{3}^{(1)}=l_{1}/2}} = \left.q_{3}^{(\alpha\beta2)} \right|_{\substack{(p,q,r) \\ \tilde{x}_{3}^{(2)}=-l_{2}/2}} \tag{8c}
$$

In addition to the above continuity conditions within the $p$th cell, the heat flux continuity at the interfaces between neighboring cells must be ensured. The conditions that ensure this are given by

$$
\left.q_{1}^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=-d_{1}^{(p+1)} / 2} ^{\langle p+1, q, r\rangle}=\left.q_{1}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=d_{2}^{(p)} / 2} ^{\langle p, q, r\rangle}
\tag{9a}
$$

$$
\left.q_{2}^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=-h_{1} / 2} ^{\langle p, q+1, r\rangle}=\left.q_{2}^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=h_{2} / 2} ^{\langle p, q, r\rangle}
\tag{9b}
$$

$$
\left.q_{3}^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=-l_{1} / 2} ^{\langle p, q, r+1\rangle}=\left.q_{3}^{(\alpha \beta 2)}\right|_{\bar{x}_{3}^{(2)}=l_{2} / 2} ^{\langle p, q, r\rangle}.
\tag{9c}
$$

3.1.3. Thermal continuity conditions. The thermal continuity conditions at the interfaces separating adjacent subcells within the representative cell $(p, q, r)$ are given by relations similar to the corresponding heat flux continuity conditions

$$
\left.T^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=d_{1}^{(p)} / 2} ^{\langle p, q, r\rangle}=\left.T^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=-d_{2}^{(p)} / 2} ^{\langle p, q, r\rangle}
\tag{10a}
$$

$$
\left.T^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=h_{1} / 2} ^{\langle p, q, r\rangle}=\left.T^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=-h_{2} / 2} ^{\langle p, q, r\rangle}
\tag{10b}
$$

$$
\left.T^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=l_{1} / 2} ^{\langle p, q, r\rangle}=\left.T^{(\alpha \beta 2)}\right|_{\bar{x}_{3}^{(2)}=-l_{2} / 2} ^{\langle p, q, r\rangle}
\tag{10c}
$$

while the thermal continuity at the interfaces between neighboring cells is ensured, as in the case of the heat flux field, by requiring that

$$
\left.T^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=-d_{1}^{(p+1)} / 2} ^{\langle p+1, q, r\rangle}=\left.T^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=d_{2}^{(p)} / 2} ^{\langle p, q, r\rangle}
\tag{11a}
$$

$$
\left.T^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=-h_{1} / 2} ^{\langle p, q+1, r\rangle}=\left.T^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=h_{2} / 2} ^{\langle p, q, r\rangle}
\tag{11b}
$$

$$
\left.T^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=-l_{1} / 2} ^{\langle p, q, r+1\rangle}=\left.T^{(\alpha \beta 2)}\right|_{\bar{x}_{3}^{(2)}=l_{2} / 2} ^{\langle p, q, r\rangle}.
\tag{11c}
$$

3.1.4. Boundary conditions. The final set of conditions that the solution for the temperature field must satisfy are the boundary conditions at the top and bottom surfaces. The temperature in the cell $p=1$ at the top surface must equal the applied temperature $T_{T}$, whereas in the cell $p=M$ at the bottom surface the temperature must be $T_{B}$

$$
\left.T^{(1 \beta \gamma)}\right|^{(1, q, r)}=T_{T}, \quad \bar{x}_{1}^{(1)}=-\frac{1}{2} d_{1}^{(1)}
\tag{12}
$$

$$
\left.T^{(2 \beta \gamma)}\right|^{(M, q, r)}=T_{B}, \quad \bar{x}_{1}^{(2)}=\frac{1}{2} d_{1}^{(M)}.
\tag{13}
$$

3.2. Thermal analysis: solution

The temperature distribution in the subcell $(\alpha \beta \gamma)$ of the $p$th cell, measured with respect to a reference temperature $T_{R}$, is denoted by $T^{(\alpha \beta \gamma)}$. We approximate this temperature field by a second-order expansion in the local coordinates $\bar{x}_{1}^{(\alpha)}, \bar{x}_{2}^{(\beta)}$, and $\bar{x}_{3}^{(\gamma)}$ as follows:

$$
\begin{aligned}
T^{(\alpha \beta \gamma)}=T_{0}^{(\alpha \beta \gamma)}+\bar{x}_{1}^{(\alpha)} T_{1}^{(\alpha \beta \gamma)}+\frac{1}{2}\left(3 \bar{x}_{1}^{(\alpha) 2}-\frac{d_{\alpha}^{(p) 2}}{4}\right) T_{2}^{(\alpha \beta \gamma)} &+\frac{1}{2}\left(3 \bar{x}_{2}^{(\beta) 2}-\frac{h_{\beta}^{2}}{4}\right) T_{3}^{(\alpha \beta \gamma)} \\
&+\frac{1}{2}\left(3 \bar{x}_{3}^{(\gamma) 2}-\frac{l_{\gamma}^{2}}{4}\right) T_{4}^{(\alpha \beta \gamma)}, \quad(14)
\end{aligned}
$$

where $T_{0}^{(\alpha \beta \gamma)}$, which is the temperature at the center of the subcell, and $T_{i}^{(\alpha \beta \gamma)}(i=1, \ldots, 4)$ are unknown coefficients which are determined from conditions that will be outlined subsequently. Henceforth, for notational simplicity and in view of the fact that the composite material is periodic in the $x_{2}-x_{3}$ plane, the designation $(p, q, r)$ for the $p$th cell will be replaced by $(p)$ whenever appropriate in this section and in the corresponding section dealing with solution to the mechanical problem.

Given the five unknown quantities associated with each subcell (i.e. $T_{0}^{(\alpha \beta \gamma)}, \ldots, T_{4}^{(\alpha \beta \gamma)}$) and eight subcells within each unit cell, $40 M$ unknown quantities must be determined for a composite with $M$ rows of fibers. These quantities are determined by first satisfying the heat conduction equation, as well as the first and second moment of this equation in each subcell in a volumetric sense in view of the temperature field approximation given by eqn (14). Subsequently, continuity of heat flux and temperature is imposed in an average sense at the interfaces separating adjacent subcells, as well as neighboring cells. Fulfillment of these field equations and continuity conditions, together with the imposed thermal boundary conditions at the top and bottom surfaces of the composite, provides the necessary $40 M$ equations for the $40 M$ unknown coefficients in the temperature field expansion. We begin the outline of steps to generate the required $40 M$ equations by first considering an arbitrary $p$th cell in the interior of the composite (i.e. $p=2, \ldots, M-1$). This produces $40(M-2)$ equations. The additional equations are obtained by considering the boundary cells (i.e. $p=1$ and $M$). For these cells, most of the preceding relations also hold, with the exception of some of the interfacial continuity conditions between adjacent cells which are replaced by the specified boundary conditions.

### 3.2.1. Heat conduction equations.
In the course of satisfying the steady-state heat equation in a volumetric sense, it is convenient to define the following flux quantities

$$
Q_{i(l, m, n)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}} \int_{-d_{\alpha}^{(p)} / 2}^{d_{\alpha}^{(p)} / 2} \int_{-h_{\beta} / 2}^{h_{\beta} / 2} \int_{-l_{\gamma} / 2}^{l_{\gamma} / 2}\left(\bar{x}_{1}^{(\alpha)}\right)^{l}\left(\bar{x}_{2}^{(\beta)}\right)^{m}\left(\bar{x}_{3}^{(\gamma)}\right)^{n} q_{i}^{(\alpha \beta \gamma)} d \bar{x}_{1}^{(\alpha)} d \bar{x}_{2}^{(\beta)} d \bar{x}_{3}^{(\gamma)},\qquad(15)
$$

where $l, m, n=0,1$, or 2 with $l+m+n \leqslant 2$, and $v_{(\alpha \beta \gamma)}^{(p)}=d_{\alpha}^{(p)} h_{\beta} l_{\gamma}$ is the volume of the subcell $(\alpha \beta \gamma)$ in the $p$ th cell. For $l=m=n=0, Q_{i(0,0,0)}^{(\alpha \beta \gamma)}$ is the average value of the heat flux component $q_{i}^{(\alpha \beta \gamma)}$ in the subcell, whereas for other values of $(l, m, n)$ eqn (15) defines higherorder heat fluxes. These flux quantities can be evaluated explicitly in terms of the coefficients $T_{l}^{(\alpha \beta \gamma)}$ by performing the required volume integration using eqns (7) and (14) in (15). This yields the following nonvanishing zeroth-order and first-order heat fluxes in terms of the unknown coefficients in the temperature field expansion

$$
Q_{1(0,0,0)}^{(\alpha \beta \gamma)}=-k_{1}^{(\alpha \beta \gamma)} T_{1}^{(\alpha \beta \gamma)}\qquad(16)
$$

$$
Q_{1(1,0,0)}^{(\alpha \beta \gamma)}=-\frac{1}{4} k_{1}^{(\alpha \beta \gamma)} d_{\alpha}^{(p) 2} T_{2}^{(\alpha \beta \gamma)}\qquad(17)
$$

$$
Q_{2(0,1,0)}^{(\alpha \beta \gamma)}=-\frac{1}{4} k_{2}^{(\alpha \beta \gamma)} h_{\beta}^{2} T_{3}^{(\alpha \beta \gamma)}\qquad(18)
$$

$$
Q_{3(0,0,1)}^{(\alpha \beta \gamma)}=-\frac{1}{4} k_{3}^{(\alpha \beta \gamma)} l_{\gamma}^{2} T_{4}^{(\alpha \beta \gamma)}.\qquad(19)
$$

Satisfaction of the zeroth, first and second moment of the steady-state heat equation results in the following eight relationships among the first-order heat fluxes $Q_{i(l, m, n)}^{(\alpha \beta \gamma)}$ in the different subcells $(\alpha \beta \gamma)$ of the $p$ th cell, after some involved algebraic manipulations (see Appendix A)

$$
\left[Q_{1(1,0,0)}^{(\alpha \beta \gamma)} / d_{\alpha}^{(p) 2}+Q_{2(0,1,0)}^{(\alpha \beta \gamma)} / h_{\beta}^{2}+Q_{3(0,0,1)}^{(\alpha \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)}=0,\qquad(20)
$$

where the triplet $(\alpha \beta \gamma)$ assumes all permutations of the integers 1 and 2.

### 3.2.2. Heat flux continuity equations.
The continuity of heat fluxes at the subcell interfaces, as well as between individual cells, associated with the $x_{1}$ (FG) direction, eqns (8a) and (9a) imposed in an average sense, is ensured by

$$
\begin{aligned}
& {\left[12 Q_{2(0,1,0)}^{(1 \beta \gamma)} / h_{\beta}^{2}+12 Q_{3(0,0,1)}^{(1 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)}+6 \frac{d_{2}^{(p)}}{d_{1}^{(p)}}\left[Q_{2(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+Q_{3(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)} } \\
& \quad+6 \frac{d_{2}^{(p-1)}}{d_{1}^{(p)}}\left[Q_{2(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+Q_{3(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p-1)}+\frac{1}{d_{1}^{(p)}}\left[\left.Q_{1(0,0,0)}^{(2 \beta \gamma)}\right|^{(p)}-\left.Q_{1(0,0,0)}^{(2 \beta \gamma)}\right|^{(p-1)}\right]=0 \quad(21)
\end{aligned}
$$

and

$$
\begin{aligned}
\left.Q_{1(0,0,0)}^{(1 \beta \gamma)}\right|^{(p)}=\left.\frac{1}{2} Q_{1(0,0,0)}^{(2 \beta \gamma)}\right|^{(p)}+ & \left.\frac{1}{2} Q_{1(0,0,0)}^{(2 \beta \gamma)}\right|^{(p-1)}+3 d_{2}^{(p)}\left[Q_{2(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+Q_{3(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)} \\
& -3 d_{2}^{(p-1)}\left[Q_{2(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+Q_{3(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p-1)} \quad(22)
\end{aligned}
$$

while the equations that ensure heat flux continuity at the subcell interfaces associated with the $x_{2}$ and $x_{3}$ directions, eqns (8b) and (8c), are given by

$$
\left[Q_{2(0,1,0)}^{(\alpha 1 \gamma)} / h_{1}+Q_{2(0,1,0)}^{(\alpha 2 \gamma)} / h_{2}\right]^{(p)}=0
$$

$$
\left[Q_{3(0,0,1)}^{(\alpha \beta 1)} / l_{1}+Q_{3(0,0,1)}^{(\alpha \beta 2)} / l_{2}\right]^{(p)}=0 \text {. }
$$

We note that eqns (9b) and (9c) are identically satisfied by the chosen temperature field representation due to the periodicity of the composite in the $x_{2}-x_{3}$ plane.

Equations (21)-(24) provide us with 16 additional relations among the zeroth-order and first-order heat fluxes. These relations, together with eqn (20), can be expressed in terms of the unknown coefficients $T_{i}^{(\alpha \beta \gamma)}(i=1, \ldots, 4)$ by making use of eqns (16)-(19), providing a total of 24 of the required 40 equations necessary for the determination of these coefficients in the $p$ th cell.

3.2.3. Thermal continuity equations. An additional set of 16 equations necessary to determine the unknown coefficients in the temperature field expansion is subsequently generated by the thermal continuity conditions imposed on an average basis at each subcell and cell interface. Imposing the thermal continuity at each subcell interface, eqns (10a-c), we obtain the following conditions for the $p$ th cell

$$
\left[T_{0}^{(1 \beta \gamma)}+d_{1}^{(p)} T_{1}^{(1 \beta \gamma)}+\frac{1}{4} d_{1}^{(p) 2} T_{2}^{(1 \beta \gamma)}\right]^{(p)}=\left[T_{0}^{(2 \beta \gamma)}-d_{2}^{(p)} T_{1}^{(2 \beta \gamma)}+\frac{1}{4} d_{2}^{(p) 2} T_{2}^{(2 \beta \gamma)}\right]^{(p)}
$$

$$
\left[T_{0}^{(\alpha 1 \gamma)}+\frac{1}{4} h_{1}^{2} T_{3}^{(\alpha 1 \gamma)}\right]^{(p)}=\left[T_{0}^{(\alpha 2 \gamma)}+\frac{1}{4} h_{2}^{2} T_{3}^{(\alpha 2 \gamma)}\right]^{(p)}
$$

$$
\left[T_{0}^{(\alpha \beta 1)}+\frac{1}{4} l_{1}^{2} T_{4}^{(\alpha \beta 1)}\right]^{(p)}=\left[T_{0}^{(\alpha \beta 2)}+\frac{1}{4} l_{2}^{2} T_{4}^{(\alpha \beta 2)}\right]^{(p)} .
$$

The continuity of temperature between neighboring cells in the FG direction, eqn (11a), on the other hand, yields

$$
\left[T_{0}^{(1 \beta \gamma)}-\frac{1}{2} d_{1}^{(p+1)} T_{1}^{(1 \beta \gamma)}+\frac{1}{4} d_{1}^{(p+1) 2} T_{2}^{(1 \beta \gamma)}\right]^{(p+1)}=\left[T_{0}^{(2 \beta \gamma)}+\frac{1}{2} d_{2}^{(p)} T_{1}^{(2 \beta \gamma)}+\frac{1}{4} d_{2}^{(p) 2} T_{2}^{(2 \beta \gamma)}\right]^{(p)} .
$$

We note that the continuity of temperature between neighboring cells in the $x_{2}$ and $x_{3}$ directions, eqns (11b) and (11c), is automatically satisfied by the chosen temperature field representation which reflects the periodic character of the composite in these directions.

3.2.4. Governing equations for the unknown coefficients in the temperature expansion.
The equilibrium equations, eqn (20), together with the heat flux and thermal continuity equations, eqns (21)-(24) and eqns (25)-(28), respectively, form altogether 40 linear algebraic equations which govern the 40 field variables $T_{i}^{(\alpha \beta \gamma)}(i=0, \ldots, 4)$ in the eight subcells $(\alpha \beta \gamma)$ of an interior cell $p ; p=2, \ldots, M-1$. For the boundary cells $p=1$ and $p=M$, a different treatment must be applied. For $p=1$, the governing equations, eqns (20), and (23)-(28), are operative. Relations (21) and (22), on the other hand, which follow

from the continuity of heat flux between a given cell and the preceding one are not applicable.
They are replaced by the condition that the heat flux at the interface between subcell $(1 \beta \gamma)$
and $(2 \beta \gamma)$ of the cell $p=1$ is continuous, as well as the applied temperature relation at the
surface $x_{1}=0$. For the cell $p=M$, the previous equations are applicable except eqns (28)
which are obviously not operative. These equations are replaced by the specific temperature
applied at the surface $x_{1}=H$.

The governing equations at the interior and boundary cells form a system of $40 M$
linear algebraic equations in the unknown coefficients $T_{i}^{(\alpha \beta \gamma)}|^{p}(i=0, \ldots, 4 ; \alpha, \beta, \gamma=1,2$;
$p=1, \ldots, M)$. Their solution determines the temperature distribution within the FG
composite subjected to the boundary conditions (12) and (13). The final form of this system
of equations is symbolically represented below

$$
\boldsymbol{\kappa} \mathbf{T}=\mathbf{t}, \tag{29}
$$

where the structural thermal conductivity matrix $\boldsymbol{\kappa}$ contains information on the geometry
and thermal conductivities of the individual subcells $(\alpha \beta \gamma)$ in the $M$ cells spanning the
thickness of the FG plate, the thermal coefficient vector $\mathbf{T}$ contains the unknown coefficients
that describe the thermal field in each subcell, i.e. $\mathbf{T}=(\mathbf{T}_{1}^{(111)}, \ldots, \mathbf{T}_{M}^{(222)})$, where $\mathbf{T}_{p}^{(\alpha \beta \gamma)}=(T_{0}$,
$T_{1}, T_{2}, T_{3}, T_{4})_{p}^{(\alpha \beta \gamma)}$, and the thermal force vector $\mathbf{t}=(T_{T}, 0, \ldots, 0, T_{B})$ contains information
on the boundary conditions.

### 3.3. Mechanical analysis: problem formulation
Given the temperature field generated by the applied temperatures $T_{T}$ and $T_{B}$ obtained
in the preceding section, we proceed to determine the resulting displacement and stress
fields. This is carried out for uniform normal (i.e. no shearing) mechanical loading applied
to the surfaces of the composite.

#### 3.3.1. Equations of equilibrium.
The stress field in the subcell $(\alpha \beta \gamma)$ of the $p$th cell
generated by the given temperature field must satisfy the equilibrium equations

$$
\partial_{1} \sigma_{1 j}^{(\alpha \beta \gamma)}+\partial_{2} \sigma_{2 j}^{(\alpha \beta \gamma)}+\partial_{3} \sigma_{3 j}^{(\alpha \beta \gamma)}=0, \quad j=1,2,3, \tag{30}
$$

where the operator $\partial_{i}$ has been defined previously. The components of the stress tensor,
assuming that the material occupying the subcell $(\alpha \beta \gamma)$ of the $p$th cell is orthotropic, are
related to the strain components through the familiar generalized Hooke's law

$$
\sigma_{i j}^{(\alpha \beta \gamma)}=c_{i j k l}^{(\alpha \beta \gamma)} \varepsilon_{k l}^{(\alpha \beta \gamma)}-\Gamma_{i j}^{(\alpha \beta \gamma)} T^{(\alpha \beta \gamma)}, \tag{31}
$$

where $c_{i j k l}^{(\alpha \beta \gamma)}$ are the elements of the stiffness tensor and the elements $\Gamma_{i j}^{(\alpha \beta \gamma)}$ of the so-called
thermal tensor are the products of the stiffness tensor and the thermal expansion coefficients.
The components of the strain tensor in the individual subcells are, in turn, obtained from
the strain-displacement relations

$$
\varepsilon_{i j}^{(\alpha \beta \gamma)}=\frac{1}{2}\left(\partial_{i} u_{j}^{(\alpha \beta \gamma)}+\partial_{j} u_{i}^{(\alpha \beta \gamma)}\right), \quad i, j=1,2,3. \tag{32}
$$

Given the relation between the stresses and displacement gradients obtained from eqns (31)
and (32), a displacement field is sought that satisfies the three equilibrium equations together
with the continuity and boundary conditions that follow.

#### 3.3.2. Traction continuity conditions.
The continuity of tractions at the interfaces
separating adjacent subcells within the repeating unit cell $(p, q, r)$ is fulfilled by requiring
that

$$
\left.\sigma_{1 i}^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=d_{1}^{(p)} / 2}=\left.\sigma_{1 i}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=-d_{2}^{(p)} / 2}
\tag{33a}
$$

$$
\left.\sigma_{2 i}^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=h_{1} / 2}=\left.\sigma_{2 i}^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=-h_{2} / 2}
\tag{33b}
$$

$$
\left.\sigma_{3 i}^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=l_{1} / 2}=\left.\sigma_{3 i}^{(\alpha \beta 2)}\right|_{\bar{x}_{3}^{(2)}=-l_{2} / 2}.
\tag{33c}
$$

In addition to the above continuity conditions within the $p$th cell, the traction continuity at the interfaces between neighboring cells must be ensured. These conditions are fulfilled by requiring that

$$
\left.\sigma_{1 i}^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=-d_{1}^{(p+1)} / 2}=\left.\sigma_{1 i}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=d_{2}^{(p)} / 2}
\tag{34a}
$$

$$
\left.\sigma_{2 i}^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=-h_{1} / 2}=\left.\sigma_{2 i}^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=h_{2} / 2}
\tag{34b}
$$

$$
\left.\sigma_{3 i}^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=-l_{1} / 2}=\left.\sigma_{3 i}^{(\alpha \beta 2)}\right|_{\bar{x}_{3}^{(2)}=l_{2} / 2}.
\tag{34c}
$$

#### 3.3.3. Displacement continuity conditions.
At the interfaces of the subcells within the repeating unit cell $(p, q, r)$ the displacements $\mathbf{u}=(u_{1}, u_{2}, u_{3})$ must be continuous

$$
\left.\mathbf{u}^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=d_{1}^{(p)} / 2}=\left.\mathbf{u}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=-d_{2}^{(p)} / 2}
\tag{35a}
$$

$$
\left.\mathbf{u}^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=h_{1} / 2}=\left.\mathbf{u}^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=-h_{2} / 2}
\tag{35b}
$$

$$
\left.\mathbf{u}^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=l_{1} / 2}=\left.\mathbf{u}^{(\alpha \beta 2)}\right|_{\bar{x}_{3}^{(2)}=-l_{2} / 2}
\tag{35c}
$$

while the continuity of displacements between neighboring cells is ensured by requiring that

$$
\left.\mathbf{u}^{(1 \beta \gamma)}\right|_{\bar{x}_{1}^{(1)}=-d_{1}^{(p+1)} / 2}=\left.\mathbf{u}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=d_{2}^{(p)} / 2}
\tag{36a}
$$

$$
\left.\mathbf{u}^{(\alpha 1 \gamma)}\right|_{\bar{x}_{2}^{(1)}=-h_{1} / 2}=\left.\mathbf{u}^{(\alpha 2 \gamma)}\right|_{\bar{x}_{2}^{(2)}=h_{2} / 2}
\tag{36b}
$$

$$
\left.\mathbf{u}^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(1)}=-l_{1} / 2}=\left.\mathbf{u}^{(\alpha \beta 1)}\right|_{\bar{x}_{3}^{(2)}=l_{2} / 2}.
\tag{36c}
$$

#### 3.3.4. Boundary conditions.
The final set of conditions that the solution for the displacement field must satisfy are the boundary conditions at the top and bottom surfaces. The normal stress in the cell $p=1$ at the top surface must equal the normal stress $f(t)$

$$
\left.\sigma_{1}^{(1 \beta \gamma)}\right|^{(1, q, r)}=f(t), \quad \bar{x}_{1}^{(1)}=-\frac{1}{2} d_{1}^{(1)}
\tag{37}
$$

with $f(t)$ describing the temporal variation of this loading, whereas in the cell $p=M$ at the bottom surface the condition that the surface $x_{1}=H$ is rigidly clamped (say) is imposed

$$
\left.u_{1}^{(2 \beta \gamma)}\right|^{(M, q, r)}=0, \quad \bar{x}_{1}^{(2)}=\frac{1}{2} d_{2}^{(M)}.
\tag{38}
$$

For other types of boundary conditions, eqn (38) should be modified accordingly.

### 3.4. Mechanical analysis: solution
Due to symmetry considerations, the displacement field in the subcell $(\alpha \beta \gamma)$ of the $p$th cell is approximated by a second-order expansion in the local coordinates $\bar{x}_{1}^{(\alpha)}$, $\bar{x}_{2}^{(\beta)}$, and $\bar{x}_{3}^{(\gamma)}$ as follows:

$$
\begin{aligned}
u_{1}^{(\alpha \beta \gamma)}= & W_{1}^{(\alpha \beta \gamma)}+\bar{x}_{1}^{(\alpha)} \phi_{1}^{(\alpha \beta \gamma)}+\frac{1}{2}\left(3 \bar{x}_{1}^{(\alpha) 2}-\frac{1}{4} d_{\alpha}^{(p) 2}\right) U_{1}^{(\alpha \beta \gamma)} \\
& +\frac{1}{2}\left(3 \bar{x}_{2}^{(\beta) 2}-\frac{1}{4} h_{\beta}^{2}\right) V_{1}^{(\alpha \beta \gamma)}+\frac{1}{2}\left(3 \bar{x}_{3}^{(\gamma) 2}-\frac{1}{4} l_{\gamma}^{2}\right) W_{1}^{(\alpha \beta \gamma)} \\
u_{2}^{(\alpha \beta \gamma)}= & \bar{x}_{2}^{(\beta)} \chi_{2}^{(\alpha \beta \gamma)} \\
u_{3}^{(\alpha \beta \gamma)}= & \bar{x}_{3}^{(\gamma)} \psi_{3}^{(\alpha \beta \gamma)},
\end{aligned}
\tag{39}
$$
```

where $w_{1}^{(\alpha \beta \gamma)}$, which are the displacements at the center of the subcell, and $U_{1}^{(\alpha \beta \gamma)}, V_{1}^{(\alpha \beta \gamma)}$, $W_{1}^{(\alpha \beta \gamma)}, \phi_{1}^{(\alpha \beta \gamma)}, \chi_{2}^{(\alpha \beta \gamma)}$, and $\psi_{3}^{(\alpha \beta \gamma)}$ must be determined from conditions similar to those employed in the thermal problem. In this case, there are $56 M$ unknown quantities. The determination of these quantities parallels that of the thermal problem. Here, the heat conduction equation is replaced by the three equilibrium equations, and the continuity of tractions and displacements at the various interfaces replaces the continuity of heat fluxes and temperature. Finally, the boundary conditions involve the appropriate mechanical quantities. As in the thermal problem, we start with the internal cells and subsequently modify the governing equations to accommodate the boundary cells $p=1$ and $M$.

3.4.1. Equations of equilibrium. In the course of satisfying the equilibrium equations in a volumetric sense, it is convenient to define the following stress quantities.

$$
S_{i j(l, m, n)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}} \int_{-d_{x}^{(p)} / 2}^{d_{x}^{(p)} / 2} \int_{-h_{\beta} / 2}^{h_{\beta} / 2} \int_{-l_{\gamma} / 2}^{l_{\gamma} / 2}\left(\bar{x}_{1}^{(\alpha)}\right)^{l}\left(\bar{x}_{2}^{(\beta)}\right)^{m}\left(\bar{x}_{3}^{(\gamma)}\right)^{n} \sigma_{i j}^{(\alpha \beta \gamma)} d \bar{x}_{1}^{(\alpha)} d \bar{x}_{2}^{(\beta)} d \bar{x}_{3}^{(\gamma)}.\qquad(40)
$$

For $l=m=n=0$, eqn (40) provides average stresses in the subcell, whereas for other values of $(l, m, n)$ higher-order stresses are obtained which are needed to describe the governing field equations of the higher-order continuum. These stress quantities can be evaluated explicitly in terms of the unknown coefficients $U_{1}^{(\alpha \beta \gamma)}, \ldots, \phi_{1}^{(\alpha \beta \gamma)}, \ldots, \psi_{3}^{(\alpha \beta \gamma)}$ by performing the required volume integration using eqns (31), (32), and (39) in eqn (40). This yields the following nonvanishing zeroth-order and first-order stress components in terms of the unknown coefficients in the displacement field expansion

$$
S_{11(0,0,0)}^{(\alpha \beta \gamma)}=c_{11}^{(\alpha \beta \gamma)} \phi_{1}^{(\alpha \beta \gamma)}+c_{12}^{(\alpha \beta \gamma)} \chi_{2}^{(\alpha \beta \gamma)}+c_{13}^{(\alpha \beta \gamma)} \psi_{3}^{(\alpha \beta \gamma)}-\Gamma_{1}^{(\alpha \beta \gamma)} T_{0}^{(\alpha \beta \gamma)}\qquad(41)
$$

$$
S_{22(0,0,0)}^{(\alpha \beta \gamma)}=c_{12}^{(\alpha \beta \gamma)} \phi_{1}^{(\alpha \beta \gamma)}+c_{22}^{(\alpha \beta \gamma)} \chi_{2}^{(\alpha \beta \gamma)}+c_{23}^{(\alpha \beta \gamma)} \psi_{3}^{(\alpha \beta \gamma)}-\Gamma_{2}^{(\alpha \beta \gamma)} T_{0}^{(\alpha \beta \gamma)}\qquad(42)
$$

$$
S_{33(0,0,0)}^{(\alpha \beta \gamma)}=c_{13}^{(\alpha \beta \gamma)} \phi_{1}^{(\alpha \beta \gamma)}+c_{23}^{(\alpha \beta \gamma)} \chi_{2}^{(\alpha \beta \gamma)}+c_{33}^{(\alpha \beta \gamma)} \psi_{3}^{(\alpha \beta \gamma)}-\Gamma_{3}^{(\alpha \beta \gamma)} T_{0}^{(\alpha \beta \gamma)}\qquad(43)
$$

$$
S_{11(1,0,0)}^{(\alpha \beta \gamma)}=\frac{1}{4} c_{11}^{(\alpha \beta \gamma)} d_{\alpha}^{(p) 2} U_{1}^{(\alpha \beta \gamma)}-\frac{1}{12} d_{\alpha}^{(p) 2} \Gamma_{1}^{(\alpha \beta \gamma)} T_{1}^{(\alpha \beta \gamma)}\qquad(44)
$$

$$
S_{12(0,1,0)}^{(\alpha \beta \gamma)}=\frac{1}{4} c_{44}^{(\alpha \beta \gamma)} h_{\beta}^{2} V_{1}^{(\alpha \beta \gamma)}\qquad(45)
$$

$$
S_{13(0,0,1)}^{(\alpha \beta \gamma)}=\frac{1}{4} c_{55}^{(\alpha \beta \gamma)} l_{\gamma}^{2} W_{1}^{(\alpha \beta \gamma)}.\qquad(46)
$$

Satisfaction of the equilibrium equations results in the following eight relations among the volume-averaged first-order stresses $S_{i j(l, m, n)}^{(\alpha \beta \gamma)}$ in the different subcells $(\alpha \beta \gamma)$ of the $p$ th cell, after lengthy algebraic manipulations (see Appendix B)

$$
\left[S_{11(1,0,0)}^{(\alpha \beta \gamma)} / d_{\alpha}^{(p) 2}+S_{12(0,1,0)}^{(\alpha \beta \gamma)} / h_{\beta}^{2}+S_{13(0,0,1)}^{(\alpha \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)}=0,\qquad(47)
$$

where, as in the case of eqn (20), the triplet $(\alpha \beta \gamma)$ assumes all permutations of the integers 1 and 2.

3.4.2. Traction continuity equations. The continuity of tractions at the subcell interfaces, as well as between individual cells, associated with the $x_{1}$ (FG) direction, eqns (33a) and (34a) imposed in an average sense, is ensured by the following relations

$$
\begin{aligned}
{\left[12 S_{12(0,1,0)}^{(1 \beta \gamma)} / h_{\beta}^{2}\right.} & \left.+12 S_{13(0,0,1)}^{(1 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)}+6 \frac{d_{2}^{(p)}}{d_{1}^{(p)}}\left[S_{12(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+S_{13(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)} \\
& +6 \frac{d_{2}^{(p-1)}}{d_{1}^{(p)}}\left[S_{12(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+S_{13(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p-1)}+\frac{1}{d_{1}^{(p)}}\left[\left.S_{11(0,0,0)}^{(2 \beta \gamma)}\right|^{(p)}-\left.S_{11(0,0,0)}^{(2 \beta \gamma)}\right|^{(p-1)}\right]=0 \quad(48)
\end{aligned}
$$

$$
\begin{aligned}
\left.S_{11(0,0,0)}^{(1 \beta \gamma)}\right|^{(p)}=\frac{1}{2}\left.S_{11(0,0,0)}^{(2 \beta \gamma)}\right|^{(p)} & +\frac{1}{2}\left.S_{11(0,0,0)}^{(2 \beta \gamma)}\right|^{(p-1)}+3 d_{2}^{(p)}\left[S_{12(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+S_{13(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p)} \\
& -3 d_{2}^{(p-1)}\left[S_{12(0,1,0)}^{(2 \beta \gamma)} / h_{\beta}^{2}+S_{13(0,0,1)}^{(2 \beta \gamma)} / l_{\gamma}^{2}\right]^{(p-1)} \quad(49)
\end{aligned}
$$

while the equations that ensure traction continuity between individual subcells associated with the $x_{2}$ and $x_{3}$ directions, eqns (33b) and (33c), are given by

$$
\left[S_{12(0,1,0)}^{(\alpha 1 \gamma)} / h_{1}+S_{12(0,1,0)}^{(\alpha 2 \gamma)} / h_{2}\right]^{(p)}=0
$$

$$
\left[S_{13(0,0,1)}^{(\alpha \beta 1)} / l_{1}+S_{13(0,0,1)}^{(\alpha \beta 2)} / l_{2}\right]^{(p)}=0
$$

$$
\left.S_{22(0,0,0)}^{(\alpha 1 \gamma)}\right|^{(p)}=\left.S_{22(0,0,0)}^{(\alpha 2 \gamma)}\right|^{(p)}
$$

$$
\left.S_{33(0,0,0)}^{(\alpha \beta 1)}\right|^{(p)}=\left.S_{33(0,0,0)}^{(\alpha \beta 2)}\right|^{(p)}.
$$

We note that eqns (34b) and (34c) are identically satisfied by the chosen displacement field representation due to the periodic character of the composite material in the $x_{2}-x_{3}$ plane.

Equations (48)-(53) provide us with 24 additional relations among the zeroth-order and first-order stresses. These relations, together with eqn (47), can be expressed in terms of the unknown coefficients $U_{1}^{(\alpha \beta \gamma)}, \ldots, \phi_{1}^{(\alpha \beta \gamma)}, \ldots, \psi_{3}^{(\alpha \beta \gamma)}$ by making use of eqns (41)-(46), providing a total of 32 of the required 56 equations necessary for the determination of these coefficients in the $p$ th cell.

3.4.3. Displacement continuity equations. The additional 24 relations necessary to determine the unknown coefficients in the displacement field expansion are subsequently obtained by imposing displacement continuity conditions on an average basis at each subcell and cell interface. The continuity of displacements at each subcell interface of the $p$ th cell, eqns (35a-c), is satisfied by the following conditions

$$
\left[w_{1}^{(1 \beta \gamma)}+\frac{1}{2} d_{1}^{(p)} \phi_{1}^{(1 \beta \gamma)}+\frac{1}{4} d_{1}^{2} U_{1}^{(1 \beta \gamma)}\right]^{(p)}=\left[w_{1}^{(2 B \gamma)}-\frac{1}{2} d_{2}^{(p)} \phi_{1}^{(2 B \gamma)}+\frac{1}{4} d_{2}^{2} U_{1}^{(2 \beta \gamma)}\right]^{(p)}
$$

$$
\left[w_{1}^{(\alpha 1 \gamma)}+\frac{1}{2} h_{1}^{2} V_{1}^{(\alpha 2 \gamma)}\right]^{(p)}=\left[w_{1}^{(\alpha 2 \gamma)}+\frac{1}{4} h_{2}^{2} V_{1}^{(\alpha 2 \gamma)}\right]^{(p)}
$$

$$
\left.h_{1} \chi_{2}^{(\alpha 1 \gamma)}\right|^{(p)}=-\left.h_{2} \chi_{2}^{(\alpha 2 \gamma)}\right|^{(p)}
$$

$$
\left[w_{1}^{(\alpha \beta 1)}+\frac{1}{4} l_{1}^{2} W_{1}^{(\alpha \beta 1)}\right]^{(p)}=\left[w_{1}^{(\alpha \beta 2)}+\frac{1}{4} l_{2}^{2} W_{1}^{(\alpha \beta 2)}\right]^{(p)}
$$

$$
\left.l_{1} \psi_{3}^{(\alpha \beta 1)}\right|^{(p)}=-\left.l_{2} \psi_{3}^{(\alpha \beta 2)}\right|^{(p)}
$$

while the continuity of displacements between neighboring cells in the FG direction, eqn (36a), requires that

$$
\left[w_{1}^{(1 \beta \gamma)}-\frac{1}{2} d_{1}^{(p+1)} \phi_{1}^{(1 \beta \gamma)}+\frac{1}{4} d_{1}^{(p+1) 2} U_{1}^{(1 \beta \gamma)}\right]^{(p+1)}=\left[w_{1}^{(2 \beta \gamma)}+\frac{1}{2} d_{2}^{(p)} \phi_{1}^{(2 \beta \gamma)}+\frac{1}{4} d_{2}^{(p) 2} U_{1}^{(2 \beta \gamma)}\right]^{(p)} .(59)
$$

The displacement continuity between neighboring cells in the $x_{2}$ and $x_{3}$ directions, eqns (36b) and (36c), is automatically satisfied by the chosen displacement field representation which reflects the periodic character of the composite in these directions.

3.4.4. Governing equations for the unknown coefficients in the displacement expansion.
The equilibrium equations, eqn (47), together with the traction and displacement continuity

equations, eqns (48)-(53) and eqns (54)-(59), respectively, form altogether 56 equations in the 56 unknowns $w_{1}^{(\alpha \beta \gamma)}, \phi_{1}^{(\alpha \beta \gamma)}, U_{1}^{(\alpha \beta \gamma)}, V_{1}^{(\alpha \beta \gamma)}, W_{1}^{(\alpha \beta \gamma)}, \chi_{2}^{(\alpha \beta \gamma)}, \psi_{3}^{(\alpha \beta \gamma)}$, which govern the equilibrium of a subcell $(\alpha \beta \gamma)$ within the $p$th cell in the interior. As in the thermal problem, a different treatment must be adopted for the boundary cells $p=1$ and $p=M$. For $p=1$, eqns (47), (50)-(53), and the displacement continuity relations, eqns (54)-(59), are operative, whereas eqns (48) and (49), which follow from the continuity of tractions between a given cell and the preceeding one, are not applicable. These eight equations must be replaced by the conditions of continuity of tractions at the interior interfaces of the cell $p=1$ and by the applied normal stress at $x_{1}=0$, eqn (37). For the cell $p=M$, the previously derived governing equations are operative except for the four relations given by eqns (59) which are obviously not applicable. These are replaced by the condition that the surface $x_{1}=H$ is rigidly clamped, eqn (38). Consequently, the governing equations at both interior and boundary cells form a system of $56 M$ linear algebraic equations in the field variables of the cells along $0 \leqslant x_{1} \leqslant H$. The final form of this system of equations is symbolically represented below

$$\mathbf{K U}=\mathbf{f},\tag{60}$$

where the structural stiffness matrix $\mathbf{K}$ contains information on the geometry and thermo-mechanical properties of the individual subcells $(\alpha \beta \gamma)$ in the $M$ cells spanning the thickness of the FG plate, the displacement coefficient vector $\mathbf{U}$ contains the unknown coefficients that describe the displacement field in each subcell, i.e. $\mathbf{U}=\left(\mathbf{U}_{1}^{(111)}, \ldots, \mathbf{U}_{M}^{(222)}\right)$, where $\mathbf{U}_{p}^{(\alpha \beta \gamma)}=\left(w_{1}, \phi_{1}, U_{1}, V_{1}, W_{1}, \chi_{2}, \psi_{3}\right)_{p}^{(\alpha \beta \gamma)}$, and the mechanical force vector $\mathbf{f}$ contains information on the boundary conditions and the thermal loading effects generated by the applied temperature.

## 4. APPLICATIONS

The approach outlined in the foregoing is employed to investigate the response of thin-walled composites subjected to a thermal gradient in the thickness direction. The investigated composites are reinforced with continuous SiC fibers embedded in a titanium aluminide matrix, with the fiber volume fraction, $v_{f}$, equal to 0.4. The temperature $T_{T}$ at the top surface of the composite $(x_{1}=0)$ is $0^{\circ} \mathrm{C}$ while the temperature $T_{B}$ at the bottom surface $(x_{1}=H)$ is $500^{\circ} \mathrm{C}$. The composite is constrained from deforming due to the applied thermal loading by imposing zero displacement at the bottom surface. At the top surface, the normal traction component is required to vanish (i.e. $\sigma_{11}=0$).

The properties of the fiber and matrix phases are provided in Table 1. We note that these properties are assumed to be independent of temperature. Although this may be a reasonably good approximation for the SiC fiber, the titanium matrix properties will change with temperature in the range of the imposed thermal gradient across the plate's thickness. This temperature dependence will also be accompanied by viscoplastic effects that are not considered here. These effects will be considered elsewhere. We also note that the thermal conductivity of the SiC fiber employed here is 50 times that of the matrix, which provides a large mismatch between the fiber and matrix conductivities. Additional results illustrating the effect of varying the thermal conductivity mismatch on the thermal and stress fields have been reported by Aboudi *et al.* (1993) in view of the lack of accurate knowledge of the thermal conductivity for the SiC fiber.

<table>
<caption>Table 1. Material properties of SCS6 SiC fiber and titanium matrix</caption>
<thead>
<tr>
<th>Material</th>
<th>$E$ (GPa)</th>
<th>$v$</th>
<th>$\alpha$ ($10^{-6}$ m/m$^\circ$C)</th>
<th>$\kappa$ (W/m $^\circ$C)</th>
</tr>
</thead>
<tbody>
<tr>
<td>SiC fiber</td>
<td>414.0</td>
<td>0.3</td>
<td>4.9</td>
<td>400.0</td>
</tr>
<tr>
<td>Ti-Al matrix</td>
<td>100.0</td>
<td>0.3</td>
<td>9.6</td>
<td>8.0</td>
</tr>
</tbody>
</table>

$E$ and $v$ denote the Young's modulus and Poisson's ratio, respectively; $\alpha$ is the coefficient of thermal expansion and $\kappa$ is the thermal conductivity.

<table>
<caption>Table 2. Material properties of the SCS6 SiC/Ti composite (\(v_f = 0.40\))</caption>
<tbody><tr>
<td>\(E_A^*\) (GPa)</td>
<td>226.0</td>
</tr>
<tr>
<td>\(v_A^*\)</td>
<td>0.30</td>
</tr>
<tr>
<td>\(E_T^*\) (GPa)</td>
<td>167.0</td>
</tr>
<tr>
<td>\(G_A^*\) (GPa)</td>
<td>60.9</td>
</tr>
<tr>
<td>\(\alpha_A^*\) (\(10^{-6}\) m/m/°C)</td>
<td>6.15</td>
</tr>
<tr>
<td>\(\alpha_T^*\) (\(10^{-6}\) m/m/°C)</td>
<td>7.90</td>
</tr>
<tr>
<td>\(\kappa_A^*\) (W/m °C)</td>
<td>164.80</td>
</tr>
<tr>
<td>\(\kappa_T^*\) (W/m °C)</td>
<td>16.20</td>
</tr>
</tbody>
</table>

Subscripts \(A\) and \(T\) denote axial and transverse quantities, respectively.

As a first step, unidirectional composites with fibers uniformly spaced in the thickness direction and oriented in the \(x_3\) direction are considered. Results for temperature distributions, stresses and in-plane force and moment resultants generated with the present approach that explicitly couples local micromechanical and global structural effects are compared with predictions based on the continuum approach in which local and global effects are decoupled. The continuum results are obtained by first generating the effective properties of the individual rows of fibers along the \(x_2\) coordinate, or "plies", using the generalized method of cells without regard to whether a representative volume exists or not. That is, these effective properties are generated on the premise that no coupling exists between local and global responses. This is the standard approach currently employed by researchers working in the area of micromechanics. These effective properties, shown in Table 2, are subsequently used in the thermal boundary-value problem of a homogeneous composite with appropriate effective properties subjected to the specified thermal loading. In addition, bidirectionally reinforced composites with uniform fiber spacing in the FG direction are also considered, with fibers oriented along the \(x_3\) axis in some layers and along the \(x_2\) axis in others. Again, comparison with the results of continuum approach is given, using cross-ply laminates subjected to the imposed thermal gradient. The solution to the thermal boundary-value problem of unidirectional and bidirectional laminates based on the continuum approach is briefly outlined in Section 4.1. We note that the continuum approach yields results that, for the considered geometry and applied boundary conditions, are identical to those that would be obtained using the classical lamination theory [see, for example, Christensen (1979)]. Thus, we employ the familiar terminology used in the classical lamination theory in developing the pertinent solution based on the continuum approach in Section 4.1.

Finally, application to functionally graded composites (or those with a tailored mesostructure) is illustrated by considering unidirectional composites with nonuniformly spaced fibers in the FG direction. Only continuous fiber configurations are considered with fibers oriented along the \(x_3\) coordinate. Data generated for linear, quadratic and cubic variation in the fiber spacing are compared with results obtained for configurations with uniformly spaced fibers occupying the same total volume of the composite.

### 4.1. Continuum approach (classical lamination approach)
Consider a laminate composed of \(M\) plies subjected to a thermal gradient by the imposition of the temperature \(T_T\) on the top surface and \(T_B\) on the bottom surface. The total thickness of the laminate is \(H\) with \(t_i\) representing the thickness of individual plies. Let \(h_0 = -H/2\) designate the coordinate of the top surface of the first ply measured from the mid-plane of the laminate denoted by \(z = 0\). The top surface of the \(i\)th ply is thus given by \(h_i = h_{i-1} + t_i\) for \(i = 1, 2, \dots, M\). The solution of the Laplace's equation for the given geometry subjected to the specified boundary conditions yields a linear temperature distribution in each ply. Letting \(T_1 = T_T\), the temperature at the interfaces of the laminate can be shown to be

$$
T_{i+1}=T_{i}+\Delta T_{i}, \quad i=1,2, \ldots, M \tag{61}
$$

where

$$
\Delta T_{i}=\frac{t_{i}}{\kappa_{i}} \frac{T_{B}-T_{T}}{\sum_{j=1}^{M} \frac{t_{j}}{\kappa_{j}}}. \qquad(62)
$$

We note that in our case, $\kappa_{i}$ are the effective transverse conductivities $\kappa_{T}^{*}$ of the $i$ th ply calculated using the method of cells (see Table 2). Also, $T_{T}=500^{\circ} \mathrm{C}$ and $T_{B}=0^{\circ} \mathrm{C}$, and $t_{i}=199 \mu \mathrm{m}$.

Given the temperature distribution throughout the laminate, the in-plane stress distributions in the $i$ th lamina in the absence of mid-plane strains and curvatures (which is the situation here for the specified boundary constraints) are simply calculated in the following manner

$$
\sigma_{x y}^{(i)}=\overline{\mathbf{Q}}^{(i)} \boldsymbol{\alpha}_{x y}^{(i)} T(z) \qquad(63)
$$

where $\overline{\mathbf{Q}}^{(i)}$ and $\boldsymbol{\alpha}_{x y}^{(i)}$ are the transformed reduced stiffness matrix and the thermal expansion coefficient vector, respectively, of the $i$ th ply referred to the laminate coordinate system $x$ - $y$.

The resulting in-plane force and moment resultants can be obtained by multiplying by $-1$ the so-called thermal in-plane force and moment resultants defined as follows:

$$
\mathbf{N}^{T}=\int_{-H / 2}^{+H / 2} \overline{\mathbf{Q}} \boldsymbol{\alpha}_{x y} T(z) \mathrm{d} z \qquad(64)
$$

$$
\mathbf{M}^{T}=\int_{-H / 2}^{+H / 2} \overline{\mathbf{Q}} \boldsymbol{\alpha}_{x y} T(z) z \mathrm{~d} z, \qquad(65)
$$

where the previously defined $\overline{\mathbf{Q}}$ and $\boldsymbol{\alpha}_{x y}$ are piecewise uniform throughout the laminate, and the superscript $(i)$ that associates these quantities with the $i$ th ply has been omitted for obvious reasons. Substitution of the linear temperature variation into eqns (64) and (65) and performing the necessary integration yields the following explicit expressions for $\mathbf{N}^{T}$ and $\mathbf{M}^{T}$ in terms of the previously defined quantities

$$
\mathbf{N}^{T}=\sum_{i=1}^{M} \overline{\mathbf{Q}}^{(i)} \boldsymbol{\alpha}_{x y}^{(i)}\left[T_{i}\left(h_{i}-h_{i-1}\right)+\frac{1}{2} \frac{\Delta T_{i}}{t_{i}}\left(h_{i}^{2}-h_{i-1}^{2}\right)-\frac{\Delta T_{i}}{t_{i}}\left[h_{i-1}\left(h_{i}-h_{i-1}\right)\right]\right] \qquad(66)
$$

$$
\mathbf{M}^{T}=\sum_{i=1}^{M} \overline{\mathbf{Q}}^{(i)} \boldsymbol{\alpha}_{x y}^{(i)}\left[\frac{1}{2} T_{i}\left(h_{i}^{2}-h_{i-1}^{2}\right)+\frac{1}{3} \frac{\Delta T_{i}}{t_{i}}\left(h_{i}^{3}-h_{i-1}^{3}\right)-\frac{1}{2} \frac{\Delta T_{i}}{t_{i}} h_{i-1}\left(h_{i}^{2}-h_{i-1}^{2}\right)\right]. \quad(67)
$$

### 4.2. Response of composites with uniform mesostructure
Here, the response of unidirectional and bidirectional composites with uniformly spaced fibers is investigated. The results are useful in answering the fundamental question of the validity of the classical homogenization scheme in the presence of thermal gradients and finite boundary effects. Just as importantly, the results give useful estimates on the number of fibers that are required in the thickness direction to produce data that can be reliably generated with the standard approach wherein the micromechanics and macro- mechanics analyses are decoupled (which clearly is less expensive than the present scheme).

#### 4.2.1. Unidirectional composites.
Consider the response of a continuously reinforced unidirectional composite having a fixed thickness of $199 \mu \mathrm{m}$ with fibers oriented in the $x_{3}$ direction. This thickness is based on a single ply of a SiC/Ti composite with $40 \%$ fiber volume and a fiber diameter of $142 \mu \mathrm{m}$. The objective is to determine the number of fibers in the thickness direction that are required for the results to approach those obtained using the standard homogenization procedure. To this end, we consider configurations with $M$

number of fibers, where $M = 1, 2, 3, 5, 8, 12, 16$, and 20. The volume of fibers occupying the total volume of the composite, i.e. the fiber volume fraction, is fixed at 0.40 for all the considered cases. Since the thickness of the composite is held constant, the size of the fibers must decrease when the number of fibers, $M$, is increased. However, since the problem is linear, the above is *equivalent* to increasing the number of fibers in the thickness direction by adding more layers in this direction, and thus increasing the thickness of the plate. For this reason the various distributions in the thickness direction are given as a function of the normalized coordinate $x_1/M$.

The results generated for such a large number of configurations provide a comprehensive library that can be used in future work to verify the applicability of various schemes in analyzing the thermal response of composites with tailored or coarse microstructures. The results also provide a continuous spectrum whose limiting behavior can be used as a basis for verification of the developed scheme. A more quantitative verification of the developed model based on the finite-element analysis of a finite thickness composite plate with a finite number of through-the-thickness fibers will be provided elsewhere. Further, these results demonstrate the power of the developed analytical model, in that a researcher can efficiently generate results by merely changing a few lines in the input data file of a computer code each time a new configuration is investigated. Due to space limitations, only selected results will be presented herein. The complete set can be found in Aboudi *et al.* (1993).

First, temperature distributions are presented for two selected configurations with $M = 2$ and $M = 20$. Figure 4 illustrates the temperature distributions in the representative cross-section (RCS) along the $x_1$ direction that includes both matrix and fiber phases (see

![](./images/812414452212170753_4.jpg)

Fig. 2). Included in the figures are the linear distributions (denoted by dashed lines) obtained from the homogenized thermal boundary-value problem based on the continuum equations. In the RCS containing both phases, the temperature profiles exhibit "staircase" patterns, with the temperature gradient in the fiber phase being much smaller than the gradient in the matrix phase. This is expected since the thermal conductivity of the SiC fiber is much higher than that of the Ti-Al matrix (see Table 1). The staircase patterns intersect the linear distributions at $M+1$ locations, as the step size decreases with increasing number of fibers $(M)$ in the thickness direction. Alternatively, the temperature profiles in the RCS containing only matrix (not shown) do not exhibit such a staircase pattern. These profiles exhibit smoother deviations from the linear distributions (see Aboudi et al., 1993). Examination of the complete set of results reveals that the temperature profiles generated using the standard homogenization approach are not reliable for $M \leqslant 8$ for the RCS that contains both phases, as well as for the RCS that contains matrix only.

Figures 5 and 6 illustrate the corresponding normal stress profiles, $\sigma_{22}$ and $\sigma_{33}$, in the RCS containing both fiber and matrix phases. As in the preceding cases, the linear normal stress distributions in the two directions generated with the standard homogenization approach (denoted by dashed lines) are included for comparison. The profiles generated with the present model are radically different from the profiles obtained with the standard homogenization approach for small values of $M$ for both RCSs. In the case of the RCS containing both phases, the stress profiles exhibit characteristic patterns, with substantially smaller gradients in the fiber phase than in the matrix phase, as suggested by the corresponding temperature profiles in Fig. 4. Examination of the complete set of results reveals that when $M$ is small, the stress profiles predicted by the present model are lower, i.e.

![](./images/812414452212170753_5.jpg)

Fig. 5. Through-the-thickness normal stress $\sigma_{22}$ in a unidirectional composite with uniformly spaced fibers in the cross-section containing both phases : (a) $M=2$; (b) $M=20$.

![](./images/812414452212170753_6.jpg)

Fig. 6. Through-the-thickness normal stress $\sigma_{33}$ in a unidirectional composite with uniformly spaced fibers in the cross-section containing both phases: (a) $M=2$; (b) $M=20$.

conservative, than those obtained using the standard homogenization approach. As $M$ increases, the normal stress distributions begin to oscillate around the linear or "mean" distribution predicted by the standard homogenization analysis. A clear pattern of oscil- lations emerges when $M$ is about 5. As $M$ increases beyond 5, the oscillations take on a characteristic pattern, forming a "fan" whose envelope grows with increasing distance from the top surface along the $x_{1}$ axis, with the actual gradients in the fiber and matrix phases being preserved. The stress magnitudes in the fiber phase are now greater than the mean distribution, and thus nonconservative, while in the matrix phase they are lower and thus conservative. These oscillations are a direct result of the mismatch in the Young's moduli of the fiber and matrix phases. It is interesting to note that the envelope of the normal stress $\sigma_{22}$ grows at a significantly smaller rate with $x_{1}$ than the envelope of the normal stress $\sigma_{33}$. This is clearly rooted in the microstructure of the composite which has preferred orientation along the $x_{3}$ axis. In other words, the normal stress carried by the individual fibers in the $x_{3}$ direction, that is required to maintain the composite flat in the presence of the thermal gradient, is significantly greater than the stress carried by the fibers in the $x_{2}$ direction. This is due to the fibers being continuous along the $x_{3}$ coordinate and discontinuous along the $x_{2}$ coordinate. In contrast, the differences in the normal stress distributions in the $x_{2}$ and $x_{3}$ directions predicted by the continuum calculations are significantly smaller than the differences predicted by the present model. Clearly, the continuum approach is insensitive to the actual microstructure of the material in the presence of large fiber diameter, finite boundaries, and thermal gradient.

In the case of the matrix only RCS (not shown), clear pattern for both normal stress distributions also emerges when $M$ is about 5. In this case however, the situation is reversed,

with the normal stress $\sigma_{22}$ exhibiting greater oscillations than $\sigma_{33}$. Further, while the average behavior of the normal stress $\sigma_{22}$ tends to the distribution predicted by the continuum model, the average behavior of $\sigma_{33}$ is below that of the linear distribution obtained from the continuum model. The oscillations observed in the $\sigma_{22}$ stress profiles are nonconservative in the matrix subcell adjacent to a fiber subcell in the $x_{2}-x_{3}$ plane, and conservative in the matrix subcell adjacent to another matrix subcell in the same plane, as required by the continuity of tractions between adjacent subcells. In contrast, the oscillations observed in the $\sigma_{33}$ stress profiles are conservative everywhere.

Finally, Figs 7 and 8 illustrate the normalized in-plane force and moment resultants in the $x_{2}$ and $x_{3}$ directions, as a function of the number of fibers, $M$, in the thickness direction, that result from the normal stress distributions in all the investigated configurations ($M = 1$, 2, 3, 5, 8, 12, 16, and 20). Normalization is carried out with respect to the corresponding continuum approach predictions. The in-plane force resultants $N_{2}$ and $N_{3}$ shown in Fig. 7 exhibit virtually identical behavior as a function of $M$, and asymptotically approach the predictions of the continuum model from below for increasing values of $M$. The continuum results thus provide a conservative estimate of the actual in-plane resultant forces that are required to maintain the various composite configurations in place, for the applied loading and boundary conditions. A major conclusion obtained from these figures is that the continuum approach does not produce reliable magnitudes of the inplane force resultants for $M$ less than about 10. However, since the predictions are conservative with respect to the macroscopic quantities, any design based on these quantities should be safe, albeit inefficient. In contrast to the identical asymptotic behavior exhibited by the in-plane force resultants, the inplane moment resultants $M_{2}$ and $M_{3}$ presented in Fig. 8 approach the continuum model predictions at different rates for increasing $M$, with $M_{2}$ approaching the

![](./images/812414452212170753_7.jpg)

Fig. 7. In-plane force resultants in a unidirectional composite with uniformly spaced fibers in the thickness direction (normalized with respect to the lamination theory prediction): (a) $N_{2}$; (b) $N_{3}$.

![](./images/812414452212170753_8.jpg)

Fig. 8. In-plane moment resultants in a unidirectional composite with uniformly spaced fibers in the thickness direction (normalized with respect to the lamination theory prediction): (a) $M_2$; (b) $M_3$.

continuum model results faster than $M_3$. In both cases, the asymptotic behavior is faster than for the in-plane force resultants. A major conclusion once again is that the continuum approach does not produce reliable magnitudes of the moment resultants for $M$ less than about 8. However, as in the preceding case, the predictions are conservative.

4.2.2. Bi-directional composites. Consider next the response of a continuously reinforced bidirectional composite with fibers oriented in both the $x_3$ and $x_2$ directions. The composite is constructed by starting with a ply having fibers oriented in the $x_3$ direction, followed by a ply with fibers along the $x_2$ direction, which in the terminology of the lamination theory is called an alternating $90^\circ/0^\circ$ laminate. This sequence is repeated as many times as desired. The thickness of each ply in this case is $199\ \mu\text{m}$ with the fiber volume fraction of 0.40 as before. Since the ply thickness is now kept constant but the number of alternating $90^\circ$ and $0^\circ$ plies is allowed to increase, the total composite thickness increases. However, since the problem is linear, this is equivalent to keeping the ply thickness constant but decreasing the fiber diameter while maintaining a constant fiber volume fraction. Therefore, although the various distributions in the thickness direction are now given as a function of the coordinate $x_1$, they can be directly compared with those of the unidirectional configurations. As before, the objective is to determine the number of fibers in the thickness direction that are required for the results to approach those obtained using the standard homogenization procedure. In view of the well-established trends for the unidirectional configurations outlined in the foregoing, we limit the discussion to bidirectional configurations containing 20 rows of fibers.

Following the previously established order of presentation of the results, we start with the discussion of the temperature distributions for the investigated configurations. The

![](./images/812414452212170753_9.jpg)

Fig. 9. Through-the-thickness normal stress $\sigma_{22}$ in a bidirectional composite with uniformly spaced fibers in the cross-section containing both phases for $M=20$.

distributions in the RCS containing both fiber and matrix phases exhibit the same charac- teristic staircase pattern seen previously in the unidirectional configurations, with the step size decreasing with increasing $M$. As expected, the temperature distributions predicted by the continuum model are the same as those for the unidirectional cases because the trans- verse conductivity in the $x_{1}$ direction is the same for both the $0^{\circ}$ and $90^{\circ}$ configurations. The temperature distributions obtained using the present approach are also the same as those obtained for the unidirectional configurations. This is a somewhat unexpected result in view of the different conductivities of the fiber and matrix phases, and the different microstructural details in the $x_{1}$ direction observed in the unidirectional and bidirectional configurations. It is not clear at this time why the present model predicts identical tem- perature distributions for the two different configurations.

The normal stress distributions $\sigma_{22}$ and $\sigma_{33}$, in the RCS containing both phases, are presented in Figs 9 and 10, respectively. Due to the presence of alternating $0^{\circ}$ and $90^{\circ}$ layers, the envelopes of these distributions grow with increasing distance along the $x_{1}$ direction at approximately the same rate. This is in contrast with the normal distributions observed in the unidirectional configurations where the $\sigma_{33}$ stress component grew faster than the $\sigma_{22}$ stress component. We note that although the normal stresses in the fiber phase increased monotonically along the $x_{1}$ axis in the unidirectional configurations, this is not the case for the bidirectional configurations. In fact, here the normal stresses increase at two different rates depending on whether the fiber associated with the $90^{\circ}$ or $0^{\circ}$ layer is considered. Consequently, the pattern that is observed for the considered RCS in the bidirectional

![](./images/812414452212170753_10.jpg)

Fig. 10. Through-the-thickness normal stress $\sigma_{33}$ in a bidirectional composite with uniformly spaced fibers in the cross-section containing both phases for $M=20$.

configurations is bimodal, thereby giving the appearance of nonuniformity for small values of $M$. Alternatively, when $M=20$, the full pattern emerges from which the growth of the two normal stresses ($\sigma_{22}$ and $\sigma_{33}$) at two different rates can be easily discerned. The distribution of the normal stresses predicted by the present model follows the results of the continuum approach in an average sense.

Figures 11 and 12 show the in-plane force and moment resultants obtained from the normal stress distributions presented in Figs 9 and 10. As in the case of unidirectional configurations, these quantities have been normalized with respect to the lamination theory predictions and plotted as a function of the number of layers, $M$, in the thickness direction. The trends observed for the behavior of the in-plane force and moment resultants for the bidirectional configurations generally follow the same pattern as in the preceding cases. However, a characteristic difference in the behavior of the in-plane moment resultants is observed. Whereas for the unidirectional configurations, the inplane moment resultants approached the lamination theory predictions in a uniformly asymptotic manner, the asymptotic behavior for the bidirectional configurations is not uniform. This is particularly true for small values of $M$ where the initially rapid increase of $M_2$ and $M_3$ is followed by a pattern of alternating slow and rapid growth rates, resembling a staircase pattern.

### 4.3. Response of composites with tailored mesostructure
In the final set of examples, we investigate the response of unidirectional composites with nonuniformly spaced fibers to thermal gradients. Three fiber spacing variations in the FG direction are considered, namely linear, quadratic and cubic. The total thickness of the composite is kept fixed and the total fiber volume fraction of the composite is 0.40 as in the

![](./images/812414452212170753_11.jpg)

Fig. 11. In-plane force resultants in a bidirectional composite with uniformly spaced fibers in the thickness direction (normalized with respect to the lamination theory prediction): (a) $N_2$; (b) $N_3$.

![](./images/812414452212170753_12.jpg)

Fig. 12. In-plane moment resultants in a bidirectional composite with uniformly spaced fibers
in the thickness direction (normalized with respect to the lamination theory prediction): (a) $M_{2}$;
(b) $M_{3}$.

preceding unidirectional composites with uniformly spaced fibers. The $p$th cell dimension,
$D_{p}$, in the FG direction which determines the fiber spacing for the three variations was
obtained from the following formulas:

linear fiber spacing

$$
D_{p}=A(p-1)+B \tag{68}
$$

quadratic fiber spacing

$$
D_{p}=A(p-1)^{2}+B \tag{69}
$$

cubic fiber spacing

$$
D_{p}=A(p-1)^{3}+B, \tag{70}
$$

where $p=1,2, \ldots, M$, $B$ is a pre-assigned constant, and $A$ governs the rate of increase of
the cell FG dimension. Let $M$ be the number of fibers in the FG composite as before. The
total thickness of the composite

$$
H = \sum_{p=1}^{M} D_{p}
$$

is then calculated from the following formulas:

**linear fiber spacing**
$$
H=A \frac{\left(M^{2}-M\right)}{2}+M B \tag{71}
$$

**quadratic fiber spacing**
$$
H=A\left[\frac{M}{6}(M+1)(2 M+1)-M^{2}\right]+M B \tag{72}
$$

**cubic fiber spacing**
$$
H=A\left[\frac{(1+M)^{2} M^{2}}{4}-M^{3}\right]+M B. \tag{73}
$$

The following results have been generated for the case when $M=10$, $B=199\ \mu\text{m}$, and $H=20B$. Given these values, one can determine $A$ directly, and since the total fiber volume fraction in the FG composite is given by
$$
v_{f}=\frac{M d_{1}^{(p) 2}}{H\left(h_{1}+h_{2}\right)} \tag{74}
$$
the parameters $d_{1}^{(p)}=h_{1}$, $d_{2}^{(p)}=D_{p}-d_{1}^{(p)}$, and $h_{2}=D_{1}-d_{1}^{(p)}$ are determined for all values of $p$.

The temperature distributions for the three nonuniformly spaced configurations, as well as the uniformly spaced reference configuration, are illustrated in Fig. 13. In all

![](./images/812414452212170753_13.jpg)

![](./images/812414452212170753_14.jpg)

Fig. 13. Through-the-thickness temperature distribution in a unidirectional composite with linearly, quadratically, and cubically spaced fibers. Comparison with uniformly spaced fiber composite.

nonuniformly spaced cases the temperature profiles are below that generated with uniformly spaced fibers. The linear fiber spacing variation produced the smallest deviation from the temperature profile obtained with uniformly spaced fibers, followed by the quadratic and then cubic fiber spacing variations.

The associated normal stress distributions $\sigma_{22}$ and $\sigma_{33}$ produced by the resulting temperature distributions for the cubic spacing are given in Fig. 14. These stress distributions are explicitly compared with the distribution obtained for the configuration with uniformly spaced fibers. As expected, those configurations that have been tailored to give lower temperature distributions necessarily produce lower stress distributions when compared to the stress distribution in the presence of uniform fiber spacing. Consequently, the greatest reduction in the normal stress distributions occurs for the cubic fiber spacing variation, followed by the quadratic and linear variations (not shown).

The resulting in-plane force and moment resultants for the three fiber spacing configurations are illustrated in Fig. 15 in bar chart form. The actual magnitudes have been normalized by the corresponding quantities obtained for the uniformly spaced fiber configuration. The results, as expected given Fig. 14, indicate that the greatest reductions in the presence of nonuniformly spaced fiber configurations occur for the cubic variation, followed by the quadratic and linear. Of the two sets of resultants, the in-plane force resultants exhibit the greatest relative reductions.

The last example discussed herein is the effect of reversing the temperature gradient on the temperature and stress distributions in the presence of nonuniformly spaced fibers. Again, the three configurations, i.e. linear, quadratic and cubic fiber spacings, discussed previously are considered, however now the top surface $(x_{1}=0)$ is exposed to the elevated

![](./images/812414452212170753_15.jpg)

Fig. 14. Through-the-thickness normal stress distributions in a unidirectional composite with cubically spaced fibers: (a) $\sigma_{22}$; (b) $\sigma_{33}$. Comparison with uniformly spaced fiber composite.

![](./images/812414452212170753_16.jpg)

Fig. 15. In-plane force and moment resultants in unidirectional composites with linearly, quad-
ratically and cubically spaced fibers, normalized with respect to the corresponding quantities in
uniformly spaced fiber composites.

temperature of $500^{\circ} C$ and the bottom surface $(x_{1}=H)$ maintained at $0^{\circ} C$. In practical
terms for instance, this situation may arise in aircraft applications involving frictional
heating of the wing skin during flight which, in turn, requires active internal cooling, causing
the given temperature gradient. In light of the preceding results, only the results for the
cubic fiber spacing case are presented.

The temperature distribution for the cubic fiber spacing variation and reference uniform
spacing is presented in Fig. 16. In contrast with the preceding case, the temperature
distribution is now higher than the distribution generated with uniformly spaced fibers, as
one would expect since the effective thermal conductivity in the elevated temperature zone
is higher. In fact, the temperature distribution with the reversed thermal gradient is the
mirror image of the distribution with the original thermal gradient. The results presented
in Fig. 16 suggest that the magnitudes of the normal stress distributions $\sigma_{22}$ and $\sigma_{33}$ will
now be greater than the corresponding magnitudes obtained for uniformly spaced fibers.
This is indeed the case as seen in Figs 17 and 18. Clearly, these normal stress distributions
will generate in-plane stress and moment resultants that will be higher than the resultants

![](./images/812414452212170753_17.jpg)

Fig. 16. Effect of reversing the direction of imposed thermal gradient on the temperature distribution in a unidirectional composite with cubically spaced fibers. Comparison with uniformly spaced fiber composite.

obtained from the uniformly spaced fiber configuration. Therefore, in order to reduce these quantities with respect to the reference quantities in the presence of uniform fiber spacing, the reversal of the thermal gradient should be accompanied by the reversal of the fiber spacing gradient.

## 5. CONCLUSIONS
A new approach has been presented for analyzing the response of thin-walled, metal matrix composites subjected to a thermal gradient, with a finite number of large-diameter fibers uniformly or nonuniformly spaced in the thickness direction. In this approach, the microstructural and macrostructural details are explicitly coupled when solving the thermomechanical boundary-value problem. This is in stark contrast to the standard micro- mechanical schemes, based on the classical homogenization procedures, which treat the local (micromechanics) and global (macromechanics) problems separately. Coupling of the local and global analyses allows one to accurately analyze the response of metal matrix composites such as SiC/TiAl that contain relatively few through-the-thickness fibers, as

![](./images/812414452212170753_18.jpg)

Fig. 17. Effect of reversing the direction of imposed thermal gradient on the normal stress $\sigma_{22}$ distribution in a unidirectional composite with cubically spaced fibers. Comparison with uniformly spaced fiber composite.

![](./images/812414452212170753_19.jpg)

Fig. 18. Effect of reversing the direction of imposed thermal gradient on the normal stress $\sigma_{33}$ distribution in a unidirectional composite with cubically spaced fibers. Comparison with uniformly spaced fiber composite.

well as so-called functionally gradient composites with continuously changing properties due to nonuniform fiber spacing or the presence of several phases. In such composites, it is difficult, if not impossible, to define the representative volume element (RVE) used in the traditional micromechanical analyses.

The numerical examples presented herein indicate that the standard homogenization procedure based on the premise of a RVE yields inaccurate results for thin-walled composites with a small number of large-diameter fibers in the thickness direction. In particular, the inplane force and moment resultants obtained using the standard homogenization approach, that are necessary to maintain the composite flat in the presence of a through-the-thickness thermal gradient, are significantly overpredicted (i.e. conservative) for fewer than about 10 fibers when the mismatch in the thermal conductivities of the fiber and matrix phases is large. For a larger number of through-the-thickness fibers, the results of the present model asymptotically approach those of the standard homogenization scheme. The local stresses, on the other hand, only converge to the classical homogenized stresses *in an average sense* with increasing number of through-the-thickness fibers, and can exhibit large nonconservative local fluctuations depending on the microstructural details of the composite (and the mismatch in the thermal and material properties). As demonstrated by Aboudi *et al.* (1993), an estimate of the local stresses can be obtained from the continuum approach by applying an average temperature over a given volume containing both the fiber and matrix phases, and solving the associated micromechanics problem, treating the given volume as an RVE. Such a "primitive" micromechanics approach must be employed with caution since it may underestimate the local stresses in the presence of stress gradients at the micromechanical level. The accuracy of this approach increases with increasing number of through-the-thickness fiber, and may be acceptable when the number of fibers is greater than ten. These observations suggest that the use of the effective modulus concept must be approached with caution when analyzing the thermal response of composites with relatively few, large-diameter fibers in the thickness direction in the presence of thermal gradients.

The results obtained for composites with tailored mesostructures, i.e. nonuniformly spaced fibers in the through-the-thickness direction, indicate that it is possible to reduce the temperature distribution, and thus obtain more favorable stress distributions, by appropriately grading the microstructure of the composite. This, in turn, reduces the inplane force and moment resultants, necessary to maintain the composite flat in the presence of a thermal gradient, with respect to the corresponding quantities that arise in composites with uniformly spaced fibers. The manner in which the microstructure of the composite is graded must take into account the sign of the thermal gradient. Consequently, tailoring of

microstructure appears to be useful in those applications where the sign of the thermal gradient is preserved.

The results presented point to the potential usefulness of the developed theoretical framework for analyzing the response of advanced composites with tailored microstructures to thermal gradients in the presence of elastic phases with temperature-independent prop- erties. In the future, the approach will be extended to include inelastic effects as well as temperature-dependent response of the constituent phases exhibited by advanced metal matrix composites at elevated temperatures. Finally, the full potential of the presented method as a design tool for functionally graded or tailored composites can only be realized, however, when it is combined with an appropriate optimization approach [see, for example, Saravanos and Chamis (1992)]. This too will be addressed in future work.

Acknowledgements-The first two authors gratefully acknowledge the support provided by the NASA-Lewis Research Center through the grant NASA NAG 3-1377. The authors are grateful to Drs Dimitris Saravanos, Thomas Wilt and Don Petrasek for their comments during the preparation of this paper. They would also like to express their appreciation to Professor Carl T. Herakovich for fruitful discussions during the initial stages of this investigation, and to Professor E. A. Starke, Dean of the School of Engineering and Applied Science at the University of Virginia for providing partial support during the first author's sabbatical leave.

## REFERENCES

Aboudi, J. (1991). *Mechanics of Composite Materials-A Unified Micromechanical Approach*. Elsevier, New York.

Aboudi, J. and Pindera, M.-J. (1992). Micromechanics of metal matrix composites using the generalized method of cells model: user's guide. NASA CR 190756, NASA-Lewis Research Center, Cleveland, OH.

Aboudi, J., Pindera, M.-J. and Arnold, S. M. (1993). Thermoelastic response of large-diameter fiber metal matrix composites to thermal gradients. NASA TM 106344, NASA-Lewis Research Center, Cleveland, OH.

Christensen, R. M. (1979). *Mechanics of Composite Materials*. John Wiley, New York.

Hill, R. (1963). Elastic properties of reinforced solids: some theoretical principles. *J. Mech. Phys. Solids* **11**, 357.

Malvern, L. E. (1969). *Introduction to the Mechanics of a Continuous Medium*. Prentice-Hall, Englewood Cliffs, NJ.

Pagano, N. J. (1974). The role of effective moduli in the elastic analysis of composite laminates. In *Composite Materials. Volume II: Mechanics of Composite Materials* (Edited by G. P. Sendecky), pp. 1-22. Academic Press, New York.

Paley, M. and Aboudi, J. (1992). Micromechanical analysis of composites by the generalized cells model. *Mechanics of Materials* **14**, 127.

Saravanos, D. A. and Chamis, C. C. (1992). Multiobjective shape and material optimization of composite structures including damping. *AIAA JI* **30**, 805.

Yamanouchi, M. Koizumi, M., Hirai, T. and Shiota, I. (1990). *Proceedings of the First International Symposium on Functionally Gradient Materials*. Sendai, Japan.

## APPENDIX A: THERMAL ANALYSIS

### 1. Heat conduction equations

Multiplying eqn (6) by $(\bar{x}_{1}^{(\alpha)})^{l}(\bar{x}_{2}^{(\beta)})^{m}(\bar{x}_{3}^{(\gamma)})^{n}$, where $l, m, n = 0, 1$ or 2 with $l+m+n \leqslant 2$, and integrating by parts, using the temperature expansion given in eqn (14), the following equations are obtained

$$
L_{1(0,0,0)}^{(\alpha \beta \gamma)}+L_{2(0,0,0)}^{(\alpha \beta \gamma)}+L_{3(0,0,0)}^{(\alpha \beta \gamma)}=0 \tag{A1}
$$

$$
L_{1(1,0,0)}^{(\alpha \beta \gamma)}-Q_{1(0,0,0)}^{(\alpha \beta \gamma)}=0 \tag{A2}
$$

$$
\frac{1}{4} d_{\alpha}^{(p) 2}\left[L_{1(1,0,0)}^{(\alpha \beta \gamma)}+\frac{1}{3} L_{2(0,0,0)}^{(\alpha \beta \gamma)}+\frac{1}{3} L_{3(0,0,0)}^{(\alpha \beta \gamma)}\right]-2 Q_{1(1,0,0)}^{(\alpha \beta \gamma)}=0 \tag{A3}
$$

$$
\frac{1}{12} h_{\beta}^{2}\left[L_{1(0,0,0)}^{(\alpha \beta \gamma)}+3 L_{2(0,0,0)}^{(\alpha \beta \gamma)}+L_{3(0,0,0)}^{(\alpha \beta \gamma)}\right]-2 Q_{2(0,1,0)}^{(\alpha \beta \gamma)}=0 \tag{A4}
$$

$$
\frac{1}{12} l_{\gamma}^{2}\left[L_{1(0,0,0)}^{(\alpha \beta \gamma)}+L_{2(0,0,0)}^{(\alpha \beta \gamma)}+3 L_{3(0,0,0)}^{(\alpha \beta \gamma)}\right]-2 Q_{3(0,0,1)}^{(\alpha \beta \gamma)}=0, \tag{A5}
$$

where $Q_{l(l, m, n)}^{(\alpha \beta \gamma)}$ has been defined previously in eqn (15), and

$$
L_{1(1,0,0)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}}\left(\frac{d_{\alpha}^{(p)}}{2}\right)^{n} \int_{-h_{\beta} / 2}^{h_{\beta} / 2} \int_{-l_{\gamma} / 2}^{l_{\gamma} / 2}\left[q_{1}^{(\alpha \beta \gamma)}\left(\frac{d_{\alpha}^{(p)}}{2}\right)+(-1)^{n+1} q_{1}^{(\alpha \beta \gamma)}\left(-\frac{d_{\alpha}^{(p)}}{2}\right)\right] d \bar{x}_{2}^{(\beta)} d \bar{x}_{3}^{(\gamma)} \tag{A6}
$$

$$
L_{2(0, n, 0)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}}\left(\frac{h_{\beta}}{2}\right)^{n} \int_{-d_{\alpha}^{(p)} / 2}^{d_{\alpha}^{(p)} / 2} \int_{-l_{\gamma} / 2}^{l_{\gamma} / 2}\left[q_{2}^{(\alpha \beta \gamma)}\left(\frac{h_{\beta}}{2}\right)+(-1)^{n+1} q_{2}^{(\alpha \beta \gamma)}\left(-\frac{h_{\beta}}{2}\right)\right] d \bar{x}_{1}^{(\alpha)} d \bar{x}_{3}^{(\gamma)} \tag{A7}
$$

$$
L_{3(0,0, m)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}}\left(\frac{l_{\gamma}}{2}\right)^{n} \int_{-d_{\alpha}^{(p)} / 2}^{d_{\alpha}^{(p)} / 2} \int_{-h_{\beta} / 2}^{h_{\beta} / 2}\left[q_{1}^{(\alpha \beta \gamma)}\left(\frac{l_{\gamma}}{2}\right)+(-1)^{n+1} q_{3}^{(\alpha \beta \gamma)}\left(-\frac{l_{\gamma}}{2}\right)\right] d \bar{x}_{1}^{(\alpha)} d \bar{x}_{2}^{(\beta)}. \tag{A8}
$$

In the above: $n=0$ or 1 ;

$$
q_{1}^{(\alpha \beta \gamma)}\left( \pm \frac{d_{\alpha}^{(p)}}{2}\right),\quad q_{2}^{(\alpha \beta \gamma)}\left( \pm \frac{h_{\beta}}{2}\right),\quad q_{3}^{(\alpha \beta \gamma)}\left( \pm \frac{l_{\gamma}}{2}\right)
$$

denote the interfacial fluxes at $\bar{x}_{1}^{(\alpha)}= \pm \frac{1}{2} d_{\alpha}^{(p)}$, $\bar{x}_{2}^{(\beta)}= \pm \frac{1}{2} h_{\beta}$, $\bar{x}_{3}^{(\gamma)}= \pm \frac{1}{2} l_{\gamma}$, respectively; and $v_{(\alpha \beta \gamma)}^{(p)}=d_{\alpha}^{(p)} h_{\beta} l_{\gamma}$ is the volume of the subcell $(\alpha \beta \gamma)$ in the $p$ th cell.

Equations (A1)-(A5) provide relations between the zeroth-order and first-order heat fluxes $Q_{i(l, m, n)}^{(\alpha \beta \gamma)}$ and the interfacial fluxes $L_{i(l, m, n)}^{(\alpha \beta \gamma)}$. Explicit expressions for the interfacial fluxes $L_{i(l, m, n)}^{(\alpha \beta \gamma)}$ given solely in terms of $Q_{i(l, m, n)}^{(\alpha \beta \gamma)}$ are obtained through the following sequence of manipulations, noting that eqn (A2) already provides a direct relation between $Q_{1(0,0,0)}^{(\alpha \beta \gamma)}$ and $L_{1(1,0,0)}^{(\alpha \beta \gamma)}$. First, substituting equation (A1) into (A4) and (A5), respectively, gives the following direct expressions for $L_{2(0,0,0)}^{(\alpha \beta \gamma)}$ and $L_{3(0,0,0)}^{(\alpha \beta \gamma)}$.

$$
\frac{1}{6} h_{\beta}^{2} L_{2(0,0,0)}^{(\alpha \beta \gamma)}=2 Q_{2(0,1,0)}^{(\alpha \beta \gamma)} \tag{A9}
$$

$$
\frac{1}{6} l_{\gamma}^{2} L_{3(0,0,0)}^{(\alpha \beta \gamma)}=2 Q_{3(0,0,1)}^{(\alpha \beta \gamma)}. \tag{A10}
$$

Then upon substitution of eqns (A9) and (A10) into (A1) we obtain the following expression for $L_{1(0,0,0)}^{(\alpha \beta \gamma)}$

$$
L_{1(0,0,0)}^{(\alpha \beta \gamma)}=-12\left(Q_{2(0,1,0)}^{(\alpha \beta \gamma)} / h_{\beta}^{2}+Q_{3(0,0,1)}^{(\alpha \beta \gamma)} / l_{\gamma}^{2}\right). \tag{A11}
$$

Equations (A9)-(A11) will be used to reduce the heat conduction and heat flux continuity equations to expressions involving only the heat flux quantities $Q_{i(l, m, n)}^{(\alpha \beta \gamma)}$. These can subsequently be expressed in terms of the fundamental unknown coefficients $T_{i}^{(\alpha \beta \gamma)}$, appearing in the temperature expansion given by eqns (14), using eqns (16)-(19).

### 2. Heat flux continuity equations
The heat flux continuity conditions (8)-(9) are imposed on an average basis at each subcell and cell interface. Prior to imposing these continuity conditions, let us define intermediate quantities $f_{i}^{(1 \beta \gamma)}$ and $g_{i}^{(1 \beta \gamma)}$ as follows:

$$
f_{i}^{(1 \beta \gamma)}=\left.q_{i}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=d_{1}^{(p)} / 2}-\left.q_{i}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=-d_{1}^{(p)} / 2} \tag{A12}
$$

$$
g_{i}^{(1 \beta \gamma)}=\left.q_{i}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=d_{1}^{(p)} / 2}+\left.q_{i}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=-d_{1}^{(p)} / 2}. \tag{A13}
$$

These quantities will simplify the algebra associated with application of the heat flux continuity requirement on an average basis in the FG direction. Then substituting eqns (8a) and (9a) into the above definitions we have

$$
\left.f^{(1 \beta \gamma)}\right|^{(p)}=\left.q_{1}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=-d_{2}^{(p)} / 2} ^{(p)}-\left.q_{1}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=d_{2}^{(p-1)} / 2} ^{(p-1)} \tag{A14}
$$

$$
\left.g_{1}^{(1 \beta \gamma)}\right|^{(p)}=\left.q_{1}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=-d_{2}^{(p)} / 2} ^{(p)}+\left.q_{1}^{(2 \beta \gamma)}\right|_{\bar{x}_{1}^{(2)}=d_{2}^{(p-1)} / 2} ^{(p-1)}. \tag{A15}
$$

Adding and subtracting equal quantities to and from eqns (A14) and (A15) it can easily be verified that

$$
2\left.f_{1}^{(1 \beta \gamma)}\right|^{(n)}=\left[-f_{1}^{(2 \beta \gamma)}+g_{1}^{(2 \beta \gamma)}\right]^{(p)}-\left[f_{1}^{(2 \beta \gamma)}+g_{1}^{(2 \beta \gamma)}\right]^{(p-1)} \tag{A16}
$$

$$
2\left.g_{1}^{(1 \beta \gamma)}\right|^{(p)}=\left[-f_{1}^{(2 \beta \gamma)}+g_{1}^{(2 \beta \gamma)}\right]^{(p)}+\left[f_{1}^{(2 \beta \gamma)}+g_{1}^{(2 \beta \gamma)}\right]^{(p-1)}. \tag{A17}
$$

Then using eqns (A16) and (A17) in (A6), we obtain the following heat flux continuity conditions for the FG direction

$$
\left.d^{(p)} L_{1(0,0,0)}^{(1 \beta \gamma)}\right|^{(p)}=\left[L_{1(1,0,0)}^{(2 \beta \gamma)}-\frac{1}{2} d_{1}^{(p)} L_{1(0,0,0)}^{(2 \beta \gamma)}\right]^{(p)}-\left[L_{1(1,0,0)}^{(2 \beta \gamma)}+\frac{1}{2} d_{2}^{(p-1)} L_{1(0,0,0)}^{(2 \beta \gamma)}\right]^{(p-1)} \tag{A18}
$$

$$
\left.L_{1(1,0,0)}^{(1 \beta \gamma)}\right|^{(p)}=\frac{1}{2}\left[L_{1(1,0,0)}^{(2 \beta \gamma)}-\frac{1}{4} d_{2}^{(p)} L_{1(0,0,0)}^{(2 \beta \gamma)}\right]^{(p)}+\frac{1}{2}\left[L_{1(1,0,0)}^{(2 \beta \gamma)}+\frac{1}{4} d_{2}^{(p-1)} L_{1(0,0,0)}^{(2 \beta \gamma)}\right]^{(p-1)}. \tag{A19}
$$

The heat flux continuity conditions in the remaining two directions are obtained using eqns (8b) and (8c) in (A7) and (A8), respectively. From eqns (8b) and (A7) we have

$$
\left.h_{1} L_{2(0,0,0)}^{(x 1 \gamma)}\right|^{(p)}=-\left.h_{2} L_{2(0,0,0)}^{(x 2 \gamma)}\right|^{(p)} \tag{A20}
$$

while from eqns (8c) and (A8)

$$
\left.l_{1} L_{3(0,0,0)}^{(\alpha \beta 1)}\right|^{(p)}=-\left.l_{2} L_{3(0,0,0)}^{(\alpha \beta 2)}\right|^{(p)}. \tag{A21}
$$

Equations (A9)-(A11), together with eqn (A2), will be employed in reducing the heat flux continuity conditions (A18)-(A21) to expressions involving only the volume-averaged zeroth-order and first-order heat flux quantities $Q_{i(l, m, n)}^{(\alpha \beta \gamma)}$.

### 3. Reduction of heat conduction and heat flux continuity equations
Substituting eqn (A1) into (A3), and using eqns (A9) and (A10), reduces the volume-averaged heat conduction equations to a set of eight equations given by eqn (20). Next, using the expression for $L_{1(0,0,0)}^{(\alpha \beta \gamma)}$ given by eqn (A11),

and the expression for $L_{1(1,0,0)}^{(\alpha \beta \gamma)}$ given by eqn (A2), in the continuity relations (A18) and (A19), we obtain eqns (21) and (22). Finally, combining eqns (A9) and (A20), as well as eqns (A10) and (A21), gives eqns (23) and (24).

## 4. Thermal continuity equations
As in the case of the heat flux field, the thermal continuity conditions (10) and (11) are imposed on an average basis at each subcell and cell interface. Thus substituting eqn (14) into eqns (10a-c), respectively, we obtain at each subcell interface the conditions (25)-(27). Furthermore, substituting eqn (14) into (11a) to ensure continuity of temperature between neighboring cells in the FG direction, we obtain the condition (28).

## APPENDIX B: MECHANICAL ANALYSIS

### 1. Equations of equilibrium
Let us multiply eqn (30) by $(\bar{x}_{1}^{(\alpha)})^{l}(\bar{x}_{2}^{(\beta)})^{m}(\bar{x}_{3}^{(\gamma)})^{n}$, where again $l, m, n = 0, 1$, or 2 with $l+m+n \leqslant 2$. Integrating the resulting equations by parts, and using the displacement expansions (39), we obtain the equations of equilibrium in the subcell region $(\alpha \beta \gamma)$ in the form

$$
I_{11(0,0,0)}^{(\alpha \beta \gamma)}+J_{21(0,0,0)}^{(\alpha \beta \gamma)}+K_{31(0,0,0)}^{(\alpha \beta \gamma)}=0 \tag{B1}
$$

$$
I_{11(1,0,0)}^{(\alpha \beta \gamma)}-S_{11(0,0,0)}^{(\alpha \beta \gamma)}=0 \tag{B2}
$$

$$
J_{22(0,1,0)}^{(\alpha \beta \gamma)}-S_{22(0,0,0)}^{(\alpha \beta \gamma)}=0 \tag{B3}
$$

$$
K_{33(0,0,1)}^{(\alpha \beta \gamma)}-S_{33(0,0,0)}^{(\alpha \beta \gamma)}=0 \tag{B4}
$$

$$
3 I_{11(0,0,0)}^{(\alpha \beta \gamma)}+J_{21(0,0,0)}^{(\alpha \beta \gamma)}+K_{31(0,0,0)}^{(\alpha \beta \gamma)}-24 S_{11(1,0,0)}^{(\alpha \beta \gamma)} / d_{\alpha}^{(p) 2}=0 \tag{B5}
$$

$$
I_{11(0,0,0)}^{(\alpha \beta \gamma)}+3 J_{21(0,0,0)}^{(\alpha \beta \gamma)}+K_{31(0,0,0)}^{(\alpha \beta \gamma)}-24 S_{12(0,1,0)}^{(\alpha \beta \gamma)} / h_{\beta}^{2}=0 \tag{B6}
$$

$$
I_{11(0,0,0)}^{(\alpha \beta \gamma)}+J_{21(0,0,0)}^{(\alpha \beta \gamma)}+3 K_{31(0,0,0)}^{(\alpha \beta \gamma)}-24 S_{13(0,0,1)}^{(\alpha \beta \gamma)} / l_{\gamma}^{2}=0, \tag{B7}
$$

where $S_{i j(l, m, n)}^{(\alpha \beta \gamma)}$ has been defined previously in eqn (40), and

$$
I_{1 j(n, 0,0)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}}\left(\frac{1}{2} d_{\alpha}^{(p)}\right)^{n} \int_{-h_{\beta} / 2}^{h_{\beta} / 2} \int_{-l_{\gamma} / 2}^{l_{\gamma} / 2}\left[\sigma_{1 j}^{(\alpha \beta \gamma)}\left(\frac{1}{2} d_{\alpha}^{(p)}\right)+(-1)^{n+1} \sigma_{1 j}^{(\alpha \beta \gamma)}\left(-\frac{1}{2} d_{\alpha}^{(p)}\right)\right] d \bar{x}_{2}^{(\gamma)} d \bar{x}_{3}^{(\gamma)} \tag{B8}
$$

$$
J_{2 j(0, n, 0)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}}\left(\frac{1}{2} h_{\beta}\right)^{n} \int_{-d_{\alpha}^{(p)} / 2}^{d_{\alpha}^{(p)} / 2} \int_{-l_{\gamma} / 2}^{l_{\gamma} / 2}\left[\sigma_{2 j}^{(\alpha \beta \gamma)}\left(\frac{1}{2} h_{\beta}\right)+(-1)^{n+1} \sigma_{2 j}^{(\alpha \beta \gamma)}\left(-\frac{1}{2} h_{\beta}\right)\right] d \bar{x}_{1}^{(\alpha)} d \bar{x}_{3}^{(\gamma)} \tag{B9}
$$

$$
K_{3 j(0,0, n)}^{(\alpha \beta \gamma)}=\frac{1}{v_{(\alpha \beta \gamma)}^{(p)}}\left(\frac{1}{2} l_{\gamma}\right)^{n} \int_{-d_{\alpha}^{(p)} / 2}^{d_{\alpha}^{(p)} / 2} \int_{-h_{\beta} / 2}^{h_{\beta} / 2}\left[\sigma_{3 j}^{(\alpha \beta \gamma)}\left(\frac{1}{2} l_{\gamma}\right)+(-1)^{n+1} \sigma_{3 j}^{(\alpha \beta \gamma)}\left(-\frac{1}{2} l_{\gamma}\right)\right] d \bar{x}_{1}^{(\alpha)} d \bar{x}_{2}^{(\beta)}. \tag{B10}
$$

In the above: $n=0$ or $1$; $\sigma_{1 j}^{(\alpha \beta \gamma)}( \pm \frac{1}{2} d_{\alpha}^{(p)}), \sigma_{2 j}^{(\alpha \beta \gamma)}( \pm \frac{1}{2} h_{\beta}), \sigma_{3 j}^{(\alpha \beta \gamma)}( \pm \frac{1}{2} l_{\gamma})$, stand for the interfacial stresses at $\bar{x}_{1}^{(\alpha)}=$ $\pm \frac{1}{2} d_{\alpha}^{(p)}, \bar{x}_{2}^{(\beta)}=\pm \frac{1}{2} h_{\beta}, \bar{x}_{3}^{(\gamma)}=\pm \frac{1}{2} l_{\gamma}$, respectively.

Equations (B1)-(B7) provide relations between the zeroth-order and first-order, volume-averaged stresses $S_{i j(l, m, n)}^{(\alpha \beta \gamma)}$ and the interfacial tractions $I_{1 j(n, 0,0)}^{(\alpha \beta \gamma)}, J_{2 j(0, n, 0)}^{(\alpha \beta \gamma)}$, and $K_{3 j(0,0, n)}^{(\alpha \beta \gamma)}$. Direct "one-to-one" relations are obtained through the following sequence of manipulations, noting that equations (B2)-(B4) already provide direct relations between $S_{11(0,0,0)}^{(\alpha \beta \gamma)}$ and $I_{11(1,0,0)}^{(\alpha \beta \gamma)}, S_{22(0,0,0)}^{(\alpha \beta \gamma)}$, and $J_{22(0,1,0)}^{(\alpha \beta \gamma)}, S_{33(0,0,0)}^{(\alpha \beta \gamma)}$ and $K_{33(0,0,1)}^{(\alpha \beta \gamma)}$. First, substituting equation (B1) into eqns (B6) and (B7), respectively, gives direct expressions for $J_{21(0,0,0)}^{(\alpha \beta \gamma)}$ and $K_{31(0,0,0)}^{(\alpha \beta \gamma)}$

$$
\frac{1}{6} h_{\beta}^{2} J_{21(0,0,0)}^{(\alpha \beta \gamma)}=2 S_{12(0,1,0)}^{(\alpha \beta \gamma)} \tag{B11}
$$

$$
\frac{1}{6} l_{\gamma}^{2} K_{31(0,0,0)}^{(\alpha \beta \gamma)}=2 S_{13(0,0,1)}^{(\alpha \beta \gamma)}. \tag{B12}
$$

Then, upon substitution of eqns (B11) and (B12) into (B1), we have the following expression for $I_{11(0,0,0)}^{(\alpha \beta \gamma)}$

$$
I_{11(0,0,0)}^{(\alpha \beta \gamma)}=-12\left(S_{12(0,1,0)}^{(\alpha \beta \gamma)} / h_{\beta}^{2}+S_{13(0,0,1)}^{(\alpha \beta \gamma)} / l_{\gamma}^{2}\right). \tag{B13}
$$

Equations (B11)-(B13) will be used to reduce the equilibrium equations and traction continuity equations to expressions involving only the zeroth-order and first-order, volume-averaged stress quantities $S_{i j(l, m, n)}^{(\alpha \beta \gamma)}$. These can subsequently be expressed in terms of the fundamental unknown coefficients $w_{1}^{(\alpha \beta \gamma)}, U_{1}^{(\alpha \beta \gamma)}, V_{1}^{(\alpha \beta \gamma)}, W_{1}^{(\alpha \beta \gamma)}, \phi_{1}^{(\alpha \beta \gamma)}$, $\chi_{2}^{(\alpha \beta \gamma)}$, and $\psi_{3}^{(\alpha \beta \gamma)}$ appearing in the displacement field expansion given by eqns (39), using eqns (41)-(46).

### 2. Traction continuity conditions
The traction continuity conditions, eqns (33) and (34), are imposed on an average basis at thc subcell and cell interfaces. These conditions imply existence of certain relationships between the surface integrals of the interfacial traction components defined by eqns (B8)-(B10). To assist in establishing these relations, let us define two new quantities $F_{i j}^{(1 \beta \gamma)}$ and $G_{i j}^{(1 \beta \gamma)}$ as follows:

$$F_{i j}^{(1 \beta \gamma)}=\left.\sigma_{i j}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=d_{1}^{(p)} / 2}-\left.\sigma_{i j}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=-d_{1}^{(p)} / 2}\tag{B14}$$

$$G_{i j}^{(1 \beta \gamma)}=\left.\sigma_{i j}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=d_{1}^{(p)} / 2}+\left.\sigma_{i j}^{(1 \beta \gamma)}\right|_{\xi_{1}^{(1)}=-d_{1}^{(p)} / 2}.\tag{B15}$$

Substituting eqns (33a) and (34a) into the above definitions, we obtain, respectively

$$F_{11}^{(1 \beta \gamma)}\left|^{(p)}=\left.\sigma_{11}^{(2 \beta \gamma)}\right|_{\xi_{1}^{(2)}=-d_{2}^{(p)} / 2}-\left.\sigma_{11}^{(2 \beta \gamma)}\right|_{\xi_{1}^{(p-1)}=d_{2}^{(p-1)} / 2}\tag{B16}$$

$$G_{11}^{(1 \beta \gamma)}\left|^{(p)}=\left.\sigma_{11}^{(2 \beta \gamma)}\right|_{\xi_{1}^{(2)}=-d_{2}^{(p)} / 2}+\left.\sigma_{11}^{(2 \beta \gamma)}\right|_{\xi_{1}^{(p-1)}=d_{2}^{(p-1)} / 2}.\tag{B17}$$

By addition and subtraction of equal quantities to and from eqns (B16) and (B17) it can easily be verified that

$$2 F_{11}^{(1 \beta \gamma)}\left|^{(p)}=\left\{-F_{11}^{(2 \beta \gamma)}+G_{11}^{(2 \beta \gamma)}\right\}^{(p)}-\left\{F_{11}^{(2 \beta \gamma)}+G_{11}^{(2 \beta \gamma)}\right\}^{(p-1)}\right.\tag{B18}$$

$$2 G_{11}^{(1 \beta \gamma)}\left|^{(p)}=\left[G_{11}^{(2 \beta \gamma)}-F_{11}^{(2 \beta \gamma)}\right]^{(p)}+\left[G_{11}^{(2 \beta \gamma)}+F_{11}^{(2 \beta \gamma)}\right]^{(p-1)}.\tag{B19}\right.$$

Then employing eqns (B18) and (B19) in equation (B8) with $j=1$, we obtain the corresponding relations

$$d_{1}^{(p)} I_{11(0,0,0)}^{(1 \beta \gamma)}\left|^{(p)}=\left[I_{11(1,0,0)}^{(2 \beta \gamma)}-\frac{1}{2} d_{2}^{(p)} I_{11(0,0,0)}^{(2 \beta \gamma)}\right]^{(p)}-\left[I_{11(1,0,0)}^{(2 \beta \gamma)}+\frac{1}{2} d_{2}^{(p-1)} I_{11(0,0,0)}^{(2 \beta \gamma)}\right]^{(p-1)}\right.\tag{B20}$$

$$I_{11(1,0,0)}^{(1 \beta \gamma)}\left|^{(p)}=\frac{1}{2}\left[I_{11(1,0,0)}^{(2 \beta \gamma)}-\frac{1}{4} d_{2}^{(p)} I_{11(0,0,0)}^{(2 \beta \gamma)}\right]^{(p)}+\frac{1}{2}\left[I_{11(1,0,0)}^{(2 \beta \gamma)}+\frac{1}{2} d_{2}^{(p-1)} I_{11(0,0,0)}^{(2 \beta \gamma)}\right]^{(p-1)}.\tag{B21}\right.$$

Similarly, using eqns (33b) and (B9) we have

$$h_{1} J_{21(0,0,0)}^{(\alpha 1 \gamma)}\left|^{(p)}=-\left.h_{2} J_{21(0,0,0)}^{(\alpha 2 \gamma)}\right|^{(p)}\right.\tag{B22}$$

$$\left.J_{22(0,1,0)}^{(\alpha 1 \gamma)}\right|^{(p)}=\left.J_{22(0,1,0)}^{(\alpha 2 \gamma)}\right|^{(p)}\tag{B23}$$

and from eqns (33c) and (B10) we obtain

$$l_{1} K_{31(0,0,0)}^{(\alpha \beta 1)}\left|^{(p)}=-\left.l_{2} K_{31(0,0,0)}^{(\alpha \beta 2)}\right|^{(p)}\right.\tag{B24}$$

$$\left.K_{33(0,0,1)}^{(\alpha \beta 1)}\right|^{(p)}=\left.K_{33(0,0,1)}^{(\alpha \beta 2)}\right|^{(p)}.\tag{B25}$$

As a result of the above manipulations, 24 relations, given by eqns (B20)-(B25), arise from the traction continuity conditions between subcells and between neighboring cells. These equations, in conjunction with equations (B1)-(B5), and eqns (B11)-(B13), will be employed in reducing the equilibrium and traction continuity equations to expressions involving only volume-averaged zeroth-order and first-order stresses $S_{i j(l, m, n)}^{(\alpha \beta \gamma)}$.

### 3. Reduction of equilibrium and traction continuity equations
Substituting eqn (B1) into eqn (B5) and using eqns (B11) and (B12), reduces the volume-averaged equilibrium equations to a set of eight equations given by eqn (47). Next, combining the expressions for $I_{11(0,0,0)}^{(\alpha \beta \gamma)}$ and $I_{11(0,0,0)}^{(\alpha \beta \gamma)}$, provided by eqns (B2) and (B13), and the continuity relations (B20) and (B21), respectively, we obtain the eight equations given by (48) and (49). Continuing, if we substitute eqn (B11) into eqn (B22) directly, and eqn (B12) into eqn (B24), we obtain, eqns (50) and (51), respectively. Finally, combining eqns (B3) and (B23), and equations (B4) and (B25), yields, eqns (52) and (53), respectively.

### 4. Displacement continuity conditions
The displacement continuity conditions, i.e. eqns (35) and (36), are now imposed on an average basis at the interfaces. This is accomplished by first substituting eqn (39) into eqn (35a), yielding eqn (54), then into eqn (35b), yielding eqns (55) and (56), followed by eqn (35c), yielding eqns (57) and (58), and finally into eqn (36a), yielding eqn (59). Consequently, eqns (54)-(59) provide 24 relations which must be imposed to guarantee the continuity of the displacements between the subcells and between neighboring cells.