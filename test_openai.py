from openai import OpenAI
from keys import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY) # client 客戶端 > 用來跟 OpenAI 伺服器溝通的物件。

response = client.responses.create(
    model="gpt-5",
    input="請幫我擬一份新尖兵結案報告的大綱，希望報告可以對我以後的履歷也有幫助。"
)

print(response.output_text)