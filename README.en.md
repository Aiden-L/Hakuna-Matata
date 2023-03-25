# Hakuna-Matata

#### Introduction
> This project is designed to help those who are experiencing setbacks, really hope it will help you.
> 
> It is normal to be confused and anxious when encountering difficulties, but don't be discouraged and stop moving forward, adjust your mindset in time and most importantly, don't give up, the storm will eventually pass and we will be greeted with a glorious sunny day.
> 
> Really love this song from The Lion King, so I'm quoting it here as the title of the project. No matter what happens, I hope everyone can face each day with optimism
> 
> Hakuna Matata, No Need to Worry, Everything Will be Fine
> 
> For a demo of the website, please visit [https://help.xingzhouren.club/](https://help.xingzhouren.club/)

#### Words from the author
> The original intention of doing this project was to help friends around me who were under a lot of stress, to inspire people with quotes and relieve stress, but halfway through the project, I thought it was an extreme failure. When a person's mood is at a low point, a correct word of encouragement is of little use, psychological problems are very difficult to solve, and what use can a word be. Although I was well aware of this, I still took the project on, and when I asked my friends around me to test it, the whole living ability of everyone was really far beyond my imagination. In the face of nonsensical questions, the AI's serious answers were more like a mockery of the difficulty itself, but in fact that's exactly the kind of spirit we need, to mock the difficulty instead of fearing it and stopping! When I saw the smiles on my friends' faces as they teased my AI, I felt that, in a sense, the project had been a success. Thank you all for your support, and stay tuned for more interesting updates on this project.
> 
> **This program is not professional psychological guidance and we hope you will have fun with it and seek help from a professional counsellor if you need it.**

## Hope you all have a good day!
[Click Here to Learn More about Hakuna Matata](https://www.youtube.com/watch?v=v34w65U98gI)

#### Software architecture
* Python 3.10
* Chat-GPT 3.5

#### Installation instructions
1. Command line input `pip install -r requirements.txt`
2. Create a new one in the project folder called `token.json`, and follow the below configuration
    ```json
    {
      "token": "put your token here"
    }
    ```

#### Instructions
1. Famous quotes generator demo: `motto.py`
2. Configuration filter `filter.json`
   - "rule": (list) List of keywords to be matched. When you enter one of them, you can apply the rule. Rules in English must be written in lowercase characters (case is ignored when matching).
   - "pass": (boolean) `true/false` Whether to pass user input into GPT after matching keywords, if `true`, The question has the probability of not entering GPT and directly returning the answer, if `false`, the "reply" result is returned directly
   - "reply": (list) Replace the list of replies by randomly selecting an item from the list as a reply (whether to incorporate GPT replies depends on the value of "pass")

