program = ''
report = ''
i = 1
check = 0
ch_over = 0  

for str_old in text_in.splitlines():

    m_list = ["+", "-", "*", "/", "%"]
    for math in m_list:
        if math in str_old:
            ch_over = -1
            #program += "//SolChk Example use external checkcode.  Use SafeMath\n" 
            #break

    if "import" in str_old and "SafeMath" in str_old:
        ch_over = 1

    program += str_old + "\n"
    i += 1
if ch_over == -1:
    program += "//SolChk Example use external checkcode.  Use SafeMath\n" 
    report += "\n Example use external checkcode.  Use SafeMath"
text_out = program
