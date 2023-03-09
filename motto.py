import json

import openai


def respond(mess):
    try:
        with open('./token.json', 'r') as f:
            data = json.load(f)
        openai.api_key = data["token"]
    except Exception:
        print("token 配置不正确，请查看 README.md 指示重新配置")
        return False

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个心理咨询师"},
            {"role": "user", "content": "我最近" + mess + "，请你用一句名人名言来缓解我的焦虑"}
        ]
    )
    # 打开下面注释，统计当前问题使用的token数量
    # print('Token used: ' + str(completion.usage.total_tokens))
    return completion.choices[0].message.content


if __name__ == '__main__':
    print("最近遇到什么困难了吗？")
    print(respond(input()))
