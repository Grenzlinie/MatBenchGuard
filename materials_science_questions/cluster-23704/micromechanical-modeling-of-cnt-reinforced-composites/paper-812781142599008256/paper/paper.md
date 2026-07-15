# A new form of a Halpin–Tsai micromechanical model for characterizing the mechanical properties of carbon nanotube-reinforced polymer nanocomposites

**MOHAMMAD KAZEM HASSANZADEH-AGHDAM¹,*** and JAMALODDIN JAMALI²

¹Department of Mechanical Engineering, Ayandegan Institute of Higher Education, P.O. Box 76963, Tonekabon, Iran
²College of Engineering and Technology, American University of the Middle East, P.O. Box 15453, Eqaila, Kuwait
*Author for correspondence (Mk.hassanzadeh@gmail.com)

MS received 9 January 2018; accepted 5 November 2018

## Abstract
In the present work, a new form of a Halpin–Tsai (H–T) micromechanical model is proposed to characterize the elastic modulus and tensile strength of carbon nanotube (CNT)-reinforced polymer nanocomposites. To this end, three critical factors, including random dispersion, non-straight shape and agglomerated state of the CNTs are appropriately incorporated into the H–T model. A comparison of the model predictions with some experiments on the CNT/polymer nanocomposites serves to verify the applicability of the proposed approach. It is found that the present predictions are in good agreement with the available experimental data. The results clearly reveal that for a more accurate prediction of the mechanical properties of the CNT/polymer nanocomposites, considering the random orientation, waviness and agglomeration of CNTs into the polymer matrix is critically essential. Also, some parametric studies are carried out to show the effects of volume fraction, non-straight shape, aspect ratio, mechanical characteristics and non-uniform dispersion of CNTs as well as matrix properties on the elastic modulus and tensile strength of CNT/polymer nanocomposites. The results reveal that it is necessary to eliminate the agglomeration and use the straight CNTs if the full potential of CNT reinforcement is to be realized.

**Keywords.** Nanocomposite; carbon nanotube; mechanical properties; Halpin–Tsai model; agglomeration.

## 1. Introduction
Carbon nanotubes (CNTs) are known to have excellent mechanical stiffness and strength [1–3]. A review of the computational studies has shown that the CNT elastic modulus can be in the range of 0.5–5.5 TPa [4–6]. In an experimental research work, Treacy *et al* [7] attained the elastic modulus of CNTs ranging from 0.4 to 4.15 TPa with an average of 1.8 TPa. The tensile strength of CNTs can be as high as 100 GPa [8]. Additionally, the CNTs have a very low coefficient of thermal expansion (CTE) and high thermal and electrical conductivities [9–12]. Consequently, the CNTs have emerged as the remarkable reinforcement materials for polymer matrix nanocomposites (PMNCs) mainly due to their excellent properties [13–15].

Over the past decade, considerable research studies have been performed on the mechanical behaviour of CNT/polymer nanocomposites. For example, Schadler *et al* [16] reported that with 5% weight addition of CNTs into the epoxy matrix, the nanocomposite elastic modulus can be improved by as much as 20% in tension and 25% in compression in comparison with that of the pure resin. Qian *et al* [17] found that the addition of 1 wt.% CNTs into a polystyrene matrix enhances Young’s modulus of the nanocomposite by 36–42% and the tensile strength by 25%. Also, Allaoui *et al* [18] observed twice and triple improvements in the nanocomposite elastic modulus and yield strength, respectively, with the addition of 1 wt.% CNTs into epoxy resin. Tai *et al* [19] indicated a double enhancement in the tensile strength of the CNT-reinforced phenolic nanocomposites by adding 3 wt.% CNTs into the phenolic resin. Based on the experimental observation of Sahoo *et al* [20], the reinforcement with CNTs significantly improves the mechanical characteristics of the shape memory polymer (SMP) nanocomposites. As compared to the pure polyurethane (PU) matrix, a 200% increase in the elastic modulus and a 37% increase in the tensile strength of the PU nanocomposite containing 2.5 wt.% CNTs have been observed [20]. Experimental outcomes of Omidi *et al* [21] have indicated that the elastic modulus and the tensile strength of the polymer nanocomposites can be considerably enhanced by adding a small percentage of CNTs. It was found that only a 3 wt.% CNT addition can increase the elastic modulus and the tensile strength of the epoxy nanocomposite up to 43.1 and 55.2%, respectively, in comparison with that of the pure epoxy resin [21].

It is well established that the efficiency of the reinforcement in the effective properties of CNT-reinforced nanocomposite materials strongly depends on various factors such as content, geometry, dispersion type and properties of CNTs [22–25]. From an experimental point of view, it is difficult to attain

comprehensive knowledge on the effects of these factors on the final nanocomposite effective properties. Generally, the experimental methods to evaluate the overall behaviour of nanocomposite materials are time-consuming and the results depend on the accessibility of CNTs with controlled shape and size. Furthermore, the quality of the experimental outcomes is critically dependent on the ability in preparing homogeneous nanocomposites with controlled dispersion of CNTs [26–28]. It should be noted that one of the common features of CNT morphology is the formation of a CNT agglomerated state into the matrix which is highly undesirable [29–31]. In this frame, the utilization of analytical and numerical methods appears promising [32–34].

Several micromechanical models have been proposed to predict the mechanical properties of the CNT-reinforced nanocomposites [35–37]. For example, Fisher *et al* [38] proposed a model combining finite element (FE) and rule of mixture (ROM) micromechanical methods to calculate the elastic modulus of PMNCs reinforced with wavy CNTs. They concluded that even a slight CNT curvature greatly decreases the effective reinforcement when compared to straight CNTs [38]. By the use of the Halpin–Tsai (H–T) micromechanical model, Thostenson and Chou [39] found that the elastic properties of CNT/polystyrene nanocomposites are sensitive to the CNT diameter. In another study, Anumandla and Gibson [40] developed a closed form micromechanics scheme to predict the Young’s modulus of polymer nanocomposites containing CNTs. The influences of volume fraction, curvature and length of CNTs on the elastic response of nanocomposites were examined [40]. Also, Seidel and Lagoudas [41] employed the composite cylinder approach (CCA), and the self-consistent Mori–Tanaka (M–T) methods to determine Young’s modulus, Poisson’s ratio and shear modulus of a nanocomposite consisting of aligned CNTs embedded in a polymer matrix. The mechanical behaviour of CNT/polyethylene nanocomposites was evaluated by Kanagaraj *et al* [42] using the H–T model and a modified form of the ROM. Moreover, Bokobza [43] applied the Guth and the H–T models to calculate the elastic modulus of elastomeric nanocomposites reinforced with CNTs. Also, the M–T scheme was used to study the elastic response of SMP nanocomposites containing randomly oriented CNTs [44]. The role of CNT waviness in the elastic modulus of SMP nanocomposites was examined [44]. The outcomes showed that the waviness can drastically decrease the stiffening effect of the CNTs and is an important factor influencing the reinforcing efficiency [44]. Ma *et al* [45] used some simple analytical models, including ROM, H–T and shear lag approaches to obtain the elastic properties of CNT/polymer nanocomposites. Also, a literature survey clearly indicates that the ROM has been extensively employed to predict the effective thermo-mechanical characteristics of PMNCs reinforced with aligned straight CNTs [46–48]. In another theoretical study, Mahmoodi and Vakilifard [49] developed a unit cell micromechanical model to investigate the electro-thermo-elastic properties of the aligned straight CNT-reinforced smart nanocomposites. The influences of volume fraction, orientation and aspect ratio on the nanocomposite effective properties were studied [49]. Yengejeh *et al* [50] carried out an excellent survey of the research studies on different modelling methods to calculate the thermo-elastic properties of CNT/polymer nanocomposites.

The main objective of the present study is to present a new form of the H–T micromechanical method for a more accurate prediction of the elastic modulus and tensile strength of the CNT/polymer nanocomposites by adopting the CNT orientation, waviness and agglomeration factors in the model. Comparative studies are performed with available experimental data in the literature to verify the efficiency of the presented new form of the H–T model. Then, several parametric studies are conducted to examine the influences of the volume fraction, non-straight shape, aspect ratio, mechanical characteristics, and non-uniform dispersion of CNTs as well as matrix properties on both the elastic modulus and tensile strength of CNT/polymer nanocomposites. The presented results could be beneficial to guide the modelling and the design of a wide range of PMNCs containing CNTs.

## 2. New form of H–T model

Generally, most of the proposed models for predicting the mechanical characteristics of CNT/polymer nanocomposites are valid only for a low range of CNT wt.% [45–49,51–53]. At low content of CNTs, the variation of the elastic modulus and the strength of polymer nanocomposites with a CNT weight fraction are nearly linear. However, the experimental results obviously indicated a nonlinear increase in the mechanical properties of CNT/polymer nanocomposites for a high range of CNT content [21]. As has been extensively reported by previous researchers [29–31], current processing techniques often lead to an agglomerated state for the CNTs. So, the dispersion of CNTs into the polymer nanocomposites cannot be entirely uniform. Besides, another fundamental aspect which influences the overall behaviour of a nanocomposite is CNT waviness [14,38]. The CNT waviness is inherent to the manufacturing process of CNT/polymer nanocomposites. According to the scanning electron microscopy (SEM) and transmission electron microscopy (TEM) images, CNTs remain vastly curved when they are embedded in the polymer matrix [17,38]. Consequently, an acceptable micromechanical model must consider the non-straight shape and agglomeration of CNTs.

### 2.1 Elastic modulus

The dependence of the mechanical response of CNT-reinforced polymer nanocomposites on the volume fraction and aspect ratio (length/diameter) of CNTs and constituent material properties can be estimated by the H–T micromechanical method [42,43,45]. The elastic modulus of an

aligned straight CNT-reinforced polymer nanocomposite can be calculated by using the H-T micromechanical model, as follows [42,43,45,54,55].

$$
E = E_{\mathrm{m}} \frac{1+2 R \delta V_{\mathrm{CNT}}}{1-\delta V_{\mathrm{CNT}}}, \quad R = \frac{L_{\mathrm{CNT}}}{d_{\mathrm{CNT}}}, \tag{1}
$$

in which

$$
\delta = \frac{(E_{\mathrm{CNT}}/E_{\mathrm{m}})-1}{(E_{\mathrm{CNT}}/E_{\mathrm{m}})+2 R}, \tag{2}
$$

where $E_{\mathrm{m}}$ and $E_{\mathrm{CNT}}$ denote the elastic modulus of the polymer matrix and CNT, respectively. Also, $V_{\mathrm{CNT}}$, $L_{\mathrm{CNT}}$ and $d_{\mathrm{CNT}}$ specify the volume fraction, length and diameter of the CNT, respectively.

As mentioned above, the presented model by equation (1) is only able to predict the elastic modulus of straight aligned CNT-reinforced nanocomposites as shown in figure 1. The H-T model assumes a uniform dispersion of the CNTs into the polymer matrix. Thus, an orientation factor $f_{\mathrm{R}}$ is added to equation (2) to account the random orientation of CNTs into the nanocomposites. It is assumed that the CNTs are randomly oriented in two dimensions when the CNT length is greater than the specimen thickness resulting in $f_{\mathrm{R}}=1/3$ [56] as indicated in figure 2a. Also, the CNTs are supposed to be randomly oriented in three dimensions if the CNT length is much smaller than the specimen thickness leading to $f_{\mathrm{R}}=1/6$ [56] as illustrated in figure 2b. So, one can write

$$
\delta = \frac{(f_{\mathrm{R}} E_{\mathrm{CNT}}/E_{\mathrm{m}})-1}{(f_{\mathrm{R}} E_{\mathrm{CNT}}/E_{\mathrm{m}})+2 R}. \tag{3}
$$

![](./images/812781142599008256_1.jpg)

Figure 1. A schematic of straight aligned CNT-reinforced nanocomposites.

In the present work, the CNTs are assumed to be randomly oriented in three dimensions. Therefore, the orientation factor $f_{\mathrm{R}}=1/6$ is selected to modify the H-T model [56].

Also, the waviness of CNTs is an important factor in deter- mining Young's modulus of CNT/polymer nanocomposites [17,38,57]. Therefore, it is necessary to consider a waviness efficiency factor $f_{\mathrm{W}}$ in equation (3), as follows

$$
\delta = \frac{(f_{\mathrm{R}} f_{\mathrm{W}} E_{\mathrm{CNT}}/E_{\mathrm{m}})-1}{(f_{\mathrm{R}} f_{\mathrm{W}} E_{\mathrm{CNT}}/E_{\mathrm{m}})+2 R}, \quad f_{\mathrm{W}} = 1-\left(\frac{A}{W}\right), \tag{4}
$$

where $A$ and $W$ stand for the amplitude and half-wavelength of a wavy CNT, respectively, as illustrated in figure 3. It should be noted that the state of waviness of both single- and multi-walled CNTs can be modelled using equation (4).

The H-T micromechanical model is further modified to cover the CNT agglomerated state in the polymer matrix.

![](./images/812781142599008256_2.jpg)

Figure 2. A schematic of (a) a nanocomposite reinforced with randomly oriented CNTs in two dimensions, $f_{\mathrm{R}}=1/3$ and (b) a nanocomposite reinforced with randomly oriented CNTs in three dimensions, $f_{\mathrm{R}}=1/6$.

![](./images/812781142599008256_3.jpg)

Figure 3. The model of a wavy CNT.

Thus, an agglomeration efficiency factor $f_{\mathrm{A}}$ is added to equation (4), as follows

$$
\begin{aligned}
\delta &=\frac{\left(f_{\mathrm{R}} f_{\mathrm{W}} f_{\mathrm{A}} E_{\mathrm{CNT}} / E_{\mathrm{m}}\right)-1}{\left(f_{\mathrm{R}} f_{\mathrm{W}} f_{\mathrm{A}} E_{\mathrm{CNT}} / E_{\mathrm{m}}\right)+2 R}, \quad f_{\mathrm{A}}=\exp \left(-\alpha V_{\mathrm{CNT}}^{\beta}\right), \\
&(5)
\end{aligned}
$$

where parameters $\alpha$ and $\beta$ are related to the degree of CNT agglomeration.

### 2.2 Tensile strength
Similar to the elastic modulus, the H–T micromechanical model can be employed to predict the tensile strength of CNT- reinforced polymer nanocomposites. By the use of equations (1)–(5), the new form of the H–T method to determine the nanocomposite tensile strength $S$ can be expressed as

$$
\begin{aligned}
S=S_{\mathrm{m}} \frac{1+2 R \delta V_{\mathrm{CNT}}}{1-\delta V_{\mathrm{CNT}}}, \quad \delta=\frac{\left(f_{\mathrm{R}} f_{\mathrm{W}} f_{\mathrm{A}} S_{\mathrm{CNT}} / E_{\mathrm{m}}\right)-1}{\left(f_{\mathrm{R}} f_{\mathrm{W}} f_{\mathrm{A}} S_{\mathrm{CNT}} / E_{\mathrm{m}}\right)+2 R}, \\
(6)
\end{aligned}
$$

where $S_{\mathrm{m}}$ and $S_{\mathrm{CNT}}$ stand for the tensile strength of the polymer matrix and CNT, respectively.

## 3. Results and discussion
It is desirable to verify the validity of new version of the H–T method as presented in section 2. To this end, the predictions of the new micromechanical model were compared with the available experimental data [21]. A nanocomposite system consisting of multi-walled CNTs embedded into the LY-5052 epoxy resin was fabricated and characterized experimentally by Omidi *et al* [21]. The values of $E_{\mathrm{m}}, E_{\mathrm{CNT}}, S_{\mathrm{m}}, S_{\mathrm{CNT}}, L_{\mathrm{CNT}}$, $d_{\mathrm{CNT}}$ and $f_{\mathrm{W}}$ are equal to 3.11 GPa, 800 GPa, 64.51 MPa, 18 GPa, $2\,\mu$m, 30 nm and 0.6, respectively [21,58]. Also, the values of $\alpha$ and $\beta$ are considered to be 10 and 0.9, respectively. Figure 4 elucidates the comparison between the two sets of results for the CNT/epoxy nanocomposite. The variation of the nanocomposite elastic modulus and tensile strength with the CNT volume fraction is shown in figure 4a and b, respectively. It is observed that the initial form of the H–T model seriously overpredicts the experimental data of nanocomposite mechanical properties [21]. Although the predictions of the H–T model considering random orientation factors are lower than those of the initial form of the H–T model, they are very far from the experimental data [21] as clarified in figure 4a and b. Incorporating the CNT waviness and random orientation factors simultaneously into the H–T model leads to the predictions to be close to the experimental data [21] at low CNT volume fraction $(V_{\mathrm{CNT}} < 1.5\%)$. But, the nanocomposite mechanical properties obtained by the H–T model considering $f_{\mathrm{R}}$ and $f_{\mathrm{W}}$ are still far from the experimental data [21] at higher CNT volume fraction. It can be observed from figure 4 that the new form of the H–T model considering three factors, including random dispersion, non-straight shape and agglomerated state of the CNTs accurately predicts both the elastic modulus and tensile strength of CNT/epoxy nanocomposites. As an important result, to have a more accurate prediction of the CNT/polymer nanocomposite mechanical properties, considering the random orientation, waviness and agglomeration of CNTs is critically essential. Thus, it can be inferred from the comparisons that the presented new version of the H–T micromechanical model can be reliably applied to predict the elastic modulus and tensile strength of CNT-reinforced polymer nanocomposite materials. The results in figure 4a and b exhibits a nonlinear increase in the mechanical properties of epoxy nanocomposites with an increase in the CNT volume fraction which is in agreement with experimental observation [21].

![](./images/812781142599008256_4.jpg)

Figure 4. Comparison between the results of the presented H–T model and experiment [21] in the case of (a) elastic modulus and (b) tensile strength of the CNT/epoxy nanocomposite.

Figure 5a and b illustrates the variation of the elastic modulus and tensile strength of the CNT/epoxy nanocomposite, respectively, with a CNT aspect ratio $(R = L_{\mathrm{CNT}}/d_{\mathrm{CNT}})$. For a comparison purpose, the results are provided in the presence and the absence of CNT agglomeration. It is found that both the elastic modulus and the tensile strength of the epoxy nanocomposite can be significantly improved by increasing

![](./images/812781142599008256_5.jpg)

Figure 5. Variation of (a) the elastic modulus and (b) the tensile strength of the CNT/epoxy nanocomposite with the CNT aspect ratio.

![](./images/812781142599008256_6.jpg)

Figure 6. Variation of (a) the elastic modulus and (b) the tensile strength of the CNT/epoxy nanocomposite with the CNT waviness factor.

the CNT aspect ratio. Also, it is shown that the mechanical properties of CNT/epoxy nanocomposites converge to the threshold value when $R>100$. The effect of the CNT aspect ratio on the mechanical characteristics seems to be more prominent in the absence of CNT agglomeration. For example, on increasing the CNT aspect ratio from 10 to 100, the values of the tensile strength in the presence of agglomeration are about 93 and 108 MPa, respectively, corresponding to a 16.12% increment. However, in the absence of agglomeration, the values of the tensile strength are 103.5 and 141.5 MPa, respectively, corresponding to a 36.7% increment. The results clearly show that the mechanical properties of the polymer nanocomposite without the formation of agglomeration are greatly improved than those of the polymer nanocomposite with agglomeration, especially at a high CNT aspect ratio.

Using the new form of the H–T model, a parametric study is carried out to obtain the mechanical properties of CNT/epoxy nanocomposites for various waviness efficiency factors. The variation of the elastic modulus and tensile strength with the CNT waviness efficiency factor is depicted in figure 6a and b, respectively. The CNT/epoxy nanocomposite mechanical properties are shown to be significantly sensitive to the CNT non-straight shape. It is observed that both the elastic modulus and tensile strength of the CNT/epoxy nanocomposite increase when the CNT waviness efficiency factor increases. In other words, the reduction of $A/W$ leads to an enhancement in the value of mechanical characteristics. As a result, it is necessary to use the straight CNTs if the full potential of CNT reinforcement is to be realized. Moreover, it is noteworthy that the rate of

![](./images/812781142599008256_7.jpg)

Figure 7. Variation of (a) the elastic modulus and (b) the tensile strength of the CNT/epoxy nanocomposite with $\alpha$.

![](./images/812781142599008256_8.jpg)

Figure 8. Variation of (a) the elastic modulus with the CNT elastic modulus and (b) the tensile strength with the CNT tensile strength.

increase in the mechanical properties in the absence of CNT agglomeration is greater than that in the presence of CNT agglomeration.

Figure 7a and b represents the variation of the elastic modulus and tensile strength of the CNT/epoxy nanocomposite, respectively, with $\alpha$. Note that increasing the value of parameter $\alpha$ leads to a greater effect of the CNT agglomerated state on the nanocomposite mechanical behaviour. The results are presented for three different CNT volume fractions, including 3, 5 and 7%. It is found that decreasing the CNT agglomeration enhances the mechanical properties. A uniform dispersion of the CNT into the polymer matrix; i.e., $\alpha = 0$ or $f_{\mathrm{A}} = 1$, leads to the highest nanocomposite elastic modulus and tensile strength. As a result, eliminating the CNT agglomeration is actually essential if the full potential of CNT reinforcement is to be realized. Also, figure 7 shows that with uniform dispersion, the CNT volume fraction can significantly affect the overall mechanical behaviour.

The variation of the CNT/epoxy nanocomposite elastic modulus with the CNT elastic modulus is presented in figure 8a. Also, the plot of the tensile strength of the CNT/epoxy nanocomposite vs. CNT tensile strength is shown in figure 8b. The change of the CNT elastic modulus and tensile strength is in the range of 200–1800 and 15–150 GPa, respectively. As shown in figure 8, the CNT/epoxy nanocomposite mechanical properties can be significantly improved when the mechanical properties of the CNT increase. A nonlinear increase of the nanocomposite tensile strength is

![](./images/812781142599008256_9.jpg)

Figure 9. Variation of (a) the elastic modulus with the matrix elastic modulus and (b) the tensile strength with the matrix tensile strength.

found with increasing CNT tensile strength, as illustrated in figure 8b.

A parametric study is performed in the case of the influence of matrix mechanical properties on the overall mechanical behaviour of the CNT/epoxy nanocomposite. The variation of the nanocomposite elastic modulus with the matrix elas- tic modulus is shown in figure 9a. Furthermore, the plot of the nanocomposite tensile strength vs. matrix tensile strength is shown in figure 9b. It can be seen that the mechanical properties of the CNT/epoxy nanocomposite increase almost linearly as the matrix mechanical properties increase.

## 4. Conclusion

In this paper, by adopting the CNT orientation, waviness and agglomeration factors in the H-T micromechanical model, the mechanical properties of the CNT-reinforced polymer nanocomposites were evaluated. The predictions of the new form of the H-T model were compared to the available experimental data in the literature mainly to verify the suit- ability of the proposed approach. An excellent agreement was observed between the two sets of results. It was found that for a more accurate prediction of the mechanical properties of the CNT/polymer nanocomposites, considering the ran- dom orientation, waviness and agglomeration of CNTs into the polymer matrix is critically essential. Also, the effec- tive elastic modulus and tensile strength of CNT/polymer nanocomposites were found to be very sensitive to the wavi- ness and the agglomeration. To realize the full potential of CNT-reinforcement, using the straight CNTs and providing a more uniform distribution of CNTs are the top priority. Also, the results indicated that by increasing both the CNT volume fraction and aspect ratio, can enhance the mechanical prop- erties of CNT-reinforced polymer nanocomposites.

## References

[1] Saha S and Bal S 2017 *Bull. Mater. Sci.* **40** 956
[2] Imani A and Farzi G 2015 *Bull. Mater. Sci.* **38** 831
[3] Feng C and Jiang L 2013 *Composites, Part A* **47** 149
[4] Yakobson B I, Campbell M P, Brabec C J and Bernholc J 1997 *Comput. Mater. Sci.* **8** 341
[5] Lu J P 1997 *Phys. Rev. Lett.* **79** 1297
[6] Kashyap K T, Koppad P G, Puneeth K B, Ram H A and Mallikarjuna H M 2011 *Comput. Mater. Sci.* **50** 2493
[7] Treacy M J, Ebbesen T W and Gibson J M 1996 *Nature* **381** 678
[8] Munir K S, Zheng Y, Zhang D, Lin J, Li Y and Wen C 2017 *Mater. Sci. Eng. A* **696** 10
[9] Dai H, Wong E W and Lieber C M 1996 *Nature* **384** 147
[10] Hone J, Whitney M, Piskoti C and Zettl A 1999 *Phys. Rev. B* **59** R2514
[11] Hassanzadeh-Aghdam M K, Ansari R and Darvizeh A 2018 *Int. J. Eng. Sci.* **130** 215
[12] Shirasu K, Nakamura A, Yamamoto G, Ogasawara T, Shima- mura Y, Inoue Y *et al* 2017 *Composites, Part A* **95** 152
[13] Zhang J and He C 2008 *Acta Mech.* **196** 33
[14] Pantano A and Cappello F 2008 *Meccanica* **43** 263
[15] Hassanzadeh-Aghdam M K and Mahmoodi M J 2018 *Mater. Sci. Eng. B* **229** 173
[16] Schadler L S, Giannaris S A and Ajayan P M 1998 *Appl. Phys. Lett.* **73** 3842
[17] Qian D, Dickey E C, Andrews R and Rantell T 2000 *Appl. Phys. Lett.* **76** 2868
[18] Allaoui A, Bai S, Cheng H M and Bai J B 2002 *Compos. Sci. Technol.* **62** 1993
[19] Tai N H, Yeh M K and Liu J H 2004 *Carbon* **42** 2774
[20] Sahoo N G, Jung Y C, Yoo H J and Cho J W 2007 *Compos. Sci. Technol.* **67** 1920
[21] Omidi M, Milani A S, Seethaler R J and Araste R 2010 *Car- bon* **48** 3218
[22] Zhang L W, Cui W C and Liew K M 2015 *Int. J. Mech. Sci.* **103** 9

[23] Hasanshahi B and Azadi M 2017 *Iran. J. Sci. Technol. Trans. Mech. Eng.* https://doi.org/10.1007/s40997-017-0137-6

[24] Farsadi M, Öchsner A and Rahmandoust M 2013 *J. Compos. Mater.* **47** 1425

[25] Vijay S J, Tugirumubano A, Go S H, Kwac L K and Kim H G 2018 *J. Alloys Compd.* **731** 465

[26] Kulakov V, Aniskevich A, Ivanov S, Poltimae T and Starkova O 2016 *J. Compos. Mater.* **51** 2979

[27] An F, Lu C, Li Y, Guo J, Lu X, Lu H *et al* 2012 *Mater. Des.* **33** 197

[28] Jen Y M and Huang C Y 2013 *J. Compos. Mater.* **47** 1665

[29] Jia Y, Peng K, Gong X L and Zhang Z 2011 *Int. J. Plast.* **27** 1239

[30] Han D, Mei H, Farhan S, Xiao S, Bai Q and Cheng L 2017 *J. Alloys Compd.* **701** 722

[31] Prashantha K, Soulestin J, Lacrampe M F, Krawczak P, Dupin G and Claes M 2009 *Compos. Sci. Technol.* **69** 1756

[32] Ren X and Seidel G D 2013 *J. Intell. Mater. Sys. Struct.* **24** 1459

[33] Hassanzadeh M and Edalatpanah S 2018 *Int. J. Nano Dimens.* **9** 112

[34] Dong C 2014 *Int. J. Smart Nano Mater.* **5** 44

[35] Hassanzadeh-Aghdam M K, Mahmoodi M J and Kazempour M R 2018 *Int. J. Mech. Mater. Des.* **14** 266

[36] Hassanzadeh-Aghdam M K, Ansari R and Darvizeh A 2017 *J. Compos. Mater.* **51** 2899

[37] Zare Y 2015 *Mech. Mater.* **85** 1

[38] Fisher F T, Bradshaw R D and Brinson L C 2003 *Compos. Sci. Technol.* **63** 1689

[39] Thostenson E T and Chou T W 2003 *J. Phys. D: Appl. Phys.* **36** 573

[40] Anumandla V and Gibson R F 2006 *Compos. Part A* **37** 2178

[41] Seidel G D and Lagoudas D C 2006 *Mech. Mater.* **38** 884

[42] Kanagaraj S, Varanda F R, Zhil'tsova T V, Oliveira M S and Simões J A 2007 *Compos. Sci. Technol.* **67** 3071

[43] Bokobza L 2007 *Polymer* **48** 4907

[44] Yang Q S, He X Q, Liu X, Leng F F and Mai Y W 2012 *Composites, Part B* **43** 33

[45] Ma X, Scarpa F, Peng H X, Allegri G, Yuan J and Ciobanu R 2015 *Aerosp. Sci. Technol.* **47** 367

[46] Kiani Y 2016 *Aerosp. Sci. Technol.* **58** 178

[47] Alibeigloo A 2016 *Composites, Part B* **87** 214

[48] Jam J E and Kiani Y 2015 *Compos. Struct.* **132** 35

[49] Mahmoodi M J and Vakilifard M 2017 *Mater. Des.* **122** 347

[50] Yengejeh S I, Kazemi S A and Öchsner A 2017 *Comput. Mater. Sci.* **136** 85

[51] Ci L and Bai J 2006 *Compos. Sci. Technol.* **66** 599

[52] Valavala P K and Odegard G M 2005 *Rev. Adv. Mater. Sci.* **9** 44

[53] Odegard G M, Gates T S, Wise K E, Park C and Siochi E J 2003 *Compos. Sci. Technol.* **63** 1671

[54] Halpin J C 1969 No. AFML-TR-67-423. *Air force materials lab* (OH: Wright-Patterson AFB)

[55] Affdl J C and Kardos J L 1976 *Polym. Eng. Sci.* **16** 344

[56] Cox H L 1952 *Br. J. Appl. Phys.* **3** 72

[57] Fisher F T, Bradshaw R D and Brinson L C 2002 *Appl. Phys. Lett.* **80** 4647

[58] Demczyk B G, Wang Y M, Cumings J, Hetman M, Han W, Zettl A *et al* 2002 *Mater. Sci. Eng. A* **334** 173