# Mechanics of SWCNT Aggregates Studied by Incremental Constrained Minimization

Mengyu Lan¹ and Haim Waisman²

**Abstract:** The stress-strain behavior of short single-walled carbon nanotube (SWCNT) aggregates is investigated by a novel incremental constrained minimization approach. An AIREBO potential is used to model the interactions within and between CNTs. The idea is to homogenously disperse SWCNTs in the computational cell at random positions and orientations following spherical uniform distributions, and incrementally deform the cell although restraining the movement of atoms at the ends of nanotubes. The stress-strain response of the system is obtained in each loading direction, and it is shown to converge to an isotropic behavior (a similar response in all directions) as the number of CNTs in the system increases. It is also shown that the Young's modulus of the system increases linearly with the CNT aggregates density. Finally, the method is shown to agree well with results obtained from molecular dynamics simulations running at near zero degrees kelvin, however they are obtained at only a fraction of the CPU time. DOI: 10.1061/(ASCE)NM.2153-5477.0000043. © 2012 American Society of Civil Engineers.

CE Database subject headings: Aggregates; Nanotechnology; Stress strain relations; Constraints.

Author keywords: Molecular mechanics; Nanotubes aggregates; Minimization; SWCNT.

## Introduction

Carbon nanotubes (CNTs) were first discovered in 1991 (Iijima 1991) and have since been the subject of intensive research because of a wide range of potential applications (Dai 2002; Modi et al. 2003; Coleman et al. 2006; Chen et al. 2006; Harrison and Atala 2007; Javeyet al. 2003; Chen and Huang 2008). CNTs are allotropes of carbon with a nanostructure that can have a length-to-diameter ratio greater than 1,000,000 and, in terms of tensile strength and elastic modulus, are among the strongest and stiffest materials ever synthesized. A single-walled carbon nanotube (SWCNT) can be regarded as a roll of graphene sheet; whereas, a multiwalled carbon nanotube (MWCNT) is an assembly of coaxial SWCNTs where the neighboring layers are separated by a Van der Waals equilibrium distance of 0.34 nm (Saito et al. 1993; Ruoff et al. 2003). The high values of CNTs Young modulus and tensile strength have attracted the attention of many researchers since their discovery.

One interesting application of nanotubes is their use as reinforcing components in nanocomposites, e.g., in epoxy adhesives or polymers, which could be employed for infrastructure or military protection. However, to obtain nearly optimal performance from a continuum point of view, it is well know that CNTs must be homogenously dispersed in the polymer (Gojny et al. 2004; He et al. 2007). This distribution would lead to a macroscopically isotropic response of nanocomposites, i.e., the mechanical behavior will be similar in every loading direction.

In this work, a novel molecular mechanics approach is proposed to study the mechanics of CNT aggregates. Despite the large bulk of work studying the mechanical properties of a SWCNT, MWCNT, and nanotube composites, little attention has been given to CNT aggregates composed of randomly agglomerated SWCNT or MWCNT bundles (Ruoff et al. 2003).

This deficit can partially be attributed to the intensive computational requirements for modeling such structures with molecular dynamics (MD) methods. Hence, in most molecular modeling methods of CNTs, only a small number is modeled assuming periodic boundary conditions; nonetheless, important conclusions can still be made. For example, a study performed by Yakobson et al. (1996) on compression of a single CNT reported a Young's modulus of 5.5 TPa. Buehler et al. (2004) have investigated a very long SWCNT under compressive loading and found three different deformation mechanisms with increasing aspect ratios. By using MD, Frankland et al. (2003) investigated the stress-strain behavior of polymers enhanced by unidirectional nanotubes and found that a long continuous nanotube composite is enhanced only in the direction of the nanotube. Qi et al. (2005) modeled polymer with nanotubes by using a Nose-Hoover MD method, which adjusts the system volume on the basis of temperature and pressure. The stress-strain curves, along with Young's modulus and Poisson's ratio were obtained at different temperatures, and it was shown that the Young's modulus of the system will decrease as the temperature increases.

To overcome the computational limitations of molecular dynamics, a novel molecular mechanics approach is proposed to investigate the stress-strain response of randomly dispersed short SWCNTs. In other words, the mechanics of SWCNT aggregates consisting of many nanotubes randomly dispersed in the simulation cell is studied. The idea is to perform strain loading by incrementally stretching the simulation cell and conformingly mapping atoms to their new position. Then, at every increment a constrained minimization is performed where the CNT ends are restrained

¹Graduate Student, Dept. of Civil Engineering and Applied Mechanics, Columbia Univ., 610 SW Mudd, Mail Code: 4709, New York, NY 10027.
²Assistant Professor, Dept. of Civil Engineering and Applied Mechanics, Columbia Univ., 610 SW Mudd, Mail Code: 4709, New York, NY 10027 (corresponding author). E-mail: waisman@civil.columbia.edu
Note. This manuscript was submitted on April 5, 2011; approved on September 21, 2011; published online on September 23, 2011. Discussion period open until November 1, 2012; separate discussions must be submitted for individual papers. This paper is part of the *Journal of Nanomechanics and Micromechanics*, Vol. 2, No. 2, June 1, 2012. ©ASCE, ISSN 2153-5434/2012/2-15-22/$25.00.

JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012 / 15
J. Nanomech. Micromech. 2012.2:15-22.

from moving. Atomic interactions within and between CNTs are modeled by an AIREBO potential, and the CNTs dispersion is determined by an algorithm that produces spherical uniform distribution of CNTs. In the simulations in this paper, a (5,5) armchair SWCNT with a length of 2 nm is employed to construct the SWCNT aggregates. The method is implemented within LAMMPS, a molecular dynamics software developed at Sandia National Labs (Plimpton 1995). By using this method the mechan- ics of nanotube aggregates are studied and it is demonstrated that the isotropic response is indeed obtained as the number of randomly dispersed CNTs increases (an intuitive result that would require intensive computational resources with molecular dynam- ics). Moreover, it is shown that Young's modulus increases as the density of nanotubes in the unit cell increases.

The paper is organized in the following way: The atomistic potential(AIREBO) that accounts for both short and long atom interactions is introduced first. Then, a detailed algorithm for generating randomly dispersed CNTs in a computational cell is de- scribed. Next, the proposed incremental constrained minimization method is given. The stress-strain response curves and the corre- sponding discussion are presented in the end.

## Computational Model

### Bonding Potentials

Two bond types, known as $\sigma$- and $\pi$- bonds, describe the interaction between atoms of carbon nanotubes. $\sigma$-bond is because of the pro- cess of $\text{sp}^2$ hybridization (Brown et al. 1999). This is a covalent bond which provides most of CNT's fabulous strength and has been studied experimentally and theoretically in (Treacy et al. 1996; Krishnan et al. 1998; Yu et al. 2000). $\pi$-bond exists between layers of multiwalled CNTs and between different single-walled CNTs in aggregates (Ruoff et al. 2003). Its effectiveness is relatively weak but not negligible. Hence, to reproduce these experimental results, many empirical potentials were developed. However, these potentials primarily capture $\sigma$-bonds and neglect the effects of $\pi$-bonds. One such potential is the so-called Tersoff-Brenner poten- tial (Brenner 1990). This is a multibody potential that is suitable for modeling covalent bonds between carbon, silicon, hydrogen, ger- manium, and their compound. Unfortunately, despite the fact that numerous studies have been devoted to investigating the mechani- cal properties of SWCNT, in most of these studies only the $\sigma$-bond was considered, although some research considering both bonds can also be found in the literature (Liew et al. 2006).

In this paper, Brenner's second generation Reactive Empirical Bond-Order (REBO) potential (Brenner et al. 2002) is employed to describe interactions within carbon nanotubes. Its accuracy was verified by computing the fracture stress and strain of a single (12,12) SWCNT (Liew et al. 2004) and comparing it to other pub- lished studies (Belytschko et al. 2002). To incorporate Van der Waals interactions between SWCNTs, a complete bond expressionmust consist of at least two terms as (Stuart et al. 2000)

$$
E=\frac{1}{2} \sum_{i} \sum_{j \neq i}\left[E_{i j}^{\mathrm{REBO}}+E_{i j}^{\mathrm{LJ}}\right]
\tag{1}
$$

where the index $i$ runs through all the atoms in the system, and where

$$
E_{i j}^{\mathrm{LJ}}=S\left(t_{r}\left(r_{i j}\right)\right) S\left(t_{b}\left(b_{i j}^{*}\right)\right) C_{i j} V_{i j}^{\mathrm{LJ}}\left(r_{i j}\right)+\left[1-S\left(t_{r}\left(r_{i j}\right)\right)\right] C_{i j} V_{i j}^{\mathrm{LJ}}\left(r_{i j}\right)
\tag{2}
$$

contributes to the Lennard-Jones (LJ) potential energy. Here, $r_{i j}=$ distance between atom $i$ and $j$; $t_{r}(r_{i j})=$ scaling function used to rescale the domain of the switching function $S(t)$; $V_{i j}=$ standard12-6 LJ interactions; and $C_{i j}=$ connectivity switch to disable LJ interactions within REBO range. In general, a LJ potential is valid where REBO potential is ineffective, i.e., when $r>0.2$ nm, which is controlled by switching on the function $S(t)$ so that the short- ranged LJ repulsive term $1 / r^{12}$ does not interfere with energy described by $E^{\mathrm{REBO}}$.

## Generation of Randomly Dispersed CNTS in the Cell

Current atomistic modeling research is primarily focused on indi- vidual SWCNT (Jin and Yuan 2003), MWCNT (Pantano et al.2004), or polymer-nanotube composites (Frankland et al. 2003). Although these theoretical models show impressive mechanical behavior, in practice, CNTs are not individually synthesized but, rather, randomly agglomerated bundles (Thess et al. 1996). More- over, as pointed out (Ruoff et al. 2003), the high stiffness and strength obtained from an individual SWCNT is not necessarily present in CNT structures.

One precondition when simulating CNT structures, valid for most simulations, is to construct a representative cell that can present both a homogeneous distribution and isotropic behavior in all loading directions. The cell must exhibit isotropic prop- erties so that the simulation results are not affected by the initial configuration.

To generate a representative cell for CNT aggregates, it is nec- essary to rotate and displace every SWCNT on the basis of an un- biased distribution, as illustrated in Fig. 1. One natural assumption is that the direction of a SWCNT in space follows a spherical uni- form distribution. One approach to generate this distribution is by employing the trig method (Shoemake 1992). The trig method, which is very efficient in three dimensions, finds an unbiased angle $\theta$ in space starting from a given base direction, e.g., the $y$-axis. Then, a rotation matrix $\mathbf{R}$ is established as

$$
\mathbf{R}=\mathbf{I}+\sin \theta \mathbf{M}+(1-\cos \theta) \mathbf{M}^{2}
\tag{3}
$$

to translate every atom in a standard carbon nanotube to a new position that corresponds to a spherical uniform distribution. Matrix $\mathbf{M}$ is constructed by using angles obtained from the trig method and $\mathbf{I}$ is the identity matrix. Once formed, the SWCNT is displaced at a distance on the basis of a 3-dimensional uniform distribution, defined in a range of a cell. With each new added SWCNT, the distance between its axis and all other already dis- placed CNTs' axis must be computed to ensure that it is greater than $2r + 0.2$ nm where $r$ is the radius of CNT and 0.2 is the distance within which covalent bonds will form. By doing so, unwanted covalent bonds can be avoided in CNT structures. If this requirement has not been met, a new location is generated for further verification. We emphasize that individual SWCNT are not relaxed before they are introduced into the cell. In other words, first all CNTs are placed in the aggregates, and then a global energy minimization is performed as discussed in "Simulation Scheme," where each CNT finds its optimal position.

Employing the algorithm previously described leads to a typical initial configuration with randomly dispersed CNTs in a box, as illustrated in Fig. 2 for 10 and 200 CNTs. Although in this paper a (5,5) armchair SWCNT with a 2-nm length is employed to con- struct the SWCNT aggregates, this method is not restricted to any particular SWCNT type.

## Simulation Scheme

Molecular statics and molecular dynamics are two widely used methods in atomistic simulations and modeling. Generally speaking, molecular dynamics (MD) employs Newton's law and
---
16 / JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012

J. Nanomech. Micromech. 2012.2:15-22.

![](./images/813377111363420160_1.jpg)
![](./images/813377111363420160_2.jpg)

Fig. 1. Transformation of a SWCNT: (a) orientation of a SWCNT in axial direction; (b) rotation and translation of a SWCNT in an arbitrary direction

![](./images/813377111363420160_3.jpg)
![](./images/813377111363420160_4.jpg)

Fig. 2. Randomly dispersed CNTs in a box: (a) a representative computational cell with 10 (5,5) SWCNTs; (b) a representative computational cell with 200 (5,5) SWCNTs

integrates the equations in time to solve for atom movements in space. This method usually contains two phases: equilibration and production, therefore committing significant computing re- sources. Moreover, the time steps used to integrate these equations are often on the order of femto-seconds $(10^{-15} ~s)$. Furthermore, to observe meaningful results in MD, one typically needs to employ thousands of steps. Hence, for some problems MD may become prohibitively expensive.

Molecular statics on the other hand, investigates ensemble prop- erties by energy minimization. Physical properties are immediately obtained once equilibrium is achieved. Nonetheless, one significant drawback is that molecular statics does not consider temperature effects; hence, any properties obtained from the simulation corre- sponds to a $0 ~K$ temperature.

In this study, molecular statics is employed to study the mechan- ics of CNT aggregates. The method developed in the paper illus- trates that an isotropic response of the cell can only be obtained when considering many randomly dispersed CNTs.

To obtain the stress-strain response, we propose an incremental loading approach with a constrained minimization problem solved at every step. Assuming that the iteration begins with a random distribution of $N$ nanotube aggregates, the following algorithmis proposed:
1. Solve an unconstrained energy minimization problem to let atoms locate their optimum positions.

2. Expand the cell in one direction at a time ( $x, y$ , or $z$ which is chosen randomly) while keeping the other two directions free. The incremental expansion size is a parameter defined by the user.
3. Rescale conformingly the coordinates of CNT atoms with the new cell dimensions. This step essentially stretches the nano- tube with the computational cell.
4. Solve a constrained energy minimization problem by fixing the ends of every CNT in the cell. Upon convergence obtain the stress in the system, e.g., by using a virial stress measurement.
5. Repeat steps (2)-(4) until a specified strain is achieved and obtain the stress increment corresponding to the strain increment.
6. Repeat the incremental loading steps (2)-(5) in all three direc- tions and obtain the total stress-strain response of the system.

One incremental loading step with a single CNT is illustrated in Fig. 3. Dashed lines correspond to increment $i$ and solid lines to increment $i+1$ . The bold lines illustrate the two fixed ends of the nanotube, retaining the nanotube from retreating back to its original positions.

Remark 1: It is assumed that only nanotubes are present, and hence all nanotubes are stretched.

Remark 2: Note that the cell expands incrementally in one direction at a time. The other two directions are free to contract so that a zero stress is obtained because of the energy minimization

JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012 / 17

J. Nanomech. Micromech. 2012.2:15-22.

![](./images/813377111363420160_5.jpg)

Fig. 3. Incremental loading procedure

algorithm; however, it is observed that the total volume of the cell is not conserved.

Remark 3: The virial stress measure is employed to compute the stress from atomistic calculations. In MD simulations, the virial stress is obtained from kinetic and potential energy contributions. However, in molecular statics, the stress is obtained only from the potential energy, that is

$$
\sigma_{i j}^{\alpha}=-\frac{1}{V^{\alpha}} \sum_{\beta} F_{i}^{\alpha \beta} r_{j}^{\alpha \beta}
\tag{4}
$$

where $V^{\alpha}=$ atomic volume of some atom $\alpha$; $F_{i}^{\alpha \beta}=i$ ith-component of the force between atom $\alpha$ and atom $\beta$ computed from the derivative of the potential; $r_{j}^{\alpha \beta}=j$-component of the distance between atom $\alpha$ and $\beta$ (Nielsen and Martin 1985; Vitek and Egami 1987). The system stress is then calculated as the summation of atomic stresses

$$
\sigma_{i j}=-\frac{1}{V} \sum_{\alpha} \sum_{\beta} F_{i}^{\alpha \beta} r_{j}^{\alpha \beta}
\tag{5}
$$

Remark 4: Mathematically, the general incremental constrained minimization algorithm may be written as

$$
\begin{aligned}
\underset{\Delta r^{i}}{\operatorname{minimize}} & E\left(r_{1}^{i-1}+\Delta r_{1}^{i}, \ldots, r_{n}^{i-1}+\Delta r_{n}^{i}\right) \\
\text { subject to } & r_{j}^{i}=r_{j 0}^{i}(j \in \text { CNTs end })
\end{aligned}
\tag{6}
$$

where $r_{j}^{i}=$ displacement in $i$ th iteration of atom $j$; $r_{j 0}^{i}=$ prescribed displacement, obtained as the cell is stretched, for atom $j$ in $i$ th iteration. This procedure corresponds to a macroscopic uniaxial tension test. It is expected that by increasing the number of nanotubes in the cell, a macroscopically isotropic response could be obtained in every direction.

## Results and Discussion

The computations are performed by using LAMMPS LAMMPS (Plimpton 1995) on a SiCortex parallel machine employing 600 processors. An axial strain is applied in each direction at an increment of $0.01 \%$ until $5 \%$ strain is reached. The stress is computed once the constrained minimization has converged, and the Young's modulus is then extracted from the slope of the stress-strain curves. In our simulations, a (5,5) armchair SWCNT with length 2 nm is employed to construct the SWCNT aggregates, hence each CNT consists of 160 atoms.

![](./images/813377111363420160_6.jpg)

Fig. 4. Stress-strain curve for 25-(5,5) CNTs by using: (a) molecular statics; (b) molecular dynamics

<table>
<caption>Table 1. Comparison between MD Simulations and the Proposed Molecular Mechanics Method for Increasing Number of Nanotubes</caption>
<thead>
  <tr>
    <th colspan="2">Number of CNTs</th>
    <th>5</th>
    <th>10</th>
    <th>15</th>
    <th>20</th>
    <th>25</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Proposed method</td>
    <td>Time(h)</td>
    <td>0.9</td>
    <td>1.0</td>
    <td>1.0</td>
    <td>1.5</td>
    <td>2.0</td>
  </tr>
  <tr>
    <td>Iterations</td>
    <td>7761</td>
    <td>7188</td>
    <td>9492</td>
    <td>6879</td>
    <td>7206</td>
  </tr>
  <tr>
    <td rowspan="2">Molecular dynamics</td>
    <td>Time(h)</td>
    <td>67.6</td>
    <td>92.9</td>
    <td>75.0</td>
    <td>137.5</td>
    <td>205.0</td>
  </tr>
  <tr>
    <td>Time steps</td>
    <td>$6.0\times10^{6}$</td>
    <td>$6.0\times10^{6}$</td>
    <td>$6.0\times10^{6}$</td>
    <td>$6.0\times10^{6}$</td>
    <td>$6.0\times10^{6}$</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="7">Note: The problem was run on a Sicortex Parallel machine with 600 processors.</td>
  </tr>
</tfoot>
</table>

18 / JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012

J. Nanomech. Micromech. 2012.2:15-22.

### Comparison with Md Simulations
The stress-strain results obtained are first compared with the proposed method to molecular dynamics simulation with a microcanonical ensemble (NVE). In the MD method, strains are applied in the same manner as the proposed method, however, NVE is used to update atoms positions. The length of the cell is increased by 0.05% strain in each iteration until 5% strain is reached. In each iteration, the system is allowed to equilibrate for 2,000 time steps, and the stresses are obtained by averaging the results in the next 2,000 production time steps. The results, shown in Fig. 4, were obtained for 25 CNTs. It is interesting to note that although the MD simulation begins at a temperature that is nearly 0 K (before the strain is applied), when it reaches 5% strain the temperature increases to 0.8 K. Thus, because of the slow loading process and the linear stress-strain relations, most of the external work is transformed into a potential energy while the temperature slowly increases in the simulation.

For this particular case, the proposed molecular mechanics approach shows very good agreement with MD simulations. However, the corresponding computing time for MD was 18 h whereas only 1 h was needed for the molecular mechanics computation. To emphasize this point Table 1 shows the CPU time that it takes to run an MD simulation versus the CPU time that it takes the proposed molecular mechanics method to converge, for a varying number of nanotubes. The table also reports the time steps versus the optimization iterations required by each method. It can clearly be seen that the MD simulation quickly becomes expensive, and it is hence impossible to solve with many atoms in the system. On the other hand, although the optimization is limited to some particular applications, the proposed method could be used to solve these huge size optimization problems.

### Studies with Increasing Number of Randomly Dispersed CNTS at Constant Density
Fig. 5 illustrates the stress-strain response obtained for 50-, 200-, 800-, and 1,000-(5,5) armchair CNT aggregates with a constant density of 0.08 g/cm³ computed as

$$
\rho=\frac{1.993 \times 10^{-26} \cdot N}{V} \tag{7}
$$

where $N$ = number of atoms in the simulation cell; $1.993 \times 10^{-26}$ kg = atom mass of Carbon-12; and $V$ = simulation volume.

![](./images/813377111363420160_7.jpg)

Fig. 5. Stress-strain curves obtained from atomistic simulations of 50-, 200-, 800- and 1,000-(5,5) armchair CNT aggregates

---

JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012 / 19

J. Nanomech. Micromech. 2012.2:15-22.

<table>
<caption>Table 2. Order Parameters for 50-,200-,800-, and 1,000-CNT Aggregates</caption>
<thead>
<tr>
<th>Number of CNTs</th>
<th>50</th>
<th>200</th>
<th>800</th>
<th>1,000</th>
</tr>
</thead>
<tbody>
<tr>
<td>Order parameter</td>
<td>−0.0577</td>
<td>0.0197</td>
<td>0.0171</td>
<td>0.0078</td>
</tr>
</tbody>
</table>

To study CNTs dispersion, the so-called order parameter $S$ is employed (Wilson 1996). This parameter is typically used to indicate isotropy and randomness of crystals and is defined by

$$
S=\left\langle\frac{3 \cos ^{2} \theta-1}{2}\right\rangle \tag{8}
$$

where $\theta =$ angle between the CNTs axis and some local director; and the brackets = spatial average. For example, an isotropic sample is indicated by $S=0$ and a perfectly aligned sample by $S=1$. The order parameter for the CNTs distribution studied in this paper is shown in Table 2. The results show that $S$ is converging to 0 as the number of CNTs in the system increases, which demonstrate the randomness and isotropic characteristic of the configuration.

Remark 5: Eq. (8) indicates that as the number of atoms in the cell increase, the volume of the simulation box must also increase accordingly, to keep a constant density.

The results in Fig. 5 infer that the macroscopic response becomes more isotropic, or in other words the uncertainty of the response reduces, as the number of nanotubes in the cell increases.

The CNT structures produce linear stress-strain curves within 5% strain, and no apparent nonlinearity is observed. The Young's modulus, calculated as the average in $x$, $y$, and $z$ directions up to 5% strain, is approximately 8.6 GPa for CNT aggregates with 1,000 nanotubes. This number is significantly smaller than reported results for one SWCNT Young's modulus, which ranges from 0.44 – 5.5 TPa (Shokrieh and Rafiee 2010). One reason for such a huge difference is because of the definition of an atomic volume when computing the stress. In a typical one SWCNT tension simulation, the atomic volume is assumed as an artificial thin-walled cylinder with a 0.34-nm wall thickness (Saito et al. 1993; Ruoff et al. 2003). However, for CNTs structures, the atomic volume is defined as the entire volume, which includes the hollow volume inside the tube and between tubes. Because of the extremely small artificial volume for a SWCNT, the stress computed by using Eq. (5) is much lager and, hence, the extracted Young's modulus. In practice however, CNTs are not individually synthesized but, rather, randomly agglomerated bundles (Thess et al. 1996).

The coefficients of variance of the computed Young's modulus and the normal stresses $\sigma_{ii}$ at every direction, as a function of the number of CNTs are shown in Figs. 6 and 7, respectively. It can be observed that when the number of CNTs grows to 700 and above, which corresponds to 112,000 atoms, the results converge with a coefficient of variance that is less than 4%, and the Young's modulus mean is 8.6 GPa. Along these lines, that is estimated as the number of nanotubes in the system increases; whereas, keeping the density constant, the coefficients of variance will decay even more, and the results will become more accurate in terms of obtaining an isotropic response in all directions.

Remark 6: Although it is difficult to quantify the number of atoms required to obtain acceptable results given different density levels, several conclusions can still be made. Assuming that 800 CNTs (128,000 atoms) provide an acceptable result with respect to the coefficient of variance, with a simulation volume of $3.2 \times 10^{-23}\ \text{m}^3$ then (1) keeping the volume fixed and adding more atoms will give acceptable results, and (2) keeping the number of atoms fixed at 128,000 and reducing the simulation volumes will also give acceptable results. In general, once an acceptable result is obtained, another one can be obtained without trial and error by simply increasing atoms in the simulation or decreasing the simulation volume.

![](./images/813377111363420160_8.jpg)
Fig. 6. Coefficients of variance indicating the variation of the young modulus from its average, obtained with increasing number of CNTs at constant density

![](./images/813377111363420160_9.jpg)
Fig. 7. Young's modulus at each direction

### Studies with 800 Randomly Dispersed CNTS and Increasing Density

Another set of simulations is performed to investigate Young's modulus change with respect to density variance. The results are present in Table 3 and Fig. 8.

All simulations were performed by using 800-(5,5) randomly dispersed CNTs so the simulation volume decreased accordingly. As discussed previously, the simulation results should have good homogenous and isotropic properties because the same amount of 128,000 atoms in a smaller simulation volume is employed.

<table>
<caption>Table 3. Young's Modulus of Aggregates at Different Density</caption>
<thead>
<tr>
<th>Density ($\text{g/cm}^3$)</th>
<th>0.1</th>
<th>0.12</th>
<th>0.14</th>
<th>0.16</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus (GPa)</td>
<td>10.87</td>
<td>12.96</td>
<td>15.28</td>
<td>17.55</td>
</tr>
<tr>
<td>Coefficient of variance</td>
<td>3.8%</td>
<td>2.6%</td>
<td>2.9%</td>
<td>3.4%</td>
</tr>
</tbody>
</table>

![](./images/813377111363420160_10.jpg)

Fig. 8. Linear relation between Young's modulus and density

A linear relation between the density and Young's modulus for (5,5) CNT aggregates can clearly be observed in Fig. 8.

## Conclusion
A new molecular mechanics approach has been introduced to study the mechanics of single-walled CNT aggregates. Within the aggregates an algorithm is developed to randomly disperse CNTs following a uniform spherical distribution.

The molecular mechanics method presented in the paper is based on an incremental constrained minimization methodology. At each increment, the simulation cell is deformed (similar to a displacement control in continuous systems), and the energy is minimized while the atoms are mapped to their new positions. It is assumed that their relative position in the cell doesn't change, and that their ends are fixed (constrained to the simulation box).

This approach produced similar results as the MD method with NVE ensembles but the convergence of the proposed method is orders of magnitude faster. Moreover, it was shown that an isotropic behavior is obtained when the number of arbitrary distributed CNTs in the aggregates increases, which is an intuitive result but would require tremendous computational resources if studied by MD. Although this technique may be limited to specific applications, it may provide a bridge between atomistic and continuum models, as the isotropic stress-strain relation may be employed in continuum formulations.

## References
Belytschko, T., Xiao, S. P., Schatz, G. C., and Ruoff, R. S. (2002). "Atomistic simulations of nanotube fracture." *Phys. Rev. B*, 65(23), 235-430.

Brenner, D. W. (1990). "Empirical potential for hydrocarbons for use in simulating the chemical vapor deposition of diamond flims." *Phys. Rev. B*, 42(15), 9458-9471.

Brenner, D. W., Shenderova, O. A., Harrison, J. A., Stuart, S. J., Ni, B., and Sinnott, S. B. (2002). "A second- generation reactive empirical bond order (REBO) potential energy expression for hydrocarbons." *J. Phys. Condens. Matter*, 14(4), 783-802.

Brown, T. E., Bursten, B. E., and Lemay, H. E. H. (1999). *Chemistry: The central science*, Prentice-Hall, Saddle River, NJ.

Buehler, M. J., Kong, Y., and Gao, H. (2004). "Deformation mechanisms of very long single-wall carbon nanotubes subject to compressive loading." *J. Eng. Mater. Technol.*, 126(3), 245-249.

Chen, X., and Huang, Y. (2008). "Nanomechanics modeling and simulation of carbon nanotubes." *J. Eng. Mech.*, 134(3), 211-216.

Chen, Z., et al. (2006). "An integrated logic circuit assembled on a single carbon nanotube." *Science*, 311(5768), 1735.

Coleman, J. N., Khan, U., Blau, W. J., and Gun'ko, Y. K. (2006). "Small but strong: A review of the mechanical properties of carbon nanotube-polymer composites." *Carbon*, 44(9), 1624-1652.

Dai, H. (2002). "Carbon nanotubes: Opportunities and challenges." *Surf. Sci.*, 500(1-3), 218-241.

Frankland, S. J. V., Harik, V. M., Odegard, G. M., Brenner, D. W., and Gates, T. S. (2003). "The stress-strain behavior of polymer-nanotube composites from molecular dynamics simulation." *Compos. Sci. Technol.*, 63(11), 1655-1661.

Gojny, F. H., Wichmann, M. H. G., Kopke, U., Fiedler, B., and Schulte, K. (2004). "Carbon nanotube-reinforced epoxy-composites: Enhanced stiness and fracture toughness at low nanotube content." *Compos. Sci. Technol.*, 64(15), 2363-2371.

Harrison, B. S., and Atala, A. (2007). "Carbon nanotube applications for tissue engineering." *Biomat. Cell, Mol, Biol.*, 28(2), 344-353.

He, C., et al. (2007). "An approach to obtaining homoge-neously dispersed carbon nanotubes in al powders for preparing reinforced al-matrix composites." *Adv. Mater.*, 19(8), 1128-1132.

Iijima, S. (1991). "Helical microtubules of graphitic carbon." *Nature*, 354(6348), 56-58.

Javey, A., Guo, J., Wang, Q., Lundstrom, M., and Dai, H. (2003). "Ballistic carbon nanotube eld-ect transistors." *Nature*, 424(6949), 654-657.

Jin, Y., and Yuan, F. G. (2003). "Simulation of elastic properties of single-walled carbon nanotubes." *Compos. Sci. Technol.*, 63(11), 1507-1515.

Krishnan, A., Dujardin, E., Ebbesen, T. W., Yianilos, P. N., and Treacy, M. M. J. (1998). "Young's modulus of single-walled nanotubes." *Phys. Rev. B*, 58(20), 14013-14019.

Liew, K. M., He, X. Q., and Wong, C. H. (2004). "On the study of elastic and plastic properties of multi-walled carbon nanotubes under axial tension using molecular dynamics simulation." *Acta Mater.*, 52(9), 2521-2527.

Liew, K., Wong, C., and Tan, M. (2006). "Tensile and compressive properties of carbon nanotube bundles." *Acta Mater.*, 54(1), 225-231.

Modi, A., Koratkar, N., Lass, E., Wei, B., and Ajayan, P. M. (2003). "Miniaturized gas ionization sensors using carbon nanotubes." *Nature*, 424(6945), 171-174.

Nielsen, O. H., and Martin, R. M. (1985). "Quantum-mechanical theory of stress and force." *Phys. Rev. B*, 32(6), 3780-3791.

Pantano, A., Parks, D. M., and Boyce, M. C. (2004). "Mechanics of deformation of single- and multi-wall carbon nanotubes." *J. Mech. Phys. Solids*, 52(4), 789-821.

Plimpton, S. (1995). "Fast parallel algorithms for short-range molecular dynamics." *J. Comput. Phys.*, 117(1), 1-19.

Qi, D., Hinkley, J., and He, G. (2005). "Molecular dynamics simulation of thermal and mechanical properties of polyimideccarbon-nanotube composites." *Modell. Simul. Mater. Sci. Eng.*, 13(4), 493-507.

Ruoff, R. S., Qian, D., and Liu, W. K. (2003). "Mechanical properties of carbon nanotubes: Theoretical predictions and experimental measurements." *C.R. Physique*, Dossier: Carbon nanotubes: state of the art and applications, 4(9), 993-1008.

Saito, Y., Yoshikawa, T., Bandow, S., Tomita, M., and Hayashi, T. (1993). "Interlayer spacings in carbon nanotubes." *Phys. Rev. B*, 48(3), 1907-1909.

Shoemake, K. (1992). *Graphics gems III*, Academic Press Professional, San Diego.

Shokrieh, M., and Rafiee, R. (2010). "A review of the mechanical properties of isolated carbon nanotubes and carbon nanotube composites." *Mech. Compos. Mater.*, 46(2), 155-172, 10.1007/s11029-010-9135-0

Stuart, S. J., Tutein, A. B., and Harrison, J. A. (2000). "A reactive potential for hydrocarbons with inter- molecular interactions." *J. Chem. Phys.*, 112(14), 6472-6486.

Thess, A., et al. (1996). "Crystalline ropes of metallic carbon nanotubes." *Science*, 273(5274), 483-487.

JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012 / 21

J. Nanomech. Micromech. 2012.2:15-22.

Treacy, M. M. J., Ebbesen, T. W., and Gibson, J. M. (1996). "Exceptionally high young's modulus observed for individual carbon nanotubes." *Nature*, 381, 678-680.

Vitek, V., and Egami, T. (1987). "Atomic level stresses in solids and liquids." *physica status solidi (b)*, 144(1), 145-156.

Wilson, M. R. (1996). "Determination of order parameters in realistic atom- based models of liquid crystal systems." *J. Mol. Liq.*, 68(1), 23-31.

Yakobson, B. I., Brabec, C. J., and Bernholc, J. (1996). "Nanomechanics of carbon tubes: Instabilities beyond linear response." *Phys. Rev. Lett.*, 76(14), 2511-2514.

Yu, M.-F., Lourie, O., Dyer, M. J., Moloni, K., Kelly, T. F., and Ruoff, R. S. (2000). "Strength and breaking mechanism of multiwalled carbon nanotubes under tensile load." *Science*, 287(5453), 637-640.

22 / JOURNAL OF NANOMECHANICS AND MICROMECHANICS © ASCE / JUNE 2012

J. Nanomech. Micromech. 2012.2:15-22.