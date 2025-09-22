from maestro.openai import OpenAI

def shakespeare_bot():
    # Same exact usage as real OpenAI SDK - uses OPENAI_API_KEY env var
    client = OpenAI()
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are William Shakespeare, the poet. Respond in poetry."},
                {"role": "user", "content": "Romeo, Romeo, wherefore art thou Romeo?"}
            ],
            temperature=0.7,
            max_tokens=50
        )
        
        print("✅ SDK replacement works!")
        print(f"Response: {response}")
        return True
        
    except Exception as e:
        print(f"❌Chat Completions SDK test failed: {e}")
        return False

# def test_drop_in_replacement_responses():
#     client = OpenAI()
#
#     try:
#         response = client.responses.create(
#                 model="gpt-4o-mini",
#                 input="How are you?"
#                 )
#         print("✅ SDK replacement works!")
#         print(f"Response: {response}")
#         return True 
#     except Exception as e:
#         print(f"NOPE. {e}")
#         return False 
#

if __name__ == "__main__":
    print("User: What is love?", end="\nGPT: ")
    shakespeare_bot()
    # print("Testing v1/responses")
    # test_drop_in_replacement_responses()
