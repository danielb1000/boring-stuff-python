def isValidChessBoard(board):
    valid_positions = [f'{col}{row}' for row in '12345678' for col in 'abcdefgh']
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    piece_count = {'w': 0, 'b': 0} 
    king_count = {'w': 0, 'b': 0}  
    pawn_count = {'w': 0, 'b': 0}  

    # check if every position given is valid
    for position, piece in board.items():
        if position not in valid_positions:
            return False
        
        # 1st char has to be either 'w' or 'b'. rest of the string needs to be a valid piece
        # eg. "wbishop" - piece[0] is w - piece[1:] is bishop
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            return False

        color = piece[0]  # 'w' or 'b'
        piece_type = piece[1:] # 'king', 'bishop', etc

        piece_count[color] += 1

        if piece_type == 'king':
            king_count[color] += 1

        if piece_type == 'pawn':
            pawn_count[color] += 1

    # needs exactly 1 king of each color
    if king_count['w'] != 1 or king_count['b'] != 1:
        return False

    # 16 total pieces each maxmimum
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False

    # 8 pawns each maximum
    if pawn_count['w'] > 8 or pawn_count['b'] > 8:
        return False

    return True

chess_board = {
    'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop',
    'h5': 'bqueen', 'e3': 'wking', 'h8': 'bbishop'
}

print(isValidChessBoard(chess_board))  
