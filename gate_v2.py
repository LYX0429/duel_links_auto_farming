from imagesearch import *
import pyautogui as pa
import sys
        
class autoDuel():
    def __init__(self):
        self.round = 0
        self.card_count = 4
        self.monster = [0, 0, 0]
        self.magic = [0, 0, 0]
        self.monster_pos = [(958, 565), (1086, 565), (833, 565)]
        self.magic_pos = [(958, 750), (1086, 750), (833, 750)]
        self.opp_field = False
        self.character = ""
        
    def getinmenu(self):
        while True:
            pos = imagesearch(folder+"start_menu.png")
            if pos[0] != -1:
                click_image(folder+"start_menu.png",pos,"left",0.5)
                continue
            pos = imagesearch(folder+"start_menu_2.png")
            if pos[0] != -1:
                click_image(folder+"start_menu_2.png",pos,"left",0.5)
                continue
            time.sleep(1)

    def reset(self):
        self.round = 0
        self.card_count = 4
        self.monster = [0, 0, 0]
        self.magic = [0, 0, 0]
        self.opp_field = False
        
    def beforeDuel(self):
        pos = imagesearch(folder+"gate.png")
        if pos[0] == -1:
            self.getinmenu()
        pos = imagesearch_loop(folder+"gate.png", 0.3)
        click_image(folder+"gate.png", pos, "left", 0.3)
        pos = imagesearch_loop(folder+"duel_gate.png", 0.5)
        click_image(folder+"duel_gate.png", pos, "left", 0.5)
        pos = imagesearch_loop(folder+"char_"+self.character+".png", 0.5)
        click_image(folder+"char_"+self.character+".png", pos, "left", 0.5)
        pos = imagesearch_loop(folder+"duel_gate.png", 0.5)
        click_image(folder+"duel_gate.png", pos, "left", 0.1)

        self.searchAndSkip(folder+"menu.png")
            
    def afterDuel(self):
        search = True
        while search:
            pos = imagesearch(folder+"ok.png")
            if pos[0] != -1:
                break
            pos = imagesearch(folder+"start_menu.png")
            if pos[0] != -1:
                return
            for _ in range(3):
                pa.click(x=960, y=832)
                time.sleep(0.2)
            time.sleep(0.5)
        click_image(folder+"ok.png", pos, "left", 0.3)

        # Wait next button
        search = True
        while search:
            pos = imagesearch(folder+"next.png")
            if pos[0] != -1:
                break
            pos = imagesearch(folder+"start_menu.png")
            if pos[0] != -1:
                return
            for _ in range(3):
                pa.click(x=960, y=119)
                time.sleep(0.2)
            time.sleep(0.5)
        click_image(folder+"next.png", pos, "left", 0.3)

        # Wait next button
        search = True
        while search:
            pos = imagesearch(folder+"next.png")
            if pos[0] != -1:
                break
            pos = imagesearch(folder+"start_menu.png")
            if pos[0] != -1:
                return
            for _ in range(3):
                pa.click(x=960, y=119)
                time.sleep(0.2)
            time.sleep(0.5)
        click_image(folder+"next.png", pos, "left", 0.3)
        
        # Wait next round
        search = True
        while search:
            pos = imagesearch(folder+"gate.png")
            if pos[0] != -1:
                search = False
            pa.click(x=600, y=400)
            time.sleep(0.3)
    
    def inDuel(self):
        while True:
            pos = self.searchAndSkip(folder+"action.png")
            if pos == None:
                return
            
            self.summon = -1
            
            # ????????????
            self.checkField()
            
            pos = self.searchAndSkip(folder+"action.png")
            if pos == None:
                return
            
            if sum(self.magic) < 2 and sum(self.monster) < 2:
                if 0 in self.monster:
                    if not self.summon_monster():
                        return
                
                pos = self.searchAndSkip(folder+"action.png")
                if pos == None:
                    return
                    
                while True:
                    result = self.use_magic()
                    if result == 0:
                        break
                    elif result == 2:
                        return
                    continue
            
            # ?????????????????????
            pos = self.searchAndSkip(folder+"action.png")
            if pos == None:
                return
                
            click_image(folder+"action.png", pos, "left", 0.1)
            time.sleep(0.5)
            pos = imagesearch(folder+"to_battle_phase.png")
            if pos[0] != -1 and not self.opp_field:
                click_image(folder+"to_battle_phase.png", pos, "left", 0.1)
            else:
                pos = imagesearch(folder+"to_end_phase.png")
                if pos == None:
                    return
                click_image(folder+"to_end_phase.png", pos, "left", 0.1)
                continue
            
            while True:
                pa.click(x=620, y=820)
                pos = imagesearch(folder+"action.png")
                if pos[0] > -1:
                    self.phase = 'battle'
                    break
                if self.checkEnd():
                    return
                time.sleep(0.2)
            
            # ????????????
            if self.monster[0] == 1:
                if not self.monster_attack(0): return

            if self.monster[1] == 1:
                if not self.monster_attack(1): return

            if self.monster[2] == 1:
                if not self.monster_attack(2): return

            pos = self.searchAndSkip(folder+"action.png")
            if pos == None:
                return
            click_image(folder+"action.png", pos, "left", 0.3)
            time.sleep(0.5)
            pos = imagesearch(folder+"to_end_phase.png")
            click_image(folder+"to_end_phase.png", pos, "left", 0.1)
    
    def searchAndSkip(self, image):
        while True:
            pa.click(x=565, y=400)
            pos = imagesearch(image)
            if pos[0] > -1:
                return pos
                
            if self.checkEnd():
                return None
                
            pos = imagesearch(folder+"confirm.png")
            if pos[0] > -1:
                click_image(folder+"confirm.png", pos, "left", 0.3)
                time.sleep(1)
                
            pos = imagesearch(folder+"decide_no.png")
            if pos[0] > -1:
                pa.click(x=670, y=750)
                time.sleep(0.5)
                pa.click(x=960, y=915)
                time.sleep(0.5)
                
            pos = imagesearch(folder+"restart.png")
            if pos[0] > -1:
                click_image(folder+"restart.png", pos, "left", 0.5)
                time.sleep(1)
                return None
                
            pos = imagesearch(folder+"start_menu.png")
            if pos[0] > -1:
                return None
                
            time.sleep(0.3)
            
    def checkEnd(self):
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            return True
        pos = imagesearch(folder+"duel_pvp.png")
        if pos[0] > -1:
            return True
        return False
        
    def summon_monster(self):
        X = 700
        while X <= 1100:
            pa.click(x=X, y=1050)
            time.sleep(0.05)
            pa.click(x=X, y=1050)
            pos = imagesearch(folder+"monster.png")
            if pos[0] == -1:
                X += 75
                time.sleep(0.05)
                continue
                
            time.sleep(0.05)
            pos = imagesearch(folder+"normal_summon.png")
            if pos[0] == -1:
                pa.click(x=X, y=1050)
                pos = imagesearch(folder+"normal_summon.png")
                if pos[0] == -1:
                    X += 75
                    time.sleep(0.05)
                    continue
                
            click_image(folder+"normal_summon.png", pos, "left", 0.3)
            self.card_count -= 1
            for i in range(3):
                if self.monster[i] == 0:
                    self.monster[i] = 1
                    self.summon = i
                    return True
            
        return True
        
    def use_magic(self):
        X = 700
        while X <= 1100:
            pa.click(x=X, y=1050)
            time.sleep(0.05)
            pa.click(x=X, y=1050)
            if 0 in self.magic:
                pos = imagesearch(folder+"magic_equip.png")
                if pos[0] != -1:
                    return self.use_magic_equip(0)
            pos = imagesearch(folder+"magic_field.png")
            if pos[0] != -1:
                return self.use_magic_field()
            X += 75
            time.sleep(0.05)
            
        return 0
    
    def use_magic_equip(self, index):
        time.sleep(0.5)
        pos = imagesearch(folder+"trigger_effect.png")
        if pos[0] == -1:
            return 0
                
        click_image(folder+"trigger_effect.png", pos, "left", 0.3)
        pos = self.searchAndSkip(folder+"action.png")
        if not pos:
            return 2
            
        self.card_count -= 1
        for i in range(3):
            if self.magic[i] == 0:
                self.magic[i] = 1
                break
            
        return 1
        
    def use_magic_field(self):
        time.sleep(0.5)
        pos = imagesearch(folder+"trigger_effect.png")
        if pos[0] == -1:
            return 0
            
        click_image(folder+"trigger_effect.png", pos, "left", 0.3)
        pos = self.searchAndSkip(folder+"action.png")
        if not pos:
            return 2
            
        self.card_count -= 1
        return 1
        
    def monster_attack(self, index):
        time.sleep(0.5)
        pa.click(x=self.monster_pos[index][0], y=self.monster_pos[index][1])
        time.sleep(0.5)
        pos = imagesearch(folder+"attack.png")
        if pos[0] != -1:
            click_image(folder+"attack.png", pos, "left", 0.3)
        pos = self.searchAndSkip(folder+"action.png")
        if not pos:
            return False
        return True
    
    def checkField(self):
        for i in range(3):
            if self.monster[i] == 1:
                pa.click(x=565, y=820)
                time.sleep(0.3)
                if i == self.summon:
                    continue
                pa.click(x=self.monster_pos[i][0], y=self.monster_pos[i][1])
                time.sleep(0.5)
                pos = imagesearch(folder+"action.png")
                if pos[0] != -1:
                    self.monster[i] = 0
                    continue
                    
                pos = imagesearch(folder+"defend_mode.png")
                if pos[0] == -1:
                    self.monster[i] = 2
                    
            if self.monster[i] == 2:
                pa.click(x=565, y=820)
                time.sleep(0.3)
                if i == self.summon:
                    continue
                pa.click(x=self.monster_pos[i][0], y=self.monster_pos[i][1])
                time.sleep(0.5)
                pos = imagesearch(folder+"action.png")
                if pos[0] != -1:
                    self.monster[i] = 0
                    continue
                    
                pos = imagesearch(folder+"reverse_summon.png")
                if pos[0] != -1:
                    click_image(folder+"reverse_summon.png", pos, "left", 0.5)
                    click_image(folder+"reverse_summon.png", pos, "left", 0.5)
                    self.monster[i] = 1
                    continue
                
                pos = imagesearch(folder+"attack_mode.png")
                if pos[0] != -1:
                    click_image(folder+"attack_mode.png", pos, "left", 0.5)
                    click_image(folder+"attack_mode.png", pos, "left", 0.5)
                    self.monster[i] = 1
                    continue
                
        for i in range(3):
            if self.magic[i] == 1:
                pa.click(x=565, y=820)
                time.sleep(0.3)
                pa.click(x=self.magic_pos[i][0], y=self.magic_pos[i][1])
                time.sleep(0.5)
                pos = imagesearch(folder+"action.png")
                if pos[0] != -1:
                    self.magic[i] = 0
                    continue
                  
        # pos = imagesearch(folder+"jingong.png")
        # if pos[0] != -1:
        #     self.opp_field = True
        # else:
        #     self.opp_field = False
    
    
if __name__ == "__main__":
    folder = "./image/"
    character = "bln"
    total_duel = 1
    if len(sys.argv) >= 2:
        total_duel = int(sys.argv[1])
    duel = autoDuel()
    duel.character = character
    if len(sys.argv) >= 3:
        duel.monster[0] = 1
        duel.monster[1] = 1
        duel.monster[2] = 1
        duel.magic[0] = 1
        duel.magic[1] = 1
        duel.magic[2] = 1
        duel.inDuel()
        duel.afterDuel()
        print("????????????")
    for i in range(1, total_duel + 1):
        print("???", i ,"?????????")
        duel.beforeDuel()
        duel.reset()
        duel.inDuel()
        duel.afterDuel()
        print("???", i ,"?????????")