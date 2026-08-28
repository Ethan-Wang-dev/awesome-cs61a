"""Web server for the schememon GUI."""
import os

from gui_files.common_server import route, start

# Import scheme modules directly from student's project
from scheme import create_global_frame
from scheme_eval_apply import scheme_eval
from scheme_reader import scheme_read, buffer_lines
from scheme_utils import repl_str
from scheme_classes import SchemeError

PORT = 31416
DEFAULT_SERVER = "https://schememon.cs61a.org/"
GUI_FOLDER = "gui_files/"


class SchemeEvaluator:
    """
    A python class that uses the interpreter built in the scheme interpreter
    project to evaluate scheme expressions

    - __init__() creates a new SchemeEvaluator instance
    - evaluate() evaluates some scheme code along with a list of files
      containing scheme code
    """

    def __init__(self):
        """
        Instantiates a new Scheme Evaluator
        Initalizes a Scheme environment
        Creates a global frame
        """
        self.env = create_global_frame()

    def evaluate(self, filenames, code):
        """
        Evaluates scheme code using the python interpreter built from
        the scheme project. Returns the evaluation of the last line of
        the scheme code.

        - filename: the file that contains all of the base code
        - code: the code that is used to expand off of base code

        Example file (example.scm):
        ===========================
        (define (square n)
            (* n n)
        )

        (define (sum x y)
            (+ x y)
        )

        Then, SchemeEvaluator().evaluate("./example.scm", "(square 7)") would return 49.
        """
        try:
            all_code = ""

            for filename in filenames:
                with open(filename, 'r') as f:
                    file_content = f.read()
                    all_code += file_content + "\n"
            all_code += code
            lines = all_code.split('\n')
            src = buffer_lines(lines)
            results = []

            try:
                while True:
                    expression = scheme_read(src)
                    result = scheme_eval(expression, self.env)
                    results.append(result)
            except EOFError:
                pass
            return results
        except Exception as e:
            raise SchemeError(f"Error evaluating multiple expressions: {e}")


@route
def verify_scheme_question(scheme_problem, scheme_solution, test_cases, expected_results):
    """
    Verifies whether your given solution code for a scheme statement question is correct.

    For every test case, the API will use SchemeEvaluator to evaluate the statement. If any testcase
    does not pass, then the API will set correct to False, and True otherwise.
    """
    try:
        evaluator = SchemeEvaluator()
        result = evaluator.evaluate(["questions.scm"], f"(solution-code (quote {scheme_problem}) (quote {scheme_solution}))")
        scheme_code = repl_str(result[-1])

        for i in range(0, len(test_cases)):
            test_case = test_cases[i]
            expected_result = expected_results[i]
            code = scheme_code + "\n\n" + test_case
            result = evaluator.evaluate([], code)[-1]

            # SPECIAL COMMENT: Python uses "True" and "False", but Scheme uses "#t" and "#f"
            # This takes care of the "in" procedure case

            if str(result) == "True":
                result = "#t"
            elif str(result) == "False":
                result = "#f"

            if str(result) != expected_result:
                return {"correct": False}

        return {"correct": True}
    except Exception as e:
        print(f"ERROR in verify_scheme_question: {e}")
        import traceback
        traceback.print_exc()
        return {"correct": False}


if __name__ == "__main__" or "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
    app = start(PORT, DEFAULT_SERVER, GUI_FOLDER)