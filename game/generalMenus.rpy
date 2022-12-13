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
            J "你有什么事？"
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