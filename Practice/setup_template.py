import

def setup_template():
    pag.hotkey('win', 'r')
    pag.typewrite('file_location')
    pag.press('enter')  
    time.sleep(0.5)
    pag.hotkey('ctrl', 'a')
    pag.hotkey('ctrl', 'c')
    webbrowser.open("page_address")
    time.sleep(2)
    pag.moveTo(4012, 139, 0.5)
    pag.click()
    pag.moveTo(4012, 223, 0.5)
    pag.click()
    time.sleep(2)
    pag.moveTo(3730, 186, 0.5)
    pag.click()
    pag.moveTo(3834, 135, 0.5)
    pag.click()
    pag.moveTo(3834, 228, 0.5)
    pag.click()
    pag.moveTo(2694, 337, 0.5)
    pag.click()
    time.sleep(0.5)
    pag.hotkey('ctrl', 'v')
    pag.moveTo(3783, 136, 0.5)
    pag.click()
    pag.moveTo(3783, 183, 0.5)
    pag.click()
