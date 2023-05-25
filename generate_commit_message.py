import openai
import os
import sys

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

# APIキーを設定
openai.api_key = api_key

# 標準入力からgit diffの出力を取得
diff_output = sys.stdin.read()

# GPT-3へのリクエストを作成
prompt = f"Given the following git diff output, suggest an appropriate commit message in English:\n\n{diff_output}\n\nCommit message:"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)

# コミットメッセージを取得して表示
commit_message = response.choices[0].text.strip()
print(commit_message)