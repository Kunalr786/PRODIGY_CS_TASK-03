import re

def password_strength(password):
    strength = {
        'short': False,
        'no_upper': False,
        'no_lower': False,
        'no_digit': False,
        'no_special': False
    }

    # Check for minimum length
    if len(password) < 8:
        strength['short'] = True

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        strength['no_upper'] = True

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        strength['no_lower'] = True

    # Check for digits
    if not re.search(r'\d', password):
        strength['no_digit'] = True

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength['no_special'] = True

    # Calculate the final score
    score = 4 - sum([strength[key] for key in strength.keys()])

    # Return the result
    return {
        'score': score,
        'strength': 'Very weak' if score == 0 else 'Weak' if score == 1 else 'Moderate' if score == 2 else 'Strong' if score == 3 else 'Very strong',
        'details': strength
    }

if __name__ == '__main__':
    password = input('Enter your password: ')
    result = password_strength(password)
    print(f'Password strength: {result["strength"]} (Score: {result["score"]})')
    print('Details:')
    for key, value in result['details'].items():
        print(f'- {key.capitalize()}: {value}')