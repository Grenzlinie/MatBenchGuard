# Coupled cluster benchmarks of large noncovalent complexes: The L7 dataset as well as DNA-ellipticine and buckycatcher-fullerene

Cite as: J. Chem. Phys. 154, 154104 (2021); https://doi.org/10.1063/5.0042906
Submitted: 05 January 2021 . Accepted: 28 March 2021 . Published Online: 19 April 2021

Francisco Ballesteros, Shelbie Dunivan, and Ka Un Lao

![](./images/812472623077261314_1.jpg) ![](./images/812472623077261314_2.jpg) ![](./images/812472623077261314_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

r²SCAN-3c: A "Swiss army knife" composite electronic-structure method
The Journal of Chemical Physics 154, 064103 (2021); https://doi.org/10.1063/5.0040021

Electronic structure software
The Journal of Chemical Physics 153, 070401 (2020); https://doi.org/10.1063/5.0023185

Dataset of noncovalent intermolecular interaction energy curves for 24 small high-spin open-shell dimers
The Journal of Chemical Physics 154, 134106 (2021); https://doi.org/10.1063/5.0043793

![](./images/812472623077261314_4.jpg)

J. Chem. Phys. 154, 154104 (2021); https://doi.org/10.1063/5.0042906
154, 154104

© 2021 Author(s).

# Coupled cluster benchmarks of large noncovalent complexes: The L7 dataset as well as DNA-ellipticine and buckycatcher-fullerene

Cite as: J. Chem. Phys. 154, 154104 (2021); doi: 10.1063/5.0042906
Submitted: 5 January 2021 • Accepted: 28 March 2021 •
Published Online: 19 April 2021

![](./images/812472623077261314_5.jpg)
![](./images/812472623077261314_6.jpg)
![](./images/812472623077261314_7.jpg)

Francisco Ballesteros, Shelbie Dunivan, and Ka Un Laoᵃ

## AFFILIATIONS
Department of Chemistry, Virginia Commonwealth University, Richmond, Virginia 23284, USA

ᵃAuthor to whom correspondence should be addressed: laoku@vcu.edu

## ABSTRACT
In this work, benchmark binding energies for dispersion-bound complexes in the L7 dataset, the DNA-ellipticine intercalation complex, and the buckycatcher-$C_{60}$ complex with 120 heavy atoms using a focal-point method based on the canonical form of second-order Møller–Plesset theory (MP2) and the domain based local pair natural orbital scheme for the coupled cluster with single, double, and perturbative triple excitations [CCSD(T)] extrapolated to the complete basis set (CBS) limit are reported. This work allows for increased confidence given the agreement with respect to values recently obtained using the local natural orbital CCSD(T) for L7 and the canonical CCSD(T)/CBS result for the coronene dimer (C2C2PD). Therefore, these results can be considered pushing the CCSD(T)/CBS binding benchmark to the hundred-atom scale. The disagreements between the two state-of-the-art methods, CCSD(T) and fixed-node diffusion Monte Carlo, are substantial with at least 2.0 (~10%), 1.9 (~5%), and 10.3 kcal/mol (~25%) differences for C2C2PD in L7, DNA-ellipticine, and buckycatcher-$C_{60}$, respectively. Such sizable discrepancy above “chemical accuracy” for large noncovalent complexes indicates how challenging it is to obtain benchmark binding interactions for systems beyond small molecules, although the three up-to-date density functionals, PBE0+D4, $\omega$B97M-V, and B97M-V, agree better with CCSD(T) for these large systems. In addition to reporting these values, different basis sets and various CBS extrapolation parameters for Hartree–Fock and MP2 correlation energies were tested for the first time in large noncovalent complexes with the goal of providing some indications toward optimal cost effective routes to approach the CBS limit without substantial loss in quality.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0042906

## I. INTRODUCTION
The gold standard coupled cluster with single, double, and perturbative triple excitations [CCSD(T)] approach¹ has been widely used for providing reliable reference noncovalent interactions of small molecules to develop density functionals, semi-empirical methods, force fields, and machine learning potentials.²³ However, its steep increase in computational cost with $\mathcal{O}(N^{7})$ scaling with respect to system size $N$ and requirement of huge memory and storage space have hindered its applicability for systems beyond small molecules.⁴ Local correlation schemes such as the direct and the fragment based approaches are two effective strategies that have been employed to reduce the computational cost of the canonical CCSD(T) approach, thereby extending viability to large complexes. These approaches include the domain based local pair natural orbital (DLPNO) scheme by Neese,⁵⁶ the pair natural orbital (PNO) based scheme by Schmitz and Hättig⁷ and by Ma and Werner,⁸ the cluster-in-molecule (CIM) approach by Li et al.⁹ and Guo et al.,¹⁰ and the local natural orbital (LNO) scheme by Kállay.¹¹¹² The accuracy of these local correlation methods can be controlled by tightening the thresholds of the local approximations.¹²¹³ However, the errors due to the local truncations for large systems are unquantifiable due to lack of canonical CCSD(T) binding energies at the complete basis set (CBS) limit.

Even after local correlation schemes have been employed, CCSD(T) is still computationally demanding and may become intractable for larger systems using a reasonable size basis set. For example, using a triple-$\zeta$ basis set for DLPNO-CCSD(T) with TightPNO threshold was infeasible$^{14}$ for the two largest complexes involving circumcoronene in the L7 dataset, which includes seven large dispersion-bound dimers.$^{15}$ In contrast to the direct extrapolation, a focal-point method or a composite approach$^{16–19}$ has often been used to calculate the CCSD(T) binding interaction at the CBS limit by adding a CCSD(T) correction term, $\Delta$CCSD(T), in a less expensive basis set to the second-order Møller–Plesset theory (MP2) binding interaction at the CBS limit. The role of the canonical MP2/CBS in this focal-point method is to reduce the basis-set incompleteness error by employing a basis-set extrapolation scheme$^{20}$ and capture the canonical electron correlation up to the MP2 level. The canonical CCSD(T) part in $\Delta$CCSD(T) can be replaced by the local CCSD(T) counterpart, such as DLPNO-CCSD(T),$^{21}$ to reduce the computational cost dramatically. Hence, local CCSD(T) approaches still play important roles in an attempt to provide benchmark quality of binding interactions for large noncovalent complexes.$^{6,14,21–23}$

It is customary for quantum chemical methods to be evaluated against sets of reference molecules for which reference data have been assembled. In order to test the assumption that the accuracy of methods for small systems is preserved for systems with large numbers of atoms, the L7 dataset including seven large noncovalent complexes with the number of atoms up to 112 (CBH, the octadecane dimer) or the number of heavy atoms up to 73 (C3GC, a guanine–cytosine base pair stacked on circumcoronene) has been developed.$^{15}$ Subsequently, several attempts were made to provide the benchmark interaction energies for this L7 dataset. The compact notation of (a)(X,Y)Z is employed in the following discussion to denote the CBS limit extrapolation using the (aug)-cc-pVXZ and (aug)-cc-pVYZ basis sets. In 2013, Sedlak *et al.*$^{15}$ estimated the L7 benchmark binding energies for the first time as the sum of the MP2/(D,T)Z binding energies scaled by 1.03, $\Delta$QCISD(T)/6-31G*(0.25) for five complexes, $\Delta$CCSD(T)/6-31G**(0.25,0.15) for GCGC, and $\Delta$QCISD(T) with the mixed cc-pVDZ/aug-cc-pVDZ basis set for C2C2PD. In 2015, Calbo *et al.*$^{21}$ reported their binding energies as the sum of the MP2/(D,T)Z binding energies and the differences between the DLPNO-CCSD(T₀)/def2-TZVPP with NormalPNO threshold and MP2/def2-TZVPP binding energies. Pavošević *et al.* in 2017$^{6}$ and Carter-Fenk *et al.* in 2019$^{14}$ calculated five complexes (excluding C3A and C3GC involving circumcoronene) in the L7 dataset using DLPNO-CCSD(T₀)-F12/cc-pVDZ with VeryTightPNO threshold and DLPNO-CCSD(T₀)/(D,T)Z with TightPNO threshold, respectively. Going back to 2018, Brandenburg *et al.*$^{24}$ estimated DLPNO-CCSD(T₀)/CBS binding energies for all seven complexes in L7 by employing the CBS* protocol,$^{25}$ which is composed of HF/(D,T)Z and $1.08 \times$ MP2/(D,T)Z correlation energies scaled by the quotient of DLPNO-CCSD(T₀) (only tightened $T_{\text{CutPairs}}$ to $10^{-5}$ on top of the default setting) and MP2 correlation energies using the def2-TZVP basis set. Recently, in 2020, Al-Hamdani *et al.*$^{23}$ obtained the binding interactions for complexes in L7 using the half counterpoise corrected LNO-CCSD(T)/a(Q,5)Z with the Tight–Very Tight LNO threshold extrapolation except C3A and C3GC, where their binding interactions were the sum of LNO-CCSD(T)/aug-cc-pVTZ with the Tight–Very Tight LNO threshold extrapolation and a Normal LNO-CCSD(T)/a(Q,5)Z-based basis-set incompleteness correction.

Alternatively, quantum Monte Carlo (QMC)$^{26–28}$ based on stochastic techniques is another state-of-the-art approach that yields accurate interaction energies for small organic dimers where CCSD(T) and the most commonly used diffusion Monte Carlo method with the fixed-node approximation (FN-DMC) approximation agree with each other within the error bars.$^{28–31}$ This good agreement between two fundamentally distinct methods engenders the confidence for given benchmark values in small molecules. However, it has been recently shown that the agreement of interaction energies between CCSD(T) and FN-DMC does not extend to large noncovalent complexes.$^{23,32}$ For example, the binding disagreements are at least 8 kcal/mol$^{23}$ between LNO-CCSD(T)/CBS and FN-DMC for a C₆₀ buckyball inside a [6]-cycloparaphenyleneacetylene ring (C₆₀@[6]CPPA consisting of 132 atoms or 108 heavy atoms) and up to 7 kcal/mol between DLPNO-CCSD(T₀)/CBS and FN-DMC for the coronene dimer.$^{32}$ Hence, the conclusions drawn from low-cost computational approaches applied to large noncovalent complexes may need to be adjusted based on the reference benchmark used as a comparison.$^{23}$ One should note that the aforementioned two state-of-the-art methods have been developed and improved upon greatly in relatively short order, and yet, their predictive powers in the regime of larger molecules are unknown.$^{23}$

In this way, pushing the benchmark quality of noncovalent interactions to large complexes would provide valuable information about the reliability of relatively low-cost computational approaches, such as density functional theory (DFT), semi-empirical approaches, force fields, and machine learning based models, for the modeling of “real-life” biomolecular complexes, host–guest complexes, and supermolecular assemblies governed by noncovalent interactions. Furthermore, it should be noted that the current benchmarks for large noncovalent complexes can come at a relatively steep and nontrivial cost via massive parallel computing.$^{23,32}$ For example, it took ~0.7 and 1 million central processing unit (CPU) core hours for FN-DMC and LNO-CCSD(T), respectively, in calculations of L7 and C₆₀@[6]CPPA, which is equivalent to spending ~7 years of constant calculations running on a modern 28 core machine.$^{23}$ Hence, this limits the establishment of benchmark noncovalent interactions for large complexes to groups with such high computing power.

In this work, we provide viable CCSD(T)/CBS benchmark interaction energies for seven dispersion-dominated complexes in the popular L7 dataset$^{15}$ by using the focal-point method based on the canonical MP2 using large basis sets augmented with diffuse basis functions, which are necessary to obtain benchmarks at the converged CBS limit, and DLPNO-CCSD(T₀) with TightPNO threshold in $\Delta$CCSD(T), where T₀ is referred to use the “semicanonical” approximation in the triples correction.$^{33}$ This recipe is a cost conscious solution to achieve CCSD(T)/CBS accuracy at a relatively lower cost when computing power is limited to a typical research lab caliber. In addition, two larger systems, the DNA–ellipticine intercalation complex,$^{34}$ consisting of 157 atoms or 95 heavy atoms, and the buckycatcher–C₆₀ complex,$^{35}$ consisting of 148 atoms or 120 heavy atoms, will be considered at the level of DLPNO-CCSD(T₀)/CBS with TightPNO threshold for the first time. Furthermore, despite the lack of the exact canonical CCSD(T)

---
J. Chem. Phys. **154**, 154104 (2021); doi: 10.1063/5.0042906
Published under license by AIP Publishing

**154**, 154104-2

references for comparison, benchmark results obtained in this work can still indicate additional information about the accuracy of local CCSD(T) and FN-DMC in large complexes.

## II. COMPUTATIONAL DETAILS

The CCSD(T)/CBS interaction energy in this work was obtained as a sum of the MP2/CBS interaction energy and a $\Delta$CCSD(T) correlation correction term extrapolated to the CBS limit,
$$
\begin{aligned}
E^{\mathrm{CCSD(T)/CBS}} &= E^{\mathrm{MP2/CBS}} + \Delta E_{\mathrm{corr}}^{\mathrm{DLPNO-CCSD(T_0)/CBS'}} \\
&= E^{\mathrm{MP2/CBS}} + \left(E_{\mathrm{corr}}^{\mathrm{DLPNO-CCSD(T_0)/CBS'}} - E_{\mathrm{corr}}^{\mathrm{MP2/CBS'}}\right), \quad (1)
\end{aligned}
$$
where CBS$'$ means using smaller basis sets to do the basis-set extrapolation, and the TightPNO threshold$^{13}$ has been used in DLPNO-CCSD(T$_0$). The MP2/CBS term can be further decomposed into Hartree–Fock at the CBS limit (HF/CBS) and MP2/CBS correlation terms,
$$
E^{\mathrm{MP2/CBS}} = E^{\mathrm{HF/CBS}} + E_{\mathrm{corr}}^{\mathrm{MP2/CBS}}. \tag{2}
$$

The HF energy converges with the size of the basis set faster than that for the correlation energy,$^{36}$ and it is adequate to obtain its CBS limit using aug-cc-pVQZ, HF/aQZ.$^{37,38}$ The HF/CBS energy can also be computed using a two-point extrapolation scheme$^{39,40}$ with cardinal numbers $X$ and $Y$ from (a)XZ and (a)YZ, respectively,
$$
E^{\mathrm{HF/CBS}} = \frac{E^{\mathrm{HF/(a)XZ}}e^{-\alpha\sqrt{Y}} - E^{\mathrm{HF/(a)YZ}}e^{-\alpha\sqrt{X}}}{e^{-\alpha\sqrt{Y}} - e^{-\alpha\sqrt{X}}}, \tag{3}
$$
where $\alpha = 4.42, 4.30, 5.46$, and 5.79 for (D,T)Z, a(D,T)Z, (T,Q)Z, and a(T,Q)Z extrapolations, respectively.$^{40}$ The MP2 correlation energy is usually extrapolated to the CBS limit using the robust inverse cubic ($\beta = 3$) extrapolation scheme suggested by Halkier *et al.*$^{20}$ from the aug-cc-pVTZ and aug-cc-pVQZ basis sets.$^{37,38}$ Several groups have pointed out that the optimum exponent for correlation energy extrapolations using double- and triple-$\zeta$ basis sets should be smaller than 3.$^{40,41}$ The general MP2 correlation energy at the CBS limit can be computed with cardinal numbers $X$ and $Y$ from (a)XZ and (a)YZ, respectively, using
$$
E_{\mathrm{corr}}^{\mathrm{MP2/CBS}} = \frac{E_{\mathrm{corr}}^{\mathrm{MP2/(a)XZ}}X^\beta - E_{\mathrm{corr}}^{\mathrm{MP2/(a)YZ}}Y^\beta}{X^\beta - Y^\beta}, \tag{4}
$$
where $\beta = 2.46, 2.51, 3.05$, and 3.05 for (D,T)Z, a(D,T)Z, (T,Q)Z, and a(T,Q)Z extrapolations, respectively.$^{40}$ The optimal values of aforementioned $\alpha$ and $\beta$ values were fitted to minimize the errors with respect to reference energies for a small-molecule dataset with the system size up to two heavy atoms.$^{40}$ This work is the first time that the performance of these $\alpha$ and $\beta$ values was tested with respect to the benchmark HF/aQZ energies and MP2/a(T,Q)Z correlation energies, respectively, for large noncovalent complexes in L7. In addition to obtaining an optimal $\beta$ value for the (D,T)Z extrapolation scheme, it has also been proposed that one should multiply a factor of 1.08 to account for the missing diffuse basis functions in (D,T)Z with $\beta = 3.^{42}$ This $1.08 \times$ (D,T)Z ($\beta = 3$) scheme is also tested in this work for large complexes in L7. Dunning basis sets$^{43}$ cc-pVXZ (XZ) and aug-cc-pVXZ (aXZ), heavy-aug-cc-pVXZ (haXZ), and the corresponding calendar basis sets$^{44,45}$ jun-cc-pVXZ (jaXZ) and may-cc-pVXZ (maXZ) have been employed for these tests. The same $\alpha$ and $\beta$ values for aXZ were employed for haXZ, jaXZ, and maXZ.

Due to the steep scaling of DLPNO-CCSD(T$_0$) calculations with system size, this work is the first time that DLPNO-CCSD(T$_0$)/cc-pVTZ with TightPNO threshold for the two largest complexes involving circumcoronene in the L7 dataset, DNA-ellipticine, and buckycatcher-$C_{60}$ has been applied. The $\Delta$CCSD(T) correlation correction term in this work is extrapolated to the CBS limit using the ha(D,T)Z ($\beta = 2.51$) for C2C2PD, CBH, GCGC, GGG, and PHE and the (D,T)Z ($\beta = 3$) scheme for C3A, C3GC, DNA-ellipticine, and buckycatcher-$C_{60}$. As compared to MP2/a(T,Q)Z correlation results for L7 shown further below, the ha(D,T)Z ($\beta = 2.51$) only shows marginal errors, and the (D,T)Z ($\beta = 3$) scheme performs much better than (D,T)Z ($\beta = 2.46$) and $1.08 \times$ (D,T)Z ($\beta = 3$).

Based on the CBS convergence study in L7 shown below, the converged HF binding energies for complexes in L7, DNA-ellipticine, and buckycatcher-$C_{60}$ were obtained using aQZ, haQZ, and jaQZ, respectively, and the corresponding CBS limit of MP2 correlation energies was obtained using a(T,Q)Z ($\beta = 3$), ha(T,Q)Z ($\beta = 3$), and ha(D,T)Z ($\beta = 2.51$) extrapolation schemes, respectively. The correlation correction terms $\Delta$CCSD(T)/ha(D,T)Z with $\beta = 2.51$ for C2C2PD, CBH, GCGC, GGG, and PHE, and $\Delta$CCSD(T)/(D,T)Z with $\beta = 3$ for C3A, C3GC, DNA-ellipticine, and buckycatcher-$C_{60}$ were added to these MP2/CBS ($E^{\mathrm{HF/CBS}} + E_{\mathrm{corr}}^{\mathrm{MP2/CBS}}$) binding energies to obtain benchmark DLPNO-CCSD(T$_0$)/CBS binding energies.

There are two main sources of error from the DLPNO-CCSD(T$_0$)/CBS focal-point scheme employed in this work, and they are the basis-set incompleteness error ($\Delta_{\mathrm{BSI}}$) and the local approximation error ($\Delta_{\mathrm{LA}}$), both of which are derived from the $\Delta$CCSD(T) term. For C2C2PD, CBH, GCGC, GGG, and PHE, the ha(D,T)Z ($\beta = 2.51$) extrapolation scheme was used in $\Delta$CCSD(T) to limit $\Delta_{\mathrm{BSI}}$. The good performance of ha(D,T)Z ($\beta = 2.51$) can be justified upon comparison with L7 MP2/a(T,Q)Z correlation energies as shown further below. Hence, it is reasonable to assume that $\Delta_{\mathrm{BSI}}$ is marginal in these five complexes. The $\Delta_{\mathrm{BSI}}$ uncertainty for $\Delta$CCSD(T)/(D,T)Z ($\beta = 3$) used in C3A, C3GC, DNA-ellipticine, and buckycatcher-$C_{60}$ was estimated using the percentage error ($\sim$4%) of $\Delta$CCSD(T)/(D,T)Z ($\beta = 3$) as compared with $\Delta$CCSD(T)/ha(D,T)Z ($\beta = 2.51$) in C2C2PD, which shows the largest $\Delta$CCSD(T) correction in L7. It should be noted that $\Delta$CCSD(T)/(D,T)Z ($\beta = 3$) is always overcorrected ($\Delta_{\mathrm{BSI}} > 0$) as compared with $\Delta$CCSD(T)/ha(D,T)Z ($\beta = 2.51$) for all C2C2PD, CBH, GCGC, GGG, and PHE. The $\Delta_{\mathrm{LA}}$ uncertainty for DLPNO-CCSD(T$_0$) used in $\Delta$CCSD(T) was decomposed into the DLPNO-CCSD and DLPNO-(T$_0$) parts, $\Delta_{\mathrm{LA}} = \Delta_{\mathrm{CCSD}}+\Delta_{(\mathrm{T_0})}$. The correlation-energy dependence of $\Delta_{\mathrm{CCSD}}$ and $\Delta_{(\mathrm{T_0})}$ can be obtained, respectively, by fitting the deviation of DLPNO-CCSD and DLPNO-(T$_0$) with respect to the canonical CCSD and (T) based on frozen natural orbitals (FNOs)$^{46}$ using a series of aromatic $\pi$–$\pi$ stacking dimers of polycyclic aromatic hydrocarbons (PAHs). These complexes show similar binding features as complexes in L7, DNA-ellipticine, and buckycatcher-$C_{60}$, which are dispersion-bound dimers and, thus, are suitable for use as model systems to analyze the deviation of DLPNO-CCSD and DLPNO-(T$_0$) in these analogous dispersion-bound complexes. It can be seen below that $\Delta_{\mathrm{CCSD}} < 0$ and $\Delta_{(\mathrm{T_0})} > 0$ both occur with some regularity in these model systems, and

therefore, $\Delta_{\text{LA}} = \Delta_{\text{CCSD}} + \Delta_{(T_0)}$ is small based on good error cancellation. The uncertainty in our DLPNO-CCSD($T_0$)/CBS results is indicated by the sum of the two absolute errors, $|\Delta_{\text{BSI}}| + |\Delta_{\text{LA}}|$, where the potential cancellation of errors between $\Delta_{\text{BSI}}$ and $\Delta_{\text{LA}}$ is not taken into account.

PBE0,⁴⁷ B97M-V,⁴⁸ $\omega$B97M-V,⁴⁹ MP2, and FNO-CCSD(T) energy calculations were performed using version 1.3.2 of the PSI4 program,⁵⁰ and DLPNO-CCSD, semi-canonical DLPNO-($T_0$), and iterative DLPNO-(T) calculations were performed using version 4.2.1 of the ORCA program.⁵¹ The sandwich geometries for aromatic $\pi$–$\pi$ stacking dimers of benzene ($D_{6h}$), naphthalene ($D_{2h}$), anthracene ($D_{2h}$), phenanthrene ($C_{2v}$), and pyrene ($D_{2h}$) were optimized at the level of B97M-V/def2-SVPD using version 5.1 of Q-CHEM.⁵² The Cartesian coordinates for these dimers of PAHs are provided in the supplementary material. The resolution-of-the-identity (RI) or density-fitting (DF) approximation was employed during the self-consistent field as well as post-HF calculations using PSI4 and ORCA. All PSI4 calculations used (aug/heavy-aug/jun/may)-cc-pVXZ-JKFIT/(aug/heavy-aug/jun/may)-cc-pVXZ-RI as the corresponding JKFIT/RI basis sets for (aug/heavy-aug/jun/may)-cc-pVXZ. In ORCA, HF calculations used cc-pVTZ/JK as the auxiliary basis set for both cc-pVDZ and cc-pVTZ, aug-cc-pVTZ/JK for both heavy-aug-cc-pVDZ and heavy-aug-cc-pVTZ, and aug-cc-pVQZ/JK for heavy-aug-cc-pVQZ; post-HF calculations used cc-pVDZ/C, cc-pVTZ/C, aug-cc-pVDZ/C, aug-cc-pVTZ/C, and aug-cc-pVQZ/C as auxiliary basis sets for cc-pVDZ, cc-pVTZ, heavy-aug-cc-pVDZ, heavy-aug-cc-pVTZ, and heavy-aug-cc-pVQZ, respectively. The D4 dispersion correction for PBE0 including three-body effects described by an Axilrod–Teller–Muto term was performed with the DFT-D4 standalone program using the electronegativity equilibration charges.⁵³ All calculations were counterpoise corrected to eliminate the basis set superposition error. The core electrons were kept frozen in all of the correlation calculations. The most expensive calculation in this work was DLPNO-CCSD($T_0$)/cc-pVTZ with TightPNO threshold for buckycatcher-$C_{60}$ (3992 basis functions), which took ~17 days using 48 cores in a node with two AMD EPYC 7742 processors, 2TB memory, and a 3TB disk.

## III. RESULTS AND DISCUSSION

Table I shows the mean absolute error (MAE) and maximum error (MAX) for HF with different basis sets and various HF extrapolation schemes with respect to HF/aQZ in L7. It is expected that the quality of HF interaction energies degrades by decreasing the number of diffuse functions in the order of aXZ, haXZ, jaXZ, maXZ, and XZ, as indicated in Table I. As compared with HF/aQZ, the HF component of the interaction energies seems essentially converged with the haQZ, jaQZ, and maQZ basis sets with MAEs of 0.001, 0.002, and 0.005 kcal/mol, respectively. This conclusion is consistent with the observation by Marchetti and Werner⁵⁴ for the S22 dataset that HF/haQZ is essentially converged. If the quadruple-$\zeta$ basis calculation with diffuse functions (haQZ, jaQZ, or maQZ) is available, it is not necessary to do the CBS extrapolation for HF since the CBS extrapolation degrades the performance of the corresponding quadruple-$\zeta$ basis calculation. The (D,T)Z ($\alpha = 4.42$) extrapolation scheme used as a part of benchmark components, HF/CBS, for L7 in previous studies¹⁴²¹ is the worst extrapolation scheme shown in Table I with a MAE of 0.142 kcal/mol and a MAX of 0.349 kcal/mol and is even worse than HF/haDZ and HF/TZ. If the quadruple-$\zeta$ basis calculation with diffuse functions is not available, HF/haTZ is recommended to obtain the converged HF interaction energies with a MAE of 0.012 kcal/mol and a MAX of 0.044 kcal/mol and performs better than HF/QZ and HF/(T,Q)Z. Hence, it is expected that to have a better HF interaction energy, adding diffuse functions rather than higher angular momentum basis functions is the appropriate route to achieve this goal.

Table II shows MAE and MAX for the MP2 correlation with different basis sets and various MP2 correlation extrapolation

<table>
<caption>TABLE I. Mean absolute error (MAE) and maximum error (MAX) in kcal/mol of the Hartree–Fock energies for the L7 dataset with respect to HF/aug-cc-pVQZ. The bold is to indicate reliable alternative approaches when HF/aug-cc-pVQZ is not available.</caption>
<tbody>
<tr>
<td></td>
<td>MAE</td>
<td>MAX</td>
<td></td>
<td>MAE</td>
<td>MAX</td>
</tr>
<tr>
<td>DZ</td>
<td>0.260</td>
<td>0.879</td>
<td>(D,T)Z ($\alpha = 4.42^a$)</td>
<td>0.142</td>
<td>0.349</td>
</tr>
<tr>
<td>TZ</td>
<td>0.127</td>
<td>0.252</td>
<td>(T,Q)Z ($\alpha = 5.46^a$)</td>
<td>0.027</td>
<td>0.059</td>
</tr>
<tr>
<td>QZ</td>
<td>0.047</td>
<td>0.090</td>
<td>ma(T,Q)Z ($\alpha = 5.79^a$)</td>
<td>0.009</td>
<td>0.018</td>
</tr>
<tr>
<td>maTZ</td>
<td>0.041</td>
<td>0.116</td>
<td>ja(D,T)Z ($\alpha = 4.30^a$)</td>
<td>0.064</td>
<td>0.259</td>
</tr>
<tr>
<td><b>maQZ</b></td>
<td><b>0.005</b></td>
<td><b>0.010</b></td>
<td>ja(T,Q)Z ($\alpha = 5.79^a$)</td>
<td>0.006</td>
<td>0.021</td>
</tr>
<tr>
<td>jaDZ</td>
<td>0.149</td>
<td>0.398</td>
<td>ha(D,T)Z ($\alpha = 4.30^a$)</td>
<td>0.027</td>
<td>0.062</td>
</tr>
<tr>
<td>jaTZ</td>
<td>0.024</td>
<td>0.092</td>
<td>ha(T,Q)Z ($\alpha = 5.79^a$)</td>
<td>0.002</td>
<td>0.003</td>
</tr>
<tr>
<td><b>jaQZ</b></td>
<td><b>0.002</b></td>
<td><b>0.003</b></td>
<td>a(D,T)Z ($\alpha = 4.30^a$)</td>
<td>0.033</td>
<td>0.067</td>
</tr>
<tr>
<td>haDZ</td>
<td>0.115</td>
<td>0.203</td>
<td>a(T,Q)Z ($\alpha = 5.79^a$)</td>
<td>0.003</td>
<td>0.010</td>
</tr>
<tr>
<td>haTZ</td>
<td>0.012</td>
<td>0.044</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><b>haQZ</b></td>
<td><b>0.001</b></td>
<td><b>0.007</b></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>aDZ</td>
<td>0.120</td>
<td>0.222</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>aTZ</td>
<td>0.010</td>
<td>0.036</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="6">$^a$The extrapolated parameter $\alpha$ is from Ref. 40.</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th></th>
<th>MAE</th>
<th>MAX</th>
<th></th>
<th>MAE</th>
<th>MAX</th>
</tr>
</thead>
<tbody>
<tr>
<td>DZ</td>
<td>9.527</td>
<td>17.555</td>
<td>(D,T)Z ($\beta = 2.46^{\mathrm{a}}$)</td>
<td>0.856</td>
<td>1.961</td>
</tr>
<tr>
<td>TZ</td>
<td>2.974</td>
<td>5.280</td>
<td>(T,Q)Z ($\beta = 3.05^{\mathrm{a}}$)</td>
<td>0.310</td>
<td>0.764</td>
</tr>
<tr>
<td>QZ</td>
<td>1.055</td>
<td>1.749</td>
<td>ma(T,Q)Z ($\beta = 3.05^{\mathrm{a}}$)</td>
<td>0.467</td>
<td>0.901</td>
</tr>
<tr>
<td>maTZ</td>
<td>2.107</td>
<td>3.491</td>
<td>ja(D,T)Z ($\beta = 2.51^{\mathrm{a}}$)</td>
<td>1.465</td>
<td>2.737</td>
</tr>
<tr>
<td>maQZ</td>
<td>0.603</td>
<td>0.925</td>
<td>ja(T,Q)Z ($\beta = 3.05^{\mathrm{a}}$)</td>
<td>0.141</td>
<td>0.243</td>
</tr>
<tr>
<td>jaDZ</td>
<td>5.639</td>
<td>9.372</td>
<td>ha(D,T)Z ($\beta = 2.51^{\mathrm{a}}$)</td>
<td>0.055</td>
<td>0.137</td>
</tr>
<tr>
<td>jaTZ</td>
<td>1.103</td>
<td>1.640</td>
<td>ha(T,Q)Z ($\beta = 3.05^{\mathrm{a}}$)</td>
<td>0.016</td>
<td>0.044</td>
</tr>
<tr>
<td>jaQZ</td>
<td>0.376</td>
<td>0.540</td>
<td>a(D,T)Z ($\beta = 2.51^{\mathrm{a}}$)</td>
<td>0.073</td>
<td>0.178</td>
</tr>
<tr>
<td>haDZ</td>
<td>1.970</td>
<td>2.841</td>
<td>a(T,Q)Z ($\beta = 3.05^{\mathrm{a}}$)</td>
<td>0.006</td>
<td>0.009</td>
</tr>
<tr>
<td>haTZ</td>
<td>0.709</td>
<td>0.977</td>
<td>(D,T)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.347</td>
<td>0.968</td>
</tr>
<tr>
<td>haQZ</td>
<td>0.297</td>
<td>0.416</td>
<td>$1.08 \times$ (D,T)Z ($\beta = 3^{\mathrm{b},\mathrm{c}}$)</td>
<td>2.385</td>
<td>4.899</td>
</tr>
<tr>
<td>aDZ</td>
<td>1.664</td>
<td>2.600</td>
<td>(T,Q)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.345</td>
<td>0.827</td>
</tr>
<tr>
<td>aTZ</td>
<td>0.572</td>
<td>0.887</td>
<td>ma(T,Q)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.494</td>
<td>0.947</td>
</tr>
<tr>
<td>aQZ</td>
<td>0.241</td>
<td>0.374</td>
<td>ja(D,T)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.807</td>
<td>1.616</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>ja(T,Q)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.154</td>
<td>0.263</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>ha(D,T)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.178</td>
<td>0.343</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>ha(T,Q)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.011</td>
<td>0.053</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>a(D,T)Z ($\beta = 3^{\mathrm{b}}$)</td>
<td>0.129</td>
<td>0.273</td>
</tr>
</tbody>
</table>

TABLE II. Mean absolute error (MAE) and maximum error (MAX) in kcal/mol of the MP2 correlation energies for the L7 dataset with respect to MP2/a(T,Q)Z ($\beta = 3$). The bold is to indicate reliable alternative approaches when MP2/a(T,Q)Z is not available.

$^{\mathrm{a}}$The extrapolated parameter $\beta$ is from Ref. 40.
$^{\mathrm{b}}$The extrapolated parameter $\beta$ is from Ref. 20.
$^{\mathrm{c}}$The 1.08 scaling factor is from Ref. 42.

schemes, including the regular inverse cubic scheme$^{20}$ and other extrapolation components, $^{40}$ with respect to MP2/a(T,Q)Z ($\beta = 3$) in L7. It shows the same trend as HF that the quality of MP2 correlation energies improves by increasing the number of diffuse functions. It is different from HF in that the extrapolation scheme always improves MP2 correlation energies except ja(D,T)Z ($\beta = 2.51$). The (D,T)Z ($\beta = 2.46$) extrapolation scheme for correlation energies used in L7 before $^{14,21}$ shows a MAE of 0.856 kcal/mol and a MAX of 1.961 kcal/mol. The regular inverse cubic scheme ($\beta = 3$) works better for (D,T)Z with a MAE of 0.347 kcal/mol and a MAX of 0.968 kcal/mol. The $1.08 \times$ (D,T)Z ($\beta = 3$) scheme performs the worst in Table II with a MAE of 2.385 kcal/mol and a MAX of 4.899 kcal/mol. Thus, it is recommended to use (D,T)Z ($\beta = 3$) for correlation energies of large noncovalent complexes if TZ is the largest reachable basis set. If a(T,Q)Z ($\beta = 3$) is not available, ha(T,Q)Z ($\beta = 3$), a(D,T)Z ($\beta = 2.51$), and ha(D,T)Z ($\beta = 2.51$) are reliable alternative approaches to obtain converged correlation energies with MAEs of 0.011, 0.073, and 0.055 kcal/mol, respectively. The ha(D,T)Z ($\beta = 2.51$) scheme is attractive because the largest basis set is triple-$\zeta$ with diffuse functions only on heavy atoms.

The conclusions obtained from the information in both tables provided the framework through which we derived the benchmark values for DNA-ellipticine and buckycatcher-$C_{60}$ complexes, where the haQZ and jaQZ basis sets are used to obtain converged HF interaction energies, respectively. For the converged MP2 correlation energies, ha(T,Q)Z ($\beta = 3$) and ha(D,T)Z ($\beta = 2.51$) are employed to the corresponding complexes.

For the $\Delta$CCSD(T) correction term, ha(D,T)Z ($\beta = 2.51$) is used for C2C2PD, CBH, GCGC, GGG, and PHE. The $\Delta$CCSD(T) correction terms for these five complexes using ha(D,T)Z ($\beta = 2.51$), haTZ, haDZ, (D,T)Z ($\beta = 3$), TZ, and DZ are shown in Table III. As compared with ha(D,T)Z ($\beta = 2.51$), haTZ shows good performance with a MAE of 0.16 kcal/mol and a MAX of 0.35 kcal/mol. This observation confirms the quality of haTZ, which has been extensively used with $\Delta$CCSD(T) to obtain benchmark values for noncovalent interactions in small dimers, such as complexes in HSG and X40. $^{55,56}$ The next best two are TZ and (D,T)Z ($\beta = 3$) with MAEs of 0.26 and 0.32 kcal/mol, respectively. The haDZ basis set is slightly worse than TZ and (D,T)Z ($\beta = 3$) with a MAE of 0.43 kcal/mol, and DZ is the worst with a MAE of 1.26 kcal/mol. Thus, it is expected that higher angular momentum basis functions are more important than adding diffuse functions to approach the converged $\Delta$CCSD(T). The haTZ and haDZ basis sets undercorrect $\Delta$CCSD(T) in C2C2PD, CBH, GCGC, and GGG but overcorrect it in PHE. The TZ and DZ basis sets undercorrect $\Delta$CCSD(T) in C2C2PD, GCGC, and GGG but overcorrect it in CBH and PHE. The (D,T)Z ($\beta = 3$) extrapolation scheme overcorrects $\Delta$CCSD(T) in all five complexes. Since (D,T)Z ($\beta = 3$) shows a consistent overcorrection for $\Delta$CCSD(T) with a reasonable MAE as compared with ha(D,T)Z ($\beta = 2.51$), (D,T)Z ($\beta = 3$) is used to obtain $\Delta$CCSD(T) for the rest of four large complexes, C3A, C3GC, DNA-ellipticine, and buckycatcher-$C_{60}$. The maximum error of (D,T)Z ($\beta = 3$) in Table III is from C2C2PD, which shows the largest $\Delta$CCSD(T) among all complexes in L7, where the corresponding $\Delta$CCSD(T)/(D,T)Z ($\beta = 3$) terms for C3A and C3GC are 10.13 and 16.63 kcal/mol, respectively. The percentage error for C2C2PD used (D,T)Z ($\beta = 3$) with respect to ha(D,T)Z ($\beta = 2.51$) is about +4%, which is used to estimate $\Delta_{\mathrm{BSI}}$ for $\Delta$CCSD(T)/(D,T)Z ($\beta = 3$) used in C3A, C3GC, DNA-ellipticine, and buckycatcher-$C_{60}$.

The $\Delta_{\mathrm{LA}}$ uncertainty for DLPNO-CCSD($\mathrm{T}_{0}$) used in $\Delta$CCSD(T) was decomposed into the DLPNO-CCSD and DLPNO-($\mathrm{T}_{0}$) parts, $\Delta_{\mathrm{LA}} = \Delta_{\mathrm{CCSD}} + \Delta_{(\mathrm{T}_{0})}$, which can be obtained by fitting their deviations with respect to the canonical FNO-CCSD and FNO-(T), respectively, using a series of aromatic $\pi-\pi$ stacking dimers of benzene, naphthalene, anthracene, phenanthrene, and pyrene with the same dispersion binding features as complexes in L7, DNA-ellipticine, and buckycatcher-$C_{60}$. Figure 1 shows the errors of DLPNO-CCSD, the “semi-canonical” DLPNO-($\mathrm{T}_{0}$), and iterative DLPNO-(T) $^{33}$ with respect to their canonical counterparts for these

<table>
<thead>
<tr>
<th></th>
<th>ha(D,T)Z</th>
<th>haTZ</th>
<th>haDZ</th>
<th>(D,T)Z</th>
<th>TZ</th>
<th>DZ</th>
</tr>
</thead>
<tbody>
<tr>
<td>C2C2PD</td>
<td>17.14</td>
<td>16.80</td>
<td>16.19</td>
<td>17.85</td>
<td>16.51</td>
<td>13.32</td>
</tr>
<tr>
<td>CBH</td>
<td>0.84</td>
<td>0.83</td>
<td>0.81</td>
<td>0.88</td>
<td>0.91</td>
<td>0.98</td>
</tr>
<tr>
<td>GCGC</td>
<td>5.41</td>
<td>5.20</td>
<td>4.83</td>
<td>5.81</td>
<td>5.23</td>
<td>3.84</td>
</tr>
<tr>
<td>GGG</td>
<td>2.42</td>
<td>2.34</td>
<td>2.18</td>
<td>2.51</td>
<td>2.31</td>
<td>1.84</td>
</tr>
<tr>
<td>PHE</td>
<td>0.99</td>
<td>1.12</td>
<td>1.34</td>
<td>1.33</td>
<td>1.28</td>
<td>1.15</td>
</tr>
<tr>
<td>MAE</td>
<td></td>
<td>0.16</td>
<td>0.43</td>
<td>0.32</td>
<td>0.26</td>
<td>1.26</td>
</tr>
<tr>
<td>MAX</td>
<td></td>
<td>0.35</td>
<td>0.96</td>
<td>0.71</td>
<td>0.63</td>
<td>3.83</td>
</tr>
</tbody>
</table>

TABLE III. The $\Delta$CCSD(T) correction terms, $E_{\mathrm{corr}}^{\mathrm{DLPNO-CCSD(T_{0})}} - E_{\mathrm{corr}}^{\mathrm{MP2}}$, in kcal/mol for C2C2PD, CBH, GCGC, GGG, and PHE in L7 using ha(D,T)Z ($\beta = 2.51$), haTZ, haDZ, (D,T)Z ($\beta = 3$), TZ, and DZ. Mean absolute error (MAE) and maximum error (MAX) are with respect to ha(D,T)Z ($\beta = 2.51$).

![](./images/812472623077261314_8.jpg)

PAH dimers using the haDZ basis set. DLPNO-CCSD overestimates the binding energies as compared with the canonical CCSD, and this overestimation increases by either increasing the size of the systems or the binding interactions. In contrast, DLPNO-(T₀) and DLPNO-(T) underestimate the binding energies as compared with the canonical (T), and this underestimation increases by increasing the binding interactions. DLPNO-(T) always shows stronger binding energies than DLPNO-(T₀) in all PAH dimers. Even for C2C2PD in L7, DLPNO-(T) is 0.3 kcal/mol stronger in binding than DLPNO-(T₀) using the cc-pVDZ basis set. The improved iterative perturbative triples correction DLPNO-(T) is more accurate than DLPNO-(T₀) in agreement with Ref. 33 and can reduce the error of DLPNO-(T₀) by ~50%. The overestimation of DLPNO-CCSD largely cancels out the underestimation of DLPNO-(T₀) or DLPNO-(T) to make DLPNO-CCSD(T₀) and DLPNO-CCSD(T) reasonable approximation approaches to canonical CCSD(T). Although DLPNO-(T) is more accurate than DLPNO-(T₀), DLPNO-(T₀) benefits highly from the good error cancellation with DLPNO-CCSD for systems larger than the naphthalene dimer. It is expected that DLPNO-CCSD(T₀) is a better approach to reproduce the canonical CCSD(T) results for large dispersion-bound complexes. The performance of DLPNO-CCSD(T) on the benzene dimer with other basis sets has also been tested and shows 0.11, 0.08, and 0.09 kcal/mol errors for haTZ, ha(D,T)Z ($\beta=2.51$), and (D,T)Z ($\beta=3$) with respect to the canonical counterparts, respectively. These errors are similar to the error with haDZ (0.16 kcal/mol), which shows the largest error among all four basis sets in the benzene dimer. It is expected that the predictive equations for $\Delta_{CCSD}$ and $\Delta_{(T_0)}$ shown below may be used to generate the worst case scenario in terms of local errors and also in the very least will not change significantly by using (D,T)Z ($\beta=3$).

The $\Delta_{CCSD}$ uncertainty was obtained by fitting parameters $a$ and $b$ for five PAH dimers using the following equation:

$$
\Delta_{\text{CCSD}} = aE_{\text{corr}}^{\text{DLPNO-CCSD/haDZ}} + b, \tag{5}
$$

where $E_{\text{corr}}^{\text{DLPNO-CCSD/haDZ}}$ is the DLPNO-CCSD/haDZ binding correlation energy and $\Delta_{CCSD}$ is the binding deviation of DLPNO-CCSD/haDZ with respect to the canonical CCSD/haDZ. The fitting parameters are $a=0.0872$ and $b=0.4557$ with $R^2=0.9667$. The $\Delta_{(T_0)}$ uncertainty was obtained by fitting parameters $c$ and $d$ for five PAH dimers using the following equation:

$$
\Delta_{(\text{T}_0)} = cE_{\text{corr}}^{\text{DLPNO-}(\text{T}_0)\text{/haDZ}} + d, \tag{6}
$$

where $E_{\text{corr}}^{\text{DLPNO-}(\text{T}_0)\text{/haDZ}}$ is the DLPNO-(T₀)/haDZ binding correlation energy and $\Delta_{(T_0)}$ is the binding deviation of DLPNO-(T₀)/haDZ with respect to the canonical (T)/haDZ. The fitting parameters are $c=-0.3531$ and $d=-0.0749$ with $R^2=0.9996$. These two equations are used to estimate $\Delta_{CCSD}$ and $\Delta_{(T_0)}$ for complexes in L7, DNA-ellipticine, and buckycatcher-$C_{60}$. All uncertainties estimated for DLPNO-CCSD(T₀)/CBS binding energies in this work including $\Delta_{\text{BSI}}$ and $\Delta_{\text{LA}}$, which are the sum of $\Delta_{CCSD}$ and $\Delta_{(T_0)}$, are shown in Table IV. In all complexes, the $\Delta_{CCSD}$ and $\Delta_{(T_0)}$ errors are always $<0$ and $>0$, respectively. The sum of $\Delta_{CCSD}$ and $\Delta_{(T_0)}$, which is $\Delta_{\text{LA}}$, is always $<0$ except GGG, which shows a very small positive (0.09 kcal/mol) $\Delta_{\text{LA}}$. In addition, $\Delta_{\text{LA}}$ is always smaller than the individual terms, $\Delta_{CCSD}$ and $\Delta_{(T_0)}$, based on good error cancellation. The total uncertainty of our DLPNO-CCSD(T₀)/CBS results is estimated by the sum of the two absolute errors, $|\Delta_{\text{BSI}}| + |\Delta_{\text{LA}}|$, where the potential cancellation of errors between $\Delta_{\text{BSI}}$ ($>0$) and $\Delta_{\text{LA}}$ ($<0$) is not taken into account. One may note that the error cancellation of $\Delta_{CCSD}$ and $\Delta_{(T_0)}$ is particularly good in PHE, which leads to only $-0.01$ kcal/mol error for $\Delta_{\text{LA}}$. The total uncertainty for PHE is very small based on the assumption that $\Delta_{\text{BSI}}$ is zero by using the ha(D,T)Z ($\beta=2.51$) extrapolation scheme. This assumption is reasonable because ha(D,T)Z ($\beta=2.51$) is very close to the CBS limit as shown in Table II for MP2 correlation energies. In addition, using the $\pi-\pi$ stacking benzene dimer as another example, MP2, DLPNO-CCSD(T₀), and $\Delta$CCSD(T) binding correlation energies employing ha(D,T)Z ($\beta=2.51$) only deviate $-0.06$, $-0.03$, and 0.03 kcal/mol, respectively, as compared with the corresponding binding energies using ha(T,Q)Z ($\beta=3$). The ha(D,T)Z ($\beta=2.51$) scheme is very close to the CBS limit in $\Delta$CCSD(T), and therefore, it is, indeed, reasonable to assume its $\Delta_{\text{BSI}}$ is zero. Although the 0.01 kcal/mol uncertainty for PHE looks unpractical, its uncertainty is kept in order to have a consistent estimation of uncertainty for all complexes in this work. We show in Table V that the reported binding energy for PHE in this work even without including the uncertainty is very close to the value estimated previously by LNO-CCSD(T).²³

Table V shows the DLPNO-CCSD(T₀)/CBS interaction energies for L7 in this work with the corresponding error estimates and compares previous LNO-CCSD(T)²³ and two FN-DMC results.²³,³² The minimum difference ($\Delta_{\text{min}}$) by considering the estimated error bars between the current DLPNO-CCSD(T₀)/CBS and LNO-CCSD(T)/FN-DMC is also given. The reported DLPNO-CCSD(T₀) results for L7 in this work agree perfectly on all the interaction energies of LNO-CCSD(T), taking error bars into account, and allow for a certain degree of confidence with respect to basis-set incompleteness errors as well as local correlation errors, both of which are warranted critiques of the local CCSD(T)/CBS paradigm as it currently stands. The agreement for these L7 complexes for the DLPNO-CCSD(T₀) results reported in this work and the previous LNO-CCSD(T) results²³ indicates that their absolute interaction

TABLE IV. The $\Delta_{\mathrm{BSI}}$ and $\Delta_{\mathrm{LA}}$ errors for DLPNO-CCSD(T$_0$)/CBS binding energies of complexes in L7, DNA-ellipticine, and buckycatcher-C$_{60}$. There are no $\Delta_{\mathrm{BSI}}$ for C2C2PD, CBH, GCGC, GGG, and PHE due to the accurate ha(D,T)Z ($\beta$ = 2.51) extrapolation scheme employed in their $\Delta$CCSD(T) terms. Based on the comparison of $\Delta$CCSD(T) using ha(D,T)Z ($\beta$ = 2.51) and (D,T)Z ($\beta$ = 3) in C2C2PD, the $\Delta_{\mathrm{BSI}}$ errors for $\Delta$CCSD(T)/(D,T)Z ($\beta$ = 3) used in C3A, C3GC, DNA-ellipticine, and buckycatcher-C$_{60}$ were estimated as 4% of their $\Delta$CCSD(T) terms. The $\Delta_{\mathrm{LA}}$ can be decomposed as the sum of $\Delta_{\mathrm{CCSD}}$ and $\Delta_{(\mathrm{T}_0)}$, which were obtained from the predictive Eqs. (5) and (6), respectively. The total uncertainty is the sum of the two absolute errors, $|\Delta_{\mathrm{BSI}}| + |\Delta_{\mathrm{LA}}|$, where the potential cancellation of errors between $\Delta_{\mathrm{BSI}}$ and $\Delta_{\mathrm{LA}}$ is not taken into account.

|  |  | $\Delta_{\mathrm{LA}} = \Delta_{\mathrm{CCSD}} + \Delta_{(\mathrm{T}_0)}$ |  |  |
| :--- | :---: | :---: | :---: | :---: |
|  | $\Delta_{\mathrm{BSI}}$ | $\Delta_{\mathrm{CCSD}}$ | $\Delta_{(\mathrm{T}_0)}$ | $\Delta_{\mathrm{CCSD}} + \Delta_{(\mathrm{T}_0)}$ | $|\Delta_{\mathrm{BSI}}| + |\Delta_{\mathrm{LA}}|$ |
| C2C2PD |  | $-2.29$ | $1.84$ | $-0.44$ | $0.44$ |
| C3A | $0.41$ | $-1.53$ | $1.15$ | $-0.38$ | $0.79$ |
| C3GC | $0.67$ | $-3.01$ | $2.13$ | $-0.88$ | $1.55$ |
| CBH |  | $-0.93$ | $0.76$ | $-0.17$ | $0.17$ |
| GCGC |  | $-1.48$ | $1.21$ | $-0.27$ | $0.27$ |
| GGG |  | $-0.32$ | $0.41$ | $0.09$ | $0.09$ |
| PHE |  | $-0.44$ | $0.43$ | $-0.01$ | $0.01$ |
| DNA-ellipticine | $0.68$ | $-4.35$ | $2.86$ | $-1.48$ | $2.16$ |
| Buckycatcher-C$_{60}$ | $1.49$ | $-5.46$ | $3.48$ | $-1.98$ | $3.47$ |

energies are established references and can be used to benchmark other methods for large noncovalent complexes.

Taking error bars into account, the minimum difference, $\Delta_{\text{min}}$, between the two FN-DMC results is up to 0.8 kcal/mol for GCGC by employing different approximations in these two studies. $^{23,32}$ Comparing the FN-DMC results from Benali $et$ $al.^{32}$ with our DLPNO-CCSD(T$_0$) results, there are three complexes with $\Delta_{\text{min}}$ over the so-called "chemical accuracy" of 1 kcal/mol, and they are C2C2PD (2.3 kcal/mol), C3GC (1.1 kcal/mol), and GCGC (2.1 kcal/mol), which all exhibit significant $\pi$-$\pi$ interactions. The remaining four complexes are within the error bars. When comparing the FN-DMC results from Al-Hamdani $et$ $al.^{23}$ with our DLPNO-CCSD(T$_0$) results, there are only two complexes with $\Delta_{\text{min}}$ over 1 kcal/mol: C2C2PD (2.0 kcal/mol) and C3GC (2.2 kcal/mol), which again exhibit significant $\pi$-$\pi$ interactions. However, only one complex, CBH with aliphatic-aliphatic interactions, is within the error bars. As was the case in previous L7 studies, $^{23,32}$ CCSD(T) generally predicts stronger interaction in these complexes than FN-DMC. This is an indication that generally speaking, FN-DMC stabilizes these "bound" complexes weakly relative to the CCSD(T) description. One possible explanation for this may be that the electron correlation is not being sufficiently captured in the DMC family of methods due to an insufficiently flexible trial wavefunction based on the fixed-node approximation. $^{23}$ It has been suggested that employing several slater determinants might mitigate this wavefunction flexibility quandary. $^{23}$ It is worth mentioning that Al-Hamdani $et$ $al.^{23}$ gauged the impact of approximations intrinsic to LNO-CCSD(T) [the basis set saturation, the local approximations, the core electron

TABLE V. Binding energies in kcal/mol for DLPNO-CCSD(T$_0$)/CBS reported in this work, LNO-CCSD(T),$^{23}$ and FN-DMC,$^{23,32}$ and for seven complexes in L7 including the coronene dimer (C2C2PD), the circumcoronene $\cdots$ adenine dimer (C3A), the circumcoronene $\cdots$ guanine-cytosine dimer (C3GC), the octadecane dimer (CBH), the guanine-cytosine base pair dimer (GCGC), the guanine trimer (GGG), and the phenylalanine residues trimer (PHE). The delta value ($\Delta_{\text{min}}$) is the minimum difference by considering the estimated error bars between the DLPNO-CCSD(T$_0$)/CBS binding energies reported in this work and the LNO-CCSD(T)/FN-DMC results in the literature. The $E^{\text{HF/aQZ}} + E_{\text{corr}}^{\text{MP2/a(T,Q)Z($\beta$=3)}} + \Delta E_{\text{corr}}^{\text{DLPNO-CCSD(T$_0$)/ha(D,T)Z($\beta$=2.51)}}$ scheme was used for C2C2PD, CBH, GCGC, GGG, and PHE, and the $E^{\text{HF/aQZ}} + E_{\text{corr}}^{\text{MP2/a(T,Q)Z($\beta$=3)}} + \Delta E_{\text{corr}}^{\text{DLPNO-CCSD(T$_0$)/(D,T)Z($\beta$=3)}}$ scheme was used for C3A and C3GC.

|  | DLPNO-CCSD(T$_0$)$^{\text{a}}$ | LNO-CCSD(T)$^{\text{b}}$ | $\Delta_{\text{min}}$ | FN-DMC$^{\text{b}}$ | $\Delta_{\text{min}}$ | FN-DMC$^{\text{c}}$ | $\Delta_{\text{min}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| C2C2PD | $-20.93 \pm 0.44$ | $-20.60 \pm 0.62$ | $0.0$ | $-18.1 \pm 0.4$ | $2.0$ | $-17.5 \pm 0.7$ | $2.3$ |
| C3A | $-16.91 \pm 0.79$ | $-16.53 \pm 0.75$ | $0.0$ | $-15.0 \pm 0.5$ | $0.6$ | $-16.6 \pm 0.9$ | $0.0$ |
| C3GC | $-28.63 \pm 1.55$ | $-28.70 \pm 1.01$ | $0.0$ | $-24.2 \pm 0.7$ | $2.2$ | $-25.1 \pm 0.9$ | $1.1$ |
| CBH | $-11.00 \pm 0.17$ | $-11.01 \pm 0.15$ | $0.0$ | $-11.4 \pm 0.4$ | $0.0$ | $-10.9 \pm 0.8$ | $0.0$ |
| GCGC | $-13.54 \pm 0.27$ | $-13.59 \pm 0.39$ | $0.0$ | $-12.3 \pm 0.3$ | $0.7$ | $-10.6 \pm 0.6$ | $2.1$ |
| GGG | $-2.08 \pm 0.09$ | $-2.09 \pm 0.20$ | $0.0$ | $-1.5 \pm 0.3$ | $0.2$ | $-2.0 \pm 0.4$ | $0.0$ |
| PHE | $-25.46 \pm 0.01$ | $-25.36 \pm 0.18$ | $0.0$ | $-26.5 \pm 0.7$ | $0.3$ | $-24.9 \pm 0.6$ | $0.0$ |

$^{\text{a}}$This work.
$^{\text{b}}$Reference 23.
$^{\text{c}}$Reference 32.

correlation, and higher-order correlation effects beyond CCSD(T)] and FN-DMC (the fixed-node approximation, the time step bias, and pseudopotentials) and determined that such a sizable deviation (~8 kcal/mol) in $C_{60}$@[6]CPPA between these two state-of-the-art approaches is an order of magnitude beyond these approximations. Hence, binding interactions from the canonical CCSD(T) approach or the full configuration interaction quantum Monte Carlo (FCI-QMC) approach $^{57,58}$ for large noncovalent complexes at the hundred-atom scale are urgently needed to solve the non-negligible differences (over the widely sought 1 kcal/mol chemical accuracy) in binding predictions between local CCSD(T) and FN-DMC.

It should be mentioned that the canonical CCSD(T) with the half-augmented double-$\zeta$ basis set (ha-cc-pVDZ) has been used to calculate the binding in C2C2PD with the energy difference between the MP2/ha-cc-pVTZ and MP2/ha-pVDZ binding energies to correct the residual basis set error. $^{59}$ Its final reporting extrapolated CCSD(T) binding for C2C2PD was $-19.98$ kcal/mol. $^{59}$ Since the size of ha-cc-pVTZ is smaller than that of haTZ, it is necessary to further correct the residual basis set error by including $(E^{\text{HF/haQZ}} - E^{\text{HF/haTZ}})$ for the HF correction and $(E_{\text{corr}}^{\text{MP2/a(T,Q)Z}} - E_{\text{corr}}^{\text{MP2/haTZ}})$ for the MP2 correlation correction reported in this work. These corrections contribute $-0.69$ kcal/mol in binding, and the final canonical CCSD(T)/CBS binding energy for C2C2PD is $-20.67$ kcal/mol. One should note that the actual binding is a little bit stronger because there will be a further correction from ha-cc-pVTZ to haTZ. This canonical CCSD(T) result matches perfectly with the reporting DLPNO-CCSD(T$_0$)/CBS value ($-20.93 \pm 0.44$) in this work and the LNO-CCSD(T)/CBS binding ($-20.60 \pm 0.62$) from the literature. $^{23}$ The agreement exhibited is a good signal to indicate the high quality of DLPNO-CCSD(T$_0$)/CBS values reported in this work. The binding energies with the corresponding MAE and MAX for L7 using MP2/CBS and the three up-to-date DFT functionals, PBE0+D4, $\omega$B97M-V, and B97M-V, combined with def2-TZVPPD are shown in Table VI. MP2 gives a very large MAE of 7.18 kcal/mol due to its strong overestimation of binding energies in $\pi$--$\pi$ stacking complexes. The $\omega$B97M-V, B97M-V, and PBE0+D4 approaches perform very well with MAEs of 0.63, 0.24, and 0.15 kcal/mol, respectively. Furthermore, the binding errors from B97M-V and PBE0+D4 are within 1 kcal/mol chemical accuracy for all complexes in L7.

TABLE VI. Binding energies in kcal/mol for MP2 at the CBS limit and three DFT functionals, $\omega$B97M-V, B97M-V, and PBE0+D4, combined with the def2-TZVPPD basis sets for seven complexes in L7. Mean absolute error (MAE) and maximum error (MAX) for each approach were calculated based on the smallest absolute difference respect to DLPNO-CCSD(T$_0$)/CBS for each complex taking error bars into account.

<table>
  <thead>
    <tr>
      <th></th>
      <th>MP2</th>
      <th>$\omega$B97M-V</th>
      <th>B97M-V</th>
      <th>PBE0+D4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C2C2PD</td>
      <td>$-38.07$</td>
      <td>$-22.66$</td>
      <td>$-20.90$</td>
      <td>$-20.42$</td>
    </tr>
    <tr>
      <td>C3A</td>
      <td>$-27.04$</td>
      <td>$-17.90$</td>
      <td>$-16.53$</td>
      <td>$-15.91$</td>
    </tr>
    <tr>
      <td>C3GC</td>
      <td>$-45.26$</td>
      <td>$-31.15$</td>
      <td>$-29.15$</td>
      <td>$-26.73$</td>
    </tr>
    <tr>
      <td>CBH</td>
      <td>$-11.84$</td>
      <td>$-11.43$</td>
      <td>$-11.79$</td>
      <td>$-11.38$</td>
    </tr>
    <tr>
      <td>GCGC</td>
      <td>$-18.95$</td>
      <td>$-15.18$</td>
      <td>$-14.39$</td>
      <td>$-13.63$</td>
    </tr>
    <tr>
      <td>GGG</td>
      <td>$-4.50$</td>
      <td>$-2.18$</td>
      <td>$-1.88$</td>
      <td>$-1.92$</td>
    </tr>
    <tr>
      <td>PHE</td>
      <td>$-26.45$</td>
      <td>$-25.80$</td>
      <td>$-25.10$</td>
      <td>$-25.29$</td>
    </tr>
    <tr>
      <td>MAE</td>
      <td>$7.18$</td>
      <td>$0.63$</td>
      <td>$0.24$</td>
      <td>$0.15$</td>
    </tr>
    <tr>
      <td>MAX</td>
      <td>$16.70$</td>
      <td>$1.37$</td>
      <td>$0.62$</td>
      <td>$0.35$</td>
    </tr>
  </tbody>
</table>

![](./images/812472623077261314_9.jpg)

FIG. 2. (a) The DNA-ellipticine (157 atoms or 95 heavy atoms) and (b) buckycatcher-$C_{60}$ (148 atoms or 120 heavy atoms) complexes.

The next benchmark system is the DNA-ellipticine intercalation complex depicted in Fig. 2(a), which includes 157 atoms or 95 heavy atoms, and is much larger than the largest complex in terms of heavy atoms (C3GC with 73 heavy atoms) in L7. Using DLPNO-CCSD(T$_0$)/CBS based on $E^{\text{HF/haQZ}}+E_{\text{corr}}^{\text{MP2/ha(T,Q)Z($\beta$=3)}} + \Delta E_{\text{corr}}^{\text{DLPNO-CCSD(T$_0$)/(D,T)Z($\beta$=3)}}$, we are able to report with relatively high confidence the interaction energy (with the corresponding uncertainty) of this complex as a benchmark shown in Table VII. The DLPNO-CCSD(T$_0$)/CBS benchmark reported in this work, for the first time, is $-38.6 \pm 2.2$ kcal/mol, which is at least 1.9 kcal/mol [~5% with respect to DLPNO-CCSD(T$_0$)/CBS] larger than the FN-DMC value in Ref. 34. It is consistent with the observation from the L7 results that DLPNO-CCSD(T$_0$)/CBS predicts stronger binding interaction than FN-DMC. PBE0+D4, $\omega$B97M-V, and B97M-V show binding interactions of $-37.5$, $-43.7$, and $-41.3$ kcal/mol, respectively. They at least overestimate 3.0, 9.2, and 6.8 kcal/mol, respectively, when compared with FN-DMC. As compared with DLPNO-CCSD(T$_0$), PBE0+D4 is within the binding uncertainty, while $\omega$B97M-V and B97M-V overestimate the binding by at least 2.9 and 0.5 kcal/mol, respectively. These three popular functionals, nevertheless, agree better with CCSD(T).

As a final benchmark system, we present interaction energies for the popular and challenging buckycatcher-$C_{60}$ complex as shown in Fig. 2(b), which includes 148 atoms or 120 heavy atoms and is the largest system in terms of heavy atoms in this work. Since MP2/haQZ is not available for buckycatcher-$C_{60}$, MP2/ha(D,T)Z

TABLE VII. Binding energies in kcal/mol for the DNA-ellipticine complex, $^{34}$ consisting of 157 atoms or 95 heavy atoms, where DLPNO-CCSD(T$_0$)/CBS in this work is obtained from $E^{\text{HF/haQZ}}+E_{\text{corr}}^{\text{MP2/ha(T,Q)Z($\beta$=3)}} + \Delta E_{\text{corr}}^{\text{DLPNO-CCSD(T$_0$)/(D,T)Z($\beta$=3)}}$.

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>$E_{\text{int}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DLPNO-CCSD(T$_0$)/CBS$^{\text{a}}$</td>
      <td>$-38.6 \pm 2.2$</td>
    </tr>
    <tr>
      <td>FN-DMC$^{\text{b}}$</td>
      <td>$-33.6 \pm 0.9$</td>
    </tr>
    <tr>
      <td>MP2/CBS$^{\text{a}}$</td>
      <td>$-55.6$</td>
    </tr>
    <tr>
      <td>PBE0+D4/def2-TZVPPD$^{\text{a}}$</td>
      <td>$-37.5$</td>
    </tr>
    <tr>
      <td>$\omega$B97M-V/def2-TZVPPD$^{\text{c}}$</td>
      <td>$-43.7$</td>
    </tr>
    <tr>
      <td>B97M-V/def2-TZVPPD$^{\text{c}}$</td>
      <td>$-41.3$</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">
        $^{\text{a}}$This work.<br>
        $^{\text{b}}$Reference 34.<br>
        $^{\text{c}}$Reference 14.
      </td>
    </tr>
  </tfoot>
</table>


$(\beta = 2.51)$ is used based on its good performance in L7. Here, DNA-ellipticine can be used to further justify the reliability of MP2/ha(D,T)Z $(\beta = 2.51)$. As compared with MP2/ha(T,Q)Z correlation binding energy for the DNA-ellipticine complex, which is $-80.77$ kcal/mol, ha(D,T)Z $(\beta = 3)$, ha(D,T)Z $(\beta = 2.51)$, a(D,T)Z $(\beta = 3)$, and a(D,T)Z $(\beta = 2.51)$ extrapolation schemes deviate 0.30, $-0.12$, 0.22, and $-0.14$ kcal/mol, respectively. It is, therefore, further justified that the ha(D,T)Z $(\beta = 2.51)$ extrapolation scheme is robust and is suitable to obtain the converged MP2 correlation energy for the buckycatcher-$C_{60}$ complex below. In addition, the corresponding MP2 correlation energy deviations from (D,T)Z $(\beta = 3)$, $1.08 \times$ (D,T)Z $(\beta = 3)$, and (D,T)Z $(\beta = 2.46)$ are 0.41, $-6.02$, and $-2.20$ kcal/mol, respectively. Hence, the (D,T)Z $(\beta = 3)$ extrapolation scheme is still a reasonable method to obtain the correlation energy at the CBS limit and will be employed to $\Delta$CCSD(T) for the buckycatcher-$C_{60}$ complex below. In summary, when compared with correlation energies for seven complexes in L7 using MP2/a(T,Q)Z and the DNA-ellipticine complex using MP2/ha(T,Q)Z, the MAEs for these eight complexes are merely 0.35 and 0.06 kcal/mol using (D,T)Z $(\beta = 3)$ and ha(D,T)Z $(\beta = 2.51)$ extrapolation schemes, respectively. These minor deviations allow for cost reduction in employing relatively smaller basis sets to obtain correlation energies at the CBS.

The high quality benchmark for the interaction energy of buckycatcher-$C_{60}$ using DLPNO-CCSD($T_0$)/CBS based on $E_{corr}^{HF/jaQZ} + E_{corr}^{MP2/ha(D,T)Z(\beta=2.51)} + \Delta E_{corr}^{DLPNO-CCSD(T_0)/(D,T)Z(\beta=3)}$ is shown in Table VIII. The deformation energy was computed at the same level of theory as the binding energy calculation, where the deformation energies are 1.48, 1.38, 1.26, 0.82, and 1.00 kcal/mol for MP2/CBS, DLPNO-CCSD($T_0$)/CBS, $\omega$B97M-V/def2-TZVPPD, B97M-V/def2-TZVPPD, and PBE0+D4/def2-TZVPPD, respectively. Its deformation energies from previous works were 1.24, 1.21, and 0.99 kcal/mol using NLDFT/def2-QZVP, $^{42}$ MP2/(D,T)Z, $^{42}$ SCS-MP2/(D,T)Z, $^{42}$ and B97M-V/haTZ, $^{62}$ respectively. Upon comparison with DLPNO-CCSD($T_0$)/CBS deformation energy, MP2/CBS and $\omega$B97M-V/def2-TZVPPD reproduce a reasonable deformation energy value.

<table>
<caption>TABLE VIII. Binding energies in kcal/mol for the buckycatcher-$C_{60}$ complex (4a in S12L), $^{35}$ consisting of 148 atoms or 120 heavy atoms, where DLPNO-CCSD($T_0$)/CBS in this work is obtained from $E_{corr}^{HF/jaQZ} + E_{corr}^{MP2/ha(D,T)Z(\beta=2.51)} + \Delta E_{corr}^{DLPNO-CCSD(T_0)/(D,T)Z(\beta=3)}$.</caption>
<thead>
  <tr>
    <th>Method</th>
    <th>$E_{int}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>DLPNO-CCSD($T_0$)/CBS$^{\text{a}}$</td>
    <td>$-41.1 \pm 3.5$</td>
  </tr>
  <tr>
    <td>FN-DMC$^{\text{b}}$</td>
    <td>$-25.8 \pm 1.5$</td>
  </tr>
  <tr>
    <td>Back-correct experiment$^{\text{c}}$</td>
    <td>$-28.4 \pm 0.6$</td>
  </tr>
  <tr>
    <td>DLPNO-CCSD($T_0$)/CBS*$^{\text{d}}$</td>
    <td>$-33.7$</td>
  </tr>
  <tr>
    <td>MP2/CBS$^{\text{a}}$</td>
    <td>$-78.3$</td>
  </tr>
  <tr>
    <td>PBE0+D4/def2-TZVPPD$^{\text{a}}$</td>
    <td>$-36.3$</td>
  </tr>
  <tr>
    <td>$\omega$B97M-V/def2-TZVPPD$^{\text{a}}$</td>
    <td>$-42.3$</td>
  </tr>
  <tr>
    <td>B97M-V/def2-TZVPPD$^{\text{a}}$</td>
    <td>$-37.7$</td>
  </tr>
  <tr>
    <td>B97M-V/haTZ$^{\text{e}}$</td>
    <td>$-37.6$</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="2">$^{\text{a}}$This work.</td>
  </tr>
  <tr>
    <td colspan="2">$^{\text{b}}$Reference 60.</td>
  </tr>
  <tr>
    <td colspan="2">$^{\text{c}}$Reference 61.</td>
  </tr>
  <tr>
    <td colspan="2">$^{\text{d}}$Reference 24.</td>
  </tr>
  <tr>
    <td colspan="2">$^{\text{e}}$Reference 62.</td>
  </tr>
</tfoot>
</table>

The DLPNO-CCSD($T_0$)/CBS benchmark value for buckycatcher-$C_{60}$ is $-41.1 \pm 3.5$ kcal/mol, which is at least 10.3 (~25%) and 8.6 kcal/mol (~21%) larger than FN-DMC in Ref. 60 and the back-correct experimental result in Ref. 61, respectively. This disagreement is even larger than the one found in the buckyball-ring system ($C_{60}$@[6]CPPA), where the difference between LNO-CCSD(T) and FN-DMC is ~8 kcal/mol (~20%). $^{23}$ DLPNO-CCSD($T_0$)/CBS again predicts stronger binding interaction than FN-DMC, which is consistent with the observation from L7 and DNA-ellipticine. In addition, the DLPNO-CCSD($T_0$)/CBS binding energy reported in this work is at least 3.9 kcal/mol stronger than the previous DLPNO-CCSD($T_0$)/CBS* result$^{24}$ based on the sum of HF/(D,T)Z and 1.08 $\times f \times$ MP2/(D,T)Z correlation energies, where $f$ is the quotient of DLPNO-CCSD($T_0$) (only tightened $T_{\text{CutPairs}}$ to $10^{-5}$ on top of the default setting) and MP2 correlation energies using def2-TZVP. We believe that the DLPNO-CCSD($T_0$)/CBS binding energy reported in this work with larger basis sets, with tighter thresholds for local approximations, and without empirical scaling factors for correlation energies is more accurate than DLPNO-CCSD($T_0$)/CBS*. PBE0+D4, $\omega$B97M-V, and B97M-V show binding interactions of $-36.3$, $-42.3$, and $-37.7$ kcal/mol, respectively. They all overestimate the binding interactions as compared with FN-DMC by at least 9.0, 15.0, and 10.4 kcal/mol, respectively. These three popular functionals agree better with DLPNO-CCSD($T_0$), where $\omega$B97M-V is within the binding uncertainty, while PBE0+D4 and B97M-V underestimate the binding by at least 1.3 and 0.1 kcal/mol, respectively. The binding of buckycatcher-$C_{60}$ using B97M-V shows only 0.1 kcal/mol difference by changing the basis set from haTZ$^{62}$ to def2-TZVPPD.

Although there may be some sources of error from the reporting DLPNO-CCSD($T_0$)/CBS benchmark values with the corresponding uncertainty estimates for large noncovalent complexes, which again shows the unprecedented level of disagreement between state-of-the-art local CCSD(T) and FN-DMC;$^{23,52}$ this work provides DLPNO-CCSD($T_0$)/CBS as alternative benchmarks for L7, DNA-ellipticine, and buckycatcher-$C_{60}$ for the development of low-cost computational approaches.

### IV. CONCLUSIONS

In order to estimate whether the accuracy of methods, such as DFT, semi-empirical approaches, force fields, and machine learning potentials, for small systems is preserved for large systems, reliable benchmark values of large noncovalent complexes are essential. Hence, agreement between the state-of-the-art methods is a useful metric to gauge these benchmark values and provides the relative confidence of the results obtained. First, this work sheds some light on the possible basis-set extrapolation strategies in large noncovalent complexes in order to obtain reliable HF and MP2 correlation energies at the CBS limit at a relatively lower cost. As compared with HF/aQZ energies and MP2/a(T,Q)Z correlation energies for complexes in L7, haQZ, jaQZ, and maQZ are recommended for HF and ha(T,Q)Z $(\beta = 3)$, a(D,T)Z $(\beta = 2.51)$, and ha(D,T)Z $(\beta = 2.51)$ are recommended for the MP2 correlation. Second, this work provides the benchmark binding energies for systems up to 120 heavy atoms including seven dispersion-bound complexes in the L7 dataset,

the DNA-ellipticine intercalation complex, and the buckycatcher-
$C_{60}$ complex using a focal-point method based on the canonical
MP2 and DLPNO-CCSD(T₀) at the CBS limit. The uncertainty of
binding has also been estimated by considering the basis-set incom-
pleteness error and the local approximation error. The DLPNO-
CCSD(T₀)/CBS values in this work for L7 perfectly match the previ-
ously reported LNO-CCSD(T) values taking error bars into account.
Furthermore, both DLPNO-CCSD(T₀)/CBS ($-20.93 \pm 0.44$) and
LNO-CCSD(T)/CBS ($-20.60 \pm 0.62$) for C2C2PD match perfectly
with the combined canonical CCSD(T) value of -20.67 kcal/mol.
This match gives a higher confidence for the quality of benchmark
DLPNO-CCSD(T₀)/CBS values reported in this work. However,
these DLPNO-CCSD(T₀) benchmark values differ substantially with
FN-DMC by at least 2.0 (~10%), 1.9 (~5%), and 10.3 kcal/mol
(~25%) for C2C2PD in L7, DNA-ellipticine, and buckycatcher-$C_{60}$,
respectively. These unprecedented disagreements for large nonco-
valent complexes over the so-called 1 kcal/mol "chemical accuracy"
indicate the canonical CCSD(T) or FCI-QMC binding interactions
at the hundred-atom scale, which are urgently needed to solve
this dilemma. The three up-to-date DFT functionals, PBE0+D4,
$\omega$B97M-V, and B97M-V, have also been employed in L7, DNA-
ellipticine, and buckycatcher-$C_{60}$ and agree better with DLPNO-
CCSD(T₀) with at most 3 kcal/mol discrepancy, where the discrep-
ancy can be up to 15 kcal/mol as compared to FN-DMC. Although
there are still some justified concerns with regard to some of the
approximations necessary in order to make the CBS limit feasible
for CCSD(T), we show that despite this, we can still derive reliable
results at a reasonable computational cost. This is critical, especially
in cases where massive computing power is not available. The value
of the research that this work entails is twofold, as these values can be
applicable today as well as provide the foundations of possible routes
for the extrapolations of tomorrow.

## SUPPLEMENTARY MATERIAL

See the supplementary material for Cartesian coordinates,
and correlation energies of DLPNO-CCSD, DLPNO-(T₀), and
DLPNO-(T), and their canonical counterparts in a series of PAH
dimers.

## ACKNOWLEDGMENTS

This study was supported by the American Chemical Soci-
ety Petroleum Research Fund through Grant No. 61654-DNI6 and
start-up funds from the Virginia Commonwealth University Col-
lege of Humanities and Sciences. This research used resources of
the National Energy Research Scientific Computing Center, which is
supported by the Office of Science of the U.S. Department of Energy
under Contract No. DE-AC02-05CH11231. We also acknowledge
resources provided by the Center for High Performance Comput-
ing at Virginia Commonwealth University (https://chipc.vcu.edu)
for conducting the research reported in this study.

## DATA AVAILABILITY

The data that support the findings of this study are available
within this article and its supplementary material.

## REFERENCES

¹K. Raghavachari, G. W. Trucks, J. A. Pople, and M. Head-Gordon, "A fifth-
order perturbation comparison of electron correlation theories," *Chem. Phys. Lett.*
157(6), 479-483 (1989).

²N. Mardirossian and M. Head-Gordon, "Thirty years of density functional theory
in computational chemistry: An overview and extensive assessment of 200 density
functionals," *Mol. Phys.* 115(19), 2315-2372 (2017).

³P. D. Mezei and O. A. von Lilienfeld, "Noncovalent quantum machine learning
corrections to density functionals," *J. Chem. Theory Comput.* 16(4), 2647-2653
(2020).

⁴Y. S. Al-Hamdani and A. Tkatchenko, "Understanding non-covalent interac-
tions in larger molecular complexes from first principles," *J. Chem. Phys.* 150(1),
010901 (2019).

⁵C. Riplinger, P. Pinski, U. Becker, E. F. Valeev, and F. Neese, "Sparse maps—
A systematic infrastructure for reduced-scaling electronic structure methods. II.
Linear scaling domain based pair natural orbital coupled cluster theory," *J. Chem.
Phys.* 144(2), 024109 (2016).

⁶F. Pavošević, C. Peng, P. Pinski, C. Riplinger, F. Neese, and E. F. Valeev, "Sparse
maps—A systematic infrastructure for reduced scaling electronic structure meth-
ods. V. Linear scaling explicitly correlated coupled-cluster method with pair
natural orbitals," *J. Chem. Phys.* 146(17), 174108 (2017).

⁷G. Schmitz and C. Hättig, "Perturbative triples correction for local pair natu-
ral orbital based explicitly correlated CCSD(F12*) using Laplace transformation
techniques," *J. Chem. Phys.* 145(23), 234107 (2016).

⁸Q. Ma and H.-J. Werner, "Scalable electron correlation methods. V. Parallel per-
turbative triples correction for explicitly correlated local coupled cluster with pair
natural orbitals," *J. Chem. Theory Comput.* 14(1), 198-215 (2018).

⁹W. Li, Z. Ni, and S. Li, "Cluster-in-molecule local correlation method for
post-Hartree-Fock calculations of large systems," *Mol. Phys.* 114(9), 1447-1460
(2016).

¹⁰Y. Guo, U. Becker, and F. Neese, "Comparison and combination of "direct" and
fragment based local correlation methods: Cluster in molecules and domain based
local pair natural orbital perturbation and coupled cluster theories," *J. Chem.
Phys.* 148(12), 124117 (2018).

¹¹P. R. Nagy, G. Samu, and M. Kállay, "Optimization of the linear-scaling local
natural orbital CCSD(T) method: Improved algorithm and benchmark applica-
tions," *J. Chem. Theory Comput.* 14(8), 4193-4215 (2018).

¹²P. R. Nagy and M. Kállay, "Approaching the basis set limit of CCSD(T) energies
for large molecules with local natural orbital coupled-cluster methods," *J. Chem.
Theory Comput.* 15(10), 5275-5298 (2019).

¹³D. G. Liakos, M. Sparta, M. K. Kesharwani, J. M. L. Martin, and F. Neese,
"Exploring the accuracy limits of local pair natural orbital coupled-cluster theory,"
*J. Chem. Theory Comput.* 11(4), 1525-1539 (2015).

¹⁴K. Carter-Fenk, K. U. Lao, K.-Y. Liu, and J. M. Herbert, "Accurate and efficient
ab initio calculations for supramolecular complexes: Symmetry-adapted perturba-
tion theory with many-body dispersion," *J. Phys. Chem. Lett.* 10(11), 2706-2714
(2019).

¹⁵R. Sedlak, T. Janowski, M. Pitoñák, J. Řezáč, P. Pulay, and P. Hobza, "Accuracy
of quantum chemical methods for large noncovalent complexes," *J. Chem. Theory
Comput.* 9(8), 3364-3374 (2013).

¹⁶S. Tsuzuki, K. Honda, T. Uchimaru, M. Mikami, and K. Tanabe, "Origin of
attraction and directionality of the $\pi/\pi$ interaction: Model chemistry calculations
of benzene dimer interaction," *J. Am. Chem. Soc.* 124(1), 104-112 (2002).

¹⁷M. O. Sinnokrot, E. F. Valeev, and C. D. Sherrill, "Estimates of the ab initio limit
for $\pi-\pi$ interactions: The benzene dimer," *J. Am. Chem. Soc.* 124(36), 10887-
10893 (2002).

¹⁸P. Hobza and J. Šponer, "Toward true DNA base-stacking energies: MP2,
CCSD(T), and complete basis set calculations," *J. Am. Chem. Soc.* 124(39),
11802-11808 (2002).

¹⁹P. Jurečka and P. Hobza, "On the convergence of the $(\Delta E^{CCSD(T)} - \Delta E^{MP2})$ term
for complexes with multiple H-bonds," *Chem. Phys. Lett.* 365(1), 89-94 (2002).

²⁰A. Halkier, T. Helgaker, P. Jørgensen, W. Klopper, H. Koch, J. Olsen, and
A. K. Wilson, "Basis-set convergence in correlated calculations on Ne, N₂, and
H₂O," *Chem. Phys. Lett.* 286(3), 243-252 (1998).


$^{21}$ J. Calbo, E. Ortí, J. C. Sancho-García, and J. Aragó, "Accurate treatment of large supramolecular complexes by double-hybrid density functionals coupled with nonlocal van der Waals corrections," J. Chem. Theory Comput. 11(3), 932-939 (2015).

$^{22}$ Q. Ma and H.-J. Werner, "Explicitly correlated local coupled-cluster methods using pair natural orbitals," Wiley Interdiscip. Rev.: Comput. Mol. Biosci. 8(6), e1371 (2018).

$^{23}$ Y. S. Al-Hamdani, P. R. Nagy, D. Barton, M. Kállay, J. G. Brandenburg, and A. Tkatchenko, "Interactions between large molecules: Puzzle for reference quantum-mechanical methods," arXiv:2009.08927v1 (2020).

$^{24}$ J. G. Brandenburg, C. Bannwarth, A. Hansen, and S. Grimme, "B97-3c: A revised low-cost variant of the B97-D density functional method," J. Chem. Phys. 148(6), 064104 (2018).

$^{25}$ H. Kruse, A. Mladek, K. Gkionis, A. Hansen, S. Grimme, and J. Sponer, "Quantum chemical benchmark study on 46 RNA backbone families using a dinucleotide unit," J. Chem. Theory Comput. 11(10), 4972-4991 (2015).

$^{26}$ A. Lúchow, "Quantum Monte Carlo methods," Wiley Interdiscip. Rev.: Comput. Mol. Sci. 1(3), 388-402 (2011).

$^{27}$ B. M. Austin, D. Y. Zubarev, and W. A. Lester, "Quantum Monte Carlo and related approaches," Chem. Rev. 112(1), 263-288 (2012).

$^{28}$ M. Dubecký, L. Mitas, and P. Jurečka, "Noncovalent interactions by quantum Monte Carlo," Chem. Rev. 116(9), 5188-5215 (2016).

$^{29}$ M. Dubecký, P. Jurečka, R. Derian, P. Hobza, M. Otyepka, and L. Mitas, "Quantum Monte Carlo methods describe noncovalent interactions with subchemical accuracy," J. Chem. Theory Comput. 9(10), 4287-4292 (2013).

$^{30}$ M. Dubecký, R. Derian, P. Jurečka, L. Mitas, P. Hobza, and M. Otyepka, "Quantum Monte Carlo for noncovalent interactions: An efficient protocol attaining benchmark accuracy," Phys. Chem. Chem. Phys. 16, 20915-20923 (2014).

$^{31}$ J. Řezáč, M. Dubecký, P. Jurečka, and P. Hobza, "Extensions and applications of the A24 data set of accurate interaction energies," Phys. Chem. Chem. Phys. 17, 19268-19277 (2015).

$^{32}$ A. Benali, H. Shin, and O. Heinonen, "Quantum Monte Carlo benchmarking of large noncovalent complexes in the L7 benchmark set," J. Chem. Phys. 153(19), 194113 (2020).

$^{33}$ Y. Guo, C. Riplinger, U. Becker, D. G. Liakos, Y. Minenkov, L. Cavallo, and F. Neese, "Communication: An improved linear scaling perturbative triples correction for the domain based local pair-natural orbital based singles and doubles coupled cluster method [DLPNO-CCSD(T)]," J. Chem. Phys. 148(1), 011101 (2018).

$^{34}$ A. Benali, L. Shulenburger, N. A. Romero, J. Kim, and O. A. von Lilienfeld, "Application of diffusion Monte Carlo to materials dominated by van der Waals interactions," J. Chem. Theory Comput. 10(8), 3417-3422 (2014).

$^{35}$ S. Grimme, "Supramolecular binding thermodynamics by dispersion-corrected density functional theory," Chem. - Eur. J. 18(32), 9955-9964 (2012).

$^{36}$ A. Halkier, T. Helgaker, P. Jørgensen, W. Klopper, and J. Olsen, "Basis-set convergence of the energy in molecular Hartree-Fock calculations," Chem. Phys. Lett. 302(5), 437-446 (1999).

$^{37}$ T. Takatani, E. G. Hohenstein, M. Malagoli, M. S. Marshall, and C. D. Sherrill, "Basis set consistent revision of the S22 test set of noncovalent interaction energies," J. Chem. Phys. 132(14), 144104 (2010).

$^{38}$ J. Řezáč, K. E. Riley, and P. Hobza, "S66: A well-balanced database of benchmark interaction energies relevant to biomolecular structures," J. Chem. Theory Comput. 7(8), 2427-2438 (2011).

$^{39}$ S. Zhong, E. C. Barnes, and G. A. Petersson, "Uniformly convergent $n$-tuple-$\zeta$ augmented polarized ($n$ZaP) basis sets for complete basis set extrapolations. I. Self-consistent field energies," J. Chem. Phys. 129(18), 184116 (2008).

$^{40}$ F. Neese and E. F. Valeev, "Revisiting the atomic natural orbital approach for basis sets: Robust systematic basis sets for explicitly correlated and conventional correlated $ab$ $initio$ methods?," J. Chem. Theory Comput. 7(1), 33-43 (2011).

$^{41}$ D. G. Truhlar, "Basis-set extrapolation," Chem. Phys. Lett. 294(1), 45-48 (1998).

$^{42}$ A. Heßelmann and T. Korona, "Intermolecular symmetry-adapted perturbation theory study of large organic complexes," J. Chem. Phys. 141(9), 094107 (2014).

$^{43}$ R. A. Kendall, T. H. Dunning, and R. J. Harrison, "Electron affinities of the first-row atoms revisited. Systematic basis sets and wave functions," J. Chem. Phys. 96(9), 6796-6806 (1992).

$^{44}$ E. Papajak and D. G. Truhlar, "Convergent partially augmented basis sets for post-Hartree-Fock calculations of molecular properties and reaction barrier heights," J. Chem. Theory Comput. 7(1), 10-18 (2011).

$^{45}$ E. Papajak, J. Zheng, X. Xu, H. R. Leverentz, and D. G. Truhlar, "Perspectives on basis sets beautiful: Seasonal plantings of diffuse basis functions," J. Chem. Theory Comput. 7(10), 3027-3034 (2011).

$^{46}$ A. E. DePrince and C. D. Sherrill, "Accurate noncovalent interaction energies using truncated basis sets based on frozen natural orbitals," J. Chem. Theory Comput. 9(1), 293-299 (2013).

$^{47}$ C. Adamo and V. Barone, "Toward reliable density functional methods without adjustable parameters: The PBE0 model," J. Chem. Phys. 110, 6158-6170 (1999).

$^{48}$ N. Mardirossian and M. Head-Gordon, "Mapping the genome of meta-generalized gradient approximation density functionals: The search for B97M-V," J. Chem. Phys. 142, 074111 (2015).

$^{49}$ N. Mardirossian and M. Head-Gordon, "$\omega$B97M-V: A combinatorially optimized, range-separated hybrid, meta-GGA density functional with VV10 nonlocal correlation," J. Chem. Phys. 144, 214110 (2016).

$^{50}$ D. G. A. Smith, L. A. Burns, A. C. Simmonett, R. M. Parrish, M. C. Schieber, R. Galvelis, P. Kraus, H. Kruse, R. Di Remigio, A. Alenaizan, A. M. James, S. Lehtola, J. P. Misiewicz, M. Scheurer, R. A. Shaw, J. B. Schriber, Y. Xie, Z. L. Glick, D. A. Sirianni, J. S. O'Brien, J. M. Waldrop, A. Kumar, E. G. Hohenstein, B. P. Pritchard, B. R. Brooks, H. F. Schaefer, A. Y. Sokolov, K. Patkowski, A. E. DePrince, U. Bozkaya, R. A. King, F. A. Evangelista, J. M. Turney, T. D. Crawford, and C. D. Sherrill, "PSI4 1.4: Open-source software for high-throughput quantum chemistry," J. Chem. Phys. 152(18), 184108 (2020).

$^{51}$ F. Neese, F. Wennmohs, U. Becker, and C. Riplinger, "The ORCA quantum chemistry program package," J. Chem. Phys. 152(22), 224108 (2020).

$^{52}$ Y. Shao, Z. Gan, E. Epifanovsky, A. T. B. Gilbert, M. Wormit, J. Kussmann, A. W. Lange, A. Behn, J. Deng, X. Feng, D. Ghosh, M. Goldey, P. R. Horn, L. D. Jacobson, I. Kaliman, R. Z. Khaliullin, T. Kuś, A. Landau, J. Liu, E. I. Proynov, Y. M. Rhee, R. M. Richard, M. A. Rohrdanz, R. P. Steele, E. J. Sundstrom, H. L. Woodcock III, P. M. Zimmerman, D. Zuev, B. Albrecht, E. Alguire, B. Austin, G. J. O. Beran, Y. A. Bernard, E. Berquist, K. Brandhorst, K. B. Bravaya, S. T. Brown, D. Casanova, C.-M. Chang, Y. Chen, S. H. Chien, K. D. Closser, D. L. Crittenden, M. Diedenhofen, R. A. DiStasio Jr., H. Do, A. D. Dutoi, R. G. Edgar, S. Fatehi, L. Fusti-Molnar, A. Ghysels, A. Golubeva-Zadorozhnaya, J. Gomes, M. W. D. Hanson-Heine, P. H. P. Harbach, A. W. Hauser, E. G. Hohenstein, Z. C. Holden, T.-C. Jagau, H. Ji, B. Kaduk, K. Khistaev, J. Kim, J. Kim, R. A. King, P. Klunzinger, D. Kosenkov, W. Kowalczyk, C. M. Krauter, K. U. Lao, A. Laurent, K. V. Lawler, S. V. Levchenko, C. Y. Lin, F. Liu, E. Livshits, R. C. Lochan, A. Luenser, P. Manohar, S. F. Manzer, S.-P. Mao, N. Mardirossian, A. V. Marenich, S. A. Maurer, N. J. Mayhall, C. M. Oana, R. Olivares-Amaya, D. P. O'Neill, J. A. Parkhill, T. M. Perrine, R. Peverati, P. A. Pieniazek, A. Prociuk, D. R. Rehn, E. Rosta, N. J. Russ, N. Sergueev, S. M. Sharada, S. Sharma, D. W. Small, A. Sodt, T. Stein, D. Stück, Y.-C. Su, A. J. W. Thom, T. Tsuchimochi, L. Vogt, O. Vydrov, T. Wang, M. A. Watson, J. Wenzel, A. White, C. F. Williams, V. Vanovschi, S. Yeganeh, S. R. Yost, Z.-Q. You, I. Y. Zhang, X. Zhang, Y. Zhao, B. R. Brooks, G. K. L. Chan, D. M. Chipman, C. J. Cramer, W. A. Goddard III, M. S. Gordon, W. J. Hehre, A. Klamt, H. F. Schaefer III, M. W. Schmidt, C. D. Sherrill, D. G. Truhlar, A. Warshel, X. Xu, A. Aspuru-Guzik, R. Baer, A. T. Bell, N. A. Besley, J.-D. Chai, A. Dreuw, B. D. Dunietz, T. R. Furlani, S. R. Gwaltney, C.-P. Hsu, Y. Jung, J. Kong, M. S. Lambrecht, W. Liang, C. Ochsenfeld, V. A. Rassolov, L. V. Slipchenko, J. E. Subotnik, T. Van Voorhis, J. M. Herbert, A. I. Krylov, P. M. W. Gill, and M. Head-Gordon, "Advances in molecular quantum chemistry contained in the Q-Chem 4 program package," Mol. Phys. 113, 184-215 (2015).

$^{53}$ E. Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, and S. Grimme, "A generally applicable atomic-charge dependent London dispersion correction," J. Chem. Phys. 150(15), 154122 (2019).

$^{54}$ O. Marchetti and H.-J. Werner, "Accurate calculations of intermolecular interaction energies using explicitly correlated wave functions," Phys. Chem. Chem. Phys. 10, 3400-3409 (2008).

---

J. Chem. Phys. 154, 154104 (2021); doi: 10.1063/5.0042906

Published under license by AIP Publishing

154, 154104-11

$^{55}$M. S. Marshall, L. A. Burns, and C. D. Sherrill, "Basis set convergence of the coupled-cluster correction, $\delta_{\text{mp2}}^{\text{ccsd(t)}}$: Best practices for benchmarking non-covalent interactions and the attendant revision of the S22, NBC10, HBC6, and HSG databases," *J. Chem. Phys.* **135**(19), 194102 (2011).

$^{56}$J. Řezáč, K. E. Riley, and P. Hobza, "Benchmark calculations of noncovalent interactions of halogenated molecules," *J. Chem. Theory Comput.* **8**(11), 4285-4292 (2012).

$^{57}$G. H. Booth, A. Grüneis, G. Kresse, and A. Alavi, "Towards an exact description of electronic wavefunctions in real solids," *Nature* **493**(7432), 365-370 (2013).

$^{58}$K. Liao, X.-Z. Li, A. Alavi, and A. Grüneis, "A comparative study using state-of-the-art electronic structure theories on solid hydrogen phases under high pressures," *npj Comput. Mater.* **5**(1), 110 (2019).

$^{59}$T. Janowski and P. Pulay, "A benchmark comparison of $\sigma/\sigma$ and $\pi/\pi$ dispersion: The dimers of naphthalene and decalin, and coronene and perhydrocoronene," *J. Am. Chem. Soc.* **134**(42), 17520-17525 (2012).

$^{60}$A. Ambrosetti, D. Alfè, R. A. DiStasio Jr., and A. Tkatchenko, "Hard numbers for large molecules: Toward exact energetics for supramolecular systems," *J. Phys. Chem. Lett.* **5**(5), 849-855 (2014).

$^{61}$R. Sure and S. Grimme, "Comprehensive benchmark of association (free) energies of realistic host-guest complexes," *J. Chem. Theory Comput.* **11**(8), 3785-3801 (2015).

$^{62}$K. U. Lao and J. M. Herbert, "Atomic orbital implementation of extended symmetry-adapted perturbation theory (XSAPT) and benchmark calculations for large supramolecular complexes," *J. Chem. Theory Comput.* **14**(6), 2955-2978 (2018).

---

J. Chem. Phys. **154**, 154104 (2021); doi: 10.1063/5.0042906
Published under license by AIP Publishing

154, 154104-12