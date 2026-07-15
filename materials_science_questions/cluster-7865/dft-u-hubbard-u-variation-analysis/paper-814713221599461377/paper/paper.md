# Density Functional Theory Study on Spin States of $\text{LaCoO}_3$ at Room Temperature

Xiang-bo Zhang, Gang Fu*, Hui-lin Wan*

State Key Laboratory for Physical Chemistry of Solid Surfaces; Department of Chemistry, College of Chemistry & Chemical Engineering, Xiamen University, Xiamen 361005, China

(Dated: Received on November 27, 2013; Accepted on December 4, 2013)

The electronic structure of the perovskite $\text{LaCoO}_3$ at room temperature structure (293 K) was calculated by using PBE, PBE+$U$ and HSE. Different spin configurations have been considered. Our calculations showed that the choice of the Hubbard $U$ parameter in DFT+$U$ and mixing factor $\alpha$ in HSE significantly influenced the band gap as well as relative energies. For the spin exited states, the optimal value for $U$ and $\alpha$ were 3.0 eV and 0.05, respectively. Our calculation also emphasized that when $U$$\geq$5.0 eV, PBE+$U$ would lead to unreasonable electronic structure and energy order.

Key words: Perovskite, $\text{LaCoO}_3$, Density functional theory

## I. INTRODUCTION

Rare earth perovskite-type oxides, *i.e.* $\text{RMO}_3$, have shown a great prospect in environmental catalysis [1]. Among them, $\text{LaCoO}_3$ exhibited high activity and stability in catalytic combustion as well as NO removal [2]. As an environmental catalyst, how to achieve high reactivity under mild conditions, especially at room temperature, attracted a broad attention. It is of importance to understand the electronic structure of $\text{LaCoO}_3$. It has been documented that there exists a temperature inducing transition from a nonmagnetic to a magnetic state [3]. At very low temperature (<90 K), $\text{Co}^{3+}$ is in the low spin state (LS, $\text{t}_{2\text{g}}^6\text{e}_{\text{g}}^2$, $S$=0); at about 90 K, $\text{LaCoO}_3$ underwent a thermal excitation to generate a magnetic state, which was supposed to be of the intermediate spin (IS, $\text{t}_{2\text{g}}^5\text{e}_{\text{g}}^1$, $S$=1); when the temperature was up to 1210 K, the high spin (HS, $\text{t}_{2\text{g}}^4\text{e}_{\text{g}}^2$, $S$=2) state would become dominated. In fact, the electronic properties were also temperature dependent. At 0–500 K, $\text{LaCoO}_3$ is a semi-conductor, while a transition from insulator to metal occurs at about 535 K.

It should be noted that the theoretical description of such temperature induced effect was a tough problem. Density functional theory (DFT) calculations have been carried out on bulky $\text{LaCoO}_3$ [4–19]. On one hand, the DFT calculations only concern the ground state at 0 K. On the other hand, there exists strong Coulomb interaction between 3d electrons which could not be described properly by using local density approximation (LDA) [4] or generalized gradient approximation (GGA). Korotin *et al.* have proposed a possible way to deal with the problems [5]. They assumed that the spin state transition was associated with thermal lattice expansion. In addition, they introduced Hubbard $U$ parameter to describe the Coulomb repulsion among the 3d electrons, *i.e.* LDA+$U$. By exploring different spin states with the structures in a broad range of temperatures, it was also proposed that $\text{LaCoO}_3$ in LS or HS states was semi-conductor, while IS state was of half metallic [5]. These opinions were supported by the following works using LDA+$U$ [6, 8, 15, 17] and GGA+$U$ [7, 16, 17]. Hsu *et al.* pointed out that the parameter $U$ was structural dependent [12], while Lee *et al.* proposed that $U$ value should be adjusted to match the experimental oxygen binding energy [13]. Pandey *et al.* have suggested that besides Hubbard $U$, the spin-orbit coupling (SOC) should be taken into account to obtain reasonable valence band spectra [10]. These DFT calculations assumed that the spin states on $\text{Co}^{3+}$ ions were "homogeneous". As a matter of fact, $\text{Co}^{3+}$ in $\text{LaCoO}_3$ may not be equivalent, that is to say, some $\text{Co}^{3+}$ ions were in LS states and others HS states. Knížek *et al.* found that LS-HS mixed solutions were energetically more stable than IS one [9, 11]. Laref *et al.* demonstrated that there existed a LS-IS/HS-IS two-stage process during the magnetic transition [18]. Very recently, hybrid DFT (PBE0 or HSE) was also employed to investigate the physicochemical properties of $\text{LaCoO}_3$, such as phonon spectrum [14] and electronic properties [19] on the ground state. And the mixing factor $\alpha$ was also suggested to be system dependent [19].

In this work, we presented a systematic DFT investigation on $\text{LaCoO}_3$ with the structure at room temperature. All possible spin configurations have been considered, including LS, IS, HS, and LS-HS mixed states. Different approximations of DFT, such as PBE, HSE,

*Authors to whom correspondence should be addressed. E-mail:
gfu@xmu.edu.cn, hlwan@xmu.edu.cn

and PBE+$U$, were performed to explore the electronic structures of $LaCoO_3$. The optimum value for $U$ and $\alpha$ was also obtained, which would be suitable to examine the catalytic processes under mild condition.

## II. COMPUTATIONAL DETAILS

All calculations were performed with the Vienna *ab initio* simulation package (VASP5.2) [20, 21]. The projector augmented plane wave (PAW) was carried out to describe electron-ion interactions, with an energy cutoff of 400 eV. Herein, three types of DFT approximations, such as PBE [22], PBE+$U$ [23, 24], and HSE [25], were used. PBE [22] is one of the most popular GGA functional, however it cannot properly describe the full Coulomb and exchange interactions between 3d electrons. This error can be corrected with the PBE+$U$ method in which an "on-site" potential was introduced [23]. Here, a simple PBE+$U$ scheme, proposed by Dudarev *et al.* [24], was adopted. In this case, the strength of the penalty function can be parameterized by single variable $U_{\text{eff}}$=$U$-$J$. For the sake of brevity, we used $U$ instead of $U_{\text{eff}}$ in following sections. Similarly to PBE+$U$, hybrid DFT can also improve the description of transition metal oxide with partially occupied d orbitals. In the screened hybrid DFT (HSE) [25], the slowly decaying long-ranged part of the exact exchange was replaced by the density functional counterpart. In this scenario, there are two important parameters, $U$ and $\alpha$. The former controls the range separation between long-range and short-range, and the latter controls the mixing ratio of exact exchange, *i.e.* $E_x^{\text{HFF}}$. The $k$-points sampling was generated following the Monkhorst-Pack procedure with a $5{\times}5{\times}3$ mesh. For HSE calculation, the Hatree-Fock kernel was calculated using single $k$-points, *i.e.* $\Gamma$ point.

The structures of $LaCoO_3$ at 4.2–1248 K have been determined by using neutron diffraction [26]. It was shown that at 293 K, $LaCoO_3$ crystallizes in a rhombohedral space group $R\overline{3}c$ with cell parameters of $a$=$b$=$c$=5.3778 Å and $\alpha$=$\beta$=$\gamma$=60.798° (Fig.1). In order to explore different spin states, we double the cell and altogether $4\ \text{Co}^{3+}$ involved in our calculations.

![](./images/814713221599461377_1.jpg)

FIG. 1 The crystal structure of $LaCoO_3$ ($R\overline{3}c$ space group).

![](./images/814713221599461377_2.jpg)

FIG. 2 Total DOS and projected DOS of LS state with 293 K experimental structure based on PBE, PBE+$U$ and HSE.

## III. RESULTS AND DISCUSSION

Figure 2 depicts the density of states (DOS) for LS calculated using different methods. According to crystal field theory, five d-orbitals should be split into triply degenerate $\text{t}_{2\text{g}}$ and doubly degenerate $\text{e}_{\text{g}}$ subsets in octahedral field. In principle, all six d electrons of $\text{Co}^{3+}$ would be placed on $\text{t}_{2\text{g}}$ states, and $\text{e}_{\text{g}}$ states were empty, hence opening a band gap. Experimentally, the band gap of $LaCoO_3$ was estimated to be 0.3–0.9 eV [3, 27, 28]. However, PBE predicted that $LaCoO_3$ at LS was a conductor rather than a semi-conductor opposite to experiment. This might be due to that PBE usually overestimated the tendency of delocalization.

When Hubbard $U$ was introduced (PBE+$U$), the occupied states were pushed down, while empty states went upward, as shown in Fig.2. We can see that the width of band gap clearly depended on the value of $U$. With increase of $U$ value, the band gaps increased from 0.6 eV ($U$=3.0 eV), to 1.5 eV ($U$=5.0 eV), to 2.3 eV ($U$=7.0 eV), consistent with previous calculations [5, 7, 9–11, 13, 16–18]. For HSE calculation, it has been reported that $\alpha$ might also be system or property dependent [19, 29, 30]. Our calculation showed that the standard HSE ($\alpha$=0.25) delivered a band gap of 2.4 eV, in agreement with previous PBE0 [14] and HSE results [19], but far beyond the experimental mea-

<table><caption>TABLE I Electronic energies $E$ for LaCoO$_3$ at different spin states with 293 K structure.</caption>
<thead>
  <tr>
    <th>Methods</th>
    <th></th>
    <th colspan="2"></th>
    <th colspan="2">FM</th>
    <th></th>
    <th colspan="2">AFM</th>
  </tr>
  <tr>
    <th></th>
    <th></th>
    <th>LS</th>
    <th>IS</th>
    <th>LS-HS (3:1)</th>
    <th>LS-HS (1:1)</th>
    <th></th>
    <th>LS-HS (1:1)</th>
    <th>HS</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>PBE+$U$</td>
    <td>$U$=3.0</td>
    <td>−36.08325</td>
    <td>−36.20111</td>
    <td>−36.13340</td>
    <td>−36.15812</td>
    <td></td>
    <td>−36.15104</td>
    <td>−36.11845</td>
  </tr>
  <tr>
    <td></td>
    <td>$U$=3.0 OPT</td>
    <td>−36.10600</td>
    <td>−36.20502</td>
    <td>−36.17916</td>
    <td>−36.20606</td>
    <td></td>
    <td>−36.20437</td>
    <td>−36.15305</td>
  </tr>
  <tr>
    <td></td>
    <td>$U$=5.0</td>
    <td>−34.98474</td>
    <td>−35.30817</td>
    <td>−35.11940</td>
    <td>−35.22918</td>
    <td></td>
    <td>−35.21369</td>
    <td>−35.40218</td>
  </tr>
  <tr>
    <td></td>
    <td>$U$=7.0</td>
    <td>−33.96390</td>
    <td>−34.60114</td>
    <td>−34.21465</td>
    <td>−34.42635</td>
    <td></td>
    <td>−34.39556</td>
    <td>−34.81860</td>
  </tr>
  <tr>
    <td>HSE06</td>
    <td>$\alpha$=0.05</td>
    <td>−40.93822</td>
    <td>−40.91217</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>$\alpha$=0.15</td>
    <td>−47.07696</td>
    <td>−47.12611</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>$\alpha$=0.25</td>
    <td>−53.41889</td>
    <td>−53.59815</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

LS: low spin, IS: intermediate spin, HS: high spin, FM: ferromagnetic, AFM: anti-ferromagnetic. OPT: optimized structure.

surement. We noticed that even a small $\alpha$, *i.e.* 0.05, would diminish the DOS near the Fermi level, yielding a band gap of 0.2 eV. Thus, the best agreement with experiment was achieved in the range of 0.05–0.15. Previously, *He et al.* also suggested that $\alpha$=0.05 led to the most accurate optimized geometry and reasonable band gaps for LaCoO$_3$ [19]. Although the gap could be opened by using PBE+$U$ and HSE, the composition of the valence bands might be dramatically different between them, especially on the top of the valence bands. For HSE ($\alpha$=0.05–0.15), the bands in the energy range from −2 eV to 0 eV originated mainly from Co3d states but had a few admixture from O2p states. However, when $U$$\geq$5.0 eV, the occupied states close to the Fermi level were mainly formed by O2p states, presenting an unphysical picture. Thus, cautions should be paid when large $U$ value was adopted [16–18]. Interestingly, PBE+$U$ with $U$=3.0 eV could give reasonable electronic structure as the peaks position and the composition of each state compared well with those of HSE with relative small $\alpha$.

Table I listed the electronic energies for LaCoO$_3$ at different spin states with 293 K structure. Here, the LS, IS, HS as well as LS-HS mixture states were considered, and the possible ferromagnetic (FM) and anti-ferromagnetic (AFM) orders were also taken into account. As reported previously, the magnetic moments for the self-consistent solution for IS and HS states were about 2 and 3 $\mu_\text{B}$, respectively [5, 11]. This can help to identify the spin states in our calculations. For PBE+$U$ with $U$=3.0 eV, only the solution for IS state in FM order could be obtained, and when starting with the AFM initial configuration, magnetic moments of Co$^{3+}$ increased to 3 $\mu_\text{B}$ during iteration process, yielding HS solution. As shown in Table I, for $U$=3.0 eV, the most stable solution was IS state, followed by the LS-HS mixing states, and the LS solution became unfavorable. The difference between IS and LS state was calculated to be 0.12 eV/formula, implying that all spin states were close in energy. In this case, standard crystal field theory failed to give correct energy order of different spin states.

The above calculations were based on the experimental structure, and we further optimized the positions of Co, La, and O atoms with fixed cell parameters. For the LS state, CoO$_6$ still kept regular octahedral structure, and the distance of Co–O bond elongated to 1.940 Å. Due to the Jahn-Teller effect, the Co–O bonds were no longer equivalent for spin excited states. For instance, in IS state, the two axial Co–O distances were 1.940 Å, whereas the four equatorial Co–O distances were 1.934 Å. For AFM HS state, the Co–O distances divided into three groups, such as 1.914, 1.941, and 1.970 Å. And the LS-HS mixing states contained two kinds of CoO$_6$ octahedra with LS or HS structure, respectively.

From Table I, after the structural relaxation, only from −0.02 eV/formula to −0.05 eV/formula energy would be gained. Interestingly, the energies of IS and LS-HS (1:1) mixing states were nearly degenerated with optimized structures, indicating that these spin states might coexist at room temperature, in agreement with previous calculations [9, 11]. We also compared the DOS of different spin exited states with $U$=3.0 eV, as shown in Fig.3. Our calculations showed that the shape and position of peaks in DOS based on experimental structure and optimized one were nearly the same. Our calculations showed that IS state was of half-metallic, while LS-HS mixing states and HS belonged to narrow gap semi-conductor, consistent with previous calculations [5–9, 11, 13]. When $U$$\geq$5.0 eV, HS state turned out to be the most stable configuration, while the IS state was 0.1−0.2 eV/formula higher in energy. This finding indicated large $U$ value would lead to unreasonable relative energies of different spin states.

To the best of our knowledge, applying hybrid DFT to examine the spin exited states for LaCoO$_3$ has never been reported. Similarly to PBE+$U$, we started with different spin configurations; however, only the configurations with Co$^{3+}$ ions in IS states converged to a stable solution. And in the case, the magnetic moment of Co$^{3+}$ reduced to 1 $\mu_\text{B}$, indicating that hybridization between Co3d ($\text{e}_\text{g}$) and O2p became more pronounced. Table I also listed the electronic energies of LS and IS

![](./images/814713221599461377_3.jpg)

FIG. 3 Total DOS and projected DOS of IS, LS-HS, and HS states with experimental and optimized structures calculated by PBE+$U$ ($U$=3.0 eV).

![](./images/814713221599461377_4.jpg)

FIG. 4 Total DOS and projected DOS of IS state with different for HSE calculation.

states with different $\alpha$ value. When $\alpha$=0.05, the LS solution was 0.02 eV/formula more stable than the IS; while for $\alpha$=0.15, the IS state favored over the LS by 0.05 eV/formula.

Figure 4 illustrated the DOS of IS with different $\alpha$ values. Our calculation demonstrated that HSE with $\alpha$=0.05 predicted a "zero gap" semi-conductor; $\alpha$=0.15 led to a narrow gap semi-conductor (0.22 eV), and the band gap increased to 1.40 eV when $\alpha$=0.15. Experimentally, above room temperature, a very small band gap of 0.02$-$0.03 eV can be observed and more than 80% of the Co sites carried magnetic state density [31]. This indicated that a higher $\alpha$ value ($\sim$0.15) should be used to describe the spin excited states than that proposed for nonmagnetic state ($\alpha$=0.05) [19]. Compared with PBE+$U$, we found that when $U$=3.0 eV, the composition, the shape and the position of DOS were similar to that by HSE with $\alpha$=0.15 except that PBE+$U$ predicted a half-metallic character rather than semi-conductor for LaCoO$_3$. In short, $U$=3.0 eV for PBE+$U$ and $\alpha$=0.15 for HSE were suitable to describe the electronic structure and relative energies for LaCoO$_3$ at room temperature, which could be used to study the surface catalytic processes.

## IV. CONCLUSION

Here we presented a systematic DFT calculation on different spin states for LaCoO$_3$ at room temperature. (i) For the LS state, the band gap from PBE+$U$ with $U$=3.0 eV or HSE with $\alpha$=0.05$-$0.15 agreed well with experiment measurements. (ii) PBE+$U$ ($U$=3.0 eV) calculations predicted that both IS state and LS-HS (1:1) mixing states were energetically degenerated so that they can coexist at the room temperature. (iii) HSE calculations showed that the mixing factor was property dependent in which $\alpha$=0.15 can give reasonable energy order and band gap for spin excited states. (iv) We emphasized that a high $U$ value ($U$$\geq$5.0 eV) in PBE+$U$ would lead to unreasonable valence band composition and incorrect energy order.

## V. ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China (No.21033006, No.21133004, and No.21373167) and the Ministry of Science and Technology (No.2010CB732303).

DOI:10.1063/1674-0068/27/03/274-278

©2014 Chinese Physical Society

[1] T. Hirohisa and M. Makoto, Curr. Opin. Solid State Mater. Sci. **5**, 381 (2001).

[2] W. B. Li, J. X. Wang, and H. Gong, Catal. Today **148**, 81 (2009).

[3] M. Abbate, J. C. Fuggle, A. Fujimori, L. H. Tjeng, C. T. Chen, R. Potze, G. A. Sawatzky, H. Eisaki, and S. Uchida, Phys. Rev. B **47**, 16124 (1993).

[4] M. Abbate, R. Potze, G. A. Sawatzky, and A. Fujimori, Phys. Rev. B **49**, 7210 (1994).

[5] M. A. Korotin, S. Yu. Ezhov, I. V. Solovyev, V. I. Anisimov, D. I. Khomskii, and G. A. Sawatzky, Phys. Rev. B **54**, 5309 (1996).

[6] I. A. Nekrasov, S. V. Streltsov, M. A. Korotin, and V. I. Anisimov, Phys. Rev. B **68**, 235113 (2003).

[7] K. Knížek, P. Novák and Z. Jirák, Phys. Rev. B **71**, 054420 (2005).

[8] M. Sahnoun, C. Daul, O. Haas, and A. Wokaun, J. Phys.: Condens. Matter **17**, 7995 (2005).

[9] K. Knížek, Z. Jirák, J. Hejtmánek, and P Novák, J. Phys.: Condens. Matter **18**, 3285 (2006).

[10] S. K. Pandey, A. Kumar, S. Patil, V. R. R. Medicherla, R. S. Singh, and K. Maiti, Phys. Rev. B **77**, 045123 (2008).

[11] K. Knížek, Z. Jirák, J. Hejtmánek, P Novák, and W. Ku, Phys. Rev. B **79**, 014430 (2009).

[12] H. Hsu, K. Umemoto, M. Cococcioni, and R. Wentzcovitch, Phys. Rev. B **79**, 125124 (2009).

[13] Y. L. Lee, J. Kleis, J. Rossmeisl, and D. Morgan, Phys. Rev. B **80**, 224101 (2009).

[14] D. Gryaznov, R. A. Evarestov, and J. Maier, Phys. Rev. B **82**, 224301 (2010).

[15] A. Laref and S. J. J. Luo, Phys. Soc. Jpn. **79**, 064702 (2010).

[16] J. Ni and C. L. Ma, Mod. Phys. Lett. B **24**, 1785 (2010).

[17] C. L. Ma and J. Cang, Solid State Commun. **150**, 1983 (2010).

[18] A. Laref, S. Laref, and S. J. Bin-Omran, Comput. Chem. **33**, 673 (2012).

[19] J. He and C. Franchini, Phys. Rev. B **86**, 235117 (2012).

[20] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[21] G. Kresse and J. Hafner, Phys. Rev. B **48**, 13115 (1993).

[22] G. Kresse and J. Furthmuller, Phys. Rev. B **54**, 11169 (1996).

[23] V. I. Anisimov and J. Zaanen, Phys. Rev. B **44**, 943 (1991).

[24] S. L. Dudarev, Phys. Rev. B **57**, 1505 (1998).

[25] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. **118**, 8207 (2003).

[26] G. Thornton, B. C. Tofield, and A. W. J. Hewat, Solid State Chem. **61**, 301 (1986).

[27] A. Chainani, M. Mathew, and D. D. Sarma, Phys. Rev. B **46**, 9976 (1992).

[28] T. Arima, Y. Tokura, and J. B. Torrance, Phys. Rev. B **48**, 17006 (1993).

[29] M. A. L. Marques, J. Vidal, M. J. T. Oliveira, L. Reining, and S. Botti, Phys. Rev. B **83**, 035119 (2011).

[30] J. B. Varley, A. Janotti, C. Franchini, and C. G. Van de Walle, Phys. Rev. B **85**, R081109 (2012).

[31] Y. Tokura, Y. Okimoto, S. Yamaguchi, H. Taniguchi, T. Kimura, and H. Takagi, Phys. Rev. B **58**, R1699 (1998).

DOI:10.1063/1674-0068/27/03/274-278

©2014 Chinese Physical Society