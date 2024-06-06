import psycopg2
#connecting to db
conn = psycopg2.connect(database = "postgres",
                        user = "postgres",
                        host = 'localhost',
                        password = "postgres",
                        port = 5432)

cur = conn.cursor()


#starting the game
def starting () -> None:
    print("Hello, Welcome to my Quiz Game!")

    name = input("Please Enter Your Name: ")

    playing =input("Do you want to play with me,"+name.title()+ "? (yes/no): ")

    if playing.lower() != "yes":
        print("Okay, maybe next time!")
        quit()


def view() -> list:
    conn = psycopg2.connect(database = "postgres",
                        user = "postgres",
                        host = 'localhost',
                        password = "postgres",
                        port = 5432)
    cur = conn.cursor()
    cur.execute("SELECT * FROM questiondb")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_valid_in(ans: str) -> str:
    answer: str = input(ans)
    if len(answer) < 100 and answer.isalpha():
        return answer
    else:
        return print("Invalid input,please only use alphabet letters less than 100 characters")
    

def main() -> None:
    score = 0
    questions = view()
    for question in questions:
        print(question[1])
        answer = get_valid_in("Your answer: ")
        if answer.lower() == question[2].lower():
            print("Correct!")
            score += 5
        else:
            print("Incorrect. The correct answer is " + question[2])
    return print(f"Your total score is {score} from 20 possible score")
        

if __name__ == '__main__':  
    starting()
    main()
