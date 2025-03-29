from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"取得したAPIキー: {api_key}")
print(f"環境変数の取得に成功しました: {api_key is not None}")
print(f"環境変数の取得に成功しました: {api_key is not None}")
print(f"環境変数の取得に成功しました: {api_key is not None}")   

