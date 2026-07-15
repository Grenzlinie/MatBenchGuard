# Magnetocrystalline anisotropy of Fe₅PB₂ and its alloys with Co and 5d elements: A combined first-principles and experimental study

Mirosław Werwiński*
Institute of Molecular Physics, Polish Academy of Sciences, M. Smoluchowskiego 17, 60-179 Poznań, Poland

Alexander Edström
Materials Theory, ETH Zürich, Wolfgang-Pauli-Straße 27, 8093 Zürich, Switzerland

Ján Rusz
Department of Physics and Astronomy, Uppsala University, Box 516, SE-751 20 Uppsala, Sweden

Daniel Hedlund, Klas Gunnarsson, and Peter Svedlindh
Department of Engineering Sciences, Uppsala University, Box 534, SE-751 21 Uppsala, Sweden

Johan Cedervall and Martin Sahlberg
Department of Chemistry - Ångström Laboratory, Uppsala University, Box 538, SE-751 21 Uppsala, Sweden

![](./images/817402910022303744_1.jpg)
(Received 1 August 2018; revised manuscript received 30 November 2018; published 18 December 2018)

The Fe₅PB₂ compound offers tunable magnetic properties via the possibility of various combinations of substitutions on the Fe and P sites. Here, we present a combined computational and experimental study of the magnetic properties of (Fe₁₋ₓCoₓ)₅PB₂. Computationally, we are able to explore the full concentration range, while the real samples were only obtained for $0 \leqslant x \leqslant 0.7$. The calculated magnetic moments, Curie temperatures, and magnetocrystalline anisotropy energies (MAEs) are found to decrease with increasing Co concentration. Co substitution allows for tuning the Curie temperature in a wide range of values, from about six hundred to zero kelvins. As the MAE depends on the electronic structure in the vicinity of the Fermi energy, the geometry of the Fermi surface of Fe₅PB₂ and the k-resolved contributions to the MAE are discussed. Low-temperature measurements of an effective anisotropy constant for a series of (Fe₁₋ₓCoₓ)₅PB₂ samples determined the highest value of $0.94\ \text{MJ}\ \text{m}^{-3}$ for the terminal Fe₅PB₂ composition, which then decreases with increasing Co concentration, thus confirming the computational result that Co alloying of Fe₅PB₂ is not a good strategy to increase the MAE of the system. However, the relativistic version of the fixed spin moment method reveals that a reduction in the magnetic moment of Fe₅PB₂, by about 25%, produces a fourfold increase of the MAE. Furthermore, calculations for (Fe₀.₉₅X₀.₀₅)₅PB₂ ($X=5d$ element) indicate that 5% doping of Fe₅PB₂ with W or Re should double the MAE. These are results of high interest for, e.g., permanent magnet applications, where a large MAE is crucial.

DOI: 10.1103/PhysRevB.98.214431

## I. INTRODUCTION

Many sectors of modern technology depend on magnetic materials, which are used in such ubiquitous applications as electric motors, power generators, transformers, and recording media. Hence, magnetic materials are crucial not only for the digital technology revolution observed in past decades but also for the green energy revolution expected within the years to come. The fundamentally and technologically most important intrinsic parameters of magnetic materials include the Curie temperature ($T_{\text{C}}$), saturation magnetization ($M_{\text{S}}$), and magnetocrystalline anisotropy energy (MAE). These parameters are important in a wide variety of applications, including hard and soft magnetic materials for energy conversion, spintronics, and information storage. Thus, the ability to predict these basic magnetic parameters from first principles is of utmost importance, and accurate modern electronic structure calculations provide an indispensable tool for exploring new materials with the desired properties. In parallel, experimental synthesis and characterization retain their fundamental importance and a close interplay between computational and experimental work is of ever increasing value in modern materials discovery.

One example of an area in which the search for new magnetic materials with specific combinations of properties has been intense in recent years is that of permanent magnets. In this field it is typically desirable to have large $M_{\text{S}}$, $T_{\text{C}}$, and MAE. This combination is obtained in the commonly used rare-earth transition metal compounds, such as NdFe₁₄B₂. However, the so called *rare-earth crisis* [1] triggered immense international research initiatives in the search for new substitute permanent magnet materials with reduced amounts of, or no, rare-earth elements [2–6]. The main challenge in

*Corresponding author: werwinski@ifmpan.poznan.pl

![](./images/817402910022303744_2.jpg)

FIG. 1. The crystal structure of $Fe_5PB_2$, space group $I4/mcm$ (No. 140).

this context is obtaining a sufficiently large MAE in transition metal compounds, where a uniaxial (e.g., tetragonal or hexagonal) crystal structure is a crucial prerequisite. Other areas of applications depend on other combinations of properties. For example, for magnetocaloric solid state cooling, it is desirable to be able to tune the ordering temperature such that it coincides with the operating temperature (often room temperature) [7,8].

Various works have shown how strain engineering or alloying can be used to carefully tune the properties of magnetic materials to obtain the desired functionality. For example, it was shown that a careful control of strain and alloy concentration allows for a large MAE in bct FeCo alloys [9–12]. The potential route to FeCo-based permanent magnets offered by that work inspired subsequent studies aiming to stabilize tetragonality in FeCo by B or C impurities [13–15]. Also the tetragonal $(Fe_{1-x}Co_x)_2B$ compound has been carefully studied due to its tunable MAE as a function of $x$ [16–20] which, furthermore, has an intriguing temperature dependence [19,21,22]. It was also shown, in both calculations and experiments, that small amounts of $5d$ substitutions on the Fe/Co site allowed a large increase in the MAE of this material [19].

The tetragonal family of compounds with compositions $(Fe_{1-x}Co_x)_5P_{1-y}Si_yB_2$ has also been the subject of numerous recent studies [23–28]. Additionally, other chemical substitutions, including Mn on the Fe/Co site [23], have been considered. Due to the broad range of chemical compositions available, this material offers wide tunability of its magnetic properties. Furthermore, the tetragonal crystal structure could potentially allow for a large MAE and, thus, make the compounds interesting within the context of permanent magnet applications. The materials also exhibit other interesting aspects, such as the temperature-dependent spin-reorientation transition in $Fe_5SiB_2$ [25].

The aim of the work is to investigate the effect of the Co and $5d$ dopants on the tunable magnetic properties of the technologically promising semihard $Fe_5PB_2$ compound. $Fe_5PB_2$ crystallizes in the $Cr_5B_3$-type structure with a body-centered tetragonal (bct) unit cell, space group $I4/mcm$ [29] (see Fig. 1). The unit cell of $Fe_5PB_2$ consists of 4 formula units (32 atoms). Fe atoms occupy two inequivalent sites $Fe_1$ ($16l$) and $Fe_2$ ($4c$). $Fe_1$ atoms are distributed on the 16-fold position, $Fe_2$ and P on the 4-fold, and B on the 8-fold position.

One of the motivations to investigate the $(Fe_{1-x}Co_x)_5PB_2$ system is our previous results for the isostructural $(Fe_{1-x}Co_x)_5SiB_2$ system (with Si in place of P), for which we have predicted the highest MAE $=1.16$ MJ m$^{-3}$ for Co concentration $x=0.3$ [24]. Next, the $(Fe_{0.8}Co_{0.2})_5SiB_2$ sample (with Co concentration $x=0.2$) was synthesized by McGuire and Parker [23] and their magnetic measurements showed an increase of the anisotropy field after Co substitution, which supports our prediction. All the previous experimental studies conducted on the $(Fe_{1-x}Co_x)_5SiB_2$ system are limited to the Fe-rich compositions, while $Co_5SiB_2$ is not known to form [23]. For melt-spun samples $Fe_5(Si_{0.75}Ge_{0.25})B_2$ Lejeune et al. determined a relatively high anisotropy constant $K_1$ of about 0.5 MJ m$^{-3}$ at room temperature, which is about double the value for $Fe_5SiB_2$ [24,30]. Recently, we also presented a combined experimental and theoretical study of the $Fe_5Si_{1-x}P_xB_2$ system, which showed the highest anisotropy constant for the terminal $Fe_5PB_2$ composition [27].

$Fe_5PB_2$ has a high $T_C$ of about $655\pm2$ K, magnetic moment of $1.72$ $\mu_B$/Fe atom ($8.60$ $\mu_B$/f.u.), and anisotropy constant $K_1$ of 0.50 MJ m$^{-3}$ measured at 2 K for a single crystal [26]. The value of an effective anisotropy constant $K_{\text{eff}}$ of $Fe_5PB_2$ obtained in our previous work is however significantly higher and equal to $\sim0.9$ MJ m$^{-3}$ at 10 K [27]. An important parameter, in the context of permanent magnets, is magnetic hardness, defined as

$$
\kappa = \sqrt{\frac{|K|}{\mu_0M_S^2}}, \tag{1}
$$

where $K$ is the magnetic anisotropy constant and $M_S$ is the saturation magnetization. An empirical rule $\kappa>1$ specifies whether the material has a chance to resist self-demagnetization [4]. From the experimental values of $K_{\text{eff}}\sim$ 0.65 MJ m$^{-3}$ and $M_S=0.87$ MA m$^{-1}$ [27], we determined for $Fe_5PB_2$ $\kappa=0.69$ (at 300 K). This implies that without a further engineering of the anisotropy constant, $Fe_5PB_2$ will stay in a category of semihard magnets [4].

In this work we consider alloying of $Fe_5PB_2$ with Co and $5d$ elements. In our recent study of $(Fe_{1-x}Co_x)_5PB_2$ alloys we observed a reduction in magnetization and Curie temperature with an increase of Co concentration [28]. McGuire and Parker also found that 20% Co alloying in $(Fe_{1-x}Co_x)_5PB_2$ leads to a decrease in magnetization, Curie temperature, and anisotropy field [23]. Previously we showed also that increase of the MAE of $3d$ alloys can be achieved through doping with $5d$ elements [19]. In this work we follow this idea and calculate the resultant MAEs of $Fe_5PB_2$-based alloys with 5% substitutions of each $5d$ element in place of Fe.

## II. COMPUTATIONAL AND EXPERIMENTAL DETAILS

### A. Computational details

The electronic band structure calculations for $(Fe_{1-x}Co_x)_5PB_2$ and $(Fe_{0.95}X_{0.05})_5PB_2$ ($X=5d$ element)

systems were carried out with use of the full-potential local-orbital electronic structure code FPLO14.0-49 [31] using a fixed atomic-like basis set. The FPLO was an optimal choice for the accurate calculations of the MAE due to the full potential and fully relativistic character of the code. To model the Co and $5d$ alloying we used the supercell method. The generalized gradient approximation (GGA) was used in the Perdew-Burke-Ernzerhof form (PBE) [32]. A $16 \times 16 \times 16$ $\mathbf{k}$ mesh was found to lead to well converged results of the MAE. For k-point integration, the tetrahedron method was used [33]. The energy and charge density convergence criteria of $\sim 10^{-7}$ eV and $10^{-6}$, respectively, were applied simultaneously. The lattice parameters and Wyckoff positions were optimized for $\text{Fe}_5\text{PB}_2$ and $\text{Co}_5\text{PB}_2$ within a spin-polarized scalar-relativistic approach. The crystallographic parameters for compositions with intermediate Co concentrations were taken from calculations of full lattice relaxation carried out previously in a virtual crystal approximation [28]. For the $(\text{Fe}_{0.95}X_{0.05})_5\text{PB}_2$ supercells we used the same crystallographic parameters as for the $\text{Fe}_5\text{PB}_2$. The MAE was evaluated as a difference between the fully relativistic total energies calculated for quantization axes [100] and [001]. In the adopted sign convention a positive sign of the MAE corresponds to an easy magnetization axis along the [001] direction. The Fermi surface (FS) of $\text{Fe}_5\text{PB}_2$ was calculated on a $28^3$ $\mathbf{k}$ mesh in the boundary of the first Brillouin zone. Using the fully relativistic fixed spin moment (FSM) scheme [34] we study the MAE as a function of total magnetic moment $(m)$ for $\text{Fe}_5\text{PB}_2$. A supercell method was used to model the chemical disorder [18,35]. To build a supercell, multiplication of the basal unit cell and replacement of an appropriate number of atoms of one type by atoms of the other type were made. The Fe atoms were replaced by Co or $5d$ atoms forming the $(\text{Fe}_{1-x}\text{Co}_x)_5\text{PB}_2$ and $(\text{Fe}_{0.95}X_{0.05})_5\text{PB}_2$ compositions ($X=5d$ element). For $(\text{Fe}_{1-x}\text{Co}_x)_5\text{PB}_2$ the considered intermediate compositions were $x=0.2$, $0.4$, $0.6$, and $0.8$. The MAE calculations based on the supercell method [18] are uncommon, as they are time-consuming even for relatively simple alloys. The reason for this is significant increase in the number of inequivalent atomic positions generated for the supercell model. Additionally, accurate results require averaging over several different large supercells [18,36]. This limits the size of supercells which we can use for MAE calculations. Hence, we study only the supercells including symmetry operations and consisting of up to 16 inequivalent atoms. The considered crystal structures are presented in Fig. 2. Three configurations were considered for $\text{Fe}_4\text{Co}_1\text{PB}_2$ and $\text{Fe}_1\text{Co}_4\text{PB}_2$ and one for $\text{Fe}_3\text{Co}_2\text{PB}_2$ and $\text{Fe}_2\text{Co}_3\text{PB}_2$ compositions. For the considered supercell models, the energy convergence with a number of $\mathbf{k}$ points was carefully tested. The supercell method was also employed to calculate the MAE of $(\text{Fe}_{0.95}X_{0.05})_5\text{PB}_2$ compositions with various $5d$ elements $X$. To construct the models, one of twenty Fe atoms in the basal $\text{Fe}_5\text{PB}_2$ supercell was replaced by the dopant. This led to the crystal structures containing 10 inequivalent atomic positions. For calculations of the systems with $5d$ dopants a relatively dense $20 \times 20 \times 10$ $\mathbf{k}$ mesh was used, in order to get the well converged results of the MAE.

![](./images/817402910022303744_3.jpg)

FIG. 2. The crystal structures of the $(\text{Fe}_{1-x}\text{Co}_x)_5\text{PB}_2$ supercells. (a)-(c) Three configurations of $\text{Fe}_4\text{Co}_1\text{PB}_2$ and (d) single configuration for $\text{Fe}_3\text{Co}_2\text{PB}_2$.

To compute the Curie temperatures within the mean-field theory ($T_{\text{C}}^{\text{MFT}}$) for the whole series of $(\text{Fe}_{1-x}\text{Co}_x)_5\text{PB}_2$ compositions the FPLO5.00 version of the code was used [37]. The $T_{\text{C}}^{\text{MFT}}$ is proportional to the total energy difference between the ferromagnetic and paramagnetic configurations [38-40] according to

$$
k_{\text{B}} T_{\text{C}}^{\text{MFT}} = \frac{2}{3} \frac{E_{\text{DLM}} - E_{\text{FM}}}{c}, \tag{2}
$$

where $E_{\text{DLM}}$ and $E_{\text{FM}}$ are total energies for the paramagnetic and ferromagnetic configurations, $k_{\text{B}}$ is the Boltzmann constant, and $c$ is the total concentration of magnetic atoms. In the case of $\text{Fe}_5\text{PB}_2$ containing five Fe atoms (considered as magnetic ones) within a formula unit consisting of eight atoms, the concentration parameter $c$ is equal 5/8. To model the paramagnetic state the disordered local moment (DLM) method was used [41], in which the thermal disorder among the magnetic moments is modeled by using the coherent potential approximation (CPA) [42]. The FPLO5 is the latest public version of the code allowing for the CPA calculations and does not have implemented the GGA. Thus, the local density approximation (PW92) [43] form of the exchange-correlation potential had to be chosen. For the calculations within FPLO5, a scalar-relativistic mode and a $12 \times 12 \times 12$ $\mathbf{k}$ mesh were used. In the FPLO5 the magnetically ordered state (resulting in $E_{\text{FM}}$) was artificially modeled within the CPA, to avoid numerical discrepancies between the ordered (in principle non-CPA) and DLM (CPA) models. In calculations using the FPLO5 code, the minimum basis has been optimized for the terminal compositions $\text{Fe}_5\text{PB}_2$ and $\text{Co}_5\text{PB}_2$; subsequently the resultant compression parameters were used for intermediate compositions modeled with CPA. The VESTA code was used for visualization of crystal structure [44].

### B. Experimental details

The samples in the series $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$ ($x$ from 0.0 to 0.7) were synthesized by mixing stoichiometric amounts of the master alloys ${\text{Fe}}_{5}{\text{PB}}_{2}$ and ${\text{Co}}_{5}{\text{PB}}_{2}$. The master alloys were prepared, in accordance with previous studies [27], from pure elements of iron (Leico Industries, purity 99.995%, surface oxides reduced in ${\text{H}}_{2}$ gas), cobalt (Johnson Matthey, purity 99.999%), phosphorus (Cerac, purity 99.999%), and boron (Wacher-Chemie, purity 99.995%). This was done by forming first the ${\text{TM}}_{2}\text{B}$ ($\text{TM} = \text{Fe}, \text{Co}$), using a conventional arc furnace, and subsequently dropping the phosphorus in a melt of the metal boride in an induction furnace using the drop synthesis method [45]. All samples were subsequently crushed, pressed into pellets, and heat treated in evacuated silica ampules at 1273 K for 14 days after which they were quenched in cold water. At $x$ higher than 0.7 the correct crystalline phase could not be produced; all attempts resulted in a decomposition to other crystalline phases.

To study the phase content and to perform crystal structure analysis of all samples, powder x-ray diffraction (XRD) was used. The measurements were done using a Bruker D8 diffractometer equipped with a LynxEye position-sensitive detector (4° opening) using $\text{CuK}{\alpha}_{1}$ radiation ($\lambda = 1.540598$ Å) at 298 K in a $2\theta$ range of $20^\circ$–$90^\circ$. The crystal structures were evaluated with the software FullProf [46] using refinements according to the Rietveld method [47]. The unit cell parameters were precisely studied using the least-squares refinement of the peak positions, employing the software UnitCell [48].

The synthesized samples were magnetically studied using a Quantum Design PPMS 6000. Samples were immobilized in gelatin capsules with varnish. The magnetization at 3 K was measured between applied magnetic fields of 0 and 7.2 MA m⁻¹. The magnetization in SI units was calculated from the magnetic moment using the sample weight and the crystallographic volume obtained from the XRD measurements at 298 K. When approaching magnetic saturation the magnetization process is described by the law of approach to saturation (LAS) [49]. LAS has been formulated in several ways [49–52], but it takes a general form

$$
\frac{M}{M_{\text{S}}} = \sum_{j} a_{j} H^{j}, \tag{3}
$$

where $j$ is usually an integer, $a_{j}$ are coefficients, $M$ and $M_{\text{S}}$ are magnetization and saturation magnetization, and $H$ is the applied magnetic field. The LAS was used to determine an effective anisotropy constant $|K_{\text{eff}}|$ in the same implementation that we used before [25,27]. The interval 93%–98% of the magnetic saturation was used. The applied formula was

$$
\frac{M}{M_{\text{S}}} = 1 + aH + \frac{b}{H} + \frac{c}{H^{2}}. \tag{4}
$$

The experimental data were fitted with four models in which the $a$ and $b$ coefficients can be zero or nonzero and since the $\frac{1}{H^{2}}$ term is used to extract $|K_{\text{eff}}|$ this part is always considered as nonzero. $|K_{\text{eff}}|$ is given here by

$$
|K_{\text{eff}}| = \sqrt{\frac{15c}{4}} \mu_{0} M_{\text{S}}. \tag{5}
$$

<table>
<caption>Table I. The optimized crystallographic parameters for ${\text{Fe}}_{5}{\text{PB}}_{2}$ and ${\text{Co}}_{5}{\text{PB}}_{2}$ as calculated with the FPLO14 code, using the GGA (PBE) functional, with (SP) and without (NM) spin polarization. Space group $I4/mcm$, No. 140. The Wyckoff positions are $\text{Fe}_{1}/\text{Co}_{1}$ $(x, x+1/2, z)$, $\text{Fe}_{2}/\text{Co}_{2}$ $(0,0,0)$, P $(0,0,1/4)$, and B $(x,x+1/2,0)$. For comparison the values measured in this work at room temperature for ${\text{Fe}}_{5}{\text{PB}}_{2}$ and the literature values for ${\text{Co}}_{5}{\text{PB}}_{2}$ are also reported.</caption>
<thead>
  <tr>
    <th>System</th>
    <th>$a$ (Å)</th>
    <th>$c$ (Å)</th>
    <th>$x_{\text{Fe}_{1}/\text{Co}_{1}}$</th>
    <th>$z_{\text{Fe}_{1}/\text{Co}_{1}}$</th>
    <th>$x_{\text{B}}$</th>
    <th>$c/a$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>${\text{Fe}}_{5}{\text{PB}}_{2}$ (GGA-SP)</td>
    <td>5.456</td>
    <td>10.296</td>
    <td>0.170</td>
    <td>0.139</td>
    <td>0.381</td>
    <td>1.887</td>
  </tr>
  <tr>
    <td>${\text{Fe}}_{5}{\text{PB}}_{2}$ (expt.)</td>
    <td>5.492</td>
    <td>10.365</td>
    <td>0.170</td>
    <td>0.141</td>
    <td>0.381</td>
    <td>1.887</td>
  </tr>
  <tr>
    <td>${\text{Co}}_{5}{\text{PB}}_{2}$ (GGA-SP)</td>
    <td>5.284</td>
    <td>10.541</td>
    <td>0.169</td>
    <td>0.142</td>
    <td>0.376</td>
    <td>1.995</td>
  </tr>
  <tr>
    <td>${\text{Co}}_{5}{\text{PB}}_{2}$ (GGA-NM)</td>
    <td>5.309</td>
    <td>10.406</td>
    <td>0.169</td>
    <td>0.141</td>
    <td>0.376</td>
    <td>1.960</td>
  </tr>
  <tr>
    <td>${\text{Co}}_{5}{\text{PB}}_{2}$ (expt.) [29]</td>
    <td>5.42</td>
    <td>10.20</td>
    <td></td>
    <td></td>
    <td></td>
    <td>1.882</td>
  </tr>
</tbody>
</table>

The difference in results between all four models is relatively small (maximum 0.20 MJ m⁻³); thus in the experimental section we present only the $|K_{\text{eff}}|$ for the simplest model with the coefficients $a = b = 0$.

### III. RESULTS AND DISCUSSION

The results of first-principles calculations of technologically important magnetic parameters for the considered systems are shown. For $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$ the $M_{\text{S}}$, $T_{\text{C}}$, and MAE are presented. For $({\text{Fe}}_{0.95}{X}_{0.05}{)}_{5}{\text{PB}}_{2}$ ($X = 5d$ element) the results are limited to the MAE and partial magnetic moments. For the main phase—${\text{Fe}}_{5}{\text{PB}}_{2}$—a detailed analysis of electronic structure, magnetic moments, Fermi surface, and MAE is given. The theoretical efforts are complemented by experimental synthesis and measurements of the considered $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$ compositions.

#### A. Crystal structure and electronic structure of ${\text{Fe}}_{5}{\text{PB}}_{2}$ and ${\text{Co}}_{5}{\text{PB}}_{2}$

The optimized crystallographic parameters of ${\text{Fe}}_{5}{\text{PB}}_{2}$ and ${\text{Co}}_{5}{\text{PB}}_{2}$ are compared in Table I with the results of measurements. For ${\text{Fe}}_{5}{\text{PB}}_{2}$ the agreement between the GGA and experiment is good and for the ${\text{Co}}_{5}{\text{PB}}_{2}$ the GGA underestimates $a$ and overestimates $c$. The disagreement may originate from both theory and experiment. The lattice parameters of ${\text{Co}}_{5}{\text{PB}}_{2}$ were last refined by Rundqvist back in 1962 [29]. Unfortunately, we did not manage to synthesize the ${\text{Co}}_{5}{\text{PB}}_{2}$ sample. According to the comprehensive study of Haas *et al.* the PBE remains the best GGA functional for most of the solids containing $3d$ transition elements [53]. However, it has a tendency to overestimate the lattice constants [53]. The presented PBE results for ${\text{Fe}}_{5}{\text{PB}}_{2}$ go against this trend. The PBE underestimates also a volume of ${\text{Co}}_{5}{\text{PB}}_{2}$. The observed underestimation of lattice parameters/volumes is similar to the results obtained from GGA for bcc Fe [54] and fcc Co [55], for which the use of GGA leads to about 0.5%–1.0% underestimation of the lattice parameters (which is equivalent to about 1.5%–3.0% underestimation in volume). In the case of ${\text{Fe}}_{5}{\text{PB}}_{2}$ and ${\text{Co}}_{5}{\text{PB}}_{2}$ the calculated (with spin polarization) PBE volumes are 2.2% and 1.8% underestimated, respectively. It is surprising, however, that when the $c/a$ ratio for

![](./images/817402910022303744_4.jpg)

FIG. 3. The spin-projected partial and total densities of states (DOSs) for Fe₅PB₂ and Co₅PB₂. Calculations were done within the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling).

Fe₅PB₂ is in agreement with experiment (both values are equal to 1.887), the corresponding result for Co₅PB₂ from the (spin-polarized) GGA is significantly different (1.995 against the experimental value 1.882). The nonmagnetic GGA calculations lead for Co₅PB₂ to c/a equal to 1.960—also significantly different from the measured value. We can only give a very general explanation for this discrepancy as coming from the insufficient treatment of corrections in the PBE functional.

The spin-projected partial and total densities of states (DOSs) for Fe₅PB₂ and Co₅PB₂ are presented in Fig. 3. The valence bands of these two metallic systems start around −9 eV. In a range from −9 to −3 eV the main contributions to a valence band come from the P 3p and B 2p orbitals, while from −5 eV up to above $E_{\text{F}}$ the dominant role is played by the 3d orbitals. The observed spin splitting (proportional to the magnetic moment) is bigger for Fe₅PB₂ than for Co₅PB₂, which is related to a higher filling of the valence band for Co₅PB₂ than for Fe₅PB₂. The majority spin channels of the two compounds are similar and nearly completely occupied. The additional electrons in the Co₅PB₂ fill mainly the minority spin channel, reducing the magnetic moment. The weak spin polarization of the P 3p and B 2p orbitals is induced by the 3d orbitals. The spin polarization on the Fermi level is defined as $P = \left| \frac{D_{\text{u}} - D_{\text{d}}}{D_{\text{u}} + D_{\text{d}}} \right|$, where $D_{\text{u}}$ is the density of states at the Fermi level of the majority spin channel, and $D_{\text{d}}$ for the minority spin channel. The calculated spin polarization on the Fermi level (a total value including Fe, Co, P, and B contributions) is about 0.46 for Fe₅PB₂ and 0.60 for Co₅PB₂.

### B. Magnetic moments of (Fe₁₋ₓCoₓ)₅PB₂

The calculated Co concentration dependence of the total magnetic moment (a sum of spin and orbital contributions) for the (Fe₁₋ₓCoₓ)₅PB₂ system is presented in Fig. 4 together with the experimental results at low temperature (3 K) [28].

![](./images/817402910022303744_5.jpg)

FIG. 4. The Co concentration dependence of total magnetic moment for the (Fe₁₋ₓCoₓ)₅PB₂ system. The results calculated with the supercell method are denoted by red circles, the results measured at 3 K by blue squares [28]. Linear fits are drawn for a better perception. Calculations were done with the FPLO14 code, using the PBE functional, and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling).

Whereas the results presented here are based on the supercell approach, in our previous work [28] one can find the corresponding $m(x)$ plots based on the virtual crystal approximation and coherent potential approximation. The calculated and experimental $m(x)$ curves presented in Fig. 4 stay in good qualitative agreement, showing a linear decrease of magnetic moment with Co concentration. Nevertheless, they differ by about 0.5–1.0 $\mu_{\text{B}}$/f.u., where the lower values come from measurements. The reasons for this discrepancy should be sought on both experimental and theoretical sides. Looking at the experiment, it is worth noting that the samples produced in this work are slightly nonstoichiometric and with a small number of impurities [28]. Our measurements at 3 K for a powder sample of Fe₅PB₂ showed a total magnetic moment equal to 8.29 $\mu_{\text{B}}$/f.u. in comparison to 8.6 $\mu_{\text{B}}$/f.u. obtained by Lamichhane *et al.* for a Fe₅PB₂ single crystal at 2 K [26]. This leads us to the conclusion that the magnetic moments we have measured may be slightly underestimated. The calculated total magnetic moment of Fe₅PB₂ (8.85 $\mu_{\text{B}}$/f.u.) using GGA is closer to the result obtained for the single crystal than for the powder sample. The discrepancy between the result of GGA calculations and single-crystal measurements can then be attributed to the insufficiency of the GGA in the description of correlations; however the calculations still provide an acceptable level of agreement with experiment.

The calculated spin, orbital, and total magnetic moments ($m_{s}$, $m_{l}$, $m$) for Fe₅PB₂ and Co₅PB₂ are collected in Table II. For Fe₅PB₂ the calculated magnetic moments on the Fe₁ and Fe₂ sites are equal to 1.81 (1.62) and 2.16 (2.16) $\mu_{\text{B}}$, respectively, where in parentheses are given estimations from the magnetic hyperfine fields [56]. The induced spin magnetic moments on P and B are relatively small and oriented antiparallel to the dominant 3d moments on Fe/Co. The total magnetic moments of Fe₅PB₂ and Co₅PB₂ are almost entirely of spin character, where the 3d orbital magnetic moments

<table><caption>TABLE II. The spin, orbital, and total magnetic moments [$\mu_\text{B}$ (atom or f.u.)$^{-1}$] for Fe$_5$PB$_2$ and Co$_5$PB$_2$ as calculated along the quantization axis [001] (easy axis) with the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling). The saturation magnetization $M_\text{S}$ (MA m$^{-1}$) is evaluated based on the total magnetic moments $m$ and theoretical lattice parameters.</caption>
<thead>
  <tr>
    <th rowspan="2">Site</th>
    <th colspan="2">Fe$_5$PB$_2$</th>
    <th colspan="2">Co$_5$PB$_2$</th>
  </tr>
  <tr>
    <th>$m_\text{s}$</th>
    <th>$m_\text{l}$</th>
    <th>$m_\text{s}$</th>
    <th>$m_\text{l}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$3d_1$</td>
    <td>1.78</td>
    <td>0.033</td>
    <td>0.41</td>
    <td>0.011</td>
  </tr>
  <tr>
    <td>$3d_2$</td>
    <td>2.11</td>
    <td>0.052</td>
    <td>0.64</td>
    <td>0.013</td>
  </tr>
  <tr>
    <td>P</td>
    <td>$-$0.13</td>
    <td>0.002</td>
    <td>$-$0.02</td>
    <td>0.001</td>
  </tr>
  <tr>
    <td>B</td>
    <td>$-$0.21</td>
    <td>0.001</td>
    <td>$-$0.05</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>$m$</td>
    <td colspan="2">8.85</td>
    <td colspan="2">2.20</td>
  </tr>
  <tr>
    <td>$M_\text{S}$</td>
    <td colspan="2">1.07</td>
    <td colspan="2">0.28</td>
  </tr>
</tbody>
</table>

($m_\text{l}$'s) are nearly quenched. The $m_\text{l}$'s of Fe$_1$ and Fe$_2$ of the Fe$_5$PB$_2$ (calculated for the [001] quantization axis) are equal to 0.033 $\mu_\text{B}$ and 0.052 $\mu_\text{B}$, respectively. These values surround the $m_\text{l}$ value calculated for bcc Fe (0.043 $\mu_\text{B}$) and are reduced in comparison to the experimental value for the bcc Fe (0.086 $\mu_\text{B}$) [57].

The underestimation of the orbital magnetic moment in transition metals is recognized as a general weakness of the local density approximation (LDA) and GGA. Finally, almost no orbital contributions are observed for P and B atoms ($m_\text{l} \sim 10^{-3}\ \mu_\text{B}$). The calculated $m$ of Co$_5$PB$_2$ is equal to 2.20 $\mu_\text{B}$/f.u. (0.44 $\mu_\text{B}$/Co atom). For comparison, the experimental magnetic moment of hcp Co is equal to 1.67 $\mu_B$/atom [58]. The calculated $m_\text{l}$'s of Co$_1$ and Co$_2$ of the Co$_5$PB$_2$ are equal to 0.011 $\mu_\text{B}$ and 0.013 $\mu_\text{B}$, respectively, and are one order of magnitude smaller than the $m_\text{l}$ measured for hcp Co (0.13 $\mu_\text{B}$) [59]. Although the theoretical values of magnetic moments for Co$_5$PB$_2$ have been presented above, the magnetic ground state of this system has not been unambiguously resolved, which will be discussed in the next section.

### C. Curie temperature of (Fe$_{1-x}$Co$_x$)$_5$PB$_2$

The Curie temperatures [$T_\text{C}^\text{MFT}$(LDA)] calculated for the whole concentration range of the (Fe$_{1-x}$Co$_x$)$_5$PB$_2$ system within the mean-field theory and with the LDA functional are presented in Fig. 5. The observed overall decrease of the calculated $T_\text{C}^\text{MFT}$ with increase of Co concentration is consistent with experimental observations [23,28]. However, in the whole range in which it is possible to compare the MFT-LDA results with the experiment ($0.0 \leqslant x \leqslant 0.7$), theoretical values are smaller. For example, the calculated $T_\text{C}^\text{MFT}$(LDA) of Fe$_5$PB$_2$ is equal 547 K, whereas the corresponding experimental value is 622 K for the powder sample [28], or $655 \pm 2$ K for the single crystal [26]. This difference is due to the limitations of the MFT approach and insufficiency of the LDA in description of correlations. By calculating Heisenberg exchange interactions, one could extract accurate critical temperatures using the random phase approximation (RPA) or Monte Carlo simulations [60,61]. The insufficiency of the LDA manifests in underestimated values of the calculated magnetic moments of Fe$_5$PB$_2$: 7.30 $\mu_B$/f.u. versus 8.6 $\mu_\text{B}$/f.u. from experiment for a single crystal [26]. As has been shown in the previous subsection, a much better description of magnetic moments of Fe$_5$PB$_2$ in relation to the experimental result can be obtained by using the GGA functional instead of the LDA. Thus, we suggest that the negative effect on $T_\text{C}^\text{MFT}$ coming from the limitations of the LDA can be partially corrected by using the correction parameter based on the magnetic moments obtained from the GGA. In the Heisenberg model, $T_\text{C}^\text{MFT}$ is proportional to the squared effective moment ($m_\text{eff}^2$). Defining $b = \frac{m^\text{GGA}}{m^\text{LDA}}$ the corrected Curie temperature is $b^2 T_\text{C}^\text{MFT}$(LDA), where in the case of (Fe$_{1-x}$Co$_x$)$_5$PB$_2$ $b$ is about 1.2. Figure 5 shows that for the region of intermediate Co concentrations the $b^2 T_\text{C}^\text{MFT}$(LDA) curve is in a better agreement with experiment than the uncorrected MFT-LDA results.

![](./images/817402910022303744_6.jpg)

FIG. 5. The Curie temperatures as functions of Co concentration $x$ in (Fe$_{1-x}$Co$_x$)$_5$PB$_2$. The theoretical $T_\text{C}^\text{MFT}$(LDA) are calculated in the mean-field approximation with the FPLO5 code, using the LDA functional, treating the chemical disorder with CPA, and modeling the paramagnetic state with DLM. The experimental $T_\text{C}$ was defined from the inflection point of field-cooled magnetization versus temperature measurements in a field of $\mu_0 H = 0.01$ T [28].

Unfortunately, we were unable to get experimental results of $T_\text{C}$ for Co concentrations $x > 0.7$. Because of this, we cannot unambiguously resolve the issue of the magnetic ground state of terminal composition Co$_5$PB$_2$. Linear extrapolation of experimental magnetic moments for the (Fe$_{1-x}$Co$_x$)$_5$PB$_2$ system suggests nonzero moment for Co$_5$PB$_2$; see Fig. 4. On the contrary, linear extrapolation of the measured Curie temperature suggests a transition from ordered to disordered magnetic state at about $x = 0.9$, and therefore a nonmagnetic ground state of Co$_5$PB$_2$; see Fig. 5. Furthermore, experimental results reported by McGuire and Parker suggested the absence of magnetic ordering for Co$_5$PB$_2$ [23]. From a theoretical point of view, both uncorrected and corrected approaches show nonzero values of $T_\text{C}$ for the Co-rich region [$T_\text{C}^\text{MFT}$(LDA) = 37 K for Co$_5$PB$_2$]. Taking into account (1) the problems with synthesis of the Co$_5$PB$_2$ phase, (2) preliminary character of the measurements reported by McGuire and Parker, (3) issues mentioned in the previous subsection regarding optimization of the structural model of Co$_5$PB$_2$, and (4) limitations of the LDA/GGA in the description of correlations of Co-rich

![](./images/817402910022303744_7.jpg)

FIG. 6. (a)-(i) The nine sheets of the Fermi surface of Fe₅PB₂. (i) The $\mathbf{k}$ path used to calculate the band structure plot. Inside the visible tubes the sheets (e) and (f) contain the invisible pockets centered at $\Gamma$. Calculations were done with the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling).

phases, we conclude that based on existing data the magnetic ground state of Co₅PB₂ cannot be definitively determined.

### D. Fermi surface of Fe₅PB₂

Figure 6 presents the calculated Fermi surface (FS) of Fe₅PB₂ in the boundary of the first Brillouin zone. The FS of Fe₅PB₂ reflects the tetragonal symmetry of the crystal. The FS consists of nine sheets and is relatively complex. The states at the Fermi level $(E_{\text{F}})$ have a Fe $3d$ character, as can be read from the DOS plots in Fig. 3. The observed FS sheets can be divided into two groups. The first group consists of four nested sheets of hole type, see panels (a)-(d) of Fig. 6, and the second group includes the remaining five sheets of electron type nested in a multiwalled way around the high-symmetry point $Z$; see panels (e)-(i) of Fig. 6. While the sheets (c)-(f) form rather tubular shapes, allowing for open orbits along the symmetry axis, the remaining sheets, (a)-(b) and (g)-(i), take the form of pockets enabling only for closed FS orbits [62]. Because the band structure was calculated with spin-orbit coupling, the FS sheets cannot be unambiguously attributed to a particular spin channel.

### E. Magnetocrystalline anisotropy of Fe₅PB₂

The results of investigating the MAE of Fe₅PB₂ carried out in this work are the band structure in the vicinity of the Fermi level, one- and two-dimensional $\mathbf{k}$-resolved MAE plots, and the cross section of FS. Our inquiry is complemented by considerations of MAE engineering, as for example reduction of total magnetic moment. The calculated MAE of the Fe₅PB₂ is $0.52\ \text{MJ}\ \text{m}^{-3}$. It indicates a uniaxial magnetocrystalline anisotropy with an easy axis along the tetragonal axis. This result stays in good agreement with the experimental value of the anisotropy constant measured at $2\ \text{K}\ (0.50\ \text{MJ}\ \text{m}^{-3})$ and with the previous theoretical findings $(0.46\ \text{MJ}\ \text{m}^{-3})$ [26]. Previously reported results for Fe₅PB₂ show that $K_{1}$ first increases with temperature starting from $2\ \text{K}$ up to about $100\ \text{K}$ and then decreases to zero at $T_{\text{C}}$ [26]. The well known origin of the magnetocrystalline anisotropy is the spin-orbit coupling, which is taken into account in the fully relativistic full potential calculations. In comparison with the scalar-relativistic approach, the fully relativistic one results in additional splitting of the electronic bands. Since the spin-orbit coupling constant of $3d$ metals is on the order of $0.05\ \text{eV}$, the spin-orbit splitting also does not exceed this value. The spin-orbit splitting leads to slightly different band structures for different quantization axes (e.g., for the orthogonal [001] and [100] axes). Figure 7 presents the band structures calculated for Fe₅PB₂ in the proximity of $E_{\text{F}}$, together with the MAE contributions per $\mathbf{k}$ point obtained with the magnetic force

![](./images/817402910022303744_8.jpg)

FIG. 7. The band structure of Fe₅PB₂ calculated for quantization axes [100] (solid red lines) and [001] (dashed blue lines), together with the MAE contribution of each $\mathbf{k}$ point (thick green line) as obtained by the magnetic force theorem. The high-symmetry points are presented within the Brillouin zone in Fig. 6(i). Calculations were done with the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling).

![](./images/817402910022303744_9.jpg)

FIG. 8. (a) The cross section of the k-resolved MAE with (b) the overlapped cross section of the Fermi surface (black lines) for the $Fe_5PB_2$. The results of MAE(k) are obtained by the magnetic force theorem within the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling).

theorem [63–65] from the formula

$$
\begin{aligned}
\text{MAE} &= E(\theta = 90^\circ) - E(\theta = 0^\circ) \\
&= \sum_{\text{occ}'} \epsilon_i(\theta = 90^\circ) - \sum_{\text{occ}''} \epsilon_i(\theta = 0^\circ),
\end{aligned} \tag{6}
$$

where $\theta$ is an angle between the magnetization direction and the $c$ axis, $E(\theta)$ is the total energy for a specific direction, and $\epsilon_i$ is the band energy of the $i$th state. The spin-orbit splitting is most easily observed for the energy window of a tenth of an eV around $E_{\text{F}}$. The k-point-resolved MAE takes positive and negative values, depending on the spin and orbital character of the bands near the Fermi energy. Generally, negative MAE contributions coincide with occupied bands for a [100] spin quantization axis (solid red line) being pushed below corresponding bands for a [001] spin quantization axis (dashed blue line), and vice versa for positive contributions. For example, at the $Z$ point, there is a negative MAE contribution and at approximately $-0.3$ eV one can observe a solid red line below the dashed blue line. A more detailed analysis of the MAE contributions is in principle straightforward but somewhat complicated due to the complex band structure. Nevertheless, one can clearly observe the characteristic jumps where the bands cross $E_{\text{F}}$, confirming the usual behavior that the MAE is determined by the electronic structure around the Fermi energy. Thus, controlling the MAE around $E_{\text{F}}$ also allows for control of the MAE, as is practically possible, for example, via alloying.

The same form of presentation of the k-resolved MAE that we have shown in Fig. 7 dominates in the literature. However, it is possible to plot the MAE(k) data within a three-dimensional Brillouin zone, similar to the FS. Recently, the 3D MAE(k) maps were presented for $(Fe_{1-x}Co_x)_2B$ and FeNi [17,66]. In Fig. 8(a) we show a cross section of the MAE(k) (single plane going trough the $\Gamma$ point). The selected profile is perpendicular to the easy axis [001], crosses the high-symmetry point $\Gamma$, and is limited by the Brillouin zone boundaries. The MAE(k) cross section is a relatively complicated map of symmetric regions consisting of positive and negative contributions. The MAE contributions observed in Fig. 8 along the orthogonal axes [100] and [010] are not equal, because the [100] direction is distinguished as quantization axis resulting in breaking of the fourfold symmetry. As the $E_{\text{F}}$ is an upper integration boundary of total MAE, the FS sheets coincide with sharp changes in the k-resolved MAE contributions. This can be seen in Fig. 8(b), where the MAE(k) 2D plot is overlapped by the corresponding section of the FS. As many of the k-resolved MAE contributions are on the order of $10^{-3}$ eV per k point, the total MAE value of about $10^{-4}$ eV/f.u. (83 $\mu$eV/f.u. or 0.52 MJ m$^{-3}$) indicates a fine compensation of many bigger components. Unfortunately, this extra fine compensation and the complexity of the MAE(k) make the ways to increase the MAE of the material difficult to predict.

![](./images/817402910022303744_10.jpg)

FIG. 9. MAE as function of total magnetic moment $(m_S + m_L)$ for $Fe_5PB_2$ and $Fe_5SiB_2$ [24] as calculated with fixed spin moment (FSM) method with the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling). The equilibrium values of magnetic moments are denoted with dotted lines.

### F. Fully relativistic fixed spin moment calculations for $Fe_5PB_2$

The MAE value for $Fe_5PB_2$ (0.52 MJ m$^{-3}$) is calculated with the equilibrium value of the magnetic moment (8.85 $\mu_{\text{B}}$/f.u.). In the fixed spin moment (FSM) method [34] the value of spin magnetic moment is considered as a parameter. The fully relativistic implementation of FSM method allows us to calculate the MAE as a function of spin magnetic moment. Previously, we presented the MAE results as a function of FSM and Co concentration for the $(Fe_{1-x}Co_x)_2B$ alloys [19]. Figure 9 presents the evolution of the MAE with the total magnetic moment $m$ for the $Fe_5PB_2$, together with the previous results for $Fe_5SiB_2$ [24]. The two MAE($m$) plots are similar in shape. Going down from an equilibrium $m$ the corresponding MAE first increases, then it reaches maximum, to decrease finally to zero at $m$ equals zero. For $Fe_5PB_2$ the maximum MAE($m$) is 1.94 MJ m$^{-3}$ for a fixed total magnetic moment of 6.7 $\mu_{\text{B}}$/f.u., which means that the optimal magnetic moment has to be reduced by about 25% with respect to the equilibrium value (8.85 $\mu_{\text{B}}$/f.u.). Thus, the question

![](./images/817402910022303744_11.jpg)

FIG. 10. The experimental effective anisotropy constant $|K_{\text{eff}}|$ of the $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$ system at 3 K (the sign of $K_{\text{eff}}$ is not considered), together with the magnetocrystalline anisotropy energy MAE values as calculated with the FPLO14 code. In calculations the supercell method for modeling of chemical disorder and the PBE functional were used. The relativistic effects were treated in a full 4-component formalism, including spin-orbit coupling (for $x$ equal to 0.2 and 0.8 several inequivalent supercells are considered). For comparison we show the value of $K_{1}$ measured by Lamichhane *et al.* for ${\text{Fe}}_{5}{\text{PB}}_{2}$ [26].

arises of how to stabilize this reduction. A simple solution would be alloying the magnetic Fe by a nonmagnetic element, which often results in a linear decrease of magnetization. However, alloying with a new element can severely affect the band structure, which would change also the expected value of the MAE. The smallest impact on the electronic structure should have substitutions chemically most similar to Fe and for this purpose we suggest Ru and Os of the Fe group. Another strategy could be alloying of Fe ($Z_{\text{Fe}}=26$) with two elements at the same time, e.g., Cr ($Z_{\text{Cr}}=24$) and Ni ($Z_{\text{Ni}}=28$), keeping a constant number of the valence electrons, which should affect the band structure the least. The above considerations, however, take into account only the band structure and neglect further issues like the crystal structure and size of the atoms, for example.

### G. Magnetocrystalline anisotropy of $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$

The effect of Fe/Co alloying on the MAE is not obvious in advance, whereby the first-principles calculations are of great value in predicting the results, as has been shown previously for the $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{2}\text{B}$ [17] and $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{SiB}}_{2}$ [24] alloys. Figure 10 presents the MAE($x$) dependence for the $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$ system as calculated with use of the supercell method. The MAE calculations based on the supercell method proved to be one of the most accurate method for evaluation of the MAE [18]. However, our calculations were limited by computational challenges of the supercell method. Thus, in practice we were able to consider only a relatively small number of configurations; see Sec. II A. The scattering of individual data points for $x=0.2$ and $x=0.8$ is in a similar range to that observed by Däne *et al.* [18] or Steiner *et al.* [36] and shows that an averaging for several configurations is needed for accurate results. In Fig. 10 the regions of positive and negative MAE (of perpendicular and in-plane anisotropy) are separated at Co concentration $x\simeq0.5$. The calculated MAE is equal $0.52$ MJ m$^{-3}$ for ${\text{Fe}}_{5}{\text{PB}}_{2}$ and $-0.51$ MJ m$^{-3}$ for ${\text{Co}}_{5}{\text{PB}}_{2}$, whereas the anisotropy value close to zero observed for $x\simeq0.5$ indicates a good soft magnetic material. Figure 10 presents also the low-temperature measurements of the effective anisotropy constant $|K_{\text{eff}}|$ carried out at 3 K for several $({\text{Fe}}_{1-x}{\text{Co}}_{x}{)}_{5}{\text{PB}}_{2}$ compositions within the boundaries of $0.0\leqslant x\leqslant0.7$. The value of $|K_{\text{eff}}|$ is the highest ($0.94$ MJ m$^{-3}$) for ${\text{Fe}}_{5}{\text{PB}}_{2}$ and the lowest for a Co concentration $x\sim0.6$. $|K_{\text{eff}}|$ measured for ${\text{Fe}}_{5}{\text{PB}}_{2}$ is significantly larger than the $K_{1}=0.5$ MJ m$^{-3}$ measured at 2 K for the single crystal [26]. The decrease of $|K_{\text{eff}}|$ with $x$ is in agreement with the previous measurements for $({\text{Fe}}_{0.8}{\text{Co}}_{0.2}{)}_{5}{\text{PB}}_{2}$ suggesting that 20% Co substitution reduces the anisotropy field [23]. Previously we also showed the corresponding $|K_{\text{eff}}|$ results for the ${\text{Fe}}_{5}{\text{Si}}_{1-x}{\text{P}}_{x}{\text{B}}_{2}$ system [27]. The presented values of $|K_{\text{eff}}|$ for ${\text{Fe}}_{5}{\text{PB}}_{2}$ were $\sim0.9$ MJ m$^{-3}$ at 10 K and $\sim0.65$ MJ m$^{-3}$ at 300 K [27]. Notice that LAS is unable to determine the sign of $|K_{\text{eff}}|$ and thus the negative values of MAE predicted for $x\gtrsim0.6$ cannot be confirmed by this method. Other methods, such as magnetometry measurements in different directions for single crystals or torque magnetometry, would be preferable. Here, single crystals were not available, and up to 10 wt. % of impurities were present in the samples. Therefore, given the limitation in the model and the starting material the results presented from these should be seen as semiquantitative. Taking into account the limitations of the LAS and the supercell method, the differences between theoretical and measured MAE($x$) results are acceptable. We conclude that Co alloying of ${\text{Fe}}_{5}{\text{PB}}_{2}$ is not a good strategy to increase the MAE of this system.

![](./images/817402910022303744_12.jpg)

FIG. 11. Magnetization ($M$) as a function of applied field ($H$) measured for ${\text{Fe}}_{5}{\text{PB}}_{2}$ at 3 K. The inset shows a normalized magnetization ($M/M_{\text{S}}$) as a function of $1/H^{2}$.

A typical magnetization ($M$) versus applied field ($H$) curve measured at 3 K is shown in Fig. 11. The inset of Fig. 11 presents a plot of $M/M_{\text{S}}$ versus $1/H^{2}$ as used to determine the $|K_{\text{eff}}|$ within the LAS method. More details on the implementation of the LAS method can be found in Sec. II B.

![](./images/817402910022303744_13.jpg)

FIG. 12. MAE for various $5d$ elements $X$ in $(Fe_{0.95}X_{0.05})_5PB_2$ as calculated with the supercell method. Calculations were done with the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling). The dashed line indicates the MAE of $Fe_5PB_2$ ($0.52$ MJ m$^{-3}$) for comparison.

![](./images/817402910022303744_14.jpg)

FIG. 13. Spin $(m_s)$ and orbital $(m_l)$ magnetic moments of $5d$ transition metal impurities $X$ in $(Fe_{0.95}X_{0.05})_5PB_2$ as calculated for spin quantization axis along the $c$ axis. Supercell calculations were done with the FPLO14 code using the PBE functional and treating the relativistic effects in a full 4-component formalism (including spin-orbit coupling).

### H. Doping $Fe_5PB_2$ with $5d$ elements

One of the methods of tailoring the MAE is doping with $5d$ elements [19,67]. Previously, we have confirmed that the $5d$ elements can significantly affect the MAE due to a large spin-orbit coupling [19]. From the $Fe_5Si_{1-x}P_xB_2$ and $(Fe_{1-x}Co_x)_5PB_2$ systems, the highest MAE is found in the $Fe_5PB_2$ phase [27]. Thus, it is considered as the parental compound for a further MAE engineering. The MAE of $(Fe_{0.95}X_{0.05})_5PB_2$ compounds ($X=5d$ elements) is calculated using the supercell method. The results are shown in Fig. 12, with the $5d$ element marked on the $x$ axis and dashed line indicating the MAE of undoped $Fe_5PB_2$. The $5d$ doping has a sometimes beneficial and sometimes adverse effect on the MAE [35,68,69]. Significant increase of the MAE is observed for W or Re doping, similar to the case of $(Fe_{1-x}Co_x)_2B$ alloys investigated experimentally in our previous work [19]. The MAE grows from $0.52$ MJ m$^{-3}$ for $Fe_5PB_2$ to about $1.1$ MJ m$^{-3}$ for the compositions with W or Re, with 5% Fe substitution. Previously we have shown that the increase in the MAE observed for W and Re dopants is mainly due to the strong spin-orbit coupling of the $5d$ atoms; however other variations in electronic structure also affect the MAE [19]. Although in our calculations the $5d$ elements are initially considered as nonmagnetic, the dopants undergo spin polarization in a ferromagnetic medium and contribute to the total magnetic moment of the system. The calculated spin and orbital magnetic moments on the $5d$ impurity show a clear trend along the increasing atomic number of the $5d$ element; see Fig. 13. The spin magnetic moments of $5d$ impurities are antiparallel to the Fe moments in the early $5d$ series, while they are parallel in the late $5d$ series. Corresponding trends for $5d$ atoms in magnetic $3d$ hosts have been found previously computationally [70,71] and experimentally [72].

### IV. SUMMARY AND CONCLUSIONS

Our considerations began with a detailed theoretical analysis of the $Fe_5PB_2$ compound. The Fe $3d$ orbitals are dominant in the valence band and responsible for the formation of large magnetic moments. For the $Fe_5PB_2$ the fully relativistic band structure in the vicinity of the Fermi level was considered to better understand the origin of the high value of magnetocrystalline anisotropy energy (MAE). The calculated Fermi surface requires experimental confirmation. The results of fully relativistic fixed spin moment calculations suggested that reduction of the magnetic moment of $Fe_5PB_2$ should induce about fourfold increase of the MAE. For practical realization of magnetic moment reduction it is suggested to alloy Fe with a nonmagnetic element Ru or Os from the Fe group, or to partially replace Fe with two elements at once, Cr and Ni, for example, keeping a constant number of valence electrons.

Three critical parameters for technological applications—saturation magnetization $(M_S)$, Curie temperature $(T_C)$, and the MAE—were calculated for the whole concentration range between $Fe_5PB_2$ and $Co_5PB_2$. The calculated $M_S$ and $T_C$ decreased with Co concentration and for the terminal composition $Co_5PB_2$ a weakly ordered magnetic ground state was predicted. The calculated $m(x)$ and $T_C(x)$ were in decent agreement with the measurements, although the ferromagnetic ground state of $Co_5PB_2$ is questionable. The Co doping in the $(Fe_{1-x}Co_x)_5PB_2$ system gives the possibility of tuning the $T_C$ in a range from about six hundred kelvins to almost down to zero. The calculated MAE was positive for $Fe_5PB_2$, negative for $Co_5PB_2$, and went through zero around 50% Co concentration. This picture of $MAE(x)$ behavior was in overall agreement with the experimental study of the effective anisotropy constant $|K_{eff}|$ for the $(Fe_{1-x}Co_x)_5PB_2$ alloys. The measurements showed the highest $|K_{eff}|$ value for stoichiometric $Fe_5PB_2$ which decreased with Co doping. We concluded then that Co alloying is not a good strategy to increase the MAE of $Fe_5PB_2$ alloy. The measured $|K_{eff}|$ of about $0.94$ MJ m$^{-3}$ at 3 K was, however, the highest value obtained so far for $Fe_5PB_2$, giving a hope for potential application of its other alloys. It was also calculated how the 5% doping of Fe with $5d$ elements affects the MAE of the $Fe_5PB_2$. It was shown that $Fe_5PB_2$ doping with W or

Re results in significant increase of the magnetocrystalline anisotropy energy.

## ACKNOWLEDGMENTS
M.W. and J.R. acknowledge financial support from the Foundation for Polish Science grant HOMING. The HOM- ING program is cofinanced by the European Union under the European Regional Development Fund. J.C. and M.S. acknowledge financial support from the Swedish Research Council. D.H., P.S., and K.G. acknowledge the Swedish Foun- dation for Strategic Research for financial support. Some of the computations were performed on resources provided by the Poznań Supercomputing and Networking Center (PSNC). We thank Bartosz Wasilewski for help with language editing and Dr. Jakub Kaczkowski for reading the manuscript and helpful discussion.

[1] K. Bourzac, Technol. Rev. 114, 58 (2011).

[2] D. Niarchos, G. Giannopoulos, M. Gjoka, C. Sarafidis, V. Psycharis, J. Rusz, A. Edström, O. Eriksson, P. Toson, J. Fidler, E. Anagnostopoulou, U. Sanyal, F. Ott, L.-M. Lacroix, G. Viau, C. Bran, M. Vazquez, L. Reichel, L. Schultz, and S. Fähler, JOM 67, 1318 (2015).

[3] S. Hirosawa, J. Magn. Soc. Jpn. 39, 85 (2015).

[4] R. Skomski and J. Coey, Scr. Mater. 112, 3 (2016).

[5] D. Li, D. Pan, S. Li, and Z. Zhang, Sci. China: Phys., Mech. Astron. 59, 617501 (2016).

[6] S. Hirosawa, M. Nishino, and S. Miyashita, Adv. Nat. Sci.: Nanosci. Nanotechnol. 8, 013002 (2017).

[7] O. Gutfleisch, M. A. Willard, E. Brück, C. H. Chen, S. G. Sankar, and J. P. Liu, Adv. Mater. 23, 821 (2011).

[8] S. Fähler, U. K. Rößler, O. Kastner, J. Eckert, G. Eggeler, H. Emmerich, P. Entel, S. Müller, E. Quandt, and K. Albe, Adv. Eng. Mater. 14, 10 (2012).

[9] T. Burkert, L. Nordström, O. Eriksson, and O. Heinonen, Phys. Rev. Lett. 93, 027203 (2004).

[10] G. Andersson, T. Burkert, P. Warnicke, M. Björck, B. Sanyal, C. Chacon, C. Zlotea, L. Nordström, P. Nordblad, and O. Eriksson, Phys. Rev. Lett. 96, 037205 (2006).

[11] Y. Kota and A. Sakuma, Appl. Phys. Express 5, 113002 (2012).

[12] I. Turek, J. Kudrnovský, and K. Carva, Phys. Rev. B 86, 174430 (2012).

[13] E. K. Delczeg-Czirjak, A. Edström, M. Werwiński, J. Rusz, N. V. Skorodumova, L. Vitos, and O. Eriksson, Phys. Rev. B 89, 144403 (2014).

[14] L. Reichel, G. Giannopoulos, S. Kauffmann-Weiss, M. Hoffmann, D. Pohl, A. Edström, S. Oswald, D. Niarchos, J. Rusz, L. Schultz, and S. Fähler, J. Appl. Phys. 116, 213901 (2014).

[15] L. Reichel, L. Schultz, D. Pohl, S. Oswald, S. Fähler, M. Werwiński, A. Edström, E. K. Delczeg-Czirjak, and J. Rusz, J. Phys.: Condens. Matter 27, 476002 (2015).

[16] M. D. Kuz'min, K. P. Skokov, H. Jian, I. Radulov, and O. Gutfleisch, J. Phys.: Condens. Matter 26, 064205 (2014).

[17] K. D. Belashchenko, L. Ke, M. Däne, L. X. Benedict, T. N. Lamichhane, V. Taufour, A. Jesche, S. L. Bud'ko, P. C. Canfield, and V. P. Antropov, Appl. Phys. Lett. 106, 062408 (2015).

[18] M. Däne, S. K. Kim, M. P. Surh, D. Åberg, and L. X. Benedict, J. Phys.: Condens. Matter 27, 266002 (2015).

[19] A. Edström, M. Werwiński, D. Iuşan, J. Rusz, O. Eriksson, K. P. Skokov, I. A. Radulov, S. Ener, M. D. Kuz'min, J. Hong, M. Fries, D. Y. Karpenkov, O. Gutfleisch, P. Toson, and J. Fidler, Phys. Rev. B 92, 174413 (2015).

[20] W. Wallisch, J. Fidler, P. Toson, H. Sassik, R. Svagera, and J. Bernardi, J. Alloys Compd. 644, 199 (2015).

[21] A. Iga, Jpn. J. Appl. Phys. 9, 415 (1970).

[22] I. A. Zhuravlev, V. P. Antropov, and K. D. Belashchenko, Phys. Rev. Lett. 115, 217201 (2015).

[23] M. A. McGuire and D. S. Parker, J. Appl. Phys. 118, 163903 (2015).

[24] M. Werwiński, S. Kontos, K. Gunnarsson, P. Svedlindh, J. Cedervall, V. Höglin, M. Sahlberg, A. Edström, O. Eriksson, and J. Rusz, Phys. Rev. B 93, 174412 (2016).

[25] J. Cedervall, S. Kontos, T. C. Hansen, O. Balmes, F. J. Martinez- Casado, Z. Matej, P. Beran, P. Svedlindh, K. Gunnarsson, and M. Sahlberg, J. Solid State Chem. 235, 113 (2016).

[26] T. N. Lamichhane, V. Taufour, S. Thimmaiah, D. S. Parker, S. L. Bud'ko, and P. C. Canfield, J. Magn. Magn. Mater. 401, 525 (2016).

[27] D. Hedlund, J. Cedervall, A. Edström, M. Werwiński, S. Kontos, O. Eriksson, J. Rusz, P. Svedlindh, M. Sahlberg, and K. Gunnarsson, Phys. Rev. B 96, 094433 (2017).

[28] J. Cedervall, E. Nonnet, D. Hedlund, L. Häggström, T. Eric- sson, M. Werwiński, A. Edström, J. Rusz, P. Svedlindh, K. Gunnarsson, and M. Sahlberg, Inorg. Chem. 57, 777 (2018).

[29] S. Rundqvist, Acta Chem. Scand. 16, 1 (1962).

[30] B. Lejeune, R. Barua, I. McDonald, A. Gabay, L. Lewis, and G. Hadjipanayis, J. Alloys Compd. 731, 995 (2018).

[31] K. Koepernik and H. Eschrig, Phys. Rev. B 59, 1743 (1999).

[32] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[33] P. E. Blöchl, O. Jepsen, and O. K. Andersen, Phys. Rev. B 49, 16223 (1994).

[34] K. Schwarz and P. Mohn, J. Phys. F 14, L129 (1984).

[35] A. Edström, Phys. Rev. B 96, 064422 (2017).

[36] S. Steiner, S. Khmelevskyi, M. Marsmann, and G. Kresse, Phys. Rev. B 93, 224425 (2016).

[37] K. Koepernik, B. Velický, R. Hayn, and H. Eschrig, Phys. Rev. B 55, 5717 (1997).

[38] B. L. Gyorffy, A. J. Pindor, J. Staunton, G. M. Stocks, and H. Winter, J. Phys. F 15, 1337 (1985).

[39] K. Sato, P. H. Dederics, and H. Katayama-Yoshida, Europhys. Lett. 61, 403 (2003).

[40] J. Kudrnovský, I. Turek, V. Drchal, F. Máca, P. Weinberger, and P. Bruno, Phys. Rev. B 69, 115208 (2004).

[41] V. Heine, J. H. Samson, and C. M. M. Nex, J. Phys. F 11, 2645 (1981).

[42] P. Soven, Phys. Rev. 156, 809 (1967).

[43] J. P. Perdew and Y. Wang, Phys. Rev. B 45, 13244 (1992).

[44] K. Momma and F. Izumi, J. Appl. Crystallogr. 41, 653 (2008).

[45] B. Carlsson, M. Gölin, and S. Rundqvist, J. Solid State Chem. 8, 57 (1973).

[46] J. Rodríguez-Carvajal, Phys. B (Amsterdam, Neth.) 192, 55 (1993).

[47] H. Rietveld, J. Appl. Crystallogr. 2, 65 (1969).

[48] T. J. B. Holland and S. A. T. Redfern, Mineral. Mag. 61, 65 (1997).

[49] S. Chikazumi, C. D. Graham, and S. Chikazumi, Physics of Ferromagnetism, 2nd ed., International Series of Monographs on Physics, Vol. 94 (Clarendon Press, Oxford, 1997).

[50] S. V. Andreev, M. I. Bartashevich, V. I. Pushkarsky, V. N. Maltsev, L. A. Pamyatnykh, E. N. Tarasov, N. V. Kudrevatykh, and T. Goto, J. Alloys Compd. 260, 196 (1997).

[51] H. Zhang, D. Zeng, and Z. Liu, J. Magn. Magn. Mater. 322, 2375 (2010).

[52] W. F. Brown, Phys. Rev. 58, 736 (1940).

[53] P. Haas, F. Tran, and P. Blaha, Phys. Rev. B 79, 085104 (2009).

[54] M. Ropo, K. Kokko, and L. Vitos, Phys. Rev. B 77, 195445 (2008).

[55] M. Zelený, D. Legut, and M. Šob, Phys. Rev. B 78, 224105 (2008).

[56] L. Häggström, R. Wäppling, T. Ericsson, Y. Andersson, and S. Rundqvist, J. Solid State Chem. 13, 84 (1975).

[57] C. T. Chen, Y. U. Idzerda, H.-J. Lin, N. V. Smith, G. Meigs, E. Chaban, G. H. Ho, E. Pellegrin, and F. Sette, Phys. Rev. Lett. 75, 152 (1995).

[58] R. A. Reck and D. L. Fry, Phys. Rev. 184, 492 (1969).

[59] R. M. Moon, Phys. Rev. 136, A195 (1964).

[60] E. Şaşıoğlu, L. M. Sandratskii, and P. Bruno, J. Appl. Phys. 98, 063523 (2005).

[61] J. Rusz, I. Turek, and M. Diviš, Phys. Rev. B 71, 174408 (2005).

[62] J. M. Ziman, Contemp. Phys. 4, 81 (1962).

[63] A. I. Liechtenstein, M. I. Katsnelson, V. P. Antropov, and V. A. Gubanov, J. Magn. Magn. Mater. 67, 65 (1987).

[64] X. Wang, D.-S. Wang, R. Wu, and A. J. Freeman, J. Magn. Magn. Mater. 159, 337 (1996).

[65] R. Wu and A. J. Freeman, J. Magn. Magn. Mater. 200, 498 (1999).

[66] M. Werwiński and W. Marciniak, J. Phys. D: Appl. Phys. 50, 495008 (2017).

[67] I. Khan and J. Hong, Curr. Appl. Phys. 18, 526 (2018).

[68] S. Ayaz Khan, P. Blaha, H. Ebert, J. Minár, and O. Šipr, Phys. Rev. B 94, 144436 (2016).

[69] A. Edström, Theoretical and computational studies on the physics of applied magnetism: Magnetocrystalline anisotropy of transition metal magnets and magnetic effects in elastic electron scattering, Ph.D. thesis, Uppsala University, 2016.

[70] H. Akai, Hyperfine Interact. 43, 253 (1988).

[71] P. H. Dederichs, R. Zeller, H. Akai, and H. Ebert, J. Magn. Magn. Mater. 100, 241 (1991).

[72] R. Wienke, G. Schütz, and H. Ebert, J. Appl. Phys. 69, 6147 (1991).