label enterRoom:
    scene bg town
    show lucy sit at right
    menu:
        L "我有空。我该怎么办？"

        "学习功夫":
            jump gongfu

        "打牌":
            jump dapai
 
        "去别的地方":
            menu:
                L "去哪儿？"

                "去我的家":
                    L "我一点儿累"
                    scene black with dissolve
                    pause 0.4
                    scene bg bedroom with dissolve
                    show lucy sit at right
                    jump houseOptions  

                "去饭馆":
                    L "我一点儿饿"
                    scene black with dissolve
                    pause 0.4
                    jump enterKitchen 

label gongfu:
    L "我很有天分。我应该学习功夫。"
    L "我的家人在哪儿？"
    call changgeMenu
    if personAppears:
        show person neutral
        show lucy talking
        L "我想学习功夫。"
        show person talking
        show lucy sit
        J "很好！"
        show person toy
        show lucy sit at right
        show lucy gongfu at center with move
        "..."
        hide person
        $ lastAction = "wan"
        call incrementTurns
        jump enterRoom
    else:
        show lucy talking
        L "我的家人太忙了。。。"
        jump enterRoom
        

label dapai:
    L "高猫在哪儿?"
    show erebus neutral at left with dissolve
    show lucy talking
    L "他在这儿！高猫！我请你跟我打牌。"
    if dapai:
        show erebus talking
        show lucy sit
        E "我很喜欢打牌！"
        L "打牌很好玩儿！"
        show lucy dapai fast
        show erebus dapai
        "。。。"
        scene black with dissolve
        $ lastAction = "wan"
        call incrementTurns
        jump enterRoom

    else:
        $ dapai = True
        show erebus talking
        show lucy sit
        E "“打牌”是什么？"
        show lucy talking
        show erebus neutral
        L "我知道。“打牌”很容易。"
        L "“打牌”的“打”是“打球”的“打”。你“打球”的时候，你打一个球。"
        L "所以，你“打牌”的时候，你打几个纸牌。"
        L "看一看。"
        show lucy sit
        menu:
            "打牌打得怎么样？"

            "快地打牌":
                show lucy dapai fast
                L "。。。"
                L "现在我打牌了。"
                show lucy talking
                L "你看得懂吗？"
                show lucy sit
                show erebus talking
                E "。。。我看不懂。"
                show erebus neutral
                "。。。"
                show lucy dapai slowly
                L "你还看不懂吗？"
                show erebus talking
                E "谢谢。我看得懂。"
                show erebus neutral
                show lucy sit
            
            "慢地打牌":
                show lucy dapai slowly
                L "。。。"
                L "现在我打牌了。"
                show lucy talking
                L "你看得懂吗？"
                show lucy sit
                show erebus talking
                E "谢谢。我看得懂。"
        show erebus neutral
        show lucy talking
        L "你试一试。"
        L "再看。"
        show lucy dapai slowly
        show erebus dapai
        "。。。"
        L "很好！"
        scene black with dissolve
        $ lastAction = "wan"
        call incrementTurns
        jump enterRoom