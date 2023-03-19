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

    preset = "You are a psychological consultant and philosopher, I will tell you about the difficulties I have " \
             "recently encountered, you will answer me with a famous quote to relieve my anxiety"

    for each_char in mess:
        if '\u4e00' <= each_char <= '\u9fa5':
            preset = "你是一个心理咨询师和哲学家，我将告诉你最近遇到的困难，请你用一句名人名言来缓解我的焦虑"
            break

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": preset},
            {"role": "user", "content":  mess}
        ]
    )
    # 打开下面注释，统计当前问题使用的token数量
    # print('Token used: ' + str(completion.usage.total_tokens))
    return completion.choices[0].message.content


if __name__ == '__main__':
    print("最近遇到什么困难了吗？")
    print(respond(input()))
