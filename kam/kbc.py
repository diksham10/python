class Questions:
    gk_questions = {
    "q1": {
        "question": "What is the capital city of Japan?\nA) Beijing\tB) Tokyo\nC) Seoul\tD) Bangkok",
        "answer": "B"
    },
    "q2": {
        "question": "Who wrote 'Romeo and Juliet'?\nA) Charles Dickens\tB) Leo Tolstoy\nC) William Shakespeare\tD) Mark Twain",
        "answer": "C"
    },
    "q3": {
        "question": "Which planet is known as the Red Planet?\nA) Mars\tB) Venus\nC) Jupiter\tD) Mercury",
        "answer": "A"
    },
    "q4": {
        "question": "Who is known as the Father of Computers?\nA) Isaac Newton\tB) Alan Turing\nC) Charles Babbage\tD) Albert Einstein",
        "answer": "C"
    },
    "q5": {
        "question": "What is the largest mammal in the world?\nA) African Elephant\tB) Blue Whale\nC) Giraffe\tD) Orca",
        "answer": "B"
    },
    "q6": {
        "question": "Which country is the largest by land area?\nA) Russia\tB) Canada\nC) China\tD) United States",
        "answer": "A"
    },
    "q7": {
        "question": "In which year did World War II end?\nA) 1942\tB) 1945\nC) 1950\tD) 1939",
        "answer": "B"
    },
    "q8": {
        "question": "What is the hardest natural substance on Earth?\nA) Diamond\tB) Gold\nC) Iron\tD) Quartz",
        "answer": "A"
    },
    "q9": {
        "question": "Who painted the Mona Lisa?\nA) Pablo Picasso\tB) Leonardo da Vinci\nC) Vincent van Gogh\tD) Michelangelo",
        "answer": "B"
    },
    "q10": {
        "question": "Which gas do plants absorb during photosynthesis?\nA) Oxygen\tB) Hydrogen\nC) Nitrogen\tD) Carbon Dioxide",
        "answer": "D"
    },
    "q11": {
        "question": "What is the currency of the United Kingdom?\nA) Dollar\tB) Pound Sterling\nC) Euro\tD) Yen",
        "answer": "B"
    },
    "q12": {
        "question": "Which continent is known as the 'Dark Continent'?\nA) Africa\tB) Asia\nC) Australia\tD) South America",
        "answer": "A"
    },
    "q13": {
        "question": "How many players are there in a cricket team?\nA) 10\tB) 11\nC) 12\tD) 9",
        "answer": "B"
    },
    "q14": {
        "question": "Which country gifted the Statue of Liberty to the USA?\nA) Germany\tB) Italy\nC) France\tD) Spain",
        "answer": "C"
    },
    "q15": {
        "question": "Who discovered gravity?\nA) Aristotle\tB) Isaac Newton\nC) Galileo Galilei\tD) Albert Einstein",
        "answer": "B"
    },
    "q16": {
        "question": "What is the smallest prime number?\nA) 1\tB) 2\nC) 3\tD) 5",
        "answer": "B"
    },
    "q17": {
        "question": "Which is the largest ocean?\nA) Atlantic Ocean\tB) Pacific Ocean\nC) Indian Ocean\tD) Arctic Ocean",
        "answer": "B"
    },
    "q18": {
        "question": "Who was the first person to walk on the moon?\nA) Buzz Aldrin\tB) Michael Collins\nC) Neil Armstrong\tD) Yuri Gagarin",
        "answer": "C"
    },
    "q19": {
        "question": "What is the boiling point of water at sea level (°C)?\nA) 50°C\tB) 100°C\nC) 80°C\tD) 120°C",
        "answer": "B"
    },
    "q20": {
        "question": "Which is the longest river in the world?\nA) Nile River\tB) Amazon River\nC) Yangtze River\tD) Mississippi River",
        "answer": "A"
    }
}


    def game(self):
        amount=0

        print("Kaoun banega crorepati")
        for i in range(1,21):
            sawal="q"+str(i)
            print(self.gk_questions[sawal]["question"])
            
            answer=input().upper().strip()

            if answer==self.gk_questions[sawal]["answer"]:
                amount+=500000
                print("Sahi jawaff")
            else:
                print("Galat jawaff")
                print(f"sahi jawaf tha: {self.gk_questions[sawal]["answer"]}")
                print(f"Aap ghar le ja rahe rahe he rs{amount}")
                return
        print(f"Aap ghar le ja rahe rahe he rs{amount}")
obj=Questions()
obj.game()