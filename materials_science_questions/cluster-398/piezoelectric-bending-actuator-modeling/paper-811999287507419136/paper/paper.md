# A Computational Method for Materials Selection in a Hybrid Actuation System

Benjamin J. Nickless$^{\mathrm{a}}$, Ji Su$^{\mathrm{b}}$, Tian-Bing Xu$^{\mathrm{c}}$, James E. Hubbard Jr.$^{\mathrm{a}}$

$^{\mathrm{a}}$University of Maryland, 3181 Glenn L. Martin Hall, College Park, MD, 20742
$^{\mathrm{b}}$NASA-Langley Research Center, Hampton, VA, 23681
$^{\mathrm{c}}$National Institute of Aerospace, 100 Exploration Way, Hampton, VA, 23666

## ABSTRACT

Researchers at NASA-LaRC have developed a hybrid actuation system (HYBAS) that cooperatively employs an electroactive polymer and an electrostrictive single crystal. Experimental measurements and theoretical model predictions have been in good agreement thus far. To date, current research has only explored the usage of one electroactive polymer and one electrostrictive single crystal. A computational model was created based on this theoretical model. It implements the equations necessary to predict the actuator displacement profile and maximum displacement. Among the model variables are the actuator material properties. Changing the actuator materials has notable effects on actuator performance. As many viable materials as could be found were compiled into a database which can serve as a building block upon which a larger database can be built. Using these materials, a trade study was performed to determine which combination of materials demonstrates the best performance. As more electroactive materials are compiled, more extensive trade studies can be performed. Thus, the work in this paper will serve as a guideline for future HYBAS designs.

**Keywords:** hybrid actuation system (HYBAS), electroactive polymer (EAP), electrostrictive single crystal (ESC), piezoelectric materials, smart materials

## 1. INTRODUCTION

A growing trend in micro- and nano-technology and multifunctional materials has caused designers to look towards smart materials for use in actuators because of their dimensional versatility, mechanical simplicity, and high energy density. These are all very desirable qualities, but the pursuit of actuation design is to obtain large actuation force and high displacement without requiring a relatively high operating voltage or current. However, actuators made from smart materials are usually found wanting in at least one of these three categories. Despite the shortcomings, a great effort has been made to amplify their displacement, increase their actuation force, and enhance their overall efficiency. Among the first and most popular resulting developments are the multilayer stacks and bimorphs. Newnham et al later introduced the ceramic metal composite actuator. Many devices aimed at amplifying displacement have followed$^{1-6}$.

Su et al at NASA-Langley Research Center have conceptualized and fabricated one such device$^{6}$. This hybrid actuation system, known as HYBAS, harmoniously employs two electroactive components in order to achieve enhanced electromechanical performance and efficiency. The HYBAS is currently in the prototype design stage. Different dimensional and geometric combinations have been tested in search of optimal performance. The two types of materials utilized are an electroactive polymer (EAP) and an electrostrictive single crystal (ESC). Only one of each type of these materials has been exploited to date. The material employed for the EAP component is uni-axially stretched and high energy electron irradiated 68/32 mol.% poly(vinylidene-fluoride-trifluoroethylene) copolymer (PVDF-TrFE), and for the ESC component is lead zinc niobate-lead titanate (PZN-PT single crystal). A proposed theoretical model has also been put forth and compared to experimental data$^{6}$. Thus far, theoretical and experimental results have been in good agreement.

Sensors and Smart Structures Technologies for Civil, Mechanical, and Aerospace Systems 2007,
edited by Masayoshi Tomizuka, Chung-Bang Yun, Victor Giurgiutiu, Proc. of SPIE Vol. 6529,
652909, (2007) · 0277-786X/07/$18 · doi: 10.1117/12.715431

Proc. of SPIE Vol. 6529 652909-1

There are many materials that exhibit an electric-field induced strain, yet no significant database of such materials exists. Using a computational version of the theoretical model of HYBAS by Xu et al⁷, shape profile and maximum displacement results can be obtained. The computational model allows changes to be made to design parameters, including material properties. After refining the computational model, its predictions were compared to those of the theoretical model to assess the correctness and accuracy of both models. After arriving at a sufficiently accurate computational model, a trade study regarding materials was conducted using a database of materials gathered by the authors. All other design parameters were held constant. The HYBAS models, both theoretical and computational, and their similarities and differences will be addressed in this paper. Comparative results of the trade study will follow.

## 2. THE CURRENT HYBAS ACTUATOR

The HYBAS has two active components and three inactive components. Active components consist of the ESC and the active EAP layer. Inactive components are comprised of electrodes, a plastic frame, and an inactive EAP layer. A diagram of the HYBAS illustrating its relative geometric layout and different components is shown in Fig. 1.

![](./images/811999287507419136_1.jpg)

Fig. 1. Schematic of the HYBAS identifying its components⁶.

Fabrication of a HYBAS begins with the ESC component. The upper and lower surfaces are coated with gold electrodes. The frame consists of two sections of plastic bar or rod, which are bonded to each end of the ESC component respectively. A frame is necessary in order to couple the ESC element and the EAP element in order to take advantage of both of their desired qualities. After coating the active EAP layer with gold electrodes, an inactive EAP layer of the same polymer is bonded to it forming the complete EAP component. The complete EAP component is then bonded to the top edges of each side of the plastic frame as shown in Fig. 1.

The PZN-PT single crystal used in the original and other possible materials for application in the ESC element are typically ceramic or exhibit ceramic-like properties. They are moderately stiff and do not tolerate large bending displacement. Electroactive polymers, including the PVDF used in the original, are usually less stiff compared to the single crystal materials. They also are able to tolerate large bending displacements without adverse effects. The ESC materials experience a dimensional decrease with applied electric field while the EAP materials experience a dimensional increase in their respective length directions perpendicular to the applied field.

The HYBAS was designed with careful consideration in order to take advantage of all the aforementioned properties of both material types. Electrically activating either or both components creates a moment in both components. The ESC element is made sufficiently stiffer than the EAP element (higher Elastic modulus and larger cross-sectional area than the EAP) so that the ESC remains planar. As a result, the EAP will buckle when either or both elements are activated. This is known as flextensional actuation and offers increased displacement compared to traditional piezostack actuators²⁻⁴,⁸. This creates an actuator displacement profile in the HYBAS shown in Fig. 2.

Initially the EAP is planar and parallel to the ESC. The moment created by either the ESC contracting or the EAP elongating could cause the EAP to buckle in either the positive or negative z-direction. However, only displacement in the positive z-direction is desired. The inactive EAP layer serves this purpose. It is employed to bias the EAP element so that it will always buckle and displace in the positive Z-direction⁶⁻⁷,⁹. The inactive EAP layer is the same PVDF copolymer as the active EAP layer.

Proc. of SPIE Vol. 6529 652909-2

![](./images/811999287507419136_2.jpg)

Fig. 2. Actuation response, displacement is in the z-direction⁹.

### 3. THEORETICAL MODEL

The HYBAS was modeled as a rectangular beam fixed at both ends subjected to a uniformly distributed load in the Z- direction⁷. The ESC component realizes displacement in the x-direction only and is much stiffer than the EAP component as mentioned before. As such it defines the dynamic length $L_d$ of the actuator which is given by

$$
L_d = L_0\left(1+s_{ESC}^e\right) \tag{1}
$$

where $L_0$ is the initial length of the ESC when the applied electric field is zero and $s_{ESC}^e$ is the effective electrostrictive strain in the ESC which is a function of the applied electric field⁷. The change in length exerts a contractive force on the EAP element. The contractive force causes the EAP element to buckle. This coupled with the effects of the inactive EAP layer induce a uniformly distributed load on the EAP element. The displacement in the z-direction of such a beam is given by

$$
w(x)=\frac{p}{24EI}\left[\left(\frac{L_d}{2}\right)^2 - x^2\right]^2 = c\left[\left(\frac{L_d}{2}\right)^2 - x^2\right]^2 \tag{2}
$$

where $E$ and $I$ are the Young's modulus and moment of inertia of the EAP element, respectively, and $p$ is the uniformly distributed load per unit length, which is dependent on the strain in both the EAP and ESC elements¹⁰. Equation (2) differs from that which appears in the reference in that it has been shifted so that $x=0$ is at the center of the beam. By using standard extrema finding techniques the maximum displacement is found to occur at the center of the beam and is given by

$$
w_{\text{max}} = \frac{cL_d^4}{16}. \tag{3}
$$

It is obvious from Eqs. (2) and (3) that the parameter $c = p/24EI$ plays an important role in the magnitude of the actuation response. The uniformly distributed load $p$, and thus $c$, is dependent on the strains in both the EAP and the ESC components⁷. To obtain a value for $c$ necessitates considering the calculation of the total length of the EAP element in its displaced form. The total length can be expressed in two manners, and both must be equal, yielding

$$
\int_{-L_d/2}^{L_d/2} \sqrt{\left(\frac{dw}{dx}\right)^2 + \left(\frac{dx}{dx}\right)^2} dx = L_0\left(1 + s_{EAP}^e\right). \tag{4}
$$

Proc. of SPIE Vol. 6529 652909-3

Inserting the derivative of Eq. (2) into Eq. (4) yields

$$
\int_{-L_{d} / 2}^{L_{d} / 2} \sqrt{c^{2}\left(4 x^{3}-L_{d}^{2} x\right)^{2}+1} \quad d x=L_{0}\left(1+s_{E A P}^{e}\right)
\tag{5}
$$

in which $s_{E A P}^{e}$ is the effective strain in the EAP component. A value for $c$ can be obtained using Eq. (5). The left-hand side of Eq. (5) cannot be evaluated using analytical techniques. It requires numerical integration to calculate which implies guessing at a value for $c$ until Eq. (5) is satisfied. Once $c$ is obtained, it can be substituted into Eqs. (2) and (3) to obtain predictions for the displacement profile and maximum value.

In turn, the right-hand side of Eq. (5), and thus $s_{E A P}^{e}$, must also be evaluated in order to get a value for $c$. The ESC component contains only active layers, whereas the EAP component contains an inactive layer that constrains its motion in both the $X$- and $Z$-directions. As such $s_{E A P}^{e}$ is affected by these factors and is less than but related to the free strain of the EAP component. Xu et al considered these effects when deriving the theoretical model of the HYBAS and found the relationship between the free strain $s_{0}$ and effective strain in this case to be $^{7}$

$$
s_{E A P}^{e}=\frac{s_{0}}{1+k}
\tag{6}
$$

where $k$ is the ratio of inactive layer stiffness to active layer stiffness and is referred to as the clamping ratio. It can be expressed as $^{9}$

$$
k=\frac{\sum_{i=1}^{q}\left(E_{n} t_{n} b_{n}\right)_{i}}{E_{a} t_{a} b_{a}}
\tag{7}
$$

where the subscript $a$ denotes active layers, the subscript $n$ denotes inactive layers, and $q$ denotes the total number of inactive layers that are to be include in the calculation of $k$. Included in the calculation of $k$ in the theoretical model are the inactive EAP layer, the epoxy layer bonding the inactive and active layers, both of the gold electrodes, and the margins of the active layer not covered by electrodes $^{7}$. The geometric and pertinent material properties used in the theoretical model are shown in Table 1.

Table 1. Dimensions and necessary material properties used in the theoretical model.

<table>
  <thead>
    <tr>
      <th rowspan="2">Component</th>
      <th rowspan="2">Effective Length (mm)</th>
      <th rowspan="2">Thickness, t (µm)</th>
      <th colspan="2">Width, b (mm)</th>
      <th rowspan="2">Young's Modulus (GPa)</th>
    </tr>
    <tr>
      <th>Total</th>
      <th>Effective</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ESC</td>
      <td>5.50</td>
      <td>470.0</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>20.0</td>
    </tr>
    <tr>
      <td>Active EAP layer</td>
      <td>5.50</td>
      <td>16.0</td>
      <td>4.50</td>
      <td>3.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>Inactive EAP layer</td>
      <td>5.50</td>
      <td>15.0</td>
      <td>4.50</td>
      <td>4.50</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>epoxy layer</td>
      <td>5.50</td>
      <td>1.0</td>
      <td>4.50</td>
      <td>4.50</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>gold electrodes on EAP</td>
      <td>5.50</td>
      <td>0.1</td>
      <td>3.00</td>
      <td>3.00</td>
      <td>74.0</td>
    </tr>
    <tr>
      <td>unelectroded margins</td>
      <td>5.50</td>
      <td>16.0</td>
      <td>0.75</td>
      <td>0.75</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

### 4. COMPUTATIONAL MODEL

The computational model is largely based on the theoretical model described above. All of the previous equations are implemented, although some assumptions had to be made in order to make their implementation possible. Before going any further it is necessary to redefine the nomenclature of components of HYBAS. Thus far the PZN-PT single crystal has been referred to simply as the ESC (electrostrictive single crystal) component. Electrostrictive suggests a particular strain vs. electric field relationship and single crystal refers to a material whose formation is tightly controlled so that all of the crystals form in a particular orientation. It is not likely that all of the materials used in the trade study will exhibit this particular relationship or have this particular crystal structure. For the HYBAS to function properly, the material performing the function of the ESC component must contract when an electric field is applied, and the material functioning as the EAP component must elongate when an electric field is applied. So from this point forward the ESC component will be referred to as the negative strain component and the EAP component will be referred to as the positive strain component.

The response to an applied electric field is assumed to be piezoelectric for all materials included in the study. This implies that the relationship between free strain and the applied electric field is linear and the slope is the piezoelectric constant of the material. As noted in the previous section, the effective strain in the positive strain component is different from its free strain. The effective strain of the negative strain component, however, is comparable to its free strain⁷. As such, the effective strain in the negative strain component is estimated as being equal to its free strain, thus no clamping ration is calculated for it. A piezoelectric material typically has many piezoelectric constants depending on the applied electric field direction and the output direction being examined. In this case the applied field is in the Z-direction and the working displacement direction is the X-direction. So, only the $d_{31}$ piezoelectric constant for each active material is needed here. The free strain will be given by

$$
s^{f}=d_{31} \frac{V}{t} \tag{8}
$$

where $V$ is the applied voltage and $t$ is the material thickness. The quantity $V/t$ is the applied electric field. Under the prior assumptions, the negative strain component effective strain will be given by Eq. (8) with appropriate parameters embedded. The positive strain component effective strain will still be given by Eq. (6), but with the free strain $s_0$ given by Eq. (8) with the appropriate parameters being used.

The main goal of the computational model is to be able to compute Eqs (2) and (3) using different material properties in order to compare different HYBAS configurations. The inherent problem previously mentioned in calculating these two equations is obtaining a value for the parameter $c$. Obtaining this value requires finding that which satisfies Eq. (5). Once the properties of the desired material are supplied, an initial guess for the value of $c$ must be made by the program user. The left-hand side of Eq. (5) is then numerically integrated with this value of $c$ using a left-hand Riemann sum algorithm with 1000 subintervals. After this computation is finished, the value is compared to the value computed for the right-hand side of Eq. (5). If the desired accuracy of this comparison is met, this value of $c$ is kept and the computation is complete. If the accuracy condition is not satisfied, the program will change the value of $c$ as necessary and repeat the process. Iteration upon $c$ continues until the desired accuracy is achieved. Here, accuracy refers to the equality of Eq. (5), not the accuracy of the numerical integration itself. Exact equality of Eq. (5) cannot be expected as numerical integration is involved, so the value of $c$ is sought that makes Eq. (5) as true as desired by asking for a certain level of accuracy (i.e. specifying a higher accuracy forces equality to more decimal places).

The values obtained for $c$ are where the computational model shows the largest amount of deviation from the values obtained by Xu et al for the original HYBAS configuration. Table 2 gives a comparison between the two models in this respect. Percent error refers to the accuracy described earlier and represents the amount of difference between the left- and right-hand sides of Eq. (5), that is to say, the error in the true value of $c$. The values reported for $c$ under the theoretical model appear in Ref. [7], but their associated percent errors were calculated later, during the writing of this paper.

It can be seen from Table 2 that the percent error in the theoretical model never drops below 0.0066%, and that by virtue of the algorithm the percent error with the computational model is consistently less than 0.001%. Thus, under the given assumptions, the values for $c$ found by the computational model are more accurate in all cases. But in spite of its accuracy deficiencies the theoretical model shows remarkable correlation with experimentally measured data⁷. While it is safe to say that the theoretical model is superior in displacement prediction for the original HYBAS configuration, the same cannot be said for the general case. While the computational model does not match the experimental data for the original HYBAS as well as the theoretical model, it implements a fundamentally sound and reliable algorithm for HYBAS performance prediction and can be applied with various HYBAS configurations. The inconsistency with the original experimental is inconsequential because the same algorithm will be applied to each configuration. As all the results will be subject to the same influences they will be sufficient for comparison.

Table 2. Comparison of theoretical and computational model regarding values computed for $c$.

<table>
    <thead>
        <tr>
            <th rowspan="2">Voltage (V<sub>RMS</sub>)</th>
            <th rowspan="2">Active Elements</th>
            <th colspan="2">Theoretical Model</th>
            <th colspan="2">Computational Model</th>
        </tr>
        <tr>
            <th>$c$ ($10^6$ m⁻³)</th>
            <th>percent error (%)</th>
            <th>$c$ ($10^6$ m⁻³)</th>
            <th>percent error (%)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>200</td>
            <td>EAP</td>
            <td>0.1786</td>
            <td>0.0066</td>
            <td>0.5591</td>
            <td rowspan="6">accuracy set so iteration stops when percent error is less than 0.001%<br><br>default starting point for $c$ in all cases is 1.000</td>
        </tr>
        <tr>
            <td></td>
            <td>ESC</td>
            <td>0.3774</td>
            <td>0.0384</td>
            <td>1.2579</td>
        </tr>
        <tr>
            <td></td>
            <td>HYBAS</td>
            <td>0.5714</td>
            <td>0.0409</td>
            <td>1.3692</td>
        </tr>
        <tr>
            <td>400</td>
            <td>EAP</td>
            <td>1.3158</td>
            <td>0.0308</td>
            <td>0.7667</td>
        </tr>
        <tr>
            <td></td>
            <td>ESC</td>
            <td>1.0000</td>
            <td>0.0580</td>
            <td>1.7924</td>
        </tr>
        <tr>
            <td></td>
            <td>HYBAS</td>
            <td>2.0964</td>
            <td>0.0160</td>
            <td>1.9510</td>
        </tr>
        <tr>
            <td>800</td>
            <td>EAP</td>
            <td>3.3340</td>
            <td>0.2627</td>
            <td>1.0511</td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td>ESC</td>
            <td>1.2500</td>
            <td>0.1278</td>
            <td>2.5540</td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td>HYBAS</td>
            <td>3.8910</td>
            <td>0.1951</td>
            <td>2.7523</td>
            <td></td>
        </tr>
        <tr>
            <td>1600</td>
            <td>EAP</td>
            <td>5.5866</td>
            <td>0.7582</td>
            <td>1.4978</td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td>ESC</td>
            <td>3.2250</td>
            <td>0.0697</td>
            <td>3.6392</td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td>HYBAS</td>
            <td>6.5876</td>
            <td>0.7117</td>
            <td>3.9138</td>
            <td></td>
        </tr>
    </tbody>
</table>

The materials that were used in the trade study along with their constants are shown in Table 3 which comprises the list of materials that was gathered and whose material constants could be considered reliable. While the list is not long, it provides a sufficient database for the current research and a building block upon which to augment for future purposes.

Table 3. Materials and their properties used in HYBAS trade study¹¹⁻¹³.

<table>
    <thead>
        <tr>
            <th colspan="2">Material</th>
            <th>$d_{31}$ (pC/N)</th>
            <th>dielectric strength or positive depoling field (kV/cm)</th>
            <th>Elastic Modulus (GPa)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">negative strain components</td>
            <td>Hard PZT (TRS100HD)</td>
            <td>-150</td>
            <td>20-50</td>
            <td>79</td>
        </tr>
        <tr>
            <td>Soft PZT (TRSHK1HD)</td>
            <td>-360</td>
            <td>20-50</td>
            <td>67</td>
        </tr>
        <tr>
            <td>PZN-4.5%PT single crystal</td>
            <td>-970</td>
            <td>20-50</td>
            <td>12</td>
        </tr>
        <tr>
            <td rowspan="2">positive strain components</td>
            <td>Uni-axial PVDF</td>
            <td>20</td>
            <td>1600</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Bi-axial PVDF</td>
            <td>8</td>
            <td>1600</td>
            <td>2</td>
        </tr>
    </tbody>
</table>

The positive depoling fields for the negative strain component materials are applicable only to positive applied electric fields. The negative depoling field, or the coercive field, applies to negative applied fields and are typically lower than the positive depoling fields. For this reason, the program assumes a DC bias is applied so that the minimum of the applied AC field is zero and so that higher voltages can be applied.

Proc. of SPIE Vol. 6529 652909-6

## 5. RESULTS

All viable combinations of materials in Table 3 were simulated at 100 $\text{V}_\text{RMS}$ and 650 $\text{V}_\text{RMS}$. These two voltages were chosen based on the electric field capability of the materials. When working with electroactive materials, their dielectric strength or depoling field must be considered. If a material does in fact have such properties, the material will fail if this electric field is exceeded. Thus any results from simulations above this electric field would be erroneous. As the results of this study are intended to be comparative, the applied voltages (and thus applied electric fields due to fixed geometry) need to be the same for each material combination. Given the thickness of both negative and positive strain components and the dielectric strength and field properties in Table 3, the peak voltage that can be applied during this study is 940 V, which mandates 665 $\text{V}_\text{RMS}$. This is governed by the negative strain components. In spite of their larger thickness, their depoling field is much lower than the positive strain component materials. Since the limit is 665 $\text{V}_\text{RMS}$, 650 $\text{V}_\text{RMS}$ is chosen for simulation to avoid virtual material destruction. As for the lower limit, 100 $\text{V}_\text{RMS}$ is chosen arbitrarily. The true lower limit would obviously be 0 $\text{V}_\text{RMS}$, but since that is the trivial case, it is not considered.

Either one or both of the active components can be electrically activated at any given time. Figures 3 shows the displacement profiles of the fully active HYBAS (both components are active) at 100 $\text{V}_\text{RMS}$. The HYBAS displacement profiles at 650 $\text{V}_\text{RMS}$ are presented in Fig. 4. It can be gathered from Figs. 3-4 that with the present set of materials, there are more gains to be had by varying the negative strain component material. There is not a significant difference in piezoelectric constant of the two positive strain component materials as compared to the negative strain component materials. Additionally, the piezoelectric constant of the negative strain component materials are an order of magnitude higher than those of the positive strain component materials. The implications are that the displacement gains from varying the positive strain component material are miniscule as compared to varying negative strain component. Figures 3-4 illustrate this point well when comparing plots in the first column with plots in the second column.

![](./images/811999287507419136_3.jpg)

Fig. 3. Displacement profiles with both components active at $\text{V}_\text{RMS}$ = 100 V. (a) PZN-PT single crystal and uni-axial PVDF, (b) Soft PZT and uni-axial PVDF, (c) Hard PZT and uni-axial PVDF, (d) PZN-PT single crystal and bi-axial PVDF, (e) Soft PZT and bi-axial PVDF, and (f) Hard PZT and bi-axial PVDF.

Proc. of SPIE Vol. 6529 652909-7

![](./images/811999287507419136_4.jpg)

Fig. 4. Displacement profiles with both components active at $V_{\text{RMS}} = 650$ V. (a) PZN-PT single crystal and uni-axial PVDF, (b) Soft PZT and uni-axial PVDF, (c) Hard PZT and uni-axial PVDF, (d) PZN-PT single crystal and bi-axial PVDF, (e) Soft PZT and bi-axial PVDF, and (f) Hard PZT and bi-axial PVDF.

![](./images/811999287507419136_5.jpg)

Fig. 5. Displacement profiles with only the ESC component active at $V_{\text{RMS}} = 100$ and $650$ V.

Proc. of SPIE Vol. 6529 652909-8

Figure 5 shows the displacement profiles at 100 and 650 $V_{\text{RMS}}$ with just the ESC component active, and Fig. 6 shows the profiles with just the EAP component active at the same voltages. Figures 5-6 reassert the conclusions drawn from Figs. 3-4 that varying the negative strain component has more impact on displacement than varying the positive strain component.

![](./images/811999287507419136_6.jpg)

Fig. 6. Displacement profiles with only the EAP component active at $V_{\text{RMS}} = 100$ and 650 V.

Displacement as a function of applied RMS voltage for all viable material combinations with both components active is shown in Fig. 7. It is obvious from Fig. 7 that the best combination of materials for achieving maximum displacement is PZN-PT single crystal and uni-axial PVDF. These materials have the highest piezoelectric constants in the negative and positive strain component groups respectively. If achieving maximum displacement is the only goal, then the materials with the highest absolute value of piezoelectric (or electrostrictive, etc.) constants will always be best suited for the application.

![](./images/811999287507419136_7.jpg)

Fig. 7. Displacement vs. RMS Voltage for all material combinations, both components active.

## 6. CONCLUSIONS AND FUTURE WORK

A computational model was created based on an actuator concept developed by researchers at NASA-Langley Research Center. The model was developed such that design parameters could be altered thus facilitating trade studies to be performed. The underlying purpose of this paper was to use this model to explore the usage of different materials via such a trade study. A theoretical model of the device was the foundation on which the computational model was built. Subtle differences, however, between the theoretical and computational models existed in the form of some necessary assumptions and the manner in which some of the parameters are calculated. After comparing predictions of the two models and careful consideration of how the assumptions might affect said predictions, the computational model was deemed reliable and the trade study was carried out. The ensuing results showed the most suitable material combination was PZN-PT single crystal and uni-axially stretched PVDF.

As mentioned before, this material combination is superior because its constituents have the highest piezoelectric constants in their respective categories of positive and negative strain components and displacement is the only performance parameter being considered here. And while this conclusion may have been obvious from the beginning, maximum displacement is not always the only goal. Even when it is one of many goals, it may not always be the most important. This work serves as a building block for further HYBAS design refinement. Future work should implement more parameters used to select the best material for the application. Parameters such as material cost and availability, fatigue limit and cycles until failure, and electrical power consumption could be included. Further considerations may also involve not only maximum displacement but displacement resolution as well. All of these parameters, including maximum displacement, are application dependent. If the HYBAS is to be tailored to an application as intended, then many of these factors need to be included.

Proc. of SPIE Vol. 6529 652909-10

### 7. ACKNOWLEDGMENTS

This work was supported by NASA SBIR, NASA Langley Research Center's Aeronautics Program, the Education Program of the National Institute of Aerospace, and the University of Maryland. The authors would like to thank the University of Maryland, NASA-Langley Research Center, and the National Institute of Aerospace for making this research possible. Also, the authors would like to thank the Morpheus Laboratory for their ongoing support and motivation.

### REFERENCES

1.  K. Uchino, *Ferroelectric Devices*, Marcel Dekker, Inc., New York, 2000.
2.  K. Uchino, *Piezoelectric Actuators and Ultrasonic Motors*, Kluwer Academic Publishers, Boston, 1997.
3.  R.E. Newnham, A. Dogan, Q. C. Xu, K. Onitsuka, J. Tressler, S. Yoshikawa, "Flextensional Moonie Actuators," *1993 Ultrasonics Symposium*, IEEE, 509-513.
4.  C. Niezrecki, D. Brei, S. Balakrishnan, A. Moskalik, "Piezoelectric Actuation: State of the Art," *The Shock and Vibration Digest*, **33**, No. 4, July 2001, 269-280.
5.  I. Chopra, "Review of State of Art of Smart Structures and Integrated Systems," *AIAA Journal*, **40**, No. 11, November 2002, 2145-2187.
6.  J. Su, T. B. Xu, S. Zhang, T. R. Shrout, Q. Zhang, "An electroactive polymer-ceramic hybrid actuation system for enhanced electromechanical performance," *Applied Physics Letters*, **86**, No. 6, August 2004.
7.  T. B. Xu, J. Su, "Theoretical modeling of electroactive polymer-ceramic hybrid actuation systems," *Journal of Applied Physics*, **97**, 2005.
8.  R. J. Meyer, Jr., A. Dogan, C. Yoon, S. M. Pilgrim, R. E. Newnham, "Displacement amplification of electroactive materials using the cymbal flextensional transducer," *Sensors and Actuators A*, **87**, No. 3, January 2001, pgs. 157-162.
9.  J. Su, T. B. Xu, S. Zhang, T. R. Shrout, Q. Zhang, "A Hybrid Actuation System (HYBAS) and Aerospace Applications," *Materials Research Society Symposium V 2005 Fall Proceedings*, **888**, 2006.
10. R. A. Walsh, *Electromechanical Design Handbook*, Mcgraw-Hill, New York, 2000, p. 5.34.
11. TRS Technologies, Inc., http://www.trstechnologies.com/, accessed on February 16, 2007.
12. Goodfellow Corporation, http://www.goodfellow.com/csp/active/gfHome.csp, accessed on February 16, 2007.
13. W. Hackenberger, TRS Technologies, Inc., private communication, February 22, 2007.