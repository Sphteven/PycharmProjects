def main():
    score = float(input("Enter score: "))
    result = check_result(score)
    print(result )

def check_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

if __name__ == '__main__':
    main()