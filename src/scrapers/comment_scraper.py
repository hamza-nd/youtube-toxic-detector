import requests
import json

url = "https://m.youtube.com/youtubei/v1/next?prettyPrint=false"

payload = json.dumps({
  "context": {
    "client": {
      "hl": "en-GB",
      "gl": "LB",
      "remoteHost": "82.146.184.22",
      "deviceMake": "Google",
      "deviceModel": "Nexus 5",
      "visitorData": "CgtmNFV2QkVtNHQ1ayi5vKbBBjIKCgJMQhIEGgAgZw%3D%3D",
      "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36,gzip(gfe)",
      "clientName": "MWEB",
      "clientVersion": "2.20250516.01.00",
      "osName": "Android",
      "osVersion": "6.0",
      "originalUrl": "https://m.youtube.com/watch?v=nyPcE29NNBU",
      "playerType": "UNIPLAYER",
      "screenPixelDensity": 2,
      "platform": "MOBILE",
      "clientFormFactor": "SMALL_FORM_FACTOR",
      "configInfo": {
        "appInstallData": "CLm8psEGEIHNzhwQvZmwBRD-ns8cEOTn_xIQzN-uBRDJ5rAFEOfjzhwQtvXOHBCH1K8FEN_czhwQgoO4IhDtoc4cEODg_xIQ3rzOHBDfuM4cELjkzhwQudnOHBDZwbEFEIiHsAUQzq-vBRD2_v8SEJybzxwQ_vP_EhCJsM4cENeczxwQrKexBRDom88cEPDizhwQu9nOHBCZjbEFEI3MsAUQvurOHBDtoM8cELSMgBMQ4eywBRDphYATEJr0zhwQ2vfOHBD8ss4cEMyJzxwQh6zOHBC9tq4FEJmYsQUQ8JywBRCn484cENPhrwUQsInPHBCk9a4FEJ3QsAUQyfevBRC36v4SEL6KsAUQlP6wBRCI468FEOvo_hIQvZrPHBD2q7AFEIuCgBMQhPLOHBC5jYATEKGhzxwqMENBTVNIaFVkb0wyd0ROSGtCcFNDRXRiMTdndWU0UWJoLXdiNTdBUEozQVVkQnc9PQ%3D%3D",
        "coldConfigData": "CLm8psEGEO66rQUQvbauBRCmla8FEL6KsAUQ8JywBRCd0LAFEM_SsAUQ4_iwBRCanLEFEKa-sQUQ2cGxBRCS1LEFEPSyzhwQ_LLOHBDf3M4cEPbczhwQp-POHBDn484cEPDlzhwQhPLOHBCY9c4cENr3zhwQsInPHBDQjs8cEJ6QzxwQ6ZLPHBDIlM8cELiVzxwQ4JbPHBC9ms8cENWazxwQnJvPHBDdm88cEOibzxwQ15zPHBD-ns8cEKGhzxwaMkFPakZveDJTZVBNTXVhYzU1bHRCNDFPT3NWOVo4QVZ3QjdkNVA5SkJDcUxicjlNYlF3IjJBT2pGb3gwQjY4ejRNUGVtOTNOa1JfaEF1UEQ1OERQb0VBbkhhQlZ1YV91TzlWc0ZTdypsQ0FNU1RBMG51TjIzQXQ0VXpnMlhIN1lxdFFTX0ZmMERnNFdhRUpJSmhBTHFBc2taN0FBVkw1bXh0eC1GcEFXYXV3Yl9XY2FBQWdTTXF3YVRMcUdvQk4zZEJnV3hLSXVMQmMwdTVwSUZ1Mk09",
        "coldHashData": "CLm8psEGEhMyMDYyMzQ0NTIzMTY4OTA4ODM5GLm8psEGMjJBT2pGb3gyU2VQTU11YWM1NWx0QjQxT09zVjlaOEFWd0I3ZDVQOUpCQ3FMYnI5TWJRdzoyQU9qRm94MEI2OHo0TVBlbTkzTmtSX2hBdVBENThEUG9FQW5IYUJWdWFfdU85VnNGU3dCbENBTVNUQTBudU4yM0F0NFV6ZzJYSDdZcXRRU19GZjBEZzRXYUVKSUpoQUxxQXNrWjdBQVZMNW14dHgtRnBBV2F1d2JfV2NhQUFnU01xd2FUTHFHb0JOM2RCZ1d4S0l1TEJjMHU1cElGdTJNPQ%3D%3D",
        "hotHashData": "CLm8psEGEhM0NjU5MzQzNDkwNzc4NjExOTQ1GLm8psEGKJTk_BIopdD9Eiiekf4SKMjK_hIot-r-EijBg_8SKLSj_xIomfL_Eij-8_8SKPb-_xIox4CAEyiLgoATKLSDgBMo8YWAEyjzhYATKNeGgBMo_ouAEyi0jIATKLmNgBMyMkFPakZveDJTZVBNTXVhYzU1bHRCNDFPT3NWOVo4QVZ3QjdkNVA5SkJDcUxicjlNYlF3OjJBT2pGb3gwQjY4ejRNUGVtOTNOa1JfaEF1UEQ1OERQb0VBbkhhQlZ1YV91TzlWc0ZTd0I0Q0FNU0lRMEtvdGY2RmE3QkJwTk44Z3E1QkJVWDNjX0NETWFuN1F2WXpRbWx3QVhXVnc9PQ%3D%3D"
      },
      "screenDensityFloat": 2.0000000596046448,
      "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
      "timeZone": "Asia/Beirut",
      "browserName": "Chrome Mobile",
      "browserVersion": "136.0.0.0",
      "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "deviceExperimentId": "ChxOelV3TlRjd05ESXlNamM0T1RFeU1qYzFNZz09ELm8psEGGLm8psEG",
      "rolloutToken": "CMnHy-Cl47GKowEQo4DPkcejjAMYrtvI_ZSqjQM%3D",
      "screenWidthPoints": 672,
      "screenHeightPoints": 787,
      "utcOffsetMinutes": 180,
      "connectionType": "CONN_CELLULAR_4G",
      "memoryTotalKbytes": "8000000",
      "mainAppWebInfo": {
        "graftUrl": "https://m.youtube.com/watch?v=nyPcE29NNBU",
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
    "clientScreenNonce": "Cl_SX5Yg-tUH-4D1",
    "clickTracking": {
      "clickTrackingParams": "CCcQuy8YACITCOTovtTQrI0DFVZETwQdVOIRwA=="
    },
    "adSignalsInfo": {
      "params": [
        {
          "key": "dt",
          "value": "1747557945183"
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
          "value": "8"
        },
        {
          "key": "u_h",
          "value": "787"
        },
        {
          "key": "u_w",
          "value": "672"
        },
        {
          "key": "u_ah",
          "value": "787"
        },
        {
          "key": "u_aw",
          "value": "672"
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
          "value": "672"
        },
        {
          "key": "brdim",
          "value": "0,0,0,0,672,0,672,787,672,787"
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
      "bid": "ANyPxKrh11iZkbuKkS11TifX2_bIpIJSiiMa7AZMxsiCUH9ayTl2NdOHFWRb4O2qx54fnAbc1EAx"
    }
  },
  "continuation": "Eg0SC255UGNFMjlOTkJVGAYyVSIuIgtueVBjRTI5Tk5CVTAAeAKqAhpVZ3kxWjF6SFlXOWR5c1dYTmRWNEFhQUJBZzABQiFlbmdhZ2VtZW50LXBhbmVsLWNvbW1lbnRzLXNlY3Rpb24%3D"
})
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'SAPISIDHASH 1747557969_b19c2fbec493fc1d1e0538885a66a3537c4d47cc_u SAPISID1PHASH 1747557969_b19c2fbec493fc1d1e0538885a66a3537c4d47cc_u SAPISID3PHASH 1747557969_b19c2fbec493fc1d1e0538885a66a3537c4d47cc_u',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'origin': 'https://m.youtube.com',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://m.youtube.com/watch?v=nyPcE29NNBU',
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
  'x-client-data': 'CJa2yQEIorbJAQipncoBCOaJywEIkqHLAQiRo8sBCIWgzQEIuMjNAQj9pc4BCNzWzgEIiuTOAQjd7c4BCOTtzgEI3u7OAQiW8M4BGNjozgE=',
  'x-goog-authuser': '0',
  'x-goog-visitor-id': 'CgtmNFV2QkVtNHQ1ayi5vKbBBjIKCgJMQhIEGgAgZw%3D%3D',
  'x-origin': 'https://m.youtube.com',
  'x-youtube-bootstrap-logged-in': 'true',
  'x-youtube-client-name': '2',
  'x-youtube-client-version': '2.20250516.01.00',
  'Cookie': 'LOGIN_INFO=AFmmF2swRQIhAI7NrxeLDax8Fux6aNIKew9gPZ5r6WkAFqSLsXbQoK2rAiApNxyiC0d2VMv30AvjcpMXg2KLhlaLWEUnV3b508MIRw:QUQ3MjNmemF2MDJDVWtWcEd1cXlSUFZKdWpZSGhEOU1Nc2hwX2hveUhvdzhwb3RQaWRSLWItUDVVQnhYNzRWR3dfV1Atc3VBeU8wM0t1TEdGakZBY2hmeFd2cE9aV2RxelVGN0hxTzM1LWhwMHlId3ZUVVRuUlZpV3d3clpRR1NmdTM3TGRINXIyQ2QyMTVQbFYzYTAxNGZlY0VMNW11Rjhn; VISITOR_INFO1_LIVE=f4UvBEm4t5k; VISITOR_PRIVACY_METADATA=CgJMQhIEGgAgZw%3D%3D; HSID=AAH2STxXK1nDbNrpI; SSID=AgclPAMoOifsdxwvD; APISID=MLkUDswvs1WuHOH-/AvL19Ui7VaLSOtiKT; SAPISID=Y2oZAsk8-goWQUi-/AVBCja2Ym-q2or8lT; __Secure-1PAPISID=Y2oZAsk8-goWQUi-/AVBCja2Ym-q2or8lT; __Secure-3PAPISID=Y2oZAsk8-goWQUi-/AVBCja2Ym-q2or8lT; SID=g.a000wwh-Lo2elRKrf35h7bfJbDgfObx9Y5QN7bpO9Qa4FAbXtbkOeX1-GUkzaIrHHrhj0hOxwAACgYKAdUSARASFQHGX2MiY_xSkAS9235rLpZOR3eqXxoVAUF8yKpbYthBzENDoxPaNl4Pgwu60076; __Secure-1PSID=g.a000wwh-Lo2elRKrf35h7bfJbDgfObx9Y5QN7bpO9Qa4FAbXtbkOAArsfrUlIu1hQs6xaz4JwwACgYKAYASARASFQHGX2MiWe2Vece4FESXgrz1aQhwVBoVAUF8yKox9jdo5lEHHfgYyMGjBLPh0076; __Secure-3PSID=g.a000wwh-Lo2elRKrf35h7bfJbDgfObx9Y5QN7bpO9Qa4FAbXtbkOQJVc-Z3mCZ6YQvK-FGU50wACgYKAd4SARASFQHGX2MiNajrSk23hF_33gdYAgKveBoVAUF8yKrLOvxvo6H5deS3ZWfGAAcI0076; YSC=l1xS9dzjh5Y; __Secure-ROLLOUT_TOKEN=CMnHy-Cl47GKowEQo4DPkcejjAMYrtvI_ZSqjQM%3D; PREF=f4=4000000&tz=Asia.Beirut&f7=100&f5=20000; __Secure-1PSIDTS=sidts-CjIBjplskM75aw8zEAwT597GDrNH4abYl7SBxxtOL_-Qa_byLz5AHaEjdZbgA9-jqtz1xRAA; __Secure-3PSIDTS=sidts-CjIBjplskM75aw8zEAwT597GDrNH4abYl7SBxxtOL_-Qa_byLz5AHaEjdZbgA9-jqtz1xRAA; SIDCC=AKEyXzXiq_ru-wEGdaNgYNXqe0WaHXbR-T1wBjXayciGPfpunTwI2pbRz7Is-1lon1aQLcI--A; __Secure-1PSIDCC=AKEyXzVl1ewpmZQDyAT1rBeRkCdJzm9MEMy_zidyToMrk3ZvXQc5bgdRcZtSw3L0uf6B33QKrw; __Secure-3PSIDCC=AKEyXzXCiun8EwOHpYVKvTAUn4whaw1ulPAuxYcyjB8A1v93XMDXXLlnS9UeBpjncg28ToGOqPw; SIDCC=AKEyXzUDwK3MyYat64aCclog9mYZ-uU8iCC4Crac6E84-027PkkF0a23r8zhP1-_YFmXJ24qDQ; __Secure-1PSIDCC=AKEyXzUHbKHmxyYJcPZuATOkKlM4VO2uUxnCrWHLVOzjAZ3ZhrZpzjhWExjStOnCeTGkCAOdKg; __Secure-3PSIDCC=AKEyXzXiUgvNwGwO2dT_zQ__koyCteuqQ-74QdR47j8rnos-C_eNiHfPrBAI8zEUQ_z5fOaS0yY'
}

response = requests.request("POST", url, headers=headers, data=payload).json()


import json

# Parse the JSON data from paste-2.txt
def extract_comments(json_data):
    comments = []
    
    # Check if we have a valid JSON response
    if not json_data:
        return "No valid JSON data found"
    
    # Try to locate comment threads in the response
    try:
        # The main response has onResponseReceivedEndpoints containing continuationItems
        endpoints = json_data.get("onResponseReceivedEndpoints", [])
        
        for endpoint in endpoints:
            # Look for reloadContinuationItemsCommand which contains the comments
            if "reloadContinuationItemsCommand" in endpoint:
                continuation_items = endpoint["reloadContinuationItemsCommand"].get("continuationItems", [])
                
                for item in continuation_items:
                    # Check if this is a comment thread
                    if "commentThreadRenderer" in item:
                        thread = item["commentThreadRenderer"]
                        
                        # Extract the main comment
                        if "comment" in thread and "commentRenderer" in thread["comment"]:
                            comment_renderer = thread["comment"]["commentRenderer"]
                            
                            # Extract author info
                            author = ""
                            if "authorText" in comment_renderer and "runs" in comment_renderer["authorText"]:
                                author = comment_renderer["authorText"]["runs"][0]["text"]
                            
                            # Extract comment text
                            text = ""
                            if "contentText" in comment_renderer and "runs" in comment_renderer["contentText"]:
                                text = comment_renderer["contentText"]["runs"][0]["text"]
                            
                            # Extract timestamp
                            time = ""
                            if "publishedTimeText" in comment_renderer and "runs" in comment_renderer["publishedTimeText"]:
                                time = comment_renderer["publishedTimeText"]["runs"][0]["text"]
                            
                            # Extract like count
                            likes = ""
                            if "voteCount" in comment_renderer and "runs" in comment_renderer["voteCount"]:
                                likes = comment_renderer["voteCount"]["runs"][0]["text"]
                            
                            # Extract reply count
                            replies = ""
                            if "replyCount" in comment_renderer:
                                replies = str(comment_renderer["replyCount"])
                            
                            comment_info = {
                                "author": author,
                                "text": text,
                                "time": time,
                                "likes": likes,
                                "replies": replies
                            }
                            
                            comments.append(comment_info)
    
    except Exception as e:
        return f"Error parsing comments: {str(e)}"
    
    return comments

# Load the JSON data from the provided content
try:
    
    data = response
    comments = extract_comments(data)
    
    print(f"Found {len(comments)} comments:")
    for i, comment in enumerate(comments, 1):
        print(f"\nComment {i}:")
        print(f"Author: {comment['author']}")
        print(f"Text: {comment['text']}")
        print(f"Time: {comment['time']}")
        print(f"Likes: {comment['likes']}")
        print(f"Replies: {comment['replies']}")
        
except Exception as e:
    print(f"Error: {str(e)}")