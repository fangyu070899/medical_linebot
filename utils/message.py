
def get_health_category_button():
  return  {
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
                    "separator": True
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
                    "separator": True
                  }
                }
              }
            ]
          }

def get_category_button_3(c1,c2,c3):
  return  {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "想了解哪個部位的病症?",
                  "size": "md",
                  "weight": "bold",
                  "style": "normal"
                }
              ]
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
                    "label": f"{c1}",
                    "text": f"選擇 {c1} 分類"
                  },
                  "height": "sm"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": f"{c2}",
                    "text": f"選擇 {c2} 分類"
                  },
                  "height": "sm"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": f"{c3}",
                    "text": f"選擇 {c3} 分類"
                  },
                  "height": "sm"
                }
              ],
              "flex": 0
            },
            "styles": {
              "footer": {
                "separator": True
              }
            }
          }

def get_category_button_2(c1,c2):
  return  {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "想了解哪個部位的病症?",
                  "size": "md",
                  "weight": "bold",
                  "style": "normal"
                }
              ]
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
                    "label": f"{c1}",
                    "text": f"選擇 {c1} 分類"
                  },
                  "height": "sm"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": f"{c2}",
                    "text": f"選擇 {c2} 分類"
                  },
                  "height": "sm"
                }
              ],
              "flex": 0
            },
            "styles": {
              "footer": {
                "separator": True
              }
            }
          }

def get_symptom_category_button():
  return {
            "type": "bubble",
            "hero": {
              "type": "image",
              "url": "https://i.imgur.com/fN0ghw0.png",
              "size": "full",
              "aspectRatio": "20:13",
              "aspectMode": "cover",
              "action": {
                "type": "uri",
                "uri": "https://kb.commonhealth.com.tw/library"
              }
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "請選擇族群",
                  "weight": "bold",
                  "size": "xl"
                }
              ]
            },
            "footer": {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "message",
                    "label": "男性",
                    "text": "選擇 男性 分類"
                  }
                },
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "message",
                    "label": "女性",
                    "text": "選擇 女性 分類"
                  }
                },
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "message",
                    "label": "老年",
                    "text": "選擇 老年 分類"
                  }
                },
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "message",
                    "label": "幼童",
                    "text": "選擇 幼童 分類"
                  }
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [],
                  "margin": "sm"
                }
              ],
              "flex": 0
            }
          }

def get_diet_button():
  return {
          "type": "carousel",
          "contents": [
            {
              "type": "bubble",
              "hero": {
                "type": "image",
                "url": "https://i.imgur.com/EM2dvnB.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://kb.commonhealth.com.tw/library/category/13"
                },
                "backgroundColor": "#FFFFFF"
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "weight": "bold",
                    "size": "xl",
                    "margin": "md",
                    "text": "高血壓飲食"
                  },
                  {
                    "type": "text",
                    "text": "高血壓患者需注意的飲食方式",
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
                      "label": "飲食少油",
                      "text": "高血壓飲食：飲食少油"
                    },
                    "height": "sm"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": "飲食少鹽",
                      "text": "高血壓飲食：飲食少鹽"
                    },
                    "height": "sm"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "text": "高血壓飲食：限鈉飲食、低鈉飲食",
                      "label": "限鈉飲食、低鈉飲食"
                    },
                    "height": "sm"
                  }
                ],
                "alignItems": "center",
                "offsetTop": "none"
              },
              "styles": {
                "footer": {
                  "separator": True
                }
              }
            },
            {
              "type": "bubble",
              "hero": {
                "type": "image",
                "url": "https://i.imgur.com/DaRhnlw.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://kb.commonhealth.com.tw/library/category/13"
                },
                "backgroundColor": "#FFFFFF"
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "weight": "bold",
                    "size": "xl",
                    "margin": "md",
                    "text": "高血壓飲食"
                  },
                  {
                    "type": "text",
                    "text": "高血壓患者需注意的飲食方式",
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
                      "label": "飲食多蔬果",
                      "text": "高血壓飲食：飲食多蔬果"
                    },
                    "height": "sm"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": "飲食少加工食品",
                      "text": "高血壓飲食：飲食少加工食品"
                    },
                    "height": "sm"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "text": "高血壓飲食：飲食多高纖食物",
                      "label": "飲食多高纖食物"
                    },
                    "height": "sm"
                  }
                ],
                "alignItems": "center",
                "offsetTop": "none"
              },
              "styles": {
                "footer": {
                  "separator": True
                }
              }
            },
            {
              "type": "bubble",
              "hero": {
                "type": "image",
                "url": "https://i.imgur.com/RhHjUUZ.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://kb.commonhealth.com.tw/library/category/13"
                },
                "backgroundColor": "#FFFFFF"
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "weight": "bold",
                    "size": "xl",
                    "margin": "md",
                    "text": "減重飲食"
                  },
                  {
                    "type": "text",
                    "text": "各種減重相關的飲食方式",
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
                      "label": "低醣飲食（阿金飲食）",
                      "text": "減重飲食：低醣飲食（阿金飲食）"
                    },
                    "height": "sm",
                    "adjustMode": "shrink-to-fit"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": "低卡飲食、低熱量飲食（LCD）",
                      "text": "減重飲食：低卡飲食、低熱量飲食（LCD）"
                    },
                    "height": "sm",
                    "adjustMode": "shrink-to-fit"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "text": "減重飲食：極低卡飲食、極低熱量飲食（VLCD）",
                      "label": "極低卡飲食、極低熱量飲食（VLCD）"
                    },
                    "height": "sm",
                    "adjustMode": "shrink-to-fit"
                  }
                ],
                "alignItems": "center",
                "offsetTop": "none"
              },
              "styles": {
                "footer": {
                  "separator": True
                }
              }
            },
            {
              "type": "bubble",
              "hero": {
                "type": "image",
                "url": "https://i.imgur.com/7EhYH42.png",
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
                    "weight": "bold",
                    "size": "xl",
                    "margin": "md",
                    "text": "其他"
                  },
                  {
                    "type": "text",
                    "text": "其他常見的飲食方式",
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
                      "label": "減重飲食：極低脂飲食",
                      "text": "減重飲食：極低脂飲食"
                    },
                    "height": "sm",
                    "adjustMode": "shrink-to-fit"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": "腎臟病飲食：減磷飲食",
                      "text": "腎臟病飲食：減磷飲食"
                    },
                    "height": "sm",
                    "adjustMode": "shrink-to-fit"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "text": "得舒飲食（DASH飲食計畫）",
                      "label": "得舒飲食（DASH飲食計畫）"
                    },
                    "height": "sm"
                  }
                ],
                "alignItems": "center",
                "offsetTop": "none"
              },
              "styles": {
                "footer": {
                  "separator": True
                }
              }
            }
          ]
        }

def get_sport_button():
  return {
            "type": "carousel",
            "contents": [
              {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://i.imgur.com/vy6sljy.png",
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://kb.commonhealth.com.tw/library/category/16"
                  },
                  "backgroundColor": "#FFFFFF"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "weight": "bold",
                      "size": "xl",
                      "margin": "md",
                      "text": "日常微運動"
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
                        "label": "煮飯",
                        "text": "日常微運動：煮飯"
                      },
                      "height": "sm"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "label": "洗碗",
                        "text": "日常微運動：洗碗"
                      },
                      "height": "sm"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "text": "日常微運動：開車",
                        "label": "開車"
                      },
                      "height": "sm"
                    }
                  ],
                  "alignItems": "center",
                  "offsetTop": "none"
                },
                "styles": {
                  "footer": {
                    "separator": True
                  }
                }
              },
              {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://i.imgur.com/R2MGYqW.png",
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://kb.commonhealth.com.tw/library/category/16"
                  },
                  "backgroundColor": "#FFFFFF"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "weight": "bold",
                      "size": "xl",
                      "margin": "md",
                      "text": "日常微運動"
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
                        "label": "家庭園藝",
                        "text": "日常微運動：家庭園藝"
                      },
                      "height": "sm"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "label": "平常辦公",
                        "text": "日常微運動：平常辦公"
                      },
                      "height": "sm"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "text": "日常微運動：平常辦公",
                        "label": " "
                      },
                      "height": "sm"
                    }
                  ],
                  "alignItems": "center",
                  "offsetTop": "none"
                },
                "styles": {
                  "footer": {
                    "separator": True
                  }
                }
              },
              {
                "type": "bubble",
                "hero": {
                  "type": "image",
                  "url": "https://i.imgur.com/0cgDOHg.png",
                  "size": "full",
                  "aspectRatio": "20:13",
                  "aspectMode": "cover",
                  "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://kb.commonhealth.com.tw/library/category/16"
                  },
                  "backgroundColor": "#FFFFFF"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "weight": "bold",
                      "size": "xl",
                      "margin": "md",
                      "text": "其他"
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
                        "label": "籃球",
                        "text": "籃球"
                      },
                      "height": "sm",
                      "adjustMode": "shrink-to-fit"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "label": "羽毛球",
                        "text": "羽毛球"
                      },
                      "height": "sm",
                      "adjustMode": "shrink-to-fit"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "text": "直排輪",
                        "label": "直排輪"
                      },
                      "height": "sm",
                      "adjustMode": "shrink-to-fit"
                    }
                  ],
                  "alignItems": "center",
                  "offsetTop": "none"
                },
                "styles": {
                  "footer": {
                    "separator": True
                  }
                }
              }
            ]
          }













