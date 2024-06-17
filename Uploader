def run(title,describe,content,bgm,path_cover):
    
    windows = driver.window_handles   # 获取所有窗口句柄
    for i in windows:
        driver.switch_to.window(i)
        if(driver.title == "抖音创作者中心"):
            publish_douyin_tuwen()
            continue
        elif(driver.title == "快手创作者服务平台"):
            publish_kuaishou_tuwen()
            continue
        elif(driver.title == "视频号助手"):
            #publish_shipinhao_tuwen()
            continue
        elif(driver.title == "小红书创作服务平台"):
            #publish_xiaohongshu()
            continue
        elif(driver.title == "@【用户名】的个人主页 - 微博"): #【用户名】对应为微博用户名
            publish_weibo()
            continue
        elif(driver.title == "豆瓣"):
            publish_douban()
            continue
        else:
            publish_zhihu()
            continue
    driver.quit()
title,describe,content,bgm,path_cover=situation(1)
run(title,describe,content,bgm,path_cover)
