# main.py
# -----------------------------------
# main program ที่เอาไว้รันทดสอบ checkmate

from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1
    board1 = """\
R...
.K..
..P.
...."""
    checkmate(board1)

    # ตัวอย่างที่ 2
    board2 = """\
..
.K"""
    checkmate(board2)

if __name__ == "__main__":
    main()
