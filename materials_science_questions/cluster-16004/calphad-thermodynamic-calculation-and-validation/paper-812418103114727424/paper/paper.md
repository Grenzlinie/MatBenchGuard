![](./images/812418103114727424_1.jpg)

Available online at www.sciencedirect.com
![](./images/812418103114727424_2.jpg)

Acta Materialia 51 (2003) 1437-1446

![](./images/812418103114727424_3.jpg)
www.actamat-journals.com

# Molecular dynamics simulations of diffusion mechanisms in NiAl

B. Soule De Bas $^{1}$ , D. Farkas $^{*}$

Department of Materials Science and Engineering, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061, USA

Received 12 July 2002; received in revised form 17 September 2002; accepted 21 October 2002

## Abstract

Molecular dynamics simulations of the diffusion process in ordered B2 NiAl at high temperature were performed using an embedded atom interatomic potential. Diffusion occurs through a variety of cyclic mechanisms that accomplish the motion of the vacancy through nearest neighbor jumps restoring order to the alloy at the end of the cycle. The traditionally postulated six-jump cycle is only one of the various cycles observed and some of these are quite complex. A detailed sequential analysis of the observed six-jump cycles was performed and the results are analyzed in terms of the activation energies for individual jumps calculated using molecular statics simulations.

© 2003 Acta Materialia Inc. Published by Elsevier Science Ltd. All rights reserved.

Keywords: Diffusion; Molecular dynamics; Intermetallics

## 1. Introduction

Contrary to the case of pure metals, where the self-diffusion mechanism is well established and consists of a nearest neighbor (NN) jump, the dif- fusion in stoichiometric ordered B2 compounds is much more complex. Two main categories of mechanisms have been postulated to characterize the diffusion in B2 compounds: the mechanisms involving a next nearest neighbor (NNN) jump, where the order is maintained at all times, and cyc- lic mechanisms involving NN jumps that destroy order temporarily.

The NNN jump mechanism can be expected to be energetically favorable based on the fact that there is no disorder created during the process. Thus, Donaldson and Rawlings [1], based on tracer diffusion studies, suggested a NNN mechanism for Ni atoms in the NiGa B2 compound. Theoretical considerations and static computer simulation stud- ies [2], performed for B2 NiAl also suggested the NNN mechanism may be energetically favorable. The NN jump mechanisms can be argued to be less favorable because the atoms jump initially to a site in the wrong sublattice, creating partial disorder in the crystal in the form of antisites. Several mech- anisms have been suggested where the partial order is recovered after a certain number of NN jumps,

* Corresponding author. Tel.: +1-540-231-4742; fax: +1-540-231-8919.
E-mail address: diana@vt.edu (D. Farkas).
1 Currently at Flinders University, Adelaide, Australia

1359-6454/03/$30.00 © 2003 Acta Materialia Inc. Published by Elsevier Science Ltd. All rights reserved.
doi:10.1016/S1359-6454(02)00537-2

constituting a diffusion cycle. The best known of these is the six-jump cycle first postulated by Elcock and McCombie [3] where the vacancy migrates along a definite path of six NN jumps. Since this mechanism was first proposed in 1958, this has been widely accepted as a main diffusion mechanism in B2 ordered alloys. Wynblatt [4], in a study based on $\beta$-AgMg, found that the six-jump cycles were energetically the most favorable. Investigations done with quasi-elastic Mössbauer spectroscopy [5] and nuclear resonant scattering [6] on FeAl showed that the diffusion of Fe in the B2 phase takes place via NN jumps. Similarly, studies done using nuclear neutron scattering [7] on NiGa showed that the Ni atoms diffuse via NN jumps. Other mechanisms have also been proposed, such as the anti-structure bridge [8], where the vacancy migrates through a "bridge" created by an existing antisite, or the antisite-assisted six- jump cycles [9], where the presence of extra anti- sites lowers the activation energy barrier. These additional mechanisms are of interest mainly for the case of non-stoichiometric and partially ordered alloys. Cyclic mechanisms are considered the basic diffusion mechanism in stoichiometric NiAl [9-13], and are assisted by antisite defects present at off-stoichiometric compositions. Recent work has analyzed these cyclic mechanisms in great detail [10-13], but no direct molecular dynamics confirmation of their existence has been reported, to our knowledge.

In the present study, our goal is to observe the mechanisms of diffusion in B2 ordered compounds by direct molecular dynamics. The B2 compound was simulated as an initially homogeneous alloy of stoichiometric composition, in which one vac- ancy was introduced. The potentials used [14] were developed to fit the properties of B2 NiAl. In the following, we first discuss the activation energies predicted by the potentials for the different expected mechanisms. We then present the statisti- cal analysis of the direct observations of the mol- ecular dynamics simulations. We finally report a detailed time evolution analysis of the six-jump cycles observed.

## 2. Computational procedure

Migration energies for the vacancy have been obtained by a simple energy minimization tech- nique in a molecular statics framework [2]. This technique was applied using the potentials of Ref.[14] to NNN vacancy jumps within the same sub- lattice as well as to the NN vacancy jumps involved in traditional {110} six-jump cycles. For these calculations we used a cubic block of nine unit cells along each side, and fully periodic boundary conditions in all directions.

All the statistical analysis reported below is based on simulations using standard molecular dynamics in a constant temperature algorithm. We used a block that is cubic in shape with repeating periodic boundary conditions in the three direc- tions. Our simulation size was of 125 unit cells arranged in a cube of five lattice parameters inside. The vacancy is initially introduced in a Ni site. The block has 249 atoms that are arranged in a per- fectly ordered structure. The lattice parameter used was that of equilibrium at the temperature of the simulations, e.g. 1000-1200 K. For each run, the diffusion processes were studied over a range of750,000 steps using a time step of $2 \times 10^{-3}$ ps. This corresponds to studying the diffusion phenomena during a total time of 1.5 ns. The choice of time step was made as the largest step possible that would not introduce spurious effects in the simul- ation.

Runs were made for several temperatures and at each temperature a number of runs were performed in order to have sufficient statistics of the diffusion mechanisms operating. The details of the diffusion process were studied by monitoring the atom dis- placements initially every 50,000 steps (0.1 ns). During a cycle type mechanism, the atomic dis-placements were monitored much more closely; every 50-100 steps or 0.1-0.2 ps. This allows the study of the details of the mechanism and the exact timing of the various jumps and jump attempts within a particular cycle.

### 2.1. Statistical procedure

For a statistical analysis of the results we classi- fied the diffusion event data according to the differ-

ent mechanisms they represent. A diffusion event was taken to be one or more atomic jumps from initiation to the restoration of the perfect order of the lattice. The different types of events that we observed and report below are: six-jump cycles, 10-jump cycles, 14-jump cycles, and failed attempts with the vacancy returning to the original position. Typically, in order to have sufficient statistics, 50–100 cyclic events were analyzed at each temperature and for each type of vacancy. The six-jump cycles were the most common successful diffusion event. We considered the frequency of the different possible types of six-jump cycles (e.g., the {110} cycle, the {100} straight cycle and the {100} bent cycle [15]). We also differentiated the uninterrupted six-jump cycles from the interrupted ones, where a neutral atom (not involved in the resulting six-jump cycles) jumps to the vacant site and goes back to its previous configuration with the rest of the sequence proceeding normally. The 10-jump cycle is a new mechanism observed in the present investigation, in which the vacancy follows a definite path of 10 jumps. As in the six-jump cycle case, we differentiated the uninterrupted jump cycles from the interrupted ones. The 14-jump cycle is also a new mechanism and in this case, the vacancy follows a definite path of 14 jumps. Details of the new mechanisms are reported below. The category of "failed attempts" refers to events where one or more jumps to nearest neighbor sites occur and are then reversed. All atoms as well as the vacancy go back to their original positions. We report three different situations: the first being where one atom jumps and goes back. In the second type two atoms jump one after another and go back in the opposite order (the second atom goes back and then the first one), and finally the case where more than two atoms jump and go back in successive steps reversing the order of the initial attempt. We also had a few cases of undefined uncompleted cyclic mechanisms. These were not common, and may be an indication of the fact that thermodynamically, a small degree of disorder is expected since the order parameter at 1200 K is close to but not exactly one. Special attention was devoted to detecting possible NNN jumps but, as discussed below, none were observed. We studied in this manner the migration of both Ni and Al vacancies.

## 3. Results
Using the molecular statics method [2], we obtained the activation energy for a NNN jump. The calculated Ni vacancy formation energy is 0.68 eV, and the Ni vacancy migration energy for a NNN jump is 2.07 eV. We also determined the energy–displacement curve for a {110} cycle performed by a Ni vacancy. The result is shown in Fig. 1a. The highest migration energy, corresponding to the third jump is 1.34 eV. This value is lower than the one found for the NNN jump. Based on this approach, the six-jump cycle is expected to be more favorable than the NNN mechanism for this particular potential.

![](./images/812418103114727424_4.jpg)

Fig. 1. Energy–displacement curve for {110} jump cycle of (a) Ni vacancy and (b) Al vacancy.

**Table 1**
Statistical occurrence of the various events observed for a Ni vacancy during 30 ns at 1150 K (15 million time steps)

<table>
  <thead>
    <tr>
      <th>Events</th>
      <th>Specifications</th>
      <th>Values (%)</th>
      <th>Total (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Six-jump cycles</td>
      <td>Uninterrupted</td>
      <td>42.3</td>
      <td rowspan="4">42.3</td>
    </tr>
    <tr>
      <td>Interrupted</td>
      <td>0</td>
    </tr>
    <tr>
      <td>[110] cycles</td>
      <td>78</td>
    </tr>
    <tr>
      <td>[100] straight cycles</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">Ten-jump cycles</td>
      <td>[100] bent cycles</td>
      <td>12</td>
      <td rowspan="2">7.6</td>
    </tr>
    <tr>
      <td>Uninterrupted</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>Fourteen-jump cycles</td>
      <td>Interrupted</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="3">Attempt returning to the original position</td>
      <td></td>
      <td>0</td>
      <td rowspan="3">38.6</td>
    </tr>
    <tr>
      <td>Involving 1 atom</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Involving 2 atoms</td>
      <td>15.4</td>
    </tr>
    <tr>
      <td rowspan="2">Other</td>
      <td>Involving more than 2 atoms</td>
      <td>4</td>
      <td>11.5</td>
    </tr>
    <tr>
      <td></td>
      <td>11.5</td>
      <td></td>
    </tr>
    <tr>
      <td>Total</td>
      <td></td>
      <td></td>
      <td>100</td>
    </tr>
  </tbody>
</table>

**Table 2**
The statistical occurrence of the various events observed for a Ni vacancy during 34.5 ns at 1200 K (17.25 million time steps)

<table>
  <thead>
    <tr>
      <th>Events</th>
      <th>Specifications</th>
      <th>Values (%)</th>
      <th>Total (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Six-jump cycles</td>
      <td>Uninterrupted</td>
      <td>32.8</td>
      <td rowspan="4">40.2</td>
    </tr>
    <tr>
      <td>Interrupted</td>
      <td>7.4</td>
    </tr>
    <tr>
      <td>[110] cycles</td>
      <td>100</td>
    </tr>
    <tr>
      <td>[100] straight cycles</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">Ten-jump cycles</td>
      <td>[100] bent cycles</td>
      <td>0</td>
      <td rowspan="2">5.9</td>
    </tr>
    <tr>
      <td>Uninterrupted</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td>Fourteen-jump cycles</td>
      <td>Interrupted</td>
      <td>1.5</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td rowspan="3">Attempt returning to the original position</td>
      <td></td>
      <td>1.5</td>
      <td rowspan="3">38.9</td>
    </tr>
    <tr>
      <td>Involving 1 atom</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Involving 2 atoms</td>
      <td>26.9</td>
    </tr>
    <tr>
      <td rowspan="2">Other</td>
      <td>Involving more than 2 atoms</td>
      <td>6</td>
      <td>13.5</td>
    </tr>
    <tr>
      <td></td>
      <td>13.5</td>
      <td></td>
    </tr>
    <tr>
      <td>Total</td>
      <td></td>
      <td></td>
      <td>100</td>
    </tr>
  </tbody>
</table>

Empirical interatomic potentials are generally not accurate enough to quantitatively rely on the specific values of the activation energies found for diffusion. Rather, in analyzing results of simulations performed with any empirical potential, the emphasis is on basic mechanisms, such as the six-jump cycle itself, the coordination of jumps observed and the possibility of new diffusion mechanisms not postulated before. We therefore concentrate in the rest of the present work on a detailed analysis of the mechanisms observed.

The results of the MD simulations for a Ni vacancy at 1150 K are presented in Table 1. We also ran simulations at 1200 K with very similar results, as shown in Table 2. The six-jump cycles are the primary mechanism involved in the diffusion process. These account for about 40% of the total events observed. Some of the six-jump cycles are interrupted by the inclusion of an extra jump at some point within the cycle. The process returns then to the normal path and ends in a configuration totally equivalent to the uninterrupted case.

The interrupted six-jump cycles correspond to 19% of all the six-jump cycles. Differentiating the different types of six-jump cycles, we see that they are mainly are {110} cycles. Thus at 1200 K we

<table>
<caption>Table 3
Statistical occurrence of the various events observed for an Al vacancy during 27.5 ns at 1100 K (13.75 million time steps)</caption>
<thead>
<tr>
<th>Events</th>
<th>Specifications</th>
<th>Values (%)</th>
<th>Total (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">Six-jump cycles</td>
<td>Uninterrupted</td>
<td>11.9</td>
<td rowspan="5">11.9</td>
</tr>
<tr>
<td>Interrupted</td>
<td>0</td>
</tr>
<tr>
<td>[110] cycles</td>
<td>100</td>
</tr>
<tr>
<td>[100] straight cycles</td>
<td>0</td>
</tr>
<tr>
<td>[100] bent cycles</td>
<td>0</td>
</tr>
<tr>
<td rowspan="5">Six-jump cycles—Ni vacancy type</td>
<td>Uninterrupted</td>
<td>9.2</td>
<td rowspan="5">10.5</td>
</tr>
<tr>
<td>Interrupted</td>
<td>1.3</td>
</tr>
<tr>
<td>[110] cycles</td>
<td>100</td>
</tr>
<tr>
<td>[100] straight cycles</td>
<td>0</td>
</tr>
<tr>
<td>[100] bent cycles</td>
<td>0</td>
</tr>
<tr>
<td rowspan="2">Ten-jump cycles</td>
<td>Uninterrupted</td>
<td>1.3</td>
<td rowspan="2">1.3</td>
</tr>
<tr>
<td>Interrupted</td>
<td>0</td>
</tr>
<tr>
<td rowspan="3">Attempt returning to the original position</td>
<td>Involving 1 atom</td>
<td>57.9</td>
<td rowspan="3">72.4</td>
</tr>
<tr>
<td>Involving 2 atoms</td>
<td>7.9</td>
</tr>
<tr>
<td>Involving more than 2 atoms</td>
<td>6.6</td>
</tr>
<tr>
<td>Other</td>
<td></td>
<td>3.9</td>
<td>3.9</td>
</tr>
<tr>
<td>Total</td>
<td></td>
<td></td>
<td>100</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4
Statistical occurrence of the various events observed for an Al vacancy during 15 ns at 1150 K (7.5 million time steps)</caption>
<thead>
<tr>
<th>Events</th>
<th>Specifications</th>
<th>Values (%)</th>
<th>Total (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">Six-jump cycles</td>
<td>Uninterrupted</td>
<td>2.3</td>
<td rowspan="5">9</td>
</tr>
<tr>
<td>Interrupted</td>
<td>6.7</td>
</tr>
<tr>
<td>[110] cycles</td>
<td>100</td>
</tr>
<tr>
<td>[100] straight cycles</td>
<td>0</td>
</tr>
<tr>
<td>[100] bent cycles</td>
<td>0</td>
</tr>
<tr>
<td rowspan="5">Six-jump cycles—Ni vacancy type</td>
<td>Uninterrupted</td>
<td>4.5</td>
<td rowspan="5">4.5</td>
</tr>
<tr>
<td>Interrupted</td>
<td>0</td>
</tr>
<tr>
<td>[110] cycles</td>
<td>100</td>
</tr>
<tr>
<td>[100] straight cycles</td>
<td>0</td>
</tr>
<tr>
<td>[100] bent cycles</td>
<td>0</td>
</tr>
<tr>
<td rowspan="2">Ten-jump cycles</td>
<td>Uninterrupted</td>
<td>2.4</td>
<td rowspan="2">2.4</td>
</tr>
<tr>
<td>Interrupted</td>
<td>0</td>
</tr>
<tr>
<td rowspan="3">Attempt returning to the original position</td>
<td>Involving 1 atom</td>
<td>61</td>
<td rowspan="3">77.2</td>
</tr>
<tr>
<td>Involving 2 atoms</td>
<td>13.8</td>
</tr>
<tr>
<td>Involving more than 2 atoms</td>
<td>2.4</td>
</tr>
<tr>
<td>Other</td>
<td></td>
<td>6.9</td>
<td>6.9</td>
</tr>
<tr>
<td>Total</td>
<td></td>
<td></td>
<td>100</td>
</tr>
</tbody>
</table>

have 100% of {110} six-jump cycles. These results agree with the reports of most studies that estimate the {110} cycle to be the most probable one. The 10-jump cycles correspond to about 6% of the events. These include the regular and the interrupted 10-jump cycles. The statistical occurrence of these events is lower than that corresponding to the six-jump cycle. The 14-jump cycle is a rare event. The failed cycle attempts account for 38.9% at 1200 K. Most of these are cycle attempts that are reversed after the second jump. This can be understood on the basis of the potential energy curve in

![](./images/812418103114727424_5.jpg)

Fig. 2. (a) First example of displacement versus time curve of a {110} jump cycle of a Ni vacancy. (b) Second example of a displacement versus time curve of a {110} jump cycle of a Ni vacancy.

![](./images/812418103114727424_6.jpg)

Fig. 3. (a) First example of displacement versus time curve of a {110} jump cycle of an Al vacancy. (b) Second example of a displacement versus time curve of a {110} jump cycle of an Al vacancy.

Fig. 1. If the system has enough energy to accomplish both jump 1 and 2, it is in a local valley. It is then reasonable that the system has a significant probability of going back to its original position rather than completing jump 3 because the energy barrier for jump 3 is slightly higher than that needed for reversing jump 2.

In the final category “other”, the final configuration of the run is complex and temporarily disordered. This probably corresponds to the fact that at this temperature the equilibrium state of the system is still very close to perfect order but the equilibrium order parameter is already somewhat lower than unity. These complex diffusion paths can thus be interpreted as resulting from the small deviation of perfect order, which already occurs at this temperature.

In the case of a Ni vacancy for the potential used here and according to the activation energy values (Fig. 1), the six-jump cycle is expected to be more favorable than the NNN mechanism. In agreement with this expectation, the latter mechanism was not observed in our simulations. A similar conclusion is reached for the migration of Al vacancies. The corresponding migration energies are shown in Fig. 1b. Tables 3 and 4 show the statistical data for the various jump sequences observed for an Al vacancy.

In Fig. 2 we show the $x$ displacements of the three jumping atoms along the $x$ direction as a function of time, for two representative six-jump cycles of the Ni vacancy observed at 1200 K. For a detailed sequential analysis of the cycle it is sufficient to analyze displacements in only one direction, since this indicates precisely when the jump occurs. The displacement allows the precise identification of when each jump in the cycle occurs.

![](./images/812418103114727424_7.jpg)

Fig. 4. Graphical representation of a Ni vacancy {110}-type 10-jump cycle: (a) first configuration; (b) second configuration.

Fig. 3 shows two representative cycles for the Al vacancy.

The total time that it takes to complete a cycle for a Ni vacancy varies from 15 to 45 ps. This is much shorter than the average time between cycles, which is 840 ps. Our detailed analysis shows that within the sequence, some specific jumps are correlated. In the first sequence, reported in Fig. 2a, jumps 1-2, 3-4, and 5-6 clearly occur together and can be seen as coordinated. In the second sequence (Fig. 2b), we have again coordinated jumps. There is a failed attempt for jump 3 by itself, followed by the coordinated jumps 5 and 6 completing the sequence. On the basis of the activation energy curve reported in Fig. 1, the fact of correlating the jumps 1-2, 3-4, and 5-6 can be seen as a way of minimizing residence time at the high-activated states. The migration energy results clearly suggest that jumps 3 and 4 should occur together, since there is no valley in between these states. In the case of jumps 1-2 and 5-6 there is a valley between the two states, but it is small and the jumps often occur anyway in a coordinated manner.

A similar analysis is valid for the cycles of the Al vacancy. Two examples are shown in Fig. 3. The statistical analysis for the Al vacancy at two different temperatures is reported in Tables 3 and 4. In this case the first jump actually decreases the energy (see Fig. 1b), so that there is a large fraction of failed attempts to initiate the cycle that are reversed after the first jump. The times that it takes to complete the cycles of the Al vacancy were observed to up to 500 ps, significantly longer than the corresponding ones for the Ni vacancy.

## 4. New cyclic mechanisms observed

The molecular dynamics investigation stresses the contribution of two new cyclic mechanisms to the diffusion process: the 10- and 14-jump cycles. These two mechanisms are seen to be less common than the six-jump cycles but have nonetheless an

![](./images/812418103114727424_8.jpg)

Fig. 5. Graphical representation of an Al vacancy {100}-type 10-jump cycle.

influence on the overall diffusion, especially the 10-jump cycles. The two following sections present an analysis of these mechanisms that is derived from the molecular dynamics investigation described below.

### 4.1. 10-Jump cycle mechanism

The 10-jump cycle is a new mechanism involving five atoms wherein the vacancy migrates following a definite path of 10 jumps. The migration of the vacancy occurs via NN sites destroying the partial order of the system. However, the order is recovered when the sequence is completed. A detailed analysis of the observed 10-jump cycle highlights two main types. The first type of mechanism consists of a vacancy and five jumping atoms distributed in two parallel {110}-type planes. Two different configurations are observed for this {110} type of 10-jump cycle. The first configuration is shown in Fig. 4a and corresponds to a vacancy and three jumping atoms lying in the same {110} plane and two other atoms located in a plane parallel to the first one. The second configuration observed is shown in Fig. 4b and consists of a vacancy and four jumping atoms lying in the same {110} plane and one atom positioned above or below this plane. In this configuration, the vacancy migrates along a ⟨111⟩-type vector and ends up in its original plane. For the first type of configuration, it migrates along a ⟨110⟩-type vector and finishes in a parallel {110} plane. This first configuration is the most common type of 10-jump cycle observed, accounting for 67% of those observed. The second type of {110} 10-jump cycle is less frequent and corresponds to 16% of the observed 10-jump cycle. Fig. 4a and b illustrates the Ni vacancy performing a {110} 10-jump cycle in the two above-mentioned configurations, respectively. Another type of 10-jump cycle consists of a vacancy and three jumping atoms lying in the same {100}-type plane and two other atoms within another plane perpendicular to the first one. This is a {100} 10-jump cycle. The vacancy migrates along a ⟨110⟩-type vector and ends up in the same plane as it was initially. This type of 10-jump cycle is not very common, representing 17% of the observed 10-jump cycles.

The first five steps of both the {110} and {100} 10-jump cycles are identical to the first five steps of the six-jump cycle they correspond to. For both configurations of the {110} 10-jump cycle (see Fig. 4), the first five atomic migrations occur within a same {110} plane as in a [110] six-jump cycle. In a {100} 10-jump cycle the first five steps correspond to the first five steps of a [100] bent six-jump cycle. The next step differs from classical six-jump cycles because of the two extra atoms that accomplish their first NN jumps as steps 6 and 7. The third atom is then completing its second NN jump in step 5. Finally the fourth and fifth atoms complete the 10-jump sequence jumping back to their own sublattice. The order of the system is then recovered.

From the geometrical analysis above, the 10-jump cycles are seen to be very similar to six-jump cycles. However, the MD statistical results show that their contribution to the overall diffusion is much less important than that of the six-jump cycles. On the basis of geometric considerations,

![](./images/812418103114727424_9.jpg)

Fig. 6. Graphical representation of a {110}-type 14-jump cycle.

it is seen that the point defect configurations introd- ucing the largest local disorder are identical for both six- and 10-jump cycles. The most unfavor- able configuration is that of $2Al_{Ni}+Ni_{Al}+V_{Al}$ and occurs for both the six- and 10-jump cycles. This consideration may suggest that the two cyclic mechanisms have a similar highest activated state (Fig. 5).

### 4.2. 14-Jump cycle mechanism

The 14-jump cycle is a new mechanism involv- ing seven atoms wherein the vacancy migrates fol- lowing a definite path of 14 jumps. Similarly to the six- and 10-jump cycles, the migration of the vacancy occurs via NN sites destroying tempor- arily the partial order of the system. This mech- anism is rare and has only been observed in the case of a Ni vacancy migration at 1200 K. As illus- trated in Fig. 6, the 14-jump cycle consists of a vacancy and six jumping atoms lying in the same {110}-type plane with an extra atom located below or above this plane. The vacancy migrates along a {100}-type vector and ends up in the same plane as it was originally. The first nine steps of the 14- jump cycle are identical to the first nine steps of a {110}-type 10-jump cycle shown in Fig. 4. Steps10 and 11 correspond to the first NN jumps of the two extra atoms involved. The fifth atom com- pletes its second NN jump going back in its own sublattice (see step 12 in Fig. 6). Finally, the two extra atoms achieve the 14-jump sequence recovering the perfect order of the crystal. Three atoms migrate in a first NNN site and four migrate in a second NNN site. The intermediate point defect configurations show that there is also a con- figuration introducing the largest local distortion of $2Al_{Ni}+Ni_{Al}+V_{Al}$ (see steps 3, 7 and 11 in Fig. 6). This configuration is again similar to the most unfavorable configuration in a six-jump cycle.

## 5. Conclusions

Direct molecular dynamics simulations of the diffusion process in ordered B2 NiAl at high temperature were performed using an embedded atom interatomic potential. We were able to follow the diffusion process and obtain a statistical analysis of the most likely diffusion mechanisms. As predicted by the calculated activation energies, we observed a large majority of diffusion events for a Ni vacancy to be the standard {110} six-jump cycle postulated in 1958. Detailed time evolution analysis of this six-jump cycle showed a strong tendency in this type of cycle to occur in a coordinated way, with jumps 1 and 2 occurring at about the same time, followed by jumps 3 and 4 and then 5 and 6. The study also revealed two new mechanisms, the 10- and 14-jump cycle that contribute to the diffusion process.

## Acknowledgements

This work was supported by the National Science Foundation, under grant DMR 97-53243.

We also acknowledge many helpful discussions with Dr Yuri Mishin.

## References

[1] Donaldson AT, Rawlings RD. Acta metall. 1976;24:285.
[2] Mishin Y, Farkas D. Phil. Mag. A 1997;75:1.
[3] Elcock EW, McCombie CW. Phys. Rev. 1958;109:6.
[4] Wynblatt P. Acta metall. 1967;15:1453.
[5] Vogl G, Sepiol B. Acta metall. mater. 1994;42:3175.
[6] Sepiol B, Czihak C, Meyer A, Vogl G, Metge J, Rüffer R. Hyperfine Interact. 1998;113:449.
[7] Kaisermayr M, Combet J, Ipser H, Schicketanz H, Sepiol B, Vogl G. Phys. Rev. B 2000;61:18.
[8] Kao CR, Chang YA. Intermetallics 1993;1:237.
[9] Athène M, Bellon P, Martin G. Phil. Mag. A 1997;76:3.
[10] Drautz R, Meyer B, Fahnle M. In: Defect and Diffusion Forum 194-1, 2001, pp. 417-22.
[11] Divinski SV, Herzig C. Intermetallics 2000;8:1357-68.
[12] Belova IV, Murch GE. Phil. Mag. A 2000;80:1481-93.
[13] Drautz R, Fahnle M. Acta mater. 1999;47:2437-47.
[14] Farkas D, Mutasa B, Vaihlé C, Ternes K. Model. Simul. Mater. Sci. Eng. 1995;3:201.
[15] Arita M, Koiwa M, Ishioka S. Acta metall. 1989;37:1363.