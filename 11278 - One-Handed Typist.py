

def solve(inp: str):
    qwerty = '4567890-=' + 'qwertyuiop[]/'  + 'asdfghjkl;\'' + 'zxcvbnm,./'
    qwerty += '$%^&*()_+' + 'QWERTYUIOP{}|' + 'ASDFGHJKL:"' + 'ZXCVBNM<>?'
    dvorak = 'qjlmfp/[]' + '456.orsuyb;-\\' + '789aehtdck-'  + '0zx,inwvg\''
    dvorak += 'QJLMFP?{}' + '$%^>ORSUYB:+|' + '&*(AEHTDCK_' + ')ZX<INWVG"'

    translation_table = str.maketrans(qwerty, dvorak)

    print(inp.translate(translation_table))


if __name__ == '__main__':
    try:
        while True:
            solve(input())
    
    except EOFError:
        pass