def checkmate(board: str):
    grid = [list(row) for row in board.splitlines()]
    n = len(grid)   

    king_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    kx, ky = king_pos  # ตำแหน่ง King
    # Find (K):     #
    # . . . . . . . #
    # . . . . . . . #
    # . . . . . . . #
    # . . . . . K . #

    # ฟังก์ชันตรวจสอบทิศทาง (ใช้กับ Rook, Bishop, Queen)
    def check_direction(dx, dy, attackers):
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < n:
            if grid[x][y] != '.':  # เจอตัวหมาก
                return grid[x][y] in attackers
            x += dx
            y += dy
        return False

    # 1) Pawn (P)                                                                               
    # Pawn โจมตีทแยงไปข้างหน้า (ขึ้นบนกระดาน)                                                    # Pawn (P):     #
    for dx, dy in [(1, -1), (1, 1)]:                                                         # . . . . . . . #
        x, y = kx + dx, ky + dy                                                              # . . X . X . . #
        if 0 <= x < n and 0 <= y < n and grid[x][y] == 'P':                                  # . . . P . . . #
            print("Success")                                                                 # . . . . . . . #
            return                                                                           # . . . . . . . #

    # 2) Bishop (B) → เดินทแยง                                                                # Bishop (B):   #
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:                                      # . X . . . X . #
        if check_direction(dx, dy, ['B', 'Q']):  # Bishop หรือ Queen                          # . . X . X . . #
            print("Success")                                                                 # . . . B . . . #
            return                                                                           # . . X . X . . #
                                                                                             # . X . . . X . #
                                                                                             
    # 3) Rook (R) → เดินตรง                                                                   # Rook (R):     #
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:                                        # . . . X . . . #
        if check_direction(dx, dy, ['R', 'Q']):  # Rook หรือ Queen                            # . . . X . . . #
            print("Success")                                                                 # X X X R X X X #
            return                                                                           # . . . X . . . #
                                                                                             # . . . X . . . #
                                                                                             
    # -------------------------------                                                        # Queen (Q)     #
    # 4) Queen (Q) → ตรวจไปแล้วรวมกับ Bishop/Rook                                              # . X . X . X . #                                   
                                                                                             # . . X X X . . #
                                                                                             # X X X Q X X X #
                                                                                             # . . X X X . . #
                                                                                             # . X . X . X . #                                                                    
    print("Fail")                                                                            
                                                                                            
                                                                                            