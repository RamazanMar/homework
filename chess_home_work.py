def check_on_board(position):
    if len(position) == 2:
        if position[0] in range(8) and position[1] in range(8):
            return True
    return False 

def filter_on_board(positions):
    return [p for p in positions if check_on_board(p)]


class Chess:
    colors = ["black", "white"]

    def __init__(self, color, position):
        assert color in self.colors 
        assert check_on_board(position)
        self.color = color
        self.position = position

    def switch_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def move(self, new_position):
        if check_on_board(new_position):
            self.position = new_position

    def potentional_moves(self):
        pass

    def check_move(self, new_position):
        return new_position in self.potentional_moves()   


class Pawn(Chess):
    def potentional_moves(self):
        ans = []
        if self.color == "white":
            ans += [(self.position[0], self.position[1]+1)]
        else:
            ans += [(self.position[0], self.position[1]-1)]
        return filter_on_board(ans)
    

class Horse(Chess):
    def potentional_moves(self):
        ans = []
        for shift in [(1,2),(2,1)]:
            for i in [1,-1]:
                for j in [1,-1]:
                    ans += [(self.position[0]+i*shift[0], self.position[1]+j*shift[1])]
        return filter_on_board(ans)
    

class Bishop(Chess):  
    def potentional_moves(self):
        ans = []
        for shift in range(1,8):
            for i in [1,-1]:
                for j in [1,-1]:
                    ans += [(self.position[0]+i*shift, self.position[1]+j*shift)]
        return filter_on_board(ans)
    

class Rook(Chess):  
    def potentional_moves(self):
        ans = []
        for shift in range(1,8):
            for i in [1,-1]:
                ans += [(self.position[0]+i*shift, self.position[1])]
                ans += [(self.position[0], self.position[1]+i*shift)]
        return filter_on_board(ans)
    

class Queen(Chess):  
    def potentional_moves(self):
        ans = []
        for shift in range(1,8):
            for i in [1,-1]:
                ans += [(self.position[0]+i*shift, self.position[1])]
                ans += [(self.position[0], self.position[1]+i*shift)]
        for shift in range(1,8):
            for i in [1,-1]:
                for j in [1,-1]:
                    ans += [(self.position[0]+i*shift, self.position[1]+j*shift)]
        return filter_on_board(ans)   


class King(Chess):
    def potentional_moves(self):
        ans = []
        for i in [1,-1]:
            ans += [(self.position[0]+i, self.position[1])]
            ans += [(self.position[0], self.position[1]+i)]
        for i in [1,-1]:
            for j in [1,-1]:
                ans += [(self.position[0]+i, self.position[1]+j)]
        return filter_on_board(ans)  

def check_who_can_get(pieces, position):
    return [p for p in pieces if position in p.potention_moves()]