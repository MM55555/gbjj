pp:str = ""

def py_exec(phr:str):
    '''
    string값 받아와서 exec함수에 집어넣고 돌리는 목적인데,,
    함수 안에서 실행되는 거라서 , 실행하자 마자 주소가 풀리는듯
    '''
    global pp
    pp = None
    exec(phr, globals())

def test_func(a):
    print(a)

def printw(*items, sep='', end='<br>'):
    '''
    printw( convertable_to_string1, ..., sep = '', end='<br>')
    py_exe에서 웹으로 출력할때 사용하는 것. 웹용 print
    반환값이 있어도 소용이 없으니(exec안에서 밖으로 꺼낼 수가 없음)
    이 모듈의 글로벌 변수에 출력값을 저장한다.
    '''
    global pp #사용할 글로벌 변수
    result_list = []

    for item in items:
        result_list.append(str(item))

    result_str = sep.join(result_list)

    if( pp == None ):
        pp = ""
        pp += result_str + end
    else:
        pp += result_str + end