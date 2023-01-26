import openai
import telegram

# Replace with your OpenAI API key
openai.api_key = "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"

bot_token = '5808195542:AAE_rfY-dVDMQQ3DqZ1erO9tOsPEfn8tZ1c' 
bot = telegram.Bot(token=bot_token)

def send_message(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

def generate_text(prompt):
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2048, n=1,stop=None,temperature=0.5)
    message = completions.choices[0].text
    return message.strip()

def handle_message(message):
    chat_id = message.chat.id
    text = message.text
    response = generate_text(text)
    send_message(chat_id, response)

bot.set_webhook(url='https://octo.hk/32DN8d41twBgmFvulnFk')
