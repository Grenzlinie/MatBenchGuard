
# Accurate bandgaps of photovoltaic kesterites from first-principles DFT+U

Andrew C. Burgess \( ^{1,2,3} \) , Lórien MacEnulty \( ^{1,4} \) , Ethan D'Arcy \( ^{1} \) , David Gavin \( ^{1,2} \) , and David D. O'Regan \( ^{1,2*} \) 

 \( ^{1} \) School of Physics, Trinity College Dublin, The University of Dublin, Ireland

 \( ^{2} \) CRANN Institute and AMBER Research Centre,

Trinity College Dublin, The University of Dublin, Ireland

 \( ^{3} \) School of Physics, University College Dublin, Dublin 4, Ireland and

 \( ^{4} \) Université catholique de Louvain, Institute of Condensed Matter and Nanoscience, Chemin des Étoiles 8, B-1348 Louvain-la-Neuve, Belgium

Streamlined prediction of the electronic properties of photoactive materials warrants a Density Functional Theory (DFT) based approach that (i) yields reliable bandgaps, (ii) is free of empirically tuned parameters, and (iii) exhibits low computational overhead. Here we show that for  \( Cu_{2}ZnSeS_{4} \)  and  \( Cu_{2}ZnGeS_{4} \)  kesterite photovoltaic materials, all three of these demands are met by the DFT plus Hubbard U technique (DFT+U) with corrective parameters evaluated via minimum-tracking linear response. The predicted bandgaps are found to even marginally outperform those from the self-consistent GW approach. Key to this method's success is the application of Hubbard U corrections to all atomic subspaces that dominate the conduction and valence band edges, as opposed to the conventional approach of correcting 3d and 4f atomic states. Intriguingly, the inclusion of Hund's J corrections via the extended DFT+U+J functional significantly worsens these results. This underperformance can be ameliorated through the use of the Burgess-Linscott-O'Regan (BLOR) flat-plane based Hubbard U plus Hund's J functional, with bandgap predictions in close agreement with the conventional DFT+U method. The DFT+U method is also used to predict defect-induced changes to the bandgap and associated formation energies, in 1,728-atom supercells.

Keywords: kesterite, photovoltaic, DFT+U, DFT+U+J, bandgaps, defect-formation energies

The need to decarbonize the global economy is one of the greatest challenges faced by humanity in the twenty-first century. Both the European Union  \( [1] \)  and the United Kingdom  \( [2] \)  are committed to achieving net-zero greenhouse gas emissions by 2050. The wide-scale adoption of renewable energy technology will play a pivotal role in achieving this ambitious goal  \( [3] \) . Photovoltaic (PV) materials have already been identified as key components of the wider renewable energy sector and are forecast to become the primary source of renewable electricity by 2030  \( [4] \) . However, owing at least in part to the material's technological maturity, the commercial market is currently dominated by multicrystalline silicon-based PVs with a typical efficiency of  \( \sim20\% \)  at most. Improving the efficiency and lowering the cost of PV technology thus demands the exploration of alternative materials.

One class of promising candidates are the quaternary kesterite chalcogenides—among them the prototypical  \( Cu_{2}ZnSnS_{4} \)  (CZTS) and its relative,  \( Cu_{2}ZnGeS_{4} \)  (CZGS; see Fig. 1)—due to their geographically abundant and non-toxic elemental constituents [5, 6], high absorption coefficients ( \( >10^{4}~cm^{-1} \) ) [7] and near-optimal single junction bandgap of  \( \sim1.5~eV \)  [8]. Furthermore, similarities between fabrication techniques of these materials and CIGS ( \( CuIn_{x}Ga_{1-x}Se_{2} \) ) [9], their more advanced yet more expensive cousins, ensures that engineers can leverage existing industrial infrastructure to expedite their entry into the PV market [10, 11].

Despite periods of rapid improvement  \( [12, 13] \)  since the seminal work of Ito and Nakazawa  \( [14] \) , the record efficiency of kesterite-based solar cells remains low, at 15.8%  \( [15, 16] \) . This efficiency reaches less than half of the predicted Shockley–Queisser limit for these materials  \( [17] \) . Fortunately, kesterite bandgap energies have been shown to be quite cleanly manipulated by partial doping or alloy substitution  \( [18–22] \) . Unlocking improved cell efficiencies thus requires a deeper understanding of the electronic and atomistic structure of quaternary kesterite chalcogenides, an understanding that is potentially accessible through density functional theory (DFT) calculations. However, conventional approximate DFT calculations with local and semi-local exchange correlation functionals erroneously predict CZTS as being near metallic in character, with a bandgap of less than 0.25 eV  \( [23, 24] \) . Improved bandgap predictions, as best-practices among modelers of photoactive materials demand, can be achieved through deployment of hybrid functionals such as that of Heyd-Scuseria-Ernzerhof, (HSE)  \( [25] \) , albeit usually with a considerable increase in computational cost. Such an increase in cost makes the approach unsuitable for use in large simulation cells, which are required for accurate modeling of defects, or when sampling many configurations. The Hubbard U-corrected DFT (DFT+U) approach  \( [26–28] \)  offers a pragmatic alternative capable of yielding reliable bandgap predictions at comparable cost to the (semi-)local base functional that it is designed to correct.

Three DFT+U-type corrective functionals have been assessed in this study, namely the well-established DFT+U functional of Dudarev et al. [29], the extended DFT+U+J functional of Himmetoglu et al. [30] and the recently developed Burgess-Linscott-O'Regan (BLOR) functional [31]. The corrective functional of Dudarev et al.
 
![](2512.14548v1-images/1_0.jpg)

FIG. 1. CZGS demonstrating the general crystal structure of a quaternary chalcogenide  \( X_{2}ZnY S_{4} \)  in the kesterite phase, space group  \( I\bar{4} \) . The principle transition metal X=Cu is shown in gray, Zn is blue, Y=Sn, Ge in green, and S in yellow.

al. was designed to explicitly treat the effective electron-electron interaction within a selected subspace using an on-site interaction term inspired by the Hubbard model,

 \[ E_{\mathrm{i n t}}=\frac{U}{2}\sum_{\sigma,m,m^{\prime}}n_{m m}^{\sigma}n_{m^{\prime}m^{\prime}}^{\bar{\sigma}}+\frac{U-J}{2}\sum_{\sigma,m\neq m^{\prime}}n_{m m}^{\sigma}n_{m^{\prime}m^{\prime}}^{\sigma}, \quad (1) \] 

Subtracting off the double-counting correction and omitting the numerically fraught minority-spin term results in the simplified rotationally-invariant DFT+U+J functional given by

 \[ \begin{aligned}E_{\mathrm{u}}=&\frac{U-J}{2}\sum_{\sigma,m,m^{\prime}}n_{mm}^{\sigma}\delta_{mm^{\prime}}-n_{mm^{\prime}}^{\sigma}n_{m^{\prime}m}^{\sigma}\\&+\frac{J}{2}\sum_{\sigma,m,m^{\prime}}n_{mm^{\prime}}^{\sigma}n_{m^{\prime}m}^{\bar{\sigma}}.\end{aligned} \quad (5) \] 

In contrast to invoking an on-site interaction term and a double counting correction, the third functional considered there, the BLOR functional, is specifically designed to enforce the flat plane condition on localized subspaces, an exact condition of DFT which defines the shape of the where U and J are the subspace-averaged, screened Coulomb and exchange interactions—typically called the Hubbard U and Hund's J parameters and to which we will collectively refer as the Hubbard parameters—and  \( n_{mm}^{\sigma} \)  is the spin- \( \sigma \)  occupancy of orbital m in the selected subspace. However, in this model, said electron-electron interaction is assumed to have already been accounted for to a less favorable extent by the approximate Hartree and exchange correlation (Hxc) functional, which the DFT+U functional is designed to supplement. Dudarev et al. mitigate this issue by invoking a spin-polarized, fully-localized limit-type double counting correction to arrive at the following expression for their DFT+U-functional [32],

 \[ E_{\mathrm{u}}=\frac{U-J}{2}\sum_{\sigma,m,m^{\prime}}n_{mm^{\prime}}^{\sigma}\delta_{m^{\prime}m^{\prime}}-n_{mm^{\prime}}^{\sigma}n_{m^{\prime}m}^{\sigma}, \quad (2) \] 

where the occupancy matrix elements can be defined using the set of subspace orbitals  \( \{\phi_{m}\} \)  and the spin-resolved Kohn-Sham (KS) density operator  \( \hat{\rho}^{\sigma} \) ,

 \[ n_{m m^{\prime}}^{\sigma}=\langle\phi_{m}|\hat{\rho}^{\sigma}|\phi_{m^{\prime}}\rangle. \quad (3) \] 

The U - J prefactor in Eq. 2 is typically labelled as the effective Hubbard parameter  \( U_{eff} \) . Like the DFT+U functional of Dudarev et al., the DFT+U+J functional of Himmetoglu et al. is based on an on-site interaction term and a spin-polarized, fully-localized-limit double-counting correction. However, in this case, the interaction term is derived from Hartree-Fock theory, keeping only the on-site Coulomb and exchange terms, which are treated at the subspace averaged level, yielding

 \[ E_{\mathrm{i n t}}=\frac{U}{2}\sum_{\sigma}\left(n^{\sigma}n^{\sigma}+n^{\sigma}n^{\bar{\sigma}}\right)-\frac{U}{2}\sum_{\sigma,m,m^{\prime}}n_{m m^{\prime}}^{\sigma}n_{m^{\prime}m}^{\sigma}+\frac{J}{2}\sum_{\sigma,m,m^{\prime}}\left(n_{m m^{\prime}}^{\sigma}n_{m^{\prime}m}^{\sigma}+n_{m m^{\prime}}^{\sigma}n_{m^{\prime}m}^{\bar{\sigma}}\right)-\frac{J}{2}\sum_{\sigma}n^{\sigma}n^{\sigma}. \quad (4) \] 

total energy surface as a function of the electron count and spin-magnetization [33, 34]. By virtue of enforcing the flat plane condition, the BLOR functional by design corrects for the subspace analogue of many-electron self-interaction error [35, 36] and static correlation error [37], two of the most pervasive errors of DFT, which can be defined as energetic deviations from the flat plane condition with respect to electron count and spin-magnetization, respectively. A many-body generalisation of the BLOR functional [38] and the DFT+U functional of Bajaj et al. [39, 40] have also been developed based on the flat-plane condition but are beyond the scope of this study.

The BLOR corrective functional has two different forms depending on whether the subspace is more or less than half-occupied, i.e., the total subspace occupancy
 

N > 2l + 1 or  \( N \leq 2l + 1 \) , where l is the orbital angu

 \[ E_{BLOR}=\left\{\begin{array}{c c c c c c}{{{\sum_{m m^{\prime}}\frac{U^{\sigma}}{2}n_{m m^{\prime}}^{\sigma}\delta_{m m^{\prime}}}}&{{{-}}}&{{{\frac{U^{\sigma}}{2}n_{m m^{\prime}}^{\sigma}n_{m^{\prime}}^{\sigma}}}}&{{{-}}}&{{{\frac{U^{\sigma}+2J}{2}n_{m m^{\prime}}^{\sigma}n_{m^{\prime}}^{\bar{\sigma}}}},}}&{{{N\leq2l+1,}}} \\{{{\sum_{m m^{\prime}}\left(U^{\sigma}+\frac{U^{\bar{\sigma}}}{2}+2J\right)n_{m m^{\prime}}^{\sigma}\delta_{m m^{\prime}}}}&{{{-}}}&{{{\frac{U^{\sigma}}{2}n_{m m^{\prime}}^{\sigma}n_{m^{\prime}}^{\bar{\sigma}}}}}&{{{-}}}&{{{\frac{U^{\sigma}+2J}{2}n_{m m^{\prime}}^{\sigma}n_{m^{\prime}}^{\bar{\sigma}}}},}}&{{{N>2l+1.}}} \\\end{array}\right. \quad (6) \] 

The BLOR functional includes a spin-dependent Hubbard parameter  \( U^{\sigma} \) , however for non-spin polarized systems such as CZTS, the spin-indexed parameter  \( U^{\sigma} = U - J \) . This article is the first reported application of the BLOR functional to solid-state systems.

Transition metal 3d and Lanthanide 4f atomic orbitals are the most commonly selected subspaces for treatment at the DFT+U level. However, the approach has been extended to a wide variety of other atomic orbitals such as oxygen 2p [41–43], transition metal 4s [44, 45] and nearest neighbor ligand states [46]. Alternative subspace definitions such as maximally-localized Wannier functions [47–49], ortho-atomic orbitals [44, 50–52], and molecular orbitals [53, 54] have also been thoroughly investigated.

Once a specific DFT+U functional and targeted subspace has been selected, the U and J parameters must be selected. Unfortunately, it remains commonplace in the literature to empirically tune the Hubbard corrective parameters to reproduce material properties of interest, severely limiting the predictive power of the DFT+U approach. By contrast, in this study, we deploy the minimum-tracking linear response methodology  \( [55–58] \)  to evaluate Hubbard U and Hund's J corrective parameters for select atomic subspaces. This is achieved by applying a series of spin-resolved perturbations to the subspace of interest and recording the change in spin-resolved subspace occupancy  \( n^{\sigma} \)  and spin-resolved, subspace-averaged Hxc potential  \( v_{Hxc}^{r} \)  where,

 \[ n^{\sigma}=\sum_{m}n_{m m}^{\sigma}\quad\&\quad v_{\mathrm{H x c}}^{\sigma}=\frac{\sum_{m}\left\langle\phi_{m}\right|\hat{v}_{\mathrm{H x c}}^{\sigma}\left|\phi_{m}\right\rangle}{\sum_{m^{\prime}}\left\langle\phi_{m^{\prime}}\right|\phi_{m^{\prime}}}\mathrm{.} \quad (7) \] 

Within this formalism, the Hubbard U and Hund's J parameters are defined as

 \[ U=\frac{1}{2}\frac{d v_{\mathrm{H x c}}^{\dagger}+d v_{\mathrm{H x c}}^{\dagger}}{d(n^{\dagger}+n^{\downarrow})}\quad\&\quad J=-\frac{1}{2}\frac{d v_{\mathrm{H x c}}^{\dagger}-d v_{\mathrm{H x c}}^{\dagger}}{d(n^{\dagger}-n^{\downarrow})}. \quad (8) \] 

The definition of the Hubbard U parameter can be re-expressed in terms of the elements of the spin-indexed, subspace-averaged Hxc kernel,

 \[ U\approx\frac{1}{2}\frac{f^{\dagger\dagger}\delta n^{\dagger}+f^{\dagger\dagger}\delta n^{\downarrow}+f^{\dagger\dagger}\delta n^{\dagger}+f^{\dagger\downarrow}n^{\downarrow}}{\delta(n^{\dagger}+n^{\downarrow})}. \quad (9) \] 

lar momentum quantum number. In terms of subspace occupancy matrix elements the corrective functional is

 \[ \begin{aligned}N\leq2l+1,\\N>2l+1.\end{aligned} \quad (6) \] 

To proceed further, one of two possible approximations needs to be made, i.e., the simple  \( 2 \times 2 \)  approach or the scaled  \( 2 \times 2 \)  approach. However, these are exactly equivalent for nonmagnetic materials, which are the exclusive focus of this study. Within the simple  \( 2 \times 2 \)  approach, it is assumed that the spin-resolved occupancies respond equally to a non-spin-polarized perturbation, i.e.,  \( \delta n^{\dagger} \approx \delta n^{\downarrow} \)  in Eq. 9, in which case the Hubbard U parameter simplifies to

 \[ U=\frac{1}{4}\left(f^{\dagger\dagger}+f^{\dagger\downarrow}+f^{\downarrow\dagger}+f^{\downarrow\downarrow}\right). \quad (10) \] 

Analogously, the simple  \( 2 \times 2 \)  approach for the Hund's parameter results in the expression

 \[ J=-\frac{1}{4}\left(f^{\dagger\dagger}-f^{\dagger\downarrow}-f^{\downarrow\dagger}+f^{\downarrow\downarrow}\right). \quad (11) \] 

The spin-indexed, subspace-averaged Hxc kernel (a partially screened quantity, when calculated for subspaces of the global system) maybe expressed as

 \[ \begin{pmatrix}f^{\dagger\dagger}&f^{\dagger\downarrow}\\f^{\downarrow\dagger}&f^{\downarrow\downarrow}\end{pmatrix}=\begin{pmatrix}\frac{dv_{\mathrm{Hxc}}^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}&\frac{dv_{\mathrm{Hxc}}^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}\\ \frac{dv_{\mathrm{Hxc}}^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}&\frac{dv_{\mathrm{Hxc}}^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}\end{pmatrix}\begin{pmatrix}\frac{dn^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}&\frac{dn^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}\\ \frac{dn^{\dagger}}{dv_{\mathrm{ext}}^{\dagger}}&\frac{dn^{\prime}}{dv_{\mathrm{ext}}^{\dagger}}\end{pmatrix}^{-1}, \quad (12) \] 

where  \( v_{ext}^{\sigma} \)  is the spin- \( \sigma \) , subspace-averaged external potential, typically defined relative to the ground state, in which case its value is equal to the spin- \( \sigma \)  perturbation strength. The matrix elements of  \( dv_{Hxc}/dv_{ext} \)  and  \( dn/dv_{ext} \)  can be readily evaluated as the slopes of the corresponding linear response plots. The response of the Hxc contribution of the Projector Augmented Wave (PAW) [59] effective potential need also be accounted for [46] within Eq. 12, but in this study, norm-conserving pseudopotentials (NCPs) were deployed throughout.

For the avoidance of doubt, no inter-site response matrix inversion was carried out, as this cumbersome step is entirely unnecessary and avoided in the minimum-tracking approach, when calculating only on-site parameters, as we are. In the present work, we also exploited the spin-symmetry of ultimately nonmagnetic systems, as was first done in Ref. [57], to calculate U and J simultaneously (without any added approximation) using
 

a single set of finite-difference perturbations. This was recently demonstrated to be an exact approach (always only for nonmagnetic systems) also in the context of the conventional 'self-consistent field' linear-response method for U, where it was termed the 'gamma' method [44]. Here, perturbations of strength  \( \gamma \)  are applied uniformly to the spin-up channel of the subspace only, in practice by setting  \( \alpha = \beta = \gamma/2 \)  in the conventional notation for the linear response Hubbard U. One can show that  \( \gamma \)  is, in this regime, a parameter for both the numerators and denominators of Eq. 8, so that a single regression each, for U and J, is sufficient, based on a common data set.

Bespoke NCPs were very painstakingly generated using the Rappe-Rabe-Kaxiras-Joannopoulos algorithm  \( [60] \)  as implemented in the open-source pseudopotential generation software OPIUM (version 3.8) with a cutoff wavevector of  \( 7.9\ R y^{1/2} \)  and 10 Bessel functions for each pseudo-orbital. In the construction of each pseudopotential, a neutral atomic reference configuration was solved using the j-averaged scalar relativistic scheme  \( [61] \)  with the Perdew-Burke-Ernzerhof (PBE) functional  \( [62] \) . Non-linear core valence interactions were accounted for using a Louie-Froyen-Cohen-type partial core correction  \( [63] \) .

All DFT calculations were executed using the ONETEP (Order-N Electronic Total Energy Package) DFT code  \( [64-67] \) . ONETEP is, in principle, a linear scaling DFT code, which is achieved through truncation of the exponentially decaying tail of the density matrix (this was not done here). The ONETEP code constructs the KS density matrix  \( \rho(\mathbf{r},\mathbf{r}^{\prime}) \)  from a set of localized basis orbitals, namely non-orthogonal generalized Wannier functions (NGWFs)  \( \{\phi_{\alpha}\} \) .

 \[ \rho(\mathbf{r},\mathbf{r}^{\prime})=\sum_{\alpha,\beta}\phi_{\alpha}(\mathbf{r})K^{\alpha\beta}\phi_{\beta}(\mathbf{r}^{\prime}), \quad (13) \] 

where  \( K^{\alpha\beta} \)  is the density kernel. Near-complete basis-set accuracy is achieved using a relatively small set of localized basis orbitals by minimizing the total energy of the system with respect to both  \( K^{\alpha\beta} \)  and  \( \{\phi_{\alpha}\} \) .

All calculations were completed using the PBE [62] exchange-correlation (XC) functional at a cutoff energy of no less than 850 eV. The convergence threshold of the root-mean-square gradient of the NGWFs and the electronic energy tolerance were set at  \( 2 \times 10^{-6} \)  Ha  \( a_{0}^{3/2} \)  and  \( 1 \times 10^{-4} \)  eV/atom, respectively. Four NGWFs were assigned per sulphur atom and nine NGWFs were assigned per non-sulphur atom. For each atom, the NGWF cutoff radii were set to encapsulate 99.8% of the norm of the respective pseudo-atomic KS wavefunctions computed by the pseudoatomic solver [68] at the onset of the ONETEP calculation. A 1,728 atom simulation cell comprising  \( 6 \times 6 \times 3 \)  copies of the conventional cell was used in all calculations, at  \( \Gamma \)  only. A Gaussian smearing of 0.1 eV was used for density-of-states plotting. Atomic positions and lattice constants were taken from the neutron diffraction results of Mangelis et al. [69].
The DFT+U approach is primarily designed to improve the description of localized electronic states which are poorly treated by conventional local and semi-local XC functionals. A topical question, however, is which subspaces should be selected for treatment at the DFT+U-level? As opposed to arbitrarily selecting atomic d-states for treatment at the DFT+U-level, in this study we selected all atomic states that dominate the valence and conduction band edges. The reasoning behind this is two-fold; (i) the linear response technique is specifically designed for application with partially occupied states near the Fermi level, and (ii) correction of the local and semi-local XC functionals' tendency to underestimate the bandgap likely warrants the treatment of all atomic states which dominate the valence and conduction band edges, as is corroborated by the work of Wexler et al. [23], where application of Hubbard U corrections to Cu 3d, Zn 3d, and Sn 4d states failed to sufficiently open the bandgap of CZTS. By contrast, Nor et al. [70] reproduced the experimental bandgap through empirical tuning of the Hubbard corrective parameters applied to the Cu 3d, Zn 3d, Sn 5p, and S 3p states, albeit at the loss of the predictive power of the technique.

Fig. 2 presents the projected density of states (PDOS) of CZGS evaluated at the bare PBE,  \( PBE+U_{eff} \)  and  \( PBE+BLOR \)  levels. An analogous plot for CZTS is presented in Fig 5. The valence and conduction band edges are dominated by Cu 3d, S 3p, and Ge 4s or Sn 5s (for CZGS or CZTS, respectively) states, and as such, these states were selected for treatment at the DFT+U-level. The computed Hubbard U and Hund's J parameters are presented in Table I. Small but non-negligible differences in the corrective parameters for the Cu 3d and S 3p atomic subspaces in CZTS compared to CZGS are observed.

Due to the near equivalent subspace occupancy matrices of the Cu atoms at the 2a and 2c Wyckoff positions, a single set of U and J parameters was used for both sites. These U and J values were evaluated by applying perturbations to the 3d subspace of Cu at the 2a Wyckoff position. No Hubbard corrective parameters were evaluated.

TABLE I. Hubbard U and Hund's J parameters computed via the simple  \( 2 \times 2 \)  minimum tracking linear response approach for CZTS and CZGS using orbitals as generated by the ONETEP pseudoatomic solver using bespoke NCPs.

<table><tr><td>Material</td><td>Subspace</td><td>U (eV)</td><td>J (eV)</td></tr><tr><td rowspan="3">CZTS</td><td>Cu 3d</td><td>9.68</td><td>0.86</td></tr><tr><td>Sn 5s</td><td>2.50</td><td>0.67</td></tr><tr><td>S 3p</td><td>4.74</td><td>0.57</td></tr><tr><td rowspan="3">CZGS</td><td>Cu 3d</td><td>10.02</td><td>0.89</td></tr><tr><td>Ge 4s</td><td>3.11</td><td>0.79</td></tr><tr><td>S 3p</td><td>4.65</td><td>0.57</td></tr></table>
 
![](2512.14548v1-images/4_0.jpg)

FIG. 2. Projected density of states (PDOS) of CZGS evaluated at the PBE (top), PBE+ \( U_{eff} \)  (middle), and PBE+BLOR (bottom) levels with a Gaussian broadening of 0.1 eV. The energy values are reported with respect to the mid-gap energy of the bare PBE calculation ( \( E_{\perp} \) ) to readily identify the effect of the Hubbard corrections on the valence and conduction bands.

ated for the Zn 3d subspace. By virtue of its absence from both the valence and conduction band edges the subspace would not be amenable to Hubbard parameter evaluation via linear response and for the same reason, reasonable Hubbard type corrections to the subspace would offer no significant correction to the bandgap.

The predicted fundamental bandgap of CZGS is presented in Fig. 3 with an increasing number of atomic subspaces selected for treatment at the  \( PBE+U_{eff} \)  level. Here  \( PBE+U_{eff} \)  refers to the DFT+U functional of Dudarev et al. with the effective Hubbard parameter  \( U_{eff} \) , set as the difference between the Hubbard U and Hund's J parameters presented in Table I (the calculated Hubbard U is, most emphatically, not already  \( U_{eff} \)  [55]). The PBE approximation was applied as the base functional in all DFT+U calculations. Treatment of the Cu-3d states alone did not sufficiently open the bandgap but this issue was rectified through the additional treatment of the S-3p states. The inclusion of Hubbard corrections on the Ge-4s states yields only a marginal change in the bandgap value, and the addition of a positive U on conduction band 4s states causing a small reduction in overall bandgap is an effect previously observed in other materials. Notwithstanding, both the  \( \mathrm{Cu(3d)+S(3p)} \)  and  \( \mathrm{Cu(3d)+S(3p)+Ge(4s)} \)  options offer bandgaps in close agreement with the reported experimental value of 1.88 eV [71]. These results corroborate our working hypothesis that reliable bandgap predictions, free from prior judgement regarding subspace selection (there remains arbitrariness with respect to projector shape), can be achieved through the application of Hubbard corrections to all atomic states that dominate the valence and conduction band edges.

Fig. 4 presents the fundamental bandgap predictions for CZTS and CZGS evaluated at the PBE,  \( PBE+U_{eff} \) ,  \( PBE+U+J \)  and  \( PBE+BLOR \)  level with Hubbard corrections applied to all three atomic subspaces. The results are benchmarked against reference experimental optical bandgaps of Khadka et al. [71, 72] and previously computed bandgaps from the literature. Caution should be taken in comparing the reference experimental optical bandgaps to computed fundamental bandgaps as the two differ by the exciton binding energy. In order to ascertain a rough estimate of the exciton binding energy, both the fundamental bandgap and the first triplet ex-

![](2512.14548v1-images/4_1.jpg)

FIG. 3. The predicted bandgap of CZGS using the PBE XC functional with Hubbard corrections applied to an increasing number of atomic subspaces. The element labels refer to the atomic subspaces to which Hubbard corrections were applied, namely Cu-3d, S-3p and Ge-4s.
 
![](2512.14548v1-images/5_0.jpg)

FIG. 4. Bandgaps of (top) CZTS and (bottom) CZGS evaluated at the PBE,  \( PBE + U_{eff} \)  and  \( PBE + U + J \)  level with Hubbard corrections applied to the Cu 3d, S 3p, Sn 5s, and Ge 4s atomic subspaces. A variety of bandgap predictions from the literature are also presented [23, 24, 71–80], these were evaluated using a Local Density Approximation (LDA) [81] (dark pink bar); semi-local approximations (PBE [62], PBEso [82], and PW91 [83]—light pink bars); a meta-generalized gradient approximation, both with and without dispersion corrections (SCAN [84] and SCAN+rV10 [85]—dark gray bars); hybrid functionals (PBE0 [86], HSE03 [25], and HSE06 [87]—green bars); the DFT+U method [29] (PBE+U and SCAN+U—dark blue bars); and both the perturbative and fully self-consistent GW approximation (light blue bars) [88, 89]. Experimental values from UV-Vis absorption spectroscopy are also provided [71, 72]. Bandgaps calculated as part of the current work are bolded and have yellow bars.

citation energies were computed at the  \( PBE+U_{eff} \)  level. The first triplet excitation energies of CZTS and CZGS were evaluated as 1.46 eV and 1.87 eV, which differ from their respective fundamental bandgaps by only 0.01 eV. This suggests a negligible exciton binding energy in both kesterite compounds, a result which is corroborated by the work of Körbel et al. [80], who reported negligible exciton binding energies having evaluated both the fundamental bandgap using the self-consistent GW approach and the optical bandgap via the Bethe-Salpeter equation. The absence of significant exciton binding effects allows a direct comparison to be made between the computed fundamental bandgaps and reference experimental optical bandgaps, cautioning of course that subtle differences can still arise due to the presence of defects [90] and finite grain-size [91], zero-point renormalization [92], spin-orbit coupling [93], and ambiguities in the extrapolation method used to ascertain the bandgap from UV-Vis absorption data [94].

Unsurprisingly, the bare PBE calculations vastly underestimated the bandgap for both kesterite structures. This failure, known more broadly as the bandgap problem  \( [95, 96] \) , is already well documented in the literature and is related to the absence of a derivative discontinuity in conventional (semi-)local XC potentials with respect to electron count. Our PBE bandgap values are at least in close agreement with previous PBE results  \( [23, 24, 74, 78] \) . Intriguingly, the poor bandgap predictions at the (semi-)local level  \( [23, 24, 73, 74, 78, 79] \)  are not even partially alleviated through use of the SCAN meta-generalized gradient approximation  \( [23] \) . Non-negligible bandgaps for CZTS can be achieved through use of the global hybrid PBE0  \( [74] \)  or DFT+U-type corrections applied to the localized atomic d-states  \( [23, 73, 78] \) , however the results remain far from quantitative agreement with experiment. Furthermore, the use of the perturbative  \( G_{0}W_{0} \)  method results in bandgaps that are exceedingly dependent on the chosen starting point  \( [77, 78] \) , be it a KS wavefunction computed at the PBE or PBE+U level. Previous studies thus suggest that reasonable bandgap predictions for CZTS and CZGS semiconductors can only be achieved through computationally demanding techniques such as range-separated hybrids  \( [23, 24, 73, 74, 76, 78] \)  or self-consistent GW approaches  \( [73, 80] \) .

Despite this, our  \( PBE+U_{eff} \)  approach yields bandgaps in remarkably good agreement with experiment, deviating by only 0.06 eV and 0.02 eV from the CZTS and

TABLE II. Subspace averaged Hubbard corrective potentials in eV. The reported Cu 3d subspace values are for the Wyckoff 2a position.

<table><tr><td>Material</td><td>Subspace</td><td>DFT+U_{\text{eff}}</td><td>BLOR</td></tr><tr><td rowspan="3">CZTS</td><td>Cu 3d</td><td>-4.35</td><td>-4.27</td></tr><tr><td>Sn 5s</td><td>-0.70</td><td>-0.37</td></tr><tr><td>S 3p</td><td>-1.72</td><td>-1.20</td></tr><tr><td rowspan="3">CZGS</td><td>Cu 3d</td><td>-4.50</td><td>-4.43</td></tr><tr><td>Ge 4s</td><td>-0.94</td><td>-0.63</td></tr><tr><td>S 3p</td><td>-1.68</td><td>-1.17</td></tr></table>
 
![](2512.14548v1-images/6_0.jpg)

FIG. 5. PDOS of CZTS evaluated at the PBE (top),  \( PBE+U_{eff} \)  (middle), and  \( PBE+BLOR \)  (bottom) levels with a Gaussian broadening of 0.1 eV. The energy values are reported with respect to the mid-gap energy of the bare PBE calculation ( \( E_{\perp} \) ) to readily identify the effect of the Hubbard corrections on the valence and conduction bands.

CZGS reference values, respectively. In both cases, the  \( PBE+U_{eff} \)  bandgap prediction outperforms even the self-consistent GW approach [73, 80, 89]. The inclusion of inter-spin corrections via the extended  \( PBE+U+J \)  functional degrades the predicted bandgaps by about 0.3 eV. To understand this discrepancy, consider a system with Hubbard corrections applied to one Hubbard manifold which is at full subspace occupancy. To first-order in perturbation theory, Dudarev's functional will, in the limit of full subspace occupancy, shift a band which projects perfectly onto the Hubbard manifold  \( -(U-J)/2 \) . The  \( DFT+U+J \)  functional will shift the same band by  \( -(U-3J)/2 \) . If the valence band edge projects perfectly onto the Hubbard manifold, the bandgap opening offered by Dudarev's functional and the  \( DFT+U+J \)  functional differs by J eV. In contrast, the BLOR functional will, like Dudarev's functional, shift the band by  \( -(U-J)/2 \) . The Cu 3d subspace in CZTS and CZGS is near full occupancy, thus unsurprisingly Dudarev's and BLOR functional predict similar bandgaps for the two kesterite compounds while the  \( DFT+U+J \)  functional offers a reduced bandgap in both cases. However, it is worth emphasizing that the exact numerical agreement between the  \( PBE+U_{eff} \)  and  \( PBE+BLOR \)  bandgaps for CZTS is merely fortuitous as the two approaches offer quite distinct corrections to the potential at the sulfur and tin/germanium sites, as indicated by the subspace averaged Hubbard corrective potentials in Table II. While the two  \( DFT+U \)  functionals offer similar corrections to the Cu 3d subspace, the BLOR functional offers a smaller correction to the S 3p and Sn 5s/Ge 4s subspaces in both materials. The underperformance of the  \( DFT+U+J \)  functional in this study, is in line with recent findings of the extended corrective functional's failure to improve the  \( DFT+U \)  adiabatic energy differences in spin-crossover transition metal complexes [46], but we note however that it has been shown to handle a test-set of nonmagnetic transition metal oxides very well [44]. Despite the promising success of the BLOR functional in predicting the bandgaps of CZTS and CZGS, further testing and possibly refinement of the corrective functional will be needed before the authors consider advocating for the method's widespread adoption on solids.

The CZTS PDOS evaluated at the bare PBE,  \( PBE+U_{eff} \)  and  \( PBE+BLOR \)  levels are presented in Fig. 5. Despite the significant differences in the Hubbard corrections to the potential at the sulfur and tin sites, Dudarev's functional and the BLOR functional offer remarkably similar corrections to the PDOS of CZTS. The energies are reported with respect to the mid-gap energy of the bare PBE calculation for ease of comparison. Application of Hubbard-type corrections to the Cu 3d, S 3p, and Sn 5s states results in a bandgap opening primarily due to a significant lowering in the energies of the occupied bands of Cu 3d and S 3p character. Intriguingly, the lowering in energy of the localized Cu 3d states results in increased hybridization with the broader

TABLE III. The valence bandwidth and energy gap between the first and second valence bands (VB → VB − 1), evaluated via application of the DFT+U_{eff} and BLOR functionals.

<table><tr><td>Material</td><td>Corrective Functional</td><td>Valence Bandwidth (eV)</td><td>VB  \( \rightarrow \)  VB - 1 Gap (eV)</td></tr><tr><td rowspan="2">CZTS</td><td>DFT+U \( _{\text{eff}} \)</td><td>6.75</td><td>1.13</td></tr><tr><td>BLOR</td><td>6.71</td><td>0.76</td></tr><tr><td rowspan="2">CZGS</td><td>DFT+U \( _{\text{eff}} \)</td><td>7.06</td><td>1.64</td></tr><tr><td>BLOR</td><td>7.02</td><td>1.30</td></tr></table>
 

S 3p states. Therefore, rather counterintuitively, the application of Hubbard-type corrections results in more energetically delocalized Cu 3d bands in CZTS. The conduction band edge is predominantly of S 3p and Sn 5s character, both with and without Hubbard-type corrections. The application of the Hubbard-type corrections results in a marginal lowering in energy of the unoccupied 3p and Sn 5s states. The Sn 5p in addition to the zinc and sulphur s states contribute significantly to the conduction band beyond 2 eV, however, of these, only the Sn 5p contribution was individually plotted to avoid overcrowding the graph. Moreover, we note that as the NGWFs in ONETEP are optimized to minimize the total energy, so they are not optimized as standard to form a complete basis for the unoccupied states. Thus, the conduction band PDOS shown should be interpreted as qualitatively but not quantitatively accurate for the approximate functional at hand. By contrast, for a given approximate functional a quantitatively accurate valence band can be achieved with the ONETEP code. The valence bandwidth and energy gap between the first and second valence bands are reported in Table I. In both materials, the DFT+ \( U_{eff} \)  and BLOR functionals predict remarkably similar values for the valence bandwidth, but the BLOR functional offers a reduced valence 'second' energy gap compared to the DFT+ \( U_{eff} \)  functional.

The linear scaling ONETEP code readily enables DFT calculations on large simulation cells; this, combined with the very satisfactory  \( PBE+U_{eff} \)  bandgap predictions, offers a computational approach which is ideally suited for the prediction of crystallographic defects. Previous computational studies suggest a wide variety of possible defects may form in CZTS under experimental conditions [23, 98–104]. Thanks to their ability to act as free carrier traps and non-radiative recombination centers [98], the presence of point defects can have a significant impact on solar cell efficiencies. Identifying and characterizing point defects in kesterite-based semicon-

![](2512.14548v1-images/7_0.jpg)

FIG. 6. The Cu-Zn antisite pair defect density at an isosurface value of  \( \pm0.02\ \mathring{A}^{-3} \)  and  \( \pm0.2\ \mathring{A}^{-3} \)  [97], evaluated as the density difference between the defect-harboring and pristine structures at the  \( PBE+U_{eff} \)  level. Cu is shown in gray, Zn in blue, Sn in dark green, and S in yellow. Density increases are shown in brown and density decreases in light green.

![](2512.14548v1-images/7_1.jpg)

FIG. 7. The bandgaps (interstitial text) of CZTS (pink) and CZGS (teal), both with (darker bars) and without (lighter bars) the charge-neutral anti-site pair defect  \( \left(\mathrm{Cu}_{\mathrm{Zn}}+\mathrm{Zn}_{\mathrm{Cu}}\right) \) , evaluated at the  \( PBE+U_{eff} \)  level. Valence band represented by lower tier of bars, and conduction band represented by the upper bars.

ductors is thus of central importance to improving device performance. The results of neutron diffraction experiments suggest a partial disorder in the cation sub-lattice, with  \( Cu_{Zn} \)  and  \( Zn_{Cu} \)  anti-sites forming at the Wyckoff 2d and 2c positions, respectively [69, 105, 106]. In this study, the formation of the Cu-Zn anti-site pair defect ( \( Cu_{Zn} + Zn_{Cu} \) ) was investigated at the  \( PBE + U_{eff} \)  level. The Cu-Zn anti-site pair defect is presented in Fig. 6 based on the density difference of the defect-harboring and pristine structures at the  \( PBE + U_{eff} \)  level. There is a sharp decrease in the electron density in the immediate vicinity of the Cu site, an increase in the electron density at larger radii and a subsequent decrease in the electron density in the Cu-S bonding region. The reverse is true at the Zn site. This effect is largely due to the additional 4s electron in Zn compared to Cu with the subtle changes in charge density at larger radii and in the transition metal-sulfur bonding region being simply due to charge compensation effects. The defect density plot suggests that both the  \( Cu_{Zn} \)  site and  \( Zn_{Cu} \)  site remain charge neutral and together form a charge neutral defect complex. This is corroborated by the Mulliken atomic (NGWF based) population analysis, where both the standard Cu site and the defective  \( Cu_{Zn} \)  site have a total occupancy of 11.1, while the occupancy at the standard Zn site and the defective  \( Zn_{Cu} \)  site are both 11.7.

In Fig. 7, the bandgaps of pristine CZTS and CZGS are compared to the equivalent structures harboring a Cu-Zn anti-site pair defect. The defect geometry was prepared by simply swapping the chemical character of neighboring Cu and Zn sites without running a geometry relaxation. As shown in Fig. 7, no defect levels are observed within the gap; rather the inclusion of the anti-
 

site pair defect results in a slight decrease of the band-gap and a corresponding increase in the energy of the valence band maximum. The defect-formation energy of the charge-neutral, stoichiometry-preserving anti-site pair defect is independent of the chemical potential and can thus be readily evaluated as the energy difference between the pristine and defect-harboring crystallographic structures. The frozen-ion defect-formation energies in CZTS and CZGS were evaluated as 0.580 eV and 0.505 eV, respectively.

In conclusion, in situ Hubbard parameters determined via minimum-tracking linear response were deployed through a series of common DFT+U functionals for the prediction of the electronic structure of kesterite-based photovoltaic materials. The conventional DFT+U-type functional of Dudarev et al. predicted bandgaps in remarkably close agreement to experimental reference values, even marginally outperforming the self-consistent GW approach. As opposed to improving the DFT+Ueff approach, the extended DFT+U+J functional introduces a systematic underestimation of the bandgap of CZTS and CZGS, this effect can be ameliorated through the use of the alternative Hubbard U plus Hund's J ex-
[1] European Parliament and Council of the European Union, Regulation (EU) 2021/1119, Establishing the framework for achieving climate neutrality and amending Regulations (EC) No 401/2009 and (EU) 2018/1999 (European Climate Law), Regulation (2021).

[2] N. Burnett, I. Stewart, and T. Hewitt, The UK’s Plans and Progress to Reach Net Zero by 2050, Tech. Rep. House of Commons Library (2025).

[3] European Commission, Directorate-General for Energy, Energy Roadmap 2050, Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions COM 885 final (2011).

[4] International Energy Agency, Renewables 2024: Analysis and forecasts to 2030, Tech. Rep. (International Energy Agency (IEA), Paris, France, 2024).

[5] W. M. Hynes, CRC Handbook of Chemistry and Physics, Vol. 91 (CRCpress, 2011).

[6] G. B. Haxel, J. B. Hedrick, and G. J. Orris, Rare Earth Elements—Critical Resources for High Technology, Mineral Commodity Summaries (U.S. Geological Survey, 2002) fact Sheet 087-82.

[7] H. Katagiri, N. Sasaguchi, S. Hando, S. Hoshino, J. Ohashi, and T. Yokota, Sol. Energy Mater. Sol. Cells 49, 407 (1997).

[8] J.-S. Seol, S.-Y. Lee, J.-C. Lee, H.-D. Nam, and K.-H. Kim, Sol. Energy Mater. Sol. Cells 75, 155 (2003).

[9] S. Suresh and A. R. Uhl, Adv. Energy Mater. 11, 2003743 (2021).

[10] T. Schnabel, M. Seboui, and E. Ahlswede, RSC Adv. 7, 26 (2017).

[11] T. Kohl, G. Brammertz, J. de Wild, M. Neuwirth, M. Meuris, J. Poortmans, and B. Vermang,

tended functional of Burgess Linscott and O'Regan. In contrast to conventional understanding of the DFT+U approach, the inclusion of Hubbard U corrections on 3d transition metal sites results in a more energetically delocalized electronic structure for this particular material class. The DFT+Ueff approach was also deployed for the prediction of defects in CZTS and CZGS. A low frozen-ion defect-formation energy of 0.580 eV and 0.505 eV was predicted for the Cu-Zn anti-site pair in CZTS and CZGS, respectively.

This research was supported by Taighde-Éireann under Grant No. GOIPG/2020/1454 and under Prime Award No. 12/RC/2278_P2, the latter of which is co-funded by the European Regional Development Fund. LM and DDO'R further acknowledge the support of Trinity College Dublin through its Provost PhD Awards. The authors wish to acknowledge the Irish Centre for High-End Computing (ICHEC) for the provision of computational facilities and support. Calculations were also performed on the Boyle cluster maintained by the Trinity Centre for High Performance Computing. This cluster was funded through grants from the European Research Council and Taighde-Éireann – Research Ireland.

Thin Solid Films 660, 247 (2018).

[12] H. Katagiri, K. Jimbo, W. S. Maw, K. Oishi, M. Yamazaki, H. Araki, and A. Takeuchi, Thin Solid Films 517, 2455 (2009).

[13] W. Wang, M. T. Winkler, O. Gunawan, T. Gokmen, T. K. Todorov, Y. Zhu, and D. B. Mitzi, Adv. Energy Mater. 4, 1301465 (2014).

[14] K. Ito and T. Nakazawa, Jpn. J. Appl. Phys. 27, 2094 (1988).

[15] J. Zhou, X. Xu, H. Wu, J. Wang, L. Lou, K. Yin, Y. Gong, J. Shi, Y. Luo, D. Li, H. Xin, and Q. Meng, Nat Energy 8, 526 (2023).

[16] M. A. Green, E. D. Dunlop, M. Yoshita, N. Kopidakis, K. Bothe, G. Siefer, X. Hao, and J. Y. Jiang, Prog. Photovolt. Res. Appl. 33, 795 (2025).

[17] W. Ki and H. W. Hillhouse, Adv. Energy Mater. 1, 732 (2011).

[18] A. Polman, M. Knight, E. C. Garnett, B. Ehrler, and W. C. Sinke, Science 352 (2016).

[19] D. B. Khadka and J. Kim, J. Phys. Chem. 119, 1706 (2015).

[20] Y.-F. Qi, D.-X. Kou, W.-H. Zhou, Z.-J. Zhou, Q.-W. Tian, Y.-N. Meng, X.-S. Liu, Z.-L. Du, and S.-X. Wu, Energy Environ. Sci. 10, 2401 (2017).

[21] S. Giraldo, Z. Jehl, M. Placidi, V. Izquierdo-Roca, A. Pérez-Rodríguez, and E. Saucedo, Adv. Mater. 31, 1806692 (2019).

[22] C. P. Heinrich, T. W. Day, W. G. Zeier, G. J. Snyder, and W. Tremel, J. Am. Chem. Soc. 136, 442 (2014).

[23] R. B. Wexler, G. S. Gautam, and E. A. Carter, Phys. Rev. B 102, 054101 (2020).

[24] J. Paier, R. Asahi, A. Nagoya, and G. Kresse, Phys. Rev. B 79, 115126 (2009).

[25] J. Heyd, G. E. Scuseria, and M. Ernzerhof,
 

J. Chem. Phys. 118, 8207 (2003).

[26] B. Himmetoglu, A. Floris, S. de Gironcoli, and M. Cococcioni, Int. J. Quantum Chem. 114, 14 (2014).

[27] V. I. Anisimov, F. Aryasetiawan, and A. I. Lichtenstein, J. Phys.: Condens. Matter 9, 767 (1997).

[28] N. E. Kirchner-Hall, W. Zhao, Y. Xiong, I. Timrov, and I. Dabo, Appl. Sci. 11, 2395 (2021).

[29] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev. B 57, 1505 (1998).

[30] B. Himmetoglu, R. M. Wentzcovitch, and M. Cococcioni, Phys. Rev. B 84, 115108 (2011).

[31] A. C. Burgess, E. Linscott, and D. D. O'Regan, Phys. Rev. B 107, L121115 (2023).

[32] In the derivation of their DFT+U functional, Dudarev et al. include an additional minor adjustment to ensure their functional form is invariant under unitary transformations of the subspace orbitals.

[33] W. Yang, Y. Zhang, and P. W. Ayers, Phys. Rev. Lett. 84, 5172 (2000).

[34] P. Mori-Sánchez, A. J. Cohen, and W. Yang, Phys. Rev. Lett. 102, 066403 (2009).

[35] A. Ruzsinszky, J. P. Perdew, G. I. Csonka, O. A. Vydrov, and G. E. Scuseria, J. Chem. Phys. 125, 194112 (2006).

[36] P. Mori-Sánchez, A. J. Cohen, and W. Yang, J. Chem. Phys. 125, 201102 (2006).

[37] A. J. Cohen, P. Mori-Sánchez, and W. Yang, J. Chem. Phys. 129, 121104 (2008).

[38] A. C. Burgess and D. D. O'Regan, Phys. Rev. B 110, 205150 (2024).

[39] A. Bajaj, J. P. Janet, and H. J. Kulik, J. Chem. Phys. 147, 191101 (2017).

[40] A. Bajaj, F. Liu, and H. J. Kulik, J. Chem. Phys. 150, 154115 (2019).

[41] G. C. Moore, M. K. Horton, E. Linscott, A. M. Ganose, M. Siron, D. D. O'Regan, and K. A. Persson, Phys. Rev. Mater. 8, 014409 (2024).

[42] A. Consiglio and Z. Tian, Sci. Rep. 6, 36875 (2016).

[43] Y. Yang, W. Yang, Y.-W. Son, and S. Liu, Phys. Rev. Mater. 9, 034402 (2025).

[44] D. S. Lambert and D. D. O'Regan, Phys. Rev. Res. 5, 013160 (2023).

[45] H. J. Kulik and N. Marzari, J. Chem. Phys. 133 (2010).

[46] L. MacEnulty, J. P. A. de Mendonça, R. Poloni, and D. D. O'Regan, Accepted for publication at JCTC. (2025), arXiv:2508.01979 [cond-mat].

[47] A. Carta, I. Timrov, P. Młkvik, A. Hampel, and C. Ederer, Phys. Rev. Res. 7, 013289 (2025).

[48] B.-C. Shih, T. A. Abtew, X. Yuan, W. Zhang, and P. Zhang, Phys. Rev. B 86, 165124 (2012).

[49] S. Fabris, S. de Gironcoli, S. Baroni, G. Vicario, and G. Balducci, Phys. Rev. B 71, 041102 (2005).

[50] I. Timrov, F. Aquilante, L. Binci, M. Cococcioni, and N. Marzari, Phys. Rev. B 102, 235159 (2020).

[51] C. Ricca, I. Timrov, M. Cococcioni, N. Marzari, and U. Aschauer, Phys. Rev. Res. 2, 023313 (2020).

[52] I. Timrov, P. Agrawal, X. Zhang, S. Erat, R. Liu, A. Braun, M. Cococcioni, M. Calandra, N. Marzari, and D. Passerone, Phys. Rev. Res. 2, 033265 (2020).

[53] A. Bajaj and H. J. Kulik, J. Phys. Chem. Lett. 12, 3633 (2021).

[54] A. Bajaj, C. Duan, A. Nandy, M. G. Taylor, and H. J. Kulik, J. Chem. Phys. 156, 184112 (2022).

[55] E. B. Linscott, D. J. Cole, M. C. Payne, and D. D. O'Regan, Phys. Rev. B 98, 235157 (2018).

[56] G. Moynihan, G. Teobaldi, and D. D. O'Regan, A self-consistent ground-state formulation of the first-principles Hubbard U parameter validated on one-electron self-interaction error (2017), arxiv:1704.08076 [cond-mat].

[57] O. K. Orhan and D. D. O'Regan, Phys. Rev. B 101, 245137 (2020).

[58] S. Berman, A. Zhussupbekova, J. E. Boschker, J. Schwarzkopf, D. D. O'Regan, I. V. Shvets, and K. Zhussupbekov, Phys. Rev. B 108, 155141 (2023).

[59] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

[60] A. M. Rappe, K. M. Rabe, E. Kaxiras, and J. D. Joannopoulos, Phys. Rev. B 41, 1227 (1990).

[61] I. Grinberg, N. J. Ramer, and A. M. Rappe, Phys. Rev. B 62, 2311 (2000).

[62] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[63] S. G. Louie, S. Froyen, and M. L. Cohen, Phys. Rev. B 26, 1738 (1982).

[64] J. C. A. Prentice, J. Aarons, J. C. Womack, A. E. A. Allen, L. Andrinopoulos, L. Anton, R. A. Bell, A. Bhandari, G. A. Bramley, R. J. Charlton, R. J. Clements, D. J. Cole, G. Constantinescu, F. Corsetti, S. M.-M. Dubois, K. K. B. Duff, J. M. Escartín, A. Greco, Q. Hill, L. P. Lee, E. Linscott, D. D. O'Regan, M. J. S. Phipps, L. E. Ratcliff, A. R. Serrano, E. W. Tait, G. Teobaldi, V. Vitale, N. Yeung, T. J. Zuehlsdorff, J. Dziedzic, P. D. Haynes, N. D. M. Hine, A. A. Mostofi, M. C. Payne, and C.-K. Skylaris, J. Chem. Phys. 152, 174111 (2020).

[65] C.-K. Skylaris, P. D. Haynes, A. A. Mostofi, and M. C. Payne, J. Chem. Phys. 122, 084119 (2005).

[66] C.-K. Skylaris, A. A. Mostofi, P. D. Haynes, O. Diéguez, and M. C. Payne, Phys. Rev. B 66, 035119 (2002).

[67] D. D. O'Regan, N. D. M. Hine, M. C. Payne, and A. A. Mostofi, Phys. Rev. B 85, 085107 (2012).

[68] Á. Ruiz-Serrano, N. D. M. Hine, and C.-K. Skylaris, J. Chem. Phys. 136, 234101 (2012).

[69] P. Mangelis, A. Aziz, I. da Silva, R. Grau-Crespo, P. Vaqueiro, and A. V. Powell, Phys. Chem. Chem. Phys. 21, 19311 (2019).

[70] N. A. N. M. Nor, M. A. H. Razali, W. H. A. W. K. Annuar, N. N. Alam, F. N. Sazman, N. H. M. Zaki, A. S. Kamisan, A. I. Kamisan, M. H. Samat, A. M. M. Ali, O. H. Hassan, B. U. Haq, M. Z. A. Yahya, and M. F. M. Taib, Physica B: Condens. Matter 673, 415450 (2024).

[71] D. B. Khadka and J. Kim, Cryst. Eng. Comm. 15, 10500 (2013).

[72] D. B. Khadka and J. Kim, J. Phys. Chem. C 118, 14227 (2014).

[73] S. Botti, D. Kammerlander, and M. A. L. Marques, Appl. Phys. Lett. 98, 241915 (2011).

[74] M. Quennet, First Principles Calculations for the Semiconductor Material Kesterite  \( Cu_{2}ZnSnS_{4} \)  and S-electronating Derivatives, Ph.D. thesis, Freie Universität Berlin, Berlin, Germany (2016), inaugural Dissertation; PDF available at Refubium.

[75] N. Dilshod, K. Kholmirzo, S. Aliona, F. Kahramon, G. Viktoriya, and K. Tameralan, Lett. Appl. NanoBioSci. 12, 67 (2022).

[76] J.-S. Park, S. Kim, and A. Walsh, J. Appl. Phys. 124, 165705 (2018).
 

[77] Y. Zhang, X. Yuan, X. Sun, B.-C. Shih, P. Zhang, and W. Zhang, Phys. Rev. B 84, 075127 (2011).

[78] Y. Zhang, X. Sun, P. Zhang, X. Yuan, F. Huang, and W. Zhang, J. Appl. Phys. 111, 063709 (2012).

[79] S. Chen, X. G. Gong, A. Walsh, and S.-H. Wei, Phys. Rev. B 79, 165211 (2009).

[80] S. Körbel, D. Kammerlander, R. Sarmiento-Pérez, C. Attaccalite, M. A. Marques, and S. Botti, Phys. Rev. B 91, 075134 (2015).

[81] D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).

[82] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. 100, 136406 (2008).

[83] K. Burke, J. P. Perdew, and Y. Wang, Electronic Density Functional Theory, edited by J. F. Dobson, G. Vignale, and M. P. Das (Springer US, Boston, MA, 1998) pp. 81–111.

[84] J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. 115, 036402 (2015).

[85] R. Sabatini, T. Gorni, and S. de Gironcoli, Phys. Rev. B 87, 041108 (2013).

[86] J. P. Perdew, M. Ernzerhof, and K. Burke, J. Chem. Phys. 105, 9982 (1996).

[87] A. V. Krukau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, J. Chem. Phys. 125, 224106 (2006).

[88] M. S. Hybertsen and S. G. Louie, Phys. Rev. B 34, 5390 (1986).

[89] F. Bruneval, N. Vast, and L. Reining, Phys. Rev. B 74, 045102 (2006).

[90] D. Huang and C. Persson, Thin Solid Films 535, 265 (2013).

[91] P. Prabeesh, I. P. Selvam, and S. Potty, Mater. Res. Express. 6, 065509 (2019).

[92] M. Engel, H. Miranda, L. Chaput, A. Togo, C. Verdi, M. Marsman, and G. Kresse,

Phys. Rev. B 106, 094316 (2022).

[93] F. P. Sabino, X. G. Zhao, G. M. Dalpian, and A. Zunger, Phys. Rev. B 110, 035160 (2024).

[94] C. Malerba, F. Biccari, C. L. A. Ricardo, M. Valentini, R. Chierchia, M. Müller, A. Santoni, E. Esposito, P. Mangiapane, P. Scardi, et al., J. Alloys Compd. 582, 528 (2014).

[95] J. P. Perdew, Int. J. Quantum Chem. 28, 497 (1985).

[96] P. Borlido, T. Aull, A. W. Huran, F. Tran, M. A. L. Marques, and S. Botti, J. Chem. Theory Comput. 15, 5069 (2019).

[97] K. Momma and F. Izumi, J. Appl. Cryst. 41, 653 (2008).

[98] S. Chen, J.-H. Yang, X. G. Gong, A. Walsh, and S.-H. Wei, Phys. Rev. B 81, 245204 (2010).

[99] S. Kim, J.-S. Park, and A. Walsh, ACS Energy Lett. 3, 496 (2018).

[100] W. Xiao, J. Wang, X. Zhao, J. Wang, G. Huang, L. Cheng, L. Jiang, and L. Wang, Solar Energy 116, 125 (2015).

[101] T. Maeda, S. Nakamura, and T. Wada, Jpn. J. Appl. Phys. 50, 04DP07 (2011).

[102] M. Kumar, A. Dubey, N. Adhikari, S. Venkatesan, and Q. Qiao, Energy Environ. Sci. 8, 3134 (2015).

[103] L. Wang, J. Ban, L. Han, Z. Zhou, W. Zhou, D. Kou, Y. Meng, Y. Qi, S. Yuan, and S. Wu, J. Mater. Chem. A 12, 25643 (2024).

[104] S. Schorr, G. Gurieva, M. Guc, M. Dimitrievska, A. Pérez-Rodríguez, V. Izquierdo-Roca, C. S. Schnohr, J. Kim, W. Jo, and J. M. Merino, J. Phys. Energy 2, 012002 (2019).

[105] S. Schorr, H.-J. Hoebler, and M. Tovar, Eur. J. Mineral., 65 (2007).

[106] S. Schorr, Sol. Energy Mater. Sol. Cells 95, 1482 (2011).
 
