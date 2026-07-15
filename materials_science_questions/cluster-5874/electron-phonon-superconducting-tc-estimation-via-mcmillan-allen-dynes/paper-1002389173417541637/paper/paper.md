Journal of Low Temperature Physics
https://doi.org/10.1007/s10909-024-03158-2

![](./images/1002389173417541637_1.jpg)

# Electron-Phonon Coupling in Copper-Substituted Lead Phosphate Apatite

Alexander C. Tyner¹,² · Sinéad M. Griffin³,⁴ · Alexander V. Balatsky¹,²

Received: 12 February 2024 / Accepted: 8 May 2024
© The Author(s) 2024

## Abstract
Recent reports of room-temperature, ambient pressure superconductivity in copper-substituted lead phosphate apatite, commonly referred to as LK99, have prompted numerous theoretical and experimental studies into its properties. As the electron–phonon interaction is a common mechanism for superconductivity, the electron–phonon coupling strength is an important quantity to compute for LK99. In this work, we compare the electron–phonon coupling strength among the proposed compositions of LK99. The results of our study are in alignment with the conclusion that LK99 is a candidate for low-temperature, not room-temperature, superconductivity if electron–phonon interaction is to serve as the mechanism.

Keywords Superconductivity · Electron–phonon coupling · First-principles

## 1 Introduction
A solid-state system admitting room temperature, ambient pressure superconductivity is commonly regarded as a “holy grail" of condensed matter physics due to the tremendous impact such a discovery would have on modern technology. In recent months, copper substituted lead apatite, commonly referred to as LK99, was proposed to support such a phenomena [1, 2], prompting a widespread theoretical and experimental effort to better understand its properties.

✉ Alexander C. Tyner
alexander.tyner@su.se

¹ Nordita, KTH Royal Institute of Technology and Stockholm University, 106 91 Stockholm, Sweden

² Department of Physics, University of Connecticut, Storrs, CT 06269, USA

³ Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA

⁴ Molecular Foundry Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA

Published online: 27 May 2024

![](./images/1002389173417541637_2.jpg)

A subsequent theoretical study computed the bulk band structure of LK99 con-
sidering two distinct locations for copper substitution, denoted Pb(1) and Pb(2), in
the lead-phosphate apatite [3], $\text{Pb}_{10}(\text{PO}_{4})_{6}\text{X}_{2}$, where $\text{X=O, OH}$. In each case, the
existence of nearly-flat bands at the Fermi energy was demonstrated. The presence
of such bands increases the density of states at the Fermi energy increasing the pos-
sibility of a mechanism for high-temperature superconductivity.

In the intervening months many questions about the nature of electronic states in
LK99 were raised. Additional studies have been published with remarkable speed
and detail [4–10], providing evidence that suggest LK99 is not a high-temperature
superconductor. It is important to note that despite being one of the most common
mechanisms for superconductivity, the electron–phonon coupling in LK99 has not
been examined in detail for each molecular configuration. We are aware of only one
work that has directly examined electron–phonon coupling strength [11]. This is
expected given the computational demands of such a quantity as well as the fact that
many available density functional theory packages do not offer the capability for
computation of electron–phonon coupling strength if a nonzero value of the Hub-
bard U is specified for a constituent atom in the compound [12]. Many works have
instead chosen to examine alternative indicators of superconductivity which are
computationally less expensive such as the Fubini-Studi metric [6].

In Ref. [11], the electron–phonon coupling strength was computed from first-
principles for $\text{Pb}_{9}\text{Cu(PO}_{4})_{6}\text{O}_{2}$ with Cu substituted at the Pb(2) site neglecting inclu-
sion of a Hubbard U. It was shown that the electron–phonon coupling is weak. Even
without inclusion of a Hubbard U for copper, this was a fascinating result as the
electron–phonon interaction is one of the most common routes to the realization of
superconductivity. It is thus a quantity of supreme importance and should be com-
pared among the possible compositions of copper substituted lead phosphate apatite.

In this work we follow a recently established protocol to compute a proxy for
the electron–phonon coupling strength, $\lambda$. This proxy involves computation of the
electron–phonon coupling at the $\Gamma$ point only, allowing us to overcome the compu-
tational challenges that have kept these quantities absent from the literature. In Ref.
[13], it is shown that,

$$
\lambda \approx f \lambda_{\Gamma} \tag{1}
$$

where it is reasonable to estimate $f$ as a constant for a family of materials. It was
further shown in Ref. [13], that the magnitude of $\lambda_{\Gamma}$ is generally sufficient for dis-
tinguishing systems likely to support superconductivity from those in which it is
highly unlikely. As a result, we have computed $\lambda_{\Gamma}$ for $\text{Pb}_{10}(\text{PO}_{4})_{6}\text{X}_{2} \text{X} = \text{O, OH}$,
with copper substitution at the Pb(1) site, allowing for a direct comparison between
the compositions.

Our work finds that the magnitude of $\lambda_{\Gamma}$ is small and generally equivalent among
the distinct compositions, making the prospect of high-temperature superconduc-
tivity by means of the electron–phonon interaction exceedingly unlikely for each
composition. Nevertheless, low-temperature superconductivity remains possible
(Table 1).

![](./images/1002389173417541637_3.jpg)

## 2 Results

In this work, all first principles calculations based on density-functional theory (DFT) are carried out using the Quantum Espresso software package [14–16]. Exchange-correlation potentials use the Perdew-Burke-Ernzerhof (PBE) parametrization of the generalized gradient approximation (GGA) [17]. In each case the atomic positions and lattice parameters are taken from Ref. [3]. The atomic positions and lattice parameters are subsequently relaxed until the maximum force on each atom is less than $1 \times 10^{-5}$Ry/Bohr. The electron–phonon coupling strength is determined using density function perturbation theory (DFPT) as implemented in the Quantum Espresso software package. Given that LK99 is proposed to support superconductivity at room temperature, spin-orbit coupling is neglected. A $8 \times 8 \times 6$ Monkhorst-Pack grid of k-points is utilized as well as a plane wave cutoff of 520 eV. We have neglected inclusion of a Hubbard U for copper in these computations, which can admittedly impact the computed values.

$\text{Pb}_{10}(\text{PO}_4)_6\text{X}_2$ belongs to space group $P6_3/m$ and $P6_3$ for X=O, OH, respectively. Details of the structure before and after copper substitution can be found in Ref. [3]. The locations for copper substitution on the two in-equivalent Pb sites, labeled Pb(1) and Pb(2) are shown in Fig. 1. The computed density of states for the relaxed structures for each of the compounds after copper substitution can be seen in Fig. 2 and the relaxed crystal structures are visible in Fig. 3.

![](./images/1002389173417541637_4.jpg)

Fig. 1 Crystal structure of $\text{Pb}_{10}(\text{PO}_4)_6\text{O}_2$ detailing two in-equivalent Pb sites

![](./images/1002389173417541637_5.jpg)

Fig. 2 Density of states for $\text{Pb}_9\text{Cu(PO}_4\text{)}_6\text{X}_2$ for a X=0 and b $\text{X = OH}$. In each case the density of states is computed in the presence and absence of spin-orbit coupling

![](./images/1002389173417541637_6.jpg)

![](./images/1002389173417541637_7.jpg)

Fig. 3 Relaxed crystal structure for $Pb_9Cu(PO_4)_6X_2$ with Cu substitution at Pb(1) for a X=OH and b X=O. The computed phonon modes at the $\Gamma$ location for X=OH, O are shown in c, d, respectively

![](./images/1002389173417541637_8.jpg)
![](./images/1002389173417541637_9.jpg)

of states computations in Fig. 2 demonstrate that the inclusion of spin-orbit cou- pling has had a minimal impact below the Fermi energy, indicating that neglect- ing spin-orbit coupling will not invalidate the results obtained. For further infor- mation regarding the crystal structure, bulk band structure, and more, we refer the reader to Refs. [3, 4, 6, 10].

The resulting phonon modes at the $\Gamma$ location are shown for $Pb_9Cu(PO_4)_6X_2$ with Cu at the Pb(1) site for X=OH, O in Fig. 3. We immediately note that the absence of negative frequency modes for X=O, indicating that this compound is dynamically stable. In contrast, for X=OH negative phonon modes can be found. While this can indicate a dynamic instability, it is likely that such negative frequency modes would be removed through imposition of a stricter convergence threshold when relaxing the structure. This presents a computational challenge due to the lightness of the hydrogen atoms whose positions can be easily adjusted with minimal effects on the energy of the structure, slowing convergence.

The computed electron-phonon coupling strength at the $\Gamma$ location at the Fermi energy as a function of the smearing values utilized in the computation is shown in Fig. 4. In order to estimate $\lambda$ for each compound, we utilize the value obtained in Ref. [11] for $Pb_9Cu(PO_4)_6O_2$ with Cu substituted at the Pb(2) site. We then determine $f$, where

$$
f = \lambda_\Gamma/\lambda \approx 3.5. \tag{2}
$$

![](./images/1002389173417541637_10.jpg)

<table>
<caption>Table 1 Estimates of $\lambda$ for Cu substituted at the Pb(1) site with X=OH and X=O, respectively, utilizing the finest value smearing value for computing density of states at the Fermi energy</caption>
<thead>
<tr>
<th>X</th>
<th>$\lambda_{\Gamma}$</th>
<th>$\lambda$</th>
</tr>
</thead>
<tbody>
<tr>
<td>O</td>
<td>0.120</td>
<td>0.43</td>
</tr>
<tr>
<td>OH</td>
<td>0.134</td>
<td>0.46</td>
</tr>
</tbody>
</table>

The value of $\lambda_{\Gamma}$ used in this computation is determined by computing the electron–phonon coupling at $\Gamma$ for the same compound in Ref. [11] at each smearing value seen in Fig. 4. Using these results, we determine $\lambda$ for Cu substituted at the Pb(1) site with X=OH and X=O, respectively, at the finest smearing value, placing the results in Table 1.

While not small enough to rule out low-temperature superconductivity, the computed values of electron–phonon coupling are weak in comparison with known conventional, high-temperature superconductors such as the high-pressure hydrates, where it is possible to obtain $\lambda \approx 6$. Hence we assume that electron–phonon coupling in all the compositions we considered is not large enough to account for possible high Tc superconducting state.

In Ref. [11], a superconducting critical temperature of $<2K$ was computed for $\text{Pb}_9\text{Cu}(\text{PO}_4)_6\text{O}_2$ with Cu substituted at the Pb(2) site. Given the current results, a similar value should be obtained for substitution at the Pb(1) site.

## 3 Conclusion

The approximated electron–phonon coupling is comparably small for copper substitution at the Pb(1) and Pb(2) sites, indicating that if LK99 is a candidate for high-temperature superconductivity, it is highly unlikely that electron–phonon coupling is the mechanism, but this is a possible mechanism for low-temperature superconductivity.

This conclusion is in agreement with the current literature which has been unable to achieve the proposed claim of room-temperature, ambient pressure superconductivity. Furthermore, there exists evidence that magnetic configurations not considered in this study may be stable and further limit the possibility of high-temperature superconductivity.

We hope that experimental data of electron–phonon coupling in LK99 materials will be available soon and provide context for the values predicted in this work.

**Acknowledgments** We are grateful to G. Aeppli for discussions. We acknowledge support from the European Research Council under the European Union Seventh Framework ERS-2018-SYG 810451 HERO and the University of Connecticut.

**Author Contributions** A.C.T. carried out the computations. S.M.G and A.B. conceived the project. A.C.T and A.B. wrote the manuscript. All authors reviewed the manuscript.

![](./images/1002389173417541637_11.jpg)

Journal of Low Temperature Physics

Funding Open access funding provided by Stockholm University.

Data Availability Data generated during the current study are available from the corresponding author on reasonable request.

## Declarations

Conflict of interest The authors declare no conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

## References

1.  S. Lee, J.-H. Kim, Y.-W. Kwon, arXiv:2307.12008 (2023a), https://doi.org/10.48550/arXiv.2307.12008
2.  S. Lee, J. Kim, H.-T. Kim, S. Im, S. An, K. H. Auh, arXiv:2307.12037 (2023b), https://doi.org/10.48550/arXiv.2307.12037
3.  S. M. Griffin, arXiv:2307.16892 ( 2023), https://doi.org/10.48550/arXiv.2307.16892
4.  J. Cabezas-Escares, N. Barrera, C. Cardenas, F. Munoz, arXiv:2308.01135 ( 2023), https://doi.org/10.48550/arXiv.2308.01135
5.  L. Hao, E. Fu, J. Mater. Sci. Technol. 173, 218 (2024). https://doi.org/10.1016/j.jmst.2023.08.010
6.  Y. Jiang, S. Lee, J. Herzog-Arbeitman, J. Yu, X. Feng, H. Hu, D. Calugar_q K经得起 study景观, chart� on Modialdynamics, P. Brodale, E. Gormley, M. G. Vergniory, et al., arXiv:2308.05143https://doi.org/10.48550/arXiv.2308.12055
7.  J. Lai, J. Li, P. Liu, Y. Sun, X.-Q. Chen, J. Mater. Sci. Technol. 171, 66 (2024). https://doi.org/10.1016/j.jmst.2023.08.001
8.  D. M. Korotin, D. Y. Novoselov, A. O. Shorikov, V. I. Anisimov, A. R. Oganov, arXiv:2308.04301 ( 2023), https://doi.org/10.48550/arXiv.2308.04301
9.  P. A. Lee, Z. Dai, arXiv:2308.04480 ( 2023), https://doi.org/10.48550/arXiv.2308.04480
10. J. Shen, D. Gaines II, S. Shahabfar, Z. Li, D. Kang, S. Griesemer, A. Salgado-Casanova, T.-c. Liu, C.-T. Chou, Y. Xia, et al., arXiv:2308.07941 ( 2023), https://doi.org/10.48550/arXiv.2308.07941
11. H. Paudyal, M. E. Flatté, D. Paudyal, arXiv:2308.14294 ( 2023), https://doi.org/10.48550/arXiv.2308.14294
12. F. Giustino, Rev. Mod. Phys. 89, 015003 (2017). https://doi.org/10.1103/RevModPhys.89.015003
13. Y. Sun, F. Zhang, C.-Z. Wang, K.-M. Ho, I.I. Mazin, V. Antropov, Phys. Rev. Mater. 6, 074801 (2022). https://doi.org/10.1103/PhysRevMaterials.6.074801
14. P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbra Mem innovationstable.经得起CRFrom quantum放心ola电源链接 coupledShow, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, R.M. Wentzcovitch, J. Phys. Condens. Matter. 21, 395502 (2009)
15. P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carnimeo, A. D. Corso, S. de Gironcoli, P. Delugas, R. A. D. Jr, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. O. de-la Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N. Vast, X. Wu, S. Baroni, J. Phys. Condens. Matter 29, 465901 ( 2017) http://stacks.iop.org/0953-8984/29/i=46/a=465901

![](./images/1002389173417541637_12.jpg)

16. P. Giannozzi, O. Baseggio, P. Bonfà, D. Brunato, R. Car, I. Carnimeo, C. Cavazzoni, S. de Gironcoli, P. Delugas, F. Ferrari. Ruffino, A. Ferretti, N. Marzari, J. Chem. Phys. **152**, 154105 (2020). https://doi.org/10.1063/5.0005082. (, **I. Timrov, A. Urru, S. Baroni**)

17. J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996). https://doi.org/10.1103/PhysRevLett.77.3865

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/1002389173417541637_13.jpg)