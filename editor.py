# Run this code to test your env setup to see everything works fine.
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

# Note: OpenAI basically no longer offers a Free Tier. 
# Any use of the API requires the addition of a minimum of $5. 
# There might just be a small system lag regarding the “visible” update of your tier under the above link. 
# I hope this helps.
# Learn more: https://community.openai.com/t/usage-tier-free-to-tier-1/919150