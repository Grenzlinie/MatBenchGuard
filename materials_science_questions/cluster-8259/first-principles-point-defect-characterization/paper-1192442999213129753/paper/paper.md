
# A CN complex as an alternative to the T center in Si

J. K. Nangoi, \( ^{1,*} \)  M. E. Turiansky, \( ^{1,2} \)  and C. G. Van de Walle \( ^{1} \) 

 \( ^{1} \) Materials Department, University of California, Santa Barbara, California 93106, USA  
 \( ^{2} \) US Naval Research Laboratory, Washington, DC 20375, USA

We present a first-principles study of a carbon-nitrogen (CN) impurity complex in silicon as an isoelectronic alternative to the T center  \( [(CCH)_{Si}] \) . The latter has been pursued for applications in quantum information science, yet its sensitivity to the presence of hydrogen is still problematic. Our proposed complex has no hydrogen, thereby eliminating this issue. First, we show that the CN complex is stable against decomposition into substitutional and interstitial defects. Next, we show that due to being isoelectronic to the T center, the CN complex has a similar electronic structure, and therefore could be used in similar applications. We assess several low-energy configurations of the CN complex, finding  \( (CN)_{Si} \)  to be stable and have the largest Debye-Waller factor. We predict a zero-phonon line (ZPL) of 828 meV (in the telecom S-band) and a radiative lifetime of 4.2  \( \mu \) s, comparable to the T center. Due to the presence of a bound exciton, choice of the exchange-correlation functional and also supercell-size scaling of the ZPL and transition dipole moment require special scrutiny; we rigorously justify our extrapolation schemes that allow computing values in the dilute limit.

Point defects in semiconductors or insulators are being studied for quantum information science applications, including as spin qubits for quantum computing  \( [1-3] \)  and single-photon emitters for quantum networks  \( [2-4] \) . For the former, the spin coherence time is the main metric, as it determines how long quantum information remains coherent. For networking, single photons carry the quantum information  \( [5, 6] \) . A high Debye-Waller (DW) factor is desired so that most photons are emitted into the zero-phonon line (ZPL), for which the photons are in a well-defined quantum state  \( [6] \) .

The nitrogen-vacancy (NV) center in diamond has been studied extensively for these applications. It has a triplet ground state with spin coherence time exceeding milliseconds  \( [7] \) , but a DW factor of only  \( \sim3\% \)   \( [8] \) . Alternatives to the NV center have been studied, such as the silicon-vacancy center in diamond  \( [9] \) , carbon-vacancy and silicon-vacancy in cubic boron nitride  \( [10] \) , or color centers in silicon  \( [3, 11, 12] \) . Silicon is an attractive host material because it offers the prospect of integration with Si-based electronics  \( [11] \) ; it is also far easier to grow and process than diamond  \( [7] \) . The T center in Si, a complex in which two carbons and one hydrogen substitute on a Si site [denoted by  \( (CCH)_{Si} \) , Fig. 1(a)], has been intensively pursued experimentally due to its high spin coherence times, large DW factor, and emission in the O-band of telecom wavelengths  \( [11, 13–17] \) .

Despite the promise, formation and stability of the T center remain a concern; it was found to be “prone to (de)hydrogenation and so requires very precise annealing conditions (temperature and atmosphere) to be efficiently formed” [12]. Identifying alternatives to the T center, preferably without H, would thus be beneficial.

In this letter, we propose a carbon-nitrogen complex as an analog of the T center. Replacing the hydrogen and

![](2511.00754v1-images/0_0.jpg)

FIG. 1. Structure of (a) T center,  \( (CCH)_{Si} \) , (b)  \( (CN)_{Si} \) , and (c)  \( C_{Si}(NSi)_{Si} \) .

one carbon atom in  \( (CCH)_{Si} \)  with a nitrogen atom keeps the center isoelectronic with the T center, since N contains the same number of electrons and protons as C+H. The absence of H makes this complex more stable with regard to (de)hydrogenation. Like H, N has non-zero nuclear spin and can thus be exploited to store quantum information. We demonstrate the stability of this center by calculating the formation and decomposition energies, and thoroughly assess its electronic structure and optical properties, including the Huang-Rhys/DW factors, energy of the ZPL transition, and radiative lifetime. Our results show that the CN center is a promising candidate for applications in quantum information science.

Our first-principles studies are based on density-functional theory (DFT) with projector-augmented wave (PAW) potentials  \( [18, 19] \)  as implemented in the Vienna Ab initio Simulation Package (VASP)  \( [20, 21] \) , with a plane-wave cutoff of 400 eV. We use the hybrid functional of Heyd, Scuseria, and Ernzerhof (HSE)  \( [22, 23] \)  with the default mixing parameter of 25%; for select results (as described below) we also employ the PBE0 (Perdew, Burke, and Ernzerhof) hybrid functional  \( [24–26] \)  with a mixing parameter of 13.6%. For the primitive cell with a Brillouin-zone sampling mesh of  \( 11 \times 11 \times 11 \) , we find an HSE lattice constant of 5.433 Å and a band gap of 1.15 eV, both in agreement with experiment (5.431 Å  \( [27] \)  and 1.17 eV at 0 K  \( [28] \) ). We model the defect in a supercell geometry, using the  \( \Gamma \)  point to sample the Brillouin
 

zone. Most of our results are presented for a 512-atom supercell  \( (4 \times 4 \times 4 \)  multiple of the conventional cubic cell), allowing us to make direct comparison with previous work [12]. We also use up to 1000-atom supercells  \( (5 \times 5 \times 5) \)  to better describe the bound excitons that are present in the excited states of the centers studied here. Structural optimizations are performed until the forces are less than 0.01 eV/ \( \AA \) .

Previous first-principles calculations identified two possible configurations of the CN complex: (1) a C-N split interstitial  \( (\mathrm{CN})_{\mathrm{Si}} \)  [29] [Fig. 1(b)], which can be thought of as replacing C-H with N in the T center  \( (\mathrm{CCH})_{\mathrm{Si}} \) , and (2) a complex of a substitutional C atom and a N-Si split interstitial,  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  [30, 31] [Fig. 1(c)].

Figure 2 shows our calculated formation energies  \( E^{f} \)  as a function of the Fermi level for both CN structures, and also for the T center.  \( E^{f} \)  is given by [32]:

 \[ E^{f}[X^{q}]=E_{\mathrm{t o t}}[X^{q}]-E_{\mathrm{t o t}}[\mathrm{S i}]-\sum_{i}n_{i}\mu_{i}+q E_{F}+E_{\mathrm{c o r r}}, \] 

where  \( E_{tot}[X^{q}] \)  is the total energy of the supercell containing the defect X in charge state q,  \( E_{tot}[Si] \)  is the total energy of the equivalent supercell containing perfect host material,  \( n_{i} \)  is the number of atoms of type i added to  \( (n_{i} > 0) \)  or removed from  \( (n_{i} < 0) \)  the supercell,  \( \mu_{i} \)  is the chemical potential of atom type i,  \( E_{F} \)  is the Fermi level, and  \( E_{corr} \)  is a finite-size correction for charged defects [33]. For the  \( \mu_{i} \)  we use the total energies per atom of bulk Si, diamond,  \( H_{2} \) , and  \( N_{2} \) .

![](2511.00754v1-images/1_0.jpg)

FIG. 2. Defect formation energies as a function of Fermi level for the T center (orange),  \( (\mathrm{CN})_{\mathrm{Si}} \)  (green), and  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  (blue). Blue and green shades indicate valence and conduction bands. The valence-band maximum (VBM) is set to 0, and the conduction-band minimum (CBM) is at 1.15 eV, our calculated Si band gap.

Our results for the T center agree with Ref. 12. The +1 charge state of the T center and  \( (\mathrm{CN})_{\mathrm{Si}} \)  are not stable in the gap, as seen in Fig. 2. We find that the -1 charge state of the T center,  \( (\mathrm{CN})_{\mathrm{Si}} \) , and  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \) , and also the +1 charge state of  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  all have net zero spin (singlet) (see Fig. S1 in the Supplemental Material (SM) [34]), precluding their use as spin qubits. We also note that the excited state of, e.g., the -1 charge state involves exciting an electron to the conduction-band minimum (CBM), leaving a neutral defect center behind. The electron will thus feel no Coulomb attraction and hence cannot act as a single-photon emitter. Similar arguments apply to the +1 charge state. These charge states are therefore less useful for quantum information applications. We thus focus on the neutral charge state, which is stable over the majority of the band gap for  \( (\mathrm{CN})_{\mathrm{Si}} \) , with the negative charge state occurring only for Fermi levels within 0.17 eV of the CBM.  \( [C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \)  is stable for Fermi levels between 0.41 and 0.94 eV.

The stability of alternate atomic configurations in the case of the CN center inspired us to investigate whether the CCH center could also be stable in other structures; we found these to be 0.6–2.5 eV higher in energy than the accepted  \( (\mathrm{CCH})_{\mathrm{Si}} \)  structure of the T center (see Sec. S2 of the SM [34]).

We assess the stability of the CN defects [both  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  and  \( (\mathrm{CN})_{\mathrm{Si}} \) ] with respect to decomposition into constituent defects (substitutions and interstitials) by calculating the decomposition energy  \( \Delta E^{f} \equiv \sum E^{f}[\mathrm{products}] - E^{f}[\mathrm{CN}\mathrm{defect}] \) ; a positive energy indicates the reaction is endothermic. For C and N interstitials, the split-interstitial configurations are found to be lowest in energy, consistent with Refs. 29, 35–38 (see Sec. S2 in the SM [34] for atomic structures and formation energies).

Table I shows our results for decomposition energies, taking into account that the overall charge state should remain neutral. All decomposition energies are positive, meaning both configurations are stable against all considered decompositions. The  \( \Delta E^{f} \)  for  \( (\mathrm{CN})_{\mathrm{Si}}^{0} \)  are  \( \sim0.2 \)  eV lower than those for  \( [\mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \) , because the formation energy of  \( (\mathrm{CN})_{\mathrm{Si}}^{0} \)  is slightly higher than that of  \( [\mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \)  (Fig. 2). Decomposition into  \( C_{Si}^{0} \)  and  \( (\mathrm{NSi})_{\mathrm{Si}}^{0} \)  has the smallest energy, with a value that is comparable to the lowest decomposition energy (0.80 eV) for  \( (\mathrm{CCH})_{\mathrm{Si}} \)  calculated in Ref. 12. Furthermore, as mentioned above, the absence of hydrogen in the CN defect is advantageous.

We use the climbing image nudged elastic band method [39] to calculate the migration barrier of  \( (\mathrm{NSi})_{\mathrm{Si}}^{0} \)  (the most mobile constituent), resulting in 0.68 eV (see Sec. S3 in the SM [34]). We can thus estimate the barrier height of the lowest-energy decomposition reaction to be 1.50 eV for  \( [\mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \)  and 1.29 eV for  \( (\mathrm{CN})_{\mathrm{Si}}^{0} \) .

TABLE I. Decomposition energies \(\Delta E^{f}\) for \((\mathrm{CN})_{\mathrm{Si}}^{0}\) and \([C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0}\).

<table><tr><td></td><td colspan="2">\( \Delta E^{f} \)  (eV)</td></tr><tr><td></td><td>\( (\mathrm{CN})_{\mathrm{Si}}^{0} \)</td><td>\( [C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \)</td></tr><tr><td>\( \rightarrow C_{\mathrm{Si}}^{0} + (\mathrm{NSi})_{\mathrm{Si}}^{0} \)</td><td>0.61</td><td>0.82</td></tr><tr><td>\( \rightarrow C_{\mathrm{Si}}^{+1} + (\mathrm{NSi})_{+1}^{0} \)</td><td>1.33</td><td>1.54</td></tr><tr><td>\( \rightarrow C_{\mathrm{Si}}^{+1} + (\mathrm{NSi})_{\mathrm{Si}}^{-1} \)</td><td>1.69</td><td>1.90</td></tr><tr><td>\( \rightarrow (\mathrm{CSi})_{\mathrm{Si}}^{0} + N_{\mathrm{Si}}^{0} \)</td><td>3.12</td><td>3.33</td></tr><tr><td>\( \rightarrow (\mathrm{CSi})_{\mathrm{Si}}^{-1} + N_{\mathrm{Si}}^{+1} \)</td><td>3.65</td><td>3.86</td></tr><tr><td>\( \rightarrow (\mathrm{CSi})_{+1}^{0} + N_{\mathrm{Si}}^{-1} \)</td><td>3.70</td><td>3.91</td></tr></table>
 

We now study the electronic structure by analyzing the spin-polarized Kohn-Sham states and wavefunctions in both the ground and excited electronic states. Figure 3 compares  \( (\mathrm{CN})_{Si}^{0} \)  and  \( [\mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \)  with  \( (\mathrm{CCH})_{Si}^{0} \)  (the T center, for which our results agree with Ref. 12). In the ground state of the T center, the  \( a^{\prime\prime} \)  antibonding state associated with the  \( C_{1h} \)  symmetry undergoes exchange splitting: the occupied spin-up state is below the VBM and the unoccupied spin-down state lies just below the CBM. The ground states of the CN centers are qualitatively similar, with exchange splitting in the b antibonding state for  \( (\mathrm{CN})_{\mathrm{Si}} \)  ( \( C_{2v} \)  symmetry) and in the a state for  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  ( \( C_{1} \)  symmetry), although the occupied spin-up a state is now above the VBM. The unoccupied states for all 3 defects [Figs. 4(a)–(c)] and the occupied state for  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  [Figs. 4(d)] are localized at the defect site.

![](2511.00754v1-images/2_0.jpg)

![](2511.00754v1-images/2_1.jpg)

![](2511.00754v1-images/2_2.jpg)

![](2511.00754v1-images/2_3.jpg)

![](2511.00754v1-images/2_4.jpg)

![](2511.00754v1-images/2_5.jpg)

FIG. 3. Ground- (top row) and excited-state (bottom row) Kohn-Sham states for the neutral charge state. “e-h” (“h-e”) labels the localized-electron (hole) case. Blue and green shades indicate valence and conduction bands. Red levels are the states associated with the defect, and blue levels are valence- and conduction-band states.

To model excited states, we use the constrained occupation  \( \Delta \) SCF approach [40], where we excite a spin-down electron from the VBM to the unoccupied defect state, constrain the electron occupation, and reoptimize the structure. The resulting structure has an in-gap state with both spin channels occupied [Figs. 3(d)–(f)] that is localized at the defect site [Figs. 4(e)–(g)] (maintaining the symmetry of the ground state), and leaves a hole with hydrogenic nature bound to the localized electron. The localized electron and the hole form a bound exciton, where, within hydrogenic effective mass theory, the hole approximately has an effective Bohr radius of  \( \sim13 \)  Å as shown in Sec. S4 of the SM [34].

For  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \) , it is also possible to excite a spin-up electron from the in-gap defect state into the CBM, resulting in an exciton with a localized hole and a hydrogenic electron [Figs. 3(g) and 4(h)]. The corresponding effective Bohr radius for the electron is approximately  \( \sim6 \)  Å (see Sec. S4 of the SM [34]). In contrast, for both

![](2511.00754v1-images/2_6.jpg)

FIG. 4. Isosurfaces (yellow) of real-space Kohn-Sham probability densities for the neutral charge state of the ground-state in-gap empty spin-down state  \( [(a)-(c)] \)  and filled spin-up state  \( [(d)] \) , and of the excited-state in-gap filled spin-down state  \( [(e)-(g)] \)  for localized-electron case and empty spin-up state  \( [(h)] \)  for localized-hole case. Blue circles are Si; brown, C; light blue, N; and pink, H.

the T center and  \( (\mathrm{CN})_{\mathrm{Si}} \) , exciting the electron from the  \( a^{\prime\prime} \)  or b state below the VBM into the CBM results in an excited state where the hole is at the VBM instead of being localized at an in-gap defect state.

We note that the localized-hole excited state of  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  has  \( C_{1h} \)  symmetry, unlike the  \( C_{1} \)  symmetry
 

for both the ground state and the localized-electron excited state, as apparent in the charge density [Fig. 4(h)]. This is because, as seen in the figure, the C, N, and Si bonded to both C and N now form a mirror plane, unlike in the ground state [Fig. 4(c) and (d)] and the localized-electron excited state [Fig. 4(g)].

Table II shows our calculated Huang-Rhys factors  \(  S = E_{\mathrm{r}} / (\hbar \Omega)  \)  and DW factors  \(  \exp(-S)  \) ;  \( E_{r} \)  and  \( \Omega \)  are the relaxation energy and phonon frequency in the electronic ground state within the one-dimensional approximation [41–43]. Details are in Sec. S5 of the SM [34]. Our calculated DW factor for the T center is  \( \sim 9\% \) ; Ref. 44 reports a calculated value of 16.5%, while the value obtained from photoluminescence (PL) data is 23% [11]. The discrepancy with Ref. 44 could be due to differences in  \( E_{r} \)  or  \( \Omega \) . The discrepancy with experiment could be because our DW factors are based on a one-dimensional model, which underestimates the more realistic, multidimensional model [45], so we focus here on trends. The DW factors for  \(  \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}  \)  are below 1%, limiting their usefulness for single-photon emitters. In the following we focus on  \(  (\mathrm{CN})_{\mathrm{Si}}  \) .

TABLE II. Relaxation energies \((E_{r})\), ground-state phonon frequencies \((\Omega)\), and Huang-Rhys \((S)\) and Debye-Waller \((DW)\) factors.

<table><tr><td></td><td>\( E_{r} \)  (eV)</td><td>\( \hbar\Omega \)  (meV)</td><td>S</td><td>DW (%)</td></tr><tr><td>\( (CCH)_{Si} \)</td><td>0.079</td><td>33</td><td>2.4</td><td>9.2</td></tr><tr><td>\( (CN)_{Si} \)</td><td>0.107</td><td>35</td><td>3.0</td><td>5.0</td></tr><tr><td>\( C_{Si}(NSi)_{Si} \)  e-h</td><td>0.157</td><td>28</td><td>5.6</td><td>0.4</td></tr><tr><td>\( C_{Si}(NSi)_{Si} \)  h-e</td><td>0.297</td><td>28</td><td>10.5</td><td>0.003</td></tr></table>

The energy of the ZPL transition  \( E_{ZPL} \)  is calculated as the total-energy difference between the excited state and the ground state. Using a 512-atom supercell, we find  \( E_{ZPL} = 981 \)  meV for the T center, in agreement with Ref. 12. However, as seen in Fig. 5 the calculated  \( E_{ZPL} \)  depends on the supercell size because our supercells are not large enough to completely fit the hydrogenic wavefunctions (Fig. S5 in the SM [34]) [46]. The dependence of  \( E_{ZPL} \)  on supercell size is well described by a linear fit to the inverse of the supercell volume (Fig. 5). An extrapolation to the dilute limit based on our HSE values produces a value of 1064 meV, overestimating the experimentally measured ZPL of 935 meV [11].

An investigation of the cause of this deviation indicated that the ZPL values are sensitive to the DFT functional. We found that PBE0 gives a better extrapolated ZPL for the T center, and therefore choose it to improve predictions for the CN defects.

A PBE0 mixing parameter of 13.6% yields a lattice constant of 5.446 Å and a band gap of 1.23 eV, which reproduces the experimental T=0 gap of 1.17 eV [28] plus the zero-point renormalization of 60 meV [47]. We found that PBE0 geometries are very close to those obtained with HSE, and hence we use single-shot PBE0 (i.e., only performing electronic structure optimization) using the relaxed HSE geometries (scaled according to the slight

![](2511.00754v1-images/3_0.jpg)

FIG. 5. Zero-phonon line energies for the T and CN centers, calculated using either single-shot PBE0 or HSE and plotted as a function of inverse supercell size (N is the number of atoms in the defect-free supercell). The lines are linear fits. The horizontal orange line represents the measured ZPL of the T center, 935 meV from Ref. 11.

difference in lattice constant). The accuracy of this approach is demonstrated in Table S1 of the SM [34].

As shown in Fig. 5, extrapolation of the PBE0 values to the dilute limit yields 918 meV for the T center  \( [(CCH)_{Si}] \) , significantly closer to experiment (935 meV, Ref. 11) than the HSE value of 1064 meV.

For  \( (\mathrm{CN})_{\mathrm{Si}} \) , we find an extrapolated PBE0 value of 828 meV (in the S-band of the telecom wavelength region [48]); see Sec. S7 for the values for  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \) . A number of luminescence lines with comparable energies have been observed in Si, at 829.8 meV [49], 844 meV [50], and 856 meV; the latter was suggested to be associated with interstitial C [49]. Experimental ZPLs ranging from 746 to 772 meV have been attributed to complexes containing C and N [49, 51–55]; however, no reliable microscopic identification of the structure of these complexes is available, and the cited references indicate that some may involve additional impurities such as oxygen.

Finally, we calculate the radiative lifetime  \( \tau \)  of the ZPL transition using the Weisskopf-Wigner formula [6, 56, 57],

 \[ \frac{1}{\tau}=\left(\frac{\mathcal{E}_{\mathrm{e f f}}}{\mathcal{E}_{0}}\right)^{2}\frac{n_{r}}{3\pi\epsilon_{0}c^{3}\hbar^{4}}(E_{\mathrm{Z P L}})^{3}|\mu|^{2}, \quad (1) \] 

where  \( n_{r} \)  is the refractive index of the host material (3.38 for Si [27]), c is the speed of light, and  \( \mu \)  is the transition dipole moment (TDM). The prefactor  \( (\mathcal{E}_{\mathrm{eff}}/\mathcal{E}_{0})^{2} \)  accounts for local-field effects [6, 56], which tend to increase the rate. Here we take  \( E_{eff} \approx E_{0} \) , which is a common approximation [6, 58].

Calculating  \( \mu \)  is challenging because it requires accurately describing the hydrogenic wavefunction corre-
 

sponding to the bound exciton. We therefore do not attempt to calculate  \( \mu \)  in the excited state, but we approximate  \( \mu \)  by scaling the TDM calculated in the ground state,  \( \mu^{0} \) , to account for the hydrogenic nature:

 \[ |\mu|^{2}\approx t|\mu^{0}|^{2}. \quad (2) \] 

Here  \( t = \tilde{V}/[\pi(a_{0}^{*})^{3}] \) , where  \( \tilde{V} \)  is the supercell volume and  \( a_{0}^{*} \)  is the effective Bohr radius of the hydrogenic wavefunction. For details, see Sec. S8 of the SM [34] [59].

Using the approximate  \( \mu \)  and the extrapolated ZPLs, we find very similar radiative lifetimes of 4.70  \( \mu \) s (which agrees well with 4.9  \( \mu \) s deduced from experiments in Ref. 60) and 4.18  \( \mu \) s for the T center and  \( (\mathrm{CN})_{\mathrm{Si}} \) . (See Table S2 for the values for  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \) .)

In conclusion, we propose the CN complex as a hydrogen-free alternative to the T center for similar quantum applications. We have shown that both  \( (\mathrm{CN})_{\mathrm{Si}} \)  and  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  are stable against decomposition to C and N substitutional/interstitial defects, and have electronic structures similar to the T center: a neutral charge state that is stable in the band gap, similar Kohn-Sham eigenvalues and eigenstates in both the ground and excited state, and an excited state consisting of a bound exciton with a localized electron and a hydrogenic hole. Additionally,  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  has an excited state consisting of a bound exciton with a localized hole and a hydrogenic electron. We carefully handle the supercell-size scaling for the ZPL and propose an extrapolation procedure for the radiative lifetimes, allowing us to obtain results in

[1] C. E. Bradley, J. Randall, M. H. Abobeih, R. C. Berrevoets, M. J. Degen, M. A. Bakker, M. Markham, D. J. Twitchen, and T. H. Taminiau, Phys. Rev. X 9, 31045 (2019).

[2] X. Yan, S. Gitt, B. Lin, D. Witt, M. Abdolahi, A. Afifi, A. Azem, A. Darcie, J. Wu, K. Awan, M. Mitchell, A. Pfenning, L. Chrostowski, and J. F. Young, APL Photonics 6, 070901 (2021).

[3] S. Simmons, PRX Quantum 5, 010102 (2024).

[4] M. Ruf, N. H. Wan, H. Choi, D. Englund, and R. Hanson, J. Appl. Phys. 130, 070901 (2021).

[5] T. E. Northup and R. Blatt, Nat. Photonics 8, 356 (2014).

[6] M. E. Turiansky, K. Parto, G. Moody, and C. G. Van de Walle, APL Photonics 9, 066117 (2024).

[7] J. R. Weber, W. F. Koehl, J. B. Varley, A. Janotti, B. B. Buckley, C. G. Van de Walle, and D. D. Awschalom, Proc. Natl. Acad. Sci. 107, 8513 (2010).

[8] G. Davies, Reports Prog. Phys. 44, 787 (1981).

[9] C. Bradac, W. Gao, J. Forneris, M. E. Trusheim, and I. Aharonovich, Nat. Commun. 10, 5625 (2019).

[10] M. E. Turiansky and C. G. Van de Walle, Phys. Rev. B 108, L041102 (2023).

[11] L. Bergeron, C. Chartrand, A. T. K. Kurkjian, K. J. Morse, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, and S. Simmons, PRX Quantum 1, 020301 (2020).

the dilute limit. We find the lifetime for  \( (\mathrm{CN})_{\mathrm{Si}} \)  to be similar to the  \( (\mathrm{CCH})_{\mathrm{Si}} \)  center. These results, combined with the fact that the predicted ZPL of  \( (\mathrm{CN})_{\mathrm{Si}} \)  is in the telecom S-band, render the  \( (\mathrm{CN})_{\mathrm{Si}} \)  center a promising hydrogen-free alternative to the T center.

## ACKNOWLEDGMENTS

We gratefully acknowledge discussions with D. Waldhör, W. Lee, M. W. Swift, C. A. Broderick, and Y. Chen. This work was supported by the U.S. Department of Energy (DOE), Office of Science (SC), National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage (C²QA) under contract number DE-SC0012704, and used computing resources provided by the National Energy Research Scientific Computing Center (NERSC), a User Facility supported by the DOE SC under Contract No. DE-AC02-05CH11231 using NERSC award BES-ERCAP0021021 and BES-ERCAP0028497. Additional resources were provided by the Texas Advanced Computing Center (TACC) at The University of Texas at Austin and the San Diego Supercomputer Center (SDSC) Expanse at the University of California, San Diego through allocation DMR070069 from the Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support (ACCESS) program [61], which is supported by National Science Foundation grants #2138259, #2138286, #2138307, #2137603, and #2138296.

[12] D. Dhaliah, Y. Xiong, A. Sipahigil, S. M. Griffin, and G. Hautier, Phys. Rev. Mater. 6, L053201 (2022).

[13] E. R. MacQuarrie, C. Chartrand, D. B. Higginbottom, K. J. Morse, V. A. Karasyuk, S. Roorda, and S. Simmons, New J. Phys. 23, 103008 (2021).

[14] D. B. Higginbottom, A. T. Kurkjian, C. Chartrand, M. Kazemi, N. A. Brunelle, E. R. MacQuarrie, J. R. Klein, N. R. Lee-Hone, J. Stacho, M. Ruether, C. Bowness, L. Bergeron, A. DeAbreu, S. R. Harrigan, J. Kanaganayagam, D. W. Marsden, T. S. Richards, L. A. Stott, S. Roorda, K. J. Morse, M. L. Thewalt, and S. Simmons, Nature 607, 266 (2022).

[15] D. B. Higginbottom, F. K. Asadi, C. Chartrand, J. W. Ji, L. Bergeron, M. L. Thewalt, C. Simon, and S. Simmons, PRX Quantum 4, 020308 (2023).

[16] A. DeAbreu, C. Bowness, A. Alizadeh, C. Chartrand, N. A. Brunelle, E. R. MacQuarrie, N. R. Lee-Hone, M. Ruether, M. Kazemi, A. T. K. Kurkjian, S. Roorda, N. V. Abrosimov, H.-J. Pohl, M. L. W. Thewalt, D. B. Higginbottom, and S. Simmons, Opt. Express 31, 15045 (2023).

[17] F. Islam, C.-M. Lee, S. Harper, M. H. Rahaman, Y. Zhao, N. K. Vij, and E. Waks, Nano Lett. 24, 319 (2024).

[18] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

[19] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

[20] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).
 

[21] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[22] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 118, 8207 (2003).

[23] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 124, 219906 (2006).

[24] J. P. Perdew, M. Ernzerhof, and K. Burke, J. Chem. Phys. 105, 9982 (1996).

[25] M. Ernzerhof and G. E. Scuseria, J. Chem. Phys. 110, 5029 (1999).

[26] Carlo and V. Barone, J. Chem. Phys. 110, 6158 (1999).

[27] M. S. Shur, Handbook Series on Semiconductor Parameters, Vol. 1 (World Scientific, 1996).

[28] W. Bludau, A. Onton, and W. Heinke, J. Appl. Phys. 45, 1846 (1974).

[29] A. Platonenko, F. S. Gentile, J. Maul, F. Pascale, E. A. Kotomin, and R. Dovesi, Mater. Today Commun. 21, 100616 (2019).

[30] N. Kuganathan, S.-R. G. Christopoulos, K. Papadopoulou, E. N. Sgourou, A. Chroneos, and C. A. Londos, Mod. Phys. Lett. B 37, 2350154 (2023).

[31] E. N. Sgourou, N. Sarlis, A. Chroneos, and C. A. Londos, Appl. Sci. 14, 1631 (2024).

[32] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti, and C. G. Van de Walle, Rev. Mod. Phys. 86, 253 (2014).

[33] C. Freysoldt, J. Neugebauer, and C. G. Van de Walle, Phys. Rev. Lett. 102, 016402 (2009).

[34] See Supplemental Material at [URL will be inserted by publisher] for Kohn-Sham states of non-neutral charge states of T and CN centers, other defects considered, migration barrier calculations, bound exciton supercell-size dependence, Huang-Rhys factor calculations, full vs. single-shot PBE0, all zero-phonon lines, radiative lifetime calculations, and relation of radiative lifetime to the radiative capture formalism, which includes Refs. [62–71].

[35] J. Tersoff, Phys. Rev. Lett. 64, 1757 (1990).

[36] F. S. Gentile, A. Platonenko, K. E. El-Kelany, M. Rérat, P. D'Arco, and R. Dovesi, J. Comput. Chem. 41, 1638 (2020).

[37] A. Platonenko, F. S. Gentile, F. Pascale, P. D'Arco, and R. Dovesi, J. Comput. Chem. 42, 806 (2021).

[38] C. Simha, G. Herrero-Saboya, L. Giacomazzi, L. Martins-Samos, A. Hemeryck, and N. Richard, Nanomaterials 13, 2123. (2023).

[39] G. Henkelman, B. P. Uberuaga, and H. Jonsson, J. Chem. Phys. 113, 9901 (2000).

[40] R. O. Jones and O. Gunnarsson, Rev. Mod. Phys. 61, 689 (1989).

[41] K. Huang and A. Rhys, Proc. R. Soc. Lond. A 204, 406 (1950).

[42] A. Alkauskas, J. L. Lyons, D. Steiauf, and C. G. Van de Walle, Phys. Rev. Lett. 109, 267401 (2012).

[43] A. Alkauskas, B. B. Buckley, D. D. Awschalom, and C. G. Van de Walle, New J. Phys. 16, 073026 (2014).

[44] Y. Xiong, J. Zheng, S. McBride, X. Zhang, S. M. Griffin, and G. Hautier, J. Am. Chem. Soc. 146, 30046 (2024).

[45] M. E. Turiansky and J. L. Lyons, Approximate excited-state potential energy surfaces for defects in solids (2025), arXiv:2506.12174 [cond-mat.mtrl-sci].

[46] Supercell-size dependence for the T center was also ob-

served in Ref. 72, which calculated exciton binding energies and dipole moment changes.

[47] D. Karaiskaj, M. L. W. Thewalt, T. Ruf, M. Cardona, and M. Konuma, Solid State Commun. 123, 87 (2002).

[48] R. Paschotta, Optical fiber communications, RP Photonics Encyclopedia (2005).

[49] G. Davies, Phys. Rep. 176, 83 (1989).

[50] H. Conzelmann, K. Graff, and E. R. Weber, Applied Physics A Solids and Surfaces 30, 169 (1983).

[51] A. Dörnen, R. Sauer, and G. Pensl, MRS Online Proc. Libr. 59, 545 (1985).

[52] A. Dörnen, G. Pensl, and R. Sauer, Phys. Rev. B 33, 1495(R) (1986).

[53] A. Dörnen, G. Pensl, and R. Sauer, Solid State Commun. 57, 861 (1986).

[54] A. Dörnen, G. Pensl, and R. Sauer, Phys. Rev. B 35, 9318 (1987).

[55] A. Dörnen, R. Sauer, and G. Pensl, J. Electron. Mater. 17, 121 (1988).

[56] A. M. Stoneham, Theory of Defects in Solids: Electronic Structure of Defects in Insulators and Semiconductors, Monographs on the Physics and Chemistry of Materials (Clarendon, Oxford, 1975).

[57] V. Weisskopf and E. Wigner, Zeitschrift für Phys. 63, 54 (1930).

[58] L. Razinkovas, M. Maciaszek, F. Reinhard, M. W. Doherty, and A. Alkauskas, Phys. Rev. B 104, 235301 (2021).

[59] The scaling method here results in a radiative lifetime formula that is analogous to the radiative capture rate formalism  \( [73] \)  as explained in Sec. 59 in the SM  \( [34] \) .

[60] M. Kazemi, M. Keshavarz, M. E. Turiansky, J. L. Lyons, N. V. Abrosimov, S. Simmons, D. B. Higginbottom, and M. L. W. Thewalt, Giant isotope effect on the excited-state lifetime and emission efficiency of the silicon t centre (2025), arXiv:2510.23862 [quant-ph].

[61] T. J. Boerner, S. Deems, T. R. Furlani, S. L. Knuth, and J. Towns, in Pract. Exp. Adv. Res. Comput., PEARC '23 (Association for Computing Machinery, New York, NY, USA, 2023) pp. 173–176.

[62] P. A. Schultz and J. S. Nelson, Appl. Phys. Lett. 78, 736 (2001).

[63] G. H. Wannier, Phys. Rev. 52, 191 (1937).

[64] J. M. Luttinger and W. Kohn, Phys. Rev. 97, 869 (1955).

[65] R. Pässler, Phys. Status Solidi 78, 625 (1976).

[66] D. J. Griffiths, Introduction to Quantum Mechanics, 2nd ed. (Pearson Education, 2005) p. 158.

[67] W. C. Dunlap and R. L. Watters, Phys. Rev. 92, 1396 (1953).

[68] H. Conzelmann, Appl. Phys. A 42, 1 (1987).

[69] A. Sommerfeld, Ann. Phys. 403, 257 (1931).

[70] M. E. Turiansky, A. Alkauskas, and C. G. Van de Walle, J. Phys. Condens. Matter 36, 195902 (2024).

[71] D. J. Griffiths, Introduction to Quantum Mechanics, 2nd ed. (Pearson Education, 2005) p. 151.

[72] L. Alaerts, Y. Xiong, S. M. Griffin, and G. Hautier, Phys. Rev. B 112, 125114 (2025).

[73] C. E. Dreyer, A. Alkauskas, J. L. Lyons, and C. G. Van de Walle, Phys. Rev. B 102, 085305 (2020).
 

# Supplemental Material: A CN complex as an alternative to the T center in Si

J. K. Nangoi, \( ^{1,*} \)  M. E. Turiansky, \( ^{1,2} \)  and C. G. Van de Walle \( ^{1} \) 

 \( ^{1} \) Materials Department, University of California, Santa Barbara, California 93106, USA  
 \( ^{2} \) US Naval Research Laboratory, Washington, DC 20375, USA

## S1. KOHN-SHAM STATES OF NON-NEUTRAL CHARGED STATES

![](2511.00754v1-images/6_0.jpg)

FIG. S1. Ground-state Kohn-Sham states for the non-neutral charged states of the T center  \( [(a)] \)  and the CN defects  \( [(b)-(d)] \) .

## S2. OTHER DEFECTS CONSIDERED

Figures S2(a)–(d) show the lowest-energy structures of  \( C_{Si} \) ,  \( N_{Si} \) ,  \( C_{i} \) , and  \( N_{i} \)  in Si used in this work, consistent with previous first-principles or molecular dynamics calculations [1–5]. Their formation energy diagrams are shown in Fig. S3.

![](2511.00754v1-images/6_1.jpg)

FIG. S2. Atomic structure, in the neutral charge state, of (a)  \( C_{Si} \) , (b)  \( N_{Si} \) , (c)  \( (CSi)_{Si} \) , (d)  \( (NSi)_{Si} \) , (e)  \( C_{Si}(CHSi)_{Si} \)  1, (f)  \( C_{Si}(CHSi)_{Si} \)  2, and (g)  \( (CSi)_{Si}(CH)_{Si} \) .

Because  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  [Fig. 1(c) in the main text] has lower formation energy than  \( (\mathrm{CN})_{\mathrm{Si}} \) , we also explore other analogous structures of CCH complex to see if they are more stable than the T center structure  \( (\mathrm{CCH})_{\mathrm{Si}} \) . We replace N in  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  with C, and place H at various positions: (1) near  \( (\mathrm{CSi})_{\mathrm{Si}} \) , (2) near  \( C_{\mathrm{Si}} \) , and (3) between the 2 carbons. After relaxation,  \( \#(1) \)  becomes two distinct structures of  \( C_{\mathrm{Si}}(\mathrm{CHSi})_{\mathrm{Si}} \) , labeled 1 and 2 [Figs. S2(e) and (f)],  \( \#(2) \)  becomes  \( (\mathrm{CSi})_{\mathrm{Si}}(\mathrm{CH})_{\mathrm{Si}} \)  [Fig. S2(g)],

and  \( \#(3) \)  becomes  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{CHSi})_{\mathrm{Si}} \)  1 [Fig. S2(e)]. As seen in the formation energy diagram [Fig. S3], in the neutral charge state, these structures are actually 0.6–2.5 eV higher in energy than  \( (\mathrm{CCH})_{\mathrm{Si}} \) .

![](2511.00754v1-images/6_2.jpg)

FIG. S3. Defect formation energies as functions of Fermi level for the +1, 0, and -1 charge states of all defects considered. HSE functional and supercell size of  \( 4 \times 4 \times 4 \)  (512 atoms) are used.

## S3. MIGRATION BARRIER OF (NSi)Si

As shown in the main text, the lowest-energy decomposition reaction of  \( (\mathrm{CN})_{Si}^{0} \)  and  \( [\mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}}]^{0} \)  produces  \( C_{Si}^{0} + (\mathrm{NSi})_{Si}^{0} \) , with (endothermic) decomposition energies of 0.61 eV and 0.82 eV. To estimate the barriers for these decomposition reactions, we compute the migration barrier of the interstitial product, namely  \( (\mathrm{NSi})_{Si}^{0} \) .

Reference 6 suggested a pathway for migration of  \( (\mathrm{NSi})_{Si}^{0} \) : the N moves between two equivalent  \( (\mathrm{NSi})_{Si}^{0} \)  sites through the bond-centered site. We therefore perform climbing image nudged elastic band (CI-NEB) calcula-
 

tions [7] between our calculated lowest-energy configuration of  \( (\mathrm{NSi})_{\mathrm{Si}}^{0} \)  [Fig. S4(a), N as black atoms] and the bond-centered configuration of  \( N_{i}^{0} \)  [Fig. S4(a), N as cyan atoms], finding a saddle-point configuration indicated by N as orange atoms. We also perform CI-NEB between 2 neighboring bond-centered configurations (which are equivalent by symmetry), finding a saddle-point configuration for which the N is in gray. In the figure, the atomic sites with the same color are equivalent by symmetry. Figure S4(b) shows the corresponding reaction pathway, for which the configurations are color-coded the same way as in Fig. S4(a). The figure shows that the barrier is 0.68 eV.

(a)

![](2511.00754v1-images/7_0.jpg)

(b)

![](2511.00754v1-images/7_1.jpg)

FIG. S4. (a) Migration pathway of  \( (\mathrm{NSi})_{\mathrm{Si}}^{0} \) . Blue circles are Si. Black circles are nitrogens in equivalent  \( (\mathrm{NSi})_{\mathrm{Si}}^{0} \)  configurations; cyan, bond-centered  \( N_{i}^{0} \) ; gray, intermediate; orange, highest-energy. (b) Formation energy differences with respect to that of  \( (\mathrm{NSi})_{\mathrm{Si}}^{0} \) . Circles label the configurations shown in panel (a), drawn with the same colors.

The results above use HSE with a supercell size of  \( 3 \times 3 \times 3 \)  (216 atoms) which is sufficiently large to converge the reaction barrier within 0.03 eV as tested using PBE. The saddle points are calculated using 1-image CI-NEB (i.e., 1 intermediate configuration between the starting and ending configurations). Using PBE, we have tested that the 1-image calculation results in a saddle-point configuration whose energy is within  \( 2 \times 10^{-5} \)  eV from that obtained using 3-image CI-NEB.
We compute configurations 0 and 2 in Fig. S4(b) using density functional theory (DFT), and then perform 1-image CI-NEB between those two, finding configuration 1. Then, we rotate configuration 2 to construct configuration 4, and perform 1-image CI-NEB between those two, finding configuration 3. Finally, path  \( 4 \rightarrow 6 \)  is equivalent by symmetry to  \( 0 \leftarrow 2 \) .

## S4. BOUND EXCITON WAVEFUNCTION AND SUPERCEL-SIZE DEPENDENCE

As discussed in the main text, the excited state consists of a defect-bound exciton consisting of a hydrogenic hole (electron) bound to an electron (hole) localized at the defect site. As an approximation, we can describe the hydrogenic charge's wavefunction within effective mass theory [8]. Following the ansatz of Kohn and Luttinger [9], the hydrogenic wavefunction takes the form [10]

 \[ \psi_{h}(\mathbf{r})=\sqrt{\mathcal{N}_{0}\Omega_{0}}\phi(\mathbf{r})u_{\mathbf{k}_{0}}(\mathbf{r}), \quad (S1) \] 

where  \( N_{0} \)  is the number of unit cells (each with volume  \( \Omega_{0} \) ) that the wavefunction extends over,  \( u_{k_{0}} \)  is the unperturbed lattice-periodic part of the Bloch function of the crystal (at the k-point  \( k_{0} \)  where the band extremum is located, i.e., VBM for the hydrogenic hole and CBM for the hydrogenic electron) normalized over a single unit cell, and  \( \phi \)  is the envelope function that satisfies the Wannier equation [8, 10], which is normalized over the entire volume  \( N_{0}\Omega_{0} \) . Taking  \( N_{0} \)  to infinity, the negative-energy (bound-state) solutions to the Wannier equation are the hydrogen wavefunctions, scaled appropriately by the band effective mass  \( m^{*} \)  and bulk dielectric constant  \( \epsilon_{r} \) . The corresponding effective Bohr radius  \( a_{0}^{*} \)  that characterizes  \( \phi \)  is then given by

 \[ a_{0}^{*}=\frac{4\pi\epsilon_{0}\hbar^{2}}{e^{2}}\frac{\epsilon_{r}}{m^{*}}. \quad (S2) \] 

For the case of the exciton with a hydrogenic hole, we expect that, as an approximation, the heavy (as opposed to the light) hole makes up the bound exciton, because the Rydberg energy [11], which approximates the excitonic binding energy, is proportional to the effective mass  \( m^{*} \) , and therefore the heavy hole will have larger binding energy. Using the experimental values for the Si heavy hole effective mass of  \( 0.49\;m_{0} \)  [12] (where  \( m_{0} \)  is the free-electron mass) and dielectric constant of 11.7 [13] yields an effective Bohr radius  \( a_{0}^{*} \)  [Eq. (S2)] of  \( \sim13\;Å \)  for the heavy hole. (For the T center, whose experimental binding energy is  \( 35\;meV \)  [14], the corresponding  \( m^{*}=0.35m_{0} \)  is indeed closer to the heavy hole mass than to the light hole mass of  \( 0.16\;m_{0} \)  [12]). The length of the largest supercell size we have considered,  \( 5\times5\times5 \)  conventional cubic cells (1000 Si atoms), is  \( \sim27\;Å \) , around twice  \( a_{0}^{*} \) . As seen in Figs. S5(a)–(c), (e)–(g), and (i)–(k), the hole seems to barely fit in the largest supercell, and appears delocalized over practically the entire supercell for the two smaller ones.
 
![](2511.00754v1-images/8_0.jpg)

FIG. S5. Isosurfaces (yellow) of real-space Kohn-Sham probability densities, shown for the whole supercell, corresponding to the hydrogenic charge in the electronic excited state  \( [(d) \) , (h), (l) for hydrogenic electron “h-e”; rest for hydrogenic hole “e-h”] for supercell size N = 216 (top row), 512 (middle row), and 1000 (bottom row). Here N denotes the number of Si atoms in the defect-free supercell. Blue circles are Si; brown, C; light blue, N; and pink, H. Purple squares indicate the defect sites. The isosurface levels used are 55.16%, 14.23%, 60.15% and 6.42% of the maximum charge density in each supercell for  \( (\mathrm{CCH})_{\mathrm{Si}} \) ,  \( (\mathrm{CN})_{\mathrm{Si}} \) ,  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  e-h and h-e, except for panel (f), for which we use 51.15% (because 14.23% is too small and yields an isosurface that fills the entire supercell).

For the case of the exciton with a hydrogenic electron, we use an effective mass of  \( 0.98~m_{0} \) , equal to the longitudinal mass of the Si CBM (which is larger than the transverse mass  \( 0.19~m_{0} \) ) [12], corresponding to an effective Bohr radius of  \( \sim6~Å \) . We choose the longitudinal mass because, as discussed above, larger effective mass means higher excitonic binding energy. Similar to the hydrogenic-hole case, here we find that the electron seems to barely fit in the largest supercell, and appears to extend beyond the supercell for the two smaller ones.

## S5. HUANG-RHYS FACTOR CALCULATIONS

The Huang-Rhys factor is defined as  \(  S = E_{\mathrm{r}} / (\hbar \Omega)  \)  where  \( E_{r} \)  equals the difference between the ground-state energy at the equilibrium structure of the excited state and that of the ground state, and  \( \Omega \)  is the phonon frequency in the ground state within the one-dimensional approximation [15]; the values of both are reported in Table II in the main text. Figure S6 shows the one-dimensional configuration-coordinate curves for the T center and the CN defects in the electronic ground state.  \( \Omega \)  is calculated from the parabolic fit  \(  E = (1/2) \Omega^{2} Q^{2}  \)  [15] to the energies calculated using DFT.

For the T center,  \( (\mathrm{CN})_{\mathrm{Si}} \) , and  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  localized-electron case “e-h” [Figs. S6(a)–(c)], the DFT-calculated potential energy surface is harmonic until at least the equilibrium excited-state structure. Therefore,  \( E_{r} \)  equals E indicated by the open circle.

For the  \( \mathrm{C}_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  localized-hole case “h-e” [Fig. S6(d)], the DFT-calculated potential energy
 
![](2511.00754v1-images/9_0.jpg)

FIG. S6. (a)–(d) Configuration coordinate curves of the electronic ground state as a function of one-dimensional coordinate Q. Circles are DFT-calculated total energies E referenced to the energy of the equilibrium structures  \( (Q = 0) \) ; only filled circles are used in the parabolic fits (blue curves). (e) Kohn-Sham eigenvalues of the a defect states for  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  as a function of Q: blue = occupied, orange = unoccupied. The vertical dashed line indicates the  \( \Delta Q \)  value for the equilibrium structure of the electronic excited state.

surface appears anharmonic. Figure S6(e) shows the Kohn-Sham eigenvalues of the a states shown in Fig. 3(c) as functions of Q. We see that the unoccupied a state crosses the CBM at  \( Q \approx 1 \) , affecting the behavior of the occupied a state in the gap in such a way that it becomes nonmonotonic. This is consistent with the observation that the apparent potential energy surface in Fig. S6(d) is anharmonic for  \( Q \geq 1 \) . Data points in the anharmonic regime (open circles) are therefore ignored, and we take  \( E_{\mathrm{r}} = (1/2)\Omega^{2}(\Delta Q)^{2} \) , where  \( \Delta Q \)  is the Q for the equilibrium structure of the excited state (Fig. S6).

## S6. FULL VS. SINGLE-SHOT PBE0

TABLE S1. Full vs. single-shot PBE0 results for bulk Si in primitive cell and T center in 216-atom supercell. CTL = charge transition level.  \( \mu^{0} \)  = transition dipole moment in ground state, Eq. (S4).

<table><tr><td></td><td>Full</td><td>Single-shot</td></tr><tr><td>Band gap (eV; bulk Si)</td><td>1.23</td><td>1.23</td></tr><tr><td>Dielectric constant (bulk Si)</td><td>11.736</td><td>11.738</td></tr><tr><td>\( E_{\text{ZPL}} \)  (meV)</td><td>680</td><td>681</td></tr><tr><td>\( E^{\text{f}} \) , neutral charge state (eV)</td><td>2.48</td><td>2.47</td></tr><tr><td>\( E_{\text{CTL},0/-} - E_{\text{VBM}} \)  (eV)</td><td>0.93</td><td>0.93</td></tr><tr><td>\( \mu^{0} \)  (eÅ)</td><td>0.201</td><td>0.195</td></tr></table>

## S7. ZERO-PHONON LINE OF ALL CENTERS

![](2511.00754v1-images/9_1.jpg)

FIG. S7. ZPL energies for the T and all CN centers calculated using single-shot PBE0.

Figure S7 shows that the extrapolated PBE0 ZPLs are 812 meV and 604 meV for  \( C_{\mathrm{Si}}(\mathrm{NSi})_{\mathrm{Si}} \)  localized-electron and localized-hole case. Both of these are far from the observed ZPL range of 746 to 772 meV attributed to complexes containing C and N (and possibly O) [16–21]. A few luminescence lines close to 812 meV have been observed in Si, at 811 meV [22] and 829.8 meV [21].

## S8. RADIATIVE LIFETIME FOR A BOUND EXCITON EMITTER

The transition dipole moment  \( \mu \)  that enters the radiative lifetime  \( \tau \) , Eq. (1), is given by

 \[ |\mu|^{2}=|\langle\psi_{l}|\mathbf{e r}|\psi_{h}\rangle|^{2}, \quad (S3) \] 

where e is the elementary charge, r is the position operator,  \( \psi_{l} \)  is the wavefunction of the charge localized at the defect, and  \( \psi_{h} \)  is the hydrogenic wavefunction given by Eq. (S1). Evaluating  \( |\mu|^{2} \)  explicitly is challenging because  \( \psi_{h} \)  can extend over distances larger than computationally tractable supercell sizes, as discussed in Sec. S4. A more convenient quantity to evaluate is the transition dipole moment  \( \mu^{0} \)  in the ground state (for which there is no bound exciton),

 \[ |\mu^{0}|^{2}=|\langle\psi_{l}|\mathbf{e r}|\psi_{h}^{0}\rangle|^{2}, \quad (S4) \] 

where  \( \psi_{h}^{0} \)  is the free-carrier (Bloch) wavefunction and is given by Eq. (S1) with an envelope function  \( \phi^{0}(\mathbf{r}) = \exp\left(i\mathbf{k}_{0} \cdot \mathbf{r}\right) / \sqrt{N_{0}}\Omega_{0} \) . Because  \( \psi_{h}^{0} \)  is delocalized while  \( \psi_{l} \)  is localized, we expect  \( |\mu^{0}|^{2} \propto 1 / (\mathcal{N}_{0}\Omega_{0}) \) , and we later confirm this with explicit calculations of  \( \mu^{0} \)  (Fig. S8).
 

To get  \( \mu \) , we introduce the approximation

 \[ |\mu|^{2}\approx\frac{|\phi(0)|^{2}}{|\phi^{0}(0)|^{2}}|\mu^{0}|^{2}=\mathcal{N}_{0}\Omega_{0}|\phi(0)|^{2}|\mu^{0}|^{2}\equiv t|\mu^{0}|^{2}, \quad (S5) \] 

where we have assumed that the localized-charge orbital is centered at the origin. We have introduced the dimensionless scaling parameter t in direct analogy to the Sommerfeld parameter  \( [10, 23, 24] \) . For the lowest-energy hydrogenic state,  \( |\phi(0)|^{2} = 1/[\pi(a_{0}^{*})^{3}] \)  [25], where  \( a_{0}^{*} \)  is the effective Bohr radius [Eq. (S2)]. The corresponding t is then

 \[ t=\mathcal{N}_{0}\Omega_{0}/[\pi(a_{0}^{*})^{3}]. \quad (S6) \] 

This approximation assumes that the orbital character of the hydrogenic hole/electron is not significantly changed from the band-edge character; i.e., the main effect of binding is to change the density of the hole/electron near the defect. Since the product of t and  \( |\mu^{0}|^{2} \)  is independent of the volume  \( N_{0}\Omega_{0} \) , we are free to evaluate it in our supercell volume  \( \tilde{V} \)  (i.e., we set  \( N_{0}\Omega_{0} = \tilde{V} \) ). [Using  \( \mu \)  from Eq. (S5) in the expression for radiative lifetime Eq. (1) leads to an expression mathematically equivalent to the radiative capture rate formalism developed for capture of free carriers by localized defects [26], as explained in Sec. S9.]

Figure S8 shows  \( \mu^{0} \)  for the T and CN centers for different supercell sizes, calculated using single-shot PBE0 as described in the main text. These  \( \mu^{0} \)  values correspond to the transitions between the ground-state Kohn-Sham states discussed in the main text and illustrated in Fig. 3 there. Because both the VBM and CBM contain multiple degenerate bands (heavy, light, and split-off bands for the VB, and 6 valleys for the indirect CBM), we project the excited-state band containing the hydrogenic charge to the degenerate ground-state bands, and use the band with the highest projection coefficient to calculate  \( \mu^{0} \) . As seen in Fig. S8,  \( |\mu^{0}|^{2} \)  follows the expected trend of being proportional to  \( 1/N \propto 1/\tilde{V} \) , particularly if we exclude the 216-atom supercell in which the wavefunctions  \( \psi_{l} \)  are probably not as accurately described.

Using the slope of  \( |\mu^{0}|^{2} \)  with respect to  \( 1/N \propto 1/\tilde{V} \)  we obtain  \( \tilde{V}|\mu^{0}|^{2} \) . We then multiply this by  \( 1/[\pi(a_{0}^{*})^{3}] \)  to get  \( |\mu|^{2} \)  [see Eq. (S5)], yielding values reported in Table S2, which includes values for all relevant effective masses (because using the heavy-hole mass, as stated in the main text and Sec. S4 above, is an approximation).

## S9. RELATION TO THE RADIATIVE CAPTURE FORMALISM

Here we note that the radiative lifetime formula with the approximate  \( \mu \)  discussed in the previous section is analogous to the radiative capture rate formalism [26] developed for capture of a free hole (electron) in valence (conduction) band by a localized defect. The difference is that here, (1) we have a charge bound to the defect rather

![](2511.00754v1-images/10_0.jpg)

FIG. S8. Modulus square of the transition dipole moment  \( |\mu^{0}|^{2} \)  [Eq. (S4)] as a function of supercell size. Lines are linear fits constrained to the origin excluding N = 216.

TABLE S2.  \( |\mu|^{2} \)  [Eq. (S5)] and radiative lifetime  \( \tau \)  using various effective masses: holes h, l,  \( E_{b} \)  = heavy, light, determined from experimental binding energy in Ref. 14; electrons  \( \ell \) , t = longitudinal, transverse. “Exp.” = radiative lifetime deduced from experiments in Ref. 27.

<table><tr><td></td><td>h</td><td>l</td><td>\( |\mu|^{2} \)</td><td>\( (\text{e}\text{\AA}^{2}) \)</td><td>Exp.</td><td>\( \ell \)</td><td>t</td></tr><tr><td>\( (CCH)_{Si} \)</td><td>0.0210</td><td>0.0007</td><td>0.0077</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>\( (CN)_{Si} \)</td><td>0.0240</td><td>0.0008</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>\( C_{Si}(NSi)_{Si} \)  e-h</td><td>0.0040</td><td>0.0001</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>\( C_{Si}(NSi)_{Si} \)  h-e</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.8080</td><td>0.0132</td><td></td></tr><tr><td></td><td></td><td></td><td>\( \tau \)  ( \( \mu \) s)</td><td></td><td></td><td></td><td></td></tr><tr><td>\( (CCH)_{Si} \)</td><td>4.70</td><td>135</td><td>12.9</td><td>4.9</td><td>-</td><td>-</td><td></td></tr><tr><td>\( (CN)_{Si} \)</td><td>4.18</td><td>120</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>\( C_{Si}(NSi)_{Si} \)  e-h</td><td>25.55</td><td>734</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>\( C_{Si}(NSi)_{Si} \)  h-e</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.06</td><td>8.23</td><td></td></tr></table>

than a free carrier, and (2) the radiative rate is for each defect-bound exciton, rather than per unit volume of the material containing defects.

Let  \( \Gamma_{R} \equiv 1/\tau \)  be the radiative rate given by Eq. (1) in
 

the main text. Using  \( \mu \)  from Eq. (S5), we obtain

 \[ \Gamma_{\mathrm{R}}\approx t\Gamma_{\mathrm{R}}^{0}=(t/\bar{V})(\bar{V}\Gamma_{\mathrm{R}}^{0})\equiv\rho C_{\mathrm{R}}, \quad (S7) \] 

where  \( \Gamma_{R}^{0} \)  is obtained by substituting  \( |\mu^{0}|^{2} \)  for  \( |\mu|^{2} \)  in Eq. (1). As discussed in the previous section,  \( |\mu^{0}|^{2} \)  is inversely proportional to the supercell volume  \( \bar{V} \) , and therefore  \( \Gamma_{R}^{0} \propto 1/\bar{V} \) . We then define  \( C_{R} \equiv \bar{V}\Gamma_{R}^{0} \) , which

[1] J. Tersoff, Phys. Rev. Lett. 64, 1757 (1990).

[2] A. Platonenko, F. S. Gentile, J. Maul, F. Pascale, E. A. Kotomin, and R. Dovesi, Mater. Today Commun. 21, 100616 (2019).

[3] F. S. Gentile, A. Platonenko, K. E. El-Kelany, M. Rétart, P. D'Arco, and R. Dovesi, J. Comput. Chem. 41, 1638 (2020).

[4] A. Platonenko, F. S. Gentile, F. Pascale, P. D'Arco, and R. Dovesi, J. Comput. Chem. 42, 806 (2021).

[5] C. Simha, G. Herrero-Saboya, L. Giacomazzi, L. Martins-Samos, A. Hemeryck, and N. Richard, Nanomaterials 13, 2123. (2023).

[6] P. A. Schultz and J. S. Nelson, Appl. Phys. Lett. 78, 736 (2001).

[7] G. Henkelman, B. P. Uberuaga, and H. Jónsson, J. Chem. Phys. 113, 9901 (2000).

[8] G. H. Wannier, Phys. Rev. 52, 191 (1937).

[9] J. M. Luttinger and W. Kohn, Phys. Rev. 97, 869 (1955).

[10] R. Pässler, Phys. Status Solidi 78, 625 (1976).

[11] D. J. Griffiths, Introduction to Quantum Mechanics, 2nd ed. (Pearson Education, 2005) p. 158.

[12] M. S. Shur, Handbook Series on Semiconductor Parameters, Vol. 1 (World Scientific, 1996).

[13] W. C. Dunlap and R. L. Watters, Phys. Rev. 92, 1396 (1953).

[14] L. Bergeron, C. Chartrand, A. T. K. Kurkjian, K. J. Morse, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, and S. Simmons, PRX Quan-

is the radiative capture coefficient [26] and is independent of  \( \bar{V} \) . We also define  \( \rho \equiv t/\bar{V} \) , which is the effective density of the holes/electrons at the defect, arising from the Coulombic binding of the carrier to the localized charge. For the lowest-energy hydrogenic state,  \( \rho = [\pi(a_{0}^{\xi})^{3}]^{-1} \) , equal to the modulus square of the envelope function  \( |\phi(0)|^{2} \)  we use in Eq. (S5).

tum 1, 020301 (2020).

[15] A. Alkauskas, J. L. Lyons, D. Steiauf, and C. G. Van de Walle, Phys. Rev. Lett. 109, 267401 (2012).

[16] A. Dörnen, R. Sauer, and G. Pensl, MRS Online Proc. Libr. 59, 545 (1985).

[17] A. Dörnen, G. Pensl, and R. Sauer, Phys. Rev. B 33, 1495(R) (1986).

[18] A. Dörnen, G. Pensl, and R. Sauer, Solid State Commun. 57, 861 (1986).

[19] A. Dörnen, G. Pensl, and R. Sauer, Phys. Rev. B 35, 9318 (1987).

[20] A. Dörnen, R. Sauer, and G. Pensl, J. Electron. Mater. 17, 121 (1988).

[21] G. Davies, Phys. Rep. 176, 83 (1989).

[22] G. Armelles, J. Barrau, V. Thomas, and M. Brousseau, J. Phys. C Solid State Phys. 19, 2593 (1986).

[23] A. Sommerfeld, Ann. Phys. 403, 257 (1931).

[24] M. E. Turiansky, A. Alkauskas, and C. G. Van de Walle, J. Phys. Condens. Matter 36, 195902 (2024).

[25] D. J. Griffiths, Introduction to Quantum Mechanics, 2nd ed. (Pearson Education, 2005) p. 151.

[26] C. E. Dreyer, A. Alkauskas, J. L. Lyons, and C. G. Van de Walle, Phys. Rev. B 102, 085305 (2020).

[27] M. Kazemi, M. Keshavarz, M. E. Turiansky, J. L. Lyons, N. V. Abrosimov, S. Simmons, D. B. Higginbottom, and M. L. W. Thewalt, “Giant isotope effect on the excited-state lifetime and emission efficiency of the silicon t centre,” (2025), arXiv:2510.23862 [quant-ph].
 
