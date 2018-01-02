import p_ws

def get_rotk(chapter = 120):
    root = "https://zh.wikisource.org/zh-hans/%E4%B8%89%E5%9C%8B%E6%BC%94%E7%BE%A9/%E7%AC%AC"
    term = "%E5%9B%9E"
    body_open = ["却说","且说", "词曰"]
    if chapter < 10:
        root += '00'
        index = chapter
        rotk = c_webstring(root, index, term)
        rotk.extract_all(body_open, "分解")
        rotk.clean_all()
        return rotk
    
    else: 
        root_temp = root + '00'
        index = 9
        rotk = c_webstring(root_temp, index, term)
        rotk.extract_all(body_open, "分解")

    if (chapter > 9 and chapter < 100):
        root = root + '0'
        index = chapter
        rotk.modify(root, chapter) 
        rotk.extract_all(body_open, "分解")
        rotk.clean_all()        
        return rotk
    
    else:
        root_temp = root + "0"
        index = 99
        rotk.modify(root_temp, index) 
        rotk.extract_all(body_open, "分解")     
        
    if chapter < 120:
        index = chapter
        rotk.modify(root, index) 
        rotk.extract_all(body_open, "分解")        
    
    else:
        index = 119 # Cap at 119
        rotk.modify(root, index) 
        rotk.extract_all(body_open, "分解")           
        
        rotk.modify(root, 120) # 120th chapter is special case
        rotk.extract_all(body_open, "后人凭吊空牢骚")
        rotk.clean_all()     
        return rotk
        
if __name__ == '__main__':
    rotk = get_rotk()
