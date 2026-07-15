# Hydrogen induced contrasting modes of initial nucleations of graphene on transition metal surfaces

Yexin Feng, Keqiu Chen, Xin-Zheng Li, Enge Wang, and Lixin Zhang

Citation: *J. Chem. Phys.* **146**, 034704 (2017); doi: 10.1063/1.4974178
View online: http://dx.doi.org/10.1063/1.4974178
View Table of Contents: http://aip.scitation.org/toc/jcp/146/3
Published by the American Institute of Physics

![](./images/811081291641389057_1.jpg)

# Hydrogen induced contrasting modes of initial nucleations of graphene on transition metal surfaces

Yexin Feng, $^{1}$ Keqiu Chen, $^{1}$ Xin-Zheng Li, $^{2}$ Enge Wang, $^{2}$ and Lixin Zhang $^{3,a)}$

$^{1}$School of Physics and Electronics, Hunan University, Changsha 410082, People's Republic of China
$^{2}$International Center for Quantum Materials and School of Physics, Peking University, Beijing 100871, People's Republic of China
$^{3}$School of Physics, Nankai University, Tianjin 300071, People's Republic of China

(Received 31 October 2016; accepted 4 January 2017; published online 18 January 2017)

Our first-principles calculations reveal that there exist contrasting modes of initial nucleations of graphene on transition metal surfaces, in which hydrogen plays the role. On Cu(100) and Cu(111) surfaces, an $sp^{2}$-type network of carbons can be automatically formed with the help of hydrogen under very low carbon coverages. Thus, by tuning the chemical potential of hydrogen, both of the nucleation process and the following growth can be finely controlled. In contrast, on the Ni(111) surface, instead of hydrogen, the carbon coverage is the critical factor for the nucleation and growth. These findings serve as new insights for further improving the poor quality of the grown graphene on transition metal substrates. *Published by AIP Publishing.* [http://dx.doi.org/10.1063/1.4974178]

## I. INTRODUCTION

In order to grow large-area and high quality graphene sheets, chemical vapor deposition (CVD) techniques on transition metal (TM) surfaces have been extensively exploited. $^{1-6}$ Currently, the Cu surfaces are highly preferred. The growth on Cu surfaces is self-limiting, with good control of the graphene layers. $^{3,7-11}$ Great efforts have been spent in improving the quality of the grown graphene sheets, $^{1-12}$ for which a fundamental insight into the atomistic mechanism of the growth is highly needed. Of course, to completely understand the whole growth process is difficult at present because in experiments a lot of growth parameters, such as substrate, temperature, vapor pressure, preannealing, and cooling, can affect the crystallinity of the graphene sheets significantly. $^{12}$ So, a combination of experimental and multiscale modeling studies should be employed to fulfill this task.

Hydrogen (H) is popular in the CVD environment of graphene growth, either coming from the feedstock gas of $H_{2}/CH_{4}$, or $CH_{4}$ pyrolysis, or substrate pretreating by $H_{2}$ gas, and can play different roles at various growth stages. $^{8-10,12-17}$ Some researchers believe that dissociative H atoms will occupy the surface active sites, inhibiting dehydrogenation of hydro-carbons and thus degrading the crystallinity of the graphene. $^{18}$ On the contrary, some researchers suggest that H atoms can clean the Cu surface and assist in the formation of carbon radicals. $^{13,17}$ Vlassiouk and co-workers even pointed out that graphene could not be grown in the absence of H atoms. $^{13}$ H atoms can also act as etchant, the role of which relies on the growth conditions. $^{9,13,14,16}$ H atoms can either etch the graphene to form hydrocarbons, inhibiting the graphene growth, $^{14}$ or remove the unorganized or defective graphene edges, improving the graphene quality. $^{13}$ Recently, using first-principles simulations, Zhang *et al.* reported that H plays a key role in the synthesis of bilayer/few-layer graphene by passivating the active edges. $^{19}$ We note that the role of hydrogen in the nucleation process, especially at the initial stage, is not fully attached and is highly unclear.

In the literature, the nucleation of graphene on TM surfaces has been investigated extensively, especially by calculations based on the density-functional theory (DFT). $^{11,12,19-26}$ First, the hydrocarbon molecules may dissociate on the surfaces, forming carbon monomers or dimers, or even larger carbon clusters. On Ni, Fe, Co, and Mo surfaces, the carbon adatoms will diffuse into the bulk first and then segregate to the surface upon the following cooling. On Cu and Au surfaces, the dissociated carbon atoms keep staying on the surface. $^{12}$ Once the carbon coverage having reached a critical value, the nucleation process starts. Carbon monomers are taken as the starting species of graphene nucleation by many studies in the history. $^{12,21,22,24}$ Recently, Wu *et al.* reported that carbon dimers instead of monomers are the dominant feeding species in the graphene epitaxial growth, $^{11}$ and larger carbon clusters in the form of chains can facilitate the graphene growth via cluster attachment. $^{23}$ Gao *et al.* pointed out that in the initial stage of graphene growth, on the Ni(111) surface, carbon takes the chain structure instead of the $sp^{2}$ cluster until the number of carbon atoms $(N_{C})>12.^{21}$ Similar trends are also expected on other TM surfaces. $^{22}$ We note that although H exists in the growth environment in large amount, it is completely ignored in these studies. The carbon chain structures mentioned in these studies, although energetically favorable, are far from the configuration of the $sp^{2}$ carbon atoms in graphene.

Cu and Ni surfaces are the most popular substrates for the graphene growth but the growth behaviors on the two surfaces are contrasting. $^{6,12}$ By far, the different C solubilities in Cu and Ni lattices are considered as the main cause. $^{29}$ H, although existing in the growth environment in large amount, has not been fully considered in the nucleation processes, which could be crucial in determining the quality of the grown graphene.

$^{a)}$Electronic mail: lxzhang@nankai.edu.cn

In this paper, we report a systematic study of the initial nucleation of graphene on Cu(111), Cu(100), and Ni(111) surfaces with H in the growth environment. On all of the surfaces, the adsorbed hydrocarbon clusters can be stabilized at high chemical potential of hydrogen ($\mu_{\rm H}$), while the corresponding pure carbon clusters are more stable at low $\mu_{\rm H}$. On Cu surfaces, the larger size of carbon cluster, the more stable the cluster is. On the other hand, on the Ni surface, the above trend takes place only when the carbon coverage is close to full. This indicates that larger carbon or hydrocarbon clusters can be formed spontaneously on Cu surfaces at any carbon coverage but not on the Ni surface. Specifically for ${\rm C}_6$ and ${\rm C}_6{\rm H}_x$ clusters, on Cu surfaces, ${\rm C}_6$ favorably takes the chain structure while ${\rm C}_6{\rm H}_x$ takes the ring structure. The ${\rm C}_6{\rm H}_x$ rings can further easily coalesce to form larger islands of graphene. While on the Ni surface, both of ${\rm C}_6$ and ${\rm C}_6{\rm H}_x$ clusters take only the chain structure. Therefore, the high quality of single layer graphene grown on Cu surfaces benefits from the presence of H.

## II. COMPUTATIONAL METHODS

The calculations are performed within the framework of density functional theory as implemented in the Vienna Ab initio Simulation Package (VASP).$^{27}$ The Kohn-Sham wave functions are expanded in a plane wave basis set with a cutoff energy of 500 eV. The projector-augmented wave (PAW) method and PBE potential for the exchange-correlation functional are used. Four-layer slab models with surface periodicity of $9 \times 9$, $6 \times 6$ and $3 \times 3$ are used to describe the Cu and Ni surfaces under different carbon coverages, in which the bottom layer is fixed at the optimized bulk positions.$^{11}$ The Monkhorst-Pack (MP) k-point meshes are $2 \times 2 \times 1$, $3 \times 3 \times 1$ and $5 \times 5 \times 1$, respectively. A force acting on each atom of $<$0.02 eV/Å is used as the criterion of convergence. For carbon coverages of 0.074 ML and 0.667 ML, the supercells with $9 \times 9$ and $3 \times 3$ surface periodicity are used, respectively. In the calculations of the ${\rm C}_1$, ${\rm C}_2$, and ${\rm C}_3$ clusters, 6, 3, and 2 pairs of the clusters are placed on the surfaces to keep the carbon coverage a constant. To study the coalescence of the clusters on the surfaces, the so called climbing image nudged elastic band method (cNEB) is employed, using a supercell with $6 \times 6$ surface periodicity.$^{28}$

The formation energy of an adsorbed hydrocarbon or C cluster is given by

$$
{\rm E_f} = {\rm E_a} - {\rm E_{metal}} - {\rm n} \times \mu_{\rm C} - {\rm m} \times \mu_{\rm H}, \tag{1}
$$

where ${\rm E_a}$ is the total energy of the adsorbed system, ${\rm E_{metal}}$ is the total energy of the reference metal surface, and n and m are the number of C and H atoms in the hydrocarbon or C cluster. The chemical potential of C ($\mu_{\rm C}$) is the energy per atom in graphene. The chemical potential of H ($\mu_{\rm H}$) is tunable during the growth, depending on the working temperature and ${\rm H_2}$ partial pressure.$^{26}$ Most of the graphene CVD growth occurs at a temperature range of 800 K–1400 K and an ${\rm H_2}$ partial pressure range of $10^{-4}$–$10^2$ mbar. Thus, the low $\mu_{\rm H}$ value of $-$1.6 eV corresponds to the high temperature and low partial pressure within the ranges, and the high $\mu_{\rm H}$ value of $-$0.6 eV corresponds to the low temperature and high partial pressure.$^{26}$

Some discussions on the influences of dispersion force and finite temperature are included in the supplementary material.

## III. RESULTS AND DISCUSSION

As the first step, we investigate the relative stabilities of adsorbed C ($-{\rm C_n}$) and hydrocarbon ($-{\rm C_nH_n}$) clusters on Cu(111), Cu(100), and Ni(111) surfaces for n = 1, 2, 3, and 6. The optimized atomic structures of the clusters on Cu(111) are illustrated in Figure 1. It can be seen that, without H, the carbon atoms tend to have more nearest neighboring Cu atoms. With increasing of n, the C atoms tend to form a chain-like cluster. With H atoms in the clusters, the chains become zigzag. For n = 6, the ring structure becomes favorable where a surface Cu atom locates below the center of the cluster. On Cu(100) and Ni(111) surfaces, the structures of the clusters are similar and shown in the supplementary material.

The corresponding formation energies of these clusters are calculated based on Eq. (1), and the results are shown in Figure 2. On the Cu(111) surface, we can see that, regardless of C coverage, all of the ${\rm C_n}$ clusters are favored under low $\mu_{\rm H}$ and the corresponding ${\rm C_nH_n}$ clusters are favored under high $\mu_{\rm H}$. This indicates that structural transformations between ${\rm C_n}$ and ${\rm C_nH_n}$ can be induced by tuning the chemical potential of H in the growth environment. We can also see that the ${\rm C_2}$ or ${\rm C_3}$ (${\rm C_2H_2}$ or ${\rm C_3H_3}$) cluster is much more favored than ${\rm C_1(C_1H_1)}$, and the ${\rm C_6(C_6H_6)}$ cluster is more favored than the ${\rm C_2}$ or ${\rm C_3}$ (${\rm C_2H_2}$ or ${\rm C_3H_3}$) cluster. This clearly indicates that on the Cu(111) surface, the C atoms prefer to form larger clusters. Last but not least, we see a structural transformation from one dimensional chain to zero dimensional ring for the most favorable clusters of n = 6. This indicates that the $\rm sp^2$ network of graphene can be spontaneously formed by just tuning the chemical potential of H in the CVD growth environment. From some previous theoretical works, we know that at the initial nucleation stage, to form the $\rm sp^2$ network of pure C atoms is not easy.$^{21,22}$

The above results for the Cu(111) surface apply to the Cu(100) surface too, which indicates that the carbon nucleation process on Cu surfaces has no obvious preference on the orientation of the substrate, which agrees with the experiments very well.

On the Ni(111) surface, the ${\rm C_nH_n}$ clusters can also be stabilized under high chemical potential of H, similar to that on the Cu surfaces. But the nucleation process is quite different

![](./images/811081291641389057_2.jpg)

FIG. 1. Representative atomic structures of most stable (a) ${\rm C_n}$ and (b) ${\rm C_nH_n}$ clusters on the Cu(111) surface. The corresponding structures on Cu(100) and Ni(111) surfaces are similar and not shown. Light blue (brown, red) balls are Cu(C, H) atoms.

![](./images/811081291641389057_3.jpg)

FIG. 2. The formation energies (per carbon atom) of the adsorbed $C_n$ and $C_nH_n$ clusters at low ($\Theta = 0.074$ monolayer) and high carbon coverage ($\Theta = 0.667$ monolayer) on Cu(111), Cu(100), and Ni(111) surfaces as functions of the chemical potential of H ($\mu_H$). The corresponding atomic structures can be found in Figure 1. The dashed lines indicate the upper and lower limits of the real experimental conditions for the graphene CVD growth.

from that on the Cu surfaces. As shown in Figure 2(f), at high carbon coverage, similar to that on the Cu surfaces, the larger clusters are more favored than the smaller clusters. But it is not the case for low carbon coverage, as seen in Figure 2(c). This indicates that on the Ni(111) surface, the carbon coverage is an important factor for the spontaneous nucleation as well as the following growth. Larger carbon or hydrocarbon clusters can be formed spontaneously on the Ni surface only at high C coverage. From Figure 2(f), we can also see that the most favored $C_6H_6$ cluster takes the chain structure rather than the ring structure as they do on the Cu surfaces. As some previous investigations of graphene nucleation on the Ni(111) surface showed, the nucleated carbon clusters still need to go through the structural transformation from the 1D chain to 2D sp$^2$ network during the initial growth of graphene.$^{21,22}$ The point is that, unlike on the Cu surfaces, the sp$^2$ carbon network cannot be formed spontaneously on the Ni(111) surface even with the help of H.

In the above discussions, two n = 6 clusters, the $C_6$ (without H) and the $C_6H_6$ (all of the carbon atoms are hydrogenated) are considered, respectively, corresponding to H poor and rich conditions. Between the two extreme conditions, $C_6H_x$ (x = 1–6) clusters may also exist, with their structures representatively shown in Figure 3(d). The atomic structures of them are shown in Figure 3(d). Their formation energies are shown in Figures 3(a)–3(c) under three specific chemical potentials of H.

From these figures, we can see that on the Ni(111) surface, the chain structures are always more favored than the ring structures. We can also see that under high $\mu_H$ (Figure 3(a)), the most favored cluster is not fully hydrogenated, with x roughly between 3 and 5; under low $\mu_H$ (Figure 3(c)), the most favored cluster is $C_6$, completely not hydrogenated; under medium $\mu_H$ (Figure 3(b)), the most favored cluster is $C_6H_x$ with x roughly between 0 and 3. This indicates that on the Ni(111) surface, the stable chain structures may be hydrogenated in different extent, depending strongly on the growth conditions.

![](./images/811081291641389057_4.jpg)

FIG. 3. The formation energies (per carbon atom) of the most favored $C_6H_x$ (x = 0, 3, 5, 6) in the ring or chain structure at (a) high, (b) medium, and (c) low $\mu_H$ on Cu(111) and Ni(111) surfaces. (d) The atomic structures for the chain and ring structures with x = 3 and 5. For x = 0 and 6, the structures are shown in Figure 1.

![](./images/811081291641389057_5.jpg)

FIG. 4. Energy profiles for the coalescing of (a) two identical $C_6H_5$ rings to form the larger $C_{12}H_{10}$ cluster, (b) two identical $C_6H_6$ rings to form the larger $C_{12}H_{10}$ cluster, releasing one $H_2$ at the same time, on Cu surfaces, (c) two identical $C_6$ chains to form the larger $C_{12}$ cluster, and (d) two $C_6H_x$ chains to form the larger $C_{12}H_y$ cluster on the Ni surface. The atomic configurations of the initial, transition, and final states are shown in the insets. Light blue (green, brown, red) balls are Cu (Ni, C, H) atoms.

On the Cu(111) surface, on the other hand, under high $\mu_{\text{H}}$ (Figure 3(a)), the most favored cluster is fully hydrogenated with x = 6, taking the ring structure; under low $\mu_{\text{H}}$ (Figure 3(c)), the most favored cluster is $C_6$ but in the chain structure; under medium $\mu_{\text{H}}$ (Figure 3(b)), the most favored cluster is $C_6H_x$ with x roughly between 3 and 6, still in the ring structure. On the Cu(100) surface, the favored structures are the same as that on the Cu(111) surface and not shown repeatedly. The above results indicate that on the Cu surfaces, both the ring and chain structures may exist and the ring structures may be partially hydrogenated, depending also on the growth condition.

During the nucleation process, one important step for adsorbed clusters is to coalesce to form larger clusters or islands. On Cu surfaces, the energy profiles for the process of merging of two $-C_6H_5$ clusters are shown in Figure 4(a). On the Cu(111) surface, the barrier is $\sim$1.20 eV and it is $\sim$1.0 eV on the Cu(100) surface. These values are in the same orders as the barriers previously reported for the attachment of the $C_2$ cluster to a graphene island.$^{11}$ Under the ordinary growth temperatures between 800 K and 1200 K, these barriers could be easily overcome. More importantly, on Cu surfaces, the merging of two $C_6H_5$ clusters is exothermic. This indicates that the coalescing process of these $C_6H_x$ clusters can take place at a very high rate. If the clusters are fully hydrogenated, as shown in Figure 4(b), the barrier for the merging is as high as $\sim$3 eV. To further release an $H_2$ molecule, the additional barrier is $\sim$1.5 eV [on the Cu(111) surface] or $\sim$2.5 eV [on the Cu(100) surface]. This indicates that in order to accelerate the coalescing of the smaller clusters, tuning $\mu_{\text{H}}$ to favor the formation of the partially hydrogenated ring cluster is the key. From the above formation energy calculation results in Figure 3(b), we can see that medium $\mu_{\text{H}}$ favors the formation of partially hydrogenated $-C_6H_x$ clusters, which can boost the coalescing process of such clusters to form a larger island.

On the Ni(111) surface, the influence of hydrogen on the coalescing process of the small clusters is much weaker than that on the Cu surfaces, as schematically shown in Figures 4(c) and 4(d). Instead, the carbon coverage plays a more important role. The coalescing process is endothermic under low carbon coverages. To accelerate the coalescing process, a high carbon coverage on the surface is needed. Because the high carbon coverage does not benefit the quality control of graphene, the graphene grown on the Ni(111) surface would intrinsically have worse quality than that grown on the Cu surfaces.

### IV. CONCLUSIONS

In summary, we have studied the role of hydrogen in the initial nucleation and the coalescing processes for graphene growth on the two most common substrates, Cu and Ni, by

using first-principles calculations. The results on different Cu surfaces are similar but are contrasting to that on the Ni(111) surface. On the Cu surfaces, the existence of hydrogen in the growth environment can favor the formation of carbon rings, and the carbon rings can easily coalesce to form a larger sp² network of carbon, the graphene island. On the other hand, on the Ni(111) surface, the hydrogen favors the formation of zigzag carbon chains. The chains can also coalesce into larger island, but only favored at high carbon coverage. This new picture of graphene nucleation is expected to be a significant step forward toward a full understanding of the graphene growth on transition metal surfaces.

SUPPLEMENTARY MATERIAL

See **supplementary material** for the atomic structures of the adsorbed clusters on Cu(100) and Ni(111) surfaces and the temperature and magnetic effects on the stabilities of the clusters.

ACKNOWLEDGMENTS

The work is supported by the NSF of China with Grant Nos. 11274179, 11574157, 11604092, and 11634001 and National 973 projects of China with No. 2012CB921900.

¹A. K. Geim, *Science* **324**, 1530 (2009).
²K. S. Kim, Y. Zhao, H. Jang, S. Y. Lee, J. M. Kim, K. S. Kim, J.-H. Ahn, P. Kim, J.-Y. Choi, and B. H. Hong, *Nature* **457**, 706 (2009).
³X. Li, W. Cai, J. An, S. Kim, J. Nah, D. Yang, R. Piner, A. Velamakanni, I. Jung, E. Tutuc, S. K. Banerjee, L. Colombo, and R. S. Ruoff, *Science* **324**, 1312 (2009).
⁴Q. Yu, L. A. Jauregui, W. Wu, R. Colby, J. Tian, Z. Su, H. Cao, Z. Liu, D. Pandey, D. Wei, T. F. Chung, P. Peng, N. P. Guisinger, E. A. Stach, J. Bao, S.-S. Pei, and Y. P. Chen, *Nat. Mater.* **10**, 443 (2011).
⁵P. Y. Huang, C. S. Ruiz-Vargas, A. M. van der Zande, W. S.Whitney, M. P. Levendorf, J. W. Kevek, S. Garg, J. S. Alden, C. J. Hustedt, Y. Zhu, J. Park, P. L. McEuen, and D. A. Muller, *Nature* **469**, 389 (2011).

⁶T. Wu, X. Zhang, Q. Yuan, J. Xue, G. Lu, Z. Liu, H. Wang, H. Wang, F. Ding, Q. Yu, X. Xie, and M. Jiang, *Nat. Mater.* **15**, 43 (2015).
⁷X. Li, C. W. Magnuson, A. Venugopal, R. M. Tromp, J. B. Hannon, E. M. Vogel, L. Colombo, and R. S. Ruoff, *J. Am. Chem. Soc.* **133**, 2816 (2011).
⁸L. Tao, J. Lee, H. Chou, M. Holt, R. S. Ruoff, and D. Akinwande, *ACS Nano* **6**, 2319 (2012).
⁹Z. Yan, J. Lin, Z. Peng, Z. Sun, Y. Zhu, L. Li, C. Xiang, E. L. Samuel, C. Kittrell, and J. M. Tour, *ACS Nano* **6**, 9110 (2012).
¹⁰Q. Li, H. Chou, J.-H. Zhong, J.-Y. Liu, A. Dolocan, J. Zhang, Y. Zhou, R. S. Ruoff, S. Chen, and W. Cai, *Nano Lett.* **13**, 486 (2013).
¹¹P. Wu, Y. Zhang, P. Cui, Z. Li, J. Yang, and Z. Zhang, *Phys. Rev. Lett.* **114**, 216102 (2015).
¹²C.-M. Seah, S.-P. Chai, and A. R. Mohamed, *Carbon* **70**, 1 (2014).
¹³I. Vlassiouk, M. Regmi, P. Fulvio, S. Dai, P. Datskos, G. Eres, and S. Smirnov, *ACS Nano* **5**, 6069 (2011).
¹⁴Y. Zhang, Z. Li, P. Kim, L. Zhang, and C. Zhou, *ACS Nano* **6**, 126 (2012).
¹⁵Y. Jin, B. Hu, Z. Wei, Z. Luo, D. Wei, Y. Xi, Y. Zhang, and Y. Liu, *J. Mater. Chem. A* **2**, 16208 (2014).
¹⁶S. Choubak, P. L. Levesque, E. Gaufres, M. Biron, P. Desjardins, and R. Martel, *J. Phys. Chem. C* **118**, 21532 (2014).
¹⁷K. Li, C. He, M. Jiao, Y. Wang, and Z. Wu, *Carbon* **74**, 255 (2014).
¹⁸M. Losurdo, M. M. Giangregorio, P. Capezzuto, and G. Bruno, *Phys. Chem. Chem. Phys.* **13**, 20836 (2011).
¹⁹X. Y. Zhang, L. Wang, J. Xin, B. I. Yakobson, and F. Ding, *J. Am. Chem. Soc.* **136**, 3040 (2014).
²⁰P. Lacovig, M. Pozzo, D. Alfè, P. Vilmercati, A. Baraldi, and S. Lizzit, *Phys. Rev. Lett.* **103**, 166101 (2009).
²¹J. Gao, J. Zhao, and F. Ding, *J. Am. Chem. Soc.* **134**, 6204 (2012).
²²J. Gao, Q. Yuan, H. Hu, J. Zhao, and F. Ding, *J. Phys. Chem. C* **115**, 17695 (2011).
²³P. Wu, H. Jiang, W. Zhang, Z. Li, Z. Hou, and J. Yang, *J. Am. Chem. Soc.* **134**, 6045 (2012).
²⁴Y. Feng, X. Yao, Z. Hu, J. J. Xu, and L. Zhang, *Phys. Rev. B* **87**, 195421 (2013).
²⁵W. Chen, P. Cui, W. Zhu, E. Kaxiras, Y. Gao, and Z. Zhang, *Phys. Rev. B* **91**, 045408 (2015).
²⁶H. Shu, X. M. Tao, and F. Ding, *Nanoscale* **7**, 1627 (2015).
²⁷G. Kresse and J. Hafner, *Phys. Rev. B* **47**, 558 (1993); **49**, 14251 (1994).
²⁸G. Henkelman, B. P. Uberuaga, and H. Jónsson, *J. Chem. Phys.* **113**, 9901 (2000).
²⁹X. Li, W. Cai, L. Colombo, and R. S. Ruoff, *Nano Lett.* **9**, 4268 (2009).

![](./images/811081291641389057_6.jpg)