var ask = prompt("Welcome! Please enter the number of the shape for which you would like to calculate the perimeter. Your options are: \n 1.Rectangle/Square \n 2.Triangle\n 3.Circle \n 4.Parallelogram.")

if (ask == 1) {
    l = prompt("Please enter the length of the rectangle.")
    b = prompt("Please enter the breadth of the rectangle.")
    r_Result = (Number(l) + Number(b)) * 2
    alert("The perimeter of the given rectangle is " + r_Result)
}

else if (ask == 2) {
    s1 = prompt("Please enter the length of the triangle's first side.")
    s2 = prompt("Please enter the length of the triangle's second side.")
    b = prompt("Please enter the length of the triangle's base.")
    t_result = Number(s1) + Number(s2) + Number(b)
    alert("The perimeter of the given rectangle is " + t_result)
}

else if (ask == 3) {
    d = prompt("Please enter the diameter of the circle.")
    c_Result = Number(d) * 3.14
    alert("The perimeter of the given circle is " + c_result)
}

else if (ask == 4) {
    h = prompt("Please enter the height of the parallelogram.")
    ba = prompt("Please enter the base of the parallelogram.")
    p_Result = (Number(h) + Number(ba)) * 2
    alert("The perimeter of this parallelogram is " + p_Result)
}