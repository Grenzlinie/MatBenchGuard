ORIGINAL PAPER

# Development of stress-modified fracture strain for ductile failure of API X65 steel

Chang-Kyun Oh · Yun-Jae Kim ·
Jong-Hyun Baek · Woo-sik Kim

Received: 1 September 2005 / Accepted: 1 November 2006 / Published online: 16 March 2007
© Springer Science+Business Media, Inc. 2007

**Abstract** The present paper proposes ductile failure criteria in terms of true fracture strain (the equivalent strain to fracture) as a function of the stress triaxiality (defined by the ratio of the hydrostatic stress to the equivalent stress) for the API X65 steel. To determine the stress-modified fracture strain, smooth and notched tensile bars with four different notch radii are tested, from which true fracture strains are determined as a function of the notch radius. Then detailed elastic-plastic, large strain finite element analyses are performed to estimate variations of stress triaxiality in the tensile bars, which leads to true fracture strains as a function of the stress triaxiality, by combining them with experimental results. Two different failure criteria are proposed, one based on local stress and strain information at the site where failure initiation is likely to take place, and the other based on averaged stress and strain information over the ligament where ductile fracture is expected. As a case study, ligament failures of API X65 pipes with a gouge are predicted and compared with experimental data.

**Keywords** Ductile fracture · API X65 steel · Stress triaxiality · Fracture strain

## 1 Introduction

Underground gas pipelines are often subject to damages due to surrounding environment (such as corrosion) and third-party accidents (such as dents and gouges). When any damage is present in a pipeline, proper engineering assessments are needed to determine whether pipelines are still fit for service. See for instance Wilkoski et al. (2000) and Cosham and Hopkins (2004) for extensive review. Assessment methodologies of such damaged pipelines can be classified into two categories. The first category is the net-section limit load approach (Kanninnen et al. 1982; ASME 1992), where a damaged pipe is assumed to fail at the load when the net section reaches a fully plastic state. Such approach is valid for a pipeline made of a material with sufficient ductility. In fact, the American Petroleum Institute (API) steels used extensively in gas pipelines are quite ductile and thus application of the net-section limit load approach could be justified. Although the net-section limit

---

C.-K. Oh
Korea Power Engineering Company (KOPEC),
Yongin-si, Kyunggi-do 449-713, Korea

Y.-J. Kim (☑)
Department of Mechanical Engineering, Korea
University, 5 Ka, Anam-dong, Sungbuk-Ku, Seoul
136-701, Korea
e-mail:kimy0308@korea.ac.kr

J.-H. Baek · W.-s. Kim
Korea Gas Corporation Research and Development
Center, 638-1 Il-dong, Ansan, Kyonggi-do 425-150,
Korea

![](./images/812008037408571393_1.jpg)

load approach is simple in many applications, val- idation is rather expensive, requiring a large num- ber of full-scale pipe test data. It should be also noted that the net-section approach is based on average stresses in the net-section and is regarded as a "global" criterion. The second approach is more fundamental and is based on the stress-mod- ified strain criterion, which is regarded as a "local" criterion. Noting that the process of ductile fracture involves void nucleation, growth and coalescence, it has been shown by a number of researchers that ductile fracture of metals is strongly dependent on the hydrostatic stress state (Hancock and Macken- zie 1976; Garrison and Moody 1987; McClintock1968; Rice and Tracey 1969; Clausing 1970; Thoma- son 1990; Mackenzie et al. 1977). Several models have been proposed to characterize ductile frac-ture of metals (see for instance Anderson 1995; Ritchie and Thompson 1985; Gurson 1977); among them, a stress-modified critical strain model is quite a simple, but physically realistic model (Ritchie and Thompson 1985; Bao 2005; Bao and Wierzbicki2004). Note that the stress-modified critical strain is an old concept dating back to Hancock and Mackenzie (1976). At that time, the stress and strains at failure were calculated by the approx- imate formula of Bridgman (1952), which could be inaccurate. A number of numerical solutions have been reported and comparisons with Bridg- man's formula have been made (Alves and Jones1999; Valiente 2001; La Losa et al. 2001, 2003; Bao2005; Kim et al. 2006). The stress-modified criti- cal strain concept also led to the concept of failurelocus curve (Theocaris 1995; Schluter et al. 1996; Schiffman et al. 1998) and was extended to simulate crack-tip failure processes (Hancock and Cowling1980).

The stress-modified critical strain model consists not only of mechanical parameters (such as stresses and strains) but also of material parameters (con- stants) that might be related to metallurgy. These material constants are typically regarded as mate- rial properties and thus should be calibrated for a given material. With these material constants, and the local stress and strain information, the stress- modified strain approach can be applied to pre- dict ductile fracture of defective structures. The objectives of this work are two-fold. The first is todevelop relevant material parameters (constants) for the stress-modified critical strain concept for the API X65 steel. The second is to verity this concept by applying it to defective API X65 pipes under internal pressure.

This paper presents the stress-modified fracture strain for API X65 steel, as a function of the stress triaxiality. To determine the stress-modified frac- ture strain, smooth and notched tensile bars with five different notch radii are tested, from which true fracture strains are determined as a function of the notch radius. Then detailed elastic-plastic, finite element (FE) analyses based on the large geometry change option are performed to estimate variations of the stress triaxiality in the notched bars. Combining experimental with FE results pro- vides the true fracture strain as a function of the stress triaxiality, which is regarded as a criterion of ductile fracture. Section 2 briefly describes experi- mental results. Results on FE analysis are given in Sect. 3. Combining the experimental results with FE analysis, the stress-modified fracture strain cri- teria are proposed in Sect. 4. The present work is discussed in Sect. 5 and concluded in Sect. 6.

## 2 Experiments
### 2.1 Material and specimen geometry
Materials for tensile tests were extracted from a pipe of outer diameter $D_{o}=762 ~mm$ and wall thickness $t=17.5 ~mm$ , made of the American Petroleum Institute (API) 5L X65 steel, typically used for gas and oil transportation (API 2000). According to the API specifications, the minimum specified yield strength and ultimate tensile strength are 448 and 530 MPa, respectively. Chem- ical composition of the API X65 steel is given in Table 1.

To investigate the effect of triaxial stress states on ductility of the API X65 steel, tensile tests were performed using smooth and notched bars with four different notch radii. These tensile bars were extracted from the pipe in the longitudinal direc- tion. Schematic diagrams for smooth and notched tensile bars, employed in the present work, are depicted in Fig. 1. For all specimens, the mini- mum section has a diameter of 6.0 mm. For notched bars, four different notch radii were machined. The

![](./images/812008037408571393_2.jpg)

<table>
<caption>Table 1 Chemical composition of the API X65 steel</caption>
<thead>
<tr>
<th colspan="7">Elements (wt.%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>C</td>
<td>P</td>
<td>Mn</td>
<td>S</td>
<td>Si</td>
<td>Fe</td>
<td>Ceq</td>
</tr>
<tr>
<td>0.08</td>
<td>0.019</td>
<td>1.45</td>
<td>0.03</td>
<td>0.31</td>
<td>Balance</td>
<td>0.32</td>
</tr>
</tbody>
</table>

![](./images/812008037408571393_3.jpg)

Fig. 1 Schematic illustrations: (a) smooth tensile bars; and (b) and (c) notched tensile bars

notch radii were 6.0 mm (R6), 3.0 mm (R3), 1.5 mm (R1.5) and 0.2 mm (R0.2). For the specimens with R6, R3 and R1.5 notches, round notches were machined, but for the specimen with R0.2, the V-notch with a half angle of $45^\circ$ was machined with the notch radius of 0.2 mm, as schematically depicted in Fig. 1.

### 2.2 Test and results

Figure 2 depicts test set-up for tensile testing of the bar with the notch radius of 1.5 mm. In testing, axial displacement was monitored using extensometer with the gauge length of 25 mm. For a given specimen geometry, tests were repeated three times, giving a total of fifteen tests. Engineering stress–strain data for all specimens tested are summarized in Fig. 3. It shows that, as the notch radius decreases, the yield and tensile strengths increase, but the strain to fracture decreases. Such trend is due to the fact that the triaxial stress increases with decreasing notch radius. More detailed discussion on test results will be given in the next section, together

![](./images/812008037408571393_4.jpg)

Fig. 2 Test set-up for notched round bar test with the notch radius of 1.5 (mm)

![](./images/812008037408571393_5.jpg)

Fig. 3 Experimental engineering stress–strain data for smooth and notched tensile bar tests

with the results from the FE analysis. Averaged true stress–strain data of the API X65 steel are shown in Fig. 4, resulting from three tensile tests of smooth bars. The Bridgman correction (Bridgman 1952) was applied to correct stresses and strains due to notch effects.

![](./images/812008037408571393_6.jpg)

![](./images/812008037408571393_7.jpg)

Fig. 4 True stress–strain data for API X65, used in the present FE analysis

## 3 Finite element analysis

### 3.1 FE model and analysis
Detailed elastic–plastic, axi-symmetric FE analyses were performed to simulate tensile tests of smooth and notched specimens and thus to determine variations of the triaxial stress and strain within the specimen. Symmetric conditions are fully utilized for efficient computation. To avoid problems associated with incompressibility, reduced integration element within ABAQUS (2005) (element type CAX8R) was used. Typical FE meshes with the different notch radii, employed in the present work, are shown in Fig. 5. The number of elements and nodes in typical FE meshes ranges from 484 elements/1557 nodes to 658 elements/2089 nodes.

The experimental true stress-plastic strain data, shown in Fig. 4, were used in the FE analyses. Materials were modeled as isotropic elastic-plastic materials that obey the incremental plasticity theory. To incorporate a large geometry change effect in tensile testing, a large geometry change option was chosen. The deformation boundary condition was applied to the top of the FE model, and the resulting tensile load was determined from nodal forces. The gauge length elongation was also monitored from the FE displacement results. Local stress and strain fields in the minimum section of the tensile bars were also extracted from the FE results, as a function of applied load.

### 3.2 Comparison with experimental results
Figure 6 compares experimental engineering stress–strain data from smooth tensile bars with the FE results, which shows excellent agreement. Although the present FE analysis cannot simulate failure of tensile test specimens, it can simulate tensile deformation behavior even after necking. Corresponding results for notched bars are shown in Fig. 7 for cases with two different notch radii, R3 mm and R6 mm. As for the smooth bar case, agreements between the test results and FE ones are quite good up to failure initiation points. Detailed results on variations of the stress triaxiality and strain will be given in the next section.

## 4 Stress-modified fracture strain
In the previous section, it was shown that the load–displacement curves (or engineering stress–strain curves) from the present FE analysis can simulate well those from un-notched and notched tensile specimen tests, up to failure initiation points on the load–displacement curve. From the FE analysis, detailed information on local stress and strain fields can be also obtained as a function of load. Thus detailed examination of local stress and strain fields at failure initiation points on the load–displacement curves would provide local failure criterion for ductile fracture of the API X65 steel, which is the topic in this section. At the end of this section, ductile failure criteria based on strain, incorporating the effect of the stress triaxiality, are proposed.

### 4.1 Variations of stress triaxiality
Figure 8a shows the radial variation of the stress triaxiality and equivalent strain in the minimum (necked) section of the smooth bar at the point of failure initiation (see Fig. 6). The stress triaxiality

![](./images/812008037408571393_8.jpg)

Fig. 5 FE meshes for
notched tensile bars:
(a) notch = 0.2R,
(b) notch = 1.5R and
(c) notch = 3R

![](./images/812008037408571393_9.jpg)

![](./images/812008037408571393_10.jpg)

Fig. 6 Comparison of experimental engineering stress-
strain data for smooth tensile bars with FE results

is defined by the ratio of the mean normal (hydro-
static) stress, $\sigma_{\mathrm{m}}$, to the equivalent stress, $\sigma_{\mathrm{e}}$:

$$
\frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}}=\frac{\sigma_{1}+\sigma_{2}+\sigma_{3}}{3 \sigma_{\mathrm{e}}} \tag{1}
$$

where $\sigma_{i}\ (i=1$–$3)$ denote the principal stress. The
equivalent stress, $\sigma_{\mathrm{e}}$, is expressed in terms of three
principal stresses as

$$
\sigma_{\mathrm{e}}=\frac{1}{\sqrt{2}}\left[\left(\sigma_{1}-\sigma_{2}\right)^{2}+\left(\sigma_{1}-\sigma_{3}\right)^{2}+\left(\sigma_{3}-\sigma_{2}\right)^{2}\right]^{0.5}\tag{2}
$$

The equivalent strain, $\varepsilon_{\mathrm{e}}$, on the other hand, is
defined by

$$
\varepsilon_{\mathrm{e}}=\frac{\sqrt{2}}{3}\left[\left(\varepsilon_{1}-\varepsilon_{2}\right)^{2}+\left(\varepsilon_{1}-\varepsilon_{3}\right)^{2}+\left(\varepsilon_{3}-\varepsilon_{2}\right)^{2}\right]^{0.5}\tag{3}
$$

The distance $(r)$ is normalized with respect to the
radius of the minimum section $(a)$, and the values
of $r/a=0$ and $r/a=1$ mean the center and the
free surface of the specimen, respectively. It shows
that both the equivalent strain and the stress tri-
axiality take their maximum values in the center

![](./images/812008037408571393_11.jpg)

![](./images/812008037408571393_12.jpg)
![](./images/812008037408571393_13.jpg)

Fig. 7 Comparison of experimental engineering stress–strain data for notched tensile bars with FE results: (a) notch=3R, (b) notch=6R

of the specimen, and thus failure is expected to occur from the center of the specimen. Figure 8b and c shows corresponding results for notched ten- sile bars. These figures show that the stress triax- iality decreases with increasing notch radius, but always attains its maximum value in the center of the notched tensile bars, regardless of the notch radius. Distributions of equivalent strain, on the other hand, show a slightly different picture. For a relatively large notch radius, equivalent strain attains its maximum value in the center of the bar. However, for smaller notch radii (in the present case, R0.2 mm and R1.5 mm cases), the maximum value of equivalent strain occurs not in the cen- ter but at the notch tip. For the R1.5 mm case, the difference between equivalent strain in the center of the specimen and that at the notch tip is not so significant. In contrast, the difference in the stress triaxiality is significant and the value in the center of the specimen is about three times larger than that at the notch tip. For the R0.2 mm case, how- ever, the equivalent strain at the notch tip is much larger than that in the center. Although the stress triaxiality in the center of the specimen is larger than that at the notch tip, it is difficult to draw any conclusion on the possible failure initiation sites. To speculate the most damaged (critical) site for failure initiation within notched bars, the follow- ing damage indicator (DI) is introduced, based on the Rice and Tracey formula (1969):

$$
\mathrm{DI}=\int \exp \left(1.5 \frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}}\right) \mathrm{d} \varepsilon_{\mathrm{e}}^{\mathrm{pl}} \quad(4)
$$

where $\varepsilon_{\mathrm{e}}^{\mathrm{pl}}$ denotes the effective plastic strain. Variations of DI with the normalized distance $(r / a)$ are shown in Fig. 9. From the results in Fig. 9, the following speculation can be made on possible fail- ure initiation locations in notched tensile bars. For smooth and notched tensile bars except those with the 0.2 mm notch radius, failure is expected to ini- tiate in the center of the minimum section in the specimen. For specimens with the 0.2 mm notch radius, the notch tip is the critical site for failure initiation.

Another interesting point in Fig. 8 is that equiv- alent strain distributions are not constant in the minimum section of notched bars. Non-uniformity of the equivalent strain in the minimum section increases with decreasing notch radius. Bridgman(1952) developed a semi-empirical analysis in terms of the radius of curvature of the neck and the radius of the minimum cross-section to approxi- mately determine local stresses in a necked round bar. The main feature of his analysis was that the equivalent strain is constant across the minimum cross-section:

$$
\varepsilon_{\mathrm{e}}=2 \ln \left(\frac{a_{\mathrm{o}}}{a}\right) \quad(5)
$$

where $a$ denotes the radius of the minimum cross section and $a_{\mathrm{o}}$ is the initial value of $a$. Based on this assumption, Bridgman found variations of radial,

![](./images/812008037408571393_14.jpg)

![](./images/812008037408571393_15.jpg)

Fig. 8 (a) Equivalent strain and stress triaxiality distributions for smooth tensile bars at the failure initiation point, determined from the FE analysis. (b) Stress triaxiality distributions and (c) equivalent strain distributions for smooth and notched tensile bars at the failure initiation point, determined from the FE analyses

![](./images/812008037408571393_16.jpg)

Fig. 9 Variations of damage with the normalized distance for notched bars. Damage is calculated using the indicator given in Eq. 4

hoop and axial stresses ($\sigma_{rr}$, $\sigma_{\theta\theta}$ and $\sigma_{zz}$, respectively) and the stress triaxiality as

$$
\sigma_{zz} = \sigma_{\mathrm{e}} \left[ 1 + \ln\left( \frac{a^2 + 2aR - r^2}{2aR} \right) \right]
$$

$$
\sigma_{rr} = \sigma_{\theta\theta} = \sigma_{\mathrm{e}} \left[ 1 + \ln\left( \frac{a^2 + 2aR - r^2}{2aR} \right) \right]
$$

$$
\frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}} = \frac{1}{3} + \ln\left( \frac{a^2 + 2aR - r^2}{2aR} \right) \tag{6}
$$

where $R$ depicts the notch radius. Figure 10a compares radial variation of the stress triaxiality according to Eq. (6) with that from the present FE analysis for the notch radius of R1.5 mm. The FE result in Fig. 10a is obtained at the failure initiation point on the load–displacement curve. Thus for comparison, the stress triaxiality from Eq. 6 should be estimated using values of $a$ and $R$ at the failure initiation point, which can be different from initial values due to the large geometry change effect. For simplicity, the Bridgman result in Fig. 10a is estimated using initial values of $a$ and $R$, and thus direct comparison should not be made. On the other hand, as ductility is relatively small for the specimen with the R1.5 mm notch, the effect of the large geometry change would not be significant, and thus the comparison in Fig. 10 would still provide useful information. It shows that the

![](./images/812008037408571393_17.jpg)

![](./images/812008037408571393_18.jpg)

Fig. 10 Comparisons of Bridgman's approximations with the FE results: (a) radial variations of the stress triaxiality for the 1.5R notched bar; and (b) maximum stress triaxiality as a function of the ratio of the bar to the notch

Bridgman approximation, Eq. 6, underestimates the maximum stress triaxiality in the necked ligament. Figure 10b compares the maximum stress triaxialities in terms of the notch radius, determined from the FE analyses, with those estimated from Eq. (6). As noted, estimated values using Eq. 6 are based on initial values of $a$ and $R$, and thus do not incorporate the large geometry change effect. That is why the larger difference is observed in Fig. 10b for the larger notch radius where the geometry change effect is more significant. However, it can be seen that the Bridgman approximation is not accurate. In fact, large differences between the Bridgman solutions and detailed FE solutions have been recently found in several works (Alves and Jones 1999; Valiente 2001; La Losa et al. 2001,2003; Bao 2005; Kim et al. 2006). These results suggest that caution should be exercised when applying the Bridgman approximation to estimate the stress triaxiality in notched bar tests.

### 4.2 Stress-modified fracture strain

From detailed elastic-plastic FE analyses with the large geometry change option, accurate values of stress and strain components can be determined at every stage of deformation. By combining such information with notched bar tensile test results, a ductile failure criterion in terms of the equivalent strain to failure as a function of the stress triaxiality can be established. Before proceeding, it should be noted that stress and strain are defined only at a point. Thus different positions (sites) with a notched bar can be chosen, which lead to different failure criteria. One possible approach is to develop a failure criterion based on stress and strain at the location where failure is most likely to initiate, which corresponds to the site with the highest stress triaxiality and strain or with the highest damage according to Eq. 4, for instance. Another interesting approach is based on average stress and strain over the minimum section. Although the former approach is more plausible, the latter approach could offer some advantages in practical application to defect assessment of gas pipelines. More detailed discussion will be given later. In the present work, both approaches are taken, and two different ductile failure criteria are developed, as described below.

Figure 11a shows the evolution of the stress triaxiality in terms of the equivalent strain for smooth and notched tensile bars. Note that the stress triaxiality and the equivalent strain are measured in the center of the minimum section in test specimens. It was shown in Fig. 9 that, for smooth and notched tensile bars except those with the 0.2 mm notch radius, failure is expected to initiate in the center of the minimum section in the specimen. For specimens with the 0.2 mm notch radius, the notch tip is

![](./images/812008037408571393_19.jpg)

![](./images/812008037408571393_20.jpg)

Fig. 11 Variations of the stress triaxiality with the equivalent strain for smooth and notched bar specimens: (a) based on the critical location criterion and (b) based on the section average criterion

the critical location for failure initiation. Therefore,
the data for the specimens with the notch radius of
0.2 mm are excluded in Fig. 11a. Figure 11a shows
that the stress triaxiality in the center of the speci-
men depends strongly on the equivalent strain. As
a ductile failure criterion should include the his-
tory of stress and strain, average stress triaxiality
is introduced, defined by

$$
\left(\frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}}\right)_{\mathrm{ave}}=\frac{1}{\varepsilon_{\mathrm{ef}}} \int_{0}^{\varepsilon_{\mathrm{ef}}} \frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}} \mathrm{d} \varepsilon_{\mathrm{e}} \tag{7}
$$

where $\varepsilon_{\mathrm{ef}}$ denotes the equivalent strain to failure
initiation. Such definition incorporates the history
effect on stresses and strains on ductile fracture.
For a given notch radius, the calculated average
stress triaxiality is constant, and is shown in Fig.
11a. Resulting equivalent strains to failure initia-
tion (called the true fracture strain) are shown in
Fig. 12, as a function of the (average) stress triaxi-
ality. Note that one point in Fig. 12 corresponds to
the result for one notch radius. It shows that the
true fracture strain decreases sharply with increas-
ing the stress triaxiality. Noting that the true frac-
ture strain is found to be exponentially dependent
on the stress triaxiality (Rice and Tracey 1969), the
following regression is proposed:

$$
\varepsilon_{\mathrm{ef}}=3.29 \exp \left(-1.54 \frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}}\right)+0.10 \tag{8}
$$

which is shown in Fig. 12 with a dotted line. It shows
that Eq. 8 agrees with the data and captures depen-
dence of the stress triaxiality on equivalent strain
to fracture.

![](./images/812008037408571393_21.jpg)

Fig. 12 True fracture strains (equivalent strain to fracture)
as a function the stress triaxiality from two criteria, one
based on the critical location criterion and the other on the
section average criterion

The first approach, described above, is based on
local stress and strain information where failure
initiation is likely to occur. As failure initiation is
likely to occur in the location where damage is the
highest, the first approach is physically sound. This

![](./images/812008037408571393_22.jpg)

approach is termed as the "critical location crite- rion". The second approach is based on stress and strain information, averaged over the minimum section, and will be termed as the "section aver- age criterion". The reason behind this approach is as follows. For a pipe with a surface defect, it would be of interest to assess the eventuality of the surface defect to penetrating through the wall thickness. In such case, the size of the remaining ligament through the wall thickness would be sim- ilar to that in present tensile tests (which is 6 mm). Thus, for engineering assessment of the ligament fracture, averaged stress and strain would be rel- evant. Figure 11b shows variations of the stress triaxiality with equivalent strain, both of which are averaged FE values over the minimum (necked) section. It also includes constant stress triaxiality values averaged over the loading history according to Eq. 7. Following the procedures given above, the following expression of a ductile failure criterion is obtained:

$$
\varepsilon_{\mathrm{ef}}=3.41 \exp \left(-2.23 \frac{\sigma_{\mathrm{m}}}{\sigma_{\mathrm{e}}}\right)+0.22 \tag{9}
$$

which is shown in Fig. 12 with a solid line. As expected, Eq. 9 is lower than Eq. 8.

To predict ductile failure of gas pipelines made of API X65 steels using the present approaches, the proposed equations, Eq. 8 or Eq. (9), should be combined with detailed elastic-plastic FE anal- yses from which local stresses and strains are deter- mined. One interesting point is possible mesh size effects. It is known that local stresses and strains from FE analyses can be sensitive to the mesh size, in particular when steep stress and strain gradi- ents are present in regions around cracks or sharp notches. Note that for smooth and notched ten- sile bars considered in the present work, stress and strain gradients are not so significant, except for the sharpest notched bar with the 0.2 mm notch radius, and thus the mesh size effects are believed not to be significant in general. However, in general problems, such effects could be significant. Thus for the first approach (the critical location criterion) where failure predictions are based on local stress and strain information at the particular location, predictions could be sensitive to FE mesh sizes. For the second approach, on the other hand, pre- dictions are based on averaged stress and strain information. Thus they should be less sensitive to mesh size and could offer an advantage in practice.

![](./images/812008037408571393_23.jpg)

Fig. 13 Schematic illustrations for pipes with gouge

## 5 Discussion

In the present work, ductile failure criteria in terms of true fracture strain (the equivalent strain to frac- ture) are proposed as a function of the stress triax- iality (defined by the ratio of the hydrostatic stress to the equivalent stress) for the API X65 steel. Two different failure criteria are given, one based on local stress and strain information at the critical location within smooth and notched bars where failure initiation is likely to take place, and the other based on averaged stress and strain infor- mation over the ligament where ductile fracture is expected. The present work would be useful to perform assessment of API X65 gas pipelines for possible defects such as corrosion, dents and/or gouges. As a case study, the ductile failure crite- rion is applied to assess burst pressure of API X65 pipes with a gouge and the assessment results are compared with experimental data.

Figure 13 depicts geometries of a pipe with a gouge, and some important dimensions are sum- marized in Table 2. The pipe has the diameter of $D_{\mathrm{o}}=762 \mathrm{~mm}$, the thickness of $t=17.5 \mathrm{~mm}$, and the total length of $L=2,300 \mathrm{~mm}$. The gouge is characterized by the 45 degree V-notch with the circular notch radius of 2 mm. The depth of the gouge is $d=8.75 \mathrm{~mm}$ which is $50 \%$ of the pipe thickness $(d / t=0.5)$. Two gouge lengths were considered: one with $\ell=100 \mathrm{~mm}$ and the other with $\ell=200 \mathrm{~mm}$. Figure 14 depicts test set-up.

![](./images/812008037408571393_24.jpg)

<table>
<caption>Table 2 Geometries of full-scale pipe tests with gouge</caption>
<thead>
<tr>
<th>Pipe no.</th>
<th>$D_{\rm o}$ (mm)</th>
<th>$L$ (mm)</th>
<th>$t$ (mm)</th>
<th>$d$ (mm)</th>
<th>$d/t$</th>
<th>$l$ (mm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>MNA</td>
<td rowspan="2">762</td>
<td rowspan="2">2300</td>
<td rowspan="2">17.5</td>
<td rowspan="2">8.75</td>
<td rowspan="2">0.5</td>
<td>100</td>
</tr>
<tr>
<td>MNB</td>
<td>200</td>
</tr>
</tbody>
</table>

![](./images/812008037408571393_25.jpg)

Fig. 14 (a) Test set-up of full-scale burst test for pipes with gouge, (b) initial gouge and (c) gouge at failure

The pipes were pressurized by water and burst pressures—at the point when the ligament failed—were experimentally determined. Figure 14 also includes photos of the gouge before and after the test. The measured pressures from full-scale pipe tests are summarized in Table 3, which shows that the burst pressure decreases with increasing the gouge length. For $\ell=100$ mm, the burst pressure is about 24.7 MPa but for $\ell=200$ mm, about 22.6 MPa.

The pipes with a gouge were modeled using finite elements. A typical finite element mesh is shown in Fig. 15, with detailed view on the defective region. The number of elements and nodes in FE meshes are 7,590 elements/35,160 nodes and 8,895 elements/41,035 nodes, depending on the length of the gouge. For both cases, however, the smallest element size in the defective area was fixed to $0.32\,{\rm mm} \times 0.67\,{\rm mm} \times 1.19\,{\rm mm}$. Internal pressure was applied to the inner surface of the pipe, together with end forces to simulate the closed cap condition. From FE analyses, the equivalent strain and stress triaxiality were monitored as a function of internal pressure.

Note that two criteria were given in the present paper: one based on local stress and strain information at the site where failure initiation is likely to take place (the critical location criterion), and the other based on averaged stress and strain information over the ligament where ductile fracture is expected (the average section criterion). Figure 16a shows radial variations of stress triaxiality and equivalent strain for the MNB pipe test. In Fig. 16a, the radial distance is normalized with respect to the minimum ligament size, and the values of 0 and 1 mean the inner surface and the notch tip of the pipe, respectively. It shows that equivalent strain take their maximum values in the notch tip, but the maximum value of stress triaxiality occurs somewhere in between the notch tip and the center. To speculate the most damaged (critical) site for failure initiation in the minimum section, the degree of damage was estimated, using the damage indicator given in Eq. 4. Variations of the resulting damage with the normalized distance $(r/a)$ are shown in Fig. 16b, suggesting that the tip of the gouge is the most critical site for failure initiation.

![](./images/812008037408571393_26.jpg)

<table>
<caption>Table 3 Comparison of burst pressures measured from experiments with estimated ones using the proposed failure criteria</caption>
<thead>
<tr>
<th>Pipe no.</th>
<th>Experiment (MPa)</th>
<th colspan="2">FE results (MPa)</th>
<th>Eq. 12</th>
</tr>
<tr>
<th></th>
<th></th>
<th>Eq. 10</th>
<th>Eq. 11</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>MNA</td>
<td>24.68</td>
<td>24.16 (−2.2%)</td>
<td>24.26 (−1.7%)</td>
<td>21.18 (−14.2%)</td>
</tr>
<tr>
<td>MNB</td>
<td>22.48</td>
<td>21.58 (−4.0%)</td>
<td>21.86 (−2.8%)</td>
<td>17.6 (−21.7%)</td>
</tr>
</tbody>
</table>

Fig. 15 Typical finite
element mesh for pipes
with gouge
![](./images/812008037408571393_27.jpg)

![](./images/812008037408571393_28.jpg)

Fig. 16 (a) Distributions of stress triaxiality and equivalent strain for the MNB pipe with gouge; and (b) variations of damage, defined by Eq. 4, with the normalized distance for pipes with gouge

For pipes with a gouge under internal pressure, failure initiation should occur from the tip of the gouge, and thus stress and strain information was extracted from the first element at the tip of the notch for the critical location criterion. For the criterion based on averaged information, stress and strain were averaged over the minimum ligament from the notch tip to the inner surface. Figure 17 shows variations of the stress triaxiality with equivalent strain, for both the critical location criterion and the average section criterion. The stress triaxiality for the critical location criterion is lower than that for the average section criterion, simply because the maximum stress triaxiality occurs

![](./images/812008037408571393_29.jpg)

![](./images/812008037408571393_30.jpg)

Fig. 17 Variations of the stress triaxiality with the equivalent strain for pipes with gouge for the critical location criterion and the section average criterion: (a) MNA pipe test and (b) MNB pipe test

somewhere in between the notch tip and the center.
Figure 17 also includes constant stress triaxiality values averaged over the loading history accord- ing to Eq. 7. It is interesting to note that for both cases the magnitude of the stress triaxiality does not depend on the equivalent strain and is almost constant. Accordingly it is also close to the aver- age stress triaxiality, defined by Eq. 7, as shown in Fig. 17. Another notable point is that the values of the average stress triaxiality are quite low: for the critical location criterion, it is about 0.85, and for the section average criterion, about 0.55. Such low values are typical for pipes under internal pressure.

Based on the proposed ductile failure criterion, burst pressures can be estimated, and are com- pared with experimentally measured data in Table 3. Figure 18 shows variations of internal pressure with radial displacement of the defective pipes, numerically measured at the inner surface in the minimum section. It also includes symbols indicat- ing failure predicted by the present failure crite- ria. As expected, the criterion based on the critical location provides slightly lower burst pressure than that based on the section average, although they are nearly the same. The estimated values are slightly higher than experimentally measured ones, but the differences are within 2.5%. One nota- ble point is that the criterion based on the critical location can be mesh sensitive, and if finer meshes are used, the predictions will be lower and could be closer to experimental values. However, use of finer meshes requires much more modeling effort and computational costs. Good agreements shown in this example provide confidence in the appli- cation of the proposed ductile fracture criteria to defect assessment of gas pipelines. Gouge defects can also be assessed using a global criterion such as the net-section limit load approach, rather than a local criterion such as the proposed one. Noting

![](./images/812008037408571393_31.jpg)

Fig. 18 Variations of pressure with radial displacement, determined from the FE analyses, indicating predicted fail- ure points

![](./images/812008037408571393_32.jpg)

that an engineering assessment equation for gouge defects is not currently available, gouge defects could be assessed using the following expression of failure pressure of axial surface cracked pipes under internal pressure, assuming that the gouge is idealized as the (axial) crack (ASME 1992):

$$
P_{\mathrm{f}}=P_{\mathrm{o}}\left(\frac{1-\frac{a}{t}}{1-\frac{a}{t} \cdot \frac{1}{M}}\right) ;
$$

$$
M=\sqrt{1+1.61 \frac{\ell^{2}}{4 R_{\mathrm{m}} t}} \tag{10}
$$

where $a$ and $\ell$ denote the crack depth and length, respectively. As the gouge is idealized as the (axial) crack, Eq. 10 can be used to estimate failure pressure, simply by replacing the crack depth $a$ with the gouge depth $d$. Resulting predictions are compared in Table 3, which shows that failure loads from Eq. 10 are lower than those from the proposed method by 14–22%. This suggests that the proposed method could significantly reduce conservatism in defect assessment of pipelines.

As discussed above, the stress-modified fracture strain concept could be quite useful for defect assessment of gas pipelines. Compared to a global approach, it can give more accurate (less conservative) failure predictions, as shown in the present example. Moreover, by reducing the number of expensive and time-consuming full-scale tests, it could provide a cost-effective way to develop defect assessment equations. However, the concept is material specific in the sense that relevant materials parameters should be determined first. One significant result of the present work is to determine the material parameters of the API X65 steel for the stress-modified fracture strain concept. Once determined, the proposed stress-modified fracture strain model can be applied to API X65 pipes with any type of defect and under various loading conditions. It is believed that the present model would be suited to assessment of API X65 pipelines with volumetric defects such as corrosion, dents and/or gouges. Application of the present model to planar defects such as cracks is questionable, due to possible numerical problems associated with steep stress/strain gradient near the crack tip and the mesh size. It could be noted that, being based on the same micro-mechanical conception, local approaches based on damage models have gained more importance in predicting ductile failure of defective components (Gurson 1977; Beremin 1981; Rousselier 1987; Tvergaard 1981, 1982; Tvergaard and Needleman 1982; Zuo et al. 2004). Such approaches based on damage models would be better suited to crack-like defect assessments, see for instance Bernauer and Brocks (2002), Dotta and Ruggieri (2004), Rivalin et al. (2001), and Chen and Lambert (2003). The authors have also developed the ductile damage model for API X65 steels and applied it to investigate the effect of pre-strain on deformation and fracture (Oh et al. 2006).

## 6 Conclusions

The present paper provides ductile failure criteria in terms of true fracture strain (the equivalent strain to fracture) as a function of the stress triaxiality (defined by the ratio of the hydrostatic stress to the equivalent stress) for the API X65 steel. To determine the stress-modified fracture strain, smooth and notched tensile bars with four different notch radii are performed, from which true fracture strains are determined as a function of the notch radius. Then detailed elastic-plastic, large strain FE analyses are performed to estimate variations of stress triaxiality in the notched bars with load. Combining these FE results with experimental ones provides true fracture strains as a function of stress triaxiality. Two different failure criteria are given, one based on local stress and strain information at the point where failure initiation is likely to take place, and the other based on averaged stress and strain information over the ligament where ductile fracture is expected. Both expressions show that fracture strain depends strongly on the stress triaxiality. Such criteria could be used to perform defect assessment of API X65 gas pipelines in conjunction with detailed elastic-plastic FE analyses. As a case study for application, API X65 pipes with a gouge are simulated using elastic-plastic FE analyses with the proposed ductile failure criteria and the resulting burst pressures are compared with experimental data. Agreement is quite good, which gives confidence in the use of the proposed criteria to defect assessment for gas pipelines.

![](./images/812008037408571393_33.jpg)

### References

Alves M, Jones N (1999) Influence of hydrostatic stress on failure of axisymmetric notched specimens. J Phys Mech Solids 47:643–667

American Petroleum Institute (2000) Specification for line pipe

American Society of Mechanical Engineers (1992) ASME Boiler and Pressure Vessel Code Section IX

Anderson TL (1995) Fracture mechanics—fundamentals and applications. CRC Press

Bao Y (2005) Dependence of ductile crack formation in tensile test on stress triaxiality, stress and strain ratios. Eng Fract Mech 72:505–522

Bao Y, Wierzbicki T (2004) On fracture locus in the equivalent strain and stress triaxiality space. Int J Mech Sci 46:81–98

Beremin FM (1981) Cavity formation from inclusions in ductile fracture of A 508 steel. Metall Trans 12A:723–731

Bernauer G, Brocks W (2002) Micro-mechanical modeling of ductile damage and tearing-results of a European numerical round robin. Fatigue Fract Eng Mater Struct 25:363–384

Bridgman P (1952) Studies in large plastic flow and fracture. McGraw-Hill Book Company Inc., New York

Chen Y, Lambert S (2003) Analysis of ductile tearing of pipeline-steel in single edge notch tension specimen. Int J Fract 124:179–199

Chu C, Needleman A (1980) Void nucleation effects in biaxially stretched sheets. J Eng Mater Technol 102:249–256

Clausing DP (1970) Effect of plastic strain state on ductility and toughness. Int J Fract Mech 6:71–85.

Cosham A, Hopkins P (2004) The effect of dents in pipelines-guidance in the pipeline defect assessment manual. Int J Pressure Vessels Piping 81:127–139

Garrison WR Jr, Moody NR (1987) Ductile fracture. J Phys Chem Solids 48:1035–1074

Dotta F, Ruggieri C (2004) Structural integrity assessments of high pressure pipelines with axial flaws using a micromechanics model. Int J Pressure Vessels Piping 81:761–770

Gurson AL (1977) Continuum theory of ductile rupture by void nucleation and growth—yield criteria and flow rules for porous ductile media. J Eng Mater Technol 99:2–15

Hancock JW, Mackenzie A (1976) On the mechanisms of ductile failure in high-strength steels subject to multiaxial stress states. J Phys Mech Solids 24:147–169

Hancock JW, Cowling MJ (1980) Role of state of stress in crack-tip failure processes. Metal Sci 293–304

Hibbitt, Karlson & Sorensen Inc. (2005) ABAQUS Version 6.4 user’s manual

Kanninnen MF, Zahoor A, Wilkoski G et al (1982) Instability predictions for circumferentially cracked Type-304 stainless pipes under dynamic loading. EPRI report NP-2347, Electric Power research Institute, Palo Alto, USA

Kim YJ, Oh CK, Myung MS et al (2006) Fully plastic analyses for notched bars and plates using finite element limit analysis. Eng Fract Mech 73:1849–1864

Koplik J, Needleman A (1988) Void growth and coalescence in porous plastic solids. Int J Solids Struct 24:835–853

La Losa G, Mirone G, Risitano A (2001) Effect of stress triaxiality corrected plastic flow on ductile damage evolution in the framework of continuum damage mechanics. Eng Fract Mech 68:417–434

La Losa G, Mirone G, Risitano A (2003) Postnecking elastoplastic characterization: degree of approximation in the Bridgman method and properties of the flow-stres/true-stress ratio. Metall Mater Trans A Phys Metall Mater Sci 34:615–624

Mackenzie A, Hancock JW, Brown D (1977) On the influence of state of stress on ductile failure initiation in high strength steels. Eng Fract Mech 9:167–188

McClintock FA (1968) A criterion of ductile fracture by the growth of holes. J Appl Mech 35:363–371

Oh CK, Kim YJ, Baek JH (2006) A micro-mechanical model of ductile fracture of API X65 steels and application to pre-strain effects on deformation and fracture. Int J Mech Sci (submitted)

Rice JR, Tracey DM (1969) On the ductile enlargement of voids in triaxial stress fields. J Phys Mech Solids 17:201–217

Ritchie RO, Thompson AW (1985) On macroscopic and microscopic analyses for crack initiation and crack growth toughness in ductile alloys. Metall Trans A 16A:233–248

Rivalin F, Besson J, Pineau A, Di Fant M (2001) Ductile tearing of pipeline-steel wide plates II-modeling of in-plane crack propagation. Eng Fract Mech 68:347–364

Rousselier G. (1987) Ductile fracture models and their potential in local approach of fracture. Nucl Eng Design 105:97–111

Schiffman R, Bleck W, Dahl W (1998) The influence of strain history on ductile failure of steel. Comput Mater Sci 13:142–147

Schluter N, Grimpe F, Bleck W et al (1996) Modeling of the damage in ductile steels. Comput Mater Sci 7:27–33

Theocaris PS (1995) Failure criteria for isotropic bodies revisited. Eng Fract Mech 51:239–264

Thomason PF (1990) Ductile fracture of metals. Pergamon Press, Oxford, UK

Tvergaard V (1981) Influence of voids on shear band instabilities under plane strain conditions. Int J Fract 17:389–407

Tvergaard V (1982) On localization in ductile materials containing spherical voids. Int J Fract 18:237–252

Tvergaard V, Needleman A (1982) Analysis of the cup-cone fracture in a round tensile bar. Acta Metall 32:157–169

Valiente A (2001) On Bridgman’s stress solution for a tensile neck applied to axisymmetrical blunt notched tension bars. J Appl Mech 68:412–419

Wilkoski G, Stephens D, Krishnaswamy P et al (2000) Progress in development of acceptance criteria for local thinned areas in pipe and piping components. Nucl Eng Design 195:149–169

Zuo J, Sutton MA, Deng X (2004) Basic studies of ductile failure processes and implications for fracture prediction. Fatigue Fract Eng Mater Struct 27:231–243

![](./images/812008037408571393_34.jpg)