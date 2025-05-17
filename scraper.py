import requests
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"testing the api": "api tested"}

url = "https://m.youtube.com/youtubei/v1/next?prettyPrint=false"

payload = json.dumps({
  "context": {
    "client": {
      "hl": "en-GB",
      "gl": "LB",
      "remoteHost": "82.146.184.22",
      "deviceMake": "Google",
      "deviceModel": "Nexus 5",
      "visitorData": "CgtmNFV2QkVtNHQ1ayihq5zBBjIKCgJMQhIEGgAgZw%3D%3D",
      "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36,gzip(gfe)",
      "clientName": "MWEB",
      "clientVersion": "2.20250515.01.00",
      "osName": "Android",
      "osVersion": "6.0",
      "originalUrl": "https://m.youtube.com/watch?v=zp_S2Uwjb-M",
      "playerType": "UNIPLAYER",
      "screenPixelDensity": 2,
      "platform": "MOBILE",
      "clientFormFactor": "SMALL_FORM_FACTOR",
      "configInfo": {
        "appInstallData": "CKGrnMEGEMn3rwUQ9v7_EhDM364FEOibzxwQ_vP_EhC9ms8cEIfUrwUQ4OD_EhCk9a4FEOvo_hIQzq-vBRCLgoATELSMgBMQ5Of_EhDtoc4cEPDizhwQ4eywBRCBzc4cEIiHsAUQ9quwBRCn484cEJr0zhwQ3rzOHBCHrM4cENr3zhwQvurOHBDZwbEFEL2ZsAUQu9nOHBC-irAFEJmYsQUQuOTOHBCcm88cEMnmsAUQ_p7PHBCU_rAFELnZzhwQ37jOHBCsp7EFEJmNsQUQibDOHBDtoM8cEN_czhwQt-r-EhCd0LAFEOmFgBMQ0-GvBRDMic8cEOfjzhwQsInPHBDwnLAFEI3MsAUQiOOvBRC9tq4FEPyyzhwQ15zPHBC29c4cEITyzhwqMENBTVNIaFVkb0wyd0ROSGtCcFNDRXRiMTdndWU0UWJoLXdiNTdBUEozQVVkQnc9PQ%3D%3D",
        "coldConfigData": "CKGrnMEGEO66rQUQvbauBRCmla8FEL6KsAUQ8JywBRCd0LAFEM_SsAUQ4_iwBRCanLEFEKa-sQUQ2cGxBRCS1LEFEPSyzhwQ_LLOHBDf3M4cEPbczhwQp-POHBDn484cEPDlzhwQhPLOHBCY9c4cENr3zhwQsInPHBDHis8cENCOzxwQnpDPHBDpks8cEMiUzxwQuJXPHBDgls8cEL2azxwQ1ZrPHBCcm88cEN2bzxwQ6JvPHBDXnM8cEP6ezxwaMkFPakZveDJTZVBNTXVhYzU1bHRCNDFPT3NWOVo4QVZ3QjdkNVA5SkJDcUxicjlNYlF3IjJBT2pGb3gwQjY4ejRNUGVtOTNOa1JfaEF1UEQ1OERQb0VBbkhhQlZ1YV91TzlWc0ZTdypsQ0FNU1RBMG51TjIzQXQ0VXpnMlhIN1lxdFFTX0ZmMERnNFdhRUpJSmhBTHFBc2taN0FBVkw1bXh0eC1GcEFXYXV3Yl9XY2FBQWdTTXF3YVRMcUdvQk4zZEJnV3hLSXVMQmMwdTVwSUZ1Mk09",
        "coldHashData": "CKGrnMEGEhQxNTc4OTIxOTgzNTQxNzA3NzQ2NBihq5zBBjIyQU9qRm94MlNlUE1NdWFjNTVsdEI0MU9Pc1Y5WjhBVndCN2Q1UDlKQkNxTGJyOU1iUXc6MkFPakZveDBCNjh6NE1QZW05M05rUl9oQXVQRDU4RFBvRUFuSGFCVnVhX3VPOVZzRlN3QmxDQU1TVEEwbnVOMjNBdDRVemcyWEg3WXF0UVNfRmYwRGc0V2FFSklKaEFMcUFza1o3QUFWTDVteHR4LUZwQVdhdXdiX1djYUFBZ1NNcXdhVExxR29CTjNkQmdXeEtJdUxCYzB1NXBJRnUyTT0%3D",
        "hotHashData": "CKGrnMEGEhM0NjU5MzQzNDkwNzc4NjExOTQ1GKGrnMEGKJTk_BIopdD9Eiiekf4SKMjK_hIot-r-EijBg_8SKLSj_xIomfL_Eij-8_8SKPb-_xIox4CAEyiLgoATKLSDgBMo8YWAEyjzhYATKNeGgBMo5YuAEyj-i4ATKLSMgBMyMkFPakZveDJTZVBNTXVhYzU1bHRCNDFPT3NWOVo4QVZ3QjdkNVA5SkJDcUxicjlNYlF3OjJBT2pGb3gwQjY4ejRNUGVtOTNOa1JfaEF1UEQ1OERQb0VBbkhhQlZ1YV91TzlWc0ZTd0I0Q0FNU0lRMEtvdGY2RmE3QkJwTk44Z3E1QkJVWDNjX0NETWFuN1F2WXpRbWx3QVhXVnc9PQ%3D%3D"
      },
      "screenDensityFloat": 2.0000000596046448,
      "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
      "timeZone": "Asia/Beirut",
      "browserName": "Chrome Mobile",
      "browserVersion": "136.0.0.0",
      "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "deviceExperimentId": "ChxOelV3TkRrNU1UQTROakV6TXpNeU1USTNPUT09EKGrnMEGGKGrnMEG",
      "rolloutToken": "CMnHy-Cl47GKowEQo4DPkcejjAMYhuXY986njQM%3D",
      "screenWidthPoints": 777,
      "screenHeightPoints": 787,
      "utcOffsetMinutes": 180,
      "connectionType": "CONN_CELLULAR_4G",
      "memoryTotalKbytes": "8000000",
      "mainAppWebInfo": {
        "graftUrl": "https://m.youtube.com/watch?v=zp_S2Uwjb-M",
        "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
        "isWebNativeShareAvailable": True
      }
    },
    "user": {
      "lockedSafetyMode": False
    },
    "request": {
      "useSsl": True,
      "internalExperimentFlags": [],
      "consistencyTokenJars": []
    },
    "clientScreenNonce": "VIK8Cnafqagw1G0X",
    "clickTracking": {
      "clickTrackingParams": "CFYQuy8YACITCN2NvI7mp40DFWOBsQMddQYHUQ=="
    },
    "adSignalsInfo": {
      "params": [
        {
          "key": "dt",
          "value": "1747391913845"
        },
        {
          "key": "flash",
          "value": "0"
        },
        {
          "key": "frm",
          "value": "0"
        },
        {
          "key": "u_tz",
          "value": "180"
        },
        {
          "key": "u_his",
          "value": "3"
        },
        {
          "key": "u_h",
          "value": "787"
        },
        {
          "key": "u_w",
          "value": "777"
        },
        {
          "key": "u_ah",
          "value": "787"
        },
        {
          "key": "u_aw",
          "value": "777"
        },
        {
          "key": "u_cd",
          "value": "24"
        },
        {
          "key": "bc",
          "value": "31"
        },
        {
          "key": "bih",
          "value": "787"
        },
        {
          "key": "biw",
          "value": "777"
        },
        {
          "key": "brdim",
          "value": "0,0,0,0,777,0,777,787,777,787"
        },
        {
          "key": "vis",
          "value": "1"
        },
        {
          "key": "wgl",
          "value": "true"
        },
        {
          "key": "ca_type",
          "value": "image"
        }
      ],
      "bid": "ANyPxKqohgjTh3-H1-vSiTwsvv-AkT93xwmPA8bX2UzBrQgXNvBsc-G9BFEDPUDbTOfiZ9pEp2uN"
    }
  },
  "continuation": "Eg0SC3pwX1MyVXdqYi1NGAYyVSIuIgt6cF9TMlV3amItTTAAeAKqAhpVZ3lLNUktWXVVZ3Z1YmVQQ1BWNEFhQUJBZzABQiFlbmdhZ2VtZW50LXBhbmVsLWNvbW1lbnRzLXNlY3Rpb24%3D"
})
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'SAPISIDHASH 1747391928_1e3c79f4cf45394f0a5e84462fcec87fa4ea8e37_u SAPISID1PHASH 1747391928_1e3c79f4cf45394f0a5e84462fcec87fa4ea8e37_u SAPISID3PHASH 1747391928_1e3c79f4cf45394f0a5e84462fcec87fa4ea8e37_u',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'origin': 'https://m.youtube.com',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://m.youtube.com/watch?v=zp_S2Uwjb-M',
  'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
  'sec-ch-ua-arch': '""',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-form-factors': '',
  'sec-ch-ua-full-version': '"136.0.7103.94"',
  'sec-ch-ua-full-version-list': '"Chromium";v="136.0.7103.94", "Google Chrome";v="136.0.7103.94", "Not.A/Brand";v="99.0.0.0"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-model': '"Nexus 5"',
  'sec-ch-ua-platform': '"Android"',
  'sec-ch-ua-platform-version': '"6.0"',
  'sec-ch-ua-wow64': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'same-origin',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
  'x-client-data': 'CJa2yQEIorbJAQipncoBCOaJywEIkqHLAQiRo8sBCIWgzQEIuMjNAQj9pc4BCNzWzgEI3e3OAQjk7c4BCN7uzgEIlvDOARjY6M4B',
  'x-goog-authuser': '0',
  'x-goog-visitor-id': 'CgtmNFV2QkVtNHQ1ayihq5zBBjIKCgJMQhIEGgAgZw%3D%3D',
  'x-origin': 'https://m.youtube.com',
  'x-youtube-bootstrap-logged-in': 'true',
  'x-youtube-client-name': '2',
  'x-youtube-client-version': '2.20250515.01.00',
  'Cookie': 'LOGIN_INFO=AFmmF2swRQIhAI7NrxeLDax8Fux6aNIKew9gPZ5r6WkAFqSLsXbQoK2rAiApNxyiC0d2VMv30AvjcpMXg2KLhlaLWEUnV3b508MIRw:QUQ3MjNmemF2MDJDVWtWcEd1cXlSUFZKdWpZSGhEOU1Nc2hwX2hveUhvdzhwb3RQaWRSLWItUDVVQnhYNzRWR3dfV1Atc3VBeU8wM0t1TEdGakZBY2hmeFd2cE9aV2RxelVGN0hxTzM1LWhwMHlId3ZUVVRuUlZpV3d3clpRR1NmdTM3TGRINXIyQ2QyMTVQbFYzYTAxNGZlY0VMNW11Rjhn; VISITOR_INFO1_LIVE=f4UvBEm4t5k; VISITOR_PRIVACY_METADATA=CgJMQhIEGgAgZw%3D%3D; HSID=AAH2STxXK1nDbNrpI; SSID=AgclPAMoOifsdxwvD; APISID=MLkUDswvs1WuHOH-/AvL19Ui7VaLSOtiKT; SAPISID=Y2oZAsk8-goWQUi-/AVBCja2Ym-q2or8lT; __Secure-1PAPISID=Y2oZAsk8-goWQUi-/AVBCja2Ym-q2or8lT; __Secure-3PAPISID=Y2oZAsk8-goWQUi-/AVBCja2Ym-q2or8lT; SID=g.a000wwh-Lo2elRKrf35h7bfJbDgfObx9Y5QN7bpO9Qa4FAbXtbkOeX1-GUkzaIrHHrhj0hOxwAACgYKAdUSARASFQHGX2MiY_xSkAS9235rLpZOR3eqXxoVAUF8yKpbYthBzENDoxPaNl4Pgwu60076; __Secure-1PSID=g.a000wwh-Lo2elRKrf35h7bfJbDgfObx9Y5QN7bpO9Qa4FAbXtbkOAArsfrUlIu1hQs6xaz4JwwACgYKAYASARASFQHGX2MiWe2Vece4FESXgrz1aQhwVBoVAUF8yKox9jdo5lEHHfgYyMGjBLPh0076; __Secure-3PSID=g.a000wwh-Lo2elRKrf35h7bfJbDgfObx9Y5QN7bpO9Qa4FAbXtbkOQJVc-Z3mCZ6YQvK-FGU50wACgYKAd4SARASFQHGX2MiNajrSk23hF_33gdYAgKveBoVAUF8yKrLOvxvo6H5deS3ZWfGAAcI0076; YSC=l1xS9dzjh5Y; __Secure-ROLLOUT_TOKEN=CMnHy-Cl47GKowEQo4DPkcejjAMYhuXY986njQM%3D; __Secure-1PSIDTS=sidts-CjIBjplskMQzCIYp7uFPNJD54tjHnfnRhpaqCl5pfKr9L9v5FZlIU1a49QX-miJtCimaOhAA; __Secure-3PSIDTS=sidts-CjIBjplskMQzCIYp7uFPNJD54tjHnfnRhpaqCl5pfKr9L9v5FZlIU1a49QX-miJtCimaOhAA; PREF=f4=4000000&tz=Asia.Beirut&f7=100&f5=20000; SIDCC=AKEyXzWQ6zjoa-iZqyVnY_4cYpL4uZzYpCC0mkVkZCekLoPjTjbskfb2V8adofsv54prqz0w5Q; __Secure-1PSIDCC=AKEyXzX2tVGOJOn-rAvztrQ-6teb3aO10Poxb2tVSymxb1t52Cps6hliuDssC7qW3q8nLJG14w; __Secure-3PSIDCC=AKEyXzXvJoi2lTgP-ldfPEMmrCEYHDIv2a4a9yCIioLrYXjX1YeAsTKjuZns1JFaR-_bmiSuVLM; SIDCC=AKEyXzWUOoNmNxE6WW_JpM3zIJGi_wvkbXdcccZjIaJ165d2ZMj0rgP0nomcG9lnL_2luQQgHw; __Secure-1PSIDCC=AKEyXzX9jQJZB46wUCs-F0ioNa27TKgflJRBsuWw3vx4pgq0nzd5rReaUkfDfSnzKLjrjS8A0Q; __Secure-3PSIDCC=AKEyXzU2uAcHJ2N99cegcXCMN_ToVbMqj4C_FMWItNtFLLSFYcVaeU9bSkFIFV-ar-81mOcMyzg'
}

response = requests.request("POST", url, headers=headers, data=payload)

@app.get("/comments")
def comments():
    response = requests.post(url, headers=headers, data=payload)
    return response.json()


