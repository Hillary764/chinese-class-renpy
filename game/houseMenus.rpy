
menu houseOptions:
    L "我应该做什么？"

    "唱歌":
        L "我喜欢我的家人。。。我给他们唱歌"
        call changgeMenu
        if personAppears:
            jump personInHouse
        else:
            "我不看我的家人。。。"
            call changAgain


    "睡觉":
        L "我很累。。。"
        if lastAction = "shuijiao":
            "。。。可是我睡觉睡得很多。。。"
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
            jump personInHouse
        else:
            L "我的家人不在这儿。。。"
            call changAgain
            if personAppears:
                jump personInHouse
            L "我必须睡觉。"
            $ leiEnd += 1
            $ turnCount += 1
            $ lastAction = "shuijiao"
            jump houseOptions
    
    "自己一个猫睡觉":
        L "我太累了。"
        L "我不必须跟我的家人聊天。"
        L "我现在睡觉"
        $ leiEnd += 1
        $ turnCount += 1
        $ lastAction = "shuijiao"
        jump houseOptions

menu personInHouse:
    J "你唱歌。为什么？"
    
    "我想睡觉":
        J "好。。。"
        L "随便坐"
        J "好。。。？"
        $ leiEnd += 1
        $ turnCount += 1
        $ lastAction = "shuijiao"
        jump houseOptions
    
    "我想你摸摸我":
        J "你太可爱！ 我很喜欢摸摸猫！"
        $ jiarenEnd += 1
        $ turnCount += 1
        jump houseOptions

