import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def letter_combinations(digits):
    if not digits:
        logger.debug("Proper input not given")
        return []

    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(index, path):
        logger.debug(f"Backtrack at {index} with path {path}")
        
        if index == len(digits):
            combination = ''.join(path)
            combinations.append(combination)
            logger.debug(f"Combination found: {combination}")
            return
        
        current_digit = digits[index]
        logger.debug(f"Current digit: {current_digit} maps to letters: {mapping[current_digit]}")
        
        for letter in mapping[current_digit]:
            path.append(letter)
            logger.debug(f"Added letter: {letter}, new path: {path}")
            backtrack(index + 1, path)
            path.pop()
            logger.debug(f"Backtracked, new path: {path}")

    combinations = []
    logger.debug(f"Starting letter combinations with digits: {digits}")
    backtrack(0, [])
    logger.debug(f"All combinations found: {combinations}")
    return combinations

digits = input("Enter digits from 2 to 9 inclusive: ")
result = letter_combinations(digits)
logger.info(f"Final output: {result}")
