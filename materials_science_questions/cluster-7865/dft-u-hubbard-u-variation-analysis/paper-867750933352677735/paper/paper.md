# Calculating branching ratio and spin-orbit coupling from first-principles: A formalism and its application to iridates

Jae-Hoon Sim¹, Hongkee Yoon¹, Sang Hyeon Park¹, and Myung Joon Han¹,²*

¹Department of Physics, Korea Advanced Institute of Science and Technology (KAIST), Daejeon 305-701, Korea and
²KAIST Institute for the NanoCentury,
Korea Advanced Institute of Science and Technology, Daejeon 305-701, Korea

(Dated: November 7, 2018)

## Abstract

We present a simple technique to calculate spin-orbit coupling, $\langle\mathbf{L} \cdot \mathbf{S}\rangle$, and branching ratio measured in x-ray absorption spectroscopy. Our method is for first-principles electronic structure calculation and its implementation is straightforward for any of standard formulations and codes. We applied this technique to several different large spin-orbit coupling iridates. The calculated $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ and branching ratio of a prototype $j_{\text{eff}}$=1/2 Mott insulator, $\text{Sr}_2\text{IrO}_4$, are in good agreement with recent experimental data over the wide range of Rh-doping. Three different double perovskite iridates (namely, $\text{Sr}_2\text{MgIrO}_6$, $\text{Sr}_2\text{ScIrO}_6$, and $\text{Sr}_2\text{TiIrO}_6$) are also well described. This technique can serve as a promising tool for studying large spin-orbit coupling materials from first-principles and for understanding experiments.

PACS numbers: 75.70.Cn, 75.47.Lx, 71.15.Mb, 78.70.Dm

### I. INTRODUCTION

Recently the role of spin-orbit coupling (SOC) in solids has attracted tremendous attention. In many cases, SOC drastically changes the electronic band structure and results in a fundamentally different material property. A class of materials, called topological insulators, is an outstanding example¹·². SOC can also play together with on-site electronic correlation, $U$, as often found in $5d$ transition-metal oxides. In iridates, for example, the cooperation of SOC and $U$ drives materials to be a novel '$j_{\mathrm{eff}}$=$1/2$ Mott insulator'³·⁴. Due to the characteristic hopping integrals caused by $j_{\mathrm{eff}}$=$1/2$ nature (instead of $S$=$1/2$), some interesting new possibilities have been proposed and still under active investigations⁵⁻⁸. The basically same features can also be found in the non-oxide $4d$ and $5d$ transition-metal compounds⁹.

The spin-orbit Hamiltonian is represented by $\lambda \langle \mathbf{L} \cdot \mathbf{S} \rangle$. While $\lambda$ is known from the atomic nature of a given species, the direct estimation of $\lambda \langle \mathbf{L} \cdot \mathbf{S} \rangle$ is not always straightforward from experiment nor by theoretical calculation. For topological insulators, the observed band structure (e.g., by angle-resolved photoemission spectroscopy (ARPES)) is regarded as a strong evidence of the characteristic band dispersion caused by SOC¹·². For iridates, the data from resonant x-ray magnetic scattering (RXMS) and/or resonant inelastic x-ray scattering (RIXS) have been accepted as a confirmation of the novel SOC physics because the interpretation of the data seems consistent only with theoretical models that take strong SOC into account⁴·¹⁰. However it is noted that sometimes a different interpretation can be made and then the conclusion might be changed (for an example of iridates, see Ref.¹¹). Further, from the theoretical point of view, it is unsatisfactory that there is no simple and well-defined way to directly calculate SOC strength and to compare with experiments. In the standard first-principles calculations, $\lambda$ can be calculated when the atomic wavefunctions are constructed by solving the relativistic Dirac equation. $\langle \mathbf{L} \cdot \mathbf{S} \rangle$, however, is not just determined by atomic nature but depends on the electronic structure of solids.

In this paper, we point out that the calculation of $\langle \mathbf{L} \cdot \mathbf{S} \rangle$ can be performed in a simple and straightforward way within the standard first-principles framework and be directly compared with experiment. One possible reason that the calculation of $\langle \mathbf{L} \cdot \mathbf{S} \rangle$ has not been often made from first-principles may be partly because of no direct reference data available from the experimental side. We note that the branching ratio, typically measured in x-ray absorption spectroscopy (XAS), can be used to estimate the strength of SOC. Instead of calculating

XAS spectrum itself, a simple technique can be used to directly calculate branching ratio through $\langle\mathbf{L} \cdot \mathbf{S}\rangle$. Our formalism is implemented into our localized pseudo-atomic orbital (PAO) basis code and applied to several different iridium oxide compounds. For a $j_{\text{eff}}$=1/2 system, $\text{Sr}_2\text{IrO}_4$ (see Fig. 1(a)), we considered Rh doping (namely, $\text{Sr}_2\text{Rh}_x\text{Ir}_{1-x}\text{O}_4$) and found that the calculated SOC and branching ratio are in good agreement with XAS data over the wide range of doping ratio $x$. The iridate double perovskites (see Fig. 1(b)), $\text{Sr}_2\text{XIrO}_6$ ($X$: Mg, Sc, Ti), are also calculated and the results are in good agreement with recent experiments. We emphasize the formalism and implementation are simple enough to be adoptable for any type of first-principles code and method. This technique can be a useful tool for study large SOC materials by providing a direct estimation of $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ and branching ratio.

## II. COMPUTATION METHOD

### A. Calculation details

For the electronic structure calculations, we used OpenMX software package$^{12-14}$ which is based on the linear combination of numerical PAO and norm-conserving pseudopotential$^{14}$. The cutoff radii for Sr, Ir, Rh, Mg, Sc, Ti, and O are 10.0, 7.0, 7.0, 7.0, 7.0, 7.0, and 5.0 a.u. respectively. The Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional$^{15}$ and 300 Ry energy cutoff. $5\times5\times2$ and $9\times9\times7$ k-meshes were taken for Rh-doped $\text{Sr}_2\text{IrO}_4$ and double perovskites, respectively. have been used. The SOC was treated within a fully relativistic $j$-dependent pseudopotential scheme in the non-collinear methodology$^{12}$. The on-site electronic correlations were taken into account within DFT+$U$ formalism$^{16,17}$. The reasonable value of $U$ may be about 2.0 – 3.0 $eV$ as noticed by the previous studies on $\text{Sr}_2\text{IrO}_4$ and $\text{Ba}_2\text{IrO}_4$$^{3,18-20}$. Throughout the manuscript, we present $U_{\text{eff}} \equiv U-J=2.0$ eV results as our main data both for Rh-doped $\text{Sr}_2\text{IrO}_4$ and double perovskites. After scanning the region of $U_{\text{eff}}=2.0-3.0$ eV, we found that any of our conclusion does not change by choosing different $U$ values. For Rh-doped iridates, the lattice constant and internal coordinates are optimized with the force criteria of $0.01$ eV/Å. For double perovskites, we used the experimental lattice parameters$^{21,22}$ of $a=3.958\text{Å}$ ($\text{Sr}_2\text{MgIrO}_6$), $4.007\text{Å}$ ($\text{Sr}_2\text{ScIrO}_6$) and $3.927\text{Å}$ ($\text{Sr}_2\text{TiIrO}_6$).

### B. Formalism

In this section, we present our formalism to calculate $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ and branching ratio from first-principles. The localized atomic orbitals are assumed to be the basis set in the below. However, it is straightforward to extend our method to any other type. We used our pseudopotential-based DFT (density functional theory) package, OpenMX$^{12}$, which takes the linear combination of numerical PAO basis$^{13,14}$. The single particle energy eigenstate is decomposed into PAO; $|\psi_{n\mathbf{k}}\rangle = \sum_{i,\alpha} c_{\alpha,i}^{n,\mathbf{k}} |\phi_{\alpha,i}\rangle$ where $|\psi_{n\mathbf{k}}\rangle$ is Khon-Sham eigenstate with momentum $\mathbf{k}$, $n$ the band index, and $|\phi_{\alpha,i}\rangle$ is PAO with orbital index $\alpha$ at position $R_i$. With $J = |\mathbf{L} + \mathbf{S}| = 5/2, 3/2$ state as a basis set for a given Ir-$5d$ orbitals,

$$
|\psi_{n\mathbf{k}}\rangle = \sum_{m_J=-5/2}^{5/2} a_{m_J}^{n\mathbf{k}} |J=5/2, m_J\rangle_{\text{Ir}} + \sum_{m_J=-3/2}^{3/2} b_{m_J}^{n\mathbf{k}} |J=3/2, m_J\rangle_{\text{Ir}} + \sum_{(i,\alpha)\neq(\text{Ir},d)} c_{\alpha,i}^{n\mathbf{k}} |\phi_{\alpha,i}\rangle. \tag{1}
$$

Now the expectation value of $\mathbf{L} \cdot \mathbf{S}$ is estimated within this basis as follow:

$$
\begin{aligned}
\langle\mathbf{L} \cdot \mathbf{S}\rangle &= \sum_{n\mathbf{k}}^{\text{occ}} \langle\psi_{n\mathbf{k}}| \mathbf{L} \cdot \mathbf{S} |\psi_{n\mathbf{k}}\rangle \\
&= \sum_{\epsilon_{n\mathbf{k}}<\epsilon_F} \sum_{m_J} (1.0 \times |a_{m_J}^{n\mathbf{k}}|^2 - 1.5 \times |b_{m_J}^{n\mathbf{k}}|^2),
\end{aligned} \tag{2}
$$

where 1.0 and 1.5 are the eigenvalue of the $\mathbf{L} \cdot \mathbf{S}$ operator for $J=5/2$ and $3/2$, respectively.

Note that it is crucial to use the $J$ state as a basis and the $j_{\text{eff}}$ is not suitable although it is often adapted to describe the low energy electronic structure of iridates. Fig. 1(c) shows the calculated $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ as a function of crystal field splitting $10Dq$ with the basis set of total angular momentum $J$ eigenstates (blue) and $j_{\text{eff}}$ states (red). For a reasonable value of $10Dq \approx 1.8$eV for the iridates$^{23}$, the two lines differ significantly due to the coupling between $t_{2g}$ and $e_g$ states. It is noted that, even in a large $10Dq$ limit, $\langle\mathbf{L} \cdot \mathbf{S}\rangle_J$ and $\langle\mathbf{L} \cdot \mathbf{S}\rangle_{j_{\text{eff}}}$ can noticeably differ from each other. Here $\langle\mathbf{L} \cdot \mathbf{S}\rangle_J$ is the same quantity with $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ in Eq.(2), and $\langle\mathbf{L} \cdot \mathbf{S}\rangle_{j_{\text{eff}}}$ is obtained from only $t_{2g}$ space taken into account.

The 'line strength' $L_j$ can be expressed as the expectation value of an operator

$$
\hat{P}_j \equiv \sum_{\lambda,q} \hat{D}_q |\lambda j\rangle \langle\lambda j| \hat{D}_q, \tag{3}
$$

where $D_q$ is the dipole operator with polarization $q$, $j$ is the total angular momentum of the core hole, and $\lambda$ denotes all quantum numbers other than $j$. The sum is taken over the $q=-1,0,1$ for the isotropic 'line strength' considered.


Branching ratio can also be estimated without calculating the full XAS spectra. We first note that the relative intensity of $L_3$ and $L_2$ edge 'white lines' can be related to the spin-orbit coupling via

$$
\frac{L_{j}}{L_{3}+L_{2}}=\frac{2 j+1}{2\left(2 l_{c}+1\right)} \pm A\left(l_{c}, l_{v}, n_{h}\right)\langle\mathbf{L} \cdot \mathbf{S}\rangle,
\tag{4}
$$

where $l_v$, $l_c$, and $j=l_c\pm1/2$ refers to the orbital angular momentum of valence electron, the orbital angular momentum of core hole, and the total angular momentum of the core hole, respectively$^{24,25}$. The number of holes in valence orbitals is denoted by $n_h$. In our case,

$$
A\left(l_{c}, l_{v}, n_{h}\right)=\frac{2-l_{v}\left(l_{v}+1\right)-l_{c}\left(l_{c}+1\right)}{l_{v}\left(l_{v}+1\right)\left(2 l_{c}+1\right)\left(n_{h}\right)}=-\frac{1}{3 n_{h}}.
\tag{5}
$$

This relation is expected to be exact for the dipole transition in which the core-hole interaction with the valence electrons is small enough in comparison to the spin-orbit interaction of the core hole. Therefore our case of iridates is suitable for this formalism to be applied. From Eq.(4), the branching ratio can be written as

$$
I_{L_{3}} / I_{L_{2}}=\frac{2 n_{h}-\langle\mathbf{L} \cdot \mathbf{S}\rangle}{n_{h}+\langle\mathbf{L} \cdot \mathbf{S}\rangle}=\frac{2-r}{1+r}
\tag{6}
$$

with $r=\langle\mathbf{L} \cdot \mathbf{S}\rangle / n_{h}$. Therefore the branching ratio can be estimated by calculating the number of holes (which is straightforward in the electronic structure calculation) and $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ (which can also be estimated as described above).

Due to recent progress, calculating XAS spectra from first-principles becomes feasible. Some codes are already available for this capability$^{26,27}$. However the calculation of the whole spectra is quite demanding in general. For example, a certain type of pseudopotential (such as projector augmented wave) should be prepared for describing the core holes. Also, the generalization to the non-collinear spin configuration space is sometimes not well prepared while the non-collinear spin order is actually stabilized in many of large SOC materials as in the case of $\text{Sr}_2\text{IrO}_4$. Our technique has a clear advantage in these regards. First of all, it is much simpler in the implementation and calculation, and does not require any special type of pseudopotential. One can just use the original code as it is and the only required information is the final band structure that is properly transformed into $J$-space. In spite of its simplicity, the quantitative comparison can still be made with experiment through the branching ratio, and the direct estimation of SOC is also provided although the full XAS spectra is not accessible.

## III. RESULT AND DISCUSSION: APPLICATION TO IRIDATES

### A. Rhodium-doped $Sr_2IrO_4$

The calculation results of Rh-doped iridates, $Sr_2Rh_xIr_{1-x}O_4$, are summarized in Fig. 2 (see the filled blue squares; corresponding to the upper $x$-axis) where XAS data is also presented (open blue squares).The good agreement between calculation and experiment is clearly noticed over the wide range of Rh-doping ratio, $x$. Note that the error can be caused in both theoretical and experimental estimation as marked by the error bars. In calculations, the one important source of error is the range of integration; namely, how to deal with the small portion of Ir-$5d$ states hybridized with oxygen states while the major Ir peaks are clearly identified. According to our estimation, this intrinsic ambiguity can cause the deviation of branching ratio by up to $\pm0.25$ which is $\lesssim5\%$. Counting the number of holes (or electrons) in Ir-$5d$ orbitals is another source of errors. This is related to the long-standing issue of charge decomposition in the electronic structure calculation, and the number of holes depends on the electron counting method. In this study, we used the standard Mulliken charge analysis. For experimental data, we simply take the error limits presented in Ref.$^{28,29}$.

Note that the $\langle\mathbf{L}\cdot\mathbf{S}\rangle$ and branching ratio are basically unchanged over the wide range of $x$, and clearly larger than the Rh value of $\sim0.8$ and $\sim3$, respectively$^{29}$. This result is therefore in contrast to the previously suggested picture of 'SOC tuning' in which Rh-doping is assumed to reduce the SOC strength of Ir sites$^{30,31}$. It is one example to show the importance of calculating SOC from the realistic electronic structure.

### B. Iridium oxide double perovskites

Another system we take to test our method is iridate double perovskites, $Sr_2XIrO_6$ ($X$: Mg, Sc, Ti). This series of materials are studied recently with XAS$^{29}$ while no theoretical investigation has been reported yet. Among many different double perovskite iridates, we chose $X=$ Mg, Sc, and Ti in which $X$ has $d^0$ configuration, and therefore we could avoid the additional ambiguity in determining $U$ values for $X$ sites. The nominal Ir valence in these compounds are $6+$, $5+$, and $4+$ for $Sr_2MgIrO_6$, $Sr_2ScIrO_6$, $Sr_2TiIrO_6$, respectively, serving

as a good test case to check the reliability of our method.

The calculation results of projected density of states (PDOS) is presented in Fig. 3. The so-called effective total angular momentum $j_{\text{eff}}$-character is well identified ($j_{\text{eff}}$=1/2 and 3/2 is in red and blue color, respectively). The gradual increase of Ir-$5d$ band filling is clearly observed as we go from Mg ($\frac{3}{4}$-filled $j_{\text{eff}}$=3/2) to Sc (fully-filled $j_{\text{eff}}$=3/2) and to Ti (half-filled $j_{\text{eff}}$=1/2). The Ti case has the same nominal valence with $\text{Sr}_2\text{IrO}_4$. Among these three compounds, $\text{Sr}_2\text{MgIrO}_6$ is reported first by Jung and Demazeau$^{22}$ and its semiconducting behavior in the transport$^{22}$ and antiferromagnetic ordering below $T_N=74\text{K}^{21}$ are consistent with our results.

The results of $\langle \mathbf{L} \cdot \mathbf{S} \rangle$ and branching ratio are summarized in Fig. 2(a) and (b), respectively (see the magenta diamond symbols corresponding to the lower axis). Again, the overall good agreement with XAS data is clearly noticed. Here we also note several possible sources of deviation, when compared to the experiments, such as the material dependent $U$ values, long PDOS tails due to the hybridization, and the electron number counting with the Mulliken analysis. Considering the uncertainties related to all of these factors, the agreement within the error bar is quite impressive. According to the previous studies$^{21,22}$, it is noted that the amount of oxygen vacancy is likely non-negligible especially for $X$=Mg sample ($\text{Sr}_2\text{MgIrO}_{6-\delta}$: $\delta \sim 0.35$ at 1 bar). It is another factor that can cause the difference between experiment and calculation. In fact, the difference is distinguishable (considering the error bars) only in the $X$=Mg case. In order to see the effect of oxygen vacancy, we performed the rigid-band shift ($\delta$= 0, 0.1, 0.2, 0.3, 0.4) and the supercell calculation ($\delta$=0.4). In the former, it is assumed that the role of vacancy is just electron doping. The results are summarized as the insets of Fig. 4. An excellent agreement with experiments for both $\langle \mathbf{L} \cdot \mathbf{S} \rangle$ and branching ratio is clearly noticed.

While our main results are obtained from 20-atom unitcells with antiferromagnetic order, we also performed the 10-atom cell calculations which correspond to ferromagnetic order. The calculated SOC and branching ratio are not noticeably different. It indicates that the effect of magnetic order and structural distortion is not significant. It is also found that the $U$ dependence is not significant in the range we considered.

## IV. SUMMARY

We introduce a technique to calculate SOC and branching ratio. It is simple enough to be adoptable basically for any type of first-principles calculation methods and formalisms. Large SOC iridates were taken to be a test case for this method. The calculation results of Rh-doped $Sr_2IrO_4$ and double perovskites, $Sr_2XIrO_6$, are shown to be in good agreement with recent XAS experiments. This technique can serve as a new promising tool for studying large SOC materials from first-principles and for understanding related experiments.

## V. ACKNOWLEDGEMENTS

MJH is greatly thankful to Michel van Veenendaal for helpful discussion. This work was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Education (2014R1A1A2057202). The computing resource is supported by National Institute of Supercomputing and Networking / Korea Institute of Science and Technology Information with supercomputing resources including technical support (KSC-2014-C2-015).

* mj.han@kaist.ac.kr

1 M. Z. Hasan and C. L. Kane, Rev. Mod. Phys. **82**, 3045 (2010).

2 X.-L. Qi and S.-C. Zhang, Rev. Mod. Phys. **83**, 1057 (2011).

3 B. J. Kim, H. Jin, S. J. Moon, J.-Y. Kim, B.-G. Park, C. S. Leem, J. Yu, T. W. Noh, C. Kim,
S.-J. Oh, J.-H. Park, V. Durairaj, G. Cao, and E. Rotenberg, Phys. Rev. Lett. **101** (2008).

4 B. J. Kim, H. Ohsumi, T. Komesu, S. Sakai, T. Morita, H. Takagi, and T. Arima, Science **323**,
1329 (2009).

5 A. Shitade, H. Katsura, J. Kune, X.-L. Qi, S.-C. Zhang, and N. Nagaosa, Phys. Rev. Lett.
**102**, 256403 (2009).

6 D. Pesin and L. Balents, Nat. Phys. **6**, 376 (2010).

7 G. Jackeli and G. Khaliullin, Phys. Rev. Lett. **102**, 017205 (2009).

8 F. Wang and T. Senthil, Phys. Rev. Lett. **106**, 136402 (2011).

9 H.-S. Kim, J. Im, M. J. Han, and H. Jin, Nat. Commun. **5**, 3988 (2014).

10 J. Kim, D. Casa, M. H. Upton, T. Gog, Y.-J. Kim, J. F. Mitchell, M. van Veenendaal,
M. Daghofer, J. van den Brink, G. Khaliullin, and B. J. Kim, Phys. Rev. Lett. 108, 177003
(2012).

11 M. Moretti Sala, S. Boseggia, D. F. McMorrow, and G. Monaco, Phys. Rev. Lett. 112, 026403
(2014).

12 "OpenMX," http://www.openmx-square.org/.

13 T. Ozaki and H. Kino, Phys. Rev. B 69, 195113 (2004).

14 T. Ozaki, Phys. Rev. B 67, 155108 (2003).

15 J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

16 S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev.
B 57, 1505 (1998).

17 M. J. Han, T. Ozaki, and J. Yu, Phys. Rev. B 73, 045110 (2006).

18 H. Zhang, K. Haule, and D. Vanderbilt, Phys. Rev. Lett. 111, 246402 (2013).

19 C. Martins, M. Aichhorn, L. Vaugier, and S. Biermann, Phys. Rev. Lett. 107, 266404 (2011).

20 R. Arita, J. Kune, A. V. Kozhevnikov, A. G. Eguiluz, and M. Imada, Phys. Rev. Lett. 108,
086403 (2012).

21 P. Kayser, M. J. Martnez-Lope, J. A. Alonso, M. Retuerto, M. Croft, A. Ignatov, and M. T.
Fernndez-Daz, Eur. J. Inorg. Chem. 2014, 178 (2014).

22 D.-Y. Jung and G. Demazeau, J. Solid State Chem. 115, 447 (1995).

23 D. Haskel, G. Fabbris, M. Zhernenkov, P. P. Kong, C. Q. Jin, G. Cao, and M. van Veenendaal,
Phys. Rev. Lett. 109, 027204 (2012).

24 G. Van der Laan and B. T. Thole, Phys. Rev. Lett. 60, 1977 (1988).

25 B. T. Thole and G. Van der Laan, Physical Review A 38, 1943 (1988).

26 P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L.
Chiarotti, M. Cococcioni, I. Dabo, and others, J. Phys.: Condens. Matter 21, 395502 (2009).

27 L. Pardini, V. Bellini, F. Manghi, and C. Ambrosch-Draxl, Comput. Phys. Commun. 183, 628
(2012).

28 M. A. Laguna-Marco, P. Kayser, J. A. Alonso, M. J. Martnez-Lope, M. van Veenendaal, Y. Choi,
and D. Haskel, Phys. Rev. B 91 (2015).

29 S. Chikara, D. Haskel, J.-H. Sim, H.-S. Kim, C.-C. Chen, G. Fabbris, L. S. I. Veiga, N. M.
Souza-Neto, J. Terzic, K. Butrouna, G. Cao, M. J. Han, and M. van Veenendaal, Phys. Rev.

B 92 (2015).

30 J. S. Lee, Y. Krockenberger, K. S. Takahashi, M. Kawasaki, and Y. Tokura, Phys. Rev. B 85, 035101 (2012).

31 T. F. Qi, O. B. Korneta, L. Li, K. Butrouna, V. S. Cao, X. Wan, P. Schlottmann, R. K. Kaul, and G. Cao, Phys. Rev. B 86, 125105 (2012).

![](./images/867750933352677735_1.jpg)

FIG. 1. The unitcell structure of (a) ${\rm Sr_2IrO_4}$ and (b) double perovskite. The green, light blue, light brown, and red spheres represent Sr, $X$, Ir and O, respectively ($X = {\rm Mg,\ Sc,\ Ti}$). The $XO_6$ and $IrO_6$ cage is shaded in blue and brown, respectively. (c) The expectation value of spin-orbit coupling calculated in the $d^5$ atomic limit as a function of $10Dq$. The blue ($\langle {\bf L} \cdot {\bf S} \rangle_J$) and red ($\langle {\bf L} \cdot {\bf S} \rangle_{j_{\rm eff}}$) line corresponds to the result obtained by using both $t_{2g}$ and $e_g$ orbitals and only $t_{2g}$ orbitals, respectively.

![](./images/867750933352677735_2.jpg)

FIG. 2. The calculated values (filled or half-filled symbols) of (a) $\langle\mathbf{L} \cdot \mathbf{S}\rangle$ and (b) branching ratio in comparison with experiments (open symbols). The upper (corresponding to the dark blue symbols) and lower axis (magenta symbols) refers to $\mathrm{Sr}_{2} \mathrm{Rh}_{x} \mathrm{Ir}_{1-x} \mathrm{O}_{4}$ and $\mathrm{Sr}_{2} X \mathrm{IrO}_{6}$ ($X = \mathrm{Mg}$, $\mathrm{Sc}$, $\mathrm{Ti}$), respectively. The error bars for experimental data are taken from the original papers. The error bars in the calculation results reflect the ambiguity related to the numerical parameters and other computation details (see the main text for more details). Inset: The effect of oxygen vacancy has been simulated for $\mathrm{Sr}_{2} \mathrm{MgIrO}_{6-\delta}$. The horizontal dashed lines refer to the experimental values. The filled (blue) symbols represent the result of rigid band shift and the half-filled (magenta) symbols are the result of the supercell calculation with oxygen removal

![](./images/867750933352677735_3.jpg)

FIG. 3. The calculated PDOS for (a) ${\rm Sr_2MgIrO_6}$, (b) ${\rm Sr_2ScIrO_6}$ and (c) ${\rm Sr_2TiIrO_6}$, corresponding to Ir valence of $6+$, $5+$, and $4+$, respectively. The blue and red lines represent $j_{\rm eff}$=$3/2$ and $1/2$ states, respectively.