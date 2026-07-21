# Hydrogenation of 2,4-Dinitro-toluene on Pd/C Catalysts: Computational Study on the Influence of the Molecular Adsorption Modes and of Steric Hindrance and Metal Dispersion on the Reaction Mechanism

Giampaolo Barone and Dario Duca¹

Dipartimento di Chimica Inorganica e Analitica S. Cannizzaro, Università di Palermo, Viale delle Scienze, I-90128 Palermo, Italy

Received December 11, 2001; revised July 12, 2002; accepted July 22, 2002

A new time-dependent Monte Carlo algorithm was developed to simulate isobar and isotherm three-phase batch hydrogenation of 2,4-dinitro-toluene on Pd/C catalysts. A new reaction mechanism was formulated, involving 9 and 27 toluene derivatives, in solution and adsorbed on the surface, respectively. In fact, three different ways of adsorption were considered for all surface derivatives. Microscopic mechanistic hypotheses were formulated analyzing the mimicked surface populations able to reproduce the experimental catalytic activity-selectivity patterns at different times, temperatures, reagent concentrations, and catalyst particle morphologies. The three different adsorption modes, giving rise to surface species having different steric hindrances, together with the morphology of the particle catalysts, were determinants in reproducing experimental findings.

© 2002 Elsevier Science (USA)

**Key Words:** catalytic nitro-derivatives hydrogenation; reaction mechanism; time-dependent Monte Carlo; steric hindrance.

## 1. INTRODUCTION

Catalytic hydrogenation of dinitro-aromatic compounds has industrial relevance (1–8). A significant example is the hydrogenation of 2,4-dinitro-toluene (2,4DNT) to 2,4-diamino-toluene (2,4DAT), which is an important intermediate in the synthesis of toluene-di-isocyanate (1).

The hydrogenation of 2,4DNT was recently investigated in a three-phase batch reactor over palladium/carbon catalysts (9–12). The reaction occurred via a complex network (10, 11), in which the nonseparable 2-nitro-4-hydroxylamino-toluene and 2-hydroxylamino-4-nitro-toluene isomers (4HA2NT and 2HA4NT) (13) and the separable 2-amino-4-nitro-toluene and 2-nitro-4-amino-toluene isomers (4A2NT and 2A4NT) were the main and the only isolable (10) intermediates.

Experimentally, the product distribution was influenced by several factors, including the reaction temperature and the catalyst morphology. Concerning the influence of the catalyst morphology on the catalytic activity and selectivity, it was hypothesized that the 2,4DNT hydrogenation could occur through a “structure-sensitive” (10, 14) mechanism. Hence, it was suggested that the adsorption configurations of the surface species, especially the 2,4DNT species, were affected by the palladium particle sizes, and that this could be the determining factor in regulating the activity and selectivity of the catalyst (10).

Time-dependent Monte Carlo (tdMC) algorithms were recently introduced to mimic metal-catalyzed processes occurring at isobar and isotherm conditions in a biphase reactor. These algorithms generally showed ability in modeling the considered catalytic processes, especially to determine features not easily accessible by experimental data (15, 16) and to rationalize the structure sensitivity observed on catalytic hydrocarbon hydrogenation occurring on different metal catalysts (17–19).

By the tdMC approach, the importance of the side interactions between hindering surface species was shown and parameterized (17–19) and was accounted for (20) in terms of residence probability of the same species.

By this approach, the influence of the metal dispersion, $D_x$ (21–23), of a catalyst on the catalytic activity-selectivity pattern was also taken into account (17, 18). Recently, *ab initio* quantum mechanical (QM) calculations at DFT and HF levels gave thermodynamic bases to the tdMC models (24).

The microscopic aspects of the three-phase hydrogenation of 2,4-dinitro-toluene on Pd surface, due to the intrinsic complexity of the reaction, cannot be easily achieved. These difficulties resulted in contradictory interpretations (see Section 3) of the microscopic aspects of the title reaction even when studied by adequate experimental techniques (9–12, 25). We believe that these difficulties could arise because of the specific ordinary differential equation system (ODES) approaches employed to explain the experimental results. To this purpose, we tried to get these microscopic details by employing an appositely designed tdMC algorithm (26). To our knowledge this is the first example of a tdMC algorithm working on a three-phase batch catalytic reactor system.

¹ To whom correspondence should be addressed. E-mail: dduca@unipa.it

We employed preliminary energetic and structural QM findings (27) to start tdMC simulations of experimental catalytic activity values. The tdMC algorithm, linked to a minimization routine, allowed us to optimize the energetic QM results, employed as fit parameters, to obtain average activation energies, i.e., probabilities of occurrence, at given temperature and catalytic surface characteristics, of simple events involved in the reaction. Together with the best-fit activation energy values, we got snapshots of the surface populations at different reaction times, illustrating the corresponding surface species arrangements.

Isobar hydrogenations, occurring at different temperatures and/or metal dispersions, were also simulated, employing the best-fit parameters. The analysis of the corresponding surface snapshots furnished microscopic insight into the connection between the macroscopic parameters involved in the reaction, i.e., the temperature and/or the metal dispersion and the related catalytic activity-selectivity pattern. This led to new hypotheses on the surface reaction mechanism, alternative to the ones already suggested (9-12, 25).

![](./images/812281391017361409_1.jpg)

SCHEME 1

## 2. ESSENTIAL COMPUTATIONAL DETAILS

### 2.1. Models

The tdMC algorithms, functional for studying the heterogeneous catalytic reactions, usually need the introduction of original chemical and physical models (15-20, 24, 26, 27). The chemical models handle the surface events, such as adsorption, desorption, diffusion, and reaction events, as well as the involved surface species and their characteristics, e.g., steric hindrance and related molecular parking (26, 28) and traffic (27) properties of the same species. The physical models deal with the environment in which the reaction occurs and the related parameters, e.g., the presence of a chemical regime, the reference time unit, the temperature, and the concentration and pressure of the involved species. Both the chemical and the physical models, employed to simulate the title reaction, were discussed in Refs. (26, 27). In the following the essential information is recalled.

To each event, an occurrence probability, $P$, was assigned (15-19) for a given reference time and number of metal surface sites. For a certain event, the value of $P$ was related to that of the activation energy, $E_a$, of the same event (17, 18, 24) by the transition-state theory (TST).

In Scheme 1 the species, disregarding ions and radicals, and the reaction paths hypothesized (both in gas and on surface phase) are shown. A priori, no route was fixed as the rate-determining step.

The acronyms below the species, in Scheme 1, are used in the paper to represent them.

Square matrices, $100 \times 100$, mimicking a mix of {100} and {111} fcc Pd faces, were employed to simulate the metal catalytic surfaces. Since the simulations were not affected by the relative extension of the two different kinds of planes, for the sake of simplicity in the following we refer to the results relative to the {100} fcc Pd system. Stationary boundary conditions and lateral interaction effects were considered (17, 18).

Due to the presence of the solvent in the simulated reaction, formation of surface polymers and/or carbonaceous deposits (26) as well as of second layers on adsorbed species was not allowed. The experimental metal dispersion was mimicked (26), introducing randomly an adequate number of gaps (18), 0-50% of the total surface sites, on the surface matrix. The simulated species were as follows:

- in solution, all the molecules represented in Scheme 1.
- on the surface, for each of the molecules above, the three different surface configurations exemplified, for {100} fcc planes, in Scheme 2 by the black-circle clusters.

The three different surface arrangements for given toluene derivatives were labeled as (26, 27) follows:

- FC, fat constellation (12 surface sites occupied), in which the benzene ring of the toluene derivatives is arranged parallel to the catalyst surface.
- HFC and FFC, hindered-flag and free-flag constellations (respectively, four and three surface sites occupied), having the benzene fragment of the toluene derivatives perpendicular to the Pd surface and the nitrogen fragment, interacting with the surface, in ortho and in para, respectively, to the methyl group.

![](./images/812281391017361409_2.jpg)

SCHEME 2

Both parallel (fat) and tilt (flag) configurations were already observed for aromatic ring derivatives interacting with different metal surface (29–31). Finally, in our model we did not consider any influences by the $\beta$-PdH phase (32) on the title reaction. This is because of the peculiar experimental evidence (25) outlined for the title reaction and because we in general believe (24, 33–35) that in the presence of hydrogenation this phase has trouble forming.

To determine the steric hindrance of the surface constellations, *ab initio* QM calculations at the HF level were performed on model systems of all the derivatives involved in the title reaction (27). More generally, QM calculations were employed to complement the tdMC approach. The methods and the results are extensively described in Ref. (27). Essentially, QM calculations allowed us to evaluate the following:

- the molecular radius of gyration (36), and hence the average volume occupied by the species in solution (26, 27).
- the standard free energy of each reaction step reported in Scheme 1.
- the interaction modes of the molecular species with the catalyst surface.
- the number of hindered sites of the surface species (see Scheme 2).
- the approximate desorption energies of the derivatives in different surface configurations involved in the 2,4DNT hydrogenation.

Using the calculated molecular volumes we could determine, by the diffusion-limited rate constant theory (37), the hitting probability of the solvated species in ethanol phase (26, 27); hence we could set an internal clock to study (15–18, 26, 27) the kinetics of the title reaction.

To reduce the number of fit parameters, the desorption probabilities of the different FC surface species, as well as of the HFC and FFC derivatives adsorbed through equal fragments, were considered the same. The probability of reaction of the $-\text{NO}_2$ and the $-\text{NHOH}$ fragments were also set constant, irrespective of whether considering FC, HFC, or FFC molecular derivatives. These constraints were introduced because of the hypothesized stronger adsorption role in the fat species of the aromatic ring fragment with respect to the nitrogen-containing groups and the analogous reactive behavior of the *ortho* and *para* substituting fragments (26). A comparison between simulation results, obtained by using differently sized sets of fit parameters, induced confidence in the choice made (26).

The tdMC code, implemented in Fortran language as KÖVÉR.FOR, was designed (26) to run in small platforms under LINUX and W98 operative systems.

### 2.2. Fit Procedure

Experimental activity results (see below) of 2,4DNT hydrogenation on a Pd/C catalyst, MGPd5 of Ref. (10), were fitted by a code wherein the fit-kernel KÖVÉR (see previous section) was linked to the AMOEBA minimization routine (38). Experimentally, the catalyst morphology was investigated by XRD, TEM, and CO chemisorption. The CO/Pd ratio, which here is identified with $D_x$, was equal to 0.27 whereas the metal particle size was 4.1 and 4.0 nm by CO chemisorption and TEM, respectively. The reaction was carried out in an ethanol medium (starting concentration of 2,4DNT equal to 0.1 M) at a constant pressure of $\text{H}_2$, 1 atm, in a three-phase batch reactor at 323.15 K. The progress of the reaction was followed by gas–liquid chromatography. The experimental appearance–disappearance ($r^{\pm}$) rates, in the solution phase, per surface metal site per second (26, 27) of the 2,4DNT, 4HA2NT+2HA4NT (HANT), 4A2NT, 2A4NT, and 2,4DAT species, at different reaction times, were reproduced in the fit. The number of times we considered the $r^{\pm}$ values of the five species was 10, homogeneously distributed from 0 to 180 min. The $5\times10$ simulated points were taken each time after pseudo-steady-state conditions (26) were reached on the surface. To reach the surface pseudo-steady state, simulated reaction times of 0.1–10 s were always sufficient. To shorten the fit computer time, each of the 10 simulated instants started on a fresh catalyst surface. The reliability of this approximation, which allows one to reduce by about $10^2$–$10^4$ the magnitude order of the simulated reaction time, was already tested (26).

In Tables 1 and 2 the concentration of the species in solution together with their experimental and simulated values of $r^{\pm}$ at different reaction times and the corresponding refined physical chemical parameters are reported, respectively.

HYDROGENATION OF 2,4-DINITRO-TOLUENE ON Pd/C CATALYSTS

TABLE 1
Experimental and Simulated Concentrations and Appearance–Disappearance Rates ($r^{\pm}$)
(per Surface Metal Site per Second) at Different Times

<table>
<thead>
<tr>
<th>Time<br>(s)</th>
<th>$\rho_{2,4DNT}$<sup>a</sup></th>
<th>$\rho_{HANT}$<sup>a</sup></th>
<th>$\rho_{4A2NT}$<sup>a</sup></th>
<th>$\rho_{2A4NT}$<sup>a</sup></th>
<th>$\rho_{2,4DAT}$<sup>a</sup></th>
<th>$10^{2} \times r_{2,4DNT}^{\pm b}$<br>($\text{s}^{-1}$)</th>
<th>$10^{2} \times r_{HANT}^{\pm b}$<br>($\text{s}^{-1}$)</th>
<th>$10^{2} \times r_{4A2NT}^{\pm b}$<br>($\text{s}^{-1}$)</th>
<th>$10^{2} \times r_{2A4NT}^{\pm b}$<br>($\text{s}^{-1}$)</th>
<th>$10^{2} \times r_{2,4DAT}^{\pm b}$<br>($\text{s}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$0.00 \times 10^{0}$</td>
<td>1.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>$-42.0|-42.0$</td>
<td>$+19.7|+13.0$</td>
<td>$+3.28|+1.70$</td>
<td>$+1.31|+0.25$</td>
<td>$0.00|0.00$</td>
</tr>
<tr>
<td>$1.20 \times 10^{3}$</td>
<td>0.45</td>
<td>0.45</td>
<td>0.07</td>
<td>0.02</td>
<td>0.00</td>
<td>$-42.0|-38.9$</td>
<td>$+19.7|+18.2$</td>
<td>$+3.28|+3.20$</td>
<td>$+0.66|+0.10$</td>
<td>$0.00|0.00$</td>
</tr>
<tr>
<td>$2.40 \times 10^{3}$</td>
<td>0.00</td>
<td>0.80</td>
<td>0.13</td>
<td>0.05</td>
<td>0.02</td>
<td>$0.00|0.00$</td>
<td>$-5.91|-12.0$</td>
<td>$+1.97|+3.80$</td>
<td>$+0.66|+0.10$</td>
<td>$+1.31|+0.20$</td>
</tr>
<tr>
<td>$3.60 \times 10^{3}$</td>
<td>0.00</td>
<td>0.67</td>
<td>0.20</td>
<td>0.07</td>
<td>0.06</td>
<td>$0.00|0.00$</td>
<td>$-5.91|-10.2$</td>
<td>$+1.31|+1.50$</td>
<td>$0.00|0.00$</td>
<td>$+3.94|+0.40$</td>
</tr>
<tr>
<td>$4.80 \times 10^{3}$</td>
<td>0.00</td>
<td>0.55</td>
<td>0.24</td>
<td>0.06</td>
<td>0.15</td>
<td>$0.00|0.00$</td>
<td>$-5.91|-8.20$</td>
<td>$+0.66|+1.30$</td>
<td>$0.00|-0.93$</td>
<td>$+3.94|+0.80$</td>
</tr>
<tr>
<td>$6.00 \times 10^{3}$</td>
<td>0.00</td>
<td>0.39</td>
<td>0.27</td>
<td>0.06</td>
<td>0.27</td>
<td>$0.00|0.00$</td>
<td>$-5.91|-7.32$</td>
<td>$0.00|0.00$</td>
<td>$+0.66|-2.00$</td>
<td>$+6.57|+1.60$</td>
</tr>
<tr>
<td>$7.20 \times 10^{3}$</td>
<td>0.00</td>
<td>0.25</td>
<td>0.22</td>
<td>0.05</td>
<td>0.48</td>
<td>$0.00|0.00$</td>
<td>$-4.60|-5.04$</td>
<td>$-1.97|-0.80$</td>
<td>$-0.66|-3.00$</td>
<td>$+6.57|+2.50$</td>
</tr>
<tr>
<td>$8.40 \times 10^{3}$</td>
<td>0.00</td>
<td>0.15</td>
<td>0.16</td>
<td>0.04</td>
<td>0.66</td>
<td>$0.00|0.00$</td>
<td>$-4.60|-2.00$</td>
<td>$-1.97|-1.00$</td>
<td>$-0.66|-3.00$</td>
<td>$+6.57|+3.00$</td>
</tr>
<tr>
<td>$9.60 \times 10^{3}$</td>
<td>0.00</td>
<td>0.05</td>
<td>0.09</td>
<td>0.00</td>
<td>0.86</td>
<td>$0.00|0.00$</td>
<td>$-1.97|-1.88$</td>
<td>$-1.97|-2.00$</td>
<td>$0.00|0.00$</td>
<td>$+6.57|+4.00$</td>
</tr>
<tr>
<td>$1.08 \times 10^{4}$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.04</td>
<td>0.00</td>
<td>0.96</td>
<td>$0.00|0.00$</td>
<td>$0.00|0.00$</td>
<td>$-1.97|-2.00$</td>
<td>$0.00|0.00$</td>
<td>$+6.57|+5.00$</td>
</tr>
</tbody>
</table>

<sup>a</sup> Experimental (10) and simulated concentrations are coincident. Here concentrations are reported as molar ratios. For the sake of simplicity, in computing the ratios, water was not included among the solution species. The label HANT symbolizes a few of the species, 2HA4NT + 4HA2NT, that were experimentally nonisolated. In the table, + and − symbols represent appearance and disappearance, respectively. Simulations were performed employing the physical chemical parameters of Table 2.

<sup>b</sup> Experimental|simulated appearance–disappearance rate values per surface metal site per second.

The six physical chemical parameters used in the fit, which reproduced the experimental conditions above (26, 27), were the desorption $E_a$ of the FC toluene species interacting with the metal surface through the benzene ring; the three desorption $E_a$ of the HFC and FFC toluene species interacting with the surface sites through the different fragments, $-\text{NO}_2$, $-\text{NHOH}$, and $-\text{NH}_2$; and the two reaction $E_a$ of the $-\text{NO}_2$ ($-\text{NO}_2 \rightarrow -\text{NHOH}$) and $-\text{NHOH}$ ($-\text{NHOH} \rightarrow -\text{NH}_2$) fragments. Of course, averaged $E_a$ refined values, involving the same fragments and actions, could be obtained (Table 2). It must be remarked that despite the dramatic simplification introduced by considering these few $E_a$ parameters, the reaction and desorption abilities of analogous fragments interacting in different configurations with the metallic surface have different occurrence probabilities (see footnote $a$ in Table 2). This clearly shows that the whole activation energy involved in a given process is, as already observed (20, 24), functional to the surface orientation of the implicated group. The QM desorption differential energy values (27) gave indications of the starting magnitude orders of the corresponding $E_a$ fitting parameters. Their final-fit refined values, although in the same order of magnitude, were quite different with respect to the starting ones. This occurrence, mainly attributable to the energetic and geometric effects convoluted in the QM and tdMC model systems studied (26, 27), was extensively discussed in Ref. (27). Conversely, the starting reaction $E_a$ parameters were roughly determined by the analysis of the experimental kinetic plots (8–10, 25).

TABLE 2
Averaged Surface Event Occurrence Probabilities (per Whole Surface Sites per Picosecond at 323.15 K) Normalized to the Number of the Sites Occupied by the Different Surface Species Configurations, and Corresponding Activation Energy Values for the Different Events Considered in the Title Reaction

<table>
<thead>
<tr>
<th>Event</th>
<th>$p^a$</th>
<th>$E_a^b$ (kJ/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$r\text{-NO}_2^c$</td>
<td>$7.8(8) \times 10^{-13}$</td>
<td>79 (5)</td>
</tr>
<tr>
<td>$r\text{-NHOH}^c$</td>
<td>$2.4(1) \times 10^{-12}$</td>
<td>76 (3)</td>
</tr>
<tr>
<td>$d\text{-NO}_2^d$</td>
<td>$1.1(4) \times 10^{-12}$</td>
<td>79 (2)</td>
</tr>
<tr>
<td>$d\text{-NHOH}^d$</td>
<td>$1.0(7) \times 10^{-11}$</td>
<td>73 (6)</td>
</tr>
<tr>
<td>$d\text{-NH}_2^d$</td>
<td>$1.0(9) \times 10^{-06}$</td>
<td>42 (3)</td>
</tr>
<tr>
<td>$d\text{-}\Phi^e$</td>
<td>$1.1(4) \times 10^{-12}$</td>
<td>79 (4)</td>
</tr>
</tbody>
</table>

<sup>a</sup> Determined, by the $E_a$ values, employing TST (17, 18, 24). Note that adsorption of the species occurs on 12 (FC), 4 (HFC), and 3 (FFC) surface sites; hence homonym-event occurrence probabilities, on the same catalytic surface, change for the different configurations. Actually, the probabilities reported in this table are those of hypothetical surface species adsorbed on one site of an otherwise unoccupied surface (maximum probabilities/fresh catalyst). To obtain the probabilities for FC, HFC, and FFC on fresh catalyst, the corresponding values must be divided for the number of surface sites occupied in the different configurations.

<sup>b</sup> $E_a$ values are fit parameters.

<sup>c</sup> $r$-$X$ is the averaged (with respect to different fat and flag molecular configurations) surface reactivity of fragment $X$.

<sup>d</sup> $d$-$X$ represents the averaged (with respect to different flag molecular configurations) desorption ability of fragment $X$.

<sup>e</sup> Average desorption probability of the different fat molecules on the metal surface.

Two more parameters were introduced in the fit procedure. The first one is the hitting configuration probability, HC$Pr$, which estimates the average probability to produce fat or flag surface configuration (the HC$Pr$ of HFC is here arbitrarily fixed equal to that of FFC), following the hit on the surface. The fit procedure pointed out that a given molecule, hitting the surface, has the proper orientation to originate FFC, HFC, and FC surface forms by HC$Pr$ equal to 0.45, 0.45, and 0.10, respectively. Therefore, the

occurrence of the flag configurations is, on average, more probable than the occurrence of the fat configuration.

The second parameter, $K$, was introduced to evaluate the relative amounts between the solution molar ratio of 4HA2NT and 2HA4NT, $K=\rho_{(4 \mathrm{HA} 2 \mathrm{NT})} / \rho_{(2 \mathrm{HA} 4 \mathrm{NT})}$, that were experimentally not determinable (13). In fact, this parameter was defined as $K=\kappa \cdot \rho_{(4 \mathrm{A} 2 \mathrm{NT})} / \rho_{(2 \mathrm{A} 4 \mathrm{NT})}$ and due to the presence of the $\rho$ terms it was variable at the different simulated reaction times. The $\rho$ terms, the molar ratios of the species in brackets, were known by the experiments whereas $\kappa$, fixed for the different simulated reaction times of one fitting run, was the adjustable parameter. After the fitting procedure, the value of $\kappa$ was $0.50(0)$, suggesting that the progress of the reaction increases the amount of the FFC with respect to the HFC surface forms. To obtain the values of the fit parameters, we minimized the function

$$
F=\frac{\sum_{i=1}^{\mathrm{n}}\left|\delta_{\mathrm{p} i}\right|}{\sum_{i=1}^{\mathrm{n}}\left|\varepsilon_{\mathrm{p} i}\right|},
$$

where $\delta_{\mathrm{p}}$ and $\varepsilon_{\mathrm{p}}$ are the differences between simulated and experimental results and the experimental error of the $i$ th point, respectively. The values of $\varepsilon_{\mathrm{p}}$ were fixed equal to $10 \%$ of the reported experimental data (10). Values of $F$ close to 1 validated the fitting model. We needed to consider the $F$ minimization function, because of the presence of many null $\varepsilon_{\mathrm{p}}$ values. In the present case an $F$ resulted equal to 3.4 (5).

After having found out, by the fit procedure, the physical chemical reaction parameters in Table 2, simulations were performed by changing the metal dispersion and temperature. The corresponding activity-selectivity findings, in addition to the analysis of the parallel surface populations, led us to a new mechanistic interpretation, which is the main topic of the next section.

## 3. RESULTS AND DISCUSSION

Starting from the hypotheses and findings of the ODES approaches so far employed (9-12, 25), it is possible to extract the following relevant considerations.

1. Hydrogenation steps should occur on two sites, respectively occupied by one surface hydrogen and one toluene fragment to be hydrogenated (11).
2. Different mechanisms could be hypothesized.
3. A numerical analysis $(9,11)$ of the results concerning the different mechanistic hypotheses, performed using the mean square error between the experimental and simulated results, should be utilizable to determine the reliability of the hypothesized mechanism.
4. The comparison of the results of the numerical analyses can indiscriminately be extended to relate mechanistic models characterized by a different number of fit parameters.
5. The relationships (a) between the catalytic pattern and the adsorption properties of the surface species and (b) between the activity-selectivity pattern and the catalyst particle morphology could be suggested (10, 12, 25).

However, at least two evident inconsistencies arise from the hypotheses and results above. In fact, it is straightforward that point 1 reports a nonphysical constraint whereas the numerical analysis $(9,11)$, summarized in points 3 and 4, if not corroborated by strong experimental and/or modeling findings, is an extremely weak discriminating tool.

Actually, the inspection of the effects of the fit parameters on the surface populations, occurring along with the simulation of the title reaction, is an important test (see point 5a) to verify the heuristic consistency of the same parameters. Both ODES (33-35, 39-41) and tdMC (15-20) methods could be used to carry out this investigation. So, as an example, by using in our tdMC algorithm the opposite of the value of the chemisorption heat of 2,4DNT species, ca. $50 \mathrm{~kJ} / \mathrm{mol}$ (11), as the desorption $E_{a}$ of the same species from a palladium surface, we found that, irrespective of the metal dispersion, the coverage of this surface due to 2,4DNT derivatives, from a $0.1 \mathrm{M}$ solution, at $323.15 \mathrm{~K}$ in the absence of hydrogenation, does not exceed $20 \%$ of the total surface. This should be at least a questionable result (42). An even more ridiculous coverage value (less than $0.1 \%$ ) comes out for the 4HA2NT species, which should have an absolute value of the heat of chemisorption on palladium (desorption $E_{a}$ value) of about $25 \mathrm{~kJ} / \mathrm{mol}$ (11). It must be stressed that such coverage did not depend on the surface configurations FC, FFC, or HFC; we considered, and it was reliant on, only the desorption $E_{a}$ introduced in the simulations.

The same mimicked systems in the presence of hydrogenation (see Section 2.2) also presented unreasonably low values of surface population. For instance, taking an $E_{a}$ value equal to $54.8 \mathrm{~kJ} / \mathrm{mol}$ (11) for the $-\mathrm{NO}_{2} \rightarrow-\mathrm{NHOH}$ surface reactions and disregarding the $-\mathrm{NHOH} \rightarrow-\mathrm{NH}_{2}$ surface routes, at the starting reaction time we found a whole surface coverage of about $15 \%$. In fact, at the starting reaction time, the $-\mathrm{NHOH} \rightarrow-\mathrm{NH}_{2}$ surface event can be ignored due to its occurrence probability, which at 323.15 is 9.5 times lower than that of the $-\mathrm{NO}_{2} \rightarrow-\mathrm{NHOH}$ surface process (11). Actually, it is significant that, using the fit procedure described in Section 2.2, we found a local minimum of the $F$ minimization function originated by $E_{a}$ values lower than that reported in Table 2 and in good agreement with those reported in Ref. (11). However, the corresponding fit solutions were discarded owing to the corresponding surface population observed.

The supposed $-\mathrm{NO}_{2} \rightarrow-\mathrm{NH}_{2}$ surface events (9-11) deserve a final consideration. These routes, having a primary role in the suggested mechanistic hypotheses (9-12, 25), should occur without desorption of the intermediate $-\mathrm{NHOH}$ species, which are produced during the

hydrogenation of the $-\text{NO}_2$ groups. However, the direct reaction $-\text{NO}_2 \rightarrow -\text{NH}_2$ and its central influence on the surface mechanism is in contrast with the assertion explaining that "2,4DNT is adsorbed on the active sites more strongly than 4HA2NT, and consequently only when almost all 2,4DNT has disappeared from the reaction vessel [can] the hydrogenation of 4HA2NT...proceed..." (11). Of course, this statement is a correct interpretation consequent to the very low desorption $E_a$ of the HANT species found by ODES approaches. However, it definitely disagrees with the central role attributed to the surface $-\text{NO}_2 \rightarrow -\text{NH}_2$ route. On the other hand, due to the low HANT desorption $E_a$ values, one should observe, opposite to what experimentally has been found (11), a large amount of dihydroxylamino-toluene species in solution.

After refining, by the fit procedure (see above), the occurrence probability values of Table 2, we used them to simulate experimental activity and selectivity findings at different metal dispersions and/or temperatures. For a better comparison of the simulation results, these were always performed taking into consideration 10,000 active catalyst sites at the starting reaction time, $t=0$ s. This procedure might have contributed to a little disagreement between experimental (not always obtained at $t=0$ s) and mimicked results. The latter are reported in Figs. 1-10. In order to achieve better representation of the simulated results the density of data points in Figs. 4-10 was decreased, without affecting the information furnished, skipping points homogeneously in the time range considered for 66% percent of the original points.

The catalyst relative activity (c.r.a.) is defined as the activity of a catalyst, with a given $D_x$, normalized to the activity of a reference catalyst, which except for the $D_x$ value equal to 0 is identical to the first. This parameter simulated for catalysts having different $D_x$ was reported versus $D_x$ in Fig. 1. The behavior is basically in agreement with the experimental findings (10, 25). A similar agreement with the experimental findings was also achieved for the simulated selectivity to HANT, 4A2NT, and 2A4NT, plotted against $D_x$ in Fig. 2.

![](./images/812281391017361409_3.jpg)

FIG. 2. Selectivity, amount of given produced species normalized to the total amount of the produced species, at $t=0$ s, to 4HA2NT + 2HA4NT (■), 4A2NT (●), and 2A4NT (○) versus catalyst metal dispersion. B-spline lines are used to interpolate the shown points. The experimental conditions simulated are described in Section 2.2.

An Arrhenius plot related to the disappearance of the 2,4DNT is reported in Fig. 3. The corresponding $E_a$ was 60 kJ/mol, which is very close to the experimental one,

![](./images/812281391017361409_4.jpg)

FIG. 1. Disappearance relative rate, at $t=0$ s, per catalyst site per second, of 2,4DNT: catalyst relative activity vs the catalyst metal dispersion; c.r.a. vs $D_x$. The interpolating line is a B-spline. The experimental conditions simulated are described in Section 2.2.

![](./images/812281391017361409_5.jpg)

FIG. 3. Arrhenius plot referring to the $\text{TOF}_{(2,4\text{DNT})}$, disappearance of 2,4DNT per catalytic site per second at $t=0$ s, occurring along with its hydrogenation. In addition to temperature values, the experimental conditions simulated are described in Section 2.2.

![](./images/812281391017361409_6.jpg)

FIG. 4. Surface population found during the hydrogenation of 2,4DNT on catalysts having different metal dispersion. (Solid and open symbols) FFC and HFC, respectively: 2,4DNT (up triangle), 4HA2NT (down triangle), and 2HA4NT (diamond). Flag noising species (circle), fat noising species (cross). B-spline lines join all the points, including the hidden ones, related to the noising species. In addition to $D_x$ values, the experimental conditions simulated are described in Section 2.2.

53.5 kJ/mol (12). The simulated $E_a$ corresponding to the production of HANT species was about 59 kJ/mol. This value, very close to the $E_a$ of the 2,4DNT disappearance, actually shows that the HANT derivatives are the main products of the 2,4DNT hydrogenation.

Here, it must be stressed that any information about the dependence of the catalytic activity-selectivity pattern on the temperature and/or metal dispersion changes was not used in the fit procedure. Hence, the qualitative agreement between the simulated and experimental findings on the dependence above must be considered a validation of the model and of the refined fit parameters found. Therefore, being confident of the parameters obtained by the fit, we tried to picture the microscopic surface populations relative to the findings obtained under different experimental conditions. Figure 4 shows the surface population, expressed as number of molecules of a given species, at the starting reaction time, related to the experimental conditions reported in Section 2.2 at different metal dispersions.

Considering the number of sites occupied by the different surface configurations (see Scheme 2), Fig. 4 shows that the surface species cover above the 65% of the whole surface up to a $D_x$ value equal to 0.6. This value is well in agreement with that of other surface arrangements (18–20) observed during catalytic hydrocarbon hydrogenation. In fact, the present toluene derivatives occupy a wider surface than that occupied by smaller hydrocarbons, namely ethylene. This is not surprising because if larger molecules have border steric hindrance comparable to that of smaller molecules, depending on the $D_x$ values, the larger molecules in the whole may leave on the surface a smaller amount of hindered (unoccupied) sites. Figure 4 shows that the surface population is mainly composed of 2,4DNT, 4HA2NT, and 2HA4NT species. Furthermore, other noising species, both in FFC and HFC forms, represent a low percentage of the occupied surface whereas the FC species are almost absent. Here and in the following, noising species are considered those species that never reach a 1% surface coverage during the simulation time.

In Table 3 some parameters related to the mimicked 2,4DNT surface molar ratios, caused by its hydrogenation and/or adsorption-desorption routes on metal crystallites at different $D_x$, are reported. The sum and the quotient between the surface molar ratios of the 2,4DNT species having

TABLE 3

Parameters Related to the 2,4DNT Surface Molar Ratios on Pd Catalyst When Hydrogenation Is or Is Not Occurring at Different Metal Dispersions

<table>
<thead>
<tr>
<th rowspan="2">$D_x$</th>
<th colspan="2">Presence of hydrogenation</th>
<th colspan="2">Absence of hydrogenation$^{a}$</th>
</tr>
<tr>
<td>$\theta_{FFC}/\theta_{HFC}^{b}$</td>
<td>$\theta_{(FFC+HFC)}^{c}$</td>
<td>$\theta_{FFC}/\theta_{HFC}^{b}$</td>
<td>$\theta_{(FFC+HFC)}^{c}$</td>
</tr>
</thead>
<tbody>
<tr>
<td>0.0</td>
<td>3.7</td>
<td>0.77</td>
<td>4.2</td>
<td>0.92</td>
</tr>
<tr>
<td>0.3</td>
<td>4.5</td>
<td>0.71</td>
<td>4.2</td>
<td>0.87</td>
</tr>
<tr>
<td>0.6</td>
<td>5.1</td>
<td>0.65</td>
<td>4.6</td>
<td>0.80</td>
</tr>
<tr>
<td>0.9</td>
<td>5.7</td>
<td>0.49</td>
<td>4.8</td>
<td>0.56</td>
</tr>
</tbody>
</table>

$^{a}$The simulated experimental conditions are detailed in Section 2.2. Pictorial representations of the surface population are shown in Figs. 4 and 5.

$^{b}$Relative amount between the 2,4DNT, FFC, and HFC surface molar ratios.

$^{c}$Sum of FFC and HFC surface molar ratios for 2,4DNT species.

constellations FFC and HFC, $\theta_{\text{FFC}} + \theta_{\text{HFC}}$ and $\theta_{\text{FFC}}/\theta_{\text{HFC}}$, could be used to justify the observed activity-selectivity pattern. In fact, as $D_x$ increases, the total surface amount of 2,4DNT, $\theta_{\text{FFC}} + \theta_{\text{HFC}}$, decreases. Of course, this can govern the corresponding decreasing activity represented in Fig. 1.

The ratio $\theta_{\text{FFC}}/\theta_{\text{HFC}}$ can be linked to the process of formation of 4A2NT and 2A4NT through the corresponding hydroxylamines, 4HA2NT and 2HA4NT, respectively. Indeed, Fig. 4 shows that 4HA2NT and 2HA4NT species mainly interact with the metallic surface via the hydroxylamino group. In fact, the number of species interacting via the hydroxylamino group is higher, especially for 4HA2NT, and relatively unaffected by $D_x$. Accordingly, in Fig. 2, where on the whole the experimental findings (11,25) on the selectivity pattern are qualitatively reproduced (26), the simulated selectivity to 4A2NT increases with increasing $D_x$ and coherently with the growth of the $\theta_{\text{FFC}}/\theta_{\text{HFC}}$ value.

The parameters of Table 2 should restrictively be used to simulate reaction conditions close to those considered in the fit. However, since the adsorption-desorption process of toluene species containing just $-\text{NO}_2$ and $-\text{NH}_2$ fragments were not affected by the occurrence of hydrogenation (27), we confidently used the fit-refined desorption $E_a$ parameters of these species in the absence of hydrogenation.

In Fig. 5 are shown the mimicked surface populations observed during the 2,4DNT adsorption-desorption processes on differently dispersed Pd surfaces. It is interesting that the FC species are always, almost or totally, absent. This shows that either in the presence or in the absence of hydrogenation, the 2,4DNT FC surface species have little or no effect on the whole reaction. In contrast, just FFC and FC clusters have so far been considered (9-12, 25) in modeling the title reaction. In particular, it was stressed that the 2,4DNT FC species were essential (10) for the *ortho* hydrogenation. The present tdMC approach, which relates the *ortho* hydrogenation of the 2,4DNT species to the presence of the HFC surface derivatives, drastically contrasts with these insights. Furthermore, Table 3 shows that the changes in $\theta_{\text{FFC}}/\theta_{\text{HFC}}$ and in $\theta_{(\text{FFC}+\text{HFC})}$, occurring along with the variation in the $D_x$ values, are more significant in the presence than in the absence of hydrogenation. This clearly suggests that the species produced by the surface transformations cannot, as was implicitly done (10,25), be considered just "onlooker" species. They certainly play an important role in reorganizing the distribution of the available surface sites (27) and indeed they were essential in reproducing the macroscopic effects experimentally observed.

Figure 6 shows the mimicked surface populations occurring along with the 2,4DAT adsorption-desorption processes on Pd surface having different $D_x$ values. In this case, the FC species are the most stable up to $D_x=0.6$. This fact demonstrates that the peculiar properties of the adsorbed species play an important role in determining the surface population. Figure 6 also shows that when the FC species predominate on the metal crystallites, the surface population is dramatically conditioned by the metal $D_x$ values.

Figure 7 shows the simulated surface populations found when the adsorption-desorption routes of the 2A4NT species are mimicked on Pd surface at different $D_x$ values. In this case the FFC surface form is the preferred. Very similar pictures can be obtained if 2A4NT are replaced, in the adsorption-desorption experiment, by 4A2NT. However, in this latter case the predominant surface configuration was the HFC. Clearly, the parking (28) effects here are

![](./images/812281391017361409_7.jpg)

FIG. 5. Surface population found during the 2,4DNT adsorption-desorption process: FFC (●), HFC (○), and FC (+). There was an absence of hydrogen and hence an absence of hydrogenation. The other experimental conditions simulated are described in Section 2.2.

![](./images/812281391017361409_8.jpg)

FIG. 6. Surface population found during the 2,4DAT adsorption-desorption process: FFC (●), HFC (○), and FC (+). There was an absence of hydrogen and the substitution of 2,4DNT by 2,4DAT. The other experimental conditions reproduced by the simulations are described in Section 2.2.

not predominant, the most probable configurations being linked to the adsorbing properties of the group interacting with the metal surface ($-\text{NO}_2$ is more strongly adsorbed than $-\text{NH}_2$).

Figure 8 presents a similar system, in which both the 2A4NT and the 4A2NT species (50% and 50%) were put in contact with a palladium surface. This figure plainly shows the importance of the parking effects for those species hav- ing analogous surface interacting groups, which in spite of this produce different surface steric hindrance. In fact, the relative amount of the FFC is always larger than that of the HFC nitro-amino toluene derivatives and increases along with the $D_x$ values. With respect to this point, it is evident from Figs. 7-9 that the FC is the surface configuration that suffers most from the increasing metal dispersion.

Although the toluene species containing $-\text{NHOH}$ groups undergo, along with the hydrogenation, changes in their adsorption-desorption processes, to obtain qualitative in- formation on these we used the $d\text{-NHOH }E_a$ values of Table 2 even to mimic surface populations in the absence of hydrogenation. Figure 9 shows that at $D_x=0.3$, the FC surface derivatives of the amino-hydroxylamino species

![](./images/812281391017361409_9.jpg)

FIG. 7. Surface population found during the 2A4NT adsorption-desorption process: FFC (●), HFC (○), and FC (+). There was an absence of hydrogen and the substitution of 2,4DNT by 2A4NT. The other experimental conditions simulated are described in Section 2.2.

![](./images/812281391017361409_10.jpg)

FIG. 8. Surface population found during the 2A4NT + 4A2NT (both having a molar ratio equal to 0.5) adsorption-desorption process. 2A4NT and 4A2NT surface population are represented, respectively, in the different configurations as follows: FFC (● and ◆), HFC (○ and ◇), and FC (+ and ×). There was an absence of hydrogen and the substitution of 2,4DNT by the equimolar mixture 2A4NT + 4A2NT. The other experimental conditions simulated are described in Section 2.2.

become quite important (corresponding to a surface mo- lar ratio of ca. 0.15) in determining the composition of the surface population. This, together with the strong surface adsorption via the –NHOH groups of the same molecules, can justify their absence from the solution phase. The anal- ysis of the surface populations performed through investi- gation of the data in Figs. 4–9 suggests that the surface hy- drogenation of 2,4DNT, in outline, starts with an initial flag configuration regime, in which mainly the surface species are arranged perpendicularly to the surface, and ends (in the presence of just 2,4DAT surface derivatives) with a fat con- figuration regime, in which the species are placed parallel to the surface. In between we should have gradual changes from one regime to the other. As already stated, parameter values shown in Table 2, which dynamically change during the reaction, are averaged on the reaction time. Prelimi- nary tdMC simulations on the title reaction performed by variable HCPr, which allows one to follow the change in the adsorption modes of the involved species, were in good agreement with the mechanism above, which, moreover,

![](./images/812281391017361409_11.jpg)

FIG. 9. Surface population found during the 4A2HAT adsorption-desorption process: FFC (●), HFC (○), and FC (+). There was an absence of hydrogen and the substitution of 2,4DNT by 4A2HAT. The other experimental conditions simulated are described in Section 2.2.

![](./images/812281391017361409_12.jpg)

FIG. 10. Surface population found during the hydrogenation of 2,4DNT on a catalyst at different temperatures. (Solid and open symbols) FFC and HFC, respectively: 2,4DNT (up triangle), 4HA2NT (down triangle), and 2HA4NT (diamond). Flag noising species (circle), fat noising species (cross). B-spline lines join all the points, including the hidden ones, related to the noising species. In addition to $T$ values, the experimental conditions simulated are described in Section 2.2.

finds support in the mechanistic explanations obtained by QM studies (27). Concerning this, we recall that both the variable HCPr tdMC findings and the QM results suggest that the absence of dihydroxylamino-toluene species is attributable to a cooperative surface interacting effect due both to the aromatic ring and to the $\text{-NHOH}$ fragments, which strongly fix the DHAT species on the metal surface in a quasi-FC form (27).

The analysis shown in Fig. 10 gives further proof of the complexity, which must be taken into consideration in the interpretation of the chemical systems involving surface processes. This figure shows the simulated surface populations found at different temperatures, in conjunction with the Arrhenius analysis of Fig. 3, on a palladium surface having $D_x = 0.3$. Clearly, the abundance of noising species increases with the temperature while the relative molar ratios of the most significant species change in the surface population. This illustrates that although the logarithmic plot of $\text{TOF}_{(2,4\text{DNT})}$ vs $1/T$ (Fig. 3) is a typical linear Arrhenius plot, the corresponding composition and population of the surface species are soundly affected by the reaction temperature. Since the surface population and composition and the related molecular steric hindrances, as well as the surface orientation and the geometric probability of reaction, are taken into account by the preexponential factor of the Arrhenius equation (37, 43), it can be stated that this also has to depend on the temperature. Hence although Arrhenius analyses on given surface reaction systems are usually performed under the hypothesis that only the exponential term is significantly (37) temperature dependent, we also have to consider that, as in the present occurrence, which we think a general one, the involvement of other important temperature-dependent factors are possible (17). Here, for example, these factors could contribute to the divergence between the $E_a$ values of the $\text{-NO}_2$ group hydrogenation reported in Table 2, ca. 79 kJ/mol, and of the whole 2,4DNT hydrogenation obtained by the Arrhenius analysis of Fig. 3, ca. 60 kJ/mol.

Finally, this computational study showed that the activity-selectivity pattern and the corresponding surface population occurring along with hydrogenation cannot be explained by simply considering metal dispersion effects and/or a bidimensional analogy (10, 25) to the well-known "random parking model" (28) applied to single species, namely 2,4DNT in the FC and FFC forms. Conversely, these dispersion and parking effects are soundly influenced by extra, dynamically evolving surface events, which involve further configurations, HFC, and the ability of adsorption of the different surface species.

So, the morphology of the metal catalyst, the temperature, and the experimental conditions on the whole influence the total amount and composition of the surface population, which effectively affects the catalytic activity-selectivity pattern. To follow the latter we need a method like the tdMC, which, supported by QM studies, gives information on the energetics and kinetics of the system and in parallel monitors the composition and population of the catalyst surface. It is our opinion that the lack of a coupled analysis of both the kinetic and the surface population studies contributed to the failure of the already reported (9-12, 25) ODES approach in studying 2,4DNT hydrogenation.

HYDROGENATION OF 2,4-DINITRO-TOLUENE ON Pd/C CATALYSTS

## 4. CONCLUSION

This study shows that the tdMC algorithm can be used to simulate three-phase batch reactor processes. Many species and their actions, occurring in several phases at different reaction conditions, could be easily mimicked with little computing time needed to reproduce the innermost physical and chemical characteristics of the system. Experimentally noninvestigated aspects and the role of nonisolated species can also be pointed out.

With regard to the title reaction, this work showed the following:

- The morphology of the metal particles and especially the steric hindrance of the different surface species have large influence in driving the reaction mechanism.
- The mechanistic interpretations of the activity-selectivity pattern based on the ODES analyses of the experimental findings are for some items questionable.

Concerning the last point, the role of the surface species, in particular that of 2,4DNT FC derivatives, and the reaction mechanism with the corresponding event activation energies, based on the ODES analyses, was shown to be unrealistic. Hence, they must be reconsidered.

## ACKNOWLEDGMENTS

Thanks are given to the Italian Ministero dell'Istruzione dell'Università e della Ricerca, M.I.U.R., and to the University of Palermo for financial support.

## REFERENCES

1. Stratz, A. M., *in* "Catalysis of Organic Reactions" (J. R. Kosak, Ed.), p. 335. Dekker, New York, 1984.
2. Rylander, P. N., "Catalytic Hydrogenation over Platinum Metals." Academic Press, New York, 1967.
3. Dovell, F. S., Ferguson, W. E., and Greenfield, H., *Ind. Eng. Chem. Prod. Res. Dev.* **9**, 224 (1970).
4. Kut, O. M., Buehlmann, T., Mayer, F., and Gut, G., *Ind. Eng. Chem. Process Des. Dev.* **23**, 335 (1984).
5. Kut, O. M., Yuculen, F., and Gut, G., *J. Chem. Technol. Biotechnol.* **39**, 107 (1987).
6. Janssen, H. J., Kruithof, A. J., Steghuis, G. J., and Westerterp, K. R., *Ind. Eng. Chem. Res.* **29**, 754 (1990).
7. Janssen, H. J., Kruithof, A. J., Steghuis, G. J., and Westerterp, K. R., *Ind. Eng. Chem. Res.* **29**, 1822 (1990).
8. Suh, D. J., Park, T. J., and Ihm, S., *Ind. Eng. Chem. Res.* **31**, 1849 (1992).
9. Neri, G., Musolino, M. G., Bonaccorsi, L., Donato, A., Mercadante, L., and Galvagno, S., *Ind. Eng. Chem. Res.* **36**, 3619 (1997).
10. Musolino, M. G., Milone, C., Neri, G., Bonaccorsi, L., Pietropaolo, R., and Galvagno, S., *Stud. Surf. Sci. Catal.* **108**, 239 (1997).

11. Neri, G., Musolino, M. G., Milone, C., and Galvagno, S., *Ind. Eng. Chem. Res.* **34**, 2226 (1995).
12. Neri, G., Musolino, M. G., Milone, C., Visco, A. M., and Di Mario, A., *J. Mol. Catal. A* **95**, 235 (1995).
13. Neri, G., Musolino, M. G., Rotondo, E., and Galvagno, S., *J. Mol. Catal. A* **111**, 257 (1996).
14. Boudart, M., and Djéga-Mariadassou, G., "Kinetics of Heterogeneous Catalytic Reactions." Princeton Univ. Press, Princeton, NJ, 1984.
15. Duca, D., Botár, L., and Vidóczy, T., *J. Catal.* **162**, 260 (1996).
16. Duca, D., Baranyai, P., and Vidóczy, T., *J. Comput. Chem.* **19**, 396 (1998).
17. Duca, D., La Manna, G., and Russo, M. R., *Phys. Chem. Chem. Phys.* **1**, 1375 (1999).
18. Duca, D., La Manna, G., Varga, Zs., and Vidóczy, T., *Theor. Chem. Acc.* **104**, 302 (2000).
19. Duca, D., Barone, G., and Varga, Zs., *Catal. Lett.* **72**, 17 (2001).
20. Duca, D., Barone, G., Varga, Zs., and La Manna, G., *J. Mol. Struct.* **542**, 207 (2001).
21. Bond, G. C., *Chem. Soc. Rev.* **20**, 441 (1991).
22. Fagherazzi, G., Benedetti, A., Deganello, G., Duca, D., Martorana, A., and Spoto, G., *J. Catal.* **150**, 117 (1994).
23. Deganello, G., Duca, D., Martorana, A., Fagherazzi, G., and Benedetti, A., *J. Catal.* **150**, 127 (1994).
24. La Manna, G., Barone, G., Varga, Zs., and Duca, D., *J. Mol. Struct.* **548**, 173 (2001).
25. Neri, G., Musolino, M. G., Milone, C., Pietropaolo, D., and Galvagno, S., *Appl. Catal. A* **208**, 307 (2001).
26. Barone, G., and Duca, D., *Chem. Eng. J.*, in press.
27. Barone, G., and Duca, D., *J. Mol. Struct.* **584**, 211 (2002).
28. Cooper, D. W., *Phys. Rev. A* **38**, 522 (1988).
29. Xi, M., Yang, M. X., Jo, S. K., and Bent, B. E., *J. Chem. Phys.* **101**, 9122 (1994).
30. Stellwag, C., Held, G., and Menzel, D., *Surf. Sci.* **325**, L379 (1995).
31. Jakob, P., and Menzel, D., *J. Chem. Phys.* **105**, 3838 (1996).
32. Benedetti, A., Fagherazzi, G., Pinna, F., Rampazzo, G., Selva, M., and Strukul, G., *Catal. Lett.* **10**, 215 (1991).
33. Duca, D., Liotta, L. F., and Deganello, G., *J. Catal.* **154**, 69 (1995).
34. Duca, D., Frusteri, F., Parmaliana, A., and Deganello, G., *Appl. Catal. A* **146**, 269 (1996).
35. Duca, D., Arena, F., Parmaliana, A., and Deganello, G., *Appl. Catal. A* **172-II**, 207 (1998).
36. Guinier, A., and Fournet, G., "Small Angle Scattering of X-Rays." Chapman & Hall, London, 1959.
37. Steinfeld, J. I., Francisco, J. S., and Hase, W. L., "Chemical Kinetics and Dynamics," 2nd ed. Prentice Hall, Upper Saddle River, NJ, 1998.
38. Press, W. H., Teukolsky, S. A., Vetterling, W. T., and Flammery, B. P., "Numerical Recipes." Cambridge Univ. Press, Cambridge, U.K., 1992.
39. Duca, D., La Manna, G., and Deganello, G., *Catal. Lett.* **52**, 73 (1998).
40. Dumesic, J. A., Dale, F. R., Aparicio, L. M., Rekoske, J. E., and Treviño, A. A., "The Microkinetics of Heterogeneous Catalysis," ACS Professional References Book. Am. Chem. Soc., Washington, DC, 1993.
41. van Santen, R. A., van Leeuwen, P. W. N. M., Moulijn, J. A., and Averill, B. A., "Catalysis: An Intergrated Approach," 2nd ed. Elsevier, Amsterdam, 1999.
42. Boudart, M., and Djéga-Mariadassou, G., "Kinetics of Heterogeneous Catalytic Reactions." Princeton Univ. Press, Princeton, NJ, 1984.
43. Kaufman, E. D., "Advanced Concept in Physical Chemistry." McGraw-Hill, New York, 1966.