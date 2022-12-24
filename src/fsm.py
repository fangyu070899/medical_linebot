from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_searched_term(self, event):
        print("go to searched_term")

    def is_going_to_suggest_term(self, event):
        print("go to suggest_term")
    
    def is_going_to_symptom_category(self, event):
        print("go to symptom_category")
    
    def is_going_to_nutrition_category(self, event):
        print("go to nutrition_category")
    
    def is_going_to_diet_category(self, event):
        print("go to diet_category")
    
    def is_going_to_sport_category(self, event):
        print("go to sport_category")
    
    def is_going_to_disease_category(self, event):
        print("go to disease_category")
    
    def is_going_to_disease_category2(self, event):
        print("go to disease_category2")
    
    def is_going_to_disease(self, event):
        print("go to bone_disease")
    
    def is_going_to_symptom(self, event):
        print("go to male_symptom")