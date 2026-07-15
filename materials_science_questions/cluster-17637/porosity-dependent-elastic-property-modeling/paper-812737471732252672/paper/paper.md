# Geometric Modeling and Finite Element Simulation for Architecture Design of 3D Printed Bio-ceramic Scaffold Used in Bone Tissue Engineering

A. D. Bagde*, A. M. Kuthe, S. R. Nagdeve, S. W. Dahake, P. S. Sapkal, S. B. Daronde, N. H. Lande and B. D. Sarode

**Abstract** | Tissue engineering is widely accepted as an effective way to treat critical size bone defect. However, fabricating the scaffold functioning as an extracellular matrix and liable for cell proliferation with excellent material and design parameter to match closely with the natural bone property is still a challenge. The present paper focuses on finite element analysis (FEA) for getting the optimized architecture design by keeping extrusion-based 3D printing in mind. Predicting and optimizing the property of scaffold through FEA was performed on a 3D printing process such as selective laser sintering (SLS) and stereolithography (SLA), but for extrusion-based 3D printing, such literature is very few. In the present paper, the various geometrical design parameters for extrusion-based 3D printed scaffold were studied. A total of 36 scaffolds were analyzed by FEA to predict the porosity and Young's modulus of the composite material. Based on the FEA result, the best scaffold with the optimum mechanical property was suggested. This article significance goes far beyond the specific objective to which it is dedicated. It shows a guideway for scaffold architecture design process matching the natural human tissue of interest.

## 1 Introduction

Significant bone defects caused by trauma, accidents, or medical conditions can be treated by prosthetic implants, autograft, or allograft bone tissue. Nevertheless, there are some limitations such as patient pain, immune reaction, disease transmission, and non-optimal interaction between the body and implanted materials. Bone tissue engineering (BTE) provides a promising solution to the above problems by producing a functional substitute for damaged tissue. Langer et al. defined tissue engineering as "a multidisciplinary scientific branch that combines cell biology, regenerative medicine, materials science and engineering"¹, ².

The two significant components of tissue engineering are: cells, the preliminary components of living organisms; and the biomaterials, used for fabricating the scaffold functioning as a provisional mechanical support and responsible for cell migration, proliferation and differentiation². A variety of metal, polymer and ceramic biomaterial have been employed for BTE and reviewed by many authors³⁻⁶, ⁷. Out of accessible biomaterials, the mineral phase of natural bone is similar to that of ceramic biomaterials based on their mechanical stiffness (Young's Modulus), hard brittle surface and low elasticity, establishing these as appropriate for bone regeneration ², ⁸, ⁹. Hydroxyapatite (HA), β tricalcium phosphate (β-TCP), magnesium oxide (MgO), silicate, alumina (Al₂O₃) and zirconia (ZrO₂) are the most common materials used in tissue engineering. Sapkal et al. worked on HA-β-TCP¹⁰, β-TCP-zirconia¹¹ and β-TCP¹² and found an improvement in mechanical strength with the addition of HA

¹ Visvesvaraya National Institute of Technology, Nagpur, India.
*bagde.ashu@gmail.com

to zirconia while comparing with β-TCP in the respective papers. Mart et al. studied Si-doped HA with gelatin for producing the micro- and macropores in the scaffold for effective drug delivery and bone regeneration¹³. Si-doped HA has been used for bone regeneration with promising results and osteoinduction has been shown by Vila et al.¹⁴. These are the few studies that represent the improvement in the biomechanical properties of the scaffold.

The perfect scaffold for BTE must have the highest interconnectivity, high porosity, biocompatibility and biodegradability along with mechanical reliability. However, modern scientific techniques have produced a wide range of composite material with the osteoconductive and osteoinductive property. Nevertheless, the porosity and interconnectivity mainly depend on the scaffold fabrication process employed. The review paper by the same author described the various scaffold fabrication processes with its advantages and disadvantages ². This paper concludes that 3D printing is advantageous compared with other conventional fabrication in terms of customized design, computer control fabrication, anisotropic scaffold fabrication and processing conditions ², ¹⁵⁻²¹, ²². A current challenge in the 3D printing process is making a balance between mechanical property, porosity, interconnectivity and pore size. It is not always possible to fabricate the scaffold and test for the desired parameters as 3D printing is slow, time-consuming, has high energy consumption and is expensive. Computer simulation provides an alternative tool for predicting mechanical property with respect to the different scaffold design parameters. It not only saves time, but can also help the researcher to know more about the mechanical behavior of the scaffold in vivo by simulation. The present article deals with the finite element simulation for predicting the effective modulus for different bioceramic composites to best match with the cortical bone characteristics.

## 2 Materials
Calcium phosphate-based materials are universally accepted in BTE applications because of their structural and chemical similitude to bone mineral and their natural features for osteoconductivity, osteoinductivity, cell attachment, cell proliferation, etc. desired for bone tissue regeneration ¹⁰. The major ceramic materials used in tissue engineering are β-tricalcium phosphate {β-TCP}, $(Ca_3(PO_4)_2)$, zirconium $(ZrO_2)$, magnesia (MgO), alumina $(Al_2O_3)$ and hydroxyapatite {HA} $(Ca_{10}(PO_4)_6(OH)_2)$. Although, β-TCP is an appropriate bone replacement material which can construct a direct chemical bond with tissue, its weak mechanical strength and rapid resorption restrict its use²³, ²⁵. $ZrO_2$ is capable of promoting cell proliferation, differentiation in osteogenic conduit with superior mechanical properties and biological features such as low corrosion potential and low cytotoxicity with minimal adhesion of bacteria¹¹, ²⁴, ²⁶, ²⁷. MgO has excellent biocompatibility and is nontoxic with good rate of bone formation and the required biomechanical properties, making it suitable for tissue engineering applications²⁸, ²⁹⁻³⁰. $Al_2O_3$ has the advantages of high hardness, low friction coefficient, excellent corrosion resistance and very low wear rate, inhibiting static fatigue and slow crack growth while under load, making it competent for hard tissue replacement²⁶. HA is one of the main mineral components of bones and teeth, with excellent biocompatibility with skin and muscle tissues as well as good physiological properties²⁷.

The best material or composite for bone regeneration is a matter of deliberation; therefore, researchers work on different materials aimed toward the improvement of the particular biomechanical property crucial from their point of view. Out of all the essential features, the one primary aim of scaffold is to work as an extracellular matrix for cell growth and provide the mechanical strength to the lesion area. The present paper aims to identify the effect of scaffold architecture design from mechanical aspects. The study is divided into three parts:

1. Study of the impact of architecture design on the porosity of the scaffold.
2. Finite element analysis of the scaffold with altered design parameters for mechanical strength.
3. Relationship between the porosity and effective Young's modulus for optimum design architecture among the proposed ones.

The mechanical properties considered in the present study are explained in Table 1.

### 2.1 Composite Material Properties
The ceramic material alone does not have all the properties needed by an ideal scaffold and hence a composite with other materials is needed to be built to obtain the characteristics of interest.

**Table 1:** Biomaterials and their properties.

<table>
  <thead>
    <tr>
      <th rowspan="2">Materials</th>
      <th colspan="2">Mechanical property</th>
      <th rowspan="2">Ref.</th>
    </tr>
    <tr>
      <th>Young's modulus ($E$) GPa</th>
      <th>Poisson's ratio ($\mu$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>β-Tricalcium phosphate (β-TCP), ($Ca_3(PO_4)_2$)</td>
      <td>120</td>
      <td>0.3</td>
      <td>23</td>
    </tr>
    <tr>
      <td>Zirconium ($ZrO_2$)</td>
      <td>210</td>
      <td>0.31</td>
      <td>24</td>
    </tr>
    <tr>
      <td>Magnesia (MgO)</td>
      <td>300</td>
      <td>0.35</td>
      <td>28</td>
    </tr>
    <tr>
      <td>Alumina ($Al_2O_3$)</td>
      <td>320</td>
      <td>0.23</td>
      <td>26</td>
    </tr>
    <tr>
      <td>Hydroxyapatite ($Ca_{10}(PO_4)_6(OH)_2$)</td>
      <td>13</td>
      <td>0.27</td>
      <td>27</td>
    </tr>
  </tbody>
</table>

Tarafder et al. demonstrate that MgO dopant TCP scaffold results in 37–41% improvement in the mechanical strength, along with improved osteogenesis during in vivo study in the rabbit model³¹. Aminzare et al. found the improvement in hardness from 2.52 to 5.12 GPa and 40% enhancement in the bending strength of the scaffold by using alumina reinforced with HA, due to the formation of calcium aluminates³². Matsumoto et al. reported that when the mixing ratio of $ZrO_2$/HA was 70/30, the strength of the scaffold was equal to the strength of the cortical bone, along with high osteoconductivity during in vivo experiments²⁴. Sapkal et al. initiated the use of TCP/$ZrO_2$ in a ratio of 70/30 to get the best suitable properties for the tissue engineering construct with indirect casting and 3D printing process¹¹,³³. In another study by Sapkal et al., they found that a TCP/HA ratio 80/20 will give the best result compared to different mixing ratios in terms of biomechanical stability¹⁰.

The mechanical properties of powder composite are difficult to calculate due to molecular changes at sintering. But the modified rule of the mixture, also known as the Halpin–Tsai equation, can give close to accurate values³⁴,³⁵.

$$
E_{\mathrm{c}}=\frac{E_{\mathrm{m}}\left(1+2 s \times q \times V_{\mathrm{p}}\right)}{\left(1-q \times V_{\mathrm{p}}\right)},
$$

$$
\text{where } q=\frac{\left(\frac{E_{\mathrm{p}}}{E_{\mathrm{m}}}-1\right)}{\left(\frac{E_{\mathrm{p}}}{E_{\mathrm{m}}}+2 s\right)}.
$$

The formula can calculate Poisson's ratio of the composite:

$$
\mu_{\mathrm{c}}=\frac{\mu_{\mathrm{m}}\left(1+2 s \times q \times V_{\mathrm{p}}\right)}{\left(1-q \times V_{\mathrm{p}}\right)},
$$

$$
\text{where } q=\frac{\left(\frac{\mu_{\mathrm{p}}}{\mu_{\mathrm{m}}}-1\right)}{\left(\frac{\mu_{\mathrm{p}}}{\mu_{\mathrm{m}}}+2 s\right)},
$$
where $E_{\mathrm{c}}, \mu_{\mathrm{c}}$ is the Young's modulus and Poisson's ratio of the composite; $E_{\mathrm{m}}, \mu_{\mathrm{m}}$ are the matrix Young's modulus and Poisson's ratio of material. $E_{\mathrm{p}}, \mu_{\mathrm{p}}$ are the Young's modulus and Poisson's ratio of the particle-reinforced material, $V_{\mathrm{p}}$ is the volume fraction of the particle-reinforced material and $S$ is the particle aspect ratio considered as 1, as the particle morphology is considered as spherical. Accordingly, the modified Young's modulus and Poisson's ratio for various composites used in the proposed FEA are explained in Table 2.

## 3 Methodology
### 3.1 Geometrical Modeling of the Scaffold
Scaffolds were designed based on models suggested by Chuan et al.³⁶, keeping in mind the extrusion-based 3D printing principles. The main parameters for scaffold design are stand diameter ($D$), pore diameter ($d$) and the orientation angle ($\theta$) of the plotted layer with respect to the previous layer. This parameter is responsible for scaffold architecture design. The scaffold architecture was noted as $D\_d\_\theta$ and denoted in Fig. 1. Strand diameter ($D$) was selected based on the needle size commercially available for extrusion-based 3D printing along with supportive evidences of previous literature and was taken as 400, 600 and $800\ \mathrm{\mu m}$¹¹,¹⁰,³⁷.

Ideally, any scaffold consists of two kinds of porosity: the first is microporosity where the pore diameter $(d) < 50\ \mathrm{\mu m}$ and is responsible for initial cell adhesion; secondly, macroporosity where the pore diameter is between 50 and $1000\ \mathrm{\mu m}$ and is responsible for oxygen, nutrient delivery and angiogenesis. The generation of micropores is not in control during the 3D printing process, as it is an effect of evaporation of the binder particle between the two matrix particles unless some porogen is mainly used to create the micropores. The impact of this micropore on the mechanical aspect is considered as negligible and hence not considered during the FEA. The macropores affect directly the mechanical strength of the scaffold and needs to be analyzed for its effect. The ideal macropore size is still a matter of debate, but pores in the range of 300–500 $\mathrm{\mu m}$ are considered as favorable for nutrient delivery and blood vessel formation¹⁵,³⁸,³⁹. So in the present study, the pore diameters $(d)$ 300, 400 and $500\ \mathrm{\mu m}$

### Table 2: Young's modulus and Poisson's ratio of matrix (β-TCP) material with other particle reinforced, where $E_c$ and $\mu_c$ are Young's modulus and Poisson's ratio of the composite.

<table>
  <thead>
    <tr>
      <th rowspan="3">Particle reinforced in composite</th>
      <th colspan="10">Composite proportion</th>
    </tr>
    <tr>
      <th colspan="2">90:10</th>
      <th colspan="2">80:20</th>
      <th colspan="2">70:30</th>
      <th colspan="2">60:40</th>
      <th colspan="2">50:50</th>
    </tr>
    <tr>
      <th>$E_c$</th>
      <th>$\mu_c$</th>
      <th>$E_c$</th>
      <th>$\mu_c$</th>
      <th>$E_c$</th>
      <th>$\mu_c$</th>
      <th>$E_c$</th>
      <th>$\mu_c$</th>
      <th>$E_c$</th>
      <th>$\mu_c$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zirconium ($ZrO_2$)</td>
      <td>127.341</td>
      <td>0.301</td>
      <td>135.000</td>
      <td>0.302</td>
      <td>142.973</td>
      <td>0.303</td>
      <td>151.311</td>
      <td>0.304</td>
      <td>160.000</td>
      <td>0.305</td>
    </tr>
    <tr>
      <td>Magnesium (Mg)</td>
      <td>132.412</td>
      <td>0.304</td>
      <td>145.722</td>
      <td>0.309</td>
      <td>159.991</td>
      <td>0.314</td>
      <td>175.351</td>
      <td>0.319</td>
      <td>191.991</td>
      <td>0.324</td>
    </tr>
    <tr>
      <td>Alumina ($Al_2O_3$)</td>
      <td>133.332</td>
      <td>0.293</td>
      <td>147.681</td>
      <td>0.286</td>
      <td>163.195</td>
      <td>0.278</td>
      <td>179.992</td>
      <td>0.272</td>
      <td>198.242</td>
      <td>0.264</td>
    </tr>
    <tr>
      <td>Hydroxyapatite ($Ca_{10}(PO_4)_6(OH)_2$)</td>
      <td>105.393</td>
      <td>0.297</td>
      <td>91.921</td>
      <td>0.294</td>
      <td>79.472</td>
      <td>0.291</td>
      <td>67.911</td>
      <td>0.288</td>
      <td>37.164</td>
      <td>0.285</td>
    </tr>
  </tbody>
</table>

![](./images/812737471732252672_1.jpg)

**Figure 1:** The nomenclature used for the scaffold architecture design.

### Table 3: Orientation angle representation.

<table>
  <thead>
    <tr>
      <th>Sr no.</th>
      <th>Layer orientation pattern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0-90</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0-45-90-135</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0-60-120</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0-30-60-90-120-150</td>
    </tr>
  </tbody>
</table>

![](./images/812737471732252672_2.jpg)

**Figure 2:** Architecture design parameters for the scaffold.

are considered. The orientation angle ($\theta$) is the angle between two subsequent layers and is responsible for the different intricate architectures of the scaffold. Four different architectures have been considered in the present study and represented by numbers as in Table 3.

By varying the three aspects of geometrical scaffold modeling, a total of 36 scaffolds were designed in computer-aided design software CATIA V5R20 (Dassault Système$^\circledR$) (Table 4) and analyses were done in ANSYS Workbench 16.2 (Fig. 2).

### 3.2 Finite element analysis (FEA)
With the improvement in computation facility, it is possible to predict the behavior of materials and perform the simulation. Much efforts have been taken toward predicting the scaffold properties starting from cell structure [simple cubic (SC), Gibson–Ashby (GA), body-centered cubic (BCC) and reinforced body-centered cubic (RBCC)] by Luxner et al.$^{40}$ to using complicated Voronoi tessellation mathematical method for getting the bone-like structure and analyze it for cell penetration, nutrient diffusion and osteoconductive properties implemented by Gómez et al.$^{41}$. Singh et al. performed the finite element simulation for comparing the compressive strength of stainless steel and titanium alloy with compact bone by using the hollow cube unit cell suitable for SLS printing$^{42}$. These methods give a close result, but suitable only for scaffold produced with hallow cube as a lattice structure and cannot be applied to another printing process, especially extrusion-based printing. Cahill et al. focused on accurate prediction of finite element prediction by improving the FEA modeling method taking into account discrepancies such as surface roughness and micropores into account. He concludes that ignoring these discrepancies leads to incorrect prediction$^{43}$. The result of this work helps authors to have accurate modeling of the scaffold in the present study. Eshraghi et al. did micromechanical investigation for polycaprolactone (PCL) and hydroxyapatite (HA) scaffold fabricated by SLS and found the FEA result to be in tune with the experimental method$^{44}$. In another study by the same author, 1D, 2D and

Table 4: An example of architecture design (four orientation angles, three pore diameters and three strand diameters, leading to 36 design of the scaffold was studied).

<table>
  <thead>
    <tr>
      <th>Architecture</th>
      <th>3D view</th>
      <th>Front view</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.4-0.5-1</td>
      <td>![](./images/812737471732252672_3.jpg)</td>
      <td>![](./images/812737471732252672_4.jpg)</td>
    </tr>
    <tr>
      <td>0.4-0.5-2</td>
      <td>![](./images/812737471732252672_5.jpg)</td>
      <td>![](./images/812737471732252672_6.jpg)</td>
    </tr>
    <tr>
      <td>0.4-0.5-3</td>
      <td>![](./images/812737471732252672_7.jpg)</td>
      <td>![](./images/812737471732252672_8.jpg)</td>
    </tr>
    <tr>
      <td>0.4-0.5-4</td>
      <td>![](./images/812737471732252672_9.jpg)</td>
      <td>![](./images/812737471732252672_10.jpg)</td>
    </tr>
  </tbody>
</table>

3D orthogonally porous scaffolds were tested and analyzed by FEA. In both studies, the fabrication process considered is SLS⁴⁵. However, from the author's best knowledge, FEA for extrusion-based printing process with different architecture designs has not been used. Hence, the authors need to work on the objective specified above.

![](./images/812737471732252672_11.jpg)

Figure 3: Schematic of steps of finite element analysis.

The steps followed for FEA analysis are explained by Singh et al.⁴² using Ansys workbench 16.2 and summarized as importing the CAD input file into the FEA software as engineering data and assigning the composite material property followed by meshing with an element size of 300 µm. For the analyses, the bottom of the model was constrained by a fixed support at the bottom end and displacement (0.001 mm, 0.002 mm, 0.003 mm, 0.004 mm) was applied at the top in a downward direction (Fig. 3). For case study 1, equivalent stresses (von Mises stresses) were noted and for case study 2 reaction forces at the support were noted.

## 4 Results and Discussion
The FEA results for various architectures and compositions were obtained and explained as follows.

### 4.1 Porosity Achieved with Different Architecture Design
The porosity of a scaffold is the void space in the solid. The higher the porosity, the more space is available in the scaffold for the formation of new tissue⁴⁶. The porosity should preferably be as high as possible. The porosity can be measured by the formula given below⁴⁷:

$$
	\text{Porosity} = 1 - \frac{V_{\text{solid}}}{V_{\text{total}}} \times 100\%,
$$

![](./images/812737471732252672_12.jpg)

**Figure 4:** Porosity of the concerned architecture design of the scaffold.

where $V_{solid}$ is the volume of the solid and $V_{total}$ is the total volume of the scaffold.

The porosity values were found to be in the range of 39.58–64.13% depending on the scaffold architecture and design. The average porosity was found to be 51.63%. The porosity was directly proportional to the design parameters: strand diameter, pore diameter and orientation angle (Fig. 4).

The results show that the strand diameter and pore diameter have a significant influence on the porosity of the structure. Larger the pore, the more is the gap between the two strands; hence, the void space also will be enormous. Thus, porosity will increase with pore diameter, as shown in the results (Fig. 4). On the contrary, the strand diameter has a negative response to porosity. Increasing strand diameter decreases the void space in the scaffold structure and hence reducing the porosity of the scaffold.

### 4.2 Case II: Effect of Architecture Design and Material Composition on Mechanical Property
The von Mises stresses for four situations, represented as $S_1$, $S_2$, $S_3$ and $S_4$ for $\beta\text{-TCP:ZrO}_2$, $\beta\text{-TCP:MgO}$, $\beta\text{-TCP:Al}_2\text{O}_3$ and $\beta\text{-TCP:HA}$, respectively, were analyzed. From pure matrix β-TCP (100:0), 10% increment in particle reinforcement to 50% was done. Figure 5 shows that von Mises stresses act as a function of displacements for different concentrations of particles in the matrix. The mechanical property of the composite depends on the mechanical property of the components. $\text{ZrO}_2$, $\text{MgO}$ and $\text{Al}_2\text{O}_3$ possess superior mechanical property than the matrix material resulting in the higher percentage of this particle in the matrix, which will ultimately improve the mechanical property of the composite. Therefore, 50:50 ratio of the matrix and particle material will show higher von Mises stress and eventually high compressive strength. But $\text{ZrO}_2$ and $\text{Al}_2\text{O}_3$ material are not biodegradable limiting its utilization in BTE and hence from FEA it is recommended to have a small portion around 10%. However, MgO is the only material which possesses the property of corrosion when in contact with body fluid. This corrosion property restricted its utilization, and hence the concentration will need to be keep below 10%. HA has inferior mechanical properties than β-TCP as represented in Table 1. Consequently, the mechanical properties of the composite will be inferior to those of pure β-TCP. Thus, HA shows the opposite trend to that of the first three materials. Nevertheless, β-TCP:HA will control the degradation rate of the matrix material and help most in conduction; therefore, it is recommended to have the composition between 20 and 30%. In the present study, the increment of the particle was considered as 10%, but to get a closer and precise result, one should follow the FEA for a small increase.

### 4.3 Relationship Between Young's Modulus and Porosity of Scaffold
Addition of zirconia, alumina and magnesia in the composite will increase β-TCP's strength sometimes more than the strength of bone, resulting in stress shielding, which can be avoided by calculating the effective modulus of the scaffold by the following formula:
$$
E_{\text{effective}} = \frac{R}{A} \bigg/ \frac{dl}{l},
$$

![](./images/812737471732252672_13.jpg)

**Figure 5:** von Mises stress for different compositions: $S_1$, $S_2$, $S_3$ and $S_4$ for $\beta$-TCP:ZrO$_2$, $\beta$-TCP:MgO, $\beta$-TCP:Al$_2$O$_3$ and $\beta$-TCP:HA, respectively.

where $R$ is the reaction force at the fixed support; $A$ is the cross-sectional area; $\frac{dl}{l}$ is the axial strain.

The reaction force for each sample situation was calculated and represented in Fig. 6. For $S_1$, the highest effective Young's modulus 28 GPa is shown by model 0.8_0.3_1 (porosity 39.58%), and 0.4_0.5_4 (porosity 64.13%) has the lowest effective Young's modulus 2.2 GPa. For $S_2$ the highest effective Young's modulus 33.2 GPa is shown by model 0.8_0.3_1 (porosity 39.58%) and 0.4_0.5_4 (porosity 64.13%) has the lowest effective Young's modulus 4.1 GPa. For $S_3$, the highest effective Young's modulus 37.2 GPa is shown by model 0.8_0.3_1 (porosity 39.58%), and 0.4_0.5_4 (porosity 64.13%) has the lowest effective Young's modulus 9.9 GPa. However for $S_4$, the highest effective Young's modulus 19.5 GPa is shown by model 0.8_0.3_1 (porosity 39.58%) and 0.4_0.5_4 (porosity 64.13%) has the lowest effective Young's modulus 0.8 GPa. The originality pattern observed during analysis demonstrates a higher effective Young's modulus with the highest strand diameter $(D)$, lowest pores diameter $(d)$ and orientation angle $(\theta)$, and vice versa for lower effective young's modulus. It shows that effective young's modulus and porosity are inversely proportional to each other, while porosity is directly proportional to the pore

![](./images/812737471732252672_14.jpg)

![](./images/812737471732252672_15.jpg)

**Figure 5:** (continued)

diameter and orientation angle. Figure 6 show the graphs of effective Young's modulus of scaffolds as a function of porosity. All the graphs follow the same trend, showing a decrease in effective Young' modulus with an increase in porosity. Higher strand diameter and lower pore diameter in scaffold models show more effective Young's modulus, as there is less gap between two strands providing more area at any cross section of the scaffold. This makes a scaffold more stable for high compressive loads. As the strand diameter decreases and pore diameter increases (meaning the rise in porosity), the cross-sectional area drops weakening the scaffold and hence decreasing its effective Young's modulus.

Considering Young's modulus of the bone as 18.6 GPa, the optimum porosity and Young's modulus for $S_1$: 0.6_0.5_2, for $S_2$: 0.4_0.4_3 and for $S_3$: 0.4_0.5_2 is found. In $S_4$, the three architecture designs can be considered as optimum that is 0.6_0.3_2; 0.8_0.4_4 and 0.6_0.3_3 showing clearly the adaptability of $\beta$-TCP:HA in many ways for tissue engineering application.

## 5 Conclusion
The scaffolds were designed based on strand diameter, pore diameter and orientation angle. 36 scaffolds were used based on the combinations of the properties for scaffolds. The porosities of each scaffold were determined and it was

![](./images/812737471732252672_16.jpg)

![](./images/812737471732252672_17.jpg)

**Figure 6:** Effective Young's modulus vs. porosity graph for different compositions: $S_1$, $S_2$, $S_3$ and $S_4$ for β-TCP:ZrO₂, β-TCP:MgO, β-TCP:Al2O3 and β-TCP:HA, respectively.

found that the strand and pore diameter had a significant effect on the porosity of the scaffold. Before finding the optimum architecture design via FEA, it is necessary to find the compressive strength for various combinations of the composite. Accordingly, β-TCP is considered as matrix material and $ZrO_2$, $MgO$, $Al_2O_3$ and HA were analyzed with different concentrations. FEA was performed on this composite and the following conclusion was drawn:

1.  For β-TCP:ZrO₂ the composite ratio of 90:10 will promoted as ideal combination by look- ing toward its non-degradability. The archi- tecture of 0.6_0.5_2 as a result of balanced between porosity and effective Young's mod- ulus matching toward natural bone.
2.  For β-TCP:MgO the composite ratio of 90:10 and architecture of 0.4_0.4_1 gives the desired scaffold properties closely matching with cortical bone.
3.  For β-TCP:Al₂O₃ the composite ratio 90:10 and architecture 0.4_0.5_2 provides higher porosity along with good mechanical sta- bility required for BTE.
4.  For β-TCP:HA the composite ratio of 80:20 or 70:30 with 0.6_0.3_2, 0.8_0.4_4 and 0.6_0.3_3 can provide the best combina- tion of porosity and effective Young's mod- ulus close toward the bone tissue.

![](./images/812737471732252672_18.jpg)

Fig. 6.3 S3

![](./images/812737471732252672_19.jpg)

Fig. 6.4 S4

**Figure 6: (continued)**

5. The result of porosity and Young's modulus comparison for all architecture design will help to decide the optimum plan to be considered for a scaffold in BTE.

6. The FEA simulation will reduce the number of trials and time for the determination of the optimum scaffold architecture to be used.

## Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Received: 31 May 2019 Accepted: 20 August 2019
Published online: 13 September 2019

## References
1. Langer R, Vacanti JP (1993) Tissue engineering. Science (80) 260(May):920-926
2. Bagde AD et al (2019) State of the art technology for bone tissue engineering and drug delivery. Irbm 40(3):133-144
3. Sheikh Z, Najeeb S, Khurshid Z, Verma V, Rashid H, Glogauer M (2015) Biodegradable materials for bone repair and tissue engineering applications. Materials (Basel) 8(9):5744-5794
4. Brien FJO, O'Brien FJ, Brien FJO, O'Brien FJ, Brien FJO (2011) Biomaterials and scaffolds for tissue engineering. Mater Today 14(3):32-39
5. Butscher A, Bohner M, Hofmann S, Gauckler L, Müller R (2011) Structural and material approaches to bone tissue

engineering in powder-based three-dimensional printing. Acta Biomater 7(3):907–920

6. Stevens MM (2008) Biomaterials for bone tissue engineering. Mater Today 11(5):18–25

7. O'Brien FJ (2011) Biomaterials and scaffolds for tissue engineering. Mater Today 14(3):32–39

8. Ma H, Feng C, Chang J, Wu C (2018) 3D-printed bioceramic scaffolds: from bone tissue engineering to tumor therapy. Acta Biomater 79:37–59

9. Jammalamadaka U, Tappa K (2018) Recent advances in biomaterials for 3D printing and tissue engineering. J Funct Biomater 9(1):22–36

10. Sapkal PS, Kuthe AM, Kashyap RS, Nayak AR, Kuthe SA, Kawle AP (2016) Indirect fabrication of hydroxyapatite/β-tricalcium phosphate scaffold for osseous tissue formation using additive manufacturing technology. J Porous Mater 23(6):1567–1574

11. Sapkal PS, Kuthe AM, Mathankar S, Deshmukh AA (2017) 3D bio-plotted tricalcium phosphate/zirconia composite scaffolds to heal large size bone defects. MCB Mol Cell Biomech 14(2):125–136

12. Sapkal PS, Kuthe AM, Kashyap RS, Nayak AR, Kuthe SA, Kawle AP (2016) Rapid prototyping assisted fabrication of patient specific β-tricalcium phosphate scaffolds for bone tissue regeneration. J Porous Mater 23(4):927–935

13. Martínez-Vázquez FJ, Cabañas MV, Paris JL, Lozano D, Vallet-Regi M (2015) Fabrication of novel Si-doped hydroxyapatite/gelatine scaffolds by rapid prototyping for drug delivery and bone regeneration. Acta Biomater 15:200–209

14. Ávila-Funes JA, Belaunzarán-Zamudio PF, Tamez-Rivera O, Crabtree-Ramírez B, Navarrete-Reyes AP, Cuellar-Rodríguez J, Sierra-Madero J, Amieva H (2016) 3D silicon doped hydroxyapatite scaffolds decorated with elastin-like recombinamers for bone regenerative medicine. AIDS Res Hum Retrovir 32(2):155–162

15. Thavornyutikarn B, Chantarapanich N, Sitthiseripratip K, Thouas GA, Chen Q (2014) Bone tissue engineering scaffolding: computer-aided scaffolding techniques. Prog Biomater 3:61–102

16. Wen Y et al (2017) 3D printed porous ceramic scaffolds for bone tissue engineering: a review. Biomater Sci 5(9):1690–1698

17. Zhu W, Ma X, Gou M, Mei D, Zhang K, Chen S (2016) 3D printing of functional biomaterials for tissue engineering. Curr Opin Biotechnol 40:103–112

18. Mandrycky C, Wang Z, Kim K, Kim DH (2016) 3D bioprinting for engineering complex tissues. Biotechnol Adv 34(4):422–434

19. Gao B, Yang Q, Zhao X, Jin G, Ma Y, Xu F (2016) 4D Bioprinting for Biomedical Applications. Trends Biotechnol 34(9):746–756

20. Travitzky N et al (2014) Additive manufacturing of ceramic-based materials. Adv Eng Mater 16(6):729–754

21. Inzana JA et al (2014) 3D printing of composite calcium phosphate and collagen scaffolds for bone regeneration. Biomaterials 35(13):4026–4034

22. Bergmann C et al (2010) 3D printing of bone substitute implants using calcium phosphate and bioactive glasses. J Eur Ceram Soc 30(12):2563–2567

23. Chicot D, Tricoteaux A, Lesage J, Leriche A, Descamps M, Rguiti-Constantin E (2013) Mechanical properties of porosity-free beta tricalcium phosphate (β-TCP) ceramic by sharp and spherical indentations. New J Glass Ceram 03(01):16–28

24. Matsumato TJ, An SH, Ishimoto T, Nakano T, Matsumoto T, Imazato S (2011) Zirconia-hydroxyapatite composite material with micro porous structure. Dent Mater 27(11):e205–e212

25. Basu B, Katti DS, Kumar A (2009) Advanced biomaterials fundamentals, processing, and applications. Wiley, USA

26. Mohanty M (1995) Medical applications of alumina ceramics. Trans Indian Ceram Soc 54(5):200–204

27. Kutz M (2009) Standard handbook of biomedical engineering and design, vol 1

28. Radha R, Sreekanth D (2017) Insight of magnesium alloys and composites for orthopedic implant applications: a review. J Magnes Alloy 5(3):286–312

29. Istrate B, Vololeniuc T, Munteanu C, Lupescu ș (2018) Topical notions about in vivo analysis for degradable biomaterials with utility in human body. IOP Conf Ser Mater Sci Eng. https://doi.org/10.1088/1757-899X/374/1/012092

30. Kumar SM, Dhindaw BK (2007) Magnesium alloy-SiCp reinforced infiltrated cast composites. Mater Manuf Process 22(4):429–432

31. Tarafder S, Dernell WS, Bandyopadhyay A, Bose S (2015) SrO- and MgO-doped microwave sintered 3D printed tricalcium phosphate scaffolds: mechanical properties and in vivo osteogenesis in a rabbit model. J Biomed Mater Res B Appl Biomater 103(3):679–690

32. Aminzare M et al (2013) Hydroxyapatite nanocomposites: synthesis, sintering and mechanical properties. Ceram Int 39(3):2197–2206

33. Sapkal PS, Kuthe AM, Kashyap RS, Nayak AR, Kuthe SA, Kawle AP (2016) Indirect casting of patient-specific tricalcium phosphate zirconia scaffolds for bone tissue regeneration using rapid prototyping methodology. J Porous Mater 24:1013. https://doi.org/10.1007/s10934-016-0341-6

34. Liu GR (1997) A step-by-step method of rule-of-mixture of fiber- and particle-reinforced composite materials. Compos Struct 40(3–4):313–322

35. Yuan Z, Li F, Zhang P, Chen B, Xue F (2014) Mechanical properties study of particles reinforced aluminum matrix composites by micro-indentation experiments. Chin J Aeronaut 27(2):397–406

36. Chuan YL, Hoque ME, Pashby I (2013) Prediction of patient-specific tissue engineering scaffolds for optimal design. Int J Model Optim 3(5):468–470

Geometric Modeling and Finite Element Simulation for Architecture Design

37. Bawolin NK, Dolovich AT, Chen DXB, Zhang CWJ (2015) Characterization of mechanical properties of tissue scaffolds by phase contrast imaging and finite element modeling. J Biomech Eng 137(8):081004

38. Wieding J, Jonitz A, Bader R (2012) The effect of structural design on mechanical properties and cellular response of additive manufactured titanium scaffolds. Materials (Basel) 5(8):1336–1347

39. Huh JT, Lee JU, Kim WJ, Yeo M, Kim GH (2018) Preparation and characterization of gelatin/$\alpha$-TCP/SF biocomposite scaffold for bone tissue regeneration. Int J Biol Macromol 110:488–496

40. Luxner MH, Stampfl J, Pettermann HE (2005) Finite element modeling concepts and linear analyses of 3D regular open cell structures. J Mater Sci 40(22):5859–5866

41. Gómez S, Vlad MD, López J, Fernández E (2016) Design and properties of 3D scaffolds for bone tissue engineering. Acta Biomater 42:341–350

42. Singh SP, Bhardwaj T, Shukla M (2017) Lattice modeling and finite element simulation for additive manufacturing of porous scaffolds. 2017 International conference on advances in mechanical, industrial, automation and management systems (AMIAMS 2017): Proceedings, pp 333–336

43. Cahill S, Lohfeld S, McHugh PE (2009) Finite element predictions compared to experimental results for the effective modulus of bone tissue engineering scaffolds fabricated by selective laser sintering. J Mater Sci Mater Med 20(6):1255–1262

44. Eshraghi S, Das S (2012) Micromechanical finite-element modeling and experimental characterization of the compressive mechanical properties of polycaprolactone-hydroxyapatite composite scaffolds prepared by selective laser sintering for bone tissue engineering. Acta Biomater 8(8):3138–3143

45. Eshraghi S, Das S (2010) Mechanical and microstructural properties of polycaprolactone scaffolds with one-dimensional, two-dimensional, and three-dimensional orthogonally oriented porous architectures produced by selective laser sintering. Acta Biomater 6(7):2467–2476

46. Van Cleynenbreugel T, Schrooten J, Van Oosterwyck H, Vander Sloten J (2006) Micro-CT-based screening of biomechanical and structural properties of bone tissue engineering scaffolds. Med Biol Eng Comput 44(7):517–525

47. Loh QL, Choong C (2013) Three-dimensional scaffolds for tissue engineering applications: role of porosity and pore size. Tissue Eng B Rev 19(6):485–502

![](./images/812737471732252672_20.jpg)
A. D. Bagde is currently working as a research scholar at Visvesvaraya National Institute of Technology, Nagpur, India. He did M.Tech. (CAD-CAM), and after that, he pursues his research in biomedical device development and tissue engineering. His area for research is tissue engineering & regenerative medicine, drug delivery, and device development.

![](./images/812737471732252672_21.jpg)
A. M. Kuthe is currently a professor and Head of CAD-CAM center under the Department of Mechanical Engineering, Visvesvaraya National Institute of Technology, Nagpur, India. He started his career after B.E. (Mechanical) from GOCE, Amravati, in Hindustan Aeronautical Limited. He did his M.Tech. (machine design) from IIT Roorkee and joined Birla consultancy services as sr. software engineer and left this company to join VNIT in 1991. He earned a Ph.D. in 2001, and his area of research is rapid prototyping, product development, computer-aided design, and foundry. Recently, he ventures into a domain of tissue engineering and regenerative medicine. He writes one book and holds authorship of more than 50 international peer-reviewed papers.

![](./images/812737471732252672_22.jpg)
S. R. Nagdeve has completed his M.Tech. (CAD-CAM) under the guidance of Prof. Kuthe. He did his B.E. (mechanical) from GCOE, Jalgaon, India. Currently, he is serving as a CAD engineer in industry.

![](./images/812737471732252672_23.jpg)
S. W. Dahake is a post-doctoral fellow in CAD-CAM center, Visvesvaraya National Institute of Technology (VNIT) Nagpur, India. He has completed his Ph.D. in design and development of RP-assisted customized surgical guides for complex surgeries under the supervision of Dr. Abhaykumar M. Kuthe from VNIT Nagpur, India. He holds a bachelor's degree in mechanical engineering and a master's degree in CAD/CAM from RTM Nagpur University, India. His areas of interest include rapid prototyping, CAD/CAM, and biomedical devise manufacturing.

![](./images/812737471732252672_24.jpg)
P. S. Sapkal is a post-doctoral fellow in CAD-CAM center, Visvesvaraya National Institute of Technology (VNIT) Nagpur, India. He has completed his Ph.D. in "Rapid prototyping assisted scaffold fabrication for bone tissue engineering" under the supervision of Dr. Abhaykumar M. Kuthe from VNIT Nagpur, India. His areas of interest include medical devices and bio-printing.

![](./images/812737471732252672_25.jpg)
S. B. Darode is working as Junior Research Fellow & Research scholar at Visvesvaraya National Institute of Technology, Nagpur (India). He holds M.Tech. (heat power) and B.E. (mechanical). His area of research is casting, simulation, and modelling.

J. Indian Inst. Sci. | VOL xxx:x | xxx–xxx 2019 | journal.iisc.ernet.in

![](./images/812737471732252672_26.jpg)

**N. H. Lande** completed her graduation and post-graduation (Biotechnology) from RTMNU, Nagpur India. Currently, she is working as a Project Assistant under BETiC RGSTC funded project in the Tissue engi- neering lab. She has also worked at Central Indian Institute of Medical Sciences, Nagpur, during 2011–2016 under DBT funded project 'Development of Low-cost prognostic kits for Brain stroke patients.' Her expertise is in immunodiagnostic, molecular biology, and animal cell cul- turing. She has nine publications in her credit in national and international journal of repute. Presently, her work is related to identifying cyto-compatibility of materials or scaffold culturing different cell line in vitro, performing cytotoxicity and cell viability assay.

![](./images/812737471732252672_27.jpg)

**B. D. Sarode** is a junior research assistant in CAD-CAM center, VNIT, Nagpur, India. He has completed his. M.Tech. in CAD- CAM engineering from VNIT, and his area of interest includes RP-assisted manufactur- ing, simulation, and CAD.