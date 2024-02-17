if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

first = max(scores)
second = max([i for i in scores if i!=first])
indices = [i for i, x in enumerate(scores) if x == second]
selected_names = []
for i in indices:
    selected_names.append(names[i])
for name in sorted(selected_names):
    print(name)
    

    

