# Fracture analysis of monolayer graphene sheets with double vacancy defects via MD simulation

R. Ansari$^{a,*}$, B. Motevalli$^{a}$, A. Montazeri$^{b,c}$, S. Ajori$^{a}$

$^{a}$ Department of Mechanical Engineering, University of Guilan, P.O. Box 3756, Rasht, Iran
$^{b}$ Computational Physical Sciences Research, School of Nano Science, Institute for Research in Fundamental Sciences (IPM), P.O. Box: 19395-5531, Tehran, Iran
$^{c}$ Institute for Nano Science and Technology, Sharif University of Technology, Tehran, Iran

---

## ARTICLE INFO

**Article history:**
Received 15 February 2011
Received in revised form
15 April 2011
Accepted 13 May 2011
by M. Grynberg
Available online 20 May 2011

**Keywords:**
A. Graphene sheets
C. Vacancy defect
D. Fracture analysis

---

## ABSTRACT

Carbon nanostructures such as carbon nanotubes (CNTs) and graphene sheets have attracted great attention due to their exceptionally high strength and elastic strain. These extraordinary mechanical properties, however, can be affected by the presence of defects in their structures. When a material contains multiple defects, it is expected that the stress concentration of them superposes if the separation distances of the defects are low, which causes a more reduction of the strength. On the other hand, it is believed that if the defects are far enough such that their affected areas are distinct, their behavior is similar to a material with single defect. In this article, molecular dynamics (MD) is used to explore the influence of separation distance of double vacancy defects on the mechanical properties of single-layered graphene sheets (SLGSs). To this end, critical stress and strain of SLGSs containing double vacancy with different distances are determined and the results are compared with those of perfect SLGSs and graphene sheets with single vacancy defect. The results reveal that the ultimate strength of the SLGS with double vacancy tends to the one with a single vacancy when the separation distance becomes further. In this regard, the threshold distance beyond which double defects behave like a single one is examined. Finally, Young's modulus of perfect, single and double vacancy defected graphene sheets with different separation distances is determined. It is concluded that this property is slightly affected by the separation distance.

© 2011 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

The 1991 lijima paper in Nature [1] is undoubtedly responsible for the current explosion of interest in carbon science: synthesis, properties, theory and applications. The experimental and theoretical investigations on carbon nanostructures such as carbon nanotubes (CNTs) and graphene sheets (GSs) have revealed their exceptional electrical and mechanical properties [2–6]. A single-layered graphene sheet (SLGS) which was detected in graphites [7–9], is a planar monolayer of carbon atoms contrived in a hexagonal appearance called honeycomb that consists of carbon–carbon bonds. In 2004, Novoselov et al. [10] found a way of separating individual graphene planes by experimental means. The high strength of these nanostructures makes them so promising for applications such as nano-composite materials [6,11]. The elastic properties and intrinsic strength of a suspended monolayer GSs over a set of open holes on an Si substrate was measured by Lee et al. [4] through an AFM nano-indention. It is believed that there are some uncertainties on the experimental measurement of these mechanical properties due to the inevitable presence of structural defects and stress concentration at the clamped points. Nevertheless, their measurement showed a critical stress ($\sigma_{\text{cr}}$) and strain of about 130 GPa and 25% for the aforementioned graphene membrane, respectively, while Young's modulus was obtained roughly as 1 TPa. Neek-Amal and Peeters [12], Neek-Amal and Asgari [13], Neek-Amal and Peeters [14] performed the MD simulation of nano-indentation of circular graphene sheets similar to the experiments of [4]. They also considered graphene sheets containing vacancy defects which were distributed randomly with different densities [14]. Their simulations revealed that presence of defects reduces the ultimate strength and Young's modulus of SLGSs. By employing molecular mechanic simulations, Kvashnin et al. [15] examined the nano-indentation of circular graphene sheets with different radii. Likewise [14], they also studied the effect of different densities of vacancy defects on mechanical properties of SLGSs. However, they observed different trends in the variation of Young's modulus from that of [14]. Regarding their simulations, Young's modulus first increases by the presence of defects then it would decrease by increasing the density of defects. Furthermore, Xu and Liao [16] studied the deflection of a circular SLGS under a transverse central load by means of both MD simulation and the finite element method

---

* Corresponding author.
E-mail address: r_ansari@guilan.ac.ir (R. Ansari).

0038-1098/$ – see front matter © 2011 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ssc.2011.05.021

(FEM). According to their results, they observed some mismatches between the two models. They stated that this discrepancy is origi- nated from the simulation mode of the two models which is a bond stretching mode for MD model and a bending to stretching transi- tion in the continuum one. Hemmasizadeh et al. [17] tried to over- come this discrepancy by an equivalent continuum model.

To investigate the elastic and mechanical properties of single- layered graphene sheets with perfect structures (SLGPs), different theoretical methods such as density functional theory (DFT), quantum mechanics, MD simulations, and continuum mechanics are implemented. By employing DFT, Liu et al. [18] obtained Young's modulus of 1.05 TPa. Moreover, they computed the critical stress and strain of SLGPs and reported the value of 110 GPa and 19.4%, respectively. Using a similar method for the case of single walled carbon nanotubes (SWCNTs), Ogata and Shibutani [19] obtained similar results for critical stress and strain equal to 107 GPa and 20.8%, respectively. Utilizing quantum mechanics, Yanovsky et al. [20] obtained these mechanical properties as: $Y = 0.737$ TPa, $\sigma_{\text{cr}} = 90$ GPa, and $\varepsilon_{\text{cr}} = 12.3\%$. Regarding MD simulations, Jiang et al. [21] examined Young's modulus of SLGSs under different sizes, temperatures, and isotopic disorders. Meanwhile, Shen et al. [22] obtained Young's and shear moduli of these nanostructures under different temperatures. On the other hand, the fracture analysis and ultimate strength $(\sigma_{u})$ of SLGSs were studied by Ni et al. [23]. They found out that these nanomaterials are much stronger in the armchair direction $(\sigma_{u} = 210$ GPa) than in the zigzag direction $(\sigma_{u} = 180$ GPa), indicating the anisotropic behavior of SLGSs. Moreover, they observed self- stiffening phenomena in the tensile process which results in higher Young's modulus after a certain strain. In addition, the same authors conducted some other MD simulations on graphene nanoribbons, and revealed a similar self-stiffening behavior in them [24]. However, their results showed a high value of difference with the existing experimental and other atomistic data [4,18,19]. The main drawbacks of atomistic modeling are their time expense and the limitation on the length scale. For this reason, a lot of efforts have been made in recent years to develop continuum mechanics theories at nano-scales. In this respect, Reddy et al. [25] obtained Young's modulus of SLGSs 0.669 TPa by employing continuum mechanics, while Shokrieh and Rafiee [26] obtained a value of 1.04 TPa. On the other hand, Arroyo and Belytschko [27,28] developed a nano-scale continuum theory in which the interatomic potential functions such as Tersoff-Brenner were imposed in the constitutive continuum model through the Cauchy-Born rule. Using this new nano-scale continuum theory, they achieved a value of 0.694 TPa for Young's modulus of carbon nanotubes (CNTs) [28]. Based on a finite element model, where the bonding of atoms is modeled by a truss of connecting beams or springs, Young's modulus was extracted as 1.025 and 1.367 TPa by Sakhaee-Pour [29] and Georgantzinos et al. [30], respectively. However, these models are not capable of modeling the fracture process and obtaining the ultimate strength of nano-structures as well as the mechanical properties of defected ones. To overcome these drawbacks, Xiao et al. [31,32] developed a FE model in conjunction with interatomic potential functions. Although the latter authors implemented the model for defective SLGSs, they indicated that the defect formation energy is more complicated than their approximated method.

Numerical simulations revealed that the presence of defects would significantly affect the mechanical properties of SLGSs [14,15,31,32]. Note that the term defect is referred to the broad sense of the word that reflects deviation of the material from the regular atomic scale structure. Thus, in the case of SLGSs, a defect is defined as a distortion of the perfect graphene sheet. The possible graphene defects can be classified into three main groups: incomplete bonding defects (vacancies, dislocations, etc.), topological defects (introduction of ring sizes other than hexagons) and heterogeneous defects (doping with impurity attachments and substitutions instead of carbon atoms). Among the various types of defects in SLGSs, vacancies have received much more attention than the others. Vacancies result from missing carbon atoms in the graphene sheets, which can happen when SLGSs are subjected to irradiation. Theoretical predictions have shown that energetic particles can induce atomic defects in graphene layers [33,34]. The carbon atoms might be knocked out by either high-energy electrons or ions. Furthermore, due to the restrictions of SLGS manufacturing, perfect SLGSs can be produced at a much lower rate than defective ones. However, the number of experimental reports on these defects is limited. Even more recently, atomic scale defects in the structure of SLGSs were successfully observed by HRTEM [35].

Unlike the MD simulations of [14,15] where the vacancy defects were distributed randomly in the structure of SLGSs, this paper aims to study SLGSs containing multiple defects, in a systematic manner. Indeed, it is expected that SLGSs containing multiple defects with lower separation distances exhibit lower ultimate strength due to the superposition of stress concentrations caused by these defects. On the other hand, the higher the separation distance becomes, the more the affected zones are distinct; consequently, the ultimate strength tends to those containing a single defect. Correspondingly, the primary objective of this paper is to examine the effect of separation distance of double vacancy defects on the mechanical properties of SLGSs using MD simulations. Moreover the other objective is to find the threshold separation distance over which the affected zones of defects are distinct; implying that the SLGS containing multiple defects behaves such a one with a single vacancy. To this end, first, a SLGP under tensile loading is studied and its Young's modulus, ultimate stress and critical strain are calculated and compared with the existing numerical and experimental results. Then, the verified model is used to compare the mechanical properties of single layer graphene sheet with single vacancy defect (SLGSV) and those with double vacancies (SLGDV). To examine the extracted threshold separation distance, a SLGS containing triple vacancy defect which are departed by this distance is also simulated.

### 2. Molecular dynamics model

The Tersoff-Brenner potential energy function (PEF) [36, 37] was utilized to simulate the energy of covalent bonding between carbon atoms in the structure of graphene layer. The simulation was conducted in a canonical ensemble with a constant temperature of 300 K (room temperature). In order to maintain the simulation temperature at $T = 300$ K, the Nose'-Hoover thermostat [38] was employed. The use of this thermostat leads to less fluctuations in the temperature [39]. Moreover, the Velocity-Verlet integration algorithm [40] was used for solving the equations of motion through time with a time step of $dt = 1$ fs. This time step guarantees good conservation of energy. Also, it provides a good balance between accuracy and computational costs. The important issue is that the initial configuration of the graphene layer in the MD simulation may not correspond to an equilibrium state of the system. Thus, before applying the external loads to produce the desired deformations, a relaxation process was implemented in which the SLGS was initially relaxed at $T = 300$ K by minimizing the total potential energy of the entire graphene. Finally, with appropriate boundary conditions, axial tension was utilized to obtain the desired mechanical properties. For this reason, one end of the graphene layer was held, while the other end was displaced incrementally when time evolves, as depicted in Fig. 1. In this respect, the incremental displacements equal to 0.05 Å were imposed in the longitudinal mode (LM) [41] (zigzag

<table><thead><tr><th>Sample No.</th><th>1 ($d_v$)</th><th>2 ($2d_v$)</th><th>3 ($4d_v$)</th><th>4 ($6d_v$)</th><th>5 ($8d_v$)</th><th>6 ($10d_v$)</th><th>7 ($12d_v$)</th><th>8 ($14d_v$)</th><th>9 ($16d_v$)</th></tr></thead><tbody><tr><td>Separation distance</td><td>4.26</td><td>8.52</td><td>17.04</td><td>25.56</td><td>34.08</td><td>42.6</td><td>51.12</td><td>59.64</td><td>68.16</td></tr></tbody></table>

![](./images/811660048525688835_1.jpg)

Fig. 1. Schematic representation of imposing tensile load on a SLGS in longitudinal mode.

![](./images/811660048525688835_2.jpg)

Fig. 2. Separation distance of two vacancy defects in the structure of SLGS ($d_v = 3\sigma$).

direction). It is noted that the system was initially relaxed for 3000 steps (3 ps), while after imposing each incremental displacement, the relaxation time was taken 2 ps.

All sets of graphene sheets under investigation had square shapes with the length of 8.5 nm containing 2950 atoms, where two atoms with their corresponding bonds were missed. Concerning the structure of graphene, it is discerned that the shortest possible distance between missing atoms of two vacancies with similar configurations, which is denoted by $d_v$, is three times of the carbon-carbon bond length (see Fig. 2). To explore the effect of separation distance of the vacancy defects on the mechanical properties, the defects were displaced apart from each other by a multiplier of this distance in the loading direction, as depicted in Fig. 2. In this regard, the samples given in Table 1 were selected to study the effect of this separation distance on the strength of graphene sheets. To perceive a comparison, two more graphene sheets with the same geometrical size were also simulated, one of which was perfect and the other one contained a single vacancy defect.

![](./images/811660048525688835_3.jpg)

Fig. 3. Stress–strain curves of graphene sheets with double vacancies, single vacancy, and a perfect structure.

## 3. Results and discussion

Fig. 3 demonstrates the stress–strain curves for samples 1 and 4 in comparison with two reference samples: SLGP and SLGSV. As revealed, the curves of different samples almost coincide until the fracture point. As expected, the ultimate strength of SLGP is the highest. The critical stress and strain, where the fracture occurs, were obtained 115.72 GPa and 20.2% for the case of perfect graphene sheet, respectively. These results are in good agreement with the ones presented by DFT models (110 GPa and 19.4% [18], and 107 GPa and 20.8% [19] for critical stress and strain, respectively). Moreover, the present result has reasonable agreement with the experiments of [4] ($130 \pm 10$ GPa and 25%). In addition, Young's modulus is achieved approximately 0.8 TPa for the present case. To demonstrate a comparison of the present results with the ones given in the literature, Table 2 is exposed. As presented in this table, Young's modulus has dispersed values ranging from 0.5 to 1.4 TPa in different studies.

As can be seen from Fig. 3, these properties are reduced by the presence of vacancy defects in the structure of the graphene sheet. For the case of SLGSV, the critical stress and strain were found to be 108.8 GPa and 18.41%, respectively. In comparison with a SLGP, the foregoing values imply 6.4% and 9.7% reductions in critical stress and strain, respectively. Meanwhile, it was observed that for the case of SLGDV, the sample with the lowest possible separation distance has about 7.3% and 11.46% reduction in its critical stress and strain (100.8 GPa and 16.3%), respectively, compared to the SLGSV. The fracture process of the foregoing sample is demonstrated in Fig. 4. As shown, prior to the fracture propagation, two pairs of pentagons and heptagons are formed around the vacancy defects. Thereafter, the fracture disperses in the transverse direction on the two sides of the defects. During fracture propagation, two chains of atoms are formed at the location of the vacancy defects. At last, four chains of atoms are formed, where two are the aforementioned chains at the location of vacancies and the other two are made up on the edges of the sheet.

<table>
<caption>Table 2
A comparison of the computed mechanical properties in the present study and the ones reported in the literature.</caption>
<thead>
<tr>
<th>Study</th>
<th>Method</th>
<th>Young’s modulus (TPa)</th>
<th>Critical stress (GPa)</th>
<th>Critical strain</th>
</tr>
</thead>
<tbody>
<tr>
<td>Present</td>
<td>MD</td>
<td>0.7985</td>
<td>115.72</td>
<td>20.2%</td>
</tr>
<tr>
<td>Lee et al. [4]</td>
<td>Experimental</td>
<td>$1 \pm 0.1$</td>
<td>$130 \pm 10$</td>
<td>25%</td>
</tr>
<tr>
<td>Jiang et al. [21]</td>
<td>MD</td>
<td>1.1</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Shen et al. [22]</td>
<td>MD</td>
<td>0.905</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Ni et al. [23]</td>
<td>MD</td>
<td>1.13</td>
<td>180</td>
<td>32.48%</td>
</tr>
<tr>
<td>Tsai and Tu [42]</td>
<td>MD</td>
<td>0.912</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Neek-Amal and Peteers [14]</td>
<td>MD</td>
<td>$0.501 \pm 0.032$</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Kvashnin et al. [15]</td>
<td>MMa</td>
<td>1.39 (average)</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Reddy et al. [25]</td>
<td>Continuum mechanics</td>
<td>0.669</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Shokrieh and Rafiee [26]</td>
<td>Continuum mechanics</td>
<td>1.04</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Liu et al. [18]</td>
<td>DFT</td>
<td>1.05</td>
<td>110</td>
<td>19.4%</td>
</tr>
<tr>
<td>Ogata and Shibutani [19]</td>
<td>DFT</td>
<td>–</td>
<td>107</td>
<td>20.8%</td>
</tr>
<tr>
<td>Yanovsky et al. [20]</td>
<td>Quantum mechanics</td>
<td>0.737</td>
<td>90</td>
<td>12.3%</td>
</tr>
<tr>
<td>Sakhaee-Pour [29]</td>
<td>FEM</td>
<td>1.025</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Georgantzinos et al. [30]</td>
<td>FEM</td>
<td>1.367</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Xiao et al. [31]</td>
<td>FEM</td>
<td>1.13</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">a Molecular Mechanics (MM).</td>
</tr>
</tfoot>
</table>

![](./images/811660048525688835_4.jpg)

Fig. 4. Failure process of a SLGDV with the shortest possible separation distance: (a) after initial relaxation, (b) formation of pentagons and heptagons at adjacent of the vacancies, (c) early stages of fracture propagation, (d) formation of two chains at the location of vacancy defects, and (e) formation of four chains.

It should be noted that formation of four chains of atoms is viewed only in graphene sheets with very short separation distances, while in other cases only two chains of atoms are formed on the edges of the sheet.

The trend of critical stress and strain of SLGDVs in terms of separation distance is presented in Fig. 5. As seen, decreasing the separation distance, causes a more noticeable decrease in the ultimate strength of the graphene sheet. The ultimate strength of the SLGDV tends to the one with a single vacancy when the separation distance becomes farther. Such a behavior can also be seen for the fracture strain. Based on the obtained data, fitted formulas are also achieved for the critical strain and stress in terms of the separation distance ($D$) as

$$
\varepsilon_{\mathrm{cr}_{\mathrm{DV}}}=\left(1-\frac{K}{D^{n}}\right) \varepsilon_{\mathrm{cr}_{\mathrm{SV}}} \quad K=0.553, \ n=1.13 \tag{1}
$$

$$
\sigma_{\mathrm{cr}_{\mathrm{DV}}}=\left(1-\frac{K^{\prime}}{D^{n^{\prime}}}\right) \sigma_{\mathrm{cr}_{\mathrm{SV}}} \quad K^{\prime}=0.308, \ n^{\prime}=1.40 \tag{2}
$$

in which, $\varepsilon_{\mathrm{cr}_{\mathrm{DV}}}$ and $\varepsilon_{\mathrm{cr}_{\mathrm{SV}}}$ are the critical strains corresponding to the SLGDV and SLGSV, respectively, meanwhile $\sigma_{\mathrm{cr}_{\mathrm{DV}}}$ and $\sigma_{\mathrm{cr}_{\mathrm{SV}}}$ are the ones representing the critical stresses. Note that in Eqs. (1) and (2), $D$ is in terms of Å. The curves obtained based on these fitted formulas are also presented in Fig. 5. To obtain a threshold separation distance where the strength of a SLGDV is almost as SLGSV, Eq. (2) is utilized. In this regard, it is found that if $D > 44.46$ Å, the amount of strength reduction is below 0.5%. Consequently, the shortest possible separation distance, for which the strength reduction is below 0.5%, is $D_{\mathrm{thr}}=11 \times(3 \sigma)=46.86$ Å.

Therefore, it is concluded that over this threshold distance ($D_{\mathrm{thr}}$), the superposition of the effects of vacancy defects is almost negligible, and a SLGDV behaves like a SLGSV. For a further examination of this fact, a case study of a single-layered graphene sheet with triple vacancies (SLGTV) which are distanced apart with $D_{\mathrm{thr}}$ was done as an example. In this respect, a rectangular graphene sheet with dimensions of $l = 14$ nm and $w = 5$ nm was used. The corresponding critical stress and strain for this particular sample were found to be 108.4 GPa and 18.39%, which indicates a 0.36% and 0.11% reduction in comparison with the ones of the SLGSV. It is seen that this SLGTV responses also like

![](./images/811660048525688835_5.jpg)

Fig. 5. (a) Critical strain and (b) critical stress versus the separation distance.

![](./images/811660048525688835_6.jpg)

Fig. 6. Variation of Young's modulus with the separation distance.

a SLGSV, indicating that the proposed threshold distance is safe. Finally, Young's modulus of all samples is disclosed in Fig. 6. It is observed that the deviation in Young's modulus is so small and negligible, where the highest difference is about 0.58% with SLGSV and 0.89% with SLGP. Actually, the slight change in Young's modulus of carbon nanostructures due to presence of vacancy defects is also presented by other studies [43,44]. The negligible deviation of Young's modulus can also be observed in Fig. 3, where the stress-strain curves of different samples almost coincide prior to their fracture, stating that their slopes are almost the same in the early stages of loading. However, as demonstrated by Refs. [14,15, 32], Young's modulus of SLGSs reduces when the number (density) of defects exceeds.

## Conclusion

In this article, based on the Tersoff-Brenner potential, molecular dynamics simulations were carried out to investigate the intrinsic strength of perfect and defective SLGSs. In the case of perfect SLGSs, the results of the present study showed good agreement with those of experimental and numerical studies. In the case of defective ones, the results exhibited that multiple vacancy defects can cause more reduction in the strength of SLGSs. In this respect, the influence of the separation distance between two single vacancies forming a double vacancy defect on the ultimate strength of these nanostructures was examined. It was observed that when the shortest separation distance of double vacancy is reached, the reduction in the ultimate strength is almost twice of the reduction caused by a single vacancy. On the other hand, it was also observed that the samples with the separation distance greater than $D_{\text{thr}} = 46.86$ Å behaves almost like a SLGS with a single vacancy defect. To examine this threshold distance, a SLGS containing triple vacancy defects which were distanced apart by $D_{\text{thr}}$, was further analyzed. Finally, the variation of Young's modulus with separation distance was investigated, and it was found that this property is slightly affected by the separation distance.

## References

[1] S. Iijima, Nature 354 (1991) 56.
[2] H. Dai, Accounts of Chemical Research 35 (2002) 1035-1044. cited 600.
[3] C.G. Navarro, R.T. Weitz, A.M. Bittner, M. Scolari, A. Mews, M. Burghard, K. Kern, Nano Letters 7 (2007) 3499-3503.
[4] C. Lee, X.D. Wei, J.W. Kysar, J. Hone, Science 321 (2008) 385.
[5] B.I. Yakobson, C.J. Brabec, J. Bernholc, Physical Review Letters 76 (1996) 2511-2514.
[6] S. Stankovich, D.A. Dikin, G.H.B. Dommett, K.M. Kohlhaas, E.J. Zimney, E.A. Stach, R.D. Piner, S.T. Nguyen, R.S. Ruoff, Nature 442 (2006) 282-286.
[7] I. Forbeaux, J.-M. Themlin, J.-M. Debever, Physical Review B 58 (1998) 16396-16406.
[8] M.-H. Tsai, C.S. Chang, J.D. Dow, I.S.T. Tsong, Physical Review B 45 (1992) 1327-1334.
[9] A.J. Van Bommel, J.E. Crombeen, A. Van Tooren, Surface Science 48 (1975) 463-472.
[10] K.S. Novoselov, A.K. Geim, S.V. Morozov, D. Jiang, Y. Zhang, S.V. Dubonos, et al., Science 306 (2004) 666.
[11] M.A. Rafiee, J. Rafiee, Z.-Z. Yu, N. Koratkar, Applied Physics Letters 95 (2009) 223103.
[12] M. Neek-Amal, F.M. Peeters, Physical Review B 81 (2010) 235421.
[13] M. Neek-Amal, R. Asgari, Nano-indentation of circular graphene flakes, Asgari, arXiv:0903.5035v1.
[14] M. Neek-Amal, F.M. Peeters, Physical Review B 81 (2010) 235437.
[15] A.G. Kvashnin, P.B. Sorokin, D.G. Kvashnin, Fullerenes, Nanotubes, and Carbon Nanostructures 18 (2010) 497-500.
[16] X. Xu, K. Liao, Materials Physics and Mechanics 4 (2001) 148-151.
[17] A. Hemmasizadeh, M. Mahzoon, E. Hadi, R. Khandan, Thin Solid Films 516 (2008) 7636-7640.
[18] F. Liu, P. Ming, J. Li, Physical Review B 76 (2007) 064120.
[19] S. Ogata, Y. Shibutani, Physical Review B 68 (2003) 165409.
[20] Y.G. Yanovsky, E.A. Nikitina, Y.N. Karnet, S.M. Nikitin, Physical Mesomechanics 12 (2009) 254-262.
[21] J.W. Jiang, J.S. Wang, B. Li, Physical Review B 80 (2009) 113405.
[22] L. Shen, H.S. Shen, C.L. Zhang, Materials and Design 31 (2010) 4445-4449.
[23] Z. Ni, H. Bu, M. Zou, H. Yi, K. Bi, Y. Chen, Physica B 405 (2010) 1301-1306.
[24] H. Bu, Y. Chen, M. Zou, H. Yi, K. Bi, Z. Ni, Physics Letters A 373 (2009) 3359-3362.
[25] C.D. Reddy, S. Rajendran, K.M. Liew, Nanotechnology 17 (2006) 864-870.
[26] M.M. Shokrieh, R. Rafiee, Materials and Design 31 (2010) 790-795.
[27] M. Arroyo, T. Belytschko, Journal of the Mechanics and Physics of Solids 50 (2002) 1941-1977.
[28] M. Arroyo, T. Belytschko, Physical Review B 69 (2004) 115415.
[29] A. Sakhaee-Pour, Solid State Communications 149 (2009) 91-95.
[30] S.K. Georgantzinos, G.I. Giannopoulos, N.K. Anifantis, Materials and Design 31 (2010) 4646-4654.
[31] J.R. Xiao, J. Staniszewski, J.W. Gillespie, Composite Structures 88 (2009) 602-609.
[32] J.R. Xiao, J. Staniszewski, J.W. Gillespie, Materials Science and Engineering A 527 (2010) 715-723.
[33] K. Nordlund, J. Keinonen, T. Mattila, Physical Review Letters 77 (1996) 699-702.
[34] A.V. Krasheninnikov, et al., Physical Review B 63 (2001) 245405.
[35] A. Hashimoto, et al., Nature 430 (2004) 870-873.
[36] J. Tersoff, Physical Review B 37 (1988) 6991.
[37] D.W. Brenner, Physical Review B 42 (1990) 9458.
[38] W.G. Hoover, Physical Review A 31 (1985) 1695.
[39] C.L. Zhang, H.S. Shen, Journal of Physics D: Applied Physics 41 (2008) 055404.

[40] M.P. Allen, D.J. Tildesley, Computer Simulation of Liquids, New York, 1986.

[41] M.B. Nardelli, B.I. Yakobson, J. Bernholc, Physical Review Letters 81 (1998) 4656.

[42] J.L. Tsai, J.F. Tu, Materials and Design 31 (2010) 194.

[43] X. Hao, H. Qiang, Y. Xiaohu, Carbon 45 (2007) 2486.

[44] C.H. Wong, Computational Materials Science 49 (2010).