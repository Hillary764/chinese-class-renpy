label enterKitchen:
    scene bg kitchen
    show lucy sit at right with dissolve
    if renpy.random.randint(0,10) >= 6:
        #erebus shows up
        L "我很饿。"
        L "我想高猫不在这儿吃饭。"

        show erebus neutral at left with dissolve

        L "哎呀！说曹操，曹操到！"
        jump erebusEating
    else:
        if renpy.random.randint(0,10) >= 2:
            #person shows up
            jump personKitchen
        #if we're here no one showed up
        jump emptyKitchen
    

menu emptyKitchen:
    L "我该怎么办？"

    "唱歌":
        L "我想吃"
        call changgeMenu
        if personAppears:
            jump personKitchen
        jump emptyKitchen
    
    "吃普通的饭":
        L "我很饿。我不想等。"
        $ lastAction = "chifan"
        call incrementTurns
        jump enterKitchen
    
    "去别的地方":
        L "去哪儿？"
        menu:
            "去哪儿？"

            "去我的家":
                L "我一点儿累"
                scene bg bedroom with dissolve
                show lucy sit at right
                jump houseOptions

            "进城":
                L "我想玩"
    


menu erebusEating:
    L "高猫现在吃饭可是我要吃饭。我应该说什么？"

    "滚" if pengyouEnd <= 0:
        $ pengyouEnd -= 1
        show erebus talking
        E "你不客气，小猫。"
        E "我去别的地方。"
        hide erebus
        jump emptyKitchen
    
    "高猫，我很饿！":
        jump erebusFoodQuestion      
    
    "不说。我应该去别的地方。":
        jump kitchenMovePlaces

menu erebusFoodQuestion:
    E "你想吃什么？"

    "吃肉。我是猫。":
        show lucy sit at right
        if shucai:
            show erebus talking
            E "你不想吃蔬菜？"
            E "好。现在我有事，所以我应该出去。"
            hide erebus
            jump emptyKitchen
        else:
            $ shucai = True
            show erebus talking at left
            E "哎呀，小猫！你应该吃很营养的菜。"
            E "蔬菜很营养。"
            E "我们有各种蔬菜。红色的，绿色的，黄色的。。。"
            E "你喜欢吃白菜吗？"
            E "白菜很好吃可是白菜是绿色的，不是白色的。。。"
            E "黄瓜，西红柿，哈密瓜，都很好吃。"
            show erebus neutral at left
            show lucy talking at right
            L "哈密瓜？哈密瓜是蔬菜？"
            show lucy sit at right
            show erebus talking at left
            E "对，对。哈密瓜最好吃的蔬菜。"
            show erebus neutral at left
            show lucy talking at right
            L "好。。。"
            show lucy sit at right
            show erebus talking at left
            E "我有一个主意！"
            E "我们的家人给你做很营养的饭！"
            E "我给他们打电话。"
            play music "audio/nyancat.mp3"
            E "喵喵喵！！！喵喵喵！！！"
            stop music
            E "看！一个家人来这里！"
            E "我正好有事"
            E "不好意思，再见！"
            hide erebus
            jump personKitchen
    "吃蔬菜？" if shucai:
        $ pengyouEnd += 1
        show erebus talking at left
        E "蔬菜很好吃！"
        E "我有一个主意！"
        E "我们的家人给你做很营养的饭！"
        E "我给他们打电话。"
        play music "audio/nyancat.mp3"
        E "喵喵喵！！！喵喵喵！！！"
        stop music
        E "看！一个家人来这里！"
        E "我正好有事"
        E "不好意思，再见！"
        hide erebus
        jump personKitchen



label personKitchen:
    show person neutral at left
    menu:
        L "我该怎么办？"

        "来点什么饮料":
            jump drinkMenu
        
        "来点什么菜":
            jump foodMenu
        
        "去别的地方":
            jump kitchenMovePlaces



menu drinkMenu:
    L "我想喝什么？"

    "奶茶":
        J "好"
        J "别喝很多的牛奶"
        scene black
        pause 0.4
        scene bg kitchen
        show lucy sit at right
        show person neutral at left
        $ lastAction = "chifan"
        call incrementTurns
        jump enterKitchen

    "水":
        J "好"
        scene black
        pause 0.4
        scene bg kitchen
        show lucy sit at right  
        show person neutral at left
        $ lastAction = "chifan"
        call incrementTurns
        jump enterKitchen

    "啤酒":
        J "啤酒？"
        jump alcohol

    "白酒":
        J "白酒！？！？"
        J "小猫，你喝过白酒吗！？"
        jump alcohol

menu foodMenu:
    L "我想吃什么？"

    "宫保鸡丁":
        J "我把鸡肉给你做饭，好吧？"
        hide person
        pause 0.3
        show person talking at left
        J "饭做好了。尝一下这个。"
        show person neutral 
        show lucy talking
        L "味道真好。"
        $ lastAction = "chifan"
        call incrementTurns
        scene black
        pause 0.4
        scene bg kitchen with dissolve
        show lucy sit at right
        jump enterKitchen


    "炒腊肉":
        J "我把几个肉给你做饭，好吧？"
        hide person
        pause 0.3
        show person talking at left
        J "饭做好了。尝一下这个。"
        show person neutral 
        show lucy talking
        L "很香。"
        $ lastAction = "chifan"
        call incrementTurns
        scene black
        pause 0.4
        scene bg kitchen with dissolve
        show lucy sit at right
        jump enterKitchen

    "蔬菜" if shucai:
        $ pengyouEnd += 1
        J "蔬菜？"
        show person neutral at left
        show lucy talking at right
        L "蔬菜是营养的，对？"
        L "我想吃哈密瓜。"
        show lucy sit
        J "。。。"
        show person talking
        J "哈密瓜？"
        J "小猫。。。你不能吃蔬菜。哈密瓜不是蔬菜可是你也不能吃哈密瓜。"
        J "你想吃别的菜？"
        show person neutral
        jump foodMenu

label alcohol:
    menu:
        J "小猫。。。 你多大了？"
        
        "我三岁":
            J "..."
            $ age3 = True

        "我五岁":
            J "..."
            $ age5 = True
    if age3 and age5:
        J "你三岁还是你五岁？"
        L "我不知道。"
        J "我也不知道。"
        J "可是你不可以喝酒，而且猫不能喝酒。"
    J "你不能喝酒。你是一只猫。"
    J "我给你来一杯水，好吗？"
    L "好。。。"
    $ lastAction = "chifan"
    call incrementTurns
    jump enterKitchen

menu kitchenMovePlaces:
    L "去哪儿？"

    "去我的家":
        L "我一点儿累。"
        scene black with dissolve
        pause 0.4
        scene bg bedroom with dissolve
        show lucy sit at right
        jump houseOptions

    "进城":
        L "我想玩儿。"
        jump enterRoom