
# Determination of the nitrogen vacancy as a shallow compensating center in GaN doped with divalent metals

J. Buckeridge, \( ^{1,*} \)  C. R. A. Catlow, \( ^{1} \)  D. O. Scanlon, \( ^{1,2} \)  T. W. Keal, \( ^{3} \)  P.

Sherwood, \( ^{3} \)  M. Miskufova, \( ^{1} \)  A. Walsh, \( ^{4} \)  S. M. Woodley, \( ^{1} \)  and A. A. Sokol \( ^{1,\dagger} \) 

 \( ^{1} \) University College London, Kathleen Lonsdale Materials Chemistry,

Department of Chemistry, 20 Gordon Street, London WC1H 0AJ, United Kingdom

 \( ^{2} \) Diamond Light Source Ltd., Diamond House, Harwell Science and Innovation Campus, Didcot, Oxfordshire OX11 0DE, United Kingdom

 \( ^{3} \) Scientific Computing Department, STFC, Daresbury Laboratory,

Daresbury, Warrington, WA4 4AD, United Kingdom

 \( ^{4} \) Centre for Sustainable Chemical Technologies and Department of Chemistry, University of Bath, Claverton Down, Bath BA2 7AY, United Kingdom

We report accurate energetics of defects introduced in GaN on doping with divalent metals, focussing on the technologically important case of Mg doping, using a model which takes into consideration both the effect of hole localisation and dipolar polarisation of the host material, and includes a well-defined reference level. Defect formation and ionisation energies show that divalent dopants are counterbalanced in GaN by nitrogen vacancies and not by holes, which explains both the difficulty in achieving p-type conductivity in GaN and the associated major spectroscopic features, including the ubiquitous 3.46 eV photoluminescence line, a characteristic of all lightly divalent-metal-doped GaN materials that has also been shown to occur in pure GaN samples. Our results give a comprehensive explanation for the observed behaviour of GaN doped with low concentrations of divalent metals in good agreement with relevant experiment.

PACS numbers: 61.72.J-, 71.55.Eq, 78.55.Cr

Gallium nitride, a wide-gap semiconductor, is an important material used for a range of applications, e.g. solid state lighting, high power microelectronics, is an essential component of commercial blue light emitting diodes, which requires both n- and p-type conducting layers [1]. While it has been intensively researched for several decades, many puzzling features still remain. For instance, GaN is natively n-type, indicating the presence of shallow donors, but whether these centres are native point defects (e.g. nitrogen vacancies) or unwanted impurities incorporated during growth (such as hydrogen, oxygen or silicon) remains a source of controversy [2, 3].

Industrially, the production of p-type GaN is still the main bottleneck. The only successful approach has been to dope with Mg but there are many associated problems: large concentrations of Mg close to the solubility limit, as well as processing such as thermal annealing or electron irradiation, are required to achieve significant p-type activation; high dislocation densities limit hole mobilities; there is a residual n-type concentration that must be overcome; and self-compensation may limit activation [4, 5].

At low temperature (T), the band gap of GaN is 3.503 eV [6]. Experimental techniques such as photoconductance, photoluminescence (PL), and deep level transient spectroscopy indicate that the  \( Mg_{Ga} \)  acceptor state lies  \( \sim 0.150 - 0.265 \)  eV above the valence band maximum (VBM) [7], corroborated by theoretical studies [8, 9]. With such a deep level, however, why Mg-doping results in p-type conductivity is not well understood, although theories have been proposed involving defect complexes and hydrogen impurities [10–12], with some experimental support [13, 14]. Similar acceptor levels are found for other divalent dopants including Zn, Cd, Be and Sr [15], but the lack of associated p-type activation, in contrast to Mg, has not been explained.

Adding small amounts of Mg to GaN leads to characteristic peaks in the UV range of the PL spectrum, at 3.27 eV and at 3.466 eV (measured at  \( T = 2 \, K \) ) [16] and in some samples a peak at  \( \sim 3.2 \, eV \)  [17, 18]. The peak at 3.466 eV is also observed in samples doped with other divalent cations [15] and is attributed to acceptor-bound excitons (ABEs) [19]. Interestingly, there is some evidence that this peak occurs in nominally undoped GaN samples [16], indicating that it may instead relate to some compensating native shallow defect. When the Mg content increases, the PL spectrum changes, becoming dominated by a broad peak at  \( \sim 2.9 \, eV \) , corresponding to blue luminescence (BL) and attributed to donor-acceptor pairs (DAPs) [16]. BL has also been observed in samples when T is raised, rather than the Mg concentration ([Mg]) [17]. So far theory fails to account for the characteristic UV luminescence associated with small [Mg], but recombination processes have been proposed to account for BL and also red luminescence [9–12], which is sometimes observed in heavily-doped samples.

Recent thermal admittance spectroscopy (TAS) measurements on epitaxially grown n-GaN have found that the shallow donor level lies 51 meV below the conduction band minimum (CBM) [20], agreeing with older measurements using electron irradiation techniques [21] (placing the level at  \( 64 \pm 10 \)  meV below the CBM). This level
 

is significantly deeper than those introduced when GaN is intentionally doped n-type with e.g. Si or O ( \( \sim \)  30 meV) [15]. Such a shallow positive defect may act as a compensating centre for holes in GaN, though this has not conclusively been shown to be the case.

In this Letter, we present calculated formation and ionisation energies of nitrogen vacancies ( \( V_{N} \) ) and Mg substituting on a Ga site ( \( Mg_{Ga} \) ) in GaN in the dilute limit, using a multiscale embedded cluster approach. We also calculate the ionisation energies associated with the divalent substitutions:  \( Be_{Ga} \) ,  \( Zn_{Ga} \) , Cd \( _{Ga} \) , and Hg \( _{Ga} \)  in the dilute limit. We find isolated  \( Mg_{Ga} \)  do not contribute to p-type conductivity, instead they are compensated by  \( V_{N} \)  formation. The same result follows for the other divalent dopants considered. We find the  \( V_{N} \)  is a shallow donor at 44 meV below the CBM, accounting for the observed 3.466 eV PL peak, and is stable in the negative charge state, facilitating Fermi level pinning close to (and above) the CBM and leading to native n-type conductivity. We determine that the equilibrium  \( Mg_{Ga} \)  level lies 0.307 eV above the VBM; we also calculate related levels that depend on the hole configuration and final spin state after excitation, that, although are slightly less favorable, will be accessible in fast PL experiments and account for the main peaks observed at low T and [Mg]. The observed BL is related to excitation and recombination of ionised  \( V_{N} \) , which will occur in greater concentrations at higher T and [Mg], in agreement with experiment. We also find good agreement between our calculated ionisation energies for Be, Zn, Cd, and Hg impurities and relevant PL measurements. Our results give a simple but comprehensive explanation to the observed native n-type conductivity, PL spectrum at low Mg content, and the difficulty with p-type doping in GaN.

We employed the hybrid quantum mechanical/molecular mechanical (QM/MM) embedded cluster method [22] to calculate bulk and defect energies in GaN. In this approach, a defect (possibly charged) and its immediately surrounding region, of the order of 100 atoms, is treated using a QM level of theory - here using density functional theory (DFT) with a triple-zeta-plus-polarisation Gaussian basis set (see Ref. [23] for details) and a hybrid exchange and correlation functional employing 42% exact exchange (BB1K) [24]. The QM region is embedded within a larger cluster, typically 10000 – 20000 atoms, which is treated at a MM level of theory, using polarisable-shell interatomic potentials that accurately reproduce the dielectric, elastic, and structural properties of the bulk material [25]. Thus one can model accurately isolated charged defects in any dimensionality [26], fully accounting for the dielectric response from the surrounding material. As supercells are not employed, there is no need to correct for image-charge interactions. Crucially, ionisation energies can be determined relative to a well-defined reference level, which we term the 'vacuum level' (although in reality it is a 'quasi-vacuum' level, because surface effects are not included in the energetics). Technical details, including the treatment of cluster termination and the interface between the QM and MM regions, are discussed elsewhere [22, 23]. One caveat is that the defects modelled must be localised within the QM region, which, however, applies in the current case. This method was applied successfully to treat defects in ZnO [27] and band alignment in  \( TiO_{2} \)  [28].

![](./images/867746557213016361_1.jpg)

FIG. 1: (Color online) Calculated spin density resulting from (a) a  \( Mg_{Ga}^{0} \) -associated hole localized on a neighboring N in the basal plane; (b) a  \( Mg_{Ga}^{0} \) -associated hole localized on a neighboring axial N; and (c) a N vacancy. Light gray/green (darker gray/blue) spheres represent Ga (N) atoms. The darkest grey sphere represents a Mg atom in (a) and (b) (purple) and a vacancy in (c) (orange). Spin densities are indicated by (red) isosurfaces of density (au) 0.05, 0.025, and 0.01 for (a) and (b) and 0.01, 0.005, 0.0025 for (c).

We first consider the  \( Mg_{Ga} \)  defect. We determine the formation energy of defect X ( \( E_{f}[X] \) ) as:

 \[ E_{f}[X]=\Delta E(X)-\sum_{i}n_{i}\mu_{i}+qE_{F}, \quad (1) \] 

where \(\Delta E(X)\) is the difference in energy between the embedded cluster with and without \(X\), \(n_{i}\) is the number of atoms of species \(i\) added (\(n_{i} > 0\)) or subtracted (\(n_{i} < 0\)) in forming \(X\), \(\mu_{i}\) is the chemical potential of species \(i\), \(q\) is the charge of \(X\), and \(E_{F}\) is the Fermi energy. For \(q = 0\), there are two localised hole configurations in the first coordination shell: either on a N in the basal plane of the surrounding tetrahedron of N atoms or on the axial N (for the related spin densities see Fig. 1 (a) and (b)). Using Eq. 2, we find that, in anion-poor conditions (see the Supplementary Information for details) \(E_{f}[Mg_{Ga}^{0}]\), with the hole localised on an axial N, is 1.928 eV, in excellent agreement with previous calculations [11]. In anion-rich conditions, this energy changes to 0.783 eV. The axial hole energy is more favourable (by 0.063 eV) than that of the configuration with the hole localised on a N in the basal plane. If we consider \(\mathrm{Mg}_{3}\mathrm{N}_{2}\) as the source of Mg, rather than Mg metal, we obtain a higher formation energy of 2.375 eV (2.756 eV) for anion-rich (anion-poor) conditions.

The energy to dissociate a hole, according to the reaction:

 \[ \mathrm{Mg}_{\mathrm{Ga}}^{0}\rightarrow\mathrm{Mg}_{\mathrm{Ca}}^{\mathrm{0}}+h^{+} \quad (2) \]
 

is highly unfavourable at 1.404 eV. This result differs from the low value of 0.26 eV obtained using periodic supercell models [11], which may suffer from incomplete cancellation of the electron self-interaction [29, 30] and treatment of long-range polarisation, as well as an absence of a well-defined reference [31]. Our result, however, is consistent with earlier work on thermodynamical doping limits in GaN [23], which showed that free holes are unstable with respect to point defect formation (agreeing with the natively n-type nature of GaN). Indeed, considering the compensation of holes by the formation of  \( V_{N} \) :

 \[ h^{+}+\frac{1}{3}\mathrm{N}_{\mathrm{N}}^{0}\leftrightarrow\frac{1}{3}\mathrm{V}_{\mathrm{N}}^{3+}+\frac{1}{6}\mathrm{N}_{2}, \quad (3) \] 

we determine a reaction energy of -1.245 eV, i.e. the balance is far to the right, indicating the thermodymical instability of holes. Consequently, doping with low levels of Mg will not result in free-hole formation, instead compensation by  \( V_{N} \)  will occur. We stress that our calculations apply to the dilute limit, under the assumption of thermodynamical equilibrium. For certain designs and/or synthetic procedures, where kinetic effects may dominate, or at higher [Mg], where the formation of complexes or phase segregated nanostructures may occur, the balance of the reaction (Eq. 3) could shift to the left.

![](./images/867746557213016361_2.jpg)

FIG. 2: (Color online) Formation energy of  \( V_{N} \)  (black line) and  \( Mg_{Ga} \)  (light gray/red line) as a function of Fermi energy above the valence band maximum (VBM). Anion-rich conditions are assumed. The position of the conduction band minimum (CBM) is indicated by the broken line. For each value of Fermi energy, only the most stable defect charge state is shown, with a change in slope indicating a change in charge state.

We show the formation energy of  \( V_{N} \)  (assuming N-rich conditions), determined using Eq. 2, as a function of  \( E_{F} \)  relative to the VBM in Fig. 2 (see Fig. 1 (c) for the related spin density). We find that, in n-type conditions, the  \( V_{N} \)  is singly ionised, indicating that it is shallow. In p-type conditions the formation of  \( V_{N}^{3+} \)  becomes spontaneous, indicating the instability of free holes.  \( V_{N}^{2+} \)  is unfavourable at any value of  \( E_{F} \)  within the gap.  \( V_{N}^{+} \)  and  \( V_{N}^{3+} \)  are equally favourable at  \( E_{F} = 1.835 \)  eV, a result significantly higher than those determined using plane-wave basis set calculations [8, 10] (see the above discussion on self-interaction errors).  \( V_{N}^{-} \)  becomes favorable in the regime of degenerate n-type conduction at  \( \sim 0.9 \)  eV above the CBM, where it is expected to pin  \( E_{F} \) . Integrating the density of states up to this  \( E_{F} \)  gives an n-type concentration of  \( \sim 10^{20} \)  cm \( ^{-3} \) , which has been observed in some undoped n-type samples [33].

![](./images/867746557213016361_3.jpg)

FIG. 3: (Color online) Calculated vertical ionisation levels of (a)  \( Mg_{Ga} \)  and (b)  \( V_{N} \)  in the relevant charge states, shown relative to the valence band (VB), conduction band (CB) and vacuum level. In (a) the two hole configuration cases, consisting of localisation on a N either in the basal plane or along the c axis, are shown. For the neutral state, ionisation to either singlet or triplet states are included. The large black boxes indicate resonance states in the VB.

In Fig. 3 (a), we show the calculated vertical ionisation energies (IEs) of  \( Mg_{Ga} \)  relative to the conduction and valence bands. The IE is defined as the difference between the energy of a defect in charge state q, and the energy of the defect in the same configuration, but with charge  \( q + 1 \) . The VBM relative to the vacuum level is determined by considering ionisation of an electron from the bulk system. We include ionisation of  \( Mg_{Ga}^{0} \)  and  \( Mg_{Ga}^{+} \) with both hole configurations (i.e. with the hole localised on a basal plane N or axial N), as both should be accessible from electron excitation experiments such as PL. For the same reason, we include both possible final states,
 

singlet and triplet, for the case of ionisation of  \( Mg_{Ga}^{0} \) . Such IEs correspond to emission energies of photoexcited electrons recombining with these defect levels, as would be observed in PL experiments, where, after excitation, atoms typically do not have adequate time to fully relax. Our calculations are in excellent agreement with the low T and [Mg] PL spectra observed experimentally [16, 17]. We reproduce well the DAP PL peaks at 3.21 and 3.27 eV, [34] and the ABE peak at 3.466 eV. The 2.75 eV IE of  \( Mg_{Ga}^{0} \) , although in approximate agreement with the observed BL peak, is unlikely to be observed due to its high formation energy (1.404 eV).

The vertical IEs of  \( V_{N} \)  are, similar to the case of  \( Mg_{Ga} \) , shown in Fig. 3 (b). We find that  \( V_{N}^{0} \)  is a shallow donor, having a vertical IE at 44 meV below the CBM, in good agreement with measurements using TAS and electron irradiation techniques [20, 21]. This level may also account for the 3.46 eV PL peak observed in a wide range of divalently-doped and undoped GaN samples [15–17].  \( V_{N}^{-} \) is also stable and shallow with a vertical IE 52 meV below the CBM. The stability and near degeneracy of the  \( V_{N}^{0} \)  and  \( V_{N}^{-} \) states facilitates Fermi level pinning near the CBM. When the  \( V_{N} \)  donates electrons and relaxes to its equilibrium configurations, the resulting IEs are deep, and in excellent agreement with the 2.95 eV BL peak that is observed at higher [Mg] and at higher T [16, 17]. We associate these levels with the BL as there will be more ionised  \( V_{N} \)  present at higher T and also at higher [Mg] due to an increased number of compensating  \( V_{N} \) .

In Table I we present our calculated IEs associated with  \( Be_{Ga} \) ,  \( Mg_{Ga} \) , Zn \( _{Ga} \) , Cd \( _{Ga} \)  and Hg \( _{Ga} \) ，along with the resulting defect levels, compared with relevant experiment. In each case the agreement is good. For all cases there is an observed 3.46 eV peak, but only for the cases of  \( Be_{Ga} \)  and  \( Mg_{Ga} \)  can we attribute it to an ABE. For the other dopants we attribute the peak to the compensating  \( V_{N} \)  (which may also play a role in Be and Mg doping).

We therefore arrive at a simple explanation for what occurs when Mg or other divalent metal dopants are added to GaN in small concentrations. Isolated  \( Mg_{Ga} \)  strongly trap holes and, therefore, do not contribute to p-type conduction, instead hole carriers will be compensated by the formation of  \( V_{N} \) , a result that follows for other divalent metal dopants [42]. The  \( V_{N} \)  are shallow donors, with the near degeneracy of the neutral and negative charge states pinning the Fermi level close to the CBM, giving rise to the native n-type conductivity. Our calculated IEs are in excellent agreement with the relevant PL spectra. Furthermore, the  \( V_{N} \)  level can give rise to the 3.46 eV peak observed in a wide range of doped and undoped samples, as it will be present as a compensating centre (for the case of Mg and Be doping the 3.46 eV peak can also be attributed to ABEs, which for Mg doping agrees with experiment [13, 15]). A comprehensive description of PL and conductivity phenomena in GaN lightly-doped with Mg, Be, Zn, Cd, and Hg is thus provided, without the need to propose, in the technologically significant case of Mg doping in particular, clustering of  \( Mg_{Ga} \)  and  \( V_{N} \) , or H impurities. The latter may, however, play an important role in heavily-doped GaN, which is less well characterised or understood. The key feature of such a material is the presence of inverted Mg-rich pyramidal domains [43], which could trap interstitial N, making vacancy formation unfavourable, and lead to lower hole ionisation potentials. Such hypotheses, however, require appropriate investigation and are beyond the scope of this study.

In summary, we have comprehensively studied defect formation associated with divalent metal doping in GaN, using a multiscale approach. Our results explain in detail the process, by which low levels of divalent dopants are compensated by  \( V_{N} \) , and are in excellent agreement with available PL experimental data.

## Acknowledgment

The authors acknowledge funding from EPSRC grants ED/D504872, EP/I01330X/1, EP/K016288/1. M. M. acknowledges support from Accelery's Ltd. The authors also acknowledge the use of the UCL Legion High Performance Computing Facility (Legion@UCL) and associated support services, the IRIDIS cluster provided by the EPSRC funded Centre for Innovation (EP/K000144/1 and EP/K000136/1), and the ARCHER supercomputer through membership of the UK’s HPC Materials Chemistry Consortium (EPSRC grant EP/L000202). A. W. thanks C. G. Van de Walle (UCSB) for useful discussions. A. W. and D. O. S. acknowledge membership of the Materials Design Network. We would like to thank C. Humphreys, T. D. Veal, and K. P. O’Donnell for useful discussions.

* Electronic address: j.buckeridge@ucl.ac.uk

 \( ^{\dagger} \)  Electronic address: a.sokol@ucl.ac.uk

[1] S. Nakamura and M. Krames, Proc. IEEE 101, 2211 (2013).

[2] S. Strite and H. Morkoç, J. Vac. Sci. Technol. B 10 (1992).

[3] H. Morkoç, editor, Handbook of Nitride Semiconductors and Devices, Vol. 1, Wiley-VCH, Weinheim, 2008.

[4] H. A. H. M. T.-Y. Seong, J. Han, editor, III-Nitride Based Light Emitting Diodes and Applications, Springer, Berlin, 2013.

[5] L. S. Chuah, Z. Hassan, S. S. Ng, and H. Abu Hassan, J. Mater. Res. 22, 2623 (2007).

[6] B. Monemar, Phys. Rev. B 10, 676 (1974).

[7] O. Madelung, Semiconductors: Data Handbook, Springer, Berlin, third edition, 2004.
 

TABLE I: Calculated photoluminescence (PL) transitions, from total energy calculations, for different hole configurations and corresponding optical defect ionization levels compared with relevant experimental results taken from Refs. [15–17, 35–41].

<table><tr><td rowspan="2"></td><td colspan="4">Photoluminescence (eV)</td><td colspan="2">Levels (meV)</td></tr><tr><td colspan="2">basal-plane hole</td><td colspan="2">axial hole</td><td>Experiment</td><td colspan="2"><img src="imgs/img_in_image_box_1201_261_1301_333.jpg" ></td></tr><tr><td>Final state</td><td>singlet</td><td>triplet</td><td>singlet</td><td> triplet</td><td>0</td><td>1-</td></tr><tr><td>Be</td><td>3.410</td><td>3.427</td><td>3.454</td><td>3.456</td><td>3.384, 3.466</td><td>93, 76, 49, 47</td></tr><tr><td>Mg</td><td>3.272</td><td>3.228</td><td>3.471</td><td>3.196</td><td>3.21, 3.27, 3.466</td><td>275, 231, 307, 32</td></tr><tr><td>Zn</td><td>3.144</td><td>3.201</td><td>3.068</td><td>3.195</td><td>3.100, 3.45</td><td>359, 302, 435, 308</td></tr><tr><td>Cd</td><td>2.845</td><td>2.929</td><td>2.814</td><td>2.934</td><td>2.8, 2.937, 3.455</td><td>658, 574, 689, 569</td></tr><tr><td>Hg</td><td>2.584</td><td>2.666</td><td>2.587</td><td>2.694</td><td>2.70</td><td>919, 837, 916, 809</td></tr></table>

[8] C. G. V. de Walle and J. Neugebauer, J. Appl. Phys. 95, 3851 (2004).

[9] S. Lany and A. Zunger, Appl. Phys. Lett. 96, 142114 (2010).

[10] Q. Yan, A. Janotti, M. Scheffler, and C. G. Van de Walle, Applied Physics Letters 100, 142110 (2012).

[11] J. L. Lyons, A. Janotti, and C. G. Van de Walle, Phys. Rev. Lett. 108, 156403 (2012).

[12] D. Lee, B. Mitchell, Y. Fujiwara, and V. Dierolf, Phys. Rev. Lett. 112, 205501 (2014).

[13] E. R. Glaser, W. E. Carlos, G. C. B. Braga, J. A. Freitas, W. J. Moore, B. V. Shanabrook, R. L. Henry, A. E. Wickenden, D. D. Koleske, H. Obloh, P. Kozodoy, S. P. DenBaars, and U. K. Mishra, Phys. Rev. B 65, 085312 (2002).

[14] M. E. Zvanut, Y. Uprety, J. Dashdorj, M. Moseley, and W. Alan Doolittle, J. Appl. Phys. 110, (2011).

[15] M. A. Reshchikov and H. Morkoç, J. Appl. Phys. 97, 061301 (2005).

[16] B. Monemar, P. P. Paskov, G. Pozina, C. Hemmingsson, J. P. Bergman, S. Khromov, V. N. Izyumskaya, V. Avrutin, X. Li, H. Morkoç, H. Amano et al., J. Appl. Phys. 115, 053507 (2014).

[17] M. Smith, G. D. Chen, J. Y. Lin, H. X. Jiang, A. Salvador, B. N. Sverdlov, A. Botchkarev, H. Morkoç, and B. Goldenberg, Appl. Phys. Lett. 68, 1883 (1996).

[18] B. Monemar, P. P. Paskov, G. Pozina, C. Hemmingsson, J. P. Bergman, T. Kawashima, H. Amano, I. Akasaki, T. Paskova, S. Figge et al., Phys. Rev. Lett. 102, 235501 (2009).

[19] R. Stepniewski, A. Wysmolek, M. Potemski, K. Pakula, J. M. Baranowski, I. Grzegory, S. Porowski, G. Martinez, and P. Wyder, Phys. Rev. Lett. 91, 226404 (2003).

[20] A. O. Ewvaraye, S. R. Smith, and S. Elhamri, J. Appl. Phys. 115, 033706 (2014).

[21] D. C. Look, D. C. Reynolds, J. W. Hemsky, J. R. Sizelove, R. L. Jones, and R. J. Molnar, Phys. Rev. Lett. 79, 2273 (1997).

[22] A. A. Sokol, S. T. Bromley, S. A. French, C. R. A. Catlow, and P. Sherwood, Int. J. Quantum Chem. 99, 695 (2004).

[23] A. Walsh, J. Buckeridge, C. R. A. Catlow, A. J. Jackson, T. W. Keal, M. Miskufova, P. Sherwood, S. A. Shevlin, M. B. Watkins, S. M. Woodley, and A. A. Sokol, Chem. Mater. 25, 2924 (2013).

[24] Y. Zhao, B. J. Lynch, and D. G. Truhlar, J. Phys. Chem. A 108, 2715 (2004).

[25] C. R. A. Catlow, Z. X. Guo, M. Miskufova, S. A. Shevlin, A. G. H. Smith, A. A. Sokol, A. Walsh, D. J. Wilson, and S. M. Woodley, Philos. T. Roy. Soc. A 368, 3379 (2010).

[26] J. Buckeridge, S. T. Bromley, A. Walsh, S. M. Woodley, C. R. A. Catlow, and A. A. Sokol, J. Chem. Phys. 139, 124101 (2013).

[27] A. A. Sokol, S. A. French, S. T. Bromley, C. R. A. Catlow, H. J. J. van Dam, and P. Sherwood, Faraday Discuss. 134, 267 (2007).

[28] D. O. Scanlon, C. W. Dunnill, J. Buckeridge, S. A. Shevlin, A. J. Losgadil, S. M. Woodley, C. R. A. Catlow, M. J. Powell, R. G. Palgrave et al., Nat. Mater. 12, 798 (2013).

[29] G. Pacchioni, F. Frigoli, D. Ricci, and J. A. Weil, Phys. Rev. B 63, 054102 (2000).

[30] If we take into consideration the self-trapping energy of a hole in GaN at 0.3 eV, our result is in reasonable agreement with that of Lany and Zunger, Ref. [9], who used a Koopman's-corrected approach to treat this error.

[31] Indeed, we find a value of 0.863 eV for the reaction energy, lower than 1.404 eV but still above 0.26 eV, when using the B97-2 functional [32], which uses 21% exact exchange, an amount even lower than that used in Ref. [11]. Accurate formation energies require an accurate thermochemical method, which reproduces structure, atomization energies, and ionization potentials.

[32] P. J. Wilson, T. J. Bradley, and D. J. Tozer, J. Chem. Phys. 115, 9233 (2001).

[33] O. Manasreh, editor, III-Nitride Semiconductors: Electrical, Structural and Defect Properties, Elsevier Science Inc., New York, NY, USA, 2000.

[34] Here we are assuming a donor level of 30 – 50 meV below the CBM, but excluding the Coulomb attraction energy between the donor and acceptor pair, as simply subtracting the donor level from the acceptor level values is equivalent to assuming infinite separation.

[35] M. A. L. Johnson, Z. Yu, C. Boney, W. C. Hughes, J. W. Cook Jr., J. F. Schetzina, H. Zhao, B. J. Skromme, and J. A. Edmond, Mater. Res. Soc. Symp. Proc. 449, 215 (1997).

[36] E. Ejder and H. Grimmeiss, Appl. Phys. 5, 275 (1974).

[37] B. Monemar, O. Lagerstedt, and H. P. Gislason, J. Appl. Phys. 51, 625 (1980).

[38] B. Monemar, H. P. Gislason, and O. Lagerstedt, J. Appl. Phys. 51, 640 (1980).

[39] M. Ilegems, R. Dingle, and R. A. Logan, J. Appl. Phys. 43, 3797 (1972).

[40] J. I. Pankove and J. A. Hutchby, J. Appl. Phys. 47, 5387 (1976).

[41] F. J. Sánchez, F. Calle, M. A. Sánchez-García, E. Calleja, E. Muñoz, C. H. Molloy, D. J. Somerford, J. J. Serrano, and J. M. Blanco, Semicond. Sci. Tech. 13, 1130 (1998).
 

[42] As we showed previously [23], the high-T treatment will not result in a significant shift in the equilibrium between the electronic and ionic defects in this and isostructural wide gap semiconductors.

[43] P. Vennéguès, B. Beaumont, E. Feltin, P. De Mierry, S. Dalmasso, M. Leroux, and P. Gibart, Appl. Phys. Lett.

77, 880 (2000).

[44] [Reference in Supplemental Material not already in Letter] F. A. Kröger, The Chemistry of Imperfect Crystals, North-Holland, Amsterdam, 1974.
 
