try:
    from aiohttp import web
    import google.generativeai as genai
except ImportError:
    import os

    os.system("pip install aiohttp google-generativeai")
    from aiohttp import web
    import google.generativeai as genai

genai.configure(api_key="API_KEY_HERE")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

SYSTEM_PROMPT = "I Will feed u a question and 4 options, just return the correct option number nothing else. (1-4)"
chat.send_message(SYSTEM_PROMPT)

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
}


async def handle(request):
    data = await request.json()
    question = data["question"]
    options = data["options"]

    resp = chat.send_message(question + " " + "\n".join(options))
    print(resp.text, question, options)
    return web.json_response({"response": resp.text}, headers=CORS_HEADERS)


async def handle_options(request):
    return web.Response(headers=CORS_HEADERS)


app = web.Application()
app.router.add_post("/", handle)
app.router.add_options("/", handle_options)

web.run_app(app, port=8080)
