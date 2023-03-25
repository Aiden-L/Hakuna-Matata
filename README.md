# Hakuna-Matata

> For the English README, please click [here](README.en.md).

#### 介绍
> 当代人每天都面临着生活各方面带来的巨大心理压力，本项目旨在开导遇到挫折的朋友，真心希望能帮到大家
> 
> 遇到困难时产生困惑，焦虑等负面情绪是很正常的，但不要因此而气馁，停止前进，要及时调整心态，最重要的是不要放弃，风雨终将过去，迎接我们的必是绚烂的晴天
> 
> 很喜欢《狮子王》里的这首歌，在此引用为项目名，无论发生了什么，都希望大家能乐观面对每一天
> 
> Hakuna Matata, No Need to Worry, Everything Will be Fine
> 
> 网站试玩Demo请访问 [https://help.xingzhouren.club/](https://help.xingzhouren.club/)

#### 作者的话
> 做这个项目的初衷是为了帮助身边压力很大的朋友，用名言金句鼓舞大家，缓解压力，但这个项目做到一半的时候，我认为这是一个极其失败的项目，当一个人的心情处于低谷的时候，一句正确的鼓励作用微乎其微，心理问题是很难以解决的，一句话又能有什么用。虽然我深知这一点，但还是把这个项目做了下来，找身边的朋友测试的时候，大家的整活能力真的远远超出了我的想象，面对无厘头的问题，AI的认真解答更像是对困难本身的嘲讽，但其实我们需要的也正是这样的精神，嘲讽困难而不是畏惧它而止步不前！当我看到朋友们戏耍我的AI时脸上浮现出的笑容时，我觉得，从某种意义上来讲，这个项目还是成功的。感谢大家的支持，后续这个项目还会更新更多有意思的玩法，敬请期待。
> 
> 本项目非专业心理指导，希望大家能从中获得快乐，如有需要，请向专业的心理咨询师寻求帮助。

## 希望大家每天都能有个好心情
[Click Here to Learn More about Hakuna Matata](https://www.youtube.com/watch?v=v34w65U98gI)

#### 软件架构
* Python 3.10
* Chat-GPT 3.5

#### 安装说明
1. 命令行输入`pip install -r requirements.txt`
2. 在项目文件夹中新建`token.json`文件，按如下配置
    ```json
    {
      "token": "put your token here"
    }
    ```

#### 使用说明
1. 名人名言生成demo: `motto.py`
2. 配置过滤器 `filter.json` 说明
   - "rule": (list) 需要匹配的关键词列表，当输入匹配到其中之一时即可应用规则，英文规则请用小写字符书写(匹配时会忽略大小写)
   - "pass": (boolean) `true/false` 匹配到关键词后，是否将用户输入传入GPT，如为`true`，则问题有概率不输入GPT，直接返回答案，如为`false`，则将reply结果直接返回
   - "reply": (list) 替换回复的列表，将随机选取列表中的一项作为回复(是否结合GPT回复取决于pass的值)

#### 更新日志
- 0.0.1: 新增名人名言接口，优化项目格式，引入Chat-GPT接口
- 0.1.0: 可视化展示界面完成
- 0.1.1: 修复了前端显示不正确的一些问题
- 0.1.2: 修复了前端文字与背景融合的问题，增加了多种背景
- 0.1.3: 改进了角色预设，增加了对英文的支持
- 0.1.4: 改进了角色预设，增加了请求超时设定 (20s)
- 0.1.5: 增加了多种背景的随机切换
- 0.1.6: 增加了animate动画，新增随机名言显示
- 0.1.7: 增加了motto输入的过滤器
