
menu houseOptions:
    L "我应该做什么？"

    "唱歌":
        L "我喜欢我的家人。。。我给他们唱歌"
        call changgeMenu
        if personAppears:
            "我想睡觉"
        else:
            "我不看我的家人。。。"

    "睡觉":
        L "我很累。。。"
        jump sleepOptions

    "去别的地方":
        L "去哪儿？"
        menu:
            "去哪儿？"

            "去饭馆":
                L "我一点儿饿"

            "进城":
                L "我想玩"


menu sleepOptions:
    L "我想睡觉可是我不看我的家人。。。"

    "唱歌":
        call changgeMenu
        if personAppears:
            L "我想睡觉"
        else:
            L "我的家人不在这儿。。。"
            jump sleepOptions
    
    "自己一个猫睡觉":
        L "我太累了。"
        L "我不必须跟我的家人聊天。"


