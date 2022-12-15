menu changgeMenu:
    #called from multiple locations
    "唱歌唱得怎么样？"

    "唱歌唱得很好听":
        show lucy talking
        L "我唱歌唱得最好听！"
        show lucy singing slowly
        L "喵喵！喵喵喵！"
        python:
            personAppears = False
            if renpy.random.randint(0,10) >= 6:
                personAppears = True
                jiarenEnd += 2
        if personAppears:
            show lucy talking at right with dissolve 
            L "我的家人！我爱你！你喜欢我的歌吗？"
            show lucy sit at right
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
        L "喵喵！！ 喵喵喵！！！"
        L "喵喵喵！喵喵喵！！ 喵喵！ 喵喵喵喵！"
        L "喵喵！喵喵喵喵！喵喵喵！！喵喵喵！！！ 喵喵！ 喵喵喵喵！！"
        python:
            personAppears = False
            if renpy.random.randint(0,10) >= 3:
                personAppears = True
                jiarenEnd += 1
        if personAppears:
            show lucy talking at right with dissolve
            L "我的家人！我爱你！"
            show lucy sit at right
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
        L "我应该唱歌唱得越来越漂亮了。。。"
        show lucy singing fast
        L "喵喵。。。 喵喵喵！！"
        L "{size=+10} 喵喵！{/size}"
        L "{size=+15} {b}喵喵喵！！{/b} {/size}"
        $ personAppears = True
        $ jiarenEnd -= 1
        show lucy sit at right with dissolve
        J "好好好。。。 等一下。。。"
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
    if turnCount > numberOfTurns:
        jump ending
    L "for testing... turnCount = [turnCount]"
    return

label ending:
    L "我很能干"
    return