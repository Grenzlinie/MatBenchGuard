![](./images/811952383989907457_1.jpg)

# Evaluation of Exchange-Correlation Functionals in Comparison to B3LYP for the Description of Silicon and Cu-Doped Silicon Clusters

AHMED DKHISSI¹,²

¹Laboratoire d'Analyse et d'Architecture des Systèmes-CNRS, 7 av. du Colonel Roche, 31077 Toulouse, France
²Interdiciplinary Research Institute c/o IEMN. Avenue Poincare BP60069, Cite Scientifique, UMR8520 Villeneuve d'Ascq F-59652 France

Received 14 September 2007; accepted 16 October 2007
Published online 10 December 2007 in Wiley InterScience (www.interscience.wiley.com).
DOI 10.1002/qua.21567

ABSTRACT: Several developed exchange-correlation functionals in density functional theory have been systematically applied to describe the geometries and electronic properties of small silicon $(Si_{n+1},n<5)$ and doped silicon $(CuSi_{n})$ clusters. The performance of the various approaches is done with their critical comparison with B3LYP and available high level wave function methods. Our calculations indicate that all functional give reasonable results. Further, OLYP/6-311+G* approach generally agrees with B3LYP results. The good performance of OLYP is of significant interest knowing that the hybrid functionals are computationally more demanding than nonhybrid schemes. So, we recommend OLYP/6-311+G* approach for studying the doped silicon clusters and understanding the electronic properties of silicon by the presence of doped metal impurities. © 2007 Wiley Periodicals, Inc. Int J Quantum Chem 108: 996-1003, 2008

Key words: silicon clusters; doped silicon; DFT

---

## Introduction

S ilicon atomic and nanoclusters have drawn more and more attention because of their relevance to the development of nanoelectronics [1-3]. Silicon clusters may be employed as building blocks for developing new silicon-based nanomaterials with tunable properties. However, pure silicon clusters are unsuitable as the building blocks, because they are chemically reactive due to the existence of dangling bonds [4-9]. Doped metal impurities either in the gas phase or on support can considerably affect the structure and electronic properties of silicon. Metal-doped silicon clusters on the other hand may tend to form closed-shell

Correspondence to: A. Dkhissi; e-mail: adkissi@laas.fr

International Journal of Quantum Chemistry, Vol 108, 996-1003 (2008)
© 2007 Wiley Periodicals, Inc.

EVALUATION OF EXCHANGE-CORRELATION FUNCTIONALS

electronic structures that are of higher stability than the pure species, a representative of new class of endohedral clusters encapsulating metal atoms. This consideration provides strong motivation for the study of the interaction between a metal impu- rity and the silicon both experimentally [10-18] and theoretically [19-41]. Indeed, because of the impor- tance of metal impurity atoms for the behavior of metal clusters, experimental information about the metal-silicon clusters are determined firstly by Beck [13]. The $MSi_{n}, M=Cu, Cr, MO$, and $W(5<n<13)$ are prepared and characterized. One of the main results of this work is the exceptional stability of $CuSi_{10}$ in the case of $CuSi_{n}$ . Further, Hiura et al.[18] studied the $MSi_{n}, M=HF, Ta, W, Re$, etc. ... $(8<n<15)$ . Between these two works, Scherer et al. [14-16] and Kishi et al. [17] succeeded to pro- duce small metal silicon cluster, $M_{n} Si_{n}$ and $NaSi_{n}$  with $n<7$ .

The presence of these essential experimental in- formations provides another motivation for the the- oretical model studies of metal-doped silicon dur- ing these two last decades. Indeed most of these theoretical studies are done with density functional theory using almost the B3LYP functional. Their ability to treat the properties of doped silicon clus- ters is demonstrated. In particular, in the case of CuSi,, clusters, Xiao et al. [23, 27] have published two interesting papers on the geometric and elec- tronic properties of $CuSi_{n}(n=4,6,8,10,12)$ and $CuSi_{n}$ (with $n<7$ ), respectively, using the popular hybrid density functional (B3LYP).

Returning now to DFT methodologies, the search for improved exchange-correlation functionals to make density functional theory (DFT) more accu- rate and generally applicable is still a topic of on- going research; we will present in this work the results obtained with different functionals on the small metal-silicon systems and compared our re- sults to those obtained with B3LYP, because the reliability of the B3LYP/6-311+G* approach for the description of $CuSi_{n}$ clusters are carefully demon strated [24]. In this paper, we will present the re- sults of a systematic investigation of the geometric and electronic properties calculated using the func- tionals from three different categories of DFT meth-ods (GGA, Meta GGA, Hybrid functionals):

1. Handy and Cohen have developed the new exchange functional OPTX [42] (OPTimized eXchange). This functional is claimed to be superior to previous exchange functionals, when compared in particular to the well- established Becke's exchange $(B)$ [43] and hence to be among the best currently avail- able density functionals; a few benchmark calculations performed with this functional and hybrid schemes [44] can be found in Refs. 44 and 45. Since the number of param- eters involved in the OPTX formulation is by far lower than for their predecessors, the im- proved accuracy with respect to the experimen- tal data or molecular databases or both is believed to originate from its careful devia- tion, thus making its range of applicability a priori more extended. The OPTX exchange functional has been coupled here to the LYP, PW91, or B95 correlation functional. The re- sulting exchange-correlation functionals are denoted OLYP, OPW91, and OB95, respec- tively, by analogy with other standard GGA functionals.

2. Voorhis and Scuseria proposed a Meta DFT functional, VSXC [46]. Meta GGA function- als depend on the electron density, its gradi- ent, and the kinetic energy density.

3. Perdew et al. have proposed a hybrid DFT functional, PBE1PBE (also called PBE0) [47].

Since little is known on the reliability of these functionals in describing the metal-silicon clusters, we address this issue in the present contribution through a critical analysis of structures and elec- tronic properties in one model ( $Cu-Si_{n}$ clusters). These data will systematically be compared to those obtained recently with B3LYP with the same basis set. This comparison is very interesting to search another alternative to B3LYP, because hybrid func- tionals are computationally more demanding than nonhybrid schemes, since they require the exact exchange to be evaluated. This is particularly inter- esting for the field of nanoelectronics where the computational cost sometimes acts as bottleneck for calculations on larger molecular clusters.

## Computational Details

All calculations were carried out using Gaussian98 [48]. We will test different categories of DFT methods namely GGA, meta GGA, and hybrid GGA. These functionals correspond to the second- generation of functionals that has been developed, with the aim of covering a larger number of prop- erties. These were elaborated within one of the

VOL. 108, NO. 5 DOI 10.1002/qua INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY 997

DKHISSI

several theoretical frameworks now firmly established for improving such expressions: (i) refinement of the GGA expression by careful reformulation of the model [PBE (Perdew-Burke-Ernzerhof), or OPTX (OPTimized eXchange)/Correlation] and (ii) inclusion of new variables, explicitly dependent on Kohn-Sham orbitals, that go beyond the density and its gradient, $n$, the mathematical form of the so-called meta-GGA functional.

The GGA methods that we are using are OLYP [42, 43, 49], OPW91 [42, 43, 50], OB95 [42, 43, 51]. Further our study involves the pure meta-GGA, VSXC [46] exchange correlation functional based on density matrix expansion up to the fourth order. Finally, the hybrid GGA method that we will assess is PBE1PBE [47]. These functionals were combined with the standard bias set 6-311+G*.

The geometric structure of ${\rm Cu}-{\rm Si}_n$ is fully optimized. In this work, we considered only the most stable isomers of ${\rm Cu}-{\rm Si}_n$ obtained with B3LYP/6-311+G* approach [23]. This method is currently widely used for studying copper-silicon clusters, because it predicts reliable geometrical and electronic properties [24, 30]. Vibrational frequency calculations were carried out for all structures to verify them as true minima by the absence of imaginary eigenvalues.

## Results and Discussion

We will first describe the geometries of individual ${\rm Si}_{n+1}$ and ${\rm CuSi}_n$ ($n=1-4$) clusters in the neutral states. Only the most stable isomer obtained for each system is considered. Then we examine the size dependences of various energetic properties for each isomer. The optimized geometric parameters (bond lengths and angles for all the most stable isomers of ${\rm Si}_{n+1}$ and ${\rm CuSi}_n$ clusters calculated with different methods are summarized in Table I. These data show the performance of the different density functionals, in comparison with B3LYP, for all most stable isomers.

In the Ref. 23, the neutral ${\rm CuSi}_n$ and ${\rm Si}_{n+1}$ clusters considering different spin configurations have been systematically investigated by using DFT/B3LYP. The authors have identified all isomers for each cluster and provide a detailed investigation of equilibrium geometries, charge transfer properties, relative stabilities, fragmentation energies, etc. . . . Our aim in this paper is not to reobtain these isomers, but to find approaches to improve the accuracy of various methods (in comparison with B3LYP, as reference) and to prescribe a new approach for predicting accurate properties of doped silicon clusters.

## $\text{Si}_2$ AND $\text{CuSi}$

The ground state of ${\rm Si}_2$ is known to be a spin triplet [23-52]. Their experimental bond length is 2.246 Å. A comparison of the performance of OLYP, OPW91, OB92, VSXC, PBE0, and B3LYP is illustrated in Table I. The PBE0 is clearly the best choice for predicting the bond length, including B3LYP functional in the list. The bond length obtained with OLYP is in good agreement with the value obtained with B3LYP.The agreement between the calculated and the experimental binding energy of ${\rm Si}_2$ decreases in the following order: OPW91 (the best agreement); OLYP; PBE0; VSXC; B3LYP; OB95 (the bad agreement).

The ground state for CuSi is a doublet [23]. Their experimental bond length is 2.280 Å. The differences in performance among all methods are small, but it is clear that OLYP and PBE0 are more accurate than the other functionals (Table I). The best functional in predicting the binding energy is OB95; however, all other functionals used in this work give a reasonable value. Note that the calculated values obtained with OLYP, OPW91, and PBE0 are in excellent agreement with the result obtained with B3LYP (taken as reference).

In the following clusters, as, in general, the experimental data are not available, all calculations are compared to those obtained with B3LYP.

## $\text{Si}_3$ AND $\text{CuSi}_2$

The ground state of ${\rm Si}_3$ is a ${\rm C}_{2{\rm v}}$ [23-52]. The OLYP and VSXC functionals are significantly more accurate in comparison with the others functionals. Note that all functionals give a reasonable results.

For ${\rm CuSi}_2$, the B3LYP calculated $r({\rm Si}_1—{\rm Cu})$ is 2.337 Å. This bond is slightly higher than that obtained with all other functionals used here. The best prediction is that obtained with OLYP (2.324 Å). Further the bond length $r({\rm S}_1—{\rm Si}_2)$ calculated with OLYP is the closest to the value obtained with B3LYP.

## $\text{Si}_4$ AND $\text{CuSi}_3$

As been noted for the above clusters, and in comparison with the prediction obtained with B3LYP, the OLYP is again the accurate method in

---

998 INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY DOI 10.1002/qua VOL. 108, NO. 5

EVALUATION OF EXCHANGE-CORRELATION FUNCTIONALS

<table>
<caption>TABLE I Geometries, point-group symmetries, and electronic states of $Si_{n+1}$ and $CuSi_n$ clusters.</caption>
<thead>
<tr>
<th>Cluster</th>
<th>OLYP</th>
<th>OPW91</th>
<th>OB95</th>
<th>VSXC</th>
<th>PBE0</th>
<th>B3LYP</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Si_2$ $D_{\infty V}$ $^3\Sigma_g$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}—\text{Si})$</td>
<td>2.298</td>
<td>2.165</td>
<td>2.162</td>
<td>2.156</td>
<td>2.265</td>
<td>2.280</td>
</tr>
<tr>
<td>$CuSi$ $C_{\infty V}$ $^2\Pi$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}—\text{Cu})$</td>
<td>2.246</td>
<td>2.232</td>
<td>2.221</td>
<td>2.235</td>
<td>2.243</td>
<td>2.251</td>
</tr>
<tr>
<td>$Si_3$ $C_{2V}$ $^1A_1$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_3)$</td>
<td>2.194</td>
<td>2.185</td>
<td>2.180</td>
<td>2.174</td>
<td>2.183</td>
<td>2.185</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_2)$</td>
<td>2.892</td>
<td>2.811</td>
<td>2.784</td>
<td>2.889</td>
<td>2.846</td>
<td>2.877</td>
</tr>
<tr>
<td>$\alpha(\text{Si}_1—\text{Si}_3—\text{Si}_2)$</td>
<td>82.455</td>
<td>80.083</td>
<td>79.357</td>
<td>83.263</td>
<td>81.372</td>
<td>82.348</td>
</tr>
<tr>
<td>$CuSi_2$ $C_{2V}$ $^2A_1$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Cu})$</td>
<td>2.324</td>
<td>2.303</td>
<td>2.290</td>
<td>2.311</td>
<td>2.322</td>
<td>2.337</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_2)$</td>
<td>2.179</td>
<td>2.166</td>
<td>2.164</td>
<td>2.161</td>
<td>2.151</td>
<td>2.170</td>
</tr>
<tr>
<td>$\alpha(\text{Si}_1—\text{Cu}—\text{Si}_2)$</td>
<td>55.923</td>
<td>56.081</td>
<td>56.400</td>
<td>55.763</td>
<td>55.191</td>
<td>55.320</td>
</tr>
<tr>
<td>$Si_4$ $D_{2h}$ $^1A_g$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_4)$</td>
<td>2.335</td>
<td>2.322</td>
<td>2.315</td>
<td>2.309</td>
<td>2.313</td>
<td>2.329</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_2)$</td>
<td>2.421</td>
<td>2.398</td>
<td>2.385</td>
<td>2.394</td>
<td>2.401</td>
<td>2.430</td>
</tr>
<tr>
<td>$\alpha(\text{Si}_1—\text{Si}_3—\text{Si}_2)$</td>
<td>62.462</td>
<td>62.169</td>
<td>62.002</td>
<td>62.437</td>
<td>62.521</td>
<td>62.893</td>
</tr>
<tr>
<td>$CuSi_3$ $C_{2V}$ $^2A_1$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Cu})$</td>
<td>2.271</td>
<td>2.249</td>
<td>2.233</td>
<td>2.263</td>
<td>2.263</td>
<td>2.279</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_3)$</td>
<td>2.265</td>
<td>2.258</td>
<td>2.243</td>
<td>2.247</td>
<td>2.237</td>
<td>2.265</td>
</tr>
<tr>
<td>$\alpha(\text{Si}_1—\text{Si}_3—\text{Si}_2)$</td>
<td>93.437</td>
<td>91.682</td>
<td>93.044</td>
<td>95.592</td>
<td>90.349</td>
<td>93.437</td>
</tr>
<tr>
<td>$\alpha(\text{Si}_1—\text{Cu}—\text{Si}_2)$</td>
<td>93.141</td>
<td>91.643</td>
<td>93.606</td>
<td>94.679</td>
<td>88.974</td>
<td>93.141</td>
</tr>
<tr>
<td>$Si_5$ $D_{3h}$ $^1A_1$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_2)$</td>
<td>2.965</td>
<td>2.964</td>
<td>2.976</td>
<td>2.922</td>
<td>2.951</td>
<td>2.947</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_3)$</td>
<td>2.321</td>
<td>2.300</td>
<td>2.288</td>
<td>2.301</td>
<td>2.306</td>
<td>2.329</td>
</tr>
<tr>
<td>$r(\text{Si}_3—\text{Si}_4)$</td>
<td>3.094</td>
<td>3.047</td>
<td>3.006</td>
<td>3.081</td>
<td>3.068</td>
<td>3.124</td>
</tr>
<tr>
<td>$CuSi_4$ $C_{2V}$ $^2A_1$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Cu})$</td>
<td>2.498</td>
<td>2.573</td>
<td>2.534</td>
<td>2.616</td>
<td>2.623</td>
<td>2.563</td>
</tr>
<tr>
<td>$r(\text{Si}_4—\text{Cu})$</td>
<td>2.366</td>
<td>2.406</td>
<td>2.387</td>
<td>2.431</td>
<td>2.401</td>
<td>2.360</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_2)$</td>
<td>2.431</td>
<td>2.438</td>
<td>2.428</td>
<td>2.432</td>
<td>2.398</td>
<td>2.438</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_3)$</td>
<td>2.359</td>
<td>2.358</td>
<td>2.350</td>
<td>2.353</td>
<td>2.353</td>
<td>2.354</td>
</tr>
<tr>
<td>$r(\text{Si}_1—\text{Si}_4)$</td>
<td>2.413</td>
<td>2.421</td>
<td>2.415</td>
<td>2.429</td>
<td>2.395</td>
<td>2.405</td>
</tr>
<tr>
<td>$\alpha(\text{Si}_3—\text{Si}_1—\text{Si}_2—\text{Si}_4)$</td>
<td>177.237</td>
<td>177.347</td>
<td>177.278</td>
<td>177.157</td>
<td>178.415</td>
<td>179.608</td>
</tr>
</tbody>
</table>

predicting the structural parameters for these systems.

## $Si_5$ AND $CuSi_4$

In the case of $Si_5$, while PBE0 is the best functional in predicting the bond length $r(\text{Si}_1—\text{Si}_2)$, the more reliable method for the two others bond lengths are obtained with OLYP functional. For $CuSi_4$, OLYP seems to perform better than the geometrical data in comparison to other functionals.

Note that for all systems the CPU time of OLYP are in average of 13% less economical than those of B3LYP.

## Charge Distributions

The net charge of Cu and Si atoms in the most stable isomers are listed in Table II. This table compares the ability of the computational methods to predict the charge. The net charge for the Cu atom in the $CuSi_n$ clusters, calculated with each method, is positive showing that the charge in the corresponding clusters transfer from the Cu to the $Si_n$ atoms. Among the DFT methods studied here and in comparison with the results obtained with B3LTP, OLYP is the best functional for predicting the net charge (considering the reference estimate obtained by B3LYP). Indeed, to compare all the

---

VOL. 108, NO. 5 DOI 10.1002/qua INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY 999

<table>
<caption>TABLE II. Natural charges for atoms in Si<sub>n+1</sub> and CuSi<sub>n</sub> clusters.</caption>
<thead>
<tr>
<th></th>
<th>OLYP</th>
<th>OPW91</th>
<th>OB95</th>
<th>VSXC</th>
<th>PBE0</th>
<th>B3LYP</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si<sub>3</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Si<sub>1</sub></td>
<td>0.189</td>
<td>0.174</td>
<td>0.165</td>
<td>0.199</td>
<td>0.202</td>
<td>0.20</td>
</tr>
<tr>
<td>Si<sub>2</sub></td>
<td>0.189</td>
<td>0.174</td>
<td>0.165</td>
<td>0.199</td>
<td>0.202</td>
<td>0.20</td>
</tr>
<tr>
<td>Si<sub>3</sub></td>
<td>−0.378</td>
<td>−0.348</td>
<td>−0.330</td>
<td>−0.398</td>
<td>−0.404</td>
<td>−0.41</td>
</tr>
<tr>
<td>CuSi<sub>2</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cu</td>
<td>0.428</td>
<td>0.464</td>
<td>0.450</td>
<td>0.416</td>
<td>0.446</td>
<td>0.40</td>
</tr>
<tr>
<td>Si<sub>1</sub></td>
<td>−0.214</td>
<td>−0.232</td>
<td>−0.225</td>
<td>−0.208</td>
<td>−0.223</td>
<td>−0.20</td>
</tr>
<tr>
<td>Si<sub>2</sub></td>
<td>−0.214</td>
<td>−0.232</td>
<td>−0.225</td>
<td>−0.208</td>
<td>−0.223</td>
<td>−0.20</td>
</tr>
<tr>
<td>Si<sub>4</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Si<sub>1</sub></td>
<td>−0.230</td>
<td>−0.233</td>
<td>−0.235</td>
<td>−0.227</td>
<td>−0.247</td>
<td>−0.23</td>
</tr>
<tr>
<td>Si<sub>2</sub></td>
<td>−0.230</td>
<td>−0.233</td>
<td>−0.235</td>
<td>−0.227</td>
<td>−0.247</td>
<td>−0.23</td>
</tr>
<tr>
<td>Si<sub>3</sub></td>
<td>0.230</td>
<td>0.233</td>
<td>0.235</td>
<td>0.227</td>
<td>0.247</td>
<td>0.23</td>
</tr>
<tr>
<td>Si<sub>4</sub></td>
<td>0.230</td>
<td>0.233</td>
<td>0.235</td>
<td>0.227</td>
<td>0.247</td>
<td>0.23</td>
</tr>
<tr>
<td>CuSi<sub>3</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cu</td>
<td>0.422</td>
<td>0.465</td>
<td>0.444</td>
<td>0.411</td>
<td>0.470</td>
<td>0.40</td>
</tr>
<tr>
<td>Si<sub>1</sub></td>
<td>−0.127</td>
<td>−0.158</td>
<td>−0.140</td>
<td>−0.105</td>
<td>−0.157</td>
<td>−0.11</td>
</tr>
<tr>
<td>Si<sub>2</sub></td>
<td>−0.127</td>
<td>−0.158</td>
<td>−0.140</td>
<td>−0.105</td>
<td>−0.157</td>
<td>−0.11</td>
</tr>
<tr>
<td>Si<sub>3</sub></td>
<td>−0.168</td>
<td>−0.146</td>
<td>−0.164</td>
<td>−0.201</td>
<td>−0.156</td>
<td>−0.18</td>
</tr>
<tr>
<td>Si<sub>5</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Si<sub>1</sub></td>
<td>−0.198</td>
<td>−0.177</td>
<td>−0.153</td>
<td>−0.212</td>
<td>−0.201</td>
<td>−0.22</td>
</tr>
<tr>
<td>Si<sub>2</sub></td>
<td>−0.198</td>
<td>−0.177</td>
<td>−0.153</td>
<td>−0.212</td>
<td>−0.201</td>
<td>−0.22</td>
</tr>
<tr>
<td>Si<sub>3</sub></td>
<td>0.132</td>
<td>0.118</td>
<td>0.103</td>
<td>0.141</td>
<td>0.134</td>
<td>0.15</td>
</tr>
<tr>
<td>Si<sub>4</sub></td>
<td>0.132</td>
<td>0.118</td>
<td>0.103</td>
<td>0.141</td>
<td>0.134</td>
<td>0.15</td>
</tr>
<tr>
<td>Si<sub>5</sub></td>
<td>0.132</td>
<td>0.118</td>
<td>0.103</td>
<td>0.141</td>
<td>0.134</td>
<td>0.15</td>
</tr>
<tr>
<td>CuSi<sub>4</sub></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cu</td>
<td>0.512</td>
<td>0.553</td>
<td>0.546</td>
<td>0.547</td>
<td>0.564</td>
<td>0.47</td>
</tr>
<tr>
<td>Si<sub>1</sub></td>
<td>−0.217</td>
<td>−0.231</td>
<td>−0.222</td>
<td>−0.218</td>
<td>−0.242</td>
<td>−0.19</td>
</tr>
<tr>
<td>Si<sub>2</sub></td>
<td>−0.217</td>
<td>−0.231</td>
<td>−0.222</td>
<td>−0.218</td>
<td>−0.242</td>
<td>−0.19</td>
</tr>
<tr>
<td>Si<sub>3</sub></td>
<td>0.040</td>
<td>0.041</td>
<td>0.024</td>
<td>0.033</td>
<td>0.051</td>
<td>0.04</td>
</tr>
<tr>
<td>Si<sub>4</sub></td>
<td>−0.119</td>
<td>−0.132</td>
<td>−0.126</td>
<td>0.104</td>
<td>−0.133</td>
<td>−0.12</td>
</tr>
</tbody>
</table>

methods, we calculated the mean deviation between the calculated values and the reference estimate. The mean deviations for the predicted net charge of metal atoms are 0.031, 0.071, 0.057, 0.034, and 0.070 with OLYP, OPW91, OB95, VSXC, and PBE0, respectively. Thus demonstrates again the excellent agreement between OLYP and B3LYP in predicting the charge transfer from the metal impurity to silicon clusters.

## Energetic Properties

To understand the effect of Cu on the structures and properties of Si<sub>n</sub>, we calculated various energetic properties: Firstly, the binding energies per atom (BE). On the other hand, as pointed by Ragha-

![](./images/811952383989907457_2.jpg)

FIGURE 1. The equilibrium geometries of the most stable neutral CuSi<sub>n</sub> and Si<sub>n +1</sub> clusters. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

EVALUATION OF EXCHANGE-CORRELATION FUNCTIONALS

![](./images/811952383989907457_3.jpg)

FIGURE 2. Calculated the binding energy per atom versus experimental binding energy per atom. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

vachari et al. [52-54], a better way of comparing the local stabilities of different sizes of $CuSi_n$ clusters and comparing the relative strength of Si—Si and Si—Cu interactions is the study of the fragmentation energies (FEs).

Figure 1 compares the ability of the computational methods to predict binding energy per atom versus their experimental data. Among the DFT methods studied here, the PBE0 has the lowest mean absolute deviations (MAD) of 0.064 eV. The MADs obtained with all functionals are in parentheses: VSXC (0.068 eV), OPW91 (0.074 eV), OLYP (0.124 eV), and 0B95 (0.211 eV). The MAD for the predicted binding energy obtained with B3LYP is about 0.196 eV. Note that the value of MAD obtained with CCSD(T)/6-31G* is 0.343 eV [55].

The binding energy per atom (BE) of $Si_n$ and $CuSi_n$ with respect to the number of atoms is shown in Figures 2-4, respectively. Firstly, the BE curves, calculated with different methods, are similar. In comparison with B3LYP method, OLYP functional is clearly superior compared to the other functionals for the calculation of binding energy for different clusters.

![](./images/811952383989907457_4.jpg)

FIGURE 3. Size dependence of the binding energy per atom of $Si_{n+1}$. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

![](./images/811952383989907457_5.jpg)

FIGURE 4. Size dependence of the binding energy per atom of $CuSi_n$. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

The BE curve for pure $Si_n$ clusters agrees well with the one obtained by Raghavachari et al. [54, 55] at the MP4/6-31G* level, in which the enhanced stability of $Si_4$ is reflected by slight local maxima. For $CuSi_n$ clusters, it seems that $CuSi_2$ has slightly enhanced stability. For all clusters sizes, the stabilities of $Si_{n+1}$ is greater than that of $CuSi_n$, indicating that, on an average, the Si—Si bond is stronger than the Si—Cu bond.

The FEs of pure $Si_{n+1}$ clusters are shown in Figure 5. All methods give a similar evolution. As been noted by Xiao et al. [23], the FE curve of $Si_{n+1}$ clusters reveals a size dependence similar to that obtained by Raghavachari et al. [54] at the MP4/6-

![](./images/811952383989907457_6.jpg)

FIGURE 5. Size dependence of the fragmentation energy of $Si_{n+1}$ with respect to $Si+Si_n$. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

VOL. 108, NO. 5 DOI 10.1002/qua INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY 1001

DKHISSI

31G*, which indicates a prominently enhanced stability at Si₄. Further, the differences in performance, compared to B3LYP, are small, but it is clear that OLYP is more accurate than the other functionals.

The FEs of CuSiₙ with respect to the fragmentation into both Cu + Siₙ and Si + CuSiₙ₋₁ is shown in Figures 6 and 7. As been noted before, all methods give a similar evolution. Further, an enhanced stability appears at MSi₂, in agreement with BE profile, and again, OLYP is the more appropriate method in comparison with B3LYP.

To conclude this part, we note the overall quality of DFT/OLYP method for prediction of various energetic properties of doped silicon clusters.

## Conclusions

With the increased computational resources of the last several years, DFT has emerged as one of the most used computational procedures for the field of Chemistry and Material science. In the field of electronics, the applications of DFT and especially with the popular B3LYP functional are of significant interest due to their reliable data. Further, the search of new alternative methods, getting high accuracy and minimizing computational time, is a topic of great importance. So, we have investigated the performance of different density functionals, in different categories, in combination with 6-311+G* basis set making comparisons to B3LYP with the same basis set. The reliability of these methods were evaluated based on their ability to reproduce known geometrical and energetical parameters experimentally or calculated with B3LYP (or high level wave methods when are available) for several Siₙ₊₁ and CuSiₙ clusters. The results indicate, in general, that the OLYP functional gives the best accuracy of testing functionals. These comparisons are very interesting because knowing that the hybrid functionals are computationally more demanding than the GGA schemes. So, the OLYP functional, the ideal alternative for B3LYP, is very promising for studies of larger metal impurities-doped silicon, and generally its uses for condensed-phase simulation of silicon would seem to be a promising avenue of research. Further, Conradie and Ghosh [56] demonstrated that this functional (OLYP) provides the best overall description of the spin state energetics of different transition-metal-Imido complexes and concluded that there is no reason to suppose that hybrid functionals are inherently better than pure functionals, as is sometimes claimed [57].

![](./images/811952383989907457_7.jpg)

FIGURE 6. Size dependence of the fragmentation energy of CuSiₙ with respect to Cu + Siₙ. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

![](./images/811952383989907457_8.jpg)

FIGURE 7. Size dependence of the fragmentation energy of CuSiₙ with respect to Si + CuSiₙ₋₁. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com.]

## References

1. Jarrold, M. F. Science 1991, 252, 1085.
2. Brown W. L.; Freeman, R. R.; Raghavachari, K.; Schluter, M. Science 1987, 235, 860.
3. Hayashi, S.; Kanzawa, Y.; Kataoka, M.; Nagarede, T.; Yamamoto, K. Phys D 1993, 26, 144.
4. Ho, K.-M.; Shvartsburg, A. A.; Pan, B.; Lu, Z.-Y.; Wang, C.-Z.; Wacker, J. G.; Fye, J.; Jarrold, M. F. Nature (London) 1998, 392, 582.
5. Hagelberg, F.; Leszczynski, J.; Murashov, V. THEOCHEM 1998, 454, 209.
6. Rata, I.; Shvartsburg, A. A.; Horoi, M.; Frauenheim, T.; Siu, K. W. M.; Jackson, K. A. Phys Rev Lett 2000, 85, 546.
7. Jarrold, M. F.; Bower, J. E. J Chem Phys 1992, 96, 9180.
8. Wang, J.; Han, J. G. J. Chem Phys 2005, 123, 244303.
9. Menon, M.; Subbaswamy, K. R. Chem Phys Lett 1994, 219, 219.
10. Hiraki, A. Surf Sci 1986, 168, 74.
11. Istratov, A. A.; Weber, E. R. Appl Phys A 1998, 66, 123.

---

1002 INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY DOI 10.1002/qua VOL. 108, NO. 5

# EVALUATION OF EXCHANGE-CORRELATION FUNCTIONALS

12. Wahl, U.; Vantomme, A.; Langouche, G.; Correia, J. G. Phys Rev Lett 2000, 84, 1495.

13. Beck, S. M. J Chem Phys 1989, 90, 6306.

14. Scherer, J. J.; Paul, J. B.; Collier, C. P.; Saykally, R. J. J Chem Phys 1995, 102, 5190.

15. Scherer, J. J.; Paul, J. B.; Collier, C. P.; Saykally, R. J. J Chem Phys 1995, 103, 113.

16. Scherer, J. J.; Paul, J. B.; Collier, C. P.; O'Keefe, A.; Saykally, R. J. J Chem Phys 1995, 103, 9187.

17. Kishi, R.; Iwata, S.; Nakajima, A.; Kaya, K. J Chem Phys 1997, 107, 3056.

18. Hiura, H.; Miyazaki, T.; Kanayama, T. Phys Rev Lett 2001, 86, 1733.

19. Zunger, A.; Lindefeldt, U. Phys Rev B 1982, 26, 5989.

20. Beeler, F.; Andersen, O. K.; Scheffler, M. Phys Rev B 1990, 41, 1603.

21. Woon, D. E.; Marynick, D. S.; Estreicher, S. K. Phys Rev B 1992, 45, 13383.

22. Estreicher, S. K. Phys Rev B 1999, 60, 5375.

23. Xiao, C.; Abraham, A.; Quinn, R.; Hagelberg, F.; Lester, W. A., Jr. J Phys Chem A 2002, 106, 11380.

24. Han, J. G.; Shi, Y. Y. Chem Phys 2001, 266, 33.

25. Hiura, H.; Miyazaki, T.; Kanayama, T. Phys Rev Lett 2001, 86, 1733.

26. Han, J. G.; Hagelberg, F. THEOCHEM 2001, 549, 165.

27. Xiao, C.; Hagelberg, F.; Lester, W. A. Phys Rev B 2002, 66, 75425.

28. Han, J. G.; Xiao, C.; Hagelberg, F. Struct Chem 2002, 13, 173.

29. Turker, L. THEOCHEM 2001, 548, 185.

30. Han, J. G.; Hagelberg, F. Chem Phys 2001, 263, 255.

31. Han, J. G. Chem Phys 2003, 286, 181.

32. Han, J. G.; Ren, Z. Y.; Sheng, L. S.; Zhang, Y. W.; Morales, J. A.; Hagelberg, F. THEOCHEM 2003, 625, 47.

33. Yuan, Z. S.; Zhu, L. F.; Tong, X.; Liu, X. J.; Xu, K. Z. THEO- CHEM 2002, 589, 229.

34. Wu, J.; Hagelberg, F. J Phys Chem A 2006, 110, 5901.

35. Wu, Z. J.; Su, Z. M. J Chem Phys 2006, 124, 184306.

36. Zhao, R. N.; Ren, Z. Y.; Guo, P.; Bai, J. T.; Zhang, C. H.; Han, J. G. J Phys Chem A 2006, 110, 4071.

37. Ren, Z. Y.; Li, F.; Gu, P.; Han, G. H. J Mol Struct Theochem 2005, 718, 165.

38. Zheng, W.; Niilles, J. M.; Radisic, D.; Bowen, K. H. J Chem Phys 2005, 122, 071101.

39. Ona, O.; Bazterra, V. E.; Caputo, M. C.; Ferraro, M. B.; Fuentealba, P.; Facelli, J. C. J Mol Struct Theochem 2004, 681, 149.

40. Han, J. G.; Ren, Z. Y.; Lu, B. Z. J Phys Chem A 2004, 108, 5100.

41. Xiao, C. Y.; Blundell, J.; Hagelberg, F.; Lester, W. A. Int J Quantum Chem 2004, 96, 416.

42. Handy, N. C.; Cohen, A. J Mol Phys 2001, 99, 403.

43. Becke, A. D. Phys Rev A 1988, 38, 3098.

44. Hoe, W.-M.; Cohen, A. J.; Handy, N. C. Chem Phys Lett 2001, 341, 319.

45. Staroverov, V.; Scuseria, G. E.; Tao, J.; Perdew, J. P. J Chem Phys 2003, 119, 12129.

46. Voorhis, T. V.; Scuseria, G. E. J Chem Phys 1998, 109, 400.

47. Perdew, J. P.; Burke, K.; Ernzerhof, M. Phys Rev Lett 1996, 77, 3865.

48. Gaussian 98, Revision A9; Gaussian, Inc: Pittsburgh, PA, 1998.

49. Lee, C.; Yang, W.; Parr, R. G. Phys Rev B 1998, 37, 785.

50. Perdew, J. P. Electronic Structure of Solids; Akademie: Ber- lin, 1991.

51. Becke, A. D. J Chem Phys 1996, 104, 1040.

52. Raghavachari, K. J Chem Phys 1986, 84, 5672.

53. Raghavachari, K.; Logovinski, V. Phys Rev Lett 1985, 55, 2853.

54. Raghavachari, K.; Rohlfing, C. M. J Chem Phys 1988, 89, 2219.

55. Zhu, X.; Zeng, X. C. J Chem Phys 2003, 118, 3558.

56. Conradie, J.; Ghosh, A. J Chem Theory Comput 2007, 3, 689.

57. Ghosh, A. J Biol Inorg Chem 2006, 11, 712.

---

VOL. 108, NO. 5
DOI 10.1002/qua
INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY
1003