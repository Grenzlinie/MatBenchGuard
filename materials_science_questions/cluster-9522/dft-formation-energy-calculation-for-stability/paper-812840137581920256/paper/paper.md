Accepted Manuscript

![](./images/812840137581920256_1.jpg)

Investigation on mechanical performances of grain boundaries in
hexagonal boron nitride sheets

Qiuyue Ding, Ning Ding, Long Liu, Nan Li,
Chi-Man Lawrence Wu

| PII:       | S0020-7403(18)32041-1                                                                 |
|------------|---------------------------------------------------------------------------------------|
| DOI:       | https://doi.org/10.1016/j.ijmecsci.2018.10.003                                       |
| Reference: | MS 4559                                                                               |
| To appear in: | *International Journal of Mechanical Sciences*                                      |
| Received date: | 25 June 2018                                                                         |
| Revised date:  | 28 September 2018                                                                    |
| Accepted date: | 2 October 2018                                                                       |

Please cite this article as: Qiuyue Ding, Ning Ding, Long Liu, Nan Li, Chi-Man Lawrence Wu,
Investigation on mechanical performances of grain boundaries in hexagonal boron nitride sheets, *In-
ternational Journal of Mechanical Sciences* (2018), doi: https://doi.org/10.1016/j.ijmecsci.2018.10.003

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.

### Highlights
- Systematically investigating the effect of GBs on the mechanical properties and failure behaviors of $h$-BN nanosheets.
- The effect of strain rate and temperature on the mechanical properties and failure behaviors of GBs have been studied.
- Explaining the fracture mechanism of GBs using MD and DFT methods.

# Investigation on mechanical performances of grain boundaries in hexagonal boron nitride sheets

Qiuyue Ding $^{a}$, Ning Ding*$^{a,b}$, Long Liu $^{a}$, Nan Li $^{a}$, Chi-Man Lawrence Wu $^{b}$

$^{a}$ Engineering Research Center of Material Failure Analysis and Safety Assessment, Qilu University of Technology (Shandong Academy of Sciences), Jinan, PR China
$^{b}$ Department of Materials Science and Engineering, City University of Hong Kong, Hong Kong SAR, PR China

*Address correspondence to: Dr. Ning Ding, Department of Mateirals Science and Engineering, City University of Hong Kong, Hong Kong SAR, PR China. E-mail: nding3-c@my.cityu.edu.hk (N. Ding)

### Abstract

In this work, molecular dynamic simulations were performed to investigate the effect of grain boundaries (GBs) on the mechanical properties and failure behaviors of hexagonal boron nitride ($h$-BN) nanosheets. It was confirmed that both the GB linear density and the detailed arrangements of GBs could affect the mechanical properties of $h$-BN sheets. The tensile tests of GB models were performed at different strain rates. Results showed that the ultimate tensile strength of GBs increased obviously with the increasing of strain rate. The effect of temperature on the mechanical properties of $h$-BN sheets was also discussed. Results showed that high temperature could reduce the ultimate tensile strength and Young's modulus of models containing high density of GBs. Molecular dynamics (MD) and density functional theory (DFT) calculation results indicated that the fracture behavior of GBs tended to begin at the bond with the lowest electron density. The information obtained in this work could provide evidence for further investigations of mechanical properties and failure mechanism of $h$-BN sheets with GBs.

Keywords: hexagonal boron nitride, grain boundary, mechanical property, failure behavior, molecular dynamics

### 1. Introduction

Two-dimensional (2D) materials, such as graphene [1-5] and hexagonal boron nitride ($h$-BN) [6-11], have attracted much attention due to their exceptional material properties. $h$-BN, as a close analog of graphene, exhibits many unique properties compared with graphene. For example, $h$-BN possesses a wide band gap of ~5.5 eV [12,13] and displays the electrically insulating properties, which is different from graphene with no band gap and being a semi-metal. Besides, $h$-BN exhibits high thermal and mechanical properties. Due to these unique characteristics, $h$-BN nanosheets have great potential for hydrogen accumulators [14,15], constructing nanodevices [16] and functional nanocomposites [17-18].

Many investigations have been performed to study the effect of defects on the mechanical characterizations of $h$-BN nanosheets. Xiong *et al.* [19] studied the influences of various pre-existing defects on the fracture behaviors of an $h$-BN monolayer nanosheet using molecular dynamics simulation. They found that various pre-existing defects can reduce the ultimate tensile strength and critical failure strain of the $h$-BN monolayer at different extents, and the armchair direction has a stronger ability to resist various defects compared to the zigzag direction. Stephani *et al.* reported the defect formation in many-layer $h$-BN nanosheets using molecular dynamics modeling. They found that the defects formed in the top layer of the many-layer lattice are qualitatively similar to the single layer results, but the presence of the bulk lattice is found to reduce the single vacancy probability in the top-most layer [20].

Grain boundary (GB) is a kind of topological defect, which can affect the electronic, thermal and mechanical properties of materials [21]. Currently, the most suitable method for producing larger-scale $h$-BN sheets is the chemical vapor deposition (CVD) technique [22-25]. Crystal growth during the CVD method leads to the formation of GBs in the place where two grains meet each other. Zettl *et al.* revealed that the main components of GBs in $h$-BN sheets were pentagon-heptagon pairs [26]. Liu *et al.* [27] reported two kinds of dislocation structures, which were square-octagon (4|8) pairs and pentagon-heptagon (5|7) pairs. On the basis of the structure of dislocations, they investigated the GBs and found that GB can be either polar (B-rich or N-rich), constituted by (5|7) pairs, or unpolar, composed of (4|8) pairs.

GB category is an important factor to affect the thermal properties of $h$-BN. Mortazavi et al [28] have investigated the thermal conductivity of polycrystalline h-BN films using molecular dynamics simulations. They constructed polycrystalline h-BN sheets with equivalent grain sizes ranging from 2 nm to 10 nm and evaluated the thermal conductivity of defect-free and ultra-fine grained h-BN films at different temperatures. The reported results proposed that polycrystalline h-BN sheets present high thermal conductivity comparable to monocrystalline sheets. Li et al [29] have studied the thermal properties of grain boundary in planar heterostructure of graphene and h-BN. They found that the thermal transfer efficiency of hybrid GB depended not only on the mismatch angle of grains but also the direction of thermal flux. Besides, the thermal transfer efficiency from graphene to h-BN is higher than that from h-BN

to graphene.

GBs have been revealed to affect not only the thermal conductivity of nanomaterials but also the mechanical properties. Our group has investigated the effect of GBs on the mechanical properties and failure behavior for $h$-BN sheets using DFT [30]. We found that the $h$-BN sheets with different types of GBs showed varied failure behavior, which were caused by the distinct stress distribution on GBs. However, due to the limitation of computing resource, more detailed performance of GBs as well as the effect of temperature and strain rate on mechanical properties and failure behavior of $h$-BN sheets with GBs were not been studied. In 2016, Abadi *et al.* [31] reported the effect of temperature and grain boundary on ultimate tensile strength of single-layer $h$-BN nanosheets using molecular dynamic simulations. They examined six different cases of GBs including four symmetric and two asymmetric models. All of these GBs were just along the zigzag direction. According to the reference [32], the strength of GBs in graphene relied on not only the density of (5|7) pairs, but also on the arrangement of (5|7) pairs. To our best knowledge, although the effect of GBs on mechanical properties of $h$-BN have been investigated by several groups, the effect of GB linear density, GB arrangement along zigzag and armchair directions, temperature and strain rate on mechanical properties of $h$-BN have not been investigated systematically and comprehensively.

In this work, the tensile properties for 27 types of GBs were measured at different temperature and strain rate based on molecular dynamic simulations. The stress-strain relation was investigated and the effect of temperature and strain rate on mechanical

properties for the zigzag and armchair $h$-BN sheets with GBs were obtained. This study is designed to provide useful guidelines for the effect of GBs on mechanical properties of $h$-BN sheets.

## 2. Computational details and GB models

In the present work, MD simulation was used to study the effect of grain boundary on the mechanical properties and failure behaviors of the $h$-BN sheets with GBs. A large-scale atomic/molecular massively parallel simulator (LAMMPS) package was used for the simulation [33]. The interactions between boron and nitrogen atoms were described by Tersoff potential [34-36], which has been used successfully in previous studies on $h$-BN nanosheets [19,37-41]. Kinaci et al [42] have optimized the parameters of the Tersoff potential by fitting the simulation results to the structural, mechanical, and vibrational response of an $h$-BN sheet obtained from first-principles calculations. Using this potential, the energy $E$ of the models was given by:

$$
E=\sum_{i} E_{i}=\frac{1}{2} \sum_{i \neq j} V_{i j}=\frac{1}{2} \sum_{i \neq j}\left(f_{c}\left(r_{i j}\right)\left[f_{R}\left(r_{i j}\right)+b_{i j} f_{A}\left(r_{i j}\right)\right]\right) \tag{1}
$$

where, $r_{i j}$ was the distance between the two neighboring atoms $i$ and $j$. $f_{c}$ was the cutoff function. $f_{A}$ and $f_{R}$ were the attractive and repulsive pair potentials. $b_{i j}$ was a bond-order parameter. The Tersoff parameters were shown in Table 2.

To avoid the effect of size, periodic boundary condition was performed on the computational unit cell. In addition, a vacuum space of $100\ \text{\AA}$ was used to eliminate the interactions between periodic images of $h$-BN sheets. The dimensions of the pristine $h$-BN sheet were around $15\ \text{nm} \times 15\ \text{nm}$. The length of $h$-BN sheets with GBs was set as approximately $15\ \text{nm}$ and the width depended on the type of GBs. The

thickness of $h$-BN sheets was taken as 0.33 nm, which was used previously [43-44].

The zigzag (zz) and armchair (am) directions of the $h$-BN sheet, were oriented along the X and Y axes, respectively.

To investigate the effect of GBs to the mechanical properties and failure behaviors of the $h$-BN sheets, 27 types of GBs and a pristine $h$-BN surface were explored. All kinds of GBs were composed of (5|7) pairs. From a geometrical perspective, a (5|7) pair resembles a disclination dipole, which contains two disclinations of opposite signs [32,41]. The nomenclature of the GB model is shown in Figure S1. A GB of the $h$-BN sheet can be described by two periodic translation vectors (n_L, m_L) and (n_R, m_R) of left and right domains along the defect direction as (n_L, m_L)|(n_R, m_R) [30,45]. The misorientation angle $\theta$, which was defined to describe the mismatching degree, can be calculated by two angles $\theta_L$ and $\theta_R$ [46]:

$$
\theta=\tan ^{-1}\left[\sqrt{3} \mathrm{~m}_{\mathrm{L}} /\left(\mathrm{m}_{\mathrm{L}}+2 \mathrm{n}_{\mathrm{L}}\right)\right]+\tan ^{-1}\left[\sqrt{3} \mathrm{~m}_{\mathrm{R}} /\left(\mathrm{m}_{\mathrm{R}}+2 \mathrm{n}_{\mathrm{R}}\right)\right] \tag{2}
$$

As shown in Figure S1, the inflection and in-plane inflection angles were defined to describe the flection degree of $h$-BN sheets and GBs in the $h$-BN sheets, respectively. The stability of GBs on the $h$-BN surface was described by the formation energy, which can be calculated as [47]

$$
E_{f}=\left(E_{\text {total }}-E_{\mathrm{BN}}-\sum_{i} n_{i} \mu_{i}\right) / 2 L \tag{3}
$$

where $E_{\text {total }}$ and $E_{\mathrm{BN}}$ are the energies of the $h$-BN sheet with and without GBs, respectively. $\mu_{i}$ is the increased $(n_i>0)$ or decreased $(n_i<0)$ chemical potential of boron (nitrogen) atoms. $L$ is the periodic length of GBs. To provide a clearer description of the GBs, we categorized all 27 GBs into four classes: (i) GBs with

different linear density of (5|7) pairs spaced evenly along the zigzag direction (shown in Figure 1); (ii) GBs with different linear density of (5|7) pairs spaced evenly along the armchair direction (shown in Figure S2); (iii) GBs with different linear density of (5|7) pairs spaced unevenly along the zigzag direction (shown in Figure S3); (iv) GBs with different in-plane inflection angles along the armchair direction (shown in Figure S4).

To obtain the optimized structures, we relaxed all of the GB configurations first. During this process, all models were relaxed at 300K by using a constant pressure-temperature ensemble (NPT) for 50 ps and a constant temperature ensemble (NVT) for 30 ps in the absence of the applied stress. The time step was set as 1.0 fs during the simulation. After this equilibration, the MD simulations for the tensile test were performed with a NPT ensemble.

### 3. Results and discussion

To obtain the mechanical properties and observe the fracture behavior of $h$-BN sheets with GBs, a tensile test along the tangential direction of the h-BN surface and perpendicular to the GB line were performed. In this process, a series of uniaxial and in-plane mechanical strains were applied on the $h$-BN sheet in the two opposite direction until the sheet fractured. The load direction during the tensile process was perpendicular to the GB lines. The stress-strain curves of the $h$-BN sheets were plotted according to the tensile test data. Then, the mechanical properties including the Young's modulus, the ultimate tensile strength and the critical failure strain of the $h$-BN sheets were calculated based on the stress-strain curves.

A pristine $h$-BN sheet without GBs was constructed and optimized with all the atomic structure parameters fully relaxed. The lattice constant of the equilibrium $h$-BN model was 2.52 Å, and the B-N bond length was 1.45 Å. These model-parameters were in close agreement with available data from experiments and DFT calculations[48-50].

The tensile test was performed on the pristine $h$-BN sheets at room temperature (300K) and with a constant strain rate of $1{\times}10^{8}\ \text{s}^{-1}$. As shown in Table 1, the ultimate tensile strength and critical failure strain of the pristine $h$-BN sheet were 133 GPa and 27.9 % along the zz direction, whereas those values were 116 GPa and 23.9 % along the am direction. The Young's modulus of the pristine $h$-BN sheet was calculated as 678(zz)/611(am) GPa. These values were in a good agreement with those from previous work[30,37-39,51].

### 3.1 Effect of different types of GBs

In this section, the tensile test was performed on the $h$-BN sheets with GBs at a room temperature (300K) and with a constant strain rate of $1{\times}10^{8}\ \text{s}^{-1}$. The structural parameters and fundamental mechanical properties of all the GB models, including the inflection angle, misorientation angle, periodic length, formation energy, critical failure strain, ultimate tensile strength, Young's modulus and GB linear density, are collected in Table 3. GB linear density was defined as the number of (5|7) pairs per nanometer. For each class of GBs, the misorientation angle decreased with the decreasing GB linear density. GB (4,3)|(3,5) showed the largest amount of GB linear density and misorientation angle. GB (8,7)|(7,8) presented the least amounts of GB linear density and misorientation angle. However, the inflection angles showed no

evident trend for GBs with different linear density. GB (1,17)|(17,1) showed the largest inflection angle among all types of GBs, while its misorientation angle is the smallest compared with other GBs along zigzag direction. Values of the formation energies for all the GBs ranged from 3.24 eV to 8.51 eV. Similar to the inflection angle, the formation energies showed no obvious trend for GBs with different linear density. GBs (8,7)|(7,8) and (2,5)|(5,2) possessed the lowest and highest formation energies, respectively.

Figure 2 shows the stress-strain curves of the pristine $h$-BN sheet and all of the GB models. An obvious brittle fracture characteristic can be observed for most of the $h$-BN models, i.e., the stress first increased with rising strain at a particular rate; when it reached a critical value, the stress decreased rapidly to approximately zero. However, for a fraction of models, such as GB (1,6)|(6,1) and (11,6)|(6,11), when the strain reached a critical value, the stress remained constant with the strain increasing substantially. It indicated that the phenomenon of yielding occurs in some particular $h$-BN sheets due to the existence of GBs. Subsequently, when the strain exceeded a certain value, the stress dropped down sharply. For pristine h-BN sheets under the applied mechanical strain, the bonds mainly suffer elongation and fracture rather than dislocation (e.g. rotational deformation) along the tensile direction, thus, pristine h-BN sheets tend to a brittle fracture. The phenomenon of yielding are particularly obvious for GBs (1,6)|(6,1) and (11,6)|(6,11). It is known that the location of stress concentration near the GBs is affected by the arrangement of (5|7) pairs. And the bonds with high stress concentration usually preferred to break. Taking GB (1,6)|(6,1)

as an example, it was found that the first bond broken happened in a B-N bond between a pentagon ring and an adjacent hexagonal ring (a pentagon/hexagonal bond). After that, the bonds in and near the (5|7) pair have a large place for rotational deformation. Accordingly, during the following tensile process, rotational deformation was the main damage pattern of the bonds rather than bond broken, i.e., the yielding process happened in the system. However, for other GBs which show a brittle fracture feature, e.g. GB (1,7)|(7,1), a hexagonal/hexagonal bond adjacent to the (5|7) pair first breaks. Compared to the fracture of the pentagon/hexagonal bond in GB(1,6)|(6,1), the bonds near GBs in GB (1,7)|(7,1) system have small place to yield rotational deformation. So the phenomenon of yielding for GB (1,7)|(7,1) is not obvious.

As shown in Table 3, the ultimate tensile strength and Young's modulus for all the GBs ranged from 47 GPa to 99 GPa and 429 GPa to 634 GPa, respectively. The critical failure strains for all the GBs varied from 10.4% to 18.2%. GBs (2,6)|(6,2) and (4,3)|(3,4) showed the smallest and largest critical failure strains, respectively. It was found that not only the GB linear density could affect the mechanical properties of $h$-BN sheets, but also the detailed arrangements of GBs were important. As shown in Figure 3(a), the ultimate tensile strength and Young's modulus of the evenly and unevenly spaced GBs with respect to different GB linear densities along zz direction were plotted. Basically, an increase in linear density of zigzag tilt GBs would result in a reduction in ultimate tensile strength for GBs spaced either evenly or unevenly in the $h$-BN sheets. When GB linear density increased from $0.31\ \text{nm}^{-1}$ to $1.51\ \text{nm}^{-1}$, the ultimate tensile strength for evenly spaced GB ranged from 99 GPa to 66 GPa, which

was 74% to 50% that of the pristine $h$-BN sheet (133GPa). The ultimate tensile strength for unevenly spaced GB ranged from 81 GPa to 68 GPa, which was 61% to 51% that of the pristine $h$-BN sheet. For the GBs with the same GB linear density, the ultimate tensile strength of evenly distributed GBs was higher than that of the unevenly spaced GBs. The Young's modulus of the evenly distributed GBs did not show obvious relationship with the GB linear density. GB (6,5)|(5,6) exhibited the largest ultimate tensile strength and Young's modulus. While for the unevenly distributed GBs, the Young's modulus increased at first, and then, when the GB linear density increased to $1.30\ \text{nm}^{-1}$, the Young's modulus decreased with the GB linear density increasing. GB (7,4)|(4,7) and (9,5)|(5,9) showed the largest Young's modulus (616GPa), which was 91% that of the pristine $h$-BN sheets in the zz direction. Similar to the ultimate tensile strength, evenly distributed GBs have a higher Young's modulus compared to the unevenly spaced GBs with the same GB linear density. It indicated that the detailed arrangements of GBs might affect the ultimate tensile strength and Young's modulus of GBs other than GB linear density of GBs. Evenly distributed GBs showed the stronger mechanical properties than the unevenly spaced GBs with the same GB linear density. From Table 3 we can see that the unevenly distributed GBs own the larger misorientation angle compared with the evenly distributed GBs with the same GB linear density. It was believed that an unevenly spaced GB would introduce more mismatches in the $h$-BN surface that led to a weak performance in mechanical properties. From this view of point, increasing the misorientation angle of the grain boundary would reduce the ultimate tensile strength

and Young's modulus of the $h$-BN sheets.

For the mechanical properties of the armchair GB models, the ultimate tensile strength and Young's modulus of all the GBs along the armchair direction were lower than those of the pristine $h$-BN sheet (116 GPa and 611 GPa, respectively). The ultimate tensile strength of the armchair GB models ranged from 63 GPa to 90 GPa, which was about 54% to 78% that of the pristine $h$-BN sheet. GB (1,4)|(4,1) and GB (1,10)|(10,1) showed the strongest and weakest ultimate tensile strength, respectively.
As shown in Figure 3(b), the ultimate tensile strength of GBs along armchair direction generally decreased with the GB linear density increasing. When the GB linear density reached to $1.75\ \text{nm}^{-1}$, the ultimate tensile strength of GBs become 54% that of the pristine armchair $h$-BN. Young's modulus of these models ranged from 549 GPa to 616 GPa. GB (1,10)|(10,1) showed the highest Young's modulus (616 GPa), which was even higher than that of the pristine $h$-BN sheets in the am direction. The Young's modulus also exhibited dependence on the GB linear density. With the increasing of GB linear density, Young's modulus presented a decreased trend.

To further investigate the effect of GB types on mechanical properties of $h$-BN sheets.
The mechanical properties of GBs with different in-plane inflection angles were calculated. As shown in Figure 3(c), with increasing of the in-plane inflection angle, the ultimate tensile strength of GBs decreased at first. When the in-plane inflection angle increased to larger than about $53^\circ$, the ultimate tensile strength of GBs began to rise. Similar to the ultimate tensile strength, Young's modulus of GBs decreased at first, and then increased as in-plane inflection angle of GBs ($>53^\circ$) increasing. When

in-plane inflection angle $\beta$ was small, grain boundaries mainly played the role of a linear defect. When the in-plane inflection angle increased to a certain degree, grain boundaries showed a significant effect on the geometry of areas where was connected with grain boundaries. It had a restrictive effect on adjacent grains, thus significantly improving the mechanical properties of GBs. From Figure 3(c) we could see that GB (2,6)|(6,2) showed the lowest ultimate tensile strength and Young's modulus. GB (1,3)|(3,1) and (1,5)|(5,1)-2 exhibited the highest ultimate tensile strength and Young's modulus, respectively. Besides, we have also compared the mechanical properties of GBs with (4|8) pairs and (5|7) pairs. Due to the serious deformation of GBs with (4|8) pairs, ultimate tensile strength and Young's modulus of (4|8) pairs are weaker than GB (3,1)|(1,3) and GB (1,3)|(3,1), which have the same linear density of GB pairs. The structures of GBs and calculated results are shown in Figure S5 and Table S1.

The effect of inflection angles and misorientation angles on the mechanical properties of $h$-BN sheet were further analyzed. From Figures 4(a) and 4(b), one can see that the ultimate tensile strength and Young's modulus basically decreased as the inflection angle $\alpha$ increasing. As shown in Table 3, the misorientation angles of the GB models were mainly in the range of $0^\circ$~$30^\circ$. In this range, the ultimate tensile strength of GBs exhibited a significant decrease with the increase in the misorientation angles (shown in Figure 4(c)). The relationship between the ultimate tensile strength and misorientation angles can be expressed as

$$
\tau = 60.73 + 57.19 \times 0.92^\theta \tag{4}
$$

According to the equation, when the misorientation angle $\theta=0^\circ$, the ultimate tensile

strength $\tau$ was equal to 118 GPa, which approached to the ultimate tensile strength of the pristine $h$-BN sheet.

The relationship between Young's modulus and misorientation angles is shown in Figure 4(d). Similar to the ultimate tensile strength, the Young's modulus decreased with the rising misorientation angle $\theta$. The relationship between them can be expressed as

$$
E=456.13+182.03 × 0.98^{\theta} \tag{5}
$$

When the misorientation angle $\theta=0^{\circ}$, Young's modulus reached to the highest value (about 638 GPa), which was consistent with the Young's modulus of the pristine $h$-BN sheet. According to the results above, the increasing inflection angles and misorientation angles can weaken the mechanical properties of the $h$-BN sheets.

To further investigate the thermodynamic stability of GBs, we have calculated the inflection angles and misorientation angles of all kinds of GBs at 300K and 1100K. As shown in Table S2, There was no obvious change for the inflection angles and misorientation angles of GBs at 300K and 1100K. It indicated that GBs could stably exist at 1100K and further proved the thermodynamic stability of GBs.

### 3.2 Strain rate effect
The strain rate in a tensile test can substantially affect the mechanical properties of $h$-BN sheet. To analyze the effect of strain rate, tensile tests were performed along the zigzag or armchair directions at 300K with the strain rate ranging from $1×10^8$ s⁻¹ to $5×10^{11}$ s⁻¹. In view of the calculation limit, four types of GB, which were GB(2,1)||(1,2), GB(1,9)||(9,1) GB(5,3)||(3,5) and GB(2,5)||(5,2), were selected for the

tensile test. These four models possess the GB densities of $1.51\ \text{nm}^{-1}$, $0.84\ \text{nm}^{-1}$, $1.15\ \text{nm}^{-1}$ and $2.56\ \text{nm}^{-1}$, respectively. The strain rate dependence of ultimate tensile strength and Young's modulus are shown in Figure 5(a) and Figure 5(b).

As shown in Figure 5(a), for evenly spaced GB (2,1)|(1,2) along the zigzag direction, the ultimate tensile strength remained nearly a constant first with the rising strain rate. When the strain rate $\dot{\varepsilon}>1 \times 10^{9}\ \text{s}^{-1}$ (i.e. $\log\ \dot{\varepsilon}>9$), the ultimate tensile strength increased rapidly from 80 GPa to 199 GPa. Then, a small plateau appeared in the strain rate range from $5 \times 10^{9}\ \text{s}^{-1}$ to $1 \times 10^{10}\ \text{s}^{-1}$, i.e., there was no obvious change for the ultimate tensile strength in this range. As the strain rate $\dot{\varepsilon}>1 \times 10^{10}\ \text{s}^{-1}$, the ultimate tensile strength of GB (2,1)|(1,2) increased again with the rising strain rate and it reached 292 GPa at the strain rate of $5 \times 10^{11}\ \text{s}^{-1}$. For evenly spaced GB (1,9)|(9,1) along the armchair direction, the ultimate tensile strength first increased with the rising strain rate at a relatively high rate. During this process, the ultimate tensile strength increased from 76 GPa with the strain rate of $1 \times 10^{8}\ \text{s}^{-1}$ to 240 GPa with the strain rate of $1 \times 10^{9}\ \text{s}^{-1}$. When the strain rate reached a critical value (about $1 \times 10^{9}\ \text{s}^{-1}$), a plateau also appeared (see the circle in Figure 5(a)), i.e., the ultimate tensile strength remains constant (about 240 GPa) independent of the strain rate. As the strain rate reached to $1 \times 10^{10}\ \text{s}^{-1}$, the ultimate tensile strength rose with the increasing strain rate again at a relatively lower rate than that of the first stage. From Figure 5(a) we could see that ultimate tensile strength of GB (5,3)|(3,5) and GB (2,5)|(5,2), which belonged to GBs spaced unevenly along armchair direction and GBs with different in-plane inflection angles, respectively, showed the similar trends with GB (1,9)|(9,1). With the

strain rate increased, the ultimate tensile strength of GB (5,3)|(3,5) and GB (2,5)|(5,2) first increased with a relatively high rate. When the strain rate reached to about $5{\times}10^9$ s⁻¹, the ultimate tensile strength remains constant. As the strain rate reached to $1{\times}10^{10}$ s⁻¹, the ultimate tensile strength increased again with the increasing strain rate.

Generally speaking, the ultimate tensile strength for both the zigzag and armchair directions increased as the strain rate increasing. A possible reason for the higher strength is that at a larger strain rate, there is less time for the thermal fluctuations of atoms to occur. As fracture results from bond dissociation through thermal vibration, reducing the time for atoms to vibrate would decrease the probability of bond rupture when the energy barrier is being overcome. A plateau occurred along zz and am directions during the process of strain rate increase. It maybe because thermal fluctuations of atoms had no obvious change when strain rate increased from $5{\times}10^9$ s⁻¹ to $1{\times}10^{10}$ s⁻¹ for GB (2,1)|(1,2), GB (5,3)|(3,5), GB (2,5)|(5,2) and from $1{\times}10^9$ s⁻¹ to $1{\times}10^{10}$ s⁻¹ for GB (1,9)|(9,1).

Furthermore, we also examined the strain rate effect on Young's modulus of GBs. As shown in Figure 5(b), when the strain rate $\dot{\varepsilon}<5{\times}10^{10}$ s⁻¹, Young's modulus was nearly a constant independent of strain rate for the four types of GBs. When the strain rate reached to $5{\times}10^{10}$ s⁻¹, Young's modulus of the four types of GBs began to decrease with the rising strain rate. When the strain rate increased to $5{\times}10^{11}$ s⁻¹, Young's modulus dropped to 88% (93%) and 91% (96%) that of the low strain rate ($1{\times}10^8$ s⁻¹) for GB (2,1)|(1,2) (GB (1,9)|(9,1)) and GB (5,3)|(3,5) (GB (2,5)|(5,2)), respectively.

From Figure 5(b) we could see that a relative low strain rate had no obvious effect on

the plastic deformation process of GBs. This phenomenon could also be seen in a graphene/silicene/graphene model [52], which showed an approximate constant Young's modulus with the strain rate increased from $1 \times 10^{7} \mathrm{~s}^{-1}$ to $1 \times 10^{10} \mathrm{~s}^{-1}$.

### 3.3 Temperature effect
As expected, temperature can affect the mechanical properties of h-BN sheet. In this section, we analyzed the tensile process of GB (2,1)|(1,2) and (1,9)|(9,1) at $1 \times 10^{8} \mathrm{~s}^{-1}$ strain rate with the temperature ranging from 1K to 1100K. Ultimate tensile strength and Young's modulus as a function of temperature for GBs (2,1)|(1,2) and (1,9)|(9,1) was plotted in Figure 5(c) and Figure 5(d).

As shown in Figure 5(c), the ultimate tensile strength of GBs (2,1)|(1,2) and (1,9)|(9,1) drop down rapidly with rising temperature. With the temperature increasing from 1K to 1100K, the ultimate tensile strength of GB (2,1)|(1,2) decreased from 98GPa to 43GPa, which corresponds to an weaken of 56%. At the same time, the ultimate tensile strength of GB (1,9)|(9,1) reduced from 90 GPa to 38 GPa, corresponding to an weaken of 58%. The average decreasing rates were about 50 and $47 \mathrm{MPa} \mathrm{K}^{-1}$ for GB (2,1)|(1,2) and GB (1,9)|(9,1), respectively. The temperature effect on Young's modulus for GBs (2,1)|(1,2) and (1,9)|(9,1) was shown in Figure 5(d). The results indicated that Young's modulus for the two chirality GB models decreased with increasing temperature. As temperature increased from 1K to 1100K, the Young's modulus decreased from 648 GPa to 551 GPa for GB(2,1)|(1,2) along zigzag direaction and from 635 GPa to 532 GPa for GB (1,9)|(9,1) along armchair direction.

The reduction in Young's modulus for the two GB models was 15% and 16%,

respectively. The average reduction rates for the two GB models were about 88 and 94
MPa K⁻¹, respectively.

### 3.4 Failure behavior of GBs
To investigate the failure behavior of GBs, four types of GBs were selected to display
and analyze. Each of them belonged to a particular class of GBs mentioned in
Section 2. The snapshots of fracture process for the four GBs are shown in Figure 6
and Figure S6. Figure 6(a) shows the fracture process of GB (6,5)||(5,6) which spaced
evenly with loading along the zigzag direction. For this model, the fracture began
with a B-N bond elongation in a hexagonal ring adjacent to the (5|7) pair rather than
in the (5|7) pair. With the strain increasing from $\varepsilon = 0.1770$ to $\varepsilon = 0.1774$, the
fracture front propagated uniformly along the zigzag edge. The angle between the
zigzag edge and vertical direction was about 35°(see Figure 6(a)). Then, with the
strain increasing to 0.1775, the propagation transits to the hexagonal pair adjacent to
another (5|7) pair in the periodic structure. When the strain reaches to 0.1777, the
$h$-BN sheet with GB (6,5)||(5,6) fails rapidly along the GB line.

The fracture process of GB (1,9)||(9,1) which spaced evenly with loading along the
armchair direction is shown in Figure 6(b). Similar to the fracture process of GB
(6,5)||(5,6), the first step of failure for GB (1,9)||(9,1) was found to be the breaking of a
B-N bond in the hexagonal ring adjacent to the (5|7) pair. However, with the strain
increasing, the fracture point preferred to propagate around the (5|7) pair forming a
large circular defect rather than propagate uniformly along the zigzag edge. The $h$-BN
sheet with GB (1,9)||(9,1) failed at the strain of $\varepsilon = 0.1449$, which is smaller than that

of $h$-BN sheet with GB (6,5)||(5,6).

The failure behaviors of GB (7,4)||(4,7) and GB (1,5)||(5,1)-2, which belong to class iii and iv of GBs, respectively, is shown in Figure S6. One can see that although the pentagon-heptagon pair spaced unevenly in the $h$-BN sheet for GB (7,4)||(4,7), its failure process is similar to GB (6,5)||(5,6) (shown in Figure S6(a)). A B-N bond in hexagonal-hexagonal pair adjacent to the pentagon-heptagon pair first break, and then the crack propagates uniformly along the zigzag edge. Finally, a large defect around the (5|7) pair formed and the $h$-BN sheet abrupt when the strain reached to 0.1401. As shown in Figure S6(b), the failure process of GB (1,5)||(5,1)-2 starts with the breaking of B-B and N-N bonds in the (5|7) pairs. Subsequently, the crack propagates along the GB line and the $h$-BN sheet fails rapidly as the strain reaching to 0.1182.

In order to investigate the behind mechanism for the failure mode revealed by MD calculations, electronic densities of the GB (3,2)||(2,3) and (1,5)||(5,1)-1 were calculated using DFT method. Periodic DFT calculations were carried out by using DMol$^3$ package [53-55]. Exchange-correlation energy was calculated with generalized gradient approximation using the form of function proposed by Perdew-Becke-Ernzerhoff (PBE) functional [56], which belongs to the class of the generalized gradient approximation (GGA) functionals [57]. Calculations were based on double-numeric quality with polarization function basis set using the convergence criterion of $10^{-5}$ a.u. on energy and maximum force of 0.002 Ha A$^{-1}$. A vacuum layer of 100 Å was built to avoid periodic interactions. As shown in Figure 7, the electron density contour of GB (3,2)||(2,3) and (1,5)||(5,1)-1 was plotted. Among all of the

geometry structures, we clearly see that the electron density of the heptagon ring is the lowest. From Figure S6(c) and (d) we can see that the failure behaviors of GB (3,2)|(2,3) and (1,5)|(5,1)-1 began with the N-N (or B-B) bond elongation in the pentagon-heptagon pairs. It indicated that the critical points for failure initiation locate at the bond with the lowest electron density. This phenomenon could also be seen in the CBN heterostructure [29].

## 4. Conclusions
In this work, the effect of GBs on mechanical properties and failure behaviors of the $h$-BN sheets were investigated using MD simulations. Results showed that both the GB linear density and the detailed arrangements of GBs could affect the mechanical properties of $h$-BN sheets. An increase in GB linear density of zigzag tilt GBs would result in a reduction in ultimate tensile strength in the whole. The ultimate tensile strength of evenly spaced GBs was larger than that of unevenly spaced GBs with the same GB linear density. As the inflection angle $\alpha$ and misorientation angles $\theta$ increasing, the ultimate tensile strength and Young's modulus exhibited a downtrend. Raising strain rate enhances the ultimate tensile strength of GBs obviously. However, Young's modulus for GBs was nearly a constant independent of strain rate when the strain rate $\dot{\varepsilon}<5{\times}10^{10}\ \text{s}^{-1}$. As the strain rate reached to $5{\times}10^{10}\ \text{s}^{-1}$, Young's modulus of the GB models began to decrease with rising strain. The ultimate tensile strength and Young's modlus of models containing GBs decreased with increase in temperature. Via both MD simulations and DFT calculations, we can see that the fracture point of GBs tend to locate at the bond with the lowest electron density.

### Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant No. 11404192 and 11605106), the Key Research and Development Project of Shandong Province, China (Grant No. 2017GSF220004), the Shandong Province Special Grant for High-Level Overseas Talents (Grant No. tshw20120745) and the research fund of Shandong Academy of Sciences (Grant No. 2017QN001 and KJHZ201805).

### References

[1] Yang BC, Wang SW, Guo YZ, Yuan JY, Si YB, Zhang SR, et al. Strength and failure behavior of a graphene sheet containing bi-grain-boundaries. Rsc Adv 2014;4:54677-54683.

[2] He LC, Guo SS, Lei JC, Sha ZD, Liu ZS. The effect of stone-thrower-wales defects on mechanical properties of graphene sheets-A molecular dynamics study. Carbon 2014;75:124-132.

[3] Han J, Ryu S, Sohn D, Seyoung I. Mechanical strength characteristics of asymmetric tilt grain boundaries in graphene. Carbon 2014;68:250-257.

[4] Novoselov KS, Geim AK, Morozov SV, Jiang D, Zhang Y, Dubonos SV, et al. Electric field effect in atomically thin carbon films. Science 2004;306:666-669.

[5] Novoselov KS, Jiang D, Schedin F, Booth TJ, Khotkevich VV, Morozov SV, et al. Two-dimensional atomic crystals. Proc Natl Acad Sci 2005;102(30):10451-10453.

[6] Gabriele T, Laurent J, Angelos M. Friction of water on graphene and hexagonal boron nitride from ab initio methods: Very different slippage despite very similar interface structures. Nano Lett 2014;14(12):6872-6877.

[7] Singh SK, Neek-Amal M, Costamagna S, Peeters FM. Thermomechanical properties of a single hexagonal boron nitride sheet. Phys Rev B 2013;87(18):184106.

[8] Li XL, Wu XJ, Zeng XC, Yang JL. Band-gap engineering via tailored line defects in boron-nitride nanoribbons, sheets, and nanotubes. Acs Nano 2012;6(5):4104-4112.

[9] Li H, Zeng XC. Wetting and interfacial properties of water nanodroplets in contact with graphene and monolayer boron-nitride sheets. ACS Nano 2012;6(3):2401-2409.

[10] Rubio A, Corkill JL, Cohen ML. Theory of graphitic boron nitride nanotubes. Phys Rev B Condens Matter Mater Phys 1994;49:5081-5084.

[11] Chopra NG, Luyken RJ, Cherrey K, Crespi VH, Cohen ML, Louie SG. Boron nitride nanotubes. Science 1995;269(5226):966-967.

[12] Blase X, Rubio A, Louie SG, Cohen ML. Stability and band gap constancy of boron nitride nanotubes. Europhys Lett 1994;28:335-340.

[13] Zhang ZH, Guo WL, Dai YT. Stability and electronic properties of small boron nitride nanotubes. J Appl Phys 2009;105(8):084312.

[14] Lu FS, Wang F, Cao L, Kong CY, Huang XC. Hexagonal boron nitride nanomaterials: Advances towards bioapplications. Nanosci Nanotechnol Lett 2012;4(10):949-961.

[15] Pakdel A, Zhi CY, Bando Y, Golberg D. Low-dimensional boron nitride nanomaterials. Mater Today 2012;15(6):256-265.

[16] Dean CR, Young AF, Meric I, Lee C, Wang L, Sorgenfrei S, et al. Boron nitride substrates for high-quality graphene electronics. Nature Nanotech 2010;5:722-726.

[17] Zhi CY, Bando Y, Tang CC, Kuwahara H, Golberg D. Large-scale fabrication of boron nitride nanosheets and their utilization in polymeric composites with improved thermal and mechanical properties. Adv Mater 2009;21:2889-2893.

[18] Gao YW, Gu AJ, Jiao YC, Yang YL, Liang GZ, Hu JT, et al. High-performance hexagonal boron nitride/bismaleimide composites with high thermal conductivity, low coefficient of thermal expansion, and low dielectric loss. Polym Adv Technol 2012;23(5):919-928.

[19] Xiong QL, Li ZH, Tian XG. The defect-induced fracture behaviors of hexagonal boron-nitride monolayer nanosheets under uniaxial tension. J Phys D: Appl Phys 2015;48:375502-375513.

[20] Stephani KA, Boyd ID. Molecular dynamics modeling of defect formation in many-layer hexagonal boron nitride. Nuclear Instruments and Methods in Physics Research B 2015;365:235-239.

[21] Priester L. Grain boundaries: From theory to engineering. Springer Press New York USA 2012.

[22] Kim KK, Hsu A, Jia X, Kim SM, Shi Y, Hofmann M, et al. Synthesis of

monolayer hexagonal boron nitride on Cu foil using chemical vapor deposition. Nano Lett 2012;12(1):161-166.

[23] Tay RY, Griep MH, Mallick G, Tsang SH, Singh RS, Tumlin T, et al. Growth of large single-crystalline two-dimensional boron nitride hexagons on electropolished copper. Nano Lett 2014;14:839-846.

[24] Kim G, Jang AR, Jeong HY, Lee Z, Kang DJ, Shin HS. Growth of high-crystalline, single-layer hexagonal boron nitride on recyclable platinum foil. Nano Lett 2013;13:1834-1839.

[25] Gao Y, Ren W, Ma T, Liu Z, Zhang Y, Liu WB, et al. Repeated and controlled growth of monolayer, bilayer and few-layer hexagonal boron nitride on Pt foils. ACS Nano 2013;7:5199-5206.

[26] Gibb AL, Alem N, Chen JH, Erickson KJ, Criston J, Gautam A, et al. Atomic resolution imaging of grain boundary defects in monolayer chemical vapor deposition-grown hexagonal boron nitride. J Am Chem Soc 2013;135(18):6758-6761.

[27] Liu YY, Zou XL, Yakobson BI. Dislocations and grain boundaries in two-dimensional boron nitride. ACS Nano 2012;6(8):7053-7058.

[28] Mortazavi B, Pereira LFC, Jiang JW, Rabczuk T. Modelling heat conduction in polycrystalline hexagonal boron-nitride films. Scientific reports 2015;5:13228.

[29] Li YF, Wei A, Ye H, Yao HM. Mechanical and thermal properties of grain boundary in planar heterostructure of graphene and hexagonal boron nitride. Nanoscale 2018;10:3497-3508.

[30] Ding N, Wu CML, Li H. The effect of grain boundaries on the mechanical properties and failure behavior of hexagonal boron nitride sheets. Phys Chem Chem Phys 2014;16:23716-23722.

[31] Abadi R, Uma RP, Izadifar M, Rabczuk T. The effect of temperature and topological defects on fracture strength of grain boundaries in single-layer polycrystalline boron-nitride nanosheet. Comput Mater Sci 2016;123:277-286.

[32] Wei YJ, Wu JT, Yin HQ, Shi XH, Yang RG, Dresselhaus M. The nature of strength enhancement and weakening by pentagon-heptagon defects in graphene.

Nat Mater 2012;11(9):759-763.

[33] Plimpton S. Fast parallel algorithms for short-range molecular dynamics. J Comput Phys 1995;117:1-19.

[34] Tersoff J. New empirical approach for the structure and energy of covalent systems. Phys Rev B 1998;37:6991-7000.

[35] Tersoff J. Modeling solid-state chemistry: Interatomic potentials for multicomponent systems. Phys Rev B 1989;39:5566-5568.

[36] Tersoff J. Empirical interatomic potential for carbon, with applications to amorphous carbon. Phys Rev Lett 1988;61:2879-2882.

[37] Mortazavi B, Cuniberti G. Mechanical properties of polycrystalline boron-nitride nanosheets. RSC Advances 2014;4:19137-19143.

[38] Zhao SJ, Xue JM. Mechanical properties of hybrid graphene and hexagonal boron nitride sheets as revealed by molecular dynamic simulations. J Phys D Appl Phys 2013;46:135303-135309.

[39] Han TW, Luo Y, Wang CY. Effects of temperature and strain rate on the mechanical properties of hexagonal boron nitride nanosheets. J Phys D Appl Phys 2014;47:025303-025308.

[40] Mortazavi B, Re´monda Y. Investigation of tensile response and thermal conductivity of boron-nitride nanosheets using molecular dynamics simulations. Physica E 2012; 44:1846-1852.

[41] Wei AR, Li YF, Datta D, Guo H, Lv Z. Mechanical properties of graphene grain boundary and hexagonal boron nitride lateral heterostructure with controlled domain size. Comput Mater Sci 2017;126:474-478.

[42] Kinaci A, Haskins JB, Sevik C, Cagin T. Thermal conductivity of BN-C nanostructures. Phys Rev B 2012;86:115410-115418.

[43] Verma V, Jindal VK, Dharamvir K. Elastic moduli of a boron nitride nanotube. Nanotechnology 2007;4:435711-435716.

[44] Kurdyumov AV, Solozhenko VL, Zelyavski WB. Lattice parameters of boron nitride polymorphous modifications as a function of their crystal-structure perfection. J Appl Crystallogr 1995;28:540-545.

[45] Yazyev OV, Louie SG. Electronic transport in polycrystalline graphene. Nat Mater 2010;9:806-809.

[46] Zhang J, Zhao J. Structure and electronic properties of symmetric and nonsymmetric graphene grain boundaries. Carbon 2013;55:151-159.

[47] Van de Walle CG, Neugebauer J. First-principles calculations for defects and impurities: Applications to III-nitrides. J Appl Phys 2004;95:3851-3879.

[48] Liu L, Feng YP, Shen ZX. Structural and electronic properties of h-BN. Phys Rev B 2003;68:104102.

[49] Peng Q, Ji W, De S. Mechanical properties of the hexagonal boron nitride monolayer: Ab initio study. Comput Mater Sci 2012;56:11-17.

[50] Bosak A, Serrano J, Krisch M, Watanabe K, Taniguchi T, Kanda H. Elasticity of hexagonal boron nitride: inelastic x-ray scattering measurements. Phys Rev B 2006;73:041402.

[51] Kumar R, Mertiny P, Parashar A. Effects of different hydrogenation regimes on mechanical properties of h-BN: A reactive force field study. J Phys Chem C 2016;120(38):21932-21938.

[52] Chung JY, Sorkin V, Pei QX, Chiu CH, Zhang YW. Mechanical properties and failure behaviour of graphene/silicene/graphene heterostructures. J Phys D Appl Phys 2017;50(34):345302.

[53] Delley B. An all-electron numerical method for solving the local density functional for polyatomic molecules. J Chem Phy 1990;92:508-517.

[54] Delley B. Fast calculation of electrostatics in crystals and large molecules. J Phys Chem 1996;100:6107-6110.

[55] Delley B. From molecules to solids with the $DMol^3$ approach. J Chem Phys 2000;113:7756-7764.

[56] Perdew JP, Burke K, Ernzerhof M. Generalized gradient approximation made simple. Phys Rev Lett 1996;77(18):3865-3868.

[57] Perdew JP, Burke K, Wang Y. Generalized gradient approximation for the exchange-correlation hole of a many-electron system. Phy Rev B 1996;54(23):16533-16539.

Figure captions

![](./images/812840137581920256_2.jpg)

Figure 1 Structures of the zigzag tilt GBs spaced evenly with different linear density of (5|7) pairs (nitrogen: blue, boron: pink).

![](./images/812840137581920256_3.jpg)

Figure 2 Stress-strain curves of GBs on the $h$-BN surface and a pristine $h$-BN along its zigzag (BN(ZZ)) and armchair (BN(AC)) directions. (a) Stress-strain curves of BN(ZZ) and GBs with different linear density along the zigzag direction, (b) Stress-strain curves of BN(AC) and GBs with different linear density along the armchair direction, (c) Stress-strain curves of GBs which are unevenly spaced along the zigzag direction , (d) Stress-strain curves of GBs with different in-plane inflection angles.

![](./images/812840137581920256_4.jpg)

Figure 3 Ultimate tensile strength and Young's modulus as a function of GB linear density for GBs which are evenly and unevenly spaced (a) along the zz direction and (b) along the am direction; (c) Ultimate tensile strength and Young's modulus as a function of the in-plane inflection angle for GBs.

![](./images/812840137581920256_5.jpg)

Figure 4 (a) Ultimate tensile strength and (b) Young's modulus of GBs as a function

of the inflection angles; (c) Ultimate tensile strength and (d) Young's modulus of GBs as a function of the misorientation angles.

![](./images/812840137581920256_6.jpg)

Figure 5 (a) Ultimate tensile strength and (b) Young's modulus of four types of GBs as a function of the strain rate. (c) Ultimate tensile strength and (d) Young's modulus of four types of GBs as a function of the temperature.

![](./images/812840137581920256_7.jpg)

Figure 6 Failure processes of (a) GB (6,5)|(5,6) and (b) GB (1,9)|(9,1).

![](./images/812840137581920256_8.jpg)

Figure 7 The electron density contour calculated using density functional theory to
demonstrate the critical bond with lowest electron density. (a) Atomic view of GB
(3,2)|(2,3). (b) Electron density contour for the atoms shown in (a). (c) Atomic view

of GB(1,5)|(5,1)-1. (d) Electron density contour for the atoms shown in (c).

Tables

Table1 Parameters of the pristine $h$-BN sheets including Young's modulus $E$, ultimate intrinsic strength $\tau$ and critical failure strain $\delta$ in the zz or am directions.

<table>
<thead>
<tr>
<th>System</th>
<th>Method</th>
<th>Young's modulus $E$ (GPa)</th>
<th>Ultimate tensile strength $\tau$ (GPa)</th>
<th>Critical failure strain $\delta$ (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6">$h$-BN sheet</td>
<td>Present work MD-Tersoff</td>
<td>678/611 (zz/am)</td>
<td>133/116 (zz/am)</td>
<td>27.9/23.9 (zz/am)</td>
</tr>
<tr>
<td>MD-Tersoff [37]</td>
<td>800-850</td>
<td>$150\pm 15$</td>
<td>30±3</td>
</tr>
<tr>
<td>MD-Tersoff [38]</td>
<td>692.7/739.9 (zz/am)</td>
<td>114.1/126.6 (zz/am)</td>
<td>27.0/28.0 (zz/am)</td>
</tr>
<tr>
<td>MD-Tersoff-like [39]</td>
<td>881.1</td>
<td>133.2</td>
<td>33.2</td>
</tr>
<tr>
<td>MD-ReaxFF[51]</td>
<td>1077/1122 (zz/am)</td>
<td>131/143 (zz/am)</td>
<td>10/11 (zz/am)</td>
</tr>
<tr>
<td>DFT [30]</td>
<td>/</td>
<td>103/87 (zz/am)</td>
<td>24/18 (zz/am)</td>
</tr>
</tbody>
</table>

Table 2 Parameters of the optimized Tersoff potential for the $h$-$BN$ interactions.

<table>
<thead>
<tr>
<th>Parameter</th>
<th>N-N</th>
<th>B-B</th>
<th>B-N or N-B</th>
</tr>
</thead>
<tbody>
<tr>
<td>$m$</td>
<td>3.0</td>
<td>3.0</td>
<td>3.0</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>1.0</td>
<td>1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>$\lambda_{III}$ (Å⁻¹)</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>$c$</td>
<td>17.7959</td>
<td>0.52629</td>
<td>25000</td>
</tr>
<tr>
<td>$d$</td>
<td>5.9484</td>
<td>0.001587</td>
<td>4.3484</td>
</tr>
<tr>
<td>$h$</td>
<td>0.00000</td>
<td>0.5</td>
<td>-0.89000</td>
</tr>
<tr>
<td>$n$</td>
<td>0.6184432</td>
<td>3.9929061</td>
<td>0.72751</td>
</tr>
<tr>
<td>$\beta$</td>
<td>0.019251</td>
<td>0.0000016</td>
<td>0.000000125724</td>
</tr>
<tr>
<td>$\lambda_{II}$(Å⁻¹)</td>
<td>2.6272721</td>
<td>2.0774982</td>
<td>2.199</td>
</tr>
<tr>
<td>$B$(ev)</td>
<td>138.77866</td>
<td>43.132016</td>
<td>340.0</td>
</tr>
<tr>
<td>$R$(Å)</td>
<td>2.0</td>
<td>2.0</td>
<td>1.95</td>
</tr>
<tr>
<td>$D$(Å)</td>
<td>0.1</td>
<td>0.1</td>
<td>0.05</td>
</tr>
<tr>
<td>$\lambda_{I}$(Å⁻¹)</td>
<td>2.8293093</td>
<td>2.2372578</td>
<td>3.568</td>
</tr>
<tr>
<td>$A$(ev)</td>
<td>128.86866</td>
<td>40.0520156</td>
<td>1380.0</td>
</tr>
</tbody>
</table>

Table 3 Parameters for the GB models including the structure vector, inflection angle $\alpha$, misorientation angle $\theta$, the periodic length along the GB line $L$, GB linear density, formation energy $E_f$, Young's modulus $E$, ultimate tensile strength $\tau$ and critical failure strain $\delta$.

<table>
<thead>
<tr>
<th>NO.</th>
<th>Model</th>
<th>Inflection angle $\alpha$ [deg]</th>
<th>Misorientation angle $\theta$ [deg]</th>
<th>Periodic length $L$ [nm]</th>
<th>GB linear density [nm⁻¹]</th>
<th>Formation energy [eV nm⁻¹]</th>
<th>Young's Modulus $E$ [GPa]</th>
<th>Ultimate tensile strength $\tau$ [GPa]</th>
<th>Critical failure strain $\delta$ [%]</th>
</tr>
</thead>
<tbody>
<tr>
<td>—</td>
<td>h-BN(ZZ)</td>
<td>0</td>
<td>0</td>
<td>15.27</td>
<td>0</td>
<td>NA</td>
<td>678</td>
<td>133</td>
<td>27.9</td>
</tr>
<tr>
<td>—</td>
<td>h-BN(AC)</td>
<td>0</td>
<td>0</td>
<td>15.12</td>
<td>0</td>
<td>NA</td>
<td>611</td>
<td>116</td>
<td>23.9</td>
</tr>
<tr>
<td>1</td>
<td>(1,3)|(3,1)</td>
<td>36</td>
<td>27.8</td>
<td>0.90</td>
<td>2.22</td>
<td>4.7</td>
<td>562</td>
<td>79</td>
<td>14.5</td>
</tr>
<tr>
<td>2</td>
<td>(1,4)|(4,1)</td>
<td>35</td>
<td>21.8</td>
<td>1.15</td>
<td>1.75</td>
<td>6.6</td>
<td>549</td>
<td>63</td>
<td>11.7</td>
</tr>
<tr>
<td>3</td>
<td>(1,5)|(5,1)-1</td>
<td>43</td>
<td>17.9</td>
<td>1.39</td>
<td>1.44</td>
<td>6.6</td>
<td>576</td>
<td>83</td>
<td>16.0</td>
</tr>
<tr>
<td>4</td>
<td>(1,6)|(6,1)</td>
<td>49</td>
<td>15.2</td>
<td>1.64</td>
<td>1.22</td>
<td>6.7</td>
<td>570</td>
<td>65</td>
<td>13.5</td>
</tr>
<tr>
<td>5</td>
<td>(1,7)|(7,1)</td>
<td>49</td>
<td>13.2</td>
<td>1.88</td>
<td>1.06</td>
<td>6.5</td>
<td>586</td>
<td>83</td>
<td>16.2</td>
</tr>
<tr>
<td>6</td>
<td>(1,9)|(9,1)</td>
<td>51</td>
<td>10.1</td>
<td>2.38</td>
<td>0.84</td>
<td>5.9</td>
<td>607</td>
<td>76</td>
<td>14.4</td>
</tr>
<tr>
<td>7</td>
<td>(1,10)|(10,1)</td>
<td>50</td>
<td>9.5</td>
<td>2.63</td>
<td>0.76</td>
<td>5.5</td>
<td>616</td>
<td>90</td>
<td>18.0</td>
</tr>
<tr>
<td>8</td>
<td>(1,17)|(17,1)</td>
<td>57</td>
<td>5.7</td>
<td>4.37</td>
<td>0.46</td>
<td>4.8</td>
<td>612</td>
<td>84</td>
<td>15.9</td>
</tr>
<tr>
<td>9</td>
<td>(3,1)|(1,3)</td>
<td>23</td>
<td>32.2</td>
<td>0.90</td>
<td>2.22</td>
<td>4.8</td>
<td>587</td>
<td>66</td>
<td>11.8</td>
</tr>
<tr>
<td>10</td>
<td>(2,1)|(1,2)</td>
<td>26</td>
<td>21.8</td>
<td>1.32</td>
<td>1.51</td>
<td>5.8</td>
<td>627</td>
<td>77</td>
<td>13.6</td>
</tr>
<tr>
<td>11</td>
<td>(3,2)|(2,3)</td>
<td>39</td>
<td>13.2</td>
<td>2.18</td>
<td>0.92</td>
<td>5.7</td>
<td>615</td>
<td>93</td>
<td>17.0</td>
</tr>
<tr>
<td>12</td>
<td>(4,3)|(3,4)</td>
<td>43</td>
<td>9.4</td>
<td>3.03</td>
<td>0.66</td>
<td>4.8</td>
<td>595</td>
<td>97</td>
<td>18.2</td>
</tr>
<tr>
<td>13</td>
<td>(5,4)|(4,5)</td>
<td>49</td>
<td>8.9</td>
<td>3.89</td>
<td>0.51</td>
<td>4.3</td>
<td>626</td>
<td>95</td>
<td>17.3</td>
</tr>
<tr>
<td>14</td>
<td>(6,5)|(5,6)</td>
<td>38</td>
<td>6.2</td>
<td>4.76</td>
<td>0.42</td>
<td>3.9</td>
<td>634</td>
<td>99</td>
<td>17.4</td>
</tr>
<tr>
<td>15</td>
<td>(7,6)|(6,7)</td>
<td>40</td>
<td>5.1</td>
<td>5.62</td>
<td>0.36</td>
<td>3.5</td>
<td>621</td>
<td>94</td>
<td>16.7</td>
</tr>
<tr>
<td>16</td>
<td>(8,7)|(7,8)</td>
<td>41</td>
<td>4.0</td>
<td>6.49</td>
<td>0.31</td>
<td>3.2</td>
<td>601</td>
<td>90</td>
<td>16.5</td>
</tr>
<tr>
<td>17</td>
<td>(5,3)|(3,5)</td>
<td>50</td>
<td>16.4</td>
<td>3.49</td>
<td>1.15</td>
<td>6.1</td>
<td>615</td>
<td>81</td>
<td>14.6</td>
</tr>
<tr>
<td>18</td>
<td>(7,4)|(4,7)</td>
<td>50</td>
<td>17.9</td>
<td>4.81</td>
<td>1.25</td>
<td>6.2</td>
<td>616</td>
<td>79</td>
<td>13.9</td>
</tr>
<tr>
<td>19</td>
<td>(9,5)|(5,9)</td>
<td>45</td>
<td>18.2</td>
<td>6.13</td>
<td>1.30</td>
<td>6.3</td>
<td>616</td>
<td>76</td>
<td>13.4</td>
</tr>
<tr>
<td>20</td>
<td>(11,6)|(6,11)</td>
<td>51</td>
<td>18.4</td>
<td>7.46</td>
<td>1.34</td>
<td>6.3</td>
<td>605</td>
<td>68</td>
<td>12.6</td>
</tr>
<tr>
<td>21</td>
<td>(6,4)|(4,6)</td>
<td>49</td>
<td>12.2</td>
<td>2.17</td>
<td>0.92</td>
<td>5.9</td>
<td>600</td>
<td>77</td>
<td>13.8</td>
</tr>
<tr>
<td>22</td>
<td>(8,6)|(6,8)</td>
<td>53</td>
<td>10.8</td>
<td>3.03</td>
<td>0.66</td>
<td>5.2</td>
<td>577</td>
<td>79</td>
<td>14.7</td>
</tr>
<tr>
<td>23</td>
<td>(10,8)|(8,10)</td>
<td>51</td>
<td>7.1</td>
<td>3.93</td>
<td>0.51</td>
<td>4.7</td>
<td>564</td>
<td>74</td>
<td>17.6</td>
</tr>
<tr>
<td>24</td>
<td>(1,5)|(5,1)-2</td>
<td>29</td>
<td>18.6</td>
<td>1.39</td>
<td>1.44</td>
<td>7.0</td>
<td>645</td>
<td>69</td>
<td>11.7</td>
</tr>
<tr>
<td>25</td>
<td>(2,5)|(5,2)</td>
<td>40</td>
<td>32.2</td>
<td>1.56</td>
<td>2.56</td>
<td>8.5</td>
<td>504</td>
<td>69</td>
<td>12.7</td>
</tr>
</tbody>
</table>


<table>
  <tr>
    <td>26</td>
    <td>(2,6)(6,2)</td>
    <td>34</td>
    <td>28.8</td>
    <td>1.80</td>
    <td>2.22</td>
    <td>5.3</td>
    <td>429</td>
    <td>47</td>
    <td>10.4</td>
  </tr>
  <tr>
    <td>27</td>
    <td>(4,3)(3,5)</td>
    <td>41</td>
    <td>54.4</td>
    <td>1.09</td>
    <td>3.67</td>
    <td>6.6</td>
    <td>544</td>
    <td>52</td>
    <td>13.3</td>
  </tr>
</table>


Graphical Abstract

![](./images/812840137581920256_9.jpg)