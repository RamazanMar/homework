class Candidate():
    def __init__(self, first_name,last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name =  first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name 

    @classmethod
    def generate_candidates(cls, filename):
        f = open(filename, "r")    
        ans = []
        header = True
        for line in f:
            if header:
                header = False
                continue
            params = line.split(",")
            params[3] = list(params[3].split("|"))
            name, surname = params[0].split(" ")
            print(params)
            ans += [cls(name, surname, *params[1:])]
        f.close()
        return ans

c = Candidate.generate_candidates("list_candidates.txt") 
print(c[0].full_name) 
