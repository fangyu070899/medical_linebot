from linebot.models import QuickReply,QuickReplyButton,MessageAction

def get_heart_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="心悸", text="心悸")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="心肌梗塞", text="心肌梗塞")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="低血壓", text="低血壓")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="白血病", text="白血病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="淋巴結腫大", text="淋巴結腫大")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="蠶豆症", text="蠶豆症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="貧血", text="貧血")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="血友病", text="血友病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="伊波拉病毒", text="伊波拉病毒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="心碎症候群", text="心碎症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="敗血症", text="敗血症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="手足發紺症", text="手足發紺症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="靜脈曲張性潰瘍", text="靜脈曲張性潰瘍")
                   )
               ]
           )

def get_bone_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="骨刺", text="骨刺")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="骨折", text="骨折")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腰痛", text="腰痛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="手麻或腳麻", text="手麻或腳麻")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="落枕", text="落枕")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="足底筋膜炎", text="足底筋膜炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="僵直性脊椎炎", text="僵直性脊椎炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="椎間盤突出", text="椎間盤突出")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="痛風", text="痛風")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="創傷性關節炎", text="創傷性關節炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="類風濕性關節炎", text="類風濕性關節炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肩頸痠痛", text="肩頸痠痛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="運動傷害", text="運動傷害")
                   )
               ]
           )

def get_brain_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="暈眩", text="暈眩")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="出血性腦中風", text="出血性腦中風")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="阿茲海默症", text="阿茲海默症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="譫妄", text="譫妄")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="日本腦炎", text="日本腦炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腦震盪", text="腦震盪")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="偏頭痛", text="偏頭痛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="記憶力變差", text="記憶力變差")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="漸凍人症", text="漸凍人症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="癲癇", text="癲癇")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="自律神經失調", text="自律神經失調")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="巴金森氏症", text="巴金森氏症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="良性運動後頭痛", text="良性運動後頭痛")
                   )
               ]
           )

def get_ear_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="一般感冒", text="一般感冒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="中耳炎", text="中耳炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="過敏性鼻炎", text="過敏性鼻炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="耳鳴", text="耳鳴")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="鼻塞", text="鼻塞")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="老年性重聽", text="老年性重聽")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="耳中風", text="耳中風")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="聲音沙啞", text="聲音沙啞")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="異物卡進喉嚨", text="異物卡進喉嚨")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="甲狀腺腫大", text="甲狀腺腫大")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="流鼻血", text="流鼻血")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="耳垢堵塞", text="耳垢堵塞")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="猩紅熱", text="猩紅熱")
                   )
               ]
           )

def get_eye_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="近視", text="近視")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="遠視", text="遠視")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="飛蚊症", text="飛蚊症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="散光", text="散光")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="角膜炎", text="角膜炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="青光眼", text="青光眼")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="黃斑部病變", text="黃斑部病變")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="乾眼症", text="乾眼症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="老花眼", text="老花眼")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="眼中風", text="眼中風")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="視網膜剝離", text="視網膜剝離")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="假性近視", text="假性近視")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="夜盲症", text="夜盲症")
                   )
               ]
           )

def get_gynecology_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="乳癌", text="乳癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="子宮頸癌", text="子宮頸癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="經痛", text="經痛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="月經不規則", text="月經不規則")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="女性更年期", text="女性更年期")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="非經期出血", text="非經期出血")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="頻尿", text="頻尿")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="愛滋病", text="愛滋病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="子宮外孕", text="子宮外孕")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="淋病", text="淋病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="月經不規則", text="月經不規則")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="骨盆腔炎", text="骨盆腔炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="小便疼痛", text="小便疼痛")
                   )
               ]
           )

def get_kidney_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="血尿", text="血尿")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="急性腎損傷", text="急性腎損傷")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="尿毒症", text="尿毒症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="泌尿道感染", text="泌尿道感染")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="高血壓腎病變", text="高血壓腎病變")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="慢性腎臟病", text="慢性腎臟病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="心腎症候群", text="心腎症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="代謝性酸中毒", text="代謝性酸中毒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="代謝性鹼中毒", text="代謝性鹼中毒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="漢他病毒", text="漢他病毒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腎盂腎炎", text="腎盂腎炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="黃熱病", text="黃熱病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="多囊性腎病", text="多囊性腎病")
                   )
               ]
           )

def get_liver_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="B型肝炎", text="B型肝炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="C型肝炎", text="C型肝炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肝囊腫", text="肝囊腫")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肝癌", text="肝癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肝硬化", text="肝硬化")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肝血管瘤", text="肝血管瘤")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="脂肪肝", text="脂肪肝")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="黃疸", text="黃疸")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="高三酸甘油酯", text="高三酸甘油酯")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肝衰竭", text="肝衰竭")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肝膿瘍", text="肝膿瘍")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="高胰島素血症", text="高胰島素血症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="病毒性肝炎", text="病毒性肝炎")
                   )
               ]
           )

def get_lung_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="氣喘", text="氣喘")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肺炎", text="肺炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肺癌", text="肺癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="咳嗽：急性咳嗽", text="咳嗽：急性咳嗽")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="流行性感冒", text="流行性感冒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肺結核", text="肺結核")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肺纖維化", text="肺纖維化")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="慢性咳嗽", text="慢性咳嗽")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="類流感", text="類流感")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="睡眠呼吸中止症", text="睡眠呼吸中止症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="新冠肺炎", text="新冠肺炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="高山症", text="高山症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="退伍軍人症", text="退伍軍人症")
                   )
               ]
           )

def get_mind_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="自閉症", text="自閉症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="強迫症", text="強迫症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="厭食症", text="厭食症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="創傷後壓力症候群", text="創傷後壓力症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="注意力不足過動症", text="注意力不足過動症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="妥瑞氏症", text="妥瑞氏症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="焦慮症", text="焦慮症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="產後憂鬱症", text="產後憂鬱症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="嗜睡症", text="嗜睡症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="睡眠不足", text="睡眠不足")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="憂鬱症", text="憂鬱症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="幽閉恐懼症", text="幽閉恐懼症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="社交焦慮症", text="社交焦慮症")
                   )
               ]
           )

def get_mouth_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="口腔癌", text="口腔癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="嘴破", text="嘴破")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="蛀牙", text="蛀牙")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="牙周病", text="牙周病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="牙齦紅腫", text="牙齦紅腫")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="牙痛", text="牙痛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="敏感性牙齒", text="敏感性牙齒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="睡眠磨牙症", text="睡眠磨牙症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="口角炎", text="口角炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="口腔潰爛", text="口腔潰爛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="牙齦增生", text="牙齦增生")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="外傷性牙齒傷害", text="外傷性牙齒傷害")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="乾性齒槽炎", text="乾性齒槽炎")
                   )
               ]
           )

def get_nutrition_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="β-胡蘿蔔素", text="β-胡蘿蔔素")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="維生素A", text="維生素A")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="反式脂肪", text="反式脂肪")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="維生素C", text="維生素C")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="木糖醇", text="木糖醇")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="水", text="水")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="益生菌", text="益生菌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="Omega-3 脂肪酸", text="Omega-3 脂肪酸")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="鎂", text="鎂")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="葉酸", text="葉酸")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="鐵", text="鐵")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="膳食纖維", text="膳食纖維")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="維生素B12", text="維生素B12")
                   )
               ]
           )

def get_skin_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="帶狀疱疹", text="帶狀疱疹")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="脂漏性皮膚炎", text="脂漏性皮膚炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="曬傷", text="曬傷")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="異位性皮膚炎", text="異位性皮膚炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="灰指甲", text="灰指甲")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="皮膚癌", text="皮膚癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="蜂窩組織炎", text="蜂窩組織炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="皮膚搔癢", text="皮膚搔癢")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="青春痘", text="青春痘")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="白化症", text="白化症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="凍瘡", text="凍瘡")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="毛孔角化症", text="毛孔角化症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="塵蟎", text="塵蟎")
                   )
               ]
           )

def get_stomach_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="十二指腸潰瘍", text="十二指腸潰瘍")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="大腸癌", text="大腸癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="胃食道逆流", text="胃食道逆流")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="膽結石", text="膽結石")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="肚子痛", text="肚子痛")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="便秘", text="便秘")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="幼童誤食異物", text="幼童誤食異物")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="食物中毒", text="食物中毒")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="蛔蟲", text="蛔蟲")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="直腸炎", text="直腸炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="諾羅病毒感染", text="諾羅病毒感染")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="痔瘡", text="痔瘡")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="盲腸炎", text="盲腸炎")
                   )
               ]
           )

def get_urinaty_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="攝護腺癌", text="攝護腺癌")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="尿道炎", text="尿道炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="膀胱炎", text="膀胱炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="頻尿", text="頻尿")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="泌尿道感染", text="泌尿道感染")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="尿路結石", text="尿路結石")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="攝護腺肥大", text="攝護腺肥大")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="膀胱過動症", text="膀胱過動症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="夜間多尿", text="夜間多尿")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="男性不孕症", text="男性不孕症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="睪固酮低下症候群", text="睪固酮低下症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="亞伯氏症候群", text="亞伯氏症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="軟性下疳", text="軟性下疳")
                   )
               ]
           )

def get_elder_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="失溫", text="失溫")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="體質性水腫", text="體質性水腫")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="阿米巴原蟲感染／阿米巴性痢疾", text="阿米巴原蟲感染／阿米巴性痢疾")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="假性痛風（焦磷酸鈣沉積症）", text="假性痛風（焦磷酸鈣沉積症）")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="非乳糜瀉麩質敏感症", text="非乳糜瀉麩質敏感症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="髕骨股骨疼痛症候群", text="髕骨股骨疼痛症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="良性原發性顫抖症", text="良性原發性顫抖症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="屈公病", text="屈公病")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="黃斑瘤", text="黃斑瘤")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="糖尿病關節病變", text="糖尿病關節病變")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腹水", text="腹水")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腎性貧血", text="腎性貧血")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="暫時性黑矇", text="暫時性黑矇")
                   )
               ]
           )

def get_minor_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="失溫", text="失溫")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腸繫膜淋巴結炎", text="腸繫膜淋巴結炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="胡蘿蔔素血症", text="胡蘿蔔素血症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="中毒性休克症候群", text="中毒性休克症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="非乳糜瀉麩質敏感症", text="非乳糜瀉麩質敏感症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="多發性肌炎", text="多發性肌炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="中毒性休克症候群", text="中毒性休克症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="梨形鞭毛蟲症", text="梨形鞭毛蟲症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="眼瞼炎", text="眼瞼炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="鞏膜炎", text="鞏膜炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="感染性單核球增多症", text="感染性單核球增多症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="腸繫膜淋巴結炎", text="腸繫膜淋巴結炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="幽門狹窄", text="幽門狹窄")
                   )
               ]
           )

def get_male_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="原發性肥胖", text="原發性肥胖")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="巨細胞動脈炎（顳動脈炎）", text="巨細胞動脈炎（顳動脈炎）")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="蹠底靜脈曲張", text="蹠底靜脈曲張")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="電解質失衡", text="電解質失衡")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="梨狀肌症候群", text="梨狀肌症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="多發性肌炎", text="多發性肌炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="急性下背痙攣（閃到腰）", text="急性下背痙攣（閃到腰）")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="默克森－羅森泰症候群", text="默克森－羅森泰症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="低血鈉", text="低血鈉")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="解離性骨軟骨炎", text="解離性骨軟骨炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="血小板低下症", text="血小板低下症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="酒精性肝炎", text="酒精性肝炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="咖啡因戒斷症狀", text="咖啡因戒斷症狀")
                   )
               ]
           )

def get_female_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(
                       action=MessageAction(label="白喉", text="白喉")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="巨細胞動脈炎（顳動脈炎）", text="巨細胞動脈炎（顳動脈炎）")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="急性呼吸窘迫症候群", text="急性呼吸窘迫症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="電解質失衡", text="電解質失衡")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="薦髂關節功能障礙", text="薦髂關節功能障礙")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="多發性肌炎", text="多發性肌炎")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="急性下背痙攣（閃到腰）", text="急性下背痙攣（閃到腰）")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="默克森－羅森泰症候群", text="默克森－羅森泰症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="低血鈉", text="低血鈉")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="馬尾症候群", text="馬尾症候群")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="血小板低下症", text="血小板低下症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="舞蹈症", text="舞蹈症")
                   ),
                   QuickReplyButton(
                       action=MessageAction(label="咖啡因戒斷症狀", text="咖啡因戒斷症狀")
                   )
               ]
           )

def get_quick_reply(item):
    return QuickReply(items=item)














