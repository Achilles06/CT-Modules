import mood_responses
import text_utils as tu
if __name__ == "__main__":
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))

    sample_string = input("Enter a string: ")

    reversed_string = tu.reverse_string(sample_string)
    capitalized_string = tu.capitalize_string(sample_string)

    print(f"Reversed String: {reversed_string}")
    print(f"Capitalized String: {capitalized_string}")