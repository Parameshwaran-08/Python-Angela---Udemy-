print(f"The love calculator is calculating your score !")

name1 = input("Enter your name : ").lower()
name2 = input("Enter your partner name : ").lower()
name = name1 + name2

t_count = name.count("t")
r_count = name.count("r")
u_count = name.count("u")
e_count = name.count("e")

true_total = t_count + r_count + u_count + e_count

l_count = name.count("l")
o_count = name.count("o")
v_count = name.count("v")

love_total = l_count + o_count + v_count + e_count

love_score = int(str(true_total) + str(love_total))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} - ass")

elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score} - piss")

else:
    print(f"Your score is {love_score} - die")