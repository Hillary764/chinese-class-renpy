menu changgeMenu:
    #called from multiple locations
    "唱歌唱得怎么样？"

    "唱歌唱得很好听":
        L "我唱歌唱得最好听！"
        L "喵喵！喵喵喵！"
        python:
            personAppears = False
            if renpy.random.randint(0,10) >= 6:
                personAppears = True
                jiarenEnd += 2
        if personAppears:
            L "我的家人！我爱你！你喜欢我的歌吗？"
            J "小猫！你唱歌唱得太好听！"
            J "你吃了吗？"
            return
        return

    "唱歌唱得很多":
        L "我要跟我的家人聊天！！！"
        L "喵喵！！ 喵喵喵！！！"
        L "喵喵喵！喵喵喵！！ 喵喵！ 喵喵喵喵！"
        L "喵喵！喵喵喵喵！喵喵喵！！喵喵喵！！！ 喵喵！ 喵喵喵喵！！"
        python:
            personAppears = False
            if renpy.random.randint(0,10) >= 3:
                personAppears = True
                jiarenEnd += 1
        if personAppears:
            L "我的家人！我爱你！"
            J "小猫。。。 你唱歌唱得太多了。。。"
            J "你有什么事？"
            return
        return

menu changAgain:
    L "再唱歌？"

    "唱歌":
        L "我应该唱歌唱得越来越漂亮了。。。"
        L "喵喵。。。 喵喵喵！！"
        L "{size=+10} 喵喵！{/size}"
        L "{size=+15} {b}喵喵喵！！{/b} {/size}"
        $ personAppears = True
        J "好好好。。。 等一下。。。"
        J "小猫，你唱歌唱得太多了。。。"
        J "你有什么事？"
        return
    
    "不唱歌":
        L "我的家人恨我！我不要给他们唱歌"
        $ personAppears = False
        return
