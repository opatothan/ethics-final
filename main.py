from story_processors import build_story

story_file = "data/updated_story.json"

total_score = 0
total_money = 5000

difficulty = 1

TITLE_TEXT = """
    ________  __    _              ______                             _    __                   ______            __
   / ____/ /_/ /_  (_)_________   / ____/___ _____ ___  ___     _    | |  / /__  _______  __   / ____/_  ______  / /
  / __/ / __/ __ \/ / ___/ ___/  / / __/ __ `/ __ `__ \/ _ \   (_)   | | / / _ \/ ___/ / / /  / /_  / / / / __ \/ / 
 / /___/ /_/ / / / / /__(__  )  / /_/ / /_/ / / / / / /  __/  _      | |/ /  __/ /  / /_/ /  / __/ / /_/ / / / /_/  
/_____/\__/_/ /_/_/\___/____/   \____/\__,_/_/ /_/ /_/\___/  (_)     |___/\___/_/   \__, /  /_/    \__,_/_/ /_(_)   
                                                                                /____/                           
"""
INSTRUCTION_TEXT = """
This is a \"choose your own adventure\" style game where you will be thrust into many different ethical situations as a software engineer.
Choose wisely! Your choices will impact your final score at the end. Try your best to be \"ethical\"

You start out with cash, and if you run out, you will be evicted and die of starvation. Future actions may earn money.
Every action will cost 1000 dollars, representing living costs.

Make too many mistakes, and the game will end.
Some choices that are particularly catastrophic will end the game immediately.

Enter \"quit\" to exit the game
"""

DEATH_MESSAGE = """
You have gone broke and died of starvation on the streets of San Francisco. Your dreams of living the dream life of a software engineer die with you.
Try again?
"""

LOW_FUNDS_MESSAGE = """
You are quickly running out of funds. You will die soon if you do not earn more money.
"""

ETHICAL_BLUNDER_MSG = """
You have performed a serious ethical violation. Congratulations. Your score will suffer.
"""

BAR = """
==========================================================================================
"""


def prompt_user_input(n):
    while True:
        try:
            user_input = input(f"Enter a number between 1 and {n}: ")
            if user_input == "quit":
                quit()
            user_input = int(user_input)
            if 1 <= user_input <= n:
                return user_input-1
            else:
                print(f"Error: The number must be between 1 and {n}. Try again.")
        except ValueError:
            print("Error: Please enter a valid integer. Try again.")


if __name__ == "__main__":
    print(TITLE_TEXT)
    print(INSTRUCTION_TEXT)

    print("Now Playing: ", story_file)
    print()

    cur_event = build_story(story_file)

    while True:
        print(BAR)
        print(f"Current Cash: {total_money}")
        cur_event.display()
        num_choices = cur_event.get_num_choices()
        if cur_event.get_num_choices() == 0:
            break
        selection = prompt_user_input(num_choices)
        score, cur_event, income = cur_event.select_choice(selection)
        total_score += score
        if income>0:
            print(f"You have earned ${income}!")
        total_money += income
        total_money -= 1000
        if total_money <= 0:
            print(DEATH_MESSAGE)
            break
        elif total_money <= 3000:
            print(LOW_FUNDS_MESSAGE)


        
    
    
    print("The game has ended, thank you for playing!")
    print(f"Your final score was: {total_score}")
    print(f"You ended with: ${total_money}")




            
