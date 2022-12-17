def get_health_category_button():
  return {
      "type": "carousel",
      "contents": [
        {
          "type": "bubble",
          "hero": {
            "type": "image",
            "url": "https://i.imgur.com/nY8joFp.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://kb.commonhealth.com.tw/library"
            },
            "backgroundColor": "#FFFFFF"
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "請選擇類別",
                "weight": "bold",
                "size": "xl",
                "margin": "md"
              },
              {
                "type": "text",
                "text": "以獲取相關病症的列表",
                "margin": "md",
                "align": "start"
              }
            ],
            "action": {
              "type": "uri",
              "label": "View detail",
              "uri": "http://linecorp.com/",
              "altUri": {
                "desktop": "http://example.com/page/123"
              }
            }
          },
          "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "心臟 肝臟 肺臟",
                  "text": "選擇 心臟 肝臟 肺臟 分類"
                },
                "height": "sm"
              },
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "腸胃 牙齒 口腔",
                  "text": "選擇 腸胃 牙齒 口腔 分類"
                },
                "height": "sm"
              },
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "腎臟 泌尿道",
                  "text": "選擇 腎臟 泌尿道 分類"
                },
                "height": "sm"
              }
            ],
            "flex": 0
          },
          "styles": {
            "footer": {
              "separator": true
            }
          }
        },
        {
          "type": "bubble",
          "hero": {
            "type": "image",
            "url": "https://i.imgur.com/YshKdIG.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "uri": "https://kb.commonhealth.com.tw/library"
            },
            "backgroundColor": "#FFFFFF"
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "請選擇類別",
                "weight": "bold",
                "size": "xl",
                "margin": "md"
              },
              {
                "type": "text",
                "text": "以獲取相關病症的列表",
                "margin": "md"
              },
              {
                "type": "spacer"
              }
            ],
            "action": {
              "type": "uri",
              "label": "View detail",
              "uri": "http://linecorp.com/",
              "altUri": {
                "desktop": "http://example.com/page/123"
              }
            }
          },
          "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "眼 耳 鼻 喉",
                  "text": "選擇 眼 耳 鼻 喉 分類"
                },
                "height": "sm"
              },
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "骨 關節 皮膚",
                  "text": "選擇 骨 關節 皮膚 分類"
                },
                "height": "sm"
              },
              {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "身心 腦神經 婦科",
                  "text": "選擇 身心 腦神經 婦科 分類"
                },
                "height": "sm"
              }
            ],
            "flex": 0
          },
          "styles": {
            "footer": {
              "separator": true
            }
          }
        }
      ]
    }