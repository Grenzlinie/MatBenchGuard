![](./images/812393806866415616_1.jpg)

Optical properties of CdSe quantum dots

M. Claudia Troparevsky, Leeor Kronik, and James R. Chelikowsky

Citation: *The Journal of Chemical Physics* **119**, 2284 (2003); doi: 10.1063/1.1585013

View online: http://dx.doi.org/10.1063/1.1585013

View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/119/4?ver=pdfcov

Published by the AIP Publishing

![](./images/812393806866415616_2.jpg)

# Optical properties of CdSe quantum dots

M. Claudia Troparevsky, $^{a)}$ Leeor Kronik, $^{b)}$ and James R. Chelikowsky $^{c)}$

Department of Chemical Engineering and Materials Science, Minnesota Supercomputing Institute,
University of Minnesota, Minneapolis, Minnesota 55455

(Received 1 April 2003; accepted 1 May 2003)

Ab initio absorption spectra and optical gaps for $\text{Cd}_n\text{Se}_n$ ($n=17,26,38$) quantum dots are calculated using time-dependent density functional theory within the local density approximation. The spectra computed using the time-dependent local density approximation technique differ from the ones calculated using conventional approaches in both absorption threshold and spectral features. The time-dependent density functional spectra suppress surface contributions in the lower-energy region of the spectra. These contributions come from the Se atoms at the surface with two dangling bonds. The optical gaps calculated using the time-dependent approach are in good agreement with experimental results. © 2003 American Institute of Physics. [DOI: 10.1063/1.1585013]

Semiconductor quantum dots have received considerable attention owing to their unusual electronic and optical properties. $^{1-7}$ These properties can be radically altered, while maintaining the chemical composition of the material, by simply changing the number of atoms in the quantum dot. In particular, much work has been devoted to the study of the optical onset in colloidally prepared II–VI semiconductors. $^{8-10}$ The size of such quantum dots can be used to tune the optical gap across a major portion of the visible spectrum. For example, in the case of CdSe, the optical gap can be tuned from deep red (1.7 eV) to green (2.4 eV) by reducing the dot diameter from 20 to 2 nm. $^{8,9}$ The ability to use "size" as a variable in tailoring the desired properties of the system, have made quantum dots promising materials for the development of new electronic and optical devices such as light emitting diodes $^{8}$ and solar cells. $^{11}$

One way of synthesizing quantum dots is allowing molecular or ionic precursors to react together in solution forming the dots as colloids. CdSe and CdS have been two of the most studied II–VI dots due to the availability of precursors, the ease of their crystallization, and the fact that their optical gap can be in the visible range. CdX (X=S,Se) quantum dots can be synthesized by mixing $\text{Cd(CH}_3\text{)}_2$ with a chalcogenide reagent in a coordinating solvent. A solvent commonly used is a mixture of TOP and TOPO (trioctyl phosphine and trioctyl phosphine oxide), which acts as a surfactant. $^{9}$ This method leads to highly monodisperse quantum dots passivated with TOP/TOPO. These quantum dots can be also terminated with other capping agents such as thiolates, pyridine, or selenophenols. $^{12-14}$

Several empirical and semiempirical theoretical studies of CdX quantum dots have been reported. $^{15,16}$ Wang and Zunger, $^{15}$ and later Rabani et al. $^{16}$ calculated optical gaps of CdSe quantum dots using an empirical pseudopotential method. The results obtained by these authors compare well with experiment. In their work, they use a ligand potential model $^{15}$ in order to simulate the surface passivation. This model places a short range electrostatic potential near the surface atoms. The potentials are taken to be Gaussians that are placed in the direction of the missing atom. However, the choice of the magnitude of the potential, the width of the Gaussian, as well as the distance from the center of the Gaussian to the surface atom, can greatly change the values of the calculated optical gaps.

Theoretical calculations of the optical spectra for semiconductor quantum dots are of particular importance since they can be directly compared with experiment. Because it is difficult to apply bulk parameterization to small quantum dots, it is desirable to use ab initio techniques. However, this involves the calculation of excited state properties, which presents enormous challenges for theoretical methods. Typical methods employed to calculate excited state properties include the configuration-interaction method, $^{17}$ quantum Monte Carlo methods, $^{18}$ or the solution of the Bethe–Salpeter equation for the two-particle Green's function. $^{19}$ However, these methods are computationally intensive and usually limited to small molecules and clusters.

A different approach is based on linear response theory within the time-dependent density functional formalism and the local density approximation (TDLDA). Formally an exact approach, in practice it is approximate owing to the use of the local density approximation (LDA) instead of the exact spatial dependence, and an adiabatic approximation instead of the exact time dependence. $^{20}$ Compared to other methods for excited states, the TDLDA technique requires a substantially smaller computational effort and is able to handle a much large number of atoms. This technique has been successfully applied to numerous localized systems, including small molecules, clusters, and quantum dots. $^{21,22}$

A detailed analysis of TDLDA theory has been given elsewhere. $^{20}$ We apply it within a frequency–space approach, in which the electronic transition energies $\Omega_n$ are obtained from the solution of the following eigenvalue problem: $^{20}$

$^{a)}$Present address: Department of Chemistry and Henry Eyring Center for Theoretical Chemistry, University of Utah, Salt Lake City, Utah 84112-0850.
$^{b)}$Present address: Department of Materials and Interfaces, Weizmann Institute of Science, Rehovoth 76100, Israel.
$^{c)}$Electronic mail: jrc@msi.umn.edu

$$\mathbf{Q F}_{n}=\Omega_{n}^{2} \mathbf{F}_{n}, \tag{1}$$
where
$$
\begin{aligned}
Q_{i j \sigma, k l \tau}= & {\left[\omega_{i j \sigma}^{2} \delta_{i k} \delta_{j l} \delta_{\sigma \tau}\right.} \\
& \left.+2 \sqrt{f_{i j \sigma} \omega_{i j \sigma}} K_{i j \sigma, k l \tau} \sqrt{f_{k l \tau} \omega_{k l \tau}}\right],
\end{aligned}
$$
$\omega_{i j \sigma}=\epsilon_{j \sigma}-\epsilon_{i \sigma}$ are the Kohn-Sham transition energies, and $f_{i j \sigma}=n_{i \sigma}-n_{j \sigma}$ are the differences between the occupation numbers of the $i$ th and $j$ th states, with the spin indice being $\sigma$. We use atomic units (a.u.), where $\hbar=m=e=1$. The eigenvectors $\mathbf{F}_{n}$ are related to the oscillator strength, and $K_{i j \sigma, k l \tau}$ is a coupling matrix given by
$$
\begin{aligned}
K_{i j \sigma, k l \tau}= & \iint \phi_{i \sigma}^{*}(\mathbf{r}) \phi_{j \sigma}(\mathbf{r})\left(\frac{1}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}+\frac{\delta v^{\mathrm{xc}}(\mathbf{r})}{\delta \rho_{\tau}\left(\mathbf{r}^{\prime}\right)}\right) \\
& \times \phi_{k \tau}\left(\mathbf{r}^{\prime}\right) \phi_{l \tau}^{*}\left(\mathbf{r}^{\prime}\right) d \mathbf{r} d \mathbf{r}^{\prime}, \tag{2}
\end{aligned}
$$
where $\phi(\mathbf{r})$ is a Kohn-Sham wave function, $i, j, \sigma$ (as well as $k, l, \tau$ ), are the occupied state, unoccupied state, and spin indices, respectively, $\rho(\mathbf{r})$ is the Kohn-Sham charge density, and $v^{\mathrm{xc}}(\mathbf{r})$ is the LDA exchange correlation.

The TDLDA calculations were performed using the higher-order finite difference pseudopotential method in real space. $^{23}$ We employed Troullier-Martins pseudopotentials $^{24}$ with a partial core correction, $^{25}$ and the local density approximation of Ceperley and Alder. $^{26,27}$ The radial cutoff parameters for the $s, p$, and $d$ components of the pseudopotentials were taken to be 2.6, 2.6, and 3.8 a.u. for Cd and 2.6,2.4, and 3.17 for Se.

The solution proceeds as follows: First, the timeindependent single-electron Kohn-Sham transition energies and wave functions are found. Then, the wave functions are used to construct the coupling matrix of Eq. (2). Finally, the TDLDA eigenvalue equation, Eq. (1), is solved and the absorption spectrum is constructed. All steps were performed using a real-space grid confined in a spherical domain. We carefully tested for convergence of the absorption spectra with respect to the size of the spherical domain, the grid spacing, and the total number of electronic states. The sphere was such that the outermost atom of the dot was at least 14 a.u. from the boundary. The grid spacing was 0.7 a.u., and the number of unoccupied states included in the calculations was more than two times greater than the number of occupied states.

We note two previous studies using $ab$ initio methods applied to CdSe quantum dots. One is by Deglmann et al. $^{29}$ In this work, they calculated the optical gaps for CdSe quantum dots using a time-dependent density functional formalism. The structures of the CdSe quantum dots were optimized with symmetry restrictions. The final structures of the quantum dots calculated using this method do not have the bulk structure. In fact, the resulting structures are strongly distorted from that of the bulk crystal, and the bond lengths are significantly larger. This is in disagreement with experimental findings. $^{9}$ Their calculated optical gaps differ from those obtained experimentally. For most of the dots they studied, the value of the optical gap is already smaller than that of the bulk phase, even for the smaller dots. Another study has been performed by Eichkorn and Ahlrichs. $^{30}$ In this work, quantum dots were modeled using ligand stabilized clusters of CdSe. A few low lying excitations were determined using TDLDA. However, the dots examined were not stoichiometric.

![](./images/812393806866415616_3.jpg)

FIG. 1. Structures of $\mathrm{Cd}_{17} \mathrm{Se}_{17}, \mathrm{Cd}_{26} \mathrm{Se}_{26}$, and $\mathrm{Cd}_{38} \mathrm{Se}_{38}$ wurtzite dots.

In this work, we perform calculations for the optical absorption spectra and optical gaps of $\mathrm{Cd}_{n} \mathrm{Se}_{n}$ quantum dots $(n=17,26,38)$. The dots studied are spherical fragments of the wurtzite crystal. These particular dots were picked because none of the surface atoms possess three dangling bonds. We chose the quantum dots employed in our work to be ligand free. The role of passivating agents such as TOPO/ TOP is to "gently" terminate the dot without altering the bulk structure. $^{9}$ Another role of capping agents is to passivate dangling bonds. Owing to the large number of atoms of the capping agents and uncertainty as to the local geometry of the TOPO/TOP-quantum dot interface, it is not feasible to model this system directly. Instead, we considered a bare dot, where the surface atoms were fixed to replicate the bulk geometry. This procedure has a number of advantages. From a computational point of view, it is not necessary to extract eigenvalues of species that are expected to be electronically inert. Moreover, it removes uncertainties associated with variant capping species.

Figure 1 shows the structures of the quantum dots studied in this work. Figure 2 shows the TDLDA computed spectra, and the time-independent LDA spectra of $\mathrm{Cd}_{17} \mathrm{Se}_{17}$, $\mathrm{Cd}_{26} \mathrm{Se}_{26}$, and $\mathrm{Cd}_{38} \mathrm{Se}_{38}$, respectively. All spectra were broadened using a Gaussian with an 0.1 eV width, in order to simulate finite temperature and lifetime effects. It can be observed that the TDLDA spectra display a blue shift with respect to the LDA spectra. This behavior was also observed in the spectra of small CdSe clusters. $^{31}$ We found that the main contribution to low lying excitations comes from Se

![](./images/812393806866415616_4.jpg)

FIG. 2. Calculated TDLDA (solid lines) and LDA (dashed lines) spectra of Cd₁₇Se₁₇, Cd₂₆Se₂₆, and Cd₃₈Se₃₈.

atoms at the surface with two dangling bonds. It can also be observed that in the low-energy region the LDA spectra present much larger oscillator strengths than that of the TDLDA computed spectra.

It is not straightforward to define an optical gap, especially for quantum dots, where the threshold may not be distinct. The absorption spectra of the studied quantum dots present a large number of weak transitions near the absorption edge. This is a disadvantage in using a bare cluster to model a quantum dot, i.e., the dangling bond states have not been explicitly removed by a passivating agent. However, we can construct a well-defined procedure to extract the gap. We take the absorption edge as the energy threshold below which the absorption is 2% of the total absorption:

$$
\int_{0}^{E_{\text{gap}}} \sigma(\omega) d \omega=0.02 F. \tag{3}
$$

$E_{\text{gap}}$ is the optical gap so defined, $\sigma$ is the absorption cross section, and $F$ is the total oscillator strength. We note that this is the same empirical criterion employed in interpreting experimental data for GaAs clusters,²⁸ where a similar problem exists. Although there is a degree of arbitrariness to the 2% rule, the gap so defined is not very sensitive to the 2% value. It will also allow us to examine trends in the quantum dot absorption spectra using a "standard" criterion.

![](./images/812393806866415616_5.jpg)

FIG. 3. Size dependence of the optical gap for CdSe quantum dots. The dashed line is a guide to the eye, roughly fit to the measured gaps. Open symbols represent gaps calculated from TDLDA (squares) and LDA (triangles). The solid symbols are measured gaps from Soloviev *et al.* (Ref. 33) (squares), Rogach *et al.* (Ref. 34) (dots), and Murray *et al.* (Ref. 9) (diamonds).

Figure 3 shows the size dependence of the optical gaps for CdSe quantum dots from theory and experiment. The measured optical gap for the smallest dot shown is 3.8 eV. For sufficiently large dots, one expects the optical gap to converge to the bulk value of 1.7 eV.³² This is consistent with experimental studies of dots over a wide range of sizes.⁹,³³ Figure 3 also shows the optical gaps obtained experimentally by Soloviev *et al.*,³³ Murray *et al.*,⁹ and Rogach *et al.*.³⁴

It can be observed that the optical gaps calculated using *time-independent* LDA significantly underestimates the experimental gaps as well as the gaps calculated using TDLDA when the "2% rule" is invoked. Specifically, the LDA gaps are more than 2 eV smaller the TDLDA values and in poor agreement with experiment. In contrast, the optical gaps calculated using TDLDA show good agreement with the experimental findings, especially with those of Soloviev *et al.*³³ This justifies our use of the "2% rule" in an *a posteriori* sense.

In summary, reproducing the experimental optical gaps of semiconductor quantum dots is not a straightforward task. The most difficult issue to address is the existence of the electronically active states in the gap. In previous work, several schemes have been attempted in order to remove such states, such as placing artificial ligand potentials at the surface.¹⁵,¹⁶ With our approach no arbitrary artificial potentials are used, and we enforce the geometry of the dots to be that of the bulk crystal, as it was found in experiment. We

calculated the absorption spectra and optical gaps for $Cd_nSe_n$ ($n=17,26,38$) quantum dots using the TDLDA technique. The TDLDA spectra differ from those calculated using the time-independent LDA approach. They differ both in absorp- tion threshold and spectral features. The calculated optical gaps for these dots are in good agreement with experimental results.

## ACKNOWLEDGMENTS

We would like to acknowledge the support provided by the National Science Foundation, the U.S. Department of Energy [Computational Materials Science Network (CMSN)], and the Minnesota Supercomputer Institute. LK acknowledges the generous support of the Estelle Funk Foundation and the Delta Career Development Chair.

$^{1}$ Al. L. Efros and M. Rosen, Annu. Rev. Mater. Sci. 30, 475 (2000).
$^{2}$ A. D. Yoffe, Adv. Phys. 42, 173 (1993).
$^{3}$ L. Jacak, P. Hawrylak, and A. Wojs, *Quantum Dots* (Springer-Verlag, Berlin, 1998).
$^{4}$ U. Woggon, *Optical Properties of Quantum Dots* (Springer-Verlag, Berlin, 1996).
$^{5}$ T. Chakraborty, *Quantum Dots: A Survey of the Properties of Artificial Atoms* (Elsevier, Amsterdam, 1999).
$^{6}$ P. Harrison, *Quantum Wells, Wires, and Dots* (Wiley, New York, 2000).
$^{7}$ L. B. Banyai and S. W. Koch, *Semiconductor Quantum Dots* (World Scientific, Singapore, 1993).
$^{8}$ A. P. Alivisatos, Science 271, 933 (1996).
$^{9}$ C. B. Murray, D. J. Norris, and M. G. Bawendi, J. Am. Chem. Soc. 115, 8706 (1993).
$^{10}$ S. Gorer and G. Hodes, J. Phys. Chem. 89, 5338 (1994).
$^{11}$ D. Gal, G. Hodes, D. Hariskos, D. Braunger, and H.-W. Schock, Appl. Phys. Lett. 73, 3135 (1998).
$^{12}$ M. Kuno, J. K. Lee, B. O. Dabbousi, F. V. Mikulec, and M. G. Bawendi, J. Chem. Phys. 106, 9869 (1997).
$^{13}$ A. C. Carter, C. E. Boulding, K. M. Kemmer, M. I. Bell, J. C. Woicik, and S. A. Majetich, Phys. Rev. B 55, 13822 (1997).
$^{14}$ V. N. Soloviev, A. Eichhöfer, D. Fenske, and U. Banin, J. Am. Chem. Soc. 123, 2354 (2001).

$^{15}$ L. Wang and A. Zunger, Phys. Rev. B 53, 9579 (1996).
$^{16}$ E. Rabani, B. Hetenyi, and B. J. Berne, J. Chem. Phys. 110, 5355 (1999).
$^{17}$ V. R. Saunders and J. H. van Lenthe, Mol. Phys. 48, 923 (1983); R. J. Buenker, S. D. Peyerimhoff, and W. Butscher, ibid. 35, 771 (1978).
$^{18}$ D. M. Ceperley and B. Bernu, J. Chem. Phys. 89, 6316 (1988); B. Bernu, D. M. Ceperley, and W. A. Lester, Jr., ibid. 93, 552 (1990); 95, 7782 (1991).
$^{19}$ M. Rohlfing and S. Louie, Phys. Rev. Lett. 81, 2312 (1998).
$^{20}$ M. E. Casida, in *Recent Advances in Density-Functional Methods*, Part I, edited by D. P. Chong (World Scientific, Singapore, 1995), p. 155; in *Recent Developments and Applications of Modern Density Functional Theory*, edited by J. M. Seminario (Elsevier Science, Amsterdam, 1996), p. 391.
$^{21}$ I. Vasiliev, S. Öğüt, and J. R. Chelikowsky, Phys. Rev. Lett. 86, 1813 (2001); I. Vasiliev, S. Öğüt, and J. R. Chelikowsky, Phys. Rev. B 65, 115416 (2002), and references therein
$^{22}$ C. S. Garoufalis, A. D. Zdetsis, and S. Grimme, Phys. Rev. Lett. 87, 276402 (2001).
$^{23}$ J. R. Chelikowsky, N. Troullier, K. Wu, and Y. Saad, Phys. Rev. B 50, 11355 (1994); J. R. Chelikowsky, N. Troullier, X. Jing, D. Dean, N. Binggeli, K. Wu, and Y. Saad, Comput. Phys. Commun. 85, 325 (1995); Y. Saad, A. Stathoupolos, J. R. Chelikowsky, K. Wu, and S. Öğüt, BIT 36, 563 (1996).
$^{24}$ N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).
$^{25}$ S. G. Louie, S. Froyen, and M. L. Cohen, Phys. Rev. B 26, 1738 (1982).
$^{26}$ D. M. Ceperley, Phys. Rev. B 18, 3126 (1978); D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).
$^{27}$ J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981).
$^{28}$ R. Schäfer and J. A. Becker, Phys. Rev. B 54, 10296 (1996).
$^{29}$ P. Deglmann, R. Ahlrichs, and K. Tsereteli, J. Chem. Phys. 116, 1585 (2002).
$^{30}$ K. Eichkorn and R. Ahlrichs, Chem. Phys. Lett. 288, 235 (1998).
$^{31}$ M. C. Troparevsky, L. Kronik, and J. R. Chelikowsky, Phys. Rev. B 65, 033311 (2002).
$^{32}$ K. H. Hellwege, *Landoldt-Börnstein, Numerical Data and Functional Relationships in Science and Technology* (Springer-Verlag, Berlin, 1983).
$^{33}$ V. N. Soloviev, A. Eichhöfer, D. Fenske, and U. Banin, J. Am. Chem. Soc. 122, 2673 (2000).
$^{34}$ A. L. Rogach, A. Koronowsky, M. Gao, A. Eychmüller, and H. J. Weller, J. Phys. Chem. B 103, 3065 (1999).