def mad_libs():
    print("Welcome to Mad Libs!")
    
    # Inputs from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    
    # Mad Libs story
    story = f"Once upon a time, a {adjective} {noun} {verb} {adverb}. The end."
    
    print("\nHere is your Mad Libs story:")
    print(story)

# Calling the function
mad_libs()
