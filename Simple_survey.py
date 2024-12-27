#SIMPLE SURVEY

class Survey:
    def __init__(self, questions):
        self.questions = questions
        self.responses = {}
        
    def conduct_survey(self):
        print("Starting the survey...")
        for question in self.questions:
            response = input(question + " ") 
            self.responses[question] = response
            
        print("Survey completed ")
        
    def display_results(self):
        print("Survey Results:")
        for question, response in self.responses.items():
            print(f"{question}: {response}")
            
def main():
    questions = [
        "What is your name?", 
        "How old are you?", 
        "What is your favorite color?"
        ]
    survey = Survey(questions)
    
    while True:
        print("\n Survey Menu ")
        print("1. Conduct survey ")
        print("2. Display results ")
        print("3. Exit ")
        
        ch = int(input("Enter your choice : "))
        if ch == 1:
            survey.conduct_survey()
        elif ch == 2:
            survey.display_results()
        elif ch == 3:
            print("Exiting the survey...")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()