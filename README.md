# AIがESを作成するアプリ-flask version-<br><sub>ESや、会社の質問、ガクチカなどを自動で書くことができます。</sub>

rinnaの日本語のGPT-2を、就活サイトのESを用いてファインチューニングして、ESを書けるようにしました。

下の文章はAIが生成した文章です。

<sub>
私が御社を志望した理由は、説明会や座談会を通じて、社員一人一人が高品質・安定供給の責任を担い、努力を惜しまない強い意志と、仕事に対する誇り、そして「小林製薬に頼んでよかった」と言ってもらえるような理想を持っていることに魅力を感じたからです。理想を実現するためには、会社全体の取り組みや現状を把握し、目標に対して計画的に行動する必要があると考えます。私は年月、型糖尿病の症を患ったがんでカ月入院しました。誰よりも早く症状が改善し、担当の方から「飲み薬の変更があって心配だけど大丈夫?」と声をかけていただいた時、日々の努力が患者様の笑顔に繋がっていると実感し、とてもうれしく思いました。この経験から、将来はより多くの人に貢献できる、製薬会社の枠を越えて、社会全体にとってより価値があるものを届けられる仕事がしたいと思っています。それに向けて挑戦できる環境が、貴社には揃っていると感じました。
</sub><br><br>

- モデル
https://huggingface.co/huranokuma/es

- ウェブアプリ
http://www.eswrite.com

2022/11/15　出力されるESの文字数を多くしました。
