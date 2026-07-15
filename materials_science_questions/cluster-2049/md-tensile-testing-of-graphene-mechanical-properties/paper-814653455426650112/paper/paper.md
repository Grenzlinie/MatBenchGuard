# Band Gaps of BN-Doped Graphene: Fluctuations, Trends and Bounds
Regiane Nascimento, Jonathan da Rocha Martins, Ronaldo Junio Campos Batista, and Helio Chacham

J. Phys. Chem. C, Just Accepted Manuscript • DOI: 10.1021/jp5101347 • Publication Date (Web): 16 Feb 2015

Downloaded from http://pubs.acs.org on February 18, 2015

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a free service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are accessible to all readers and citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/814653455426650112_1.jpg)

The Journal of Physical Chemistry C is published by the American Chemical Society.
1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Band Gaps of BN-doped Graphene: Fluctuations, Trends and Bounds

Regiane Nascimento,† Jonathan da Rocha Martins,‡ Ronaldo J. C. Batista,¶
and Hélio Chacham*,†

Departamento de Física, ICEX, Universidade Federal de Minas Gerais, CP 702,
30123-970, Belo Horizonte, MG, Brazil, Departamento de Física, Universidade Federal do
Piauí, Campus Ministro Petrônio Portela- Bairro Ininga, 64049-550, Teresina, PI, Brazil,
and Departamento de Física, Universidade Federal de Ouro Preto, Campus Morro do
Cruzeiro, 35400-000, Ouro Preto, MG, Brazil

E-mail: chacham@fisica.ufmg.br

---

*To whom correspondence should be addressed
†Universidade Federal de Minas Gerais
‡Universidade Federal do Piauí
¶Universidade Federal de Ouro Preto

**ABSTRACT**

A Monte Carlo based simulated annealing process combined with *ab initio* calculations are employed to investigate electronic and structural properties of boron nitride (BN) doped graphene, in a wide doping range. We find that, for a given BN doping concentration, the doping-induced band gap can vary over an order of magnitude depending on the placement of the B and N atoms. We propose an analytical tight-binding model that reproduces the dependence of the band gap on both the concentration and the morphology obtained in the *ab initio* calculations, and provides an upper bound for the band gap at a given BN concentration. We also predict that the dependence of the band gap with applied tensile stress should be strong, non-monotonic, and anisotropic, within the range of strain values attainable experimentally.

**KEYWORD:** graphene; B-C-N; electronic properties; band gap; stress

## 1 INTRODUCTION

Since the discovery of graphene in $2004^1$ the interest in 2D materials has grown continuously. Hexagonal boron nitride (h-BN)$^2$ and phosphorene$^3$ are examples of 2D materials that, like graphene, present scientific and technological appeal. Boron and nitrogen doped graphene,$^{4-6}$ as well as BN co-doped graphene have also been investigated.$^{5-10}$ Unlike the pristine 2D materials, gr:BN - a solid solution with B and N atoms substituting carbon atoms in graphene at the same concentration - does not have a unique chemical composition and morphology. As a result, its electronic properties can be tuned by changing the growing conditions in which gr:BN layers are formed.$^{11}$ The band gaps of gr:BN structures vary over a wide range,$^{12}$ from graphene's zero value up the 5.5 eV band gap of hexagonal boron nitride,$^2$ which may lead to applications in opto-electronics. In particular, a semiconductor material with the high carrier mobility and the low contact resistance characteristic of graphene could provide the modulation necessary to produce efficient devices, which cannot be based only on single-layer graphene due its zero band gap.

The concentrations of B and N atoms are variables that can be controlled during gr:BN growth. Due to the high energy cost of C-N and C-B bonds as compared to that of a B-N bond,¹³ B and N atoms tend to form BN pairs in stable gr:BN structures.¹⁴,¹⁵ However, it is also possible to produce gr:BN structures in which B and N atoms are placed apart as isolated impurities.¹¹,¹⁶ For large BN concentrations, an inhomogeneous lattice tends to be formed due to BN segregation, that is, the B and N atoms segregate from graphene to form BN regions within the graphene lattice.⁸,¹⁵ There are several theoretical and experimental studies involving the combination of graphene and hexagonal boron nitride.⁹,¹⁷⁻¹⁹ The dependence of the band gap with the BN concentration and gr:BN morphology is not yet fully understood. Experimental results show a non-monotonic dependence of the band gap with the BN concentration,⁸,²⁰,²¹ indicating that the band gaps may depend on morphological characteristics other than just the BN concentration. For instance, recent experimental studies by Chang et al²⁰ indicate the opening of a band gap in graphene of 0.6 eV when doped with 6% BN, while Ci et al²¹ measured a much smaller gap of 18 meV at a much higher BN concentration of 44%.

In the present work we employ a bond-energy model¹³,¹⁴ to obtain, through a simulated annealing process, gr:BN layers with BN concentrations varying from 2.08% up to 10.42%. Then, we employ first principles calculations based on density functional theory to investigate the electronic structure of gr:BN layers with different morphologies for each BN concentration. We find that the band gaps of gr:BN can vary by up to an order of magnitude for a given BN concentration, depending on the specific morphology of the gr:BN layer. We propose an analytical model that explains the observed dependence of band gap with the morphology in terms of the occupation of graphene non-equivalent sublattices by N and B atoms. We also address the effects of applied stress on the band gaps of gr:BN layers.

## 2 THEORETICAL METHODS

In order to obtain the low energy gr:BN structures for the electronic structure calculations we performed a configurational optimization of randomly generated gr:BN structures through an simulated annealing procedure.¹⁴ The simulation starts with a configuration where we arbitrarily select the B, C or N atoms for each site with equal probability. We then proceed to a configurational optimization through a Monte Carlo algorithm. In the first iteration, at an initial temperature $T_0$, we randomly select first-neighbor atoms in the unit cell and exchange these atoms with probability proportional to the Boltzmann factor $e^{-\frac{\Delta E}{k_B T}}$, where $\Delta E$ is the difference between the system total energy after and before the configurational modification. We set the initial temperature as $T_0 = 11600\ K$, which allows for a high degree of C, B and N positional disorder in the initial cell. The atomic positions are fixed and are not considered as degrees of freedom in our simulations. The temperature decreases linearly with the Monte Carlo steps, $(T_i = T_0(\frac{max-i}{max}))$; where $max$ is the maximum number $i$ of iterations. The annealing process continues until the temperature reaches a value which is small enough so as to make negligible the exchange probability. The total energy is obtained from a bond-energy model,¹³

$$
E_{total}^{i} = \sum_{\alpha\beta} n_{\alpha\beta}^{i} \epsilon_{\alpha\beta}^{i}, \tag{1}
$$

where $i$ is the configuration label, $\alpha, \beta = \text{C,B,N}$ and $n_{\alpha\beta}^{i}$ is the number of $\alpha\beta$ bonds in the configuration. The bond energy $\epsilon_{\alpha\beta}$ values are parameterized according to ab initio calculations. The parametrization procedure is described in detail in Ref. 13. The parameters $\epsilon_{CC}$ and $\epsilon_{BN}$ are obtained from ab initio calculations of graphene and h-BN, respectively. The remaining parameters are obtained by least-square fitting to the ab initio total energies of several $\text{B}_x\text{C}_y\text{N}_z$ structures, as described in Ref. 13.

With this methodology, we can obtain low energy B-C-N configurations. Geometry optimization and electronic structure calculations were carried out using the SIESTA²²,²³ code,

which implements the density functional theory (DFT).$^{24}$ We used the generalized gradient approximation (GGA)$^{25}$ for the exchange-correlation potential and a double-$\zeta$ plus polarization (DZP) basis set to expand the electronic wavefunctions. The real-space grid was defined by a 200 Ry energy cutoff. All geometries were optimized until the force on each atom was less than 0.025 eV/Ang. We used $c$-axis vector with a of $20$ $\text{\AA}$ modulus, perpendicular to $\text{B}_x\text{C}_y\text{N}_x$ plane, to avoid interaction between layers. Finally, we used a $55 \times 55 \times 1$ Monkhorst-Pack grid for integrations over the Brillouin zone.

## 3 RESULTS AND DISCUSSION

### 3.1. Structural Properties
To simulate the atomic configurations of gr:BN layers, we consider periodic cells with 96-atoms in a honeycomb lattice where the positions of the B, C, and N atoms - at fixed numbers - are obtained by means of the simulated annealing Monte Carlo procedure$^{14}$ described in the Methods section. For each BN concentration (from 2.08 up to 10.42%) we consider eight $\text{B}_x\text{C}_y\text{N}_x$ structures with different morphologies. As an example, Figure 1 shows the geometries of gr:BN layers with 10.42% BN concentration. We have also performed calculations with larger supercells containing 384 atoms. Four supercells have been considered at two concentrations, 4.17% and 10.42%. For each concentration, two distinct configurations are considered. These are shown in Figures 3 and 4, respectively. It is worth to say that except for the geometries of Figures 3b and 4b (built to investigate the effect of segregation to larger islands), we did not impose specific geometric shapes for the islands. Rather, the geometries resulted from the Monte Carlo simulated annealing method.$^{14}$

### 3.2. Electronic Properties
The introduction of BN dimers in graphene modulates its band gap, as it can be seen in Figures 2 and 5. Figure 2 shows the electronic structure of both pristine graphene and the gr:BN layer of Figure 1f. Figure 5c shows the electronic structure of the gr:BN layer of Figure 3a. These two structures, as well as that of Figure 3b,

![](./images/814653455426650112_2.jpg)

Figure 1: Low energy $B_5C_{86}N_5$ structures generated by the simulated annealing Monte Carlo procedure. $^{14}$

have the same BN concentration of 10.42%, but different band gaps. The band gaps of the structures shown in Figures 3a and 3b are 175 and 144 meV, respectively, while the band gap of the configuration shown in Figure 1f is 313 meV. For the supercells with 384 atoms and 4.17% BN concentration (Figures 4a and 4b) the band gaps are 64 and 74 meV, respectively. As a comparison, the experimental value reported by Chang et $al^{20}$ for the band gap of BN-doped graphene with 6% of BN pair concentration is 600 meV. We should mention that DFT calculations with local or semilocal approximations for the exchange-correlation functional (such as GGA) underestimate the calculated band gaps relative to both experimental results and GW quasiparticle calculations. $^{26}$

The local density of states (LDOS) at the band edges of the structure shown in Figure 3a is depicted in Figure 5. Figure 5a shows the probability density associated to states near the top of the highest valence band, and Figure 5b shows the probability density associated to states near the minimum of the lowest conduction band . In both cases, the band edge states are predominantly located at graphene regions nearby BN islands, as well as at edge atoms of those islands.

Let us now investigate the effect of the gr:BN morphology in the band gap values. We

![](./images/814653455426650112_3.jpg)

Figure 2: (a) Electronic structure of pristine graphene, considering a 96-atom unit cell; (b) Electronic structure of the $B_5C_{86}N_5$ structure shown in Figure 1f. The inset in panel (a) shows the path in the Brillouin zone in which energy eigenvalues were calculated.

![](./images/814653455426650112_4.jpg)

Figure 3: Two distinct configurations for a 384-atoms supercell of $B_{20}C_{344}N_{20}$ (10.42% BN concentration).

![](./images/814653455426650112_5.jpg)

Figure 4: Two distinct configurations for a 384-atoms supercell of $B_8C_{368}N_8$ (4.17% BN concentration).

![](./images/814653455426650112_6.jpg)

Figure 5: LDOS of the $B_{20}C_{344}N_{20}$ structure of Figure 3.(a): valence band maximum, (b): conduction band minimum. (c) Electronic structure of this supercell, presenting a band gap of 175 meV.

calculated band gaps of 38 gr:BN structures, with BN concentrations ranging from 2% to more than 10%. The calculated band gaps vary from less than 0.02 eV to more than 0.3 eV, as seen in Figure 6. We found large variations in the band gap values for each BN concentration. For structures with 10.42% of BN, for instance, the calculated band gaps vary from 99.6 to 313.1 meV. This demonstrates that morphology plays an important role in the band gaps of gr:BN. Another interesting feature of our results, also seen in Figure 6, is a clear trend of increasing band gap with BN concentration. This trend is predicted by an analytical tight-binding model discussed below. The comparison between model and

calculations indicates that the model provides an upper bound for the calculated band gaps.

Let us now proceed to describe such model.

### 3.3. The Virtual Crystal Model - Let us consider an infinite gr:BN structure, with
B, C, and N atoms at the honeycomb lattice sites. We will also consider that: (i) the concentration of B and N atoms is the same, such that we can define a BN concentration, $c_{BN}$; (ii) the B and N atoms might have different concentrations on each sublattice - 1 or 2 - of the honeycomb lattice, such that $p$ is the conditioned probability that a boron atom occupies a site in the sublattice 1 and not 2, and $(1-p)$, vice-versa.

Let us now consider a tight-binding hamiltonian with one $p_z$ orbital per site in that structure. For simplicity, we will only consider first-neighbor hopping matrix elements $t$ and on-site terms $\varepsilon_C$, $\varepsilon_B$, and $\varepsilon_N$ at C, B, and N sites, respectively. Let us now apply the virtual crystal approximation to this hamiltonian, that is, the on-site terms $\varepsilon_1$ and $\varepsilon_2$ of the effective hamiltonian on a given sublattice (1 or 2) will be given by the average values of all on-site terms of the tight-binding hamiltonian on that sublattice. We obtain

$$
\begin{cases}
\varepsilon_1 = (1 - c_{BN})\varepsilon_C + c_{BN} \left[ p\ \varepsilon_B + (1-p)\varepsilon_N \right] \\
\varepsilon_2 = (1 - c_{BN})\varepsilon_C + c_{BN} \left[(1-p)\varepsilon_B + p\ \varepsilon_N\right],
\end{cases} \tag{2}
$$

and the band gap is given by

$$
E_{gap} = |\varepsilon_1 - \varepsilon_2| = E_{gap}^{BN} c_{BN} |2p - 1|, \tag{3}
$$

where $E_{gap}^{BN} = \varepsilon_N - \varepsilon_B$ is the energy gap of pristine BN. Therefore, according to the model (i.e., from Eq. 3), the band gap depends on two distinct characteristics of gr:BN : the BN concentration $c_{BN}$ and the B-N asymmetry in the sublattice occupation. In the first case, the band gap is simply linear with $c_{BN}$. In the second case, the gap is linear with $|p - 1/2|$. That is, for a nearly symmetric occupation of sublattices 1 and 2 by B and N atoms ($p$ near 1/2) the gap vanishes, and for maximum asymmetry ($p$ near either unity or zero) the band gap

is maximum. For consistency between model and DFT calculations, we have set $E_{gap}^{BN}=4.5$ eV, our calculated DFT value. This is equivalent to parametrize $\varepsilon_N - \varepsilon_B$ by the same value in the tight-binding hamiltonian. The maximum $E_{gap}$ value from Eq. 3, $E_{gap}=E_{gap}^{BN}c_{BN}$, is a good estimate for the upper bound of band gaps in gr:BN. This is seen in Figure 6, as a the green dashed line. Figure 6 also shows the average value of the calculated band gaps at each concentration, and a linear fit to these average values. The slope of this linear fit, 1.8 eV, is approximately $39\%$ of $E_{gap}^{BN}$.

![](./images/814653455426650112_7.jpg)

Figure 6: Red dots: Calculated energy gaps of BN-doped graphene with BN concentration less than 11%. Blue dots: average values for each concentration with error bars from standard deviation values. Green dashed line: upper limit of Eq. 3. Dotted black line: linear fit to blue dots.

Our results for the band gaps of BN co-doped graphene, shown in Figure 6, are consistent with previous theoretical results $^{6,8}$ for the band gaps of graphene with low BN co-doping ($c_{BN}<13\%$). In Ref. 8, three such band gaps have been reported: 0.39 eV and 0.27 eV for two distinct structures with $c_{BN}=0.125$, and 0.13 eV or a structure with $c_{BN}=0.047$. In all cases the ratio $E_{gap}/c_{BN}$ is less than 3.5 eV. This is not only consistent with our DFT results, but also with the predictions of the virtual crystal model described above. In Ref. 6, the calculated onset for optical absorption also results in $E_{onset}/c_{BN}$ being less than 3.5 eV. We shall mention that the mean field description given by the virtual crystal model is

best applied to small BN islands, low-concentration limit. For larger BN concentrations and larger island sizes, both the quantum confinement effect at the graphene islands and edge effects such as those from zigzag boundaries might cause deviations from our mean field approach.

Let us consider for a moment that the virtual crystal model contains the physical basis for the origin of the band gaps of gr:BN at low concentration. This is not unreasonable to assume in view of the good agreement between model and DFT calculations seen in Figure 6. If so, where would we find the B-N asymmetry in the sublattice occupation, which, according to the model, is the origin of the band gap? Such asymmetry does not exist in the thermodynamic limit, that is, for the infinite crystal, unless there is a bias to the occupation of sites 1 or 2 by B and N atoms, which is not the present case. A possible answer to this apparent puzzle can be seen in the local density of states (LDOS) of band edges states, shown in Figure 5. As previously mentioned, the figure shows that both the conduction and valence band edge states are localized near BN islands. This suggests that the relevant occupation asymmetry is not that of the whole, infinite 2D material, but that in regions near the probability density maxima of the band edge states. In fact, there is a strong occupation asymmetry in such regions in Figure 5, originating from the alternate occupation of B and N atoms in the BN islands.

Let us also mention that, besides the local occupation asymmetry near BN islands, there is also an intrinsic local asymmetry originating from statistical fluctuations. In that case, there would be a probability distribution $P(p)$ of $p$ values, centered at $p=1/2$ and with a standard deviation $\sigma$ scaling as $1/\sqrt{N}$, where $N$ is the number of sites of the region. Supposing a gaussian distribution, Eq. 3 leads to

$$
\left\langle E_{g}\right\rangle=2 E_{g a p}^{B N} c_{B N} \frac{\int_{0}^{1 / 2} x e^{-(x)^{2} / \sigma^{2}} d x}{\int_{0}^{1 / 2} e^{-(x)^{2} / \sigma^{2}} d x}, \tag{4}
$$

which integrates to

$$
\frac{\langle E_{g}\rangle}{E_{gap}^{BN}c_{BN}}=\frac{2\sigma}{\sqrt{\pi}}\frac{1 - e^{-\frac{1}{4\sigma^{2}}}}{erf\left(\frac{1}{2\sigma}\right)}.\tag{5}
$$

As the number of sites of the region, $N$, tends to infinity, $\sigma$ tends to zero and Eq. 5 leads to a zero-gap value, as expected. For finite values of $\sigma$ the gap is non-zero, with an asymptote $\frac{\langle E_{g}\rangle}{E_{gap}^{BN}c_{BN}}=1/2$ for large $\sigma$. Therefore, the statistical fluctuation effect, although able to produce finite $E_{gap}$ values, is not enough to account for the calculated values. Still regarding occupation asymmetry, we should mention that it is experimentally possible to obtain such asymmetry. Khosousi et $al^{16}$ observed by STM measurements that nitrogen doped graphene under single-crystal Cu(111) substrates presents well-separated domains where nitrogen occupies the same sublattice. This is observed only in samples grown by CVD, for other methods of nitrogen doping occur at random distributions of sublattices.

3.4. Strain Effects - Deformations of the graphene lattice due to external tension can occur either naturally - when graphene is deposited on a substrate - or as a result of an applied stress. $^{27}$ Regarding B-C-N materials, recent experiments $^{28}$ have reported strong electromechanical responses of B-C-N nanotubes to torsion. Therefore, it is relevant to investigate how the strain would affect the gr:BN electronic structure, particularly the band gap. To investigate such an effect we have considered the application of uniaxial tensile stress to two distinct gr:BN structures, namely those of Figure 1f and Figure 1b. Such structures were subjected to uniaxial stress, with tensions up to 31.8 N/m and 36.0 N/m, respectively applied along the armchair and the zigzag directions. For larger values of tension, instability and collapse of the lattice was observed.

Figure 7 shows the calculated stress-strain relation for the gr:BN cell in Figure 1f. Up to second order in the strain $\varepsilon$, one obtains $^{27}$

$$
\sigma=C\varepsilon+D\varepsilon^{2},\tag{6}
$$

where $\sigma$ is the 2D stress, $C$ is the in-plane stiffness, and $D$ is the third-order elastic modulus.

Fitting Eq. 6 to our DFT results for 10.42% BN concentration leads to $C = 322$ N/m for the zigzag direction and $C = 338$ N/m for the armchair direction, respectively, as shown in Figure 7. These results may be compared to the experimental value of 309 N/m for a gr:BN sample with 2% BN concentration, $^{29}$ and to experimental $(340 \pm 50$ N/m$^{27})$ and theoretical $(347.2$ N/m$^{30})$ values for pristine graphene.

Figures 8 and 9 show the calculated band gaps of the structures shown in Figure 1f and Figure 1b, respectively, when subjected to uniaxial stress along the armchair and zigzag directions. As it can be seen in Figures 8 and 9, the band gap presents non-monotonic behavior with increasing strain along both directions. The dependence of the band gap with uniaxial strain is anisotropic for both small and large strain values, with the derivative of the gap with respect to strain presenting opposite signs for each direction. The effects are, however, opposite regarding the strain orientation for configurations 1f and 1b. In Figure 8, at values of strain of about 0.04, a minimum and a maximum band gap are observed for deformations along the armchair and the zigzag directions, respectively. In contrast, in Figure 9, a maximum band gap occurs at values of strain of about 0.02 along the armchair direction and a minimum at strain of about 0.04 along the zigzag direction. In both structures, the strain induced effect on the band gap is very large - up to $\sim 50\%$ in Figure 8, and up to $\sim 20\%$ in Figure 9.

Figure 10 shows the band structures of the structure of Figure 1f when subjected to uniaxial stress, along to zigzag direction. Interestingly, we find that not only the band gap values change with strain, but also the position of the band extrema in the reciprocal space.

We shall mention another effect related to the application of strain to polar materials such as BN is piezoelectricity$^{31-33}$. The piezoelectric effect, consisting on the dependence of polarization in the local strain, should be more evident for large BN domains.

![](./images/814653455426650112_8.jpg)

Figure 7: Calculated stress-strain relation of the structure shown in Figure 1f when subjected to uniaxial stress along the armchair and zigzag directions. The dashed blue and red lines are fits to Eq. 6.

![](./images/814653455426650112_9.jpg)

Figure 8: Calculated band gap of the structure shown in Figure 1f when subjected to uniaxial stress along the armchair and zigzag directions.

![](./images/814653455426650112_10.jpg)

Figure 9: Calculated band gap of the structure shown in Figure 1b when subjected to uniaxial stress along the armchair and zigzag directions.

![](./images/814653455426650112_11.jpg)

Figure 10: Band structures of the cell shown in Figure 1f when subjected to uniaxial stress along the zigzag direction. The corresponding strain values, s, are indicated on each panel.

## 4 CONCLUSIONS

We employed a bond-energy model¹³,¹⁴ to obtain, through a simulated annealing process, gr:BN structures with BN concentrations varying from 2.08 up to 10.42%. We also employed

first principles calculations, based on density functional theory, to investigate the electronic structure of gr:BN layers at several BN concentrations, with different morphologies for each concentration. We find that the band gaps of gr:BN can vary by up to an order of magnitude for a given BN concentration, depending on the specific morphology of the gr:BN layer. We propose an analytical model that explains the observed dependence of band gap with the morphology in terms of the occupation of graphene non-equivalent sublattices by N and B atoms. We also address the effects of applied stress on the band gap of gr:BN layers. Our results show a non-monotonic and anisotropic dependence of the band gap with applied uniaxial stress.

## ACKNOWLEDGEMENT

We acknowledge support from the Brazilian agencies CNPq, FAPEMIG, CAPES, and the project INCT de Nanomateriais de Carbono.

## REFERENCES

(1) Geim, A. K.; Novoselov, K. S. The rise of graphene. *Nature Mat.* **2007**, *6*, 183-191.

(2) Song, L.; Ci, L.; Lu, H.; Sorokin, P. B.; Jin, C.; Ni, J.; Kvashnin, A. G.; Kvashnin, D. G.; Lou, J.; Yakobson, B. I.; Ajayan, P. M. Large Scale Growth and Characterization of Atomic Hexagonal Boron Nitride Layers. *Nano lett.* **2013**, *10*, 3209-3215.

(3) Liu, H.; Neal, A. T.; Zhu, Z.; Luo, Z.; Xu, X.; Tománek, D.; Ye, P. D. Phosphorene: An Unexplored 2D Semiconductor with a High Hole Mobil- ity. *ACS Nano* **2014**, *8*, 4033-4041.

(4) Rani, P.; Jindal, V. K. Designing band gap of graphene by B and N dopant atoms. *RSC Advances* **2013**, *3*, 802-812.

(5) Fan, X.; Shen, Z.; Liu, A. Q.; Kuo, J. L. Band gap opening of graphene by doping small boron nitride domains. *Nanoscale* **2012**, *4*, 2157-2165.

(6) Rani, P.; Dubey, G. S.; Jindal, V. K. DFT study of optical properties of pure and doped graphene. *Physica E* **2014**, *62*, 28-35.

(7) Mukherjee, S.; Kaloni, T.P. Electronic properties of boron-and nitrogen-doped graphene: a first principles study. *J. Nanopart. Res.* **2012**, *14*, 1-5.

(8) Muchharla, B.; Pathak, A.; Liu, Z.; Song, L.; Jayasekera, T.; Kar, S.; Vaj-tai, R.; Balicas, L.; Ajayan, P. M.; Talapatra, S. *et al.* Tunable Electronics in Large Area Atomic Layers of Boron-Nitrogen-Carbon. *Nano lett.* **2013**, *13*, 3476-3481.

(9) Shinde, P. P.; Kumar, V. Direct band gap opening in graphene by BN doping: Ab initio calculations. *Phys. Rev. B* **2011**, *84*, 125401.

(10) Sen, D.; Thapa, R.; Chattopadhyay, K. K. Rules of Boron-Nitrogen Dop-ing in Defect Graphene Sheets: A First-Principles Investigation of Band-Gap Tuning and Oxygen Reduction Reaction Catalysis Capabilities. *Chem. Phys. Chem.* **2014**, *15*, 2542-2549.

(11) Jin, J.; Pan, F.; Jiang, L.; Fu, X.; Liang, A.; Wei, Z.; Zhang, J.; Sun, G. Catalyst-Free Synthesis of Crumpled Born and Nitrogen Co-Doped Graphite Layers with Tunable Bond Structure for Oxygen Reduction Re-action. *ACS Nano* **2014**, *8*, 3313-3321.

(12) Radisav, S. K.; Zeljko, S. Atomic Structure, Electronic Properties and Reactivity of In-Plane Heterostructures of Graphene and Hexagonal Boron Nitride. *J. Phys. Chem. C* **2014**, *118*, 16104-16112.

(13) Mazzoni, M. S. C.; Nunes, R. W.; Azevedo, S.; Chacham, H. Electronic structure and energetics of $\text{B}_x\text{C}_y\text{N}_z$ layered structures. *Phys. Rev. B* **2006**, 73, 073108.

(14) da Rocha Martins, J.; Chacham, H. Disorder and Segregation in B- C- N Graphene-Type Layers and Nanotubes: Tuning the Band Gap. *ACS Nano* **2010**, 5, 385-393.

(15) da Rocha Martins, J.; Chacham, H. N-rich gr:BN layers: From segregated alloy to solid solution. *Phys. Rev. B* **2012**, 86, 075421.

(16) Khosousi, Z. A.; Zhao, L.; Pálová, L.; Hybertsen, M. S.; Reichman, D. R.; Pasupathy, A. N.; Flynn, G. W. Segregation of Sublattice Domains in Nitrogen-Doped Graphene. *J. Am. Chem. Soc.* **2014**, 136, 1391-1397.

(17) Raidongia, K.; Nag, A.; Hembram, K. P. S. S.; Waghmare, U. V.; Datta, R.; Rao, C. N. R. gr:BN: A graphene analogue with remarkable adsorptive properties. *Chem.- Eur. J.* **2010**, 16, 149-157.

(18) Fan, X.; Shen, Z.; Liu, A. Q.; Kuo, Jer-Lai. Band gap opening of graphene by doping small boron nitride domains. *Nanoscale* **2012**, 4, 2157-2165.

(19) Gao, Y.; Zhang, Y.; Chen, P.; Li, Y.; Liu, M.; Gao, T.; Ma, D.; Chen, Y.; Cheng, Z.; Qiu, X. *et al.* Towards Single-layer Uniform Hexagonal Boron Nitride-Graphene Patchworks with Zigzag Linking Edges. *Nano Lett.* **2013**, 13, 3439-3443.

(20) Chang, C. K.; Kataria, S.; Kuo, C. C.; Ganguly, A.; Wang, B. Y.; Hwang, J. Y.; Huang, K. J.; Yang, W. H.; Wang, S. B.; Chuang, C. H. *et al.* Band Gap Engineering of Chemical Vapor Deposited Graphene by in Situ BN Doping. *ACS Nano* **2013**, 7, 1333-1341.

(21) Ci, L.; Song, L.; Jin, C.; Jariwala, D.; Wu, D.; Li, Y.; Srivastava, A.; Wang, Z. F.; Storr, K.; Balicas, L. *et al.* Atomic layers of hybridized boron nitride and graphene domains. *Nature Mat.* **2010**, *9*, 430-435.

(22) Soler, J. M.; Artacho, E.; Gale, J. D.; García, A.; Junquera, J.; Ordejón, P.; Sánchez-Portal, D. The SIESTA Method for *ab initio* Order-N Materials Simulation. *J. Phys. Condens. Matter* **2002**, *14*, 2745-2779.

(23) Sánchez-Portal, D.; Ordejón, P.; Soler, J. M.; Artacho, E. Density- Functional Method for Very Large Systems With LCAO Basis Set. *Int. J. Quantum Chem.* **1997**, *65*, 453-461.

(24) Kohn, W.; Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Phys. Rev.* **1965**, *140*, A1133-A1138.

(25) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approxima- tion Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865-3868.

(26) Onida, G.; Reining, L.; Rubio, A. Electronic excitations: density-functional versus many-body Green's-function approaches. *Rev. Mod. Phys.* **2002**, *76*, 601.

(27) Lee, C.; Wei, X.; Kysar, J. W.; Hone, J. Measurement of the Elastic Prop- erties and Intrinsic Strength of Monolayer Graphene. *Science* **2008**, *321*, 385-388.

(28) Garel, J.; Zhao, C.; Popovitz-Biro R.; Golberg, D.; Wang, W.; Josele- vich, E. BCN Nanotubes as Highly Sensitive Torsional Electromechanical Transducers. *Nano Lett.* **2014**, *14*, 6132-6137.

(29) Pan, S. H.;Medina, H.; Wang, S. B.; Chou, L. J.; Wang, Z. M.; Chen, K. H.; Chen, L. C.; Chueh, Y. L. Direct assessment of the mechanical

modulus of graphene co-doped with low concentrations of boron-nitrogen by a non-contact approach. *Nanoscale* **2014**, *6*, 8635-8641.

(30) Peng, Q.; Zamiri, A.; Ji, W.; De, S. Elastic properties of hybrid graphene/boron nitride monolayer. *Acta Mech.* **2012**, *223*, 2591-2596.

(31) Shimada, K.; Sota, T.; Suzuki, K.; Okumura, H. First-Principles Study on Piezoelectric Constants in Strained BN, AlN, and GaN. *Jpn. J. Appl. Phys.* **1998**, *37*, 1421-1423.

(32) Sai, N.; Mele, E. J. Microscopic theory for nanotube piezoelectricity. *Phys. Rev. B* **2003**, *68*, 241405.

(33) Nakhmanson, S. M.; Calzolari, A.; Meunier, V.; Bernholc, J.; Nardelli, M. B. Spontaneous polarization and piezoelectricity in boron nitride nanotubes. *Phys. Rev. B* **2003**, *67*, 235406.

Graphical TOC Entry

![](./images/814653455426650112_12.jpg)