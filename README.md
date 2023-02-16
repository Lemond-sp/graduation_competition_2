# graduation_competition_2
## 愛媛大学 工学部 人工知能研究室 自然言語処理グループ

## 卒論コンペティション第二回(~2023.02/14)


- **TASK**
  - 日本語のTwitterテキストについての感情極性分類
  - 書き手の感情極性を５クラス分類(-2,-1,0,1,2)
  - 評価指標 Quadratic Weighted Kappa
- **DATASET**
  - Train/Dev/Test = 30k/2.5k/2.5k
  - 分割を変更してはならない
- 予定
  - 第一回 : ニューラルネットワークを使用しない
  - 第二回 : 外部データ(事前学習)を使用しない⭕️
  - 制約なし


# 解法
## 擬似ラベル(Pseudo-Label)による半教師あり学習
1. ラベルづけされているデータで学習済みモデルを作る
2. 1.で作成したモデルを使って、ラベルづけされていないデータ(Test)で予測値を出す
3. 2.の予測値を疑似ラベルとし、疑似ラベルづきデータをラベルづきデータに混ぜて学習する

## Optuna
- LinearSVRの閾値をOptunaで最適化
## モデル
- 擬似ラベルを適用したBiLSTM, LinearSVR + MLP
![](src/images/model.png)
### BiLSTM
擬似ラベル手法を用いたテストデータを学習データに加えて再学習をn回繰り返し
### LinearSVR
擬似ラベル手法を用いたテストデータを学習データに加えて再学習をn回繰り返し
### MLP
MLPによる分類問題
### アンサンブル
- 擬似ラベル手法を適応したBiLSTMとLinearSVRとのアンサンブル(Aとする)
- AとMLPとのアンサンブル