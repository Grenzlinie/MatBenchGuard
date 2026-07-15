# TEMPERATURE AND STRAIN-RATE DEPENDENT PLASTIC DEFORMATION OF CARBON NANOTUBE

Chengyu Wei, Kyeongjae Cho, Department of Mechanical Engineering, Stanford University, California; Deepak Srivastava, NASA Ames Research Center, MST27A-1, Moffett Field, California

## ABSTRACT

In this work we use classical molecular dynamics to study strain rate and temperature dependent plasticity of carbon nanotube (CNT) under compressive strain. We focus on two types of defects: sp3 bond formation and bond rotation. Our simulation shows that thermal fluctuations help the strained CNT to overcome the local energy barrier to obtain plastic deformation. The yielding strain of a compressed CNT found to be strain-rate and temperature dependent, and low strain rate limit of the yielding strain is estimated to be less that 6%.

## INTRODUCTION

Carbon nanotubes (CNTs) are formed by wrapping a graphite plane around certain directions. Experimental and theoretical studies find that CNTs have unusual strength [1,2] because of the strong sp2 bonds leading to Young's modulus of 1TPa or higher. There are many studies on possible ways to use CNTs in nano-scale devices or as nano-fibers in composite materials [3-6]. For the applications it is important to understand how CNT respond to external mechanical loads and the mechanisms of formation of possible defects leading to plastic deformations. It is thus essential to understand the intrinsic mechanical properties of CNT at atomistic level. Previous atomistic simulations on this subject were generally conducted at zero temperature or without considering strain rate effect, while under real experimental conditions these factors can play important role. The subject we are interested in this work is the plastic deformation of CNTs at finite temperatures, and specifically the strain-rate and temperature dependant behavior of yielding strain of CNTs.

## SIMULATIONS

All the simulations in this work are conducted with Tersoff-Brenner interaction potential [7,8] for carbon atoms and with 0.5 fs time step in MD simulation.

### 1. Plastic deformation of CNT under compressive strain at finite temperatures

Previous simulations using classical molecular dynamics (MD) [9] and tight-binding (TB) [10] simulations have confirmed the high strength of CNTs. MD simulations found CNTs to be super-elastic up to strain as large as 15%, while in TB simulations CNTs collapse at 12 % strain with sp3 diamond-like bond formed at some sections of the nanotube. Both studies were conducted at zero temperature. In this work, we study how temperature dependent fluctuations can help CNTs to overcome possible energy barriers

AA6.5.1

![](./images/811669857652178947_1.jpg)

Figure 1: Radical distribution function (RDF) plots of plastic deformed CNT at various temperatures

![](./images/811669857652178947_2.jpg)

Figure 2: Strain energy of the compressed CNT as a function of relaxation time

from local minimum configurations to plastic deformations as discovered in TB simulations [10].

We chose a section of (8,0) CNT about 40 Å long with 12% uniform compressive strain, at which the CNT found to collapse in the TB simulations. With both ends of the CNT constrained, MD simulations were conducted at several temperatures T = 300K, 800K, 1200K and 1600K with simulation times up to 200ps. For a comparison, a simulation at T = 0K was also conducted.

AA6.5.2

At zero temperature "fins" structure is formed to release strain energy, in agreement with previous studies [7]. The RDFs of the relaxed configurations of the CNT at various temperatures are shown in Figure 1. The RDFs of the relaxed configurations starting from the collapsed structure of TB simulation are also plotted at the corresponding temperatures. From Figure 1, we can see that the peak around $1.3\ \mathrm{\mathring{A}}$, which represents the initial uniform compressive strain, disappears after "fins" structure is formed at zero temperature. This indicates that such elastic deformation helps release some of the strain energy, but at the same time the lack of any peaks from $1.5\ \mathrm{\mathring{A}}$ to $1.6\ \mathrm{\mathring{A}}$ indicates that no sp3 bonds are formed, in contrast to the TB simulation data. RDFs from classical MD at finite temperatures do show distributions around $1.5\ \mathrm{\mathring{A}}$ to $1.6\ \mathrm{\mathring{A}}$, suggesting that sp3 bonds are formed at finite temperatures, and the RDFs are quite similar to those of the collapsed structure starting from TB simulation structures.

The strain energies of the CNT as a function of the relaxation time at various temperatures are shown in Figure 2. Note that strain energies are released during the process of relaxation. For $\mathrm{T}=300\mathrm{K}$, $800\mathrm{K}$ and $1200\mathrm{K}$, after several pico seconds run, the strain energy of the system begin to be lower than the strain energy at zero temperature, which suggests that the strained CNT overcomes local energy barrier and reaches to more stable structures. The large vibrations at high temperatures can explain the relatively high strain energies of CNT at $1200\mathrm{K}$ and $1600\mathrm{K}$.

To understand whether any defects are formed during these relaxation processes at finite temperatures, we track the appearance of sp3 bond and bond rotation. The results are plotted in Figure 3 and Figure 4.

From Figure 3, we can see that for $\mathrm{T}=300\mathrm{K}$, sp3 bond begins to form after about $1\mathrm{ps}$. At higher temperature, the thermal activities apparently help such defects form at earlier time. Bond rotation also begins to happen at about $1\mathrm{ps}$ for $\mathrm{T}=300\mathrm{K}$ and has earlier appearance at higher temperature. Such "Stone-Wales" dislocation was found when CNT is under tensile stress at high temperature [11]. Different from the formation of sp3 bond where the average numbers of such defect are in same range (4-5) for various

![](./images/811669857652178947_3.jpg)

Figure 3: sp3 bond formation with relaxation

![](./images/811669857652178947_4.jpg)

Figure 4: bond rotation with relaxation

AA6.5.3

![](./images/811669857652178947_5.jpg)

Figure 5: Configurations of the compressed CNT with plastic deformations

temperatures after long MD run, bond rotations increase with temperature with much larger section of CNT involved at higher temperatures. The formation of sp3 bond in the strained CNT is in agreement of what is found in TB simulation. The "Stone-Wales" defect was not found in either classical MD or TB simulation, which were conducted at zero temperature.

In Figure 5, the configurations of the strained CNT with plastic deformation at several temperatures are plotted, where diamond-like sp3 bonds are formed at highly strained section of the compressed CNT. At temperature 1600K, "Stone-Wales" dislocations appear at the upper section of the CNT. At lower temperatures, cracks or large ring are also formed and they are originated from bond rotations.

The energy barriers between elastically strained structure of CNT and the collapsed ones in our simulations are estimated as about 0.15 to 0.9 eV, using Arrhenius formula: t = (1/ν) $exp(E\gamma/\text{kT})$, where t is relaxation time, $E\gamma$ is activation energy and ν is the vibration frequency of C-C bond.

### 2. Strain-rate and temperature dependent behavior of plastic deformations of CNT

The failure of a material is a dynamic process, which strongly depends on strain-rate and temperature. To understand the formation of defects on carbon nanotube under strain more thoroughly, it is import to consider such factors. In this section, we conducted a series of simulation on compression of CNT, applying various strain-rates and temperatures.

We chose a section of (10,0) CNT about 60 Å long. Compressive strain is applied at the two ends of the tube at a certain rate, ranged from 2%/ps to 0.0125%/ps, and the middle section of the tube is allowed to relax for a period of time, which depends on the strain-rate. The CNT is strained up to 15%. To capture the thermal-fluctuation effects, 6 sample sets were used for each data point. In Figure 6, the strain energies of the CNT as a function of compressive strain are plotted for T = 300K, 800K and 1600K at strain rate

AA6.5.4

![](./images/811669857652178947_6.jpg)

Figure 6: Strain energy of the compressed CNT as a function of strain, at different temperatures and strain rates

2%/ps, 0.1%/ps and 0.0125%/ps. It can be seen that the non-linear elastic behavior of the CNT begins to appear at strain 6% to 10%, depending on the strain rate and temperature. Slower strain rate or higher temperature leads to smaller strain at which CNT shows deviation from linear elastic behavior, accompanied by formation of "fins" structure. With the increase of thermal fluctuations and the appearance of non-uniform "fins" structures, higher local stress will be induced during the process of compressing the CNT and defects are expected to form. There are two possible defects, "Stone-Wales" bond rotation or sp3 bond formation as discussed in previous section. The relaxation time of defect formation can be described by Arrhenius formula:

$$
t=(1 / v) e^{U / k T}, \tag{1}
$$

where t is the relaxation time, v is the vibration frequency of C-C bond, $U$ is activation energy and $T$ is absolute temperature. Usually the formation of defects is much easier in a stressed material. For a first order approximation, $U$ can be considered to decrease linearly with the local stress or the local strain. The Arrhenius formula for a stressed material is then as following:

$$
t(\varepsilon)=(1 / v) e^{\frac{U_{0}-\alpha \varepsilon}{k T}}, \tag{2}
$$

where $\varepsilon$ is local strain and $\alpha$ is a parameter dependent on the activation volume and local force constants. Strain usually doesn't distribute uniformly in a material especially when a large strain is applied, like the case here, where "fins" structures are common on a highly compressed CNT. Some region will have larger local stress or strain and it is the place where defects will appear first. When the maximum local strain becomes large

AA6.5.5

enough, the CNT will begin to have plastic deformation, if enough time is allowed for a relaxation. In the case when constant strain rate is applied, the plastic deformation will happen if the following condition is satisfied:

$$
\Delta t=(1 / v) e^{\frac{U_{0}-\alpha \varepsilon_{\max }}{k T}}, \tag{3}
$$

where $\Delta t$ is the relaxation time allowed for each step during which 1% strain increase is applied. To have plastic deformation for a certain time step and temperature, the required maximum local strain can be expressed as following by rewriting Equation (3):

$$
\varepsilon_{\max }=1 / \alpha\left(U_{0}-k T \ln (v \Delta t)\right), \tag{4}
$$

We can see from this expression that the plastic deformation will happen at a smaller strain with higher temperature or slower strain rate. Although the local strain is not a simple function of the macroscopic strain and depends on the detailed mechanics of a material system, we can still expect a strong strain-rate and temperature dependent behavior of plastic deformation.

In Figure 7a, the yielding strain at which bond rotation begins to happen is plotted as a function of strain-rate for temperature 300K, 800K and 1600K. We can see that, with the decrease of strain-rate the bond rotation happens at smaller strain, as the system has more time to relax to a more stable structure. The yielding strain is also decreased with the increase of temperature, because the larger thermal fluctuations help system to reach its lower energy configurations.

The results of the appearance of sp3 bond show a similar strain-rate and temperature dependent pattern, as can be seen from Figure 7b. It is important to note that the sp3 bond formation is highly dependent on the "fins" structure. Comparing Figure 6 and Figure 7b, we can see that sp3 bonds are always formed after "fins" structure appears. These two

![](./images/811669857652178947_7.jpg)

Figure 7a:Yielding strain of the compressed with bond rotations

![](./images/811669857652178947_8.jpg)

Figure 7b: Yielding strain of the CNT compressed CNT with sp3 bond formation

AA6.5.6

![](./images/811669857652178947_9.jpg)

Figure 8: Compression of CNT with different temperatures with 2%/ps strain rate

![](./images/811669857652178947_10.jpg)

Figure 9: Compression of CNT with different temperatures with 0.0125%/ps strain rate

defects, bond rotation and sp3 bond formation, are quite correlated with each other. With the formation of sp3 bond at some site, the bond rotation becomes easier to happen in the neighborhood. In Figure 8 and Figure 9, sequences of configurations of the compressed CNT are plotted for different temperatures with fast strain rate 2%/ps and slow strain rate 0.012%/ps. From Figure 8, it can be seen that at such fast strain rate, compressed CNT doesn't have enough time to relax at low temperatures, while at high temperature like 1600K, the larger thermal-fluctuations will provide more chance to induce sp3 bond formation and bond rotation on the CNT. From Figure 9, we can see that with more time to relax at each step, sp3 bond and bond rotation appear on the compressed CNT at relatively low temperature like 300K. The early appearance of "Stone-Wales" dislocation (6% strain) at high temperature 1600K, suggests that the formation of bond rotation are

AA6.5.7

much temperature dependent than the formation of sp3 bond, which is more accompanied by the highly non-uniformed "fins" structure.

## CONCLUSION

In this work, we use classical MD simulation to study the plastic deformation of carbon nanotube under compressive strain at finite temperatures. We found sp3 bond can be formed on a strained CNT, in agreement with TB simulation. "Stone-Wales" bond rotation can also be induced. The plastic deformation of CNT is found to be dependent strongly on strain-rate and temperature. Slower strain rate and higher temperature tends to have CNT yield at smaller strain of 6%.

## ACKNOWLEDGEMENT

This work is supported by NASA funding.

## REFERENCE

[1] M. M. J. Treacy, T. W. Ebbesen and J. M. Giblson, *Nature* **381**, 678 (1996).
[2] O. Lourie, D. M. Cox and H. D. Wagner, *Phys. Rev. Lett.* **81**, 1638 (1998).
[3] L. S. Schadler, S. C. Giannaris and P. M. Ajayan, *App. Phys. Lett.* **73**, 3842 (1998).
[4] R. Andrews et. al., *App. Phys. Lett.* **75**, 1329 (1999).
[5] P. M. Ajayan, L. S. Schadler, C. Giannaris and A. Rubio, Advanced Materials **12**, 750 (2000).
[6] D. Qian, E. C. Dickey, R. Andrews and T. Rantell, *App. Phys. Lett.* **76**, 2868 (2000).
[7] J. Tersoff, *Phys. Rev. B* **37**, 6991 (1988).
[8] D. W. Brenner, *Phys. Rev. B* **42**, 9458 (1990).
[9] B. I. Yakobson, C. J. Brabec and J. Bernholc, *Phys. Rev. Lett.* **76**, 2511 (1996).
[10] D. Srivastava, M. Menon and K. Cho, *Phys. Rev. Lett.* **83**, 2973 (1999).
[11] M. B. Nardelli, B. I. Yakobson and J. Berholc, *Phys. Rev. Lett.* **81**, 4656 (1998)