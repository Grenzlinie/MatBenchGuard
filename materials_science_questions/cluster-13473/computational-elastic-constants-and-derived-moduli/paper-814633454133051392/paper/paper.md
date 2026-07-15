# Correlation of structure and mechanical response in solid-like polymers

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2015 J. Phys.: Condens. Matter 27 194131

(http://iopscience.iop.org/0953-8984/27/19/194131)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 194.27.18.18
This content was downloaded on 06/05/2015 at 02:14

Please note that terms and conditions apply.

# Correlation of structure and mechanical response in solid-like polymers

Sara Jabbari-Farouji¹, Joerg Rottler², Olivier Lame³, Ali Makke⁴,
Michel Perez³ and Jean-Louis Barrat¹,⁵

¹ Université Grenoble Alpes, UJF Liphy, F38041 Grenoble, France
² Department of Physics and Astronomy, The University of British Columbia, 6224 Agricultural Road, Vancouver, BC V6T 1Z1, Canada
³ INSA Lyon, MATEIS, UMR CNRS 5510, Université de Lyon, F69621 Villeurbanne, France
⁴ EPF école d'ingénieur, Institut Charles Delaunay, LASMIS UMR CNRS 6279, F10004 Troyes, France
⁵ Institut Laue-Langevin, 6 rue Jules Horowitz, BP 156, F-38042 Grenoble, France

E-mail: sara.jabbari@gmail.com

Received 27 October 2014, revised 26 January 2015
Accepted for publication 23 February 2015
Published 29 April 2015

![](./images/814633454133051392_1.jpg)

## Abstract
Employing large scale molecular dynamics simulations, we measure the uniaxial tensile response of amorphous and semicrystalline states of a coarse-grained PVA bead-spring model. The response beyond the elastic limit encompasses strain-softening and strain-hardening regimes. To understand the underlying mechanisms of plastic deformation, we analyse conformational and structural changes of polymers. In particular, we characterise the volume distribution of crystalline domains along the stress–strain curve. The strain-softening regime in semicrystalline samples is dominated by deformation of crystalline parts, while strain-hardening involves unfolding and alignment of chains in both amorphous and crystalline parts. Comparing the tensile response of semicrystalline and amorphous polymers, we find similar conformations of polymers for both systems in the strain-hardening regime.

Keywords: semicrystalline polymers, amorphous polymers, plastic deformation, molecular dynamics

(Some figures may appear in colour only in the online journal)

---

## 1. Introduction
Polymeric materials have a wide range of applications from packaging to more high-performance products such as bullet resistant vests and helmets. What makes them attractive for various applications are their special mechanical properties. They deform elastically for relatively large amounts of deformation before they exhibit plastic flow. Into the plastic flow, right after the elastic limit, the true stress usually decreases with an increase in the strain, defining the strain-softening region. Beyond this regime, further increase of strain leads to a huge rise in stress before failure and this effect is known as strain-hardening. A more efficient exploitation of these particular mechanical properties of polymers calls for a deeper understanding of the mechanisms of deformation and in particular the link between underlying microstructure and the resulting mechanical response.

Solid-like polymers are found in amorphous or semi-crystalline states. Performing a rapid thermal quench, polymers form glassy disordered states. For slow enough cooling rates, polymers with regular side chains form partially crystalline structures that consist of stacking chain folded lamellae (crystallites) and amorphous regions [1,2]. Even for the slowest cooling rates, perfect ordering of crystallisable polymers is hindered due to the connectivity and entanglement of the long chain molecules which impose topological constraints. Instead, we obtain semicrystalline polymers which are formed at higher temperatures compared to their glassy counterparts and, at similar temperatures, they are usually stiffer. The enhanced stiffness finds its origin in the underlying microstructural configurations of polymers, i.e. in the presence of crystalline domains.

Deformation mechanisms in the plastic regime of flow of amorphous polymers (either rubbery or glassy) have been

widely investigated and are rather well understood [3–7]. However, the underlying mechanism of deformation in their semicrystalline counterparts is still a matter of debate [8–10]. It is not clear how crystalline domains are modified under deformation at the scale of a few crystallites. It has been suggested that yielding of semicrystalline polymers is controlled by nucleation and motion of screw dislocations [11]. However, experimental evidence indicates that in addition to dislocations, the density of stress transmitters also plays a part in the yield stress [12].

Based on experimental data the following scenario for the sequence of events during plastic deformation of semicrystalline polymers has been proposed [13]: (i) elongation of amorphous parts, (ii) yielding of crystallites that can result from shearing of crystallites, buckling of both parts or cavitation of amorphous parts, (iii) tilting of lamellae towards the tensile axis and separation of crystalline block segments, (iv) stretching of crystallites and amorphous regions along the tensile axis. Because of the small length scales involved, there is no direct visualisation of plastic events during deformation of polymers and only a few simulation studies exist [14, 15].

Our aim is to fill this gap by molecular dynamics simulations of semicrystalline polymers and by analysing the evolution of polymer conformations and crystalline domains along the stress–strain curve. To this end, we perform large- scale molecular dynamics simulations of a coarse-grained model for semiflexible polymers of polyvinyl alcohol (CG- PVA) [16]. Crystallization and melting in this model have been studied for various chain lengths $10 \leqslant N \leqslant 1000$ [16, 17, 19–21] where $N$ is the number of monomers. For very short chains $N < 50$, full crystallisation is achieved, while longer chains form chain-folded structures for slow enough cooling rates. Here, we choose to work with PVA polymers of size $N = 300$ which encompass few stem lengths (about 30 monomers) in the semicrystalline phase. Furthermore, they are already in the weakly entangled regime.

Starting from equilibrated polymer melts via tuning the cooling rate, we obtain both glassy and semicrystalline states. These simulations allow us to obtain direct information about conformational changes of polymers upon deformation as briefly reported in [23]. Here, we provide a more detailed analysis of structural correlations upon deformation to gain an insight into the local mechanisms of plastic events. In particular, we address two key questions: (i) How do ordered and amorphous regions transform under uniaxial tension in semicrystalline polymers? (ii) How does the mechanical response of semicrystalline polymers differ from their amorphous counterparts?

To analyse the evolution of polymer conformations and crystalline domains along the stress–strain curve, we introduce appropriate tools for analysis of configurations of crystalline and amorphous regions. In particular, we develop a cluster- analysis algorithm to find the volume distribution of crystalline domains and we obtain the evolution of crystallinity and global nematic order parameter as a function of deformation. We also compute the pair distribution functions in each of the ordered and disordered regions. We demonstrate that plastic deformation in a semicrystalline model of polymers involves tilting of crystallites and breakage of the largest crystalline blocks in the strain-softening regime followed by stretching and alignment of both amorphous and folded chains in the strain-hardening regime.

## 2. Methods
In the CG-PVA bead-spring model, monomers are connected by harmonic bonds and, additionally, interact via an angular bending potential which retains semiflexibility of chains originated from torsional states of the atomistic backbone [16]. The non-bonded interactions are approximated by a 6–9 Lennard-Jones potential. The length unit is reported as $\sigma = 0.52$ nm and the bond length is $b_0 = 0.5\sigma$. The range and strength of the 6–9 Lennard-Jones potential are given by $\sigma_{\text{LJ}} = 0.89\sigma$ and $\epsilon_{\text{LJ}} = 1.511\, k_{\text{B}}T_0$ where $T_0 = 550$ K is the reference temperature of the PVA melt [16]. The Lennard- Jones potential is truncated and shifted at $r_{\text{LJ}}^{\text{C}} = 1.6\sigma$ unless stated otherwise. The time unit from the conversion relation of units is $\tau = 1.31$ ps. The temperatures and pressures are reported in reduced units $T = T_{\text{real}}/T_0$ and $P = P_{\text{real}}\sigma^3/\epsilon_0$. We apply periodic boundary conditions and NPT ensemble using a Berendsen barostat ($P = 8$, in reduced units) and Nose–Hoover thermostat. The time step used through all our simulations is $0.005\tau$.

We use a LAMMPS molecular dynamics (MD) code [18] to perform large-scale simulations of systems of 3600 chains of 300 monomers obtained from replications of smaller samples of 300 chains with the same size. The equilibrated melt configurations of 300 chains were obtained by $3.75 \times 10^8$ MD steps of equilibration. We perform continuous cooling from the equilibrated melts with density $\rho_{\text{mon}}\sigma^3 = 2.35$ at $T = 1$ to the desired temperature at cooling rates in the range $2 \times 10^{-7} - 10^{-3}\, \tau^{-1}$ which allow us to obtain semicrystalline and glassy states. The choice of cutoff in our simulations is different from the original CG-PVA model [16] where only the repulsive interactions are included $r_{\text{LJ}}^{\text{C}} = 1.01\sigma$, although we have used the same pressure ($P = 8$). As a result, the density of our samples is higher than the structures obtained with smaller cutoff [16]. Likewise, the onset of crystallisation obtained by a slow cooling rate $\dot{T} = 10^{-6}\tau^{-1}$ in our simulations is higher (0.9) than the semicrystalline polymers obtained with the same $\dot{T}$ without attractive potential (0.78 in [17]).

To characterise the crystallites, we use the notion of *crystalline domains* which are defined as a set of spatially connected regions with the same orientation [22]. To identify the crystalline domains, we divide the box into cells of size about $2\sigma$ and we compute the nematic tensor $Q_{\alpha\beta} = 1/N \sum_i (3/2b'^i_{\alpha}b'^i_{\beta} - 1/2\delta_{\alpha\beta})$ of unit bond vectors of polymers $\widehat{b}^i$ within each cell. The largest eigenvalue and the corresponding eigenvector of the nematic tensor determine the order parameter $S$ and the preferred orientation of bonds, i.e. director $\widehat{n}$ in each cell. The volume fraction of cells with $S > 0.8$ defines the degree of *crystallinity* $X_{\text{C}}$. We perform a cluster analysis by merging two neighbouring cells if they are both crystalline and their directors share the same orientation within the threshold $\widehat{n} \cdot \widehat{n}' \geqslant 0.97$. We determine the volume

distribution of crystallites as a function of $V_{\text{domain}} = n v_{\text{cell}}$ where $n$ is the number of cells with volume $v_{\text{cell}}$ in a domain and we normalise it to the volume of the box $V$. Thus, we obtain $\frac{\mathrm{d}\Phi}{\mathrm{d}V} = \frac{n v_{\text{cell}} N(n)}{V \Delta n}$ where $N(n)$ is the number of domains which comprise between $n$ and $n + \Delta n$ crystalline cells. We define a volume-averaged volume fraction of crystalline domains as $\langle \Phi \rangle = \frac{1}{V} \frac{\sum_{n} n^{2} N(n)}{\sum_{n} n N(n)}$.

We perform a uniaxial tensile deformation in the $y$-direction with a constant true strain-rate of $10^{-5} \tau^{-1}$ and an imposed pressure of $P = 8$ (the same pressure as in the undeformed sample [16]) in the other two directions. To distinguish and quantify the deformation in crystalline and non-crystalline parts during deformation, we compute the pair distribution function $g(\rho, y)$ at different stages of deformation where $\rho = \sqrt{x^{2} + z^{2}}$ refers to separations in the direction perpendicular to the tensile axis. The $g(\rho, y)$ in crystalline regions is obtained as $g_{\text{crys}}(\rho, y) = \frac{1}{2 \pi \rho N_{\text{mon}} \rho_{\text{mon}} X_{C}} \sum_{i=1}^{N_{\text{mon}}^{\text{crys}}} \sum_{j \neq i}^{N_{\text{mon}}^{\text{crys}}} \langle \delta(\rho - \rho_{ij}) \delta(y - y_{ij}) \rangle$ where the sum is over all the monomers which lie in the crystalline regions and $\rho_{ij} = |\rho_{i} - \rho_{j}|$ and $y_{ij} = |y_{i} - y_{j}|$ refer to distances of two monomers $i$ and $j$ in the directions perpendicular and parallel to the tensile axis $y$. Likewise, the pair distribution function in amorphous regions is computed as $g_{\text{amorph}}(\rho, y) = \frac{1}{2 \pi \rho N_{\text{mon}} \rho_{\text{mon}} (1 - X_{C})} \sum_{i=1}^{N_{\text{mon}}^{\text{amorph}}} \sum_{j \neq i}^{N_{\text{mon}}^{\text{amorph}}} \langle \delta(\rho - \rho_{ij}) \delta(y - y_{ij}) \rangle$ where the sum is over all the monomers which lie in the amorphous regions. The binning size used for computation of pair distribution functions in each of $\rho$ and $y$ directions is $0.03\sigma$.

## 3. Results
### 3.1. Amorphous and semicrystalline PVA polymers

Starting from an equilibrated polymer melt with random coil conformation of polymers at $T = 1$ and adjusting the cooling rate, we obtain both semicrystalline and glassy samples. Figure 1 shows the volume per monomer as a function of temperature for 3600 polymer chains of length 300 obtained by a rapid quench $\dot{T} = 10^{-3} \tau^{-1}$ and a slow cooling rate $\dot{T} = 10^{-6} \tau^{-1}$ leading to semicrystalline and glassy states, respectively. We have shown the conformations of the polymers in each state (left) as well as the melt (right). Performing a rapid quench, we obtain a glass which has the same structure as the melt but a different mechanical response as will be discussed in the next subsection. The glass transition temperature $T_{g}$ is defined as the temperature at which the slope of the cooling curve changes and corresponds to $T_{g} \approx 0.58$. The semicrystalline samples obtained by a slower cooling rate consist of stacking chain folded lamellae and amorphous regions. We observe a rather abrupt drop of volume and change of slope of the $v-T$ curve at a certain temperature which can be attributed to a phase transformation, i.e. partial crystallization of polymers. This temperature $T_{\text{c}} \approx 0.9$ is a measure of the crystallisation temperature $T_{c}$. The instantaneous degree of crystallinity right after crystallization, $X_{C}$ as a function of temperature is presented in figure 2. We find that $X_{C}$ rises from 0.32 at $T = 0.85$ to about $X_{C} = 0.425$ at the lowest temperature $T = 0.2$. Hence, once the crystallisation takes place, $X_{C}$ is a weak function of temperature for $T < T_{\text{crys}}$.

![](./images/814633454133051392_2.jpg)

**Figure 1.** Volume per monomer as a function of reduced temperature $T$ for 3600 chains of length 300 obtained at a slow cooling rate $\dot{T} = 10^{-6} \tau^{-1}$ and a rapid quench $\dot{T} = 10^{-3} \tau^{-1}$ leading to semicrystalline and glassy states of polymers, respectively. The conformations of polymers in the melt (right), glassy and semicrystalline states (left) are also depicted.

To examine the effect of cooling rate on crystallinity, we made a systematic study of the crystallinity degree as a function of $\dot{T}$, as presented in figure 2(b). This plot shows that $X_{C}$ decreases continuously upon increase of the cooling rate. Thus, there is no evidence of a sharp transition between glassy and semicrystalline states upon varying cooling rate. However, for fast enough cooling rates, i.e. $\dot{T} > 5 \times 10^{-4}$, we find that $X_{C} < 0.01$ at all temperatures. Hence, the sample obtained at $\dot{T} = 10^{-3} \tau^{-1}$ is glassy and does not contain any crystallites.

In order to determine the entanglement length of undeformed samples, we perform a Primitive-Path Analysis (PPA) using the minimization approach [24]. We extract the entanglement length from the intrachain bond correlations $\langle \hat{b}^{i} . \hat{b}^{i+j} \rangle$ of the primitive path averaged over the whole system as twice its decay length [25]. We observe an increase of entanglement length from about 32 in the melt ($T = 1$) to about 36 for the glassy state obtained at a cooling rate of $10^{-3} \tau^{-1}$ at $T < T_{g}$. The increase of $N_{e}$ in the glassy phase is most likely due to a decrease of thermal fluctuations. For the semicrystalline phase obtained at a cooling rate $10^{-6} \tau^{-1}$, the entanglement length averaged over both crystalline and amorphous parts increased to around 44 at the lowest temperatures ($T = 0.2$). Therefore, PVA polymers of size $N = 300$ encompass about 8–9 entanglement lengths.

### 3.2. Tensile-deformation response

Having provided an overview of amorphous and semicrys- talline polymers of the PVA model, we turn to their mechan- ical response under uniaxial tension. Figures 3(a) and (b) present the stress–strain curves for semicrystalline and amor- phous samples, respectively, obtained at different tempera- tures. In all the samples, we observe an elastic regime of deformation at very small deformations $\epsilon_{yy} < 0.1$. At slightly higher strains, yielding occurs and we enter the plastic flow region. Following yield, the low temperature samples exhibit an overshoot and a reduction in stress which is known as strain- softening. At higher strains the stress increases again and we enter into the strain-hardening regime. The yield stress, associ- ated with overcoming the barrier to rearrangements of polymer

![](./images/814633454133051392_3.jpg)

Figure 2. (a) Crystallinity as a function of temperature for 3600 chains of length 300 obtained at a slow cooling rate $10^{-6}\tau^{-1}$. (b) Cooling rate dependence of $X_{\rm C}$ at different temperatures.

![](./images/814633454133051392_4.jpg)

Figure 3. Uniaxial tension tests for polymeric systems of 3600 chains of length 300: stress–strain curves obtained at different temperatures (a) for a semicrystalline samples obtained by a continuous cooling rate $10^{-6}\tau^{-1}$ and (b) amorphous samples obtained by a cooling rate $10^{-3}\tau^{-1}$. Here, $\epsilon/\sigma^{3}\approx54$ MPa.

configurations, increases by lowering the temperature in both amorphous and semicrystalline samples.

We have extracted Young's modulus $E$ from the linear (elastic) regime of response and the strain-hardening modulus $G_{\rm H}$ from the initial slope of stress versus $g(\lambda)=\lambda^{2}-\lambda^{-1}$, with $\lambda=L_{y}/L_{y}^{0}$ being the draw ratio, in the strain-hardening regime. Figures 4(a) and (b) show $E$ and $G_{\rm H}$ as a function of temperature for semicrystalline and amorphous samples, respectively. The Young's modulus $E$ is larger in the semicrystalline samples compared to their amorphous counterparts at the same temperature. By contrast, the strain-hardening modulus $G_{\rm H}$ is lower in semicrystalline polymers compared to the amorphous ones.

$E$ and $G_{\rm H}$ increase with decrease of temperature in both semicrystalline and amorphous polymers. For semicrystalline polymers, $E$ and $G_{\rm H}$ drop linearly with increase of temperature. In contrast, $E$ and $G_{\rm H}$ do not vary linearly with temperature in the amorphous samples, especially in the glassy range of temperatures. This trend is different from the linear drop of $G_{\rm H}$ with temperature observed for the FENE bead-spring model with cosine angular bending stiffness [6]. Moreover, the increase of $E$ with decrease of $T$ is a softer function of temperature in comparison with polymers of the FENE model where a scaling relation of generic Kremer-Grest-like models $E=A(T_{g}-T)^{\gamma}$ has been found [26]. This behaviour is most likely due to the softer nature of 6–9 Lennard-Jones potential.

In the following, we will focus on understanding the underlying mechanisms of deformation in the plastic regime of flow beyond the yield point, i.e. the strain-softening and strain-hardening regimes. To this end, we investigate conformational changes of polymers at the single chain level as well as large-scale structural evolution of the samples.

### 3.3. Conformational and structural changes of polymers

Figure 5 shows conformations of semicrystalline and glassy polymers at different stages of plastic deformation. We notice that concomitant with stretching of the box in the tensile direction, the samples shrink in the perpendicular directions. The volume increase is at most 6% for the semicrystalline polymers at lowest temperature $T=0.2$ while for the amorphous polymers, the volume increase is less than 2% at all $T$. Therefore, PVA polymers behave nearly as an incompressible fluid.

At strains beyond the yield point, the chain-folded structures of semicrystalline polymers in figure 5(a) align partially in the direction of tensile stress. At larger deformations in the strain-hardening regime, chains in crystalline domains are unfolded as a result of tensile stress and both chains in amorphous and crystalline domains are stretched and aligned. The changes in conformations of glassy polymers are shown in figure 5(b). Upon increase of deformation glassy polymers get more and more stretched and aligned along the tensile axis.

![](./images/814633454133051392_5.jpg)

Figure 4. (a) Young's modulus $E$ and (b) strain-hardening modulus $G_{\text{H}}$ extracted from stress-strain curves for semicrystalline and glassy polymers in figure 3 as a function of $T$. Here, $\epsilon/\sigma^{3} \approx 54$ MPa.

![](./images/814633454133051392_6.jpg)

Figure 5. Snapshots of polymer configurations of (a) semicrystalline polymers and (b) glassy polymers at $T=0.2$ at different stages of deformation.

![](./images/814633454133051392_7.jpg)

Figure 6. The evolution of intrachain bond correlations $\langle \hat{b}^{i}.\hat{b}^{i+j} \rangle$ of (a) a semicrystalline sample of $T=0.2$, (b) rubbery polymers at $T=0.7$ and (c) glassy polymers at $T=0.2$ at different stages of deformation. The corresponding strain values are shown in the legends.

To quantify the conformational changes of polymers at single chain level, we compute the intrachain bond correlations defined as the ensemble-averaged correlation between the unit bond vectors $\hat{b}^{i}$ along the chains, i.e. $\langle \hat{b}^{i}.\hat{b}^{i+j} \rangle$. In an amorphous sample (melt, rubbery or glassy) the intrachain bond correlation function decays exponentially and its decay length gives us an estimate of the persistence length of the polymers. In the semicrystalline samples, the chain-folded conformation of polymers gives rise to a minimum with negative value in the intrachain correlation function. The position of this minimum provides us with the average stem length. In the case that there exist many uncrystallised chains, which have a zero contribution to the bond correlation, the depth of $\langle \hat{b}^{i}.\hat{b}^{i+j} \rangle$ is an indicator of the crystallinity degree.

Figure 6 presents the intrachain bond correlation functions at different stages of deformation for rubbery (figure 6(a)), glassy (figure 6(b)) and semicrystalline polymers (figure 6(c)). In the amorphous samples, the decay length of the intrachain bond correlations increases with deformation, demonstrating the stretching of the polymers as a result of tensile deformation. In semicrystalline polymers as shown in figure 6(c), upon increase of deformation, the depth of the minimum gradually

![](./images/814633454133051392_8.jpg)

Figure 7. The evolution of pair distribution functions $g(\rho, 0)$ and $g(0, y)$ in crystalline and amorphous parts of a semicrystalline sample of $T=0.2$ obtained with $\dot{T}=10^{-6} \tau^{-1}$ at different stages of deformation.

decreases in the strain-softening regime and finally it disappears in the strain-hardening regime where the chains are unfolded and stretched.

It still remains unclear how each of the amorphous and crystalline regions deform at various stages of deformation. To quantify and separate the deformation into ordered and disordered parts of semicrystalline polymers during deformation, we compute the pair distribution function of monomer positions $g(\rho, y)$ in the directions perpendicular $\rho$ and parallel $y$ to the tensile deformation in each region, i.e. $g_{\text {cry }}(\rho, y)$ and $g_{\text {amorph }}(\rho, y)$, as defined in section 2.

Figure 7 shows $g(\rho, 0)$ and $g(0, y)$ in both crystalline and amorphous regions at several strain values for a semicrystalline sample at $T=0.2$. The overall evolution of $g(\rho, 0)$ and $g(0, y)$ in the ordered regions of deformed samples shows that the initial 2D long-range order of the hexagonal crystalline lattice [17] is gradually destroyed. Instead, a new 1D longrange order develops as a result of chain alignment along the tensile axis, which we refer to as strain-induced crystallisation. To understand better the structural changes in each of the ordered and disordered regions, we investigate in detail the evolution of first and second peaks in $g(0, y)$ and $g(\rho, 0)$.

The first peak in $g(\rho, 0)$ and $g(0, y)$ is associated with the covalent bonds and its position describes the average bond length for the segments which are perpendicular and parallel to the tensile axis. Its value, more precisely the integral over the first peak, is proportional to the average number of covalent bonds which are perpendicular and parallel to the tensile axis, respectively. As can be seen from figure 7, the position of the first peak in all $g(\rho, 0)$ and $g(0, y)$ is constant, hence the average length of covalent bonds in either direction does not change. However, the relative population of bonds in each direction (perpendicular or parallel) with respect to the undeformed sample changes. The relative population of covalent bonds is proportional to value of the first peak normalised to its value for the undeformed sample.

In figure 8(a), we have plotted the normalised value of the first peak for each of $g(\rho, 0)$ and $g(0, y)$ in amorphous and crystalline parts as a function of strain. The fraction of bonds in the direction perpendicular to the tensile axis decreases for both crystalline and amorphous regions while the relative population of bonds along the tensile axis increases upon increase of deformation. In the strain-softening regime, the relative increase of covalent bonds along the tensile axis is dominated by the crystalline parts. In the strain-hardening regime, the population of covalent bonds in ordered parts does not change anymore while the population of covalent bonds in the disordered part keeps on increasing. These observations demonstrate that upon increase of tensile deformation a larger fraction of bonds are aligned along the tensile axis.

The second peak in $g(\rho, 0)$ and $g(0, y)$ is associated with the second nearest neighbour separations in perpendicular and parallel directions. Its position gives us the average nearest neighbour distance between two non-bonded monomers which can be in the same chain (interacting via angular potential) or in two different chains (interacting via Lennard-Jones potential).

![](./images/814633454133051392_9.jpg)

Figure 8. The evolution of (a) values of first peaks of $g(\rho,0)$ and $g(0,y)$, associated with covalent bonds, normalised to their corresponding values for undeformed samples. (b) The positions of second peaks of $g(\rho,0)$, associated with the second nearest neighbour separation.

![](./images/814633454133051392_10.jpg)

Figure 9. Snapshots of distribution of crystalline domains in a semicrystalline sample at $T=0.2$ at $\epsilon_{yy}=0$, 0.5 and 1.6 and the corresponding volume distribution functions.

Figure $8(b)$ shows the evolution in the position of the second peak of $g(\rho,0)$ in crystalline and amorphous regions normalised to their corresponding values in the undeformed samples. For strains $\epsilon_{yy}<0.8$, the non-bonded average perpendicular separation in the crystalline parts decreases while the corresponding separation in the amorphous part remains almost constant. At $\epsilon_{yy}\approx0.8$, as a result of further compression in the perpendicular direction, the non-bonded nearest neighbour distance in the amorphous parts also decreases. For larger deformations corresponding to the strain-hardening regime, the positions of the second peaks of $g(\rho,0)$ do not vary anymore. This observed trend in combination with the evidence of a larger increase of the bond population parallel to the tensile axis in crystalline parts indicates that the strain-softening regime is dominated by deformation of crystalline regions.

### 3.4. Evolution of crystalline domains and strain-induced crystallisation

Having investigated the intrachain and interchain structural changes, we next examine the evolution of crystalline domains under tensile deformation in the semicrystalline polymers and strain-induced crystallisation in amorphous polymers. For this purpose, we characterise the volume fraction distribution of crystalline domains $\mathrm{d}\Phi/\mathrm{d}V$ (figure 9), crystallinity (figure $10(a)$), average volume fraction $\langle\Phi\rangle$ (figure $10(b)$) and global nematic order parameter $S_{\text{global}}$ as a function of strain (figure $11(a)$).

Figure 9 presents the snapshots of crystalline domains obtained by our cluster analysis algorithm as explained in section 2 accompanied by the volume distribution function of crystallites at different stages of deformation. For an undeformed semicrystalline polymer, the volume distribution function consists of a majority of small crystalline domains whose distribution has a power law form for $V_{\text{domain}}<100$. For larger domain sizes, the volume distribution function decays less rapidly than a power law and these large crystalline domains have a major contribution to the crystallinity. We notice that the orientations of crystalline domains are isotropically distributed at $\epsilon_{yy}=0$.

Upon increase of deformation beyond the yield point, in the strain-softening (stress plateau for $T=0.7$) regime, the volume distribution of crystalline domains evolves as

![](./images/814633454133051392_11.jpg)

Figure 10. (a) The evolution of crystallinity $X_C$. (b) Average volume fraction of crystallites as a function of uniaxial strain.

![](./images/814633454133051392_12.jpg)

Figure 11. (a) The evolution of nematic order parameter. (b) Microscopic stretch $\lambda_{\text{eff}} \equiv R_y/R_y^0$ versus macroscopic stretch $\lambda \equiv L_y/L_y^0$.

can be observed from the second snapshot for $\epsilon_{yy} = 0.5$ in figure 9. An inspection of $\frac{d\Phi}{dV}$ at this regime indicates that the volume fraction of intermediate and large crystalline domains decreases and that of the smaller ones increases. This implies fragmentation of some of the larger crystalline domains that leads to a partial loss of crystallinity as evidenced by figure 10(a). The average volume fraction of crystalline domains $\langle \Phi \rangle$, as presented in figure 10(b), is almost constant at $T = 0.7 > T_g$ and corresponds to the stress plateau in figure 2(a) while at $T = 0.2 < T_g$, $\langle \Phi \rangle$ shows a slight decrease in the strain-softening regime. As can be observed from the snapshot of crystalline domains at $\epsilon_{yy} = 0.5$ a slight degree of anisotropy develops as a result of tensile deformation. The partial rotation of crystalline domains in this regime is verified by a rapid rise of the global nematic order parameter $S_{\text{global}}$ in figure 11(a) which signifies reorientation of a fraction of polymer bonds.

At larger deformations, in the strain-hardening regime, the majority of the chains are aligned since $S_{\text{global}} > 0.5$ as can be noticed from figure 11. Notably, the volume distribution of crystalline domains in figure 9 changes dramatically at such high strains. $\mathrm{d}\Phi/\mathrm{d}V$ comprises a set of small domains and a large domain of aligned chains. This regime is delineated by the onset of an increase in $X_C$ in figure 10(a) although crystallinity is due to alignment of chains rather than the original crystalline network of chain-folded structures. Indeed, in this regime, the chains are unfolded and stretched. The large $X_C$ observed at large strains as a result of chain reorientation is called strain-induced crystallization [8] and it is independent of the original structure. This statement is verified by the large $X_C$ in figure 10(a) and a large $S_{\text{global}}$ in figure 11(a) observed for amorphous samples at high strains. We note that although the amorphous polymers lack any kind of order in the undeformed state and small deformations, upon increase of deformation crystallinity as well as average volume of crystalline domains in figure 10 grow. In fact, the crystallinity curves for semicrystalline and amorphous samples both at low and high temperatures become very similar. Hence, crystallisation at high strains is mainly because of strain-induced alignment and has the same origin in both amorphous and semicrystalline polymers.

Exploring the global nematic order parameter in rubbery and glassy polymers, we find that strain hardening occurs when chains align along the tensile axis and $S_{\text{global}} > 0.4$ in figure 11(a). However, glassy polymers at $T = 0.2$ show a markedly different tensile response from their amorphous counterparts at $T = 0.7$. We observe a strain softening regime similar to the semicrystalline polymers although the origin of yielding is different and results from overcoming free energy barriers [6,7]. In polymeric glasses it is shown that strain hardening is related to the work needed to reorient the chains along the tensile axis [6,7] while in the rubbery polymers strain hardening has an entropic origin. Interestingly, in rubbery polymers $X_C$ and $\langle \Phi \rangle$ grow linearly up to $\epsilon_{yy} \approx 1$, while in the glassy polymers, we observe a non-zero crystallinity only for $\epsilon_{yy} > 0.6$ which coincides with the onset of strain-hardening. This is presumably due to the fact that rubbers can rearrange more easily and hence align along the tensile axis with less strong deformation.

![](./images/814633454133051392_13.jpg)

Figure 12. Stress–strain curves for a semicrystalline sample prepared at a cooling rate $10^{-6}\tau^{-1}$ at two different values for the range of non-bonded Lennard-Jones interaction.

Our simulations also allow us to obtain the microscopic deformation and compare it to the macroscopic stretch. Therefore, we can test if the chains deform affinely under the tensile deformation. The microscopic chain stretch $\lambda_{\text{eff}}$ can be defined in terms of root mean-squared components of end-to-end vectors of chains $R_{\alpha}$ relative to their initial values $R_{\alpha}^{0}$ in undeformed samples [7]. For uniaxial tensile deformation in the $y$ direction $\lambda_{\text{eff}} \equiv R_{y}/R_{y}^{0}=(R_{x}^{0}/R_{x})^{2}=(R_{z}^{0}/R_{z})^{2}$, where the last two equalities are implied by volume conservation. If the chains were to deform affinely, then $\lambda_{\text{eff}} = \lambda \equiv L_{y}/L_{y}^{0}$. In figure 11, we have plotted the microscopic stretch as a function of macroscopic stretch $\lambda$ for semicrystalline and amorphous samples. Interestingly, the average microscopic stretching of the chains is very similar for all the samples, regardless of their structure and temperature. For small deformations up to $\lambda \approx 2$ ($\epsilon_{yy} \approx 0.7$) which spans the elastic and the strain-softening regimes, the microscopic and macroscopic stretching coincide. At larger deformations in the strain-hardening regime, we observe a deviation from the macroscopic stretch and the chains on the average deform sub-affinely.

### 3.5. Effect of range of Lennard-Jones potential

Our analysis of conformational, structural and crystalline domains shows that the plastic deformation in semicrystalline polymers of the CG-PVA model involves tilting of crystallites and separation of the larger crystalline blocks in the strain-softening regime followed by stretching and alignment of both amorphous and folded chains in the strain-hardening regime. Hence, in the early stages of plastic flow, deformation is dominated by crystalline parts rather than the amorphous regions. This observation suggests that the crystallites in the CG-PVA model are too soft. One possible way to increase the stiffness of crystallites is to increase the range of the Lennard-Jones potential to allow for more cohesion between monomers in crystalline regions. Thus, we performed some simulations with $r_{\text{LJ}}^{\text{C}} = 2.5$ and obtained the tensile response of semicrystalline polymers as depicted in figure 12. Increasing the range of attraction leads to elevation of yield stress and strain-hardening modulus. However, analysing the configurations of samples with a stronger attraction, we find that the underlying mechanism of deformation remains unaltered. The rise in yield stress and strain-hardening modulus can be explained by the increase of density of semicrystalline samples as a result of increase of range of attraction. The density of semicrystalline polymers obtained with $r_{\text{LJ}}^{\text{C}} = 2.5$ is $4\%$ higher than that of their counterparts obtained with $r_{\text{LJ}}^{\text{C}} = 1.6$.

## 4. Discussion and concluding remarks

By simulating a tensile test on semicrystalline and amorphous polymers of the CG-PVA model, we have demonstrated that it is possible to identify the conformational and structural changes of crystalline and amorphous parts of semicrystalline polymers. Moreover, we have compared their features to those of amorphous polymers at temperatures above and below the glass transition. The plastic deformation in semicrystalline polymers of the CG-PVA model involves tilting of crystallites and separation of the largest crystalline blocks in the strain-softening regime followed by stretching and alignment of both amorphous and folded chains in the strain-hardening regime.

Comparing our simulations with experiments on *real polymers*, we notice some differences because of limitations in simulations and the coarse-grained nature of the employed model. Indeed, to crystallise in an accessible number of MD steps, it is required to use a rapidly crystallisable model like CG-PVA. The reduced cooling rates in simulations correspond to $10^{8}\ \text{K}\ \text{s}^{-1} < \dot{T}_{\text{real}} < 4.2 \times 10^{11}\ \text{K}\ \text{s}^{-1}$ and are much faster than the most rapid cooling rates in experiments. The latter crystallise easily so that a high number of nuclei appear in a relatively small number of MD steps (extremely short real time). As a consequence we have obtained semicrystalline microstructures which are relatively far from the classical ones observed for real polymers. Nonetheless, it is remarkable that most of the results obtained are in qualitative agreement with the main features of semi-crystalline polymers.

The general form of the stress/strain curves as well as the increase of $E$ and $G_{\text{H}}$ with lowering temperature in semicrystalline and glassy polymers are consistent with experimental findings [27,28]. The strain-hardening is generally attributed to the alignment of polymer bonds in the amorphous parts and $G_{\text{H}}$ is assumed to increase with the

content of tie molecules [29, 30]. The probability to form tie molecules is a decreasing function of the average size of crystallites [31,32], which itself increases with crystallinity. As a result, $G_{\mathrm{H}}$ should decrease with the crystallinity, in agreement with the trend observed in our simulations [23].

In terms of microstructural evolution with deformation, this model accounts for the progressive fracture of the larger crystallites to obtain smaller ones. However, it seems that the model overestimates the amount of crystal formed during the tensile deformation both at $T=0.2$ and $T=0.7$, even if the mechanisms of melting/recrystallisation are evoked [33,34]. Again, this behaviour is due to the high ability of this model to produce new crystallites in a short time.

In contrast to some experimental evidence [13], our simulations suggest that the crystalline parts are deformed first and only at larger strains are the amorphous parts deformed. This is most likely because of the coarse-grained nature of the model which leads to formation of softer crystalline domains compared to real semicrystalline polymers. This imperfection could be remedied by a modification of the potential in the crystalline zone and will be investigated in the future.

Another important issue that merits further investigations is the effect of polymer length on their mechanical response, particularly in the crossover regime from unentangled polymers to the entangled ones. We have investigated both crystallisation and glass formation for chain lengths in the range $N=50-1000$. A study on the effect of polymer length on tensile response is in progress and it will be presented in a future work.

## Acknowledgments
We are grateful to H Meyer for providing the LAMMPS scripts and useful discussions. We also thank C Luo for the advice with Primitive Path Analysis. All of the computations presented in this paper were performed using the Froggy platform of the CIMENT infrastructure (https://ciment.ujf-grenoble.fr), which is supported by the Rhône-Alpes region (GRANT CPER07-13 CIRA) and the Equip@Meso project (reference ANR-10-EQPX-29-01) of the programme Investissements d'Avenir supervised by the Agence Nationale pour la Recherche. JLB is supported by Institut Universitaire de France and by grant ERC-2011- ADG20110209.

## References
[1] Keller A 1968 Rep. Prog. Phys. 31 623
[2] Strobl G 2009 Rev. Mod. Phys. 81 1287
[3] Treloar L R G 1975 The Physics of Rubber Elasticity (Oxford: Clarendon)
[4] Haward R N and Young R J 1997 The Physics of Glassy Polymers 2nd edn (London: Chapman and Hall)
[5] Strobl G 2007 The Physics of Polymers 3rd edn (Berlin: Springer)
[6] Hoy R S and Robbins M O 2006 J. Polym. Sci. B: Polym. Phys.44 3487
[7] Hoy R S and Robbins M O 2008 Phys. Rev. E 77 031801
[8] Bartczak Z and Galeski A 2010 Macromol. Symp. 294 67
[9] Oleinik E F, Rudnev S N and Salamatina O B 2007 Polym. Sci.A491302
[10] Men Y, Rieger J and Strobl G 2003 Phys. Rev. Lett. 91 095502
[11] Young R 1976 J. Phil. Mag. 30 86
[12] Humbert S, Lame O and Vigier G 2009 Polymer 50 3755
[13] Schultz J M 1974 Polymer Materials Science (EnglewoodCliffs, NJ: Prentice-Hall)
[14] Lee S and Rutledge G C 2011 Macromolecules 44 3096
[15] In't Veld P J, Hutter M and Rutledge G C 2006Macromolecules 39 439
[16] Meyer H and Müller-Plathe F 2001 J. Chem. Phys. 115 7807
[17] Meyer H and Müller-Plathe F 2002 Macromolecules 35 1241
[18] Plimpton S 1995 J. Comput. Phys. 117 1
[19] Luo C and Sommer J U 2009 Phys. Rev. Lett. 102 147801
[20] Luo C and Sommer J U 2011 Macromolecules 44 1523
[21] Luo C and Sommer J U 2014 Phys. Rev. Lett. 112 195702
[22] Luo C and Sommer J U 2010 J. Polym. Sci. B: Polym. Phys.48 2222
[23] Jabbari-Farouji S, Rottler J, Lame O, Makke A, Perez M andBarrat J L 2015 ACS Macro Lett. 4 147
[24] Everaers R, Sukumaran S K, Grest G S, Svaneborg C,Sivasubramanian A and Kremer K 2004 Science 303 823
[25] Foteinopoulou K, Karayiannis N C, Mavrantzas V G andKroger M 2006 Macromolecules 39 4207
[26] Schnell B, Meyer H, Fond C, Wittmer J P and Baschnagel2011 Eur. Phys. J. E 34 97
[27] Humbert S, Lame O, Segula R and Vigier G 2011 Polymer52 4899
[28] van Melick H G H, Govaert L E and Meijer H E H 2003Polymer 44 2493
[29] Bartczak Z 2005 Macromolecules 38 7702
[30] Makke A, Lame O, Perez M and Barrat J L 2012Macromolecules 45 8445
[31] Huang Y L and Brown N J 1988 Mater Sci. 23 3648
[32] Humbert S, Lame O, Chenal J M, Rochas C and Vigier G 2010Macromolecules 43 7212
[33] Butler M F, Donald A M, Bras W, Mant G R, Derbyshire G Eand Ryan A J 1995 Macromolecules 28 638
[34] Jiang Z et al 2010 Macromolecules 43 4727