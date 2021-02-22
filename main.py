#importing files for run_output function
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art
import basics.output.escape_character as escape_character

# define function for choosing program from ouptput directory
def run_output():
    while(True):
        print("[a] Display Single Message program")
        print("[b] Display Multiline Message program ")
        print("[c] Display ASCII character program")
        print("[d] Display message with Toescape character program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/q")
        choice=input().lower().strip()
        if choice=="a":
            simple_message.run()
        elif choice=="b":
            multiline_message.run()
        elif choice=="c":
            ascii_art.run()
        elif choice=="d":
            escape_character.run()
        elif choice=="q":
            break
        else:
            print("Invalid option! Please try again.")
# importing files for run_input function
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.string_operator as string_operator
import basics.input.user_input as user_input
# define function for choosing programs from  input directory
def run_input():
    while(True):
        print("[a] Ascii Robot with dynamic eyes program")
        print("[b] Use of different data types program ")
        print("[c] Use of string operator program")
        print("[d] To read user input program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/q")
        choice=input().lower().strip()
        if choice=="a":
            ascii_robot.run()
        elif choice=="b":
            data_types.run()
        elif choice=="c":
            string_operator.run()
        elif choice=="d":
            user_input.run()
        elif choice=="q":
            break
        else:
            print("Invalid option! Please try again.")

#import files for run_nested_decision function
import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.nested_decision.nested as nested
# define function to choose program from nested_decision directory
def run_nested_decision():
    while (True):
        print("[a] use of multiple nested decision program")
        print("[b] use of nested decision program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/q")
        choice = input().lower().strip()
        if choice == "a":
            nestception.run()
        elif choice == "b":
            nested.run()
        elif choice == "q":
            break
        else:
            print("Invalid option! Please try again.")
#import files for run_simple_decision function
import basics.decisions.simple_decision.comparison_operators as comparison_operators
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.if1 as if1
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
# define function to choose program from simple_decision directory
def run_simple_decision():
    while (True):
        print("[a] comparison operator program")
        print("[b] counter program")
        print("[c] Use of if statement  program")
        print("[d] Use of if elif else program")
        print("[e] Use of if else program")
        print("[f] modular operator program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/e/f/q")
        choice = input().lower().strip()
        if choice == "a":
            comparison_operators.run()
        elif choice == "b":
            counter.run()
        elif choice == "c":
            if1.run()
        elif choice == "d":
            if_elif_else.run()
        elif choice == "e":
            if_else.run()
        elif choice == "f":
            modulo_operator.run()
        elif choice == "q":
            break
        else:
            print("Invalid option! Please try again.")
#import files for run_decision function
import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.review as review
# define function to choose directory/ program from decision directory
def run_decision():
    while(True):
        print("[a] open nested decision directory")
        print("[b] open simple decision directory")
        print("[c] and operator program")
        print("[d] or operator program")
        print("[e] review program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/e/q")
        choice=input().lower().strip()
        if choice=="a":
            run_nested_decision()
        elif choice=="b":
            run_simple_decision()
        elif choice=="c":
            and_operator.run()
        elif choice=="d":
            or_operator.run()
        elif choice=="e":
            review.run()
        elif choice=="q":
            break
        else:
            print("Invalid option! Please try again.")
#import files for for_loop
import basics.repetition.for_loop.characters as characters
import basics.repetition.for_loop.count_down as count_down
import basics.repetition.for_loop.range as range
import basics.repetition.for_loop.reverse as reverse
import basics.repetition.for_loop.simple as simple

#define function to choose program from for_loop directory
def run_for_loop():
    while (True):
        print("[a] string indexing program")
        print("[b] count_down program")
        print("[c] range program")
        print("[d] to reverse a string program")
        print("[e] simple program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/e/q")
        choice = input().lower().strip()
        if choice == "a":
            characters.run()
        elif choice == "b":
            count_down.run()
        elif choice == "c":
            range.run()
        elif choice == "d":
            reverse.run()
        elif choice == "e":
            simple.run()
        elif choice == "q":
            break
        else:
            print("Invalid option! Please try again.")
#import files for run_nested_loop
import basics.repetition.nested_loop.nested as nested
import basics.repetition.nested_loop.nesting as nesting

#define function to choose program from nested_loop directory
def run_nested_loop():
    while (True):
        print("[a] one loop nested in another program")
        print("[b] use of nested loop and decision program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/q")
        choice = input().lower().strip()
        if choice == "a":
            nested.run()
        elif choice == "b":
            nesting.run()
        elif choice == "q":
            break
        else:
            print("Invalid option! Please try again.")
#import files for run_while_loop function
import basics.repetition.while_loop.ascii as ascii
import basics.repetition.while_loop.count as count
import basics.repetition.while_loop.factorial as factorial
import basics.repetition.while_loop.len as len
import basics.repetition.while_loop.simple as simple
import basics.repetition.while_loop.sum_100 as sum_100
import basics.repetition.while_loop.sum_user_numbers as sum_user_numbers

#define function to choose program from while_loop directory
def run_while_loop():
    while (True):
        print("[a]  ascii with while-loop program")
        print("[b] counting with while-loop program")
        print("[c] To calculate factorial program")
        print("[d] use of len function program")
        print("[e] simple while-loop program")
        print("[f] To add first 100 numbers program")
        print("[g] to add numbers program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/e/f/g/q")
        choice = input().lower().strip()
        if choice == "a":
            ascii.run()
        elif choice == "b":
            count.run()
        elif choice == "c":
            factorial.run()
        elif choice == "d":
            len.run()
        elif choice == "e":
           simple.run()
        elif choice == "f":
          sum_100.run()
        elif choice == "g":
            sum_user_numbers.run()
        elif choice == "q":
            break
        else:
            print("Invalid option! Please try again.")

# define function to choose files/ directory from repetition directory
def run_repetition():
    while(True):
        print("[a] open for loop directory")
        print("[b] open nested loop directory")
        print("[c] open while loop directory")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/q")
        choice=input().lower().strip()
        if choice=="a":
            run_for_loop()
        elif choice=="b":
            run_nested_loop()
        elif choice=="c":
            run_while_loop()
        elif choice=="q":
            break
        else:
            print("Invalid option! Please try again.")
#import files for run_functions function
import basics.functions.simple_function as simple_function
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.function_calls as function_calls
import basics.functions.ascii_code as ascii_code
import basics.functions.ascii_character as ascii_character
import basics.functions.function_with_loop as function_with_loop
import basics.functions.multiple_function as multiple_function
import basics.functions.return_values as return_values

# define function to choose program from function directory
def run_functions():
    while(True):
        print("[a] use of abs, chr function program")
        print("[b] use of len, ord function program")
        print("[c] function calls program")
        print("[d] function with loop program")
        print("[e] function with nesting decision program")
        print("[f] function with parameter program")
        print("[g] function with parameters program")
        print("[h] return values program")
        print("[i] simple function program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/b/c/d/e/f/g/h/q")
        choice=input().lower().strip()
        if choice=="a":
            ascii_character.run()
        elif choice=="b":
            ascii_code.run()
        elif choice=="c":
            function_calls.run()
        elif choice=="d":
            function_with_loop.run()
        elif choice == "e":
            function_with_nesting.run()
        elif choice == "f":
            function_with_parameter.run()
        elif choice == "g":
            function_with_parameters.run()
        elif choice == "h":
            return_values.run()
        elif choice == "i":
            simple_function.run()
        elif choice=="q":
            break
        else:
            print("Invalid option! Please try again.")
#import file for modules funtion
import basics.modules.guess_the_number as guess_the_number
# define function to choose program from for modules directory
def run_modules():
    while(True):
        print("[a] Guess the Number program")
        print("[q] to quit")
        print(" please Enter which program you want to Execute")
        print(" press a/q")
        choice=input().lower().strip()
        if choice=="a":
            guess_the_number.run()
        elif choice=="q":
            break
        else:
            print("Invalid option! Please try again.")

#define function to choose from all options of basics directory
def run_block_a():
    while (True):

        print("[a] To run Output programs")
        print("[b] To run input programs")
        print("[c] To run decision programs")
        print("[d] To run repetition programs")
        print("[e] To run functions programs")
        print("[f] To run modules programs")
        print("[q] To quit")
        print("Which Programs you want to run . please press the right choice")
        print("press a/b/c/d/e/f/q")
        choice=input()
        if choice=="a":
            run_output()
        elif choice=="b":
            run_input()
        elif choice=="c":
            run_decision()
        elif choice=="d":
            run_repetition()
        elif choice=="e":
            run_functions()
        elif choice=="f":
            run_modules()
        elif choice=="q":
            break;
        else:
            print("Invalid option! Please try again.")
# define main function
def run():
    while (True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        print ("press a/q")
        response = input()
        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()
print("Thank Yor :)")