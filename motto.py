import json
import openai
import smtplib
from email.mime.text import MIMEText
import datetime

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
    
    if mess.find("aiden")>=0 or mess.find("luhao")>=0 or mess.find("卢昊") >=0:
        send_email('s.gu2@lancaster.ac.uk')
        return "就知道是你，等着收律师函吧哇哈哈哈哈哈哈哈"
    
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

def send_email(receiver):
    """
    :param receiver: String, 收件人的电子邮箱.
    :return Boolean: True 表示发送成功; False 表示发送失败.
    """
    # 配置信息
    content = '''
    亲爱的顾书豪先生:

    您于'''+datetime.today()+'''涉嫌搞怪东西被指控
    请于24小时内洗好屁股前往house 17 flat 6 c24报道，否则将会面临巨额赔偿或被记载入aiden的小本本

    希望阁下一切如常
    ——行舟人团队
    '''
    mail_host = "smtp.qq.com"
    mail_user = "xingzhouren"
    mail_pass = ""
    mail_postfix = "qq.com"
    mail_theme = "律师函"
    # 邮件封装
    msg_to = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = mail_theme
    msg['From'] = msg_to
    msg['To'] = receiver
    try:
        server = smtplib.SMTP_SSL(mail_host)
        server.ehlo(mail_host)
        # server = smtplib.SMTP()
        # server.connect(mail_host)  # 连接服务器
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(msg_to, receiver, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    print("最近遇到什么困难了吗？")
    print(respond(input()))
