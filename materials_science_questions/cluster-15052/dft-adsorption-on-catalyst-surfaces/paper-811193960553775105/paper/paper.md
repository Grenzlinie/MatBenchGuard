PCCP

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: P. Wu and B. Yang, Phys. Chem. Chem. Phys., 2016, DOI: 10.1039/C6CP02735K.

![](./images/811193960553775105_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/811193960553775105_2.jpg)

www.rsc.org/pccp

# Theoretical Insights into the Promotion Effect of Subsurface Boron for the
## Selective Hydrogenation of CO to Methanol over Pd Catalysts

Panpan Wu, Bo Yang*

School of Physical Science and Technology, ShanghaiTech University, Shanghai
201210, China

Email address: yangbo1@shanghaitech.edu.cn

## Abstract

The activity and selectivity of methanol synthesis from syngas has been studied for decades from both experimental and theoretical aspects. In this work, CO hydrogenation to methanol on both Pd(211) and subsurface boron-modified Pd(211) surfaces are investigated based on density functional theory calculations. Methane formation is considered as the main competitive reaction in the process and all the barriers and reaction energies involved are also calculated. We find that the modification of boron atoms will not alter the corresponding favored reaction pathways to produce methanol and methane on Pd(211), namely CO → CHO → CHOH → CH₂OH → CH₃OH for methanol formation and CO → COH → C → CH → CH₂ → CH₃ → CH₄ for methane formation. In addition, by using the two-step model to estimate the effective barriers for methanol and methane formation, the activity and selectivity for the products formation could be obtained and compared. It is found that the addition of boron atoms would significantly increase the activity of methanol formation while the activity of methane formation on clean and boron modified Pd surfaces are similar. Furthermore, we find that the hydrogenation of CO over clean Pd(211) will give high methane selectivity, whilst the boron modified Pd(211) mainly produces methanol. All these observed results can be explained by the electronic interaction between boron atoms and local Pd atoms through the lattice strain effect and alloying effect, resulting in the downshift of the d-band center of surface Pd away from the Fermi level. Finally, the extended Brønsted-Evans-Polanyi

(BEP) relationship is found between the energies of the transition states and the initial/final states for hydrogenation/dissociation reactions, which may provide significant insight to the activity and selectivity of the catalysts for methanol synthesis.

Key Words

DFT; CO; Hydrogenation; Activity; Selectivity; Methanol

## 1. Introduction

Due to the increasing demand of energy and the worse situation of global warming, it is imperative to find clean renewable liquid fuels. Methanol has been recognized as an ideal liquid fuel to alternate present petroleum. $^{1,2}$ In industry, methanol is synthesized from syngas, a mixture of $CO$, $CO_2$ and $H_2$, at high pressures (50 to 100 bar) and high temperatures (473 to 573K).$^{3}$ The industrial synthesis of methanol from syngas has been studied for decades, and the main reactions, regarding the hydrogenation of carbon monoxide, in this process might be,

$$CO+2H_2 \rightarrow CH_3OH,\quad \Delta H = -91kJ/mol$$

$$CO+3H_2 \rightarrow CH_4+H_2O,\quad \Delta H = -206kJ/mol$$

From the reactions above, it is obvious that methane generation is thermodynamically favored in the process. Therefore, methane is supposed to be the main by-product for methanol synthesis under the industrial reaction conditions. A large volume of investigations, from both aspects of scientific research and industry applications, have been carried out to improve the activity and selectivity of methanol formation from syngas conversion.

The majority of the studies are concentrated on active oxide, e.g. ZnO and $Al_2O_3$, supported Cu-based catalysts and the strong metal support interaction (SMSI) effect in the system,$^{4-6}$ and it was reported that the activity of CO hydrogenation proceeding to the formation of methanol on pure copper is poor.$^{7,8}$ Previous experimental studies dealing with syngas (either $CO+H_2$ or $CO/CO_2+H_2$) conversion suggested that promoted Pd could give better activity and selectivity than Pd for methanol synthesis process.$^{9-18}$ For example, it was shown that catalysts prepared by mixing palladium chloride solution with silica gel were both active and extremely selective for methanol synthesis.$^{17}$ Bell and co-workers reported the strong effect of different supports on the activity and selectivity of methanol formation over Pd.$^{13,18}$ In addition, Tamaru *et al.* revealed that Li-Pd or Na-Pd catalysts were not only very selective, but also active in producing methanol from $CO+H_2$ mixtures under mild conditions, whereas many similar Pd catalysts produce mainly methane.$^{9}$ Recently, using density functional

theory (DFT) calculations combined with microkinetic analysis, Nørskov group obtained the activity and selectivity maps of CO hydrogenation over transition metal (211) facets as a function of the binding energies of carbon and oxygen atoms. $^{19}$ In the selectivity map reported, the selectivity of methane over Pd is higher than that on Cu, which may be due to the much stronger adsorption of C atom and CO on Pd. In other words, if the adsorption of CO on Pd(211) surface can be weakened to some extent, the selectivity of methanol may be promoted.

In fact, extensive work has been conducted to improve the performance of the widely used palladium catalysts by adding light non-metal elements, such as carbon and boron atoms, as promoters. $^{20-23}$ By using DFT calculations, Yang *et al.* reported that over boron-modified palladium catalyst, where boron atoms prefer to locate at the subsurface octahedral sites of Pd, the selectivity of the hydrogenation of acetylene to ethylene could be promoted compared with that over pure Pd catalyst. $^{21}$ The authors further revealed that the electronic structure of Pd is modified upon boron doping and the adsorption strength of the desired product ethylene is weakened, which lowered the possibility of ethylene further hydrogenation. More recently, Tsang and co-workers prepared palladium nanoparticles with interstitial modification of boron atoms, and observed outclass performance on alkyne selective hydrogenation to desired products compared with the traditional Lindlar catalyst. $^{24}$ In addition, Nørskov *et al.* have studied the effect of boron modification on the catalytic property of Pd for formic acid decomposition reaction, $^{25}$ and found that the formation rate of hydrogen and $CO_2$ would be increased upon boron doping. Therefore, we can see that there is a high possibility to regulate both the activity and selectivity of Pd catalyst by doping with boron atoms.

It is widely accepted that the step sites over catalyst surfaces are the active sites for bond scission reactions, especially for CO and $N_2$ dissociation in methanation and ammonia synthesis processes, respectively, $^{26-31}$ which means methane formation is much easier at the step sites. Therefore, it is obvious that the performance of the whole Pd catalyst can be promoted simultaneously given that the selectivity of

methanol formation at the step sites is promoted. In the current work, we will use DFT calculations to study the hydrogenation of CO to methanol and methane on both Pd(211) and boron-modified Pd(211) (defined as Pd(211)-B in this paper) surfaces. Firstly, the stability of boron atoms at the subsurface sites of Pd(211) and Pd(111), as well as the B5 sites over Pd(211), will be compared at different boron coverages. Subsequently, all the possible reaction pathways from CO and hydrogen to methanol and methane, including the hydrogenation of CO, the dissociation of C-O bond and the further hydrogenation steps, will be investigated over both clean and boron modified Pd(211) surfaces. Upon obtaining the possible reaction pathways, the effective barriers for methanol and methane formation over Pd(211) and Pd(211)-B surfaces can be estimated, and the corresponding activity and selectivity will be compared. The electronic modification effect of boron doping will be discussed. Some general trends will be summarized and discussed in order to obtain some insights into the future catalyst design for methanol synthesis.

## 2. Computational Details
All the density functional calculations shown in this work were performed using the Vienna Ab-initio Simulation Package (VASP) code $^{32-34}$ with the projector-augmented wave (PAW) method. $^{35, 36}$ The generalized gradient approximation (GGA) was used with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional. $^{37}$ Twelve-layer and 1×4 slabs with the upmost six Pd layers relaxed during optimization were used to model the adsorption and reaction processes for Pd(211) surfaces. The slab was set with a vacuum to be at least 11 Å to make sure these processes take place on one side of the slabs. A 3×2×1 $k$-point grid generated with the Monkhorst-Pack scheme was used. An energy cutoff of 500 eV and convergence criteria of the force on each relaxed atoms below 0.05 eV/ Å were found to give converged results in the current work. Transition states were located with a constrained minimization method. $^{38-40}$ Adsorption energies were defined as:

$$
E_{\text{ad}} = E_{\text{total}} - (E_{\text{slab}} + E_{\text{g}}) \tag{1}
$$

Where $E_{\text{total}}$ is the energy of the system after adsorption $E_{\text{g}}$ is the energy of the gas-phase molecule, and $E_{\text{slab}}$ is the energy of slab. In addition, zero point energy (ZPE) corrections are included for all the energies.

In order to determine the location and coverage of boron atoms, the analysis of the average and differential adsorption energies of boron atoms at different sites of Pd(211)and Pd(111)was conducted (see Figure 1), where the average adsorption energies ($\Delta E_{\text{av}}$) were calculated from the equation,

$$
\Delta E_{\mathrm{av}}(N)=\frac{E_{\mathrm{slab}+\mathrm{N}^{*} \mathrm{ads}.}-E_{\mathrm{slab}}-N \cdot E_{\mathrm{ads}}}{N} \quad (2)
$$

and the differential adsorption energies ($\Delta E_{\text{diff}}$)were calculated from the equation,

$$
\Delta E_{\mathrm{diff}}(N)=\frac{\partial\left(N \cdot \Delta E_{\mathrm{av}}\right)}{\partial N} \quad (3)
$$

where $E_{\text{slab+N*ads}}$ is the energy of the system containing adsorbates with the number of $N$, $E_{\text{ads}}$ is the energy of adsorbate, i.e. one boron atom in the current work, which can be calculated from the equation,

$$
E_{\mathrm{ads}}=\frac{E_{B_{2} H_{6}(g)}-3 \cdot E_{H_{2}(g)}}{2} \quad (4)
$$

Where $E_{B_{2} H_{6}(g)}$ and $E_{H_{2}(g)}$ is the energy of the gaseous borane and hydrogen, respectively. The corresponding adsorption configurations of boron atoms at different sites of Pd(211) and Pd(111) with different coverages are shown in the electronic supplementary information (ESI) as Figure S1.

It is found from Figure 1 that the most stable adsorption site of boron atoms on Pd(211) is the octahedral subsurface site and the average adsorption energy is calculated to be lower than those at the four-fold B5 site at all the boron coverages studied. For comparison, the adsorption of boron atoms at the subsurface sites of Pd(111) is calculated as well. It turns out that, at 0.25 monolayer (ML) coverage, the corresponding adsorption energy of boron atoms at the octahedral subsurface site of Pd(111) is quite similar to the adsorption at both the subsurface sites and B5 sites of Pd(211). However, with the increasing of boron coverage, the average adsorption on

Pd(111) is becoming much less stable than those on Pd(211). Moreover, as shown in Figure 1(B), with the increase of boron coverage, the differential adsorption energy exhibits a sudden rise on Pd(111) while the situation on Pd(211) is gentler. Meanwhile, one can see that, at high boron coverages, the differential adsorption energies even become positive although the average adsorption energies are still negative, indicating that it is rather difficult for the subsurface sites of Pd(111) to be modified with boron atoms at such high coverages. In this work, we use the Pd(211)-octahedral model to investigate the effect of boron atoms on methanol synthesis from CO, in accordance with the previous study by Yang *et. al.*,²¹ and the structures of Pd(211) and Pd(211)-B surfaces are shown in Figure S2 in the ESI. This model contains twelve surface Pd atoms and four subsurface boron atoms, thus the boron coverage is around 0.33 ML, which is consistent with the experimentally measured coverage of boron on Pd surface (~ 0.3 ML).⁴¹

## 3. Results and Discussion

### 3.1 Scheme of Methanol and Methane Formation

As is discussed above, competing reactions for the hydrogenation of CO, including the formation of methanol and methane together with water, are considered in this work. Scheme 1 shows that $\text{CH}_3\text{OH}$ can be produced through the step-wise hydrogenation of the C or O atom of CO and the following intermediates. Meanwhile, the activation of C-O bond for CO methanation reactions can be divided into two types, the direct dissociation and the hydrogen-assisted dissociation,³¹ both possibilities will be considered here along with the subsequent hydrogenation reactions of C (CH) and O (OH) for the formation of $\text{CH}_4$ and $\text{H}_2\text{O}$.

### 3.2 Adsorption of the Reactants and Products

The most stable adsorption geometries of all the reactants, products and molecular intermediates involved in CO hydrogenation to methanol and methane, i.e. CO, H, $\text{CH}_3\text{OH}$, $\text{H}_2\text{O}$ and $\text{CH}_2\text{O}$, on both Pd(211) and Pd(211)-B surfaces, are represented in

Figure 2 and the corresponding adsorption energies are listed in Table1. It should be mentioned that the adsorption of methane is not considered in the current work due to the weak adsorption energy ($\sim$ 0 eV) obtained.

One can see from Figure 2 that CO prefers to stay at the three-fold hollow site at the step edge on Pd(211) with an adsorption energy of -1.95 eV, in agreement with the value(-1.97eV) reported in the literature. $^{42}$ Meanwhile, this site is also found to be favored for CO adsorption over Pd(211)-B, but the adsorption is weakened to -1.32 eV. For hydrogen atom, the most stable adsorption site is also the hollow edge site on both Pd(211) and Pd(211)-B and the adsorption energy is -0.48eV and -0.31eV, respectively. The adsorption of methanol at the top site of a Pd atom, which is the favorite adsorption site for methanol, over Pd(211) is calculated to be -0.36eV, similar to the value obtained on Pd(211)-B (top site, -0.34 eV). The most stable adsorption sites on these two surfaces for $\mathrm{H_2O}$ are also the top sites of Pd at the step edge, and the calculated adsorption energies are -0.22 eV and -0.20 eV for Pd(211) and Pd(211)-B, respectively. In addition, $\mathrm{CH_2O}$ prefers to stay at the bridge site at the step edge on both surfaces but with the adsorption energy of -0.84 and -0.59 eV over Pd(211) and Pd(211)-B, respectively. In general, Table 1 suggests that the adsorption energies, especially those of CO, H and $\mathrm{CH_2O}$, are reduced on Pd(211) by introducing boron atoms to the subsurface.

### 3.3 Reaction Pathways of Methanol formation
The elementary steps involved in possible reaction pathways of methanol formation on both Pd(211) and Pd(211)-B are listed in Table 2, along with the corresponding activation barriers and reaction energies. The optimal adsorption geometries of the intermediates and transition state structures of each elementary step are shown in Figures 3.

#### 3.3.1 Methanol formation on Pd(211)
As shown in Scheme 1, there are two possibilities for the hydrogenation of CO,

corresponding to the production of CHO and COH. At the transition state of CO+H→CHO, CO tends to leave the stable adsorption site (hollow site) to locate at the neighboring bridge site with a hydrogen atom at the adjacent top site of Pd atom, as shown in Figure 3. The reaction barrier is calculated to be 1.21 eV, which is lower than the previous theoretical barrier value on Pd(111) (1.48 eV),⁴² indicating that the step sites may have some promotion effects on this elementary step. CHO is then generated and sits at the bridge site of the step edge with hydrogen pointing to the lower terrace. In fact, the stability of this configuration is identical to that with hydrogen pointing to the upper terrace, and the energy difference is within the error of DFT calculations. Meanwhile, as mentioned above, the hydrogenation of CO can also produce COH through the addition of hydrogen to the oxygen moiety. At the transition state, CO prefers to locate at the hollow site with H atom adsorbed on the top of an adjacent Pd atom at the step edge. Then COH is found to situate at the three-fold hollow site at the step edge, as shown in Figure 3. This step features a higher reaction barrier of 1.79 eV, compared with that of CHO formation. Considering that the reaction energies of CHO and COH formation are identical, we find that it is much easier for the hydrogenation of CO to form CHO rather than COH at the first hydrogenation step kinetically.

Further hydrogenation of CHO leads to two species, i.e. CH₂O and CHOH. Regarding the reaction of CHO+H→CH₂O, at the transition state, CHO prefers to adsorb at the bridge site with H pointing to the upper terrace and H sits on the top of a neighboring Pd atom. As listed in Table 2, the formation of CH₂O needs to overcome a barrier of 1.04 eV. For the reaction CHO+H→CHOH, we find that the activation energy of this step is 0.55 eV, with a transition state configuration in which the hydrogen atom of CHO pointing to the upper terrace. It should be mentioned that we also searched the transition state configuration of CHO hydrogenation with H atom of CHO pointing to the lower terrace, and the activation energy is calculated to be 0.86 eV, which is higher than that of the former one. When comparing the reaction barriers of the competing reactions for CHO hydrogenation, it is obvious that the hydrogenation of

CHO tends to produce CHOH preferentially. In addition, CHOH can also be produced from the hydrogenation of COH, according to Scheme 1. The required barrier of this step is 0.98 eV, and is higher than that of CHO hydrogenation discussed above. Hence, it is more likely for CHOH to be produced by the further hydrogenation of CHO.

At this stage, $\text{CH}_2\text{O}$ and CHOH are formed after the second hydrogen atom addition. The next step of further hydrogenation of these two species could obtain $\text{CH}_3\text{O}$ and $\text{CH}_2\text{OH}$, where $\text{CH}_3\text{O}$ is formed by the hydrogenation of $\text{CH}_2\text{O}$ at the carbon atom, whilst $\text{CH}_2\text{OH}$ can be generated through both $\text{CH}_2\text{O}$ and CHOH hydrogenation. At the transition state of $\text{CH}_3\text{O}$ formation, $\text{CH}_2\text{O}$ locates at the bridge site of the step edge through C and O atoms with the hydrogen atom sitting at the top site of the same Pd atom with carbon, and the barrier that this step needs to overcome is 0.98 eV. The produced $\text{CH}_3\text{O}$ is found to stay at the bridge site, as shown in Figure 3. Regarding the two transition states for the elementary steps of $\text{CH}_2\text{OH}$ formation, i.e. $\text{CH}_2\text{O+H→CH}_2\text{OH}$ and $\text{CHOH+H→CH}_2\text{OH}$, the former one gives rise to a structure with $\text{CH}_2\text{O}$ adsorbs at the bridge site with a hydrogen atom approaching from the oxygen side to form the O-H bond, whilst the latter step has the transition state configuration with carbon and hydrogen atoms sitting at the same Pd atom, as shown in Figure 3(a), both configurations are similar to those reported in the literature for aldehyde hydrogenation. $^{43-47}$ The reaction barrier of $\text{CH}_2\text{O}$ and CHOH hydrogenation to produce $\text{CH}_2\text{OH}$ is 1.16 and 0.55 eV, respectively, as listed in Table 2.

On the basis of the hydrogenation steps discussed above, $\text{CH}_3\text{OH}$ will be finally generated after the addition of one hydrogen atom to$\text{CH}_3\text{O}$ or $\text{CH}_2\text{OH}$. As one can see from Figure 3, at the transition state, $\text{CH}_3\text{O}$ and H co-adsorb at adjacent sites, with methoxy at the bridge site and H at the top site and the barrier is 1.16 eV. Meanwhile, $\text{CH}_2\text{OH}$, sitting at the bridge site, can be hydrogenated by a hydrogen atom at the adjacent top site as well. The activation barrier is calculated to be 0.90 eV, which is lower than that of $\text{CH}_3\text{O}$ hydrogenation.

After the systematic and detailed study on the elementary steps of methanol formation on Pd(211), we can obtain the energy profiles of all the possible pathways included,


which are shown in Figure 4(a). The reaction pathways of methanol formation are summarized as: pathway I (CO→ COH → CHOH → CH₂OH → CH₃OH), pathway II (CO → CHO → CHOH → CH₂OH → CH₃OH), pathway III (CO → CHO → CH₂O → CH₂OH → CH₃OH) and pathway IV (CO →CHO → CH₂O → CH₃O → CH₃OH).

One can see from Figure 4(a) that pathway II shows the lowest energies for almost all the transition states and intermediate states compared with the other three pathways, indicating that this pathway should be the favored reaction route to produce CH₃OH on Pd(211). It should be mentioned that the mechanism of methanol formation on Pd(211) differs from that on Cu(211), where pathway IV is followed as reported in the literature.⁴⁸ Furthermore, on combining all the steps in pathway II and using the two-step approach reported before,²⁰,⁴⁹,⁵⁰ we estimate that the effective barrier of pathway II, calculated from the energy difference between the transition state with the highest energy and the adsorption state with the lowest energy in the energy profile, is as high as 2.97 eV, which is in accordance with the low methanol formation rate observed for Pd catalysts in previous experiments.¹⁰,¹⁸ It is worth pointing out that this two-step approach is a simplified description of real systems and generalizes the surface catalytic processes into two steps, namely dissociative adsorption and associative desorption, where the diffusion and the entropy of the surface adsorbates are not strictly considered. This approach has been shown successful for estimating the effective barriers in heterogeneous catalysis,²⁰⁻²³,⁴³⁻⁴⁵,⁵¹ and will also be used in the following part of this work.

### 3.3.2 Methanol formation on Pd(211)-B
An analogous study was undertaken regarding the formation of methanol on Pd(211)-B. The corresponding energetics are also listed in Table 2 and the configurations are shown in Figure 3(b). One can see that the adsorption and transition state structures for methanol formation over Pd(211)-B are similar to those over Pd(211), which will not be discussed in detail here, but it should be noted that the related energies differ remarkably.

On Pd(211)-B, for the formation of CHO from CO hydrogenation, the calculated activation energy is 1.03 eV, and is 0.18eV lower than that on Pd(211), whilst the formation barrier for COH is 1.89 eV, but is 0.10 eV higher than that on Pd(211). The optimized adsorbed CHO is found to stay at the bridge site with hydrogen pointing to the upper terrace, which is the same stable as that with hydrogen pointing to the opposite side. However, the formed COH prefers to bind at the four-fold B5 site on Pd(211)-B, which is different from that over Pd(211). Accordingly, at the transition state of COH formation on Pd(211)-B, CO sits at the four-fold B5 site with a hydrogen atom at the adjacent top site preferentially, as shown in Figure 3. We can find from the results above that the activity of CHO formation is promoted upon the modification of boron atoms, whilst the formation of COH is prevented.

Subsequently, the formed CHO and COH will be further hydrogenated as discussed above. The barrier of CHO+H→CH₂O and CHO+H→CHOH is 0.79 and 0.84 eV, respectively, and the corresponding reaction energies are 0.27 and 0.48 eV on Pd(211)-B. It is interesting to find that both the activation and reaction energies of CHOH formation are increased while those of CH₂O are decreased, but the geometries of the transition states are almost the same. Regarding the hydrogenation of COH, only CHOH can be produced and the barrier of this step on Pd(211)-B is similar to that on Pd(211). Again, due to the stable adsorption geometry of COH at the B5 site, the transition state configuration of this step on Pd(211)-B differs remarkably from that on Pd(211), as shown in Figure 3.

Moreover, on Pd(211)-B, the barrier of H+CH₂O→CH₃O is calculated to be 0.77 eV, which is 0.21 eV lower than that on Pd(211), but the reaction barrier of CH₂O+H→CH₂OH sees an increase of 0.11 eV upon boron doping, as shown in Table 2. When it comes to the reaction CHOH+H→CH₂OH, the barrier and reaction energies have been decreased to 0.49 and 0.04 eV, respectively, after the modification of boron atoms, compared with those on Pd(211). Although the energetic of this step on two surfaces are different, one can find from Figure 3 that all the transition state structures on Pd(211)-B are almost the same as those on Pd(211).

Finally, methanol will be produced via $\text{CH}_3\text{O}$ and $\text{CH}_2\text{OH}$ further hydrogenation. The barriers of these two reactions are 1.15 and 0.64 eV, respectively, and the corresponding reaction energies are both -0.30 eV, as one can see in Table 2.

Comparing the energetics listed in Table 2 for Pd(211) and Pd(211)-B, it is interesting to find that almost all the barriers and reaction energies of hydrogenation reactions taking place at the carbon moiety are decreased on Pd(211)-B, except for the barrier of CHO+H→CHOH, which features a slight increase of 0.09 eV. However, similar trend is not observed for the hydrogenation at the oxygen end.

This section provides a basis for the full description of methanol formation on Pd(211) and Pd(211)-B surfaces. Among the four pathways investigated for the generation of $\text{CH}_3\text{OH}$, pathway II, i.e. $\text{CO} \rightarrow \text{CHO} \rightarrow \text{CHOH} \rightarrow \text{CH}_2\text{OH} \rightarrow \text{CH}_3\text{OH}$, is found dominating on both surfaces as shown in Figure 4(b), which suggests the modification of Pd(211) with boron atoms will not change the reaction mechanism of methanol formation. It should be noticed from Figure 4(b) that the formation of $\text{CH}_3\text{O}$ through pathway IV and $\text{CH}_2\text{OH}$ through pathway II are competing in the system. However, the barrier of the further hydrogenation of $\text{CH}_3\text{O}$ to produce methanol is 0.51 eV higher than that of $\text{CH}_2\text{OH}$ hydrogenation, as one can see in Table 2, we hereby consider $\text{CH}_3\text{O}$ as a spectator on the surface. Moreover, the effective barrier of pathway II is even reduced by about 1.00 eV to 1.98 eV upon boron atoms doping, indicating that the activity of methanol formation might be largely enhanced.

### 3.4 Reaction Pathways of Methane Formation

#### 3.4.1 C-O bond dissociation on Pd(211) and Pd(211)-B

The activation of CO is the key step of CO methanation, thus the C-O bond dissociation will be discussed in detail first in this section. As mentioned in section 3.1, two types of C-O bond scission possibilities are taken into consideration, i.e. direct dissociation and hydrogen-assisted dissociation. The structures of the C-O bond dissociation transition states are shown in Figure 5(b) and the calculated barriers and reaction energies are listed in Table 3 for both Pd(211) and Pd(211)-B surfaces.

For the direct dissociation CO→C+O, the barrier and the reaction energy is calculated to be 2.76 and 1.48 eV on Pd(211), respectively, while on Pd(211)-B the values change to 3.23 and 2.23 eV, respectively. Hence, it is obvious that the direct dissociation of CO is quite difficult to proceed on Pd(211) and the introduction of boron atoms will further suppress the process. After the dissociation, C atom is found to sit at the B5 site and O atom prefers the hollow site at the step edge.

One of the hydrogen-assisted C-O bond dissociation is via the CHO intermediate. The first step of this manner is CO+H→CHO, corresponding energetics and geometries have been discussed in the first step of methanol formation and will not be introduced in detail here. The second step is CHO→CH+O, for which the obtained barrier and reaction energy is 1.51 and 0.80 eV on Pd(211), respectively. In comparison, on Pd(211)-B, an increase to 2.11 and 1.55 eV is observed for the reaction barrier and reaction energy, respectively. As shown in Figure 3, at the initial state, CHO prefers to stay at the bridge site on both surfaces. Whereas at the transition state, it moves to the nearest B5 site on Pd(211) and Pd(211)-B. After the reaction, CH stays at the B5 site and O adsorbs at the neighboring hollow site.

Another possibility of hydrogen-assisted C-O bond dissociation is through the COH intermediate. After the formation of COH, the reaction of COH→C+OH sees a barrier of 1.34 and 1.14 eV on Pd(211) and Pd(211)-B, respectively, indicating that the activity of C-O bond dissociation via COH might be similar on both surfaces. However, the structures of the transition states are quite different, as shown in Figure 5(b), which may be attributed to the different adsorption configurations of COH on these two surfaces. It should be mentioned that other hydrogen-assisted C-O bond dissociation pathways, including the dissociation of CHOH, CH₂O, CH₂OH and CH₃O, are also considered in this work and the activation energies and reaction energies are listed in Table S1. Although the dissociation of CH₂OH seem to have accessible barriers on both surfaces, as one can see in Table S1, the corresponding hydrogenation barriers of CH₂OH are lower, indicating that the hydrogenation of CH₂OH is more likely to happen on both surfaces.

With all the energies of CO bond activation pathways obtained, the energy profiles are concluded according to the elementary reactions considered, as shown in Figure 5(a). For clarity, we only present the energy profiles of the direct dissociation pathway and the C-O bond dissociation of CHO and COH in Figure 5(a), and those of all the possible pathways are presented in Figure S3 of the ESI, along with the corresponding transition state configurations. It is clear in Figure 5(a) and Figure S3 that the CO direct dissociation is rather difficult to proceed because of the high barrier on both surfaces. Furthermore, C-O bond breaking via COH pathway is found more favorable on both Pd(211) and Pd(211)-B, which is consistent with the previous theoretical study.⁵²

### 3.4.2 Methane and water formation on Pd(211) and Pd(211)-B
Once the reactant CO is activated, a sequential addition of hydrogen atoms to the produced C (CH) and O (OH) can lead to CH₄and H₂Oeventually. The elementary reactions and relative energies of methane and water formation are also listed in Table 3. For the formation of methane, the corresponding adsorption and transition state structures on Pd(211) and Pd(211)-B are shown in Figure 6(b). Table 3 suggests that the activation barriers of the further hydrogenation of carbon decrease from Pd(211) to Pd(211)-B, and the elementary reactions are becoming more exothermic. The effective barriers for C (CH) hydrogenation to produce methane on Pd(211) and Pd(211)-B are 1.52 (1.00) and 0.96 (0.82) eV, respectively.

On the other hand, regarding the formation of H₂O, the adsorption geometries of O and OH and the transition state structures proceeding to H₂O are similar on both surfaces, as shown in Figure 7. The reaction barriers of OH and H₂O formation are 1.22 and 1.16 eV on Pd(211), respectively, whilst on Pd(211)-B, the values are decreased to 0.90 and 1.06 eV, respectively. Moreover, the reaction energies of the two reactions are decreased by 0.56 and 0.39 eV, respectively, upon boron doping. Therefore, one can see that CH₄ and H₂O are more readily produced from the hydrogenation of C (CH) and O (OH) on Pd(211)-B from both kinetic and

thermodynamic aspects.

While comparing the effective barriers for C-O dissociation with those for the following hydrogenation reactions, one can find that methane formation process is determined by C-O activation on both surfaces. Therefore, the effective barrier for methane formation on Pd(211) and Pd(211)-B should be 2.47 and 2.22 eV, respectively. As discussed above, the reaction pathway $\ce{CO -> COH -> C -> CH -> CH2 -> CH3 -> CH4}$ is favored on both surfaces, indicating that the modification with subsurface boron atoms over Pd(211) will not change the reaction mechanism for methane formation. Moreover, the effective barrier of the favored pathway on Pd(211)-B is similar with that on Pd(211), declaring that the activity of methane formation is identical on these surfaces.

### 3.5 Selectivity of Methanol Formation
Based on the results in sections 3, we can see that the effective barriers of the preferred pathways of methanol and methane formation on Pd(211) is 2.97 and 2.47 eV, respectively, while on Pd(211)-B the corresponding values are 1.98 and 2.22 eV, and higher effective barriers will give rise to lower production rates. According to the literature,¹⁹ pure Pd is not a good catalyst for methanol synthesis, which is consistent with the high effective barrier obtained in our work. One can see that the activity of methanol formation is significantly promoted over Pd(211)-B compared with Pd(211), since the effective barrier is strongly decreased by 0.99 eV, while the promotion effect for methane formation is marginal after the modification with boron atoms at the subsurface of Pd(211). Moreover, it is obvious that methane is produced selectively on Pd(211) whereas methanol is the selective product on Pd(211)-B. It should be mentioned that our calculation results are consistent with the reported experimental observations that Pd possess high methane selectivity towards CO hydrogenation.⁹
The above results suggest that, by introducing boron atoms at the subsurface sites of Pd(211) surface, the activity and selectivity of methanol might be increased over methane for the hydrogenation of CO. However, the formation of methane is

thermodynamically favored in this process, when the temperature is getting higher,
the adsorption of the gaseous molecules will be weakened due to the entropic effects.
More importantly, the reaction free energy for methanol formation will become less
negative. In other words, with the increase of temperature, the formation of methanol
will be inhibited and the selectivity of methanol will decrease.

### 3.6 General Discussion

*Lattice strain effect and alloying effect* According to Yang et al.,$^{21}$ the $d$-band center
of Pd(211) would be down-shifted after boron doping, which could be considered as
the reason for the weaker adsorption of reaction intermediates observed in Section 3.2.
It is acknowledged that the $d$-band center of a given type of transition metal can be
tuned in different ways, while in this case where Pd(211) is modified with subsurface
boron atoms, lattice straining and alloying would be considered dominating.
Regarding the lattice strain effect, as shown in Figure S2 in the ESI, the metal-metal
bond lengths in the surface Pd rows that along the step edge direction are almost
unchanged after boron modification, while those between the rows on the surface
have been stretched from 2.75 (2.73) to 2.91 (2.77) Å. The expansion of lattice is
expected to shift up the $d$-band center of Pd and hence increase the interaction
between adsorbates and catalyst surface.$^{53}$ A schematic view of this change is shown
in Figure 8, where the $d$-band center of pure Pd has been shifted up from $\varepsilon_{\rm d}$ to $\varepsilon_{\rm d}'$, and
increased by $\delta\varepsilon_{\rm d}'$. The alloying effect will possibly broaden the $d$-band of Pd due to
the interaction with the $p$ states of boron atoms and thus lead to a downshift of the
$d$-band center, which would weaken the interaction between adsorbates and surface
atoms.$^{24, 54}$ One can see in Figure 8 that a downshift of $\delta\varepsilon_{\rm d}''$ of the $d$-band center
makes the energy of $d$-band center of Pd(211) decreased to $\varepsilon_{\rm d}''$ after the modification
of boron.

However, making a comparison with the calculated results obtained in the current
work, the lattice strain effect is contradicted to the fact that the adsorption energies of
most of the reaction intermediates are reduced. In fact, previous study reported that,

over Pd(111) surface, the influence of alloying effect override that of lattice stretch and hence the $d$-band center is overall downshifted by the introduction of boron atoms.$^{24}$ Although we are focusing on the less closed-packed Pd(211) surface and the bond distance between Pd atoms is more likely to be stretched, a similar conclusion could be drawn here that the effect of alloying surpasses that of lattice strain, resulting in the weakened adsorption energies of the reaction intermediates.

Extended Brønsted-Evans-Polanyi (BEP) relationship Having obtained the explanation on the weaker adsorption of surface intermediates observed, we further studied the trend of transition state energies. Previous theoretical study revealed that a linear behavior, extended from the traditional BEP relation,$^{55}$ exists when the energies of the transition states of elementary steps are plotted against the energies of the corresponding initial/final states.$^{56,57}$ All the elementary reactions involved in this work can be divided into three categories, i.e. hydrogenation of the carbon atom (C-H) in $\mathrm{CH_xO}$ (x=0~3) and $\mathrm{CH_x}$ (x=0~3), hydrogenation of the oxygen atom (O-H) in $\mathrm{CH_xO}$ (x=0~3) and $\mathrm{OH_x}$ (x=0~1), as well as direct C-O bond dissociation and hydrogen-assisted C-O bond dissociation of $\mathrm{CH_xO}$ (x=0~3). As shown in Figure 9, it is clear that a general linear relationship is found between the energy of transition state and the initial state for hydrogenation reactions or the final state for bond dissociation reactions, respectively, for both Pd(211) and Pd(211)-B surfaces. This kind of relationship may be originated from the geometric similarity between the initial (final) state and the transition state, where initial (final)-state-like transition states can be recognized as early (late) transition states.$^{58}$ In addition, it could be seen from our results that the weaker adsorption of the reactants over Pd(211)-B will give higher activity for methanol formation, which further proves that the activity of Pd lies in the strong adsorption side of the corresponding volcano curve, in accordance with the previous result.$^{19}$

### 4. Conclusions

In summary, we have examined the competitive pathways for methanol and methane

formation from CO hydrogenation on Pd(211) and Pd(211)-B surfaces by using a plane-wave DFT method. It is found that the formation of methanol on both surfaces prefers the path: CO→CHO→CHOH→CH₂OH→CH₃OH, but with promoted activity on Pd(211)-B. Meanwhile, the formation of methane is via CO→COH→C→CH →CH₂→CH₃→CH₄ on Pd(211) and Pd(211)-B and the dissociation of C-O bond is rate-determining on both surfaces. The effective barrier of methanol formation obtained is higher than that of methane on Pd(211), whereas, on Pd(211)-B, the formation of methanol is preferred, suggesting that the selectivity of methanol is promoted with the modification of boron atoms. All these observed results can be attributed to the alloying effect of boron doping, which shifts the location of d-band center of the surface Pd down from the Fermi level, and the adsorption of the reaction intermediates is weakened. Since Pd(211) lies in the strong adsorption side of the volcano curve for methanol formation, the weaker adsorption would give rise to higher methanol formation rates. Moreover, the extended Brønsted-Evans-Polanyi (BEP) relationship is found between the energy of transition state and the initial/final state of the elementary steps over both surfaces, which may provide a prediction for the activity and selectivity of the catalysts and facilitate the future catalyst design for methanol synthesis.

Acknowledgement

B.Y. would like to thank ShanghaiTech University for the start-up funding support.

References

1. G. A. Olah, *Angew. Chem. Int. Ed.*, 2005, **44**, 2636-2639.

2. G. A. Olah, G. K. S. Prakash and A. Goeppert, *J. Am. Chem. Soc.*, 2011, **133**, 12881-12898.

3. K. C. Waugh, *Catal. Today*, 1992, **15**, 51-75.

4. S. Fujita, M. Usui, H. Ito and N. Takezawa, *J. Catal.*, 1995, **157**, 403-413.

5. M. Behrens, F. Studt, I. Kasatkin, S. Kühl, M. Hävecker, F. Abild-Pedersen, S.

Zander, F. Girgsdies, P. Kurr, B.-L. Kniep, M. Tovar, R. W. Fischer, J. K. Nørskov and R. Schlögl, *Science*, 2012, **336**, 893-897.

6. J. Sun, S. Wan, F. Wang, J. Lin and Y. Wang, *Ind. Eng. Chem. Res.*, 2015, **54**, 7841-7851.

7. G. R. Sheffer and T. S. King, *J. Catal.*, 1989, **116**, 488-497.

8. G. R. Sheffer and T. S. King, *J. Catal.*, 1989, **115**, 376-387.

9. Y. Kikuzono, S. Kagami, S. Naito, T. Onishi and K. Tamaru, *Faraday Discuss. Chem. Soc.*, 1981, **72**, 135-143.

10. Y. A. Ryndin, R. F. Hicks, A. T. Bell and Y. I. Yermakov, *J. Catal.*, 1981, **70**, 287-297.

11. F. Fajula, R. G. Anthony and J. H. Lunsford, *J. Catal.*, 1982, **73**, 237-256.

12. J. M. Driessen, E. K. Poels, J. P. Hindermann and V. Ponec, *J. Catal.*, 1983, **82**, 26-34.

13. J. S. Rieck and A. T. Bell, *J. Catal.*, 1985, **96**, 88-105.

14. A. F. Gusovius, T. C. Watling and R. Prins, *Appl. Catal. A Gen.*, 1999, **188**, 187-199.

15. N. Koizumi, X. Jiang, J. Kugai and C. Song, *Catal. Today*, 2012, **194**, 16-24.

16. A. Ota, E. L. Kunkes, I. Kasatkin, E. Groppo, D. Ferri, B. Poceiro, R. M. Navarro Yerga and M. Behrens, *J. Catal.*, 2012, **293**, 27-38.

17. M. L. Poutsma, L. F. Elek, P. A. Ibarbia, A. P. Risch and J. A. Rabo, *J. Catal.*, 1978, **52**, 157-168.

18. R. F. Hicks and A. T. Bell, *J. Catal.*, 1985, **91**, 104-115.

19. A. J. Medford, A. C. Lausche, F. Abild-Pedersen, B. Temel, N. C. Schjodt, J. K. Norskov and F. Studt, *Top. Catal.*, 2014, **57**, 135-142.

20. B. Yang, R. Burch, C. Hardacre, G. Headdock and P. Hu, *J. Catal.*, 2013, **305**, 264-276.

21. B. Yang, R. Burch, C. Hardacre, P. Hu and P. Hughes, *J. Phys. Chem. C*, 2014, **118**, 3664-3671.

22. B. Yang, R. Burch, C. Hardacre, P. Hu and P. Hughes, *J. Phys. Chem. C*, 2014,

118, 1560-1567.

23. B. Yang, R. Burch, C. Hardacre, P. Hu and P. Hughes, *Surf. Sci.*, 2016, **646**, 45-49.

24. C. W. A. Chan, A. H. Mahadi, M. M.-J. Li, E. C. Corbos, C. Tang, G. Jones, W. C. H. Kuo, J. Cookson, C. M. Brown, P. T. Bishop and S. C. E. Tsang, *Nature Commun.*, 2014, **5**.

25. J. S. Yoo, Z.-J. Zhao, J. K. Nørskov and F. Studt, *ACS Catal.*, 2015, **5**, 6579-6586.

26. C. Egawa, S. Naito and K. Tamaru, *Surf. Sci.*, 1985, **154**, 706-707.

27. E. Shincho, C. Egawa, S. Naito and K. Tamaru, *Surf. Sci.*, 1985, **149**, 1-16.

28. G. Rupprechter, V. V. Kaichev, H. Unterhalt, M. Morkel and V. I. Bukhtiyarov, *Appl. Surf. Sci.*, 2004, **235**, 26-31.

29. S. Shetty, A. P. J. Jansen and R. A. van Santen, *J. Phy. Chem. C*, 2008, **112**, 14027-14033.

30. A. L. Kustov, A. M. Frey, K. E. Larsen, T. Johannessen, J. K. Nørskov and C. H. Christensen, *Appl. Catal. A Gen.*, 2007, **320**, 98-104.

31. S. Shetty, A. P. J. Jansen and R. A. van Santen, *J. Am. Chem. Soc.*, 2009, **131**, 12874-12875.

32. G. Kresse and J. Hafner, *Phy. Rev. B*, 1994, **49**, 14251-14269.

33. G. Kresse and J. Furthmüller, *Comp. Mater. Sci.*, 1996, **6**, 15-50.

34. G. Kresse and J. Furthmüller, *Phy. Rev. B*, 1996, **54**, 11169-11186.

35. P. E. Blöchl, *Phy. Rev. B*, 1994, **50**, 17953-17979.

36. G. Kresse and D. Joubert, *Phys. Rev. B*, 1999, **59**, 1758-1775.

37. J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

38. A. Alavi, P. Hu, T. Deutsch, P. L. Silvestrelli and J. Hutter, *Phys. Rev. Lett.*, 1998, **80**, 3650-3653.

39. Z.-P. Liu and P. Hu, *J. Am. Chem. Soc.*, 2003, **125**, 1958-1967.

40. A. Michaelides, Z. P. Liu, C. J. Zhang, A. Alavi, D. A. King and P. Hu, *J. Am.*

*Chem. Soc.*, 2003, **125**, 3704-3705.

41. M. Krawczyk and W. Palczewska, *Vacuum*, 1995, **46**, 1151-1153.

42. S. Lin, J. Ma, X. Ye, D. Xie and H. Guo, *J. Phy. Chem. C*, 2013, **117**, 14667-14676.

43. B. Yang, X.-Q. Gong, H.-F. Wang, X.-M. Cao, J. J. Rooney and P. Hu, *J. Am. Chem. Soc.*, 2013, **135**, 15244-15250.

44. B. Yang, D. Wang, X.-Q. Gong and P. Hu, *Phys. Chem. Chem. Phys.*, 2011, **13**, 21146-21152.

45. B. Yang, X.-M. Cao, X.-Q. Gong and P. Hu, *Phys. Chem. Chem. Phys.*, 2012, **14**, 3741-3745.

46. H. G. Manyar, B. Yang, H. Daly, H. Moor, S. McMonagle, Y. Tao, G. D. Yadav, A. Goguet, P. Hu and C. Hardacre, *ChemCatChem*, 2013, **5**, 506-512.

47. H. G. Manyar, R. Morgan, K. Morgan, B. Yang, P. Hu, J. Szlachetko, J. Sa and C. Hardacre, *Catal. Sci. Technol.*, 2013, **3**, 1497-1500.

48. F. Studt, F. Abild-Pedersen, J. B. Varley and J. K. Nørskov, *Catal. Lett.*, 2012, **143**, 71-73.

49. J. Cheng, P. Hu, P. Ellis, S. French, G. Kelly and C. M. Lok, *J. Phy. Chem. C*, 2008, **112**, 1308-1311.

50. B. Yang, R. Burch, C. Hardacre, G. Headdock and P. Hu, *ACS Catal.*, 2014, **4**, 182-186.

51. B. Yang, R. Burch, C. Hardacre, G. Headdock and P. Hu, *ACS Catal.*, 2012, **2**, 1027-1032.

52. A. C. Lausche, A. J. Medford, T. S. Khan, Y. Xu, T. Bligaard, F. Abild-Pedersen, J. K. Nørskov and F. Studt, *J. Catal.*, 2013, **307**, 275-282.

53. M. Mavrikakis, B. Hammer and J. K. Nørskov, *Phys. Rev. Lett.*, 1998, **81**, 2819-2822.

54. J. R. Kitchin, J. K. Nørskov, M. A. Barteau and J. G. Chen, *J. Chem. Phys.*, 2004, **120**, 10240-10246.

55. J. K. Nørskov, T. Bligaard, A. Logadottir, S. Bahn, L. B. Hansen, M.

Bollinger, H. Bengaard, B. Hammer, Z. Sljivancanin, M. Mavrikakis, Y. Xu, S. Dahl and C. J. H. Jacobsen, *J. Catal.*, 2002, **209**, 275-278.

56. R. García-Muelas, Q. Li and N. López, *ACS Catal.*, 2015, **5**, 1027-1036.

57. D. Loffreda, F. Delbecq, F. Vigné and P. Sautet, *Angew. Chem. Int. Ed.*, 2009, **48**, 8978-8980.

58. R. A. v. Santen, M. Neurock and S. G. Shetty, *Chem. Rev.*, 2010, **110**, 2005-2048.

![](./images/811193960553775105_3.jpg)

Scheme 1. Network of possible reaction paths of CO hydrogenation to produce methanol and methane. The solid line and the dash line represent elementary reactions and multistep hydrogenation reactions, respectively.

Table 1. Adsorption energies (in eV) of CO, H, CH₃OH, H₂O and CH₂O on both Pd(211) and Pd(211)-B.

<table>
  <thead>
    <tr>
      <th></th>
      <th>CO</th>
      <th>H</th>
      <th>CH₃OH</th>
      <th>H₂O</th>
      <th>CH₂O</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pd(211)</td>
      <td>-1.95</td>
      <td>-0.48</td>
      <td>-0.36</td>
      <td>-0.21</td>
      <td>-0.84</td>
    </tr>
    <tr>
      <td>Pd(211)-B</td>
      <td>-1.32</td>
      <td>-0.31</td>
      <td>-0.34</td>
      <td>-0.20</td>
      <td>-0.59</td>
    </tr>
  </tbody>
</table>

Table 2. Calculated activation energies ($E_\mathrm{a}$) and reaction energies ($\Delta E$) of the elementary reactions of methanol formation on Pd(211) and Pd(211)-B, ZPE corrections are included. The elementary reactions in the preferred reaction pathway for methanol formation are shown in bold.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">Pd(211)</th>
<th colspan="2">Pd(211)-B</th>
</tr>
<tr>
<th>$E_\mathrm{a}$(eV)</th>
<th>$\Delta E$(eV)</th>
<th>$E_\mathrm{a}$(eV)</th>
<th>$\Delta E$(eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>CO*+H*→CHO*+*</b></td>
<td>1.21</td>
<td>1.20</td>
<td>1.03</td>
<td>0.81</td>
</tr>
<tr>
<td>CO*+H*→COH*+*</td>
<td>1.79</td>
<td>1.12</td>
<td>1.89</td>
<td>1.08</td>
</tr>
<tr>
<td>CHO*+H*→CH₂O*+*</td>
<td>1.04</td>
<td>0.61</td>
<td>0.79</td>
<td>0.27</td>
</tr>
<tr>
<td><b>CHO*+H*→CHOH*+*</b></td>
<td>0.55</td>
<td>0.28</td>
<td>0.84</td>
<td>0.48</td>
</tr>
<tr>
<td>COH*+H*→CHOH*+*</td>
<td>0.98</td>
<td>0.36</td>
<td>1.07</td>
<td>0.22</td>
</tr>
<tr>
<td>CH₂O*+H*→CH₃O*+*</td>
<td>0.98</td>
<td>0.46</td>
<td>0.77</td>
<td>0.25</td>
</tr>
<tr>
<td>CH₂O*+H*→CH₂OH*+*</td>
<td>1.16</td>
<td>0.27</td>
<td>1.27</td>
<td>0.25</td>
</tr>
<tr>
<td><b>CHOH*+H*→CH₂OH*+*</b></td>
<td>0.84</td>
<td>0.60</td>
<td>0.49</td>
<td>0.04</td>
</tr>
<tr>
<td>CH₃O*+H*→CH₃OH*+*</td>
<td>1.16</td>
<td>0.08</td>
<td>1.15</td>
<td>-0.30</td>
</tr>
<tr>
<td><b>CH₂OH*+H*→CH₃OH*+*</b></td>
<td>0.90</td>
<td>0.27</td>
<td>0.64</td>
<td>-0.30</td>
</tr>
</tbody>
</table>

Table 3. Calculated activation energies ($E_\text{a}$) and reaction energies ($\Delta E$) of the elementary reactions of methane formation on Pd(211) and Pd(211)-B, ZPE corrections are included.

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Pd(211)</th>
      <th colspan="2">Pd(211)-B</th>
    </tr>
    <tr>
      <th></th>
      <th>$E_\text{a}$(eV)</th>
      <th>$\Delta E$(eV)</th>
      <th>$E_\text{a}$(eV)</th>
      <th>$\Delta E$(eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CO*+*→C*+O*</td>
      <td>2.76</td>
      <td>1.48</td>
      <td>3.20</td>
      <td>2.23</td>
    </tr>
    <tr>
      <td>CHO*+*→CH*+O*</td>
      <td>1.51</td>
      <td>0.80</td>
      <td>2.11</td>
      <td>1.55</td>
    </tr>
    <tr>
      <td>COH*+*→C*+OH*</td>
      <td>1.34</td>
      <td>-0.10</td>
      <td>1.14</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>C*+H*→CH*+*</td>
      <td>0.91</td>
      <td>0.52</td>
      <td>0.91</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>CH*+H*→CH₂*+*</td>
      <td>0.89</td>
      <td>0.39</td>
      <td>0.82</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>CH₂*+H*→CH₃*+*</td>
      <td>0.60</td>
      <td>0.15</td>
      <td>0.39</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <td>CH₃*+H*→CH₄(g)+*</td>
      <td>0.42</td>
      <td>0.01</td>
      <td>0.15</td>
      <td>-0.69</td>
    </tr>
    <tr>
      <td>O*+H*→OH*+*</td>
      <td>1.22</td>
      <td>-0.45</td>
      <td>0.90</td>
      <td>-1.01</td>
    </tr>
    <tr>
      <td>OH*+H*→H₂O*+*</td>
      <td>1.16</td>
      <td>0.20</td>
      <td>1.06</td>
      <td>-0.19</td>
    </tr>
  </tbody>
</table>

![](./images/811193960553775105_4.jpg)

Figure 1. (A) Average adsorption energies and (B) differential adsorption energies of boron at different sites of the palladium subsurface (black square: adsorption at the octahedral subsurface site of Pd(211), Pd(211)-Octa; red circle: adsorption at the 4-fold B5 site of Pd(211), Pd(211)-B5; blue triangle: adsorption at the octahedral subsurface site of Pd(111), Pd(111)-Octa). The adsorption energies of boron shown here are with respect to the decomposition of gaseous $B_2H_6$ to adsorbed boron and gaseous $H_2$.

![](./images/811193960553775105_5.jpg)

Figure 2. Adsorption structures of CO, H, CH₃OH, H₂O and CH₂O on Pd(211) (above)
and Pd(211)-B (below). The Pd, C, H, O and B atoms are represented in dark green,
gray, white, red and orange, respectively, in this figure and those hereafter.

![](./images/811193960553775105_6.jpg)

Figure 3. Configurations of the adsorbed intermediates and corresponding transition states of the elementary steps of methanol formation on (a) Pd(211) and (b) Pd(211)-B.

![](./images/811193960553775105_7.jpg)

Figure 4. Energy profiles of the possible pathways for methanol generation on (a) Pd(211) and (b) Pd(211)-B, according to the elementary reactions listed in Table 2. The reaction pathways of methanol formation are summarized as: pathway I (CO → COH → CHOH → CH₂OH → CH₃OH), pathway II (CO → CHO → CHOH → CH₂OH → CH₃OH), pathway III (CO → CHO → CH₂O → CH₂OH → CH₃OH) and pathway IV (CO → CHO → CH₂O → CH₃O → CH₃OH).

![](./images/811193960553775105_8.jpg)

Figure 5. (a) Energy profiles of C-O bond dissociation reactions on Pd(211) (left) and Pd(211)-B(right), respectively. (b) Transition state structures of C-O bond dissociation on both Pd(211) and Pd(211)-B.

![](./images/811193960553775105_9.jpg)

Figure 6. (a) Energy profiles of methane formation on Pd(211) (black dash line) and Pd(211)-B (red dash line), respectively; (b) Adsorption configurations of C, CH, CH₂ and CH₃ as well as the transition state structures of the hydrogenation steps on Pd(211) and Pd(211)-B.

![](./images/811193960553775105_10.jpg)

Figure 7. Energy profiles of water formation on Pd(211) (black dash) and Pd(211)-B (red dash). Inserted are the corresponding configurations of adsorption states and transition states for each reaction step on Pd(211) and Pd(211)-B.

![](./images/811193960553775105_11.jpg)

Figure 8. A schematic illustration of the electronic effect provided by lattice strain and electronic interaction contributed by boron atoms. The d-band of pure Pd is shown in the middle. $\varepsilon_{\text{F}}$, $\varepsilon_{\text{d}}{'}$ ($\varepsilon_{\text{d}}''$) and $\delta\varepsilon_{\text{d}}{'}$ ($\delta\varepsilon_{\text{d}}''$) are Fermi energy, the energy of d-band center and the shift of the d-band center (eV), respectively, where $\delta\varepsilon_{\text{d}}{'}$ = $\varepsilon_{\text{d}}{'}$ - $\varepsilon_{\text{d}}$ and $\delta\varepsilon_{\text{d}}''$ = $\varepsilon_{\text{d}}''$ - $\varepsilon_{\text{d}}$.

![](./images/811193960553775105_12.jpg)

Figure 9. Extended-Brønsted-Evans-Polanyi (BEP) relationship for different bond forming and breaking elementary reactions involved in the methanol and methane production as shown in Table 2, 3 and S1. Reactions on Pd(211) and Pd(211)-B are represented as blue square and red circle, respectively.