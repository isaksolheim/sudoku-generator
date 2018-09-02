##SUDOKU GENERATOR####
from random import choice

def main():
    def empty_square():
        square = []

        for x in range(3):
            square.append([" "] * 3)
        return square

    table = [empty_square() for x in range(9)]
    def table_print():
        
        for row in range(3):
            for square in range(3):
                if square == 2:
                    print(table[square][row])
                else:
                    print(table[square][row], end = "")
        
        print("---------------------------")
        for row in range(3):
            for square in range(3,6):
                if square == 5:
                    print(table[square][row])
                else:
                    print(table[square][row], end = "")
        print("---------------------------")    
        for row in range(3):
            for square in range(6,9):
                if square == 8:
                    print(table[square][row])
                else:
                    print(table[square][row], end = "")




    def valid_check(square, row, num):
        if square in range(3):
            sqrs = range(3)
        elif square in range(3,6):
            sqrs = range(3,6)
        else:
            sqrs = range(6,9)

        numbers = [1,2,3,4,5,6,7,8,9]

        # check square
        counter = 0
        x = 0
        while counter != 50:
            if x == 3:
                x = 0
            else:
                pass

            number = choice(numbers)
            if number in table[square][x]:
                numbers.remove(number)
            else:
                pass
            counter += 1
            x += 1
            
        number = choice(numbers)

        #check row
        counter = 0
        while counter != 50:
            if len(numbers) == 0:
                number = 0
                break

            else:
                for sqr in sqrs:
                    if number in table[sqr][row]:
                        numbers.remove(number)
                    else:
                        pass
                    if len(numbers) == 0:
                        number = 0
                        break
                    else:
                        number = choice(numbers)
                counter += 1

        if len(numbers) == 0:
            number = 0
        else:
            number = choice(numbers)

        #check column

        """
        for x in range(3):
            for y in range(3):
                if number == table[x][y][num]:
                    numbers.remove(number)
                else:
                    pass
                if len(numbers) == 0:
                    number = 0
                    break
                else:
                    number = choice(numbers)
        x += 3
        """
        cen1 = [0, 3, 6]
        cen2 = [1, 4, 7]
        cen3 = [2, 5, 8]

        if square in cen1:
            counter = 0
            while counter != 50:
                test1 = 0
                for x in range(3):
                    if len(numbers) == 0:
                        number = 0
                        break
                    else:
                        for y in range(3):
                            if number == table[test1][y][num]:
                                numbers.remove(number)
                            else:
                                pass
                            if len(numbers) == 0:
                                number = 0
                                break
                            else:
                                number = choice(numbers)
                        test1 += 3
                counter += 1

        elif square in cen2:
            counter = 0
            while counter != 50:
                test1 = 1
                for x in range(3):
                    if len(numbers) == 0:
                        break
                    else:
                        for y in range(3):
                            if number == table[test1][y][num]:
                                numbers.remove(number)
                            else:
                                pass
                            if len(numbers) == 0:
                                number = 0
                                break
                            else:
                                number = choice(numbers)
                        test1 += 3
                counter += 1
        else:
            counter = 0
            while counter != 50:
                test1 = 2
                for x in range(3):
                    if len(numbers) == 0:
                        break
                    else:
                        for y in range(3):
                            if number == table[test1][y][num]:
                                numbers.remove(number)
                            else:
                                pass
                            if len(numbers) == 0:
                                number = 0
                                break
                            else:
                                number = choice(numbers)
                        test1 += 3
                counter += 1

        return(number)



    def sudoku():
        numbers = [[1,2,3,4,5,6,7,8,9] for x in range(9)]
        num = 0
        row = 0
        square = 0
        

        for x in range(81):
            if num == 3:
                num = 0
                row += 1
            
            if row == 3:
                row = 0
                square += 1

            """
            number = choice(numbers[square])
            table[square][row][num] = number
            numbers[square].remove(number)
            """

            number = valid_check(square, row, num)
            table[square][row][num] = number
            if x != 80: 
                num += 1
            else:
                pass

    sudoku()

    """
    for x in range(9):
        for y in range(3):
            if 0 in table[x][y]:
                sudoku()
            else:
                pass
    """
    table_print()
if __name__ == "__main__":
    main()
