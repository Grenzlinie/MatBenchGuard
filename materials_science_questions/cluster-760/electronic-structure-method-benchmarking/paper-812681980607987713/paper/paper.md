![](./images/812681980607987713_1.jpg)

Extrapolating the coupled-cluster sequence toward the full configuration-interaction limit

David Z. Goodson

Citation: *J. Chem. Phys.* **116**, 6948 (2002); doi: 10.1063/1.1462620
View online: http://dx.doi.org/10.1063/1.1462620
View Table of Contents: http://jcp.aip.org/resource/1/JCPSA6/v116/i16
Published by the American Institute of Physics.

---

Additional information on *J. Chem. Phys.*
Journal Homepage: http://jcp.aip.org/
Journal Information: http://jcp.aip.org/about/about_the_journal
Top downloads: http://jcp.aip.org/features/most_downloaded
Information for Authors: http://jcp.aip.org/authors

ADVERTISEMENT

![](./images/812681980607987713_2.jpg)

# Extrapolating the coupled-cluster sequence toward the full configuration-interaction limit

David Z. Goodson⁽ᵃ⁾
Department of Chemistry, Southern Methodist University, Dallas, Texas 75275

(Received 26 November 2001; accepted 29 January 2002)

Extrapolation methods that accelerate the convergence of coupled-cluster energy sequences toward the full configuration–interaction (FCI) limit are developed and demonstrated for a variety of atoms and small molecules for which FCI energies are available, and the results are compared with those from Møller–Plesset (MP) perturbation theory. For the coupled-cluster sequence SCF, CCSD, CCSD(T), a method based on a continued-fraction formalism is found to be particularly successful. It yields sufficient improvement over conventional CCSD(T) that the results become competitive with, and often better than, results from the MP4-qλ method (MP4 summed with quadratic approximants and λ transformation). The sequence SCF, CCSD, CCSDT can be extrapolated with a quadratic approximant but the results are not appreciably more accurate than those from the CCSD(T) continued fraction. Singularity analysis of the MP perturbation series provides a criterion for estimating the accuracy the CCSD(T) continued fraction. © 2002 *American Institute of Physics.* [DOI: 10.1063/1.1462620]

## I. INTRODUCTION

The use of *ab initio* quantum chemistry methods for practical applications is hampered by the slow rate at which accuracy improves as computational cost increases. The Hartree–Fock self-consistent-field (SCF) method is cost efficient and can be used to calculate the electronic energy of large molecules, but its accuracy is often insufficient for quantitative prediction of chemical behavior. At the opposite extreme, the full configuration–interaction (FCI) method can in principle provide an arbitrarily high level of accuracy if used with a large enough basis set, but its unfavorable cost scaling of $N!$ with the number of basis functions $N$ limits its use at present to systems with no more than approximately 10 correlated electrons.

For moderately small molecules, methods with a cost scaling of $N^{7}$, such as MP4 (fourth-order Møller–Plesset perturbation theory)¹ or CCSD(T) (the coupled-cluster method with singles, doubles, and noniterative treatment of triples),² are thought to provide a relatively good balance between cost and accuracy.³ In the past few years a consensus seems to have been developing in favor of CCSD(T).⁴⁻⁶ However, it was recently shown⁷ that the accuracy of MP4 can be significantly increased, by repartitioning the Hamiltonian with the λ transformation⁸,⁹ and summing the resulting series with quadratic summation approximants. This method, designated MP4-qλ, works by explicitly modeling the known mathematical structure of the underlying perturbation theory. Its accuracy is typically somewhat higher than that of CCSD(T). The success of this approach for MP perturbation theory raises the question of whether it might be possible to develop some analogous procedure for improving the accuracy of CC calculations. In this paper simple extrapolation formulas are developed that accomplish this.

An advantage of MP theory is its straightforward mathematical interpretation as a Taylor series of a function, which made it possible to derive the MP4-qλ method from first principles.⁷,¹⁰ The mathematical interpretation of CC theories is more complicated. Therefore, no attempt is made here to justify the coupled-cluster extrapolation formulas theoretically. Instead they will be justified empirically, by comparison with FCI energy calculations. Although FCI calculations are very expensive, enough of them are now available in the literature that it is possible to assemble a realistic set of representative benchmark calculations so that such a comparison can be meaningfully made. The accuracy of the CCSD(T) extrapolation will be shown to be comparable to that of MP4-qλ; sometimes slightly worse, but for certain kinds of systems consistently somewhat better.

In addition, it will be demonstrated that singularity analysis of the MP perturbation series can be used to predict cases in which the extrapolated CCSD(T) will be better than MP4-qλ. Quadratic summation approximants can be used to estimate the location of the dominant branch-point singularity in the complex plane of the perturbation parameter.⁷,¹⁰⁻¹² The position of this singularity can be used as a criterion for deciding which calculation method to use.

In Sec. II various extrapolation formulas are developed. The first, which has the form of a continued fraction, will prove to be the most useful for CCSD(T). Also presented are formulas based on Padé approximants, both rational and quadratic. Section III compares the results of the extrapolation methods with FCI energies for a variety of systems and basis sets. In Sec. IV the results are discussed and an attempt is made to develop recommendations for when to use CCSD(T) as opposed to MP4-qλ or multireference methods. These recommendations are summarized in Sec. V.

⁽ᵃ⁾Current address: Department of Chemistry and Biochemistry, University of Massachusetts at Dartmouth, North Dartmouth, MA 02747. Electronic mail: dgoodson@umassd.edu

## II. EXTRAPOLATION FORMULAS

### A. Continued fraction

The continued fraction is a venerable extrapolation technique of number theory with modern applications to numerical and functional analysis. $^{13}$ It has the characteristic form

$$
a_{1} /\left(1+a_{2} /\left(1+a_{3} /(1+\cdots)\right)\right), \tag{1}
$$

with the sequence $a_{1}, a_{2}, a_{3}, \ldots$ chosen so that this expression converges to some quantity of interest.

A continued-fraction approximant for a coupled-cluster sequence can be constructed as follows. Express the coupled-cluster approximation for the electronic energy of an atom or molecule as

$$
E_{\mathrm{CC}}=\delta_{1}+\delta_{2}+\delta_{3}, \tag{2}
$$

where $\delta_{1}=E_{\mathrm{SCF}}$ is the Hartree-Fock self-consistent-field approximation and, for the CCSD(T) approximation,

$$
\delta_{2}=E_{\mathrm{CCSD}}-E_{\mathrm{SCF}}, \quad \delta_{3}=E_{\mathrm{CCSD}(\mathrm{T})}-E_{\mathrm{CCSD}}. \tag{3}
$$

Alternatively, one could use CCSDT, with full treatment of triple excitations, instead of CCSD(T) in these expressions. Since $E_{\mathrm{SCF}}$ typically accounts for well over $90 \%$ of the total energy, we know that $\delta_{1} \gg \delta_{2}+\delta_{3}$. Therefore,

$$
\delta_{1}+\delta_{2}+\delta_{3} \approx \delta_{1}\left(1-\left(\delta_{2}+\delta_{3}\right) / \delta_{1}\right)^{-1}. \tag{4}
$$

It is typically the case that the CCSD approximation accounts for most of the correlation energy. Let us assume, then, that $\delta_{2} \gg \delta_{3}$, which implies that

$$
\delta_{2}+\delta_{3} \approx \delta_{2}\left(1-\delta_{3} / \delta_{2}\right)^{-1}. \tag{5}
$$

Substituting Eq. (5) into Eq. (4) gives the continued-fraction approximant

$$
E_{\mathrm{CCcf}}=\frac{\delta_{1}}{1-\frac{\delta_{2} / \delta_{1}}{1-\delta_{3} / \delta_{2}}}. \tag{6}
$$

When the ratios $\delta_{2} / \delta_{1}$ and $\delta_{3} / \delta_{2}$ are small, the continued fraction can be expanded to give a series of additive corrections to $E_{\mathrm{CC}}$,

$$
E_{\mathrm{CCcf}} \approx E_{\mathrm{CC}}+\frac{\delta_{2}^{2}}{\delta_{1}}+\frac{\delta_{3}^{2}}{\delta_{2}}+2 \frac{\delta_{2} \delta_{3}}{\delta_{1}}+\cdots. \tag{7}
$$

### B. Rational Padé approximant

Suppose that one knows the Taylor series of a function $F(z)$ at the point $z=0$ and in addition has some information about the functional form of $F(z)$ in the complex $z$ plane. Then a reasonable approach to estimating the value of $F$ at some arbitrary nonzero $z$ is to construct an approximant that is an analytic function of $z$ with the expected functional form, containing parameters whose values are fixed by equating the Taylor series of the approximant with that of $F$. This approach was developed by Padé, $^{14}$ who proposed a variety of functional forms. The best known is the rational approximant, in the form $P(z) / Q(z)$ where $P$ and $Q$ are polynomials. These approximants are constructed to model functions with poles, but they can sometimes also do a good job of modeling functions with more complicated singularities. $^{15}$

The coupled-cluster sequence, Eq. (2), is not a Taylor series. Consider, however, a function

$$
E_{\mathrm{CC}}(z)=\delta_{1}+\delta_{2} z+\delta_{3} z^{2}, \tag{8}
$$

which smoothly interpolates between the SCF value at $z$ $=0$ and the CC approximation at $z=1$. If we equate Eq. (8) to the Taylor series of the rational approximant and evaluate it at $z=1$, we obtain the following formula:

$$
E_{\mathrm{CCr}}=\delta_{1} \frac{1+\delta_{2} / \delta_{1}-\delta_{3} / \delta_{2}}{1-\delta_{3} / \delta_{2}}. \tag{9}
$$

The expansion of Eq. (9) is

$$
E_{\mathrm{CCr}} \approx E_{\mathrm{CC}}+\frac{\delta_{3}^{2}}{\delta_{2}}+\frac{\delta_{3}^{3}}{\delta_{2}^{2}}+\cdots. \tag{10}
$$

### C. Quadratic Padé approximant

Also proposed by Padé $^{14}$ were approximants with algebraic singularities. It is only rather recently that they have attracted much attention, as their mathematical properties have been studied $^{12,16-19}$ and applications have been found for them in various areas of atomic and molecular physics. $^{7,10,11,20-25}$ Consider the quadratic approximant, with the form $P / 2-\left(P^{2} / 4-R\right)^{1 / 2}$ where $P$ and $R$ are polynomials in $z$ satisfying the asymptotic relation $E^{2}-P E+R \sim 0$. Setting $R(z)=r_{0}+r_{1} z$ and $P(z)=p_{0}$, and substituting Eq. (8) for $E$, leads to the approximant

$$
E_{\mathrm{CCq}}=\delta_{1}+\frac{1}{2} \frac{\delta_{2}^{2}}{\delta_{3}}\left[1-\left(1-\frac{4 \delta_{3}}{\delta_{2}}\right)^{1 / 2}\right], \tag{11}
$$

which has the expansion

$$
E_{\mathrm{CCq}} \approx E_{\mathrm{CC}}+2 \frac{\delta_{3}^{2}}{\delta_{2}}+5 \frac{\delta_{3}^{3}}{\delta_{2}^{2}}+\cdots. \tag{12}
$$

## III. RESULTS

A set of benchmark FCI calculations from the literature $^{6,26-32}$ is presented in Table I. These cover a wide range of atoms, molecules, and ions with first-row elements as well as a few systems with second-row elements. Most are frozen-core calculations, with only the valence electrons correlated. The earlier calculations use customized versions of the DZP (double-zeta plus polarization) basis sets $^{33}$ while the more recent ones mostly use the correlation-consistent polarized valence multiple-zeta sets, either cc-pVXZ $^{34}$ or aug-cc-pVXZ. $^{35}$ The "aug" sets are augmented with diffuse functions that improve the accuracy of electron affinity calculations.

These will be compared with MP and CC results. The MP results for $\mathrm{CH}_{2}, \mathrm{CH}_{3}$, and $\mathrm{NH}_{2}$ are from $\mathrm{He}$ and Cremer $^{36}$ while the CC results are from Watts et al. $^{37}$ For $\mathrm{BH}, \mathrm{N}_{2}, \mathrm{C}_{2}, \mathrm{CN}^{+}, \mathrm{Ar}, \mathrm{Cl}^{-}$, and $\mathrm{HCl}$, and for $\mathrm{HF}$ with the cc-pVDZ and aug-cc-pVDZ basis sets the MP and CC results are from Leininger et al. $^{6}$ For $\mathrm{Ne}$ and $\mathrm{F}^{-}$with aug-cc-pVDZ and $\mathrm{F}^{-}$with cc-pVTZ-$(f)$ the MP results are from Olsen

<table>
<caption>Table I. FCI energies, in $E_{\text{h}}$.
</caption>
<thead>
<tr>
<th>System
</th>
<th>Basis
</th>
<th>FCIa
</th>
<th>Reference
</th></tr></thead>
<tbody>
<tr>
<td>BH $X\,^{1}\Sigma^{+}$
</td>
<td>cc-pVDZ
</td>
<td>−25.215 324
</td>
<td>6
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>−25.218 432
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ
</td>
<td>−25.231 136
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVTZ
</td>
<td>−25.232 012
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>cc-pVQZ
</td>
<td>−25.235 568
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVQZ
</td>
<td>−25.235 843
</td>
<td>
</td></tr>
<tr>
<td>AlH $X\,^{1}\Sigma^{+}$
</td>
<td>cc-pVDZ
</td>
<td>−242.528 970
</td>
<td>26
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>−242.532 346
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ
</td>
<td>−242.546 102
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVTZ
</td>
<td>−242.547 064
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>cc-pVQZ
</td>
<td>−242.550 466
</td>
<td>
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVQZ
</td>
<td>−242.550 779
</td>
<td>
</td></tr>
<tr>
<td>CH₂ $\tilde{X}\,^{3}B_{1}$
</td>
<td>DZP
</td>
<td>−39.046 260
</td>
<td>27
</td></tr>
<tr>
<td>CH₂ $\tilde{a}\,^{1}A_{1}$
</td>
<td>DZP
</td>
<td>−39.027 183
</td>
<td>27
</td></tr>
<tr>
<td>CH₃ $\tilde{X}\,^{2}A_{2}''$
</td>
<td>DZP
</td>
<td>−39.721 212
</td>
<td>28
</td></tr>
<tr>
<td>NH₂ $\tilde{X}\,^{2}B_{1}$
</td>
<td>DZP
</td>
<td>−55.742 620
</td>
<td>29
</td></tr>
<tr>
<td>NH₂ $\tilde{A}\,^{2}A_{1}$
</td>
<td>DZP
</td>
<td>−55.688 762
</td>
<td>29
</td></tr>
<tr>
<td>H₂O⁺ $\tilde{X}\,^{2}B_{2}$
</td>
<td>cc-pVDZ
</td>
<td>−75.806 892b
</td>
<td>30
</td></tr>
<tr>
<td>H₂O⁺ $\tilde{A}\,^{2}A_{1}$
</td>
<td>cc-pVDZ
</td>
<td>−75.732 910b
</td>
<td>30
</td></tr>
<tr>
<td>H₂O⁺ $\tilde{B}\,^{2}B_{1}$
</td>
<td>cc-pVDZ
</td>
<td>−75.558 233b
</td>
<td>30
</td></tr>
<tr>
<td>H₂O $X\,^{1}A_{1}$
</td>
<td>cc-pVDZ
</td>
<td>−76.241 860
</td>
<td>30
</td></tr>
<tr>
<td>H₂S $X\,^{1}A_{1}$
</td>
<td>cc-pVDZ
</td>
<td>−398.865 583
</td>
<td>26
</td></tr>
<tr>
<td>F $X\,^{2}P$
</td>
<td>DZP
</td>
<td>−99.594 877
</td>
<td>31
</td></tr>
<tr>
<td>Ne $X\,^{1}S$
</td>
<td>cc-pVDZ
</td>
<td>−128.679 025
</td>
<td>32
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ-$(f)$
</td>
<td>−128.777 048
</td>
<td>32
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>−128.709 476
</td>
<td>32
</td></tr>
<tr>
<td>F⁻ $X\,^{1}S$
</td>
<td>cc-pVDZ
</td>
<td>−99.558 917
</td>
<td>32
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ-$(f)$
</td>
<td>−99.675 158
</td>
<td>32
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>−99.669 369
</td>
<td>32
</td></tr>
<tr>
<td>
</td>
<td>DZPc
</td>
<td>−99.706 690
</td>
<td>31
</td></tr>
<tr>
<td>HF $X\,^{1}\Sigma^{+}$
</td>
<td>cc-pVDZ
</td>
<td>−100.228 652
</td>
<td>6
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ-$(f/d)$
</td>
<td>−100.312 756
</td>
<td>32
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>−100.264 177
</td>
<td>6
</td></tr>
<tr>
<td>Ar $X\,^{1}S$
</td>
<td>aug-cc-pVDZ
</td>
<td>−526.970 128
</td>
<td>6
</td></tr>
<tr>
<td>Cl⁻ $X\,^{1}S$
</td>
<td>aug-cc-pVDZ
</td>
<td>−459.738 991
</td>
<td>6
</td></tr>
<tr>
<td>HCl $X\,^{1}\Sigma^{+}$
</td>
<td>aug-cc-pVDZ
</td>
<td>−460.272 768
</td>
<td>6
</td></tr>
<tr>
<td>N₂ $X\,^{1}\Sigma_{g}^{+}$
</td>
<td>cc-pVDZ
</td>
<td>−109.278 340
</td>
<td>6
</td></tr>
<tr>
<td>C₂ $X\,^{1}\Sigma_{g}^{+}$
</td>
<td>cc-pVDZ
</td>
<td>−75.729 853
</td>
<td>6
</td></tr>
<tr>
<td>CN⁺ $X\,^{1}\Sigma_{g}^{+}$
</td>
<td>cc-pVDZ
</td>
<td>−91.997 969
</td>
<td>6
</td></tr></tbody></table>

$^{\text{a}}$All values are from frozen-core calculations except those for H₂O and H₂O⁺.
$^{\text{b}}$At the equilibrium geometry of neutral H₂O.
$^{\text{c}}$[$5s4p3d$] aumented with diffuse functions.

*et al.*³² while the CC results are from Leininger.³⁸ CC results for AlH and H₂S are from Császár and Leininger.²⁶ For F and F⁻ with DZP basis, MP results are from He and Cremer³⁶ while CC results are from Scuseria³⁹ and Watts and Bartlett.⁴⁰ The results for H₂O and H₂O⁺ are from Olsen *et al.*³⁰ All other MP and CC values were calculated with GAUSSIAN 98.⁴¹

Table II shows the results of extrapolating CCSD with the continued-fraction approximant $\delta_{1}(1-\delta_{2}/\delta_{1})^{-1}$, which could just as well be thought of as a [0/1] rational Padé approximant. In every case this approximant improves the accuracy, although the amount of the improvement is in most cases only a rather small fraction of the total error. For the systems with first-row elements $E_{\text{CCSD}}-E_{\text{FCI}}$ is reduced by an average of 14% while for the systems with second-row elements it is reduced by just 2%.

<table>
<caption>Table II. $\Delta E=E_{\text{approx}}-E_{\text{FCI}}$, in $mE_{\text{h}}$, for SCF and CCSD calculations.
</caption>
<thead>
<tr>
<th>System
</th>
<th>Basis
</th>
<th>SCF
</th>
<th>CCSD
</th>
<th>CCSD-cf
</th></tr></thead>
<tbody>
<tr>
<td>BH $X\,^{1}\Sigma^{+}$
</td>
<td>cc-pVDZ
</td>
<td>90.137
</td>
<td>1.853
</td>
<td>1.542
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>92.163
</td>
<td>2.058
</td>
<td>1.734
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ
</td>
<td>101.231
</td>
<td>2.557
</td>
<td>2.168
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVTZ
</td>
<td>101.841
</td>
<td>2.631
</td>
<td>2.238
</td></tr>
<tr>
<td>
</td>
<td>cc-pVQZ
</td>
<td>104.282
</td>
<td>2.720
</td>
<td>2.308
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVQZ
</td>
<td>104.483
</td>
<td>2.740
</td>
<td>2.326
</td></tr>
<tr>
<td>AlH $X\,^{1}\Sigma^{+}$
</td>
<td>cc-pVDZ
</td>
<td>75.024
</td>
<td>1.380
</td>
<td>1.358
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>77.976
</td>
<td>1.560
</td>
<td>1.536
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ
</td>
<td>84.280
</td>
<td>1.862
</td>
<td>1.834
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVTZ
</td>
<td>85.156
</td>
<td>1.958
</td>
<td>1.929
</td></tr>
<tr>
<td>
</td>
<td>cc-pVQZ
</td>
<td>86.711
</td>
<td>2.006
</td>
<td>1.976
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVQZ
</td>
<td>86.979
</td>
<td>2.029
</td>
<td>1.999
</td></tr>
<tr>
<td>CH₂ $\tilde{X}\,^{3}B_{1}$
</td>
<td>DZP
</td>
<td>113.215
</td>
<td>2.090
</td>
<td>1.772
</td></tr>
<tr>
<td>CH₂ $\tilde{a}\,^{1}A_{1}$
</td>
<td>DZP
</td>
<td>140.886
</td>
<td>3.544
</td>
<td>3.057
</td></tr>
<tr>
<td>CH₃ $\tilde{X}\,^{2}A_{2}''$
</td>
<td>DZP
</td>
<td>150.583
</td>
<td>2.790
</td>
<td>2.236
</td></tr>
<tr>
<td>NH₂ $\tilde{X}\,^{2}B_{1}$
</td>
<td>DZP
</td>
<td>165.438
</td>
<td>3.273
</td>
<td>2.798
</td></tr>
<tr>
<td>NH₂ $\tilde{A}\,^{2}A_{1}$
</td>
<td>DZP
</td>
<td>162.380
</td>
<td>3.049
</td>
<td>2.590
</td></tr>
<tr>
<td>H₂O⁺ $\tilde{X}\,^{2}B_{2}$
</td>
<td>cc-pVDZ
</td>
<td>177.398
</td>
<td>2.637
</td>
<td>2.232
</td></tr>
<tr>
<td>H₂O⁺ $\tilde{A}\,^{2}A_{1}$
</td>
<td>cc-pVDZ
</td>
<td>175.510
</td>
<td>2.628
</td>
<td>2.232
</td></tr>
<tr>
<td>H₂O⁺ $\tilde{B}\,^{2}B_{1}$
</td>
<td>cc-pVDZ
</td>
<td>177.444
</td>
<td>3.019
</td>
<td>2.614
</td></tr>
<tr>
<td>H₂O $X\,^{1}A_{1}$
</td>
<td>cc-pVDZ
</td>
<td>217.821
</td>
<td>3.744
</td>
<td>3.139
</td></tr>
<tr>
<td>H₂S $X\,^{1}A_{1}$
</td>
<td>cc-pVDZ
</td>
<td>171.011
</td>
<td>4.001
</td>
<td>3.931
</td></tr>
<tr>
<td>F $X\,^{2}P$
</td>
<td>DZP
</td>
<td>194.894
</td>
<td>3.432
</td>
<td>3.062
</td></tr>
<tr>
<td>Ne $X\,^{1}S$
</td>
<td>cc-pVDZ
</td>
<td>190.249
</td>
<td>1.233
</td>
<td>0.954
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ-$(f)$
</td>
<td>245.186
</td>
<td>3.756
</td>
<td>3.302
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>213.126
</td>
<td>2.972
</td>
<td>2.628
</td></tr>
<tr>
<td>F⁻ $X\,^{1}S$
</td>
<td>cc-pVDZ
</td>
<td>192.933
</td>
<td>1.071
</td>
<td>0.699
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ-$(f)$
</td>
<td>250.859
</td>
<td>5.109
</td>
<td>4.500
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>241.086
</td>
<td>6.679
</td>
<td>6.125
</td></tr>
<tr>
<td>
</td>
<td>DZP
</td>
<td>262.994
</td>
<td>7.715
</td>
<td>7.058
</td></tr>
<tr>
<td>HF $X\,^{1}\Sigma^{+}$
</td>
<td>cc-pVDZ
</td>
<td>209.374
</td>
<td>2.423
</td>
<td>1.994
</td></tr>
<tr>
<td>
</td>
<td>cc-pVTZ-$(f/d)$
</td>
<td>255.923
</td>
<td>5.826
</td>
<td>5.199
</td></tr>
<tr>
<td>
</td>
<td>aug-cc-pVDZ
</td>
<td>231.083
</td>
<td>4.707
</td>
<td>4.194
</td></tr>
<tr>
<td>Ar $X\,^{1}S$
</td>
<td>aug-cc-pVDZ
</td>
<td>169.155
</td>
<td>2.968
</td>
<td>2.916
</td></tr>
<tr>
<td>Cl⁻ $X\,^{1}S$
</td>
<td>aug-cc-pVDZ
</td>
<td>175.346
</td>
<td>4.805
</td>
<td>4.742
</td></tr>
<tr>
<td>HCl $X\,^{1}\Sigma^{+}$
</td>
<td>aug-cc-pVDZ
</td>
<td>180.904
</td>
<td>4.718
</td>
<td>4.651
</td></tr>
<tr>
<td>N₂ $X\,^{1}\Sigma_{g}^{+}$
</td>
<td>cc-pVDZ
</td>
<td>328.783
</td>
<td>14.442
</td>
<td>13.532
</td></tr>
<tr>
<td>C₂ $X\,^{1}\Sigma_{g}^{+}$
</td>
<td>cc-pVDZ
</td>
<td>343.396
</td>
<td>29.957
</td>
<td>28.648
</td></tr>
<tr>
<td>CN⁺ $X\,^{1}\Sigma_{g}^{+}$
</td>
<td>cc-pVDZ
</td>
<td>380.477
</td>
<td>33.193
</td>
<td>31.872
</td></tr></tbody></table>

Tables III and IV show the extrapolation results for CCSD(T) and compare them to the results of MP4 and MP4-qλ. The results are grouped according to the “class” of the MP perturbation series. Class A systems have series that converge monotonically while class B systems have nonmonotonic series with, typically, the coefficients alternating in sign.⁸,³⁶,⁴²⁻⁴⁴ These different behaviors are, in principle, due to the location of the dominant singularity, $z_{d}$, in the complex plane of the perturbation parameter.¹⁰ For class A systems $z_{d}$ is in the positive half plane while for class B systems it is in the negative half plane. An alternative rationale for these classifications, developed by Cremer and He,⁴³ is based on the qualitative nature of the electronic orbitals. Class A systems have well-separated electron pairs while class B systems have electrons that cluster in some region of space. For most of the systems considered here, all three schemes lead to the same classifications. Exceptions, for which the large-order behavior is not manifest at fourth order, are here placed according to the Cremer–He criteria.

<table>
<caption>TABLE III. $\Delta E=E_{\text{approx}}-E_{\text{FCI}}$, in $mE_{\text{h}}$, using $N^{7}$ methods for class A systems.</caption>
<thead>
<tr>
<th>System</th>
<th>Basis</th>
<th>MP4 sum</th>
<th>MP4-q$\lambda^{\text{a}}$</th>
<th>CCSD(T)</th>
<th>CCSD(T)-cf</th>
<th>CCSD(T)-r</th>
<th>CCSD(T)-q</th>
</tr>
</thead>
<tbody>
<tr>
<td>BH $X\,^{1}\Sigma^{+}$</td>
<td>cc-pVDZ</td>
<td>5.227</td>
<td>0.217</td>
<td>0.483</td>
<td>0.140</td>
<td>0.461</td>
<td>0.439</td>
</tr>
<tr>
<td></td>
<td>aug-cc-pVDZ</td>
<td>5.242</td>
<td>0.061</td>
<td>0.529</td>
<td>0.167</td>
<td>0.503</td>
<td>0.475</td>
</tr>
<tr>
<td></td>
<td>cc-pVTZ</td>
<td>5.163</td>
<td>$-0.019$</td>
<td>0.521</td>
<td>0.073</td>
<td>0.478</td>
<td>0.432</td>
</tr>
<tr>
<td></td>
<td>aug-cc-pVTZ</td>
<td>5.171</td>
<td>0.016</td>
<td>0.532</td>
<td>0.076</td>
<td>0.487</td>
<td>0.438</td>
</tr>
<tr>
<td></td>
<td>cc-pVQZ</td>
<td>5.149</td>
<td>$-0.145$</td>
<td>0.504</td>
<td>0.024</td>
<td>0.455</td>
<td>0.402</td>
</tr>
<tr>
<td></td>
<td>aug-cc-pVQZ</td>
<td>5.162</td>
<td>$-0.155$</td>
<td>0.501</td>
<td>0.018</td>
<td>0.451</td>
<td>0.397</td>
</tr>
<tr>
<td>AlH $X\,^{1}\Sigma^{+}$</td>
<td>cc-pVDZ</td>
<td>3.010</td>
<td>$-0.350$</td>
<td>0.389</td>
<td>0.352</td>
<td>0.375</td>
<td>0.361</td>
</tr>
<tr>
<td></td>
<td>aug-cc-pVDZ</td>
<td>3.063</td>
<td>$-0.394$</td>
<td>0.433</td>
<td>0.391</td>
<td>0.416</td>
<td>0.398</td>
</tr>
<tr>
<td></td>
<td>cc-pVTZ</td>
<td>3.049</td>
<td>$-0.651$</td>
<td>0.437</td>
<td>0.383</td>
<td>0.412</td>
<td>0.385</td>
</tr>
<tr>
<td></td>
<td>aug-cc-pVTZ</td>
<td>3.103</td>
<td>$-0.569$</td>
<td>0.462</td>
<td>0.405</td>
<td>0.435</td>
<td>0.406</td>
</tr>
<tr>
<td></td>
<td>cc-pVQZ</td>
<td>3.143</td>
<td>$-0.828$</td>
<td>0.429</td>
<td>0.368</td>
<td>0.399</td>
<td>0.367</td>
</tr>
<tr>
<td></td>
<td>aug-cc-pVQZ</td>
<td>3.170</td>
<td>$-0.831$</td>
<td>0.426</td>
<td>0.364</td>
<td>0.395</td>
<td>0.362</td>
</tr>
<tr>
<td>CH$_2$ $\tilde{X}\,^{3}B_1$</td>
<td>DZP</td>
<td>1.880</td>
<td>0.270</td>
<td>0.360</td>
<td>0.004</td>
<td>0.333</td>
<td>0.304</td>
</tr>
<tr>
<td>CH$_2$ $\tilde{a}\,^{1}A_1$</td>
<td>DZP</td>
<td>4.979</td>
<td>1.926</td>
<td>0.873</td>
<td>0.314</td>
<td>0.820</td>
<td>0.764</td>
</tr>
<tr>
<td>CH$_3$ $\tilde{X}\,^{2}A_2''$</td>
<td>DZP</td>
<td>1.981</td>
<td>0.126</td>
<td>0.499</td>
<td>$-0.109$</td>
<td>0.463</td>
<td>0.425</td>
</tr>
<tr>
<td>NH$_2$ $\tilde{X}\,^{2}B_1$</td>
<td>DZP</td>
<td>1.900</td>
<td>$-0.055$</td>
<td>0.547</td>
<td>0.012</td>
<td>0.503</td>
<td>0.456</td>
</tr>
<tr>
<td>NH$_2$ $\tilde{A}\,^{2}A_1$</td>
<td>DZP</td>
<td>1.617</td>
<td>0.008</td>
<td>0.532</td>
<td>0.020</td>
<td>0.493</td>
<td>0.453</td>
</tr>
<tr>
<td>H$_2$O$^+$ $\tilde{X}\,^{2}B_2$</td>
<td>cc-pVDZ</td>
<td>1.493</td>
<td>0.066</td>
<td>0.454</td>
<td>0.011</td>
<td>0.426</td>
<td>0.398</td>
</tr>
<tr>
<td>H$_2$O$^+$ $\tilde{A}\,^{2}A_1$</td>
<td>cc-pVDZ</td>
<td>1.199</td>
<td>$-0.115$</td>
<td>0.462</td>
<td>0.028</td>
<td>0.435</td>
<td>0.406</td>
</tr>
<tr>
<td>H$_2$O$^+$ $\tilde{B}\,^{2}B_1$</td>
<td>cc-pVDZ</td>
<td>1.402</td>
<td>0.034</td>
<td>0.531</td>
<td>0.079</td>
<td>0.495</td>
<td>0.457</td>
</tr>
<tr>
<td>Mean $|\Delta E|^{\text{b}}$</td>
<td></td>
<td>2.473</td>
<td>0.331</td>
<td>0.520</td>
<td>0.104</td>
<td>0.485</td>
<td>0.447</td>
</tr>
<tr>
<td>Median $|\Delta E|^{\text{b}}$</td>
<td></td>
<td>1.890</td>
<td>0.109</td>
<td>0.506</td>
<td>0.051</td>
<td>0.466</td>
<td>0.430</td>
</tr>
</tbody>
</table>

$^{\text{a}}$This is the [1/0,1] approximant with $z_d$ in the positive half plane (Ref. 7).
$^{\text{b}}$BH and AlH are each given unit weight in the mean and median.

For the class A systems, in Table III, conventional MP4 performs poorly. The convergence is monotonic but slow. As shown previously, $^{7}$ the MP4-q$\lambda$ summation method dramatically improves the convergence for class A systems. For the systems in Table III the mean and median errors are reduced by factors of 7.5 and 17.5, respectively. The CCSD(T)-cf method reduces the mean and median errors of CCSD(T) in Table III by factors of 5.0 and 9.9, but since conventional MP4 is much less accurate than CCSD(T) for these systems, CCSD(T)-cf ends up being even more accurate than MP4-q$\lambda$, with results that are remarkably close to the FCI energies. The Padé methods for CCSD(T) give only a very small improvement over conventional CCSD(T).

For the class B systems, in Table IV, the trends are similar except that the magnitude of the improvement from the q$\lambda$ and cf techniques is smaller. The systems are listed in order of the value of $z_d$ in the MP4-q$\lambda$ approximant, which has been suggested as a predictor of the accuracy of the approximant. $^{7}$ The Møller–Plesset partitioning of the Hamiltonian is

<table>
<caption>TABLE IV. $\Delta E=E_{\text{approx}}-E_{\text{FCI}}$, in $mE_{\text{h}}$, using $N^{7}$ methods for class B systems, and the location $z_d$ of the dominant branch point of the MP4-q$\lambda$ approximant.</caption>
<thead>
<tr>
<th>System</th>
<th>Basis</th>
<th>MP4 sum</th>
<th>MP4-q$\lambda^{\text{a}}$</th>
<th>CCSD(T)</th>
<th>CCSD(T)-cf</th>
<th>CCSD(T)-r</th>
<th>CCSD(T)-q</th>
<th>$z_d$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ar $X\,^{1}S$</td>
<td>aug-cc-pVDZ</td>
<td>0.490</td>
<td>0.229</td>
<td>0.443</td>
<td>0.350</td>
<td>0.404</td>
<td>0.363</td>
<td>$-6.50$</td>
</tr>
<tr>
<td>F$^-$ $X\,^{1}S$</td>
<td>cc-pVDZ</td>
<td>0.590</td>
<td>0.597</td>
<td>0.464</td>
<td>0.088</td>
<td>0.462</td>
<td>0.460</td>
<td>$-3.66$</td>
</tr>
<tr>
<td>Ne $X\,^{1}S$</td>
<td>cc-pVDZ</td>
<td>$-0.025$</td>
<td>$-0.054$</td>
<td>0.188</td>
<td>$-0.099$</td>
<td>0.183</td>
<td>0.177</td>
<td>$-3.53$</td>
</tr>
<tr>
<td>Cl$^-$ $X\,^{1}S$</td>
<td>aug-cc-pVDZ</td>
<td>0.752</td>
<td>0.140</td>
<td>0.689</td>
<td>0.521</td>
<td>0.587</td>
<td>0.477</td>
<td>$-3.32$</td>
</tr>
<tr>
<td>HCl $X\,^{1}\Sigma^{+}$</td>
<td>aug-cc-pVDZ</td>
<td>1.131</td>
<td>0.174</td>
<td>0.695</td>
<td>0.530</td>
<td>0.601</td>
<td>0.500</td>
<td>$-3.19$</td>
</tr>
<tr>
<td>H$_2$S $X\,^{1}A_1$</td>
<td>cc-pVDZ</td>
<td>1.680</td>
<td>0.194</td>
<td>0.677</td>
<td>0.537</td>
<td>0.609</td>
<td>0.538</td>
<td>$-3.06$</td>
</tr>
<tr>
<td>HF $X\,^{1}\Sigma^{+}$</td>
<td>cc-pVDZ</td>
<td>0.496</td>
<td>0.479</td>
<td>0.496</td>
<td>0.041</td>
<td>0.478</td>
<td>0.459</td>
<td>$-2.67$</td>
</tr>
<tr>
<td>F $X\,^{2}P$</td>
<td>DZP</td>
<td>0.529</td>
<td>0.102</td>
<td>0.219</td>
<td>$-0.218$</td>
<td>0.164</td>
<td>0.106</td>
<td>$-2.49$</td>
</tr>
<tr>
<td>Ne $X\,^{1}S$</td>
<td>cc-pVTZ-($f$)</td>
<td>$-0.643$</td>
<td>$-0.328$</td>
<td>0.066</td>
<td>$-0.460$</td>
<td>0.009</td>
<td>$-0.051$</td>
<td>$-2.49$</td>
</tr>
<tr>
<td>Ne $X\,^{1}S$</td>
<td>aug-cc-pVDZ</td>
<td>$-0.981$</td>
<td>$-0.857$</td>
<td>0.181</td>
<td>$-0.210$</td>
<td>0.143</td>
<td>0.104</td>
<td>$-2.33$</td>
</tr>
<tr>
<td>H$_2$O $X\,^{1}A_1$</td>
<td>cc-pVDZ</td>
<td>1.060</td>
<td>0.784</td>
<td>0.658</td>
<td>$-0.009$</td>
<td>0.613</td>
<td>0.566</td>
<td>$-2.32$</td>
</tr>
<tr>
<td>F$^-$ $X\,^{1}S$</td>
<td>cc-pVTZ-($f$)</td>
<td>$-1.016$</td>
<td>$-0.086$</td>
<td>0.208</td>
<td>$-0.526$</td>
<td>0.108</td>
<td>0.002</td>
<td>$-2.04$</td>
</tr>
<tr>
<td>HF $X\,^{1}\Sigma^{+}$</td>
<td>cc-pVTZ-($f/d$)</td>
<td>$-0.851$</td>
<td>$-0.165$</td>
<td>0.229</td>
<td>$-0.554$</td>
<td>0.101</td>
<td>$-0.036$</td>
<td>$-1.95$</td>
</tr>
<tr>
<td>HF $X\,^{1}\Sigma^{+}$</td>
<td>aug-cc-pVDZ</td>
<td>$-0.882$</td>
<td>$-0.447$</td>
<td>0.536</td>
<td>$-0.075$</td>
<td>0.458</td>
<td>0.375</td>
<td>$-1.90$</td>
</tr>
<tr>
<td>F$^-$ $X\,^{1}S$</td>
<td>DZP</td>
<td>$-5.398$</td>
<td>$-1.482$</td>
<td>0.285</td>
<td>$-0.635$</td>
<td>0.062</td>
<td>$-0.182$</td>
<td>$-1.42$</td>
</tr>
<tr>
<td>F$^-$ $X\,^{1}S$</td>
<td>aug-cc-pVDZ</td>
<td>$-5.502$</td>
<td>$-2.165$</td>
<td>0.735</td>
<td>$-0.003$</td>
<td>0.580</td>
<td>0.413</td>
<td>$-1.36$</td>
</tr>
<tr>
<td>N$_2$ $X\,^{1}\Sigma_{g}^{+}$</td>
<td>cc-pVDZ</td>
<td>$-2.221$</td>
<td>1.643</td>
<td>1.862</td>
<td>0.350</td>
<td>1.338</td>
<td>0.742</td>
<td>$-1.28$</td>
</tr>
<tr>
<td>C$_2$ $X\,^{1}\Sigma_{g}^{+}$</td>
<td>cc-pVDZ</td>
<td>$-8.062$</td>
<td>20.203</td>
<td>2.042</td>
<td>$-2.265$</td>
<td>$-0.687$</td>
<td>$-4.416$</td>
<td>$-0.73$</td>
</tr>
<tr>
<td>CN$^+$ $X\,^{1}\Sigma_{g}^{+}$</td>
<td>cc-pVDZ</td>
<td>$-21.933$</td>
<td>26.687</td>
<td>$-0.231$</td>
<td>$-5.409$</td>
<td>$-3.790$</td>
<td>$-8.804$</td>
<td>$-0.68$</td>
</tr>
</tbody>
</table>

$^{\text{a}}$This is the [1/0,2] approximant with the constraint $R(0)=0$ and $z_d$ in the negative half plane (Ref. 7).

<table>
<caption>TABLE V. Mean and median $|\Delta E|$, in $mE_{\rm h}$, for class B systems for different ranges of $z_d$.</caption>
<thead>
<tr>
<th>Range of $z_d$</th>
<th></th>
<th>MP4 sum</th>
<th>MP4-q$\lambda$</th>
<th>CCSD(T)</th>
<th>CCSD(T)-cf</th>
<th>CCSD(T)-r</th>
<th>CCSD(T)-q</th>
</tr>
</thead>
<tbody>
<tr>
<td>$|z_d|$$&gt;$2.50</td>
<td>Mean</td>
<td>0.738</td>
<td>0.267</td>
<td>0.522</td>
<td>0.309</td>
<td>0.475</td>
<td>0.425</td>
</tr>
<tr>
<td></td>
<td>Median</td>
<td>0.590</td>
<td>0.194</td>
<td>0.496</td>
<td>0.350</td>
<td>0.478</td>
<td>0.460</td>
</tr>
<tr>
<td>$|z_d|$$\geqslant$1.90</td>
<td>Mean</td>
<td>0.795</td>
<td>0.331</td>
<td>0.411</td>
<td>0.301</td>
<td>0.351</td>
<td>0.301</td>
</tr>
<tr>
<td></td>
<td>Median</td>
<td>0.802</td>
<td>0.212</td>
<td>0.454</td>
<td>0.284</td>
<td>0.431</td>
<td>0.369</td>
</tr>
<tr>
<td>$|z_d|$$&gt;$1.00</td>
<td>Mean</td>
<td>1.426</td>
<td>0.584</td>
<td>0.508</td>
<td>0.306</td>
<td>0.406</td>
<td>0.327</td>
</tr>
<tr>
<td></td>
<td>Median</td>
<td>0.882</td>
<td>0.328</td>
<td>0.464</td>
<td>0.350</td>
<td>0.458</td>
<td>0.375</td>
</tr>
</tbody>
</table>

$$
H=H_{0}+z H_{1}, \quad(13)
$$

where $H_0$ is the sum of Fock operators and $z$ is a continuous parameter such that $z=0$ corresponds to the Hartree–Fock approximation and $z=1$ to the physical Hamiltonian. The perturbation theory yields a power series in $z$ that can be interpreted as the Taylor series of the energy function $E(z)$. At high orders of perturbation theory the convergence rate is governed by the absolute value of the dominant singularity $z_d$, which is the closest singularity to the point $z=0$. The q$\lambda$ method$^7$ uses a repartitioning of the Hamiltonian$^8$ to shift $z_d$ away from $z=0$. The resulting perturbation series is then summed with a quadratic Padé approximant. The repartitioning depends on a parameter $\lambda$, the value of which is chosen to maximize the distance between the $z=0$ and the nearest branch point singularity of the approximant. This is the $z_d$ value listed in the last column of Table IV.

The accuracy of MP4-q$\lambda$ shows a sharp drop as $|z_d|$ falls below about 1.5. The CCSD(T) methods also show a drop in accuracy, although less sharp, at the smallest $|z_d|$ values. Table V lists the mean and median errors from the different methods for class B systems, grouped according to the range of $z_d$. For $|z_d|$$&gt;$2.5, MP4-q$\lambda$ is the most dependable method. Over the range $|z_d|$$&gt;$1.90, MP4-q$\lambda$ and CCSD(T)-cf appear to be equally good.

For the class A systems BH and AlH, results are available for a variety of different basis sets. Since the accuracy of the coupled-cluster results for these systems does not seem to depend much on the basis, BH and AlH are each weighted as a single system in computing the mean and median. For class B there is a much stronger basis set dependence. For this reason, systems with different basis sets are considered as different systems in computing the means and medians in Table V.

For CCSDT, with full triples, the quadratic Padé approximant is the most dependable of the extrapolation methods. However, for class A systems even CCSDT-q is usually less accurate than the much less expensive CCSD(T)-cf. Table VI lists the class A mean and median errors. CCSDT-q is better than CCSD(T)-cf, among the class A systems, only for AlH and for the $\tilde{a}^1A_1$ state of $\text{CH}_2$. For class B, CCSDT-q is somewhat more accurate on average than the $N^7$ methods. Class B means and medians are shown in Table VII.

Finally, Table VIII shows an analysis of the coupled cluster and MP calculations of Olsen $et$ $al.^{30}$ for the water molecule with its geometry distorted along the symmetric stretch. The difficulties experienced by single-reference CC and MP as covalent bonds are stretched are well known.$^{30,37,45,46}$ MP is clearly more sensitive to these effects than is CC, and for those cases in which the effects are significant the quadratic summation approximant actually makes the MP4 results worse. Similarly, for the spin-restricted RCC calculations the extrapolated RCCSD(T) and RCCSDT methods give even worse results than do the conventional RCCSD(T) and RCCSDT as the molecule approaches dissociation. However, for the spin-unrestricted UCC calculations the extrapolation methods consistently improve the results even at $R=2R_e$, where spin contamination is severe. For the relatively small distortion $R=1.5R_e$ the extrapolation methods work well with the RCC calculations.

## IV. DISCUSSION

The results in Table III indicate that for systems with a class A perturbation series the CCSD(T)-cf continued-fraction extrapolation, from Eq. (6), gives substantially higher accuracy than MP4-q$\lambda$, with median error smaller by a factor of 2 and mean error by a factor of 3. The median error from CCSD(T)-cf for the 10 benchmark class A systems is a remarkably small $0.05\ mE_{\rm h}$. For class B systems, in Table IV, the accuracy from CCSD(T)-cf is about the same as that from MP4-q$\lambda$.

An advantage of perturbation theory, however, over coupled-cluster theory is the transparency of its theoretical foundation. The MP perturbation expansion is the asymptotic series of a function $E(z)$ in the complex plane of the perturbation parameter $z$. Therefore, it is straightforward to analyze the theory using methods of complex analysis. Katz$^{47}$ has proved that any eigenstate with the same symmetry as the ground state will somewhere in the complex $z$ plane become degenerate with the ground state. At each of these crossing points, which occur in complex-conjugate pairs, a square-root branch point is present in $E(z)$. Class A behavior is due to a complex-conjugate pair of branch points in the positive half plane, corresponding to an avoided crossing between the ground state and an excited state at a real value of $z$ beyond the physical value $z=1.^{48,49}$ Class B behavior can apparently be due to a branch point on the negative real axis that

<table>
<caption>TABLE VI. $\Delta E$ in $mE_{\rm h}$ for class A systems using CCSDT.</caption>
<thead>
<tr>
<th>
</th>
<th>CCSDT</th>
<th>CCSDT-cf</th>
<th>CCSDT-r</th>
<th>CCSDT-q</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mean$^a$</td>
<td>0.329</td>
<td>0.540</td>
<td>0.317</td>
<td>0.320</td>
</tr>
<tr>
<td>Median$^a$</td>
<td>0.223</td>
<td>0.327</td>
<td>0.181</td>
<td>0.134</td>
</tr>
<tr>
<td colspan="5">
$^a$BH and AlH have unit weight in the mean and median.
</td>
</tr>
</tbody>
</table>

<table>
 <thead>
  <tr>
   <th colspan="2">
    Range of $z_{d}$
   </th>
   <th>
    MP4-q$\lambda$
   </th>
   <th>
    CCSD(T)-cf
   </th>
   <th>
    CCSDT
   </th>
   <th>
    CCSDT-cf
   </th>
   <th>
    CCSDT-r
   </th>
   <th>
    CCSDT-q
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    $|z_{d}| &gt; 2.50$
   </td>
   <td>
    Mean
   </td>
   <td>
    0.243
   </td>
   <td>
    0.396
   </td>
   <td>
    0.327
   </td>
   <td>
    0.131
   </td>
   <td>
    0.251
   </td>
   <td>
    0.169
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
    Median
   </td>
   <td>
    0.194
   </td>
   <td>
    0.521
   </td>
   <td>
    0.340
   </td>
   <td>
    0.154
   </td>
   <td>
    0.228
   </td>
   <td>
    0.123
   </td>
  </tr>
  <tr>
   <td>
    $|z_{d} \geq 1.90$
   </td>
   <td>
    Mean
   </td>
   <td>
    0.349
   </td>
   <td>
    0.302
   </td>
   <td>
    0.277
   </td>
   <td>
    0.242
   </td>
   <td>
    0.218
   </td>
   <td>
    0.159
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
    Median
   </td>
   <td>
    0.212
   </td>
   <td>
    0.284
   </td>
   <td>
    0.301
   </td>
   <td>
    0.182
   </td>
   <td>
    0.218
   </td>
   <td>
    0.134
   </td>
  </tr>
  <tr>
   <td>
    $|z_{d}| &gt; 1.00$
   </td>
   <td>
    Mean
   </td>
   <td>
    0.676
   </td>
   <td>
    0.308
   </td>
   <td>
    0.406
   </td>
   <td>
    0.288
   </td>
   <td>
    0.289
   </td>
   <td>
    0.195
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
    Median
   </td>
   <td>
    0.447
   </td>
   <td>
    0.350
   </td>
   <td>
    0.335
   </td>
   <td>
    0.285
   </td>
   <td>
    0.224
   </td>
   <td>
    0.145
   </td>
  </tr>
 </tbody>
</table>

$^{a}$These results include those systems in Table IV for which CCSDT results are available [all but F⁻ and Ne with cc-pVDZ, Ne with cc-pVTZ-($f$), and HF with cc-pVTZ-($f/d$)].

represents a phase transition in which the electrons collectively dissociate from the nuclei. The existence of such a phenomenon was predicted by Baker⁵⁰ some years ago. It was recently analyzed by Stillinger⁵¹ in a study of a model problem and seems consistent with the results of analyses of large-order MP perturbation series for atomic wave functions.5,49 Both kinds of singularities can always be expected to be present, and the one closest to the origin is expected to determine the class of the perturbation series.

The MP4-q$\lambda$ method works by building the function $E(z)$ from its singularities and then shifting the position of the dominant singularity away from the origin in order to lessen its effect. An added benefit, in the case of class B systems, is that the singularity structure of the summation approximant can indicate cases in which the method will have trouble.⁷ If the dominant singularity $z_{d}$ of the summation approximant cannot be shifted beyond $- 1.5$ for a class B system, then the result for the energy should be viewed with suspicion. There are five such cases in in Table IV, and for each of them the result from CCSD(T)-cf is significantly better than that from MP4-q$\lambda$. Otherwise, MP4-q$\lambda$ seems to give a lower median error for class B.

This kind of singularity analysis is less useful for class A systems, in that there seems to be no correlation between the shifted position of the singularity structure in the positive half plane and the accuracy of the approximant. Perhaps this is because of the fact that the class A singularity structure really does consist of square-root branch points. The quadratic approximant presumably can model this branch point structure more accurately than it can model the more complicated class B phase transition branch point. This would make it less important to lessen the effect of the class A singularity structure by shifting it away.

The theoretical analysis of the coupled-cluster method is

<table>
 <thead>
  <tr>
   <th>
    Method
   </th>
   <th>
    $R_{e}$
   </th>
   <th>
    $1.5R_{e}$
   </th>
   <th>
    $2R_{e}$
   </th>
   <th>
    $2.5R_{e}$
   </th>
   <th>
    $3R_{e}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    RCCSD(T)
   </th>
   <td>
    0.658
   </td>
   <td>
    1.631
   </td>
   <td>
    $-$3.820
   </td>
   <td>
    $-$42.564
   </td>
   <td>
    $-$90.512
   </td>
  </tr>
  <tr>
   <th>
    RMP4-q$\lambda$¹
   </th>
   <td>
    0.784
   </td>
   <td>
    7.260
   </td>
   <td>
    30.211
   </td>
   <td>
    58.791
   </td>
   <td>
    73.200
   </td>
  </tr>
  <tr>
   <th>
    RCCSD(T)-cf
   </th>
   <td>
    $-$0.009
   </td>
   <td>
    0.394
   </td>
   <td>
    $-$7.753
   </td>
   <td>
    $-$56.348
   </td>
   <td>
    $-$119.280
   </td>
  </tr>
  <tr>
   <th>
    RCCSD(T)-r
   </th>
   <td>
    0.613
   </td>
   <td>
    1.350
   </td>
   <td>
    $-$5.934
   </td>
   <td>
    $-$52.607
   </td>
   <td>
    $-$113.075
   </td>
  </tr>
  <tr>
   <th>
    RCCSD(T)-q
   </th>
   <td>
    0.566
   </td>
   <td>
    1.038
   </td>
   <td>
    $-$8.671
   </td>
   <td>
    $-$69.856
   </td>
   <td>
    $-$164.348
   </td>
  </tr>
  <tr>
   <th>
    UCCSD(T)
   </th>
   <td>
    0.658
   </td>
   <td>
    5.243
   </td>
   <td>
    12.624
   </td>
   <td>
    4.497
   </td>
   <td>
    1.092
   </td>
  </tr>
  <tr>
   <th>
    UMP4-q$\lambda$¹
   </th>
   <td>
    0.784
   </td>
   <td>
    49.392
   </td>
   <td>
    27.457
   </td>
   <td>
    5.441
   </td>
   <td>
    1.170
   </td>
  </tr>
  <tr>
   <th>
    UCCSD(T)-cf
   </th>
   <td>
    $-$0.009
   </td>
   <td>
    4.224
   </td>
   <td>
    12.105
   </td>
   <td>
    4.288
   </td>
   <td>
    0.897
   </td>
  </tr>
  <tr>
   <th>
    UCCSD(T)-r
   </th>
   <td>
    0.613
   </td>
   <td>
    4.971
   </td>
   <td>
    12.385
   </td>
   <td>
    4.486
   </td>
   <td>
    1.087
   </td>
  </tr>
  <tr>
   <th>
    UCCSD(T)-q
   </th>
   <td>
    0.566
   </td>
   <td>
    4.667
   </td>
   <td>
    12.113
   </td>
   <td>
    4.474
   </td>
   <td>
    1.081
   </td>
  </tr>
  <tr>
   <th>
    RCCSDT
   </th>
   <td>
    0.493
   </td>
   <td>
    1.423
   </td>
   <td>
    $-$1.405
   </td>
   <td>
    $-$24.752
   </td>
   <td>
    $-$40.126
   </td>
  </tr>
  <tr>
   <th>
    RCCSDT-cf
   </th>
   <td>
    $-$0.180
   </td>
   <td>
    0.171
   </td>
   <td>
    $-$4.921
   </td>
   <td>
    $-$33.110
   </td>
   <td>
    $-$50.289
   </td>
  </tr>
  <tr>
   <th>
    RCCSDT-r
   </th>
   <td>
    0.443
   </td>
   <td>
    1.127
   </td>
   <td>
    $-$3.130
   </td>
   <td>
    $-$29.687
   </td>
   <td>
    $-$45.264
   </td>
  </tr>
  <tr>
   <th>
    RCCSDT-q
   </th>
   <td>
    0.390
   </td>
   <td>
    0.799
   </td>
   <td>
    $-$5.302
   </td>
   <td>
    $-$36.713
   </td>
   <td>
    $-$52.358
   </td>
  </tr>
  <tr>
   <th>
    UCCSDT
   </th>
   <td>
    0.493
   </td>
   <td>
    2.067
   </td>
   <td>
    5.512
   </td>
   <td>
    1.774
   </td>
   <td>
    0.539
   </td>
  </tr>
  <tr>
   <th>
    UCCSDT-cf
   </th>
   <td>
    $-$0.180
   </td>
   <td>
    0.750
   </td>
   <td>
    3.915
   </td>
   <td>
    1.438
   </td>
   <td>
    0.332
   </td>
  </tr>
  <tr>
   <th>
    UCCSDT-r
   </th>
   <td>
    0.443
   </td>
   <td>
    1.519
   </td>
   <td>
    4.227
   </td>
   <td>
    1.645
   </td>
   <td>
    0.523
   </td>
  </tr>
  <tr>
   <th>
    UCCSDT-q
   </th>
   <td>
    0.390
   </td>
   <td>
    0.879
   </td>
   <td>
    2.454
   </td>
   <td>
    1.502
   </td>
   <td>
    0.507
   </td>
  </tr>
  <tr>
   <th>
    $z_{d}$, RMP4-q$\lambda$
   </th>
   <td>
    $-$2.32
   </td>
   <td>
    $-$1.27
   </td>
   <td>
    $-$0.81
   </td>
   <td>
    $-$0.63
   </td>
   <td>
    $-$0.55
   </td>
  </tr>
  <tr>
   <th>
    $z_{d}$, UMP4-q$\lambda$
   </th>
   <td>
    $-$2.32
   </td>
   <td>
    $-$1.16
   </td>
   <td>
    $-$2.45
   </td>
   <td>
    $-$4.18
   </td>
   <td>
    $-$4.93
   </td>
  </tr>
 </tbody>
</table>

$^{a}$These results are from the [1/0,2] approximant with the constraint $R(0) = 0$ and $Z_{d}$ in the negative half plane (Ref. 7).

less straightforward. It can be thought of as an infinite sum- mation of certain classes of the terms that enter into the calculation of the MP series coefficients.⁴⁶ Thus, CC mixes terms proportional to different powers of the perturbation parameter z, which implies that an expression such as Eq. (8) will give a less accurate description of $E(z)$ in the limit of small z than will the asymptotic expansion, which is given by the MP series. It is probably best to consider the z depen- dence in Eq. (8) as little more than a convenient bookkeeping device that keeps track of the relative sizes of the correction terms in the construction of extrapolation formulas, rather than as an attempt to model the true z dependence of $E(z)$. Furthermore, the "parentheses" approximation² in CCSD(T) is not well-justified theoretically. Stanton⁵² has developed an after-the-fact theoretical argument that makes the approxima- tion seem reasonable, but the primary justification for the method remains its empirically demonstrated successes. In this light, the ad hoc nature of the CCSD(T)-cf extrapolation formula should not be discouraging. Its justification is its empirical success.

The CC extrapolation formulas always lower the energy. Since CC methods do not satisfy the variational principle, there is no guarantee that a CC energy will be higher than the FCI energy, and if it is not then the extrapolation methods will make the result less accurate. For class B there are only two such cases among the systems considered here, the $CN^{+}$ molecule for CCSD(T) and the F atom for CCSDT. For class A, the only such cases are $CH_{3}$ and $NH_{2}^{2}B_{1}$ with CCSDT. In all other cases the extrapolation moves in the correct di- rection, but occasionally it overcorrects, giving a negative error that is greater than the original positive error. For CCSD(T) with class B there are 6 out of the 19 cases in which CCSD(T)-cf is worse than CCSD(T) by more than 0.1 $mE_{h}$, while for CCSD(T)-q this is the case only for $C_{2}$ and $CN^{+}$, and for CCSD(T)-r only in the case of $CN^{+}$. Thus, for class B the Padé methods are safer, in that they are less likely to make the CCSD(T) result worse, but CCSD(T)-cf is better in terms of the mean and median. For the cf, r, and q ex- trapolations for CCSDT, the number of cases in which the extrapolation is worse by at least $0.1\ mE_{h}$ is 5,1, and 2, respectively, out of the 10 class A systems and 4, 0, and 1, respectively, out of 15 class B cases.

The systems $C_{2}$ and $CN^{+}$ are the two cases in Table IV for which the $\lambda$ transformation of the MP Hamiltonian can- not shift $z_{d}$ beyond $-1$, and all of the calculation methods give poor results, with the qλ and cf methods making the results significantly worse. [While CCSD(T) gives a very good energy for $CN^{+}$, this result is probably fortuitous-the bond distance and vibrational frequency are given inaccurately.⁶] An analysis¹⁰ of the large-order behavior of the MP series for $C_{2}$ using quadratic approximants indicates that the closest branch points to the origin for the untrans- formed $(\lambda=0)$ energy function $E(z)$ are at $-0.97\pm 0.34i$ and $1.18\pm 0.36i$. The MP4 quadratic approximant (for $\lambda$ $=0$) models this singularity structure with a branch point at $-0.46$. It seems the MP4 approximant senses the singulari- ties in both half planes, approximately equidistant from (and rather close to) the origin. The approximant refuses to make a choice and simply places a branch point somewhere be- tween the true branch points. If the branch points of the quadratic approximant are not providing a reliable model of the true singularity structure of $E(z)$, then the criterion for choosing the optimal $\lambda$ value for the qλ method will fail and the MP4-qλ result for the energy will be inaccurate.

For these two isoelectronic molecules the ground state is nearly degenerate with a low-lying doubly excited state.⁵³ Presumably, the branch points for $C_{2}$ at $1.18\pm 0.36i$ mark the points where the degeneracy becomes exact. However, one should not conclude from this that single-reference state CCSD(T) and MP4 are bound to fail in all cases of near degeneracy. The class A systems $BH, CH_{2}^{3}B_{1}$, and $CH_{2}^{1}A_{1}$ also have a nearly degenerate ground state but the qλ and cf methods work well, and the CCSD(T)-cf results are quite accurate.

Evidently, the source of the difficulty is the additional singularity structure in the negative half plane. With more typical class B systems, such as Ne with the aug-cc-pVDZ basis, the large-order quadratic approximants place the domi- nant singularity very close to, or exactly on, the negative real axis. It would seem that the Baker-Stillinger phase transitionis responsible for the class B singularity of Ne while for $C_{2}$  the dominant singularity structure in the negative half plane is caused by a Katz degeneracy. Large-order analyses of the $N_{2}$ and $CN^{+}$ series with quadratic approximants show singu larity structure qualitatively similar to that of $C_{2}$ but the structure in the negative half plane has a branch point on the real axis as well as a pair displaced from the axis. For $N_{2}$ the singularities are all somewhat farther from the origin than for $C_{2}$ and $CN^{+}$, and while CCSD(T) is somewhat inaccurate for $N_{2}$, CCSD(T)-cf does quite well. The implication is that a decision to use a more expensive multireference method instead of the single-reference method can be based on an analysis of the character of the MP singularity structure. The value of $z_{d}$ from the MP4-qλ approximant appears to offer a criterion. If $z_{d}$ is beyond $-1.2$ the CCSD(T)-cf method seems to be dependable.

It is not surprising that the singularity structure of MP perturbation theory should affect the accuracy of MP4 and MP4-qλ energies. It is less obvious why this singularity structure should affect the behavior of coupled-cluster calcu- lations. Evidently, systems with the kind of electronic struc- ture that yields "normal" singularity structure in $E(z)$, that is, a dominant class A branch point pair in the positive half plane with only very distant singularities in the negative half plane, have a characteristic pattern of convergence for the sequence SCF, CCSD, CCSD(T), FCI that happens to be modeled by the continued fraction. The kind of electronic structure that corresponds to less distant singularities in the negative half plane gives rise to a different convergence pat- tern. Figure 1 shows $E_{approx}-E_{FCI}$ as a function of $z_{d}$ for CCSD(T) and CCSD(T)-cf. In general, for class B systems with larger values of $|z_{d}|$ the CCSD(T)-cf and CCSDT-cf results lie above the FCI energy while for smaller values they lie below it. There is a clear downward trend in $E$ as $z_{d}$ approaches the origin for CCSD(T)-cf and CCSDT-cf but no such trend for CCSD(T) and CCSDT. A related phenomenon is the fact that there is a strong inverse correspondence for class B systems between the value of $|z_{d}|$ and the value of

$\delta_{2}^{2}/\delta_{1}$, the first correction term in the expansion of the continued fraction, Eq. (7).

The grouping of systems into class A and class B can sometimes be ambiguous. The groupings in the tables are based on the qualitative criteria developed by Cremer and He. $^{43}$ Alternatively, one could use the classification scheme based on the analysis by Schmidt *et al.*$^{8}$ as simplified by Cremer and He, $^{43}$ in which a system is placed in class A if its MP series converges monotonically and in class B otherwise. Since the convergence of the series is governed by the positions of the singularities of $E(z)$, it has also been proposed$^{10}$ that the classification be based on the location of the dominant singularity—class A if it is in the positive half plane, class B if it is in the negative half plane. The classification based on the convergence pattern and the classification based on singularity positions are equivalent in the limit of large order (except for a superimposed oscillation due to the imaginary parts of a class A complex-conjugate branch point pair$^{54}$) and, judging from the work of Cremer and He, $^{43}$ they are also consistent with the classification from the qualitative scheme. However, the large-order behavior sometimes is not yet apparent at fourth order, if it is temporarily masked by a more distant singularity with a larger prefactor or by nonsingular contributions.

For the most part, those class B systems with delayed onset of large-order behavior, such as $\ce{H_{2}O}$ and F, and HF and $\ce{F^{-}}$ in the cc-pVDZ basis, are handled quite well by the CCSD(T)-cf method. Including them in class A would not affect the conclusion that this method is the preferred approach for that class. The one exception is $\ce{H_{2}S}$, for which CCSD(T)-cf only reduces the error from 0.695 to $0.530\ \mathrm{m}E_{\mathrm{h}}$ while the error from MP4-q$\lambda$ is $0.194\ \mathrm{m}E_{\mathrm{h}}$. All the systems with a second-row element show only very modest improvement from the continued fraction. One might conclude from this that the continued fraction is best suited for systems with first-row elements while MP4-q$\lambda$ is better for systems with second-row elements, at least if they are in class B.

The focus here has been on molecules at their equilibrium geometries and on atoms. This is because a comparably comprehensive set of FCI benchmarks is not available for distorted geometries. However, it is calculations with stretched bonds that tend to be most in need of improvement. CCSD(T) calculations based on a single RHF reference determinant cannot properly describe covalent bond breaking, while use of a UHF reference can lead to serious spin contamination at bond lengths intermediate between equilibrium values and dissociation. $^{30,37,46}$ It is unreasonable to expect a simple extrapolation formula to completely solve these problems, but it might be the case that by improving the accuracy at small geometry distortions the continued fraction will enlarge the region of the potential energy hypersurface that can be accurately treated with single-reference calculations and stave off the need for a more expensive multireference method.

The results for the water molecule in Table VIII suggest this is in fact the case. The most striking result in that table is the success of RCCSD(T)-cf at $R=1.5R_{e}$. This suggests that RCCSD(T)-cf could be a good approach for calculations of transition states, which typically have bond distortions of this magnitude, and of vibrational energy levels. Conventional CCSD(T) gives good results for low-lying vibrational levels, $^{55}$ and continued-fraction extrapolation could make it feasible to treat more highly excited states. One should not conclude too much from a study of a single molecule, but these results are encouraging. A more systematic analysis of molecules with stretched bonds will be left for a future study.

![](./images/812681980607987713_3.jpg)

FIG. 1. $\Delta E=E_{\mathrm{approx}}-E_{\mathrm{FCI}}$ as a function of the position of the dominant singularity of the MP4 [1/0, 2] constrained q$\lambda$ approximant (Ref. 7), for CCSD(T)-cf (solid curve), and CCSD(T) (dashed curve), for class B systems.

In Table VIII $z_{d}$ continues to be a good indicator of the accuracy of the result, in the same way as for the class B systems in Table IV. The accuracy of RCCSD(T)-cf seems to drop precipitously when $|z_{d}|$ falls below 1.2. For the UHF-based methods $|z_{d}|$ reaches a minimum somewhere between $1.5R_{e}$ and $2R_{e}$, but as $|z_{d}|$ then increases, the accuracy of UCCSD(T)-cf decreases. This indicates that the poor accuracy at intermediate $R$ is due to spin contamination rather than to the convergence patterns at play for systems at equilibrium geometry.

### V. CONCLUSIONS

Comparison with benchmark FCI calculations for 22 different atoms and molecules with various basis sets indicates that it is usually better not to use CCSD(T) or MP4 results directly but to subject them to additional analysis. MP4 should be summed with the "q$\lambda$" method, $^{7}$ in which the series is subjected to a $\lambda$ transformation and then summed with a quadratic approximant. CCSD(T) should be extrapolated with the continued-fraction approximant, CCSD(T)-cf, developed here. Whether it is best to use MP4-q$\lambda$ or CCSD(T)-cf depends on the class of the MP series, as deter-

mined by the criteria of Cremer and He.⁴³ Class A systems, which are characterized by an uncrowded electron orbital structure, should be treated with CCSD(T)-cf, with significant improvement over conventional MP4 and CCSD(T) expected.

For class B systems the situation is more complicated, since MP4-qλ and CCSD(T)-cf seem to give results of about the same level of accuracy. Perhaps the major advantage of the qλ method is the fact that it is firmly based on functional analysis of the MP energy function, while the justification for the coupled-cluster extrapolations is only empirical. Also, MP4-qλ seems to give better results than CCSD(T)-cf for systems with the second-row elements S, Cl, and Ar. It is important to calculate the position of the dominant singularity \( z_d \) of the MP4-qλ approximant. For class B systems with \( |z_d| \) below approximately 1.5 it is safer to use CCSD(T)-cf. If \( |z_d|<1 \), then none of these methods is dependable. Such singularity structure indicates strong interaction between the ground-state reference determinant and two different excited states, and suggests that a multireference treatment would be more appropriate.

The CCSD(T)-cf method is less sensitive than MP4-qλ to bond stretching. Therefore, it may be able to give better results than MP4-qλ for molecular properties even when it gives a slightly worse result for the total energy at equilibrium geometry. The continued fraction seems to extend the range of bond distance for which single-reference CCSD(T) is useful. The position of \( z_d \) of the MP4-qλ approximant can indicate geometries for which a single-reference CCSD(T)-cf calculation will fail.

CCSDT can also be extrapolated reasonably dependably, but the amount of improvement is smaller than that from applying continued fractions to CCSD(T). The most appropriate extrapolation method for CCSDT seems to be the quadratic approximant, for both classes of systems, but the resulting accuracy is not appreciably better than that from MP4-qλ and CCSD(T)-cf. CCSD is consistently improved by continued-fraction extrapolation, although not as dramatically as CCSD(T).

## ACKNOWLEDGMENTS

The author thanks Professor Rodney Bartlett for a helpful discussion that prompted this study. This work was supported by a grant from the Welch Foundation.

¹C. Møller and M. S. Plesset, Phys. Rev. **46**, 618 (1934).
²K. Raghavachari, G. W. Trucks, J. A. Pople, and M. Head-Gordon, Chem. Phys. Lett. **157**, 479 (1989).
³J. Gauss, in *Encyclopedia of Computational Chemistry*, edited by P. v. R. Schleyer (Wiley, New York, 1998), pp. 615–636.
⁴T. H. Dunning, Jr. and K. A. Peterson, J. Chem. Phys. **108**, 4761 (1998).
⁵O. Christiansen, J. Olsen, P. Jørgensen, H. Koch, and P.-A. Malmqvist, Chem. Phys. Lett. **261**, 369 (1996).
⁶M. L. Leininger, W. D. Allen, H. F. Schaefer III, and C. D. Sherrill, J. Chem. Phys. **112**, 9213 (2000).
⁷D. Z. Goodson, J. Chem. Phys. **113**, 6461 (2000).
⁸Ch. Schmidt, M. Warken, and N. C. Handy, Chem. Phys. Lett. **211**, 272 (1993).
⁹E. Feenberg, Phys. Rev. **103**, 1116 (1956).
¹⁰D. Z. Goodson, J. Chem. Phys. **112**, 4901 (2000).
¹¹M. López-Cabrera, D. Z. Goodson, D. R. Herschbach, and J. D. Morgan III, Phys. Rev. Lett. **68**, 1992 (1992).
¹²A. V. Sergeev and D. Z. Goodson, J. Phys. **A 31**, 4301 (1998).
¹³P. Henrici, *Applied and Computational Complex Analysis* (Wiley, New York, 1977), Vol. 2, Chap. 12.
¹⁴H. Padé, Ann. de l'Ecole Normale Sup. 3iéme Série **9**, Suppl., 1 (1892).
¹⁵G. A. Baker, Jr., *The Essentials of Padé Approximants* (Academic, New York, 1975).
¹⁶R. E. Shafer, SIAM (Soc. Ind. Appl. Math.) J. Math. Anal. **11**, 447 (1975).
¹⁷G. A. Baker, Jr. and P. Graves-Morris, *Padé Approximants* (Cambridge University Press, Cambridge, 1996), pp. 524–569.
¹⁸A. V. Sergeyev, Zh. Vychisl. Mat. Mat. Fiz. **26**, 348 (1986) [USSR Comput. Math. Math. Phys. **26**, 17 (1986)].
¹⁹F. M. Fernández and C. G. Diaz, Eur. Phys. J. **D 15**, 41 (2001).
²⁰V. M. Vainberg, V. D. Mur, V. S. Popov, and A. V. Sergeev, Pis'ma Zh. Eksp. Teor. Fiz. **44**, 9 (1986); [JETP Lett. **44**, 9 (1986)].
²¹T. C. Germann and S. Kais, J. Chem. Phys. **99**, 7739 (1993).
²²A. V. Sergeev, J. Phys. **A 28**, 4157 (1995).
²³D. Z. Goodson and A. V. Sergeev, J. Chem. Phys. **110**, 8205 (1999).
²⁴F. M. Fernández and R. H. Tipping, J. Mol. Struct.: THEOCHEM **488**, 157 (1999).
²⁵C. G. Diaz and F. M. Fernández, J. Mol. Struct.: THEOCHEM **541**, 39 (2001).
²⁶A. G. Császár and M. L. Leininger, J. Chem. Phys. **114**, 5491 (2001).
²⁷C. W. Bauschlicher, Jr. and P. R. Taylor, J. Chem. Phys. **85**, 6510 (1986).
²⁸C. W. Bauschlicher, Jr. and P. R. Taylor, J. Chem. Phys. **86**, 5600 (1987).
²⁹C. W. Bauschlicher, Jr., S. R. Langhoff, P. R. Taylor, N. C. Handy, and P. J. Knowles, J. Chem. Phys. **85**, 1469 (1986).
³⁰J. Olsen, P. Jørgensen, H. Koch, A. Balkova, and R. J. Bartlett, J. Chem. Phys. **104**, 8007 (1996).
³¹C. W. Bauschlicher, Jr. and P. R. Taylor, J. Chem. Phys. **85**, 2779 (1986).
³²J. Olsen, O. Christiansen, H. Koch, and P. Jørgensen, J. Chem. Phys. **105**, 5082 (1996).
³³S. Huzinaga, J. Chem. Phys. **42**, 1293 (1965); T. H. Dunning, *ibid*. **53**, 2823 (1970); **55**, 3958 (1971).
³⁴T. H. Dunning, Jr., J. Chem. Phys. **90**, 1007 (1989).
³⁵R. A. Kendall, T. H. Dunning, Jr., and R. J. Harrison, J. Chem. Phys. **96**, 6796 (1992).
³⁶Z. He and D. Cremer, Int. J. Quantum Chem. **59**, 71 (1996).
³⁷J. D. Watts, J. Gauss, and R. J. Bartlett, J. Chem. Phys. **98**, 8718 (1993).
³⁸M. L. Leininger (private communication).
³⁹G. E. Scuseria, J. Chem. Phys. **95**, 7426 (1991).
⁴⁰J. D. Watts and R. J. Bartlett, J. Chem. Phys. **93**, 6104 (1990).
⁴¹M. J. Frisch, G. W. Trucks, H. B. Schlegel, *et al.*, GAUSSIAN 98, Revision A.9, Gaussian, Inc., Pittsburgh, PA, 1998.
⁴²Z. He and D. Cremer, Int. J. Quantum Chem. **59**, 57 (1996).
⁴³D. Cremer and Z. He, J. Phys. Chem. **100**, 6173 (1996).
⁴⁴Y. He and D. Cremer, Mol. Phys. **98**, 1415 (2000).
⁴⁵N. C. Handy, P. J. Knowles, and K. Somasundram, Theor. Chim. Acta **68**, 87 (1985).
⁴⁶R. J. Bartlett, J. Phys. Chem. **93**, 1697 (1989), and references therein.
⁴⁷A. Katz, Nucl. Phys. **29**, 353 (1962).
⁴⁸K. Dietz, Ch. Schmidt, M. Warken, and B. A. Heß, J. Phys. **B 26**, 1885 (1993).
⁴⁹J. Olsen, P. Jørgensen, T. Helgaker, and O. Christiansen, J. Chem. Phys. **112**, 9736 (2000).
⁵⁰G. A. Baker, Jr., Rev. Mod. Phys. **43**, 479 (1971).
⁵¹F. H. Stillinger, J. Chem. Phys. **112**, 9711 (2000).
⁵²J. F. Stanton, Chem. Phys. Lett. **281**, 130 (1997).
⁵³M. L. Leininger, C. D. Sherrill, W. D. Allen, and H. F. Schaefer III, J. Chem. Phys. **108**, 6717 (1998).
⁵⁴D. Z. Goodson, M. López-Cabrera, D. R. Herschbach, and J. D. Morgan III, J. Chem. Phys. **97**, 8481 (1992).
⁵⁵J. M. L. Martin, Chem. Phys. Lett. **292**, 411 (1998).
