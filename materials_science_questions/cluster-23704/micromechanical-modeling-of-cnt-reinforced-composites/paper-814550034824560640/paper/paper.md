Studies on Effective Elastic Properties of CNT/Nano-Clay Reinforced Polymer Hybrid
Composite

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 IOP Conf. Ser.: Mater. Sci. Eng. 115 012007

(http://iopscience.iop.org/1757-899X/115/1/012007)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 117.255.247.223
This content was downloaded on 14/04/2016 at 18:27

Please note that terms and conditions apply.

5th National Conference on Processing and Characterization of Materials
IOP Publishing
IOP Conf. Series: Materials Science and Engineering 115 (2016) 012007  doi:10.1088/1757-899X/115/1/012007

# Studies on Effective Elastic Properties of CNT/Nano-Clay Reinforced Polymer Hybrid Composite

Arvind Kumar Thakur¹, Puneet Kumar²,J. Srinivas³
¹ Master student, ² Research scholar, ³ Associate Professor
Department of Mechanical Engineering, National Institute of Technology Rourkela,
Rourkela-769008, Odisha, India

*E-mail: srin07@yahoo.co.in, Phone: +91661-2462503

Abstract.This paper presents a computational approach to predict elastic propertiesof hybrid nano-composite material prepared by adding nano-clayplatelets to conventional CNT-reinforced epoxy system. In comparison to polymers alone/single-fiber reinforced polymers, if an additional fiber is added to the composite structure, it was found a drastic improvement in resultant properties. In this regard, effective elastic moduli of a hybrid nano composite are determined by using finite element (FE) model with square representative volume element (RVE). Continuum mechanics based homogenization of the nano-filler reinforced composite is considered for evaluating the volumetric average of the stresses and the strains under different periodic boundary conditions.A three phase Halpin-Tsai approach is selected to obtain the analytical result based on micromechanical modeling. The effect of the volume fractions of CNTs and nano-clay platelets on the mechanical behavior is studied. Two different RVEs of nano-clay platelets were used to investigate the influence of nano-filler geometry on composite properties. The combination of high aspect ratio of CNTs and larger surface area of clay platelets contribute to the stiffening effect of the hybrid samples. Results of analysis are validated with Halpin-Tsai empirical formulae.

Keywords:Nano-clay, CNT, Hybrid composite, FEM, Halpin-Tsai, RVE.

## 1. Introduction
Polymers with suitable and proper nano filler have emerged as an advanced polymeric composites system which shows prospective applications in the field of automotive, aerospace, packaging and construction industries [1]. Compared to conventional and micro fillers, carbon nanotubes (CNTs) reinforced polymers have gained increased interest in both industrial and academic fields, specifically utilizing their high aspect ratio and tremendous mechanical strength of CNTs [2-4]. But practical point of view CNT reinforced polymer composite materials have limited applications because of poor load transfer through interfacial region and agglomerations of CNTs [5-6]. Surface treatment and chemical functionalization are few effective techniques to enhance the interfacial adhesion and dispersion ability of CNTs [7-8]. Similarly, polymer materials reinforced with Nano fillers such as layered silicates (clay) [9] are prominent substitute for conventional composite materials. Intuitively, polymer/clay Nano composite provide best performance with high degree of clay exfoliation. With the time, rapid advancement have taken place in material science and technology and developed new generation multi-scale, multifunctional nanostructured hybrid polymer composite reinforced by CNTs and other nano reinforcements. Therefore, it becomes necessary to investigate the reinforcing mechanism of hybrid polymer composite which provides basic foundation for modeling and design of these high performances composite. Clay-CNT/polymer matrix hybrid composite [10-14] is one of the most widely used materials due to their light weight, long durability, high strength, chemical resistant, and so forth. Great deals of analytical and

![](./images/814550034824560640_1.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd

numerical works have been carried out to investigate the mechanical properties of CNTs reinforced polymer [15-16] and clay reinforced polymer [17] composite separately. Among the analytical techniques employed to obtain effective properties of composite, most of the researchers used the rule of mixture and Halpin-Tsai equations to modeling nanocomposite. However, few modifications have been employed to traditional theories to account the irregular geometry and distribution of nanostructured reinforcement at nano-scale for hybrid composite. Till to date no work found in literature related to modeling of clay- CNTs/polymer hybrid composite, however few articles are investigated numerical analysis of silica nanoparticle-MWCNT hybrid composite [18]. Jia eta al. [19] prepared a novel nanostructure hybrid (SiO2-MWCNTs) polymer composite, in which nano silica particle are grown over CNTs. Rahmanian et al.[20] demonstrate the FE modeling of carbon nanotube silica reinforced epoxy composite considering that CNTs are grown over micro silica particle. In most of work related to hybrid composite finite element method is an efficient and preferable numerical approach for investigating the reinforcing effect of different nano fillers on polymer composite. This method demonstrates the continuum representation of nano filler structure and polymer matrix.

Since CNTs/nano-clay hybrid showed prominent reinforcement on polymer matrix than pure CNTs as reported in previous work, there is a great potential in preparing new generation high performance composite. In present work, finite element method is used to predict the elastic behavior of epoxy composite reinforce by CNTs and nano-clay platelets. Specifically, to accurately describe geometry and reinforcing mechanism of CNTs and nano-clay platelets, the traditional theories of the rule of mixtures and Halpin–Tsai equations were properly corrected and a finite element approach based on nano-scale representative volume element (RVE) model was built up. To better understand the stiffening effect of CNTs and nano-clay nanoparticles in hybrid polymer composite, the tensile modulus for CNT/nano- clay/epoxy composites predicted by three phase Halpin–Tsai equations, were compared with FEM outcomes.

## 2. Modeling of hybrid composite

Modelling of CNT and nano clay reinforced hybrid composite is presented in two steps. In first part illustrate the micromechanical modelling and second one numerical modelling (FEM).

### 2.1.Micromechanical modeling

To predict the mechanical properties of three phase polymer composite, Halpin-Tsai model and theory of micromechanics were applied in hierarchy. The rule of mixture are used to obtained the effective elastic modulus of effective clay particle and effective CNT fiber (as shown in figure 1) which include clay, CNT and interphase as follow,

$$E_{CP}=E_{clay}\alpha +E_{int}(1-\alpha)\ (1)$$

$$E_{CF}=E_{cnt}\beta +E_{int}(1-\beta)\tag{2}$$

Where E<sub>CP</sub> and E<sub>CF</sub> are the effective elastic modulus of clay particle and CNT fiber. $E_{clay}$, $E_{cnt}$, $\alpha$, $\beta$ are the elastic modulus and volume fractions of clay and CNT respectively.

![](./images/814550034824560640_2.jpg)

Fig. 1:- Representation of effective Clay particle and effective CNT fiber

To evaluate the elastic modulus of hybrid composite by combining effective particle and polymer (epoxy) by using modified Halpin-Tsai model as follow.

$$
\frac{P}{P_{m}}=\frac{1+\left(\varepsilon_{1} \eta_{C P} V_{C P}+\varepsilon_{2} \eta_{C F} V_{C F}\right)}{1-\left(\eta_{C P} V_{C P}+\eta_{C F} V_{C F}\right)} \tag{3}
$$

Where, P is the elastic property of hybrid composite and $P_{m}$ is elastic properties of polymer matrix.

$$
\eta_{C P}=\frac{\left(P_{C P} / P_{m}\right)-1}{\left(P_{C P} / P_{m}\right)+\varepsilon_{1}} \tag{4}
$$

$$
\eta_{C F}=\frac{\left(P_{C F} / P_{m}\right)-1}{\left(P_{C F} / P_{m}\right)+\varepsilon_{2}} \tag{5}
$$

$$
V_{m}+V_{C P}+V_{C F}=1 \tag{6}
$$

Where $V_{m}$, $V_{CP}$, and $V_{CF}$ are the volume fraction of polymer matrix, clay particle and CNT fiber respectively. $\varepsilon_{1}$, $\varepsilon_{2}$ are the reinforcement efficiency parameters for clay particle and CNT fiber. For, longitudinal elastic modulus $\varepsilon_{1}=(2 l / d_{p})$, $\varepsilon_{2}=(2 l / d)$ and for transverse elastic modulus $\varepsilon_{1}=\sqrt{3} \log (l / d_{p})$, $\varepsilon_{2}=1$. Where $d_{p}=d_{c}+2*d_{l}$, $d=2r$ are total thickness of effective clay particle and diameter of effective CNT fiber respectively. Figure 2 demonstrate the overall modeling procedure of CNT/nano-clay reinforced hybrid composite using micromechanical modeling.

![](./images/814550034824560640_3.jpg)

Fig. 2:- Modeling procedure of CNT/nano-clay reinforced hybrid composite

### 2.2.Constitutive relations and RVE model
For a transversely isotropic composite, the material behavior is based on only five independent constants. This concept is particularly ensured for regular fiber arrangement. In this work arbitrary fiber distributions are considered which results in transversely isotropic properties. By considering effective stiffness coefficient and average stress-strain value, the constitutive equations for the homogenized composite can be expressed as

$$
\left\{\begin{array}{l}
\overline{\sigma_{1}} \\
\overline{\sigma_{2}} \\
\overline{\sigma_{3}} \\
\overline{\sigma_{4}} \\
\overline{\sigma_{5}} \\
\overline{\sigma_{6}}
\end{array}\right\}=\left[\begin{array}{cccccc}
C_{11} & C_{12} & C_{12} & 0 & 0 & 0 \\
C_{12} & C_{22} & C_{23} & 0 & 0 & 0 \\
C_{12} & C_{23} & C_{22} & 0 & 0 & 0 \\
0 & 0 & 0 & \frac{1}{2}\left(C_{22}-C_{23}\right) & 0 & 0 \\
0 & 0 & 0 & 0 & C_{66} & 0 \\
0 & 0 & 0 & 0 & 0 & C_{66}
\end{array}\right]\left\{\begin{array}{l}
\overline{\varepsilon_{1}} \\
\overline{\varepsilon_{2}} \\
\overline{\varepsilon_{3}} \\
\overline{\gamma_{4}} \\
\overline{\gamma_{5}} \\
\overline{\gamma_{6}}
\end{array}\right\}
\tag{7}
$$

A representative volume element model can be used for the calculation of effective elastic coefficients by applying the appropriate periodic boundary conditions under the assumption of periodicity of fiber arrangement. Figure 3 shows the RVE model for CNT/nano-clay reinforced polymer composite.

![](./images/814550034824560640_4.jpg)

Fig. 3:- RVE of CNT/nano-clay reinforced polymer

The main advantage of the method is to replace the original composite with globally homogenized equivalent medium with same strain energy stored. To find out effective elastic coefficients such load cases with different boundary conditions must be applied that for a particular load case only one value in the strain field vector is non-zero and all other becomes zero. Then from corresponding column, the effective coefficients can be determined using calculated average stress value corresponding to unit strain.

### 2.3.Finite element modeling
A three dimensional multi-field elements is used for finite element calculations using FE package ANSYS. ANSYS Parametric Design Language (APDL) coding is used for modeling and applying the constraint equations. An algorithm was written in APDL for automated generation of RVE with aligns CNT and clay inside the polymer matrix. First 2-D model is generated in $X_2$-$X_3$ plane with circle as CNT and rectangle as clay and meshed with PLANE82 element. Further FE mesh is extruded in $X_1$ direction with SOLID185, 3-D element for meshing of RVE. Fibers surfaces are connected by Boolean operation with the aim of predicting the modulus of resin matrix reinforced with periodic nano-reinforcement of clay-CNTs. An interphase region is also considered here between CNT/polymer and clay/polymer to demonstrate the imperfect load transfer phenomenon at interfaces. The interphase region is meshed with random material properties lies between fiber and polymer matric properties. The generation of RVE can be controlled by some input parameters like size of RVE, CNT and nano-clay diameters for desired volumefraction. A certain minimum distance must be ensuring to generate suitable meshing of each part of model. From the numerical analysis, the effective elastic parameters of compositional material were estimated by relating boundary conditions.The calculation of effective coefficients in order to evaluate the overall stiffness matrix [C] of hybrid composite, RVE is subjected to an average strain. The six components of strain are applied by imposing the following boundary conditions on the displacement components.

$$
\begin{aligned}
&-a_{2} \leq x_{2} \leq a_{2} \\
u_{i}\left(a_{1}, x_{2}, x_{3}\right)-u_{i}\left(-a_{1}, x_{2}, x_{3}\right)=2 a_{1} \varepsilon_{i 1} &-a_{3} \leq x_{3} \leq a_{3} \\
&-a_{1} \leq x_{1} \leq a_{1} \\
u_{i}\left(x_{1}, a_{2}, x_{3}\right)-u_{i}\left(x_{1},-a_{2}, x_{3}\right)=2 a_{2} \varepsilon_{i 2} &-a_{3} \leq x_{3} \leq a_{3}
\end{aligned}
$$

$$
\begin{aligned}
& -a_{1} \leq x_{1} \leq a_{1} \\
u_{i}\left(x_{1}, x_{2}, a_{3}\right)-u_{i}\left(x_{1}, x_{2},-a_{3}\right)=2 a_{3} \varepsilon_{i 3} & -a_{2} \leq x_{2} \leq a_{2}
\end{aligned}
\tag{8}
$$

Here $2a_j\varepsilon_{ij}$ represents the applied displacement necessary to enforce a strain $\varepsilon_{ij}$ over a distance $2a_j$. The strain applied on boundary results in complex state of strain inside the RVE. So, volume average strain in the RVE equals to the applied strain, i.e.

$$
\overline{\varepsilon_{i j}}=\frac{1}{V} \int_{V} \varepsilon_{i j} d V=\varepsilon_{i j}
\tag{9}
$$

Considering hybrid composite as homogeneous material, the average stress-strain relationship can be written as

$$
\overline{\sigma_{\alpha}}=C_{\alpha \beta} \overline{\varepsilon_{\beta}}
\tag{10}
$$

By choosing a unit applied strain in one direction and imposing periodic boundary conditions on other directions, stress field can be computed. Whose average value over the volume gives the required components of stiffness matrix, one column at a time;

$$
C_{\alpha \beta}=\overline{\sigma_{\alpha}}=\frac{1}{V} \int_{V} \sigma_{\alpha}\left(x_{1}, x_{2}, x_{3}\right) d V
\tag{11}
$$

Where $\alpha, \beta$ are varying 1 to 3. Gauss-Legendre quadrature can be used for evaluating the volume integrals of a finite element. Commercial ANSYS have such type of capability to evaluate the average stress over the volume, element by element. Three loading cases are imposed to evaluate the all elastic coefficient of [C] for transversely isotropic composite. Figure 4 shows the meshing of RVEs used in finite element analysis.

![](./images/814550034824560640_5.jpg)

Fig. 4:- Meshing of (a) 1 CNT and 4 clay based RVE (b) 1 clay and 4 CNT based RVE

### 3. Results and discussion
By considering interphase parameters, elastic behavior of nanocomposite reinforced by CNTs and nano-clay plateletsis first analyzed. The advantages of nano-clay in CNT- reinforced polymer composite can be explained with reduction of interfacial reinforcing area of CNTs and enhancing the interfacial adhesion and dispersion of CNTs in polymer. In Fig.5 stress and strain distributionswere shown to explain the elastic behavior of CNT/nano-clay reinforced hybrid composite.

![](./images/814550034824560640_6.jpg)

Fig. 5:- (a) Stress and (b) strain distribution across cross-section of a RVE

The elastic and geometric property of each phase of RVE is listed in table 1. For simplification of calculation RVE length is considered as 50 nm.

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>Elastic Modulus (GPa)</th>
      <th>Poisson's ratio ($\mu$)</th>
      <th>Geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Epoxy</td>
      <td>2.026</td>
      <td>0.4</td>
      <td>25x25 nm</td>
    </tr>
    <tr>
      <td>CNT</td>
      <td>1054</td>
      <td>0.25</td>
      <td>r<sub>i</sub>=0.315 nm, r<sub>o</sub>=0.650</td>
    </tr>
    <tr>
      <td>Clay (MMT)</td>
      <td>178</td>
      <td>0.28</td>
      <td>t=4 nm, d<sub>c</sub>=1 nm</td>
    </tr>
    <tr>
      <td>CNT/polymer interphase</td>
      <td>16.10</td>
      <td>0.4</td>
      <td>r<sub>int</sub>=1.404 nm</td>
    </tr>
    <tr>
      <td>Clay/polymer interphase</td>
      <td>16.10</td>
      <td>0.4</td>
      <td>d<sub>I</sub>=3 nm</td>
    </tr>
  </tbody>
</table>

A case study has been illustrated to reveal the importance of nano-clay reinforcement in CNT reinforced composite. Table 2 shows the elastic properties of CNT/clay hybrid composite considering four types RVE. The finite element modeling results are validated with micromechanical modeling results.

Table 2 Elastic properties of hybrid composite with variation of number of clay platelet

<table>
  <thead>
    <tr>
      <th>RVE with</th>
      <th>E<sub>L</sub></th>
      <th>E<sub>T</sub></th>
      <th>G<sub>T</sub></th>
      <th>v<sub>L</sub></th>
      <th>v<sub>T</sub></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 CNT</td>
      <td>3.667</td>
      <td>2.2119</td>
      <td>0.738</td>
      <td>0.395</td>
      <td>0.5054</td>
    </tr>
    <tr>
      <td>1 CNT +1 Clay</td>
      <td>5.3245</td>
      <td>2.420</td>
      <td>0.7868</td>
      <td>0.3938</td>
      <td>0.5382</td>
    </tr>
    <tr>
      <td>1 CNT + 2 Clay</td>
      <td>7.0019</td>
      <td>2.626</td>
      <td>0.8468</td>
      <td>0.3938</td>
      <td>0.5508</td>
    </tr>
    <tr>
      <td>1 CNT + 3 Clay</td>
      <td>8.6448</td>
      <td>2.8338</td>
      <td>0.9092</td>
      <td>0.3928</td>
      <td>0.5582</td>
    </tr>
    <tr>
      <td>1 CNT +4 Clay</td>
      <td>10.2846</td>
      <td>3.0908</td>
      <td>0.9929</td>
      <td>0.3917</td>
      <td>0.5564</td>
    </tr>
    <tr>
      <td>Three phase</td>
      <td>9.8932</td>
      <td>2.9931</td>
      <td>0.9865</td>
      <td>0.3899</td>
      <td>0.5423</td>
    </tr>
    <tr>
      <td>Halpin-Tsai</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

In Table 3, elastic moduli are investigated considering constant volume fraction of CNTs inside hybrid composite. It can be concluded from predicted results that four CNTs with one clay based RVE gives better results as compared to one CNT with four-clay RVE.

Table 3 Elastic properties of hybrid composite with variation of Number of CNTs

<table>
  <thead>
    <tr>
      <th>RVE with</th>
      <th>$E_{L}$</th>
      <th>$E_{T}$</th>
      <th>$G_{T}$</th>
      <th>$v_{L}$</th>
      <th>$v_{T}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 Clay</td>
      <td>3.6576</td>
      <td>2.3079</td>
      <td>0.7719</td>
      <td>0.3952</td>
      <td>0.4949</td>
    </tr>
    <tr>
      <td>1 Clay +1 CNT</td>
      <td>5.3236</td>
      <td>2.4137</td>
      <td>0.7838</td>
      <td>0.3948</td>
      <td>0.5397</td>
    </tr>
    <tr>
      <td>1 Clay + 2 CNT</td>
      <td>6.9921</td>
      <td>2.4899</td>
      <td>0.7963</td>
      <td>0.3944</td>
      <td>0.5634</td>
    </tr>
    <tr>
      <td>1 Clay + 3 CNT</td>
      <td>8.6552</td>
      <td>2.5700</td>
      <td>0.8164</td>
      <td>0.3940</td>
      <td>0.5753</td>
    </tr>
    <tr>
      <td>1 Clay +4 CNT</td>
      <td>10.3201</td>
      <td>2.6521</td>
      <td>0.8381</td>
      <td>0.3935</td>
      <td>0.5820</td>
    </tr>
  </tbody>
</table>

## 4. Conclusions

A nano structured hybrid composite composed of clay nano particle and carbon nanotubes were studied using finite element modeling. For numerical investigations through finite element approach, a square RVE was selected to demonstrate the hybrid composite structure. Predicted values from FE modeling were compared with three-phase Halpin-Tsai model. It was found that the elastic modulus from numerical modelling is in close agreement with micromechanics based results. This work provides basic overview of modeling of hybrid composite; furthermore studies have to be done by considering the variation of interphase properties and random distribution of nano-clay and CNTs. It is also planned to prepare CNT/nano clay polymer composite specimen and perform tensile and compressive test to validate the predicted numerical data.

## References

[1]. K. Lau, C. Gu, D. Hui, A critical review on nanotube and nanotube/nanoclay related polymer composite materials, *Composites: Part B* 37 (2006) 425–436.

[2]. T. Hayashi, M.Endo, Carbon nanotubes as structural material and their application in composites, *Composites: Part B* 42(2011) 2151–2157.

[3]. M.T. Kim, K.Y. Rhee, J.H. Lee, D. Hui, A. K.T. Lau, Property enhancement of a carbon fiber/epoxy composite by using carbon nanotubes, *Composites: Part B*42 (2011) 1257–1261.

[4]. J. Srinivas P. Kumar,Analysis of elastic properties of transversely isotropic CNT-reinforced polymers, *Nano Science and Nano Technology*8 (2014) 291-297.

[5]. M.S.P. Shaffer, X. Fan, A.H. Windle, Dispersion and packing of carbon nanotubes, *Carbon* 36 (1998) 1603–1612.

[6]. S. Wang, R.Liang, B.Wang, C. Zhang, Load-transfer in functionalized carbon nanotubes/polymer composites, *Chemical Physics Letters* 457 (2008) 371–375.

[7]. S.W. Kim, T. Kim, Y.S. Kim, H.S.Choi, H.J.Lim, S.J.Yang, C.R.Park, Surface modifications for the effective dispersion of carbon nanotubes in solvents and polymers,*Carbon* 50 (2012) 3–33.

[8]. P.C. Ma, J.K.Kim , B.Z. Tang, Effects of silane functionalization on the properties of carbon nanotube/epoxy nanocomposites, *Composite Science and Technology*67 (2007) 2965–2972.

[9]. S. P. Pereira, G. Scocchi, R. Toth, P. Posocco, D. R nieto, S. Pricl, M. Fermeglia, Multiscale modeling of polymer/clay nanocomposites, *Journal of Multiscale Modelling*3(2011) 151-176.

[10]. S. Wang, R.Liang, B.Wang, C. Zhang, Reinforcing polymer composites with epoxide-grafted carbon nanotubes, *Nanotechnology*19 (2008) 085710.

[11]. V. Levchenko, Y. Mamunya, G. Boiteux, M. Lebovka, P. Alcouffe, G. Seytre, E. Lebedev, Influence of organo-clay on electrical and mechanical properties of PP/MWCNT/OC nanocomposites, *European Polymer Journal* 47 (2011) 1351-1360.

[12]. L. Liu and J. C. Grunlan, Clay Assisted Dispersion of Carbon Nanotubes in Conductive Epoxy Nanocomposites, *Advanced Functional Materials* 17 (2007)2343-2348.

[13]. B. L. Silva, F. C. Nack, C. M. Lepienski, L. A. F. Coelho, D. Becker, Influence of intercalation methods in properties of clay and carbon nanotube and high density polyethylene nanocomposites, *Materials Research* 17 (2014) 1628-1636.

[14]. Z. Wang, C. Xu, Y. Zhao, D. Zhao, Z. Wang, H. Li, K. Lau, Fabrication and mechanical properties of exfoliated clay-CNTs/epoxy nanocomposites, *Materials Science and Engineering A* 490 (2008) 481-487.

[15]. Y. J. Liu and X. L. Chen, Evaluations of the effective material properties of carbon nanotube-based composites using a nanoscale representative volume element, *Mechanics of Materials* 35 (2003) 69-81.

[16]. P. Kumar and J. Srinivas, Numerical evaluation of effective elastic properties of CNT-reinforced polymers for interphase effects, *Computational Material Science*88(2014) 139-144.

[17]. N. Sheng, M.C. Boyce, D.M. Parks, G.C. Rutledge, J.I. Abes, R.E. Cohen, Multiscale micromechanical modeling of polymer/clay nanocomposites and the effective clay particle,*Polymer*45 (2004) 487-506.

[18]. L. M. Jr., G. Dai,Hybrid and hierarchical nanoreinforced polymer composites: Computational modelling of structure-properties relationships, *Composite Structures* 117 (2014) 156-168.

[19]. X. Jia, B. Liu, L. Huang, D. Hui, X. Yang, Numerical analysis of synergistic reinforcing effect of silica nanoparticle-MWCNT hybrid on epoxy-based composites, *Composites Part B: Engineering* 54 (2013) 133-137.

[20]. S. Rahmanian, A.R. Suraya, B. Roshanravan, R.N. Othman, A.H. Nasser, R. Zahari, E.S. Zainudin, The influence of multiscale fillers on the rheological and mechanical properties of carbon-nanotube-silica-reinforced epoxy composite, *Materials and Design*88 (2015) 227-235.