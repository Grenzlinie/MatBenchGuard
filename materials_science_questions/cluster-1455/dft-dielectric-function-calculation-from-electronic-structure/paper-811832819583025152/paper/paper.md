PHYSICAL REVIEW B 80, 115209 (2009)

# Optical properties of pseudobinary GeTe, $Ge_2Sb_2Te_5$, $GeSb_2Te_4$, $GeSb_4Te_7$, and $Sb_2Te_3$ from ellipsometry and density functional theory

Jun-Woo Park, Seung Hwan Eom, and Hosun Lee*
Department of Applied Physics, Kyung Hee University, Suwon 446-701, South Korea

Juarez L. F. Da Silva
National Renewable Energy Laboratory, 1617 Cole Boulevard, Golden, Colorado 80401, USA

Youn-Seon Kang, Tae-Yon Lee, and Yoon Ho Khang
New Memory Laboratory, Samsung Electronics R&D Center, Suwon 440-600, South Korea

(Received 5 May 2009; revised manuscript received 24 June 2009; published 21 September 2009; corrected 22 September 2009)

We study the optical properties and the band structures of (GeTe, $Sb_2Te_3$) pseudobinary compounds experimentally and theoretically by using spectroscopic ellipsometry and density functional calculations. We measure the dielectric functions of (GeTe, $Sb_2Te_3$) pseudobinary thin films—GeTe, $Ge_2Sb_2Te_5$, $Ge_1Sb_2Te_4$, $Ge_1Sb_4Te_7$, and $Sb_2Te_3$—by using spectroscopic ellipsometry. We anneal the thin films at various temperatures. According to x-ray diffraction, the as-grown thin films are amorphous and the annealed films have metastable and stable crystalline phases. By using standard critical-point model, we obtain the accurate values of the energy gap of the amorphous phase as well as the critical-point energies of the metastable and stable crystalline thin films. The optical gap (indirect band gap) energy of the amorphous (crystalline) thin films is estimated by the equation, $(\alpha E)^{1/2}=A(E-E_{opt(ind)})$. As the Sb-to-Ge atomic ratio increases, the optical (band) gap energy of amorphous (crystalline) phase decreases. Standard critical-point model analysis shows several higher band gaps. The electronic band structures, the dielectric functions, and the absorption coefficients of the thin films are calculated by using density functional theory (DFT) and are compared to the measured ones. The band-structure calculations show in stable phase that GeTe, $Ge_2Sb_2Te_5$, and $Ge_1Sb_2Te_4$ have indirect gap whereas $Ge_1Sb_4Te_7$ and $Sb_2Te_3$ have direct gap. The band gaps of metastable phase have similar behavior. The measured indirect band-gap energies are compared to those of the electronic band-structure calculations. The experimental critical-point energies of the pseudobinary compounds, especially GeTe, match well to those of theoretical calculation. The DFT calculations show that the stable and metastable phases have similar dielectric functions and absorption properties, etc., because of the similarity between the lowest-energy crystal structures for both the stable and metastable phases. However, experimental results show that there exist important differences between those of the stable and metastable phases. We discuss the discrepancy in terms of insufficient ordering of vacancies in the real materials of metastable phase.

DOI: 10.1103/PhysRevB.80.115209
PACS number(s): 78.20.Ci, 78.66.Li, 78.40.Fy, 71.20.Nr

## I. INTRODUCTION

Phase change materials such as the ternary (GeTe, $Sb_2Te_3$) (GST) compounds are widely used for rewritable optical storage applications, e.g., compact disk, digital versatile disk, and Blue-ray disks. Beyond of those applications, the GST compounds have been considered as a natural candidate for nonvolatile memory applications. These applications rely on a fast and reversible phase transition between the crystalline and amorphous (AM) GST phases and due to resistance difference between the crystalline and amorphous phases, which yields a different optical contrast between both phases. $^{1,2}$ The recording and erasing processes in optical and electrical storage devices employing thin GST films is obtained upon short irradiation by a laser beam and a joule heating of a very short electronic pulse, respectively. $^{1,2}$ The popular use of GST in optical storage applications have motivated a large number of experimental and theoretical studies of this class of compounds. However, as we will show below, several questions remain open and are under intense debate.

Recent experimental and theoretical studies have provided a deep atom-level understanding of the structure properties of the crystalline and amorphous phases. The GST compounds crystallize into different phases, namely, stable and metastable crystallines (s-GST and m-GST), and amorphous phases (a-GST), which can be obtained by different annealing temperature. The s-GST phase crystallizes in hexagonal structures with space groups $P\overline{3}m$ or $R\overline{3}m$ in which the Ge, Sb, and Te atoms are stacked along of the $c$ axis. The intrinsic vacancies originated from $Sb_2Te_3$ only separate the GST building blocks. The m-GST phase crystallizes in rocksalt-type (RS-type) structures in which the Ge, Sb, and intrinsic vacancies occupy the cation $4b$-type sites and the Te atoms occupy the anion $4a$-type sites. Recent first-principles calculations reported by Da Silva et al. $^{3}$ found that at the lowest-energy structures, the intrinsic vacancies form ordered layers perpendicular to the $c$ axis and hence the GST building blocks are connected by weak binding interactions of few meV. However, at nonequilibrium structures, the intrinsic vacancies might be randomly distributed in the cation sites. Furthermore, they reported that lower energy structures can be identified by maximizing the number of Te atoms surrounded by three Ge and three Sb atoms (called the 3Ge-Te-3Sb rule). The amorphous phase has been widely studied and a consensus has been achieved in a few points. For example,

1098-0121/2009/80(11)/115209(14)
115209-1
©2009 The American Physical Society

the majority atoms show covalent bonding and the coordina- tions around the majority atoms of Ge, Sb, and Te satisfy 8-N rules. $^{4}$ The present knowledge of the atomic structure pro vides the path to obtain a better understanding of the optical contrast between the crystalline and amorphous phases. However, it is important to point out that the mechanism that drives the phase transition from the metastable crystalline to amorphous phases is still under intense debate. There are a large number of studies on the phase-transition mechanism between the crystalline and amorphous phases, $^{5-11}$ as well as on the electronic properties that determine the large differ- ences in resistivity between both crystalline and amorphous phases. $^{12-14}$ Although those studies have provided a great contribution to obtain an atomlike picture of the figures of merit of GST compounds, in particular, $Ge_{2} Sb_{2} Te_{5}$ , a com plete picture that include other compositions is still contro- versial. The GST compounds form three phases such as amorphous, metastable, and stable phases as annealing tem- perature increases. $^{15-17}$ For example, in the case of Ge2Sb2Te5, amorphous phase is transformed into metastable RS phase at $140^{\circ} C$ and subsequently to stable hexagonal(HEX) structure at $250^{\circ} C$ with increasing annealing temperature. $^{18,19}$ One end-point binary GeTe, which has only stable crystalline phase, has a slightly distorted RS structure stretched along $< 111>$ direction below $430^{\circ} C$ for unit cell and can be described as HEX for conventional cell. $^{16}$ Theother end-point binary $Sb_{2} Te_{3}$ has only rhombohedral (RH) structure in crystalline phase and can be also described as HEX for conventional cell. $^{20}$ We note that the amorphous phases are characterized by locally ordered motifs and long- range disorder with the volume expansion of $6 \%$ comparedwith the crystalline phases. $^{21}$

The optical and electronic properties of (GeTe, $Sb_{2} Te_{3}$ ) thins films have been studied by several groups. $^{4,22-25}$ The optical estimate of the optical gap energy of amorphous phase and the lowest band gap of crystalline phase for Ge2Sb2Te, has been done by using the linear extrapolation of the absorption coefficients. $^{22}$ The optical properties and elec tronic structural properties of (GeTe, $Sb_{2} Te_{3}$ ) pseudobinary thin films with increasing $Sb / Ge$ atomic ratio were reported for amorphous and stable phases by Park et al. $^{26}$ Wehnic and co-workers presented $a b$ initio calculations of the optical properties of GeTe and $Ge_{1} Sb_{2} Te_{4}$ in the amorphous and metastable phases and compared those properties to experi- mental data. They reported the correlation between local structural changes and optical properties as well as the origin of the optical contrast in these materials. They attributed the optical contrast between the two phases to the significant changes in the transition matrix elements. According to Shportko et al., $^{27}$ the dielectric functions of GST pseudobi naries in the infrared and visible energy range reveal that the optical dielectric constant $(\varepsilon_{\infty})$ is $70-200 \%$ larger for the crystalline than that of the amorphous phases. This difference is attributed to a significant change in bonding between the two phases, that is, the covalent bonding of the amorphous phase and the resonant bonding of the crystalline phase. In order to predict promising phase-change materials, Lencer et $a l.^{28}$ went further in this resonant bonding model and devel oped a quantitative method, which is based on the ionic and the covalent bonding characteristics. Thus, most of the stud- ies have been done for the $Ge_{2} Sb_{2} Te_{5}$ and so far there are few reports on the systematic comparison between the opti-cal properties and the electronic properties of (GeTe, $Sb_{2} Te_{3}$ ) pseudobinary thin films of all three phases. For example, a combined experimental and theoretical study of electronic band structures of GST compounds as a function of $Sb / Ge$  ratio has not been reported as well as the fundamental gap energies, the dielectric functions, and absorption coefficients for all possible phases of amorphous, metastable, and stable phases.

The information on the critical-point (CP) energies is ba- sic to understand the electronic band structures of the chal- cogenides, where CP is a symmetry point in $E(k)$ band dia gram where the slopes of $E_{c}(k)$ and $E_{v}(k)$ are parallel. $^{29}$ The electronic band structures of the pseudobinaries are impor- tant to understand the optical and electronic properties of the chalcogenides. By using standard critical-point (SCP) model analysis on the dielectric function spectrum, we can deter- mine the $CP$ energies experimentally, which can be com pared to the band-structure calculations.

In this work, we combine experimental ellipsometric tech- niques with density functional theory (DFT) calculations to obtain insights on the optical and electronic properties of $Ge_{2} Sb_{2} Te_{5}, Ge_{1} Sb_{2} Te_{4}$ , and $Ge_{1} Sb_{4} Te_{7}$ . Furthermore, for comparison we study also the parent compounds of GeTeand $Sb_{2} Te_{3}$ . By using parametric optical constant (POC)model, we estimated the dielectric functions $[\varepsilon=\varepsilon_{1}+i \varepsilon_{2}$ =N2=(n+ik)2] for the amorphous and crystalline phases. Theoptical (indirect band) gap energy of amorphous (crystalline) phase was determined by the linear extrapolation of the ab- sorption coefficients. We compared the dielectric functions of the five GST compounds in amorphous, metastable, and stable phases. This work shows how the dielectric functions transform as the Sb-to-Ge atomic ratio increases and also as the phase change occurs. By applying the SCP model on the second derivative of the best-match dielectric functions, we estimated the $CP$ energies. From the DFT calculations we calculated the electronic band structures, dielectric functions, absorption coefficients, and $CP$ energies. Those results are discussed in comparison to experimental data.

## II. EXPERIMENTS
The thin films of GeTe, $Ge_{2} Sb_{2} Te_{5}, Ge_{1} Sb_{2} Te_{4}$ , $Ge_{1} Sb_{4} Te_{7}$ , and $Sb_{2} Te_{3}$ pseudobinary thin films were grown on $SiO_{2}(100 ~nm) / Si$ substrate at room temperature. By using radio-frequency sputtering of single GST targets, amor- phous layers were prepared at RT with base pressure less than $1.0 \times 10^{-8}$ Torr. The compositions of as-prepared and annealed GST layers were checked by inductively coupled plasma atomic emission spectroscopy (Shimadzu ICPS-8100). The films are in the order of increasing $Sb$ content and the nominal thickness was about $100 ~nm$ . The films wereannealed either at $160^{\circ} C$ or at $250^{\circ} C$ for $5 ~min$ in the $N_{2}$  gas ambient by using rapid thermal annealing for crystalliza- tion.
Microstructures and crystal orientations were determined by using a conventional x-ray diffractometer (MacScience Model M18XHF, maximum power $18 ~kW$ ). We measured the

![](./images/811832819583025152_1.jpg)

FIG. 1. (Color online) The $\theta$-2$\theta$ scan spectra of x-ray diffraction of (a) amorphous, (b) 160 °C, and (c) 250 °C-annealed thin films of GeTe, Ge₂Sb₂Te₅, Ge₁Sb₂Te₄, Ge₁Sb₄Te₇, and Sb₂Te₃.

ellipsometric angles ($\Psi$ and $\Delta$) of the thin films by using the spectroscopic ellipsometry (VASE model, J.A. Woollam Inc.) at room temperature at various angles of incidence of 65°, 70°, and 75°. In order to improve the accuracy of the dielectric function measurements, we employed autoretarder. A conventional transmission electron microscopy study shows the polycrystalline property and a very sharp interface between SiO₂ and Ge₂Te₂Sb₅ (not shown here).

## III. EXPERIMENTAL RESULTS

### A. X-ray diffraction

Figure 1 shows the x-ray diffraction spectra of (a) as-grown, (b) 160 °C-, and (c) 250 °C-annealed films. It can be seen clearly that as-grown thin films are AM while the annealed thin films show that the crystals are polycrystalline. In Fig. 1(a), we have broad peaks near 27° and 48° for AM phase instead of sharp x-ray diffraction peaks. In the case of 160 °C annealing, GeTe mainly shows RS phase mixed with a slight portion of AM phase, Ge₂Sb₂Te₅, and Ge₁Sb₂Te₄ shows RS phase, Ge₁Sb₄Te₇ shows HEX phase, and Sb₂Te₃ shows RH phase. At 160 °C, GeTe appears to compose of a major RS phase and a minor AM phase because a broad and weak peak originating from AM phase exists between 26° and 29°. In Fig. 1(b), the metastable phase (RS phase) structure of the GST compounds has two main diffraction peaks of (2,0,0) at 29.8° and (2,2,0) at 42.8° with a small (1,1,1) peak at 26.7° while the stable phase (HEX phase) has (1,0,-3) peak at 28.6° instead of 29.8° with a new peak of (1,0,-6) at 39.0° as shown in Fig. 1.¹⁷,³⁰ In the case of 250 °C-annealed films, GeTe has RS phase, GST compounds have HEX phase, and Sb₂Te₃ has RH phase. We note that the end-point binaries GeTe and Sb₂Te₃ films have RS and RH structures, respectively, whether at 160 °C or at 250 °C. The Ge₁Sb₄Te₇ thin film is known to have a RS phase between 120 and 150 °C although we did not confirm here.¹⁸ Based on the x-ray diffraction data, we can neglect a possible residual AM phase for 250 °C-annealed films.

In summary, we found by using x-ray diffraction that the as-grown thin films were amorphous and the thin films after annealing at 160 °C showed distorted RS structure for GeTe, Ge₂Sb₂Te₅, and Ge₁Sb₂Te₄, HEX structure for Ge₁Sb₄Te₇ and RH structure for Sb₂Te₃. After annealing at 250 °C, the thin films showed the same structures as those of 160 °C annealing for GeTe, Ge₁Sb₄Te₇, and Sb₂Te₃, respectively, whereas the thin films showed HEX structure for Ge₂Sb₂Te₅ and Ge₁Sb₂Te₄.

### B. Ellipsometry

Figure 2 shows the raw (discrete symbols) and the best-match (solid lines) ellipsometric angles ($\Psi$ and $\Delta$) for (a) as-grown, (b) 160 °C-annealed, and (c) 250 °C-annealed Ge₂Sb₂Te₅ thin films. The angle of incidence was varied as 65° (circle), 70° (triangle), and 75° (rectangle). The ellipsometric angles for other thin films are not shown here for simplicity.

![](./images/811832819583025152_2.jpg)

FIG. 2. (Color online) The raw (discrete symbols) and fitted (solid lines) ellipsometric angles ($\Psi$ and $\Delta$) for (a) as-grown, (b) 160 °C-annealed, and (c) 250 °C-annealed $Ge_2Sb_2Te_5$ thin films. The angle of incidence was varied as 65° (circle), 70° (triangle), and 75° (rectangle).

We assumed four phase model of surface roughness ($\sim$10 nm), main GST layer ($\sim$100 nm), $SiO_2$ layer (107 nm), and Si substrate and estimated the layer dielectric functions of the GST thin films by using POC model as shown in Table I. We employ the POC model developed by Johs et al.,$^{31,32}$ which can provide a Kramers-Kronig-consistent model dielectric function and has been successfully applied to the dielectric functions of polymers as well as to crystalline and amorphous semiconductors. We note that a point-by-point fitting provided the same layer dielectric functions as those of POC model for most of the thin films. We adopted an isotropic layer model even for HEX phase because they are polycrystals.

We note that the amorphous (as grown), 160, and 250 °C thin films studied in our work were grown as the different batch of samples and were grown a couple of months apart from each other. Therefore, accurate comparison of the film thicknesses, i.e., density change, due to phase transformation is not possible in our work. In order to compare the change in densities due to amorphous-to-crystalline phase transition exactly, we have to compare the same film in different phases. For example, we have to measure the thickness of an amorphous film and then remeasure the thickness of the same sample after annealing. The estimated roughness thickness of amorphous and crystalline $Ge_2Sb_2Te_5$ thin films in our work is 4.2 nm (amorphous) and 7.4 nm (RS), which is consistent with literature values of, for example, 6 nm (amorphous) to 7.5 nm (fcc) for $Ge_2Sb_2Te_5$ in Table I from Orava et al.$^{33}$ Lee et al.$^{24}$ also noted that the best match of their ellipsometric data was obtained with the estimated surface

TABLE I. The thin-film thickness of (GeTe, $Sb_2Te_3$) pseudobinary compounds estimated by the ellipsometry and the crystal structure of the thin films determined by x-ray diffraction. The total layer thickness is the sum of those of the surface roughness layer and the main layer. The uncertainty of the total layer thickness was about 0.4 nm with 95% reliabilities. We note that the surface roughness layer includes oxide layer. Here, AM, RS, HEX, and RH denote amorphous, rock-salt, hexagonal, and rhombohedral phases, respectively.

<table>
  <thead>
    <tr>
      <th>Phase, thickness (nm)</th>
      <th>GeTe</th>
      <th>$Ge_2Sb_2Te_5$</th>
      <th>$Ge_1Sb_2Te_4$</th>
      <th>$Ge_1Sb_4Te_7$</th>
      <th>$Sb_2Te_3$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>As grown</td>
      <td>AM<br>116.5 (7.3/109.2)</td>
      <td>AM<br>137.3 (4.2/133.1)</td>
      <td>AM<br>112.6 (4.7/107.9)</td>
      <td>AM<br>162.1 (5.7/156.4)</td>
      <td>AM<br>159.7 (17.8/141.9)</td>
    </tr>
    <tr>
      <td>160 °C annealed</td>
      <td>Mixture of RS and AM</td>
      <td>RS<br>127.4(7.4/120.0)</td>
      <td>RS<br>111.1(9.8/101.3)</td>
      <td>HEX<br>150.0(11.1/138.9)</td>
      <td>RH<br>170.0(22.3/147.7)</td>
    </tr>
    <tr>
      <td>250 °C annealed</td>
      <td>RS<br>101.4 (18.1/83.3)</td>
      <td>HEX<br>109.5 (5.9/103.6)</td>
      <td>HEX<br>96.0 (7.6/88.4)</td>
      <td>HEX<br>137.0 (9.0/128.0)</td>
      <td>RH<br>151.3(26.6/124.7)</td>
    </tr>
  </tbody>
</table>

layer thickness of 6 nm (RS) for $Ge_2Sb_2Te_5$. Orava et al. $^{33}$ also noted that the ellipsometric measurement may exaggerate the roughness thickness compared to the atomic force microscopy measurement because ellipsometry cannot discern the surface roughness from the oxide overlayer. Indeed, the estimated roughness thickness include oxide thickness as well as true surface roughness. For group IV and III-V semiconductors, Aspnes and Studna $^{34}$ have shown that spectroscopic ellipsometry cannot differentiate the surface roughness from oxide overlayer. It has been reported that GST ternary compounds may be subject to long-time oxidation. $^{35}$ In the case of Si, the oxide thickness grows very slowly after a rapid initial oxidation of 2 or 3 nm thickness. However, the oxygen atoms seems to penetrate the GST thin films gradually and persistently for GST thin films although detailed mechanism of the oxidation is not verified yet. However, in the case of GeTe and $Sb_2Te_3$, the roughness estimated in our study is somewhat large. Especially, one of the end-point binary, $Sb_2Te_3$ has roughness thickness as large as 20 nm whether as grown or annealed. Therefore, GeTe as well as $Sb_2Te_3$ thin films may have either large roughness or substantial oxidation more severe than GST alloys.

Figure 3 shows the best-match dielectric functions ($\varepsilon_1$ and $\varepsilon_2$) of various phases (AM, RS, HEX, and RH) by using POC model for (a) GeTe, (b) $Ge_2Sb_2Te_5$, (c) $Ge_1Sb_2Te_4$, (d) $Ge_1Sb_4Te_7$, and (e) $Sb_2Te_3$. The amplitude of dielectric function increases in amorphous phase as Sb content increases. We find a large change in the amplitudes between the dielectric functions of amorphous and crystalline phases except that of $Sb_2Te_3$. Furthermore, we also find a large change of dielectric functions between RS and HEX phases for those of $Ge_2Sb_2Te_5$ and $Ge_1Sb_2Te_4$.

Figure 4 is the plot of the absorption coefficients ($\alpha$) of various phases for (a) GeTe, (b) $Ge_2Sb_2Te_5$, (c) $Ge_1Sb_2Te_4$, (d) $Ge_1Sb_4Te_7$, and (e) $Sb_2Te_3$, which were derived from Fig. 3. The absorption coefficient $\alpha$ can be obtained from the equation $\alpha$=$4\pi k/\lambda$, where $k$ is the extinction coefficient and $\lambda$ is the wavelength. The absorption coefficients increase in the order of AM, RS, and HEX. For $Ge_2Sb_2Te_5$ and $Ge_1Sb_2Te_4$, the values of $\alpha$ for RS phase are in the middle of those of AM and HEX in the spectral range between 2 and 3 eV.

## IV. DENSITY FUNCTIONAL THEORY CALCULATIONS

Our band-structure calculations are based on the all-electron projector augmented wave method $^{36,37}$ and DFT within the generalized gradient approximation of Perdew et al. $^{38}$ as implemented in VASP (Vienna ab initio simulation package). $^{39,40}$ For all calculations, the Ge $3d$ states were considered as part of the valence, which implies 14 valence electrons while for Te and Sb we considered six valence electrons. For the band structures, dielectric functions, and absorption properties, we employed a cutoff energy of 288 eV while the Brillouin-zone integration was performed using a $(18\times18\times6)$ $k$-point Monkhorst-Pack grid (202 $k$ points in the irreducible Brillouin zone of GeTe in the conventional hexagonal cell). The same $k$-point density was employed for all other calculations. For the crystalline phases of GeTe, GST, and $Sb_2Te_3$, we employed the structure models and equilibrium lattice parameters reported in Ref. 3, which are shown in Fig. 5 and Table II. Those structures were obtained by a full relaxation of the volume, shape, and atomic positions of the unit cell to minimize the quantum-mechanical stresses and forces. We note that the RS and RH crystal structures are studied in the conventional HEX unit cell for DFT calculations. The procedure used to obtain those crystalline (c-) GST structures as well as the structure mechanisms derived from those DFT calculations are discussed in details in Ref. 3. For the a-GST phase, we will employ the a-GST structure models reported in Ref. 43, which were obtained by first-principles molecular dynamics simulations at high temperatures using the same approach adopted in previous a-GST studies. $^{6,44,45}$ For the electronic structure analysis, all results were averaged over three model structures for each composition in order to improve the quality of our analysis by taking into account that different a-GST structures yields slightly different electronic properties. One model crystal structures for each GST composition are shown in Fig. 5 for visualization, however, its structure details will not be discussed in this work, as they are discussed in Refs. 3 and 43.

## V. DISCUSSION

As the c-GST compounds are described by hexagonal lattices, the band structures of the GeTe and $Sb_2Te_3$ compounds were calculated using also their conventional hexagonal lattices even though their primitive rhombohedral cells are one third smaller. Figure 6 shows the electronic band structures of metastable and stable phases for GST compounds. Except for the electronic band structure of quasi-isotropic GeTe, those of other chalcogenides are very complex. We found that GeTe has an indirect band gap, $E_g$, of 0.66 eV in which the valence-band maximum (VBM) is located near the $\Gamma$ point while the conduction-band minimum is located at the L point. The band gap at L point is 0.75 eV, i.e., only 0.09 eV larger than the indirect band gap. Furthermore, in the valence band the A point is higher by about 0.18 eV than the $\Gamma$ point. In contrast to the GeTe system, we found a direct band gap of 0.17 eV for $Sb_2Te_3$ located at the $\Gamma$ point. In the valence band, the $\Gamma$ point is higher by about 0.20 eV than the A point, which is opposite to the GeTe in which the A point is higher in energy.

In the combined GeTe and $Sb_2Te_3$ systems, i.e., $(GeTe)_m(Sb_2Te_3)_n$, we would predict that the electronic features of both phases would be present, which is in fact obtained in our calculations. We want to point out that our results for the GST compounds in both metastable and stable phases are based on calculations for the lowest-energy structures in which all intrinsic vacancies are ordered in planes perpendicular to the $c$ axis in the hexagonal lattice while at real conditions the intrinsic vacancies in the metastable phase might be randomly distributed. We found that the nature of the band gap, i.e., indirect or direct, depends on the composition. For all compositions, we found a larger band gap for the metastable phase, e.g., 0.41 eV (stable) and 0.51 (metastable) eV for $Ge_2Sb_2Te_5$, 0.43 eV (stable) and 0.55 eV

![](./images/811832819583025152_3.jpg)

FIG. 3. (Color online) Best-match dielectric functions ($\varepsilon_1$ and $\varepsilon_2$) of various phases (AM, RS, HEX, and RH) by using POC model for (a) GeTe, (b) $Ge_2Sb_2Te_5$, (c) $Ge_1Sb_2Te_4$, (d) $Ge_1Sb_4Te_7$, and (e) $Sb_2Te_3$. Lines and lines with symbols denote dielectric functions of amorphous and crystalline phases, respectively. Unfilled circular and triangle symbols denote the real and imaginary dielectric functions of RS phase, respectively. Filled circular and triangle symbols denote the real and imaginary dielectric functions of HEX phase, respectively. Finally, unfilled rectangular and diamond symbols denote the real and imaginary dielectric functions of RH phase, respectively.

(metastable) for $Ge_1Sb_2Te_4$, and 0.34 eV (stable) and 0.51 eV (metastable) for $GeSb_4Te_7$. In Table III, we summarized the band gaps for GST pseudobinary compounds.

Our results for the nature of the band gap, i.e., direct or indirect, should be taken with caution due to the small differences between the indirect and direct band gaps as shown in the band-structure diagram in Fig. 5. For example, let us discuss the band gaps of stable phase. For $Ge_1Sb_2Te_4$, our results indicate an indirect band gap of 0.43 eV slightly away from the A point, however, the direct band gap at the A point is 0.46 eV, i.e., a difference of 0.03 eV. Furthermore, the valence-band values at the $\Gamma$ and A points differ by only about 0.05 eV. We found a direct band gap for $Ge_1Sb_4Te_7$ located at the $\Gamma$ point, which is similar to $Sb_2Te_3$. This is expected if we take into account that $Ge_1Sb_4Te_7$ is composed by one GeTe formula unit and two $Sb_2Te_3$ formula units. Thus, even though we calculated only three compositions, our results appear to indicate that GST compounds have a slightly indirect band gap for high GeTe compositions and direct band gap for high $Sb_2Te_3$ compositions for both stable and metastable phases, which is consistent with the results obtained for the end-point binaries, GeTe and $Sb_2Te_3$. That is, GeTe, $Ge_2Sb_2Te_5$, and $Ge_1Sb_2Te_4$ have indirect gap, and $Ge_1Sb_4Te_7$ and $Sb_2Te_3$ have direct gap for stable phase.$^{26,47}$

![](./images/811832819583025152_4.jpg)

FIG. 4. (Color online) Absorption coefficients $(\alpha)$ of various phases for (a) GeTe, (b) Ge₂Sb₂Te₅, (c) Ge₁Sb₂Te₄, (d) Ge₁Sb₄Te₇, and (e) Sb₂Te₃, which were derived from Fig. 3. They are plotted in the same scale.

Figure 7 shows how to estimate the optical (indirect) gap energies for (GeTe, Sb₂Te₃) pseudobinary thin films by the linear extrapolation of the measured absorption coefficients. The optical gap energy of the amorphous and the indirect band-gap energy of crystalline thin films are estimated by the equation $(\alpha E)^{1/2}=A(E-E_{opt(ind)}).^{24}$ Figure 8 shows the estimated optical (indirect band) gap energies for (GeTe, Sb₂Te₃) thin films for various phases. In crystalline phase, the indirect band-gap energy is about 0.5–0.6 eV whether in RS, HEX, or RH phase. The band-gap energy of RS phase is slightly smaller than those of HEX phase for Ge₂Sb₂Te₅ and Ge₁Sb₂Te₄ whereas the band-structure calculations show the opposite. The magnitude of our calculated band gaps are in good agreement with experimental results taken into account the well-known deficiencies in plain DFT to describe band gaps in semiconductors systems. Even though the estimated optical (indirect) gap energies are below our spectral range, we could estimate them by using linear extrapolation method.

The calculated fundamental band-gap energies decrease as the Sb contents increases and the band-gap energies are GeTe (0.66 eV), Ge₂Sb₂Te₅ (0.41 eV), Ge₁Sb₂Te₄ (0.43 eV), Ge₁Sb₄Te₇ (0.34 eV), and Sb₂Te₃ (0.17 eV) for stable phase. The decrease in the indirect band gap for stable phase with increasing Sb composition is consistent with the experimental results shown in Fig. 8. The calculated direct band-gap energy for Ge₁Sb₄Te₇ (0.32 eV) and Sb₂Te₃ (0.14 eV) is below the experimental spectral energy range and therefore they could not be compared to experimental values. Note that in the literature the optical gap and band-gap energies of

![](./images/811832819583025152_5.jpg)

FIG. 5. (Color online) Crystal structures for (GeTe, $Sb_2Te_3$) pseudobinary compounds for metastable and stable phases.

$Sb_2Te_3$ were reported to be 0.55-0.8 eV and 0.15-0.22 eV, respectively, and are consistent with the measured optical gap energy (0.52 eV) and the calculated band-gap energy (0.14 eV) in our work. $^{46}$

In Fig. 8, the experimental band-gap energy of RS phase is slightly smaller than those of HEX phase for $Ge_2Sb_2Te_5$ and $Ge_1Sb_2Te_4$ whereas the band-structure calculations show the opposite. In Table III, at the average, we found a smaller band gap for the stable phase by 0.13 eV, whereas experi- mental results found smaller band gaps for the metastable phase, i.e., about 0.06 eV. This phenomenon may arise pos- sibly because vacancies are not well ordered in real meta- stable phase in contrast to the theoretical model.

In our data, the optical gap energy of the AM phase and the indirect band-gap energy of RS and HEX band-gaps val- ues of $Ge_2Sb_2Te_5$ are 0.80, 0.50, and 0.57 eV, respectively, in contrast to the calculations of 0.51 eV (RS, metastable) and0.41 eV (HEX, stable) as shown in Table III and Fig. $8.^{24,44}$  These values match well with literature. For example, Lee et $a l.^{24}$ reported that the optical gap energy for $Ge_{2} Sb_{2} Te_{5}$ in AM phase is 0.7 eV whereas that of RS (and HEX) phase is0.5 eV. Kato and Tanaka $^{35}$ reported for $Ge_{2} Sb_{2} Te_{5}$ that the optical gap energy is 0.74 eV for AM phase and the indirect- gap energy is 0.5 eV for both RS and HEX phases. Lee et $a l.^{48}$ measured the VBM of $Ge_{2} Sb_{2} Te_{5}$ by using photoemis sion spectroscopy and reported that the VBM increases for amorphous-to-RS structural transition whereas no change for RS-to-HEX transition.

In order to compare to the experimental dielectric func- tion in Fig. 3, we calculated the dielectric functions (real and imaginary parts) by using the longitudinal pseudopotential approach as implemented in VASP, $^{49,50}$ which has been used in the study of semiconductors. $^{51}$ In this approach, the tran sition matrix elements between the valence and conduction bands are used to derive the imaginary part of the dielectric function while the real part of the dielectric functions is ob- tained from the imaginary part through the Kramers-Kronig relations. $^{52}$ In order to obtain consistent and accurate dielec tric functions, the number of states in the conduction band(empty bonds) was set to half of the number of valence elec- trons in each supercell as a rule. For example, for GeTe, we have 240 electrons in the conventional hexagonal cell, which implies 120 empty states in the conduction band. Due to the hexagonal lattice of the c-GeTe, c-GST, and c- $Sb_{2} Te_{3}$ com pounds, there are two different components for the dielectric functions, i.e., parallel and perpendicular components, which are averaged $(\varepsilon=\frac{\varepsilon_{\perp}+2 \varepsilon_{\|}}{3})$ in the present work and will not be discussed separately.

Figure 9 shows the calculated real and imaginary parts of the dielectric function for amorphous, metastable, and stable phases for GST compound thin films. In the case of stable

TABLE II. Lattice parameters of the GeTe, GST, and $Sb_{2} Te_{3}$ compounds. $a_{0}$ is given per $(1 ×1 ×1)$ unit cell while $c_{0}$ is given per number of building blocks in the $(1 ×1 ×1)$ hexagonal cell. The numbers in parentheses are obtained using the lattice constants of GeTe and $Sb_{2} Te_{3}$ . The experimental results for the metastable phase are obtained from the averaged $a_{0}^{RS-type}$ .

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="4">Stable hexagonal GST structures</th>
<th colspan="4">Metastable rocksalt GST structures</th>
</tr>
<tr>
<th></th>
<th>$a_{0}$ (Å)</th>
<th></th>
<th>$c_{0}$ (Å)</th>
<th></th>
<th>$a_{0}$ (Å)</th>
<th></th>
<th>$c_{0}$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>GeTe</td>
<td>4.23</td>
<td>$4.17^{a}$</td>
<td>3.64</td>
<td>$3.54^{a}$</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$Ge_{2}Sb_{2}Te_{5}$</td>
<td>4.27</td>
<td>$4.22^{b}$</td>
<td>17.89</td>
<td>$17.24^{b}$</td>
<td>4.27</td>
<td>$4.26^{b}$</td>
<td>18.36</td>
<td>$17.40^{b}$</td>
</tr>
<tr>
<td>$Ge_{1}Sb_{2}Te_{4}$</td>
<td>4.31</td>
<td>$4.27^{c}$</td>
<td>14.04</td>
<td>$13.90^{c}$</td>
<td>4.30</td>
<td>$4.27^{c}$</td>
<td>14.38</td>
<td>$13.96^{c}$</td>
</tr>
<tr>
<td>$Ge_{1}Sb_{4}Te_{7}$</td>
<td>4.32</td>
<td></td>
<td>24.42</td>
<td></td>
<td>4.30</td>
<td></td>
<td>25.26</td>
<td></td>
</tr>
<tr>
<td>$Sb_{2}Te_{3}$</td>
<td>4.34</td>
<td>$4.26^{d}$</td>
<td>10.43</td>
<td>$10.15^{d}$</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

$^{a}$Expt. Ref. 16.
$^{b}$Expt. Ref. 19.
$^{c}$Expt. at 873 K, Ref. 41.
$^{d}$Expt. Ref. 42.

![](./images/811832819583025152_6.jpg)

FIG. 6. Electronic band structures of metastable and stable phases for (GeTe, Sb₂Te₃) pseudobinary thin films.

phase, in accordance with the experimental dielectric func- tion spectra in Fig. 3, the main peaks of the imaginary di- electric functions are located between 1 and 2 eV, and the amplitudes of pseudobinary compounds are larger than those of the end-point binaries.²³,²⁷ In Fig. 9 we found small dif- ference between the stable and metastable phases, which re- flects their minor structure differences (Te stacking) as the intrinsic vacancies form ordered structures perpendicular to the $c$ axis in both cases at their lowest-energy structures in theoretical model.³ However, experimentally we found large difference between the dielectric functions between meta- stable and stable phases as is shown in Fig. 3.

We found clear differences between the crystalline and amorphous phases both experimentally and theoretically, which can provide insights into the electronic structure dif- ferences between both phases. For example, the real part of the dielectric function at the zero energy limit has different values for both phases. In particular, the amorphous phase

TABLE III. Interband transition and band-gap energy of (GeTe, Sb₂Te₃) pseudobinary thin films calculated by using DFT.

<table>
<thead>
  <tr>
    <th rowspan="2"></th>
    <th>Amorphous phase</th>
    <th colspan="2">Metastable phase</th>
    <th colspan="2">Stable phase</th>
  </tr>
  <tr>
    <th>Optical gap energy (eV)</th>
    <th>Interband transition</th>
    <th>Band-gap energy (eV)</th>
    <th>Interband transition</th>
    <th>Band-gap energy (eV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>GeTe</td>
    <td>0.80ᵃ</td>
    <td></td>
    <td></td>
    <td>$K_{v}$-$\Gamma_{v} \leftrightarrow \Gamma_{c}$</td>
    <td>$E_{ind}$=0.66 (0.61ᵃ)</td>
  </tr>
  <tr>
    <td>Ge₂Sb₂Te₅</td>
    <td>0.80ᵃ,0.7ᵇ,0.74ᶜ</td>
    <td>$\Gamma_{v} \leftrightarrow \Gamma_{c}$ away</td>
    <td>$E_{ind}$=0.51 (0.5ᵃ,ᵇ,ᶜ)</td>
    <td>$\Gamma_{v} \leftrightarrow \Gamma_{c}$ away</td>
    <td>$E_{ind}$=0.41 (0.57ᵃ, 0.5ᵇ,ᶜ)</td>
  </tr>
  <tr>
    <td>Ge₁Sb₂Te₄</td>
    <td>0.71ᵃ</td>
    <td>$A_{v} \leftrightarrow A_{c}$ away</td>
    <td>$E_{ind(dir)}$=0.55 (0.49ᵃ)</td>
    <td>$A_{v} \leftrightarrow A_{c}$ away</td>
    <td>$E_{ind}$=0.43 (0.55ᵃ)</td>
  </tr>
  <tr>
    <td>Ge₁Sb₄Te₇</td>
    <td>0.70ᵃ</td>
    <td>$A_{v} \leftrightarrow A_{c}$ ($\Gamma_{v} \leftrightarrow \Gamma_{c}$)</td>
    <td>$E_{ind}$=0.51</td>
    <td>$A_{v} \leftrightarrow A_{c}$</td>
    <td>$E_{dir}$=0.34</td>
  </tr>
  <tr>
    <td>Sb₂Te₃</td>
    <td>0.52ᵃ,0.55–0.8ᵈ</td>
    <td></td>
    <td></td>
    <td>$\Gamma_{v} \leftrightarrow \Gamma_{c}$</td>
    <td>$E_{dir}$=0.17 (0.15–0.22ᵈ)</td>
  </tr>
</tbody>
</table>

ᵃExpt. in this work.
ᵇExpt. Ref. 24.
ᶜExpt. Ref. 35.
ᵈExpt. Ref. 46 and references therein.

![](./images/811832819583025152_7.jpg)

FIG. 7. (Color online) Estimate of the optical (indirect) gap energies for (GeTe, Sb₂Te₃) pseudobinary thin films by the linear extrapolation of absorption coefficients.

has a smaller dielectric function for all compositions, which is also consistent with recent experimental results by Shportko et al.²⁷ Furthermore, we can see in Fig. 9 that it is composition dependent, i.e., large difference for Ge₂Sb₂Te₅ and smaller for Ge₁Sb₄Te₇. The calculated dielectric constant values $\varepsilon_{\infty}$ are summarized in Table IV along with reported experimental results.²⁷ Clearly, our results are overestimated compared with experimental results, which is a simple consequence of the underestimation of the band gap for the amorphous phase, in particular. However, the trends are correctly described.

In order to obtain further insights, we also calculated the absorption coefficients from the imaginary and real parts of the dielectric functions.⁵³ Figure 10 shows the calculated absorption coefficients for amorphous, metastable, and stable phases for various GSTs. As expected, we obtained small differences between the crystalline stable and metastable phases in contrast to the substantial difference of experimental data in Fig. 4. For all compositions and phases, we do not obtain strong absorption for energies below 1.0 eV due to the weak transitions for energies below the band gap. For the crystalline phases we observe a substantial increasing in the absorption for energies above 1.0 eV up to about 2.5–3.0 eV, from which the absorption drops slowly. However, a different behavior is observed for the amorphous phase. For the amorphous phase, the absorption increases almost linearly up to about 3.0 eV.

![](./images/811832819583025152_8.jpg)

FIG. 8. (Color online) The best-match optical (indirect) gap energies for (GeTe, Sb₂Te₃) pseudobinaries by using linear extrapolation of absorption coefficients. The uncertainty was about 0.01eV.

![](./images/811832819583025152_9.jpg)

FIG. 9. (Color online) Calculated (a) real and (b) imaginary parts of the dielectric function for amorphous, metastable, and stable phases for (GeTe, Sb₂Te₃) pseudobinary thin films.

The small difference of both the calculated dielectric functions and the absorption coefficients between RS and HEX phases for GST compounds in Figs. 9 and 10 are in contrast to the substantial difference of those of the experimental data for Ge₂Sb₂Te₅ and Ge₁Sb₂Te₄ in Figs. 3 and 4. For the metastable phase, as we noted in Sec. III, the distribution of the intrinsic vacancies depends on the growth/annealing conditions, and hence, this effect is not taken into account by our calculations where the metastable phase has a complete ordering of voids. The DFT calculations shows that the both stable and metastable phases have similar absorption and dielectric functions, etc, because of the similarity between the lowest-energy structures for both the stable and metastable phases. However, the experimental results in

<table>
<caption>TABLE IV. Dielectric constant $\varepsilon_{\infty}$ of GeTe, GST, and Sb₂Te₃. The s-GST, m-GST, and a-GST indicate stable, metastable, and amorphous GST. Note. The numbers in parentheses are experimental results from Ref. 27.</caption>
<thead>
<tr>
<th>
</th>
<th>
s-GST
</th>
<th>
m-GST
</th>
<th>
a-GST
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
GeTe
</td>
<td>
39.28(33.2)
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Ge₂Sb₂Te₅
</td>
<td>
45.75
</td>
<td>
40.85(33.3)
</td>
<td>
28.82(16.0)
</td>
</tr>
<tr>
<td>
GeSb₂Te₄
</td>
<td>
45.46
</td>
<td>
39.15(36.2)
</td>
<td>
26.97(16.6)
</td>
</tr>
<tr>
<td>
GeSb₄Te₇
</td>
<td>
44.99
</td>
<td>
36.59
</td>
<td>
32.53
</td>
</tr>
<tr>
<td>
Sb₂Te₃
</td>
<td>
45.36
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

![](./images/811832819583025152_10.jpg)

FIG. 10. (Color online) Calculated absorption coefficients for amorphous, metastable, and stable phases for (GeTe, $Sb_2Te_3$) pseudobinary thin films.

Figs. 3 and 4 show that there exist important differences between those of the stable and metastable phases. This phenomenon may occur because the intrinsic vacancies of the real thin films are not ordered as in the lowest-energy metastable structures. Thus, these results imply that the structure of the metable phase depends on the experimental preparation. We empathize that we use the lowest-energy structures for metastable phases for theoretical model. Therefore we need equilibrium structure for a particular temperature in which the vacancies are disordered. The difference and similarity between metastable and stable phases has been investigated by Matsunaga et al. $^{19}$ They, indeed, noted that the stable phase has no vacancy in the Ge/Sb layer, whereas the metastable phase have vacancies in the layer. The dielectric functions and the band-gap energies of amorphous and crystalline phases were also studied by using optical spectroscopy, DFT, and resonant bonding model by others; Ref. 23 only considered the dielectric functions of amorphous and metastable phase of GeTe and $Ge_1Sb_2Te_4$. Reference 27 measured the dielectric functions and band gaps of several GST pseudobinary compounds and explained the large enhancement of polarizability of crystalline phase over amorphous phase in terms of resonant bonding model.

The SCP model assumes simple parabolic dispersion relations for the valence and conduction bands for semiconductors. The SCP line shape equation is given by $^{29}$

$$
\varepsilon(E)=C-A e^{i \Phi}\left(E-E_{t h}+i \Gamma\right)^{n}, \quad \text { (1) }
$$

where the CP is described by the amplitude $A$, the threshold energy $E_{t h}$, the broadening $\Gamma$, and the excitonic phase angle $\Phi$. The exponent $n$ takes the values of $-1 / 2$ for one-dimensional, 0 [logarithmic, i.e., $\ln (E-E_{t h}+i \Gamma)$ ] for two dimensional, and $1 / 2$ for three-dimensional CPs. Discrete excitons are represented by $n=-1$. Here the excitonic phase angle $\Phi$ represents a coupling between the discrete exciton states and continuum band states or a mixture between two CPs. To remove the background contribution, we fit the second derivative of the dielectric function with respect to energy $(d^{2} \varepsilon / d E^{2})$ by using the SCP model. The SCP model is a generalization of Lorentzian oscillator and has been successfully applied to polymers as well as semiconductors. $^{54}$ By using SCP model, we obtained the accurate values of the optical transition energy of the amorphous thin films as well as the CP energy of the crystalline thin films. $^{29}$ In the case of amorphous semiconductors, the SCP model can be still applied as a phenomenological model even though the band picture is not applicable.

Figure 11 shows the second derivative spectra of the dielectric functions, $\varepsilon=\varepsilon_{1}+i \varepsilon_{2}=(n+i k)^{2}$ of Fig. 3. We denoted the CP energies as $E_{\mathrm{a}}, E_{\mathrm{b}}, E_{\mathrm{c}}, E_{\mathrm{d}}, \ldots$ in the order of increasing band-gap energy. In Fig. 11, the $E_{\mathrm{a}}$ CP energy decreases after crystallization except for $Ge_{1}Sb_{2}Te_{4}$. This is consistent with the fact that the indirect-gap energy of the crystalline phase is smaller than the optical gap energy of the amorphous phase. $^{23,24}$ The main optical structure arises between 1 and 2 eV regions. Figure 11 also shows that several optical structures appear as a result of crystallization. In Fig. 11, we found that the excitonic fitting was the best compared to one-, two-, and three-dimensional CP fitting for both amorphous and crystalline phases. We attribute the exciton best match to the localization of the electronic wave function both in the crystalline and amorphous phases of (GeTe, $Sb_2Te_3$) pseudobinaries. The localization of wave functions can lead to strong interactions among electrons. $^{29}$ The thin films are disordered by defects of various kinds, which can lead to the localization of electronic wave functions. Even the end-point binary GeTe has substantial intrinsic vacancies. $^{55}$ GST pseudobinaries have intrinsic vacancies because of the imbalance between the number of cations and that of anions. $Sb_{2}Te_{3}$ has antisites as main defects. $^{20}$ Table V shows the measured CP energies for various (GeTe, $Sb_2Te_3$) pseudobinary thin films. Note that GeTe has a very large dielectric constant $(\varepsilon_{\infty}=36)$ and thus the Coulomb interaction between electrons can be strongly screened. Therefore the exciton best match in the spectra of the dielectric function may suggest a deeply localized character of electronic wave functions for the chalcogenides. $^{56}$ This argument can be generalized to other GST compounds. In the case of delocalized wave functions associated with band-to-band transition, the CP can be fitted by one-, two-, or three-dimensional line shape in the SCP model. The coexistence of localization and band-structure aspects in optical spectra was discussed in detail by Toyozawa et al. $^{57}$ One can derive a line shape expression of an optical spectra in which exist the both aspects, namely, the metastable excitons (or quasilocal modes) on the one hand and the Van Hove singularities on the other hand. $^{57}$ Excitons can survive even with increasing disorder associated with AM phase. For example, reflectance spectra of solid and liquid xenon showed that excitons can persist even with the lattice disorder associated with liquid state. $^{58}$

We can also obtain the CP energies of the uniaxial GST compounds from the electronic band structure in Fig. 6. The

![](./images/811832819583025152_11.jpg)

FIG. 11. (Color online) Second derivative spectra of the dielectric functions, $\varepsilon=\varepsilon_{1}+i\varepsilon_{2}=(n+ik)^{2}$ of (a) GeTe, (b) $\text{Ge}_{2}\text{Sb}_{2}\text{Te}_{5}$, (c) $\text{Ge}_{1}\text{Sb}_{2}\text{Te}_{4}$, (d) $\text{Ge}_{1}\text{Sb}_{4}\text{Te}_{7}$, and (e) $\text{Sb}_{2}\text{Te}_{3}$ from Fig. 3. Circular and triangle symbols denote the real and imaginary parts of the second derivative spectra of the dielectric functions, respectively. The lines denote the best-match curves by using the SCP model. We denoted the band-gap energies as $E_{\text{a}}$, $E_{\text{b}}$, $E_{\text{c}}$, $E_{\text{d}}$, and $E_{\text{e}}$ in the order of increasing band-gap energy. The uncertainty was about 0.05 eV with 95% reliabilities.

direct comparison of the measured and the calculated CP energies was difficult because the band structures are very complex except that of GeTe due to the large unit-cell sizes and the thin films were polycrystalline rather than single crystalline. However, the experimental values of the indirect band gap and the CP energy of the polycrystalline phase provide rough estimate of the electronic band structure of the single-crystalline films. In the case of Si, the CP energy values of polycrystalline phase are similar to those of single-crystalline phase. Of course, the CP energy values of the uniaxial GST single crystals differ depending on whether the field direction is along the ordinary or the extraordinary axis.

Critical points can be easily found for GeTe from Fig. 6 of the calculated band structure because of quasi-isotropic crystal structure. We get 0.7, **1.2, 1.7**, 2.0, **2.3, 3.3**, and **3.8 eV** for CP energies, where bold font numbers match well with experimental ones in Fig. 11. Experimentally the measured CP energies are only a subset of calculated ones because the experimental data are a sort of weight-averaged dielectric function of the anisotropic dielectric function. We also found that the experimentally determined the CP energies of other GST compounds are subset of those estimated by the band calculations. They are not shown here because there are so

<table>
<caption>TABLE V. CP energies of (a) amorphous, (b) RS, (c) HEX, and (d) RH phase of (GeTe, Sb₂Te₃) pseudobinary thin film. The uncertainty was about 0.05 eV with 95% reliabilities.</caption>
<thead>
<tr>
<th>Composition</th>
<th>Phase</th>
<th>Eₐ (eV)</th>
<th>Eᵦ (eV)</th>
<th>E<sub>c</sub> (eV)</th>
<th>E<sub>d</sub> (eV)</th>
<th>E<sub>e</sub> (eV)</th>
<th>E<sub>f</sub> (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>GeTe</td>
<td>AM</td>
<td>1.39</td>
<td>3.38</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>RS</td>
<td>1.11</td>
<td>1.56</td>
<td>2.25</td>
<td>3.03</td>
<td>3.70</td>
<td></td>
</tr>
<tr>
<td>Ge₂Sb₂Te₅</td>
<td>AM</td>
<td>1.34</td>
<td>2.84</td>
<td></td>
<td>5.81</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>RS</td>
<td>1.01</td>
<td>1.66</td>
<td>4.64</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>HEX</td>
<td>1.13</td>
<td>1.88</td>
<td>2.32</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ge₁Sb₂Te₄</td>
<td>AM</td>
<td>1.11</td>
<td>1.68</td>
<td>4.56</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>RS</td>
<td>0.86</td>
<td>1.87</td>
<td>4.11</td>
<td>5.44</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>HEX</td>
<td>1.21</td>
<td>1.57</td>
<td>3.22</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ge₁Sb₄Te₇</td>
<td>AM</td>
<td>1.17</td>
<td>1.94</td>
<td>3.79</td>
<td>5.04</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>HEX</td>
<td>0.93</td>
<td>1.45</td>
<td>2.41</td>
<td>3.09</td>
<td>3.35</td>
<td></td>
</tr>
<tr>
<td>Sb₂Te₃</td>
<td>AM</td>
<td>1.27</td>
<td>2.54</td>
<td>3.48</td>
<td>4.38</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>RH</td>
<td>1.09</td>
<td>1.53</td>
<td>1.94</td>
<td>2.57</td>
<td>4.86</td>
<td>5.11</td>
</tr>
</tbody>
</table>

many calculated CP energy values for other GST compounds.

## VI. CONCLUSION

We measured the dielectric functions of (GeTe, Sb₂Te₃) pseudobinary thin films—GeTe, Ge₂Sb₂Te₅, Ge₁Sb₂Te₄, Ge₁Sb₄Te₇, and Sb₂Te₃—by using spectroscopic ellipsometry. In the case of the amorphous thin films, the amplitudes of the complex refractive indexes increased as the Sb-to-Ge atomic ratio increases. In the case of the annealed HEX thin films, the amplitudes of Ge-containing thin films increased significantly compared to those of the amorphous thin films, whereas that of Sb₂Te₃ increased slightly. By using SCP model, we obtained the accurate values of the energy gap of the amorphous phase as well as the CP energies of the crystalline films. These band-gap energy values are compared to those determined by the method of linear extrapolation of the optical absorption. As the Sb-to-Ge atomic ratio increased, the optical gap energy of amorphous phase decreased from 0.8 to 0.52 eV and the indirect band-gap energy of crystalline phase decreased from 0.61 to 0.5 eV. The second derivative spectra of the dielectric functions with SCP model analysis show several higher band gaps. The electronic band structures, dielectric functions, and absorption coefficients of the thin films are calculated by using DFT and are compared to the measured ones. The band-structure calculations show that the crystalline phase of GeTe, Ge₂Sb₂Te₅, and Ge₁Sb₂Te₄ have indirect gap whereas that of Ge₁Sb₄Te₇ and Sb₂Te₃ have direct gap. The experimental CP energies of the pseudobinary compounds, especially GeTe, match well to those of theoretical calculation. The measured indirect band-gap energies are compared to the electronic band-structure calculations. The stable phase of GST compounds has a smaller band gap of 0.13 eV in band-structure calculations, whereas experimental results found smaller band gaps for the metastable phase, i.e., about 0.06 eV. Moreover, experimentally there are large differences between the dielectric functions and absorption coefficients of both the metastable and stable phases in contrast to the predicted small differences of those properties from the DFT calculations. We attributed the discrepancy to the insufficient ordering of vacancies in the real materials of metastable phase. In this work, we studied all three phases (amorphous, metastable, and stable phases) for (GeTe, Sb₂Te₃) pseudobinary compounds. We calculated the full band structures, the band-gap energies, the CP energies, the dielectric functions, and the absorption coefficients, and finally compared those to the experimental data.

## ACKNOWLEDGMENTS

This work was supported by the Korea Science and Engineering Foundation (KOSEF) grant funded by the Korea Government (MOST) (Grant No. R01-2007-000-20142-0). S.H. Eom was supported by the Korea Research Foundation (KRF) funded by the Korean Government (MOEHRD, Basic Research Promotion Fund) under Grant No. KRF-2005-005-J00802. J. W. Park was supported by Graduate School, Kyung Hee University.

*Corresponding author; hlee@khu.ac.kr

¹M. Wuttig and N. Yamada, Nature Mater. 6, 824 (2007).

²T. Ohta, J. Optoelectron. Adv. Mater. 3, 609 (2001).

³J. L. F. Da Silva, A. Walsh, and H. Lee, Phys. Rev. B 78, 224111 (2008).

⁴P. Jóvári, I. Kaban, J. Steiner, B. Beuneu, A. Schóps, and M. A. Webb, Phys. Rev. B 77, 035202 (2008).

⁵Z. Sun, J. Zhou, A. Blomqvist, B. Johansson, and R. Ahuja,

Appl. Phys. Lett. 93, 061913 (2008).

$^{6}$J. Hegedüs and S. R. Elliott, Nature Mater. 7, 399 (2008).

$^{7}$K. Kohary, V. M. Burlakov, and D. G. Pettifor, Phys. Rev. B 71, 235309 (2005).

$^{8}$A. V. Kolobov, P. Fons, A. I. Frenkel, Alexei L. Ankudinov, Junji Tominaga, and Tomoya Uruga, Nature Mater. 3, 703 (2004).

$^{9}$D. A. Baker, M. A. Paesler, G. Lucovsky, S. C. Agarwal, and P. C. Taylor, Phys. Rev. Lett. 96, 255501 (2006).

$^{10}$J. Im, J-H. Eom, C. Park, K. Park, D-S Suh, K. Kim, Y-S Kang, C. Kim, T-Y Lee, Y. Khang, Y-G Yoon, and Jisoon Ihm, Phys. Rev. B 78, 205205 (2008).

$^{11}$S. Kohara, K. Kato, S. Kimura, Hitoshi Tanaka, T. Usuki, K. Suzuya, Hiroshi Tanaka, Y. Moritomo, T. Matsunaga, N. Yamada, Y. Tanaka, H. Suematsu, and M. Takata, Appl. Phys. Lett. 89, 201910 (2006).

$^{12}$M. H. R. Lankhorst, B. W. S. M. M. Ketelaars, and R. A. M. Wolters, Nature Mater. 4, 347 (2005).

$^{13}$D. Ielmini, A. L. Lacaita, and D. Mantegazza, IEEE Trans. Electron Devices 54, 308 (2007).

$^{14}$A. Redaelli, A. Pirovano, A. Benvenuti, and A. L. Lacaita, J. Appl. Phys. 103, 111101 (2008).

$^{15}$B. J. Kooi and J. Th. M. De Hosson, J. Appl. Phys. 92, 3584 (2002).

$^{16}$T. Nonaka, G. Ohbayashi, Y. Toriumi, Y. Mori, and H. Hashimoto, Thin Solid Films 370, 258 (2000).

$^{17}$J. Yu, B. Liu, T. Zhang, Z. Song, S. Feng, and B. Chen, Appl. Surf. Sci. 253, 6125 (2007).

$^{18}$N. Yamada, E. Ohno, K. Nishiuchi, N. Akira, and M. Takao, J. Appl. Phys. 69, 2849 (1991).

$^{19}$T. Matsunaga, N. Yamada, and Y. Kubota, Acta Crystallogr., Sect. B: Struct. Sci. 60, 685 (2004).

$^{20}$T. Thonhauser, G. S. Jeon, G. D. Mahan, and J. O. Sofo, Phys. Rev. B 68, 205207 (2003).

$^{21}$V. Weidenhof, I. Friedrich, S. Ziegler, and M. Wuttig, J. Appl. Phys. 86, 5879 (1999).

$^{22}$A. Pirovano, A. L. Lacaita, A. Benvenuti, F. Pellizzer, and R. Bez, IEEE Trans. Electron Devices 51, 452 (2004).

$^{23}$W. Wełnic, S. Botti, L. Reining, and M. Wuttig, Phys. Rev. Lett. 98, 236403 (2007).

$^{24}$B. S. Lee, J. R. Abelson, S. G. Bishop, D. H. Kang, B. K. Cheong, and K. B. Kim, J. Appl. Phys. 97, 093509 (2005).

$^{25}$E. García-García, A. Mendoza-Galván, Y. Vorobiev, E. Morales-Sánchez, J. González-Hernandez, G. Martínez, and B. S. Chao, J. Vac. Sci. Technol. A 17, 1805 (1999).

$^{26}$J.-W. Park, S. H. Baek, T. D. Kang, H. Lee, Y.-S. Kang, T.-Y. Lee, D.-S. Suk, K. J. Kim, C. K. Kim, Y. H. Khang, J. L. F. Da Silva, and S.-H. Wei, Appl. Phys. Lett. 93, 021914 (2008).

$^{27}$K. Shportko, S. Kremers, M. Woda, D. Lencer, J. Robertson, and M. Wuttig, Nature Mater. 7, 653 (2008), and reference therein.

$^{28}$D. Lencer, M. Salinger, B. Grabowski, T. Hickel, J. Neugebauer, and M. Wuttig, Nature Mater. 7, 972 (2008).

$^{29}$P. Lautenschlager, M. Garriga, L. Viña, and M. Cardona, Phys. Rev. B 36, 4821 (1987).

$^{30}$I. Friedrich, V. Weidenhof, W. Njoroge, P. Franz, and M. Wuttig, J. Appl. Phys. 87, 4130 (2000).

$^{31}$R. Schmidt-Grund, A. Carstens, B. Rheinländer, D. Spemann, H. Hochmut, G. Zimmermann, M. Lorenz, M. Grundman, C. M. Herzinger, and M. Schubert, J. Appl. Phys. 99, 123701 (2006).

$^{32}$B. Johs, C. M. Herzinger, J. H. Dinan, A. Cornfeld, and J. D. Benson, Thin Solid Films 313-314, 137 (1998).

$^{33}$J. Orava, T. Wágner, J. Šik, J. Příkryl, M. Frumer, and L. Beneš, J. Appl. Phys. 104, 043523 (2008).

$^{34}$D. E. Aspnes and A. A. Studna, Phys. Rev. B 27, 985 (1983).

$^{35}$T. Kato and K. Tanaka, Jpn. J. Appl. Phys., Part 1 44, 7340 (2005).

$^{36}$P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

$^{37}$G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

$^{38}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

$^{39}$G. Kresse and J. Hafner, Phys. Rev. B 48, 13115 (1993).

$^{40}$G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

$^{41}$T. Matsunaga and N. Yamada, Phys. Rev. B 69, 104111 (2004).

$^{42}$P. Villars and L. D. Calvert, *Persons's Handbook of Crystallographic Data for Intermetallic Phases* (ASM International, Materials Park, OH, 1991).

$^{43}$J. L. F. Da Silva, A. Walsh, S. H. Wei, and H. Lee (unpublished).

$^{44}$J. Akola and R. O. Jones, Phys. Rev. B 76, 235201 (2007).

$^{45}$S. Caravati, M. Bernasconi, T. D. Kühne, M. Krack, and M. Parrinello, Appl. Phys. Lett. 91, 171906 (2007).

$^{46}$J. K. Olson, H. Li, T. Ju, J. M. Viner, and P. C. Taylor, J. Appl. Phys. 99, 103508 (2006).

$^{47}$S. Yamanaka, S. Ogawa, I. Morimoto, and Y. Ueshima, Jpn. J. Appl. Phys., Part 1 37, 3327 (1998).

$^{48}$D. Lee, S. S. Lee, W. Kim, C. Hwang, M. B. Hossain, N. L. Hung, H. Kim, C. G. Kim, H. Lee, H. N. Hwang, and C.-C. Hwang, Appl. Phys. Lett. 91, 251901 (2007).

$^{49}$B. Adolph, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 63, 125108 (2001).

$^{50}$M. Gajdős, K. Hummer, G. Kresse, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 73, 045112 (2006).

$^{51}$M. Rakel, C. Cobet, N. Esser, F. Fuchs, F. Bechstedt, R. Goldhahn, W. G. Schmidt, and W. Schaff, Phys. Rev. B 77, 115120 (2008).

$^{52}$P. Y. Yu and M. Cardona, *Fundamentals of Semiconductors* (Spinger-Verlag, Berlin, 2005).

$^{53}$D. Segev and S.-H. Wei, Phys. Rev. B 71, 125129 (2005).

$^{54}$M. Campoy-Quiles, J. Nelson, D. D. C. Bradly, and P. G. Etchegoin, Phys. Rev. B 76, 235206 (2007).

$^{55}$A. H. Edwards, A. C. Pineda, P. A. Schultz, M. G. Martin, A. P. Thompson, H. P. Hjalmarson, and C. J. Umrigar, Phys. Rev. B 73, 045210 (2006).

$^{56}$P.-J. Lin, W. Saslow, and M. L. Cohen, Solid State Commun. 5, 893 (1967).

$^{57}$Y. Toyozawa, M. Inoue, T. Inui, M. Okazaki, and E. Hanamura, J. Phys. Soc. Jpn. 22, 1337 (1967).

$^{58}$D. Beaglehole, Phys. Rev. Lett. 15, 551 (1965).