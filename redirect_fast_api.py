# RUN
# cd e-commerce_software/Marketplaces/ideasoft/
# uvicorn redirect_fast_api:app --reload --port 8000
###
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")

    if code:
        # Burada gelen code ile access token alırsın (isteğe bağlı)
        return HTMLResponse(f"""
            <h1>✅ Access Token Alındı</h1>
            <p><b>Access Token:</b> {code}</p>
            <p><b>State:</b> {state}</p>
            <p>Bu kodu kullanarak token alabilirsin.</p>
        """)
    else:
        return HTMLResponse("<h1> ❌ Authorization Code Bulunamadı.</h1>")





############### VERSION 2 ###############
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# import requests
#
#
# app = FastAPI()
# # Bu bilgileri kendi IdeaSoft uygulamandan al
#
#
# CLIENT_ID = "2l165ha7118g8804gw8cow8cc4s4c0oocwoscw4sgosw4wowks"
# CLIENT_SECRET = "2mv7ryuplkqocsc0okgw8sskksw4kcg8cw4ws480kokwsksok"
# REDIRECT_URI = "http://localhost:8000/callback"
# TOKEN_URL = "https://sogutlusilver.myideasoft.com/oauth/v2/token"
# STATE='2b33fdd45jbevd6nam'
#
# @app.get("/callback")
# async def callback(request: Request):
#     code = request.query_params.get("code")
#     state = request.query_params.get("state")
#
#     if code:
#         # Token almak için POST isteği gönder
#         token_response = requests.post(TOKEN_URL, data={
#             "grant_type": "authorization_code",
#             "code": code,
#             "redirect_uri": REDIRECT_URI,
#             "client_id": CLIENT_ID,
#             "client_secret": CLIENT_SECRET,
#         })
#
#         if token_response.status_code == 200:
#             token_data = token_response.json()
#             return HTMLResponse(f"""
#                 <h1>✅ Access Token Alındı</h1>
#                 <p><b>Access Token:</b> {token_data['access_token']}</p>
#                 <p><b>Refresh Token:</b> {token_data.get('refresh_token')}</p>
#                 <p><b>Expires In:</b> {token_data.get('expires_in')} saniye</p>
#             """)
#         else:
#             return HTMLResponse(f"<h1>❌ Token alınamadı</h1><pre>{token_response.text}</pre>")
#
#     return HTMLResponse("<h1>❌ Authorization Code bulunamadı</h1>")
