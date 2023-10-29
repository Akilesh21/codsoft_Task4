from django.shortcuts import render
import random

def index(request):
    return render(request, 'game.html')

def play(request):
    user_choice = request.POST.get('user_choice')
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    result = ''
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Scissors' and computer_choice == 'Paper') or
        (user_choice == 'Paper' and computer_choice == 'Rock')
    ):
        result = 'You win!'
    else:
        result = 'Computer wins!'

    return render(request, 'result.html', {'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result})
