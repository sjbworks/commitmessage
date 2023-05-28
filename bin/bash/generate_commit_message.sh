export OPENAI_API_KEY=$OPENAI_API_KEY
git diff --staged | python3 generate_commit_message.py