
# Magnetocrystalline anisotropy of Laves phase  \( Fe_{2}Ta_{1-x}W_{x} \)  from first principles - the effect of 3d-5d hybridisation

Alexander Edström

Department of Physics and Astronomy, Uppsala University, Box 516, 75121 Uppsala, Sweden

The magnetic properties of  \( Fe_{2}Ta \)  and  \( Fe_{2}P \)  in the hexagonal Laves phase are computed using density functional theory in the generalised gradient approximation, with the full potential linearised augmented plane wave method. The alloy  \( Fe_{2}Ta_{1-x}W_{x} \)  is studied using the virtual crystal approximation to treat disorder.  \( Fe_{2}Ta \)  is found to be ferromagnetic with a saturation magnetization of  \( \mu_{0}M_{s}=0.66 \)  T while, in contrast to earlier computational work,  \( Fe_{2}P \)  is found to be ferrimagnetic with  \( \mu_{0}M_{s}=0.35 \)  T. The transition from the ferri- to the ferromagnetic state occurs for  \( x\leq0.1 \) . The magnetocrystalline anisotropy energy (MAE) is calculated to  \( 1.25~MJ/m^{3} \)  for  \( Fe_{2}Ta \)  and  \( 0.87~MJ/m^{3} \)  for  \( Fe_{2}P \) . The MAE is found to be smaller for all values x in  \( Fe_{2}Ta_{1-x}W_{x} \)  than for the end compounds and it is negative (in-plane anisotropy) for  \( 0.1\leq x\leq0.9 \) . The MAE is carefully analysed in terms of the electronic structure. Even though there are weak 5d contributions to the density of states at the Fermi energy in both end compounds, a reciprocal space analysis, using the magnetic force theorem, reveals that the MAE originates mainly from regions of the Brillouin zone with strong 3d-5d hybridisation near the Fermi energy. Perturbation theory and its applicability in relation to the MAE is discussed.

The magnetocrystalline anisotropy energy (MAE) is the intrinsic relativistic feature, originating from spin-orbit coupling (SOC) \( ^{1} \) , of magnetic materials that the energy depends on the direction of magnetization relative to the crystal lattice. It is crucial in a wide range of applications, from permanent magnets \( ^{2-5} \)  to magnetic storage devices \( ^{6} \) . The SOC is strong in heavy elements such as rare-earths (REs) and actinides which consequently acquire large MAE, while in applications it is highly desirable to obtain a large MAE without such expensive or inaccessible constituent elements \( ^{7} \) . One compound which has gained much attention due to its huge MAE is tetragonal FePt \( ^{8-12} \) . This material acquires its magnetisation mainly from Fe, while the important factors resulting in the large MAE include the strong SOC of the Pt atom, as well as the uniaxial crystal structure. The crystal structure is crucial because highly symmetric, e.g. cubic, crystals tend to have at least one order of magnitude lower MAE. Nevertheless, FePt contains large amounts of the valuable element Pt, whereby alternative magnetic 3d-5d composites in uniaxial crystal structures can be of great technological value. One such compound is hexagonal Laves phase  \( Fe_{2}W \) , which was initially reported by Arnfelt and Westgren \( ^{13} \)  and recently attracted some attention in the context of permanent magnet replacement materials \( ^{14,15} \) . Early electronic structure calculations \( ^{16} \)  failed to establish the existence of ferromagnetism in the compound from the Stoner criterion. While it now seems clear that the compound is magnetically ordered \( ^{14,15} \) , a thorough understanding of the magnetism in this material appears to be absent in literature and some discrepancies can be seen between recent computational \( ^{14} \)  and experimental work \( ^{15} \) . For example, calculations \( ^{14} \)  overestimated the saturation magnetization by nearly thirty percent and provided a vastly different MAE when compared to experimental data from nanoparticles \( ^{15} \) . It is therefore the purpose of this work to use state of the art electronic structure calculations to unambiguously determine the magnetic ground state of the  \( Fe_{2}W \)  compound and investigate the magnetic properties, including the technologically important intrinsic properties of saturation magnetization ( \( M_{s} \) ) and MAE. The closely related compound  \( Fe_{2}Ta \)  is isostructural to  \( Fe_{2}P \)  \( ^{17} \)  and also studied. Some focus will be put on the MAE, which will be carefully analysed in terms of the electronic structure. Furthermore, the possibility to tune the MAE by alloying W and Ta will be examined and a discussion of the underlying physical principles provided.

Density functional theory (DFT) calculations in the generalized gradient approximation \( ^{18} \)  (GGA) were performed with the full-potential linearized augmented plane waves (FP-LAPW) method as implemented in WIEN2k \( ^{19} \) . Initially, spin-polarized calculations were performed in the scalar relativistic approximation, but to calculate the MAE, SOC must be included and this was done in a second variational approach \( ^{20} \) . The size of the basis set used is typically described by the product of the smallest muffin-tin sphere and the largest reciprocal lattice vector included,  \( RK_{max} \) . For structure optimizations, this value was set to  \( RK_{max} = 7 \) , while for MAE calculations a larger value of  \( RK_{max} = 9 \)  was used. To obtain a well converged formation energy, a value as large as  \( RK_{max} = 9.5 \)  was needed. Integration of k-points over the Brillouin zone was performed using the improved tetrahedron method \( ^{21} \)  and 700 k-points in the full Brillouin zone (48 in the irreducible wedge of the Brillouin zone after considering the 24 symmetry operations of the crystal) were used for structure optimization, 1500 for the calculation of formation energy and as many as 30000 k-points were used in order to obtain well converged MAE values.

One unit cell of the relevant crystal structure contains two inequivalent Fe positions with multiplicity two and six respectively, as well as two equivalent 5d sites. Calculations were performed with the initial spin state either in ferro or ferrimagnetic configurations, i.e. parallel or an-
 

Table I: Lattice parameters and parameters of the internal atomic positions, magnetic moments, saturation magnetization and formation energy of Fe2W and Fe2Ta as calculated in a scalar relativistic, spin polarized GGA calculation, neglecting SOC, in WIEN2k.

<table><tr><td></td><td>Fe2Ta</td><td>Fe2W</td></tr><tr><td>a ( \( \textup{\AA} \) )</td><td>4.811</td><td>4.674</td></tr><tr><td>c ( \( \textup{\AA} \) )</td><td>7.874</td><td>7.768</td></tr><tr><td>xFe2</td><td>0.83192</td><td>0.82946</td></tr><tr><td>z5d</td><td>0.06405</td><td>0.06924</td></tr><tr><td>m(Fe1) ( \( \mu \) B)</td><td>0.90</td><td>-1.14</td></tr><tr><td>m(Fe2) ( \( \mu \) B)</td><td>1.43</td><td>1.17</td></tr><tr><td>m(5d) ( \( \mu \) B)</td><td>-0.24</td><td>-0.05</td></tr><tr><td>m_{tot} ( \( \mu \) B/u.c.)</td><td>8.88</td><td>4.45</td></tr><tr><td>\( \mu_{0}M_{s} \)  (T)</td><td>0.66</td><td>0.35</td></tr><tr><td>Formation energy (eV/u.c.)</td><td>-2.82</td><td>-0.63</td></tr></table>

tiparallel alignment of spins on the two different Fe positions. In the case of  \( Fe_{2}Ta \) , the total energy was found to be approximately 1.8 eV per unit cell lower in the case of ferromagnetic ordering compared to ferrimagnetic ordering. For  \( Fe_{2}W \) , on the other hand, all calculations converged into the ferrimagnetic state, regardless of initial spin configuration and lattice parameters. Lattice parameters were calculated by minimizing the total energy with respect to volume and c/a and relaxing the internal atomic positions in each step. The calculated lattice parameters are reported in Table I, which also contains spin magnetic moments and the corresponding saturation magnetizations as well as formation energies. For  \( Fe_{2}Ta \) , the lattice parameters have been experimentally reported as  \( a = 4.833 \AA \)  and  \( c = 7.868 \AA^{17} \)  and for  \( Fe_{2}W \) ,  \( a = 4.727 \AA \)  and  \( c = 7.704 \AA^{13} \) , in close agreement with the calculated values in Table I, although for  \( Fe_{2}W \) , c/a is slightly larger in the calculated data. The Fe moments in  \( Fe_{2}W \)  are of similar size and opposite sign but as there are two and six of the respective Fe sites in one unit cell, there is a net total of  \( 4.45 \mu_{B}/u.c. \) , corresponding to a saturation magnetization of  \( \mu_{0}M_{s} = 0.35 T \) . Since in  \( Fe_{2}Ta \)  the Fe moments are parallel, the total magnetic moment and corresponding saturation magnetization is significantly larger, reaching a value of  \( \mu_{0}M_{s} = 0.66 T \) . Ta and W have a small induced moments of  \( -0.24 \mu_{B} \)  and  \( -0.05 \mu_{B} $ , anti-parallel to the total magnetic moment, respectively, as is typical for these 5d atoms in a magnetic 3d host \( ^{22} \) .

Since a different magnetic ordering, with a magnetic moment close to zero on the first Fe site and a larger moment moment around  \( 1.3\mu_{B} \)  on the second Fe atom, has been reported in earlier computational work (pseudopotential DFT calculations in the GGA) \( ^{14} \)  for  \( Fe_{2}W \) , further investigation seems necessary to unambiguously determine the correct magnetic ground state within the GGA. Hence, fixed spin moment calculations, allowing the total magnetic moment of the system to be constrained to a fixed given value, were performed. The total magnetic moment was varied around the value of  \( 6.8\mu_{B}/u.c. \) , previously reported \( ^{14} \) . Magnetic moments of  \( -0.05\mu_{B} \)  and  \( 1.25\mu_{B} \) , were then obtained on the two Fe atoms, which is similar to the earlier computational results \( ^{14} \) . Initially, the lattice parameters were set to the values mentioned in Ref \( ^{14} \)  but then attempts were made at optimizing the crystal structure with fixed magnetic moment to lower the energy further. However, all calculations resulted in total energies which were higher than those obtained for the structure given in Table I and no minimum could be located in the total energy as function of total magnetic moment. Based on these results, the most probable conclusion appears to be that the authors of Ref \( ^{14} \)  assumed a ferromagnetic order as initial state and reached a local energy minimum for the magnetic moments were reported. The correct magnetic moments corresponding to the global energy minimum, within the GGA, based on all results obtained here, are expected to be those in Table I. The explanation given here is consistent with the observation that the previous computational work presented a value of  \( \mu_{0}M_{s} \)  as approximately 0.56 T which overestimated the experimental low temperature value of approximately  \( \mu_{0}M_{s} = 0.44 \)  T. Nevertheless, the value given in this work somewhat underestimates the experimental result. A possible source of discrepancy is surface effects of the nanoparticles, where enhanced magnetic moments could appear near the surface.

Somewhat surprisingly, a non-negligible difference is seen also in lattice parameters and total magnetic moment for  \( Fe_{2}Ta \) , when comparing to previous computational work \( ^{14} \) , where a = 4.825 Å and c/a = 1.6329 (corresponding to c = 7.879 Å) was reported. The difference in a is merely 2% and might be expected for the two different computational methods. The difference in total spin magnetic moment is, however, larger. For example, the magnetic moment on the  \( Fe_{1} \)  is computed to 0.90  \( \mu_{B} \) , while the other authors reported a value well above 1  \( \mu_{B} \) . The reason for this discrepancy is difficult to pinpoint exactly, as both sets of calculations are performed in the GGA \( ^{18} \) , but might partly be related to the difference in lattice parameters.

By comparing the total energy of  \( \mathrm{Fe}_{2}(\mathrm{Ta}/\mathrm{W}) \)  in the calculated ground state with that of bcc Fe and bcc Ta or W, the formation energy was calculated to -0.63 eV/u.c for  \( Fe_{2}W \) , which is lower than the value close to zero previously reported \( ^{14} \) . A negative formation energy is expected for a stable phase and a possible scenario appears to be that the authors of Ref. \( ^{14} \)  obtained a too high formation energy due to calculating a local energy minimum and thus a too high total energy. For  \( Fe_{2}Ta \) , the formation energy is lower and this compound may therefore be expected to be more stable and form more easily in nature.

In order to compute the MAE, calculations were performed including SOC, which also results in a non-zero
 

orbital magnetic moment, that is otherwise quenched. The computed spin magnetic moments  \( (m_{\mathrm{S}}) \) , orbital magnetic moments  \( (M_{\mathrm{L}}) \)  and MAEs are listed in Table II. When the magnetization is along the a-axis, the SOC results in a lowering of symmetry so that the second Fe site with initially six equivalent atoms are split into two types with two and four Fe atoms of each, labelled  \( Fe_{2} \)  and  \( Fe_{3} \)  respectively. Hence, the spin and orbital moments are same for  \( Fe_{2} \)  and  \( Fe_{3} \)  when the magnetization is along the c-axis but not when it is along the a-axis. The MAE is calculated to  \( E_{MAE} = 1.24 \, meV/u.c. = 1.25 \, MJ/m^{3} \)  for  \( Fe_{2}Ta \)  and  \( E_{MAE} = 0.79 \, meV/u.c. = 0.87 \, MJ/m^{3} \)  for  \( Fe_{2}W \) , with easy magnetization axis along the c-direction of the crystal in both cases. The calculated uniaxial MAE for  \( Fe_{2}W \)  presented here is in better agreement with the small uniaxial MAE recently presented in experimental work \( ^{15} \)  than the large in plane MAE previously computed for the  \( Fe_{2}W \)  compound \( ^{14} \) . Nevertheless, the computed value found in this work is significantly larger than the reported experimental value of  \( 286 \, kg/cm^{3} = 28.6 \, kJ/m^{3} \) . However, measurements have only been presented for nanoparticles, while unambiguous MAE measurements require single crystals. For  \( Fe_{2}Ta \) , an experimental MAE has not been found in literature, but the value calculated here differs notably from the value of  \( E_{MAE} = -1.4 \, meV/u.c. \)  previously calculated \( ^{14} \) . This discrepancy is most likely related to the difference in magnetic moments obtained, as mentioned above, but could also be partially related to other computational details, such as the treatment of SOC or core electrons.

Fig. 1 shows the spin polarized density of states (DOS) for  \( Fe_{2}Ta \)  (a) and  \( Fe_{2}F \)  (b). The majority spin DOS is similar for the two compounds, with the Fermi energy ( \( E_{F} \) ) at approximately the same location. However, as Ta is exchanged for W more electrons are added into the system and the minority spin states become occupied, whereby these are shifted more to the left in Fig. 1b) and, as a result,  \( E_{F} \)  coincides with the bottom of a valley in the minority spin DOS of  \( Fe_{2}F \) . Thus the DOS( \( E_{F} \) ) for  \( Fe_{2}F \)  is dominated by minority spin states, in contrast to  \( Fe_{2}Ta \) , where the opposite is true. This fact will be of importance later when analysing the relation between MAE and orbital moment anisotropy. It is also interesting to note that the minority spin DOS of  \( Fe_{2}F \)  has a valley at  \( E_{F} \) , resulting in a higher degree of spin polarization of the DOS( \( E_{F} \) ) compared to  \( Fe_{2}Ta \) . In both cases, the DOS( \( E_{F} \) ) is dominated by Fe, with rather modest contributions from the 5d atoms. This might be one important reason, together with other details in the band structure around  \( E_{F} \) , why these compounds do not possess larger MAE. Even the  \( L_{1} \)  phase of MnAl exhibits an MAE well above 1 MJ/m \( ^{3} \)  without any constituent element heavier than a 3d atom. Heavier atoms, such as 5d's, should allow significantly larger MAE, e.g., 4 MJ/m \( ^{3} \)  or more \( ^{24} \)  in FePt. However, this requires significant 3d-5d hybridisation around  \( E_{F} \) , as is seen in FePt \( ^{25} \) , but appears to be limited in the compounds studied here.

Table II: Spin magnetic moments,  \( m_{S} \) , orbital magnetic moments  \( m_{L} \) , saturation magnetizations and MAE for  \( Fe_{2}W \)  as calculated in WIEN2k, including SOC with magnetization either along 100 or 001 directions and using the lattice parameters presented in Table I.

<table><tr><td>Fe2Ta</td><td>m || 100</td><td>m || 001</td></tr><tr><td>mS(Fe1) (μB)</td><td>0.943</td><td>0.932</td></tr><tr><td>mS(Fe2) (μB)</td><td>1.433</td><td>1.432</td></tr><tr><td>mS(Fe3) (μB)</td><td>1.427</td><td>1.432</td></tr><tr><td>mS(Ta) (μB)</td><td>-0.240</td><td>-0.238</td></tr><tr><td>mL(Fe1) (μB)</td><td>0.070</td><td>0.109</td></tr><tr><td>mL(Fe2) (μB)</td><td>0.091</td><td>0.099</td></tr><tr><td>mL(Fe3) (μB)</td><td>0.101</td><td>0.099</td></tr><tr><td>mL(Ta) (μB)</td><td>0.033</td><td>0.034</td></tr><tr><td>μ0Ms(T)</td><td>0.69</td><td>0.69</td></tr><tr><td>Energy (meV/u.c.)</td><td>1.24</td><td>0</td></tr><tr><td>Energy (MJ/m3)</td><td>1.25</td><td>0</td></tr><tr><td>Fe2W</td><td>m || 100</td><td>m || 001</td></tr><tr><td>mS(Fe1) (μB)</td><td>-1.148</td><td>-1.150</td></tr><tr><td>mS(Fe2) (μB)</td><td>1.163</td><td>1.172</td></tr><tr><td>mS(Fe3) (μB)</td><td>1.172</td><td>1.172</td></tr><tr><td>mS(W) (μB)</td><td>-0.044</td><td>-0.043</td></tr><tr><td>mL(Fe1) (μB)</td><td>-0.066</td><td>-0.151</td></tr><tr><td>mL(Fe2) (μB)</td><td>0.045</td><td>0.039</td></tr><tr><td>mL(Fe3) (μB)</td><td>0.074</td><td>0.039</td></tr><tr><td>mL(W) (μB)</td><td>0.002</td><td>0.002</td></tr><tr><td>μ0Ms(T)</td><td>0.36</td><td>0.35</td></tr><tr><td>Energy (meV/u.c.)</td><td>0.79</td><td>0</td></tr><tr><td>Energy (MJ/m3)</td><td>0.87</td><td>0</td></tr></table>

Nevertheless, the contribution from Ta (3.2 states/eV for both spin channels summed) is greater than that of W (1.8 states/eV). This is consistent with the observation that the MAE is greater in the compound containing Ta, although other differences in the electronic structure are also expected to play a role. One more interesting observation in the DOS is that the minority spin DOS of  \( Fe_{2}W \)  has a valley at  \( E_{F} \) , resulting in a higher degree of spin polarization of the  \( \mathrm{DOS}(E_{\mathrm{F}}) \)  compared to  \( Fe_{2}Ta \) .

In a system with weak SOC, such as 3d-based itinerant magnets, where  \( \xi \)  is significantly smaller than the bandwidth (less than 100 meV compared to several eV), it is reasonable to describe the effect of SOC in terms of perturbation theory and important insights can be gained by doing so \( ^{26-28} \) . For a uniaxial crystal the leading term is of second order while for cubic crystals it is fourth order. Andersson et al. \( ^{28} \)  discussed the case of having several atomic types and hybridisation between these in a tight-binding description. One can consider unperturbed single particle states at the point k in the Brillouin zone.
 
![](./images/867768681097069331_1.jpg)

![](./images/867768681097069331_2.jpg)

Figure 1: Spin polarized DOS for  \( Fe_{2}Ta \)  in a) and  \( Fe_{2}F \)  in b).

as

 \[ |\mathbf{k},i\rangle=\sum_{q,\mu}c_{\mathbf{k},i,q,\mu}|\mathbf{k},q,\mu,\sigma_{i}\rangle, \quad (1) \] 

with summation over atomic sites q and orbital states  \( \mu \) , but not over the spin  \( \sigma_{n} \)  since the unperturbed states each have well defined spin. With on site SOC, The shift in the energy eigenvalue  \( E_{k,i} \)  associated with  \( |k,i\rangle \)  is

 \[ \begin{align*}\Delta E_{\mathbf{k},i}(\hat{\mathbf{n}})=-\sum_{j\neq i}\sum_{q q^{\prime}}\sum_{\mu\mu^{\prime}}\sum_{\mathbf{m}}\eta_{\mathbf{k},i,q\mu,q^{\prime}\mathbf{m}^{\prime \prime\prime}\mathbf{n}_{\mathbf{k},j,q^{\prime}\mathbf{m}^{\prime \prime\prime}\mathbf{n}_{\mathbf{k},j,q^{\prime \prime}\mathbf{m}^{\prime \prime\prime}}}}\cdot\\ \cdot\frac{\langle q\mu\sigma_{i}|\xi_{\mathbf{q}}\hat{\mathbf{1}}\cdot\hat{\mathbf{s}}|q\mu^{\prime}\sigma_{j}\rangle\langle q^{\prime}\mathbf{m}^{\prime \prime}\sigma_{j}|\xi_{q^{\prime}}\hat{\mathbf{1}}\cdot\hat{\mathbf{s}}|q^{\prime}\mathbf{m}^{\prime \prime \prime}\sigma_{i}\rangle}{E_{\mathbf{k},j}-E_{\mathbf{k},i}},\end{align*} \quad (2) \] 

with occupation numbers  \( n_{\mathbf{k},i,q,\mu,q',\mu''} = c_{\mathbf{k},i,q,\mu}^{*} c_{\mathbf{k}, i,q',\mu''} \)  and spin and orbital angular momentum operators  \( \hat{s} \)  and  \( \hat{1} \) . For a given q and k, it is clear that the effect of the SOC is determined by matrix elements of the form  \( \langle \mu_{i}, \sigma_{i} | \hat{1} \cdot \hat{s} | \mu_{j}, \sigma_{j} \rangle \)  and for convenience these are listed with respect to spin and d-orbitals in the appendix.  \( \hat{n} \)  is the spin quantization axis (magnetization direction) and the dependence of  \( \Delta E_{\mathbf{k},i}(\hat{\mathbf{n}}) \)  on this quantity comes from the SOC matrix elements. For the total shift in  \( E_{\mathbf{k},i} \) , the coupling between all states  \( j \neq i \)  should be considered. However, if both i and j denote occupied states there will be a cancellation when these are summed over to compute the total energy. Therefore, only coupling between occupied and unoccupied states are relevant, except possibly in the small regions of the Brillouin zone where deformations of the Fermi surface occur, as was pointed out by Kondorskii and Straube \( ^{26} \) . This leads to the important and well established conclusion that the MAE is determined by the electronic band structure near the Fermi energy, in particular by the coupling between occupied and unoccupied states. One more important observation from Eq. 2 is that regions in the band structure with significant Fe-Ta hybridisation will allow MAE contributions of order  \( \frac{\xi_{Ta}\xi_{Fe}}{E_{\mathbf{k},j}-E_{\mathbf{k},i}} \) , which is significantly larger than  \( \frac{\xi_{Fe}^{2}}{E_{\mathbf{k},j}-E_{\mathbf{k},i}} \) , since  \( \xi_{Ta} \)  is several times larger than  \( \xi_{Fe} \) , or similarly for W instead of Ta.

From the discussion above it is motivated to perform a careful analysis of the electronic band structure near the Fermi energy to obtain a better understanding of the MAE. Fig. 2a)-f) shows the spin polarized band structure through various high symmetry points in the Brillouin zone, without SOC, for  \( Fe_{2}Ta \) , with spin up states on the left side and spin down states on the right side. Color coding is used to show the orbital character of the bands with red, green and blue indicating  \( m = 0 \)  ( \( d_{z^{2}} \) ),  \( m = 1 \)  ( \( d_{xz} \)  or  \( d_{yz} \) ) and  \( m = 2 \)  ( \( d_{xy} \)  or  \( d_{x^{2}-y^{2}} \) ) character, respectively, for different atomic types in the different rows. A black region on a band indicates that the given atomic type is not significantly contributing to the band in that region. The large number of bands present, even within one electronvolt from the Fermi surface, and complicated band structure with further complication due to hybridisation, makes analysis of the MAE in terms of the band structure difficult. Some observation can, nevertheless, directly be made. The  \( \Gamma \)  point is often of particular importance since it has the highest symmetry. Here there are occupied and unoccupied spin up states very near the Fermi energy at this point, potentially allowing very strong effect from the SOC, especially since these states both show strong Ta contributions and Ta has the largest SOC constant. However, the unoccupied band is largely of m = 0 character, while the occupied one is of m = 1 character. Such states do not couple via SOC (see Table IV), whereby the potentially strong MAE contribution at  \( \Gamma \)  is absent.

To obtain information about which regions in reciprocal space are particularly important to the MAE, the band structures after applying SOC with magnetization along either 100 or 001 directions are plotted in Fig. 2g). From these bands the MAE contribution per k-point can be evaluated using the magnetic force theorem \( ^{29} \) , by taking the difference of the sum over occupied energy eigenvalues for different magnetization directions, which is also plotted (red line, right y-axis) in Fig. 2g). Since the MAE is positive in  \( Fe_{2}Ta \) , regions with positive MAE contributions are expected to outweigh the negative regions. In agreement with the observation mentioned about  \( \Gamma \)  above, there is a rather weak MAE contribution from the region around that point. Instead, it is clear that the most important region is that around the A-point where a large and positive MAE contribution is seen,
 

while other regions show smaller values of varying sign, which one might expect to nearly cancel out in a Brillouin zone integration. From a first look at the bands in Fig. 2a)-f), the most important bands for the MAE at A should be the highest occupied and lowest unoccupied ones, which are in both cases spin down with fourfold degeneracy. However, in Fig. 2g) one can identify the strongest positive MAE contribution where occupied 001-bands (blue dashed line) are shifted well below the corresponding 100-bands (black dash-dotted line). This occurs mainly for the highest occupied (also four-fold degenerate) spin up bands at A, whereby these should also be considered. The three sets of band which thus far appear most important at A all have significant contributions from several atomic types and orbitals, in particular Ta and  \( Fe_{1} \) , m = 1 and m = 2 states, but for the lowest unoccupied spin down bands,  \( Fe_{2} \)  m = 1 and m = 2 are also important. This means that detailed analysis of the MAE contribution from the A-point is complicated since a large number of terms from Eq. 2 must be considered. It is clear, however, that there is a significant Fe-Ta hybridisation in the relevant region and as was pointed out above, this allows for significant additions to the MAE.

Fig. 3 contains the same type of information as Fig. 2, but for  \( Fe_{2}W \) . Since  \( Fe_{2}F \)  also has a uniaxial (positive) MAE, positive regions are expected to dominate the MAE contributions in Fig. 3g). In similarity with the  \( Fe_{2}Ta \)  case, there are large regions of small contributions with varying sign, which one would expect to nearly vanish in an integration. In particular, the important  \( \Gamma \) -point provides a weak contribution, which can be understood from the relatively large separation in energy between the highest occupied and lowest unoccupied states, compared to other regions. The most important positive contributions to the MAE stem from the L-neighbourhood, as well as a region along the path A-H, while there is a significant negative region around M, which might partially explain why the MAE of  \( Fe_{2}W \)  is weak. In the important region along the A-H path, there are two spin up bands nearly parallel to each other. These are on opposite sides of the Fermi energy where the k-point resolved MAE is strongest, and can therefore contribute to the MAE. Both bands are mainly of W and  \( Fe_{1} \)  m=1 character. From the SOC matrix elements in the appendix, one finds that states of same spin and m value yield a positive (uniaxial) contribution to the MAE. Furthermore, the Fe-W hybridisation allows the large W SOC to make the coupling strength large and this explains the large positive MAE coming from that part of the A-H path.

At the L-point, a significant positive source of MAE is found in the highest occupied spin up states which are mainly Ta and  \( Fe_{1} \)  m = 1, since the 001 bands are shifted below the 100 bands. This situation is reversed as one moves along the L - M path and the change of sign in the k-resolved MAE appears to coincide with the spin down bands which are unoccupied at L becoming occupied near M. The presence of many bands with significant hybridisation effects makes it difficult to pinpoint states coupling via SOC which are particularly important to the MAE along the L - M path. Nevertheless, it should be pointed out that once again there is significant Fe-W hybridisation, so that the strong W SOC can increase the MAE. Since there is a limited 5d contribution to the DOS at the Fermi energy, there can only be significant 3d-5d hybridisation near the Fermi energy in a limited region of the Brillouin zone. Nevertheless, the reciprocal space analysis of the electronic structure and MAE contributions reveals that the MAE is mainly determined by those regions in the Brillouin zone where there is notable 3d-5d hybridisation, in both  \( Fe_{2}Ta \)  and  \( Fe_{2}F \) .

As both quantities are due to the SOC, Bruno \( ^{27} \)  pointed out the close relation between magnetocrystalline anisotropy and orbital moments and showed, using perturbation theory on a tight binding model, that if deformations of the Fermi surface can be neglected and the MAE is dominated by spin-diagonal coupling, the MAE and orbital magnetic moment anisotropy are proportional. If coupling between minority spin states dominates the SOC, a maximum orbital magnetic moment is expected in the easy direction of magnetization, as is seen in the case of  \( Fe_{2}Ta \)  in Table II. If, on the other hand, the SOC is dominated by the coupling between majority spin states, a maximum orbital magnetic moment is expected along the hard magnetisation axis, as is seen in the case of  \( Fe_{2}F \) . This is consistent with the observation made in Fig. 1, that the  \( Fe_{2}Ta \)  DOS( \( E_{F} \) ) is dominated by minority spin states, while the opposite is true for  \( Fe_{2}F \) . For a further analysis of the relation between MAE and  \( m_{L} \)  in the studied systems, energy and orbital moments have been computed as functions of the angle  \( \theta \)  (with  \( \phi = 0 \) ) when the magnetization is along  \( \hat{\mathbf{n}} = (\sin \theta \cos \phi, \sin \theta \sin \phi, \cos \theta) \) . The result for the energy as a function of  \( \theta \)  is shown in Fig. 4. The second order perturbation theory for a uniaxial system leads to the conclusion that the energy as a function of  \( \theta \)  follows the relation

 \[ E(\theta)=K_{0}+K_{1}\sin^{2}\theta, \quad (3) \] 

with isotropic energy  \( K_{0} \) . This is merely the first part of the longer expansion

 \[ \begin{aligned}E(\theta,\phi)&=K_{0}+K_{1}\sin^{2}\theta+K_{2}\sin^{4}\theta+\\&\quad+K_{3}\sin^{6}\theta\left(1+k_{3,3}\cos3\phi+k_{3,6}\cos6\phi\right)+...\end{aligned} \quad (4) \] 

valid for a uniaxial crystal with three-fold rotational symmetry about the z-axis, such as the one studied here. For a system where the MAE is well described by second order perturbation theory, one expects that the energy is well fitted by Eq. 3 and that  \( K_{i} \)  is vanishingly small for i > 1. As seen in Fig. 4a), fitting the energy as a function of angle between magnetization direction and 001-direction to  \( K_{1}\sin^{2}\theta \)  provides an unsatisfactory curve for  \( E(\theta) \)  for both  \( Fe_{2}Ta \)  and  \( Fe_{2}F \) , while including also the term
 
![](./images/867768681097069331_3.jpg)

(a) Fe \( _{1} \) , spin up.

![](./images/867768681097069331_4.jpg)

(b) Fe \( _{1} \) , spin down.

![](./images/867768681097069331_5.jpg)

(c) Fe \( _{2} \) , spin up.

![](./images/867768681097069331_6.jpg)

(d) Fe \( _{2} \) , spin down.

![](./images/867768681097069331_7.jpg)

(e) Ta, spin up.

![](./images/867768681097069331_8.jpg)

(f) Ta, spin down.

![](./images/867768681097069331_9.jpg)

(g) Band structure including SOC with magnetisation along 100 (black dash-dotted line) or 001-direction (blue dashed line) as well as the MAE contribution per k-point (red solid line).

Figure 2: Atomic type and spin resolved band structure of  \( Fe_{2}Ta \)  with the colors red, green and blue indicating the contribution of  \( m=0\left(\mathrm{d}_{z^{2}}\right) \) ,  \( m=1\left(\mathrm{d}_{xz} \)  or  \( d_{yz}\right) \)  and  \( m=2\left(\mathrm{d}_{xy} \)  or  \( d_{x^{2}-y^{2}}\right) \)  states respectively, in (a)-(f). Black bands mean that the d-orbitals of given atomic type do not contribute significantly to the band in that region. (g) shows bands with SOC as well as k-point resolved MAE contributions obtained via the magnetic force theorem.

 \( K_{2}\sin^{4}\theta \)  yields an excellent fit (for the fit to  \( K_{1}\sin^{2}\theta \) ,  \( K_{1} \)  was simply set to  \( E(\pi/2)-E(0) \) , while the fit to  \( K_{1}\sin^{2}\theta+K_{2}\sin^{4}\theta \)  was done with the method of least squares). This indicates that second order perturbation theory provides a quantitatively inaccurate description of the MAE in the studied compounds, while fourth order terms should provide an accurate description with higher (than fourth) order corrections being small. Clearly, the
 
![](./images/867768681097069331_10.jpg)

(a)  \( Fe_{1} \) , spin up.

![](./images/867768681097069331_11.jpg)

(b)  \( Fe_{1} \) , spin down.

![](./images/867768681097069331_12.jpg)

(c)  \( Fe_{2} \) , spin up.

![](./images/867768681097069331_13.jpg)

(d)  \( Fe_{2} \) , spin down.

![](./images/867768681097069331_14.jpg)

(e) W, spin up.

![](./images/867768681097069331_15.jpg)

(f) W, spin down.

![](./images/867768681097069331_16.jpg)

(g) Band structure including SOC with magnetisation along 100 (black dash-dotted line) or 001-direction (blue dashed line) as well as the MAE contribution per k-point (red solid line).

Figure 3: Atomic type and spin resolved band structure of  \( Fe_{2}W \)  with the colors red, green and blue indicating the contribution of  \( m = 0 \)  ( \( d_{z^{2}} \) ),  \( m = 1 \)  ( \( d_{xz} \)  or  \( d_{yz} \) ) and  \( m = 2 \)  ( \( d_{xy} \)  or  \( d_{x^{2}-y^{2}} \) ) states respectively, in (a)-(f). Black bands means that the d-orbitals of given atomic type do not contribute significantly to the band in that region. (g) shows bands with SOC as well as k-point resolved MAE contributions obtained via the magnetic force theorem.

fit to  \( K_{1}\sin^{2}\theta \)  is significantly better in the case of  \( Fe_{2}W \)  than for  \( Fe_{2}T_{a} \) . This indicates that restriction to second order perturbation theory, rather than fourth, is a better approximation for the W compound, which might be related to the smaller contribution of the 5d atom to the  \( \mathrm{DOS}(E_{\mathrm{F}}) \) , making the assumption of a small  \( \xi \)  more realistic.

The anisotropy constants obtained from the fitting to
 
![](./images/867768681097069331_17.jpg)

![](./images/867768681097069331_18.jpg)

Figure 4: Energy as a function of the polar angle  \( \theta \)  between the c-axis and the magnetization direction in a) and Energy as a function of the azimuthal angle  \( \phi \)  with  \( \theta = \frac{\pi}{2} \)  in b). The fit in b) is to a function  \( E(\theta = \frac{\pi}{2}, \phi) = C_{1} + C_{2} \cos 3\phi + C_{3} \cos 6\phi \)  and  \( \tilde{C}_{2} \cos 3\phi + C_{3} \cos 6\phi \)  is plotted.

 \( K_{1}\sin^{2}\theta+K_{2}\sin^{4}\theta \)  are listed in Table III. As was already anticipated from Fig. 4a),  \( K_{2} \)  is of more importance in  \( Fe_{2}Ta \)  and in fact it is of opposite sign and significantly bigger than  \( K_{1} \) . In the case where  \( K_{1}\sin^{2}\theta+K_{2}\sin^{4}\theta \)  has a sine sign, the  \( \theta \) -derivative of  \( E(\theta)=K_{1}\sin^{2}\theta+K_{2}\sin^{4}\theta \)  has only two zeros for real  \( K_{i} \) , namely  \( \theta=0 \)  and  \( \theta=\pi/2 \) , whereby the easy and hard magnetization directions will occur at these angles. For opposite signs of  \( K_{1} \)  and  \( K_{2} \) , an additional zero occurs at

 \[ \theta=\sin^{-1}(\sqrt{-\frac{K_{1}}{2K_{2}}}) \quad (5) \] 

and for  \( Fe_{2}Ta \)  there is a minimum in the energy at approximately  \( \theta = 0.15 = 8.8^{\circ} \) . The easy magnetization direction is thus expected at this angle rather than at  \( \theta = 0 \) , so the material strictly speaking does not have a uniaxial magnetization. For  \( Fe_{2}W \) , both constants are positive so  \( \theta = 0 \)  is the easy axis. Although in this case

Table III: Anisotropy constants \(K_{1}, K_{2}\) and \(\tilde{K}_{3} = K_{3}(1 + k_{3,3} + k_{3,6})\) from least squares fitting of \(E(\theta, \phi = 0)\) to \(K_{1}\sin^{2}\theta + K_{2}\sin^{4}\theta\) or \(K_{1}\sin^{2}\theta + K_{2}\sin^{4}\theta + \tilde{K}_{3}\sin^{6}\theta\) (see Fig. 4).

<table><tr><td></td><td>\( K_{1} \)  (meV/f.u.)</td><td>\( K_{2} \)  (mev/f.u.)</td><td>\(\tilde{K}_{3}\) (meV/f.u.)</td></tr><tr><td>Fe2Ta</td><td>-0.27</td><td>1.50</td><td></td></tr><tr><td>Fe2Ta</td><td>-0.19</td><td>1.23</td><td>0.19</td></tr><tr><td>Fe2W</td><td>0.50</td><td>0.30</td><td></td></tr><tr><td>Fe2W</td><td>0.45</td><td>0.46</td><td>-0.11</td></tr></table>

the magnitude of  \( K_{1} \)  is greater than  \( K_{2} \) , the latter is not negligible.

Table III also contains parameters from a fit to  \( K_{1}\sin^{2}\theta + K_{2}\sin^{4}\theta + \tilde{K}_{3}\sin^{6}\theta \) . This indicates non-negligible values of  \( \tilde{K}_{3} \)  for both compounds and, in the case of  \( Fe_{2}Ta \) , it is of the same magnitude as  \( K_{1} \) . However, it is not clear how many fitting parameters are reasonable to include with the given numerical accuracy. Comparison to a fit from a calculation with only  \( 2 \times 10^{4} \)  k-points yields a value smaller by a factor of one third for  \( Fe_{2}Ta \) , indicating that the numerical accuracy might be insufficient. However, more accurate calculations become prohibitively computationally demanding.

Typically, in uniaxial systems which do not possess strong SOC, the variation in energy for rotations of the magnetisation direction in the plane is small. This makes it challenging and computationally heavy to compute the in plane magnetic anisotropy (this might differ in, for example, actinide systems, where even cubic materials can have enormous MAE \( ^{30} \) ). Nevertheless, the energy as a function of  \( \phi \)  with  \( \theta = \frac{\pi}{2} \)  was computed and the result is shown in Fig. 4b). The calculated points have been fitted to  \( E(\theta = \frac{\pi}{2}, \phi) = C_{1} + C_{2} \cos 3\phi + C_{3} \cos 6\phi \)  ( \( C_{2} \)  and  \( C_{3} \)  should correspond to  \( K_{3}k_{3,3} \)  and  \( K_{3} k_{3,6} \) , respectively) and  \( C_{1} \)  has been subtracted from the calculated points and fitted curves. As expected, the variations in Fig. 4b) are much smaller, by nearly three orders of magnitude, than the variations seen in Fig. 4a). It is difficult to say whether the deviations between the computed points and the fitted lines are mainly due to limitations in the numerical accuracy or because of neglecting higher order terms.

Fig. 5 shows how the orbital magnetic moments vary with magnetization direction for  \( Fe_{2}Ta \)  (a) and  \( Fe_{2}P \)  (b). In both materials the greatest contribution to the orbital moment anisotropy is due to the  \( Fe_{1} \)  atom. The  \( Fe_{2} \)  and  \( Fe_{3} \)  atoms have identical orbital magnetic moments at  \( \theta = 0 \) , as expected from symmetry, while they deviate from one another at other directions. The compounds differ in the sign of the variation of the orbital magnetic moment with  \( \theta \) , although they both have same sign of  \( K_{1} + K_{2} \) . In Fig. 5c), which shows a plot of the energy as a function of  \( \theta \)  vs the anisotropy in total orbital magnetic moment as a function of  \( \theta \) , this appears as a difference in the sign of the slope of the curves.
 

As was previously mentioned, this can be understood in terms of the  \( \mathrm{DOS}(E_{\mathrm{F}}) \)  which is mainly due to the majority spin channel in  \( Fe_{2}W \)  and mainly due to the minority spin channel for  \( Fe_{2}Ta \) . According to the work of Bruno \( ^{27} \) , this should lead to approximate proportionality between  \( \Delta m_{L}(\theta) \)  and  \( E(\theta) \) , but with opposite signs in the proportionality constants. However, that was based on second order perturbation theory, and as was seen above, fourth order perturbation theory is expected to be necessary for a quantitative description of the magnetic anisotropy in these materials, especially in  \( Fe_{2}Ta \) . Fig. 5c) also shows a linear fit to the curves for  \( E(\theta) \)  vs  \( \Delta m_{L}(\theta) \) . For  \( Fe_{2}W \) , the linear fit provides a reasonable description of the curve, while in  \( Fe_{2}Ta \)  the deviation from linearity is more pronounced. This might largely be because of strong spin polarisation of the DOS at  \( E_{F} \)  for  \( Fe_{2}W \) , which makes the approximation that only spin diagonal SOC contributes to the magnetic anisotropy more reasonable. Although the  \( \mathrm{DOS}(E_{\mathrm{F}}) \)  in  \( Fe_{2}Ta \)  is dominated by minority spin states, the contribution from the majority spin channel is significant, whereby neglecting spin-off diagonal contributions is questionable. Furthermore, the stronger contribution from the 5d states could also affect the relation between MAE and orbital moment anisotropy in that direction, consistent with previous observations \( ^{28} \)  of non-proportionality between orbital magnetic moment and anisotropy in energy systems with significant 3d-5d hybridisation.

As the MAE depends sensitively on the band structure around the Fermi energy, it can be controlled by tuning the band structure around the Fermi energy. In practice this can be done, for example, by alloying, which will be explored next by considering the alloy  \( Fe_{2}Ta_{1-x}W_{x} \) . Due to the complicated electronic structure, which was illustrated in Fig. 2g) and Fig. 3g), it is difficult to predict the effect of alloying on properties such as the MAE without explicitly doing calculations to evaluate the properties. For the system studied here it is also of interest to investigate where the transition from ferro- to ferrimagnetism occurs. The virtual crystal approximation \( ^{31} \)  (VCA), in which the alloyed atoms are exchanged for virtual atoms with non-integer effective atomic numbers, Z, which on average have the right ionic charge and number of electrons for a given alloy concentration, will be used to treat the disorder. The VCA, although simple compared to more sophisticated single site approximations, such as the coherent potential approximation (CPA), often provides a good average description for properties such as magnetic moments \( ^{3,32-34} \) , especially for neighbours in the periodic table and small alloy concentrations \( ^{31} \) . For delicate properties, like the MAE, on the other hand, the VCA has often been seen to result in quantitative overestimates compared to CPA calculations \( ^{34,35} \) , super cell calculations \( ^{36,37} \)  or experiments \( ^{34,38,39} \) . Nevertheless, one should still be able to observe correct qualitative trends in the MAE from the VCA and it will be applied also for this property.

Calculations were performed for values of x in incre-

![](./images/867768681097069331_19.jpg)

(a) Orbital magnetic moment as function of  \( \theta \)  for  \( Fe_{2}Ta \) .

![](./images/867768681097069331_20.jpg)

(b) Orbital magnetic moment as function of  \( \theta \)  for  \( Fe_{2}W \) 

![](./images/867768681097069331_21.jpg)

(c) Change in energy versus change in orbital moment as  \( \theta \)  is varied from 0 to  \( \pi/2 \) .

Figure 5: Energy and orbital magnetic moments as function of the angle  \( \theta \)  between then magnetization direction and the 001 axis.

ments of 0.1. A calculation for x = 0.1 revealed that this is enough for the magnetic ordering to transition into the ferrimagnetic ordering observed also for  \( Fe_{2}W \) . A complete structural relaxation, using spin polarized calculations neglecting SOC, was thus performed for x = 0.1.
 

The resulting lattice parameters are  \( a = 4.771 \AA \)  and  \( c = 7.847 \AA \) . Lattice parameters for  \( 0.2 \leq x \leq 0.9 \)  were calculated by linear interpolation between the values obtained for x = 0.1 and x = 1.0. Calculations including SOC were then performed for the whole range of alloys and the resulting spin magnetic moments (for magnetization along the c-axis) and MAEs are presented in Fig. 6. A large decrease in total spin magnetic moment is seen when going from x = 0 to x = 0.1, due to the change in sign of the  \( Fe_{1} \)  spin moment, but also because of an accompanying reduction in size of the  \( Fe_{2} \)  moment. For x greater than 0.1, the total spin magnetic moment monotonically increases until x = 1.0. This appears to be from a combination of decrease in size of the  \( Fe_{1} \)  moment and increase in size of the  $ Fe_{2} \(  moment. The MAE decreases with x until it reaches a minimum at x = 0.5 and then increases until x = 1.0. Hence, the largest positive values of the MAE are obtained for the end compounds and it cannot be increased by the alloying considered here. A negative in-plane anisotropy of very large magnitude is seen for x = 0.5. However, it is important to remember that the VCA is expected to overestimate the magnitude of the MAE, whereby the real value might be of smaller magnitude.

![](./images/867768681097069331_22.jpg)

![](./images/867768681097069331_23.jpg)

Figure 6: a) Spin magnetic moments and b) MAE (computed as total energy differences for magnetizations along 100 and 001 directions) as functions of x in  \( Fe_{2}Ta_{1-x}W_{x} \) .

A comprehensive computational study has been performed for the hexagonal Laves phase compounds  \( Fe_{2}Ta \)  and  \( Fe_{2}F_{2}W \) , with focus on the important intrinsic magnetic properties saturation magnetization and MAE. For  \( Fe_{2}W \) , a new ferrimagnetic ground state has been suggested, different from that found in earlier computational work \( ^{[14]} \) . In the case of  \( Fe_{2}Ta \) , a similar magnetic ordering is found as in preceding calculations \( ^{[14]} \) , but an opposite sign is found in the MAE. The discrepancies in comparison with earlier calculations call for further experimental efforts to unambiguously determine the magnetic properties of these compounds.

The MAE has been carefully analysed in terms of the electronic structure and by using the magnetic force theorem to compute k-point resolved contributions to the MAE. Because the density of states at the Fermi energy is dominated by 3d states, 5d-states can only contribute notably to the MAE in small regions of the Brillouin zone. Nevertheless, it is found that the MAE originates mainly from regions in the Brillouin zone where there is a strong 3d-5d hybridisation, allowing the strong SOC of the 5d atoms to increase the MAE.

The main motivation to study uniaxial 3d-5d compounds is the possibility to have a very large MAE, such as the value of  \( 6.6 \, MJ/m^{3} \)  observed in FePt. When a significant amount of magnetic 3d elements is included, this can be combined with large saturation magnetisation and a high Curie temperature. Among the compounds studied here, the MAEs calculated are quite modest compared to that seen in FePt. In addition, for  \( Fe_{2}W \) , a ferrimagnetic ordering is found, resulting in a low saturation magnetisation. Nevertheless, whether a material is useful for a given application depends on a combination of the mentioned intrinsic parameters. For example, in the context of permanent magnets, the hardness parameter

 \[ \kappa=\sqrt{\frac{K}{\mu_{0}M^{2}}}, \quad (6) \] 

with MAE K and saturation magnetisation M, can be used to determine whether a material has potential to exhibit a reasonable coercive field and be used as a permanent magnet \( ^{4,5} \) .  \( \kappa \)  is required to be greater than unity but the microstructural engineering to obtain the desired properties of a permanent magnet should be easier with larger  \( \kappa \)  and Hirosawa \( ^{5} \)  suggested  \( \kappa > 1.4 \)  to be demanded from potential permanent magnet materials. For the materials studied here one finds  \( \kappa = 1.8 \)  for  \( Fe_{2}Ta \)  and  \( \kappa = 2.9 \)  for  \( Fe_{2}W \) , from the data in Table II, well above the requirement put forward by Hirosawa. These large values of  \( \kappa \)  appear largely because of the modest saturation magnetisations and the energy product of a permanent magnet will be limited by this. In both materials the saturation magnetisation is below the value of  \( \mu_{0}M_{s} = 1.6 \)  T \( ^{4} \)  found in the powerful  \( Nd_{2}Fe_{14}B \)  magnet. However, at least in  \( Fe_{2}Ta \)  the saturation magnetisation is greater than 0.48 T seen in  \( BaFe_{12}O_{19} \)  ferrite magnets, potentially making the compound technologically interesting as an intermediate alternative between rare-earth and ferrite magnets.

Experimental work has reported a Curie temperature of 550 K in  \( Fe_{2}W^{15} \) , which should be sufficient for many technological applications. As a useful extension of the
 

current work, it would be interesting to compute the Curie temperatures of  \( Fe_{2}W \)  and  \( Fe_{2}T_{a} \) , e.g., by calculating the Heisenberg exchange parameters from first principles and using these as input to the mean field approximation or Monte Carlo simulations. This would reveal whether  \( Fe_{2}T_{a} \)  also has a high enough Curie temperature to be technologically interesting and might also shed further light on the issue regarding the magnetic ordering of  \( Fe_{2}W \) .

To investigate the possibility of enhancing the relevant properties, alloying of W and Ta has been considered in calculations for  \( Fe_{2}Ta_{1-x}W_{x} \) , with the disorder treated in the virtual crystal approximation. These calculations indicate that the transition from ferro- to ferrimagnetic ordering occurs for x smaller than 0.1 and that the MAE is significantly reduced and mainly strongly negative in the alloy. For technological purposes this does not appear promising. However, there are various isostructural 3d-5d compounds, such as  \( Mn_{2}Ta \) ,  \( Co_{2}Ta \)  or  \( Fe_{2}Hf^{27.40} \)  and one might also consider alloys among these. Allowing for 3d or 4d atoms to substitute the 5d atom gives further possibilities \( ^{40} \) . As a next step, it should be worthwhile to investigate ternary or quaternary phase diagrams for magnetic 3d elements combined with 5d and other elements in uniaxial crystals. Numerous such phases which have not been properly characterized in terms of magnetic properties should exist and the type of computational methods used in this work should be of great value in identifying interesting materials.

I would like to thank Yaroslav Kvashnin for critically reading and providing useful comments on the manuscript. I'm also grateful to Ján Rusz and Olle Eriksson for discussions and for encouragement to pursue this work. Computational work has been performed with resources from the Swedish National Infrastructure for Computing (SNIC) at the National Supercomputer Centre (NSC) in Linköping.

## Appendix A: Matrix elements of the spin-orbit operator

If  \( |i\rangle \)  is a single particle eigenstate to an unperturbed Hamiltonian with no SOC, the total shift in the energy

 \( ^{1} \)  J. H. V. Vleck, Physical Review 52, 1178 (1937)

 \( ^{2} \)  O. Gutfleisch, M. a. Willard, E. Brück, C. H. Chen, S. G. Sankar, and J. P. Liu, Advanced materials 23, 821 (2011)

 \( ^{3} \)  D. Niarchos, G. Giannopoulos, M. Gjoka, C. Sarafidis, V. Psycharis, J. Rusz, A. Edström, O. Eriksson, P. Toson, J. Fidler, E. Anagnostopoulou, U. Sanyal, F. Ott, L.-M. Lacroix, G. Viau, C. Bran, M. Vazquez, L. Reichel, L. Schultz, and S. Fähler, JOM 67, 1318 (2015)

 \( ^{4} \)  J. M. D. Coey, IEEE Transactions on Magnetics 47, 4671 (2011)

 \( ^{5} \)  S. Hirosawa, Journal of Magnetics Society of Japan(2015)

 \( E_{i} \)  due to  \( H_{SOC} = \xi\hat{1} \cdot \hat{s} \)  in second order perturbation theory is

 \[ \Delta E_{i}=-\xi^{2}\sum_{j\neq i}\frac{\left|\left\langle n\right|\hat{1}\cdot\hat{s}\left|k\right\rangle\right|^{2}}{E_{j}-E_{i}}, \quad (A1) \] 

If the unperturbed Hamiltonian commutes with the spin operator,  \( |i\rangle \)  has a well defined spin  \( \sigma_{i} \)  but can be considered a superposition of different orbitals  \( \mu \)  so in the simplest case (ignoring other quantum numbers, e.g., k)

 \[ |i\rangle=\sum_{\mu}c_{i,\mu}\left|\mu,\sigma_{i}\right\rangle. \quad (A2) \] 

For d-electron magnetism, which is of focus here, it is suitable to consider  \( \mu \)  as  \( d_{z^{2}} \) ,  \( d_{xz} \) ,  \( d_{{yz}} \) ,  \( d_{xy} \)  or  \( d_{x^{2}-y^{2}} \) . The numerator in Eq. A1 then contains matrix elements  \( \langle d_{i},\sigma_{i}|1\cdot s|d_{j},\sigma_{j}\rangle \) , which determine the effect of the SOC. For convenience these matrix elements are explicitly listed in Tabel IV, with  \( \theta \)  and  \( \phi \)  denoting the polar and azimuthal angles of the spin quantization axis relative to the crystal lattice.

As mentioned in the main text, only coupling between states  \( |i\rangle \)  and  \( |j\rangle \)  with energies  \( E_{i} \)  and  \( E_{j} \)  such that  \( E_{i} < E_{F} < E_{j} \)  will contribute to the MAE and clearly then  \( \Delta E_{i} \leq 0 \)  according to Eq. A1. In terms of the matrix elements in Table IV this means that any coupling containing  \( \cos\theta \)  will lower the energy for  \( \theta = 0 \) , i.e. favoring a uniaxial magnetization (positive MAE), while  \( \sin\theta \)  lowers the energy for  \( \theta = \pi/2 \)  which favors in-plane magnetization (negative MAE). The situation taking into account multiple atomic types and hybridisation in Eq. 2 is somewhat more complicated and contains a product of matrix elements for possibly different atomic types. Nevertheless, the MAE is still determined by the matrix elements in Table IV.
 

Table IV: Matrix elements  \( \langle\sigma_{i},\mathrm{d}_{i}|\hat{\mathbf{1}}\cdot\hat{\mathbf{s}}|\sigma_{j},\mathrm{d}_{j}\rangle \)  of the spin-orbit coupling operator with respect to spin states in direction  \( \hat{\mathbf{n}}=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta) \)  and d-orbitals, in units of  \( \hbar^{2} \) . Reproduced from Ref. \( ^{41} \) .

<table><tr><td></td><td>\( |\uparrow,\mathrm{d}_{xy}\rangle \)</td><td>\( |\downarrow,\mathrm{d}_{yz}\rangle \)</td><td>$ |\uparrow,\mathrm{d}_{z2}\rangle</td><td>$ |\downarrow,\mathrm{d}_{xz}\rangle</td><td>$ \left|\uparrow,\mathrm{d}_{x2-y2}\right\rangle</td></tr><tr><td>\( \langle\uparrow,\mathrm{d}_{xy}\rangle \)</td><td>0</td><td>\( \frac{1}{2}\mathrm{i}\sin\theta\sin\phi \)</td><td>0</td><td>\( -\frac{1}{2}\mathrm{i}\sin\theta\cos\phi \)</td><td>\( \mathrm{i}\cos\theta \)</td></tr><tr><td>\( \langle\uparrow,\mathrm{d}_{yz}\rangle \)</td><td>\( -\frac{1}{2}\mathrm{i}\sin\theta\sin\phi \)</td><td>0</td><td>\( -\frac{\sqrt{3}}{2}\mathrm{i}\sin\theta\cos\phi \)</td><td>\( \frac{1}{2}\cos\theta \)</td><td>\( -\frac{1}{2} \)   \( \sin\theta\cos\phi \)</td></tr><tr><td>\( \langle\uparrow,\mathrm{d}_{z2}\rangle \)</td><td>0</td><td>\( \frac{\sqrt{3}}{2}\mathrm{i}\sin\theta\cos\phi \)</td><td>0</td><td>\( -\frac{\sqrt{3}}{2}\mathrm{i}\sin\theta\sin\phi \)</td><td>0</td></tr><tr><td>\( \langle\uparrow,\mathrm{d}_{xz}\rangle \)</td><td>\( \frac{1}{2}\mathrm{i}\sin\theta\cos\phi \)</td><td>\( -\frac{1}{2}\cos\theta \)</td><td>\( \frac{\sqrt{3}}{2}\mathrm{i}\sin\theta\sin\phi \)</td><td>0</td><td>\( -\frac{1}{2}\mathrm{i}\sin\theta\sin\phi \)</td></tr><tr><td>\( \langle\uparrow,\mathrm{d}_{x2-y2}\rangle \)</td><td>\( -\mathrm{i}\cos\theta \)</td><td>\( -\frac{1}{2}\sin\theta\cos\phi \)</td><td>0</td><td>\( \frac{1}{2}\mathrm{i}\sin\theta\sin\phi \)</td><td>0</td></tr><tr><td>\( \langle\downarrow,\mathrm{d}_{xy}\rangle \)</td><td>0</td><td>\( -\frac{1}{2}(\cos\phi \)</td><td>0</td><td>\( -\frac{1}{2}(\sin\phi \)</td><td>\( -\mathrm{i}\sin\theta \)</td></tr><tr><td>\( \langle\downarrow,\mathrm{d}_{yz}\rangle \)</td><td>\( -\mathrm{i}\cos\theta\sin\phi \)</td><td>0</td><td>\( -\frac{\sqrt{3}}{2}(\sin\phi \)</td><td>\( -\frac{1}{2}\sin\theta \)</td><td>\( -\mathrm{i}\cos\theta\cos\phi \)</td></tr><tr><td>\( \langle\downarrow,\mathrm{d}_{z2}\rangle \)</td><td>0</td><td>\( \frac{\sqrt{3}}{2}(\sin\phi \)</td><td>\( +\mathrm{i}\cos\theta\cos\phi \)</td><td>\( -\frac{1}{2}\sin\theta \)</td><td>\( +\mathrm{i}\cos\theta\cos\phi \)</td></tr><tr><td>\( \langle\downarrow,\mathrm{d}_{xz}\rangle \)</td><td>\( \frac{1}{2}(\sin\phi \)</td><td>\( +\mathrm{i}\cos\theta\cos\phi \)</td><td>0</td><td>\( -\frac{\sqrt{3}}{2}(\cos\phi \)</td><td>0</td></tr><tr><td>\( \langle\downarrow,\mathrm{d}_{x2-y2}\rangle \)</td><td>\( \mathrm{i}\sin\theta \)</td><td>\( -\frac{1}{2}(\sin\phi \)</td><td>\( -\mathrm{i}\cos\theta\sin\phi \)</td><td>0</td><td>\( -\mathrm{1}\cos\theta\sin\phi \)</td></tr></table>

mada, and K. Fukamichi, Physical Review B 66, 024413 (2002)

 \( ^{11} \)  T. Burkert, O. Eriksson, S. I. Simak, A. V. Ruban, B. Sanyal, L. Nordström, and J. M. Wills, Physical Review B 71, 134411 (2005)

 \( ^{12} \)  J. Lyubina, I. Opahle, K.-H. Müller, O. Gutfleisch, M. Richter, M. Wolf, and L. Schultz, Journal of Physics: Condensed Matter 17, 4157 (2005)

 \( ^{13} \)  H. Arnfelt and A. Westgren, Jernkontorets Annaler, 185(1935)

 \( ^{14} \)  P. Kumar, A. Kashyap, B. Balamurugan, J. E. Shield, D. J. Sellmyer, and R. Skomski, Journal of physics: Condensed matter 26, 064209 (2014)

 \( ^{15} \)  M. A. Koten, P. Manchanda, B. Balamurugan, R. Skomski, D. J. Sellmyer, and J. E. Shield, APL Materials 3, 076101 (2015)

 \( ^{16} \)  S. Ishida, S. Asano, and J. Ishida, “Electronic Structures of the C14 Laves Phase Compounds AFe \( _{2} \)  (A=Mo, Hf, Ta, W),” (1985)

 \( ^{17} \)  Ž. Blažina and S. Pavković, Journal of the Less Common Metals 155, 247 (1989)

 \( ^{18} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996)

 \( ^{19} \)  P. Blaha, G. Madsen, K. Schwarz, D. Kvasnicka, and J. Luitz, “WIEN2k, An Augmented Plane Wave + Local Orbitals Program for Calculating Crystal Properties,” (2001)

 \( ^{20} \)  D. D. Koelling and H. N. Harmon, Journal of Physics C: Solid State Physics 10 (1977)

 \( ^{21} \)  P. E. Blöchl, O. Jepsen, and O. K. Andersen, Phys. Rev. B 49, 16223 (1994)

 \( ^{22} \)  R. Wienke, G. Schütz, and H. Ebert, Journal of Applied Physics 69, 6147 (1991)

 \( ^{23} \)  A. Edström, J. Chico, A. Jakobsson, A. Bergman, and J. Rusz, Physical Review B 90, 014402 (2014)

 \( ^{24} \)  J.-U. Thiele, L. Folks, M. F. Toney, and D. K. Weller, Journal of Applied Physics 84, 5686 (1998)

 \( ^{25} \)  P. Ravindran, A. Kjekshus, H. Fjellvaag, P. James, L. Nordström, B. Johansson, and O. Eriksson, Phys. Rev. B 63, 144409 (2001)

 \( ^{26} \)  E. I. Kondorskii and E. Straube, Journal of Experimental and Theoretical Physics 63, 188 (1973)

 \( ^{27} \)  P. Bruno, Physical Review B 39, 865 (1989)

 \( ^{28} \)  C. Andersson, B. Sanyal, O. Eriksson, L. Nordström, O. Karis, D. Arvanitis, T. Konishi, E. Holub-Krappe, and J. H. Dunn, Physical Review Letters 99, 177207 (2007)

 \( ^{29} \)  G. H. O. Daalderop, P. J. Kelly, and M. F. H. Schuurmans, Physical Review B 41, 11919 (1990)

 \( ^{30} \)  G. H. Lander, M. S. S. Brooks, B. Lebech, P. J. Brown, O. Vogt, and K. Mattenberger, Applied Physics Letters 57, 989 (1990)

 \( ^{31} \)  J. Faulkner, Progress in Materials Science 27, 1 (1982)

 \( ^{32} \)  R. H. Victora and L. M. Falicov, Physical Review B 30, 259 (1984)

 \( ^{33} \)  E. K. Delczeg-Czirjak, A. Edström, M. Werwinski, J. Rusz, N. V. Skorodumova, L. Vitos, and O. Eriksson, Physical Review B 89, 144403 (2014)

 \( ^{34} \)  A. Edström, M. Werwinski, D. Iuşan, J. Rusz, O. Eriksson, K. P. Skokov, I. A. Radulov, S. Ener, M. D. Kuz'min, J. Hong, M. Fries, D. Y. Karpenkov, O. Gutfleisch, P. Toson, and J. Fidler, Phys. Rev. B 92, 174413 (2015)

 \( ^{35} \)  I. Turek, J. Kudrnovský, and K. Carva, Physical Review B 86, 174430 (2012)

 \( ^{36} \)  C. Neise, S. Schönecker, M. Richter, K. Koepernik, and H. Eschrig, Physica Status Solidi (B) 248, 2398 (2011)

 \( ^{37} \)  S. Steiner, S. Khmelevskyi, M. Marsmann, and G. Kresse, Physical Review B 93, 224425 (2016)

 \( ^{38} \)  G. Andersson, T. Burkert, P. Warnicke, M. Björck, B. Sanyal, C. Chacon, C. Zlotea, L. Nordström, P. Nordblad, and O. Eriksson, Physical Review Letters 96, 037205 (2006)

 \( ^{39} \)  L. Reichel, G. Giannopoulos, S. Kauffmann-Weiss, M. Hoffmann, D. Pohl, A. Edström, S. Oswald, D. Niarchos, J. Rusz, L. Schultz, and S. Fähler, Journal of Applied Physics 116, 213901 (2014)

 \( ^{40} \)  Y. Nishihara, Journal of Magnetism and Magnetic Materials 70, 75 (1987)

 \( ^{41} \)  E. Abate and M. Asdente, Physical Review 140, A1303 (1965)
 
