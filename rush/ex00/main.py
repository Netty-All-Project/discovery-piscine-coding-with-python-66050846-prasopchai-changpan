from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1
    board1 = """\
R...
.K..
..P.
...."""
    print("Board 1: ", end='')
    checkmate(board1)

    # ตัวอย่างที่ 2
    board2 = """\
R...
.K..
....
...."""
    print("Board 2: ", end='')
    checkmate(board2)
    
    # ตัวอย่างที่ 3
    board3 = """\
.K.Q
....
....
.B.."""
    print("Board 3: ", end='')
    checkmate(board3)
    
    # ตัวอย่างที่ 4
    board4 = """\
..Q.
P...
....
.B.."""
    print("Board 4: ", end='')
    checkmate(board4)

if __name__ == "__main__":
    main()
