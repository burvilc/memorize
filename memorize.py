#!env python3

from termcolor import colored
import logging
import click
import click_log


class Text:

    def __init__(self):
        self.verse_text = "凡事謙虛、溫柔、忍耐，用愛心彼此寬容"
        self.verse = "Ephesians 4:2"
        self.error_count = 0

    def match_character(self, user_guess, actual_value):
        if not user_guess:
            return False
        elif user_guess == actual_value:
            print(colored(user_guess, 'green'), end=' ', flush=True)
            return True
        else:
            print(colored(actual_value, 'red'), end=' ', flush=True)
            self.error_count = self.error_count + 1
            return False
        return False

    def practice(self):
        ref_chars = [*self.verse_text]
        for ref_char in ref_chars:
            guess = input("Please enter a character:")
            while self.match_character(guess, ref_char):
                pass
        # log stats, don't mark as pass until >90%


# Main function
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
)
click_log.basic_config(logger)


@click.command()
@click_log.simple_verbosity_option(logger)
def main():
    TextToMemorize = Text()
    TextToMemorize.practice()


if __name__ == "__main__":
    main()

'''

function LogSession () {
    # log start time, date
}

function GetVerse () {
    # pull from Bible API
}

#get input from text file
#put into array of characters
function GetTextToMemorize () {

}
'''
