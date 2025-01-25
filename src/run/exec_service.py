import multiprocessing
import io
import sys
import itertools

def run_code_in_sandbox(code, output_queue):
    """
    Executes code in an isolated environment.
    The execution result is sent to a queue.
    """
    allowed_globals = {
        "__builtins__": {"print": print, "__import__": __import__},
        "functools": itertools,
    }

    output = io.StringIO()
    sys.stdout = output

    try:
        exec(code, allowed_globals)
    except Exception as e:
        output_queue.put(f"error: {e}")
    else:
        output_queue.put(output.getvalue())
    finally:
        sys.stdout = sys.__stdout__

def execute_with_limits(code, timeout: int):
    """Runs code with restrictions."""
    output_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=run_code_in_sandbox, args=(code, output_queue))

    process.start()
    process.join(timeout=timeout)

    if process.is_alive():
        process.terminate()
        return "Execution time exceeded!"

    if not output_queue.empty():
        return output_queue.get()

    return "The code terminated without output."

