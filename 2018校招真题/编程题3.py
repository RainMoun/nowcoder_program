class Idea:
    def __init__(self, id_, pm_id, propose_time, grade, need_time):
        self.id_ = id_
        self.pm_id = pm_id
        self.propose_time = propose_time
        self.grade = grade
        self.need_time = need_time
        self.last_time = need_time
        self.coder_id = None


idea_time_dict = {}
n, m, p = map(int, input().strip().split())
for i in range(p):
    idea_message = list(map(int, input().strip().split()))
    idea = Idea(i, idea_message[0], idea_message[1], idea_message[2], idea_message[3])
    if idea_message[1] not in idea_time_dict.keys():
        idea_time_dict[idea_message[1]] = [idea]
    else:
        idea_time_dict[idea_message[1]].append(idea)
time = 1
finished_time = [-1 for _ in range(p)]
ongoing_idea = []
wait_idea = []
coder_busy = [0 for _ in range(m)]
while True:
    if time in idea_time_dict.keys():
        wait_idea.extend(idea_time_dict[time])
        wait_idea = list(sorted(wait_idea, key=lambda x: (x.grade, x.need_time, x.id_)))
    temp_ongoing_idea = ongoing_idea[:]
    for idea in ongoing_idea:
        idea.last_time -= 1
        if idea.last_time == 0:
            coder_busy[idea.coder_id] = 0
            finished_time[idea.id_] = time
            temp_ongoing_idea.remove(idea)
    ongoing_idea = temp_ongoing_idea[:]
    for i in range(len(coder_busy)):
        if coder_busy[i] == 0:
            if wait_idea:
                idea = wait_idea.pop(0)
                idea.coder_id = i
                ongoing_idea.append(idea)
                coder_busy[i] = 1
    if -1 not in finished_time:
        break
    time += 1
for i in finished_time:
    print(i)