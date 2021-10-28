from calculator_factories import make_app,make_display, make_buttons, make_label
from class_calculator import Calculator

def main():
    app = make_app()
    display = make_display(app)
    label = make_label(app)
    buttons = make_buttons(app)
    calculator = Calculator(app, label,display,buttons)
    calculator.start()

if __name__ == '__main__':
    main()
