# DENSITY FUNCTIONAL CALCULATION OF THE Si-H DISSOCIATION ENERGIES ON THE Si(100) SURFACE

CARLOS SOSA*, CHENGTEH LEE*, PETR NACHTIGALL** AND KENNETH D. JORDAN**

*Cray Research, Inc., 655 E Lone Oak Dr., Eagan, MN 55121
**Department of Chemistry, University of Pittsburgh, Pittsburgh, PA 15260

## ABSTRACT

Density functional theory is used to investigate the surface dimer of the 2x1 reconstructed Si(100) surface and its hydrides. This is accomplished by adoption of a $Si_9H_{12}$ cluster to model the bare surface dimer and $Si_9H_{13}$ and $Si_9H_{14}$ clusters to model surface hydrides. DFT calculations with nonlocal corrections give energies of 84.2, 81.4, and 54.0 kcal/mol for the $Si_9H_{14} \rightarrow Si_9H_{13} + H$, $Si_9H_{13} \rightarrow Si_9H_{12} + H$, and $Si_9H_{14} \rightarrow Si_9H_{12} + H_2$ reactions, respectively. These are in good agreement with earlier estimates of the reaction energies calculated by means of the quadratic CI procedure.

## Introduction

The reconstructed Si(100)2x1 surface consists of rows of surface dimers, with each Si atom of a dimer pair having one dangling bond with an unpaired electron. As a result, the surface is quite reactive. Much recent work has focused on the mechanism of recombinative $H_2$ desorption from the monohydride phase of Si(100)2x1 surfaces [1, 2]. Experimental values of the activation energy of desorption range from 45 to 66 kcal/mol. Moreover, several different mechanisms for the desorption process have been proposed. These include: (a) model of "delocalized" hydrogen suggested by Sinniah and coworkers [2a], (b) "pair-wise" desorption mechanism [2c], and (c) mechanism involving 1,2 hydrogen shift prior to desorption [1c,2f]. Theoretical studies can prove valuable in elucidating the mechanisms of such surface processes.

In this study, Density Functional Theory (DFT) is used to calculate the strengths of the surface Si-H bonds, information which is important for understanding $H_2$ desorption and H atom diffusion on the Si(100) surface. Comparison will be made with the predictions of much more computationally demanding quadratic CI (QCI) calculations. As has been done in several prior investigations [1c], we adopt a $Si_9H_{12}$ cluster model of the Si(100) surface. This cluster has a pair of Si atoms at the surface, four, two, and one Si atoms in the first, second, and third sublayers, respectively. The hydrogen atoms are included to terminate the subsurface Si atoms. In order to calculate Si-H surface bonds we also consider the $Si_9H_{13}$ and $Si_9H_{14}$ clusters.

Mat. Res. Soc. Symp. Proc. Vol. 315. ©1993 Materials Research Society

### Method

The DFT calculations were carried out using the DGauss [3] and deMon [4] programs. Gaussian-type functions are used for representing the Kohn-Sham orbitals [5, 6] as well as auxiliary fitting functions [7-9]. Geometries are optimized in the local density approximation (LDA) using the Dirac exchange functional and the Vosko, Wilk, and Nusair (VWN) correlation energy functional [10].

Single point calculations including self-consistent nonlocal corrections (NLSD) are carried out at the LDA optimized structures. Two types of gradient corrected functionals were used in the NLSD calculations: (1) using the Becke [9] exchange and the Lee, Yang and Parr correlation functional [11a] (B-LYP) and (2) using the Becke [9] exchange and the Perdew [11b] correlation (B-P) functional. The LYP correlation is the density functional energy formulation of Colle-Salvetti correlation energy [12]. In the Becke-Perdew model the gradient corrected exchange-correlation terms were also added perturbatively to the local spin density energy (VWN+BP).

A double-zeta-split-valence plus polarization (DZVP) basis sets [13] were used for all atoms in the geometry optimization and single point calculations. In addition, single point calculations with the VWN+BP approximation were carried out using triple-zeta plus polarization basis functions (TZVPP) [14].

The geometries of the three clusters were optimized as described in ref. [1c]. The atom labeling scheme is defined in Figure 1. All the Si atoms for layers four (Si3) and three (Si1 and Si2) were fully frozen in the bulk-like positions. All of the coordinates for the hydrogen atoms used to terminate dangling bonds were also fully fixed. The four Si atoms in the second layer (Si16, Si17, Si18, and Si19) were allowed to move in the x and z directions (see figure 1). The position of the surface Si atoms and the associated hydrogen atoms (if any) were fully optimized. The constraints on the sublayer atoms were chosen in order to prevent unrealistic distortions due to the adoption of the finite cluster model.

### Results and Discussion

The geometries of the $Si_9H_{13}$ and $Si_9H_{14}$ clusters were previously optimized using the Hartree-Fock approximation, and that of the $Si_9H_{12}$ cluster was optimized at the Hartree-Fock and two-configuration MCSCF levels [1c]. For $Si_9H_{13}$ and $Si_9H_{14}$, LDA and Hartree-Fock optimized geometries are in good agreement. On the other hand, different theoretical methods give appreciably different results for the $Si_9H_{12}$ cluster, particularly for the Si-Si distance in the surface dimer. It should be pointed out that this bond has partial "$\pi$" character due to weak interaction of dangling bonds on surface dimer silicon atoms. As a result, HF description is insufficient, giving Si-Si bond length $2.18\ \mathring{A}$, 0.14 shorter than value obtained at the MCSCF level of theory $(2.32\ \mathring{A})$. At the LSD level the Si-Si bond length is $2.23\ \mathring{A}$. (Experimentally this bond length 2.35-2.47 $\mathring{A}$ [15].) The NLSD and QCI energies for $Si_9H_{14}$ $\rightarrow Si_9H_{13} + H$, $Si_9H_{13} \rightarrow Si_9H_{12} + H$, and $Si_9H_{14} \rightarrow Si_9H_{12} + H_2$ are compared in table I.

![](./images/811676629959966722_1.jpg)

![](./images/811676629959966722_2.jpg)

![](./images/811676629959966722_3.jpg)

Figure 1. Optimized cluster geometries.

**Table I. Energies of Reaction in kcal/mol.**

<table>
  <thead>
    <tr>
      <th>Level</th>
      <th>$\text{Si}_9\text{H}_{14} \rightarrow \text{Si}_9\text{H}_{13} + \text{H}$</th>
      <th>$\text{Si}_9\text{H}_{13} \rightarrow \text{Si}_9\text{H}_{12} + \text{H}$</th>
      <th>$\text{Si}_9\text{H}_{14} \rightarrow\text{Si}_9\text{H}_{12} + \text{H}_2$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>QCISD(T)/TZ2P</td>
      <td>87.9</td>
      <td>83.6</td>
      <td>64.4</td>
    </tr>
    <tr>
      <td>VWN+BP/TZVPP</td>
      <td>84.2</td>
      <td>81.4</td>
      <td>54.0</td>
    </tr>
  </tbody>
</table>

The QCISD(T) and NLSD methods are giving energies of Si-H bonds in a good agreement. The NLSD calculated energies are 3.7 and 2.2 kcal/mol smaller than the QCISD(T) values for the desorption energy of the second and first H atom on the dimer, respectively. On the other hand, there is 10.4 kcal/mol difference between NLSD and QCISD(T) calculated $\text{H}_2$ desorption energy. This is mainly due to the description of H-H bond. The $\text{H}_2$ dissociation energies (not including zero-point energy correction) are 106.9 and 111.6 kcal/mol at the QCISD(T)/TZ2P and VWN+BP/TZVPP levels of theory, respectively, while experimental value is 109.4 kcal/mol. Thus $\text{H}_2$ description is responsible for almost 5 kcal/mol difference in desorption energies of $\text{H}_2$ at NLSD and QCISD(T) levels of theory. As indicated above, the rest of the difference comes from the description of Si-H bonds. Giving opposite sign of the error in describing $\text{H}_2$ dissociation energy at QCISD(T) and NLSD levels of theory, we believe that the correct $\text{H}_2$ desorption energy lies between the QCISD(T) and NLSD value. In other words, the 10.4 kcal/mol difference in $\text{H}_2$ desorption energy is due to approximations in both QCISD(T) and NLSD methods. We conclude that for the description of $\text{H}_2$ desorption from the Si(100) surface the NLSD level of theory can provide energies of comparable reliability as QCISD(T) with all-electron corrections. This is important for study of larger clusters where QCISD(T) method cannot be applied.

In order to investigate the reliability of VWN+BP nonlocal corrections, which uses only LSD density, we calculated energies for the $\text{Si}_9\text{H}_{14} \rightarrow \text{Si}_9\text{H}_{13} + \text{H}$, $\text{Si}_9\text{H}_{13} \rightarrow \text{Si}_9\text{H}_{12} + \text{H}$, and $\text{Si}_9\text{H}_{14} \rightarrow\text{Si}_9\text{H}_{12} + \text{H}_2$ processes by employing several different exchange and correlation functionals and DZVP basis set. Results are summarized in table II.

**Table II. Nonlocal Reaction Energies**

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>VWN+BP</th>
      <th>B-P</th>
      <th>B-LYP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{Si}_9\text{H}_{14} \rightarrow \text{Si}_9\text{H}_{13} + \text{H}$</td>
      <td>86.1</td>
      <td>86.3</td>
      <td>85.0</td>
    </tr>
    <tr>
      <td>$\text{Si}_9\text{H}_{13} \rightarrow \text{Si}_9\text{H}_{12} + \text{H}$</td>
      <td>82.9</td>
      <td>82.4</td>
      <td>82.2</td>
    </tr>
    <tr>
      <td>$\text{Si}_9\text{H}_{14} \rightarrow\text{Si}_9\text{H}_{12} + \text{H}_2$</td>
      <td>56.0</td>
      <td>55.8</td>
      <td>56.5</td>
    </tr>
  </tbody>
</table>

Nonlocal corrections were added perturbatively ( VWN+BP ) as well as self-consistently (B-P and B-LYP). Reaction energies at VWN+BP, B-P, and B-LYP levels are in very good agreement.

### Acknowledgements

The authors wish to thank the Corporate Computing and Networking Division at Cray Research is kindly acknowledged for providing computational resources to carry out this work.

### References

1.  (a) A. Redondo and W. A. Goddard III, J. Vac. Sci. Technol. **21**, 344(1982); (b) Y. J. Chabal and K. Raghavachari, Phys. Rev. Lett. **53**, 282(1984); (c) P. Nachtigall, K. D. Jordan, and K. C. Janda, J. Chem. Phys. **95**, 8652(1991); (d) C. J. Wu and E. A. Carter, Chem. Phys. Lett. **185**, 172(1991); (e) J. A. Appelbaum, G. A. Baraff, D. R. Hamann, H. D. Hagstrum, and T. Sakurai, Surface Sci. **70**, 654(1978); f) W. S. Verwoed, Surface Sci. **108**, 153(1981); g) B.I. Craig and P. V. Smith, Surface Sci. **226**, 155(1990).

2.  (a) K. Sinniah, M. G. Sherman, L. B. Lewis, W. H. Weinberg, J. T. Yates, Jr., and K. C. Janda, J. Chem. Phys. **92**, 5700(1990); (b) K. Sinniah, M. G. Sherman, L. B. Lewis, W. H. Weinberg, J. T. Yates, Jr., and K. C. Janda, Phys. Rev. Lett. **62**, 567(1989); (c) M. L. Wise, B. G. Koehler, P. Gupta, P. A. Coon, and S. M. George, Surf. Sci. ( in press ); (d) K. W. Kolasinski, S. F. Shane, and R. N. Zare, J. Chem. Phys. **95**, 5482(1991); (e) J. J. Boland, Phys. Rev. Lett. **67**, 1539(1991); (f) S. F. Shane, K. W. Kolasinski, and R. N. Zare, J. Chem. Phys. **97**, 3704(1992)

3.  (a) J. Andzelm and E. Wimmer, J. Chem. Phys. **96**, 1280(1992); (b) J. Andzelm, in Density Functional Methods in Chemistry, edited by J. Labanowski, and J. Andzelm (Springer, New York, 1991), pp. 155.

4.  D. R. Salahub, R. Fournier, P. Mlynarski, I. Papay, A. St-Amant, and J. Ushio, in Density Functional Methods in Chemistry, edited by J. Labanowski and J. Andzelm (Springer-Verlag, New York, 1991), pp. 77.

5.  P. Hohenberg and W. Kohn, Phys. Rev. **B136**, 864 (1964).

6.  W. Kohn and L. J. Sham, Phys. Rev. **A140**, 1133 (1965).

7.  H. Sambe, and R.H. Felton, J. Chem. Phys. **B62**, 1122 (1975).

8.  B.I. Dunlap, J.W.D. Connolly, and J.R. Sabin, J. Chem. Phys. **71**, 3396 (1979).

9.  (a) A. D. Becke, Phys. Rev. **A38**, 3098(1988); (b) A. D. Becke, J. Chem. Phys. **88**, 2547(1988).

10. S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys. **58**, 1200(1980).

11. (a) C. Lee, W. Yang, and R. G. Parr, Phys. Rev. **B37**, 785(1988); (b) J. P. Perdew, Phys. Rev. **B33**, 8822(1986).

12. R. Colle and D. Salvetti, Theor. Chim. Acta **37**, 329(1975).

13. N. Godbout, D. R. Salahub, J. Andzelm, and E. Wimmer, Can. J. Chem. **70**, 560(1992)..

14. The TZVPP basis set uses (13s9p1d)/[5s4p1d] contraction of Godbout's DZVPP basis set [16] for silicon atoms. The correlation consistent TZP basis set of Dunning was employed for hydrogen atoms. T. H. Dunning, Jr., J. Chem. Phys. **90**, 1007 (1989).

15. Z. Jing and J. L. Whitten, Surface Sci. **274**, 106(1992).