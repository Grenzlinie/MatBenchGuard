# THE EFFECT OF CHARGING ON ELECTRON DIFFUSION IN SOLIDS

Hendrix Demers and Raynald Gauvin
Département de génie mécanique, Université de Sherbrooke, Sherbrooke, Québec, Canada, J1K 2R1

The studies of insulating specimen by using scanning electron microscopy (SEM) or associated microanalytical techniques such as electron probe microanalysis (EPMA), Auger electron spectroscopy (AES), etc., is limited by the charging phenomena. Different techniques have been found to minimize this problem: coating the specimen with a conductor, working at low energy [1], etc. But for a better knowledge of this effect, we have started a study of the mechanisms of charging as well as its effect on the electrons trajectories in the case of an insulating specimen. With the success, in past years, of Monte Carlo (MC) simulation of electron scattering in solid specimens [2], we have been developing a new Monte Carlo program for the simulation of the electron trajectory in insulators.

With this program, we want to understand the effect of the trapping charge on a insulating specimen. The new MC will be constructed by adding a succession of refined model. In each step, the model goes deeper in the mechanisms for the charging phenomena.

The first model we have studied is a simple one-dimensional electrostatic model for the distribution of the field and the potential. In this model, used by S. Odof [3] and O. Jbara [4], the charge density is supposed uniform in the a coated specimen and the electric field change only with depth. This model suppose a steady state of charging (i.e. no time dependency in the density of trapping centers) and the specimen is assumed to be irradiated by an incident beam scanned over a large area during analysis (i.e. the lateral dimensions of the scanned area are far larger than the range of incident electrons). For the simulation, we use a standard Monte Carlo procedure with single scattering model using Mott Cross Section and a continuous slowing down approximation for the energy loss [2]. In the case with charge effect, we have two simulation parameters to choose: the electric field at the surface of the specimen ($E_{max}$) and the depth of the charge density ($Z_{max}$).

With this first model, we have chosen $E_{max}$ arbitrarily, this value should not represent the real value for a specific specimen, to see is effect on electrons trajectories in MC simulation. The depth has been determined by Monte Carlo simulation without the electric field. The main result for this simulation is the decrease of the depth reached by electrons in the specimen with a increase of the charging ($E_{max}$). This is show in the first figure (1) with the increase of the backscattered coefficient with a increase of $E_{max}$ for an $Al_2O_3$ specimen. Again in the second figure (2) this influence of $E_{max}$ is clearly show by the depth distribution of the total energy loss by electrons. In the two last figures, the total energy loss is separate in two contribution: the Bethe stopping power (3) and the electric energy loss (4).

The next step in our study will be to investigate the effect of more complex models in order to determine their effect in an MC simulation. We will incorporate the X-ray and secondary electrons production, a method for the evaluation of the charge density produced by the interaction of the incident beam and the specimen with a mechanism of trapping and untrapping of charges. The calculation of the electric field, $\mathbf{E}$, inside and outside the specimen will be made by solving the Poisson equation with the charge density deduced by the simulation. We will also look at the influence of the charging and the gaseous environment above the specimen, like in the environmental SEM, on the incident beam and the detection of backscattered and secondary electron and the influence of ions on surface charge.


![](./images/812595436530434048_1.jpg)

Fig 1.

FIG 1. Backscattered coefficient in function of $E_{max}$ for Alumina.

![](./images/812595436530434048_2.jpg)

Fig 2.

FIG 2. Depth distribution of the total energy loss by electrons for Alumina at 20 keV.

![](./images/812595436530434048_3.jpg)

Fig 3.

FIG 3. Depth distribution of the Bethe stopping power by electrons for Alumina at 20 keV.

![](./images/812595436530434048_4.jpg)

Fig 4.

FIG 4. Depth distribution of the electric energy loss by electrons for Alumina at 20 keV

## References
1 D.C. Joy and C.S. Joy, *Low Voltage Scanning Electron Microscopy*, MICRON., 27 (3-4), 247-263 (1996).
2 P. Hovington et al.,*CASINO: A new Monte Carlo code in C language for the electron beam interactions - Part I: Description of the Program*, SCANNING, 19, 1-14 (1997).
3 S. Odof, *Microanalyse X des isolants: simulation de Monte-Carlo*, 2000, Ph.D. Thesis, University of Reims Champagne-Ardenne.
4 O. Jbara et al., *Electron Probe Microanalysis of Insulating Oxides: Monte Carlo Simulations*, X-RAY SPECTROMETRY, 26, 291-302 (1997).