menu changgeMenu:
    #called from multiple locations
    "唱歌唱得怎么样？"

    "唱歌唱得很好听":
        show lucy talking
        L "我唱歌唱得最好听！"
        show lucy singing slowly
        play music "audio/nyancat.mp3"
        L "喵喵！喵喵喵！"
        stop music
        python:
            personAppears = False
            if renpy.random.randint(0,10) >= 6:
                personAppears = True
                jiarenEnd += 2
        if personAppears:
            show lucy talking at right 
            show person neutral at left with dissolve
            L "我的家人！我爱你！你喜欢我的歌吗？"
            show lucy sit at right
            show person talking
            J "小猫！你唱歌唱得太好听！"
            J "你吃了吗？"
            return
        show lucy sit
        L "我的家人不在这儿。。。"
        call changAgain
        return

    "唱歌唱得很多":
        show lucy talking
        L "我要跟我的家人聊天！！！"
        show lucy singing mid
        play music "audio/nyancat.mp3"
        L "喵喵！！ 喵喵喵！！！"
        L "喵喵喵！喵喵喵！！ 喵喵！ 喵喵喵喵！"
        L "喵喵！喵喵喵喵！喵喵喵！！喵喵喵！！！ 喵喵！ 喵喵喵喵！！"
        stop music
        python:
            personAppears = False
            if renpy.random.randint(0,10) >= 3:
                personAppears = True
                jiarenEnd += 1
        if personAppears:
            show lucy talking at right with dissolve
            show person neutral at left with dissolve
            L "我的家人！我爱你！"
            show lucy sit at right
            show person talking
            J "小猫。。。 你唱歌唱得太多了。。。"
            J "你有什么事？"
            return
        show lucy sit
        L "我的家人不在这儿。。。"
        call changAgain
        return

menu changAgain:
    L "再唱歌？"

    "唱歌":
        show lucy talking
        L "我应该唱歌唱得越来越好听了。。。"
        show lucy singing fast
        play music "audio/nyancat.mp3"
        L "喵喵。。。 喵喵喵！！"
        L "{size=+10} 喵喵！{/size}"
        L "{size=+15} {b}喵喵喵！！{/b} {/size}"
        stop music
        $ personAppears = True
        $ jiarenEnd -= 1
        show lucy sit at right with dissolve
        J "好好好。。。 等一下。。。"
        show person talking at left
        J "小猫，你唱歌唱得太多了。。。"
        J "你有什么事？"
        return
    
    "不唱歌":
        L "我的家人恨我！我不要给他们唱歌"
        $ personAppears = False
        return


label incrementTurns:
    python:
        turnCount += 1
        if lastAction == "chifan" or lastAction == "shuijiao":
            leiEnd += 1
        elif lastAction == "aijiaren":
            jiarenEnd += 1
        elif lastAction == "wan":
            haowanEnd += 1
    if turnCount > numberOfTurns:
        jump ending
    # L "for testing... turnCount = [turnCount]"
    return

label ending:
    scene black
    L "我很忙。"
    if jiarenEnd + pengyouEnd < 0:
        "BAD END: 你打搅大家。"
    elif pengyouEnd >= leiEnd and pengyouEnd >= jiarenEnd and pengyouEnd >= haowanEnd:
        "GOOD END: 你和高猫是很好的朋友！"
    elif leiEnd >= jiarenEnd and leiEnd >= haowanEnd:
        "NEUTRAL END: 你太累了！"
    elif jiarenEnd >= haowanEnd:
        "GOOD END: 你的家人爱你！"
    else:
        "GOOD END: 你喜欢好玩儿的事！"
    $ MainMenu(confirm=False)()

