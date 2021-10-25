from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def root():
    sonnets_file = open("sonnets.txt", "r") 
    sonnets_list = sonnets_file.read().split("\n\n")
    sonnets_file.close() 
    couplets = []
    for sonnet in sonnets_list:
        lines = sonnet.split("\n")
        if len(lines) != 14:
            continue
        couplets.append(tuple([lines[0], lines[2]]))
        couplets.append(tuple([lines[1], lines[3]]))
        couplets.append(tuple([lines[4], lines[6]]))
        couplets.append(tuple([lines[5], lines[7]]))
        couplets.append(tuple([lines[8], lines[10]]))
        couplets.append(tuple([lines[9], lines[11]]))
        couplets.append(tuple([lines[12], lines[13]]))
    final_sonnet = []
    couplet0 = random.choice(couplets)
    couplet1 = random.choice(couplets)
    couplet2 = random.choice(couplets)
    couplet3 = random.choice(couplets)
    couplet4 = random.choice(couplets)
    couplet5 = random.choice(couplets)
    couplet6 = random.choice(couplets)
    final_sonnet.append(couplet0[0])
    final_sonnet.append(couplet1[0])
    final_sonnet.append(couplet0[1])
    final_sonnet.append(couplet1[1])
    final_sonnet.append(couplet2[0])
    final_sonnet.append(couplet3[0])
    final_sonnet.append(couplet2[1])
    final_sonnet.append(couplet3[1])
    final_sonnet.append(couplet4[0])
    final_sonnet.append(couplet5[0])
    final_sonnet.append(couplet4[1])
    final_sonnet.append(couplet5[1])
    final_sonnet.append(couplet6[0])
    final_sonnet.append(couplet6[1])
    return "<br>".join(final_sonnet)