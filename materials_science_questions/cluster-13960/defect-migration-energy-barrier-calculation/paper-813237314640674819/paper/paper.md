# He, Kr and Xe diffusion in ZrN – An atomic scale study
M. Pukari*, P. Olsson, N. Sandberg

Royal Institute of Technology, AlbaNova University Center, Roslagstullsbacken 21, SE-106 91 Stockholm, Sweden

---

## ARTICLE INFO
Article history:
Received 24 September 2012
Accepted 15 February 2013
Available online 13 March 2013

## ABSTRACT
The atomic scale diffusion mechanisms for He, Kr and Xe in the nitride fuel component ZrN are developed from first principles. The vacancy formation energies reveal a prevalent N vacancy concentration in the material. However, a high N self-diffusion barrier hinders vacancy-aided Kr and Xe diffusion. High, attrac- tive binding energies of interstitial Xe and Kr to a N vacancy effectively eliminate interstitial diffusion mechanism for these gases. In comparison, He exhibits considerable degrees of freedom, as it is weekly bound to a N vacancy, enhances N-vacancy aided diffusion, has the lowest interstitial migration barrier, and has the capacity to be reintroduced into the ZrN lattice as an interstitial. N self-diffusion barriers are lowered if the diffusing N is in close proximity to a substitutional atom. The obtained results suggest a high release of He, while the majority of Kr and Xe is retained, in agreement with experiments.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction
For future nuclear systems to be successfully implemented, there are many challenges to overcome. One of such is to develop the optimal nuclear fuel for high burnup and for efficient transmu- tation of long-lived isotopes. Nitride fuels are considered as one of the candidates to fulfil these requirements in Generation-IV reac- tors, as well as in Accelerator driven systems [1-3].

Zirconium nitride exhibits many desirable characteristics as a nuclear fuel component, yet is seldom studied as such. Research on pure actinide nitrides, as well as mixed nitrides, has resulted in a respectable volume of knowledge on diffusion processes and fission gas behaviour in nitride fuels [4-9]. In order to help predict the properties of a ternary (A, Zr)N system (A for actinide) the properties and behaviours of the non-fissile components of the mixed nitride fuels have to be investigated and understood. For example, previous research has revealed that the relatively low dissociation temperature of UN [4,10,11] is significantly increased if UN is in solid solution with ZrN [12-14]. Likewise, it has been re- ported that, if in solution with ZrN, nitride fuels exhibit relatively good swelling behaviour [4,15], leading to a reduced interaction between the cladding and the hard nitride fuel [16].

A recent publication on irradiated (Pu, Zr)N reveals that the majority of fission-induced Xe is retained in the material, while, to a large extent, He is released to the fuel pin [4]. This raises ques- tions on the underlying differences of inert gas behaviour in nitride fuel. The recent development of computational technology, part- nered with applied modelling methods, simplifies the investigation of stoichiometric, impurity-free materials. Therefore, the emphasis of this work is on *ab initio* modelling, with the attempt to under- stand the migration paths of He, Kr and Xe in ZrN, on the atomic scale. The results of this work can provide an explanation to the macroscopic diffusion phenomena in ZrN. The current work pro- vides key information on gas diffusion mechanisms in the ZrN phase of nitride fuels. The results can also be applied in modelling of gas diffusion in U or Pu-bearing nitride fuels, which, due to the presence of f-electrons, are difficult to reliably model from first- principles with current methods.

To the authors' best knowledge, there is no experimental re- search investigating the diffusion behaviour of inert gases in ZrN. Furthermore, neither the atomic scale behaviour of fission gases, nor the macroscopic diffusion coefficients for nitride fuels are com- prehensively understood. It has been shown that the experimental results on self-diffusion vary to a large degree, often due to varia- tions in porosity or impurity content of the materials investigated [5]. For instance, research on self-diffusion in UN and (U, Pu)N has shown a strong correlation between stoichiometry and diffusion coefficients [6]. Fission gas release and irradiation-induced swell- ing have been investigated in numerous experiments concerning (U, Pu)N [4,7,8]. The diffusion of Xe and Kr have also been mea- sured experimentally in UC, a nuclear fuel material comparable with nitride fuels in terms of physical properties, such as crystal structure and thermal conductivity [17,18].

In general, nitride fuels present several advantages over the conventional oxide fuels, such as very high thermal conductivity [19-21] and high actinide density, while other vital traits, such as high melting temperature [22], are not compromised. Nitride fuels are currently considered as the primary fuel candidate for lead-cooled (ELECTRA [23], BREST-300 [24]) and lead-bismuth cooled (hyperion [25]) reactors. A good compatibility with liquid-metal coolants [26] is therefore crucial, along with being

* Corresponding author.
E-mail address: pukari@kth.se (M. Pukari).

---
0022-3115/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.jnucmat.2013.02.077

reprocessable along established routes [1,27,28]. To date, the dissociation of AmN during conventional sintering is the most challenging aspect of nitride fuel fabrication, although this can be addressed by employing spark-plasma sintering [29]. The unavoidable incorporation of C and O impurities [3] is equally problematic. In addition, it is necessary to enrich $N_2$ in the naturally less abundant $^{15}$N for fabricating nitride fuels, so that the eventual production of radioactive $^{14}$C can be minimised [30].

## 2. Methods

All first-principles calculations presented here are performed with the Density Functional Theory (DFT) [31] simulation package VASP 5.2.2 [32,33], using scalar relativistic projected augmented wave (PAW) pseudo-potentials [34,35]. The non-magnetic, rocksalt structure ZrN is simulated with Zr of 4 valence electrons and N of 5 valence electrons. The exchange and correlation effects are described with the generalised gradient approximation (GGA) [36]. The plane-wave cutoff energy is set to 500 eV for an adequate accuracy; electronic relaxation is considered to have converged at an energy divergence of $10^{-6}$ eV per atom.

The equilibrium lattice parameter, achieved by stepwise alteration of the volume of the unit cell, is deduced with the Birch-Murnaghan equation of state [37]. The cubic unit cell consists of 4 Zr and 4 N atoms, each species organised to a face-centered cubic crystal structure. For these calculations, a Monkhorst-Pack [38] mesh of $13 \times 13 \times 13$ $k$-points leads to a ground state energy convergence which is deemed sufficient. The obtained lattice parameter ($a_0 = 4.60$ Å) is used in the modelling work utilising a 216-atom supercell that consists of $3 \times 3 \times 3$ of the described unit cells. The supercell is chosen as a compromise between computational cost and image interference caused by the periodic boundary conditions. A Monkhorst-Pack mesh of $3 \times 3 \times 3$ $k$-points in the Brillouin zone is sufficient to satisfy the convergence criterion stated above. Unless specified otherwise, the internal degrees of freedom, as well as the volume, are allowed to relax, whereas the cell shape remains unchanged.

The nudged elastic band method [39] has been employed in order to determine the energy barriers that an atom would be required to cross as a prerequisite for interstitial or vacancy-aided diffusion. The migration barrier, $E_m$, is derived according to:
$$
E_m = E_n - E_0 \tag{1}
$$

Here $E_n$ is the total energy of the $n$th image along the reaction path in a specific ZrN system. $E_0$ represents the lowest total energy of the same system at one of the end points of the reaction path. The default spring constant setting is used along with the conjugate gradient algorithm for determining the local energy minimum of the images. During these calculations, the supercell volume is kept constant.

The vacancy formation energies are calculated as:
$$
E_{f,\text{vac}} = E_{\text{vac}} - n_{\text{Zr}} \mu_{\text{Zr}} - n_{\text{N}} \mu_{\text{N}} \tag{2}
$$
were $E_{\text{vac}}$ represents the total energy of a supercell with either a Zr or a N vacancy introduced into it; $n_{\text{Zr}}$ and $n_{\text{N}}$ the number of Zr and N atoms in this supercell; $\mu_{\text{Zr}}$ and $\mu_{\text{N}}$ the respective chemical potentials of each species. This formulation is based on the enthalpy of formation and does not include the entropy contribution. In contrast to defect formation calculations in monatomic materials, the chemical potentials for a poly-atomic material are not singularly defined. For the purpose of this paper we have made assumptions similar to surface energy calculations, assuming a thermo-chemical equilibrium in the bulk, and thereby defining the limiting values for Zr and N chemical potentials [40].

On the one hand, the chemical potentials must fall below the corresponding energies of formation of pure $N_2$ gas and Zr metal, representing a locally occurring saturation in either of the species. These energies are represented by the dissociation energy per atom of the triple-bonded $N_2$ gas and the hexagonal Zr metal:
$$
\mu_{\text{Zr}} < \mu_{\text{Zr,metal}} \tag{3}
$$

$$
\mu_{\text{N}} < \mu_{\text{N,gas}} \tag{4}
$$

On the other hand, the formation energy of a Schottky defect must equal the formation energy of a bulk ZrN per molecule as well as the sum of both chemical potentials:
$$
\mu_{\text{N}} + \mu_{\text{Zr}} = \mu_{\text{ZrN}} \tag{5}
$$

Finally, we stipulate that the combined effect of the chemical potentials in a stable ZrN must be such that, applied in Eq. (2), the vacancy formation energies obtained are positive:
$$
E_{f,\text{vac}} > 0 \tag{6}
$$

The equilibrium concentration per volume, $c_i$, of each vacancy type is determined according to:
$$
c_i = N_{\text{S}} \cdot \exp \frac{-E_{f,\text{vac}}}{k_{\text{B}} \cdot \text{T}} \tag{7}
$$

In the ZrN crystal there are $4.08 \times 10^{22}$ sub-lattice sites, $N_{\text{S}}$, per cm$^3$. The $c_i$ is calculated as a function of temperature, $T$. The variable $E_{f,\text{vac}}$ is defined above and does not include the entropy factor.

The binding energies, $E_b$, are found by determining the ground state energies of four systems, of which three contain a defect:
$$
E_b = E_D + E_{\text{ref}} - E_{D1} - E_{D2} \tag{8}
$$

Here $E_D$ is the energy of ZrN with two defects introduced into the material at a close distance to, or overlapping, each other. $E_{\text{ref}}$ represents the energy of the bulk ZrN, $E_{D1}$ and $E_{D2}$ the energies of the material with either defect introduced to the lattice independently. In this formulation, a negative binding energy indicates an attractive force between the defects. In order to verify the validity of the binding energies as well as confirm that the supercell is large enough for the introduced defects not to interfere with each other, we have additionally investigated the binding energies with a direct method. The binding energy is then determined from
$$
E_b = E_D - E_D'' \tag{9}
$$
where $E_D''$ represents a similar configuration to $E_D$, but with the two defects at maximal distance in relation to each other.

## 3. Results

### 3.1. Formation and binding energies

The nature of macroscopic diffusion of inert gases and self-diffusion of N and Zr is defined by migration on the atomic scale. It has been shown that the stoichiometry in some materials has great influence over the diffusion process [5]. Therefore, we investigate the formation energies of N and Zr vacancies as well as their equilibrium concentrations to help evaluate to what degree each type of these defects mediates diffusion in ZrN. The vacancy formation energies, $E_{f,\text{vac(Zr)}}$ and $E_{f,\text{vac(N)}}$, are given in Fig. 1 as a function of $\Delta \mu$, defined as
$$
\Delta \mu = (\mu_{\text{Zr}} - \mu_{\text{N}}) - (\mu_{\text{Zr,metal}} - \mu_{\text{N,gas}}) \tag{10}
$$

The range for $\Delta \mu$ is determined according to the limits stated by Eqs. (3)-(5), in effect stating that $\Delta \mu$ is limited by the heat of formation of ZrN ($-\Delta H < \Delta \mu < \Delta H$). The heat of formation of Zr metal ($\mu_{\text{Zr,metal}} = -8.45$ eV) in Eq. (3) is determined by modelling a hexagonal

![](./images/813237314640674819_1.jpg)

Fig. 1. Defect formation energies of Zr and N vacancies as a function of $\Delta\mu$, defined by Eq. (10). The lowest values of $\Delta\mu$ represent a $\mu_{\text{N,gas}}$-dominated region, while the highest values correspond to the $\mu_{\text{Zr,metal}}$-dominated region.

Zr supercell analogously to the methodology described in the previous section. The limit given by Eq. (4) ($\mu_{\text{N,gas}}=-9.80$ eV) is provided by literature [41]. The formation energy of a ZrN molecule, defined as the ratio of the formation energy of a bulk ZrN to the number of molecules in the crystal, is determined by modelling ($-20.35$ eV). Consequently, one can assume the following:

$$
\begin{aligned}
-10.55 &< \mu_{\text{Zr}} < -8.45 \text{ eV} \\
-9.80 &> \mu_{\text{N}} > -11.90 \text{ eV}
\end{aligned} \tag{11}
$$

The range for $\Delta\mu$ is further reduced by the requirement in Eq. (6), so that $-2.1 < \Delta\mu < 1.2$ eV (see Fig. 1). Within these boundaries, $E_{f,\text{vac}}(\text{Zr})$ remains high. To the contrary, the range of values for $E_{f,\text{vac}}(\text{N})$ is considerably lower and, with the exception of the region dominated by the heat of formation of $\text{N}_{\text{gas}}$ ($-2.1 < \Delta\mu < -1.45$ eV), falls below the values of $E_{f,\text{vac}}(\text{Zr})$. Such results would allow to suggest that, in accordance with previous theoretical and experimental results reported [42–45], the dominant vacancy type in ZrN is a N vacancy. The equilibrium concentrations of Zr and N vacancies, dependent on the chosen chemical potentials, are depicted in Fig. 2. For the purpose of illustration the value for $\Delta\mu$ is assumed to be 0, illustrating that, at room temperature, $c_{\text{N}}$ would be 25 orders of magnitude higher than $c_{\text{Zr}}$, while this disparity is greatly reduced at higher temperatures. This supports further the assumption of N vacancies being the dominant diffusion mediators. In comparison with the $4.08 \times 10^{22}$ N sub-lattice sites per $\text{cm}^3$, ZrN at high temperatures ($T > 1000$ K) is expected to contain a significant amount of N vacancies, rendering the material's closed porosity relatively high. The thermal concentration of vacancies is comparable with stoichiometric ZrN, whereas the effect of the often occurring N deficiency in manufactured ZrN [46,47] has been excluded from the calculations. In light of the potentially high fraction of vacancies in ZrN, we have evaluated the binding energies of two vacancies by the step-wise increase of the distance between these vacancies. The binding of two vacancies of the same species, as well as the binding of two vacancies of different species, was considered. In periodic boundary conditions, the given 216-atom supercell provides nine unique configurations for removing two atoms, in which case the distance between these atoms ranges from 3.26 to $10.80$ Å. The negative binding energies, obtained as defined by Eq. (8), indicate an attractive force between Zr vacancies ($-0.37 < E_{\text{bind}} < -0.15$ eV) and N vacancies ($-0.05 < E_{\text{bind}} < -0.01$ eV), with just one exception. As indicated in Fig.3, the positive binding energy of 0.22 eV for the two Zr vacancies and 0.10 eV for the N vacancies is obtained, provided they are first nearest neighbours (nn). The binding energies for a N and a Zr vacancy are always negative ($-0.18 < E_{\text{bind}} < -0.11$ eV). We must underline that no obvious trend of binding energy as a function of distance emerges. The low negative binding energies of two N vacancies suggest that they are considerably more independent than Zr vacancies in similar conditions, which further underlies the N-vacancy dependent diffusion mechanism.

![](./images/813237314640674819_2.jpg)

Fig. 2. Equilibrium concentrations of Zr and N vacancies as a function of temperature with the assumption of $\Delta\mu=0$. As a comparison, the number of sub-lattice sites in ZrN, $N_s$, is $4.08 \times 10^{22}$ $\frac{1}{\text{cm}^3}$.

### 3.2. Self-diffusion

According to the calculations performed on an anti-site defect, the energy cost for reversing the positions of two closest Zr and N atoms is 19.1 eV, compared to the 23.4 eV if the swapping occurs at the maximal distance possible in the supercell. These values indicate that the self-diffusion in ZrN must take place on two

![](./images/813237314640674819_3.jpg)

Fig. 3. Binding energies of two vacancies in relation to the inter-vacancy distance, whereas the two vacancies can be both N or Zr vacancies, or, a N and a Zr vacancy.

separate sub-lattices independently of each other. The migration barrier of self-diffusion for a N atom in its respective sub-lattice is 3.86 eV, corresponding to the energy required to move a N atom to an adjacent, pre-existing N vacancy. The respective self-diffusion barrier for Zr equals 4.50 eV (see Fig. 4c). For both species, the migration route is rectilinear and the diffusing atom mostly perturbs its nearest neighbours. In other words, a diffusing N atom primarily exerts force on atoms in the surrounding Zr sub-lattice, and vice versa. In either case, the required energy for passing the migration barrier is sufficiently high to claim that the self-diffusion of Zr and N atoms in ZrN is an exceptional event at operating temperatures, confirming a low mobility for vacancies in ZrN.

However, the characteristics of self-diffusion in an irradiated material incorporating inert gases is in all likelihood different. First of all, it is a matter of interest whether and to what extent the gas atoms are incorporated into the ZrN structure. Hence, we have calculated the binding energies of an interstitial gas atom – He, Kr or Xe – to a pre-existing vacant site on either Zr or N sub-lattices. These values, given in Table 1, state that the ZrN crystal will gain the most energy when eliminating the interstitial defects by incorporating them into vacant lattice sites. Furthermore, any of these gases would be more easily accommodated in the lattice by occupying a vacant Zr rather than a N site, were it not for the comparatively low fraction of Zr vacancies. Secondly, it is apparent that the probability of Kr and Xe atoms to be re-introduced into the crystal as an interstitial defect, once absorbed to a vacant lattice site, is negligible. This does not necessarily hold for He impurities, as the –0.50 eV binding energy can be exceeded by thermal energy, consequently reimposing the He atom as an interstitial defect.

<table>
<caption>Table 1
The binding energies of He, Kr and Xe atoms to a pre-existing N or Zr vacancy, calculated as stated in Eq. (8). Values in brackets are calculated according to Eq. (9).</caption>
<thead>
<tr>
<th>Sub</th>
<th>He</th>
<th>Kr</th>
<th>Xe</th>
</tr>
</thead>
<tbody>
<tr>
<td>N</td>
<td>–0.50 (–0.46)</td>
<td>–6.56 (–5.99)</td>
<td>–7.73 (–7.96)</td>
</tr>
<tr>
<td>Zr</td>
<td>–3.32 (–3.19)</td>
<td>–8.73 (–8.67)</td>
<td>–9.93 (–9.87)</td>
</tr>
</tbody>
</table>

![](./images/813237314640674819_4.jpg)

Fig. 4. Migration barriers for self-diffusion of N and Zr atoms in their respective sub-lattices in ZrN. (a) Self-diffusion of Zr as 1nn in the vicinity of A, where A represents either another Zr atom or a substitutional gas atom (He, Kr, and Xe). (b) Self-diffusion of N in similar conditions as described in a. (c) Migration barriers of self-diffusion, $E_m$, corresponding to the 8 scenarios described with a and b.

Two factors directly influence these binding energies. Above all, the noble gas atoms with larger volumes require more energy to be accommodated by the lattice, which explains the manyfold incorporation energy of Xe and Kr compared to He. Secondly, noble gas atoms are more readily accommodated in vacancies, which leave the most volume available. It is thus expected that most energy is gained by a Xe interstitial occupying a Zr vacancy. This statement is, of course, strictly valid only in case of a pre-existing Zr vacancy, as the method of calculation does not consider the Zr vacancy formation energy. The values in Table 1, calculated as defined by Eqs. (8) and (9), also highlight that these results are roughly in agreement between the two calculation methods. Ergo, the supercell size can be considered adequate to accommodate two defects with minimal perturbation, provided they are introduced at a maximal distance from each other. Given the results in Table 1, it is appropriate to subsequently investigate how these gases, as substitutional defects, influence self-diffusion. Our results, depicted in Fig. 4, illustrate that the migration barriers for N and Zr self-diffusion are reduced by a significant amount in the near vicinity of a substitutional He, Kr or Xe atom. The migration barrier for N self-diffusion is lowered by a maximum of 1.82 eV, given that, in relation to the substitutional He atom on the N sub-lattice, a N atom diffuses from a 1nn position to an equivalent position in the crystal. Likewise, the migration barrier is reduced if the N atom diffuses as a 1nn in relation to a substitutional Kr or Xe atom, though to a lesser extent (1.01 eV and 0.47 eV, respectively). A remarkable reduction for a self-diffusion migration barrier also occurs for Zr in similar conditions, the energy penalty being halved to as low as 2.22 eV in the vicinity of a He atom, compared to the 4.50 eV barrier in a gas-free supercell. Once the crystal accommodates a substitutional gas atom, the diffusion path is no longer rectilinear, but favours a trajectory which is curved towards the gas atom.

A substitutional gas atom will also moderate the migration barriers if a N atom is diffusing away from or towards the gas atom, as

![](./images/813237314640674819_5.jpg)

Fig. 5. The migration barriers of N atom diffusion from a 1nn position to a 2nn position, in relation to a substitutional He, Kr or Xe atom. The dashed line, representing N self-diffusion in a gas-free lattice, is given as a reference.

depicted in Fig. 5. The migration barrier for a N atom diffusing away from the He atom, from 1nn to 2nn position, is largely unaltered in comparison with N self-diffusion in a gas-free crystal. In similar conditions, migrating away from a substitutional Kr or Xe atom, the migration barrier is raised by 0.67 eV and 1.00 eV, respectively. The results in Fig. 5 appear to indicate that the migration barrier is directionally dependent, as the total energy difference for the 2nn position compared to the 1nn position in the case of substitutional Kr and Xe atoms corresponds to 0.19 eV, respectively 0.39 eV. Therefore, complementary calculations were performed, where a N vacancy is in a 3nn, 4nn or 5nn position in relation to a substitutional Kr or Xe atom. The obtained energies indicate no directional dependency between the total energy and the relative distance of the N vacancy and the substitutional gas atoms. However, according to complementary calculations performed on 3nn, 4nn and 5nn positions, there is no apparent relationship between the vacancy-substitutional atom distance and the ground state energy.

### 3.3. Interstitial gas diffusion
Due to the local restructuring of a crystal in the event of atoms fissioning, the He, Kr or Xe introduced into ZrN might occupy an interstitial position in the lattice. Therefore, we have introduced gas atoms into the lattice as interstitial defects to investigate the properties of their interstitial migration. For Kr and Xe, the given scenario is most relevant provided there is a lack of vacancies in the near vicinity of the interstitial as well as in the event of fission gases having already exhausted the possibility of occupying available vacant sites at that particular location. For He, however, interstitial diffusion is not exempt from being a component of the overall migration mechanism.

In the ZrN crystal, one can identify two types of equilibrium positions which an interstitial gas atom can occupy. The tetrahedral site is expected to provide the lowest global energy of the system, while the octahedral site serves as a saddle-point (see Fig. 6a). The interstitial diffusion of inert gases from site $A$ to $A'$, over B, results in the migration barriers shown in Fig. 6b. The results clearly illustrate that for the described diffusion path, there is a single-peak migration barrier with the maximum at the octahedral site for all gas species considered. The migration barriers of the gas atoms are correlated to their respective sizes. The smaller He atom ($r_W = 1.40$ Å) has a significantly lower migration barrier (1.04 eV) than the larger Kr ($r_W = 2.02$ Å) and Xe atoms ($r_W = 2.16$ Å) [48] have (1.56 eV and 1.52 eV).

### 3.4. Vacancy-aided gas diffusion
While vacancy-aided self-diffusion is often investigated in monatomic crystals, studying the diffusion of a third species in a diatomic crystal poses certain limitations. We consider here that the vacancies through which He, Kr and Xe diffuse must be of the same species – in this case N vacancies – and therefore vacancy aided diffusion occurs on a face-centered cubic N sub-lattice. We investigate here the diffusion capability of a cluster consisting of a single gas atom and two N vacancies. In such a cluster the gas atom either (a) adopts the site of one of the vacancies or (b) is positioned between the two vacancies in one or more equilibrium positions in the attempt to reach the most stable configuration. As illustrated in Fig. 7, our calculations indicate that the first is true for Kr and Xe, while the second applies for He. The larger Kr and Xe atoms remain as substitutional defects in the N sub-lattice, adjusting their position by less than 1% in the direction of the adjacent vacancy. Thus, the substitutional position serves as the global minimum for vacancy-aided diffusion for these two species. This is depicted in Fig. 8, along with the characteristic single-peak migration barrier. As expected, the migration barriers for vacancy-aided self-diffusion are similar for Kr and Xe, amounting to 2.29 eV and 2.44 eV, respectively.

![](./images/813237314640674819_6.jpg)

Fig. 6. (a) The migration path of an interstitial inert gas atom between tetrahedral positions (A and $A'$) through an octahedral position (saddle point, B). (b) The migration barriers for the described reaction path of interstitial diffusion of He, Kr and Xe.

As a contrast, our calculations on vacancy-aided He diffusion portray an alternative picture, one of the most pronounced differences being the ambiguous global energy minimum. As clarified in Fig. 7, one can expect to find the global energy minimum for the described cluster when the He atom is at a distance of roughly one-third from either of the vacancies on the (1 1 0) direction. That being said, there is a considerable degree of freedom for the He atom in all directions at no or negligible cost in energy. In the cluster of a single substitutional He and two N vacancies, the energy landscape within certain geometric boundaries is too flat for the calculations to converge within a reasonable time frame. Notably, a similar complication arises when attempting to estimate the N self-diffusion in the vicinity of a He atom. To the contrary of vacancy-aided diffusion of Kr and Xe, the global migration barrier ($E_m^{He}=0.09$ eV) for He occurs at the vacant N sub-lattice, whereas the local migration barrier at the midpoint between the two vacancies is indistinguishable from the expected precision variance.

### 3.5. He release from the lattice
In light of the reported binding energies, it is justifiable to assume that a substitutional He atom can be released from a N lattice site. As mentioned earlier, a release of Kr or Xe atoms is not foreseen. We have considered the release of He, as illustrated in Fig. 9a-c, from a single vacant site or from a system including two vacancies. Of the latter, two versions are considered. The results in Fig. 9d reveal that the cost of releasing a He atom from a single vacancy (1.40 eV) is lower than from a di-vacancy system

![](./images/813237314640674819_7.jpg)

Fig. 7. (a) In a cluster of 2 N vacancies and 1 substitutional He atom, the global energy minimum is at a distance of one third from the nearest vacancy on the (1 1 0) line. (b) To reach an equivalent equilibrium position (ep), the energy cost is negligible. (c) A Kr or a Xe atom in an equivalent initial setup is immobile; the required energy to reach an equivalent equilibrium position is 2.29 and 2.44 eV, respectively.

![](./images/813237314640674819_8.jpg)

Fig. 8. Migration barriers of vacancy-aided He, Kr and Xe diffusion in the N sublattice. Do note that the energies plotted for He diffusion are given on a separate axis and that the values are negligible compared to those of Kr and Xe diffusion. The x-axis represents relative positions between the two N vacancies on the (1 1 0) line as illustrated in Fig. 7.

(2.04 eV), provided that reaction path (b) is considered. Furthermore, the figure confirms the binding energy of a He interstitial to a single vacancy (0.49 eV) already at a very close distance and yields the binding energy of a He to a di-vacancy cluster (1.24 eV). However, due to the very low migration barrier for the reaction path (c) in Fig. 9, we can assume this to be the dominant mechanism for releasing He from a di-vacancy into the lattice. That being said, it is important to note that all three migration paths require less energy from the system than vacancy-aided He diffusion.

## 4. Discussion

A recent publication within the CONFIRM and EUTROTRANS framework programmes [4], reporting the results on post-irradiation examination of Pu-bearing nitride fuel, has brought up the need to better understand some of the observed phenomena. The results presented therein reveal that nuclear fuel pellets with a composition of ($\text{Pu}_{0.3}\text{Zr}_{0.7}$)N, irradiated to the burn-up of 9.7% fissions per initial metal atom (FIMA), released about 80% of the produced He, while only 5% of all produced Xe was released. Therefore, the results reported here help establish a foundation for explaining the underlying phenomena of inert gas diffusion in these or similar materials.

While the inert gases considered can diffuse interstitially, a migration barrier of 1.0–1.6 eV, in combination with the binding energies reported in Table 1, suggest that inert gas atoms are strongly trapped by vacancies. In the case of an atom fissioning, the crystal structure is locally disorganised due to the high recoil energy. Since the abundance of fission-induced vacancies largely surpasses the, on average, two fission products created, all inert gas atoms are presumably trapped eventually. The subsequent vacancy-aided diffusion of inert gases, on the grounds of the vacancy

![](./images/813237314640674819_9.jpg)

Fig. 9. The migration paths for releasing a He atom, locked into a single (a) or a di-vacancy system (b and c), into an interstitial position, followed by the corresponding migration barriers (d).

formation energies, equilibrium concentrations and migration barriers reported in this paper, is mainly limited by the N self-diffusion. Furthermore, the results presented here illustrate that the diffusion capacity of inert gas atoms has a clear correlation to the size of these atoms, as the deviation in migration barrier values cannot arise from bonding. The nature of migration of He is consequently distinguished compared to that of Kr and Xe.

The absorption of an interstitial He atom to a vacant lattice site promotes the self-diffusion of atoms on the same sub-lattice. Namely, self-diffusion barriers of N and Zr atoms are reduced in the near proximity of a substitutional He atom as well as between the nearest and next-nearest lattice sites. This reduction of about 1.8 eV for N self-diffusion in turn creates favourable conditions for vacancy-aided He diffusion. The latter is, in effect, immediate. Without a comparatively aggravated N self-diffusion, He release from ZrN would be prompt. It is important to consider that the binding energy of He to a N vacancy is considerably lower than that of Kr and Xe. For the He atom to be released from the sink and diffuse interstitially, it requires somewhat less energy than for the vacancy-aided diffusion, including the N self-diffusion dependency. It is thus possible that the following diffusion mechanisms are employed (a) He exploits the system of two vacancies and N self-diffusion in the vicinity of a He atom to advance in ZrN (Fig. 10a); (b) He is released from a single vacancy and diffuses interstitially until it becomes trapped in the next vacancy (Fig. 10b); and (c) He is released from a system of two vacancies and diffuses interstitially until it becomes trapped (Fig. 10c). It must be mentioned that once trapped in a Zr vacancy, He is estimated to be immobile. Due to the diffusion enhancing effect of a substitutional He, the cost of the three diffusion mechanism (a) is about 2.05 eV, whereas it requires 1.41 eV to proceed with mechanism (b), and 1.28 eV to proceed with mechanism (c), depicted in Fig. 10. The latter value represents a sum of the migration barrier reported in Fig. 9d (0.24 eV) and the interstitial migration barrier (1.04 eV). Finally, it is reasonable to assume that the flat energy landscape for He diffusion may lead to a mixed mechanism not considered here.

![](./images/813237314640674819_10.jpg)

Fig. 10. Diffusion mechanism of inert gases in ZrN, a two-dimensional schematic. (a) N vacancy-aided gas diffusion, valid for Kr and Xe, at the total energy cost of 2.29 + 2.85 eV and 2.44 + 3.39 eV, respectively. One of the diffusion options for He (2.05 eV). (b) He atom is released from a single N vacancy at a cost of 1.40 eV, after which it diffuses interstitially). and (c) He atom is released from a di-vacancy system at a cost of 1.28 eV.

Unlike He, the binding energy between a Kr atom and either a N or a Zr vacancy is significant enough to render the gas atom immobile lest an additional vacancy emerges in the vicinity of the Kr atom to be exploited for vacancy-aided diffusion. As some fraction of Kr and Xe diffuses out of ZrN, this must occur through vacancy-aided diffusion, albeit at a significantly lower rate than He. While the substitutional Kr aids N self-diffusion strictly around the Kr atom, it has no or slightly adverse effect on self-diffusion between the 1nn and 2nn neighbours. In other words, the Kr atom remains at a fixed position until a 4.53 eV migration barrier has been surpassed for attracting a second vacancy, in which case the mechanism illustrated in Fig. 10a must apply. Pertaining to Xe diffusion, the same observations apply, except that a substitutional Xe hinders N self-diffusion between 1nn and 2nn position in relation to itself (by 0.36 eV), which further impedes diffusion.

It bears pointing out that this is a considerably simplified image of the atomic scale migration mechanisms. This study has been limited to investigating a maximum of two vacancies mediating the diffusion. While more elaborate configurations assisting diffusion are not ruled out, the obtained binding energies suggest that two repulsive vacancies in nearest neighbour positions assist in diffusion, while a larger number of vacancies would preferentially agglomerate to form immobile pores. Neither is this approach able to allow for effects introduced by high temperature or the irradiation effects, e.g. rapidly forming and annealing defects in the material. While the self-diffusion migration barriers in a bulk ZrN are quite high, these are considerably reduced in an irradiated material, leading to a more rapid reorganization of the material.

Unlike the material studied here, the nitride fuel investigated within the CONFIRM and EUTROTRANS framework programmes contains a significant fraction of Pu. Neglecting this species in calculations may lead to somewhat alternative explanation of self-diffusion. However, one can assume that inert gas diffusion is largely unperturbed due to their chemical nature. It is beyond the scope of this work to take the effect of Pu properly into account.

## 5. Conclusions

The aim of this work is to clarify the differences in inert gas release from an irradiated nitride fuel, which consists largely of ZrN [4]. The results and discussion presented here demonstrate how the characteristic diffusion of He, Kr and Xe is a consequence of the size of these inert gas atoms. The dominant diffusion mechanisms for He, Kr and Xe gases are of interstitial type, vacancy-aided, or a combination of both, depending on the gas species in question. The reported self-diffusion and gas-diffusion barriers suggest why the majority of He would be released from an irradiated ZrN, whereas the majority of Kr and Xe would be retained. The results are in agreement with earlier publications, stating that N deficiency is prominent in nitride fuel materials. Finally, the values reported in this study provide insight into how fission-induced inert gases facilitate self-diffusion in ZrN, thus suggesting a considerably more rapid reorganisation of the irradiated material.

## Acknowledgements

The authors thank the Swedish Research Council for financial support through the GENIUS project and Prof. Janne Wallenius for reviewing the manuscript. The authors acknowledge interesting and enlightening discussions with Dr. Simon Middlebrough.

The computations were supported by the Swedish National Infrastructure for Computing (SNIC 003-11-26) via PDC.

## References
[1] H. Kleykamp, J. Nucl. Mater. 275 (1) (1999) 1-11.
[2] K. Minato et al., J. Nucl. Mater. 320 (12) (2003) 18-24.
[3] M. Streit, F. Ingold, J. Eur. Ceram. Soc. 25 (12) (2005) 2687-2692.
[4] J. Wallenius, Confirm: Final Technical Report: Collaboration on Nitride Fuel Irradiation and Modelling, Tech. Rep., Kungliga Tekniska Högskolan, 2009.
[5] J. Desmaison, W. Smeltzer, J. Electrochem. Soc. 122 (3) (1974) 354-357.
[6] H. Matvke, J. Less Common Met. 121 (0) (1986) 537-564.
[7] K. Tanaka et al., J. Nucl. Mater. 327 (23) (2004) 77-87.
[8] W. Chubb et al., Mater. Sci. Eng. 9 (0) (1972) 293-300.
[9] M. Klipfel, P.V. Uffelen, J. Nucl. Mater. 422 (13) (2012) 137-142.
[10] T. Ogawa et al., J. Alloys Compd. 271-273 (1998) 347-354.
[11] H. Tagawa, J. Nucl. Mater. 51 (1) (1974) 78-89.
[12] R. Thetford, M. Mignanelli, J. Nucl. Mater. 320 (1-2) (2003) 44-53.
[13] T. Ogawa, M. Akabori, J. Alloys Compd. 213-214 (1994) 173-177.
[14] M.V. Skupov et al., Mater. Sci. New Mater. 2 (67) (2006).
[15] B.D. Rogozkin et al., At Energy 109 (6) (2011).
[16] X.-J. Chen et al., Proc. Natl. Acad. Sci. USA 102 (9) (2005) 3198-3201.
[17] A. Auskern, Y. Osawa, J. Nucl. Mater. 6 (3) (1962) 334-335.
[18] H. Matzke, F. Springer, Radiat. Eff. 2 (1) (1969) 11-18.
[19] S. Hayes, J. Thomas, K. Peddicord, J. Nucl. Mater. 171 (23) (1990) 289-299.
[20] T. Kikuchi, T. Takahashi, S. Nasu, J. Nucl. Mater. 45 (4) (1973) 284-292.
[21] Y. Suzuki, Y. Arai, J. Alloys Compd. 271-273 (1998) 577-582.
[22] S. Sunder, N.H. Miller, J. Alloys Compd. 271-273 (1998) 568-572.
[23] J. Wallenius, E. Suvdantsetseg, A. Fokau, Nucl. Technol. 177 (3) (2012) 303-313.
[24] E. Adamov et al., Nucl. Eng. Des. 173 (1997) 143-150.

[25] M.S. Campagna, Hyperion Power Generation, ANS Winter Meeting, Washington DC, November 15-19, 2009.
[26] H. Bailly, D. Menessier, C. Prunier, The Nuclear Fuel of Pressurized Water Reactors and Fast Reactors: Design and Behaviour, Intercept Ltd., 1999.
[27] L.M. Ferris, J. Inorg. Nucl. Chem. 30 (10) (1968) 2661-2669.
[28] N. Hadibi-Olschewski et al., J. Nucl. Mater. 188 (0) (1992) 244-248.
[29] H. Muta et al., J. Nucl. Mater. 389 (1) (2009) 186-190.
[30] CEA, Carbon 14 Production and Nitrogen 15 Enrichment of Nitride Fuels, Tech. Rep., Laboratoire des Irradiations, 2001.
[31] W. Kohn, L.J. Sham, Phys. Rev. 140 (4A) (1965) A1133-A1138.
[32] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169-11186.
[33] G. Kresse, J. Furthmüller, Comp. Mat. Sci. 6 (1996) 15-50.
[34] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953-17979.
[35] G. Kresse, D. Joubert, Phys. Rev. B 59 (3) (1999) 1758-1775.
[36] J.P. Perdew et al., Phys. Rev. B 46 (11) (1992) 6671-6687.
[37] F. Birch, Phys. Rev. 71 (11) (1947) 809-824.
[38] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (12) (1976) 5188-5192.
[39] H. Jonsson, G. Mills, K.W. Jacobsen, Nudged elastic band method for finding minimum energy paths of transitions, in: B.J. Berne, G. Ciccotti, D.F. Coker (Eds.), Classical and Quantum Dynamics in Condensed Phase Simulations, World Scientific, 1998.
[40] S. Zhang, J.E. Northrup, Phys. Rev. Lett. 67 (17) (1991) 2339-2342.
[41] G. Aylward, T. Findlay, S.I. Chemical Data, 2nd ed., John Wiley & Sons, 1974.
[42] E.A. Kotomin et al., J. Phys. Condens. Matter 19 (10) (2007) 106208.
[43] E.A. Kotomin et al., Phys. Status Solidi C 4 (3) (2007) 1193-1196.
[44] E. Kotomin, Y. Mastrikov, J. Nucl. Mater. 377 (3) (2008) 492-495.
[45] E. Kotomin et al., Nucl. Instrum. Methods Phys. Res., Sect. B 266 (12-13) (2008) 2671-2675.
[46] T.B. Massalski, H. Okamoto, A. International, Binary Alloy Phase Diagrams, 2nd ed., vol. 3, ASM International, 1990.
[47] M. Takano et al., J. Alloys Compd. 439 (12) (2007) 215-220.
[48] A. Bondi, J. Phys. Chem. 68 (3) (1964) 441-451.