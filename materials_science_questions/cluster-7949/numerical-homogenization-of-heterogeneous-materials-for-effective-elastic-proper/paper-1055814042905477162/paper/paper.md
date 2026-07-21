![](./images/1055814042905477162_1.jpg)

# Thermal Performance of Lightweight Earth: From Prediction to Optimization through Multiscale Modeling

Séverine Rosa Latapie, Vincent Sabathier, Ariane Abou-Chakra

▶ To cite this version:

Séverine Rosa Latapie, Vincent Sabathier, Ariane Abou-Chakra. Thermal Performance of Lightweight Earth: From Prediction to Optimization through Multiscale Modeling. Construction Materials, 2024, 4 (3), pp.543-565. 10.3390/constrmater4030029 . hal-04824509

HAL Id: hal-04824509

https://hal.science/hal-04824509v1

Submitted on 6 Dec 2024

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

Article

# Thermal Performance of Lightweight Earth: From Prediction to Optimization through Multiscale Modeling

Séverine Rosa Latapie *, Vincent Sabathier and Ariane Abou-Chakra

Laboratoire Matériaux et Durabilité des Constructions (LMDC), National Institute of Applied Sciences (INSA), UPS, Université de Toulouse, 135 Avenue de Rangueil, 31077 Toulouse, France;
vsabathi@insa-toulouse.fr (V.S.); abouchak@insa-toulouse.fr (A.A.-C.)
* Correspondence: slatapie@insa-toulouse.fr

**Highlights:** What are the key points of this study?

- Predictive models: Experimental data are used to develop and calibrate thermal conductivity prediction models.
- Real morphology: Models incorporatethe morphology of lightweight earth materials.
- Optimization: Thermal performance is optimized according to various criteria, enhancing the material's efficiency and applicability.

**Abstract:** This study investigates the prediction of the thermal conductivity of lightweight earth and raw earth blocks incorporating plant aggregates. Given the high variability of raw materials, it is not currently possible to predict the thermal performance of this type of material before sample production. This is a major obstacle to using these eco-materials, although their use is widely encouraged to improve building performance under evolving regulatory frameworks such as The French RE2020 standard. The incorporation of plant aggregates into earth-based materials offers improved insulation properties without compromising their mechanical integrity, positioning them as promising sustainable alternatives. Mean-field homogenization techniques, including the Mori-Tanaka as well as double inclusion models, are used to develop predictive tools for thermal behavior, using rigorously selected experimental data. The selected methods are particularly relevant. The Mori-Tanaka model appears to be better suited when the proportion of aggregates is limited, whereas the double inclusion scheme proves its worth when a higher proportion of aggregates is incorporated. This study emphasizes the influence of aggregate types and processing methods on thermal conductivity, highlighting the need for precise formulation and processing techniques to optimize performance. This paper demonstrates the relevance of the applied homogenization techniques applied. It enables the real morphology of the materials studied, such as aggregate shape and intrinsic cracking, to be taken into account. It contributes to the advancement of eco-material modeling toward predictive digital twins, with the goal of simulating and optimizing complex material behavior under various environmental conditions.

**Keywords:** multiscale modeling; geo-based building materials; thermal conductivity; optimization

---

## 1. Introduction

Composed of plant aggregates coated in a matrix of raw earth, lightweight earth provides insulation while offering a denser material than loose insulation. Such a property not only improves the performance of buildings in terms of summer comfort, but it makes it easier to meet the new targets set by the RE 2020 French standard as well. Lightweight earth is therefore a particularly promising building material. The incorporation of plant aggregates in raw earth blocks, in a lower proportion than in lightweight earth, can also be justified to improve insulation capacity. Interestingly, this incorporation can lead to mechanical properties close to those of raw earth blocks without plant additives. So far,

the literature does not contain any report of any deleterious reaction between the raw earth matrix and the plant aggregate, unlike what occurs with hydraulic matrices used in plant-based concretes [1]. Raw earth-based materials incorporating plant aggregates are therefore of particular interest, hence the decision to consider them as a priority when proposing and validating models for predicting thermal behavior.

This article focuses on thermal conductivity prediction for various lightweight earths and raw earth blocks incorporating plant aggregates. Recent work carried out under the RILEM TC 274-TCE program highlights the difficulty of characterizing this type of composite material, especially from a thermal viewpoint [2]. Temperature and relative humidity conditions influence measurements, although there is no consensus on a well-defined measurement protocol to date [3]. The wide variety of formulations (nature of the plant aggregate, volume fraction of aggregates, etc.) equally complicates an identification of the most significant criteria and increases the growing number of campaigns as confirmed by the literature. Such a variability component probably explains the lack of modeling references in the field of raw earth building materials to date [4]. Authors are led to consider model materials in an attempt to understand the specific nature of these materials [5]. Meanwhile, few modeling studies have explored the possibility of predicting their insulating capacity from formulation data specifically. This study uses mean-field homogenization techniques (the Mori-Tanaka [6] and double inclusion schemes [7]) to offer a tool for predicting the thermal conductivity of these eco-materials.

In this sense, experimental work from the literature is rigorously selected to serve as a basis for the study. Two types of representative volume elements (RVE) are tested to assess the effective thermal conductivity of each of the materials, through a homogenization process. The aim is to identify the most relevant description in line with the actual morphology of the material (shape and orientation of the plant aggregates, cracking stage after the drying phase).

Additionally, the lack of comprehensive porosity data requires further calibration to account for "global cracking". This concept includes both drying cracking in a plane perpendicular to compaction and binder/aggregate porosity. When air inclusions are considered in the RVE, they represent both the cracks within the matrix and the porosity at the matrix/aggregate interface. Particular attention is given to the accessibility and consistency of model input data, although the proportion of composite cracking remains unknown in the selected works. Consequently, this lack of data makes it necessary to formulate working hypotheses.

The proposed RVEs, which are consistent with the actual microstructure of the materials, make it possible to predict the thermal conductivity of rammed earth materials incorporating plant aggregates in a consistent manner. Thence, this study highlights the need for further work to assess the impact of changes in microstructure on the thermal performance of materials. One of the identified goals is to be able to guide pre-production testing and thus contribute to optimizing the formulation of geo-sourced materials. Modeling also enables an exploration of the impact of other parameters such as aggregate shape or orientation. Thence, another goal is to provide modeling results to serve as a basis for discussion on the establishment of thermal conductivity measurement procedures for earth-based building materials that will result in a consensus in the scientific community.

## 2. Material Description
### 2.1. Lightweight Earths

Lightweight earths made from plant aggregates and raw earth binders offer interesting hygrothermal properties and are particularly environmentally friendly, given the local availability, recyclability, and ecological nature of their constituents [8,9]. They provide a very low-impact construction solution. Lightweight earths are manufactured by incorporating plant aggregates (e.g., agricultural by-products) into pre-wetted earth. This earth binder can be obtained from quarry fines from aggregate washing processes coming from

the chemical or concrete industries [10]. Excavated earth can also be used directly on the construction site to produce earth-based building materials [11]. These materials are particularly heterogeneous due to the binding phase, which coats the plant aggregates to a greater or lesser degree. Additionally, the aggregates vary in shape and size (see Figure 1).

![](./images/1055814042905477162_2.jpg)

Figure 1. Picture (left) and several close-ups (right) of lightweight earth (sunflower pith in earth-based binder matrix).

Macroscopically, these materials can be described in two distinct ways. Depending on the formulation, the earth-based binder may be predominant with a few visible aggregates [10]. Alternatively, the aggregates are coated with earth and bonded together (see Figure 1).

### 2.2. Earth-Based Binder
A change in raw-earth binders could be used to predict the thermal behavior of composites so as to help optimize formulations. The aim is to explore how the intrinsic variability of earth can be taken into account on the scale of the resource (earth alone) to explore later on the composite scale. A study is therefore carried out on a wide range of earths and on their thermal conductivities, in an attempt to identify trends that could then be used in modeling.

### 2.3. Plant-Aggregates
The plant aggregates selected for this study in earth-based composites are hemp shiv, sunflower bark, and sunflower pith. Hemp shiv and sunflower bark exhibit macroscopic cylindrical shapes and tubular pores. The aspect ratios were determined through particle size analysis in the studies that provided the thermal conductivities of the composites. Otherwise, they were extracted by the same authors in preliminary works [10], ensuring consistent input data and mitigating the impact of resource variability [12].

The aspect ratio of hemp shiv is 3.3 as reported by Laborel-Préneron et al. (2018) [13], and the aspect ratio of sunflower bark is 3.4 according to Lagouin et al. (2019) [1]. Sunflower pith, characterized by honeycomb pores, is predominantly spherical (see as described by Lagouin et al. (2020) [14], Magniont et al. (2012) [15] and Arufe et al. (2021) [16]) at the macroscopic scale [17] with an aspect ratio very close to 1. The assumption of spherical inclusions for sunflower pith in mean-field homogenization was validated in previous research [18].

### 2.4. Earth-Based Materials Incorporating Plant Aggregates

Experimental data for lightweight earth are selected according to various criteria. Finding studies that provide all the necessary information for the homogenization approach proved challenging. The selected composites and the associated data are listed in Table 1.

Table 1. Earth composites selected for the study: experimental characteristics.

<table>
  <thead>
    <tr>
      <th>Earth Composite</th>
      <th>Reference</th>
      <th>Binder/Aggregate</th>
      <th>Density (kg.m⁻³)</th>
      <th>Volume Fraction of the Aggregate</th>
      <th>Porosity of the Composite (%)</th>
      <th>Thermal Conductivity (W.m⁻¹.K⁻¹)</th>
      <th>Measurement Conditions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FH3-Laborel</td>
      <td rowspan="2">Laborel Préneron et al. 2018 [8]</td>
      <td>FWAS/Hemp shiv</td>
      <td>1519 ± 38</td>
      <td>0.22</td>
      <td>/</td>
      <td>0.30 ± 0.01</td>
      <td rowspan="2">25 °C, dry state</td>
    </tr>
    <tr>
      <td>FH6-Laborel</td>
      <td>FWAS/Hemp shiv</td>
      <td>1271 ± 16</td>
      <td>0.37</td>
      <td>/</td>
      <td>0.20 ± 0.01</td>
    </tr>
    <tr>
      <td>CSP-Belayachi</td>
      <td>Brouard et al. 2018 [19]</td>
      <td>Clay/Sunflower Pith</td>
      <td>235</td>
      <td>/</td>
      <td>90</td>
      <td>0.055</td>
      <td rowspan="2">Dry state</td>
    </tr>
    <tr>
      <td>CSB-Belayachi</td>
      <td>Belayachi et al. 2022 [20]</td>
      <td>Clay/Sunflower Bark</td>
      <td>714</td>
      <td>/</td>
      <td>64</td>
      <td>0.158</td>
    </tr>
  </tbody>
</table>

These materials are used as a basis for comparing the different modeling tools mentioned in Section 3. It is worth noting that the aggregate volume fraction in the study by Laborel-Préneron et al. [8] is determined under the assumption of a binder matrix containing aggregates free from additional porosity. Indeed, these values can be found using the density of the washing fines (binder) and the density and the mass proportion of plant aggregates of each composite. However, the nature of the porosity reported in the work of Belayachi et al. [20] is not specified. For the sunflower pith and clay composite, given its very high value, total porosity (including intra-granular and inter-granular) was assumed.

Furthermore, in order to link the thermal conductivity of the stabilized material to its formulation, i.e., the material in its fresh state, it is valuable to specify the volume fraction of each component. The literature provides information on formulations, summarized in Table 2.

Table 2. Formulation of selected earth-based composites from Labore-Préneron et al. [10] and Brouard et al. [19].

<table>
  <tbody>
    <tr>
      <td>Lightweight Earth</td>
      <td>Binder (%)</td>
      <td>Aggregate (%)</td>
      <td>Water (%)</td>
    </tr>
    <tr>
      <td>FH3-Laborel</td>
      <td>/</td>
      <td>3</td>
      <td>17</td>
    </tr>
    <tr>
      <td>FH6-Laborel</td>
      <td>/</td>
      <td>6</td>
      <td>20</td>
    </tr>
    <tr>
      <td></td>
      <td>Binder/aggregate weight ratio</td>
      <td>Water/binder weight ratio</td>
      <td>Aggregate/clay volume ratio</td>
    </tr>
    <tr>
      <td>CSP-Belayachi</td>
      <td>2.4</td>
      <td>1</td>
      <td>26</td>
    </tr>
    <tr>
      <td>CSB-Belayachi</td>
      <td>2.4</td>
      <td>1</td>
      <td>4.7</td>
    </tr>
  </tbody>
</table>

It is worth noting that authors use varying terminology when discussing formulation, complicating the extraction of input data for modeling purposes. Initially, aggregate volume fractions, calculated from density and mass proportions, did not take additional porosity into account. Subsequently, a 10% porosity was considered to account for the cracking post-drying phase with an adequate preferential orientation . This adjustment is based on literature indicating a high cohesion of these materials [21].

Finally, when applying the double inclusion model, the volume fraction of the coating part becomes a critical input. Though no specific data are available in the literature, a credible value is set at 20%. The percentage of coating is adjusted in the modeling process.

## 3. Methodology

### 3.1. Mean-Field Homogenization (MFH) Methods: Double-Inclusion and Mori-Tanaka Models

To determine the effective thermal conductivity tensor, mean-field theories utilize concentration tensors that relate the averaged fields at the microstructure level (i.e., inclusions and matrix) with the corresponding macroscopic fields. The double-inclusion (D-I) model, based on the theory by Hori and Nemat-Nasser [7], is employed. This model assumes that each inclusion in each phase is surrounded by a hollow inclusion embedded in an outer matrix. Additionally, it is assumed that both inclusions share altogether the same aspect ratio, symmetry axis, center, and volume ratio as the inclusions and matrix in the composite.

By setting the coating phase with the same properties as the matrix, the Mori-Tanaka (M-T) model can be derived from the double-inclusion model. The analytical approach presented here—via the Mori-Tanaka and double inclusion models—is a well-known technique of mean-field homogenization. It is usually applied in disciplines other than earth-based building materials [16–18]. Although such a technique is generally used for elasticity tensor, it can be efficiently transposed to the effective conductivity tensor (refer to its relevance in numerous works [18–22].)

The M-T model is based on an approximate use of Eshelby's solution. Inclusions are embedded in a matrix. Each inclusion is surrounded by a region of the matrix with the interaction between the inclusions and the matrix being averaged. This relationship can be expressed through the following equations [22]:

$$
\underline{\underline{\Lambda}}_{hom} = \sum_{r=1}^{N} f_r \underline{\underline{\Lambda}}_r \cdot \mathbb{A}_r^{MT} \text{ with } \mathbb{A}_r^{MT} = \mathbb{A}_r^O \cdot \left( \sum_{r=0}^{n} f_i \cdot \mathbb{A}_r^O \right)^{-1} \tag{1}
$$

where $\underline{\underline{\Lambda}}_{hom}$ is the effective thermal conductivity tensor of the representative volume element (RVE), $\underline{\underline{\Lambda}}_r$ is the thermal conductivity tensors of the r-th phase (matrix or inclusion), $f_r$ is the volume fraction of the r-th phase, and $\mathbb{A}_r$ is the concentration tensor of the r-th phase.

The concentration tensor is noted $\mathbb{A}_0^0$ for the matrix, and it is equal to the $\underline{\underline{\delta}}$ Kronecker symbol. The inclusions are supposed to have identical properties: their concentration tensor $\mathbb{A}_r^O$ is determined as follows:

$$
\mathbb{A}_r^O = \left[ \underline{\underline{\delta}} + \underline{\underline{P}}_r \cdot \left( \underline{\underline{\lambda}}_i - \underline{\underline{\lambda}}_0 \right) \right]^{-1} \tag{2}
$$

where $\underline{\underline{P}}_r$ is the second-order interaction tensor and $\underline{\underline{\lambda}}_i$ and $\underline{\underline{\lambda}}_0$ are, respectively, the thermal conductivity tensor of the i inclusion and of the 0 matrix.

The inclusion shape is taken into account thanks to the $\underline{\underline{S}}_r$ depolarization tensor which is linked to $P_r$ through the relationship:

$$
\underline{\underline{P}}_r = \underline{\underline{S}}_r \cdot \left( \underline{\underline{\lambda}}_0 \right)^{-1} \tag{3}
$$

### 3.2. Challenges in Homogenization

One of the challenges of homogenization deals with heterogeneous materials with random microstructures. The arrangement of phases is not perfectly known; the microstructure of geo-based building materials is particularly complex, featuring multiscale porosities [23]. Information on phase arrangement at the microscopic level can only be provided through the volume fractions $f_r$ of the constituents as follows [24]:

$$
f_{r}=\frac{V_{r}}{V_{t o t}} \text { with } V_{t o t}=\sum_{r}^{N} V_{r}+V_{m} \tag{4}
$$

where $V_r$ and $V_m$ are, respectively, the volumes of inclusions and of the matrix in the total volume $V_{tot}$ of the RVE.

The application of homogenization models onto the materials considered here is no trivial matter. However, in the literature, material formulations typically only specify the mass relationships between the constituents. This poses a significant challenge in deter- mining the input data for homogenization and, consequently, in calculating the effective thermal conductivity tensor. To address this point, a correspondence between mass ratios and volume ratios can be explored, using X-ray tomography images [25]. In the absence of information for earth-building materials, assumptions about volume fractions at the material scale are necessary, followed by calibration. At the particle scale, previously val- idated methods are used to account for relevant volume fractions [26], such as intra-par- ticle porosity [27,28].

### 3.3. Particulate Orientation
The concentration tensor in Equation (1) depends on a Hill tensor, which takes the variability of the microstructure in terms of the orientation and the shape of the inclusions into account [28].

In the analytical approach proposed here, the orientation of aggregates in composites can be characterized by two angles, with $\Theta$ the angle between the primary axis of the inclusion and the Z-axis in global coordinates and $\varphi$ the angle between the projection of the inclusion onto the $XY$ plane and the $Y$-axis. Image analysis based on microstructure data could provide information on the actual orientation of particles in the composites studied. While some work on plant-based concretes has produced initial results [14], such data are not available for lightweight earth. Due to this lack of precise data on the orien- tation of aggregates within the studied materials, this study adopts two key assumptions.

First, it assumes a fully random orientation of aggregates in all spatial directions, named the "random 3D" assumption as if the implementation technique was free on any no impact on the orientation of the inclusions. Secondly, it assumes that the compaction process during placement results in a random orientation of aggregates confined to the $XY$ plane, termed the "random 2D" assumption. The high compaction rate of the tech- niques used may support this second hypothesis [10].

### 3.4. Particulate Thermal Conductivity tensor
The effective thermal conductivity, influenced by the anisotropy of each RVE, is de- scribed by a tensor with components as follows:

$$
\underline{\underline{\Lambda}}_{E B}=\left(\begin{array}{ccc}
\lambda_{i}^{E B} & 0 & 0 \\
0 & \lambda_{j}^{E B} & 0 \\
0 & 0 & \lambda_{k}^{E B}
\end{array}\right) \tag{5}
$$

These components may vary depending on the orientation of particles, which is sig- nificant in the case of earth-based composites. The manufacturing process can influence the particles' preferred orientation and therefore the properties of the final material [10]. Thus, in order to evaluate the impact of particle shape and orientation on the effective thermal conductivity of the composite, plant aggregates are considered as anisotropic in- clusions in this study.

### 3.5. Representative Volume Element (RVE)

Each constitutive model is based on an RVE to conduct the homogenization process. Consequently, each RVE is carefully defined to take the specific characteristics of lightweight earths into account, in particular the development of cracks perpendicular to compaction after drying [10]. Homogenization enables the determination of effective thermal conductivity in scalar or tensor forms, depending on the calculation assumptions. It should be pointed out that various RVE configurations can be considered by drawing inspiration from both the macro- and microstructure of materials.

First, under the assumption of a low volume fraction of aggregates, the earth matrix contains aggregates as inclusions, with no additional porosity apart from particulate and binder intrinsic porosities. This type of RVE is designated as "EB-1".

In the manufacturing process of lightweight earth, the literature reports the occurrence of cracks perpendicular to compaction after compaction and drying. Cracking in a stabilized state is taken into account by spheroidal air inclusions with an aspect ratio of 20 for consistency (5 to 15 times longer than aggregates), randomly oriented in the plane perpendicular to compaction [10]. This type of RVE is referred to as "EB-2".

Finally, plant particles may appear to be simply embedded within the earth matrix, in a relatively random arrangement. In this context, an RVE describing coated particles bathed in an air matrix looks relevant as well (see Figure 1) This latter case is noted as "HB-3".

Figure 2 provides further illustration of the various models defined in this study.

![](./images/1055814042905477162_3.jpg)

Figure 2. Different types of RVE considered for the analytical homogenization of earth-based materials.

The Mori-Tanaka scheme is applied in the RVE-EB-1 and the RVE-EB-2 patterns. The double inclusion scheme is used for the RVE-EB-3 structure. The two analytical approaches are based on different homogenization assumptions (cf. Section 3.1). In addition, the representative volume elements are significantly different. In the Mori-Tanaka scheme, the binding matrix is represented by earth. In the case of the double inclusion scheme the matrix enclosing the embedded inclusions is made up of air.

### 3.6. Overall Study Strategy

In order to clarify the overall approach carried out in this study, a flowchart has been designed (Figure 3). It highlights three main steps: the input data determination for the homogenization process, the model validation, and the optimization phase according to different criteria.

![](./images/1055814042905477162_4.jpg)

Figure 3. Flowchart of the methodology used in this study.

## 4. Application, Validation and Optimization
### 4.1. Modeling Input Data
#### 4.1.1. Particulate Thermal Conductivity

Thanks to previous work [26,27], particulate thermal conductivity can be determined by both the density of the bulk particles and the thermal conductivity value measured on the same bulk particles. Since the required data are available in the selected references, each component of the particle thermal conductivity tensors is calculated. Hence, these dry reference values at the temperature of 20 °C are selected as reference values. If needed, corrections are made according to the experimental conditions of the thermal conductivity measurements on composites since thermal conductivity depends on temperature and relative humidity. The particulate values calculated and used as input data in the homogenization process are listed in Table 3.

Table 3. Particulate thermal conductivities values calculated under 20 °C and in a dry state.
<table>
<thead>
<tr>
<th rowspan="2">Reference</th>
<th rowspan="2">Type of Aggregate</th>
<th rowspan="2">Calculation Method<br>in Reference of Rosa<br>Latapie et al., 2023 [27–31]</th>
<th colspan="2">Modeled Particulate Thermal<br>Conductivity (W.m⁻¹.K⁻¹)</th>
</tr>
<tr>
<th>$\lambda_{T}$</th>
<th>$\lambda_{N}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Laborel-Préneron et al.,<br>2018 [10]</td>
<td>Hemp shiv</td>
<td rowspan="3">From measurement on bulk<br>particles</td>
<td>0.044</td>
<td>0.066</td>
</tr>
<tr>
<td rowspan="2">Brouard et al., 2022 [19]</td>
<td>Sunflower pith</td>
<td colspan="2">$\lambda_{iso}$= 0.08</td>
</tr>
<tr>
<td>Sunflower bark</td>
<td>0.045</td>
<td>0.068</td>
</tr>
</tbody>
</table>

#### 4.1.2. Binder Thermal Conductivity

A correlation is commonly highlighted in the literature between the density of a bio-sourced material and its thermal conductivity [14]. The purpose of this section is to explore whether this trend is confirmed on the specific scale of earth-based binders. A compilation of literature data [8,32–38] clearly demonstrates that no trend emerges between thermal conductivity and material density (Figure 4). It is therefore necessary to systematically measure the thermal conductivity of the earth material alone used as binder, in order to have this input data for modeling.

![](./images/1055814042905477162_5.jpg)

Figure 4. Thermal conductivity of an earth-based binder as a function of its density [29] [29], [30], [31], [32], [33], [34]

These observations are consistent with various studies that have highlighted the significant variability of earth materials (constituents, clay content, etc.) and the difficulty of predicting their thermal conductivity [39,40].

Thereafter, it is assumed that any change in an earth-based binder requires a thermal conductivity measurement before prediction and optimization. Consequently, changes to raw earth binders are therefore not considered in this study. The original earth binders are maintained for the optimization phase.

### 4.1.3. Volume Fractions
The particulate thermal conductivities determined in the dry state are not corrected (cf. Table 3) since the experimental thermal conductivity measurements are taken on pre-dried composites. The thermal conductivity of the binder is considered constant, although the literature reports sorption—particularly in raw earth materials—and consequent changes in thermal conductivity [34]. Finally, the volume fractions of the aggregates are either extracted from the experimental study [8] or calculated from the mass ratios and densities of the constituents, initially assuming no additional porosity within the final composite [20].

In the case of lightweight earth, the input data—required for the various homogenization calculations carried out in this study—are listed in Table 4.

Table 4. Input data common to modeling for earth-based composites at a dry state and at a temperature of below 25 °C.

<table>
<thead>
<tr>
<th rowspan="3">Composite</th>
<th colspan="3">Earth-Based Binder</th>
<th colspan="5">Aggregate</th>
</tr>
<th rowspan="2">Density (kg.m⁻³)</th>
<th rowspan="2">Thermal Conductivity (W.m⁻¹.K⁻¹)</th>
<th rowspan="2">Particulate Density (kg.m⁻³)</th>
<th colspan="2">Particulate Thermal Conductivity (W.m⁻¹.K⁻¹)</th>
<th rowspan="2">Volume Fraction</th>
<th rowspan="2">Aspect Ratio</th>
</tr>
<tr>
<th>$\lambda_{T}$</th>
<th>$\lambda_{N}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>FH3-Laborel</td>
<td rowspan="2">1891 (FWAS)</td>
<td rowspan="2">0.57 ± 0.03</td>
<td rowspan="2">248</td>
<td rowspan="2">0.044</td>
<td rowspan="2">0.066</td>
<td>0.22</td>
<td rowspan="2">3.3</td>
</tr>
<tr>
<td>FH6-Laborel</td>
<td>0.37</td>
</tr>
<tr>
<td>CSP-Belayachi</td>
<td rowspan="2">900 (clay)</td>
<td rowspan="2">0.27</td>
<td>56</td>
<td colspan="2">$\lambda_{N} = \lambda_{T} = 0.08$ or 0.04</td>
<td>0.79</td>
<td>1</td>
</tr>
<tr>
<td>CSB-Belayachi</td>
<td>425</td>
<td>0.045</td>
<td>0.068</td>
<td>0.39</td>
<td>3.4</td>
</tr>
</tbody>
</table>

### 4.2. Validation
#### 4.2.1. Fine-Based Composites
- FH3-Laborel composite

For the first earth-based building material reference modeled in this study, referred to as HF3-Laborel, the results of the analytical homogenizations are gathered in Figure 5.

![](./images/1055814042905477162_6.jpg)

**Figure 5.** Results of predicted values concerning FH3-Laborel composite compared to the experimental value.

Several aspects can be highlighted in these results: Models using the double inclusion scheme give inconsistent results, diverging from the experimental value by almost 80%. Avoiding the cracking after drying stages results in an overestimation of the experimental value by around 40%.

Moreover, the most appropriate model is undoubtedly the one that considers cracks in a plane perpendicular to compaction, with a deviation of around 15% from the target value. Consequently, the FH3-Laborel-3 model is retained for the rest of the study.

It is noted that the difference between 3D and 2D models is insignificant. The percentage of cracking in this case was initially set arbitrarily at 10%.

The following step is to refine this percentage to calibrate the model from experimental data. It was carried out by considering the average of the components given by the homogenization process to simplify the comparison with the experimental single scalar value (Figure 6).

![](./images/1055814042905477162_7.jpg)

Figure 6. Calibration of cracking percentage in FH3-Laborel-EB-2 type models.

The graph in Figure 6 reveals that with an unassuming cracking percentage of 18%, the model predicts a value within 2% of the experimental one. Thence, this calibrated percentage is adopted for subsequent analysis.

Interestingly enough, the orientation of particles, whether considered or not, has a minimal impact on the model's predicted value, likely due to the cracking's predominant influence perpendicular to compaction. The influence of plant aggregate orientation would therefore be negligible when considering the volume fractions of the actual composite. The FH3-Laborel-EB-2 model is thus retained for this composite to further study the subsequent impact of particle orientation and aspect ratio.

- FH6-Laborel composite

For the FH6-Laborel composite, in which the mass proportion of hemp shiv is twice that of the FH3 composite, the homogenization results also demonstrate the beneficial impact of including cracking on the Mori-Tanaka model (Figure 7).

The key findings include:
- Models only considering the raw earth matrix and aggregates overestimate the effective thermal conductivity of lightweight earth by almost 50%.
- Models based on the double inclusion scheme underestimate the experimental value by an average of 60%.

The most relevant model is clearly the EB-2 model, with a relative deviation from the experimental value of around 20%.

As in the previous section, the adjustment of the volume fraction of air in the composite (i.e., cracking) is necessary before using this model further in the study (Figure 8).

![](./images/1055814042905477162_8.jpg)

Figure 7. Results of predicted values concerning the FH6-Laborel composite compared to the experimental value.

![](./images/1055814042905477162_9.jpg)

Figure 8. Calibration of cracking percentage in FH6-Laborel-EB-2 type models.

Assuming a percentage of 24% cracking, Figure 8 reveals that the model predicts a value within 1% of the experimental value. Consequently, this calibrated value is adopted, and the FH6-Laborel-EB-2 model is selected to represent the FH6-Laborel composite.

With the calibration system, it is worth noting that with calibration a slightly higher cracking value is obtained in the case of the FH 6 composite due to its higher aggregate

content. That element may potentially affect air space due to binder matrix bridging observed in some instances [37].

### 4.2.2. Clay-Based Composites
- **CSP-Belayachi**

In the case of sunflower pith composites, the components of the thermal conductivity tensor are strictly equal for the EB-1 and EB-3 models due to particle isotropy. The consideration of cracking in the case of EB-2 induces a slight anisotropy which is neglected. The values of the normal and tangential components differ by less than 5%. Furthermore, as discussed in the section, the two particulate values of 0.04 and 0.08 W.m⁻¹.K⁻¹ have been tested in the modeling. The predicted values of the different models are compared with the experimental one in Figure 9.

![](./images/1055814042905477162_10.jpg)

Figure 9. Results of predicted values concerning the CSP-Belayachi composite compared to the experimental value.

Regardless of the model considered, taking into account the particle value of 0.08 W.m⁻¹.K⁻¹ systematically overestimates the experimental value by more than 50%. The value of 0.04 W.m⁻¹.K⁻¹ is adopted for the rest of the study as it is considered more relevant in light of these results along with previous work [18]. The EB-1 type model overestimates the experimental value by 40% and is therefore considered unsuitable. Meanwhile, The EB-2 and EB-3 models—based, respectively, on the Mori-Tanaka Model (with the cracking phase) and the double inclusion model—approach the experimental value to less than 15%. Both types of models appear relevant. It may be difficult at this stage to consider any value more valid than the other. Given the lack of data available in the literature, both include arbitrary but plausible values. As a reminder, type EB-2 uses a cracking value of 10%, whereas type EB-3 uses a coating proportion of 20%. Insofar as the aim of the developed models is to best reflect the morphology of the material studied, the double inclusion model is adopted, and the proportion of coating adjusted (Figure 10). Considering the volume fraction of plant aggregates as being close to 80%, the CSP-Belayachi composite appears to be closer to a description in which the coated aggregates are immersed in an air matrix.

![](./images/1055814042905477162_11.jpg)

Figure 10. Calibration of coating percentage in CSP-Belayachi-EB-3-3D model.

In the following sections, particle coating is estimated at 20% for the CSP-Belayachi composite as it provides a deviation between model and experimental values of less than 1%.

-   CSB-Belayachi

The results of thermal conductivity prediction for the CSB-Belayachi composite are presented in Figure 11.

For this composite, the EB-3 type models underestimate the experimental value by over 60%. They are consequently rejected. The EB-1 model, which takes no cracking into account, overestimates the experimental value by 6%. Furthermore, the measurement un- certainty is not specified in the selected references [13,14], but this difference could prob- ably be included in it. A cracking adjustment on the EB-2 model shows that an error of ±1% is reached between the modeled value and the experimental value when considering a cracking of 3% instead of 10% (initial value arbitrarily set). This point is illustrated in Figure 12.

These results demonstrate the consistency of the two types of modeling and the pos- sibility for the given composite to neglect the cracking phenomenon that appears, to a certain extent, after drying. Hereafter, the authors have agreed to adopt the model offering a predicted value closest to that measured one. For this reason, the EB-2-2D model with 3% cracking has been retained for the CSB-Belayachi composite.

![](./images/1055814042905477162_12.jpg)

Figure 11. Results of predicted values concerning the CSB-Belayachi composite compared to the experimental value.

![](./images/1055814042905477162_13.jpg)

Figure 12. Calibration of cracking percentage in CSB-Belayachi-EB-2- models.

### 4.3. Optimization Criteria

To optimize the effective thermal conductivity, this section will be investigating three specific parameters that can influence this property.

### 4.3.1. Influence of Aggregate Type on Thermal Properties
The use of an analytical homogenization approach to investigate how different aggregates influence composite materials is favored. By incorporating sunflower pith, sunflower bark, or hemp shiv, while keeping other parameters constant—such as formulation and processing conditions—the study aims to optimize the material formulation. Undeniably, the impact of these aggregates on effective thermal properties is crucial for enhancing the performance and efficiency of the composite material.

### 4.3.2. Influence of Aspect Ratio Variation on Thermal Conductivity
In the modeling process, the particle aspect ratio is fixed in the first instance. The input values are those specified in Section 2.2. Due to their natural origin and extraction methods, aggregates actually come in a wide range of sizes; this is extensively documented by Granulometric analyses in the literature [40-44]. However, for optimization purposes, it is crucial to examine the impact of the various aspect ratios of the aggregates.

Selecting plant aggregates with uniform shapes for experimental studies is particularly challenging. Indeed, modeling enables the investigation of how plant particle aspect ratios affect thermal properties. Within this scope, the range of aspect ratios selected for this study aligns with data reported in the literature. For instance, hemp shiv has an aspect ratio ranging from 2.28 to 8.75, sunflower bark ranges from 2.99 to 4.74, and sunflower pith varies between 1.00 and 1.50 (Ratsimbazafy et al., 2021 [17]).

### 4.3.3. Influence of Preferential Orientation on Thermal Behavior
Due to the anisotropic thermal behavior of plant particles, the shape of the aggregate necessarily influences the effective thermal conductivity of the resulting geo-sourced composite. In addition, the preferential orientation of these particles within the material—whether due to compaction or spray application [38,39]—adds to the phenomenon and probably amplifies or compensates for the inherent anisotropy of the particles.

Regarding particle orientation, various cases are tested, ranging from random orientations to the extreme case of the perfect alignment of all particles in the same direction. It is important to note that while perfect alignment does not correspond to any practical implementation seen to date, exploring this extreme case allows for a more comprehensive discussion of the material's thermal behavior.

## 5. Results
### 5.1. Initial Modeling
In each study within this section, only the calibrated model appropriate for each composite is utilized. When particle orientation is not specifically examined, a random distribution is adopted if it results in a smaller relative deviation from the experimental value compared to orientation in a plane. To investigate the effect of changing aggregates (either in nature or shape factor), it is assumed that all other modeling parameters remain constant. During the optimization process, the reference thermal conductivity, denoted as $\lambda_{model}^{composite}$, is determined by the modeling results. The thermal conductivities associated with selected models and their calibration values are detailed in Table 5.

Table 5. Recapitulation of the models chosen for each composite and the reference thermal conductivity values before optimization.

<table>
<thead>
<tr>
<th colspan="5">Earth-based materials</th>
</tr>
</thead>
<tbody>
<tr>
<td>Composite</td>
<td>FH3-Laborel</td>
<td>FH6-Laborel</td>
<td>CSP-Belayachi</td>
<td>CSB-Belayachi</td>
</tr>
<tr>
<td>Model type</td>
<td>EB-2-2D</td>
<td>EB-2-2D</td>
<td>EB-3-3D</td>
<td>EB-1-2D</td>
</tr>
<tr>
<td>Calibrated value</td>
<td>18% cracking</td>
<td>24% cracking</td>
<td>15% coating</td>
<td>/</td>
</tr>
<tr>
<td>$\lambda_{composite}$ [W.m⁻¹.K⁻¹]</td>
<td>0.3</td>
<td>0.2</td>
<td>0.055</td>
<td>0.158</td>
</tr>
<tr>
<td>$\lambda_{model}^{composite}$ [W.m⁻¹.K⁻¹]</td>
<td>0.304</td>
<td>0.201</td>
<td>0.055</td>
<td>0.159</td>
</tr>
<tr>
<td>Relative deviation</td>
<td>3%</td>
<td>1%</td>
<td>1%</td>
<td>1%</td>
</tr>
</tbody>
</table>

Calibration allows for a consistent prediction of modeled thermal conductivity to be-low 5% of the experimentally measured value. Based on this value, simulations are con-ducted by varying several criteria: the type of plant aggregate, the aggregate shape factor, and the aggregate orientation.

### 5.2. Influence of Aggregate Type on Thermal Conductivity

Simulation results allow for assessing the impact of each composite's substituted ag-gregate on thermal conductivity (Figure 13). For instance, in a composite, hemp shiv is replaced by sunflower pith or sunflower bark, as described in Section 4.3.1. The compo-sites are abbreviated with letters here below: H for hemp shiv, SP for sunflower pith, and SB for sunflower bark.

![](./images/1055814042905477162_14.jpg)

Figure 13. Impact of a plant aggregate change in lightweight earth.

The sunflower pith stands out as the optimal plant-based aggregate for thermal per-formance across all composite types due to its consistently low particulate thermal con-ductivity. Conversely, composites incorporating sunflower bark exhibit the lowest ther-mal efficiency, which is attributed to its significantly higher particulate thermal conduc-tivity compared to hemp shiv and sunflower pith.

In FH-Laborel composites, substituting hemp shiv with sunflower pith does not no-tably alter thermal conductivity. This is likely due to the similar particulate thermal con-ductivities of the aggregates and the relatively low aggregate volume fractions in FH3 and FH6 composites (less than 50%). However, if sunflower bark is used, thermal conductivity increases by 10% in FH3 and 20% in FH6, consistent with the higher mass fraction in FH6.

### 5.3. Effect of Aggregate Shape on Thermal Conductivity

Due to the variability in resources, the literature reports different aspect ratio values for a given type of plant aggregate [17]. Therefore, assuming a uniform particulate thermal conductivity, the aspect ratios of aggregates in each composite are adjusted across the range documented in the literature (see Section 2.2). These aspect ratios are input data for the homogenization process. The aim is to examine the impact of this variation on each composite's effective thermal conductivity. The outcomes of these homogenization calcu-lations are depicted in Figure 14.

![](./images/1055814042905477162_15.jpg)

Figure 14. Impact of an aggregate aspect ratio change in modeled composites.

Based on our homogenization calculations across the selected composites, the aspect ratio can influence thermal conductivity notably when a wide range of values prevail due to variability in raw materials. However, in comparison to measurement uncertainties, this influence is generally negligible regarding the thermal conductivity of the composites under study. It is substantial to highlight that our modeling assumed fixed aspect ratios, whereas in reality plant aggregates exhibit a specific size distribution, which can be quantified through particle size analysis [40]. This study could therefore be extended by incorporating the results of a granulometric analysis of aggregates used in lightweight earth materials.

### 5.4. Impact of Aggregate Orientation on Thermal Conductivity

Current processing techniques tend to favor a preferential orientation of plant particles in the plane perpendicular to either compaction or projection. In order to consider the development of new techniques that would enable plant aggregates to be oriented differently, the full range of possible orientations has been considered in this study. Different values of the angles described in Section 3.3 are considered and the first results are presented in Figure 15.

![](./images/1055814042905477162_16.jpg)

Figure 15. Impact of a granulate orientation change in modeled composites: case of average thermal conductivity values.

When focusing only on average thermal conductivity values, particle orientation seems to exert minimal influence on thermal conductivity in the studied composites. However, exploring the variability in component values of the thermal conductivity tensor with respect to particle orientation is insightful. Figure 16 illustrates these findings for the considered materials.

![](./images/1055814042905477162_17.jpg)

Figure 16. Impact of a granulate orientation change in modeled lightweight earth: case of thermal conductivity tensor components.

Depending on the orientation of the plant particles, the composite's thermal conduc- tivity in a specific direction can vary about 20% in lightweight earths. In Laborel's FH3 and FH 6 lightweight earths, the low relative volume fraction of aggregates—by volume and, respectively, 22% and 37%—and of cracking in the plane perpendicular to compac- tion attenuate the influence of particle orientation on thermal conductivity. Finally, in the case of the CSB-Belayachi composite, both the relatively moderate volume fraction of sun- flower bark (below 40%) and the effect of the low-conductivity matrix (air) explain the low degree of anisotropy.

In order to be more explicit about the most favorable or unfavorable cases for each of the composites, the following table summarizes the extremum results (Table 6).

<table>
<caption>Table 6. Extreme thermal conductivities for each modeled composite.</caption>
<thead>
<tr>
<th>Earth-based Materials</th>
<th>FH3-Laborel</th>
<th>FH6-Laborel</th>
<th>CSB-Belayachi</th>
</tr>
</thead>
<tbody>
<tr>
<td>Composite</td>
<td>![](./images/1055814042905477162_18.jpg)</td>
<td>![](./images/1055814042905477162_19.jpg)</td>
<td>![](./images/1055814042905477162_20.jpg)</td>
</tr>
<tr>
<td>$\lambda_{max}/\lambda_{min}$</td>
<td>1.2</td>
<td>1.3</td>
<td>1.2</td>
</tr>
</tbody>
</table>

No value can be found in the literature concerning sunflower bark-based composites to assess the relevance of these results. However, in the case of hemp-based composites, the ratio between normal and tangential thermal conductivity reported by experimental

work is about 1.5 for non-optimized composites [27] i.e., where particle alignment is not necessarily identical. According to this work, the ratio is from 1.2 to 1.3 when the hemp particles are aligned in the same direction. The influence of the binder is not considered, as it has an isotropic thermal behavior according to our assumptions. Eventually, modeling results are consistent with the orders of magnitude given in the literature; the results highlight that processing techniques controlling particle orientation could be used to optimize the thermal properties of a geo-sourced material with a given formulation.

## 6. Conclusions
### 6.1. Relevance of Methods Used
In this study, the goal is to develop a reliable tool to predict the thermal conductivity of lightweight earth and raw earth blocks incorporating plant aggregates. Four composites selected from the literature are used to support the modeling work. To ensure consistency, the proposed models take both the macrostructure and the microstructure of the selected materials into account. In cases where data are missing—such as the proportion of cracking after drying or the extent of aggregate coating by the binder matrix—model calibration is proposed.

The approach presented here has proven effective for lightweight earth, maintaining a discrepancy between experimental and modeled thermal conductivity values within 5%, which falls within measurement uncertainties. However, the Mori-Tanaka model may become inconsistent with larger volume fractions of aggregate, making the double inclusion model more appropriate. Overall, the results indicate that mean-field homogenization is a valuable tool for modeling the thermal behavior of earth materials, paving the way for predictive tools to guide formulation choices.

### 6.2. Optimization of Formulations
By validating models for each studied composite, the impact of various criteria on thermal conductivity is evaluated, identifying the type of aggregate as a key factor. This is a significant result with a view to optimizing the formulation of geo-based materials for insulating purposes. While particle orientation seems to exert minimal influence on thermal conductivity in the studied composites, aspect ratio can notably affect thermal conductivity when there is significant variability in raw materials. However, this influence is generally negligible compared to measurement uncertainties. Additionally, the difference between normal and tangential components (along or perpendicular to the compaction axis) can reach 40%, underscoring the importance of appropriate processing techniques in optimizing the thermal performance of geo-sourced materials. These findings highlight the need for a careful consideration of aggregate type and processing methods to achieve optimal thermal efficiency in these composites. In this way, the conclusions of this study could inspire new manufacturing techniques for lightweight earth.

### 6.3. Future Outlooks
This work is a follow-up to the modeling work carried out at the scale of the plant aggregate particle [26], a key element in the homogenization process presented here. The addition of the binder phase constituted by the earth adds difficulty in determining the volume proportion of the binder phase as well as the one due to cracking after drying. Microstructure images such as X-ray tomography images could provide valuable information to avoid the calibration step currently required. To enhance robustness, this approach should be applied to a broader range of geo-sourced materials, as the current study's conclusions are limited to the selected materials.

Additionally, this research suggests the potential for mixing different plant aggregates to accommodate local and seasonal availability. Recent studies indicate that plant aggregates can swell or shrink in response to relative humidity [41]. Quantifying this behavior could enhance the accuracy of models predicting thermal insulation performance. Additionally, models could be further refined by incorporating the variability in aspect

ratio values for the same type of aggregate, addressing the intrinsic variability that has not been considered in this study.

Finally, the developed virtual models represent real geo-based materials and could be further enhanced with new experimental data, such as fire resistance and sustainability indicators. This work serves as a precursor to digital twins, enabling the prediction of the complex behavior of eco-materials under various conditions. For this purpose, the mod- eling process needs to incorporate extensive experimental information [42]. Given the vast diversity of possible formulations for geo-sourced materials, advanced data exploitation techniques—such as Bayesian networks—may help address the inevitable data gaps [43], [44].

Author Contributions: Conceptualization, S.R.L.; methodology, S.R.L.; software, S.R.L.; validation, S.R.L., V.S. and A.A.-C.; formal analysis, S.R.L.; investigation, S.R.L.; resources, S.R.L.; data curation, S.R.L.; writing—original draft preparation, S.R.L. and A.A.-C.; writing—review and editing, S.R.L. and A.A.-C.; visualization, S.R.L.; supervision, A.A.-C.; project administration, S.R.L.; funding ac- quisition, S.R.L. All authors have read and agreed to the published version of the manuscript

Funding: This research received no external funding

Data Availability Statement: The original contributions presented in the study are included in the article, further inquiries can be directed to the corresponding author

Acknowledgments: The authors wish to thank ADEME (Agence française pour le Development et la Maîtrise de l'Energie, the French Energy Agency) and LOCABATI project for financial support of this study.

Conflicts of Interest: The authors declare no conflict of interest.

Nomenclature

Latin symbols
$\underline{\underline{\Lambda}}$
Thermal conductivity tensor
$\mathbb{A}_r$
Concentration tensor
$\underline{\underline{P_R}}$
Interaction tensor
$\underline{\underline{\lambda_i}}$
Thermal conductivity tensor of the inclusion i and the matrix 0.
$\underline{\underline{\lambda_0}}$
Thermal conductivity tensor of the matrix 0
$\underline{\underline{S_R}}$
Depolarization tensor $\underline{\underline{S_R}}$
$f_r$
Volume fraction of r phase
$V_r$
Volume of r phase

Greek symbols
$\lambda$
Thermal conductivity (W/(mK))
$\underline{\underline{\delta}}$
Kronecker symbol

Superscripts
MT
Mori-Tanaka scheme
EB
Earth-based

Subscripts
R
r-th phase
m
Earth-based binder
i,j,k
Reference to the Cartesian coordinate space vector base
tot
Total
hom
Homogeneous materials
T
Parallel to the compaction (for the earth composites) or fiber axis (for ag- gregates)
N
Perpendicular to the compaction (for earth composites) or fiber axis (for aggregates)

Abbreviations
RVE
Representative Volume Element
FWAS
Quarry fines from aggregate washing processing
FH3
Composite with FWAS and hemp shiv

FH6
Composite with FWAS and hemp shiv
CSP
Composite with clay and sunflower pith
CSB
Composite with clay and sunflower bark

## References

1.  Lagouin, M.; Magniont, C.; Sénéchal, P.; Moonen, P.; Aubert, J.-E.; Laborel-préneron, A. Influence of types of binder and plant aggregates on hygrothermal and mechanical properties of vegetal concretes. *Constr. Build. Mater.* 2019, 222, 852–871. https://doi.org/10.1016/j.conbuildmat.2019.06.004.

2.  RILEM. BEC: Bio-Stabilised Earth-Based Construction: Performance-Approach for Better Resilience. Available online: https://www.rilem.net/groupe/bec-bio-stabilised-earth-based-construction-performance-approach-for-better-resilience-447 (accessed on 4 April 2024).

3.  Fabbri, A.; Morel, J.C.; Aubert, J.-E.; Bui, Q.-B.; Gallipoli, D.; Ventura, A.; Reddy, V.B.V.; Hamard, E.; Pele-Peltier, A.; Abhilash, H.N. An overview of the remaining challenges of the RILEM TC 274-TCE, testing and characterisation of earth-based building materials and elements. *RILEM Tech. Lett.* 2021, 6, 150–157. https://doi.org/10.21809/rilemtechlett.2021.149.

4.  Rosa Latapie, S.; Abou-Chakra, A.; Sabathier, V. Bibliometric Analysis of Bio- and Earth-Based Building Materials: Current and Future Trends. *Constr. Mater.* 2023, 3, 474–508. https://doi.org/10.3390/constrmater3040031.

5.  Anglade, E.; Sellier, A.; Aubert, J.-E.; Papon, A. An Experimental Study on Clay and Sand Mixes to Develop a Non-Linear Homogenized Model for Earth Construction Materials. *Constr. Technol. Archit.* 2022, 1, 293–302. https://doi.org/10.4028/www.scientific.net/CTA.1.293.

6.  Mori, T.; Tanaka, K. Average stress in matrix and average elastic energy of materials with misfitting inclusions. *Acta Metall.* 1973, 21, 571–574. https://doi.org/10.1016/0001-6160(73)90064-3.

7.  Hori, M.; Nemat-Nasser, S. Double-inclusion model and overall moduli of multi-phase composites. *Mech. Mater.* 1993, 14, 189–206. https://doi.org/10.1016/0167-6636(93)90066-Z.

8.  Laborel-Préneron, A.; Magniont, C.; Aubert, J.-E. Hygrothermal properties of unfired earth bricks: Effect of barley straw, hemp shiv and corn cob addition. *Energy Build.* 2018, 178, 265–278. https://doi.org/10.1016/j.enbuild.2018.08.021.

9.  Gomes, M.I.; Faria, P.; Gonçalves, T.D. Earth-based mortars for repair and protection of rammed earth walls. Stabilization with mineral binders and fibers. *J. Clean. Prod.* 2018, 172, 2401–2414. https://doi.org/10.1016/j.jclepro.2017.11.170.

10. Laborel-Préneron, A.; Aubert, J.-E.; Magniont, C.; Maillard, P.; Poirier, C. Effect of Plant Aggregates on Mechanical Properties of Earth Bricks. *J. Mater. Civ. Eng.* 2017, 29, 04017244. https://doi.org/10.1061/(ASCE)MT.1943-5533.0002096.

11. Gasnier, H. Construire en Terres D'Excavation, un Enjeu pour la Ville Durable. Ph.D. Thesis, Université Grenoble Alpes, Saint-Martin-d'Hères, France, 2019. Available online: https://theses.hal.science/tel-02165900 (accessed on 4 April 2024).

12. Wang, L.; Lenormand, H.; Zmamou, H.; Leblanc, N. Effect of variability of hemp shiv on the setting of lime hemp concrete, *Ind. Crops Prod.* 2021, 171, 113915, https://doi.org/10.1016/j.indcrop.2021.113915.

13. Laborel-Préneron, A.; Magniont, C.; Aubert, J.-E. Characterization of Barley Straw, Hemp Shiv and Corn Cob as Resources for Bioaggregate Based Building Materials, *Waste Biomass Valori.* 2018, 9, 1095–1112. https://link.springer.com/article/10.1007/s12649-017-9895-z.

14. Lagouin, M.; Magniont, C.; Sénéchal, P.; Moonen, P.; Aubert, J.-E.; Laborel-préneron, A. Influence of types of binder and plant aggregates on hygrothermal and mechanical properties of vegetal concretes. *Constr. Build. Mater.* 2019, 222, 852–871. https://doi.org/10.1016/j.conbuildmat.2019.06.004.

15. Magniont, C.; Escadeillas, G.; Coutand, M.; Oms-Multon, C. Use of plant aggregates in building ecomaterials, *Eur. J. Environ. Civ. Eng.* 2012, 16, 17–33. https://doi.org/10.1080/19648189.2012.682452.

16. Arufe, S.; Hellouin de Menibus, A.; Leblanc, N.; Lenormand, H. Physico-chemical characterisation of plant particles with po- tential to produce biobased building materials, *Ind. Crop. Prod.* 2021, 171, 113901. https://doi.org/10.1016/j.indcrop.2021.113901.

17. Ratsimbazafy, H.H.; Laborel-Preneron, A.; Magniont, C.; Evon, P. A review of the multi-physical characteristics of plant aggre- gates and their effects on the properties of plant-based concrete. *Recent Prog. Mater.* 2021, 3, 1–69. https://doi.org/10.21926/rpm.2102026.

18. Rosa Latapie, S.; Lagouin, M.; Sabathier, V.; Abou-Chakra, A. From aggregate to particleboard: A new multi-scale model ap- proach to thermal conductivity in bio-based materials. *J. Build. Eng.* 2023, 78, 107664. https://doi.org/10.1016/j.jobe.2023.107664.

19. Brouard, Y.; Belayachi, N.; Hoxha, D.; Ranganathan, N.; Méo, S. Mechanical and hygrothermal behavior of clay—Sunflower (*Helianthus annuus*) and rape straw (*Brassica napus*) plaster bio-composites for building insulation. *Constr. Build. Mater.* 2018, 161, 196–207. https://doi.org/10.1016/j.conbuildmat.2017.11.140.

20. Belayachi, N.; Ismail, B.; Brouard, Y. Propriétés effectives thermiques d'un bio-composite à base de tournesol. *Acad. J. Civ. Eng.* 2022, 40, 240–243. https://doi.org/10.26168/ajce.40.1.59.

21. de Menibus, A.H.; Basco, C.; Degrave-Lemeurs, M.; Colinart, T.; Glé, P.; Hamard, E.; Lecompte, T.; Lenormand, H.; Meunier, M.; Vinceslas, T. Étude des bétons biosourcés à base de terre crue et de chanvre dans le cadre du projet ECO-TERRA. *Acad. J. Civ. Eng.* 2018, 36, 25–28. https://doi.org/10.26168/ajce.36.1.7.

22. Eshelby, J.D. The Determination of the Elastic Field of an Ellipsoidal Inclusion, and Related Problems. *Proc. R. Soc. Lond. Ser. A* 1957, 241, 376–396. https://doi.org/10.1098/rspa.1957.0133.

23. Collet, F.; Chamoin, J.; Pretot, S.; Lanos, C. Comparison of the hygric behaviour of three hemp concretes. *Energy Build.* 2013, 62, 294–303. https://doi.org/10.1016/j.enbuild.2013.03.010.

24. Bluhm, J.; De Boer, R. The Volume Fraction Concept in the Porous Media Theory. *ZAMMM—J. Appl. Math. Mech./Z. Für Angew. Math. Mech.* 1997, 77, 563–577. https://doi.org/10.1002/zamm.19970770803

25. Bennai, F.; El Hachem, C.; Abahri, K.; Belarbi, R. Microscopic hydric characterization of hemp concrete by X-ray microtomography and digital volume correlation. *Constr. Build. Mater.* 2018, 188, 983–994. https://doi.org/10.1016/j.conbuildmat.2018.08.198.

26. Rosa Latapie, S.; Sabathier, V.; Abou-Chakra, A. Bio-based building materials: A prediction of insulating properties for a wide range of agricultural by-products. *J. Build. Eng.* 2024, 86, 108867. https://doi.org/10.1016/j.jobe.2024.108867.

27. Rosa Latapie, S.; Lagouin, M.; Douk, N.; Sabathier, V.; Abou-Chakra, A. Multiscale Modelling of Bio-composites: Towards Prediction of Their Thermal Conductivity Based on Adequate Knowledge of Their Constituents. In *Bio-Based Building Materials*; Amziane, S., Merta, I., Page, J., Eds.; RILEM Bookseries; Springer Nature: Cham, Switzerland, 2023; pp. 841–858. https://doi.org/10.1007/978-3-031-33465-8_65.

28. Huang, G.; Abou-Chakra, A.; Geoffroy, S.; Absi, J. A Multi-Scale Numerical Simulation on Thermal Conductivity of Bio-Based Construction Materials. *Constr. Mater.* 2022, 2, 148–165. https://doi.org/10.3390/constrmater2030011.

29. Palumbo, M.; McGregor, F.; Heath, A.; Walker, P. The influence of two crop by-products on the hygrothermal properties of earth plasters. *Build. Environ.* 2016, 105, 245–252. https://doi.org/10.1016/j.buildenv.2016.06.004.

30. Cagnon, H.; Aubert, J.E.; Coutand, M.; Magniont, C. Hygrothermal properties of earth bricks. *Energy Build.* 2014, 80, 208–217. https://doi.org/10.1016/j.enbuild.2014.05.024.

31. Toure, P.M.; Sambou, V.; Faye, M.; Thiam, A. Mechanical and thermal characterization of stabilized earth bricks. *Energy Procedia* 2017, 139, 676–681. https://doi.org/10.1016/j.egypro.2017.11.271.

32. Lima, J.; Faria, P.; Santos Silva, A. Earth Plasters: The Influence of Clay Mineralogy in the Plasters' Properties. *Int. J. Archit. Herit.* 2020, 14, 948–963. https://doi.org/10.1080/15583058.2020.1727064.

33. Hall, M.; Allinson, D. Analysis of the hygrothermal functional properties of stabilised rammed earth materials. *Build. Environ.* 2009, 44, 1935–1942. https://doi.org/10.1016/j.buildenv.2009.01.007.

34. Liuzzi, S.; Hall, M.R.; Stefanizzi, P.; Casey, S.P. Hygrothermal behaviour and relative humidity buffering of unfired and hydrated lime-stabilised clay composites in a Mediterranean climate. *Build. Environ.* 2013, 61, 82–92. https://doi.org/10.1016/j.buildenv.2012.12.006.

35. Liu, L.; He, H.; Dyck, M.; Lv, J. Modeling thermal conductivity of clays: A review and evaluation of 28 predictive models. *Eng. Geol.* 2021, 288, 106107. https://doi.org/10.1016/j.enggeo.2021.106107.

36. Barnaure, M.; Bonnet, S.; Poullain, P. Earth buildings with local materials: Assessing the variability of properties measured using non-destructive methods. *Constr. Build. Mater.* 2021, 281, 122613. https://doi.org/10.1016/j.conbuildmat.2021.122613.

37. Saad, M.; Sabathier, V.; Turatsinze, A. Natural Fibers vs. Synthetic Fibers Reinforcement: Effect on Resistance of Mortars to Impact Loads. In *Construction Technologies and Architecture*; Trans Tech Publications Ltd.: Bäch, Switzerland, 2022; p. 102. https://doi.org/10.4028/www.scientific.net/CTA.1.95.

38. Sáez-Pérez, M.P.; Brümmer, M.; Durán-Suárez, J.A. A review of the factors affecting the properties and performance of hemp aggregate concretes. *J. Build. Eng.* 2020, 31, 101323. https://doi.org/10.1016/j.jobe.2020.101323.

39. Williams, J.; Lawrence, M.; Walker, P. The influence of constituents on the properties of the bio-aggregate composite hemlime. *Constr. Build. Mater.* 2018, 159, 9–17. https://doi.org/10.1016/j.conbuildmat.2017.10.109.

40. Fehrmann, J.; Belleville, B.; Ozarska, B.; Gutowski, W.S.; Wilson, D. Influence of particle granulometry and panel composition on the physico-mechanical properties of ultra-low-density hemp hurd particleboard. *Polym. Compos.* 2023, 44, 7363–7383. https://doi.org/10.1002/pc.27631.

41. Achour, C.; Remond, S.; Belayachi, N. Swelling and shrinkage of plant aggregates: Experimental and treatment effect. *Ind. Crops Prod.* 2023, 203, 117173. https://doi.org/10.1016/j.indcrop.2023.117173.

42. Ghanem, R.; Soize, C.; Mehrez, L.; Aitharaju, V. Probabilistic learning and updating of a digital twin for composite material systems. *Int. J. Numer. Methods Eng.* 2022, 123, 3004–3020. https://doi.org/10.1002/nme.6430.

43. Duprat, F.; Vu, N.T.; Sellier, A. Accelerated carbonation tests for the probabilistic prediction of the durability of concrete structures. *Constr. Build. Mater.* 2014, 66, 597–605. https://doi.org/10.1016/j.conbuildmat.2014.05.103.

44. Biedermann, A.; Taroni, F. Bayesian networks and probabilistic reasoning about scientific evidence when there is a lack of data. *Forensic Sci. Int.* 2006, 157, 163–167. https://doi.org/10.1016/j.forsciint.2005.09.008.

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.