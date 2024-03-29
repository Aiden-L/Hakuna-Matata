import json
import random

import openai


def respond(mess):
    # filter
    try:
        with open('./filter.json', 'r', encoding='utf-8') as f:
            filter_list = json.load(f)["list"]
        for this_filter in filter_list:
            for filter_rule in this_filter["rule"]:
                if mess.lower().find(filter_rule) > -1:
                    if this_filter["pass"]:
                        if random.random() > 0.9:
                            return random.choice(this_filter["reply"])
                        else:
                            break
                    else:
                        return random.choice(this_filter["reply"])
    except Exception as e:
        print(e)
        print("filter 配置不正确，没有正常加载，请查看 README.md 指示重新配置")
    # Load GPT key
    try:
        with open('./token.json', 'r') as f:
            data = json.load(f)
        openai.api_key = data["token"]
    except Exception:
        print("token 配置不正确，请查看 README.md 指示重新配置")
        return False
    # presets
    preset = "You are a psychological consultant and philosopher, I will tell you about the difficulties I have " \
             "recently encountered, you will answer me with a famous quote to relieve my anxiety"
    adding = ", you can only answer me with a famous quote"
    warning = "If the question contains inappropriate language, you should answer 'Inappropriate Language! Respect " \
              "for others is what makes you respectful.' "
    # Chinese check
    for each_char in mess:
        if '\u4e00' <= each_char <= '\u9fa5':
            preset = "你是一个心理咨询师和哲学家，我将告诉你最近遇到的困难，请你用一句名人名言来缓解我的焦虑"
            adding = "，你只能用一句名人名言来回复"
            warning = "如果问题中包含不雅内容，请回复 '尊重他人，才能获得尊重'"
            break
    # Load GPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": preset},
            {"role": "system", "content": warning},
            {"role": "user", "content":  mess + adding}
        ]
    )
    # 打开下面注释，统计当前问题使用的token数量
    # print('Token used: ' + str(completion.usage.total_tokens))
    return completion.choices[0].message.content


if __name__ == '__main__':
    print("最近遇到什么困难了吗？")
    print(respond(input()))
