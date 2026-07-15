# Electronic Structure of Twin Boundaries in 3C-SiC, Si, and Diamond

Hisaomi Iwata $^{1,2)}$, Ulf Lindefelt $^{1,2,3)}$, Sven Öberg $^{4)}$, and Patrick R. Briddon $^{5)}$

$^{1)}$Department of Physics and Measurement Technology, Linköping University,
SE-58183 Linköping, Sweden
$^{2)}$Department of Microelectronics and Information Technology, Royal Institute of Technology,
KTH Electrum 229, SE-16440 Kista, Sweden
$^{3)}$ABB Group Service Center, ABB Corporate Research, SE-72178 Västerås, Sweden
$^{4)}$Department of Mathematics, Luleå University of Technology, SE-97187 Luleå, Sweden
$^{5)}$Department of Physics, University of Newcastle upon Tyne, NE1 7RU, UK

**Keywords:** 3C-SiC, Stacking Faults, First-principles Calculation, Twin boundaries

**Abstract:** We report on a first-principles band structure calculation of twin boundaries in 3C-SiC, Si, and diamond, based on the density functional theory in the local density approximation. It is found that the electron wave functions belonging to the conduction and valence band edge states in 3C-SiC tend to be localized almost exclusively on different sides of the boundaries, while there is no such feature in Si and diamond. We have interpreted these localization and segregation phenomena as a consequence of the electrostatic field caused by the spontaneous polarization due to the hexagonal symmetry around twin boundaries. A mechanism for the creation of twin boundaries, i.e., propagation of partial dislocations in neighboring basal planes, has been investigated using total energy calculations, and it has been realized that the double-intrinsic-stacking-fault structure in 3C-SiC, coinciding with the extrinsic stacking faults, is much energetically favored.

## Introduction
Because of the recent progress of the crystal growth technology for 3C-SiC [1], this polytype has attracted considerable attention as a choice for SiC-based electronic devices. However, 3C-SiC has been investigated much less intensively than 4H- and 6H-SiC polytypes. In this work, we have studied the electronic structure of one type of twin boundary (TB) in 3C-SiC which can be formed without breaking any bonds, using an *ab initio* supercell approach. Electronic structures and energies of TBs in Si and diamond are also calculated [2,3].

TBs are quite common structural defects in 3C-SiC [1,4]. In terms of the ABC stacking notation, the normal stacking sequence of 3C-SiC is ...ABCABC..., where A, B, and C correspond to Si-C bi-layers at A-, B-, and C-sites, respectively. It is possible to have a stacking fault during crystal growth along the [111]-direction. If a C-layer, instead of a B-layer, occurs immediately after an A-layer, the growth sequence can become ...ACBACB..., and a TB is formed. Figure 1 shows a schematic illustration of the TB viewed from a [1-10]-direction ([11-20]-direction in the hexagonal symmetry). As will be discussed later, the motion of successive partial dislocations can create TBs in the perfect crystals as well [5].

Also, we have recently reported a series of theoretical investigations on stacking disorders in SiC [6,7] in order to shed some light on the electronic degradation problem in SiC-based bipolar devices [8,9]. A study of TBs can be a cornerstone to understand the nature of more complicated stacking disorders since the TB is, in a sense, the simplest planar defect.

## Method and Model
### A. Structural Model
Apart from the possibility to have TBs during crystal growth, it is quite possible to introduce TBs by pure partial dislocation glide [5]. To see this, let us introduce the Hägg notation since it is usually clearer than the ABC-notation. All the SiC polytypes can be expressed as the sequence of two kinds of bi-layers composed of, so called, 'normal' or 'twinned' tetrahedrons (see

Fig.1). Let us denote a bi-layer of normal tetrahedrons with a '+' sign and that of twinned with a '-' sign. Then, for example, the crystal containing one TB in Fig.1 can be expressed as ...++++++++-------... Of course, a perfect 3C-SiC is ...++++++... or ...-------... Now, we are ready to explore some more complicated stacking disorders in SiC. In SiC a complete dislocation is usually dissociated into two partial dislocations, having a stacking fault (SF) in between. Then in such a region, the stacking sequence becomes ...+++++--+++... [1SF]. This is called 'intrinsic' SF. If another partial is introduced immediately above or below the first SF, the stacking sequence will become ...+++++--+++.... [2SF]. By inserting par- tials in the adjacent SF-plane one after another, one can obtain a stacking sequence like ...+++++(-----...----)+++... [nSF], where the sequence in the parentheses is also perfect 3C-SiC, i.e., two TBs have been created. In order to shed some light on this mechanism in 3C-SiC, we have calculated the total energies of supercells with nSF (n=1-10), and deter- mined the n:th SF energy by

$$
\gamma_{n}=\frac{E(n)-E(n-1)}{A},
$$

where A is the interface area, E(n) is the total energy of the crystal with nSF. E(0) is the total energy of the perfect crystal.

All these planar defects are modeled using 120-atom supercells. Note that when modeling a single isolated TB, each supercell must have two TBs, i.e., it corresponds to 60H-SiC, 60H-Si, or 60H-diamond. TBs therefore repeat after 30 bi-layers along the c-axis and spread infinitely perpendicular to the c-axis. Single and multiple SFs [nSF] can be modeled without repeating twice in the supercell. We expect that these supercells are sufficiently large to extract some essential information about these extended defects.

### B. Computational Method
In our LDA-DFT method, wave functions are expanded in a basis set of real-space Gaussians with s-, p-, and d-characters while ion-electron interactions are described by norm-conserving pseudopotentials with non-linear core correction. Brillouin zone integrations are replaced by six Monkhorst-Pack k-points in the basal plane

## Results and Model
Our calculations have shown that the electron densities belonging to the top of the valence band and to the bottom of the conduction band seem to be localized almost exclusively on different sides of the TB in 3C-SiC, as shown in Fig.2, whereas no such wave function localization and segregation takes place in Si and diamond. We interpret this segregation and localization of the wave functions at the band edges in 3C-SiC as a consequence of the electrostatic field caused by the spontaneous polarization (SP). Qteish et. al. reported that charge transfer takes place between the non-equivalent bonds in the hexagonal SiC polytypes and results in an electric dipole moment along the negative c-direction (as defined in Fig.1) which is quite strongly lo- calized around the hexagonal turns [10]. (In the cubic symmetry, the four tetrahedral bonds are equivalent.) Based on these results, we show schematically in Fig.3 the SP-induced potential experienced by an electron. From this figure it is quite understandable that the conduction band electron tends to be localized below (to the left of) the TB due to the attractive portion of the potential, and similarly that the electronic state at the top of the valence band is pushed into the band gap by the repulsive part of the potential and gets localized above (to the right of) the TB. Note that such SP cannot take place in Si and diamond since a reflection symmetry around the hexagonal turn remains. Our result for Si seems to be consistent with the previous band-structure calculation of Ref.2. Since the modification of band edges in Si and diamond due to the occurrence of TBs is only subtle and minor, we expect these planar defects to be almost *electrically inactive*. On the other hand, TBs in 3C-SiC can modify band edge states to

some extent because of the SP around the hexagonal turns. These near-edge states, however, are extremely shallow and very weekly localized. We therefore expect that isolated TBs themselves in 3C-SiC cannot damage device performance in an obvious way like SFs in 4H- and 6H-SiC.

We have calculated the formation energies of TBs in 3C-SiC, Si, and diamond to be -14.5,5.8, and $105.5 \mathrm{~mJ} / \mathrm{m}^{2}$, respectively, all atomic positions in the supercells having been fully relaxed to minimize the total energy. Here, the formation energy is defined as the energy cost per unit interface area to have one TB in the crystal. These values of Si and diamond are in very good agreement with Ref.3, where the formation energies were extracted from the ANNNI model and found to be 8.4 and $105.2 \mathrm{~mJ} / \mathrm{m}^{2}$ for TBs in Si and diamond, respectively.

Figure 4 shows the n:th SF energy (without intra-supercell relaxation). In Fig.4, it is no- ticeable that the 2nd SF energy has a large negative value while n:th (n>4) SF energy are around zero, leading to an expectation that this double-intrinsic-SF structure, or even the tri- ple-intrinsic-SF structure, is quite common in3C-SiC. The double-intrinsic-SF structure co- incides with the extrinsic SF in cubic materials. In Ref. 11, the intrinsic and extrinsic SF ener- gies in 3C-SiC were calculated to be -3.4 and $-28 ~mJ / m^{2}$ , and from those values the $2 nd SF$  energy becomes $-25 ~mJ / m^{2}$ . This agrees well with our calculation. These calculated values lead us to believe that: an isolated intrinsic SF can induce the 2nd SF in the adjacent planes(immediately below or above the first SF-plane), i.e., the partial dislocation in the2nd SF-plane can penetrate the crystal very easily.

![](./images/811868421829427201_1.jpg)

Fig.4. The n:th SF energy in 3C-SiC.

## Acknowledgement
The authors gratefully thank the Swedish Foundation for Strategic Research (SSF) for financial support and the National Supercomputer Center (NSC), Sweden, for computer time. The au- thors are also grateful to P. Pirouz for suggesting to do the calculation corresponding to Fig.4.

## References
[1] See, e.g., H. Nagasawa, T. Kawahara, and K. Yagi, Mater. Sci. Forum 389-393 (2002), p.319; T. Yamada and K. M. Itoh, ibid, p.675; H. Nagasawa and K. Yagi, Phys. Stat. Sol. (b) 202 (1997), p.335.
[2] Z. Ikonic, G. P. Srivastava, and J. C. Inkson, Phys. Rev. B 48 (1993), p.17181; Phys. Rev. B 52 (1995), p.14078.
[3] C. Raffy, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 66 (2002), p.075201.
[4] See, e.g., C. Long, S. A. Ustin, and W. Ho, J. Appl. Phys. 86 (1999), p.2509.
[5] P. Pirouz and J. W. Yang, UItramicroscopy 51 (1993), p.189; P. Pirouz, Solid State Phenom. 56(1997), p.107; P. Pirouz, Mater. Sci. Forum 264-268 (1998), p.399.
[6] H. Iwata, U. Lindefelt, S. Oberg, and P. R. Briddon, Phys. Rev. B 65 (2002), p.033203; Mater. Sci.Forum 389-393 (2002), p.529; Mater. Sci. Forum 389-393 (2002), p.533; Mater. Sci. Forum 389-393(2002), p.439; J. Phys.: Condens. Matter 14 (2002), p. 12733; J. Appl. Phys. (2003), in press.
[7] U. Lindefelt, H. Iwata, S. Oberg, and P. R. Briddon, submitted to Phys. Rev. B.
[8] H. Lendenmann, F. Dahlquist, N. Johansson, R. Soderholm, P. A. Nilsson, J. P. Bergman, and P. Skytt, Mater. Sci. Forum 353-356 (2000), p.727.
[9] J. P. Bergman, H. Lendenmann, P. A. Nilsson, U. Lindefelt, and P. Skytt, Mater. Sci. Forum 353-356(2000), p.299.
[10] A. Qteish, V. Heine, and R. J. Needs, Phys. Rev. B 45 (1992), p.6534; Phys. Rev. B 45 (1992), p.6376.
[11] P. Kckell, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 58 (1998), p.1326.

![](./images/811868421829427201_2.jpg)

Fig. 1. Stacking sequence around a TB viewed from a [11-20]-direction. Open (filled) circles denote Si (C) atoms. The tetrahedrons below (above) the twin boundary are called 'normal' ('twinned').

![](./images/811868421829427201_3.jpg)

Fig. 2. The squared wave function along the c-axis, $f(z)=\iint |\psi(x,y,z)|^2 dxdy$, in 60H-SiC where the integration for each value of z along the c-axis is performed in a basal plane within the supercell. (a) For the electron at the conduction band minimum at the M-point and (b) for the valence band maximum at the $\Gamma$-point. The corresponding stacking sequences are also shown.

![](./images/811868421829427201_4.jpg)

Fig.3. Schematic diagram of the potential experienced by an electron. The electric dipole moment caused by the spontaneous polarization around the hexagonal turn is directed to the opposite direction of the c-axis.

Silicon Carbide and Related Materials - 2002
10.4028/www.scientific.net/MSF.433-436

Electronic Structure of Twin Boundaries in 3C-SiC, Si and Diamond
10.4028/www.scientific.net/MSF.433-436.527

DOI References

[1] See, e.g., H. Nagasawa, T. Kawahara, and K. Yagi, Mater. Sci. Forum 389-393 (2002), p.319; T. amada and K. M. Itoh, ibid, p.675; H. Nagasawa and K. Yagi, Phys. Stat. Sol. (b) 202 (1997), p.335.
doi:10.4028/www.scientific.net/MSF.389-393.319

[2] Z. Ikonic, G. P. Srivastava, and J. C. Inkson, Phys. Rev. B 48 (1993), p.17181; Phys. Rev. B 52 (1995), .14078.
doi:10.1103/PhysRevB.52.14078

[3] C. Raffy, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 66 (2002), p.075201.
doi:10.1103/PhysRevB.66.075201

[4] See, e.g., C. Long, S. A. Ustin, and W. Ho, J. Appl. Phys. 86 (1999), p.2509.
doi:10.1063/1.371085

[5] P. Pirouz and J. W. Yang, Ultramicroscopy 51 (1993), p.189; P. Pirouz, Solid State Phenom. 56 1997), p.107; P. Pirouz, Mater. Sci. Forum 264-268 (1998), p.399.
doi:10.4028/www.scientific.net/MSF.264-268.399

[10] A. Qteish, V. Heine, and R. J. Needs, Phys. Rev. B 45 (1992), p.6534; Phys. Rev. B 45 (1992), .6376.
doi:10.1103/PhysRevB.45.6534

[1] See, e.g., H. Nagasawa, T. Kawahara, and K. Yagi, Mater. Sci. Forum 389-393 (2002), p.319; T. Yamada and K. M. Itoh, ibid, p.675; H. Nagasawa and K. Yagi, Phys. Stat. Sol. (b) 202 (1997), p.335.
doi:10.4028/www.scientific.net/MSF.389-393.319

[2] Z. Ikonic, G. P. Srivastava, and J. C. Inkson, Phys. Rev. B 48 (1993), p.17181; Phys. Rev. B 52 (1995), p.14078.
doi:10.1103/PhysRevB.52.14078

[3] C. Raffy, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 66 (2002), p.075201.
doi:10.1103/PhysRevB.66.075201

[5] P. Pirouz and J. W. Yang, Ultramicroscopy 51 (1993), p.189; P. Pirouz, Solid State Phenom. 56 (1997), p.107; P. Pirouz, Mater. Sci. Forum 264-268 (1998), p.399.
doi:10.4028/www.scientific.net/MSF.264-268.399

[10] A. Qteish, V. Heine, and R. J. Needs, Phys. Rev. B 45 (1992), p.6534; Phys. Rev. B 45 (1992), p.6376.
doi:10.1103/PhysRevB.45.6534