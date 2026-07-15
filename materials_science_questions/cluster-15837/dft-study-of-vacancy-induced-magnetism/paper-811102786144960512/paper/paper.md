PCCP

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: E. German and R.
Gebauer, Phys. Chem. Chem. Phys., 2016, DOI: 10.1039/C6CP05993G.

![](./images/811102786144960512_1.jpg)

This is an Accepted Manuscript, which has been through the
Royal Society of Chemistry peer review process and has been
accepted for publication.

Accepted Manuscripts are published online shortly after
acceptance, before technical editing, formatting and proof reading.
Using this free service, authors can make their results available
to the community, in citable form, before we publish the edited
article. We will replace this Accepted Manuscript with the edited
and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the
author guidelines.

Please note that technical editing may introduce minor changes
to the text and/or graphics, which may alter content. The journal's
standard Terms & Conditions and the ethical guidelines, outlined
in our author and reviewer resource centre, still apply. In no
event shall the Royal Society of Chemistry be held responsible
for any errors or omissions in this Accepted Manuscript or any
consequences arising from the use of any information it contains.

![](./images/811102786144960512_2.jpg)

rsc.li/pccp

# Hydrogen divacancy diffusion: a new perspective on H migration in MgH₂ materials for energy storage

Estefania German¹,²,* and Ralph Gebauer²

¹ Departamento de Física, Universidad Nacional del Sur & IFISUR (UNS-CONICET), Av. Alem 1253, 8000, Bahía Blanca, Argentina.

² The Abdus Salam International Center for Theoretical Physics (ICTP), Strada Costiera 11, 34151, Trieste, Italy.

*corresponding author email: egerman@uns.edu.ar

Tel: +54 291 4882982 int. 33

## Abstract

The formation and diffusion of pairs of hydrogen vacancies (divacancies) in magnesium hydride is modeled using density functional theory. Compared to the commonly studied case of single hydrogen vacancies, it is found that divacancies are energetically favored over two isolated vacancies. Also, as a function of the diffusion axis considered, the calculated diffusion barriers of divacancies are either smaller or of comparable magnitude with respect to the diffusion barriers of a single vacancy. These findings shed new light on hydrogen transport in MgH₂, which is of crucial importance to understand the kinetics of hydrogen take-up and release in this storage material.

Keywords: DFT; energy; storage; hydrogen; diffusion; magnesium

### Introduction

A renewable and clean replacement of fossil fuels is an essential requirement to address the global challenge of anthropogenic climate change. One of the important bottlenecks for a more widespread use of solar or wind energy is represented by the need to store the energy of such intermittent sources and to allow their use also for mobile applications, like transportation. The storage of energy in the form of chemical fuels like hydrogen is considered very promising because of several attractive features: a high gravimetric energy content and near zero CO₂ emissions when used in conjunction with a fuel cell ¹⁻². However, there are still many challenges concerning the compact and safe storage as well as the transportation of hydrogen ³⁻⁸. The general goal is to find materials which can store hydrogen and take and release H₂ efficiently.

The interest in magnesium hydride as a storage material is prompted because of its promising properties, like a very high gravimetric capacity (7.6 wt %), abundance, and low cost ⁹. Nevertheless, there still exist several drawbacks regarding practical mobile applications, amongst which high thermodynamic stability and slow kinetics in the absorption and desorption of H₂. These features are linked to the slow H diffusion inside the hydride and at the Mg/MgH₂ interface. In order to overcome these obstacles, some experimental and theoretical studies have been done, like doping of the hydride with transition metals (like Nb, Zr, Ti among others) ¹⁰⁻¹⁷ and shortening the path for H diffusion using nanostructures or thin films ¹⁸.

In particular the hydrogen vacancy diffusion in the hydride is a rate-determining step when it comes to absorption and release of H₂, limiting the use of MgH₂ for practical hydrogen

storage. A better understanding of how the diffusion mechanism occurs can help to find a way to accelerate this process. Several studies have been published concerning hydrogen single vacancy diffusion $^{19-21}$, and how to improve it using transition metals as dopants $^{22-23}$.

However, only little is known about hydrogen divacancy formation and its kinetics. R. Crespo et al. have calculated theoretically the divacancy formation energy in bulk $MgH_2$ $^{24}$ and A. J. Du et al. have also studied the (110) surface $^{25}$. In both studies it was found that when two hydrogen vacancies are close enough, less energy is required for their generation. To the best of our knowledge there exist no studies regarding the diffusion of hydrogen divacancies, i.e. the diffusion of vacancies as a pair. One key problem is the difficulty to determine diffusion mechanisms experimentally on an atomic scale. First-principles calculations can help to shed some light on the microscopic level of the diffusion processes.

In the following, we present a computational study of hydrogen divacancy formation energies and divacancy diffusion barriers in bulk magnesium hydride using density functional theory.

## Computational Methodology

Density functional theory calculation were performed to determine energetic and structural properties of pure and defected $MgH_2$ systems. We employed version 5.1 of the quantum-ESPRESSO suite of electronic structure codes $^{26}$. We have selected the generalized gradient approximation (GGA) with the Perdew-Wang-91 (PW91) functional $^{27-28}$ for most calculations. Because of the open-shell nature of the defective systems, it is important to assess the accuracy of the PW91 computations shown here. We did this by employing also

the hybrid functional PBE0 $^{29}$. Because of the heavy computational load of hybrid functionals, we used PBE0 only for single-point calculations along the paths which were previously determined at the PW91 level of theory.

The electron-ion interactions were modeled using Vanderbilt's ultrasoft pseudopotentials (USPP) $^{30}$. Namely, H.pw91-van_ak.UPF for hydrogen and Mg.pw91-np-van.UPF for magnesium, both pseudopotentials are available from the Quantum ESPRESSO Web site $^{31}$. The employed pseudopotentials correspond to the following electronic configurations: $1s^1$ for H and $2p^6\,3s^2$ for Mg. This choice amounts to a valence of 1 for H and 8 for Mg. A plane-wave cutoff energy of 35 Ry was used for the Kohn-Sham orbitals, and 350 Ry for the charge density. We checked that higher cutoff values did not affect significantly the results. As in our previous work regarding single hydrogen vacancies in MgH$_2$ $^{22}$, the studied structures were modeled using a supercell containing 162 atoms (27 unit cells of MgH$_2$). The Brillouin-zone was sampled using a $2\times2\times2$ Monkhorst-Pack grid $^{32}$. For the diffusion study, which consists in the determination of energy barriers and reaction pathways, we used the nudged elastic band (NEB) method $^{33-37}$. The Broyden optimizer was used to move the system under the NEB forces towards the minimum energy path (MEP). To move the highest energy image to the saddle point along the reaction coordinate, the climbing image algorithm was utilized with the NEB calculations. For each barrier, seven images in total were used to explore the potential energy along the MEP. Forces were converged below 0.05 eV/Å. We have selected paths of length equal or minor than a lattice parameter, except for one of 4.80 Å. In a previous work, $^{38}$ we calculated lattice parameters for the pristine MgH$_2$ cell, which has a rutile type tetragonal structure (P42/mnm, group No. 136), characterized by a lattice parameter a and the c/a ratio, a= 4.501 Å, c/a = 0.6674,

$u = 3.22$ Å. The Wyckoff positions for Mg and H are 2a (0, 0, 0) and 4f (0.304, 0.304, 0) respectively. These results are in agreement with experimental values. As mentioned above, hydrogen divacancies ($v\text{H}_2$) were considered in these systems, the extracted hydrogen atoms are numbered in Figure 1 and the formation energy of divacancies were calculated following the equation:

$$
\text{FEVH}_2 = \text{E}\ (\text{Mg}_{54}\text{H}_{108-2}) + \text{E}\ (\text{H}_2) - \text{E}\ (\text{Mg}_{54}\text{H}_{108})
$$

where $\text{E}\ (\text{Mg}_{54}\text{H}_{108-2})$ is the energy of the bulk $\text{MgH}_2$ containing a H divacancy, $\text{E}\ (\text{H}_2)$ is the energy of hydrogen gas and $\text{E}\ (\text{Mg}_{54}\text{H}_{108})$ is the energy of the pure system, i.e. without vacancies. As it can be seen in Figure 1, the supercell used is formed by 54 Mg atoms and 108 H atoms. For each case, the H atoms are indicated which were removed to form a divacancy.

![](./images/811102786144960512_3.jpg)

Figure 1. $\text{MgH}_2$ supercell and numbering of extracted hydrogen atoms to generate divacancies.

Apart from the mere formation of a divacancy, it is worth to study its diffusion as a pair of vacancies inside the crystal and to check whether diffusion is isotropic in this crystal. Therefore, we have considered various migration paths in the three Cartesian directions, namely along the $x$-axis from V2V3 to V11V12, along the $y$-axis from V2V3 to V8V9 and along the $z$-axis from V2V3 to V5V6 (see Figure 1). In this way, possible diffusion paths in all three dimensions are covered.

Our calculations were spin-unrestricted, allowing for unpaired configurations, however the magnetization drops to zero in every case, indicating that the proximity of two vacancies leads to spin compensated electronic structures. This remains true in the case of the hybrid density functional PBE0, where also spin compensated divacancy structures are found.

## Results and Discussions

### Geometry and energy optimization

In our previous work $^{22}$ pristine $\text{MgH}_2$ bulk was relaxed in order to find the equilibrium geometry and energy. From that structure H divacancies were generated and structurally optimized. Formation energies and vacancy-vacancy distances are summarized in Table 1, using the vacancy labels of Figure 1. We can see that when the distance between vacancies is small, they are more stable, i.e. they require less energy to be formed. As a comparison, in our paper regarding single vacancies $^{22}$, a formation energy of 1.35 eV for each vacancy was obtained, therefore we can deduce that some divacancies (like V2V3, V1V2, etc.) are easier to generate than two isolated single vacancies (1.35 eV + 1.35 eV = 2.70 eV). The

minimum energy value calculated of 2.11 eV highly agrees with previous calculations in the literature $^{24-25}$.

Table 1. Divacancy sets generated in MgH₂ bulk, formation energies and vacancy-vacancy distances.

<table>
  <thead>
    <tr>
      <th>Divacancy</th>
      <th>FEVH₂ (eV)</th>
      <th>V-V distance (Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>V2V3</td>
      <td>2.11</td>
      <td>2.492</td>
    </tr>
    <tr>
      <td>V5V6</td>
      <td>2.11</td>
      <td>2.492</td>
    </tr>
    <tr>
      <td>V8V9</td>
      <td>2.11</td>
      <td>2.492</td>
    </tr>
    <tr>
      <td>V11V12</td>
      <td>2.11</td>
      <td>2.492</td>
    </tr>
    <tr>
      <td>V7V1</td>
      <td>2.11</td>
      <td>2.493</td>
    </tr>
    <tr>
      <td>V1V5</td>
      <td>2.33</td>
      <td>2.750</td>
    </tr>
    <tr>
      <td>V1V6</td>
      <td>2.33</td>
      <td>2.750</td>
    </tr>
    <tr>
      <td>V1V2</td>
      <td>2.33</td>
      <td>2.751</td>
    </tr>
    <tr>
      <td>V1V3</td>
      <td>2.33</td>
      <td>2.751</td>
    </tr>
    <tr>
      <td>V3V6</td>
      <td>2.65</td>
      <td>3.900</td>
    </tr>
    <tr>
      <td>V2V6</td>
      <td>2.72</td>
      <td>3.010</td>
    </tr>
    <tr>
      <td>V1V10</td>
      <td>2.75</td>
      <td>3.256</td>
    </tr>
    <tr>
      <td>V7V2</td>
      <td>2.76</td>
      <td>4.841</td>
    </tr>
    <tr>
      <td>V1V4</td>
      <td>2.93</td>
      <td>3.872</td>
    </tr>
    <tr>
      <td>V3V11</td>
      <td>3.10</td>
      <td>6.507</td>
    </tr>
    <tr>
      <td>V2V9</td>
      <td>3.10</td>
      <td>6.507</td>
    </tr>
  </tbody>
</table>

Diffusion of a hydrogen divacancy

Regarding hydrogen divacancy diffusion, to the best of our knowledge, there are no studies reported up to now. Given that most divacancies are easier to be formed than two single vacancies, it is interesting to consider their diffusion as pairs. As mentioned above, we have taken into account diffusion along all three spatial directions (along the x, y and z axes). We have analyzed two cases: the direct diffusion and the diffusion through an intermediate

state. In each case we have considered simultaneous and sequential moves, the first involves the movement of two vacancies at the same time while the second involves the movement of one vacancy after the other.

Along the x-axis

The initial state is $MgH_2$ containing a V2V3 divacancy and the final state is $MgH_2$ containing a V11V12 divacancy. As mentioned in the previous section, we have studied the direct diffusion mechanism considering simultaneous and sequential paths. The length that vacancies have to diffuse is one lattice parameter (4.501 Å). The simultaneous case has a lower barrier than the sequential one, 1.07 and 2.23 eV respectively. We have also studied this diffusion through the V7V1 intermediate, which is not oriented along the x-axis. Here, the simultaneous diffusion, i.e. the movement of two vacancies at the same time is not feasible energetically, but a sequential diffusion mechanism is possible, where a first step goes from V3 to V1 and a second step from V2 to V7 to reach the intermediate geometry. The activation energy is 1.01 eV. The path lengths and energy barriers are summarized in Table 2. In Figure 2, the obtained minimal energy path curves are plotted. In the most favored case the rate determining step has an activation energy of 1.01 eV. Compared with the case of the diffusion of a single vacancy in $MgH_2$, 1.10 eV $^{22}$, divacancies not only are easier to form energetically, but they also require slightly less energy to diffuse along the x-axis.

![](./images/811102786144960512_4.jpg)

Figure 2. $VH_2$ diffusion curves and zoomed $MgH_2$ cell indicating vacancy movements. (a) correspond to simultaneous direct, (b) to sequential direct diffusion and (c) to sequential by intermediate diffusion, along the $x$-axis.

Table 2. Details of each movement, path lengths and energetic barriers for simultaneous and sequential direct and sequential by intermediate diffusion along the $x$-axis.

<table>
<thead>
<tr>
<th colspan="2"></th>
<th rowspan="2">Path length</th>
<th colspan="2">Activation energy (eV)</th>
</tr>
<tr>
<th colspan="2">Simultaneous direct</th>
<th>A -&gt; B</th>
<th>B -&gt; A</th>
</tr>
</thead>
<tbody>
<tr>
<td>Step 1</td>
<td>V2V3-V11V12</td>
<td>4.50 Å</td>
<td>1.07</td>
<td>1.07</td>
</tr>
<tr>
<th colspan="2">Sequential direct</th>
<th>Path length</th>
<th>A -&gt; B</th>
<th>B -&gt; A</th>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V11V3</td>
<td>4.50 Å</td>
<td>2.23</td>
<td>1.24</td>
</tr>
<tr>
<td>Step 2</td>
<td>V11V3-V11V12</td>
<td>4.50 Å</td>
<td>1.24</td>
<td>2.23</td>
</tr>
<tr>
<th colspan="2">Sequential intermediate</th>
<th>Path length</th>
<th>A -&gt; B</th>
<th>B -&gt; A</th>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V2V1</td>
<td>2.75 Å</td>
<td>1.01</td>
<td>0.79</td>
</tr>
<tr>
<td>Step 2</td>
<td>V2V1-V7V1</td>
<td>4.80 Å</td>
<td>0.58</td>
<td>0.80</td>
</tr>
<tr>
<td>Step 3</td>
<td>V7V1-V11V1</td>
<td>4.80 Å</td>
<td>0.80</td>
<td>0.58</td>
</tr>
<tr>
<td>Step 4</td>
<td>V11V1-V11V12</td>
<td>2.75 Å</td>
<td>0.79</td>
<td>1.01</td>
</tr>
</tbody>
</table>

### Along the y-axis

Here we consider as initial state $MgH_2$ containing a V2V3 divacancy, like in the case of diffusion along the $x$-axis, but now the final state is $MgH_2$ containing a V8V9 divacancy.
We take into account different possible diffusion paths, namely a direct one and one other path passing through a V1V10 divacancy intermediate. The direct simultaneous movement from V2V3 to V8V9 is not probable energetically, but a sequential diffusion is possible. It consists in a first step from V3 to V9 and a second step from V2 to V8. These two diffusions are symmetric as it can be seen in Figure 3 (a). However this mechanism has a high activation energy (2.25 eV). In the case in which we consider the intermediate (V1V10) state, the simultaneous diffusion, from V2V3 to V1V10 and then to V8V9 (see Figure 3 (b)) and the sequential diffusion i.e. a first step V2 to V1 and a second step from V3 to V10 to reach the intermediate, both require an activation energy of only 1.01 eV. In Table 3 more information about these diffusions is resumed. In this direction, according to our previous study $^{22}$, the energy barrier for the movement through an intermediate state for an isolated single vacancy is 0.79 eV, but the direct diffusion along the $y$-axis for a single vacancy is larger than 1.06 eV. Therefore, unlike in the case of the $x$-axis, divacancy diffusion along the $y$-axis is not favored if we compare the intermediate path, however if we compare the direct path, divacancy diffusion is favored over single vacancy diffusion.

![](./images/811102786144960512_5.jpg)

Figure 3. $VH_2$ diffusion curves and zoomed $MgH_2$ cell indicating vacancy movements, (a) correspond to sequential direct diffusion (b) to simultaneous by intermediate and (c) to sequential by intermediate diffusion along the y-axis.

Table 3. Details of each step, path lengths and energetic barriers for sequential direct, simultaneous and sequential by intermediate diffusion along the y-axis.

<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th></th>
      <th colspan="2">Activation energy (eV)</th>
    </tr>
    <tr>
      <th colspan="2">Sequential direct</th>
      <th>Path length</th>
      <th>A -> B</th>
      <th>B -> A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Step 1</td>
      <td>V2V3-V2V9</td>
      <td>4.50 Å</td>
      <td>2.24</td>
      <td>1.39</td>
    </tr>
    <tr>
      <td>Step 2</td>
      <td>V2V9-V8V9</td>
      <td>4.50 Å</td>
      <td>1.40</td>
      <td>2.25</td>
    </tr>
    <tr>
      <th colspan="2">Simultaneous intermediate</th>
      <th>Path length</th>
      <th>A -> B</th>
      <th>B -> A</th>
    </tr>
    <tr>
      <td>Step 1</td>
      <td>V2V3-V1V10</td>
      <td>2.75 Å</td>
      <td>1.01</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>Step 2</td>
      <td>V1V10-V8V9</td>
      <td>2.75 Å</td>
      <td>0.38</td>
      <td>1.02</td>
    </tr>
    <tr>
      <th colspan="2">Sequential intermediate</th>
      <th>Path length</th>
      <th>A -> B</th>
      <th>B -> A</th>
    </tr>
    <tr>
      <td>Step 1</td>
      <td>V2V3-V1V3</td>
      <td>2.75 Å</td>
      <td>1.01</td>
      <td>0.79</td>
    </tr>
    <tr>
      <td>Step 2</td>
      <td>V1V3-V1V10</td>
      <td>2.75 Å</td>
      <td>0.93</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>Step 3</td>
      <td>V1V10-V8V10</td>
      <td>2.75 Å</td>
      <td>0.50</td>
      <td>0.93</td>
    </tr>
    <tr>
      <td>Step 4</td>
      <td>V1V10-V8V9</td>
      <td>2.75 Å</td>
      <td>0.79</td>
      <td>1.01</td>
    </tr>
  </tbody>
</table>

### Along the z-axis

Like in the two previous cases, we start from MgH₂ containing a V2V3 divacancy, but here the final state is MgH₂ containing a V5V6 divacancy. The direct simultaneous diffusion has a high activation energy (2.04 eV). This activation energy decreases significantly when a sequential diffusion is considered, a barrier of 0.93 eV is found. If we study an alternative simultaneous path, through the intermediate V1V4, which involves only short distance moves, it is less probable to occur because of a high barrier of 2.26 eV. Similarly, the sequential diffusion through an intermediate state is not feasible due to the step from V1V3 to V1V4 which is energetically not possible, despite the short distance between the vacancies in this intermediate (V1V4) state. Details for these diffusions can be found in Figure 4 and Table 4. Like in the case of diffusion along the x-axis, divacancy diffusion along the z-axis is favored in comparison with movements for an isolated single vacancy (1.05 eV) ²².

![](./images/811102786144960512_6.jpg)

Figure 4. VH₂ diffusion curves and zoomed MgH₂ cell indicating vacancy movements. (a) corresponds to simultaneous direct, (b) to sequential direct diffusion and (c) to simultaneous by intermediate, along the z-axis.

Table 4. Details of each step, path lengths and energetic barriers for simultaneous direct, sequential direct diffusion and simultaneous by intermediate diffusion along the z-axis.

<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th></th>
      <th colspan="2">Activation energy (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="2">Simultaneous direct</th>
      <th>Path length</th>
      <td>A -&gt; B</td>
      <td>B -&gt; A</td>
    </tr>
    <tr>
      <td>Step 1</td>
      <td>V2V3-V5V6</td>
      <td>3.01 Å</td>
      <td>2.04</td>
      <td>2.04</td>
    </tr>
    <tr>
      <th colspan="2">Sequential direct</th>
      <th>Path length</th>
      <td>A -&gt; B</td>
      <td>B -&gt; A</td>
    </tr>
    <tr>
      <td>Step 1</td>
      <td>V2V3-V5V3</td>
      <td>3.01 Å</td>
      <td>0.93</td>
      <td>0.38</td>
    </tr>
    <tr>
      <td>Step 2</td>
      <td>V5V3-V5V6</td>
      <td>3.01 Å</td>
      <td>0.38</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th colspan="2">Simultaneous intermediate</th>
      <th>Path length</th>
      <td>A -&gt; B</td>
      <td>B -&gt; A</td>
    </tr>
    <tr>
      <td>Step 1</td>
      <td>V2V3-V1V4</td>
      <td>2.75 Å</td>
      <td>2.26</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>Step 2</td>
      <td>V1V4-V5V6</td>
      <td>2.75 Å</td>
      <td>1.44</td>
      <td>2.26</td>
    </tr>
  </tbody>
</table>

Comparison of energetic barriers using hybrid functional PBE0

Using PBE0, we have re-calculated the energies along all diffusion paths previously determined at the PW91 level. PW91 and PBE0 lead to the same preferential diffusion mechanisms in all three spatial directions, as we can see in Table 5.

Table 5. Energetic barriers for hydrogen divacancy diffusion using the hybrid PBE0 functional, for the x-, y- and z-axis, respectively

<table>
<thead>
<tr>
<th colspan="2">X-axis</th>
<th></th>
<th colspan="2">Activation energy (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">Simultaneous direct</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V11V12</td>
<td>4.50 Å</td>
<td>1.48</td>
<td>1.53</td>
</tr>
<tr>
<td colspan="2">Sequential direct</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V11V3</td>
<td>4.50 Å</td>
<td>1.61</td>
<td>1.17</td>
</tr>
<tr>
<td>Step 2</td>
<td>V11V3-V11V12</td>
<td>4.50 Å</td>
<td>1.17</td>
<td>1.61</td>
</tr>
<tr>
<td colspan="2">Sequential intermediate</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V2V1</td>
<td>2.75 Å</td>
<td>0.75</td>
<td>0.71</td>
</tr>
<tr>
<td>Step 2</td>
<td>V2V1-V7V1</td>
<td>4.80 Å</td>
<td>1.17</td>
<td>1.22</td>
</tr>
<tr>
<th colspan="2">Y-axis</th>
<th></th>
<th colspan="2">Activation energy (eV)</th>
</tr>
<tr>
<td colspan="2">Sequential direct</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V2V9</td>
<td>4.50 Å</td>
<td>1.64</td>
<td>1.12</td>
</tr>
<tr>
<td>Step 2</td>
<td>V2V9-V8V9</td>
<td>4.50 Å</td>
<td>0.99</td>
<td>1.73</td>
</tr>
<tr>
<td colspan="2">Simultaneous intermediate</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V1V10</td>
<td>2.75 Å</td>
<td>0.66</td>
<td>0.18</td>
</tr>
<tr>
<td>Step 2</td>
<td>V1V10-V8V9</td>
<td>2.75 Å</td>
<td>0.67</td>
<td>1.16</td>
</tr>
<tr>
<td colspan="2">Sequential intermediate</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V1V3</td>
<td>2.75 Å</td>
<td>0.74</td>
<td>0.71</td>
</tr>
<tr>
<td>Step 2</td>
<td>V1V3-V1V10</td>
<td>2.75 Å</td>
<td>0.65</td>
<td>0.28</td>
</tr>
<tr>
<th colspan="2">Z-axis</th>
<th></th>
<th colspan="2">Activation energy (eV)</th>
</tr>
<tr>
<td colspan="2">Simultaneous direct</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V5V6</td>
<td>3.01 Å</td>
<td>2.19</td>
<td>2.19</td>
</tr>
<tr>
<td colspan="2">Sequential direct</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V5V3</td>
<td>3.01 Å</td>
<td>0.76</td>
<td>0.54</td>
</tr>
<tr>
<td>Step 2</td>
<td>V5V3-V5V6</td>
<td>3.01 Å</td>
<td>0.94</td>
<td>1.16</td>
</tr>
<tr>
<td colspan="2">Simultaneous intermediate</td>
<td>Path length</td>
<td>A -&gt; B</td>
<td>B -&gt; A</td>
</tr>
<tr>
<td>Step 1</td>
<td>V2V3-V1V4</td>
<td>2.75 Å</td>
<td>2.59</td>
<td>1.43</td>
</tr>
<tr>
<td>Step 2</td>
<td>V1V4-V5V6</td>
<td>2.75 Å</td>
<td>1.43</td>
<td>2.59</td>
</tr>
</tbody>
</table>

We have not found a general tendency of always under- or overestimating of the relative energies when comparing the semilocal with the hybrid functional. The differences between the two functionals can be sizeable, but the general shape and order of magnitude of the

barriers remains the same. In Figure 5 we present a comparison of the curves obtained using hybrid vs. semilocal functional for the preferential mechanisms.

![](./images/811102786144960512_7.jpg)

**Figure 5.** Comparison of $VH_2$ diffusion curves using the semilocal PW91 and the hybrid PBE0 functionals. The most probable diffusion paths for the three Cartesian directions are shown. (a) first two steps of sequential intermediate diffusion along the x-axis, (b) simultaneous intermediate diffusion along the y-axis and (c) sequential direct diffusion along the z-axis.

### Conclusions

We performed ab-initio DFT-based calculations to study the formation energy and diffusion of hydrogen divacancies in bulk magnesium hydride. Based in the obtained results we can conclude that the formation of a pair of H vacancies is more favorable energetically than the formation of two isolated single vacancies. This fact can be attributed to the spin-pairing of defect electrons, a result which is supported by the absence of any spin polarization in the systems containing divacancies. As a function of the distance between the two vacancies, the formation energy varies, as shorter distances between the two H vacancies are favored. Regarding the diffusion of the divacancies, the minimum energy barriers along the three Cartesian directions are 1.01, 1.01 and 0.93 eV for the *x*-, *y*- and *z*-axis, respectively, formally leading to a non-isotropic diffusion probability. However, at typical operational temperatures of 300-350°C such small differences are unlikely to have any discernable influence. These barrier heights are of similar magnitude as single vacancy diffusion barriers in the same material. Starting from these results, work is currently in progress to study the influence of dopants on divacancy diffusion and to model nanostructured MgH₂ systems, characterized by the presence of surfaces, interfaces and thin films. The diffusion mechanisms of single or divacancies in MgH₂ is mainly relevant when the stoichiometry is close to the ideal ratio H/Mg=2, i.e. in situations with a low concentration of H vacancies. In future work, we plan to investigate the much more challenging situation where the pure Mg and MgH₂ phases are destabilized due to a massive uptake or release of hydrogen. In such situations, interfaces and lamellar Mg-MgH₂ structures ³⁹ will determine the reaction kinetics. This kind of process will require computational methodologies, which lie beyond the scope of the present paper.

### Acknowledgments

E.G. is a member of CONICET. The authors acknowledge SGCyT (UNS), IFISUR-CONICET, CIC-Buenos Aires, PICT 1770, and PICT-2012-1609 for financial support.

E.G. would like to thank the ICTP and the Simons Foundation for providing the opportunity to undertake this research by supporting her visit to the ICTP as an ICTP–Simons Associate.

### References

1 J.H. Dai, Y. Song, R. Yang, *Int. J. Hydrogen Energy* 2011, **36**, 12939.

2 J.H. Dai, Y. Song, R. Yang, *J. Phys. Chem. C* 2010, **114**, 11328.

3 L. Schlapbach, A. Züttel, *Nature* 2001, **414**, 353.

4 R. Bardhan, A.M. Rumininski, A. Brand, J.J. Urban, *Energy Environ. Sci.* 2011, **4**, 4882.

5 S.A. Shevlin, Z.X. Guo, *Chem. Soc. Rev.* 2009, **38**, 211.

6 Y. Lei, S.A. Shevlin, W. Zhu, Z.X. Guo, *Phys. Rev. B* 2008, **77**, 134114.

7 K.F. Aguey-Zinsou, J.R. Ares-Fernández, *Energy Environ. Sci.* 2010, **3**, 526.

8 S.A. Shevlin, C. Cazorla, Z.X. Guo, *J. Phys. Chem. C* 2012, **116**, 13488.

9 J. Yang, A. Sudik, C. Wolverton, D.J. Siegel, *Chem. Soc. Rev.* 2010, **39**, 656.

10 T. Hussain, T.A. Maark, B. Pathak, R. Ahuja, *AIP Adv.* 2013, **3**, 102117.

11 L.L. Wang, D.D. Johnson, *J. Phys. Chem. C* 2012, **116**, 7874.

12 T. Hussain, A. De Sarkar, T.A. Maark, W. Sun, R. Ahuja, *EPL* 2013, **101**, 27006.

13 N. Novaković, J. Grbović Novaković, L. Matović, M. Manasijević, I. Radisavljević, B. PaskašMamula, N. Ivanović, *Int. J. Hydrogen Energy* 2010, **35**, 598.

14 X.Q. Zeng, L.F. Cheng, J.X. Zou, W.J. Ding, H.Y. Tian, C. Buckley, *J. Appl. Phys.* 2012, **111**, 093720.

15 D. Moser, D.J. Bull, T. Sato, D. Noré us, D. Kyoi, T. Sakai, N. Kitamura, H. Yusa, T. Taniguchi, W.P. Kalisvaart, P. Notten, *J. Mater. Chem.* 2009, **19**, 8150.

16 X.B. Xiao, W.B. Zhang, W.Y. Yu, N. Wang, B.Y. Tang, *Phys. B* 2009, **404**, 2234.

17 S.X. Tao, P.H.L. Notten, R.A. van Santen, A.P.J. Jansen, *Phys. Rev. B: Condens. Matter Mater. Phys.* 2010, **82**, 125448.

18 T. Liu, C. Wang, Y. Wu, *Int. J. Hydrogen Energy* 2014, **39**, 14262.

19 M.S. Park, A. Janotti, C.G. Van de Walle, *Phys. Rev. B: Condens. Matter Mater. Phys.* 2009, **80**, 064102.

20 S.X. Tao, W.P. Kalisvaart, M. Danaie, D. Mitlin, P.H.L. Notten, R.A. van Santen, A.P.J Jansen, *Int. J. Hydrogen Energy* 2011, **36**, 11802.

21 W. Stier, L.G. Camargo, F. Óskarsson, H. Jónsson, *Prepr. Pap.-Am. Chem. Soc., Div. Fuel Chem.* 2005, **50**, 15.

22 E. German, R. Gebauer, *J. Phys. Chem. C* 2016, **120**, 4806.

23 V. Koteski, J. Belošević-Čavor, K. Batalović, J. Radaković, A. Umićević, *RSC Adv.* 2015, **5**, 34894.

24 R. Grau-Crespo, K.C. Smith, T.S. Fisher, N.H. de Leeuw, U.V. Waghmare, *Phys. Rev. B* 2009, **80**, 174117.

25 A.J. Du, S.C. Smith, G.Q. Lu, *J. Phys. Chem. C* 2007, **111**, 8360.

26 P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, et al. *J. Phys.: Condens. Matter* 2009, **21**, 395502.

27 J.P. Perdew, Y. Wang, *Phys. Rev. B: Condens. Matter Mater. Phys.* 1992, **45**, 13244.

28 J.P. Perdew, *In Electronic Structure of Solids* Ziesche, P., Eschrig, H., Eds.; Akademie Verlag: Berlin, 1991.

29 C. Adamo, V. Barone, *J. Chem. Phys.* 1999, **110**, 6158.

30 D. Vanderbilt, *Phys. Rev. B: Condens. Matter Mater. Phys.* 1990, **41**, 7892.

31 http://www.quantum-espresso.org/pseudopotentials/

32 H.J. Monkhorst, J.D. Pack, *Phys. Rev. B* 1976, **13**, 5188.

33 H. Jónsson, G. Mills, K.W. Jacobsen, *In Nudged Elastic Band Method for Finding Minimum Energy Paths of Transitions*, in *Classical and Quantum Dynamics in Condensed Phase Simulations*; B.J. Berne, G. Ciccotti, D.F. Coker, Eds.; World Scientific: 1998.

34 D. Sheppard, R. Terrell, G. Henkelman, *J. Chem. Phys.* 2008, **128**, 134106.

35 G. Henkelman, G. Jóhannesson, H. Jónsson, *In Methods for Finding Saddle Points and Minimum Energy Paths*, in *Progress on Theoretical Chemistry and Physics*; Schwartz, S. D., Ed.; Kluwer Academic Publishers: 2000.

36 G. Henkelman, B.P. Uberuaga, H. Jónsson, *J. Chem. Phys.* 2000, **113**, 9901.

37 G. Henkelman, H. Jónsson, *J. Chem. Phys.* 2000, **113**, 9978.

38 C.R. Luna, E. German, C. Macchi, A. Juan, A. Somoza, *J. Alloys Compd.* 2013, **556**, 188.

39 B. Bokhonov, E. Ivanov, V. Boldyrev, *Mater. Lett.* 1987, **5**, 218.