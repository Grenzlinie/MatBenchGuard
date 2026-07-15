# Finite element analysis of the open-cell nickel foam based on the Kelvin model

Zhao Longzhi, Zhang xiaolan, Zhao Mingjuan
Key Laboratory of Ministry of Education for Conveyance and Equipment, East China Jiaotong Engineering
ECJTU
Nanchang 330013, China
zhaolongzhi@163.com

Zhao Longzhi, Yan Hong
School of Mechanical Electronical Engineering,
Nanchang University
NCU
Nanchang 330013, China

Abstract—Nickel foam is mainly used for the battery electrode materials specifically for MH-Ni batteries, which can be widely used in the portable computers, the mobile phones and the hybrid electric vehicle. It is important to study the mechanical properties. The effects of the porosity and model type of the open cell nickel foam on the tensile behavior were investigated. With the finite element method based on Kelvin model in this paper. The results show that the Kelvin model is more resistant to deformation than the Gibson-Ashby model and is closer to the experiment results, and the bearing capacity decreasing as the porosity increasing.

Keywords-nickel foam; Kelvin model; Gibson-Ashby model; porosity; tensile

## I. INTRODUCTION

Nickel foam, the porous new functional foam metal materials with tri-dimensional network, low density and the porosity within 88% ~ 99%, which is used in separate engineering, new energy materials, storage materials, filtration, heat exchange, heat insulation, catalyst carrier, separated flame, explosion-proof, fire-retardant, acoustic damping and other fields. At present nickel foam is primarily used for electrode substrates of Secondary MH-Ni and nickel-cadmium battery [1~4], and with large market demand. Porous electrode substrate of battery played the role of concentrating electric current and supporting for carrying active material body [5], and it has bright prospects for its application.

Nickel foam is assumed as open-cell foam materials, which is the continuous tri-dimensional network and with the pores connected. The Kelvin model is used to analog low-density foam mechanical properties ideally, because it can more truly reflect the characteristics of the collection of foam materials and completely fill the entire space, and can better meet the characteristics of cell body special conditions [6].

The materials' mechanical properties play an important role in their application. Therefore, the study of its mechanical properties is significant. Uniaxial tensile behavior of the open cell nickel foam is investigated with the finite element method based on ANSYS software in this paper. The Kelvin model is selected to simulate and then analyze the mechanical properties of open-cell nickel foam. Two aspects of different models and porosity are used to compare the effects. The stress-strain curves are drew by simulation analysis' results, and are investigated its influence on mechanical properties of nickel foam materials.

## II. THE ESTABLISHMENT OF THE MODELS

The solid45 unit is selected for improving the accuracy. Solid45 is used for the 3-D modeling of solid structures. The element is defined by eight nodes having three degrees of freedom at each node: translations in the nodal x, y, and z directions. The element has plasticity, creep, swelling, stress stiffening, large deflection, and large strain capabilities. The elastic modulus of material was chosen by 93 MPa, with Poisson's ratio 0.31, area density 375 Kg/m², yield strength of 0.43 MPa and shear modulus 36 MPa respectively in this paper. The porosity of the two models is the same to 96.1%. The free meshing is used to mesh the model, because it is applied to mesh the complex solid. It can automatically generate triangle or quadrilateral mesh, automatically generated tetrahedral mesh in the body and is the one of the highest degree of automation of the meshing technologies. Set the boundary conditions and applied loads, restricted the degrees of freedom for all the nodes at the left of model. Static tensile force is imposed to the right surface of the model. The Microstructure of nickel foam is shown in Fig. 1.

![](./images/811756286990352385_1.jpg)

Figure 1. The microstructure of nickel foam

## III. THE INFLUENCE OF DIFFERENT MODELS

Kelvin multi-cell model is shown in Fig. 2. The Kelvin unit cell model structure consists of 8 regular hexagons and 6

---
Sponsored by Science Research Foundation of East Jiaotong University (No.01306016, No07JJD06), Young Science Foundation of Jiangxi Provincial Education Office (09497), and Young Science Foundation of Jiangxi Province (2009GQC0014) .

978-1-4244-7739-5/10/$26.00 ©2010 IEEE

squares, contains 24 vertices and 36 pillars of equal length. Three plane-symmetry axises pass through the center of figure and four line-symmetry axises pass through the pillars of 6 squares [7]. The pillars of foam materials are conceived as same cross-section beam [8]. Gibson-Ashby multi-cell model is shown in Fig.3. The Gibson-Ashby unit cell model structure is a cubic lattice, which constructed by the same 12 prisms. Isotropic open-cell foam materials are characterized abstractly a collection unit with cubic structure by Gibson-Ashby model [9].

![](./images/811756286990352385_2.jpg)

Figure 2. The Kelvin multi-cell model

![](./images/811756286990352385_3.jpg)

Figure 3. The Gibson-Ashby multi-cell model

![](./images/811756286990352385_4.jpg)

Figure 4. Equivalent stress nephograms (a-the Kelvin model b-Gibson-Ashby model)

The equivalent stress and strain nephograms of two kinds of models are loaded with the equal load as shown in Fig.4 and Fig. 5. Two kinds of models are composed of a number of reinforcements, and the load is bore by a large number of reinforcements. Stress and strain are the smallest in the reinforcements perpendicular to direction of the load except the bearing surface; and where the greatest stress and strain is in the intersects of reinforcements can be seen from the figure.

Fig. 6 shows the stress - strain curves which obtained from simulation of two models. Can be seen from the figure: the elastic deformation stage of the two kinds of model are short, the Gibson-Ashby model shows the apparent plastic behavior after the yield point, that is, small changes occurred in the tensile strength, there is a great deformation in the model (Here "great" is relative to the shorter stage of elastic); but there is a small deformation in the Kelvin model even though great changes occurred in the tensile strength. This needs greater load to exert to the Kelvin model for the same strain. It is that the Kelvin model could bear greater load than the Gibson-Ashby model. The gradual increase to the same value of the load, there is more strain of the Gibson-Ashby model than the Kelvin model. This shows that the strength of the Kelvin model is greater than the Gibson-Ashby model. The reason is obtained by analyzing: the most of reinforcements of the Gibson-Ashby model is parallel to the direction of the load and is more conducive to deliver the power. And there is a certain angle in the Kelvin model, which would cause the loss of power. In addition, in the intersection, the right angles between the ribs of the Gibson-Ashby model are easier to stress concentration.

![](./images/811756286990352385_5.jpg)

Figure 5. Equivalent strain nephograms (a- Kelvin model b- Gibson-Ashby model)

The experimental of the nickel foam under uniaxial tensile with aerial density $375\ \text{g/m}^2$, relative density 0.039 was made in the CSS-44020 Electronic Universal Testing Machine, the stress - strain curves were obtained. The expression between the porosity and the relative density of the foam materials as shown in (1):

$$\theta=1-\rho \tag{1}$$

The $\theta$ is the porosity, is $\rho$ the relative density [10]. So the porosity of the aluminum foam is 96.1%. The data as shown in Fig. 6, the results showed that: The stress - strain curve consist of linear elastic deformation stage and the plastic deformation phases, and the linear elastic deformation stage is very short. The stress is low at the beginning of the plastic deformation. The plastic deformation began with less than 1% strain deformation, and the stress up to 2 Mpa with the strain deformation reached 4% [11].

The stress - strain curve of the Kelvin model is closer to the experimental results throughout the deformation stage than the Gibson-Ashby model. Because the irregular and inhomogeneo- us of the arrangement of the atoms exist in the practical application of the nickel foam materials. However, there are many shortcomings in the Kelvin model, such as the more complicated of the shape, more intersections and there are a lot of curved surface. It needed longer time and also high requirements on the equipment in the modeling, meshing and solving process.

![](./images/811756286990352385_6.jpg)

Figure 6. Stress - strain curves of the two models

## IV. THE EFFECTS OF POROSITY

The porosity of the porous materials is that the proportion of porous volume ratio of the total volume of the porous body is expressed as a percentage generally. Studies have shown that the performance of porous materials depends on the porosity most, its effects is greater than all the other factors [12]. The effects of porosity of the nickel foam to the mechanical proper- ties are studied by the Kelvin model. The material parameters are shown in Table Ⅰ. The others are as the same as the above.

**TABLE I. THE MATERIAL PARAMETERS**

<table>
  <tr>
    <th>Porosity</th>
    <th>Cross-Section Radius/mm</th>
    <th>Elastic-Modulus /MPa</th>
    <th>Poisso n's Ratio</th>
    <th>Shear-Modulus /MPa</th>
  </tr>
  <tr>
    <td>89%</td>
    <td>0.064</td>
    <td>261.00</td>
    <td>0.31</td>
    <td>101.0</td>
  </tr>
  <tr>
    <td>92%</td>
    <td>0.051</td>
    <td>191.00</td>
    <td>0.31</td>
    <td>74.0</td>
  </tr>
  <tr>
    <td>95%</td>
    <td>0.043</td>
    <td>119.00</td>
    <td>0.31</td>
    <td>46.0</td>
  </tr>
  <tr>
    <td>97%</td>
    <td>0.033</td>
    <td>71.48</td>
    <td>0.31</td>
    <td>27.7</td>
  </tr>
</table>

The stress - strain curves under different porosity are shown in Fig. 7. From the figure can be seen: The smaller the porosity, the shorter the elastic stage, the more slowly get into the plastic stage with the gradually increasing load. In the stage of producing the same deformation, the smaller the porosity, the greater the load it has to be imposed. This result from that the smaller the porosity, the bigger the volume of entity, and the bigger load area, then The smaller the load of average area. Though more of the active substance can be carried, the battery's energy density and specific energy are increased for the high porosity nickel foam electrode, light weight and big stiffness of the structure can be brought about and lead to low bearing of the total structure by high porosity [13]. However, it needed longer time and also high requirements on the equipment in the modeling, meshing and solving process.

![](./images/811756286990352385_7.jpg)

Figure 7. Stress-strain curves under different porosity

## V. CONCLUSION

(1) The nickel foam with the Kelvin model could bear greater load and more resistant to deformation than the Gibson-Ashby model , that is the strength is greater in the static tensile behavior, and the stress-strain curves of the Kelvin model is closer to the experimental results than the Gibson-Ashby model .

(2) With the porosity decreasing, the carrying power and the strength are increasing.

## REFERENCES

[1] L. H. Zhang, Z. L. HUI, and Z. Q. Fang, "Preparation and performance of nickel foam," Chinese journal of rare metals. Beijing, vol. 25, pp. 230-234, 2001.

[2] Y. F. Zhang, L. J. MA, and Z. X. Cui, "A study on absorption Property of Foamed Nickel," Noise and vibration control. Shanghai, vol. 2, pp. 30-33, 2001.

[3] J. Y. Zhang, P. Zhang, and Q. L. Gan, "An experimental study on mechanical properties of nickel foams," Materials reviews. Chongqing, vol. 18, pp. 92-94, 2004.

[4] P. S. Liu, C. Fu, and T. F. Li, "The tensile strength of high-porosity metals," Rare metal materials and engineering. Xian, vol. 29, pp. 94-100, April, 2000.

[5] P. Liu, Q. C. Yang, J. Luo, and J. F. Xia, "Macroscopic tensile fracture behavior of nickel foam," Metallic functional materials. Beijing, vol. 16, pp. 33-37, 2009.

[6] J. L. Zhang, and Z. X. Lu, "Finite element analysis for the elastic properties of closed-cell foams based on a tetrakaidecahedron model," Journal of mechanical strength. Henan, vol. 29, pp. 315-319 , 2007.

[7] S. L. Shi, and Z. X. Lu, "Finite element analysis for the elastic modulus of open-cell foams based on a tetrakaidecahedron model," Journal of Mechanical Strength. Henan, vol. 28, pp.108-112, 2006.

[8] L. S. Xie, M. H. Chen, G. Q. Tong, and L. Gao. "Anisotropic Elastic Properties of Foam Metal with Open Cells," Materials for Mechanical Engineering. Shanghai, vol. 27, pp. 7-16, 2003.

[9] P. S. Liu, "Basic Analysis to Classical Model for Foamed Metals," Nonferrous metals. Beijing, vol. 57, pp. 55-57, 2005.

[10] Q. L. Gan, and J. Y. Zhang, The basic mechanical properties and constitutive relation of metal foams. Hunan, P. 14, 2004.

[11] Q. L. Gan, and J. Y. Zhang, "Efects of temperature and strain rate on tensile behavior of nickel foam," Natural science journal of xiangtan university. Hunan, vol 25, pp. 88-90, 2003.

[12] P. S. Liu, "Introduction to Porous materials," Beijing: Tsinghua University Press, p. 299, 2004.

[13] C. Q. Li, X. H. Li, Z. X. Wang, and H. J. Guo, "Research progress in current collecting material for alkaline nickel battery" Battery bimonthly. Hunan, vol. 37, pp. 57-5, 2007.