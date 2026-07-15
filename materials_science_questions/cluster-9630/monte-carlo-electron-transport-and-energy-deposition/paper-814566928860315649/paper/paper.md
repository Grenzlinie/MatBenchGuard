# Simulation and Optimization for Space Low Energy Charged Particle Detector

Ba De-dong
Science and Technology on Vacuum Technology Lab
Lanzhou Institute of Physics
Lanzhou, China
Badd215@126.com

Shi Feng
Institute of High Energy Physics
Science Academe of China
Beijing, China
fengshi@sac.cn

Abstract—In order to measure electron and proton in space with the range of $0.1{\sim}1.0$MeV, a permanent magnet and two pieces of one dimension position-sensitive silicon micro-strip detectors(PSSMSD) are used. When incident through the aperture of the detector, the proton will be gathered by a PSSMSD denoted D1 which is paralleled to the center line of the aperture. The distance between D1 and the center line of the aperture is 5mm. while, electron will be gathered by another PSSMSD denoted D2 after deflected to 180 degree. Measure the distance between the center line of the aperture and the point on the PSSMSD which the particle hit, the energy of the particle could be calculated. Based on Geant4, the detector is modeled; the energy resolution, the error in energy measurement and the discrimination efficiency between proton and other positive ion are simulated. The optimized results for the two PSSMSDs are given.

Keywords—space low energy charged particle, one dimension position-sensitive silicon micro-strip detector, Geant4, simulation, optimization

## I. INTRODUCTION

As a component of space radiation environment, low energy charged particles have an important influence on spacecraft, such as space charging. It is meaningful to detect them. So far, there is none of the detectors which can monitor low energy charged particles in the range of $0.1{\sim}1.0$ MeV. Based on magnetic field formed by permanent magnet and position-sensitive silicon micro-strip detector with one dimension (PSSMSD), a conceptual design of the detector to monitor electrons and protons in the range of $0.1{\sim}1.0$ MeV in space is proposed.

Incident through the aperture of the detector, after be deflected a small degree, protons will hit on a piece of PSSMSD denoted D1, which is paralleled to the aperture's center line. The distance between D1 and the center line of the aperture is 5mm. Electrons will hit on another piece of PSSMSD denoted D2 after deflected to 180 degree. Measure the distance between the center line of the aperture and the point on the PSSMSD which the particle hit, the energy of the particle could be calculated easily. In conceptual design, the magnetic field strength is 0.1T, the gap of the aperture is 2.0 millimeters, the size of D1 is 8.8centimeters long, 2centimeters wide, and D2 is 9.0centimeters long, 2.0centimeters wide. Both of the D1 and D2 have the thickness of 500 micrometers.

## II. SIMULATION FOR THE DETECTOR

### A. Detector modeling

To make a validation and optimization, based on Geant4, the detector is modeled; the cross-section of the model is illustrated in Fig. 1. The direction of X axis is perpendicular and out to the paper, while the direction of magnetic field is opposite. D1 is placed along Z axis, and D2 is placed along Y axis. To simulating simply, we define the length of D1 and D2 are 15 centimeters, and the widths are 0.2centimeters. Particles will travel through the gap of the aperture and get into the inner of the detector. The gap of the aperture has a width of 2 millimeters. The magnetic field strength is 0.1T.

![](./images/814566928860315649_1.jpg)

Fig. 1. Cross Section of detector modeled

### B. Simulation with electrons

In order to study the capability for electrons monitoring of the detector, the interaction between electrons in the range of $0.1{\sim}1.0$MeV and the detector is simulated. To obtain better and more representable results, the numbers of electrons should be used as more as possible. In this simulation, we use 0.1 million electrons which has a uniform distribution in energy in the range of $0.1{\sim}1.0$MeV. Deflected by magnetic field, electrons will hit on different position of D2. Since the track diameters of electrons are in direct proportion to their energy, the relationship between the hit positions on D2 vs. the energy of the electrons is linear. Science the thicknesses of D2 is 0.05centimeters, electrons whose energy less than 1.0MeV

978-1-5090-0232-0/15/$31.00 ©2015 IEEE

can't penetrate D2 and lose whole energy in D2. So is the relation between the deposited energy and hit position.

As an important character of PSSMSD, the width of the pitch of PSSMSD will affect the results of the energy measurement. To study that, different widths of the pitch are used. The root mean square (RMS) of energy measured vs. the width of the pitch is illustrated in Fig.2, while the energy resolution vs. the incident energy of electrons is shown in Fig.3.

![](./images/814566928860315649_2.jpg)

Fig. 2. RMS in energy measurement vs. strip pitch (electrons)

![](./images/814566928860315649_3.jpg)

Fig. 3. Energy Resolution vs. strip pitch (electrons)

It can be seen that the RMS of the energy measured is the smallest when the strip pitch is 1.5mm. When the strip pitch is wider than 0.15centimeters, as the strip pitch is increasing, the RMS of the energy measured is increasing too. Moreover, when the strip pitch is less or more than 0.15centimeters, the energy resolution is getting worse and worse.

### C. Simulation with protons and positrons

In order to study the response of the detector to positive particles, simulation with 0.1 million protons in the energy range of 0.1～1.0 MeV and 0.1 million positrons in the energy range of 10.0～50.0 MeV are practiced. The result for positron is illustrated in Fig.4, and the result for proton is illustrated in Fig.5.

![](./images/814566928860315649_4.jpg)

Fig. 4. Deposited energy of positron vs. hit position

![](./images/814566928860315649_5.jpg)

Fig. 5. deposited energy of positron vs. hit position

It is shown in figure5 that the deposited energy of positrons with the energy of 10.0～50.0 MeV is in the range of 0.5～1.5 MeV, and the hit position has a range of 6.0～13.0 centimeters. For protons, the deposited energy range is 0.1～1.0 MeV, and the hit position has a range of 6.8～12.0 centimeters.

The RMS of the energy measured and the energy resolution are also simulated under the condition of different strip pitches, the results are illustrated in Fig.6 and Fig.7 separately.

![](./images/814566928860315649_6.jpg)

Fig. 6. RMS in energy measurement vs. strip pitches (protons/positrons)

![](./images/814566928860315649_7.jpg)

Fig. 7. Energy Resolution vs. strip pitch (protons/positrons)

### III. RESULTS

According to the simulation results, we can conclude: for electrons, when the strip-pitch of D2 is wider than 0.15 centimeters, the RMS of energy measured and the energy resolution have a bigger fluctuation, but when the strip-pitch of D2 is less than 0.15 centimeters, the fluctuation in both of them are getting smaller. For different strip pitches, energy resolution are decreasing as the particle energy are increasing. When the strip-pitch of D2 is 0.15 centimeters, the energy resolution and RMS in energy measured of D2 are the most optimized. Moreover, for protons, for different strip pitches of D1, RMS in energy measured is increasing when the energy is increasing; when the strip pitch of D1 is wider than 1.0 centimeters, RMS in energy measurement has a bigger fluctuation. When the strip pitch of D1 is less than 0.5 centimeters, the energy resolution is stable as the energy of protons is increasing. So the compromised value of the strip-pitch of D1 is 0.5 centimeters.

### IV. CONCLUSION

According to the results simulated, the optimized characters for both D1 and D2 are given in table1.Thus, the detector will have a good performance for monitoring the low energy electrons and protons with the energy of 0.1～1.0MeV in space.

<table>
  <caption>TABLE I. OPTIMIZED CHARACTERS FOR D1 AND D2</caption>
  <thead>
    <tr>
      <th>Detectors</th>
      <th>Thickness (millimeters)</th>
      <th>Length (millimeters)</th>
      <th>Strip Pitch (millimeters)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>D1</td>
      <td>0.5</td>
      <td>75.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>D2</td>
      <td>0.5</td>
      <td>55.0</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>

### ACKNOWLEDGMENT

With the help of Dr. Sheng-sheng Yang, Senior Engineer Yu-xiong Xue, the paper is finished. Thanks a lot for their valuable work.

### REFERENCES

[1] Qian Zhen-ya, "Study of the monitoring technologies on low energy particles ," Space Science Academy of China, pp. 32-37, 2003

[2] B. P. F. Dirks, O. Limousin, P. Ferrando, R. Chipaux "3D modeling of Cd (Zn) Te detectors for the SIMBOL-X Space", High energy Detectors in Astronomy , proceedings of SPIE, vol. 5501, pp. 412-415, 2004.

[3] J. W. nam, Y. I. Choi, D. W. Kim, J. H. Kim, "A detailed Monte Carlo simulation for the Belle TOF system," Nuclear Instruments and Methods in Physics Research A., vol.491, no. 4, pp. 54-68, 2002.

[4] M. Ablikim, J. Z. Bai, Y. Ban, J. G. Bian, "BES II detector simulation," Nuclear Instruments and Methods in Physics Research A., vol. 552, no. 6,pp. 344-356, Dec, 2005.

[5] MAKOTO ASAI, "Geant4 Applications In Space," 10th ICATPP Conference On Astroparticle, Particle, Space Physics, Detectors and Medical Physics Applications, Como, Italy, Oct, 2007.