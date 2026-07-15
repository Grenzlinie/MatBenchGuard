A multilevel approach to modeling of porous bioceramics

Valentina A. Mikushina, and Yury N. Sidorenko

Citation: AIP Conference Proceedings 1683, 020150 (2015); doi: 10.1063/1.4932840
View online: http://dx.doi.org/10.1063/1.4932840
View Table of Contents: http://aip.scitation.org/toc/apc/1683/1
Published by the American Institute of Physics

![](./images/814583053023182850_1.jpg)

# A Multilevel Approach to Modeling of Porous Bioceramics

Valentina A. Mikushina $^{1, a)}$ and Yury N. Sidorenko $^{1, b)}$

$^{1}$ National Research Tomsk State University, Tomsk, 634050 Russia

a)Corresponding author: mikushina_93@mail.ru
b)yus911@rambler.ru

Abstract. The paper is devoted to discussion of multiscale models of heterogeneous materials using principles. The specificity of approach considered is the using of geometrical model of composites representative volume, which must be generated with taking the materials reinforcement structure into account. In framework of such model may be considered different physical processes which have influence on the effective mechanical properties of composite, in particular, the process of damage accumulation. It is shown that such approach can be used to prediction the value of composite macroscopic ultimate strength. As an example discussed the particular problem of the study the mechanical properties of biocomposite representing porous ceramics matrix filled with cortical bones tissue.

## INTRODUCTION

The development of modern medicine is connected with using products from materials, the technologies of which have been developed in recent decades, particularly with the use of powder metallurgy. These are metals and alloys, composite and other materials. Such materials are used as a "substitute" for damaged or destroyed fragments of human bone tissues in dentistry, oral surgery, etc. The main requirement for such materials is their biocompatibility with living tissues of the human body. One such factor ensuring the biocompatibility of materials is a high-porous structure. The presence of a developed system of pores, and channels which connect them, allows the living tissues of a human body to "grow" into the ceramic product. In this case there is gradual formation of hard bone tissue in pores. So it is possible to speak about the formation of a specific material (biocomposite), where the ceramic is its matrix, and the filler is the biological tissue of a living organism [1]. An example of such a material is highly porous ceramic based on zirconium dioxide [2], characterized by its high strength among other properties.

The success of using such materials in medicine as well as in other applications is largely determined by the completeness of information on their biological and mechanical properties. For obtaining such information, methods of computer modeling are now used. The accuracy of these methods directly depends on the quality of the computer models of biomaterials.

When solving engineering problems such biocomposites as a homogeneous material can be considered. This way of describing characteristics of materials is acceptable, as there is a significant difference between the characteristic sizes of implants and elements of the porous structure of material. However, the mechanical action of the material at this level (the mechanical characteristics of volume materials of the macroscopic level) is determined by the presence and parameters of its porous structure. To study the behavior of the material at the level of pores it is necessary to take into account volumes of the materials, comparable to the size of the elements of porous structure, i.e. the volume of the mesoscopic level. Thus, when modeling biocompatible ceramic materials, using a multilevel approach can be most effective [3-5]. In particular, this approach is useful for estimating the strength characteristic of such materials [6].

According to this approach several levels of modeling can be identified. In this article three levels of modeling materials will be shown: the microscale—for volumes belonging to one or another component of material; the mesoscale—for local volumes of materials, the choice of sizes occurs according to local aspects of reinforcement structure; the macroscale—for representative (effectively—homogeneous) volumes of the composite.

Advanced Materials with Hierarchical Structure for New Technologies and Reliable Structures
AIP Conf. Proc. 1683, 020150-1-020150-4; doi: 10.1063/1.4932840
© 2015 AIP Publishing LLC 978-0-7354-1330-6/$30.00

020150-1

![](./images/814583053023182850_2.jpg)
(a)

![](./images/814583053023182850_3.jpg)
(b)

FIGURE 1. Models of biocomposite structure: (a) "pores" model (type 1), (b) "pores" + "canals" model (type 2)

In making an assessment of the mechanical properties of the composite multi-level model, it is necessary to take into account the possibility of damage to the volumes of the material on each scale level, as well as provide the ability to transmit information about the loading conditions and the state of different-scale volumes between the levels of the model.

# THE MULTILEVEL MODEL OF BIOCERAMICS

In this paper model composite material (CM) is considered, where porous ceramics is its matrix and the filler is cortical bone. Based on the above, the composite material was considered at several levels: the macro-, meso- and microlevels.

On the macro level CM is quasihomogeneous. The properties of CM at this level according to space coordinates change quite slowly, which makes them permanent in some limited surroundings of the selected points. Properties at this level are characterized by some effective values, representing the result of compilation of information about the behavior of the material obtained at the mesolevel. The mesovolume is a fragment of a piecewise-homogeneous (porous) environment for which are clearly defined the distribution of the components and loading conditions [7–9]. For the mesovolume there is a concept of locally-effective properties, which are defined as the average (effective) for the selected limited fragment of a heterogeneous environment. On the micro level there is such a volume, the sizes of which are much larger than the interatomic distances, and at the same time smaller than the characteristic sizes of the structural components of the composite. It is believed that for such a volume, the locations of continuum mechanics are acceptable, i.e. the hypothesis of continuity and homogeneity hypothesis are accomplished for it, and mathematical apparatus of integral and differential calculus can be used for its description. The properties of the material at this level are described by equations of the mechanics of the deformed solid body which include equilibrium equations, Cauchy (geometric equations) and equations of state of the environment [10].

In making an assessment of the strength at the macro level an approach is used based on the percolation theory. In assessing the strength of these states, the original (intact) and the final state (destroyed) may be considered [11, 12]. In accordance with the concepts of the clustering analysis, the points which are in the same state can be clustered. It is believed that the criterion of transfer of the entire system to a new state (the condition of macroscopic fracture) is formation of the connective damage cluster.

The numerical realization of approach discussed is based on the using of geometrical model of composite's porous structure within representative volume of material. In case of 2-dimensional realization such a model represents by self a square shape cross section of composite randomly filled with circle shaped inclusions (pores). For the purpose of the local properties' determination the representative set of random points is taken within geometrical model. For each of these points the finite elements "model describing pores" relative positions in small vicinity of particular point is build [13, 14]. All such models represent a set of mesoscopic scale level's volumes of composite.

020150-2

![](./images/814583053023182850_4.jpg)
![](./images/814583053023182850_5.jpg)

FIGURE 2. The main results of numerical simulation: (a) Weibull's distributions of local elastic module (1—structure type 1,
2—structure type 2), (b) damage accumulation in bioceramic components depending on the strain value

Each separate finite element of FEM-model can be considered in the framework of approach discussed as a
volume of microscopic scale level. The boundary conditions for the FEM-model of meso-volume correspond to
chosen type of loading.

# THE AIM OF THE RESEARCH

The aim of the study is to research the framework of the described multilevel model of biocomposite, the impact
of accounting for various elements of the porous structure of the material on the results of modeling of its
mechanical properties. Large pores and connecting channels are considered as elements of the porous structure. The
problem is solved in two-dimensional formulation. Thus large pores in the geometric model are represented as a
circular inclusion of the diameter D, and the channels are circular inclusions of the diameter $d = kD$, where $k < 1)$.
Both types of geometrical models are shown on the Fig. 1. The mechanical properties of matrix correspond to
ceramics, properties of "pores" and "canals"—to cortical bone tissue [15, 16].

# THE RESULTS OF COMPUTER MODELING

There are two types of geometric models of biocomposite: the first model takes into account only large pores in
the structure of porous biocomposite; in the second model the availability of additional interporous channels is
considered. The first model (model of type 1) is shown in the Fig. 1a. The pores are filled with bone tissue,
described in the model as circular inclusions, randomly placed within the model structure. The second model (model
of type 2) is shown in the Fig. 1b. The place of the inclusions is random. The ratio of channel diameter to the
diameter of the pore is $1:5$. The size of the square side comprising a geometric model exceeds the diameter of a
pore 50 times. The actual object sizes of the geometric model: pores—200 $\mu$m, channels—40 $\mu$m. The sizes of the
model were chosen based on the requirements of its geometric representation.

The volume fraction of large pores in both models is 32%, the volume content of the second channel model 8%
(thus, the total porosity value in the second case is 40%).

As a result of the calculations the values of the effective elastic modules were obtained, in the first case ($C =$
32%) without channels—91 GPa, while in the second case with the channels ($C = 40\%$)—76 GPa.

In Fig. 2a is shown the function of distribution of the local elastic modules for the model structures of both types
of biocomposite. The distribution functions are approximated according to the law of Weibull [17].

Figure 2b shows that the presence of channels in the second structure greatly influences the distribution of
Weibull. The second structure ($S = 40\%$) compared with the first ($S = 32\%$) is more homogeneous and the average
value of the effective modules of elasticity is smaller.

Also, the maximum amount of deformation was defined in the research. For $S = 32\%$ it is 0.13% and $S = 40\%$—
0.15%. The imprecision in determining the ultimate deformation in the calculation does not exceed 0.01%. For these
values, research was conducted on the development of the process of accumulation of damage. Figure 4 shows the
accumulation of damages in bioceramic components ($q_k$) depending on the strain value.

020150-3

Figure 4 shows that the structure containing the channels and pores is more resistant to the accumulation of damage, indicating the need to account for all elements of the structure biocomposite porosity when building its calculation model. The process of accumulation in bone tissue develops more intensively than in the ceramic matrix. By the time of formation connecting cluster, the proportion of damaged volume bone tissue reaches 70%, and the matrix—40%.

# CONCLUSION

The results of numerical modeling have shown the effectiveness of a multilevel approach to modeling the mechanical properties of the biocompatible composite. The rates of maximum deformation biocomposites were obtained. It has been shown that the limiting deformations of model materials are sufficiently close and constitute 0.13% (type 1, porosity 32%) and 0.15% (type 2, porosity 40%). It has also been shown that the process of accumulation of damage in the bone tissue develops more intensively than in the ceramic matrix and by the time of formation of a connecting cluster, the proportion of damaged volume of bone tissue reaches 70%, and the matrix—40%. According to the results, the presence of channels in the structure of porosity of the composite leads to a reduction of its effective elastic modules: no damage 16%, and at the moment of formation connecting cluster damage 19%.

# REFERENCES

1.  S. P. Buyakova, I. A. Khlusov, and S. N. Kulkov, Phys. Mesomech. 7(Spec. Uss., Part 1), 127–130 (2004).
2.  S. P. Buyakova and S. N. Kulkov, Vestnik TGU 23, 89–94 (2004).
3.  P. V. Trusov, P. S. Volegov, and A. Yu. Yanz, *Phys. Mesomech.* 17(4), 349–355 (2014).
4.  V. E. Egorushkin, V. E. Panin, and A. V. Panin, *Phys. Mesomech.* 18(1), 8–12 (2015).
5.  E. J. Pineda, B. A. Bednarcyk, S. M. Arnold, Achieving ICME with Multiscale Modeling: The Effects of ConstituentProperties and Processing on the Performanceof Laminated Polymer Matrix Composite Structures,” in *AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference, 55th* (National Harbor, Maryland, USA, 2014), p. 21.
6.  Yu. V. Sovetova, Yu. N. Sidorenko, and V. A. Skripnyak, Phys. Mesomech. 16, 59–65 (2013).
7.  Yu. N. Sidorenko, PhD Dissertation, Tomsk State University, Tomsk, 2004.
8.  A. Wang and C. Yan, *Composites. A* 36, 1335–1346 (2005).
9.  A. Wongsto and S. Li, *Composites. A* 36, 1246–1266 (2005).
10. S. P. Timoshenko and J. N. Goodier, *Theory of Elasticity* (McGraw-Hill, New York, 1970).
11. L. J. Broutman and R. H. Kork, *Composite Materials, vol. 2: Mechanics of Composite Materials* (Academoc Press, New York, 1974).
12. S. Salekeen and D. L. Jones, *Composite Struct.* 79, 119–124 (2007).
13. O. C. Zienkiewicz and R. L. Taylor, *The Finite Element Method for Solid and Structural Mechanics* (McGraw Hill, New York, 1967).
14. L. J. Segerlind, *Applied Finite Element Analysis* (New York, 1984).
15. S. M. Barinov, Uspekhi Khimii 79(1), 15–30 (2010).
16. A. I. Matveeva, A. G. Ivanov, R. Sh. Gvetadze, et al., Stomatologija 76(5), 44–48 (1997).
17. A. S. Kobayashi, *Handbook on Experimental Mechanics* (Prentice-Hall, New Jersey, 1987).

020150-4