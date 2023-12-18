import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MathProblemForm
from .models import MathProblem
from sympy import symbols, Integral, simplify, latex, parse_expr, solve
from sympy.parsing.latex import parse_latex
from sympy.integrals.manualintegrate import integral_steps


def solve_latex_input(latex_input):
    x = symbols('x')

    try:
        sympy_expression = parse_expr(str(parse_latex(latex_input)), transformations='all')
        print(sympy_expression)

        # Check if the expression is an integration problem
        if isinstance(sympy_expression, Integral):
            # Perform numerical integration with the 'manual' strategy
            solution = sympy_expression.doit()
            # Extract and format the steps involved in the manual integration
            strategy_steps = integral_steps(sympy_expression, x).__str__
            # strategy_steps_to_string = [step.rule for step in strategy_steps]

            result = {
                'latex_input': latex(sympy_expression),
                'numerical_solution': solution,
                'solution_strategy': strategy_steps
            }
        else:
            result = {'error': 'Not an integration problem'}

        return result

    except Exception as e:
        print(e)
        return {'error': str(e)}

def math_problem_solver(request):
    result = None

    # test_latex_input = r'\int_{0}^{1} x^2 \,dx'
    # result = solve_latex_input(test_latex_input)
    # form = MathProblemForm()
    form = MathProblemForm()
    if request.method == 'POST':
        form = MathProblemForm(request.POST)
        if form.is_valid():
            latex_input = form.cleaned_data['latex_input']
            print("input: " + repr(latex_input))
            result = solve_latex_input(latex_input)

    return render(request, 'index.html', {'form': form, 'result': result})