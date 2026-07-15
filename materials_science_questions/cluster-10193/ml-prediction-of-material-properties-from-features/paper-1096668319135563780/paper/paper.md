# CAST: Cross ATTENTION BASED MULTIMODAL FUSION OF STRUCTURE AND TEXT FOR MATERIALS PROPERTY PREDICTION

Jaewan Lee
Materials Intelligence Lab
LG AI Research
Seoul, Republic of Korea
jaewan.lee@lgresearch.ai

Changyoung Park
Materials Intelligence Lab
LG AI Research
Seoul, Republic of Korea
changyoung.park@lgresearch.ai

Hongjun Yang
Materials Intelligence Lab
LG AI Research
Seoul, Republic of Koreal
hongjun.yang@lgresearch.ai

Sungbin Lim
Department of statistics
Korea University
Seoul, Republic of Korea
sunbin@korea.ac.kr

Sehui Han
Materials Intelligence Lab
LG AI Research
Seoul, Republic of Korea
hansse.han@lgresearch.ai

February 12, 2025

## ABSTRACT
Recent advancements in AI have revolutionized property prediction in materials science and accelerating material discovery. Graph neural networks (GNNs) stand out due to their ability to represent crystal structures as graphs, effectively capturing local interactions and delivering superior predictions. However, these methods often lose critical global information, such as crystal systems and repetitive unit connectivity. To address this, we propose CAST, a cross-attention-based multimodal fusion model that integrates graph and text modalities to preserve essential material information. CAST combines node- and token-level features using cross-attention mechanisms, surpassing previous approaches reliant on material-level embeddings like graph mean-pooling or [ĠCLS] tokens. A masked node prediction pretraining strategy further enhances atomic-level information integration. Our method achieved up to 22.9% improvement in property prediction across four crystal properties including band gap compared to methods like CrysMMNet and MultiMat. Pretraining was key to aligning node and text embeddings, with attention maps confirming its effectiveness in capturing relationships between nodes and tokens. This study highlights the potential of multimodal learning in materials science, paving the way for more robust predictive models that incorporate both local and global information.

## 1 Introduction
Designing AI-based predictive models has become an essential tool for accelerating the discovery and optimization of advanced materials. Traditional approaches rely heavily on domain expertise and heuristic methods, often supplemented by Density Functional Theory(DFT) calculations. While DFT is widely used for its accuracy in predicting material properties, its computational expense and time requirements limit its scalability for high-throughput material discovery, especially given the complexity and diversity of material systems. With the advent of machine learning(ML) techniques, particularly Graph Neural Networks(GNNs), researchers have been able to model material structures with unprecedented accuracy and speed by representing them as graphs and capturing intricate local interactions[1, 2, 3, 4, 5, 6]. Despite these advancements, the process of converting material structures into graph representations inherently leads to the loss of crucial information, such as crystal symmetries and the connectivity of repetitive structural units, which are critical to certain material properties. This issue is inherent when using GNNs. To address this limitation, multimodal learning can be leveraged to complement the lost information by incorporating additional modalities. While multimodal learning has been extensively studied in fields such as vision, language, and speech [7, 8, 9], its application in the materials,

especially inorganic crystals, remains relatively underexplored.[10, 11, 12, 13, 14] One primary reason for this gap is the relative scarcity of data suitable for multimodal learning in materials science. However, the recent development of tools like Crystallographer[15], an API that generates textual descriptions from crystal structures, has enabled some initial studies in this area. Crystallographer generates text descriptions based on rules derived from structural information, including global and semi-global features that are often lost when structures are converted into graph representations. This advancement has opened new opportunities for integrating multimodal approaches in materials science research.

Techniques such as various attention methods[16, 17, 18] and gradient modulation [19, 20] often drive advancements in multimodal learning within the Vision-Language and molecule domains. In contrast, materials science primarily relies on simpler approaches, such as concatenation or contrastive pretraining methods like CLIP[21]. Notable examples are CrysMMNet[10] and MultiMat[22], which are optimized to predict properties of materials. CrysMMNet encodes structure and text using separate modality encoders, then concatenates the embeddings to predict material properties. MultiMat simultaneously leverages structure, text, density of states(DOS), and charge density, employing contrastive learning to pretrain a GNN encoder before applying it to downstream tasks. Both approaches demonstrated performance improvements over unimodal GNNs, but their reliance on coarse-level modality combination introduces limitations which may fail to fully exploit the intricate relationships between modalities, potentially resulting in suboptimal performance.

In contrast, we propose a CAST, Cross Attention-based multimodal fusion of Structure and Text, which integrates graph and text modalities at a fine-grained level, ensuring profound mutual interactions. Our method incorporates node- and token-level features using cross-attention mechanisms, which are proposed in a Transformer[23], allowing the model to learn more complex relationships between the structural and textual representations. Inspired by the success of masked object prediction in the language domain [24, 25, 26], we applied a Masked Node Prediction (MNP) pretraining strategy by masking a subset of nodes in the graph and training the model to predict the masked nodes using information from their neighboring nodes and corresponding text tokens. Through extensive experimentation, we demonstrate that our approach outperforms unimodal models as well as multimodal methods like CrysMMNet and MultiMat, achieving performance gains of up to 22.9% across four property prediction tasks. Analyses of cross-attention maps further reveal that pretraining enables attention heads to effectively capture a diverse range of node-token relationships, which are critical for accurate predictions. By addressing the inherent limitations of existing models, our work establishes a robust framework for multimodal learning in materials science, paving the way for more accurate predictive models.

## 2 Results and discussion

### 2.1 Data

For training and evaluation, data was downloaded from the Materials Project[27] database and rigorously filtered to ensure quality and relevance. The filtering criteria were inspired by the data cleaning methods used in MatBench[28] and further enhanced with additional constraints to ensure practical applicability and facilitate efficient screening processes for real-world use. The applied filters are as follows:
**MatBench Filtering Criteria:**

- Remove entries with a formation energy or energy above the convex hull greater than 150 meV.
- Exclude entries where $G_{\text{Voigt}}$, $G_{\text{Reuss}}$, $G_{\text{VRH}}$, $K_{\text{Voigt}}$, $K_{\text{Reuss}}$, or $K_{\text{VRH}}$ are less than or equal to zero.
- Remove entries that do not satisfy the conditions $G_{Reuss} < G_{VRH} < G_{Voigt}$ or $K_{Reuss} < K_{VRH} < K_{Voigt}$.
- Exclude entries containing noble gases.

**Additional Filtering:**

- Exclude entries with a formation energy greater than -10 eV.
- Remove entries with shear modulus or bulk modulus values exceeding 1000 GPa.

For regression tasks, we used four properties(total energy, bandgap, shear modulus and bulk modululs). Each dataset comprised 114,398, 65,367, 9,423 and 9,423 instances, respectively. Detailed statistical analyses of the regression data for each target property can be found in the Table 2. For the pretraining stage, we leveraged the total energy data, which had the largest volume of samples.

![](./images/1096668319135563780_1.jpg)

Figure 1: Overall framework of CAST (a) Pretraining. During pretraining, a subset of nodes is masked with a 50% probability. The structure encoder processes the graph to generate node embeddings, while the corresponding text is encoded into token-level embeddings using a language model (LM). A cross-attention mechanism enables node embeddings to interact with text token embeddings, aligning nodes with relevant textual descriptions. The model learns to predict the masked node's element type, aligning structural and textual features. (b) Finetuning. In the finetuning stage, the pretrained model is adapted for material property prediction by replacing the classification block with a regression block. The structural and textual embeddings, aligned during pretraining, are leveraged to predict material properties accurately through cross-attention and interaction layers.

## 2.2 Text generation
While the Materials Project directly provides structural information in cif formats, textual descriptions of material structures were generated using the Robocrystallographer API[15]. This allows for the automatic conversion of structural data into textual descriptions, which we processed using the default settings. For instances where text could not be generated, we adapted our approach by passing only the [ĊĿS] token through the text encoder. The proportion of cases where text generation failed varies by property but remains below 0.2% for all properties. Therefore, it did not pose a significant concern. Statistical analyses, including the number of text tokens and the proportion of successfully generated texts, are detailed in the Table2.

## 2.3 Framework
CAST was trained in two stages, (1) MNP pretraining and (2) finetuning with MP data, as illustrated in Fig1. To embed each modality, we utilized a randomly initialized coGN[5] to generate node embeddings from the graph and MatSciBERT[29], pretrained on a large corpus of peer-reviewed materials science publications, to get text token embeddings.

### 2.3.1 Pretraining: Masked Node Prediction(MNP)
A subset of nodes in the graph is masked with a 50% probability, and the structure encoder processes the graph to generate embeddings for each node. Simultaneously, the corresponding text is passed through a text encoder to produce

token-level embeddings. The node embeddings(as queries) and the text token embeddings(as keys and values) interact through a cross-attention mechanism. This interaction allows the node embeddings to gather information from the text token embeddings through the cross-attention mechanism. As the model learns to predict the masked node's element type, it simultaneously aligns the node embeddings with the most relevant text tokens. This process enhances the model's ability to represent and utilize cross-modal relationships.

### 2.3.2 Finetuning
The pretrained model architecture is preserved, with the classification block replaced by a regression block to align with the predictive objective. By leveraging the structural and textual embeddings aligned during pretraining, the model is optimized to predict material properties with improved accuracy. This enhancement stems directly from the pretrained cross-modal understanding, which enables a more comprehensive integration of multimodal features.

## 2.4 Comparison of Predictive Performance
CAST was compared against unimodal models(coGN[5] and MatSciBERT[29]) and other multimodal methods, CrysMMNet(concatenation)[10] and MultiMat(pretrained with contrastive learning)[22]. In the original studies, CrysMMNet and MultiMat utilized different encoders for their respective architectures. However, to ensure a fair comparison of fusion methods, we standardized the encoders by using coGN as the structure encoder and MatSciBERT as the text encoder for training both models. In MultiMat, contrastive learning is originally conducted using four modalities, but in this study, we used only structure and text for training. While CrysMMNet originally froze the text encoder during training, we evaluated both the frozen approach and a fine-tuning approach using LoRA [30], a widely adopted technique for efficient model fine-tuning. Since the MatSciBERT was not pretrained for regression tasks, incorporating LoRA allowed us to explore and compare a broader range of multimodal scenarios within the concatenation framework. Our approach demonstrated the best performance in predicting three out of four properties, except for bulk modulus, where it achieved results only 0.001 lower than the best-performing method, CrysMMNet(LoRA fine-tuning), making it nearly equivalent in performance. Notably, the test MAE loss for total energy prediction was approximately 23% lower than that of the second best model, CrysMMNet(LoRA ft). Details on the implementation of each model are provided in the Method section. When comparing single-modality models, the text based MatSciBERT showed superior performance in predicting total energy, while coGN excelled in bandgap prediction. For modulus predictions, the performance of the two models was nearly identical. These results suggest that certain modalities are better suited for predicting specific properties, highlighting the importance for developing multimodal predictive models that leverage the strengths of multiple modalities.

Among multimodal approaches, the strong performance of CAST can be attributed to its ability to integrate information from both modalities in a fine-grained manner at the token level and to align the two modalities through pretraining. However, when comparing CAST (w/o pretraining) with other methods, it was observed that cross-attention alone was insufficient to achieve superior performance across all properties. In contrast, CAST with pretraining showed consistently improved predictive performance across all properties, outperforming both other methods and its w/o pretraining counterpart. Specifically, for bandgap prediction, most multimodal methods, including CAST (w/o pretraining), performed worse than the unimodal coGN. However, pretraining mitigated this issue, underscoring its critical role in multimodal learning. With CrysMMNet, fine-tuning with LoRA outperformed using a frozen language model for most properties, except for bandgap. This suggests that, since MatSciBERT was not optimized for property regression during pretraining, the addition of low-rank matrices through fine-tuning provided beneficial adjustments that improved performance. On the other hand, the MultiMat(pretrained with contrastive learning) approach negatively affected the parameters of the GNN during pretraining, resulting in degraded performance compared to the unimodal coGN model. In the case of the MultiMat paper, performance improved when different GNNs and text encoders were used. Further research is required to determine whether this improvement stems from changes in the dataset or the choice of encoders. The superior performance of the concatenation approach over contrastive learning suggests that leveraging both modalities directly together can have complementary effects. This is likely because, during fine-tuning, GNNs pretrained with contrastive learning do not directly utilize the text modality, limiting their ability to fully benefit from multimodal information.

## 2.5 Further analysis of pretraining effects
We conducted an analysis to investigate how pretraining contributed to the observed improvement in predictive performance. Using a test set example, we examined the attention maps generated by the cross-attention mechanism (Fig. 2). In the figure, the x-axis represents the text tokens acting as keys, while the y-axis corresponds to the query tokens. Each cell indicates the attention score, with brighter colors reflecting higher scores and stronger associations.

<table>
<thead>
  <tr>
    <th>Models</th>
    <th>Total Energy</th>
    <th>Bandgap</th>
    <th>log(Shear Modulus)</th>
    <th>log(Bulk Modulus)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>coGN</td>
    <td>0.673(0.118)</td>
    <td>0.381(0.006)</td>
    <td>0.091(0.006)</td>
    <td>0.050(0.001)</td>
  </tr>
  <tr>
    <td>MatSciBERT</td>
    <td>0.390(0.047)</td>
    <td>0.420(0.002)</td>
    <td>0.089(0.002)</td>
    <td>0.053(0.001)</td>
  </tr>
  <tr>
    <td>CrysMMNet(frozen LM)</td>
    <td>0.615(0.121)</td>
    <td>0.369(0.005)</td>
    <td>0.085(0.003)</td>
    <td>0.047(0.001)</td>
  </tr>
  <tr>
    <td>CrysMMNet(LoRA ft)</td>
    <td>0.332(0.056)</td>
    <td>0.416(0.005)</td>
    <td>0.073(0.004)</td>
    <td><b>0.038(0.001)</b></td>
  </tr>
  <tr>
    <td>MultiMat</td>
    <td>1.095(0.086)</td>
    <td>0.414(0.003)</td>
    <td>0.089(0.002)</td>
    <td>0.055(0.002)</td>
  </tr>
  <tr>
    <td>CAST(w/o pretraining)</td>
    <td>0.277(0.051)</td>
    <td>0.394(0.003)</td>
    <td>0.072(0.002)</td>
    <td>0.042(0.002)</td>
  </tr>
  <tr>
    <td>CAST(ours)</td>
    <td><b>0.256(0.045)</b></td>
    <td><b>0.354(0.002)</b></td>
    <td><b>0.069(0.001)</b></td>
    <td>0.039(0.0003)</td>
  </tr>
</tbody>
</table>

Table 1: This table shows the predictive performance of five models in terms of MAE. We tested using three different random seeds, with the mean values presented as numbers and the standard deviation values shown in parentheses. Bold text indicates the best-performing model. The second-highest performance is indicated with an underline. In the original studies, CrysMMNet and MultiMat utilized different encoders for their respective architectures. However, to ensure a fair comparison of fusion methods, we standardized the encoders by using coGN as the structure encoder and MatSciBERT as the text encoder for training both models. In MultiMat, contrastive learning is originally conducted using four modalities, but in this study, we used only structure and text for training.

![](./images/1096668319135563780_2.jpg)

Figure 2: A example of attention map To analyze whether the node tokens in the cross-attention heads effectively attend to diverse text tokens, we brought one example from the test set(mp-1963). In the case of CAST(w/o pretraining), we observed that node tokens tend to attend to a limited variety of text tokens, often assigning similar importance to the same tokens. This behavior frequently results in vertical linear patterns. In contrast, for the CAST(w/ pretraining), node tokens demonstrate a broader and more varied attention to different text tokens compared to the CAST(w/o pretraining). This indicates pretraining improved cross-modal interaction between modalities. Other examples can be seen in Supplementary Information.

The first row, labeled "CAST(w/o pretraining)", shows the attention maps extracted from CAST (w/o pretraining), whereas the second row, "CAST(w/ pretraining)", represents the attention maps obtained from CAST. In the "CAST(w/o pretraining)" case, we observed that all nodes predominantly attended to the same text tokens, resulting in stripe-like attention patterns. In contrast, the CAST(w/ pretraining) exhibited a more diverse attention distribution, where nodes attended to a broader range of text tokens rather than focusing on just a few. This indicates that pretraining enables the model to establish meaningful associations between node tokens and text tokens, allowing each query node to attend more diversely to relevant text tokens. Additional examples are provided in the Supplementary Information.

To generalize these observations, we analyzed the distribution of similarities in the attention maps between node tokens across the dataset(Fig 3). In the given example, the material is represented as a graph with four nodes (Al, Te, Te, Te). To quantify how diversely node tokens reference text tokens, we calculated the cosine similarity of attention values between all pairs of nodes (combinations). This analysis offers a quantitative measure of how pretraining enhances the diversity of text token references by node tokens. In the CAST(w/o pretraining), the similarities were predominantly concentrated near 1, indicating a high degree of focus that intensified as layers progressed. On the other hand, the pretrained model exhibited a wider distribution of similarities, with less severe concentration as layers deepened compared to the CAST(w/o pretraining).

These findings confirm that pretraining enables node tokens to reference a variety of text tokens, allowing them to gather more diverse and relevant information. This validates that the phenomenon observed in Fig 2 is not limited

![](./images/1096668319135563780_3.jpg)

![](./images/1096668319135563780_4.jpg)

Figure 3: **Distributions of similarities** To generalize these observations, we analyzed the distribution of similarities in the attention maps between node tokens across the dataset. Each row represents how a node token references text tokens. We calculated the cosine similarity of attention values between all pairs of nodes (combinations). In the CAST(w/o pretraining), the similarities were mostly concentrated near 1, with a high degree of focus that intensified as layers progressed. On the other hand, the CAST(w/ pretraining) exhibited a wider distribution of similarities, with less severe concentration as layers deepened compared to the from-scratch case. These findings indicate that pretraining enables node tokens to reference a variety of text tokens, allowing them to receive more relevant and diverse information. This diversity in information flow directly enhances the model's performance on downstream regression tasks, demonstrating the effectiveness of pretraining in improving the overall learning process.

to few examples but reflects an overall trend acrooss the dataset. The ability of node tokens to reference a diverse range of relevant text tokens demonstrates that the model has effectively captured the token-level relationships between modalities, ultimately contributing to improved downstream performance.

## 3 Conclusion

In this study, we proposed **CAST**(Cross Attention based multimodal fusion of Structure and Text), a multimodal learning framework for material property prediction that integrates structural and textual data at a fine-grained level. Through extensive experimentation, we demonstrated that our approach outperforms unimodal baselines(coGN and MatSciBERT) and other multimodal models(Concatenation and Contrastive learning) across multiple material property prediction tasks. Our results highlight the critical role of cross attention and pretraining in aligning structural and textual modalities. The Masked Node Prediction(MNP) pretraining strategy significantly improved the model's ability to align node tokens with their relevant text tokens, as evidenced by the diverse and meaningful attention patterns observed in the cross-attention maps. This alignment not only improved the accuracy of property predictions, particularly for challenging properties such as bandgap, but also contributed to the stability of the learning process, reducing performance variability across random seeds.

Despite these achievements, there are several areas where the framework could be further improved to enhance its applicability and efficiency. First, the reliance on language models for text encoding and attention mechanisms for modality fusion leads to increased computational costs, particularly as the number of tokens grows. This poses

challenges for scalability when dealing with datasets taht include significantly larger or more complex structural and textual modalities. Additionally, the framework is more sensitive to data quality compared to traditional unimodal materials datasets, because both modalities must be well-represented and paired. Lastly, the text encoder employed in this study is limited to processing only 512 tokens. Employing a text encoder capable of handling longer text sequences could further enhance performance, as demonstrated in previous research[31]. Addressing these limitations in future research could involve the development of more efficient fusion strategies, exploration of lightweight or advanced encoders, and application of the framework to more diverse multimodal datasets and a broader range of material properties.

## 4 Methods

### 4.1 Statistical analysis of data

The table presents a comprehensive summary of the dataset statistics for various material properties, including total energy, bandgap, the logarithm of shear modulus, and the logarithm of bulk modulus, along with their respective train, valid, and test splits. For each property, key characteristics of the graph and text representations are detailed, such as the mean and standard deviation of the number of graph nodes and text tokens. The text existence rate indicates the proportion of samples with successfully generated textual descriptions, with absolute counts provided in parentheses. Furthermore, the table reports the mean and standard deviation of the target property values, offering insights into the distributions within the dataset. These statistics underscore the variation in structural and textual complexities across properties and highlight the near-complete availability of text descriptions, enabling the seamless integration of multimodal information for predictive modeling tasks.

<table>
<thead>
<tr>
<th colspan="2">Total Energy</th>
<th colspan="2">Bandgap</th>
<th colspan="2">log(Shear Modulus)</th>
<th colspan="2">log(Bulk Modulus)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Data type</td>
<td>train val/test</td>
<td>train</td>
<td>val/test</td>
<td>train</td>
<td>val/test</td>
<td>train</td>
<td>val/test</td>
</tr>
<tr>
<td>Dataset size</td>
<td>91,520 22,878</td>
<td>52,371</td>
<td>12,996</td>
<td>7,513</td>
<td>1,910</td>
<td>7,513</td>
<td>1,910</td>
</tr>
<tr>
<td># of node mean(std)</td>
<td>17.28(28.59) 17.10(28.34)</td>
<td>22.95(34.95)</td>
<td>22.78(34.76)</td>
<td>3.67(2.03)</td>
<td>3.58(2.39)</td>
<td>3.67(2.03)</td>
<td>3.58(2.39)</td>
</tr>
<tr>
<td># of tokens mean(std)</td>
<td>1,796.65(3574.83) 1,783.56(3516.19)</td>
<td>2,326.0(4137.72)</td>
<td>2,323.2(4109.76)</td>
<td>250.83(272.62)</td>
<td>250.16(327.55)</td>
<td>250.83(272.62)</td>
<td>250.16(327.55)</td>
</tr>
<tr>
<td>Text existence rate</td>
<td>99.9%(91,437) 99.9%(22,855)</td>
<td>99.9%(52,298)</td>
<td>99.8%(12,974)</td>
<td>100%(7,513)</td>
<td>100%(1,910)</td>
<td>100%(7,513)</td>
<td>100%(1,910)</td>
</tr>
<tr>
<td>Y mean(std)</td>
<td>-9.14(7.22) -9.26(7.38)</td>
<td>2.17(1.54)</td>
<td>2.15(1.55)</td>
<td>1.54(0.39)</td>
<td>1.55(0.38)</td>
<td>1.87(0.38)</td>
<td>1.88(0.37)</td>
</tr>
</tbody>
</table>

Table 2: Statistical analysis of data The table provides a comprehensive summary of the dataset statistics across different material properties, including total energy, bandgap, logarithm of shear modulus, and logarithm of Bulk Modulus, as well as their respective data splits for train and val/test.

### 4.2 Encoders for each modality

#### 4.2.1 Structure Encoder : coGN

By leveraging the inherent symmetry of crystals, coGN [5] employs an asymmetric unit cell representation to reduce the number of graph nodes, thereby improving computational efficiency. The proposed Nested Line Graph Network (NLGN) architecture further enhances the GNN framework through optimized message passing. This approach has demonstrated superior performance across most tasks within the MatBench benchmark dataset [28]. Key factors contributing to these performance improvements include optimized connectivity and enriched message-passing capabilities. The methods introduced by coGN are broadly applicable for modeling crystal structures, providing a systematic framework for comparing and designing diverse GNN architectures. Given its state-of-the-art (SOTA) performance on MatBench and computational efficiency, coGN is considered to have robust encoding capabilities, making it an ideal choice as the GNN encoder for our work.

#### 4.2.2 Text Encoder: MatSciBERT

MatSciBERT[29] is a domain-specific language model designed for materials science, trained on a large corpus of peer-reviewed materials science publications. It excels at information extraction tasks by effectively interpreting the unique notations and terminology prevalent in materials science literature. Evaluations on tasks related to materials such as abstract classification, named entity recognition, and relation extraction have demonstrated that MatSciBERT outperforms general scientific language models, such as SciBERT. The pretrained and fine-tuned models are publicly available, serving as a valuable resource for the materials science community. We hypothesize that leveraging a model with a deep understanding of materials science will significantly enhance predictive performance. Therefore, we adopted MatSciBERT as the text encoder in our framework.

### 4.3 Multimodal fusion methods

We compared regression performance using three approaches: concatenation, contrastive learning-based pretraining, and CAST(cross attention). Among these, CAST demonstrated the best prediction performance across four properties. While concatenation and contrastive learning utilize instance-level multimodal features, CAST leverages token-level features. To ensure a fair comparison, we standardized the training hyperparameters across all methods.

For training, we employed a periodic cosine scheduling strategy to adjust the learning rate. To enhance training stability, we included a warm-up phase for the initial 1,000 steps. For contrastive learning pretraining, we set the batch size to 360, following the configuration used in the MultiMat paper[22], as larger batch sizes are more efficient for this approach. For other pretraining task and regression tasks, a batch size of 64 was used.

For consistency, we employed coGN[5] and MatSciBERT[29] as the structure and text encoders across all methods. Accordingly, the feature dimensions of node tokens and text tokens were set to 128 and 768, respectively.

### 4.3.1 CAST(proposed method)

CAST, based on cross-attention, follows a two-step process: pretraining and finetuning. Unlike previous studies [10, 22, 11] in the materials domain that focused on multimodal fusion at the instance level, we hypothesize that token-level fusion can achieve superior performance. To enable interaction at the token level, we employ the cross-attention mechanism of transformer models [23].

During the pretraining phase, a subset of graph nodes is randomly masked with a 50% probability. The structure encoder processes the graph to generate embeddings for each node, while the corresponding text is passed through a text encoder to produce token-level embeddings. These embeddings interact through a cross-attention mechanism, where the node embeddings serve as queries, and the text token embeddings act as keys and values. This interaction allows the node embeddings to incorporate contextual information from the text. As the model learns to predict the element types of the masked nodes, it simultaneously aligns node embeddings with the most relevant text tokens. The fusion module consists of four cross attention layers with eight attention heads, each with an attention dimension of 128. The classification block is a single linear layer.

Following the pretraining phase, the model undergoes a finetuning stage specifically designed for property prediction tasks. In this phase, the pretrained model is preserved, but the classification block is replaced with a regression block, also a single linear layer, to align with the predictive objective. By leveraging the structural and textual embeddings aligned during pretraining, the model is optimized to predict material properties with heightened accuracy. This improvement stems from the pretrained cross-modal understanding, which facilitates a more comprehensive integration of multimodal features. As shown in Table 2.4, our method demonstrates more stable and accurate predictive performance compared to other multimodal approaches and unimodal models.

### 4.3.2 Concatenation(CrysMMNet)

CrysMMNet[10], to the best of our knowledge, is the first approach to leverage multimodal learning for material property prediction. Their model employs ALIGNN as the structure encoder and MatSciBERT as the text encoder. In this framework, the graph structure is processed through a graph encoder to generate graph embeddings, while textual descriptions are passed through a text encoder and a projection layer to produce text embeddings. These representations are then fused to jointly model the input modalities and predict crystal properties. Notably, the text encoder is frozen during training in their method, and the study does not evaluate the model's performance when the text encoder is not frozen. To address this gap, we conducted additional experiments, comparing the performance of the Concat method with a frozen language model (LM) and with LoRA fine-tuning. The results of these experiments are presented in Table 2.4.

### 4.3.3 Contrastive Learning(MultiMat)

In MultiMat, contrastive learning between multimodal representations is utilized to pretrain the structure encoder, similar to the approach used in CLIP[21]. Their study reported that applying the pretrained graph encoder to downstream tasks improves performance compared to training from scratch. MultiMat leverages four modalities—crystal structures, density of states (DOS), and charge density, whereas our study focuses on comparing different modality fusion strategies. To ensure a fair comparison with other methods, we pretrained the model using only structural information and textual descriptions. Furthermore, while MultiMat utilizes PotNet [32] as the structure encoder and MatBERT [33] as the text encoder, we adapted the model by employing the coGN structure encoder and MatSciBERT text encoder. This alignment with the configurations of other methods ensures consistent evaluation across models.


## References

[1] Tian Xie and Jeffrey C Grossman. Crystal graph convolutional neural networks for an accurate and interpretable prediction of material properties. *Physical review letters*, 120(14):145301, 2018.

[2] Johannes Gasteiger, Janek Groß, and Stephan Günnemann. Directional message passing for molecular graphs. *arXiv preprint arXiv:2003.03123*, 2020.

[3] Johannes Gasteiger, Florian Becker, and Stephan Günnemann. Gemnet: Universal directional graph neural networks for molecules. *Advances in Neural Information Processing Systems*, 34:6790-6802, 2021.

[4] Kamal Choudhary and Brian DeCost. Atomistic line graph neural network for improved materials property predictions. *npj Computational Materials*, 7(1):185, 2021.

[5] Robin Ruff, Patrick Reiser, Jan Stühmer, and Pascal Friederich. Connectivity optimized nested line graph networks for crystal structures. *Digital Discovery*, 3(3):594-601, 2024.

[6] Amil Merchant, Simon Batzner, Samuel S Schoenholz, Muratahan Aykol, Gowoon Cheon, and Ekin Dogus Cubuk. Scaling deep learning for materials discovery. *Nature*, 624(7990):80-85, 2023.

[7] Xiao Wang, Guangyao Chen, Guangwu Qian, Pengcheng Gao, Xiao-Yong Wei, Yaowei Wang, Yonghong Tian, and Wen Gao. Large-scale multi-modal pre-trained models: A comprehensive survey. *Machine Intelligence Research*, 20(4):447-482, 2023.

[8] Peng Xu, Xiatian Zhu, and David A Clifton. Multimodal learning with transformers: A survey. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 45(10):12113-12132, 2023.

[9] Sungjin Park, Seongsu Bae, Jiho Kim, Tackeun Kim, and Edward Choi. Graph-text multi-modal pre-training for medical representation learning. In *Conference on Health, Inference, and Learning*, pages 261-281. PMLR, 2022.

[10] Kishalay Das, Pawan Goyal, Seung-Cheol Lee, Satadeep Bhattacharjee, and Niloy Ganguly. Crysmmnet: multimodal representation for crystal property prediction. In *Uncertainty in Artificial Intelligence*, pages 507-517. PMLR, 2023.

[11] Mrigi Munjal, Jaewan Lee, Changyoung Park, and Sehui Han. Lattice lingo: Effect of textual detail on multimodal learning for property prediction of crystals. *arXiv preprint arXiv:2412.04670*, 2024.

[12] Keisuke Ozawa, Teppei Suzuki, Shunsuke Tonogai, and Tomoya Itakura. Graph-text contrastive learning of inorganic crystal structure toward a foundation model of inorganic materials. *Science and Technology of Advanced Materials: Methods*, (just-accepted):2406219, 2024.

[13] Janghoon Ock, Joseph Montoya, Daniel Schweigert, Linda Hung, Santosh K Suram, and Weike Ye. Unimat: Unifying materials embeddings through multi-modal learning. *arXiv preprint arXiv:2411.08664*, 2024.

[14] Jaewan Lee, Changyoung Park, Hongjun Yang, Sehui Han, and Woohyung Lim. Clcs: Contrastive learning between compositions and structures for practical li-ion battery electrodes design. In *AI for Accelerated Materials Design-NeurIPS 2023 Workshop*.

[15] Alex M Ganose and Anubhav Jain. Robocrystallographer: automated crystal structure text descriptions and analysis. *MRS Communications*, 9(3):874-881, 2019.

[16] Hao Hao Tan and Mohit Bansal. Lxmert: Learning cross-modality encoder representations from transformers. In *Conference on Empirical Methods in Natural Language Processing*, 2019.

[17] Junnan Li, Dongxu Li, Caiming Xiong, and Steven C. H. Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In *International Conference on Machine Learning*, 2022.

[18] Junnan Li, Dongxu Li, Silvio Savarese, and Steven C. H. Hoi. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. In *International Conference on Machine Learning*, 2023.

[19] Xiaokang Peng, Yake Wei, Andong Deng, Dong Wang, and Di Hu. Balanced multimodal learning via on-the-fly gradient modulation. *2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, pages 8228-8237, 2022.

[20] Xiaohui Zhang, Jaehong Yoon, Mohit Bansal, and Huaxiu Yao. Multimodal representation learning by alternating unimodal adaptation. *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, pages 27446-27456, 2023.


[21] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In *International conference on machine learning*, pages 8748–8763. PMLR, 2021.

[22] Viggo Moro, Charlotte Loh, Rumen Dangovski, Ali Ghorashi, Andrew Ma, Zhuo Chen, Samuel Kim, Peter Y. Lu, Thomas Christensen, and Marin Soljačić. Multimodal learning for materials, 2024.

[23] A Vaswani. Attention is all you need. *Advances in Neural Information Processing Systems*, 2017.

[24] Alec Radford. Improving language understanding by generative pre-training. 2018.

[25] Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of naacL-HLT*, volume 1, page 2. Minneapolis, Minnesota, 2019.

[26] Yinhan Liu. Roberta: A robustly optimized bert pretraining approach. *arXiv preprint arXiv:1907.11692*, 364, 2019.

[27] Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek, Shreyas Cholia, Dan Gunter, David Skinner, Gerbrand Ceder, et al. Commentary: The materials project: A materials genome approach to accelerating materials innovation. *APL materials*, 1(1), 2013.

[28] Alexander Dunn, Qi Wang, Alex Ganose, Daniel Dopp, and Anubhav Jain. Benchmarking materials property prediction methods: the matbench test set and automatminer reference algorithm. *npj Computational Materials*, 6(1):138, 2020.

[29] Tanishq Gupta, Mohd Zaki, NM Anoop Krishnan, and Mausam. Matscibert: A materials domain language model for text mining and information extraction. *npj Computational Materials*, 8(1):102, 2022.

[30] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models. *arXiv preprint arXiv:2106.09685*, 2021.

[31] Nawaf Alampara, Santiago Miret, and Kevin Maik Jablonka. Mattext: Do language models need more than text & scale for materials modeling? *arXiv preprint arXiv:2406.17295*, 2024.

[32] Yuchao Lin, Keqiang Yan, Youzhi Luo, Yi Liu, Xiaoning Qian, and Shuiwang Ji. Efficient approximations of complete interatomic potentials for crystal property prediction. In *International Conference on Machine Learning*, pages 21260–21287. PMLR, 2023.

[33] Nicholas Walker, Amalie Trewartha, Haoyan Huo, Sanghoon Lee, Kevin Cruse, John Dagdelen, Alexander Dunn, Kristin Persson, Gerbrand Ceder, and Anubhav Jain. The impact of domain-specific pre-training on named entity recognition tasks in materials science. *Available at SSRN 3950755*, 2021.