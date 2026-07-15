![](./images/814530938699513857_1.jpg)

Computational Materials Science 120 (2016) 94-98

Contents lists available at ScienceDirect

# Computational Materials Science

journal homepage: www.elsevier.com/locate/commatsci

![](./images/814530938699513857_2.jpg)

# Concurrence of oscillatory and rotation of the rotors in a thermal nanotube motor

Jiao Shi $^{a}$, Zhengzhong Wang $^{a,*}$, Zhen Chen $^{b,c}$

$^{a}$ College of Water Resources and Architectural Engineering, Northwest A\&F University, Yangling 712100, China
$^{b}$ State Key Laboratory of Structural Analysis for Industrial Equipment, Department of Engineering Mechanics, Faculty of Vehicle Engineering and Mechanics, Dalian University of Technology, Dalian 116024, China
$^{c}$ Department of Civil \& Environmental Engineering, University of Missouri, Columbia, MO 65211-2200, USA

![](./images/814530938699513857_3.jpg)

## ARTICLE INFO

**Article history:**
Received 12 February 2016
Received in revised form 31 March 2016
Accepted 5 April 2016
Available online 27 April 2016

**Keywords:**
Nanomotor
Carbon nanotube
Oscillator
Rotor
NEMS

## ABSTRACT

In studying dynamic response of a nanomotor made from triple-walled carbon nanotubes (TWCNTs), we find the concurrence of oscillation and rotation of the rotors in the fixed outer tubes (i.e., stators) when the system is in a canonical NVT ensemble with temperature higher than 100 K. In the system, the mid tube, called mid-rotor, is driven to rotate by the collision between the end carbon atoms on mid-rotor and the inward radial deviated (IRD) atom(s) on stator(s). The collision depends on three factors, e.g., the inward radial deviation of end atom(s) on stator(s), the number of IRD atoms and temperature of environment. In present research, fixing the first factor with a constant, the acceleration of the mid-rotor needs lower time to approach the maximal rotational frequency when the stators have more IRD atoms. And the maximal rotational frequency of mid-rotor is greater at higher temperature. Due to intertube friction, the inner tube, called inner-rotor, is driven to rotate by the mid-rotor. The system is stable when the inner-rotor has a stable rotational frequency which can be different from that of mid-rotor. During rotating, the inner-rotor may have large-amplitude oscillation. Hence, the simple but interesting model suggests a potential application in a nano-electro-mechanical system (NEMS).

© 2016 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Since the work by Cumings and Zettl [1], people have taken much effort on developing nanomotor made from carbon nanotubes (CNT) [2–14]. According to the motion types of the movers in motors, the motors can be classified into two types. One is the linear motor with translational motion along the axis of the stator (fixed tube(s)) and the other is the rotary motor with rotating along the axis of the stator.

Considering ultralow friction between adjacent walls [1,16], Zheng and Jiang [17] proposed a CNT-oscillator model to predict the oscillation response of the free inner tubes in outer tube. Commonly, such oscillator is also considered as a linear motor [7,18–26]. As a matter of fact, the rotary nanomotor is popular, too. For example, in experiments, Fennimore et al. [2] and Bourlon et al. [3] fabricated a rotary nanomotor in which the multi-walled carbon nanotubes (MWCNTs) acting as a bearing. Using simulation method, Tu and Hu [5] designed a rotary motor from DWCNTs, in which a short outer tube driven was actuated by varying electrical voltage along axis to rotate on a fixed long inner tube. Hamdi et al. [10] found that the charged inner tube in an opposing chirality outer tube can also be actuated to rotate in a static electronic field. In 2014, Cai et al. [14] found that the inner CNT in a fixed outer CNT would rotate at an NVT ensemble with constant temperature and the final stable rotational frequency of rotor was over 100 GHz. Due to only two tube, i.e., one is fixed and the other is free, in the system in a thermostat, it suggested the most simple rotary nanomotor model. Recently, Cai et al. [15] gave an accurate model on carbon nanotube based nanomotor driven by thermal vibration of atoms on motor.

In general, the movers may contain both of linear motion and rotation in a stator [24,25,27]. For either linear motion or rotation, the energy transfer/dissipation [24,26,28–30] of the rotor leads to the damped motion of the motor with time. How to control a system with simple model but stable rotation and large-amplitude oscillation is a challenge for its applications in a nano-electro-mechanical system (NEMS). For instance, Rivera et al. [18] measured the sliding resistance of the damped oscillation of a DWCNTs-based linear motor. Zhao et al. [19] studied the mechanism of energy transfer during oscillation and stated that the friction force per atoms was in $10^{-17}$-$10^{-14}$ N. Legoas et al. [21],

* Corresponding author.
E-mail address: coopcsw@163.com (Z. Wang).

http://dx.doi.org/10.1016/j.commatsci.2016.04.005
0927-0256/© 2016 Elsevier B.V. All rights reserved.

suggested to providing magnetic force to obtain a stable oscillation of the movable core. To maintain stable oscillation, Neild et al. [22] suggested to providing periodically varying external force on the core along axis. Ershova et al. [23] gave a systematic study on the way to provide external force to drive the stable oscillation.

As one can see, the system mentioned above is small but very complicated, e.g., requiring Gega Hertz or even Tera Hertz external force field. Hence, in the present work, we build a new model shown in Fig. 1 inspired by the temperature nanomotor model proposed by Cai et al. [14,15]. In the triple-walled carbon nanotubes (TWCNTs), the outer tube is separated into short parts which are fixed as stators. Both ends of the mid tube are almost aligned with the outer ends of stators. The mid tube will rotate if the outer end(s) of the stators have no geometric symmetry. Due to intertube friction, the rotational frequency of mid tube will have a maximal value, and the inner tube will also be actuated to rotate. We prepare a series of schemes on the stators and the temperature of environment to find the stable large-amplitude oscillation of the inner tube.

## 2. Models and methods

The system shown in Fig. 1a is made from TWCNTs, in which the outer tube is separated into two parts named left stator (L-stator) and right stator (R-stator), the mid tube and the inner tube are rotors and called mid-rotor and inner-rotor, respectively. Each stator has 210 atoms, the mid tube and the inner tube have 460 and 500 atoms, respectively. To describe the interaction among atoms in the system, the Adaptive Intermolecular Reactive Empirical Bond Order (AIREBO) Potential proposed by Stuart et al. [31] is adopted in simulation which is carried out in the open sources molecular dynamic package of LAMMPS [32]. The time step for integration is 0.001 ps. After energy minimization on the initial model, the atoms (including IRD atoms) on the two stators are fixed. The two rotors are set at canonical NVT ($N$: the number of atoms in system; $V$: volume of system; $T$: temperature of system) ensemble. The simulation duration of dynamic response of the system is 8000 ps. For calculating the rotational frequency of inner-rotor, we use syntax "variable omg_in equal omega(inner, z) * 500/3.14159265357", in which "inner" means inner-rotor, $z$ is the axial direction of inner-rotor (from left to right in the present simulation). The unit of omg_in will be GHz. For obtaining the oscillation of inner-rotor, we adopt syntax "variable disin equal xcm(inner, z)/10", and the unit of "disin" is nm.

## 3. Results and discussions

### 3.1. Dynamics response of the model with different IRD schemes

Mechanism of rotation of both rotors is as following. The mid-rotor is driven to rotate by the thermal vibration of the end atoms on the rotor and the IRD atoms on the stators. The reason for that is the thermal vibration of end atoms on rotor results in collision between the end atoms and the IRD atoms on the stator(s) [15]. The collision produces circular and axial velocity of the rotor. The circular velocity results in rotation of rotor and the axial velocity raises oscillation. The rotor rotates in acceleration until the friction between the rotor and stator(s) is in balance with the impact force in collision. Hence, IRD schemes and temperature determines the dynamic behavior of the rotor. The rotation of inner-rotor is actuated by the friction between the two rotors. The oscillation of inner-rotor can happen due to serious end interaction with the mid-rotor.

Fig. 2a shows that the rotational acceleration process of mid-rotor is different at 400 K when the stators have different number of IRD atoms. The final stable rotational frequency of mid-rotor has small differences among the schemes, e.g., nearby 133 GHz. As one can see, the mid-rotor driven by the stators with more IRD atoms has shorter time of rotational acceleration. Except driven by the stators in the IRD schemes of 2L and 2LR, the difference of the

![](./images/814530938699513857_4.jpg)

Fig. 1. (a) A model of nanomotor made from triple-walled carbon nanotubes, in which the two (15, 15) outer CNTs are fixed as stators, e.g., left stator (L-stator) and right stator (R-stator), the (10, 10) CNT acts as a rotor (mid-rotor), which is driven to rotate at NVT ensemble by the stator(s). The (5, 5) inner CNT acts as both o f a rotor and an oscillator when the mid tube is rotating along z-axis. (b) Schematics of 8 schemes of the layout of the inward radial deviated (IRD) atoms (red balls) on the outer ends of stator(s) to represent the geometrical asymmetry of ends. 1L means there is only one IRD atom on the left end of the L-stator, similarly, the number of IRD atoms can also be 2, 3 or 4, with respect to 2L, 3L or 4L scheme. 1LR indicates that on both outer ends of the stators there is an IRD atom, similarly, the number of IRD atoms can be 2, 3 or 4, with respect to 2LR, 3LR or 4LR scheme. The inward radial deviations of the IRD atoms are the same, i.e., 0.4 times of the $sp^2$ carbon-carbon bond length (0.142 nm). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/814530938699513857_5.jpg)
![](./images/814530938699513857_6.jpg)

Fig. 2. (a) Rotational histories of the mid and inner rotors driven by the stators at the temperature of 400 K. "Mid" and "In" represent the mid-rotor, and the inner-rotor, respectively. (b) Oscillation histories of the inner-rotor in the system with different IRD schemes. The value of rotational frequency of both rotors being negative implies that rotational directions of the two rotors are opposite to that (of the "$\omega$") shown in Fig. 1. (c) Histories of potential energy of the whole system with different IRD schemes at 400 K.

acceleration process of mid-rotor is slight when comparing the mid-rotor is driven either by one stator (e.g., 1L, 3L or 4L scheme) or by two stators (e.g., 1LR, 3LR or 4LR scheme).

Curves also show that the two rotors have synchronous rotation in the schemes of 1L, 1LR and 2L. The major reason is that the acceleration process of mid-rotor lasts longer time, and the inter-shell friction between two rotors has enough time to reduce their relative speed during acceleration. When the two rotors rotate asynchronously, the fluctuation of the rotational frequency of inner-rotor is in [75, 100] GHz, which is far greater than that of the mid-rotor. The initial position of the mass center of inner rotor is at $\sim$3.0 nm away from the reference position (with respect to z = 0 in Fig. 1a). From the curves shown in Fig. 2b, the mass center of inn-rotor mainly varies in [1.5, 4.5] nm, i.e., the amplitude of oscillation is $\sim$1.5 nm if the inner-rotor has stable oscillation (see the 1LR curve in Fig. 2b). From the model shown in Fig. 1, we know that the length difference between two rotors is $\sim$3.29 nm. Half of 3.29 nm is slightly higher than 1.5 nm because the two adjacent ends of the two rotors cannot be aligned well due to higher potential on ends. For the sake of symmetric layout of the stators, the inner-rotor is randomly aligned with the mid-rotor at left end (mass center of inner tube varies in [4, 4.5] nm) or at right end (mass center of the inner tube varies in [1.5, 2] nm) along z-axis.

Fig. 2c shows the potential energy history curves of the system with different IRD schemes. As one can see, the difference between the 1L and 1LR or between the 2L and 2LR schemes is. As the number of IRD atoms is high, e.g., 3 or 4, the difference becomes slight. The potential energy of the system contains four parts. The first part is produced by the initial relative positions of atoms in the system. It is $\sim -$9725 eV, which is the major fixed part of the whole potential energy in Fig. 2c. The second part is the deformation energy of the mid-rotor due to centrifugal force which is produced by high speed rotation. The third part is the deformation energy of the inner-rotor. The final part is the interaction among the tubes. Clearly, the last three parts change with the time. Especially, the rotational speed of both rotors increases with the time. It brings in the major variation of potential energy of the system. Comparing the second and the third parts, we find that the mid-rotor provides higher variation of the potential energy. Hence, one can easily find that the tendency of the potential energy curves matches that of the rotational frequency curve of the mid-rotor very well.

From Fig. 2d one can see that the mid-rotor also has oscillation along z-axis. However, the amplitude of the oscillation of mid-rotor is no more than 0.1 nm, which far less than that of inner-rotor. The reason is that the two stators constrain the mid-rotor to move far away from the outer ends. However, the oscillation will provide axial collision with the ends of the inner-tube as the ends are close to each other. It suggests oscillation of the inner-rotor.

From above, one should pay attention to the following three states: (1) synchronous rotation of two rotors; (2) asynchronous rotation and (3) concurrence of rotation and stable large-amplitude oscillation of inner rotor (e.g., in scheme 1LR). The three states should be able to transfer from one to another if considering potential application in a future NEMS. As we know, the device working at finite temperature, the effect of temperature on the states should be demonstrated.

![](./images/814530938699513857_7.jpg)
![](./images/814530938699513857_8.jpg)

Fig. 3. The dynamic response of the two rotors in the motor with IRD scheme of 4LR at different temperature. (a) Rotational histories; (b) oscillation of the inner-rotor.

![](./images/814530938699513857_9.jpg)
![](./images/814530938699513857_10.jpg)

Fig. 4. The dynamic response of the two rotors in the motor with IRD scheme of 1LR at different temperature. (a) Rotational histories; (b) oscillation of the inner-rotor.

### 3.2. Temperature effects on the dynamic response of the motor

Temperature, actually, is the essential factor of the dynamic response of the two rotors [14]. In general, the rotors rotate slower at lower temperature. From Fig. 2, we know that the inner-rotor can have stable large-amplitude oscillation at 400 K. What will happen to the oscillation at lower temperature?

Fig. 3 shows the behavior of the two rotors driven by stators in the IRD scheme of 4LR at different temperature below 400 K. The stable oscillation of the inner-rotor happens at the temperature of 200 K. At the same time, both rotors have stable rotation. The rotational frequency of inner-rotor is $\sim$25 GHz and the rotational frequency of mid-rotor is $\sim$70 GHz which is the lowest among four temperature cases. It concludes that the stable large-amplitude oscillation of inner-rotor can happen at lower temperature. When the temperature is in [250, 350] K, the stable rotational frequency of mid-rotor varies slightly nearby 133 GHz. The rotational frequency of inner-rotor increases faster at higher temperature. And the relative rotational frequency between both rotors is lower at higher temperature.

In Fig. 3, each stator has 4 IRD atoms. As one can see that the inner-rotor has stable large-amplitude oscillation at 200 K. What will happen to the oscillation of inner-rotor if there is only one IRD on each stator? Fig. 4 demonstrates the behavior of the rotors driven by the stators with the IRD scheme of 1LR at different temperature.

From Fig. 4, the difference of the rotational frequency between both rotors decreases with the increasing of temperature. In particular, the two rotors rotate synchronously when the temperature is 300 or 400 K. It implies that the rotational state of both rotors can be adjusted by varying temperature. For all cases, the inner-rotor always has oscillation with large amplitude. It suggests a way to obtain a "rotator + oscillator" nanodevice (see Movie attached).

### 4. Concluding remarks

In the TWCNTs-based nanomotor, the outer tube are separated into two parts and fixed as stators. The inner-rotor and mid-rotor are free. When the position of one or more atoms on the outer ends of the stators has inward deviation along radial direction, the two rotors can be driven to rotate at high temperature. And the inner-rotor can have large-amplitude oscillation while rotating. From numerical results, some conclusions are drawn.

(1) The mid-rotor is driven to rotate by the collision between the end carbon atoms on mid-rotor and the IRD atom(s) on stator(s) due to thermal vibration. When the impact force and the friction applied on the mi-rotor is in balance on time average, the maximal rotational frequency reaches. And the maximal rotational frequency of mid-rotor is greater at higher temperature.

(2) The inner-rotor is driven to rotate by the friction of the mid-rotor. During rotating, the inner-rotor may have large-amplitude oscillation, which depends on temperature (>100 K) weakly.

(3) The three states of rotors, i.e., synchronous rotation; asynchronous rotation and rotation with stable large-amplitude oscillation of the inner rotor, can be adjusted by changing temperature and the number of IRD atoms on stators.

(4) The inner-rotor oscillates due to ends collision with the mid-rotor. However, the present oscillation is not stable. Our future task will focus on the stable oscillation of inner-rotor.

## Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.commatsci.2016.04.005.

## References

[1] J. Cumings, A. Zettl, Science 289 (2000) 602.
[2] A.M. Fennimore, T.D. Yuzvinsky, W.Q. Han, M.S. Fuhrer, J. Cumings, A. Zettl, Nature 424 (2003) 408.
[3] B. Bourlon, D.C. Glattli, C. Miko, L. Forro, A. Bachtold, Nano Lett. 4 (2004) 709.
[4] J.W. Kang, H.J. Hwang, Nanotechnology 15 (2004) 1633.
[5] Z. Tu, X. Hu, Phys. Rev. B 72 (2005). 033404.
[6] B. Wang, L. Vuković, P. Král, Phys. Rev. Lett. 101 (2008). 186808.
[7] A. Barreiro, R. Rurali, E.R. Hernandez, J. Moser, T. Pichler, L. Forro, A. Bachtold, Science 320 (2008) 775.
[8] H. Somada, K. Hirahara, S. Akita, Y. Nakayama, Nano Lett. 9 (2009) 62.
[9] P.M. Shenai, J. Ye, Y. Zhao, Nanotechnology 21 (2010). 495303.
[10] M. Hamdi, A. Subramanian, L. Dong, A. Ferreira, B.J. Nelson, IEEE/ASME Trans. 18 (2013) 130.

[11] I. Santamaria-Holek, D. Reguera, J.M. Rubi, J. Phys. Chem. C 117 (2013) 3109.
[12] K. Cai, J.Z. Yu, J. Wan, H. Yin, J. Shi, Q.H. Qin, Carbon 101 (2016) 168-176.
[13] S.B. Legoas, V.R. Coluci, S.F. Braga, P.Z. Coura, S.O. Dantas, D.S. Galvão, Phys. Rev. Lett. 90 (2003). 055504.
[14] K. Cai, Y. Li, Q.H. Qin, H. Yin, Nanotechnology 25 (2014). 505701.
[15] K. Cai, J. Wan, Q.H. Qin, J. Shi, Nanotechnology 27 (5) (2016). 055706.
[16] R. Zhang, Z. Ning, Y. Zhang, Q. Zheng, Q. Chen, H. Xie, Q. Zhang, W. Qian, F. Wei, Nat. Nanotechnol. 8 (2013) 912.
[17] Q. Zheng, Q. Jiang, Phys. Rev. Lett. 88 (2002). 045503.
[18] J.L. Rivera, C. McCabe, P.T. Cummings, Nano Lett. 3 (2003) 1001.
[19] Y. Zhao, C.C. Ma, G. Chen, Q. Jiang, Phys. Rev. Lett. 91 (2003). 1755041.
[20] C.-C. Ma, Y. Zhao, C.-Y. Yam, G.H. Chen, Q. Jiang, Nanotechnology 16 (2005) 1253.
[21] S.B. Legoas, V.R. Coluci, S.F. Braga, P.Z. Coura, S.O. Dantas, D.S. Galvão, Nanotechnology 15 (2004) S184.
[22] A. Neild, T.W. Ng, Q. Zheng, EPL 87 (2009) 16002.
[23] O.V. Ershova, I.V. Lebedeva, Y.E. Lozovik, A.M. Popov, A.A. Knizhnik, B.V. Potapkin, O.N. Bubel, E.F. Kislyakov, N.A. Poklonskii, Phys. Rev. B 81 (2010). 155453.
[24] Y. Li, N. Hu, G. Yamamoto, Z. Wang, T. Hashida, H. Asanuma, C. Dong, T. Okabe, M. Arai, H. Fukunaga, Carbon 48 (2010) 2934.
[25] A.M. Popov, I.V. Lebedeva, A.A. Knizhnik, Y.E. Lozovik, B.V. Potapkin, J. Chem. Phys. 138 (2013). 024703.
[26] J. Chen, Y. Gao, C. Wang, R. Zhang, H. Zhao, H. Fang, J. Phys. Chem. C 119 (2015) 17362.
[27] A.V. Belikov, Y.E. Lozovik, A.G. Nikolaev, A.M. Popo, Chem. Phys. Lett. 385 (2004) 72.
[28] C. Zhu, W. Guo, T. Yu, Nanotechnology 19 (2008). 465703.
[29] A. Eichler, J. Moser, J. Chaste, M. Zdrojek, I. Wilson-Rae, A. Bachtold, Nat. Nanotechnol. 6 (2011) 339.
[30] K. Cai, H. Yin, Q.H. Qin, Y. Li, Nano Lett. 14 (2014) 2558.
[31] S.T. Stuart, A.B. Tutein, J.A. Harrison, J. Chem. Phys. 112 (2000) 6472.
[32] LAMMPS, Molecular Dynamics Simulator, 2015, <http://lammps.sandia.gov/>.