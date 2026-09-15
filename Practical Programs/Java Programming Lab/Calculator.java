import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;

public class Calculator implements ActionListener {
    Frame frame;
    TextField display;
    Button[] digitButtons = new Button[10];
    Button add, subtract, multiply, divide, clear, equalTo;
    double num1, num2, result;
    char operator;

    public Calculator() {
        frame = new Frame("Calculator");

        display = new TextField();
        display.setEditable(false);
        display.setFont(new Font("Arial", Font.BOLD, 25));
        frame.add(display, BorderLayout.NORTH);

        Panel panel = new Panel();
        panel.setLayout(new GridLayout(4, 4));
        for (int i = 0; i <= 9; i++) {
            digitButtons[i] = new Button(String.valueOf(i));
            digitButtons[i].addActionListener(this);
        }

        add = new Button("+");
        subtract = new Button("-");
        multiply = new Button("*");
        divide = new Button("/");
        equalTo = new Button("=");
        clear = new Button("C");

        add.addActionListener(this);
        subtract.addActionListener(this);
        multiply.addActionListener(this);
        divide.addActionListener(this);
        equalTo.addActionListener(this);
        clear.addActionListener(this);

        panel.add(digitButtons[7]);
        panel.add(digitButtons[8]);
        panel.add(digitButtons[9]);
        panel.add(divide);

        panel.add(digitButtons[4]);
        panel.add(digitButtons[5]);
        panel.add(digitButtons[6]);
        panel.add(multiply);

        panel.add(digitButtons[1]);
        panel.add(digitButtons[2]);
        panel.add(digitButtons[3]);
        panel.add(subtract);

        panel.add(digitButtons[0]);
        panel.add(equalTo);
        panel.add(add);
        panel.add(clear);

        frame.add(panel, BorderLayout.CENTER);

        frame.setSize(400, 400);
        frame.setVisible(true);
    }

    @Override 
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        
        try {
            if(command.charAt(0) >= '0' && command.charAt(0) <= '9') {
                display.setText(display.getText() + command);
            } 
            
            else if (command.equals("C")) {
                display.setText("");
                num1 = 0;
                num2 = 0;
                result = 0;
            } 
            
            else if (
                command.equals("/") ||
                command.equals("*") ||
                command.equals("+") ||
                command.equals("-")
            ) {
                num1 = Double.parseDouble(display.getText());
                operator = command.charAt(0);
                display.setText("");
            } 
            
            else if (command.equals("=")) {
                num2 = Double.parseDouble(display.getText());

                switch(operator) {
                    case '+':
                        result = num1 + num2;
                        break;
                    case '-':
                        result = num1 - num2;
                        break;
                    case '*':
                        result = num1 * num2;
                        break;
                    case '/':
                        if(num2 == 0) {
                            throw new ArithmeticException("Cannot divide by zero");
                        }

                        result = num1 / num2;
                        break;
                }

                display.setText(String.valueOf(result));
            }

        } catch (ArithmeticException ex) {
            JOptionPane.showMessageDialog(
                frame,
                ex.getMessage(),
                "Arithmetic Error",
                JOptionPane.ERROR_MESSAGE
            );

            display.setText("");
        }
    }

    public static void main(String[] args) {
        new Calculator();
    }
}