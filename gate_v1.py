from imagesearch import *
import pyautogui as pa

folder = "./image/"
character = "zd"

total_duel = 50

for i in range(1, total_duel + 1):
    # Find gate button
    print("第", i ,"轮开始")
    
    pos = imagesearch_loop(folder+"gate.png", 0.5)
    # Click gate button
    click_image(folder+"gate.png", pos, "left", 0.5)

    # Find duel button #1
    pos = imagesearch_loop(folder+"duel_gate.png", 0.5)

    # Click duel button #1
    click_image(folder+"duel_gate.png", pos, "left", 0.5)

    # Find character (Example : Aster Phoenix)
    pos = imagesearch_loop(folder+"char_"+character+".png", 0.5)
    click_image(folder+"char_"+character+".png", pos, "left", 0.5)

    # Find duel button #2
    pos = imagesearch_loop(folder+"duel_gate.png", 0.5)

    # Click duel button #2
    click_image(folder+"duel_gate.png", pos, "left", 0.1)

    search = True
    while search:
        pos = imagesearch(folder+"menu.png")
        if pos[0] != -1:
            search = False
            break
        for _ in range(5):
            pa.click(x=960, y=832)
            time.sleep(0.2)
        time.sleep(0.5)

    # Summon monster
    monster_count = 0
    round = 0
    card_count = 4

    # Loop starts here
    finished = False

    # Timeout in second
    timeout = 0

    while not finished:
        for _ in range(300):
            pa.click(x=620, y=820)
            pos = imagesearch(folder+"action.png")
            if pos[0] > -1:
                break
            time.sleep(0.2)
        
        if pos[0] == -1:
            break
        
        time.sleep(1)

        if monster_count < 3:
            # Click monster on hand
            pa.click(x=953, y=1035)

            # Find normal summon button
            pos = imagesearch_loop(folder+"normal_summon.png", 0.5)

            # Click normal summon button
            click_image(folder+"normal_summon.png", pos, "left", 0.1)

            # Increment monster count
            monster_count += 1

        # Find action button
        pos = imagesearch_loop(folder+"action.png", 0.5)

        # Click action button
        click_image(folder+"action.png", pos, "left", 0.1)

        # Find battle phase button
        time.sleep(0.5)
        pos = imagesearch(folder+"to_battle_phase.png")
        if pos[0] != -1:
            # Click battle phase button
            click_image(folder+"to_battle_phase.png", pos, "left", 0.1)
        else:
            # You can't attack if you get the first turn
            pos = imagesearch_loop(folder+"to_end_phase.png", 0.1)
            # Click end phase button
            click_image(folder+"to_end_phase.png", pos, "left", 0.1)

            # Skip battle phase
            continue
        
        imagesearch_loop(folder+"action.png", 0.5)

        if monster_count >= 1:
            # Monster #1 attack
            # Find monster #1 location
            time.sleep(0.5)
            pa.click(x=958, y=667)
            # Find attack #1 button
            for _ in range(10):
                pos = imagesearch(folder+"attack.png")
                if pos[0] != -1:
                    break
                time.sleep(0.1)
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            
        # Check if finished
        search = False
        for _ in range(5):
            pos = imagesearch(folder+"action.png")
            if pos[0] != -1:
                search = True
                break
            for _ in range(5):
                pa.click(x=620, y=820)
                time.sleep(0.2)
            
        if not search:
            break

        if monster_count >= 2:
            # Monster #2 attack
            # Find monster #2 location
            time.sleep(0.5)
            pa.click(x=1086, y=667)
            # Find attack #2 button
            for _ in range(10):
                pos = imagesearch(folder+"attack.png")
                if pos[0] != -1:
                    break
                time.sleep(0.1)
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            
        # Check if finished
        search = False
        for _ in range(5):
            pos = imagesearch(folder+"action.png")
            if pos[0] != -1:
                search = True
                break
            for _ in range(5):
                pa.click(x=620, y=820)
                time.sleep(0.2)
            
        if not search:
            break

        if monster_count >= 3:
            # Monster #3 attack
            # Find monster #3 location
            time.sleep(0.5)
            pa.click(x=833, y=671)
            # Find attack #3 button
            for _ in range(10):
                pos = imagesearch(folder+"attack.png")
                if pos[0] != -1:
                    break
                time.sleep(0.1)
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)

        # Check if finished
        search = False
        for _ in range(5):
            pos = imagesearch(folder+"action.png")
            if pos[0] != -1:
                search = True
                break
            for _ in range(5):
                pa.click(x=620, y=820)
                time.sleep(0.2)
            
        if not search:
            break

        if not finished:
            pos = imagesearch_loop(folder+"action.png", 0.5)

            # Click action button
            click_image(folder+"action.png", pos, "left", 0.1)

            # Find end phase button
            pos = imagesearch_loop(folder+"to_end_phase.png", 0.5)

            # Click end phase button
            click_image(folder+"to_end_phase.png", pos, "left", 0.1)
        
    # Wait ok button
    search = True
    while search:
        pos = imagesearch(folder+"ok.png")
        if pos[0] != -1:
            search = False
            break
        for _ in range(3):
            pa.click(x=960, y=832)
            time.sleep(0.2)
        time.sleep(0.5)
    click_image(folder+"ok.png", pos, "left", 0.5)

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
            break
        for _ in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.2)
        time.sleep(0.5)
    click_image(folder+"next.png", pos, "left", 0.5)

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
            break
        for _ in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.2)
        time.sleep(0.5)
    click_image(folder+"next.png", pos, "left", 0.5)
    
    # Wait next round
    search = True
    while search:
        pos = imagesearch(folder+"gate.png")
        if pos[0] != -1:
            search = False
        pa.click(x=600, y=500)
        time.sleep(0.3)
        
    print("第", i ,"轮结束")

