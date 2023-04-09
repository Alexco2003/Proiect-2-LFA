def read_grammar(file_name):
    #Reads a regular grammar from the given file and returns it as a dictionary
    grammar = {}
    with open(file_name, "r") as f:
        for line in f:
            #Split the line into the left side (ls) and right side (rs) of the rule
            parts = line.strip().split("->")
            ls = parts[0].strip()
            rs = parts[1].strip().split("|")

            #Add the rs to the grammar dictionary under the ls key
            if ls not in grammar:
                grammar[ls] = []
            for rule in rs:
                grammar[ls].extend(rule.split())

    return grammar


def accepts(grammar, symbol, word):
    #Verifies if the given word is accepted by the given regular grammar starting from the given symbol (the first symbol will always be 'S' in this implementation)

    if not word:
        #If the word is empty, check if the symbol can produce the empty string ('lambda' in our case).
        #A symbol can produce the empty string if it is in the grammar and has a production rule that generates the empty string.
        return 'lambda' in grammar[symbol]

    if len(word) == 1:
        #If the word has only one letter left, check if the symbol can produce the last letter (if the last letter is a terminal state)
        last_letter = word[0]
        for transition in grammar[symbol]:
            if len(transition) == 1 and transition[0] == last_letter:
                return True

    #If the word has more than one letter, check if there is a transition from the symbol to another state that can produce the rest of the word recursively
    for transition in grammar[symbol]:
        if len(transition) > 1 and transition[0] == word[0]:
            if accepts(grammar, transition[1], word[1:]):
                return True

    #If none of the above conditions apply, the word is not accepted by the grammar
    return False

grammar = read_grammar(input("Enter the Regular Grammar file name : ").strip())
symbol = 'S'
word = input("Enter a word: ")
if accepts(grammar, symbol, word):
    print(f"The word '{word}' is accepted by the grammar.")
else:
    print(f"The word '{word}' is not accepted by the grammar.")