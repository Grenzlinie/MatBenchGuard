# Ab initio calculations for industrial materials engineering: successes and challenges

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

2010 J. Phys.: Condens. Matter 22 384215

(http://iopscience.iop.org/0953-8984/22/38/384215)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:
IP Address: 150.108.161.71
The article was downloaded on 27/12/2012 at 08:23

Please note that [terms and conditions apply].

# Ab initio calculations for industrial materials engineering: successes and challenges

Erich Wimmer$^{1,2}$, Reza Najafabadi$^{3}$, George A Young Jr$^{3}$, Jake D Ballard$^{3}$, Thomas M Angeliu$^{3}$, James Vollmer$^{3}$, James J Chambers$^{4}$, Hiroaki Niimi$^{4}$, Judy B Shaw$^{4}$, Clive Freeman$^{1,2}$, Mikael Christensen$^{1,2}$, Walter Wolf$^{1,2}$ and Paul Saxe$^{1,2}$

$^{1}$ Materials Design, Inc., PO Box 2000, Angel Fire, NM 87710, USA
$^{2}$ Materials Design SARL, 44 av. F-A. Bartholdi, 72000 Le Mans, France
$^{3}$ Knolls Atomic Power Laboratory, PO Box 1072, Schenectady, NY 12301-1072, USA
$^{4}$ Advanced CMOS, Texas Instruments Incorporated, Dallas, TX 75243, USA

E-mail: ewimmer@materialsdesign.com

Received 12 February 2010, in final form 9 July 2010
Published 7 September 2010
Online at stacks.iop.org/JPhysCM/22/384215

## Abstract
Computational materials science based on *ab initio* calculations has become an important partner to experiment. This is demonstrated here for the effect of impurities and alloying elements on the strength of a Zr twist grain boundary, the dissociative adsorption and diffusion of iodine on a zirconium surface, the diffusion of oxygen atoms in a Ni twist grain boundary and in bulk Ni, and the dependence of the work function of a TiN–HfO₂ junction on the replacement of N by O atoms. In all of these cases, computations provide atomic-scale understanding as well as quantitative materials property data of value to industrial research and development. There are two key challenges in applying *ab initio* calculations, namely a higher accuracy in the electronic energy and the efficient exploration of large parts of the configurational space. While progress in these areas is fueled by advances in computer hardware, innovative theoretical concepts combined with systematic large-scale computations will be needed to realize the full potential of *ab initio* calculations for industrial applications.

(Some figures in this article are in colour only in the electronic version)

---

## 1. Goals of computational materials engineering

During the past three decades, computational materials science has evolved from a fundamental research activity into a field that increasingly impacts engineering disciplines. This does not imply that theoretical methods have fully matured. Quite the contrary, the growing interest in applying computational materials science to complex industrial problems exposes the challenges which still have to be overcome, for example in dealing with the configurational complexity of surface reactions and in achieving accuracy in describing chemical reactions and phase transitions. Nevertheless, the contact between theoretical research and practical engineering applications has been made and is now sparking an exciting dialog between researchers developing new computational methods and scientists and engineers using these capabilities to solve technological problems.

An overall goal of computational materials science and engineering (CMS&E) is the atomic-scale understanding and quantitative prediction of materials properties. This en- compasses mechanical, thermal, electrical, optical, magnetic, and chemical properties of metals, semiconductors, ceramics, glasses, polymers, liquids, and gases. Many technological problems involve interfaces between these materials, so one has to consider any combination of the above listed materials.

A wide range of theoretical and computational approaches are being pursued, which are presently at quite different stages of maturity. This includes analytical theory, heuristic cor-
---

**Table 1.** Representative materials properties accessible by *ab initio* calculations.

| Structural properties | Chemical properties |
|-----------------------|---------------------|
| Interatomic distances in molecules and clusters<br>Lattice parameters and atom positions in crystals<br>Surface relaxations and reconstructions<br>Defect structures (point defects, dislocations)<br>Adsorption geometries<br>Structure of interfaces<br>Density of liquids and amorphous systems | Reaction rates in gases and condensed phases<br>Surface reactivity<br>Solid–solid reactions<br>Pressure-induced reactions<br>Photochemical reactions |
| **Thermo-mechanical properties** | **Transport properties** |
| Elastic moduli<br>Speed of sound<br>Vibrational properties<br>Thermal expansion<br>Cleavage energy | Mass diffusion<br>Permeability<br>Thermal conductivity<br>Viscosity |
| **Thermodynamic properties** | **Electronic, optical, and magnetic properties** |
| $\Delta U$, $\Delta H$, $\Delta S$, $\Delta G$, $C_p$, $C_v$<br>Solubility<br>Melting temperature<br>Vapor pressure<br>Surface energy, surface tension<br>Interface energy | Electric moments<br>Polarizability, hyperpolarizability<br>UV and visible spectra<br>Dielectric properties<br>Piezoelectric properties<br>Work function<br>Energy band structure, band gaps, band offsets<br>Ionization energies, electron affinities<br>Magnetic moments, magnetic anisotropy energy |

relations such as quantitative structure–property relationships (QSPR), coarse-grain methods such as dissipative particle dynamics, molecular dynamics and Monte Carlo methods employing empirical interatomic potentials (forcefields), semi-empirical quantum mechanical methods, and finally *ab initio* quantum mechanical methods. The latter are the focus of this contribution. This approach holds the promise for having the highest predictive power, since no system-specific parameters are introduced in the model. However, this level of theory possesses three main limitations, namely the restriction to a relatively small system size (a few hundred atoms per supercell), the limitation to a very narrow region of phase space (a few thousand configurations), and the uncertainties in the total energy. Progress in these three areas is the key to unlocking the full promise of CMS&E. Despite the above mentioned limitations remarkable capabilities are now available, as will be illustrated and discussed in the present contribution.

## 2. The central role of materials properties

Materials properties and their variation in response to environment (stress, temperature, electromagnetic fields, exposure to corrosive fluids, irradiation) are the cornerstone of materials science. Table 1 summarizes a representative range of materials properties, which are within the scope of the present computational approaches.

Successes of *ab initio* calculations have been demonstrated in all of the areas listed in table 1. One of the first convincing examples of industrial impact was the pioneering *ab initio* calculations of thermodynamic properties of industrially important molecules in the research laboratories at Dupont in the USA using Hartree–Fock theory with second-order perturbation theory (MP2) and analytic second derivatives to compute the vibrational terms of the partition function [1]. It turned out that for molecules such as the different isomers of fluorinated ethane, which became replacements of chlorofluorocarbons (CFC) refrigerants, the accuracy of the computed heats of formation was comparable to that obtained experimentally. Yet, despite the high cost and modest performance (by today's standards) of large-scale computers in the late 1980s, computations were already then significantly faster and cheaper than experiments, namely about $5000 and a few days per compound computationally versus about $50 000 and several months experimentally. Today, this type of calculation can be done on a laptop in a few hours.

The capabilities available in the 1980s for small molecules containing main-group elements in the gas phase have now been achieved for solid state materials containing essentially any element of the periodic table in structures, which contain of the order of 100 atoms per unit cell. This is illustrated by the following examples.

## 3. Examples

### 3.1. Effect of impurities on a Zr grain boundary

The formation of cracks and subsequent fracture of structural materials is a major concern, especially in nuclear power plants where safety is of highest importance. To this end, substantial efforts have been made to understand factors which control fracture in high-performance zirconium and nickel alloys.

In our first example, brittle fracture of zirconium alloy cladding can occur during power transients in commercial nuclear power plants and is known as pellet–clad interaction (PCI). The responsible mechanism is believed to be fission product induced stress corrosion cracking (SCC), with iodine suspected as the primary detrimental specie. However, mechanistic details for how iodine promotes brittle failure are unknown. In one mechanism, iodine adsorbed on a crack

![](./images/811741440534118400_1.jpg)

Figure 1. Periodic model of a Zr Σ7(0001) twist grain boundary. Each grain is represented by a two-dimensionally periodic slab consisting of six atomic layers. The picture shows a fully relaxed structure obtained from density functional calculations. The top view (lower panel) displays only the Zr layers adjacent to the grain boundary.

face lowers the Zr-Zr bond energy leading to separation along crystallographic planes (transgranular cleavage crack path) or grain boundaries (intergranular crack path) [2]. Since it is difficult to obtain experimental information on the effects of impurity atoms on grain boundary strength, theory provides useful insight via first-principles calculations. Therefore, the effects of different impurity elements on pure Zr grain boundary cohesion were investigated using a first-principles approach [3]. The results obtained for pure zirconium were expected to be qualitatively correct for zirconium-base cladding materials as their alloying concentration in the matrix is small.

A Σ7(0001) twist grain boundary of Zr was modeled using a supercell containing six atomic layers for each grain amounting to a total of 84 atoms per supercell, as illustrated in figure 1. The lattice parameters and atomic positions were relaxed using density functional theory (DFT) with the generalized-gradient approximation (GGA) as proposed by Perdew-Burke-Ernzerhof (PBE) [4]. The Kohn-Sham equations were solved with the projector-augmented-wave method [5] as implemented in the Vienna ab initio simulation package (VASP) [6] and integrated in the MedeA computational environment [7]. The plane-wave cutoff energy was 330 eV. The $k$-spacing of the Monkhorst-Pack grid for the integration over the Brillouin zone was taken to be $0.5\ \mathring{\text{A}}^{-1}$ using a Methfessel-Paxton scheme with $\sigma=0.2$ eV. Geometry relaxations were converged to forces smaller than $0.01\ \text{eV}\ \mathring{\text{A}}^{-1}$ on any atom in the cell. This choice of model size and computational parameters provided a good balance between accuracy and computational efficiency.

The fully relaxed structure of the pure grain boundary showed only small distortions from the atomic positions in bulk

<table>
<caption>Table 2. Computed cleavage energy of bulk Zr and a Σ7(0001) grain boundary.</caption>
<thead>
<tr>
<th>Type of cleavage</th>
<th>System</th>
<th>$E_{\text{cleave}}$ (J m⁻²)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Transgranular</td>
<td>Zr bulk along (0001) plane</td>
<td>3.15</td>
</tr>
<tr>
<td>Intergranular</td>
<td>Zr Σ7(0001) grain boundary</td>
<td>2.86</td>
</tr>
</tbody>
</table>

Zr, which crystallizes in a hexagonal close-packed structure at ambient conditions (cf figure 1). Using this structure as reference, the cleavage energy (ideal Griffith energy), $E_{\text{cleave}}$, was computed from the energy difference of the system with the grain boundaries and free surfaces, which were evaluated by removing one of the grains in the supercell and relaxing the atomic positions. As reference the cleavage of a crystal without any grain boundary was computed from the total energy of a pure Zr and the free surfaces. The results are summarized in table 2.

The Σ7(0001) twist grain boundary of Zr is very dense and the local coordination of the atoms at the grain boundary remains similar to that in bulk Zr. Hence, cleavage of the system along the grain boundary is only 9% less than that of a perfect Zr crystal. It should be noted here that the cleavage energy computed in this model represents a limiting case of a cleavage in the sense that only atomic relaxations of the surfaces after separations are taken into account. Actual cleavage processes are complicated due to dynamic effects and formation of defects such as dislocations and other structural rearrangements. Furthermore, only the electronic energies of the initial and final states are considered here. Despite these simplifications, valuable systematic trends can be identified as shown below. It is expected that calculations performed on more general grain boundaries show the same trends.

The effect of alloying elements and impurities on the strength of these grain boundaries is obtained by first determining the equilibrium position of the impurity element (interstitial or substitutional) and then by following the same computational protocol as outlined for the pure system, namely relaxation of the system with the impurity at the grain boundary, separation of the grains and relaxation of the free surfaces.

The results for Zr are illustrated in figure 2. Most elements investigated in this work have a detrimental effect on the strength of this dense Zr grain boundary. The strongest effect is seen for cesium, iodine, and helium. Sb, O, C, N and B are more stable in the bulk than at the grain boundary (in terms of electronic total energies) and thus are unlikely to play a significant role in influencing the strength of grain boundaries. Only Nb, Cr, and Fe have a weak tendency to strengthen the grain boundary. As expected, Hf has almost no effect due to its similar size and chemical properties.

### 3.2. Adsorption and diffusion of iodine on Zr surface

Further studies regarding the interaction of iodine and zirconium alloy cladding evaluated the propensity of molecular iodine to adsorb, dissociate, and diffuse on the surface. The intent was to gain insight on potential rate controlling processes of iodine SCC. Zr-I reactions have been extensively

![](./images/811741440534118400_2.jpg)

Figure 2. Computed effect of impurities on the strength of a Zr Σ7(0001) grain boundary (GB) ordered from the most weakening (Cs) to the most strengthening (Fe). Impurities having a tendency to segregate to the grain boundaries are marked by solid black bars; elements with a tendency to dissolve in the bulk are shown with empty bars.

studied experimentally in support of the industrial Van Arkel iodine process to refine zirconium [8, 9], and attempts have been made to experimentally show links between reaction kinetics and mechanistic details of iodine SCC [10, 11]. This current study used electronic structure calculations combined with algorithms for transition state searches to provide detailed insight into Zr–I interactions and quantitative data of adsorption energies and diffusion rates for this system.

In the gas phase, iodine forms diatomic molecules in thermal equilibrium with free atoms. The computed dissociation energy is quite large, namely 206 kJ mol⁻¹. The equilibrium constant for the dissociation of I₂ into iodine atoms remains below 0.001 for temperature up to 1500 K. Hence we need to consider the adsorption of iodine molecules on metallic zirconium. The hexagonal close-packed basal plane, i.e. the (0001) plane was chosen as a representative surface.

Computation of the adsorption profile using a nudged elastic band method [12] revealed no barrier to the dissociation of an I₂ molecule on a Zr(0001) surface as illustrated in figure 3. The computed adsorption energy (I₂ (gas phase molecule) → 2I adsorbed atoms) is large, namely nearly 600 kJ mol⁻¹, which indicates a very strong chemical affinity of iodine and zirconium. This strong affinity is due to chemical bonding formed between iodine and its neighboring Zr atoms. Therefore, it is relatively insensitive to surface crystallographic orientation

<table>
<caption>Table 3. Computed adsorption energy and electronic part of chemical potential of an iodine atom on a Zr(0001) surface as a function of coverage. An isolated iodine molecule in the gas phase (1/2I₂) and the clean Zr surface are used as reference.</caption>
<thead>
<tr>
<th>Coverage</th>
<th>Adsorption energy (kJ mol⁻¹)</th>
<th>Chemical potential (kJ mol⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.11</td>
<td>−267</td>
<td>−267</td>
</tr>
<tr>
<td>0.22</td>
<td>−263</td>
<td>−258</td>
</tr>
<tr>
<td>0.33</td>
<td>−258</td>
<td>−248</td>
</tr>
<tr>
<td>0.67</td>
<td>−199</td>
<td>−139</td>
</tr>
<tr>
<td>0.89</td>
<td>−159</td>
<td>−40</td>
</tr>
<tr>
<td>1.00</td>
<td>−141</td>
<td>0</td>
</tr>
</tbody>
</table>

Knowledge of the enthalpy and the entropy of an iodine atom adsorbed on the Zr(0001) as a function of temperature and coverage yields its chemical potential in the adsorbed state. On the scale of the adsorption energy vibrational contributions are small and are ignored. Together with the data for the chemical potential of iodine in the gas phase (present as I₂ molecules) one can compute the adsorption isotherm [3]. A key ingredient is the dependence of the electronic total energy as a function of iodine coverage. This information is obtained from a series of total energy calculations performed on the above supercell model with the results given in table 3.

Throughout the range of coverages investigated in the present work, iodine atoms are adsorbed in three-fold hollow ‘fcc’ sites, where no Zr sub-surface atoms are directly below the adsorbed iodine atoms. At a coverage of $\theta = 1$ all fcc sites of the Zr(0001) surface are occupied by iodine atoms. Somewhat surprisingly, the bond distance between adsorbed iodine atoms and the nearest surface Zr atoms decreases from

![](./images/811741440534118400_3.jpg)

Figure 3. Computed energy profile of the dissociation of an I₂ molecule on a Zr(0001) surface. Note the absence of any activation barrier and the rather large adsorption energy of almost 600 kJ mol⁻¹ I₂. The reaction coordinate, x, is related to the height of the center of mass of the two iodine atoms with $x = 0$ corresponding to the undissociated I₂ molecule at a height of 7.83 Å and $x = 1$ referring to the adsorbed iodine atoms at a height of 2.27 Å.

![](./images/811741440534118400_4.jpg)

Figure 4. Difference in standard chemical potential of an iodine atom adsorbed on a Zr(0001) surface and $I_2$ in the gas phase.

3.04 to 2.90 Å with increasing coverage while the distance between the surface and sub-surface Zr layer expands.

A fit to the data given in table 3 together with the temperature-dependent contribution yields the chemical potential $\mu_{i, \text{ads}}$ as a function of coverage $\theta$ and temperature $T$.
$$
\begin{aligned}
\mu_{\mathrm{I}, \mathrm{ads}}(q, T) &=-273.1-51.22 \theta+489.1 \theta^{2}-161.5 \theta^{3} \\
&+T\left(-10^{-5} T-3.71 \times 10^{-3} \theta+6.81 \times 10^{-3}\right).
\end{aligned}
\tag{1}
$$

For the gas phase the chemical potential at standard pressure can be expressed by the following fit:
$$1 / 2 \mu_{\mathrm{I}_{2}, \text { gas }}^{0}(T)=23.88-0.130 T-9 \times 10^{-6} T^{2}. \tag{2}$$

The difference in the Gibbs free energy between the gas and the adsorbed state is
$$\Delta G_{\mathrm{I}}^{0}=\mu_{\mathrm{I}, \mathrm{ads}}(\theta, T)-1 / 2 \mu_{\mathrm{I}_{2}, \text { gas }}^{0}(T). \tag{3}$$

A plot of this standard chemical potential difference is shown in figure 4. Due to the very strong bonding of iodine to the zirconium surface the chemical potential of iodine on the surface is lower than in the gas phase even at quite high temperatures.

For a given temperature and coverage, the equilibrium constant $K$ at a standard pressure of 100 kPa (1 bar) is given by
$$K=\mathrm{e}^{-\Delta G_{\mathrm{I}}^{0} /(R T)}. \tag{4}$$

Using statistical thermodynamics within an independent site model, the relationship between the iodine partial pressure $P$ in the gas phase and the surface coverage is given by the expression
$$P=\frac{\theta^{2}}{K^{2}(1-\theta)^{2}}. \tag{5}$$

Compared with the standard Langmuir adsorption isotherm, equation (5) contains a square because the present case involves dissociative adsorption of a diatomic molecule rather than adsorption of monoatomic (or monomolecular) species.

![](./images/811741440534118400_5.jpg)

Figure 5. Computed adsorption isotherms of $I_2 \to 2I$ on a Zr(0001) surface.

The resulting adsorption isotherms are plotted in figure 5. A large fraction of the zirconium surface is covered by iodine even at very low partial pressures of the iodine gas, due to the large adsorption energy of iodine on the zirconium surface. This is an important property of iodine, which is related to enhanced intergranular fracture as will be discussed below. In the present study zirconium iodide precipitation was not considered but might be important at high iodine surface coverage.

Knowing that a fairly high concentration of iodine atoms are adsorbed on zirconium surfaces exposed to an atmosphere containing molecular iodine, the next property of interest is the diffusivity of these atoms. As will be shown below, the diffusivity of iodine atoms on Zr(0001) surfaces is very high despite their large adsorption energy.

The calculation of the diffusion coefficient was carried out using Eyring's transition state theory as discussed, for example, in [13]. The energy profile of the diffusion path shown in figure 6 revealed that the most stable adsorption site of an I atom on a Zr(0001) surface is a three-fold hollow-site without a Zr atom in the sub-surface layer. This site corresponds to an ABC stacking in face-centered cubic lattice and is thus called the FCC site. The adjacent HCP site is slightly less favorable, which gives rise to a corrugated diffusion profile. The electronic part of the activation barrier is $7.0 \mathrm{~kJ} \mathrm{~mol}^{-1}$. The vibrational frequencies of an I atom in the ground state and the transition state are approximated by displacing the I atom from their fully relaxed structures in the ground state and the transition state. The frequencies of the I atom vibrating in the FCC site are 3.7 THz for the mode perpendicular to the surface and 2.3 THz for the two vibrations parallel to the surface. At the transition state one of the in-plane modes becomes a translation and the two remaining modes have frequencies of 3.9 THz for the out-of-plane mode and 3.1 THz for the remaining in-plane mode. At elevated temperatures both FCC and HCP sites will be occupied. Taking this into account leads to an effective diffusion coefficient of the form
$$D=\frac{1}{2} d^{2} \Gamma\left[1+\mathrm{e}^{-\Delta G_{\mathrm{FCC}-\mathrm{HCP}} /(R T)}\right]^{-1}. \tag{6}$$

![](./images/811741440534118400_6.jpg)

Figure 6. Computed energy profile for the diffusion of an iodine atom on a Zr(0001) surface. The so-called FCC site is energetically more stable than the HCP site. Note the small energy scale compared with the adsorption energy.

In this expression $\Gamma$ is the jump rate from the FCC to the HCP site as calculated from transition state theory and $\Delta G_{\text{FCC-HCP}}$ is the free energy difference between the two states. The distance between two adjacent FCC sites is $d$. The inclusion of the metastable site has only a small retarding effect on the computed diffusion rate. A linear fit to an Arrhenius plot leads to a diffusion coefficient of $D = D_0\text{e}^{-Q/(RT)}$ with an effective barrier of $Q = 6.78$ kJ mol$^{-1}$ and a prefactor $D_0 = 2.0 \times 10^{-8}$ m$^2$ s$^{-1}$. Note that the effective barrier $Q$ is slightly different from the electronic energy difference of 7.0 kJ mol$^{-1}$ shown in figure 6.

In a recent study, Legris and Domain [14] reported smaller values for the diffusion coefficients. In particular at 600 K Legris and Domain obtain a diffusivity of $3.2 \times 10^{-9}$ m$^2$ s$^{-1}$ compared with $2.0 \times 10^{-8}$ m$^2$ s$^{-1}$ computed in the present work. The main reason for this difference is a discrepancy in the values for the activation energy. For jumps between FCC and HCP sites the present work gives an effective activation energy of 6.78 kJ mol$^{-1}$ compared to 10.6 kJ mol$^{-1}$ in [14]. The difference is likely due to the treatment of the Zr surface atoms. In the present work, the Zr atoms are allowed to relax as an iodine atom diffuses across the surface, whereas in the previous study the positions of the Zr atoms were fixed.

These results provide insight into mechanistic details of iodine SCC in zirconium-base alloys. Iodine was shown to readily dissociate and diffuse along a Zr(0001) surface and will decrease cohesion when residing at a grain boundary. However, experimental observations using iodine tracer methods showed no iodine diffusion along Zr grain boundaries ahead of a crack tip [15]. While calculated iodine diffusivities yield a $\sim$140–230 $\mu$m s$^{-1}$ root mean distance for surface diffusion, this distance is large compared to pellet-clad interaction (PCI) crack propagation rates of 2–20 $\mu$m s$^{-1}$ [16]. This comparison suggests that surface diffusion would supply sufficient iodine to a moving crack tip to enable an iodine-induced cracking mechanism, in agreement with [17]. Supporting experimental evidence showed iodine to readily chemisorb onto zirconium-base alloy to form chemisorbed ZrI$_4$ that migrates readily under a temperature gradient [18]. Whether iodine is weakening the crack tip or promoting Zr removal by a ZrI$_{4(g)}$ mechanism is not completely clear and warrants further investigations. However, the present work demonstrates that iodine atoms can be present and are very mobile at crack tips even at relatively low concentrations of iodine in the gas phase and at elevated temperatures.

### 3.3. Diffusion of oxygen in a nickel grain boundary

For the understanding of SCC of Ni-base alloys it is of fundamental importance to understand the thermodynamic and kinetic properties of impurities in the bulk material, at grain boundaries, and at surfaces. The dominant atomistic mechanism controlling the SCC growth rate in Ni-base alloys is not well understood. The temperature dependence of the SCC growth rate is not consistent with a single known diffusion process in the oxide or metal. It is speculated that it is more consistent with the oxygen diffusion along grain boundaries in Ni [19]. However, there is no consensus in the experimental literature on the diffusivity of oxygen in bulk, let alone along grain boundaries [20].

To address this, we investigate here the diffusion of an oxygen atom in a Ni $\Sigma 5(001)$ twist grain boundary. In addition, we also consider diffusion of an oxygen atom in bulk Ni through the interstitial mechanism to assess its importance to SCC in Ni-base alloys.

The grain boundary is modeled by a repeated slab geometry consisting of 40 Ni atoms, namely four layers with five atoms for each of the two grains in the supercell. The geometry is relaxed using the same computational approach as in the case of the Zr grain boundary, except that the calculations for Ni were done with a spin-polarized Hamiltonian and a 400 eV energy cutoff dictated by the oxygen atom.

Once the model for the pure Ni grain boundary is established, a geometric analysis of the empty space at the grain boundary is performed to identify potential sites for interstitial oxygen atoms. A total of 12 sites are found with three different local environments (symmetry types) as illustrated in figure 7. For each of the three symmetry-inequivalent positions an oxygen atom is inserted and the position of all atoms in the supercell are relaxed. Next, the transition states between each of the symmetry-inequivalent oxygen sites are determined using a nudged elastic band method as described earlier.

For each of the (meta)stable oxygen sites and the transition states the phonon dispersions for the entire supercell are computed using the direct phonon method of Parlinski [21] as implemented with VASP [6] in the MedeA environment [7]. Figure 8 shows the phonon dispersions for the case of an oxygen atom at transition state C (cf figure 7). The two high-frequency modes around 15 THz correspond to vibrations of the oxygen atom perpendicular to the diffusion path. The mode with an imaginary frequency is plotted as negative eigenvalue near $-7$ THz. It corresponds to a motion of the O atom along the diffusion path.

![](./images/811741440534118400_7.jpg)

Figure 7. Topology of interstitial sites for oxygen atoms in a Ni Σ5(001) grain boundary. The network drawn as dark tubes represents the possible diffusion channels of oxygen atoms. The Ni atoms in the two layers adjacent to the grain boundaries are denoted by $Ni_{up}$ and $Ni_{down}$. The symmetry-inequivalent stable and metastable oxygen sites are labeled by numbers (1, 2, 3) with + and – indicating a position closer to the upper and lower Ni layer, respectively. A, B, and C mark the three inequivalent transition states between the oxygen sites.

![](./images/811741440534118400_8.jpg)

Figure 8. Phonon dispersion of a 40-atom Ni-supercell with an oxygen atom in a Σ5(001) twist grain boundary at the transition state C (cf figure 7). The arrows mark modes associated with the oxygen atom.

According to Eyring's transition state theory the electronic energy of the diffusion barrier together with the vibrational contributions of the free energy at the transition state and the initial state contain all information necessary to compute a temperature-dependent jump rate. This is done for each jump from each of the local minima of an O atom to the nearest minimum. Finally, the diffusion coefficient is obtained by a kinetic Monte Carlo simulation using the jump rates computed from ab initio theory as described above.

The result is shown in figure 9 in the form of an Arrhenius plot. The effective activation barrier for O diffusion in this Ni grain boundary is relatively low, namely $25.8\ \text{kJ mol}^{-1}$ with a quite small prefactor of $2.7 \times 10^{-10}\ \text{m}^2\text{s}^{-1}$. This leads to a fairly gentle slope in an Arrhenius plot (cf figure 9). In contrast, the effective barrier for interstitial diffusion of oxygen in bulk Ni is quite high ($78.1\ \text{kJ mol}^{-1}$), but with a significantly larger prefactor of $5.0 \times 10^{-7}\ \text{m}^2\text{s}^{-1}$. Note that previous work indicates that oxygen prefers the interstitial site (vice substitutional diffusion) at temperatures below $\sim$600 K [20].

This gives rise to a qualitatively different behavior at low and high temperatures. At low temperatures the high effective barrier in bulk diffusion causes a very low diffusion coefficient. In contrast, the lower effective barrier for grain boundary diffusion makes it possible for O atoms to diffuse significantly even at low temperature. At high temperatures, the prefactor $D_0$ prevails and bulk diffusion is faster than grain boundary diffusion.

![](./images/811741440534118400_9.jpg)

Figure 9. Computed diffusivity of an oxygen atom in a Ni Σ5(001) twist grain boundary compared with the interstitial oxygen diffusing in bulk Ni. For comparison also the computed values of interstitial hydrogen diffusion in bulk Ni are given. All calculations are based on ab initio electronic structure theory combined with phonon calculations and kinetic Monte Carlo simulations.

The calculated activation energies for interstitial diffusion of oxygen in bulk Ni ($78.1\ \text{kJ mol}^{-1}$) and grain boundary diffusion (Σ5(001) twist grain boundary, $25.8\ \text{kJ mol}^{-1}$)

are lower than the reported activation energy for stress corrosion $(\sim 110-150 \mathrm{~kJ} \mathrm{~mol}^{-1})$. Thus simple diffusion is not the rate controlling mechanism, but could be part of a more complex process of oxygen supply to the crack tip (e.g., one involving uptake, diffusion, and trapping). These bulk and grain boundary diffusion activation energies are far below those reported in the experimental literature for diffusion $(\sim 150-410 \mathrm{~kJ} \mathrm{~mol}^{-1})$ and show that oxygen embrittlement is a kinetically feasible mechanism of stress corrosion cracking [19].

### 3.4. Tuning work functions in CMOS gate stacks
The introduction of hafnium oxide as high-$k$ dielectric in complementary metal-oxide-semiconductor (CMOS) devices necessitates a change of the metallic gate material. The effective work function (EWF) of the metal needs to be tuned such that for n-doped devices (NMOS) the Fermi energy of the metal gate lines up closely with the bottom of the conduction band of the Si channel, while for p-type metal-oxide-semiconductor (PMOS) the Fermi level should be close to the valence band maximum. In other words the EWF needs to be tuned over the range of the band gap in Si with a high EWF for PMOS and a low EWF for NMOS devices.

Titanium nitride is being considered as one of the possible metallic gate materials. The tuning of EWF has posed considerable challenges [22, 23] and the understanding of the important effects is still incomplete despite substantial efforts. In this context $a b$ initio simulations provide unique insight into the relationship between chemical composition, structure, and work function. For such an analysis the key quantity is the electrostatic potential across the gate stack in the direction perpendicular to the interfaces. Similar to work function changes at surfaces, the formation of dipole layers due to charge transfer at the metal/oxide interface is critical in determining the EWF. For this reason, the $\mathrm{HfO}_{2} / \mathrm{TiN}$ interface and the role of the chemical composition and structure on interface dipole layers are of particular interest.

A model of the $\mathrm{HfO}_{2} / \mathrm{TiN}$ interface is constructed as follows. Hafnium oxide is represented by a film of crystalline monoclinic $\mathrm{HfO}_{2}$ with its most stable surface forming the interface. Despite the partially amorphous character of the oxide film in actual systems, a crystalline model is reasonable since the coordination of Hf in amorphous and annealed oxides is likely to reflect the key local structural aspects such as nearest-neighbor bond distances and bond angles as found in stable crystalline structures. A series of calculations on all low-index surfaces of monoclinic $\mathrm{HfO}_{2}$ shows that the stoichiometric $(\underline{1} 11)$ surface has the lowest surface energy. This surface is taken as substrate.

A systematic search of a good geometric match between the $\mathrm{HfO}_{2}(\underline{1} 11)$ surface and a $\mathrm{N}$-terminated $\mathrm{TiN}(111)$ surface leads to a computationally convenient supercell containing $12 \mathrm{Hf}$ atoms and $16 \mathrm{Ti}$ atoms per layer. The interface area in this supercell is $127.37 \AA^{2}$ with a mismatch between the two lattices of only $0.5 \%$ and $-1.9 \%$ of the in-plane lattice parameters and less than $4^{\circ}$ in the lattice angles. Using this geometry first a few layers of TiN in the sequence Ti-N$\mathrm{Ti}-\mathrm{N}$ are deposited on the oxide surface and the system is relaxed by $a b$ initio molecular dynamics simulated annealing. Subsequently additional layers of Ti and $\mathrm{N}$ with a capping layerof Ti are added, which results in a supercell containing 288 atoms of the composition $\mathrm{Hf}_{48} \mathrm{O}_{96} \mathrm{Ti}_{80} \mathrm{~N}_{64}$.

All atom positions of the entire system are relaxed using a conjugate gradient method with $a b$ initio forces computed with VASP [6] in the MedeA environment [7]. The electrostatic potential of this model is averaged in planes parallel to the interface, and smoothed using a macroscopic average [24]. This establishes a reference for the electrostatic potential across the interface.

Experimentally it has been found that annealing of $\mathrm{HfO}_{2} / \mathrm{TiN}$ stacks under an oxygen-containing atmosphere leads to incorporation of oxygen atoms in the TiN film and an increase of the EWF by up to $550 \mathrm{meV}$ [25]. Hence the first question to answer is the effect on the EWF when $\mathrm{N}$ atoms are replaced by $\mathrm{O}$ in the TiN. Specifically, $14 \%$ of the $\mathrm{N}$ atoms in the TiN film are replaced by $\mathrm{O}$, all atom positions are relaxed and the resulting planar-averaged electrostatic potential is compared with that of the reference system. As illustrated in figure 10, this modification of TiN has very little effect on the EWF and thus cannot be the cause of the observed work function increase.

Calculations reveal that modifications directly at the $\mathrm{HfO}_{2} / \mathrm{TiN}$ interface can have a major impact. This is illustrated by replacing one third of $\mathrm{O}$ atoms at the interface by $\mathrm{N}$ atoms (see panels (b) and (d) in figure 10). This modification causes an increase of $180 \mathrm{meV}$ in the EWF. At first this appears to be counter-intuitive. One would expect that the replacement of strongly electronegative atoms such as $\mathrm{O}$ by the less electronegative $\mathrm{N}$ atoms would lead to a decrease in the work function. This would be true for a surface of TiN, but not an interface, where one also has to consider the electronic rearrangement around Hf. In fact the replacement of $\mathrm{O}$ by $\mathrm{N}$ at the interface leads to changes of two opposing dipoles, namely that of $\mathrm{Hf}-\mathrm{X}$ and $\mathrm{X}-\mathrm{Ti}(\mathrm{X}=\mathrm{O}$ and $\mathrm{N})$. Hf atoms are larger and more polarizable than $\mathrm{Ti}$ atoms, so the changes in the $\mathrm{Hf}-$ $\mathrm{X}$ layers prevail and the net effect is an increase of the work function viewed from the TiN side of the stack.

This insight gained from the $a b$ initio calculations of these gate-stack materials provides guidelines for the optimization of the process conditions in the fabrication of these stacks. The control of the chemical composition at the interface at the scale of a single atomic layer is of critical importance while the EWF is rather insensitive to changes inside the TiN layer. This study also demonstrates that $a b$ initio calculations can now be performed on models which are sufficiently large to capture main features of actual devices such as metal-oxide interfaces.

In a metallic system the work function is correctly described by ground state theory such as DFT-GGA. However, the quantitative positioning of impurity states in a band gap requires a post-DFT approach. This is illustrated here for the energy of a neutral oxygen defect in the high- $k$ dielectric $\mathrm{HfO}_{2}$. Using a cubic $2 \times 2 \times 2 \mathrm{HfO}_{2}$ supercell as a model, a hybrid functional calculation with the so-called HSE06 potential [26] gives an energy band gap of $5.6 \mathrm{eV}$, which is reasonably close to the experimental value of $5.9 \mathrm{eV}$. In contrast the DFT-GGA band gap using the PBEsol potential [27] is only $3.9 \mathrm{eV}$. The

![](./images/811741440534118400_10.jpg)

Figure 10. Change of the average electrostatic potential across a $HfO_2$-TiN interface computed from the self-consistent charge density of a fully relaxed interface model. Panels (a) and (b) show the small effect caused by replacing N atoms by O atoms inside the TiN layer; (c) and (d) illustrate the pronounced effect of replacing 1/3 of O atoms directly at the interface by N atoms.

defect level in an oxygen vacancy in $HfO_2$ arises from dangling bonds localized at the Hf atom. These states are detached from the bottom of the conduction band and fall deeply into the band gap. While the GGA and the HSE06 calculations give a similar qualitative picture for the location of the defect state, the hybrid functional gives a much larger relative separation from the bottom of the conduction band compared with the GGA results as illustrated in figure 11. This comparison illustrates the importance of methods beyond the DFT-GGA level of theory, which provide quantitative values for excitation energies, while also providing guidelines for the interpretation of GGA results. In other words, carefully selected calculations at the higher level of theory enhance the value of standard GGA calculations by providing a basis to assess their applicability.

## 4. Assessment of present situation

The examples discussed here demonstrate that ab initio methods have matured to a stage where their contribution in addressing industrial issues is clearly evident. In the case of Zr grain boundary strength, calculations provide a systematic ranking over a range of alloying elements and impurities. Such a systematic picture is a valuable guide for metallurgists. It would be practically impossible to obtain an analogous dataset from experiment. In fact, experiments have been carried out to address the effect of impurities on zirconium alloys, but these efforts took many years and do not give a clear picture of the effect of each atomic species separately.

The computed values of diffusion coefficients for iodine on a Zr surface and for oxygen atoms in Ni bulk and grain boundaries represent quantitative materials property data, which are critical in the understanding of mechanisms related to environmentally-induced cracking. Hence the calculations are beneficial for improving the long-term reliability of products based on these materials. The last example related to work functions in CMOS gate stacks illustrates how calculation can help to focus experimental efforts on the important parameters of a system. All of the above cases are industrially valuable as they contribute to improved safety, better performance, and shorter development time.

These examples also show that expectations from ab initio materials simulations have to be realistic. They contribute to the research and development process by providing critical materials property data and by helping to focus experimental efforts through insight and understanding. However, it would be unrealistic to expect that a purely computational approach, starting with ab initio calculations and ending with quasi- continuum simulations of the microstructure evolution can simply replace experiments all together. The non-equilibrium character, which determines most of the processing and lifetime behavior of materials, contains far too many variables and degrees of freedom, which makes predictive modeling extremely challenging. Ab initio simulations combined with methods of statistical mechanics can only address a rather narrow section of the configurational space. On the other hand, with the predictive power and impressive generality of ab initio methods we have tremendous freedom to chose almost any

![](./images/811741440534118400_11.jpg)

Figure 11. Energy of a neutral oxygen defect level in cubic $HfO_2$ computed (a) at DFT-GGA level of theory with a PBEsol potential and (b) with the HSE06 hybrid functional. The defect is described by a $2 \times 2 \times 2$ supercell. The results obtained with the hybrid functional are in significantly better agreement with experiment compared with the simpler DFT-GGA calculations.

region of this configurational space. Hence the real challenge is the construction of relevant models and the selection of properties to be computed such that industrially relevant results are obtained.

While models such as a perfect $\Sigma7(0001)$ twist grain boundary of zirconium metal, a defect-free Zr(0001) surface with adsorbed iodine, or an interface between $HfO_2(\underline{111})$ and TiN(111) surfaces are idealized, they represent specific points in the materials design space, as is the case for other idealized systems like perfect three-dimensional crystals or isolated molecules in the gas phase. For such systems, although idealized, the computed materials properties are rather accurate. This applies to the change in the work of separation caused by different impurities and the change in the work function due to atomic substitutions. In fact, once the system is defined such as a free surface of Zr and an iodine molecule, the computed properties are often of similar accuracy as data which could be obtained from experiment. This is particularly striking in the case of interatomic distances or elastic properties. Of course there are uncertainties in the computed materials properties, but the same applies to experimental data. The remaining question is, if the chosen model is actually relevant, is a dense twist grain boundary really representative for a microstructure in a zirconium alloy? Is the diffusivity of iodine on a zirconium alloy really determined by diffusion on perfect Zr(0001) surfaces? Is the $HfO_2(\underline{111})$-TiN(111) interface really representative of this interface between the high-$k$ material and the metal gate?

The key question seems to have shifted from that of the intrinsic accuracy of the calculation to the viability of the model. Of course there are still a number of intrinsic challenges to be overcome as will be discussed below, but it seems that the central question of *ab initio*-based computational materials science is now fundamentally the same as in experiment. Is the chosen model representative? Any experimental test in the laboratory or in a test facility faces the same issue. Computational materials science has matured to a level where it has become an important and valuable partner to experiment.

## 5. Challenges and trends

One of the fundamental scientific challenges in the field of computational materials science is the accuracy of electronic structure calculations. For example, computations of the free energy of formation of a compound at the standard generalized-gradient approximation (GGA) level of theory can have absolute errors of several tens of kJ mol⁻¹. This is useful, but not good enough. Progress on this front is very difficult and leading research groups in the field of computational methods are pursuing this challenge. For example, the work in the group of Professor Kresse on the use of the random phase approximation for correlation as reported at the present workshop indicates that progress on this front can be achieved. However, the computational effort with current hardware is daunting and these types of calculations are far from routine applications. The dimension of this challenge can be appreciated by considering the number of decades it took to arrive at today's approaches. The roots of Hartree–Fock theory go back almost ninety years and those of density functional theory reach back to the middle of the past century, or even longer if we consider Thomas–Fermi theory. The so-called GW method was formulated over forty years ago, and quantum Monte Carlo has a history of many decades. It is realistic to expect that systematic improvements in the accuracy of electronic structure methods will be the topic of research for many decades to come. Furthermore, whenever major theoretical advances are achieved, the creation of well tested, comprehensive, and robust computer programs takes many years of additional work, thus further postponing routine applications.

A major shortcoming of standard DFT–GGA calculations is the insufficient description of weak interactions. For example, the computed interplanar distance in graphite is too large (or there is no bonding at all) and the structure of molecular crystals is not properly captured if the cohesive properties are dominated by van-der-Waals interactions. This problem is being addressed by a number of research groups using, for example, semi-empirical corrections [28] or by adding corrections derived from many-body perturbation theory [29]. The aspect of non-bonding interactions is very important for many organic and polymeric systems. Thus, the growing interest in organic materials for electronic and optical applications is likely to stimulate further developments in this area.

Application of the DFT–GGA method to alloy materials with partial or mixed lattice site occupancy is limited as the

method is not well developed to accurately treat partial/mixed site occupancies. Theoretical advances in this area are required to further open up the application of the method to materials of interest to various industries.

Notwithstanding these present limitations, many very useful materials properties can be computed with sufficient accuracy using the existing, well established levels of theory, notably gradient-corrected DFT. This includes properties such as elastic constants, phonon dispersions and the related thermodynamic functions such as heat capacity, temperature- dependent enthalpy and entropy, the coefficient of thermal expansion within the quasiharmonic approximation, and diffusion coefficients. These properties depend on relative changes of the total energy rather than its absolute value, thus leading to relatively highly accurate predictions.

A profound challenge is dealing with configurational complexity. For example, knowing that the structural relaxation and the cohesion at grain boundaries are fairly well described by DFT-GGA calculations, how can one obtain a statistically meaningful result for an actual microstructure, which includes a large range of different grain boundaries?

A particularly fascinating but also very difficult area is heterogeneous catalysis. Stimulated by the advances in experimental techniques such as photoemission spectroscopy with synchrotron radiation, scanning tunneling microscopy, surface-enhanced IR and Raman spectroscopy, and high- resolution electron microscopy, impressive progress has been achieved in the computational treatment of catalytic systems. For example, computational work on reactions in zeolites by Bucko [30] in the group of Professor Hafner at the University of Vienna has lead to remarkable understanding and quantitative predictions. However, the computational treatment of reactions on partially disordered surfaces faces the ubiquitous challenge of configurational complexity. The actual reactive surface with its active sites is structurally ill defined and changes with the various reaction conditions. Overlaid on this structural challenge is the difficulty to describe the kinetic evolution of the system. This implies knowledge of reaction mechanisms and an accurate description of the free energy along the reaction coordinates is needed.

Given the intellectual challenge and the technological importance of catalytic processes, it is quite likely that this will remain a very active research area combining advanced statistical concepts with large-scale ab initio calculations. Possibly, the low hanging fruits in this field are the structural and thermodynamic characterization of the various phases involved in a catalytic system as well as the elucidation of interfacial properties. Furthermore, the investigation of the elementary steps such as the dissociation of oxygen on catalytic surfaces [31] and the reduction mechanism of hydrodesulfurization catalysts [32] provide very valuable information, which is helpful in the development of industrial catalysts.

The challenges encountered in the modeling and simulation of heterogeneous catalytic systems are exacerbated in electrochemical systems, where solid/liquid interfaces and inorganic/organic systems within an external electrical field need to be considered.

These aspects stress the need for data reduction and coarse graining in the modeling approach. This is easily stated, but very difficult to realize due to the inherent discontinuities (such as phase transitions) in the behavior of chemical systems. Forcefield methods have proven to be very successful in the field of biopolymers and synthetic polymers, but their use in inorganic systems is seriously hampered by the importance of electronic structure effects. The development of generalized interatomic potentials such as the Gaussian approximation potentials [33] points into a promising direction. The basic idea is the mapping of interatomic energies and forces obtained from ab initio calculations onto a general interatomic potential. In fact, the current generation of so-called class 2 valence forcefields was developed in the 1980s by making extensive use of ab initio calculations (forces and second derivatives) of small molecules representing various functional groups occurring, for example, in proteins [34]. This approach has lead to very successful forcefields, which have been extensively used in the chemical and pharmaceutical industry during the past decades. It is quite likely that the development of quasi-classical potential functions will continue to represent a fascinating challenge requiring some novel ideas and approaches. In this context the 'Learn on the Fly' approach [35] appears to be promising, although the practical implementation and generalization is all but simple.

The ever growing power and cost-effectiveness of computer hardware will clearly help enormously in meeting the above listed challenges, hopefully sparking new computational concepts. In fact, in this context it is remarkable that practically all current electronic structure methods for molecules and solids use variational expansions in analytical or numerical basis sets, thus following a path chosen in the middle of the 20th century by pioneers such as Slater and Boys. Compact basis sets lead to relatively small matrices, which could be diagonalized on computers with modest sizes of memory. The introduction of large plane-wave basis sets using iterative evaluations of the eigenvalues in the 1980s represented a conceptual breakthrough. This happened at a time when the memory of computers grew substantially. It is likely that the availability of massive parallel computers with large memory will stimulate the development of new approaches and algorithms. Possibly, quantum Monte Carlo will see wider applications, provided that intrinsic challenges such as the fixed-node approximation can be overcome.

As the fields of computational physics, chemistry, and materials science mature, there will be a trend towards industrially supported software as we have witnessed in the field of structural analysis with finite element programs and in computational fluid dynamics. It is reasonable to expect that software developed by academic groups will continue to be the source of innovation in electronic structure methods, especially those beyond DFT. However, the growing industrial use of these methods in an engineering context will drive the need for commercial support. This trend can be expected to fuel further research and development as well as the education of a larger number of young scientists and engineers in the proper use of the computational tools.

## 6. Conclusions

Four examples have been discussed to demonstrate the successful industrial application of *ab initio* electronic structure methods to stress corrosion cracking in metal alloys and metal/insulator interfaces in semiconductor devices. Specifically, these examples were (i) the role of impurities on the strength of a zirconium grain boundary, (ii) the adsorption and diffusion of iodine on zirconium metal, (iii) the diffusion of oxygen atoms in the bulk and a grain boundary in nickel, and the tuning of the work function of a titanium nitride-hafnium oxide interface.

In each of these examples industrial value was manifest in a deeper understanding and the provision of quantitative materials property data. Those are the two major contributions of modeling and simulations. However, from an industrial point of view, four criteria need to be met for the successful application of *ab initio* methods, namely (i) the problem must be economically important, (ii) the model underlying the calculations must capture a relevant aspect of the system, (iii) the calculations need to provide understanding and quantitative materials properties with sufficient accuracy so that engineering decisions can be based upon the computed results, and (iv) the calculations need to be faster, cheaper, and safer than experiment.

In an industrial environment the cost of decisions is often large, for example in the selection of alloy compositions, irradiation testing, or the choice of a particular material in a microelectronic device. Thus, a deeper understanding and more comprehensive knowledge of materials properties can be key to prudent investments.

The confluence of sophisticated computational approaches and computer programs, the remarkable power and cost- effectiveness of today's computer hardware, and the growing industrial demand for better control of materials on the nanoscale have brought us to a point where *ab initio* calculations are becoming an integral part of industrial research and development. However, we are still in an early stage of this process. The confinement to relatively small systems, narrow parts of the configurational space, and limitations in accuracy still represent major challenges. Nevertheless, the bridge between fundamental research and engineering applications has been made and *ab initio* calculations for industrial materials engineering will continue to expand, thus helping to meet the many challenges of our industrialized society.

## References

[1] Dixon D A and Smart B E 1990 *Chem. Eng. Commun.* **98** 173

[2] Sidky P S 1998 *J. Nucl. Mater.* **256** 1-17

[3] Christensen M, Ballard J D, Angeliu T M, Vollmer J, Najafabadi R and Wimmer E 2009 *Proc. Top Fuel 2009 Conf. (Paris)* paper 2165
Christensen M, Angeliu T M, Ballard J D, Vollmer J, Najafabadi R and Wimmer E 2010 *J. Nucl. Mater.* at press

[4] Perdew J P, Ernzerhof M and Burke K 1996 *J. Chem. Phys.* **105** 9982

Ernzerhof M, Perdew J P and Burke K 1997 *Int. J. Quantum Chem.* **64** 285

[5] Blöchl P E 1994 *Phys. Rev. B* **50** 17953

[6] Kresse G and Hafner J 1993 *Phys. Rev. B* **47** 558
Kresse G and Furthmüller J 1996 *Comput. Mater. Sci.* **6** 15
Kresse G and Joubert J 1999 *Phys. Rev. B* **59** 1758

[7] MedeA version 2.3 2007 Materials Design, Inc., Angel Fire, NM, USA

[8] Sale F R 1969 *J. Less-Common Met.* **19** 53-62

[9] Horton R M and Kinney R L 1975 *Int. Symp. on Metal-Slag-Gas Reactions and Processes, Proc. Electrochemical Society* pp 317-27

[10] Balooch M and Olander D R 1983 *J. Electrochem. Soc.* **130** 151-7

[11] Yang T-T and Tsai C-H 1989 *J. Chin. Inst. Eng.* **12** 745-53

[12] Jónsson H, Mills H G and Jacobsen K W 1998 *Classical and Quantum Dynamics in Condensed Phase Simulations* ed B J Berne, G Cicotti and D F Coker (Singapore: World Scientific) p 385

[13] Wimmer E, Wolf W, Sticht J, Saxe P, Geller C B, Najafabadi R and Young G A 2008 *Phys. Rev. B* **77** 134305

[14] Legris A and Domain C 2005 *Phil. Mag.* **85** 589

[15] Cox B and Haddad R 1987 *Zirconium in the Nuclear Industry: 7th Int. Symp. ASTM STP 939* ed R B Adamson and L R P Van Swan (Philadelphia, PA: American Society for Testing and Materials) p 717

[16] Cox B 1990 *J. Nucl. Mater.* **172** 249

[17] Likhanskii V V and Matweev L V 2002 *Nucl. Eng. Des.* **213** 133

[18] Feuerstein H 1970 *ORNL-4543* Oak Ridge National Lab

[19] Scott P M 1999 *19th Int. Symp. on Environmental Degradation of Materials in Nuclear Power Systems-Water Reactors* (Newport Beach, CA)

[20] Young G A *et al* 2005 The mechanism and modeling of intergranular stress corrosion cracking of nickel-chromium-iron alloys exposed to high purity water *12th Int. Conf. on Environmental Degradation of Materials in Nuclear Power Systems (Salt Lake City, UT)*

[21] Parlinski K, Li Z Q and Kawazoe Y 1997 *Phys. Rev. Lett.* **78** 4063 and references therein

[22] Lee B H, Oh J, Tseng H H, Jammy R and Huff H 2006 *Mater. Today* **9** 32

[23] Gusev E P, Narayanan V and Frank M M 2006 *IBM J. Res. Dev.* **50** 387

[24] Peressi M, Baroni S, Baldereschi A and Resta A 1990 *Phys. Rev. B* **41** 12106

[25] Hinkle C L, Galatage R V, Chapman R A, Vogel E M, Alshareef H N, Freeman C, Wimmer E, Niimi H, Li-Fatou A, Shaw J B and Chambers J J 2010 *Appl. Phys. Lett.* **96** 103502

[26] Heyd J, Scuseria G E and Ernzerhof M 2006 *J. Chem. Phys.* **124** 219906

[27] Perdew J P, Ruzsinszky A, Csonka G I, Vydrov O A, Scuseria G E, Constantin L A, Zhou X and Burke K 2008 *Phys. Rev. Lett.* **100** 136406

[28] Grimme S 2006 *J. Comput. Chem.* **27** 1787

[29] Tuma C and Sauer J 2006 *Phys. Chem. Chem. Phys.* **8** 3955

[30] Bucko T 2008 *J. Phys.: Condens. Matter* **20** 064211

[31] Shan B, Kapur N, Hyun J, Wang L, Nicholas J B and Cho K 2009 *J. Phys. Chem. C* **113** 710

[32] Dinter N, Rusanen M, Raybaud P, Kasztelan S, da Silva P and Toulhoat H 2009 *J. Catal.* **267** 67

[33] Bartók A P, Payne M C, Kondor R and Csányi G 2009 arXiv:0910.1019v3 [physics.comp-ph]

[34] Maple J R, Dinur U and Hagler A T 1988 *Proc. Natl Acad. Sci.* **85** 5350

[35] Csányi G, Albaret T, Payne M C and De Vita A 2004 *Phys. Rev. Lett.* **93** 175503