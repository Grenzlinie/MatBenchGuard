# A first principles analysis of the hydrogenation of $C_1$—$C_4$ aldehydes and ketones over Ru(0001)

Nishant K. Sinha $^{a,1}$, Matthew Neurock $^{a,b,*}$

$^{a}$ Department of Chemical Engineering, University of Virginia, 102 Engineers' Way, Charlottesville, VA 22904, United States
$^{b}$ Department of Chemistry, University of Virginia, McCormick Road, Charlottesville, VA 22904, United States

---

## ARTICLE INFO

Article history:
Received 28 October 2011
Revised 25 June 2012
Accepted 17 July 2012
Available online 23 September 2012

Keywords:
Hydrogenation
Aldehydes
Ketones
Density functional theory
Ruthenium
Surface kinetics
Kinetic Monte Carlo simulation

---

## ABSTRACT

The structure and degree of substitution of $C_1$—$C_4$ oxygenate molecules can influence their chemisorption and reactivity on metal surfaces. Gradient-corrected periodic density functional theory calculations were carried out to analyze alkyl substituent effects on the hydrogenation of $C_1$—$C_4$ aldehydes and ketones to their corresponding alcohols. All of these aldehydes along with acetone were found to adsorb in a di-$\sigma$ $\eta^1\eta^2$(C,O) mode onto the Ru(0001) surface and result in rehybridization of the C=O bond. Steric hindrance from two alkyl substituents on the carbonyl backbone of methyl ethyl ketone (MEK), however, prevents it from binding di-$\sigma$ $\eta^1\eta^2$(C,O). It adsorbs instead atop a Ru atom in an $\eta^1$(O) configuration through its oxygen atom. Hydrogenation of both aldehydes and ketones can occur through either a hydroxy or an alkoxy mechanism. The hydroxy route proceeds via the formation of the hydroxyalkyl intermediate ($R_1R_2C^*OH$) by the addition of hydrogen to the oxygen of the carbonyl, whereas the alkoxy mechanism proceeds by the addition of hydrogen to the carbon end to form the alkoxy intermediate ($R_1-R_2CHO^*$). DFT calculations indicate that the activation barrier for the initial addition of hydrogen to the carbon to form the C—H bond in the alkoxy mechanism is independent of the substituent groups that are attached to the carbon center as these groups are oriented away from the surface in the transition state and thus have little influence on the activation energies. The activation barriers for the addition of hydrogen to the oxygen of the carbonyl to form the O—H bond in the hydroxy mechanism, however, was found to linearly correlate with the binding energy of the hydroxyalkyl intermediate that forms. This trend can be explained through the Brønsted–Evans–Polanyi relationship and the fact that both the hydroxyalkyl products and carbonyl reactants interact via their carbon centers and are correlated with one another. All of the carbonyls follow a similar trend in that the addition of hydrogen to the carbon of the carbonyl has a much lower barrier on Ru(0001) than the addition of hydrogen to the oxygen. The carbonyls thus readily react to form their alkoxy intermediates. Simple kinetic analyses and first-principle-based kinetic Monte Carlo simulations for formaldehyde over Ru(0001) show that the alkoxy is the most abundant surface intermediate and that the alkoxy route is more favorable than the hydroxy route.

© 2012 Elsevier Inc. All rights reserved.

---

### 1. Introduction

The catalytic conversion of intermediate bio-oils derived via the enzymatic or thermal conversion of lignocellulosic biomass into fuels and chemicals will require the ability to selectively activate specific C—O, O—H, C—H and C—C bonds for a range of different oxygenate intermediates [1]. In particular, the selective reduction of carbonyl (C=O) bonds is an important step in the conversion of these oils as well as in the molecular transformations of specific platform chemicals intermediates to value-added products. Chemo- and enantio-selective hydrogenation of carbonyl compounds is also important step in the synthesis of various fine chemical and pharmaceutical intermediates [2–4]. Many of these molecules have multiple reaction centers, which can lead to multiple reaction products and pathways and thus low reaction selectivities. An important example is that for the synthesis of unsaturated alcohols used in the production of fragrances as well as pharmaceuticals, which is carried out by the selective reduction of C=O bonds in $\alpha$, $\beta$ unsaturated aldehydes and ketones. This requires the selective hydrogenation of the C=O bond over the C=C bond [5]. This is

---

* Corresponding author at: Department of Chemical Engineering, University of Virginia, 102 Engineers' Way, Charlottesville, VA 22904, United States. Fax: +1 434 982 2658.
E-mail addresses: Nishant.sinha@accelrys.com (N.K. Sinha), mn4n@virginia.edu (M. Neurock).
1 Present address: Accelrys K.K., #24, 1st Cross, Magrath Road, Bangalore 560 025, India.

0021-9517/$ - see front matter © 2012 Elsevier Inc. All rights reserved.
http://dx.doi.org/10.1016/j.jcat.2012.07.018

typically rather difficult as the C=C is more strongly held to most transition metal surfaces and tends to be the more reactive of the two bonds. Previous studies for the hydrogenation of $\alpha$, $\beta$ unsaturated aldehydes indicate that branching or substitution of bulkier hydrocarbon intermediates near the C=C bond inhibits the adsorption as well as the hydrogenation of the C=C bond [5,6], which can enhance product selectivity [7]. Similarly, one might expect that the increased substitution at the C=O group would inhibit its ability to adsorb and influence its hydrogenation kinetics.

Despite the wealth of studies in the literature on the hydrogenation of saturated and unsaturated aldehydes and ketones [5,8,9], very little is known about how the structural factors of the reactant influence its intrinsic catalytic hydrogenation kinetics. In general, the selective hydrogenation of aldehydes and ketones over supported metal particles appears to be controlled by the reactant structure, the surface structure and composition of the metal or alloy that is used, the structure and composition of the support, and the presence of solvent [10]. Each of these effects can be important in dictating the activity and selectivity in the hydrogenation of these oxygenates. Herein, we focus solely on the influence of the reactant structure and its effect on the hydrogenation of model $C_1$–$C_4$ aldehydes and ketones in order to provide a fundamental understanding of how these features influence the elementary reaction energies and activation barriers that control catalytic kinetics and selectivity. We specifically analyze the effects of the carbon chain length and the degree of substitution at the carbon atom in the reactive carbonyl.

We first review some of the relevant studies carried out with aldehydes and ketones of different chain lengths and different molecular structures in order to establish the salient factors that control the hydrogenation kinetics. There are relatively few studies on the hydrogenation of formaldehyde, the smallest and least substituted carbonyl that forms via the hydrogenation of CO, since it is rather reactive. Aika et al. [11] examined the hydrogenation of formaldehyde over a variety of group VIII metals to elucidate the effect of metal, support, and promoters on selectivity to methanol. They were able to demonstrate a direct correlation between the selectivity to methanol and the heat of formation of the metal oxide which suggests that the metal-oxygen bond of the methoxy intermediate plays an important role in controlling reactivity. Hirschl et al. [12] used density functional theoretical calculations to examine the hydrogenation of formaldehyde over Pt(111) and Pt₈₀Fe₂₀(111). They found that the addition of first hydrogen to the carbon and oxygen centers of formaldehyde have similar activation barriers on both surfaces.

The substitution of one or both of the hydrogens on carbon end of formaldehyde with substituents can result in significant differences in the reaction kinetics. van Druten and Ponec [13], for example, showed experimentally that propionaldehyde was much less reactive than acetone over supported Pt, Pd, and Rh catalysts. The differences between acetone and propionaldehyde were attributed to the differences in binding modes for the two molecules to the metal. They speculated that the $\eta^2$(C,O) adsorption mode for the aldehydes was less reactive than the $\eta^1$(O) mode. Alcala et al. [14], however, reported the opposite trend for the hydrogenation of propionaldehyde and acetone over the model Pt(111) surface based on theoretical calculations revealing that the hydrogenation of propionaldehyde was faster than acetone. The number of studies on larger aldehydes such as butyraldehyde or hydrocarbon substituted ketones such as methyl ethyl ketone is very limited. Kishida, Murakami, Imanaka, and Teranishi investigated the liquid-phase hydrogenation of various ketones including acetone, methyl ethyl ketone, methyl n-propyl ketone, and methyl isobutyl ketone over a nickel boride catalyst [15,16]. Their results, presented in terms of a Langmuir–Hinshelwood model [17], indicate that the rate constant as well as the adsorption strength of the ketone becomes larger with increasing number of carbon atoms in the alkyl chain. Chang et al. [18] used initial rate methods to investigate the hydrogenation kinetics of acetone, methyl ethyl ketone, methyl n-propyl ketone, and diethyl ketone in the liquid phase. They found that their results could be appropriately described by a Langmuir–Hinshelwood model. In contrast to previous results, they found that the reaction rate was first-order in hydrogen pressure rather than half-order.

In general, Pt, Pd, Ru, Rh, and Ni metals [19] tend to be the most effective in hydrogenating different carbonyl intermediates. Breen et al. [20] studied a series of Ru-containing monometallic and bimetallic catalysts for hydrogenation of MEK to 2-butanol at 30° C and 3 bar H₂. They found that the activity of a 5:1 Ru/Pt wt% bimetallic catalyst was much higher than that of the monometallic catalysts. They suggested that the dissociative adsorption of hydrogen at step sites might control the rate. Kluson and Cerveny [21] indicated that among transition metals, ruthenium is the most active catalyst for hydrogenation of aliphatic carbonyl compounds, particularly in the presence of water.

Herein we carry out ab initio density functional theory (DFT) calculations to elucidate the mechanisms and structural features of the reactant that control the hydrogenation of model aliphatic aldehydes and ketones. More specifically, we examine the hydrogenation of formaldehyde, acetaldehyde, propionaldehyde, acetone, butyraldehyde, and methyl ethyl ketone (MEK) over Ru(0001). The computational results reveal direct correlations between the reaction energies as well as the activation barriers for the governing elementary reaction steps and the binding energies of the relevant reaction intermediates. The trends are governed by the nature of the alkyl substituents on the carbonyl group containing hydrocarbons. In order to assess the kinetics, we carry out kinetic Monte Carlo simulations [22] to elucidate the favored pathways for conversion of formaldehyde to methanol using the DFT-calculated adsorption, reaction and activation energies, and through-space and through-surface interaction models.

## Computational details

Gradient-corrected periodic density functional theoretical (DFT) [23] calculations were carried out using the Vienna ab initio Simulation Package (VASP) [24] to examine the adsorption energies, reaction energies, and activation barriers for substituted $C_1$–$C_4$ aldehydes and ketones over the Ru(0001) surface. The Perdew Wang 91 [25] exchange correlation functional was used to treat the gradient corrections to the exchange and correlation energies. The core electrons and the nuclei of the atoms were described using Vanderbilt ultrasoft pseudopotential along with a plane-wave basis set with a cutoff energy of 400 eV [26]. A 3 × 3 × 1 Monkhorst–Pack k-point [27] grid was used to model the first Brillouin zone. All the gas-phase optimizations were carried out spin-unrestricted. The wave functions were converged to within $1 \times 10^{-4}$ eV, and the geometry was optimized until the forces on all of the atoms were less than 0.05 eV/Å. A number of test calculations on different carbonyls and alcohols carried out with an electronic convergence of $1 \times 10^{-6}$ eV, and a structural convergence of 0.01 eV/Å showed that the changes in energy were less than 0.03 eV.

A 3 × 3 unit cell with vacuum space of 16 Å was used in all the calculations discussed to effectively model systems with coverages of 1/9 ML for adsorbates that bind to one metal site and up to 2/9 ML for adsorbates that take up two sites if we assume that the coverage can be determined by the number of sites taken up by an adsorbate per the total number of sites. The results at high coverages show strong repulsive interactions which would suggest that the more substituted hydrocarbons will desorb from the surface. While this may occur, the goals in this work were to systematically

examine the influence in the intrinsic hydrogenation activity. The full effects of coverage will be treated in a follow up study. We therefore focus our present analysis on the hydrogenation chemis- try at 1/9-2/9 ML coverages. A $4 \times 4$ unit cell was used to test the level of error in using a $3 \times 3$ unit cell. The changes in the adsorption energies for butanol (and MEK) were found to be within 0.03 eV.

The Ru(0001) surface was modeled using a four-layer Ru slab. The four-layer slab proved to be a reliable model of the Ru(0001) surface as the calculated binding energies for various intermediates were found to change by less than 0.05 eV in moving to surfaces with 3, 4, and 5 Ru layers. The adsorbate structures as well as the top three metal layers were allowed to fully relax during the structural optimizations, whereas the bottom Ru layer was held fixed to the experimental bulk lattice positions of Ru ($a = 2.71$ Å).

The adsorption energies for the all of the reactants, intermediates, and products for the reactions considered were calculated using the following expression:

$$
\Delta E_{\text{ads}} = E_{\text{adsorbate/M}} - E_{\text{adsorbate}} - E_{M} \tag{1}
$$

where $E_{\text{adsorbate/M}}, E_{\text{adsorbate}}$, and $E_{M}$ refer to the energies of the adsorbate-metal surface system, the adsorbate, and the bare metal surface, respectively. Negative adsorption energies imply more exothermic adsorption and stronger metal-adsorbate bonding. The symbol "*" is used herein to refer to the site on the molecule, which is adsorbed to the surface.

The reaction energies were calculated using:

$$
\Delta E_{\text{rxn}} = E_{\text{products}} - E_{\text{reactants}} \tag{2}
$$

where $E_{\text{products}}$ and $E_{\text{reactants}}$ refer to the energies of the products and reactants, respectively. A negative value of the reaction energy refers to an exothermic reaction.

The energies of adsorption and reaction are used herein as simple measures of the heats of adsorption and reaction, respectively. A more quantitative analysis would require the full accounting of the zero point energies and the changes that result from the specific heats, which would be computationally rather costly as this would require a full vibrational analysis for all of the reactant, intermediate, and product species.

The climbing-image nudged elastic band (CI-NEB) [28] method was used to determine the minimum energy paths (MEPs) for all the hydrogenation steps. The initial MEP was generated with eight images between the reactant and the product. The tangential force on the highest energy image was optimized to less than $0.05$ eV/Å to isolate the transition state (TS). The transition states were verified using vibrational frequency analysis, confirming a single imaginary frequency corresponding to the reaction mode. Activation barriers were calculated from:

$$
\Delta E_{\text{act}} = E_{\text{TS}} - E_{\text{reactants}} \tag{3}
$$

where $E_{\text{TS}}$ is the total electronic energy of transition state.

In order to examine the kinetics, we carry out kinetic Monte Carlo simulations for the hydrogenation of formaldehyde to methanol over Ru(0001). These simulations were all carried out using a previously developed first-principle-based kinetic Monte Carlo simulation code, which is discussed in detail elsewhere [22]. The code utilizes DFT-calculated activation energies, reaction energies, and adsorption energies to explicitly track the spatial and temporal changes of all the surface intermediates in order to simulate the kinetics. The specific elementary reaction steps used in the simulation along with the corresponding pre-exponential factors and sticking coefficients for the forward and reverse reactions are shown in Scheme 1. The adsorption energies, activation barriers, and reaction energies used in the simulations were taken from the DFT values reported in Tables 1 and 2. Bond-order conservation (BOC) and Merck Molecular Force Field [29] algorithms were used as a first approximation to treat the through-surface and through-space lateral interactions between coadsorbates, respectively [30]. The diffusion barriers were determined from DFT-binding energies and BOC estimates [30].

<div style="display: grid; grid-template-columns: auto auto auto auto; gap: 8px; align-items: center;">
  <div></div>
  <div></div>
  <div></div>
  <div style="text-align: center;">$v_{for}$</div>
  <div style="text-align: center;">$v_{rev}$</div>
  <div>$\text{CH}_2\text{O}$</div>
  <div>+ *</div>
  <div>$\rightleftharpoons$ $\text{CH}_2\text{O}^\ast$</div>
  <td style="text-align: center;">$s_0 = 1$</td>
  <td style="text-align: center;">$10^9$ s$^{-1}$</td>
  <div>$\text{H}_2$</div>
  <div>+ 2 *</div>
  <div>$\rightleftharpoons$ 2 $\text{H}^\ast$</div>
  <td style="text-align: center;">$s_0 = 0.1$</td>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <div>$\text{CH}_2\text{O}^\ast$</div>
  <div>+ $\text{H}^\ast$</div>
  <div>$\rightleftharpoons$ $\text{C}^\ast\text{H}_2\text{OH}$ + *</div>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <div>$\text{CH}_2\text{O}^\ast$</div>
  <div>+ $\text{H}^\ast$</div>
  <div>$\rightleftharpoons$ $\text{CH}_3\text{O}^\ast$ + *</div>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <div>$\text{C}^\ast\text{H}_2\text{OH}$</div>
  <div>+ $\text{H}^\ast$</div>
  <div>$\rightleftharpoons$ $\text{CH}_3\text{OH}$ + 2 *</div>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <td style="text-align: center;">N/A</td>
  <div>$\text{CH}_3\text{O}^\ast$</div>
  <div>+ $\text{H}^\ast$</div>
  <div>$\rightleftharpoons$ $\text{CH}_3\text{OH}$ + 2 *</div>
  <td style="text-align: center;">$10^{13}$ s$^{-1}$</td>
  <td style="text-align: center;">N/A</td>
</div>

Scheme 1. Elementary reactions used in the kMC simulation. Pre-exponentials ($v_{for}$, $v_{rev}$) and sticking coefficients ($s_0$) are assumed or taken from the literature as described in the text.

The pre-exponential factors for all of the hydrogenation reaction steps are reported in Scheme 1 as well as the desorption of formaldehyde and methanol was assumed to be $10^{13}$ s$^{-1}$, which is consistent with transition state theory for immobile transition states and desorption transition states which resemble their reactant states. The associative desorption of hydrogen was set at $10^9$ s$^{-1}$, which is consistent with experimental hydrogen desorption kinetics [31,32]. The sticking coefficients for formaldehyde and hydrogen were chosen to be 1 and 0.1, respectively, as previously reported for unsaturated molecules and hydrogen [22]. While the choice of different pre-exponential values result in different rates, they did not change the nature of the most abundant reaction intermediate, the controlling hydrogenation path, or the conclusions.

The kinetics were simulated over a Ru(0001) surface comprised of a $20 \times 20$ grid. Test simulations carried out on a larger $100 \times 100$ grid improved the precision in the simulations but did not notably change the surface coverages or the rates. The simulations reported herein were carried out only to establish the key surface intermediates that form and to help establish the controlling reaction path.

### 3. Results and discussion

The hydrogenation of carbonyl-containing oxygenates ($\text{R}_1\text{R}_{2-}$ $\text{C=O}$) proceeds via the adsorption of the reactant from gas phase onto a metal surface and the dissociative adsorption of hydrogen. The dissociative adsorption over Ru(0001) proceeds with an activation barrier that is only 2 kJ/mol [33]. The adsorbed oxygenate reacts via a sequence of hydrogen addition steps to convert the carbonyl to the corresponding alcohol via a general Horiuti-Polanyi mechanism [34]. This can occur via one of the two paths shown in Fig. 1. In the first route, known as the *hydroxy mechanism*, a surface-bound hydrogen atom, $\text{H}^\ast$, initially adds to the oxygen of the adsorbed carbonyl to form the hydroxyalkyl intermediate ($\text{R}_1\text{R}_2\text{C}^{\ast-}$ $\text{OH}$). In the second route, known as the *alkoxy mechanism*, the first hydrogen adds to the carbon atom of the adsorbed carbonyl to form the alkoxy ($\text{R}_1\text{R}_2\text{CH-O}^\ast$) intermediate. The second hydrogen adds to the oxygen of the adsorbed alkoxy intermediate to form the alcohol. The literature suggests that both the *hydroxy* and *alkoxy* mechanisms are possible for the hydrogenation of aldehydes and ketones [19,35-40]. We, therefore, examine both mechanisms in detail and explore the effects of alkyl chain length and degree of substitution at the carbon center of the carbonyl. More specifically, we analyze the hydrogenation of model $\text{C}_1-\text{C}_4$

<table>
<caption>Table 1<br>DFT calculated geometric and energetic parameters for the most favorable adsorption modes for different intermediates over Ru(0001).</caption>
<thead>
<tr>
<th colspan="2">Species</th>
<th>E<sub>ads</sub> (kJ/mol)</th>
<th>Mode</th>
<th>C—O (Å)</th>
<th>M—O (Å)</th>
<th>M—C (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Carbonyl</td>
<td>Formaldehyde</td>
<td>–104</td>
<td>η¹η²(C,O)</td>
<td>1.41</td>
<td>2.14</td>
<td>2.14</td>
</tr>
<tr>
<td></td>
<td>Acetaldehyde</td>
<td>–69</td>
<td>η¹η²(C,O)</td>
<td>1.41</td>
<td>2.16</td>
<td>2.16</td>
</tr>
<tr>
<td></td>
<td>Propanaldehyde</td>
<td>–72</td>
<td>η¹η¹(C,O)</td>
<td>1.42</td>
<td>2.17</td>
<td>2.17</td>
</tr>
<tr>
<td></td>
<td>Acetone</td>
<td>–43</td>
<td>η¹η²(C,O)</td>
<td>1.43</td>
<td>2.17</td>
<td>2.17</td>
</tr>
<tr>
<td></td>
<td>Butyraldehyde</td>
<td>–67</td>
<td>η¹η²(C,O)</td>
<td>1.42</td>
<td>2.17</td>
<td>2.14</td>
</tr>
<tr>
<td></td>
<td>MEK</td>
<td>–33</td>
<td>η¹(O)</td>
<td>1.24</td>
<td>2.13</td>
<td>–</td>
</tr>
<tr>
<td>Hydroxy intermediate</td>
<td>Hydroxy-methyl</td>
<td>–188</td>
<td>η²(C,O)</td>
<td>1.48</td>
<td>2.21</td>
<td>2.13</td>
</tr>
<tr>
<td></td>
<td>1-Hydroxy-ethyl</td>
<td>–169</td>
<td>η²(C,O)</td>
<td>1.49</td>
<td>2.25</td>
<td>2.14</td>
</tr>
<tr>
<td></td>
<td>1-Hydroxy- propyl</td>
<td>–165</td>
<td>η²(C,O)</td>
<td>1.50</td>
<td>2.23</td>
<td>2.15</td>
</tr>
<tr>
<td></td>
<td>2-Hydroxy- propyl</td>
<td>–152</td>
<td>η²(C,O)</td>
<td>1.51</td>
<td>2.28</td>
<td>2.16</td>
</tr>
<tr>
<td></td>
<td>1-Hydroxy-butyl</td>
<td>–157</td>
<td>η²(C,O)</td>
<td>1.50</td>
<td>2.25</td>
<td>2.15</td>
</tr>
<tr>
<td></td>
<td>2-Hydroxy-butyl</td>
<td>–151</td>
<td>η²(C,O)</td>
<td>1.50</td>
<td>2.23</td>
<td>2.21</td>
</tr>
<tr>
<td>Alkoxy intermediate</td>
<td>Methoxy</td>
<td>–259</td>
<td>η³(O)</td>
<td>1.44</td>
<td>2.22</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>Ethoxy</td>
<td>–263</td>
<td>η³(O)</td>
<td>1.45</td>
<td>2.16</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>1-Propoxy</td>
<td>–258</td>
<td>η³(O)</td>
<td>1.46</td>
<td>2.17</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>2-Propoxy</td>
<td>–268</td>
<td>η³(O)</td>
<td>1.48</td>
<td>2.16</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>1-Butoxy</td>
<td>–259</td>
<td>η³(O)</td>
<td>1.47</td>
<td>2.18</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>2-Butoxy</td>
<td>–267</td>
<td>η³(O)</td>
<td>1.48</td>
<td>2.18</td>
<td>–</td>
</tr>
<tr>
<td>Alcohol</td>
<td>Methanol</td>
<td>–38</td>
<td>η¹(O)</td>
<td>1.45</td>
<td>2.29</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>Ethanol</td>
<td>–21</td>
<td>η¹(O)</td>
<td>1.46</td>
<td>2.32</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>1-Propanol</td>
<td>–24</td>
<td>η¹(O)</td>
<td>1.46</td>
<td>2.40</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>2-Propanol</td>
<td>–33</td>
<td>η¹(O)</td>
<td>1.47</td>
<td>2.37</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>1-Butanol</td>
<td>–34</td>
<td>η¹(O)</td>
<td>1.46</td>
<td>2.42</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>2-Butanol</td>
<td>–41</td>
<td>η¹(O)</td>
<td>1.47</td>
<td>2.36</td>
<td>–</td>
</tr>
<tr>
<td>Atomic hydrogen</td>
<td></td>
<td>–91*</td>
<td>η³(H)</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

* With respect to the gas-phase molecular hydrogen.

<table>
<caption>Table 2<br>DFT calculated geometric and energetic parameters for the transition states for elementary hydrogenation steps in the hydroxy and the alkoxy routes over Ru(0001).</caption>
<thead>
<tr>
<th colspan="2">Species</th>
<th>ΔE<sub>act</sub> (kJ/mol)</th>
<th>ΔE<sub>rxn</sub> (kJ/mol)</th>
<th>O—H<sup>a</sup>/ C—H<sup>b</sup> (Å)</th>
<th>M—H (Å)</th>
<th>M—O (Å)</th>
<th>M—C (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hydroxy TS1<sup>a</sup></td>
<td>Formaldehyde</td>
<td>90</td>
<td>37</td>
<td>1.43</td>
<td>1.96</td>
<td>2.13</td>
<td>2.15</td>
</tr>
<tr>
<td></td>
<td>Acetaldehyde</td>
<td>110</td>
<td>41</td>
<td>1.40</td>
<td>1.95</td>
<td>2.15</td>
<td>2.17</td>
</tr>
<tr>
<td></td>
<td>Propanaldehyde</td>
<td>121</td>
<td>47</td>
<td>1.43</td>
<td>1.89</td>
<td>2.15</td>
<td>2.18</td>
</tr>
<tr>
<td></td>
<td>Acetone</td>
<td>127</td>
<td>49</td>
<td>1.43</td>
<td>1.86</td>
<td>2.17</td>
<td>2.19</td>
</tr>
<tr>
<td></td>
<td>Butyraldehyde</td>
<td>126</td>
<td>51</td>
<td>1.44</td>
<td>1.86</td>
<td>2.17</td>
<td>2.18</td>
</tr>
<tr>
<td></td>
<td>MEK</td>
<td>64</td>
<td>22</td>
<td>1.40</td>
<td>1.95</td>
<td>2.12</td>
<td>2.26</td>
</tr>
<tr>
<td>Hydroxy TS2<sup>b</sup></td>
<td>Formaldehyde</td>
<td>90</td>
<td>14</td>
<td>1.40</td>
<td>1.65</td>
<td>2.24</td>
<td>2.31</td>
</tr>
<tr>
<td></td>
<td>Acetaldehyde</td>
<td>79</td>
<td>9</td>
<td>1.43</td>
<td>1.65</td>
<td>2.30</td>
<td>2.34</td>
</tr>
<tr>
<td></td>
<td>Propanaldehyde</td>
<td>75</td>
<td>7</td>
<td>1.43</td>
<td>1.65</td>
<td>2.22</td>
<td>2.36</td>
</tr>
<tr>
<td></td>
<td>Acetone</td>
<td>76</td>
<td>–1</td>
<td>1.44</td>
<td>1.65</td>
<td>2.30</td>
<td>2.38</td>
</tr>
<tr>
<td></td>
<td>Butyraldehyde</td>
<td>70</td>
<td>–7</td>
<td>1.45</td>
<td>1.65</td>
<td>2.27</td>
<td>2.34</td>
</tr>
<tr>
<td></td>
<td>MEK</td>
<td>72</td>
<td>–10</td>
<td>1.53</td>
<td>1.67</td>
<td>2.25</td>
<td>2.44</td>
</tr>
<tr>
<td>Alkoxy TS1<sup>b</sup></td>
<td>Formaldehyde</td>
<td>65</td>
<td>–3</td>
<td>1.50</td>
<td>1.67</td>
<td>2.11</td>
<td>2.26</td>
</tr>
<tr>
<td></td>
<td>Acetaldehyde</td>
<td>63</td>
<td>–14</td>
<td>1.56</td>
<td>1.66</td>
<td>2.01</td>
<td>2.41</td>
</tr>
<tr>
<td></td>
<td>Propanaldehyde</td>
<td>58</td>
<td>–7</td>
<td>1.56</td>
<td>1.64</td>
<td>2.17</td>
<td>2.32</td>
</tr>
<tr>
<td></td>
<td>Acetone</td>
<td>53</td>
<td>–24</td>
<td>1.63</td>
<td>1.65</td>
<td>2.01</td>
<td>2.45</td>
</tr>
<tr>
<td></td>
<td>Butyraldehyde</td>
<td>65</td>
<td>–9</td>
<td>1.54</td>
<td>1.65</td>
<td>2.25</td>
<td>2.32</td>
</tr>
<tr>
<td></td>
<td>MEK</td>
<td>58</td>
<td>–47</td>
<td>1.63</td>
<td>1.65</td>
<td>2.08</td>
<td>2.45</td>
</tr>
<tr>
<td>Alkoxy TS2<sup>a</sup></td>
<td>Formaldehyde</td>
<td>124</td>
<td>53</td>
<td>1.44</td>
<td>1.82</td>
<td>2.16</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>Acetaldehyde</td>
<td>128</td>
<td>64</td>
<td>1.43</td>
<td>1.78</td>
<td>2.16</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>Propanaldehyde</td>
<td>127</td>
<td>61</td>
<td>1.46</td>
<td>1.78</td>
<td>2.19</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>Acetone</td>
<td>126</td>
<td>59</td>
<td>1.46</td>
<td>1.79</td>
<td>2.12</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>Butyraldehyde</td>
<td>125</td>
<td>56</td>
<td>1.47</td>
<td>1.77</td>
<td>2.27</td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>MEK</td>
<td>124</td>
<td>51</td>
<td>1.42</td>
<td>1.86</td>
<td>2.09</td>
<td>–</td>
</tr>
</tbody>
</table>

<sup>a</sup> Transition states in which O—H bonds are formed.
<sup>b</sup> Transition states in which C—H bonds are formed.

aldehydes (formaldehyde, acetaldehyde, propionaldehyde, and butyraldehyde) and two simple model $C_3$—$C_4$ ketones (acetone and methyl ethyl ketone).

### 3.1. Adsorption of reactants, intermediates, and products

DFT calculations were first carried out to determine the modes and corresponding adsorption energies for all of the aldehyde and ketone reactants discussed above as well as the corresponding hydroxyalkyl and alkoxy intermediates and alcohol products that form upon hydrogenation over the Ru(0001) surface.

Experimental and theoretical studies suggest that aldehydes and ketones adsorb onto transition metal surfaces in either $\eta^1(O)$ or $\eta^2(C,O)$ [14,41–49] modes, which reflect their bonding configurations. In the $\eta^1(O)$ mode, the molecule binds atop of a single metal atom through the donation of the electrons from the lone pair

![](./images/813277449742712832_1.jpg)

Fig. 1. The hydroxy and alkoxy reaction pathways for the hydrogenation of aldehydes and ketones.

on the oxygen into a non-bonding d-orbital on the metal [50,51]. Adsorption in the di-$\sigma$ ($\eta^{1}\eta^{2}(C,O)$) mode involves the rehybridization of the carbon-oxygen bond of the molecule, allowing both the carbon and the oxygen atoms of the C=O bond to form $\sigma$ bonds with two neighboring surface Ru atoms [43]. The binding energies for all of the $C_{1}-C_{4}$ aldehydes and ketones examined on Ru(0001) were calculated using DFT and presented in Table 1. While the binding energies for each of these carbonyls were calculated in four different adsorption modes (atop, bridge, hollow, and di-$\sigma$), we only report here the values for the most stable configurations found on the Ru(0001) surface. The results reported in Table 1 indicate that the di-$\sigma$ ($\eta^{1}\eta^{2}(C,O)$) configuration shown in Fig. 2A (for formaldehyde) is the preferred adsorption mode for all of the aldehydes. Experimental results corroborate this for the adsorption of formaldehyde, acetaldehyde, and propionaldehyde over Ru(0001) and Rh(111) surfaces [50,52-54].

The results in Fig. 3A and Table 1 indicate that increasing the chain length, $R_{1}$, of a specific aldehyde ($R_{1}HC{=}O$) alone has very little influence on its adsorption energy. More predominant changes result, however, upon increasing the degree of substitution on the carbon atom that anchors the carbonyl to the surface. This weakens the adsorption energy by nearly 30 kJ/mol for each substituent and is the result of the repulsive interactions between the alkyl substituent and the surface.

The hydroxyalkyl intermediate that forms upon the hydrogenation of the adsorbed carbonyl binds in $\eta^{2}(C,O)$ configuration (Fig. 2B) to the Ru(0001) surface. The $\eta^{2}$ mode was found to be the preferred configuration for all of the hydroxyalkyl intermediates examined. The Ru—O(H) bond that forms in the hydroxyalkyl surface intermediate is significantly weakened as a result of the hydrogenation of the carbonyl. The strong adsorption of these intermediates is due to the fact that these species are unstable open-shell free radicals in the gas phase. The trends in the calculated binding energies for the hydroxyalkyl intermediates as a function of carbon chain length and degree of substitution reported in Fig. 3B are quite similar to the trends in the adsorption energies for the carbonyls shown in Fig. 3A. The binding of the hydroxymethyl intermediate, which is $- 188$ kJ/mol, is 19 kJ/mol stronger than that for the 1-hydroxyethyl intermediate ($- 169$ kJ/mol) whereby one of the hydrogen atoms is replaced by a methyl group. A second substitution at the carbon atom bound to the surface to form the 2-hydroxypropyl intermediate ($- 152$ kJ/mol) weakens the binding energy by an additional 17 kJ/mol. The changes that result by simply increasing the chain length were found to be rather small (<10 kJ/mol) and similar to that which was found in the adsorption of the carbonyl adsorbates.

The hydrogenation of the adsorbed carbonyl can also proceed via the addition of the hydrogen to the carbon end of the molecule, thus resulting in the formation of a surface alkoxy intermediate. DFT results indicate that the alkoxy intermediate preferentially binds through its oxygen at a threefold fcc site on Ru(0001) (Fig. 2C). The binding energies for all of the alkoxy intermediates were found to be significantly stronger than those for the hydroxyalkyl intermediates on Ru as Ru is very oxophillic but varied by only 10 kJ/mol ranging from $- 258$ to $- 268$ kJ/mol. The alkyl substituents on the alkoxy intermediates are much further removed from the surface. They, therefore, do not interact with the surface and thus have little effect on the adsorption energies. The relatively small changes that result in the binding energies with changes in the carbon chain length and carbon substitution are evident in Fig. 3C.

The subsequent hydrogenation of both the hydroxyalkyl and alkoxy intermediates results in the formation of the alcohol product. The resulting $C_{1}-C_{4}$ alcohols were found to bind atop of a Ru via their oxygen atom in a bent configuration shown in Fig. 2D as a result of valence shell repulsion from the lone pair of electrons on the oxygen and the filled states of the metal. This configuration is

![](./images/813277449742712832_2.jpg)

Fig. 2. DFT-optimized adsorption configuration for (a) formaldehyde, (b) hydroxymethyl, (c) methoxy, and (d) methanol over Ru(0001).

![](./images/813277449742712832_3.jpg)

Fig. 3. Trends in the binding energies of $C_1$–$C_4$ (a) carbonyls, (b) hydroxyalkyl intermediate, (c) alkoxy intermediate, and (d) alcohol over Ru(0001).

well established for various ROH intermediates including water, methanol, and ethanol [39,55–59]. The alkyl groups on the alcohol only weakly influence the alcohol's interaction with the surface and as such the adsorption energies vary by only 20 kJ/mol. The weak changes in the alcohol adsorption energies with chain length and degree of substitution are shown in Fig. 3D.

### 3.2. Reaction energies and activation barriers

The reaction energies were calculated for the two hydrogen addition steps that occur in both the alkoxy and the hydroxy mechanisms. In the absence of the metal surface (i.e., in the gas phase), the addition of the hydrogen atom to the oxygen (O—H bond formation) of an aldehyde or ketone is favored over the addition to the carbon (C—H bond formation) as the O—H bond for water and alcohols is about 40 kJ/mol stronger than the C—H bond for alkanes and alcohols. This can change on a metal surface since the differences between the O—H and the C—H bond energies in the gas phase are compensated for by the differences in metal—OR (alkoxy) and metal—C(OH)R (hydroxyalkyl) bond strengths. The two of these effects tend to counter one another since an increase in the exothermicity of the gas-phase reaction stabilizes the gas-phase intermediate thus weakening its interaction with the surface. On Ru(0001), the metal–alkoxy bond is over 70 kJ/mol stronger than the metal–hydroxyalkyl bond which suggests that hydrogen prefers to add to the carbon rather than the oxygen of the adsorbed carbonyl.

#### 3.2.1. Hydroxy mechanism

In the hydroxy mechanism, the reaction energy for the initial hydrogenation of the aldehyde or ketone to form the $R_1R_2C^*$—OH hydroxyalkyl intermediate on Ru(0001) was found to be endothermic for all of the reactants examined (Table 2). A close analysis of the changes in the adsorption energies as well as the gas-phase reaction energies that make up the overall reaction energies indicate that the binding energies of the hydroxyalkyl intermediates decrease with the degree of substitution or increasing chain length as hydroxymethyl ($^*CH_2OH$) is over 31 kJ/mol stronger than 1-hydroxybutyl. The adsorption energy of carbonyl reactant also decreases with increasing degree of substitution and chain length as formaldehyde is over 37 kJ/mol stronger than the butanaldehye. The adsorption energies of the hydroxyalkyl intermediates are linearly related to the adsorption energies of the carbonyls as is shown in Fig. 4. The slope of this line (0.606) reveals that the weakening of the carbonyl is greater than the weakening of the hydroxyalkyl product. The reaction energies thus also scale linearly with the adsorption of the hydroxyalkyl (as well as carbonyl) adsorption energies as is shown in Fig. 5A. The reaction energy therefore become becomes less favorable with increasing the degree of substitution or the chain length. The lone exception is the

![](./images/813277449742712832_4.jpg)

Fig. 4. Comparison of the DFT-calculated adsorption energies for the hydroxyalkyl intermediate versus the adsorption energies of the carbonyl reactant (excluding MEK). The best-fit line is $y = 0.6056x - 123.2$ with $R^2 = 0.901$. $i$-$C_3$ refers to the intermediate derived from acetone.

![](./images/813277449742712832_5.jpg)

Fig. 5. Trends in the (a) reaction energies and (b) activation barriers for the formation of the hydroxy intermediates from the carbonyls over Ru(0001). The best-fit lines to the reaction energies (a) and the activation barriers (b) versus the hyroxyalkyl adsorption energies (excluding MEK) are (a) $y=0.3892x+109.69$ with $R^{2}=0.86$ and (b) $y=1.0869x+295.45$ with $R^{2}=0.96$. $i-C_{3}$ and $i-C_{4}$ refer to the intermediates derived from acetone and MEK, respectively.

addition of hydrogen to MEK, which has the most favorable reaction energy. This is due to the strong repulsive interactions of the alkyl substituents on MEK, which force it up off of the surface where it can only very weakly bond via an $\eta^{1}(O)$ mode on the surface. This significant destabilization of the MEK reactant dominates over comparatively weaker changes in hydroxy product binding energies.

The addition of the first hydrogen to oxygen atom of the adsorbed carbonyl in the hydroxyalkyl mechanism proceeds via a transition state, which involves the insertion of hydrogen into the $Ru-O$ bond as is shown in Fig. 6A to form a classic three center complex with $Ru-H$, $O-H$ and $Ru-O$ bonds lengths of 1.96, 1.43 and $2.13\ \text{\AA}$, respectively (for hydroxymethyl). The transition-state structure appears to be much more reactant-like than product-like and very similar to previous structures found for the hydrogenation of formaldehyde on Pd(111) [60]. The activation barriers for different aldehydes and ketones were found to be directly correlated with the overall energies of reaction via a classic Brønsted-Evans-Polanyi (BEP) relationship [61] as is shown in Fig. 7A. MEK once again presents the lone exception as it results in the removal of strong steric repulsion in moving from the reactant state to the transition state, which leads to a lower barrier than that found for the other carbonyls.

The barriers were also found to correlate directly with the heat of adsorption of the hydroxyalkyl intermediate that forms, as is shown in Fig. 5B. This derives in part from Brønsted-Evans-Polanyi relationship:

$$
\begin{aligned}
\Delta(\Delta E_{\text{act}}) & =\alpha \Delta(\Delta H_{\text{rxn}})=\alpha \Delta(\Delta H_{\text{hydroxyalkyl}}-\Delta H_{\text{H}}-\Delta H_{\text{carbonyl}}+\Delta H_{\text{rxn}}(\mathrm{g})) \\
& \sim \alpha \Delta(\Delta H_{\text{hydroxyalkyl}}+\Delta H_{\text{rxn}}(\mathrm{g})-\Delta H_{\text{carbonyl}}) \\
& \sim \alpha \Delta(\Delta H_{\text{hydroxyalkyl}}) \sim-\alpha \Delta(\Delta H_{\text{carbonyl}})
\end{aligned}
\tag{4}
$$

where changes in the activation barrier $(\Delta(\Delta E_{\text{act}}))$ are linearly proportional to the changes in heats of adsorption of the hydroxyalkyl product $(\Delta H_{\text{hydroxyalkyl}})$ minus the changes in heats of adsorption of the carbonyl $(\Delta H_{\text{carbonyl}})$ and hydrogen $(\Delta H_{\text{H}})$ reactants as well as the gas-phase adsorption energies $(\Delta H_{\text{rxn}}(\mathrm{g}))$. The heat of adsorption of atomic hydrogen does not change from one reactant to the next; as such $\Delta(\Delta H_{\text{H}})$ is zero. The changes in the gas-phase heats of reaction can also be neglected since they are much smaller than the changes in the heats of adsorption of the carbonyl or the hydroxyalkyl. Lastly, since the changes in the adsorption energies for the hydroxyalkyl intermediates are linearly correlated with the adsorption energies of the corresponding carbonyls (Fig. 4), the changes in the activation barrier can be linearly related to the changes in the heats of adsorption of the hydroxyalkyl. The barriers can similarly be related to the heats of adsorption of the carbonyls. The heats of adsorption are approximated here by the changes in energy as the changes in zero point energies and specific heats will be quite small in comparing similar reactions. More detailed information concerning all of the transition-state structures and the calculated activation barriers are given in Table 2.

The second step in the hydroxy mechanism involves the addition of second hydrogen to the carbon end of the adsorbed hydroxyalkyl intermediate to form the alcohol (Fig. 1). The reaction energy for this step is endothermic for the hydroxymethyl $(\text{C}^{\text{H}}_{2}\text{OH})$, hydroxyethyl $(\text{CH}_{3}\text{C}^{\text{H}}\text{HOH})$, and 1-hydroxypropyl $(\text{CH}_{3}\text{CH}_{2}\text{C}^{\text{H}}\text{HOH})$ intermediates and exothermic for the other three reactants, 2-hydroxypropyl $(\text{CH}_{3})_{2}\text{C}^{\text{OH}}$, 1-hydroxybutyl $(\text{CH}_{3}\text{CH}_{2}\text{CH}_{2}\text{C}^{\text{H}}\text{HOH})$, and 2-hydroxybutyl $\text{CH}_{3}\text{CH}_{2}\text{C}^{\text{*}}(\text{CH}_{3})\text{OH}$. The trend in the reaction energy here is also correlated to the binding energy of the hydroxyalkyl intermediate (Fig. 8A) but in the exact opposite way as that for the first hydrogen addition step. The increase in the hydroxyalkyl binding energy to the metal surface leads to an increase in the reaction endothermicity rather than the decrease, which was found in Fig. 5A. This should be expected as the hydroxyalkyl intermediate is now the reactant rather than the product. The adsorption energy of the hydroxyalkyl reactant dominates over the weakly held alcohol product and thus controls the overall reported reaction energies. Increasing the hydroxyalkyl bond strength stabilizes the reactant over the product state and thus results in a more endothermic reaction. It is important to note that MEK falls on the line for the correlation between the binding energy of the hydroxyalkyl intermediate and the reaction energy for the hydrogenation of this intermediate. In this case, the strong steric effects present in the adsorption of MEK are not dominant in the hydroxyalkyl intermediate or the alcohol product.

The transition state for hydrogen addition to the carbon end of the adsorbed hydroxymethyl intermediate to form methanol on the Ru(0001) surface (shown in Fig. 6B) involves an insertion of hydrogen into the metal-carbon bond. This results in the transition from an $\eta^{2}(\text{C,O})$ binding mode to an $\eta^{1}(\text{O})$ (atop site through oxygen) mode as the methyl group that forms leaves the surface. The transition state is much more reactant-like than product-like and very similar to that found for the hydrogenation of other alkyl intermediate such as that found for the hydrogenation of an ethyl intermediate to ethane [62]. The $\text{M-O}$, $\text{M-C}$, and $\text{M-H}$ bonds in the transition state were found to be 2.24, 2.31, and $1.65\ \text{\AA}$, respectively (for the hydroxymethyl intermediate). The trend in the activation barriers is also guided by the adsorption energies of the

![](./images/813277449742712832_6.jpg)

Fig. 6. DFT-calculated transition-state structures for the formation of the (a) hydroxymethyl intermediate from formaldehyde, (b) methanol from the hydroxymethyl intermediate, (c) methoxy intermediate from formaldehyde, and (d) methanol from the methoxy intermediate over Ru(0001).

![](./images/813277449742712832_7.jpg)

Fig. 7. Brønsted-Evans-Polanyi correlations of the activation energy against the energy of reaction for the hydrogenation of aldehydes and ketones over Ru(0001) via the: (a) hyroxy and (b) alkoxy mechanisms. The best-fit lines for the hydroxy (a) and alkoxy (b) BEP correlations are (a) $y=2.2878x+12.153; R^{2}=0.97$ (Step 1) and $y=0.6327x+75.735; R^{2}=0.72$ (Step 2); (b) $y=0.1584x+63.079; R^{2}=0.29$ (Step 1) and $y=0.3269x+106.92; R^{2}=0.97$ (Step 2).

hydroxyalkyl intermediates (Fig. 8B). The most strongly bound hydroxyalkyl intermediates are those that are most difficult to hydrogenate (i.e., high activation barriers). This can also be pre- dicted from a Brønsted-Evans-Polanyi relationship, which linearly relates the change in the overall reaction energies with the changes in the activation barriers (Fig. 7A). This is shown in the following equation:

$$
\begin{aligned}
\Delta\left(\Delta E_{\mathrm{act}}\right) & =\alpha \Delta\left(\Delta H_{\mathrm{rxn}}\right) \\
& =\alpha \Delta\left(\Delta H_{\text {alcohol }}-\Delta H_{\mathrm{H}}-\Delta H_{\text {hydroxyalkyl }}+\Delta H_{\mathrm{rxn}}(\mathrm{g})\right) \\
& \sim \alpha\left[-\Delta\left(\Delta E_{\text {hydroxyalkyl }}\right)\right]
\end{aligned}
\tag{5}
$$

Similar arguments to those outlined above in establishing Eq. (4) can be used to show that the heat of reaction can be approxi- mated by the heat of adsorption of the hydroxyalkyl intermediate as this is dominate term in Eq. (5). The hydroxyalkyl intermediate, however, is now the reactant and the weakly held alcohol is the product. The barrier for the hydrogenation of the 2-hydroxybutyl intermediate (from MEK) to form 2-butanol is nicely contained within the correlation since the steric crowding at the carbon cen- ter is not the dominant factor.

### 3.2.2. Alkoxy mechanism
In the alkoxy mechanism, the first hydrogen adds to the carbon atom of the bound carbonyl, thus, forming the corresponding sur- face alkoxy intermediate. The reaction energy for this step was found to be exothermic for all of the cases examined. As was dis- cussed above, the formation of the $C-H$ bond is more exothermic and favorable than the $O-H$ bond formation on $Ru(0001)$ . The activation barriers are roughly correlated with the overall energies of reaction in the BEP plot in Fig. 7B. The calculated reaction ener- gies for the initial $C-H$ bond formation, however, do not appear to correlate with the adsorption energy of the alkoxy intermediate as reflected in the data given in Tables 1 and 2. This is due to the fact that the alkoxy product that forms is fairly insensitive to changes in alkyl substituents as was shown previously in Fig. 3C (and in Ta- ble 1). The alkyl substituents on the alkoxy intermediate are bound

![](./images/813277449742712832_8.jpg)

Fig. 8. Trends in the (a) reaction energies and (b) activation barriers for the formation of the alcohol from the hydroxyalkyl intermediates over Ru(0001). The best-fit lines to the reaction energies (a) and the activation barriers (b) versus the hydroxyalkyl adsorption energies are (a) $y = -0.6052x - 97.049$; $R^2 = 0.78$ and (b) $y = -0.463x + 1.2263$; $R^2 = 0.82$. $i$-$C_3$ and $i$-$C_4$ refer to the intermediates derived from acetone and MEK, respectively.

![](./images/813277449742712832_9.jpg)

Fig. 9. Trends in the (a) reaction energies and (b) activation barriers for the formation of the alkoxy intermediates from the carbonyls over Ru(0001). The best- fit line for the correlation between the reaction energies and the adsorption energies of the carbonyls (excluding MEK) is $y = -0.3326x - 35.017$; $R^2 = 0.80$. $i$-$C_3$ and $i$-$C_4$ refer to the intermediates derived from acetone and MEK, respectively.

to the carbon atom, which is further away from the surface and, as such, they do not interact with the surface. There is, thus, very little change in the heat of reaction due to changes in adsorption of the alkoxy product state. The changes in the heat of reaction should instead be due to changes in the structure of carbonyl reactant state. The correlation observed in Fig. 9A between the reaction energy and the adsorption of the aldehyde or ketone indicates that the reaction is more exothermic when the carbonyl is more weakly held to the surface. MEK and, to some extent, acetone appear to be exceptions. This is due to the increased steric repulsion that occurs upon increasing the substitution at the carbon center of the carbonyl. Both acetone and MEK can relieve these steric repulsions via the addition of hydrogen to the carbon atom to form the much more favorable alkoxy intermediates. The effect here is more pronounced (influencing not only MEK but acetone as well) than that found in Fig. 5A as the hydrogen addition now occurs directly at the crowded carbon center.

The transition state for the addition of hydrogen to the carbon end of the adsorbed formaldehyde, which is shown in Fig. 6C, is very similar to that for the hydrogenation of the hydroxymethyl intermediate shown in Fig. 6B as it involves the insertion of hydrogen into the Ru—C bond. The Ru—C, Ru—H, and the C—H bonds in the transition state were found to be 2.26, 1.67 and $1.50\,\text{Å}$, respectively, which is very similar to the values of 2.31, 1.65, and $1.40\,\text{Å}$ found for the hydroxymethyl hydrogenation transition state.

The changes in the activation barriers for this reaction, however, are quite different than those reported for the hydrogenation of the hydroxyalkyl intermediate. The activation barriers here are fairly insensitive to changes in the substituents on the carbonyl as is shown in the values given in Table 2 and the BEP plot shown in Fig. 7B. The changes in the transition-state energy that result from changes in substituents are very similar to those that occur in the reactant state. These changes tend to cancel one another out and as such there is very little correlation between the calculated activation energies and the adsorption energies of the carbonyl reactants. The calculated activation barriers for this reaction should be correlated instead with the energies of the alkoxy product state. Even these changes, however, are rather weak as shown in Fig. 9B, and the barriers can be considered essentially independent of the substituent. The activation barriers, for example, are clustered within about 10 kJ/mol of one another (53–65 kJ/mol). As such the correlation between the activation barrier and the adsorption energy of the alkoxy intermediate shown in Fig. 9B is not very strong. The barriers for $C_3$ and $C_4$ aldehydes appear to be slightly higher than the corresponding ketones. The results are consistent with the experimental results by van Druten and Ponec [13] who found the hydrogenation of propionaldehyde to be slower than the hydrogenation of acetone over Pt. This, as mentioned earlier, is in contrast to DFT results by Alcala et al. who reported slower hydrogenation rate for acetone [14].

The subsequent addition of hydrogen to the oxygen atom of the adsorbed alkoxy intermediate leads to the formation of the alcohol. This step was found to be fairly endothermic for all of the intermediates examined (Table 2). The endothermicity is attributed to the strong binding energy of the alkoxy intermediate on Ru(0001). Since all of the alkoxy adsorption energies are similar, the changes that result in the overall reaction energies must be the result of the changes in the product state energies, that is, the adsorption energies of the alcohols. The reaction energies become more exothermic as the binding energy of the alcohol becomes stronger and are linearly correlated as shown in Fig. 10A. The correlations with the linear and branched alkoxy intermediates, derived from the aldehydes and ketones, respectively, is slightly different as the branched alkoxy intermediates are only ~5 kJ/mol less endothermic than the linear structures. This is due to the slightly stronger adsorption energies for the more substituted alcohol product that results from the ketones.

The transition state for this reaction, which is depicted in Fig. 6D, involves the insertion of hydrogen into the metal-oxygen bond of the adsorbed alkoxy intermediate. As hydrogen approaches the oxygen atom, the alkoxy moves from the threefold hollow site to the neighboring atop site on the surface. While the activation barriers are linearly related to the reaction energies as shown in Fig. 7B, the correlation of the barriers with the alkoxide adsorption energy is rather weak (as shown in Fig. 10B) due to the very small changes in the alkoxide binding energies (<10 kJ/mol). The activation barriers for hydrogenation of all the alkoxy intermediates are all close to 125 kJ/mol. This indicates that the steric effects by the alkyl groups on these alkoxy species are not significant. This is further corroborated by Wang et al. who found that the activation barrier for hydrogenating the hydroxy intermediate to water is 120 kJ/mol [63]. It should be noted that this hydrogenation step results in the highest activation barriers for all of the steps examined. The barriers calculated here on Ru(0001) appear to be significantly higher than those found by Alcala et al. [14] for the hydrogenation of isopropoxy and n-propoxy over Pt(111), which were found to be less than 20 kJ/mol. The difference is likely the result of the stronger alkoxy binding on Ru(0001) than on Pt(111). For example, our calculations show that the binding energies of methoxy species on Ru(0001) (-259 kJ/mol) is 126 kJ/mol stronger than on Pt(111) (-133 kJ/mol).

In general, the intrinsic activation barriers calculated here are likely higher than those present under working conditions as the higher surface coverages of hydrocarbons and hydrogen under reaction conditions will result in lateral repulsive interactions, which will decrease the barriers for hydrogenation. It has been shown previously that the intrinsic barriers for ethylene hydrogenation decrease by nearly 30 kJ/mol in moving from 1/6 ML up to 1/3 ML surface coverage [64]. The hydrogenation of aldehydes and ketones is also typically carried out in the presence of water or another polar medium, which is also known to lower the activation barriers due to the stabilization of the transition states or intermediates [21].

![](./images/813277449742712832_10.jpg)

Fig. 10. Trends in the (a) reaction energies and (b) activation barriers for the hydrogenation of the alkoxy intermediates to alcohols over Ru(0001). The best-fit line for the correlation between the reaction energies and the adsorption energies of the carbonyls is $y=0.6084x+76.7$; $R^{2}=0.94$. $i$-$C_{3}$ and $i$-$C_{4}$ refer to the intermediates derived from acetone and MEK, respectively.

### 3.3. Comparisons between the carbonyls for the overall catalytic cycle

In order to draw qualitative conclusions concerning the differences between the two mechanisms and the effects of the alkyl substituents, we used the energies reported in Tables 1 and 2 to construct the overall potential energy diagrams shown in Fig. 11A and B for the hydrogenation of the different aldehydes and ketones over Ru(0001) via the hydroxy and alkoxy mechanisms, respectively. While the results provide useful insights, formal predictions concerning rates and selectivity require full kinetic simulations and the effects of surface coverage. In general, the results show that, regardless of whether the reaction proceeds via the hydroxy or alkoxy route, the addition of hydrogen to oxygen end of the molecule is more difficult than the addition of hydrogen to the carbon end for all carbonyls considered.

In the alkoxy route, which is shown in Fig. 11B, the addition of hydrogen to the carbon end of the weakly held carbonyl should occur quite readily as it has the lowest barrier of all the steps considered (ranging from 53 to 65 kJ/mol) as a result of the weak metal-carbon bond. The alkoxy intermediate that forms, however, is very strongly bound to the surface as a result of the high oxophilicity of Ru, thus resulting in the highest hydrogenation barriers of all the steps considered (around 125 kJ/mol) as it requires hydrogen to insert into and break the strong metal-oxygen bond.

Alternatively, the first step in the hydroxy route involves the addition of hydrogen to the oxygen end of the adsorbed carbonyl resulting in activation barriers that range from 64 to 126 kJ/mol. These barriers are significantly higher than those found to add to the carbon end of the bound carbonyl in the first step of the alkoxy mechanism, but much lower than those required to add to the oxygen of the alkoxy intermediate in step two of the alkoxy mechanism. Similarly, the barriers to add hydrogen to the carbon atom of the strongly bound hydroxy intermediate that forms in the hydroxy route (which range from 70 to 90 kJ/mol) are higher than those required to add to the carbon atom of the weakly held carbonyl but on the same order as those in the first step of the hydroxy mechanism involving the addition of hydrogen to the bound oxygen atom of the bound carbonyl. The similar transition-state

![](./images/813277449742712832_11.jpg)

Fig. 11. Overall energy cycles for hydrogenation of $C_1$—$C_4$ carbonyls via (a) hydroxy route and (b) alkoxy route over Ru(0001). Total energy of a bare ruthenium surface with two adsorbed atomic hydrogen has been taken as reference (zero energy). TS1 and TS2 refer to the transition states for the first and the second hydrogenation steps in both the mechanisms.

energies for the two hydrogen addition steps for the hydroxy mechanism (Fig. 11A) are in sharp contrast to the much higher and lower transition-state energies found in the alkoxy mechanism (Fig. 11B).

The preferred hydrogenation path will depend upon the car- bonyl considered as well as the kinetics, which requires a full accounting of the surface coverages in order to calculate rates. A simple analysis of the kinetics would suggest that for a particular

<table><caption>Table 3 Simulated surface coverages and rate of methanol formation as a function of temperature. The partial pressures of hydrogen and formaldehyde are 100 Torr and 25 Torr, respectively.</caption>
<tbody><tr><td rowspan="2">Temperature</td><td colspan="3">Coverage (ML)</td><td colspan="2">Rate of methanol formation (1/s)</td></tr><tr><td>H</td><td>CH₃O</td><td>CH₂O</td><td>CH₃O* + H* ⇒ CH₃OH</td><td>C*H₂OH + H* ⇒ CH₃OH</td></tr><tr><td>300</td><td>0.22</td><td>0.57</td><td>0.05</td><td>6.13E−02</td><td>7.32E−08</td></tr><tr><td>400</td><td>0.16</td><td>0.44</td><td>0.03</td><td>5.27E+02</td><td>1.05E−05</td></tr><tr><td>425</td><td>0.15</td><td>0.3S</td><td>0.01</td><td>7.19E+02</td><td>1.14E−04</td></tr></tbody></table>

carbonyl, the reaction (via alkoxy rote) can be written by the following sequence of steps:

$$\mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CO}+{ }^{*} \stackrel{K_{\mathrm{R} 1 \mathrm{R} 2 \mathrm{CO}}}{\rightleftarrows} \mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CO}^{*}$$

$$\mathrm{H}_{2}+2^{*} \stackrel{K_{\mathrm{H} 2}}{\rightleftarrows} 2 \mathrm{H}^{*}$$

$$\mathrm{H}^{*}+\mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CO}^{*} \stackrel{K_{1}}{\rightleftarrows} \mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CHO}^{+}+^{*}$$

$$\mathrm{H}^{*}+\mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CHO}^{*} \stackrel{k_{\mathrm{Alk}}}{\rightarrow} \mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CHOH}+2^{*}$$

where $K_{R 1 R 2 C O}$, $K_{H 2}$, $K_{1}$, and $k_{Alk}$ refer to the equilibrium adsorption constant for the reactant carbonyl, the equilibrium adsorption constant for the dissociative adsorption of hydrogen, the equilibrium constant for the first hydrogen addition step, and the rate constant for the rate controlling step, which is considered to be the addition of hydrogen to the bound alkoxide, respectively. The analysis here is similar to that presented by Boudart and Mariadassou [65] for the hydrogenation of cyclohexene to cyclohexane over Pt. In the present example, the most abundant surface intermediate, regardless of the preferred mechanism, is the surface alkoxide as the addition of hydrogen to carbon of the carbonyl is very rapid.

In the alkoxy mechanism, the rate is controlled by the last hydrogen addition step and can be written as:

$$r=k_{\mathrm{Alk}}\left[\mathrm{H}^{*}\right]\left[\mathrm{R}_{1} \mathrm{R}_{2} \mathrm{CHO}^{*}\right]$$

As the alkoxide is thought to cover the surface, its concentration $[R_{1}R_{2}CHO^{*}]$ can be approximated to be equal to the total number of sites [L]. The rate can then be written as:

$$r=k_{\mathrm{Alk}} K_{\mathrm{H} 2}^{1 / 2} P_{\mathrm{H} 2}^{1 / 2} L\left[{ }^{*}\right]$$

where the rate is then half-order in hydrogen, which is consistent with experimental results for the hydrogenation of acetone over Pt in vapor phase [66].

Analyzing the hydroxy mechanism, however, is more difficult as the kinetics is more complicated and thus requires microkinetic simulations.

### 3.4. Hydrogenation kinetics

The DFT-calculated adsorption energies, reaction energies, and activation barriers calculated herein were also used as input to first-principle kinetic Monte Carlo simulation developed previously by Hansen and Neurock [22] to follow the surface chemistry and steady-state kinetics for the hydrogenation of formaldehyde to methanol at constant temperature and constant pressures of formaldehyde and hydrogen. Simulated turnover frequencies for methanol formation were determined by calculating the number of methanol molecules that desorb from the Ru(0001) surface as a function of time per Ru surface atom.

Steady-state kinetic simulations were carried out at constant temperatures (300, 400, and 425 K) and constant partial pressures of formaldehyde ($P_{\text{Formaldehyde}}$ = 25 Torr) and hydrogen ($P_{\text{H2}}$ = 100 Torr), respectively. The results from these simulations are summarized in Table 3. It is clear that at the steady-state conditions, the Ru surface is predominantly covered by methoxy intermediates with coverages of 0.57 ML, 0.44 ML, and 0.38 ML at 300 K, 400 K, and 425 K, respectively. This can be seen in Fig. 12 that shows a snapshot of the Ru surface at steady-state conditions at 300 K. Atomic hydrogen and formaldehyde are also present on the surface at lower coverages that range from 0.22–0.15 and 0.05–0.01 ML, respectively. The total surface coverages were found to decrease from 0.84 ML down to 0.54 ML as the temperature was is increased from 300 K to 425 K.

![](./images/813277449742712832_12.jpg)

Fig. 12. Snapshot from kinetic Monte Carlo simulations of the hydrogenation of formaldehyde over the Ru(0001) surface at steady-state conditions for $T$ = 300 K and $P_{\text{Formaldehyde}}$ = 25 Torr and $P_{\text{H2}}$ = 100 Torr. The blue, grey, red, and white spheres refer to the Ru, C, O, and H atoms, respectively. Under steady-state conditions, the surface is predominantly covered by methoxy with much lower coverages of hydrogen and formaldehyde.

The high surface coverages of methoxy are consistent with the DFT results reported in Fig. 11B that show a low activation barrier for its formation (65 kJ/mol) and a barrier of 124 kJ/mol for its hydrogenation, which is considerably higher than any of the other steps in the hydrogenation of formaldehyde to methanol. The low barrier for the dehydrogenation of the methoxy back to formaldehyde and hydrogen suggests that this step is equilibrated under reaction conditions, which sets the surface methoxy coverage. The kinetically relevant step thus appears to be the hydrogenation of the methoxy to methanol.

Of the two possible hydrogenation paths (alkoxy versus hydroxy), it is found that the rate for hydrogenation via the alkoxy route is significantly higher than the hydroxy route. The results presented in Table 3 indicate that turnover frequencies for methanol were six orders of magnitude higher for the methoxy over the hydroxymethyl route. The simulated TOFs increase with temperature as this decreases the inhibition by methoxy intermediates. While these simulations only follow the hydrogenation of formaldehyde to methanol, the hydrogenation of other aldehydes and ketones examined herein are speculated to show similar results based on their similar potential energy diagrams shown in Fig. 11A and B.

## 4. Summary and conclusions

The hydrogenation of linear $C_1$–$C_4$ oxygenates including formaldehyde, acetaldehyde, propionaldehyde, acetone, butyraldehyde, and methyl ethyl ketone (MEK) over Ru(0001) were examined using first principles periodic density functional theoretical calculations to elucidate the mechanism and understand how changes in the carbonyl and its substituents influence the elementary

reaction energetics. All the aldehydes as well as acetone undergo a rehybridization and bind in a di-σ $\eta^1\eta^2(C,O)$ configuration in order to maximize the interaction of the carbon and the oxygen with the Ru(0001) surface. The bulkier methyl and ethyl substituents bound to central carbon of MEK lead to strong steric repulsion, which drives the carbon end of the molecule from the surface and forces MEK to adsorb via its oxygen atop of Ru in an $\eta^1(O)$ configuration. These DFT results are consistent with experimental results in the literature that suggest that smaller aldehydes have stronger adsorption energies than ketones and tend to undergo rehybridization [44,48,50].

Increasing the substitution at the carbon center of the carbonyl leads to significant steric effects. The adsorption energies decrease by 35, 26, and 10 kJ/mol as methyl substituents were added to formaldehyde to form acetaldehyde, acetone, and methyl ethyl ketone, respectively. The increase in chain length for the aldehydes had a much weaker effect on its adsorption energy (<5 kJ/mol). A similar decrease in adsorption energies was found for the substituted hydroxyalkyl intermediates as they have very similar bonding configurations. The changes in the structure of the alkoxy intermediate had very little effect on its binding energies as the alkoxy binds solely through its oxygen and the carbon substituents are removed from the surface.

The hydrogenation of carbonyls can proceed through either an alkoxy mechanism where the carbon end of the molecule is hydrogenated first or through a hydroxy mechanism in which the oxygen end of the molecule is hydrogenated first. The activation barriers for all four of the different hydrogenation steps were found to correlate with the reaction energies through the Brønsted–Evans–Polanyi relationships. The reaction energies were subsequently found to be linearly related to the adsorption energies for the most strongly bound reactant (or product) that demonstrated the greatest change with changes in substitution. The activation barriers for the formation of the hydroxyalkyl intermediates as well as its subsequent hydrogenation were both found to be directly correlated with the hydroxyalkyl binding energies. The activation barriers for both the formation of the alkoxy intermediate and its subsequent hydrogenation, on the other hand, showed no correlation with the dominant alkoxy binding energies. They were found to be independent of the substituents attached to the carbonyl group since the carbon end of the intermediate is removed from the surface in the transition state.

A comparison of the activation energies and the desorption energies for different aldehydes and ketones on Ru(0001) indicate that they are much more likely to hydrogenate than desorb with the lone exception of MEK, and MEK hydrogenation can proceed but likely requires the presence of more coordinatively unsaturated sites.

A rigorous comparison of the individual activation barriers for the O—H and C—H bond formation steps in the hydroxy and alkoxy mechanisms indicates that alkoxy mechanism has the lowest initial activation barrier as the hydrogen preferentially adds to the carbon over the oxygen. The subsequent hydrogenation of the alkoxy that forms, however, is much more difficult as it has the highest activation energy of all the steps considered. The hydroxy route has activation barriers that lie between the two extreme barriers in the alkoxy mechanism. Regardless of the mechanism, the metal surfaces are likely covered by the alkoxide intermediate under steady-state conditions.

Kinetic analyses as well as first-principles-based kinetic Monte Carlo simulations of hydrogenation of formaldehyde to methanol over Ru(0001) both show that methoxy is most abundant intermediate on the Ru surface at steady-state conditions and the key reactive intermediate. The simulations indicate that methanol is predominantly produced via the alkoxy rather than the hydroxy route.

## Acknowledgments

We would like to thank all of our collaborators in the CARMAC and CASTECH program out of Queens University in Belfast as well as the financial support from the EPSRC under Grant Number GR/S43702/01. The work was also supported by the National Science Foundation under Award No. EEC-0813570. We especially thank Hugh Stitt (Johnson Matthey), Robbie Burch (Queens University), Chris Hardacre (Queens University), David Rooney (Queens University), Kenny Hindle (Queens University), and Lynn Gladden (Cambridge University). We also kindly acknowledge the computational support from the National Centre for Computational Sciences (NCCS) at Oak Ridge National Laboratory and the Environmental Molecular Sciences Laboratory (EMSL) at Pacific Northwest National Laboratory. Both of these are national scientific user facilities sponsored by the Department of Energy's Office of Science.

## References

[1] J.N. Chheda, G.W. Huber, J.A. Dumesic, Liquid-phase catalytic processing of biomass-derived oxygenated hydrocarbons to fuels and chemicals, Angew. Chem.-Int. Ed. 46 (38) (2007) 7164–7183.

[2] P.N. Rylander, Hydrogenation in Organic Synthesis, Academic Press, New York, 1979.

[3] R.L. Augustine, Heterogeneous Catalysts for the Synthetic Chemist, Marcel Dekker Inc., New York, 1996.

[4] R.A. Sheldon, H. van Bekkum, Fine Chemicals through Heterogeneous Catalysis, WILEY-VCH, Weinheim, 2001.

[5] P. Gallezot, D. Richard, Selective hydrogenation of alpha beta-unsaturated aldehydes, Catal. Rev.: Sci. Eng. 40 (1) (1998) 81–126.

[6] F. Delbecq, P. Sautet, A density functional study of adsorption structures of unsaturated aldehydes on Pt(1 1 1): a key factor for hydrogenation selectivity, J. Catal. 211 (2) (2002) 398–406.

[7] S. Laref, F. Delbecq, D. Loffreda, Theoretical elucidation of the selectivity changes for the hydrogenation of unsaturated aldehydes on Pt(1 1 1), J. Catal. 265 (1) (2009) 35–42.

[8] D.Y. Murzin, H. Backman, On selectivity of catalytic reactions with multicentered adsorption, React. Kinet. Catal. Lett. 91 (1) (2007) 141–147.

[9] S. Mukherjee, M.A. Vannice, Solvent effects in liquid-phase reactions: I. Activity and selectivity during citral hydrogenation on Pt/SiO₂ and evaluation of mass transfer effects, J. Catal. 243 (1) (2006) 108–130.

[10] P.N. Rylander, Catalytic Hydrogenation, Academic Press, London, 1985.

[11] K.-i. Aika, H. Sekiya, A. Ozaki, Selectivities of group VIII metals for the hydrogenation of formaldehyde and the effect of support and promoter, Chem. Lett. 12 (3) (1983) 301–304.

[12] R. Hirschl, A. Eichler, J. Hafner, Hydrogenation of ethylene and formaldehyde on Pt (1 1 1) and Pt80Fe20 (1 1 1): a density-functional study, J. Catal. 226 (2) (2004) 273–282.

[13] G.M.R. van Druten, V. Ponec, Hydrogenation of carbonylc compounds: Part I: Competitive hydrogenation of propanal and acetone over noble metal catalysts, Appl. Catal. A 191 (1–2) (2000) 153–162.

[14] R. Alcala, J. Greeley, M. Mavrikakis, J.A. Dumesic, Density-functional theory studies of acetone and propanal hydrogenation on Pt(1 1 1), J. Chem. Phys. 116 (20) (2002) 8973–8980.

[15] S. Kishida, Y. Murakami, T. Imanaka, S. Teranishi, Hydrogenation of various ketones on nickel boride catalyst, J. Catal. 12 (1) (1968) 97–101.

[16] S. Kishida, S. Teranishi, Kinetics of liquid-phase hydrogenation of acetone over Raney nickel catalyst, J. Catal. 12 (1) (1968) 90–96.

[17] C.N. Hinshelwood, Kinetics of Chemical Changes, Clarendon, Oxford, UK, 1940.

[18] N.-S. Chang, S. Aldrett, M.T. Holtzapple, R.R. Davison, Kinetic studies of ketone hydrogenation over Raney nickel catalyst, Chem. Eng. Sci. 55 (23) (2000) 5721–5732.

[19] M. Mavrikakis, M.A. Barteau, Oxygenate reaction pathways on transition metal surfaces, J. Mol. Catal. A: Chem. 131 (1–3) (1998) 135–147.

[20] J.P. Breen, R. Burch, C. Griffin, C. Hardacre, M. Hayes, X. Huang, S.D. O'Brien, Bimetallic effects in the liquid-phase hydrogenation of 2-butanone, J. Catal. 236 (2) (2005) 270–281.

[21] P. Kluson, L. Cerveny, Selective hydrogenation over ruthenium catalysts, Appl. Catal. A 128 (1) (1995) 13–31.

[22] E.W. Hansen, M. Neurock, First-principles-based Monte Carlo simulation of ethylene hydrogenation kinetics on Pd, J. Catal. 196 (2) (2000) 241–252.

[23] P. Hohenberg, W. Kohn, Inhomogeneous electron gas, Phys. Rev. 136 (3B) (1964). B864 LP-B871.

[24] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1993) 558–561.

[25] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Atoms, molecules, solids, and surfaces: applications of the generalized gradient approximation for exchange and correlation, Phys. Rev. B 46 (11) (1992) 6671.

[26] D. Vanderbilt, Optimally smooth norm-conserving pseudopotentials, Phys. Rev. B 32 (1985) 8412-8415.

[27] H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13 (12) (1976). 5188 LP-5192.

[28] G. Mills, H. Jonsson, G.K. Schenter, Reversible work transition state theory: application to dissociative adsorption of hydrogen, Surf. Sci. 324 (2-3) (1995) 305-337.

[29] T.A. Halgren, Merck molecular force field. I. Basis, form, scope, parameterization, and performance of MMFF94, J. Comput. Chem. 17 (5-6) (1996) 490-519.

[30] E. Shustorovich, A.T. Bell, An analysis of formic acid decomposition on metal surfaces by the bond-order-conservation-Morse-potential approach, Surf. Sci. 222 (2-3) (1989) 371-382.

[31] R.J. Madix, G. Ertl, K. Christmann, Preexponential factors for hydrogen desorption from single crystal metal surfaces, Chem. Phys. Lett. 62 (1) (1979) 38-41.

[32] W.T. Tysoe, G.L. Nyberg, R.M. Lambert, Structural, kinetic, and reactive properties of the palladium(111)-ethylene system, J. Phys. Chem. 88 (10) (1984) 1960-1963.

[33] J.K. Vincent, R.A. Olsen, G.-J. Kroes, M. Luppi, E.-J. Baerends, Six-dimensional quantum dynamics of dissociative chemisorption of $H_2$ on Ru(0001), J. Chem. Phys. 122 (4) (2005) 044701-044708.

[34] J. Horiuti, M. Polanyi, Exchange reactions of hydrogen on metallic catalysts, Trans. Faraday Soc. 30 (1934) 1164-1172.

[35] Y. Okamoto, O. Sugino, Y. Mochizuki, T. Ikeshoji, Y. Morikawa, Comparative study of dehydrogenation of methanol at Pt(111)/water and Pt(111)/vacuum interfaces, Chem. Phys. Lett. 377 (1-2) (2003) 236-242.

[36] N.V.T. Pavlenko, A.I. Tripol'skii, G.I. Golodets, Kinetics and mechanism of vapor-phase hydrogenation of propionaldehyde on a platinum catalyst, Kinet. Katal. 30 (6) (1989) 1371.

[37] J. Kua, W.A. Goddard, Oxidation of methanol on 2nd and 3rd row group VIII transition metals (Pt, Ir, Os, Pd, Rh, and Ru): application to direct methanol fuel cells, J. Am. Chem. Soc. 121 (47) (1999) 10928-10941.

[38] Y. Ishikawa, M.-S. Liao, C.R. Cabrera, Oxidation of methanol on platinum, ruthenium and mixed Pt-M metals (M = Ru, Sn): a theoretical study, Surf. Sci. 463 (1) (2000) 66-80.

[39] S.K. Desai, M. Neurock, K. Kourtakis, A periodic density functional theory study of dehydrogenation of methanol over Pt(111), J. Phys. Chem. B 106 (2002) 2559-2568.

[40] J. Greeley, M. Mavrikakis, Competitive paths for methanol decomposition on Pt(111), J. Am. Chem. Soc. 126 (12) (2004) 3910-3919.

[41] S.C. Sparks, A. Szabo, G.J. Szulczewski, K. Junker, J.M. White, Thermal, electron, and photon induced chemistry of acetone on Ag(111), J. Phys. Chem. B 101 (41) (1997) 8315-8323.

[42] J.-P. Jalkanen, F. Zerbetto, Interaction model for the adsorption of organic molecules on the silver surface, J. Phys. Chem. B 110 (11) (2006) 5595-5601.

[43] D. Syomin, B.E. Koel, IRAS studies of the orientation of acetone molecules in monolayer and multilayer films on Au(111) surfaces, Surf. Sci. 498 (1-2) (2002) 53-60.

[44] S.M. Johnston, A. Mulligan, V. Dhanak, M. Kadodwala, The bonding of acetone on Cu(111), Surf. Sci. 548 (1-3) (2004) 5-12.

[45] J.L. Davis, M.A. Barteau, The influence of temperature and surface composition upon the coordination of acetone to the Pd(111) surface, Surf. Sci. 208 (3) (1989) 383-403.

[46] J.L. Davis, M.A. Barteau, Spectroscopic identification of alkoxide, aldehyde, and acyl intermediates in alcohol decomposition on Pd(111), Surf. Sci. 235 (2-3) (1990) 235-248.

[47] C. Houtman, M.A. Barteau, Adsorbed states of acetone and their reactions on rhodium(111) and rhodium(111)-(2×2)oxygen surfaces, J. Phys. Chem. 95 (9) (1991) 3755-3764.

[48] A.B. Anton, N.R. Avery, B.H. Toby, W.H. Weinberg, Adsorption of acetone both on the clean ruthenium(001) surface and on the ruthenium(001) surface modified chemically by the presence of an ordered oxygen adatom overlayer, J. Am. Chem. Soc. 108 (4) (1986) 684-694.

[49] N.R. Avery, EELS identification of the adsorbed species from acetone adsorption on Pt(111), Surf. Sci. 125 (3) (1983) 771-786.

[50] A.B. Anton, J.E. Parmeter, W.H. Weinberg, Adsorption of formaldehyde on the Ru(001) and Ru(001)-p(2×2)O surfaces, J. Am. Chem. Soc. 108 (8) (1986) 1823-1833.

[51] V. Pallassana, M. Neurock, G.W. Coulston, Theoretical density functional analysis of maleic anhydride chemisorption on Pd(111), Re(0001), and bimetallic $Pd_{ML}$/Re(0001) and $Pd_{ML}$/Mo(110) pseudomorphic overlayers, J. Phys. Chem. B 103 (42) (1999) 8973-8983.

[52] A.B. Anton, J.E. Parmeter, W.H. Weinberg, Adsorption and decomposition of formaldehyde on the Ru(001) surface: the spectroscopic identification of .eta.2-formaldehyde and .eta.2-formyl, J. Am. Chem. Soc. 107 (19) (1985) 5558-5560.

[53] M.A. Henderson, Y. Zhou, J.M. White, Polymerization and decomposition of acetaldehyde on rutherium(001), J. Am. Chem. Soc. 111 (4) (1989) 1185-1193.

[54] N.F. Brown, M.A. Barteau, Reactions of 1-propanol and propionaldehyde on rhodium(111), Langmuir 8 (3) (1992) 862-869.

[55] D. Cao, G.-Q. Lu, A. Wieckowski, S.A. Wasileski, M. Neurock, Mechanisms of methanol decomposition on platinum: a combined experimental and ab initio approach, J. Phys. Chem. B 109 (23) (2005) 11622-11633.

[56] T.R. Mattsson, S.J. Paddison, Methanol at the water-platinum interface studied by ab initio molecular dynamics, Surf. Sci. 544 (2-3) (2003) L697-L702.

[57] G. Zilberman, The adsorption of t-butanol on gold - an electrochemical and electrochemical quartz microbalance study, J. Electroanal. Chem. 502 (1-2) (2001) 100-108.

[58] I. Lee, F. Zaera, Enantioselectivity of adsorption sites created by chiral 2- butanol adsorbed on Pt(111) single-crystal surfaces, J. Phys. Chem. B 109 (26) (2005) 12920-12926.

[59] L.J. Shorthouse, A.J. Roberts, R. Raval, Propan-2-ol on Ni(111): identification of surface intermediates and reaction products, Surf. Sci. 480 (1-2) (2001) 37-46.

[60] S.K. Desai, Theoretical Investigation of Solution Effects on Metal Catalyzed Hydrogenation and Oxidation Processes, University of Virginia, Charlottesville, 2002.

[61] M.G. Evans, M. Polanyi, On the introduction of thermodynamic variables into reaction kinetics, Trans. Faraday Soc. 33 (1937) 448.

[62] V. Pallassana, M. Neurock, V.S. Lusvardi, J.J. Lerou, D.D. Kragten, R.A. van Santen, A density functional theory analysis of the reaction pathways and intermediates for ethylene dehydrogenation over Pd(111), J. Phys. Chem. B 106 (7) (2002) 1656-1669.

[63] G.-C. Wang, S.-X. Tao, X.-H. Bu, A systematic theoretical study of water dissociation on clean and oxygen-preadsorbed transition metals, J. Catal. 244 (1) (2006) 10-16.

[64] M. Neurock, V. Pallassana, R.A. van Santen, The importance of transient states at higher coverages in catalytic reactions, J. Am. Chem. Soc. 122 (6) (2000) 1150-1153.

[65] M. Boudart, G.D. Mariadassou, Kinetics of Heterogeneous Catalytic Reactions, Princeton University Press, Princeton, 1984.

[66] F. Rositani, S. Galvagno, Z. Poltarzewski, P. Staiti, P.L. Antonucci, Kinetics of acetone hydrogenation over $Pt/Al_2O_3$ catalysts, J. Chem. Technol. Biotechnol., Chem. Technol. 35 (5) (1985) 234-240.