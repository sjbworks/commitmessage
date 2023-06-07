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
prompt = f"Given the following git diff output, suggest an appropriate commit message in English, with a lowercase prefix at the beginning:\n\n{diff_output}\n\nPrefix rules should be as follows\n\nfeat: A new feature\n\nfix: A bug fix\n\ndocs: Documentation only changes\n\nstyle: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)\n\nrefactor: A code change that neither fixes a bug nor adds a feature\n\nperf: A code change that improves performance\n\ntest: Adding missing or correcting existing tests\n\nchore: Changes to the build process or auxiliary tools and libraries such as documentation generation\n\nCommit message:"
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