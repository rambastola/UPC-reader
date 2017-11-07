
import turtle

def translate_left(num):
    """
    converts user's input to its binary numbers for the left sides of barcode.

    :param num: user input
    :return: a list of binary for each input
    """

    left = {0: "0001101", 1:"0011001", 2:"0010011", 3:"0111101", 4:"0100011",
             5:"0110001", 6:"0101111",7:"0111011", 8:"0110111",9:"0001011" }

    new_list = []

    for i in num:
        if i in left.keys():
            i = left[i]

            new_list.append(i)

    return new_list

def translate_right(z):
    """
    converts user's input to its binary numbers for the right side of the barcode.

    :param z: user input
    :return: list of binary numbers for user's input
    """

    right = {0:"1110010", 1:"1100110", 2:"1101100", 3:"1000010", 4:"1011100", 5:"1001110",
             6:"1010000", 7:"1000100", 8:"1001000", 9:"1110100"}

    list2 = []
    for i in z:
        if i in right.keys():
            i = right[i]

            list2.append(i)
    return list2

def drawing(left, right, lamo):
    """
    draw lines for UPC barcode

    :param left: binary for the left side of barcode
    :param right: binary for the right side of barcode
    :return: nothing. program ends here.
    """

    drawlines = turtle.Turtle()
    drawlines.speed(0)
    drawlines.pensize(1)
    wn = turtle.Screen()
    drawlines.penup()
    drawlines.goto(-100, 0)
    drawlines.pendown()
    side_guard = ["1", "0", "1"]
    mid = ["0", "1", "0", "1", "0"]
    for i in side_guard:
        line(i, drawlines, 70)

    for t in left:
        for q in t:
            line(q, drawlines, 50)

    for i in mid:
        for a in i:
            line(a, drawlines, 70)
    for t in right:

        for w in t:
            line(w, drawlines, 50)
    for i in side_guard:
        line(i, drawlines, 70)

    drawlines.penup()
    drawlines.goto(-100, -100)
    drawlines.pendown()

    drawlines.write(lamo, font=("Arial", 26, "normal"))

    wn.exitonclick()

def line(a, drawlines, height):
    """

    draw lines for barcode
    :param a: individual numbers of list
    :param drawlines: turtle that draws
    :param height: height of the lines
    :return: n/a, print's out on turtle window
    """

    if a == "1":
        drawlines.pendown()
    else:
        drawlines.penup()

    drawlines.left(90)
    drawlines.backward(height)

    drawlines.forward(height)
    drawlines.right(90)

    drawlines.penup()
    drawlines.fd(1)
    drawlines.pendown()

def digit_12_check(x):
    """

    check if the input is 12 digits and if they are all numbers
    :param x: input
    :return: input
    """

    while len(x) != 12 or x.isdigit() == False:
        x = input("Enter valid 12 digits UPC number: ")

    return x

def create_list(a):

    """
    Solves to check the UPC is valid.

    :param x: list
    :return: valid list
    """

    empty_list = []

    for i in a:
        empty_list.append(int(i))


    odd = 0
    a = 0
    for i in range(6):
        odd += empty_list[a]
        a += 2

    add = odd * 3

    even_sum = 0
    d = 1
    for i in range(5):
        even_sum += empty_list[d]
        d += 2

    total = add + even_sum

    # check modulus
    newtotal = total % 10
    if newtotal != 0:
        newtotal = 10 - newtotal

    if newtotal == empty_list[-1]:

        return empty_list

    elif newtotal != empty_list[-1]:

        #print error msg on turtle

        bond = turtle.Turtle()
        wn = turtle.Screen()
        bond.write("This is not a valid UPC number. Try again with correct UPC number.")
        wn.mainloop()

def main():

    user = input("Enter 12 digits UPC number: ")

    checked = digit_12_check(user)

    user = create_list(checked)

    le = translate_left(user)

    ri = translate_right(user)

    drawing(le, ri, checked)


main()
