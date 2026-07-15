# Characterizing load transfer efficiency in double-walled carbon nanotubes using multiscale finite element modeling

Ting-Chu Lu, Jia-Lin Tsai *

Department of Mechanical Engineering, National Chiao Tung University, Hsinchu 300, Taiwan

---

## ARTICLE INFO

Article history:
Received 4 December 2011
Received in revised form 6 April 2012
Accepted 25 April 2012
Available online 2 May 2012

Keywords:
A. Nano-structures
B. Interface/interphase
B. Stress transfer
Multiscale simulation

## ABSTRACT

Load transfer efficiency from matrix to carbon nanotubes (CNTs) plays an important role in the mechanical response of CNTs nanocomposites as it may affect the effectiveness of the nano-reinforcements. For double-walled carbon nanotubes (DWCNTs), the outer graphene layer as well as the inner layer may be responsible for the load bearing capacity. In this study, the load transfer efficiency within DWCNTs was investigated using a multiscale simulation scheme. The multiscale simulation consists of two steps. First, the atomistic behaviors between the adjacent graphite layers in DWCNTs were characterized using molecular dynamic (MD) simulation, from which a cylindrical equivalent continuum solid of DWCNTs with embedded spring elements was proposed to describe the interactions of neighboring graphene layers. Two kinds of interatomistic properties in DWCNTs, i.e., van der Walls (vdW) interactions and artificial build-up covalent bonds, were considered in the equivalent solid. Subsequently, the equivalent solid was implemented as reinforcement in the micromechanical model of CNTs nanocomposites for evaluating the load transfer efficiency. Results indicated that the DWCNTs with covalent bonds exhibit superior load transfer efficiency than those with only vdW interactions. In addition, when the DWCNTs get long, the load transfer efficiency of DWCNTs increases accordingly.

© 2012 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

CNTs with superlative mechanical and physical properties have been extensively utilized as reinforcements in nanocomposites [1–3]. The load transfer efficiency from the matrix to the CNTs plays an important role in the mechanical responses of the CNTs nanocomposites as it may affect the load bearing implementation of nano-reinforcements. For multi-walled carbon nanotubes (MWCNTs), the outer graphene layers as well as the inner layers may be responsible for sustaining the applied load. Therefore, the load carrying capacity from the outermost layer to interior layers in MWCNTs associated with different interatomistic properties must be investigated thoroughly.

Zalamea et al. [4] employed the shear transfer model as well as the shear lag model to explore the stress transfer from the outermost layer to the interior layers in MWCNTs. Basically, the interlayer properties between graphene layers were designated by scaling the parameter of shear transfer efficiency with respect to the perfect bonding. Zalamea et al. pointed out that as the number of layers in MWCNTs increases, the stress transfer efficiency decreases correspondingly. Shen et al. [5] examined load transfer between adjacent walls of DWCNTs using MD simulation, indicating that the tensile loading on the outermost wall of MWCNTs cannot be effectively transferred into the inner walls. However, when chemical bonding between the walls is established, the effectiveness can be dramatically enhanced. It is noted that in the above investigations, the loadings were applied directly on the outermost layers of MWCNTs; the stresses in the inner layers were then calculated either from the continuum mechanics approach [4] or MD simulation [5]. Shokrieh and Rafiee [6] examined the mechanical properties of nanocomposites with capped single-walled carbon nanotubes (SWCNTs) embedded in a polymer matrix. The load transfer efficiency in terms of different CNTs' lengths was the main concern in their examination. By introducing an interphase to represent the vdW interactions between SWCNTs and the surrounding matrix, Shokrieh and Rafiee [7] converted the atomistic SWCNTs into an equivalent continuum fiber in finite element analysis. The idea of an equivalent solid fiber was also proposed by Gao and Li [8] to replace the atomistic structure of capped SWCNTs in the nanocomposites' cylindrical unit cell. The modulus of the equivalent solid was determined based on the atomistic structure of SWCNTs through molecular structure mechanics [9]. Subsequently, the continuum-based shear lag analysis was carried out to evaluate the axial stress distribution in CNTs. In addition, the influence of end caps in SWCNTs on the stress distribution of nanocomposites was also taken into account in their analysis. Tsai and Lu [10] characterized the effects of the layer number, intergraphic layers interaction, and aspect ratio of MWCNTs on the load

* Corresponding author. Tel.: +886 3 5731608; fax: +886 3 5720634.
E-mail address: jialin@mail.nctu.edu.tw (J.-L. Tsai).

1359-8368/$ - see front matter © 2012 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.compositesb.2012.04.059

transfer efficiency using the conventional shear lag model and finite element analysis. However, in their analysis, the interatomistic characteristics of the adjacent graphene layers associated with different degrees of interactions were simplified by a thin interphase with different moduli. The atomistic interaction between the graphene layers was not taken into account in their modeling of MWCNTs.

In light of the forgoing investigations, the equivalent solid of SWCNTs was developed by several researchers and then implemented as reinforcement in continuum-based nanocomposite models. Nevertheless, for MWCNTs, the subjects concerning the development of equivalent continuum solid are seldom explored in the literature. In fact, how to introduce the atomistic characteristics, i.e., the interfacial properties of neighboring graphene layers in MWCNTs, into the equivalent continuum solid is a challenging task as the length scales used to describe the physical phenomenon are distinct. Thus, a multi-scale based simulation is required to account for the atomistic attribute of MWCNTs into an equivalent continuum solid. In this study, the multi-scale approach was utilized to investigate the load transfer efficiency from surrounding matrix to DWCNTs. The analysis consisted of two stages. First, a cylindrical DWCNTs equivalent continuum was proposed based on MD simulation where the pullout extension on the outer layer was performed in an attempt to characterize the atomistic behaviors between neighboring graphite layers. Subsequently, the cylindrical continuum was embedded in a unit cell of nanocomposites, and the axial stress distribution as well as the load transfer efficiency of the DWCNTs was evaluated from finite element analysis. Both single-walled carbon nanotubes (SWCNTs) and DWCNTs were considered in the simulation and the results were compared with each other.

## 2. Molecular dynamics simulation

### 2.1. Construction of atomistic structures of DWCNTs

The configuration of DWCNTs is a hollow cylindrical structure, which contains two concentric graphene layers. Each graphene layer is constructed by the carbon atoms arranged in a hexagonal pattern. The interatomistic distance between adjacent carbon atoms is $1.42\,\text{Å}$, and the associated atomistic interaction is covalently bonded by $\text{sp}^2$ hybridized electrons. Experimental observation found that the interlayer spacing of graphene layers is around $0.34\,\text{nm}$ [11]. In order to investigate the atomistic behaviors of DWCNTs, the molecular model has to be constructed in conjunction with the appropriately specified atomistic interactions. In the description of DWCNTs, two kinds of atomistic interactions are normally taken into account; one is bonded interaction, such as the covalent bond, and the other is the non-bonded interaction, i.e., vdW force. For the covalent bond, the atomistic interactions between neighboring carbon atoms that provides the building block of the primary structure of CNTs were described using the potential energy that consists of bond stretching, bond angle variation, torsion, and inversion [12]. In this study, an AMBER force field [9,13] was utilized to simulate the bonded interactions of carbon atoms. Moreover, the non-bonded interaction between the carbon atoms was characterized by the Lennard-Jones (L-J) potential as [14]

$$
U_{vdW}=4u\left[\left(\frac{r_0}{r_{ij}}\right)^{12}-\left(\frac{r_0}{r_{ij}}\right)^6\right] \tag{1}
$$

where $r_{ij}$ is the distance between the non-bonded pair of carbon atoms. The parameters $u=0.0556\,\text{kcal/mol}$ and $r_0=3.40\,\text{Å}$ suggested in the literature [9] were adopted in Eq. (1) to model the non-bonded interaction within graphene layer. In addition, the same parameters were also selected for the carbon-carbon non-bonded interactions between different layers of DWCNTs. On the other hand, in addition to vdW force, the covalent bonds with $\text{sp}^3$ hybridized electrons were artificially established between the two graphene layers in DWCNTs in order to understand the effect of covalent bonding in the interfacial adhesion. The covalent bonds were constructed at four different positions along the DWCNTs, i.e., about $3.69\,\text{Å}$ and one fourth of the length from both ends, as illustrated in Fig. 1. In this study, (3,3) and (8,8) DWCNTs with the lengths (2L) of 160, 324, 590 and $984\,\text{Å}$ were employed in the MD simulations. It is noted that for the CNTs without any cross covalent link to another layer, the adjacent carbon atoms are covalently

![](./images/813313146641973251_1.jpg)

Fig. 1. (a) Illustration of atomistic structure of DWCNTs with covalent bonds (b) enlarged region of covalent bonding and (c) three covalent bonds established in each location.

![](./images/813313146641973251_2.jpg)

Fig. 2. Extension of outer layer relative to inner layer in DWCNTs.

![](./images/813313146641973251_3.jpg)

Fig. 3. Half model of DWCNTs with the extension of outer layer in MD simulation.

bonded by $sp^2$ hybridized electrons. However, when a cross covalent link is established on the carbon atoms between different layers, the atomistic interactions of the carbon atoms in terms of $sp^3$ hybridized electrons were considered in our MD simulation.

### 2.2. Atomistic interactions between adjacent graphene layers in DWCNTs

The interatomistic intensity of adjacent graphene layers was evaluated by pulling the outer layer of DWCNTs from both sides relative to the inner layer as shown in Fig. 2. It is noted that the intention of such configuration shown in Fig. 2 is to simulate the deformed behavior of DWCNTs when the nanocomposites with embedded DWCNTs is subjected to tensile loading. Because of the aspect of symmetry, only half model with a fixed boundary condition in the middle section, as shown in Fig. 3, was adopted in the MD simulation. In other words, the carbon atoms located in the middle section of DWCNTs were constrained during the simulation. When the outer layer was elongated monotonically, the reaction force in the inner layer was calculated accordingly. The intensity of reaction force in the inner layer corresponding to the extension of the outer layer was regarded as an index of the intensity of interfacial adhesion for the two neighboring graphene layers. The extension process of the outer layer was performed in MD simulation. The equilibrated molecular structure with minimized energy was accomplished from the canonical (NVT) ensemble with time increments of 1 fs for 100 ps (the total iteration steps are 100,000). It is noted that canonical (NVT) ensemble stands for that the volume, and temperature is fixed during the simulation [15]. Fig. 4 illustrated the variation of potential energy during the canonical (NVT) ensemble. After 10 ps, a stable value of potential energy was attained, indicating that an atomistic model of DWCNTs with energy minimization was achieved from the NVT ensemble. Subsequently, the carbon atoms located at the edge of the outer layer were extended 0.02 Å and then fixed in the new position. The NVT ensemble was conducted again for 50 ps, and the energy minimization configuration of DWCNTs with outer layer extended relative to the inner layer was updated. Fig. 5 shows the energy history of the DWCNTs in the NVT ensemble, and it seems that the potential energy attains a stable condition after 10 ps. Once the deformed configuration of DWCNTs is achieved, the reaction force (unbalanced force) acting on the atoms of inner layer located at a fixed end was calculated. The resultant force "F" acting on the inner wall was then derived as the following:

$$
F = \sum_{i=1}^{n} f_{i} \tag{2}
$$

where $n$ is the number of atoms at the fixed end of the inner layer, and $f_i$ is the corresponding reaction force for each atom. The outer

![](./images/813313146641973251_4.jpg)

Fig. 4. Variation of potential energy in NVT ensemble.

![](./images/813313146641973251_5.jpg)

Fig. 5. Variation of potential energy during the extension of outer layer.

![](./images/813313146641973251_6.jpg)

Fig. 6. Geometric conversion of DWCNTs molecular structure into an equivalent continuum solid. (a) Discrete molecular structures and (b) equivalent continuum solid.

<table>
<caption>Table 1<br>Material properties of DWCNTs.</caption>
<thead>
<tr>
<th></th>
<th>Outer layer</th>
<th>Inner layer</th>
</tr>
</thead>
<tbody>
<tr>
<td>Modulus of elasticity (GPa)</td>
<td>788.5</td>
<td>739.3</td>
</tr>
<tr>
<td>Poisson's ratio</td>
<td>0.2732</td>
<td>0.2822</td>
</tr>
</tbody>
</table>

layer was extended proportionally with the increment of $0.02\ \text{\AA}$ in MD simulation. For each extension, the configuration of DWCNTs was updated, and concomitantly, the reaction force in the inner layer was calculated. Eventually, the extension versus reaction curve during the elongation for the atomistic structures of DWCNTs was established. The MD simulations were conducted using a DL-POLY package [16] with a homemade subroutine for the calculation of the reaction force in the inner layer.

### 3. Equivalent continuum solid of DWCNTs

Based on the extension versus reaction curves of DWCNTs obtained from MD simulation, a two-layer hollow equivalent solid was proposed to represent the atomistic model of DWCNTs. The equivalence of the continuum model to the atomistic model is not only rooted in the interfacial properties of graphene layers, but it is also in the geometric configuration. For the compatibility of the geometric configuration, the atomistic configurations of DWCNTs with the diameters of the outer and inner layers being $D_1$ and $D_2$ were converted equivalently into its continuum counterpart as shown in Fig. 6. For (3,3) (8,8) DWCNTs, the diameters of $D_1$ and $D_2$ are $10.85\ \text{\AA}$ and $4.07\ \text{\AA}$, respectively. It is noted that "h" indicates the interlayer spacing of the graphene walls and is equal to 0.34 nm [11]. The geometric parameter $R_{1o}$, $R_{1i}$, and $R_{2i}$ representing the inner and outer radius of each layer in the continuum solid can be expressed in terms of the atomistic configuration as $R_{1o}=(D_1+h)/2$, $R_{1i}=(D_2+h)/2$, and $R_{2i}=(D_2-h)/2$. In the continuum solid, it was assumed that the thickness of each layer is equal to 0.34 nm such that no gap exists between the adjacent layers.

For the compatibility of interfacial properties, the interaction of the neighboring layers in the hollow equivalent solid was modeled with spring elements. It is noted that the corresponding spring constants in the equivalent solid were determined so that the extension versus reaction curve derived from the continuum model would coincide with that obtained from the MD simulation. Basically, the spring constants corresponding to two different interfacial adhesions, i.e., vdW interaction and covalent bonding, have to be determined individually in the equivalent solid. Moreover, the material properties of DWCNTs used in the continuum model were also obtained from the MD simulation. The detail procedure can be found elsewhere [17], and the results for the (3,3) and (8,8) CNTs are listed, respectively, in Table 1. Subsequently, a 3-D finite element method (FEM) model where the interaction of neighboring layers was described with spring element was developed to represent the discrete atomistic structure of the DWCNTs. Basically, the FEM analysis was conducted in the commercial software ANSYS. In the FEM model as shown in Fig. 7, the graphene layers were modeled by 8-node solid elements (solid45), and the interface between the layer was simulated with two-node spring elements (combin39). In fact, the two nodes in the spring element are geometrically coincided with each other; however, they belong to two different elements, i.e., outer layer (layer 1) and inner layer (layer 2). The spring elements with two nodes were deployed homogeneously on the interface, which provides the connection between the two graphene layers. The deployment of the spring element on the interface between two solid elements is shown in Fig. 8. It is noted that in the employment of spring element, the 1-D option was selected, and meanwhile the orientation of the elements was specified in the axial direction ($x$ direction). Therefore, only the relative movement along axial direction would be experienced by the axial springs with spring constants $Kx$. In addition, in order to prevent the interpenetration between the two layers, the contact elements (CONTA 173 and TARGE 170) were employed on the contact surfaces. The purpose of the establishment of equivalent continuum model is to correlate the axial extension of the DWCNTs obtained from MD simulation, so the lateral confinement effect due to Poisson's ratio was lumped into the spring element in our FEM model. The outer layer was then gradually extended in the FEM analysis, and for each increment, the reaction force in the inner layer was evaluated. The associated spring constants in FEM model were determined so that the extension of outer layer versus the reaction force of inner layer curves derived from the continuum model would match with that obtained from the MD simulation. Once the spring constant is

![](./images/813313146641973251_7.jpg)

Fig. 7. Equivalent continuum solid model with extension of outer layer.

![](./images/813313146641973251_8.jpg)

Fig. 8. Deployment of spring element on the equivalent solid.

![](./images/813313146641973251_9.jpg)

Fig. 9. Reaction force versus extension curve of atomistic model obtained from MD simulation (a) DWCNTs and (b) DWCNTs with covalent bonds.

decided, the two-layer hollow FEM model was embedded in the matrix to form a continuum model of nanocomposites.

Fig. 9 demonstrates the correlation of reaction force with exten- sion obtained from MD simulation for the DWCNTs with or without covalent bonds. The presence of covalent bonds on the interface seems to effectively raise the reaction force generated

![](./images/813313146641973251_10.jpg)

Fig. 10. Correspondence of the reaction force versus extension curves obtained respectively from atomistic model and equivalent continuum model (a) DWCNTs and (b) DWCNTs with covalent bonds.

![](./images/813313146641973251_11.jpg)

Fig. 11. Spring constants Kx used in the nonlinear spring element.

in the inner layer, resulting in the improvement of load transfer efficiency. In addition, it was found that for DWCNTs with a

![](./images/813313146641973251_12.jpg)

covalent bond, the reaction forces in the inner layer are basically proportional to the elongation of outer layer. Associated with the same extension, the longer DWCNTs exhibits less reaction force in the inner layer. This occurs because for the same elongation of the outer layer, the longer DWCNTs have less strain deformation as compared to the shorter DWCNTs, leading to less relative move- ment as well as less stress transfer to the inner layer. Moreover, be- cause the same number of covalent bonds was constructed in the DWCNTs, the longer the CNTs, the lower the covalent bond density. Conversely, for the DWCNTs without a covalent bond, the reaction force curves are linear in the early portion and deviate from the lin- ear curve as the extension is increasing. This nonlinearity is attrib- uted to the nonlinear characteristics of vdW interactions shown in Eq. (1).

The coincidence of the reaction curves obtained from the MD simulation and the equivalent continuum model for the DWCNTs with length of $984\,\mathring{A}$ was compared in Fig. 10. It is shown that the kinking curve in atomistic mode is modeled by a nonlinear smooth curve in the equivalent model and the tendencies of both curves are quite close. Thus, the relative sliding behaviors between the neighboring layers in DWCNTs can be described by the equiv- alent continuum model with the embedded spring elements. The

![](./images/813313146641973251_13.jpg)

nonlinear spring constant used in the spring element for the DWCNTs with length of 984 Å is illustrated in Fig. 11. In light of forgoing comparisons, the atomistic properties of DWCNTs can be completely represented by the equivalent continuum solid. It should be noted that the values of spring constants in the equiva- lent continuum DWCNTs are relied on the length and the adhesion properties of DWCNTs. Therefore, MD simulation is still required in the multi-scale simulation in order that the spring constants in the equivalent continuum model can be properly characterized.

## 4. Continuum finite element analysis model of nanocomposites

A cylindrical representative volume element (RVE) containing the hollow cylindrical continuum solid (denoting the CNTs) and ma- trix phase was employed in the FEM continuum analysis for the evaluation of load transfer efficiency. Because of the cylindrical attribute of the RVE, a half-quarter of 3D FEA model was employed in the evaluation of the load transfer on the DWCNTs nanocompos- ites. Fig. 12 demonstrates the continuum model for the nanocom- posites where the matrix was modeled by an 8-node solid element with an elastic modulus of 3 GPa. For the (3,3) (8,8) DWCNTs, the geometric parameters of the inner and outer layers are $R_{1o}=7.125$ Å, $R_{1i}=3.735$ Å, and $R_{2i}=0.335$ Å, respectively. By assuming the CNTs volume fraction in the nanocomposites is around 1%, the radius of the RVE was estimated as $R_{m}=71.25$ Å. It is noted that in Fig. 12, the DWCNTs is perfectly bonded to the ma- trix, and the interface between the graphite layers is modeled using the spring element as previously described. By applying a loading $\sigma_{0}$ ($\sigma_{0}=100$ MPa) on the matrix, the corresponding stress distribution on the layer-1 (outer layer) and layer-2 (inner layer) can be evalu- ated directly from FEA analysis. The peculiarity of the model is that the inherent atomistic interactions existing between the graphite layers in DWCNTs was successfully implanted in the continuum nanocomposites. In addition, the length effect of DWCNTs as well as interfacial properties in the load transfer efficiency can be directly extracted from the continuum nanocomposites model.

## 5. Results and discussion

Fig. 13 shows the axial stress distribution in layer 1 and layer 2 for the DWCNTs with vdW interactions in terms of four different lengths. It can be seen that the stress in both layers increases from the CNTs' ends, but the increasing rate for layer 2 is much less than that in layer 1. With the increment of the CNTs length, the stress in layer 1 increases and eventually attains a saturated value, however, layer 2 is still in the low stress level. Thus, when DWCNTs is

![](./images/813313146641973251_14.jpg)

Fig. 14. Stress distribution in the DWCNTs with covalent bond (a) $L=80$ Å, (b) $L=162$ Å, (c) $L=295$ Å and (d) $L=492$ Å.

employed as reinforcement in nanocomposites, most loading is still carried by the outer layer, and only little loading is transferred into the inner layer. Similar results were also presented in Ref. [5]. The phenomena further denote that the vdW interaction between the graphene layers cannot provide substantial adhesion to effec- tively transfer the load from the outer layer to the inner layer.

For the DWCNTs with covalent bonds, the stress distribution for two graphene layers associated with different lengths is shown in Fig. 14. It can be seen that even in the shortest case of DWCNTs (80 Å), the inner layer can still sustain the stress. As compared to the vdW interactions, the covalent bonds can efficiently enhance load transfer efficiency from the matrix to the outer layer and far- ther into the inner layer. Moreover, as the length of DWCNTs in- crease, the stress level in layer 2 increases accordingly. When the length achieves 492 Å, the stress in the outer layer is almost satu- rated; meanwhile, the inner layer also exhibits the highest stress among the four cases. In order to quantify the load transfer effi- ciency of DWCNTs, the concept of effective length is introduced as [10]:

$$
L_{e f f}=\frac{\int_{0}^{L}\left(\sigma_{f 1}+\sigma_{f 2}\right) d y}{2 \sigma_{f}^{s}} \tag{3}
$$

where $\sigma_{f 1}, \sigma_{f 2}$ indicate the axial stress in layer 1 and layer 2, respec tively, and $\sigma_{f}^{s}$ is the saturated stress of the SWCNTs embedded in matrix. The effective length calculated by Eq. (3) represents the length in which the equivalent amount of the saturated load is carried. It should be noted that the definition of effective length is different from that of the critical length which is often used in the micromechanical mechanics. The critical length denotes the length where the load transfer from the matrix to the fiber until the tensile strength of fiber is attained [18]. In the nanocomposites's design, the fundamental perception is to facilitate the load applied on the materials being efficiently transferred into the reinforcement and eventually carried by the reinforcement. Indeed, the effective length can be regarded as an index to estimate the effectiveness of the reinforcement. When the effective length is increasing, it reveals that the load carrying efficiency of the reinforcement is increasing, and the overall mechanical properties of the nanocomposites can be enhanced accordingly. In comparison, the effective length of SWCNTs was also calculated as:

$$
L_{e f f}=\frac{\int_{0}^{L} \sigma_{f} d y}{\sigma_{f}^{s}} \tag{4}
$$

where $\sigma_{f}$ is the axial stress in the SWCNTs, and $\sigma_{f}^{s}$ is the correspond ing saturated stress as indicated in Eq. (3). Here, (8,8) SWCNTs was adopted as an example in the simulation. Fig. 15 illustrates the load transfer efficiency of SWCNTs and DWCNTs with covalent bond. It is obvious that the covalent bond can effectively improve the load transfer efficiency of DWCNTs. In addition, the length is another essential factor to improve the load transfer efficiency in CNTs nanocomposites. It should be noted that the increment of the CNTs' length can effectively improve the load transfer efficiency in the outermost layers, nevertheless, for the inner layers, the improve- ment is minor. Thus, as compared to SWCNTs, DWCNTs still illus- trate less load transfer efficiency even if there is covalent bond between the graphene layers. On the other hand, for the MWCNTs, because most of inner layers would not bear loading, the corre- sponding load transfer efficiency of MWCNTs decreases accordingly as the number of the inner layers increases. Such decreasing behav- ior was also predicted by Zalamea et al. [4]. Consequently, for the purpose of reinforcement, SWCNTs should be considered as a suit- able additive rather than DWCNTs/MWCNTs in nanocomposites.

![](./images/813313146641973251_15.jpg)
Fig. 15. Effective length of SWCNTs, DWCNTs and DWCNTs with covalent bonds.

It is noted that the main contribution of the study is to provide an approach converting the atomistic structures of DWCNTs into an equivalent continuum solid. In order to validate the above approach, we compared the load transfer efficiency of DWCNTS as well as the inner layer load carrying capacity with those pre- sented in literatures [4,5]. Basically, the phenomena that the load transfer efficiency in DWCNTs/MWCNTs is poor and the load bear- ing capacity in inner layers is low shown in literature are also dem- onstrated in our model. The fundamental agreement provides some validation of our current models.

## 6. Conclusions
An equivalent cylindrical solid to represent the atomistic attri- butes of DWCNTs was proposed in this study. The atomistic interac- tion of adjacent graphite layers in DWCNTs was characterized using MD simulation based on which a spring element was introduced in the continuum equivalent solid to demonstrate the interfacial prop- erties of DWCNTs. Subsequently, the proposed continuum solid (de- notes DWCNTs) was embedded in the matrix to form DWCNTs nanocomposites (continuum model), and the load transfer effi- ciency within the DWCNTs was determined from FEM analysis. For the demonstration purpose, the DWCNTs with four different lengths were considered in the investigation. Analysis results illus- trate that the increment of CNTs' length can effectively improve the load transfer efficiency in the outermost layers, nevertheless, for the inner layers, the enhancement is miniature. On the other hand, when the covalent bonds between the adjacent graphene layers are crafted, the load carrying capacity in the inner layer increases as so does the load transfer efficiency of DWCNTs. As compared to SWCNTs, the DWCNTs still possess the less capacity of load transfer efficiency even though there are covalent bonds generated in the DWCNTs.

## References
[1] Thostenson ET, Li C, Chou TW. Nanocomposites in context. Compos Sci Technol 2005;65(3-4):491-516.
[2] Lau KT, Gu C, Hui D. A critical review on nanotube and nanotube/nanoclay related polymer composite materials. Composite Part B: Eng 2006;37(6):425-36.
[3] Schadler LS, Giannaris SC, Ajayan PM. Load transfer in carbon nanotube epoxy composites. Appl Phys Lett 1998;73(26):3842-4.
[4] Zalamea L, Kim H, Pipes RB. Stress transfer in multi-walled carbon nanotubes. Compos Sci Technol 2007;67(15-16):3425-33.
[5] Shen GA, Namilae S, Chandra N. Load transfer issues in the tensile and compressive behavior of multiwall carbon nanotubes. Mater Sci Eng A2006;429(1-2):66-73.
[6] Shokrieh MM, Rafiee R. Investigation of nanotube length effect on the reinforcement efficiency in carbon nanotube based composites. Compos Struct 2010;92(10):2415-20.

[7] Shokrieh MM, Rafiee R. On the tensile behavior of an embedded carbon nanotube in polymer matrix with non-bonded interphase region. Compos Struct 2010;92(3):647-52.

[8] Gao XL, Li K. A shear-lag model for carbon nanotube-reinforced polymer composites. Int J Solids Struct 2005;42(5-6):1649-67.

[9] Li C, Chou TW. A structural mechanics approach for the analysis of carbon nanotubes. Int J Solids Struct 2003;40(10):2487-99.

[10] Tsai JL, Lu TC. Investigating the load transfer efficiency in carbon nanotubes reinforced nanocomposites. Compos Struct 2009;90(2):172-9.

[11] Iijima S. Helical microtubules of graphitic carbon. Nature 1991;354:56-8.

[12] Rappe AK, Casewit CJ. Molecular mechanics across chemistry. Sausalito, California: University Science Books; 1997.

[13] Cornell WD, Cieplak P, Bayly CI, Gould IR, Merz KM, Ferguson DM, et al. A second generation force field for the simulation of proteins, nucleic acids, and organic molecules. J Am Chem Soc 1995;117(19):5179-97.

[14] Battezzati L, Pisani C, Ricca F. Equilibrium conformation and surface motion of hydrocarbon molecules physisorbed on graphite. J Chem Soc 1975;71:1629-39.

[15] Allen MP, Tildesley DJ. Computer simulation of liquids. Oxford: Oxford university press; 1989.

[16] Smith W, Forester TR. The DL_POLY-2.13 User Manual; 2001.

[17] Tsai JL, Tu JF. Characterizing mechanical properties of graphite using molecular dynamics simulation. Mater Des 2010;31:194-9.

[18] Gibson RF. Principles of composite material mechanics. CRC Press; 2007.