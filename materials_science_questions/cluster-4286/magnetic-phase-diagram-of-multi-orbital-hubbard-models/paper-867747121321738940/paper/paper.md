
# Fermi surface reconstruction and drop of Hall number due to spiral antiferromagnetism in high- \( T_{c} \)  cuprates

Andreas Eberlein, \( ^{1} \)  Walter Metzner, \( ^{2} \)  Subir Sachdev, \( ^{1,3} \)  and Hiroyuki Yamase \( ^{4} \) 

 \( ^{1} \) Department of Physics, Harvard University, Cambridge MA 02138, USA

 \( ^{2} \) Max Planck Institute for Solid State Research, D-70569 Stuttgart, Germany

 \( ^{3} \) Perimeter Institute for Theoretical Physics, Waterloo, Ontario, Canada N2L 2Y5

 \( ^{4} \) National Institute for Materials Science, Tsukuba 305-0047, Japan (Dated: October 10, 2016)

We show that a Fermi surface reconstruction due to spiral antiferromagnetic order may explain the rapid change in the Hall number as recently observed near optimal doping in cuprate superconductors [Badoux et al., Nature 531, 210 (2016)]. The single-particle spectral function in the spiral state exhibits hole pockets which look like Fermi arcs due to a strong momentum dependence of the spectral weight. Adding charge-density wave order further reduces the Fermi surface to a single electron pocket. We propose quantum oscillation measurements to distinguish between commensurate and spiral antiferromagnetic order. Similar results apply to certain metals in which topological order replaces antiferromagnetic order.

PACS numbers: 71.10.Fd, 74.20.-z, 75.10.-b

Introduction.— Cuprate superconductors evolve from a Mott insulator to a correlated metal with increasing hole doping p. Long ago it was suggested that this evolution involves a quantum critical point (QCP) near optimal doping, and that the associated fluctuations are responsible for the high critical temperature for superconductivity  \( [1-3] \) . The existence and nature of this QCP has not been clarified yet, because it is masked by superconductivity. Recently, the normal ground state became accessible by suppressing superconductivity with high magnetic fields. Near optimal doping in YBCO, Badoux et al. reported a rapid change of the Hall number  \( n_{H} = (R_{H}e)^{-1} \)  with doping [4]. A similar behavior consistent with a drastic drop of the charge carrier density upon lowering the doping was found shortly after in the Hall number and the resistivity of several cuprate materials [5, 6]. These results suggest that a QCP at optimal doping is associated with the reconstruction of a large Fermi surface enclosing a volume corresponding to a density  \( 1 + p \)  of empty states (holes) at large doping, to small pockets with a volume corresponding to a hole-density p in the underdoped regime. Moreover, these experiments indicate that the QCP for the closing of the pseudogap [4, 7] is distinct from that for the disappearance of charge order [8].

The observed transition in the charge carrier density could be associated with the termination of novel pseudogap metals without magnetic order  \( [9–12] \)  or a QCP at which charge-density wave (CDW)  \( [13] \)  or Neel-type antiferromagnetic (AF)  \( [14] \)  order disappears. However, there is experimental evidence at least for YBCO that magnetic order in the ground state of the underdoped regime is incommensurate  \( [15, 16] \) . From theoretical arguments, incommensurate AF has been shown to be favorable long ago for weakly doped Hubbard and t-J models  \( [17–27] \) . Recent renormalization group calculations suggest that incommensurate AF can coexist with superconductivity in a broad doping range  \( [28] \) . The energy gain from the magnetic order is tiny beyond the underdoped regime, but it becomes much more robust when superconductivity is suppressed. This raises the question whether the transition in the Hall number as seen in experiment could be caused by incommensurate antiferromagnetic order.

In this letter, we show that a quantum phase transition from a paramagnetic metal to a spiral antiferromagnetic metal may indeed give rise to a crossover from  \( 1 + p \)  to p in the Hall number as seen in cuprates [4]. Moreover, we find that the single-particle spectral function exhibits hole pockets with a strong spectral weight anisotropy reminiscent of Fermi arcs. Additional charge-density wave order can lead to a single electron pocket, with no additional Fermi surfaces, as observed [29]. To discriminate incommensurate spiral from commensurate antiferromagnetic order we propose a quantum oscillation experiment. We also note that certain topological Fermi liquids [30] have charge transport properties nearly identical to those of metals with magnetic order. And so our transport results apply also to such states.

Spiral states.— In the following we describe spiral antiferromagnetic states using the mean-field Hamiltonian [27]

 \[ H_{\mathrm{M F}}=\sum_{\boldsymbol{k}}\left(c_{\boldsymbol{k}\uparrow}^{\dagger},c_{\boldsymbol{k}+\boldsymbol{Q}\downarrow}^{\dagger}\right)\begin{pmatrix}\xi_{\boldsymbol{k}}&-A\\ -A&\xi_{\boldsymbol{k}+\boldsymbol{Q}}\end{pmatrix}\begin{pmatrix}c_{\boldsymbol{k}\uparrow}\\ c_{\boldsymbol{k}+\boldsymbol{Q}}\end{pmatrix}, \quad (1) \] 

where  \( \xi_{\boldsymbol{k}} = -2t(\cos k_{x} + \cos k_{y}) - 4t' \cos k_{x} \cos k_{y} - \mu \)  is the fermionic dispersion, A the antiferromagnetic gap and  \( Q = (\pi - 2\pi\eta, \pi) \)  the ordering wave vector. We
 

choose the hopping amplitude \(t=1\) as our unit of energy in all numerical results. Diagonalization of \(H_{\mathrm{MF}}\) yields \(H_{\mathrm{MP}}=\sum_{\mathbf{k},i=1,2}E_{\mathbf{k},i}a_{\mathbf{k}i}^{\dagger}a_{\mathbf{k} i}\), where

 \[ E_{\mathbf{k},1/2}=\frac{\xi_{\mathbf{k}}+\xi_{\mathbf{k}+Q}}{2}\mp\sqrt{\frac{1}{4}(\xi_{\mathbf{k}}-\xi_{\mathbf{k}+Q})^{2}+A^{2}}. \quad (2) \] 

The quasi-particle operators  \( a_{ki} \)  are related to the bare fermion operators by  \( c_{\kappa\uparrow} = \sum_{j} U_{\kappa,1j} a_{\kappa j} \)  and  \( c_{\kappa+Q\downarrow} = \sum_{j} U_{\kappa,2j} a_{\kappa j} \) , where

 \[ U_{\mathbf{k}}=\left(\begin{array}{c c}{\frac{A}{\sqrt{A^{2}+(\xi_{\mathbf{k}}-E_{1,\mathbf{k}})^{2}}}}&{\frac{A}{\sqrt{A^{2}+(\xi_{\mathbf{k}}-E_{2,\mathbf{k}})^{2}}}}\\ {-\frac{A}{\sqrt{A^{2}+(\xi_{\mathbf{k}}-E_{2,\mathbf{k}})^{2}}}}&{\frac{A}{\sqrt{A^{2}+(\xi_{\mathbf{k}}-E_{1,\mathbf{k}})^{2}}}}\end{array}\right) \quad (3) \] 

is the orthogonal transformation that diagonalizes  \( H_{MF} \) . In a spiral antiferromagnetic state, the magnetic moments rotate in the xy plane and their directions are modulated by the wave vector Q as  \( \mathbf{m}(\mathbf{R}_{i}) \sim \cos(\mathbf{Q} \cdot \mathbf{R}_{i}) e_{x} + \sin(\mathbf{Q} \cdot \mathbf{R}_{i}) e_{y} \) , where  \( R_{i} \)  is a lattice vector.

We make the ansatz  \( A(p)=\alpha(p^{*}-p)\Theta(p^{*}-p) \)  for the doping dependence of the gap, motivated by results for the on-site magnetization in spiral states in the t-t'-J model [25]. A similar linear doping dependence of the gap in underdoped cuprates is also found in resonating valence bond mean-field theories for the t-J-model [9] or the pseudogap energy scale seen in experiments [31]. For every doping p, the incommensurability  \( \eta \)  is determined by minimizing the free energy at fixed A. More details on the doping dependence of  \( \eta \)  can be found in the supplementary material [32].

Fermi surface and spectral function.— Filling the quasi-particle bands  \( E_{k,1/2} \)  of the spiral state up to the Fermi level yields hole and sometimes electron pockets as shown in the left panel of Fig. 1. For small doping one obtains only two hole pockets [25], while for larger doping two electron pockets appear in addition. Spiral states with four hole pockets are also possible in principle [33], but were not obtained in the present study if the incommensurability  \( \eta \)  is chosen such that the free energy is minimized.

The spectral function for single-particle excitations is given by  \( A(\mathbf{k},\omega)=\sum_{\sigma}A_{\sigma}(\mathbf{k},\omega) \) , where

 \[ A_{\uparrow}(\boldsymbol{k},\omega)=\sum_{i=1,2}U_{\boldsymbol{k},1i}^{2}\delta(\omega-E_{\boldsymbol{k},i}), \quad (4) \] 

 \[ A_{\downarrow}(\boldsymbol{k},\omega)=\sum_{i=1,2}U_{\boldsymbol{k}-\boldsymbol{Q},2i}^{2}\delta(\omega-E_{\boldsymbol{k}-\boldsymbol{Q},i}). \quad (5) \] 

Numerical results for the spectral function at  \( \omega=0 \)  are shown in the right panel of Fig. 1 for two different hole dopings. The momentum shift by Q in the quasi-particle bands contributing to  \( A_{\downarrow}(\mathbf{k},\omega) \)  generates a shifted copy of all pockets. The total (spin summed) spectral function is thus inversion symmetric, but still exhibits a slight nematic deformation.

![](./images/867747121321738940_1.jpg)

![](./images/867747121321738940_2.jpg)

![](./images/867747121321738940_3.jpg)

![](./images/867747121321738940_4.jpg)

Figure 1: Quasi-particle Fermi surfaces (left) and single-electron spectral functions (right) of spiral antiferromagnetic states for p = 0.08, A = 0.63 (top) and p = 0.15, A = 0.23 (bottom), where  \( t' = -0.35 \)  and  \( \eta \approx p \) . Hole and electron pockets in the left panels are marked in red and green, respectively, while the thin lines indicate the bare (black) and the Q shifted (blue) unreconstructed Fermi surfaces.

A most intriguing feature is that for small doping we obtain Fermi pockets with a strongly suppressed spectral weight at their backside, reminiscent of the mysterious Fermi arcs observed in underdoped cuprates. Let us see how this comes about for the hole-pockets related to particles with spin up. Their contribution to the spectral weight at  \( \omega=0 \)  is given by  \( U_{\mathbf{k},11}^{2}\delta(E_{\mathbf{k},1}) \) , where  \( U_{\mathbf{k},11}^{2}=A^{2}/(A^{2}+\xi_{\mathbf{k}}^{2}) \)  for  \( E_{k,1}=0 \) . From Fig. 1 it is clear that a large fraction of the inner side of the pockets is very close to the bare Fermi surface, where  \( \xi_{k}=0 \) . Hence  \( U_{k,11}^{2} \)  and thus the spectral weight there is almost one. The back side of the pocket is remote from the bare Fermi surface so that  \( A<\xi_{k} \)  and the spectral weight is thus quite small. A similar spectral function, albeit with fourfold rotation symmetry, is obtained in the commensurate case for  \( \eta=0 \) .

Hall coefficient.— The Hall coefficient is defined as  \( R_{H} = \sigma_{H} / (\sigma_{xx} \sigma_{yy}) \) , where  \( \sigma_{H} \)  is the Hall conductivity and  \( \sigma_{\alpha\alpha} \)  is the longitudinal conductivity in direction  \( \alpha \) . We compute the conductivities in a relaxation time approximation with a momentum independent scattering time  \( \tau \) . Neglecting “interband” scattering between the two quasi-particle bands  \( E_{k,1} \)  and  \( E_{k},2 \) , the conductivities in the spiral state are given by the same expressions as for non-interacting two-band systems [34]. Although the magnetic fields applied in the recent experiments by
 
![](./images/867747121321738940_5.jpg)

Figure 2: Hall number  \( n_{H} \)  as a function of doping for  \( t' = -0.35 \) . Results for a linear dependence,  \( A(p) \sim (p^{*} - p) \) , and a square root dependence,  \( A(p) \sim \sqrt{p^{*} - p} \) , where  \( p^{*} = 0.19 \)  in both cases, are labeled as “Lin” and “Sqrt”, respectively. The thin lines mark  \( n_{H} = p \)  and  \( 1 + p \) .

Badoux et al. [4] are impressively high, the product  \( \omega_{c}\tau \)  is still small since the relaxation time  \( \tau \)  is rather short ( \( \omega_{c} = \text{cyclotron frequency} \) ). In the so-called weak-field limit  \( \omega_{c}\tau \ll 1 \) , one obtains [34]

 \[ \sigma_{\alpha\alpha}=e^{2}\tau\sum_{i=1,2}\int\frac{d^{2}\boldsymbol{k}}{(2\pi)^{2}}\frac{\partial^{2}E_{\boldsymbol{k},i}}{\partial k_{\alpha}^{i}{}^{2}}n_{F}(E_{\boldsymbol{k},i}), \quad (6) \] 

 \[ \begin{align*}\sigma_{H}&=-e^{3}\tau^{2}\sum_{i=1,2}\int\frac{d^{2}\boldsymbol{k}}{(2\pi)^{2}}\\&\quad\times\Big[\frac{\partial^{2}E_{\boldsymbol{k},i}}{\partial k_{x}^{2}}\frac{\partial^{2}E_{\boldsymbol{k},i}}{\partial k_{y}^{2}}-\Big(\frac{\partial^{2}E_{\boldsymbol{k},i}}{\partial k_{x}\partial k_{y}}\Big)^{2}\Big]n_{F}(E_{\boldsymbol{k},i}).\end{align*} \quad (7) \] 

Note that the  \( \tau \) -dependence cancels in the Hall coefficient  \( R_{H} \) . The Hall number is defined as  \( n_{H} = (R_{H}e)^{-1} \) . In special cases such as parabolic dispersions, or for generic band structures with closed Fermi surfaces in the high-field limit  \( \omega_{c}\tau \gg 1 \) , the Hall number is simply given by the charge carrier density [35].

Results for the doping dependence of  \( n_{H} \)  are shown for different values of the antiferromagnetic gap in Fig. 2. At small doping,  \( n_{H} \)  is roughly given by the hole density p. Near  \( p^{*} = 0.19 \) ,  \( n_{H} \)  crosses over to  \( 1 + p \) . In the weak-field limit, the width of this crossover depends on the size of the antiferromagnetic gap. Larger gaps, or a square root doping dependence of the gap, lead to a sharper crossover. In the crossover region, the Fermi surface consists of hole and electron pockets, which is similar to the commensurate case and the YRZ scenarios studied in Ref. [14].

In the high field limit  \( \omega_{c}\tau \gg 1 \)  and at zero temperature,  \( n_{H} \)  is expected to be equal to the sum of the charge

![](./images/867747121321738940_6.jpg)

(a)

![](./images/867747121321738940_7.jpg)

(b)

Figure 3: Comparison between hole Fermi pockets of (a) incommensurate and (b) commensurate antiferromagnetic states with hole density  \( p = 0.1 \)  for  \( t' = -0.35 \)  and A = 0.7.  \( \eta = 0.1 \)  in a).

carrier densities of all Fermi pockets weighted by their sign, which is equal to the doping level p. One would thus expect a jump in  \( n_{H} \)  from p to  \( 1+p \)  in the high-field limit. The width of the crossover at weak and intermediate fields depends on the Fermi surface geometry, temperature, and the field strength.

Quantum oscillations.— The measurements of the Hall coefficient by Badoux et al. [4] are consistent with both a commensurate Néel state and an incommensurate spiral state. The Hall signal involves a sum over all Fermi surface sheets. For sufficiently high fields, the Hall number is given by the sum over all areas enclosed by the Fermi surface sheets, with electron-like Fermi surfaces counting negatively. Luttinger's theorem then implies that the Hall number is equal to doping p, irrespective of the incommensurability.

As an example, in Fig. 3 we show Fermi surfaces for a Néel state and an incommensurate spiral state at p = 0.1 for parameters where only hole pockets appear. In the Néel state, the hole density is given by

 \[ p=\sum_{\sigma=\uparrow,\downarrow}\int_{\mathrm{MBZ}}\frac{d^{2}\boldsymbol{k}}{(2\pi)^{2}}\Theta(E_{\boldsymbol{k},1})=\int_{\mathrm{BZ}}\frac{d^{2}\boldsymbol{k}}{(2\pi)^{2}}\Theta(E_{\boldsymbol{k},1}), \quad (8) \] 

where integrals marked with MBZ and BZ are over the magnetic and full Brillouin zone, respectively. In the spiral state, one has

 \[ p=\int_{\mathrm{B Z}}\frac{d^{2}\pmb{k}}{(2\pi)^{2}}\Theta(E_{\pmb{k},1}). \quad (9) \] 

The integrals measure the area of the hole pockets. The total area is the same in both cases and is determined by p.

However, the single pockets in the spiral state are twice as large as the pockets in the Néel state. Spiral states could therefore be distinguished by quantum oscillations in the magnetic field dependence, as pointed
 
![](./images/867747121321738940_8.jpg)

(a)

![](./images/867747121321738940_9.jpg)

(b)

Figure 4: Reconstructed quasi-particle Fermi surface due to spiral antiferromagnetic and charge-density wave order (red). The symmetry of the order parameter of the latter is a) s-wave and b) d-wave. The parameters are  \( t' = -0.35 \) ,  \( p \approx 0.12 \) ,  \( \eta = 0.125 \)  and A = 0.9 for both and a) C = 0.15 and b) C = 0.

out previously by Sebastian et al. [33]. For  \( \omega_{c}\tau > 1 \) , the magnetic susceptibility and other response quantities exhibit periodic oscillations as a function of  \( B^{-1} \)  due to Landau quantization [35]. Each closed Fermi surface sheet yields a signal with an oscillation frequency

 \[ F=\left(\Delta B^{-1}\right)^{-1}=\frac{\hbar S}{2\pi e}, \quad (10) \] 

where S is the enclosed momentum space area. The pocket areas in the commensurate Néel state with four hole pockets and the incommensurate spiral state with two hole pockets are

 \[ S_{\mathrm{CAF}}=\left(\frac{2\pi}{a}\right)^{2}\frac{p}{4}\qquad S_{\mathrm{IAF}}=\left(\frac{2\pi}{a}\right)^{2}\frac{p}{2}, \quad (11) \] 

respectively, where a is the lattice constant. The quantum oscillation frequencies of incommensurate spiral states are thus expected to be twice as large as those of Néel states at the same hole density. In particular, with the in-plane lattice constant of YBCO, a = 3.8Å, one obtains the oscillation frequencies  \( F_{CAF} = 7160T \cdot p \)  and  \( F_{IAF} = 14320T \cdot p \) .

Fermi surface for coexisting spiral antiferromagnetic and charge-density wave orders.— Cuprates show strong charge-density wave (CDW) correlations for  \( p \approx 0.12 \) , which become long-ranged in high magnetic fields [36–42]. In the field-induced ordered state, measurements of quantum oscillations and the Hall or Seebeck coefficient indicate a reconstruction of the Fermi surface into an electron Fermi pocket [43–46], and no additional hole pockets are found in single-layer materials [47]. Theoretical attempts to explain this reconstruction starting from a large hole Fermi surface [48] or the YRZ ansatz with small hole pockets [49] yielded additional open Fermi surface sheets or hole pockets. A reconstruction into one electron pocket could work starting from four Fermi arcs [50], but that proposal did not answer the question about their origin.

Coexisting spiral AF and bidirectional CDW order can be described by adding

 \[ H_{\mathrm{CDW}}=-C\sum_{\boldsymbol{k},\sigma,i}f(\boldsymbol{k}+\frac{\boldsymbol{q}_{i}}{2})\left(c_{\boldsymbol{k}+\boldsymbol{q}_{i}}^{\dagger}\sigma c_{\boldsymbol{k}\sigma}+c_{\boldsymbol{k}\sigma}^{\dagger}c_{\boldsymbol{k}+\boldsymbol{q}_{i}\sigma}\right) \quad (12) \] 

to Eq. (1), where C is the CDW order parameter. Bidirectional CDW order with ordering wave vectors  \( \mathbf{q}_{1} = (\pi/2, 0) \)  and  \( \mathbf{q}_{2} = (0, \pi/2) \)  is chosen as a simple approximation for the (incommensurate) CDW with a period of roughly four lattice constants that is seen in experiments. The form factor  \( f(\boldsymbol{k}) \)  is of predominantly d-wave symmetry ( \( f(\boldsymbol{k} = \cos k_{x} - \cos k_{y}) \)  in cuprates. We determine the Fermi surface for this symmetry and an onsite CDW with s-wave symmetry ( \( f(\boldsymbol{k}) = 1 \) ). In Fig. 4 we show that CDW order of both symmetries can reconstruct the two hole Fermi pockets of the spiral state (similar to those in Fig. 3a) into a single electron pocket. For d-wave CDW order with a smaller order parameter, the resulting Fermi surface is qualitatively similar to Fig. 4a [32]. Intriguingly, larger d-wave CDW order parameters, as in Fig. 4b, can give rise to additional Dirac cones in the spectrum. These arise from the inversion of two bands with different spin chirality, similar to topological insulators with spin-orbit coupling.

Conclusions.— We have shown that spiral antiferromagnetism may explain several features of the phenomenology of hole-doped cuprates. The spectral function of spiral antiferromagnetic states consists of hole pockets, which due to a strong momentum dependence of the spectral weight look like Fermi arcs. The Fermi surface reconstruction at a quantum critical point due to spiral antiferromagnetic order may explain the rapid change in the Hall number as recently observed near optimal doping in cuprate superconductors. In a doping regime where it is observed in cuprates, additional charge-density wave order further reconstructs the hole Fermi surface of the spiral antiferromagnetic state into a single electron pocket.

Metals with topological order can have the same charge transport properties as metals with magnetic order  \( [30] \) , but their fermionic quasiparticles carry a pseudospin with no Zeeman coupling, and so can be distinguished in quantum oscillation or low T photoemission.

The detection of spiral antiferromagnetic order, or quantum-fluctuating order in the topological metals, in hole-doped cuprates near optimal doping would signifi
 

cantly improve our understanding of the cuprate phase diagram. Incommensurate antiferromagnetism is expected from a theoretical point of view and is favorable over Néel-type antiferromagnetism. We propose quantum oscillation measurements to distinguish between Néel-type and spiral antiferromagnetic order.

Acknowledgments.— We would like to thank O. Sushkov, L. Taillefer and R. Zeyher for valuable discussions. AE acknowledges support from the German National Academy of Sciences Leopoldina through grant LPDS 2014-13. HY appreciates support by the Alexander von Humboldt Foundation and a Grant-in-Aid for Scientific Research from the Japan Society for the Promotion of Science. This research was supported by the NSF under Grant DMR-1360789 and MURI grant W911NF-14-1-0003 from ARO. Research at Perimeter Institute is supported by the Government of Canada through Industry Canada and by the Province of Ontario through the Ministry of Economic Development & Innovation. SS also acknowledges support from Cenovus Energy at Perimeter Institute.

[1] D. M. Broun, “What lies beneath the dome?” Nature Physics 4, 170 (2008).

[2] S. Sachdev, “Where is the quantum critical point in the cuprate superconductors?” physica status solidi (b) 247, 537 (2010), arXiv:0907.0008 [cond-mat.str-el].

[3] D. J. Scalapino, “A common thread: The pairing interaction for unconventional superconductors,” Rev. Mod. Phys. 84, 1383 (2012), arXiv:1207.4093 [cond-mat.supr-con].

[4] S. Badoux, W. Tabis, F. Laliberté, G. Grissonnanche, B. Vignolle, D. Vignolles, J. Béard, D. A. Bonn, W. N. Hardy, R. Liang, N. Doiron-Leyraud, L. Taillefer, and C. Proust, “Change of carrier density at the pseudogap critical point of a cuprate superconductor,” Nature 531, 210 (2016), arXiv:1511.08162 [cond-mat.supr-con].

[5] F. Laliberte, W. Tabis, S. Badoux, B. Vignolle, D. Destraz, N. Momono, T. Kurosawa, K. Yamada, H. Takagi, N. Doiron-Leyraud, C. Proust, and L. Taillefer, “Origin of the metal-to-insulator crossover in cuprate superconductors,” ArXiv e-prints (2016), arXiv:1606.04491 [cond-mat.supr-con].

[6] C. Collignon, S. Badoux, S. A. A. Afshar, B. Michon, F. Laliberte, O. Cyr-Choiniere, J.-S. Zhou, S. Licciardello, S. Wiedmann, N. Doiron-Leyraud, and L. Taillefer, “Fermi-surface transformation across the pseudogap critical point of the cuprate superconductor  \( La_{1.6}-xNd_{0.4}Sr_{x}CuO_{4} \) ,” ArXiv e-prints (2016), arXiv:1607.05693 [cond-mat.supr-con].

[7] S. Badoux, S. A. A. Afshar, B. Michon, A. Ouellet, S. Fortier, D. LeBoeuf, T. P. Croft, C. Lester, S. M. Hayden, H. Takagi, K. Yamada, D. Graf, N. Doiron-Leyraud, and L. Taillefer, “Critical doping for the onset of Fermi-surface reconstruction by charge-density-wave order in the cuprate superconductor  \( La_{2-x}Sr_{x}CuO_{4} \) ,”

Phys. Rev. X 6, 021004 (2016), arXiv:1512.00292 [cond-mat.supr-con].

[8] B. J. Ramshaw, S. E. Sebastian, R. D. McDonald, J. Day, B. S. Tan, Z. Zhu, J. B. Betts, R. Liang, D. A. Bonn, W. N. Hardy, and N. Harrison, “Quasiparticle mass enhancement approaching optimal doping in a high-Tc superconductor,” Science 348, 317 (2015), arXiv:1409.3990 [cond-mat.supr-con].

[9] K.-Y. Yang, T. M. Rice, and F.-C. Zhang, “Phenomenological theory of the pseudogap state,” Phys. Rev. B 73, 174501 (2006), arXiv:cond-mat/0602164 [cond-mat.supr-con].

[10] R. K. Kaul, A. Kolezhuk, M. Levin, S. Sachdev, and T. Senthil, “Hole dynamics in an antiferromagnet across a deconfined quantum critical point,” Phys. Rev. B 75, 235122 (2007), cond-mat/0702119.

[11] Y. Qi and S. Sachdev, “Effective theory of Fermi pockets in fluctuating antiferromagnets,” Phys. Rev. B 81, 115129 (2010), arXiv:0912.0943 [cond-mat.str-el].

[12] S. Chatterjee and S. Sachdev, “A fractionalized Fermi liquid with bosonic chargons as a candidate for the pseudogap metal,” ArXiv e-prints (2016), arXiv:1607.05727 [cond-mat.str-el].

[13] S. Caprara, C. Di Castro, G. Seibold, and M. Grilli, “Dynamical charge density waves rule the phase diagram of cuprates,” ArXiv e-prints (2016), arXiv:1604.07852 [cond-mat.supr-con].

[14] J. G. Storey, “Hall effect and Fermi surface reconstruction via electron pockets in the high-Tc cuprates,” Europhys. Lett. 113, 27003 (2016), arXiv:1512.03112 [cond-mat.supr-con].

[15] D. Haug, V. Hinkov, A. Suchaneck, D. S. Inosov, N. B. Christensen, C. Niedermayer, P. Bourges, Y. Sidis, J. T. Park, A. Ivanov, C. T. Lin, J. Mesot, and B. Keimer, "Magnetic-field-enhanced incommensurate magnetic order in the underdoped high-temperature superconductor  \( YBa_{2}Cu_{3}O_{6.45} \) ," Phys. Rev. Lett. 103, 017001 (2009), arXiv:0902.3335 [cond-mat.str-el].

[16] D. Haug, V. Hinkov, Y. Sidis, P. Bourges, N. B. Christensen, A. Ivanov, T. Keller, C. T. Lin, and B. Keimer, "Neutron scattering study of the magnetic phase diagram of underdoped  \( YBa_{2}Cu_{3}O_{6+x} \) ," New J. Phys. 12, 105006 (2010), arXiv:1008.4298 [cond-mat.str-el].

[17] B. I. Shrainman and E. D. Siggia, “Spiral phase of a doped quantum antiferromagnet,” Phys. Rev. Lett. 62, 1564 (1989).

[18] K. Machida, “Magnetism in  \( La_{2}CuO_{4} \)  based compounds,” Physica C: Superconductivity 158, 192 (1989).

[19] M. Kato, K. Machida, H. Nakanishi, and M. Fujita, "Soliton lattice modulation of incommensurate spin density wave in two dimensional hubbard model -a mean field study-," J. Phys. Soc. Jpn. 59, 1047 (1990).

[20] C. L. Kane, P. A. Lee, T. K. Ng, B. Chakraborty, and N. Read, “Mean-field theory of the spiral phases of a doped antiferromagnet,” Phys. Rev. B 41, 2653 (1990).

[21] H. J. Schulz, “Incommensurate antiferromagnetism in the two-dimensional Hubbard model,” Phys. Rev. Lett. 64, 1445 (1990).

[22] A. V. Chubukov and D. M. Frenkel, “Renormalized perturbation theory of magnetic instabilities in the two-dimensional Hubbard model at small doping,” Phys. Rev. B 46, 11884 (1992).
 

[23] A. V. Chubukov and K. A. Musaelian, “Magnetic phases of the two-dimensional Hubbard model at low doping,” Phys. Rev. B 51, 12605 (1995), arXiv:cond-mat/9501036.

[24] V. N. Kotov and O. P. Sushkov, “Stability of the spiral phase in the two-dimensional extended t-J model,” Phys. Rev. B 70, 195105 (2004), arXiv:cond-mat/0407242.

[25] O. P. Sushkov and V. N. Kotov, “Superconducting spiral phase in the two-dimensional t-J model,” Phys. Rev. B 70, 024503 (2004), arXiv:cond-mat/0310635.

[26] M. Raczkowski, R. Frésard, and A. M. Oles, “Interplay between incommensurate phases in the cuprates,” Europhys. Lett. 76, 128 (2006), arXiv:cond-mat/0606059.

[27] P. A. Igoshev, M. A. Timirgazin, A. A. Katanin, A. K. Arzhnikov, and V. Y. Irkhin, “Incommensurate magnetic order and phase separation in the two-dimensional Hubbard model with nearest- and next-nearest-neighbor hopping,” Phys. Rev. B 81, 094407 (2010), arXiv:0912.0992 [cond-mat.str-el].

[28] H. Yamase, A. Eberlein, and W. Metzner, “Coexistence of incommensurate magnetism and superconductivity in the two-dimensional Hubbard model,” Phys. Rev. Lett. 116, 096402 (2016), arXiv:1507.00560 [cond-mat.str-el].

[29] Yuxuan Wang (private communication) has noted the possibility that co-existing spin and charge density wave orders can yield a single electron pocket.

[30] S. Sachdev and D. Chowdhury, “The novel metallic states of the cuprates: topological Fermi liquids and strange metals,” ArXiv e-prints (2016), arXiv:1605.03579 [cond-mat.str-el].

[31] J. L. Tallon and J. W. Loram, “The doping dependence of  \( T^{*} \)  - what is the real high-Tc phase diagram?” Physica C: Superconductivity 349, 53 (2001), arXiv:cond-mat/0005063.

[32] More details can be found in the Supplementary Material.

[33] S. E. Sebastian, N. Harrison, E. Palm, T. P. Murphy, C. H. Mielke, R. Liang, D. A. Bonn, W. N. Hardy, and G. G. Lonzarich, “A multi-component Fermi surface in the vortex state of an underdoped high-Tc superconductor,” Nature 454, 200 (2008).

[34] P. Voruganti, A. Golubentsev, and S. John, “Conductivity and Hall effect in the two-dimensional Hubbard model,” Phys. Rev. B 45, 13945 (1992).

[35] N. Ashcroft and N. Mermin, Solid State Physics (Holt, Rinehart and Winston, New York, 1976).

[36] T. Wu, H. Mayaffre, S. Kramer, M. Horvatic, C. Berthier, W. N. Hardy, R. Liang, D. A. Bonn, and M.-H. Julien, "Magnetic-field-induced charge-stripe order in the high-temperature superconductor  \( YBa_{2}Cu_{3}O_{y} \) ," Nature 477, 191 (2011), arXiv:1109.2011 [cond-mat.supr-con].

[37] T. Wu, H. Mayaffre, S. Krämer, M. Horvatić, C. Berthier, P. L. Kuhns, A. P. Reyes, R. Liang, W. N. Hardy, D. A. Bonn, and M.-H. Julien, “Emergence of charge order from the vortex state of a high-temperature superconductor,” Nat Commun 4, 2113 (2013), arXiv:1307.2049 [cond-mat.supr-con].

[38] G. Ghiringhelli, M. Le Tacon, M. Minola, S. Blanco-Canosa, C. Mazzoli, N. B. Brookes, G. M. De Luca, A. Frano, D. G. Hawthorn, F. He, T. Loew, M. M. Sala, D. C. Peets, M. Salluzzo, E. Schierle, R. Sutarto, G. A. Sawatzky, E. Weschke, B. Keimer, and

L. Braicovich, “Long-range incommensurate charge fluctuations in  \( (\mathrm{Y},\mathrm{Nd})\mathrm{Ba}_{2}\mathrm{Cu}_{3}\mathrm{O}_{6+x} \) ,” Science 337, 821 (2012), arXiv:1207.0915 [cond-mat.str-el].

[39] D. LeBoeuf, S. Kramer, W. N. Hardy, R. Liang, D. A. Bonn, and C. Proust, “Thermodynamic phase diagram of static charge order in underdoped  \( YBa_{2}Cu_{3}O_{y} \) ,” Nat Phys 9, 79 (2013), arXiv:1211.2724 [cond-mat.supr-con].

[40] S. Blanco-Canosa, A. Frano, T. Loew, Y. Lu, J. Porras, G. Ghiringhelli, M. Minola, C. Mazzoli, L. Braicovich, E. Schierle, E. Weschke, M. Le Tacon, and B. Keimer, “Momentum-dependent charge correlations in  \( YBa_{2}Cu_{3}O_{6+\delta} \)  superconductors probed by resonant x-ray scattering: Evidence for three competing phases,” Phys. Rev. Lett. 110, 187001 (2013), arXiv:1212.5580 [cond-mat.supr-con].

[41] R. Comin, R. Sutarto, F. He, E. H. da Silva Neto, L. Chauviere, A. Frano, R. Liang, W. N. Hardy, D. A. Bonn, Y. Yoshida, H. Eisaki, A. J. Achkar, D. G. Hawthorn, B. Keimer, G. A. Sawatzky, and A. Damascelli, “Symmetry of charge order in cuprates,” Nat. Mater. 14, 796 (2015), arXiv:1402.5415 [cond-mat.supr-con].

[42] S. Gerber, H. Jang, H. Nojiri, S. Matsuzawa, H. Yasumura, D. A. Bonn, R. Liang, W. N. Hardy, Z. Islam, A. Mehta, S. Song, M. Sikorski, D. Stefanescu, Y. Feng, S. A. Kivelson, T. P. Devereaux, Z.-X. Shen, C.-C. Kao, W.-S. Lee, D. Zhu, and J.-S. Lee, “Three-dimensional charge density wave order in  \( YBa_{2}Cu_{3}O_{6.67} \)  at high magnetic fields,” Science 350, 949 (2015), arXiv:1506.07910 [cond-mat.str-el].

[43] N. Doiron-Leyraud, C. Proust, D. LeBoeuf, J. Levallois, J.-B. Bonnemaison, R. Liang, D. A. Bonn, W. N. Hardy, and L. Taillefer, “Quantum oscillations and the Fermi surface in an underdoped high-Tc superconductor,” Nature 447, 565 (2007), arXiv:0801.1281 [cond-mat.supr-con].

[44] D. LeBoeuf, N. Doiron-Leyraud, J. Levallois, R. Daou, J.-B. Bonnemaison, N. E. Hussey, L. Balicas, B. J. Ramshaw, R. Liang, D. A. Bonn, W. N. Hardy, S. Adachi, C. Proust, and L. Taillefer, “Electron pockets in the Fermi surface of hole-doped high- \( T_{c} \)  superconductors,” Nature 450, 533 (2007), arXiv:0806.4621 [cond-mat.supr-con].

[45] N. Doiron-Leyraud, S. Lepault, O. Cyr-Choinière, B. Vignolle, G. Grissonnanche, F. Laliberté, J. Chang, N. Barisić, M. K. Chan, L. Ji, X. Zhao, Y. Li, M. Greven, C. Proust, and L. Taillefer, “Hall, Seebeck, and Nernst coefficients of underdoped  \( HgBa_{2}CuO_{4+\delta} \) : Fermi-surface reconstruction in an archetypal cuprate superconductor,” Phys. Rev. X 3, 021019 (2013), arXiv:1210.8411 [cond-mat.supr-con].

[46] J. B. Kemper, O. Vafek, J. B. Betts, F. F. Balakirev, W. N. Hardy, R. Liang, D. A. Bonn, and G. S. Boebinger, “Thermodynamic signature of a magnetic-field-driven phase transition within the superconducting state of an underdoped cuprate,” Nat Phys 12, 47 (2016), arXiv:1403.3702 [cond-mat.supr-con].

[47] M. K. Chan, N. Harrison, R. D. McDonald, B. J. Ramshaw, K. A. Modic, N. Barisic, and M. Greven, "Single reconstructed Fermi surface pocket in an underdoped single layer cuprate superconductor," (2016), arXiv:1606.02772 [cond-mat.supr-con].
 

[48] A. Allais, D. Chowdhury, and S. Sachdev, “Connecting high-field quantum oscillations to zero-field electron spectral functions in the underdoped cuprates,” Nat. Commun. 5, 5771 (2014), 10.1038/ncomms6771, arXiv:1406.0503 [cond-mat.str-el].

[49] L. Zhang and J.-W. Mei, “Quantum oscillation as di-

agnostics of pseudogap state in underdoped cuprates," Europhys. Lett. 114, 47008 (2016), arXiv:1411.2098 [cond-mat.str-el].

[50] N. Harrison, “Number of holes contained within the fermi surface volume in underdoped high-temperature superconductors,” Phys. Rev. B 94, 085129 (2016), arXiv:1605.03381 [cond-mat.str-el].

## Supplementary information

In this Supplementary Material we provide details on the dependence of the spiral antiferromagnetic gap A and the incommensurability  \( \eta \)  on the hole doping concentration p. We also show the quasi-particle Fermi surface for a state with spiral antiferromagnetism and charge-density wave order with d-wave symmetry for an additional set of parameters.

In Fig. 5, we show the doping dependence of the spiral antiferromagnetic gap A that we assume in the main text. In order to study the influence of how the antiferromagnetic gap closes, we consider gaps that vanish as  \( A(p) \sim p^{*} - p \)  or  \( \sim \sqrt{p^{*} - p} \) , with  \( p^{*} = 0.19 \) .

![](./images/867747121321738940_10.jpg)

Figure 5: Antiferromagnetic gap A as a function of doping p.

In Fig. 6, we show the doping dependence of the incommensurability  \( \eta \)  that parametrizes the antiferromagnetic ordering wave vector as  \( \mathbf{Q} = (\pi - 2\pi\eta, \pi) \) .  \( \eta \)  was determined by minimization of the fermionic contribution to the ground state energy for any given p and  \( A(p) \) . For the parameters considered,  \( \eta \)  is equal to p to a very good approximation.

![](./images/867747121321738940_11.jpg)

Figure 6: Incommensurability  \( \eta \)  as a function of doping. The grey line marks  \( \eta = p \) .

In Fig. 7, we show the quasi-particle Fermi surface for coexisting spiral antiferromagnetic and charge-density wave order, the latter having d-wave symmetry. In comparison to Fig. 4b in the main text, the charge-density wave gap is
 

smaller. The Fermi surface is reconstructed into one electron pocket, but no Dirac cones appear close to the Fermi surface.

![](./images/867747121321738940_12.jpg)

Figure 7: Reconstructed quasi-particle Fermi surface due to spiral antiferromagnetic and d-wave charge-density wave order (red). The parameters are  \( t' = -0.35 \) ,  \( p \approx 0.11 \) ,  \( \eta = 0.125 \) , A = 0.8 and C = 0.3. The black dashed lines show the Fermi surface of the spiral antiferromagnetic state after backfolding to the reduced Brillouin zone (i.e. C = 0). The electron pocket is shaded in grey.
 
