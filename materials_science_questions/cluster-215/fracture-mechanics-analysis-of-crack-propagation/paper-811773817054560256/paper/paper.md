# Prediction of shear-induced fracture in sheet metal forming

Yaning Li $^{a,*}$, Meng Luo $^{a}$, Jörg Gerlach $^{b}$, Tomasz Wierzbicki $^{a}$

$^{a}$ Massachusetts Institute of Technology, Cambridge, MA, United States
$^{b}$ ThyssenKrupp Steel Europe AG, Duisburg, Germany

---

## A R T I C L E  I N F O

**Article history:**
Received 11 February 2010
Received in revised form 6 June 2010
Accepted 28 June 2010

**Keywords:**
Shear-induced fracture
Sheet metal forming
Forming Limit Diagram (FLD)
Fracture Forming Limit Diagram (FFLD)
Modified Mohr-Coulomb criterion (MMC)
Advanced High Strength Steels (AHSS)

---

## A B S T R A C T

Necking has been the dominant failure mode in sheet metal forming industry and several analytical and numerical tools were developed to predict the onset of necking. However, the introduction of Advanced High Strength Steels (AHSS) with reduced ductility brought up an issue of a shear fracture which could not be predicted using the concept of Forming Limit Curve (FLC). The Modified Mohr-Coulomb fracture criterion (MMC) was recently shown to be applicable to problems involving ductile fracture of materials and sheets. In the limiting case of plane stress, the fracture locus consists of four branches when represented on the plane of the equivalent strain to fracture and the stress triaxiality. A transformation of above 2D fracture locus to the space of principal strains was performed which revealed the existence of two new branches not extensively studied before. The existence of those branches explains the formation of shear-induced fracture. As an illustration of this new approach, initiation and propagation of cracks is predicted and compared with series of deep-drawing punch tests of ThyssenKrupp AHSS (grade RA-K 40/70, standard HCT690T) performed at ThyssenKrupp. It was shown that the location of fracture as well as the magnitude of punch travel corresponding to first fracture was correctly predicted by MMC fracture criterion for both circular and square punch.

© 2010 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Sheet forming is mainly a tensile process that may be limited by necking, tearing, fracture or wrinkling. The science and art of sheet forming is to achieve the required final shape without producing strains that approach any of these limits. Forming Limit Diagram (FLD) first introduced by Keeler and Backofen (1963) and Goodwin (1968) has been developed for decades and is widely used in deep-drawing industry as a useful tool for predicting limits of sheet forming operations. Finite element method has been widely used to look for numerical solution of sheet metal forming application. Taylor et al. (1995) used both implicit and explicit modules of ABAQUS to simulate sheet metal forming. Cao and Boyce (1997) developed a methodology to predict wrinkling failure using numerical tools. For a review of the existing strain-based theoretical models including Swift's criterion, Hill's criterion, Storen and Rice bifurcation analysis (1975), M-K method and their corresponding stress-based forms, a reader is referred to Stoughton and Zhu (2004). All these models were derived from the necking and stability analysis in the plane of a sheet. Bressan and Williams (1983) proposed an alternative approach based on stability analysis through the thickness. Alsos et al. (2008) combined this criterion with Hill's instability criterion (1952) as BWH criterion and used it for numerical analysis of sheet metal instability. The range of validity of all these models is restricted to the strain ratio $-1/2 \leq \alpha \leq 1$, corresponding to stress states between the uniaxial and biaxial tension. No reliable model exists to predict failure of sheet between the uniaxial tension ($\alpha=-1/2$) through pure shear ($\alpha=-1$) all the way to uniaxial compression ($\alpha=-2$). Because of this deficiency, none of existing models can predict shear-induced fracture during forming for these strain paths.

Earlier work on fracture theory incorporating stress triaxiality and Lode angle was pursued at Engineering System International (ESI) and incorporated into previous releases of the software PAM-CRASH. Pickett et al. (2004) studied and evaluated several micro- and macro-constitutive and failure laws, when PAM-CRASH was used for studying the crashworthiness of high strength steels. Kamoulakos (2002) showed a method of numerically simulating metal rapture using PAM-CRASH, and Lemoins and Kamoulakos (2003) applied this method to study the failure of high strength steels. Subsequently, the BMW/CrashFEM team proposed a method of predicting fracture using a combination of two distinct branches of the fracture locus, one representing void growth and linkage and the other one shear fracture. Hooputra et al. (2004) discussed the effectiveness of this approach in predicting failure by comparing numerical results with test data by 3-point bending and axial compression tests of double chamber extrusion components made from aluminum alloy EN AW-7108 T6.

---

* Corresponding author at: Massachusetts Institute of Technology, Mechanical Engineering, 77 Massachusetts Ave., Room 5-218, MIT, Cambridge, United States.
E-mail address: yaningli@mit.edu (Y. Li.)

0924-0136/$ – see front matter © 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.jmatprotec.2010.06.021

Kessler et al. (2008) proposed an post instability strain model for shells (PIS Model), which combines the model for localized necking with the model for ductile shear fracture, and applied it to simulate Nakajima tests and 3-point bending test of an automotive component. Recently, necking condition was used by Hudgins et al. (2010) to predict a failure at the die and punch radius.

Team of researchers at the Impact and Crashworthiness Lab (ICL) at MIT proposed much more approaches to ductile fracture of metals and sheets together with the calibration procedure. For example, Bao and Wierzbicki (2004) determined a fracture diagram in a wide range of stress triaxiality based on the results of 36 meticulous experiments and numerical simulations of several types of specimens. More recently, a general form of an asymmetric fracture model, considering both the pressure sensitivity and the Lode dependence, was postulated by Xue (2007) and Bai and Wierzbicki (2010). In the present paper, a plane stress version of the more general 3D Modified Mohr-Coulomb fracture model will be used. It is shown that the MMC fracture criterion is applicable to the whole range of strain ratio ($-2 < \alpha \leq 1$) and therefore it can successfully capture the experimentally observed shear-induced fracture in punch forming. The MMC fracture locus consists of four branches in the space of equivalent strain to fracture and the stress triaxiality. These branches can be transformed into four branches in the Forming Limit Diagram (FLD) accordingly, which is explained in Section 4 in detail.

The problem of stretch bending of a strip has been studied extensively in the literature. Analytical solutions for fracture initiation on the punch and die radii utilizing MMC fracture model were recently developed by Bai and Wierzbicki (2010) and Issa (2009). Luo and Wierzbicki (in press) successfully applied the MMC fracture model to predict fracture of a metal strip at the die and punch radius. Their numerical solution was shown to correlate well with test reported by Zeng et al. (2009). It is interesting that the first application of fracture initiation and propagation with element deletion under punch loading came from the ship rather than sheet metal forming industry (Alsos et al., 2009). They presented a detailed analysis of unstiffened and stiffened flat plates loaded by a rounded conical punch and compared the results with their own experiments.

The present paper reports on an extensive numerical and experimental study of the deep-drawing process leading to initiation and propagation of cracks within the realm of MMC fracture model. The most interesting conclusion drawn from this research is that for certain combination of material parameters and forming tools, shear-induced fracture was observed which cannot be predicted by the existing FLD approach. Further more, the strain paths at critical locations were not proportional so that the history dependent fracture model to be outlined in what follows must be used. The punch forming process was modeled by shell elements in ABAQUS/EXPLICIT v-6.8. In order to make a prediction more accurate, the fracture criterion was checked at every integration point through thickness. In this way, through thickness crack propagation was captured.

## 2. Comparative study of existing failure criteria for sheet metal application

This section presents a brief review of the two representative approaches to predict failure of sheets with an objective to point out on the limitations. Traditionally, local necking has been considered as a limiting condition for sheet metal forming. Out of many different formula in the existing literature, Hill (1952) and Storen and Rice (1975) (called H-SR criterion in the present study) are

![](./images/811773817054560256_1.jpg)

Fig. 1. Sketch of Hill's criterion and BW criterion (Bressan and Williams, 1983) (in-plane tension is in plane 1-2) (a) Hill's criterion and (b) BW criterion.

mostly used by the industry, as shown in Eq. (1)

$$
\varepsilon_{1}^{\mathrm{H}-\mathrm{SR}}=
\begin{cases}
\frac{n}{1+\alpha} & -1<\alpha \leq 0 \quad \text { negative quadrant } \\
\frac{3 \alpha^{2}+n(2+\alpha)^{2}}{2(2+\alpha)\left(1+\alpha+\alpha^{2}\right)} & 0 \leq \alpha \leq 1 \quad \text { positive quadrant }
\end{cases},
\tag{1}
$$

where $n$ is the exponent of the power hardening law and $\alpha$ is the strain increment ratio:

$$
d \varepsilon_{2}=\alpha d \varepsilon_{1}. \tag{2}
$$

The basis of the derivation of Eq. (1) is an assumption that necking instability occurs in the direction where zero extension holds in the plane of the sheet in the negative quadrant, and bifurcation occurs in the positive quadrant of the FLD (Storen and Rice, 1975), see Fig. 1a.

The orientation of the localized necking band is related to the strain ratio by

$$
\varphi=\tan ^{-1}(-\alpha), \quad \alpha>-1 \tag{3}
$$

where $\varphi$ represents the direction of the localized shear band in plane 1-2 predicted by Hill's criterion. The plot of H-SR criterion in two different coordinate systems is shown in Fig. 2a by red dash lines (for interpretation of the references to color in this sentence, the reader is referred to the web version of the article).

An alternative and very interesting way of predicting stability of sheets was proposed by Bressan and Williams (1983) and applied to the problem of ship grounding by Alsos et al. (2009). By contrast to H-SR criterion, BW criterion was derived on the assumption of the existence of zero extension in the through thickness direction, see Fig. 1b. The orientation of the plane of critical shear stress is predicted by

$$
\cos 2 \theta=-\frac{\alpha}{2+\alpha}, \quad-1 \leq \alpha<1 \tag{4}
$$

where $\theta$ represents the direction of the localization band in plane 1-3 predicted by BW criterion, shown in Fig. 1b. The instability condition is valid for both first and second quadrant, Eq. (5).

$$
\varepsilon_{1}^{B W}=n\left(\frac{\sqrt{2(2+\alpha)}}{3}\right)^{1 / n}\left(1+\alpha+\alpha^{2}\right)^{(1 / 2 n)-1 / 2}, \quad-1<\alpha<1 \ (5)
$$

A plot of Eq. (5) is shown in Fig. 2a by the black dotted lines. Eqs. (1) and (5) are seen to be almost identical in the first quadrant. There is a gradually increasing difference between those two functions in the second or negative quadrant of FLD.

The criteria of ductile fracture have been represented by many authors on the plane of the equivalent fracture strain to failure and the stress triaxiality. Under the assumption of plane stress, there is a unique relation between the stress triaxiality $\eta$ and the strain ratio $\alpha$ for an isotropic material:

$$
\eta=\frac{\sigma_{m}}{\bar{\sigma}}=\frac{1+\alpha}{\sqrt{3} \sqrt{1+\alpha+\alpha^{2}}} \tag{6}
$$

![](./images/811773817054560256_2.jpg)

Fig. 2. Comparison of MMC-FFLD and FLDs in two spaces: (a) in the space of major and minor principal strains; (b) in the space of stress triaxiality and equivalent strain to failure.

where $\bar{\sigma}$ is the equivalent stress and $\sigma_{m}$ is the mean stress. In addition, from the definition of the equivalent strain for material exhibiting plastic isotropy, one has

$$
d\bar{\varepsilon} = \frac{2d\varepsilon_{1}}{\sqrt{3}} \sqrt{1+\alpha+\alpha^{2}} \tag{7}
$$

Using the above equations, the transformed H-SR, BW failure loci are compared in Fig. 2b. The range of the applicability of the necking/failure criteria are from the equi-biaxial tension to uniaxial tension. The shaded areas in Fig. 2 a and b represent the range where shear fracture could occur in sheet metal forming operations and this range will be studied more carefully in the subsequent sections.

The above two failure criteria work well for most of the sheet metal forming operations but are unable to predict in-plane shear fracture. To do this, the problem should be attacked from an entirely new angle, as outlined below.

## 3. Deep-drawing tests of TRIP 690

Sheet metal forming by deep drawing is a common manufacturing process used in many industries, especially the automotive industry. The material studied in this investigation is one product of ThyssenKrupp in the category of the Advanced High Strength Steel (AHSS), grade: RA-K 40/70, standard HCT690T, which is cold rolled Retained Austenite Steel (TRIP steel) with 690 MPa minimum tensile strength. So it is called TRIP690 in this paper. TRIP steel is an important member of the family of AHSS. In order to investigate the formability of a TRIP690 steel sheet, a series of deep-drawing tests were conducted at ThyssenKrupp Steel Europe AG (Germany). All blanks in this study are extracted from 1.6 mm thick TRIP 690 sheet.

The schematic diagram of the deep-drawing operation is shown in Fig. 3. During the whole operation, a constant blank-holder force is applied on the blank sheet, while the punch travels downward and draws the blank sheet into the die cavity. Certain lubricant was applied to all the contact surfaces. In the present study, two different punches were adopted. One features a square cross-section, and the other one has a circular cross-section. Corresponding dies and blank-holders were employed to match the punch geometry.

The major objective of this study is to predict failure in the deep-drawing operations with a phenomenological fracture model. Therefore, for each test condition, the drawing depth was gradually increased until the first crack was observed on the sheet. The drawing depth at fracture initiation, as well as the load-displacement response was recorded for each test condition.

![](./images/811773817054560256_3.jpg)

Fig. 3. Schematic diagram of the deep-drawing operation.

### 3.1. Square punch test

For the square punch tests, the edge length of the punch cross-sectional square is $d = 70$ mm. The punch radius is $r_{1} = 10$ mm, and the die radius is $r_{2} = 5$ mm. The blank sheet is in square shape for the square punch test, and its edge length is $D_{0} = 150$ mm. The sheet was arranged at two orientations $0^{\circ}$ and $45^{\circ}$ by rotating the rolling direction of the sheet in the coordinate system of the punch, thus two different boundaries are set up, as shown in Fig. 4. Constant blank-holder force (BHF) was kept during punching operation. The BHF of case 1 is 50 kN, the BHF of case 2 is 30 kN.

![](./images/811773817054560256_4.jpg)

Fig. 4. Top view of two cases of square punch tests with different sheet orientations.

![](./images/811773817054560256_5.jpg)

### 3.2. Circular punch test

The top view of the circular punch test is shown in Fig. 5. In this test, the diameter of the circular punch cross-section is $d = 100$ mm. The punch radius is $r_1 = 13$ mm, and the die radius is $r_2 = 5$ mm. The blank sheet for the circular punch test is in rectangular shape with a length $D_0 = 250$ mm and a width $D_1 = 150$ mm. The rolling direction of the TRIP690 sheet is aligned with the width of the blank, as shown in Fig. 5. Throughout the circular punch tests, a constant blank-holder force of 200 kN was applied.

## 4. Material model

### 4.1. Plasticity modeling and characterization

TRIP 690 steel sheets were shown by Bai and Wierzbicki (2010) to exhibit little anisotropy in plasticity, therefore, von Mises isotropic yield functions are employed in this study. Under plane stress condition ($\sigma_3 = 0$), von Mises yield criteria take the forms shown in Eq. (8)

$$
\sigma_{1}^{2}+\sigma_{2}^{2}-\sigma_{1} \sigma_{2}=\sigma_{Y}^{2} \tag{8}
$$

where $\sigma_1, \sigma_2$ are two principal stresses in the sheet plane, while $\sigma_Y$ is the tensile yielding stress in the sheet rolling direction.

Besides the yield condition, the flow rule and hardening law are also important building blocks for the plasticity modeling. Here, associated flow rule and isotropic power law hardening are used for both yield functions. The power hardening law reads $\bar{\sigma}=A \bar{\varepsilon}^{n}$, where $\bar{\sigma}$ and $\bar{\varepsilon}$ are equivalent stress and equivalent strain defined by the yield condition, while $A$ and $n$ are material parameters to be calibrated. For the present TRIP690 sheet, $A$ and $n$ are determined by fitting the stress-strain curve obtained from uniaxial tensile test along the rolling direction. As shown in Fig. 6, with hardening parameters $A = 1276$ MPa and $n = 0.2655$, an encouraging curve fitting was obtained.

![](./images/811773817054560256_6.jpg)

### 4.2. Summary of MMC fracture model

There are two concepts on which the present fracture theory is based. The first concept is the definition of the damage indicator.

$$
D=\int_{0}^{\bar{\varepsilon}} \frac{d \bar{\varepsilon}}{f(\eta, \bar{\theta})}. \tag{9}
$$

where $\bar{\varepsilon}$ is the equivalent plastic strain, $\eta$ is the stress triaxiality, $\eta=\sigma_{m} / \bar{\sigma}, \sigma_{m}$ is the mean stress, $\bar{\sigma}$ is the equivalent stress and $\bar{\theta}$ is the Lode angle parameter, which is defined as

$$
\bar{\theta}=1-\frac{2}{\pi} \arccos \left(\left(\frac{r}{\bar{\sigma}}\right)^{3}\right) \tag{10}
$$

where $r$ is the third invariant of the deviatoric stress tensor $\underline{S}$, and

$$
r=\left(\frac{9}{2} \underline{S}: \underline{S}: \underline{S}\right)^{1 / 3}=\left[\frac{27}{2}\left(\sigma_{1}-\sigma_{m}\right)\left(\sigma_{2}-\sigma_{m}\right)\left(\sigma_{3}-\sigma_{m}\right)\right]^{1 / 3}. \quad(11)
$$

The Lode angle is related to the third invariant of stress deviator. The fracture is said to occur when $\bar{\varepsilon}=\bar{\varepsilon}_{f}$, and $D=1$ for any combinational non-proportional and proportional loading. The interpretation of the function $f(\eta, \bar{\theta})$ becomes clear if one considers a proportional loading for which the nondimensional stress parameters $\eta$ and $\bar{\theta}$ are constant. In this case, the integration in Eq. (9) can be performed and, at the point of fracture:

$$
\bar{\varepsilon}_{f}=f(\eta, \bar{\theta}) \tag{12}
$$

Thus Eq. (12) represents the locus of all stress states under which fracture is achieved along the proportional loading path. This function could be either found by fitting a certain number of experimental points or by making use of a phenomenological model such as the Modified Mohr-Coulomb (MMC) fracture criterion. The former approach was used for example, by Bao and Wierzbicki (2004). The latter one (MMC) will be used in the present paper. According to this model, the function $f(\eta, \bar{\theta})$ is uniquely defined by five parameters, including three new free material parameters $C_1, C_2, C_3$ and takes the following form:

$$
\begin{aligned}
\bar{\varepsilon}_{f}(\eta, \bar{\theta})= & \left\{\frac{A}{C_{2}}\left[C_{3}+\frac{\sqrt{3}}{2-\sqrt{3}}\left(1-C_{3}\right)\left(\sec \left(\frac{\bar{\theta} \pi}{6}\right)-1\right)\right]\right. \\
& \left.\times\left[\sqrt{\frac{1+C_{1}^{2}}{3}} \cdot \cos \left(\frac{\bar{\theta} \pi}{6}\right)+C_{1}\left(\eta+\frac{1}{3} \sin \left(\frac{\bar{\theta} \pi}{6}\right)\right)\right]\right\}^{-1 / n} \quad(13)
\end{aligned}
$$

where $A$ and $n$ are the strength coefficient and the exponent of the power law hardening rule, respectively. The procedure for calibrating the fracture parameters $C_1, C_2$ and $C_3$ is quite complex on its own right and can be found in Beese et al. (2010), Luo and Wierzbicki (2009) and Bai and Wierzbicki (2010). Interested reader is referred to those publications for details. For ThyssenKrupp TRIP 690, the plasticity and fracture parameters are: $A = 1275.9$ MPa, $n = 0.2655$, $C_1 = 0.12$, $C_2 = 720$ MPa, $C_3 = 1.095$ and the above input parameters will be used in the subsequent simulations. The 3D fracture locus, defined by Eq. (13) for TRIP 690 is plotted in Fig. 7. It is evident that the Lode angle parameter influences the equivalent fracture strain to the similar extend as the stress triaxiality.

In the special case of plane stress, the triaxiality and Lode angle parameter are uniquely related through (Wierzbicki and Xue, 2005; Bai and Wierzbicki, 2010; Li et al., submitted for publication; Li and Wierzbicki, 2009; Li and Wierzbicki, 2010):

$$
-\frac{27}{2} \eta\left(\eta^{2}-\frac{1}{3}\right)=\sin \left(\frac{\pi}{2} \bar{\theta}\right) \tag{14}
$$

![](./images/811773817054560256_7.jpg)

Fig. 7. 3D fracture locus in the space of the equivalent strain to fracture, stress triaxiality and Lode angle parameter.

By substituting Eq. (14) into Eq. (13), the 2D plane stress MMC fracture locus is obtained:

$$
\bar{\varepsilon}_{f}(\eta)=\left\{\frac{A}{C_{2}^{2}} f_{3}\left[\sqrt{\frac{1+C_{1}^{2}}{3}} \cdot f_{1}+C_{1}\left(\eta+\frac{f_{2}}{3}\right)\right]\right\}^{-1 / n}
\tag{15a}
$$

where

$$
f_{1}=\cos \left\{\frac{1}{3} \arcsin \left[-\frac{27}{2} \eta\left(\eta^{2}-\frac{1}{3}\right)\right]\right\}
\tag{15b}
$$

$$
f_{2}=\sin \left\{\frac{1}{3} \arcsin \left[-\frac{27}{2} \eta\left(\eta^{2}-\frac{1}{3}\right)\right]\right\}
\tag{15c}
$$

$$
f_{3}=C_{3}+\frac{\sqrt{3}}{2-\sqrt{3}}\left(1-C_{3}\right)\left(\frac{1}{f_{1}}-1\right).
\tag{15d}
$$

Eq. (14), representing all plane stress states, is indicated by the red solid line in Fig. 7.

This line resembles the trajectory of snowboarder in half tube. The 2D projection of the general fracture locus on the $(\bar{\varepsilon}_{f}, \eta)$ plane is presented in Fig. 8.

It consists two smooth branches with a discontinuity point. Note that the third branch between the state of uniaxial and biaxial compression is not plotted in this figure because sheets will buckle rather than fracture in this range.

The fracture envelope presented in Fig. 8 can be transformed to the space of principle strains using Eqs. (2), (6) and (7). The corresponding plot is shown in Fig. 9.

In summary, the MMC fracture locus consists of four branches in the space of equivalent strain to fracture and the stress triaxiality $\eta$, as shown in Fig. 8. The first branch corresponds to the stress states between equi-biaxial tension $(\eta=2 / 3)$ and plane strain $(\eta=1 / \sqrt{3})$. The second branch covers the range from plane strain $(\eta=1 / \sqrt{3})$ to uniaxial tension $(\eta=1 / 3)$. The third branch extends from uniaxial tension $(\eta=1 / 3)$ to pure shear $(\eta=0)$. The fourth and last branch is applicable to the stress states between pure shear $(\eta=0)$ and uniaxial compression $(\eta=-1 / 3)$. Those four branches could also be distinguished after transformation to the space of principal strains and the resulting locus of fracture point is referred to as the Fracture Forming Limit Diagram (FFLD), as shown in Fig. 9. The first branch corresponds to the stress states between equi-biaxial tension $(\alpha=1)$ and plane strain $(\alpha=0)$. The second branch covers the range from plane strain $(\alpha=0)$ to uniaxial tension $(\alpha=-1 / 2)$. The third branch extends from uniaxial tension $(\alpha=-1 / 2)$ to pure shear $(\alpha=-1)$. The fourth and last branch is applicable to the stress states between pure shear $(\alpha=-1)$ and uniaxial compression $(\alpha=-2)$.

![](./images/811773817054560256_8.jpg)

Fig. 8. The 2D, MMC plane stress fracture locus.

![](./images/811773817054560256_9.jpg)

Fig. 9. The 2D, MMC plane stress fracture locus represented in the space of principal true strains.

Fig. 9 represents the complete FFLD. The branches 3 and 4 between the uniaxial tension and pure shear strain are excluded by the conventional FLC for the sheet metal forming community. It offers a clue for predicting shear fracture in sheets that could not be tackled using conventional FLC approach.

Generally, there are two different types of approaches in the literature to study ductile fracture, as explained in Li and Wierzbicki (2010). For the first approach, fracture is modeled as a process of damage accumulation within the continuum, which means the constitutive model and fracture model are coupled. For the second approach, fracture is considered as a sudden event when the stress and strain states of the undamaged continuum reaches a critical level. The former type is referred to as 'coupled' fracture modeling and the latter as 'uncoupled' fracture modeling (Li and Wierzbicki, 2010). Both of them have both advantages and disadvantages. It is need to be noted that in this study, the method used in this paper is the 'uncoupled' approach. The plasticity and fracture is uncoupled and the current fracture model is based on the definition of isotropy. The study of the fracture model with the anisotropic effects is still in progress.

## 5. Finite element modeling

### 5.1. Model description

All the finite element simulations of the present deep-drawing tests were performed in the environment of ABAQUS/Explicit V6.8. The crack initiation and propagation is simulated using the element deletion technique. The element is deleted when all integration points through thickness reach $D=1$. A similar approach was used by Li et al. (submitted for publication) to study the combined Mode I and III crack propagation.

The finite element model of the square punch test is shown in Fig. 10a. The punch, die and blank-holder are modeled as discrete rigid body in ABAQUS, with mesh size $2 \mathrm{~mm} \times 2 \mathrm{~mm}$. The square sheet is modeled by 22,500 four-node shell elements with reduced integration points (S4R in ABAQUS) with a mesh size of

![](./images/811773817054560256_10.jpg)

Fig. 10. Finite element models for the deep-drawing tests of TRIP690: (a) square punch and (b) circular punch.

1 mm × 1 mm. As shown in Fig. 10b, for the circular punch model, the punch, die and blank-holder are modeled as analytical rigid body in ABAQUS because of their simpler geometry, while the blank sheet is discretized using 7500 S4R elements with a mesh size of 2 mm × 2 mm. For both models, 5 Simpson integration points through the thickness of shell elements are used to get reliable simulations for the deep-drawing process which features large bending/unbending processes.

In the simulations, the mesh sizes are chosen due to the fact that the size of either the localized necking zone or shear zone is about the same size as the blank thickness. More extensive study on mesh-size effects of the fracture of TRIP690 can be found in Li and Wierzbicki (2009).

ABAQUS/Explicit is used to solve this quasi-static problem using a dynamic approach. In order to run the simulation more efficiently without influencing the results, certain mass scaling (1000) is employed. Following the same boundary conditions described in the experiments (Section 3), the simulation of the punching process is divided into two steps: In step 1 ($t$=0–1.2 s), a blank-holder force is applied as a ramp type loading, and a gap of 3 mm between the blank-holder and the top surface of the sheet is set up to avoid numerical oscillation caused by potential initial penetration during contact; In step 2 ($t$=0.2–1.2 s), a constant vertical velocity of the punch, 35 mm/s is controlled. The die is fixed, the blank-holder and the sheet has free boundary in both two steps. The punch is fixed in step 1 and is only allowed for vertical movement in step 2.

### 5.2. Calibration of friction coefficients

In the FE simulations, the friction coefficients are assumed the same everywhere between the punch and the sheet, as well as between the die and the sheet, which is not true in reality. Hence, the friction coefficient used in the simulation is an 'average' value with a combination of physical and numerical factors. For the cold rolled uncoated steel in combination with the used lubricant, a friction coefficient of 0.15 is obtained using the patented experimental technique of TKS (Masarczyk and Struppek, 2003). The inverse method is used to adjust the friction coefficients around this value for different simulations to guarantee that the simulation results of load-displacement are accurate before fracture. After the adjustment, the friction coefficients used to simulate the square punch and circular punch tests are 0.17 and 0.10, respectively. As an example to explain the process of the inverse method, the adjustment for case 1 of square punch test is shown in Fig. 11.

![](./images/811773817054560256_11.jpg)

Fig. 11. Determination of friction coefficient using J2 isotropic plasticity model for square punch simulation, case 1.

## 6. Results of simulation and comparison

With the details of the approach discussed above, the punching tests are simulated in ABAQUS V.8. The results are presented and analyzed in this section.

### 6.1. Square punch

#### 6.1.1. Case 1: $0^\circ$

Fig. 12a shows the photo of test with a crack located at the die radius of the sheet and was propagating circumferentially. A flat fracture surface through thickness is observed in Fig. 12a. Fig. 12b shows the simulation results of the same test. The crack location and propagation are captured by the FE simulation accurately.

Also, considering the bending effects, the integration points located on the top or bottom surfaces are critical. The global strain states of the integration points located at surfaces inside (−) and outside (+) at only one incremental step before fracture initiation are plotted in Fig. 13. The black solid line is the ThyssenKrupp defined FLD based on the Nakajima tensile test results. The method of the specific approximation and definition of the FLC was proposed by Gerlach et al. (2007). The black circles are the experimental necking strains of TRIP 690 provided by ThyssenKrupp. The blue solid line is the MMC-FFLD, which was derived in Section 4.2 and plotted in Fig. 9.

It indicates that the integration point located on the negative surface at the corner of the die radius reaches MMC-FFLD first, shown in Fig. 13a, although, the other critical integration point located on the positive surface at the corner of punch radius is close to the MMC-FFLD too. Fig. 13a indicates that fracture initiation is due to pure shear in the second quadrant.

![](./images/811773817054560256_12.jpg)

Fig. 12. Comparison of the fracture modes of case 1 (a) experiment and (b) simulation.

![](./images/811773817054560256_13.jpg)

![](./images/811773817054560256_14.jpg)

Fig. 14. Comparison of the fracture mode of case 2: (a) experiment and (b) simulation.

It can be seen from Fig. 13 that the MMC-FFLD predicts higher locus than FLC in the range of $-1/2 \leq \alpha \leq 1$, which indicates that for TRIP690, necking occurs before fracture.

### 6.1.2. Case 2: $45^\circ$
Fig. 14a shows the photo of test with a crack located at the punch radius of the sheet and was also propagating circumferentially. A slant fracture mode is observed from Fig. 14a. Fig. 14b shows the simulation results of the same test. The crack location and propagation are captured by the FE simulation accurately, again.

The global strain states and the state of damage indicator on the negative surface and the positive surface right before fracture initiation are shown in Fig. 15a and b, respectively. Different from case 1, the material points on the positive surface at the punch radius satisfied the MMC fracture criteria first. It is need to be noted that although the strain states located at the die radius exceed the MMC-FFLD, the damage indicator is less than 1, which indicate no fracture. This is due to the effect of normal stress illustrated in case 1. In Fig. 15b, the integration points at the punch radius reaches the MMC-FFLD and $D$ reaches 1, indicating crack will initiate there.

### 6.1.3. Comparison
The comparison of the experimental and numerically predicted load-displacement curves of case 1 and case 2 is shown in Fig. 16. The FE simulations capture the fracture locations and fracture punch travels accurately for both cases.

Also, from Figs. 14 and 15 we can conclude that, for case 1, fracture initiates from the surface inside (-) located at the corner of die radius; for case 2, fracture initiates from the surface outside (+) located at the corner of punch radius.

![](./images/811773817054560256_15.jpg)

Fig. 15. Global strain status and the damage indicator (the color represent the value of damage indicator): (a) results at the integration points located at the negative surface and (b) results at the integration points located at the positive surface. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

![](./images/811773817054560256_16.jpg)

Fig. 16. Comparison of the punch force displacement curves between simulation results and experimental data of the square punch test.

### 6.2. Circular punch

The photo of a tested specimen after a circular punch test is shown in Fig. 17a, and it can be seen that the crack locates at the drawn-in edge. The location of crack initiation is captured correctly by the FE simulation, as shown in Fig. 17b. However, as of crack propagation, the crack does not go to the edge if no modification is made to the model, as shown in Fig. 17c. The reason for this unrealistic failure model is that the edge of the sheet is always under uniaxial tension/compression, which has a high fracture strain limit. On the other hand, there is considerable initial damage introduced to the edge during shearing/machining of the blank, and this initial damage causes the crack propagation to the edge. In this study, an engineering approach was used to take the edge damage into account. An initial damage was assigned to the elements at the edge of the sheet. After certain optimization of the initial damage value, a more realistic failure model was obtained, as shown in Fig. 17d. The edge crack during stamping is still a hot and challenging problem, and it is also an ongoing research of the same team, so the detailed procedures will not be given here.

For the circular punch test, the classical J2 isotropic plasticity with a properly calibrated friction coefficient gives good prediction of the load-displacement curve, as shown in Fig. 18. Meanwhile, the crack initiation in the drawn-in area does not cause a sudden force drop in load-displacement response, and thus the crack initiation points in tests and simulation are labeled in Fig. 18. It can be seen that the FE model predicts crack initiation about 12% earlier. This could be explained by certain wrinkling, which was observed around the drawn-in edge area in some tests but not captured by FE simulation.

![](./images/811773817054560256_17.jpg)

Fig. 18. Comparison of the punch force displacement curves between simulation results and experimental data of the circular punch test.

The global strain states and the distribution of damage indicator on the positive surface and the negative surface right before fracture initiation are shown in Fig. 19a and b, respectively. As observed from the simulation, the crack initiates from the drawn-in edge area (Fig. 17), and it starts from the positive side of the sheet. Clearly, Fig. 19 shows that the critical area in this case is experiencing a loading between pure shear and compression $(-2 \leq \alpha \leq -1)$, which is out of the realm of FLC. Consequently, the FLC again cannot predict failure correctly in this case, while the MMC fracture model is able to capture the fracture initiation accurately, as shown by the damage contour.

It is noteworthy that in Fig. 13a, Fig. 15a and Fig. 19a, the strain path already exceeds the MMC-FFLD curve at the last time step before crack initiation, but the damage indicator is still below 1. This is because the MMC fracture envelope (Fig. 7) is not used simply as a strain limit, but as a reference strain value in the damage accumulation rule (Eq. (9)). In a way, this approach takes strain history effect and non-proportional loading into consideration. An example of the strain evolution history of specific spots during deep drawing can be found in Fig. 21, which indicates that

![](./images/811773817054560256_18.jpg)

Fig. 17. Comparison of fracture mode in circular punch test: (a) experiment, (b) simulation of crack initiation, (c) crack propagation without initial edge damage and (d) crack propagation with initial edge damage (color coded is damage indicator D). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

![](./images/811773817054560256_19.jpg)

Fig. 19. Global strain status and the damage indicator contour for circular punch test: (a) results at the integration points located at the positive surface and (b) results at the integration points located at the negative surface.

the critical areas are experiencing complex non-proportional loading.

## 7. Study of fracture mechanism

In this section, several detailed discussions are raised regarding the typical fracture mechanism during a deep-drawing operation. Based on the numerical and experimental results shown in Section 6, the square punch test features more complex strain/stress state, and thus is more typical and representative for a detailed investigation. Therefore, this section will mainly take the case 1 of the square punch test as an example.

### 7.1. Typical strain states of the sheets during forming

Material points at different locations on the sheet have different strain paths during punching. Strain paths of material points at five locations on the blank: point O at the center of the sheet, point 1 at the corner of the punch radius, point 2 on the side wall, point 3 at the corner of die radius, and point 5 at the flange, are studied by FE simulation (see Fig. 20). In FE simulations, five elements are chosen at these five locations to study the loading paths of them. Considering the bending effects, for each element, three integration points are studied and are also shown in Fig. 20, which are located at the mid-plane and the top (+) and bottom (-) surfaces through thickness. 15 integration points in total were traced during the punching process in simulation. The loading paths of them are shown in Fig. 21.

If the element has only in-plane load, the loading path of the three integration points through thickness should be identical, otherwise, it is in bending to some extend. Element O experiences purely equi-biaxial tension and the strains of three integration points are identical and are very small. Element 1 at the corner of punch radius is under a combined biaxial tension and bending. Although the loading paths of its three integration points are all located in the first quadrant, the strain on the outside surface is more critical to fracture than that on the surface contacting with the punch (the solid line has more extensive strains then the dash line). Element 2 on the side wall is always in plane-strain condition with zero strain in the circumferential direction. Element 3 at the die radius experiences a combined bending and in-plane shear. The loading paths of all integration points are located in the second quadrant between uniaxial tension and uniaxial compression and the load path of the mid-surface is very close to the proportional loading of pure shear. The surface inside contacting with the punch is more critical than the surface outside (the solid line has more extensive strains than the dash line). Element 4 at the flange of the sheet is in the state of uniaxial compression initially, and bending develops later. Element 1 and 3 experience substantial bending and the critical points are on the convex surfaces of the deformed sheet at both locations.

Also, the loading paths of the two critical points are not strictly proportional, there are some history effects. For example, the material located at the convex surface of element 1 (blue solid line) is in equi-biaxial tension and plane-strain alternately; the material point at the convex surface of element 3 (red dash line) is in uniaxial tension first and then shift to pure shear. Elements 1, 2 and 3 are competing for reaching the fracture locus first. Their competition result determines the fracture location of the sheet during punching.

The histories of thinning at all typical points are shown in Fig. 22. It can be seen that all other points experience continuing thickening or thinning except the critical point 3 with a shear-induced fracture

![](./images/811773817054560256_20.jpg)

Fig. 20. Sketch of the five locations and the corresponding three integration points studied at each location (the color of the contour is the thickness distribution of the sheet, red-blue: thick-thin). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

![](./images/811773817054560256_21.jpg)

Fig. 21. Strain paths of 15 integration points through the thickness of the five typical elements from the FE simulation of case 1 (the colors of the curves are consistent with those at various locations in Fig. 20): solid lines represent the integration point on the top-surface (+), dash lines represent the integration point on the bottom-surface (-), dash-point lines represent the integration point on the mid-surface.

![](./images/811773817054560256_22.jpg)

Fig. 22. Thinning/thickening histories of five typical elements at different location.

![](./images/811773817054560256_23.jpg)

Fig. 23. Comparison of the influence of different element deletion law on the load-displacement curve in the simulation.

initiation. Point 3 is thickened first and then is thinned, indicating a transformation from a compression dominant strain state to a tension dominant state through pure shear.

### 7.2. Through thickness fracture

Fracture through thickness is simulated by applying the frac- ture criterion at all integration points through the thickness. Fig. 23 shows that the predicted fracture is pre-mature when 1-point ele- ment deletion law¹ is used. This pre-mature fracture was also observed by Alsos et al. (2009), in which, they reported that when using Hill-Bressan-Williams criterion and 1-point element dele- tion law to simulate the 'giant bulge' test of both circular and elliptic plate and die, the predicted fracture are both much earlier than the experimental results. Actually, for models of FLC based on bifurca- tion and stability analysis, only 1-point element deletion law (Alsos et al., 2008) is applicable on the membrane surface. 5-Point ele- ment deletion law² is able to capture the crack propagation through thickness due to bending and avoids the pre-mature fracture, as shown in Fig. 23.

Various numbers of Simpson integration points (5, 9 and 21) through thickness are used to obtain convergent results. Fig. 24 shows that the choice of 5 integration points through thickness is accurate enough to represent the convergent result.

As mentioned before, when $D=1$, the fracture initiates. The dele- tion of the first element indicates the fracture initiation and the position of this element indicates the location of the crack. Fig. 25 shows the damage evolution of three integration points through the thickness of the element at point 3 during punching. The dif- ference of these curves is attributed to bending effect. At the same punch travel, the order of the damage indicator at the three integra- tion points through the thickness is that the damage on the negative surface (the inside surface contacting with the punch) is larger than the damage on the mid-surface and both are larger than the damage on the positive surface (outside), indicating that the surface inside is more critical and crack initiates there and propagates to outside surface through the thickness, although the propagation process can be very rapid, shown in Fig. 25.

![](./images/811773817054560256_24.jpg)

Fig. 24. Convergence study of the number of Simpson integration points through the thickness of shell elements.

### 7.3. Competition between biaxial tension and in-plane shear fracture

The main difference between case1 and case 2 is the orientation of the sheet corresponding to the punch, as shown in Fig. 4. It was shown before that this difference causes different fracture locations for the two cases. Fig. 16 shows that the fracture occurs at a smaller punch travel and a higher punching force for case 2.

Another difference of the two cases is that the fracture surface is flat for case1, while the fracture surface of case 2 is slant. The fracture mode through thickness is not able to be captured by shell element model visually, but this phenomenon can be captured by 3D solid element model with several elements through thickness using the same approach, which is shown by Li et al. (submitted for publication) in studying the crack propagation of combined Mode I and III loading. Also slant fracture of the plane-strain specimen was predicted by using 2D plane-strain model through thickness (Li and Wierzbicki, 2010). In this study, this phenomenon of flat vs. slant fracture can be explained analytically using BW criterion

![](./images/811773817054560256_25.jpg)

Fig. 25. Evolution of the damage indicators with punch travel of three integration points of the critical element (in the legend, 'Neg.' represents the surface contacting with the punch; 'Pos.' represents the surface outside; 'Mid' represents the middle surface).

---

¹ One-point element deletion law is that when any integration point through thickness of one element reaches the fracture criterion, the element is deleted.
² 5-Point element deletion law is that when all five integration points through thickness reach the fracture criterion, the element is deleted from the model.

![](./images/811773817054560256_26.jpg)

Fig. 26. Global strain status and the color contour of damage indicator at different time steps of the integration points. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

based on the stability analysis, which is illustrated in Section 2. For case1, at the die radius $\alpha \approx -1$, therefore $\theta \approx 0^{\circ}$, which indicates a flat fracture; for case 2, at the punch radius, $\alpha \geq 0$, then $\theta$ is non-zero, indicating a slant fracture, using Eq. (4). Comparing with the BW analysis combined with a maximum shear criterion, the advantage of MMC is that MMC also includes the influence of the hydrostatic stress on fracture.

By taking case 1 as an example, the global strain status of integration points at different punch travels are recorded from the FE simulation in Fig. 26. The global strain status on the neg. surface are always mainly located in the quadrant II, see Fig. 26a, while the global strain status on the pos. surface mainly located in the quadrant I initially, see Fig. 26b ($t=0.5$ s), later, the boundary of global strain status extends towards the FFLD in both quadrants, but the extension in quadrant II is much more rapid. It can be seen from Fig. 26 that from $t=0.65-0.83$ s, the strains in quadrant II develops substantially, while the strains in quadrant I almost stop developing. Eventually, the critical integration point on the negative surface reaches the fracture locus first and the shear-induced crack initiates there. In conclusion, Fig. 26 shows a rotation of strains from quadrant I to quadrant II anti-clockwise and a much more rapid extension of stains in quadrant II with the increasing punch travel.

## 8. Conclusions
The existing models of traditional FLC have no solutions in the second quadrant beyond pure shear and therefore are unable to predict shear failure in this region. The new approach developed in this investigation fills this gap. This approach is validated by experiments of square and cylindrical punch tests with a shear-induced fracture. Study of the square punch test, case 2 shows the current approach is also accurate than FLC in predicting fracture in the first quadrant. The application of MMC fracture criterion to predict fracture limit in the sheet metal forming of ThyssenKrupp TRIP690 steel is shown in this investigation. All experimental observations of square and cylindrical punch tests are captured by this application accurately.

Global strain status of integration points shows that the competition of tensile fracture in quadrant I, the plane-strain fracture and the shear-induced fracture in quadrant II are intense and are very sensitive to the failure criteria during sheet metal forming. The features of failure, such as fracture locations, modes and punch travels all depend on the competition results. It was shown that the traditional approach of FLC is not accurate enough to capture this competition. In order to capture these features, a more advanced fracture model is needed, and the MMC fracture criterion is proved to be an accurate criterion in calibrating the fracture limit of sheet metal forming.

The crack propagation through the thickness of the shell element can be simulated by implementing the MMC fracture criterion at all integration points through the thickness. It is shown that using the approach developed in this study, the crack propagation through thickness due to bending in the punching process, which are not able to be captured by the FLC approach, can be also taken into consideration.

## References
Alsos, H.S., Amdahl, J., Hopperstad, O.S., 2009. On the resistance to penetration of stiffened plates. Part II: Numerical analysis. International Journal of Impact Engineering 36, 875-887.

Alsos, H.S., Hopperstad, O.S., Tornqvist, R., Amdahl, J., 2008. Analytical and numerical analysis of sheet metal instability using a stress based criterion. International Journal of Solids and Structures 45, 2042-2055.

Bai, Y., Wierzbicki, T., 2010. Application of extended Mohr-Coulomb criterion to ductile fracture. International Journal of Fracture 161 (1), 1-20.

Bao, Y., Wierzbicki, T., 2004. On fracture locus in the equivalent strain and stress triaxiality space. International Journal of Mechanical Sciences 46, 81-98.

Beese, A., Luo, M., Li, Y., Bai, Y., Wierzbicki, T., 2010. Partially coupled anisotropic fracture model for aluminum sheets. Engineering Fracture Mechanics 77, 1128-1152.

Bressan, J.D., Williams, J.A., 1983. The use of a shear instability criterion to predict local necking in sheet metal deformation. International Journal of Mechanical Sciences 25, 155-168.

Cao,J., Boyce, M.C., 1997. A predictive tool for delaying wrinkling and tearing failures in sheet metal forming. Transactions of the ASME 119, 354-365.

Gerlach, J., Kessler, L., Paul, U., Rösen, H., 2007. Possibilities and influencing parameters for the early detection of sheet metal failure in press shop operations, Materials Processing and Design; Modeling, Simulation and Applications; NUMI- FORM'07. In: Proceedings of the 9th International Conference on Numerical Methods in Industrial Forming Processes. AIP Conference Proceedings, Volume 908, pp. 99-104.

Goodwin, G.M., 1968. Application of strain analysis to sheet metal forming in the press shop. SAE paper 680093.

Hill, R., 1952. On discontinuous plastic states, with special reference to localized necking in thin sheets. J Mech. Phys. Solids 1, 19-30.

Hooputra, H., Gese, H., Dell, H., Werner, H., 2004. A comprehensive failure model for crashworthiness simulation of Aluminum extrusions. International Journal of Crashworthiness 9 (5), 449-463.

Hudgins, A.W., Matlock, D.K., Speer, J.G., Tyne, C.J., 2010. Predicting instability at die radii in advanced high strength steels. Journal of Material Processing Technology 210,741-750.

Issa, D., 2009. Testing and Prediction of Failure of AHSS Sheets at Die Radius and Sidewall using Novel Fracture Apparatus. Master's Thesis.

Kamoulakos, A., 2002. Numerical simulation of metal rupture - the new PAM 'E-W' rupture model, EuroPAM 2002, Antibes, France.

Keeler, S., Backofen, W., 1963. Plastic instability and fracture in sheets stretched over rigid punches. ASM TRANS Q 56 (1), 25-48.

Kessler, L., Gese, H., Metzmacher, G., Werner, H., 2008. An approach to model sheet failure after onset of localized necking in industrial high strength steel stamping and crash simulations. SAE Technical paper series 2008-01-0503.

Lemoins, X., Kamoulakos, A., 2003. Calibrating and using the EWK rupture model- application on arcelor high strength steel, EuroPAM 2003, Mainz, Germany.

Li, Y., Wierzbicki, T., 2010. Prediction of plane strain fracture of AHSS sheets with post-initiation softening. International Journal of Solids and Structures 47 (17), 2316-2327.

Li, Y., Wierzbicki, T., 2009. Mesh-size study of ductile fracture by non-local plasticity model. Proceeding of SEM Annual Conference and Exposition on Experimental and Applied Mechanics. Paper No. 387, Albuquerque, June 2009.

Li, Y., Wierzbicki, T., Sutton, M., et al., submitted for publication. Mixed mode stable tearing of thin sheet Al6061-T6 specimens: experimental measurements and finite element simulations using a Modified Mohr-Coulomb fracture criterion. International Journal of Fracture.

Luo, M., Wierzbicki, T., 2009. Ductile fracture calibration and validation of anisotropic aluminum sheets. In: Proceedings of 2009 SEM Annual Conference and Exposition on Experimental and Applied Mechanics, Albuquerque, NM, pp. 402-413.

Luo, M., Wierzbicki, T., in press. Numerical failure analysis of a stretch-bending test on dual-phase steel sheets using a phenomenological fracture model. Interna- tional Journal of Solid and Structures.

Masarczyk, P.P., Struppek, T., 2003. Process for the determination of the friction properties of sheet metal during forming and the measuring apparatus for carrying out the process, United States Patent, No. US6,591,659 B1.

Pickett, A., Pyttel, T., Payen, F., Lauro, F., Petrinic, N., Werner, H., Christlein, J., 2004. Failure prediction for advanced crashworthiness of transportation vehicles. International Journal of Impact Engineering 30, 853-872.

Storen, S., Rice, J.R., 1975. Localized necking in thin sheets. Journal of the Mechanics and Physics of Solids 23 (6), 421-441.

Stoughton, T.B., Zhu, X., 2004. Review of theoretical models of the strain-based FLD and their relevance to the stress-based fld. International Journal of Plasticity 20, 1463-1486.

Taylor, L., Cao, J., Karafillis, A.P., Boyce, M.C., 1995. Numerical simulations of sheet- metal forming. Journal of Materials Processing Technology 50, 168-179.

Wierzbicki, T., Xue, L., 2005. On the effect of the third invariant of the stress deviator on ductile fracture. Technical report. Impact and Crashworthiness Laboratory. Massachusetts Institute of Technology, Cambridge, MA.

Xue, L., 2007. Damage accumulation and fracture initiation in uncracked ductile solids subject to triaxial loading. International Journal of Solids and Structures 44,5163-5181.

Zeng, D., Xia, Z., Shih, H., Shi, M., 2009. Development of shear fracture criterion for dual-phase steel stamping. In: SAE2009 World Congress. 2009-01-1172, Detroit, MI.