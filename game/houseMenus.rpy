
menu houseOptions:
    L "我应该做什么？"

    "唱歌":
        L "我喜欢我的家人。。。我给他们唱歌"
        call changgeMenu
        if personAppears:
            jump personInHouse
        else:
            jump houseOptions


    "睡觉":
        L "我很累。。。"
        if lastAction == "shuijiao":
            "。。。可是我睡觉睡得很多。。。"
            menu:
                L "睡觉？"

                "睡觉":
                    L "我太累了！"
                    $ leiEnd += 1
                    jump lucySleeps


                "不睡觉":
                    L "因为我很忙，所以我不想睡觉。"
                    jump houseOptions
        jump sleepOptions

    "去别的地方":
        L "去哪儿？"
        menu:
            "去哪儿？"

            "去饭馆":
                L "我一点儿饿。"
                jump enterKitchen

            "进城":
                L "我想玩儿。"
                jump enterRoom


menu sleepOptions:
    L "我想睡觉可是我不看我的家人。。。"

    "唱歌":
        call changgeMenu
        if personAppears:
            jump personInHouse
        else:
            L "我必须睡觉。"
            jump lucySleeps
    
    "自己一只猫睡觉":
        #meant to be like “自己一个人” lol
        L "我太累了。"
        L "我不必须跟我的家人聊天。"
        L "我现在睡觉"
        jump lucySleeps

label personInHouse:
    show person neutral at left with dissolve
    menu:
        J "你唱歌。为什么？"
        
        "我想睡觉":
            J "好。。。"
            show person neutral
            show lucy talking
            L "随便坐。"
            show person talking
            show lucy sit
            J "好。。。？"
            hide person
            hide lucy
            show person sit at center
            J "。。。"
            scene black with dissolve
            pause 0.5
            scene bg bedroom
            show lucy sit at right
            $ lastAction = "aijiaren"
            call incrementTurns
            jump houseOptions
        
        "我想你摸摸我":
            J "你太可爱！ 我很喜欢摸摸猫！"
            $ lastAction = "aijiaren"
            call incrementTurns
            hide person
            jump houseOptions

label lucySleeps:
    show lucy sleep at right
    L "。。。"
    scene black with dissolve
    pause 0.5
    scene bg bedroom with dissolve
    show lucy sit at right
    $ lastAction = "shuijiao"
    call incrementTurns
    jump houseOptions