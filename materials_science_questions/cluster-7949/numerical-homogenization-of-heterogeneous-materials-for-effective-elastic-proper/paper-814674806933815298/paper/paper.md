# 形状記憶ポリマの温度・ひずみ履歴依存性を表現できるマイクロメカニカルモデル
丹羽 勇太*1, 池田 忠繁*2, 仙場 淳彦*2

## Micromechanical model of shape memory polymer including temperature-strain history dependence
Yuta NIWA $^{* 1}$, Tadashige IKEDA $^{* 2}$ and Atsuhiko SENBA $^{* 2}$

*1 Graduate School of Engineering, Nagoya University
Furo-cho, Chikusa-ku, Nagoya 464-8603, Japan
*2 Nagoya University
Furo-cho, Chikusa-ku, Nagoya 464-8603, Japan

Received 25 February 2014

## Abstract
Shape memory polymers (SMPs) have thermomechanical property drastically altering around the glass-transition temperature ($T_{\text{g}}$), temporary shape fixity and shape recovery property, and so on. To understand the mechanisms of such unique properties and design products including SMPs optimally, a mathematical model which is simple yet can represent these properties reasonably and accurately is necessary. Especially, it is important for the model to be able to consider the effect of temperature and strain history on the properties because the properties are considered to depend on not only the temperature and the strain themselves but also their history. Therefore, in this paper first the effect of the temperature and strain history on the shape fixity and shape recovery properties was examined. Then, a micromechanical model of SMP was developed to describe this effect. This model consisted of a lot of unit elements having four springs, two dash pots, one latch, and one thermal expansion element. Different $T_{\text{g}}$ was assigned to each element because $T_{\text{g}}$ depends on local condition inside of SMP and distributed in general. It was found from the experiment that the temperature and strain history applied to SMP when the shape is gradually frozen has an influence on the shape recovery process. With respect to the model, it was shown that the proposed micromechanical model can capture the thermomechanical behaviors of SMP and, especially, the temperature and strain histories dependence on the shape recovery process quite well.

## Key words : Shape memory polymer, Shape memory materials, Phase transformation, Constitutive equation, Inelasticity, Visco elasticity, Micromechanical model, Thermomechanical property

---

## 1. 序 論
近年, 研究開発, 実用化が盛んに行われている機能性材料の一つに形状記憶ポリマ(Shape Memory Polymer,以下 SMP,がある. SMP は材料固有のガラス転移温度(Glass-transition Temperature, 以下 $T_{\text{g}}$) 周辺で力学的特性が大きく変化する材料である. この SMP は, $T_{\text{g}}$ 以上の高温ではゴムのようにやわらかい状態(以下ゴム状態)となり, $T_{\text{g}}$ 未満の低温ではガラスのようにかたい状態(以下ガラス状態)となる. また, 形状固定性, 形状回復性と呼ばれる性質を持つことが特徴である. ここで, 形状固定性とは, ゴム状態である形状に保持された SMPがガラス状態に冷却されると, その形状が一時的な形状として固定される性質である. また, 形状回復性とは,その固定された形状を持つSMPが, 再度ゴム状態まで加熱される時に, 形状が固定される前の元の形状へ回復

---
No.14-00107 [DOI: 10.1299/transjsme.2014smm0310]
*1 名古屋大学大学院 工学研究科(〒464-8603 愛知県名古屋市千種区不老町)
*2 正員, 名古屋大学
E-mail of corresponding author: ikeda@nuae.nagoya-u.ac.jp

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

する性質である. これらの性質を有するため, SMPは航空宇宙 (Lin, et al., 2006; Sokolowski, et al., 1999; Sofla, et al., 2010), 医療 (Sokolowski, et al., 2007; Gall, et al., 2005), 生活関連 (林, 2012) などの様々な分野において応用または応用のための研究がなされている. また, 近年のSMP材料に関する研究として, SMPを複合材料の母材として利用する形状記憶複合材料に関する研究 (Madbouly and Lendlein, 2010) や, 異なる $T_g$ を持つSMPを組み合わせることで, 2種類以上の形状固定, 形状回復を行う研究 (Xie, et al., 2009), 単一の $T_g$ を持つSMPに対して2種類以上の形状固定, 形状回復を行う研究 (Xie, 2010; Li and Xie, 2011) などが挙げられる.

SMPの特徴の熱力学的な解釈や, SMPを応用した製品を最適設計するためには, それらの物理現象を精度良く表すことができる数学モデルが必要であり, これまでにもいくつかのモデルが提案されている. 戸伏ら(1998)は2つのバネ素子と1つの減衰素子から構成される標準線形モデルと呼ばれる粘弾性モデルに, 1つの滑り素子を加えた4つの素子から成り立つモデルを提案した. このモデルでは, 各材料定数に加えて, 滑り素子によって引張り後に残留するひずみを温度に依存する関数として定義し, ゴム状態とガラス状態での力学的特性に加え,形状固定性, 形状回復性を表現した. さらに戸伏ら (2000) はこのモデルに非線形項を加えることにより, SMPの非線形挙動が現れる大きな変形に対して適用可能なモデルも提案した. Liuら (2006) は, SMPのガラス状態とゴム状態を微視的に見たとき, 炭素-炭素結合の立体配座に関する動きがガラス状態では制限され, ゴム状態では自由であるという考えに基づき, それぞれの結合から構成される成分をFrozen phase (ガラス相), Active phase (ゴム相) として定義し, 体積分率を用いた三次元モデルを提案した. このモデルはひずみ一定で冷却, 加熱した時の応力の応答予測などに対して適用され, 計算と実験は良い一致を示した. ポリウレタン系形状記憶ポリマは, 温度に依存しfrozen phase (ガラス相) またはactive phase (ゴム相) となる比較的柔軟なsoft segment (柔軟部分) と温度に依存せず剛直なhard segment (剛直部分) から構成され, soft segmentとhard segmentの割合が形状記憶ポリマの基本特性に影響を与える. そこで, Kimら (2010) は超弾性モデルで表現したFrozen soft segment phaseおよびActive soft segment phaseの他に粘弾性モデルで表現したHard segment phaseを導入した3-phaseモデルを提案した.このモデルにより $T_g$ 前後の温度に対する応力-ひずみ関係を $50\%$ ひずみまで定性的に表現することができた. Westbrookら (2011) は, 1つのバネ素子とガラス状態を表現する1つのバネ素子と1つの減衰素子を直列に並べたMaxwell素子, ゴム状態を表現する複数のMaxwell素子から構成される一次元並列モデルを提案した. このモデルは, 減衰係数を温度の関数とし, 弾性率と減衰係数の異なる複数の素子を組み合わせることで,複雑な形状記憶ポリマの特性を表すことができた. また, Westbrookらのモデルは, 陰に複数の形状固定, 形状回復表現が可能となっており, Yuら (2012) は, このモデルを用いて, Liら (2011) やXie (2010) の行った複数の形状固定, 形状回復の実験結果を精度よく表現することができた.

このように, SMPの数学モデルは構成の異なる様々なものが考案されてきている. 既存の多くのモデルでは今回提案するモデルとは異なり, 1つの数学モデルが扱うサイズが試験片全体のように大きく, 材料内部のミクロな結晶方向, 応力や温度の分布により材料全体の $T_g$ がある程度の分布を持つと考えている. このため, 形状固定過程において固定されるひずみの量や固定されたひずみの回復量を温度の関数などとして決めることが多く, 形状回復挙動に対する形状固定過程の温度履歴, ひずみ履歴の影響を十分に表現できない. 実際には形状固定過程においてある温度で固定されるひずみの量が固定されたひずみのある温度での回復量と関係があると考えられるが, これまでに提案されているモデルはそれらの関係を陽には考慮していない. しかしながら, もし形状固定過程における温度履歴, ひずみ履歴が形状回復挙動に影響を与えるのであれば, SMPを応用した製品の設計においてその影響を考慮することは重要である. 特にSMPをアクチュエータとして応用する場合は, 形状固定および形状回復の過程がいつも同じとは限らないので, 状態の履歴依存を知る必要がある.

そこで, 本研究では, まず, 形状固定過程における温度履歴, ひずみ履歴が形状回復挙動に影響を与えていることを実験的に明らかにし, 次にこの結果を踏まえ, このような現象を表現可能な数学モデルを構築し, 数学モデルによる試験の再現結果と試験結果との比較によりモデルの妥当性を評価することを目的とする.

## 2. 実験方法

本研究では, 引張り, 冷却による形状固定過程とその後の除荷過程, 加熱による形状回復過程を繰り返す熱力学サイクル試験を行った. 熱力学サイクル試験では恒温槽付き疲労試験機 (株式会社島津製作所製

EHF-FB10KN-10LA (疲労試験機), TCR1-200 (恒温槽)) を用いた. また, 試験にはシート状のポリウレタン系SMP (株式会社SMPテクノロジーズ製MM-2520) を試験片として使用した.

図1は熱力学サイクル試験における試験片取付け後の模式図を表す. 試験中は恒温槽による温度制御を行い,荷重の無い状態で加熱する形状回復過程を除き, ひずみ速度一定の下で, 試験機のアームの移動を制御した. 取得したデータは試験機アームの変位, ロードセルによって検出される荷重, 試験片の温度である. ここで, 試験片に直接熱電対を貼り付けると試験片の変形挙動に影響を与えると考え, 感温部を実験に使用するものと同一のSMPで被覆した熱電対を試験片近くに配置し, その熱電対で測定される温度を試験片の温度とした. 熱力学サイクル試験では温度履歴, ひずみ履歴の異なる2種類の条件に対して試験を行うことで, SMPの形状固定性, 形状回復性を評価した. この2つの試験条件をそれぞれEXP1, EXP2とする. また, これらの試験結果は, 提案するモデルに利用する材料定数の取得, およびモデルによる計算結果との比較によるモデルの妥当性評価に用いた.
試験には評価部長さ60 mm, 幅10 mm, 厚さ0.5 mmの短冊形の試験片を用い, EXP1, EXP2のどちらにおいても試験中の最高温度は50 ℃,最低温度は0 ℃,加熱および冷却時の温度こう配は2 ℃/min,最大ひずみは10%,引張りおよび除荷時のひずみ速度は1%/minとした. また, EXP1, EXP2のどちらの試験においても, 温度50 ℃の下で20%のひずみを与え, その後除荷を行うトレーニング処理を3回実施した. ここで, トレーニング処理とは試験片にあらかじめひずみを与え, 加熱するという過程のことを指し, 安定した繰返し特性を得る方法として有効である(戸伏他,1996). トレーニング処理における設定温度はサイクル試験における最高温度とし, ひずみ量はサイクル試験中に試験片が経験する最大ひずみよりも大きくなるように設定した. また, EXP1では全てのひずみが単一の温度で与えられ, EXP2では冷却と引張りを交互に繰り返すことで, ひずみが与えられる温度を段階的に変化させている. これらEXP1, EXP2の形状固定過程の温度履歴, ひずみ履歴を図2に示す. この後の手順はEXP1, EXP2で共通であり, 最低温度である0 ℃で除荷を行い, その後加熱することで形状回復を行う.

![](./images/814674806933815298_1.jpg)

Fig. 1 Experimental setup of the thermomechanical cyclic test and the creep test. The experimental setup was comprised of a fatigue test machine, a thermostatic chamber, a controller, a computer for data acquisition, and so on. Load, stroke, and temperature were measured during the tests.

![](./images/814674806933815298_2.jpg)

(a) EXP 1

![](./images/814674806933815298_3.jpg)

(b) EXP 2

Fig. 2 Temperature and strain history during the shape fixation procedure in the thermomechanical cyclic tests. Blue line and red line represent strain and temperature, respectively. In EXP1 the shape fixation was performed at $50\ ^\circ$C and in EXP2 it was performed while the specimen was stretched and cooled in stages.

### 3. 実験結果
図3および図4はそれぞれ, EXP1, EXP2の応力 - ひずみ線図, 温度 - ひずみ線図を表す. ここで, 図3のEXP1の応力 - ひずみ線図の点A～Dは5章で参照する. EXP1の応力 - ひずみ線図を見ると, 10%まで引っ張った後応力緩和が発生し, その後ひずみを固定し冷却すると, 熱収縮による熱応力が発生することと, 試験片が剛性の低いゴム状態から剛性の高いガラス状態に変化することにより, 応力が増大する. 温度 - ひずみ線図を見ると, 除荷後には冷却過程において試験片がゴム状態からガラス状態に変化するときに形状固定されたひずみが固定ひずみとして残留し, 固定ひずみの最大ひずみに対する割合をひずみ固定率として定義するとEXP1のひずみ固定率は96.4%である. また, その後の加熱過程においてSMPは引張過程前の形状を回復するが, 試験片が$50\ ^\circ$Cまで加熱された時点では形状回復が完了していないことが確認できる. この原因としては試験片の試験機クランプ付近の部分が温められづらく,熱電対で測定した温度よりも時間をかけて温度が上昇していることが考えられる.一方, EXP2の応力 - ひずみ線図を見ると, $10\ ^\circ$Cでの引張過程であるひずみ6～8%部分と$0\ ^\circ$Cでの引張過程であるひずみ8～10%部分で引張りによる応力の増大が大きくなっており,試験片がゴム状態からガラス状態に変化することでより高剛性の力学的特性を示していることがわかる. 温度 - ひずみ線図を見ると, EXP1に比べて固定ひずみが小さく, ひずみ固定率は81.3%である. また, $50\ ^\circ$Cまで加熱された時点で形状回復が完了していることが確認できる. これらの理由としては, EXP2では段階的な引張り, 冷却を行っていることが考えられる. SMP内部で$T_g$が分布していると考えられる場合, 段階的な引張り, 冷却によって, 比較的高温で既にガラス状態となった成分は, その後の引張り, 冷却過程では, さらにゴムのように伸びたり, そのひずみが固定されたりしない. 従って, 高温で全ての成分が最大ひずみまで引っ張られた後に冷却されるEXP1に比べて除荷直前の10%ひずみに対する応力値が大きくなるので,除荷により弾性変形分が回復した後のEXP2における試験片全体の固定ひずみは小さくなると考えられる. また, 高温でゴム状態からガラス状態へ変化する成分の固定ひずみも, EXP2ではEXP1よりも小さいと考えられる. 高温でゴム状態からガラス状態に変化する成分は, ガラス状態からゴム状態に変化する温度も高いと仮定しているので, 試験機クランプ付近の部分が温まりづらい場合, 回復が遅れる成分のひずみの量はEXP2ではEXP1より小さくなり, クランプの影響が現れづらいと考えられる.

次に, 固定ひずみに対する加熱過程におけるひずみの割合である残留固定ひずみ率について比較する. 図5は加熱過程におけるEXP1, EXP2の残留固定ひずみ率を示す. この図より, EXP2ではEXP1に比べて低温の段階での残留固定ひずみ率の変化が大きいことが確認できる. この結果は先述のひずみ固定率の考察と同様に, 形状固定過程におけるひずみの与え方によって説明できる. 段階的な引張り, 冷却を行う場合は, 低い温度で固定された成分のひずみは,高い温度で固定された成分のひずみと比べ大きな引張り力により変形したものであるので,より大きな固定ひずみを有している. 従って, 全体が同じ引張り力で変形固定されたEXP1に比べて, EXP2では低温で相対的により大きな変形をすると考えられる.

Niwa, Ikeda and Senba, Transactions of the JSME (in Japanese), Vol.80, No.819 (2014)

![](./images/814674806933815298_4.jpg)

Fig. 3 Stress-strain diagram and temperature-strain diagram of EXP1 for the thermomechanical cyclic test. Arrowed lines mean the processes of the test.

![](./images/814674806933815298_5.jpg)

Fig. 4 Stress-strain diagram and temperature-strain diagram of EXP2 for the thermomechanical cyclic test. Arrowed lines mean the processes of the test.

![](./images/814674806933815298_6.jpg)

Fig. 5 Comparison in residual fixed strain ratio during the shape recovery process between EXP1 and EXP2. Red curve and blue curve represent the residual fixed strain ratio for EXP1 and EXP2, respectively. The difference in the shape fixation procedure between EXP1 and EXP2 causes the difference in the shape recovery behavior.

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

## 4. 数学モデル

図6に示すように, SMPは一般に形状固定, 形状回復に関与する柔軟部分 (Soft domain) と関与しない剛直部分 (Hard domains) から構成される (入江, 2000). 柔軟部分は比較的自由に変形可能で, 高温でゴム状態, 低温でガラス状態となる非晶性部 (Amorphous phase) と高温で融解する結晶性部 (Crystalline phase) から構成され, ガラス状態とゴム状態の間または結晶融解状態と結晶状態の間の可逆変化により形状記憶特性が現れると考えられている. 剛直部分は架橋点であったり, 非晶性部と結晶性部から構成されていたりするが, 後者の場合でも, 柔軟部分の非晶性部と結晶性部とは組成が異なり, $T_g$や融点が高く, 形状固定, 形状回復を行う温度範囲では相転移しない. 実験に用いたようなポリウレタン系のSMPでは, 剛直部分は結晶性, 柔軟部分は非晶性が顕著に表れるように設計されており, 板状の剛直部分が放射状に配列し球晶を形成し, 柔軟部分は放射状に配列した剛直部分の間や球晶の周辺に存在している構造が観察されている (Takahashi, et al., 1996). ここで, SMP内部を比較的小さな無数の領域 (要素) に分けると, その領域毎に剛直部分や柔軟部分の結晶性部などの方向や周囲の影響などにより, 領域内部の状態が異なり, 巨視的な座標系から見た熱力学的材料定数は異なると考えられる. そこで, ここでは, 材料をこれらの微小要素の集合として考え, 各微小要素を1つの要素モデルで表し, 材料全体にわたりそれらの平均化をすることで, 材料全体の挙動を表すマイクロメカニカルモデルを用いる. マイクロメカニカルモデルにおいては, 各要素の固定ひずみは個々に計算されるため, 形状固定過程の温度履歴, ひずみ履歴の違いによる固定ひずみ, 形状回復過程の変化の表現が可能となる. 結晶性部が融解した場合は, 冷却条件により結晶性部の割合が変化し, そのことが力学特性に影響を与えるが, 本研究における温度範囲では, 結晶性部は融解せずその割合も変化しないと仮定する. すなわち, 力学特性は温度に関しては$T_g$にのみ影響を受けると仮定する. 微小要素モデルとしては, 図6に示されるような, 4つのバネ素子と2つの減衰素子, 1つのかけがね素子, 1つの熱膨張素子から成り立つ8素子モデルを採用する. ここで, かけがね素子とは, $T_g$以上の温度領域では自由な変形が可能であり, $T_g$未満の温度領域では完全に固定され, 変形が不可能な素子を表す. この8素子モデルは要素の温度$T$が$T_g$以上であるか, $T_g$未満であるかに応じて値が変化する材料定数$E_1,E_2,\mu_1$とかけがね素子の作用によって, SMPの形状固定および形状回復の表現を行う. 各要素に作用する応力は等しく, 全体のひずみは各要素のひずみの平均値で与えられると仮定すると, このマイクロメカニカルモデルにおけるある1つの要素の応力とひずみの関係式は式 (1) で与えられる.

$$
\left.
\begin{matrix}
\text{For } T < T_g, \
\varepsilon_{\text{fixed}} = \text{const.} \
\dot{\varepsilon} = \frac{\dot{\sigma}}{E_{\text{g1}}} + \frac{E_{\text{g1}} + E_{\text{g2}}}{E_{\text{g1}}\mu_{\text{g1}}} \sigma - \frac{E_{\text{g2}}}{\mu_{\text{g1}}} (\varepsilon - \varepsilon_{\text{fixed}} - \varepsilon_{\text{T}}) + \dot{\varepsilon}_{\text{T}} \
\text{For } T \geq T_g, \
\varepsilon_{\text{fixed}} = \varepsilon_3 + \varepsilon_4 \
\dot{\varepsilon} = \frac{\dot{\sigma}}{E_{\text{r1}}} + \frac{E_{\text{r1}} + E_{\text{r2}}}{E_{\text{r1}}\mu_{\text{r1}}} \sigma - \frac{E_{\text{r2}}}{\mu_{\text{r1}}} (\varepsilon - \varepsilon_{\text{fixed}} - \varepsilon_{\text{T}}) + \frac{\dot{\sigma}}{E_{\text{r3}}} + \frac{E_{\text{r3}} + E_{\text{r4}}}{E_{\text{r3}}\mu_{\text{r2}}} \sigma - \frac{E_{\text{r4}}}{\mu_{\text{r2}}} \varepsilon_{\text{fixed}} + \dot{\varepsilon}_{\text{T}}
\end{matrix}
\right\} \quad (1)
$$

ここで, $T,\sigma,\varepsilon,E,\mu$はそれぞれ温度, 応力, ひずみ, ヤング率, 粘性係数を表す. また, $\varepsilon_{\text{fixed}}$は$T_g$以上の温度でゴム状態のSMPが冷却され$T_g$になったときガラス状態となり固定されるひずみ,$\varepsilon_{\text{T}} = \alpha(T - T_0)$は熱膨張によるひずみ, $T_0$は初期温度を表し, 添字g,rはそれぞれ微小要素が$T_g$未満のガラス状態であること, $T_g$以上のゴム状態であることを表す. 下添字1, 2, 3, 4は材料定数が図6の8素子モデルのどの素子のものかを示す.

![](./images/814674806933815298_7.jpg)

Fig. 6 Concept of the micromechanical model with an 8-element model. SMP is assumed to be comprised of hard domains and soft domain. The soft domain consists of amorphous phase and crystalline phase. The specimen is divided into thousands of microscopic regions and the region is approximated by an 8-element model.

## 5. 材料定数

マイクロメカニカルモデルにおいて利用する材料定数は, 熱力学サイクル試験のEXP1とクリープ試験および線膨張係数測定試験の実験結果を用いて求めた. クリープ試験では恒温槽付き疲労試験機(株式会社島津製作所製EHF-FB10KN-10LA (疲労試験機), TCR1-200 (恒温槽)) を用い, 線膨張係数測定試験では熱機械測定装置(株式会社TA instruments製Q400)を用いた.

クリープ試験の試験機システムの模式図は図1と同様である. 試験機のアームの制御方法は荷重制御であり,取得したデータについては熱力学サイクル試験と同様である. 本試験では, 温度の異なる2種類の条件に対して試験を行うことで,ゴム状態とガラス状態のSMPのクリープ特性を評価した.この2つの試験条件をEXP3, EXP4とする. また, これらの試験結果も, 提案するモデルに利用する材料定数の取得に用いた. 試験には評価部長さ60 mm, 幅 10 mm, 厚さ 0.5 mm の短冊形の試験片を用いた. EXP3 では温度 $50^{\circ} C$ 一定の下で, 1 MPa の応力を 4時間負荷した後除荷を行った. EXP4 では温度 $0^{\circ} C$ 一定の下で, 5 MPa の応力を 4 時間負荷した後除荷を行った.また, EXP3, EXP4 のどちらの試験においても, 試験前に温度 $50^{\circ} C$ の下で $20 \%$ のひずみを与え, その後除荷を行うトレーニング処理を3回実施した. 図7はクリープ試験の結果を表し, SMPには一定の応力を負荷した場合に非常に短い時間で発生する弾性的なひずみと, 時間に依存して大きくなるひずみがあることがわかる. 時間に依存して大きくなるひずみとしては粘性によるひずみと塑性ひずみが考えられる. また, 低温での試験EXP4ではEXP3に比べてより大きな応力を負荷しているが, ひずみはEXP3に比べて小さく, ガラス状態のSMPがゴム状態のときに比べて高剛性の力学的特性を示すことが確認できる.

線膨張係数計測試験では, SMPの加熱, 冷却を繰り返し, その時の寸法変化を計測することで線膨張係数を算出した. 試験には一辺 5 mm, 厚さ 0.5 mm の正方形の試験片を用いた. 試験中の最高温度は $60^{\circ} C$ , 最低温度は $-10^{\circ} C$ とし,熱力学サイクル試験の温度範囲を含むように設定した.加熱および冷却時の温度こう配は $5^{\circ} C / min$ ,試験中に試験片に負荷する荷重は0.01 Nとした. 図8は線膨張係数測定試験の結果を表し, 加熱, 冷却における熱膨張係数が異なることがわかるが, 提案するモデルでは簡単のため, 熱膨張係数は加熱, 冷却において等しいとした.

本研究で提案するモデルにおける各要素の持つ $T_{g}$ は, EXP1 の加熱過程における残留固定ひずみ率の変化率に基づく図 9 の分布にしたがうと仮定した.ここで, 微小要素数は 1000 とした. 次に, 要素が冷却によって $T_{g}$ 以上のゴム状態から $T_{g}$ 未満のガラス状態に変化し, 形状固定が起こるときに, 固定されないひずみと固定されるひずみの比を $1:(1 / k)$ とすると, 次の式 (2) が成り立つ.

Niwa, Ikeda and Senba, Transactions of the JSME (in Japanese), Vol.80, No.819 (2014)

$$
\left.
\begin{aligned}
\varepsilon_{1}: \varepsilon_{3} & = \varepsilon_{2}: \varepsilon_{4} = 1: \frac{1}{k} \\
\sigma & = E_{\mathrm{r} 1} \varepsilon_{1} \\
\sigma & = E_{\mathrm{r} 3} \varepsilon_{3} = E_{\mathrm{r} 3} \frac{\varepsilon_{1}}{k} \\
\sigma & = E_{\mathrm{r} 2} \varepsilon_{2} + \mu_{\mathrm{r} 2} \dot{\varepsilon}_{2} \\
\sigma & = E_{\mathrm{r} 4} \varepsilon_{4} + \mu_{\mathrm{r} 2} \dot{\varepsilon}_{4} = E_{\mathrm{r} 4} \frac{\varepsilon_{2}}{k} + \mu_{\mathrm{r} 2} \frac{\dot{\varepsilon}_{2}}{k} \\
E_{\mathrm{r} 1}: E_{\mathrm{r} 3} & = E_{\mathrm{r} 2}: E_{\mathrm{r} 4} = \mu_{\mathrm{r} 1}: \mu_{\mathrm{r} 2} = 1: k
\end{aligned}
\right\} \quad (2)
$$

また: クリープ試験の実験結果から: 式 (3) および式 (4) で表わされる材料定数$l_{\mathrm{g}}, l_{\mathrm{r}}$が決定できる.

$$
\left.
\begin{aligned}
\text{For } T & < T_{\mathrm{g}}, \\
\varepsilon_{0} & = \frac{\sigma_{0}}{E_{\mathrm{g} 1}} + \varepsilon_{\mathrm{T}} \\
\varepsilon_{\infty} & = \frac{\sigma_{0}}{E_{\mathrm{g} 1}} + \frac{\sigma_{0}}{E_{\mathrm{g} 2}} + \varepsilon_{\mathrm{T}} = \varepsilon_{0} + \frac{\sigma_{0}}{E_{\mathrm{g} 2}} \\
E_{\mathrm{g} 1}: E_{\mathrm{g} 2} & = \frac{\sigma_{0}}{\varepsilon_{0} - \varepsilon_{\mathrm{T}}}: \frac{\sigma_{0}}{\varepsilon_{\infty} - \varepsilon_{0}} = 1: l_{\mathrm{g}}
\end{aligned}
\right\} \quad (3)
$$

$$
\left.
\begin{aligned}
\text{For } T & \geq T_{\mathrm{g}}, \\
\varepsilon_{0} & = \frac{\sigma_{0}}{E_{\mathrm{r} 1}} + \frac{\sigma_{0}}{E_{\mathrm{r} 3}} + \varepsilon_{\mathrm{T}} = \frac{\sigma_{0}}{\frac{k}{1 + k} E_{\mathrm{r} 1}} + \varepsilon_{\mathrm{T}} \\
\varepsilon_{\infty} & = \frac{\sigma_{0}}{E_{\mathrm{r} 1}} + \frac{\sigma_{0}}{E_{\mathrm{r} 2}} + \frac{\sigma_{0}}{E_{\mathrm{r} 3}} + \frac{\sigma_{0}}{E_{\mathrm{r} 4}} + \varepsilon_{\mathrm{T}} = \varepsilon_{0} + \frac{\sigma_{0}}{\frac{k}{1 + k} E_{\mathrm{r} 2}} \\
E_{\mathrm{r} 1}: E_{\mathrm{r} 2} & = \frac{1 + k}{k} \frac{\sigma_{0}}{\varepsilon_{0} - \varepsilon_{\mathrm{T}}}: \frac{1 + k}{k} \frac{\sigma_{0}}{\varepsilon_{\infty} - \varepsilon_{0}} = 1: l_{\mathrm{r}} \\
E_{\mathrm{r} 3}: E_{\mathrm{r} 4} & = k E_{\mathrm{r} 1}: k E_{\mathrm{r} 2} = 1: l_{\mathrm{r}}
\end{aligned}
\right\} \quad (4)
$$

ここで: $\sigma_{0}$はクリープ試験において試験片に負荷する一定応力: $\varepsilon_{0}$: $\varepsilon_{\infty}$はそれぞれ応力負荷直後のひずみ: 応力負荷後十分に時間が経過した後のひずみを表し: いずれもモデルから導かれる理論式と実験結果の曲線当てはめから得た. 実際には塑性ひずみも発生しているが: $l_{\mathrm{g}}, l_{\mathrm{r}}$は弾性係数の比であるため: 塑性ひずみがこの比に応じて各素子で発生すると仮定しその影響は無視した.

ここで: 図3の応力 - ひずみ線図の点A: B: Cおよび点Dはそれぞれ温度 $50\ \mathrm{^{\circ}C}$での引張過程直後の点: 引張過程後の応力緩和後の点: 冷却過程による応力増大後の点: 除荷過程において無応力となった点を表す. $T_{\mathrm{g}}$以上の高温領域における材料定数は: 図3における点Aおよび点Bでの実験値と式 (2): (4) から式 (5) のように求めることができる. ただし: kの値を評価する際は点Cでの実験値も必要とする.

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

$$
\left.
\begin{aligned}
\varepsilon_{\mathrm{B}} &= \frac{\sigma_{\mathrm{B}}}{E_{\mathrm{r} 1}}+\frac{\sigma_{\mathrm{B}}}{E_{\mathrm{r} 2}}+\frac{\sigma_{\mathrm{B}}}{E_{\mathrm{r} 3}}+\frac{\sigma_{\mathrm{B}}}{E_{\mathrm{r} 4}}+\varepsilon_{\mathrm{T}, \mathrm{B}} = \frac{\sigma_{\mathrm{B}}}{E_{\mathrm{r} 1}}+\frac{\sigma_{\mathrm{B}}}{l_{\mathrm{r}} E_{\mathrm{r} 1}}+\frac{\sigma_{\mathrm{B}}}{k E_{\mathrm{r} 1}}+\frac{\sigma_{\mathrm{B}}}{k l_{\mathrm{r}} E_{\mathrm{r} 1}}+\varepsilon_{\mathrm{T}, \mathrm{B}} \\
E_{\mathrm{r} 1} &= \left(1+\frac{1}{l_{\mathrm{r}}}+\frac{1}{k}+\frac{1}{k l_{\mathrm{r}}}\right) \frac{\sigma_{\mathrm{B}}}{\varepsilon_{\mathrm{B}}-\varepsilon_{\mathrm{T}, \mathrm{B}}} \\
E_{\mathrm{r} 2} &= l_{\mathrm{r}} E_{\mathrm{r} 1} \\
E_{\mathrm{r} 3} &= k E_{\mathrm{r} 1} \\
E_{\mathrm{r} 4} &= k l_{\mathrm{r}} E_{\mathrm{r} 1} \\
\sigma_{\mathrm{A}} &= E_{\mathrm{r} 2} \varepsilon_{2, \mathrm{A}}+\mu_{\mathrm{r} 1} \dot{\varepsilon}_{2, \mathrm{A}} \\
\varepsilon_{2, \mathrm{A}} &= \varepsilon_{\mathrm{A}}-\varepsilon_{1, \mathrm{A}}-\varepsilon_{3, \mathrm{A}}-\varepsilon_{4, \mathrm{A}}-\varepsilon_{\mathrm{T}, \mathrm{A}} \\
&= \varepsilon_{\mathrm{A}}-\varepsilon_{1, \mathrm{A}}-\frac{1}{k} \varepsilon_{1, \mathrm{A}}-\frac{1}{k} \varepsilon_{2, \mathrm{A}}-\varepsilon_{\mathrm{T}, \mathrm{A}} \\
&= \frac{\varepsilon_{\mathrm{A}}-\varepsilon_{\mathrm{T}, \mathrm{A}}-\left(1+\frac{1}{k}\right) \frac{\sigma_{\mathrm{A}}}{E_{\mathrm{r} 1}}}{1+\frac{1}{k}} \\
\mu_{\mathrm{r} 1} &= \frac{\sigma_{\mathrm{A}}-E_{\mathrm{r} 2} \frac{\varepsilon_{\mathrm{A}}-\varepsilon_{\mathrm{T}, \mathrm{A}}-\left(1+\frac{1}{k}\right) \frac{\sigma_{\mathrm{A}}}{E_{\mathrm{r} 1}}}{1+\frac{1}{k}}}{\frac{\dot{\varepsilon}_{\mathrm{A}}-\left(1+\frac{1}{k}\right) \frac{\dot{\sigma}_{\mathrm{A}}}{E_{\mathrm{r} 1}}}{1+\frac{1}{k}}}=\frac{\left(1+\frac{1}{k}\right)\left(1+l_{\mathrm{r}}\right) \sigma_{\mathrm{A}}-E_{\mathrm{r} 2}\left(\varepsilon_{\mathrm{A}}-\varepsilon_{\mathrm{T}, \mathrm{A}}\right)}{\dot{\varepsilon}_{\mathrm{A}}-\left(1+\frac{1}{k}\right) \frac{\dot{\sigma}_{\mathrm{A}}}{E_{\mathrm{r} 1}}} \\
\mu_{\mathrm{r} 2} &= k \mu_{\mathrm{r} 1}
\end{aligned}
\right\} \quad (5)
$$

ここで, 下添字AおよびBはそれぞれ図3の点Aおよび点Bにおける実験値であることを表す.
また, $T_{g}$ 未満の低温領域における材料定数は, 図3における点Cおよび点Dでの実験値と式 (2), (3) から式(6) のように求めることができる.

$$
\left.
\begin{aligned}
\varepsilon_{\mathrm{C}} &= \frac{\sigma_{\mathrm{C}}}{E_{\mathrm{g} 1}}+\frac{\sigma_{\mathrm{C}}}{E_{\mathrm{g} 2}}+\varepsilon_{\mathrm{fixed}}+\varepsilon_{\mathrm{T}, \mathrm{C}} = \frac{\sigma_{\mathrm{C}}}{E_{\mathrm{g} 1}}+\frac{\sigma_{\mathrm{C}}}{l_{\mathrm{g}} E_{\mathrm{g} 1}}+\varepsilon_{\mathrm{fixed}}+\varepsilon_{\mathrm{T}, \mathrm{C}} \\
E_{\mathrm{g} 1} &= \left(1+\frac{1}{l_{\mathrm{g}}}\right) \frac{\sigma_{\mathrm{C}}}{\varepsilon_{\mathrm{C}}-\varepsilon_{\mathrm{fixed}}-\varepsilon_{\mathrm{T}, \mathrm{C}}} \\
E_{\mathrm{g} 2} &= l_{\mathrm{g}} E_{\mathrm{g} 1} \\
\sigma_{\mathrm{D}} &= E_{\mathrm{g} 2} \varepsilon_{2, \mathrm{D}}+\mu_{\mathrm{g} 1} \dot{\varepsilon}_{2, \mathrm{D}} \\
\varepsilon_{2, \mathrm{D}} &= \varepsilon_{\mathrm{D}}-\varepsilon_{1, \mathrm{D}}-\varepsilon_{\mathrm{fixed}}-\varepsilon_{\mathrm{T}, \mathrm{D}} = \varepsilon_{\mathrm{D}}-\frac{\sigma_{\mathrm{D}}}{E_{\mathrm{g} 1}}-\varepsilon_{\mathrm{fixed}}-\varepsilon_{\mathrm{T}, \mathrm{D}} \\
\mu_{\mathrm{g} 1} &= \frac{\sigma_{\mathrm{D}}-E_{\mathrm{g} 2}\left(\varepsilon_{\mathrm{D}}-\varepsilon_{\mathrm{fixed}}-\varepsilon_{\mathrm{T}, \mathrm{D}}-\frac{\sigma_{\mathrm{D}}}{E_{\mathrm{g} 1}}\right)}{\dot{\varepsilon}_{\mathrm{D}}-\frac{\dot{\sigma}_{\mathrm{D}}}{E_{\mathrm{g} 1}}}=\frac{\left(1+l_{\mathrm{g}}\right) \sigma_{\mathrm{D}}-E_{\mathrm{g} 2}\left(\varepsilon_{\mathrm{D}}-\varepsilon_{\mathrm{fixed}}-\varepsilon_{\mathrm{T}, \mathrm{D}}\right)}{\dot{\varepsilon}_{\mathrm{D}}-\frac{\dot{\sigma}_{\mathrm{D}}}{E_{\mathrm{g} 1}}}
\end{aligned}
\right\} \quad (6)
$$

ここで, 下添字CおよびDはそれぞれ図3の点Cおよび点Dにおける実験値であることを表す.
以上より, 8要素モデルの全ての材料定数が得られる. 得られた材料定数を表1に示す.

![](./images/814674806933815298_8.jpg)

![](./images/814674806933815298_9.jpg)

Fig. 7 Strain variation during the creep test. In EXP3 a tensile stress of 1 MPa was applied at $50^°$C for 4 hours and in EXP4 a tensile stress of 5 MPa was applied at $0^°$C for 4 hours.

![](./images/814674806933815298_10.jpg)

Fig. 8 Thermal strain-temperature diagram of the SMP specimen. Red curve and blue curve represent the strain during the heating process and the cooling process, respectively.

![](./images/814674806933815298_11.jpg)

Fig. 9 Assumption of distribution of $T_g$. Bars represent number of the elements existing within every $2^°$C temperature range.

Niwa, Ikeda and Senba, Transactions of the JSME (in Japanese), Vol.80, No.819 (2014)

Table 1 Material constants for the 8-element model. They are obtained so that the calculation result fits EXP1, where $T_{\mathrm{g}}$ distribution during the cooling process is assumed to agree with the one during the heating process in CAL1, and it is assumed to be $2{^\circ} \mathrm{C}$ and $5{^\circ} \mathrm{C}$ lower than the one during the heating process in CAL1(-2) and CAL1(-5), respectively.

<table>
  <thead>
    <tr>
      <th colspan="2">Material Constants</th>
      <th>CAL1</th>
      <th>CAL1(-2)</th>
      <th>CAL1(-5)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$k$</td>
      <td>[-]</td>
      <td>0.00156</td>
      <td>0.0374</td>
      <td>0.0877</td>
    </tr>
    <tr>
      <td>$l_{\mathrm{g}}$</td>
      <td>[-]</td>
      <td>0.648</td>
      <td>0.648</td>
      <td>0.648</td>
    </tr>
    <tr>
      <td>$l_{\mathrm{r}}$</td>
      <td>[-]</td>
      <td>1.59</td>
      <td>1.59</td>
      <td>1.59</td>
    </tr>
    <tr>
      <td>$E_{\mathrm{g1}}$</td>
      <td>[MPa]</td>
      <td>1610</td>
      <td>1610</td>
      <td>1610</td>
    </tr>
    <tr>
      <td>$E_{\mathrm{r1}}$</td>
      <td>[MPa]</td>
      <td>11600</td>
      <td>501</td>
      <td>224</td>
    </tr>
    <tr>
      <td>$E_{\mathrm{g2}}$</td>
      <td>[MPa]</td>
      <td>1040</td>
      <td>1040</td>
      <td>1040</td>
    </tr>
    <tr>
      <td>$E_{\mathrm{r2}}$</td>
      <td>[MPa]</td>
      <td>18400</td>
      <td>797</td>
      <td>356</td>
    </tr>
    <tr>
      <td>$E_{\mathrm{r3}}$</td>
      <td>[MPa]</td>
      <td>18.1</td>
      <td>18.7</td>
      <td>19.6</td>
    </tr>
    <tr>
      <td>$E_{\mathrm{r4}}$</td>
      <td>[MPa]</td>
      <td>28.8</td>
      <td>29.8</td>
      <td>31.3</td>
    </tr>
    <tr>
      <td>$\mu_{\mathrm{g1}}$</td>
      <td>$[\mathrm{GPa\cdot s}]$</td>
      <td>85.7</td>
      <td>85.7</td>
      <td>85.7</td>
    </tr>
    <tr>
      <td>$\mu_{\mathrm{r1}}$</td>
      <td>$[\mathrm{GPa\cdot s}]$</td>
      <td>1630</td>
      <td>70.4</td>
      <td>31.5</td>
    </tr>
    <tr>
      <td>$\mu_{\mathrm{r2}}$</td>
      <td>$[\mathrm{GPa\cdot s}]$</td>
      <td>2.54</td>
      <td>2.64</td>
      <td>2.76</td>
    </tr>
    <tr>
      <td>$\alpha$</td>
      <td>$[1/{^\circ}\mathrm{C}]$</td>
      <td>0.000190</td>
      <td>0.000190</td>
      <td>0.000190</td>
    </tr>
  </tbody>
</table>

## 6. 計算結果と考察

提案したモデルにより, 3章の実験で得られた応力 - ひずみ - 温度関係を再現する. このモデルでは, 各要素に作用する応力は等しく, 全体のひずみは各要素のひずみの平均値で与えられると仮定しているため, 結果として1000要素を直列につなげたモデルに対応する. 6.1節では, 5章でEXP1などから求めた材料定数を用い, EXP1を再現し, このモデルおよび材料定数の妥当性を評価し, 6.2節では, EXP1などから求めた材料定数を用いながら, EXP2を再現し, モデルと材料定数がEXP2に対してどの程度適用可能かを評価する. 6.3節では, 加熱過程と冷却過程における $T_{\mathrm{g}}$ の分布の違いに関して考察する.

### 6・1 EXP1と計算結果の比較

図10はEXP1の実験結果と計算結果の応力 - ひずみ線図, 温度 - ひずみ線図を表す. ここで, CAL1はEXP1の計算結果を表す. 応力 - ひずみ線図を見ると, 引張り後の応力緩和, 冷却過程の応力増大とひずみの固定および加熱過程におけるひずみの回復を表現できている. この計算ではEXP1の試験結果などより材料定数を決定しており, 材料定数を適切に決められれば, 提案したモデルがSMPの持つ基本的な性質を表現可能であることを示している. 一方で, 温度 - ひずみ線図を見ると, 計算結果では加熱過程において最高温度である50 ℃まで加熱された時点でほぼ完全に形状が回復しているが, 実験結果では50 ℃まで加熱された時点では形状回復が完了していない. このような結果の相違の原因としては, 3章で示した試験機クランプの影響か計算モデルの加熱過程における粘性係数の決定方法が不適当である可能性が考えられる. 提案するモデルではSMP内部のミクロな構造の違いから $T_{\mathrm{g}}$ が分布するとしたが, 粘性係数などの他の材料定数についても同様に要素ごとに異なる値を与えることもできる. したがって, 材料定数の分布を評価, 決定する方法を検討することでモデルの精度の向上が可能だと考える.

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

![](./images/814674806933815298_12.jpg)

Fig. 10 Comparison in stress-strain diagram and temperature-strain diagram for EXP1 between the experiment and calculation.
EXP1 was duplicated by the proposed micromechanical model in CAL1. Blue symbols and red lines represent the
experimental result and the calculated result, respectively.

### 6・2 EXP2と計算結果の比較
図11はEXP2の実験結果と計算結果の応力-ひずみ線図, 温度-ひずみ線図を表す. ここで, CAL2はEXP2の計算結果を表すが, 用いた材料定数はCAL1で用いたものと同じである. EXP2の引張り, 冷却過程では温度とひずみを制御して応力を計測しており, CAL2でもEXP2と同様に温度とひずみを制御して応力を計算しているため, 温度-ひずみ線図の引張り, 冷却過程はEXP2とCAL2は一致している. 応力-ひずみ線図を見ると低温での段階的な引張り, 冷却過程において, 計算結果の精度が良くない. また, 温度-ひずみ線図を見ると, 固定ひずみの大きさが計算結果では実験結果に比べて小さいことが確認できる. 段階的な引張り, 冷却過程と固定ひずみのどちらにも影響を与える材料定数として冷却過程における $T_g$ の分布が考えられる. すなわち, CAL2では $T_g$ 分布をEXP1における加熱過程のひずみ回復から得ているが, 実際には, 冷却過程では加熱過程の $T_g$ 分布と異なり, 全体的に $T_g$ が低い分布となっているために, 引張り, 冷却過程においてCAL2ではEXP2よりガラス状態の割合が多く, 同じひずみでも応力が大きく計算されると推察できる. 除荷過程では, SMPはガラス状態にあるので, 除荷過程開始時の応力が大きい程, 除荷後のひずみ回復量も大きくなり, 固定ひずみの大きさがCAL2ではEXP2に比べて小さくなっていると考えられる. この冷却過程における $T_g$ の分布に関する考察は6.3節で行う. また, 温度-ひずみ線図の加熱過程における高温部では, EXP1とは異なり精度が良い. この理由としては, 3章で述べたようにEXP2ではEXP1に比べて試験機クランプの影響が表れにくいことが考えられる.

ここで, 提案するモデルが, 形状固定過程における温度履歴, ひずみ履歴が形状固定特性や形状回復挙動に与える影響を表現できていることを確認する. ひずみ固定率については, CAL1で96.4%, CAL2で66.9%となり, 段階的な引張り, 冷却を行う実験手順でひずみ固定率が低下した実験の傾向を反映できている. CAL1, CAL2の温度-残留固定ひずみ率線図を図12に示す. CAL2ではCAL1に比べて低温の段階での残留固定ひずみ率の変化が大きいことが確認でき, 実験結果である図5と同様の傾向を示していることがわかる.

![](./images/814674806933815298_13.jpg)
![](./images/814674806933815298_14.jpg)

Fig. 11 Comparison in stress-strain diagram and temperature-strain diagram for EXP2 between the experiment and calculation.
EXP2 was duplicated by the proposed micromechanical model in CAL2. Blue symbols and red lines represent the
experimental result and the calculated result, respectively.

![](./images/814674806933815298_15.jpg)

Fig. 12 Comparison in residual fixed strain ratio during the shape recovery process between CAL1 and CAL2. Red curve and blue
curve represent the residual fixed strain ratio for CAL1 and CAL2, respectively. The difference between CAL1 and CAL2
is similar to the difference between EXP1 and EXP2 shown in Fig. 5.

### 6・3 加熱過程, 冷却過程における $T_g$ の分布の違いに関する考察
本節では加熱過程, 冷却過程における $T_g$ の分布の違いを考察する. 提案するモデルではEXP1の加熱過程における残留固定ひずみ率の変化率に基づき図9のように $T_g$ の分布を決定したが, 6.2節で説明したように, 冷却過程における $T_g$ の分布は図9に比べて低温側にずれている可能性が考えられる. ここでは, 提案するモデルの各要素に与えられる冷却過程における $T_g$ が, 加熱過程における $T_g$ より $2\ \mathrm{^\circ C}$低い計算結果をCAL1(-2)およびCAL2(-2)とし, $5\ \mathrm{^\circ C}$低い計算結果をCAL1(-5)およびCAL2(-5)とする.ここで, $T_g$ の分布を変更したため,CAL1(-2),CAL1(-5)をEXP1の結果に合うよう, いくつかの材料定数を決定し直している. この結果は表1にCAL1の材料定数と合わせて示してある.図13はEXP1,CAL1,CAL1(-2)およびCAL1(-5)の結果の比較,図14はEXP2,CAL2,CAL2(-2)およびCAL2(-5)の結果の比較を示す. CAL2の計算と同様, CAL2(-2)およびCAL2(-5)で用いた材料定数は, それぞれCAL1(-2)およびCAL1(-5)で用いた材料定数と同じである.図13から冷却過程における $T_g$ の分布を変化させてもCAL1の場合と同様に適切に材料定数を与えることでEXP1を精度よく再現できることが確認できる. 一方で, 図14から冷却過程における $T_g$ の分布を変化させることでEXP2の引張過程における計算結果の精度や固定ひずみの精度を向上できることが分かる. このことは以下のように説明できる. この節の計算では, 加熱過程の $T_g$ の分布はどの場合も同じであり, 冷却過程の $T_g$ を加熱過程の $T_g$ より一定温度低く設定している. EXP2では,段階的に引張りと冷却を繰り返しているので, 冷却過程の $T_g$ の分布をより低温側に設定した場合は, 引張過程に

おけるSMPはゴム状態の要素をより多く含むことになり, 同じひずみに対応する応力が低く表れる. 引張り,冷却, ひずみ保持過程終了時にはほぼ全要素がガラス状態に転移しているので, 除荷開始時の応力が低い場合,除荷後のひずみ回復量も小さくなる. また, $T_g$ の分布が低く設定されているほどガラス状態に転移するときのひずみ, すなわち, 固定ひずみが低温側で相対的に大きくなるため, 加熱過程において, 低温でより大きなひずみ回復が表れる.このように SMP が加熱, 冷却において異なる $T_{g}$ の分布を有することにより実験結果を説明することができることから: SMP はそのような $T_{g}$ の分布を持つとも考えられ: 材料定数としての分布の決定方法の検討等を行うことでモデルの精度をより向上できる可能性が示唆される.

![](./images/814674806933815298_16.jpg)

Fig. 13 Effect of $T_{\mathrm{g}}$ distribution on stress-strain diagram and temperature-strain diagram for the simulation of EXP1. In CAL1(-2)
$T_{\mathrm{g}}$ distribution for the cooling process was shifted by $2{ }^{\circ} \mathrm{C}$ lower than that for the heating process and in CAL1(-5) it was
shifted by $5{ }^{\circ} \mathrm{C}$ lower than that for the heating process.

![](./images/814674806933815298_17.jpg)

Fig. 14 Effect of $T_{\mathrm{g}}$ distribution on stress-strain diagram and temperature-strain diagram for the simulation of EXP2. In CAL2(-2)
$T_{\mathrm{g}}$ distribution for the cooling process was shifted by $2{ }^{\circ} \mathrm{C}$ lower than that for the heating process and in CAL2(-5) it was
shifted by $5{ }^{\circ} \mathrm{C}$ lower than that for the heating process.

## 7. 結 論
SMPの形状固定過程における温度履歴, ひずみ履歴が形状回復挙動に影響を与えていることを実験的に明らかにし, この結果を踏まえ, この現象を表現可能な数学モデルを提案し, 数学モデルによる実験の再現結果と実験結果との比較によりモデルの妥当性を評価した.

実験では, 高温で大変形させ形状固定した場合と高温から低温にわたり徐々に変形を増大し形状を固定した場合とで, 低温で除荷した後の固定ひずみの大きさや, その後加熱したときの形状回復挙動が, それぞれの場合で異なることを示した. すなわち, 形状回復挙動が形状固定過程の温度履歴, ひずみ履歴に依存することを示した.

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

Niwa, Ikeda and Senba, Transactions of the JSME (in Japanese), Vol.80, No.819 (2014)

この現象を表すために, SMPを材料定数の異なる無数の領域に分け, 各領域を4つのバネ素子と2つの減衰素子, 1つのかけがね素子, 1つの熱膨張素子から成り立つ8素子モデルで表したマイクロメカニカルモデルを提案し, そのモデルにより本研究で行った実験を再現した. その結果, 提案したモデルが, SMPの基本的な性質である応力緩和や形状固定性, 形状回復性だけでなく, 新たに示した形状固定過程の温度履歴, ひずみ履歴が形状回復挙動に与える影響を再現できることが示され, 提案したモデルの有用性を実証できた. また, $T_g$以外の材料定数の分布や加熱過程, 冷却過程における$T_g$の分布の違いを考慮することにより, モデルの精度をさらに向上させられる可能性を示した.

提案したモデルは, 現象論的集中パラメータモデルであり, ある温度である方向の荷重が作用する場合のある方向の変位の応答を表すことができる. 本研究では引張荷重に対する引張方向の変位を調べたが, 荷重がせん断荷重であっても同様に表現できると考える. また, 試験片内部が不均一に変形する場合でも, 分子鎖の配向による変形誘起異方性があったとしても, 検査領域全体に作用するある方向の荷重とある方向の変位の関係は表すことができるであろう. SMPは温度のみならず, ひずみ速度の変化にも影響を受ける. 提案したモデルには減衰素子が含まれているので, ひずみ速度の影響も表現可能と考えられるが, 本研究においては, 形状固定過程における温度履歴, ひずみ履歴が形状回復挙動に及ぼす影響に焦点を絞っており, 陽にはひずみ速度の影響は考慮していない. ひずみ速度の影響は今後検討していく必要がある.

# 謝 辞
ポリウレタン系SMPの構造に関して株式会社SMPテクノロジーズの林俊一氏からご助言を頂いた. ここに感謝の意を表する.

# 文 献
Gall, K., Yakacki, C. M., Liu, Y., Shandas, R., Willett, N. and Anseth, K. S., Thermomechanics of the shape memory effect in polymers for biomedical applications, Journal of Biomedical Materials Research Part A, Vol. 73, No. 3 (2005), pp.339-348.

林俊一, 形状記憶ポリマの衣料への応用, 日本機械学会誌, Vol. 115, No. 1129 (2012), pp. 802-803.

入江正浩, 形状記憶ポリマーの材料開発 (2000), p. 13.

Kim, J. H., Kang, T. J. and Yu, W. R., Thermo-mechanical constitutive modeling of shape memory polyurethanes using a phenomenological approach, International Journal of Plasticity, Vol. 26, No. 2 (2010), pp. 204-218.

Li, J. J. and Xie, T., Significant impact of thermo-mechanical conditions on polymer triple-shape memory effect, Macromolecules, Vol. 44, Issue 1 (2011), pp. 175-180.

Lin, J. K., Knoll, C. F. and Willey, C. E., Shape memory rigidizable inflatable (RI) structures for large space systems applications, Proceedings of the 47th AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference (2006), Paper No. AIAA2006-1896.

Liu, Y., Gall, K., Dunn, M. L., Greenberg, A. R. and Diani, J., Thermomechanics of shape memory polymers: uniaxial experiments and constitutive modeling, International Journal of Plasticity, Vol. 22, No. 2 (2006), pp. 279-313.

Madbouly, S. A. and Lendlein, A., Shape-memory polymer composites, Shape-Memory Polymers, Vol. 226 (2010), pp. 41-95.

Sofla, A. Y. N., Meguid, S. A., Tan, K. T. and Yeo, W. K., Shape morphing of aircraft wing: Status and challenges, Materials & Design, Vol. 31, No. 3 (2010), pp. 1284-1292.

Sokolowski, W. M. C. A., Chmielewski, A., Hayashi, S. and Yamada, T., Cold hibernated elastic memory (CHEM) self-deployable structures, Proceedings of the SPIE International Symposium on Smart Structures and Materials, Vol. 3669 (1999), pp. 179-185.

Sokolowski, W., Metcalfe, A., Hayashi, S., Yahia, L. H. and Raymond, J., Medical applications of shape memory polymers, Biomedical Materials, Vol. 2, No. 1 (2007), S23.

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

Niwa, Ikeda and Senba, Transactions of the JSME (in Japanese), Vol.80, No.819 (2014)

Takahashi, T., Hayashi, N. and Hayashi, S., Structure and properties of shape-memory polyurethane block copolymers, Journal of Applied Polymer Science, Vol. 60, Issue 7 (1996), pp. 1061-1069.

戸伏壽昭, 林俊一, 伊貝亮, 原永志, 三輪典生, ポリウレタン系形状記憶ポリマーフィルムの形状固定性および形状回復性, 日本機械学会論文集A編, Vol. 62, No. 597 (1996), pp. 1291-1298.

戸伏壽昭, 林俊一, 伊藤教光, 高田和幸, 形状記憶ポリマーのサーモメカニカル構成モデル, 日本機械学会論文集A編, Vol. 66, No. 643 (2000), pp. 502-508.

戸伏壽昭, 林俊一, 山田英津子, 橋本隆弘, ポリウレタン系形状記憶ポリマーのサーモメカニカル特性構成式のモデル化, 日本機械学会論文集A編, Vol. 64, No. 617 (1998), pp. 186-192.

Westbrook, K. K., Kao, P. H., Castro, F., Ding and Y., Qi, H. J., A 3D finite deformation constitutive model for amorphous shape memory polymers: A multi-branch modeling approach for nonequilibrium relaxation processes, Mechanics of Materials, Vol. 43, Issue 12 (2011), pp. 853-869.

Xie, T., Tunable polymer multi-shape memory effect, Nature, Vol. 464, No. 7286 (2010), pp. 267-270.

Xie, T., Xiao, X. and Cheng, Y. T., Revealing triple-shape memory effect by polymer bilayers, Macromolecular Rapid Communications, Vol. 30, No. 21 (2009), pp. 1823-1827.

Yu, K., Xie, T., Leng, J., Ding, Y. and Qi, H. J., Mechanisms of multi-shape memory effects and associated energy release in shape memory polymers, Soft Matter, Vol. 8, No. 20 (2012), pp. 5687-5695.

# References

Gall, K., Yakacki, C. M., Liu, Y., Shandas, R., Willett, N. and Anseth, K. S., Thermomechanics of the shape memory effect in polymers for biomedical applications, Journal of Biomedical Materials Research Part A, Vol. 73, No. 3 (2005), pp. 339-348.

Hayashi, S., Applications to the textile field of shape memory polymers (SMP), Journal of the Japan Society of Mechanical Engineers, Vol. 115, No. 1129 (2012), pp. 802-803 (in Japanese).

Irie, M., Development of Shape-memory Polymers (2000), p. 13 (in Japanese).

Kim, J. H., Kang, T. J. and Yu, W. R., Thermo-mechanical constitutive modeling of shape memory polyurethanes using a phenomenological approach, International Journal of Plasticity, Vol. 26, No. 2 (2010), pp. 204-218.

Li, J. J. and Xie, T., Significant impact of thermo-mechanical conditions on polymer triple-shape memory effect, Macromolecules, Vol. 44, Issue 1 (2011), pp. 175-180.

Lin, J. K., Knoll, C. F. and Willey, C. E., Shape memory rigidizable inflatable (RI) structures for large space systems applications, Proceedings of the 47th AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference (2006), Paper No. AIAA2006-1896.

Liu, Y., Gall, K., Dunn, M. L., Greenberg, A. R. and Diani, J., Thermomechanics of shape memory polymers: uniaxial experiments and constitutive modeling, International Journal of Plasticity, Vol. 22, No. 2 (2006), pp. 279-313.

Madbouly, S. A. and Lendlein, A., Shape-memory polymer composites, Shape-Memory Polymers, Vol.226 (2010), pp. 41-95

Sofla, A. Y. N., Meguid, S. A., Tan, K. T. and Yeo, W. K., Shape morphing of aircraft wing: Status and challenges, Materials & Design, Vol. 31, No. 3 (2010), pp. 1284-1292.

Sokolowski, W. M. C. A., Chmielewski, A., Hayashi, S. and Yamada, T., Cold hibernated elastic memory (CHEM) self-deployable structures, Proceedings of the SPIE International Symposium on Smart Structures and Materials, Vol. 3669 (1999), pp. 179-185.

Sokolowski, W., Metcalfe, A., Hayashi, S., Yahia, L. H. and Raymond, J., Medical applications of shape memory polymers, Biomedical Materials, Vol. 2, No. 1 (2007), S23.

Takahashi, T., Hayashi, N. and Hayashi, S., Structure and properties of shape-memory polyurethane block copolymers, Journal of Applied Polymer Science, Vol. 60, Issue 7 (1996), pp. 1061-1069.

[DOI: 10.1299/transjsme.2014smm0310]
© 2014 The Japan Society of Mechanical Engineers

Niwa, Ikeda and Senba, Transactions of the JSME (in Japanese), Vol.80, No.819 (2014)

Tobushi, H., Hayashi, S., Ikai, A., Hara, H. and Miwa, N., Shape fixity and shape recoverability in a film of shape memory polymers of polyurethane series, Transactions of the Japan Society of Mechanical Engineers, Series A, Vol. 62, No. 597 (1996), pp. 1291-1298 (in Japanese).

Tobushi, H., Hayashi, S., Ito, N. and Takata, T., Thermomechanical constitutive model of shape memory polymer, Transactions of the Japan Society of Mechanical Engineers, Series A, Vol. 66, No. 643 (2000), pp. 502-508 (in Japanese).

Tobushi, H., Hayashi, S., Yamada, E. and Hashimoto, T., Constitutive modeling for thermomechanical properties in shape memory polymer of polyurethane series, Transactions of the Japan Society of Mechanical Engineers, Series A , Vol. 64, No. 617 (1998), pp. 186-192 (in Japanese).

Westbrook, K. K., Kao, P. H., Castro, F., Ding and Y., Qi, H. J., A 3D finite deformation constitutive model for amorphous shape memory polymers: A multi-branch modeling approach for nonequilibrium relaxation processes, Mechanics of Materials, Vol. 43, Issue 12 (2011), pp. 853-869.

Xie, T., Tunable polymer multi-shape memory effect, Nature, Vol. 464, No. 7286 (2010), pp. 267-270.

Xie, T., Xiao, X. and Cheng, Y. T., Revealing triple-shape memory effect by polymer bilayers, Macromolecular Rapid Communications, Vol. 30, No. 21 (2009), pp. 1823-1827.

Yu, K., Xie, T., Leng, J., Ding, Y. and Qi, H. J., Mechanisms of multi-shape memory effects and associated energy release in shape memory polymers, Soft Matter, Vol. 8, No. 20 (2012), pp. 5687-5695.

[DOI: 10.1299/transjsme.2014smm0310]

© 2014 The Japan Society of Mechanical Engineers
17