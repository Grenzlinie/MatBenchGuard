![](./images/811702140597698560_1.jpg)

# Emerald Insight

![](./images/811702140597698560_2.jpg)

## International Journal of Structural Integrity
Using a standard specimen for crack propagation under plain strain conditions
R. Branco J.M. Silva V. Infante F. Antunes F. Ferreira

### Article information:

To cite this document:
R. Branco J.M. Silva V. Infante F. Antunes F. Ferreira, (2010),"Using a standard specimen for crack propagation under plain strain conditions", International Journal of Structural Integrity, Vol. 1 Iss 4 pp. 332 - 343

Permanent link to this document:
http://dx.doi.org/10.1108/17579861011099169

Downloaded on: 20 June 2016, At: 21:42 (PT)
References: this document contains references to 29 other documents.
To copy this document: permissions@emeraldinsight.com
The fulltext of this document has been downloaded 1427 times since 2010*

Access to this document was granted through an Emerald subscription provided by emerald-srm:277515 []

### For Authors

If you would like to write for this, or any other Emerald publication, then please use our Emerald for Authors service information about how to choose which publication to write for and submission guidelines are available for all. Please visit www.emeraldinsight.com/authors for more information.

### About Emerald www.emeraldinsight.com

Emerald is a global publisher linking research and practice to the benefit of society. The company manages a portfolio of more than 290 journals and over 2,350 books and book series volumes, as well as providing an extensive range of online products and additional customer resources and services.

Emerald is both COUNTER 4 and TRANSFER compliant. The organization is a partner of the Committee on Publication Ethics (COPE) and also works with Portico and the LOCKSS initiative for digital archive preservation.

*Related content and download information correct at time of download.

![](./images/811702140597698560_3.jpg)
The current issue and full text archive of this journal is available at
www.emeraldinsight.com/1757-9864.htm

# Using a standard specimen for crack propagation under plain strain conditions

R. Branco
CEMUC, Department of Mechanical Engineering, ISEC,
Polytechnic Institute of Coimbra, Coimbra, Portugal

J.M. Silva
Department of Aerospace Sciences, University of Beira Interior,
Covilhã, Portugal

V. Infante
Department of Mechanical Engineering, Technical University of Lisbon,
Lisboa, Portugal

F. Antunes
CEMUC, Department of Mechanical Engineering, University of Coimbra,
Coimbra, Portugal, and

F. Ferreira
División de Aeronáutica y Espacio, Altran, Miñano, Spain

## Abstract
Purpose - Stress state has a major influence on different phenomena, namely those involving diffusion and plastic deformation (like crack closure and high-temperature fatigue crack growth, void formation or ductile fracture). The isolation of plane stress and plane strain states is crucial in fundamental studies of material behavior. The isolation of plane stress state is achieved with thin specimens, whilst the isolation of plane strain state is usually done increasing the thickness or introducing lateral grooves. The purpose of this paper is to propose a specimen geometry able to isolate the plane strain state, based on the standard M(T) geometry.

Design/methodology/approach - A numerical study was carried out aiming at obtaining a stress triaxiality parameter, h, as a function of different geometrical features of the specimen, such as the notch radius, notch depth and specimen thickness.

Findings - Results show that a pure plane strain state is achievable (i.e. 97 percent of specimen thickness has $h > 0.97$) if a specimen with optimized geometrical features is used, which corresponds to a notch radius of 0.5 mm, a notch depth of 1 mm and a total specimen thickness of 12.56 mm.

Originality/value - This type of specimen geometry is a simple and efficient alternative to other common approaches used to obtain pure plain strain conditions for experimental purposes.

Keywords Fatigue, Test specimens, Strain measurement, Stress (materials)
Paper type Research paper

The authors are indebted to the Portuguese Foundation for the Science and Technology (FCT) through COMPETE program from QREN and to FEDER (European Regional Development Fund) for the financial support (Project PTDC/EME-PME/114892/2009).

![](./images/811702140597698560_4.jpg)

International Journal of Structural
Integrity
Vol. 1 No. 4, 2010
pp.332-343
© Emerald Group Publishing Limited
1757-9864
DOI 10.1108/17579861011099169

### Nomenclature

|  |  |  |  |
| --- | --- | --- | --- |
| a, 2a | = Half-crack length, crack length | $\mathrm{pt_h}$ | = Portion of thickness with $h$ greater than a predefined value |
| $b$ | = Groove depth | $\mathrm{r}$ | = Concordance radius at groove tip |
| E | = Young's modulus | $\mathrm{t_0}$ | = Original thickness |
| FEM | = Finite element method | $\mathrm{t}$ | = Reduced thickness $(= t_0$-$2b)$ |
| $\Theta$, h | = Stress triaxiality parameters | W | = Specimen's width |
| L | = Specimen's length | $\mathrm{z/t}$ | = Fraction of reduced thickness |
| M(T) | = Middle-cracked tension specimen | $\alpha$ | = Groove angle |
| n | = Layer number | $\nu$ | = Poisson's ratio |

Crack
propagation

### 1. Introduction

Stress state has a major influence on different phenomena, namely, crack closure, high-temperature fatigue (HTF) crack growth and void formation in ductile materials. In the near surface regions of a crack front the plane stress state dominates, whilst at interior positions there is a plane strain state condition. The isolation of plane stress state is achieved with relatively thin specimens, whereas the study of plane strain situations is usually achieved with relatively thick specimens. However, in this latter case the plane stress state at surface still exists and experimental procedure requires more material and high loads. The inclusion of lateral grooves on the specimens is a solution to isolate plane strain state in relatively thin specimens, and this will be exploited here.

In general, all diffusion processes are influenced by the triaxiality of stress state. An important example of this effect is HTF crack growth in nickel-base superalloys. Significant tunneling effect has been observed in compact specimen (CT) and corner crack specimens as a result of the influence of stress state on oxidation (Tong *et al.*, 1997; Webster and Ainsworth, 1994). At surface, the plane stress state promotes cyclic plastic deformation and propagation is predominantly transgranular (Antunes *et al.*, 2001). Inside, the stress triaxiality associated with plane strain state accelerates oxygen diffusion, which promotes an intergranular and time-dependent propagation mode. Hydrogen-induced cracking is also susceptible to stress triaxiality (Cayón *et al.*, 2003).

The plastic deformation of metals is also greatly affected by the stress state, as it is evident in ductile fracture of metals and plasticity-induced crack closure (PICC). Ductile fracture in metallic alloys usually follows a multi-step failure process involving several mechanisms: nucleation of microscopic voids by fracture or decohesion of second-phase inclusions, growth of voids induced by plastic straining, localization of plastic flow between the enlarged voids and final tearing of the ligaments between enlarged voids (Van Stone *et al.*, 1985). All these mechanisms are greatly affected by the stress state (Kim *et al.*, 2004). Concerning PICC, there is a general agreement that plane stress state has significantly larger levels of crack closure compared with plane strain loading conditions. A significant number of numerical (Fleck and Smith, 1982; Pommier, 2002; Sehitoglu and Sun, 1991) and experimental studies (Pippan *et al.*, 1994) focusing on plane strain PICC have been carried out, but the level and even the existence of PICC under plane strain conditions still are controversial. Numerical simulation of plane strain PICC is achieved with adequate boundary conditions that eliminate out-of-plane deformations. However, experimental work is difficult due to the lack of pure plane strain specimens. Therefore, the use of plane strain specimens will permit the isolated analysis of this stress state.

Fatigue crack propagation is usually studied based on standard specimens (Schive, 1998). BS 6835-1: 1988 (1998) and ASTM 647-95 a (1995) indicate the use of CT, middle-crack tension specimen (MT) and bending specimens. A large number of non-standard specimens have also been developed to study crack propagation (Qian and Fatemi, 1996). Specimens with lateral notches have also been used by different authors. CT specimens with lateral side notches were used to study creep crack growth in a nickel-base superalloy (Inconel 718) at 600 °C (Branco *et al.*, 1999). An acceleration of crack growth was observed compared to normal CT specimens. Macdonald and Pajot (1990) suggested the use of side grooving for fracture toughness specimens in order to meet the crack front straightness requirements. The fatigue crack propagation behavior of the microcapsule-modified epoxy was investigated using a tapered double-cantilever beam specimen. Side notches ensured controlled crack growth along the centreline of specimen (Brown *et al.*, 2006). Numerical simulations of notched specimens are more frequent. Lin *et al.* (1998) have simulated the 3D crack extension in an aluminium alloy 2024FC for a side-grooved compact tension specimen. The fatigue crack growth of different surface cracks in semi-circularly notched round bars has been modeled in different research studies (Carpinteri *et al.*, 2006; Lin and Smith, 1999, 1998). Carpinteri *et al.* (2005) have also studied the effect of a circular-arc circumferential notch in a pipe. The solid round specimen with a circunferential V-notch under tension has been used to study the fatigue crack growth under pure mode-III loading (Pook, 1985).

The analysis and optimization of pure plane strain specimens requires numerical parameters to quantify stress triaxiality. Different authors (Mirone, 2007; Shen *et al.*, 2005; Henry and Luxmoore, 1997; Chandrakanth and Pandey, 1995) used the triaxiality parameter $\Theta$ defined by equation (1):

$$
\Theta=\frac{\sigma_{H}}{\sigma_{v M}}=\frac{1 / 3\left(\sigma_{1}+\sigma_{2}+\sigma_{3}\right)}{1 / \sqrt{2}\left[\left(\sigma_{1}-\sigma_{2}\right)^{2}+\left(\sigma_{1}-\sigma_{3}\right)^{2}+\left(\sigma_{2}-\sigma_{3}\right)^{2}\right]^{1 / 2}} \tag{1}
$$

which represents the ratio between the average hydrostatic stress and equivalent Von Mises stresses. This parameter ranges from zero for pure plane strain to five to six for plane strain situations. An alternative triaxiality factor, $h$, is given by equation (2):

$$
h=\frac{\sigma_{z z}}{\nu\left(\sigma_{x x}+\sigma_{y y}\right)} \tag{2}
$$

being $\nu$ the Poisson's ratio. $h$ is equal to 1 or 0 for plane strain or plane stress conditions, respectively, which is quite convenient. Different authors considered this parameter as an effective an accurate alternative to obtain the stress triaxiality level (Macdonald and Pajot, 1990; Bakker, 1992).

This paper follows a preliminary approach of the authors to the problem of considering the use of a standard specimen geometry for experimental purposes under plane strain conditions (Silva *et al.*, 2010). In particular, the main objective of this work is to propose an optimized specimen geometry able to isolate the plane strain state based on the standard M(T) specimen. Lateral width grooves were introduced and the triaxiality was assessed along the crack front. The work followed a parametric study based on the main geometrical features of the specimen, namely: groove geometry,

specimen thickness and crack length. Easiness of production and reproducibility were also two important premises considered during the course of this investigation.

## 2. Numerical procedure
As mentioned before, this study was based on the standard M(T) specimen geometry, as shown in Figure 1(a). Lateral U-shaped (Figure 1(b)) or V-shaped (Figure 1(c)) width grooves were introduced. Both configurations are easy to produce which simplifies the reproducibility of tests, as intended. Indeed, U-shaped grooves can be considered particular cases of V-shaped grooves with $\alpha=0$. Main geometrical parameters are: original thickness ($t_0$), width ($W$), groove depth ($b$), concordance radius at groove tip ($r$), groove angle ($\alpha$) and crack length ($2a$), as shown in Figure 1. Reduced thickness ($t$) can be calculated from the expression: $t = t_0 - 2b$. The crack was assumed to be planar, normal to the longitudinal axis of the specimen and existing in its middle section. The specimen was submitted to tension load, producing mode I loading along the crack fronts. The material was assumed to be homogeneous, isotropic and linear elastic with $E=74$ GPa and $\nu=0.33$.

Symmetry conditions were utilized for efficient computation. Only one-eighth of the specimen was modeled. Figure 2 shows the typical 3D finite element mesh, which was developed with the commercial software Cosmos/M$^\circledR$ (version 2.0). This mesh uses 20-node and 20-node collapsed isoparametric hexahedric elements and has 10,370 elements and 116,020 nodes. Singular elements with mid-side nodes at quarter point positions were considered around the crack front. A spider web pattern, made of three concentric rings centered at the crack tip, was employed (Figure 2(d)). A smooth change from a refined mesh near the crack front to a larger one at remote positions was carried out by creating a transition mesh between those. Along the thickness, the mesh was designed with an increasing level of refinement (Figure 2(d)). The refinement is important to accurately model the stress gradient existing in this direction, namely near the corner points of the crack front. The mesh had a total of

![](./images/811702140597698560_5.jpg)

Figure 1.
(a) Notched M(T)
specimen; (b) U-shaped;
(c) sharp V-shaped notches

![](./images/811702140597698560_6.jpg)

**Figure 2.**
Finite element mesh of the
U-shaped geometry

**Notes:** (a) Global view; (b) detail of specimen's mid-section; (c) detail of crack front;
(d) detail of mesh refinement of spider web mesh along the thickness; $L = 200$ mm,
$W = 50$ mm, $r = 1$ mm, $b = 2$ mm, $t = 7$ mm, $t = 5$ mm and a straight initial crack
with $a = 10$ mm

50 layers divided into three main regions. The most refined one (I), located near the
surface, had 26 layers non-uniformly distributed (Figure 2(d)). The smallest element
size, corresponding to the thickness of superficial layer, had $1\ \mu\text{m}$. The layers were
positioned according to the relationship $1 \times 1.1^{(n-1)}\ \mu\text{m}$, where $n$ is the layer number
($n = 1$ at the surface). Bakker (1992) proposed a geometric progression with ratio 2
between the element sizes along the thickness of the specimen. This means that being
$\Delta z_n$ the size of the surface element, the second, third and fourth elements have sizes of
$2\Delta z_n$, $4\Delta z_n$ and $8\Delta z_n$, respectively (i.e. $\Delta z_n = 2.\Delta z_{n-1}$).The intermediate region (II),
consisting of 14 layers uniformly distributed, had an element size equal to $50\ \mu\text{m}$.
Finally, the larger region (III) had ten layers disposed uniformly, and its element size
depends on the specimen thickness. After a mesh refinement study has been carried
out, a constant element size was adopted in the radial direction, since the triaxiality
parameters were found to be independent of this radial size. The mesh was developed
in a parametric manner and therefore can be used to simulate different crack lengths
and crack shapes. The stress triaxiality parameters were calculated using the normal

stresses of nodes along the crack front. $h$ and $\Theta$ stress triaxiality parameters, given by equations (1) and (2), respectively, were employed in this study. A comparative study was developed, and similar trends were obtained with both parameters. Figure 3(b) shows the evolution of both triaxiality parameters with $z/t$ for the MT unnotched specimen. As can be seen, the same type of behavior is observed. Besides, results show that $h$ ranges from 0 in plane stress to 1 in plane strain, which is quite convenient for the analysis of the stress triaxiality conditions; therefore, this parameter was adopted instead of $\Theta$.

![](./images/811702140597698560_7.jpg)

![](./images/811702140597698560_8.jpg)

![](./images/811702140597698560_9.jpg)

**Notes:** (a) Notch radius ($d=2.5$ mm); (b) notch depth ($r=0.5$ mm); (c) specimen thickness ($b=3$ mm, $r=0.5$ mm)

**Figure 3.**
Effect of geometrical
details on the stress
triaxiality parameter $h$

### 3. Selection of groove type
It is a well-known fact that different lateral groove configurations produce distinct triaxiality distributions along the thickness. In this specimen, a careful analysis of all geometrical dimensions (such as, concordance radius at groove tip, groove depth, thickness, groove angle, width, height and crack length) was carried out. Relevant effects were observed for the first three, whereas for the others no influence on triaxiality was observed. A specimen geometry with $L = 100$ mm, $W = 50$ mm, $t = 10$ mm and $2a = 20$ mm was considered in the following analysis. Figure 3(a) shows the evolution of the $h$ triaxiality parameter (equation (2)) with the fraction of thickness ($z/t$) for several values of concordance radius at groove tip ($r$) of a U-shaped groove. The evolution of $h$ for an unnotched specimen was superimposed for comparison. As mentioned before, the numerical model represents only half-thickness ($z/t \in [0.5 - 1]$) and the remaining part is expected to be symmetrical. However, for clarity purposes, the evolution of $h$ for values of $z/t$ less than 0.8 was suppressed. In that region, the curves are stable and therefore such area is not a relevant part in this analysis. As can be shown in Figure 3, the value of $h$ is 0 near the surface, which means that a plane stress condition occurs at this region. In this portion of thickness, intense and steep changes in $h$ are clearly observed, which rises suddenly towards a value near unity (plane strain). It is clear in Figure 3(a) that the decrease of $r$ rises the triaxiality profile near the surface. On the other hand, regardless of the radius, all curves converge to the same value. The convergence is slower for greater values of $r$. Furthermore, the curve of the unnotched specimen (used as reference) lies always below those of the grooved geometries and presents a relative smaller in-depth value of $h$ (roughly 0.95). This demonstrates that the groove presence is advantageous to increase the level of triaxiality, as was expected. Moreover, it is important to point out that conclusions mentioned for U-shaped grooves are valid for V-shaped grooves as well. As shown in Figure 3(a), the evolution of $h$ for a V-shaped groove with $b = 3$ mm, $r = 0.5$ mm and $\alpha = 45^\circ$ (series of circles) is similar to the case of a U-shape with same depth and groove radius ($r = 0.5$ and $d = 2.5$ mm). Therefore, the type of groove is irrelevant once the groove radius is similar. As mentioned before, U-shaped grooves are a particular case of V-shaped grooves.

Figure 3(b) shows the evolution of $h$ against $z/t$ for various values of groove depth for a U-shaped groove considering a fixed groove radius ($r = 0.5$ mm). As in the previous case, the evolution of $h$ for an unnotched specimen was superimposed for comparison purposes. In a first place, the general trends of the curves are identical to the ones shown in Figure 3(a), i.e. there is a superficial region where steep changes of the triaxiality parameter occur whilst a plateau prevails for the inner positions. As regards the effect of $b$ on $h$, results show that the triaxiality state is more significant in-depth, as visible from the stable values increase for longer groove depths. Therefore, in terms of triaxiality, longer depths are preferable. Near the surface, all curves are overlapped, which denotes no influence of $b$ on $h$. Furthermore, Figure 3(b) also shows the evolution of $h$ for a V-shaped groove with $b = 1$ mm, $r = 0.5$ mm and $\alpha = 90^\circ$ (series of circles). Comparing it with the corresponding U-shaped groove ($r = 0.5$ and $b = 1$ mm), the results show an identical behavior, since both curves are superimposed. This reinforces the conclusion that the groove angle has no effect on $h$.

The influence of thickness on triaxiality is shown in Figure 3(c). It can be seen that curves converge towards unity in every cases. Moreover, the convergence zone is less extensive for greater values of thickness. However, the benefit in terms of triaxiality

decreases with $t$ once curves are closer as the thickness increases. Figure 3(c) shows the evolution of $h$ for a V-shaped groove with $b=3 \mathrm{~mm}, r=0.5 \mathrm{~mm}, \alpha=45^{\circ}$ and $t=5 \mathrm{~mm}$. A comparison of this case with the one of a U-shaped groove with $b=3$, $r=0.5$ and $t=5 \mathrm{~mm}$ permits to observe that both curves follow similar trends, as expected.

From Figure 3, it is possible to conclude that either U-shape or V-shaped grooves are adequate. Both types of grooves can be easily made, which facilitates the reproducibility of tests. Besides, amplitude of groove angle is not a decisive geometrical detail. In terms of groove radius, it should be as small as possible in order to minimize specimen's thickness. The minimum limit of $r$ depends upon the technology used. Theoretically, $r=0 \mathrm{~mm}$ would be the desirable value but this is not technically feasible. Therefore, a trade-off solution must be considered regarding the value of the groove radius.

An alternative and more accurate manner to quantify the effects of geometrical variables on triaxiality was carried out employing a parameter that quantifies the portion of thickness (pt) in which $h$ is greater or equal than a predefined value. Although relatively simple, this parameter is quite sensitive and therefore interesting to define the main specimen dimensions. This sensitivity can be inferred from the observation of Figure 3(c). As can be seen, the intersection of each curve with the dashed line at the top $(h=0.97)$ is unique and occurs for different values of $z / t$.

Figure 4 shows the evolution of $p t$ for a value of $h \geq 0.97$. Different groove radii and groove depths were considered in this analysis. There is a strong effect of thickness on $p t$. However, this effect decays for greater values of $t$. For smaller values of thickness, $p t$ rises suddenly. Furthermore, $p t$ is also quite affected by the groove radius: smaller groove radii cause greater values of $p t$. The other parameter affecting $p t$ is the groove

![](./images/811702140597698560_10.jpg)

Figure 4.
Evolution of $p t$ with
thickness for different
notch radii and notch
depths $(h \geq 0.97)$

Crack
propagation

depth: for smaller dimensions identical to the groove radius this parameter has an important effect, but for depths two or three times greater this parameter has a limited effect. Figure 4 can help researchers to select the main specimen dimensions (groove radius, groove depth and thickness) in terms of triaxiality, since it allows finding different combinations of those variables which produce similar values of triaxiality. In this study, it was assumed that a plane strain state, i.e. that a high stress triaxiality level, is achieved with a specimen having at least 97 percent of thickness with $h \geq 0.97$. According to the authors, this is a quite restrictive criterion that is adequate for a significant number of experimental conditions. However, the effectiveness of this triaxiality level must be verified for each phenomenon influenced by the stress state (crack closure, diffusion, etc.) in order to ensure a perfect plane strain condition. Dashed line, at the top of Figure 4, identifies this objective. As can be seen, diverse possibilities are available. In order to reduce material cost, a minimum original specimen thickness $(t_0)$ is desirable. From all solutions available in Figure 4, the minimum original thickness is achieved with the following set of dimensions: $r = 0.5$, $b = 1$, $t = 10.56$ and $t_0 = 12.56$ mm. This combination is shown in Figure 4 by a grey diamond. The selected groove radius ($r = 0.5$ mm) is technically feasible. It can be made using current machining technology which simplifies specimen manufacture and reduces costs. Besides, the groove depth ($b = 1$ mm) is within reasonable values, which avoids excessive machining time. Finally, the dimensions proposed are small enough to be tested using current laboratory equipment. Notice that an unnotched specimen with identical characteristics in terms of triaxiality (i.e. 97 percent of thickness with $h \geq 0.97$) would require a minimum thickness of 43.06 mm.

The information in Figure 4 was re-plotted in Figure 5. Figure 5(a) shows different combinations of main variables ($r$, $t$ and $b$) for three different levels of triaxiality (97 percent of thickness with $h \geq 0.97$, 95 percent of thickness with $h \geq 0.95$ and 93 percent of thickness with $h \geq 0.93$). Variables $1/b$ and $(t/b)^{0.25}$ were chosen to optimize the information of this figure in order to confirm the previous conclusions.

![](./images/811702140597698560_11.jpg)

Figure 5.
Combinations of the main
geometrical features of the
specimen for different
levels of triaxiality

Figure 5(b) shows specimen thickness against the groove radius for several groove depths. The same levels of triaxiality (97 percent of thickness with $h \geq 0.97$, 95 percent of thickness with $h \geq 0.95$ and 93 percent of thickness with $h \geq 0.93$) were also considered in this case. Both figures can be used to define different specimen geometries with different triaxiality levels according with the requirements of the experimental research.

## 4. Conclusions
An M(T) specimen with lateral grooves was proposed as a convenient and straightforward solution to obtain a pure plane strain geometry. A computational analysis was carried out considering the effect of different geometrical features of the specimen in the triaxiality stress state along all the positions of the crack front. A stress triaxiality parameter, $h$, was considered to study the effect of groove radius, groove depth and specimen thickness. Results show that a pure plane strain state is achieved (i.e. 97 percent of specimen thickness has $h > 0.97$) if a specimen with optimized geometrical features is used, which corresponds to a groove radius of 0.5 mm, a groove depth of 1 mm and a total specimen thickness of 12.56 mm.

## References
Antunes, F.V., Ferreira, J.A.M., Branco, C.M. and Byrne, J. (2001), "Influence of stress state on high temperature fatigue crack growth in Inconel 718", *Fatigue & Fracture of Engineering Materials & Structures*, Vol. 24, pp. 127-35.

ASTM 647-95 a (1995), *Standard Test Method for Measurement of Fatigue Crack Growth Rates*, ASTM International, West Conshohocken, PA.

Bakker, A. (1992), "Three-dimensional constraint effects on stress intensity distributions in plate geometries with through-thickness cracks", *Fatigue & Fracture of Engineering Materials & Structures*, Vol. 15 No. 11, pp. 1051-69.

Branco, C.M., Baptista, J. and Byrne, J. (1999), "Crack growth under constant sustained load at elevated temperature in IN718 superalloy", *Materials at High Temperature*, Vol. 16 No. 1, pp. 27-35.

Brown, E.N., White, S.R. and Sottos, N.R. (2006), "Fatigue crack propagation in microcapsule toughened epoxy", *Journal of Materials Science*, Vol. 41 No. 19, pp. 6266-73.

BS 6835-1: 1998 (1998), *Method for the Determination of the Rate of Fatigue Crack Growth in Metallic Materials*, BSI, London.

Carpinteri, A., Brighenti, R. and Vantadori, S. (2005), "Circumferentially notched pipe with an external surface crack under complex loading", *International Journal of Mechanical Sciences*, Vol. 45, pp. 1929-47.

Carpinteri, A., Brighenti, R. and Vantadori, S. (2006), "Surface cracks in notched round bars under cyclic tension and bending", *International Journal of Fatigue*, Vol. 28, pp. 251-60.

Cayón, A., Alvarez, J.A. and Gutiérrez-Solana, F. (2003), "Influence of microstructure and triaxial stress states on hydrogen induced cracking", *Anales de Mecanica de la Fractura*, Vol. 20, pp. 273-8.

Chandrakanth, S. and Pandey, P.C. (1995), "An isotropic damage model for ductile material", *Engineering Fracture Mechanics, India*, Vol. 50 No. 4, pp. 457-65.

Fleck, N.A. and Smith, R.A. (1982), "Crack closure – is it just a surface phenomenon?", *International Journal of Fracture*, Vol. 4, pp. 157-9.

Henry, B.S. and Luxmoore, A.R. (1997), "The stress triaxiality constraint and the Q-value as a ductile fracture parameter", *Engineering Fracture Mechanics*, Vol. 57 No. 4, pp. 375-90.

Kim, J., Gao, X. and Srivatsan, S. (2004), "Modelling of void growth in ductile solids: effects of stress triaxiality and initial porosity", *Engineering Fracture Mechanics*, Vol. 71, pp. 379-400.

Lin, G., Cornec, A. and Schawalbe, K.-H. (1998), "Three-dimensional finite element simulation of crack extension in aluminium alloy 2024FC", *Fatigue & Fracture of Engineering Materials & Structures*, Vol. 21, pp. 1159-73.

Lin, X.B. and Smith, R.A. (1998), "Fatigue growth simulation for cracks in notched and unnotched round bars", *International Journal of Mechanical Sciences*, Vol. 40, pp. 405-19.

Lin, X.B. and Smith, R.A. (1999), "Shape evolution of surface cracks in fatigued round bars with a semicircular circumferential notch", *International Journal of Fatigue*, Vol. 21, pp. 965-73.

Macdonald, B.D. and Pajot, J.J. (1990), "Stress intensity factors for side-grooved fracture specimens", *Journal of Testing and Evaluation*, Vol. 18 No. 4, pp. 281-5.

Mirone, G. (2007), "Role of stress triaxiality in elastoplastic characterization and ductile failure prediction", *Engineering Fracture Mechanics, Italy*, Vol. 74, pp. 1203-21.

Pippan, R., Kolednik, O. and Lang, M. (1994), "A mechanism for plasticity-induced crack closure under plane strain conditions", *Fatigue & Fracture of Engineering Materials & Structures*, Vol. 17 No. 6, pp. 721-6.

Pommier, S. (2002), "Plain strain crack closure and cyclic hardening", *Engineering Fracture Mechanics*, Vol. 69, pp. 25-44.

Pook, L.P. (1985), "Comments on fatigue crack growth under mixed modes I and III and pure mode III loading", in Miller, K.J. and Brown, M.W. (Eds), *Multiaxual Fatigue*, ASTM STP 853, American Society for Testing and Materials, Philadelphia, PA, pp. 249-63.

Qian, J. and Fatemi, A. (1996), "Mixed mode fatigue crack growth: a literature survey", *Engineering Fracture Mechanics*, Vol. 55 No. 6, pp. 969-90.

Schive, J. (1998), "Fatigue specimens for sheet and plate material", *Fatigue & Fracture of Engineering Materials & Structures*, Vol. 21, pp. 347-57.

Sehitoglu, H. and Sun, W. (1991), "Modelling of plane strain fatigue crack closure", *ASME Journal of Engineering Materials and Technology*, Vol. 113, pp. 31-40.

Shen, W., Peng, L.H. and Tang, C.Y. (2005), "An anisotropic damage-based plastic yield criterion and its application to analysis of metal forming process", *International Journal of Mechanical Science, China*, Vol. 47, pp. 1897-922.

Silva, J.M., Infante, V., Antunes, F. and Ferreira, F. (2010), "Using a standard specimen geometry for crack propagation under plain strain conditions", *Proceedings of CIFIE 2010 - Iberian Conference on Fracture and Structural Integrity, Porto, Portugal*.

Tong, J., Byrne, J., Hall, R. and Aliabadi, M.H. (1997), "A comparison of corner notched and compact tension specimens for high temperature fatigue testing", *Proceedings of Conference Engineering Against Fatigue, University of Sheffield, Sheffield, UK*, pp. 583-90.

Van Stone, R.H., Cox, T.B., Low, J.R. Jr and Psioda, J.A. (1985), "Microstructural aspects of fracture by dimple rupture", *International Metals Review*, Vol. 30, pp. 157-79.

Webster, G.A. and Ainsworth, R.A. (1994), *High Temperature Component Life Assessment*, Chapman & Hall, London.

### About the authors

R. Branco is a Lecturer at the Department of Mechanical Engineering, Polytechnic Institute of Coimbra (Coimbra, Portugal); and a PhD student (final stage). His research interests include: numerical analysis of cracked components.

J.M. Silva is an Assistant Professor at the Department of Aerospace Sciences, University of Beira Interior (Covilhã, Portugal). He has a PhD in Aerospace Engineering (Technical Institute of Lisbon), a MSc in Mechanical Engineering (University of Coimbra), and is Investigator of AeroG (UBI), CAST (UBI) and ICEMS (IST). His research interests include: aerospace materials and structures, fracture mechanics and high-temperature materials. J.M. Silva is the corresponding author and can be contacted at: jmas@ubi.pt

V. Infante is an Assistant Professor at the Department of Mechanical Engineering, Technical Institute of Lisbon (Lisbon, Portugal). He has a PhD in Mechanical Engineering (Technical Institute of Lisbon), a MSc in Mechanical Engineering (Technical Institute of Lisbon) and is an Investigator of ICEMS (IST). His research interests include: mechanical behavior of materials, welding techniques and fracture mechanics.

F. Antunes is an Assistant Professor at the Department of Mechanical Engineering, University of Coimbra (Coimbra, Portugal). He has a PhD in Mechanical Engineering (University of Coimbra), a MSc in Mechanical Engineering (University of Coimbra), and is an Investigator of CEMUC (University of Coimbra). His research interests include: numerical simulation and experimental analysis of cracked bodies and HTF.

F. Ferreira is a Stress Engineer at Altran Spain (Victoria, Spain); he has a MSc in Aeronautical Engineering. His research interests include: FEM/FEA analysis of aerospace structures and components and numerical analysis of cracked bodies.

---

To purchase reprints of this article please e-mail: reprints@emeraldinsight.com

Or visit our web site for further details: www.emeraldinsight.com/reprints

Crack
propagation

This article has been cited by:

1. Ricardo Branco, F.V. Antunes, J.D. Costa. 2015. A review on 3D-FE adaptive remeshing techniques for crack growth modelling. *Engineering Fracture Mechanics* **141**, 170-195. [CrossRef]

2. R. Branco, F. V. Antunes, J. D. Costa. 2014. Lynx: A user-friendly computer application for simulating fatigue growth of planar cracks using FEM. *Computer Applications in Engineering Education* **22**:3, 529-540. [CrossRef]

3. R. Branco, F.V. Antunes, L.C.H. Ricardo, J.D. Costa. 2012. Extent of surface regions near corner points of notched cracked bodies subjected to mode-I loading. *Finite Elements in Analysis and Design* **50**, 147-160. [CrossRef]