
# On models to describe the volume in the context of establishing high-pressure Gibbs energy databases

Guillaume Deffrennes \( ^{a,*} \) , Jean-Marc Joubert \( ^{b} \) , Benoit Oudot \( ^{a,*} \) 

 \( ^{a} \)  CEA, DAM, VALDUC, F-21120 Is-sur-Tille, France

 \( ^{b} \)  Univ. Paris Est Creteil, CNRS, ICMPE, UMR 7182, 2 rue Henri Dunant, 94320 Thiais, France

* Corresponding authors:

Dr. Guillaume Deffrennes

Present postal address: National Institute for Materials Science, 1-1 Namiki, Tsukuba, Ibaraki

305-0044, Japan

e-mail : guillaume.deffrennes@gmail.com

Dr. Benoit Oudot

Postal address: CEA, DAM, VALDUC, F-21120 Is-sur-Tille, France

e-mail : benoit.oudot@cea.fr

## Keywords

High pressure, Modeling, Volume, CALPHAD, EOS
 

## Abstract

High-pressure Gibbs energy approaches are promising for establishing multi-component thermodynamic databases. However, so far, they have often been considered unsuccessful, because of their tendency to lead to unphysical extrapolations of the thermodynamic properties at elevated temperatures and pressures. Beyond this symptom, the root causes of the problem are rarely investigated. In this work, it is identified that these shortcomings are caused by (i) an inconsistent treatment of the SGTE method of extrapolation, and (ii) an insufficient knowledge of the models to describe the volume that are the key to extend CALPHAD databases toward high pressures. Because the first step toward solving the problem is to focus on the later issue, several models to describe the volume that are built upon the Grover empirical law are investigated, namely, the Lu-Grover, Joubert-Lu-Grover, Jacobs-Grover, and the Anand-Saxena-Grover approaches. In addition, an original description built upon the concept of thermal pressure, and a new scheme based on the equivalence between temperature and pressure when computing the volume are discussed. For each of these models, limitations and possibilities are identified from a practical standpoint.
 

## 1. Introduction

There is a strong interest in the establishment of multi-component thermodynamic databases valid up to high temperatures and pressures for applications not only in geophysics, but also in metallurgy  \( [1-5] \) . To achieve this purpose, there are two main ways. On the one hand, the approaches that rely on the modeling of the Helmholtz energy as a function of temperature and volume  \( [6-8] \)  naturally relate to ab initio calculations. The models are built based on physical considerations, and simplifying assumptions. They allow to achieve reasonable descriptions up to extreme conditions of temperature and pressure for stoichiometric phases, but their application to the modeling of solution phases in multi-component systems have been limited  \( [8] \) . They will not be further considered in the present study. On the other hand, the approaches that rely on the modeling of the Gibbs energy as a function of temperature and pressure naturally relate to experimental work. Therefore, the models tend to be empirical in nature, and phenomenological. They allow to achieve accurate descriptions of complex multi-component systems at atmospheric pressure within the framework of the CALPHAD method, but their extension toward high pressures met only limited success so far. That is because Gibbs energy approaches tend to lead to unphysical extrapolations at high pressure. For instance, a negative heat capacity was calculated in this range for Pt  \( [6] \) , Mo  \( [9] \) , W  \( [10] \) , or Al  \( [11] \) . However, beyond this symptom, the root causes of the problem are rarely investigated. The Gibbs energy can, by definition, be expressed as the sum of two contributions as follows:

 \[ \Delta G(T,p)=\Delta G(T,p^{0})+\int\limits_{p^{0}}^{p}V(T,p^{\prime})d p^{\prime} \quad (1.1) \] 

with  \( \Delta G \)  the Gibbs energy of a phase relative to a given reference state, p the pressure and  \( p^{0} \)  the atmospheric pressure, T the temperature, and V the molar volume. The composition
 

dependence of the Gibbs energy and of the volume falls outside the scope of the present study.

It follows from Eq. (1.1) that the problematic extrapolations obtained at high pressures with Gibbs energy approaches can stem from either the description of the Gibbs energy at atmospheric pressure, or the one of the volume. It was discussed by Brosh et al. [11] that the origin of the problem was due to the so-called SGTE method of extrapolation [12]. Yet, it was recently highlighted that this was not the main cause of these shortcomings, and that the primary problem laid in the description of the volume and related properties [13].

In this work, the problem arising from the SGTE method of extrapolation is first discussed in Section 2. Then, a critical analysis of several models to describe the volume as a function of T and p is proposed. The focus is put on models built upon the empirical relationship discovered by Grover et al. [14] in the early 70s. To begin with, the model provided by Lu et al. [15] is investigated in Section 3. Then, a revised version of this model recently proposed by Joubert et al. [13] is discussed in Section 4. In Section 5, a theoretical analysis of the framework built by Jacobs et al. [16–19] is given. A revision of this Jacobs-Grover model is proposed in subsequent Section 6. Next, a description of the volume based on the Grover empirical law and on the use of thermal pressure is presented in Section 7. This model has the same general behavior as the one proposed by Anand et al. [20] based on the formulation from Saxena [21] of the Grover empirical law. Finally, a new scheme based on the equivalence between temperature and pressure is discussed in Section 8.
 

## 2. The problem arising from the SGTE method of extrapolation

The SGTE method of extrapolation [12], which is commonly used in CALPHAD databases, consists in setting the heat capacity of solids to an arbitrary constant value above their melting point to avoid their spurious re-stabilization at very high temperatures. This scheme is used because lattice instabilities are not accounted for within the CALPHAD framework, resulting in the Gibbs energy of solid phases being extrapolated into regions where it is not thermodynamically well-defined [22]. Yet, it seems challenging to both account for mechanical instabilities and model solution phases containing many elements using end-members.

From the Maxwell relation  \( (\partial C_{p}/\partial p)_{T} = -T(\partial^{2}V/\partial T^{2})_{p} \)  and the definition of the volumetric thermal expansion  \( \alpha \) , the following generally applicable equation is obtained:

 \[ \left(\frac{\partial C_{p}}{\partial p}\right)_{T}=-T V\left(\alpha^{2}+\left(\frac{\partial\alpha}{\partial T}\right)_{p}\right) \quad (2.1) \] 

with  \( C_{p} \)  the isobaric heat capacity.

In the models to describe the volume that are based on physical considerations, the temperature derivative of the thermal expansion coefficient always tends to increase with T at high temperature. This is due to the rise of electronic, and eventually thermal vacancies contributions in this range [23]. Therefore, if these models are coupled with an atmospheric pressure CALPHAD database in which the heat capacity of solid phases is kept constant above their melting point, it follows from Eq. (2.1) that it will inevitably lead to negative  \( C_{p} \)  at very high temperatures and pressures. This is why an “incompatibility” was observed by Brosh et al. [11] between the SGTE method of extrapolation and the Mie-Grüneisen equation of state. It is argued here that this problem is caused by an inconsistency more than an
 

incompatibility. That is because the heat capacity, the thermal expansivity and the bulk modulus  \( K_{T} \)  are closely related to each other, and their variations with temperature arise from the same underlying physics [24]. Therefore, if the SGTE method of extrapolation is applied to the heat capacity for practical purposes, it should also be extended to the description of  \( \alpha \)  and  \( K_{T} \) . In other words, if an arbitrary constant value is set for the heat capacity of solids above their melting point at atmospheric pressure, the same treatment should be applied to their thermal expansion coefficient and bulk modulus. Then, the description would be consistent, and it would be one way to solve the problem brought forward by Brosh et al. [11]. This approach would be practical and not physical, and, for a given model, its impact on the phase diagram and volumetric properties at high temperatures and pressures would have to be investigated. A more physical solution to solve this problem of inconsistency would be to remove the “SGTE constraint” from the databases, and then to rely on the high temperature extrapolations provided by the  \( 2^{nd} \)  generation CALPHAD phenomenological descriptions, or preferably on the ones provided by the  \( 3^{rd} \)  generation semi-empirical models. To avoid the spurious re-stabilization of solids at very high temperatures, the equal-entropy criterion proposed by Sundman et al. [25] could then be a remedial treatment.

However, to make any progress toward solving this problem of inconsistency, it is first necessary to have a suitable description of the volume, and a precise knowledge of how it behaves up to very high temperatures and pressures. Yet, such a knowledge is often lacking, because in the attempt to build high-pressure Gibbs energy databases so far, not a lot of attention has been given to the underlying description of the volume and its limitations.
 

## 3. Investigation of the Lu-Grover model

Grover et al. [14] found from static and dynamic compression data on a large variety of metals that, along isotherms, there was a nearly precise linear relationship between the molar volume and the logarithm of the isothermal bulk modulus. This empirical finding was observed up to volume changes of 40%, or up to pressure of two times the atmospheric bulk modulus. Subsequent studies suggest that this empirical law is not specific to metals, but also apply, at least to some extent, to oxides such as MgO and  \( Mg_{2}SiO_{4} \)  [16,18], and ionic compounds such as NaCl [20].

Based on the Grover empirical law, an explicit formulation of the volume was proposed by Lu et al. [15] as follows:

 \[ V=-c E i^{-1}\left(E i\left(-\frac{V^{0}}{c}\right)-\frac{1}{K_{T}^{0}}\exp\left(-\frac{V^{0}}{c}\right)(p-p^{0})\right) \quad (3.1) \] 

with c a material characteristic parameter that can be temperature dependent,  \( K_{T} \)  the isothermal bulk modulus, and Ei the exponential integral function that can be calculated numerically from tabulations. More details on how Eq. (3.1) is derived from the empirical finding from Grover et al. [14] are provided in Supplementary Note A. It is noted that, for the sake of clarity, a simple nomenclature is used for equations: the independent variables T and p do not appear explicitly, and for instance  \( V(T, p) \)  is simply written V. Besides, the underscript “0” is referring to the reference temperature, and superscript “0” to the atmospheric pressure, and for instance  \( K_{T}(T, p^{0}) \)  is written  \( K_{T}^{0} \) .

It was demonstrated by Lu et al. [15] that an explicit expression of the contribution to the Gibbs energy from the volume can then be obtained as follows:
 

 \[ G-G^{0}=cK_{T}{}^{0}\left(\exp\left(\frac{V^{0}-V}{c}\right)-1\right) \quad (3.2) \] 

The model proposed by Lu et al. [15] was applied in this work to the  \( \beta \) -Sn phase. The atmospheric pressure description of the volume and of the isothermal bulk modulus was taken from [24]. A comparison between this description [24] and the experimental data [26–50] is presented in Supplementary Notes A and B. It is noted that this description is based on a novel  \( 3^{rd} \)  generation CALPHAD model which differs from the phenomenological polynomial functions of T used so far in Gibbs energy approaches. However, numerically speaking, very similar descriptions could be obtained above room temperature using either type of model. Therefore, it is emphasized here that the results obtained throughout this study are not exclusive to the  \( 3^{rd} \)  generation CALPHAD framework. A value for the c parameter of  \( 2.945 \times 10^{-6} \)  was obtained from the fit of the molar volume [34,35,51,52] and bulk modulus [53–56] data available along the room temperature isotherm. The agreement that was reached is presented in Supplementary Note C. The Gibbs energy description at atmospheric pressure was taken from the  \( 3^{rd} \)  generation CALPHAD modeling proposed by Khvan et al. [57], which is supported by abundant and consistent data [57–65], as shown in Supplementary Note B. On this basis, the isobaric heat capacity of  \( \beta \) -Sn was calculated at various pressures using the Thermo-Calc software [66], and the results are presented in Fig. 1. A reasonable trend is obtained up to roughly 10 GPa, after which abnormal results are obtained. Indeed, the heat capacity becomes negative at higher pressure, which will lead to a negative entropy. It appears clearly from Fig. 1 that the so-called SGTE method of extrapolation is not at the origin of these abnormal results, as negative values for the heat capacity are obtained below 505 K, which is the atmospheric pressure melting point of the phase. Because the atmospheric pressure description proposed by Khvan et al. [57] is based on solid grounds (Fig. S1), it
 

follows from Eq. (1.1) that the contribution to the Gibbs energy from the volume is the source of the problem.

![](./images/867748583355449772_1.jpg)

Fig. 1 – Isobaric heat capacity of  \( \beta \) -Sn calculated using the Lu-Grover model

It follows from Eq. (2.1) that the problematic heat capacity extrapolations obtained at high pressure within the Lu-Grover framework must come from an unphysical description of the thermal expansion coefficient in this range. A hypothesis often made for solids is that the product of the thermal expansion by the bulk modulus is temperature independent [67]. It was claimed by Kumar et al. [68,69] that this product was also pressure independent, although no justification was provided by the authors to support this assumption. It was noted by Anderson et al. [70] that this hypothesis was also considered by Birch [71] for oxides and silicates based on experiments on alkali metals to up to 3 GPa. Therefore, this simplifying assumption is not well-established, and further investigations, possibly from ab initio calculations, would be of interest. Yet, this constraint may be useful to avoid obtaining an abnormal description of the thermal expansion at high pressure. Indeed, as the bulk modulus increases with pressure, the thermal expansion coefficient would naturally tend toward 0, which is the expected trend. Besides, the product  \( \alpha K_{T} \)  is also closely related to the thermal pressure, a property from which equations of state can be built upon, as it will be discussed in Section 7. For both these reasons, the variations of this product with pressure will be
 

investigated for each model considered in this work, starting with the Lu-Grover framework. For this model, the following equation can be obtained, as demonstrated in Supplementary Note A:

 \[ \left(\frac{\partial\alpha K_{T}}{\partial p}\right)_{T}=\frac{V^{0}\alpha^{0}}{c}+\frac{1}{K_{T}^{0}}\bigg(\frac{\partial K_{T}^{0}}{\partial T}\bigg)_{p}-\frac{1}{c}\ln\left(\frac{K_{T}}{K_{T}^{0}}\right)\left(\frac{\partial c}{\partial T}\right)_{p} \quad (3.3) \] 

In the present case of  \( \beta \) -Sn, variations along different isobars of the product  \( \alpha K_{T} \) , of  \( \alpha \)  and of  \( K_{T} \)  are presented in Fig. 2. As the positive c parameter is here a constant, the last term of Eq. (3.3) is removed. As a result, it can be deduced from Eq. (3.3) that the product  \( \alpha K_{T} \)  varies linearly with pressure along isotherms. Plus, Eq. (3.3) now simplifies into two contributions: a positive one linked to the description of the volume at atmospheric pressure, and a negative one linked to the temperature derivative of the bulk modulus at atmospheric pressure. It can be seen from Fig. 2(a) that at 437 K, the product  \( \alpha K_{T} \)  is pressure independent, which means both remaining terms of Eq. (3.3) cancel each other out. At lower temperatures,  \( \alpha K_{T} \)  decreases linearly with increasing pressure, and becomes negative on an increasingly wide temperature range. Thus, so does the thermal expansion, as seen in Fig. 2(b). It follows from Eq. (2.1) that this is what causes the spurious low temperature bumps observed above 10 GPa on the heat capacity of  \( \beta \) -Sn in Fig. 1. At higher temperatures, the product  \( \alpha K_{T} \)  increases linearly with increasing pressure. As a result, the higher the pressure, the higher the increase of thermal expansion with temperature. This result is also unphysical, and following Eq. (2.1), it leads to the negative heat capacity observed in Fig. 1.
 
![](./images/867748583355449772_2.jpg)

![](./images/867748583355449772_3.jpg)

![](./images/867748583355449772_4.jpg)

Fig. 2 – (a) Product  \( \alpha K_{T} \) , (b) thermal expansion coefficient, and (c) bulk modulus of  \( \beta \) -Sn calculated along different isobars using the Lu-Grover model

At atmospheric pressure, the modeling of  \( \beta \) -Sn is well-constrained by the data (Fig. S1-S2). Using the Lu-Grover model, the data on the volume available up to 15 GPa are reproduced closely (Fig. S2), but anomalies in the thermal expansion appear from 10 GPa (Fig. 2). In a recent study, the Lu-Grover model was applied to the Ti unary, and data on phase equilibria and volumetric properties were satisfactorily reproduced up to at least 20 GPa [5]. Using the
 

authors’ description, negative values for the thermal expansion coefficient of hexagonal close-packed Ti are obtained from 100 GPa. The experimental data on the volumetric properties of MgO were satisfactorily reproduced by Lu et al. [15], including thermal expansion data available up to 2000 K and 200 GPa. Yet, the description of the thermal expansion of the phase causes the  \( C_{p} = f(T) \)  curve to take an inverted U-shape from 50 GPa. It is concluded that the Lu-Grover model is only applicable at relatively low pressures that should not exceed one fourth of the standard bulk modulus of the phases. Nonetheless, despite this limitation, this model can help in understanding microstructure evolution in metals subjected to severe plastic deformation [5].
 

## 4. Investigation of the Joubert–Lu–Grover model

In an analysis complementary to the one presented in Section 3, Joubert et al. [13] recently investigated on the origin of the unphysical extrapolations obtained at high pressure within the Lu-Grover framework. It was demonstrated that abnormal heat capacity extrapolations arise from the uncontrolled behavior of the thermal expansion at high pressure, and to a lesser extent from the cross correlations between thermal expansion and compressibility. A revision of the Lu-Grover model was proposed so that a reasonable description of the volume would be obtained at high pressure. This revised approach was applied to the description of the Os-Pt binary system [72].

In the Joubert–Lu–Gover model, the description of the volume is still provided by Eq. (3.1), following the work of Lu et al. [15]. However, pressure dependent cut-off parameters are introduced in the expressions of  \( \alpha^{0} \)  and of  \( K_{T}^{0} \)  as follows:

 \[ \alpha^{0}=A_{0}\exp\left(-\frac{p}{p_{CUT}}\right)+\sum_{i}A_{i}T^{i}\exp\left(-\frac{p}{p_{CUT}}\right) \quad (4.1) \] 

 \[ K_{T}^{0}=\frac{1}{B_{0}+\sum_{i}B_{i}T^{i}\exp\left(-\frac{p}{p_{CUT}}\right)} \quad (4.2) \] 

with  \( p_{CUT} \)  and  \( p_{CUTR} \)  the added cut-off parameters,  \( A_{i} \)  and  \( B_{i} \)  the fitting parameters of the polynomial functions used for  \( 2^{nd} \)  generation CALPHAD descriptions of  \( \alpha^{0} \)  and  \( K_{T}^{0} \) , and i an integer. It is noted that in the original model from Lu et al. [15],  \( \alpha^{0} \)  and  \( K_{T}^{0} \)  are the atmospheric pressure thermal expansion coefficient and bulk modulus, but within the Joubert–Lu–Gover framework, at high pressures this is not true anymore, and they should then be considered more as model parameters.
 

It appears clearly from plotting  \( \exp(-x/x_{CUT}) \)  as a function of  \( x/x_{CUT} \)  that significant variations with x are only obtained in the  \( 10^{-3}x_{CUT} < x < 10x_{CUT} \)  range. Consequently, the pressure cut-off terms added in Eq. (4.1) and (4.2) such that  \( p_{CUT} < p_{CUT}' \)  only lead to significant variations with pressure in the  \( 10^{-3}p_{CUT} < P < 10p_{CUT}' \)  range. Hence, outside this range  \( \alpha^{0}, V^{0} \) , as well as  \( K_{T}^{0} \)  are pressure independent, and all the equations obtained within the Lu-Grover framework are still valid. When the pressure is lower than  \( 10^{-3}p_{CUT} \) , both cut-off terms are basically equal to 1, and the very same behavior as in the Lu-Grover model is maintained. When the pressure is greater than  \( 10p_{CUT}' \)  however, both cut-off terms are basically equal to 0, and provided that the c parameter is a constant, it can be shown that the thermal expansion becomes null, and the bulk modulus temperature independent. It is noteworthy that if the c parameter is modeled as a polynomial function of T as in the original work of Lu et al. [15], it can be deduced from Eq. (3.3) that, to keep the product  \( \alpha K_{T} \)  well-constrained, a cut-off parameter should also be applied to it as follows:

 \[ c=C_{0}+\sum_{i}C_{i}T^{i}\exp\Big(-\frac{p}{p_{CUT}}\Big) \quad (4.3) \] 

with  \( C_{i} \)  the fitting parameters of the polynomial function used to describe the c parameter.

A consequence of the modifications presented in Eq. (4.1), (4.2) and (4.3) is that, in the Joubert-Lu-Grover model,  \( \alpha^{0} \) ,  \( K_{T}^{0} \)  and possibly also c are pressure dependent in the  \( 10^{-3}p_{CUT} < p < 10p_{CUT}' \)  range. As a result, the explicit expression of the contribution to the Gibbs energy from the volume presented in Eq. (3.2) does not hold anymore. Therefore, in order to compute the thermodynamic properties at high pressure, it is required to perform a numerical integration of V over p. Yet, it may still be interesting to use Eq. (3.2). Besides from allowing to gain in computational efficiency, it can be shown that within the Joubert-Lu-Grover framework, all the parameters from Eq. (3.2) are temperature independent at high
 

pressure. Therefore, if Eq. (3.2) is used, there will be no contribution from the volume to the entropy in the high-pressure range, meaning that the heat capacity will start by decreasing with pressure, but will eventually increase back up to its atmospheric pressure value. This trend is unphysical, and the Gibbs energy function calculated that way is inexact. Yet, to follow this approach has the benefit of ensuring direct compatibility with the SGTE method of extrapolation. Therefore, it could be a be a practical solution to the problem of inconsistency that was discussed in Section 2, leading at high pressure and temperature to an approximate but reasonable thermodynamic description, and maybe to a correct phase diagram as suggested by recent studies  \( [72,73] \) .

A practical investigation of the Joubert-Lu-Grover model was conducted taking the case of  \( \beta \) -Sn. As in Section 3, the description at atmospheric pressure of the thermal expansion and the bulk modulus were accepted from [24]. Because it is based on a  \( 3^{rd} \)  generation CALPHAD model, the Joubert-Lu-Grover model that was proposed in the framework of  \( 2^{nd} \)  generation polynomial formulations had to be adapted as described in detail in Supplementary Note D. In order to adjust the  \( p_{CUT} \)  and  \( p_{CUTR}' \)  parameters, information on the volume of the phase in the T - p space are ideally required. Yet, high-pressure measurements for the  \( \beta \) -Sn phase are limited along the room temperature isotherm. Therefore, an arbitrary value of  \( 10^{10} \)  Pa was selected for  \( p_{CUTR}' \) . Then, values for  \( p_{CTOT} \)  and c of respectively  \( 2 \times 10^{9} \)  Pa and  \( 3.456 \times 10^{-6} \)  were obtained from fitting the bulk modulus [53–56] and molar volume [34,35,51,52] data available along the room temperature isotherm. The agreement that was reached is presented in Supplementary Note E. It is noted that different values for the parameters listed above could lead to equally satisfying results, and additional data at high pressure, possibly from DFT calculations, would be needed to constrain further the model. Nonetheless, the available experimental data are enough for the present purpose, which is to highlight the general
 

features of different models. Finally, the atmospheric pressure description of the Gibbs energy was taken from [57].

From this description, various calculations were conducted along the 298.15 K isotherm using the Thermo-Calc software [66] and worksheets, and the results are presented in Fig. 3. It is shown in Fig. 3(a) that the product  \( \alpha K_{T} \)  reaches a constant value of 0 at high pressure within the Joubert-Lu-Grover framework, whereas it becomes negative for the description based on the Lu-Grover model. Because the bulk modulus is similar for both modeling as shown in Fig. 3(b), this change in the product  \( \alpha K_{T} \)  mainly impacts the thermal expansion, that is presented for both cases in Fig. 3(c). Using the Joubert-Lu-Grover model, the thermal expansion does not exhibit an abnormal behavior at high pressure anymore, but does tend to 0, which is the expected and reasonable trend.
 
![](./images/867748583355449772_5.jpg)

![](./images/867748583355449772_6.jpg)

![](./images/867748583355449772_7.jpg)

Fig. 3 – (a) Product  \( \alpha K_{T} \) , (b) bulk modulus, (c) thermal expansion coefficient of  \( \beta \) -Sn calculated along the 298.15 K isotherm using the Joubert-Lu-Grover model and the Lu-Grover model.

The Joubert-Lu-Grover model has been applied successfully to describe up to high temperatures and pressures the volumetric properties of face-centered cubic Pt [13], hexagonal close-packed Os [72], and body-centered tetragonal and cubic Sn [73]. Yet, after calculating the Gibbs energy by numerical integration of V over p, it appears from Fig. 4(a) that the heat capacity is overestimated at high temperatures and pressures, considering that it
 

should converge to the Dulong-Petit limit of 3R in this range. This overestimation is due to the steep decline of the temperature derivative of the thermal expansion coefficient above the cut-off term  \( \exp(-p/p_{cut}) \) . A possible solution to improve the description would be to use a different mathematical expression for this term. Another possibility is, as discussed above, to use Eq. (3.2) to compute the thermodynamic functions instead of performing a numerical integration of the volume. Doing so, it appears from Fig. 4(b) that, as expected, at high pressures the  \( C_{p} \)  increases back toward its atmospheric pressure value. While this trend is abnormal, this approach may still be a practical solution for extending CALPHAD databases toward high pressures if the “SGTE constraint” (Section 2) is set to the Dulong-Petit limit. Indeed, this approach was applied to the Sn unary, and the available data on phase equilibria, shock compression and volumetric properties were closely reproduced up to pressures of almost 3 times the standard bulk modulus of the element, and temperatures 5 times higher than its atmospheric pressure melting point [73].

![](./images/867748583355449772_8.jpg)

(a)

![](./images/867748583355449772_9.jpg)

(b)

Fig. 4 – Heat capacity of  \( \beta \) -Sn calculated in two different ways using the Joubert-Lu-Grover model. (a) Exact determination from the Gibbs energy that was calculated by numerical integration of the volume, and (b) approximate determination from Eq. (3.2). In (a), the description of the heat capacity at atmospheric pressure was left unconstrained above the melting point of the phase of 505 K, whereas in (b) the “SGTE constraint” was set to 3R.
 

## 5. Investigation of the Jacobs-Grover model

The empirical relation discovered by Grover et al. [14] was originally an isotherm. Yet, Jacobs et al. [16–19] assumed that this relationship was also valid along isobars. The following relationship was then proposed by the authors in their former work on MgO [16,17]:

 \[ V=V_{0}^{0}-c\ln\left(\frac{K_{T}}{K_{T_{0}^{0}}}\right) \quad (5.1) \] 

It is highlighted that the parameters of Eq. (5.1) are constants, as they are independent not only of p as in the Lu-Grover model, but also of T.

In their later work on  \( Mg_{2}SiO_{4} \)  [18] and  \( Fe_{2}SiO_{4} \)  [19], Jacobs et al. introduced an additional parameter in Eq. (5.1), leading to:

 \[ V=V_{0}^{0}+a(T-T_{0})-c\ln\left(\frac{K_{T}}{K_{T_{0}}^{0}}\right) \quad (5.2) \] 

with a the additional material-dependent constant, which role will be explained shortly.

By re-arranging Eq. (5.2), following the same approach detailed in Supplementary Note A for the Lu-Grover model, the following differential equation is obtained:

 \[ \frac{\exp\left(-\frac{V_{0}^{0}+a(T-T_{0})}{c}\right)}{K_{T}^{0}}=-\frac{\exp\left(-\frac{V}{c}\right)}{V}\left(\frac{\partial V}{\partial p}\right)_{T} \quad (5.3) \] 

Unlike Lu et al. [15], Jacobs et al. [19] did not use the exponential integral function to solve Eq. (5.3), but a power series, leading to:

 \[ p=p^{0}-K_{T_{0}}^{0}\exp\left(\frac{V_{0}^{0}+a(T-T_{0})}{c}\right)\left(\ln\left(\frac{V}{V^{0}}\right)+\sum_{j=1}^{\infty}\left(-\frac{c^{-j}\left(V^{j}-(V^{0})^{j}\right)^{j}}{j\times j!}\right)\right) \quad (5.4) \]
 

An explicit expression of the volume cannot be obtained from Eq. (5.4), and roughly 20 to 30 terms are needed in the power series to obtain accurate descriptions. Therefore, it makes the Jacobs-Grover approach less computationally efficient compared to the models investigated so far. Besides from this practical consideration, let us now investigate the implications of the fact that, in the model of Jacobs et al. [16–19], the relation from Grover et al. [14] was considered to hold along both isotherms and isobars, i.e., the reference volume and bulk modulus are constants in the initial Eq. (5.1). As detailed in Supplementary Note F, the following equations can be obtained:

 \[ \left(\frac{\partial\alpha K_{T}}{\partial p}\right)_{T}=\frac{a}{c} \quad (5.5) \] 

 \[ \left(\frac{\partial K_{T}}{\partial T}\right)_{V}=\frac{a}{c}K_{T} \quad (5.6) \] 

It appears from Eq. (5.6) that without using the a parameter, the bulk modulus would be temperature independent along isochores. As a result, it follows from Eq. (5.5) that the product  \( \alpha K_{T} \)  would be pressure independent along isotherms, as discussed by Jacobs et al. [74] in their reply to the comments from Raju et al. [75]. The a parameter is therefore needed to account for the deviations from this ideal behavior. In practice, it can also be shown that without using the a parameter, the c parameter solely accounts for the variations of the bulk modulus along both isobars and isotherms. A satisfying fit of the available data may therefore not be obtained with this single degree of freedom, as it was notably highlighted by Jacobs et al. [18] in the case of  \( Mg_{2}SiO_{4} \) . Nonetheless, if the a parameter is negative, such as for  \( Mg_{2}SiO_{4} \)  [18], the product  \( \alpha K_{T} \)  will exhibit a monotonic decrease with increasing pressure. At high pressure, this will inevitably result in a negative thermal expansion coefficient. This feature may lead to similar problems as the ones encountered with the Lu-Grover model (Section 3).
 

## 6. A revised Jacobs-Grover model

In section 5, it was highlighted that, although the Jacobs-Grover model leads to a more predictable behavior at high pressure than the Lu-Grover approach, it is not free from abnormal behavior nonetheless. Besides, it is also less computationally efficient. In the following, a revised Jacobs-Gover model is proposed, aiming at solving both issues.

First of all, in order to avoid obtaining a monotonic decrease of the product  \( \alpha K_{T} \)  with increasing pressure, a pressure dependent cut-off term, similar to the ones introduced in the Joubert-Lu-Grover model, is added on the a parameter of Eq. (5.2) as follows:

 \[ a=a^{0}\exp\left(-\frac{p}{p_{CUT}}\right) \quad (6.1) \] 

with  \( a_{0} \)  the initial parameter optimized using available bulk modulus data, and  \( p_{CUT} \)  the pressure cut-off from which the a parameter will rapidly drop to 0. Following the same approach as detailed in Supplementary Note A and E, it can be shown that:

 \[ \left(\frac{\partial\alpha K_{T}}{\partial p}\right)_{T}=\frac{a}{c}+\frac{\alpha(T-T_{0})}{c}\left(\frac{\partial a}{\partial p}\right)_{T} \quad (6.2) \] 

As discussed in Section 4, the cut-off term added in Eq. (6.1) basically acts as a switch which goes from 1 for pressures below  \( 10^{-3} p_{CUT} \)  to 0 for the ones above  \( 10 p_{CUT} \) . Therefore, when  \( p < 10^{-3} p_{CUT} \) , the a parameter is equal to the initial value  \( a_{0} \)  and is pressure independent, so the same behavior as the original Jacobs-Grover model is obtained. When  \( p > 10 p_{CUT} \)  however, the a parameter becomes equal to 0, and so does its pressure derivative. As a result, it can be seen from Eq. (6.2) that the product  \( \alpha K_{T} \)  will become pressure independent as well. Therefore, the product  \( \alpha K_{T} \)  will not exhibit a monotonic decrease at high pressure anymore, and the modification proposed in Eq. (6.1) thus fixes the anomaly of the Jacobs-Grover model highlighted in Section 5.
 

Then, instead of using a power series to solve differential equation (5.3), the exponential integral function can be used. As in the Lu-Grover approach, an explicit expression of the volume can then be obtained. By injecting pressure dependent Eq. (6.1) into Eq. (5.3), it turns out that the exponential integral function now has to be used to solve both sides of the differential equation. By re-arranging the obtained result, the following description of the volume is finally obtained:

 \[ \begin{aligned}V&=-cE i^{-1}\left(Ei\left(-\frac{V^{0}}{c}\right)\right.\\&\left.\quad-\frac{1}{K_{T_{0}}^{0}}\exp\left(-\frac{V_{0}^{0}}{c}\right)p_{CUT}\left(Ei\left(-\frac{a^{0}(T-T_{0})}{c}\exp\left(-\frac{p^{0}}{p_{CUT}}\right)\right)\right.\right.\\&\left.\left.\quad-Ei\left(-\frac{a^{0}(T-T_{0})}{c}\exp\left(-\frac{p}{p_{CUT}}\right)\right)\right)\right)\\ \end{aligned} \quad (6.3) \] 

Despite appearances, Eq. (6.3) is no more complicated than Eq. (3.1) from the Lu-Grover model, and it can be solved in a worksheet after tabulating the exponential integral function. In practice, a numerical problem is however obtained at pressures significantly higher than  \( p_{CUT} \) , because  \( \exp(-p/p_{CUT}) \)  then quickly leads to unreasonably low arguments for the most right hand side  \( E_{i} \)  function. To overcome this practical issue, we used the fact that when  \( p > 20 p_{CUT} \) , the a parameter defined in Eq. (6.1) can very reasonably be taken to be 0, as it is  \( 10^{9} \)  times smaller than its original value at  \( p^{0} \) . Therefore, for pressures higher than  \( 20 p_{CUT} \) , differential equation (5.3) can be solved considering both distinct intervals as follows:
 

 \[ \begin{aligned}V&=-cE i^{-1}\left(E i\left(-\frac{V^{0}}{c}\right)\right.\\&\left.\quad-\frac{1}{K_{T_{0}}^{0}}\exp\left(-\frac{V_{0}^{0}}{c}\right)p_{CUT}\left(E i\left(-\frac{a^{0}(T-T_{0})}{c}\exp\left(-\frac{p^{0}}{p_{CUT}}\right)\right)\right.\right.\\&\left.\left.\quad-E i\left(-\frac{a^{0}(T-T_{0})}{c}\exp(-20)\right)\right)+p-20p_{CUT}\right)\end{aligned} \quad (6.4) \] 

Finally, for materials for which a is equal to 0 at atmospheric pressure, such as MgO [16,17], the description of the volume is provided by the following expression, reminiscent of Eq.

(3.1) from the Lu-Grover model:

 \[ V=-cE i^{-1}\left(E i\left(-\frac{V^{0}}{c}\right)-\frac{1}{K_{T_{0}}^{0}}\exp\left(-\frac{V_{0}^{0}}{c}\right)(p-p^{0})\right) \quad (6.5) \] 

Following the same procedure that was presented by Lu et al. [15] to derive their Eq. (10), the effect of pressure on the Gibbs energy function is obtained from Eq. (5.3) as follows:

 \[ G-G^{0}=cK_{T_{0}}^{0}\exp\left(\frac{V_{0}^{0}+a^{0}exp\left(-\frac{p}{p_{CUT}}\right)(T-T_{0})}{c}\right)\left(\exp\left(-\frac{V}{c}\right)-\exp\left(-\frac{V^{0}}{c}\right)\right) \quad (6.6) \] 

This revised Jacobs-Grover equation of state was applied to the modeling of the  \( \beta \) -Sn phase. The description of  \( V^{0} \)  and  \( G^{0} \)  were taken from [24] and [57], respectively. Values for the c, a and  \( p_{CUT} \)  parameters of  \( 3.5 \times 10^{-6} \) ,  \( -6 \times 10^{-10} \)  and  \( 10^{9} \)  Pa were respectively obtained from fitting the bulk modulus [53–56] and molar volume [34,35,51,52] data along the room temperature isotherm, as well as the bulk modulus data along the atmospheric pressure isobar [32,48–50] critically selected in [24]. A satisfying agreement between the model and the available experimental data was reached, as presented in Supplementary Note G.
 

From the obtained description, calculations were conducted along different isobars, and the results are presented in Fig. 5. To begin with, it is highlighted in Fig. 5(a) that, in contrast with the Lu-Grover model, the product  \( \alpha K_{T} \)  does vary only slightly with increasing pressure, and becomes pressure independent above  \( p_{CUT} \)  due to our modification. However, a very different trend is noted regarding the variations of this quantity with temperature, which are imposed by the Grover empirical law that was considered valid not only along isotherms, but also along isobars. Indeed, it appears from Fig. 5(a) that above 1000 K, the product  \( \alpha K_{T} \)  starts decreasing strongly with temperature. Then, from 3500 K, it slowly diminishes down to 0 GPa. \( K^{-1} \)  at atmospheric pressure, or down to a slightly negative value at higher pressure due to the use of the a parameter. The bulk modulus presented in Fig. 5(b) varies with temperature in a somewhat consistent manner, decreasing steeply before also becoming almost temperature independent above 3500 K. Next, it is shown in Fig. 5(c) that when the pressure increases even so slightly, there is a critical temperature from which the thermal expansion coefficient will suddenly drop from the accepted atmospheric pressure description. This critical temperature decreases with increasing pressure. Indeed, if the anomaly occurs from roughly 4700 K just above atmospheric pressure, at 100 GPa this behavior is obtained from 1000 K, which is roughly twice the atmospheric pressure melting point of the phase. It follows from Eq. (2.1) that this decrease in the thermal expansion coefficient will lead to a significant increase in the heat capacity at high pressure, as highlighted in Fig. 5(d), which is unphysical. This limitation is inherent to the Jacobs-Grover framework, and comes from the fact that the Grover relationship was considered to be valid along isobars, a hypothesis which does not seem to hold at high temperatures, especially when the pressure is also high. Using the description of MgO proposed by Jacobs and Oonk [16,17], it is found that the temperature derivative of the thermal expansion coefficient of the phase becomes negative from 4000 K at 10 GPa, and from 2500 K at 160 GPa. It is concluded that, at pressures close to the standard
 

bulk modulus of the material, the Jacobs-Grover model is only applicable up to relatively low temperatures that should not exceed its atmospheric pressure melting point.

(a)

![](./images/867748583355449772_10.jpg)

![](./images/867748583355449772_11.jpg)

(b)

![](./images/867748583355449772_12.jpg)

![](./images/867748583355449772_13.jpg)

Fig. 5 – (a) Product  \( \alpha K_{T} \) , (b) bulk modulus, (c) thermal expansion coefficient, and (d) heat capacity of  \( \beta \) -Sn calculated along different isobars using the revised Jacobs-Grover model. The discontinuity in the temperature derivative of the heat capacity function in (d) at 505 K is caused by the SGTE method of extrapolation.
 

## 7. Investigation of a model based on the use of thermal pressure

In the models investigated so far, the effect of temperature on the volume were accounted for by injecting temperature dependent descriptions of  \( \alpha \) , V and  \( K_{T} \)  into isothermal equations of state. In other words, the base principle was to first take position along the reference isobar by computing the volume and related properties at the temperature of interest, and then to extend the description toward high pressure from this point. An alternative to this approach is to make use of the concept of thermal pressure, which was extensively discussed by Anderson [67]. In equations of state in the form  \( p = f(T, V) \) , it is common to express the pressure as the sum of two contributions. The first one, referred as the cold pressure, is computed as a function of the volume only using an isothermal equation of state. The second one is the thermal pressure, noted  \( p_{TH} \) . It is obtained based on the thermodynamic identity  \( (\partial p / \partial T)_{V} = \alpha K_{T} \)  from the following integral, which is made at constant volume:

 \[ p_{T H}=\int\limits_{T_{0}}^{T}\alpha K_{T}d T \quad (7.1) \] 

For the present purpose, an equation of state in the form  \(  V = f(T, p)  \)  is required. Then, it follows from the definition of thermal pressure that the volume at given high temperature and pressure conditions is equivalent to a volume at a lower pressure along the reference isotherm:

 \[ V(T,P)=V(T_{0},p-p_{T H}) \quad (7.2) \] 

In practice, in order to solve Eq. (7.1) without using V as an independent variable, hypotheses have to be made. For instance, Anand et al. [20] considered that the product  \( \alpha K_{T} \)  was a constant, independent of both T and p.
 

In this work, the temperature dependence of the product  \( \alpha K_{T} \)  is modeled within the framework proposed in [24], which is built upon on a multi-frequency Einstein-Grüneisen model. The following equation is obtained:

 \[ \alpha K_{T}=\frac{3R}{V_{0}^{0}}\sum_{i}\gamma_{i0}a_{i}\left(\left(\frac{\theta_{i}}{T}\right)^{2}\frac{e^{\frac{\theta_{i}}{\bar{T}}}}{\left(e^{\frac{\theta_{1}}{\bar{T}}}-1\right)^{2}}+A T+B T^{2}\right) \quad (7.3) \] 

with R the gas constant,  \( \theta_{i} \) ,  \( a_{i} \)  and  \( \gamma_{i0} \)  the Einstein temperature, a pre-factor, and the Grüneisen parameter associated with the  \( i^{th} \)  Einstein mode of vibration, and A and B parameters to account for anharmonic and electronic contributions to the heat capacity.

Then, the product  \( \alpha K_{T} \)  is considered to be pressure independent, and it follows from Eq. (7.1) that the thermal pressure can be obtained by integration of Eq. (7.3), which gives:

 \[ p_{T H}=\frac{3R}{V_{0}^{0}}\sum_{i}\gamma_{i0}a_{i}\left(\frac{\theta_{i}}{e^{\frac{\theta_{i}}{\bar{T}}}-1}+\frac{A T^{2}}{2}+\frac{B T^{3}}{3}\right) \quad (7.4) \] 

From this point, the empirical description discovered by Grover et al. [14] is formulated along the reference isotherm as follows:

 \[ V_{0}=V_{0}^{0}-c\ln\left(\frac{K_{T0}}{K_{T0}^{0}}\right) \quad (7.5) \] 

Following the same procedure detailed in Supplementary Note A, an isothermal description of the volume is obtained from Eq. (7.5). The effect of temperature is then accounted for based on Eq. (7.2) and (7.1), and the following description is finally obtained:

 \[ V=-c E_{i}^{-1}\left(E_{i}\left(-\frac{V_{0}^{0}}{c}\right)-\frac{1}{K_{T0}^{0}}\exp\left(-\frac{V_{0}^{0}}{c}\right)(p-p_{T H}-p^{0})\right) \quad (7.6) \]
 

where it is stressed out that the c parameter has to be a constant, as otherwise the product  \( \alpha K_{T} \)  would not be pressure independent.

It is emphasized here that the same general behavior could be obtained from either Eq. (7.6) or from the model proposed by Anand et al. [20] based on the isothermal formulation from Saxena [21] of the Grover empirical law. Indeed, although Anand et al. [20] considered that the product  \( \alpha K_{T} \)  was temperature independent, Eq. (7.4) could very well be injected in the authors' framework to generalize it. Therefore, the main difference lies in the isothermal equation of state that was used to build each model. In the formulation provided by Saxena [21] and used by Anand et al. [20], it appears that the bulk modulus was considered to vary linearly with pressure. An advantage of this simplifying assumption is that an explicit expression of  \( K_{T} \)  can be obtained as a function of T and p. In this work, the formulation of the empirical law from Grover et al. [14] presented in Eq. (7.5) was preferred to build the model so that it could be more precise.

To investigate on the features of the present model, it was applied to  \( \beta \) -Sn. All the parameters of Eq. (7.3) were taken from [24] in addition to  \( K_{T}^{0} \)  from Eq. (7.6). The c parameter was adjusted based on the bulk modulus data along the atmospheric pressure isobar [32,48–50] critically selected in [24], and a value of  \( 2.1 \times 10^{-6} \)  was obtained. A satisfying fit was reached as presented in Supplementary Note H. However, above 1 GPa, the volume and bulk modulus data available along the reference isotherm could not be satisfactorily reproduced, as also highlighted in Supplementary Note H. This difficulty to reproduce the data accurately is due to the fact that there is only a single degree of freedom, that is the parameter c, to account for the variations of  \( K_{T} \)  along both isobars and isotherms. It is similar to what was discussed in Section 5. It is a limitation of the present approach and of the similar Anand-Saxena-Grover model.
 

Then,  \( \alpha \) ,  \( K_{T} \) , and the product  \( \alpha K_{T} \)  of  \( \beta \) -Sn are calculated along different isobars and the results are presented in Fig. 6(a-c). To begin with, it can be seen from Fig. 6(a) that the bulk modulus decreases strongly with temperature. As a result, at low pressures, it quickly becomes negative. Brosh et al. [11] obtained similar results in their modeling of solid Al using a Mie-Grüneisen equation of state also based on the use of thermal pressure, and it was discussed by the authors that this behavior meant that the phase had become mechanically unstable from this point. A consequence of this trend is that, when  \( K_{T} \)  reaches 0, the product  \( \alpha K_{T} \)  follows, deviating from the input atmospheric pressure description as presented in Fig. 6(b). As a result,  \( \alpha \)  diverges to infinitely high values approaching from this critical point as seen in Fig. 6(c). In the present case of  \( \beta \) -Sn, this sharp increase of  \( \alpha \)  starts from roughly 700 K at  \( 10^{5} \)  Pa, which is only slightly higher than the corresponding melting point of the phase of 505 K. In the case of CaO however, which was also investigated based on the description proposed in [24], at  \( 10^{5} \)  Pa this increase starts before the melting point of the compound of 3222 K [76]. As a result, the available high temperature thermal expansion data cannot be closely reproduced. Besides, it follows from Eq. (2.1) that this steep increase in the thermal expansion coefficient will lead to a dramatic decrease in the heat capacity with increasing pressure. While it can be argued that these extrapolations may not be physically meaningful if the phase had become mechanically unstable, this behavior occurs at low pressure at temperatures which are close to the melting point of the phases, and it appears as an important limitation in the context of establishing Gibbs energy databases.

It is interesting to note that, for the approaches based on the use of thermal pressure discussed in this section, the higher the pressure, the better the result. Indeed, it can be seen from Fig. 6 that for  \( \beta \) -Sn, problematic features are obtained at low pressures, whereas reasonable extrapolations are achieved at 100 GPa. In the models investigated so far, it is rather at high pressure that problems would arise. Some insights on this unusual feature can be gained from
 

Fig. 6(d), where  \( p - p^{0} - p_{TH} \)  is presented as a function of T along different isobars. At  \( 10^{5} \)  Pa, this term is always negative. At the corresponding melting point of  \( \beta \) -Sn, it reaches roughly -1.6 GPa. Yet, most isothermal equations of state, such as the one built based on the Grover empirical law in this section, were established for compression only. Therefore, it may be suggested that problematic results are obtained at low cold pressures and high temperatures because high tensile stresses are then input in an isothermal equation of state that is not valid in this domain. At very high cold pressures however,  \( p - p^{0} - p_{TH} \)  is positive, and reasonable results are thus obtained.

![](./images/867748583355449772_14.jpg)

![](./images/867748583355449772_15.jpg)

![](./images/867748583355449772_16.jpg)

![](./images/867748583355449772_17.jpg)

Fig. 6 – (a) Bulk modulus, (b) product  \( \alpha K_{T} \) , and (c) thermal expansion coefficient of  \( \beta \) -Sn calculated along different isobars using the approach based on the Grover empirical law and the use of thermal pressure presented in Section 7. (d) Overall pressure input in the model calculated from the difference between the cold pressure and the thermal pressure.
 

## 8. A new scheme based on the equivalence between pressure and temperature

For the models based on the use of thermal pressure discussed in Section 7, it was highlighted that problematic results were obtained when  \( p - p^{0} - p_{TH} \)  was significantly negative. Nevertheless, satisfying extrapolations were reached for high cold pressures. Therefore, in the present section, the same model as presented in Section 7 is adopted when  \( p - p^{0} - p_{TH} \)  is positive. However, when  \( p - p^{0} - p_{TH} \)  is negative, a new scheme also based on the equivalence between pressure and temperature when calculating the volume is proposed. A corollary of the approach leading to Eq. (7.2) is that the volume at a given high temperature and pressure is equivalent to a volume along the atmospheric pressure isobar, but at a lower temperature. Put into equation, it gives:

 \[ V(T,p)=V\big(T_{EQUIV},p^{0}\big) \quad (8.1) \] 

with  \( T_{EQUIV} \)  the equivalent temperature defined when  \( p - p^{0} - p_{TH} \)  is negative as:

 \[ p^{0}+p_{TH}-P=\int\limits_{T_{0}}^{T_{EQUIV}}\alpha K_{T}dT \quad (8.2) \] 

In this study, an explicit expression of  \( T_{EQUIV} \)  as a function of T and p could not be obtained. Therefore, this term had to be computed numerically from the function  \(  p_{TH} = f(T)  \)  as  \(  T_{EQUIV} = f^{-1}(p - p^{0} - p_{TH})  \) . This makes this model less computationally efficient than the other approaches previously discussed.

To summarize, when the difference between the cold pressure and the thermal pressure is negative (i.e., at rather low p or high T, see Fig. 6(d)), the volume is calculated along the  \( p^{0} \)  isobar based on Eq. (8.1) and (8.2). Because the product  \( \alpha K_{T} \)  is considered to be pressure
 

independent, all that is required in this range is  \( \alpha^{0} \) ,  \( K_{T}^{0} \) , and  \( V_{0}^{0} \) , i.e., a description at atmospheric pressure of the volume and related properties. Then, when the difference between the cold pressure and the thermal pressure becomes positive (i.e., at rather high p or low T, see Fig. 6(d)), the volume is calculated along the room temperature isotherm based on Eq. (7.6). An additional parameter c, which is a constant, is required in this range.

This scheme was applied to the modeling of  \( \beta \) -Sn. The description of the volume and related properties at atmospheric pressure was taken from [24], and the thermal pressure was then calculated using Eq. (7.4) that is derived from the authors' model. Next, the c parameter from Eq. (7.6) was adjusted using the bulk modulus [53–56] and molar volume [34,35,51,52] data available along the room temperature isotherm. As in Section 6, a value of  \( 3.5 \times 10^{-6} \)  was obtained for this parameter.

On this basis, the product  \( \alpha K_{T} \) ,  \( \alpha \) , and  \( K_{T} \)  of  \( \beta \) -Sn were calculated along different isobars, and the results are presented in Fig. 7. Reasonable extrapolations of  \( \alpha \)  and  \( K_{T} \)  are obtained up to very high temperatures at both low and high pressures, as shown in Fig. 7(b-c). Plus, the available experimental data along both the atmospheric pressure isobar and the room temperature isotherm were fitted closely, as shown in Supplementary Note I. This satisfying fit was reached under the assumption that the product  \( \alpha K_{T} \)  was pressure independent, and without using an extra  \( \alpha \)  parameter as in the Jacobs-Grover framework. However, at the specific conditions of p and T where  \( p - p^{0} - p_{TH} \)  equals 0, such as at 10 GPa and roughly 2000 K, a temperature derivative discontinuity is observed for  \( \alpha \)  and  \( K_{T} \) . This is due to the transition between the two submodels when the overall pressure goes from tensile to compressive. It may be argued that, in practice, this breakpoint in the temperature derivative of  \( \alpha \)  and  \( K_{T} \)  should not significantly impact the validity of the description.
 
![](./images/867748583355449772_18.jpg)

![](./images/867748583355449772_19.jpg)

![](./images/867748583355449772_20.jpg)

Fig. 7 – (a) Product  \( \alpha K_{T} \) , (b) thermal expansion coefficient, and (c) bulk modulus of  \( \beta \) -Sn calculated along different isobars using the new scheme presented in Section 8 that is based on the equivalence between temperature and pressure when calculating the volume.

In Fig. 8, the heat capacity of  \( \beta \) -Sn is calculated numerically along different isobars based on the present description of the volume and on the atmospheric pressure thermodynamic description from [57]. A reasonable description is obtained up to temperatures and pressures of roughly twice the atmospheric pressure melting point and the standard bulk modulus of the
 

phase, respectively. However, the heat capacity decreases too much with increasing pressure, and the model does not converge to the Dulong-Petit limit of 3R at high temperatures and pressures. Additional constraints in the model or in the optimization procedure would be required to improve the description. It is noted that very slightly negative values are obtained below 30 K.

![](./images/867748583355449772_21.jpg)

Fig. 8 – Heat capacity of  \( \beta \) -Sn calculated numerically from the description of the volume presented in Section 8 and the atmospheric pressure thermodynamic description from [57] from which the “SGTE constraint” was removed.
 

## Conclusion

The current shortcomings of high-pressure Gibbs energy approaches are identified to be caused by an inconsistent treatment of the SGTE method of extrapolation, and an insufficient knowledge of the underlying models to describe the volume and their limitations. Two possible practical ways of solving the first problem were outlined in Section 2. Then, several models to describe the volume were analyzed.

First, it was demonstrated in Section 3 that the Lu-Grover model leads to an unphysical description of the thermal expansion at high pressure. This model is only applicable at relatively low pressures that should not exceed one fourth of the standard bulk modulus of the material. In the Joubert-Lu-Grover model discussed in Section 4, new parameters are added to improve the description. This revised model has been applied successfully to describe the volumetric properties of several metals up to high temperatures and pressures. Within this framework, the thermodynamic properties can be computed in two ways. The first is by performing a numerical integration of V over p, which leads to an overestimated heat capacity at high pressure. This could possibly be improved by modifying the mathematical expression of the pressure cut-off terms introduced in the model. The second is by using an equation that leads to an approximate description of the heat capacity. This approach allows direct compatibility with the SGTE method of extrapolation. It appears promising to extend CALPHAD databases up to pressures of at least twice the standard bulk modulus of the phases, and temperatures higher than twice their atmospheric pressure melting point. Further studies, notably on materials other than metals, would be of interest.

Then, the Jacobs-Grover model was investigated in Sections 5-6, and improvements were proposed to make it more computationally efficient and to avoid an unphysical high-pressure feature. It was found that the Jacobs-Grover approach is only applicable within a limited
 

temperature range, and that the higher the pressure, the lower the critical temperature from which problematic results are obtained. At pressures close to the standard bulk modulus of the material, the Jacobs-Grover model should not be applied at temperatures higher than its atmospheric pressure melting point.

Last, a model based on the use of thermal pressure to account for the temperature dependence of the volume was investigated in Section 7. This attempt leads to the same general behavior as the Anand-Saxena-Grover model. The data on the volumetric properties of  \( \beta \) -Sn could not be satisfactorily reproduced by this approach. Besides, problematic results were obtained at relatively low cold pressures and high temperatures. To solve both these problems, a new scheme based on the equivalence between T and p was proposed in Section 8. This model led to a reasonable description of the volumetric properties of  \( \beta \) -Sn for all temperatures and pressures, but it relies heavily on numerical calculations. Besides, additional constraints in the model or in the optimization procedure would be required to improve the description of the heat capacity. Therefore, this approach seems to have potential, but requires further refinement and validation.

## Acknowledgements

The authors gratefully acknowledge the French consortium in high temperature thermodynamics GDR CNRS n°3584 (TherMatHT), where constructive exchanges led to the present collaborative work. This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
 

## Data Statement

For the models investigated in Section 3 and 4, thermodynamic database files made for the Thermo-Calc [66] software are provided as supplementary materials. The atmospheric pressure data that were used to constrain some model parameters are available in [77]. Other materials (literature datasets, worksheets...) can be made available upon request.

## Declaration of competing interest

We declare no competing interests.

## References

[1] J.C. Jie, C.M. Zou, E. Brosh, H.W. Wang, Z.J. Wei, T.J. Li, Microstructure and mechanical properties of an Al–Mg alloy solidified under high pressures, Journal of Alloys and Compounds. 578 (2013) 394–404. https://doi.org/10.1016/j.jallcom.2013.04.184.

[2] T. Gu, J. Li, F. Xu, L. Wu, Y. Zhao, H. Hou, J. Liu, Effect of high temperature-high pressure treatment on microstructure and mechanical properties of Cu-Cr alloy, Mater. Res. Express. 7 (2020) 026505. https://doi.org/10.1088/2053-1591/ab6c10.

[3] M. Kawasaki, B. Ahn, H. Lee, A.P. Zhilyaev, T.G. Langdon, Using high-pressure torsion to process an aluminum–magnesium nanocomposite through diffusion bonding, J. Mater. Res. 31 (2016) 88–99. https://doi.org/10.1557/jmr.2015.257.

[4] A. Bartkowska, P. Bazarnik, Y. Huang, M. Lewandowska, T.G. Langdon, Using high-pressure torsion to fabricate an Al–Ti hybrid system with exceptional mechanical properties, Materials Science and Engineering: A. 799 (2021) 140114. https://doi.org/10.1016/j.msea.2020.140114.

[5] M.J. Kriegel, M.H. Wetzel, O. Fabrichnaya, D. Rafaja, Binary Ti–Fe system. Part II: Modelling of pressure-dependent phase stabilities, Calphad. 76 (2022) 102383. https://doi.org/10.1016/j.calphad.2021.102383.

[6] T. Hammerschmidt, I.A. Abrikosov, D. Alfè, S.G. Fries, L. Höglund, M.H.G. Jacobs, J. Koßmann, X.-G. Lu, G. Paul, Including the effects of pressure and stress in thermodynamic functions: Pressure and stress in thermodynamic functions, Phys. Status Solidi B. 251 (2014) 81–96. https://doi.org/10.1002/pssb.201350156.

[7] Y.-L. He, X.-G. Lu, N.-Q. Zhu, B. Sundman, CALPHAD modeling of molar volume, Chin. Sci. Bull. 59 (2014) 1646–1651. https://doi.org/10.1007/s11434-014-0218-5.

[8] X.-G. Lu, Q. Chen, A CALPHAD Helmholtz energy approach to calculate thermodynamic and thermophysical properties of fcc Cu, Philosophical Magazine. 89 (2009) 2167–2194. https://doi.org/10.1080/14786430903059004.

[9] A.F. Guillermet, Critical evaluation of the thermodynamic properties of molybdenum, Int J Thermophys. 6 (1985) 367–393. https://doi.org/10.1007/BF00500269.

[10] A. Karbasi, S.K. Saxena, R. Hrubiak, The thermodynamics of several elements at high pressure, Calphad. 35 (2011) 72–81. https://doi.org/10.1016/j.calphad.2010.11.007.
 

[11] E. Brosh, G. Makov, R.Z. Shneck, Application of CALPHAD to high pressures, Calphad. 31 (2007) 173–185. https://doi.org/10.1016/j.calphad.2006.12.008.

[12] J.-O. Andersson, A.F. Guillermet, P. Gustafson, M. Hillert, B. Jansson, B. Jönsson, B. Sundman, J. Ågren, A new method of describing lattice stabilities, Calphad. 11 (1987) 93–98. https://doi.org/10.1016/0364-5916(87)90022-8.

[13] J.-M. Joubert, J.-C. Crivello, G. Deffrennes, Modification of Lu’s (2005) high pressure model for improved high pressure/high temperature extrapolations. Part I: Modeling of platinum at high pressure/high temperature, Calphad. 74 (2021) 102304. https://doi.org/10.1016/j.calphad.2021.102304.

[14] R. Grover, I.C. Getting, G.C. Kennedy, Simple Compressibility Relation for Solids, Phys. Rev. B. 7 (1973) 567–571. https://doi.org/10.1103/PhysRevB.7.567.

[15] X.-G. Lu, M. Selleby, B. Sundman, Implementation of a new model for pressure dependence of condensed phases in Thermo-Calc, Calphad. 29 (2005) 49–55. https://doi.org/10.1016/j.calphad.2005.04.001.

[16] M.H.G. Jacobs, H.A.J. Oonk, A new equation of state based on Grover, Getting and Kennedy’s empirical relation between volume and bulk modulus. The high-pressure thermodynamics of MgO, Phys. Chem. Chem. Phys. 2 (2000) 2641–2646. https://doi.org/10.1039/a910247g.

[17] M.H.G. Jacobs, H.A.J. Oonk, A realistic equation of state for solids. The high pressure and high temperature thermodynamic properties of MGO, Calphad. 24 (2000) 133–147. https://doi.org/10.1016/S0364-5916(00)00019-5.

[18] M.H.G. Jacobs, H.A.J. Oonk, The Gibbs energy formulation of the  \( \alpha \) ,  \( \beta \) , and  \( \gamma \)  forms of Mg2SiO4 using Grover, Getting and Kennedy’s empirical relation between volume and bulk modulus, Physics and Chemistry of Minerals. 28 (2001) 572–585. https://doi.org/10.1007/s002690100180.

[19] M.H.G. Jacobs, B.H.W.S. de Jong, H.A.J. Oonk, The Gibbs energy formulation of  \( \alpha \) ,  \( \gamma \) , and liquid Fe2SiO4 using Grover, Getting, and Kennedy’s empirical relation between volume and bulk modulus, Geochimica et Cosmochimica Acta. 65 (2001) 4231–4242. https://doi.org/10.1016/S0016-7037(01)00694-9.

[20] K. Anand, M.P. Singh, B.S. Sharma, Analysis of V–P–T relationships and bulk modulus for some geophysically-relevant solids using the Grover–Saxena equation of state, Journal of Physics and Chemistry of Solids. 134 (2019) 121–126. https://doi.org/10.1016/j.jpcs.2019.05.039.

[21] S.K. Saxena, Pressure–volume equation of state for solids, Journal of Physics and Chemistry of Solids. 65 (2004) 1561–1563. https://doi.org/10.1016/j.jpcs.2004.02.003.

[22] G. Grimvall, B. Magyarí-Köpe, V. Ozolins, K.A. Persson, Lattice instabilities in metallic elements, Rev. Mod. Phys. 84 (2012) 945–986. https://doi.org/10.1103/RevModPhys.84.945.

[23] S. Bigdeli, L.-F. Zhu, A. Glensk, B. Grabowski, B. Lindahl, T. Hickel, M. Selleby, An insight into using DFT data for Calphad modeling of solid phases in the third generation of Calphad databases, a case study for Al, Calphad. 65 (2019) 79–85. https://doi.org/10.1016/j.calphad.2019.02.008.

[24] G. Deffrennes, B. Oudot, A self-consistent model to describe the temperature dependence of the bulk modulus, thermal expansion and molar volume compatible with 3rd generation CALPHAD databases, Calphad. 74 (2021) 102291. https://doi.org/10.1016/j.calphad.2021.102291.

[25] B. Sundman, U.R. Kattner, M. Hillert, M. Selleby, J. Ågren, S. Bigdeli, Q. Chen, A. Dinsdale, B. Hallstedt, A. Khvan, H. Mao, R. Otis, A method for handling the extrapolation of solid crystalline phases to temperatures far above their melting point, Calphad. 68 (2020) 101737. https://doi.org/10.1016/j.calphad.2020.101737.
 

[26] E.R. Jette, E.B. Gebert, An X-Ray Study of the Binary Alloys of Silicon with Ag, Au, Pb, Sn, Zn, Cd, Sb and Bi, The Journal of Chemical Physics. 1 (1933) 753–755. https://doi.org/10.1063/1.1749242.

[27] J.A. Lee, G.V. Raynor, The Lattice Spacings of Binary Tin-Rich Alloys, Proc. Phys. Soc. B. 67 (1954) 737–747. https://doi.org/10.1088/0370-1301/67/10/301.

[28] M.E. Straumanis, The Precision Determination of Lattice Constants by the Powder and Rotating Crystal Methods and Applications, Journal of Applied Physics. 20 (1949) 726–734. https://doi.org/10.1063/1.1698520.

[29] V.T. Deshpande, D.B. Sirdeshmukh, Thermal expansion of tetragonal tin, Acta Cryst. 14 (1961) 355–356. https://doi.org/10.1107/S0365110X61001212.

[30] V.T. Deshpande, D.B. Sirdeshmukh, Thermal expansion of tin in the  \( \beta-\gamma \)  transition region, Acta Cryst. 15 (1962) 294–295. https://doi.org/10.1107/S0365110X62000742.

[31] W.J. Helfrich, R.A. Dodd, Densities and lattice parameters of tin (indium) solid solutions, Acta Metallurgica. 12 (1964) 667–669. https://doi.org/10.1016/0001-6160(64)90039-2.

[32] J.A. Rayne, B.S. Chandrasekhar, Elastic Constants of  \( \beta \)  Tin from 4.2°K to 300°K, Phys. Rev. 120 (1960) 1658–1663. https://doi.org/10.1103/PhysRev.120.1658.

[33] R. Balzer, H. Sigvaldason, Equilibrium vacancy concentration measurements on tin single crystals, Phys. Stat. Sol. (b). 92 (1979) 143–147. https://doi.org/10.1002/pssb.2220920116.

[34] H. Olijnyk, W.B. Holzapfel, PHASE TRANSITIONS IN Si, Ge AND Sn UNDER PRESSURE, J. Phys. Colloques. 45 (1984) C8-153-C8-156. https://doi.org/10.1051/jphyscol:1984828.

[35] M. Liu, L.-G. Lui, Compressions and phase transitions of tin to half a megabar, High Temp. - High Press. 18 (1986) 79–85.

[36] N. Oehl, G. Schmueling, M. Knipper, R. Kloepsch, T. Placke, J. Kolny-Olesiak, T. Plaggenborg, M. Winter, J. Parisi, In situ X-ray diffraction study on the formation of  \( \alpha \) -Sn in nanocrystalline Sn-based electrodes for lithium-ion batteries, CrystEngComm. 17 (2015) 8500–8504. https://doi.org/10.1039/C5CE01841B.

[37] M.C. Allison, M. Avdeev, S. Schmid, S. Liu, T. Söhnel, C.D. Ling, Synthesis, structure and geometrically frustrated magnetism of the layered oxide-stannide compounds Fe(Fe 3–xMnx)Si2Sn7O16, Dalton Trans. 45 (2016) 9689–9694. https://doi.org/10.1039/C6DT01074A.

[38] H.G. Dorsey, Coefficient of Linear Expansion at Low Temperatures, Phys. Rev. (Series I). 25 (1907) 88–102. https://doi.org/10.1103/PhysRevSeriesI.25.88.

[39] P.W. Bridgman, Certain Physical Properties of Single Crystals of Tungsten, Antimony, Bismuth, Tellurium, Cadmium, Zinc, and Tin, Proceedings of the American Academy of Arts and Sciences. 60 (1925) 305. https://doi.org/10.2307/25130058.

[40] G. Shinoda, X-Ray Investigations on the Thermal Expansion of Solids (Part 1), Memoirs of the College of Science, Kyoto Imperial University. Series A. 16 (1933) 193–201.

[41] G. Grube, H. Voßkühler, Elektrische Leitfähigkeit und Zustandsdiagramm bei Binären Legierungen. 13. Mitteilung. Über Mischkristallbildung Im System Magnesium-Zinn, Ztschr. Elektrochem. Bd. 40 (1934) 566–570. https://doi.org/10.1002/bbpc.19340400806.

[42] H.D. Erfling, Studien zur thermischen Ausdehnung fester Stoffe in tiefer Temperatur. II (Cr,  \( \beta \) -Mn, Mo, Rh, Be, Graphit, Tl, Zr, Bi, Sb, Sn und Beryll), Ann. Phys. 426 (1939) 136–160. https://doi.org/10.1002/andp.19394260204.

[43] B.G. Childs, S. Weintroub, The Measurement of the Thermal Expansion of Single Crystals of Tin by an Interferometric Method, Proc. Phys. Soc. B. 63 (1950) 267–277. https://doi.org/10.1088/0370-1301/63/4/303.
 

[44] E.V. Vernon, S. Weintroub, The Measurement of the Thermal Expansion of Single Crystals of Indium and Tin with a Photoelectric Recording Dilatometer, Proc. Phys. Soc. B. 66 (1953) 887–894. https://doi.org/10.1088/0370-1301/66/10/309.

[45] G.K. White, Thermal expansion of anisotropic metals at low temperatures, Physics Letters. 8 (1964) 294–295. https://doi.org/10.1016/S0031-9163(64)80002-0.

[46] L.J. Balasundaram, A.N. Sinha, Thermal Expansion of Lead-Tin and Lead-Cadmium Alloys, Journal of Applied Physics. 42 (1971) 5207–5207. https://doi.org/10.1063/1.1659926.

[47] M.A. Current, Vacancy Concentrations in Zinc and tin, Faculty of Rensselaer polytechnic Institute, 1974.

[48] L.C. Cardinal, NRL Problem No: F03-01, Report of NRL Progress, Naval Research Laboratory. (1963) 31.

[49] E.W. Kammer, L.C. Cardinal, C.L. Vold, M.E. Glicksman, The elastic constants for single-crystal bismuth and tin from room temperature to the melting point, J. Phys. Chem. Solids. 33 (1972) 1891–1989. https://doi.org/10.1016/S0022-3697(72)80487-6.

[50] X. Du, J.-C. Zhao, Facile measurement of single-crystal elastic constants from polycrystalline samples, Npj Comput Mater. 3 (2017) 17. https://doi.org/10.1038/s41524-017-0019-x.

[51] N. Rambert, B. Sitaud, P. Faure, Equation d'état multiphase et courbe de fusion de l'étain sous pression : une nouvelle approche expérimentale, Rapport CEA A-22F00-00-10. (2003).

[52] A. Salamat, R. Briggs, P. Bouvier, S. Petitgirard, A. Dewaele, M.E. Cutler, F. Corà, D. Daisenberger, G. Garbarino, P.F. McMillan, High-pressure structural transformations of Sn up to 138 GPa: Angle-dispersive synchrotron x-ray diffraction study, Phys. Rev. B. 88 (2013) 104104. https://doi.org/10.1103/PhysRevB.88.104104.

[53] L.H. Adams, E.D. Williamson, J. Johnston, THE DETERMINATION OF THE COMPRESSIBILITY OF SOLIDS AT HIGH PRESSURES., J. Am. Chem. Soc. 41 (1919) 12–42. https://doi.org/10.1021/ja01458a002.

[54] P.W. Bridgman, The Compressibility of Thirty Metals as a Function of Pressure and Temperature, Proceedings of the American Academy of Arts and Sciences. 58 (1923) 165. https://doi.org/10.2307/20025987.

[55] P.W. Bridgman, Linear Compressions to 30,000 Kg/Cm \( ^{3} \) , including Relatively Incompressible Substances, Proceedings of the American Academy of Arts and Sciences. 77 (1949) 189. https://doi.org/10.2307/20023541.

[56] S.N. Vaboya, G.C. Kennedy, Compressibility of 18 metals to 45 kbar, Journal of Physics and Chemistry of Solids. 31 (1970) 2329–2345. https://doi.org/10.1016/0022-3697(70)90247-7.

[57] A.V. Khvan, T. Babkina, A.T. Dinsdale, I.A. Uspenskaya, I.V. Fartushna, A.I. Druzhinina, A.B. Syzdykova, M.P. Belov, I.A. Abrikosov, Thermodynamic properties of tin: Part I Experimental investigation, ab-initio modelling of  \( \alpha \) -,  \( \beta \) -phase and a thermodynamic description for pure metal in solid and liquid state from 0 K, Calphad. 65 (2019) 50–72. https://doi.org/10.1016/j.calphad.2019.02.003.

[58] J.N. Brönsted, Stadien zur chemischen Affinität. IX, Zeitschrift Für Physikalische Chemie. 88U (1914). https://doi.org/10.1515/zpch-1914-8833.

[59] W.H. Rodebush, THE ATOMIC HEATS OF CADMIUM AND TIN AT LOW TEMPERATURES, J. Am. Chem. Soc. 45 (1923) 1413–1416. https://doi.org/10.1021/ja01659a011.

[60] F. Lange, Untersuchungen über die spezifische Wärme bei tiefen Temperaturen, Zeitschrift Für Physikalische Chemie. 110U (1924). https://doi.org/10.1515/zpch-1924-11022.
 

[61] H. Klinkhardt, Messung von wahren spezifischen Wärmen bei hohen Temperaturen durch Heizung mit Glühelektronen, Ann. Phys. 389 (1927) 167–200. https://doi.org/10.1002/andp.19273891711.

[62] W.H. Keesom, J.N. van den Ende, The specific heats of solids at temperatures obtainable with liquid helium. IV, Measurements of the atomic heats of tin and zinc, Leiden. Comm. 219b (1932) 143–155.

[63] T.C. Cetas, J.C. Holste, C.A. Swenson, Heat Capacities from 1 to 30 K of Zn, Cd, Sn, Bi, and Y, Phys. Rev. 182 (1969) 679–685. https://doi.org/10.1103/PhysRev.182.679.

[64] W. Kramer, J. Nölting, Anomale spezifische Wärmen und fehlordnung der Metalle indium, Zinn, Blei, Zink, Antimon und Aluminium, Acta Metallurgica. 20 (1972) 1353–1359. https://doi.org/10.1016/0001-6160(72)90070-3.

[65] V.N. Naumov, V.V. Nogteva, I.E. Paukov, Teploemkost, Entropiya Belogo Olova ( \( \beta \) -Sn) s interval 1.8–311 K, J. Phys. Chem. (Russ.). 2 (1978) 497–498.

[66] J.-O. Andersson, T. Helander, L. Höglund, P. Shi, B. Sundman, Thermo-Calc & DICTRA, computational tools for materials science, Calphad. 26 (2002) 273–312. https://doi.org/10.1016/S0364-5916(02)00037-8.

[67] O.L. Anderson, Equations of state of solids for geophysics and ceramic science, Oxford University Press, New York, 1995.

[68] M. Kumar, S.P. Upadhyay, Pressure dependence of thermal expansivity for alkali halides, Journal of Physics and Chemistry of Solids. 54 (1993) 773–776. https://doi.org/10.1016/0022-3697(93)90140-M.

[69] M. Kumar, High pressure equation of state for solids, Physica B: Condensed Matter. 212 (1995) 391–394. https://doi.org/10.1016/0921-4526(95)00361-C.

[70] OrsonL. Anderson, K. Zou, Formulation of the thermodynamic functions for mantle minerals: MgO as an example, Phys Chem Minerals. 16 (1989). https://doi.org/10.1007/BF00223312.

[71] F. Birch, Elasticity and constitution of the Earth’s interior, J. Geophys. Res. 57 (1952) 227–286. https://doi.org/10.1029/JZ057i002p00227.

[72] J.-M. Joubert, J.-C. Crivello, K.V. Yusenko, Modification of Lu’s (2005) high pressure model for improved high pressure/high temperature extrapolations. Part II: Modeling of osmium–platinum system at high pressure/high temperature, Calphad. 74 (2021) 102311. https://doi.org/10.1016/j.calphad.2021.102311.

[73] G. Deffrennes, P. Faure, F. Bottin, J.-M. Joubert, B. Oudot, Tin (Sn) at high pressure: review, X-ray diffraction, DFT calculations, and Gibbs energy modeling, ArXiv Preprint. (2022). https://doi.org/10.48550/ARXIV.2203.16240.

[74] M.H.G. Jacobs, H.A.J. Oonk, Reply to the ‘Comment on “A new equation of state based on Grover, Getting and Kennedy’s empirical relation between volume and bulk modulus. The high-pressure thermodynamics of  \( MgO \) ” by S. Raju, E. Mohandas and K. Sivasubramanian, Phys. Chem. Chem. Phys., 2001, 3, 1391, Phys. Chem. Chem. Phys. 3 (2001) 1394–1395. https://doi.org/10.1039/b101037i.

[75] S. Raju, E. Mohandas, K. Sivasubramanian, Comment on “A new equation of state based on Grover, Getting and Kennedy’s empirical relation between volume and bulk modulus. The high pressure thermodynamics of  \( MgO \) ” by M. H. G. Jacobs and H. A. J. Oonk, Phys. Chem. Chem. Phys., 2000, 2, 2641, Phys. Chem. Chem. Phys. 3 (2001) 1391–1393. https://doi.org/10.1039/b009587g.

[76] G. Deffrennes, N. Jakse, C.M.S. Alvares, I. Nuta, A. Pasturel, A. Khvan, A. Pisch, Thermodynamic modelling of the Ca–O system including 3rd generation description of CaO and CaO \( _{2} \) , Calphad. 69 (2020) 101764. https://doi.org/10.1016/j.calphad.2020.101764.
 

[77] G. Deffrennes, B. Oudot, Data for: A self-consistent model to describe the temperature dependence of the bulk modulus, thermal expansion and molar volume compatible with 3rd generation CALPHAD databases, Mendeley Data, V1. (2021). http://dx.doi.org/10.17632/xskt8cj82b.1.
 

## Supplementary Notes for:

On models to describe the volume in the context of establishing high-pressure Gibbs energy databases

Guillaume Deffrennes \( ^{a,*} \) , Jean-Marc Joubert \( ^{b} \) , Benoit Oudot \( ^{a,*} \) 

 \( ^{a} \)  CEA, DAM, VALDUC, F-21120 Is-sur-Tille, France

 \( ^{b} \)  Univ. Paris Est Creteil, CNRS, ICMPE, UMR 7182, 2 rue Henri Dunant, 94320 Thiais, France

* Corresponding authors:

Dr. Guillaume Deffrennes

Present postal address: National Institute for Materials Science, 1-1 Namiki, Tsukuba, Ibaraki

305-0044, Japan

e-mail : guillaume.deffrennes@gmail.com

Dr. Benoit Oudot

Postal address: CEA, DAM, VALDUC, F-21120 Is-sur-Tille, France

e-mail : benoit.oudot@cea.fr
 

Supplementary Note A: Derivation of the equations presented in section 3 (Lu-Grover model)

How to obtain Eq. (3.1) of the manuscript:

The empirical relationship discovered by Grover et al. [1] was formulated by Lu et al. [2] as follows:

 \[ V=V^{0}-c\ln\left(\frac{K_{T}}{K_{T}^{0}}\right) \quad (A. 1) \] 

with c a material characteristic parameter that can be temperature dependent, and  \( K_{T} \)  the isothermal bulk modulus defined as the inverse of the compressibility  \( \kappa_{T} \)  as follows:

 \[ K_{T}=-V\left(\frac{\partial p}{\partial V}\right)_{T} \quad (A. 2) \] 

By re-arranging Eq. (A.1), and by injecting Eq. (A.2) into the expression, the following differential equation is obtained:

 \[ \frac{\exp\left(-\frac{V^{0}}{c}\right)}{K_{T}^{0}}=-\frac{\exp\left(-\frac{V}{c}\right)}{V}\left(\frac{\partial V}{\partial p}\right)_{T} \quad (A. 3) \] 

Finally, by integrating Eq. (A.3) and re-arranging the resulting expression, Eq. (3.1) from the manuscript is obtained:

 \[ V=-cE i^{-1}\left(E i\left(-\frac{V^{0}}{c}\right)-\frac{1}{K_{T}^{0}}\exp\left(-\frac{V^{0}}{c}\right)(p-p^{0})\right) \quad (3.1) \] 

where Ei is the exponential integral function, that can be calculated numerically from tabulations, and that is defined as:
 

 \[ E i(x)=\int\limits_{-\infty}^{x}\frac{e^{t}}{t}d t \quad (A. 4) \] 

It is noted that Eq. (3.1) differs from the original equation (9) from Lu et al. [2], because the authors actually used the  \( E_{1} \)  function, that was noted Ei, and that is defined only for positive value of x as  \( E_{1}(x) = -Ei(-x) \) .

## How to obtain Eq. (3.3) of the manuscript:

The variations of the product  \( \alpha K_{T} \)  within the Lu-Grover framework can be obtained starting from:

 \[ \left(\frac{\partial(\alpha K_{T})}{\partial p}\right)_{T}=\alpha\left(\frac{\partial K_{T}}{\partial p}\right)_{T}+K_{T}\left(\frac{\partial\alpha}{\partial p}\right)_{T} \quad (A. 5) \] 

Then, from the thermodynamic identity:

 \[ \left(\frac{\partial\alpha}{\partial p}\right)_{T}=\frac{1}{K_{T}{}^{2}}\left(\frac{\partial K_{T}}{\partial T}\right)_{p} \quad (A. 6) \] 

, one obtains the generally valid relationship:

 \[ \left(\frac{\partial(\alpha K_{T})}{\partial p}\right)_{T}=\alpha\left(\frac{\partial K_{T}}{\partial p}\right)_{T}+\frac{1}{K_{T}}\left(\frac{\partial K_{T}}{\partial T}\right)_{p} \quad (A. 7) \] 

In the Lu-Grover equation of state, the pressure derivative of the bulk modulus can be obtained by derivation of Eq. (A.1) as follows:

 \[ \left(\frac{\partial V}{\partial p}\right)_{T}=-\frac{c}{K_{T}}\left(\frac{\partial K_{T}}{\partial p}\right)_{T} \quad (A. 8) \] 

Then, by injecting Eq. (A.2) into Eq. (A.8), one obtains:
 

 \[ \left(\frac{\partial K_{T}}{\partial p}\right)_{T}=\frac{V}{c} \quad (A.9) \] 

The temperature derivative of the bulk modulus can be determined in a very similar manner by derivation of Eq. (A.1), and by injecting the definition of the thermal expansion coefficient into the resulting expression. One finally obtains:

 \[ \left(\frac{\partial K_{T}}{\partial T}\right)_{p}=\frac{K_{T}}{c}\left(V^{0}\alpha^{0}-V\alpha\right)+\frac{K_{T}}{K_{T}{}^{0}}\left(\frac{\partial K_{T}{}^{0}}{\partial T}\right)_{p}-\frac{K_{T}}{c}\ln\left(\frac{K_{T}}{K_{T}{}^{0}}\right)\left(\frac{\partial c}{\partial T}\right)_{p} \quad (A.10) \] 

By injecting Eq. (A.9) and (A.10) into Eq. (A.7), Eq. (3.3) from the manuscript is obtained:

 \[ \left(\frac{\partial\alpha K_{T}}{\partial p}\right)_{T}=\frac{V^{0}\alpha^{0}}{c}+\frac{1}{K_{T}{}^{0}}\left(\frac{\partial K_{T}{}^{0}}{\partial T}\right)_{p}-\frac{1}{c}\ln\left(\frac{K_{T}{}_{0}}{K_{T}{}^{0}}\right)\left(\frac{\partial c}{\partial T}\right)_{p} \quad (3.3) \]
 

Supplementary Note B: Description at atmospheric pressure of the volume, thermal expansion and heat capacity of  \( \beta \) -Sn accepted in this work compared with experiments

![](./images/867748583355449772_22.jpg)

(a)

![](./images/867748583355449772_23.jpg)

(b)

![](./images/867748583355449772_24.jpg)

(c)

Fig. S1 – Atmospheric pressure description of (a) the volume, (b) the thermal expansion, and (c) the heat capacity of  \( \beta \) -Sn that is used in the various models investigated in this work compared with experimental data. The description of the heat capacity is further supported by heat content data as shown in [4].
 

Supplementary Note C: Agreement between calculations and experimental data for  \( \beta \) -Sn when the Lu-Grover model presented in Section 3 is used

![](./images/867748583355449772_25.jpg)

(a)

![](./images/867748583355449772_26.jpg)

(b)

![](./images/867748583355449772_27.jpg)

(c)

Fig. S2 – Bulk modulus along (a) the  \( 10^{5} \)  Pa isobar and (b) the 298.15 K isotherm and (c) molar volume along the 298.15K isotherm as calculated using the Lu-Grover model compared with experimental data
 

Supplementary Note D: The Joubert-Lu-Grover approach (Section 4) adapted to the  \( 3^{rd} \)  generation model for the thermal expansion and bulk modulus from [3]

First of all, following Eq. (4.2) of the manuscript, a cut-off parameter was applied to the parameter governing the temperature dependence of the bulk modulus as follows:

 \[ K_{T}{}^{0}=\frac{1}{\chi_{T_{0}}+C(p)\sum_{i}\frac{a_{i}}{\exp\left(\frac{\theta_{i}}{T}\right)-1}} \quad (C. 1) \] 

 \[ C(p)=C\exp\left(-\frac{p}{p_{CUT}}\right) \quad (C. 2) \] 

with  \( \chi_{T_{0}} \)  the compressibility at the reference temperature, C a material-dependent parameter that does not vary with T and should not be confused with the Lu-Grover parameter c,  \( \theta_{i} \)  the Einstein temperature associated with the  \( i^{th} \)  Einstein mode of vibration, and  \( a_{i} \)  the corresponding pre-factor.

Then, in [3], the thermal expansion coefficient is expressed from the description of the bulk modulus and of the isochoric heat capacity. The first cutoff parameter noted  \( p_{CUT}' \)  in Eq. (4.1) and applied to the constant parameter in the  \( 2^{nd} \)  generation description was transposed to the harmonic contribution to the heat capacity, which is also constant above the Einstein temperature. The second cutoff parameter noted  \( p_{CUT} \)  in Eq. (4.1) was applied to the anharmonic and electronic contributions to the heat capacity, which gives the increase in the thermal expansion coefficient at high temperature. Finally, the following expression was obtained:
 

 \[ \begin{aligned}\alpha(T)=\frac{3R}{V_{0}}\sum_{i}\gamma_{i_{0}}a_{i}\left(\left(\frac{\theta_{i}}{T}\right)^{2}\frac{e^{\frac{\theta_{i}}{\theta_{i}}}}{\left(e^{\frac{\theta_{j}}{T}}-1\right)^{2}}\exp\left(-\frac{p}{p_{CUT}}\right)\left(\chi_{T_{0}}+\frac{C(p)}{e^{\frac{\theta_{i}}{\theta_{i}}}-1}\right)\right.\\ \left.+\left((AT+BT^{2})\exp\left(-\frac{p}{p_{CUT}}\right)\left(\chi_{T_{0}}+C(p)\left(\frac{T}{\theta_{i}}-\frac{1}{2}\right)\right)\right)\right)\\ \end{aligned} \quad (C.3) \] 

with R the gas constant,  \( V_{0} \)  the molar volume at the reference temperature,  \( \gamma_{i_{0}} \)  the Grüneisen parameter associated with the  \( i^{th} \)  Einstein mode of vibration, and A and B phenomenological parameters to account for anharmonic and electronic contributions to the heat capacity.
 

Supplementary Note E: Agreement between calculations and experimental data for  \( \beta \) -Sn when the Joubert-Lu-Grover model presented in Section 4 is used

![](./images/867748583355449772_28.jpg)

(a)

![](./images/867748583355449772_29.jpg)

(b)

![](./images/867748583355449772_30.jpg)

(c)

Fig. S3 – Bulk modulus along (a) the  \( 10^{5} \)  Pa isobar and (b) the 298.15 K isotherm and (c) molar volume along the 298.15K isotherm as calculated using the Joubert-Lu-Grover model compared with experimental data
 

Supplementary Note F: Derivation of the equations presented in Section 5 (Jacobs-Grover model)

How to obtain Eq. (5.5) of the manuscript:

Following the same approach that previously led to Eq. (A.9), it can be shown starting from Eq. (5.2) of the manuscript that the expression of  \( (\partial K_{T}/\partial p)_{T} \)  is unchanged from the framework of the Lu-Grover equation of state.

Then, the temperature derivative of the bulk modulus is obtained by derivation of Eq. (5.2), and by injecting the definition of the thermal expansion coefficient into the resulting expression, the following equation is obtained:

 \[ \left(\frac{\partial K_{T}}{\partial T}\right)_{p}=\frac{K_{T}}{c}\left(a-V\alpha\right) \quad (E. 1) \] 

Finally, by injecting Eq. (A.9) and (E.1) into Eq. (A.7), Eq. (5.5) of the manuscript is obtained.

How to obtain Eq. (5.6) of the manuscript:

Eq. (5.6) of the manuscript can be either obtained by derivation of Eq. (5.2), or by injecting Eq. (A.9) and (E.1) into the thermodynamic identity:

 \[ \left(\frac{\partial K_{T}}{\partial T}\right)_{V}=\left(\frac{\partial K_{T}}{\partial T}\right)_{p}+\alpha K_{T}\left(\frac{\partial K_{T}}{\partial p}\right)_{T} \quad (E. 2) \]
 

Supplementary Note G: Agreement between calculations and experimental data for  \( \beta \) -Sn when the revised Jacobs-Grover model presented in Section 6 is used

![](./images/867748583355449772_31.jpg)

(a)

![](./images/867748583355449772_32.jpg)

(b)

![](./images/867748583355449772_33.jpg)

(c)

Fig. S4 – Bulk modulus along (a) the  \( 10^{5} \)  Pa isobar and (b) the 298.15 K isotherm and (c) molar volume along the 298.15K isotherm as calculated using the revised Jacobs-Grover model compared with experimental data
 

Supplementary Note H: Agreement between calculations and experimental data for  \( \beta \) -Sn when the model based on thermal pressure presented in Section 7 is used

![](./images/867748583355449772_34.jpg)

(a)

![](./images/867748583355449772_35.jpg)

(b)

![](./images/867748583355449772_36.jpg)

(c)

Fig. S5 – Bulk modulus along (a) the  \( 10^{5} \)  Pa isobar and (b) the 298.15 K isotherm and (c) molar volume along the 298.15K isotherm as calculated using the model based on thermal pressure presented in Section 7 compared with experimental data
 

Supplementary Note I: Agreement between calculations and experimental data for  \( \beta \) -Sn when the new scheme presented in Section 8 is used

![](./images/867748583355449772_37.jpg)

(a)

![](./images/867748583355449772_38.jpg)

(b)

![](./images/867748583355449772_39.jpg)

(c)

Fig. S6 – Bulk modulus along (a) the  \( 10^{5} \)  Pa isobar and (b) the 298.15 K isotherm and (c) molar volume along the 298.15K isotherm as calculated using the new scheme presented in section 8 compared with experimental data. The pressure derivative discontinuity observed in (b) for  \( K_{T} \)  is discussed in more details in the manuscript (Section 8).
 
