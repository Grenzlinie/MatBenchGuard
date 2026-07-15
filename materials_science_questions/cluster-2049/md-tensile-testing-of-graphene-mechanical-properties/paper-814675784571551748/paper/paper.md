# Infrared Thermal Emission from Joule-Heated Graphene with Defects

Anna Kozłowska¹, Grzegorz Gawlik¹, Roman Szewczyk², Anna Piątkowska¹, Aleksandra Krajewska¹

¹Institute of Electronic Materials Technology, 133 Wólczyńska St., 01-919 Warsaw, Poland
²Warsaw University of Technology, Institute of Metrology and Biomedical Engineering, Św. A. Boboli 8 St., 02-525 Warsaw, Poland

**Abstract:** The influence of mechanical defects on the thermal properties of Joule heated graphene samples is investigated. Modeling and experimental results reveal the hot spots attributed to non-uniform heating due to the mechanical defects of graphene.

OCIS codes: (160.4236) Nanomaterials; (310.7005) Transparent conductive coatings

## 1. Introduction

Graphene is an intriguing material which attracts much attention due to the outstanding electronic, thermal and mechanical properties. Prospects of its application has been demonstrated in many areas including high-speed electronics, mode-locking in laser systems, photovoltaic devices, photodetectors, transparent contacts and heaters [1]. However, proper operation of the graphene devices can be strongly affected by various defects of the structure. Monoatomic vacancies and Stone-Wales dislocations can be responsible for the reduction of the thermal conductivity and Young's modulus [2]. One of a promising area of graphene application is construction of large area transparent electrodes for transparent screens or for transparent window heaters. In this case some macroscopic discontinuities of the graphene layer may play important role because of the current flow through the structure usually is affected by such changes of the electrode shape. Heat dissipation from the graphene devices is often limited by the interfaces, contacts and substrate materials.

A powerful technique for investigations of electronic and thermal properties of graphene devices is infrared imaging. It was successfully used to obtain the temperature distributions and carrier densities in the graphene layers of large area transistors [3,4]. Stationary hot spots that did not move with changing voltage were also observed and were associated with the defects [3]. However, the role of various defects in thermal and electronic properties of graphene devices is not fully understood yet and needs to be clarified. In this paper, the influence of mechanical defects of graphene layers such as cracks or discontinuities on the thermal properties of Joule-heated graphene devices is investigated.

## 2. Experiment

Graphene was synthesized by chemical vapor deposition (CVD) on Cu foil and then transferred onto the glass substrate. For comparison, commercial single layer as well as chemically synthesized graphene samples were investigated in this work. Ohmic contacts to graphene were formed by using silver conductive paste or by vacuum deposition of Cr/Au layers.

Infrared imaging has been performed using InSb 640 M camera (Thermosensorik / DCG Systems). Camera detection range 1.1-4.9 µm was restricted to 3.0-4.9 µm using filters. Two objectives were used in the experiments: wide-field lens with the focal length of 28 mm and microscope objective with the magnification x10 that allows to achieve the spatial resolution of 3 µm. The sample was placed on the heated table in order to register the calibration maps in the controlled temperature. An Auriga cross beam workstation from Carl Zeiss has been used for SEM characterization of the graphene surface.

## 3. Modeling

The scheme of the modeled object is presented in Fig. 1a. Current to graphene coated layer (1) is provided by the conductive plates (2). Power is supplied by the voltage source $U_p$.

For modeling of the Joule heating distribution in the graphene layer, the finite element method was applied. For this modeling, the static current approximation Maxwell's equations was used [5]. Object mesh was generated using top down strategy, where fast Delaunay algorithm generates most of the elements [6]. Then, partial differential equations describing Maxwell's equations were solved using conjugate gradient oriented strategy. It should be stressed, that the model was implemented using open-source software. Mesh was created using NETGEN 5.1, whereas partial differential equations describing Maxwell's equations were solved using ELMER FEM software.

Results of the modeling of Joule heating at the surface of graphene are presented in Figs. 1 b-d. An uniform heating is observed for uniform surface of graphene. However, in the presence of rectangular cracks (Figs 1b and

1d) heating distributions are no more uniform and the areas with elevated heating appear at the opposite rectangle sides. It can be also observed, that a crack starting from the border of graphene surface gives Joule heating distribution in the form of a single heating point (Fig. 1c).

Results of simulations create new possibility of understanding the role of defects in the heating plate. Consequently, the obtained results may be used for improving of manufacturing of the graphene heating electrodes.

![](./images/814675784571551748_1.jpg)

Fig. 1. Schematic diagram of modeled object and the results of simulation of Joule heating distribution P (W/m²) on the graphene layer supplied by voltage Uₚ = 40V: b) square crack, c) crack from the border, d) rectangular crack

## 4. Results and discussion

The results of thermographic characterization for an exemplary Joule heated sample are shown in Fig. 2. Thermal map registered for I = 20 mA and U = 65 V reveals areas with elevated temperature located in the middle and side parts of the sample (Fig. 2a). The inset shows a thermal image of a hot spot gathered with microscope IR optics. Under high magnification it can be seen, that a hot area is composed from a number of smaller hot spots. The horizontal and vertical cross-sections trough a hot spot recalculated to temperature for three power levels are shown in Fig. 2b and 2c, respectively. SEM observations of the sample indicated various defects such as the cracks and graphene discontinuities. Thermographic characterizations of a commercial sample as well as a chemical synthesis sample revealed quite similar hot spots in the area under test as shown in Fig 2a.

![](./images/814675784571551748_2.jpg)

Fig. 2 Thermal image for a CVD graphene sample biased with I = 9.0 mA and U= 40 V; the inset shows a thermal image of a hot spot registered with microscope IR optics; horizontal (b) and vertical (c) cross-sections for three supply power levels

In order to elucidate the effects of hot spot creation an experiment with intentionally introduced defects was performed. First, a reference thermal image for a sample biased with I = 9.0 mA and U= 40 V was captured. Next, two cracks were made on the graphene layer and the second image was taken at the same bias. Resulting differential image is shown in Fig. 3a. The position of the cracks is marked with the dotted lines.

A good coincidence between experimental and modelling results can be seen. As predicted, a crack starting from the border of the sample gives Joule heating distribution in form of a single hot spot, as it can be seen in Fig. 3a and at the cross-sections A and B in Figs. 2b and 3c, respectively. On the other hand, a rectangular defect results in two hot areas at the ends of the crack. The horizontal cross-sections trough the hot areas and in the middle of the defect are shown in Figs. 3 d-f.

![](./images/814675784571551748_3.jpg)

Fig. 3 Thermal image for a sample biased with I = 9.0 mA and U= 40 V; the position of the defects is marked with the dotted line; b)-f)
horizontal temperature distributions for 5 vertical positions marked as A-E

## 5. Conclusions

Results of infrared imaging of CVD and chemically deposited on glass Joule heated graphene samples are presented. Modeling of the Joule heating distribution in the graphene in the presence of layer defects using the finite element method is performed. The results indicate the uniformity deterioration of temperature distributions due to various mechanical defects of the graphene layers. Such defects can arise during the process of deposition of graphene as well as during the manipulation of the samples. In spite of theoretically high fracture strength of graphene, reaching 130 GPa [7], our results indicate high fragility of the single layer graphene. Infrared imaging of Joule heated samples gives a good insight into quality of graphene layers. In practice, presented results may help to better understand the heat emission from graphene electrodes in complex shape.

## 6. Acknowledgements

This work was supported by the Polish National Center for Research and Development under the project no GRAF-TECH/NCBiR/06/30/2012.

## 7. References

[1] F. Bonaccorso, Z. Sun, T. Hasan, , A. C. Ferrari, "Graphene photonics and optoelectronics," Nature Photonics **4**, 611-622 (2010).

[2] F. Hao, D. Fang, Z. Xu, ,,Mechanical and thermal transport properties of graphene with defects," Appl. Phys. Lett. **99**, 041901-1-3 (2011).

[3] M. Freitag, H-Y Chiu, M. Steiner, V. Perebeinos, P. Avouris, ,,Thermal infrared emission from biased graphene, " Nature Nanotechnology **5**, 497-501 (2010).

[4] I. J. Luxmoore, C. Adlem, T. Poole, L.M. Lawton, N.H. Mahlmeier, ,,Thermal emission from large area chemical vapor deposited graphene devices," Appl. Phys. Lett. **103**, 131906-1-3 (2013).

[5] P. Raback, M. Malinen, J. Ruokolainen, A. Pursula, T. Zwinger "Elmer Models Manual" CSC – IT Center for Science (2014).

[6] J. Schoeberl "NETGEN" TU Wien (2003).

[7] C. Lee, X. Wei, J. W. Kysar, and J. Hone, "Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene," Science **321**, 385 (2008).