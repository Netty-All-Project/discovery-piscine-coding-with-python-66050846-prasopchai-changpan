# checkmate.py
# -----------------------------------
# ฟังก์ชันหลัก: checkmate(board)
# หน้าที่: รับ chessboard (string หลายบรรทัด) แล้วตรวจสอบว่า King (K) ถูกโจมตีหรือไม่
# ถ้าใช่ → print("Success")
# ถ้าไม่ใช่ → print("Fail")

def checkmate(board: str):
    """
    ฟังก์ชันนี้ตรวจสอบว่า King อยู่ในสถานะ in-check หรือไม่
    :param board: ตัวแปร string ที่แทน chessboard เช่น:
        "R...\n.K..\n..P.\n...."
    """
    # แปลง string ให้กลายเป็น list ของ list (matrix)
    grid = [list(row) for row in board.splitlines()]
    n = len(grid)   # ขนาดกระดาน (n x n)

    # หา King (K) อยู่ที่ตำแหน่งไหน
    king_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")  # ถ้าไม่มี K บนกระดาน → ถือว่าผิดพลาด
        return

    kx, ky = king_pos  # ตำแหน่ง King

    # -------------------------------
    # ฟังก์ชันตรวจสอบทิศทาง (ใช้กับ Rook, Bishop, Queen)
    def check_direction(dx, dy, attackers):
        """
        ตรวจสอบว่ามีตัวหมากที่สามารถเดินตรงตามทิศทาง dx, dy
        และเจอ King ได้โดยไม่มีหมากอื่นบังทาง
        """
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < n:
            if grid[x][y] != '.':  # เจอตัวหมาก
                return grid[x][y] in attackers
            x += dx
            y += dy
        return False

    # -------------------------------
    # 1) Pawn (P)
    # Pawn โจมตีทแยงไปข้างหน้า (ขึ้นบนกระดาน) = (kx-1, ky-1) และ (kx-1, ky+1)
    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = kx + dx, ky + dy
        if 0 <= x < n and 0 <= y < n and grid[x][y] == 'P':
            print("Success")
            return

    # -------------------------------
    # 2) Bishop (B) → เดินทแยง
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if check_direction(dx, dy, ['B', 'Q']):  # Bishop หรือ Queen
            print("Success")
            return

    # -------------------------------
    # 3) Rook (R) → เดินตรง
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if check_direction(dx, dy, ['R', 'Q']):  # Rook หรือ Queen
            print("Success")
            return

    # -------------------------------
    # 4) Queen (Q) → ตรวจไปแล้วรวมกับ Bishop/Rook

    # ถ้าไม่เจอใครโจมตี
    print("Fail")
