Accepted Manuscript

Interpreting experimental observations of irradiation on single-phase concen-
trated solid-solution alloys from first principles

Xin-Xin Wang, Liang-Liang Niu, Shaoqing Wang

<table>
  <tr>
    <td>PII:</td>
    <td>S0167-577X(17)30775-9</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/10.1016/j.matlet.2017.05.051</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>MLBLUE 22626</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Materials Letters</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>23 March 2017</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>11 May 2017</td>
  </tr>
</table>

![](./images/813134095851716609_1.jpg)

Please cite this article as: X-X. Wang, L-L. Niu, S. Wang, Interpreting experimental observations of irradiation on single-phase concentrated solid-solution alloys from first principles, Materials Letters (2017), doi: http://dx.doi.org/10.1016/j.matlet.2017.05.051

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Interpreting experimental observations of irradiation on single-phase concentrated solid-solution alloys from first principles

Xin-Xin Wang$^{\mathrm{a,b},*}$, Liang-Liang Niu$^{\mathrm{c}}$, Shaoqing Wang$^{\mathrm{a}}$

$^{\mathrm{a}}$Shenyang National Laboratory for Materials Science, Institute of Metal Research, Chinese Academy of Sciences, Shenyang 110016, China

$^{\mathrm{b}}$School of Materials Science and Engineering, University of Science and Technology of China, Hefei 230026, China

$^{\mathrm{c}}$Department of Nuclear Engineering and Radiological Science, University of Michigan, Ann Arbor, MI 48109, USA.

## Abstract

Most recently, a host of irradiation experiments conducted on single-phase concentrated solid-solution alloys has been lacking interpretations from first principles. Here, the formation energetics and migration kinetics of interstitial defects in pure Ni and two Ni-based alloys (NiCo and NiFe) have been investigated by first principles calculations, based on which we are able to provide significant insights to two key aspects of experimental observations concerning the irradiation-induced segregation and the enhanced radiation tolerance.

## Keywords:
Simulation and modelling; Microstructure; First principles; interstitial defects; Single-phase concentrated solid-solution alloy

*Corresponding author.

E-mail address: xxwang14b@imr.ac.cn (X-X. Wang)

### 1. Introduction

Single-phase concentrated solid-solution alloys (SP-CSAs) have drawn special interest for their remarkable physical properties [1, 2]. Recently, another important attribute, i.e., enhanced radiation tolerance, was added to the repertoire of this class of materials [3-5]. Zhang et al. [3] demonstrated that the improved radiation tolerance can be accounted for by the chemical complexity of SP-CSAs, which will lead to a much slower energy dissipation rate. Lu and coworkers [4] further showed that their irradiation performance are fundamentally related to the atomic-level defect dynamics. On the aspect of radiation-induced segregation, a simultaneous enrichment of Co/Ni and depletion of Cr/Fe/Mn/Pd on interstitial loops has been observed [6, 7].

Despite the aforementioned experimental and simulation results, we find surprisingly little information on first principles investigation of defect behaviors in SP-CSAs apart from that performed by Zhao et al. [8]. Here, we have studied the formation energetics and migration kinetics of interstitial defects in Ni, $Ni_{0.75}Fe_{0.25}$ (NiFe) and $Ni_{0.75}Co_{0.25}$ (NiCo) systems using first principles calculations. To simplify the complex random picture, the extreme case of ordered L1₂ alloy configurations have been used. Our primary goal is to gain insight into the experimental observations and provide reference for future work adopting more sophisticated models.

### 2. Methodology

The first-principles calculations were performed by VASP code [9]. The interaction between ions and electrons was described by projector augmented wave method [10] and the generalized gradient approximation [11] with the exchange-correlation functional of Perdew-Burke-Ernzerh. Each 3×3×3 supercell contains 108 atoms, and the cutoff energy for the plane wave basis was set to 400 eV. An uniform Monkhorst-Pack k-points sampling [12] of 3×3×3 was used to summate the Brillouin zone.

Spin polarization was considered in all calculations. The iteration continues until the forces on all atoms are less than $0.01\ \text{eV}\mathring{\text{A}}^{-1}$ in structure optimization and $0.02\ \text{eV}\mathring{\text{A}}^{-1}$ in migration barrier calculations, which were performed using the nudged elastic band method [13]. Lattice parameter validation and the definition of formation energy have been presented in the Supplementary Materials.

## 3. Results and discussion

Fig. 1 presents the formation energies of single interstitials in the form of <100>, <110> and <111> dumbbells (the missing configurations are unstable). We found that the <100> dumbbells in all systems are the most stable interstitial configurations. In NiFe, the order of formation energies for individual dumbbells is Ni-Ni<Ni-Fe<Fe-Ni<Fe-Fe for <100>, Ni-Ni<Ni-Fe<Fe-Fe for <110>, and Fe-Ni<Fe-Fe for <111> dumbbells. Additionally, the energy difference between Ni-Ni and Ni-Fe configurations is ~0.3 eV. These results indicate that the most energetically favorable interstitial defects have Ni-Ni composition, followed by mixed dumbbells and Fe-Fe. This tendency was also observed in recent MD simulations of SP-CSAs [14]. In contrary, the formation energy order in NiCo is Ni-Co<Co-Co<Co-Ni<Ni-Ni for <100, Ni-Co<Co-Co<Ni-Ni for <110>, and Co-Co<Co-Ni for <111> dumbbells. The energy difference between Ni-Co and Co-Co is less than 0.1 eV, much smaller than that in NiFe. This indicates that the most energetically favorable interstitial defects in NiCo have Ni-Co and Co-Co composition, followed by Co-Ni and Ni-Ni. It is thus reasonable to believe that the interstitial configurations will be primarily composed of Ni-Ni in NiFe alloys (highly enriched with Ni), whereas the primary composition will be Ni-Co and Co-Co in NiCo (slightly favoring Co). The fact that the interstitial configurations favor Co and Ni strongly supports experimental observations [6, 7] that both perfect and Frank loops, which are essentially the

respective aggregates of <110> and <111> interstitial defects, are enriched with Ni/Co (Co has the most pronounced enrichment) and depleted with Cr/Fe/Mn/Pd in several complex SP-CSAs. Due to the smaller atomic radius of Ni/Co in comparison with Fe, the energetic driving force is for interstitial loops to be enriched with Ni/Co and depleted with Fe to minimize the strain energy [6].

![](./images/813134095851716609_2.jpg)

Fig. 1. Formation energies of (a) <100>, (b) <110>, and (c) <111> dumbbells in NiFe and NiCo alloys. The corresponding configurations are illustrated in (d). The dashed lines indicate interstitial formation energies of the corresponding configurations in pure Ni.

We further show in Fig. 2 the migration behaviors of interstitials in terms of one-dimensional (1D) translation and three dimensional (3D) rotation in all three systems. Particularly, the 1D migration of <110> dumbbells in pure Ni is too low (0.004 eV) to be shown, much lower than the 3D translation and rotation barrier of 0.14 eV for <100> dumbbells (Fig. 2d), the barrier of 0.17 eV for 3D transition between <111> and <110> dumbbells (Fig. 2c), and the barrier of 0.78 eV for 3D transition beween <100> to <110> dumbells (Fig. 2d). We only calculate the case of single interstitials due to size restriction. However, regarding interstitial behavior in pure fcc metals, it is well-established that:
(1) 1D migration of <110> crowdion exhibits strong dynamic correlation due to the extremely low barriers [15]; (2) the stability of <110> interstitial clusters increases with cluster size [16]; (3) the 1D

migration of interstitial cluster is essentially completed by the migration of individual crowdions and their migration barriers are of the same order as individual crowdions [15]. Therefore, interstitial behavior in pure Ni is dominated by the fast 1D migration of interstitials because of the pronounced barrier disparities beween 1D and 3D motion.

For interstitial migration in NiCo, the 1D migration barrier of 0.07 eV (Fig. 2a) is more than one order of magnitude higher than that in pure Ni (0.004 eV), but it is comparable to the barrier of 0.08 eV for 3D transition between <111> and <110> dumbbells (Fig. 2c), and the 3D translation and rotation barrier of 0.21 eV for <100> dumbbells (Fig. 2d). We thus believe that the both 1D and 3D interstitial migration are important in NiCo. For NiFe, we found that single <110> dumbbell is essentially incapable of 1D migration (Fig. 2b), which can be understood from the high formation energies of Fe-containing interstitials. Hence, when interstitials encounter Fe during 1D translation, they are more energetically favorable to rotate to Ni sites. The obtained 3D transition barrier of 0.15 eV is of the same order to the barrier of 0.12 eV for 3D transition between <111> and <110> dumbbells (Fig. 2c), the 3D translation and rotation barrier of 0.39 eV for <100> dumbbells (Fig. 2d), and the barrier of 0.60 eV for 3D transition beween <100> to <110> dumbells (Fig. 2d). Therefore, interstitial behavior in NiFe should be dominated by the 3D sluggish diffusion of interstials because of its high friction of 1D translation.

![](./images/813134095851716609_3.jpg)

Fig. 2. Energy landscape of interstitial migration. (a) The 1D migration for <110> Ni-Co→<110> Co-Co→<110>
Ni-Co in NiCo and (b) The 3D migration from <110> Fe-Fe to <110> Ni-Fe in NiFe. The <110> dumbbells in NiFe
is unable to perform 1D translation due to the easy rotation. (c) The 3D rotation from <111> to <110> dumbbells.
(d) The 3D translation and rotation from <100> X-Ni to <110> Ni-Ni with <001> Ni-Ni as an intermediate state.

We thus sucessfully explained why there is an interstitial migration mode transition [4] from fast
long-range 1D to slow short-range 3D as the system changes from pure Ni to NiCo, and to NiFe.
This also explains the MD reports [17, 18] that interstitial loops grow slower and interstitial clusters
with much smaller sizes were found in Ni alloys than in pure Ni. Moreover, kinetically, the much
lower interstitial migration barriers in comparison to those of vacancy defects indicate an interstitial-dominated segregation behavior.

Again, we should clarify that the we adopted ordered configurations, but real SP-CSAs in
experiments have random structures. While the present results can provide important insight into the
experimental observations and previous atomistic simulations [19] showed that the defect production

in the ordered and random configurations is similar, the defect behaviors might be very different in disordered (random) alloy structures. This calls for more sophisticated first-principles study using more realistic models to further the preliminary results presented here.

## 4. Conclusions
Our first-principles calculations show that the lower formation energies of Co- and Ni-containing interstitials than Fe-containing ones and their lower migration barriers in comparison to vacancies suggest an interstitial-dominated mechanism for Co/Ni enrichment and Fe depletion at interstitial loops, in good agreement with the experimental observations on irradiation-induced segregation. Most importantly, the change of migration barrier differences between 1D translation and 3D rotation of interstitials imply a shift of interstitial migration from fast long-range 1D motion in Ni to mixed 1D and 3D motion in NiCo, and further to slow short-range 3D motion in NiFe, thus empowering them the increasing defect recombination rate and the increasingly enhanced radiation tolerance.

## Acknowledgements
This work was supported by the National Natural Science Foundation of China (No.51471164) and the National Key R&D Program of China (No.2016YFB0701302). The computational support from the Informalization Construction Project of Chinese Academy of Sciences during the 11th Five-Year Plan Period (No.INFO-115-B01) and the Special Program for Applied Research on Super Computation of the NSFC-Guangdong Joint Fund (the second phase) are also highly acknowledged.

## References
[1] B. Gludovatz, A. Hohenwarter, D. Catoor, E.H. Chang, E.P. George, R.O. Ritchie, Science, 345 (2014) 1153-1158.

[2] Z. Li, K.G. Pradeep, Y. Deng, D. Raabe, C.C. Tasan, Nature, 534 (2016) 227-230.

[3] Y. Zhang, G.M. Stocks, K. Jin, C. Lu, H. Bei, B.C. Sales, L. Wang, L.K. Béland, R.E. Stoller, G.D. Samolyuk, M. Caro, A. Caro, W.J. Weber, Nat. Commun., 6 (2015) 8736.

[4] C. Lu, L. Niu, N. Chen, K. Jin, T. Yang, P. Xiu, Y. Zhang, F. Gao, H. Bei, S. Shi, M.-R. He, I.M. Robertson, W.J. Weber, L. Wang, Nat. Commun., 7 (2016) 13564.

[5] F. Granberg, K. Nordlund, M.W. Ullah, K. Jin, C. Lu, H. Bei, L.M. Wang, F. Djurabekova, W.J. Weber, Y. Zhang, Phys. Rev. Lett., 116 (2016) 135504.

[6] M.-R. He, S. Wang, S. Shi, K. Jin, H. Bei, K. Yasuda, S. Matsumura, K. Higashida, I.M. Robertson, Acta Mater., 126 (2017) 182-193.

[7] C. Lu, T. Yang, K. Jin, N. Gao, P. Xiu, Y. Zhang, F. Gao, H. Bei, W.J. Weber, K. Sun, Y. Dong, L. Wang, Acta Mater., 127 (2017) 98-107.

[8] S. Zhao, G.M. Stocks, Y. Zhang, Phys. Chem. Chem. Phys., 18 (2016) 24043-24056.

[9] G. Kresse, J. Furthmüller, Phys. Rev. B, 54 (1996) 11169-11186.

[10] P. Blöchl, Phys. Rev. B, 50 (1994) 17953-17979.

[11] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett., 77 (1996) 3865-3868.

[12] H.J. Monkhorst, J.D. Pack, Phys. Rev. B, 13 (1976) 5188-5192.

[13] G. Henkelman, B.P. Uberuaga, H. Jónsson, J. Chem. Phys., 113 (2000) 9901-9904.

[14] Y.N. Osetsky, L.K. Béland, R.E. Stoller, Acta Mater., 115 (2016) 364-371.

[15] Y.N. Osetsky, D.J. Bacon, A. Serra, B.N. Singh, S.I. Golubov, J. Nucl. Mater., 276 (2000) 65-77.

[16] Y.N. Osetsky, A. Serra, B.N. Singh, S.I. Golubov, Philos. Mag. A, 80 (2000) 2131-2157.

[17] M.W. Ullah, D.S. Aidhy, Y. Zhang, W.J. Weber, Acta Mater., 109 (2016) 17-22.

[18] D.S. Aidhy, C. Lu, K. Jin, H. Bei, Y. Zhang, L. Wang, W.J. Weber, Acta Mater., 99 (2015) 69-76.

[19] K. Vörtler, N. Juslin, G. Bonny, L. Malerba, K. Nordlund, J. Phys.: Condens. Matter, 23 (2011) 355007.


<br>

**Highlights:**

- Interstitial properties in Ni and Ni alloys have been investigated.

- Radiation-induced segregation at interstitial loops is intersitital-dominated.

- Interstitial migration mode dictates radiation resistance.