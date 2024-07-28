# -------------------------------
def new_game():
    guesses = []
    correct = 0
    question_num = 1 

    for key in questions:
        print('----------------------')
        print(key)
        for i in opitions[question_num-1]:
            print(i)
        guess = input('enter A,B,C or D: ')
        guess = guess.upper()
        guesses.append(guess)

        correct += check_answer(questions.get(key),guess)
        question_num += 1

    
    display_score(correct,guesses)

# -------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print('correct')
        return 1
    else:
        print('wrong')
        return 0
# -------------------------------
def display_score(correct,guesses):
    print('-------------------')
    print('results')
    print('-------------------')
    print('answers: ',end='')
    for i in questions:
        print(questions.get(i),end=' ')
    print()

    print('guesses: ',end='')
    for i in guesses:
        print(i,end=' ')

    score = int((correct/len(questions))*100)
    print('you score is '+str(score)+'%')
# -------------------------------
def play_again():
    response = input('jogar dnv? ')
    response = response.upper()

    if response == 'S':
        return True
    else:
        return False
# -------------------------------

questions = {
    'qm criou o python? ' : 'A',
    'em q ano o python foi criado? ' : 'B',
    'python é mencionado em qual comedia? ' : 'C',
    'a terra é redonda? ' : 'A'
}

opitions = [
    ['a. guido' , 'b.batman' , 'c.robin' , 'd.elon musk'],
    ['a.sla' , 'b.nsei','c.tb','d.ola'],
    ['a.sla' , 'b.nsei','c.tb','d.ola'],
    ['a.sla' , 'b.nsei','c.tb','d.ola']
]

new_game()

while play_again():
    new_game()

print('flwwwww')