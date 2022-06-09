import time
import keyboard
import pyautogui as pya

spotsDict = {
        'All Upgrades' : (0, 0),
        'Wiz towers' : (0, 0),
        'SHOW GRIMOIRE' : (0, 0),
        'FTHOF' : (0, 0),
        'Legacy' : (0, 0),
        'Reincarnate' : (0, 0)
        }

# Tab function
def altTabTo(window):
    if window == 'last':
        pya.hotkey('alt', 'tab')
    else:
        pya.getWindowsWithTitle(window)[0].minimize()
        pya.getWindowsWithTitle(window)[0].maximize()
            
for item in spotsDict:
    print('In your game, move your cursor where the Buy '+ item + ' button is.'
          '\nWhen ready, press \'Spacebar\' to record Buy '+ item + ' button\'s position in your screen.')
    print('Press \'Enter\' to alt-tab to Cookie Clicker.\n\t>')
    input()
    altTabTo('Cookie Clicker')
    done = False
    while not done:
        if keyboard.is_pressed('space'):
            x, y = pya.position()
            spotsDict[item]= x, y
            print(item +' button\'s location saved!\n\n')
            done = True
            altTabTo('last')
        if keyboard.is_pressed('q'):
            pya.moveTo(0, 0, duration = 0)
            
altTabTo('Cookie Clicker')
pya.moveTo(spotsDict['Reincarnate'], duration = 0)
pya.click()
pya.press('enter')
time.sleep(1)

taimer = 0
check = False

while not check:
    check = False 
    pya.moveTo(spotsDict['All Upgrades'], duration = 0)
    time.sleep(1)
    pya.click()
    pya.moveTo(spotsDict['Wiz towers'], duration = 0)
    time.sleep(0.5)
    pya.click()
    pya.moveTo(spotsDict['SHOW GRIMOIRE'], duration = 0)
    time.sleep(0.5)
    pya.click()
    pya.moveTo(spotsDict['FTHOF'], duration = 0)
    check = True
    taimer = 0
    while taimer < 10 and check == True:
        if keyboard.is_pressed('space'):
            check = False
        time.sleep(1)
        taimer = taimer + 1
    if not check:        
        pya.moveTo(spotsDict['Legacy'], duration = 0)
        pya.click()
        time.sleep(0.5)
        pya.press('enter')
        time.sleep(0.5)
        pya.press('esc')
        pya.moveTo(spotsDict['Reincarnate'], duration = 0)
        pya.click()
        pya.press('enter')
        time.sleep(1)    