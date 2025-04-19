import io
import contextlib


def run_user_code(code: str) -> str:
    output = io.StringIO()
    try:
        compile(code, '<string>', 'exec')
        
        local_variables = {}
        with contextlib.redirect_stdout(output):
            
            exec(code, {'__builtins__': __builtins__}, local_variables)
        return output.getvalue() or "No output generated"
    
    except SyntaxError as e:
        return f"Syntax error: {e.msg} at line {e.lineno}, column {e.offset}"
    except AttributeError as e:
        return f"AttributeError: {str(e)}"
    except Exception as e:
        return f"Runtime error: {type(e).__name__}: {str(e)}"